# LOCAL-RESOURCES — what this project reuses from sibling repos

Six sibling repos were mined for patterns this project should reuse. This
document records, per repo: what to reuse and where it lives, what is already
superseded by `bc-modules` (see `docs/BC-MODULES-API.md` for the verified call
inventory), and concrete recommendations for this project's own pipeline. A
final section collects exact accounting and legal text this project can use as
worked examples of uncertainty vocabulary.

Do not copy code from any of these repos into this one. Everything below is a
pointer plus a description of the pattern, per the task rule: document paths
and patterns, reuse `bc-modules` for the actual implementation.

---

## 1. `understanding-accounting` — `media/shorts/`, `media/video/`, `docs/youtube/`

This is the closest analog to what this project needs: a script-driven,
per-frame drawn concept-explainer pipeline, with a documented voice, brand,
and QA system built over roughly a year of shipped videos.

### The script format to adopt (the shape, not the code)

`media/shorts/spec.py`
(`/home/mjbommar/projects/personal/understanding-accounting/media/shorts/spec.py`)
defines a YAML contract worth copying the *shape* of for `videos/<slug>/script.yaml`:

```yaml
id: S1
slug: credit-good-debit-bad
format: short                 # or "explainer"
title: "..."
segments:
  - id: s01
    narration: "..."
    caption: null              # burned-in caption text, or null to reuse narration
    scene: title_card          # which drawing routine renders this segment
    args: {question: "...", subtitle: null}
    hold: 0.4                  # extra seconds held after narration ends
    sound: [{name: "chart-pop", at: "the second time we saw this"}]
status: draft                  # gates the whole build until reviewed
```

The load-time refusals in `spec.py` are worth keeping too: reject an unknown
scene name or a missing required argument, reject a caption over two lines or
40 characters per line, reject an empty narration line. Adopt this as
`pipeline/`'s script schema (a pydantic model, validated by
`uv run python -m pipeline.build ... --stage check`), with a `SCENES` registry
of `scene_name -> required_args` exactly like `spec.py`'s, but pointed at
`bc_viz.Canvas`-based drawing functions instead of the accounting-specific
vocabulary (`journal_entry`, `t_account`, `trial_balance`, ...). This
project's scene vocabulary should instead cover things like `sample_space`,
`confidence_band`, `forecast_cone`, `bayes_update`, `calibration_plot`,
`counterfactual_branch`, `venn_diagram`, `probability_bar`.

### Scene-drawing pattern to reuse (not the code — the technique)

`media/shorts/scenes.py`
(`/home/mjbommar/projects/personal/understanding-accounting/media/shorts/scenes.py`)
establishes three ideas worth carrying into `pipeline/`'s scene functions,
now built on `bc_viz.Canvas` and `bc_image` rather than raw Pillow:

1. **Persistence, not restart.** Each scene function receives the previous
   segment's `args`. If a new segment reuses the same scene with identical
   args, draw the settled state plus ambient motion only; if the args
   changed, animate only the delta (a new bar segment appearing, a shifted
   highlight). `bc_image.change_mask`/`regions` (see `BC-MODULES-API.md` §5)
   is the `bc-modules` primitive for detecting exactly this kind of delta.
2. **Never a perfectly still frame.** A `_sheen()`-style ambient motion (a
   soft light hairline crossing the frame every few seconds) keeps a settled
   scene from reading as frozen or broken. Cheap to add to any `bc_viz`
   canvas via a slow-moving low-opacity element.
3. **One emphasis device, not a looping one.** A single one-shot highlight
   wash for "this is the important part," not a repeating pulse — the
   repo's own note is exact: "a highlight that breathes for ever reads as a
   loading spinner."

### Brand tokens worth carrying (as a starting point, not final choices)

