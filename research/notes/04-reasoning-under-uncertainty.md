# 4. Logic and reasoning under uncertainty

Scope: deduction, induction, and abduction; Hume's problem of induction;
reasoning that takes back its conclusions (nonmonotonic reasoning); Bayesian
updating; calibration and overconfidence; the Tversky and Kahneman heuristics;
the Brier score; the Good Judgment Project results; noise; misreadings of
confidence intervals.

Sources: S28 Hume, S29 SEP Problem of Induction, S30 SEP Abduction, S31 SEP
Non-monotonic Logic, S32 Tversky and Kahneman 1974, S33 Brier 1950 (landing
page only, see Gaps), S34 Mellers et al. 2014, S35 Kahneman et al. 2016 HBR
(partial), S36 Hoekstra et al. 2014, S59 Gigerenzer and Hoffrage 1995, S21 SEP
Formal Epistemology, S57 Spiegelhalter 2017.

## Key claims

- Deduction is the only kind of inference where true premises guarantee a true conclusion. Induction and abduction are "ampliative": the conclusion says more than the premises, so it can be wrong even when every premise is true. [S30]
- Induction and abduction differ in what they appeal to. Induction appeals only to observed frequencies. Abduction appeals to which hypothesis best explains the evidence. [S30]
- Abduction picks the best explanation from the candidates we thought of. If the true explanation is not on our list, abduction can pick "the best of a bad lot." This is a way that unknown unknowns enter reasoning. [S30]
- Hume: a claim about a matter of fact can be denied without contradiction. "The sun will not rise tomorrow" is not self-contradictory, so no deductive proof can rule it out. [S28]
- Hume: every argument from experience assumes that the future will resemble the past. Trying to prove that assumption from experience is circular. [S28, S29]
- Hume's own answer is that we rely on custom, or habit, not on reason, to expect the future to resemble the past. [S28, S29]
- Everyday reasoning takes back conclusions when new facts arrive. Tweety is a bird, so we infer Tweety flies; we learn Tweety is a penguin, so we retract it. Logic in which adding premises can remove conclusions is called nonmonotonic. Deductive logic cannot do this. [S31]
- Bayes' theorem says how to update a probability when evidence arrives: multiply the prior by how much more likely the evidence is if the hypothesis is true. [S21]
- People do much better at Bayesian problems when the numbers are given as counts ("8 of every 10 women") rather than as single-event probabilities ("80%"). Across Gigerenzer and Hoffrage's first study, correct Bayesian reasoning rose from 16% of answers with probabilities to 46% (standard menu) and 50% (short menu) with frequencies. [S59, raw PDF pages 10 and 12]
- In the classic mammography problem, 95 of 100 physicians in Eddy's 1982 study put the chance of cancer after a positive test at 70% to 80%. The right answer is 7.8%. [S59, raw PDF page 3]
- People judge probability by shortcuts: how much a case resembles a stereotype (representativeness), how easily examples come to mind (availability), and adjustment from a starting number (anchoring). These shortcuts are useful but cause predictable errors. [S32]
- Anchoring works even with a number known to be random. Subjects who saw a wheel of fortune land on 10 gave a median estimate of 25% for the share of African countries in the United Nations; those who saw 65 gave 45%. Paying for accuracy did not remove the effect. [S32, raw PDF page 6]
- People are overconfident. When asked for 98% ranges, the true value fell outside the range in about 30% of problems, not 2%. Proper scoring rules did not fix it. [S32, raw PDF page 7]
- A calibrated forecaster's 70% events happen about 70% of the time. Calibration can be measured and it can be trained. [S34, S57]
- The Brier score is the average squared gap between the forecast probabilities and what happened (1 for happened, 0 for did not). Lower is better. In the two-outcome form used by the Good Judgment Project, 0 is perfect and 2 is the worst. It is a "proper" score: the forecaster's best strategy is to report what they actually believe. [S34]
- In the IARPA geopolitical forecasting tournament, the Good Judgment Project found three things that made forecasts more accurate: probability training, working in teams, and putting the top 2% of forecasters together in elite teams ("tracking"). [S34]
- A training module that took about 45 minutes improved accuracy across two forecasting seasons of about 8 to 10 months each. [S34]
- Even good forecasters were overconfident at the extremes. Forecasts of 100% made early in a question's life were right only about 70% of the time; the same forecasts made near the end were right about 90% of the time. The problem was a failure to update. [S34]
- Superforecasters beat other groups mainly on resolution: they told likely events from unlikely ones more sharply, not only more honestly. [S34]
- Noise is unwanted variation between judges who should agree. The same application file sent to two offices of one firm came back with very different quotes. [S35]
- Most researchers misread confidence intervals. Given six false statements about a 95% interval, 120 researchers and 442 students endorsed on average more than three. Researchers did no better than first-year students who had no training in statistical inference. [S36]
- The correct reading of a 95% confidence interval is about the procedure: if we repeated the experiment many times, 95% of the intervals made this way would contain the true value. It does not say there is a 95% chance that this particular interval contains it. [S36]

