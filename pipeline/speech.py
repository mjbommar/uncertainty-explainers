"""Narration: one verified, cached, receipted clip per segment.

Gemini 3.1 TTS models go through ``bc_gen.GeminiSpeech`` unchanged. Gemini
3.8 TTS models cannot: 3.8 reads its text "strictly as a verbatim transcript"
(Google's speech-generation guide), so bc-gen's anti-answer wrapper is spoken
aloud (measured: the ASR round trip heard the wrapper and not the script), the
model refuses a system instruction, and it returns a RIFF WAV rather than raw
PCM. :class:`GeminiStyledSpeech` is therefore a ``bc_gen.ProviderBackend``
subclass that posts to the interactions endpoint with the delivery in
``speech_metadata.style``. Everything else (cache key, receipt, retry, price
ladder, verify-then-cache) is bc-gen's. It is recorded in
``docs/PRODUCTION-LOG.md`` as a candidate for bc-gen.

Every clip passes ``SpeechVerifier`` (ASR round trip: WER, numbers, quotes)
before it is cached. The verifier's own transcription spend is not in bc-gen's
receipts, so :class:`MeteredTranscriber` counts it.
"""

from __future__ import annotations

import asyncio
import base64
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from bc_gen import (
    NOTATION,
    GeminiSpeech,
    GenCache,
    OpenAITranscribe,
    ProviderBackend,
    SpeechRequest,
    SpeechVerifier,
    VerificationFailed,
    generate_verified,
    strip_markdown,
)
from bc_gen.models import Request
from bc_gen.retry import GenError
from bc_gen.speech import audio_duration
from bc_gen.transcribe import Transcript

from . import CACHE
from .spec import Segment, Video, VoiceSpec

__all__ = [
    "ClipResult",
    "GeminiStyledSpeech",
    "MeteredTranscriber",
    "backend_for",
    "request_for",
    "speakable",
    "synthesize",
]

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta"


class GeminiStyledSpeech(ProviderBackend):
    """Gemini 3.8 TTS through ``/v1beta/interactions`` with ``speech_metadata.style``."""

    provider = "google"
    kind = "speech"
    env_keys = ("GEMINI_API_KEY", "GOOGLE_API_KEY")

    def __init__(self, model: str = "gemini-3.8-flash-tts", **kw: Any) -> None:
        kw.setdefault("timeout_s", 300.0)
        super().__init__(model, **kw)

    def params(self, request: Request) -> dict[str, Any]:
        data = request.params()
        data["endpoint"] = "interactions"
        data["style_field"] = "speech_metadata.style"
        return data

    def estimate(self, request: Request) -> float | None:
        assert isinstance(request, SpeechRequest)
        return self.pricing.speech(self.qualified_model, characters=len(request.text))

    async def _call(self, request: Request) -> tuple[bytes, str, dict[str, Any]]:
        assert isinstance(request, SpeechRequest)
        content: dict[str, Any] = {"type": "text", "text": request.text}
        if request.instructions:
            content["annotations"] = [{"type": "speech_metadata", "style": request.instructions}]
        body = {
            "model": self.model,
            "input": [{"type": "user_input", "content": [content]}],
            "response_format": {"type": "audio"},
            "generation_config": {"speech_config": [{"voice": request.voice}]},
        }
        response = await self._post(
            f"{GEMINI_BASE_URL}/interactions", headers={"x-goog-api-key": self.api_key()}, json=body
        )
        payload = response.json()
        found = _find_audio(payload)
        if found is None:
            raise GenError(
                f"gemini interactions: no audio in response: {response.text[:600]}",
                provider=self.provider,
                body=response.text,
            )
        data, mime = found
        usage = payload.get("usage") or {}
        meta: dict[str, Any] = {
            "mime_type": mime,
            "interaction_id": payload.get("id", ""),
            "prompt_tokens": int(usage.get("total_input_tokens") or 0),
            "output_tokens": int(usage.get("total_output_tokens") or 0),
        }
        if "wav" not in mime:
            raise GenError(f"gemini interactions: expected audio/wav, got {mime}", provider=self.provider)
        return data, "wav", meta

    def _actual_cost(self, request: Request, meta: dict[str, Any], path: Path) -> tuple[float | None, dict[str, float]]:
        assert isinstance(request, SpeechRequest)
        seconds = audio_duration(path)
        units: dict[str, float] = {"characters": float(len(request.text))}
        if seconds is not None:
            meta["duration_s"] = seconds
            units["seconds"] = seconds
        if meta.get("output_tokens"):
            units["input_tokens"] = float(meta["prompt_tokens"])
            units["output_tokens"] = float(meta["output_tokens"])
            cost = self.pricing.speech_usage(
                self.qualified_model,
                input_tokens=int(meta["prompt_tokens"]),
                output_tokens=int(meta["output_tokens"]),
            )
            if cost is not None:
                return cost, units
        return self.pricing.speech(self.qualified_model, characters=len(request.text), seconds=seconds), units


def _find_audio(payload: Any) -> tuple[bytes, str] | None:
    """The interactions response carries audio under ``steps[].content[]`` or ``output_audio``."""
    if isinstance(payload, dict):
        audio = payload.get("output_audio")
        if isinstance(audio, dict) and audio.get("data"):
            return base64.b64decode(audio["data"]), str(audio.get("mime_type", "audio/wav"))
        for step in payload.get("steps", []) or []:
            for item in (step.get("content") or []) if isinstance(step, dict) else []:
                if isinstance(item, dict) and item.get("type") == "audio" and item.get("data"):
                    return base64.b64decode(item["data"]), str(item.get("mime_type", "audio/wav"))
        for item in payload.get("outputs", []) or []:
            if isinstance(item, dict) and item.get("type") == "audio" and item.get("data"):
                return base64.b64decode(item["data"]), str(item.get("mime_type", "audio/wav"))
    return None


