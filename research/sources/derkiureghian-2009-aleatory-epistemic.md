---
title: Aleatory or epistemic? Does it matter?
authors: Armen Der Kiureghian; Ove Ditlevsen
year: '2009'
url: https://www.ripid.ethz.ch/Paper/DerKiureghian_paper.pdf
final_url: https://www.ripid.ethz.ch/Paper/DerKiureghian_paper.pdf
retrieved: '2026-09-23'
sha256: eaeffee4b970d0ffdebeb38bf404d663d41dde5e31fd62f8badc6a85dbeb8f3b
kind: pdf
parser: kaos-pdf
tier: http
engine: curl_cffi
escalated: false
found_by: exa
note: ''
chars: 44180
---

Special Workshop on Risk Acceptance and Risk Communication

March 26-27, 2007, Stanford University

Aleatory or epistemic? Does it matter?

Armen Der Kiureghian

University of California, Berkeley

723 Davis Hall, University of California, Berkeley, CA 94720-1710, USA, adk@ce.Berkeley.edu

u

and

Ove Ditlevsen

Technical University of Denmark

Nils Koppels Allé, Building 403, DK-2800 Kgs. Lyngby, Denmark, od@mek.dtu.dk

k

Abstract

The sources and characterization of uncertainties in engineering modeling for risk and reliability analy

ses are discussed. While many sources of uncertainty may exist, they are generally categorized as either

aleatory or epistemic. Uncertainties are characterized as epistemic, if the modeler sees a possibility to

reduce them by gathering more data or by refining models. Uncertainties are categorized as aleatory if

the modeler does not foresee the possibility of reducing them. From a pragmatic standpoint, it is useful

to categorize the uncertainties within a model, since it then becomes clear as to which uncertainties

have the potential of being reduced. More importantly, epistemic  uncertainties may introduce depend

ence between events, which may not be properly noted if their character is not correctly modeled. Influ

ences of the two types of uncertainties in reliability assessment, codified design, performance-based

engineering and risk-based decision-making are discussed. Two simple examples demonstrate the influ

ence of statistical dependence arising from epistemic uncertainties on systems and time-variant reliabil

ity problems.

\1. Introduction

The nature of uncertainties and the manner of dealing with them has been a topic of discussion by stat

isticians, engineers and other specialists for a long time (see, e.g., Paté-Cornell 1996, Vrouwenvelder

2003, Faber 2005). This paper attempts to reopen that discussion in the  context of structural reliability

and risk analysis one more time. It is unlikely that this paper r will bring a closure to that discussion. Yet,

we hope that it will shed some light on the topic as it relates to such issues as assessment of structural

reliability, codified design, performance-based design and risk-based decision-making. In particular, we

will consider systems reliability and time-variant reliability problems, for which proper treatment of

uncertainties is more crucial than for time-invariant component reliability problems. We argue that the

nature of uncertainties and how one deals with them depends on the context and the application.

Engineering problems, including reliability, risk and decision problems, without exception, are solved

within the confines of a model universe. This universe contains the set of physical and probabilistic

models (or sub-models), which are employed as mathematical idealizations of reality to render a solu-

tion for the problem at hand. The model universe may contain inherently uncertain quantities; further

more, the sub-models are invariably imperfect giving rise to additional uncertainties. Therefore, an im

portant part of building the model universe is the modeling of these  uncertainties. Any discussion on

the nature and character of uncertainties should be stated within the confines of the model universe.

While there can be many sources of uncertainty, in the context of modeling, it is convenient to catego

rize the character of uncertainties as either aleatory or epistemic. The word aleatory derives from the

Latin alea, which means the rolling of dice. Thus, an aleatoric uncertainty is one that is presumed to be

the intrinsic randomness of a phenomenon. Interestingly, the word is also used in the context of music,

film and other arts, where a randomness or improvisation in the performance is implied. The word epis

temic derives from the Greek η (episteme), which means knowledge. Thus, an epistemic uncer

επιστηµη

tainty is one that is presumed as being caused by lack of knowledge (or data). The reason that it is con

venient to have this distinction within an engineering analysis model  is that the lack-of-knowledge-part

of the uncertainty can be represented in the model by introducing auxiliary non-physical variables.

These variables capture information obtained through the gathering  of more data or use of more ad

vanced scientific principles. An uttermost important point is that these auxiliary variables define statis

tical dependencies (correlations) in a clear and transparent way.

Most problems of engineering interest involve both types of uncertainties. In the modeling phase, some

times it may be difficult to determine whether a particular r uncertainty should be put in the aleatory

category or the epistemic category. It is the job of the model builder to make the distinction. The choice

the model builder makes is, of course, conditioned on the general state  of scientific knowledge, but

much more on the practical need for limiting the sophistication of f the model to a level of significant

engineering importance for the decisions yielding from the model.

To provide a context for the following discussion, we consider the model universe for a structural reli

ability or risk analysis problem that involves a set of input variables x = ( x x ) that take values as

1 , K , n

outcomes of a corresponding set of basic random variables X = ( XX ) , a parameterized probabil

1 , K , n

