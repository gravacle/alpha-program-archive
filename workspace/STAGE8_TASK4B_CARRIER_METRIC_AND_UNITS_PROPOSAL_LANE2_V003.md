# STAGE 8 TASK 4B — CARRIER_METRIC_AND_UNITS ADOPTION PROPOSAL — LANE 2 V003

Date: 2026-08-03  
Task: PASTE 459 / Task 4b  
Lane: CODEX LANE 2  
Status: **PROPOSED_NOT_ADOPTED — FULLNESS CLEANUP COMPLETE; FORCED FULL-CARRIER METRIC CORE SEPARATED FROM THE DoR-019 RESIDUE**

```text
REGISTER_HEAD_AT_PREFLIGHT = Q-377
PREFLIGHT = PASS

LEAD_RESULT = FULLNESS_INSTALLED_DERIVED

FINITE_FORCED_FORM:
  s_G(c,d)=g_A4(u_c,u_d) | TYPE-P | premises: DoR-015

FULLNESS:
  image(L_G)+image(B_G)=E_G | TYPE-P | premises: DoR-015 A2-R10
  ker(I_K,G)={0} family-wide | TYPE-P
  s_G positive definite on full K_G | TYPE-P

COMPLETION:
  forced-s Hilbert completion injective | TYPE-P
  identification with R5 K_cycle/C_prop | PROPOSED_NOT_ADOPTED

W3_RANK_PRESERVING_SOURCE_ISOMETRY = TYPE-P | premises: DoR-015 W3
A4_AUTOMORPHISM_ISOMETRY = PROPOSED_NOT_ADOPTED

NULL_SECTOR = absent | TYPE-R on admitted family
VISIBLE_CURRENT_QUOTIENT = K_G/0=K_G | trivial derived identity
NULL_OR_QUOTIENT_BRANCH_SELECTED = false | branches closed by theorem

R_A_UNIT = U_A^(-2)
R_A_INVERSE_UNIT = U_A^(2)

READY_FOR_CROSS_REVIEW = yes
READY_FOR_DOR019_RULING = after cross-review
DOR_019 = RESERVED

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The full metric carrier is no longer a choice.  A2-R10 forces the realized
connection tangent to fill the Gate-4 quotient, so every nonzero cycle
defines a nonzero A4 current.  The pullback semiform is therefore positive
definite on the full cycle carrier, and its forced-norm completion remains
faithful.  The former quotient/null alternatives are scope-empty on the
admitted family.

---

## 0. Preflight, custody, and verified authorities

The live questions-settled register and sidecar were checked before work;
the head was exactly `Q-377`.  The required fullness certificate was
hash-verified before reading.

| Artifact | Verified SHA-256 | Use |
|---|---|---|
| fullness certificate and V002 review | `f422a0340e253a72223f3c11d240b9b6a08b25a78ebf309085e84e965d8067ad` | U1–U3 bounded cleanup standard |
| carrier metric V002 | `7788e29da98be54e983a660768c0c70258e7d6d89eb51a2dafc4dbe17a9ea825` | repaired baseline |
| DoR-015 / field signature V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | forced form, R10 lineage, W3 |
| DoR-015 decision | `617bd51a70860d2cfb2066640630ba37ec289d56255ebbe1433bc0dfcba0159d` | ratification and exact W3 precision |
| square V004 | `abf6d366a5a7e375b9b53df75402f35d37f7c6a4b1bb0b10a44309ad3b0e1912` | R4 units and R5 carrier interfaces |
| DoR-017 decision | `ee9d81bf78ab0ac9361cad5b48dde2b6b8b1e9fb0e28a4fdbba41e1c43db3e45` | N member, symbolic `nu`, standing falsifier |
| divergence-datum descent | `c39de7a0ef5a29e92ded5fc961b54dfe933171ea291b221c38bf0aa3a9c0dcf3` | DP1–DP10 boundary |

```text
DOES_THE_OBJECT_EXIST = yes | forced metric core and bounded cleanup exist
IS_THE_VERSION_CURRENT = yes | Q-377
ARE_ITS_INPUTS_PRESENT = yes

