"""Scenes added for video 1, "Two kinds of not knowing".

``object_cards``: generated objects on cards (a die, an envelope, a street of
insured buildings), each with the name of the kind of uncertainty it stands for.
``sort_bins``: examples dropping one by one into two labelled columns
(Keynes's 1937 list). ``stacked_bars``: rows of parts that should add to one,
with any shortfall outlined (Ellsberg's two urns). ``level_scale``: the
scale from complete certainty to total ignorance, a marker walking along it.

Imported by one line at the end of ``pipeline/scenes.py``.
"""

from __future__ import annotations

import math
from typing import Any

from .brand import DISPLAY, MONO, TEXT, Box
from .canvas import Frame, at, clamp, ease, hexa, lerp, mix_hex, pulse
from .scenes import Clock, Ctx, header_block, role, scene, tracked

__all__ = ["level_scale", "object_cards", "range_bar", "sort_bins", "stacked_bars"]


def _placeholder(f: Frame, b: Box, tone: str, opacity: float) -> None:
    f.circle(b.cx, b.cy, min(b.w, b.h) * 0.34, fill=hexa(tone, 0.25), opacity=opacity)
    f.circle(b.cx, b.cy, min(b.w, b.h) * 0.16, fill=tone, opacity=opacity)


def _picture(f: Frame, ctx: Ctx, ref: str | None, b: Box, tone: str, opacity: float) -> None:
    img = ctx.image(ref)
    if img is not None:
        f.image(img, b, opacity=opacity)
    else:
        _placeholder(f, b, tone, opacity)


def _k(c: Clock, beat: int | None, dur: float = 0.8, spacing: float = 1.2) -> float:
    if beat is None or beat < 0:
        return 1.0
    return c.beat(beat, dur=dur, spacing=spacing)


# ------------------------------------------------------------------ object_cards


