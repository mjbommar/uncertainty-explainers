"""Scenes for video 3, "Saying it out loud": words, the numbers behind them, and who hears what.

Registered into :data:`pipeline.scenes.REGISTRY` on import (``scenes.py`` imports
this module on its last line). Every scene follows the house contract: draw
inside ``box``, colour by palette role, stage reveals on ``clock.beat(i)``, and
keep one ambient motion on ``clock.seconds`` so a settled frame still changes.
"""

from __future__ import annotations

import math
from typing import Any

import numpy as np

from .brand import DISPLAY, MONO, Box
from .canvas import Frame, at, clamp, ease, hexa, lerp, mix_hex, pulse
from .scenes import Clock, Ctx, header_block, rng, role, tracked
from .scenes import scene as _register

__all__: list[str] = []


# ------------------------------------------------------------------ helpers


class _Kept:
    """A clock whose first ``keep`` beats (and, when ``keep`` is given, the base reveal) are done,
    and whose beats from ``upto`` on have not happened yet.

    ``keep`` lets a segment continue the previous segment's picture and add to
    it, instead of rebuilding it when one parameter changes; ``upto`` holds back
    the parts that belong to the next segment.
    """

    def __init__(self, c: Clock, keep: int, upto: int | None, base: bool):
        self._c = c
        self.keep, self.upto = keep, upto
        self.t = 1.0 if base else c.t
        self.local, self.seconds, self.progress = c.local, c.seconds, c.progress
        self.duration, self.beats, self.settled = c.duration, c.beats, c.settled

    def beat(self, i: int, **kw: Any) -> float:
        if self.upto is not None and i >= self.upto:
            return 0.0
        return 1.0 if i < self.keep else self._c.beat(i, **kw)


