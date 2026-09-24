# Uncertainty Explainers

Short animated video explainers on conceptions of uncertainty: how different
kinds of not-knowing connect to epistemology, mathematical probability, logic
and reasoning, and why they matter when we predict or model states of the
world that have not happened, or did not happen.

Built with [bc-modules](https://github.com/mjbommar) for research, generation,
audio post-processing and video assembly. Narration follows Simplified Book
English (`docs/guides/`).

## The videos

| # | Title | Length | Thesis |
|---|---|---|---|
| 1 | [Not knowing comes in different forms](videos/01-two-kinds-of-not-knowing/) | 4:32 | Some uncertainty is chance and some is missing facts; some can be measured and some cannot. Name what you do not know before you name the odds. |
| 2 | [How evidence becomes a forecast](videos/02-from-evidence-to-forecast/) | 7:32 | A probability sums up evidence; it is not a hidden fact in the world. Name its group, update from the base rate, use a range when evidence is thin, and score forecasts over many cases. |
| 3 | [Say what the odds mean](videos/03-saying-it-out-loud/) | 9:56 | Uncertainty is not communicated until the listener holds the number the speaker meant. Give the word, the number, the group, and the strength of the evidence. |

The series is published by [Da Vinci Math](https://math.davincilearner.com/)
([@DaVinciMath](https://www.youtube.com/@DaVinciMath)). Each published MP4
opens with the Da Vinci Math intro (4.2 s) and closes with its outro (7.0 s);
running times above include both.

Each video directory holds `script.yaml` (narration, scenes, sources, sound),
`storyboard.md`, generated assets with their receipts, and `publish/` with the
MP4 (Git LFS), WebVTT captions, poster, `qa.md`, and the YouTube fields:
`youtube.yaml` (the source), `youtube.txt` (the paste-ready upload sheet) and
`youtube.md`.

The argument they rest on is `research/SYNTHESIS.md`, built from 78 sources
registered in `research/SOURCES.md`. Every narrated claim carries a source key.

## How they were made

Every video poses one question, shows its map, visits each stop with a
bridge and a takeaway, and returns to the question (`docs/STRUCTURE.md`).

Narration is Gemini 3.1 Flash TTS (voice Enceladus, paced after verification), checked by transcribing
each clip back and comparing it with the script. Sound effects are ElevenLabs;
the music bed is Lyria; icons and illustrations are gpt-image-2.5. Every
frame is drawn by code in `pipeline/scenes*.py`, mastered to -16 LUFS and
-1.5 dBTP, and assembled with `bc_motion`. `docs/PIPELINE.md` describes the
stages and gates; `docs/MODELS.md` records the model choices;
`docs/TOOLING-REPORT.md` records what worked and what did not in bc-modules.
Generation cost for all three videos was under $1.

## Build

```bash
git lfs install && git lfs pull   # the published MP4s
uv sync                              # needs ../../bc/bc-modules checked out
uv run python -m pipeline.build videos/<slug>/script.yaml --stage check
uv run python -m pipeline.build videos/<slug>/script.yaml
uv run python -m pipeline.youtube videos/<slug>/script.yaml   # publish/youtube.txt
```

See `AGENTS.md` for the layout and `docs/PIPELINE.md` for the stages.
