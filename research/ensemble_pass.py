"""One bc-research ensemble + triage pass per research question, logged.

    uv run python research/ensemble_pass.py

Writes research/ensemble/<slug>.md (rendered results) and .json (every row with its
verdict), and one RETRIEVAL-LOG.jsonl line per question.
"""

from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

from bc_core import BudgetMeter
from bc_llm import BcLlmSettings, PydanticAIBackend
from bc_research import ResearchContext, ResearchSearch, SearchCache
from bc_web.search import Searcher
from bc_web.settings import BcWebSettings

sys.path.insert(0, str(Path(__file__).parent))
from tools import ROOT, log  # noqa: E402

OUT = ROOT / "ensemble"

QUESTIONS = [
    (
        "verbal-probability-interpretation",
        "how people interpret verbal probability phrases such as likely and serious possibility",
        ResearchContext(
            topic="Empirical studies of how people translate verbal probability expressions "
            "(likely, very likely, serious possibility, fair chance) into numbers, including "
            "IPCC and intelligence estimative language",
            goal="Find primary studies with numbers a short explainer video can show on screen",
            include=("peer-reviewed experiments", "government or IPCC guidance documents",
                     "intelligence community studies"),
            exclude=("marketing", "generic blog posts without data"),
        ),
    ),
    (
        "deep-uncertainty-decision",
        "decision making under deep uncertainty robust decision making definition",
        ResearchContext(
            topic="Definitions and origins of 'deep uncertainty' and robust decision making (RDM), "
            "including levels of uncertainty frameworks (Walker, Lempert, Kwakkel, RAND)",
            goal="Primary definitional sources a script writer can quote",
            include=("RAND reports", "peer-reviewed papers", "open access book chapters"),
            exclude=("consulting marketing pages",),
        ),
    ),
]


async def main() -> None:
    OUT.mkdir(exist_ok=True)
    llm_settings = BcLlmSettings()
    llm = PydanticAIBackend(
        llm_settings.registry(), pricing=llm_settings.pricing(),
        meter=BudgetMeter(max_usd=3.0),
    )
    web = BcWebSettings()
    searcher = Searcher(web)
    rs = ResearchSearch(searcher, llm=llm, cache=SearchCache(ROOT / ".search-cache"),
                        search_prices={"serpapi": 0.01, "exa": 0.005})
    for slug, seed, ctx in QUESTIONS:
        try:
            res = await rs.run(seed, ctx, tier="triage")
        except Exception as exc:
            log({"kind": "bc_research", "tier": "triage", "slug": slug, "query": seed,
                 "outcome": "error", "error": f"{type(exc).__name__}: {exc}"[:500]})
            print(slug, "ERROR", exc)
            continue
        (OUT / f"{slug}.md").write_text(res.render(n=40), encoding="utf-8")
        rows = [r.model_dump(mode="json") for r in res.rows]
        (OUT / f"{slug}.json").write_text(json.dumps({
            "queries": list(res.queries), "search_usd": res.search_usd, "llm_usd": res.llm_usd,
            "errors": list(res.errors), "rows": rows}, indent=1, default=str), encoding="utf-8")
        log({"kind": "bc_research", "tier": "triage", "slug": slug, "query": seed,
             "queries": list(res.queries), "n_rows": len(res.rows), "n_kept": len(res.kept),
             "search_usd": res.search_usd, "llm_usd": res.llm_usd, "errors": list(res.errors),
             "kept": [{"url": r.url, "title": r.candidate.title} for r in res.kept[:40]],
             "outcome": "ok"})
        print(slug, f"kept {len(res.kept)}/{len(res.rows)}", res.search_usd, res.llm_usd, res.errors)


if __name__ == "__main__":
    asyncio.run(main())
