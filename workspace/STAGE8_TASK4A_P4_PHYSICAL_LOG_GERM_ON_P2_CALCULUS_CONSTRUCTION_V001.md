# Stage 8 Task 4a P4 PhysicalLogGerm on P2 Calculus Construction V001

Date: 2026-08-02

Lane: CODEX LANE 1

Task: PASTE 356 - Task 4a / P4

Status: CERTIFIED SOURCE-ANALYTIC CONSTRUCTION; FULL PHYSICAL P4 WAITS ON P3

Every premise-dependent positive is marked:

~~~text
TYPE-P | premises: DoR-008, DoR-009, DoR-013, DoR-014
~~~

~~~text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
~~~

## 0. Lead determination

**The full P2 source domain contains exact zeros.** For every admitted ordered
rank class [A], with symbolic p_[A] in (0,1),

~~~text
Z_[A],n(s)=(1-p_[A])+p_[A] exp(Xi_n(s)),
~~~

the complete source-domain zero set is

~~~text
Zero_[A],n
  = union_(m in Z) Xi_n^(-1)(c_[A],m),

c_[A],m
  = log((1-p_[A])/p_[A]) + i(2m+1)pi.             (P4-1)
~~~

These are nonempty closed affine hyperplanes because Xi_n is a nonzero
bounded complex-linear functional. Each zero is simple in the transverse
Xi_n coordinate. A loop around one hyperplane has winding one, so a
single-valued logarithm does not exist on the entire zero complement.

That global obstruction does not obstruct the required local germ. The
rank-family neighborhood was frozen before downstream output:

~~~text
epsilon_[A] := log(1+1/(2p_[A])),
N_[A],n := {s in E_src: |Xi_n(s)|<epsilon_[A]}.
~~~

On this domain, |Z_[A],n-1|<1/2. The anchored power series defines a unique
holomorphic Log_0, with no local branch freedom. Its first, second, mixed, and
higher Frechet derivatives exist in Q-273's P2 calculus and commute with every
finite restriction.

The finite Q-243 falsifier passes after keeping three objects distinct:

~~~text
Gamma_log,N :=  Log_0 Z_N,
Gamma_fin,N := -Log_0 Z_N,          earlier finite Gamma convention,
W_N         := -i hbar Log_0 Z_N,   P4/P5 convention.
~~~

The earlier result d Gamma_fin/d theta|_0=-i p_[A] is recovered exactly. It is
not the derivative of Gamma_log. The response-facing W_N has the sealed
difference/difference Hessian and zero mixed retarded block.

P4's complete source-analytic body is now constructed, and P5 has all of its
source-analytic operands. The original PhysicalLogGerm identity also carries
P3's quotient, measure, contour, boundary-domain, and provenance fields. Those
remain unbuilt. This artifact therefore does not call the full physical tuple
complete or call an analytic R derivative a physical raw correlator.

~~~text
P4_SOURCE_ANALYTIC_LOG_GERM_EXISTS = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P4_GLOBAL_LOG_ON_FULL_ZERO_COMPLEMENT_EXISTS = false | TYPE-R |
  test: a transverse loop around any simple zero in (P4-1) has winding one
P4_LOCAL_ANCHORED_BRANCH_UNIQUE = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P4_FULL_PHYSICAL_LOG_GERM_EXISTS = false | TYPE-U |
  would-build: P3 physical quotient, descended measure, contour prescription,
               boundary/contact domains, and common-origin provenance
P5_SOURCE_ANALYTIC_INPUTS_COMPLETE = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P5_PHYSICAL_RAW_G_INSTANCE_EXISTS = false | TYPE-U |
  would-build: P3 plus the P5 raw-correlator construction on its physical domain
~~~

## 1. Scope, currency, and authorities

### 1.1 Scope

Roots entered:

~~~text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha_supervision
~~~

Exclusions:

~~~text
a32_holdout/custodian_private/                  NOT ENTERED
physical response, inversion, root, coupling    NOT CONSTRUCTED OR EVALUATED
measure or contour import                       NOT PERFORMED
measured-constant comparison                    NOT PERFORMED
specific ordered rank pair                      NOT SELECTED
register, plan, tracker, git, commit, push       NOT TOUCHED
~~~

