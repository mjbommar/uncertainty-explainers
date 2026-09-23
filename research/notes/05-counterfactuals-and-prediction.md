# 5. Counterfactuals and prediction

Scope: Lewis-style counterfactuals, Pearl's ladder of causation, Rubin's potential
outcomes, scenario planning at Shell, Lorenz and sensitive dependence, ECMWF
ensembles, and the IPCC vocabulary for prediction, projection and scenario.
Keys resolve through `research/keys.yaml`. Every quote below was checked with
`research/tools.py verify` on 2026-09-23.

## Key claims

- A counterfactual is a claim about what would have happened if something had been different. It contrasts with an indicative claim about what is in fact the case. The Oswald pair shows the difference: one sentence is true and the other is, as far as we know, false. [S37]
- The standard philosophical account ties causation to counterfactuals: c caused e if, had c not happened, e would not have happened. This idea runs from Hume through David Lewis (1973). [S37]
- Lewis judged a counterfactual by looking at the "closest" possible worlds where the "if" part is true, where "closest" means "most similar to the actual world". The claim is true if the "then" part holds in all of those worlds. [S37]
- Lewis admitted that similarity is vague and argued that this vagueness matches the vagueness of counterfactuals themselves. [S37]
- Pearl sorts causal questions into three levels: association (seeing), intervention (doing), and counterfactual (imagining). A question at one level cannot be answered with information from a lower level only. [S38]
- Data on what happened cannot by itself answer "what if we change it?", because the change alters how people behave. Pearl's example is doubling a price. [S38]
- Rubin defines a causal effect for one unit as the difference between its outcome under treatment and its outcome under control. We can never observe both, because we cannot go back in time and give the other treatment. This is now called the fundamental problem of causal inference. [S39]
- Rubin's conclusion: randomize whenever possible, but carefully controlled nonrandomized data are a reasonable and necessary way to estimate causal effects in many cases. [S39]
- Wack wrote that planning based on forecasts worked in the stable 1950s and 1960s, but from the early 1970s forecasting errors became more frequent and sometimes huge. [S40]
- Shell's scenarios prepared management for the possibility of an oil crisis, though not its timing. When the 1973 embargo came, crude rose from about $2.50 to $11 in weeks. [S41] [S42]
- Scenarios are not predictions. IPCC says so directly, and Shell describes its method as imagining how events "might plausibly" shape the world rather than forecasting probable futures. [S46] [S42]
- Lorenz (1963) showed that in a simple deterministic model of convection, slightly different starting states can grow into very different states. He then examined what this means for very-long-range weather prediction. [S43]
- ECMWF answers this sensitivity with an ensemble: many forecasts from slightly perturbed starting states plus one unperturbed control. The medium-range ensemble has 50 members at 9 km resolution. [S44]
- When the ensemble members agree, the atmosphere is in a predictable state. When they scatter, no categorical forecast can be issued with any certainty. The spread is information, not noise. [S44]
- ECMWF calls the probability of an event "the most consistent way" to convey forecast uncertainty. It warns that the ensemble mean can hide a high-impact event. [S45]
- IPCC separates a climate prediction (an estimate of the actual future, starting from the present state) from a climate projection (a response conditional on an emissions scenario that may or may not happen). [S46]
- IPCC adds that even with arbitrarily accurate models and observations, a nonlinear system like the climate may have limits to predictability. [S46]
- Deep uncertainty means analysts do not know, or cannot agree on, the right model, the right probabilities, or how to value outcomes. Under those conditions RAND's Robust Decision Making drops "predict-then-act". It runs models on hundreds to thousands of sets of assumptions and looks for plans that do well across them. [S10] [S11] [S12]

## Definitions in plain words

