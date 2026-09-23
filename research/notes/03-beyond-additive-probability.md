# 3. Beyond additive probability

Scope: Dempster-Shafer belief functions, imprecise probability and credal sets, possibility theory and fuzzy sets. When each is used, and why. How Ellsberg's urn looks in each.

Keys: S23 SEP "Imprecise Probabilities" (Bradley), S24 Shafer "Dempster-Shafer Theory", S25 Denoeux lecture on belief functions, S26 Zadeh 1965 "Fuzzy Sets", S27 Zadeh 1977 "Fuzzy Sets as a Basis for a Theory of Possibility". Supporting: S05 Ellsberg, S15 SEP "Interpretations of Probability", S21 SEP "Formal Epistemology", S56 van der Bles et al.

## Key claims

- Ordinary probability is *additive*: if two events cannot both happen, the chance of "one or the other" is the sum of their chances. Every framework in this note relaxes that rule, or replaces it [S23, S25].
- A single probability number cannot tell two states of mind apart. You have seen 100 tosses of a fair coin, or you know nothing about a coin's bias. Both give p(heads) = 0.5. Imprecise probability separates them: {0.5} against the whole interval [0, 1] [S23 §2.3].
- The principle of indifference (spread belief evenly when you know nothing) gives inconsistent answers when you describe the same question two ways. The "life around Sirius" example gives 1/2 with two options and 1/3 with three options. Denoeux gives this as the reason Dempster-Shafer theory exists [S25, slides 9-12].
- Dempster-Shafer (DS) theory builds degrees of belief about one question from probabilities about a *related* question, such as how reliable a witness is. It combines independent pieces of evidence with Dempster's rule [S24].
- In DS theory a zero degree of belief means "no evidence for this", not "certainly false". That is the key difference from a zero probability [S24].
- Every DS judgment gives two numbers, belief (Bel) and plausibility (Pl), with Bel ≤ Pl. The gap is widest under total ignorance (0 and 1). It closes to one number when the evidence is fully probabilistic. So ordinary probability is a special case of DS [S25, slide 23].
- Dempster's rule assumes the evidence items are independent. Two witnesses who could both mistake a dog for a burglar share a cause of error. You must model that shared cause before you combine them [S24].
- Imprecise probability (IP) represents belief by a *set* of probability functions. Levi calls it a credal set; Bradley calls it a "credal committee". The lower and upper envelopes of the set give an interval for each event [S23 §1.1].
- IP can make the usual Ellsberg choices rational: P(red) = 1/3, P(blue) and P(yellow) each [0, 2/3]. No single probability function can [S23 §2.1].
- IP has costs. Starting from total ignorance, [0, 1], no evidence ever narrows the interval ("belief inertia"). Walley accepts this and advises priors that are close to vacuous but not fully vacuous [S23 §3.2]. Learning can also *widen* intervals ("dilation") [S23 §3.1].
- IP is used in statistics (Walley 1991), engineering, economics, computer science, physics and philosophy, including Kyburg 1983 [S23 §1]. Our sources only name Kyburg in a list. See Gaps.
- A fuzzy set gives each object a grade of membership between 0 and 1. It is for *vague categories* ("tall men", "numbers much greater than 1"), not for random events [S26].
- Possibility theory reads a fuzzy set as a limit on what a variable's value could be. "John is young" makes age 28 possible to degree about 0.7 [S27 §2].
- Possibility and probability measure different things. In Zadeh's egg example, eating 3 eggs is fully possible (1) but has probability 0.1. The one link: what is impossible must be improbable [S27, PDF p. 12].
- Zadeh's thesis: the vagueness of natural language is mostly possibilistic, not probabilistic [S27, abstract and p. 5]. This bears on the communication problem (note 6): "likely" is a vague category as much as a number.
- A possibility distribution is a special DS belief function whose focal sets are nested ("consonant"). Plausibility of a set is then the largest possibility of any element [S25, slide 28]. So the three frameworks are related, not rivals.
- Formal epistemology's main results about updating also hold in other formalisms such as DS theory and ranking theory [S21].

## Definitions in plain words

