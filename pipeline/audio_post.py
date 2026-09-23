"""The audio post chain, on bc-audio and bc-signal, in an order that is the point.

Per clip (``prepare_clips``, before the timeline, because its output lengths
*are* the timeline):

1. decode to 48 kHz mono (``bc_audio.ffmpeg.decode``);
2. trim leading and trailing silence on a 20 ms RMS envelope
   (``bc_signal.rms_blocks``), keeping a short lead and tail;
3. tighten internal pauses longer than ``MAX_PAUSE`` to ``KEEP_PAUSE``
   (the cut sits inside silence, with a raised-cosine ramp either side);
4. ``bc_audio.voice.TTS_NARRATION``: high-pass, levelling compressor, derived
   split-band de-esser, band exciter, presence EQ, edge fades, loudness
   normalisation and a proven true-peak limit;
5. ``bc_audio.session.SessionMatcher`` across the set, so clips generated
   separately sound like one session.

The programme (``mix_and_master``): narration placed at each state's first
frame, sound effects at their offsets under a keyed compressor so they duck
beneath speech, the music bed looped seamlessly and ducked harder, then the
whole mix normalised to -16 LUFS integrated with a -1.5 dBTP true-peak ceiling
(``normalize_loudness`` then ``limit_true_peak``) and measured on
``bc_signal``'s BS.1770 meter. The mastering report is JSON beside the track.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import bc_audio as ba
import bc_signal as bs
import numpy as np
from bc_audio import ffmpeg
from bc_audio.master import Measurement, Profile, measure, problems
from bc_audio.session import SessionMatcher
from bc_audio.voice import TTS_NARRATION
from bc_motion.models import Timeline
from bc_motion.timeline import cue_offset

from .spec import Video

__all__ = ["RATE", "YOUTUBE", "Prepared", "mix_and_master", "prepare_clips"]

RATE = 48_000
FLOOR_DB = 42.0  # below the clip's loudest block, a block is silence
LEAD_S, TAIL_S = 0.05, 0.14
MAX_PAUSE, KEEP_PAUSE = 0.60, 0.42
RAMP_S = 0.012

#: YouTube's reference: it normalises down to about -14 LUFS, and -16 LUFS with
#: -1.5 dBTP leaves speech-led material a little headroom under that (house choice;
#: YouTube publishes no target). Stereo, 48 kHz.
YOUTUBE = Profile(
    name="youtube-speech",
    integrated_lufs=-16.0,
    true_peak_dbtp=-1.5,
    loudness_range_lu=9.0,
    sample_rate_hz=RATE,
    channels=2,
    bitrate="192k",
    loudness_tolerance_lu=0.5,
    peak_ceiling_dbtp=-1.4,
    max_loudness_range_lu=12.0,
)


@dataclass(frozen=True, slots=True)
class Prepared:
    segment: str
    path: Path
    seconds: float
    report: dict[str, Any]


def _envelope_db(x: np.ndarray) -> tuple[np.ndarray, int]:
    hop = int(0.01 * RATE)
    rms = np.asarray(bs.rms_blocks(np.ascontiguousarray(x), int(0.02 * RATE), hop), dtype=np.float64)
    return 20 * np.log10(rms + 1e-9), hop


def trim(x: np.ndarray) -> tuple[np.ndarray, dict[str, float]]:
    db, hop = _envelope_db(x)
    loud = np.nonzero(db > db.max() - FLOOR_DB)[0]
    if loud.size == 0:
        return x, {"trim_head_s": 0.0, "trim_tail_s": 0.0}
    a = max(0, loud[0] * hop - int(LEAD_S * RATE))
    b = min(x.size, (loud[-1] + 2) * hop + int(TAIL_S * RATE))
    return x[a:b].copy(), {"trim_head_s": a / RATE, "trim_tail_s": (x.size - b) / RATE}


def tighten(x: np.ndarray) -> tuple[np.ndarray, list[float]]:
    """Shorten long internal silences; returns the audio and each pause's original length."""
    db, hop = _envelope_db(x)
    quiet = db <= db.max() - FLOOR_DB
    runs: list[tuple[int, int]] = []
    i = 0
    while i < quiet.size:
        if quiet[i]:
            j = i
            while j < quiet.size and quiet[j]:
                j += 1
            runs.append((i, j))
            i = j
        else:
            i += 1
    cuts, lengths = [], []
    for a, b in runs:
        if a == 0 or b >= quiet.size:
            continue
        secs = (b - a) * hop / RATE
        if secs > MAX_PAUSE:
            excess = int((secs - KEEP_PAUSE) * RATE)
            mid = (a + b) * hop // 2
            cuts.append((mid - excess // 2, mid - excess // 2 + excess))
            lengths.append(round(secs, 3))
    if not cuts:
        return x, []
    ramp = int(RAMP_S * RATE)
    pieces, at = [], 0
    for c0, c1 in cuts:
        piece = x[at:c0].copy()
        piece[-ramp:] *= np.cos(np.linspace(0, np.pi / 2, ramp, dtype=np.float32)) ** 2
        pieces.append(piece)
        at = c1
    tail = x[at:].copy()
    tail[:ramp] *= np.sin(np.linspace(0, np.pi / 2, ramp, dtype=np.float32)) ** 2
    pieces.append(tail)
    return np.concatenate(pieces).astype(np.float32), lengths


def _m(m: Measurement) -> dict[str, float]:
    return {
        "lufs": round(m.integrated_lufs, 2),
        "dbtp": round(m.true_peak_dbtp, 2),
        "lra": round(m.loudness_range_lu, 2),
        "seconds": round(m.duration_seconds, 3),
    }


def prepare_clips(clips: list[tuple[str, Path]], out_dir: Path) -> list[Prepared]:
    """Trim, tighten, voice-chain and session-match every narration clip."""
    out_dir.mkdir(parents=True, exist_ok=True)
    chained: list[np.ndarray] = []
    reports: list[dict[str, Any]] = []
    for seg_id, path in clips:
        raw = ffmpeg.decode(path, rate=RATE, channels=1)[0]
        cut, trims = trim(raw)
        tight, pauses = tighten(cut)
        result = TTS_NARRATION.apply(np.ascontiguousarray(tight, dtype=np.float32))
        chained.append(np.ascontiguousarray(result.samples, dtype=np.float32))
        reports.append(
            {
                "segment": seg_id,
                "source": str(path),
                "source_seconds": round(raw.size / RATE, 3),
                **{k: round(v, 3) for k, v in trims.items()},
                "pauses_tightened_s": pauses,
                "chain_before": _m(result.before),
                "chain_after": _m(result.after),
                "stages": [{"kind": s.kind, **{k: round(v, 3) for k, v in s.outcome.items()}} for s in result.stages],
            }
        )
    session: dict[str, Any] = {}
    try:
        matched = SessionMatcher(RATE).match(chained, [r["segment"] for r in reports])
        final = [np.ascontiguousarray(c, dtype=np.float32) for c in matched.clips]
        rep = matched.report
        session = {
            "target_lufs": rep.target_lufs,
            "spread_after_lu": round(rep.after_spread_lu, 3),
            "warnings": list(rep.warnings),
            "problems": list(rep.problems()),
        }
    except Exception as exc:  # matching is a refinement; the chain output is already levelled
        final = chained
        session = {"skipped": f"{type(exc).__name__}: {exc}"}
    out: list[Prepared] = []
    for body, rep in zip(final, reports, strict=True):
        dest = out_dir / f"{rep['segment']}.wav"
        ba.wav_write(str(dest), body, RATE, bits=24)
        rep["seconds"] = round(body.size / RATE, 4)
        rep["session"] = session
        out.append(Prepared(rep["segment"], dest, body.size / RATE, rep))
    return out


# ------------------------------------------------------------------ programme


def _place(bus: np.ndarray, x: np.ndarray, start: int) -> None:
    if start >= bus.shape[-1]:
        return
    end = min(bus.shape[-1], start + x.shape[-1])
    bus[..., start:end] += x[..., : end - start]


def _stereo(x: np.ndarray) -> np.ndarray:
    return np.ascontiguousarray(np.vstack([x, x]) if x.ndim == 1 else x, dtype=np.float32)


def duck(bus: np.ndarray, key: np.ndarray, **kw: float) -> tuple[np.ndarray, float]:
    """Keyed compression per channel. ``bc_audio.compressor`` is mono; with a shared key the
    gain curve depends only on the key, so per-channel runs are a linked stereo duck."""
    out, worst = [], 0.0
    for ch in bus:
        y, red = ba.compressor(np.ascontiguousarray(ch, dtype=np.float32), RATE, key=key, **kw)
        out.append(y)
        worst = max(worst, abs(float(red)))
    return np.ascontiguousarray(np.vstack(out), dtype=np.float32), worst


def mix_and_master(
    video: Video,
    timeline: Timeline,
    clips: dict[str, Path],
    sfx: dict[str, Any],
    sfx_keys: list[list[str]],
    bed: Path | None,
    work: Path,
) -> tuple[Path, dict[str, Any]]:
    """Mix, duck and master the programme to ``YOUTUBE``; returns the WAV and the report."""
    work.mkdir(parents=True, exist_ok=True)
    total = round(timeline.total_frames / timeline.fps * RATE)
    narr = np.zeros(total, dtype=np.float32)
    spoken = {s.item: s for s in timeline.states if s.spoken}
    placements = []
    for i, seg in enumerate(video.segments):
        state = spoken[i]
        x = ffmpeg.decode(clips[seg.id], rate=RATE, channels=1)[0]
        start = round(state.start * RATE)
        _place(narr, x, start)
        placements.append({"segment": seg.id, "start_s": round(state.start, 3), "seconds": round(x.size / RATE, 3)})

    fx_bus = np.zeros((2, total), dtype=np.float32)
    fx_rows = []
    for i, seg in enumerate(video.segments):
        state = spoken[i]
        for fx, key in zip(seg.sfx, sfx_keys[i], strict=True):
            item = sfx[key]
            y = ffmpeg.decode(item.path, rate=RATE, channels=2)
            y, level = ba.normalize_loudness(np.ascontiguousarray(y), RATE, -24.0, -3.0, "hold")
            y = y * np.float32(10 ** (fx.gain_db / 20))
            offset = cue_offset(seg.say, fx.at, state.seconds)
            start = round((state.start + offset) * RATE)
            _place(fx_bus, y, start)
            fx_rows.append(
                {
                    "segment": seg.id,
                    "cue": item.label,
                    "at_s": round(state.start + offset, 3),
                    "gain_db": fx.gain_db,
                    "level_gain_db": round(level.gain_db, 2),
                }
            )
    if fx_rows:
        fx_bus, fx_red = duck(fx_bus, narr, threshold_db=-28.0, ratio=1.8, attack_ms=10.0, release_ms=200.0)
    else:
        fx_red = 0.0

    bed_row: dict[str, Any] = {"used": False}
    bed_bus = np.zeros((2, total), dtype=np.float32)
    if bed is not None and video.music is not None:
        looped = ffmpeg.seamless_bed(bed, total / RATE + 0.5, work / "bed.wav", rate=RATE, channels=2)
        b = ffmpeg.decode(looped, rate=RATE, channels=2)[:, :total]
        b, _level = ba.normalize_loudness(np.ascontiguousarray(b), RATE, -18.0, -3.0, "hold")
        b = b * np.float32(10 ** (video.music.gain_db / 20))
        fade_in, fade_out = int(1.5 * RATE), int(3.0 * RATE)
        b = np.vstack([bs.fade_both(np.ascontiguousarray(ch), fade_in, fade_out, "raised_cosine") for ch in b])
        b, bed_red = duck(b, narr, threshold_db=-30.0, ratio=2.0, attack_ms=80.0, release_ms=700.0)
        bed_bus[:, : b.shape[1]] = b
        bed_row = {"used": True, "gain_db": video.music.gain_db, "duck_max_db": round(float(bed_red), 2)}

    mix = _stereo(narr) + fx_bus + bed_bus
    pre = measure(mix, RATE)
    levelled, level = ba.normalize_loudness(
        np.ascontiguousarray(mix), RATE, YOUTUBE.integrated_lufs, YOUTUBE.true_peak_dbtp, "limit"
    )
    limited, limit = ba.limit_true_peak(np.ascontiguousarray(levelled), RATE, YOUTUBE.true_peak_dbtp)
    post = measure(limited, RATE)
    dest = work / "master.wav"
    ba.wav_write(str(dest), limited, RATE, bits=24)
    faults = problems(post, YOUTUBE)
    report = {
        "profile": YOUTUBE.model_dump(),
        "timeline_seconds": round(timeline.total_seconds, 4),
        "track_seconds": round(limited.shape[1] / RATE, 4),
        "narration": placements,
        "sfx": fx_rows,
        "sfx_duck_max_db": round(float(fx_red), 2),
        "bed": bed_row,
        "pre_master": _m(pre),
        "level": {"gain_db": round(level.gain_db, 2), "max_reduction_db": round(level.max_reduction_db, 2)},
        "limit": {
            "max_reduction_db": round(limit.max_reduction_db, 2),
            "true_peak_dbtp": round(limit.true_peak_dbtp, 2),
        },
        "master": _m(post),
        "problems": faults,
    }
    (work / "mastering.json").write_text(json.dumps(report, indent=1) + "\n")
    if faults:
        raise RuntimeError("mastering missed its contract: " + "; ".join(faults))
    return dest, report
