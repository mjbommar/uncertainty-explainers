# Synthesis: conceptions of uncertainty

This is the argument the three videos rest on. Every factual claim cites a key in
`SOURCES.md`. Quotes, page numbers and fuller detail are in `notes/01` to `notes/07`.
Numbers marked "our illustration" are worked examples built on a source's definitions, not
figures reported by the source.

The argument in one paragraph: "uncertain" names several different conditions. Some can be
measured with a probability, some can be bounded but not pinned down, and some cannot be
measured at all. Each kind enters at a different step on the way from evidence to a public
claim. Most failures of prediction and communication come from treating one kind as another.
A point number is given where only a range is honest. A projection is read as a forecast. A
vague word is read as a number the speaker never meant.

---

## (a) A taxonomy of uncertainty

The oldest split is between chance in the world and gaps in what we know. Engineers call
these aleatory and epistemic uncertainty. Epistemic uncertainty is the kind "the modeler
sees a possibility to reduce ... by gathering more data or by refining models." Aleatory
uncertainty is the kind the modeler "does not foresee the possibility of reducing" [S01].
The word aleatory comes from the Latin *alea*, dice [S01]. The split is a choice the
modeler makes, not a fact about nature: "It is the job of the model builder to make the
distinction" [S01]. The same annual wind speed can be treated as chance in one model and
as a knowledge gap in another [S01]. Philosophers make a similar three-way cut inside the
word "probability". It can mean support from evidence, a person's degree of confidence, or
a physical tendency "independently of what anyone thinks" [S15].

A second split asks whether the uncertainty can be measured at all. Knight (1921) said
uncertainty "must be taken in a sense radically distinct from the familiar notion of
Risk." He argued that a measurable uncertainty "is not in effect an uncertainty at all"
and kept the word for "cases of the non-quantitive type" [S76]. Keynes (1937) drew the line
with examples. Roulette and life expectancy are not uncertain in his sense. The price of
copper twenty years ahead is: "About these matters there is no scientific basis on which
to form any calculable probability whatever. We simply do not know" [S04].

Between those two ends there is a middle ground, where we can say something but not one
number. Ellsberg (1961) showed that people treat known odds and unknown odds differently,
even when no single probability can explain their choices [S77, S23]. Modelers later built
full scales that run from certainty to total ignorance [S08, S09].

| Kind | Plain meaning | Everyday case | Can more data shrink it? | Key sources |
|---|---|---|---|---|
| Aleatory (chance, variability) | Outcomes vary even when the process is known | The next roll of a fair die | No, as far as the model goes | [S01], [S08], [S15] |
| Epistemic (knowledge gap) | A fixed fact we do not know yet | Last year's true unemployment rate | Yes, in principle | [S01], [S56] |
| Knightian risk | Chance we can measure from a group of similar cases | Fire insurance on many similar houses | Already measured | [S76], [S02] |
| Ambiguity | We know the outcomes but not which probabilities apply | An urn with an unknown mix of colors | Sometimes | [S77], [S23] |
| Weight of evidence (Keynes) | How much evidence stands behind a probability, apart from where it points | Same 50-50 from 2 tosses or from 2,000 | Yes | [S03] |
| Indirect uncertainty | Doubt about the quality of the evidence behind a number | A shaky study behind a precise figure | Yes | [S56] |
| Model uncertainty | The model's form may be wrong, not just its inputs | Wind speed from a statistical fit versus from physics | Sometimes | [S01], [S08] |
| Scenario uncertainty | We can list possible futures but not give them probabilities | Several oil-price paths | Rarely | [S08], [S42] |
| Deep uncertainty | Experts do not know or cannot agree on the model, the probabilities, or how to value outcomes | Climate adaptation over 50 years | Not reliably | [S10], [S12], [S09] |
| Radical or "true" uncertainty | No basis for any number | "A European war" in Keynes's 1937 list | No | [S04], [S76], [S13] |
| Unknown unknowns | Possibilities nobody has thought of | Rumsfeld's third category | Only by surprise | [S06], [S07], [S08] |
| Linguistic vagueness | The words themselves have fuzzy edges | "Tall", "likely", "fair chance" | By defining terms | [S26], [S27], [S56] |

