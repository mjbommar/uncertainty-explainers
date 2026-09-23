# AGENTS.md

Canonical instructions for humans and agents working in `uncertainty-explainers`.
`CLAUDE.md` points here.

## What this is

A series of short animated video explainers (2 to 10 minutes) on conceptions
of uncertainty: how they connect to epistemology, mathematical probability,
logic and reasoning, and why they matter for making and communicating
predictions about future or counterfactual states.

## Layout

| Where | What |
|---|---|
| `research/` | Sources, notes, and the synthesis the scripts rest on. `research/SYNTHESIS.md` is the distilled argument; `research/SOURCES.md` is the citation register; `downloads/` holds fetched PDFs and HTML (not committed) and `sources/` their markdown conversions. |
| `docs/guides/` | Voice: `SIMPLIFIED-ENGLISH.md`, `STYLE.md`, `STYLE-CRAFT.md`, `STYLE-AI-TELLS.md` (copied from `../book-template`). Every spoken and on-screen word obeys them. |
| `docs/` | `PIPELINE.md` (how a script becomes an MP4), `LOCAL-RESOURCES.md` (what was reused from sibling repos), `PRODUCTION-LOG.md`. |
| `pipeline/` | The production code: script schema, scenes drawn per frame, speech, sound, images, mastering, assembly, QA. Composes `bc-modules`; does not re-implement it. |
| `videos/<slug>/` | One video. `script.yaml` (narration, scenes, timing), `storyboard.md`, `assets/` (generated images, SFX, receipts), `output/` (build product, not committed), `publish/` (the final MP4 and VTT, committed). |
| `scripts/` | Voice checkers copied from the book template: `check_simplified.py`, `check_style.py`, `check_prose.py`. |

## Tools

All media and research work goes through `../../bc/bc-modules` (path
dependencies in `pyproject.toml`; `uv sync` builds the Rust extensions):

- Search: `bc_web.Retriever.search` with `backend="exa"` and `backend="serpapi"`.
- Fetch: `bc_web.Retriever.fetch` (HTTP first, escalates to Playwright or pydoll for anti-bot pages).
- PDF and HTML to markdown: `bc_content.parse_payload`.
- Research workflow: `bc_research.deep_research`, `ResearchSearch`.
- Speech: `bc_gen.GeminiSpeech`; sound effects: `bc_gen.ElevenLabsSound`; images: `bc_gen.OpenAIImage` and `bc_gen.GeminiImage`; all through `bc_gen.generate_verified` with a `GenCache` and receipts.
- Audio post: `bc_audio` (compressor, limiter, mastering to BS.1770 loudness) and `bc_signal`.
- Frames and motion: `bc_image`, `bc_viz`, `bc_motion` (timeline, transitions, captions, `encode.assemble`).

## Rules

1. Voice is Simplified Book English. Plain, direct, patient, a little dry.
   One term per concept. Define every technical term at first use. No
   metaphor as decoration. No em dashes in narration. Sentences average 12 to
   18 words. Run `uv run scripts/check_prose.py` and `check_simplified.py`
   on every script before it is voiced.
2. Every factual claim in a script traces to an entry in `research/SOURCES.md`.
3. Every generated asset has a receipt beside it (bc-gen writes them). Never
   hand-edit a receipt.
4. Never commit `output/` or `.venv/`. `publish/` holds the final MP4 and VTT only.
5. A build is not done until the MP4 has been fully decoded, frames around
   every cut inspected, the audio loudness measured, and the narration
   transcribed back and compared with the script.
6. Compose `bc-modules`; do not copy its code here. If something is missing
   there, note it in `docs/PRODUCTION-LOG.md` rather than working around it silently.
