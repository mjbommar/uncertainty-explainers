"""Script validation: what is accepted, and what is refused with a useful message."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from pipeline.spec import SpecError, Video, estimate, load, validate

ROOT = Path(__file__).resolve().parents[1]
SMOKE = ROOT / "videos" / "_smoke" / "script.yaml"


def _raw() -> dict:
    return yaml.safe_load(SMOKE.read_text())


def _write(tmp_path: Path, raw: dict) -> Path:
    p = tmp_path / "script.yaml"
    p.write_text(yaml.safe_dump(raw))
    return p


def test_smoke_script_loads() -> None:
    video = load(SMOKE)
    assert video.slug == "_smoke"
    assert len(video.segments) == 5
    assert video.image("storm").provider == "openai"


def test_estimate_is_words_at_150_wpm_plus_holds() -> None:
    video = load(SMOKE)
    est = estimate(video)
    speech = video.words / 150 * 60
    holds = sum(s.hold for s in video.segments)
    assert est["seconds"] == pytest.approx(speech + holds + video.end_card.seconds, abs=0.11)


@pytest.mark.parametrize(
    ("mutate", "message"),
    [
        (lambda r: r["segments"][1]["scene"].update(name="nope"), "unknown scene"),
        (lambda r: r["segments"][1]["scene"]["params"].pop("left"), "needs param 'left'"),
        (lambda r: r["segments"][1]["scene"]["params"].update(colour="red"), "unknown params"),
        (lambda r: r["segments"][1].update(transition="spin"), "unknown transition"),
        (lambda r: r["segments"][1]["sfx"][0].update(cue="kazoo"), "unknown sfx cue"),
        (lambda r: r["segments"][1]["sfx"][0].update(at="not said"), "not in the narration"),
        (lambda r: r["segments"][1].update(say="Risk — and more risk than you would think."), "em dash"),
        (lambda r: r["segments"][4]["scene"]["params"].update(image="image:missing"), "not defined"),
        (lambda r: r["segments"][1].update(sources=["S9999"]), "not of the form"),
        (lambda r: r["segments"][1].update(beats=["never spoken"]), "beat"),
    ],
)
def test_refusals(tmp_path: Path, mutate, message: str) -> None:
    raw = _raw()
    mutate(raw)
    with pytest.raises(SpecError, match=message):
        load(_write(tmp_path, raw))


def test_sfx_needs_exactly_one_source(tmp_path: Path) -> None:
    raw = _raw()
    raw["segments"][1]["sfx"] = [{"cue": "whoosh", "prompt": "a whoosh", "duration": 1.0}]
    with pytest.raises(SpecError, match="exactly one"):
        load(_write(tmp_path, raw))


def test_unknown_top_level_key_is_refused(tmp_path: Path) -> None:
    raw = _raw()
    raw["colour"] = "blue"
    with pytest.raises(SpecError, match="colour"):
        load(_write(tmp_path, raw))


def test_length_warning() -> None:
    video = Video.model_validate({**_raw(), "target_seconds": 5})
    assert any("target" in w for w in validate(video))
