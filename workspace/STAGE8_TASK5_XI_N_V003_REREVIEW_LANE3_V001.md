# STAGE 8 TASK 5 — RE-REVIEW OF XI_N V003

Lane: CODEX LANE 3 (SOL, HIGH EFFORT)  
Version: V001  
Date: 2026-08-05  
Task: PASTE 588  
Custody: cross-family re-review; the adoption ruling follows only on confirmation  
Scope: symbolic determination only

## Lead verdict

[YOURS — determination] V003 closes the old A7 tautology, the cross-carrier unit
transfer, the false cycle-creating seal claim, and the stale linear winding
calculation. The rank-preserving and cycle-creating squares now have the right
directions and gated source types.

It is nevertheless DEFECTIVE at adoption strength. The decisive defects are
structural rather than editorial:

1. the V002 anti-counterterm law (Y9), and with it the full D-side/cycle-side
   support bridge G4, disappears from V003;
2. Z3's constancy on every fixed-support stratum silently restores
   Xi_N(-x)=Xi_N(x) unless the still-untyped strata carry a signed/oriented
   refinement, so the negative-scale collapse re-enters through a different
   clause;
3. the redone winding calculation is correct, but V003's conclusion that the
   character necessarily jumps at the origin is false when the period lies in
   2 pi Z — exactly the identity-branch case Z-A7 requires;
4. the support-birth theorem omits the positive-scale support-stability premise,
   and the status phrase "continuous extension through 0 is not defined" is not
   the correct boundary for a map already defined at 0;
5. the void suite is not carried into the superseding clause set, and several
   verbs in the candidate's self-audit exceed the displayed premises.

~~~text
R1 Z-A7                         = PASS
R2 Z3                           = KILL AS WRITTEN
R3 zero-homogeneous calculation = PASS
R3 character-jump conclusion    = KILL AS WRITTEN
R3 G2 whole-image rebase        = PASS IN SUBSTANCE / G2-vs-G2-N BOOKING DEFECT
R4 native units                 = PASS
R4 rank-preserving square       = PASS AS GATED CONDITION
R4 cycle-creating square        = PASS AS GATED CONDITION / DISPLAY RESIDUE
R5 five disclosed defects       = 1-4 CLOSED IN THEIR ORIGINAL FORMS;
                                  5 WITHDRAWN BUT ITS REPLACEMENT IS DEFECTIVE
SIXTH DEFECT                    = Y9/full-G4 anti-counterterm law omitted
FRESH HORN                      = fixed-support constancy restores sign-evenness

MEMBER_BOUND = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false
MEASURED_CONSTANT_COMPARISON = none
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
~~~

## 0. Preflight

### 0.1 No-clobber and register

[PROVABLE — access check] Before construction, neither
STAGE8_TASK5_XI_N_V003_REREVIEW_LANE3_V001.md nor its seal existed in the
Lane-3 cleanroom or alpha-program-archive/workspace.

[PROVABLE — register] Before review work, the questions-settled register ended
at Q-514 before its usage footer. Q-514 records the seams V002 return. No later
row was consumed, and this lane performed no register action.

[PROVABLE — seal-time drift check] During this review, Q-515 was appended for
the independent seams-V002 confirmation relay. It postdates this review's
required Q-514 start, concerns the separate R9/carriage artifact, and supplies
no premise used by the Xi_N V003 verdict. It was observed but not consumed as
an authority. The start preflight therefore remains Q-514 exactly.

### 0.2 Input verification

[PROVABLE — seal check] The artifact under review was verified before reading:

~~~text
STAGE8_TASK5_XI_N_CANDIDATE_DARIO_V003.md
lines   = 398
SHA-256 = d8f5112951c5378ce10126f91e8c89d0f31ebaae7ba6477677c9beb17b979e6c
sidecar = matching
mirror  = byte-identical
~~~

[PROVABLE — standard check] My own defect-list standard was also verified:

~~~text
STAGE8_TASK5_XI_N_V002_REREVIEW_LANE3_V001.md
SHA-256 = ef2e4e8ec0d90562838d2ba7a52c9334eccb6b89e10075efd9655b7cd961f76a
sidecar = matching
~~~

The directly used authority ledger is:

