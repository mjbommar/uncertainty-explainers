# QA: Saying it out loud (`03-saying-it-out-loud`)

Machine gates: **PASS**. Human review (watched in full, with sound): **pending**.

| Gate | Result | Evidence |
|---|---|---|
| Full decode | PASS | `ffmpeg -v error -f null`: 0 errors |
| Stream | PASS | 16621 frames vs 16621 in the timeline; 1920x1080 30/1 h264 High yuv420p, bt709/bt709/bt709, 554.033 s |
| Loudness (muxed) | PASS | -16.05 LUFS integrated (target -16 +/- 0.7), -1.48 dBTP (ceiling -1.0), LRA 2.13 LU, 2 ch |
| Narration ASR | PASS | worst WER 0.091 (limit 0.1) |
| Containment | PASS | 196 scene renders, 0 with ink outside the stage |
| Captions | PASS | 136 cues, 0 problems |

Master WAV before encode: -16.0 LUFS, -1.5 dBTP, LRA 2.13 LU. Track vs timeline drift: {'measured_seconds': 554.0333, 'timeline_seconds': 554.0333333333333, 'seconds': -3.333333324917476e-05, 'ratio': 0.9999999398351485}.

## Narration, segment by segment

| Segment | WER | Hearings | Heard |
|---|---|---|---|
| s01 | 0.000 | 1 | In February 1961, the Joint Chiefs of Staff reviewed a CIA plan to invade Cuba at the Bay of Pigs. Their report came down to one phrase: |
| s02 | 0.000 | 1 | The report listed the plan's weak points, and then closed with a judgment: the plan, it said, has a fair chance of ultimate success. |
| s03 | 0.000 | 1 | The officer who drafted that line later said the chiefs put the odds at roughly three in ten. He meant "fair" as a warning, the way a C on a school test means fair work. |
| s04 | 0.000 | 1 | Other readers heard approval. The commandant of the Marine Corps said the plan should have accomplished the mission. The CIA quoted the phrase in a paper that argued for the invasion. |
| s05 | 0.000 | 1 | President Kennedy came to believe that the Joint Chiefs had endorsed the plan. After the invasion collapsed, he wondered why no one had warned him. |
| s06 | 0.000 | 1 | The words were true to the writer, and they failed at the other end. Uncertainty is not communicated until the listener holds the number the speaker meant. |
| s07 | 0.000 | 1 | Ten years earlier the same fault had shown up at the CIA. In March 1951 a National Intelligence Estimate, a formal forecast agreed by the intelligence agencies, said a Soviet attack on Yugoslavia should be considered a serious possibility. |
| s08 | 0.028 | 1 | A few days later, the head of the State Department's planning staff asked Sherman Kent what "odds" that meant. Kent said about 65-35 in favor of an attack; the planner had read it as much lower. |
| s09 | 0.034 | 1 | Kahneman then asked the members of the board that had approved the wording, and each had meant different odds: the lowest had meant about twenty in a hundred, and the highest about eighty. |
| s10 | 0.000 | 1 | They had agreed on a phrase, without agreeing on a number. Kent wrote that this shook him more than the failure with the Reader. |
| s11 | 0.000 | 1 | Kent's answer was a table, in which each word got a number and a margin. "Probable" meant 75 percent, give or take about 12. "Chances about even" meant 50, give or take 10. |
| s12 | 0.000 | 1 | Numbers stayed rare. A 2012 study read 379 declassified estimates and found that only 16 gave any number for a probability. |
| s13 | 0.000 | 1 | Since 2015, a directive called ICD 203 has told United States intelligence analysts to use one of two fixed ladders, seven words each, tied to ranges. "Likely" means 55 to 80 percent. |
| s14 | 0.091 | 1 | Climate scientists built their own ladder for the Intergovernmental Panel on Climate Change (IPCC). On that ladder, "likely" means 66-100%. |
| s15 | 0.040 | 1 | So one word carries two meanings. A 60% chance is "likely" to an intelligence analyst, but on the climate ladder it is only "about as likely as not". |
| s16 | 0.000 | 1 | The climate ranges also overlap, so anything very likely is also likely. The intelligence ranges sit end-to-end, and none of them reaches 0 or 100. |
| s17 | 0.000 | 1 | Readers bend the words as well. In a 2012 study, Americans read sentences from IPCC reports and gave the number they thought each word stood for. |
| s18 | 0.000 | 1 | "Very likely" is meant as 90% or more, and on average readers put it at 62. "Very unlikely" is meant as 10% or less, and readers put it at 41. Both ends were pulled toward the middle. |
| s19 | 0.000 | 1 | A 2019 study tested fixes for the intelligence ladder with 924 people. A table of meanings one click away barely helped, because only about half the readers ever opened it. |
| s20 | 0.000 | 1 | What worked was the number in brackets inside the sentence. With the word alone, readers’ ranges overlapped the official range by about a third. With the bracket beside the word, the overlap was about two thirds. |
| s21 | 0.000 | 1 | Numbers alone are not safe either. A forecast says 30% chance of rain tomorrow, and in 2005 researchers asked people in five cities what that means. |
| s22 | 0.000 | 1 | Many said it would rain 30% of the time. Others said it would rain over 30% of the area. |
| s23 | 0.032 | 1 | The weather service means something else: a 30% chance that your spot gets at least a hundredth of an inch. Put another way, it rains on about three of every 10 days like tomorrow. |
| s24 | 0.000 | 1 | In New York, about two-thirds of the people asked chose that meaning; in Amsterdam, Berlin, Milan, and Athens, only one-third to one-fifth did. |
| s25 | 0.000 | 1 | The missing piece has a name: the reference class. It is the set of cases that a percentage counts over, such as days, hours, or square miles. Until that is said, the number is only half a message. |
| s26 | 0.000 | 1 | Pictures carry the same risk. The National Hurricane Center draws a cone around a storm's forecast track to show where the center of the storm will probably go. |
| s27 | 0.029 | 1 | The cone is built from circles, each sized so that two-thirds of past forecast errors fall inside it. So about one time in three, the center leaves the cone. The cone does not show the storm size. |
| s28 | 0.000 | 1 | In August 2004, the forecast line for Hurricane Charley ran close to Tampa. Charley struck Punta Gorda instead, about 70 miles to the south. |
| s29 | 0.000 | 1 | Charlotte County around Punta Gorda had been inside the cone for four days. Much of the television coverage had pointed viewers at the line. |
| s30 | 0.000 | 1 | In the most exposed evacuation zones around Tampa Bay, 53 percent of people left. In the same kind of zone in southwest Florida, including Charlotte County, 31 percent did. |
| s31 | 0.000 | 1 | The director of the Hurricane Center, Max Mayfield, later joked about the words for his tombstone: "Don't focus on the skinny black line." |
| s32 | 0.040 | 1 | A probability can be right and still feel wrong. In its final forecast of the 2016 election, FiveThirtyEight gave Donald Trump about a 29 percent chance of winning. |
| s33 | 0.000 | 1 | Other models gave him 15 percent, eight, two, and less than one. FiveThirtyEight's line was 71 for Hillary Clinton against 29 for Trump. |
| s34 | 0.000 | 1 | Twenty-nine in a hundred is not small. It is more than one chance in four, and events with those odds happen all the time. |
| s35 | 0.000 | 1 | Three days after the vote, Nate Silver wrote that "people mistake having a large volume of polling data for eliminating uncertainty." |
| s36 | 0.000 | 1 | A single result cannot prove a probability right or wrong. Many forecasts, scored against what happened, can. |
| s37 | 0.000 | 1 | Accountants and courts face the same problem, and they answer with words too. Under the accounting rule for losses, now called ASC 450, a loss is probable, reasonably possible, or remote. |
| s38 | 0.000 | 1 | The rule defines each word only with other words: probable means likely to occur, and remote means slight. Reasonably possible sits between—more than remote but less than likely. |
| s39 | 0.000 | 1 | Each word sets an action: a probable loss that can be estimated goes into the accounts, and a reasonably possible loss gets a note to readers. A remote loss needs neither. |
| s40 | 0.000 | 1 | The tax rule is the exception: a company books the largest tax benefit that is greater than 50% likely to be realized, a number stated outright. |
| s41 | 0.069 | 1 | Courts have a ladder too. In Addington against Texas in 1979, the Supreme Court described three standards of proof. A standard of proof says how sure the factfinder must be. |
| s42 | 0.000 | 1 | In a money dispute, the standard is a preponderance of the evidence, and the two sides share the risk of a wrong decision in roughly equal fashion. |
| s43 | 0.000 | 1 | In a criminal case, the proof must be beyond a reasonable doubt, and society takes almost the entire risk of error upon itself. Clear and convincing evidence sits between the two. |
| s44 | 0.000 | 1 | The court put no numbers on these phrases. It said that the truth about how they shape decisions may well be unknowable. |
| s45 | 0.061 | 1 | In 2019, Annemarie van der Bles and her colleagues set out what a statement of uncertainty should contain. Start with what you are unsure about: a fact, a number or a scientific claim. |
| s46 | 0.000 | 1 | Then, pick a form, such as a range, a probability, or a word. Then say how good the evidence is. The IPCC calls this "confidence," rated by how much evidence there is and how closely findings agree. |
| s47 | 0.000 | 1 | Confidence is not a probability, and the intelligence directive keeps the two apart. A likelihood and a confidence level may not appear in the same sentence. |
| s48 | 0.034 | 1 | Put together, a full statement reads like this: "Rain tomorrow is likely (55-80% counted over days like tomorrow at this spot); our confidence in that range is medium." |
| s49 | 0.000 | 1 | Fifteen years after the Bay of Pigs, the officer who wrote "A Fair Chance" was still troubled. He had not insisted that the numbers be used. |

## Review material

- Frames around every cut: `cuts.png` (196 frames)
- One frame per segment: `segments.png`

## Cost

Spent on this build: $0.0315. Total value of the generations the video uses (from receipts, cached or not): $0.3151. Unpriced items: [].

Machine verification is evidence for these gates only; it is not a substitute for watching the video.
