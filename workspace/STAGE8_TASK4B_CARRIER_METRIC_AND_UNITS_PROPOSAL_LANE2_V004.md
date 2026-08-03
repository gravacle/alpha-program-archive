# STAGE 8 TASK 4B — CARRIER_METRIC_AND_UNITS ADOPTION PROPOSAL — LANE 2 V004

Date: 2026-08-03  
Task: PASTE 461 / Task 4b  
Lane: CODEX LANE 2  
Status: **PROPOSED_NOT_ADOPTED — BOUNDED RESTORE COMPLETE; FULL FINITE C/K METRIC CORE AND FOUR-ITEM DoR-019 RESIDUE PRESENT**

```text
REGISTER_HEAD_AT_PREFLIGHT = Q-379
PREFLIGHT = PASS

LEAD_RESULT = V003_CLEANUP_PLUS_V002_FINITE_C_SIDE_RESTORED

DERIVED_FINITE_K_SIDE:
  s_G(c,d)=g_A4(u_c,u_d)
  image(L_G)+image(B_G)=E_G
  ker(I_K,G)=0
  R_K,G isomorphism

DERIVED_FINITE_C_SIDE:
  beta_G:Q_G^lin->K_G^* isomorphism
  g_C,G=beta_G^* g_(K_G^*)
  R_C,G isomorphism
  ||[x]||_C=sup_(c!=0)|c^T x|/||c||_K

DERIVED_TRANSPORT:
  W3 rank-preserving inclusions isometric
  W3 restrictions are adjoints

AUTHORED_RESIDUE_COUNT = 4
LIVE_NULL_BRANCHES = none
PENDANT_TREE_REGRESSION = PASS

R_A_UNIT = U_A^(-2)
R_A_INVERSE_UNIT = U_A^(2)

READY_FOR_CROSS_REVIEW = yes
READY_FOR_DOR019_RULING = after cross-review
DOR_019 = RESERVED

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

V004 restores the finite complement metric that V003 dropped.  No new
authored field is introduced: after A2-R10 fullness, Gate-4 duality carries
the already-derived positive K metric to the finite C side uniquely.  The
completed R5 identification remains authored, but the finite `g_C`, `R_C`,
quotient norm, and pendant/tree theorem are derived inputs to that seam.

---

## 0. Preflight, custody, and verified authorities

The live questions-settled register and sidecar were verified before work;
the head was exactly `Q-379`.  The required final check was hash-verified
before reading.

| Artifact | Verified SHA-256 | Use |
|---|---|---|
| metric V003 final check | `8c72435ec53225d3dfe9fb4bba180f39ccf41009a025d36d42c404a3bce36571` | bounded restore specification |
| carrier metric V003 | `29ec770a8299fccadd68456b150f041eb64651ca2ba080b8a1c56c102f120fc9` | fullness/W3 cleanup baseline |
| carrier metric V002 | `7788e29da98be54e983a660768c0c70258e7d6d89eb51a2dafc4dbe17a9ea825` | finite C-side and regression source |
| fullness certificate | `f422a0340e253a72223f3c11d240b9b6a08b25a78ebf309085e84e965d8067ad` | A2-R10 theorem and W3 provenance |
| DoR-015 / field signature V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | finite quotient/current data |
| DoR-015 decision | `617bd51a70860d2cfb2066640630ba37ec289d56255ebbe1433bc0dfcba0159d` | exact W3 precision |
| square V004 | `abf6d366a5a7e375b9b53df75402f35d37f7c6a4b1bb0b10a44309ad3b0e1912` | R4 units and R5 interfaces |
| DoR-017 decision | `ee9d81bf78ab0ac9361cad5b48dde2b6b8b1e9fb0e28a4fdbba41e1c43db3e45` | symbolic `nu` and standing falsifier |
| divergence-datum descent | `c39de7a0ef5a29e92ded5fc961b54dfe933171ea291b221c38bf0aa3a9c0dcf3` | DP1–DP10 boundary |

```text
DOES_THE_OBJECT_EXIST = yes | V003 cleanup and dropped V002 content exist
IS_THE_VERSION_CURRENT = yes | Q-379
ARE_ITS_INPUTS_PRESENT = yes

