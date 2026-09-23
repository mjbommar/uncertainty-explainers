"""Frames: every one drawn from scratch as a function of programme time.

A frame is the stage (the segment's scene over the ground), possibly mid-
transition, with the chrome on top: a series label and progress rail in the
header, and the burned-in caption in the reserved band. Transitions are live:
both the outgoing and the incoming scene keep moving while
``bc_motion.render_transition`` blends them, so nothing freezes at a cut. A
segment whose scene and parameters equal the previous one's is drawn settled
rather than re-revealed.

``stream`` renders in worker processes and yields frames in order, with a
bounded window so a 4K render does not hold the whole video in memory; its
output goes straight into ``bc_motion.encode.assemble``.
"""

from __future__ import annotations

from collections import deque
from collections.abc import Iterator
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from pathlib import Path

import bc_image as bi
import bc_motion as bm
import numpy as np
from bc_motion.encode import TRANSITION_SECONDS

from . import brand, scenes
from .brand import BAND, HEADER, STAGE, TEXT
from .canvas import Frame, clamp, ease, ground, hexa
from .scenes import Clock, Ctx, tracked
from .spec import Video
from .timeline import Plan, cues

__all__ = ["Job", "frame_at", "poster", "stream"]


@dataclass(frozen=True, slots=True)
class Job:
    video: Video
    plan: Plan
    images: dict[str, np.ndarray]
    scale: int = 1

    @property
    def size(self) -> tuple[int, int]:
        return brand.WIDTH * self.scale, brand.HEIGHT * self.scale


def reveal_seconds(seconds: float) -> float:
    return min(max(2.2, 0.45 * seconds), 3.6)


def _end_params(video: Video) -> dict:
    return {"label": video.series, "title": video.end_card.line, "subtitle": video.end_card.note or None}


def _settled(video: Video, index: int) -> bool:
    if index <= 0:
        return False
    a, b = video.segments[index - 1].scene, video.segments[index].scene
    return a.name == b.name and a.params == b.params


def _stage(job: Job, span_i: int, s: float) -> np.ndarray:
    """The stage for span ``span_i`` at programme time ``s`` (may be past the span's end)."""
    video, plan = job.video, job.plan
    seg_i, start, end = plan.spans[span_i]
    pal = brand.palette(video.theme)
    f = Frame(pal)
    local = max(0.0, s - start)
    total = plan.timeline.total_seconds
    if seg_i < 0:
        name, params, beats, settled = "title_card", _end_params(video), (), False
    else:
        seg = video.segments[seg_i]
        name, params, beats, settled = seg.scene.name, seg.scene.params, plan.beats[seg_i], _settled(video, seg_i)
        if seg.image and "image" not in params:
            params = {**params, "image": f"image:{seg.image}"}
    clock = Clock(
        t=1.0 if settled else clamp(local / reveal_seconds(end - start)),
        local=local,
        seconds=s,
        progress=clamp(s / total),
        duration=end - start,
        beats=beats,
        settled=settled,
    )
    scenes.draw(f, name, params, STAGE, clock, Ctx(images=job.images))
    w, h = job.size
    return f.render(ground(video.theme, w, h), scale=job.scale)


def _chrome_alpha(job: Job, span_i: int, s: float) -> float:
    """Header and rail hide on the title card and the end card, fading in and out."""
    video, plan = job.video, job.plan

    def bare(i: int) -> bool:
        k = plan.spans[i][0]
        return k < 0 or video.segments[k].scene.name == "title_card"

    here = 0.0 if bare(span_i) else 1.0
    if span_i > 0:
        prev = 0.0 if bare(span_i - 1) else 1.0
        into = s - plan.spans[span_i][1]
        return prev + (here - prev) * ease(clamp(into / 0.5), "smoothstep")
    return here


def _chrome(job: Job, span_i: int, s: float, base: np.ndarray) -> np.ndarray:
    video, plan = job.video, job.plan
    pal = brand.palette(video.theme)
    f = Frame(pal)
    a = _chrome_alpha(job, span_i, s)
    if a > 0.002:
        with f.group(opacity=a):
            tracked(f, HEADER.x, HEADER.y + 26, video.series.upper(), size=17, fill=pal.text_faint)
            f.text(HEADER.right, HEADER.y + 26, video.title, size=19, fill=pal.text_faint, anchor="end")
            y = HEADER.bottom + 4
            p = clamp(s / plan.timeline.total_seconds)
            f.line(HEADER.x, y, HEADER.right, y, stroke=hexa(pal.line, 0.8), width=2, cap="butt")
            x = HEADER.x + (HEADER.right - HEADER.x) * p
            f.line(HEADER.x, y, x, y, stroke=hexa(pal.unknown, 0.85), width=2, cap="butt")
            f.circle(x, y, 4, fill=pal.unknown)
    if video.burn_captions:
        text, k = _caption_at(job, s)
        if text:
            _caption(f, text, k)
    if len(f.layers[0][1]) == 0 and len(f.layers) == 1:
        return base
    return f.render(base, scale=job.scale)


