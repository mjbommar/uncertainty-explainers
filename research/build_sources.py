"""Build research/SOURCES.md from keys.yaml, catalog.yaml, manifest.json and the log.

    uv run python research/build_sources.py
"""

from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent

VENUE = {
    "derkiureghian-2009-aleatory-epistemic": "Structural Safety 31(2):105-112 (author copy, ETH RIPID workshop)",
    "knight-1921-risk-uncertainty-profit": "Houghton Mifflin, Boston (FRASER, St. Louis Fed scan)",
    "keynes-1921-treatise-probability": "Macmillan, London (Project Gutenberg 32625)",
    "keynes-1937-general-theory-employment": "Quarterly Journal of Economics 51(2):209-223 (HET website transcription)",
    "ellsberg-1961-risk-ambiguity": "Quarterly Journal of Economics 75(4):643-669 (course-reading copy, UC Irvine)",
    "rumsfeld-2002-dod-briefing": "U.S. Department of Defense transcript (Yale Avalon Project)",
    "wikipedia-unknown-unknowns": "Wikipedia (secondary; for origins of the phrase)",
    "walker-2003-defining-uncertainty": "Integrated Assessment 4(1):5-17 (TU Delft repository)",
    "marchau-2019-dmdu-book": "Decision Making under Deep Uncertainty, Springer, ch. 1 (open access)",
    "lempert-2003-shaping-next-100-years": "RAND MR-1626",
    "lempert-2019-rdm-chapter": "Decision Making under Deep Uncertainty, Springer, ch. 2 (open access)",
    "rand-2013-rb9701-rdm-brief": "RAND Research Brief RB-9701",
    "iea-2020-review-radical-uncertainty": "Institute of Economic Affairs (book review; secondary for Kay and King 2020)",
    "taleb-2004-edge-learning-to-expect": "Edge.org essay",
    "sep-probability-interpret": "Stanford Encyclopedia of Philosophy",
    "laplace-1814-philosophical-essay": "Wiley/Chapman and Hall 1902 translation (Project Gutenberg 58881)",
    "ramsey-1926-truth-probability": "In The Foundations of Mathematics and Other Logical Essays (1931), ch. VII (fitelson.org copy)",
    "jaynes-2003-probability-theory": "Cambridge University Press 2003 (author preprint, bayes.wustl.edu)",
    "vanhorn-2003-cox-theorem": "International Journal of Approximate Reasoning 34(1):3-24 (course copy)",
    "sep-dutch-book": "Stanford Encyclopedia of Philosophy",
    "sep-formal-epistemology": "Stanford Encyclopedia of Philosophy",
    "sep-epistemology": "Stanford Encyclopedia of Philosophy",
    "sep-imprecise-probabilities": "Stanford Encyclopedia of Philosophy",
    "shafer-1990-dempster-shafer": "Encyclopedia entry (fitelson.org copy)",
    "denoeux-2023-belief-functions-lecture": "Lecture slides, Universite de technologie de Compiegne",
    "zadeh-1965-fuzzy-sets": "Information and Control 8:338-353",
    "zadeh-1977-possibility": "UC Berkeley ERL Memo M77/12; Fuzzy Sets and Systems 1:3-28 (1978)",
    "hume-1748-enquiry": "Project Gutenberg 9662 (Harvard Classics text)",
    "sep-induction-problem": "Stanford Encyclopedia of Philosophy",
    "sep-abduction": "Stanford Encyclopedia of Philosophy",
    "sep-logic-nonmonotonic": "Stanford Encyclopedia of Philosophy",
    "tversky-kahneman-1974-heuristics": "Science 185(4157):1124-1131 (course-reading copy, UC Irvine)",
    "brier-1950-verification": "Monthly Weather Review 78(1):1-3 (AMS Journals)",
    "mellers-2014-forecasting-tournament": "Psychological Science 25(5):1106-1115 (Wharton faculty copy)",
    "kahneman-2016-hbr-noise": "Harvard Business Review, October 2016 (partial: paywall)",
    "hoekstra-2014-ci-misinterpretation": "Psychonomic Bulletin & Review 21(5):1157-1164 (author copy)",
    "sep-counterfactuals": "Stanford Encyclopedia of Philosophy",
    "pearl-2019-seven-tools": "Communications of the ACM 62(3):54-60 (UCLA tech report R-481)",
    "rubin-1974-causal-effects": "Journal of Educational Psychology 66(5):688-701",
    "wack-1985-scenarios-hbr": "Harvard Business Review, September 1985 (landing page only: paywall)",
    "wack-1985-marshall-foundation": "Andrew W. Marshall Foundation library entry (abstract only)",
    "shell-2013-40-years-scenarios": "Shell International",
    "lorenz-1963-nonperiodic-flow": "Journal of the Atmospheric Sciences 20(2):130-141 (AMS Journals)",
    "ecmwf-fug-ensemble-rationale": "ECMWF Forecast User Guide (Confluence)",
    "ecmwf-fug-ensemble-products": "ECMWF Forecast User Guide (Confluence)",
    "ipcc-ar6-wg1-glossary": "Climate Change 2021: The Physical Science Basis, Annex VII",
    "kent-1964-words-estimative-probability": "Studies in Intelligence 8(4):49-65 (CIA CSI)",
    "cia-definition-estimative-expressions": "Studies in Intelligence (CIA CSI)",
    "kesselman-2008-verbal-probability-nie": "MS thesis, Mercyhurst College (ETH ISN copy)",
    "odni-2015-icd-203": "ODNI Intelligence Community Directive 203 (2 January 2015)",
    "mastrandrea-2010-ipcc-guidance-note": "IPCC Cross-Working Group Meeting on Consistent Treatment of Uncertainties",
    "mastrandrea-2011-guidance-note-commentary": "Climatic Change 108:675-691 (author copy)",
    "budescu-2012-effective-communication-ipcc": "Climatic Change 113:181-200 (course copy)",
    "harris-2013-lost-in-translation": "Climatic Change 121:415-425 (UCL author final)",
    "plosone-2019-verbal-probabilities": "PLOS ONE 14(4):e0213522",
    "vanderbles-2019-communicating-uncertainty": "Royal Society Open Science 6:181870",
    "spiegelhalter-2017-risk-uncertainty-communication": "Annual Review of Statistics and Its Application 4:31-60 (regulation.org.uk copy)",
    "guardian-2024-review-art-of-uncertainty": "The Observer/Guardian book review (secondary for Spiegelhalter 2024)",
    "gigerenzer-hoffrage-1995-frequency-formats": "Psychological Review 102(4):684-704 (MPIB library)",
    "gigerenzer-2005-30-percent-rain": "Risk Analysis 25(3):623-629 (MPIB library)",
    "silver-2016-final-election-update": "FiveThirtyEight, 2016-11-08 (Wayback Machine)",
    "silver-2016-why-538-gave-trump-better-chance": "FiveThirtyEight, 2016-11-11 (Wayback Machine)",
    "broad-2007-cone-misinterpretations": "Bulletin of the American Meteorological Society 88(5):651-667",
    "nhc-cone-definition": "NOAA National Hurricane Center web page",
    "nws-pop-definition": "NOAA National Weather Service web page",
    "friedman-zeckhauser-2012-assessing-uncertainty-intelligence": "Intelligence and National Security 27(6):824-847 (course copy, UC Berkeley)",
    "friedman-2019-war-and-chance-preview": "Oxford University Press (publisher preview: front matter and introduction)",
    "frus-1961-d35-jcs-evaluation": "Foreign Relations of the United States 1961-1963, vol. X, doc. 35 (JCSM-57-61, 3 Feb 1961)",
    "frus-1961-d46": "Foreign Relations of the United States 1961-1963, vol. X, doc. 46 (CIA paper, 17 Feb 1961)",
    "fasb-summary-statement-5": "FASB superseded-standards summary (codified as ASC 450)",
    "pcaob-au337b-fas5-excerpts": "PCAOB AU 337B (reproduces FAS 5 definitions)",
    "fasb-summary-statement-157": "FASB superseded-standards summary (codified as ASC 820)",
    "fasb-summary-fin-48": "FASB superseded-standards summary (codified in ASC 740)",
    "cpajournal-sop-94-6": "The CPA Journal (secondary for SOP 94-6, codified as ASC 275)",
    "addington-1979-standard-of-proof": "441 U.S. 418 (Cornell LII)",
    "knight-1921-econlib-pt1-ch1": "Econlib edition of Knight 1921, Part I, Chapter I",
    "ellsberg-1961-dklevine-copy": "Quarterly Journal of Economics 75(4):643-669 (dklevine.com archive copy)",
    "springer-2024-ellsberg-1961-text-context": "Decisions in Economics and Finance (2024), open access",
}


