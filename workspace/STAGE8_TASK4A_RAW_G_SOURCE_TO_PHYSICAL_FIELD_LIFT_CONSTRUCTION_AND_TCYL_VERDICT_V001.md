# Stage 8 Task 4a Raw-G Source-to-Physical-Field Lift Construction and T_cyl Verdict V001

Date: 2026-08-02  
Task: PASTE 368 / Task 4a  
Lane: CODEX LANE 2  
Status: EXPLICIT CYLINDRICAL LIFT SUBFAMILY BUILT; FULL FAMILY UNFROZEN; INTERTWINER UNSELECTED; NATURAL UNWEIGHTED BILOCAL COMPLETION REFUTED; PHYSICAL RAW `G` UNBUILT; Q-286 SIX-ACCOUNT PACKAGE INCOMPLETE

Premise-dependent positives are marked:

```text
TYPE-P | premises: DoR-008, DoR-009, DoR-013, DoR-014
```

```text
alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 0. Lead determination

**`T_cyl` can host a family of linear source lifts, but the ratified corpus does
not select the intertwiner. Its natural unweighted bilocal continuation is
unbounded on P2's trace-class domain.**

The P2 linear source space

```text
E_J=ell^1(N)_+ direct-sum ell^1(N)_-
```

has the following explicit bounded, restriction-natural **candidate** map into
the ratified C0 field algebra and its standard-module representation:

```text
Sigma_J(J)
 := sum_(a in {+,-}) sum_(j>=1)
      J_(a,j) pi_C0(e_a(U_(e_j))).                    (LIFT-1)
```

The series converges in operator norm and

```text
||Sigma_J(J)|| <= ||J||_1.
```

This candidate genuinely uses `T_cyl`. But the coefficient-identification
`J_(a,j) -> j(a,e_j)` is not sealed. More generally, for every fixed nonzero
real scalar `c`,

```text
Sigma_J^c(J)
 := c sum_(a,j)J_(a,j)pi_C0(e_a(U_(e_j)))
```

obeys the same boundedness, branch, reality, and restriction rules. Pairing it
with `c^(-1)` times the identity-character evaluation reproduces the same
ratified germ exponent. The germ fixes the **composition**, not its two
factors. At least this continuous rescaling family survives every sealed
cross-layer condition found. Therefore the linear intertwiner carries genuine
unselected freedom (`TYPE-U` on selection; uniqueness refuted on the stated
constraints).

**The natural unweighted bilocal candidate fails at the completed source
domain.** DoR-008 supplies only the finite algebraic map

```text
Sigma_R,N(R)
 := (1/2) sum_(a,j,b,k)
      R_((a,j),(b,k))
      pi_C0(e_a(U_(e_j))e_b(U_(e_k))).                (LIFT-2)
```

P2 instead admits the completed trace-class domain

```text
E_R=S_1,sym(H_CTP).
```

There is no bounded extension of this fixed unweighted association from that
trace-class domain into the `T_cyl` C-star/module norm class. The
counterexample is exact. On one
branch choose a unit vector `v_m` uniformly supported on an increasing finite
set and set

```text
R_m=v_m tensor v_m.
```

Every `R_m` has the same trace norm. Its finite character image is, up to the
fixed source convention,

```text
Sigma_R,m(R_m)(x)
  = (sum_j v_(m,j) x_j)^2.
```

At the all-identity character its magnitude grows with the support size.
Hence the C-star norms of the images are unbounded while the trace norms of
the inputs are fixed. No bounded trace-class-to-`T_cyl` extension exists.

This is not a failure of the finite maps. They remain exact at every finite
stage. It refutes the scale-free unweighted completed candidate. Weighted or
quotiented maps can evade the counterexample, but their weights/quotients are
not supplied by any ratified cross-layer rule; they remain an unbuilt family,
not a repair adopted here.

The physical port grammar is sealed:

```text
J_I couples to A^I;
R_IJ couples to A^I A^J/2;
raw G^(IJ)=2 delta W/delta R_IJ-Abar^I Abar^J.
```

But the actual ratified germ couples `J` and `R` to the charged projector
through the scalar exponent

```text
Xi_n[J,R]=L_n^Theta(J)-(1/2)Q_delta^Theta(R).
```

No sealed map identifies that scalar charged-projector insertion with the
formal physical operator insertion `J_I A^I+A^I R_IJ A^J/2`. C0's module has
no scalar state, and the germ's source-state trace is not a scalarization of
the C0 field module. Therefore the connected subtraction does not build.

The maximal new receipt is:

```text
RAW_G_LIFT_MAXIMAL_RECEIPT := (
  {Sigma_J^c:E_J -> L_B(E_C0)}_(c),           # completed candidate family
  {Sigma_R,N^(c^2):E_R,N -> L_B(E_C0,N)}_(N,c), # explicit finite subfamily
  GeneralIntertwinerInterface,                 # schema, not passed as instances
  GermLinearFactorizationFamily,
  FiniteBilocalRestrictionSquares,
  PartialLiftDependenceAccounts
).
```

The full raw-`G` lift remains `TYPE-U`. Its exact missing object is now:

```text
PHYSICAL_FIELD_SOURCE_REALIZATION_PACKAGE := (
  V_phys and its compound indices I=(a,mu,x),
  represented A^I on a scalar physical CTP carrier,
  a completed bilocal source map on E_R,
  source-field and source-bilocal intertwiners,
  scalar state/measure and branch pairing,
  Conn:Sym^2(V_phys)->Bil(V_phys),
  the connected-subtraction certificate,
  finite restriction/refinement squares,
  Tail_R action and common-origin provenance
).
```

`T_cyl` alone cannot supply this package. It has character labels, their C-star
algebra, a Hilbert module, and norm retractions; it has no spacetime/field
compound index, local field operator, scalar state, completed bilocal map, or
response assignment. Q-261 already proves the completed retarded consumer
does not factor through it.

```text
P2_LINEAR_SOURCE_TO_TCYL_EXPLICIT_RESCALING_SUBFAMILY_BUILT = true | STRUCTURAL
P2_LINEAR_SOURCE_TO_TCYL_FULL_INTERTWINER_FAMILY_FROZEN = false | TYPE-U |
  would-build: an exhaustive cross-layer family declaration and coverage proof
