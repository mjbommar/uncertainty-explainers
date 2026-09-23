"""QA of the delivered MP4, not of its sources.

Gates, each recorded with its number and its limit in ``qa.json`` and ``qa.md``:

1. **Decode**: ``ffmpeg -v error -f null`` over the whole file, no errors.
2. **Stream**: frame count equals the timeline's; size, rate, codec, pixel
   format and BT.709 tags as the profile promises (``bc_motion.encode.video_info``).
3. **Cuts**: frames decoded from the MP4 just before, at, inside and after
   every transition, on one contact sheet, plus one mid-segment frame each.
4. **Loudness**: the muxed audio re-measured on bc-signal's BS.1770 meter.
5. **Narration**: each segment's span of the muxed audio transcribed
   (``bc_gen.OpenAITranscribe``) and scored against the script
   (``SpeechVerifier.score``: WER, numbers).
6. **Containment**: every scene used, at four reveal points, rasterised on its
   own; no ink outside the stage box.
7. **Captions**: the VTT re-parsed and validated against the duration.

A pass here is machine evidence only. ``qa.md`` says so, and leaves the
human-review line open until somebody has watched it with sound.
"""

from __future__ import annotations

import asyncio
import json
import re
import subprocess
from pathlib import Path
from typing import Any

import bc_image as bi
import numpy as np
from bc_audio import ffmpeg
from bc_audio.master import measure_file
from bc_gen import OpenAITranscribe, SpeechVerifier
from bc_motion import captions, encode
from bc_motion.encode import TRANSITION_SECONDS

from . import brand, scenes
from .canvas import Frame, ink_bbox
from .sheet import contact_sheet
from .spec import Video
from .speech import speakable
from .timeline import CAPTION_CHARS, Plan

__all__ = ["containment", "run"]

WER_MAX = 0.10
MUXED_TP_CEILING = -1.0  # AAC can lift true peak a few tenths above the WAV master's -1.5


def decode_errors(mp4: Path) -> list[str]:
    proc = subprocess.run(
        [ffmpeg.binary(), "-v", "error", "-i", str(mp4), "-f", "null", "-"], capture_output=True, text=True
    )
    lines = [ln for ln in proc.stderr.splitlines() if ln.strip()]
    if proc.returncode != 0:
        lines.append(f"ffmpeg exited {proc.returncode}")
    return lines


def extract_frames(mp4: Path, indices: list[int], out: Path) -> list[np.ndarray]:
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("f_*.png"):
        old.unlink()
    uniq = sorted(set(indices))
    expr = "+".join(f"eq(n\\,{i})" for i in uniq)
    subprocess.run(
        [
            ffmpeg.binary(),
            "-v",
            "error",
            "-i",
            str(mp4),
            "-vf",
            f"select='{expr}'",
            "-vsync",
            "0",
            str(out / "f_%04d.png"),
        ],
        check=True,
    )
    files = sorted(out.glob("f_*.png"))
    by_index = dict(zip(uniq, files, strict=False))
    return [bi.to_u8(bi.load(by_index[i])) for i in indices if i in by_index]


def containment(video: Video, images: dict[str, np.ndarray]) -> list[dict[str, Any]]:
    """Each scene the video uses, drawn alone at four reveal points: ink inside the stage?"""
    pal = brand.palette(video.theme)
    rows = []
    for seg in video.segments:
        for t in (0.15, 0.4, 0.7, 1.0):
            f = Frame(pal)
            clock = scenes.Clock(t=t, local=t * 3.2, seconds=5.0 + t * 3.2, settled=t >= 1.0)
            params = dict(seg.scene.params)
            scenes.draw(f, seg.scene.name, params, brand.STAGE, clock, scenes.Ctx(images=images))
            box = ink_bbox(f.render_rgba())
            ok = bool(box is None or brand.STAGE.contains(box, slack=2.0))
            rows.append(
                {
                    "segment": seg.id,
                    "scene": seg.scene.name,
                    "t": t,
                    "ok": ok,
                    "bbox": None if box is None else [round(box.x), round(box.y), round(box.right), round(box.bottom)],
                }
            )
    return rows


