"""The roadmap scene stays in the stage in every mode, with the longest allowed text."""

from __future__ import annotations

import pytest

from pipeline import brand, scenes
from pipeline.canvas import Frame, ink_bbox
from pipeline.scenes_shared import _DEMO_STOPS

LONG = {"kicker": "Stop six of six", "heading": "Two kinds of not knowing, in six steps"}
CASES = {
    "overview4": {"stops": _DEMO_STOPS[:4], "mode": "overview", "current": -1},
    "overview6": {"stops": _DEMO_STOPS, "mode": "overview", "current": -1},
    "travel_first": {"stops": _DEMO_STOPS, "mode": "travel", "current": 0},
    "travel_last": {**LONG, "stops": _DEMO_STOPS, "mode": "travel", "current": 5},
    "summary4": {**LONG, "stops": _DEMO_STOPS[:4], "mode": "summary", "current": 4},
    "summary6_bare": {"stops": _DEMO_STOPS, "mode": "summary", "current": 6},
}


@pytest.mark.parametrize("theme", ["ink", "paper"])
@pytest.mark.parametrize("case", sorted(CASES))
def test_roadmap_modes_stay_in_stage(case: str, theme: str) -> None:
    for t in (0.0, 0.3, 0.6, 1.0):
        f = Frame(brand.palette(theme))
        clock = scenes.Clock(t=t, local=t * 3.2, seconds=7.0 + t, settled=t >= 1.0)
        scenes.draw(f, "roadmap", CASES[case], brand.STAGE, clock)
        box = ink_bbox(f.render_rgba())
        assert box is None or brand.STAGE.contains(box, slack=2.0), f"{case} t={t}: {box}"


@pytest.mark.parametrize(
    "params",
    [
        {"stops": _DEMO_STOPS[:3]},
        {"stops": _DEMO_STOPS, "current": 9},
        {"stops": _DEMO_STOPS, "mode": "tour"},
        {"stops": [{"label": "No question"}] * 4},
    ],
)
def test_roadmap_rejects_bad_params(params: dict) -> None:
    with pytest.raises(ValueError):
        scenes.draw(Frame(brand.palette("ink")), "roadmap", params, brand.STAGE, scenes.Clock())
