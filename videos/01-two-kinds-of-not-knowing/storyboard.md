# Storyboard: Two kinds of not knowing

Slug `01-two-kinds-of-not-knowing`. Running time 215.8 s (6473 frames at 30 fps). Shape from `docs/STRUCTURE.md` (Video 1): opening scene and question, claim, map, four stops (bridge, vignette, takeaway), zoom-out. Seconds are from the built timeline (`output/timeline_summary.json`). `roadmap` is the shared scene in `pipeline/scenes_shared.py`; `three_unknowns`, `takeaway`, `object_cards`, `sort_bins`, `range_bar` and `level_scale` are in `pipeline/scenes_01_two_kinds_of_not_knowing.py`; `statement` is from `pipeline/scenes_03_saying_it_out_loud.py`; `quote_card` and `urn` from `pipeline/scenes.py`.

**Opening question** (s02, answered in the same words in s26): "When someone says they do not know, what exactly is it they do not know, and does the difference matter?"

**Takeaways** (spoken and on screen): 1. Chance stays. Ignorance can be closed with data. 2. A number needs a group of similar cases. Without one, there is none. 3. Where the odds are unknown, one number claims too much. People treat that differently, and so should a forecast. 4. So every forecast should first say where on the scale it stands.

## Pose the problem

### s01  (0.0 to 10.2 s, 10.2 s), vignette

- **Say:** Three people say, I do not know. One holds a die, one a sealed envelope. One is asked the price of copper in twenty years.
- **Scene:** `three_unknowns`; transition in: dissolve
- **Beats:** 'Three people', 'sealed envelope', 'price of copper'
- **Image:** `copper` (a small stack of three copper ingots), `die` (a single six-sided die, tilted to show three faces with pips), `envelope` (a closed paper envelope sealed with a round wax seal)
- **SFX:** none
- **Sources:** none (structure line, no new factual claim)

### s02  (10.2 to 18.2 s, 7.9 s), opening question

- **Say:** When someone says they do not know, what exactly is it they do not know, and does the difference matter?
- **Scene:** `three_unknowns`; transition in: cut
- **Beats:** 'what exactly'
- **Image:** `copper` (a small stack of three copper ingots), `die` (a single six-sided die, tilted to show three faces with pips), `envelope` (a closed paper envelope sealed with a round wax seal)
- **SFX:** none
- **Sources:** none (structure line, no new factual claim)

## Claim and map

### s03  (18.2 to 27.8 s, 9.6 s), claim

- **Say:** Uncertainty is not one thing. Two questions tell its kinds apart: chance or ignorance, and measurable or not.
- **Scene:** `statement`, lines "Uncertainty is not one thing. / Chance or ignorance? / Measurable or not?"; transition in: dissolve
- **Beats:** 'Uncertainty', 'chance or ignorance', 'measurable or not'
- **Image:** none
- **SFX:** none
- **Sources:** S01, S76

### s04  (27.8 to 36.6 s, 8.8 s), map

- **Say:** Four stops: chance or ignorance, measurable or not, unknown odds, and where a case sits.
- **Scene:** `roadmap`, mode `overview`, current -1; transition in: glide
- **Beats:** none (even spacing)
- **Image:** none
- **SFX:** none
- **Sources:** none (structure line, no new factual claim)

## Stop 1: Chance or ignorance?

### s05  (36.6 to 41.3 s, 4.8 s), bridge

- **Say:** Start with the die and the envelope, which fail for different reasons.
- **Scene:** `roadmap`, mode `travel`, current 0; transition in: dip
- **Beats:** none (even spacing)
- **Image:** none
- **SFX:** none
- **Sources:** none (structure line, no new factual claim)

### s06  (41.3 to 48.2 s, 6.9 s), vignette

- **Say:** More study of a die will not tell you the next roll. That is aleatory uncertainty.
- **Scene:** `object_cards`, heading "Chance or ignorance?"; transition in: dissolve
- **Beats:** 'study of a die', 'aleatory uncertainty'
- **Image:** `die` (a single six-sided die, tilted to show three faces with pips)
- **SFX:** custom: A single six-sided plastic die rolled across a woo... at "study of a die"
- **Sources:** S01

### s07  (48.2 to 57.6 s, 9.4 s), vignette