def main() -> None:
    keys = yaml.safe_load((ROOT / "keys.yaml").read_text())
    cat = {e["slug"]: e for e in yaml.safe_load((ROOT / "catalog.yaml").read_text())}
    man = json.loads((ROOT / "manifest.json").read_text())
    log = [json.loads(l) for l in (ROOT / "RETRIEVAL-LOG.jsonl").read_text().splitlines() if l.strip()]
    fetches = [r for r in log if r.get("kind") == "fetch" and "slug" in r]

    lines = [
        "# Sources",
        "",
        "Numbered citation register. Every script claim cites a key here. `Local file` is the",
        "markdown conversion in `research/sources/`; the raw download is in `research/downloads/`",
        "(not committed). `How retrieved` gives the bc-web tier and engine that returned the body,",
        "`found by` the search backend that surfaced the URL (exa, serpapi, both, bc-research",
        "ensemble, or direct for known SEP URLs). `Verified` is the retrieval date; the sha256 in",
        "each file's front matter pins the exact bytes. Rebuild with",
        "`uv run python research/build_sources.py`.",
        "",
        "| Key | Author(s) | Year | Title | Venue | URL | Local file | How retrieved | Verified |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for key, slug in keys.items():
        m, c = man[slug], cat[slug]
        how = f"{m.get('tier')}/{m.get('engine')}"
        if m.get("escalated"):
            how += " (escalated)"
        how += f"; found by {c.get('found_by') or 'direct'}"
        title = c["title"].replace("|", "/")
        lines.append(
            f"| [{key}] | {c.get('authors','')} | {c.get('year','')} | {title} | {VENUE.get(slug,'')} "
            f"| <{c['url']}> | `sources/{slug}.md` | {how} | {m.get('retrieved')} |"
        )
    lines += [
        "",
        "## Partial sources",
        "",
        "- [S35] HBR 2016 \"Noise\": paywall; only the summary and opening paragraphs came back.",
        "- [S40] HBR 1985 Wack: paywall; landing page only. [S41] is an abstract. The Shell",
        "  history [S42] carries the 1973 story instead.",
        "- [S13] and [S58] are book reviews standing in for Kay and King (2020) and Spiegelhalter",
        "  (2024), which are not open.",
        "- [S02] FRASER scan: only book pp. 197-232 have a text layer and kaos-pdf scrambles word",
        "  order. Use [S76] (Econlib Ch. I) for Knight's definitions.",
        "- [S05] UC Irvine Ellsberg copy has doubled-letter OCR. [S77] is cleaner; its tables are",
        "  still mangled, so take the payoff table from [S23] or [S78].",
        "- [S33] Brier 1950 is the AMS landing page with references, not the paper text. The score",
        "  definition is taken from [S34].",
        "- [S43] Lorenz 1963: abstract only. Both full-text PDFs tried were scans with no text",
        "  layer (UVM; Notre Dame <https://www3.nd.edu/~powers/ame.60611/lorenz.article.pdf>).",
        "- [S39] Rubin 1974 and [S32], [S59]: two-column OCR is scrambled in places; notes cite",
        "  raw PDF pages for numbers that did not verify in markdown.",
        "- [S74] is a 1995 CPA Journal summary standing in for AICPA SOP 94-6 (ASC 275).",
        "",
        "## Not fetched, or replaced by an open substitute",
        "",
        "Every URL below was requested; the outcome is in `RETRIEVAL-LOG.jsonl`.",
        "",
        "| Wanted | URL tried | Outcome | Substitute |",
        "|---|---|---|---|",
    ]
    failed = [
        ("Ellsberg 1961 (RAND P-2173 scan)", "https://www.rand.org/content/dam/rand/pubs/papers/2008/P2173.pdf", "HTTP 200, PDF has no text layer (0 chars)", "[S05] UC Irvine copy"),
        ("Lorenz 1963 (UVM PDF)", "https://cdanfort.w3.uvm.edu/research/lorenz-1963.pdf", "HTTP 200, PDF has no text layer (0 chars)", "[S43] AMS HTML via Playwright"),
        ("Friedman & Zeckhauser 2012 (Harvard DASH)", "https://dash.harvard.edu/bitstreams/7312037c-a56a-6bd4-e053-0100007fdf3b/download", "Cloudflare captcha; pydoll headful bypass failed (WebSocket HTTP 500)", "[S66] UC Berkeley course copy"),
        ("Marchau et al. 2019 full book (OAPEN)", "https://library.oapen.org/bitstream/handle/20.500.12657/22900/1007261.pdf", "Anubis proof-of-work page, not detected as a challenge", "[S09], [S11] Springer chapter PDFs"),
        ("Kent 1964 (CSI HTML page)", "https://www.cia.gov/resources/csi/studies-in-intelligence/archives/vol-8-no-4/words-of-estimative-probability/", "HTTP 200 stub (135 chars) linking a PDF", "[S47] CSI static PDF"),
        ("Zadeh 1977 (tech report landing page)", "https://www2.eecs.berkeley.edu/Pubs/TechRpts/1977/29351.html", "landing page only", "[S27] archive PDF"),
        ("Arduin 2021 review of Kay & King", "https://www.modernlawreview.co.uk/may-2021/arduin-kay-king/", "abstract only (Wiley paywall)", "[S13] IEA review"),
        ("Spiegelhalter 2024 review (PMC)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11892765/", "HTTP 203 cookie interstitial at every tier incl. pydoll headful; not detected as a challenge", "[S58] Guardian review"),
        ("Spiegelhalter 2024 review (Europe PMC REST)", "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11892765/fullTextXML", "HTTP 500", "[S58]"),
        ("Lichtenstein, Fischhoff & Phillips 1981 (DTIC HTML)", "https://apps.dtic.mil/sti/html/tr/ADA101986/", "DTIC 'Under Maintenance' page", "none; calibration rests on [S33], [S34], [S57]"),
        ("Lichtenstein, Fischhoff & Phillips 1981 (DTIC PDF)", "https://apps.dtic.mil/sti/tr/pdf/ADA101986.pdf", "DTIC 'Under Maintenance' page", "none"),
        ("AICPA SOP 94-6 (eGrove)", "https://egrove.olemiss.edu/cgi/viewcontent.cgi?article=1223&context=aicpa_sop", "Cloudflare captcha (HTTP), unflagged captcha page (Playwright), AWS WAF captcha (pydoll headful)", "[S74] CPA Journal"),
        ("AICPA SOP 94-6 (FASB PDF viewer)", "https://www.fasb.org/page/document?pdf=SOP+94-6.pdf&title=SOP%2094-6", "Cloudflare challenge at all three tiers", "[S74]"),
        ("Broad et al. 2007, second fetch", "https://journals.ametsoc.org/downloadpdf/view/journals/bams/88/5/bams-88-5-651.pdf", "first fetch HTTP 200 PDF; refetch failed net::ERR_ABORTED in browser tier", "[S63] from first fetch (re-parsed offline)"),
    ]
    for w, u, o, s in failed:
        lines.append(f"| {w} | <{u}> | {o} | {s} |")
    lines += [
        "",
        "Not open and not attempted as full text: Hacking, *The Emergence of Probability* (1975);",
        "Walley, *Statistical Reasoning with Imprecise Probabilities* (1991); Kay and King,",
        "*Radical Uncertainty* (2020); Tetlock and Gardner, *Superforecasting* (2015); Pearl and",
        "Mackenzie, *The Book of Why* (2018); Kahneman, Sibony and Sunstein, *Noise* (2021);",
        "Spiegelhalter, *The Art of Uncertainty* (2024); Taleb, *The Black Swan* (2007); Lewis,",
        "*Counterfactuals* (1973); FASB Codification text (another agent is mining local ASC",
        "copies). Claims about these rest on the open sources above, which describe them.",
        "",
        f"Fetch attempts logged: {len(fetches)}.",
    ]
    (ROOT / "SOURCES.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(len(keys), "sources")


if __name__ == "__main__":
    main()
