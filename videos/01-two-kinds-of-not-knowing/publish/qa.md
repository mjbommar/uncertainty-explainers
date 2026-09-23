# QA: Two kinds of not knowing (`01-two-kinds-of-not-knowing`)

Machine gates: **PASS**. Human review (watched in full, with sound): **pending**.

| Gate | Result | Evidence |
|---|---|---|
| Full decode | PASS | `ffmpeg -v error -f null`: 0 errors |
| Stream | PASS | 5302 frames vs 5302 in the timeline; 1920x1080 30/1 h264 High yuv420p, bt709/bt709/bt709, 176.733 s |
| Loudness (muxed) | PASS | -16.05 LUFS integrated (target -16 +/- 0.7), -1.57 dBTP (ceiling -1.0), LRA 2.27 LU, 2 ch |
| Narration ASR | PASS | worst WER 0.000 (limit 0.1) |
| Containment | PASS | 52 scene renders, 0 with ink outside the stage |
| Captions | PASS | 40 cues, 0 problems |

Master WAV before encode: -16.0 LUFS, -1.53 dBTP, LRA 2.28 LU. Track vs timeline drift: {'measured_seconds': 176.7333, 'timeline_seconds': 176.73333333333332, 'seconds': -3.3333333306018176e-05, 'ratio': 0.9999998113919277}.

## Narration, segment by segment

| Segment | WER | Hearings | Heard |
|---|---|---|---|
| s01 | 0.000 | 1 | Some of what we do not know is chance. Some is ignorance. A forecast has to say which kind it faces. |
| s02 | 0.000 | 1 | Roll a fair die. No one can say what comes up next, and more study of the die will not help. Engineers call this aleatory uncertainty, from the Latin word for dice. |
| s03 | 0.000 | 1 | Now seal a number in an envelope. You do not know it either, but it is already fixed. Open the envelope, and the doubt is gone. This is epistemic uncertainty, a gap in what we know which more data could close. |
| s04 | 0.000 | 1 | Which kind we face depends on the model. Two engineers put it plainly in 2009: "It is the job of the model builder to make the distinction." |
| s05 | 0.000 | 1 | A second question is whether a chance can be measured at all. In 1921 the economist Frank Knight pointed to fire insurance. No one can say whether one building will burn. Across many buildings, the loss evens out, and an insurer can carry it. |
| s06 | 0.000 | 1 | A new business venture has no such group of similar cases. Knight called the measurable kind risk and the kind that cannot be measured true uncertainty. |
| s07 | 0.000 | 1 | In 1937, John Maynard Keynes drew a similar line, with examples: roulette, he wrote, is not uncertain in his sense, the length of a life is only slightly uncertain and the weather only moderately. A European war is uncertain, and so is the price of copper twenty years ahead. |
| s08 | 0.000 | 1 | About these matters he wrote, "There is no scientific basis on which to form any calculable probability whatever. We simply do not know." |
| s09 | 0.000 | 1 | In 1961, Daniel Ellsberg turned this into a bet. On the left, urn one holds 100 red and black balls, in a mix nobody tells you. On the right, urn two holds exactly 50 of each. Draw your color, and you win $100. |
| s10 | 0.000 | 1 | Most people would rather draw from urn two, whether they bet on red or on black. That choice treats red in urn one as less likely than a half, and black as less likely too. The two chances would add up to less than one. |
| s11 | 0.000 | 1 | No single probability fits those choices. The name for this is ambiguity. The probabilities themselves are unknown, or only partly known. In urn one, the chance of red could be anything from zero to one. |
| s12 | 0.000 | 1 | These kinds lie along one scale, from complete certainty to total ignorance. Choosing a supermarket line sits near the measured end; keeping an umbrella in the car, for rain you cannot put odds on, sits further along. |
| s13 | 0.000 | 1 | At the far end is total ignorance, where in one team's words, we do not even know that we do not know. A forecast should first say where on this scale it stands. |

## Review material

- Frames around every cut: `cuts.png` (52 frames)
- One frame per segment: `segments.png`

## Cost

Spent on this build: $0.0099. Total value of the generations the video uses (from receipts, cached or not): $0.2022. Unpriced items: [].

Machine verification is evidence for these gates only; it is not a substitute for watching the video.