- **Counterfactual.** A statement about what would be true if the past had been different. "If Oswald hadn't killed Kennedy, someone else would have." It cannot be checked by looking, because the "if" never happened. [S37]
- **Indicative conditional.** A statement about what is true given what we might learn about the actual world. "If Oswald didn't kill Kennedy, someone else did." [S37]
- **Possible world, closest world.** A complete way the world could have been. The closest worlds are the ones that differ least from the real one. [S37]
- **Association, intervention, counterfactual.** Pearl's three levels of causal questions: what does seeing X tell me; what happens if I do X; would Y have happened if X had been different. [S38]
- **Potential outcomes.** For one unit (a child, a patient), the outcome it would have with treatment and the outcome it would have without. The causal effect is the difference. Only one is ever seen. [S39]
- **Scenario.** A plausible, internally consistent story of how the future could develop. It carries no probability and is not a forecast. [S46]
- **Prediction or forecast (IPCC use).** An attempt to estimate the actual future evolution, starting from the present state. IPCC treats "climate prediction" and "climate forecast" as the same thing. [S46]
- **Projection.** A possible future path of some quantity, usually computed with a model, conditional on assumptions (such as an emissions scenario) that may or may not come true. [S46]
- **Ensemble.** A set of forecasts run from slightly different starting states, and sometimes with perturbed model physics, to show the range of outcomes. [S44]
- **Control member.** The one ensemble run started from the best, unperturbed analysis. [S44]
- **Spread.** How far the ensemble members differ from each other. On average, small spread goes with an accurate ensemble mean. [S44]
- **Deep uncertainty.** Uncertainty so basic that experts cannot agree on the model, the probabilities, or the values. [S10]

## Table: five ways of talking about states we cannot observe

| Term | Question it answers | Conditional on what | Can it be checked later? | Example | Source |
|---|---|---|---|---|---|
| Forecast (weather sense) | What will happen, with what probability? | The current observed state and the model | Yes, and scored (for example with a Brier score) | ECMWF probability that 10 m wind exceeds 20 m/s | [S44] [S45] |
| Prediction (IPCC sense) | What is the actual future evolution? | The present state of the system | Yes, against observations ("prediction quality/skill") | A seasonal or decadal climate prediction | [S46] |
| Projection | What would happen if this scenario unfolds? | An assumed path (emissions, policy, technology) | Only in part: the scenario itself may never happen | Warming under SSP5-8.5 | [S46] |
| Scenario | What futures are plausible and consistent? | A coherent set of assumptions about driving forces | No probability to check; it is judged by usefulness | Shell 1972-73 "what if the world faced an oil crisis?" | [S42] [S46] |
| Counterfactual | What would have happened had things been different? | A change to the actual past | Never directly; only through models, experiments or randomization | "Would Kennedy be alive had Oswald not shot him?" | [S37] [S38] [S39] |

The column that matters most for communication is "conditional on what". A projection
reported without its scenario sounds like a forecast. A scenario reported with a
number sounds like a prediction.

## Quotable passages

> If Oswald didn’t kill Kennedy, someone else did.

> If Oswald hadn’t killed Kennedy, someone else would have.

[S37], section 1 (examples 3 and 4, credited to Adams 1970). verified: yes

> an (actual) event *c* causes an (actual) event *e* just in case if *c* had not occurred, *e* would not have occurred.

[S37], section 2.1 "Metaphysics and Science". verified: yes

> David Lewis (1973b) measured closeness by *similarity*: the more similar a world is to the actual world, the closer it is.

[S37], section 5.1 "Closeness and Similarity". verified: yes

> for a counterfactual to be true, *all* of those closest (or sufficiently close) antecedent-worlds must be consequent worlds.

[S37], section 5.1. verified: yes

> Counterfactuals are notoriously vague. That does not mean we cannot give a clear account of their truth conditions.

[S37], section 5.4 "Objections to Similarity", quoting Lewis 1973b. verified: yes

> The levels are titled 1. Association, 2. Intervention, and 3. Counterfactual.

[S38], PDF page 1, "The Three Layer Causal Hierarchy". verified: yes

> The second level, Intervention, ranks higher than Association because it involves not just seeing what is, but changing what we see.

[S38], PDF page 1. verified: yes

> Such questions cannot be answered from sales data alone, because they involve a change in customers choices, in reaction to the new pricing.

[S38], PDF page 1 (the "double the price" example). verified: yes

> A typical question in the counterfactual category is “What if I had acted differently,” thus necessitating retrospective reasoning.

[S38], PDF page 1. verified: yes

> The basic conclusion is that randomization should be

[S39], PDF page 1, abstract. The sentence continues "employed whenever possible but that the use of carefully controlled nonrandomized data to estimate causal effects is a reasonable and necessary procedure in many cases." The second fragment, "use of carefully controlled nonrandomized data to estimate causal effects is a reasonable and nec", also verifies on PDF page 1. verified: yes (in two fragments, see cautions)

> Traditional planning was based on forecasts, which worked reasonably well in the relatively stable 1950s and 1960s.

> Since the early 1970s, however, forecasting errors have become more frequent and occasionally of dramatic and unprecedented magnitude.

