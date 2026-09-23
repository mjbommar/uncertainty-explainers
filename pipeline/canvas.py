"""Drawing primitives for one frame: vector layers from ``bc_viz``, images through ``bc_image``.

A :class:`Frame` is an ordered list of layers in a 1920x1080 logical space.
A vector layer is a ``bc_viz.Canvas`` (retained geometry, deterministic SVG,
rasterised by ``resvg`` with only the brand's font files loaded); an image
layer is an RGBA array placed in a box. :meth:`Frame.render` rasterises each
vector layer at the output size (the SVG scales, so 4K costs nothing in
drawing code) and composites every layer over the ground with
``bc_image.over``. Groups give whole-layer opacity, translation and clipping,
which is how scenes fade and slide as a unit.

Motion helpers wrap ``bc_motion.easing`` so every curve in a video comes from
one definition.
"""

from __future__ import annotations

import math
from collections.abc import Iterator, Sequence
from contextlib import contextmanager
from functools import lru_cache

import bc_image as bi
import numpy as np
from bc_motion import easing as E
from bc_viz import Canvas, Group, PathBuilder, Scene

from . import brand
from .brand import Box, Palette

__all__ = [
    "Frame",
    "at",
    "clamp",
    "ease",
    "ground",
    "hexa",
    "ink_bbox",
    "lerp",
    "mix_hex",
    "pulse",
]


# ------------------------------------------------------------------ motion