Three cautions for the script. First, "ontic" does not appear in our sources; they say
aleatory, variability or physical (notes/01, Gaps). Second, Hacking's "Janus-faced"
duality is not in our corpus, so do not attribute it on screen. The three concepts in the Stanford Encyclopedia of Philosophy (SEP)
[S15] carry the same point. Third, Knight and Keynes should not be merged. Knight asks
whether a group of similar cases exists [S76]. Keynes asks whether the evidence supports
any number, or even a ranking [S03].

"Unknown unknowns" is older than Rumsfeld. He said it at a 12 February 2002 briefing in
answer to a question about Iraq and terrorists [S06]. By 1968 United States defense
engineers already spoke of "known unknowns, and the unknown unknowns," and shortened the
second to "unk-unks" [S07]. Walker et al. give the same idea a formal slot, "total
ignorance", the state in which "we do not even know that we do not know" [S08].

## (b) How each kind maps to a formal treatment

Ordinary probability is additive. If two events cannot both happen, the chance of one or
the other is the sum of their chances [S23, S25]. It is the default, and for good reasons.
Cox's theorem shows that any rule for plausible reasoning that meets a few consistency
conditions works like probability theory, provided a plausibility is a single real number
[S19, S18]. Dutch book arguments show that betting prices which break the probability
rules can be exploited by a set of bets that loses money whatever happens [S20, S15]. The
first condition of Cox's theorem, one real number per belief, is exactly what the other
frameworks give up [S19].

A single number cannot tell two very different states of mind apart. Having watched 100
fair tosses and knowing nothing about a coin both give p(heads) = 0.5 [S23]. The
principle of indifference, which spreads belief evenly when you know nothing, also gives
different answers when the same question is described in different ways. For side length,
face area and volume of a cube, it gives 1/2, 1/4 and 1/8 for one event [S15]. Those two
problems are why the alternatives exist.

| Kind of uncertainty | Best-fit formal treatment | What it outputs | Source |
|---|---|---|---|
| Aleatory, with good frequency data | Frequency or propensity probability | One number | [S15], [S01] |
| Epistemic, with enough evidence to commit | Bayesian (subjective or logical) probability, updated by Bayes' rule | One number, revised as evidence arrives | [S17], [S18], [S21] |
| Ambiguity, thin or conflicting evidence | Imprecise probability: a set of probabilities (credal set) | An interval, lower and upper | [S23] |
| Evidence from partly reliable sources | Dempster-Shafer belief functions | Two numbers, belief ≤ plausibility | [S24], [S25] |
| Vague categories and words | Fuzzy sets and possibility theory | A degree of fit, which need not add to 1 | [S26], [S27] |
| Scenario and deep uncertainty | No probability. Scenarios, stress tests, robust decisions | A map of where a plan fails | [S08], [S12], [S11] |
| Unknown unknowns | None | Humility, monitoring, adaptive plans | [S09], [S08] |

Each alternative, in one line:

- **Imprecise probability.** Belief is a set of probability functions, sometimes pictured as a
  "credal committee." The lowest and highest members give an interval for each event
  [S23]. In SEP's words: "If only we had better evidence, a single probability function
  would do. But since our evidence is weak, we must use a set" [S23]. There is a cost. If
  you start from total ignorance, [0, 1], no evidence ever narrows the interval [S23].
- **Dempster-Shafer theory.** It builds belief about one question from probabilities about a
  related question, such as how reliable a witness is [S24]. A belief of zero means "no
  evidence for this," not "certainly false" [S24]. Ordinary probability is the special
  case where belief and plausibility meet [S25].
- **Possibility theory.** A fuzzy set gives each object a grade of membership between 0 and 1
  for categories like "tall men" [S26]. Possibility theory reads such a set as a limit on
  what a value could be [S27]. It measures something different from probability. In
  Zadeh's example, Hans can easily eat 3 eggs (possibility 1), but he usually eats 2, and
  the chance he eats 3 is 0.1 [S27]. Zadeh argued that the vagueness of natural language
  is mostly of this kind, not probabilistic [S27]. That matters for (e): "likely" is a
  vague category before it is a number.