[S40], opening paragraph (HBR free preview). verified: yes

> Shell’s management was prepared for the eventuality—if not the timing—of the 1973 oil crisis.

[S41], HBR editor's summary reproduced on the Marshall Foundation library page. verified: yes

> What if the world faced an oil crisis?

[S42], PDF page 8. verified: yes

> oil soared from around $2.50 to $11 in

[S42], PDF page 16. Full sentence in the source: "The price of crude oil soared from around $2.50 to $11 in a matter of weeks." It is split across a two-column layout, so only this fragment verifies as one string. verified: yes (fragment)

> DEEP IN OUR HEARTS, WE WOULD ALL CHOOSE A SCENARIO WITH NO SURPRISES

[S42], PDF pages 14, 15 and 39 (pull quote attributed to Wack). verified: yes

> it is found that nonperiodic solutions are ordinarily unstable with respect to small modifications, so that slightly differing initial states can evolve into considerably different states.

> The feasibility of very-long-range weather prediction is examined in the light of these results.

[S43], abstract. verified: yes

> an ensemble is formed of many different “perturbed” initial states and one unperturbed analysis (the control member, CTRL).

[S44], section "Structure and operation of the ensemble". verified: yes

> ensemble currently has 50 members and 9km resolution.

[S44], same section. Full text: "The [medium range] ensemble currently has 50 members and 9km resolution." verified: yes

> If the perturbed forecasts deviate significantly from the control member forecast and from each other, then the atmosphere can be considered to be in a rather unpredictable state.

[S44], section "Qualitative use of the ensemble". verified: yes

> An ensemble of forecasts produces a range of possible scenarios rather than a single predicted value.

[S44], caption of Fig5-1. verified: yes

> At short lead times the isolines are very tightly packed for forecasts because the spread of the ensembles is quite limited.

[S45], section "Spaghetti diagrams". verified: yes

> The most consistent way to convey forecast uncertainty information is by the probability of the occurrence of an event.

[S45], section "Probabilities". verified: yes

> High-impact events, which in the ensemble mean appear weak or absent, can be easily overlooked

[S45], section "Ensemble mean". verified: yes

> A climate prediction or climate forecast is the result of an attempt to produce (starting from a particular state of the climate system) an estimate of the actual evolution of the climate in the future

[S46], PDF page 9, entry "Climate prediction". verified: yes

> Climate projections are distinguished from climate predictions by their dependence on the emission/concentration/ radiative forcing scenario used

[S46], PDF page 9, entry "Climate projection". verified: yes

> Unlike predictions, projections are conditional on assumptions concerning, for example, future socio-economic and technological developments that may or may not be realized.

[S46], PDF page 30, entry "Projection". verified: yes

> Note that scenarios are neither predictions nor forecasts, but are used to provide a view of the implications of developments and actions.

[S46], PDF page 33, entry "Scenario". verified: yes

> Even with arbitrarily accurate models and observations, there may still be limits to the predictability of such a non-linear system

[S46], PDF page 30, entry "Predictability". verified: yes

> analysts do not know, or the parties to a decision cannot agree on, (1) the appropriate conceptual models

[S10], PDF pages 12 and 25. The definition goes on to (2) probability distributions and (3) how to value outcomes. verified: yes

> RDM rests on a simple concept. Rather than using computer models and data to describe a best-estimate future, RDM runs models on hundreds to thousands of different sets of assumptions to describe how plans perform in a range of plausible futures.

[S12], PDF page 1. verified: yes

> because they begin by seeking agreement regarding the likelihood of future states of the world and then use this agreement to provide a prescriptive ranking of policy alternatives.

[S11], PDF page 5, describing "predict-then-act" decision analysis. verified: yes

Count: 33 verified quote strings (some shown as pairs).

## Numbers and stories for the screen

