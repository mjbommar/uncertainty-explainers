# 1. Kinds of uncertainty

Scope: aleatory and epistemic uncertainty; Knight's risk and uncertainty; Keynes on
unmeasurable probability, weight of evidence, and "we simply do not know"; Ellsberg's
ambiguity; known and unknown unknowns; deep uncertainty and its levels; Kay and King's
radical uncertainty; Taleb's black swans; linguistic uncertainty; model uncertainty; and
uncertainty about uncertainty. Keys are from `research/keys.yaml`. Every quote below was
checked with `uv run python research/tools.py verify <slug> "<quote>"` on 2026-09-23.

## Key claims

- Engineers sort uncertainty into two kinds. Epistemic uncertainty could be reduced with more data or better models. Aleatory uncertainty cannot be reduced, as far as the modeler can see. [S01]
- The sorting is a modeling choice, not a fact about nature. The same quantity can be aleatory in one model and epistemic in another. Der Kiureghian and Ditlevsen's example is a tower designer's annual maximum wind speed. [S01]
- Getting the category wrong has a price. Treating epistemic uncertainty as aleatory can hide dependence between events. This can misstate a failure probability by orders of magnitude. [S01]
- Philosophers name three concepts under the word "probability": evidential support, an agent's degree of confidence, and a physical tendency in the world. The aleatory and epistemic split maps roughly onto physical and the other two. [S15]
- Knight (1921) separated measurable uncertainty, which business can insure or pool away, from unmeasurable "true uncertainty". He argued that true uncertainty is the source of profit. [S02]
- For Knight, most business decisions are too unique to form a group of similar cases, so an objective probability does not apply. [S02]
- Keynes (1921) argued that some probabilities cannot be given numbers, or even ranked against each other. His example is whether to take an umbrella when the barometer is high but the clouds are black. [S03]
- Keynes also separated a probability from the weight of the evidence behind it. New evidence can move a probability up or down, but it always adds weight. This is an early statement of "uncertainty about uncertainty". [S03]
- Keynes (1937) drew the line with examples. Roulette, life expectancy, and even the weather are not "uncertain" in his sense. A European war, the price of copper in 20 years, and the social system in 1970 are. [S04]
- Ellsberg (1961) showed that people prefer a bet with known odds to one with unknown odds. The resulting pattern of choices fits no single probability assignment, which is why it is called ambiguity aversion. [S05, S23]
- The Ellsberg pattern can be represented with a set of probabilities: red is exactly 1/3 and black and yellow are each anywhere in [0, 2/3]. This is the entry point to imprecise probability (note 3). [S23]
- Rumsfeld's 2002 "unknown unknowns" line came in answer to a question about evidence of Iraq supplying terrorists with weapons of mass destruction. [S06]
- The phrase predates Rumsfeld. It was common in US defense procurement by the late 1960s, including a 1968 remark by Lt. Gen. William B. Bunker. Engineers shortened it to "unk-unks". [S07]
- Walker et al. (2003) define uncertainty as any departure from complete determinism. They classify it on three axes: location (where in the model), level (from determinism to total ignorance), and nature (knowledge versus variability). [S08]
- The Walker levels run: statistical uncertainty, scenario uncertainty, recognized ignorance, total ignorance. Scenario uncertainty begins where outcomes can be listed but not given probabilities. [S08]
- Marchau et al. (2019) restate the scale as Level 1 to Level 4 (split into 4a and 4b), between complete certainty and total ignorance. Levels 4a and 4b are "deep uncertainty". [S09]
- Deep uncertainty (RAND) is when the parties to a decision do not know, or cannot agree on, the right models, the probability distributions, or how to value outcomes. [S10, S12]
- Robust Decision Making (RDM) reverses "predict then act". It tests a plan against hundreds or thousands of plausible futures and looks for the conditions under which it fails. [S12, S11]
- Kay and King call the unquantifiable kind "radical uncertainty". They argue that economics wrongly folded it into quantifiable risk after Ramsey and Savage "won the argument" (per a review; the book itself is not in our corpus). [S13]
- Taleb's black swan is an outlier beyond normal expectations, with extreme impact, that people explain only after the fact. [S14, S09]
- Van der Bles et al. separate direct uncertainty (about a fact or number) from indirect uncertainty (about the quality of the evidence). Indirect uncertainty is a practical name for uncertainty about uncertainty. [S56]
- Linguistic uncertainty, meaning ambiguity about what words mean, is a separate source again. Van der Bles lists it among everyday uses of "uncertain". Zadeh's fuzzy sets start from vague classes such as "tall men" (note 3). [S56, S26]

