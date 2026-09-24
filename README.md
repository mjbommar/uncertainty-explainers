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
| 1 | [Two kinds of not knowing](videos/01-two-kinds-of-not-knowing/) | 3:36 | Some uncertainty is chance and some is ignorance; some can be measured and some cannot. A forecast should first say which kind it faces. |
| 2 | [From evidence to forecast](videos/02-from-evidence-to-forecast/) | 6:31 | A probability is a disciplined summary of evidence, not a fact about the world. It must be honest about its reference class and its width, and stated so it can be scored. |
| 3 | [Saying it out loud](videos/03-saying-it-out-loud/) | 9:16 | Uncertainty is not communicated until the listener holds the number the speaker meant. Pair every word with a number, a reference class, and a statement of confidence. |

Each video directory holds `script.yaml` (narration, scenes, sources, sound),
`storyboard.md`, generated assets with their receipts, and `publish/` with the
MP4 (Git LFS), WebVTT captions, poster, `qa.md` and `youtube.md`.

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
```

See `AGENTS.md` for the layout and `docs/PIPELINE.md` for the stages.