`media/shorts/brand.py`
(`/home/mjbommar/projects/personal/understanding-accounting/media/shorts/brand.py`)
is worth reading for the *pattern* — one palette file, mirrored from the
site's own CSS tokens, with semantic color aliases chosen for what they teach
rather than convention (`DEBIT = BLUE`, `CREDIT = RUST`, deliberately not
green/red, "a palette that judged the two sides would teach a
misconception"). This project should do the same: pick a small, fixed
palette and, if any concept has a color mapping (e.g. "warm = higher
probability"), choose it deliberately and document why in `pipeline/`.

Safe-box numbers are directly reusable if this project ever ships a vertical
or square cut: vertical (1080x1920) safe box `(65,250)-(940,1490)`, caption
band `(65,1300)-(940,1490)`; horizontal (1920x1080) safe box
`(120,90)-(1800,990)`, caption band `(320,880)-(1600,990)`. This project's
`AGENTS.md` doesn't specify a frame size yet — recommend 1920x1080 (the
`format: explainer` case) as the primary target, since these are 2-10 minute
explainers, not Shorts.

### Voice — exact auditioned settings

`media/audio/voices.yaml` and `docs/youtube/VOICE-AND-MUSIC.md`
(`/home/mjbommar/projects/personal/understanding-accounting/`) recorded a
real by-ear audition across Gemini and OpenAI TTS voices before choosing one.
Two things worth reusing directly:

- **The measurement method**, not just the result: for each candidate voice,
  measure words-per-minute, loudness range (95th-20th percentile of 100ms
  RMS frames), and pitch range (10th-90th percentile f0 in semitones) against
  a fixed audition script, then pick by ear plus these numbers. Their
  finding — "the direction bought rate and nothing else; wording like 'be
  more dynamic' does not reach the measure" — means don't trust a voice
  direction's adjectives; measure the delivered audio.
- **Plan against delivered rate, not requested rate.** Their shipped
  direction asked for ~170 words per minute; measured delivery across built
  scripts ranged 107-162 wpm even after a 1.15x tempo correction. Their
  stated rule: "plan a script against 120 to 150 words a minute rather than
  the 170 the direction asks for." This project should budget narration word
  counts the same way — for a target video length, multiply minutes by
  120-150, not by whatever a voice's marketing copy claims.

The exact shipped direction string (for the explainer-register casting,
`gemini-shorts`, voice **Sadaltager**, model `gemini-3.1-flash-tts-preview`):

> "Speak in a neutral American accent. You are a sharp, energetic explainer
> in a short video: brisk, about 170 words per minute, with real dynamic
> range. Lift pitch and pace on questions and setups, then drop lower and
> slower to land the key term or the number. Punch the contrast words.
> Confident and animated, never breathy and never a hype voice; a great
> teacher who is genuinely pleased the idea is about to click. Crisp
> consonants, firm sentence endings, short pauses."

This is a good starting direction to audition for this project's own
narrator voice via `bc_gen.Voice`/`bc_gen.Casting` (see
`BC-MODULES-API.md` §3) — adjusted for a calmer, more measured register,
since a video about calibrated uncertainty language probably wants a voice
that undersells rather than "punches," but the *audition method* (measure
wpm/loudness-range/pitch-range against a fixed script) transfers directly.

### SFX and music approach

Two reusable patterns from `docs/youtube/VOICE-AND-MUSIC.md`, independent of
the specific vendor cues:

- **A small, named SFX vocabulary invoked from the script**, not ad hoc: a
  segment's `sound:` field names a cue (`chart-pop`, `whoosh-soft`,
  `tick-count`) either at a literal second offset or at a phrase in the
  narration (resolved via word-level ASR alignment — `bc_content.align`, see
  `BC-MODULES-API.md` §11). Build a small SFX pack for this project's own
  needs (a soft tick for a probability updating, a clean pop for a term
  landing on screen) via `bc_gen.ElevenLabsSound` rather than reusing
  understanding-accounting's accounting-flavored pack.
- **A continuous, deliberately quiet ambient bed, sidechain-ducked under
  narration.** Their numbers: bed mixed at -12 dB relative to the
  clip-normalized voice, sidechain ratio 5:1, 60ms attack, 700ms release,
  crossfade-looped past its natural length so a long program never audibly
  repeats, and mixed low enough in the 800-4000 Hz band (3.6% of its energy)
  that it never masks consonants. Reuse this as a starting mix recipe via
  `bc_audio.compressor(..., key=narration)` for the ducking and
  `bc_audio.ffmpeg.seamless_bed` for the loop (`BC-MODULES-API.md` §4).

### Mastering targets

Two profiles were shipped, and neither matches `bc_audio`'s `SPOKEN_WORD`
default exactly:

| | Lecture (`media/video`) | Shorts (`media/shorts`) | `bc_audio.SPOKEN_WORD` default |
|---|---|---|---|
| Integrated loudness | -18.0 LUFS | **-16.0 LUFS** | -18.0 LUFS |
| True peak | -1.5 dBTP | -1.5 dBTP | -1.5 dBTP |
| Loudness range | 7.0 LU (9.0 max) | 8.0 LU (12.0 max) | 7.0 LU |
| Channels | mono | **stereo** | mono |
| Bitrate | 128k | 192k | — |

