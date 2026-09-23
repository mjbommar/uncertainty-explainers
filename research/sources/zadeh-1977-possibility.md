---
title: Fuzzy Sets as a Basis for a Theory of Possibility
authors: L.A. Zadeh
year: '1977'
url: http://www2.eecs.berkeley.edu/Pubs/TechRpts/1977/Archive/ERL-m-77-12.pdf
final_url: https://www2.eecs.berkeley.edu/Pubs/TechRpts/1977/Archive/ERL-m-77-12.pdf
retrieved: '2026-09-23'
sha256: 33504f49af80cbe8b52861a003224da0c83501d16cc5ddad06ea7bfaa869d4bb
kind: pdf
parser: kaos-pdf
tier: http
engine: curl_cffi
escalated: false
found_by: exa
note: UCB/ERL M77/12; published in Fuzzy Sets and Systems 1:3-28 (1978)
chars: 51601
---

on the first page. To copy otherwise, to republish, to post on servers or to redistribute to

for profit or

classroom use is granted without fee provided that copies are not made or distributed

Permission to make digital or hard copies of all or part of this work for personal or

Copyright © 1977, by the author(s).

All rights reserved.

commercial advantage and that copies bear this notice

lists, requires prior specific permission.

and the full citation

FUZZY SETS AS A BASIS FOR A THEORY

by

L. A. Zadeh

Memorandum No. UCB/ERL

23 February 1977

##### ELECTRONICS RESEARCH LABORATORY

College of Engineering

University of California,

94720

###### !£V 
^HOTO"\*\*V 
OUPLIC\*-OAN 
ATON DEPARTMENT 
SECTION)

!£V 
V OAN 
^HOTOOUPLICAT.ON DEPARTME
SECTION) 
RY

###### THE GENWAL LIBRARY

#### •N.VERS.TY OF CALIFORNIA

###### •ERKELEY. CALIFORNIA 84720

##### OF POSSIBILITY

M77/12

Berkeley

*FUZZY SETS AS A BASIS FOR A THEORY OF POSSIBILITY*

\*

*L.A. Zadeh*

*Abstract*

*The theory of possibility described in this paper is related to the*

*theory of fuzzy sets by defining the concept of a possibility distribution*

*as afuzzy restriction which acts as an elastic constraint on the values that*

*may be assigned to avariable. More specifically, if F is a fuzzy subset*

*of a universe of discourse U = {u} which is characterized by its membership*

*function then proposition of the form "X is F," where X is varia*

*up, aa*

*ble taking values in U, induces a possibility distribution nx which equates*

*the possibility of X taking the value u to up(u) \<-- the compatibility*

*of with F. In this X becomes fuzzy variable which is associated*

*u way, a*

*with the possibility distribution Itx in much the same random variable*

*way as a*

*is associated with a probability distribution. In general, a variable*

*may*

*be associated both with a possibility distribution and a probability distribu*

