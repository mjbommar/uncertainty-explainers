# 6. Communicating uncertainty

Sources: S47 to S69 (see `research/keys.yaml` and `research/SOURCES.md`). Every quote below was checked with `uv run python research/tools.py verify <slug> "<quote>"` on 2026-09-23. Where the markdown conversion of a PDF is garbled (letters doubled, words fused, tables dropped), the quote was checked against the raw PDF text layer instead, and the entry says so.

## Key claims

- An estimate is a judgment, not a fact. Kent sorts intelligence statements into three kinds: near-certain fact, a judgment about something knowable but not known, and a judgment about something no one can yet know. [S47]
- The same words mean different numbers to different people, even inside one expert team. In 1951 the Board of National Estimates agreed on "serious possibility" for a Soviet attack on Yugoslavia. Asked afterwards, members had meant odds from 20 to 80 up to 80 to 20. Kent himself meant about 65 to 35 in favor of an attack. [S47]
- Kent's fix was a five-step odds table (plus certainty and impossibility at the ends), and a rule that "possible" must not be modified. His colleagues resisted it, and it was never printed in every estimate. [S47]
- A 1960s CIA survey of 240 analysts and 63 policy officers found agreement on "probable" and "likely", no agreement on "possible", "we believe" and "might", and that policy officers read words as lower probabilities than analysts did. [S48]
- Across National Intelligence Estimates from the 1950s to the 2000s, usage of estimative words was inconsistent, and the most frequent word was "will", a word of full certainty. [S49]
- Only 16 of 379 declassified NIEs (4 per cent) used any numeric probability. Friedman and Zeckhauser argue the goal is to assess uncertainty, not to remove it, and that vague likelihoods cause "probability neglect". [S66]
- Today the US intelligence community must use one of two fixed seven-step ladders tied to numeric ranges, and must not put a likelihood and a confidence level in the same sentence. [S50]
- The IPCC uses two separate measures: confidence (from evidence and agreement, expressed in words) and likelihood (a calibrated probability scale). [S51, S52]
- People read the IPCC words "regressively": they pull extreme terms toward 50%. In one US study the mean reading of "very likely" (meant as 90-100%) was 62, and of "very unlikely" (meant as 0-10%) was 41. Adding the number next to the word helped, but only somewhat. [S53]
- The effect differs across languages and cultures: Chinese readers of the translated IPCC terms were more regressive and more variable than British readers. [S54]
- For the ICD 203 ladder, readers matched the intended meaning only when the number sat in brackets beside the word (66% correspondence versus 32% with words alone). A clickable table or tooltip barely helped, because people did not open it. [S55]
- Communicating uncertainty has parts: who communicates, what the uncertainty is about (object, source, level, magnitude), in what form (expression, format, medium), to whom, and to what effect. There are three objects (facts, numbers, science), two levels (direct, indirect) and nine expressions of direct uncertainty, from a full distribution down to explicit denial. [S56]
- A number is not self-explaining. "30% chance of rain" was read as 30% of the time or 30% of the area by most people in four European cities. It means rain on 3 out of 10 days like this one. The missing piece is the reference class. [S60, S65]
- Frequencies make Bayesian reasoning easier than percentages. In the mammography problem, 95 of 100 physicians in Eddy's study guessed 70-80% when the answer is 7.8%. Stated as counts out of 1,000 women, naive participants reasoned correctly far more often (46% vs 16% Bayesian solutions). [S59]
- A probability can be right and still feel wrong. FiveThirtyEight gave Trump a 28-29% chance on the eve of the 2016 election, much higher than other models (15, 8, 2 and under 1 percent). An event with a 3-in-10 chance happens often. [S61, S62]
- A graphic can mislead as much as a word. The hurricane cone shows only where the storm center will probably go, sized so two-thirds of past track errors fall inside. In 2004 many people fixed on the "skinny black line" through the middle, and Charlotte County, inside the cone, was surprised by Hurricane Charley. [S63, S64]
- A vague phrase can change history. The Joint Chiefs judged the Bay of Pigs plan had "a fair chance of ultimate success". The author later said they meant about three in ten. Kennedy's circle read it as an endorsement, and the CIA quoted it in favor of the plan. [S67, S68, S69]
- Good practice: be clear about objectives, use absolute risks, state the reference class and time interval, use percent chance for single events, and have "the humility to admit uncertainty". [S57]