CUSTODY = builder bounded cleanup; Lane 1 confirmation required
STANDING = PROPOSED_NOT_ADOPTED
P_VERDICT_DECLARED = false
NUMERIC_RESPONSE_EVALUATED = false
ROOT_OR_K_STAR_EVALUATED = false
MEASURED_CONSTANT_COMPARISON = false
```

---

## 1. U1 — fullness installed as derived content

### 1.1 The forced finite form, carried unchanged

For every admitted finite realization `G`, DoR-015 supplies

```text
K_G:=ker(B_G^T),
I_K,G(c):=u_c,
g_A4,G on the finite current image.
```

Therefore

```text
s_G(c,d):=g_A4,G(I_K,G c,I_K,G d)
         =g_A4,G(u_c,u_d),                       (U1-1)

s_G(c,c)=||u_c||_A4^2>=0,
ker(s_G)=ker(I_K,G).                             (U1-2)
```

`(U1-1)` and `(U1-2)` remain premise-marked derived content, exactly as in
V002.

### 1.2 The A2-R10 forcing chain

The fullness theorem has the following ratified provenance:

1. Field-signature V003 A2-R10 states that the differential of the framed
   scalar transport “reaches every admitted finite edge-coordinate direction
   modulo the displayed vertex-frame action.”
2. Field-signature V004 preserves A2-R1 through R11.
3. Field-signature V005 preserves every V004 survivor unless explicitly
   retargeted; it retargets the quotient/current domain, not A2-R10.
4. DoR-015 ratifies V005 and its external realization.

The finite differential is

```text
-i h_e^(-1)d h_e(a,theta)
 =(L_G a)_e+(B_G theta)_e,

(L_G a)_e=integral_(gamma_e) a,
(B_G theta)_e=theta_t-theta_s.                   (U1-3)
```

A2-R10 therefore says, equivalently,

```text
image(L_G)+image(B_G)=E_G,                       (U1-4)

q_G image(L_G)=E_G/image(B_G).                   (U1-5)
```

### 1.3 Kernel proof

Take `c in K_G` and suppose `I_K,G(c)=u_c=0`.  For arbitrary `x in E_G`,
`(U1-4)` gives `a,theta` with `x=L_G a+B_G theta`.  Then

```text
c^T x
 =c^T L_G a+c^T B_G theta
 =u_c(a)+(B_G^T c)^T theta
 =0.                                             (U1-6)
```

The edge pairing is nondegenerate and `x` was arbitrary, so `c=0`.
Consequently

```text
ker(I_K,G)={0}                                   (U1-7)
```

for every admitted realization member and every finite stage.  The proof
uses no selected path, frame, orientation, filtration, cycle basis, or
realization member.

From `(U1-2)` and `(U1-7)`,

```text
s_G is positive definite on the full K_G.        (U1-8)
```

This is the decisive correction to V002.

### 1.4 Integral cycles and record visibility

Since `(U1-7)` holds on the real carrier, it holds on the integral lattice:

```text
ker(I_K,G) intersection K_G^Z={0}.               (U1-9)
```

Hence no record-visible integral cycle can be A4-current-null on the
admitted family.  The conditional V002 theorem about a `D_G`-visible null
cycle has an empty antecedent under DoR-015.

```text
FINITE_FULLNESS = true | TYPE-P | premises: DoR-015 A2-R10
FINITE_SEMIFORM_NONDEGENERATE = true | TYPE-P
D_G_VISIBLE_A4_NULL_CYCLE = none | TYPE-R on admitted family
```

### 1.5 Directed core and forced-norm completion

Let `K_fin` be the algebraic directed union of the finite `K_G`.  Every
element occurs at a finite stage, so `(U1-7)` gives

```text
ker(I_K:K_fin->J_fin)={0}.                        (U1-10)
```

Use the forced norm

```text
||c||_s:=||I_K c||_A4.                           (U1-11)
```

DoR-015 W3 supplies the retained isometric finite inclusions, so `(U1-11)`
is a consistent pre-Hilbert norm on the directed core.  Complete `K_fin` in
this norm.  The map `I_K` extends uniquely as an isometry into
`J_phys^005`; if the extension maps `k` to zero, then

```text
||k||_s=||I_K k||_A4=0,
```

so `k=0`.  Thus

```text
ker(completed I_K)={0}.                           (U1-12)
```

This canonical forced-norm completion is derived mathematical content.  The
claim that R5's named `K_cycle` is exactly this completion remains the
authored carrier-identification residue.

---

## 2. U2 — null-sector branches closed by theorem

V002's quotient construction remains a valid abstract lemma:

```text
K_G^vis=K_G/ker(I_K,G).
```

On the admitted family, `(U1-7)` makes it the identity

```text
K_G^vis=K_G/{0}=K_G.                             (U2-1)
```

The former Q branch therefore adds no carrier, while the former N branch
has no null sector on which to place an independent form.  Both branches
are removed from the live proposal.  The V002 quotient-naturality theorem
is banked for any future realization family that weakens R10; it has no
live DoR-019 choice role under DoR-015.

```text
FULLNESS_BRANCH_AS_OPTION = closed by theorem
VISIBLE_QUOTIENT_BRANCH_AS_OPTION = closed by theorem | quotient is identity
NULL_METRIC_EXTENSION_BRANCH = scope-empty | TYPE-S
LIVE_NULL_SECTOR = false | TYPE-R
```

No record-visible content is deleted: there is nothing in the kernel.

---

## 3. U3 — W3 rank-preserving isometry re-derived

### 3.1 Exact ratified clause

The DoR-015 decision states:

```text
finite source restrictions are ADJOINTS of the retained isometric
inclusions; naive truncation is invalid.           (U3-1)
```

On an isometric inclusion `i_NM:C_N->C_M`, the ratified W3 restriction is

```text
rho_MN=i_NM^*.                                   (U3-2)
```

DoR-015's zero-extension/current seam also gives

```text
I_K,M j_K,NM=i_NM I_K,N.                         (U3-3)
```

### 3.2 Derived source/cycle isometry

For `c,d in K_N`, use `(U1-1)`, `(U3-1)`, and `(U3-3)`:

```text
s_M(j_K c,j_K d)
 =g_A4,M(I_K,M j_K c,I_K,M j_K d)
 =g_A4,M(i_NM I_K,N c,i_NM I_K,N d)
 =g_A4,N(I_K,N c,I_K,N d)
 =s_N(c,d).                                      (U3-4)
