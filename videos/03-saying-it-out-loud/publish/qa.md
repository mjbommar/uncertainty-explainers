# QA: Saying it out loud (`03-saying-it-out-loud`)

Machine gates: **PASS**. Human review (watched in full, with sound): **pending**.

| Gate | Result | Evidence |
|---|---|---|
| Full decode | PASS | `ffmpeg -v error -f null`: 0 errors |
| Stream | PASS | 16685 frames vs 16685 in the timeline; 1920x1080 30/1 h264 High yuv420p, bt709/bt709/bt709, 556.167 s |
| Loudness (muxed) | PASS | -16.02 LUFS integrated (target -16 +/- 0.7), -1.51 dBTP (ceiling -1.0), LRA 3.05 LU, 2 ch |
| Narration ASR | PASS | worst WER 0.086 (limit 0.1) |
| Containment | PASS | 212 scene renders, 0 with ink outside the stage |
| Captions | PASS | 119 cues, 0 problems |

Master WAV before encode: -16.0 LUFS, -1.5 dBTP, LRA 3.05 LU. Track vs timeline drift: {'measured_seconds': 556.1667, 'timeline_seconds': 556.1666666666666, 'seconds': 3.3333333362861595e-05, 'ratio': 1.0000000599340726}.

## Narration, segment by segment

