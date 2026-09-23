# Production log

What was built, what worked, what in `bc-modules` was missing or broken and
how each was handled, and what it cost. Newest first.

## 2026-09-23: video 2, "From evidence to forecast"

`videos/02-from-evidence-to-forecast`: 38 segments plus end card, 995 words,
399.4 s (6:39), 11,981 frames. Every machine QA gate passes (`publish/qa.md`):
worst narration WER 0.059, -16.05 LUFS / -1.32 dBTP muxed, 152 containment
renders clean, 101 caption cues valid. Human review: pending.

New scenes in `pipeline/scenes_02_from_evidence_to_forecast.py` (one import
line added to `scenes.py`): `icon_array` (1,000 people built over three
segments with a `step` parameter), `cube_three_ways`, `interval_rows` (a dot
for one probability, a bar for a range, a `then` morph on a beat),
`big_number`, `card_row` (optional images and a dashed "ghost" card),
`induction_gap`, `sort_table` (one row per segment via `upto`), `bars`,
`calibration`, `ellsberg_urn`, `divergence`. A `steady: true` parameter keeps
the heading from fading in again when a picture continues across segments.

### Pipeline bug fixed

- **`qa.containment` crashed instead of failing.** `ok` was a numpy bool
  (the bbox coordinates are `np.float64`), so `json.dumps` of the report
  raised `TypeError` whenever any render spilled outside the stage, and the
  QA stage died without writing `qa.md`. Fixed with `bool(...)` in
  `pipeline/qa.py`; `tests/test_qa.py` reproduces it with a scene that spills.

### What looking and listening changed

- The first cut read "8%" where the answer is 7.8% (`probability_bar` rounds
  its label); the Bayes result and the physicians' 70 to 80 percent moved to
  `big_number` (with `decimals`, and `count: false` so a probability does not
  count up from zero) and `interval_rows`.
- Stages that stayed empty until a late beat (the icon array, the urn, two
  bar charts, the tournament cards) now start on an earlier phrase or on the
  reveal.
- The shared `spaghetti_plot` fans out from the first step, which contradicts
  "tight at 30 hours"; Lorenz and the 26 May 2017 case use `divergence`.
- Whisper-1 on the master heard "Alan Hodgik" for Hajek despite a `direction`;
  the name moved from narration to the on-screen kicker.
- A 2-card `icon_grid` grew to the full stage height and its entrance slide
  left the stage (containment caught it); Betty's cards moved to `card_row`.

### Cost

$0.2468 of generations by receipts (38 narration clips, 5 images including
one unused `oil_barrel` from a cut segment and a redrawn `witness`, 6 effects,
one music bed), plus QA and verifier transcription.

## 2026-09-23: video 1, "Two kinds of not knowing"

`videos/01-two-kinds-of-not-knowing`: 13 segments plus end card, 459 words,
176.7 s, 5,302 frames. Every machine QA gate passes (`publish/qa.md`): worst
narration WER 0.000, -16.05 LUFS / -1.57 dBTP muxed, 52 containment renders
clean, 40 caption cues valid. Human review: pending.

- **New scenes** in `pipeline/scenes_01_two_kinds_of_not_knowing.py`
  (imported by one line at the end of `scenes.py`): `object_cards`
  (generated objects on cards, a cycling "next roll" ticker, a grid of
  insured buildings where a different one is lit each second), `sort_bins`
  (Keynes's 1937 list into two columns), `stacked_bars` (Ellsberg: two
  chances that add up to less than one), `range_bar` (a fixed point against a
  marker that wanders over 0 to 1), `level_scale` (Marchau's scale from
  complete certainty to total ignorance; `intro: false` keeps the track
  settled when the next segment continues it). All pass `tests/test_scenes.py`.
  No other file in `pipeline/` was changed.
- **Fixed after looking at frames** (four rebuilds, all cached except QA):
  empty stages under the heading for 4 to 5 s at the start of s05, s09 and
  s10 (reveals moved to the first beat); `stacked_bars` gap outline arriving
  before the bars because a fifth beat fell back to the default spacing
  (beats now explicit per row and part); the ambiguity frame showed "50%"
  for Urn I (replaced by `range_bar`); s13 re-drew the whole scale from zero
  at the cut (now `intro: false`); Keynes chips flew across earlier chips on
  their way into a column (now a short slide into their own slot); gradient
  seams on the scale track; the gap label colliding with the "1" tick.
