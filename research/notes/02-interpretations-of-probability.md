# 2. Interpretations of probability

Scope: what a probability number is *about*. The same rules of calculation (Kolmogorov's axioms) have at least five readings: classical, logical or evidential, subjective (Bayesian), frequency, and propensity. This note also covers the arguments that tie degrees of belief to those rules (Dutch book, Cox's theorem, Jaynes' robot) and the basic vocabulary of epistemology: knowledge, belief, and credence.

Keys: S15 SEP Interpretations of Probability (Hájek); S16 Laplace 1814; S17 Ramsey 1926; S18 Jaynes 2003; S19 Van Horn 2003; S20 SEP Dutch Book Arguments; S21 SEP Formal Epistemology; S22 SEP Epistemology; S03 Keynes 1921.

## Key claims

- There are three broad concepts under the one word "probably". The first is evidential support ("in light of the data, California will probably have a major earthquake this decade"). The second is a person's degree of confidence. The third is a physical tendency that holds whatever anyone thinks ("a radium atom will probably decay within 10,000 years"). [S15]
- Five readings are traditional: classical, logical, subjective, frequency, and propensity. "Best-system" chance is a newer sixth. [S15]
- Classical (Laplace): probability is the number of favourable cases over the number of equally possible cases. "Equally possible" is either a category mistake or circular, and the principle of indifference patches it. [S15, S16]
- The principle of indifference gives different answers when the same problem is described in different ways (Bertrand's paradox). Its critics say it "extracts information from ignorance". [S15]
- Laplace made probability a measure of our ignorance. His all-knowing "intelligence" would need no probability at all. [S16]
- Laplace's rule of succession gives (N+1)/(N+2). He used it to put the odds that the sun rises tomorrow at 1,826,214 to 1. [S16, S15]
- Logical (Keynes, Carnap): probability is a degree of partial implication, c(h, e), between evidence and hypothesis. Carnap's measure m* lets you learn from experience, but the choice among infinitely many measures looks arbitrary. It also depends on the language you pick. [S15]
- Keynes held that some probabilities cannot be compared at all. His example is deciding on an umbrella when the barometer is high but the clouds are black. [S03]
- Ramsey rejected Keynes's logical relations because he could not perceive them and others could not agree on them. He turned instead to belief measured by betting. [S17, S15]
- Subjective (Ramsey, de Finetti, Savage): probability is a rational agent's degree of belief (credence), measured by the price at which the agent would buy or sell a bet paying 1 unit. Ramsey, and later Savage and Jeffrey, derive both probabilities and utilities from preferences alone. [S15, S17]
- Dutch book theorem: if your betting prices break the probability axioms, a set of bets exists that loses you money however the world turns out. The converse also holds: coherent credences cannot be booked. [S15, S20]
- Frequency (Venn, Reichenbach, von Mises): probability is a relative frequency in a reference class, finite or limiting. This faces the single-case problem and the reference-class problem. Von Mises called the probability of death for a single person meaningless. [S15]
- Propensity (Peirce, Popper): probability is a physical disposition of a chance set-up. Popper wanted single-case probabilities for quantum mechanics. Critics say "propensity" names the property without explaining it. [S15]
- Cox's theorem: any system of plausible reasoning that meets a few qualitative consistency requirements is isomorphic to probability theory. Its first requirement, that a plausibility is one real number, is the main point of dispute with non-Bayesian approaches (see note 03). [S19]
- Jaynes builds the same result through an imaginary reasoning robot. The robot's plausibilities are real numbers, it agrees qualitatively with common sense, and it reasons consistently. [S18]
- The axioms alone do not fix starting probabilities. This is the problem of the priors, and it splits objective from subjective Bayesians. [S21, S15]
- Epistemology's classical account says knowledge is justified true belief. Gettier cases show that is not sufficient. Credence is graded; knowledge and full belief are all-or-nothing. [S22, S15]

## Definitions in plain words

- **Probability calculus (Kolmogorov's axioms).** The rules for manipulating probability numbers. No probability is negative, a certain thing gets 1, and the chances of incompatible outcomes add. The rules say nothing about what the numbers mean. [S15, S20]
- **Interpretation of probability.** An account of what a probability statement is about: the world, the evidence, or a mind. [S15]
- **Classical probability.** Count the equally possible cases and divide the favourable cases by all cases. A fair die shows an even number with probability 3/6. [S15, S16]
- **Principle of indifference.** If you have no reason to favour one alternative over another, give them equal probability. Keynes coined the name. [S15]
- **Logical probability.** The degree to which evidence e supports hypothesis h. It works like partial implication and is written c(h, e). [S15]
- **Evidential probability.** How strongly present evidence tells for or against a hypothesis. This is not the same as physical chance, and not the same as anyone's actual belief (Williamson). [S15]
- **Credence (degree of belief).** How confident a person is, on a scale from 0 to 1. [S15, S21]
- **Betting quotient (fair price).** The price, as a fraction of the stake, at which you would take either side of a bet on an event. [S15, S20]
- **Dutch book.** A set of bets, each acceptable at your own prices, that together guarantee you a loss. [S15]
- **Coherent.** Credences that obey the probability rules and so cannot be Dutch-booked. [S15]
- **Frequency probability.** The proportion of times an outcome occurs in a reference class, either an actual finite class or an imagined infinite one. [S15]
- **Reference class problem.** One person belongs to many classes (male, non-smoker, and so on), each with a different frequency. Which one gives "my" probability? [S15]
- **Propensity.** A physical tendency of a set-up, such as a die thrown from a box, to produce an outcome. [S15]
- **Prior.** The probability you start with before the new evidence. **Posterior.** The probability after updating on it by Bayes' theorem. [S21]
- **Cox's theorem.** A proof that a few consistency requirements on plausible reasoning force the rules of probability. [S19]
- **Knowledge (classical account).** A belief that is true and justified. Gettier showed this can still be true by luck, so it is not enough. [S22]

## One-table summary

| Interpretation | What a probability is about | Example sentence | Who | Main weakness |
|---|---|---|---|---|
| Classical | Ratio of favourable to equally possible cases | "An even number on a fair die: 3 in 6." | de Moivre, Laplace [S15, S16] | "Equally possible" is circular. Indifference gives different answers under redescription (Bertrand). [S15] |
| Logical / evidential | Degree to which evidence supports a hypothesis | "Given the seismic data, a big quake this decade is probable." | Keynes, Jeffreys, Carnap; Williamson [S15, S03] | The choice of confirmation function and language looks arbitrary. Ramsey could not "perceive" the relations. [S15, S17] |
| Subjective (Bayesian) | A rational agent's degree of belief | "I'd pay 30 cents for a ticket paying $1 if it rains." | Ramsey, de Finetti, Savage [S15, S17] | Different people can start from different priors. Betting behaviour is an imperfect gauge of belief. [S15, S21] |
| Frequency | Relative frequency in a (possibly infinite) reference class | "Of 1,000 tosses, 503 came up heads." | Venn, Reichenbach, von Mises [S15] | No probability for a single case. The answer depends on the reference class. Limits are hypothetical. [S15] |
| Propensity | Physical tendency of a chance set-up | "This radium atom has a 1/2 chance of decaying in 1,600 years." | Peirce, Popper [S15] | Hard to test. Risks naming the property without explaining it. Humphreys' paradox. [S15] |

## Quotable passages

> An epistemological concept, which is meant to measure objective evidential support relations.

[S15], section 3 "The Main Interpretations", concept 1. Verified: yes.

> The concept of an agent’s degree of confidence, a graded belief.

[S15], section 3, concept 2. Verified: yes.

> A physical concept that applies to various systems in the world, independently of what anyone thinks.

[S15], section 3, concept 3. Verified: yes.

> The theory of chance consists in reducing all the events of the same kind to a certain number of cases equally possible

[S16], Chapter II "Concerning Probability" (1902 Truscott and Emory translation, about p. 6 to 7). Verified: yes.

> for it, nothing would be uncertain and the future, as the past, would be present to its eyes.

[S16], Chapter II "Concerning Probability" (the all-knowing "intelligence", often called Laplace's demon). Verified: yes.

> Probability is relative, in part to this ignorance, in part to our knowledge.

[S16], Chapter II "Concerning Probability". Verified: yes.

> Placing the most ancient epoch of history at five thousand years ago, or at 1826213 days, and the sun having risen constantly in the interval at each revolution of twenty-four hours, it is a bet of 1826214 to one that it will rise again to-morrow.

[S16], Chapter III "The General Principles of the Calculus of Probabilities" (about p. 19 of the translation). Verified: yes.

> the theory of probabilities is at bottom only common sense reduced to calculus

[S16], Chapter XVIII (closing paragraph of the essay). Verified: yes.

> Critics accuse the principle of indifference of extracting information from ignorance.

[S15], section 3.1 "Classical Probability". Verified: yes.

> The event ‘the side-length lies in [0, 1/2]’, receives a different probability when merely redescribed.

[S15], section 3.1 (Bertrand-style cube factory). Verified: yes.

> Is our expectation of rain, when we start out for a walk, always more likely than not, or less likely than not, or as likely as not? I am prepared to argue that on some occasions none of these alternatives hold, and that it will be an arbitrary matter to decide for or against the umbrella.

[S03], Part I, ch. III, section 8 (printed p. 32), PDF page 44. Verified: yes.

> I do not perceive them, and if I am to be persuaded that they exist it must be by argument; moreover I shrewdly suspect that others do not perceive them either, because they are able to come to so very little agreement as to which of them relates any two given propositions.

[S17] (Ramsey on Keynes's probability relations), PDF page 10. Verified: yes.

> The old-established way of measuring a person's belief is to propose a bet, and see what are the lowest odds which he will accept.

[S17], PDF page 15. Verified: yes.

> it is based fundamentally on betting, but this will not seem unreasonable when it is seen that all our lives we are in a sense betting.

[S17], PDF page 23. Verified: yes.

> Whenever we go to the station we are betting that a train will really run, and if we had not a sufficient degree of belief in this we should decline the bet and stay at home.

[S17], PDF page 23. Verified: yes.

> such a consistency between the odds acceptable on different propositions as shall prevent a book being made against you.

[S17], PDF page 23. Verified: yes.

> A *Dutch book* is a series of bets bought and sold at prices that collectively guarantee loss, however the world turns out.

[S15], section 3.3.2 "The betting analysis and the Dutch Book argument". Verified: yes.

> Given a set of betting quotients that fails to satisfy the probability axioms, there is a set of bets with those quotients that guarantees a net loss to one side.

[S20], section 1.1 "The Probability Axioms and the Dutch Book Theorem". Verified: yes.

> probability is nothing but that proportion

[S15], section 3.4 "Frequency Interpretations" (quoting Venn 1876, p. 84). Verified: yes.

> I belong to the class of males, the class of non-smokers, the class of philosophy professors who have two vowels in their surname

[S15], section 3.4 (the reference class problem, Hájek on his own chance of living to 80). Verified: yes.

> We can say nothing about the probability of death of an individual even if we know his condition of life and health in detail.

[S15], section 3.4 (quoting von Mises 1957). Verified: yes.

> Popper (1957) is motivated by the desire to make sense of single-case probability attributions that one finds in quantum mechanics

[S15], section 3.5 "Propensity Interpretations". Verified: yes.

> Suppose some dark night a policeman walks down a street, apparently deserted; but suddenly he hears a burglar alarm, looks across the street, and sees a jewelry store with a broken window.

[S18], ch. 1 "Plausible Reasoning", PDF page 20. Verified: yes.

> but it did make it extremely plausible.

[S18], ch. 1, PDF page 20 (the policeman's inference is not deduction). Verified: yes.

> shall invent an imaginary being. Its brain is to be designed by us, so that it reasons according to certain definite rules.

[S18], ch. 1 "Introducing the Robot", PDF page 24. Verified: yes.

> then that will be an accomplishment of the theory, not a premise.

[S18], ch. 1 "Introducing the Robot", PDF page 25. Verified: yes.

> Degrees of Plausibility are represented by real numbers

[S18], ch. 1 "The Basic Desiderata", desideratum (I), PDF page 32. Verified: yes.

> The robot always takes into account all of the evidence it has

[S18], ch. 1, desideratum (IIIb), PDF page 33. Verified: yes.

> In other words, the robot is completely non-ideological.

[S18], ch. 1, desideratum (IIIb), PDF page 33. Verified: yes.

> “Probability theory is nothing but common sense reduced to calculation.”

[S18], ch. 2 epigraph (Laplace), PDF page 40. Verified: yes.

> showed that only those systems isomorphic to probability theory satisfy the requirements.

[S19], section 1 "Introduction" (on Cox 1946), PDF page 1. Verified: yes.

> By representing plausibilities with a single real number we implicitly assume that the plausibilities of any two propositions are comparable.

[S19], discussion of requirement R1, PDF page 5. Verified: yes.

> This weakness of the probability axioms generates the famous *problem of the priors*, the problem of saying where initial probabilities come from.

[S21], section 1.4 "The Problem of the Priors". Verified: yes.

> the three conditions—truth, belief, and justification—are individually necessary and jointly sufficient for knowledge of facts.

[S22], section 2.3 "Knowing Facts". Verified: yes.

> It turns out, as Edmund Gettier showed, that there are cases of JTB that are not cases of knowledge.

[S22], section 2.3 "Knowing Facts". Verified: yes.

## Numbers and stories for the screen

1. **The sunrise bet.** Laplace's rule of succession says that after N successes in a row, the chance of one more is (N+1)/(N+2). With 5,000 years of history, or 1,826,213 sunrises, he gets odds of 1,826,214 to 1 that the sun rises tomorrow. He then adds at once that anyone who understands the physics would put the odds far higher. [S16, S15] The point for viewers: the same event gets a different number depending on what you know. The rule counts only the tally; the astronomer knows the mechanism.
2. **The cube factory (Bertrand's paradox).** A factory makes cubes with side length between 0 and 1 foot. "Indifference" over side length gives P(side ≤ 1/2) = 1/2. The same event is "face area ≤ 1/4", and indifference over area gives 1/4. It is also "volume ≤ 1/8", and indifference over volume gives 1/8. One event, three "ignorance" probabilities. [S15] This makes a clean three-panel animation.
3. **A worked Dutch book (illustrative arithmetic on the SEP recipe).** You say rain tomorrow has probability 0.6 and no rain also has probability 0.6. Your credences sum to 1.2, which breaks additivity. At your own prices a bookie sells you a $1 ticket on "rain" for $0.60 and a $1 ticket on "no rain" for $0.60. You pay $1.20 and exactly one ticket pays $1, so you lose $0.20 whatever the weather does. If your numbers sum to 0.8, the bookie *buys* both tickets from you for $0.80 total and pays out $1. You lose $0.20 again. [S15, S20] (The prices are our example; the construction is the SEP's additivity case.)
4. **Carnap learning from one observation.** There are three individuals a, b, c and one property F. Carnap's m* gives the hypothesis "c is F" a prior of 1/2. After seeing that a is F, it rises to 2/3. [S15] This is a small visual of "evidence moves the number".
5. **Bayes with a registrar's numbers.** 35% of students take philosophy, 20% of all students have high grades, and 25% of philosophy students have high grades. So P(philosophy | high grades) = 0.35 × 0.25 / 0.20 = 7/16, about 0.44. That is up from the prior of 0.35. [S21] (See caution below about a typo in the source.)
6. **The policeman and the masked man.** A masked man crawls out of a broken jewelry-store window with a bag of jewels. The policeman concludes "dishonest" without deduction, since the man might be the owner coming home from a masquerade. The evidence makes guilt "extremely plausible", not certain. Jaynes uses this to motivate probability as an extension of logic. [S18]
7. **Ramsey's train.** "Whenever we go to the station we are betting that a train will really run." Every action is a bet, and credence is what the bet reveals. [S17]
8. **Keynes's umbrella.** High barometer, black clouds. Keynes argues there may be no fact about whether rain is more or less likely than not, so the umbrella decision is "arbitrary". This is the opening for imprecise probability (note 03). [S03]
9. **The reference class of one man.** Hájek's chance of living to 80 differs for males, non-smokers, philosophy professors, and so on. Which frequency is "his"? [S15]

## Candidate visuals

- **Three jars, one word.** The word "probably" sits over three jars labelled *evidence*, *belief*, *world*, each with the SEP's example sentence (earthquake, rain in Canberra, radium atom). [S15]
- **The five-column table** above, revealed one column at a time, with a face or portrait for each school.
- **Cube factory.** One cube grows from side 0 to 1. Three rulers (side, area, volume) light up the same cube as "1/2", "1/4", "1/8". [S15]
- **Dutch book ledger.** Two tickets, two prices, two weather outcomes, and a running cash balance that ends at minus $0.20 in both columns. [S15, S20]
- **Laplace's counter.** A sunrise tally ticking to 1,826,213, then the fraction (N+1)/(N+2) converging toward 1. [S16]
- **Jaynes' robot.** A cartoon robot with a dial per proposition (real numbers), a "common sense" check, and three consistency lights (IIIa, b, c). [S18]
- **Knowledge Venn diagram.** Circles for *true*, *believed*, and *justified*, with the overlap labelled "knowledge?". A barn facade pops up in the overlap to show a Gettier case. [S22]
- **Credence slider.** Full belief is an on/off switch; credence is a 0 to 1 slider beside it. [S15, S21]

## Gaps and cautions

- De Finetti, Savage, Venn, von Mises, Carnap, and Popper are reached **only through the SEP entry [S15]** (secondary, though authoritative). The Venn and von Mises lines are SEP's quotations of them. Cite them as "quoted in [S15]".
- **SEP typo in [S21].** Section 1.2.2 computes the posterior 7/16 and then says "That’s higher than p(H) = 20/100". The prior in its own example is 35/100 (20/100 is p(E)). The conclusion still holds (7/16 ≈ 0.44 > 0.35). Do not reproduce "20/100" on screen.
- **Laplace wording.** [S16] is the 1902 Truscott and Emory translation (Gutenberg). SEP [S15] quotes a different translation ("The theory of chances consists in reducing all events of the same kind..."). Use one version consistently. The Jaynes epigraph [S18] gives a third wording ("common sense reduced to calculation" versus Laplace-translation "reduced to calculus").
- **Dutch book example numbers** are our own arithmetic on the SEP recipe, not quoted. Label them as an illustration.
- **Ramsey PDF** [S17] is a transcription with some scrambled line order around the "laws of consistency" passage (around PDF page 21). Quote only the verified passages above.
- **Van Horn** [S19] converted without apostrophes ("Coxs"). Verified quotes avoid those spans.
- **Jaynes** [S18] is the 1990s preprint on bayes.wustl.edu, not the 2003 Cambridge edition. Page numbers are PDF pages of the preprint.
- Not covered by a downloaded primary source: Savage's *Foundations of Statistics* (1954), de Finetti's *Theory of Probability* (1974), von Mises's *Probability, Statistics and Truth*, and Popper 1957/1959. All reach us via [S15].
- "Best-system" chance (Lewis) is described in [S15] section 3.6 but is probably too far into the weeds for a short video.
