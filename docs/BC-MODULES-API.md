# BC-MODULES-API — verified call inventory, by production stage

`uncertainty-explainers` composes `bc-modules` (`AGENTS.md` rule 6) rather than
re-implementing media code. This is a verified inventory of the public API
this project should call, organized by pipeline stage: research, script,
speech, sfx/music, images, frames, timeline, assemble, master, captions, QA.

Every name below was confirmed against the source in
`/home/mjbommar/projects/bc/bc-modules/` (grep for `^class `/`^def `, or the
Rust-backed `_native.pyi` stub where the implementation is in Rust) — nothing
here is inferred from a README alone. File paths are absolute. Line numbers
are approximate (the modules are under active development) — treat them as
"look near here," not exact anchors.

Two module-boundary notes worth keeping in mind while reading this table:

- **bc-signal vs. bc-audio.** `bc-signal` is medium-agnostic 1-D array numerics
  (FFT/STFT, filters, envelope followers, BS.1770 loudness, pitch tracking,
  crossfades) — it knows about a sample rate and a window, not about channels,
  containers, or what a limiter is *for*. `bc-audio` sits on top of it and
  owns everything audio-specific (loudness targets for speech, the limiter,
  the compressor, mastering profiles, the ffmpeg driver). Call `bc-audio` for
  anything about narration or mixing; reach into `bc-signal` only for raw
  signal math a higher module doesn't already expose.
- **bc-web's escalation ladder.** `AGENTS.md` says fetch "escalates to
  Playwright or pydoll for anti-bot pages." That is directionally right but
  imprecise: the default ladder (`BC_WEB_ESCALATION`, default
  `"http,playwright"`) only includes Playwright. `pydoll:headful` (the tier
  that actually clears Cloudflare managed challenges, run under Xvfb) has to
  be added explicitly to the escalation setting — it is not on by default.

---

## 1. Research

| Call | Purpose | File | Example |
|---|---|---|---|
| `bc_web.Retriever.search(query, **options) -> SearchResponse` | One backend's search. | `bc-web/python/bc_web/retriever.py:820` | `r.search("Knight risk uncertainty 1921", backend="exa", n=8)` |
| `bc_web.Retriever.search_all(query, **options) -> FusedResponse` | Search every configured backend and fuse by rank. | `bc-web/python/bc_web/retriever.py:824` | `r.search_all("IPCC uncertainty guidance note")` |
| `bc_web.Retriever.fetch(url_or_request, **overrides) -> FetchResult` | Fetch one URL, escalating `http -> playwright -> (pydoll:headful if configured)` on a blocked/challenge/needs-browser verdict. | `bc-web/python/bc_web/retriever.py:496` | `r.fetch("https://plato.stanford.edu/entries/probability-interpret/")` |
| `bc_web.Retriever.fetch_many(urls, concurrency=4)` | Batch fetch. | `bc-web/python/bc_web/retriever.py:855` | — |
| `bc_web.Retriever.discover(url_or_origin, include_sitemaps=True) -> SiteDiscovery` | robots/sitemap/llms.txt/feed discovery before a crawl. | `bc-web/python/bc_web/retriever.py:801` | — |
| `bc_content.parse_payload(raw, content_type, url, *, kind=None) -> ParsedContent` | PDF/HTML/DOCX/PPTX/XLSX/text to markdown; never raises, returns `ok=False` on failure. | `bc-content/python/bc_content/parse.py:249` | `doc = parse_payload(raw_bytes, "application/pdf", url)` |
| `bc_content.sentences(text) -> list[TextSegment]` / `chunk_sentences(text, size=6000, overlap=400)` | Offset-preserving sentence/paragraph/chunk splitting for long fetched sources. | `bc-content/python/bc_content/chunk.py:31-141` | `for c in chunk_sentences(doc.text, size=7000, overlap=400): ...` |
| `bc_content.assess(text) -> DocumentQuality` | Flags mojibake/page-dump junk before a source is trusted. | `bc-content/python/bc_content/quality.py:49` | `if assess(doc.text).usable: ...` |
| `bc_content.extract_dates(text)` / `extract_money(text)` | Pull dated/dollar spans out of a source, for fact-checking a script's numbers. | `bc-content/python/bc_content/facts.py:53,71` | — |
| `bc_research.ResearchSearch(searcher, *, llm, fetcher, cache, ...)` | Four-tier search: `.search` (fan out, unjudged) -> `.ensemble` (query variants) -> `.triage` (cheap-model relevance judgment) -> `.read` (fetch + judge full text). `.run(query, context, tier="read")` chains all four. | `bc-research/python/bc_research/pipeline.py:305,353,393,757` | `results = await rs.run("Kent words of estimative probability 1964", context, tier="read")` |
| `bc_research.deep_research(question, context, *, rs, llm, fetcher, out_dir, intents=DEFAULT_INTENTS, ...) -> DeepResult` | Full research workflow: per-`Intent` query planning, search, claim extraction with verified quotes, reference-chasing, cross-source corroboration, timeline building, coverage/citation audit. Resumable; every skipped/failed stage recorded rather than dropped. | `bc-research/python/bc_research/deep.py:648` | one call per research question in `research/SOURCES.md` |
| `bc_research.Intent` | `StrEnum`: `PRIMARY, COVERAGE, ANALYSIS, SCHOLARLY, DATA, OFFICIAL, OPPOSITION, LOCAL`. | `bc-research/python/bc_research/intents.py:56` | — |
| `bc_research.ResearchContext` | `topic`/`goal`/`include`/`exclude` steering for triage and read relevance. | `bc-research/python/bc_research/pipeline.py` (README example) | — |
| `bc_research.SearchCache(root)` | On-disk cache keyed by query — avoid paying for the same search twice across a research session. | `bc-research/python/bc_research/search.py:73` | — |