The register head checked before construction was Q-273. No later ruling was
used.

### 1.2 Verified authorities

| Authority | SHA-256 | Load-bearing use |
|---|---|---|
| DECISION_OF_RECORD_014_SOURCE_GERM_PHYS_RATIFIED_2026-08-02_V001.md | b6e4116df63403478d28be8cdb6589b091cc1aa8b6ad5a40776a28b135cd138f | P1 germ and rank-family discipline |
| STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V004.md | d4cdbb6623797df6accb7dc9b24134d179bfc8e8d039c585d5c91ae23255869e | exact Z_inc, C-A/C-B, exported derivatives |
| STAGE8_TASK4A_P2_PHYSICAL_SOURCE_TOPOLOGY_AND_DIFFERENTIAL_CALCULUS_CONSTRUCTION_V001.md | 1339e3ce9793b8a528595835091d83db5266705041a440cc9d0c790d16cfb542 | P2 topology, dense core, calculus, restriction naturality |
| STAGE8_TASK4A_MISSING_PHYSICAL_LAYER_CONSOLIDATED_SPEC_AND_CONSTRAINT_BATTERY_V001.md | 241bf43f04aed7f215bad6ea80170a9c7733000896df839ac80974769d0a46c3 | Q-254 P4 and P5 contracts |
| STAGE8_CTP_PHYS_INPUT_PACKAGE_ITEM2_PHYSICAL_LOG0_GERM_SPEC_V001.md | 14573a676a385dd4c814f3fd12d8fb53caa601598e96b35525c6372329d506b3 | PhysicalLogGerm tuple and L-T0 through L-T7 tests |
| STAGE8_FINITE_P_CH_DEPENDENCE_AND_PHASE_RESIDUAL_TRANSPORT_DETERMINATION_V001.md | 8a71b6cdeca839fb6e52dbac4c2d13f7b9d2dafc3531dc1cc8bdc9089b3410b0 | finite minus-Log derivatives |
| STAGE8_TASK4A_FINITE_HESSIAN_TO_DELTAPHI_TRANSPORT_MAP_CONSTRUCTION_AND_P_CH_TRACE_V001.md | 70185aa842bc500724719c65bd66b5f07005e2214b97be0d35e07fd029d5c68c | Q-243 Keldysh block and finite retarded projection |
| STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md | 57c06fcbedf4a486b87b42c02e6d13a92096ac6a56751d3ae5fd55f4b11deb57 | P5 raw G consumer signature |

All available authority sidecars used above were verified before construction.

## 2. P4 contract and P5 consumer

### 2.1 P4 contract

The Q-254 contract at
STAGE8_TASK4A_MISSING_PHYSICAL_LAYER_CONSOLIDATED_SPEC_AND_CONSTRAINT_BATTERY_V001.md:250-268
requires:

~~~text
a nonzero neighborhood of the physical zero-source point;
a declared branch Log_0;
W=-i Log_0 Z_inc;
regularity sufficient for admitted first and second derivatives;
provenance tying the germ to the same physical functional.
~~~

The property-level specification at
STAGE8_CTP_PHYS_INPUT_PACKAGE_ITEM2_PHYSICAL_LOG0_GERM_SPEC_V001.md:281-316
gives the codomain:

~~~text
PhysicalLogGerm =
  [(N,Z_inc|N,Log_0,W_inc,Reg_req,provenance)]_0_src.
~~~

It requires N open, Z_inc nonzero there, the branch anchored at zero, first J
and symmetric-R derivatives, U1 reality, and U3 quotient/measure/contour/
boundary provenance.

### 2.2 P5 consumer signature

Q-254 states the P5 chain at :270-280:

~~~text
raw G from the bilocal R derivative of W;
its admitted inverse I_C on a named quotient/domain;
the stationary/2PI Hessian H_C or normalized equivalent;
the contour boundary-value and retarded extraction H_R;
RetHess_phys and topology_RetHess;
the exact induced response Pi_R,ind and subtraction/contact conventions.
~~~

The raw-map specification at
STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:639-670 fixes:

~~~text
Abar^I = delta W_inc/delta J_I,
G^(IJ) = 2 delta W_inc/delta R_IJ - Abar^I Abar^J.
~~~