async def _asr(mp4: Path, video: Video, plan: Plan, work: Path) -> tuple[list[dict[str, Any]], float]:
    ear = OpenAITranscribe()
    verifier = SpeechVerifier(ear)
    rows, cost = [], 0.0
    work.mkdir(parents=True, exist_ok=True)
    try:
        for i, seg in enumerate(video.segments):
            start, secs = plan.narration_start[i], plan.narration_seconds[i]
            wav = work / f"{seg.id}.wav"
            subprocess.run(
                [
                    ffmpeg.binary(),
                    "-v",
                    "error",
                    "-y",
                    "-ss",
                    f"{start:.3f}",
                    "-t",
                    f"{secs + 0.15:.3f}",
                    "-i",
                    str(mp4),
                    "-vn",
                    "-ac",
                    "1",
                    "-ar",
                    "16000",
                    str(wav),
                ],
                check=True,
            )
            script = speakable(seg.say)
            attempts = []
            for _ in range(2):  # an ASR truncation is not a narration fault: hear a failure twice
                heard = await ear.transcribe(wav)
                cost += float(heard.cost_usd or 0.0)
                v = verifier.score(script, heard.text)
                attempts.append((v, heard.text))
                if v.ok:
                    break
            v, text = min(attempts, key=lambda a: float(a[0].score or 0.0))
            rows.append(
                {
                    "segment": seg.id,
                    "wer": round(float(v.score or 0.0), 3),
                    "ok": v.ok or (v.score or 0) <= WER_MAX,
                    "problems": list(v.problems),
                    "heard": text,
                    "hearings": len(attempts),
                    "first_heard": attempts[0][1] if len(attempts) > 1 else None,
                }
            )
    finally:
        await ear.aclose()
    return rows, cost