```

Therefore the rank-preserving cycle inclusion is isometric in the forced
metric, and its finite restriction is the adjoint:

```text
j_K,NM is isometric,
rho_K,MN=j_K,NM^*.                               (U3-5)
```

This is `TYPE-P | premises: DoR-015 W3`; it is not a DoR-019 authored
choice.

### 3.3 Exact scope

W3 does not supply:

1. automorphism isometry of the retained A4 norm;
2. a physical upward quotient map for cycle-creating extensions;
3. generic batching isometry;
4. identification of an arbitrary external R5 enlargement with the
   forced-norm completion.

Those claims are not inferred from `(U3-1)`.

```text
W3_RANK_PRESERVING_SOURCE_ISOMETRY = true | TYPE-P
W3_ADJOINT_RESTRICTION = true | TYPE-P
GENERIC_BATCHING_ISOMETRY = not claimed
CYCLE_CREATING_UPWARD_QUOTIENT_MAP = false | TYPE-R | Z7 retained
```

---

## 4. Cleaned full-carrier package

### 4.1 Derived core

The carrier metric's derived core is

```text
DERIVED_CORE_019 := (
  K_G=ker(B_G^T),
  I_K,G(c)=u_c,
  s_G(c,d)=g_A4(u_c,u_d),
  image(L_G)+image(B_G)=E_G,
  ker(I_K,G)=0,
  K_fin with ||c||_s=||I_K c||_A4,
  faithful forced-s Hilbert completion,
  W3 isometric rank-preserving inclusions and adjoint restrictions
).                                                (U4-1)
```

No element of `(U4-1)` is authored by DoR-019.

### 4.2 Authored residue

The live proposal adds only

```text
AUTHORED_RESIDUE_019 := (
  CARRIER_IDENTIFICATION_CERT,
  A4_AUTOMORPHISM_ISOMETRY_CERT,
  POSITIVITY_AND_REALITY_CONVENTION,
  CARRIER_UNIT_TORSORS_AND_R4_UNIT_SEAM
).                                                (U4-2)
```

The terms mean:

```text
CARRIER_IDENTIFICATION_CERT:
  R5 K_cycle is exactly the faithful forced-s completion;
  R5 C_prop is its completed Hilbert dual on D_017;
  the finite evaluation maps are dense, onto, closed-range compatible;
  rho_Gamma,N and rho_H,N consume these carriers on their proved scopes.

A4_AUTOMORPHISM_ISOMETRY_CERT:
  admitted exchanges/relabelings preserve g_A4;
  reality/orientation reversal is antiunitary after complexification;
  stabilizers preserve the same form;
  no member or orbit representative is selected.