- **Say:** The number in the envelope is already fixed. Open it and the doubt is gone. That is epistemic uncertainty.
- **Scene:** `object_cards`, heading "Chance or ignorance?"; transition in: dissolve
- **Beats:** 'already fixed', 'epistemic uncertainty'
- **Image:** `die` (a single six-sided die, tilted to show three faces with pips), `envelope` (a closed paper envelope sealed with a round wax seal)
- **SFX:** paper at "Open it"
- **Sources:** S01, S56

### s08  (57.6 to 62.6 s, 5.0 s), takeaway

- **Say:** Chance stays. Ignorance can be closed with data.
- **Scene:** `takeaway`, line "Chance stays. Ignorance can be closed with data."; transition in: glide
- **Beats:** none (even spacing)
- **Image:** none
- **SFX:** none
- **Sources:** S01

## Stop 2: Can it be measured?

### s09  (62.6 to 70.3 s, 7.6 s), bridge

- **Say:** So ignorance can shrink and chance cannot. But even chance needs something to count.
- **Scene:** `roadmap`, mode `travel`, current 1; transition in: dip
- **Beats:** none (even spacing)
- **Image:** none
- **SFX:** none
- **Sources:** none (structure line, no new factual claim)

### s10  (70.3 to 78.5 s, 8.2 s), vignette

- **Say:** In 1921 Frank Knight pointed to fire insurance. Across many buildings, the loss evens out.
- **Scene:** `object_cards`, heading "Knight, 1921"; transition in: wipe
- **Beats:** 'Frank Knight', 'many buildings'
- **Image:** `house` (a small simple house with a pitched roof and one door)
- **SFX:** none
- **Sources:** S76, S02

### s11  (78.5 to 86.8 s, 8.3 s), vignette

- **Say:** A new venture has no such group. Knight called the first kind risk, and the second true uncertainty.
- **Scene:** `object_cards`, heading "Knight, 1921"; transition in: dissolve
- **Beats:** 'new venture', 'first kind risk', 'true uncertainty'
- **Image:** `house` (a small simple house with a pitched roof and one door), `venture` (a lightbulb with a small gear inside it, a new invention)
- **SFX:** none
- **Sources:** S02, S76

### s12  (86.8 to 96.0 s, 9.2 s), vignette

- **Say:** In 1937 John Maynard Keynes set roulette apart from a European war, or copper prices twenty years out.
- **Scene:** `sort_bins`, heading "Keynes, 1937"; transition in: push-left
- **Beats:** 'Keynes', 'European war', 'copper prices'
- **Image:** `copper` (a small stack of three copper ingots), `roulette` (a roulette wheel seen from above)
- **SFX:** soft_click at "European war"
- **Sources:** S04
- **Direction:** Say Keynes so it rhymes with canes.

### s13  (96.0 to 106.8 s, 10.8 s), vignette

- **Say:** About these, he wrote, "there is no scientific basis on which to form any calculable probability whatever. We simply do not know."
- **Scene:** `quote_card`; transition in: dissolve
- **Beats:** none (even spacing)
- **Image:** none
- **SFX:** low_pad at "0.0"
- **Sources:** S04
- **Direction:** Leave a short pause before the last four words.

### s14  (106.8 to 112.8 s, 6.1 s), takeaway

- **Say:** A number needs a group of similar cases. Without one, there is none.
- **Scene:** `takeaway`, line "A number needs a group of similar cases. Without one, there is none."; transition in: glide
- **Beats:** none (even spacing)
- **Image:** none
- **SFX:** none
- **Sources:** S02, S76

## Stop 3: What if the odds are unknown?

### s15  (112.8 to 119.4 s, 6.5 s), bridge

- **Say:** Knight and Keynes drew a hard line. Ellsberg tested the ground between.
- **Scene:** `roadmap`, mode `travel`, current 2; transition in: dip
- **Beats:** none (even spacing)
- **Image:** none
- **SFX:** none
- **Sources:** none (structure line, no new factual claim)

### s16  (119.4 to 130.0 s, 10.6 s), vignette

- **Say:** In 1961 Daniel Ellsberg offered two urns: a hundred red and black balls, mix unknown, or fifty of each.
- **Scene:** `urn`, heading "Ellsberg's two urns"; transition in: wipe
- **Beats:** 'Ellsberg', 'a hundred red', 'fifty of each'
- **Image:** none
- **SFX:** marbles at "fifty of each"
- **Sources:** S77

