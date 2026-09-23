"""The scene library: every visual the uncertainty videos need, drawn per frame.

A scene is a function ``draw(frame, box, params, clock, ctx)``. ``clock.t`` is
reveal progress (0..1 over the reveal window), ``clock.local`` seconds into the
segment, ``clock.seconds`` absolute programme time (ambient motion runs on it,
so a settled scene never freezes), ``clock.progress`` position through the
whole video, and ``clock.beat(i)`` eased progress since the *i*-th narration
beat (a phrase in ``say`` resolved to seconds, or an even default spacing).

Every scene draws inside the box it is handed; ``tests/test_scenes.py``
rasterises each one at four reveal points and fails on a pixel outside it.
Colour comes from roles on the palette, never from a hex literal.

Register a scene with :func:`scene`, giving its required and optional
parameters and a ``demo`` parameter set for the gallery and the tests.
"""

from __future__ import annotations

import math
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

import numpy as np
from bc_viz import PathBuilder

from . import brand
from .brand import DISPLAY, MONO, TEXT, Box
from .canvas import Frame, at, clamp, ease, hexa, lerp, mix_hex, pulse

__all__ = ["REGISTRY", "Clock", "Ctx", "SceneDef", "draw", "scene"]


# ------------------------------------------------------------------ plumbing


@dataclass(frozen=True, slots=True)
class Clock:
    t: float = 1.0
    local: float = 10.0
    seconds: float = 10.0
    progress: float = 0.5
    duration: float = 10.0
    beats: tuple[float, ...] = ()
    settled: bool = False

    def beat(self, i: int, dur: float = 0.9, name: str = "ease-out-cubic", spacing: float = 0.75) -> float:
        """Eased 0..1 since beat ``i``; beats not given fall at ``i * spacing`` seconds."""
        if self.settled:
            return 1.0
        start = self.beats[i] if i < len(self.beats) else i * spacing
        return at(self.local, start, start + dur, name)


@dataclass(slots=True)
class Ctx:
    images: dict[str, np.ndarray] = field(default_factory=dict)

    def image(self, ref: str | None) -> np.ndarray | None:
        if not ref:
            return None
        key = ref.split(":", 1)[1] if ref.startswith("image:") else ref
        return self.images.get(key)


Draw = Callable[[Frame, Box, dict[str, Any], Clock, Ctx], None]


@dataclass(frozen=True, slots=True)
class SceneDef:
    name: str
    fn: Draw
    required: tuple[str, ...]
    optional: tuple[str, ...]
    demo: dict[str, Any]
    note: str


REGISTRY: dict[str, SceneDef] = {}
_COMMON = ("kicker", "heading")


def scene(
    name: str, *, required: tuple[str, ...] = (), optional: tuple[str, ...] = (), demo: dict[str, Any] | None = None
) -> Callable[[Draw], Draw]:
    def wrap(fn: Draw) -> Draw:
        REGISTRY[name] = SceneDef(
            name, fn, required, tuple(optional) + _COMMON, demo or {}, (fn.__doc__ or "").strip().splitlines()[0]
        )
        return fn

    return wrap


def draw(f: Frame, name: str, params: dict[str, Any], box: Box, clock: Clock, ctx: Ctx | None = None) -> None:
    REGISTRY[name].fn(f, box, params, clock, ctx or Ctx())


# ------------------------------------------------------------------ shared pieces


def tracked(
    f: Frame,
    x: float,
    y: float,
    s: str,
    *,
    size: float,
    fill: str,
    tracking: float = 0.12,
    weight: int = 600,
    family: str = TEXT,
    anchor: str = "start",
    alpha: float = 1.0,
) -> float:
    """Letter-spaced small caps line (the rasteriser has no letter-spacing). Returns width."""
    gap = size * tracking
    widths = [f.measure(ch, size, family, weight) for ch in s]
    total = sum(widths) + gap * max(0, len(s) - 1)
    x0 = x - total / 2 if anchor == "middle" else x - total if anchor == "end" else x
    cx = x0
    for ch, w in zip(s, widths, strict=True):
        if ch != " ":
            f.text(cx, y, ch, size=size, fill=fill, family=family, weight=weight, alpha=alpha)
        cx += w + gap
    return total


def header_block(f: Frame, box: Box, p: dict[str, Any], c: Clock) -> Box:
    """Optional kicker and heading at the top of the stage; returns the box below them."""
    pal = f.pal
    kicker, heading = p.get("kicker"), p.get("heading")
    if not kicker and not heading:
        return box
    k = ease(c.t / 0.35) if not c.settled else 1.0
    y = box.y
    with f.group(opacity=k, dy=(1 - k) * 12):
        if kicker:
            tracked(f, box.x, y + 22, str(kicker).upper(), size=22, fill=pal.unknown)
            y += 40
        if heading:
            size = f.fit(str(heading), box.w, 60, 40, DISPLAY)
            f.text(box.x, y + size * 0.92, str(heading), size=size, fill=pal.text, family=DISPLAY)
            y += size * 1.25
    return Box(box.x, y + 24, box.w, box.bottom - y - 24)


def role(pal: brand.Palette, name: str | None, default: str = "known") -> str:
    name = name or default
    if name.startswith("#"):
        return name
    return getattr(pal, name)


def rng(seed: int) -> np.random.Generator:
    return np.random.default_rng(seed)


def ball(
    f: Frame, cx: float, cy: float, r: float, color: str, *, ring: str | None = None, opacity: float = 1.0
) -> None:
    """A lit sphere: base disc, a soft lower shade, a small highlight."""
    f.circle(cx, cy, r, fill=color, stroke=ring, width=2 if ring else 1, opacity=opacity)
    f.circle(cx + r * 0.08, cy + r * 0.12, r * 0.82, fill=hexa("#000000", 0.18), opacity=opacity)
    f.circle(cx, cy, r * 0.86, fill=color, opacity=opacity * 0.9)
    f.circle(cx - r * 0.34, cy - r * 0.36, r * 0.24, fill=hexa("#ffffff", 0.38), opacity=opacity)


# ------------------------------------------------------------------ title_card