POSITIVITY_AND_REALITY_CONVENTION:
  the real positive form and its complex Hermitian extension are fixed;
  no response-support clause, indefinite replacement, or extra null
  direction is introduced.

CARRIER_UNIT_TORSORS_AND_R4_UNIT_SEAM:
  formal U_C,U_K, no torsor member selected;
  U_action remains R4's action unit;
  nu stays symbolic and does not set a carrier scale.
```

### 4.3 Correct Riesz units, carried unchanged

For `A in {C,K}`:

```text
R_A:A->A^*,
[R_A]=U_A^(-2),
[R_A^(-1)]=U_A^(2).                              (U4-3)
```

The derivative-unit table remains:

| Object | Unit |
|---|---|
| `a in A` | `U_A` |
| `ell in A^*` | `U_A^(-1)` |
| scalar metric `g_A(a,b)` | `1` |
| `R_A` | `U_A^(-2)` |
| `R_A^(-1)` | `U_A^(2)` |
| `phi`, `nu` | `U_action` |
| `D_A phi` | `U_action U_A^(-1)` |
| `D_A D_B phi:B->A^*` | `U_action U_A^(-1)U_B^(-1)` |
| `R_A^(-1)D_A phi` | `U_action U_A` |
| `R_A^(-1)D_A D_B phi` | `U_action U_A U_B^(-1)` |

---

## 5. Cleaned choice table

| Field | Live proposed content | Genuine alternatives | Minimality | Void condition |
|---|---|---|---|---|
| completed carrier identification | identify R5 `K_cycle` with the faithful forced-s completion and `C_prop` with its Hilbert dual | different dense completion with proved equivalence; reject | only remaining seam from derived finite/fullness core to R5 | external enlargement, non-dense finite core, failed onto/closed-range proof, or D_017 mismatch |
| A4 automorphism isometry | retained A4 form invariant under exchanges/relabelings; reversal antiunitary | disclosed invariant replacement inducing the same W3 topology; bounded covariance only and no orthogonal propagation | W3 fixes stage maps but not automorphism isometry | S8-A exchange, orientation reversal, or stabilizer changes the form |
| positivity/reality convention | real positive carrier form with Hermitian complexification | real-only rigging; independently justified compatible Hermitian form | supplies the calculus convention without changing the forced finite values | indefiniteness, changed forced semiform, response-selected signature, or new null direction |
| carrier units | formal `U_C,U_K`, corrected Riesz powers, R4 action-unit seam | different formal unit convention with equivalent dimensional equations; reject units package | records dimensions without choosing scale | fixes `nu`, a rank ratio, numerical value, or desired response |
| reject | no DoR-019 adoption | — | preserves current TYPE-U boundary | — |

The former F/Q/N carrier alternatives do not appear: fullness is a theorem,
the quotient is the identity, and the null branch is scope-empty.

---

## 6. Restriction, automorphism, and cycle-creation ledger

| Map/operation | Standing in V003 | Provenance/scope |
|---|---|---|
| finite `I_K,G` | injective | A2-R10, `(U1-6)` |
| forced finite Riesz map | isomorphism on full `K_G` | positivity `(U1-8)` |
| forced-s completion | faithful | `(U1-10)`–`(U1-12)` |
| rank-preserving `j_K,NM` | isometric | DoR-015 W3, `(U3-4)` |
| rank-preserving `rho_K,MN` | adjoint of inclusion | DoR-015 W3, `(U3-5)` |
| realization automorphism | algebraically covariant; metric isometry proposed | authored residue only |
| reality reversal | algebraically semilinear; antiunitarity proposed | authored residue only |
| batching | existing covariance retained; no generic isometry | bounded/proved scopes only |
| cycle-creating addition | old cycle/current content retained; no upward physical quotient map | Z7 boundary retained |
| `rho_Gamma,N` | scalar derivative square retained | square V004 |
| `rho_H,N` | R5-generated Hessian cube retained | square V004; metric upgrade after DoR-019 residue |

No metric adjoint is used to manufacture the cycle-creating upward quotient
map refuted by Z7.

---

## 7. DP1/DP7 executability on the cleaned package

### DP1

The finite carrier form, positivity, and forced-norm completion now exist as
derived mathematics.  DoR-019 would supply the R5 identification and unit
convention.  The divergence datum itself remains absent.

```text
DP1_FINITE_CARRIER_FORM = TYPE-P | U1-1
DP1_FINITE_POSITIVITY = TYPE-P | A2-R10
DP1_FORCED_COMPLETION = TYPE-P | U1-12
DP1_R5_IDENTIFICATION_AND_UNITS = TYPE-U pending DoR-019
DP1_DIV_G_DELTA_G_ALPHA_DIV = TYPE-U
```

### DP7

Rank-preserving metric naturality is already derived from W3.  Automorphism
metric isometry remains part of the authored residue.  Generator naturality
and the divergence handoff remain open.

```text
DP7_RANK_PRESERVING_METRIC_NATURALITY = TYPE-P | DoR-015 W3
DP7_AUTOMORPHISM_METRIC_ISOMETRY = TYPE-U pending DoR-019
DP7_GENERATOR_NATURALITY = TYPE-U
DP7_FULL_D_G_HANDOFF = no null obstruction | fullness proved