This project's own `research/tools.py` already wraps the first tier of this
(`bc_web.Retriever.search`/`.fetch`, `bc_content.parse_payload`) with a
retrieval log and a markdown-source archive. `bc_research.deep_research` and
`ResearchSearch` are not yet used there — reach for them when a research
question needs corroboration across sources or a synthesized timeline, not
just "find and save one PDF."

## 2. Script

Scriptwriting is a human act here (`AGENTS.md`: every fact traces to
`research/SOURCES.md`; narration is Simplified Book English, not generated
prose). `bc-llm` is for *assisting* that process, not replacing it.

| Call | Purpose | File | Example |
|---|---|---|---|
| `bc_llm.PydanticAIBackend(registry, ...).generate(role=..., prompt=..., output_type=T, ...) -> CallResult[T]` | Structured-output completion against a named role/model, budget-checked and cost-recorded. | `bc-llm/python/bc_llm/pydantic_ai_backend.py:84,218` | drafting a structured scene-by-scene outline for human review, never final narration |
| `bc_llm.PromptLibrary(directory)` | Load/render/hash versioned prompt templates. | `bc-llm/python/bc_llm/prompts.py:29` | — |
| `bc_llm.repair.repair(...)` / `bc_llm.repair.abstaining(...)` | Retry-and-repair around structured generation; `abstaining` returns `Verdict`/`Abstained` rather than fabricating. | `bc-llm/python/bc_llm/repair.py:47,124` | — |
| `bc_llm.resolve_citations(text, known_ids, require_citation=False) -> CitationResult` | Numbers citation tokens in a draft and deletes any sentence whose citation doesn't resolve — a mechanical check that a script's claims trace to `research/SOURCES.md`. | `bc-llm/python/bc_llm/citations.py:72` | run against a script draft before the human style pass |
| `bc_llm.ConsensusBackend(inner, n=3)` | Field-by-field majority vote across `n` completions, for anything where you want redundancy before trusting a generated field. | `bc-llm/python/bc_llm/consensus.py:179` | — |
| `bc_llm.JudgePanel(models, passes, ...)` | Multi-model, multi-pass judging of a batch of items — see QA §11. | `bc-llm/python/bc_llm/judge.py:185` | rating draft scene descriptions against the script's claim list |

## 3. Speech

