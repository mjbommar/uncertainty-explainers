# QA: How evidence becomes a forecast (`02-from-evidence-to-forecast`)

Machine gates: **PASS**. Human review (watched in full, with sound): **pending**.

| Gate | Result | Evidence |
|---|---|---|
| Full decode | PASS | `ffmpeg -v error -f null`: 0 errors |
| Stream | PASS | 13234 frames vs 13234 in the timeline; 1920x1080 30/1 h264 High yuv420p, bt709/bt709/bt709, 441.133 s |
| Loudness (muxed) | PASS | -16.03 LUFS integrated (target -16 +/- 0.7), -1.51 dBTP (ceiling -1.0), LRA 2.97 LU, 2 ch |
| Narration ASR | PASS | worst WER 0.071 (limit 0.1) |
| Containment | PASS | 156 scene renders, 0 with ink outside the stage |
| Captions | PASS | 93 cues, 0 problems |

Master WAV before encode: -16.0 LUFS, -1.5 dBTP, LRA 2.97 LU. Track vs timeline drift: {'measured_seconds': 441.1333, 'timeline_seconds': 441.1333333333333, 'seconds': -3.3333333306018176e-05, 'ratio': 0.9999999244370561}.

## Narration, segment by segment

| Segment | WER | Hearings | Heard |
|---|---|---|---|
| open1 | 0.071 | 1 | A 40-year-old woman gets a routine breast cancer screening. Her test result is positive. |
| open2 | 0.071 | 1 | In a 1982 study, 95 out of 100 doctors said her chance of cancer was between 70 and 80 percent. |
| open3 | 0.000 | 1 | The correct answer was about 8 percent. Most doctors gave an answer almost 10 times too high. |
| open4 | 0.000 | 1 | How can the same test lead to such different numbers? Where does a probability come from and how can we test it? |
| claim | 0.000 | 1 | A probability sums up evidence; it is not a hidden fact waiting inside the world. We must choose the evidence, judge its limits, and test the result. |
| map | 0.000 | 1 | We will make five stops: the group being counted, the update after new evidence, the width of the answer, the kind of future claim, and the score. |
| b1 | 0.000 | 1 | First, ask what the number counts. That question will show where the doctors went wrong. |
| g1 | 0.061 | 1 | A reference class is the group used for a count. Philosopher Alan Hajek belongs to several groups: men, non-smokers, and philosophy professors. Each group gives him different odds of living to 80. |
| g2 | 0.000 | 1 | In 1814, Pierre-Simon Laplace counted about 5,000 years of recorded sunrises. His count gave odds near two million to one for another sunrise. |
| g3 | 0.000 | 1 | Laplace added that an astronomer would give much higher odds. The astronomer knew why days and seasons occur. The event stayed the same, but the evidence changed. |
| t1 | 0.000 | 1 | Every probability uses a group. Name that group, or the number has no clear meaning. |
| b2 | 0.000 | 1 | The group gives the number a base the doctors still missed because they used the test result badly. |
| u1 | 0.000 | 1 | Bayes' rule shows how new evidence should change a probability. It begins with the base rate, which is how common the disease was before the test. |
| u2 | 0.000 | 2 | Picture 1,040-year-old women at routine screening. Ten have breast cancer. That count gives the base rate: one in one hundred. |
| | | first hearing | Picture 1,040-year-old women at routine screening. Ten have breast cancer. |
| u3 | 0.000 | 1 | Eight of the ten women with cancer test positive. 95 of the 990 women without cancer also test positive. |
| u4 | 0.000 | 1 | In all, 103 women get a positive result. Only 8 have cancer. 8 out of 103 is about 7.8%. |
| u5 | 0.000 | 1 | Cancer is rare in this group, so most positive results come from women without cancer. The doctors focused on the test and lost sight of the base rate. |
| u6 | 0.000 | 1 | Whole-number counts made the problem easier: in a 1995 study, correct answers rose from 16% with percentages to about half with counts. |
| t2 | 0.000 | 1 | Start with how common the event is, then use the new evidence to update it. One test rarely turns a rare event into a common one. |
| b3 | 0.000 | 1 | Here, the group and test supported one useful number. We are not always that lucky. |
| w1 | 0.000 | 1 | A coin that lands heads 50 times in 100 tosses supports odds near one-half. An unseen coin might also be assigned one-half, but no toss supports that point. A range from zero to one shows our ignorance. |
| w2 | 0.000 | 1 | Daniel Ellsberg gave another example in 1961. An urn holds 30 red balls. The other 60 are black or yellow, but no one tells us the mix. |
| w3 | 0.000 | 1 | The chance of drawing red is exactly one third. The chance of black could be anywhere from zero to two thirds. A dot fits one answer; a range fits the other. |
| t3 | 0.000 | 1 | Thin evidence calls for a range; one exact point would hide how little we know. |
| b4 | 0.000 | 1 | A range shows the limits of today's evidence. A forecast adds a harder step, a claim about the future. |
| f1 | 0.000 | 1 | Forecasts use patterns from the past. In 1748, David Hume pointed out the hidden assumption: we expect the future to behave like the past. |
| f2 | 0.000 | 1 | A forecast also uses a model, which is a simplified account of how something works. In 1963, Edward Lorenz showed that tiny changes at the start could lead to very different results. |
| f3 | 0.000 | 1 | Europe's main weather center therefore runs its model 50 times with slightly different starting values. A tight group of runs supports a firmer forecast; a wide spread signals more uncertainty. |
| f4 | 0.000 | 1 | Different future claims do different jobs. Forecasts start with current conditions. Projections depend on stated assumptions. Scenarios describe possible paths, without assigning odds. |
| t4 | 0.000 | 1 | Forecasting joins past evidence to a model. Name the kind of future claim, state its assumptions, and show the spread of possible results. |
| b5 | 0.000 | 1 | We now have a future claim with clear limits. The last step is to test many such claims. |
| k1 | 0.033 | 1 | The Brier score measures the gap between a forecast and what happened. Lower scores are better. A 90% forecast earns a low cost when right and a high cost when wrong. |
| k2 | 0.000 | 1 | One result may be luck; many results reveal calibration. A calibrated set of 70% forecasts comes true about 70% of the time. |
| k3 | 0.000 | 1 | People are often too sure. In studies reviewed in 1974, ranges that people said were 98 percent certain missed the answer about 30 percent of the time. |
| t5 | 0.000 | 1 | One outcome cannot test a forecast; a long record of scored forecasts can. |
| z1 | 0.000 | 1 | Name the group before giving a probability. Start with the base rate, then update it with new evidence. Use a range when evidence is thin. For a future claim, name the model and assumptions. Test your work across many forecasts. |
| z2 | 0.000 | 1 | Return to the positive test. The answer begins with 1,000 similar women, then uses the test result to update the base rate. That path leads to 7.8%. |
| z3 | 0.000 | 1 | Where does a probability come from? It comes from a named group and evidence that changes what we know. How do we test it? We score many forecasts, not one result. |
| z4 | 0.000 | 1 | Even a well-built number can fail after we say it. The final video asks whether the listener heard the same probability we meant. |

## Review material

- Frames around every cut: `cuts.png` (156 frames)
- One frame per segment: `segments.png`

## Cost

Spent on this build: $0.0233. Total value of the generations the video uses (from receipts, cached or not): $0.4508. Unpriced items: [].

Machine verification is evidence for these gates only; it is not a substitute for watching the video.

## Brand bookends

The published MP4 is the programme above with the Da Vinci Math intro (4.2 s) before it and the outro (7.0 s, @DaVinciMath, https://math.davincilearner.com/) after a 0.5 s dissolve. Idents: `assets/brand/davinci-math/` (source: `davinci-math/brand/idents`).

| Gate | Result | Evidence |
|---|---|---|
| Full decode | PASS | 0 errors |
| Stream | PASS | 13555 frames vs 13555 expected; 1920x1080 30/1 h264 High yuv420p, bt709, 451.866 s |
| Loudness (muxed) | PASS | -16.09 LUFS, -1.51 dBTP, LRA 3.08 LU |
| Narration ASR at shifted times | PASS | 39 segments, worst WER 0.071 |
| Captions shifted | PASS | 93 cues, first at 4.200 s, 0 problems |

Frames around both joins: `package-joins.png`.