P2_LINEAR_SOURCE_TO_TCYL_INTERTWINER_SELECTED = false | TYPE-U |
  would-build: a cross-layer normalization/representation theorem or a
               principal-ratified intertwiner

P2_BILOCAL_SOURCE_FINITE_C0_LIFT_BUILT = true | TYPE-P |
  premises: DoR-008, DoR-014

UNWEIGHTED_P2_TRACE_CLASS_BILOCAL_TO_TCYL_EXTENSION_EXISTS = false | TYPE-R |
  test: fixed-trace-norm rank-one inputs have unbounded character-product images

SOME_OTHER_ADMISSIBLE_BILOCAL_TCYL_EXTENSION_EXISTS = NO_VERDICT |
  prerequisite: declare the full cross-layer intertwiner family and its
                physical admissibility constraints

TCYL_ALONE_IS_FULL_RAW_G_FIELD_LAYER = false | TYPE-R |
  test: the physical field/response signature is absent and the natural
        unweighted bilocal candidate fails

PHYSICAL_RAW_G_LIFT_BUILT = false | TYPE-U
RAW_G_CONNECTED_SUBTRACTION_BUILT = false | TYPE-U
```

## 1. Preflight, currency, roots, and authorities

### 1.1 Preflight and currency

```text
DOES_THE_PHYSICAL_RAW_G_LIFT_EXIST = false | TYPE-U
IS_THE_VERSION_CURRENT = true | through Q-286 at send-time custody
ARE_THE_INPUTS_PRESENT = PARTIAL |
  source derivatives, P2/P4, C0_008, finite source maps, and T_cyl exist;
  physical field realization, completed bilocal map, and scalarization do not
```

Q-283 and Q-284 are consumed. Q-285 and Q-286 landed during construction and
are consumed at send time. Q-285 proves that weak-star bidual completion is an
explicit tail creator and names this raw-`G` lift as the first physical
custodian of the completion-class choice. Q-286 independently confirms the
finite mathematics and the raw-`G` stop, but corrects Q-284's accounting
taxonomy: the response-operation table is only a partial account; four
field-operation accounts plus stationary-Schur and class-formation accounts
remain required.

### 1.2 Roots entered and exclusions

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha_supervision
/Users/bgm/MB Work/alpha-program-archive/workspace
```

```text
a32_holdout/custodian_private/                  NOT ENTERED
alpha/kappa/coupling/root/scale evaluation      NOT PERFORMED
rank-pair selection or ratio evaluation         NOT PERFORMED
measured-constant comparison                    NOT PERFORMED
register/plan/tracker/git/commit/push            NOT TOUCHED
```

### 1.3 Controlling authorities

| Authority | SHA-256 | Load-bearing content |
|---|---|---|
| `STAGE8_TASK4A_P5_MAXIMAL_TRANSPORT_CHAIN_AND_DEPENDENCE_ACCOUNTING_PACKAGE_V001.md` | `2fc227d0707f2720fece37bc90e966783887f79989412d127455409c05430d22` | Q-284 source derivative tensor, raw-`G` stop, and partial response-operation accounts (scope corrected by Q-286) |
| `STAGE8_TASK4A_W_GEN_TAIL_CREATION_IMAGE_THEOREM_DETERMINATION_V001.md` | `5f341414cda1001369fb97484729d9bef6475e9e8e21d12c41a2f2b3af433c44` | Q-285 explicit weak-star/bidual tail creator and raw-`G` class-formation custody |
| `STAGE8_TASK4A_P5_MAXIMAL_CHAIN_AND_ACCOUNTING_CROSS_VERIFICATION_DETERMINATION_V001.md` | `260fb9fcd944b100df9ca3f5c433a04170d577dc098ea513a9ddd8ddfdee3233` | Q-286 independent recomputation and corrected six-account taxonomy |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_C0_DOR008_ASSEMBLY_AND_FIRST_RESTRICTION_TEST_V001.md` | `1467ab9850022931e68dc9ffa625d95099d8f6bb74d734dc9d0466f169bd00b6` | `C0_008` carrier and finite `s_J,s_R` maps (`:142-190,223-292`) |
| `STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md` | `76916244bdbcac7c2a6d4afae40f35127540d1d9e4cfc86fb72318506671161f` | ratified label algebra/module and exact source-map domains (`:212-329,368-516`) |
| `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V004.md` | `d4cdbb6623797df6accb7dc9b24134d179bfc8e8d039c585d5c91ae23255869e` | live ratified germ lineage and family discipline |
| `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V001.md` | lineage retained by V004 | P2 source carriers and exact `L_n^Theta,Q_delta^Theta` ports (`:180-324`) |
| `STAGE8_TASK4A_P2_PHYSICAL_SOURCE_TOPOLOGY_AND_DIFFERENTIAL_CALCULUS_CONSTRUCTION_V002.md` | `40b2af34443e051fffdc7bf2ec7025c811a98c501a82d19164596ee6f37f00c1` | completed `ell^1`/trace-class source domain, dense finite core, and natural restrictions |
| `STAGE8_TASK4A_P4_PHYSICAL_LOG_GERM_ON_P2_CALCULUS_CONSTRUCTION_V001.md` | `b4c77ea948a02f3736fc824976f9ebd6381deff35f5c339a646739ea159725c5` | source derivatives and physical raw-`G` consumer distinction (`:135-208`) |
| `STAGE8_TASK4D_STITCHING_THEOREM_GERM_INDEPENDENT_HALF_V001.md` | `430f09715146cc03dabb0e349c422ae2499cff893d4e46b490fc0870954d1cb4` | `T_cyl` definition/proof (`:213-243,344-469`) and `T_phys` deficits (`:283-299`) |
| `STAGE8_TASK4D_CELLULATION_INDEPENDENCE_OD3_VERDICT_INVARIANCE_THEOREM_V001.md` | `f20639a6a1d5c8d73312bd646ceb2e0c74059c6f6206dca04032289f307e217b` | Q-261 nonfactorization of connection/response consumers through `T_cyl` (`:376-409`) |
| `STAGE8_TASK4A_ANCHORED_ORIGIN_TO_PHYSICAL_BACKGROUND_MAP_IDENTIFICATION_DETERMINATION_V001.md` | `f893d210191551bd8b6af060f85a73510f8119171c8709c46e925a6708314ed2` | source seed, absent intertwiners, and `STAT_BG_LIFT_FIBER` |
| `STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md` | sealed specification | formal physical source coupling and raw-`G` definitions (`:168-225`) |

### 1.4 Version and symbol adjudication

The live germ is V004. Its source-port formulas are inherited from V001 by
the V004 lineage; no later germ version supplies a different physical-field
intertwiner. `T_cyl` and the Q-261 factorization audit each have one live V001
artifact. Q-285 and Q-286 are later than the start-time Q-284 head and are
incorporated rather than treated as version replacements.

`kappa_R` below is Q-279's symbolic source/noise coefficient. It is not
`kappa_record` and is never evaluated here. `G` below is the formal raw
physical correlator only where the compound field indices are present; the
source-dual shadow is always labeled separately.

## 2. Three source-port layers that must not be identified

### 2.1 Formal physical field port

The formal physical CTP identity states (`STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md:168-204`):

```text
I=(a,mu,x),

