"""Scenes shared by every video in the series.

``roadmap``: the map of a video's stops (docs/STRUCTURE.md, "The roadmap
scene"). A horizontal path with one node per stop, each named by a short
label and a question. It opens a video (``overview``), returns at every bridge
with the next stop lighting up (``travel``), and closes it with every stop lit
and every takeaway shown (``summary``).

Imported by one line at the end of ``pipeline/scenes.py``.
"""

from __future__ import annotations

import math
from typing import Any

from .brand import DISPLAY, MONO, TEXT, Box
from .canvas import Frame, at, clamp, ease, hexa, lerp, mix_hex, pulse
from .scenes import Clock, Ctx, header_block, scene

__all__ = ["roadmap"]

MODES = ("overview", "travel", "summary")

_DEMO_STOPS = [
    {
        "label": "Chance or ignorance",
        "question": "Is the gap chance, or something we lack?",
        "takeaway": "Chance stays; ignorance can be closed by looking harder.",
    },
    {
        "label": "Can it be measured",
        "question": "Is there a group of cases to count?",
        "takeaway": "A number needs a group of cases behind it.",
    },
    {
        "label": "Unknown odds",
        "question": "What if the odds themselves are unknown?",
        "takeaway": "Where odds are unknown, one number claims too much.",
    },
    {
        "label": "Where mine sits",
        "question": "Where on the scale does my forecast stand?",
        "takeaway": "Every forecast should say where on the scale.",
    },
    {
        "label": "Words for odds",
        "question": "Which words carry a number, and which don't?",
        "takeaway": "Words like likely hide ranges that readers disagree about.",
    },
    {
        "label": "Saying it plainly",
        "question": "How do we say all this out loud?",
        "takeaway": "Say the kind, then the number, then the confidence.",
    },
]


def _resolve(p: dict[str, Any]) -> tuple[list[dict[str, Any]], int, str]:
    stops = list(p["stops"])
    n = len(stops)
    if not 4 <= n <= 6:
        raise ValueError(f"roadmap: needs 4 to 6 stops, got {n}")
    for s in stops:
        if "label" not in s or "question" not in s:
            raise ValueError(f"roadmap: every stop needs a label and a question: {s!r}")
    cur = int(p.get("current", -1))
    if not -1 <= cur <= n:
        raise ValueError(f"roadmap: current must be -1..{n}, got {cur}")
    mode = str(p.get("mode") or ("overview" if cur < 0 else "summary" if cur >= n else "travel"))
    if mode not in MODES:
        raise ValueError(f"roadmap: mode must be one of {MODES}, got {mode!r}")
    if mode == "summary":
        cur = n
    return stops, cur, mode