def run(
    video: Video, plan: Plan, mp4: Path, out: Path, images: dict[str, np.ndarray], extra: dict[str, Any] | None = None
) -> dict[str, Any]:
    qa_dir = out / "qa"
    qa_dir.mkdir(parents=True, exist_ok=True)
    t = plan.timeline
    fps = t.fps
    report: dict[str, Any] = {"video": str(mp4)}

    errors = decode_errors(mp4)
    report["decode"] = {"ok": not errors, "errors": errors[:20]}

    info = encode.video_info(mp4)
    report["stream"] = {
        "ok": info.get("nb_frames") == t.total_frames and info.get("color_space") == "bt709",
        "frames": info.get("nb_frames"),
        "timeline_frames": t.total_frames,
        **{
            k: info.get(k)
            for k in (
                "codec_name",
                "profile",
                "pix_fmt",
                "width",
                "height",
                "r_frame_rate",
                "color_space",
                "color_transfer",
                "color_primaries",
                "duration",
            )
        },
    }

    # Cuts: 2 frames before, the cut, the transition's middle, 3 frames after it ends; plus mid-spans.
    idx, labels = [], []
    for k in range(1, len(plan.spans)):
        seg_i, a, _b = plan.spans[k]
        name = "dissolve" if seg_i < 0 else video.segments[seg_i].transition
        f0 = round(a * fps)
        tf = round(TRANSITION_SECONDS.get(name, 0.0) * fps)
        for off, tag in ((-2, "before"), (0, "cut"), (tf // 2, "mid"), (tf + 3, "after")):
            n = min(max(0, f0 + off), t.total_frames - 1)
            idx.append(n)
            labels.append(f"cut {k} {name} {tag}  #{n}  {n / fps:.2f}s")
    cut_frames = extract_frames(mp4, idx, qa_dir / "cuts")
    report["cuts"] = {
        "sheet": str(
            contact_sheet(
                cut_frames,
                labels[: len(cut_frames)],
                qa_dir / "cuts.png",
                columns=4,
                tile_width=460,
                title=f"{video.slug}: frames around every cut",
            )
        ),
        "frames": len(cut_frames),
    }
    mids = [min(t.total_frames - 1, round((a + b) / 2 * fps)) for _, a, b in plan.spans]
    mid_frames = extract_frames(mp4, mids, qa_dir / "mids")
    names = [(video.segments[i].id if i >= 0 else "end_card") for i, _, _ in plan.spans]
    report["segments_sheet"] = str(
        contact_sheet(
            mid_frames,
            [f"{n}  #{m}" for n, m in zip(names, mids, strict=True)],
            qa_dir / "segments.png",
            columns=3,
            tile_width=620,
            title=f"{video.slug}: one frame per segment",
        )
    )
    for n, frame in zip(names, mid_frames, strict=True):
        bi.save(frame, qa_dir / f"mid-{n}.png")

    m = measure_file(mp4)
    report["loudness"] = {
        "integrated_lufs": round(m.integrated_lufs, 2),
        "true_peak_dbtp": round(m.true_peak_dbtp, 2),
        "lra_lu": round(m.loudness_range_lu, 2),
        "channels": m.channels,
        "ok": abs(m.integrated_lufs + 16.0) <= 0.7 and m.true_peak_dbtp <= MUXED_TP_CEILING,
    }

    asr_rows, asr_cost = asyncio.run(_asr(mp4, video, plan, qa_dir / "asr"))
    report["narration"] = {"ok": all(r["ok"] for r in asr_rows), "segments": asr_rows, "asr_usd": round(asr_cost, 5)}

    rows = containment(video, images)
    report["containment"] = {
        "ok": all(r["ok"] for r in rows),
        "failures": [r for r in rows if not r["ok"]],
        "checked": len(rows),
    }

    vtt = (out / "captions.vtt").read_text()
    faults = captions.problems_vtt(vtt, t.total_seconds, max_chars=CAPTION_CHARS)
    report["captions"] = {"ok": not faults, "cues": len(captions.parse_vtt(vtt)), "problems": faults}
    if extra:
        report.update(extra)
    gates = ["decode", "stream", "loudness", "narration", "containment", "captions"]
    report["pass"] = all(report[g]["ok"] for g in gates)
    (out / "qa.json").write_text(json.dumps(report, indent=1) + "\n")
    (out / "qa.md").write_text(markdown(video, report, gates))
    return report


def markdown(video: Video, r: dict[str, Any], gates: list[str]) -> str:
    def mark(ok: bool) -> str:
        return "PASS" if ok else "FAIL"

    s = r["stream"]
    ld = r["loudness"]
    lines = [
        f"# QA: {video.title} (`{video.slug}`)",
        "",
        f"Machine gates: **{mark(r['pass'])}**. Human review (watched in full, with sound): **pending**.",
        "",
        "| Gate | Result | Evidence |",
        "|---|---|---|",
        f"| Full decode | {mark(r['decode']['ok'])} | `ffmpeg -v error -f null`: {len(r['decode']['errors'])} errors |",
        f"| Stream | {mark(s['ok'])} | {s['frames']} frames vs {s['timeline_frames']} in the timeline; "
        f"{s['width']}x{s['height']} {s['r_frame_rate']} {s['codec_name']} {s['profile']} {s['pix_fmt']}, "
        f"{s['color_space']}/{s['color_transfer']}/{s['color_primaries']}, {float(s['duration']):.3f} s |",
        f"| Loudness (muxed) | {mark(ld['ok'])} | {ld['integrated_lufs']} LUFS integrated (target -16 +/- 0.7), "
        f"{ld['true_peak_dbtp']} dBTP (ceiling {MUXED_TP_CEILING}), LRA {ld['lra_lu']} LU, {ld['channels']} ch |",
        f"| Narration ASR | {mark(r['narration']['ok'])} | worst WER "
        f"{max((x['wer'] for x in r['narration']['segments']), default=0):.3f} (limit {WER_MAX}) |",
        f"| Containment | {mark(r['containment']['ok'])} | {r['containment']['checked']} scene renders, "
        f"{len(r['containment']['failures'])} with ink outside the stage |",
        f"| Captions | {mark(r['captions']['ok'])} | {r['captions']['cues']} cues, "
        f"{len(r['captions']['problems'])} problems |",
        "",
    ]
    if "master" in r:
        mm = r["master"]
        lines += [
            f"Master WAV before encode: {mm['lufs']} LUFS, {mm['dbtp']} dBTP, LRA {mm['lra']} LU. "
            f"Track vs timeline drift: {r.get('drift', {})}.",
            "",
        ]
    lines += ["## Narration, segment by segment", "", "| Segment | WER | Hearings | Heard |", "|---|---|---|---|"]
    for x in r["narration"]["segments"]:
        heard = re.sub(r"\s+", " ", x["heard"]).replace("|", "/")
        lines.append(f"| {x['segment']} | {x['wer']:.3f} | {x.get('hearings', 1)} | {heard} |")
        if x.get("first_heard"):
            lines.append(f"| | | first hearing | {re.sub(r'[|]', '/', x['first_heard'])} |")
    lines += [
        "",
        "## Review material",
        "",
        f"- Frames around every cut: `{Path(r['cuts']['sheet']).name}` ({r['cuts']['frames']} frames)",
        f"- One frame per segment: `{Path(r['segments_sheet']).name}`",
        "",
    ]
    if "costs" in r:
        c = r["costs"]
        lines += [
            "## Cost",
            "",
            f"Spent on this build: ${c['spent_usd']:.4f}. Total value of the generations the video uses "
            f"(from receipts, cached or not): ${c['receipts_usd']:.4f}. Unpriced items: {c['unpriced']}.",
            "",
        ]
    lines += [
        "Machine verification is evidence for these gates only; it is not a substitute for watching the video.",
        "",
    ]
    return "\n".join(lines)