Z_inc[J,R]
 =Tr_full{I_final T_C exp[(i/hbar)
    {S_CTP+J_I A^I+(1/2)A^I R_IJ A^J}]rho_pre},

Abar^I=delta W_inc/delta J_I,
G^(IJ)=2 delta W_inc/delta R_IJ-Abar^I Abar^J.
```

Thus the formal answer to “what does the source couple to?” is exact:

```text
J_I -> the physical connection-field operator A^I;
R_IJ -> the symmetric product A^I A^J.
```

This is a sealed **port grammar**. The same source explicitly lists the full
field Hilbert space, quotient, measure, branch data, and physical Dyson kernel
as unbuilt (`:206-225`). It does not instantiate `A^I`.

### 2.2 Ratified C0 character-operator port

DoR-008 instead supplies the bounded kinematic operators

```text
s_J(j)=sum_(a,lambda)j(a,lambda)pi_C0(e_a(U_lambda)),

s_R(r)=(1/2)sum r((a,lambda),(b,mu))
              pi_C0(e_a(U_lambda)e_b(U_mu)),
```

on the algebraic finite-support domains

```text
D_J=C_c({+,-} x (Lambda without {0});C),
D_R=D_J tensor_alg D_J.
```

These are character-unitary source insertions in the state-free Hilbert
`B`-module. DoR-008 expressly supplies no scalar functional `B->C`, no local
continuum connection, and no unbounded field operator.

### 2.3 Ratified germ port

DoR-014 supplies

```text
Xi_n[J,R]=L_n^Theta(J)-(1/2)Q_delta^Theta(R),
F_src=P_0+exp(Xi_n[J,R])P_ch,
Z_inc=(1-p)+p exp(Xi_n[J,R]),
```

where

```text
L_n^Theta(J) is the U1-real form of i n sum_j J_delta,j,
Q_delta^Theta(R) is the U1-real form of Tr(R_delta,delta).
```

This port couples both sources to the **charged projector insertion**. Its
scalarization is the source-state trace on the `P_0/P_ch` carrier. That trace
is not a state on C0's coefficient algebra `B`.

### 2.4 Port-identity standing

```text
FORMAL_PHYSICAL_SOURCE_PORT_GRAMMAR_SPECIFIED = true | SEALED-SPECIFIED
C0_CHARACTER_SOURCE_PORT_INSTANTIATED = true | TYPE-P | premises: DoR-008
GERM_CHARGED_PROJECTOR_SOURCE_PORT_INSTANTIATED = true | TYPE-P |
  premises: DoR-013, DoR-014

C0_CHARACTER_PORT_IDENTIFIED_WITH_PHYSICAL_A_FIELD_PORT = false | TYPE-U |
  would-build: physical field realization and source-action intertwiner

GERM_PROJECTOR_PORT_IDENTIFIED_WITH_C0_CHARACTER_PORT = false | TYPE-U |
  would-build: a common scalar representation and a commuting source-insertion diagram

GERM_POINTWISE_Z_IDENTIFIED_WITH_FORMAL_MICRO_CTP_Z = false | TYPE-U |
  would-build: the same diagram plus complete dynamics/measure/contour/domain provenance
```

The three port forms are not synonyms. The rest of the construction keeps them
separate.

## 3. Frozen lift family and the executable linear candidates

### 3.1 Candidate interface and explicit subfamily frozen before testing

Before testing an output, declare the cross-layer candidate interface. A
member is a pair of linear maps

```text
K_J,N:E_J,N->D_J,N,
K_R,N:E_R,N->D_R,N
```

that preserves branch involution, symmetric bilocal typing, `N<=M`
naturality, and the frozen Field-10 codomain. This interface is a schema, not
an instantiated exhaustive family. The corpus supplies neither a sealed bound
from which to freeze all members nor a theorem selecting one. The following
explicit subfamily is frozen before the tests. Its simplest unweighted member
uses the ratified stage basis:

```text
iota_J,N:J_(a,j) -> j(a,e_j)=J_(a,j),
iota_R,N:R_((a,j),(b,k))
  -> r((a,e_j),(b,e_k))=R_((a,j),(b,k)).
```

and freezes

```text
Sigma_J,N^id:=s_J compose iota_J,N,
Sigma_R,N^id:=s_R compose iota_R,N.
```

This member is tested because it adds no weights. It is not declared uniquely
physical. The subfamily

```text
K_J,N^c=c iota_J,N,
K_R,N^c=c^2 iota_R,N
```

with fixed nonzero real `c` already supplies inequivalent cross-layer
normalizations satisfying the same structural rules. More general compatible
weighted maps are not enumerated or passed as instances because no sealed
envelope bounds them.

### 3.2 Linear completion theorem

For the identity member and finite support,

```text
Sigma_J,N^id(J)
 =sum_(a,j<=N)J_(a,j)pi_C0(e_a(U_(e_j))).