def clamp(t: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return lo if t < lo else hi if t > hi else t


def ease(t: float, name: str = "ease-out-cubic") -> float:
    return float(E.ease(name, clamp(t)))


def at(t: float, start: float, end: float, name: str = "ease-out-cubic") -> float:
    """``t`` mapped through ``[start, end]`` and eased: the workhorse for staged reveals."""
    return float(E.at(name, t, start, end))


def pulse(seconds: float, period: float = 2.4) -> float:
    """0..1 sine breathing on absolute time; ambient motion that never stops."""
    return float(E.pulse(seconds, period))


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


# ------------------------------------------------------------------ colour


def hexa(color: str, alpha: float = 1.0) -> str:
    """``#rrggbb`` with an alpha byte: how text and strokes fade inside one layer."""
    c = color.lstrip("#")[:6]
    a = round(clamp(alpha) * 255)
    return f"#{c}{a:02x}"


def mix_hex(a: str, b: str, t: float) -> str:
    """Interpolate two colours in Lab (``bc_viz.interpolate``)."""
    from bc_viz import Rgb, interpolate

    return interpolate(Rgb.from_hex(a[:7]), Rgb.from_hex(b[:7]), clamp(t), "lab").to_hex()


# ------------------------------------------------------------------ ground


@lru_cache(maxsize=8)
def ground(theme: str, width: int, height: int) -> np.ndarray:
    """The frame's floor: a vertical fall-off, a soft vignette, and a fixed 1-LSB dither.

    A dark gradient bands visibly in 8-bit 4:2:0; the dither is seeded, so every
    frame carries the same grain and the encoder sees it as static texture.
    """
    pal = brand.palette(theme)
    top = np.array(pal.rgb("ground"), dtype=np.float32)
    edge = np.array(pal.rgb("ground_edge"), dtype=np.float32)
    ramp = (np.linspace(0.0, 1.0, height, dtype=np.float32) ** 1.8)[:, None, None]
    base = top[None, None, :] * (1 - 0.35 * ramp) + edge[None, None, :] * (0.35 * ramp)
    base = np.ascontiguousarray(np.broadcast_to(base, (height, width, 3)), dtype=np.float32)
    edge_frame = np.ascontiguousarray(np.broadcast_to(edge[None, None, :], (height, width, 3)), dtype=np.float32)
    # radial_ramp is 1 inside a growing circle; its inverse is the vignette.
    inside = bi.radial_ramp(width, height, 0.78, (0.5, 0.46), 0.55)
    vignette = np.ascontiguousarray((1.0 - inside) * 0.85, dtype=np.float32)
    frame = bi.blend(base, edge_frame, vignette)
    rng = np.random.default_rng(1921)
    grain = rng.uniform(-0.6 / 255, 0.6 / 255, size=(height, width, 1)).astype(np.float32)
    return bi.to_u8(np.ascontiguousarray(np.clip(frame + grain, 0, 1), dtype=np.float32))


# ------------------------------------------------------------------ frame


class Frame:
    """One frame under construction, in logical 1920x1080 pixels."""

    def __init__(self, pal: Palette, *, width: int = brand.WIDTH, height: int = brand.HEIGHT):
        self.pal = pal
        self.width = width
        self.height = height
        self.layers: list[tuple] = []
        self._stack: list[Canvas | Group] = []
        self._new_vector()

    # ----------------------------------------------------------- layers

    def _new_vector(self) -> None:
        canvas = Canvas(self.width, self.height)
        self.layers.append(("svg", canvas))
        self._stack = [canvas]

    @property
    def _c(self) -> Canvas | Group:
        return self._stack[-1]

    @contextmanager
    def group(
        self,
        *,
        opacity: float = 1.0,
        dx: float = 0.0,
        dy: float = 0.0,
        clip: Box | None = None,
    ) -> Iterator[None]:
        """Draw a set of items as one layer: faded, moved, clipped together."""
        g = Group(
            opacity=clamp(opacity),
            dx=dx,
            dy=dy,
            clip=(clip.x, clip.y, clip.w, clip.h) if clip else None,
        )
        parent = self._c
        self._stack.append(g)
        try:
            yield
        finally:
            self._stack.pop()
            if opacity > 0.002 and len(g):
                parent.group(g)

    def image(self, rgba: np.ndarray, box: Box, *, opacity: float = 1.0, fit: str = "contain") -> None:
        """Place an RGBA uint8 image in ``box`` (aspect kept), above what is drawn so far."""
        if opacity <= 0.002 or box.w < 1 or box.h < 1:
            return
        h, w = rgba.shape[:2]
        s = min(box.w / w, box.h / h) if fit == "contain" else max(box.w / w, box.h / h)
        dw, dh = w * s, h * s
        placed = Box(box.cx - dw / 2, box.cy - dh / 2, dw, dh)
        self.layers.append(("img", rgba, placed, clamp(opacity)))
        self._new_vector()

    # ----------------------------------------------------------- shapes

    def rect(
        self,
        b: Box,
        *,
        fill: str | None = None,
        stroke: str | None = None,
        width: float = 1.0,
        r: float = 0.0,
        opacity: float = 1.0,
        dash: list[float] | None = None,
    ) -> None:
        self._c.rect(
            b.x, b.y, b.w, b.h, rx=r, fill=fill, stroke=stroke, stroke_width=width, opacity=clamp(opacity), dash=dash
        )

    def line(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        *,
        stroke: str,
        width: float = 2.0,
        opacity: float = 1.0,
        cap: str = "round",
        dash: list[float] | None = None,
    ) -> None:
        self._c.line(x1, y1, x2, y2, stroke=stroke, stroke_width=width, linecap=cap, opacity=clamp(opacity), dash=dash)

    def polyline(
        self,
        pts: Sequence[tuple[float, float]],
        *,
        stroke: str,
        width: float = 2.0,
        opacity: float = 1.0,
        cap: str = "round",
    ) -> None:
        if len(pts) >= 2:
            self._c.polyline(list(pts), stroke=stroke, stroke_width=width, linecap=cap, opacity=clamp(opacity))

    def polygon(
        self,
        pts: Sequence[tuple[float, float]],
        *,
        fill: str | None = None,
        stroke: str | None = None,
        width: float = 1.0,
        opacity: float = 1.0,
    ) -> None:
        if len(pts) >= 3:
            self._c.polygon(list(pts), fill=fill, stroke=stroke, stroke_width=width, opacity=clamp(opacity))

    def circle(
        self,
        cx: float,
        cy: float,
        r: float,
        *,
        fill: str | None = None,
        stroke: str | None = None,
        width: float = 1.0,
        opacity: float = 1.0,
    ) -> None:
        if r > 0.05:
            self._c.circle(cx, cy, r, fill=fill, stroke=stroke, stroke_width=width, opacity=clamp(opacity))

    def path(
        self,
        p: PathBuilder,
        *,
        fill: str | None = None,
        stroke: str | None = None,
        width: float = 2.0,
        opacity: float = 1.0,
        cap: str = "round",
    ) -> None:
        self._c.path(p, fill=fill, stroke=stroke, stroke_width=width, linecap=cap, opacity=clamp(opacity))

    def arc(
        self,
        cx: float,
        cy: float,
        r: float,
        a0: float,
        a1: float,
        *,
        stroke: str,
        width: float = 2.0,
        opacity: float = 1.0,
        steps: int = 64,
    ) -> None:
        """An arc from angle ``a0`` to ``a1`` (radians, 0 = east, clockwise on screen)."""
        if abs(a1 - a0) < 1e-4:
            return
        n = max(2, int(steps * abs(a1 - a0) / math.pi) + 2)
        pts = [
            (cx + r * math.cos(a0 + (a1 - a0) * i / (n - 1)), cy + r * math.sin(a0 + (a1 - a0) * i / (n - 1)))
            for i in range(n)
        ]
        self.polyline(pts, stroke=stroke, width=width, opacity=opacity)

    # ------------------------------------------------------------- text

    def measure(self, text: str, size: float, family: str = brand.TEXT, weight: int = 400) -> float:
        return float(brand.metrics(family, weight).width(text, size))

    def wrap(self, text: str, size: float, max_width: float, family: str = brand.TEXT, weight: int = 400) -> list[str]:
        return list(brand.metrics(family, weight).wrap(text, size, max_width))

    def fit(
        self, text: str, width: float, preferred: float, minimum: float, family: str = brand.TEXT, weight: int = 400
    ) -> float:
        return float(brand.metrics(family, weight).fit_size(text, width, preferred, minimum))

    def text(
        self,
        x: float,
        y: float,
        s: str,
        *,
        size: float,
        fill: str,
        family: str = brand.TEXT,
        weight: int = 400,
        anchor: str = "start",
        alpha: float = 1.0,
    ) -> None:
        """One line; ``y`` is the baseline. ``alpha`` fades it within its layer."""
        if not s or alpha <= 0.002:
            return
        self._c.text(
            x,
            y,
            s,
            size=size,
            family=family,
            weight=weight,
            fill=hexa(fill, alpha),
            anchor=anchor,
            metrics=brand.metrics(family, weight),
        )

    def text_lines(
        self, x: float, y: float, lines: Sequence[str], *, size: float, fill: str, leading: float = 1.25, **kw
    ) -> float:
        """Stacked lines from a first baseline; returns the last baseline."""
        for i, line in enumerate(lines):
            self.text(x, y + i * size * leading, line, size=size, fill=fill, **kw)
        return y + (len(lines) - 1) * size * leading

    # ----------------------------------------------------------- render

    def render(self, base: np.ndarray, scale: float = 1.0) -> np.ndarray:
        """Composite every layer over ``base`` (uint8 ``(H, W, 3)`` at output size)."""
        out = np.ascontiguousarray(base)
        oh, ow = out.shape[:2]
        for layer in self.layers:
            if layer[0] == "svg":
                canvas = layer[1]
                if len(canvas) == 0:
                    continue
                rgba = Scene.parse(canvas.to_svg(), list(brand.FONT_PATHS)).render(ow, oh)
                out = bi.over(out, rgba)
            else:
                _, rgba, box, opacity = layer
                out = _place(out, rgba, box, opacity, scale)
        return out

    def render_rgba(self, scale: float = 1.0) -> np.ndarray:
        """The frame over nothing, as straight RGBA: what containment tests measure."""
        w, h = round(self.width * scale), round(self.height * scale)
        acc_rgb = np.zeros((h, w, 3), dtype=np.float32)
        acc_a = np.zeros((h, w), dtype=np.float32)
        for layer in self.layers:
            if layer[0] == "svg":
                if len(layer[1]) == 0:
                    continue
                rgba = Scene.parse(layer[1].to_svg(), list(brand.FONT_PATHS)).render(w, h)
            else:
                _, img, box, opacity = layer
                rgba = np.zeros((h, w, 4), dtype=np.uint8)
                _place_rgba(rgba, img, box, opacity, scale)
            a = rgba[..., 3].astype(np.float32) / 255.0
            acc_rgb = acc_rgb * (1 - a[..., None]) + rgba[..., :3].astype(np.float32) / 255 * a[..., None]
            acc_a = acc_a + a * (1 - acc_a)
        return np.dstack([np.clip(acc_rgb * 255, 0, 255), np.clip(acc_a * 255, 0, 255)]).astype(np.uint8)


@lru_cache(maxsize=256)
def _resized(key: int, w: int, h: int) -> np.ndarray:
    rgba = _IMAGES[key]
    rgb = bi.resize(np.ascontiguousarray(rgba[..., :3]), w, h)
    alpha = bi.resize(np.ascontiguousarray(np.repeat(rgba[..., 3:4], 3, axis=2)), w, h)[..., 0]
    return np.dstack([bi.to_u8(rgb), bi.to_u8(np.ascontiguousarray(np.repeat(alpha[..., None], 3, axis=2)))[..., 0]])


_IMAGES: dict[int, np.ndarray] = {}


def _scaled(rgba: np.ndarray, w: int, h: int) -> np.ndarray:
    key = id(rgba)
    _IMAGES[key] = rgba
    return _resized(key, w, h)


def _place_rgba(dest: np.ndarray, rgba: np.ndarray, box: Box, opacity: float, scale: float) -> None:
    w, h = max(1, round(box.w * scale)), max(1, round(box.h * scale))
    x, y = round(box.x * scale), round(box.y * scale)
    img = _scaled(rgba, w, h)
    x0, y0, x1, y1 = max(0, x), max(0, y), min(dest.shape[1], x + w), min(dest.shape[0], y + h)
    if x1 <= x0 or y1 <= y0:
        return
    crop = img[y0 - y : y1 - y, x0 - x : x1 - x].copy()
    crop[..., 3] = (crop[..., 3].astype(np.float32) * opacity).astype(np.uint8)
    dest[y0:y1, x0:x1] = crop


def _place(out: np.ndarray, rgba: np.ndarray, box: Box, opacity: float, scale: float) -> np.ndarray:
    w, h = max(1, round(box.w * scale)), max(1, round(box.h * scale))
    x, y = round(box.x * scale), round(box.y * scale)
    img = _scaled(rgba, w, h)
    x0, y0, x1, y1 = max(0, x), max(0, y), min(out.shape[1], x + w), min(out.shape[0], y + h)
    if x1 <= x0 or y1 <= y0:
        return out
    out = out.copy() if not out.flags.writeable else out
    region = np.ascontiguousarray(out[y0:y1, x0:x1])
    layer = np.ascontiguousarray(img[y0 - y : y1 - y, x0 - x : x1 - x])
    out[y0:y1, x0:x1] = bi.over(region, layer, opacity)
    return out


def ink_bbox(rgba: np.ndarray, threshold: int = 8, scale: float = 1.0) -> Box | None:
    """The logical-pixel box around every pixel with alpha above ``threshold``."""
    ys, xs = np.nonzero(rgba[..., 3] > threshold)
    if xs.size == 0:
        return None
    return Box(xs.min() / scale, ys.min() / scale, (xs.max() + 1 - xs.min()) / scale, (ys.max() + 1 - ys.min()) / scale)