- **Listening.** The master was transcribed again with whisper-1 (independent
  of QA's gpt-4o-transcribe) and matched the script. Names were cut out and
  transcribed alone, with no context: whisper-1 heard the isolated "Keynes"
  as "canes", the correct pronunciation; Ellsberg and Knight were heard as
  written. No respelling was needed.
- **Knight citation.** The fire-insurance example and "far too unique" are in
  Knight's Ch. VII, which is only in [S02] (FRASER scan, checked against the
  raw PDF text layer, book pp. 213 and 231; `tools.py verify` finds it on PDF
  page 223 but not in the scrambled markdown). The definitions of risk and
  "true" uncertainty are cited to [S76]. s05 and s06 therefore cite both.
- **Cost.** First build $0.087 (13 TTS clips, 7 SFX, 6 images; the music bed
  was a cache hit from the smoke video's identical prompt), four rebuilds at
  about $0.010 each (QA transcription), listening transcriptions about $0.02.
  About $0.15 in all. Generations the video uses are worth $0.202 by receipt.

## 2026-09-23: pipeline and smoke video

Built `pipeline/` (spec, brand, canvas, scenes, speech, sound, images,
audio_post, timeline, render, build, qa, gallery, audition, sheet) and
`tests/` (64 tests, no network). Built `videos/_smoke` end to end: 5 segments
plus end card, 36.6 s, 1,098 frames. All machine QA gates pass
(`videos/_smoke/publish/qa.md`). Human review: pending.

### What worked

- **Frame rendering.** A retained-geometry `bc_viz.Canvas` per layer,
  rasterised by resvg with only the brand's font files, composited with
  `bc_image.over`: about 15 ms a 1080p layer. The whole 36.6 s video renders
  and encodes in 16.5 s wall on 18 workers. 4K is the same drawing code at
  `scale=2` (0.49 s for one cold frame).
- **Live transitions.** Rendering both scenes at the same programme time and
  blending them with `bc_motion.render_transition` means nothing freezes at a
  cut. A frame-difference scan of the decoded MP4 found no identical
  consecutive frames and no large change away from a transition.
- **Timeline from processed clips.** The per-clip chain runs before the
  timeline, so the timeline is built from the lengths that are actually
  placed; the track matched it to the sample (drift 0.000 s).
- **Narration.** Gemini 3.8 Flash TTS (Charon) passed the ASR gate on the
  first draw for all 5 smoke clips and all 12 audition clips. Session spread
  after `SessionMatcher`: 0.049 LU.
- **Mastering.** -16.00 LUFS, -1.70 dBTP, LRA 2.35 LU on the WAV master;
  -16.04 LUFS and -1.69 dBTP re-measured from the muxed AAC.
- **Containment test.** It caught three real faults on first run
  (`histogram_of_answers` 100% label, `timeline_strip` first label,
  `two_column_compare` entrance slide below the stage), all fixed.
- **Icon keying.** `gpt-image-2.5-flare` followed the two-colour house style;
  white keyed to alpha with colour un-premultiplied gives clean edges on the
  ink ground.

### What was missing or broken in bc-modules, and what was done

1. **bc-gen: prices missing** for `gemini-3.8-flash-tts`,
   `gemini-3.8-flash-lite-tts`, `gpt-image-2.5-flare` and
   `gpt-image-2.5-sunburst`. genai-prices fuzzy-matched the 3.8 TTS ids to the
   3.8 Flash *text* rates. **Changed in bc-modules (uncommitted there):**
   four dated entries in `bc-gen/python/bc_gen/data/prices.json` with sources
   in `data/SOURCES.md`.
2. **bc-gen: `PriceTable.image_usage` ignored the overlay for OpenAI images**
   (it consulted the overlay only when `output_image_tokens` was passed, which
   `OpenAIImage` never does), so a new OpenAI image model was unpriced even
   with an overlay entry. **Changed in bc-modules:** a 7-line branch in
   `pricing.py` that prices OpenAI `output_tokens` at the overlay's
   `output_image_per_mtok`; a test for it; and the overlay test's pinned read
   date loosened to "an ISO date on or after 2026-09-22". bc-gen's 72 unit tests
   pass; ruff is clean.
3. **bc-gen: `GeminiSpeech` cannot drive Gemini 3.8 TTS.** Measured: the
   anti-answer wrapper is spoken aloud and the script is not, a system
   instruction is refused, and the response is a RIFF WAV that `_pcm16_to`
   would decode as PCM (a click at the head). **Not changed in bc-modules**
   (more than a one-line fix). The pipeline has
   `pipeline.speech.GeminiStyledSpeech`, a `bc_gen.ProviderBackend` subclass
   (about 60 lines) that posts to `/v1beta/interactions` with the delivery in
   `speech_metadata.style` and keeps bc-gen's key, receipt, retry, pricing and
   verify-then-cache. **Upstream candidate:** move it into bc-gen as
   `GeminiSpeech(model="gemini-3.8-...")` switching endpoint by model.
4. **bc-gen: the verifier's transcription cost is not in any receipt.**
   `SpeechVerifier` spends on `OpenAITranscribe` for every draw, and nothing
   records it. The pipeline wraps the transcriber (`MeteredTranscriber`) and
   books the spend in `output/costs.json`. Upstream candidate: a
   `verify_cost_usd` field on `Receipt`.
5. **bc-gen: no WER on a passing receipt.** `Verdict.score` is dropped when a
   clip passes, so the ledger cannot show how close a pass was. The pipeline
   re-scores the last transcript it heard. Upstream candidate: store
   `verdict.score` in the receipt.
6. **bc-audio: `compressor` is mono only**, and the docs do not say so. The
   pipeline's `audio_post.duck` runs it per channel with one shared key,
   which is exactly a linked stereo duck because the gain depends only on the
   key.
7. **bc-viz: no letter-spacing, no italic selection, no embedded images.**
   Tracked small caps are drawn a glyph at a time (`scenes.tracked`); quotes use
   the upright display face; images are composited by `bc_image` as their own
   layer. Upstream candidates: `letter_spacing=` and `style=` on `text`.
8. **OpenAI ASR (`gpt-4o-transcribe`) truncated one transcript** of an intact
   clip (it returned the first sentence only; the same file re-transcribed
   whole). QA now hears a failing segment a second time and records both
   hearings. Worth watching: a truncation during *generation* would re-roll
   a good clip and spend money for nothing.

### Decisions

- Images: `gpt-image-2.5-flare` (the asked-for gpt-image-2.5 exists); no
  Gemini 3.8 image model exists, so `gemini-3.1-flash-image` is the fallback.
- Narrator: `gemini-3.8-flash-tts`, Charon (see `MODELS.md`), on machine
  measures only. **Listen before the first real episode.**
- Loudness: -16 LUFS integrated, -1.5 dBTP, stereo 48 kHz (a house choice for
  YouTube, which publishes no target and normalises down to about -14).
- Ducking: gentle. The first pass ducked effects by up to 15 dB and the bed by
  22 dB, which buries a cue that fires mid-sentence; now at most about 9 and
  7.5 dB.

### Costs so far

| Item | USD |
|---|---|
| Voice audition: 12 TTS clips (6 on 3.8, 6 on 3.1) | 0.0467 |
| Audition ASR verification | 0.0053 |
| Smoke narration: 5 clips | 0.0095 |
| Smoke verifier ASR | about 0.0025 |
| Smoke SFX: marbles 1.6 s, whoosh 1.0 s | 0.0052 |
| Smoke music bed: one Lyria 30 s clip | 0.0400 |
| Smoke icon: gpt-image-2.5-flare, 1024x1024 medium | 0.0137 |
| QA transcription, three QA runs | about 0.0060 |
| Probe calls (3.8 TTS behaviour tests, debug transcriptions) | about 0.0050 |
| **Total** | **about 0.134** |

The smoke video's generations are worth $0.070 by their receipts; a rebuild
of the unchanged script costs $0.0019 (QA transcription only).

### Known gaps

- No human has watched or listened to anything yet.
- The music bed and effects have not been judged by ear; levels were set by
  measurement (bed about 14 LU under narration before ducking).
- `GeminiStyledSpeech` should live in bc-gen (item 3).
- `research/SOURCES.md` keys are checked for existence, not for whether the
  cited passage supports the sentence.
- Scenes not in the smoke video (`cone`, `ladder`, `dial`, `distribution`,
  `histogram_of_answers`, `quote_card`, `icon_grid`, `timeline_strip`,
  `two_column_compare`) are only gallery- and test-verified, not seen in motion.
- No chapter markers, no YouTube description writer, no upload.
- 4K has been rendered frame by frame, not assembled end to end.