DP1_DP10_DISCHARGED_BY_METRIC = false
```

The metric package makes the carrier portions executable; it does not
instantiate DP2–DP6 or DP8–DP10.

---

## 8. U4 — regression and battery rerun

### B1 — R10-violating countermodel, permanent admissibility regression

The former model was

```text
Q_G^lin=R^2,
K_G=R^2,
T_phys,G=span{e_1},
u_(c_1,c_2)(t e_1)=c_1 t.
```

It has `ker I_K=span{e_2}` because

```text
T_phys,G=span{e_1} != Q_G^lin=R^2,
image(L_G)+image(B_G) != E_G.                    (B1-1)
```

Thus it violates A2-R10 and is rejected before metric formation.

```text
R2_LINEAR_ALGEBRA = valid
R2_ADMITTED_BY_DOR015 = false | TYPE-R | A2-R10 failure
R2_COUNTERMODEL_ROLE = PERMANENT_ADMISSIBILITY_REGRESSION
```

### B2 — response-support attack

The forced form and fullness theorem contain no Hessian, Schur block,
stationary root, `p`, or desired output.  The authored residue is void if
its convention is selected for response support.

```text
RESPONSE_SUPPORT_TUNING = NOT_FOUND | PASS
```

### B3 — hidden-scale attack

Carrier units remain formal and use `(U4-3)`; `nu` remains a symbolic action
unit.  No numerical torsor member is selected.

```text
HIDDEN_NU_FIXING = NOT_FOUND | PASS
```

### B4 — fullness regression

For arbitrary `c` with `u_c=0`, `(U1-6)` evaluates `c` against an arbitrary
edge vector and forces `c=0`.  This runs family-wide.

```text
FULLNESS_KERNEL_TEST = PASS
```

### B5 — W3 double-charge regression

The choice table contains no rank-preserving stage-isometry row.  It is
listed only in the derived ledger with DoR-015 W3 provenance.

```text
W3_ISOMETRY_REAUTHORED = false | PASS
```

### B6 — A4 anisotropic exchange

The form `diag(1,2)` with exchange matrix `P` gives
`P^T diag(1,2)P=diag(2,1)`.  It fails the authored automorphism-isometry
certificate; V003 does not call that certificate derived.

```text
A4_AUTOMORPHISM_ISOMETRY_ASSUMED = false | PASS
```

### B7 — Riesz unit regression

Every live statement uses `[R_A]=U_A^-2` and
`[R_A^-1]=U_A^2`.

```text
R7_UNIT_POWER = PASS
```

### B8 — null-branch resurrection

Search of the live choice table finds no quotient/null option.  The only
mention is the closed-by-theorem disposition in Section 2 and this test.

```text
LIVE_NULL_OR_QUOTIENT_BRANCH = false | PASS
```

### B9 — cycle-creating upward-map attack

W3 is used only on its retained rank-preserving scope.  No metric adjoint is
promoted across a cycle-creating extension.

```text
Z7_BOUNDARY_RETAINED = true | PASS
```

### B10 — external enlargement attack

Add a completion direction orthogonal to every finite current.  It is not
part of the forced-s completion and fails the carrier-identification
certificate's density/closed-range clauses.

```text
UNWEIGHED_EXTERNAL_R5_DIRECTION_ADMITTED = false | PASS
```

---

## 9. U4 — bounded delta table versus V002

| V002 clause | V003 bounded change | Reason |
|---|---|---|
| `ACTUAL_KERNEL_ZERO=NO_VERDICT` | `ker(I_K,G)=0` derived family-wide | U1 / A2-R10 |
| `K_vis=K/ker I_K` live metric carrier | `K_vis=K/0=K`, trivial identity | U1/U2 |
| F/Q/N/reject branch table | F/Q/N removed; one completed full-carrier proposal plus reject | U2 |
| record-visible null theorem live | antecedent proved empty; theorem banked only | U2 |
| R2 model permanent countermodel | retained only as permanent R10-admissibility regression | U4 |
| A4 rank-preserving isometry authored | reclassified derived from DoR-015 W3 | U3 |
| A4 automorphism isometry authored | unchanged | outside W3 |
| generic batching bounded | unchanged | outside W3 isometry scope |
| cycle-creating upward map refuted | unchanged | Z7 |
| corrected Riesz units | unchanged verbatim in substance | R7 pass |
| response-support and hidden-scale defenses | unchanged and rerun | R3 pass |
| completed carrier certificate | retained, now full-carrier only | DoR-019 residue |
| DP1/DP7 ledger | fullness and W3 consequences promoted to derived; remaining doors unchanged | U4 |

No other mathematical field, unit equation, door, no-selection clause, or
fence from V002 is changed.

---

## 10. U5 — exact DoR-019 board

### 10.1 Derived core consumed by the ruling

| Item | Standing before DoR-019 |
|---|---|
| finite form `s_G(c,d)=g_A4(u_c,u_d)` | **DERIVED / TYPE-P**, DoR-015 |
| A2-R10 fullness `image L+image B=E` | **DERIVED / TYPE-P**, DoR-015 |
| `ker I_K=0` and full-carrier positivity | **DERIVED / TYPE-P** |
| integral-cycle faithfulness | **DERIVED / TYPE-P** |
| faithful forced-s Hilbert completion | **DERIVED / TYPE-P** |
| rank-preserving source/cycle isometry | **RATIFIED PREMISE / TYPE-P**, DoR-015 W3 |
| adjoint finite restrictions | **RATIFIED PREMISE / TYPE-P**, DoR-015 W3 |
| finite full-carrier Riesz maps | **DERIVED / TYPE-P** with corrected units |

DoR-019 does not author these items.  Its decision may cite them as the
foundation of the adopted package.

### 10.2 Authored residue the principal would ratify

| Item | Exact proposed addition |
|---|---|
| completion/carrier identification | R5 `K_cycle` is the forced-s completion; `C_prop` is its completed Hilbert dual on `D_017`; all restriction/Hessian seams commute |
| positivity/reality convention | real positive form and Hermitian complexification, with no changed finite values or extra nulls |
| A4 automorphism isometry | exchanges/relabelings orthogonal; reversal antiunitary; stabilizers preserve the form |
| units | formal `U_C,U_K`; corrected Riesz powers; R4 action-unit seam; `nu` symbolic |

The principal's live choices are:

1. adopt this completed full-carrier residue on the derived core;
2. request a different carrier-only completion/convention satisfying the
   same derived core and falsifier;
3. reject DoR-019.

No branch is selected here.

### 10.3 Standing falsifier

Any adopted package voids if it:

1. changes the forced finite form;
2. violates A2-R10 fullness or admits the permanent countermodel;
3. introduces a finite or completed null direction;
4. changes W3's isometric-inclusion/adjoint-restriction precision;
5. assumes generic batching or cycle-creating isometry beyond W3;
6. fails automorphism/reality isometry after adopting that residue;
7. reverses the Riesz unit power;
8. fixes `nu`, a numerical scale, rank, ratio, frame, filtration, or member;
9. uses response support or a desired downstream output.

```text
CARRIER_METRIC_V003 = BOUNDED_CLEANUP_COMPLETE

DERIVED_CORE:
  forced semiform = yes
  A2-R10 fullness = yes
  full-carrier positivity = yes
  faithful forced-s completion = yes
  W3 rank-preserving isometry/adjoints = yes

AUTHORED_RESIDUE:
  R5 completed carrier identification = proposed
  positivity/reality completion convention = proposed
  A4 automorphism isometry = proposed
  carrier units/R4 seam = proposed

LIVE_NULL_BRANCHES = none
R10_COUNTERMODEL_REGRESSION = installed
BATTERY = 10 attacks run
DP1_DP7 = restated on cleaned full carrier

READY_FOR_CROSS_REVIEW = yes
READY_FOR_DOR019_RULING = after cross-review
PROPOSAL_STANDING = PROPOSED_NOT_ADOPTED
DOR_019 = RESERVED

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