CUSTODY = builder bounded restore; Lane 1 re-check required
STANDING = PROPOSED_NOT_ADOPTED
P_VERDICT_DECLARED = false
NUMERIC_RESPONSE_EVALUATED = false
ROOT_OR_K_STAR_EVALUATED = false
MEASURED_CONSTANT_COMPARISON = false
```

---

## 1. V003 cleanup retained — forced K form and fullness

### 1.1 Forced finite K form

For each admitted finite realization `G`, let

```text
K_G:=ker(B_G^T),
I_K,G(c):=u_c.
```

The retained A4 form forces

```text
s_G(c,d):=g_A4,G(I_K,G c,I_K,G d)
         =g_A4,G(u_c,u_d),                       (W1-1)

s_G(c,c)=||u_c||_A4^2>=0,
ker(s_G)=ker(I_K,G).                             (W1-2)
```

These equations are `TYPE-P | premises: DoR-015`.

### 1.2 A2-R10 fullness chain

The adopted framed transport obeys

```text
-i h_e^(-1)d h_e(a,theta)
 =(L_G a)_e+(B_G theta)_e,

(L_G a)_e=integral_(gamma_e)a,
(B_G theta)_e=theta_t-theta_s.                   (W1-3)
```

Field-signature V003 A2-R10 says this differential reaches every admitted
finite edge direction modulo the displayed frame action; V004 preserves
A2-R1 through R11; V005 does not retarget R10; DoR-015 ratifies V005.
Therefore

```text
image(L_G)+image(B_G)=E_G(edge),                 (W1-4)
q_G image(L_G)=E_G(edge)/image(B_G).             (W1-5)
```

If `c in K_G` and `u_c=0`, write arbitrary
`x=L_G a+B_G theta`.  Then

```text
c^T x=u_c(a)+(B_G^T c)^T theta=0.                (W1-6)
```

Nondegeneracy of the edge pairing gives

```text
ker(I_K,G)={0}.                                  (W1-7)
```

Hence

```text
g_K,G:=s_G
```

is positive definite on the full finite carrier, and

```text
R_K,G:K_G->K_G^*,
(R_K,G c)(d)=g_K,G(c,d)                          (W1-8)
```

is a finite Riesz isomorphism.

### 1.3 Directed core and completion

On the algebraic directed core `K_fin`, set

```text
||c||_K:=||I_K c||_A4.                           (W1-9)
```

DoR-015 W3 gives retained isometric inclusions, so this is a consistent
pre-Hilbert norm.  Completion extends `I_K` isometrically into
`J_phys^005`; its kernel remains zero.  The mathematical forced-norm
completion is derived.  Identifying R5's named `K_cycle` with it is part of
the authored completion seam.

```text
FINITE_FULLNESS = true | TYPE-P
FULL_FINITE_K_METRIC = true | TYPE-P
FORCED_K_COMPLETION_FAITHFUL = true | TYPE-P
```

---

## 2. W1 restore — finite C-side dual metric and Riesz map

### 2.1 V002 finite evaluation map, restored

The following V002 construction is reinstated at definition level, with
V003 fullness making the formerly visible carrier the full carrier,
`K_G^vis=K_G`:

```text
Eval_G:T_phys,G->K_G^*,
Eval_G(t)(c)=u_c(t).                              (W2-1)
```

It is injective by A4 separation.  At finite dimension, the rank of the
current family equals `dim K_G`, while separation gives
`rank(Eval_G)=dim T_phys,G`.  A2-R10 strengthens this to

```text
T_phys,G=Q_G^lin=E_G(edge)/image(B_G),
dim T_phys,G=dim K_G,
Eval_G is an isomorphism.                         (W2-2)
```

Equivalently, use the Gate-4 duality map

```text
beta_G:Q_G^lin->K_G^*,
beta_G([x])(c)=c^T x.                            (W2-3)
```

The map is well-defined because `c^T B_G theta=0`; it is injective by
Gate-4 separation and onto by equal finite dimension.

### 2.2 Derived finite C metric

The K metric induces the dual metric

```text
g_(K_G^*)(ell,m)
 :=g_K,G(R_K,G^(-1)ell,R_K,G^(-1)m).             (W2-4)
