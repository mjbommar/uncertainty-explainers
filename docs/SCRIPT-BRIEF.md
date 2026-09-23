# Script and production brief

One agent owns one video, end to end: script, storyboard, generated assets,
build, QA, review, fixes. Read, in this order: `AGENTS.md`, `docs/VOICE.md`,
`docs/guides/SIMPLIFIED-ENGLISH.md`, `docs/guides/STYLE.md`,
`docs/guides/STYLE-AI-TELLS.md`, `docs/PIPELINE.md`, `docs/MODELS.md`,
`docs/PRODUCTION-LOG.md`, `research/SYNTHESIS.md`, then the `research/notes/`
files for your video and `research/SOURCES.md` for the keys. Look at
`videos/_smoke/script.yaml` and `videos/_smoke/publish/poster.png` and
`videos/_smoke/output/qa/cuts.png` to see what the pipeline already produces.

## The series

| # | Slug | Title | Target | Thesis |
|---|---|---|---|---|
| 1 | `01-two-kinds-of-not-knowing` | Two kinds of not knowing | 2.5 to 3.5 min | Some uncertainty is chance and some is ignorance; some can be measured and some cannot. The first job of a forecast is to say which kind it faces. |
| 2 | `02-from-evidence-to-forecast` | From evidence to forecast | 6 to 7 min | A probability is a disciplined summary of evidence, not a fact about the world. It must be honest about its reference class and its width, and stated so it can be scored. |
| 3 | `03-saying-it-out-loud` | Saying it out loud | 9 to 10 min | Uncertainty is not communicated until the listener holds the number the speaker meant. Pair every word with a number, a reference class, and a statement of confidence. |

Beats for each video are in `research/SYNTHESIS.md` section (g). Video 1 is
short by design: cut it to the four strongest beats (die and envelope, Knight,
Keynes "we simply do not know", Ellsberg's urn, one closing line on the ladder
to total ignorance). Each video stands alone. The end card of 1 names 2, the
end card of 2 names 3, the end card of 3 names the series.

Shared settings: `theme: ink`, voice `gemini-3.8-flash-tts` / `Charon`, series
label "Uncertainty Explainers", music bed on, burned captions on. Narration
pace plan: 140 words a minute delivered, so a 3 minute video is about 420
words and a 10 minute video about 1,400.

## Writing rules that matter most

- Simplified Book English. Plain, direct, patient, a little dry. Define every
  technical term at first use, in the sentence where it appears. One term per
  concept for the whole video.
- Speak numbers as words where a listener hears them ("three in ten"), but the
  on-screen scene shows the numeral.
- No em dashes anywhere in `say`. No "e.g.", "i.e.". No rhetorical questions
  in a row. No "imagine", "let's dive in", "in this video". No closer that
  restates. Sentences average 12 to 18 words, ceiling 28, varied on purpose.
- Every factual sentence carries `sources: [Sxx]` and the source actually
  supports it. Read the note and the source markdown; do not cite from
  memory. Quotes are verbatim from `research/sources/*.md`; run
  `uv run python research/tools.py verify` if the tool supports the quote.
- Refer to the screen only when it helps: "On the left, Urn A."
- Run `uv run scripts/check_prose.py`, `check_style.py`, and
  `check_simplified.py` on the narration (see `docs/VOICE.md`), and fix what
  they report before voicing.

## Visual rules

- Every segment has a scene that changes with the sentence. Reveals land on
  `beats`. Nothing is static for more than two seconds.
- Use generated images (gpt-image-2.5-flare via `images:`) for objects that a
  vector scene cannot draw well: a die, a sealed envelope, an insured house,
  copper ingots, a hurricane, an urn if the vector one is not enough. House
  style is applied by the pipeline. Two to six images per video.
- Sound: a cue on the beat that matters (a die roll, a page turn, a soft
  tick), never on every sentence. Two to eight cues per video.
- If you need a scene that does not exist, add it in a new file
  `pipeline/scenes_<slug>.py` with the `@scene` decorator, and import that
  module with one added line at the end of `pipeline/scenes.py`. Re-read
  `scenes.py` immediately before editing it, because two other agents may add
  their own line. Do not otherwise edit `pipeline/` except to fix a bug you
  can prove with a test; log any such fix in `docs/PRODUCTION-LOG.md`.

## Done means

1. `--stage check` passes with the estimate inside the target range.
2. The build runs all stages and `output/qa.md` shows every gate green:
   frame count, loudness -16 LUFS / -1.5 dBTP, ASR round trip within limit
   for every segment, containment, captions valid.
3. You have looked at `output/qa/cuts.png`, the gallery of your new scenes,
   and at least ten decoded frames spread through the video, and fixed
   anything ugly: overlap, clipping, poor contrast, a still frame, a reveal
   that lands off its beat. Then you rebuilt and looked again.
4. You have listened for problems the machine cannot see: transcribe the
   master and read it against the script for mispronounced terms or names
   (Keynes rhymes with "canes"; Knight; Ellsberg; Bayes rhymes with "days";
   Brier rhymes with "higher"). Fix with a `direction` or a respelling.
5. `videos/<slug>/publish/` holds the MP4, VTT, poster PNG, `qa.md`, and a
   `youtube.md` (title, description with sources, chapters by segment).
6. `videos/<slug>/storyboard.md` lists every segment: say, scene, image, sfx,
   sources, seconds.
7. Commit only your paths (`git add videos/<slug> pipeline/scenes_<slug>.py
   pipeline/scenes.py docs/PRODUCTION-LOG.md`), never `git add -A`. If
   `index.lock` exists, wait and retry. Do not push.

Record the cost from `output/costs.json` in your report.