_CUES: dict[int, list] = {}


def _caption_at(job: Job, s: float) -> tuple[str | None, float]:
    key = id(job.plan)
    if key not in _CUES:
        _CUES[key] = cues(job.plan)
    ms = s * 1000
    prev_end = -1e9
    for cue in _CUES[key]:
        if cue.start_ms <= ms < cue.end_ms:
            gap = cue.start_ms - prev_end
            k = 1.0 if gap < 120 else clamp((ms - cue.start_ms) / 140)
            k = min(k, 1.0 if cue.end_ms - ms > 140 else clamp((cue.end_ms - ms) / 140))
            return cue.text, k
        prev_end = cue.end_ms
    return None, 0.0


def _caption(f: Frame, text: str, k: float) -> None:
    pal = f.pal
    size = 34
    lines = f.wrap(text, size, BAND.w - 96, TEXT, 500)[:2]
    width = max(f.measure(ln, size, TEXT, 500) for ln in lines) + 64
    lead = size * 1.32
    h = lead * len(lines) + 30
    plate = brand.Box(BAND.cx - width / 2, BAND.bottom - h, width, h)
    with f.group(opacity=k):
        f.rect(plate, fill=hexa(pal.caption_plate, 0.74), r=14)
        for i, ln in enumerate(lines):
            f.text(
                BAND.cx,
                plate.y + 15 + size * 0.95 + i * lead,
                ln,
                size=size,
                fill=pal.caption_text,
                weight=500,
                anchor="middle",
            )


def _span_at(plan: Plan, s: float) -> int:
    for i, (_, a, b) in enumerate(plan.spans):
        if a <= s < b:
            return i
    return len(plan.spans) - 1


def frame_at(job: Job, index: int) -> np.ndarray:
    """The delivered frame ``index`` (uint8, output size)."""
    fps = job.plan.timeline.fps
    s = (index + 0.5) / fps
    i = _span_at(job.plan, s)
    seg_i, start, _ = job.plan.spans[i]
    name = "dissolve" if seg_i < 0 else job.video.segments[seg_i].transition
    dur = TRANSITION_SECONDS.get(name, 0.0)
    into = s - start
    stage = _stage(job, i, s)
    if i > 0 and name != "cut" and into < dur:
        before = _stage(job, i - 1, s)
        stage = bm.render_transition(
            name, before, stage, clamp(into / dur), paper=brand.palette(job.video.theme).rgb("ground")
        )
        stage = bi.to_u8(np.ascontiguousarray(stage))
    return _chrome(job, i, s, np.ascontiguousarray(stage))


# ------------------------------------------------------------------ parallel

_JOB: Job | None = None


def _init(job: Job) -> None:
    global _JOB
    _JOB = job


def _chunk(bounds: tuple[int, int]) -> list[np.ndarray]:
    assert _JOB is not None
    return [frame_at(_JOB, i) for i in range(*bounds)]


def stream(job: Job, *, workers: int = 8, chunk: int = 6) -> Iterator[np.ndarray]:
    """Every frame in order, rendered ``workers`` wide with a bounded look-ahead."""
    total = job.plan.timeline.total_frames
    bounds = [(i, min(total, i + chunk)) for i in range(0, total, chunk)]
    window = workers * 2
    with ProcessPoolExecutor(max_workers=workers, initializer=_init, initargs=(job,)) as pool:
        pending: deque = deque()
        it = iter(bounds)
        for b in it:
            pending.append(pool.submit(_chunk, b))
            if len(pending) >= window:
                break
        while pending:
            frames = pending.popleft().result()
            nxt = next(it, None)
            if nxt is not None:
                pending.append(pool.submit(_chunk, nxt))
            yield from frames


def poster(job: Job, dest: Path, thumb: Path | None = None) -> Path:
    """The title card fully settled, without chrome: the poster, plus a 1280x720 thumbnail."""
    video = job.video
    pal = brand.palette(video.theme)
    f = Frame(pal)
    first = video.segments[0].scene
    params = first.params if first.name == "title_card" else {"title": video.title, "subtitle": video.subtitle}
    scenes.draw(f, "title_card", params, STAGE, Clock(t=1.0, local=30.0, seconds=30.0, settled=True))
    w, h = job.size
    img = f.render(ground(video.theme, w, h), scale=job.scale)
    bi.save(img, dest)
    if thumb is not None:
        bi.save(bi.to_u8(bi.resize(img, 1280, 720)), thumb)
    return dest
