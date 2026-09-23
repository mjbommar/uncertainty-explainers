# Research

Sources, notes and the synthesis behind the uncertainty explainers.

| File | What it is |
|---|---|
| `SYNTHESIS.md` | The distilled argument and the proposed three-video cut. Start here. |
| `SOURCES.md` | Numbered register, [S01] to [S78]. Every claim in a script cites one. |
| `notes/0N-*.md` | One note per scope area: claims, verified quotes with page, plain definitions, candidate visuals. |
| `keys.yaml` | S-key to slug. Append only. |
| `catalog.yaml` | What to fetch: slug, URL, title, authors, year, which search backend found it. |
| `sources/<slug>.md` | Markdown conversion with YAML front matter (url, retrieved, sha256, tier, engine, parser). |
| `downloads/` | Raw PDF and HTML bytes. Not committed; re-created by the fetch step. |
| `manifest.json` | One row per fetched source, the machine form of the front matter. |
| `RETRIEVAL-LOG.jsonl` | Every search, fetch, re-parse, quote check and bc-research run, one JSON line each. |
| `ensemble/` | bc-research ensemble and triage output for two research questions. |
| `tools.py`, `ensemble_pass.py`, `build_sources.py` | The code. It composes bc-web, bc-content and bc-research. |

## Re-run

From the repo root:

```bash
uv sync                                                        # needs bc-content[pdf] and bc-llm[openai]
uv run python research/tools.py search "Knight risk uncertainty" -n 8          # both backends, logged
uv run python research/tools.py catalog research/catalog.yaml                  # fetch anything not yet ok
uv run python research/tools.py catalog research/catalog.yaml --force --only SLUG
uv run python research/tools.py reparse research/catalog.yaml SLUG             # offline, from downloads/
uv run python research/tools.py verify SLUG "exact quote"                      # quote check + PDF page
uv run python research/ensemble_pass.py                                        # bc-research, about $0.30
uv run python research/build_sources.py                                        # regenerate SOURCES.md
```

`EXA_API_KEY`, `SERPAPI_API_KEY` and `OPENAI_API_KEY` must be set. The fetch ladder is
HTTP, then Playwright headless, then pydoll headful under Xvfb.

## How the pieces were found and fetched (2026-09-23)

- **Searches:** 120 logged (60 on Exa, 60 on SerpAPI), about $0.42. Of the 78 sources, the URL
  came from Exa alone for 34, both backends for 24, SerpAPI alone for 6, the bc-research
  ensemble for 5, and 9 were known SEP URLs. 389 quote checks are logged as `verify` lines.
- **SerpAPI noise:** on about 8 of the 50 discovery queries SerpAPI returned unrelated Google
  results (YouTube, obituaries, phone reviews) when the key terms were a surname or a
  common word: "Ramsey 1926 Truth and Probability pdf", "Shafer Dempster-Shafer ...",
  "Mastrandrea 2010 IPCC guidance note ...", "National Hurricane Center definition of the
  cone ...", "ECMWF ensemble forecasting explained ...", "Bay of Pigs Joint Chiefs ...".
  Exa returned on-topic hits for all 50.
- **bc-research:** `ResearchSearch.run(tier="triage")` on two questions. Each wrote 7
  queries, ran 14 searches and 10 model calls, and kept 69 of 99 and 66 of 107 candidates
  for about $0.14 each. It surfaced the PLOS ONE 2019 study [S55], Wark's CIA survey [S48],
  Kesselman 2008 [S49], RAND RB-9701 [S12] and the RDM chapter [S11], none of which the
  direct queries had found.
- **Fetch tiers:** 73 sources came back on plain HTTP (curl_cffi). Five needed browser
  escalation, all to Playwright headless after a Cloudflare challenge on HTTP: AMS
  Journals (Brier [S33], Lorenz [S43]) and three FASB summary pages [S70, S72, S73].
  pydoll headful never produced a usable page in this run.

## Tool problems met (for the bc-modules tooling report)

1. **Missing extras.** `pyproject.toml` listed `bc-content` without `[pdf]`, so every
   PDF parsed to zero characters with `ModuleNotFoundError: kaos_pdf`. It also listed
   `bc-llm` without `[openai]`, so the default roles could not run. Both extras are now
   declared.
2. **Unflagged walls marked `ok`.** The Rust challenge detector does not recognize: the
   Anubis proof-of-work page (OAPEN), the PMC "Cookies must be enabled" interstitial
   (HTTP 203), a "Let's confirm you are human" puzzle served to Playwright by eGrove, and
   DTIC's "Under Maintenance" page. Because they pass as `ok`, the ladder stops before the
   next tier. The only symptom is a short body.
3. **pydoll Cloudflare bypass failed** on Harvard DASH with `Error in cloudflare bypass:
   server rejected WebSocket connection: HTTP 500`. It was then rejected by AWS WAF on
   eGrove and by Cloudflare on the fasb.org PDF viewer.
4. **Scanned PDFs.** RAND P-2173 (Ellsberg) and the UVM Lorenz copy parse to 0 characters.
   They have no text layer, and bc-content has no OCR path. Other copies were used.
5. **Browser-tier PDF downloads.** Once cached cookies sent a refetch of the AMS PDF
   through the browser, it failed with `net::ERR_ABORTED`. Navigating to a file download
   aborts the navigation. The first HTTP fetch had the bytes, so the file was re-parsed offline.
6. **HTML readability picks.** `tools.py` keeps bc-web's readability markdown when it is at
   least half the length of the kaos-web output. For SEP and journal pages this keeps the
   article and drops the navigation.
7. **Conversion losses in kaos-pdf.** It dropped the IPCC AR5 likelihood table entirely
   [S51]. It doubled letters in some scans (ICD 203 [S50], Ellsberg [S05]), reversed
   lines in Budescu [S53], fused words in two-column layouts, and scrambled word order in
   the Knight FRASER scan [S02]. The notes cite raw PDF pages for anything that did not
   verify in markdown. Clean replacements were fetched for Knight [S76] and Ellsberg [S77].
8. **HTML body dropped.** For the NWS PoP FAQ [S65] the saved markdown kept only
   navigation. The FAQ text is present only in the raw HTML.
9. **Landing pages that look like papers.** AMS Journals returned the article landing page
   (abstract plus references) for Brier [S33] and Lorenz [S43], not the paper text.
   Both Lorenz PDFs found were scans with no text layer.
10. **Own bug, fixed.** `tools.py` first let the content kind (`pdf`, `html`) overwrite the
    event kind in log lines. Those 114 lines were rewritten to `kind: fetch` with a
    `content_kind` field. `verify` now strips pdfium's U+FFFE hyphen marker.
