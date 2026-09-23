"""The CLI: one script, six stages, each stopping early on purpose.

    uv run python -m pipeline.build videos/<slug>/script.yaml --stage check
    uv run python -m pipeline.build videos/<slug>/script.yaml --stage timeline
    uv run python -m pipeline.build videos/<slug>/script.yaml --stage audio
    uv run python -m pipeline.build videos/<slug>/script.yaml --stage frames
    uv run python -m pipeline.build videos/<slug>/script.yaml --stage assemble [--4k]
    uv run python -m pipeline.build videos/<slug>/script.yaml --stage qa
    uv run python -m pipeline.build videos/<slug>/script.yaml            # all of them

``check`` is free: validation, the length estimate, the voice checkers.
``timeline`` synthesises and verifies narration, runs the per-clip chain, and
lays out the timeline and captions. ``audio`` generates effects and the bed,
mixes, masters and asserts drift. ``frames`` generates images and writes
review stills. ``assemble`` renders every frame in parallel into the encoder
and writes the poster. ``qa`` checks the MP4 and writes ``qa.md``.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

from . import ROOT
from .spec import SpecError, Video, estimate, load, validate

STAGES = ("check", "timeline", "audio", "frames", "assemble", "qa")


class Paths:
    def __init__(self, script: Path) -> None:
        self.script = script.resolve()
        self.root = self.script.parent
        self.assets = self.root / "assets"
        self.receipts = self.assets / "receipts"
        self.out = self.root / "output"
        self.clips = self.out / "clips"
        self.publish = self.root / "publish"


def _log(msg: str) -> None:
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def _ledger(paths: Paths) -> dict[str, Any]:
    f = paths.out / "costs.json"
    return json.loads(f.read_text()) if f.is_file() else {"entries": []}


def _record(paths: Paths, stage: str, rows: list[dict[str, Any]]) -> None:
    led = _ledger(paths)
    led["entries"] = [e for e in led["entries"] if e["stage"] != stage] + [{"stage": stage, **r} for r in rows]
    spent = [e.get("spent_usd") for e in led["entries"]]
    worth = [e.get("receipt_usd") for e in led["entries"]]
    led["spent_usd"] = round(sum(x or 0.0 for x in spent), 5)
    led["receipts_usd"] = round(sum(x or 0.0 for x in worth), 5)
    led["unpriced"] = [e["item"] for e in led["entries"] if e.get("receipt_usd") is None and e.get("kind") != "asr"]
    paths.out.mkdir(parents=True, exist_ok=True)
    (paths.out / "costs.json").write_text(json.dumps(led, indent=1) + "\n")


# ------------------------------------------------------------------ stages


def stage_check(video: Video, paths: Paths) -> dict[str, Any]:
    warnings = validate(video)
    est = estimate(video)
    paths.out.mkdir(parents=True, exist_ok=True)
    text = paths.out / "narration.md"
    text.write_text("\n\n".join(f"{s.say}" for s in video.segments) + "\n")
    checks = {}
    for script in ("check_prose.py", "check_simplified.py"):
        proc = subprocess.run(
            ["uv", "run", str(ROOT / "scripts" / script), str(text)], capture_output=True, text=True, cwd=ROOT
        )
        tail = (proc.stdout + proc.stderr).strip().splitlines()[-12:]
        checks[script] = {"exit": proc.returncode, "tail": tail}
    report = {"estimate": est, "warnings": warnings, "voice_checks": checks}
    (paths.out / "check.json").write_text(json.dumps(report, indent=1) + "\n")
    _log(f"check: {est['words']} words, about {est['seconds']:.1f}s (target {video.target_seconds:.0f}s)")
    for w in warnings:
        _log(f"  warning: {w}")
    for name, c in checks.items():
        _log(f"  {name}: exit {c['exit']}" + (f"; {c['tail'][-1]}" if c["tail"] else ""))
    return report


def stage_timeline(video: Video, paths: Paths) -> dict[str, Any]:
    from . import audio_post, speech, timeline

    _log(f"narration: {len(video.segments)} clips in {video.voice.model}/{video.voice.voice}")
    clips, asr_cost = speech.synthesize(video, paths.receipts)
    _record(
        paths,
        "timeline",
        [
            {
                "kind": "speech",
                "item": c.segment,
                "spent_usd": 0.0 if c.cached else c.cost_usd,
                "receipt_usd": json.loads(c.receipt.read_text()).get("cost_usd"),
                "cached": c.cached,
                "attempts": c.attempts,
                "wer": c.wer,
            }
            for c in clips
        ]
        + [
            {
                "kind": "asr",
                "item": "verifier transcription",
                "spent_usd": round(asr_cost, 5),
                "receipt_usd": round(asr_cost, 5),
            }
        ],
    )
    prepared = audio_post.prepare_clips([(c.segment, c.path) for c in clips], paths.clips)
    meta = [
        {**p.report, "raw_seconds": c.seconds, "wer": c.wer, "attempts": c.attempts, "cached": c.cached}
        for p, c in zip(prepared, clips, strict=True)
    ]
    (paths.out / "clips.json").write_text(json.dumps(meta, indent=1) + "\n")
    plan = timeline.build(video, [p.seconds for p in prepared])
    summary = timeline.write(video, plan, paths.out)
    _log(f"timeline: {summary['frames']} frames, {summary['seconds']:.2f}s, {summary['cues']} cues")
    return summary


def stage_audio(video: Video, paths: Paths) -> dict[str, Any]:
    from . import audio_post, sound, timeline

    plan = timeline.load_plan(video, paths.out)
    fx = sound.generate_sfx(video, paths.receipts)
    bed, why = sound.generate_bed(video, paths.receipts)
    rows = [
        {
            "kind": "sfx",
            "item": r.label,
            "spent_usd": 0.0 if r.cached else r.cost_usd,
            "receipt_usd": json.loads(r.receipt.read_text()).get("cost_usd"),
            "cached": r.cached,
        }
        for r in fx.values()
    ]
    if bed is not None:
        rows.append(
            {
                "kind": "music",
                "item": "bed",
                "spent_usd": 0.0 if bed.cached else bed.cost_usd,
                "receipt_usd": json.loads(bed.receipt.read_text()).get("cost_usd"),
                "cached": bed.cached,
            }
        )
    else:
        _log(f"  music bed skipped: {why}")
    _record(paths, "audio", rows)
    keys = [[sound.sfx_key(f) for f in seg.sfx] for seg in video.segments]
    clips = {s.id: paths.clips / f"{s.id}.wav" for s in video.segments}
    _master, report = audio_post.mix_and_master(
        video, plan.timeline, clips, fx, keys, bed.path if bed else None, paths.out
    )
    report["drift"] = timeline.check_drift(plan, report["track_seconds"])
    report["bed_skipped"] = why
    (paths.out / "mastering.json").write_text(json.dumps(report, indent=1) + "\n")
    m = report["master"]
    _log(f"audio: {m['lufs']} LUFS, {m['dbtp']} dBTP, LRA {m['lra']} LU, {report['track_seconds']:.3f}s")
    return report


def _images(video: Video, paths: Paths):
    from . import images

    rows = images.generate_images(video, paths.assets)
    if rows:
        _record(
            paths,
            "images",
            [
                {
                    "kind": "image",
                    "item": r["id"],
                    "spent_usd": r["cost_usd"] if not r["cached"] else 0.0,
                    "receipt_usd": r["receipt_cost_usd"],
                    "cached": r["cached"],
                }
                for r in rows
            ],
        )
    return images.load_images(video, paths.assets)


def _job(video: Video, paths: Paths, scale: int = 1):
    from . import timeline
    from .render import Job

    return Job(video=video, plan=timeline.load_plan(video, paths.out), images=_images(video, paths), scale=scale)


def stage_frames(video: Video, paths: Paths) -> dict[str, Any]:
    from .render import frame_at
    from .sheet import contact_sheet

    job = _job(video, paths)
    fps = job.plan.timeline.fps
    idx, labels = [], []
    for i, a, b in job.plan.spans:
        name = video.segments[i].id if i >= 0 else "end_card"
        for frac in (0.12, 0.45, 0.9):
            n = min(job.plan.timeline.total_frames - 1, int((a + (b - a) * frac) * fps))
            idx.append(n)
            labels.append(f"{name} {frac:.0%}  #{n}")
    frames = [frame_at(job, n) for n in idx]
    dest = contact_sheet(
        frames,
        labels,
        paths.out / "frames" / "stills.png",
        columns=3,
        tile_width=620,
        title=f"{video.slug}: stills from the renderer",
    )
    from bc_image import save

    for n, frame, lab in zip(idx, frames, labels, strict=True):
        save(frame, paths.out / "frames" / f"{lab.split()[0]}-{n:05d}.png")
    _log(f"frames: {len(frames)} stills -> {dest}")
    return {"sheet": str(dest), "frames": len(frames)}


def stage_assemble(video: Video, paths: Paths, *, four_k: bool = False, workers: int | None = None) -> dict[str, Any]:
    from bc_motion import encode

    from .render import poster, stream

    scale = 2 if four_k else 1
    job = _job(video, paths, scale)
    t = job.plan.timeline
    dest = paths.out / (f"{video.slug}-4k.mp4" if four_k else f"{video.slug}.mp4")
    started = time.time()
    n = workers or max(2, (os.cpu_count() or 4) - 2)
    _log(f"assemble: {t.total_frames} frames at {job.size[0]}x{job.size[1]} on {n} workers")
    report = encode.assemble(
        stream(job, workers=n),
        paths.out / "master.wav",
        dest,
        profile=encode.H264_HIGH_QUALITY,
        fps=t.fps,
        size=job.size,
        timeline=t,
    )
    wall = time.time() - started
    poster(job, paths.out / "poster.png", paths.out / "thumbnail.png")
    _log(f"assemble: {report.seconds:.3f}s video in {wall:.1f}s wall -> {dest}")
    return {
        "mp4": str(dest),
        "seconds": report.seconds,
        "frames": report.frames,
        "wall_s": round(wall, 1),
        "bytes": dest.stat().st_size,
    }


def stage_qa(video: Video, paths: Paths) -> dict[str, Any]:
    from . import images, qa, timeline

    plan = timeline.load_plan(video, paths.out)
    mp4 = paths.out / f"{video.slug}.mp4"
    mastering = json.loads((paths.out / "mastering.json").read_text())
    led = _ledger(paths)
    extra = {
        "master": mastering["master"],
        "drift": mastering.get("drift"),
        "costs": {
            "spent_usd": led.get("spent_usd", 0.0),
            "receipts_usd": led.get("receipts_usd", 0.0),
            "unpriced": led.get("unpriced", []),
        },
    }
    report = qa.run(video, plan, mp4, paths.out, images.load_images(video, paths.assets), extra)
    _record(
        paths,
        "qa",
        [
            {
                "kind": "asr",
                "item": "qa transcription",
                "spent_usd": report["narration"]["asr_usd"],
                "receipt_usd": report["narration"]["asr_usd"],
            }
        ],
    )
    led = _ledger(paths)
    report["costs"] = {"spent_usd": led["spent_usd"], "receipts_usd": led["receipts_usd"], "unpriced": led["unpriced"]}
    (paths.out / "qa.md").write_text(
        qa.markdown(video, report, ["decode", "stream", "loudness", "narration", "containment", "captions"])
    )
    paths.publish.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(paths.out / "qa.md", paths.publish / "qa.md")
    shutil.copyfile(paths.out / "poster.png", paths.publish / "poster.png")
    _log(f"qa: {'PASS' if report['pass'] else 'FAIL'} -> {paths.out / 'qa.md'}")
    return report


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("script", type=Path)
    ap.add_argument("--stage", choices=(*STAGES, "all"), default="all")
    ap.add_argument("--4k", dest="four_k", action="store_true", help="assemble at 3840x2160")
    ap.add_argument("--workers", type=int)
    args = ap.parse_args(argv)
    try:
        video = load(args.script)
    except SpecError as exc:
        print(f"script refused: {exc}", file=sys.stderr)
        return 2
    paths = Paths(args.script)
    order = STAGES if args.stage == "all" else (args.stage,)
    for stage in order:
        if stage == "check":
            stage_check(video, paths)
        elif stage == "timeline":
            stage_timeline(video, paths)
        elif stage == "audio":
            stage_audio(video, paths)
        elif stage == "frames":
            stage_frames(video, paths)
        elif stage == "assemble":
            stage_assemble(video, paths, four_k=args.four_k, workers=args.workers)
        elif stage == "qa":
            report = stage_qa(video, paths)
            if not report["pass"]:
                return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