- **Additivity.** If A and B cannot both be true, P(A or B) = P(A) + P(B).
- **Frame of discernment.** The list of possible answers to a question. Denoeux stresses that how finely you cut this list is a choice [S25, slide 14].
- **Mass function (m).** A share-out of one unit of evidence over *sets* of answers, not single answers. Mass on a set means "the evidence points here but says no more". Mass on the whole frame means "I don't know" [S25, slides 14-19].
- **Belief, Bel(A).** Total mass on sets inside A: how strongly the evidence *supports* A.
- **Plausibility, Pl(A).** Total mass on sets that overlap A. It equals 1 minus the belief in "not A": how far the evidence *fails to rule A out* [S25, slide 21].
- **Belief-plausibility interval.** [Bel(A), Pl(A)]. The width shows how much the evidence leaves open.
- **Dempster's rule.** Multiply masses from two independent sources and give each product to the intersection of the two sets. Throw away products whose intersection is empty (the conflict, κ). Divide the rest by 1 − κ [S25, slide 42].
- **Credal set (representor, credal committee).** A set of probability functions, all consistent with what you know. Each member is one "committee member's" opinion [S23 §1.1].
- **Lower and upper probability (envelopes).** The smallest and largest probability any committee member gives an event. Upper(A) = 1 − Lower(not A) [S23 §1.1].
- **Lower and upper previsions.** Walley's general form: lower and upper expected values of a gamble. A probability is the prevision of a yes/no gamble [S23 §1.2].
- **Risk and ambiguity.** A bet is risky when the probabilities of its outcomes are known. It is ambiguous when they are unknown or only partly known [S23 §2.1].
- **Fuzzy set.** A class with "a continuum of grades of membership". A membership function gives each object a number from 0 (clearly out) to 1 (clearly in) [S26].
- **Possibility distribution.** A fuzzy set used as an "elastic constraint" on a variable's value. π(u) is how easily the value u fits what you were told [S27 §2].

## Comparison table

| Framework | What it represents | Number(s) it gives | Use it when | Do not use it when |
|---|---|---|---|---|
| Additive (Bayesian) probability | One degree of belief or one frequency per event | One number p(A) in [0, 1] | Evidence or frequencies support a single sharp number; you must bet or decide and want a coherent, well-tested rule | The number would be false precision ("0.75? Why not 0.75001?") [S23 §1], or you must tell "no evidence" apart from "evenly balanced evidence" [S23 §2.3] |
| Dempster-Shafer belief functions | Evidence about related questions (sensor or witness reliability), and how it bears on the question you care about | Two numbers, Bel(A) ≤ Pl(A) | Combining several independent, partly reliable sources: sensor fusion, expert systems, classifiers [S24, S25] | Sources share hidden causes of error (the dog and the burglar), so they are not independent [S24]; sources conflict heavily (see Gaps) |
| Imprecise probability (credal sets, lower and upper previsions) | A set of probability functions that fit the evidence | An interval [lower P(A), upper P(A)], or a set of expectations | Evidence is thin, conflicting, or comes from a disagreeing group; ambiguity (Ellsberg); robustness checks in statistics [S23 §2] | You start from total ignorance and hope data will narrow it: vacuous priors never learn [S23 §3.2]; you need one decision rule with no further choices [S23 §3.3] |
| Possibility theory and fuzzy sets | Vagueness of categories, and how easily a value fits a vague description | Membership or possibility degree π(u) in [0, 1]; for a set, the maximum π over its members | Words and categories with fuzzy edges: "young", "small integer", "about 30"; meaning in natural language; control and pattern classification [S26, S27] | You have real frequencies or chances: a high possibility says nothing about probability [S27, p. 12] |
| None (no formal measure) | Radical or deep uncertainty: you cannot list the outcomes | Scenarios, stress tests (see notes 1 and 5) | The frame itself is unknown | Any of the above would hide that you cannot list the outcomes |

## Worked examples

### A. Dempster-Shafer: Betty the witness, then two sensors

