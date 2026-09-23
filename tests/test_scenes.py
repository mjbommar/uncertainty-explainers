"""Every scene stays inside the box it is handed, at every reveal point, on both grounds."""

from __future__ import annotations

import numpy as np
import pytest

from pipeline import brand, scenes
from pipeline.canvas import Frame, ink_bbox

POINTS = (0.0, 0.15, 0.4, 0.7, 1.0)
ICON = np.zeros((64, 64, 4), dtype=np.uint8)
ICON[8:56, 8:56] = (108, 192, 176, 255)


@pytest.mark.parametrize("theme", ["ink", "paper"])
@pytest.mark.parametrize("name", sorted(scenes.REGISTRY))
def test_scene_stays_in_its_box(name: str, theme: str) -> None:
    demo = dict(scenes.REGISTRY[name].demo)
    if name == "icon_grid":
        demo["items"] = [{**it, "image": "image:icon"} for it in demo["items"]]
    for t in POINTS:
        f = Frame(brand.palette(theme))
        clock = scenes.Clock(t=t, local=t * 3.2, seconds=7.0 + t, settled=t >= 1.0)
        scenes.draw(f, name, demo, brand.STAGE, clock, scenes.Ctx(images={"icon": ICON}))
        box = ink_bbox(f.render_rgba())
        if box is None:
            continue
        assert brand.STAGE.contains(box, slack=2.0), f"{name} at t={t}: ink {box} outside {brand.STAGE}"


@pytest.mark.parametrize("name", sorted(scenes.REGISTRY))
def test_settled_scene_still_moves(name: str) -> None:
    """Ambient motion: two settled frames a second apart are not identical."""
    frames = []
    for s in (20.0, 21.0):
        f = Frame(brand.palette("ink"))
        clock = scenes.Clock(t=1.0, local=s, seconds=s, settled=True)
        scenes.draw(f, name, scenes.REGISTRY[name].demo, brand.STAGE, clock, scenes.Ctx())
        frames.append(f.render_rgba())
    assert not np.array_equal(frames[0], frames[1]), f"{name} freezes once settled"


def test_every_scene_has_a_demo_with_its_required_params() -> None:
    for name, sd in scenes.REGISTRY.items():
        missing = [k for k in sd.required if k not in sd.demo]
        assert not missing, f"{name} demo lacks {missing}"