*tion, with the weak connection between the two expressed as the possibility/*

*probability consistency principle.*

*Athesis advanced in this is that the imprecision that is intrinsic*

*paper*

*in natural languages is, in the main, possibilistic rather than probabilistic*

*in nature. Thus, by employing the of possibility distribution,*

*concept a a*

*proposition, p, in anatural language may be translated into aprocedure*

*which the probability distribution of of attributes which*

*computes aset are*

*implied by p. Several types of conditional translation rules are discussed*

*and, in particular, atranslation rule for propositions of the form Xis Fis*

*a-possible, where a is anumber in the interval \[0,1\], is formulated and*

*illustrated by examples.*

*Computer 
iScience Division, Department of Electrical Engineering 
iiand Computer 
i*

*p
Sciences and the Electronics Research Laboratory, 
d bl g
University 
liof p
California,*

*Berkeley, 
CCA 94720. Research supported by y
Naval Electronic Systems 
C0Command*

*y
Contract N00039-77-C-0022, U.S. Army y 
Research Office Contract DAHC04-75-G0056*

*and National Science Foundation Grant MCS76-06693.*

*FUZZY SETS AS A BASIS FOR A THEORY OF POSSIBILITY1\**

*L.A. Zadeh\**

*\1. Introduction*

*The pioneering work of Wiener and Shannon on the statistical theory of*

*communication has led to a universal acceptance of the belief that informa*

*tion is intrinsically statistical in nature and, as such, must be dealt with*

*by the methods provided by probability theory.*

*Unquestionably, the statistical point of view has contributed deep*

*insights into the fundamental processes involved in the coding, transmission*

*and reception of data, and played a key role in the development of modern*

*communication, detection and telemetering systems. In recent years, however,*

*a number of other important applications have come to the fore in which the*

*major issues center not on the transmission of information but on its mean*

*ing. In such applications, what matters is the ability to answer questions*

*relating to the information that is stored in a data base — as in natural*

*language processing, knowledge representation, speech recognition, robotics,*

*medical diagnosis, analysis of rare events, decision-making under uncertainty,*

*picture analysis, information retrieval and related areas.*

*A thesis advanced in this is that when main is with*

*paper our concern*

*the meaning of information — rather than with its measure — the proper*

*framework for information analysis is possibilistic rather than probabilistic*

*in nature, thus implying that what is needed for such an analysis is not*

*Computer Science Division, Department of Electrical Engineering and Computer*

*Sciences and the Electronics Research Laboratory, University of California,*

*Berkeley, CA 94720. Research supported by Naval Electronic Systems Command*

*Contract N00039-77-C-0022, U.S. Army Research Office Contract DAHC04-75-G0056*

*and National Science Foundation Grant MCS76-06693.*

*^The term possibilistic — in the sense used here — was coined by*

*B.R. Gaines and L. Kohout in their possible automata \[1\].*

*paper on*

*To in the International Journal for Fuzzy Sets and Systems.*

*appear*

*1*

*probability theory but an analogous — and yet different — theory which*

*2*

*might be called the theory of possibility.*

*As will be seen in the sequel, the mathematical apparatus of the theory*

*of fuzzy sets provides a natural basis for the theory of possibility, play*

*ing a role which is similar to that of measure theory in relation to the*

*theory of probability. Viewed in this perspective, a fuzzy restriction may*

*be interpreted as a possibility distribution, with its membership function*

*playing the role of a possibility distribution function, and a fuzzy variable*

*is associated with a possibility distribution in much the same manner as a*

*random variable is associated with a probability distribution. In general,*

*however, a variable be associated both with possibility distribution*

*may a*

*and a probability distribution, with the connection between the two expressi*

*ble as the possibility/probability consistency principle. This principle —*

*which is an expression of a weak connection between possibility and probability*

*will be described in greater detail at a later point in this*

*— paper.*

*The importance of the theory of possibility stems from the fact that*

*— contrary to what has become a widely accepted assumption — much of the*

*information on which human decisions are based is possibilistic rather than*

*probabilistic in nature. In particular, the intrinsic fuzziness of natural*

*languages which is a logical of the necessity to*

*— consequence express*

*information in a summarized form — is, in the main, possibilistic in origin.*

*Based on this premise, it is possible to construct a universal language in*

*which the translation of a proposition expressed in a natural language takes*

\_

*The interpretation of the concept of possibility in the theory of possi*

*bility is quite different from that of modal logic \[2\] in which proposi*

*tions of the form "It is possible that..." and "It is that..."*

*necessary*

*are considered.*

*Such a language, called PRUF (Possibilistic Relational Universal Fuzzy),*

*will be described in a forthcoming*

*paper.*

*the form of a procedure for computing the possibility distribution of a set*

*of fuzzy relations in a data base. This procedure, then, be interpreted*

*may*

*as the meaning of the proposition in question, with the computed possibility*

*distribution playing the role of the information which is conveyed by the*

*proposition.*

*The present has the limited objective of exploring of the*

*paper some*

*elementary properties of the concept of a.possibility distribution, moti*

*vated principally by the application of this concept to the representation*

*of meaning in natural lnaguages. Since our intuition concerning the pro*

*perties of possibility distributions is not as yet well developed, some of*

*the definitions which are formulated in the sequel should be viewed as*

*provisional in nature.*

*\2. The Concept of a Possibility Distribution*

*What is a possibility distribution? It is convenient to answer this*

*question in terms of another concept, namely, that of a fuzzy restriction*

*\[ 4 \], \[ 5 \], to which the concept of a possibility distribution bears a*

*close relation.*

*Let X be a variable which takes values in a universe of discourse U,*

*with the generic element of U denoted by u and*

*X=u (2.1)*

*signifying that X is assigned the value u, u e U.*

*Let F be a fuzzy subset of U which is characterized by a membership*

*function Then F is fuzzy restriction X (or associated with X)*

*up. a on*

*if F acts as an elastic constraint on the values that be assigned to*

*may*

*X -- in the sense that the assignment of a value u to X has the form*

*X=X=u=u: uF(u) (2.2)*

*where \]ip(u) is interpreted as the degree to which the constraint repre*

*sented by F is satisfied when u is assigned to X. Equivalently, (2.2)*

*implies that 1^Up(u) is the degree to which the constraint in question*

*4*

*must be stretched in order to allow the assignment of u to X.*

*Let R(X) denote a fuzzy restriction associated with X. Then, to*

*that F plays the role of a fuzzy restriction in relation to X,*

*express*

*we write*

*R(X) = F . (2.3)*

*An equation of this form is called a relational assignment equation because*

*it represents the assignment of a fuzzy set (or a fuzzy relation) to the*

*restriction associated with X.*

*To illustrate the concept of a fuzzy restriction, consider a proposi*

*a 
t5*

*tion of the form a 
t= X is F, where X is the of an object, variable*

*p name a*

*or a proposition, and F is the name of a fuzzy subset of U, as in*

*"Jessie is intelligent," "X is small number," "Harriet is blond is*

### wery a

*quite true," etc. As shown in \[ 4 \] and \[ 6 \], the translation of such a*

*proposition may be expressed as*

*R(A(X)) = F (2.4)*

*where A(X) is an implied attribute of X which takes values in U, and*

*(2.4) signifies that the proposition p £ X is F has the effect of assigning*

*F to the fuzzy restriction on the values of A(X).*

*4*

*A point that must be stressed is that a fuzzy set per se\* is not a fuzzy*

*restriction. To be a fuzzy restriction, it must be acting as a constraint*

*on the values of a variable.*

### The symbol A stands for "denotes" or "is defined to be."

*As a simple example of (2.4), let p be the proposition "John is young,"*

*in which is fuzzy subset of U \[0,100\] characterized by the*

*young a*

*=*

*membership function*

*uyoung(u) \]S(u;.20,30,40) (2.5)*

*"*

*=*

*where is the numerical and the S-function is defined by \[ 4 \]*

*u age*

# S(u;\<x,3,y) = 0 for u \<\_a (2.6)

*=2(^)2 
vya for a\<u\<3*

*()
vy-a — —*

*U-Y\\2
\]^L)*

### = 1-U-Y\\
%Y-a
2{\]^L) for 3 \< u \< y

*%Y-a
{\]L)*

*1 for*

*= u >\_ y*

### in which the 3k ^\~ is t^e point, that is,

*parameter crossover*

*S(3;a,3,Y) 0.5. In this the implied attribute A(X) is Age(John)*

*= case,*

*and the translation of "John is young" assumes the form:*

*John is —> R(Age(John)) (2.7)*

*young = young .*

*To relate the concept of a fuzzy restriction to that of a possibility*

*distribution, we interpret the right-hand member of (2.4) in the following*

*manner.*

*Consider a numerical 28, whose grade of membership in*

*age, say u =*

*the fuzzy set (as defined by (2.5)) is approximately 0.7. First,*

*young we*

*interpret 0.7 as the degree of compatibility of 28 with the concept labeled*

*young. Then, we postulate that the proposition "John is young" converts*

*the meaning of 0.7 from the degree of compatibility of 28 with young to the*

*degree of possibility that John is 28 given the proposition "John is young."*

*In short, the compatibility of a value of u with young becomes converted*

*into the possibility of that value of u given "John is young."*

*Stated in more general terms, the concept of a possibility distribution*

*be defined follows. (For simplicity, that A(X) X.)*

*may as we assume =*

*Definition. Let F be a fuzzy subset of a universe of discourse U*

*which is characterized by its membership function uF, with the grade of*

*membership, yF(u), interpreted as the compatibility of u with the concept*

*labeled F.*

*Let X be a variable taking values in U, and let F act as a fuzzy*

*restriction, R(X), associated with X. Then the proposition "X is F,"*

*which translates into*

*R(X) = F , (2.8)*

*associates a possibility distribution, JI„, with X which is postulated*

*to be equal to R(X), i.e.,*

*nx = R(X) (2.9)*

*.*

*Correspondingly, the possibility distribution function associated with X*

*(or the possibility distribution function of IL,) is denoted by ttx and*

*is defined to be numerically equal to the membership function of F, i.e.,*

*ttx £(2.10)*

*yp .*

*Thus, ir„(u), the possibility that X = u, is postulated to be equal to*

*yp(u).*

*In view of (2.9), the relational assignment equation (2,8) be*

*may*

*expressed equivalently in the form*

*nx = F (2.11)*

*placing in evidence that the proposition p 4 X is F has the effect of*

*associating X with a possibility distribution IL. which, by (2.9), is*

*equal to F. When expressed in the form of (2.11), a relational assignment*

*equation will be referred to as a possibility association equation, with*

*the understanding that Ex is induced by p.*

*As a simple illustration, let U be the universe of positive integers*

*and let F be the fuzzy set of small integers defined by*

*small integer = 1/1 +1/2 +0.8/3 +0.6/4 +0.4/5 +0.2/6 (2.12)*

*.*

*Then, the proposition "X is a small integer" associates with X the possi*

*bility distribution*

*nx = 1/1+1/2 +0.8/3 +0.6/4 +0.4/5 +0.2/6*

*in which a term such as 0.8/3 signifies that the possibility that X is 3,*

*given that X is a small integer, is 0.8.*

*There are several important points relating to the above definition*

*which are in need of comment.*

*First, (2.9) implies that the possibility distribution nx may be*

*regarded as an interpretation of the concept of a fuzzy restriction and,*

*consequently, that the mathematical apparatus of the theory of fuzzy sets*

*— and, especially, the calculus of fuzzy restrictions \[ 4 \] -- provides*

*a basis for the manipulation of possibility distributions by the rules of*

*this calculus.*

*Second, the definition implies the assumption that our intuitive*

*perception of the ways in which possibilities combine is in accord with the*

*rules of combination of fuzzy restrictions. Although the validity of this*

*assumption cannot be proved at this juncture, it appears that there is a*

*fairly close agreement between such basic operations as the union and inter*

*section of fuzzy sets, on the one hand, and the possibility distributions*

*8*

*associated with the disjunctions and conjunctions of propositions of the*

*form "X is F." However, since our intuition concerning the behavior of*

*possibilities is not very reliable, a great deal of empirical work would*

*have to be done to provide us with a better understanding of the ways in*

*which possibility distributions are manipulated by humans. Such an under*

*standing would be enhanced by the development of an axiomatic approach to*

*the definition of subjective possibilities — an approach which might be*

*in the spirit of the axiomatic approaches to the definition of subjective*

*probabilities \[ 7 \], \[ 8 \].*

*Third, the definition of ttx(u) implies that the degree of possibility*

*be number in the interval \[0,1\] rather than just 0 1. In this*

*may any or*

*connection, it should be noted that the existence of intermediate degrees*

*of possibility is implicit in such commonly encountered propositions as*

*"There is slight possibility that Marilyn is rich," "It is quite*

### a very

*possible that Jean-Paul will be promoted," "It is almost impossible to find*

*a needle in a haystack," etc.*

*It could be argued, of course, that a characterization of an inter*

*mediate degree of possibility by a label such as "slight possibility" is*

*commonly meant to be interpreted as "slight probability." Unquestionably,*

*this is frequently the case in everyday discourse. Nevertheless, there is*

*a fundamental difference between probability and possibility which, once*

*better understood, will lead to a more careful differentiation between the*

*characterizations of degrees of possibility vs. degrees of probability --*

*especially in legal discourse, medical diagnosis, synthetic languages and,*

*more generally, those applications in which a high degree of precision of*

*meaning is an important desideratum.*

*To illustrate the difference between probability and possibility by*

*a simple example, consider the statement "Hans ate X eggs for breakfast,"*

*with X taking values in U = {1,2,3,4,...}. We associate possi*

*may a*

*bility distribution with X by interpreting 7rx(u) as the degree of ease*

*with which Hans can eat We also associate probability*

*u eggs. may a*

*distribution with X by interpreting px(u) as the probability of Hans*

*eating u eggs for breakfast. Assuming that we employ some explicit or*

*implicit criterion for assessing the degree of ease with which Hans can*

*eat for breakfast, the values of irx(u) and px(u) might be*

*u eggs as*

*shown in Table 1.*

*1 2 3 4 5 6 7 8*

*u*

###### TTX(U)

*1110.80.60.40.2*

*1*

*Px(u)0.10.80.100000*

*Table 1. The possibility and probability distributions*

*associated with X.*

*We observe that, whereas the possibility that Hans may eat 3 eggs for*

*breakfast is 1, the probability that he do might be quite small,*

*may so*

*e.g., 0.1. Thus, a high degree of possibility does not imply a high degree*

*of probability, nor does a low degree of probability imply a low degree of*

*possibility. However, if an event is impossible, it is bound to be improba*

*ble. This heuristic connection between possibilities and probabilities*

*may*

*be stated in the form of what might be called the possibility/probability*

*consistency principle, namely:*

*If a variable X can take the values u^,...,u with respective*

*possibilities tt =(^.....tt ) and probabilities p=(p^,... ,pp), then*

*the degree of consistency of the probability distribution p with the*

*10*

*possibility distribution ir is expressed by*

*Vl ""+Vn (2'13)*

*'*

*Y =+*

*It should be understood, of course, that the possibility/probability*

*consistency principle is not a precise law or a relationship that is intrin*

*sic in the concepts of possibility and probability. Rather it is an approxi*

*mate formalization of the heuristic observation that a lessening of the*

*possibility of an event tends to lessen its probability -- but not vice*

*versa. In this sense, the principle is of use in situations in which what*

*is known about a variable X is its possibility — rather than its probabil*

*ity — distribution. In such cases — which occur far more frequently than*

*those inwhichthe reverse is true — the possibility/probability consistency*

*principle provides a basis for the computation of the possibility distribution*

*of the probability distribution of X. Such computations play a particularly*

*important role in decision-making under uncertainty and in the theories of*

*evidence and belief \[ 9 \], \[ 10\], \[ 11 \], \[ 12\].*

*In the example discussed above, the possibility of X assuming a value*

*is interpreted as the degree of ease with which be assigned to*

*u u may*

*X, the degree of with which Hans eat for breakfast.*

*e.g., ease may u eggs*

*It should be understood, however, that this "degree of ease" not*

*may or may*

*have physical reality. Thus, the proposition "John is young" induces a*

*possibility distribution whose possibility distribution function is expressed*

*by (2.5). In this the possibility that the variable Age(John)*

*case, may*

*take the value 28 is 0.7, with 0.7 representing the degree of ease with*

*which 28 be assigned to Age(John) given the elasticity of the fuzzy*

*may*

*restriction labeled Thus, in this "the degree of ease" has*

*young. case a*

*figurative rather than physical significance.*

*11*

*If is proposition of the form 4 X is F which translates into*

*p a p*

*the possibility association equation*

*nA(x)-.F (2.14)*

*where F is a fuzzy subset of U and A(X) is an implied attribute of X*

*taking values in U, then the information conveyed by p, I(p), may be*

*identified with the possibility distribution, n.^x, of the fuzzy variable*

*A(X). Thus, the connection between I(p), IIwjq, R(A(X)) and F is*

*expressed by*

*Kp) AnA(x) (2.15)*

*where*

*nA(X) R(A(X)) (2-16)*

*'*

*==F*

*For example, if the proposition 4 John is translates into*

*p young*

*the possibility association equation*

*nAge(John) =youn9 (2-17)*

*where is defined by (2.5), then*

*young*

*KJohn is young) =nAge(John) (2.18)*

*in which the possibility distribution function of Age(John) is given by*

*irAge(John)(u) =1-S(u;20,30,40) , ue\[0,100\] (2.19)*

*.*

*definition it if is*

*^*

*From the of I(p) follows that X F and*

*p*

*£ X is G, then is at least informative expressed*

*q p as as q, as*

*I(p) I(q), if F c G. Thus, have partial ordering of the I(p)*

*\>\_ we a*

*defined by*

*12*

# I(X is F) > I(X is G) o FCG (2.20)

*which implies that the more restrictive a possibility distribution is, the*

*more informative is the proposition with which it is associated. For example,*

*since tall tall, have*

### very c we

*I(Lucy is tall) > I(Lucy is tall)-,*

*very*

*\3. N-Ary Possibility Distributions*

*In asserting that the translation of a proposition of the form*

*is is*

*^*

*p X F expressed by*

*X is F -> R(A(X)) = F (3.1)*

*or, equivalently,*

*Xis F-F-> nA(x) =F(3.2)*

*,*

*we are tacitly assuming that p contains a single implied attribute A(X)*

*whose possibility distribution is given by the right-hand member of (3.2).*

*More generally, contain implied attributes A,(X),...,A (X),*

*p may n*

*with A.(X) taking values in U., i = l,...,n. In this case, the transla*

*tion of 4 X is F, where F is fuzzy relation in the cartesian*

*p a*

*product*

*\* \* the form*

*u = U, ••• U , assumes*

*XisF-v R(A1(X),...,An(X)) =F (3.3)*

*or, equivalently,*

*x1sF^n(A1w--Vx»"F (3'4)*

*where RfA^X),... ,A (X)) is an fuzzy restriction and n^A (x),...,a (X))*

*n-ary*

*is an possibility distribution which is induced by Correspondingly,*

*n-ary p.*

*13*

*the n-ary possibility distribution function induced by, p is given by*

### %(« IL(X))(U1 Un} =y=yF{ul un} • l"y—»J 6U•

*(3.5)*

*where is the membership function of F. In particular, if F is*

*yp a*

*cartesian product of n fuzzy relations F.j,...,F then the right*

*unary*

*,*

*hand member of (3,3) decomposes into a system of n relational*

*unary*

*assignment equations, i.e.,*

*Xis F— F— RCA^X)) =F1 (3.6)*

###### R(A2(X)) = F2

*R(An(X)) = Fn*

*.*

*Correspondingly,*

**_n(A1(X),..,,An(X))=IIA1(X)X---xnAn(X) ^7)_**

*and*

**_"(A^X) An(X))(uV—un) -\\M^\] \\W{^ (3-8)_**

*where*

*irA (x)(u.) uF (u^ il,...,n (3.9)*

*=u. eU., =*

*,*

*and \* denotes min (in infix form).*

*As a simple illustration, consider the proposition p4 carpet is large,*

*in which large is a fuzzy relation whose tableau is of the form shown in*

*Table 2 (with length and width expressed in metric units).*

*6If F and G are fuzzy 
irelations in U and V, respectively, then their carte*

*sian product 
bFxG y 
is a fuzzy 
() 'relation in UxV whose y
membership function is*

*given p
by yp^^v) =vp(u) y 
'vUq(v).*

*14*

*large width length u*

*250 300 0.6*

*250 350 0.7*

*300 400 0.8*

*400 600 1*

*Table 2. Tableau of large.*

*In this the translation (3.3) leads to the possibility associa*

*case,*

*tion equation*

*(3,10)*

*... (width(carpet),length(carpet))*

*n,... (wi"*

*arge*

*which implies that if the compatibility of a carpet whose width is,*

*say,*

*250 cm and length is 350 cm with "large carpet" is 0.7, then the possibility*

*that the width of the carpet is 250 cm and its length is 350 cm — given*

*the proposition p 4 carpet is large — is 0.7.*

*Now, if large is defined as*

*large = widex long (3.11)*

*where long and wide are fuzzy relations, then (3.10) decomposes into*

*unary*

*the possibility association equations*

*nwidth(carpet) =w1de*

*and*

*nlength(carpet) =long*

*where the tableaux of long and wide are of the form shown in Table 3.*

*15*

*long length*

*wide width y*

y

*300 0.6*

*250 0.6*

*350 0.7*

*300 0.7*

*400 0.8*

*350 0.8*

•

*500 1*

*400 1*

*Table 3. Tableaux of wide and long.*

*Marginal Possibility Distributions*

*The concept of a marginal possibility distribution bears a close rela*

*tion to the concept of a marginal fuzzy restriction \[ 4 \], which in turn*

*is analogous to the concept of a marginal probability distribution.*

*More specifically, let X=(X\] Xn) be an n-ary fuzzy variable*

*taking values in U=U-, xxUn, and let nx be apossibility distribu*

*...*

*tion associated with X, with irx(ur...,un) denoting the possibility*

*distribution function of II...*

*qk(ir...»ik) be index*

*Let qkasubsequence of the sequence (l,...,n)*

*and let X, be the fuzzy variable X^ £(X.. ,...,Xi ). The*

*x q-ary*

*marginal possibility distribution nx is a possibility distribution*

*associated with X/ x which is induced by nx as the projection of nxon*

*U, x A u. x...xu. Thus, by definition,*

*.*

**_(q) ">! \\_**

*"*

*(3.12)*

*£ Proj,, n*

*n,*

*l(q)(q)*

*which implies that the probability distribution function of X^ j is related*

*to that of X by*

*(3.13)*

*(q) u(ql) X*

IT.

*(q)*

*16*

**_xk {u. ,...,ui_**

*where u, xk ), q' £(j-,,...,Jm) is asubsequence of (l,...,n)*

*which is complementary to (e.g., if n= 5 and £ (i-j,i2) (2,4),*

*q q*

*=*

*then q' = (j\\,j?,jo) 
12 3 = (1,3,5), u, .x 
) 4 (u. 
j,...,u. 
\3) and V 
udenotes*

### \\,j?
12 o) 
3 (q x 
) . 
j1 . 
3m V 
u(q()

*the (u. ) e U. x««'xU.*

*supremum over ,...,u. .*

*Jl Jm Jl Jm*

*As a simple illustration, assume that U, = U„ = Ug = {a,b} and the*

*tableau of IL. is given by*

*x2*

*TT*

#### h h X3

*a a 0.8*

*a*

*a b 1*

*a*

*b a a 0.6*

*b b 0.2*

*a*

*b b b 0.5*

*Table 4. Tableau of nx.*

*Then,*

*= "^U
Proj,, ^X
nv = l/(a,a)+0.6/(b,a) +0.5/(b,b) (3.14)*

*(xrx2) "^U^U^X
Proj,, .. nv*

*n " U
..*

*which in tabular form reads*

*n(xrx2)*

*TT*

#### xl h

*a 1*

*a*

*b 0.6*

*a*

*b b 0.5*

(xrx2r

*Table 5. Tableau of n*

*17*

*Then, from nx it follows that the possibility that X, = b, X„ = aand*

*X3 = b is 0.2, while from 11/x x x it follows that the possibility of*

*X1 = b and X2 = a is 0.6.*

*By analogy with the concept of independence of random variables, the*

*fuzzy variables X,nx (x. ,...,X. ) and X, £ (X. )*

*g .x are*

*,*

*noninteractive if and only if the possibility distribution associated with*

*X = (X,,...,X ) is the cartesian product of the possibility distributions*

*associated with X/ x and X/ ,x, i.e.,*

*nv = nv xnv (3.15)*

*X X(q) X(q')*

*or, equivalently,*

*TTY(u1f...,u 
X 1 ) = 
n irY 
X(u. 
i,...,u. 
i)\*tty 
k X(u. 
3,...,u. 
j) . (3.16)*

#### TTY(u1f...,u ) 
X 1 n rY 
X(q) . 
i} . )
ik y 
X(ql) u. 
3} u. 
jm

*In particular, the variables X,,...,X are noninteractive if and only if*

*nY xl x...xl (3.17)*

*n„*

*=*

*.*

*A Ai A/> A\_*

### I l n

*The intuitive significance of noninteraction be clarified by a*

*may*

### simple k (X,,X2), noninter

*example. Suppose that Xand X. and X« are*

*active, i.e.,*

*7rX^uTu2^ ^X ^"l'^X ^u2^ (3.18)*

*'*

*=*

*Furthermore, suppose that for some particular values of u, and u«,*

*irx (u,) ttx (u2) a2 \< and hence Trx(u, ,u„) Now, if the*

*a,, a, cu.*

*===*

*value of TT (u,) is increased to a,+6.., 6, > 0, it is not possible to*

*decrease the value of it.. (u2) by a positive amount, 62, such that*

*say*

*the value of tfv(u,,u2) remains unchanged. In this increase in*

*sense, an*

*18*

*the possibility of u, cannot be compensated by a decrease in the possibility*

*of u?, and vice-versa. Thus, in noninteraction be viewed*

*essence, may as*

*a form of noncompensation in which a variation in one or more components of*

*a possibility distribution cannot be compensated by variations in the comple*

*mentary components.*

*In the manipulation of possibility distributions, it is convenient to*

*employ a type of symbolic representation which is commonly used in the case*

*of fuzzy sets. Specifically, assume, for simplicity, that U.j,...,Un are*

*finite and let r1 4-(r\],...,r^) denote*

*sets, an n-tuple of values drawn*

*from U,,...,U respectively. Furthermore, let -ft., denote the possibility*

*,*

*of r1 and let the n-tuple (r\],...,rj) be written as the string r\]---rj.*

*Using this notation, a possibility distribution nx may be expressed*

*in the symbolic form*

N 
I

### nY 
X = N 
I 
^i ir,rr...r 
i 1 2 (3.19)

*Y 
X I 
.^i r
i rr...r 
1 2 n*

*in separator symbol is needed,*

*or, case a as*

nx-j1vrir2-ri (3-2o)

*where N is the number of n-tuples in the tableau of nx> and the summa*

*tion should be interpreted as the union of the fuzzy singletons ^/(^,... ,rn)*

*As an illustration, in the notation of (3.19), the possibility distribution*

*defined in Table 4 reads*

*nY =0.8 aaa + 1aab + 0.6 baa + 0.2 bab + 0.5 bbb (3.21)*

*.*

*The advantage of this notation is that it allows the possibility*

*distributions to be manipulated in much the same manner as linear forms in*

*19*

*n variables, with the understanding that, if r and s are*

*and a and $ are their respective possibilities, then*

*ar + $r = (av $)r*

*ar n 3r = (a\*$)r*

*and ar x $s = (a-3)rs*

*where rs denotes the concatenation of r and s. For*

*nx =0.8 aa +0,5ab +1bb*

*and*

*0.9 ba +0.6bb*

*ny*

*=*

*then*

*nx +0.8 +0.5ab +0.9 ba +1bb*

*ny aa*

*=*

*nx 0.6bb*

*nny*

*=*

*and L x i = 0.8aaba + 0.5 abba + 0.9bbba*

*\+ 0.6aabb + 0.5abbb + 0.6bbbb*

*.*

*To obtain the projection of a possibility distribution*

*U/ \\ 4 (U. ,...,U. ), it is sufficient to set the values of*

*in each tuple in nx equal to unity (i.e., multiplicative*

*an illustration, the projection of the possibility distribution*

*Table 4 on U-j xU« is given by*

*Proj., nY = 0.8 aa + 1aa + 0.6 ba + 0.2 ba + 0.5*

*„*

1\*9

*= 1 aa + 0.6 ba + 0.5 bb*

*which with Table 5.*

*agrees*

*two tuples*

*(3.22)*

*(3.23)*

*(3.24)*

*example, if*

*(3.25)*

*(3.26)*

*(3.27)*

*(3.28)*

*(3.29)*

*JIX on*

*X. ,...,X.*

*identity). As*

*defined by*

*bb (3.30)*

*20*

*Conditioned Possibility Distributions*

*In the theory of possibilities, the concept of a conditioned possibility*

*distribution plays a role that is analogous — though not completely — to*

*that of a conditional possibility distribution in the theory of probabilities.*

*More concretely, let avariable X= (X.j,...,X ) be associated with*

*a possibility distribution Ify, with nx characterized by a possibility*

*distribution function irJu,,... ,un) which assigns to each n-tuple (u1,...,un)*

*in U,x---xU its possibility ^x(u-j "n)»*

*Let (ir...,ik) and (J1 Jm) be subsequences of the*

*qs*

*==*

*index (l,...,n), and let (a. ) be n-tuple of values*

*sequence ,...,a. an*

*Jl Jm*

*assigned to X,,x 
) = (X. ,...,X. ). By definition, the conditioned*

### xq ) J-j Jm

*possibility distribution of X/ 4(X. ,...,Xi ) given X^q,x (a.. )*

*x,...,a..*

*=*

*i i\\ i in*

*is a possibility distribution expressed as nY \[X. 
^=a. ;...;X. 
J=a. \]*

*Y 
x(q) . 
^1 . 
Jl Jm Jm*

*whose possibility distribution function is q
given by7*

*irv (u. IX. =a. ;...;X. =a. ) (3.31)*

*,...,u.*

*\*(q) nl nk> Jl Jl Jm Jm*

*Airx(ur...,un)*

*u. =a. ,...,u. =a.*

*Jl Jl Jm Jm*

*As a simple example, in the case of (3.21), we have*

*n(x x)^xi=a-' =0,8aa +\]ab ^3'32^*

## Cm O

*as the expression for the conditioned possibility distribution of (X2>X3)*

*given X, = a.*

*7In some applications, it may be appropriate to normalize the expression*

*for the conditioned possibility distribution function by dividing the*

*riqht-hand member of (3.31) by its supremum over U. x xu.*

*... .*

*3 H 'k*

*21*

*An equivalent expression for the conditioned possibility distribution*

*which makes clearer the connection between IIY \[X. =a. ;X. =a. \]*

*;...*

*\*(q) Jl Jl Jm Jm*

*and n„ be derived follows.*

*may as*

*Let nY\[X. =a. ;...;X. =a.\] denote a possibility distribution which*

*consists of those terms in (3.19) in which the j,-th 
I element is a. 
Jthe*

*,*

*,
I . 
J-,*

*j0-th 
L element is a. and the j 
m -th element is a. For example,*

*,..., .*

### 0
L . 
J2 j 
m Jm

*in the case of (3.21)*

*nx\[X1 =a\] =0.8 aaa +1aab (3.33)*

*.*

*Expressed in the above notation, the conditioned possibility distribu*

*tion of X, (X, ,...,X. ) given X. =a. ,...,X. =a. be written*

*x may*

*=*

*as*

*nY \[X. =a. ;...;X. =a. \] = Proj,, n„\[X. =a. ;...;X. =a. \] (3.34)*

*X(q) Jl 31 U(q)*

*\**

*Jm Jm Jl Jl Jm Jm*

*which places in evidence that IIX (conditioned on X/x =a/x) is a*

*marginal possibility distribution induced by nx (conditioned on x(s)=a(s))'*

*Thus, by employing (3.33) and (3.34), we obtain*

*)^X1 sa^ °'8aa ^3'35^*

*n(X X=+\]ab*

*which with (3.32).*

*agrees*

*In the foregoing discussion, we have assumed that the possibility*

*distribution of X = (X,,...,X ) is conditioned on the values assigned to*

*a specified subset, X/ x, of the constituent variables of X. In a more*

*general setting, what might be specified is a possibility distribution*

*associated with X/^x 
irather than the values of X. 
J,...,X. 
JIn such*

*.*

*/x 
is; . 
J1 . 
Jm*