The three alternatives are related. A possibility distribution is a special belief
function [S25]. Many results about updating carry over from probability to these other
systems [S21]. The practical rule for the videos: use one number when the evidence earns
it, an interval when it does not, and no number when you cannot even list the outcomes.

## (c) From evidence to a public claim

Every prediction passes through the same chain. Each link lets in its own kind of
uncertainty.

**1. Evidence.** Data carry measurement error and chance variation, which is aleatory
[S01]. They also carry doubts about their quality, which is indirect uncertainty [S56].
Keynes's point about weight belongs here. New evidence "will sometimes decrease the
probability of an argument, but it will always increase its 'weight'" [S03]. A 50-50 based
on a mountain of evidence and a 50-50 based on nothing are different claims.

**2. Inference to a belief.** Deduction alone gives certainty, and only about what is
already in the premises. Induction and abduction are ampliative: the conclusion says more
than the premises, so it can be false even when every premise is true [S30]. Hume showed
that every inference from experience assumes the future will resemble the past, and that
assumption cannot be proved from experience without circularity [S28, S29]. Abduction
picks the best explanation we have thought of, and can pick "the best of a bad lot" when
the truth is not on the list [S30]. This is where unknown unknowns enter the reasoning.
Everyday reasoning also withdraws conclusions when facts arrive. "Tweety is a bird, so
Tweety flies" is withdrawn on learning that Tweety is a penguin [S31].

**3. A number.** Bayes' rule says how evidence should move a probability [S21]. People
apply it badly. They ignore base rates, anchor on arbitrary numbers, and give ranges that
are too narrow [S32, S59]. Counting helps. In one study, correct Bayesian answers rose from
16 percent with percentages to 46 and 50 percent with natural frequencies [S59].

**4. A model and a forecast.** Models add model uncertainty and sensitivity to starting
conditions. Lorenz found that in a simple deterministic model of convection, slightly
different starting states can grow into very different states. He then examined "the
feasibility of very-long-range weather prediction" in that light [S43]. Weather centres
answer with an ensemble: many runs from slightly perturbed starting states [S44].
Scenario and deep uncertainty enter here too. The model may be the wrong model, and the
future may lie outside every scenario [S08, S10].

**5. Scoring.** A forecast can be checked only if it is stated so it can be wrong. The
Brier score, the mean squared gap between forecast probabilities and outcomes, rewards
forecasters who report what they actually believe [S34]. The Good Judgment Project found
that forecasters improved with probability training, working in teams, and grouping the
best 2 percent together [S34]. Even good forecasters were overconfident. Early forecasts of
100 percent came true only about 70 percent of the time [S34]. Judgment also carries noise,
meaning unwanted variation between people who should agree [S35].

**6. The public claim.** The last link turns a belief into words, numbers or a picture.
Here linguistic uncertainty enters, and it can undo every careful step before it. Section
(e) is about this link.

Two misreadings of the scientist's own tool belong at link 5 or 6. A 95 percent
confidence interval describes the procedure: 95 percent of intervals built this way would
contain the true value. It does not say there is a 95 percent chance that this interval
contains it [S36]. Yet 59 percent of researchers endorsed exactly that statement [S36].

## (d) Counterfactuals, forecasts, projections and scenarios

These are different kinds of claims, and a viewer should be able to sort them. The key
question is "conditional on what?"

| Term | Question it answers | Conditional on | Can it be checked later? | Example |
|---|---|---|---|---|
| Forecast | What will happen, and how likely is it? | The present observed state and a model | Yes, and it can be scored | the European Centre for Medium-Range Weather Forecasts (ECMWF) probability of high wind [S44], [S45] |
| Prediction (IPCC sense) | What is the actual future evolution? | The present state of the system | Yes | A seasonal climate prediction [S46] |
| Projection | What would happen if this scenario unfolds? | An assumed path of emissions, policy or technology | Only in part, since the scenario may never happen | Warming under a high-emissions pathway [S46] |
| Scenario | Which futures are plausible and consistent? | A coherent set of assumptions | No probability to check. It is judged by usefulness | Shell's 1972 "oil crisis" story [S42] |
| Counterfactual | What would have happened if things had been different? | A change to the actual past | Never directly. Only through models, experiments or randomization | "Had the treatment been given..." [S37], [S38], [S39] |