| Key | Authority | SHA-256 |
|---|---|---|
| XI-V3 | STAGE8_TASK5_XI_N_CANDIDATE_DARIO_V003.md | d8f5112951c5378ce10126f91e8c89d0f31ebaae7ba6477677c9beb17b979e6c |
| XI-V2 | STAGE8_TASK5_XI_N_CANDIDATE_DARIO_V002.md | 7958b54d9964f387750f70a52bcaf869dded9fbe3df5e6c14a53255e94ca18c4 |
| XI-R2 | STAGE8_TASK5_XI_N_V002_REREVIEW_LANE3_V001.md | ef2e4e8ec0d90562838d2ba7a52c9334eccb6b89e10075efd9655b7cd961f76a |
| XI-R1 | STAGE8_TASK5_XI_N_REVIEW_AND_DISPLAYS_LANE3_V001.md | c9b62076cc07951ec26fcf4aa4c15e21ec973f6089fb83ca476a98b83aefd071 |
| COMMON | STAGE8_TASK5_COMMON_SEAMS_LANE3_V001.md | 5de94e16db09b982f85fdf117281af62df6ab0d05c9e7577ac258d47594b69b7 |
| COMMON-V2 | STAGE8_TASK5_COMMON_SEAMS_LANE3_V002.md | 2525096ba06973b70064d6b9f9578470e0afca9c48e2cca6cf0f5c1194d12c52 |
| A1 | DOR_020_A1_WHERE_CLAUSES_AMENDMENT_2026-08-04.md | c4dc5976d7e65fe8a6597870629e64cabe6a031b95de97f5572bb36379abb588 |
| A7 | DOR_020_A7_EC_BRANCH_CARRIED_2026-08-05.md | 834e46029a292122c1e4c604af4f3e3249e6a9ee2638255464685623fba5eb8f |
| A8 | DOR_020_A8_GAMMA_BOTH_ROUTES_2026-08-05.md | 0ee6c897055f803b31bc570b9f4ef852ccb3c4aba21fcd5274a7d740c8eb601d |

COMMON-V2 is noted only for currency: it repairs R9 at Q-514. Its separate
cross-family confirmation is outside this artifact. No result below assumes
that confirmation.

### 0.3 Determination tags

~~~text
PROVABLE
 = follows from a displayed elementary argument or a verified sealed premise.

PART-PROVABLE
 = the displayed implication is valid, but one or more named inputs remain
   uninhabited.

YOURS
 = this review's determination, repair boundary, or counterexample.

PASS
 = adoption-safe as a candidate clause at exactly its displayed scope.

KILL
 = not adoption-safe as written.
~~~

## 1. Frozen types

The type distinctions used below are:

~~~text
K_N^(cyc,R)
 :=ker(B_N^T:R^(E_N)->R^(V_N)),

Lambda_N^cyc
 :=K_N^(cyc,R) intersection Z^(E_N),

D_N^Loc
 :=future ExtSrc image carrier,

Xi_N:D_N^Loc->Lambda_N^cyc
 :=proposed set map,

u_z:T_A Conn(P_N)->R
 :=ratified period functional,

Theta_N^rel(x;A_1,A_0)
 :=Hol_(A_1)(Xi_N(x)) Hol_(A_0)(Xi_N(x))^(-1),

A_0,A_1 in Conn(P_N)
 :=a retained ordered pair on the same admitted bundle.             (T1)
~~~

The target lattice is torsion-free:

~~~text
Lambda_N^cyc subset Z^(E_N)

2z=0 in Lambda_N^cyc
 =>2z=0 in Z^(E_N)
 =>z=0.                                                             (T2)
~~~

No use below upgrades ExtSrc, Ker, tau_f^Loc, rho_f^Loc, G4-D, full G4, G5,
Xi_N, or a scalarization family from a specification to an inhabitant.

## 2. R1 — Z-A7 and the separated chart conditions

### 2.1 [PROVABLE] The V002 clause was a tautology

For a fully formed retained tuple

~~~text
q=(A_1,A_0,K,a,b,x),

p_q
 :=u_(Xi_N(Ker_(a,K)(x)))(A_1-A_0),             (A1)
~~~

relative holonomy gives

~~~text
Theta_N^rel(Ker_(a,K)(x);A_1,A_0)
 =exp(i p_q).                                    (A2)
~~~

Elementary character theory gives, for every real p_q,

~~~text
exp(i p_q)=1_(U(1))
 iff p_q in 2 pi Z.                              (A3)
~~~

The V002 biconditional merely repeated A3 and could be refuted by no value of
p_q.

### 2.2 [PROVABLE] Z-A7 is now an assertion

V003 instead states, on epsilon=1,

~~~text
for every retained q,

Theta_N^rel(Ker_(a,K)(x);A_1,A_0)=1_(U(1)),

equivalently

p_q in 2 pi Z.                                  (A4)
~~~

Suppose one fully typed retained tuple q_* is displayed with

~~~text
p_(q_*) not in 2 pi Z.                           (A5)
~~~

Then A3 gives

~~~text
p_(q_*) not in 2 pi Z
 =>exp(i p_(q_*)) !=1_(U(1))
 =>Theta_N^rel(Ker_(a,K)(x_*);A_1,A_0)
      !=1_(U(1)).                                (A6)
~~~