@scene(
    "title_card",
    required=("title",),
    optional=("subtitle", "label"),
    demo={"title": "Risk is not uncertainty", "subtitle": "What the odds can and cannot tell us", "label": "Episode 1"},
)
def title_card(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """A display title over a slow field of drifting probability points."""
    pal = f.pal
    # Ambient field: deterministic points, drifting on absolute time.
    r = rng(7)
    n = 46
    xs, ys = r.uniform(0, 1, n), r.uniform(0, 1, n)
    phase, speed, size = r.uniform(0, 2 * math.pi, n), r.uniform(0.05, 0.16, n), r.uniform(2.5, 6.5, n)
    fade = ease(c.t / 0.6) if not c.settled else 1.0
    inner = box.inset(24)
    for i in range(n):
        x = inner.x + inner.w * ((xs[i] + 0.012 * math.sin(c.seconds * speed[i] + phase[i])) % 1.0)
        y = inner.y + inner.h * (ys[i] + 0.03 * math.sin(c.seconds * speed[i] * 1.7 + phase[i] * 2)) * 0.98
        tone = pal.known if i % 3 else pal.unknown
        tw = 0.10 + 0.14 * pulse(c.seconds + phase[i], 5.0 + speed[i] * 10)
        f.circle(x, y, size[i], fill=tone, opacity=tw * fade)
    # A faint horizon arc under the title.
    cx, cy = box.cx, box.cy
    f.arc(cx, cy + 620, 900, math.pi * 1.22, math.pi * 1.78, stroke=hexa(pal.line, 0.9), width=2, opacity=fade)
    label, title, sub = p.get("label"), str(p["title"]), p.get("subtitle")
    size = f.fit(title, box.w * 0.86, 116, 64, DISPLAY)
    lines = f.wrap(title, size, box.w * 0.86, DISPLAY)[:2]
    block = size * 1.08 * len(lines)
    top = cy - block / 2 - (30 if sub else 0)
    k1 = at(c.t, 0.05, 0.55) if not c.settled else 1.0
    if label:
        k0 = at(c.t, 0.0, 0.35) if not c.settled else 1.0
        tracked(f, cx, top - 34, str(label).upper(), size=24, fill=pal.unknown, anchor="middle", alpha=k0)
    with f.group(opacity=k1, dy=(1 - k1) * 26):
        for i, line in enumerate(lines):
            f.text(
                cx, top + size * 0.86 + i * size * 1.08, line, size=size, fill=pal.text, family=DISPLAY, anchor="middle"
            )
    k2 = at(c.t, 0.35, 0.85, "ease-in-out-cubic") if not c.settled else 1.0
    rule_y = top + block + 34
    half = 150 * k2
    f.line(cx - half, rule_y, cx + half, rule_y, stroke=pal.unknown, width=3, opacity=k2)
    if sub:
        k3 = at(c.t, 0.5, 1.0) if not c.settled else 1.0
        f.text(cx, rule_y + 64, str(sub), size=38, fill=pal.text_soft, anchor="middle", alpha=k3)


# ------------------------------------------------------------------ two_column_compare


@scene(
    "two_column_compare",
    required=("left", "right"),
    demo={
        "heading": "Two kinds of not knowing",
        "left": {"title": "Risk", "lines": ["The odds are known", "A fair die, a roulette wheel"], "tone": "known"},
        "right": {
            "title": "Uncertainty",
            "lines": ["The odds are not known", "A new drug, next year's market"],
            "tone": "unknown",
        },
    },
)
def two_column_compare(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Two cards side by side, the right one arriving on the second beat."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    left, right = Box(inner.x, inner.y, inner.w, inner.h - 30).split_x(0.5, gap=64)
    for i, (card, side) in enumerate(((left, p["left"]), (right, p["right"]))):
        k = c.beat(i * 1, dur=0.9, spacing=1.4)
        tone = role(pal, side.get("tone"), "known" if i == 0 else "unknown")
        with f.group(opacity=k, dy=(1 - k) * 28):
            f.rect(card, fill=pal.surface, r=22)
            f.rect(Box(card.x, card.y, card.w, 6), fill=tone, r=3)
            glow = 0.5 + 0.5 * pulse(c.seconds + i * 1.3, 3.6)
            f.circle(card.x + 58, card.y + 76, 13, fill=tone, opacity=0.35 + 0.5 * glow)
            f.circle(card.x + 58, card.y + 76, 7, fill=tone)
            size = f.fit(str(side["title"]), card.w - 140, 64, 40, DISPLAY)
            f.text(card.x + 92, card.y + 98, str(side["title"]), size=size, fill=pal.text, family=DISPLAY)
            y = card.y + 190
            for j, line in enumerate(side.get("lines", [])):
                kj = clamp((k - 0.35 - 0.2 * j) / 0.4) if not c.settled else 1.0
                wrapped = f.wrap(str(line), 36, card.w - 120)[:2]
                f.circle(card.x + 60, y - 12, 5, fill=pal.text_faint, opacity=kj)
                f.text_lines(
                    card.x + 88, y, wrapped, size=36, fill=pal.text_soft if j else pal.text, alpha=kj, leading=1.3
                )
                y += 36 * 1.3 * len(wrapped) + 30
                if y > card.bottom - 40:
                    break


# ------------------------------------------------------------------ urn


def _urn_path(b: Box) -> PathBuilder:
    """A jar: straight shoulders under a rim, a rounded belly, a flat foot."""
    x0, x1, y0, y1 = b.x, b.right, b.y, b.bottom
    neck = b.w * 0.16
    p = PathBuilder()
    p.move_to(x0 + neck, y0)
    p.cubic_to(x0 + neck, y0 + b.h * 0.10, x0, y0 + b.h * 0.12, x0, y0 + b.h * 0.34)
    p.line_to(x0, y1 - b.h * 0.16)
    p.cubic_to(x0, y1 - b.h * 0.02, x0 + b.w * 0.08, y1, x0 + b.w * 0.22, y1)
    p.line_to(x1 - b.w * 0.22, y1)
    p.cubic_to(x1 - b.w * 0.08, y1, x1, y1 - b.h * 0.02, x1, y1 - b.h * 0.16)
    p.line_to(x1, y0 + b.h * 0.34)
    p.cubic_to(x1, y0 + b.h * 0.12, x1 - neck, y0 + b.h * 0.10, x1 - neck, y0)
    return p


def _pack(b: Box, n: int, r: float, seed: int) -> list[tuple[float, float]]:
    """Ball centres settled in centred rows from the bottom of a jar, with a little jitter."""
    g = rng(seed)
    per_row = max(1, int((b.w - 2 * r) // (2.05 * r)) + 1)
    out: list[tuple[float, float]] = []
    row = 0
    while len(out) < n:
        cols = per_row - (row % 2)
        take = min(cols, n - len(out))
        width = (take - 1) * 2.05 * r
        x0 = b.cx - width / 2
        y = b.bottom - r - row * 1.78 * r
        for col in range(take):
            out.append((x0 + col * 2.05 * r + g.uniform(-1.2, 1.2), y + g.uniform(-0.8, 0.8)))
        row += 1
    return out


@scene(
    "urn",
    required=("left", "right"),
    optional=("colors",),
    demo={
        "heading": "Which urn would you draw from?",
        "left": {"label": "Urn A", "a": 50, "b": 50, "caption": "50 red, 50 black"},
        "right": {"label": "Urn B", "total": 100, "caption": "100 balls, mix unknown"},
    },
)
def urn(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Ellsberg's two urns: a known mix fills first; the unknown mix shimmers between colours."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    colors = p.get("colors") or {}
    red = role(pal, colors.get("a"), "warn")
    black = "#15181f" if pal.name == "ink" else "#1b2130"
    ring = pal.text_soft if pal.name == "ink" else None
    halves = inner.split_x(0.5, gap=80)
    for side_i, (half, side) in enumerate(zip(halves, (p["left"], p["right"]), strict=True)):
        k = c.beat(side_i * 2, dur=0.8, spacing=0.75)
        jar_h = min(half.h - 120, 520)
        jar_w = min(half.w * 0.62, jar_h * 0.86)
        jar = Box(half.cx - jar_w / 2, half.y + 6, jar_w, jar_h)
        with f.group(opacity=k, dy=(1 - k) * 20):
            f.path(_urn_path(jar), fill=hexa(pal.surface, 0.85), stroke=pal.line, width=3)
            f.line(
                jar.x + jar.w * 0.16 - 10, jar.y, jar.right - jar.w * 0.16 + 10, jar.y, stroke=pal.text_faint, width=5
            )
        n = int(side.get("total") or (int(side.get("a", 0)) + int(side.get("b", 0))))
        shown = max(1, min(n, 48))
        n_a = round(int(side.get("a", 0)) * shown / max(1, n))
        n = shown
        belly = Box(jar.x + 16, jar.y + jar.h * 0.34, jar.w - 32, jar.h * 0.66 - 14)
        r = 26.0
        while r > 8:
            per_row = max(1, int((belly.w - 2 * r) // (2.05 * r)) + 1)
            rows = math.ceil(n / max(1.0, per_row - 0.5))
            if rows * 1.78 * r + r <= belly.h * 0.86:
                break
            r -= 0.5
        spots = _pack(belly, n, r, 11 + side_i)
        known = "total" not in side
        order = rng(3 + side_i).permutation(n)
        fill_t = c.beat(side_i * 2 + 1, dur=1.6, spacing=0.75)
        for idx, (x, y) in enumerate(spots):
            appear = clamp((fill_t * (n + 10) - idx) / 10) if not c.settled else 1.0
            if appear <= 0:
                continue
            drop = (1 - ease(appear, "ease-out-back")) * 70
            if known:
                color = red if order[idx] < n_a else black
            else:
                w = clamp(0.5 + 1.8 * math.sin(c.seconds * 0.55 + idx * 2.39))
                color = mix_hex(red, black, w)
            ball(
                f, x, y - drop, r, color, ring=ring if (known and color == black) or not known else None, opacity=appear
            )
        if not known:
            q = 0.55 + 0.45 * pulse(c.seconds, 2.6)
            f.text(
                jar.cx,
                jar.y + jar.h * 0.26,
                "?",
                size=64,
                fill=pal.unknown,
                family=DISPLAY,
                anchor="middle",
                alpha=k * q,
            )
        with f.group(opacity=k):
            f.text(
                half.cx,
                jar.bottom + 58,
                str(side.get("label", "")),
                size=40,
                fill=pal.text,
                family=DISPLAY,
                anchor="middle",
            )
            cap = side.get("caption")
            if cap:
                f.text(half.cx, jar.bottom + 100, str(cap), size=28, fill=pal.text_soft, anchor="middle", family=MONO)


# ------------------------------------------------------------------ probability_bar


@scene(
    "probability_bar",
    required=("value",),
    optional=("label", "band", "band_label", "tone", "note", "start"),
    demo={
        "heading": "The chance of heads",
        "value": 50,
        "label": "a fair coin",
        "band": [40, 60],
        "note": "known exactly",
    },
)
def probability_bar(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """A 0-100 track; the fill and a counting marker arrive, an optional band shades a range."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    tone = role(pal, p.get("tone"), "known")
    value = float(p["value"])
    start = float(p.get("start", 0))
    x0, x1 = inner.x + 40, inner.right - 40
    cy = inner.y + inner.h * 0.5 + 40
    h = 30

    def X(v: float) -> float:
        return lerp(x0, x1, clamp(v / 100.0))

    k0 = at(c.t, 0.0, 0.3) if not c.settled else 1.0
    f.rect(Box(x0, cy - h / 2, x1 - x0, h), fill=pal.surface_2, r=h / 2, opacity=k0)
    for v in (0, 25, 50, 75, 100):
        f.line(X(v), cy + h / 2 + 14, X(v), cy + h / 2 + 30, stroke=pal.text_faint, width=2, opacity=k0)
        f.text(X(v), cy + h / 2 + 70, f"{v}%", size=28, fill=pal.text_faint, family=MONO, anchor="middle", alpha=k0)
    band = p.get("band")
    if band:
        kb = c.beat(1, dur=0.9, spacing=1.6)
        lo, hi = float(band[0]), float(band[1])
        mid = (lo + hi) / 2
        a, b = X(lerp(mid, lo, kb)), X(lerp(mid, hi, kb))
        by = cy + h / 2 + 118
        f.line(a, by, b, by, stroke=pal.unknown, width=3, opacity=kb)
        f.line(a, by - 14, a, by + 14, stroke=pal.unknown, width=3, opacity=kb)
        f.line(b, by - 14, b, by + 14, stroke=pal.unknown, width=3, opacity=kb)
        f.rect(Box(a, cy - h / 2, max(0.0, b - a), h), fill=hexa(pal.unknown, 0.22), r=h / 2, opacity=kb)
        bl = p.get("band_label") or f"{band[0]:g}% to {band[1]:g}%"
        f.text((a + b) / 2, by + 50, str(bl), size=30, fill=pal.unknown, anchor="middle", alpha=kb)
    k = at(c.t, 0.15, 0.85, "ease-in-out-cubic") if not c.settled else 1.0
    v = lerp(start, value, k)
    if v > 0.3:
        f.rect(Box(x0, cy - h / 2, X(v) - x0, h), fill=tone, r=h / 2, opacity=k0)
    mx = X(v)
    glow = pulse(c.seconds, 2.2)
    f.circle(mx, cy, 26 + 6 * glow, fill=tone, opacity=0.18 * k0)
    f.circle(mx, cy, 20, fill=pal.text, opacity=k0)
    f.circle(mx, cy, 11, fill=tone, opacity=k0)
    num = f"{round(v)}%"
    tx = clamp(mx, x0 + 60, x1 - 60)
    f.text(tx, cy - 62, num, size=76, fill=pal.text, family=MONO, anchor="middle", alpha=k0)
    label = p.get("label")
    if label:
        f.text(x0, cy - 150, str(label), size=40, fill=pal.text_soft, alpha=k0)
    note = p.get("note")
    if note:
        kn = at(c.t, 0.7, 1.0) if not c.settled else 1.0
        f.text(x1, cy - 150, str(note), size=34, fill=tone, anchor="end", alpha=kn)


# ------------------------------------------------------------------ word_ladder


@scene(
    "word_ladder",
    required=("rungs",),
    optional=("scale", "highlight", "source"),
    demo={
        "heading": "Words for chances",
        "scale": "ICD 203",
        "rungs": [
            {"word": "almost no chance", "lo": 1, "hi": 5},
            {"word": "very unlikely", "lo": 5, "hi": 20},
            {"word": "unlikely", "lo": 20, "hi": 45},
            {"word": "roughly even chance", "lo": 45, "hi": 55},
            {"word": "likely", "lo": 55, "hi": 80},
            {"word": "very likely", "lo": 80, "hi": 95},
            {"word": "almost certain", "lo": 95, "hi": 99},
        ],
        "highlight": "likely",
    },
)
def word_ladder(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Estimative words on the left, each mapped to its numeric range on a 0-100 axis."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    rungs = list(p["rungs"])
    n = len(rungs)
    label_w = 420
    x0, x1 = inner.x + label_w + 40, inner.right - 30
    axis_y = inner.bottom - 50
    top = inner.y + 10
    row = min(78.0, (axis_y - top - 20) / max(1, n))

    def X(v: float) -> float:
        return lerp(x0, x1, clamp(v / 100.0))

    k0 = at(c.t, 0.0, 0.25) if not c.settled else 1.0
    f.line(x0, axis_y, x1, axis_y, stroke=pal.line, width=2, opacity=k0)
    for v in range(0, 101, 10):
        big = v % 50 == 0
        f.line(X(v), axis_y, X(v), axis_y + (14 if big else 8), stroke=pal.text_faint, width=2, opacity=k0)
        if v % 25 == 0:
            f.text(X(v), axis_y + 46, f"{v}%", size=26, fill=pal.text_faint, family=MONO, anchor="middle", alpha=k0)
        f.line(X(v), top, X(v), axis_y, stroke=hexa(pal.line, 0.35 if not big else 0.6), width=1, opacity=k0)
    scale = p.get("scale")
    if scale:
        f.text(
            inner.x + label_w, axis_y + 46, str(scale), size=26, fill=pal.unknown, anchor="end", weight=600, alpha=k0
        )
    hl = p.get("highlight")
    windows = [(0.12 + 0.72 * i / max(1, n), 0.12 + 0.72 * i / max(1, n) + 0.3) for i in range(n)]
    for i, rung in enumerate(rungs):
        # Top of the ladder is the most likely word: draw highest range at the top.
        y = top + row * (n - 1 - i) + row / 2
        k = at(c.t, *windows[i]) if not c.settled else 1.0
        lit = hl is not None and rung.get("word") == hl
        tone = pal.unknown if lit else pal.known
        with f.group(opacity=k, dx=(1 - k) * -18):
            f.text(
                inner.x + label_w,
                y + 12,
                str(rung["word"]),
                size=34 if lit else 32,
                fill=pal.text if lit else pal.text_soft,
                anchor="end",
                weight=600 if lit else 400,
            )
        lo, hi = float(rung["lo"]), float(rung["hi"])
        grow = ease(clamp((k - 0.2) / 0.8))
        a = X(lo)
        b = lerp(a, X(hi), grow)
        bar_h = row * 0.46
        if b - a > 0.5:
            f.rect(
                Box(a, y - bar_h / 2, max(bar_h * 0.2, b - a), bar_h),
                fill=tone,
                r=bar_h / 2,
                opacity=(0.95 if lit else 0.72) * k,
            )
        if lit and grow > 0.99:
            f.text(X(hi) + 18, y + 10, f"{lo:g}–{hi:g}%", size=26, fill=pal.unknown, family=MONO)
            sweep = (c.seconds * 0.45) % 1.0
            sx = lerp(a, X(hi), sweep)
            f.circle(sx, y, bar_h * 0.36, fill=hexa("#ffffff", 0.35))


# ------------------------------------------------------------------ spaghetti_plot


def _walks(n: int, steps: int, seed: int, spread: float) -> np.ndarray:
    g = rng(seed)
    shocks = g.normal(0, 1, (n, steps))
    # Smooth the shocks so the paths read as forecasts, not noise.
    kernel = np.hanning(9)
    kernel /= kernel.sum()
    smooth = np.array([np.convolve(s, kernel, mode="same") for s in shocks])
    drift = g.normal(0, 0.35, (n, 1))
    walk = np.cumsum(smooth + drift * 0.08, axis=1)
    walk -= walk[:, :1]
    scale = np.abs(walk).max() or 1.0
    return walk / scale * spread


@scene(
    "spaghetti_plot",
    required=(),
    optional=("paths", "seed", "spread", "x_label", "y_label", "start_label", "mean", "image"),
    demo={
        "heading": "Twenty-four runs of one model",
        "paths": 24,
        "seed": 4,
        "x_label": "days ahead",
        "start_label": "today",
    },
)
def spaghetti_plot(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """An ensemble fanning from one known point; dots travel the paths once they are drawn."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    n = int(p.get("paths", 24))
    steps = 90
    walks = _walks(n, steps, int(p.get("seed", 4)), float(p.get("spread", 1.0)))
    plot = Box(inner.x + 60, inner.y + 10, inner.w - 100, inner.h - 90)
    x_of = np.linspace(plot.x, plot.right, steps)
    mid = plot.cy
    amp = plot.h * 0.46
    k0 = at(c.t, 0.0, 0.2) if not c.settled else 1.0
    f.line(plot.x, plot.bottom + 20, plot.right, plot.bottom + 20, stroke=pal.line, width=2, opacity=k0)
    x_label = p.get("x_label")
    if x_label:
        f.text(plot.right, plot.bottom + 66, str(x_label), size=28, fill=pal.text_faint, anchor="end", alpha=k0)
    reach = at(c.t, 0.1, 1.0, "ease-in-out-cubic") if not c.settled else 1.0
    upto = max(2, int(reach * steps))
    for i in range(n):
        wob = 0.018 * math.sin(c.seconds * 0.7 + i)
        ys = mid - (walks[i] * (1 + wob)) * amp
        pts = list(zip(x_of[:upto].tolist(), ys[:upto].tolist(), strict=True))
        f.polyline(pts, stroke=pal.known, width=2.2, opacity=0.38)
    if p.get("mean", True):
        mean = walks.mean(axis=0)
        ys = mid - mean * amp
        pts = list(zip(x_of[:upto].tolist(), ys[:upto].tolist(), strict=True))
        f.polyline(pts, stroke=pal.unknown, width=4.5, opacity=0.95 * k0)
    if reach >= 0.999:
        for i in range(0, n, 3):
            s = (c.seconds * 0.12 + i * 0.137) % 1.0
            j = min(steps - 1, int(s * (steps - 1)))
            y = mid - walks[i][j] * amp
            f.circle(float(x_of[j]), float(y), 5, fill=pal.known, opacity=0.9 * math.sin(math.pi * s))
    g = pulse(c.seconds, 2.0)
    f.circle(plot.x, mid, 18 + 5 * g, fill=pal.text, opacity=0.15 * k0)
    f.circle(plot.x, mid, 10, fill=pal.text, opacity=k0)
    sl = p.get("start_label")
    if sl:
        f.text(plot.x, plot.bottom + 66, str(sl), size=28, fill=pal.text_soft, alpha=k0)
    img = ctx.image(p.get("image"))
    if img is not None:
        ki = c.beat(0, dur=0.8, name="ease-out-back", spacing=0.4)
        side = 150 * (0.85 + 0.15 * ki)
        bob = 4 * math.sin(c.seconds * 1.2)
        cx, cy = plot.x + 90, plot.y + 80 + bob
        f.circle(cx, cy, side * 0.62, fill=pal.surface, opacity=ki)
        f.image(img, Box(cx - side / 2, cy - side / 2, side, side), opacity=ki)


# ------------------------------------------------------------------ cone


@scene(
    "cone", required=(), optional=("days", "labels", "growth"), demo={"heading": "The cone of uncertainty", "days": 5}
)
def cone(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """A forecast track with a cone widening day by day; a spinning mark rides the front."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    days = int(p.get("days", 5))
    plot = Box(inner.x + 60, inner.y + 20, inner.w - 140, inner.h - 100)
    n = 80
    xs = np.linspace(plot.x, plot.right, n)
    u = np.linspace(0, 1, n)
    track = plot.cy + plot.h * 0.18 * np.sin(u * math.pi * 0.9 + 0.3) - plot.h * 0.12 * u
    growth = float(p.get("growth", 1.0))
    half = 8 + (plot.h * 0.36 * growth) * u**1.1
    reach = at(c.t, 0.05, 1.0, "ease-in-out-cubic") if not c.settled else 1.0
    m = max(2, int(reach * (n - 1)) + 1)
    upper = [(float(xs[i]), float(track[i] - half[i])) for i in range(m)]
    lower = [(float(xs[i]), float(track[i] + half[i])) for i in reversed(range(m))]
    f.polygon(upper + lower, fill=hexa(pal.unknown, 0.16), stroke=hexa(pal.unknown, 0.7), width=2)
    f.polyline([(float(xs[i]), float(track[i])) for i in range(m)], stroke=pal.text, width=3, opacity=0.9)
    labels = p.get("labels") or [f"Day {d}" for d in range(1, days + 1)]
    for d in range(days + 1):
        idx = round(d / days * (n - 1))
        if idx >= m:
            break
        x, y = float(xs[idx]), float(track[idx])
        f.circle(x, y, 9, fill=pal.ground, stroke=pal.text, width=3)
        if d > 0:
            f.text(x, plot.bottom + 70, str(labels[d - 1]), size=28, fill=pal.text_faint, family=MONO, anchor="middle")
    fx, fy = float(xs[m - 1]), float(track[m - 1])
    ang = c.seconds * 2.4
    for arm in range(3):
        a0 = ang + arm * 2 * math.pi / 3
        f.arc(fx, fy, 22, a0, a0 + 1.4, stroke=pal.unknown, width=4)
    f.circle(fx, fy, 6, fill=pal.unknown)


# ------------------------------------------------------------------ ladder


@scene(
    "ladder",
    required=(),
    optional=("rungs", "highlight"),
    demo={
        "heading": "The ladder of causation",
        "rungs": [
            {"title": "Seeing", "question": "What goes with what?"},
            {"title": "Doing", "question": "What if I act?"},
            {"title": "Imagining", "question": "What if it had been different?"},
        ],
        "highlight": 2,
    },
)
def ladder(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Pearl's three rungs, climbed from the bottom; the highlighted rung glows."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    rungs = p.get("rungs") or REGISTRY["ladder"].demo["rungs"]
    n = len(rungs)
    hl = p.get("highlight")
    lx0, lx1 = inner.x + 60, inner.x + 250
    top, bottom = inner.y + 20, inner.bottom - 20
    k0 = at(c.t, 0.0, 0.3) if not c.settled else 1.0
    rail_top = lerp(bottom, top, k0)
    f.line(lx0, bottom, lx0, rail_top, stroke=pal.text_soft, width=6)
    f.line(lx1, bottom, lx1, rail_top, stroke=pal.text_soft, width=6)
    gap = (bottom - top) / n
    for i, rung in enumerate(rungs):
        y = bottom - gap * (i + 0.5)
        k = at(c.t, 0.2 + 0.25 * i, 0.5 + 0.25 * i) if not c.settled else 1.0
        lit = hl == i
        tone = pal.unknown if lit else pal.known
        f.line(lx0, y, lerp(lx0, lx1, k), y, stroke=tone, width=8, opacity=max(k, 0.001))
        card = Box(lx1 + 70, y - gap * 0.4, inner.right - lx1 - 70, gap * 0.8)
        with f.group(opacity=k, dx=(1 - k) * 30):
            f.rect(card, fill=pal.surface, r=18)
            if lit:
                g = pulse(c.seconds, 3.0)
                f.rect(card, stroke=hexa(pal.unknown, 0.5 + 0.4 * g), width=3, r=18)
            f.text(card.x + 40, card.cy - 4, f"{i + 1}", size=30, fill=tone, family=MONO)
            f.text(card.x + 96, card.cy - 4, str(rung["title"]), size=52, fill=pal.text, family=DISPLAY)
            q = rung.get("question")
            if q:
                f.text(card.x + 96, card.cy + 44, str(q), size=30, fill=pal.text_soft)


# ------------------------------------------------------------------ dial


@scene(
    "dial",
    required=("value",),
    optional=("label", "tone", "zones"),
    demo={"heading": "How sure are you?", "value": 70, "label": "confidence"},
)
def dial(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """A half-circle gauge; the needle swings in with a little overshoot and never quite rests."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    tone = role(pal, p.get("tone"), "unknown")
    value = float(p["value"])
    r = min(inner.w * 0.3, inner.h * 0.78)
    cx, cy = inner.cx, inner.y + r + 30
    k0 = at(c.t, 0.0, 0.3) if not c.settled else 1.0
    f.arc(cx, cy, r, math.pi, 2 * math.pi, stroke=pal.surface_2, width=34, opacity=k0)
    zones = p.get("zones")
    if zones:
        for z in zones:
            f.arc(
                cx,
                cy,
                r,
                math.pi + math.pi * float(z["lo"]) / 100,
                math.pi + math.pi * float(z["hi"]) / 100,
                stroke=role(pal, z.get("tone"), "known_soft"),
                width=34,
                opacity=k0,
            )
    k = at(c.t, 0.15, 0.9, "ease-out-back") if not c.settled else 1.0
    v = value * k + 0.6 * math.sin(c.seconds * 3.1) * k0
    a = math.pi + math.pi * clamp(v / 100.0, -0.02, 1.02)
    f.arc(cx, cy, r, math.pi, max(math.pi + 0.001, min(a, 2 * math.pi)), stroke=tone, width=34, opacity=k0)
    for tick in range(0, 101, 10):
        ta = math.pi + math.pi * tick / 100
        r0, r1 = r - 40, r - (58 if tick % 50 == 0 else 50)
        f.line(
            cx + r0 * math.cos(ta),
            cy + r0 * math.sin(ta),
            cx + r1 * math.cos(ta),
            cy + r1 * math.sin(ta),
            stroke=pal.text_faint,
            width=2,
            opacity=k0,
        )
    for tick, anchor in ((0, "middle"), (50, "middle"), (100, "middle")):
        ta = math.pi + math.pi * tick / 100
        rr = r + 58
        f.text(
            cx + rr * math.cos(ta),
            cy + rr * math.sin(ta) + 10,
            f"{tick}",
            size=26,
            fill=pal.text_faint,
            family=MONO,
            anchor=anchor,
            alpha=k0,
        )
    nl = r - 70
    f.line(cx, cy, cx + nl * math.cos(a), cy + nl * math.sin(a), stroke=pal.text, width=6, opacity=k0)
    f.circle(cx, cy, 18, fill=pal.text, opacity=k0)
    f.circle(cx, cy, 8, fill=tone, opacity=k0)
    f.text(cx, cy - r * 0.34, f"{round(value * k)}%", size=84, fill=pal.text, family=MONO, anchor="middle", alpha=k0)
    label = p.get("label")
    if label:
        f.text(cx, cy + 64, str(label), size=32, fill=pal.text_soft, anchor="middle", alpha=k0)


# ------------------------------------------------------------------ distribution


def _density(x: np.ndarray, mean: float, sd: float, skew: float) -> np.ndarray:
    z = (x - mean) / sd
    pdf = np.exp(-0.5 * z * z)
    cdf = 0.5 * (1 + np.tanh(0.7978845608 * (skew * z + 0.044715 * (skew * z) ** 3)))
    return pdf * (2 * cdf if skew else 1.0)


@scene(
    "distribution",
    required=("mean", "sd"),
    optional=("skew", "interval", "to", "x_label", "domain", "tone", "interval_label"),
    demo={
        "heading": "A forecast is a spread",
        "mean": 50,
        "sd": 10,
        "interval": [35, 65],
        "to": {"mean": 55, "sd": 16},
        "x_label": "outcome",
        "interval_label": "90% interval",
    },
)
def distribution(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """A density drawn left to right, an interval shaded, then an optional widen or shift."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    tone = role(pal, p.get("tone"), "known")
    lo_d, hi_d = p.get("domain", [0, 100])
    plot = Box(inner.x + 40, inner.y + 20, inner.w - 80, inner.h - 100)
    xs = np.linspace(float(lo_d), float(hi_d), 220)
    morph = c.beat(2, dur=1.4, name="ease-in-out-cubic", spacing=1.6) if p.get("to") else 0.0
    to = p.get("to") or {}
    mean = lerp(float(p["mean"]), float(to.get("mean", p["mean"])), morph)
    sd = lerp(float(p["sd"]), float(to.get("sd", p["sd"])), morph)
    skew = lerp(float(p.get("skew", 0)), float(to.get("skew", p.get("skew", 0))), morph)
    dens = _density(xs, mean, sd, skew)
    ref = _density(xs, float(p["mean"]), float(p["sd"]), float(p.get("skew", 0))).max()
    ys = plot.bottom - dens / ref * plot.h * 0.92 * (float(p["sd"]) / sd) ** 0.0
    ys = np.maximum(ys, plot.y)
    X = plot.x + (xs - float(lo_d)) / (float(hi_d) - float(lo_d)) * plot.w
    k0 = at(c.t, 0.0, 0.2) if not c.settled else 1.0
    f.line(plot.x, plot.bottom, plot.right, plot.bottom, stroke=pal.line, width=2, opacity=k0)
    reach = at(c.t, 0.05, 0.7, "ease-in-out-cubic") if not c.settled else 1.0
    m = max(2, int(reach * len(xs)))
    interval = p.get("interval")
    if interval:
        ki = c.beat(1, dur=0.9, spacing=1.6)
        ilo, ihi = float(interval[0]), float(interval[1])
        if to:
            w0 = (ihi - ilo) / 2
            scale = sd / float(p["sd"])
            ilo, ihi = mean - w0 * scale, mean + w0 * scale
        sel = (xs >= ilo) & (xs <= ihi)
        idx = np.nonzero(sel)[0]
        if idx.size > 1 and ki > 0:
            pts = [(float(X[i]), float(ys[i])) for i in idx] + [
                (float(X[idx[-1]]), plot.bottom),
                (float(X[idx[0]]), plot.bottom),
            ]
            f.polygon(pts, fill=hexa(tone, 0.28), opacity=ki)
            f.line(float(X[idx[0]]), plot.bottom, float(X[idx[0]]), float(ys[idx[0]]), stroke=tone, width=2, opacity=ki)
            f.line(
                float(X[idx[-1]]), plot.bottom, float(X[idx[-1]]), float(ys[idx[-1]]), stroke=tone, width=2, opacity=ki
            )
            il = p.get("interval_label")
            if il:
                f.text(
                    float((X[idx[0]] + X[idx[-1]]) / 2),
                    plot.bottom + 64,
                    str(il),
                    size=28,
                    fill=tone,
                    anchor="middle",
                    alpha=ki,
                )
    f.polyline([(float(X[i]), float(ys[i])) for i in range(m)], stroke=pal.text, width=4)
    mx = plot.x + (mean - float(lo_d)) / (float(hi_d) - float(lo_d)) * plot.w
    peak = float(ys[int(np.argmin(ys))])
    g = pulse(c.seconds, 2.8)
    f.line(
        mx, plot.bottom, mx, peak, stroke=hexa(pal.unknown, 0.55 + 0.35 * g), width=2, dash=[8, 8], opacity=k0 * reach
    )
    xl = p.get("x_label")
    if xl:
        f.text(plot.right, plot.bottom + 64, str(xl), size=28, fill=pal.text_faint, anchor="end", alpha=k0)


# ------------------------------------------------------------------ histogram_of_answers


@scene(
    "histogram_of_answers",
    required=("phrase",),
    optional=("answers", "n", "mean", "sd", "seed", "bin", "note"),
    demo={"phrase": "probably", "n": 120, "mean": 68, "sd": 12, "seed": 2, "note": "What number do people mean?"},
)
def histogram_of_answers(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Many readers' numbers for one phrase, falling as dots into 5-point bins."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    if p.get("answers"):
        vals = np.clip(np.asarray(p["answers"], dtype=float), 0, 100)
    else:
        g = rng(int(p.get("seed", 2)))
        vals = np.clip(g.normal(float(p.get("mean", 60)), float(p.get("sd", 12)), int(p.get("n", 100))), 0, 99.9)
    width = float(p.get("bin", 5))
    bins = np.floor(vals / width).astype(int)
    order = np.argsort(rng(9).random(vals.size))
    title_h = 110
    phrase = f"“{p['phrase']}”"
    k0 = at(c.t, 0.0, 0.25) if not c.settled else 1.0
    f.text(inner.x, inner.y + 70, phrase, size=72, fill=pal.text, family=DISPLAY, alpha=k0)
    note = p.get("note")
    if note:
        f.text(inner.right, inner.y + 64, str(note), size=32, fill=pal.text_soft, anchor="end", alpha=k0)
    plot = Box(inner.x + 44, inner.y + title_h + 10, inner.w - 88, inner.h - title_h - 90)
    nb = math.ceil(100 / width)
    colw = plot.w / nb
    counts = np.bincount(bins, minlength=nb)
    r = min(colw * 0.42, plot.h / (2.05 * max(1, counts.max())))
    f.line(plot.x, plot.bottom + 4, plot.right, plot.bottom + 4, stroke=pal.line, width=2, opacity=k0)
    for v in (0, 25, 50, 75, 100):
        x = plot.x + v / 100 * plot.w
        f.text(x, plot.bottom + 56, f"{v}%", size=26, fill=pal.text_faint, family=MONO, anchor="middle", alpha=k0)
    fill = at(c.t, 0.1, 1.0, "linear") if not c.settled else 1.0
    height = np.zeros(nb, dtype=int)
    shown = round(fill * vals.size)
    mode = int(np.argmax(counts))
    for rank, idx in enumerate(order):
        b = int(bins[idx])
        slot = height[b]
        height[b] += 1
        if rank >= shown + 4:
            continue
        local = clamp((fill * vals.size - rank) / 4.0) if not c.settled else 1.0
        x = plot.x + (b + 0.5) * colw
        y_end = plot.bottom - r - slot * 2.05 * r
        y = lerp(plot.y - 20, y_end, ease(local, "ease-in-cubic") if local < 1 else 1.0)
        tone = pal.unknown if b == mode else pal.known
        f.circle(x, y, r * 0.92, fill=tone, opacity=clamp(local * 3))
    if fill >= 1.0:
        g = pulse(c.seconds, 2.6)
        top = plot.bottom - counts[mode] * 2.05 * r - 18
        x = plot.x + (mode + 0.5) * colw
        f.line(x - colw * 0.4, top, x + colw * 0.4, top, stroke=pal.unknown, width=3, opacity=0.5 + 0.5 * g)


# ------------------------------------------------------------------ quote_card


@scene(
    "quote_card",
    required=("text", "who"),
    optional=("when", "source"),
    demo={
        "text": "Uncertainty must be taken in a sense radically distinct from the familiar notion of risk.",
        "who": "Frank Knight",
        "when": "1921",
    },
)
def quote_card(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """An attributed quotation, its words arriving in reading order."""
    pal = f.pal
    text = str(p["text"])
    inner = box.inset(80, 20)
    size = 62.0
    while size > 38:
        lines = f.wrap(text, size, inner.w - 120, DISPLAY)
        if len(lines) * size * 1.28 < inner.h - 170:
            break
        size -= 2
    lines = f.wrap(text, size, inner.w - 120, DISPLAY)
    block = len(lines) * size * 1.28
    top = inner.cy - (block + 110) / 2
    k0 = at(c.t, 0.0, 0.3) if not c.settled else 1.0
    g = pulse(c.seconds, 4.0)
    f.text(inner.x, top + 90, "“", size=200, fill=pal.unknown, family=DISPLAY, alpha=k0 * (0.75 + 0.25 * g))
    words_total = sum(len(line.split()) for line in lines)
    wi = 0
    speed = at(c.t, 0.1, 0.9, "linear") if not c.settled else 1.0
    for li, line in enumerate(lines):
        x = inner.x + 120
        y = top + size + li * size * 1.28
        for word in line.split():
            kw = clamp((speed * (words_total + 3) - wi) / 3.0) if not c.settled else 1.0
            f.text(x, y + (1 - kw) * 8, word, size=size, fill=pal.text, family=DISPLAY, alpha=kw)
            x += f.measure(word + " ", size, DISPLAY)
            wi += 1
    ka = at(c.t, 0.7, 1.0) if not c.settled else 1.0
    attrib = str(p["who"]).upper() + (f"  ·  {p['when']}" if p.get("when") else "")
    ay = top + block + 80
    f.line(inner.x + 120, ay - 10, inner.x + 120 + 60 * ka, ay - 10, stroke=pal.unknown, width=3, opacity=ka)
    tracked(f, inner.x + 200, ay, attrib, size=24, fill=pal.text_soft, alpha=ka)


# ------------------------------------------------------------------ icon_grid


@scene(
    "icon_grid",
    required=("items",),
    optional=("columns",),
    demo={
        "heading": "Where forecasts go wrong",
        "items": [{"label": "Weather"}, {"label": "Markets"}, {"label": "Elections"}, {"label": "Medicine"}],
    },
)
def icon_grid(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Generated icons on cards, arriving one after another and floating gently."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    items = list(p["items"])
    n = len(items)
    cols = int(p.get("columns", min(4, n)))
    rows = math.ceil(n / cols)
    gap = 40
    cw = (inner.w - gap * (cols - 1)) / cols
    ch = min((inner.h - gap * (rows - 1)) / rows, cw * 1.05)
    y0 = inner.y + (inner.h - (ch * rows + gap * (rows - 1))) / 2
    for i, item in enumerate(items):
        r_, c_ = divmod(i, cols)
        card = Box(inner.x + c_ * (cw + gap), y0 + r_ * (ch + gap), cw, ch)
        k = at(c.t, 0.08 + 0.7 * i / max(1, n), 0.38 + 0.7 * i / max(1, n), "ease-out-cubic") if not c.settled else 1.0
        if k <= 0:
            continue
        bob = 5 * math.sin(c.seconds * 1.1 + i * 1.3)
        with f.group(opacity=k, dy=(1 - k) * 30):
            f.rect(card, fill=pal.surface, r=24)
            label = item.get("label")
            if label:
                f.text(card.cx, card.bottom - 44, str(label), size=34, fill=pal.text, anchor="middle", weight=500)
        img = ctx.image(item.get("image"))
        s = 0.8 + 0.2 * ease(k, "ease-out-back")
        side = min(card.w, card.h - 90) * 0.72 * s
        ibox = Box(card.cx - side / 2, card.y + (card.h - 90 - side) / 2 + 10 + bob * k, side, side)
        if img is not None:
            f.image(img, ibox, opacity=k)
        else:
            f.circle(ibox.cx, ibox.cy, side * 0.34, fill=pal.known_soft, opacity=k)
            f.circle(ibox.cx, ibox.cy, side * 0.16, fill=pal.known, opacity=k)


# ------------------------------------------------------------------ timeline_strip


@scene(
    "timeline_strip",
    required=("events",),
    optional=("highlight", "span"),
    demo={
        "heading": "A short history of the odds",
        "events": [
            {"year": 1654, "label": "Pascal and Fermat"},
            {"year": 1713, "label": "Bernoulli"},
            {"year": 1921, "label": "Knight"},
            {"year": 1961, "label": "Ellsberg"},
            {"year": 2015, "label": "ICD 203"},
        ],
        "highlight": 2,
    },
)
def timeline_strip(f: Frame, box: Box, p: dict[str, Any], c: Clock, ctx: Ctx) -> None:
    """Dated events on a line drawn left to right, labels alternating above and below."""
    pal = f.pal
    inner = header_block(f, box, p, c)
    ev = sorted(p["events"], key=lambda e: float(e["year"]))
    span = p.get("span") or [float(ev[0]["year"]), float(ev[-1]["year"])]
    lo, hi = float(span[0]), float(span[1])
    x0, x1 = inner.x + 80, inner.right - 80
    y = inner.cy + 10
    reach = at(c.t, 0.0, 0.8, "ease-in-out-cubic") if not c.settled else 1.0
    f.line(x0 - 40, y, lerp(x0 - 40, x1 + 40, reach), y, stroke=pal.line, width=3)
    hl = p.get("highlight")
    for i, e in enumerate(ev):
        frac = (float(e["year"]) - lo) / max(1e-6, hi - lo)
        x = lerp(x0, x1, frac)
        k = clamp((reach * 1.08 - frac) / 0.12) if not c.settled else 1.0
        if k <= 0:
            continue
        lit = hl == i
        tone = pal.unknown if lit else pal.known
        up = i % 2 == 0
        stem = 70
        ky = ease(k, "ease-out-back")
        f.line(x, y, x, y + (-stem if up else stem) * ky, stroke=hexa(tone, 0.6), width=2)
        if lit:
            g = pulse(c.seconds, 2.4)
            f.circle(x, y, 20 + 8 * g, fill=tone, opacity=0.2 * k)
        f.circle(x, y, 11 * ky, fill=tone)
        ty = y - stem - 26 if up else y + stem + 50
        with f.group(opacity=k):
            f.text(
                x, ty - (38 if up else 0), str(int(float(e["year"]))), size=30, fill=tone, family=MONO, anchor="middle"
            )
            label = str(e.get("label", ""))
            size = f.fit(label, (x1 - x0) / max(1, len(ev) - 1) * 1.6, 32, 22)
            half = f.measure(label, size) / 2
            lx = clamp(x, inner.x + half, inner.right - half)
            f.text(lx, ty + (0 if up else 40), label, size=size, fill=pal.text, anchor="middle")
from . import scenes_01_two_kinds_of_not_knowing  # noqa: E402,F401  (video 1 scenes)