def scene(name: str, *, required=(), optional=(), demo=None):
    """``pipeline.scenes.scene`` plus ``keep`` and ``upto`` (beats already shown, beats held back)."""

    def wrap(fn):
        def run(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
            keep, upto = int(p.get("keep", 0)), p.get("upto")
            if "keep" in p or upto is not None:
                c = _Kept(c, keep, None if upto is None else int(upto), base="keep" in p)
            fn(f, box, p, c, ctx)

        run.__doc__ = fn.__doc__
        run.__name__ = fn.__name__
        _register(name, required=required, optional=(*tuple(optional), "keep", "upto"), demo=demo)(run)
        return fn

    return wrap


def _paper(pal) -> tuple[str, str, str]:
    """Paper fill, ink and faint ink for a document card on either ground."""
    if pal.name == "ink":
        return "#ece4d4", "#1d212b", "#6f6a60"
    return "#fffdf7", pal.text, pal.text_faint


def _axis(f: Frame, x0: float, x1: float, y: float, k: float, *, ticks=(0, 25, 50, 75, 100), size=24) -> None:
    pal = f.pal
    f.line(x0, y, x1, y, stroke=pal.line, width=2, opacity=k)
    for v in range(0, 101, 10):
        big = v % 50 == 0
        f.line(
            lerp(x0, x1, v / 100),
            y,
            lerp(x0, x1, v / 100),
            y + (14 if big else 8),
            stroke=pal.text_faint,
            width=2,
            opacity=k,
        )
    for v in ticks:
        f.text(
            lerp(x0, x1, v / 100),
            y + 44,
            f"{v}%",
            size=size,
            fill=pal.text_faint,
            family=MONO,
            anchor="middle",
            alpha=k,
        )


def _image_badge(f: Frame, ctx: Ctx, ref: str | None, cx: float, cy: float, side: float, k: float, c: Clock) -> None:
    img = ctx.image(ref)
    if img is None or k <= 0.002:
        return
    bob = 4 * math.sin(c.seconds * 1.1)
    f.circle(cx, cy + bob, side * 0.62, fill=f.pal.surface, opacity=k)
    f.image(img, Box(cx - side / 2, cy - side / 2 + bob, side, side), opacity=k)


def _arrow(
    f: Frame,
    x0: float,
    y0: float,
    x1: float,
    y1: float,
    *,
    stroke: str,
    width: float = 3,
    head: float = 14,
    opacity: float = 1.0,
) -> None:
    f.line(x0, y0, x1, y1, stroke=stroke, width=width, opacity=opacity)
    ang = math.atan2(y1 - y0, x1 - x0)
    for s in (-1, 1):
        a = ang + math.pi + s * 0.45
        f.line(x1, y1, x1 + head * math.cos(a), y1 + head * math.sin(a), stroke=stroke, width=width, opacity=opacity)


# ------------------------------------------------------------------ memo


@scene(
    "memo",
    required=("text",),
    optional=("highlight", "note", "stamp", "image", "note_tone"),
    demo={
        "stamp": "JCSM-57-61  ·  3 FEBRUARY 1961",
        "text": (
            "Despite the shortcomings pointed out in the assessment, the Joint Chiefs of Staff consider "
            "that timely execution of this plan has a fair chance of ultimate success."
        ),
        "highlight": "a fair chance",
        "note": "The writer's odds: about 3 in 10",
    },
)
def memo(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """A typed memo on paper; one phrase is marked on beat 1, a margin note arrives on beat 2."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    paper, ink, faint = _paper(pal)
    note = p.get("note")
    card_w = inner.w * (0.60 if note else 0.78)
    card = Box(inner.x + (0 if note else (inner.w - card_w) / 2), inner.y + 10, card_w, inner.h - 30)
    probe_lines = f.wrap(str(p["text"]), 36, card_w - 112, MONO)
    fit_h = (154 if p.get("stamp") else 70) + len(probe_lines) * 36 * 1.55 + 90
    if fit_h < card.h:
        card = Box(card.x, inner.y + (inner.h - fit_h) / 2, card.w, fit_h)
    k0 = c.beat(0, dur=0.8, spacing=0.4)
    sway = 1.5 * math.sin(c.seconds * 0.6)
    with f.group(opacity=k0, dy=(1 - k0) * 30 + sway):
        f.rect(Box(card.x + 10, card.y + 14, card.w, card.h), fill=hexa("#000000", 0.28), r=10)
        f.rect(card, fill=paper, r=10)
        stamp = p.get("stamp")
        y = card.y + 70
        if stamp:
            tracked(f, card.x + 56, y, str(stamp).upper(), size=20, fill=faint, family=MONO, weight=400, tracking=0.08)
            f.line(card.x + 56, y + 22, card.right - 56, y + 22, stroke=hexa(faint, 0.6), width=1.5)
            y += 84
        size = 36.0
        text = str(p["text"])
        width = card.w - 112
        while size > 24:
            lines = f.wrap(text, size, width, MONO)
            if len(lines) * size * 1.55 < card.bottom - y - 40:
                break
            size -= 1
        lines = f.wrap(text, size, width, MONO)
        hl = str(p.get("highlight") or "").split()
        words = [w for ln in lines for w in ln.split()]

        # Find the highlight as a run of words (punctuation-insensitive).
        def norm(w: str) -> str:
            return "".join(ch for ch in w.lower() if ch.isalnum())

        start = -1
        if hl:
            target = [norm(w) for w in hl]
            for i in range(len(words) - len(target) + 1):
                if [norm(w) for w in words[i : i + len(target)]] == target:
                    start = i
                    break
        kh = c.beat(1, dur=0.7, spacing=1.2) if start >= 0 else 0.0
        wi = 0
        marks: list[Box] = []
        space = f.measure(" ", size, MONO)
        for li, ln in enumerate(lines):
            x = card.x + 56
            by = y + size + li * size * 1.55
            for w in ln.split():
                ww = f.measure(w, size, MONO)
                if start >= 0 and start <= wi < start + len(hl):
                    box_w = Box(x - 6, by - size * 0.92, ww + 12, size * 1.22)
                    if marks and abs(marks[-1].y - box_w.y) < 1:
                        m = marks[-1]
                        marks[-1] = Box(m.x, m.y, box_w.right - m.x, m.h)
                    else:
                        marks.append(box_w)
                wi += 1
                x += ww + space
        # Marker strokes grow left to right across the phrase, under the type.
        total = sum(m.w for m in marks) or 1.0
        run = kh * total
        for m in marks:
            wdt = clamp(run / m.w) * m.w
            run -= m.w
            if wdt > 0.5:
                f.rect(Box(m.x, m.y, wdt, m.h), fill=hexa(pal.unknown, 0.55 + 0.1 * pulse(c.seconds, 2.4)), r=4)
        for li, ln in enumerate(lines):
            x = card.x + 56
            by = y + size + li * size * 1.55
            for w in ln.split():
                f.text(x, by, w, size=size, fill=ink, family=MONO)
                x += f.measure(w, size, MONO) + space
    if note:
        kn = c.beat(2, dur=0.8, spacing=2.0)
        tone = role(pal, p.get("note_tone"), "unknown")
        m = marks[-1] if marks else Box(card.right, inner.cy, 0, 0)
        ay = m.bottom + size * 0.42
        nh = 190.0
        nb = Box(card.right + 70, clamp(ay - nh / 2, inner.y, inner.bottom - nh), inner.right - card.right - 70, nh)
        with f.group(opacity=kn, dy=(1 - kn) * 20):
            f.rect(nb, fill=pal.surface, r=18)
            f.rect(Box(nb.x, nb.y, 6, nb.h), fill=tone, r=3)
            if isinstance(note, list):
                nlines = [str(x) for x in note][:3]
                nsize = min(f.fit(x, nb.w - 70, 40, 26) for x in nlines)
            else:
                nsize = f.fit(str(note), (nb.w - 70) * 2.2, 40, 28)
                nlines = f.wrap(str(note), nsize, nb.w - 70)[:3]
            ty = nb.cy - (len(nlines) - 1) * nsize * 0.65 + nsize * 0.35
            f.text_lines(nb.x + 40, ty, nlines, size=nsize, fill=pal.text, leading=1.3)
            if marks:
                g = 0.6 + 0.4 * pulse(c.seconds, 2.2)
                ex = lerp(nb.x - 10, m.cx, ease(kn))
                f.line(nb.x - 10, ay, ex, ay, stroke=hexa(tone, g), width=3)
                if kn > 0.95:
                    _arrow(f, m.cx, ay, m.cx, m.bottom + 6, stroke=hexa(tone, g), width=3, head=12)
    _image_badge(f, ctx, p.get("image"), card.right - 70, card.y + 64, 84, k0, c)


# ------------------------------------------------------------------ phrase_readings


@scene(
    "phrase_readings",
    required=("phrase",),
    optional=("pins", "band", "ghosts", "zone", "note", "seed"),
    demo={
        "phrase": "serious possibility",
        "pins": [
            {"value": 20, "label": "lowest", "beat": 1, "tone": "known"},
            {"value": 80, "label": "highest", "beat": 1, "tone": "known"},
            {"value": 65, "label": "Kent", "beat": 0, "tone": "unknown", "up": True},
        ],
        "band": {"lo": 20, "hi": 80, "label": "the rest ranged in between", "beat": 2},
        "ghosts": 7,
    },
)
def phrase_readings(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """One phrase, many readers: pins on a 0-100 axis, a band, drifting unnamed readings."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    k0 = at(c.t, 0.0, 0.3) if not c.settled else 1.0
    phrase = f"“{p['phrase']}”"
    psize = f.fit(phrase, inner.w * 0.9, 76, 48, DISPLAY)
    f.text(
        inner.cx, inner.y + psize * 0.95, phrase, size=psize, fill=pal.text, family=DISPLAY, anchor="middle", alpha=k0
    )
    note = p.get("note")
    if note:
        kn = c.beat(3, dur=0.8, spacing=2.4)
        f.text(inner.cx, inner.y + psize * 0.95 + 58, str(note), size=32, fill=pal.unknown, anchor="middle", alpha=kn)
    x0, x1 = inner.x + 60, inner.right - 60
    ay = inner.bottom - 90

    def X(v: float) -> float:
        return lerp(x0, x1, clamp(v / 100.0))

    _axis(f, x0, x1, ay, k0)
    band = p.get("band")
    if band:
        kb = c.beat(int(band.get("beat", 2)), dur=1.0, spacing=1.6)
        lo, hi = float(band["lo"]), float(band["hi"])
        mid = (lo + hi) / 2
        a, b = X(lerp(mid, lo, kb)), X(lerp(mid, hi, kb))
        f.rect(Box(a, ay - 240, max(0.0, b - a), 240), fill=hexa(pal.known, 0.10), opacity=kb)
        f.line(a, ay - 240, b, ay - 240, stroke=hexa(pal.known, 0.5), width=2, dash=[6, 8], opacity=kb)
        bl = band.get("label")
        if bl:
            f.text((a + b) / 2, ay - 258, str(bl), size=28, fill=pal.known, anchor="middle", alpha=kb)
        n = int(p.get("ghosts", 0))
        if n:
            g = rng(int(p.get("seed", 5)))
            base = g.uniform(0.08, 0.92, n)
            ph = g.uniform(0, 2 * math.pi, n)
            hs = g.uniform(0.25, 0.8, n)
            for i in range(n):
                v = lo + (hi - lo) * clamp(base[i] + 0.05 * math.sin(c.seconds * 0.5 + ph[i]), 0.02, 0.98)
                y = ay - 30 - hs[i] * 170
                f.circle(X(v), y, 11, fill=pal.known_soft, stroke=hexa(pal.known, 0.6), width=2, opacity=kb * 0.9)
    zone = p.get("zone")
    if zone:
        kz = c.beat(int(zone.get("beat", 1)), dur=0.9, spacing=1.6)
        hi = float(zone["hi"])
        xa = X(hi)
        xb = lerp(xa, X(float(zone.get("lo", 2))), kz)
        zy = ay - 120
        f.rect(Box(min(xa, xb), zy - 26, abs(xa - xb), 52), fill=hexa(pal.cool, 0.16), r=26, opacity=kz)
        if kz > 0.05:
            _arrow(f, xa, zy, xb, zy, stroke=pal.cool, width=3, opacity=kz)
        zl = zone.get("label")
        if zl:
            f.text(
                (xa + X(float(zone.get("lo", 2)))) / 2,
                zy - 44,
                str(zl),
                size=28,
                fill=pal.cool,
                anchor="middle",
                alpha=kz,
            )
    for i, pin in enumerate(p.get("pins") or []):
        kp = c.beat(int(pin.get("beat", i)), dur=0.8, name="ease-out-back", spacing=1.2)
        if kp <= 0.001:
            continue
        v = float(pin["value"])
        tone = role(pal, pin.get("tone"), "unknown")
        tall = 340 if pin.get("up") else 220
        x = X(v)
        top = ay - tall * kp
        f.line(x, ay, x, top, stroke=tone, width=4)
        g = pulse(c.seconds + i, 2.6)
        f.circle(x, top, 20 + 5 * g, fill=tone, opacity=0.2 * clamp(kp))
        f.circle(x, top, 13, fill=tone, opacity=clamp(kp))
        label = str(pin.get("label", ""))
        val = pin.get("text") or f"{v:g}%"
        with f.group(opacity=clamp(kp)):
            f.text(x, top - 58, str(val), size=34, fill=pal.text, family=MONO, anchor="middle")
            if label:
                f.text(x, top - 26, label, size=26, fill=tone, anchor="middle", weight=600)


# ------------------------------------------------------------------ point_ladder


@scene(
    "point_ladder",
    required=("rungs",),
    optional=("highlight", "scale"),
    demo={
        "scale": "Kent, 1964",
        "rungs": [
            {"word": "Certainty", "p": 100, "pm": 0},
            {"word": "Almost certain", "p": 93, "pm": 6},
            {"word": "Probable", "p": 75, "pm": 12},
            {"word": "Chances about even", "p": 50, "pm": 10},
            {"word": "Probably not", "p": 30, "pm": 10},
            {"word": "Almost certainly not", "p": 7, "pm": 5},
            {"word": "Impossibility", "p": 0, "pm": 0},
        ],
        "highlight": ["Probable"],
    },
)
def point_ladder(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Kent's table: each word a point with a give-or-take band, filled from the top."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    rungs = list(p["rungs"])
    n = len(rungs)
    hl = p.get("highlight") or []
    hl = [hl] if isinstance(hl, str) else list(hl)
    label_w = 400
    x0, x1 = inner.x + label_w + 50, inner.right - 190
    axis_y = inner.bottom - 50
    top = inner.y + 10
    row = min(96.0, (axis_y - top - 20) / max(1, n))

    def X(v: float) -> float:
        return lerp(x0, x1, clamp(v / 100.0))

    k0 = at(c.t, 0.0, 0.25) if not c.settled else 1.0
    _axis(f, x0, x1, axis_y, k0, size=24)
    for v in range(0, 101, 25):
        f.line(X(v), top, X(v), axis_y, stroke=hexa(pal.line, 0.45), width=1, opacity=k0)
    scale = p.get("scale")
    if scale:
        f.text(
            inner.x + label_w, axis_y + 44, str(scale), size=24, fill=pal.unknown, anchor="end", weight=600, alpha=k0
        )
    for i, rung in enumerate(rungs):
        y = top + row * i + row / 2
        k = at(c.t, 0.1 + 0.6 * i / max(1, n), 0.4 + 0.6 * i / max(1, n)) if not c.settled else 1.0
        lit = rung.get("word") in hl
        kl = c.beat(1, dur=0.7, spacing=1.8) if lit else 0.0
        tone = mix_hex(pal.known, pal.unknown, kl)
        pv, pm = float(rung["p"]), float(rung.get("pm", 0))
        with f.group(opacity=k, dx=(1 - k) * -18):
            f.text(
                inner.x + label_w,
                y + 11,
                str(rung["word"]),
                size=32,
                fill=mix_hex(pal.text_soft, pal.text, kl),
                anchor="end",
                weight=600 if lit else 400,
            )
            if pm > 0:
                grow = ease(clamp((k - 0.3) / 0.7))
                a, b = X(pv - pm * grow), X(pv + pm * grow)
                f.rect(Box(a, y - 13, b - a, 26), fill=hexa(tone, 0.32 + 0.2 * kl), r=13)
                f.line(a, y - 16, a, y + 16, stroke=tone, width=2)
                f.line(b, y - 16, b, y + 16, stroke=tone, width=2)
            g = pulse(c.seconds + i * 0.7, 3.0) if lit else 0.0
            f.circle(X(pv), y, 11 + 4 * g, fill=tone)
            txt = f"{pv:g}%" + (f"  ± {pm:g}" if pm else "")
            f.text(
                inner.right,
                y + 10,
                txt,
                size=28,
                fill=mix_hex(pal.text_faint, pal.unknown, kl),
                family=MONO,
                anchor="end",
            )


# ------------------------------------------------------------------ unit_grid


@scene(
    "unit_grid",
    required=("n", "k"),
    optional=("columns", "label", "caption", "pick", "seed", "spread"),
    demo={
        "n": 379,
        "k": 16,
        "columns": 32,
        "label": "16 of 379",
        "caption": "estimates with any number for a probability",
    },
)
def unit_grid(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """``n`` small squares, ``k`` of them lit; with ``pick``, a draw lands on one square again and again."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    n, k = int(p["n"]), int(p["k"])
    cols = int(p.get("columns", 10 if n <= 100 else 32))
    rows = math.ceil(n / cols)
    label = p.get("label")
    side_w = 520 if label else 0
    area = Box(inner.x, inner.y + 10, inner.w - side_w, inner.h - 20)
    cell = min(area.w / cols, area.h / rows)
    gw, gh = cell * cols, cell * rows
    gx, gy = area.x + (area.w - gw) / 2, area.y + (area.h - gh) / 2
    g = rng(int(p.get("seed", 3)))
    lit = set(g.permutation(n)[:k].tolist()) if p.get("spread", True) else set(range(k))
    fill = at(c.t, 0.0, 0.55, "linear") if not c.settled else 1.0
    kl = c.beat(1, dur=0.9, spacing=1.6)
    order = rng(11).permutation(n)
    rank = np.empty(n, dtype=int)
    rank[order] = np.arange(n)
    pick = None
    if p.get("pick") and kl >= 0.99:
        step = int(c.seconds / 1.4)
        pick = int(rng(100 + step).integers(0, n))
    for i in range(n):
        r_, c_ = divmod(i, cols)
        a = clamp((fill * (n + 20) - rank[i]) / 20) if not c.settled else 1.0
        if a <= 0:
            continue
        x, y = gx + c_ * cell, gy + r_ * cell
        is_lit = i in lit
        color = mix_hex(pal.known_soft, pal.unknown, kl) if is_lit else pal.known_soft
        tw = 0.06 * pulse(c.seconds + (i % 7) * 0.4, 2.8) if is_lit else 0.0
        s = cell * (0.78 + (0.1 * kl + tw if is_lit else 0))
        f.rect(Box(x + (cell - s) / 2, y + (cell - s) / 2, s, s), fill=color, r=s * 0.22, opacity=a)
        if i == pick:
            f.rect(Box(x - 3, y - 3, cell + 6, cell + 6), stroke=pal.text, width=3, r=cell * 0.25)
    if label:
        lx = inner.right - side_w + 60
        kt = kl
        f.text(
            lx,
            inner.cy - 10,
            str(label),
            size=f.fit(str(label), side_w - 60, 96, 56, MONO),
            fill=pal.unknown,
            family=MONO,
            alpha=kt,
        )
        cap = p.get("caption")
        if cap:
            lines = f.wrap(str(cap), 32, side_w - 70)[:3]
            f.text_lines(lx, inner.cy + 50, lines, size=32, fill=pal.text_soft, alpha=kt, leading=1.3)
        if pick is not None:
            hit = pick in lit
            f.text(
                lx,
                inner.cy + 190,
                "this draw: " + ("happens" if hit else "does not"),
                size=30,
                fill=pal.unknown if hit else pal.text_faint,
                weight=600,
            )


# ------------------------------------------------------------------ two_ladders


@scene(
    "two_ladders",
    required=("top", "bottom"),
    optional=("highlight", "probe", "probe_label"),
    demo={
        "top": {
            "scale": "ICD 203 (intelligence)",
            "rungs": [
                {"word": "almost no chance", "lo": 1, "hi": 5},
                {"word": "very unlikely", "lo": 5, "hi": 20},
                {"word": "unlikely", "lo": 20, "hi": 45},
                {"word": "roughly even chance", "lo": 45, "hi": 55},
                {"word": "likely", "lo": 55, "hi": 80},
                {"word": "very likely", "lo": 80, "hi": 95},
                {"word": "almost certain", "lo": 95, "hi": 99},
            ],
        },
        "bottom": {
            "scale": "IPCC (climate)",
            "rungs": [
                {"word": "exceptionally unlikely", "lo": 0, "hi": 1},
                {"word": "very unlikely", "lo": 0, "hi": 10},
                {"word": "unlikely", "lo": 0, "hi": 33},
                {"word": "about as likely as not", "lo": 33, "hi": 66},
                {"word": "likely", "lo": 66, "hi": 100},
                {"word": "very likely", "lo": 90, "hi": 100},
                {"word": "virtually certain", "lo": 99, "hi": 100},
            ],
        },
        "highlight": "likely",
        "probe": 60,
    },
)
def two_ladders(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Two probability-word ladders on one shared 0-100 axis; one word lit in both, an optional probe line."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    label_w = 400
    x0, x1 = inner.x + label_w + 40, inner.right - 40
    axis_y = inner.bottom - 46
    panels = (p["top"], p["bottom"])
    gap = 34
    rows = [len(pp["rungs"]) for pp in panels]
    row = min(40.0, (axis_y - inner.y - 20 - gap - 2 * 34) / max(1, sum(rows)))
    hl = p.get("highlight")

    def X(v: float) -> float:
        return lerp(x0, x1, clamp(v / 100.0))

    k0 = at(c.t, 0.0, 0.25) if not c.settled else 1.0
    _axis(f, x0, x1, axis_y, k0, size=24)
    for v in range(0, 101, 10):
        f.line(X(v), inner.y, X(v), axis_y, stroke=hexa(pal.line, 0.55 if v % 50 == 0 else 0.28), width=1, opacity=k0)
    kh = c.beat(2, dur=0.8, spacing=1.8) if hl else 0.0
    y = inner.y + 4
    lit_spans: list[tuple[float, float, float]] = []
    for pi, panel in enumerate(panels):
        kp = c.beat(pi, dur=0.9, spacing=1.4)
        tone = pal.known if pi == 0 else pal.cool
        with f.group(opacity=kp):
            tracked(f, inner.x, y + 24, str(panel.get("scale", "")).upper(), size=20, fill=tone)
        y += 34
        rungs = list(panel["rungs"])
        n = len(rungs)
        for i, rung in enumerate(rungs):
            ry = y + row * (n - 1 - i) + row / 2
            ki = clamp((kp * (n + 2) - i) / 2.5) if not c.settled else 1.0
            lit = hl is not None and rung.get("word") == hl
            klit = kh if lit else 0.0
            color = mix_hex(tone, pal.unknown, klit)
            f.text(
                inner.x + label_w,
                ry + 9,
                str(rung["word"]),
                size=25,
                fill=mix_hex(pal.text_soft, pal.text, klit),
                anchor="end",
                weight=600 if lit and klit > 0.5 else 400,
                alpha=ki,
            )
            lo, hi = float(rung["lo"]), float(rung["hi"])
            a = X(lo)
            b = lerp(a, X(hi), ease(ki))
            bh = row * 0.56
            if b - a > 0.5:
                f.rect(
                    Box(a, ry - bh / 2, max(bh * 0.3, b - a), bh),
                    fill=color,
                    r=bh / 2,
                    opacity=(0.55 + 0.4 * klit) * ki,
                )
            if lit:
                lit_spans.append((lo, hi, ry))
                if klit > 0.02:
                    inside = hi >= 90
                    f.text(
                        (X(lo) + X(hi)) / 2 if inside else X(hi) + 14,
                        ry + 8,
                        f"{lo:g}–{hi:g}%",
                        size=22 if inside else 24,
                        fill=pal.ground if inside else pal.unknown,
                        family=MONO,
                        weight=600 if inside else 400,
                        anchor="middle" if inside else "start",
                        alpha=klit,
                    )
        y += row * n + gap
    if kh > 0.02 and len(lit_spans) == 2:
        top_y, bot_y = lit_spans[0][2], lit_spans[1][2]
        for v in (lit_spans[0][0], lit_spans[1][0]):
            f.line(X(v), top_y, X(v), bot_y, stroke=hexa(pal.unknown, 0.6), width=2, dash=[6, 7], opacity=kh)
    probe = p.get("probe")
    if probe is not None:
        kq = c.beat(3, dur=0.9, spacing=2.4)
        if kq > 0.01:
            xv = X(float(probe))
            wob = 0.6 * math.sin(c.seconds * 2.0)
            f.line(
                xv + wob, inner.y + 36, xv + wob, lerp(inner.y + 36, axis_y, kq), stroke=pal.text, width=3, opacity=0.9
            )
            f.circle(xv, axis_y, 9, fill=pal.text, opacity=kq)
            f.text(
                xv,
                inner.y + 26,
                str(p.get("probe_label") or f"{float(probe):g}%"),
                size=26,
                fill=pal.text,
                family=MONO,
                anchor="middle",
                alpha=kq,
            )


# ------------------------------------------------------------------ pull_to_middle


@scene(
    "pull_to_middle",
    required=("rows",),
    optional=("mean_label", "range_label"),
    demo={
        "rows": [
            {"word": "very likely", "lo": 90, "hi": 100, "mean": 62},
            {"word": "likely", "lo": 66, "hi": 100, "mean": 54},
            {"word": "unlikely", "lo": 0, "hi": 33, "mean": 44},
            {"word": "very unlikely", "lo": 0, "hi": 10, "mean": 41},
        ],
        "mean_label": "readers' average",
        "range_label": "meant as",
    },
)
def pull_to_middle(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Intended ranges as bars; on beat 1 each reader average slides out from its range toward 50."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    rows = list(p["rows"])
    n = len(rows)
    label_w = 330
    x0, x1 = inner.x + label_w + 40, inner.right - 30
    axis_y = inner.bottom - 50
    top = inner.y + 90
    row = min(130.0, (axis_y - top - 10) / max(1, n))

    def X(v: float) -> float:
        return lerp(x0, x1, clamp(v / 100.0))

    k0 = at(c.t, 0.0, 0.25) if not c.settled else 1.0
    _axis(f, x0, x1, axis_y, k0)
    g = pulse(c.seconds, 3.0)
    f.line(X(50), top - 40, X(50), axis_y, stroke=hexa(pal.text_faint, 0.5 + 0.3 * g), width=2, dash=[8, 8], opacity=k0)
    f.text(X(50), top - 48, "50%", size=24, fill=pal.text_faint, family=MONO, anchor="middle", alpha=k0)
    km_all = c.beat(1, dur=1.4, name="ease-in-out-cubic", spacing=1.6)
    with f.group(opacity=k0):
        f.rect(Box(inner.x, inner.y + 4, 26, 16), fill=pal.known, r=8)
        f.text(inner.x + 40, inner.y + 19, str(p.get("range_label", "meant as")), size=26, fill=pal.text_soft)
    with f.group(opacity=km_all):
        lx = inner.x + 300
        f.circle(lx + 12, inner.y + 12, 11, fill=pal.unknown)
        f.text(lx + 36, inner.y + 21, str(p.get("mean_label", "readers' average")), size=26, fill=pal.text_soft)
    for i, r_ in enumerate(rows):
        y = top + row * i + row / 2
        k = at(c.t, 0.1 + 0.5 * i / max(1, n), 0.45 + 0.5 * i / max(1, n)) if not c.settled else 1.0
        lo, hi, mean = float(r_["lo"]), float(r_["hi"]), float(r_["mean"])
        with f.group(opacity=k):
            f.text(inner.x + label_w, y + 11, str(r_["word"]), size=32, fill=pal.text, anchor="end")
            f.rect(Box(X(lo), y - 14, X(hi) - X(lo), 28), fill=hexa(pal.known, 0.75), r=14)
        km = clamp((km_all * (n + 1) - i * 0.6) / 1.4) if not c.settled else 1.0
        if km <= 0.001:
            continue
        edge = hi if mean > hi else lo if mean < lo else mean
        v = lerp(edge, mean, ease(km, "ease-in-out-cubic"))
        if abs(X(v) - X(edge)) > 18:
            _arrow(
                f, X(edge), y, X(v) + (-16 if v > edge else 16), y, stroke=hexa(pal.unknown, 0.8), width=3, opacity=km
            )
        f.circle(X(v), y, 14, fill=pal.unknown, opacity=km)
        f.text(X(v), y - 28, f"{round(v)}", size=28, fill=pal.unknown, family=MONO, anchor="middle", alpha=km)


# ------------------------------------------------------------------ bar_rows


@scene(
    "bar_rows",
    required=("rows",),
    optional=("note", "max", "unit"),
    demo={
        "rows": [
            {"label": "word alone", "value": 32},
            {"label": "table, one click away", "value": 39},
            {"label": "tooltip", "value": 40},
            {"label": "number in brackets", "value": 66, "tone": "unknown"},
        ],
        "note": "overlap with the official range",
    },
)
def bar_rows(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Labelled horizontal bars (a value, or a lo-hi range), each growing on its own beat."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    rows = list(p["rows"])
    n = len(rows)
    vmax = float(p.get("max", 100))
    unit = str(p.get("unit", "%"))
    note = p.get("note")
    top = inner.y + (56 if note else 10)
    label_w = min(560.0, max(f.measure(str(r["label"]), 32) for r in rows) + 30)
    x0, x1 = inner.x + label_w + 30, inner.right - 180
    row = min(120.0, (inner.bottom - top - 60) / max(1, n))
    k0 = at(c.t, 0.0, 0.25) if not c.settled else 1.0
    if note:
        f.text(inner.x, inner.y + 30, str(note), size=30, fill=pal.text_soft, alpha=k0)
    base_y = top + row * n + 10
    f.line(x0, top - 6, x0, base_y, stroke=pal.line, width=2, opacity=k0)
    for v in (0, 25, 50, 75, 100):
        if v <= vmax:
            xv = lerp(x0, x1, v / vmax)
            f.line(xv, top - 6, xv, base_y, stroke=hexa(pal.line, 0.35), width=1, opacity=k0)
            f.text(xv, base_y + 40, f"{v}{unit}", size=24, fill=pal.text_faint, family=MONO, anchor="middle", alpha=k0)
    for i, r_ in enumerate(rows):
        y = top + row * i + row / 2
        k = c.beat(int(r_.get("beat", i)), dur=1.0, name="ease-in-out-cubic", spacing=0.9)
        tone = role(pal, r_.get("tone"), "known")
        f.text(
            inner.x + label_w,
            y + 11,
            str(r_["label"]),
            size=32,
            fill=pal.text if k > 0.5 else pal.text_soft,
            anchor="end",
            alpha=max(k0 * 0.5, k),
        )
        bh = min(46.0, row * 0.5)
        if "lo" in r_:
            lo, hi = float(r_["lo"]), float(r_["hi"])
            a, b = lerp(x0, x1, lo / vmax), lerp(x0, x1, hi / vmax)
            m = (a + b) / 2
            a2, b2 = lerp(m, a, k), lerp(m, b, k)
            f.rect(Box(x0, y - bh / 2, (a2 - x0), bh), fill=hexa(tone, 0.35), r=0, opacity=k)
            f.rect(
                Box(a2, y - bh / 2, b2 - a2, bh),
                fill=tone,
                r=bh / 2,
                opacity=k * (0.55 + 0.25 * pulse(c.seconds + i, 2.8)),
            )
            end = b2
        else:
            v = float(r_["value"]) * ease(k)
            end = lerp(x0, x1, clamp(v / vmax))
            if end - x0 > 1:
                f.rect(Box(x0, y - bh / 2, end - x0, bh), fill=tone, r=bh / 2, opacity=0.9)
            sweep = (c.seconds * 0.35 + i * 0.23) % 1.0
            if k >= 0.99 and end - x0 > 30:
                f.circle(lerp(x0 + 10, end - 10, sweep), y, bh * 0.22, fill=hexa("#ffffff", 0.3))
        txt = r_.get("text") or (f"{float(r_['value']) * ease(k):.0f}{unit}" if "value" in r_ else "")
        f.text(end + 20, y + 11, str(txt), size=32, fill=tone, family=MONO, alpha=k)


# ------------------------------------------------------------------ bracket_sentence


@scene(
    "bracket_sentence",
    required=("before", "word", "bracket"),
    optional=("after", "results"),
    demo={
        "before": "X is",
        "word": "very unlikely",
        "bracket": "(05–20%)",
        "after": "to happen this year.",
        "results": [{"label": "word alone", "value": 32}, {"label": "number in brackets", "value": 66}],
    },
)
def bracket_sentence(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """A sentence whose probability word gains its number in brackets on beat 0; results follow."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    size = 60.0
    before, word, bracket, after = str(p["before"]), str(p["word"]), str(p["bracket"]), str(p.get("after", ""))
    kb = c.beat(0, dur=0.9, name="ease-in-out-cubic", spacing=0.6)
    sp = f.measure(" ", size, DISPLAY)
    wb = f.measure(before, size, DISPLAY)
    ww = f.measure(word, size, DISPLAY)
    wk = f.measure(bracket, size * 0.8, MONO)
    wa = f.measure(after, size, DISPLAY)
    total = wb + sp + ww + sp + (wk + sp + 14) * kb + wa
    while total > inner.w - 40 and size > 36:
        size -= 2
        sp = f.measure(" ", size, DISPLAY)
        wb, ww, wa = f.measure(before, size, DISPLAY), f.measure(word, size, DISPLAY), f.measure(after, size, DISPLAY)
        wk = f.measure(bracket, size * 0.8, MONO)
        total = wb + sp + ww + sp + (wk + sp + 14) * kb + wa
    results = p.get("results") or []
    y = inner.y + (inner.h * 0.28 if results else inner.cy) + size * 0.35
    x = inner.cx - total / 2
    k0 = at(c.t, 0.0, 0.25) if not c.settled else 1.0
    f.text(x, y, before, size=size, fill=pal.text_soft, family=DISPLAY, alpha=k0)
    x += wb + sp
    g = pulse(c.seconds, 2.6)
    f.rect(Box(x - 8, y + 14, ww + 16, 5), fill=pal.unknown, r=2, opacity=k0 * (0.6 + 0.4 * g))
    f.text(x, y, word, size=size, fill=pal.text, family=DISPLAY, alpha=k0)
    x += ww + sp
    if kb > 0.01:
        with f.group(opacity=kb, dy=(1 - kb) * -16):
            f.rect(Box(x - 10, y - size * 0.82, wk + 20, size * 1.08), fill=hexa(pal.unknown, 0.16), r=10)
            f.text(x, y - size * 0.06, bracket, size=size * 0.8, fill=pal.unknown, family=MONO)
    x += (wk + sp + 14) * kb
    f.text(x, y, after, size=size, fill=pal.text_soft, family=DISPLAY, alpha=k0)
    if results:
        x0 = inner.x + 470
        x1 = inner.right - 150
        for i, r_ in enumerate(results):
            ry = inner.y + inner.h * 0.55 + i * 110
            kr = c.beat(1 + i, dur=1.0, name="ease-in-out-cubic", spacing=1.4)
            tone = pal.unknown if i == len(results) - 1 else pal.known
            f.text(x0 - 30, ry + 12, str(r_["label"]), size=34, fill=pal.text, anchor="end", alpha=max(0.35 * k0, kr))
            f.rect(Box(x0, ry - 24, x1 - x0, 48), fill=pal.surface_2, r=24, opacity=k0)
            v = float(r_["value"]) * ease(kr)
            if v > 0.5:
                f.rect(Box(x0, ry - 24, (x1 - x0) * v / 100, 48), fill=tone, r=24)
            f.text(x0 + (x1 - x0) * v / 100 + 20, ry + 13, f"{v:.0f}%", size=34, fill=tone, family=MONO, alpha=kr)
        f.text(
            x0,
            inner.y + inner.h * 0.55 + len(results) * 110 - 20,
            "overlap of readers' ranges with the official range",
            size=26,
            fill=pal.text_faint,
            alpha=k0,
        )


# ------------------------------------------------------------------ rain_readings


def _rain_drop(f: Frame, x: float, y: float, s: float, color: str, opacity: float = 1.0) -> None:
    f.polygon([(x, y - s), (x + s * 0.55, y + s * 0.2), (x - s * 0.55, y + s * 0.2)], fill=color, opacity=opacity)
    f.circle(x, y + s * 0.25, s * 0.56, fill=color, opacity=opacity)


@scene(
    "rain_readings",
    required=(),
    optional=("value", "correct", "image", "titles", "placeholders"),
    demo={"value": 30, "correct": 2},
)
def rain_readings(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """One forecast, three readings (time, area, days); beats 0-2 bring each in, beat 3 marks the intended one."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    value = float(p.get("value", 30))
    correct = p.get("correct")
    titles = p.get("titles") or [
        f"{value:g}% of the time",
        f"{value:g}% of the area",
        f"{value * 10 / 100:g} of 10 days like this",
    ]
    k0 = at(c.t, 0.0, 0.25) if not c.settled else 1.0
    head = f"“{value:g}% chance of rain tomorrow”"
    img = ctx.image(p.get("image"))
    hx = inner.cx + (40 if img is not None else 0)
    f.text(hx, inner.y + 56, head, size=56, fill=pal.text, family=DISPLAY, anchor="middle", alpha=k0)
    if img is not None:
        hw = f.measure(head, 56, DISPLAY)
        _image_badge(f, ctx, p.get("image"), hx - hw / 2 - 70, inner.y + 44, 72, k0, c)
    cards_box = Box(inner.x, inner.y + 110, inner.w, inner.h - 120)
    gap = 44
    cw = (cards_box.w - 2 * gap) / 3
    kc = c.beat(3, dur=0.8, spacing=3.0) if correct is not None else 0.0
    for i in range(3):
        card = Box(cards_box.x + i * (cw + gap), cards_box.y, cw, cards_box.h)
        k = c.beat(i, dur=0.8, spacing=1.0)
        right = correct is not None and i == int(correct)
        dim = 1.0 - (0.55 * kc if not right else 0.0)
        if k < 1.0 and p.get("placeholders"):
            kp = (at(c.t, 0.2 + 0.15 * i, 0.5 + 0.15 * i) if not c.settled else 1.0) * (1 - clamp(k * 4))
            g = 0.5 + 0.5 * pulse(c.seconds + i * 0.9, 2.6)
            with f.group(opacity=kp):
                f.rect(card, stroke=hexa(pal.line, 0.9), width=2, r=20, dash=[10, 10])
                f.text(
                    card.cx,
                    card.cy + 30,
                    "?",
                    size=110,
                    fill=hexa(pal.unknown, 0.4 + 0.5 * g),
                    family=DISPLAY,
                    anchor="middle",
                )
        with f.group(opacity=k * dim, dy=(1 - k) * 26):
            f.rect(card, fill=pal.surface, r=20)
            if right and kc > 0.01:
                f.rect(card, stroke=hexa(pal.known, kc), width=4, r=20)
            f.text(
                card.cx,
                card.bottom - 36,
                titles[i],
                size=f.fit(titles[i], card.w - 40, 32, 22),
                fill=pal.text,
                anchor="middle",
            )
            art = Box(card.x + 30, card.y + 30, card.w - 60, card.h - 110)
            cx, cy = art.cx, art.cy
            if i == 0:  # a clock face, 30% of it shaded
                r = min(art.w, art.h) * 0.42
                f.circle(cx, cy, r, fill=pal.surface_2, stroke=pal.line, width=3)
                sweep = 2 * math.pi * value / 100 * ease(k)
                pts = [(cx, cy)] + [(cx + r * math.sin(a), cy - r * math.cos(a)) for a in np.linspace(0, sweep, 40)]
                f.polygon(pts, fill=hexa(pal.cool, 0.7))
                for h in range(12):
                    a = h / 12 * 2 * math.pi
                    f.line(
                        cx + r * 0.86 * math.sin(a),
                        cy - r * 0.86 * math.cos(a),
                        cx + r * 0.96 * math.sin(a),
                        cy - r * 0.96 * math.cos(a),
                        stroke=pal.text_faint,
                        width=3,
                    )
                ha = c.seconds * 0.8
                f.line(cx, cy, cx + r * 0.72 * math.sin(ha), cy - r * 0.72 * math.cos(ha), stroke=pal.text, width=4)
                f.circle(cx, cy, 7, fill=pal.text)
            elif i == 1:  # a map of 10 x 10 cells, 30 of them wet
                n = 10
                s = min(art.w, art.h) * 0.86 / n
                gx, gy = cx - s * n / 2, cy - s * n / 2
                wet = set(rng(8).permutation(100)[: int(value)].tolist())
                # Contiguous-looking area: take the 30 cells nearest a point.
                pts = [(ci % n, ci // n) for ci in range(100)]
                ctr = (6.5 + 0.6 * math.sin(c.seconds * 0.3), 3.5)
                ranked = sorted(range(100), key=lambda j: (pts[j][0] - ctr[0]) ** 2 + (pts[j][1] - ctr[1]) ** 2)
                wet = set(ranked[: round(value * ease(k))])
                for j in range(100):
                    xx, yy = pts[j]
                    f.rect(
                        Box(gx + xx * s + 1.5, gy + yy * s + 1.5, s - 3, s - 3),
                        fill=hexa(pal.cool, 0.75) if j in wet else pal.surface_2,
                        r=3,
                    )
            else:  # ten days like tomorrow, three of them rainy
                cols, rows_ = 5, 2
                s = min(art.w / cols, art.h / rows_) * 0.9
                gx, gy = cx - s * cols / 2, cy - s * rows_ / 2
                rainy = {1, 5, 8}
                for d in range(10):
                    xx, yy = d % cols, d // cols
                    b = Box(gx + xx * s + 5, gy + yy * s + 5, s - 10, s - 10)
                    wet = d in rainy
                    f.rect(b, fill=pal.surface_2, stroke=hexa(pal.cool, 0.9) if wet else None, width=2, r=10)
                    if wet:
                        for q in range(3):
                            t = (c.seconds * 0.9 + q / 3 + d * 0.17) % 1.0
                            _rain_drop(
                                f,
                                b.x + b.w * (0.25 + 0.25 * q),
                                b.y + b.h * (0.2 + 0.6 * t),
                                b.w * 0.13,
                                pal.cool,
                                opacity=math.sin(math.pi * t),
                            )
                    else:
                        f.circle(b.cx, b.cy, b.w * 0.16, fill=hexa(pal.unknown, 0.55))
        if right and kc > 0.02:
            f.circle(card.right - 34, card.y + 34, 22 * ease(kc, "ease-out-back"), fill=pal.known)
            f.polyline(
                [(card.right - 44, card.y + 35), (card.right - 36, card.y + 43), (card.right - 23, card.y + 26)],
                stroke=pal.ground,
                width=5,
            )


# ------------------------------------------------------------------ charley


_COAST = [(0.495, -0.02), (0.505, 0.14), (0.515, 0.30), (0.522, 0.44), (0.535, 0.58), (0.555, 0.78), (0.585, 1.02)]
_TAMPA = (0.534, 0.30)
_PUNTA = (0.538, 0.58)
_START = (0.25, 1.04)
_END = (0.64, 0.0)


def _bez(p0, p1, p2, t):
    return (
        (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0],
        (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1],
    )


def _charley_body(f: Frame, plot: Box, p: dict[str, Any], c: Clock, ctx: Ctx, layers: list, head: list) -> None:
    pal = f.pal

    def P(uv: tuple[float, float]) -> tuple[float, float]:
        return plot.x + uv[0] * plot.w, plot.y + uv[1] * plot.h

    def kfor(name: str) -> float:
        if name not in layers:
            return 0.0
        return c.beat(layers.index(name), dur=1.2, name="ease-in-out-cubic", spacing=1.3)

    k0 = at(c.t, 0.0, 0.3) if not c.settled else 1.0
    with f.group(opacity=k0):
        land = [P(q) for q in _COAST] + [P((1.02, 1.02)), P((1.02, -0.02))]
        f.polygon(land, fill=pal.surface_2)
        f.polyline([P(q) for q in _COAST], stroke=pal.line, width=3)
        for j in range(5):
            yy = 0.12 + j * 0.2
            ph = c.seconds * 0.25 + j
            pts = [P((0.03 + 0.36 * t, yy + 0.008 * math.sin(ph + t * 9))) for t in np.linspace(0, 1, 30)]
            f.polyline(pts, stroke=hexa(pal.line, 0.5), width=1.5)
    sx, sy = P(_START)
    ex, ey = P(_END)
    length = math.hypot(ex - sx, ey - sy)
    ux, uy = (ex - sx) / length, (ey - sy) / length
    nx, ny = -uy, ux
    w0, w1 = 14.0, 370.0

    def half(t: float) -> float:
        return w0 + (w1 - w0) * t

    kcone = kfor("cone")
    if kcone > 0:
        t1 = kcone
        cxe, cye = sx + ux * length * t1, sy + uy * length * t1
        h1 = half(t1)
        # A cone is swept circles; tangents from the small start circle to the end circle, plus the end cap.
        up = [(sx + nx * w0, sy + ny * w0), (cxe + nx * h1, cye + ny * h1)]
        base = math.atan2(ny, nx)
        cap = [(cxe + h1 * math.cos(base - a), cye + h1 * math.sin(base - a)) for a in np.linspace(0, math.pi, 24)]
        lo = [(sx - nx * w0, sy - ny * w0)]
        f.polygon(up + cap[1:] + lo, fill=hexa(pal.unknown, 0.15), stroke=hexa(pal.unknown, 0.7), width=2)
    kc = kfor("circles")
    if kc > 0:
        for j, t in enumerate((0.12, 0.24, 0.36, 0.5, 0.64, 0.8, 0.96)):
            if t > kc:
                break
            x, y = sx + ux * length * t, sy + uy * length * t
            g = 0.5 + 0.5 * pulse(c.seconds + j * 0.4, 3.0)
            f.circle(x, y, half(t), stroke=hexa(pal.unknown, 0.3 + 0.35 * g), width=2)
            f.circle(x, y, 4, fill=pal.unknown)
    kl = kfor("line")
    if kl > 0:
        f.line(sx, sy, sx + ux * length * kl, sy + uy * length * kl, stroke=pal.text, width=4)
        if kl > 0.95:
            tq = 0.42
            off = (half(tq) + 26) if "cone" in layers else 30
            lx, ly = sx + ux * length * tq - nx * off, sy + uy * length * tq - ny * off
            f.text(lx, ly, "forecast line", size=26, fill=pal.text_soft, anchor="end")
    km = kfor("misses")
    if km > 0:
        ang = math.atan2(uy, ux)
        spread = math.atan2(w1, length)
        for j, off in enumerate((-1.45, -0.62, -0.3, 0.0, 0.28, 0.55, 0.8, 1.3, 1.6)):
            a = ang + off * spread
            leave = abs(off) > 1.0
            L = length * 0.92 * km
            wig = 0.03 * math.sin(c.seconds * 0.8 + j)
            pts = [
                (sx + math.cos(a + wig * q) * L * q, sy + math.sin(a + wig * q) * L * q) for q in np.linspace(0, 1, 20)
            ]
            f.polyline(
                pts, stroke=hexa(pal.warn if leave else pal.known, 0.9 if leave else 0.5), width=3 if leave else 2
            )
    ka = kfor("actual")
    if ka > 0:
        pts = [_bez(_START, (0.39, 0.67), _PUNTA, t) for t in np.linspace(0, 1, 40)]
        pts += [_bez(_PUNTA, (0.62, 0.42), (0.80, 0.18), t) for t in np.linspace(0, 1, 30)[1:]]
        m = max(2, int(ka * len(pts)))
        f.polyline([P(q) for q in pts[:m]], stroke=pal.warn, width=5)
        hx, hy = P(pts[m - 1])
        img = ctx.image(p.get("image"))
        if img is not None:
            head.append((hx, hy))
        else:
            spin = c.seconds * 2.2
            for arm in range(3):
                a0 = spin + arm * 2 * math.pi / 3
                f.arc(hx, hy, 20, a0, a0 + 1.4, stroke=pal.warn, width=4)
        if ka > 0.95:
            tx, ty = P((0.82, 0.18))
            f.text(tx + 50, ty + 10, "Charley's path", size=28, fill=pal.warn, weight=600)
    kcty = kfor("county")
    if kcty > 0:
        x, y = P(_PUNTA)
        g = pulse(c.seconds, 2.4)
        f.circle(
            x + 60, y + 10, 64 * ease(kcty), fill=hexa(pal.known, 0.2 + 0.1 * g), stroke=hexa(pal.known, 0.8), width=2
        )
        f.text(x + 90, y + 126, "Charlotte County", size=28, fill=pal.known, alpha=kcty, anchor="middle")
    for name, q, left in (("Tampa", _TAMPA, False), ("Punta Gorda", _PUNTA, True)):
        x, y = P(q)
        f.circle(x, y, 9, fill=pal.text, opacity=k0)
        if left:
            f.text(x + 20, y + 42, name, size=30, fill=pal.text, weight=600, alpha=k0)
        else:
            f.text(x + 22, y + 10, name, size=30, fill=pal.text, weight=600, alpha=k0)
    note = p.get("note")
    if note:
        f.text(plot.x + 10, plot.bottom - 14, str(note), size=22, fill=pal.text_faint, alpha=k0)


@scene(
    "charley",
    required=(),
    optional=("layers", "image", "note"),
    demo={"layers": ["cone", "line", "actual", "county"], "note": "Schematic, not to scale"},
)
def charley(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """A schematic Gulf coast: the cone and its centre line toward Tampa, the real track to Punta Gorda.

    ``layers`` lists what to draw, each arriving on its own beat, in order:
    ``circles`` (the cone's build), ``cone``, ``line``, ``misses`` (tracks that
    leave the cone), ``actual``, ``county``.
    """
    inner = header_block(f, box, p, c)
    layers = list(p.get("layers") or ["cone", "line"])
    plot = Box(inner.x + 10, inner.y, inner.w - 20, inner.h - 6)
    head: list[tuple[float, float]] = []
    with f.group(clip=plot):
        _charley_body(f, plot, p, c, ctx, layers, head)
    img = ctx.image(p.get("image"))
    if img is not None and head:
        hx, hy = head[0]
        spin = 3 * math.sin(c.seconds * 1.4)
        f.image(img, Box(hx - 40, hy - 40 + spin, 80, 80), opacity=1.0)


# ------------------------------------------------------------------ action_ladder


@scene(
    "action_ladder",
    required=("rungs",),
    optional=("image", "highlight", "scale"),
    demo={
        "scale": "ASC 450, loss contingencies",
        "rungs": [
            {"word": "Probable", "gloss": "“likely to occur”", "action": "book it"},
            {
                "word": "Reasonably possible",
                "gloss": "“more than remote but less than likely”",
                "action": "tell readers",
            },
            {"word": "Remote", "gloss": "“slight”", "action": "nothing"},
        ],
    },
)
def action_ladder(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Words defined by words: each rung's word (beat 0), its gloss (beat 1), the action it sets (beat 2)."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    rungs = list(p["rungs"])
    n = len(rungs)
    scale = p.get("scale")
    top = inner.y + (50 if scale else 0)
    if scale:
        tracked(
            f,
            inner.x,
            inner.y + 24,
            str(scale).upper(),
            size=20,
            fill=pal.unknown,
            alpha=at(c.t, 0, 0.3) if not c.settled else 1.0,
        )
    gap = 26
    rh = min(170.0, (inner.bottom - top - gap * (n - 1)) / n)
    hl = p.get("highlight")
    act_w = 330
    for i, r_ in enumerate(rungs):
        y = top + i * (rh + gap)
        card = Box(inner.x, y, inner.w - act_w - 80, rh)
        kw = clamp((c.beat(0, dur=1.2, spacing=0.8) * (n + 1) - i) / 1.5) if not c.settled else 1.0
        kg = c.beat(1, dur=0.9, spacing=1.8)
        ka = clamp((c.beat(2, dur=1.2, spacing=2.8) * (n + 1) - i) / 1.5) if not c.settled else 1.0
        lit = hl == i
        g = pulse(c.seconds + i * 0.8, 3.2)
        tone = [pal.known, pal.unknown, pal.text_faint][min(i, 2)] if n == 3 else pal.known
        with f.group(opacity=kw, dy=(1 - kw) * 20):
            f.rect(card, fill=pal.surface, r=18)
            f.rect(Box(card.x, card.y, 8, card.h), fill=hexa(tone, 0.7 + 0.3 * g), r=4)
            if lit:
                f.rect(card, stroke=hexa(pal.unknown, 0.5 + 0.4 * g), width=3, r=18)
            ws = f.fit(str(r_["word"]), card.w * 0.46, 50, 32, DISPLAY)
            f.text(card.x + 40, card.cy + ws * 0.34, str(r_["word"]), size=ws, fill=pal.text, family=DISPLAY)
            gl = r_.get("gloss")
            if gl:
                gx = card.x + card.w * 0.50
                lines = f.wrap(str(gl), 30, card.right - gx - 30)[:3]
                f.text_lines(
                    gx, card.cy - (len(lines) - 1) * 19 + 10, lines, size=30, fill=pal.text_soft, alpha=kg, leading=1.28
                )
        act = r_.get("action")
        if act and ka > 0.001:
            ab = Box(inner.right - act_w, y + rh * 0.18, act_w, rh * 0.64)
            with f.group(opacity=ka, dx=(1 - ka) * 30):
                _arrow(f, card.right + 12, card.cy, ab.x - 14, card.cy, stroke=pal.text_faint, width=3, head=12)
                f.rect(ab, fill=hexa(tone, 0.22), stroke=tone, width=2, r=ab.h / 2)
                f.text(
                    ab.cx,
                    ab.cy + 12,
                    str(act),
                    size=f.fit(str(act), ab.w - 40, 36, 24),
                    fill=pal.text,
                    anchor="middle",
                    weight=600,
                )
    _image_badge(
        f, ctx, p.get("image"), inner.right - 40, inner.y + 30, 44, at(c.t, 0, 0.3) if not c.settled else 1.0, c
    )


# ------------------------------------------------------------------ risk_seesaw


@scene(
    "risk_seesaw",
    required=("levels",),
    optional=("left", "right", "caption", "image"),
    demo={
        "levels": [
            {
                "name": "Preponderance of the evidence",
                "share": 0.5,
                "note": "share the risk of error in roughly equal fashion",
            },
            {"name": "Beyond a reasonable doubt", "share": 0.92, "note": "almost the entire risk of error on society"},
            {"name": "Clear and convincing evidence", "share": 0.72, "note": "in between"},
        ],
        "left": "the side that brings the case",
        "right": "the other side",
    },
)
def risk_seesaw(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """A balance of the risk of error: level *i* takes over on beat *i*; the beam tilts to its share."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    levels = list(p["levels"])
    n = len(levels)
    ks = [c.beat(i, dur=1.2, name="ease-in-out-cubic", spacing=2.0) for i in range(n)]
    active = 0
    share = float(levels[0].get("share", 0.5))
    for i in range(1, n):
        share = lerp(share, float(levels[i].get("share", 0.5)), ks[i])
        if ks[i] > 0.5:
            active = i
    k0 = at(c.t, 0.0, 0.3) if not c.settled else 1.0
    stage = Box(inner.x, inner.y, inner.w, inner.h - 150)
    cx, cy = stage.cx, stage.y + stage.h * 0.40
    half = min(stage.w * 0.34, 560)
    wob = 0.014 * math.sin(c.seconds * 1.1)
    ang = (share - 0.5) * 0.36 + wob  # positive tilts the left side down
    dx, dy = half * math.cos(ang), half * math.sin(ang)
    lx, ly = cx - dx, cy + dy
    rx, ry = cx + dx, cy - dy
    with f.group(opacity=k0):
        f.polygon(
            [(cx, cy + 6), (cx - 60, cy + 150), (cx + 60, cy + 150)], fill=pal.surface_2, stroke=pal.line, width=2
        )
        f.line(lx, ly, rx, ry, stroke=pal.text_soft, width=10)
        f.circle(cx, cy, 12, fill=pal.text)
        for (px, py), sh, label in (((lx, ly), share, p.get("left", "")), ((rx, ry), 1 - share, p.get("right", ""))):
            hang = 150
            f.line(px - 90, py + hang, px, py, stroke=pal.text_faint, width=2)
            f.line(px + 90, py + hang, px, py, stroke=pal.text_faint, width=2)
            pan = Box(px - 120, py + hang, 240, 16)
            f.rect(pan, fill=pal.text_soft, r=8)
            # The risk of error, drawn as a mound whose size follows its share (no numbers).
            h = 18 + 104 * sh
            w = 40 + 78 * sh
            mound = [(px - w, py + hang)] + [
                (px + w * math.cos(a), py + hang - h * math.sin(a)) for a in np.linspace(math.pi, 0, 24)
            ]
            f.polygon(mound, fill=hexa(pal.warn, 0.35 + 0.35 * sh), stroke=hexa(pal.warn, 0.9), width=2)
            if label:
                f.text(px, py + hang + 56, str(label), size=26, fill=pal.text_soft, anchor="middle")
        f.text(cx, stage.y + 26, "risk of error", size=28, fill=pal.warn, anchor="middle", weight=600)
    _image_badge(f, ctx, p.get("image"), inner.right - 60, inner.y + 50, 80, k0, c)
    tab_y = inner.bottom - 118
    tw = (inner.w - 30 * (n - 1)) / n
    slots = sorted(range(n), key=lambda j: float(levels[j].get("share", 0.5)))
    for i, lv in enumerate(levels):
        tb = Box(inner.x + slots.index(i) * (tw + 30), tab_y, tw, 108)
        kt = ks[i]
        on = i == active
        kb = at(c.t, 0.15 + 0.25 * slots.index(i), 0.45 + 0.25 * slots.index(i)) if not c.settled else 1.0
        with f.group(opacity=kb * (1.0 if on else 0.5 + 0.1 * kt)):
            f.rect(tb, fill=pal.surface, stroke=pal.unknown if on else None, width=3, r=16)
            name = str(lv["name"])
            f.text(
                tb.cx, tb.y + 44, name, size=f.fit(name, tb.w - 30, 30, 20), fill=pal.text, anchor="middle", weight=600
            )
            note = lv.get("note")
            if note:
                f.text(
                    tb.cx,
                    tb.y + 84,
                    str(note),
                    size=f.fit(str(note), tb.w - 30, 24, 16),
                    fill=pal.text_soft,
                    anchor="middle",
                )


# ------------------------------------------------------------------ checklist


@scene(
    "checklist",
    required=("items",),
    optional=("image", "done"),
    demo={
        "heading": "A full statement of uncertainty",
        "items": [
            {"title": "What", "detail": "a fact, a number, or a scientific claim"},
            {"title": "In what form", "detail": "a range, a probability, a word"},
            {"title": "How good is the evidence", "detail": "the confidence behind it"},
        ],
    },
)
def checklist(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Items arrive and tick on beats; ``done`` items (from an earlier segment) start ticked."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    items = list(p["items"])
    n = len(items)
    done = int(p.get("done", 0))
    rh = min(150.0, (inner.h - 20) / n)
    for i, it in enumerate(items):
        y = inner.y + 10 + i * rh
        k = 1.0 if i < done else c.beat(i - done, dur=0.9, spacing=1.6)
        kt = 1.0 if i < done else c.beat(i - done, dur=0.6, name="ease-out-back", spacing=1.6)
        row = Box(inner.x, y, inner.w, rh - 22)
        g = pulse(c.seconds + i, 3.4)
        with f.group(opacity=max(0.18, k), dy=(1 - k) * 20):
            f.rect(row, fill=pal.surface, r=18)
            bx = Box(row.x + 36, row.cy - 28, 56, 56)
            f.rect(bx, stroke=hexa(pal.known, 0.6 + 0.4 * g), width=3, r=12)
            if kt > 0.02:
                s = kt
                f.polyline(
                    [(bx.x + 12, bx.cy), (bx.x + 12 + 12 * s, bx.cy + 13 * s), (bx.x + 12 + 34 * s, bx.cy - 18 * s)],
                    stroke=pal.known,
                    width=6,
                )
            ts = f.fit(str(it["title"]), row.w * 0.4, 46, 30, DISPLAY)
            f.text(row.x + 130, row.cy + ts * 0.34, str(it["title"]), size=ts, fill=pal.text, family=DISPLAY)
            d = it.get("detail")
            if d:
                f.text(
                    row.x + row.w * 0.46,
                    row.cy + 11,
                    str(d),
                    size=f.fit(str(d), row.w * 0.52, 32, 22),
                    fill=hexa(pal.text_soft, 0.85 + 0.15 * g),
                )


# ------------------------------------------------------------------ confidence_grid


@scene(
    "confidence_grid",
    required=(),
    optional=("mark", "likelihood", "separate"),
    demo={"mark": [1, 1], "likelihood": "likely (66–100%)", "separate": True},
)
def confidence_grid(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """The IPCC confidence grid (evidence by agreement), kept apart from a likelihood chip."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    ev = ["limited", "medium", "robust"]
    ag = ["low", "medium", "high"]
    lik = p.get("likelihood")
    gw = min(inner.h - 110, inner.w * (0.5 if lik else 0.8))
    gx = inner.x + 190
    gy = inner.y + 10
    cs = gw / 3
    k0 = at(c.t, 0.0, 0.5) if not c.settled else 1.0
    for a in range(3):
        for e in range(3):
            kk = clamp((k0 * 9 - (e + (2 - a))) / 3) if not c.settled else 1.0
            strength = (e + a) / 4
            b = Box(gx + e * cs + 4, gy + (2 - a) * cs + 4, cs - 8, cs - 8)
            f.rect(b, fill=mix_hex(pal.surface, pal.known, 0.12 + 0.7 * strength), r=12, opacity=kk)
    f.text(gx + gw / 2, gy + gw + 44, "evidence", size=28, fill=pal.text_soft, anchor="middle", alpha=k0)
    for e in range(3):
        f.text(gx + (e + 0.5) * cs, gy + gw - 18, ev[e], size=22, fill=pal.text, anchor="middle", alpha=k0 * 0.8)
    for a in range(3):
        f.text(gx - 20, gy + (2 - a + 0.5) * cs + 8, ag[a], size=24, fill=pal.text_faint, anchor="end", alpha=k0)
    f.text(gx - 20, gy + 20, "agreement", size=24, fill=pal.text_soft, anchor="end", alpha=k0)
    g = pulse(c.seconds, 2.8)
    f.text(
        gx + gw / 2,
        gy + gw + 84,
        "confidence rises toward the top right",
        size=24,
        fill=pal.text_faint,
        anchor="middle",
        alpha=k0 * (0.7 + 0.3 * g),
    )
    mark = p.get("mark")
    if mark is not None:
        km = c.beat(1, dur=0.8, name="ease-out-back", spacing=1.8)
        e, a = int(mark[0]), int(mark[1])
        b = Box(gx + e * cs + 4, gy + (2 - a) * cs + 4, cs - 8, cs - 8)
        f.rect(b, stroke=pal.unknown, width=4 + 2 * g, r=12, opacity=km)
        f.text(b.cx, b.cy + 10, "medium", size=30, fill=pal.text, anchor="middle", weight=600, alpha=km)
    if lik:
        kl = c.beat(2, dur=0.9, spacing=3.0)
        lx = gx + gw + 150
        lb = Box(lx, inner.y + inner.h * 0.30, inner.right - lx, 120)
        with f.group(opacity=kl, dx=(1 - kl) * 30):
            tracked(f, lb.x, lb.y - 24, "LIKELIHOOD: ABOUT THE EVENT", size=20, fill=pal.unknown)
            f.rect(lb, fill=pal.surface, stroke=pal.unknown, width=2, r=18)
            f.text(lb.cx, lb.cy + 14, str(lik), size=f.fit(str(lik), lb.w - 40, 42, 26), fill=pal.text, anchor="middle")
            tracked(f, lb.x, lb.bottom + 50, "CONFIDENCE: ABOUT THE EVIDENCE", size=20, fill=pal.known)
            if p.get("separate"):
                ks = c.beat(3, dur=0.8, spacing=3.8)
                sy = lb.bottom + 120
                f.text(lb.x, sy + 20, "never in the same sentence", size=32, fill=pal.warn, alpha=ks, weight=600)


# ------------------------------------------------------------------ sentence_builder


@scene(
    "sentence_builder",
    required=("parts",),
    optional=("label",),
    demo={
        "label": "An example",
        "parts": [
            {"text": "Rain tomorrow is likely", "tag": "the word"},
            {"text": "(55–80%),", "tag": "the number", "mono": True},
            {"text": "counted over days like tomorrow at this spot.", "tag": "the reference class"},
            {"text": "Confidence in that range: medium.", "tag": "the evidence", "newline": True},
        ],
    },
)
def sentence_builder(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """A statement assembled a piece at a time, each piece tagged with the job it does."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    parts = list(p["parts"])
    tones = [pal.text, pal.unknown, pal.known, pal.cool, pal.warn]
    size = 50.0
    label = p.get("label")
    k0 = at(c.t, 0.0, 0.3) if not c.settled else 1.0
    if label:
        tracked(f, inner.x, inner.y + 24, str(label).upper(), size=20, fill=pal.text_faint, alpha=k0)
    # Lay pieces out as word runs that wrap, remembering each piece's extent per line.
    while True:
        x, line = 0.0, 0
        spans: list[list[tuple[int, float, float]]] = [[] for _ in parts]
        words_at: list[tuple[int, int, float, str]] = []
        sp = f.measure(" ", size, DISPLAY)
        for i, part in enumerate(parts):
            if part.get("newline") and x > 0:
                x, line = 0.0, line + 1
            fam = MONO if part.get("mono") else DISPLAY
            fs = size * (0.84 if part.get("mono") else 1.0)
            for w in str(part["text"]).split():
                ww = f.measure(w, fs, fam)
                if x > 0 and x + ww > inner.w - 40:
                    x, line = 0.0, line + 1
                words_at.append((i, line, x, w))
                if spans[i] and spans[i][-1][0] == line:
                    spans[i][-1] = (line, spans[i][-1][1], x + ww)
                else:
                    spans[i].append((line, x, x + ww))
                x += ww + sp
        if line <= 3 or size <= 34:
            break
        size -= 2
    lead = size * 2.3
    nlines = line + 1
    y0 = inner.y + 60 + max(0.0, (inner.h - 60 - nlines * lead) / 2) + size
    x0 = inner.x + 20
    for i, part in enumerate(parts):
        k = c.beat(i, dur=0.8, spacing=1.4)
        if k <= 0.001:
            continue
        tone = tones[i % len(tones)]
        fam = MONO if part.get("mono") else DISPLAY
        fs = size * (0.84 if part.get("mono") else 1.0)
        with f.group(opacity=k, dy=(1 - k) * 14):
            for j, ln, x, w in words_at:
                if j == i:
                    f.text(x0 + x, y0 + ln * lead, w, size=fs, fill=pal.text if i == 0 else tone, family=fam)
            tag = part.get("tag")
            for sl, (ln, a, b) in enumerate(spans[i]):
                uy = y0 + ln * lead + 18
                g = 0.6 + 0.4 * pulse(c.seconds + i * 0.7, 3.0)
                f.line(
                    x0 + a, uy, x0 + a + (b - a) * ease(k), uy, stroke=hexa(tone if i else pal.text_soft, g), width=3
                )
                if tag and sl == 0:
                    f.text(x0 + a, uy + 36, str(tag), size=24, fill=tone if i else pal.text_soft, weight=600)


# ------------------------------------------------------------------ statement


@scene(
    "statement",
    required=("lines",),
    optional=("highlight", "note"),
    demo={
        "lines": ["Uncertainty is not communicated", "until the listener holds", "the number the speaker meant."],
        "highlight": ["the number the speaker meant."],
    },
)
def statement(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Large display lines arriving on beats; highlighted lines take the amber and an underline."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    lines = [str(x) for x in p["lines"]]
    hl = p.get("highlight") or []
    size = 76.0
    while size > 44 and max(f.measure(ln, size, DISPLAY) for ln in lines) > inner.w - 80:
        size -= 2
    lead = size * 1.3
    note = p.get("note")
    block = lead * len(lines) + (80 if note else 0)
    top = inner.cy - block / 2 + size * 0.8
    r = rng(17)
    fade = at(c.t, 0.0, 0.5) if not c.settled else 1.0
    for i in range(18):
        x = inner.x + inner.w * ((r.uniform() + 0.01 * math.sin(c.seconds * 0.2 + i)) % 1.0)
        y = inner.y + inner.h * r.uniform(0.05, 0.95)
        f.circle(
            x,
            y,
            r.uniform(2, 5),
            fill=pal.known if i % 3 else pal.unknown,
            opacity=(0.08 + 0.1 * pulse(c.seconds + i, 5.0)) * fade,
        )
    for i, ln in enumerate(lines):
        k = c.beat(i, dur=0.9, spacing=1.1)
        lit = ln in hl
        y = top + i * lead
        with f.group(opacity=k, dy=(1 - k) * 18):
            f.text(inner.cx, y, ln, size=size, fill=pal.unknown if lit else pal.text, family=DISPLAY, anchor="middle")
            if lit:
                w = f.measure(ln, size, DISPLAY)
                g = 0.55 + 0.45 * pulse(c.seconds, 2.6)
                f.line(
                    inner.cx - w / 2 * ease(k),
                    y + 20,
                    inner.cx + w / 2 * ease(k),
                    y + 20,
                    stroke=hexa(pal.unknown, g),
                    width=3,
                )
    if note:
        kn = c.beat(len(lines), dur=0.8, spacing=1.1)
        f.text(
            inner.cx, top + len(lines) * lead + 20, str(note), size=34, fill=pal.text_soft, anchor="middle", alpha=kn
        )