istic sub-model f X( x Θ ) describing the distribution of the random vector X , and a set of parameter

f X, f

ized physical sub-models y = g ( x Θ )i = ,1 ,2 m , describing relations between the quantities x

i i , g, K,

and  derived quantities ( ), which are employed in modeling the reliability or risk prob

m y = y 1 , K , y

m

lem under study. The random variables X  are called basic because we assume they are directly observ

able and, hence, empirical data is available for them. They may represent such quantities as material

properties (strength, ductility, toughness, fatigue life, etc.), load characteristics (e.g., earthquake magni

tude, wind velocity, wave height), other environmental effects (e.g., temperature, concentration of tox

ins, amount of pollution), and geometric dimensions (e.g., cross sectional sizes, location of supports,

out-of-straightness). The derived variables y  usually are not directly observable, except in laboratory

or field studies aimed at model development. Engineering performance criteria usually are described in

terms of such derived quantities, e.g., stresses, deformations, stability limits, measures of damage, loss,

downtime, concentration of toxins in downstream waters. The sub-models f X( x Θ ) and g ( x Θ )

f X, fi , g,

i = ,2,1 m , are invariably imperfect mathematical idealizations of reality and contain uncertain er

K,

rors. Their parameters, Θ  and Θ, are usually assessed through a process of “fitting” these sub

fg

models to observed data.

Most problems in reliability or risk analysis involve the above elements. Throughout this paper we will

use these elements to discuss the modeling of uncertainties and to assess their relevance to risk and re

liability evaluation in different application contexts.

2

\2. Sources of uncertainty

In the context of the problem described above, one can identify the following sources of uncertainty:

\1. Uncertainty inherent in the basic random variables X , such as the uncertainty inherent in material

property constants and load values, which can be directly measured.

\2. Uncertain model error resulting from selection of ththe f form  of the probabilistic sub-model f X( x Θ)

f X, f

used to describe the distribution of basic variables.

\3. Uncertain modeling errors resulting from selection of the physical sub-models g ( x Θ )

i , g,

i = ,2,1 m, used to describe the derived variables.

K,

\4. Statistical uncertainty in the estimation of the pararameters Θ  of the probabilistic sub-model.

f

\5. Statistical uncertainty in the estimation of the pararameters Θ of the physical sub-models.

g

\6. Uncertain errors involved in measuring of observations, based on which the parameters Θ  and Θ

fg

are estimated. These include errors involved in indirect measurement, e.g., the measurement of a quan

tity through a proxy, as in nondestructive testing of material strength.

\7. Uncertainty modeled by the random variables Y  corresponding to the derived variables y , which

may include, in addition to all the above uncertaintnties, uncertain errors resulting from computational

errors, numerical approximations or truncations. For example, the computation of load effects in a

nonlinear structure by a finite element procedure employs iterative calculations, which invariably in

volve convergence tolerances and truncation errors.

\3. Categorization of uncertainties

In this section, we discuss the categorization of each of the uncertainty sources described above.

3.1. Uncertainty in basic variables

Consider a basic random variable X  describing a material property constant, such as the compressive

strength of concrete. Should the uncertainty in X  be categorized as aleatory or epistemic? The answer

depends on the circumstances. If the desired strength is that of the  concrete in an existing building, then

the uncertainty should be categorized as epistemic if it is decided that specimens taken from the build

ing can be tested, yielding information about the strength. The testing may, of course, involve random

errors of measurement, particularly if non-destructive methods are used. This measurement uncertainty

should also be categorized as epistemic, if there is possibility of considering alternative methods of

measurement. On the other hand, the uncertainty in the strength of concrete in a future building should

be categorized as aleatory, if there will be no attempts to make more detailed modeling related to the

control of the concrete production, for example. Until the building has been realized, no amount of test

ing will reduce the variability inherent in the strength of concrete of the future building.

The situation with demand (load) variables is somewhwhat different, as in assessing the reliability of both

existing and future buildings, one is usually interested in future realizations of demand values. Hence, in

this context, the uncertainty in basic demand variabables is usually categorized as aleatory.

It is important to reiterate the difference between b basic and derived variables. This is a choice made by the

modeler, usually following standard engineering practice. Consider, for example, the annual maximum

wind velocity, which may be of interest in designing a tower. The modeler may choose to consider this

3

quantity as a basic variable, in which case he/she would fit a probabilistic sub-model, possibly selected

from some standard recommendation, to empirically obtained annual maximum wind velocity data. Alter

natively, if such data are not available, the analyst may choose to use a predictive sub-model for the  wind

velocity derived from more basic meteorological data. In that case, the annual wind velocity is a derived

variable of the form ( x Θ ), where x  denotes the input meteorological variables and ( x Θ)

y = g , g ,

gg

denotes the predictive sub-model of the wind velocity. The categorization of uncertainties in a derived

variable is described below as a part of model uncertainty. As we will see, the uncertainty in a derived

variable may be categorized as a combination of aleatory and epistemic uncertainties.

The arbitrariness in the choice of variables as basic or derived when building the analysis model sug

