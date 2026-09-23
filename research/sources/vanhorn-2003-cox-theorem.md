---
title: 'Constructing a logic of plausible inference: a guide to Cox''s theorem'
authors: Kevin S. Van Horn
year: '2003'
url: https://cse.sc.edu/~mgv/csce582sp20/links/vanHorn1.pdf
final_url: https://cse.sc.edu/~mgv/csce582sp20/links/vanHorn1.pdf
retrieved: '2026-09-23'
sha256: 8061d068d08f4f5aa2ab836b7df31d89b9339c61cfaee5bffca91aee88b2ce19
kind: pdf
parser: kaos-pdf
tier: http
engine: curl_cffi
escalated: false
found_by: exa
note: ''
chars: 55621
---

International Journal of Approximate Reasoning 34 (2003) 3–24

www.elsevier.com/locate/ijar

## Constructing a logic of plausible inference: a guide to Coxs theorem



Kevin S. Van Horn

Department of Computer Science and Operations Research, North Dakota State University,

Fargo, ND 58105, USA

Received 1 April 2002; accepted 1 February 2003

Abstract

Coxs theorem provides a theoretical basis for using probability theory as a general



logic of plausible inference. The theorem states that any system for plausible reasoning

that satisfies certain qualitative requirements intended to ensure consistency with clas

sical deductive logic and correspondence with commonsense reasoning is isomorphic to

probability theory. However, the requirements used to obtain this result have been the

subject of much debate. We review Coxs theorem, discussing its requirements, the in



tuition and reasoning behind these, and the most important objections, and finish with

an abbreviated proof of the theorem.

 2003 Elsevier Inc. All rights reserved.

Keywords: Cox; Bayesian; Probability

\1. Introduction

In 1946, Cox wrote a paper \[1\] discussing systems for plausible reasoning,

that is, reasoning about degrees of plausibility, belief, confidence, or credibility.

He proposed a handful of intuitively-appealing, qualitative requirements on

systems of plausible reasoning, and showed that only those systems isomorphic

to probability theory satisfy the requirements. Over the years Cox



s arguments

have been refined by others \[2–5\], making explicit some requirements that

were only implicit in Coxs original presentation, and replacing some of the



E-mail address: kevin.vanhorn@ndsu.nodak.edu (K.S. Van Horn).

0888-613X/$ - see front matter  2003 Elsevier Inc. All rights reserved.

doi:10.1016/S0888-613X(03)00051-3

4 K.S. Van Horn / Internat. J. Approx. Reason. 34 (2003) 3–24

requirements with slightly less demanding (and hence less disputable) as

sumptions than those used in Coxs original proof. We apply the name ‘‘Cox



s

theorem’’ to all of these variants.

Orthodox statistics views probabilities only as long-run frequencies of re

peatable events \[6\], in contrast to Bayesian theory, in which probabilities may

describe degrees of belief \[7\] or states of partial knowledge \[8\] (and hence may

be applied even to nonrepeatable events). From the orthodox, frequentist

standpoint, Bayesians may seem to be misapplying probability theory––after

all, why should one expect rules for manipulating relative frequencies to be at

all appropriate for manipulating degrees of plausibility? Coxs theorem answers



this objection: the rules of probability theory need not be derived from a

definition of probabilities as relative frequencies, but also follow from certain

properties one might desire of any system of plausible reasoning.

This paper may be thought of as a tutorial guide to Coxs theorem. In order to



understand the significance, applicability, and limitations of Coxs theorem, one



must know exactly what requirements are used to obtain the result; thus, we

follow Pariss lead \[4\] in carefully and explicitly laying out the requirements we



use. We go further and devote a major portion of this paper to discussing why

one might find the requirements to be reasonable or desirable, and discussing the

most significant objections to these requirements. We then give an abbreviated

proof of Coxs theorem from our requirements. We omit the proofs of solutions



to functional equations, instead merely referencing where these may be found in

the literature; the emphasis is on how our requirements lead to these equations.

In contrast to previous treatments of Coxs theorem, but following common



working practice among Bayesians, we condition the plausibility of a propo

sition on a state of information, rather than on another proposition. This is

important in motivating the universality requirement of Section 7.

\2. Degrees of plausibility vs. degrees of truth

Our goal is to develop a system of plausible reasoning that extends classical

deductive logic––in particular, the propositional calculus––to deal with prop

ositions that we cannot conclusively prove true nor false. Instead of simply

giving up in such cases and providing no information at all about the truth of

the proposition, our logic should allow us to compute a degree of plausibility

for the proposition. Such plausible reasoning constitutes the vast majority of

the reasoning that we as humans do, since outside of mathematics there is little

that we can declare true or false with complete certainty.

We stress that we are concerned with degrees of plausibility, as opposed to

degrees of truth. Fuzzy logic \[9\] (with the exception of possibility theory \[10\])

and various other multivalued logics deal with the latter, and hence have aims

distinct from ours. Failure to distinguish these distinct concepts has in the past

led to unnecessary controversy \[11\]. On this issue, Dubois and Prade \[12\] write:

K.S. Van Horn / Internat. J. Approx. Reason. 34 (2003) 3–24 5

\[name omitted\] fails to understand the important distinction between

‘‘

...

two totally different problemsThese are the handling of gradual (thus

...

nonBoolean) properties whose satisfaction is a matter of degree (even

when information is complete) on the one hand, and the handling of un

certainty being induced by incomplete states of knowledge

...

Very often, discussions about fuzzy expert systems or uncertain knowl

edge base systems get confused because of a lack of distinction between

degrees of truth and degrees of uncertaintyThis distinction was made

...

by one of the founders of subjective probability theory––De Finetti––but

with few exceptions (including ourselves) it has been quite forgotten by

the AI community in general.’’

As an example, ones confidence in the statement (‘‘Jim is over six feet



P

tall’’), after seeing Jim sitting at a table, is a degree of plausibility. In contrast,

the statement Q (‘‘Jim is tall’’) may be somewhat true (if Jim measures five feet

eleven inches) or entirely true (if Jim measure seven feet even).

Our logic shall be restricted to statements such as P, which are either true or

false, although we may not know which. This does not leave us utterly inca

pable of dealing with statements such as Q. In some cases, we may take

statements involving fuzzy concepts (e.g., ‘‘Jim has a beard’’) and, as an en

gineering approximation, treat them as either entirely true or entirely false. A

more general approach is to recognize that such fuzzy statements usually arise

as human utterances, and to turn them into propositions by stating that

someone uttered them. For example, we may apply plausible reasoning to the

0 00

proposition Q(‘‘Mary said that Jim is tall’’) or Q(‘‘I was told that Jim is

tall’’), rather than to Q itself, with the goal of deriving the plausibility of an

other proposition such as P

.

\3. Preliminary definitions

Before proceeding, let us review some notions from the propositional cal

culus and provide basic definitions we use throughout this paper. A proposition

is an unambiguous statement that is either true or false. A compound propo

sition is constructed from other propositions using the unary operator : (ne

gation) or any of the binary operators ^ (and), \_ (or), ) (implies), or ()

(equivalence). All other propositions are atomic propositions: they cannot be

