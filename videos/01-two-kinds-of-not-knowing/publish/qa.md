# QA: Not knowing comes in different forms (`01-two-kinds-of-not-knowing`)

Machine gates: **PASS**. Human review (watched in full, with sound): **pending**.

| Gate | Result | Evidence |
|---|---|---|
| Full decode | PASS | `ffmpeg -v error -f null`: 0 errors |
| Stream | PASS | 7839 frames vs 7839 in the timeline; 1920x1080 30/1 h264 High yuv420p, bt709/bt709/bt709, 261.300 s |
| Loudness (muxed) | PASS | -16.03 LUFS integrated (target -16 +/- 0.7), -1.45 dBTP (ceiling -1.0), LRA 2.59 LU, 2 ch |
| Narration ASR | PASS | worst WER 0.062 (limit 0.1) |
| Containment | PASS | 100 scene renders, 0 with ink outside the stage |
| Captions | PASS | 50 cues, 0 problems |

Master WAV before encode: -16.0 LUFS, -1.5 dBTP, LRA 2.6 LU. Track vs timeline drift: {'measured_seconds': 261.3, 'timeline_seconds': 261.3, 'seconds': 0.0, 'ratio': 1.0}.

## Narration, segment by segment

| Segment | WER | Hearings | Heard |
|---|---|---|---|
| s01 | 0.000 | 1 | Three people give the same answer: "I do not know." One will roll a die, one holds a sealed envelope, one must guess the price of copper 20 years from now. |
| s02 | 0.000 | 1 | These people lack different things. What does each person not know? Why does that difference matter? |
| s03 | 0.000 | 1 | Uncertainty means that we do not know something. Two questions help us sort it. Does chance create the gap, or are facts missing? Can evidence support a number? |
| s04 | 0.000 | 1 | We will make four stops. First, chance, or missing facts. Then, what we can measure. Next, unknown odds. Last, the range between certainty and total ignorance. |
| s05 | 0.000 | 1 | Start with the die and the envelope. Both hide an answer, but they hide it in different ways. |
| s06 | 0.000 | 1 | No amount of study can reveal the next roll. Chance creates this uncertainty. Researchers call it aleatory uncertainty. |
| s07 | 0.000 | 1 | The number in the envelope is already fixed; opening it gives us the missing fact. Researchers call this epistemic uncertainty. |
| s08 | 0.000 | 1 | Chance remains, missing facts can be found. |
| s09 | 0.000 | 1 | We can find a missing fact, but we cannot remove chance. To give chance a number, we need many similar cases to count. |
| s10 | 0.000 | 1 | In 1921, Frank Knight used fire insurance as an example. One building may burn. Across many buildings, the insurer can measure how often fires occur. |
| s11 | 0.000 | 1 | A new business has no long record of close matches. Knight called the first case risk. He called this second case true uncertainty. |
| s12 | 0.000 | 1 | In 1937, John Maynard Keynes made the same split. Roulette has known odds. A future war or the price of copper twenty years later does not. |
| s13 | 0.042 | 1 | For those long-range questions, Keyes wrote that no scientific basis supported a calculation. His last sentence was plain: "We simply do not know." |
| s14 | 0.000 | 1 | Honest odds need many similar cases; without them, no sound number exists. |
| s15 | 0.000 | 1 | Knight and Keynes drew a sharp line between measurable risk and uncertainty. Daniel Ellsberg studied a case between those ends. |
| s16 | 0.062 | 1 | In 1961, Ellsberg described two urns: one holds 50 red and 50 black balls; the other holds 100 balls in an unknown mix. |
| s17 | 0.000 | 1 | Most people prefer the urn with the known mix, whichever color wins the bet. This case is called ambiguity: we know the possible results but not their odds. |
| s19 | 0.000 | 1 | Unknown odds call for a range. One exact number would claim more than the evidence supports. |
| s20 | 0.000 | 1 | Chance, missing facts, weak groups, and unknown odds do not fit into four separate boxes; they lie along a scale of what we can know. |
| s21 | 0.000 | 1 | One end holds complete certainty. At the other end, we may not even know which questions we have missed. |
| s22 | 0.000 | 1 | Before giving odds, place the forecast on this scale. Tell the audience what the evidence can support. |
| s23 | 0.000 | 1 | Chance remains while missing facts can be found. Honest odds need similar cases. When the odds are unknown, use a range. First place the forecast on the scale, then choose the number. |
| s25 | 0.000 | 1 | Now return to the three people. The die has known odds but an unknown result. The envelope holds a fixed fact we can learn. Copper's distant price has no sound odds. |
| s26 | 0.000 | 1 | What does each person not know? One lacks a future result, one lacks a fact, one lacks sound odds; the difference decides whether a number can help or mislead. |
| s27 | 0.000 | 1 | Once we know the kind of uncertainty, we can ask what a number can honestly say. |

## Review material

- Frames around every cut: `cuts.png` (100 frames)
- One frame per segment: `segments.png`

## Cost

Spent on this build: $0.2274. Total value of the generations the video uses (from receipts, cached or not): $0.3695. Unpriced items: [].

Machine verification is evidence for these gates only; it is not a substitute for watching the video.

## Brand bookends

The published MP4 is the programme above with the Da Vinci Math intro (4.2 s) before it and the outro (7.0 s, @DaVinciMath, https://math.davincilearner.com/) after a 0.5 s dissolve. Idents: `assets/brand/davinci-math/` (source: `davinci-math/brand/idents`).

| Gate | Result | Evidence |
|---|---|---|
| Full decode | PASS | 0 errors |
| Stream | PASS | 8160 frames vs 8160 expected; 1920x1080 30/1 h264 High yuv420p, bt709, 272.029 s |
| Loudness (muxed) | PASS | -16.11 LUFS, -1.23 dBTP, LRA 2.76 LU |
| Narration ASR at shifted times | PASS | 25 segments, worst WER 0.062 |
| Captions shifted | PASS | 50 cues, first at 4.200 s, 0 problems |

Frames around both joins: `package-joins.png`.
