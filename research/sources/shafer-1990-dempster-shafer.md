---
title: Dempster-Shafer Theory
authors: Glenn Shafer
year: '1990'
url: https://fitelson.org/topics/shafer.pdf
final_url: https://fitelson.org/topics/shafer.pdf
retrieved: '2026-09-23'
sha256: 12b30c5003cb9cd989886165725298beb78e1bce0ab826a645003f2a434c6fb0
kind: pdf
parser: kaos-pdf
tier: http
engine: curl_cffi
escalated: false
found_by: exa
note: ''
chars: 6411
---

# Dempster-Shafer Theory

Glenn Shafer1

The Dempster-Shafer theory, also known as the theory of belief functions, is a generalization of the

Bayesian theory of subjective probability. Whereas the Bayesian theory requires probabilities for each

question of interest, belief functions allow us to base degrees of belief for one question on probabilities for

a related question. These degrees of belief may or may not have the mathematical properties of

probabilities; how much they differ from probabilities will depend on how closely the two questions are

related.

The Dempster-Shafer theory owes its name to work by A. P. Dempster (1968) and Glenn Shafer

(1976), but the kind of reasoning the theory uses can be found as far back as the seventeenth century. The

theory came to the attention of AI researchers in the early 1980s, when they were trying to adapt probability

theory to expert systems. Dempster-Shafer degrees of belief resemble the certainty factors in MYCIN, and

this resemblance suggested that they might combine the rigor of probability theory with the flexibility of

rule-based systems. Subsequent work has made clear that the management of uncertainty inherently

requires more structure than is available in simple rule-based systems, but the Dempster-Shafer theory

remains attractive because of its relative flexibility.

The Dempster-Shafer theory is based on two ideas: the idea of obtaining degrees of belief for one

question from subjective probabilities for a related question, and Dempster's rule for combining such

degrees of belief when they are based on independent items of evidence.

To illustrate the idea of obtaining degrees of belief for one question from subjective probabilities for

another, suppose I have subjective probabilities for the reliability of my friend Betty. My probability that

she is reliable is 0.9, and my probability that she is unreliable is 0.1. Suppose she tells me a limb fell on my

car. This statement, which must true if she is reliable, is not necessarily false if she is unreliable. So her

testimony alone justifies a 0.9 degree of belief that a limb fell on my car, but only a zero degree of belief

(not a 0.1 degree of belief) that no limb fell on my car. This zero does not mean that I am sure that no limb

fell on my car, as a zero probability would; it merely means that Betty's testimony gives me no reason to

believe that no limb fell on my car. The 0.9 and the zero together constitute a belief function.

To illustrate Dempster's rule for combining degrees of belief, suppose I also have a 0.9 subjective

probability for the reliability of Sally, and suppose she too testifies, independently of Betty, that a limb fell

on my car. The event that Betty is reliable is independent of the event that Sally is reliable, and we may

multiply the probabilities of these events; the probability that both are reliable is 0.9x0.9 = 0.81, the

probability that neither is reliable is 0.1x0.1 = 0.01, and the probability that at least one is reliable is 1 -

0.01 = 0.99. Since they both said that a limb fell on my car, at least of them being reliable implies that a

limb did fall on my car, and hence I may assign this event a degree of belief of 0.99.

Suppose, on the other hand, that Betty and Sally contradict each other—Betty says that a limb fell on

my car, and Sally says no limb fell on my car. In this case, they cannot both be right and hence cannot both

be reliable—only one is reliable, or neither is reliable. The prior probabilities that only Betty is reliable,

only Sally is reliable, and that neither is reliable are 0.09, 0.09, and 0.01, respectively, and the posterior

probabilities (given that not both are reliable) are , and , respectively. Hence we have a degree of

9919

19 , 19 19 19

belief that a limb did fall on my car (because Betty is reliable) and a degree of belief that no limb fell on

9

19

my car (because Sally is reliable).

In summary, we obtain degrees of belief for one question (Did a limb fall on my car?) from

probabilities for another question (Is the witness reliable?). Dempster's rule begins with the assumption that

the questions for which we have probabilities are independent with respect to our subjective probability

judgments, but this independence is only a priori; it disappears when conflict is discerned between the

different items of evidence.

Implementing the Dempster-Shafer theory in a specific problem generally involves solving two related

problems. First, we must sort the uncertainties in the problem into a priori independent items of evidence.

Second, we must carry out Dempster's rule computationally. These two problems and and their solutions

are closely related. Sorting the uncertainties into independent items leads to a structure involving items of

evidence that bear on different but related questions, and this structure can be used to make computations

1

Ronald G. Harper Distinguished Professor of Business, School of Business,

Summerfield Hall, University of Kansas, Lawrence, Kansas 66045.

feasible. Suppose, for example, that Betty and Sally testify independently that they heard a burglar enter my

house. They might both have mistaken the noise of a dog for that of a burglar, and because of this common

uncertainty, I cannot combine degrees of belief based on their evidence directly by Dempster's rule. But if I

consider explicitly the possibility of a dog's presence, then I can identify three independent items of

evidence: my other evidence for or against the presence of a dog, my evidence for Betty's reliability, and

my evidence for Sally's reliability. I can combine these items of evidence by Dempster's rule and the

computations are facilitated by the structure that relates the different questions involved.

For more information, see Shafer (1990) and the articles on the belief functions in Shafer and Pearl

(1990).

## References

*Dempster, A.P. (1968). A generalization of Bayesian inference. Journal of the Royal Statistical Society,*

### Series B 30 205-247.

*Shafer, Glenn (1976). A Mathematical Theory of Evidence. Princeton University Press.*

*Shafer, Glenn (1990). Perspectives on the theory and practice of belief functions. International Journal of*

### Approximate Reasoning 3 1-40.

*Shafer, Glenn, and Judea Pearl, eds. (1990). Readings in Uncertain Reasoning. Morgan Kaufmann.*

2
