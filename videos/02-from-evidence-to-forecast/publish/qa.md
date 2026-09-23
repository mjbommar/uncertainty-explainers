# QA: From evidence to forecast (`02-from-evidence-to-forecast`)

Machine gates: **PASS**. Human review (watched in full, with sound): **pending**.

| Gate | Result | Evidence |
|---|---|---|
| Full decode | PASS | `ffmpeg -v error -f null`: 0 errors |
| Stream | PASS | 11981 frames vs 11981 in the timeline; 1920x1080 30/1 h264 High yuv420p, bt709/bt709/bt709, 399.367 s |
| Loudness (muxed) | PASS | -16.05 LUFS integrated (target -16 +/- 0.7), -1.32 dBTP (ceiling -1.0), LRA 2.16 LU, 2 ch |
| Narration ASR | PASS | worst WER 0.059 (limit 0.1) |
| Containment | PASS | 152 scene renders, 0 with ink outside the stage |
| Captions | PASS | 101 cues, 0 problems |

Master WAV before encode: -16.0 LUFS, -1.5 dBTP, LRA 2.16 LU. Track vs timeline drift: {'measured_seconds': 399.3667, 'timeline_seconds': 399.3666666666667, 'seconds': 3.3333333306018176e-05, 'ratio': 1.000000083465487}.

## Narration, segment by segment