A6 falsifies the universal assertion A4. It does not merely make two sides of
a biconditional false together. The tuple must carry its pair, K, address,
factor basis, and response; the phrase "one x" is shorthand only after those
indices are fixed.

### 2.3 [PROVABLE] Raw neutrality is separated from the chart seam

V003 separately books, for every carried scalarization member S,

~~~text
1_(U(1)) in U_b^S,
log_b^S(1_(U(1)))=0,
U_(a,1;A_1,A_0,N,S)^Hol(0)=0.                   (A7)
~~~

Thus

~~~text
Z-A7 inhabited
 +G2-N normalization member inhabited

 =>log_b^S(
      Theta_N^rel(Ker_(a,K)(x);A_1,A_0))
   =log_b^S(1_(U(1)))
   =0

 =>U_(a,1;A_1,A_0,N,S)^Hol(
      log_b^S(
        Theta_N^rel(Ker_(a,K)(x);A_1,A_0)))

   =U_(a,1;A_1,A_0,N,S)^Hol(
      log_b^S(1_(U(1))))

   =U_(a,1;A_1,A_0,N,S)^Hol(0)

   =0.                                           (A8)
~~~

The candidate's abbreviated U^Hol(0)=0 is harmless only when read with all
indices in the displayed G2-N condition (A7). No chart or U^Hol member is
supplied by this display.

~~~text
R1_Z_A7 = PASS
R1_SINGLE_ELEMENT_REFUTATION = GENUINE
R1_CHART_SEPARATION = PASS
~~~

## 3. R2 — Z3, its true theorem, and the sign-stratum horn

### 3.1 [PROVABLE] The zero-discontinuity theorem is sound

Assume an alleged member has

~~~text
Xi_N(x_0)=z !=0.                                 (H1)
~~~

For any positive sequence t_n->0, continuity of scalar multiplication in the
real quotient carrier gives

~~~text
t_n x_0->0.                                      (H2)
~~~

Z2(i) and Xi_N(0)=0 give

~~~text
Xi_N(t_n x_0)
 =Xi_N(x_0)
 =z
 !=0
 =Xi_N(0).                                       (H3)
~~~

Therefore Xi_N is not continuous at 0. This uses no reader, response output,
end test, or numerical value.

### 3.2 [YOURS — boundary correction] "Extension through 0" is the wrong status

Z1 already types Xi_N on D_N^Loc, and Z2 explicitly defines Xi_N(0)=0.
Therefore the phrase

~~~text
NOT DEFINED: any continuous extension of Xi_N through 0
~~~

does not state the exact boundary: there is no missing value at 0 to extend.
The exact statements are

~~~text
CONTINUITY_AT_ZERO is not a candidate requirement;

if im(Xi_N) contains z !=0,
then continuity at zero is PROVABLY IMPOSSIBLE by H1-H3;

if Xi_N is the zero map,
H1 is false and the zero map is continuous.      (H4)
~~~

This correction matters because "undefined", "unrequired", and "refuted for
every nonzero member" are different record statuses.

### 3.3 [PART-PROVABLE] The support-birth computation needs one more premise

The valid conditional theorem starts with

~~~text
supp_D(x) disjoint supp_D(y),
Xi_N(y)=z !=0,
t_n>0,
t_n->0,
supp_D(t_n y)=supp_D(y).                         (H5)
~~~

The last line is the positive-scale support-stability law. From H5,

~~~text
supp_D(x) disjoint supp_D(t_n y).                (H6)
~~~

Then Z2(i) and Z2(iii) give

~~~text
Xi_N(x+t_n y)
 =Xi_N(x)+Xi_N(t_n y)
 =Xi_N(x)+Xi_N(y)
 =Xi_N(x)+z
 !=Xi_N(x).                                      (H7)
~~~

Since x+t_n y->x, H7 proves discontinuity at that support-birth boundary.

V003 names typed disjointness and a nonzero y, but G4-D is uninhabited and no
support map or equation supp_D(t y)=supp_D(y) is displayed. Its theorem is
therefore PART-PROVABLE with H5, not proved merely from the phrase "typed
disjointness is inhabited." It also does not cover a birth direction y with
Xi_N(y)=0.

### 3.4 [PROVABLE conditional attack] Fixed-support constancy restores sign-evenness

V003 simultaneously says:

~~~text
negative scaling is not asserted;

if G5 supplies the sign-odd action,
Xi_N(-x)=-Xi_N(x);                               (H8)

Xi_N is constant on every fixed-support stratum. (H9)
~~~

For ordinary support,

~~~text
supp_D(-x)=supp_D(x).                            (H10)
~~~

H9-H10 give

~~~text
Xi_N(-x)=Xi_N(x).                                (H11)
~~~

On any G5 sign-odd sector, H8 and H11 combine:

~~~text
Xi_N(x)
 =Xi_N(-x)
 =-Xi_N(x),