The IPCC is explicit. A projection is "conditional on assumptions" about the future, and
scenarios "are neither predictions nor forecasts" (notes/05, [S46]). Walker et al. make the
same point: scenarios "do not forecast what will happen in the future; rather they
indicate what might happen" [S08].

Counterfactuals are the hardest. Lewis judged "if A had happened, B would have happened"
by looking at the closest possible worlds in which A is true [S37]. Pearl puts
counterfactuals on the top rung of a three-rung ladder: seeing (association), doing
(intervention) and imagining (counterfactuals). A question on one rung cannot be answered
with data from a lower rung alone [S38]. Rubin defines a causal effect for one unit as
the difference between its outcome with treatment and without. Only one of those two
outcomes can ever be observed [S39]. In his reading-test illustration, a child would score
38 with the new program and 34 without, an effect of 4 items. The script should present
that as a paraphrase, since the scanned text of the paper is poor (notes/05). Every forecast about a policy is a
counterfactual about a future that has not happened: what happens if we do this rather
than that.

Deep uncertainty changes the question itself. Robust Decision Making drops "predict then
act." It tests a plan against many plausible futures and asks where the plan breaks
[S12, S11]. As RAND puts it, "predictions are often wrong, and relying on them can be
dangerous" [S12].

## (e) The communication problem

The same careful analysis can mean opposite things to speaker and listener. There are
two routes to failure. The first is vague words that each reader turns into a different
number. The second is honest numbers or pictures that readers take to mean something else.

### The word problem

Sherman Kent told the story himself. National Intelligence Estimate 29-51 (1951) said a
Soviet attack on Yugoslavia was a "serious possibility." When asked afterwards, members of
the Board that approved it gave meanings ranging from odds of 20 to 80 up to 80 to 20.
Kent had meant about 65 to 35 [S47]. His answer was a fixed table of words and odds.

**Kent 1964** [S47, PDF p. 8]

| Term | Probability | Give or take |
|---|---|---|
| Certainty | 100% | |
| Almost certain | 93% | about 6% |
| Probable | 75% | about 12% |
| Chances about even | 50% | about 10% |
| Probably not | 30% | about 10% |
| Almost certainly not | 7% | about 5% |
| Impossibility | 0% | |

Numbers stayed rare. Of 379 declassified National Intelligence Estimates studied by
Friedman and Zeckhauser, 16 gave any numeric probability [S66]. The 2015 directive ICD 203
now requires analysts to use one of two fixed sets of terms [S50].

**ICD 203 (2015)** [S50, PDF p. 5]

| Range | Term | Alternative term |
|---|---|---|
| 01-05% | almost no chance | remote |
| 05-20% | very unlikely | highly improbable |
| 20-45% | unlikely | improbable |
| 45-55% | roughly even chance | roughly even odds |
| 55-80% | likely | probable |
| 80-95% | very likely | highly probable |
| 95-99% | almost certain | nearly certain |

The directive also forbids combining a confidence level and a degree of likelihood in the
same sentence [S50]. The two carry different information. Likelihood is about the event.
Confidence is about the evidence behind the judgment, which is Keynes's weight again.

The IPCC made the same separation, with a different ladder.

**IPCC AR5 likelihood scale** [S51, PDF p. 5]

| Term | Likelihood of the outcome |
|---|---|
| Virtually certain | 99-100% |
| Very likely | 90-100% |
| Likely | 66-100% |
| About as likely as not | 33-66% |
| Unlikely | 0-33% |
| Very unlikely | 0-10% |
| Exceptionally unlikely | 0-1% |

