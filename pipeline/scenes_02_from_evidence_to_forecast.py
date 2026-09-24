"""Scenes for video 2, "From evidence to forecast".

Registered into :data:`pipeline.scenes.REGISTRY` on import (the last line of
``scenes.py`` imports this module). Every scene follows the house contract:
draw only inside ``box``, colour by palette role, stage reveals on
``clock.beat(i)``, and keep one ambient motion on ``clock.seconds``.

Several scenes take a ``step`` or ``upto`` parameter so one picture can be
built over consecutive segments: everything before the current step is drawn
complete, and only the new step animates. Pass ``steady: true`` on the later
steps so the heading does not fade in again.
"""

from __future__ import annotations

import math
from dataclasses import replace
from typing import Any

import numpy as np

from .brand import DISPLAY, MONO, Box
from .canvas import Frame, at, clamp, ease, hexa, lerp, mix_hex, pulse
from .scenes import Clock, Ctx, _pack, _urn_path, ball, header_block, rng, role, scene, tracked

__all__: list[str] = []


def _head(f: Frame, box: Box, p: dict[str, Any], c: Clock) -> Box:
    """``header_block``, drawn already settled when the scene continues a previous step."""
    return header_block(f, box, p, replace(c, settled=True) if p.get("steady") else c)


def _stepk(p: dict[str, Any], c: Clock, key: str, need: int, beat: int, dur: float = 0.9) -> float:
    """1 for a step already shown, the eased beat for the current step, 0 for a later one."""
    cur = int(p.get(key, 0))
    if cur > need:
        return 1.0
    if cur < need:
        return 0.0
    return c.beat(beat, dur=dur, spacing=1.1)


# ------------------------------------------------------------------ icon_array


