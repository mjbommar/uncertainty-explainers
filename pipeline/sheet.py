"""Contact sheets: labelled grids of frames for review (gallery, cut inspection)."""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

import bc_image as bi
import numpy as np
from bc_viz import Canvas, Scene

from . import brand

__all__ = ["contact_sheet"]


def contact_sheet(
    frames: Sequence[np.ndarray],
    labels: Sequence[str],
    dest: Path,
    *,
    columns: int = 4,
    tile_width: int = 480,
    title: str = "",
) -> Path:
    """Tile ``frames`` (uint8 or float32 ``(h, w, 3)``) with a caption strip under each."""
    if not frames:
        raise ValueError("a contact sheet needs at least one frame")
    if len(labels) != len(frames):
        raise ValueError("one label per frame")
    h0, w0 = frames[0].shape[:2]
    tw, th = tile_width, round(tile_width * h0 / w0)
    cap = 34
    pad = 12
    head = 56 if title else 0
    rows = -(-len(frames) // columns)
    W = columns * (tw + pad) + pad
    H = head + rows * (th + cap + pad) + pad
    sheet = np.full((H, W, 3), 26, dtype=np.uint8)
    # Text is rasterised one strip at a time: a single canvas the height of a
    # long video's sheet exceeds the rasteriser's 16384-pixel side limit.
    fonts = list(brand.FONT_PATHS)

    def strip(y0: int, h: int, draw) -> None:
        canvas = Canvas(W, h)
        draw(canvas)
        rgba = Scene.parse(canvas.to_svg(), fonts).render(W, h)
        sheet[y0 : y0 + h] = bi.to_u8(bi.over(sheet[y0 : y0 + h], rgba))

    if title:
        strip(0, head, lambda cv: cv.text(pad, 38, title, size=26, family=brand.TEXT, weight=600, fill="#e8e2d6"))
    for i, frame in enumerate(frames):
        r, c = divmod(i, columns)
        x = pad + c * (tw + pad)
        y = head + pad + r * (th + cap + pad)
        sheet[y : y + th, x : x + tw] = bi.to_u8(bi.resize(np.ascontiguousarray(frame), tw, th))
    for r in range(rows):
        y = head + pad + r * (th + cap + pad) + th
        row = [(i, lab) for i, lab in enumerate(labels) if i // columns == r]

        def draw(cv, row=row) -> None:
            for i, label in row:
                x = pad + (i % columns) * (tw + pad)
                cv.text(x + 4, 24, label[:70], size=17, family=brand.TEXT, fill="#c9c3b8")

        strip(y, cap, draw)
    out = sheet
    dest.parent.mkdir(parents=True, exist_ok=True)
    bi.save(out, dest)
    return dest