| Segment | WER | Hearings | Heard |
|---|---|---|---|
| s01 | 0.000 | 1 | In February 1961, the Joint Chiefs of Staff reviewed a CIA plan to invade Cuba at the Bay of Pigs. |
| s02 | 0.000 | 1 | Their report listed the plan's weak points, then closed with a judgment: The plan, it said, has a fair chance of ultimate success. |
| s03 | 0.000 | 1 | The officer who drafted that line later said the chiefs put the odds at roughly three in ten. He meant fair, as a warning. |
| s04 | 0.000 | 1 | Other readers heard approval. The CIA quoted the phrase in a paper that argued for the invasion. |
| s05 | 0.000 | 1 | President Kennedy came to believe that the Joint Chiefs had endorsed the plan. After the invasion collapsed, he wondered why no one had warned him. |
| s06 | 0.000 | 1 | Three in ten meant seven chances in ten of failure. Where between the writer and the reader did seven in ten disappear, and how do you stop it? |
| s07 | 0.000 | 1 | Uncertainty is not communicated until the listener holds the number the speaker meant. A message about uncertainty has parts, and each part can fail. |
| s08 | 0.000 | 1 | The message has six stops: the word, the group a number counts over, the picture, and the single result; then words used on purpose, and the whole statement, with its missing part, how good the evidence is. |
| s09 | 0.000 | 1 | First, the word: The trouble began ten years before the Bay of Pigs. |
| s10 | 0.000 | 1 | In March 1951, a formal intelligence forecast said a Soviet attack on Yugoslavia should be considered a serious possibility. |
| s11 | 0.000 | 1 | Sherman Kent, on the board that approved it, meant about 65 in a hundred. A State Department planner had read it as much lower. |
| s12 | 0.048 | 1 | The other board members had meant anything from twenty and a hundred to eighty. They had agreed on a phrase without agreeing on a number. |
| s13 | 0.086 | 1 | Kent's fix was to give each word a number, and such ladders are now official. For United States intelligence, "likely" means 55–80%; for the Intergovernmental Panel on Climate Change (IPCC) it means 66–100%. |
| s14 | 0.050 | 1 | So a 60% chance is likely to an intelligence analyst but only about as likely as not to a climate scientist. |
| s15 | 0.000 | 1 | Readers bend the words, too. In a 2012 study, Americans put "very likely," meant as 90 percent or more, at 62. "Very unlikely" came out at 41. |
| s16 | 0.000 | 1 | A 2019 study found a fix that works: the number in brackets inside the sentence. With the word alone, readers' ranges overlapped the official range by about a third. With the bracket, by about two-thirds. |
| s17 | 0.000 | 1 | A word carries a number only if the number is beside it. |
| s18 | 0.000 | 1 | A number beside the word fixes the word, but a number can fail too. |
| s19 | 0.036 | 1 | Take a 30 percent chance of rain tomorrow. In 2005, researchers asked people in five cities what that means. Many said "rain 30 percent of the time" or "over 30 percent of the area." |
| s20 | 0.000 | 1 | The weather service means something else: it rains on about three of every ten days like tomorrow. |
| s21 | 0.000 | 1 | In New York, about two-thirds chose that meaning; in four European cities, only one-third to one-fifth did. |
| s22 | 0.000 | 1 | The missing piece is the reference class, the set of cases a number counts over. A number needs its reference class, or the listener supplies their own. |
| s23 | 0.000 | 1 | Words and numbers fail in the ear, pictures fail in the eye. |
| s24 | 0.000 | 1 | The clearest case is a hurricane. The National Hurricane Center draws a cone around a storm's forecast track to show where its center will probably go. |
| s25 | 0.000 | 1 | Each circle is sized so that two-thirds of past forecast errors fall inside, so about one time in three the center leaves the cone. |
| s26 | 0.000 | 1 | In August 2004, the forecast line for Hurricane Charley ran close to Tampa. Charley struck Punta Gorda instead, about 70 miles to the south. |
| s27 | 0.000 | 1 | Charlotte County, around Punta Gorda, had been inside the cone for four days, but much of the television coverage had pointed viewers at the line. |
| s28 | 0.000 | 1 | The hurricane center's director, Max Mayfield, later joked about his tombstone: "Don't focus on the skinny black line." |
| s29 | 0.000 | 1 | A picture of uncertainty is read as a picture of certainty, unless it says what it leaves out. |
| s30 | 0.000 | 1 | Suppose the word, the number, the group, and the picture are all right |
| s31 | 0.053 | 1 | The listener still judges by one outcome. In its final 2016 forecast, FiveThirtyEight gave Donald Trump about a 29% chance of winning. |
| s32 | 0.000 | 1 | Other models gave him 15 percent, and some gave him less than one. |
| s33 | 0.000 | 1 | Trump won. But 29 in 100 is more than one chance in four, and events with those odds happen all the time. |
| s34 | 0.000 | 1 | One outcome cannot judge a probability. Say so before the outcome arrives. |
| s35 | 0.000 | 1 | If words fail so often, why not always use numbers? |
| s36 | 0.000 | 1 | Some institutions refuse them on purpose. Take accounting. Under its rule for losses, now called ASC 450, a loss is probable, reasonably possible or remote. |
| s37 | 0.000 | 1 | The rule defines each word only with other words: probable means likely to occur and remote means slight. |
| s38 | 0.000 | 1 | Each word sets an action. A probable loss that can be estimated goes into the accounts, a reasonably possible one gets a note, and a remote one gets neither. |
| s39 | 0.000 | 1 | Courts have a ladder, too. In Addington against Texas, in 1979, the Supreme Court described three standards of proof. How sure the judge or jury must be. |
| s40 | 0.000 | 1 | In a money dispute, the two sides share the risk of error about equally. In a criminal case, society takes almost all of it. Clear and convincing evidence sits between. |
| s41 | 0.000 | 1 | The court put no numbers on these phrases; it said that how they shape decisions may well be unknowable. |
| s42 | 0.000 | 1 | Some ladders are words on purpose, tied to actions. Know which ladder you are on. |
| s43 | 0.000 | 1 | Word, number, group, picture, one result, and the ladder you are on. |
| s44 | 0.000 | 1 | One piece is still missing. In 2019, Van der Bles and colleagues set out what a statement of uncertainty should contain. It says what you are unsure about, and in what form, such as a range or a word. |
| s45 | 0.000 | 1 | Then, it says how good the evidence is. The IPCC calls this confidence, rated by the amount of evidence and how closely findings agree. |
| s46 | 0.000 | 1 | Confidence is a separate scale, not a probability. It tells the listener how far to trust the number. |
| s47 | 0.000 | 1 | Put together, a full statement reads like this: "Rain tomorrow is likely, 55 to 80%, counted over days like tomorrow at this spot. Our confidence in that range is medium." |
| s48 | 0.000 | 1 | Say the word, the number, the group, and how good the evidence is. |
| s49 | 0.000 | 1 | Taken in order, the stops make one argument: a word needs a number beside it, but a number needs its group, and a picture must say what it leaves out. |
| s50 | 0.000 | 1 | Even then, one outcome cannot judge the forecast, so say that first. Some ladders are words on purpose, so know which one you are on, and every message needs a statement of how good the evidence is. |
| s51 | 0.000 | 1 | Where, between the writer and the reader did seven in ten disappear, and how do you stop it? It disappeared beside the word, where no number, no group, and no confidence was written. |
| s52 | 0.000 | 1 | Written in full, the line would read like this: The plan has a fair chance, about three in ten, judged against operations of this kind, and our confidence in that number is low. |
| s53 | 0.000 | 1 | Fifteen years after the Bay of Pigs, the officer who wrote "A Fair Chance" was still troubled. He had not insisted that the numbers be used. Say the word, then say the number. |

## Review material

- Frames around every cut: `cuts.png` (212 frames)
- One frame per segment: `segments.png`

## Cost

Spent on this build: $0.0345. Total value of the generations the video uses (from receipts, cached or not): $0.5624. Unpriced items: [].

Machine verification is evidence for these gates only; it is not a substitute for watching the video.
