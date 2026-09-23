"""The script schema: one YAML file per video, validated before anything is spent.

A video is metadata (slug, title, target length, voice casting, theme), a list
of generated image assets, and a list of ``segments``. Each segment carries one
narration line (``say``, Simplified Book English), exactly one ``scene`` with
its parameters, optional sound effects, an optional image reference, the
transition *into* it, a silent ``hold`` after it, and the ``sources`` keys
(``S01``...) its claims rest on. Unknown scenes, missing scene parameters,
undefined images, unknown cues and cue phrases that are not in the narration
are refused here with a message that says what to change.

``estimate`` is the free ``--stage check``: word count at 150 words a minute
plus holds and the end card.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator, model_validator

from . import ROOT

__all__ = [
    "HOUSE_STYLE",
    "WPM",
    "EndCard",
    "ImageSpec",
    "MusicSpec",
    "SceneSpec",
    "Segment",
    "SfxSpec",
    "SpecError",
    "Video",
    "VoiceSpec",
    "estimate",
    "load",
    "source_keys",
]

WPM = 150.0
#: The narrator's sustained delivery, sent as Gemini 3.8 ``speech_metadata.style``.
HOUSE_STYLE = (
    "A calm, clear adult narrator for a short educational film. Unhurried and even, "
    "about 145 words a minute, warm but not theatrical. Plain American English. "
    "Give each sentence a natural full stop and let key terms land without stressing them."
)
_SOURCE_KEY = re.compile(r"^S\d{2,3}$")
_SOURCE_DEF = re.compile(r"\[?(S\d{2,3})\]?")


class SpecError(ValueError):
    """The script cannot be built as written."""


class _Model(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")


class VoiceSpec(_Model):
    """Who reads the narration. ``gemini-3.8-*`` goes through the styled backend."""

    provider: Literal["gemini"] = "gemini"
    model: str = "gemini-3.8-flash-tts"
    voice: str = "Charon"
    style: str = HOUSE_STYLE


class SfxSpec(_Model):
    """One sound effect: a named library cue, or a prompt with a duration.

    ``at`` is seconds into the segment's narration, or a phrase from ``say``;
    the cue fires where that phrase is spoken (by character weight).
    """

    cue: str | None = None
    prompt: str | None = None
    duration: float | None = Field(default=None, ge=0.5, le=22.0)
    at: float | str = 0.0
    gain_db: float = Field(default=0.0, ge=-40.0, le=12.0)

    @model_validator(mode="after")
    def _one_source(self) -> SfxSpec:
        if (self.cue is None) == (self.prompt is None):
            raise ValueError("an sfx needs exactly one of 'cue' (a library name) or 'prompt'")
        if self.prompt is not None and self.duration is None:
            raise ValueError("a prompted sfx needs 'duration' in seconds (0.5 to 22)")
        return self


class ImageSpec(_Model):
    """A generated image asset, referenced by ``id`` from segments and scene params."""

    id: str = Field(pattern=r"^[a-z0-9][a-z0-9_-]*$")
    prompt: str = Field(min_length=3)
    kind: Literal["icon", "illustration"] = "icon"
    provider: Literal["openai", "gemini"] = "openai"
    model: str | None = None
    quality: Literal["low", "medium", "high", "auto"] = "medium"


class MusicSpec(_Model):
    """An optional instrumental bed, ducked under the narration."""

    prompt: str
    gain_db: float = Field(default=-20.0, le=0.0)
    enabled: bool = True


class SceneSpec(_Model):
    name: str
    params: dict[str, Any] = Field(default_factory=dict)


class EndCard(_Model):
    seconds: float = Field(default=4.0, ge=1.5, le=12.0)
    line: str = "Uncertainty Explainers"
    note: str = ""


class Segment(_Model):
    id: str
    say: str = Field(min_length=1)
    scene: SceneSpec
    sfx: tuple[SfxSpec, ...] = ()
    image: str | None = None
    transition: str = "dissolve"
    hold: float = Field(default=0.45, ge=0.0, le=6.0)
    sources: tuple[str, ...] = ()
    caption: str | None = None
    beats: tuple[float | str, ...] = ()
    direction: str | None = None

    @field_validator("sfx", mode="before")
    @classmethod
    def _listify(cls, v: Any) -> Any:
        if v is None:
            return ()
        return [v] if isinstance(v, dict | str) else v

    @property
    def words(self) -> int:
        return len(self.say.split())


class Video(_Model):
    slug: str = Field(pattern=r"^_?[a-z0-9][a-z0-9_-]*$")
    title: str
    subtitle: str = ""
    series: str = "Uncertainty Explainers"
    target_seconds: float = Field(gt=0)
    theme: Literal["ink", "paper"] = "ink"
    voice: VoiceSpec = VoiceSpec()
    music: MusicSpec | None = None
    images: tuple[ImageSpec, ...] = ()
    burn_captions: bool = True
    end_card: EndCard = EndCard()
    segments: tuple[Segment, ...] = Field(min_length=1)
    status: Literal["draft", "review", "final"] = "draft"

    @property
    def words(self) -> int:
        return sum(s.words for s in self.segments)

    def image(self, image_id: str) -> ImageSpec:
        for spec in self.images:
            if spec.id == image_id:
                return spec
        raise KeyError(image_id)


def source_keys(register: Path | None = None) -> set[str] | None:
    """The ``Sxx`` keys defined in ``research/SOURCES.md``, or ``None`` if it is absent."""
    path = register or ROOT / "research" / "SOURCES.md"
    if not path.is_file():
        return None
    keys: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        head = line.lstrip("#|-* ").strip()
        m = _SOURCE_DEF.match(head)
        if m:
            keys.add(m.group(1))
    return keys


def _image_refs(value: Any) -> list[str]:
    """Scene params reference images as ``"image:<id>"`` strings, anywhere in the tree."""
    out: list[str] = []
    if isinstance(value, str) and value.startswith("image:"):
        out.append(value.split(":", 1)[1])
    elif isinstance(value, dict):
        for v in value.values():
            out.extend(_image_refs(v))
    elif isinstance(value, list | tuple):
        for v in value:
            out.extend(_image_refs(v))
    return out


def validate(video: Video) -> list[str]:
    """Refuse what cannot be built (raises); return warnings for what is merely doubtful."""
    from bc_motion import TRANSITIONS

    from . import scenes, sound

    errors: list[str] = []
    warnings: list[str] = []
    ids = [s.id for s in video.segments]
    if len(set(ids)) != len(ids):
        errors.append(f"segment ids repeat: {ids}")
    image_ids = {i.id for i in video.images}
    if len(image_ids) != len(video.images):
        errors.append("image ids repeat")
    known_sources = source_keys()
    if known_sources is None:
        warnings.append("research/SOURCES.md is missing; source keys were not checked")
    for seg in video.segments:
        where = f"segment {seg.id}"
        if "—" in seg.say or " -- " in seg.say:
            errors.append(f"{where}: narration has an em dash; use a full stop or a comma")
        reg = scenes.REGISTRY.get(seg.scene.name)
        if reg is None:
            errors.append(f"{where}: unknown scene {seg.scene.name!r}; known: {', '.join(sorted(scenes.REGISTRY))}")
        else:
            for key in reg.required:
                if key not in seg.scene.params:
                    errors.append(f"{where}: scene {seg.scene.name} needs param {key!r}")
            unknown = set(seg.scene.params) - set(reg.required) - set(reg.optional)
            if unknown:
                errors.append(
                    f"{where}: scene {seg.scene.name} has unknown params {sorted(unknown)}; "
                    f"allowed: {sorted(set(reg.required) | set(reg.optional))}"
                )
        if seg.transition not in TRANSITIONS:
            errors.append(f"{where}: unknown transition {seg.transition!r}; known: {TRANSITIONS}")
        refs = _image_refs(seg.scene.params) + ([seg.image] if seg.image else [])
        for ref in refs:
            if ref not in image_ids:
                errors.append(f"{where}: image {ref!r} is not defined under images:")
        for fx in seg.sfx:
            if fx.cue is not None and fx.cue not in sound.LIBRARY:
                errors.append(f"{where}: unknown sfx cue {fx.cue!r}; known: {', '.join(sorted(sound.LIBRARY))}")
            if isinstance(fx.at, str) and fx.at.lower() not in seg.say.lower():
                errors.append(f"{where}: sfx fires on {fx.at!r}, which is not in the narration")
        for beat in seg.beats:
            if isinstance(beat, str) and beat.lower() not in seg.say.lower():
                errors.append(f"{where}: beat {beat!r} is not in the narration")
        for key in seg.sources:
            if not _SOURCE_KEY.match(key):
                errors.append(f"{where}: source key {key!r} is not of the form S01")
            elif known_sources is not None and key not in known_sources:
                errors.append(f"{where}: source {key} is not in research/SOURCES.md")
        if seg.words < 6:
            warnings.append(f"{where}: only {seg.words} words; very short TTS lines invent speech more often")
    if errors:
        raise SpecError("; ".join(errors))
    est = estimate(video)["seconds"]
    if abs(est - video.target_seconds) > 0.25 * video.target_seconds:
        warnings.append(f"estimated {est:.1f}s is more than 25% from the {video.target_seconds:.0f}s target")
    return warnings


def estimate(video: Video) -> dict[str, Any]:
    speech = video.words / WPM * 60.0
    holds = sum(s.hold for s in video.segments)
    return {
        "words": video.words,
        "speech_seconds": round(speech, 1),
        "hold_seconds": round(holds, 1),
        "end_card_seconds": video.end_card.seconds,
        "seconds": round(speech + holds + video.end_card.seconds, 1),
        "segments": [
            {"id": s.id, "words": s.words, "seconds": round(s.words / WPM * 60.0 + s.hold, 1)} for s in video.segments
        ],
    }


def load(path: Path | str) -> Video:
    """Read and validate a script; raises :class:`SpecError` with every fault found."""
    p = Path(path)
    try:
        raw = yaml.safe_load(p.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise SpecError(f"{p}: {exc}") from exc
    if not isinstance(raw, dict):
        raise SpecError(f"{p}: the script must be a mapping")
    try:
        video = Video.model_validate(raw)
    except ValidationError as exc:
        faults = "; ".join(f"{'.'.join(str(x) for x in e['loc'])}: {e['msg']}" for e in exc.errors())
        raise SpecError(f"{p}: {faults}") from None
    validate(video)
    return video