AR4 terms also allowed: extremely likely 95-100%, more likely than not >50-100%,
extremely unlikely 0-5% [S51]. The IPCC ranges overlap, since "likely" includes "very
likely." The ICD 203 bands do not overlap. The same word can therefore mean different
numbers in the two systems. "Likely" is 55 to 80 percent in intelligence and 66 to 100
percent in climate science [S50, S51].

**IPCC confidence** [S51, pp. 3-5]. This is a separate scale. Evidence is rated limited,
medium or robust, and agreement low, medium or high. These combine into five confidence
levels, from very low to very high. Confidence is not a probability [S51].

Readers do not use these ladders as written. Asked to interpret IPCC sentences, people
pulled the words toward the middle. "Very likely", meant as 90 to 100 percent, averaged 62.
"Very unlikely", meant as 0 to 10 percent, averaged 41 [S53]. Chinese readers of the
translated terms pulled them to the middle more than British readers did [S54]. Putting the number in the sentence, as in "very likely
(90-100%)", worked better than a separate table. It raised agreement with the intended
meaning from 32 percent to 66 percent [S55]. A CIA survey found reasonable agreement on
"probable", with analysts at 75 percent and policy officers at 70. It found none on
"possible" [S48].

In accounting and law, the words are defined only by other words. Under FAS 5 (now ASC
450), a loss that is "probable" ("likely to occur") and can be reasonably estimated must
be booked. A "reasonably possible" loss ("more than remote but less than likely") must be
disclosed. A "remote" loss ("slight") needs neither [S71, S70]. None of these words carries
a number in the standard [S71]. The tax rule is the exception. Under FIN 48 (now in ASC
740), a position must be "more likely than not" to survive examination, and the amount
booked is the largest that is "greater than 50 percent likely" to be realized [S73].
Courts work the same way. In *Addington v. Texas* (1979) the Supreme Court described the
standard of proof as a way to share the risk of error. Under a preponderance of the
evidence, the parties "share the risk of error in roughly equal fashion". Under beyond a
reasonable doubt, "our society imposes almost the entire risk of error upon itself" [S75].
The Court did not attach numbers, and it admitted it did not know how jurors apply these
phrases [S75]. Fair value accounting grades its numbers by evidence instead. Level 1 is a
quoted market price, and Level 3 rests on "significant unobservable inputs" [S72]. That is
a confidence scale in all but name.

### The number and picture problem

Numbers are not safe either. People must know what a number is a probability *of*.

- **"30% chance of rain."** The National Weather Service defines it as the probability that
  the forecast point gets at least 0.01 inch of rain [S65]. In New York about two-thirds
  of people surveyed picked the intended meaning, "rain on 30 percent of days like this."
  In Amsterdam, Berlin, Milan and Athens only one-third to one-fifth did. Others took it as
  30 percent of the area or 30 percent of the time [S60]. The reference class, the set of
  cases the percentage counts over, was never stated.
- **Relative risk.** An 18 percent rise in relative risk from eating bacon sounds alarming.
  In absolute terms it means 6 people in 100 getting the disease becomes 7 in 100 [S57].
- **The hurricane cone.** The cone shows where the storm's *center* may go. It is sized so
  that about two-thirds of past track errors fall inside it, so the center leaves the cone
  about one time in three. It says nothing about how wide the storm's effects will be
  [S64]. In 2004 the forecast line for Hurricane Charley pointed at Tampa. Charley struck
  Punta Gorda, about 70 miles south, although Charlotte County had been inside the cone
  for four days. In similar risk zones, 53 percent evacuated around Tampa Bay but 31 percent
  in southwest coastal Florida [S63]. The line drew the eye, and the cone was read as the
  storm's size.
- **Averages that hide the extreme.** If every ensemble member shows an intense storm, each
  in a different place, the ensemble mean shows a shallow one. ECMWF calls event
  probabilities "the most consistent way" to convey forecast uncertainty [S45].

Van der Bles et al. give a framework for all of this. Say *what* you are uncertain about
(a fact, a number, a hypothesis). Say it in a *form* (a range, a probability, a verbal
phrase, a picture). Report *both* levels: direct uncertainty about the quantity, and
indirect uncertainty about the quality of the evidence [S56]. Spiegelhalter adds that
people read numbers best as expected frequencies, with an absolute baseline [S57].