## Definitions in plain words

- **Aleatory uncertainty**: variation we treat as chance, like the roll of a die. More study of the die will not tell us the next roll. The word comes from Latin *alea*, dice. [S01]
- **Epistemic uncertainty**: not knowing something that could, at least in principle, be found out. Examples are a measured constant or last year's unemployment rate. [S01, S56]
- **Ontic uncertainty**: another name for aleatory, meaning uncertainty "in the thing" rather than in our knowledge. Our sources use "aleatory", "variability uncertainty" [S08], or "physical" probability [S15]. None uses "ontic" itself; see Gaps.
- **Risk (Knight)**: uncertainty about outcomes whose chances can be measured, from logic or from a group of similar cases. Insurance handles it. [S02]
- **Uncertainty or true uncertainty (Knight; radical uncertainty, Kay and King)**: uncertainty that cannot be turned into a trustworthy number because there is no suitable group of similar cases. [S02, S13]
- **Weight of evidence (Keynes)**: how much relevant evidence stands behind a probability, as opposed to which way the evidence points. [S03]
- **Ambiguity (Ellsberg)**: uncertainty about which probabilities apply, as with an urn whose mix of colors is unknown. [S05, S23]
- **Known unknown**: a gap you know you have. **Unknown unknown**: a possibility you have not thought of at all. [S06, S07]
- **Model uncertainty**: error that comes from choosing the wrong form of a model, not from its inputs. Der Kiureghian lists it separately from parameter and measurement error. [S01]
- **Scenario**: a plausible, internally consistent description of how the future might develop. It is not a forecast. [S08, S09]
- **Deep uncertainty**: the experts do not know, or the parties cannot agree on, the model, the probabilities, or how to value the outcomes. [S10, S12]
- **Robust decision**: one that works acceptably across many plausible futures, rather than best in one predicted future. [S09, S12]
- **Direct and indirect uncertainty**: uncertainty about a number (a range or probability) versus uncertainty about how good the evidence for that number is. [S56]

## Quotable passages

> Uncertainties are characterized as epistemic, if the modeler sees a possibility to reduce them by gathering more data or by refining models.

[S01], PDF page 1 (abstract), verified: yes

> Uncertainties are categorized as aleatory if the modeler does not foresee the possibility of reducing them.

[S01], PDF page 1 (abstract), verified: yes

> The word aleatory derives from the Latin alea, which means the rolling of dice.

[S01], PDF page 2, section 1, verified: yes

> It is the job of the model builder to make the distinction.

[S01], PDF page 2, section 1, verified: yes

> ...is determined by our modeling choices.

[S01], PDF page 11, section 5 Conclusions (full sentence: "The distinction between aleatory and epistemic uncertainties is determined by our modeling choices"; the PDF splits "uncertainties" across a line, so only the tail verifies), verified: yes (tail)

> The conception of an objectively measurable probability or chance is simply inapplicable.

[S02], PDF page 241 (book p. 231, Ch. VII), verified: raw PDF text layer only. The markdown conversion of this PDF scrambles word order, so `found_in_markdown` is false. See Gaps.

> measurable uncertainties do not introduce into business any uncertainty whatever

[S02], PDF page 242 (book p. 232, Ch. VII), verified: raw PDF text layer only (same caveat)

> I am prepared to argue that on some occasions none of these alternatives hold, and that it will be an arbitrary matter to decide for or against the umbrella.

[S03], PDF page 44 (Ch. III §8, book pp. 31-32), verified: yes

> New evidence will sometimes decrease the probability of an argument, but it will always increase its 'weight.'

[S03], PDF page 91 (Ch. VI "The Weight of Arguments" §1), verified: yes

> there were 12 prizes of equal value, so that the average chance of success was about one in four

[S03], PDF page 40 (Ch. III, the *Chaplin v. Hicks* 1911 beauty contest case, quoting Lord Justice Vaughan Williams), verified: yes

> The game of roulette is not subject, in this sense, to uncertainty

[S04], QJE 1937 pp. 213-214 (HET transcription marks [p.214] mid-passage), verified: yes

> or the price of copper and the rate of interest twenty years hence

[S04], p. 214, verified: yes

> About these matters there is no scientific basis on which to form any calculable probability whatever. We simply do not know.