*22*

*8*

*cases, we shall that is particularized by specifying that G,*

*say nv nv =*

*\**

*X X(s)*

*where G is a given possibility distribution. It should be noted*

*m-ary*

*that in the present context n„ is a given possibility distribution*

*X(s)*

*rather than a marginal distribution that is induced by IL..*

*To analyze this case, it is convenient to assume -- in order to simplify*

*the notation — that X. =X,, X. =X9,...,X. =X m \< n. Let G denote*

*,*

*Jl J2*

*'*

# c Jm m

*the cylindrical extension of G, that is, the possibility distribution*

*defined by*

*G£GxUm+1x...xUn (3.36)*

*which implies that*

*yg(u1,...,un) iyG(uls...,um) eU., j=l,...,n, (3.37)*

*u.*

*,*

*where is the membership function of the fuzzy relation G.*

*yp*

*The assumption that we are given IL. and G is equivalent to assuming*

*that we are given the intersection IL.HG. From this intersection, then,*

*we can deduce the particularized possibility distribution nv \[nY =G\]*

*X(q) X(s)*

*by projection on U/ x. Thus,*

*nY \[nY =G\] = Proj.. nYng (3.38)*

*.*

*X(q) X(s) U(q) X*

*Equivalently, the left-hand member of (3.38) may be regarded as the compo*