@scene(
    "roadmap",
    required=("stops",),
    optional=("current", "mode"),
    demo={
        "kicker": "Where we have been",
        "heading": "Two kinds of not knowing, in six steps",
        "mode": "summary",
        "current": 6,
        "stops": _DEMO_STOPS,
    },
)
def roadmap(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """The video's stops on one path: done in teal, the current one amber, the rest to come."""
    pal = f.pal
    stops, cur, mode = _resolve(p)
    n = len(stops)
    inner = header_block(f, box, p, c)
    live = not c.settled

    col = inner.w / n
    text_w = col - 36

    def X(i: float) -> float:
        return inner.x + col * (i + 0.5)

    # ---- measure every text block first, so the composition can be centred.
    # Under each label: the takeaway in summary mode, the question in the overview.
    note_key = {"summary": "takeaway", "overview": "question"}.get(mode)
    notes = [str(s.get(note_key) or "") if note_key else "" for s in stops]

    def fits(rows: int, size: float, width: float) -> bool:
        return all(len(f.wrap(t, size, width)) <= rows for t in notes if t)

    # One column per stop when every note takes two lines at a readable size. Otherwise the
    # blocks alternate above and below the path, so each gets two columns of width and stays
    # at two lines: small type or a cut word would be worse.
    narrow = col - 36
    stagger = any(notes) and not fits(2, 24, narrow)
    text_w = min(2 * col - 120, 500) if stagger else narrow
    tiers = [(2, sz) for sz in (27, 26, 25, 24)] + [(3, sz) for sz in (25, 24, 23, 22)]
    take_size = next((float(sz) for rows, sz in tiers if fits(rows, sz, text_w)), 22.0)
    takes = [f.wrap(t, take_size, text_w) if t else [] for t in notes]
    take_lead = take_size * 1.32
    take_rows = max(len(t) for t in takes)

    names = [str(s["label"]) for s in stops]
    label_size = next(
        (sz for sz in (30.0, 28.0, 26.0) if all(len(f.wrap(t, sz, text_w, TEXT, 600)) <= 2 for t in names)), 24.0
    )
    labels = [f.wrap(t, label_size, text_w, TEXT, 600) for t in names]
    label_lead = label_size * 1.2
    label_rows = max(len(ls) for ls in labels)

    node_r = 24.0
    gap = 26.0  # node edge to its text block
    block_h = label_size * 0.8 + (label_rows - 1) * label_lead + label_size * 0.25
    if take_rows:
        block_h += 50 + take_size * 0.8 + (take_rows - 1) * take_lead - label_size * 0.25 + take_size * 0.25

    def up(i: int) -> bool:
        return stagger and i % 2 == 0

    q_text = str(stops[cur]["question"]) if 0 <= cur < n else ""
    q_size = f.fit(q_text, min(inner.w, 1200), 56, 40, DISPLAY) if q_text else 0.0

    above = (q_size + 70) if q_text else 60  # question cap height + gap to the node
    if stagger:
        above = max(above, node_r + gap + block_h)
    below = node_r + gap + block_h
    # The path sits at the same height in every mode, so a dissolve from one visit to the
    # next never doubles it; it moves only when a mode would not otherwise fit.
    y = clamp(inner.cy, inner.y + above, inner.bottom - below)

    # ---- timing
    reveal_track = at(c.t, 0.0, 0.35, "ease-in-out-cubic") if live and mode == "overview" else 1.0
    if mode == "travel":
        start_i, end_i = max(0, cur - 1), cur
    elif mode == "summary":
        start_i, end_i = 0, n - 1
    else:
        start_i, end_i = 0, max(0, cur)
    kf = at(c.t, 0.12, 0.62, "ease-in-out-cubic") if live else 1.0
    if (mode == "travel" and cur == 0) or mode == "summary":
        kf = 1.0  # nothing to travel: the first stop, or the zoom-out after the last
    head_pos = lerp(float(start_i), float(end_i), kf)  # in node units
    if cur < 0:
        head_pos = 0.0
    x_first, x_last = X(0), X(n - 1)
    head = X(head_pos)

    # ---- the track and its fill
    track_w = 6.0
    reach = lerp(x_first, x_last, reveal_track)
    f.line(x_first, y, reach, y, stroke=pal.line, width=track_w)
    if head > x_first + 0.5:
        # Solid teal up to the last completed node, then a teal-to-amber run into the head.
        solid_end = X(min(head_pos, float(max(0, cur - 1)))) if 0 <= cur < n else head
        if solid_end > x_first:
            f.line(x_first, y, solid_end, y, stroke=pal.known, width=track_w)
        if head > solid_end + 0.5:
            segs = 24
            for s in range(segs):
                a = lerp(solid_end, head, s / segs)
                b = lerp(solid_end, head, (s + 1) / segs)
                tone = mix_hex(pal.known, pal.unknown, (s + 0.5) / segs)
                f.line(a, y, min(b + 1.5, head), y, stroke=tone, width=track_w, cap="butt")
    # Ambient drift: a soft glint that runs along the filled path (or the bare track) and loops.
    run_end = head if head > x_first + 40 else x_last
    span = run_end - x_first
    if span > 1:
        g = (c.seconds / 5.5) % 1.0
        gx = x_first + span * g
        glint_a = (0.55 if head > x_first + 40 else 0.22) * math.sin(math.pi * g) * reveal_track
        for k in range(6):
            w = 90 - 14 * k
            f.line(
                max(x_first, gx - w / 2),
                y,
                min(run_end, gx + w / 2),
                y,
                stroke=hexa(pal.text, 0.10 + 0.05 * k),
                width=track_w,
                opacity=glint_a,
                cap="butt",
            )

    # ---- nodes, numbers, labels
    for i in range(n):
        x = X(i)
        kn = at(c.t, 0.05 + 0.35 * i / n, 0.2 + 0.35 * i / n) if live and mode == "overview" else 1.0
        if kn <= 0.002:
            continue
        pop = ease(kn, "ease-out-back")
        arrived = clamp((head_pos - i) * 4 + 1) if head_pos > i - 0.25 else 0.0
        if i < cur:
            # A node that was current on the last visit hands its amber to teal as the fill leaves it.
            handing = mode == "travel" and i == cur - 1 and live
            state_col = mix_hex(pal.unknown, pal.known, kf) if handing else pal.known
            fill, ring, num = state_col, state_col, pal.ground
            lab_col, lab_w = (pal.text if mode == "summary" else pal.text_soft), 600
        elif i == cur:
            amb = arrived if live else 1.0
            fill = mix_hex(pal.surface_2, pal.unknown, amb)
            ring, num = mix_hex(pal.line, pal.unknown, amb), mix_hex(pal.text_faint, pal.ground, amb)
            lab_col, lab_w = mix_hex(pal.text_soft, pal.text, amb), 600
            g = pulse(c.seconds, 2.4)
            f.circle(x, y, node_r + 12 + 9 * g, fill=pal.unknown, opacity=(0.10 + 0.12 * g) * amb)
            f.circle(x, y, node_r + 6, stroke=pal.unknown, width=2, opacity=(0.35 + 0.3 * g) * amb)
        else:
            fill, ring, num = pal.surface, pal.line, pal.text_faint
            lab_col, lab_w = (pal.text if mode == "overview" else pal.text_faint), 600
        r = node_r * pop
        f.circle(x, y, r + 3, fill=pal.ground, opacity=kn)
        f.circle(x, y, r, fill=fill, stroke=ring, width=3, opacity=kn)
        with f.group(opacity=kn):
            f.text(x, y + 8, str(i + 1), size=22, fill=num, family=MONO, anchor="middle", weight=700)
        top_y = y - node_r - gap - block_h if up(i) else y + node_r + gap
        wide = max(
            [f.measure(ln, label_size, TEXT, 600) for ln in labels[i]] + [f.measure(ln, take_size) for ln in takes[i]]
        )
        bx = clamp(x, inner.x + wide / 2, inner.right - wide / 2)
        ly = top_y + label_size * 0.8
        with f.group(opacity=kn):
            f.text_lines(bx, ly, labels[i], size=label_size, fill=lab_col, leading=1.2, anchor="middle", weight=lab_w)
        if takes[i]:
            t0 = 0.3 if mode == "summary" else 0.12
            kt = at(c.t, t0 + 0.55 * i / n, t0 + 0.15 + 0.55 * i / n) if live else 1.0
            ty = ly + (label_rows - 1) * label_lead + 50 + take_size * 0.8
            with f.group(opacity=kt, dy=(1 - kt) * 10):
                tick_y = ty - take_size * 0.8 - 20
                tick = hexa(pal.known if mode == "summary" else pal.line, 0.8)
                f.line(bx - 18, tick_y, bx + 18, tick_y, stroke=tick, width=2)
                f.text_lines(bx, ty, takes[i], size=take_size, fill=pal.text_soft, leading=1.32, anchor="middle")

    # ---- the current stop's question, above its node
    if q_text:
        kq = at(c.t, 0.5, 0.85) if live else 1.0
        if mode == "travel" and cur == 0 and live:
            kq = at(c.t, 0.2, 0.6)
        half = f.measure(q_text, q_size, DISPLAY) / 2
        qx = clamp(X(cur), inner.x + half, inner.right - half)
        qy = y - 70
        with f.group(opacity=kq, dy=(1 - kq) * 14):
            f.text(qx, qy, q_text, size=q_size, fill=pal.text, family=DISPLAY, anchor="middle")