```

Every represented generator is unitary, so the triangle inequality gives

```text
||Sigma_J,N(J)|| <= sum_(a,j<=N)|J_(a,j)|.
```

The identity-member finite maps therefore extend uniquely by density to the
bounded map (LIFT-1):

```text
Sigma_J^id:E_J -> L_B(E_C0).
```

Retraction naturality is exact:

```text
Pi_N Sigma_J^id = Sigma_J,N^id rho_J,N.
```

The Fourier characters `e_a(U_(e_j))` are linearly independent. Continuity
and uniqueness of Fourier coefficients then give `ker Sigma_J^id={0}`. Its image
is the singleton-character Wiener subspace of the represented `T_cyl` algebra,
not the whole field algebra.

```text
LINEAR_P2_TO_C0_IDENTITY_MEMBER_CONSTRUCTED = true | HYPOTHETICAL-CANDIDATE

LINEAR_P2_TO_C0_IDENTITY_MEMBER_BOUNDED = true | STRUCTURAL

LINEAR_P2_TO_C0_IDENTITY_MEMBER_RESTRICTION_SQUARE_COMMUTES = true | STRUCTURAL

SEALED_CURRENT_CONSTRAINTS_FORCE_UNIQUE_LINEAR_INTERTWINER = false | TYPE-R |
  test: the symbolic c-family preserves every stated cross-layer constraint

LINEAR_P2_TO_C0_PHYSICAL_MEMBER_SELECTED = false | TYPE-U |
  would-build: a normalization/representation selector over the declared family
```

### 3.3 Germ factorization of the linear exponent

Let `ev_1` be evaluation of the character algebra at the identity point of its
spectrum and let `Delta_CTP` take the declared branch difference. On finite
sources,

```text
i n ev_1(Delta_CTP Sigma_J,N^id(J))
  =i n sum_(j<=N)J_delta,j.
```

Both sides extend continuously in the `ell^1` norm. After the already-ratified
U1 orbit symmetrization, this is exactly `L_n^Theta(J)`. Hence:

```text
L_n^Theta = Sym_U1 compose (i n ev_1) compose Delta_CTP compose Sigma_J^id.
```

This factorization is a statement about the germ's scalar consumer. It does
not install `ev_1` as C0's physical state and does not turn a character unitary
into the local field `A^I`.

```text
GERM_LINEAR_PORT_FACTORS_THROUGH_IDENTITY_MEMBER = true |
  HYPOTHETICAL-MEMBER THEOREM | premises: DoR-008, DoR-014

GERM_LINEAR_FACTORIZATION_SELECTS_IDENTITY_MEMBER = false | TYPE-R |
  test: Sigma_J^c paired with c^(-1)ev_1 gives the same L_n^Theta

IDENTITY_CHARACTER_EVALUATION_IS_C0_PHYSICAL_SCALAR_STATE = false | TYPE-S |
  scope: DoR-008 C0; its scalarization firewall exports no state
```

## 4. Bilocal extension theorem — refutation in `T_cyl`

### 4.1 Finite map

For every instantiated member of the displayed rescaling subfamily,
`s_R compose K_R,N` is a valid finite map into `L_B(E_C0)`. In particular,
`Sigma_R,N^id` is star-covariant under U1 and uses the exact Field-10 source
form. Its finite source restrictions and C0 retractions commute.

```text
FINITE_BILOCAL_P2_TO_C0_IDENTITY_MEMBERS_CONSTRUCTED = true |
  HYPOTHETICAL-CANDIDATE

FINITE_BILOCAL_IDENTITY_MEMBER_RESTRICTION_SQUARE_COMMUTES = true | STRUCTURAL
```

### 4.2 Counterexample to a trace-norm bounded extension

Assume a bounded extension of the frozen unweighted member

```text
Sigma_R^id:S_1,sym(H_CTP)->L_B(E_C0)
```

agrees with every finite `Sigma_R,N^id`. Work inside one branch and let `v_m` be
the normalized vector with equal components on its first `m` cell basis
vectors. Let

```text
R_m=v_m tensor v_m.
```

Then `R_m` is symmetric rank one and

```text
||R_m||_1,trace=||v_m||_2^2,
```

independent of `m`. In the commutative field algebra its finite image is the
square of the character polynomial with coefficients `v_m`:

```text
Sigma_R,m^id(R_m)(x)
  =(fixed convention factor)
    (sum_(j<=m)v_(m,j)x_j)^2.
```

At the identity point `x_j=1`, its magnitude grows without bound with `m`.
The C-star norm dominates every point evaluation, so

```text
sup_m ||Sigma_R,m^id(R_m)|| = infinity
```

while the trace norms of the inputs are fixed. This contradicts boundedness.
Therefore no such extension exists.

The counterexample uses neither a physical rank pair nor an output target. It
tests the exact two ratified norms and the exact finite source map.

```text
UNWEIGHTED_FIELD10_BILOCAL_MAP_EXTENDS_TO_P2_TRACE_CLASS = false | TYPE-R |
  test: normalized rank-one family above

P2_AND_C0_BILOCAL_COMPLETIONS_HAVE_A_RATIFIED_COMPATIBILITY_MAP = false | TYPE-U |
  would-build: choose and certify a cross-layer member; the unweighted member
               is refuted, while weighted/quotient members remain unadjudicated
```

### 4.3 Why the germ bilocal scalar still exists

The germ does not apply a completed `Sigma_R` as an operator-valued map. It applies

```text
Q_delta^Theta(R)=Sym_U1 Tr(R_delta,delta),
```

which is bounded on trace class. At finite stage this can be represented as a
same-cell coefficient functional on `Sigma_R,N`. The scalar contractions can
be projectively consistent even though the operator-valued images have no
norm limit.

Thus the germ's existence does not repair the C0 bilocal map. Promoting the
scalar trace contraction to the physical bilocal field operator would be the
forbidden identification of a scalar consumer with its operator-valued
discharger.

```text
GERM_BILOCAL_SCALAR_FUNCTIONAL_EXISTS = true | TYPE-P |
  premises: DoR-014

GERM_BILOCAL_SCALAR_IMPLIES_COMPLETED_C0_BILOCAL_OPERATOR = false | TYPE-R |
  test: scalar trace remains bounded on the counterexample while the C0 images do not
