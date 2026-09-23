# Storyboard: Two kinds of not knowing

Slug `01-two-kinds-of-not-knowing`. Running time 176.7 s (5302 frames at 30 fps). Seconds are from the built timeline (`output/timeline_summary.json`); scenes live in `pipeline/scenes.py` and, for `object_cards`, `sort_bins`, `stacked_bars`, `range_bar` and `level_scale`, in `pipeline/scenes_01_two_kinds_of_not_knowing.py`.

## s01  (0.0 to 7.9 s, 7.9 s)

- **Say:** Some of what we do not know is chance. Some is ignorance. A forecast has to say which kind it faces.
- **Scene:** `title_card`
- **Beats:** none (even spacing)
- **Image:** none
- **SFX:** none
- **Sources:** none (framing line, no factual claim)

## s02  (7.9 to 20.1 s, 12.2 s)

- **Say:** Roll a fair die. No one can say what comes up next, and more study of the die will not help. Engineers call this aleatory uncertainty, from the Latin word for dice.
- **Scene:** `object_cards`, heading "Two kinds of not knowing"; transition in: dissolve
- **Beats:** 'Roll a fair die', 'aleatory uncertainty'
- **Image:** `die` (a single six-sided die, tilted to show three faces with pips)
- **SFX:** custom: A single six-sided plastic die rolled across a wooden table,... at "Roll a fair die"
- **Sources:** S01

## s03  (20.1 to 34.8 s, 14.6 s)

- **Say:** Now seal a number in an envelope. You do not know it either, but it is already fixed. Open the envelope and the doubt is gone. This is epistemic uncertainty: a gap in what we know, which more data could close.
- **Scene:** `object_cards`, heading "Two kinds of not knowing"; transition in: dissolve
- **Beats:** 'seal a number', 'epistemic uncertainty'
- **Image:** `die` (a single six-sided die, tilted to show three faces with pips), `envelope` (a closed paper envelope sealed with a round wax seal)
- **SFX:** paper at "seal a number"
- **Sources:** S01, S56

## s04  (34.8 to 45.3 s, 10.5 s)

- **Say:** Which kind we face depends on the model. Two engineers put it plainly in 2009: "It is the job of the model builder to make the distinction."
- **Scene:** `quote_card`; transition in: glide
- **Beats:** none (even spacing)
- **Image:** none
- **SFX:** none
- **Sources:** S01

## s05  (45.3 to 61.0 s, 15.7 s)

- **Say:** A second question is whether a chance can be measured at all. In 1921 the economist Frank Knight pointed to fire insurance. No one can say whether one building will burn. Across many buildings, the loss evens out, and an insurer can carry it.
- **Scene:** `object_cards`, heading "Knight, 1921"; transition in: wipe
- **Beats:** 'A second question', 'one building', 'many buildings'
- **Image:** `house` (a small simple house with a pitched roof and one door)
- **SFX:** none
- **Sources:** S76, S02

## s06  (61.0 to 71.0 s, 10.1 s)

- **Say:** A new business venture has no such group of similar cases. Knight called the measurable kind risk, and the kind that cannot be measured true uncertainty.
- **Scene:** `object_cards`, heading "Knight, 1921"; transition in: dissolve
- **Beats:** 'new business venture', 'measurable kind risk', 'true uncertainty'
- **Image:** `house` (a small simple house with a pitched roof and one door), `venture` (a lightbulb with a small gear inside it, a new invention)
- **SFX:** none
- **Sources:** S02, S76

## s07  (71.0 to 89.1 s, 18.1 s)

- **Say:** In 1937, John Maynard Keynes drew a similar line, with examples. Roulette, he wrote, is not uncertain in his sense. The length of a life is only slightly uncertain, and the weather only moderately. A European war is uncertain, and so is the price of copper twenty years ahead.
- **Scene:** `sort_bins`, heading "Keynes, 1937"; transition in: push-left
- **Beats:** 'Roulette', 'length of a life', 'the weather', 'European war', 'price of copper'
- **Image:** `copper` (a small stack of three copper ingots), `roulette` (a roulette wheel seen from above)
- **SFX:** soft_click at "European war"
- **Sources:** S04
- **Direction:** Say Keynes so it rhymes with canes.

## s08  (89.1 to 99.3 s, 10.1 s)

- **Say:** About these matters, he wrote, "there is no scientific basis on which to form any calculable probability whatever. We simply do not know."
- **Scene:** `quote_card`; transition in: dissolve
- **Beats:** none (even spacing)
- **Image:** none
- **SFX:** low_pad at "0.0"
- **Sources:** S04
- **Direction:** Slow down and leave a short pause before the last four words.

## s09  (99.3 to 116.3 s, 17.1 s)

- **Say:** In 1961 Daniel Ellsberg turned this into a bet. On the left, Urn One holds a hundred red and black balls, in a mix nobody tells you. On the right, Urn Two holds exactly fifty of each. Draw your color and you win a hundred dollars.
- **Scene:** `urn`, heading "Ellsberg's two urns"; transition in: wipe
- **Beats:** 'Ellsberg', 'a hundred red', 'Urn Two', 'fifty of each'
- **Image:** none
- **SFX:** marbles at "fifty of each"
- **Sources:** S77

## s10  (116.3 to 131.6 s, 15.3 s)

- **Say:** Most people would rather draw from Urn Two, whether they bet on red or on black. That choice treats red in Urn One as less likely than a half, and black as less likely too. The two chances would add up to less than one.
- **Scene:** `stacked_bars`, heading "What the choices imply"; transition in: glide
- **Beats:** 'Most people', 'red in Urn One', 'black as less', 'less than one'
- **Image:** none
- **SFX:** none
- **Sources:** S77

## s11  (131.6 to 146.3 s, 14.7 s)

- **Say:** No single probability fits those choices. The name for this is ambiguity: the probabilities themselves are unknown, or only partly known. In Urn One, the chance of red could be anything from zero to one.
- **Scene:** `range_bar`, heading "Ambiguity"; transition in: dissolve
- **Beats:** 'No single probability', 'ambiguity'
- **Image:** none
- **SFX:** none
- **Sources:** S23, S77

## s12  (146.3 to 160.8 s, 14.5 s)

- **Say:** These kinds lie along one scale, from complete certainty to total ignorance. Choosing a supermarket line sits near the measured end. Keeping an umbrella in the car, for rain you cannot put odds on, sits further along.
- **Scene:** `level_scale`, heading "From certainty to total ignorance"; transition in: push-left
- **Beats:** 'complete certainty', 'supermarket', 'umbrella'
- **Image:** none
- **SFX:** tick at "supermarket", tick at "umbrella"
- **Sources:** S09, S10

## s13  (160.8 to 172.2 s, 11.5 s)

- **Say:** At the far end is total ignorance, where, in one team's words, "we do not even know that we do not know." A forecast should first say where on this scale it stands.
- **Scene:** `level_scale`, heading "From certainty to total ignorance"; transition in: dissolve
- **Beats:** 'At the far end', 'total ignorance', 'A forecast'
- **Image:** none
- **SFX:** chime at "A forecast"
- **Sources:** S08, S09, S10

## End card  (172.2 to 176.7 s)

- **Line:** Name the kind of not knowing first.
- **Note:** Next: From evidence to forecast