**Recommendation:** for 2-10 minute explainers (closer to the lecture
register than to a Short, but meant for YouTube where -16 to -14 LUFS is
common informal guidance the team itself could not confirm from a primary
source), define a project-specific `bc_audio.master.Profile` at **-16.0
LUFS, -1.5 dBTP, LRA 8/12, stereo, 192k** — the Shorts profile's numbers,
which already sit 2 LU under the loosely-sourced -14 LUFS "consensus" for
deliberate headroom — rather than reusing `SPOKEN_WORD` unmodified. Record
the exact `Profile(...)` call once decided in `pipeline/` and reuse it for
every video so numbers stay comparable release to release.

### Caption approach

Two limits worth adopting directly: `MAX_CUE_CHARS = 220` for the VTT
transcript-cue splitting (matches `bc_motion.captions`'s Rust-side default
closely — see `BC-MODULES-API.md` §10), and a **separate, tighter cap for
the burned-in on-screen caption plate**: 2 lines, 40 characters per line
(36 as the softer authoring target). Treat these as two different budgets:
the VTT file can carry a full sentence per cue; the on-screen caption text
should be shorter and simpler, because it has to be read at a glance while
something else is moving on screen.

### QA gates — the most valuable thing to carry over wholesale

Four specific, load-bearing patterns from
`docs/youtube/CHECKLIST.md`/`LESSONS.md`/`review-2026-09-10/` and
`media/shorts/test_scenes.py`:

1. **The ASR round-trip gate is necessary but insufficient, and they proved
   it.** Quoted directly: "The synthesis gate compares the audio to the
   script. It proves the machine said what was written. It cannot tell you
   the writing was wrong, and it says nothing about whether the visual
   matches the sentence." Their concrete failure: a video shipped a
   T-account contradicting its own narration, and every line had passed the
   WER/CER gate. `bc_gen.SpeechVerifier` (`BC-MODULES-API.md` §11) covers
   only the first half; the human/frame-review pass below covers the rest.
2. **A specific, non-uniform frame-sampling rule for decoded-frame review:**
   75% of every segment's span (deliberately chosen because it is after the
   entrance/reveal animation has settled, not during it), plus 10% for a
   short-format video or 5% for a long one, plus the hook frame and the end
   card. Adopt this exact sampling rule for this project's `--stage check`
   or equivalent review step, adjusted for this project's own reveal timing.
3. **"A finding names a frame, and a reviewer verifies it there."** A review
   process failure occurred when findings were reported without re-opening
   the exact named frame. The fix, worth adopting as a hard rule for
   `docs/PRODUCTION-LOG.md` review entries: every finding cites a frame
   number, and closing it requires opening that exact frame again, not
   trusting memory or the fix's intent.
4. **"A re-render is not a re-review."** A code or script fix does not
   retroactively validate frames that no longer exist after a re-render. A
   finding closes only when a *new* frame from the corrected build is
   inspected and shows the fix. This directly extends `AGENTS.md` rule 5's
   "fully decoded, frames inspected" requirement: re-inspect after every
   re-render, not only after the first one.

Also adopt the **draft gate** pattern outright: a script's `status` field
starts at `draft`; a build step refuses to proceed past narration synthesis
without `--allow-drafts`, and any preview built from a draft is labeled as
such. `bc_motion.narration.require_reviewed` (`BC-MODULES-API.md` §7) is the
`bc-modules` primitive for exactly this gate.

### One technical gotcha worth knowing regardless of implementation

`media/shorts/canvas.py`'s documented "alpha bug": Pillow's `ImageDraw` does
not alpha-composite into RGBA — it writes ink directly and a later
`convert("RGB")` silently discards the alpha, so any partially-transparent
draw has to be painted into a small tile and `alpha_composite`d over the
frame by hand. This project should not hit this at all if scene drawing goes
through `bc_viz.Canvas` (which rasterizes via resvg, not raw Pillow) — but
worth knowing if any part of the pipeline falls back to direct Pillow
compositing (e.g. a quick placeholder frame).

### What is superseded by `bc-modules`

Per `/home/mjbommar/projects/bc/bc-modules/docs/MEDIA_REBUILD.md` (the
rebuild plan, status: all six media modules done, tagged `v0.3.0`), most of
the *implementation* in `media/video/` and `media/shorts/` is now generalized
into `bc-modules` and should not be reimplemented:

| understanding-accounting (old) | bc-modules (new) |
|---|---|
| `media/video/timeline.py` | `bc_motion.Timeline` |
| `media/video/captions.py`, `media/audio/transcript.py` | `bc_motion.captions` |
| `media/video/transitions.py` (14 transitions) | `bc_motion` transitions (Rust) |
| `media/video/encode.py`, `motion_encode.py` | `bc_motion.encode` |
| `media/video/deck.py` | `bc_motion.deck` |
| `media/audio/render.py`, `mastering.py` | `bc_gen.speech`, `bc_audio.master` |
| `media/audio/verify.py`, `checked.py` | `bc_gen.verify` + `bc_content.align` |
| `media/audio/numerals.py` | `bc_content.numerals` |
| `media/shorts/canvas.py`, `hud/*.py` | `bc_viz` canvas + rasterization |
| `media/shorts/words.py` (Whisper alignment) | `bc_gen.transcribe` + `bc_content.align` |
| `scripts/figures/generate_images.py` | `bc_gen.image`, `bc_image.io` |

Not superseded, and not meant to be: the accounting-specific scene vocabulary
in `scenes.py`, the YAML script format's *shape* (reuse the pattern, not the
code), the brand palette values, the specific SFX pack and voice castings
(content decisions, not infrastructure), and the QA *process* documents
(`CHECKLIST.md`, the review-log convention) — those are practices to imitate,
not code to import.

---

## 2. `davinci-math` — production pipeline, voice adaptation, video architecture

### The ten-stage release gate

`docs/LESSON-VIDEO-PRODUCTION.md`
(`/home/mjbommar/projects/personal/davinci-math/docs/LESSON-VIDEO-PRODUCTION.md`)
is worth adapting wholesale as `docs/PIPELINE.md`'s QA section: establish
authority/context, author the narration arc, synthesize/verify/master audio,
design the visual argument before layout, author timing from meaning (not
from where a cue happens to end), build the production master at native
resolution (never upscale an intermediate), review the encoded video (not
just its sources), publish immutable media, run a site/asset review loop,
then commit and verify the live/published state.

Its closing **"stop conditions"** list is the single most reusable artifact
here — a concrete, quotable do-not-publish checklist:

> editorial/production language spoken in narration; invented prior
> knowledge; unmatched spoken diagram; animation finishing early without a
> deliberate hold; frame clipping/overflow; mechanically-inferred
> (unreviewed) scene timing; full sequential decode not yet passed;
> mutable/stale/unverified media URLs; "a green test run is the only
> evidence of visual quality."

Adapt this list directly into `docs/PIPELINE.md` as this project's own
do-not-publish gate, replacing lesson-specific items with video-specific
equivalents.

### The narration-arc pattern (doorway / close)

`docs/LESSON-VIDEO-PRODUCTION.md` describes an explicit narration arc: a
**doorway** (locate the listener, recall the prior result or say this is the
first stop, distinguish remembered from new, give a carry-forward question)
and a **close** (retrieve the result and why it works, ask the listener to
restate or use it, name what's next, say what carries forward). This
project's three to four videos on uncertainty (epistemology, probability,
logic and prediction, communicating uncertainty) form a natural sequence —
adopt the doorway/close pattern to connect them, in `research/SYNTHESIS.md`
or a per-video outline: each video should open by placing itself relative to
the one before it and close by naming what the next one builds on.

### Voice rules already folded into `docs/VOICE.md`

The readability-tradeoff mechanism — a numeric target used only as an
advisory finder, never a gate, plus a named exception list for terms that
must stay exact — and the concrete sentence-length numbers (8-20 words
typical, 28-word ceiling, grade 5-8 target) are already distilled into this
project's own `docs/VOICE.md`. One quotable line worth keeping in mind
verbatim, from `docs/STYLE.md`:

> "Readability formulas are advisory. They can find long sentences and dense
> words, but they cannot detect an awkward rhythm, a bad metaphor, or a
> clear definition of a hard idea."

And the term-introduction sequence from `docs/CRAFT.md` — picture/try, notice
the pattern, name the exact idea, state it precisely, test an example and a
boundary case, show what it lets you do — is a good default shape for
introducing each new uncertainty concept (aleatory vs. epistemic
uncertainty, a credible interval, a calibration curve) in a script.

### Video architecture — direct ancestor of `bc_motion`