gests that the categorization of uncertainties in a problem depends on our choice of sub-models. By use

of sub-models, we rely on empirical data on further basic variables, or r sometimes on a priori probability

assignments. A good example arises in seismic hazard analysis. Here, the interest is in the intensity of

potential earthquake ground motions at a site, a demand variable. Since empirical data on the intensities

of ground motions experienced at a specific site are hard to get, the common practice is to relate the

intensity measure to the earthquake magnitude, for which empirical  data is available, and to distance,

for which an a priori sub-model can be used, e.g., the earthquake can be assumed to be equally likely to

occur anywhere along an active fault. This is done through an “attenuation” law, which can be viewed

as a predictive sub-model of ground motion intensity. In this formulation the ground motion intensity

becomes a derived variable, whereas the basic variables are the earthquake magnitude and distance. In

making this sub-model choice, we introduce additional uncertainties, which can have both aleatory and

epistemic components, as described in the following section.

It is worth noting that the different categorization of uncertainties in an existing versus a future building

dictates a fundamental difference in the methods used for assessing their reliabilities. For an existi

ng

building, the reliability assessment should aim at evaluating the reliability conditioned on the known n his

tory of the building. For example, the knowledge that the building has survived an earthquake of known

intensity can be used to truncate the lower tail of f the strength distribution. As more information is gath

ered, the uncertainty in the assessment decreases. In essence, this is a problem of information updating, for

which Bayesian techniques are ideally suited. On the other hand, the problem of assessing the reliability of

a future building, say during the design process, is one of determining the state of a random sample taken

from a population. After all reasonable control measures have been taken into account, no updating with th

direct information can be performed until the building has been realized. This distinction in assessing the

reliability of an existing versus a future structure has often been missed in the literature on structutural reli

ability.

3.2. Model uncertainty

Consider a physical quantity y , which is uniquely determined in terms of two sets  of basic variables x x and

z. We wish to develop a mathematical model (or sub-model) to predict y y. Very often the exact form of the

relationship between y  y y and (xz)  is unknown. Furthermore, the modeler may not be awarare of the depend

,

ence of y  y y on z, or for reasons of pragmatism he/she may not wish to include these variables in a predictive

model of y. For example, it may be practically impossible to gather data on the variables z z and, therefore,

y

including them in the model would not be useful.

As a specific example, consider the ground motion intensity attenuation model described above. We are

well aware that the intensity at a site is dependentnt, in addition to the earthquake magnitude and distance,

4

on such variables as the propagation velocity of the  fault rupture, the mechanical characteristics of ththe path

of propagation of seismic waves, the geologic featurures surrounding the site, and so on. However, from a

pragmatic standpoint, it is difficult if not impossible to measure these variables for a given site. Therefore,

we exclude them in the attenuation model. These variables, as well as others of which we may not be

aware, constitute the missing variables z z in the ground motion attenuation model that is expressed only in

terms of the earthquake magnitude and distance, which constitute the vector of basic variables x for the

model.

The predictive model of y  y y may be written in the form

ˆ

y = g ( x Θ ) + ε  (1)

, g

ˆ

where ( x Θ ) is an idealized mathematical model involving the basic variabables x  with Θ as its pa

g ,

gg

ˆ

rameters, and ε = y − g ( x Θ ) is the model error (the residual). The parameters Θ are usually esti

, g g

mated through statistical analysis of the model against observed data on  and x . It is noted that, while

y

it may be difficult to observe y  for the particular risk analysis problem of interest, paired observations

of  and x  are necessary to assess the model in (1). These observations are usually conducted under

y

special laboratory or field studies aimed at model development.

The model error ε  has two components: (a) the effect of the missing variables z , which are absent in

the model, and (b) the effect of the potentially inaccurate form of the model. For example, the relation

ship between y  and x  could be nonlinear, while the model may use a linear form. Since these effects

are uncertain, ε  is modeled as a random variable. Usually, one is interested in an unbiased model. In

that case, parameters Θ are determined by setting the mean of ε  equal to zero. Furthermore, by a

g

proper transformation of the model, it is often possible for ε  to have a normal distribution with its

standard deviation σ – a measure of the inaccuracy of the model – being independent of x . This is

ε

known as the homoskedastic form of the model (Box and Tiao 1992). Thus, in order r to completely de

fine the model, the set of model parameters to be estimated is ( Θσ, ) . When more than one sub

g ε

model is involved, in addition to all the parameters Θ and the standard deviation σ for each sub

gε

model, one will need to also determine the correlation coefficients between the error terms for different

sub-models.

We now examine the nature of the uncertainties in the model of the foform in (1). As explained above, ε

accounts for the uncertain effects of the missing variables z  as well as the potentially inaccurate form

of the model. Both these uncertainties can be reduced if the model is  refined to include one or more of

the missing variables and/or mathematical expressions (analytical or algorithmic), which provide a bet

ter approximation to the correct form. In this sense, the uncertainty in ε  is categorized as at least partly

epistemic. However, our limited state of scientific knowledge may not allow us to further refine the

model form and our inability to measure the missing variables may preclude the possibility of expand

