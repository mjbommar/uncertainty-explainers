# QA: Risk and uncertainty (`_smoke`)

Machine gates: **PASS**. Human review (watched in full, with sound): **pending**.

| Gate | Result | Evidence |
|---|---|---|
| Full decode | PASS | `ffmpeg -v error -f null`: 0 errors |
| Stream | PASS | 1098 frames vs 1098 in the timeline; 1920x1080 30/1 h264 High yuv420p, bt709/bt709/bt709, 36.600 s |
| Loudness (muxed) | PASS | -16.04 LUFS integrated (target -16 +/- 0.7), -1.69 dBTP (ceiling -1.0), LRA 2.31 LU, 2 ch |
| Narration ASR | PASS | worst WER 0.062 (limit 0.1) |
| Containment | PASS | 20 scene renders, 0 with ink outside the stage |
| Captions | PASS | 7 cues, 0 problems |

Master WAV before encode: -16.0 LUFS, -1.7 dBTP, LRA 2.35 LU. Track vs timeline drift: {'measured_seconds': 36.6, 'timeline_seconds': 36.6, 'seconds': 0.0, 'ratio': 1.0}.

## Narration, segment by segment

| Segment | WER | Hearings | Heard |
|---|---|---|---|
| s01 | 0.000 | 1 | Some unknowns come with odds, some do not. |
| s02 | 0.062 | 1 | Urn A holds 50 red and 50 black balls. Urn B holds 100 balls in a mix nobody tells you. |
| s03 | 0.000 | 1 | From urn A, the chance of red is one-half. That is risk, a gamble with known odds. |
| s04 | 0.000 | 1 | Without known odds, we use words. U.S. analysts read "likely" as 55 to 80 percent. |
| s05 | 0.000 | 1 | A weather model runs many times. The spread of its paths shows what it does not know. |

## Review material

- Frames around every cut: `cuts.png` (20 frames)
- One frame per segment: `segments.png`

## Cost

Spent on this build: $0.0019. Total value of the generations the video uses (from receipts, cached or not): $0.0703. Unpriced items: [].

Machine verification is evidence for these gates only; it is not a substitute for watching the video.