The compound indices, contractions, quotient, measure, contour, contacts, and
inverse domain are additional P3/P5 inputs. P4 supplies the analytic
derivatives but cannot promote their formal combination to physical G.

### 2.3 Lawful split

Define the constructed object:

~~~text
P4_SOURCE_ANALYTIC_LOG_GERM_[A] :=
  [(N_[A],Z_[A]|N_[A],Log_0,[A],W_[A],
    Reg_D1,Reg_D2,Prov_(P1,P2))]_0_src.             (P4-2)
~~~

The complete physical tuple is:

~~~text
P4_PHYSICAL_LOG_GERM_[A] :=
  P4_SOURCE_ANALYTIC_LOG_GERM_[A]
  plus Prov_(P3 quotient,measure,contour,boundary domains). (P4-3)
~~~

Equation (P4-2) is built below. Equation (P4-3) remains TYPE-U. This exposes
the remaining fields without altering the contract.

## 3. Domain and exact zero set

For each DoR-014 class [A], retain the symbolic coefficient

~~~text
p:=p_[A]=Tr_A(P_ch)/Tr_A(I_A),  0<p<1.
~~~

No rank pair is instantiated. Q-273 supplies

~~~text
E_src = ell^1(N)_+ direct-sum ell^1(N)_-
        direct-sum S_1,sym(H_CTP),
D_src = {+1,-1} cross E_src.
~~~

On one character component, set

~~~text
lambda_n(j,r):=L_n^Theta(j)-(1/2)Q_delta^Theta(r),
Xi_n(s):=lambda_n(s),
Z_[A],n(s):=(1-p)+p exp(Xi_n(s)).                  (P4-4)
~~~

lambda_n is bounded complex-linear and nonzero. On a sealed one-cell R=0
source, L_n^Theta is the exact nonconstant faithful-character exponent
(STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V001.md:256-280). A nonzero
complex-linear functional has range C.

Solving Z=0 gives exactly (P4-1). Each fiber is a closed affine translate of
ker(lambda_n). At a zero s_0,

~~~text
D Z_[A],n(s_0)
  =p exp(Xi_n(s_0))lambda_n
  =-(1-p)lambda_n,
~~~

which is nonzero. Every hyperplane is a simple amplitude-zero locus in the
transverse coordinate.

Choose v with lambda_n(v)=1. On the complex line {zv}, a small loop around
one c_[A],m avoids all other zeros. Z has winding one around zero on this
loop. A global continuous logarithm would have zero winding, so no global
branch exists on the full zero complement.

~~~text
FULL_SOURCE_DOMAIN_ZERO_FREE = false | TYPE-R |
  test: exact zero locus (P4-1)
GLOBAL_SINGLE_VALUED_LOG_ON_COMPLETE_ZERO_COMPLEMENT = false | TYPE-R |
  test: simple-zero transverse loop has winding one
~~~

## 4. Frozen local neighborhood and branch

Use the neighborhood predeclared in the germ lineage:

~~~text
epsilon_p:=log(1+1/(2p)),
N_[A],n:={s in E_src: |Xi_n(s)|<epsilon_p}.
~~~

Continuity of Xi_n makes N_[A],n open and zero is interior. For every point:

~~~text
|Z_[A],n(s)-1|
  =p|exp(Xi_n(s))-1|
  <=p(exp(|Xi_n(s)|)-1)
  <1/2.                                                (P4-5)
~~~

Thus this domain misses every zero hyperplane and its Z image lies in the
simply connected disk |z-1|<1/2. The domain was declared at
STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V001.md:372-407 before the proposal
battery and downstream outputs, then carried through V004 and DoR-014.

Define:

~~~text
Log_0,[A] Z_[A],n(s)
  :=sum_(k>=1)(-1)^(k+1)(Z_[A],n(s)-1)^k/k,           (P4-6)

W_[A],n:=-i hbar Log_0,[A] Z_[A],n.                  (P4-7)
~~~

The series converges absolutely and locally uniformly. It is holomorphic,
exp(Log_0 Z)=Z, and Log_0 Z(0)=W(0)=0. Any two continuous logarithms differ
by a locally constant multiple of 2pi i; the basepoint value forces that
multiple to zero.