ing the model. In such cases, at least a portion of the uncertainty in ε  is categorized as aleatory. In par

ticular, the part of the uncertainty in ε  that arises from the effect of the missing variables is reasonably

categorized as aleatory if these variables, though unknown, are characterized as being aleatory random

variables.

We now turn to the probabilistic model (or sub-model) f X( x Θ ). This model is normally selected by

f X, f

fitting a theoretical distribution to available data. Various methods for evaluating goodness of the fit are

5

available. However, when events with small probabilities are of interest, as is the case in most structural

reliability and risk problems, the tail of the probability distribution becomes important. Unfortunately,

standard goodness-of-fit tests do not guarantee accuracy of the fit in the tail. For example, Ditlevsen

(1994) has shown that equally well-fitted distributions can lead to significantly different probability

estimates. Therefore, in computing probabilities, particularly for rare events, an error of uncertain mag

nitude arises from the assumed distribution model. This error can be  placed in the epistemic category,

since gathering of more data would allow a better fit of the distribution and, therefore, a reduction in

the model uncertainty. However, unlike the case of physical models described above, it is difficult to

assess the magnitude of the error arising from the choice of a distribution model. A logical way to do

this would be to compute the probability of interest for all viable distribution models and assess the

variability in the computed probability values. A second approach, suggested in Der Kiureghian (1989),

is to parameterize the choice of the distribution. The uncertainty y in the distribution model is then repre

sented by the uncertainty in the parameter. However, both these apapproaches are demanding of large

amounts of analysis.

The arbitrariness in the choice of the distribution model and the “tail-sensitivity” of small probabilities

has lead to the recommendation that probabilistic structural design codes standardize probability distri

butions for load and resistance quantities (Ditlevsen and Madsen, 1989). One point of view is that in

such a construct the computed probabilities should be considered as notional values and that caution

should be exercised in using them in an absolute sense, e.g., for computing the expected costs of rare

events. However, this view assumes that absolute probability y exists as a physical entity outside the

mathematical model by which it is computed.

It is only in very special problems, where one can think of the  probability of an event as the relative

frequency of the physical occurrence of the event in a long series  of independent repetitions of an un

changed experiment, in which the event can occur. In the field of struructural safety, several highly im

portant sources of uncertainty do not exhibit such a repetitive behavior under identical circumstances.

One can safely state that the interpretation of the stable long run occurrence frequency as an absolute

probability in the physical sense belongs to utopia. Consequently, the usefulness of the probability con

cept must rest on another rational foundation. However, as a mind construruct (and a simulation tool) the

relative frequency interpretation of a mathematical probability is decisive for its usefulness as a degree

of belief regarding the occurrence of an event. To make a probababilistic degree-of-belief model subject

to a pragmatic test of falsification (a concept by Matheron based on Popper), and thus defensible as an

objective tool, it is necessary that some type of relative frequency behavior be associated with the prob

abilistic model. A detailed discussion of the philosophy of this objbjectivity issue is given in Ditlevsen

and Madsen (1996).

The mentioned codification of selected probability distributions should be seen as a consensus of the

structural reliability engineering profession concerning the model  elements to which the calculated

probabilities are sensitive. Otherwise the engineering practice becomes open to unjustified distribution

tail choices made for competitive reasons. Moreover, a useful commmmon knowledge bank is obtained in

this way, not the least with respect to the choice of distributions of the epistemic uncertainties. Clearly,

for distributions based on sample data, the knowledge bank should be subject to revision as more data

and better quality data become available.

6

To overcome the problem of arbitrary distribution choice, probababilistic codes are developed by a proc

ess of calibration to accepted practice, whereby it becomes  reasonable at least to use probability as a

means of comparison and adjustment. It even makes sense to use the  standardized distributions in mod

els for optimal decision-making, provided the intangible utility y values are also calibrated so that the

accepted practice on the average is the optimal practice.

In recent years considerable attention has been paid to developing performance-based engineering, par

ticularly with regard to design of buildings and other structures to resist earthquake forces (Cornell and

Krawinkler 2000). Central to this approach is the promise of computing risk associated with various

structural performance requirements, including those of rare events  such as extreme damage and col

lapse. In the rapidly developing literature in this field, little attention is paid to such issues as the tail

sensitivity problem or the characterization of uncertainties inherent in the modeling and estimation.

While this paper may not contribute to solving this problem, it raises a concern and hopefully sheds

some light on the underlying issues and problems of an approach that relies on values of probabilities

for rare events.

3.3. Parameter uncertainty

The parameters ( Θσ, )  of the physical sub-models and Θ  of the distribution sub-model are estimated

g εf

by statistical analysis of observed data. Specifically, ( Θσ, )  are estimated based on pair-wise observa

g ε

tions of Y  and X , and Θ  are estimated based on observations of X . The preferred approach is the

f

Bayesian analysis, which allows incorporation of prior information on the parameters, possibly in the form

subjective expert opinion. The uncertainty in the parameter estimates is directly related to the amount nt and

quality of the available information. By amount, we  refer to the size of the available samples of observa

