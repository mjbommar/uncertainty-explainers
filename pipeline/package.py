"""Bookend a checked programme with the Da Vinci Math intro and outro.

    uv run python -m pipeline.build videos/<slug>/script.yaml --stage package

The programme (`output/<slug>.mp4`) is built and checked on its own timeline
first; `qa` must have passed. This stage then joins, in one re-encode with the
programme's own profile:

    intro (4.2 s) | programme | 0.5 s dissolve | outro (7.0 s)

The intro ends on the ink ground and the programme opens on it, so that join
is a cut between identical frames. The outro opens with 0.5 s of that same
ground held in silence (its manifest's `outro_lead_seconds`); the programme's
end card dissolves into exactly that lead, so its type fades to ground before
the logo arrives and the two never cross.

The idents live in `assets/brand/davinci-math/` with a manifest that names
their source (`davinci-math/brand/idents`), their digests and the ground
they were rendered to join. A digest or ground mismatch is refused.

Checks on the packaged file, written to `output/package.json` and appended to
`qa.md`: full decode; stream (frame count, geometry, profile, BT.709);
loudness; every narration segment transcribed again at its shifted time (a
join that slipped audio against the timeline fails here); the shifted
captions validated; and frames around both joins on `qa/package-joins.png`.
The packaged MP4 and captions are then copied to `publish/`.
"""

from __future__ import annotations

import asyncio
import dataclasses
import hashlib
import json
import shutil
import subprocess
from pathlib import Path
from typing import Any

from bc_audio import ffmpeg
from bc_audio.master import measure_file
from bc_motion import captions, encode
from bc_motion.models import Cue

from . import ROOT, brand
from .qa import MUXED_TP_CEILING, _asr, decode_errors, extract_frames
from .sheet import contact_sheet
from .spec import Video
from .timeline import CAPTION_CHARS, Plan

__all__ = ["BRAND_DIR", "DISSOLVE", "package"]

BRAND_DIR = ROOT / "assets" / "brand" / "davinci-math"
#: The end card dissolves into the outro over this many seconds.
DISSOLVE = 0.5


def _manifest(video: Video) -> dict[str, Any]:
    m = json.loads((BRAND_DIR / "manifest.json").read_text())
    ground = brand.palette(video.theme).ground
    if m["join"].lower() != ground.lower():
        raise ValueError(f"idents were rendered to join {m['join']}, but theme {video.theme!r} has ground {ground}")
    for cue in ("intro", "outro"):
        f = BRAND_DIR / m["cues"][cue]["file"]
        digest = hashlib.sha256(f.read_bytes()).hexdigest()
        if digest != m["cues"][cue]["sha256"]:
            raise ValueError(f"{f.name}: sha256 {digest[:12]} does not match the manifest")
    return m


def _join(intro: Path, core: Path, outro: Path, core_seconds: float, dest: Path, fps: int) -> None:
    prof = encode.H264_HIGH_QUALITY
    norm = f"fps={fps},settb=1/{fps},format=yuv420p"
    graph = ";".join(
        [
            f"[0:v]{norm}[iv]",
            f"[1:v]{norm}[cv]",
            f"[2:v]{norm}[ov]",
            "[0:a]aresample=48000,aformat=channel_layouts=stereo[ia]",
            "[1:a]aresample=48000,aformat=channel_layouts=stereo[ca]",
            "[2:a]aresample=48000,aformat=channel_layouts=stereo[oa]",
            # concat hands on a microsecond timebase; xfade needs both inputs on one.
            "[iv][ia][cv][ca]concat=n=2:v=1:a=1[hv0][ha]",
            f"[hv0]settb=1/{fps}[hv]",
            f"[hv][ov]xfade=transition=fade:duration={DISSOLVE}:offset={core_seconds - DISSOLVE:.6f}[v]",
            f"[ha][oa]acrossfade=d={DISSOLVE}:c1=tri:c2=tri[a]",
        ]
    )
    subprocess.run(
        [
            ffmpeg.binary(),
            "-v",
            "error",
            "-y",
            "-i",
            str(intro),
            "-i",
            str(core),
            "-i",
            str(outro),
            "-filter_complex",
            graph,
            "-map",
            "[v]",
            "-map",
            "[a]",
            "-c:v",
            prof.codec,
            *prof.video_args,
            "-pix_fmt",
            prof.pixel_format,
            "-colorspace",
            "bt709",
            "-color_primaries",
            "bt709",
            "-color_trc",
            "bt709",
            "-color_range",
            "tv",
            *prof.audio_args,
            "-ac",
            "2",
            "-movflags",
            "+faststart",
            str(dest),
        ],
        check=True,
    )


