# QA: From evidence to forecast (`02-from-evidence-to-forecast`)

Machine gates: **PASS**. Human review (watched in full, with sound): **pending**.

| Gate | Result | Evidence |
|---|---|---|
| Full decode | PASS | `ffmpeg -v error -f null`: 0 errors |
| Stream | PASS | 11732 frames vs 11732 in the timeline; 1920x1080 30/1 h264 High yuv420p, bt709/bt709/bt709, 391.067 s |
| Loudness (muxed) | PASS | -16.02 LUFS integrated (target -16 +/- 0.7), -1.6 dBTP (ceiling -1.0), LRA 2.98 LU, 2 ch |
| Narration ASR | PASS | worst WER 0.100 (limit 0.1) |
| Containment | PASS | 156 scene renders, 0 with ink outside the stage |
| Captions | PASS | 83 cues, 0 problems |

Master WAV before encode: -16.0 LUFS, -1.57 dBTP, LRA 2.98 LU. Track vs timeline drift: {'measured_seconds': 391.0667, 'timeline_seconds': 391.06666666666666, 'seconds': 3.3333333362861595e-05, 'ratio': 1.0000000852369588}.

## Narration, segment by segment

| Segment | WER | Hearings | Heard |
|---|---|---|---|
| open1 | 0.000 | 1 | A woman of forty goes for routine breast screening. The test comes back positive. |
| open2 | 0.000 | 1 | In a study reported in 1982, 95 of 100 physicians put her chance of cancer at 70 to 80 percent. |
| open3 | 0.000 | 1 | The right answer is under 8%. Same evidence, and a number ten times too big. |
| open4 | 0.000 | 1 | So where does a probability come from, and how can you tell whether it is any good? |
| claim | 0.000 | 1 | A probability is a summary of evidence, not a fact about the world, so it can be built badly, it can claim too much, and it can be checked. |
| map | 0.000 | 1 | Five stops. What the number counts, how evidence should move it, when one number is too many, what it says about the future, and how we know it was good. |
| b1 | 0.000 | 1 | To see where the doctors went wrong, start with what the number counts. |
| g1 | 0.057 | 1 | Counting needs a reference class—the group you count over. The philosopher Alan Hájek is a man, a nonsmoker, and a philosophy professor. Each group gives a different chance that he lives to 80. |
| g2 | 0.000 | 1 | In 1814, Laplace counted 5,000 years of sunrises and put the odds of one more at nearly two million to one. |
| g3 | 0.000 | 1 | Anyone who knows what drives the days and seasons," he added, "would put the odds far higher. Same sunrise, more evidence: a different number. |
| t1 | 0.000 | 1 | A probability counts over a group. Name the group, or the number floats. |
| b2 | 0.000 | 1 | The group matters, but the doctors had the right group and missed. |
| u1 | 0.000 | 1 | Their error was how the test moved the number. Bayes' rule starts from the base rate, how common the disease is before any test. |
| u2 | 0.000 | 1 | Take a thousand women of 40 in screening. Ten have breast cancer. That is the base rate. |
| u3 | 0.000 | 1 | Eight of those ten test positive. Of the 990 without cancer, 95 also test positive. |
| u4 | 0.000 | 1 | So 103 women test positive, and only eight of them have cancer. That is 7.8%. |
| u5 | 0.000 | 1 | The disease is rare, so most positives come from healthy women. The doctors left out the base rate, as earlier research found people do most of the time. |
| u6 | 0.000 | 1 | Counts help: in Gigerenzer and Hoffrage's 1995 study, correct answers rose from 16% with percentages to about half with counts. |
| t2 | 0.000 | 1 | Start from how common it is. Then let the test move you. Rare things stay rare after one test. |
| b3 | 0.100 | 1 | Baze gives one number, and for the test, that was enough. |
| w1 | 0.000 | 1 | But one number can claim too much. A coin that landed heads in half of a hundred tosses gets one half; so may a coin never seen. Its honest summary is a range: zero to one. |
| w2 | 0.067 | 1 | Daniel Ellsberg's urn from 1961 holds 30 red balls and 60 black and yellow balls in an unknown mix. |
| w3 | 0.000 | 1 | The chance of red is one third. The chance of black is anywhere from zero to two thirds. |
| t3 | 0.000 | 1 | When evidence is thin, an honest summary is a range, not a point. |
| b4 | 0.000 | 1 | A range is honest about today, a forecast reaches into tomorrow. |
| f1 | 0.000 | 1 | That claim leans on the past. In 1748, David Hume wrote that every conclusion from experience assumes the future will be like the past. |
| f2 | 0.000 | 1 | It also leans on a model. In 1963, Edward Lorenz showed that in a simple model of rising air, slightly different starts can grow into very different states. |
| f3 | 0.034 | 1 | So Europe's main weather center runs its model 50 times from slightly altered starts. When the runs agree, the weather is predictable; when they scatter, no firm forecast is possible. |
| f4 | 0.000 | 1 | A forecast starts from the present, a projection holds only if its assumption holds, and a scenario is a plausible story with no probability attached. |
| t4 | 0.000 | 1 | A forecast leans on the past and on a model: Say which kind of claim it is, and show the spread. |
| b5 | 0.000 | 1 | So a forecast is a claim, and a claim can be graded. |
| k1 | 0.000 | 1 | The Brier score from 1950 is the squared gap between forecast and outcome, and lower is better. In the Good Judgment Project, 90% cost 0.02 if right, 1.62 if wrong. |
| k2 | 0.000 | 1 | One miss can be bad luck. Over many forecasts, the scores show calibration. The events you call 70 percent should happen 70 percent of the time. |
| k3 | 0.000 | 1 | People often are not. In studies reviewed by Tversky and Kahneman in 1974, ranges given as 98% sure missed about 30% of the time. |
| t5 | 0.000 | 1 | One outcome proves nothing. Many forecasts, scored, do. |
| z1 | 0.000 | 1 | A probability counts over a group, so name the group. Evidence moves it by Bayes' rule, so start from the base rate, but thin evidence earns a range. A forecast adds a model, so say what kind of claim it is and show the spread, and none of it is trusted until it is scored. |
| z2 | 0.000 | 1 | Back to the positive test: 7.8% counts a thousand women like her moved by one test. It is one number because the evidence is good. |
| z3 | 0.000 | 1 | So where does a probability come from, and how can you tell whether it is any good? From a named group, moved by evidence, and by scoring many like it. |
| z4 | 0.000 | 1 | A scored number can still fail. The next video shows how. The listener hears a number other than the one you meant. |

## Review material

- Frames around every cut: `cuts.png` (156 frames)
- One frame per segment: `segments.png`

## Cost

Spent on this build: $0.0207. Total value of the generations the video uses (from receipts, cached or not): $0.4259. Unpriced items: [].

Machine verification is evidence for these gates only; it is not a substitute for watching the video.
