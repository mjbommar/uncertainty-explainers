"""The one palette, type system and layout authority.

Two grounds. **Ink** is a deep blue-black with warm paper-white type, for the
series default. **Paper** is a warm off-white with ink type, for the rare video
that wants a lighter register. Both share one role vocabulary, so a scene names
``accent`` or ``known`` and never a hex value.

Colour roles carry meaning across the series, and they are kept to four:

- ``known`` (teal): the part we can count; risk; a measured quantity.
- ``unknown`` (amber): the part we cannot; uncertainty; an estimate.
- ``warn`` (coral): a mistake, a misreading, a gap between people.
- ``cool`` (slate blue): neutral structure, a second series.

Type: DM Serif Display for display lines and quotations (high contrast, reads as
a book, not a dashboard); Inter for text and labels; IBM Plex Mono for numbers
that must line up. All three are installed on this machine (``fc-list``) and are
passed to the rasteriser by path, so a missing face fails loudly.

Layout is a 1920x1080 logical frame, rendered at any multiple. The safe area is
the title-safe 90 % region plus a reserved caption band at the bottom that no
scene may enter, so platform captions never cover a label.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import cache
from pathlib import Path

__all__ = [
    "BAND",
    "DISPLAY",
    "FONT_PATHS",
    "HEADER",
    "HEIGHT",
    "MONO",
    "SAFE",
    "STAGE",
    "TEXT",
    "WIDTH",
    "Box",
    "Palette",
    "metrics",
    "palette",
]

WIDTH, HEIGHT = 1920, 1080

DISPLAY = "DM Serif Display"
TEXT = "Inter"
MONO = "IBM Plex Mono"

_HOME_FONTS = Path.home() / ".local/share/fonts"
FONT_PATHS: tuple[str, ...] = (
    "/usr/share/fonts/opentype/inter/Inter-Regular.otf",
    "/usr/share/fonts/opentype/inter/Inter-Medium.otf",
    "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf",
    "/usr/share/fonts/opentype/inter/Inter-Italic.otf",
    str(_HOME_FONTS / "DMSerifDisplay-Regular.ttf"),
    str(_HOME_FONTS / "DMSerifDisplay-Italic.ttf"),
    str(_HOME_FONTS / "ibm-plex/IBMPlexMono-Regular.otf"),
    str(_HOME_FONTS / "ibm-plex/IBMPlexMono-Bold.otf"),
)
_METRIC_FILES = {
    (TEXT, 400): FONT_PATHS[0],
    (TEXT, 500): FONT_PATHS[1],
    (TEXT, 600): FONT_PATHS[2],
    (DISPLAY, 400): FONT_PATHS[4],
    (MONO, 400): FONT_PATHS[6],
    (MONO, 700): FONT_PATHS[7],
}


@dataclass(frozen=True, slots=True)
class Box:
    """An axis-aligned region in logical pixels."""

    x: float
    y: float
    w: float
    h: float

    @property
    def right(self) -> float:
        return self.x + self.w

    @property
    def bottom(self) -> float:
        return self.y + self.h

    @property
    def cx(self) -> float:
        return self.x + self.w / 2

    @property
    def cy(self) -> float:
        return self.y + self.h / 2

    def inset(self, dx: float, dy: float | None = None) -> Box:
        dy = dx if dy is None else dy
        return Box(self.x + dx, self.y + dy, self.w - 2 * dx, self.h - 2 * dy)

    def split_x(self, fraction: float, gap: float = 0.0) -> tuple[Box, Box]:
        left = (self.w - gap) * fraction
        return (
            Box(self.x, self.y, left, self.h),
            Box(self.x + left + gap, self.y, self.w - left - gap, self.h),
        )

    def split_y(self, fraction: float, gap: float = 0.0) -> tuple[Box, Box]:
        top = (self.h - gap) * fraction
        return (
            Box(self.x, self.y, self.w, top),
            Box(self.x, self.y + top + gap, self.w, self.h - top - gap),
        )

    def contains(self, other: Box, slack: float = 0.0) -> bool:
        return (
            other.x >= self.x - slack
            and other.y >= self.y - slack
            and other.right <= self.right + slack
            and other.bottom <= self.bottom + slack
        )


#: Title-safe: 6.25 % left/right (120 px), a header strip above the stage.
SAFE = Box(120, 72, WIDTH - 240, HEIGHT - 144)
#: Series label and progress rail.
HEADER = Box(120, 56, WIDTH - 240, 44)
#: Where scenes draw. Nothing below it: the caption band is reserved.
STAGE = Box(120, 140, WIDTH - 240, 740)
#: Burned-in captions (when on) and the platform's own captions.
BAND = Box(240, 906, WIDTH - 480, 118)


@dataclass(frozen=True, slots=True)
class Palette:
    name: str
    ground: str
    ground_edge: str
    surface: str
    surface_2: str
    line: str
    text: str
    text_soft: str
    text_faint: str
    known: str
    known_soft: str
    unknown: str
    unknown_soft: str
    warn: str
    cool: str
    caption_plate: str
    caption_text: str

    def rgb(self, role: str) -> tuple[float, float, float]:
        value = getattr(self, role).lstrip("#")
        return tuple(int(value[i : i + 2], 16) / 255.0 for i in (0, 2, 4))  # type: ignore[return-value]


INK = Palette(
    name="ink",
    ground="#11141b",
    ground_edge="#090b10",
    surface="#1a1f29",
    surface_2="#232a36",
    line="#343d4c",
    text="#f1ebdf",
    text_soft="#b4ada1",
    text_faint="#7d7a74",
    known="#6cc0b0",
    known_soft="#2c5a55",
    unknown="#e9b35a",
    unknown_soft="#6b5330",
    warn="#e0826a",
    cool="#86a2d4",
    caption_plate="#0a0c11",
    caption_text="#f4efe6",
)

PAPER = Palette(
    name="paper",
    ground="#f5f0e6",
    ground_edge="#e7dfcf",
    surface="#ece5d7",
    surface_2="#e2d9c7",
    line="#cfc5b1",
    text="#1b2130",
    text_soft="#555b68",
    text_faint="#8b8a86",
    known="#1f7a6d",
    known_soft="#b9d9d2",
    unknown="#a8661a",
    unknown_soft="#ecd3ad",
    warn="#b24b33",
    cool="#3d5c94",
    caption_plate="#1b2130",
    caption_text="#f5f0e6",
)

_PALETTES = {"ink": INK, "paper": PAPER}


def palette(name: str) -> Palette:
    try:
        return _PALETTES[name]
    except KeyError:
        raise KeyError(f"unknown theme {name!r}; known: {sorted(_PALETTES)}") from None


@cache
def metrics(family: str, weight: int = 400):  # -> bc_viz.FontMetrics
    """The advance table for one face, cached on disk by the font file's sha256."""
    from bc_viz.fonts import extract_metrics

    from . import ROOT

    key = (family, weight)
    if key not in _METRIC_FILES:
        key = (family, 400)
    return extract_metrics(_METRIC_FILES[key], cache_dir=ROOT / ".cache" / "fonts")


def missing_fonts() -> list[str]:
    return [p for p in FONT_PATHS if not Path(p).is_file()]