2 Xi_N(x)=0,

Lambda_N^cyc torsion-free
 =>Xi_N(x)=0.                                    (H12)
~~~

H12 is exactly the collapse the repair removed from the all-real scale law.
It has been reintroduced through the untyped meaning of "fixed-support
stratum."

The two lawful repair shapes are:

~~~text
REPAIR A:
weaken H9 to constancy on each positive ray
{t x:t>0};

REPAIR B:
type an oriented/signed stratum map q_D^pm satisfying
q_D^pm(-x) !=q_D^pm(x) on a G5 sign-odd sector,
and state the exact factor equation

q_D^pm(x)=q_D^pm(y)
 =>Xi_N(x)=Xi_N(y).                              (H13)
~~~

V003 displays neither repair. Z4 says only that a fixed-support factorization
will exist later.

### 3.5 [YOURS] The provenance tag also overreaches

My V002 review proved H1-H3 and the conditional form H5-H7. It said the new
type may instead be constant within a fixed-support stratum. It did not prove
H9 as a consequence of Z1-Z2. V003 turns that possibility into

~~~text
DEFINED: Xi_N restricted to any fixed-support stratum is constant
~~~

and later calls it PROVABLE, even while Z4 admits the factorization is
unbuilt. At strongest, H9 is an authored YOURS clause, gated by a fully typed
G4-D. As currently worded, it additionally fails H12.

~~~text
R2_ZERO_HORN = PROVEN
R2_SUPPORT_BIRTH = PART_PROVABLE (+H5 support-stability premise)
R2_FIXED_SUPPORT_CONSTANCY = KILL (+H12)
R2_DEFINED_UNDEFINED_BOUNDARY = DEFECTIVE
~~~

## 4. R3 — zero-homogeneous winding and G2

### 4.1 [PROVABLE] The redone ray calculation is correct

Let

~~~text
k:=Ker_(a,K)(Rhat_(Kcycle,a)),
p:=u_(Xi_N(k))(A_1-A_0).                         (W1)
~~~

For t>0, linearity of an alleged Ker member and Z2(i) give every intermediate
equality:

~~~text
Theta_N^rel(
  Ker_(a,K)(t Rhat_(Kcycle,a));A_1,A_0)

=Theta_N^rel(
  t Ker_(a,K)(Rhat_(Kcycle,a));A_1,A_0)

=Theta_N^rel(t k;A_1,A_0)

=exp(i u_(Xi_N(t k))(A_1-A_0))

=exp(i u_(Xi_N(k))(A_1-A_0))

=exp(i p).                                       (W2)
~~~

At t=0:

~~~text
Ker_(a,K)(0)=0,
Xi_N(0)=0,
u_0=0,

Theta_N^rel(Ker_(a,K)(0);A_1,A_0)
 =exp(i u_0(A_1-A_0))
 =1_(U(1)).                                      (W3)
~~~

Therefore the punctured positive ray is constant. The killed linear formula
exp(i t p) does not follow, and the V001 full-line winding attack is
inapplicable.

### 4.2 [PROVABLE] The asserted character jump is conditional, not universal

From W2-W3:

~~~text
the character jumps at t=0

iff exp(i p) !=1_(U(1))

iff p not in 2 pi Z.                             (W4)
~~~

If instead

~~~text
p in 2 pi Z,                                    (W5)
~~~

then

~~~text
for every t>0,
Theta_N^rel(Ker_(a,K)(t Rhat);A_1,A_0)
 =exp(i p)
 =1_(U(1))

and

Theta_N^rel(Ker_(a,K)(0);A_1,A_0)
 =1_(U(1)).                                      (W6)
~~~

W6 is an explicit counterexample to V003's unqualified verbs "jumps to 1 at
the origin" and "the third horn ... seen through the character." The Xi value
may jump from a nonzero lattice cycle to zero while the U(1) character hides
that jump. When W1's Rhat is one of Z-A7's addressed identity-branch
responses, epsilon=1 requires W5.

Thus the stale linear proof is genuinely withdrawn, but the replacement
conclusion is still false as written.

### 4.3 [PART-PROVABLE] The independent G2 rebase is sound

The absence of the killed winding proof does not produce a logarithm. A real
scalar extraction still needs, for every retained scalarization member S,

~~~text
im(Theta_N^rel compose Ker_(a,K))
 subset U_b^S,

U_b^S subset U(1) open proper logarithm chart,

log_b^S:U_b^S->R continuous and single-valued,

exp(i log_b^S(g))=g
 for every g in U_b^S,                           (W7)
~~~

together with response independence, address/reality covariance, and the
separately booked identity normalization (A7).

No whole-image certificate or complete scalarization member is inhabited.
Therefore retaining G2 on the independent whole-image basis is sound.