## Definitions in plain words

- **Deduction.** Reasoning where the conclusion must be true if the premises are true. "All men are mortal; Socrates is a man; so Socrates is mortal." [S30]
- **Induction.** Reasoning from observed cases to unobserved ones, based only on how often things happened. "Every piece of bread so far has fed me; so the next one will." [S29, S30]
- **Abduction** (inference to the best explanation). Reasoning from evidence to the hypothesis that would best explain it. "The streets are wet; the best explanation is rain." [S30, S31]
- **Ampliative.** A conclusion that goes beyond what the premises contain. Induction and abduction are ampliative, so they can fail. [S30]
- **Problem of induction.** Hume's point that no argument, deductive or from experience, can show that the future will resemble the past without assuming it. [S28, S29]
- **Nonmonotonic (defeasible) reasoning.** Reasoning where learning more can remove a conclusion. The name comes from breaking "monotony," the rule of deductive logic that adding premises never removes conclusions. [S31]
- **Prior, likelihood, posterior.** The prior is how probable a hypothesis was before the evidence. The likelihood is how probable the evidence is if the hypothesis is true. The posterior is the updated probability after the evidence. Bayes' theorem links them. [S21]
- **Natural frequencies.** Counts out of a fixed group of people, such as "10 out of every 1,000 women," used instead of percentages. [S59, S57]
- **Heuristic.** A mental shortcut for judging probability. Tversky and Kahneman named three: representativeness, availability, and anchoring. [S32]
- **Calibration.** A forecaster is calibrated if, among all the times they said 70%, the event happened about 70% of the time. [S32, S34]
- **Overconfidence.** Stating ranges that are too narrow or probabilities that are too extreme for what one knows. [S32, S34]
- **Resolution.** Skill at giving different probabilities to events that turn out differently; decisiveness that is earned. [S34]
- **Brier score.** Average squared error of probability forecasts against outcomes coded 1 and 0. [S34]
- **Noise.** Scatter in judgments that should be identical. Different from bias, which is error in a consistent direction. [S35]
- **Confidence interval.** A range computed by a procedure that, over many repetitions, captures the true value a stated share of the time (for example 95%). [S36]

## Worked examples

### Bayes with natural frequencies (mammography)

Numbers from S59 (raw PDF page 5). Probability version: 1% of women aged 40
in routine screening have breast cancer. If a woman has it, the chance of a
positive mammogram is 80%. If she does not, the chance is 9.6%. A woman tests
positive. What is the chance she has cancer?

Frequency version (same numbers):

1. Picture 1,000 women.
2. 10 of them have breast cancer. 990 do not.
3. Of the 10 with cancer, 8 test positive.
4. Of the 990 without cancer, 95 test positive (9.6% of 990 is about 95).
5. So 8 + 95 = 103 women test positive.
6. Of those 103, only 8 have cancer. 8 / 103 = 7.8%.