| Call | Purpose | File | Example |
|---|---|---|---|
| `bc_gen.Voice(provider, name, instructions="", model=None)` | One named voice with a direction string. | `bc-gen/python/bc_gen/speech.py:416` | `Voice("gemini", "Sadaltager", instructions="Speak in a neutral American accent...")` |
| `bc_gen.Casting(name, provider, model, voices, label="", summary="")` | A named set of role -> `Voice` bindings (narrator, quoted-source, etc.). | `bc-gen/python/bc_gen/speech.py:439` | — |
| `bc_gen.CastingBook(castings, default)` / `bc_gen.load_castings(path)` | A file of castings (understanding-accounting's `voices.yaml` schema) with a default. | `bc-gen/python/bc_gen/speech.py:460,474` | `book = load_castings("voices.yaml"); casting = book.get("narrator")` |
| `bc_gen.prepare(text, *, rules=None, min_words=60, max_words=250, fences="drop", tables="rows") -> list[Chunk]` | Markdown-to-speakable-prose plus symbol-reading rules, chunked to a TTS-friendly length. | `bc-gen/python/bc_gen/speech.py:379` | `chunks = prepare(scene_narration, rules=NOTATION)` |
| `bc_gen.NOTATION` | The default symbol-reading rule table (`%` -> "percent", `x` -> "times", `Section symbol` -> "section", etc.) — use this instead of hand-writing how a script's numbers should sound. | `bc-gen/python/bc_gen/speech.py:109` | — |
| `bc_gen.GeminiSpeech(model="gemini-3.1-flash-tts-preview", **kw)` | Gemini TTS backend (the voice understanding-accounting auditioned and shipped as `gemini-shorts`/Sadaltager). | `bc-gen/python/bc_gen/speech.py:626` | — |
| `bc_gen.OpenAISpeech(model="gpt-4o-mini-tts", **kw)` | OpenAI TTS backend (the voice davinci-math shipped for its lesson videos). | `bc-gen/python/bc_gen/speech.py:575` | — |
| `bc_gen.generate_verified(backend, request, *, cache, verifier=DEFAULT, rerolls=5) -> GenResult` | Cache lookup, provider call, verify, re-roll on failure, cache only on pass. This is the one entry point that should wrap every TTS call in this project. | `bc-gen/python/bc_gen/pipeline.py` | `result = await generate_verified(GeminiSpeech(), casting.voice("narrator").request(chunk.text), cache=cache)` |
| `bc_gen.GenCache(root, *, level=3)` | Content-addressed cache of every generated asset plus its `Receipt` — never hand-edit a receipt (`AGENTS.md` rule 3). | `bc-gen/python/bc_gen/cache.py` | `cache = GenCache("videos/<slug>/assets/.cache")` |
| `bc_gen.SpeechVerifier(transcriber, *, wer_max=0.10, cer_max=0.05, numerals=True, quotes=True)` | ASR round-trip verification: word error rate, numeral agreement, verbatim-quote containment. Defaults (0.10 WER / 0.05 CER) match understanding-accounting's shipped thresholds exactly. | `bc-gen/python/bc_gen/verify.py:82` | `verifier = SpeechVerifier(OpenAITranscribe())` |
| `bc_gen.OpenAITranscribe(...)` | The ASR side of the verification loop. | `bc-gen/python/bc_gen/transcribe.py:63` | — |

## 4. SFX and music

| Call | Purpose | File | Example |
|---|---|---|---|
| `bc_gen.ElevenLabsSound(model="eleven_text_to_sound_v2", *, output_format="mp3_44100_192")` | Text-prompted sound-effect generation. | `bc-gen/python/bc_gen/sound.py:35` | `sfx = await generate_verified(ElevenLabsSound(), SoundRequest(prompt="a soft chime, one note"), cache=cache)` |
| `bc_gen.Lyria(model=None, *, wav=False)` | Instrumental music generation (`LYRIA_MODELS = {"song": "lyria-3.5", "clip": "lyria-3-clip-preview"}`); `bc_gen.INSTRUMENTAL` is the standard "no vocals" prompt suffix. | `bc-gen/python/bc_gen/sound.py:123` | an ambient bed for the video, analogous to understanding-accounting's `bed.wav` |
| `bc_audio.compressor(samples, sample_rate, *, key=None, ...)` | Sidechain ducking: pass the narration track as `key` and the music bed as `samples` to duck the bed under narration. | `bc-audio/python/bc_audio/*.py` (Rust `compressor.rs:3`) | `ducked, _ = compressor(bed, sr, threshold_db=-18, ratio=5.0, key=narration)` |
| `bc_audio.ffmpeg.seamless_bed(source, seconds, dest, *, xfade_s=0.25)` | Crossfade-loop a short bed track to cover a longer video without an audible seam. | `bc-audio/python/bc_audio/ffmpeg.py` | — |
| `bc_signal.equal_power(...)` / `raised_cosine(...)` / `loop_seam(...)` | Lower-level crossfade kernels `bc_audio`'s bed-looping is built on, if a custom fade shape is needed. | `bc-signal/python/bc_signal/_native.pyi` | — |

## 5. Images

| Call | Purpose | File | Example |
|---|---|---|---|
| `bc_gen.OpenAIImage(model="gpt-image-2", **kw)` | Image generation/editing (edits take `references`). | `bc-gen/python/bc_gen/image.py:33` | — |
| `bc_gen.GeminiImage(model="gemini-3.1-flash-image", *, mime_type="image/png")` | Image generation with tiered `image_size` (`0.5K/1K/2K/4K`) and `aspect_ratio`. | `bc-gen/python/bc_gen/image.py:127` | — |
| `bc_gen.to_webp(path, dest, *, max_width=1400, quality=84)` | Re-encode/downscale a generated image for a smaller asset footprint. | `bc-gen/python/bc_gen/image.py:256` | — |
| `bc_image.io.load(path)` / `.save(frame, path)` / `.probe(path)` | Frame I/O. | `bc-image/python/bc_image/io.py` | — |
| `bc_image.compose(background, fg, at)` / `bc_image.blend(a, b, alpha)` | Compositing a foreground element or a two-frame cross-blend, with correct alpha handling (see the QA note in §11 about the Pillow alpha gotcha this supersedes). | `bc-image/python/bc_image/_native.pyi:151` | — |
| `bc_image.change_mask(a, b, threshold=0.06)` / `regions(mask, ...)` | Diff two frames to find what changed, for animating only the delta between two scene states (the persistence pattern understanding-accounting's `scenes.py` implements by hand). | `bc-image/python/bc_image/_native.pyi` | — |
| `bc_image.phash(gray)` / `hamming(a, b)` | Perceptual-hash dedupe, useful for catching accidentally duplicated generated stills. | `bc-image/python/bc_image/_native.pyi` | — |

## 6. Frames

| Call | Purpose | File | Example |
|---|---|---|---|
| `bc_viz.Canvas(w, h, background=...)` | Retained-geometry vector canvas — the direct successor to understanding-accounting's hand-rolled Pillow `Canvas` in `media/shorts/canvas.py`. | `bc-viz/python/bc_viz/_native.pyi:564` | `c = Canvas(1920, 1080, background="#f7f4ed")` |
| `bc_viz.Group(id=..., dx=..., dy=...)` | A positioned sub-group of canvas elements. | `bc-viz/python/bc_viz/_native.pyi:536` | — |
| `bc_viz.Scene.parse(svg, fonts) -> Scene` / `.render(w, h) -> ndarray` | Rasterize an SVG scene to a frame buffer via resvg, with explicit font paths (the successor to hand-loading vendored `.woff2` files the way understanding-accounting's `brand.py` does). | `bc-viz/python/bc_viz/_native.pyi:675` | — |
| `bc_viz.collisions(canvas) -> list[Finding]` | Overlap / out-of-bounds / tiny-text / low-contrast QA gate on a composed frame — see QA §11. | `bc-viz/python/bc_viz/_native.pyi:618` | — |
| `bc_viz.overflow_findings(svg, fonts)` | Ink-in-border-band check — the generalized version of understanding-accounting's hand-written `_ink_in_right_margin` containment fix. | `bc-viz/python/bc_viz/_native.pyi:717` | — |
| `bc_viz.svg.save_svg(canvas, path, *, title, description)` / `svg_geometry_hash(svg)` | Deterministic SVG writer plus a content hash, for reproducible figure builds. | `bc-viz/python/bc_viz/svg.py:42,96` | — |
| `bc_viz.Linear(domain, range)` / `Sqrt(...)` / `Threshold(edges)` | Scale mapping for data-driven marks (a probability axis, an area-encoded mark, a discretized confidence band). | `bc-viz/python/bc_viz/_native.pyi:36,85,115` | mapping a probability in `[0,1]` to a bar height |
| `bc_viz.models.FlowDiagram` / `DecisionFlow` / `Chart` / `EquationBridge` / `CycleDiagram` / `ThemeSpec` + `render(spec, theme, metrics) -> Canvas` | Declarative diagram specs (closer to `asc-legal-position-paper`'s TikZ card vocabulary than to hand-drawn scenes) — a good fit for a "here is the structure of Bayes' rule" or "here is a decision tree" panel. | `bc-viz/python/bc_viz/models.py:273` | — |

## 7. Timeline

| Call | Purpose | File | Example |
|---|---|---|---|
| `bc_motion.narration.load(path) -> Narration` / `.loads(text, ...)` | Load the narration sidecar — one YAML/JSON file per video: `deck`, and a list of `Note(page, say, slide, status, hold, transition, entrance, animation, animation_start, animation_end, sound, ...)`. This generalizes davinci-math's per-lesson narration JSON contract. | `bc-motion/python/bc_motion/narration.py:59,185` | — |
| `bc_motion.narration.require_reviewed(narration)` | Gate: refuses to proceed while any `Note.status == "draft"` — the mechanism for understanding-accounting's Rule 13 ("nothing is spoken until a person has owned the sentence") and davinci-math's "publishable output refuses any draft entry." | `bc-motion/python/bc_motion/narration.py:209` | call before any build stage past narration authoring |
| `bc_motion.narration.alignment_problems(narration, titles)` | Checks each note's declared `slide` against the actual deck's rendered titles — catches page/title drift, a hard error in davinci-math's pipeline. | `bc-motion/python/bc_motion/narration.py:227` | — |
| `bc_motion.narration.speakable(note, prepare=None)` | The exact text that should be sent to TTS for one note (after any prep rules). | `bc-motion/python/bc_motion/narration.py:267` | — |
| `bc_motion.timeline.build(pages, seconds, texts, holds, transitions, fps) -> Timeline` | Quantize measured clip durations into per-page frame spans. | `bc-motion/python/bc_motion/timeline.py:55` | — |
| `bc_motion.models.Timeline` — `.at_frame(frame)`, `.at(seconds)`, `.progress(frame, window)`, `.problems(...)`, `.drift` | The timeline object itself: frame-indexed lookup, davinci-math's `u = clamp(...)` continuous-animation progress helper, and consistency checks (no state shorter than a floor, no gap/overlap). | `bc-motion/python/bc_motion/models.py:143` | `state = timeline.at_frame(f); u = timeline.progress(f)` |
| `bc_motion.models.State(page, start_frame, frames, fps, spoken, hold=False, ...)` | One timeline entry: a page on screen for a span of frames. | `bc-motion/python/bc_motion/models.py:82` | — |
| `bc_motion.deck.compile(source, out_dir, *, engine="lualatex")` / `.rasterize(pdf, *, width, height, cache_dir)` / `.page_texts(pdf)` / `.titles(...)` | If a scene calls for a LaTeX/Beamer card (the `asc-legal-position-paper` pattern) rather than a pure `bc_viz` canvas: compile, rasterize (sha256-cached), and read back page text/titles for alignment checking — the clean, sidecar-based alternative to that project's embedded-footline-marker trick. | `bc-motion/python/bc_motion/deck.py:86,134,188,244` | — |

## 8. Assemble

| Call | Purpose | File | Example |
|---|---|---|---|
| `bc_motion.encode.assemble(entries, track, dest, profile=H264_HIGH_QUALITY, fps, size, timeline) -> AssembleReport` | Mux held/animated frame entries against the mastered narration track; raises `EncodeError` if the muxed duration disagrees with the timeline by more than `max(0.1, 2/fps)` seconds — the hard gate `asc-legal-position-paper`'s `gaap_render.py` and davinci-math's `encode.py` each hand-rolled independently. | `bc-motion/python/bc_motion/encode.py:516` | — |
| `bc_motion.encode.EncodingProfile` — named presets `H264_COMPATIBILITY`, `H264_HIGH_QUALITY`, `H264_ANIMATION`, `H264_STILLIMAGE`, `VP9_SCREEN_444` | Codec/pixel-format/GOP presets pulled from understanding-accounting and davinci-math's own encode settings. | `bc-motion/python/bc_motion/encode.py:40-173` | pick `H264_HIGH_QUALITY` for a release master |
| `bc_motion.render_sequence(name, page_a, page_b, count) -> ndarray` | Render `count` transition frames between two pages. 14 named transitions: `cut, dissolve, dip, defocus, push-left, push-up, glide, whip, zoom-in, zoom-out, focus-point, iris, wipe, curl` — a strict superset of `asc-legal-position-paper`'s two hand-written transitions (dissolve, dip). | `bc-motion` (Rust `transitions.rs:69`) | `bm.render_sequence("dip", page_a, page_b, 20)` |
| `bc_motion.motion_ledger(shots, fps)` / `shots_from_timeline(...)` | Build understanding-accounting's `frames.txt`-style row ledger from a timeline, for a frame-by-frame renderer that doesn't go through `assemble` directly. | `bc-motion/python/bc_motion/encode.py:200,221` | — |

## 9. Master

| Call | Purpose | File | Example |
|---|---|---|---|
| `bc_audio.master.master(source, dest, profile=SPOKEN_WORD, *, codec=None) -> Measurement` | Two-pass ffmpeg `loudnorm` mastering to a named profile, re-measured after the fact; deletes the output and raises `MasteringError` on drift rather than shipping an out-of-spec file. | `bc-audio/python/bc_audio/master.py` | `master("narration.wav", "narration-master.mp3", SPOKEN_WORD)` |
| `bc_audio.master.Profile` named constants | `SPOKEN_WORD` (**-18.0 LUFS**, -1.5 dBTP, LRA 7, mono) is the module default and matches understanding-accounting's lecture profile exactly; also `EDITORIAL` (-20.0), `SPOTIFY` (-14.0), `APPLE_PODCAST` (-16.0), `EBU_R128` (-23.0), `ATSC_A85` (-24.0). None of these is exactly understanding-accounting's Shorts profile (-16.0 LUFS, -1.5 dBTP, LRA 8/12, **stereo**, 192k) — see the recommendation in `LOCAL-RESOURCES.md` §"Mastering targets" for which to use. | `bc-audio/python/bc_audio/master.py` | `Profile(name="explainer-stereo", integrated_lufs=-16.0, true_peak_dbtp=-1.5, loudness_range_lu=8.0, max_loudness_range_lu=12.0, channels=2, bitrate="192k")` |
| `bc_audio.master.measure(samples, rate) -> Measurement` | BS.1770-4 loudness measurement via `bc_signal.Bs1770`. | `bc-audio/python/bc_audio/master.py` | — |
| `bc_audio.limiter(samples, sample_rate, ceiling_db=-1.0, lookahead_ms=5.0, release_ms=120.0, detector="true")` | Look-ahead true-peak limiter (BS.1770 Annex-2 oversampled detector). | `bc-audio` (Rust `limiter.rs:113`) | — |
| `bc_audio.ffmpeg.loudnorm(source, dest, *, integrated_lufs, true_peak_dbtp, loudness_range_lu, ...)` | The two-pass EBU R128 primitive `master()` is built on, for a custom mastering step outside the `Profile` model. | `bc-audio/python/bc_audio/ffmpeg.py` | — |
| `bc_audio.ffmpeg.concat(paths, dest, *, padding_budget_s=None)` | Concatenate narration clips into one continuous track; asserts the result duration equals the sum of parts — the fix for davinci-math's documented "per-clip MP3 padding drift" bug in understanding-accounting's older pipeline. | `bc-audio/python/bc_audio/ffmpeg.py` | — |
| `bc_audio.ffmpeg.trim_silence_tail(source, dest, *, noise_db=-45.0, min_silence_s=0.35)` | Trim trailing silence from a synthesized clip before concatenation. | `bc-audio/python/bc_audio/ffmpeg.py` | — |

## 10. Captions

| Call | Purpose | File | Example |
|---|---|---|---|
| `bc_motion.captions.cues_from_timeline(timeline, ...) -> list[Cue]` | One caption cue per spoken timeline state. | `bc-motion/python/bc_motion/captions.py:98` | — |
| `bc_motion.captions.render_vtt(cues, *, title="") -> str` / `render_srt(cues) -> str` | Emit WebVTT (this project's `publish/` format per `AGENTS.md`) or SRT. | `bc-motion/python/bc_motion/captions.py:129,145` | `Path("publish/captions.vtt").write_text(render_vtt(cues))` |
| `bc_motion.captions.split_text(text, max_chars=MAX_CUE_CHARS)` | Split a long spoken line into cue-sized pieces. `MAX_CUE_CHARS` comes from the Rust core's default and is in the same range as understanding-accounting's own `MAX_CUE_CHARS = 220` transcript-cue constant. | `bc-motion/python/bc_motion/captions.py:50` | — |
| `bc_motion.captions.problems(cues)` / `problems_vtt(vtt_text)` | Structural checks: monotonic, non-overlapping, in-bounds, under the max-chars limit — the same checks understanding-accounting's `captions.problems()` hand-implements (`WEBVTT` header present, no cue ends before it starts, no overlap, last cue within 0.5s of video length). | `bc-motion/python/bc_motion/captions.py:165,176` | run before staging a build |

## 11. QA

| Call | Purpose | File | Example |
|---|---|---|---|
| `bc_gen.SpeechVerifier(transcriber, wer_max=0.10, cer_max=0.05, numerals=True, quotes=True).verify(request, path) -> Verdict` | The ASR round-trip gate `AGENTS.md` rule 5 requires: transcribes the synthesized clip and checks word error rate, numeral agreement, and verbatim-quote containment before the asset is cached. | `bc-gen/python/bc_gen/verify.py:82` | already wired into `generate_verified` by default — call directly only to re-check an existing clip |
| `bc_gen.SoundVerifier` / `bc_gen.ImageVerifier` / `bc_gen.NoVerifier` / `bc_gen.default_verifier(request)` | The same verify-before-cache contract for SFX (duration/channels/codec) and images (size/aspect); `NoVerifier` is an explicit, receipt-recorded opt-out, never a silent skip. | `bc-gen/python/bc_gen/verify.py:223,275,64,316` | — |
| `bc_content.align.wer(ref, hyp)` / `cer(ref, hyp)` / `align_words_to_times(...)` | The lower-level alignment primitives `SpeechVerifier` is built on — useful directly if you need word-level timing (e.g. to place a sound cue at a specific spoken word, the way understanding-accounting's `sound:` cue field resolves an `at:` phrase). | `bc-content/python/bc_content/align.py:75-282` | — |
| `bc_viz.collisions(canvas) -> list[Finding]` / `overflow_findings(svg, fonts)` | Frame-level QA: overlapping/out-of-bounds/tiny-text/low-contrast elements, and ink bleeding into a safe-area border — the generalized version of understanding-accounting's hand-written `test_scenes.py` containment tests. | `bc-viz/python/bc_viz/_native.pyi:618,717` | run against every generated `bc_viz.Canvas` before it's accepted into a build |
| `bc_motion.models.Timeline.problems(pages=None, min_seconds=0.5)` / `.drift` | Structural timeline QA: gaps, overlaps, states shorter than a floor, measured-vs-timeline duration drift. | `bc-motion/python/bc_motion/models.py` | — |
| `bc_llm.JudgePanel(models, passes).run(items) -> JudgeReport` | Multi-model, multi-pass judged review of a batch (e.g. every scene's on-screen text checked against its narration sentence) — the tool-assisted half of understanding-accounting's decoded-frame human review process; it does not replace the human pass (see `LOCAL-RESOURCES.md`'s QA section on why the gate "does not prove the writing is right"). | `bc-llm/python/bc_llm/judge.py:185` | — |
| `bc_llm.resolve_citations(text, known_ids, require_citation=False)` | Mechanical citation-resolution check on a script draft against `research/SOURCES.md`'s id list. | `bc-llm/python/bc_llm/citations.py:72` | — |

---

## Not yet in bc-modules (per `docs/MEDIA_REBUILD.md`)

`/home/mjbommar/projects/bc/bc-modules/docs/MEDIA_REBUILD.md` records the
migration of understanding-accounting's `media/` (26,127 LOC) into
`bc-modules`; as of that document, all six media modules (`bc-signal`,
`bc-audio`, `bc-image`, `bc-motion`, `bc-viz`, `bc-gen`) are done and tagged
`v0.3.0`. Two things named there are explicitly **not yet built**, and stay
project-specific for now:

- **Publishing** — `media/{audio,video,sfx,shorts/youtube}/publish.py` is
  mapped to a future `bc_store.publish`, "follow-up, not yet built." This
  project's `publish/` directory and any S3/CDN step (if one is added later)
  currently has no `bc-modules` equivalent to call.
- **Content-specific synthesis primitives** stay where the content lives, by
  design: understanding-accounting's SFX pack of named dings and its
  money/locator narration-prep rules are explicitly kept in that repo rather
  than generalized into `bc-gen`. This project's own uncertainty-specific
  scene vocabulary (a calibration plot, a forecast cone, a Venn diagram of a
  sample space) belongs in `pipeline/`, built on `bc_viz`, the same way.