There is one gate-booking collision. V003 first creates G2-N for A7, but Z6
later says G2 contains the chart conditions of A4. A4 does not contain all of
W7, and it was expressly separated from G2. The exact ledger must remain

~~~text
G2   =W7 plus the other non-normalization Scal^Hol member conditions;

G2-N =1 in U_b^S
      +log_b^S(1)=0
      +U_(a,1;A_1,A_0,N,S)^Hol(0)=0.             (W8)
~~~

~~~text
R3_WINDING_COMPUTATION = PASS
R3_CHARACTER_JUMP = KILL (+missing p notin 2 pi Z condition)
R3_G2_REBASE = PASS_IN_SUBSTANCE
R3_GATE_LEDGER = DEFECTIVE (+G2/G2-N collision)
~~~

## 5. R4 — units and both transport squares

### 5.1 [PROVABLE] Native phase units

For z=Xi_N(x) in Lambda_N^cyc, the U(1) edge relation gives

~~~text
h_e(A_1) h_e(A_0)^(-1)
 =exp(i integral_(gamma_e)(A_1-A_0)).            (U1)
~~~

Using integral exponents z_e:

~~~text
Hol_(A_1)(z) Hol_(A_0)(z)^(-1)

=product_e h_e(A_1)^(z_e)
  product_e h_e(A_0)^(-z_e)

=product_e
  (h_e(A_1) h_e(A_0)^(-1))^(z_e)

=product_e
  exp(i z_e integral_(gamma_e)(A_1-A_0))

=exp(i sum_e z_e integral_(gamma_e)(A_1-A_0))

=exp(i u_z(A_1-A_0)).                            (U2)
~~~

The exponent in U1 is a phase by the native U(1) relation, and the
integer-weighted sum in U2 retains that phase unit. No unit statement about
raw x in D_N^Loc is used:

~~~text
[U2 exponent]=1,

but no inference

x in D_N^Loc =>[x]=1                             (U3)
~~~

is licensed. Integrality is supplied only by the authored codomain
Xi_N(x) in Lambda_N^cyc.

### 5.2 [PART-PROVABLE] Rank-preserving transport

For rank-preserving f:N->M, the exact maps/types are

~~~text
S_f^Lambda:Lambda_N^cyc->Lambda_M^cyc,

tau_f^Loc:D_N^Loc->D_M^Loc.                     (U4)
~~~

Here S_f^Lambda is A1's adopted current transport restricted to the integral
lattice; tau_f^Loc is the future ExtSrc member.

Z9 requires

~~~text
Xi_M compose tau_f^Loc
 =S_f^Lambda compose Xi_N.                       (U5)
~~~

For A_0,A_1 in Conn(P_M), the relative consequence is:

~~~text
Theta_N^rel(
  x;eta_conn,f(A_1),eta_conn,f(A_0))

=Hol_(eta_conn,f(A_1))(Xi_N x)
  Hol_(eta_conn,f(A_0))(Xi_N x)^(-1)

=Hol_(A_1)(S_f^Lambda Xi_N x)
  Hol_(A_0)(S_f^Lambda Xi_N x)^(-1)

=Hol_(A_1)(Xi_M tau_f^Loc x)
  Hol_(A_0)(Xi_M tau_f^Loc x)^(-1)

=Theta_M^rel(tau_f^Loc x;A_1,A_0).              (U6)
~~~

The second equality is the sealed connection/cycle transport relation; the
third uses U5. Since tau_f^Loc is an uninhabited ExtSrc/G3 member, U5-U6 are a
gated condition, not a proved naturality square on an actual member.

### 5.3 [PART-PROVABLE] Cycle-creating transport

A1's adopted path/current law supplies injectivity on the admitted old
current image. The full type needed before writing an inverse is

~~~text
S_f^Lambda:Lambda_N^cyc->Lambda_M^cyc
 integral and injective,

Lambda_M^(cyc,old)
 :=S_f^Lambda(Lambda_N^cyc),

r_f^(Lambda,old)
 :=(S_f^Lambda)^(-1)
 :Lambda_M^(cyc,old)->Lambda_N^cyc,

D_M^(Loc,old)
 :=D_M^Loc intersection D_M^(ker,old),

rho_f^Loc:D_M^(Loc,old)->D_N^Loc.                (U7)
~~~

V003 types the formerly omitted physical old-image/rho datum in U7 and
supplies the formerly omitted cycle-image premise in U8:

~~~text
Xi_M(D_M^(Loc,old))
 subset Lambda_M^(cyc,old),                      (U8)

Xi_N compose rho_f^Loc
 =r_f^(Lambda,old)
   compose Xi_M|_(D_M^(Loc,old)).                (U9)
~~~

For A_0,A_1 in Conn(P_M) and y in D_M^(Loc,old):

