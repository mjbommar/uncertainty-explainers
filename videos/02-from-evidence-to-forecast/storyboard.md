# Storyboard: From evidence to forecast

Video 2 of Uncertainty Explainers. Slug `02-from-evidence-to-forecast`. Built running time 391.1 s (6:31), 873 narrated words, 39 segments plus a 3.5 s end card.

Shape: `docs/STRUCTURE.md`, video 2. Opening question: *where does a probability come from, and how can you tell whether it is any good?* Claim: a probability is a summary of evidence, not a fact about the world. Five stops, each entered by a bridge over the shared `roadmap` scene (travel mode) and closed by a spoken takeaway shown as a `takeaway_line` card. The zoom-out reads the takeaways as one chain over `roadmap` in summary mode, returns to the 1,000 women, and answers the opening question in the same words.

| Stop | Takeaway (spoken and on screen) |
|---|---|
| 1. The group | A probability counts over a group. Name the group, or the number floats. |
| 2. The update | Start from how common it is, then let the test move you. Rare things stay rare after one test. |
| 3. The width | When evidence is thin, an honest summary is a range, not a point. |
| 4. The future | A forecast leans on the past and on a model. Say which kind of claim it is, and show the spread. |
| 5. The score | One outcome proves nothing. Many forecasts, scored, do. |

Seconds are the built spans from `output/timeline_summary.json` (narration, hold and transition). Scenes marked (v2) live in `pipeline/scenes_02_from_evidence_to_forecast.py`; `roadmap` is shared, in `pipeline/scenes_shared.py`.

Illustrations (ours, not reported by a source): the 1,000-women counts are the source's own natural-frequency version; the dot-and-range pictures of the coins and Ellsberg's urn are drawn from the sources' stated values; the paths in the ensemble and divergence plots are schematic, not ECMWF or Lorenz output. Takeaways, bridges, the claim, the map and the zoom-out are reasoning over the cited segments and carry no source of their own.

## Pose the problem  (0.0 to 29.5 s, 29.5 s)

### open1  (0.0 to 6.3 s, 6.3 s)

- **Say:** A woman of forty goes for routine breast screening. The test comes back positive.
- **Scene:** `card_row` (v2); Routine screening, a positive test
- **Beats:** woman of forty, positive
- **Image:** patient, test_result
- **Sfx:** none
- **Sources:** S59
- **Transition in:** dissolve

### open2  (6.3 to 16.7 s, 10.4 s)

- **Say:** In a study reported in 1982, ninety-five of a hundred physicians put her chance of cancer at seventy to eighty percent.
- **Scene:** `interval_rows` (v2); Her chance of cancer, after a positive test
- **Beats:** seventy to eighty
- **Image:** none
- **Sfx:** none
- **Sources:** S59
- **Transition in:** glide

### open3  (16.7 to 24.2 s, 7.4 s)

- **Say:** The right answer is under eight percent. Same evidence, and a number ten times too big.
- **Scene:** `interval_rows` (v2); Her chance of cancer, after a positive test
- **Beats:** right answer, under eight
- **Image:** none
- **Sfx:** soft_click at "under eight"
- **Sources:** S59
- **Transition in:** cut

### open4  (24.2 to 29.5 s, 5.4 s)

- **Say:** So where does a probability come from, and how can you tell whether it is any good?
- **Scene:** `title_card`; Where does a probability come from?
- **Beats:** reveal only
- **Image:** none
- **Sfx:** none
- **Sources:** none (structure: reasoning over cited segments)
- **Transition in:** dissolve

## Claim and map  (29.5 to 52.8 s, 23.3 s)

### claim  (29.5 to 41.1 s, 11.6 s)

- **Say:** A probability is a summary of evidence, not a fact about the world. So it can be built badly, it can claim too much, and it can be checked.
- **Scene:** `card_row` (v2); What a probability is
- **Beats:** summary of evidence, built badly, claim too much, checked
- **Image:** none
- **Sfx:** none
- **Sources:** none (structure: reasoning over cited segments)
- **Transition in:** dissolve

### map  (41.1 to 52.8 s, 11.7 s)

- **Say:** Five stops: what the number counts, how evidence should move it, when one number is too many, what it says about the future, and how we know it was good.
- **Scene:** `roadmap`; mode overview, current -1
- **Beats:** reveal only
- **Image:** none
- **Sfx:** none
- **Sources:** none (structure: reasoning over cited segments)
- **Transition in:** dissolve

## Stop 1: The group. What is the number counting?  (52.8 to 100.1 s, 47.3 s)

### b1  (52.8 to 57.3 s, 4.5 s)

