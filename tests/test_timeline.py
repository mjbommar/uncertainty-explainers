"""Timeline arithmetic: quantisation, spans, beats, captions and drift. No network."""

from __future__ import annotations

from pathlib import Path

import pytest

from pipeline import timeline
from pipeline.spec import load

SMOKE = Path(__file__).resolve().parents[1] / "videos" / "_smoke" / "script.yaml"
SECONDS = [3.72, 7.77, 6.59, 7.09, 5.6]


def plan():
    return timeline.build(load(SMOKE), SECONDS)


def test_frames_are_the_sum_of_quantised_states() -> None:
    p = plan()
    video = load(SMOKE)
    expected = sum(max(1, round(s * 30)) for s in SECONDS)
    expected += sum(round(seg.hold * 30) for seg in video.segments if seg.hold > 0)
    expected += round(video.end_card.seconds * 30)
    assert p.timeline.total_frames == expected


def test_spans_tile_the_programme() -> None:
    p = plan()
    assert p.spans[0][1] == 0.0
    for (_, _, end), (_, start, _) in zip(p.spans, p.spans[1:], strict=False):
        assert start == pytest.approx(end)
    assert p.spans[-1][0] == -1
    assert p.spans[-1][2] == pytest.approx(p.timeline.total_seconds)


def test_beats_are_inside_their_narration() -> None:
    p = plan()
    beats = p.beats[1]
    assert len(beats) == 4
    assert beats == tuple(sorted(beats))
    assert beats[0] >= 0.0 and beats[-1] < p.narration_seconds[1]


def test_captions_are_valid_and_one_per_sentence_group(tmp_path: Path) -> None:
    summary = timeline.write(load(SMOKE), plan(), tmp_path)
    assert summary["caption_problems"] == []
    assert (tmp_path / "captions.vtt").read_text().startswith("WEBVTT")


def test_drift_is_asserted() -> None:
    p = plan()
    timeline.check_drift(p, p.timeline.total_seconds)
    with pytest.raises(ValueError, match="drift"):
        timeline.check_drift(p, p.timeline.total_seconds + 1.0)


def test_wrong_clip_count_is_refused() -> None:
    with pytest.raises(ValueError, match="measured clips"):
        timeline.build(load(SMOKE), SECONDS[:-1])