```

### 4.4 Exact would-build

The completed bilocal port now requires one of the following, declared before
use:

1. a selected cross-layer weighting/intertwiner with a proof that it is not an
   imported scale or target-tuned suppression;
2. a different physical operator codomain and topology in which all finite
   chosen maps extend continuously from trace class;
3. a named closable/unbounded bilocal insertion with common domain and
   restriction theorem; or
4. a new source domain smaller than trace class.

Option 4 conflicts with the ratified P2 domain unless separately proposed and
ratified. Options 1-3 are construction/authorship territory and must carry
measure, contour, domain, and common-origin certificates. Nothing here selects
one.

## 5. `T_cyl` verdict

### 5.1 What `T_cyl` does supply

`T_cyl` supplies:

```text
Lambda=direct-sum_j Z e_j,
A_F=C*(Lambda),
B=A_F,+ tensor_min A_F,-^op,
the standard Hilbert-B module,
canonical finite retractions,
norm-class separation.
```

Consequently it can carry every displayed `Sigma_J^c` candidate and every
displayed finite `Sigma_R,N^(c^2)` candidate. It does not select their
cross-layer maps.

### 5.2 Two independent scope failures

First, the natural unweighted bilocal trace-class extension is refuted in
Section 4, while no weighted or quotient member is ratified.

Second, Q-258/Q-261 prove that `T_cyl` has no cell/edge/path realization,
spacetime point, physical connection one-form, measure, local derivative,
response map, or retarded CTP Hessian. Its compound labels are sequential
characters, not `I=(a,mu,x)`.

Q-261's exact consumer result is:

```text
completed connection-history response and retarded CTP Hessian
  do not factor through T_cyl.
```

The raw-`G` field layer is upstream of that same consumer and needs the missing
field/spacetime indices and bilocal pairing. Adding them changes the middle
object from `T_cyl` to the unbuilt `T_ref/T_phys` or an independently authored
physical CTP field package.

### 5.3 Accumulated-character warning

Even the all-cell faithful product is not one norm element of `T_cyl`. At
stage `N`, let

```text
u_n,N(x)=product_(j<=N)x_j^n.
```

For `M>N`, a product-spectrum point can make the added coordinate factors
reverse the value while leaving the first `N` coordinates fixed. Hence
`(u_n,N)` is not Cauchy in the C-star norm. The P2 germ exists because the
`ell^1` source topology makes the **evaluated phase sum** converge, not because
the partial-product observables converge in `T_cyl` norm.

This gives a second no-transport warning:

```text
the scalar norm-holomorphic germ is not one T_cyl observable.
```

### 5.4 Typed verdict

```text
LINEAR_SOURCE_FIELD_CHARACTER_LIFT_FAMILY_LIVES_ON_TCYL = true | STRUCTURAL

FULL_BILOCAL_RAW_G_LIFT_IS_SUPPLIED_BY_TCYL_ALONE = false | TYPE-R |
  test: unweighted extension counterexample, unselected alternative maps, and
        absent physical field signature

PHYSICAL_RETHESS_FACTORS_THROUGH_TCYL = false | TYPE-R |
  authority: Q-261

TCYL_ACCUMULATED_ALL_CELL_CHARACTER_EXISTS_AS_NORM_LIMIT = false | TYPE-R |
  test: partial products are not norm Cauchy
```

### 5.5 Q-285 tail-class custody

Q-285 distinguishes two completion classes that this lift must not conflate:

```text
separated norm/module codomain
  -> common finite-restriction kernel is zero;
  -> the lift cannot create response-tail content;

nonseparating weak-star/bidual completion
  -> the exact Q-247 moving family can acquire a nonzero element of z_tail B**;
  -> the class-formation act can create response-tail content.
```

The present construction enters neither completed physical class. The linear
identity candidate lands in a separated `T_cyl` norm class, but it is not the
selected physical intertwiner. The unweighted bilocal norm completion is
refuted. A weighted, quotient, unbounded, or weak-star completion remains
unselected and unbuilt. Consequently the raw-`G` lift is exactly the first
place where the topology decision becomes physical, as Q-285 states.

```text
RAW_G_LIFT_CLASS_FORMATION_TAIL_ACCOUNT_INTERFACE_SPECIFIED = true | TYPE-P |
  premises: Q-285

RAW_G_LIFT_CLASS_FORMATION_TAIL_CERTIFICATE_EXECUTED = false | TYPE-U |
  would-build: instantiate the class-formation operation and compute its
               image intersection with the declared physical Tail_R

RAW_G_LIFT_SELECTED_CLASS_IS_SEPARATED_NORM_MODULE = false | TYPE-U |
  would-build: the physical field/source realization package with its named
               raw-G codomain topology and restriction theorem

RAW_G_LIFT_SELECTED_CLASS_IS_NONSEPARATING_BIDUAL = false | TYPE-U |
  would-build: the same package plus a physical embedding of the Q-247 tail

RAW_G_LIFT_PHYSICALLY_CREATES_TAIL_R = NO_VERDICT |
  prerequisite: select or derive the completed physical class and execute its
                image-intersection certificate
```

The required extension to Q-284's accounting package is therefore:

```text
DEP_ACCOUNT_class_formation := (
  input core and topology,
  output raw-G class and topology,
  completion/extension act,
  image intersect Tail_R,
  physical restrictions and commuting square,
  quotient/closure exactness,
  common-origin provenance,
  target-independence certificate
).
```

## 6. Maximal lifted object and Q-279 restriction

### 6.1 Executable object

The maximal lifted construction is

```text
CylSourceLift := (
  {Sigma_J^c}_c,
  {Sigma_R,N^(c^2)}_(N,c),
  ev_1/branch-difference factorization of L_n^Theta,
  finite same-cell coefficient factorization of Q_delta^Theta,
  SourceDerivativeTensor_[A],
  G_JJ,src,[A],
  finite source restrictions and C0 retractions
).
```

Its codomain is a family of represented character operators, scalar germ
functionals, and source-dual derivatives. It is not a physical bilocal field
kernel.

### 6.2 Sector structure and `p` content

No new coefficient is introduced. The lift preserves Q-284/Q-279 exactly:

| Sector | Lift behavior | Exact `p` content |
|---|---|---|
| `J_c` | killed by the germ branch-difference consumer | zero |
| `J_delta` | any paired `Sigma_J^c`/consumer factorization | `omega_R` at first order; `kappa_R` at second order |
| `R_delta,delta` | finite `Sigma_R,N^(c^2)`, then its paired same-cell functional | `omega_R` first order; `kappa_R` in mixed and second derivatives |
| `J_delta/R` | finite source calculus; no physical sector transfer | `kappa_R` |
| ordered retarded `(delta,c)` | Q-243/Q-279 projection | zero and `p`-free |

### 6.3 Restriction squares

Each declared linear candidate square commutes on the completed P2 domain. A
declared bilocal candidate square commutes only on each finite stage:

```text
Pi_N Sigma_J^c = Sigma_J,N^c rho_J,N,