- **Say:** To see where the doctors went wrong, start with what the number counts.
- **Scene:** `roadmap`; mode travel, current 0
- **Beats:** reveal only
- **Image:** none
- **Sfx:** none
- **Sources:** none (structure: reasoning over cited segments)
- **Transition in:** dissolve

### g1  (57.3 to 71.5 s, 14.2 s)

- **Say:** Counting needs a reference class, the group you count over. The philosopher Alan Hájek is a man, a non-smoker and a philosophy professor. Each group gives a different chance that he lives to eighty.
- **Scene:** `card_row` (v2); Which group is he in?
- **Beats:** reference class, non-smoker, philosophy professor
- **Image:** none
- **Sfx:** none
- **Sources:** S15
- **Transition in:** dissolve; direction: Say Hájek as HAH-yek.

### g2  (71.5 to 82.3 s, 10.8 s)

- **Say:** In 1814 Laplace counted five thousand years of sunrises, and put the odds of one more at nearly two million to one.
- **Scene:** `big_number` (v2); 
- **Beats:** five thousand years, nearly two million
- **Image:** sunrise
- **Sfx:** none
- **Sources:** S16
- **Transition in:** dissolve; direction: Say Laplace as la-PLAHSS.

### g3  (82.3 to 93.9 s, 11.5 s)

- **Say:** Anyone who knows what drives the days and seasons, he added, would put the odds far higher. Same sunrise, more evidence, a different number.
- **Scene:** `two_column_compare`; Same sunrise, two bodies of evidence
- **Beats:** he added, far higher
- **Image:** none
- **Sfx:** none
- **Sources:** S16
- **Transition in:** push-left

### t1  (93.9 to 100.1 s, 6.2 s)

- **Say:** A probability counts over a group. Name the group, or the number floats.
- **Scene:** `takeaway_line` (v2); A probability counts over a group. Name the group, or the number floats.
- **Beats:** reveal only
- **Image:** none
- **Sfx:** none
- **Sources:** none (structure: reasoning over cited segments)
- **Transition in:** dissolve

## Stop 2: The update. How should evidence move it?  (100.1 to 171.4 s, 71.3 s)

### b2  (100.1 to 105.3 s, 5.2 s)

- **Say:** The group matters. But the doctors had the right group, and missed.
- **Scene:** `roadmap`; mode travel, current 1
- **Beats:** reveal only
- **Image:** none
- **Sfx:** none
- **Sources:** none (structure: reasoning over cited segments)
- **Transition in:** dissolve

### u1  (105.3 to 115.4 s, 10.0 s)

- **Say:** Their error was how the test moved the number. Bayes' rule starts from the base rate, how common the disease is before any test.
- **Scene:** `card_row` (v2); How evidence moves a number
- **Beats:** Bayes' rule, base rate, before any test
- **Image:** none
- **Sfx:** none
- **Sources:** S21
- **Transition in:** wipe; direction: Bayes rhymes with days.

### u2  (115.4 to 122.4 s, 7.0 s)

- **Say:** Take a thousand women of forty in screening. Ten have breast cancer. That is the base rate.
- **Scene:** `icon_array` (v2); One thousand women, one test
- **Beats:** thousand women, Ten have
- **Image:** none
- **Sfx:** none
- **Sources:** S59
- **Transition in:** dissolve

### u3  (122.4 to 130.8 s, 8.5 s)

- **Say:** Eight of those ten test positive. Of the nine hundred and ninety without cancer, ninety-five also test positive.
- **Scene:** `icon_array` (v2); One thousand women, one test
- **Beats:** Eight of those, ninety-five
- **Image:** none
- **Sfx:** tick at "Eight of those"
- **Sources:** S59
- **Transition in:** cut

### u4  (130.8 to 139.5 s, 8.6 s)

- **Say:** So one hundred and three women test positive, and only eight of them have cancer. That is seven point eight percent.
- **Scene:** `icon_array` (v2); One thousand women, one test
- **Beats:** one hundred and three, only eight
- **Image:** none
- **Sfx:** chime at "seven point eight"
- **Sources:** S59
- **Transition in:** cut

### u5  (139.5 to 151.3 s, 11.8 s)

- **Say:** The disease is rare, so most positives come from healthy women. The doctors left out the base rate, as earlier research found people do most of the time.
- **Scene:** `interval_rows` (v2); Where seventy percent came from
- **Beats:** disease is rare, left out
- **Image:** none
- **Sfx:** none
- **Sources:** S59
- **Transition in:** dissolve

### u6  (151.3 to 162.2 s, 10.9 s)

- **Say:** Counts help. In Gigerenzer and Hoffrage's 1995 study, correct answers rose from sixteen percent with percentages to about half with counts.
- **Scene:** `bars` (v2); People who reasoned correctly
- **Beats:** sixteen percent, about half, with counts
- **Image:** none
- **Sfx:** none
- **Sources:** S59
- **Transition in:** glide; direction: Say Gigerenzer as GIG-er-en-tser.