*sition of nx and G \[5\].*

*As a simple illustration, consider the possibility distribution defined*

*by (3.21) and assume that*

*G =• 0.4 aa + 0.8 ba + 1 bb (3.39)*

*.*

*8In the case of nbnfuzzy relations,particularization is closely related to*

*what is commonly referred to as restriction. We are not employing this*

*more conventional term here because of our use of the term "fuzzy restric*

*tion" to denote an elastic constraint on the values that be assigned*

*may*

*to a variable.*

*Then*

*G = 0.4 aaa +*

*LOG = 0.4 aaa +*

A

*n*

*and*

*As an elementary*

*A John is big, where*

*p*

*in Table 6 (with height*

*Now, that*

*suppose*

*that £ John is tall,*

*q*

*tabulated form) by Table*

*23*

*0.4 aab + 0.8 baa + 0.8 bab + 1bba + 1bbb (3.40)*

*0.4 aab + 0.6 baa + 0.2 bab + 0.5 bbb (3.41)*

*\[II/X x x=G\] =0.6a + 0,5b (3.42)*

*.*

*application of (3.38), consider the proposition*

*big is a relation whose tableau is of the form shown*

*and weight expressed in metric units).*

*big height weight*

y

*170 70 0.7*

*170 80 0.8*

*180 80 0.9*