S59 gives the computation as "8/(8 + 95)". Eddy's physicians mostly answered
70% to 80%, about ten times too high [S59, raw PDF page 3]. The error is
ignoring the base rate: most positives come from the large healthy group.

### A Brier score for two forecasters

Using the two-outcome Brier score from S34, which for a yes/no event equals
2 x (forecast minus outcome) squared, where the outcome is 1 or 0.

S34's own example: a forecaster says 90% and the event happens:
(0.9 - 1)^2 + (0.1 - 0)^2 = 0.02. If the event does not happen:
(0.9 - 0)^2 + (0.1 - 1)^2 = 1.62.

Illustration built on that rule (our numbers, not from a source): four days,
rain on three of them (rain, rain, rain, dry).

| Forecaster | Forecasts of rain | Score per day | Average Brier score |
|---|---|---|---|
| Careful (says 70% every day) | 70, 70, 70, 70 | 0.18, 0.18, 0.18, 0.98 | 0.38 |
| Certain (says 100% every day) | 100, 100, 100, 100 | 0, 0, 0, 2.00 | 0.50 |
| Coin flip (says 50% every day) | 50, 50, 50, 50 | 0.50 each | 0.50 |
| Skilled (90, 90, 90, 10) | 90, 90, 90, 10 | 0.02 each | 0.02 |

Lesson for the screen: the "certain" forecaster was right three days out of
four and still scored as badly as a coin flip, because one confident miss
costs 2.00. Lower is better.

### Anchoring numbers

From S32 (raw PDF page 6): a wheel of fortune was spun in front of subjects.
Group A saw 10, group B saw 65. Both were asked whether the share of African
countries in the United Nations was higher or lower, then to estimate it.
Median estimates: 25% (group A) and 45% (group B). A random number moved the
answer by 20 points. Payoffs for accuracy did not remove the effect.

### Overconfident ranges

From S32 (raw PDF page 7): when people give a range they are 98% sure
contains the true value, the truth should fall outside only 2% of the time.
In most studies it fell outside about 30% of the time.

## Quotable passages

> The contrary of every matter of fact is still possible; because it can never imply a contradiction

[S28], location = Enquiry, Section IV, Part I, paragraph 21, verified: yes

> That the sun will not rise to-morrow is no less intelligible a proposition, and implies no more contradiction than the affirmation, that it will rise.

[S28], location = Enquiry, Section IV, Part I, paragraph 21 (italics in the original dropped), verified: yes

> all our experimental conclusions proceed upon the supposition that the future will be conformable to the past.

[S28], location = Enquiry, Section IV, Part II, paragraph 30, verified: yes

> Custom, then, is the great guide of human life.

[S28], location = Enquiry, Section V, Part I, paragraph 36, verified: yes

> It is not a contradiction that the next piece of bread is not nourishing.