~~~text
Theta_N^rel(
  rho_f^Loc y;eta_conn,f(A_1),eta_conn,f(A_0))

=Hol_(eta_conn,f(A_1))(Xi_N rho_f^Loc y)
  Hol_(eta_conn,f(A_0))(Xi_N rho_f^Loc y)^(-1)

=Hol_(eta_conn,f(A_1))(
    r_f^(Lambda,old) Xi_M y)
  Hol_(eta_conn,f(A_0))(
    r_f^(Lambda,old) Xi_M y)^(-1)

=Hol_(A_1)(
    S_f^Lambda r_f^(Lambda,old) Xi_M y)
  Hol_(A_0)(
    S_f^Lambda r_f^(Lambda,old) Xi_M y)^(-1)

=Hol_(A_1)(Xi_M y)
  Hol_(A_0)(Xi_M y)^(-1)

=Theta_M^rel(y;A_1,A_0).                        (U10)
~~~

The second equality uses U9. The fourth uses U8 and
S_f^Lambda r_f^(Lambda,old)=id on Lambda_M^(cyc,old).

V003 correctly calls rho_f^Loc a future G3-old member, assigns no value on the
target-new-cycle complement, and introduces no upward Xi law. It should have
restated the injectivity/type line in U7 before writing the inverse, but A1
supplies it; this is a display residue, not a mathematical obstruction.

### 5.4 R4 verdict

~~~text
R4_NATIVE_UNITS = PASS
R4_D_SIDE_UNIT_TRANSFER = WITHDRAWN
R4_INTEGRALITY_PROVENANCE = PASS
R4_RANK_SQUARE = PASS AS GATED CONDITION
R4_CYCLE_SQUARE = PASS AS GATED CONDITION
R4_FALSE_SEAL_CLAIM = WITHDRAWN
R4_TWO_OMITTED_PREMISES = SUPPLIED
R4_INVERSE_DISPLAY = RESIDUE (+injectivity not locally restated)
~~~

## 6. R5 — the five disclosed defects and the sixth-defect hunt

### 6.1 The five-item closure board

| # | V002 defect disclosed by V003 | Re-review | Exact disposition |
|---|---|---|---|
| 1 | Y-A7 was a tautology | PASS | Z-A7 is the universal assertion A4; A5-A6 give genuine one-element refutation; A7 is separately gated. |
| 2 | Y5 crossed from C_N^k to D_N^Loc | PASS | U1-U3 derive only native phase units and explicitly withdraw the raw D-side unit claim. |
| 3 | Y8 falsely sealed rho_f^D and omitted two premises | PASS with display residue | rho_f^Loc is future; U7 and U8 supply the physical old-domain/rho typing and cycle-image premise; the candidate omits the local injectivity line, which A1 supplies and this review restores in U7. |
| 4 | Y4 kept a linear winding proof after changing Xi's type | ORIGINAL DEFECT CLOSED; NEW CLAIM KILLED | W2-W3 correctly replace exp(i t p) by exp(i p), but W4-W6 refute the unconditional character-jump claim. |
| 5 | "locally constant away from 0" was false | OLD PHRASE WITHDRAWN; REPLACEMENT NOT CLOSED | Ambient local constancy is withdrawn, but fixed-support constancy is unproved as tagged and causes H12 unless signed strata are typed. |

Thus none of items 1-4 is merely renamed. Item 5 is not closed at adoption
strength: its replacement introduces a new structural collision.

### 6.2 [PROVABLE] Sixth defect: the anti-counterterm support law disappeared

V002 contained the separate law

~~~text
supp_Lambda(Xi_N(x))
 subset cl_record(supp_D(x)),                    (S1)
~~~

with the status:

~~~text
S1 is stated but unrunnable until full G4 bridges
the D-side and cycle-side support notions.        (S2)
~~~

My V002 review expressly distinguished:

~~~text
G4-D
 =D-side support/disjointness needed to state
  disjoint-support additivity;

full G4
 =the comparison needed to type S1 between
  supp_D and supp_Lambda.                         (S3)
~~~

V003's Z4 books only G4-D. No Z-clause restates S1, the final gate list contains
G4-D but not full G4, and the V3 hidden-counterterm void tied to S1 is absent.

The omission is failure-capable. Work on epsilon=0, take the one-dimensional
source carrier D=R e, let x=e, and choose an integral cycle z_out satisfying

~~~text
x !=0,
supp_Lambda(z_out)
 not subset cl_record(supp_D(x)).                (S4)
~~~

Define the full set map:

~~~text
Xi_N(0)=0,
Xi_N(t e)=z_out for every t !=0.                 (S5)
~~~

Then:

~~~text
positive-scale invariance holds;
fixed-support constancy holds on the sole nonzero support stratum;
disjoint-support additivity is vacuous on the
single indecomposable support apart from zero;
the integral codomain holds;
relative holonomy can consume z_out;
G5 is left uninhabited, exactly as V003 permits;

but S1 fails by S4.                               (S6)
~~~

No V003 clause rejects S4-S6. The candidate therefore permits precisely the
remote-cycle assignment the anti-counterterm law was meant to expose.

This is not a request to prove S1 or inhabit full G4. The bounded repair is to
restore S1 as a stated-but-unrunnable clause, restore full G4 to the gate
ledger, and restore the associated V3 failure condition.

### 6.3 [PROVABLE conditional attack] Seventh finding: the sign-stratum horn

H8-H12 are independent of the missing S1 law. Even after S1 is restored, Z3
still collapses every nonzero value on a G5 sign-odd sector unless the stratum
type distinguishes orientation/sign. This is a second fresh defect, not a
restatement of the anti-counterterm omission.

### 6.4 [PROVABLE] The superseding draft also drops the void board

V002 carried:

~~~text
V1 dependency,
V2 curvature relabeling,
V3 hidden counterterm,
V4 discipline,
V5 selection,
V6 A8 identification,
V7 identity branch,
V8 empty family relocated to the stopping board. (S7)
~~~

V003 says it supersedes V002, but it contains no successor void board. The
reader/no-selection clauses preserve parts of V1/V5, Z-A7 repairs V7, and the
lead retains the empty-family discipline. That does not carry the full suite:

~~~text
V3 is materially lost with S1;
V2 is not restated;
V4's split failure conditions are not restated;
V6's fault-isolation caveat is not restated.      (S8)
~~~

A superseding adoption candidate cannot obtain those tests by silence. They
must be carried explicitly or the draft must state that V002's void board
remains incorporated without supersession.

### 6.5 R5 verdict

~~~text
DISCLOSED_1_A7 = CLOSED
DISCLOSED_2_UNITS = CLOSED
DISCLOSED_3_RHO = CLOSED (+display residue)
DISCLOSED_4_STALE_WINDING = CLOSED
DISCLOSED_5_LOCAL_CONSTANCY = NOT CLOSED BY THE PROPOSED REPLACEMENT

SIXTH_DEFECT
 =Y9/full-G4 anti-counterterm law and V3 void omitted

SEVENTH_FINDING
 =fixed-support constancy restores the sign-even collapse

EIGHTH_FINDING
 =the character-jump conclusion omits p notin 2 pi Z

VOID_SUITE = NOT CARRIED
~~~

## 7. Clause and consequence board

| V003 item | Verdict | Adoption-strength reason |
|---|---|---|
| Z1 type | PASS as conditional specification | Integral set-map type is coherent and inhabits no member. |
| Z2(i) positive scaling | PASS as authored/gated law | It evades the old real-ray horn. |
| Z2(ii) sign arm | PASS as G5-conditional text | It does not itself identify reversal with scalar negation. |
| Z2(iii) disjoint additivity | PART-PROVABLE | G4-D and support-scale stability are uninhabited. |
| Z3 zero horn | PASS for H1-H3 | Nonzero members are discontinuous at zero. |
| Z3 fixed-support constancy | KILL | Under the ordinary unsigned-support reading it gives H12 on a sign-odd sector; otherwise the missing signed/oriented stratum type is itself the defect. |
| Z3 support births | PART-PROVABLE | Requires H5 and only covers nonzero disjoint births. |
| Z4 G4-D | INCOMPLETE | It does not replace full G4 or S1. |
| Z5 relative holonomy | PASS with same-bundle/integral scope | U2 is exact. |
| Z6 winding class | PASS | The class in R/(2 pi Z) is correctly typed. |
| Z6 G2 basis | PASS in substance | Whole-image containment remains uninhabited. |
| Z6 gate booking | DEFECTIVE as ledger text | It conflates G2 with separately introduced G2-N; the winding-class mathematics remains sound. |
| Z7 phase units | PASS | Native U(1) derivation; no D-side transfer. |
| Z8 integrality | PASS as authored codomain | Not miscredited to units or scaling. |
| Z9 rank transport | PASS as gated square | U4-U6; tau_f^Loc remains uninhabited. |
| Z10 cycle creation | PASS as gated old-image square | U7-U10; no new-cycle lift. |
| Z11 covariance/no selection | PASS as G5-gated text | It does not repair H12 without signed strata. |
| Z12 reader/consequence freedom | PASS | No reader or forbidden consequence appears. |
| Z-A7 | PASS | A4-A8. |
| Z-U | PASS only as bare candidate/residue | No U^Hol or Scal^Hol member is inhabited. |
| Y9 successor | MISSING | S1-S6. |
| void suite | MISSING/PARTIAL | S7-S8. |

