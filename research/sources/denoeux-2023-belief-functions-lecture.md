---
title: 'Theory of Belief Functions: Application to machine learning and statistics (lecture 1)'
authors: Thierry Denoeux
year: '2023'
url: https://www.hds.utc.fr/~tdenoeux/dokuwiki/_media/en/bf2023_lecture1.pdf
final_url: https://www.hds.utc.fr/~tdenoeux/dokuwiki/_media/en/bf2023_lecture1.pdf
retrieved: '2026-09-23'
sha256: ff8f71ee8fdd7693160a6094d2e0dfcf017311fe23515410f5129edae7ab39ea
kind: pdf
parser: kaos-pdf
tier: http
engine: curl_cffi
escalated: false
found_by: exa
note: ''
chars: 26985
---

Lecture 1: basic concepts

Thierry Denœux

Summer 2023

Belief functions - Basic concepts Summer 2023 1 / 53

# learning and statistical inference

Theory of Belief Functions: Application to machine

*“Reasoning with fuzzy and uncertain evidence using epistemic random fuzzy*

Random sets and belief functions in a general framework (lecture + exercises)

*“Constructing belief functions from sample data using multinomial confidence*

*“A neural network classifier based on Dempster-Shafer theory”*

*“A k-nearest neighbor classification rule based on Dempster-Shafer theory”*

First applications: classification and statistical inference

Belief functions on finite sets. Dempster’s rule (lecture + exercises)

[https://www.hds.utc.fr/\~tdenoeux/dokuwiki/en/bf](https://www.hds.utc.fr/~tdenoeux/dokuwiki/en/bf)

# Outline of the course I

Course homepage:

Roadmap:

1 Basic notions:

Decision making (lecture + exercises)

2

(paper reading + exercises in R)

exercises in R)

*regions” (paper reading + exercises in R)*

3 Advanced concepts:

Possibility and Random fuzzy sets

*sets: general framework and practical models”*

Thierry Denœux Belief functions - Basic concepts