`docs/video/ARCHITECTURE.md`
(`/home/mjbommar/projects/personal/davinci-math/docs/video/ARCHITECTURE.md`)
describes a narration sidecar (strict JSON per deck page: page number, slide
title, spoken prose, `draft`/`reviewed` status, optional hold, optional
animation) with a hard rule that page/title drift is an error and a
publishable build refuses any `draft` entry. **This is not just a pattern to
imitate — it is the design `bc_motion.narration` (`Note`/`Narration`,
`require_reviewed`, `alignment_problems`) already generalizes.** Use
`bc_motion.narration` directly rather than reimplementing davinci-math's
`video/narration.py`.

Likewise its continuous-animation timing formula,
`u = clamp((f/(N-1) - start) / (end - start), 0, 1)`, is now
`bc_motion.models.Timeline.progress(frame, window)` — call that instead of
re-deriving it.

Two explicit statements in davinci-math's own docs are worth carrying as
institutional memory about *why* certain choices were made:

> "Audio assembly decodes clips and silent holds into one continuous track,
> avoiding the per-clip MP3 padding drift found in the accounting pipeline."

This bug and its fix are now handled by `bc_audio.ffmpeg.concat`'s
duration-assertion (`BC-MODULES-API.md` §9) — a reason to always assemble
narration through that call rather than a bare `ffmpeg concat` invocation.

### What's superseded