- **ECMWF ensemble sizes** [S44]: medium range, 50 perturbed members at 9 km, out to 15 days. Sub-seasonal (46 days), 100 members plus control at 36 km. Seasonal (7 or 13 months), 50 members plus control. Initial-condition errors dominate "during the first five days or so".
- **The 41% rule** [S44]: the spread around any single member is about 41% larger than the spread around the ensemble mean. The control run falls outside the plume about 4% of the time, in theory. Good for a caution that "the main model run" is not special.
- **Spaghetti plot, 26 May 2017** [S45]: 500 hPa height, 560 dam contour. At T+30 hours the lines are tight. By T+144 hours (1 June 2017) they have spread but keep the general ridge pattern. A clean before-and-after image of uncertainty growing with lead time.
- **Ensemble mean hides the storm** [S45]: all members may show an intense low in different places, and the mean then shows a shallow, weak low. This is a direct argument for showing probabilities, not averages.
- **Shell 1973** [S41] [S42]: scenarios shared with management by 1973 asked "What if the world faced an oil crisis?" In September 1972 Wack gave a three-hour presentation of six scenarios drawn as a river forking into two streams, each splitting into three. The October 1973 embargo sent crude from about $2.50 to $11 in weeks. The HBR summary is careful: Shell was prepared for "the eventuality", not "the timing".
- **Rubin's reading test** [S39], paraphrase: a child given the enriched program would score 38 items; the same child given the regular program would score 34. The causal effect is 38 minus 34, or 4 items. Only one of the two scores can ever be recorded.
- **Pearl's ladder examples** [S38]: seeing ("What does a symptom tell me about a disease?"), doing ("What if I take aspirin, will my headache be cured?"), imagining ("Was it the aspirin that stopped my headache?").
- **Lorenz's rounding story**: NOT in S43. The downloaded text is the AMS abstract page; the full paper is a scanned PDF with no text layer. The well-known story (rerunning a model from a printout rounded to three decimals) comes from later accounts, not from this source. Do not script it on S43 alone.

## Candidate visuals

1. **Two-sentence split screen** (Oswald indicative vs. counterfactual). One is marked "true, as far as we know", the other "false, as far as we know". Viewers must see that only the verb mood changed. [S37]
2. **Spheres of worlds**: concentric rings around "our world". Highlight the closest ring where the "if" holds, then check whether the "then" holds everywhere in it. [S37]
3. **Three-rung ladder**: SEEING / DOING / IMAGINING, each with one plain example and its notation, P(y|x), P(y|do(x)), P(y_x|x',y'). An arrow shows that information flows down the ladder but not up. [S38]
4. **One child, two doors**: the same child walks through "enriched program" (38) and "regular program" (34). One door closes, grayed out as "never observed". [S39]
5. **Plume and spaghetti**: 51 thin lines leaving one starting point, tight at day 1 and fanned out by day 6. Then one line in red for the control, to show it is just one of many. [S44] [S45]
6. **The averaged-away storm**: 50 small lows in different spots, merged into one faint blob labelled "ensemble mean". [S45]
7. **The five-box sorter**: forecast, prediction, projection, scenario, counterfactual, each tagged with its "conditional on" label and a check mark or cross for "can be checked later". Built from the table above. [S46]
8. **River of scenarios**: Wack's river forking into two streams, then into three tributaries each, with one branch labelled "oil crisis" lighting up in October 1973. [S42]

## Gaps and cautions

- **Lorenz** [S43] is abstract only. His concluding paragraph on long-range prediction is not in the downloaded text, and neither is the rounding story. A text-layer copy of the paper, or a secondary source that quotes it, is needed before a script quotes Lorenz beyond the abstract.
- **Rubin** [S39] is badly garbled OCR (two columns interleaved, doubled letters). Only the abstract fragments verified as strings. The 38 vs. 34 example and "we can never observe both y(E) and y(C)" are readable in the markdown near PDF page 3, but the exact wording should be checked against the PDF image before on-screen quotation.
- **Wack** [S40] is the HBR paywalled page: only the opening paragraph and the author note are available. [S41] is an editor's summary, not Wack's text. The 1973 narrative rests on Shell's own retrospective [S42], which is corporate self-description and should be labelled as such.
- **Shell's "billions of dollars"** gain claim appears in S42 but in a two-column layout. It is Shell's own claim. Avoid it, or say "Shell says".
- **Lewis 1973** is used through the SEP entry [S37], not the book itself. The quotes attributed to Lewis are SEP's quotations of Lewis.
- **Pearl notation** for level 3 was mangled in extraction; take the symbols from the published figure, not from the markdown.
- **ECMWF numbers** [S44] describe the system "currently" (the page is tagged "FUG associated with Cy50r1"). Date them on screen ("as of 2026").
- **IPCC vocabulary conflict**: IPCC uses "forecast" and "prediction" as synonyms for climate, while weather services use "forecast" for probabilistic outlooks. The table uses the IPCC sense for "prediction" and the ECMWF sense for "forecast". A script should pick one term per concept and hold it.
