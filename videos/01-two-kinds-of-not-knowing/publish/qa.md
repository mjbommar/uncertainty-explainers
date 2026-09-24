# QA: Two kinds of not knowing (`01-two-kinds-of-not-knowing`)

Machine gates: **PASS**. Human review (watched in full, with sound): **pending**.

| Gate | Result | Evidence |
|---|---|---|
| Full decode | PASS | `ffmpeg -v error -f null`: 0 errors |
| Stream | PASS | 6473 frames vs 6473 in the timeline; 1920x1080 30/1 h264 High yuv420p, bt709/bt709/bt709, 215.767 s |
| Loudness (muxed) | PASS | -16.03 LUFS integrated (target -16 +/- 0.7), -1.49 dBTP (ceiling -1.0), LRA 2.86 LU, 2 ch |
| Narration ASR | PASS | worst WER 0.083 (limit 0.1) |
| Containment | PASS | 100 scene renders, 0 with ink outside the stage |
| Captions | PASS | 43 cues, 0 problems |

Master WAV before encode: -16.0 LUFS, -1.5 dBTP, LRA 2.86 LU. Track vs timeline drift: {'measured_seconds': 215.7667, 'timeline_seconds': 215.76666666666668, 'seconds': 3.3333333306018176e-05, 'ratio': 1.0000001544878725}.

## Narration, segment by segment

| Segment | WER | Hearings | Heard |
|---|---|---|---|
| s01 | 0.000 | 1 | Three people say "I do not know." One holds a die, one a sealed envelope. One is asked the price of copper in twenty years. |
| s02 | 0.000 | 1 | When someone says they do not know, what exactly is it they do not know? And does the difference matter? |
| s03 | 0.000 | 1 | Uncertainty is not one thing; two questions tell its kinds apart, chance or ignorance, and measurable or not. |
| s04 | 0.000 | 1 | Four stops: chance or ignorance, measurable or not, unknown odds, and where a case sits. |
| s05 | 0.000 | 1 | Start with the die and the envelope, which fail for different reasons. |
| s06 | 0.000 | 1 | More study of a die will not tell you the next roll; that is aleatory uncertainty. |
| s07 | 0.000 | 1 | The number in the envelope is already fixed; open it and the doubt is gone. That is epistemic uncertainty. |
| s08 | 0.000 | 1 | Chance stays. Ignorance can be closed with data. |
| s09 | 0.000 | 1 | So ignorance can shrink, and chance cannot; but even chance needs something to count. |
| s10 | 0.000 | 1 | In 1921, Frank Knight pointed to fire insurance: across many buildings, the loss evens out. |
| s11 | 0.000 | 1 | A new venture has no such group. Knight called the first kind "risk" and the second "true uncertainty." |
| s12 | 0.000 | 1 | In 1937, John Maynard Keynes set roulette apart from a European war or copper prices twenty years out. |
| s13 | 0.000 | 1 | About these, he wrote, "There is no scientific basis on which to form any calculable probability whatever. We simply do not know." |
| s14 | 0.000 | 1 | A number needs a group of similar cases. Without one, there is none. |
| s15 | 0.083 | 1 | Knight and Canes drew a hard line. Ellsberg tested the ground between. |
| s16 | 0.000 | 1 | In 1961, Daniel Ellsberg offered two urns: 100 red and black balls (mix unknown) or 50 of each. |
| s17 | 0.000 | 1 | Whichever color they bet on, most people pick fifty of each. No single chance of red fits that. This is ambiguity. Outcomes known, odds not. |
| s19 | 0.000 | 1 | Where the odds are unknown, one number claims too much. People treat that differently, and so should a forecast. |
| s20 | 0.000 | 1 | Chance, ignorance, no group, unknown odds: these are points on one scale. |
| s21 | 0.000 | 1 | At the far end of that scale, in one team's words, we do not even know that we do not know. |
| s22 | 0.000 | 1 | So every forecast should first say where on the scale it stands. |
| s23 | 0.000 | 1 | Chance stays, and ignorance can be closed, so say which. But a number needs a group of cases, and where odds are unknown, one number claims too much. So say where on the scale you stand. |
| s25 | 0.000 | 1 | The die is chance with a number. The envelope is ignorance with a number waiting. Copper has no honest number. |
| s26 | 0.000 | 1 | When someone says they do not know, what exactly they do not know is a chance, a fact, or something no one can count. The difference matters. It decides what a number can mean. |
| s27 | 0.000 | 1 | The next question is what a number can honestly say. |

## Review material

- Frames around every cut: `cuts.png` (100 frames)
- One frame per segment: `segments.png`

## Cost

Spent on this build: $0.0114. Total value of the generations the video uses (from receipts, cached or not): $0.3164. Unpriced items: [].

Machine verification is evidence for these gates only; it is not a substitute for watching the video.