## (f) Teachable moments

Each of these is a scene a video could dramatize. Each has numbers from our sources.

1. **"A fair chance" at the Bay of Pigs (1961).** The Joint Chiefs judged that the plan "has
   a fair chance of ultimate success" [S68]. The officer who drafted it later said he
   meant roughly three in ten, a warning. He regretted not insisting that numbers be used
   [S67]. The CIA quoted the phrase in favor of the plan [S69]. Kennedy came to believe the
   Chiefs had endorsed it, and after the collapse he wondered why no one had warned him
   [S67]. Visual: the phrase on a memo, with a 30 percent dial behind it that only the
   writer can see.

2. **"Serious possibility" (1951).** One phrase, one Board, readings from 20 percent to 80
   percent. Kent meant 65 [S47]. Visual: a number line with each reader's pin dropped on
   it, then Kent's table sliding in.

3. **Ellsberg's urn.** The urn holds 30 red balls and 60 black and yellow balls "in unknown
   proportion" [S77]. Most people bet on red rather than black. They then bet on black or
   yellow rather than red or yellow. The first choice implies red is more likely than
   black, and the second implies the reverse. "No numbers can jointly satisfy these two
   constraints" [S23]. The honest description is P(red) = 1/3 and P(black) anywhere from 0
   to 2/3 [S23]. Visual: a dot for red and a bar for black. Use Ellsberg's colors, not
   SEP's blue [S77].

4. **The sunrise and the cube.** Laplace's rule of succession puts the odds that the sun
   rises tomorrow at 1,826,214 to 1. He added at once that anyone who knows the physics
   would put them far higher [S16, S15]. In the cube factory, spreading belief evenly over
   side, area or volume gives 1/2, 1/4 or 1/8 for one event [S15]. Visual: one cube, three
   answers.

5. **The 1,000 women.** 10 have breast cancer, and 8 of them test positive. 95 of the 990
   healthy women also test positive. Only 8 of the 103 positives are real, 7.8 percent. In
   Eddy's study 95 of 100 physicians said 70 to 80 percent [S59]. Visual: an icon array of
   1,000.

6. **The 2016 election.** FiveThirtyEight's final forecast gave Clinton about 71 percent
   and Trump about 29 percent. Other models gave Trump 15, 8, 2 and under 1 percent
   [S61, S62]. A 29 percent event happens more than one time in four. Visual: a
   ten-sided die with three faces red; roll it. The lesson is calibration, not vindication.
   One outcome cannot prove a probability right or wrong. Many forecasts, scored, can [S34].

7. **The spaghetti plot.** ECMWF runs 50 perturbed forecasts plus a control at 9 km
   resolution [S44]. On 26 May 2017 the lines were tight at 30 hours. By 144 hours they had
   spread, while keeping the broad pattern [S45]. Pair with Lorenz's finding that small
   differences in starting states grow [S43]. Visual: the lines fanning out as the clock
   runs.

8. **The cone of uncertainty.** Two-thirds of past errors fall inside it. Charley missed the
   line by about 70 miles but stayed in the cone. Evacuation was 53 percent in Tampa Bay and
   31 percent in southwest Florida [S64, S63]. Visual: a storm walking off the line but
   inside the cone, with a third of simulated tracks leaving the cone entirely.

9. **The 30 percent of what?** One forecast, three readings: days, area, time [S60, S65].
   Visual: three splits of the same map.

10. **The accountant's ladder and the court's ladder.** Probable means book it. Reasonably
    possible means tell readers. Remote means nothing [S71]. Preponderance shares the risk
    of error roughly equally. Beyond a reasonable doubt puts almost all of it on society
    [S75]. Neither ladder has numbers, except the tax rule's "greater than 50 percent" [S73].
    Visual: the same unlabeled slider, with four professions writing different words on it
    (Kent, ICD 203, IPCC, Financial Accounting Standards Board, FASB).