[S04], p. 214, verified: yes

> Urn I contains 100 red

[S05], PDF page 8 (QJE p. 650). Only this fragment verifies: the scan's OCR doubles letters ("50 r red a and 550 b black"). Use S23 for the full setup. verified: yes (fragment)

> I have an urn that contains ninety marbles. Thirty marbles are red. The remainder are blue or yellow in some unknown proportion.

[S23], section 2.1 "Ellsberg decisions", verified: yes

> No numbers can jointly satisfy these two constraints.

[S23], section 2.1, verified: yes

> there are known knowns; there are things we know we know. We also know there are known unknowns; that is to say we know there are some things we do not know. But there are also unknown unknowns -- the ones we don't know we don't know.

[S06], transcript, answer to the question on Iraq and terrorist links, verified: yes

> there are two kinds of technical problems: there are the known unknowns, and the unknown unknowns.

[S07], section on origins (Bunker, 1968, as quoted by Wikipedia), verified: yes

> industry shorthand to have developed where unknown-unknowns were referred to as "unk-unks"

[S07], section on origins, verified: yes

> a general definition of uncertainty as being any departure from the unachievable ideal of complete determinism.

[S08], PDF page 4, verified: yes

> the nature of uncertainty - whether the uncertainty is due to the imperfection of our knowledge or is due to the inherent variability of the phenomena being described.

[S08], PDF page 4 (the three dimensions), verified: yes

> Scenarios do not forecast what will happen in the future; rather they indicate what might happen

[S08], PDF page 8, section 5.1 Scenario Uncertainty, verified: yes

> to the extent that we do not even know that we do not know.

[S08], PDF page 9 (total ignorance), verified: yes

> Deciding on which line to join in a supermarket would be a Level 2 problem.

[S09], PDF page 7 (ch. 1, levels of uncertainty), verified: yes

> Leaving an umbrella in the trunk of your car in case of rain is an approach to addressing Level 3 uncertainty.

[S09], PDF page 7, verified: yes

> situations in which we only know that we do not know (4b)

[S09], PDF page 7, verified: yes

> analysts do not know, or the parties to a decision cannot agree on, (1) the appropriate conceptual models that describe the relationships among the key driving forces that will shape the long-term future

[S10], PDF pages 12 and 25 (Summary, and repeated in the body), verified: yes

> Deep uncertainty occurs when the parties to a decision do not know—or agree on—the best model for relating actions to consequences or the likelihood of future events.

[S12], PDF page 2, verified: yes

> But predictions are often wrong, and relying on them can be dangerous.

[S12], PDF page 1, verified: yes

> The shaded region in the figure shows the 120 cases in which the plan generally failed to meet its goals

[S12], PDF page 3 (IEUA water plan, 200 cases), verified: yes

> Keynes and Knight made a distinction between risk which could be quantified with probability calculations and real uncertainty that is unquantifiable.

[S13], review text, verified: yes

> A black swan is an outlier, an event that lies beyond the realm of normal expectations.

[S14], essay para. 3, verified: yes

> Epistemic uncertainty generally, but not always, concerns past or present phenomena that we currently don't know but could, at least in theory, know or establish.

[S56], section 1 Introduction (the source italicizes "don't know"), verified: yes

> Indirect uncertainty in terms of the quality of the underlying knowledge that forms a basis for any claims about the fact, number or hypothesis.

[S56], section 3.3 levels of uncertainty, verified: yes

> A physical concept that applies to various systems in the world, independently of what anyone thinks.

[S15], section 3 "The Main Interpretations", verified: yes

> If only we had better evidence, a single probability function would do. But since our evidence is weak, we must use a set.

[S23], section 3.5 lead-in ("uncertainty escalator"), verified: yes

## Numbers and stories for the screen