Pi_N Sigma_R,M^(c^2) iota_R,NM
  =Sigma_R,N^(c^2) rho_R,N       on finite-support R.
```

For each displayed candidate paired with the compensating scalar consumer,
composition reproduces Q-279's entire source-level tuple: the
`omega_R/kappa_R` noise and probe blocks and the zero ordered retarded block.
This is not a new physical lift or a numerical evaluation; it is equality of
the same finite source maps and therefore does not select a candidate.

```text
Q279_SOURCE_PATTERN_PRESERVED_BY_PAIRED_CYL_FACTORIZATION = true |
  HYPOTHETICAL-FAMILY THEOREM |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

COMPLETED_BILOCAL_RESTRICTION_SQUARE_EXISTS = false | TYPE-U |
  would-build: select and build a completed bilocal map; the unweighted
               T_cyl candidate is refuted
```

## 7. Connected subtraction and inverse

### 7.1 Why connected subtraction still does not form

The physical subtraction requires both terms in one bilocal field codomain:

```text
2 delta W/delta R_IJ - Abar^I Abar^J.
```

The current objects are:

```text
D_JW in E_J^*,
D_RW in E_R^*,
Sigma_J^c(E_J) in L_B(E_C0), with c unselected,
Sigma_R,N^(c^2)(E_R,N) in L_B(E_C0) only finitely, with c unselected,
E_C0 a Hilbert B-module with no scalar state.
```

There is no represented `A^I`, no scalar physical expectation on the module,
no completed `Sigma_R`, and no common map

```text
Conn:Sym^2(V_phys)->Bil(V_phys).
```

Therefore neither the bilocal-source definition nor its agreement with the
linear-source connected definition is executable.

```text
CONNECTED_SUBTRACTION_ON_TCYL_BUILT = false | TYPE-U |
  would-build: PHYSICAL_FIELD_SOURCE_REALIZATION_PACKAGE

LINEAR_SOURCE_SHADOW_EQUALS_PHYSICAL_RAW_G = false | TYPE-R |
  test: source-dual bilinear versus physical field/spacetime bilocal kernel
```

### 7.2 Physical inverse

Without physical raw `G`, its convolution measure, delta, prescription,
quotient, boundary/contact data, and common domains, the physical inverse
cannot be posed. The finite `T_cyl` module multiplication is not the physical
convolution inverse and is not substituted.

```text
PHYSICAL_RAW_G_BUILT = false | TYPE-U
PHYSICAL_RAW_G_INVERSE_BUILT = false | TYPE-U
```

## 8. Corrected accounting extension through Q-286

Q-286 independently recomputes Q-284's derivative tensor, complete Q-279
restriction, finite `p`-clean retarded image, and raw-`G` stop. It also refutes
the identity between Q-284's response-operation rows and Q-282's required
field-operation accounts. The table below is therefore retained and extended
under the narrower name:

```text
P5_RESPONSE_AND_RAW_G_LIFT_PARTIAL_DEPENDENCE_ACCOUNT.
```

It is not the complete Q-282 package.

| Lift operation | Kernel/null data | Image | Sector transfers | Restriction square | Tail action | Standing |
|---|---|---|---|---|---|---|
| `K_J -> s_J -> Sigma_J^K` | member-dependent; identity member has zero kernel; selected kernel untyped | singleton-character/selected character subspace of `L_B(E_C0)` | `+/-` branches map through C0 embeddings; no physical spacetime index | displayed rescaling members commute | `Tail_src={0}`; norm images reach no `Tail_R` | explicit subfamily built; full family and member selection `TYPE-U` |
| `K_R,N -> s_R -> Sigma_R,N^K` | member-dependent coefficient symmetries | finite character-product operator subspace | bilocal branch pair to selected product; no retarded projection | displayed finite rescaling members commute | finite only; no response tail | family interface plus explicit subfamily built; full family/member selection `TYPE-U` |
| attempted unweighted `Sigma_R^id` completion | applicability fails: identity-member finite maps are unbounded in P2 trace norm | no completed identity-member image | none | completed square absent | no `Tail_R` action defined | refuted in `T_cyl`, `TYPE-R` |
| germ `L_n^Theta` consumer | `ker L_n^Theta`, including `J_c` and zero-sum `J_delta` directions | one scalar exponent | branch difference only | commutes by `ell^1` density | `Tail_src={0}` | built `TYPE-P` |
| germ `Q_delta^Theta` consumer | trace-zero and non-DD bilocal directions | one scalar exponent | DD same-cell contraction only | finite restrictions converge in trace norm | `Tail_src={0}` | built `TYPE-P` |
| physical field realization | uninstantiated | `V_phys`, `Bil(V_phys)` | must create `I=(a,mu,x)` and preserve U1/CTP data | absent | must declare `Tail_R` generation/action | `TYPE-U` |
| physical class formation | uninstantiated | selected raw-`G` class | no sector transfer by itself; may change completion class | absent | zero if separated; can be nonzero under Q-285 weak-star/bidual completion | `NO_VERDICT`; first physical tail custodian |
| connected subtraction | uninstantiated | raw physical `G` | must combine first and bilocal derivatives in one codomain | absent | uninstantiated | `TYPE-U` |

This table extends Q-284 rather than replacing its four response arrows. The
last three rows feed Q-284 Arrow One; the later response arrows remain
unchanged.

### 8.1 Q-282/Q-286 account-status table

| Required account | Current instance | Exact standing |
|---|---|---|
| `DEP_ACCOUNT_measure` | no physical measure operation instantiated | `false | TYPE-U` |
| `DEP_ACCOUNT_contour` | no named-topology physical boundary-value operation instantiated | `false | TYPE-U` |
| `DEP_ACCOUNT_boundary` | no joint boundary/contact/null-reduction operation instantiated | `false | TYPE-U` |
| `DEP_ACCOUNT_domain` | no physical closure/extension operation instantiated | `false | TYPE-U` |
| `DEP_ACCOUNT_stationary_schur` | stationary 2PI/Schur operation uninstantiated | `false | TYPE-U` |
| `DEP_ACCOUNT_class_formation` | interface specified by Q-285 and Section 5.5; physical class and image-intersection certificate uninstantiated | `false | TYPE-U` |

```text
Q284_RESPONSE_ROWS_INTERNALLY_CORRECT_ON_BUILT_SCOPE = true | TYPE-P |
  premises: Q-286