[S29], location = section 2 (reconstruction of Hume's argument), verified: yes

> In deductive inferences, what is inferred is necessarily true if the premises from which it is inferred are true; that is, the truth of the premises guarantees the truth of the conclusion.

[S30], location = section 1 (Abduction: The General Idea), verified: yes

> both are ampliative, meaning that the conclusion goes beyond what is (logically) contained in the premises

[S30], location = section 1, verified: yes

> in abduction there is an implicit or explicit appeal to explanatory considerations, whereas in induction there is not; in induction, there is only an appeal to observed frequencies or statistics.

[S30], location = section 1 (emphasis in original dropped), verified: yes

> the best of a bad lot

[S30], location = section 2 (quoting van Fraassen 1989, p. 143), verified: yes

> Although we infer that Tweety flies on the basis of the information that Tweety is a bird and the background knowledge that birds usually fly, we have good reasons to retract this inference when learning that Tweety is a penguin or a kiwi.

[S31], location = section 1, Dealing with the dynamics of defeasible reasoning, verified: yes

> Bayes’ theorem isn’t just a useful calculational tool.

[S21], location = section 1.2.2, Bayes' Theorem, verified: yes

> toward the initial values. We call this phenomenon anchoring.

[S32], location = PDF page 6 (Adjustment and Anchoring), verified: yes. Note: most of S32's markdown is scrambled by the two-column layout; this is the only long fragment that survives intact. The anchoring and overconfidence numbers above were read from the raw PDF with pypdfium2 (pages 6 and 7) and are not counted as verified quotes.

> Training, teaming, and tracking are psychological interventions that dramatically increased the accuracy of forecasts.

[S34], location = PDF page 1 (Abstract), verified: yes

> Tracking placed the highest performers (top 2% from Year 1) in elite teams that worked together.

[S34], location = PDF page 1 (Abstract), verified: yes

> We don’t deal in certainty, we deal in prob

[S34], location = PDF page 1 (quoting the film Zero Dark Thirty; the word continues "probability" after a line break), verified: yes

> 0 is the best score, and 2 is the worst

[S34], location = PDF page 3 (Questions and measures), verified: yes

> so extreme, incorrect forecasts are heavily punished.

[S34], location = PDF page 3, verified: yes

> which means that forecasters were overconfident

[S34], location = PDF page 6, verified: yes

> were accurate only about 70% of the time

[S34], location = PDF page 7 (forecasts of 100% made in the first 20% of days), verified: yes

> were correct about 90% of the time

[S34], location = PDF page 7 (the same forecasts made in the final 20% of days), verified: yes

> took only about 45 min to complete, the benefits lasted

[S34], location = PDF page 8 (Discussion), verified: yes

> the separate offices returned very different quotes.

[S35], location = opening paragraph (only part of the article is available), verified: yes

> Although all six statements were false, both researchers and students endorsed, on average, more than three statements, indicating a gross misunderstanding of CIs.

[S36], location = PDF page 1 (Abstract), verified: yes

> a CI can be used to evaluate only the procedure and not a specific interval.

[S36], location = PDF page 4 (Method), verified: yes

> If we were to repeat the experiment over and over, then 95 % of the time the true mean falls between 0.1 and 0.4.

[S36], location = PDF page 4 (false statement 6, the most endorsed by master students at 79%), verified: yes

> 7.8%

[S59], location = PDF pages 3 and 11, verified: yes (the rest of S59's markdown is garbled; the sentence "Eddy (1982) reported that 95 out of 100 physicians estimated the posterior probability p(cancer | positive) to be between 70% and 80%, rather than 7.8%" was read from the raw PDF, page 3, and is not counted as verified)

## Numbers and stories for the screen

- **The 1,000 women.** 10 have cancer, 8 of them test positive; 95 of the 990 healthy women also test positive. 8 of 103 positives are real: 7.8%. Most physicians guessed 70% to 80%. [S59]
- **16% to 50%.** Share of people reasoning correctly jumps from 16% with percentages to 46% and 50% with counts. [S59]
- **The wheel of fortune.** A random 10 leads to a median guess of 25%; a random 65 leads to 45%. [S32]
- **The 98% range that misses 30% of the time.** [S32]
- **"Steve is very shy and withdrawn."** People rank him as likely a librarian because he fits the stereotype, and ignore how few librarians there are compared with farmers. The engineer and lawyer experiment varied the base rate from 70:30 to 30:70 and people's answers barely changed. [S32, raw PDF page 2; paraphrase, not a verified quote]
- **Brier score of 0.02 versus 1.62.** Saying 90% and being right costs 0.02. Saying 90% and being wrong costs 1.62. [S34]
- **Good Judgment Project scale.** Year 1 began with 2,246 participants; 85 questions closed in Year 1 and 114 in Year 2; superforecasters were the top 2%. [S34]
- **The 45-minute training.** A short probability-training module improved accuracy for two seasons. [S34]
- **The early 100%.** Early "certain" forecasts were right about 70% of the time; late ones about 90%. [S34]
- **Zero Dark Thirty.** "We don't deal in certainty, we deal in probability... sixty percent" versus the analyst who says 100%, then 95% "because I know how certainty freaks you guys out." Mellers et al. open their paper with it. [S34]
- **Same file, two offices, two very different quotes.** [S35]
- **Six false statements.** Researchers endorsed on average 3.45, master students 3.24, first-year students 3.51. 59% of researchers endorsed "There is a 95% probability that the true mean lies between 0.1 and 0.4." [S36, PDF page 4, Table 1]
- **Tweety the penguin.** One new fact overturns a safe-looking conclusion. [S31]
- **The sun tomorrow.** Its failure to rise is not a contradiction, only a surprise. [S28]

## Candidate visuals

- **Three arrows.** Deduction as a locked chain (premises to conclusion, no gap). Induction as a stack of past observations with a dotted arrow into the future. Abduction as evidence with several candidate explanations, one highlighted; then a faint outline appears for an explanation that was never on the list ("the best of a bad lot").
- **Hume's bridge.** A bridge from "past" to "future" whose support column is labeled "the future resembles the past," and the column rests on the bridge itself (circularity).
- **Tweety update.** A bird icon with a green "flies" tag; a penguin label drops in and the tag flips to red. Caption: adding a fact removed a conclusion.
- **Icon array of 1,000 dots.** 10 colored for cancer; 8 of those outlined as positive; 95 of the gray dots outlined as positive. Zoom into the 103 outlined dots; 8 are colored. Counter reads 7.8%. Then show the physicians' guess of 70% to 80% as a bar far to the right.
- **Wheel of fortune.** Two spins, 10 and 65, each with a crowd's estimate sliding toward the number and stopping at 25 and 45.
- **Brier scoreboard.** Four forecasters across four days of weather icons, with running squared-error bars. The "always certain" forecaster's bar leaps on the one dry day.
- **Calibration curve.** Stated confidence on the x-axis, how often right on the y-axis, the diagonal as perfect calibration. Points below the line are overconfidence. Use S34 Figures 2 and 3 as the model.
- **Noise target.** Two panels: arrows clustered off-center (bias) and arrows scattered around the center (noise).
- **Confidence interval ladder.** Twenty horizontal intervals from repeated experiments, 19 crossing a vertical "true value" line and one missing it. Caption: 95% is about the method, not about any one interval.

## Gaps and cautions

- **Superforecasting (Tetlock and Gardner 2015) was not fetched.** Claims about superforecasters here rest on Mellers et al. 2014 [S34] only. Do not quote the book or its popular numbers (for example claims about beating intelligence analysts by a set percentage) without a source.
- **Brier 1950 [S33] is only the AMS landing page.** The full text is not in `sources/brier-1950-verification.md`, so no quote from Brier himself is verified. The definition and example here come from S34, which cites Brier 1950. Note that S34 uses the two-outcome form (range 0 to 2); many other sources use the one-outcome form (range 0 to 1), which is half as large for yes/no events. Pick one form and say which on screen.
- **HBR "Noise" [S35] is partial.** Only the summary and opening anecdote are available. The book *Noise* (2021) was not fetched. Any numbers about noise audits (for example underwriters differing by a set percentage) need another source before they go on screen.
- **S32 (Tversky and Kahneman) and S59 (Gigerenzer and Hoffrage) converted badly.** The two-column scans produced scrambled markdown. Numbers marked "raw PDF page N" were read directly from the downloaded PDFs with pypdfium2. They are reliable but did not pass the markdown `verify` check, so they are not counted as verified quotes. A cleaner re-parse of those two PDFs would fix this.
- **The Brier score table with four forecasters is our illustration.** Only the 0.02 and 1.62 figures come from S34.
- **Hoekstra's Table 1 column headers are misaligned in the markdown.** The order is first-year students (n = 442), master students (n = 34), researchers (n = 118), matching the mean endorsements 3.51, 3.24, and 3.45.
- **The "fits the stereotype" librarian example is a paraphrase.** The exact Steve quote did not verify in the markdown.