*190 90 1*

*Table 6. Tableau of big.*

*in addition to knowing that John is big, we also know*

*where the tableau of tall is given (in partially*

*7.*

*tall height*

y

*170 0.8*

*180 0.9*

*190 1*

*Table 7. Tableau of tall.*

*24*

*The question is: What is the weight of John? By making use of (3.38),*

*the possibility distribution of the weight of John may be expressed as*

*Vight =Projweight n(height,weight)\[nheight =t=tall\] (3\*39)*

*= 0.7/70 + 0.9/80 + 1/90*

*.*

*An acceptable linguistic approximation \[5\], \[13\] to the right-hand side of*

*(3.39) might be "somewhat heavy," where "somewhat" is a modifier which has*

*a specified effect on the fuzzy set labeled "heavy." Correspondingly, an*

*approximate answer to the question would be "John is somewhat heavy."*

*\4. Possibility Distributions of Composite and Qualified Propositions*

*As was stated in the Introduction, the concept of a possibility*

*distribution provides a natural for defining the meaning well*

*way as as*

*the information content of a proposition in a natural language. Thus, if*

*is proposition in natural language NL and M is its meaning,*

*p a a*

*then M be viewed procedure which acts set of relations in*

*may as a on a*

*a universe of discourse associated with NL and yields the possibility*

*distribution of a set of variables or relations which are explicit or*

*implicit in p.*

*In constructing the meaning of n given propositions, it is convenient*

*to have a collection of what might be called conditional translation rules*

*\[14\] which relate the meaning of a proposition to the meaning of its modi*

*fications or combinations with other propositions. In what follows, we*

*shall discuss briefly some of the basic rules of this type and, in particular,*

*will formulate a rule governing the modification of possibility distributions*

*by the possibility qualification of a proposition.*

*25*

*Rules of Type I*

*Let p be a proposition of the form Xis F, and let m be amodi*

*fier such as quite, rather, etc. The so-called modifier rule \[6\]*

*very,*

*which defines the modification in the possibility distribution induced by*

*be stated follows.*

*p may as*

*If*

*XisF-nA(x) =F (4.1)*

*then*

**_-\*_**

*XiXis mF II^jq =F=F+ (4.2)*

*where A(X) is an implied attribute of X and F is a modification of*

*F defined by m.9 For example, if mthen F Fif*

*very, ;*

*==*

*m4more or less then F+ =vf; and if m=not then F+ =F' £comple*

*ment of F. As an illustration:*

*If*

# John is —> nAge(John) (4.3)

*young =young*

*=y*

*then*

*2*

*John is*

*-\**

# very young nAge(John) =young

*.*

*In particular, if*

*young = 1 - S(20,30,40) (4.4)*

*then*

*young2 =(1 -S-S(20,30,40))2*

*where the S-function (with its argument suppressed) is defined by (2.6).*

*9A more detailed discussion of the effect of modifiers (or hedges) be*

*may*

*found in \[15\], \[16\], \[17\], \[8\], \[6\], \[13\] and \[18\].*

*26*

*Rules of Type II*

*If p and q are propositions, then r 4 p\*q denotes a proposition*

*which is a composition of p and The three most commonly used modes*

*q.*

*of composition are (i) conjunctive, involving the connective "and";*

*(ii) disjunctive, involving the connective "or"; and (iii) conditional,*

*involving the connective "if...then." The conditional translation rules*

*relating to these modes of composition are stated below.*

*Conjunctive (noninteractive): If*

*Xis F-F->-nA(xx =F (4.5)*

*and*

*Yis G-\*nB(Y) =G (4-6)*

*then*

*X is Fand Y is G-> n#A#x% g/yxx =FxG (4.7)*

*where A(X) and B(Y) are the implied attributes of X and Y,*

*respectively, II/A/xx B(Yu 1S tne possibility distribution of the variables*

*A(X) and B(Y), and FxG is the cartesian product of F and G. It*

*should be noted that FxG may be expressed equivalently. as*

###### FxG = F HG (4.8)

*where F and G are the cylindrical extensions of F and G, respectively*

*Disjunctive (noninteractive): If (4.5) and (4.6) hold, then*

*Xis ForY isG-n(A(x)>B(Y)) =F+G (4.9)*

*where the symbols have the same meaning as in (4.5) and (4.6), and +*

*denotes the union.*

*27*

*Conditional (noninteractive): If (4.5) and (4.6) hold, then*

*If Xis Fthen Yis G— n(A(X),B(Y)) =F'®G (4J0)*

*where F\* is the complement of F and © is the bounded sum defined by*

*•Wg-^-i'f+V (4J1)*

*in which + and - denote the arithmetic addition and subtraction, and*

*yF and y« are the membership functions of F and G, respectively.*

*Illustrations of these rules -- expressed in terms of fuzzy restrictions*

*rather than possibility distributions — may be found in \[6\] and \[14\].*

*Truth Qualification, Probability Qualification and Possibility Qualification*

*In natural languages, an important mechanism for the modification of*

*the meaning of a proposition is provided by the adjunction of three types*

*of qualifiers: (i) is t, where t is a linguistic truth-value, e.g.,*

*true, very true, more or less true, false, etc.,; (ii) is X, where X is*

*a linguistic probability-value (or likelihood), e.g., likely, very likely,*

*very unlikely, etc.; and (iii) is tt, where tt is a linguistic possibility*

*value, e.g., possible, quite possible, slightly possible, impossible, etc.*

*These modes of qualification will be referred to, respectively, as truth*

*qualification, probability qualification and possibility qualification.*

*The rules governing these qualifications may be stated as follows.*

*Truth qualification: If*

*Xis F-> nA/x^ =F (4.12)*

*then*

*X is F is t —\*• nA/xx = F*

*28*

*where*

*uF+(u) =yT(yp(u)) , u eU ; (4.13)*

*y and yF are the membership functions of t and F, respectively,*

*and U is the universe of discourse associated with A(X). As an illus*

*tration, if young is defined by (4.4); x = very true is defined by*

*true S2(0.6,0.8,l) (4.14)*

### very

*=*

*and*

*John is nAge(John) (4,15)*

*young =young*

*— =y*

*then*

*+*

*John is is true -\*• nAge(Jonn)*

*young very young*

*=*

*where*

*young+(u) =S2(l-S(u;20,30,40);0.6,0.8,l) , ueU.*

*yo*

*=S*

*Probability qualification: If*

*Xis F-• nA/xx =F (4.16)*

*then*

*X is F is X -\* n = X (4.17)*

*Ip(u)yF(u)du*

# JU r

*where p(u)du is the probability that the value of A(X) falls in the*

*interval (u,u+du); the integral*

*p(u)yP(u)du*

*U h*

*is the probability of the fuzzy event F \[19\]; and X is a linguistic*

*probability-value. Thus, (4.17) defines a possibility distribution of*

*probability distributions, with the possibility of a probability density*

*29*

*p(«) given by*

*p(u)yp(u)du| (4.18)*

*tt(pH) =yx .*

*As an illustration, consider the proposition p4 John is young is very*

*likely, in which young is defined by (4.4) and*

*u 
\*\\,.,,," 
likely S2(0.6,0.8,l) 
v(4.19)*

*.*

*u 
\*\\ery ,.,,,
likely v*

*Then*

*100*

*p(u) (1 S(u;2Q,30,40)du);0.6,0.8,1 (4.20)*

*.2*

*-*

*ir(p(0) S1*

*• .*

*0*

*Possibility qualification: If*

*(4.21)*

*X1sF-\*nA(X) =F*

*then*

# X is F is possible -+ nA#y\\ = F

*in which*

*(4.22)*

*F = F © n*

*where is 2°defined*

*H afuzzy set of Type by*

*yn(u) =\[0,1\] , ueU , (4.23)*

*and © is the bounded sum defined by (4.11). Equivalently,*

*Up+(u) =\[yp(u),l\] , u eU , (4.24)*

*which defines yF+ as an interval-valued membership function.*

*10The membership function of a fuzzy set of Type 2 takes values in the set*

*of fuzzy subsets of the unit interval \[5\], \[6\].*

*30*

*In effect, the rule in question signifies that possibility qualifica*

*tion has the effect of weakening the proposition which it qualifies through*

*the addition to F of a possibility distribution n which represents*

*total indeterminacy in the sense that the degree of possibility which it*

*associates with each point in U be number in the interval \[0,1\].*

*may any*

*An illustration of the application of this rule to the proposition 4 X*

*p*

*is small is shown in Figure 1.*

*As an extension of the above rule, we have: If*

*is (4.25)*

*F-\**

*XF-nA(xx =F*

*then, for 0 \< a \< 1,*

*is is a-possible (4.26)*

*—\**

###### X FHA(X) = F

*where F+ is a fuzzy set of Type 2whose interval-valued membership function*

*is given by*

*yF+(u) =\[a-yp(u), a©(l-yF(u))\] , ueU . (4.27)*

*As an illustration, the result of the application of this rule to the propo*

*sition 4 X is small is shown in Figure 2. Note that the rule expressed*

*p*

*by (4.24) may be regarded as a special case of (4,27) corresponding to*

*a = 1.*

*A further extension of the rule expressed by (4.25) to linguistic*

*possibility-values may be obtained by an application of the extension prin*

*ciple, leading to the linguistic possibility qualification rule:*

*11n may be interpreted as the possibilistic counterpart of white noise.*

*31*

*If*

*is (4.28)*

*F-\**

*XF-nA(x) =F*

*then*

*X is F is 7r-possible —• IU/yx = F*

*where F+ is a fuzzy set of Type 2whose membership function is given by*

*VpCu) =(>o(TT^yF(u)))n(\<o(7T©(l.vlF(u)))) (4.29)*

*where tt is the linguistic possibility (e.g., quite possible, almost*

*impossible, etc.) and © denotes the composition of fuzzy relations. The*

*statement of this rule should be regarded as provisional in nature, since*

*the implications of a linguistic possibility qualification are not as yet*

*fully understood.*

*An interesting aspect of possibility qualification relates to the*

*invariance of implication under this mode of qualification. Thus, from the*

*definition of implication \[ 6 \], ist follows at once that*

*X is F =\* X is G if F c G . (4.30)*

*Now, it can readily be shown that*

*FC G => F+ C G+ (4.31)*

*where c in the right-hand member of (4.31) should be interpreted as the*

*relation of containment for fuzzy sets of Type 2. In of (4.31),*

*consequence*

*then, we can assert that*

*X is F is possible => X is G is possible if F c G . (4.32)*

*32*

*\5. Concluding Remark*

*The exposition of the theory of possibility in the present paper*

*touches only few of the facets of this yet largely unexplored*

*upon a many -- as*

*-- theory. Clearly, the intuitive concepts of possibility and probability*

*play a central role in human decision-making and underlie much of the human*

*ability to reason in approximate terms. Consequently, it will be essential*

*to develop a better understanding of the interplay between possibility and*

*probability -- especially in relation to the roles which these concepts*

*play in natural languages -- in order to enhance our ability to develop*

*machines which can simulate the remarkable human ability to attain impre*

*cisely defined goals in a fuzzy environment.*

*Acknowledgment*

*The idea of employing the theory of fuzzy sets as a basis for the*

*theory of possibility was inspired by the paper of B.R, Gaines and L. Kohout*

*on possible automata \[ 1 \]. In addition, our work was stimulated by*

*discussions with H\*J. Zimmermann regarding the interpretation of the*

*opera*

*tions of conjunction and disjunction; the results of a psychological study*

*conducted by Eleanor Rosch and Louis Gomez; and discussions with Barbara*

*Cerny.*

*33*

*References*

*\[I\] B.R. Gaines and L.J. Kohout, 
iPossible automata, 
liProc. Int. Symp. 
183on*

*Multiple-Valued Logic, , 
Univ. of Indiana, , 
Bloomington, Ind., yp
183-19F*

*(1975).*

*\[2\] G.E. Hughes and M.J. Cresswell, An Introduction to Modal Logic, Methuen,*

*London (1968).*

*\[3\] A. Kaufmann, Valuation and probabilization, in Theory of Fuzzy Subsets,*

*Vol. 5, A. Kaufmann and E. Sanchez, Masson and Co., Paris (1977T*

*\[4\] L.A. Zadeh, Calculus of fuzzy restrictions, in Fuzzy Sets and Their*

*Applications to Cognitive and Decision Processes, L.A. Zadeh, K.S. Fu,*

*K. Tanaka and M. Shimura, eds., 1-39, Academic Press, New York (1975).*

*\[5\] L.A. Zadeh, The concept of a linguistic variable and its application*

*to approximate reasoning, Part I, Inf. Sci. 8, 199-249 (1975);*

*Part II, Inf- M- §., 301-357 (1975)7 Part III, Inf. Set. 9, 43-80*

*(1975).*

*\[6\] R.E. Bellman and L.A. Zadeh, Local and fuzzy logics, ERL Memo. M-584,*

*Univ. of Calif., Berkeley (1976). To in Modern Uses of*

*appear*

*Multiple-Valued Logics, D. Epstein, ed., D. Reidel, Dordrecht (1976).*

*\[7\] B. DeFinetti, Probability Theory, J. Wiley, New York (1974).*

*\[8\] T. Fine, Theories of Probability, Academic Press, New York (1973).*

*\[9\] A. Dempster, Upper and lower probabilities induced by multi-valued*

*mapping, Ann. Math. Statist. 38, 325-339 (1967).*

*\[10\] G. Shafer, A Mathematical Theory of Evidence, Princeton University Press,*

*Princeton (1976).*

*\[II\] E.H. Shortliffe, A model of inexact reasoning in medicine, Math.*

*Biosciences 23, 351-379 (1975).*

*\[12\] R.O. Duda, P.F. Hart and N.J. Nilsson, Subjective Bayesian methods for*

*rule-based inference systems, Stanford Research Institute Tech. Note 124,*

*Stanford (1976).*

*\[13\] F. Wenstop, Deductive verbal models of organization, Int. Man-Machine*

*J\_.*

*Studies 8, 293-311 (1976).*

*\[14\] L.A. Zadeh, Theory of fuzzy sets, Memo. No. UCB/ERL M77/1, University of*

*California, Berkeley (1977).*

*\[15\] L.A. Zadeh, A fuzzy-set-theoretic interpretation of linguistic hedges,*

*J. Cybernetics 2, 4-34 (1972).*

*34*

*\[16\] G. Lakoff, Hedges: a study in meaning criteria and the logic of fuzzy*

*concepts, Phil. Logic 2, 458-508 (1973). Also presented*

*J\_. paper*

*at 8th Regional Meeting of Chicago Linguistic Soc. (1972) and in*

*Contemporary Research in Philosophical Logic and Linguistic Semantics,*

*D. Hockney, W. Harper and B". Freed, eds., 221^71, D\~ Reidel, The*

*Netherlands (1975).*

*\[17\] H.M. Hersch and A. Carramazaa, A fuzzy set approach to modifiers and*

*in natural languages, Dept. of Psych., The Johns Hopkins Univ.,*

*vagueness*

*Baltimore, Md. (1975).*

*\[18\] P.J. MacVicar-Whelan, Fuzzy sets, the concept of height and the hedge*

*very, Tech. Memo 1, Physics Dept., Grand Valley State Colleges,*

*Allendale, Mich. (1974),*

*\[19\] L.A. Zadeh, Probability measures of fuzzy events, »h Math. Anal. Appl.*

*23, 421-427 (1968).*

*\[20\] M. Sugeno, Theory of fuzzy integrals and its applications, Ph.D. Thesis,*

*Tokyo Institute of Technology, Tokyo (1974).*

*\[21\] W. Rodder, On 'and1 and 'or' connectives in fuzzy set theory,*

*Inst, for Oper. Res., Tech. Univ. of Aachen, Aachen (1975).*

*\[22\] L.A. Zadeh, K.S. Fu, K. Tanaka and M. Shimura, eds., Fuzzy Sets and*

*Their Applications to Cognitive and Decision Processes, Academic*

*Press, New York (1975).*

*\[23\] E. Mamdani, Application of fuzzy logic to approximate reasoning*

*using linguistic synthesis, Proc. 6th Int. Symp. on Multiple-Valued*

*Logic, Utah State Univ., Logan, Utah, T96-20FT1976).*

*\[24\] V.V. Nalimov, Probabilistic model of language, Moscow State Univ.,*

*Moscow (1974).*

*\[25\] J.A. Goguen, Concept representation in natural and artificial languages:*

*axioms, extensions and applications for fuzzy sets, Int. JL Man-Machine*

*Studies 6, 513-561 (1974).*

*\[26\] C.V. Negoita and D.A. Ralescu, Applications of Fuzzy Sets to Systems*

*Analysis, Birkhauser Verlag, Basel and Stuttgart (197511*

*Fig. 1. The possibility*

*"X is small*

*Ismail*

*Ismail*

*distribution of*

*is possible".*

Fig. 2. The

"X is small

possibility distribution of

is a-possible".