Supporting scenes, if time allows. Shell's 1972 scenarios asked "what if the world faced
an oil crisis?" When the 1973 embargo came, crude rose from about $2.50 to $11 in weeks.
Shell was ready for "the eventuality", not the timing [S42, S41]. RAND tested a water plan
against 200 plausible futures, and it failed in 120 [S12]. A wheel of fortune landing on 10
or on 65 moved median estimates of African countries in the UN from 25 percent to 45
percent [S32]. In a Brier score, saying 90 percent costs 0.02 if right and 1.62 if wrong
[S34]. Our illustration: a forecaster who always says 100 percent, and is right three
days in four, scores the same as a coin flip.

## (g) Three videos

The cut follows the chain in (c): what kind of not-knowing we face, how it becomes a
number or a range, and how it is said to others. Each video stands alone. Together they
run about 24 minutes.

### Video 1. "Two kinds of not knowing" (about 7 minutes)

**Thesis:** Some uncertainty is chance and some is ignorance, some can be measured and
some cannot, and the first job of any forecast is to say which kind it faces.

Beats:
1. The die and the sealed envelope (aleatory and epistemic) [S01].
2. Knight's insured houses and the new venture [S76].
3. Keynes: roulette against copper prices, and "We simply do not know" [S04].
4. Ellsberg's urn [S77, S23].
5. The ladder from certainty to total ignorance: Level 2 is the supermarket line, Level 3
   the umbrella in the trunk [S09, S08].
6. Known unknowns, with the 1968 origin [S06, S07].
7. Deep uncertainty and the 200 futures of the water plan [S10, S12].

Sources: S01, S03, S04, S06-S10, S12, S13, S15, S23, S56, S76, S77.

### Video 2. "From evidence to forecast" (about 8 minutes)

**Thesis:** A probability is a disciplined summary of evidence, not a fact about the
world. It must be honest about its reference class and its width, and it must be stated
so it can be scored.

Beats:
1. What "probability" means: frequency, degree of belief, tendency. The sunrise and the
   cube [S15, S16].
2. Bayes with 1,000 women [S59, S21].
3. Why a single number sometimes lies: intervals for Ellsberg, and the Betty-and-Sally
   witnesses [S23, S24].
4. Induction's gap and "the best of a bad lot" [S28, S30].
5. Lorenz and the spaghetti plot [S43, S44, S45].
6. Forecast, projection, scenario, counterfactual: the sorting table [S46, S38, S39, S42].
7. Scoring: Brier, calibration, superforecasters, and the early 100 percent that came true
   70 percent of the time [S34, S32].

Sources: S15, S16, S18-S21, S23, S24, S28, S30, S32, S34, S38, S39, S42-S46, S59.

### Video 3. "Saying it out loud" (about 9 minutes)

**Thesis:** Uncertainty is not communicated until the listener holds the same number the
speaker meant. Words alone rarely do that, so pair every word with a number, a reference
class and a statement of confidence.

Beats:
1. "A fair chance," 1961 [S68, S67, S69].
2. "Serious possibility," 1951, and Kent's table [S47].
3. ICD 203 and the IPCC ladders side by side. "Likely" means two different ranges [S50,
   S51].
4. How readers pull the words to the middle, and the bracket fix [S53, S55].
5. "30% chance of rain" of what [S60, S65].
6. The hurricane cone and Charley [S64, S63].
7. 2016, 71 against 29 [S61, S62].
8. The accountant's and the court's ladders [S71, S73, S75].
9. Van der Bles's checklist: what, in what form, and how sure of the evidence [S56, S57].

Sources: S47, S48, S50, S51, S53-S57, S60-S65, S67-S69, S70, S71, S73, S75.

### Open items for the script writer

- Quote Knight from [S76], not the scrambled FRASER conversion [S02]. Lorenz [S43] is an
  abstract only, so the rounding story needs a new source.
- The National Weather Service (NWS) formula "PoP = C x A" is not in [S65], and ASC 820 Level 2 is not described in
  [S72]. Keep both off screen until a source is added.
- Kay and King [S13] and Spiegelhalter 2024 [S58] are reviews. Attribute any book quote
  "as quoted in."