## Definitions in plain words

- **Estimate (Kent's sense).** A judgment about something not known for certain. It needs a qualifier word to show how sure the writer is. [S47]
- **Words of estimative probability.** Everyday words ("probable", "unlikely") used to state odds without giving a number. [S47, S49]
- **Likelihood.** How probable an event or outcome is. In IPCC and ICD 203 usage it is tied to a numeric range. [S50, S51]
- **Confidence.** How good the basis for a judgment is: how much evidence, how good, and how much experts agree. It is not a probability. The IPCC says it "should not be interpreted probabilistically". ICD 203 bans mixing it with likelihood in one sentence. [S50, S51]
- **Calibrated language.** A fixed list of words, each with an agreed numeric range, so that writer and reader mean the same thing. [S51, S52]
- **Regressive interpretation.** Reading extreme probability words as closer to 50% than intended. [S53, S54, S55]
- **Direct uncertainty.** Uncertainty about the fact or number itself, such as a range or a probability. [S56]
- **Indirect uncertainty.** Uncertainty about the quality of the evidence behind a claim, such as "low-quality evidence". [S56]
- **Epistemic vs aleatory (as van der Bles use them).** Epistemic: we do not know, but could in principle, usually about past or present facts. Aleatory: we cannot know because the outcome is still to be decided by chance. [S56]
- **Reference class.** The group of cases a probability counts over. "30% chance of rain" counts over days like tomorrow, not hours or square miles. [S60]
- **Natural frequencies.** Counts out of a whole ("8 of 10 women with cancer test positive") instead of conditional percentages. [S59]
- **Probability of precipitation (PoP).** The probability that a given forecast point gets at least 0.01 inch of rain in the forecast period. [S65]
- **Track forecast cone.** The area the center of a storm will probably pass through, built from circles along the forecast track, each sized so that two-thirds of past official track errors fall inside. [S64]

## The ladders

### Kent 1964 odds table [S47, PDF p. 8]

As printed ("set down in its classical simplicity thus"). The middle three rows sit under the bracket label "The General Area of Possibility".

| Probability | Give or take | Term |
|---|---|---|
| 100% | | Certainty |
| 93% | about 6% | Almost certain |
| 75% | about 12% | Probable |
| 50% | about 10% | Chances about even |
| 30% | about 10% | Probably not |
| 7% | about 5% | Almost certainly not |
| 0% | | Impossibility |

Checked: fragments "100% certainty", "Give or take almost", "93% Almost certain", "75% Probable", "Give or take about", "Chances about", "30% Probably not", "Almost certainly", "0% Impossibility" are all in the markdown, and the raw PDF p. 8 reads in order: "Give or take almost 93% Almost certain 6 %", "Give or take about 75% Probable 12 %", "Give or take about Chances about 50% ... 10 % even", "Give or take about 30% Probably not 10 %", "Give or take about 5 Almost certainly 7% % not". (Note the first row prints "Give or take almost" where the others say "about".)

Kent's worked example on the same page: "unlikely" means the chances of it happening "are about one in four", that is "around a 25-percent" chance. [S47, p. 8]

### ICD 203 (2015) likelihood ladder [S50, PDF p. 5]

"For expressions of likelihood or probability, an analytic product must use one of the following sets of terms":

| Range | Row 1 | Row 2 |
|---|---|---|
| 01-05% | almost no chance | remote |
| 05-20% | very unlikely | highly improbable |
| 20-45% | unlikely | improbable (improbably) |
| 45-55% | roughly even chance | roughly even odds |
| 55-80% | likely | probable (probably) |
| 80-95% | very likely | highly probable |
| 95-99% | almost certain(ly) | nearly certain |

Rules on the same page: "Analysts are strongly encouraged not to mix terms from different rows." Products that express confidence "must not combine a confidence level and a degree of likelihood, which refers to an event or development, in the same sentence."

Checked: the range string "01-05% 05-20% 20-45% 45-55% 55-80% 80-95% 95-99%" is in the markdown. The term rows and rule sentences were checked against the raw PDF text of p. 5; the markdown has doubled-letter artifacts ("t the", "n not"). Note that the ladder has no 0% or 100% step.

### IPCC AR5 likelihood scale (Table 1) [S51, PDF p. 5]

| Term | Likelihood of the outcome |
|---|---|
| Virtually certain | 99-100% probability |
| Very likely | 90-100% probability |
| Likely | 66-100% probability |
| About as likely as not | 33 to 66% probability |
| Unlikely | 0-33% probability |
| Very unlikely | 0-10% probability |
| Exceptionally unlikely | 0-1% probability |

Footnote to the table: "Additional terms that were used in limited circumstances in the AR4 (extremely likely – 95-100% probability, more likely than not – >50-100% probability, and extremely unlikely – 0-5% probability) may also be used in the AR5 when appropriate."

Checked against raw PDF p. 5. **The kaos-pdf markdown conversion dropped this table entirely**, so the markdown cannot be used for it. Note the ranges overlap (they are cumulative, "likely" includes "very likely"), unlike ICD 203's mutually exclusive bands. [S51, S55]

### IPCC AR5 confidence [S51, PDF pp. 3-5]

Two metrics: confidence in the validity of a finding, and quantified measures of uncertainty expressed probabilistically.

- Evidence is rated on "the type, amount, quality, and consistency of evidence (summary terms: “limited,” “medium,” or “robust”)", and agreement as "“low,” “medium,” or “high”" (p. 4).
- "A level of confidence is expressed using five qualifiers: “very low,” “low,” “medium,” “high,” and “very high.”" (p. 5)
- Figure 1 is a 3 x 3 grid: evidence (limited, medium, robust) on the horizontal axis, agreement (low, medium, high) on the vertical. "Confidence increases towards the top-right corner as suggested by the increasing strength of shading." (p. 5)

| | Limited evidence | Medium evidence | Robust evidence |
|---|---|---|---|
| **High agreement** | High agreement, limited evidence | High agreement, medium evidence | High agreement, robust evidence |
| **Medium agreement** | Medium agreement, limited evidence | Medium agreement, medium evidence | Medium agreement, robust evidence |
| **Low agreement** | Low agreement, limited evidence | Low agreement, medium evidence | Low agreement, robust evidence |

(Confidence rises toward the top-right cell. The figure's cell labels were read from the raw PDF text; the layout is reconstructed from the caption.)

### NWS probability of precipitation [S65]

The fetched NWS Peachtree City FAQ gives a point definition, not a formula: "The "Probability of Precipitation" (PoP) simply describes the probability that the forecast grid/point in question will receive at least 0.01" of rain." Its worked example: a forecast of "CHANCE OF RAIN 40 PERCENT" means "a 40 percent probability for at least 0.01" of rain at the specific forecast point of interest".

Checked against the raw HTML in `research/downloads/nws-pop-definition.html`. **The markdown conversion kept only the page navigation and dropped this FAQ text.** The often-quoted formula PoP = C x A (forecaster confidence times fraction of area) is **not** in this source; do not use it on screen without a new source. Gigerenzer et al. quote an older NWS Tulsa definition: "the likelihood of occurrence (expressed as a percentage) of a measurable amount of liquid precipitation . . . during a specified period of time at any given point in the forecast area". [S60, raw PDF p. 2]

## Quotable passages

Kent 1964 [S47]

> It makes the case, say, 90 percent of the way.

[S47], PDF p. 2 (the "almost certainly a military airfield" example), verified: yes.

> an attack on Yugoslavia in 1951 should be considered a serious possibility

[S47], PDF p. 3, NIE 29-51 key judgment, verified: yes.

> namely that the odds were around 65 to 35 in favor of an attack

[S47], PDF p. 4, Kent's own meaning, verified: yes.

> low man was thinking of about 20 to 80, the high of 80 to 20

[S47], PDF p. 4, the Board members' spread, verified: yes. (The markdown scrambles line order on this page. The raw sentence around it is: "each Board member had had somewhat different odds in mind and the low man was thinking of about 20 to 80, the high of 80 to 20. The rest ranged in between.")

> the precise mathematical language of the actuary or the race track bookie and a less precise though useful verbal equivalent

[S47], PDF p. 5, verified: yes.

> The first cardinal rule to emerge was thus, "The word `possible' (and its cognates) must not be modified."

[S47], PDF p. 6, verified: yes (checked as two fragments because of a page break in the markdown).

> I realize the truth in the above; I am not reconciled; I deplore it.

[S47], PDF p. 10, Kent on the "poets" who resist numbers, verified: yes.

Wark, CIA survey [S48]

> Responses were received from 240 intelligence analysts and 63 policy officers.

[S48], PDF p. 2, verified: yes.

> There was no satisfactory agreement on the meaning of possible or a wide variety of verb forms such as we believe and might.

[S48], PDF p. 2, verified: yes (raw PDF; markdown line breaks garbled).

> The policy offices consistently assigned lower probabilities than intelligence analysts did.

[S48], PDF p. 2, verified: yes.

Kesselman 2008 [S49]

> use of the word will has by far been the most popular for analysts, registering over 700 occurrences throughout the decades

[S49], PDF p. 6 (thesis abstract), verified: yes.

ICD 203 [S50]

> Degrees of likelihood encompass a full spectrum from remote to nearly certain.

[S50], PDF p. 5, section D.6.b.(2), verified: yes (raw PDF).

IPCC guidance note [S51]

> Confidence should not be interpreted probabilistically, and it is distinct from “statistical confidence.”

[S51], PDF p. 5, paragraph 9, verified: yes (raw PDF).

> “About as likely as not” should not be used to express a lack of knowledge

[S51], PDF p. 5, paragraph 10, verified: yes (raw PDF).

> there is evidence that readers may adjust their interpretation of this likelihood language according to the magnitude of perceived potential consequences

[S51], PDF p. 5, paragraph 10, verified: yes (raw PDF).

Budescu, Por and Broomell 2012 [S53]

> the public consistently misinterprets the probabilistic statements in the IPCC report in a regressive fashion

[S53], PDF p. 1, abstract, verified: yes (raw PDF; markdown abstract is line-reversed).

> The mean estimates for the four words are 41 for Very Unlikely, 44 for Unlikely, 54 for Likely, and 62 for Very Likely.

[S53], PDF p. 9, verified: yes (raw PDF).

> 24% of the respondents had no response consistent with the guidelines

[S53], PDF p. 9, verified: yes.

Harris et al. 2013 [S54]

> Whilst British interpretations differ somewhat from the IPCC’s prescriptions, Chinese interpretations differ to a much greater degree and show more variation.

[S54], PDF p. 2, abstract, verified: yes.

Wintle et al. 2019 [S55]

> Results indicate that correspondence with the ICD 203 standard is substantially improved only when numerical guidelines are bracketed in text. For this condition, average correspondence was 66%, compared with 32% in the control.

[S55], Abstract, verified: yes.

> two people can, and often do, have very different numbers in mind when they hear or read words of estimative probability

[S55], Introduction, verified: yes.

van der Bles et al. 2019 [S56]

> we identify three objects of uncertainty—facts, numbers and science—and two levels of uncertainty: direct and indirect. An examination of current practices provides a scale of nine expressions of direct uncertainty.

[S56], Abstract, verified: yes.

> Conclusion 2. The Intelligence Community did not accurately or adequately explain to policymakers the uncertainties behind the judgments in the October 2002 National Intelligence Estimate

[S56], section 1 (quoting the US Senate Select Committee on the 2002 Iraq NIE), verified: yes.

> Simply stated, there is no doubt that Saddam Hussein now has weapons of mass destruction

[S56], Table 1, expression (9) "explicit denial uncertainty exists" (Cheney, 26 August 2002), verified: yes.

> While there is some evidence that communicating epistemic uncertainty does not necessarily affect audiences negatively, impact can vary between individuals and communication formats.

[S56], Abstract, verified: yes.

Spiegelhalter 2017 [S57]

> which is a rise from 6 cases to 7 cases

[S57], PDF p. 2, sidebar "Is bacon as dangerous as cigarettes?" (an 18% relative increase in lifetime bowel cancer risk, from 6 in 100 to 7 in 100), verified: yes.

> Some of our intelligence officers thought that it was only a 40 or 30% chance that Bin Laden was in the compound.

[S57], PDF p. 18, quoting Obama; he ends "this is basically 50–50.", verified: yes (raw PDF for the first sentence; "this is basically 50–50." is in the markdown).

> Have the humility to admit uncertainty.

[S57], PDF p. 23, Conclusions, verified: yes.

> it is crucial to be clear about the reference class

[S57], PDF p. 23, Conclusions, verified: yes.

> Be cautious about interactivity and animations—they may introduce unnecessary complexity.

[S57], PDF p. 24, Conclusions (relevant to this video series), verified: yes (raw PDF).

> The take-home sound bite is simply to be clear about what you are trying to achieve, and check that you are doing it.

[S57], PDF p. 24, verified: yes.

Guardian/Observer review of *The Art of Uncertainty* [S58]

> Uncertainty, in Spiegelhalter’s view, is a *relationship* between an individual and the outside world.

[S58], review body, verified: yes.

Gigerenzer and Hoffrage 1995 [S59]

> Eddy (1982) reported that 95 out of 100 physicians estimated the posterior probability p(cancer | positive) to be between 70% and 80%, rather than 7.8%.

[S59], PDF p. 3, verified: yes (raw PDF; first clause checked, and "7.8%." checked on the same page).

> 10 out of every 1,000 women at age forty who participate in routine screening have breast cancer. 8 of every 10 women with breast cancer will get a positive mammography. 95 out of every 990 women without breast cancer will also get a positive mammography.

[S59], PDF p. 5, Table 1 (natural frequency format), verified: yes (raw PDF, each sentence checked separately).

Gigerenzer et al. 2005 [S60]

> Only in New York did a majority of them supply the standard meteorological interpretation

[S60], PDF p. 1, abstract, verified: yes (raw PDF).

> The preferred interpretation in Europe was that it will rain tomorrow “30% of the time,” followed by “in 30% of the area.”

[S60], PDF p. 1, abstract, verified: yes (raw PDF).

> “A percentage of days is most absurd.”

[S60], PDF p. 3, a Milanese respondent, verified: yes (raw PDF).

> It means that in 3 out of 10 times when meteorologists make this prediction, there will be at least a trace of rain the next day.

[S60], PDF p. 7, the authors' proposed wording, verified: yes (raw PDF).

FiveThirtyEight 2016 [S61, S62]

> Clinton is a 71 percent favorite to win the election according to our polls-only model and a 72 percent favorite according to our polls-plus model.

[S61], opening, archive snapshot of 2016-11-08, verified: yes (first clause checked; the markdown has link markup inside the sentence).

> put Trump’s chances about three times higher — 28 percent — this year?

[S61], opening (compared with Romney's 9 percent in 2012), verified: yes.

> had Trump with a 29 percent chance of winning the Electoral College.

[S62], opening, final forecast "issued early Tuesday evening", verified: yes.

> put Trump’s odds at: 15 percent, 8 percent, 2 percent and less than 1 percent.

[S62], opening (other models tracked by The New York Times), verified: yes.

> But people mistake having a large volume of polling data for eliminating uncertainty.

[S62], section "A small, systematic polling error made a big difference", verified: yes.

> The single most important reason that our model gave Trump a better chance than others is because of our assumption that polling errors are correlated.

[S62], section "Undecideds and late deciders broke for Trump", verified: yes.

NHC cone [S64]

> The cone represents the probable track of the center of a tropical cyclone

[S64], "Definition", verified: yes.

> The size of each circle is set so that two-thirds of historical official forecast errors over a 5-year sample fall within the circle.

[S64], "Definition", verified: yes.

Broad et al. 2007 [S63]

> Hurricane Charley ultimately struck Punta Gorda, about 70 miles south of Tampa

[S63], PDF p. 6, verified: yes (raw PDF; markdown fuses words, "ultimatelstruck").

> They were in the cone of uncertainty for four days

[S63], PDF p. 7, NHC director Max Mayfield, verified: yes (raw PDF).

> Of the articles reviewed, 42% stated that people should simply not focus on the line

[S63], PDF p. 9, verified: yes (raw PDF).

> Don't focus on the skinny black line

[S63], PDF p. 10, what Mayfield joked he should have on his tombstone, verified: yes (raw PDF).

Bay of Pigs [S67, S68, S69]

> Despite the shortcomings pointed out in the assessment, the Joint Chiefs of Staff consider that timely execution of this plan has a fair chance of ultimate success

[S68], FRUS 1961-63 vol. X doc. 35, JCSM-57-61, Joint Chiefs to McNamara, 3 February 1961, verified: yes.

> They have concluded that “this plan has a fair chance of ultimate success” (that is of detonating a major and ultimately successful revolt against Castro)

[S69], FRUS vol. X doc. 46, "Paper Prepared in the Central Intelligence Agency" (drafted by Bissell), 17 February 1961, verified: yes.

> The problem was that no one had a clear idea of what that judgment actually meant.

[S67], PDF p. 16 (book p. 3), verified: yes.

> Gray told Wyden that the Joint Chiefs believed that the odds of the invasion succeeding were roughly three in ten.

[S67], PDF p. 16, footnote 4, citing Peter Wyden, *Bay of Pigs: The Untold Story* (1979), pp. 88-90, verified: yes (checked as two fragments across a line break).

Friedman and Zeckhauser 2012 [S66]

> Of the 379 declassified NIEs surveyed for this article, only 16 (4 per cent) discuss probability using quantitative indicators of any kind.

[S66], PDF p. 14, verified: yes (raw PDF).

> Why not simply report those probability estimates in the first place?

[S66], PDF p. 14, verified: yes (raw PDF).

> Presenting likelihoods vaguely – or not presenting them at all – creates this very problem.

[S66], PDF p. 16, verified: yes (raw PDF).

## Numbers and stories for the screen

1. **"Serious possibility" (1951).** One phrase, one Board, readings from 20% to 80%. Kent meant 65%. The State Department reader had assumed much lower. [S47]
2. **Kent's ladder.** Five words, each with a number and a band: 93, 75, 50, 30, 7. [S47]
3. **"Fair chance" (1961).** Written meaning about 30%. Read as a go-ahead. After the failure Kennedy "wondered why no one had warned him". [S67, S68, S69]
4. **The Wark survey.** "Probably" got 75 from analysts, 70 from policy officers; "possible" got no agreement at all. The most frequent answer for "possibly" was 50. [S48]
5. **The Bin Laden raid.** Officers said 30-40%, others 80-90%; Obama concluded "basically 50–50". [S57]
6. **IPCC words read toward the middle.** "Very likely" is meant as 90-100%; readers averaged 62. "Very unlikely" is meant as 0-10%; readers averaged 41. [S51, S53]
7. **Brackets beat tables.** Put the number in the sentence: 66% agreement versus 32% without it. [S55]
8. **30% chance of rain.** In New York about two-thirds pick "30% of days like this"; in Amsterdam, Berlin, Milan and Athens only one-third to one-fifth do. [S60]
9. **Mammography.** Base rate 1%, hit rate 80%, false alarm 9.6%. Physicians guess 70-80%; the answer is 7.8%. As counts: of 1,000 women, 10 have cancer, 8 of them test positive; 95 of the 990 without cancer also test positive; so 8 of 103 positives have cancer. [S59]
10. **Bacon.** An 18% rise in relative risk sounds alarming; in absolute terms it is 6 people in 100 becoming 7 in 100. [S57]
11. **2016.** 71-72% Clinton the morning of the vote, 29% Trump in the final evening forecast, versus other models at 15, 8, 2 and under 1 percent. [S61, S62]
12. **Hurricane Charley, 2004.** The track line pointed at Tampa until the day of landfall. Charley hit Punta Gorda, about 70 miles south, as a category 4 storm with 145 mph winds, causing an estimated $15 billion in damage. Charlotte County had been inside the cone for four days. In similar risk zones, 53% evacuated in Tampa Bay and 31% in southwest coastal Florida. 38% of newspaper articles called it the "cone of probability", a name NHC does not use. [S63]
13. **The cone's rule.** Two-thirds of past errors fall inside each circle, so the center misses the cone about one time in three. For the 2026 Atlantic season the circle radius grows from 25 nautical miles at 12 hours to 200 at 120 hours. [S64]
14. **Four per cent.** Of 379 declassified NIEs, 16 gave any numeric probability. [S66]

## Candidate visuals

- **The spread bar.** A horizontal 0-100% axis. One label, "serious possibility", then a scatter of dots for each Board member between 20 and 80, and one dot for Kent at 65. Repeat with "fair chance" and a single dot at 30 labelled "what the author meant". [S47, S67]
- **Three ladders side by side.** Kent (5 steps, with bands), ICD 203 (7 exclusive bands, 1-99%), IPCC (7 overlapping bands, 0-100%). Show that the same word "likely" is 55-80% in one and 66-100% in the other. [S47, S50, S51]
- **The regression arrows.** IPCC intended ranges as bars, with arrows pulling the public's mean readings toward 50 (62 for "very likely", 41 for "very unlikely"). [S53]
- **Bracket vs table.** The same intelligence sentence shown twice, once with "(55-80%)" inline, once with a "see table" link; agreement rising from 32% to 66%. [S55]
- **Reference-class split screen.** One forecast, "30% chance of rain", then three animated readings: a clock 30% shaded, a map 30% shaded, a calendar of 10 similar days with 3 rainy. Only the calendar is right. [S60]
- **Icon array of 1,000 women.** 10 highlighted with cancer, 8 of those marked positive, 95 more marked positive among the rest. Zoom to the 103 positives: 8 of them. [S59]
- **Confidence grid.** The IPCC 3 x 3 evidence by agreement grid, shaded toward the top right, kept visually separate from the likelihood ladder. [S51]
- **The cone and its circles.** Build the cone from its circles (radii from the NHC table), then fade the center line out, and plot Charley's actual landfall inside the cone but away from the line. [S63, S64]
- **Nine expressions staircase.** van der Bles's nine forms as steps from "full probability distribution" down to "no mention" and "explicit denial", with one real example on each step. [S56]
- **Many worlds of 2016.** A grid of 10 election "runs", 3 of them red, to show what 29% looks like. [S62]

## Gaps and cautions

- The hurricane cone image itself was not downloaded, only the NHC definition page and its circle-size table. The page links an example graphic (Hurricane Helene) that would need its own fetch and license check before use. [S64]
- The Spiegelhalter 2024 book *The Art of Uncertainty* was not fetched. Only the Observer review [S58] is available; do not attribute specific book content beyond what the review quotes.
- The Gigerenzer 2005 per-city percentages are shown in Figure 1, which is an image. The text only gives "two-thirds" for New York and "one-third to one-fifth" elsewhere. Use those words, not invented bar heights. [S60]
- The NWS "C x A" formula for PoP is not in any fetched source. [S65]
- The "three in ten" Bay of Pigs number is secondhand: Friedman [S67] reports what Gray told Wyden in about 1976. The primary FRUS text [S68] says only "fair chance". Say "the officer who wrote it later said".
- The FiveThirtyEight numbers differ by time of day: 71-72% Clinton and 28% Trump in the morning snapshot [S61], 29% Trump in the final evening forecast [S62]. Pick one and name its time.
- Budescu et al. measured US respondents with IPCC AR4 sentences; the 41/44/54/62 means are for the control group of that study. [S53]
- Tooling: the kaos-pdf markdown for several PDFs in this area is unreliable (S50 doubled letters; S51 lost its likelihood table; S53 reversed lines; S59, S60, S63, S66 fused words and soft-hyphen breaks). For those, quotes were checked against the pdfium text layer of the raw PDF. `tools.py verify` does not strip the U+FFFE hyphen marker that pdfium emits, so some raw-PDF page lookups also returned empty until that character was removed. The S65 markdown dropped the FAQ body; the quote came from the raw HTML.
