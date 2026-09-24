"""Render paste-ready YouTube fields for one video.

    uv run python -m pipeline.youtube videos/<slug>/script.yaml

Reads `publish/youtube.yaml` (title, description, chapters by segment id,
credits, tags) and writes two files beside it:

- `publish/youtube.txt`: the upload sheet. Plain text, one line per paragraph
  (YouTube keeps every newline it is given, so a wrapped paragraph would stay
  wrapped), URLs on their own lines, and each field headed with its length
  against YouTube's limit, the same layout as understanding-accounting's
  `youtube.txt` files.
- `publish/youtube.md`: the same fields for reading in the repository.

Chapter times are not typed. Each chapter names a segment; its time is that
segment's start on the timeline plus the Da Vinci Math intro, floored to the
second, so a rebuild that moves a segment moves its chapter. The first
chapter is 0:00 and carries the intro. Sources are every key the script's
segments cite, looked up in `research/SOURCES.md`.

Refused: a title over 100 characters, a description over 5000, tags over 500,
a chapter that names no segment, chapters out of order, or two chapters less
than 10 seconds apart (YouTube then ignores all of them).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from itertools import pairwise
from pathlib import Path

import yaml

from . import ROOT
from .package import BRAND_DIR
from .spec import SpecError, load
from .timeline import load_plan

LIMITS = {"title": 100, "description": 5000, "tags": 500}
MIN_CHAPTER_SECONDS = 10


def _sources() -> dict[str, str]:
    """``S01`` -> ``Author (Year). Title. URL`` from the register's table."""
    out = {}
    for line in (ROOT / "research" / "SOURCES.md").read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        m = re.fullmatch(r"\[(S\d+)\]", cells[0]) if cells else None
        if not m or len(cells) < 6:
            continue
        authors, year, title, url = cells[1], cells[2], cells[3], cells[5].strip("<>")
        names = [n.strip() for n in authors.split(";") if n.strip() and n.strip() != "et al."]
        if len(names) > 2:  # keeps a long reading list inside YouTube's 5000 characters
            authors = f"{names[0]} et al."
        stop = "" if title.endswith((".", "?", "!")) else "."
        out[m.group(1)] = f"{authors} ({year}). {title}{stop} {url}"
    return out


def _stamp(seconds: float) -> str:
    s = int(seconds)
    return f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}" if s >= 3600 else f"{s // 60}:{s % 60:02d}"


def _paragraphs(text: str) -> list[str]:
    return [" ".join(ln.strip() for ln in p.splitlines()) for p in text.strip().split("\n\n")]


def render(script: Path) -> dict:
    video = load(script)
    root = script.resolve().parent
    meta = yaml.safe_load((root / "publish" / "youtube.yaml").read_text())
    brand = json.loads((BRAND_DIR / "manifest.json").read_text())
    intro = brand["cues"]["intro"]["seconds"]
    plan = load_plan(video, root / "output")
    starts = {video.segments[i].id: a for i, a, _ in plan.spans if i >= 0}
    faults = []

    chapters = []
    for n, ch in enumerate(meta["chapters"]):
        if ch["segment"] not in starts:
            faults.append(f"chapter {ch['title']!r} names unknown segment {ch['segment']!r}")
            continue
        at = 0.0 if n == 0 else intro + starts[ch["segment"]]
        chapters.append((int(at), ch["title"]))
    if chapters and meta["chapters"][0]["segment"] != video.segments[0].id:
        faults.append("the first chapter must be the first segment (it becomes 0:00)")
    for (a, t0), (b, _) in pairwise(chapters):
        if b - a < MIN_CHAPTER_SECONDS:
            faults.append(f"chapter {t0!r} lasts {b - a} s; YouTube needs {MIN_CHAPTER_SECONDS}")

    cited = sorted({k for seg in video.segments for k in seg.sources}, key=lambda k: int(k[1:]))
    register = _sources()
    missing = [k for k in cited if k not in register]
    if missing:
        faults.append(f"sources not in research/SOURCES.md: {missing}")

    body = _paragraphs(meta["description"])
    blocks = [
        "\n\n".join(body),
        "\n".join(f"{_stamp(a)} {t}" for a, t in chapters),
        f"Made by {brand['brand']}. More lessons on YouTube at {brand['handle']} and on the web:\n{brand['site']}",
        "Sources:\n" + "\n".join(f"[{k}] {register[k]}" for k in cited if k in register),
        meta["credits"] + " Intro and outro music: the harmonic series and a chain of pure fifths, "
        "played on lute, harp, viola, and recorder.",
    ]
    description = "\n\n".join(blocks)
    tags = ", ".join(" ".join(str(t).split()) for t in meta["tags"])
    for field, value in (("title", meta["title"]), ("description", description), ("tags", tags)):
        if len(value) > LIMITS[field]:
            faults.append(f"{field} is {len(value)} characters; YouTube allows {LIMITS[field]}")
    if faults:
        raise SpecError("youtube.yaml refused:\n  " + "\n  ".join(faults))

    rel = root.relative_to(ROOT)
    files = [
        ("video", rel / "publish" / f"{video.slug}.mp4"),
        (
            "thumbnail",
            rel / "publish" / ("thumbnail.png" if (root / "publish" / "thumbnail.png").is_file() else "poster.png"),
        ),
        ("captions", rel / "publish" / f"{video.slug}.vtt"),
    ]
    txt = "\n".join(
        [
            f"=== {video.slug} — status: {meta['status']} ===",
            "",
            f"--- TITLE ({len(meta['title'])}/100) ---",
            meta["title"],
            "",
            f"--- DESCRIPTION ({len(description)}/5000) ---",
            description,
            "",
            f"--- TAGS ({len(tags)}/500) ---",
            tags,
            "",
            "--- FILES ---",
            *(f"{k:<9} {v}" for k, v in files),
            "",
        ]
    )
    (root / "publish" / "youtube.txt").write_text(txt)
    md = "\n".join(
        [
            f"# YouTube: {video.title}",
            "",
            "Rendered from `youtube.yaml` by `pipeline/youtube.py`; paste from `youtube.txt`.",
            "",
            f"**Title** ({len(meta['title'])}/100): {meta['title']}",
            "",
            f"**Description** ({len(description)}/5000):",
            "",
            "```text",
            description,
            "```",
            "",
            f"**Tags** ({len(tags)}/500): {tags}",
            "",
            "**Files:** " + "; ".join(f"{k} `{v}`" for k, v in files),
            "",
        ]
    )
    (root / "publish" / "youtube.md").write_text(md)
    return {
        "title": len(meta["title"]),
        "description": len(description),
        "tags": len(tags),
        "chapters": [f"{_stamp(a)} {t}" for a, t in chapters],
        "sources": len(cited),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("scripts", type=Path, nargs="+")
    a = ap.parse_args(argv)
    for s in a.scripts:
        try:
            print(s.parent.name, json.dumps(render(s)))
        except SpecError as exc:
            print(f"{s}: {exc}", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