def _shift(vtt: str, seconds: float) -> list[Cue]:
    ms = round(seconds * 1000)
    return [
        c.model_copy(update={"start_ms": c.start_ms + ms, "end_ms": c.end_ms + ms}) for c in captions.parse_vtt(vtt)
    ]


def package(video: Video, plan: Plan, out: Path, publish: Path) -> dict[str, Any]:
    core = out / f"{video.slug}.mp4"
    qa = json.loads((out / "qa.json").read_text())
    if not qa.get("pass") or Path(qa["video"]).resolve() != core.resolve():
        raise ValueError("package needs a programme that passed qa; run --stage qa first")
    m = _manifest(video)
    if m.get("outro_lead_seconds", 0.0) < DISSOLVE:
        raise ValueError(f"the outro needs at least {DISSOLVE} s of held ground to dissolve into")
    intro_s = m["cues"]["intro"]["seconds"]
    outro_s = m["cues"]["outro"]["seconds"]
    t = plan.timeline
    fps = t.fps
    core_s = t.total_frames / fps
    # The intro's audio must be exactly its frames long or the programme would slip.
    for cue in ("intro", "outro"):
        info = encode.video_info(BRAND_DIR / m["cues"][cue]["file"])
        if info.get("nb_frames") != m["cues"][cue]["frames"] or info.get("r_frame_rate") != f"{fps}/1":
            raise ValueError(
                f"{cue}: {info.get('nb_frames')} frames at {info.get('r_frame_rate')}, expected "
                f"{m['cues'][cue]['frames']} at {fps}/1"
            )
    dest = out / f"{video.slug}-packaged.mp4"
    _join(BRAND_DIR / "intro.mp4", core, BRAND_DIR / "outro.mp4", intro_s + core_s, dest, fps)
    total_frames = round((intro_s + core_s + outro_s - DISSOLVE) * fps)

    report: dict[str, Any] = {
        "video": str(dest),
        "intro_seconds": intro_s,
        "outro_seconds": outro_s,
        "dissolve_seconds": DISSOLVE,
        "idents": m,
    }
    errors = decode_errors(dest)
    report["decode"] = {"ok": not errors, "errors": errors[:20]}
    info = encode.video_info(dest)
    report["stream"] = {
        "ok": info.get("nb_frames") == total_frames
        and info.get("color_space") == "bt709"
        and info.get("profile") == "High"
        and (info.get("width"), info.get("height")) == (brand.WIDTH, brand.HEIGHT),
        "frames": info.get("nb_frames"),
        "expected_frames": total_frames,
        **{
            k: info.get(k)
            for k in ("codec_name", "profile", "pix_fmt", "width", "height", "r_frame_rate", "color_space", "duration")
        },
    }
    lm = measure_file(dest)
    report["loudness"] = {
        "integrated_lufs": round(lm.integrated_lufs, 2),
        "true_peak_dbtp": round(lm.true_peak_dbtp, 2),
        "lra_lu": round(lm.loudness_range_lu, 2),
        "ok": abs(lm.integrated_lufs + 16.0) <= 0.7 and lm.true_peak_dbtp <= MUXED_TP_CEILING,
    }
    shifted = dataclasses.replace(plan, narration_start=[s + intro_s for s in plan.narration_start])
    rows, cost = asyncio.run(_asr(dest, video, shifted, out / "qa" / "package-asr"))
    report["narration"] = {
        "ok": all(r["ok"] for r in rows),
        "worst_wer": max(r["wer"] for r in rows),
        "segments": [{k: r[k] for k in ("segment", "wer", "ok", "hearings")} for r in rows],
        "asr_usd": round(cost, 5),
    }
    cues = _shift((out / "captions.vtt").read_text(), intro_s)
    vtt = captions.render_vtt(cues, title=video.title)
    faults = captions.problems_vtt(vtt, total_frames / fps, max_chars=CAPTION_CHARS)
    report["captions"] = {
        "ok": not faults and cues[0].start_ms >= round(intro_s * 1000),
        "cues": len(cues),
        "first_cue_ms": cues[0].start_ms,
        "problems": faults,
    }
    # Frames around each join.
    j1 = round(intro_s * fps)
    j2 = round((intro_s + core_s - DISSOLVE) * fps)
    picks = [
        (j1 - 20, "intro"),
        (j1 - 3, "intro end"),
        (j1 - 1, "last intro"),
        (j1, "first programme"),
        (j1 + 5, "programme"),
        (j1 + 30, "programme 1s"),
        (j2 - 3, "end card"),
        (j2 + round(DISSOLVE * fps / 2), "dissolve mid"),
        (j2 + round(DISSOLVE * fps), "outro"),
        (j2 + 60, "outro 2s"),
        (total_frames - 45, "outro close"),
        (total_frames - 1, "last frame"),
    ]
    frames = extract_frames(dest, [n for n, _ in picks], out / "qa" / "package-joins")
    sheet = contact_sheet(
        frames,
        [f"{tag}  #{n}  {n / fps:.2f}s" for n, tag in picks][: len(frames)],
        out / "qa" / "package-joins.png",
        columns=4,
        tile_width=460,
        title=f"{video.slug}: frames around the brand joins",
    )
    report["joins"] = {"sheet": str(sheet), "frames": len(frames), "intro_join_frame": j1, "outro_dissolve_frame": j2}
    gates = ["decode", "stream", "loudness", "narration", "captions"]
    report["pass"] = all(report[g]["ok"] for g in gates)
    (out / "package.json").write_text(json.dumps(report, indent=1) + "\n")
    if not report["pass"]:
        return report

    publish.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(dest, publish / f"{video.slug}.mp4")
    (publish / f"{video.slug}.vtt").write_text(vtt)
    section = _markdown(report)
    for qa_md in (out / "qa.md", publish / "qa.md"):
        text = qa_md.read_text()
        cut = text.find("\n## Brand bookends")
        qa_md.write_text((text if cut < 0 else text[:cut]).rstrip() + "\n\n" + section)
    return report