### t2  (162.2 to 171.4 s, 9.2 s)

- **Say:** Start from how common it is, then let the test move you. Rare things stay rare after one test.
- **Scene:** `takeaway_line` (v2); Start from how common it is, then let the test move you. Rare things stay rare after one test.
- **Beats:** reveal only
- **Image:** none
- **Sfx:** none
- **Sources:** none (structure: reasoning over cited segments)
- **Transition in:** dissolve

## Stop 3: The width. When is one number too many?  (171.4 to 214.8 s, 43.5 s)

### b3  (171.4 to 176.1 s, 4.7 s)

- **Say:** Bayes gives one number, and for the test that was enough.
- **Scene:** `roadmap`; mode travel, current 2
- **Beats:** reveal only
- **Image:** none
- **Sfx:** none
- **Sources:** none (structure: reasoning over cited segments)
- **Transition in:** dissolve

### w1  (176.1 to 191.5 s, 15.4 s)

- **Say:** But one number can claim too much. A coin that landed heads in half of a hundred tosses gets one half. So may a coin never seen. Its honest summary is a range, zero to one.
- **Scene:** `interval_rows` (v2); Same number, different evidence
- **Beats:** A coin that, never seen, a range
- **Image:** none
- **Sfx:** none
- **Sources:** S23
- **Transition in:** dissolve

### w2  (191.5 to 200.9 s, 9.4 s)

- **Say:** Daniel Ellsberg's urn, from 1961, holds thirty red balls, and sixty black and yellow balls in an unknown mix.
- **Scene:** `ellsberg_urn` (v2); Ellsberg's urn, 1961
- **Beats:** urn, from 1961, sixty black
- **Image:** none
- **Sfx:** marbles at "thirty red"
- **Sources:** S77
- **Transition in:** dissolve

### w3  (200.9 to 208.6 s, 7.7 s)

- **Say:** The chance of red is one third. The chance of black is anywhere from zero to two thirds.
- **Scene:** `interval_rows` (v2); One urn, a dot and a range
- **Beats:** chance of red, chance of black
- **Image:** none
- **Sfx:** none
- **Sources:** S23
- **Transition in:** glide

### t3  (208.6 to 214.8 s, 6.2 s)

- **Say:** When evidence is thin, an honest summary is a range, not a point.
- **Scene:** `takeaway_line` (v2); When evidence is thin, an honest summary is a range, not a point.
- **Beats:** reveal only
- **Image:** none
- **Sfx:** none
- **Sources:** none (structure: reasoning over cited segments)
- **Transition in:** dissolve

## Stop 4: The future. What can it say about the future?  (214.8 to 277.9 s, 63.0 s)

### b4  (214.8 to 221.0 s, 6.2 s)

- **Say:** A range is honest about today. A forecast reaches into tomorrow.
- **Scene:** `roadmap`; mode travel, current 3
- **Beats:** reveal only
- **Image:** none
- **Sfx:** none
- **Sources:** none (structure: reasoning over cited segments)
- **Transition in:** dissolve

### f1  (221.0 to 231.6 s, 10.6 s)

- **Say:** That claim leans on the past. In 1748 David Hume wrote that every conclusion from experience assumes the future will be like the past.
- **Scene:** `induction_gap` (v2); The gap in induction
- **Beats:** leans on the past, David Hume, like the past
- **Image:** none
- **Sfx:** none
- **Sources:** S28
- **Transition in:** dissolve

### f2  (231.6 to 244.6 s, 12.9 s)

- **Say:** It also leans on a model. In 1963 Edward Lorenz showed that in a simple model of rising air, slightly different starts can grow into very different states.
- **Scene:** `divergence` (v2); Two runs, almost the same start
- **Beats:** reveal only
- **Image:** none
- **Sfx:** none
- **Sources:** S43
- **Transition in:** dissolve

### f3  (244.6 to 257.4 s, 12.9 s)

- **Say:** So Europe's main weather centre runs its model fifty times from slightly altered starts. When the runs agree, the weather is predictable. When they scatter, no firm forecast is possible.
- **Scene:** `spaghetti_plot`; An ensemble, 50 altered runs and one control
- **Beats:** fifty times, runs agree, scatter
- **Image:** storm
- **Sfx:** whoosh at "fifty times"
- **Sources:** S44
- **Transition in:** dissolve

### f4  (257.4 to 269.3 s, 11.9 s)

