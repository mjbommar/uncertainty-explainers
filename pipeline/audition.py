"""The same two sentences in each candidate narrator, verified, measured and priced.

``uv run python -m pipeline.audition`` writes ``build/audition/<model>/<voice>-<n>.wav``
and ``build/audition/audition.json``; ``docs/MODELS.md`` records the numbers.
"""

from __future__ import annotations

import asyncio
import json
import shutil

from bc_gen import GenCache, OpenAITranscribe, SpeechVerifier, generate_verified

from . import CACHE, ROOT
from .spec import VoiceSpec
from .speech import MeteredTranscriber, backend_for, request_for

SENTENCES = (
    "Risk is a gamble whose odds you know, like a fair coin that lands heads half the time.",
    "Uncertainty is different: nobody can tell you the odds, so a forecast of 70 percent means less than it seems.",
)
VOICES = ("Charon", "Schedar", "Sadaltager")
MODELS = ("gemini-3.8-flash-tts", "gemini-3.1-flash-tts-preview")


async def run() -> list[dict]:
    cache = GenCache(CACHE)
    out = ROOT / "build" / "audition"
    rows = []
    for model in MODELS:
        for voice in VOICES:
            spec = VoiceSpec(model=model, voice=voice)
            backend = backend_for(spec)
            for n, text in enumerate(SENTENCES, 1):
                ear = MeteredTranscriber(OpenAITranscribe())
                verifier = SpeechVerifier(ear)
                req = request_for(spec, text)
                res = await generate_verified(backend, req, cache=cache, verifier=verifier, rerolls=2)
                dest = out / model / f"{voice}-{n}.wav"
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(res.path, dest)
                heard = ear.heard[-1] if ear.heard else None
                if heard is None:  # cache hit: hear it once for the record
                    heard = (await ear.transcribe(res.path)).text
                wer = verifier.score(req.text, heard).score
                secs = res.receipt.duration_s or 0.0
                rows.append(
                    {
                        "model": model,
                        "voice": voice,
                        "sentence": n,
                        "seconds": round(secs, 2),
                        "wpm": round(len(text.split()) / secs * 60, 1) if secs else None,
                        "wer": round(wer or 0.0, 3),
                        "attempts": res.receipt.attempts,
                        "cost_usd": res.receipt.cost_usd,
                        "asr_usd": round(ear.cost_usd, 5),
                        "heard": heard,
                        "path": str(dest.relative_to(ROOT)),
                    }
                )
                print(json.dumps(rows[-1]))
            await backend.aclose()
    (out / "audition.json").write_text(json.dumps(rows, indent=1) + "\n")
    return rows


if __name__ == "__main__":
    asyncio.run(run())
