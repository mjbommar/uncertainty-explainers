# Pipeline

How a `videos/<slug>/script.yaml` becomes a checked 1920x1080 MP4. The code is
`pipeline/`; every stage composes `bc-modules` (see `AGENTS.md`).

```bash
uv run python -m pipeline.build videos/<slug>/script.yaml --stage check
uv run python -m pipeline.build videos/<slug>/script.yaml            # every stage, in order
uv run python -m pipeline.build videos/<slug>/script.yaml --stage assemble --4k
uv run python -m pipeline.gallery [--theme paper]                    # every scene, four reveal points
uv run python -m pipeline.audition                                   # narrator candidates, measured
uv run python -m pytest -q                                           # no network
```

## Stages

| Stage | Does | Spends | Writes (under `videos/<slug>/output/`) |
|---|---|---|---|
| `check` | Validates the script, estimates length at 150 wpm plus holds and the end card, runs `scripts/check_prose.py` and `check_simplified.py` on the narration | nothing | `check.json`, `narration.md` |
| `timeline` | One narration clip per segment through bc-gen (verified by an ASR round trip before it is cached), the per-clip audio chain, then the timeline and captions from the *processed* clip lengths | TTS + verifier ASR | `clips/*.wav`, `clips.json`, `timeline.json`, `captions.vtt`/`.srt`, `motion_ledger.json`, `timeline_summary.json` |
| `audio` | Sound effects and the music bed through bc-gen, the mix with ducking, mastering to -16 LUFS / -1.5 dBTP, and the drift assertion against the timeline | SFX + music | `master.wav`, `mastering.json` |
| `frames` | Generates images, renders three stills per segment for review | images | `frames/stills.png` and PNGs |
| `assemble` | Renders every frame in worker processes, streams them to `bc_motion.encode.assemble` (H.264 High, CRF 14, BT.709, AAC 192k), writes the poster and thumbnail | nothing | `<slug>.mp4` (or `-4k.mp4`), `poster.png`, `thumbnail.png` |
| `qa` | Checks the MP4 itself (below) and copies `qa.md` and `poster.png` to `publish/` | QA transcription | `qa.json`, `qa.md`, `qa/cuts.png`, `qa/segments.png` |

Each stage reads what the stage before it wrote, so any one can be rerun
alone. Every generation is cached, so a rerun of an unchanged script pays only
for QA transcription (the smoke build: 41.7 s wall and $0.0019).

## The script

```yaml
slug: _smoke                     # directory name; a leading underscore marks a test video
title: Risk and uncertainty      # header strip, VTT NOTE, poster fallback
target_seconds: 32               # check warns if the estimate is more than 25% away
theme: ink                       # ink (deep blue-black) or paper (warm off-white)
burn_captions: true              # draw the current cue in the caption band (default true)
voice:
  model: gemini-3.8-flash-tts    # 3.8 models use the styled backend; 3.1 models use bc_gen.GeminiSpeech
  voice: Charon
  # style: ...                   # sustained delivery; defaults to spec.HOUSE_STYLE
music:                           # optional; skipped gracefully if Lyria fails
  prompt: Calm, sparse documentary underscore...
  gain_db: -14                   # relative to narration level, before ducking
images:                          # generated assets, referenced as "image:<id>"
  - id: storm
    prompt: a storm cloud with a single small lightning bolt   # house style is added
    provider: openai             # openai (gpt-image-2.5-flare) or gemini (gemini-3.1-flash-image)
    quality: medium
end_card:
  seconds: 3.5
  line: Risk has odds. Uncertainty does not.
  note: Uncertainty Explainers
segments:
  - id: s02
    say: Urn A holds fifty red and fifty black balls. Urn B holds a hundred balls, in a mix nobody tells you.
    sources: [S05]               # keys in research/SOURCES.md; unknown keys are refused
    transition: dissolve         # into this segment; any of bc_motion.TRANSITIONS
    beats: ["Urn A", "fifty red", "Urn B", "a hundred"]   # phrases -> seconds; scenes stage reveals on them
    sfx:
      - cue: marbles             # a LIBRARY cue, or prompt: + duration:
        at: fifty red            # seconds into the narration, or a phrase from say
        gain_db: -6
    scene:
      name: urn
      params:
        heading: Two urns
        left: {label: Urn A, a: 50, b: 50, caption: "50 red, 50 black"}
        right: {label: Urn B, total: 100, caption: "100 balls, mix unknown"}
    hold: 0.4                    # silence after the narration, seconds
    direction: slower here       # optional, appended to the style for this line only
```

The loader refuses, with every fault in one message: unknown or missing scene
parameters, unknown transitions or cues, an `at` or beat phrase that is not in
`say`, an image reference that is not defined, a malformed or unregistered
source key, an em dash in narration, and any unknown key anywhere.

## Scenes

