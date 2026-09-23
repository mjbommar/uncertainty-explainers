"""Research helpers for the uncertainty explainers.

Composes bc-modules only:

- search: ``bc_web.Retriever.search`` on both backends (Exa, SerpAPI);
- fetch:  ``bc_web.Retriever.fetch`` in ``mode="auto"``, escalating
  HTTP -> Playwright (headless) -> pydoll (headful under Xvfb);
- parse:  ``bc_content.parse_payload`` for PDF and HTML to markdown.

Every search and fetch is appended to ``research/RETRIEVAL-LOG.jsonl``.
Raw bytes go to ``research/downloads/<slug>.<ext>`` and markdown to
``research/sources/<slug>.md`` with a YAML front-matter header. A manifest of
every fetched source is kept in ``research/manifest.json``.

Usage::

    uv run python research/tools.py search "Knight risk uncertainty" [--backend exa|serpapi|both] [-n 8]
    uv run python research/tools.py fetch SLUG URL --title T --authors A --year Y [--browser]
    uv run python research/tools.py catalog research/catalog.yaml [--only slug,slug] [--force]
    uv run python research/tools.py reparse research/catalog.yaml slug,slug   # offline re-parse
    uv run python research/tools.py verify SLUG "exact quote"   # quote check + PDF page
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml
from bc_content import parse_payload
from bc_web import Retriever

ROOT = Path(__file__).resolve().parent
DOWNLOADS = ROOT / "downloads"
SOURCES = ROOT / "sources"
LOG = ROOT / "RETRIEVAL-LOG.jsonl"
MANIFEST = ROOT / "manifest.json"

# The escalation ladder for auto mode. pydoll headful is the Cloudflare tier.
ESCALATION = ["http", "playwright", "pydoll:headful"]


def now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def log(event: dict[str, Any]) -> None:
    event = {"ts": now(), **event}
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(event, ensure_ascii=False) + "\n")


def load_manifest() -> dict[str, Any]:
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text())
    return {}


def save_manifest(m: dict[str, Any]) -> None:
    MANIFEST.write_text(json.dumps(m, indent=2, ensure_ascii=False, sort_keys=True) + "\n")


# ---------------------------------------------------------------- search


async def search(r: Retriever, query: str, backend: str = "exa", n: int = 8, **opts: Any):
    """One search on one backend, logged. Returns the SearchResponse or None."""
    try:
        resp = await r.search(query, backend=backend, max_results=n, **opts)
    except Exception as exc:  # logged, not raised: one bad backend must not stop a pass
        log({"kind": "search", "query": query, "backend": backend, "opts": _jsonable(opts),
             "outcome": "error", "error": f"{type(exc).__name__}: {exc}"[:400]})
        return None
    log({"kind": "search", "query": query, "backend": backend, "opts": _jsonable(opts),
         "outcome": "ok", "n_hits": len(resp.hits), "cost_usd": resp.cost_usd,
         "hits": [{"pos": h.position, "title": h.title, "url": h.url} for h in resp.hits]})
    return resp


async def search_both(r: Retriever, query: str, n: int = 8, **opts: Any) -> dict[str, Any]:
    exa_opts = {k: v for k, v in opts.items() if k not in ("engine",)}
    serp_opts = {k: v for k, v in opts.items() if k not in ("exa_type", "category")}
    exa, serp = await asyncio.gather(
        search(r, query, "exa", n, **exa_opts), search(r, query, "serpapi", n, **serp_opts)
    )
    return {"exa": exa, "serpapi": serp}


def _jsonable(d: dict[str, Any]) -> dict[str, Any]:
    return {k: (str(v) if not isinstance(v, (str, int, float, bool, list, type(None))) else v)
            for k, v in d.items()}


# ---------------------------------------------------------------- fetch


def _ext(kind: str) -> str:
    return {"pdf": ".pdf", "html": ".html", "docx": ".docx", "text": ".txt"}.get(kind, ".bin")


def _front_matter(meta: dict[str, Any]) -> str:
    return "---\n" + yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=100) + "---\n\n"


async def fetch_source(
    r: Retriever,
    slug: str,
    url: str,
    *,
    title: str,
    authors: str = "",
    year: str | int = "",
    browser: bool = False,
    found_by: str = "",
    note: str = "",
) -> dict[str, Any]:
    """Fetch one URL with escalation, save raw and markdown, log, return manifest row."""
    req: dict[str, Any] = {}
    if browser:
        req = {"mode": "browser", "engine": "pydoll", "headless": False}
    try:
        res = await r.fetch(url, **req)
    except Exception as exc:
        row = {"slug": slug, "url": url, "outcome": "error",
               "error": f"{type(exc).__name__}: {exc}"[:400]}
        log({"kind": "fetch", **row})
        return row
    attempts = [{"tier": a.tier, "engine": a.engine, "headless": a.headless,
                 "status": a.status, "outcome": a.outcome, "note": a.note[:160]}
                for a in res.attempts]
    body = res.raw if res.raw is not None else res.html.encode("utf-8", "replace")
    base = {"slug": slug, "url": url, "final_url": res.final_url, "status": res.status,
            "tier": res.tier, "engine": res.engine, "headless": res.headless,
            "attempts": attempts, "content_type": res.content_type,
            "challenge": res.challenge.model_dump() if res.challenge else None}
    if not res.ok or not body:
        row = {**base, "outcome": "fetch_failed", "error": res.error}
        log({"kind": "fetch", **row})
        return row
    parsed = parse_payload(body, res.content_type, res.final_url)
    kind = parsed.kind.value if parsed.kind else "bin"
    sha = hashlib.sha256(body).hexdigest()
    raw_path = DOWNLOADS / f"{slug}{_ext(kind)}"
    raw_path.write_bytes(body)
    md = parsed.markdown if parsed.ok else ""
    # For HTML, bc-web's own readability markdown is often cleaner than kaos-web's full
    # page; keep whichever is longer-but-readable (bc-web first when it is substantial).
    if kind == "html" and res.markdown and len(res.markdown) > 0.5 * len(md or ""):
        md, parser = res.markdown, "bc-web-readability"
    else:
        parser = parsed.parser
    escalated = len(attempts) > 1 or (res.tier != "http")
    meta = {
        "title": title, "authors": authors, "year": str(year), "url": url,
        "final_url": res.final_url, "retrieved": now()[:10], "sha256": sha,
        "kind": kind, "parser": parser, "tier": res.tier, "engine": res.engine,
        "escalated": escalated, "found_by": found_by, "note": note,
        "chars": len(md),
    }
    (SOURCES / f"{slug}.md").write_text(_front_matter(meta) + md, encoding="utf-8")
    outcome = "ok" if len(md) > 500 else "thin"
    row = {**base, "outcome": outcome, "content_kind": kind, "parser": parser, "sha256": sha,
           "chars": len(md), "escalated": escalated, "raw_path": str(raw_path.relative_to(ROOT)),
           "parse_error": parsed.error}
    log({"kind": "fetch", **row})
    m = load_manifest()
    m[slug] = {**meta, "outcome": outcome, "status": res.status, "attempts": attempts,
               "raw_path": row["raw_path"]}
    save_manifest(m)
    return row


def reparse(slug: str, *, title: str, authors: str = "", year: str | int = "", url: str = "",
            found_by: str = "", note: str = "") -> dict[str, Any]:
    """Re-parse a saved download (no network), e.g. after installing a parser extra."""
    raw_path = next(DOWNLOADS.glob(f"{slug}.*"))
    body = raw_path.read_bytes()
    parsed = parse_payload(body, None, url or raw_path.name)
    sha = hashlib.sha256(body).hexdigest()
    md = parsed.markdown if parsed.ok else ""
    m = load_manifest()
    prev = m.get(slug, {})
    meta = {**{k: prev.get(k) for k in ("final_url", "tier", "engine", "escalated")},
            "title": title, "authors": authors, "year": str(year), "url": url,
            "retrieved": prev.get("retrieved", now()[:10]), "sha256": sha,
            "kind": parsed.kind.value if parsed.kind else "bin", "parser": parsed.parser,
            "found_by": found_by, "note": note, "chars": len(md)}
    (SOURCES / f"{slug}.md").write_text(_front_matter(meta) + md, encoding="utf-8")
    outcome = "ok" if len(md) > 500 else "thin"
    m[slug] = {**prev, **meta, "outcome": outcome, "raw_path": str(raw_path.relative_to(ROOT))}
    save_manifest(m)
    row = {"slug": slug, "url": url, "outcome": outcome, "chars": len(md), "tier": "local-reparse",
           "parser": parsed.parser, "parse_error": parsed.error}
    log({"kind": "reparse", **row})
    return row


def _norm(text: str) -> str:
    import re
    import unicodedata
    t = unicodedata.normalize("NFKC", text)
    t = t.replace("\u00ad", "").replace("\ufffe", "").replace("\x02", "").replace("\\", "")
    t = re.sub(r"[\u2018\u2019\u201b\u2032]", "'", t)
    t = re.sub(r"[\u201c\u201d\u201f\u2033]", '"', t)
    t = re.sub(r"[\u2010-\u2015]", "-", t)
    t = re.sub(r"-\s*\n\s*", "", t)          # hyphenated line breaks
    t = re.sub(r"[*_#>`]", "", t)              # markdown emphasis and headings
    return re.sub(r"\s+", " ", t).strip().lower()


def verify(slug: str, quote: str) -> dict[str, Any]:
    """Is ``quote`` in the converted source? For PDFs, which page(s) of the raw file?"""
    md = (SOURCES / f"{slug}.md").read_text(encoding="utf-8")
    found = _norm(quote) in _norm(md)
    pages: list[int] = []
    raw = next(DOWNLOADS.glob(f"{slug}.pdf"), None)
    if raw is not None:
        import pypdfium2 as pdfium
        doc = pdfium.PdfDocument(str(raw))
        q = _norm(quote)
        probe = q[: min(len(q), 60)]
        for i in range(len(doc)):
            txt = _norm(doc[i].get_textpage().get_text_range())
            if q in txt or probe in txt:
                pages.append(i + 1)
    row = {"slug": slug, "found_in_markdown": found, "pdf_pages": pages, "quote": quote[:200]}
    log({"kind": "verify", **row})
    return row


def retriever() -> Retriever:
    return Retriever(escalation=ESCALATION)


async def run_catalog(path: Path, only: set[str] | None, force: bool, conc: int = 4) -> None:
    entries = yaml.safe_load(path.read_text())
    done = load_manifest()
    todo = [e for e in entries
            if (not only or e["slug"] in only)
            and (force or done.get(e["slug"], {}).get("outcome") != "ok")]
    sem = asyncio.Semaphore(conc)
    async with retriever() as r:
        async def one(e: dict[str, Any]) -> None:
            async with sem:
                row = await fetch_source(
                    r, e["slug"], e["url"], title=e["title"], authors=e.get("authors", ""),
                    year=e.get("year", ""), browser=e.get("browser", False),
                    found_by=e.get("found_by", ""), note=e.get("note", ""))
                print(f"{row.get('outcome'):12} {row.get('tier')!s:10} {row.get('chars', 0):>8} "
                      f"{e['slug']}  {row.get('error') or ''}", flush=True)
        await asyncio.gather(*(one(e) for e in todo))


# ---------------------------------------------------------------- CLI


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("--backend", default="both")
    s.add_argument("-n", type=int, default=8)
    s.add_argument("--site", action="append", default=[])
    s.add_argument("--category")
    f = sub.add_parser("fetch")
    f.add_argument("slug")
    f.add_argument("url")
    f.add_argument("--title", required=True)
    f.add_argument("--authors", default="")
    f.add_argument("--year", default="")
    f.add_argument("--browser", action="store_true")
    c = sub.add_parser("catalog")
    c.add_argument("path", type=Path)
    c.add_argument("--only", default="")
    c.add_argument("--force", action="store_true")
    v = sub.add_parser("verify")
    v.add_argument("slug")
    v.add_argument("quote")
    rp = sub.add_parser("reparse")
    rp.add_argument("path", type=Path)
    rp.add_argument("slugs")
    a = ap.parse_args(argv)

    async def go() -> None:
        if a.cmd == "search":
            opts: dict[str, Any] = {}
            if a.site:
                opts["include_domains"] = a.site
            async with retriever() as r:
                backs = ["exa", "serpapi"] if a.backend == "both" else [a.backend]
                for b in backs:
                    o = dict(opts)
                    if a.category and b == "exa":
                        o["category"] = a.category
                    resp = await search(r, a.query, b, a.n, **o)
                    print(f"== {b}")
                    for h in (resp.hits if resp else []):
                        print(f"  {h.position:>2}. {h.title[:90]}\n      {h.url}")
        elif a.cmd == "fetch":
            async with retriever() as r:
                row = await fetch_source(r, a.slug, a.url, title=a.title, authors=a.authors,
                                         year=a.year, browser=a.browser)
                print(json.dumps(row, indent=2, default=str))
        elif a.cmd == "catalog":
            only = set(filter(None, a.only.split(","))) or None
            await run_catalog(a.path, only, a.force)
        elif a.cmd == "verify":
            print(json.dumps(verify(a.slug, a.quote)))
        elif a.cmd == "reparse":
            entries = {e["slug"]: e for e in yaml.safe_load(a.path.read_text())}
            for slug in a.slugs.split(","):
                e = entries[slug]
                row = reparse(slug, title=e["title"], authors=e.get("authors", ""),
                              year=e.get("year", ""), url=e["url"],
                              found_by=e.get("found_by", ""), note=e.get("note", ""))
                print(row)

    asyncio.run(go())
    return 0


if __name__ == "__main__":
    sys.exit(main())
