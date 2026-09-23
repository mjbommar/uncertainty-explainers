# Plan

Phases, each gated by review of the previous one.

1. Foundations (parallel): web research into `research/`; local-resource mining
   into `docs/LOCAL-RESOURCES.md`, `docs/BC-MODULES-API.md`, `docs/VOICE.md`;
   pipeline build-out into `pipeline/` with a smoke video.
2. Scripts: three video scripts in `videos/<slug>/script.yaml` with
   storyboards, written in Simplified Book English, every claim keyed to
   `research/SOURCES.md`. Checked with `scripts/check_prose.py` and
   `scripts/check_simplified.py`.
3. Production: one agent per video generates narration, sound, images, frames,
   assembles, masters, captions.
4. Review: QA reports, decoded-frame inspection, ASR round trip, a viewing
   pass on each MP4; fixes; publish under `videos/<slug>/publish/`.

Video cut (provisional, to be revised by the research synthesis):

| # | Working title | Length | Thesis |
|---|---|---|---|
| 1 | Kinds of not knowing | 3 min | Uncertainty is not one thing; the kind you face decides which tools work. |
| 2 | What a probability is | 6 to 8 min | The same number means different things under different interpretations, and the reasoning that gets you there is where errors hide. |
| 3 | Saying what you do not know | 8 to 10 min | Predictions, scenarios and counterfactuals are different claims; communicating them badly is how good models fail people. |