def _markdown(r: dict[str, Any]) -> str:
    def mark(ok: bool) -> str:
        return "PASS" if ok else "FAIL"

    s, lo, n, c = r["stream"], r["loudness"], r["narration"], r["captions"]
    m = r["idents"]
    stream = (
        f"{s['frames']} frames vs {s['expected_frames']} expected; {s['width']}x{s['height']} "
        f"{s['r_frame_rate']} {s['codec_name']} {s['profile']} {s['pix_fmt']}, {s['color_space']}, "
        f"{float(s['duration']):.3f} s"
    )
    loud = f"{lo['integrated_lufs']} LUFS, {lo['true_peak_dbtp']} dBTP, LRA {lo['lra_lu']} LU"
    asr = f"{len(n['segments'])} segments, worst WER {n['worst_wer']:.3f}"
    caps = f"{c['cues']} cues, first at {c['first_cue_ms'] / 1000:.3f} s, {len(c['problems'])} problems"
    return "\n".join(
        [
            "## Brand bookends",
            "",
            f"The published MP4 is the programme above with the {m['brand']} intro ({r['intro_seconds']} s) "
            f"before it and the outro ({r['outro_seconds']} s, {m['handle']}, {m['site']}) after a "
            f"{r['dissolve_seconds']} s dissolve. "
            "Idents: `assets/brand/davinci-math/` (source: `davinci-math/brand/idents`).",
            "",
            "| Gate | Result | Evidence |",
            "|---|---|---|",
            f"| Full decode | {mark(r['decode']['ok'])} | {len(r['decode']['errors'])} errors |",
            f"| Stream | {mark(s['ok'])} | {stream} |",
            f"| Loudness (muxed) | {mark(lo['ok'])} | {loud} |",
            f"| Narration ASR at shifted times | {mark(n['ok'])} | {asr} |",
            f"| Captions shifted | {mark(c['ok'])} | {caps} |",
            "",
            "Frames around both joins: `package-joins.png`.",
            "",
        ]
    )
