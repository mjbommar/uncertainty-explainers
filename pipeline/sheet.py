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
    h0, w0 = frames[0].shape[:2]
    tw, th = tile_width, round(tile_width * h0 / w0)
    cap = 34
    pad = 12
    head = 56 if title else 0
    rows = -(-len(frames) // columns)
    W = columns * (tw + pad) + pad
    H = head + rows * (th + cap + pad) + pad
    sheet = np.full((H, W, 3), 26, dtype=np.uint8)
    canvas = Canvas(W, H)
    if title:
        canvas.text(pad, 38, title, size=26, family=brand.TEXT, weight=600, fill="#e8e2d6")
    for i, (frame, label) in enumerate(zip(frames, labels, strict=True)):
        r, c = divmod(i, columns)
        x = pad + c * (tw + pad)
        y = head + pad + r * (th + cap + pad)
        tile = bi.to_u8(bi.resize(np.ascontiguousarray(frame), tw, th))
        sheet[y : y + th, x : x + tw] = tile
        canvas.text(x + 4, y + th + 24, label[:70], size=17, family=brand.TEXT, fill="#c9c3b8")
    rgba = Scene.parse(canvas.to_svg(), list(brand.FONT_PATHS)).render(W, H)
    out = bi.over(sheet, rgba)
    dest.parent.mkdir(parents=True, exist_ok=True)
    bi.save(out, dest)
    return dest
