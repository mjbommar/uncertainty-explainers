"""QA reports a containment failure instead of crashing on it."""

from __future__ import annotations

import json

from pipeline import qa, scenes, spec
from pipeline.brand import Box


def test_containment_rows_are_json_serialisable(monkeypatch) -> None:
    def spill(f, box, p, c, ctx):
        f.rect(Box(box.x, box.y, box.w + 60, 40), fill=f.pal.text)

    monkeypatch.setitem(scenes.REGISTRY, "_spill", scenes.SceneDef("_spill", spill, (), (), {}, "spills"))
    video = spec.Video(slug="_t", title="t", target_seconds=5, segments=[{"id": "a", "say": "one two three four five six", "scene": {"name": "_spill"}}])
    rows = qa.containment(video, {})
    assert not rows[0]["ok"]
    json.dumps(rows)