### s17  (130.0 to 142.6 s, 12.6 s), vignette

- **Say:** Whichever color they bet on, most people pick fifty of each. No single chance of red fits that. This is ambiguity: outcomes known, odds not.
- **Scene:** `range_bar`, heading "Ambiguity"; transition in: dissolve
- **Beats:** 'Whichever', 'No single chance', 'ambiguity'
- **Image:** none
- **SFX:** none
- **Sources:** S77, S23

### s19  (142.6 to 150.4 s, 7.8 s), takeaway

- **Say:** Where the odds are unknown, one number claims too much. People treat that differently, and so should a forecast.
- **Scene:** `takeaway`, line "Where the odds are unknown, one number claims too much."; transition in: glide
- **Beats:** 'Where the odds', 'People treat'
- **Image:** none
- **SFX:** none
- **Sources:** S77, S23

## Stop 4: Where does mine sit?

### s20  (150.4 to 157.9 s, 7.5 s), bridge

- **Say:** Chance, ignorance, no group, unknown odds: these are points on one scale.
- **Scene:** `roadmap`, mode `travel`, current 3; transition in: dip
- **Beats:** none (even spacing)
- **Image:** none
- **SFX:** none
- **Sources:** none (structure line, no new factual claim)

### s21  (157.9 to 164.7 s, 6.8 s), vignette

- **Say:** At the far end of that scale, in one team's words, "we do not even know that we do not know."
- **Scene:** `level_scale`, heading "From certainty to total ignorance"; transition in: push-left
- **Beats:** 'far end', 'we do not even'
- **Image:** none
- **SFX:** tick at "far end"
- **Sources:** S09, S08

### s22  (164.7 to 169.7 s, 5.0 s), takeaway

- **Say:** So every forecast should first say where on the scale it stands.
- **Scene:** `takeaway`, line "Every forecast should first say where on the scale it stands."; transition in: glide
- **Beats:** none (even spacing)
- **Image:** none
- **SFX:** chime at "every forecast"
- **Sources:** S09, S08

## Zoom out

### s23  (169.7 to 185.1 s, 15.3 s), chain of takeaways

- **Say:** Chance stays and ignorance can be closed, so say which. But a number needs a group of cases, and where odds are unknown, one number claims too much. So say where on the scale you stand.
- **Scene:** `roadmap`, mode `summary`, current 4; transition in: dip
- **Beats:** none (even spacing)
- **Image:** none
- **SFX:** none
- **Sources:** none (structure line, no new factual claim)

### s25  (185.1 to 194.7 s, 9.7 s), return to the opening

- **Say:** The die is chance, with a number. The envelope is ignorance, with a number waiting. Copper has no honest number.
- **Scene:** `three_unknowns`; transition in: dissolve
- **Beats:** 'The die is chance', 'The envelope is ignorance', 'Copper has'
- **Image:** `copper` (a small stack of three copper ingots), `die` (a single six-sided die, tilted to show three faces with pips), `envelope` (a closed paper envelope sealed with a round wax seal)
- **SFX:** none
- **Sources:** S04

### s26  (194.7 to 207.9 s, 13.1 s), answer to the opening question

- **Say:** When someone says they do not know, what exactly they do not know is a chance, a fact, or something no one can count. The difference matters: it decides what a number can mean.
- **Scene:** `three_unknowns`; transition in: cut
- **Beats:** 'the difference matters'
- **Image:** `copper` (a small stack of three copper ingots), `die` (a single six-sided die, tilted to show three faces with pips), `envelope` (a closed paper envelope sealed with a round wax seal)
- **SFX:** none
- **Sources:** none (structure line, no new factual claim)

### s27  (207.9 to 212.6 s, 4.7 s), hand-off

- **Say:** The next question is what a number can honestly say.
- **Scene:** `statement`, lines "What can a number / honestly say?"; transition in: dissolve
- **Beats:** none (even spacing)
- **Image:** none
- **SFX:** none
- **Sources:** none (structure line, no new factual claim)

## End card  (212.6 to 215.8 s)

- **Line:** Name the kind of not knowing first.
- **Note:** Next: From evidence to forecast