The ratified U1 relation

~~~text
Xi_(-n)(Theta_src s)=conjugate(Xi_n(s))
~~~

preserves the neighborhood. Since p and the series coefficients are real:

~~~text
Log_0 Z(Theta_src s)=conjugate(Log_0 Z(s)),
W(Theta_src s)=-conjugate(W(s)).
~~~

~~~text
P4_LOCAL_NONVANISHING = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P4_LOCAL_BRANCH_FREEDOM_REMAINS = false | TYPE-R |
  test: simply connected image disk plus anchored basepoint
P4_U1_REALITY = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
~~~

## 5. Frechet derivative tower

For s in N_[A],n, define

~~~text
q(s):=p exp(Xi_n(s))/Z_[A],n(s),
Gamma_log,[A],n:=Log_0,[A] Z_[A],n.
~~~

Since Xi_n is linear:

~~~text
D Gamma_log(s)[h]
  =q(s)lambda_n(h),                                  (P4-8)

D^2 Gamma_log(s)[h_1,h_2]
  =q(s)(1-q(s))lambda_n(h_1)lambda_n(h_2).           (P4-9)
~~~

All higher derivatives are fixed by:

~~~text
C_1(q):=q,
C_(k+1)(q):=q(1-q)dC_k(q)/dq,

D^k Gamma_log(s)[h_1,...,h_k]
  =C_k(q(s)) product_(a=1)^k lambda_n(h_a).          (P4-10)
~~~

For example, C_3(q)=q(1-q)(1-2q). These are bounded symmetric multilinear
forms on every norm-bounded subneighborhood whose closure remains in N.
Multiplication by -i hbar gives every derivative of W.

At zero, q=p:

~~~text
D_J Gamma_log(0)[j]=p L_n^Theta(j),
D_R Gamma_log(0)[r]=-(p/2)Q_delta^Theta(r),

D^2 Gamma_log(0)[h_1,h_2]
  =p(1-p)lambda_n(h_1)lambda_n(h_2),                (P4-11)

D^k W(0)=-i hbar C_k(p)lambda_n^(tensor k).
~~~

Equation (P4-11) supplies J/J, J/R, and R/R profiles in the one P2 calculus.
It does not identify the first R derivative with physical raw G.

~~~text
P4_REG_D1_CONSTRUCTED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P4_REG_D2_CONSTRUCTED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P4_HIGHER_FRECHET_TOWER_CONSTRUCTED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
~~~

## 6. Finite restrictions and falsifier

For Q-273's zero extension iota_src,N, define:

~~~text
Xi_n,N:=Xi_n compose iota_src,N,
Z_[A],n,N:=Z_[A],n compose iota_src,N,
N_[A],n,N:=iota_src,N^(-1)(N_[A],n),
Log_0,N:=Log_0 compose iota_src,N,
W_N:=W compose iota_src,N.
~~~

The bound (P4-5) holds on the finite domain, so the finite branch is a
restriction of the completed branch. For finite directions:

~~~text
D^k Log_0,N(s_N)[h_1,...,h_k]
 =D^k Log_0(iota_src,N s_N)
   [iota_src,N h_1,...,iota_src,N h_k],             (P4-12)
~~~

and likewise for W. At R=0, Z_N is exactly the sealed finite amplitude for
every N and both character orientations.

### 6.1 Sign correspondence

For the plus-character phase coordinate, write:

~~~text
A_N(theta)=(1-p)+p exp(i theta).
~~~

Exact differentiation gives:

| Object | Definition | First derivative at zero | Second derivative at zero |
|---|---|---|---|
| P4 logarithm | Gamma_log,N=Log_0 A_N | +i p | -p(1-p) |
| Earlier finite Gamma_N | Gamma_fin,N=-Log_0 A_N | -i p | +p(1-p) |
| Response-facing functional | W_N=-i hbar Log_0 A_N | hbar p | i hbar p(1-p) |

The n=-1 character reverses the first phase orientation and carries the same
transformed bilinear form.

The relay phrase "Gamma_phys=log Z_inc" together with
"dGamma|0=-i p_[A]" combines two sign conventions. The minus-i result is
recovered after the sealed map Gamma_fin=-Gamma_log. Q-243 consumes W.