The candidate is not ready for an adoption ruling. The bounded repair set is:

1. restore S1, full G4, and the V3 hidden-counterterm void;
2. type G4-D with an explicit support map, scale-stability law, and either
   signed/oriented strata or only positive-ray constancy;
3. replace the unconditional character-jump prose by W4;
4. keep G2 and G2-N distinct and restate the full W7 chart conditions;
5. restate U7 before the cycle-creating inverse;
6. carry the void board or incorporate it expressly.

No listed repair asks for a member, fixed point, end test, numeric value, or
route selection.

## 8. Fresh attack, battery, and verb audit

### 8.1 Fresh attack summary

[PROVABLE] The remote-cycle model S4-S6 is a single-element attack on the
omitted anti-counterterm law. The sign-stratum chain H8-H12 is an independent
conditional collapse. The phase-blind counterexample W5-W6 refutes the
unqualified claim that the character always detects Xi's discontinuity.

None was chosen because of a desired route or numerical consequence.

### 8.2 Candidate verb audit

| Candidate phrase | Audit |
|---|---|
| fixed-support constancy is DEFINED/PROVABLE | Too strong: it is an authored, uninhabited clause and fails H12 without signed strata. |
| the support-birth theorem holds at every birth | Too broad: H5 and Xi_N(y) !=0 are required. |
| continuous extension through 0 is NOT DEFINED | Wrong status: Xi_N(0) is defined; continuity is unrequired and impossible for a nonzero member. |
| the ray "jumps to 1" | False unless p notin 2 pi Z; W5-W6 refute the universal wording. |
| the third horn is seen through the character | False when the U(1) character hides an integral 2 pi period. |
| Z9 corrects V002's claim that rank transport was sealed | Provenance error: V002 expressly called that D-side map unsealed; its defect was the missing exact type/square. |
| Z9/Z10 are exact | The square equations are exact; U7's injectivity/type line still should precede the inverse. |
| G2 includes A4 | Conflicts with the separately booked G2-N and understates W7. |
| candidate self-verb audit is CLEAN | Refuted by the preceding rows. |
| five V002 defects all closed | Items 1-4 close in their original forms; item 5's replacement is defective. |

The phrase in V003 that the third-horn result was "adopted as Z3" also conflicts
with its own statement that the artifact adopts nothing. The honest verb is
"authored" or "stated."

### 8.3 This review's verb audit

| This review verb | Display |
|---|---|
| verified | Q-514 tail, hashes, sidecars, mirror comparison, line count, and no-clobber checks were run before writing. |
| pass | Restricted to a candidate clause at its stated conditional scope; no inhabitance inferred. |
| proved | Each use points to A1-A8, H1-H12, W1-W8, U1-U10, or S1-S8. |
| refuted/killed | Each use has a displayed counterexample, contradiction, missing type, or omitted clause. |
| conditional | Every uninhabited support, sign, ExtSrc, transport, and scalarization premise remains named. |
| omitted | XI-V2 and XI-V3 inventories were compared directly; S1 and S7 have no V003 successors. |
| not ready | The missing support law and H12 change load-bearing candidate content. |

No verb in this review is stronger than its displayed basis.

### 8.4 F_PLDEC and anti-tuning

~~~text
F_PLDEC
 =CLEAN:
  Xi_N, support laws, winding analysis, units, and transport squares are
  stated before and independently of every reader and response consequence;
  no reader appears in A1-S8.

ANTI_TUNING
 =CLEAN:
  no verdict uses a desired threshold, route winner, coefficient magnitude,
  measured constant, or numerical consequence.

NO_SELECTION
 =CLEAN:
  no Xi member, connection, reference, chart, orientation, scale, branch, or
  route is selected.

CONTRAVARIANCE
 =CLEAN:
  U7-U10 are old-image downward only; no upward lift is introduced.

MEMBER_BOUND = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false
MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL
 =G4-D/full-G4 support typing
  +G5 sign action
  +ExtSrc/Ker/tau_f^Loc/rho_f^Loc
  +whole-image chart/scalarization inhabitance;
  the structural review verdict itself does not depend on those members.
~~~

No register, plan, tracker, git, commit, push, member-binding, fixed-point,
end-test, numerical-evaluation, or measured-constant-comparison action was
performed by this lane. No law was adopted.

XI_N_V003 = DEFECTIVE (+Y9/full-G4 anti-counterterm law and its V3 void are omitted; under the ordinary unsigned-support reading Z3 fixed-support constancy restores sign-even collapse on every G5 sign-odd sector, while any escape requires the missing signed/oriented stratum type; the support-birth display lacks positive-scale support stability; the winding character jumps only when p notin 2 pi Z; G2/G2-N and the void suite are not carried cleanly)
READY_FOR_RULING = no
VERB_AUDIT_SELF = CLEAN