**Betty** [S24]. You are 90% sure Betty is reliable. She says a limb fell on your car.
- Mass: m({limb fell}) = 0.9. The other 0.1 goes to the whole frame {fell, didn't fall}, because an unreliable Betty tells you nothing.
- Bel(limb fell) = 0.9; Pl(limb fell) = 1.0.
- Bel(no limb) = 0; Pl(no limb) = 0.1.
- A Bayesian would need some number for "no limb". Here the zero means only that Betty gave no reason to believe it.

**Sally agrees** (also 90% reliable, independent). The chance that at least one is reliable is 1 − 0.1 × 0.1 = 0.99. So Bel(limb fell) = 0.99 [S24].

**Sally contradicts Betty.** They cannot both be reliable. Prior weights: only Betty reliable 0.09, only Sally 0.09, neither 0.01. Remove the impossible "both" case (0.81) and divide by 0.19. Bel(limb fell) = 9/19 ≈ 0.47. Bel(no limb) = 9/19 ≈ 0.47. The remaining 1/19 ≈ 0.05 stays on "don't know" [S24; the fractions are garbled in the PDF text layer, recomputed here from the stated 0.09, 0.09, 0.01].

**Two sensors on a road scene** [S25, slides 17-24, 37-39]. Frame: {Grass, Road, Tree, Obstacle, Sky}.
- Lidar, 90% reliable, says "Tree or Obstacle": m1({T, O}) = 0.9, m1(all) = 0.1. Then Bel({T}) = 0 and Pl({T}) = 1.
- Camera, 80% reliable, says "Grass or Tree": m2({G, T}) = 0.8, m2(all) = 0.2.
- Dempster's rule, with no conflict here: m({T}) = 0.72, m({T, O}) = 0.18, m({G, T}) = 0.08, m(all) = 0.02.
- Now Bel({Tree}) = 0.72 and Pl({Tree}) = 1.0. Two vague reports combine into fairly strong support for "tree".

### B. Credal set: Ellsberg's urn

Urn: 90 balls. 30 are red; the other 60 are blue or yellow in unknown proportion [S23 §2.1; Ellsberg's own paper says black, not blue, S05].

Credal set: every p with p(R) = 1/3 and p(B) + p(Y) = 2/3, with p(B) anywhere from 0 to 2/3 [S23].

| Bet wins if ball is | Lower P | Upper P | Kind |
|---|---|---|---|
| I: red | 1/3 | 1/3 | risky (known) |
| II: blue | 0 | 2/3 | ambiguous |
| III: not blue (red or yellow) | 1/3 | 1 | ambiguous |
| IV: not red (blue or yellow) | 2/3 | 2/3 | risky (known) |

Many people prefer I to II and IV to III. With one probability that needs r > b and also r + y < y + b. "No numbers can jointly satisfy these two constraints" [S23]. An agent who dislikes ambiguity and ranks bets by their lower probability picks I (1/3 > 0) and IV (2/3 > 1/3), which is the observed pattern. (The lower and upper columns for III and IV are derived here from S23's constraint p(B) = 2/3 − p(Y).)

The same urn in DS form: m({R}) = 1/3, m({B, Y}) = 2/3. Then Bel(blue) = 0, Pl(blue) = 2/3, and Bel(not red) = Pl(not red) = 2/3. The intervals match the credal set (derived here from the S25 definitions). No exact possibility distribution fits this urn: the focal sets {R} and {B, Y} are not nested, and possibility theory needs nested ones [S25, slide 28].

### C. Possibility: "about 30 years old" and Hans's eggs

Zadeh's own examples [S27]:
- "John is young" makes π(age = 28) ≈ 0.7. That is how well 28 fits "young", recast as how possible age 28 is, given only that statement.
- "X is a small integer": π = 1/1 + 1/2 + 0.8/3 + 0.6/4 + 0.4/5 + 0.2/6. That is, 1 and 2 fully possible, 3 possible to degree 0.8, and so on [S27 p. 10].

An "about 30 years old" distribution for the video (illustrative, built with S27's definition): π(30) = 1; π falls in straight lines to 0 at 20 and at 40. So π(25) = π(35) = 0.5 and π(28) = π(32) = 0.8.
- Possibility that the person is 28 to 32 = the largest π in that range = 1.
- Possibility that the person is over 38 = π(38) = 0.2.
- Unlike probabilities, the π values do not add to 1. Many ages can each be fully possible.

**Hans's eggs** [S27, PDF p. 12, Table 1]:

| Eggs u | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Possibility π(u), how easily Hans *can* eat u | 1 | 1 | 1 | 1 | 0.8 | 0.6 | 0.4 | 0.2 |
| Probability p(u), how often he *does* | 0.1 | 0.8 | 0.1 | 0 | 0 | 0 | 0 | 0 |

## Quotable passages

> The Dempster-Shafer theory, also known as the theory of belief functions, is a generalization of the Bayesian theory of subjective probability.

[S24], location = PDF page 1, verified: yes

> So her testimony alone justifies a 0.9 degree of belief that a limb fell on my car, but only a zero degree of belief (not a 0.1 degree of belief) that no limb fell on my car.

[S24], location = PDF page 1, verified: yes

> This zero does not mean that I am sure that no limb fell on my car, as a zero probability would; it merely means that Betty's testimony gives me no reason to believe that no limb fell on my car.

[S24], location = PDF page 1, verified: yes

> They might both have mistaken the noise of a dog for that of a burglar, and because of this common uncertainty, I cannot combine degrees of belief based on their evidence directly by Dempster's rule.

[S24], location = PDF page 2, verified: yes

> The only sensible solution is provided by Laplace's principle of indifference (PI): "In the absence of any relevant evidence, agents should distribute their credence (or 'degrees of belief') equally among all the possible outcomes under consideration".

[S25], location = PDF page 9 (slide 9), verified: yes

> As shown by the following example, this principle leads to paradoxes.

[S25], location = PDF page 9 (slide 9, followed by the Sirius example on slides 10-11), verified: yes

> The Dempster-Shafer theory was introduced to solve such paradoxes.

[S25], location = PDF page 12 (slide 12), verified: yes

> The probabilistic formalism is recovered as a special case (known frequencies or proportions in a population).

[S25], location = PDF page 12 (slide 12), verified: yes

> This rule can be used to combine mass functions induced by independent pieces of evidence

[S25], location = PDF page 42 (slide 42, "Dempster's rule"), verified: yes

> What should your rational degree of belief be that global mean surface temperature will have risen by more than four degrees by 2080? Perhaps it should be 0.75? Why not 0.75001? Why not 0.7497?

[S23], location = §1 Introduction, verified: yes

> Your representor is a credal committee: each probability function in it represents the opinions of one member of a committee that, collectively, represents your beliefs.

[S23], location = §1.1 A summary of terminology, verified: yes

> A prospect is risky if its outcome is uncertain but its outcomes occur with known probability. A prospect is ambiguous if the outcomes occur with unknown or only partially known probabilities.

[S23], location = §2.1 Ellsberg decisions, verified: yes

> No numbers can jointly satisfy these two constraints.

[S23], location = §2.1 Ellsberg decisions, verified: yes

> The first case is represented by \(P(H)=\{0.5\}\), while the second is captured by \(P(H)=[0,1]\).

[S23], location = §2.3 Weight of evidence, balance of evidence (fair coin against coin of unknown bias), verified: yes

> When there is little or no information on which to base our conclusions, we cannot expect reasoning (no matter how clever or thorough) to reveal a most probable hypothesis or a uniquely reasonable course of action. There are limits to the power of reason.

[S23] quoting Walley 1991: 2, location = §2.4 Suspending judgement, verified: yes

> It seems like the imprecise probabilist cannot learn from vacuous priors.

[S23], location = §3.2 Belief inertia, verified: yes

> Imprecise probabilities aren't a radically new theory. They are merely a slight modification of existing models of belief for situations of ambiguity.

[S23], location = §3.4 Interpreting IP, verified: yes

> A fuzzy set is a class of objects with a continuum of grades of membership.

[S26], location = PDF page 1 (abstract; journal p. 338), verified: yes

> Essentially, such a framework provides a natural way of dealing with problems in which the source of imprecision is the absence of sharply defined criteria of class membership rather than the presence of random variables.

[S26], location = PDF page 2 (journal p. 339), verified: yes

> much of the information on which human decisions are based is possibilistic rather than probabilistic in nature.

[S27], location = PDF page 5 (§1 Introduction), verified: yes

> in which a term such as 0.8/3 signifies that the possibility that X is 3, given that X is a small integer, is 0.8.

[S27], location = PDF page 10 (§2), verified: yes

> Thus, a high degree of possibility does not imply a high degree of probability, nor does a low degree of probability imply a low degree of possibility.

[S27], location = PDF page 12 (after Table 1, Hans's eggs), verified: yes

## Candidate visuals

1. **Two coins, one number.** Left: a coin with a tally of 100 tosses, about half heads. Right: a coin in a sealed box. Both labelled "p = 0.5". Then the right label splits into a bar from 0 to 1 while the left stays a dot [S23 §2.3].
2. **The Sirius paradox.** A question card, "Is there life around Sirius?", split into 2 boxes (1/2 each), then re-split into 3 (1/3 each). The "life" box shrinks from 1/2 to 1/3 with no new evidence [S25].
3. **Betty's testimony as a bar.** A horizontal bar from 0 to 1 for "a limb fell". Solid fill to 0.9 (belief), hatched from 0.9 to 1.0 (uncommitted). A second bar for "no limb" with no solid fill and hatching to 0.1. Then Sally arrives and the solid fill grows to 0.99 [S24].
4. **Dempster's rule as a grid.** The road-scene 2 × 2 table: lidar masses on one side, camera on the other, each cell the product placed on the intersection set. Cells light up and pool into m({Tree}) = 0.72 [S25, slide 39].
5. **Ellsberg's urn and a committee.** The urn with 30 red and 60 grey (unknown) balls. A row of little committee figures, each holding a different blue/yellow split, from 0/60 to 60/60. Their answers for "blue" spread across 0 to 2/3, while every figure agrees red = 1/3 [S23].
6. **Hans's eggs.** Two rows of 8 egg icons. Top row shaded by possibility (four full, then fading). Bottom row shaded by probability (almost everything on 2 eggs). The caption states the one rule that links them: impossible implies improbable [S27].
7. **Fuzzy edge against sharp edge.** A line of ages 15 to 45. A crisp set "under 30" is a hard step. The fuzzy "about 30" is a tent peaking at 30. Point to 28 (0.8) and 38 (0.2) [S26, S27].
8. **Family tree.** Probability is the special case of DS where Bel = Pl. Possibility is the special case where focal sets are nested. Credal sets contain both [S25, S23].

## Gaps and cautions

- **Kyburg.** Our sources only list "Kyburg 1983" among IP work in philosophy [S23 §1]. The SEP historical appendix, which covers Kyburg's interval probabilities, was not fetched. Do not attribute any specific Kyburg claim without a new source.
- **Walley.** We have Walley only through SEP quotations (1991: 2 and 1991: 93) and SEP's summary that the formal theory is about previsions [S23]. There is no primary Walley text.
- **Zadeh's counterexample to Dempster's rule** (two doctors, near-total conflict, and the rule puts all belief on a diagnosis both thought unlikely) is **not in any fetched source**. The Betty/Sally conflict case in S24 shows the renormalisation step but not the paradox. Get a source before using the counterexample.
- **Ellsberg primary text.** The text layer of S05 is badly garbled (doubled letters), so no Ellsberg quote is usable from it. Use S23's statement of the urn. Ellsberg's own colours are red, black, yellow; SEP says blue.
- **OCR quality.** S27 (1977 scanned report) and S25 (slides) have scrambled layout. The Hans's-eggs table and the Dempster's-rule numbers above were checked against the logic of the example, and the DS fractions for Betty and Sally were recomputed from the stated inputs. Quote only the lines listed above.
- **Derived numbers.** The Ellsberg lower/upper columns for bets III and IV, the DS form of the urn, and the "about 30" tent are this note's derivations from the sources' definitions, not quotations. Label them as illustrations on screen.
- **Decision rules.** Ranking bets by lower probability ("maximin") is one of several IP decision rules; SEP says IP decision making is unsettled when the credal committee disagrees [S23 §3.3]. Do not present maximin as *the* IP rule.
- **Possibility is not modal logic.** Zadeh warns that his "possibility" differs from "it is possible that" in modal logic [S27, footnote p. 5]. Keep this distinct from Lewis's possible worlds in note 5.
- **Alternative reading of Ellsberg.** Al-Najjar and Weinstein (2009) explain the choices with a precise model plus suspicion of the person offering the bet [S23 §2.1]. Say "one explanation" when IP is presented as the explanation.
