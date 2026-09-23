"""The one timeline: built from measured clip seconds, everything else derived from it.

``bc_motion.timeline.build`` quantises each segment's narration and hold to
frames; the end card is one silent state after the last segment. From the
timeline come the segment spans the renderer walks, the caption cues (WebVTT
and SRT, validated), each segment's beats in seconds, and the motion ledger.
The narration track is asserted against it (``drift``); nothing is stretched.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from bc_motion import captions, encode
from bc_motion import timeline as tl
from bc_motion.models import Timeline

from .spec import Video

__all__ = ["CAPTION_CHARS", "FPS", "Plan", "build", "check_drift", "write"]

FPS = 30
CAPTION_CHARS = 84  # two readable lines in the caption band


@dataclass(frozen=True, slots=True)
class Plan:
    timeline: Timeline
    spans: list[tuple[int, float, float]]  # (segment index or -1 for the end card, start, end)
    narration_start: list[float]
    narration_seconds: list[float]
    beats: list[tuple[float, ...]]


def build(video: Video, seconds: list[float], *, fps: int = FPS) -> Plan:
    n = len(video.segments)
    if len(seconds) != n:
        raise ValueError(f"{len(seconds)} measured clips for {n} segments")
    timeline = tl.build(
        pages=[*range(1, n + 1), n + 1],
        seconds=[*seconds, video.end_card.seconds],
        texts=[*(s.say for s in video.segments), ""],
        holds=[*(s.hold for s in video.segments), 0.0],
        transitions=[*(s.transition for s in video.segments), "dissolve"],
        spoken=[True] * n + [False],
        fps=fps,
    )
    faults = [p for p in timeline.problems(pages=n + 1) if p.severity == "error"]
    if faults:
        raise ValueError("timeline problems: " + "; ".join(str(p) for p in faults))
    spans_raw = tl.spans(timeline)
    spans = [(sp.index if sp.index < n else -1, sp.start, sp.end) for sp in spans_raw]
    spoken = {s.item: s for s in timeline.states if s.spoken}
    starts = [spoken[i].start for i in range(n)]
    lengths = [spoken[i].seconds for i in range(n)]
    beats = [
        tuple(float(tl.cue_offset(seg.say, b, lengths[i])) for b in seg.beats) for i, seg in enumerate(video.segments)
    ]
    return Plan(timeline, spans, starts, lengths, beats)


def cues(plan: Plan):
    return captions.cues_from_timeline(plan.timeline, max_chars=CAPTION_CHARS)


def write(video: Video, plan: Plan, out: Path) -> dict:
    """``timeline.json``, ``captions.vtt``/``.srt`` and ``motion_ledger.json``; returns a summary."""
    out.mkdir(parents=True, exist_ok=True)
    t = plan.timeline
    (out / "timeline.json").write_text(t.model_dump_json(indent=1) + "\n")
    cs = cues(plan)
    vtt = captions.render_vtt(cs, title=video.title)
    faults = captions.problems(cs, t.total_seconds, max_chars=CAPTION_CHARS)
    faults += captions.problems_vtt(vtt, t.total_seconds, max_chars=CAPTION_CHARS)
    (out / "captions.vtt").write_text(vtt)
    (out / "captions.srt").write_text(captions.render_srt(cs))
    ledger = encode.motion_ledger(encode.shots_from_timeline(t), fps=t.fps)
    (out / "motion_ledger.json").write_text(json.dumps([r.model_dump() for r in ledger], indent=1) + "\n")
    summary = {
        "fps": t.fps,
        "frames": t.total_frames,
        "seconds": round(t.total_seconds, 3),
        "states": len(t.states),
        "cues": len(cs),
        "caption_problems": faults,
        "spans": [
            {"segment": (video.segments[i].id if i >= 0 else "end_card"), "start": round(a, 3), "end": round(b, 3)}
            for i, a, b in plan.spans
        ],
        "beats": {video.segments[i].id: [round(b, 3) for b in bs] for i, bs in enumerate(plan.beats) if bs},
        "motion_frames": sum(1 for r in ledger if r.kind != "page"),
    }
    (out / "timeline_summary.json").write_text(json.dumps(summary, indent=1) + "\n")
    if faults:
        raise ValueError("caption problems: " + "; ".join(faults))
    return summary


def check_drift(plan: Plan, track_seconds: float, *, max_drift: float = 0.005) -> dict:
    """The track against the timeline; raises if they were built from different things."""
    d = plan.timeline.drift(track_seconds)
    faults = plan.timeline.track_problems(track_seconds, max_drift=max_drift)
    if faults:
        raise ValueError("track drift: " + "; ".join(str(p) for p in faults))
    return d.model_dump()


def load_plan(video: Video, out: Path) -> Plan:
    """Rebuild the plan from the prepared clip lengths recorded by the timeline stage."""
    meta = json.loads((out / "clips.json").read_text())
    return build(video, [m["seconds"] for m in meta])