@scene(
    "icon_array",
    required=(),
    optional=("step", "total", "sick", "sick_pos", "false_pos", "cols", "labels", "steady", "seed"),
    demo={"heading": "One thousand women, one test", "step": 2},
)
def icon_array(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """1,000 people as dots: the sick, the positives, then the positives gathered and counted."""
    pal = f.pal
    inner = _head(f, box, p, c)
    total = int(p.get("total", 1000))
    sick, sick_pos, false_pos = int(p.get("sick", 10)), int(p.get("sick_pos", 8)), int(p.get("false_pos", 95))
    cols = int(p.get("cols", 50))
    rows = math.ceil(total / cols)
    labels = p.get("labels") or [
        f"{total:,} women",
        f"{sick} have cancer",
        f"{sick_pos} of {sick} test positive",
        f"{false_pos} of {total - sick} also test positive",
        f"{sick_pos + false_pos} positives",
        f"{sick_pos} / {sick_pos + false_pos} = {100 * sick_pos / (sick_pos + false_pos):.1f}%",
    ]
    grid, panel = inner.split_x(0.66, gap=60)
    s = min(grid.w / cols, (grid.h - 10) / rows)
    gx = grid.x + (grid.w - s * cols) / 2
    gy = grid.y + (grid.h - s * rows) / 2
    r = s * 0.34
    perm = rng(int(p.get("seed", 17))).permutation(total)
    kind = np.zeros(total, dtype=int)  # 0 healthy, 1 sick negative, 2 sick positive, 3 false positive
    kind[perm[:sick]] = 1
    kind[perm[:sick_pos]] = 2
    kind[perm[sick : sick + false_pos]] = 3

    k_fill = (1.0 if int(p.get("step", 0)) > 0 or c.settled else at(c.t, 0.05, 0.6, "ease-in-out-cubic"))
    k_sick = _stepk(p, c, "step", 0, 1)
    k_tp = _stepk(p, c, "step", 1, 0)
    k_fp = _stepk(p, c, "step", 1, 1, dur=1.6)
    k_gather = _stepk(p, c, "step", 2, 0, dur=1.4)
    k_count = _stepk(p, c, "step", 2, 1)

    # Where the positives gather: a compact block in the middle of the grid.
    pos_idx = [int(i) for i in np.nonzero(kind >= 2)[0]]
    pos_idx.sort(key=lambda i: (kind[i] != 2, i))
    bcols = 13
    brows = math.ceil(len(pos_idx) / bcols)
    bs = s * 1.9
    bx = grid.cx - bcols * bs / 2
    by = grid.cy - brows * bs / 2
    home = {i: (bx + (j % bcols + 0.5) * bs, by + (j // bcols + 0.5) * bs) for j, i in enumerate(pos_idx)}
    g = ease(k_gather, "ease-in-out-cubic")
    neutral = pal.text_faint
    fp_sorted = np.sort(perm[sick : sick + false_pos])
    fp_order = {int(v): (j + 0.5) / false_pos for j, v in enumerate(fp_sorted)}
    for i in range(total):
        row, col = divmod(i, cols)
        x0 = gx + (col + 0.5) * s
        y0 = gy + (row + 0.5) * s
        appear = clamp((k_fill * (rows + 6) - row) / 6)
        if appear <= 0:
            continue
        kd = kind[i]
        x, y, rr = x0, y0, r
        dim = 1.0
        if kd >= 2 and g > 0:
            hx, hy = home[i]
            x, y, rr = lerp(x0, hx, g), lerp(y0, hy, g), lerp(r, r * 1.7, g)
        elif g > 0:
            dim = lerp(1.0, 0.18, g)
        is_sick = kd in (1, 2)
        fill = mix_hex(neutral, pal.unknown, k_sick) if is_sick else neutral
        base_op = (0.55 if not is_sick else lerp(0.55, 1.0, k_sick)) * appear * dim
        if kd == 2 and k_count > 0:
            base_op = 1.0
            rr *= 1 + 0.12 * pulse(c.seconds + i * 0.3, 1.8) * k_count
        f.circle(x, y, rr, fill=fill, opacity=base_op)
        ring_k = k_tp if kd == 2 else k_fp if kd == 3 else 0.0
        if kd == 3:
            order = fp_order[i]
            ring_k = clamp((k_fp * 1.4 - order * 0.9) / 0.5) if k_fp < 1 else 1.0
        if ring_k > 0:
            f.circle(x, y, rr + 3.2 * (1 + g * 0.5), stroke=pal.known, width=2.4, opacity=ring_k * dim)
    if k_sick > 0 and g < 1:
        tw = 0.5 + 0.5 * pulse(c.seconds, 2.4)
        for i in np.nonzero((kind == 1) | (kind == 2))[0]:
            row, col = divmod(int(i), cols)
            f.circle(
                gx + (col + 0.5) * s, gy + (row + 0.5) * s, r * 2.2, fill=pal.unknown, opacity=0.12 * tw * k_sick * (1 - g)
            )
    if g > 0.02:
        f.rect(
            Box(bx - 18, by - 18, bcols * bs + 36, brows * bs + 36),
            stroke=hexa(pal.known, 0.6),
            width=2,
            r=16,
            opacity=g,
            dash=[10, 8],
        )

    # The counting panel.
    ks = [k_fill, k_sick, k_tp, k_fp, k_gather, k_count]
    tones = [pal.text_soft, pal.unknown, pal.known, pal.known, pal.text, pal.unknown]
    y = panel.y + 60
    for i, (label, k) in enumerate(zip(labels, ks, strict=False)):
        if k <= 0:
            y += 74 if i < 5 else 0
            continue
        big = i == 5
        size = 64 if big else 36
        with f.group(opacity=k, dx=(1 - k) * 24):
            if big:
                y += 30
                glow = 0.7 + 0.3 * pulse(c.seconds, 2.6)
                f.text(panel.x, y + 40, str(label), size=f.fit(str(label), panel.w, size, 36, MONO), fill=tones[i], family=MONO, alpha=glow)
            else:
                f.circle(panel.x + 10, y - 12, 7, fill=tones[i])
                f.text(panel.x + 34, y, str(label), size=f.fit(str(label), panel.w - 40, size, 24), fill=pal.text)
        y += 74


# ------------------------------------------------------------------ cube_three_ways


def _cube(f: Frame, cx: float, cy: float, a: float, *, fill: str | None, stroke: str, op: float, width: float = 3) -> None:
    """An isometric cube of edge ``a`` whose bottom-front corner sits at (cx, cy)."""
    dx, dy = a * math.cos(math.pi / 6), a * math.sin(math.pi / 6)
    # Faces from the bottom-front vertex (cx, cy).
    b = (cx, cy)
    r_ = (cx + dx, cy - dy)
    l_ = (cx - dx, cy - dy)
    t = (cx, cy - a)
    tr = (cx + dx, cy - dy - a)
    tl = (cx - dx, cy - dy - a)
    back = (cx, cy - 2 * dy - a)
    faces = [([b, r_, tr, t], 0.85), ([b, l_, tl, t], 0.65), ([t, tr, back, tl], 1.0)]
    for pts, shade in faces:
        f.polygon(pts, fill=hexa(fill, shade * 0.9) if fill else None, stroke=stroke, width=width, opacity=op)


@scene(
    "cube_three_ways",
    required=("answers",),
    optional=("event",),
    demo={
        "heading": "One event, three answers",
        "event": "side under 1/2 ft",
        "answers": [
            {"measure": "Even over side length", "value": "1/2", "frac": 0.5},
            {"measure": "Even over face area", "value": "1/4", "frac": 0.25},
            {"measure": "Even over volume", "value": "1/8", "frac": 0.125},
        ],
    },
)
def cube_three_ways(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """A unit cube holding the half-size cube, and the three 'ignorance' answers for that one event."""
    pal = f.pal
    inner = _head(f, box, p, c)
    left, right = inner.split_x(0.36, gap=60)
    a = min(left.w * 0.45, left.h * 0.5 - 60)
    cx = left.cx
    cy = left.cy + a - 20
    k0 = at(c.t, 0.0, 0.35) if not c.settled else 1.0
    breathe = 1 + 0.015 * math.sin(c.seconds * 1.3)
    _cube(f, cx, cy, a * breathe, fill=None, stroke=pal.text_soft, op=k0, width=3)
    k_in = c.beat(0, dur=1.0, spacing=1.0)
    _cube(f, cx, cy, a * 0.5 * breathe, fill=pal.unknown, stroke=pal.unknown, op=k_in, width=2)
    ev = p.get("event")
    if ev:
        f.text(cx, cy + 70, str(ev), size=30, fill=pal.unknown, anchor="middle", alpha=k_in)
    answers = list(p["answers"])
    n = len(answers)
    rowh = right.h / max(1, n)
    for i, ans in enumerate(answers):
        k = c.beat(i + 1, dur=0.9, spacing=1.0)
        y = right.y + rowh * i + rowh * 0.5
        x0, x1 = right.x, right.right - 220
        with f.group(opacity=k, dy=(1 - k) * 24):
            f.text(x0, y - 30, str(ans["measure"]), size=34, fill=pal.text)
            f.rect(Box(x0, y, x1 - x0, 22), fill=pal.surface_2, r=11)
            w = (x1 - x0) * float(ans["frac"]) * ease(clamp((k - 0.3) / 0.7))
            if w > 1:
                f.rect(Box(x0, y, w, 22), fill=pal.known if i == 0 else pal.unknown, r=11)
            sweep = (c.seconds * 0.3 + i * 0.33) % 1.0
            f.circle(x0 + (x1 - x0) * float(ans["frac"]) * sweep, y + 11, 6, fill=hexa("#ffffff", 0.3))
            f.text(right.right, y + 24, str(ans["value"]), size=72, fill=pal.text, family=MONO, anchor="end")


# ------------------------------------------------------------------ interval_rows


@scene(
    "interval_rows",
    required=("rows",),
    optional=("ticks", "then_beat", "image", "axis_label", "steady"),
    demo={
        "heading": "One number, or a range",
        "rows": [
            {"label": "Coin tossed 100 times", "lo": 0.5, "hi": 0.5, "note": "1/2"},
            {"label": "Coin never seen", "lo": 0.5, "hi": 0.5, "then": {"lo": 0.0, "hi": 1.0}, "then_note": "0 to 1"},
        ],
        "ticks": [{"v": 0, "label": "0"}, {"v": 0.5, "label": "1/2"}, {"v": 1, "label": "1"}],
        "then_beat": 2,
    },
)
def interval_rows(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Rows on a 0-1 axis: a dot for a single probability, a bar for a range; a row may widen or move on a beat."""
    pal = f.pal
    inner = _head(f, box, p, c)
    rows = list(p["rows"])
    img = ctx.image(p.get("image"))
    label_w = 470
    x0 = inner.x + label_w + 40
    x1 = inner.right - 250
    axis_y = inner.bottom - 60
    top = inner.y + 20
    rowh = min(150.0, (axis_y - top - 20) / max(1, len(rows)))

    def X(v: float) -> float:
        return lerp(x0, x1, clamp(v))

    k0 = at(c.t, 0.0, 0.3) if not c.settled or p.get("steady") else 1.0
    if p.get("steady"):
        k0 = 1.0
    f.line(x0, axis_y, x1, axis_y, stroke=pal.line, width=2, opacity=k0)
    ticks = p.get("ticks") or [{"v": 0, "label": "0"}, {"v": 0.5, "label": "0.5"}, {"v": 1, "label": "1"}]
    for tk in ticks:
        v = float(tk["v"])
        f.line(X(v), top, X(v), axis_y + 12, stroke=hexa(pal.line, 0.5), width=1, opacity=k0)
        f.text(X(v), axis_y + 48, str(tk.get("label", v)), size=28, fill=pal.text_faint, family=MONO, anchor="middle", alpha=k0)
    al = p.get("axis_label")
    if al:
        f.text(inner.x + label_w, axis_y + 48, str(al), size=26, fill=pal.unknown, anchor="end", alpha=k0)
    tb = int(p.get("then_beat", len(rows)))
    km = c.beat(tb, dur=1.2, name="ease-in-out-cubic", spacing=1.2)
    for i, row in enumerate(rows):
        k = 1.0 if row.get("shown") else c.beat(i, dur=0.8, spacing=1.2)
        if k <= 0:
            continue
        y = top + rowh * (i + 0.5)
        then = row.get("then")
        m = km if then else 0.0
        lo = lerp(float(row["lo"]), float(then["lo"]) if then else float(row["lo"]), m)
        hi = lerp(float(row["hi"]), float(then["hi"]) if then else float(row["hi"]), m)
        tone = role(pal, row.get("tone"), "known")
        if then and m > 0:
            tone = mix_hex(tone, role(pal, row.get("then_tone"), "unknown"), m)
        with f.group(opacity=k, dx=(1 - k) * -20):
            lines = f.wrap(str(row["label"]), 34, label_w - 10)[:2]
            ly = y + 12 - (len(lines) - 1) * 21
            for j, ln in enumerate(lines):
                f.text(inner.x + label_w, ly + j * 42, ln, size=34, fill=pal.text, anchor="end")
        a, b = X(lo), X(hi)
        h = 30
        if b - a < 3:
            glow = pulse(c.seconds + i, 2.4)
            f.circle(a, y, 22 + 5 * glow, fill=tone, opacity=0.2 * k)
            f.circle(a, y, 15, fill=tone, opacity=k)
        else:
            f.rect(Box(a, y - h / 2, b - a, h), fill=hexa(tone, 0.35), r=h / 2, opacity=k)
            f.line(a, y - 22, a, y + 22, stroke=tone, width=4, opacity=k)
            f.line(b, y - 22, b, y + 22, stroke=tone, width=4, opacity=k)
            sweep = (c.seconds * 0.35 + i * 0.4) % 1.0
            f.circle(lerp(a, b, sweep), y, 8, fill=tone, opacity=0.8 * k)
        note = row.get("then_note") if then and m > 0.5 else row.get("note")
        if note:
            f.text(max(a, b) + 34, y + 11, str(note), size=32, fill=tone, family=MONO, alpha=k)
    if img is not None:
        ki = c.beat(0, dur=0.8, name="ease-out-back", spacing=0.4)
        side = 170
        bob = 4 * math.sin(c.seconds * 1.1)
        f.image(img, Box(inner.right - side, axis_y - side - 40 + bob, side, side), opacity=ki)


# ------------------------------------------------------------------ big_number


@scene(
    "big_number",
    required=("value",),
    optional=("prefix", "suffix", "label", "sub", "image", "decimals", "count"),
    demo={"value": 1826214, "suffix": " to 1", "label": "Laplace's odds that the sun rises tomorrow", "sub": "after 1,826,213 sunrises"},
)
def big_number(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """A large number counting up to its value, a label above, a second line arriving on the next beat."""
    pal = f.pal
    inner = _head(f, box, p, c)
    img = ctx.image(p.get("image"))
    cx = inner.cx + (110 if img is not None else 0)
    cy = inner.cy + 10
    value = float(p["value"])
    k = at(c.t, 0.05, 0.85, "ease-out-cubic") if not c.settled else 1.0
    v = value * k if p.get("count", True) else value
    dec = int(p.get("decimals", 0))
    num = f"{p.get('prefix', '')}{v:,.{dec}f}{p.get('suffix', '')}"
    full = f"{p.get('prefix', '')}{value:,.{dec}f}{p.get('suffix', '')}"
    size = f.fit(full, inner.w * (0.62 if img is not None else 0.8), 150, 70, MONO)
    k0 = at(c.t, 0.0, 0.25) if not c.settled else 1.0
    f.text(cx, cy + size * 0.35, num, size=size, fill=pal.text, family=MONO, anchor="middle", alpha=k0)
    label = p.get("label")
    if label:
        f.text(cx, cy - size * 0.75, str(label), size=38, fill=pal.text_soft, anchor="middle", alpha=k0)
    half = 220 * ease(k)
    glow = 0.6 + 0.4 * pulse(c.seconds, 2.8)
    f.line(cx - half, cy + size * 0.35 + 50, cx + half, cy + size * 0.35 + 50, stroke=pal.unknown, width=3, opacity=k0 * glow)
    sub = p.get("sub")
    if sub:
        ks = c.beat(1, dur=0.9, spacing=1.6)
        f.text(cx, cy + size * 0.35 + 120, str(sub), size=36, fill=pal.unknown, anchor="middle", alpha=ks)
    if img is not None:
        ki = c.beat(0, dur=0.9, name="ease-out-back", spacing=0.4)
        side = 260
        rise = 8 * math.sin(c.seconds * 0.8)
        f.image(img, Box(inner.x + 20, cy - side / 2 + rise, side, side), opacity=ki)


# ------------------------------------------------------------------ card_row


@scene(
    "card_row",
    required=("cards",),
    optional=("ghost", "highlight", "steady"),
    demo={
        "heading": "Three things 'probably' can mean",
        "cards": [
            {"title": "Evidence", "line": "How strongly the data support a claim"},
            {"title": "Belief", "line": "How confident a person is", "tone": "unknown"},
            {"title": "Tendency", "line": "A physical disposition, whatever anyone thinks", "tone": "cool", "image": "image:icon"},
        ],
        "ghost": {"title": "Not on the list", "line": "The explanation nobody thought of"},
    },
)
def card_row(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Cards in a row, one per beat; an optional dashed 'ghost' card arrives last; one may be highlighted."""
    pal = f.pal
    inner = _head(f, box, p, c)
    cards = list(p["cards"])
    ghost = p.get("ghost")
    n = len(cards) + (1 if ghost else 0)
    gap = 36
    cw = (inner.w - gap * (n - 1)) / n
    has_img = any(isinstance(it, dict) and it.get("image") for it in cards)
    ch = min(inner.h - 40, 600.0 if has_img else 470.0)
    y0 = inner.y + (inner.h - ch) / 2 - 10
    hl = p.get("highlight")
    for i in range(n):
        is_ghost = ghost is not None and i == len(cards)
        item = ghost if is_ghost else cards[i]
        k = c.beat(i, dur=0.9, spacing=1.3)
        if k <= 0:
            continue
        card = Box(inner.x + i * (cw + gap), y0, cw, ch)
        tone = pal.text_faint if is_ghost else role(pal, item.get("tone"), "known")
        bob = 4 * math.sin(c.seconds * 1.0 + i * 1.4)
        with f.group(opacity=k, dy=(1 - k) * 30 + bob):
            if is_ghost:
                g = 0.45 + 0.35 * pulse(c.seconds, 3.0)
                f.rect(card, stroke=hexa(pal.text_soft, g), width=3, r=22, dash=[14, 10])
            else:
                f.rect(card, fill=pal.surface, r=22)
                f.rect(Box(card.x, card.y, card.w, 6), fill=tone, r=3)
                if hl is not None and int(hl) == i:
                    g = pulse(c.seconds, 2.6)
                    f.rect(card, stroke=hexa(tone, 0.5 + 0.4 * g), width=3, r=22)
            title = str(item["title"])
            size = f.fit(title, card.w - 70, 54, 32, DISPLAY)
            f.text(card.x + 36, card.y + 96, title, size=size, fill=pal.text_soft if is_ghost else pal.text, family=DISPLAY)
            f.line(card.x + 36, card.y + 130, card.x + 96, card.y + 130, stroke=tone, width=3)
            line = item.get("line")
            img = ctx.image(item.get("image"))
            if line:
                lines = f.wrap(str(line), 32, card.w - 72)[: 2 if img is not None else 5]
                f.text_lines(card.x + 36, card.y + 190, lines, size=32, fill=pal.text_soft, leading=1.32)
        if img is not None:
            top = card.y + 270
            side = min(card.w - 80, card.bottom - top - 24)
            if side > 20:
                f.image(img, Box(card.cx - side / 2, top + bob + (1 - k) * 30, side, side), opacity=k)


# ------------------------------------------------------------------ induction_gap


@scene(
    "induction_gap",
    required=(),
    optional=("count", "past_label", "future_label", "gap_label", "steady"),
    demo={
        "heading": "From the past to tomorrow",
        "count": 14,
        "past_label": "every sunrise so far",
        "future_label": "tomorrow",
        "gap_label": "assumed: the future will be like the past",
    },
)
def induction_gap(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """A row of past observations, then a dashed leap over a gap to an open 'tomorrow'."""
    pal = f.pal
    inner = _head(f, box, p, c)
    n = int(p.get("count", 14))
    y = inner.cy - 10
    x0, xg = inner.x + 60, inner.x + inner.w * 0.6
    xf = inner.right - 120
    step = (xg - x0) / max(1, n - 1)
    k_past = c.beat(0, dur=1.6, spacing=1.2)
    f.line(x0 - 30, y, lerp(x0 - 30, xg, k_past), y, stroke=pal.line, width=3)
    for i in range(n):
        ki = clamp((k_past * (n + 3) - i) / 3)
        if ki <= 0:
            continue
        x = x0 + i * step
        tw = 0.8 + 0.2 * pulse(c.seconds + i * 0.4, 3.2)
        f.circle(x, y, 24 * ease(ki, "ease-out-back"), fill=pal.unknown, opacity=tw)
        f.circle(x, y, 34 * ki, stroke=hexa(pal.unknown, 0.35), width=2)
    pl = p.get("past_label")
    if pl:
        f.text((x0 + xg) / 2, y + 90, str(pl), size=34, fill=pal.text_soft, anchor="middle", alpha=k_past)
    k_gap = c.beat(1, dur=1.2, spacing=1.2)
    if k_gap > 0:
        pts = []
        m = 40
        for j in range(int(m * k_gap) + 1):
            u = j / m
            pts.append((lerp(xg, xf, u), y - math.sin(u * math.pi) * 150))
        for a, b in zip(pts[::2], pts[1::2], strict=False):
            f.line(a[0], a[1], b[0], b[1], stroke=pal.known, width=4)
        q = 0.6 + 0.4 * pulse(c.seconds, 2.2)
        f.circle(xf, y, 30, stroke=pal.known, width=4, opacity=k_gap)
        f.text(xf, y + 20, "?", size=56, fill=pal.known, family=DISPLAY, anchor="middle", alpha=k_gap * q)
        fl = p.get("future_label")
        if fl:
            f.text(xf, y + 90, str(fl), size=34, fill=pal.text_soft, anchor="middle", alpha=k_gap)
    gl = p.get("gap_label")
    if gl:
        kl = c.beat(2, dur=0.9, spacing=1.2)
        f.text((xg + xf) / 2, y - 190, str(gl), size=f.fit(str(gl), inner.w * 0.55, 34, 24), fill=pal.known, anchor="middle", alpha=kl)


# ------------------------------------------------------------------ sort_table


@scene(
    "sort_table",
    required=("rows",),
    optional=("upto", "columns", "steady", "by_beats"),
    demo={
        "heading": "Four kinds of claim",
        "rows": [
            {"term": "Forecast", "basis": "the present state", "check": "yes, scored"},
            {"term": "Projection", "basis": "an assumed path", "check": "only in part"},
            {"term": "Scenario", "basis": "a plausible story", "check": "no probability"},
            {"term": "Counterfactual", "basis": "a changed past", "check": "never directly"},
        ],
        "upto": 3,
    },
)
def sort_table(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """A table built one row per segment; the newest row slides in and glows, older rows stay."""
    pal = f.pal
    inner = _head(f, box, p, c)
    rows = list(p["rows"])
    upto = int(p.get("upto", len(rows) - 1))
    cols = p.get("columns") or ["Claim", "Conditional on", "Checkable later?"]
    xs = [inner.x + 30, inner.x + inner.w * 0.34, inner.x + inner.w * 0.7]
    k0 = 1.0 if p.get("steady") or c.settled else at(c.t, 0.0, 0.3)
    hy = inner.y + 30
    for x, name in zip(xs, cols, strict=False):
        f.text(x, hy, str(name).upper(), size=22, fill=pal.text_faint, weight=600, alpha=k0)
    f.line(inner.x, hy + 22, inner.right, hy + 22, stroke=pal.line, width=2, opacity=k0)
    rowh = min(128.0, (inner.bottom - hy - 40) / max(1, len(rows)))
    for i, row in enumerate(rows):
        if i > upto:
            break
        if p.get("by_beats"):
            # Every row up to ``upto`` arrives on its own beat within one segment.
            k = c.beat(i, dur=0.9, spacing=1.2)
            if k <= 0:
                continue
        else:
            k = 1.0 if i < upto else c.beat(0, dur=0.9, spacing=1.0)
        y = hy + 40 + rowh * i
        rb = Box(inner.x + 4, y, inner.w - 8, rowh - 14)
        cur = i == upto
        if p.get("by_beats"):
            # The newest row that has arrived carries the glow.
            arrived = [j for j in range(upto + 1) if c.beat(j, dur=0.9, spacing=1.2) > 0]
            cur = i == (arrived[-1] if arrived else 0)
        tone = role(pal, row.get("tone"), "known")
        with f.group(opacity=k * (1.0 if cur else 0.62), dy=(1 - k) * 30):
            f.rect(rb, fill=pal.surface if cur else hexa(pal.surface, 0.55), r=16)
            if cur:
                g = pulse(c.seconds, 2.8)
                f.rect(rb, stroke=hexa(tone, 0.45 + 0.4 * g), width=3, r=16)
                f.rect(Box(rb.x, rb.y, 8, rb.h), fill=tone, r=4)
            my = rb.cy + 14
            f.text(xs[0], my, str(row["term"]), size=46, fill=pal.text, family=DISPLAY)
            f.text(xs[1], my - 2, str(row.get("basis", "")), size=f.fit(str(row.get("basis", "")), xs[2] - xs[1] - 30, 34, 24), fill=pal.text_soft)
            f.text(xs[2], my - 2, str(row.get("check", "")), size=f.fit(str(row.get("check", "")), inner.right - xs[2] - 20, 34, 24), fill=tone)


# ------------------------------------------------------------------ bars


@scene(
    "bars",
    required=("items",),
    optional=("max", "unit", "decimals", "steady"),
    demo={
        "heading": "Correct answers",
        "items": [
            {"label": "Given as percentages", "value": 16, "tone": "warn"},
            {"label": "Given as counts (standard)", "value": 46},
            {"label": "Given as counts (short)", "value": 50},
        ],
        "max": 100,
        "unit": "%",
    },
)
def bars(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Horizontal bars, one per beat, each growing to its value with a counting label."""
    pal = f.pal
    inner = _head(f, box, p, c)
    items = list(p["items"])
    vmax = float(p.get("max", max(float(it["value"]) for it in items)))
    unit = str(p.get("unit", ""))
    dec = int(p.get("decimals", 0))
    n = len(items)
    rowh = min(170.0, (inner.h - 20) / max(1, n))
    y0 = inner.y + (inner.h - rowh * n) / 2
    x0, x1 = inner.x, inner.right - 220
    for i, it in enumerate(items):
        k = c.beat(i, dur=1.1, spacing=1.2)
        if k <= 0:
            continue
        y = y0 + rowh * i
        tone = role(pal, it.get("tone"), "known")
        v = float(it["value"])
        w = (x1 - x0) * clamp(v / vmax) * ease(k)
        with f.group(opacity=clamp(k * 2)):
            f.text(x0, y + 40, str(it["label"]), size=34, fill=pal.text)
            f.rect(Box(x0, y + 60, x1 - x0, 36), fill=pal.surface_2, r=18)
            if w > 1:
                f.rect(Box(x0, y + 60, max(36.0, w), 36), fill=tone, r=18)
                g = pulse(c.seconds + i, 2.4)
                f.circle(x0 + max(36.0, w) - 18, y + 78, 10 + 3 * g, fill=hexa("#ffffff", 0.35))
            shown = it.get("text") if k >= 0.999 and it.get("text") else f"{v * ease(k):.{dec}f}{unit}"
            f.text(inner.right, y + 92, str(shown), size=52, fill=tone, family=MONO, anchor="end")


# ------------------------------------------------------------------ calibration


@scene(
    "calibration",
    required=(),
    optional=("points", "x_label", "y_label", "steady"),
    demo={
        "heading": "Said against happened",
        "points": [
            {"x": 70, "y": 70, "label": "calibrated", "tone": "known"},
            {"x": 100, "y": 70, "label": "early 100%", "tone": "warn"},
        ],
    },
)
def calibration(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Stated probability against how often it came true; the diagonal is honesty, points below it overconfidence."""
    pal = f.pal
    inner = _head(f, box, p, c)
    side = min(inner.h - 160, inner.w * 0.5)
    plot = Box(inner.x + 190, inner.y + 60, side, side)

    def P(x: float, y: float) -> tuple[float, float]:
        return plot.x + plot.w * x / 100, plot.bottom - plot.h * y / 100

    k0 = 1.0 if p.get("steady") or c.settled else at(c.t, 0.0, 0.3)
    f.line(plot.x, plot.bottom, plot.right, plot.bottom, stroke=pal.line, width=2, opacity=k0)
    f.line(plot.x, plot.bottom, plot.x, plot.y, stroke=pal.line, width=2, opacity=k0)
    for v in (0, 50, 100):
        x, _ = P(v, 0)
        f.text(x, plot.bottom + 44, f"{v}%", size=26, fill=pal.text_faint, family=MONO, anchor="middle", alpha=k0)
        _, y = P(0, v)
        f.text(plot.x - 18, y + 9, f"{v}%", size=26, fill=pal.text_faint, family=MONO, anchor="end", alpha=k0)
    f.text(plot.cx, plot.bottom + 90, str(p.get("x_label", "the forecast said")), size=30, fill=pal.text_soft, anchor="middle", alpha=k0)
    f.text(plot.x - 18, plot.y - 22, str(p.get("y_label", "how often it happened")), size=30, fill=pal.text_soft, alpha=k0)
    kd = 1.0 if p.get("steady") or c.settled else at(c.t, 0.1, 0.5, "ease-in-out-cubic")
    a, b = P(0, 0), P(100 * kd, 100 * kd)
    f.line(a[0], a[1], b[0], b[1], stroke=hexa(pal.known, 0.6), width=3, dash=[12, 10])
    f.text(P(100, 100)[0] + 16, P(100, 100)[1] + 10, "honest", size=28, fill=pal.known, alpha=kd)
    tx = plot.right + 120
    ty = plot.y + 80
    for i, pt in enumerate(p.get("points") or []):
        k = 1.0 if pt.get("shown") else c.beat(i, dur=0.9, spacing=1.2)
        if k <= 0:
            continue
        tone = role(pal, pt.get("tone"), "known")
        x, y = float(pt["x"]), float(pt["y"])
        px, py = P(x, lerp(x, y, ease(k)))
        dx_, dy_ = P(x, x)
        if abs(x - y) > 0.5:
            f.line(dx_, dy_, px, py, stroke=tone, width=3, opacity=k, dash=[6, 6])
        g = pulse(c.seconds + i, 2.2)
        f.circle(px, py, 18 + 5 * g, fill=tone, opacity=0.2 * k)
        f.circle(px, py, 12, fill=tone, opacity=k)
        label = pt.get("label")
        if label:
            with f.group(opacity=k):
                f.circle(tx, ty - 11, 9, fill=tone)
                lines = f.wrap(str(label), 34, inner.right - tx - 30)[:2]
                f.text_lines(tx + 26, ty, lines, size=34, fill=pal.text, leading=1.25)
            ty += 44 * len(lines) + 40


# ------------------------------------------------------------------ ellsberg_urn


@scene(
    "ellsberg_urn",
    required=(),
    optional=("red", "other", "notes"),
    demo={
        "heading": "Ellsberg's urn",
        "red": 30,
        "other": 60,
        "notes": ["30 red: known", "60 black or yellow: mix unknown"],
    },
)
def ellsberg_urn(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """One jar: the red balls drop in first, then the black-or-yellow balls, whose colours never settle."""
    pal = f.pal
    inner = _head(f, box, p, c)
    n_red, n_other = int(p.get("red", 30)), int(p.get("other", 60))
    n = n_red + n_other
    left, right = inner.split_x(0.46, gap=60)
    jar_h = min(left.h - 20, 560)
    jar_w = min(left.w * 0.8, jar_h * 0.9)
    jar = Box(left.cx - jar_w / 2, left.y + (left.h - jar_h) / 2, jar_w, jar_h)
    k0 = at(c.t, 0.0, 0.3) if not c.settled else 1.0
    with f.group(opacity=k0):
        f.path(_urn_path(jar), fill=hexa(pal.surface, 0.85), stroke=pal.line, width=3)
    belly = Box(jar.x + 16, jar.y + jar.h * 0.3, jar.w - 32, jar.h * 0.7 - 14)
    r = 26.0
    while r > 6:
        per_row = max(1, int((belly.w - 2 * r) // (2.05 * r)) + 1)
        rows = math.ceil(n / max(1.0, per_row - 0.5))
        if rows * 1.78 * r + r <= belly.h * 0.9:
            break
        r -= 0.5
    spots = _pack(belly, n, r, 5)
    order = rng(8).permutation(n)
    red = pal.warn
    black = "#15181f" if pal.name == "ink" else "#1b2130"
    yellow = pal.unknown
    ring = pal.text_soft if pal.name == "ink" else None
    k_red = c.beat(0, dur=1.3, spacing=1.0)
    k_oth = c.beat(1, dur=1.6, spacing=1.0)
    ri = rj = 0
    for idx, (x, y) in enumerate(spots):
        is_red = order[idx] < n_red
        if is_red:
            appear = clamp((k_red * (n_red + 8) - ri) / 8) if not c.settled else 1.0
            ri += 1
            color = red
        else:
            appear = clamp((k_oth * (n_other + 8) - rj) / 8) if not c.settled else 1.0
            rj += 1
            w = clamp(0.5 + 1.8 * math.sin(c.seconds * 0.5 + idx * 2.39))
            color = mix_hex(black, yellow, w)
        if appear <= 0:
            continue
        drop = (1 - ease(appear, "ease-out-back")) * 60
        ball(f, x, y - drop, r, color, ring=None if is_red else ring, opacity=appear)
    notes = p.get("notes") or [f"{n_red} red: known", f"{n_other} black or yellow: mix unknown"]
    tones = [red, yellow]
    ty = right.y + right.h * 0.36
    for i, note in enumerate(notes[:2]):
        k = k_red if i == 0 else k_oth
        with f.group(opacity=k, dx=(1 - k) * 24):
            f.circle(right.x + 16, ty - 12, 14, fill=tones[i])
            lines = f.wrap(str(note), 40, right.w - 60)[:2]
            f.text_lines(right.x + 50, ty, lines, size=40, fill=pal.text, leading=1.25)
        ty += 150


# ------------------------------------------------------------------ divergence


@scene(
    "divergence",
    required=(),
    optional=("paths", "seed", "growth", "spread", "marks", "control", "x_label", "start_label", "steady"),
    demo={
        "heading": "Tight at first, spread later",
        "paths": 30,
        "seed": 3,
        "marks": [{"at": 0.2, "label": "30 hours"}, {"at": 0.95, "label": "6 days"}],
        "control": True,
        "start_label": "start",
    },
)
def divergence(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Runs that share a path at first and then pull apart; the gap grows with time, drawn left to right."""
    pal = f.pal
    inner = _head(f, box, p, c)
    n = int(p.get("paths", 30))
    steps = 120
    g = rng(int(p.get("seed", 3)))
    u = np.linspace(0, 1, steps)
    base = 0.28 * np.sin(u * 5.2 + 0.4) + 0.12 * np.sin(u * 11.0 + 1.3)
    growth = float(p.get("growth", 4.0))
    env = (np.exp(growth * u) - 1) / (np.exp(growth) - 1)
    kernel = np.hanning(21)
    kernel /= kernel.sum()
    spread = float(p.get("spread", 0.55))
    members = []
    for i in range(n):
        w = np.convolve(g.normal(0, 1, steps + 40), kernel, mode="same")[20:-20]
        w = w / (np.abs(w).max() or 1.0)
        members.append(base + spread * env * (0.35 * w + g.normal(0, 0.7)))
    plot = Box(inner.x + 40, inner.y + 20, inner.w - 80, inner.h - 110)
    xs = plot.x + u * plot.w
    mid, amp = plot.cy, plot.h * 0.5
    k0 = 1.0 if p.get("steady") or c.settled else at(c.t, 0.0, 0.2)
    f.line(plot.x, plot.bottom + 20, plot.right, plot.bottom + 20, stroke=pal.line, width=2, opacity=k0)
    reach = 1.0 if c.settled else at(c.t, 0.1, 1.0, "ease-in-out-cubic")
    upto = max(2, int(reach * steps))
    for mk in p.get("marks") or []:
        x = plot.x + float(mk["at"]) * plot.w
        km = clamp((reach - float(mk["at"])) / 0.08 + 0.001)
        if km <= 0:
            continue
        f.line(x, plot.y, x, plot.bottom + 20, stroke=hexa(pal.unknown, 0.55), width=2, dash=[8, 8], opacity=km)
        f.text(x, plot.bottom + 64, str(mk["label"]), size=28, fill=pal.unknown, anchor="middle", alpha=km)
    wide = n <= 3
    for i, m in enumerate(members):
        ys = mid - np.clip(m, -1, 1) * amp
        pts = list(zip(xs[:upto].tolist(), ys[:upto].tolist(), strict=True))
        is_ctrl = bool(p.get("control")) and i == 0
        tone = pal.warn if is_ctrl else (pal.known if not wide or i == 0 else pal.cool)
        f.polyline(pts, stroke=tone, width=4.5 if (wide or is_ctrl) else 2.0, opacity=0.95 if (wide or is_ctrl) else 0.4)
    if reach >= 0.999:
        for i in range(0, n, max(1, n // 8)):
            s = (c.seconds * 0.1 + i * 0.137) % 1.0
            j = min(steps - 1, int(s * (steps - 1)))
            y = mid - float(np.clip(members[i][j], -1, 1)) * amp
            f.circle(float(xs[j]), y, 6, fill=pal.text, opacity=0.8 * math.sin(math.pi * s))
    gl = pulse(c.seconds, 2.0)
    y0 = mid - float(members[0][0]) * amp
    f.circle(plot.x, y0, 16 + 5 * gl, fill=pal.text, opacity=0.15 * k0)
    f.circle(plot.x, y0, 9, fill=pal.text, opacity=k0)
    sl = p.get("start_label")
    if sl:
        f.text(plot.x, plot.bottom + 64, str(sl), size=28, fill=pal.text_soft, alpha=k0)
    xl = p.get("x_label")
    if xl:
        f.text(plot.right, plot.bottom + 64, str(xl), size=28, fill=pal.text_faint, anchor="end", alpha=k0)


# ------------------------------------------------------------------ takeaway_line


@scene(
    "takeaway_line",
    required=("text",),
    optional=("stop", "of", "label"),
    demo={"text": "A probability counts over a group. Name the group, or the number floats.", "stop": 0, "of": 5,
          "label": "The group"},
)
def takeaway_line(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """A stop's answer as one line of display type, with the stop's place among the others above it."""
    pal = f.pal
    text = str(p["text"])
    n = int(p.get("of", 0))
    cur = int(p.get("stop", -1))
    live = not c.settled
    inner = box.inset(120, 20)
    size = 72.0
    while size > 44:
        lines = f.wrap(text, size, inner.w, DISPLAY)
        if len(lines) <= 3:
            break
        size -= 2
    # Avoid a one-word last line: narrow the measure until the last line holds two words or more.
    width = inner.w
    lines = f.wrap(text, size, width, DISPLAY)
    while len(lines) > 1 and len(lines[-1].split()) < 2 and width > inner.w * 0.6:
        width -= 40
        trial = f.wrap(text, size, width, DISPLAY)
        if len(trial) > 3:
            break
        lines = trial
    lines = lines[:3]
    lead = size * 1.24
    block = lead * len(lines)
    top = inner.cy - block / 2 + 10
    # Where this stop sits: a short row of dots, the finished ones teal, this one amber and pulsing.
    k0 = at(c.t, 0.0, 0.25) if live else 1.0
    head_y = top - 120
    if n > 0:
        gap = 44
        x0 = inner.cx - gap * (n - 1) / 2
        for i in range(n):
            x = x0 + gap * i
            if i < cur:
                f.circle(x, head_y, 9, fill=pal.known, opacity=k0)
            elif i == cur:
                g = pulse(c.seconds, 2.4)
                f.circle(x, head_y, 17 + 5 * g, fill=pal.unknown, opacity=(0.12 + 0.1 * g) * k0)
                f.circle(x, head_y, 11, fill=pal.unknown, opacity=k0)
            else:
                f.circle(x, head_y, 8, stroke=pal.line, width=2, opacity=k0)
    label = p.get("label")
    kick = "TAKEAWAY" + (f"  ·  {str(label).upper()}" if label else "")
    tracked(f, inner.cx, head_y + 58, kick, size=22, fill=pal.unknown, anchor="middle", alpha=k0)
    # The words arrive in reading order.
    words_total = sum(len(ln.split()) for ln in lines)
    speed = at(c.t, 0.04, 0.42, "linear") if live else 1.0
    wi = 0
    for li, line in enumerate(lines):
        w = f.measure(line, size, DISPLAY)
        x = inner.cx - w / 2
        y = top + size * 0.9 + li * lead
        for word in line.split():
            kw = clamp((speed * (words_total + 3) - wi) / 3.0) if live else 1.0
            f.text(x, y + (1 - kw) * 10, word, size=size, fill=pal.text, family=DISPLAY, alpha=kw)
            x += f.measure(word + " ", size, DISPLAY)
            wi += 1
    # A teal rule under the line draws out, with a soft glint running along it.
    kr = at(c.t, 0.4, 0.8, "ease-in-out-cubic") if live else 1.0
    ry = top + block + 36
    half = 220 * kr
    f.line(inner.cx - half, ry, inner.cx + half, ry, stroke=pal.known, width=3, opacity=kr)
    if kr > 0.5:
        g = (c.seconds / 4.0) % 1.0
        gx = inner.cx - half + 2 * half * g
        f.circle(gx, ry, 5, fill=pal.text, opacity=0.5 * math.sin(math.pi * g) * kr)