- **Ellsberg's two urns** [S05, verified fragment; S23]. Urn I holds 100 balls, red and black in an unknown ratio (anything from 0 to 100 red). Urn II holds exactly 50 red and 50 black. The payoff is $100 if you draw your color and $0 if not. Most people prefer to bet on Urn II whichever color they pick. That is incoherent under any single probability for Urn I. (The counts are legible in the S05 OCR even where exact sentences are not. Confirm against the RAND P-2173 scan before putting them on screen.)
- **Ellsberg's three-color urn** [S23; S05]. There are 90 balls: 30 red and 60 black or yellow in an unknown mix. Bet I pays $100 on red; Bet II pays $100 on black. Most people choose I. Bet III pays on red or yellow; Bet IV pays on black or yellow. Most people choose IV. Choosing I means P(red) > P(black), and choosing IV means P(black or yellow) > P(red or yellow). Together these say r > b and b > r. "No numbers can jointly satisfy these two constraints." SEP uses blue for Ellsberg's black. The imprecise model is P(red) = 1/3 and P(black), P(yellow) each in [0, 2/3].
- **Keynes's beauty contest, *Chaplin v. Hicks* (1911)** [S03]. About 6,000 photographs were sent in. Readers' votes chose 50 finalists, and Seymour Hicks was to pick 12 winners. The plaintiff, a finalist, missed her appointment. The appeals judge valued her lost chance at "about one in four" (12 in 50), and the jury awarded £100. Keynes uses the case to ask whether such a chance is measurable at all. It is a vivid court case of pricing a counterfactual chance.
- **Keynes's umbrella** [S03]. The barometer is high but the clouds are black. Keynes says neither "more likely than not" nor "less likely" may be rational; the decision is "arbitrary". Marchau's umbrella in the car trunk is the Level 3 (robust) answer to the same weather [S09]. These make a natural pair of shots.
- **Keynes's 1937 list** [S04]. Not uncertain: roulette, a Victory bond draw, life expectancy, and, "only moderately", the weather. Uncertain: a European war, copper prices and interest rates 20 years out, a new invention's obsolescence, and wealth-holders' place "in 1970". This works as a sorting game on screen.
- **Rumsfeld, 2002-02-12** [S06], with origins in 1968 defense procurement and "unk-unks" [S07]. Wikipedia also cites a 1955 two-by-two grid, the Johari window of Luft and Ingham, and Žižek's fourth cell, the "unknown known" [S07].
- **RDM and the Inland Empire water plan** [S12]. The 2005 plan aimed to raise groundwater use 75% and recycled water use 600%. RAND ran it through 200 plausible futures, and it failed (cost at least 20% above best estimate) in 120. Failure needed three conditions together: precipitation down at least 10%, aquifer recharge down at least 3%, and larger climate effects on imports. This shows "find the futures where the plan breaks" in one chart.
- **The level ladder** [S08, S09]: complete certainty; Level 1 (mail delivery and garbage collection); Level 2 (which supermarket line to join); Level 3 (umbrella in the trunk); Level 4a and 4b (deep uncertainty, black swans); total ignorance.
- **The same wind speed, two categories** [S01]. A tower designer can fit a probability model to wind records, treating the variability as aleatory. Or the designer can derive wind speed from meteorological sub-models, which exposes epistemic model error. The physics does not change; the model does.

## Candidate visuals

- **Two dials**: a die, which more study will not predict, next to a sealed envelope holding a number, which opening would reveal. Label them "aleatory" and "epistemic", then show the label hanging from the modeler's hand, not the object [S01].
- **Knight's two boxes**: many near-identical houses insured against fire (a group of cases, so risk) next to one new venture with no group (uncertainty) [S02].
- **Ellsberg urns** drawn side by side: one transparent with 50 and 50, one opaque. The viewer picks, then sees the r > b and b > r contradiction appear as two arrows that cannot both hold [S23].
- **A probability as a point versus an interval**: P(yellow) as a dot, then stretched into a bar from 0 to 2/3 [S23].
- **Keynes's weight**: a balance scale whose tilt is the probability, while the pile of evidence on both pans grows. The tilt can stay the same while the pile gets taller [S03].
- **A 2x2 grid** of known and unknown by us and by others, filled in with Rumsfeld's words, then a date stamp moving back to 1968 [S06, S07].
- **The uncertainty ladder** as a horizontal bar from determinism to total ignorance, with a tick for each level and its everyday example [S08, S09].
- **Walker's cube**: three axes, location, level, and nature, with one uncertainty plotted as a point [S08].
- **The RDM scatter**: 200 dots, 120 shaded, and a scenario-discovery box outlining the three joint conditions [S12].
- **Direct and indirect**: a number with an error bar, and beside it a GRADE-style star rating of the evidence [S56].

## Gaps and cautions

