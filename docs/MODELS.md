# Models

Probed 2026-09-23 against the providers' own model lists: OpenAI `GET /v1/models`
(145 ids) and Gemini `GET v1beta/models` (61 ids). Prices are from the
providers' pricing pages on the same day and now sit in bc-gen's dated overlay
(`bc-gen/python/bc_gen/data/prices.json`, sources in `data/SOURCES.md`).

## What was asked for, and what exists

| Asked for | Exists? | Used |
|---|---|---|
| `gpt-image-2.5` | Yes, as two variants: `gpt-image-2.5-flare` and `gpt-image-2.5-sunburst` (snapshots `-2026-09-08`). Same rates: $5/M text in, $8/M image in, $30/M image out. Flare is the faster, lighter one. | **`gpt-image-2.5-flare`** for icons (quality `medium`) |
| "gemini 3.8 flash" for images | **No.** `gemini-3.8-flash` exists but is a text model. There is no `gemini-3.8-flash-image`. The newest Gemini image models are `gemini-3.1-flash-image` (Nano Banana 2), `gemini-3.1-flash-lite-image` and `gemini-3-pro-image`. | `gemini-3.1-flash-image` is the fallback provider (`provider: gemini` in a script) |
| Gemini voices | Yes. `gemini-3.8-flash-tts` and `gemini-3.8-flash-lite-tts` are new; `gemini-3.1-flash-tts-preview` (bc-gen's default) and the 2.5 preview TTS models remain. | **`gemini-3.8-flash-tts`, voice `Charon`** |

## Model ids by job

**Image generation.** OpenAI: `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`,
`gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-1.5`, `gpt-image-1`,
`gpt-image-1-mini`, `chatgpt-image-latest`. Gemini: `gemini-3.1-flash-image`,
`gemini-3.1-flash-image-preview`, `gemini-3.1-flash-lite-image`,
`gemini-3-pro-image`, `gemini-3-pro-image-preview`, `gemini-2.5-flash-image`.

**Text to speech.** Gemini: `gemini-3.8-flash-tts`, `gemini-3.8-flash-lite-tts`,
`gemini-3.1-flash-tts-preview`, `gemini-2.5-flash-preview-tts`,
`gemini-2.5-pro-preview-tts`. OpenAI: `gpt-4o-mini-tts` (and its two dated
snapshots), `tts-1`, `tts-1-hd`.

**Transcription (the verifier's ear and QA).** `gpt-4o-transcribe` (used),
`gpt-4o-mini-transcribe`, `gpt-transcribe`, `whisper-1` (word timestamps).

**Newest flash text model.** `gemini-3.8-flash` ($0.75/M in, $3.75/M out through
31 December 2026, then $1.50 / $7.50). Not used by the pipeline yet.

**Music.** `lyria-3.5`, `lyria-3-pro-preview`, `lyria-3-clip-preview` (used for the
30-second bed, $0.04 a clip).

**Sound effects.** ElevenLabs `eleven_text_to_sound_v2` ($0.12 a minute).

## Prices added to bc-gen's overlay

| Model | Rate | Why it was needed |
|---|---|---|
| `google:gemini-3.8-flash-tts` | $0.50/M text in, $9.00/M audio out, 25 audio tokens/s (2026 rate; doubles on 1 January 2027) | genai-prices fuzzy-matches the id to the 3.8 Flash *text* rates, which is wrong for audio |
| `google:gemini-3.8-flash-lite-tts` | $0.50/M in, $6.00/M audio out | same |
| `openai:gpt-image-2.5-flare`, `-sunburst` | $5/M text in, $30/M image out | genai-prices does not know them; the actual is priced from the response's `usage` |

## Gemini 3.8 TTS behaves differently

Gemini's guide says 3.8 treats the text "strictly as a verbatim transcript" and
takes sustained delivery in `speech_metadata.style` on the interactions
endpoint. Measured here through bc-gen's `GeminiSpeech` path
(`generateContent` with bc-gen's wrapper): the model spoke the wrapper
("You are a speech synthesizer...") and stopped before the script; a
`systemInstruction` is refused ("Developer instruction is not enabled for this
model"); and the audio comes back as a RIFF WAV, not raw PCM. So the pipeline
reaches 3.8 through `pipeline.speech.GeminiStyledSpeech`, a
`bc_gen.ProviderBackend` subclass (see `PRODUCTION-LOG.md`).

## Voices

The 30 prebuilt Gemini voices, with Google's one-word character: Zephyr
(bright), Puck (upbeat), Charon (informative), Kore (firm), Fenrir (excitable),
Leda (youthful), Orus (firm), Aoede (breezy), Callirrhoe (easy-going), Autonoe
(bright), Enceladus (breathy), Iapetus (clear), Umbriel (easy-going), Algieba
(smooth), Despina (smooth), Erinome (clear), Algenib (gravelly), Rasalgethi
(informative), Laomedeia (upbeat), Achernar (soft), Alnilam (firm), Schedar
(even), Gacrux (mature), Pulcherrima (forward), Achird (friendly),
Zubenelgenubi (casual), Vindemiatrix (gentle), Sadachbia (lively), Sadaltager
(knowledgeable), Sulafat (warm).

Candidates for a calm, clear, adult narrator: **Charon** (informative),
**Schedar** (even), **Sadaltager** (knowledgeable).

## Audition

`uv run python -m pipeline.audition`. The same two sentences in each voice, on
both current TTS models, every clip through `generate_verified` with
`SpeechVerifier(OpenAITranscribe("gpt-4o-transcribe"))`, delivery style
`pipeline.spec.HOUSE_STYLE`. Clips are in `build/audition/<model>/`, numbers in
`build/audition/audition.json`. f0 is the median tracked pitch
(`bc_signal.track`); loudness is the raw clip before any chain.

| Model | Voice | Seconds (s1 / s2) | Mean wpm | Worst WER | f0 Hz | Raw LUFS | Max dBTP | TTS cost | ASR cost |
|---|---|---|---|---|---|---|---|---|---|
| gemini-3.8-flash-tts | **Charon** | 6.44 / 8.08 | 158 | 0.000 | 117 | -19.6 to -18.1 | -1.7 | $0.0042 | $0.0009 |
| gemini-3.8-flash-tts | Schedar | 6.32 / 8.20 | 159 | 0.000 | 123 | -18.4 to -18.2 | -0.5 | $0.0042 | $0.0009 |
| gemini-3.8-flash-tts | Sadaltager | 5.76 / 8.28 | 166 | 0.000 | 128 | -18.3 to -17.3 | -1.5 | $0.0041 | $0.0008 |
| gemini-3.1-flash-tts-preview | Charon | 7.36 / 9.76 | 135 | 0.000 | 147 | -19.6 to -18.6 | -1.3 | $0.0113 | $0.0009 |
| gemini-3.1-flash-tts-preview | Schedar | 7.48 / 10.16 | 131 | 0.000 | 150 | -23.4 to -21.0 | -2.9 | $0.0116 | $0.0009 |
| gemini-3.1-flash-tts-preview | Sadaltager | 7.08 / 9.52 | 139 | 0.000 | 124 | -21.9 to -18.6 | -1.6 | $0.0110 | $0.0009 |

All twelve clips passed on the first draw. Audition total: $0.052.

**Chosen: `gemini-3.8-flash-tts` with Charon.** Closest to the ~145 wpm target
among the 3.8 voices without the 3.1 model's slow second sentence (123 wpm);
the lowest, steadiest pitch of the set; level consistent between clips; the
style is honoured as metadata rather than as risky prompt text; and 2.6 times
cheaper per second than 3.1. Schedar is the second choice (its raw peak hit
-0.5 dBTP, which the chain limits anyway).

**Not yet done:** nobody has listened. These are machine measures. Listen to
`build/audition/gemini-3.8-flash-tts/` before the first real episode is voiced,
and change `voice:` in the script if the ear disagrees.