tions. By quality, we refer to the accuracy in the observations. Any measurement error present in the ob

servations deteriorates the information content and, hence, the quality of the data. The quality also refers

to the information content in the prior. This kind of analysis is now routine and we will not discuss further

details.

Parameter uncertainties are strictly epistemic becauause the uncertainty in the estimation decreases and d may

asymptotically vanish with increasing quantity and quality of the available observational data.

3.4. Final remark

The above discussions may raise the philosophical question whether there is any aleatory uncertainty at

all. Clearly this question does not make sense outside the model universe. From a linguistic point of

view, all uncertainties are the same as lack of knowledge. However, as  explained above, it is convenient

within a probabilistic model (mathematical statistical model, in particular) to introduce the categoriza

tion of uncertainties into aleatory and epistemic. Thus, within the model universe, the word epistemic

assumes a more narrow meaning than just lack of knowledge.

Perhaps it is just a matter of time before it becomes sufffficient to consider models that do not need the

aleatory category, assuming that we learn about all missing variables and exact forms of models. Per

haps even basic variables can be explained through exact predictive models. In such a world, if uncer

tainty exists, it will only be epistemic. This utopian world, however, is too far from the reality of engi

neering practice today. The advantage of separating the uncertainties into aleatory and epistemic is that

we thereby make clear which uncertainties can be reduced and which uncertainties are less prone to

reduction, at least in the near-term. This categorization helps us  in allocation of resources and in devel-

7

oping engineering models. Furthermore, better understanding of the categorization of uncertainties is

essential in order to properly formulate risk or reliability problems. For example, epistemic uncertain

ties may introduce dependence among the estimated performances of the components of a system, and

non-ergodic uncertainties may introduce dependence among a sequence of events in time or space. In

practice, these dependences are often neglected due to improper treatment of the uncertainties. The ex

amples in the following section demonstrate the influences of such effects.

\4. Influence of uncertainties

In this section we present two examples to demonstrate the influence of uncertainties on reliability as

sessment. The first example demonstrates the influence of statistical dependence introduced by epis

temic uncertainties among the components of a system. The second example demonstrates the influence

of non-ergodic uncertainties, both epistemic and aleatory, in a time-variant reliability problem.

4.1. System reliability

Consider a k-k-out-of-N -N N system. Such a system survives if at least k k out of N N components survive, where

1≤ k ≤ N . The extreme values k =1  and k = N  respectively define the special cases of parallel and series

systems. For the sake of simplicity, we assume the components have statistically independent and identi

cally distributed capacities represented by the random variable X, and also statistically independent and

1

identically distributed demands represented by the random variable X . In essence, the component ca

2

pacities and demands are random realizations from ththe distributions of X and X , respectively. Thus,

12

the components have identical limit-state functions  defined by,

g(x) = x − x  (2)

1 2

with {(X) ≤ }0  indicating the failure event. We further assume that X and X  are normal random

g12

variables with unknown means  and  and known standard deviations  and , respectively. Ac

µµσ1σ2

12

cording to the terminology introduced earlier in this paper, X = ( XX )  are basic random variables and

1 , 2

Θ = µ( µ, )  are distribution parameters to be estimated. Suppose the available information for estimat

f 1 2

ing µ and µ are sample observations of size n  of the capacity and demand values with respective sam

12

ple means x  and x . It is convenient to adopt Bayesian modeling, in whwhich µ and µ are considered as

1212

realizations of Bayesian random variables M and M . Assuming independence of M and M  and

1212

diffuse priors, these imply posterior distributions  of M and M , which are normal with means x  and

121

x  and standard deviations σ / n  and σ / n , respectively.

212

As described earlier, the statistical uncertainty in the distribution parameters µ and µ is epistemic in

12

nature. Since the component capacities and demands are identically distributed, this uncertainty is shared

by all the components of the system. Hence, the statistical uncertainty inherent in the estimation of the

distribution parameters introduces statistical dependence among the estimated states of the system compmpo

nents. To investigate this effect, we proceed as follows:

Observe that, for the case of linear limit-state fununction and normal random variables, the conditional  reli

ability index of a typical component for given values of  and  is

µ1µ2

µ 1 −µ2

µ(β µ, )=  (3)

1 2

22

σ +σ

12

8

Since M and M  are normally distributed posterior to obtaining the data, it can be easily shown that

12

22

B (β MM )  has the normal distribution with mean (/) +  and standard deviation

= 1 , 2µ B = x1 − x2σ1 σ 2

σ = /1 n . It is evident that the uncertainty in the reliability index in account of the statistical uncer

B

tainty is directly related to the size of observation samples. The probability of failure of the component

conditioned on the distribution parameters is given n by µ( ) Φ \[ 
− µ(β )\] . Viewing this as a