- **Knight markdown is scrambled.** `sources/knight-1921-risk-uncertainty-profit.md` came from kaos-pdf with word order jumbled, and only book pp. 197-232 have a text layer at all (many PDF pages, including the famous Ch. I pp. 19-20 "radically distinct" passage, have no text). The two Knight quotes above were checked against the raw PDF text layer via pypdfium2, not the markdown. The often-quoted "We shall accordingly restrict the term 'uncertainty' to cases of the non-quantitive type" is **not verified** in our corpus. Recommend regenerating the markdown from the pypdfium2 text layer and finding a clean Ch. I source (econlib or OLL, both surfaced in discovery) before quoting Ch. I.
- **Ellsberg markdown is badly OCR'd** (doubled letters). The urn counts are legible but exact sentences are not. Use S23 for quotes, or re-fetch a text-layer copy (dklevine refs47605.pdf or core.ac.uk surfaced in discovery). Ellsberg's own phrase for ambiguity ("the ambiguity of this information") is garbled in S05.
- **Hacking's duality is not in our corpus.** No fetched source states Hacking's claim, from *The Emergence of Probability* (1975), that probability was "Janus-faced" from its start around 1660 (statistical and epistemological at once). SEP S15 gives the three-concept split (epistemological, degree of belief, physical), which carries the same point without the attribution. Do not attribute the "Janus-faced" wording to Hacking on screen until a source is fetched. The book is not open; a review or the Cambridge front matter may serve.
- **"Ontic" is not used by our sources**; they say aleatory, variability [S08], or physical [S15]. If the script says "ontic", mark it as our own gloss.
- **Linguistic uncertainty** has no dedicated source. A standard one is Regan, Colyvan and Burgman 2002, "A taxonomy and treatment of uncertainty for ecology and conservation biology" (epistemic versus linguistic, covering vagueness, ambiguity, underspecificity and context dependence). Worth fetching if Video 1 names this category.
- **Kay and King** are covered only through a review [S13]. Quotes of the book in S13 are the reviewer's transcriptions (pp. xiv-xv, p. 133) and should be attributed "as quoted in".
- **Taleb** is represented by a 2004 essay [S14] and by Marchau's summary of the 2007 definition [S09], not the book.
- **Rumsfeld**: the Avalon transcript [S06] is a faithful copy of the DoD transcript but not the defense.gov original (Wikipedia cites an archive.org copy of it). The 1968 Bunker and Drake quotes are secondary through Wikipedia [S07]. Say "by 1968, defense engineers were already saying" rather than naming a coiner.
- **Knight versus Keynes**: the reviewer groups them together [S13]. Their concepts differ. Knight's line is about whether a group of similar cases exists; Keynes's is about whether evidence supports any number or ranking. Do not merge them on screen.
- **"Deep uncertainty" definitions differ in wording** across RAND sources [S10, S12] and Marchau [S09]. Quote one verbatim and do not paraphrase it as a single canonical definition.
- **The aleatory and epistemic split is contested** in machine learning (the discovery pass surfaced arXiv 2412.20892, "Rethinking Aleatoric and Epistemic Uncertainty"). Not fetched; S01's "it's a modeling choice" line is the safe framing.

## Addendum (research lead, after the first pass): clean Knight and Ellsberg texts

Two replacement copies were fetched after this note was drafted: [S76], the Econlib
edition of Knight's Part I, Chapter I, and [S77], a cleaner Ellsberg copy. The quotes
below all pass `tools.py verify`.

> But Uncertainty must be taken in a sense radically distinct from the familiar notion of Risk, from which it has never been properly separated.

[S76], Part I, Chapter I. Verified: yes.

> *measurable* uncertainty, or "risk" proper, as we shall use the term, is so far different from an *unmeasurable* one that it is not in effect an uncertainty at all.

[S76], Part I, Chapter I. Verified: yes. The checked substring is "unmeasurable one that it is not in effect an uncertainty at all". The asterisks are Econlib's italics.

> We shall accordingly restrict the term "uncertainty" to cases of the non-quantitive type.

[S76], Part I, Chapter I. Verified: yes. "non-quantitive" is Knight's spelling.

> Imagine an urn known to contain 30 red balls and 60 black and yellow balls, the latter in unknown proportion.

[S77], PDF page 12 (QJE p. 653). Verified: yes. Ellsberg's own colors are red, black and yellow; SEP [S23] calls the unknown balls blue. Use Ellsberg's colors on screen.

The payoff table (bets I to IV, $100 prizes) is mangled by OCR in [S77]. The note's table follows [S23]. Moscati 2024 [S78] is an open-access account of the paper's text and context, useful for the story of Ellsberg at RAND.
