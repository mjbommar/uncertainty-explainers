"""Contact sheets for long videos: taller than the rasteriser's 16384-pixel side limit."""

from __future__ import annotations

import bc_image as bi
import numpy as np

from pipeline.sheet import contact_sheet


def test_contact_sheet_taller_than_raster_limit(tmp_path) -> None:
    frames = [np.full((108, 192, 3), 40 + (i % 50), dtype=np.uint8) for i in range(240)]
    labels = [f"frame {i}" for i in range(240)]
    dest = contact_sheet(frames, labels, tmp_path / "tall.png", title="tall")
    img = np.asarray(bi.load(dest))
    assert img.shape[0] > 16384
    # The caption strip under the last row carries text, not flat background.
    assert img[-40:-10, :200].std() > 0