| Segment | WER | Hearings | Heard |
|---|---|---|---|
| s01 | 0.000 | 1 | A probability in a forecast is not a fact about the world; it is a summary of evidence. |
| s02 | 0.000 | 1 | The word 'probability' covers three ideas. It can mean how strongly evidence supports a claim, or how confident a person is, or a physical tendency, whatever anyone thinks. |
| s03 | 0.000 | 1 | Counting cases needs a reference class: the group you count over. One philosopher notes that he is a man, a non-smoker, and a philosophy professor; each group gives a different chance of living to 80. |
| s04 | 0.000 | 1 | In 1814, Pierre-Simon Laplace took recorded history as five thousand years of sunrises. His rule put the odds of one more sunrise at nearly two million to one. |
| s05 | 0.000 | 1 | He added that anyone who knows what drives the seasons would put the odds far higher. Same sunrise, more evidence, a different number. |
| s06 | 0.000 | 1 | Ignorance does not fix a number either. A factory makes cubes with sides up to one foot. Spread belief evenly over side length, and a side under half a foot gets one half. Over face area, one quarter. Over volume, one eighth. One event, three answers. |
| s07 | 0.000 | 1 | Evidence should move a number, and Bayes' Rule says how far. It starts from the base rate, how common something is before any test, and then weighs what the test shows |
| s08 | 0.000 | 1 | A 1995 study by Gigerenzer and Hoffrage used a screening test: Take 1000 women aged 40. 10 of them have breast cancer. |
| s09 | 0.000 | 1 | Eight of those ten test positive. Of the 990 women without cancer, 95 also test positive. |
| s10 | 0.000 | 1 | So 103 women test positive and only 8 of them have cancer. That is 7.8%. |
| s11 | 0.000 | 1 | In this reference class, the disease is rare, so most positive tests come from healthy women. |
| s12 | 0.000 | 1 | Given as percentages, this problem defeats experts: In a 1982 study by Eddy, 95 of 100 physicians said 70 to 80 percent. |
| s13 | 0.000 | 1 | Counting helps. In the 1995 study, correct answers rose from 16 percent with percentages to about half with counts of people. |
| s14 | 0.000 | 1 | One number can hide how much you know. A coin that landed heads in half of a hundred tosses gets one-half; so may a coin you have never seen. Its honest summary is a range, zero to one. |
| s15 | 0.053 | 1 | Daniel Ellsberg's urn, from 1961, makes the same point: it holds 30 red balls and 60 black and yellow balls in an unknown mix. |
| s16 | 0.000 | 1 | The chance of red is one-third. The chance of black is anywhere from zero to two-thirds. People often bet on this urn in a way no single number explains. A range offers one explanation. |
| s17 | 0.000 | 1 | Witness evidence has another shape. In Glenn Shafer's example, you trust your friend Betty nine times in ten. She says a limb fell on your car. |
| s18 | 0.000 | 1 | Her word supports a belief of 0.9 that it fell, and a belief of 0 that it did not. That 0 means no evidence, not certainty. |
| s19 | 0.000 | 1 | Dempster-Shafer theory gives each claim two numbers, a belief and an upper limit. If a second friend, equally reliable, independently agrees, belief rises to 0.99. |
| s20 | 0.000 | 1 | All these numbers lean on the past. In 1748, David Hume wrote that every conclusion from experience assumes the future will be like the past. |
| s21 | 0.000 | 1 | That is the problem of induction: the sun failing to rise tomorrow is no contradiction, and the assumption cannot be proved from experience without arguing in a circle. |
| s23 | 0.000 | 1 | Picking the best explanation adds a further gap: the best of the ones we thought of can be what Bas van Fraassen called the best of a bad lot. |
| s24 | 0.000 | 1 | Weather adds a harder problem. In 1963, Edward Lorenz showed that in a simple model of rising warm air, slightly different starting states can grow into very different states |
| s25 | 0.000 | 1 | So forecasters run the model many times. The European Centre for Medium-Range Weather Forecasts starts 50 runs from slightly altered states, plus one unaltered run. That set is an ensemble. |
| s26 | 0.000 | 1 | In one forecast from 26 May 2017, the runs sat close together 30 hours ahead; six days ahead, they had spread apart. |
| s27 | 0.050 | 1 | The spread is information. The center calls the probability of an event the most consistent way to convey forecast uncertainty. |
| s28 | 0.000 | 1 | Not every claim about the future is a forecast. A forecast starts from the present state and says what will happen in a form you can check. |
| s29 | 0.000 | 1 | A projection says what would happen if an assumption holds, such as a path of emissions. That assumption may or may not come true. |
| s30 | 0.000 | 1 | A scenario is a plausible story about the future, with no probability attached. The United Nations climate panel says scenarios are neither predictions nor forecasts. |
| s32 | 0.000 | 1 | A counterfactual asks what would have happened had the past been different. As Donald Rubin noted in 1974, we see a person's outcome with a treatment or without it, never both. |
| s33 | 0.000 | 1 | Judea Pearl puts these questions on three rungs: seeing, doing, and imagining. Data from a lower rung cannot alone answer a question from a higher one. |
| s34 | 0.000 | 1 | A forecast earns trust only when it is scored. The Brier score, from 1950, measures the squared gap between forecast and outcome. Lower is better. |
| s35 | 0.059 | 1 | In one tournament's form of the score, saying 90% costs 0.02 if right and 1.62 if wrong; the worst score is 2. |
| s36 | 0.000 | 1 | A forecaster is calibrated when the events they call 70% happen about 70% of the time. |
| s37 | 0.000 | 1 | People often are not. In studies reviewed by Tversky and Kahneman in 1974, ranges given as 98 percent sure missed about 30 percent of the time. |
| s38 | 0.000 | 1 | Forecasting can be trained. The Good Judgment Project found three things that helped: probability training, teamwork, and grouping the top 2 percent together. |
| s39 | 0.000 | 1 | Even they were overconfident at the edge. Early forecasts of 100 percent came true only about 70 percent of the time; late in a question, about 90. |
| s40 | 0.000 | 2 | A scored number still fails if the listener hears a different one. That is the next problem. |
| | | first hearing | A scored number still fails if the listener hears a different one. |

## Review material

- Frames around every cut: `cuts.png` (152 frames)
- One frame per segment: `segments.png`

## Cost

Spent on this build: $0.0276. Total value of the generations the video uses (from receipts, cached or not): $0.2468. Unpriced items: [].

Machine verification is evidence for these gates only; it is not a substitute for watching the video.
