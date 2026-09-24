"""Voice against direction: does the guidance or the voice make the read flat?

Same three lines, verified, in a grid of (model, voice, direction). Measures
what understanding-accounting's audition measured: words a minute, loudness
range (95th minus 20th percentile of voiced 100 ms RMS frames), median f0 and
the semitone spread of the pitch track. Writes ``build/audition2/``.
"""

from __future__ import annotations

import asyncio
import json
import shutil
import sys

import numpy as np
from bc_gen import GenCache, OpenAITranscribe, SpeechVerifier, generate_verified
from bc_signal import pitch_summary, track

from . import CACHE, ROOT
from .spec import HOUSE_STYLE, VoiceSpec
from .speech import MeteredTranscriber, backend_for, request_for

LINES = (
    "In 1937, John Maynard Keynes drew a similar line, with examples. Roulette, he wrote, is not uncertain in his sense.",
    "Most people would rather draw from Urn Two, whether they bet on red or on black. The two chances would add up to less than one.",
    "The officer who wrote it meant about three in ten. The readers heard approval.",
)

# understanding-accounting's gemini-enceladus casting, verbatim (media/audio/voices.yaml).
UA_ENCELADUS = (
    "Speak in a neutral American accent. You are narrating a short explainer video with "
    "medium energy: unhurried, about 150 words per minute, deeper and more intimate than a "
    "presenter. Low, warm, slightly gravelly, as if you are a touch too close to the "
    "microphone, speaking to one listener. Keep real dynamic range: lift a little on "
    "questions and setups, then settle lower and slower to land the key term or the number. "
    "Never breathy, never a hype voice, never a whisper. Crisp consonants, firm sentence "
    "endings, short pauses."
)
DIRECTIONS = {"ua": UA_ENCELADUS, "flat": HOUSE_STYLE}
GRID = [
    ("gemini-3.8-flash-tts", "Enceladus", "ua"),
    ("gemini-3.8-flash-tts", "Enceladus", "flat"),
    ("gemini-3.8-flash-tts", "Charon", "ua"),
    ("gemini-3.8-flash-tts", "Charon", "flat"),
    ("gemini-3.1-flash-tts-preview", "Enceladus", "ua"),
    ("gemini-3.8-flash-tts", "Sadaltager", "ua"),
]


def _wav(path) -> tuple[np.ndarray, int]:
    from bc_audio import wav_read

    x, sr = wav_read(str(path))
    x = np.asarray(x, dtype=np.float32)
    return (x.mean(axis=0) if x.ndim == 2 else x), sr


def measure(path) -> dict:
    x, sr = _wav(path)
    hop = int(sr * 0.1)
    frames = np.array([np.sqrt(np.mean(x[i : i + hop] ** 2) + 1e-12) for i in range(0, len(x) - hop, hop)])
    db = 20 * np.log10(frames + 1e-9)
    voiced = db[db > db.max() - 30]
    loud_range = float(np.percentile(voiced, 95) - np.percentile(voiced, 20))
    f0, voiced_frac, clarity, spread = pitch_summary(track(x, sr, min_hz=60, max_hz=400))
    return {
        "seconds": round(len(x) / sr, 2),
        "loud_range_db": round(loud_range, 1),
        "f0_hz": round(f0, 0),
        "pitch_spread_st": round(spread, 1),
    }


async def run() -> None:
    cache = GenCache(CACHE)
    out = ROOT / "build" / "audition2"
    rows = []
    for model, voice, dkey in GRID:
        spec = VoiceSpec(model=model, voice=voice, style=DIRECTIONS[dkey])
        backend = backend_for(spec)
        try:
            for n, text in enumerate(LINES, 1):
                ear = MeteredTranscriber(OpenAITranscribe())
                req = request_for(spec, text)
                res = await generate_verified(backend, req, cache=cache, verifier=SpeechVerifier(ear), rerolls=2)
                dest = out / f"{model}--{voice}--{dkey}--{n}.wav"
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(res.path, dest)
                m = measure(dest)
                m["wpm"] = round(len(text.split()) / m["seconds"] * 60) if m["seconds"] else None
                rows.append({"model": model, "voice": voice, "direction": dkey, "line": n, "cost": res.receipt.cost_usd, **m, "path": str(dest.relative_to(ROOT))})
                print(json.dumps(rows[-1]), file=sys.stderr)
        finally:
            await backend.aclose()
    (out / "audition2.json").write_text(json.dumps(rows, indent=1) + "\n")
    # summary per (model, voice, direction)
    print("| model | voice | direction | wpm | loud range dB | f0 Hz | pitch spread st | cost |")
    print("|---|---|---|---|---|---|---|---|")
    keys = sorted({(r["model"], r["voice"], r["direction"]) for r in rows}, key=lambda k: [g.index(k) if k in (g := [x for x in GRID]) else 0][0])
    for k in [tuple(g) for g in GRID]:
        rs = [r for r in rows if (r["model"], r["voice"], r["direction"]) == k]
        mean = lambda f: round(float(np.mean([r[f] for r in rs])), 1)
        print(f"| {k[0]} | {k[1]} | {k[2]} | {mean('wpm'):.0f} | {mean('loud_range_db')} | {mean('f0_hz'):.0f} | {mean('pitch_spread_st')} | ${sum(r['cost'] or 0 for r in rs):.4f} |")


if __name__ == "__main__":
    asyncio.run(run())
