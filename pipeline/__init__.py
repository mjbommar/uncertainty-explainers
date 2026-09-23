"""The production pipeline: a YAML script in, a checked 1920x1080 explainer out.

Every stage composes ``bc-modules``: speech, sound and images through ``bc_gen``
(verified, cached, receipted), audio post through ``bc_audio``/``bc_signal``,
frames drawn per frame with ``bc_viz`` and composited with ``bc_image``, time and
assembly through ``bc_motion``. See ``docs/PIPELINE.md``.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / ".cache" / "bc-gen"

__all__ = ["CACHE", "ROOT"]