`video/model.py`, `timeline.py`, `narration.py`, `captions.py`, `encode.py`,
and `deck.py` are all superseded by `bc_motion` (see the mapping table in
`BC-MODULES-API.md`'s closing section — `docs/MEDIA_REBUILD.md` names
davinci-math explicitly as one of the pipelines absorbed into the rebuild,
alongside understanding-accounting, fieldscore, and autosoundboard). Not
superseded: `video/animations.py`/`cinematic.py` (lesson-specific animation
content), `video/palette.py` (this project's own brand tokens, not
davinci-math's), and the `docs/readability_report.py` pattern — an advisory
Flesch-Kincaid finder over rendered narration text, worth optionally
adapting for this project's own scripts even though it isn't one of the
three required checkers.

---

## 3. `asc-legal-position-paper/video/` — a LaTeX-deck-driven alternative pipeline

### The timeline model, precisely

`gaap_timeline.py`
(`/home/mjbommar/projects/personal/asc-legal-position-paper/video/gaap_timeline.py`)
is a slide-deck-to-video model, not a continuous per-frame canvas: the unit
of visual content is a rasterized Beamer page (a "state"); display duration
comes from cue timings measured from already-synthesized narration audio,
cross-checked against markers embedded in the compiled deck via a custom
Beamer footline macro (`\seg{04-007}{1,4,8}` before a frame, stamped
invisibly into the rendered PDF and recovered later with `pdftotext`).

**This embedded-marker technique is clever but should not be reused as-is.**
`bc_motion.deck.page_texts()` plus `bc_motion.narration`'s explicit sidecar
(with `alignment_problems()` checking declared page/title against the
rendered deck) solves the same page-to-narration binding problem more
directly, without needing a custom Beamer macro or a `pdftotext` round-trip.
If this project uses a LaTeX/Beamer deck for any scene, drive it through
`bc_motion.deck` and `bc_motion.narration`, not a marker-embedding scheme.

### Style tokens and the timeline's two transition types

`theme/gaapvideo.sty` and `gaap_style.py`
(`/home/mjbommar/projects/personal/asc-legal-position-paper/video/`) use a
cream/ink/warm-accent/cool-accent palette (`ground #f4efe5`, `ink #1a1c20`,
`accent #8b6a2a`, `cool #5d7a8a`) and a single serif face (TeX Gyre Schola)
throughout — worth noting as a second concrete example of "pick one small
palette and one type family, mirror it everywhere," alongside understanding-
accounting's palette. `gaap_render.py`'s two transitions (a 12-frame dissolve
for a same-chapter cut, a 20-frame dip-to-ground for a chapter boundary) are
a strict subset of `bc_motion`'s 14 native transitions
(`cut, dissolve, dip, defocus, push-left, push-up, glide, whip, zoom-in,
zoom-out, focus-point, iris, wipe, curl`) — use `bc_motion.render_sequence`
directly rather than hand-rolling a cross-fade.

### Thumbnail pattern worth imitating (no `bc-modules` equivalent exists yet)

`gaap_thumbnail.py` builds a 1280x720 thumbnail at 3x supersampling,
Lanczos-downsampled, with two styles (a bold high-contrast attention
thumbnail, and a quieter title/subtitle style that picks the loudest
2-second window of the actual narration to show an audio-reactive visual at
its peak). No `bc-modules` module currently covers thumbnail generation
(`BC-MODULES-API.md`'s closing section notes this gap) — this pattern (pull
all copy from the same metadata source the video uses, never hand-type it;
pick the timestamp for a "quiet" style from measured audio, not by eye) is
worth reimplementing directly in `pipeline/` using `bc_viz`/`bc_image`.

### Recommendation: which visual approach fits this project

The research agent that reviewed this pipeline reached a specific,
actionable conclusion worth recording here: the deck-driven card/TikZ
vocabulary (`asc-legal-position-paper`) suits **discrete diagrammatic
panels** — a confidence-interval diagram, a decision tree, a comparison
table — where LaTeX's typesetting precision matters and content can be
authored as reveal-by-reveal slide states. The continuous drawn-canvas
approach (`understanding-accounting/media/shorts`) suits **motion tied
tightly to spoken cadence** — a counter counting up as a number is spoken, a
bar filling in as a probability updates. **Recommendation for this
project:** a hybrid, using `bc_viz`'s declarative diagram models
(`FlowDiagram`, `DecisionFlow`, `EquationBridge` — `BC-MODULES-API.md` §6)
for structural panels, and hand-built `bc_viz.Canvas` scenes with the
persistence/ambient-motion pattern from understanding-accounting for
anything that needs to visibly move while a sentence is spoken (a
probability bar, a forecast cone widening, a sample space filling in).

---

## 4. `asc-filing-data` — concrete numbers for measurement/construct validity

The paper "What Binds" (`/home/mjbommar/projects/personal/asc-filing-data/`)
is a ready-made worked example for the "communicating uncertainty" video's
point that **an instrument can measure something other than what it's
assumed to measure** — exactly the construct-validity idea this project's
research catalog already tracks (van der Bles et al. 2019; Spiegelhalter
2017). Five numbers, each with an exact quoted sentence and file reference:

1. **"ASC 230 is tagged by 99.2% of filers and discussed by 0.8%. The only
   topic discussed more than tagged is ASC 360, which carries impairment —
   an estimate, so it is narrative."**
   File: `/home/mjbommar/projects/personal/asc-filing-data/README.md`.
   Why it works: a single sentence contrasting a mechanical, mandated
   disclosure (tagged almost universally, discussed almost never) against a
   judgment-call disclosure (the opposite pattern) — the cleanest
   demonstration that "tagged" and "discussed" are different constructs.

2. **The exact gap table** (`docs/DESIGN.md`): ASC 230 is `+98.4` percentage
   points (tagged minus discussed); ASC 360 is the only **negative** row,
   `-2.3` points (5.5% tagged vs. 7.8% discussed). Quoted line immediately
   following: "Nearly every filer *applies* ASC 230 and almost none *writes
   about* it. The topics where prose meets or exceeds tagging are the
   judgmental ones — 360 carries impairment, which is narrative because it
   is an estimate."

3. **SAB 74 and "mandated anticipation."**
   File: `/home/mjbommar/projects/personal/asc-filing-data/README.md` and
   `docs/DESIGN.md`. Quoted: "SAB 74 (ASC 250-10-S99-5) requires disclosure
   of issued-but-not-yet-effective guidance, so the instrument fires when the
   FASB acts, not when firms apply. The series measures mandated
   anticipation." With the supporting numbers: "ASU citation mass is 53%
   before the effective period and only 23% after," and "breadth decays for
   standards that indisputably still bind: ASC 606 falls from 85.4% (2018)
   to 54.5% (2023)." This is the single best example for a script: a
   citation-count series designed to proxy for *adoption* instead tracks a
   specific SEC rule's anticipatory-disclosure requirement.

4. **The construct-validity failure, stated in the project's own words.**
   File: `/home/mjbommar/projects/personal/asc-filing-data/docs/QA_LOG.md`.
   Quoted: "Tested against six externally-documented standard timelines: 1
   PASS, 3 PARTIAL, 2 FAIL. **The construct did not survive.** Superseded
   topics co-peak with successors instead of mirroring them: corr(606,605) =
   +0.90, corr(842,840) = +0.88." This is an unusually blunt, quotable
   admission of a failed validation check — good as the "here is what it
   looks like when a measure gets checked against reality and fails" beat.

5. **The 2009 Codification handover, as a contrast case.**
   File: `/home/mjbommar/projects/personal/asc-filing-data/README.md`.
   Quoted: "ASC citation goes from 1.1% to 70.9% of filers in fiscal 2009
   while legacy citation holds at 97.3% — 68.5% of all filers use both
   vocabularies in the same document. 13.4% were still citing superseded
   standards four years later." A second, independent instance of "the
   measure doesn't cleanly capture the transition everyone assumes it
   captures" — useful if the video needs a second, contrasting example.

Framing line worth using as connective narration ahead of these numbers
(same file): "Existing measures of accounting complexity proxy for how much
of GAAP binds a firm without observing it — weighting standards by length,
or counting XBRL tags without mapping them to the guidance they implement."

---

## 5. `fasb-asc-site` — local ASC text, and a licensing caveat that matters

### What's there

`/home/mjbommar/projects/personal/fasb-asc-site/src/data/subtopics/*.json`
stores full ASC paragraph text (548 subtopic files, 23,898 source paragraphs,
citation-keyed, HTML fragment per paragraph) plus a 1,287-term glossary
(`src/data/glossary.json`). ASC 450 (contingencies), ASC 820 (fair value),
and ASC 275 (risks and uncertainties) are all present as full retrievable
text, not just an index — see §6 below for the exact quotes this project can
use.

### The licensing caveat — read before using this repo's data as an input

`fasb-asc-site`'s own `docs/legal/faf-codification-license-agreement-2024-10-10.txt`
is FAF's actual license for the source Codification, and it contains a
clause that matters directly for this project's pipeline, independent of any
copyright fair-use question:

> Clause 3(b) ("Artificial Intelligence") prohibits using any portion of the
> Codification "in connection with any artificial intelligence or machine
> learning technology ... or large language models (LLMs) ... under any
> circumstances," including as training data or to build, train, fine-tune,
> or create AI services, software, derivative works, or compilations.

**This is a contractual restriction on the source material fasb-asc-site's
JSON was scraped under, separate from copyright.** It means:

- **Do not** feed `fasb-asc-site`'s JSON data files into any `bc-llm` or
  `bc-research` call (summarization, research synthesis, structured
  extraction, or any other AI-driven processing) as part of this project's
  pipeline.
- **Do** quote a handful of specific, short definitional passages by hand,
  written directly into `research/SOURCES.md` and narration by a human
  script writer, the same way a print book quotes a short passage of a
  copyrighted standard for educational commentary. That is a materially
  smaller, more conventional fair-use case than fasb-asc-site's own
  "faithful publication of the complete current substantive Codification"
  theory (`src/pages/position/index.md`), which that site built specifically
  to justify *whole-Codification* republication and does not need to be
  invoked here.
- This project's own `research/catalog.yaml` already has independent,
  non-fasb-asc-site sources for the same underlying standards — the FASB's
  own public superseded-standard summaries (`fasb-summary-statement-5`,
  `fasb-summary-statement-157`, `fasb-summary-fin-48`). Prefer those as the
  cited source where a summary suffices; use the exact paragraph quotes in
  §6 below (independently reproduced here, not re-scraped by any pipeline
  code) only where the video needs the precise defining sentence.

---

## 6. Accounting and law examples of uncertainty vocabulary

Exact quoted text for scripts that want a real, sourced example of
regulatory language calibrating uncertainty. All paragraph text below is
independently reproduced by hand from
`/home/mjbommar/projects/personal/fasb-asc-site/src/data/subtopics/`, cross-
referenced against `/home/mjbommar/projects/personal/understanding-accounting/`'s
own corpus notes (which paraphrase these same paragraphs without reproducing
them verbatim, per that project's own copyright caution). See §5 above before
writing any tooling that re-fetches this text programmatically.

### ASC 450 — Contingencies: probable, reasonably possible, remote

File: `fasb-asc-site/src/data/subtopics/450-20.json`

> 450-20-25-1: "When a loss contingency exists, the likelihood that the
> future event or events will confirm the loss or impairment of an asset or
> the incurrence of a liability can range from probable to remote. ... The
> Contingencies Topic uses the terms probable, reasonably possible, and
> remote to identify three areas within that range."

Glossary definitions (`fasb-asc-site/src/data/glossary.json`):

> **Probable**: "The future event or events are likely to occur."
> **Reasonably Possible**: "The chance of the future event or events
> occurring is more than remote but less than likely."
> **Remote**: "The chance of the future event or events occurring is
> slight."

This is a three-level, unquantified verbal probability scale, defined by a
regulator, used to decide whether to recognize a loss or merely disclose it.
It's a strong parallel to the "words of estimative probability" material
already in `research/catalog.yaml` (Kent 1964; ICD 203) and a natural example
for the "communicating uncertainty" video: regulators, like intelligence
analysts, have had to invent verbal probability tiers and then argue about
where the boundaries fall.

### ASC 820 — Fair Value Measurement: the three-level hierarchy

File: `fasb-asc-site/src/data/subtopics/820-10.json`

> 820-10-35-40 (Level 1): "Level 1 inputs are quoted prices (unadjusted) in
> active markets for identical assets or liabilities that the reporting
> entity can access at the measurement date."
> 820-10-35-47 (Level 2): "Level 2 inputs are inputs other than quoted
> prices included within Level 1 that are observable for the asset or
> liability, either directly or indirectly."
> 820-10-35-52 (Level 3): "Level 3 inputs are unobservable inputs for the
> asset or liability."

A clean example for the "epistemology of measurement" thread: a value can be
*known* (an actual traded price), *inferred* (observable but not directly
quoted), or *estimated* (a model with no market check at all) — three
different epistemic statuses, ranked, with financial statements required to
disclose which level any given number came from.

### ASC 275 — Risks and Uncertainties

File: `fasb-asc-site/src/data/subtopics/275-10.json`

> 275-10-50-8: "Disclosure regarding an estimate shall be made when known
> information ... indicates that both of the following criteria are met: a.
> It is at least reasonably possible that the estimate ... will change in
> the near term due to one or more future confirming events. b. The effect
> of the change would be material to the financial statements."

A good example of the general pattern this project's videos are about: not
every uncertainty is worth reporting, only the ones both likely enough to
change and large enough to matter — a two-part materiality-and-likelihood
gate.

### ASC 740 — Income Taxes: more-likely-than-not

File: `fasb-asc-site/src/data/subtopics/740-10.json`

> 740-10-25-6: "An entity shall initially recognize the financial statement
> effects of a tax position when it is more likely than not, based on the
> technical merits, that the position will be sustained upon examination.
> The term more likely than not means a likelihood of more than 50
> percent."

A rare case of a regulator giving a verbal probability term an *exact*
numeric threshold (more than 50%) rather than leaving it to judgment —
worth contrasting directly against ASC 450's unquantified "probable" in a
script about how differently the same kind of institution can choose to
calibrate the same kind of word.

### ASC 360 — Impairment (an estimate, not a fact)

File: `fasb-asc-site/src/data/subtopics/360-10.json`

> 360-10-35-17: "An impairment loss shall be recognized only if the carrying
> amount of a long-lived asset (asset group) is not recoverable and exceeds
> its fair value. ... An impairment loss shall be measured as the amount by
> which the carrying amount of a long-lived asset (asset group) exceeds its
> fair value."

Pair this directly with `asc-filing-data`'s finding (§4 above) that ASC 360
is the one topic discussed in prose more than it is tagged — because it is
an estimate, not a mechanical calculation, accountants write sentences about
it instead of just filling in a number. That pairing (the rule, then the
empirical proof that filers treat it as narrative) is a complete, sourced
beat for a script.

### asc-filing-data's numbers (see §4 for full quotes and file references)

- ASC 230: 99.2% tagged, 0.8% discussed (+98.4 point gap).
- ASC 360: 5.5% tagged, 7.8% discussed (-2.3 points — the only negative row).
- SAB 74 citation mass: 53% before a standard's effective date, 23% after.
- ASC 606 citation breadth: 85.4% (2018) down to 54.5% (2023), despite still
  being in force.
- Construct-validity check: "the construct did not survive" — corr(606,605)
  = +0.90, corr(842,840) = +0.88 (superseded and successor standards
  co-peak instead of trading off).
- 2009 Codification handover: 68.5% of filers used both the old and new
  citation vocabulary in the same document; 13.4% were still citing
  superseded standards four years later.

---

## 7. `bc-modules` — see `docs/BC-MODULES-API.md`

The full verified call inventory, organized by production stage (research,
script, speech, sfx/music, images, frames, timeline, assemble, master,
captions, QA), lives in `docs/BC-MODULES-API.md`. The single most important
fact from that inventory for planning this project's pipeline:
`bc_gen.SpeechVerifier`'s default thresholds (WER <= 0.10, CER <= 0.05) are
identical to the thresholds understanding-accounting's own hand-built
verification gate shipped — this project gets that exact, already-calibrated
gate for free by calling `bc_gen.generate_verified` instead of writing a new
one.
