# QA: Say what the odds mean (`03-saying-it-out-loud`)

Machine gates: **PASS**. Human review (watched in full, with sound): **pending**.

| Gate | Result | Evidence |
|---|---|---|
| Full decode | PASS | `ffmpeg -v error -f null`: 0 errors |
| Stream | PASS | 17563 frames vs 17563 in the timeline; 1920x1080 30/1 h264 High yuv420p, bt709/bt709/bt709, 585.433 s |
| Loudness (muxed) | PASS | -16.02 LUFS integrated (target -16 +/- 0.7), -1.49 dBTP (ceiling -1.0), LRA 2.76 LU, 2 ch |
| Narration ASR | PASS | worst WER 0.067 (limit 0.1) |
| Containment | PASS | 212 scene renders, 0 with ink outside the stage |
| Captions | PASS | 128 cues, 0 problems |

Master WAV before encode: -16.0 LUFS, -1.5 dBTP, LRA 2.76 LU. Track vs timeline drift: {'measured_seconds': 585.4333, 'timeline_seconds': 585.4333333333333, 'seconds': -3.333333324917476e-05, 'ratio': 0.9999999430621194}.

## Narration, segment by segment

| Segment | WER | Hearings | Heard |
|---|---|---|---|
| s01 | 0.000 | 1 | In February 1961, the Joint Chiefs of Staff reviewed a United States plan to invade Cuba at the Bay of Pigs. |
| s02 | 0.000 | 1 | Their report listed serious problems, yet its final judgment said the plan has a fair chance of ultimate success. |
| s03 | 0.000 | 1 | The officer who wrote that sentence later explained the intended odds: about three chances in ten; he meant fair as a warning. |
| s04 | 0.000 | 1 | Other readers heard support for the plan. The Central Intelligence Agency quoted the phrase while arguing that the invasion should proceed. |
| s05 | 0.000 | 1 | President John F. Kennedy believed the military leaders had supported the plan. After the invasion failed, he asked why they had not warned him. |
| s06 | 0.000 | 1 | Three chances in ten of success also meant seven chances in ten of failure. Where did those seven chances disappear, between writer and reader? How can we keep that from happening? |
| s07 | 0.000 | 1 | Communication succeeds only when the listener understands the odds the speaker meant. Words, numbers, groups, and pictures can each change the message. |
| s08 | 0.042 | 1 | We will follow six points where meaning can change: the word, the numbers group, the picture, one result, words tied to actions, and the complete statement. |
| s09 | 0.000 | 1 | Begin with the word: Ten years before the Bay of Pigs, Sherman Kent found the same problem in another intelligence report. |
| s10 | 0.000 | 1 | In March 1951, an official forecast said a Soviet attack on Yugoslavia should be considered a serious possibility. |
| s11 | 0.000 | 1 | Kent helped approve that phrase. He thought it meant about 65 chances in 100. A State Department planner read it as much less likely. |
| s12 | 0.000 | 1 | Other board members gave meanings from 20 to 80 chances in 100: everyone had approved the same words, but they had not shared the same odds. |
| s13 | 0.061 | 1 | Kent proposed linking each word to a number range. Agencies now use such scales. United States intelligence uses "likely" for 55% to 80%. The Intergovernmental Panel on Climate Change uses "likely" for 66% to 100%. |
| s14 | 0.043 | 1 | A 60% chance is therefore likely on the intelligence scale. On the climate scale, the same number is only about as likely as not. |
| s15 | 0.000 | 1 | Readers also pull strong words toward the middle. In a 2012 study, people read "very likely" (meant as at least 90%) as 62%; they read "very unlikely" as 41%. |
| s16 | 0.000 | 1 | A 2019 study tested a simple fix: put the number in brackets beside the word. Readers matched the official range about twice as well when they saw both. |
| s17 | 0.000 | 1 | A word does not carry fixed odds by itself; put the number beside it. |
| s18 | 0.000 | 1 | The number makes the word clearer. Next, ask what that number counts. |
| s19 | 0.037 | 1 | Suppose tomorrow has a 30% chance of rain. In a 2005 study, respondents often thought that meant rain for 30% of the day or across 30% of the area. |
| s20 | 0.000 | 1 | The weather forecast means something else. Rain occurs on about three out of ten days with conditions like tomorrow's at that location. |
| s21 | 0.000 | 1 | About two out of three New Yorkers chose that meaning; in four European cities, only one out of five to one out of three people did. |
| s22 | 0.000 | 1 | The missing piece is the reference class, meaning the group of cases being counted. Name that group—otherwise, listeners will invent one. |
| s23 | 0.000 | 1 | Clear words and numbers still need a clear picture. A picture can hide uncertainty, even while trying to show it. |
| s24 | 0.000 | 1 | Consider a hurricane forecast. The National Hurricane Center draws a cone around the predicted track to show a likely area for the storm's center. |
| s25 | 0.000 | 1 | The cone is based on past forecast errors. About two-thirds of storm centers stay inside it, which means about one third travel outside it. |
| s26 | 0.000 | 1 | In August 2004, Hurricane Charley's forecast line ran near Tampa. The storm struck Punta Gorda instead, about 70 miles south. |
| s27 | 0.000 | 1 | Punta Gorda and the surrounding county had remained inside the cone for four days; much television coverage still drew attention to the center line. |
| s28 | 0.000 | 1 | National Hurricane Center director Max Mayfield later joked that his tombstone should say "Don't focus on the skinny black line." |
| s29 | 0.000 | 1 | Viewers may treat a forecast line as a promised path. Every uncertainty picture must explain what it includes and what it leaves out. |
| s30 | 0.000 | 1 | Now, suppose the word, number, group, and picture are clear. One more trap remains: judging the forecast by one result. |
| s31 | 0.067 | 1 | In its final 2016 forecast, FiveThirtyEight gave Donald Trump a 29% chance of winning the presidential election. |
| s32 | 0.000 | 1 | Other models gave him 15%. Some placed his chance below 1%. |
| s33 | 0.048 | 1 | Trump won. That result did not prove the 29% forecast wrong. Events with a 29% chance should occur about 29 times out of 100. |
| s34 | 0.000 | 1 | One result cannot test a probability. Explain that before anyone knows the result. |
| s35 | 0.000 | 1 | If words can confuse people, should every field replace them with numbers? No, some words set rules for action. |
| s36 | 0.000 | 1 | Accounting provides one example: a rule called Accounting Standards Codification 450 sorts possible losses into three groups: probable, reasonably possible, and remote. |
| s37 | 0.000 | 1 | The rule defines these terms with words, not fixed percentages: "Probable" means likely to occur, "remote" means the chance is slight. |
| s38 | 0.000 | 1 | Each term leads to an accounting action: a probable loss that can be estimated enters the accounts, a reasonably possible loss gets a note, a remote loss usually gets neither. |
| s39 | 0.032 | 1 | Courts also use word-based levels. In the 1979 case Addington v. Texas, the Supreme Court discussed three standards of proof. A standard tells a judge or jury how sure they must be |
| s40 | 0.000 | 1 | In most civil disputes, the two sides bear the risk of error more evenly. In criminal cases, the government bears much more of that risk. Clear and convincing evidence lies between those levels. |
| s41 | 0.000 | 1 | The court did not attach percentages to these standards; it said their exact effect on decisions may well be unknowable. |
| s42 | 0.000 | 1 | Some word scales exist to guide action, not to report exact odds. Before adding a number, ask what the scale is meant to do. |
| s43 | 0.000 | 1 | We have checked the word, number, group, picture, result, and kind of scale. One final part is still missing. |
| s44 | 0.000 | 1 | In 2019, van der Bles and other researchers described the parts of a useful uncertainty statement: state what is uncertain, then show its form, such as a probability, range, or word. |
| s45 | 0.000 | 1 | The statement should also describe the strength of the evidence. The climate panel calls this “confidence.” It depends on how much evidence exists and how well the findings agree. |
| s46 | 0.000 | 1 | Confidence and probability answer different questions. Probability gives the odds of an event. Confidence tells us how strongly the evidence supports those odds. |
| s47 | 0.032 | 1 | Here is a complete example: "Rain tomorrow is likely, with a chance between 55 and 80%." That range refers to days with similar conditions at this location. Confidence in the range is medium. |
| s48 | 0.000 | 1 | Give the word, the number, the group being counted, and the strength of the evidence. |
| s49 | 0.000 | 1 | The full message now comes together: put the number beside the word, name the group behind the number, explain what the picture includes and leaves out. |
| s50 | 0.000 | 1 | Warn that one result cannot test the forecast. Keep word scales when they guide action, then state how strongly the evidence supports the claim. |
| s51 | 0.000 | 1 | Where did seven chances in ten disappear? They vanished inside the phrase "fair chance." The report gave no number, no comparison group, and no account of the evidence's strength. |
| s52 | 0.000 | 1 | A clearer sentence might have said this: The plan has about three chances in ten of success, compared with similar operations. Our confidence in that estimate is low. |
| s53 | 0.000 | 1 | Fifteen years later, the officer who wrote A Fair Chance still regretted that he had not insisted on numbers: give the word, number, group, and strength of evidence; make the odds hard to miss. |

## Review material

- Frames around every cut: `cuts.png` (212 frames)
- One frame per segment: `segments.png`

## Cost

Spent on this build: $0.5244. Total value of the generations the video uses (from receipts, cached or not): $0.6491. Unpriced items: [].

Machine verification is evidence for these gates only; it is not a substitute for watching the video.

## Brand bookends

The published MP4 is the programme above with the Da Vinci Math intro (4.2 s) before it and the outro (7.0 s, @DaVinciMath, https://math.davincilearner.com/) after a 0.5 s dissolve. Idents: `assets/brand/davinci-math/` (source: `davinci-math/brand/idents`).

| Gate | Result | Evidence |
|---|---|---|
| Full decode | PASS | 0 errors |
| Stream | PASS | 17884 frames vs 17884 expected; 1920x1080 30/1 h264 High yuv420p, bt709, 596.163 s |
| Loudness (muxed) | PASS | -16.07 LUFS, -1.42 dBTP, LRA 2.82 LU |
| Narration ASR at shifted times | PASS | 53 segments, worst WER 0.067 |
| Captions shifted | PASS | 128 cues, first at 4.200 s, 0 problems |

Frames around both joins: `package-joins.png`.