Q284_ACCOUNTING_TABLE_IS_Q282_REQUIRED_FOUR_ARROW_PACKAGE = false | TYPE-R |
  test: Q-282 accounts measure/contour/boundary/domain; Q-284 accounts
        differentiation/inversion/Keldysh/induced-response

CURRENT_TAIL_ACCOUNT_COMPLETE_AFTER_Q286 = false | TYPE-U |
  would-build: all six accounts in the table above on instantiated physical
               operations, classes, restrictions, and topologies
```

## 9. Shared and distinct content of the background lift

### 9.1 Shared with raw `G`

Both the raw-`G` lift and `STAT_BG_LIFT_FIBER([A])` require:

1. the physical field carrier and represented `A^I`;
2. source-field and source-bilocal intertwiners;
3. one scalar physical CTP functional/measure on that carrier;
4. compound-index, branch, quotient, and domain data;
5. the connected bilocal construction and finite restriction squares.

The explicit `Sigma_J^c` subfamily supplies only candidate
character-operator parts of item 2; no member is selected. The finite
`Sigma_R,N^(c^2)` receipts supply only finite candidate pieces of the bilocal
part. The general `K` interface remains a schema, not an instantiated family.

### 9.2 Distinct background requirements

After the shared lift exists, the background fiber additionally requires:

```text
Leg:(Abar,G)<->(J,R),
the source-free stationary 2PI equations,
the stationary solution/existence and uniqueness class,
the physical evaluation-point rule,
boundary/contour data for the solution,
a verdict-uniform theorem across admitted lifts or one forced lift.
```

Those are not needed merely to type a raw correlator at a declared source
point. Thus the two consumers share a floor but do not collapse into one
object.

```text
RAW_G_AND_BACKGROUND_SHARE_FIELD_REALIZATION_FLOOR = true | TYPE-P |
  premises: Q-281, Q-284, and this construction

RAW_G_LIFT_EQUALS_STATIONARY_BACKGROUND_LIFT = false | TYPE-R |
  test: background additionally solves Legendre/stationary/evaluation equations
```

## 10. Updated residue from Q-284

Q-284's six deliverables remain six, but item 1 is narrowed and item 4 now
shares its floor explicitly:

| Q-284 item | Updated standing after this build |
|---|---|
| 1. raw-`G` lift | **PARTIAL:** linear and finite-bilocal candidate families built; no intertwiner selected; the unweighted `T_cyl` bilocal completion refuted; `PHYSICAL_FIELD_SOURCE_REALIZATION_PACKAGE` is the exact residue |
| 2. physical inverse | unchanged `TYPE-U`; waits on item 1 plus physical measure/prescription/domains |
| 3. P5/P6 transport | unchanged `TYPE-U`; waits on items 1-2 and physical restrictions |
| 4. background lift | narrowed: shares item 1's realization floor, then independently needs Legendre/stationary/evaluation data |
| 5. induced response | unchanged `TYPE-U`; needs the complete induced operator, second variation, contacts, and tail action |
| 6. consumption signature | Q-283 excludes `W_free`; Q-285 refutes universal `W_gen` emptiness by an explicit mathematical bidual creator, but physical `W_gen` remains `NO_VERDICT` and is now gated by item 1's class-formation choice |

The shortest updated dependency order is:

```text
R1  PhysicalFieldSourceRealizationPackage
    -- select/derive the cross-layer intertwiners and provide a bounded
       non-unweighted-T_cyl bilocal completion or declared unbounded realization
R2  raw G plus connected-subtraction and finite restriction theorem
R3  physical inverse / RetHess / P6 squares
R4a stationary 2PI background lift
R4b induced response plus Tail_ind
R5  consumption signature and final symbolic p-presence/absence verdict
```

### 10.1 Geometric critical-path consequence

If the program requires the physical connection/field layer to be **derived
from its geometric record structure**, R1 is now in `T_ref/T_phys` and O-D3
territory: `T_cyl` is insufficient by theorem. An independently authored
physical CTP field realization is a logically different route and would need
its own premise gate. Therefore:

```text
DERIVED_GEOMETRIC_ROUTE_REACHES_OD3_TPHYS_AT_RAW_G_LIFT = true |
  scope: route requiring physical field geometry to descend from record structure

EVERY_LOGICAL_RAW_G_ROUTE_REQUIRES_OD3 = false | TYPE-R |
  test: a separately authored physical CTP field realization is a distinct route
```

No authored route is selected here.

## 11. Kill-passes

### 11.1 Counterexample hunted before promotion

The trace-class rank-one family kills the tempting completed `Sigma_R` map.
The result leads; it is not repaired by shrinking P2 or changing topology.

### 11.2 No scalarization import

Identity-character evaluation is used only to prove the already-ratified germ
factorization. It is not installed as C0's physical state, measure, or GNS
functional.

### 11.3 No `T_cyl`/`T_phys` identity

Character-label norm completion, physical field continuum, geometric
refinement, raw correlator, and retarded response remain distinct objects.

### 11.4 No topology change

P2 remains `ell^1 direct-sum trace-class`. The bilocal counterexample is
reported; the domain is not narrowed to make Field 10 extend.

### 11.5 No missing-field value or rank value

No physical field, measure, scalar state, contour, background, tail, response,
rank pair, or ratio is selected or evaluated.

## 12. Final typed ledger

```text
FORMAL_PHYSICAL_SOURCE_PORT_GRAMMAR_SPECIFIED = true | SEALED-SPECIFIED
C0_CHARACTER_SOURCE_PORT_INSTANTIATED = true | TYPE-P |
  premises: DoR-008