@scene(
    "object_cards",
    required=("items",),
    optional=("slots", "start"),
    demo={
        "heading": "Two kinds of not knowing",
        "slots": 2,
        "items": [
            {
                "image": "image:icon",
                "term": "Aleatory",
                "caption": "Chance: more study will not tell the next roll",
                "tone": "known",
                "ticker": ["3", "6", "1", "4", "2", "5"],
                "ticker_label": "next roll",
            },
            {
                "image": "image:icon",
                "term": "Epistemic",
                "caption": "A fixed fact we do not know yet",
                "tone": "unknown",
                "stamp": "?",
            },
        ],
    },
)
def object_cards(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Objects on cards; each arrives on a beat, its term lands on a later one."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    items = list(p["items"])
    slots = int(p.get("slots", len(items)))
    start = int(p.get("start", 0))
    gap = 64
    cw = (inner.w - gap * (slots - 1)) / slots
    cw = min(cw, 760)
    total_w = cw * slots + gap * (slots - 1)
    x0 = inner.cx - total_w / 2
    card_h = min(inner.h - 10, 600)
    y0 = inner.y + (inner.h - card_h) / 2
    for i, it in enumerate(items[:slots]):
        tone = role(pal, it.get("tone"), "known" if i == 0 else "unknown")
        before = i < start
        arrive = 1.0 if before or c.settled else _k(c, it.get("at", i - start))
        term_k = 1.0 if before or c.settled else _k(c, it.get("term_at", it.get("at", i - start)), dur=0.7)
        if arrive <= 0.002:
            continue
        card = Box(x0 + i * (cw + gap), y0, cw, card_h)
        dy = (1 - arrive) * 30
        with f.group(opacity=arrive, dy=dy):
            f.rect(card, fill=pal.surface, r=24)
            f.rect(Box(card.x, card.y, card.w, 6), fill=tone, r=3)
        pic = Box(card.x + 40, card.y + 40, card.w - 80, card.h * 0.52)
        bob = 5 * math.sin(c.seconds * 1.1 + i * 1.7)
        count = int(it.get("count", 1))
        if count <= 1:
            side = min(pic.w, pic.h) * (0.86 + 0.14 * ease(arrive, "ease-out-back"))
            ib = Box(pic.cx - side / 2, pic.cy - side / 2 + bob + dy, side, side)
            _picture(f, ctx, it.get("image"), ib, tone, arrive)
        else:
            cols = int(it.get("columns", math.ceil(math.sqrt(count * pic.w / pic.h))))
            rows = math.ceil(count / cols)
            cell = min(pic.w / cols, pic.h / rows)
            gx = pic.cx - cell * cols / 2
            gy = pic.cy - cell * rows / 2 + dy
            marked = set(int(m) for m in it.get("marked", ()))
            # A different building "burns" every so often: the count stays steady.
            flick = int(c.seconds / 1.3)
            lit = {(m + flick * 7) % count for m in marked}
            for j in range(count):
                r_, c_ = divmod(j, cols)
                kj = clamp((arrive * (count + 6) - j) / 6) if not c.settled else 1.0
                if kj <= 0.002:
                    continue
                cb = Box(gx + c_ * cell + cell * 0.1, gy + r_ * cell + cell * 0.1, cell * 0.8, cell * 0.8)
                if j in lit:
                    g = pulse(c.seconds, 1.3)
                    f.circle(cb.cx, cb.cy, cell * 0.46, fill=pal.warn, opacity=(0.25 + 0.3 * g) * kj)
                _picture(f, ctx, it.get("image"), cb, tone, kj)
        with f.group(opacity=arrive * term_k, dy=dy + (1 - term_k) * 14):
            term = str(it.get("term", ""))
            if term:
                size = f.fit(term, card.w - 80, 64, 40, DISPLAY)
                f.text(card.cx, card.y + card.h * 0.52 + 120, term, size=size, fill=tone, family=DISPLAY, anchor="middle")
            cap = it.get("caption")
            if cap:
                lines = f.wrap(str(cap), 32, card.w - 90)[:2]
                f.text_lines(
                    card.cx, card.y + card.h * 0.52 + 180, lines, size=32, fill=pal.text_soft, anchor="middle", leading=1.3
                )
        ticker = it.get("ticker")
        if ticker:
            idx = int(c.seconds / 0.55) % len(ticker)
            tx, ty = card.right - 40, card.y + 70 + dy
            with f.group(opacity=arrive):
                lbl = str(it.get("ticker_label", "")).upper()
                if lbl:
                    tracked(f, tx, ty - 6, lbl, size=18, fill=pal.text_faint, anchor="end")
                f.text(tx, ty + 62, str(ticker[idx]), size=64, fill=tone, family=MONO, anchor="end")
        stamp = it.get("stamp")
        if stamp:
            g = 0.6 + 0.4 * pulse(c.seconds, 2.6)
            f.text(
                card.right - 50, card.y + 130 + dy, str(stamp), size=80, fill=tone, family=DISPLAY, anchor="end",
                alpha=arrive * g,
            )


# ------------------------------------------------------------------ sort_bins


@scene(
    "sort_bins",
    required=("left", "right", "items"),
    optional=("note",),
    demo={
        "heading": "Keynes, 1937",
        "left": "Not uncertain",
        "right": "Uncertain",
        "items": [
            {"text": "Roulette", "side": "left", "image": "image:icon"},
            {"text": "Length of a life", "side": "left", "note": "only slightly"},
            {"text": "The weather", "side": "left", "note": "only moderately"},
            {"text": "A European war", "side": "right"},
            {"text": "Copper, 20 years out", "side": "right", "image": "image:icon"},
        ],
    },
)
def sort_bins(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Two labelled columns; examples arrive one per beat and slide into their column."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    cols = inner.split_x(0.5, gap=80)
    tones = (pal.known, pal.unknown)
    k0 = at(c.t, 0.0, 0.25) if not c.settled else 1.0
    for ci, (col, title) in enumerate(zip(cols, (p["left"], p["right"]), strict=True)):
        tone = tones[ci]
        with f.group(opacity=k0):
            g = 0.5 + 0.5 * pulse(c.seconds + ci * 1.1, 3.4)
            f.circle(col.x + 14, col.y + 26, 12, fill=tone, opacity=0.3 + 0.4 * g)
            f.circle(col.x + 14, col.y + 26, 6, fill=tone)
            f.text(col.x + 42, col.y + 42, str(title), size=48, fill=pal.text, family=DISPLAY)
            f.line(col.x, col.y + 74, col.right, col.y + 74, stroke=tone, width=3)
    items = list(p["items"])
    per_side = {"left": 0, "right": 0}
    chip_h = 104
    for i, it in enumerate(items):
        side = "right" if str(it.get("side", "left")) == "right" else "left"
        ci = 0 if side == "left" else 1
        slot = per_side[side]
        per_side[side] += 1
        k = c.beat(i, dur=0.9, spacing=1.0) if not c.settled else 1.0
        if k <= 0.002:
            continue
        col = cols[ci]
        tx, ty = col.x, col.y + 104 + slot * (chip_h + 22)
        # Slide a short way in from the centre gap into its own slot; never across another chip.
        e = ease(k, "ease-out-cubic")
        x, y = tx + (1 - e) * (56 if ci == 0 else -56), ty
        chip = Box(x, y, col.w, chip_h)
        tone = tones[ci]
        with f.group(opacity=clamp(k * 1.6)):
            f.rect(chip, fill=pal.surface, r=18)
            f.rect(Box(chip.x, chip.y, 6, chip.h), fill=tone, r=3)
        has_img = bool(it.get("image"))
        tx0 = chip.x + 40
        if has_img:
            bob = 3 * math.sin(c.seconds * 1.3 + i)
            ib = Box(chip.x + 26, chip.y + 12 + bob, chip_h - 24, chip_h - 24)
            _picture(f, ctx, it.get("image"), ib, tone, clamp(k * 1.6))
            tx0 = ib.right + 26
        with f.group(opacity=clamp(k * 1.6)):
            note = it.get("note")
            size = f.fit(str(it["text"]), chip.right - tx0 - (230 if note else 30), 40, 26)
            f.text(tx0, chip.cy + size * 0.36, str(it["text"]), size=size, fill=pal.text)
            if note:
                f.text(chip.right - 28, chip.cy + 10, str(note), size=28, fill=tone, anchor="end")
    note = p.get("note")
    if note:
        kn = at(c.t, 0.8, 1.0) if not c.settled else 1.0
        f.text(inner.cx, inner.bottom - 8, str(note), size=28, fill=pal.text_faint, anchor="middle", alpha=kn)


# ------------------------------------------------------------------ stacked_bars


@scene(
    "stacked_bars",
    required=("rows",),
    optional=(),
    demo={
        "heading": "What the bets imply",
        "rows": [
            {
                "label": "Urn II",
                "parts": [{"value": 50, "label": "red: ½", "tone": "warn"}, {"value": 50, "label": "black: ½", "tone": "dark"}],
            },
            {
                "label": "Urn I, as the bets treat it",
                "parts": [
                    {"value": 40, "label": "red: less than ½", "tone": "warn"},
                    {"value": 40, "label": "black: less than ½", "tone": "dark"},
                ],
                "gap_label": "adds to less than 1",
            },
        ],
    },
)
def stacked_bars(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Rows of parts on a 0-to-1 track; parts grow in order and a shortfall is outlined in coral."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    rows = list(p["rows"])
    x0, x1 = inner.x + 20, inner.right - 20
    row_h = min(240.0, inner.h / max(1, len(rows)))
    top = inner.y + (inner.h - row_h * len(rows)) / 2
    h = 70
    dark = "#262c38" if pal.name == "ink" else "#2b3242"
    beat = 0
    for ri, row in enumerate(rows):
        y = top + ri * row_h + 70
        row_at = int(row.get("at", beat))
        kr = c.beat(row_at, dur=0.6, spacing=1.2) if not c.settled else 1.0
        with f.group(opacity=kr):
            f.text(x0, y - 22, str(row.get("label", "")), size=38, fill=pal.text, family=DISPLAY)
            f.rect(Box(x0, y, x1 - x0, h), fill=hexa(pal.surface_2, 0.7), r=12)
            f.text(x0, y + h + 40, "0", size=24, fill=pal.text_faint, family=MONO)
            f.text(x1, y + h + 40, "1", size=24, fill=pal.text_faint, family=MONO, anchor="end")
        x = x0
        beat = row_at
        for pi, part in enumerate(row.get("parts", [])):
            part_at = int(part.get("at", row_at))
            beat = max(beat, part_at + 1)
            kp = c.beat(part_at, dur=1.0, spacing=1.2) if not c.settled else 1.0
            kp = clamp(kp * 1.15 - 0.15 * pi) if "at" not in part else kp
            v = float(part["value"]) / 100.0
            w = (x1 - x0) * v * ease(kp, "ease-in-out-cubic")
            tname = part.get("tone", "known")
            tone = dark if tname == "dark" else role(pal, tname)
            if w > 1:
                f.rect(Box(x, y, w, h), fill=tone, stroke=pal.text_soft if tname == "dark" else None, width=2, r=12)
                lbl = str(part.get("label", ""))
                if lbl and kp > 0.3:
                    f.text(
                        x + w / 2, y + h / 2 + 11, lbl, size=30, fill=pal.text, anchor="middle",
                        alpha=clamp((kp - 0.3) / 0.5),
                    )
            x += (x1 - x0) * v
        gap_label = row.get("gap_label")
        if gap_label and x < x1 - 2:
            gap_at = int(row.get("gap_at", beat))
            beat = gap_at + 1
            kg = c.beat(gap_at, dur=0.8, spacing=1.2) if not c.settled else 1.0
            if kg > 0.002:
                g = pulse(c.seconds, 1.8)
                f.rect(
                    Box(x + 4, y - 4, x1 - x - 4, h + 8), stroke=pal.warn, width=3 + 1.5 * g, r=12, opacity=kg,
                    dash=[12, 8],
                )
                f.text(x + (x1 - x) / 2, y + h / 2 + 12, "?", size=40, fill=pal.warn, family=DISPLAY, anchor="middle", alpha=kg)
                half = f.measure(str(gap_label), 32, TEXT, 500) / 2
                gx = clamp(x + (x1 - x) / 2, x0 + half, x1 - half)
                f.text(gx, y + h + 88, str(gap_label), size=32, fill=pal.warn, anchor="middle", alpha=kg, weight=500)


# ------------------------------------------------------------------ range_bar


@scene(
    "range_bar",
    required=("rows",),
    optional=("low_label", "high_label"),
    demo={
        "heading": "Ambiguity",
        "rows": [
            {"label": "Urn II: chance of red", "value": 50, "value_label": "exactly ½", "tone": "known"},
            {"label": "Urn I: chance of red", "lo": 0, "hi": 100, "value_label": "anywhere from 0 to 1", "tone": "unknown"},
        ],
        "low_label": "0",
        "high_label": "1",
    },
)
def range_bar(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Tracks from 0 to 1: a row is a fixed point, or a range whose marker wanders across it."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    rows = list(p["rows"])
    x0, x1 = inner.x + 40, inner.right - 40
    row_h = min(250.0, inner.h / max(1, len(rows)))
    top = inner.y + (inner.h - row_h * len(rows)) / 2
    h = 26

    def X(v: float) -> float:
        return lerp(x0, x1, clamp(v / 100.0))

    for ri, row in enumerate(rows):
        k = c.beat(int(row.get("at", ri)), dur=0.9, spacing=1.4) if not c.settled else 1.0
        if k <= 0.002:
            continue
        tone = role(pal, row.get("tone"), "known" if ri == 0 else "unknown")
        cy = top + ri * row_h + 110
        with f.group(opacity=k):
            f.text(x0, cy - 60, str(row.get("label", "")), size=38, fill=pal.text_soft)
            f.rect(Box(x0, cy - h / 2, x1 - x0, h), fill=pal.surface_2, r=h / 2)
            for v, t in ((0, p.get("low_label", "0")), (100, p.get("high_label", "1"))):
                f.text(X(v), cy + h / 2 + 44, str(t), size=26, fill=pal.text_faint, family=MONO, anchor="middle")
            vl = row.get("value_label")
            if vl:
                f.text(x1, cy - 60, str(vl), size=34, fill=tone, anchor="end", weight=500)
        if "value" in row:
            mx = X(float(row["value"]))
        else:
            lo, hi = float(row.get("lo", 0)), float(row.get("hi", 100))
            e = ease(k, "ease-in-out-cubic")
            mid = (lo + hi) / 2
            a, b = X(lerp(mid, lo, e)), X(lerp(mid, hi, e))
            f.rect(Box(a, cy - h / 2, b - a, h), fill=hexa(tone, 0.35), r=h / 2, opacity=k)
            # The marker cannot settle: it wanders over the whole range.
            w = 0.5 + 0.45 * math.sin(c.seconds * 0.9) * math.cos(c.seconds * 0.37 + 1.0)
            mx = lerp(a, b, w)
        g = pulse(c.seconds + ri, 2.2)
        f.circle(mx, cy, 26 + 6 * g, fill=tone, opacity=0.2 * k)
        f.circle(mx, cy, 19, fill=pal.text, opacity=k)
        f.circle(mx, cy, 10, fill=tone, opacity=k)
        if "value" not in row:
            f.text(mx, cy - 34, "?", size=40, fill=tone, family=DISPLAY, anchor="middle", alpha=k * (0.6 + 0.4 * g))


# ------------------------------------------------------------------ level_scale


@scene(
    "level_scale",
    required=("levels",),
    optional=("marks", "left_label", "right_label", "intro"),
    demo={
        "heading": "From certainty to total ignorance",
        "levels": [
            {"label": "Complete certainty"},
            {"label": "Level 1"},
            {"label": "Level 2", "example": "which supermarket line"},
            {"label": "Level 3", "example": "umbrella in the car"},
            {"label": "Level 4", "example": "deep uncertainty"},
            {"label": "Total ignorance"},
        ],
        "marks": [0, 2, 3, 5],
    },
)
def level_scale(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """A track from teal to amber with a tick per level; a marker steps to ``marks[i]`` on beat ``i``."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    levels = list(p["levels"])
    n = len(levels)
    marks = [int(m) for m in p.get("marks", [0])] or [0]
    x0, x1 = inner.x + 110, inner.right - 110
    cy = inner.y + inner.h * 0.5

    def X(i: float) -> float:
        return lerp(x0, x1, i / max(1, n - 1))

    intro = bool(p.get("intro", True)) and not c.settled
    k0 = at(c.t, 0.0, 0.3, "ease-in-out-cubic") if intro else 1.0
    segs = 40
    reach = x0 + (x1 - x0) * k0
    for s in range(segs):
        a, b = lerp(x0, x1, s / segs), lerp(x0, x1, (s + 1) / segs)
        if a >= reach:
            break
        col = mix_hex(pal.known, pal.unknown, s / (segs - 1))
        f.line(a, cy, min(b + 2.0, reach), cy, stroke=col, width=10, cap="butt")
    for i, lv in enumerate(levels):
        ki = at(c.t, 0.08 + 0.3 * i / n, 0.28 + 0.3 * i / n) if intro else 1.0
        if ki <= 0.002:
            continue
        x = X(i)
        col = mix_hex(pal.known, pal.unknown, i / max(1, n - 1))
        up = i % 2 == 0
        f.line(x, cy - 26, x, cy + 26, stroke=col, width=4, opacity=ki)
        label = str(lv["label"])
        size = 34
        half = f.measure(label, size, TEXT, 600) / 2
        lx = clamp(x, inner.x + half, inner.right - half)
        ly = cy - 60 if up else cy + 88
        f.text(lx, ly, label, size=size, fill=pal.text, anchor="middle", weight=600, alpha=ki)
        ex = lv.get("example")
        if ex:
            lines = f.wrap(str(ex), 29, 330)[:2]
            ey = ly - 44 - 36 * (len(lines) - 1) if up else ly + 44
            ehalf = max(f.measure(line_, 29) for line_ in lines) / 2
            ex_x = clamp(x, inner.x + ehalf, inner.right - ehalf)
            f.text_lines(ex_x, ey, lines, size=29, fill=pal.text_soft, anchor="middle", alpha=ki, leading=1.25)
    # The marker: steps between marks on the beats.
    pos = float(marks[0])
    for i in range(1, len(marks)):
        k = c.beat(i, dur=1.1, name="ease-in-out-cubic", spacing=1.4) if not c.settled else 1.0
        pos = lerp(pos, float(marks[i]), k)
    km = c.beat(0, dur=0.6, spacing=1.4) if intro else 1.0
    mx = X(pos)
    col = mix_hex(pal.known, pal.unknown, pos / max(1, n - 1))
    g = pulse(c.seconds, 2.2)
    f.circle(mx, cy, 30 + 8 * g, fill=col, opacity=0.22 * km)
    f.circle(mx, cy, 20, fill=pal.text, opacity=km)
    f.circle(mx, cy, 11, fill=col, opacity=km)
    ll, rl = p.get("left_label"), p.get("right_label")
    kb = at(c.t, 0.5, 0.9) if not c.settled else 1.0
    if ll:
        f.text(x0, inner.bottom - 20, str(ll), size=28, fill=pal.known, alpha=kb)
    if rl:
        f.text(x1, inner.bottom - 20, str(rl), size=28, fill=pal.unknown, anchor="end", alpha=kb)
