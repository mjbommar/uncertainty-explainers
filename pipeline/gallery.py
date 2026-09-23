"""Every scene at four reveal points, on both grounds, as one contact sheet each.

``uv run python -m pipeline.gallery [--theme ink|paper] [--scene NAME]`` writes
``build/gallery/<theme>.png`` and, per scene, ``build/gallery/<theme>/<scene>.png``
at full size for close inspection.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np

from . import ROOT, brand, scenes
from .canvas import Frame, ground
from .sheet import contact_sheet

REVEAL = (0.15, 0.4, 0.7, 1.0)
REVEAL_SECONDS = 3.2


def still(
    name: str,
    params: dict,
    t: float,
    theme: str,
    *,
    seconds: float | None = None,
    images: dict[str, np.ndarray] | None = None,
) -> np.ndarray:
    """One scene at reveal ``t`` on the full ground, as a uint8 frame."""
    pal = brand.palette(theme)
    f = Frame(pal)
    local = t * REVEAL_SECONDS
    clock = scenes.Clock(
        t=t,
        local=local,
        seconds=seconds if seconds is not None else 4.0 + local,
        progress=0.5,
        duration=REVEAL_SECONDS + 1,
        settled=t >= 1.0,
    )
    scenes.draw(f, name, params, brand.STAGE, clock, scenes.Ctx(images=images or {}))
    return f.render(ground(theme, brand.WIDTH, brand.HEIGHT))


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--theme", default="ink", choices=["ink", "paper"])
    ap.add_argument("--scene", action="append")
    ap.add_argument("--out", type=Path, default=ROOT / "build" / "gallery")
    args = ap.parse_args(argv)
    names = args.scene or sorted(scenes.REGISTRY)
    frames, labels = [], []
    for name in names:
        demo = scenes.REGISTRY[name].demo
        row = []
        for t in REVEAL:
            img = still(name, demo, t, args.theme)
            frames.append(img)
            labels.append(f"{name}  t={t:.2f}")
            row.append(img)
        from bc_image import save

        save(row[-1], args.out / args.theme / f"{name}.png")
    dest = contact_sheet(
        frames, labels, args.out / f"{args.theme}.png", columns=4, tile_width=460, title=f"Scene gallery ({args.theme})"
    )
    print(dest)


if __name__ == "__main__":
    main()