~~~text
LOG_Z_FIRST_PHASE_DERIVATIVE_EQUALS_MINUS_I_P = false | TYPE-R |
  test: exact differentiation of A_N(theta)
FINITE_MINUS_LOG_DERIVATIVE_EQUALS_MINUS_I_P = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P4_TO_FINITE_GAMMA_SIGN_MAP = Gamma_fin,N equals -Gamma_log,N
~~~

### 6.2 Q-243 Keldysh check

The finite W_N Hessian is proportional to:

~~~text
M_DD=[[1,-1],[-1,1]],
T_CTP^T M_DD T_CTP=[[0,0],[0,1]].
~~~

The bilinear is entirely difference/difference. The ordered mixed retarded
(delta,c) block is exactly zero. The symbolic p(1-p) remains in the noise
block and is projected out without division or normalization.

~~~text
P4_DOR008_FINITE_J_RESTRICTION_FALSIFIER = PASS | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P4_Q243_FINITE_KELDYSH_FALSIFIER = PASS | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P4_FINITE_MIXED_RETARDED_BLOCK = ZERO_AND_RANK_PARAMETER_FREE
~~~

At nonzero R, C-B is ratified premise content but no independently sealed
finite raw-G reference exists. No additional comparison is manufactured:

~~~text
P4_NONZERO_R_INDEPENDENT_FINITE_FALSIFIER_EXISTS = false | TYPE-U |
  would-build: an independently sealed finite bilocal-source functional and
               derivative reference on the same source convention
~~~

## 7. Property-specific certificates

| Test | Verdict | Certificate or residue |
|---|---|---|
| L-T0 basepoint | PASS / TYPE-P | 0_src admitted; Z(0)=1 and Log_0 Z(0)=W(0)=0. |
| L-T1 open domain | PASS / TYPE-P | N is an inverse image of an open disk under continuous Xi; zero is interior. |
| L-T2 nonvanishing | PASS / TYPE-P | Exact bound abs(Z-1)<1/2; ambient zeros separately exposed. |
| L-T3 branch | PASS / TYPE-P | Anchored series is unique locally; global extension refuted by monodromy. |
| L-T4 regularity | PASS / TYPE-P | Equations (P4-8) through (P4-11) supply the full P2 tower. |
| L-T5a analytic predeclaration | PASS / TYPE-P | Topology, calculus, neighborhood, and branch were frozen before output. |
| L-T5a complete U3 prescription | NO_VERDICT | P3 contour and physical prescription unbuilt. |
| L-T5b prescription equivalence | NO_VERDICT | No two complete U3 prescriptions exist to compare. |
| L-T6 U1 reality | PASS / TYPE-P | U1 preserves N and the real-coefficient series. |
| L-T7 finite restriction | PASS at R=0 / TYPE-P | Exact amplitude, branch, derivatives, and Q-243 block reproduced. Nonzero-R independent control remains TYPE-U. |

~~~text
P4_SOURCE_ANALYTIC_TESTS = PASS
P4_COMPLETE_U3_PRESCRIPTION_TEST = NO_VERDICT |
  prerequisite: P3 contour and physical prescription package
P4_U3_EQUIVALENCE_NATURALITY_TEST = NO_VERDICT |
  prerequisite: two completed prescriptions and an independently proved map
~~~

## 8. P5 consumer readiness

P5 can now consume immediately, uniformly over the rank family:

~~~text
N_[A],n and Log_0,[A];
W_[A],n=-i hbar Log_0,[A] Z_[A],n;
D_J W, D_R W, D^2 W, and higher source derivatives;
finite restriction maps and derivative naturality;
the exact finite Keldysh difference/difference certificate;
P1/P2 common-origin provenance.
~~~

Every source-analytic operand in

~~~text
Abar=delta W/delta J,
G=2 delta W/delta R-Abar Abar
~~~

is available. P5 still lacks:

~~~text
P3 physical quotient and descended measure;
CTP contour/i-epsilon and boundary/contact domains;
compound-index contraction on that package;
the resulting physical raw G instance;
inverse I_C and stationary/2PI Hessian;
RetHess_phys, topology_RetHess, and physical restrictions;
retarded extraction and induced response.
~~~