(paper reading +

(paper reading + exercises)

Summer 2023 2 / 53

# Outline of the course II

4 Statistical and ML applications:

Statistical prediction using belief functions: application to linear and logistic

regression

*“Prediction of future observations using belief functions: a likelihood-based*

*approach” (paper reading + exercises)*

*“Quantifying Prediction Uncertainty in Regression using Random Fuzzy Sets:*

*the ENNreg model” (paper reading + exercises)*

5 Statistical inference and learning from uncertain data:

*“Maximum likelihood estimation from Uncertain Data in the Belief Function*

*Framework” (paper reading + exercises)*

*“Parametric Classification with Soft Labels using the Evidential EM Algorithm”*

(paper reading + exercises)

6 Project

7 Project presentation

Thierry Denœux Belief functions - Basic concepts Summer 2023 3 / 53

Some applications to econometrics. A new research avenue to explore!

(information fusion, uncertainty quantification, risk analysis), statistics

Many applications in AI (expert systems, machine learning), engineering

such as interval analysis as special cases: it is very general.

DS encompasses probability theory and set-membership approaches

statistical inference, and developed by G. Shafer in the late 1970’s into a

This formalism was introduced by A. P. Dempster in the 1960’s for

What we will study in this course

A mathematical formalism called

Dempster-Shafer (DS) theory

Evidence theory

Theory of belief functions

general theory for reasoning under uncertainty

.

(statistical estimation and prediction), etc.

Thierry Denœux Belief functions - Basic concepts

Summer 2023 4 / 53

# Outline

1 Representation of evidence

Mass functions

Consonant belief functions

2 Dempster’s rule

Definition

Conditioning

Commonality function

Representation of evidence

Belief and plausibility functions

Belief functions - Basic concepts Summer 2023 5 / 53

Let Ω

A probability mass function

The corresponding

defined by

be a finite set (sample space, universe or discourse,...)

# Reminder: probability mass functions and measures

Representation of evidence

*is mapping p : Ω → \[01\] such that*

*,*

*Xp(ω) = 1*

*ω∈Ω*

Ω

*probability measure is the mapping P : 2→ \[01\]*

*,*

*P(A) = Xp(ω) for all A ⊆ Ω*

*ω∈A*

Belief functions - Basic concepts Summer 2023 6 / 53

# Properties

*P(∅) = 0, P(Ω) =*

Additivity:

*∀A*

*,*

More generally, for any

Ω

,

*P*

Representation of evidence

1

*B ⊆ ΩP(A ∪ B) = P(A) + P(B) − P(A ∩ B)*

*,*

*k ≥ 2 and for any family A1Ak of subsets of*

*, . . . ,*

*k*

\[!X\\!

*|I|+1*

*Ai=(−1)PAi(1)*

*i=1∅6=6=I⊆{1k}i∈I*

*,...,*

Belief functions - Basic concepts Summer 2023 7 / 53

Representation of evidence

# Interpretations

1 Objective:

Ω is the set of possible outcomes of a random experiment

*p(ω) is the limit frequency of outcome ω in a series of repetitions of the*

random experiment

*P(A) is the limit frequency of the event “A*

”

*ω ∈*

2 Subjective:

Ω is the set of possible answers to some question

*P(A) is a agent’s degree of belief that the true answer belongs to A*

Probability theory is the mainstream formalism for representing uncertainty

in AI

Should degrees of belief be additive?

Thierry Denœux Belief functions - Basic concepts Summer 2023 8 / 53

Representation of evidence

# The case of complete ignorance

To highlight the implications of the additivity assumption, it is useful to

consider the extreme (but frequent) situation of complete ignorance

.

How to define a probability measure on Ω in that case?

The only sensible solution is provided by Laplace’s principle of

indifference (PI): “In the absence of any relevant evidence, agents should

distribute their credence (or ’degrees of belief’) equally among all the

possible outcomes under consideration”.

As shown by the following example, this principle leads to paradoxes.

Thierry Denœux Belief functions - Basic concepts Summer 2023 9 / 53

Representation of evidence

# Is there life around Sirius?

Consider the question: “Are there or are there not living beings in orbit

around the star Sirius”?

*The set of possibilities can be denoted by Θ = {θ1, θ2}, where*

*θ1 is the possibility that there is life*

*θ2 is the possibility that there is not*

As we are completely ignorant about this question, the probabilities

should be, according to the PI:

*p(θ1) = p(θ2) = 1/2*

Thierry Denœux Belief functions - Basic concepts Summer 2023 10 / 53

Representation of evidence

# Is there life around Sirius? (continued)

We could also have considered a refined set of possibilities, such as

*Ω = {ω1, ω2, ω3}, where*

*ω1 corresponds to the possibility that there is life around Sirius*

*ω2 corresponds to the possibility that there are planets but no life, and*

*ω3 corresponds to the possibility that there are not even planets*

With this new set of probabilities, complete ignorance is represented by

*p(ω1) = p(ω2) = p(ω3) = 1/3*

*But θhas the same meaning as ωand θhas the same meaning as*

1 1 2

*{ω2, ω3}, so the probability distributions on Θ and Ω are inconsistent.*

Thierry Denœux Belief functions - Basic concepts Summer 2023 11 / 53

Representation of evidence

# The solution: relax the additivity property

The Dempster-Shafer theory was introduced to solve such paradoxes.

*It replaces the probability measure P by two nonadditive measures: a*

belief function and a plausibility function.

The probabilistic formalism is recovered as a special case (known

frequencies or proportions in a population).

Thierry Denœux Belief functions - Basic concepts Summer 2023 12 / 53

# Outline

1 Representation of evidence

Mass functions

2 Dempster’s rule

Definition

Conditioning

Commonality function

Representation of evidence Mass functions

Belief and plausibility functions

Consonant belief functions

Belief functions - Basic concepts Summer 2023 13 / 53

Representation of evidence Mass functions

# Mass function

Definition

*Let Ω be the finite set of possible answers to some question X*

.

To emphasize the fact that the granularity of Ω is a matter of choice, Ω is

sometimes called the frame of discernment

Ω

*A mass function is a mapping m : 2→ \[01\] such that*

*,*

*Xm(A) = 1*

*A⊆Ω*

and

*m(∅) = 0*

*Every subset A of Ω such that m(A) > 0 is a focal set of m*

Thierry Denœux Belief functions - Basic concepts Summer 2023 14 / 53

, i.e., partial information about the question of interest.

Representation of evidence Mass functions

# Mass function

Interpretation

*In DS theory, a mass function m on Ω is used as a representation of*

evidence

It is usually induced by

*A mapping Γ from a set S of interpretations (or possible meanings) of the*

evidence

*Known probabilities on S*

*Each probability p(s) for s ∈ S is then transferred to subset*

*m(A) = Xp(s)*

*{s∈S:Γ(s)=A}*

Thierry Denœux Belief functions - Basic concepts

*Γ(s) ⊆ Ω, and*

Summer 2023 15 / 53

Representation of evidence Mass functions

# Example: road scene analysis

Realfworldfdrivingfscene

Over-segmentation

Camera LIDAR ... SensorfN

Ground Vegetation... ClassfK

Independentfclassificationfmodules

Classifiedfsegments

Fusionfonfafunified

decisionfspace

Thierry Denœux Belief functions - Basic concepts

Summer 2023 16 / 53

Representation of evidence Mass functions

# Example: road scene analysis (continued)

*Let X be the contents of some region in the image, and*

## Ω = {GRTOS}, corresponding to the possibilities Grass, Road,

*, , , ,*

### Tree/Bush, Obstacle, Sky.

Assume that a lidar sensor (laser telemeter) returns the information

*X ∈ {TO}, but we there is a probability p = 01 that the information is*

*, .*

not reliable (because, e.g., the sensor is out of order).

How to represent this information by a mass function?

Thierry Denœux Belief functions - Basic concepts Summer 2023 17 / 53

Representation of evidence Mass functions

# Formalization

S

(S,	2P)

,Ω

Γ

broken(0.1)

G

T

R

working(0.9)O

S

*Here, the probability p is not about X, but about the state of a sensor.*

*Let S = {workingbroken} the set of possible sensor states.*

*,*

*If the state is “working”, we know that X ∈ {TO}*

*, .*

*If the state is “broken”, we just know that X ∈ Ω, and nothing more.*

*This uncertain evidence can be represented by a mass function m on Ω*

,

such that

*m({TO}) = 09m(Ω) = 01*

*, ., .*

Thierry Denœux Belief functions - Basic concepts Summer 2023 18 / 53

Representation of evidence Mass functions

# Special cases

*Logical mass function: If the evidence tells us that X ∈ A for sure and nothing*

*more, for some A ⊆ Ω, then we have a logical mass function mAmA*

*such that mAmA(A) = 1. Example: mdenotes the mass*

*{TO}*

*,*

*function such that m({TO}) = 1.*

*{TO},*

*,*

*Vacuous mass function: In particular, mrepresents total ignorance; it is*

Ω

called the vacuous mass function

*Bayesian mass function: If all focal sets of m are singletons, m is said to be*

Bayesian. It is equivalent to a probability mass function.

*Example: m({T}) = 0.5, m({O}) = 0.5.*

A Dempster-Shafer mass function can thus be seen as

A generalized set

A generalized probability distribution

Thierry Denœux Belief functions - Basic concepts Summer 2023 19 / 53

# Outline

1 Representation of evidence

Mass functions

2 Dempster’s rule

Definition

Conditioning

Commonality function

Representation of evidence

Belief and plausibility functions

Consonant belief functions

Belief functions - Basic concepts

Belief and plausibility functions

Summer 2023 20 / 53

Representation of evidence Belief and plausibility functions

# Defiinitions

*Given a mass function m on Ω, the corresponding belief and plausibility*

Ω

functions are mappings from 2to \[0,1\] defined as follows:

*Bel(A) = Xm(B)*

*B⊆A*

*Pl(A) = Xm(B) = 1 − Bel(A).*

*B∩A6=6=∅*

Interpretation:

*Bel(A) is a measure of the strength with which A is supported by the*

*available evidence (taking into accounts all subsets B ⊆ A); it is a degree of*

*belief in A*

*Pl(A) is a measure of the lack of support given to the complement of A, it is*

*a degree of lack of belief in A*

Thierry Denœux Belief functions - Basic concepts Summer 2023 21 / 53

# Elementary properties

*Bel(∅) = Pl(∅) =*

*Bel(Ω) = Pl(Ω) =*

*For all A ⊆ Ω*

,

Superadditivity of

*Bel*

Subadditivity of

Representation of evidence Belief and plausibility functions

0

1

*Bel(A) = 1 − Pl(A)*

*Pl(A) = 1 − Bel(A)*

*Bel:*

*(A ∪ B) ≥ Bel(A) + Bel(B)*

*Pl:*

*Pl(A ∪ B) ≤ Pl(A) + Pl(B) −*

Belief functions - Basic concepts

*− Bel(A ∩ B)*

*Pl(A ∩ B)*

Summer 2023 22 / 53

Representation of evidence Belief and plausibility functions

# Two-dimensional representation

*The uncertainty about a proposition A is represented by two numbers:*

*Bel(A) and Pl(A), with Bel(A) ≤ Pl(A)*

*The intervals \[Bel(A)Pl(A)\] have maximum length when m is vacuous:*

*,*

*then, Bel(A) = 0 for all A 6= Ω6= , and Pl(A) = 1 for all A 6= 6= ∅*

.

*The intervals \[Bel(A)Pl(A)\] have minimum length when m is Bayesian.*

*,*

Then,

*Bel(A) = Pl(A) = Xm({ω})*

*ω∈A*

*for all A, and Bel is a probability measure.*

Thierry Denœux Belief functions - Basic concepts Summer 2023 23 / 53

Representation of evidence Belief and plausibility functions

# Road scene analysis example

*We had Ω = {GRTOS} and*

*, , , ,*

*m({TO}) = 09m(Ω) = 01*

*, ., .*

What are the credibility and the plausibility that the region corresponds or

does not correspond to a tree?

*Bel({T}) = 0Pl({T}) = 09 + 01 = 1*

*, ..*

*Bel({T}) = 0Pl({T}) = 1*

*,*

But

*Bel({T} ∪ {T}) = Bel(Ω) = 1*

and

*Pl({T} ∪ {T}) = Pl(Ω) = 1.*

Thierry Denœux Belief functions - Basic concepts Summer 2023 24 / 53

# Characterization of belief functions

Representation of evidence Belief and plausibility functions

Theorem

Ω

*Let F : 2→ \[01\]. The following two statements are equivalent:*

*,*

Ω

*Statement 1 There exists a mass function m : 2→ \[01\]*

*,*

*F(A) = Pm(B) for all A ⊆ Ω (i.e., F is a*

*B⊆A*

*Statement 2 Function F has the following 3 properties:*

*1 F(∅) = 0*

*2 F(Ω) = 1*

*3 For any k ≥ 2 and for any family A1A*

*, . . . ,*

*k*

\[!X

*|I|+1*

*FAi≥(−1)F*

*i=1∅6=6=I⊆{1k}*

*,...,*

(Property (2) is called complete monotonicity).

Thierry Denœux Belief functions - Basic concepts

*such that*

*belief function)n).*

Ω

*in 2*

*k ,*

*\\Ai!(2)*

*i∈I*

Summer 2023 25 / 53

Representation of evidence Belief and plausibility functions

# Relations between mBel and Pl

,

*Let m be a mass function, Bel and Pl the corresponding belief and*

plausibility functions

Thanks to the following equations, given any one of these functions, we

*can recover the other two: for all A ⊆ Ω*

,

*Bel(A) = Xm(B)*

*B⊆A*

*Pl(A) = 1 − Bel(A)*

*Bel(A) = 1 − Pl(A)*

X

*|A|−|B|*

*m(A) = (−1)Bel(B)*

*∅6=6=B⊆A*

*mBel et Pl are thus three equivalent representations of a piece of*

,

evidence.

Thierry Denœux Belief functions - Basic concepts Summer 2023 26 / 53

# Outline

1 Representation of evidence

Mass functions

2 Dempster’s rule

Definition

Conditioning

Commonality function

Representation of evidence

Belief and plausibility functions

Consonant belief functions

Belief functions - Basic concepts

Consonant belief functions

Summer 2023 27 / 53

Representation of evidence Consonant belief functions

# Definition and theorem

Consonant mass functions are an important special case.

Definition (Consonant mass function)

*A mass function m is consonant iff its focal sets are nested, d, i.e., for any two*

*focal set Aand Aj, A⊆ Aj or Aj ⊆ A*

*i Aji Aj Aj i*

Theorem

*Let m be a mass function, and let Bel and Pl be the corresponding belief and*

*plausibility functions. The following statements are equivalent:*

*1 m is consonant*

*2 For any AB ⊆ Ω, Bel(A ∩ B) = min \[Bel(A)Bel(B)\]*

*, ,*

*3 For any AB ⊆ Ω, Pl(A ∪ B) = max \[Pl(A)Pl(B)\]*

*, ,*

*4 For any A ⊆ Ω, Pl(A) = maxA pl(ω), where pl(ω) = Pl({ω})*

*ω∈*

*(Function pl : Ω → \[01\] is called the contour function).*

*,*

Thierry Denœux Belief functions - Basic concepts Summer 2023 28 / 53

# Proof of 1 ⇒

*Let m*

*For any AB ⊆*

*,*

*A⊆ B, respectively.*

*i*

*Then, Ai ⊆ A*

Representation of evidence Consonant belief functions

2

*be a consonant mass function with focal sets A⊆ A⊆ ⊆ A*

*1 2 . . . r.*

*Ω, let i1 i1 and i2 i2 be the largest indices such that Ai ⊆ A and*

*∩ B iff i ≤ min(i1i1i2i2) and*

*,*

*min(i1i1i2i2)*

*,*

*Bel(A ∩ B) =Xm(Ai)*

*i=1*

*i1i2*

!

i1i2

*= min Xm(Ai)Xm(Ai)*

*,*

*i=1i=1*

*= min(Bel(A)Bel(B))*

*, .*

Belief functions - Basic concepts Summer 2023 29 / 53

Representation of evidence Consonant belief functions

# Proof of 2 ⇒ 3

*Now, from the equality A ∪ B = A ∩ B, we have*

*Pl(A ∪ B) = 1 − Bel(A ∪ B)*

*= 1 − Bel(A ∩ B)*

*= 1 − min(Bel(A)Bel(B))*

*,*

*= max(1 − Bel(A)1 − Bel(B))*

*,*

*= max(Pl(A)Pl(B))*

*, .*

Thierry Denœux Belief functions - Basic concepts

Summer 2023 30 / 53

Representation of evidence Consonant belief functions

# Proof of 3 ⇒ 4

*Assume that Pl(A ∪ B) = max(Pl(A)Pl(B)) for all AB ⊆ Ω*

*, , .*

*Let Πbe the following property: Pl(A) = maxA pl(ω) for all A ⊆ Ω such*

*n ω∈*

*that |A| ≤ n.*

*We prove Πfor all n ≥ 0 by induction:*

*n*

Πand Πtrivially true.

1 2

*Assume Πn is true and let A ⊆ Ω such that |A| = n + 1. We can write*

*A = B ∪ {ω0} with |B| = n. Consequently,*

*Pl(A) = max(Pl(B)pl(ω0))*

*,*

*= max(maxpl(ω)pl(ω0))*

*,*

*ω∈B*

*= maxpl(ω)*

*ω∈A*

Thierry Denœux Belief functions - Basic concepts Summer 2023 31 / 53

be the frame of discernment with elements arranged

Representation of evidence Consonant belief functions

# Proof of 4 ⇒ 1 I

A=Ω

A4

A3

A2

1

ωωωω

1234

*Let Pl be a plausibility function verifying Pl(A) = maxA*

*ω∈*

*Let Ω = {ω1, . . . , ω}*

*n*

by decreasing order of plausibility, i.e.,

*1 = pl(ω1) ≥ pl(ω2) ≥ ≥ pl(ω)*

*. . . n*

*and let Ai denote the set {ω1, . . . , ωi}, for 1 ≤ i ≤ n.*

*Let m denote the following consonant mass function:*

*m(Ai) = pl(ωi) − pl(ωi1)1 ≤ i ≤ n − 1*

*+,*

*m(Ω) = pl(ω)*

*n.*

Thierry Denœux Belief functions - Basic concepts

*pl(ω) for all A.*

Summer 2023 32 / 53

For instance, for the following contour function defined on the frame

# Example

*Ω = {abcd}:*

*, , ,*

the corresponding mass function is

Representation of evidence

*ω*

*pl(ω)*

*m({c}) =*

| m({cdba}) = | , , , | 03 | .. |
| --- | --- | --- | --- |
| m({cdb}) = | , , | 05 − 03 = 02 | ... |
| m({cd}) = | , | 07 − 05 = 02 | ... |

Consonant belief functions

*a b c d*

0.3 0.5 1 0.7

*1 − 07 = 03*

*..*

Belief functions - Basic concepts Summer 2023 33 / 53

Representation of evidence Consonant belief functions

# Proof of 4 ⇒ 1 (continued)

*Let Plm be the plausibility function induced by m*

*lm .*

*For any subset A of Ω, let iA iA = min{1 ≤ i ≤ n : ωi ∈ A}.*

*A∩ A 6= 6= ∅ iff i ≥ iA*

*i iA.*

Consequently,

*n*

*Plm(A) = Xm(Ai)*

*lm*

*i=iAiA*

*= pl(ωiA) − pl(ωiA1) + pl(ωiA1) − pl(ωiA2) +*

*iAiA+iA+iA+. . .*

*= pl(ωiA)*

*iA*

*= maxpl(ω) = Pl(A)*

*,*

*ω∈A*

*i.e., Plm = Pl*

*lm .*

Thierry Denœux Belief functions - Basic concepts

*− pl(ω) + pl(ω)*

*nn*

Summer 2023 34 / 53

# Outline

1 Representation of evidence

Mass functions

2 Dempster’s rule

Definition

Conditioning

Commonality function

Belief and plausibility functions

Consonant belief functions

Dempster’s rule

Belief functions - Basic concepts Summer 2023 35 / 53

# Outline

1 Representation of evidence

Mass functions

2 Dempster’s rule

Definition

Conditioning

Commonality function

Belief and plausibility functions

Consonant belief functions

Dempster’s rule

Belief functions - Basic concepts

Definition

Summer 2023 36 / 53

Dempster’s rule Definition

# Road scene example continued

*Variable X was defined as the type of object in some region of the image,*

*and the frame was Ω = {GRTOS}, corresponding to the possibilities*

*, , , ,*

### Grass, Road, Tree/Bush, Obstacle, Sky

A lidar sensor gave us the following mass function:

*m1({TO}) = 09m1(Ω) = 01*

*, ., .*

Now, assume that a camera returns the mass function:

*m2({GT}) = 08m2(Ω) = 02*

*, ., .*

How to combine these two pieces of evidence?

Thierry Denœux Belief functions - Basic concepts Summer 2023 37 / 53

# Analysis

If interpretations

*and sboth hold is*

2

Dempster’s rule Definition

(SP)

1,1

broken(0.1)

Γ

1

working(0.9)

(SP)

2,2

working(0.8)

Γ

2

broken

(0.2)

*s∈ Sand s∈ S2*

1 1 2 S2

If the two pieces of evidence are independent

*P1({s1})P2P2({s2})*

Belief functions - Basic concepts

Ω

S

O

R

T

G

*both hold, then X ∈ Γ1(s1) ∩ Γ2(s2)*

*, then the probability that s1*

Summer 2023 38 / 53

We then get the following combined mass function,

# Computation

*m1\\m2*

*{OT} (0.9)*

*,*

Ω (0.1)

Dempster’s rule Definition

*{TG}*

*,*

(0.8) (0.2)

*{T} (0.72) {O*

*,*

###### {TG} (0.08) Ω

*,*

*m({T}) = 0.72*

*m({OT}) = 018*

*, .*

*m({TG}) = 008*

*, .*

*m(Ω) = 0.02*

Belief functions - Basic concepts

Ω

*T} (0.18)*

(0.02)

Summer 2023 39 / 53

*If Γ1(s1) ∩ Γ2*

eliminate such pairs

# Case of conflicting pieces of evidence

Dempster’s rule Definition

(SP)

1,1

broken(0.1)

Γ

1 Ω

working(0.9)

S

O

R

T

(SP)

2,2

G

working(0.8)

Γ

2

broken

(0.2)

*(s) = ∅, we know that sand scannot hold simultaneously*

21 2

*The joint probability distribution on S× S2 must be conditioned to*

1 S2

Belief functions - Basic concepts Summer 2023 40 / 53

Dempster’s rule Definition

# Computation

*m1\\m2 {GR} Ω*

*,*

(0.8) (0.2)

*{OT} (0.9) ∅ (0.72) {OT} (0.18)*

*, ,*

###### Ω (0.1) {GR} (0.08) Ω (0.02)

*,*

We then get the following combined mass function,

*m(∅) = 0*

*m({OT}) = 018/028 = 9/14*

*, ..*

*m({GR}) = 008/028 = 4/14*

*, ..*

*m(Ω) = 0.02/0.28 = 1/14*

Thierry Denœux Belief functions - Basic concepts Summer 2023 41 / 53

Dempster’s rule Definition

# Dempster’s rule

*Let mand mbe two mass functions and*

1 2

*κ =Xm1(B)m2(C)*

*B∩C=∅*

their degree of conflict

*If κ \< 1, then mand mcan be combined as*

1 2

1

*(m1 ⊕ m2)(A) = Xm1(B)m2(C)∀A 6= 6= ∅ (3)*

*,*

*1 − κ*

###### B∩C=A

*and (m⊕ m)(∅) = 0*

1 2

*m⊕ mis called the orthogonal sum of mand m*

1 2 1 2

This rule can be used to combine mass functions induced by

independent pieces of evidence

Thierry Denœux Belief functions - Basic concepts Summer 2023 42 / 53

Dempster’s rule Definition

# Another example

*A ∅ {a} {b} {ab} {c} {ac} {bc} {abc}*

*, , , , ,*

*m1(A) 0 0 0.5 0.2 0 0.3 0 0*

*m2(A) 0 0.1 0 0.4 0.5 0 0 0*

*m2*

*{a}01 {ab}04 {c}05*

*, ., , ., .*

*{b}05 ∅005 {b}02 ∅025*

*, ., ., ., .*

*m{ab}02 {a}002 {ab}008 ∅01*

*1 , , ., ., , ., .*

*{ac}03 {a}003 {a}012 {c}015*

*, , ., ., ., .*

*The degree of conflict is κ = 005 + 025 + 01 = 04. The combined mass*

*....*

function is

*(m1 ⊕ m2)({a}) = (0.02 + 0.03 + 0.12)/0.6 = 0.17/0.6 ≈ 0.2833*

*(m1 ⊕ m2)({b}) = 0.2/0.6 = 1/3*

*(m1 ⊕ m2)({ab}) = 008/06 ≈ 01333*

*, ...*

*(m1 ⊕ m2)({c}) = 0.15/0.6 = 0.25.*

Thierry Denœux Belief functions - Basic concepts Summer 2023 43 / 53

singleton with another subset is either a singleton, or the empty set).

Dempster’s rule Definition

# Properties

*1 Commutativity, associativity. Neutral element: m?*

*2 Generalization of intersection: if mA and m*

*mA B*

*and A ∩ B 6= 6= ∅, then*

*mA mA ⊕ mB = mAmAB*

*∩*

*3If either mor mis Bayesian, then so is m⊕ m*

1 2 1

Thierry Denœux Belief functions - Basic concepts

are logical mass functions

2 (as the intersection of a

Summer 2023 44 / 53

# Outline

1 Representation of evidence

Mass functions

2 Dempster’s rule

Definition

Conditioning

Commonality function

Belief and plausibility functions

Consonant belief functions

Dempster’s rule

Belief functions - Basic concepts

Conditioning

Summer 2023 45 / 53

Dempster’s rule Conditioning

# Dempster’s rule conditioning

*Conditioning is a special case, where a mass function m is combined with*

*a logical mass function mB. Notation:*

*m ⊕ mB = m(· | B)*

*We thus have m(A | B) = 0 for any A not included in B and, for any*

*A ⊆ B*

,

X

1

*(A | B) = (1 )(C)(4)*

*−*

*m− κm*

*,*

###### C∩B=A

*where the degree of conflict κ is*

*κ =Xm(C) = 1 −Xm(C) = 1 − Pl(B).*

*C∩B=∅C∩B6=6=∅*

Thierry Denœux Belief functions - Basic concepts Summer 2023 46 / 53

Dempster’s rule Conditioning

# Conditional plausibility function

Proposition

*The plausibility function Pl(·|B) induced by m(·|B) is given by*

*Pl(A ∩ B)*

*Pl(A | B) =*

*Pl(B)*

*Proof: We have*

*Pl(A | B) = Xm(C|B)*

*{C:C∩A6=6=∅}*

XX

1

*Pl(B)(D)*

*−*

*= m*

*{C:C∩A6=6=∅}{D:D∩B=C}*

*Pl(A ∩ B)*

X

1

*Pl(B)(D) =*

*−*

*= m*

*Pl(B)*

*{D:D∩B∩A6=6=∅}*

*If Pl is a probability measure, Pl(· | B) is, thus, the conditional probability*

*measure given B: Dempster’s rule of combination thus extends Bayesian*

conditioning

.

Thierry Denœux Belief functions - Basic concepts Summer 2023 47 / 53

# Outline

1 Representation of evidence

Mass functions

Belief and plausibility functions

Consonant belief functions

2 Dempster’s rule

Definition

Conditioning

Commonality function

Dempster’s rule

Belief functions - Basic concepts

Commonality function

Summer 2023 48 / 53

is another equivalent representation of a belief function.

# Commonality function

Commonality function

Conversely,

*Q*

*Properties: Q(∅) =*

Dempster’s rule Commonality function

Ω

*: let Q : 2→ \[01\] be defined as*

*,*

#### Q(A) = Xm(B)∀A ⊆ Ω

*,*

*B⊇A*

X

*|B\\A|*

*m(A) = (−1)Q(B) (5)*

*B⊇A*

*1 and Q(Ω) = m(Ω)*

Belief functions - Basic concepts Summer 2023 49 / 53

*Let Qand Q2*

1 Q2

*Let Q⊕ Q2*

1 Q2

*We have (Q1 ⊕*

# Commonality function and Dempster’s rule

Dempster’s rule Commonality function

*be the commonality functions associated to m1 and m2*

.

*be the commonality function associated to m1 ⊕ m2*

.

*Q2)(∅) = 1 and, for all non empty subset A of Ω*

Q2,

1

*(QQ2)(A) = (1 )Q(A) Q2(A)*

*−*

*1 ⊕ Q2− κ1· Q2.*

Belief functions - Basic concepts Summer 2023 50 / 53

# Proof

*(Q1 ⊕*

##### Q2Q2)(A

Dempster’s rule Commonality function

*) = X(m1 ⊕ m2)(B)*

*B⊇A*

XX

1

*= (1 )(C)(D)*

*−*

*− κm1m2*

###### B⊇AC∩D=B

X

1

*= (1 )(C)(D)*

*−*

*− κm1m2*

###### C∩D⊇A

X

1

*= (1 )(C)(D)*

*−*

*− κm1m2*

###### C⊇AD⊇A

*,*






XX

1

*= (1 )(C)*

*−*

*− κm1m2*






###### C⊇AD⊇A

1

*= (1 )Q(A) Q2(A)*

*−*

*− κ1· Q2.*

Belief functions - Basic concepts




*(D)*




Summer 2023 51 / 53

Dempster’s rule Commonality function

Product rule for commonality and contour functions

*Using (5) with A = ∅, we get*

X

*|B|*

*(−1)Q(B) = −Q(∅) = −1(6)*

*,*

*∅6=6=B⊆Ω*

which makes it possible to compute the commonality function once

commonality numbers are determined up to some multiplicative constant.

(See following example)

*Given two mass functions mand m, we can thus combine them either*

1 2

using (3), or by converting them to commonality functions, multiplying

them pointwise, and computing the corresponding mass function using

(5).

*In particular, pl(ω) = Q({ω}). Consequently,*

1

*pl1 pl2 = (1 )pl1pl2*

*−*

*l1 ⊕ l2 − κl1l2.*

Thierry Denœux Belief functions - Basic concepts Summer 2023 52 / 53

0 0.2833 0.3333 0.1333 0.25 0 0 0

1 0.4167 0.4667 0.1333 0.25 0 0 0

1 0.25 0.28 0.08 0.15 0 0 0

1 0.5 0.4 0.4 0.5 0 0 0

1 0.5 0.7 0.2 0.3 0.3 0 0

# Example (cf. Slide 43)

*A ∅ {a*

*Q1(A)*

##### Q2Q2(A) Q1(A)Q2Q2(A)

1

*(1 )1/(025*

*−*

*− κ= −−.*

*A ∅ {a*

###### (Q1 ⊕ Q2Q2)(A)

*(m1 ⊕ m2)(A)*

Dempster’s rule Commonality function

*} {b} {ab} {c} {ac*

*, ,*

*− 0.28 − 0.15 + 0.08) = 1.6667*

*⇒ κ = 1*

*} {b} {ab} {c} {a*

*, ,*

Belief functions - Basic concepts

*} {bc} {abc}*

*, , ,*

*− (1/1.6667) = 0.4*

*c} {bc} {abc}*

*, , ,*

Summer 2023 53 / 53