```

Restore the finite complement definition:

```text
C_G:=T_phys,G=Q_G^lin,

g_C,G(q,q')
 :=g_(K_G^*)(beta_G q,beta_G q'),                (W2-5)

R_C,G:C_G->C_G^*,
(R_C,G q)(q'):=g_C,G(q,q').                      (W2-6)
```

Because `beta_G` and `R_K,G` are isomorphisms, `g_C,G` is positive definite
and `R_C,G` is a finite Riesz isomorphism.  These are derived facts, not
DoR-019 authored fields.

```text
FINITE_C_DUALITY = true | TYPE-P
FINITE_G_C_POSITIVE = true | TYPE-P
FINITE_R_C_ISOMORPHISM = true | TYPE-P
```

### 2.3 Quotient-norm formula, restored

For `[x] in Q_G^lin`, the dual norm is

```text
||[x]||_C
 =sup_(0!=c in K_G) |c^T x|/||c||_K.             (W2-7)
```

This is representative-independent:

```text
c^T(x+B_G theta)=c^T x+(B_G^T c)^T theta=c^T x. (W2-8)
```

If `[x]=0`, `(W2-7)` is zero.  Conversely, if `(W2-7)` is zero, `[x]`
pairs to zero with every `c`; Gate-4 nondegeneracy gives `[x]=0`.

```text
FINITE_QUOTIENT_NORM_FORMULA = W2-7 | TYPE-P
QUOTIENT_REPRESENTATIVE_INDEPENDENCE = true | TYPE-P
```

### 2.4 Completed C-side residue, correctly scoped

The finite equations do not themselves identify R5's completed `C_prop`.
The live authored certificate remains:

```text
CARRIER_IDENTIFICATION_CERT := {
  R5 K_cycle is the faithful forced-K completion;
  R5 C_prop is its completed Hilbert dual;
  finite beta_G/Eval_G maps form a dense compatible core;
  completed beta is injective, onto, and closed-range;
  automorphism and restriction naturality;
  compatibility with D_017, rho_Gamma,N, and rho_H,N.
}.                                                (W2-9)
```

The certificate authors only the completed seam.  It does not author
`g_C,G`, `R_C,G`, or `(W2-7)`.

---

## 3. W1 restore — pendant/tree quotient theorem and regression

Let `[x]=[x+B_G theta]`.  Equation `(W2-8)` proves the quotient norm is
independent of the representative.

For a connected tree,

```text
K_G=ker(B_G^T)={0},
Q_G^lin={0}.                                     (W3-1)
```

The phase carrier is correctly scope-empty and has no nonzero scalar norm.

For a graph with a cycle and a pendant tree edge, varying only the pendant
coordinate is a vertex coboundary.  It pairs to zero with every conserved
cycle, hence

```text
||[x_pendant]||_C=0.                             (W3-2)
```

A nonzero cycle-holonomy quotient class has a conserved `c` with
`c^T x_cycle!=0`; therefore

```text
||[x_cycle]||_C>0.                               (W3-3)
```

```text
PENDANT_TREE_GAUGE_NORM = 0 | TYPE-P
RECORD_VISIBLE_CYCLE_NORM_POSITIVE = true | TYPE-P
PENDANT_WITNESS_DOES_NOT_REENTER = true
TREE_PHASE_DECLARED_PHYSICAL = false | TYPE-R
```

This is the restored permanent regression.

---

## 4. V003 cleanup retained — W3 and null-branch disposition

### 4.1 Rank-preserving W3 isometry

DoR-015 states:

```text
finite source restrictions are ADJOINTS of the retained isometric
inclusions; naive truncation is invalid.           (W4-1)
```

For `i_NM:C_N->C_M`,

```text
rho_MN=i_NM^*,
I_K,M j_K,NM=i_NM I_K,N.                         (W4-2)
```

Thus

```text
g_K,M(j_K c,j_K d)
 =g_A4,M(i_NM I_K,N c,i_NM I_K,N d)
 =g_K,N(c,d),                                    (W4-3)

rho_K,MN=j_K,NM^*.                               (W4-4)
```

By duality of `(W2-3)`, the finite C-side maps carry the corresponding
isometric/adjoint square.  No rank-preserving isometry is authored by
DoR-019.

W3 does not prove automorphism isometry, generic batching isometry, or a
cycle-creating physical upward quotient map.

### 4.2 Null branches remain closed

Fullness gives

```text
K_G/ker(I_K,G)=K_G/0=K_G.                        (W4-5)
```

The former quotient branch is the identity and the null-extension branch
is scope-empty.  Neither is live in V004.  The V002 quotient-naturality
lemma is banked only for a future family that weakens R10.

```text
LIVE_NULL_SECTOR = false | TYPE-R
LIVE_F_Q_N_BRANCH = false
```

---

## 5. Full derived carrier core

```text
DERIVED_CORE_019 := (
  K_G=ker(B_G^T),
  I_K,G(c)=u_c,
  g_K,G(c,d)=g_A4(u_c,u_d),
  image(L_G)+image(B_G)=E_G,
  ker(I_K,G)=0,
  R_K,G,
  beta_G:Q_G^lin->K_G^*,
  C_G=Q_G^lin,
  g_C,G=beta_G^*g_(K_G^*),
  R_C,G,
  ||[x]||_C=sup_(c!=0)|c^T x|/||c||_K,
  pendant/tree quotient theorem,
  faithful forced-norm Hilbert completion,
  W3 isometric rank-preserving inclusions and adjoint restrictions
).                                                (W5-1)
```

Every finite item in `(W5-1)` is derived or already ratified.  DoR-019
does not author it.

---

## 6. Four-item authored residue, unchanged from V003

```text
AUTHORED_RESIDUE_019 := (
  CARRIER_IDENTIFICATION_CERT,
  A4_AUTOMORPHISM_ISOMETRY_CERT,
  POSITIVITY_AND_REALITY_CONVENTION,
  CARRIER_UNIT_TORSORS_AND_R4_UNIT_SEAM
).                                                (W6-1)
```

### 6.1 Completion/carrier identification

R5 `K_cycle` is proposed to be the faithful forced-K completion, and R5
`C_prop` its completed Hilbert dual on `D_017`.  The finite `beta_G`,
`g_C,G`, and `R_C,G` are derived dense-core inputs, not fields hidden in
this authored row.

### 6.2 A4 automorphism isometry

Admitted exchanges/relabelings must preserve `g_A4`; reality/orientation
reversal must be antiunitary after complexification; stabilizers must
preserve the same form.  A disclosed invariant replacement or bounded-only
covariance is a live alternative.  The certificate voids if the S8-A
exchange, reversal, or a stabilizer changes the proposed form.

### 6.3 Positivity/reality completion convention

The proposed completed convention is the real positive form with Hermitian
complexification.  It may not alter any finite `g_K,G` or `g_C,G`, introduce
a null direction, or select a signature from response support.

### 6.4 Units and R4 seam

For `A in {C,K}`:

```text
R_A:A->A^*,
[R_A]=U_A^(-2),
[R_A^(-1)]=U_A^(2).                              (W6-2)
```

The unit table is unchanged:

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

No torsor member, numerical unit, rank, ratio, frame, or relation fixing
`nu` is selected.

---

## 7. Cleaned choice table

| Field | Live proposed content | Genuine alternatives | Minimality | Void condition |
|---|---|---|---|---|
| completed carrier identification | R5 `K_cycle` equals forced-K completion; `C_prop` equals its completed dual with finite `beta_G/g_C/R_C` dense core | different dense completion with proved equivalence; reject | only remaining finite-to-R5 seam | external enlargement, non-dense core, failed onto/closed-range proof, or D_017 mismatch |
| A4 automorphism isometry | retained A4 form invariant under exchanges/relabelings; reversal antiunitary | disclosed invariant replacement; bounded covariance without orthogonal propagation | W3 fixes stages, not automorphisms | S8-A exchange/reversal/stabilizer changes the form |
| positivity/reality convention | real positive completion with Hermitian complexification | real-only rigging; independently justified compatible convention | completes the derived finite forms without changing them | changed finite value, indefiniteness, response-selected signature, or null direction |
| carrier units | formal `U_C,U_K`, corrected Riesz powers, R4 seam | equivalent formal convention; reject | dimensional typing without numerical scale | fixes `nu`, rank ratio, numeric value, or desired response |
| reject | no DoR-019 adoption | — | preserves current TYPE-U seam | — |

No quotient/null carrier branch is live.

---

## 8. Transport and restriction ledger

| Map/operation | Standing | Provenance/scope |
|---|---|---|
| finite `I_K,G` | injective | A2-R10 |
| finite `R_K,G` | isomorphism | derived positive K form |
| finite `beta_G` | isomorphism | Gate-4 duality + fullness |
| finite `R_C,G` | isomorphism | derived dual C form |
| quotient norm | representative-independent | `(W2-7)`–`(W2-8)` |
| rank-preserving K inclusion | isometric | DoR-015 W3 |
| rank-preserving C dual map | isometric/adjoint on dual square | W3 + beta naturality |
| finite restrictions | adjoints, never naive truncations | DoR-015 W3 |
| realization automorphism | algebraically covariant; metric isometry proposed | authored residue |
| reality reversal | semilinear; antiunitarity proposed | authored residue |
| batching | existing covariance retained; generic isometry not claimed | bounded/proved scope |
| cycle creation | no physical upward quotient map | Z7 retained |
| `rho_Gamma,N` | scalar derivative square retained | square V004 |
| `rho_H,N` | R5-generated Hessian cube retained | metric upgrade after DoR-019 |

---

## 9. DP1/DP7 executability on both carrier sides

```text
DP1_FINITE_K_FORM_RIESZ = TYPE-P
DP1_FINITE_C_FORM_RIESZ = TYPE-P
DP1_QUOTIENT_NORM = TYPE-P
DP1_FORCED_COMPLETION = TYPE-P
DP1_R5_IDENTIFICATION_AND_UNITS = TYPE-U pending DoR-019
DP1_DIV_G_DELTA_G_ALPHA_DIV = TYPE-U

DP7_RANK_PRESERVING_K_NATURALITY = TYPE-P | DoR-015 W3
DP7_RANK_PRESERVING_C_NATURALITY = TYPE-P | dual W3 square
DP7_AUTOMORPHISM_METRIC_ISOMETRY = TYPE-U pending DoR-019
DP7_GENERATOR_NATURALITY = TYPE-U
DP7_FULL_D_G_HANDOFF = no null obstruction | fullness proved

DP1_DP10_DISCHARGED_BY_METRIC = false
```

The restored C-side makes the carrier interface executable on both sectors;
it does not instantiate the divergence datum or generator.

---

## 10. W4 — full battery and regression suite

### B1 — R10 admissibility regression

The old model

```text
Q_G^lin=R^2,
K_G=R^2,
T_phys,G=span{e_1}
```

has `ker I_K=span{e_2}` but violates
`image(L_G)+image(B_G)=E_G`.  It is rejected before metric formation.

```text
R2_ADMITTED_BY_DOR015 = false | TYPE-R | A2-R10 failure
```

### B2 — fullness kernel

For arbitrary `c` with `u_c=0`, `(W1-6)` evaluates it against every edge
vector and forces `c=0`.

```text
FULLNESS_KERNEL_TEST = PASS
```

### B3 — finite C-side evaporation

Trace any nonzero `q in Q_G^lin` through `beta_G`, `(W2-5)`, and `(W2-6)`.
Gate-4 injectivity gives `beta_G q!=0`; the dual K metric gives
`g_C,G(q,q)>0`; `R_C,G q` is displayed.  No implementation can vary the C
metric while preserving these equations.

```text
FINITE_C_METRIC_PRESENT = PASS
FINITE_R_C_PRESENT = PASS
```

### B4 — quotient representative

Replace `x` by `x+B_G theta`.  Equation `(W2-8)` leaves every pairing and
therefore the supremum norm unchanged.

```text
QUOTIENT_NORM_REPRESENTATIVE_INDEPENDENT = PASS
```

### B5 — pendant/tree regression

On a tree, both K and Q vanish.  On a cyclic graph, a pure pendant change is
a coboundary and has norm zero, while a nonzero cycle class has positive
norm by `(W3-3)`.

```text
PENDANT_TREE_REGRESSION = PASS
```

### B6 — response-support attack

No finite metric definition contains a Hessian, Schur block, stationary
root, `p`, or desired response.  The completion convention voids if selected
by response support.

```text
RESPONSE_SUPPORT_TUNING = NOT_FOUND | PASS
```

### B7 — hidden-scale attack

The Riesz powers are corrected, carrier units remain formal, and `nu`
remains a symbolic action unit.

```text
HIDDEN_NU_FIXING = NOT_FOUND | PASS
```

### B8 — W3 double charge

Rank-preserving K and C isometry appear only in the derived ledger.  They
are absent from the authored choice table.

```text
W3_ISOMETRY_REAUTHORED = false | PASS
```

### B9 — automorphism anisotropy

The form `diag(1,2)` fails the rank-two exchange.  It is rejected by the
authored automorphism certificate, not mislabeled as excluded by W3.

```text
A4_AUTOMORPHISM_ISOMETRY_ASSUMED = false | PASS
```

### B10 — unit regression

Every live row uses `[R_A]=U_A^-2` and `[R_A^-1]=U_A^2`.

```text
R7_UNIT_POWER = PASS
```

### B11 — null-branch resurrection

Fullness gives `K/ker I_K=K`; no quotient/null alternative occurs in the
live choice table.

```text
LIVE_NULL_OR_QUOTIENT_BRANCH = false | PASS
```

### B12 — cycle-creating upward map

W3 is used only on rank-preserving inclusions.  No adjoint is promoted to
the Z7-refuted physical upward quotient map.

```text
Z7_BOUNDARY_RETAINED = true | PASS
```

### B13 — external enlargement

A completed direction orthogonal to every finite K and C datum violates the
density and closed-range clauses of `CARRIER_IDENTIFICATION_CERT`.

```text
UNWEIGHED_EXTERNAL_R5_DIRECTION_ADMITTED = false | PASS
```

---

## 11. W3 — true delta table versus V002

Every V002 substantive section is accounted as follows:

| V002 section/content | V004 standing | Exact delta from V002 |
|---|---|---|
| S1 forced semiform | retained | fullness now makes it positive definite on full K |
| S2 injectivity/countermodel | theorem superseded by A2-R10 | countermodel moved to inadmissibility regression |
| S2 visible quotient | quotient-natural lemma banked | live quotient branch removed because kernel is zero |
| S2 D_G obstruction | antecedent empty | full handoff has no null obstruction |
| S3 two-level carrier | collapsed to full K | null layer removed by theorem |
| S4.1 finite evaluation/C metric | **restored** | `K_vis=K`; `Eval/beta`, `g_C`, explicit `R_C` present |
| S4.2 completed carrier cert | retained | narrowed to one full-carrier completion |
| S5 A4 isometry | automorphism row retained | rank-preserving stage isometry reclassified derived by W3 |
| S6 unit algebra | retained with the same equations and unit table | no change |
| S7 choice table | retained fields with cleanup | F/Q/N rows removed; four-item residue only |
| S8 restriction ledger | retained and expanded | C-side dual W3 row restored |
| S9 DP1/DP7 | retained and expanded | C-side finite interfaces restored; fullness/W3 derived |
| S10 battery | retained and expanded | inadmissibility replaces admitted R2; pendant/C regressions restored |
| S11 delta | replaced by this two-baseline audit | true content-level accounting |
| S12 final board | retained with fullness cleanup | full finite C/K derived core displayed |

No V002 passing provenance, unit, door, no-selection, Z7, or DP boundary is
removed.

---

## 12. W3 — true delta table versus V003

| V003 content | V004 standing | Exact delta from V003 |
|---|---|---|
| preflight/fullness proof | unchanged in substance | none |
| null-branch cleanup | unchanged | none |
| W3 rank-preserving derivation | unchanged | none |
| finite K metric/R_K | unchanged | none |
| finite C metric | restored as `(W2-3)`–`(W2-5)` | added derived equations |
| finite R_C | restored as `(W2-6)` | added derived equation and proof |
| quotient norm | restored as `(W2-7)`–`(W2-8)` | added derived formula/proof |
| pendant/tree theorem | restored as Section 3 | added permanent regression |
| derived core | expanded only by restored C-side items | provenance corrected |
| four-item authored residue | unchanged | completion row narrowed to consume, not author, finite C data |
| choice table | same four live fields plus reject | finite dense-core wording restored |
| restriction ledger | expanded by finite C dual row | no K-side change |
| DP1/DP7 | expanded by C-side interface rows | no divergence status change |
| battery | V003 ten attacks retained | C evaporation, quotient, pendant tests added |
| Riesz units | unchanged | none |
| gates/fences | unchanged | none |

The only positive additions relative to V003 are the four requested restored
objects and the checks/accounting that make their presence failure-capable.

---

## 13. Exact DoR-019 board

### 13.1 Derived/ratified core

| Item | Standing |
|---|---|
| forced finite K form | **DERIVED / TYPE-P**, DoR-015 |
| A2-R10 fullness and `ker I_K=0` | **DERIVED / TYPE-P** |
| finite `R_K` | **DERIVED / TYPE-P** |
| finite Gate-4 `beta_G` | **DERIVED / TYPE-P** |
| finite C metric and `R_C` | **DERIVED / TYPE-P** |
| quotient-norm formula | **DERIVED / TYPE-P** |
| pendant/tree quotient theorem | **DERIVED / TYPE-P** |
| faithful forced-norm completion | **DERIVED / TYPE-P** |
| rank-preserving K/C isometry | **RATIFIED PREMISE / TYPE-P**, DoR-015 W3 |
| adjoint finite restrictions | **RATIFIED PREMISE / TYPE-P**, DoR-015 W3 |

### 13.2 Four authored items

| Item | Exact DoR-019 addition |
|---|---|
| R5 completed-carrier identification | identify `K_cycle` and `C_prop` with the forced completions/duals on `D_017`, using the derived finite dense core |
| positivity/reality completion convention | real-positive/Hermitian completed convention, no changed finite values or new nulls |
| A4 automorphism isometry | exchanges/relabelings orthogonal, reversal antiunitary, stabilizers isometric |
| carrier units/R4 seam | formal `U_C,U_K`, corrected Riesz powers, `nu` symbolic |

DoR-019 would ratify only these four authored items while citing the derived
core as their mandatory foundation.  The principal may adopt this residue,
request a different carrier-only completion satisfying the same core, or
reject.  No choice is made here.

### 13.3 Standing falsifier

The package voids if it:

1. changes any finite `g_K`, `g_C`, `R_K`, or `R_C` equation;
2. violates R10 fullness or admits the old countermodel;
3. gives a pendant/tree coboundary positive physical norm;
4. gives a nonzero cycle quotient zero norm;
5. introduces a finite or completed null direction;
6. changes W3's isometric-inclusion/adjoint-restriction precision;
7. claims batching/cycle-creation isometry beyond W3;
8. fails the authored automorphism/reality certificate;
9. reverses the Riesz unit power or fixes `nu`;
10. uses response support or any desired downstream result.

```text
CARRIER_METRIC_V004 = BOUNDED_RESTORE_COMPLETE

DERIVED_CORE_COMPLETE:
  finite K metric/R_K = yes
  A2-R10 fullness = yes
  finite C metric/R_C = yes
  quotient norm = yes
  pendant/tree theorem = yes
  faithful forced completion = yes
  W3 rank-preserving isometry/adjoints = yes

AUTHORED_RESIDUE_EXACTLY_FOUR:
  R5 completed-carrier identification
  positivity/reality completion convention
  A4 automorphism isometry
  carrier units/R4 seam

LIVE_NULL_BRANCHES = none
R10_COUNTERMODEL_REGRESSION = installed
PENDANT_TREE_REGRESSION = installed_and_passed
BATTERY = 13 attacks run
DELTA_V002 = complete
DELTA_V003 = complete
DP1_DP7 = both carrier sides restored

READY_FOR_CROSS_REVIEW = yes
READY_FOR_DOR019_RULING = after cross-review
PROPOSAL_STANDING = PROPOSED_NOT_ADOPTED
DOR_019 = RESERVED

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