The next lawful step is to complete P3 and instantiate raw G on that package
using the already constructed P4 derivatives.

~~~text
P5_HAS_ALL_SOURCE_ANALYTIC_INPUTS = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P5_HAS_ALL_PHYSICAL_INPUTS = false | TYPE-U |
  would-build: P3 and the P5 physical raw-G/inverse/extraction package
P4_DERIVATIVES_ARE_PHYSICAL_RAW_G = false | TYPE-R |
  test: the P5 signature additionally requires quotient, measure, contour,
        compound indices, boundary/contact domains, and connected subtraction
~~~

## 9. Mandatory kill passes

The ambient zeros and global monodromy are exposed. The local branch uses the
predeclared V001 neighborhood, not a domain selected after failure. Every
definition is family-wide in [A]; no rank pair is instantiated. No measure or
contour is imported. Log Z, minus-Log Z, and minus-i-hbar Log Z remain
distinct.

~~~text
HIDDEN_LOCAL_BRANCH_CHOICE_FOUND = false | TYPE-R |
  test: anchored uniqueness on the frozen image disk
POST_FAILURE_DOMAIN_SHRINK_FOUND = false | TYPE-S |
  scope: V001-to-DoR014 neighborhood lineage and this construction
SPECIFIC_RANK_PAIR_SELECTED = false | TYPE-S |
  scope: all P4 definitions and certificates
SMUGGLED_MEASURE_FOUND = false | TYPE-S |
  scope: P4 source-analytic construction
SMUGGLED_CONTOUR_FOUND = false | TYPE-S |
  scope: P4 source-analytic construction
RELAY_GAMMA_SIGN_CONFLATION_FOUND = true
P4_CONSTRUCTION_SIGN_CONFLATION_FOUND = false | TYPE-R |
  test: the three-row exact correspondence in Section 6.1
P4_SURVIVES_MANDATORY_SELF_KILL = true
~~~

## 10. Final typed ledger

~~~text
P4_SOURCE_ANALYTIC_LOG_GERM_EXISTS = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

P4_ZERO_SET =
  union_(m in Z) Xi_n^(-1)(log((1-p_[A])/p_[A])+i(2m+1)pi)
P4_FULL_SOURCE_DOMAIN_ZERO_FREE = false | TYPE-R |
  test: exact solution of Z_[A],n=0
P4_GLOBAL_LOG_ON_FULL_ZERO_COMPLEMENT_EXISTS = false | TYPE-R |
  test: simple-zero monodromy

P4_LOCAL_NONZERO_NEIGHBORHOOD_CONSTRUCTED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P4_LOCAL_LOG0_BRANCH_CONSTRUCTED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P4_LOCAL_LOG0_BRANCH_UNIQUE = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P4_W_INC_CONSTRUCTED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P4_REG_D1_REG_D2_AND_HIGHER_CONSTRUCTED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P4_DIFFERENTIATION_COMMUTES_WITH_RESTRICTION = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

P4_DOR008_FINITE_J_FALSIFIER = PASS | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P4_Q243_FINITE_KELDYSH_FALSIFIER = PASS | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P4_NONZERO_R_INDEPENDENT_FINITE_FALSIFIER_EXISTS = false | TYPE-U |
  would-build: independent finite bilocal-source derivative authority

P4_FULL_PHYSICAL_LOG_GERM_EXISTS = false | TYPE-U |
  would-build: P3 quotient, measure, contour, boundary/contact domains,
               prescription, and provenance
P5_SOURCE_ANALYTIC_INPUTS_COMPLETE = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P5_PHYSICAL_RAW_G_AND_RESPONSE_CHAIN_COMPLETE = false | TYPE-U |
  would-build: P3 then P5 raw G, inverse, Hessian, response class,
               restrictions, and retarded extraction

SPECIFIC_RANK_PAIR_SELECTED = false | TYPE-S |
  scope: this family-wide construction
MEASURE_OR_CONTOUR_IMPORTED = false | TYPE-S |
  scope: this source-analytic construction

alpha_computed = false [TERMINAL FENCE DECLARATION]
proof_authorized = false [TERMINAL FENCE DECLARATION]
kappa_record_computed = false [TERMINAL FENCE DECLARATION]
~~~
