# bc-modules tooling report

What this project asked of `bc-modules`, what worked, and what did not. Each
item names the module and, where known, the fix that belongs upstream. The
detail behind the research items is in `research/README.md` ("Tool problems
met"); the detail behind the production items is in `docs/PRODUCTION-LOG.md`.

## Research (bc-web, bc-content, bc-research)

| Module | Used for | Result |
|---|---|---|
| `bc_web.Retriever.search`, Exa | 50 discovery queries | Relevant hits on all 50. |
| `bc_web.Retriever.search`, SerpAPI | The same 50 queries | About 8 returned unrelated results when the key term was a surname or a common word. |
| `bc_research` triage pass | Two ensemble questions | Found 5 sources the direct searches missed, for about $0.28. |
| `bc_web.Retriever.fetch`, ladder | 78 sources | 73 on plain HTTP, 5 needed a browser tier. |
| `bc_web` challenge detector | Every fetch | Marked four walls as `ok` (OAPEN Anubis, PMC cookie wall, an eGrove captcha, a DTIC maintenance page), so the ladder stopped early. Fix upstream: add those page shapes to the anti-bot detector's evidence set. |
| `bc_web` pydoll headful | Cloudflare and AWS WAF pages | Never returned a usable page (WebSocket HTTP 500 on Harvard DASH; rejected on eGrove and fasb.org). |
| `bc_web` browser fetch of a PDF | AMS journal PDF | `net::ERR_ABORTED` on the second fetch. |
| `bc_content.parse_payload`, PDF | Every PDF | Needs the `bc-content[pdf]` extra or every PDF converts to zero characters. The IPCC likelihood table was dropped; letters doubled in two files; scans have no OCR. |
| `bc_content.parse_payload`, HTML | NWS FAQ | Kept only the navigation; text is only in the raw HTML. |

## Production (bc-gen, bc-audio, bc-signal, bc-image, bc-viz, bc-motion)

| Module | Used for | Result |
|---|---|---|
| `bc_gen.GeminiSpeech` | Narration | Works for 3.1 models. `gemini-3.8-flash-tts` reads the instruction wrapper aloud, refuses a system instruction, and returns WAV. `pipeline/speech.py` carries a small 3.8 backend that keeps bc-gen's cache, receipts and verifier; it belongs upstream. |
| `bc_gen` pricing overlay | 3.8 TTS, gpt-image-2.5 | Prices added to the overlay in bc-modules (uncommitted there), plus a 7-line fix so OpenAI images price from the table. |
| `bc_gen.SpeechVerifier` | Every clip | Works; the verifier's transcription cost is not in the receipt, so the pipeline counts it. |
| `bc_gen.ElevenLabsSound` | Cues | Works. |
| `bc_gen.Lyria` | Music bed | Works, about $0.04 a clip. |
| `bc_gen.OpenAIImage` | gpt-image-2.5-flare | Works. No Gemini 3.8 image model exists; `gemini-3.1-flash-image` is the Gemini option. |
| `bc_audio` compressor | Master chain | Mono only; the pipeline splits and rejoins stereo. |
| `bc_signal` BS.1770 meter | Master | Works; -16.04 LUFS, -1.69 dBTP on the smoke encode. |
| `bc_viz` canvas | Every frame | Works; no letter-spacing, italic, or image embedding, so those are done in `bc_image`. |
| `bc_motion.timeline`, `encode.assemble` | Every build | Works; frame count and muxed duration match. |
