"""The brand bookends and the YouTube sheet: offline checks, no network."""

from __future__ import annotations

import hashlib
import json

from pipeline import youtube
from pipeline.package import BRAND_DIR, DISSOLVE, _shift


def test_idents_match_their_manifest():
    m = json.loads((BRAND_DIR / "manifest.json").read_text())
    assert m["handle"] == "@DaVinciMath"
    assert m["site"] == "https://math.davincilearner.com/"
    assert m["outro_lead_seconds"] >= DISSOLVE  # the end card dissolves into held ground
    for cue in m["cues"].values():
        digest = hashlib.sha256((BRAND_DIR / cue["file"]).read_bytes()).hexdigest()
        assert digest == cue["sha256"]
        assert cue["frames"] == round(cue["seconds"] * cue["fps"])


def test_captions_shift_by_the_intro():
    vtt = "WEBVTT\n\n00:00:00.000 --> 00:00:02.500\nOne.\n\n00:00:03.000 --> 00:00:04.000\nTwo.\n"
    cues = _shift(vtt, 4.2)
    assert [(c.start_ms, c.end_ms) for c in cues] == [(4200, 6700), (7200, 8200)]


def test_stamps_and_paragraphs():
    assert youtube._stamp(0) == "0:00"
    assert youtube._stamp(599.9) == "9:59"
    assert youtube._stamp(3725) == "1:02:05"
    assert youtube._paragraphs("a\nb\n\nc\n") == ["a b", "c"]


def test_sources_read_from_the_register():
    reg = youtube._sources()
    assert reg["S01"].endswith("https://www.ripid.ethz.ch/Paper/DerKiureghian_paper.pdf")
    assert "?. " not in reg["S01"]  # a title ending in ? takes no extra stop
    assert "et al." in reg["S08"]  # seven authors are shortened