class MeteredTranscriber:
    """Wraps a transcriber, counting what the verifier spent and what it heard."""

    def __init__(self, inner: Any) -> None:
        self.inner = inner
        self.name = f"metered:{getattr(inner, 'name', 'transcriber')}"
        self.cost_usd = 0.0
        self.calls = 0
        self.heard: list[str] = []

    async def transcribe(self, path: Path, *, words: bool = False) -> Transcript:
        t = await self.inner.transcribe(path, words=words)
        self.calls += 1
        self.cost_usd += float(t.cost_usd or 0.0)
        self.heard.append(t.text)
        return t


def speakable(text: str) -> str:
    """What the engine is sent: markdown stripped, notation read aloud (bc-gen's rules)."""
    return NOTATION.apply(strip_markdown(text)).strip()


def backend_for(voice: VoiceSpec) -> ProviderBackend:
    if voice.model.startswith("gemini-3.8"):
        return GeminiStyledSpeech(voice.model)
    return GeminiSpeech(voice.model)


def request_for(voice: VoiceSpec, text: str, direction: str | None = None) -> SpeechRequest:
    style = voice.style if not direction else f"{voice.style} For this line: {direction.strip()}"
    return SpeechRequest(text=speakable(text), voice=voice.voice, instructions=style, format="wav")


@dataclass(frozen=True, slots=True)
class ClipResult:
    segment: str
    path: Path
    seconds: float
    cost_usd: float | None
    cached: bool
    attempts: int
    tolerated: bool
    wer: float | None
    receipt: Path


def _copy_receipt(cache: GenCache, key: str, dest_dir: Path, label: str) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    src = cache.receipt_path(key)
    dest = dest_dir / f"{label}-{key[:12]}.json"
    shutil.copyfile(src, dest)
    return dest


def paced(src: Path, out_dir: Path) -> Path:
    """A verified clip, with long pauses shortened and a mild tempo lift (spec.PACE_*).

    Deterministic transform of the verified file, keyed by its name and the
    parameters, so a changed setting can never serve a stale file. The engine's
    own read is what the receipt scored; this runs after that gate, as
    understanding-accounting's ``media/shorts/pace.py`` does.
    """
    from bc_audio import ffmpeg as ff

    from .spec import PACE_MAX_PAUSE_S, PACE_PAUSE_S, PACE_TEMPO, PACE_THRESHOLD_DB

    tag = f"{PACE_MAX_PAUSE_S}-{PACE_PAUSE_S}-{PACE_THRESHOLD_DB}-{PACE_TEMPO}"
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / f"{src.stem}-paced-{tag}.wav"
    if dest.exists():
        return dest
    keep = PACE_PAUSE_S
    filt = (
        f"silenceremove=stop_periods=-1:stop_duration={PACE_MAX_PAUSE_S}:stop_threshold={PACE_THRESHOLD_DB}dB"
        f":stop_silence={keep},atempo={PACE_TEMPO}"
    )
    ff._run([ff.binary(), "-v", "error", "-y", "-i", str(src), "-af", filt, "-ar", "48000", "-ac", "1", str(dest)])
    return dest


async def _one(
    backend: ProviderBackend, seg: Segment, voice: VoiceSpec, cache: GenCache, receipts: Path, rerolls: int
) -> tuple[ClipResult, MeteredTranscriber]:
    ear = MeteredTranscriber(OpenAITranscribe())
    verifier = SpeechVerifier(ear)
    request = request_for(voice, seg.say, seg.direction)
    try:
        result = await generate_verified(
            backend, request, cache=cache, verifier=verifier, rerolls=rerolls, stage=f"narration:{seg.id}"
        )
    except VerificationFailed as exc:
        raise VerificationFailed(exc.key, [f"segment {seg.id}", *exc.failures], attempts=exc.attempts) from exc
    wer = verifier.score(request.text, ear.heard[-1]).score if ear.heard else None
    path = paced(result.path, receipts.parent / "paced") if voice.pace else result.path
    seconds = audio_duration(path) if path is not result.path else (result.receipt.duration_s or audio_duration(path))
    receipt = _copy_receipt(cache, result.key, receipts, f"narration-{seg.id}")
    return (
        ClipResult(
            segment=seg.id,
            path=path,
            seconds=float(seconds or 0.0),
            cost_usd=result.cost_usd,
            cached=result.cached,
            attempts=result.receipt.attempts,
            tolerated=result.receipt.tolerated,
            wer=wer,
            receipt=receipt,
        ),
        ear,
    )


async def synthesize_async(
    video: Video, receipts: Path, *, rerolls: int = 3, concurrency: int = 4
) -> tuple[list[ClipResult], float]:
    """Every segment's clip, in order; returns the clips and the verifier's ASR spend."""
    cache = GenCache(CACHE)
    backend = backend_for(video.voice)
    gate = asyncio.Semaphore(concurrency)

    async def bounded(seg: Segment) -> tuple[ClipResult, MeteredTranscriber]:
        async with gate:
            return await _one(backend, seg, video.voice, cache, receipts, rerolls)

    try:
        pairs = await asyncio.gather(*(bounded(s) for s in video.segments))
    finally:
        await backend.aclose()
    return [p[0] for p in pairs], sum(p[1].cost_usd for p in pairs)


def synthesize(video: Video, receipts: Path, **kw: Any) -> tuple[list[ClipResult], float]:
    return asyncio.run(synthesize_async(video, receipts, **kw))
