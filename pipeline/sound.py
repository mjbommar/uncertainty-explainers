"""Sound effects through ElevenLabs and an optional Lyria bed, all via ``bc_gen``.

Cues are a small reusable library: each is a prompt and an explicit duration,
so the same cue is one cached generation across every video. A segment can
also prompt a one-off effect. ``SoundVerifier`` checks each file's duration
before it is cached; receipts are copied beside the video's assets.

The music bed is a Lyria 30-second clip, looped seamlessly by
``bc_audio.ffmpeg.seamless_bed`` in the mix. Any failure there (no
``google-genai``, no access, a refusal) is logged and the video is built
without a bed rather than stopped.
"""

from __future__ import annotations

import asyncio
import shutil
from dataclasses import dataclass
from pathlib import Path

from bc_gen import ElevenLabsSound, GenCache, Lyria, MusicRequest, SoundRequest, generate_verified

from . import CACHE
from .spec import MusicSpec, SfxSpec, Video

__all__ = ["LIBRARY", "Cue", "SfxResult", "generate_bed", "generate_sfx"]


@dataclass(frozen=True, slots=True)
class Cue:
    prompt: str
    seconds: float
    influence: float = 0.55


_DRY = "Clean studio recording, no music, no voice, no reverb tail, no background noise."
LIBRARY: dict[str, Cue] = {
    "whoosh": Cue(f"A soft, airy whoosh passing from left to right, gentle and short. {_DRY}", 1.0),
    "soft_click": Cue(f"A single soft, muted interface click, like a felt-tipped key. {_DRY}", 0.5),
    "paper": Cue(f"A single sheet of heavy paper slid across a wooden desk. {_DRY}", 1.0),
    "tick": Cue(f"One quiet wooden tick, like a clock escapement, dry and close. {_DRY}", 0.5),
    "low_pad": Cue(
        "A warm, low synthesizer pad swelling in and fading out, calm and cinematic, no melody, no percussion.",
        4.0,
        0.4,
    ),
    "marbles": Cue(f"A handful of glass marbles dropped gently into a ceramic jar, settling. {_DRY}", 1.6),
    "chime": Cue(f"A single soft glass chime, bright and clean, fading quickly. {_DRY}", 1.2),
}


@dataclass(frozen=True, slots=True)
class SfxResult:
    label: str
    path: Path
    seconds: float
    cost_usd: float | None
    cached: bool
    receipt: Path


def request_for(fx: SfxSpec) -> tuple[str, SoundRequest]:
    if fx.cue is not None:
        cue = LIBRARY[fx.cue]
        return fx.cue, SoundRequest(prompt=cue.prompt, seconds=cue.seconds, prompt_influence=cue.influence)
    assert fx.prompt is not None and fx.duration is not None
    return "custom", SoundRequest(prompt=fx.prompt, seconds=fx.duration, prompt_influence=0.55)


def _copy(cache: GenCache, key: str, dest_dir: Path, label: str) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{label}-{key[:12]}.json"
    shutil.copyfile(cache.receipt_path(key), dest)
    return dest


async def _sfx_async(video: Video, receipts: Path) -> dict[str, SfxResult]:
    cache = GenCache(CACHE)
    backend = ElevenLabsSound()
    wanted: dict[str, tuple[str, SoundRequest]] = {}
    for seg in video.segments:
        for fx in seg.sfx:
            label, req = request_for(fx)
            wanted[backend.key(req)] = (label, req)
    out: dict[str, SfxResult] = {}
    try:
        for key, (label, req) in wanted.items():
            res = await generate_verified(backend, req, cache=cache, rerolls=2, stage=f"sfx:{label}")
            out[key] = SfxResult(
                label,
                res.path,
                float(res.receipt.duration_s or req.seconds),
                res.cost_usd,
                res.cached,
                _copy(cache, res.key, receipts, f"sfx-{label}"),
            )
    finally:
        await backend.aclose()
    return out


def generate_sfx(video: Video, receipts: Path) -> dict[str, SfxResult]:
    """Every effect the script names, keyed by the bc-gen cache key of its request."""
    return asyncio.run(_sfx_async(video, receipts))


def sfx_key(fx: SfxSpec) -> str:
    return ElevenLabsSound().key(request_for(fx)[1])


async def _bed_async(spec: MusicSpec, receipts: Path) -> SfxResult:
    cache = GenCache(CACHE)
    backend = Lyria()
    req = MusicRequest(prompt=spec.prompt, kind="clip", instrumental=True)
    # A clip has no requested minutes, so the default SoundVerifier checks that audio came back.
    res = await generate_verified(backend, req, cache=cache, rerolls=1, stage="music")
    return SfxResult(
        "music",
        res.path,
        float(res.receipt.duration_s or 30.0),
        res.cost_usd,
        res.cached,
        _copy(cache, res.key, receipts, "music"),
    )


def generate_bed(video: Video, receipts: Path) -> tuple[SfxResult | None, str | None]:
    """The bed, or ``(None, reason)`` when there is none; never raises."""
    if video.music is None or not video.music.enabled:
        return None, "no music in the script"
    try:
        return asyncio.run(_bed_async(video.music, receipts)), None
    except Exception as exc:  # the bed is optional by design
        return None, f"{type(exc).__name__}: {str(exc)[:300]}"