GERM_PROJECTOR_SOURCE_PORT_INSTANTIATED = true | TYPE-P |
  premises: DoR-013, DoR-014

LINEAR_P2_TO_C0_EXPLICIT_RESCALING_SUBFAMILY_BUILT = true | STRUCTURAL
LINEAR_P2_TO_C0_FULL_INTERTWINER_FAMILY_FROZEN = false | TYPE-U
LINEAR_P2_TO_C0_IDENTITY_MEMBER_BOUNDED = true | STRUCTURAL
LINEAR_P2_TO_C0_IDENTITY_MEMBER_RESTRICTION_SQUARE_COMMUTES = true | STRUCTURAL
SEALED_CURRENT_CONSTRAINTS_FORCE_UNIQUE_LINEAR_INTERTWINER = false | TYPE-R
LINEAR_P2_TO_C0_PHYSICAL_MEMBER_SELECTED = false | TYPE-U
GERM_LINEAR_PORT_FACTORS_THROUGH_EACH_PAIRED_C_MEMBER = true |
  HYPOTHETICAL-FAMILY THEOREM

FINITE_BILOCAL_P2_TO_C0_FAMILY_INTERFACE_BUILT = true | STRUCTURAL
FINITE_BILOCAL_P2_TO_C0_FULL_INTERTWINER_FAMILY_FROZEN = false | TYPE-U
FINITE_BILOCAL_IDENTITY_MEMBER_RESTRICTION_SQUARE_COMMUTES = true | STRUCTURAL
UNWEIGHTED_FIELD10_BILOCAL_MAP_EXTENDS_TO_P2_TRACE_CLASS = false | TYPE-R
P2_AND_C0_BILOCAL_COMPLETIONS_HAVE_A_RATIFIED_COMPATIBILITY_MAP = false | TYPE-U

LINEAR_SOURCE_FIELD_CHARACTER_LIFT_FAMILY_LIVES_ON_TCYL = true | STRUCTURAL
FULL_BILOCAL_RAW_G_LIFT_IS_SUPPLIED_BY_TCYL_ALONE = false | TYPE-R
TCYL_ALONE_IS_FULL_RAW_G_FIELD_LAYER = false | TYPE-R
TCYL_ACCUMULATED_ALL_CELL_CHARACTER_EXISTS_AS_NORM_LIMIT = false | TYPE-R
PHYSICAL_RETHESS_FACTORS_THROUGH_TCYL = false | TYPE-R |
  authority: Q-261

GERM_BILOCAL_SCALAR_FUNCTIONAL_EXISTS = true | TYPE-P |
  premises: DoR-014
GERM_BILOCAL_SCALAR_IMPLIES_COMPLETED_C0_BILOCAL_OPERATOR = false | TYPE-R
GERM_POINTWISE_Z_IDENTIFIED_WITH_FORMAL_MICRO_CTP_Z = false | TYPE-U

Q279_SOURCE_PATTERN_PRESERVED_BY_PAIRED_CYL_FACTORIZATION = true |
  HYPOTHETICAL-FAMILY THEOREM |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
COMPLETED_BILOCAL_RESTRICTION_SQUARE_EXISTS = false | TYPE-U

Q285_WEAK_STAR_BIDUAL_COMPLETION_CREATES_TAIL = true | TYPE-P |
  premises: Q-247, Q-285
RAW_G_LIFT_IS_FIRST_PHYSICAL_TAIL_CLASS_CUSTODIAN = true | TYPE-P |
  premises: Q-284, Q-285
RAW_G_LIFT_CLASS_FORMATION_TAIL_ACCOUNT_INTERFACE_SPECIFIED = true | TYPE-P |
  premises: Q-285
RAW_G_LIFT_CLASS_FORMATION_TAIL_CERTIFICATE_EXECUTED = false | TYPE-U
RAW_G_LIFT_PHYSICALLY_CREATES_TAIL_R = NO_VERDICT

Q286_Q284_FINITE_MATHEMATICS_RECOMPUTES = PASS | TYPE-P |
  premises: Q-286
Q284_ACCOUNTING_TABLE_IS_Q282_REQUIRED_FOUR_ARROW_PACKAGE = false | TYPE-R
DEP_ACCOUNT_MEASURE_EXISTS = false | TYPE-U
DEP_ACCOUNT_CONTOUR_EXISTS = false | TYPE-U
DEP_ACCOUNT_BOUNDARY_EXISTS = false | TYPE-U
DEP_ACCOUNT_DOMAIN_EXISTS = false | TYPE-U
DEP_ACCOUNT_STATIONARY_SCHUR_EXISTS = false | TYPE-U
DEP_ACCOUNT_CLASS_FORMATION_EXISTS = false | TYPE-U
CURRENT_TAIL_ACCOUNT_COMPLETE_AFTER_Q286 = false | TYPE-U

PHYSICAL_FIELD_SOURCE_REALIZATION_PACKAGE_BUILT = false | TYPE-U
CONNECTED_SUBTRACTION_ON_TCYL_BUILT = false | TYPE-U
PHYSICAL_RAW_G_BUILT = false | TYPE-U
PHYSICAL_RAW_G_INVERSE_BUILT = false | TYPE-U

RAW_G_AND_BACKGROUND_SHARE_FIELD_REALIZATION_FLOOR = true | TYPE-P |
  premises: Q-281, Q-284, and this construction
RAW_G_LIFT_EQUALS_STATIONARY_BACKGROUND_LIFT = false | TYPE-R

REGISTER_HEAD_AT_START = Q-284
REGISTER_HEAD_AT_SEND_TIME = Q-286
LATER_BEARING_RULINGS_CONSUMED = Q-285, Q-286 |
  effect: Q-285 makes the raw-G completion topology the first physical tail
          custody decision; Q-286 confirms the mathematics and requires the
          corrected six-account taxonomy

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

The raw-`G` lift has moved, but it has not closed: an explicit linear
source-lift subfamily lives on the ratified cylindrical field algebra, with no
member selected; the natural unweighted bilocal member provably does not
extend there from the ratified trace-class domain. The next object is the
precisely typed physical field/source realization package, including an
exhaustive intertwiner family, a completed bilocal realization, a common
scalar physical CTP representation, and the Q-285 class-formation tail
certificate.