1

decomposed into other propositions.

1

Atomic propositions may still have some internal structure. For example, we might wish to

consider the atomic proposition x ¼ e for any numeric expression e.

6 K.S. Van Horn / Internat. J. Approx. Reason. 34 (2003) 3–24

Definition 1. A state of information X summarizes the information we have

about some set of atomic propositions A, called the basis of X, and their re

lationships to each other. The domain of X is the logical closure of A, that is,

the union of A and all compound propositions that involve only atomic

propositions from A

.

A state of information is not restricted to containing only deductive infor

mation; it can also contain soft information that says nothing with certainty,

but still affects ones assignment of plausibilities. We do not at this point pin



down exactly what states of information are in a formal sense, but we shall

characterize them axiomatically.

Definition 2. If X is a state of information and A is a proposition in the domain

of X, we write ðAjXÞ for the plausibility we assign to A given the information in

X. We write AX for the state of information obtained from X by adding the

,

additional information that A is true.

Although our notation is reminiscent of the notation of probability theory,

please keep in mind that we are not introducing probability theory at this point.

Note also one difference between the plausibility ðAjXÞ and a conditional

probability PðAjBÞ from classical, frequentist probability theory: B is a prop

osition, while X is a state of information. The comma notation allows us to

write things like ðAjBXÞ, that is, ‘‘the plausibility of A given both X and that B

;

is true.’’

In the sequel we assume that X is a state of information and that ABC and

, ,

D are propositions in the domain of X

.

\4. Representation of plausibility

R1 ðAjXÞ, the plausibility A given X, is a single real number. There exists a real

number T such that ðAjXÞ 6 T for every X and A

.

Since we use real numbers to measure everything from time and distance to

temperature––indeed, to measure any sort of magnitude––it seems quite rea

sonable to measure degrees of plausibility this way. At this point the only

meaning we can assign to these numbers is that higher numbers indicate higher

degrees of plausibility, with T being the plausibility of a known true proposi

tion. One might want to represent truth by þ1, or falsity by 1, but any such

representation of plausibilities can be mapped into a finite interval of the real

number line via a continuous, strictly increasing, invertible transformation––

for example, f ðxÞ¼ arctanðxÞ

.

K.S. Van Horn / Internat. J. Approx. Reason. 34 (2003) 3–24 7

We must mention, however, that R1 is not without controversy. In fact, it is

arguably the most fundamental distinction between the Bayesian and other

approaches to plausible reasoning.

By representing plausibilities with a single real number we implicitly assume

that the plausibilities of any two propositions are comparable. That is, given

any two propositions A and B and a state of information X, either A and B are

equally plausible, or one is more plausible than the other. Some consider this

assumption of universal comparability unwarranted, and have explored weaker

assumptions. Fine \[13\] gives one summary of approaches that do away with

universal comparability, whereas Jaynes \[8, Appendix A\] argues for universal

comparability on pragmatic grounds.

The most common objection to universal comparability is a more funda

mental objection to representing ones degree of certainty or belief in a prop



osition with a single value. In particular, two popular approaches to plausible

inference––belief-function theories \[14,15\] and possibility theory \[10\]––are two

dimensional theories in which ones certainty in a proposition is represented by



a pair of numbers. Such theories unavoidably lack universal comparability.

With regard to belief-function theory, Shafer \[14, p. 42\] writes:

‘‘Ones beliefs about a proposition are not fully described by ones de



A