p µ, = \[ 
− µ,

f 1 2 1 2

transformation between β  and , one easily determines that the distribution of the (Bayesian) random

p

f

failure probability P 
f = p ( MM ) , reflecting the effect of the statistical uncertainty, is

P 
f f1 , 2


2












1



\[ \]Φ −
−1
1( )p

nx −x2

1 1 21

# f 
P( ) Φ 1( )\[ Φ 1( ) (4)

− −

p n exp p+ p











= − − −−

f 
Pf

Pf2222









σ +σ





12

Figure 1 shows plots of the distributions of B  and Pf for µ = 3  and n = 10  and 30. The so-called pre

PfB

\~

dictive failure probability, denoted p, is the mean of this distribution. Its value can be  obtained by either

f

of the following formulas:

+∞+∞

∫ ∫

\~

p =p µ( µ, ) f 
M µ( ) f
Mµ( d) µ dµ

f f 1 2 f 
M 1 1 f
M22 1 2

∞∞

(5)

−−

1

### =∫pf 
p( p d)
pd
p

f 
pf

0

\~\~

\~ \~

The corresponding predictive reliability index is β = Φ 1(− p ). Plots of β and p for µ = 3  and as

f fB

functions of the sample size n  are shown in Figure 2. Note that with increasing n  the predictive reliability

index asymptotically approaches µ = 3  and the predictive failure probability approaches Φ(−µ ) =

BB

0.00135, the limiting values without statistical uncertainty. Increasing statistical uncertainty (decreasing

sample size) tends to increase the predictive failurure probability and decrease the predictive reliability in

dex.

We now consider the system failure probability. Even though the component states are statistically inde

pendent, statistical dependence among their probability estimates is present due to sharing of the uncertain

distribution parameters M and M  by all components. Thus, to properly handle this dependence, we

12

must first evaluate the conditional probability of the system failure given the distribution parameters, and

then integrate over all possible values of the paramameters. Using the complementary binomial cumulative

probability function, the conditional probability of failure is

N

N!

\[ \] ( ) 
f
p 
1 2 
µ µ, \[ \] ( ) 
f
p−
1 2
1 µ µ,

∑

N

( ) 
1 2 
µ µ, ( ) 
1 2 
µ µ, ( ) 
1 2
µ µ,

j−j

## pµ µ, = \[ 
p µ µ, \[ 
1 −pµ µ, (6)

sf 1 2 f1 2 f1 2

j (! N −j)!

j = N − k+1

Using the distribution of P 
f = p ( MM )  given in (5), the predictive system failure probability is ob

P 
f f1 , 2

tained as

1N

N!

∫ ∑

\~ j N j

1( ) f 
P( pd) (7)

−

p = p −p p pd

sf f 
Pf

Pf

j (! N −j)!

0 j = N − k+1

9

\~

As mentioned earlier, when n  approaches infinity, p = Φ ( − µ ). The corresponding value of the system

f B

failure probability is obtained by substituting this value in place of p µ( µ, ) in (6). We denote this

f 1 2

\~ \~ \~

value as . Figure 3 shows plots of the ratio / for series systems (k N)  with 3

p p p = µ =

sf ,n→∞sf f ,n→∞B

and for parallel systems (k = )1  with µ = 2 , both systems having 1 to 5 components. It can be seen that

B

increasing statistical uncertainty (decreasing sample size n ) increases the predictive failure probability for

both systems. For series systems, the effect is relatively modest. For parallel systems, the increase in the

failure probability can be by orders of magnitude. Figure 4 shows the same ratio for systems with N = 5

components with varying k  for n = 10 and 30 and µ = 3 . As can be seen, the influence of the statistical

B

uncertainty increases with increasing redundancy of f the system (decreasing k ). This is because the posi

tive correlation arising from statistical uncertaintnty effectively reduces the redundancy of the system

.

4.2. Time-variant reliability

Consider a structure subjected to repeated applications of earthquake loads. Each earthquake produces a

stochastic ground motion at the site of the structurure. Following common practice, we use a single measure

(e.g., the peak ground acceleration) to characterize the intensity of the motion. Let S  denote this intensity

measure and assume, for a given earthquake of random chararacteristics, it has a lognormal distribution with

parameters λ  and ζ . Also let ν  denote the mean rate of earthquakes per year. If ththe occurrence of

SS

earthquakes are assumed to follow a Poisson process, then h ( s ) = 1 − exp{ − ν Φ \[ − (ln s − λ ζ/) \]}  is the

S S

annual seismic hazard function for the site. Let R  denote the capacity of the structure (for any perfoform

ance criterion of interest) expressed in terms of the ground motion intensity measure, and assume it has

the lognormal distribution with parameters λ  and ζ . In general, there are errors in modeling the struc

RR

ture. Furthermore, a single intensity measure cannot fully characterize the effect of a stochastic motion on

the structure. To account for these errors, we adopt the limit-state function

g(rsε) = ln r + ε − ln s + ε  (8)

,,1 2

where r  and s  are realizations of R  and S , respectively, and ε  and ε  are model error terms, the for

12

mer reflecting errors in modeling the structure (model form error) and the latter reflecting the effect of the

stochastic ground motion (missing variables). We assume the model errors are normally distributed with

zero means and standard deviation σ and σ, respectively. Furthermore, we assume R S ε  and ε

12, , 12

are statistically independent. It follows from these assumptions that  has the normal distribution with

g

22 22

mean λ − λ  and variance ζ+ σ + ζ+ σ . The set of distribution parameters Θ = λ,ν( ζ, λ, ζ,

#### R SR 1S 2R R S S,

σ σ, ) are, of course, subject to statistical uncertainty y and so we let Θ
f (θ)  denote their posterior joint

1 2Θ
f

distribution.

For a given earthquake, no distinction between the uncertainty types needs to be made, and the predictive

failure probability is given by





λ λ

∫







−

\~R S

p = Φ −Θ
f(θ d) θ (9)

fΘ
f







22 22

ζ ζ





\+ σ + + σ

θR 1S2

\~

The product µp, where µ denotes the mean of ν , represents the mean rate of earthquake-induced

νfν

failures per year. This observation has lead many investigators (see Der Kiureghian 2005 for several refer

ences) to assume that the failure events are Poisson and therefore the following expression for the failure

probability in t),0( t has been used:

10

( 
− )

\~

\~

P 
f = 1 − exp ( 
− µp t (10)

P 
f , Psn νf

However, due to the presence of non-ergodic uncertainties, the failure events in time are not statistically

independent and, therefore, cannot constitute Poisson events. More specifically, the aleatory or epistemic

uncertainties in R  and ε  as well as the epistemic uncertainties in Θ  are shared by all earthquake events,

1

while the aleatory uncertainties in S  and ε  are renewed at each earthquake. To overcome this depend

2

ence, we note that the conditional failure events given R = r ε = e  and Θ = θ  are Poisson with the

, 1

2 2

mean rate ν Φ \[ − (ln r + e − λ /) ζ + σ \]. Hence, the predictive failure probability over the time interval

S S 2

t),0( t is given by









ln + λ









∫

\~r e−

S

P 
f = 1 exp νΦ t f 
R( r ) ε
f ( e ) Θ 
f ( θ d) r d edθ (11)







− − −

P 
f f 
RΘ 
f







ε
f 1

22

ζ





+





σ

r e θS2

, ,

To investigate the difference between the approximatation in (10) and the exact result in (11), we assume

the following distributions and parameter values: ν  is lognormal with varying mean µ and 50% coeffi

ν

2

cient of variation, ζ = .0 294 λ  is normal with a zero mean and variance ζ /n ζ = .0 472 λ  is nor

#### R, RR, S, S

2

mal with mean − 0.1  and variance ζ /n σ = 3.0  and σ = 5.0 , where n  is a measure of the quality of

S, 1 2

\~\~

statistical information (analogous to sample size).  Figure 5 shows plots of Pf and Pf as a function of

Pf,PsnPf

t  for 10  and → . It can be seen that neglecting the dependence betwtween successive events due

µn =n ∞

ν

to the non-ergodic uncertainties results in an overestimatation of the failure probability for large µt  values.

ν

Also, increasing statistical uncertainty (small n)  increases the failure probability estimate. The differences

between the two results, however, are relatively insignificant. This is because the considered time-varariant

problem is analogous to a series system problem with th a random number of components.

\5. Conclusions

The characterization of uncertainties into aleatory and epistemic in risk and reliability analysis and in

codified or performance-based design is discussed. The distinction between aleatory and epistemic un

certainties is determined by our modeling choices. The distinction is useful for identifying sources of

uncertainty that can be reduced, and in developing sound risk and reliability models. It is shown that for

proper formulation of reliability, careful attention should be paid to the categorization (epistemic, alea

tory, ergodic or non-ergodic) of uncertainties. Failure to do so may result in underestimation or overes

timation of failure probability, which can be quite significant (orders of f magnitude) in certain cases.

References

Cornell, C. A., and Krawinkler, H. (2000). Progress and challenges in seismic performance assessment.

PEER Center News, Spring 2000. http://peer.berkeley.edu/news/2000spring/index.html

Box, G.E.P., and G.C. Tiao (1992). Bayesian inference in statistical analysis. Addison-Wesley, Read

ing, Mass.

Der Kiureghian, A. (1989). Measures of structural safety under imperfect states of knowledge.  J. Struc

tural Engineering, ASCE, 115:1119-1140.

Der Kiureghian, A. (2005). Non-ergodicity and PEER’s framework formula. Earthquake Engineering

and Structural Dynamics34:1643-1652.

,

Ditlevsen, O. (1994). Distribution arbitrariness in structural reliability. Structural Safety & Reliability

,

G. Schuëller, M. Shinozuka and J. Yao, Eds., Balkema, Rotterdam, The Netherlands, Proceedings of

##### ICOSSAR’93, 1241-1247.

11

Ditlevsen, O. and H. O. Madsen (1989). Proposal for a code for the direct use of reliability methods in

structural design. JCSS Working Document, 1989.

Ditlevsen, O., and H.O. Madsen (1996). Structural reliability methods. J. Wiley & Sons, New York,

NY.

Faber, M. H. (2005). On the treatment of uncertainties and probabilities in engineering decision analy

sis. J J. Offshore Mechanics and Arctic Engineering, 127:243-248.

Paté-Cornell, M. E. (1996). Uncertainties in risk analysis: six levels of treatment. Reliability Engineer

ing and System Safety54:95-111.

,

Vrouwenvelder, A.C.W.M. (2003). Uncertainty analysis for flood defense systems in the Netherland.

Proceedings, ESREL, 2003.

3600

n=10

n=30

2400

fβ β( β( ) , 3 , 103 10fp p 3 ( , 
f ( p 3 ( ) , , 10
f ( p) 10
)

p p ( 
f 
P3 , 
( ) 0
)

, , , , 
(

p

3 , 
β

f 
Pf

β β( 
fBβ
fB, 
(30
) Pf

fβ β( 
fBβ( ) , 3 , 30
fB(β) , 
(3 
β, 
β30
) fp p 3 ( , 
fp 3 ( ) , , 30
f, , 30

1200

00

2 2.5 3 3.5 40 0.002 0.004 0.006 0.008

β
β p
p

β
β p
p

( )

Figure 1: Distributions of reliability index (left) and failure probability  (right).

0.0025

3

0.002

\~

βtilde 3 n ( ,
β
\~ 3 ( 
\~ ptilde 3 n ( ,
f
pe ( 
p3 n ( ) ,
f
p

3 n ( ) ,
β
\~ 2.93 
f

3 ( 
β

,,

0.0015

2.80.001

0 20 40 60 80 1000 20 40 60 80 100

n
n n

n
 n n

Figure 2: Predictive reliability index (left) and failure probability (rigight) as functions of sample size.

12

Figure 3: Influence of statistical uncertainty on series (left) and parall

µβ := 2
 n n

Pftilde 3 n ( , 3 n ( ) , , 1 , 1, , 1 , 1

Pfinf 3 1 ( , 3 1 ( ) , , 111.5

, ,

Pftilde 3 n ( , 3 n ( ) , , 2 , 2, , 2 , 2

Pfinf 3 2 ( , 3 2 ( ) , , 2
\~21.4

( 
\~, ,

e 3 ( 
p

Pftilde 3 n ( , 
sf
p3 n ( ) , , 3 , 3
sf
p3 n , 
sf, 
sf, 3 , 3

Pfi
\~Pfinf 3 3 ( , 
\~3 3 ( ) , , 3, , 31.3

ftild
p

Pftilde 3 n ( , 
sf n→
p
,de ( 
sf 3 n ( ) , , 4 , 4
f n→∞,3 
,3 , 
n, 
nn , 
→, 
→4 
∞4 
∞, 4

Pfinf 3 4 ( , 3 4 ( ) , , 4, , 41.2

Pftilde 3 n ( , 3 n ( ) , , 5 , 5, , 5 , 5

Pfinf 3 5 ( , 3 5 ( ) , , 5, , 51.1

1

µ
 β 
 := 2

4

1.10

3

1.10

Pftilde 3 10 ( , 
\~e 3 ( 
\~3 10 ( ) , , 5 , K
p
\~5 K

, , ,

( 
nf ( 
p

Pfinf 3 5 ( , 
sf
p3 5 ( ) , , K
sf
p3 ( , 
sfK

, 
f,

\~100

Pftilde 3 30 ( , 
f 
p3 30 ( ) , , 5 , K
f n→5 K

ftild
p

de ( 
fif 
sf

, , ,

,n→∞

Pfinf 3 5 ( , 
f 3 5 ( ) , , KK

, ,

10

100

1

Series systems

3

µ B =

k = N =1-5

0 20 40 60 80 100

n

N=5

3

µ B=

n =10

n = 30

1 2 3 4 5

K
k

K
k

Figure 4: Influence of statistical uncertainty

on k-out-of-N system.

10

Pftilde ( ) µβ , n , 1 , 1µβ , n , 1 , 1Parallel systems

Pfinf ( ) µβ , 1 , 1µβ 1 1

, , 82

µ B =

Pftilde ( ) µβ , n , 2 , 1µβ , n , 2 , 1

( 
\~

Pfinf 
p( ) µβ , 2 , 1
p
\~µβ 
p
\~2 1

f ( µ
p

, ,

β 
sf6

Pftilde ( ) µβ , n , 3 , 1
fµβ , n , 3 , 1k / N = 5/1

\~

Pfinf 
p( ) µβ , 3 , 1
f µβ 
f 3 1

Pfin
p, ,

( µ
sf ,n→∞

Pftilde ( ) µβ , n , 4 , 1µβ n 4 1

, , , 41/4

Pfinf ( ) µβ , 4 , 1µβ , 4 , 1

1/3

Pftilde ( ) µβ , n , 5 , 1µβ n 5 1

, , , 21/2

Pfinf ( ) µβ , 5 , 1µβ , 5 , 1

1/1

0

0 20 40 60 80 100

n

el (right) systems.

0.08

\~

Pf

0.0710Pf Psn

n =,

n→ ∞

0.06

0.05

0.04

\~

0.03

Pf

Pf

0.02

0.01

0

0 1 2 3 4 5 6 7 8 9 10

µt

ν

Figure 5: Influence of non-ergodic uncertain

ties on time-variant reliability

13
