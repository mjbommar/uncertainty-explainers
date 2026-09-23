# VOICE — a working brief for narration

One page for anyone writing `script.yaml` narration text for these videos.
It distills `docs/guides/SIMPLIFIED-ENGLISH.md`, `STYLE.md`, `STYLE-CRAFT.md`,
and `STYLE-AI-TELLS.md` into rules for words that get *spoken*, not read, plus
how davinci-math adapted the same house style for a narrated, on-screen
medium. Read the four guides for the full reasoning; this page is the
checklist you keep open while drafting.

## The listener

An adult general reader, per SIMPLIFIED-ENGLISH.md §1: fluent in English, not
a specialist in probability, logic, or accounting, hearing the sentence once,
with no chance to re-read it. That last part is the whole difference from a
book. A reader can stop and re-read a dense sentence. A listener cannot. Every
rule below follows from that.

## Sentence and paragraph shape

- **12 to 18 words average, 30-word hard ceiling** (AGENTS.md Rule 1; this is
  the guides' range for guides/instructional prose, STYLE.md §3). Spoken
  narration is closer to instruction than to narrative nonfiction: pick the
  guides/instructional targets, not the 15-20/35 narrative ones.
- **Vary length on purpose.** A run of same-length sentences is as audible as
  it is readable — maybe more, since the listener has no punctuation to see.
  Use the short/medium/long bands in STYLE.md §3: an ultra-short sentence
  (1-5 words) after a longer one is the single best way to land a point in
  narration.
- **One idea per sentence.** If narration needs "and" to join two separate
  claims, split it into two sentences and let the pause between them do the
  work a comma would do on the page.
- **Front-load the claim.** The first few words should tell the listener what
  the sentence is about, because there is no way to skim ahead and check.
- **2 to 5 sentences per narration block** (STYLE.md §4, guide-length
  paragraphs). A scene's narration block is one beat; give it one point, one
  piece of evidence, one implication, then cut to the next beat or the visual.

## Terms: one per concept, defined where it is first spoken

- **Define every technical term at first use, out loud, in the same breath**
  (AGENTS.md Rule 1; SIMPLIFIED-ENGLISH.md R4). There is no glossary a
  listener can flip to and no bold `\keyterm` markup to lean on — the
  definition has to be spoken prose. Use SIMPLIFIED-ENGLISH.md's Route 1
  pattern: an appositive, a "that is" clause, or a colon, right where the
  term lands.
  - Written for print: "A **credible interval** is the Bayesian analogue of
    a confidence interval."
  - Spoken for narration: "Statisticians call this range a credible
    interval. It says how sure we are, given what we saw."
- **One name per concept, book-wide** (SIMPLIFIED-ENGLISH.md R2). Across all
  three or four videos, pick one term for "epistemic uncertainty" and use
  only that term. Do not alternate with a synonym for variety — that is the
  one place synonym-hunting actively hurts a listener, because it suggests a
  second concept exists.
- **One concept per term** (R3). Do not let "probability" mean both the
  formal Kolmogorov object and the colloquial "chances" in the same script.
  If the script needs both senses, name them differently the first time.
- **Expand abbreviations the first time they are spoken**, in full prose, not
  as a parenthetical the ear can't hear: "the Financial Accounting Standards
  Board — FASB for short" rather than "FASB (Financial Accounting Standards
  Board)," which only works on a page.
- **Concept load: about 5 to 7 new terms per video**, not per chapter
  (SIMPLIFIED-ENGLISH.md §5, STYLE.md §7). A 3 to 10 minute video is closer
  to one chapter than to a book; treat the pacing target as a per-video
  budget, not a per-scene one.

## Numbers, read aloud

- **Write numbers the way they should be spoken**, not the way they'd be
  typeset. "About one in six" reads fine in narration; "16.7%" does not,
  because whoever voices or synthesizes the line has to silently convert it
  first. Do the conversion at script-writing time and let the pipeline's TTS
  notation rules (see `docs/BC-MODULES-API.md`, bc-gen `speech.py`) handle
  only genuine edge cases, not routine style.
- **Round for the ear** (STYLE.md §6): "about 800,000 homes," not
  "798,412 homes," unless the exact figure is the point (a specific year, a
  specific vote count).
- **Every statistic gets a spoken source and a spoken comparison** in the
  same breath: "The 2019 Royal Society review found that..." and "enough to
  power a city the size of..." A bare number spoken alone is the single
  fastest way to lose a listener, because there is nothing to anchor it to
  while the next sentence is already arriving.
- **No mushy dates.** "Recently," "in recent years," and "these days" are
  banned in the written guides for the same reason they are worse spoken:
  say "since 2020" or "in the 2019 review."
- **Spell out one to ten in narration text**, numerals for 11 and up, per
  STYLE.md §6 — this only matters for how the writer reads the draft; the
  TTS layer speaks either form the same way.

## No machine tells, especially the ones that show up in narration

Everything in STYLE-AI-TELLS.md applies, and a few tells are worse spoken
than written because the listener cannot see the em dash or the semicolon
that would have signaled "this is a list, not a thought":

- **No em dashes in narration** (AGENTS.md Rule 1, absolute — stricter than
  STYLE.md's "one per paragraph" print rule). Use a full sentence break, a
  colon, or a comma instead. A listener can't tell an em dash from a comma;
  writing one only produces run-on prose when it's read aloud.
- **No filler transitions**: no "furthermore," "moreover," "that said,"
  "moving forward." Cut them; the pause between sentences already marks the
  transition.
- **No summary openers or closers**: never "In this video, we'll explore...''
  and never "So, to sum up...". Start on the claim. End on the last new
  fact or the question the next video answers (STYLE-CRAFT.md §8).
- **No rhetorical-question transitions** ("So what does this mean? It
  means..."). Just state what it means.
- **No triadic padding.** Don't force three examples when two make the
  point and a third is filler — three take longer to say than to read, and
  narration has a hard runtime budget a book doesn't.
- **No hedge clusters** ("might possibly," "could potentially"). Hedge once,
  specifically, and only for real uncertainty — appropriate irony, since
  this project's whole subject is calibrated uncertainty language (see
  `research/catalog.yaml`, Kent 1964 and the IPCC guidance note entries).
- **No "testament to / underscores / plays a crucial role"** abstraction
  verbs. State the fact.

## How to refer to what's on screen

Borrowed directly from davinci-math's `docs/VOICE.md`, adapted for scene
based video rather than a lesson page: **do not speak production
vocabulary.** Never say "in this scene," "this animation shows," "the
diagram on screen," or any word that names how the video was made. Only
describe a visual when the description itself carries information the
listener needs, and then describe it the way a person would, not the way a
storyboard would:

- Avoid: "In this animation, we see a diagram of a Venn diagram
  representing the sample space."
- Prefer: "Picture every possible outcome as one square. The part that's
  shaded is the outcomes where the alarm goes off."

If a scene's visual is decorative or redundant with the narration, don't
mention it at all — let it support the sentence rather than being named by
it.

## The read-aloud test

Before a script is voiced, read the whole narration track aloud, at
speaking pace, without stopping to fix anything on the first pass
(STYLE.md §1, §10). Use the **kitchen-table test**: a friend who hasn't
touched a probability class in twenty years, hearing this over a kitchen
table with no board and no pause button. If a sentence needs a second
listen to parse, or an equation has no spoken meaning attached to it, it
fails, whether or not it passes the checkers below.

## Ten-line checklist

1. Sentences average 12-18 words; nothing over 30; lengths visibly vary.
2. Every technical term is defined out loud, in the sentence it first
   appears in, using one term per concept, all video long.
3. No more than 5-7 new terms in the whole video.
4. Every number is written the way it should be spoken, rounded for the
   ear, and paired with a spoken source and a spoken comparison.
5. No dates without an anchor year; no "recently."
6. Zero em dashes anywhere in narration text.
7. No filler transitions, summary openers/closers, or rhetorical-question
   transitions.
8. No hedge clusters; hedge once, specifically, only for real uncertainty.
9. No production or camera language ("in this animation," "as you can
   see") unless the visual description itself carries needed meaning.
10. Read the whole track aloud at speaking pace; it passes the
    kitchen-table test before it passes any checker.

## Running the checkers on a script's narration

The three checkers in `scripts/` (`check_prose.py`, `check_style.py`,
`check_simplified.py`) were copied from `../book-template`, which checks
`latex/chapters/*.tex` files. This repo has no `latex/` tree — narration
lives in each `videos/<slug>/script.yaml`'s `narration:` fields — so all
three now take explicit file arguments and were verified to run with
`uv run` against plain text.

**Extract narration to a plain-text file first.** Until `pipeline/`
implements a `check` stage (`AGENTS.md`'s `uv run python -m pipeline.build
videos/<slug>/script.yaml --stage check` should do this), pull the
narration strings out by hand or with a one-liner, one sentence-block per
line, e.g.:

```bash
uv run python -c "
import yaml, sys
doc = yaml.safe_load(open(sys.argv[1]))
for scene in doc.get('scenes', []):
    text = scene.get('narration')
    if text:
        print(text)
" videos/<slug>/script.yaml > /tmp/<slug>-narration.txt
```

Then run all three against that file:

```bash
uv run scripts/check_prose.py /tmp/<slug>-narration.txt
uv run scripts/check_style.py /tmp/<slug>-narration.txt
uv run scripts/check_simplified.py /tmp/<slug>-narration.txt
```

**What had to change to make that work, and why:**

- `scripts/check_style.py` previously took no file arguments at all — it
  only ever scanned `latex/chapters/*.tex` (book-template's layout) and
  called `sys.exit` if that directory was empty. It also read `book.yaml`
  unconditionally to look up the book's title and author for the
  literal-metadata check, which does not exist in this repo. Fixed by: (1)
  adding a `files` positional argument that falls back to the old
  `latex/chapters/*.tex` glob only when no files are given, so both this
  repo and any future book-template-style repo work; (2) making `book.yaml`
  optional — when absent, the literal-metadata and style-profile checks are
  skipped and only the base STYLE.md/STYLE-AI-TELLS.md banned-word,
  banned-phrase, tell-pattern, and machine-artifact checks run; (3) wrapping
  the `chapter.relative_to(ROOT)` call in a `try/except` so it can report
  paths outside the repo root (e.g. a `/tmp` scratch file) without
  crashing.
- `scripts/check_simplified.py` imports `converter.latex_source.blank` and
  `.extract_prose` — a TexSoup-based LaTeX prose extractor that lives in
  `../book-template/epub/converter/`, is not a dependency of this project,
  and is not needed here because narration text is already plain prose,
  not LaTeX. Fixed with a `try/except ModuleNotFoundError` around the
  import: when the `converter` package isn't on the path, `blank()` falls
  back to the same same-length-whitespace behavior book-template's version
  has, and `extract_prose()` becomes the identity function (there is
  nothing to strip out of plain text). Everything else in the file already
  handled a missing `book.yaml` gracefully and already accepted explicit
  file arguments, so no other changes were needed.
- `scripts/check_prose.py` needed no changes. It already accepts explicit
  file arguments and does LaTeX stripping via `pydetex`, which is a no-op
  on prose that has no LaTeX in it.
- `check_simplified.py`'s own docstring says to run it with
  `uv run --group sbe scripts/check_simplified.py`. That dependency group
  does not exist in this repo's `pyproject.toml` — `inflect` and
  `simplemma` are already listed as direct project dependencies here
  (unlike book-template, where they live behind an optional group), so
  plain `uv run scripts/check_simplified.py ...` is the correct invocation
  in this repo.

All three were run against a sample narration paragraph as part of this
change and produced clean, non-crashing output.