gree of belief Bel(A(A), for Bel(A(A) does not reveal to what extent one doubts



A––i.e., to what extent one believes its negation A. A fuller description

consists of the degree of belief Bel(A(A) together with the degree of doubt



Dou(A(A) ¼ Bel(A(A).’’

Describing possibility theory, Dubois and Prade \[10, p. 11\] likewise write:

‘‘The possibility (or necessity) of an event, and that of the contrary event,

are but weakly linked; in particular, in order to characterize the uncer

tainty of an event A one needs both of the numbers PðAÞ and NðAÞ.’’

One motivation for using a two-dimensional theory is the concern that a

one-dimensional theory cannot adequately represent ignorance. Belief-function

theories allow one to represent ignorance by allowing one to express a degree

of belief that some one out of a set of possibilities is true, without requiring one

to subdivide this into assignments of belief to the individual possibilities. Re

garding the representation of ignorance with probabilities, Shafer \[14, p. 23, 24\]

writes:

‘‘Are there or are there not living beings in orbit around the star Sirius?

Some scientists may have evidence on this question, but most of us will

profess complete ignorance about it. So if h1 denotes the possibility that

there is such life and hdenotes the possibility that there is not, we will

2

8 K.S. Van Horn / Internat. J. Approx. Reason. 34 (2003) 3–24

adopt the vacuous belief function over the set of possibilities

H ¼fh1h2g

; .

We can also consider the question in the context of a more refined set

of possibilities. We might, for example, raise the question of whether

there even exist planets around Sirius. We would then have a set of pos

sibilities X ¼fnnng, say, where ncorresponds to the possibility that

1; 2; 31

there is life around Sirius, ncorresponds to the possibility that there are

2

planets but no life, and ncorresponds to the possibility that there are not

3

even planets

’’

...

Shafer then points out that if one tries to represent ignorance about the

question by assigning equal probabilities to all the possibilities, one runs into

an inconsistency: the probability of the proposition A that there are living

beings in orbit around Sirius differs depending on whether one examines the set

of possibilities H or the more refined set of possibilities X

.

One response to such concerns is that, in practice, one is never completely

ignorant. One generally has at least some weak information about the prop

ositions of interest. Still, the notion of complete ignorance is useful as a limiting

case, and as an approximation when the available information is so weak as to

not be worth the effort of including it in ones analysis.



A better response is that ‘‘complete ignorance’’ is a slippery concept, and we

need to be careful to state exactly wherein our ignorance lies. Returning to

Shafers example, the set of possibilities , and the assignment of equal



H

probabilities to these, corresponds to a state of information wherein we are

completely ignorant of any factors relevant to A. But the very act of including

000

ninstead of n(life and one or more planets) and n(life but no planets) in the

1 1 1

set of possibilities X reveals that we are not completely ignorant––we are, in

fact, aware that A cannot be true unless there are one or more planets in orbit

about Sirius. Assignment of equal probabilities to the elements of X corre

sponds to a state of information wherein we know that planets are necessary

for life, but that is all we know. There is no inconsistency in arriving at different

probabilities for A when using the two different sets of possibilities, as they

2

represent different states of information.

Can a one-dimensional theory adequately represent ignorance? A reasonable

discussion of this question would take us well beyond the scope of this paper,

but we can make a few comments. Bayesians have not ignored this issue. Jaynes

suggests treating each aspect of ones ignorance as defining a transformation of



the problem that leaves ones state of information invariant, and using this to



derive a probability distribution representing ignorance \[16,17\]. Though quite

2

We believe this response to Shafer originated with E.T. Jaynes, but we have been unable to

track down a specific reference.

K.S. Van Horn / Internat. J. Approx. Reason. 34 (2003) 3–24 9

elegant, this approach does not always yield a unique solution: too few trans

formations can yield multiple candidate distributions, and too many can leave

no solution at all. Kass and Wasserman have written a useful review of tech

niques for constructing probability distributions representing ignorance \[18\].

Their paper illustrates a difficulty Bayesians face in representing ignorance:

there are too many choices available, as the issue is not sufficiently resolved to

allow widespread agreement on the proper solution. On the other hand, the

rapidly growing use of Bayesian methods by working scientists \[19\] suggests that

the issue need not be a serious stumbling block in practice.

Another motivation for two-dimensional theories has been the perception

that proper application of Bayesian methods requires knowledge of the ‘‘true’’

probabilities, which are viewed as physical properties. This can lead to theories

in which one represents uncertainty as a convex set of probability distributions

\[20\]. Jaynes dismisses such concerns about ‘‘true,’’ physical probabilities as

examples of the ‘‘Mind Projection Fallacy’’ \[21\], yet even the Jaynesian view

point admits certain states of information that are mathematically equivalent to

3

being uncertain about some ‘‘physical’’ probability. Bayesians deal with un

certain ‘‘physical’’ probabilities by reasoning about the probabilities of various

physical probability values. This brings us back to the previous concern, rep

resentation of ignorance, and hence this second motivation for considering a

two-dimensional theory reduces to the first.

We close our discussion of R1 with one final, pragmatic argument in

its favor: it is the simplest alternative available. Two-dimensional theories

are unavoidably more complex, and in applications to decision-making

under uncertainty they lack the simple (and widely used) principle of maxi

mizing expected utility. Thus, R1 seems a desirable property for a system of

plausible inference to have, as long as it does not lead to an unsatisfactory

theory.

\5. Compatibility with the propositional calculus

4

Definition 3. We say that A is equivalent to B if ðA () BÞ is a tautology.

Definition 4. We say that X is consistent if there is no proposition A for which

both ðAjXÞ¼ T and ð:AjXÞ¼ T

.

3

Consider repeated draws, with replacement, from an urn full of black balls and white balls,

with the urn thoroughly shaken between draws. Detailed information on the initial positions of the

balls and on the shaking and drawing process would allow us to predict each draw with certainty,

but in the absence of such information the fraction of white balls determines the probability of

drawing a white ball on each turn.

4

A proposition that is true regardless of the truth or falsity of its atomic propositions, e.g.,

ðC \_:CÞ.

10 K.S. Van Horn / Internat. J. Approx. Reason. 34 (2003) 3–24

A state of information is consistent if it does not assert the truth of two

contradictory propositions. :A:AAX is an example of an inconsistent state of

; ;

information.

R2 Plausibility assignments are compatible with the propositional calculus:

ðjÞ¼ðjÞ

0 0

(1) If A is equivalent to Athen AXAX

.

(2) If A is a tautology then ðAjXÞ¼ T

.

(3) ðAjBCXÞ¼ðAjðB ^ CÞXÞ

; ; ; .

(4) If X is consistent and ð:A:AjXÞ \< T, then AX is also consistent.

,

Let us consider why one might desire each of the above requirements in

turn:

5

(1) If A and B are equivalent, we should be able to use them interchangeably.

(2) In accordance with the propositional calculus, any tautology is known

true, hence our plausibility assignment should reflect this.

(3) If we know that B is true, and we also know that C is true, then we know

that B ^ C is true. Likewise, if we know that B ^ C is true, we know that B

and C individually are true.

(4) If we cannot say with certainty that :A :A is true, then there remains a possi

bility that A is true, thus A must not contradict the information we have.

Pariss treatment of Coxs theorem has no equivalent to the last two re



quirements above. This is because he does not make states of information

explicit. What we write as ðAjBXÞ, Paris writes as Bel(A(AjB), with X implicit.

;

What we write as ðAjXÞ, Paris would write as Bel(A(AjB) for some tautology B

.

We have chosen to make states of information explicit and axiomatize them, as

this helps to make clear the rationale for the universality requirement we give

below. Furthermore, making states of information explicit is of great practical

use in avoiding errors arising from unwitting use of different states of infor

mation in different parts of an analysis.

\6. Negation

R3 There exists a nonincreasing function S0 S0 such that ð:A:AjXÞ¼ S0S0ðAjXÞ for

all A and consistent X

.

A and :A :A are just flip sides of the same question. For the propositional

calculus, there is a simple functional relation between the truth values of A and

:A:A: if we know that one is true, then we know that the other is false. Thus it

may seem natural to extend this to a functional relation between ðAjXÞ and

ð:A:AjXÞ

.

5

Recall that equivalence here means only that ðA () () BÞ is a tautology, which is a decidable

question.

K.S. Van Horn / Internat. J. Approx. Reason. 34 (2003) 3–24 11

If, to the contrary, we allow ðAjXÞ and ð:A:AjXÞ to vary independently of each

other, then we effectively have a two-dimensional theory, as we need two

numbers to completely characterize our uncertainty about A \[10, p. 11, 14, p.

42\]. Thus we see that R3 goes hand in hand with R1 \[22\], and all of the ar

guments we have presented for or against the latter also apply to the former.

R3 also states that S0 S0 is nonincreasing, i.e., if ðAjXÞ \< ðAjY Þ then

S0S0ðAjXÞ P S0S0ðAjY Þ. This just states that if we become more certain that A is true

(our state of information changes from X to Y ), we should not also become

more certain that is false. We note that Coxs original proof has no explicit



A

requirement that S0 S0 be nonincreasing, instead requiring that it be twice dif

6

ferentiable; however, a close examination of the appendix of Cox



s paper

reveals that his proof implicitly requires S0 S0 to be either strictly increasing or

ððÞ Þ

0

strictly decreasing S
0x6¼ 6¼ 0

S
0.

The following are immediate consequences of these first requirements:

Proposition 1. Define F ¼ S0S0ðTÞ. Then F 6 ðAjXÞ 6 T for all A and consistent X

.

Proof. ðAjXÞ¼ S0S0ð:A:AjXÞ PS0S0ðTÞ

.

Proposition 2. If X is consistent and x ¼ðAjXÞ then x ¼ S0S0ðS0S0ðxÞÞ

.

Proof. x ¼ ð::AjXÞ¼ S0S0ðS0S0ðAjXÞÞ

.

\7. Universality

R4 There exists a nonempty set of real numbers P0 with the following two

properties:

• P0 is a dense subset of ðFTÞ. That is, for every pair of real numbers ab such

;,

that F 6 a \< b 6 T, there exists some c 2 Psuch that a \< c \< b

0 .

• For every 2 Pthere exists some consistent X with a basis of at least

y1; y2y2; y3 y3 0

three atomic propositions––call them A1A2 and A3––such that ðA1jXÞ¼ y1

, ,

ðA2jA1XÞ¼ y2 y2 and ðA3jA2A1XÞ¼ y3y3

; ; ; .

To understand the motivation for R4, recall the purpose of this enterprise:

to construct a universal system or logic of plausible reasoning, intended as an

extension of the propositional calculus. Since the propositional calculus is

applicable to any problem domain for which we can formulate useful pro

positions, the same should be true for our logic of plausible reasoning; in

6

Actually, instead of our S0 S0 Cox postulates a function s such that wð:A:AjXÞ¼ sðwðAjXÞÞ (we

define w in Section 10). Given our requirements w is continuous and strictly increasing, so the two

approaches are equivalent, but the distinction becomes important if we relax the strictness

requirement on F of Section 10 \[23\].

12 K.S. Van Horn / Internat. J. Approx. Reason. 34 (2003) 3–24

particular, the least we can ask is that our logic of plausible reasoning be ca

pable of handling a case where we have three completely unrelated atomic

propositions with arbitrary plausibilities.

R4 requires a bit less than that. First of all, we do not require our logic to

handle completely arbitrary plausibilities. We allow for the possibility that

certain real numbers in the range ½FT simply are not allowed as plausibilities.

;

For example, we could restrict ourselves to rational values. However, we do

require that the set P0 of allowed plausibility values be dense. We want our

theory to have no holes, no entire intervals of forbidden plausibility values, as

this would unduly restrict its applicability.

Secondly, if the propositions Aare completely unrelated, then knowing that

i

one of the propositions is true should not change the plausibility of the others;

that is, we would expect that ðA2jA1XÞ¼ðA2jXÞðA3jA2A1XÞ¼ðA3jA1XÞ¼

; , ; ; ;

ðA3jXÞ, etc. We have not required this, but R4 is consistent with such an in

terpretation, for it is satisfied by first choosing arbitrary values for the various

ðAijXÞ, then using the above equalities.

R4 is not without controversy. Paris \[4\] highlights its crucial importance in

his proof of Coxs theorem, and Halpern \[24\] shows that omitting R4 allows



one to construct an explicit counterexample to Coxs theorem. Halpern goes



further to argue that R4 is unreasonable for finite domains (those with only a

finite set of atomic propositions). Following Cox, Halpern conditions on

propositions rather than states of information, and he writes W for the set of

pairs of propositions ðABÞ (corresponding to plausibility expression ðAjBÞ)

;

constructed from the set of atomic propositions, with equivalent propositions

considered equal. He writes \[25\]:

‘‘The problematic assumption here is \[R4\]\[T\]o satisfy \[R4\], W must be

...

infinite; \[R4\] cannot be satisfied in finite domains. While naturaland



reasonableare, of course, in the eye of the beholder, it does not strike



me as a natural or reasonable assumption in any obvious sense of the

words. This is particularly true since many domains of interest in AI

(and other application areas) are finite; any version of Coxs theorem that



uses \[R4\] is simply not applicable in these domains.’’

Halpern does mention that one might require R4 because one desires a set of

rules that apply to arbitrary domains, but then dismisses this motivation be

cause it ‘‘does not allow a notion of belief that has only finitely many grada

tions’’ \[24,25\]. (Why one might desire to have only finitely many gradations he

does not say.) One may argue to the contrary that any logic of plausible rea

soning applicable to only a single domain is of little value. We (humanity)

would have found it difficult to make any significant progress in mathematics if

we had been required to come up with new rules of logic for every new domain

we wished to investigate. It is the very fact that we have identified widely

K.S. Van Horn / Internat. J. Approx. Reason. 34 (2003) 3–24 13

7

applicable rules of logic, to be used in nearly every domain, that allows us to

reason with confidence when entering new conceptual territory.

Still, let us consider doing as Halpern proposes, and restrict ourselves to one

finite set of atomic propositions A used in one problem domain. Halpern notes

that W is then finite, and hence the set of plausibility values ðAjBÞ is also finite;

but the traditional notation ðAjBÞ, with A and B both propositions, hides a

dependence on ones prior state of information . Using the notation of this



X

paper, the set of possible plausibility values are all values ðAjBXÞ, where X

;

may range over any allowed state of information whose basis is A. Thus, the

set of possible plausibility values is finite only if, in addition to restricting

ourselves to a single, finite problem domain, we also restrict ourselves to a finite

set of possible states of information for that problem domain.

Snow \[28\] argues against such a restriction and for infinite gradations of

plausibility within even a single, finite domain:

‘‘It often happens that sentences of interest include some that describe

events for which there is an objectiveprobability



...

The source of an objective rational measure of belief is external to the

cognitive apparatus of the believer. Its value is determined by the vagaries

of the real world or by some idealized model of that world. There is no

way to tell in advance just which values might arise, and each value

may be graduated with arbitrary precision. Any such value can simply

be adopted by the believer without recourse to unboundedly precise dis

crimination between affective states related to credibility

’’

...

For example, consider the proposition A that a particular atom of a ra

dioactive isotope will decay within a particular time period. The plausibility

that we assign A will depend on what we determine the half-life of the isotope

to be, and has a continuum of potential values before the measurement is

made.

Let us examine a variant of an example that Snow gives, illustrating a

continuum of plausibility values arising from different states of information for

the same problem domain, but not relying on any notion of ‘‘physical’’

probabilities. Suppose we have a problem in a finite domain involving a

proposition B whose meaning is ‘‘point p lies on the vertical leg of right triangle

T .’’ Let XðxyÞ denote a state of information in which the only thing we know

;

about the location of is that it lies on the perimeter of T , which has width

p x

and height y. It seems reasonable to assign ðBjXðxyÞÞ a value near F if y  x,a

;

7

The predicate calculus (plus the axioms of set theory) seems to be adequate for almost all of

mathematics and science. Many feel it is inadequate for certain domains, however, and have

proposed various alternatives \[26,27\].

14 K.S. Van Horn / Internat. J. Approx. Reason. 34 (2003) 3–24

value near T if y  x, and that ðAjXðxyÞÞ should increase smoothly as y=x

;

increases from 0 to infinity.

Arnborg and Sjdin have investigated an alternative form of Cox s theorem

€ 

o

that does not rely on universality, but instead uses notions of noninformative

refinability and information independence for finite domains \[29,30\]. Other

differences include replacing R3 with a requirement that ðA \_ BjXÞ, where A

and B are exclusive, be a strictly increasing function of ðAjXÞ and ðBjXÞ

.

One trivial consequence of adding R4 is that our logic does not collapse to a

single possible plausibility value:

Proposition 3. F \< T

.

Proof. Follows from the fact that P0 is nonempty. 

*\8. Properties of S0S0*

Our requirements to this point imply some additional properties for the

function S0

S0.

Lemma 4. There exists a continuous, strictly decreasing function

S1 : ½FT!½FT such that S1ðAjXÞ¼ S0S0ðAjXÞ ¼ ð:AjXÞ for all A and consis

;;

tent X

.

Proof. Let P1 be the set of all possible plausibility values ðAjXÞ, where X is

consistent, and restrict the domain of S0 S0 to P1. If x1x2 2 P1 and S0S0ðx1Þ¼

;

S0S0ðx2Þ¼ y, then x1 ¼ S0S0ðyÞ¼ x2; hence S0 S0 is one-to-one, and therefore strictly

decreasing. Proposition 2 tells us that P1 is the range of S0S0; combined with the

facts that P1 is a dense subset of ½FT and S0 S0 is nonincreasing, this implies that

;

S0 S0 is continuous (any discontinuity would produce a gap in the range of S0S0.)

The lemma is then proved by defining S1ðxÞ¼ limyS0S0ðyÞ

my!x .

Paris \[4\] shows that, if we strengthen R4 to require that P0 ¼½FT, then we

;

can dispense with the requirement that S0 S0 be nonincreasing, as we can derive

this property from the other requirements.

\9. Conjunction

2

R5 There exists a continuous function F : ½FT!½FT, strictly increasing

;;

2

in both arguments on ðFT, such that ðA ^ BjXÞ¼ F ððAjBXÞðBjXÞÞ for any A

;; ;,

B and consistent X

.

K.S. Van Horn / Internat. J. Approx. Reason. 34 (2003) 3–24 15

Let us first examine why it might be reasonable to require ðA ^ BjXÞ to be a

function of ðBjXÞ and ðAjBXÞ only. The obvious candidates on which

;

ðA ^ BjXÞ might depend are ðAjXÞðBjXÞðAjBXÞ, and ðBjAXÞ. There are 15

, , ; ;

different subsets of these four values from which we might compute ðA ^ BjXÞ;

however, A ^ B is equivalent to B ^ A, and this symmetry reduces the number

of distinct candidates to nine. In a similar fashion as Tribus \[5\], we try to rule

out as many of these nine candidates as we can:

(1) ðA ^ BjXÞ¼ F ðAjXÞ. Suppose that A is a tautology and B any atomic prop

osition. Then A ^ B is equivalent to B, and ðAjXÞ¼ T, so F ðTÞ¼ðBjXÞ

.

But we can choose X so as to make ðBjXÞ be any desired value in the infi

nite set P, so we have a contradiction.

0

(2) ðA ^ BjXÞ¼ F ðAjBXÞ. Suppose that A and B are the same atomic propo

;

sition. Then ðA ^ BjXÞ¼ðAjXÞ and common sense dictates that ðAjBXÞ¼

;

T, hence F ðTÞ¼ðAjXÞ, yielding a contradiction.

(3) ðA ^ BjXÞ¼ F ððAjXÞðAjBXÞÞ. Suppose that A is a tautology and B any

;;

atomic proposition. Then F ðTTÞ¼ðBjXÞ, yielding a contradiction.

;

(4) ðA ^ BjXÞ¼ F ððAjBXÞðBjAXÞÞ. Suppose that A and B are the same

; ;;

atomic proposition. Common sense dictates that ðAjBXÞ¼ðBjAXÞ¼ T

; ; ,

so F ðTTÞ¼ðAjXÞ, yielding a contradiction.

;

(5) ðA ^ BjXÞ¼ F ððAjXÞðBjXÞÞ. Let A be any atomic proposition and let B be

;

:A. Then F ¼ F ððAjXÞS1ðAjXÞÞ, hence F ðxS1ðxÞÞ ¼ F for all x 2 P0. If in

; ;

stead A and B are the same atomic proposition, we obtain F ðxxÞ¼ x for all

;

x 2 P0. These equalities lead to the following three undesirable conse

quences:

(a) F must be discontinuous. To see this, assume that F is continuous. Then

F ðxS1ðxÞÞ ¼ F for all x 2½FT and F ðxxÞ¼ x for all x 2½FT. Since

; ;; ;

S1 is a continuous and strictly decreasing function whose domain and

range are both ½FT, it has a fixed point in the interior of this range;

;

that is, there exists some F \< x0 \< T such that x0 ¼ S1ðx0Þ. Then

x0 ¼ F ðx0x0Þ¼ F ðx0S1ðx0ÞÞ ¼ F, which contradicts x0 > F

; ; .

(b) It is not allowed for a proposition and its negation to be equally plausible.

For if x ¼ðAjXÞ ¼ ð:AjXÞ, we have x ¼ F ðxxÞ¼ F ðxS1ðxÞÞ ¼ F and

; ;

so x ¼ S1ðxÞ¼ F; but S1ðFÞ¼ F is not possible, since S1 is strictly de

creasing and its range is ½FT

;.

(c) There are plausibility values xy > F such that F ðxyÞ¼ F. This is unde

, ;

sirable because it means that if ðAjXÞ¼ x and ðBjXÞ¼ y, then ðA ^ BjXÞ

must be known false with absolute certainty, even when A and B are en

tirely unrelated propositions, each individually possible. This conse

quence arises as follows. Choose any arbitrary x 2 P0 and define

y ¼ S1ðxÞ. Since S1ðTÞ¼ F and S1 is strictly decreasing, we have

y > F. Then F ðxyÞ¼ F ðxS1ðxÞÞ ¼ F

; ; .

We are left with the following possibilities:

(1) ðA ^ BjXÞ¼ F ððAjBXÞðBjXÞÞ

; ;.

16 K.S. Van Horn / Internat. J. Approx. Reason. 34 (2003) 3–24

(2) ðA ^ BjXÞ¼ F ððAjBXÞðBjXÞðAjXÞÞ

; ;;.

(3) ðA ^ BjXÞ¼ F ððAjBXÞðBjXÞðBjAXÞÞ

; ;;; .

(4) ðA ^ BjXÞ¼ F ððAjBXÞðBjXÞðBjAXÞðAjXÞÞ

; ;;; ;.

Tribus claims to rule out (3) and (4) by showing that for these candidates

one cannot avoid dealing with plausibility expressions that involve some in

consistent state of information Y , and hence there is unavoidable ambiguity.

We find this argument unconvincing, as there is no problem with simply

picking an arbitrary value for ðAjY Þ when Y is inconsistent. From deductive

logic we know that one can prove anything from inconsistent premises, and so

there is even a good argument for defining ðAjY Þ¼ T for all propositions A and

inconsistent Y . Tribus also claims that one can rule out (2), but leaves this as an

exercise for the student.

At this point we have to admit that there is no completely compelling reason

for choosing any particular one of the four remaining candidates. However, (1)

seems intuitively appealing to many people (it has not engendered any con

troversy of which we are aware); furthermore, the other candidates merely add

additional arguments to those used in (1)––whatever we decide, we are going to

need at least ðBjXÞ and ðAjBXÞ––and the simpler candidate is to be preferred,

;

all else being equal.

Jaynes \[8, Chapter 2\] gives the following intuitive rationale for (1):

‘‘In order for A ^ B to be a true proposition, it is necessary that B is true.

Thus the plausibility ðBjXÞ should be involved. In addition, if B is true, it

is further necessary that A should be true; so the plausibility of ðAjBXÞ is

;

also needed. But if B is false, then of course A ^ B is false independently

of whatever one knows about A, as expressed by ðAj:BXÞ; if the robot

;

reasons first about B, then the plausibility of A will be relevant only if

B is true. Thus, if the robot has ðBjXÞ and ðAjBXÞ it will not need

;

ðAjXÞ. That would tell it nothing about A ^ B that it did not have al

ready.’’

(We have replaced Jayness notation with our own in the above quote.)



Let us now consider the remaining requirements on F

.

• F must be strictly increasing. Suppose that our state of information changes

so as to make either B more plausible or make A (assuming B) more plausi

ble, while leaving the other no less plausible. Surely A ^ B must not become

less plausible in this case. It accords with many peoples intuition that



A ^ B

must, in fact, be considered more plausible in this case, but there are others

who disagree with this stronger requirement.

F must be continuous. If ones state of information changes so that either



• B

becomes infinitesimally more plausible, or A (assuming B) becomes infinites

imally more plausible, many would find it quite unnatural and counterintu

itive for the plausibility of A ^ B to suddenly jump.

K.S. Van Horn / Internat. J. Approx. Reason. 34 (2003) 3–24 17

Coxs 1946 paper does not explicitly require that be strictly increasing,



F

instead requiring that it be twice differentiable; however, a careful examination

of the appendix to his paper reveals that the proof implicitly assumes F to be

either strictly increasing in both arguments or strictly decreasing in both ar

2

guments on ðFT

;.

It is possible to slightly weaken our requirements on F without losing our

main result (that our system must be isomorphic to probability theory) \[31\].

Unfortunately, we cannot get by with requirements nearly as weak as those on

S0S0. In particular, the requirement that F be strictly increasing is essential; if we

relax this to a requirement that F be merely nondecreasing, then F ðxyÞ¼

;

minðxyÞ is consistent with our requirements \[22,23\], giving us a system not

;

isomorphic to probability theory.

\10. The product rule

We have now presented all of the requirements we impose on our system of

plausible reasoning. We now proceed to show that those requirements force

our system of plausible reasoning to be isomorphic to probability theory,

giving us the Bayesian approach to plausible reasoning. Our proof borrows

from Jaynes \[3\] and Paris \[4\].

We begin by deriving some properties of F . The simple fact that ‘‘^’’ is

associative turns out to have great ramifications. It ensures that F is associa

tive, which in turn limits the possibilities for F to functions that are isomorphic

to multiplication.

Lemma 5. F ðxF ðyzÞÞ ¼ F ðF ðxyÞzÞ for all xyz 2½FT

; ;; ;, , ;.

Proof. Let us consider ðA ^ B ^ CjXÞ, where X is consistent. Applying R5 and

R2, we obtain

ðA ^ðB ^ CÞjXÞ¼ F ½ðAjðB ^ CÞXÞðB ^ CjXÞ

; ;

¼ F ½ðAjBCXÞF ½ðBjCXÞðCjXÞ

; ; ; ; ;

Using an alternate grouping, we obtain

ððA ^ BÞ^ CjXÞ¼ F ½ðA ^ BjCXÞðCjXÞ

; ;

¼ F ½F ½F ½ðAjBCXÞðBjCXÞðCjXÞ

; ; ;; ;

But A ^ðB ^ CÞ is equivalent to ðA ^ BÞ^ C, so equating the two plausibilities

above and applying R4 yields

F ðxF ðyzÞÞ ¼ F ðF ðxyÞzÞ

; ;; ;

18 K.S. Van Horn / Internat. J. Approx. Reason. 34 (2003) 3–24

for all x2 P. Since F is continuous and Pis dense, the equation holds for

, y, z 00

all xyz 2½FT

, , ;.

The functional equation we have obtained for F is one with a long history

extending back to the early 19th century. Here is its solution.



Lemma 6 (Aczel). Let a and b, with a \< b, be real numbers. Suppose that

2

f : ðab!ðab is a continuous function, strictly increasing in both arguments,

; ;

and satisfies the associativity equation

f ðxf ðyzÞÞ ¼ f ðf ðf ðxyÞzÞ

; ;; ;

for all xyz 2ðab. Then there exists some continuous, strictly increasing

, , ;

function g such that

gðf ðf ðxyÞÞ ¼ gðxÞþ gðyÞ

;

for all xy 2ðab

, ; .



This theorem is found on p. 256 of Aczls book \[2\], in a slightly different



Proof. e

and more general form. 

We now obtain the familiar product rule from probability theory.

Lemma 7. There exists a continuous, strictly increasing, nonnegative function w

such that

wðA ^ BjXÞ¼ wðAjBXÞwðBjXÞ

;

for every AB and consistent X

, .

Proof. R5 and Lemma 5 allow us to apply Lemma 6, with f ¼ F a ¼ F, and

,

b ¼ T. Define wðxÞ¼ expðgðxÞÞ; then wðF ðxyÞÞ ¼ wðxÞwðyÞ for xy 2ðFT

; , ;.

Since w is increasing, continuous, and nonnegative on ðFT, limxF wðxÞ exists

;mx!

and is nonnegative. Defining wðFÞ to be this limit makes w increasing, con

tinuous, and nonnegative on ½FT. By continuity of w and F , we then have

;

wðF ðxyÞÞ ¼ wðxÞwðyÞ for xy 2½FT, and combined with R5 this gives us the

; , ;

lemma. 

The function w rescales plausibilities to what one might call ‘‘proto-prob

abilities’’. Lemma 7 states that proto-probabilities obey the product rule of

probability theory. The next lemma states that proto-probabilities have the

same range of values, and represent truth and falsity in the same way, as

probabilities.

Lemma 8. wðFÞ¼ 0wðTÞ¼ 1, and 0 \< wðxÞ \< 1 for F \< x \< T

, .

K.S. Van Horn / Internat. J. Approx. Reason. 34 (2003) 3–24 19

Proof. For x > F we have wðxÞ > wðFÞ P 0. Choose any A, tautology D, and

consistent X with ðAjXÞ > F; then

wðAjXÞ¼ wðD ^ AjXÞ¼ wðDjAXÞwðAjXÞ¼ wðTÞwðAjXÞ

; :

Dividing both sides of the above equation by wðAjXÞ gives wðTÞ¼ 1, and hence

wðxÞ \< 1 for x \< T

.

ffi
z p

ffiffip

Suppose that wðFÞ¼ z > 0. Then 0 \< z \< 1, hence z \< z p \< 1. Choose A1

,

11

ffi
z p

ffiffip

A, consistent X, and Psuch that ðÞ ð Þ and ðAjXÞ¼



2x 2 0 wz\< x \< wz p 1

ðA2jA1XÞ¼ x. Then

;

2

wðA1 ^ A2jXÞ¼ wðxÞ\< z ¼ wðFÞ

and hence ðA1 ^ A2jXÞ \< F, a contradiction. So wðFÞ¼ 0. 

\11. The sum rule

Having established that F must amount to multiplication under the map

ping from plausibilities to proto-probabilities, we now investigate what form S1

must take. We begin by using w to construct what will turn out to be a mapping

from plausibilities to probabilities, and examine the behavior of S1 under this

mapping.

1

Definition 5. We define SðÞ to be ðSðpðÞÞÞ, where



xp1ðpx

r

• pðxÞ¼ wðxÞ

,

• r ¼ ðlog 2Þ=ðlog wðaÞÞ, and

• a is the unique fixed point of S1, i.e., S1ðaÞ¼ a and F \< a \< T

.

1

Lemma 9. is well defined and p has the following properties:



p

(1) p is continuous and strictly increasing.

(2) pðFÞ¼ 0pðTÞ¼ 1, and 0 \< pðxÞ \< 1 for F \< x \< T

, .

(3) pðA ^ BjXÞ¼ pðAjBXÞpðBjXÞ for all AB, and consistent X

; , .

S is also well defined, and Sð1=2Þ¼ 1=2

.

Proof. S1 has a fixed point because it is continuous and maps the interval ½FT

;

onto itself. The fixed point is unique because S1 is strictly decreasing, hence a is

well defined and F \< a \< T. Then 0 \< wðaÞ \< 1, and so 1 \< log wðaÞ \< 0.

This furthermore implies that 0 \< r \< 1. Combined with the continuity and

strictness of w, this gives (1). Item (2) follows from the facts that r > 0 and w

r

has the same properties. Item (3) follows from ðabÞbfor all b, and the

rr

¼ aa

,

corresponding property for w. Item (1) implies that p is one-to-one, hence the

1

inverse is well defined.

p

20 K.S. Van Horn / Internat. J. Approx. Reason. 34 (2003) 3–24

r

Substituting in the definition of r gives pðaÞ¼ wðaÞ¼ 1=2. Hence,

1

Sð1=2Þ¼ ðSðpð1=2ÞÞÞ ¼ ðSðÞÞ ¼ ðÞ¼ 1=2



p1ðpp1apa:

We now restate R3, R4, and Proposition 2 in terms of p and S

.

Proposition 10. The following are true:

• pð:A:AjXÞ¼ SðpðpðAjXÞÞ for every A and consistent X

.

• S is continuous and strictly decreasing.

• Let P ¼ pðP0Þ. Then P is a dense subset of (0,1), and for every y1y2y2y3 y3 2 P

; ;

there exists some consistent X with a basis of three atomic propositions––call

them A1A2 and A3––such that pðA1jXÞ¼ y1pðA2jA1XÞ¼ y2 y2 and pðA3jA2

, , ; ;

A1XÞ¼ y3y3

; .

• SðSðxÞÞ ¼ x for all 0 6 x 6 1

.

Proof. These follow straightforwardly from our previous results. 

As with F , we now derive a functional equation for S from purely logical

considerations.

Lemma 11. For all 0 \< x 6 y \< 1ySðx=yÞ¼ SðxÞSðSðyÞ=SðxÞÞ

, .

Proof. For any uy 2 P we can find propositions A and B and a consistent X

,

such that y ¼ pðBjXÞ and u ¼ pðAjBXÞ. Let x ¼ uy ¼ pðA ^ BjXÞ. Note that

;

0 \< x\< 1. Then

, y, u

ySðx=yÞ¼ ySðuÞ¼ pðBjXÞpð:A:AjBXÞ¼ pð:A :A ^ BjXÞ

; :

Define C  ð:A \_:BÞ and D ðA \_:BÞ. Since :B is equivalent to D ^ C, we

have

SðyÞ¼ pðD ^ CjXÞ

SðxÞ¼ pðCjXÞ:

These last two equalities then give

# SðyÞ
SðxÞ
 pðD ^ CjXÞ
pðCjXÞ


SðyÞpðD ^ CjXÞ

SðxÞS ¼ SðxÞS ¼ SðxÞSðpðpðDjCXÞÞ

;

SðxÞpðCjXÞ

¼ pðCjXÞpð:DjCXÞ¼ pð:D ^ CjXÞ¼ pð:A ^ BjXÞ

;

¼ ySðx=yÞ:

The third step relies on the fact that pð:CjXÞ¼ x \< 1 and hence CX is

,

consistent (R2.4). Since P is dense and S is continuous, the equality then holds

for all 0 \< \< 1 and 0 \< 6 1, hence for all 0 \< 6 \< 1. 

y u x y

K.S. Van Horn / Internat. J. Approx. Reason. 34 (2003) 3–24 21

Lemma 12. Let s : ½01!½01 be a strictly decreasing and continuous function,

; ;

with sð0Þ¼ 1sð1Þ¼ 0, and sð1=2Þ¼ 1=2. If s satisfies both of the functional

,

equations

• sðsðxÞÞ ¼ x

,

• ysðx=yÞ¼ sðxÞsðsðyðyÞ=sðxÞÞ

for all 0 \< x 6 y \< 1, then sðxÞ¼ 1  x for all 0 6 x 6 1

.

Proof. Lemmas 3.10 through 3.15 of Paris \[4\] amount to a proof of this as

sertion. 

We now obtain the sum rule of probability theory:

Lemma 13. pð:AjXÞ¼ 1  pðAjXÞ for all A and consistent X

.

Proof. Follows directly from Lemmas 9, 11, 12, and Proposition 10. 

\12. Probability theory

We can now summarize all of these results into one theorem that states that

our plausibilities must obey the rules of probability theory after mapping by

the function

p.

Theorem 14. There exists a continuous, strictly increasing function p such that,

for every AB and consistent X

, ,

(1) pðAjXÞ¼ 0 iff A is known to be false given the information in X

.

(2) pðAjXÞ¼ 1 iff A is known to be true given the information in X

.

(3) 0 6 pðAjXÞ 6 1.

(4) pðA ^ BjXÞ¼ pðAjXÞpðBjAXÞ

; .

(5) pð:A:AjXÞ¼ 1  pðAjXÞ if X is consistent.

Items 1–5 of Theorem 14 are just the basic rules of probability theory. Since

p is invertible we lose no information by working with probabilities only in

stead of the original plausibilities; thus, any system of plausible reasoning that

is not isomorphic to probability theory must necessarily violate one of the

requirements we have presented. But how do we know that our requirements

are not contradictory? How do we know that there is any system of plausible

reasoning (that is, choice for FTF S0S0P0ðjÞ, and definition of a state of

, , , , ,

information) that satisfies all of our requirements? The set-theoretical ap

proach to probability theory may be taken as an existence proof that our re

quirements are not contradictory, by taking states of information to be

probability distributions, and defining AX to be the probability distribution

,

obtained from X by conditioning on the set of values for which A is true. In the

which Jaynes applies transformation invariance arguments \[16\] and the principle of maximum

Assignment of the prior probabilities from which inference proceeds is a separate issue, to

\[1\] R.T. Cox, Probability, frequency and reasonable expectation, American Journal of Physics 17

s original paper, allows linear possibility distributions

proposes a set of requirements that necessarily lead to belief-function theory

Other requirements may be proposed, leading to different results. Smets

portant area of disagreement is perhaps over R1/R3: whether a single number

mains disagreement as to the desirability of several of them. The most im

make a compelling case for all of these requirements, however, and there re

requirements allow only systems isomorphic to probability theory. We cannot

reasoning that many find intuitively appealing, and have shown how these

We have discussed a set of qualitative requirements on systems of plausible

set-theoretical probability theory so as to make these rules true, and hence the

proven from inconsistent premises. Conditional probabilities can be defined in

analogous to the result from the propositional calculus that anything can be

0’’ from the statements of theorems. These rules are

Adding these rules often allows us to drop requirements such as ‘‘X

Finally, we note that it is convenient, but not necessary, to extend R2 to

of results for finite domains \[8, Chapters 2, 15, and Appendix B\].

for continuous domains are accepted only when they are the well-defined limit

(what amounts to) R2, rejecting any result not derivable from these.

s approach to Bayesian inference is built entirely on Theorem 14 and

sistent sets of axioms (plausibility assignments from which we derive other

comes the model theory for our logic, a tool to enable us to construct con

terminology of mathematical logic, set-theoretical probability theory then be

22

plausibilities).



Jaynes

include the following:

• If X is inconsistent then ðAjXÞ¼ T

.

• If ðBjXÞ¼ F then ðAjBXÞ¼ T

; .

consistent’’ or ‘‘ppðBjXÞ >

extended axiom set remains consistent.

\13. Conclusion

suffices to completely specify ones uncertainty in a proposition.



\[33,34\]. Relaxing the strictness requirement on F , combined with a relaxation

of R3 in the spirit of Cox



\[23\].

References

(1946) 1–13.

8

entropy \[32\].

8

Results

‘X is

K.S. Van Horn / Internat. J. Approx. Reason. 34 (2003) 3–24

K.S. Van Horn / Internat. J. Approx. Reason. 34 (2003) 3–24 23



\[2\] J. Aczel, Lectures on Functional Equations and their Applications, Academic Press, 1996.

\[3\] E.T. Jaynes, How does the brain do plausible reasoning, Tech. Rep. 421, Stanford University

Microwave Laboratory, reprinted in \[35\], 1957, pp. 1–23.

\[4\] J.B. Paris, The Uncertain Reasoners Companion: a Mathematical Perspective, Cambridge



University Press, 1994.

\[5\] M. Tribus, Rational Descriptions, Decisions and Designs, Pergamon Press, 1969.

\[6\] W. Feller, An Introduction to Probability Theory and its Applications, John Wiley & Sons,

1950.

\[7\] J.M. Bernardo, A.F.M. Smith, Bayesian Theory, John Wiley & Sons, 1994.

\[8\] E.T. Jaynes, Probability Theory: the Logic of Science, Cambridge University Press,

Cambridge, 2003 (edited by G.L. Bretthorst).

\[9\] L.A. Zadeh, G.J. Klir, B. Yuan, Fuzzy Sets, Fuzzy Logic, and Fuzzy Systems: Selected Papers

by Lofti A. Zadeh, in: Advances in Fuzzy Systems––Applications and Theory, World Scientific

Publishing Company, 1996.

\[10\] D. Dubois, H. Prade, Possibility Theory: an Approach to Computerized Processing of

Uncertainty, Plenum Press, 1988.

\[11\] C. Elkan, The paradoxical success of fuzzy logic, IEEE Expert 9 (4) (1994) 3–8.

\[12\] D. Dubois, H. Prade, Partial truth is not uncertainty: fuzzy logic versus possibilistic logic,

IEEE Expert 9 (4) (1994) 15–19.

\[13\] T.L. Fine, Theories of Probability, Academic Press, 1973.

\[14\] G. Shafer, A Mathematical Theory of Evidence, Princeton University Press, 1976.

\[15\] P. Smets, The transferable belief model and other interpretations of Dempster-Shafers model,



in: P.P. Bonissone, M. Henrion, L.N. Kanal, J.F. Lemmer (Eds.), Uncertainty in Artificial

Intelligence, vol. 6, Elsevier Science Publishers, 1991, pp. 375–383.

\[16\] E.T. Jaynes, Prior probabilities, IEEE Transactions on System Science and Cybernetics SSC-4

(1968) 227–241, reprinted in \[36\], pp. 114–130.

\[17\] E.T. Jaynes, The well-posed problem, Foundations of Physics 3 (1973) 477–493, reprinted in

\[36\], pp. 131–148.

\[18\] R.E. Kass, L. Wasserman, Formal rules for selecting prior distributions: a review and

annotated bibliography, Tech. Rep. 583, Department. of Statistics, Carnegie-Mellon Univer

sity, available at http://www.stat.cmu.edu/www/cmu-stats/tr/, 1993.

\[19\] D. Malakoff, Bayes offers a to make sense of numbers, Science 286 (1999) 1460–



new way

1464.

\[20\] H.E. Kyburg Jr., Bayesian and non-Bayesian evidential updating, Artificial Intelligence 31

(1987) 271–293.

\[21\] E.T. Jaynes, Probability theory as logic, in: P.F. Fougere (Ed.), Proceedings, Maximum

Entropy and Bayesian Methods, Kluwer Academic Publishers, 1990, also available in a

substantially revised and extended form at http://bayes.wustl.edu/etj/node1.html.

\[22\] D. Dubois, H. Prade, The logical view of conditioning and its application to possibility and

evidence theories, International Journal of Approximate Reasoning 4 (1) (1990) 23–46.

\[23\] P. Snow, The reasonableness of possibility from the perspective of Cox, Computational

Intelligence 17 (1) (2001) 178–192.

\[24\] J.Y. Halpern, A counterexample to theorems of Cox and Fine, Journal of Artificial Intelligence

Research 10 (1999) 67–85.

\[25\] J.Y. Halpern, Coxs theorem revisited, Journal of Artificial Intelligence Research 11 (1999)



429–435, technical addendum.

\[26\] D. Gabbay, F. Guenthner (Eds.), Extensions of Classical Logic, Handbook of Philosophical

Logic, vol. II, D. Reidel Publishing Company, 1984.

\[27\] D. Gabbay, F. Guenthner (Eds.), Alternatives to Classical Logic, Handbook of Philosophical

Logic, vol. III, D. Reidel Publishing Company, 1986.

\[28\] P. Snow, On the correctness and reasonableness of Coxs theorem for finite domains,



Computational Intelligence 14 (3) (1998) 452–459.

24 K.S. Van Horn / Internat. J. Approx. Reason. 34 (2003) 3–24

\[29\] S. Arnborg, G. Sjdin, Bayes rules in finite models, in: Proceedings of the European

€

o

Conference on Artificial Intelligence, 2000, pp. 571–575.

\[30\] S. Arnborg, G. Sjdin, On the foundations of Bayesianism, in: A. Mohammad-Djarafi (Ed.),

€

o

Bayesian Inference and Maximum Entropy Methods in Science and Engineering, 20th

International Workshop, American Institute of Physics, 2001, pp. 61–71.

\[31\] S. Arnborg, G. Sjdin, A Note on Foundations of Bayesianism, http://www.sics.se/arc/papers/

€

o

99-3-arnborg.ps.

\[32\] E.T. Jaynes, Information theory and statistical mechanics I, Physical Review 106 (1957) 620–

630.

\[33\] P. Smets, Quantifying beliefs by belief functions: an axiomatic justification, in: Proceedings of

the 13th International Joint Conference on Artificial Intelligence, Morgan Kaufmann, 1993,

pp. 598–603.

\[34\] P. Smets, The normative representation of quantified beliefs by belief functions, Artificial

Intelligence 92 (1997) 229–242.

\[35\] G.J. Erickson, C.R. Smith (Eds.), Maximum Entropy and Bayesian Methods in Science and

Engineering, Kluwer Academic Publishers, 1988.

\[36\] E.T. Jaynes, Papers on Probability, Statistics and Statistical Physics, D. Reidel Publishing

Company, 1983.
