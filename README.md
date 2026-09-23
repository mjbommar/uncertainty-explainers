# Uncertainty Explainers

Short animated video explainers on conceptions of uncertainty: how different
kinds of not-knowing connect to epistemology, mathematical probability, logic
and reasoning, and why they matter when we predict or model states of the
world that have not happened, or did not happen.

Built with [bc-modules](https://github.com/mjbommar) for research, generation,
audio post-processing and video assembly. Narration follows Simplified Book
English (`docs/guides/`).

## Build

```bash
uv sync
uv run python -m pipeline.build videos/<slug>/script.yaml --stage check
uv run python -m pipeline.build videos/<slug>/script.yaml
```

See `AGENTS.md` for the layout and `docs/PIPELINE.md` for the stages.