- **Say:** A forecast starts from the present. A projection holds only if its assumption holds. And a scenario is a plausible story, with no probability attached.
- **Scene:** `sort_table` (v2); Three kinds of claim about the future
- **Beats:** A forecast starts, A projection, a scenario
- **Image:** none
- **Sfx:** none
- **Sources:** S46
- **Transition in:** wipe

### t4  (269.3 to 277.9 s, 8.5 s)

- **Say:** A forecast leans on the past and on a model. Say which kind of claim it is, and show the spread.
- **Scene:** `takeaway_line` (v2); A forecast leans on the past and on a model. Say which kind of claim it is, and show the spread.
- **Beats:** reveal only
- **Image:** none
- **Sfx:** none
- **Sources:** none (structure: reasoning over cited segments)
- **Transition in:** dissolve

## Stop 5: The score. How do we know it was good?  (277.9 to 332.9 s, 55.1 s)

### b5  (277.9 to 283.2 s, 5.3 s)

- **Say:** So a forecast is a claim, and a claim can be graded.
- **Scene:** `roadmap`; mode travel, current 4
- **Beats:** reveal only
- **Image:** none
- **Sfx:** none
- **Sources:** none (structure: reasoning over cited segments)
- **Transition in:** dissolve

### k1  (283.2 to 300.5 s, 17.4 s)

- **Say:** The Brier score, from 1950, is the squared gap between forecast and outcome, and lower is better. In the Good Judgment Project, ninety percent cost zero point zero two if right, one point six two if wrong.
- **Scene:** `bars` (v2); What saying 90% costs
- **Beats:** zero point zero two, one point six two
- **Image:** none
- **Sfx:** none
- **Sources:** S34, S33
- **Transition in:** wipe; direction: Brier rhymes with higher.

### k2  (300.5 to 312.6 s, 12.1 s)

- **Say:** One miss can be bad luck. Over many forecasts the scores show calibration: the events you call seventy percent should happen seventy percent of the time.
- **Scene:** `calibration` (v2); Calibration
- **Beats:** reveal only
- **Image:** none
- **Sfx:** none
- **Sources:** S34
- **Transition in:** dissolve

### k3  (312.6 to 326.3 s, 13.7 s)

- **Say:** People often are not. In studies reviewed by Tversky and Kahneman in 1974, ranges given as ninety-eight percent sure missed about thirty percent of the time.
- **Scene:** `bars` (v2); Ranges given as 98% sure
- **Beats:** Tversky, thirty percent
- **Image:** none
- **Sfx:** none
- **Sources:** S32
- **Transition in:** glide

### t5  (326.3 to 332.9 s, 6.6 s)

- **Say:** One outcome proves nothing. Many forecasts, scored, do.
- **Scene:** `takeaway_line` (v2); One outcome proves nothing. Many forecasts, scored, do.
- **Beats:** reveal only
- **Image:** none
- **Sfx:** none
- **Sources:** none (structure: reasoning over cited segments)
- **Transition in:** dissolve

## Zoom out  (332.9 to 387.6 s, 54.6 s)

### z1  (332.9 to 354.9 s, 21.9 s)

- **Say:** A probability counts over a group, so name the group. Evidence moves it by Bayes' rule, so start from the base rate. But thin evidence earns a range. A forecast adds a model, so say what kind of claim it is, and show the spread. And none of it is trusted until it is scored.
- **Scene:** `roadmap`; mode summary, current 5
- **Beats:** reveal only
- **Image:** none
- **Sfx:** none
- **Sources:** none (structure: reasoning over cited segments)
- **Transition in:** dissolve; direction: Bayes rhymes with days.

### z2  (354.9 to 366.6 s, 11.7 s)

- **Say:** Back to the positive test. Seven point eight percent counts a thousand women like her, moved by one test. It is one number because the evidence is good.
- **Scene:** `icon_array` (v2); One thousand women, one test
- **Beats:** reveal only
- **Image:** none
- **Sfx:** none
- **Sources:** S59
- **Transition in:** dissolve

### z3  (366.6 to 379.1 s, 12.5 s)

- **Say:** So where does a probability come from, and how can you tell whether it is any good? From a named group, moved by evidence. And by scoring many like it.
- **Scene:** `title_card`; A named group, moved by evidence
- **Beats:** reveal only
- **Image:** none
- **Sfx:** none
- **Sources:** none (structure: reasoning over cited segments)
- **Transition in:** dissolve

### z4  (379.1 to 387.6 s, 8.5 s)

- **Say:** A scored number can still fail. The next video shows how: the listener hears a number other than the one you meant.
- **Scene:** `title_card`; Said, and heard
- **Beats:** reveal only
- **Image:** none
- **Sfx:** none
- **Sources:** none (structure: reasoning over cited segments)
- **Transition in:** dissolve