`pipeline/scenes.py`. Each scene is `draw(frame, box, params, clock, ctx)` and
receives `clock.t` (reveal progress), `clock.local` (seconds into the
segment), `clock.seconds` (programme time, for ambient motion),
`clock.progress`, and `clock.beat(i)` (eased progress since beat *i*). All
scenes accept `kicker` and `heading`.

`title_card`, `two_column_compare`, `urn`, `probability_bar`, `word_ladder`,
`spaghetti_plot`, `cone`, `ladder`, `dial`, `distribution`,
`histogram_of_answers`, `quote_card`, `icon_grid`, `timeline_strip`.
`build/gallery/<theme>.png` shows each at four reveal points.

A segment whose scene and parameters equal the previous segment's is drawn
settled, not re-revealed. Transitions are live: both scenes keep moving while
`bc_motion.render_transition` blends them.

### Adding a scene

1. Write `def my_scene(f, box, p, c, ctx)` in `scenes.py` and decorate it with
   `@scene("my_scene", required=(...), optional=(...), demo={...})`. The demo
   must include every required parameter.
2. Draw only inside `box` (use `header_block` for the heading), colour by
   palette role (`pal.known`, `pal.unknown`, `pal.warn`, `pal.cool`, `pal.text*`),
   type by `brand.DISPLAY` / `TEXT` / `MONO`, and give it one ambient motion on
   `c.seconds` so a settled frame still changes.
3. `uv run python -m pytest -q tests/test_scenes.py` rasterises it at five
   reveal points on both grounds and fails on any ink outside the box, and on
   two identical settled frames a second apart.
4. `uv run python -m pipeline.gallery --scene my_scene` and look at
   `build/gallery/ink/my_scene.png` at full size.

## Brand

`pipeline/brand.py`. Palettes `ink` and `paper` with the same roles; teal
means the counted or known, amber the estimated or unknown, coral a mistake.
Type: DM Serif Display (display, quotations), Inter 400/500/600 (text), IBM
Plex Mono (numbers). Layout: title-safe 120 px sides; header strip at y 56-100
(series label, title, progress rail); stage at y 140-880; the caption band at
y 906-1024 is reserved and no scene may enter it.

## Audio

Per clip, before the timeline: decode to 48 kHz mono; trim silence at each end
(keep 50 ms lead, 140 ms tail); shorten internal pauses over 0.60 s to 0.42 s;
`bc_audio.voice.TTS_NARRATION` (high-pass, levelling compressor, derived
split-band de-esser, band exciter, presence EQ, fades, -18 LUFS, proven -1.5
dBTP); `SessionMatcher` across the set. The programme: narration at each
state's first frame; effects loudness-normalised, placed at their offsets and
ducked gently under the narration key; the bed looped by
`ffmpeg.seamless_bed`, faded and ducked; the sum normalised to -16 LUFS and
true-peak limited to -1.5 dBTP in-core, measured on the BS.1770 meter.

## Caching, receipts and costs

Every generation goes through `bc_gen.generate_verified` with the cache at
`.cache/bc-gen` (not committed): the key is the hash of provider, model,
parameters and prompt, and a file enters the cache only after its verifier
passes (speech: ASR round trip; sound: duration; image: size). A copy of each
receipt goes to `videos/<slug>/assets/receipts/`. Receipts are never edited.

`output/costs.json` is the build's ledger: `spent_usd` is what this run paid
(cache hits are free), `receipts_usd` is what the generations the video uses
cost when they were made, and `unpriced` lists anything the price ladder could
not price. The verifier's own transcription is not in bc-gen's receipts, so
`speech.MeteredTranscriber` counts it separately.

## QA gates, and what "done" means

`qa` checks the delivered MP4, not its sources:

1. Full decode with `ffmpeg -v error -f null`: no errors.
2. Stream: frame count equals the timeline's; 1920x1080 (or 3840x2160), 30
   fps, H.264 High, yuv420p, BT.709 tags.
3. Frames decoded from the MP4 before, at, inside and after every transition,
   on `qa/cuts.png`, plus one mid-segment frame each on `qa/segments.png`.
4. Loudness of the muxed audio: -16 +/- 0.7 LUFS, true peak at most -1.0 dBTP
   (the WAV master is held to -1.5; AAC may lift peaks a few tenths).
5. Narration: each segment's span of the muxed audio transcribed and scored
   against the script, WER at most 0.10 with numbers exact. A failing
   segment is heard a second time before it fails, and both hearings are
   recorded (one ASR truncation was observed on an intact clip).
6. Containment: every scene the video uses, at four reveal points, with no ink
   outside the stage.
7. Captions: the VTT re-parsed and validated.

A video is **done** when all seven pass *and* a person has watched it in full
with sound, looked at `qa/cuts.png` and the segment frames, and changed the
"Human review" line in `qa.md` from pending. Machine gates are evidence for
their gates only.
