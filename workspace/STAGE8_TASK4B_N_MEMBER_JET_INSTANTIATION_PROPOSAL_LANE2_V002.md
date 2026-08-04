# STAGE 8 TASK 4B — N-MEMBER JET INSTANTIATION PROPOSAL — LANE 2 V002

Date: 2026-08-03  
Task: PASTE 465 / Task 4b  
Lane: CODEX LANE 2  
Status: **PROPOSED_NOT_ADOPTED — TWO-SHAPE DoR-018 FIBER; NO SHAPE SELECTED**

```text
REGISTER_HEAD_AT_PREFLIGHT = Q-384
PREFLIGHT = PASS

DOR_019 = IN_FORCE
CARRIER_METRIC_V005_SHA256 =
  2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961

LEAD_RESULT = BOTH_MINIMAL_CARRIER_SHAPES_CONSTRUCTED_AND_DP_AUDITED

SHAPE_K:
  phi_K(c,k)=nu f(||k||_K^2)
  D_C phi_K=D_C^2 phi_K=D_C D_K phi_K=D_K D_C phi_K=0

SHAPE_CK:
  phi_CK(c,k)=nu (1+(1/2)||c||_C^2) f(||k||_K^2)
  all four Hessian blocks displayed below

f(s)=exp(-1/s) for s>0; f(0)=0

DIVERGENCE_PROVENANCE:
  neither shape derived from delta_div
  both shapes openly authored and DP1-DP10 failure-capable
  LOG_DIVERGENCE_PROVENANCE = false

DOR_018_FIBER = {K,CK,reject}
SHAPE_SELECTED_BY_LANE = false
TARGET_AWARE_JUSTIFICATION = none

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

DoR-019 supplies the positive completed C/K geometry, Riesz maps, unit
duality classes, automorphism isometries, W3 restrictions, and R4-only
cross-sector routing that V001 lacked.  It does not select an action shape.
The DP reach theorem proves that the extensional divergence datum also does
not select one.  V002 therefore carries the two lowest carrier-structural
support classes together and leaves the choice to DoR-018.

---

## 0. Preflight, custody, and authorities

The live register was checked before substantive work and its head was
exactly `Q-384`.  The DoR-019 decision and adopted metric were read only
after their hashes matched.

| Authority | Verified SHA-256 | Use |
|---|---|---|
| DoR-019 decision | `6ab72b0cb3a93e123eb1d3c5088fc83361d86c6dc739f0a886380dbd2d143f1f` | ratified metric/unit package and regressions |
| metric V005 | `2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961` | C/K norms, Riesz maps, unit classes, routing |
| germ V001 | `0a7b45a68899054be3266e2f1a2fb23806e7ba75e73a6326c683eebda216fac1` | passing flatness/jet/Schur mechanics and killed claims |
| DP1–DP10 provenance standard | `c39de7a0ef5a29e92ded5fc961b54dfe933171ea291b221c38bf0aa3a9c0dcf3` | shape-thin datum and certificate |
| V001 adjudication | `2e1b011069043c1cc03277178be061a8b7d1704d2146be97eb799965aef9c679` | G2/G3/G7 repair standard |
| response computation | `be570c182ef875b557395b62c382ee875420ac0462e2efb5774e9600f794b27a` | confirmed Schur consumer |
| response cross-verification | `cac131d949a917576e30332b2f4ec76ca7db57d6d4683e91cfeac658994c499b` | tags, zero theorem, jet boundary |
| square V004 | `abf6d366a5a7e375b9b53df75402f35d37f7c6a4b1bb0b10a44309ad3b0e1912` | R1–R5, `rho_H,N`, Schur cube |
| DoR-017 decision | `ee9d81bf78ab0ac9361cad5b48dde2b6b8b1e9fb0e28a4fdbba41e1c43db3e45` | N member, symbolic `nu`, void discipline |

```text
CUSTODY = full gate; cross-review and principal ruling required
PROPOSAL_STANDING = PROPOSED_NOT_ADOPTED
DOR_018 = RESERVED
P_VERDICT_COMPUTED = false
NUMERIC_RESPONSE_VALUE_COMPUTED = false
```

### 0.1 Ownership and symbols

```text
c in C_prop       = complement carrier coordinate;
k in K_cycle      = record-visible cycle coordinate;
R_C,R_K           = ratified same-sector Riesz maps;
nu                = symbolic DoR-017 normalizer, not evaluated;
p                 = base label, absent from both profile definitions;
K in Shape K      = sector name, not shell cutoff or K_*;
N member          != finite stage N;
shape consequence != shape justification.
```

### 0.2 V001 kill-to-repair accounting

| V001 kill | V002 repair |
|---|---|
| G2/J3 response-support tuning | K and CK both retained; every shape clause justified before response loading and solely by carrier invariance/minimal degree |
| G3 missing metric, units, covariance | DoR-019 premises consumed; R1-COV, Riesz naturality, units, and `rho_H,N` cube proved below |
| G7 cycle-creating stationary overclaim | only vertical action/Hessian cocycles claimed; stationary-root restriction remains `TYPE-U` |

The passing V001 finite-flatness, zero-degeneration, and Schur mechanics are
recomputed rather than inherited by assertion.

---

## 1. Common carrier construction fixed before either consequence

Let

```text
Y_G=C_G direct-sum K_G,
S_G=C_G direct-sum {0},
q_C,G(c):=(1/2)||c||_C^2,
s_K,G(k):=||k||_K^2.                              (B0-1)
```

The norms and their unit-valued Hilbert classes are ratified by DoR-019.
`q_C` and `s_K` are dimensionless scalar invariants; no unit-class
representative is selected.  For every admitted automorphism `alpha`,

```text
q_C,G'(alpha_C c)=q_C,G(c),
s_K,G'(alpha_K k)=s_K,G(k).                       (B0-2)
```

Define the parameter-free smooth flat gate

```text
f(s):={exp(-1/s),s>0;0,s=0},
f_1(s)=f(s)/s^2,
f_2(s)=f(s)(s^(-4)-2s^(-3)) for s>0.             (B0-3)
```

Every derivative of `f(s_K(k))` vanishes at `k=0`.  This is the common
finite-flatness mechanism.  The exact gate is an authored representative of
the nonzero smooth-flat class; it is not claimed unique or divergence-
derived.

### 1.1 Shape-class minimality, not outcome minimality

The admitted isometry group leaves two lowest carrier support classes:

```text
K:  an invariant depends on s_K only;
CK: an invariant depends on the canonical quadratic q_C and s_K.
```

Within K, `f(s_K)` is the parameter-free nonzero flat representative.  Within
CK, `(1+q_C)f(s_K)` is the lowest-degree even normalized complement coupling:
it equals the K representative at `c=0`, its complement Hessian is `R_C`,
and it contains no chosen covector or extra scale.  These are carrier-only
facts.  Neither support class is preferred, and the DP theorem says neither
is forced by `delta_div`.

### 1.2 Authored choice table

| Field | Proposed alternatives carried | Carrier-only minimality | Void condition |
|---|---|---|---|
| support shape | K; CK; reject | K and CK are the two lowest invariant support classes; both remain live | either shape selected by a response consequence |
| K radius | `s_K=||k||_K^2` | canonical quadratic invariant of ratified K geometry | selected cycle/basis, extra weight, or failed isometry |
| CK complement factor | `1+q_C`, `q_C=||c||_C^2/2` | origin-normalized lowest even nonconstant invariant of ratified C geometry | response-block justification, selected covector, or extra width |
| flat gate | displayed `exp(-1/s)` representative; another fully certified nonzero smooth-flat gate; reject | explicit parameter-free representative, with alternatives retained | hidden scale, nonflat finite jet, target-fitted profile |
| generator provenance | authored shape tag plus extensional `delta_div` orbit | makes shape freedom visible under DP9 | calls the shape divergence-determined without DP2–DP6 content |
| normalizer | coefficient extraction `Norm(nu psi_S)=nu` | preserves DoR-017 symbolic scaling line | numeric value, nonlinear hidden scale, or `nu` fixed by carrier units |
| stationary family | complete R5 local branch family | no root/member selected | omitted branch, evaluated root, response-based branch rule |
| cycle creation | R2 vertical cocycle only | strongest statement DoR-019 permits without upward map | assertion of `(BC-6)` without a new theorem |

Everything in this table is `PROPOSED_NOT_ADOPTED` except the consumed
DoR-017/DoR-019 premises.  No lane choice is made among K, CK, and reject.

---

## 2. B1 — Shape K, cycle-only

### 2.1 Definition and generation

```text
psi_K,G(c,k):=f(s_K,G(k)),
phi_K,G(c,k):=nu psi_K,G(c,k).                    (BK-1)
```

Shape K consumes only the ratified K norm.  It is smooth, real, invariant,
and all-orders flat on `S_G`.  For symbolic nonzero `nu`, it is nonzero off
the active section.

### 2.2 Exact jets

Write `k^flat=R_K k`.  For `s=s_K(k)>0`,

```text
D_C phi_K=0,
F_CC^K:=D_C^2 phi_K=0,
F_CK^K:=D_C D_K phi_K=0,
F_KC^K:=D_K D_C phi_K=0,

D_K phi_K=2nu f_1(s)k^flat,
F_KK^K:=D_K^2 phi_K
 =nu[2f_1(s)R_K+4f_2(s)k^flat tensor k^flat].    (BK-2)
```

At `k=0`, all expressions are zero.  The only nonzero direct member block
is the K/K block.

### 2.3 Stationary structure and neutral response consequence

The complement stationarity equation is unchanged:

```text
D_C(Gamma_base+phi_K)=D_C Gamma_base=0.           (BK-3)
```

Hence Shape K consumes the complete covariant base complement-critical
family supplied by R5; it selects no root.  Structurally,

```text
H_CC^K=H_CC^base,
H_CK^K=H_CK^base,
H_KC^K=H_KC^base,
H_KK^K=H_KK^base+F_KK^K.                         (BK-4)
```

Thus the complement inverse and mixed blocks are base-only, while the K/K
block carries the member.  This is a consequence computed after `(BK-1)`
was fixed, not a reason to choose Shape K.  No response value or p verdict
is taken.

---

## 3. B2 — Shape CK, complement-coupled

### 3.1 Definition and carrier-only justification

```text
a_C,G(c):=1+q_C,G(c)=1+(1/2)||c||_C^2,
psi_CK,G(c,k):=a_C,G(c)f(s_K,G(k)),
phi_CK,G(c,k):=nu psi_CK,G(c,k).                  (BCK-1)
```

Every defining justification is carrier-structural:

| Choice | Carrier-only justification | Response content consulted? |
|---|---|---|
| `s_K=||k||^2` | least nonconstant isometry invariant on K | no |
| `q_C=||c||^2/2` | canonical quadratic energy of the ratified C metric | no |
| `1+q_C` | normalized at the common origin and lowest even polynomial degree | no |
| `f(s)` | explicit nonzero parameter-free smooth-flat representative | no |
| product | lowest algebraic coupling of the two declared scalar invariants | no |
| coefficient `nu` | already-ratified symbolic N-member normalizer | no |

No line cites `H_CC`, `H_CK`, Schur support, cancellation, survival, p, or a
desired output.  The killed V001 J3 justification is absent.

### 3.2 Exact jets

Write `c^flat=R_C c`, `k^flat=R_K k`.  For `s>0`,

```text
D_C phi_CK=nu f(s)c^flat,
F_CC^CK:=D_C^2 phi_CK=nu f(s)R_C,

F_CK^CK:=D_C D_K phi_CK
 =2nu f_1(s)c^flat tensor k^flat,

F_KC^CK:=D_K D_C phi_CK=(F_CK^CK)^T,

D_K phi_CK=2nu a_C(c)f_1(s)k^flat,
F_KK^CK:=D_K^2 phi_CK
 =nu a_C(c)[2f_1(s)R_K
             +4f_2(s)k^flat tensor k^flat].      (BCK-2)
```

All jets vanish at `k=0`.  The mixed tensor is an R4-typed bilinear map
`K->C^*` (and its reality adjoint), not a vector conversion between C and K.

### 3.3 Stationary structure and neutral response consequence

Retain the complete local R5 branch family solving

```text
D_C Gamma_base(p;c,k)+nu f(s_K(k))R_C c=0.        (BCK-3)
```

No branch or root is evaluated.  Structurally all four total blocks may
receive the displayed member jets:

```text
H_AB^CK=H_AB^base+F_AB^CK.                        (BCK-4)
```

This statement is reported only after `(BCK-1)` and its carrier-only choice
ledger were frozen.  It neither favors CK nor states a response outcome.

---

## 4. B3 — common certificates on ratified geometry

### 4.1 `nu` homogeneity and zero degeneration

For either `S in {K,CK}` and dimensionless symbolic `lambda`,

```text
nu->lambda nu =>
phi_S->lambda phi_S,
D phi_S->lambda D phi_S,
D^2 phi_S->lambda D^2 phi_S.                     (BC-1)
```

The carrier-unit classes do not change and no equation fixes `nu`.  At
`nu=0`, each germ and every direct jet equals the Z member exactly.  A
stationary family converges to its base family only on a uniform R5 inverse
chart; no statement crosses an inverse-support jump.

### 4.2 R1-COV and the completed Hessian cube

DoR-019 makes every admitted realization automorphism isometric on C and K.
Equations `(B0-2)` therefore give

```text
phi_S,G'(alpha_C c,alpha_K k)=phi_S,G(c,k).       (BC-2)
```

Differentiate twice.  Riesz naturality and the signed/antiunitary reality
action transport every covector and tensor index, yielding

```text
H_AB,G'^S alpha_B=alpha_H,A H_AB,G^S.             (BC-3)
```

For every completed-to-finite restriction in square V004, instantiate the
finite bottom germ independently by the same finite formula.  The metric
V005 restriction/Riesz cubes then give

```text
rho_H,N H_AB^S=H_AB,N^S rho_D,N                  (BC-4)
```

on the declared R5 domain.  Composing `(BC-3)` with `(BC-4)` is exactly the
ratified `rho_H,N` automorphism cube.  Unlike V001, no metric premise is
conditional.

### 4.3 Cycle-creating scope — G7 repair

Three distinct claims are kept separate.

1. **Completed-to-one-stage restriction:** `(BC-4)` is proved for each N.
2. **Rank-preserving stage arrows:** W3 isometry makes the action, Hessian,
   and stationary family natural on the already-certified R5 branch scope.
3. **Cycle-creating arrows:** DoR-019 provides a new carrier class at M and
   expressly supplies no upward quotient map.  Define only the R2 vertical
   action/Hessian differences

```text
v_MN^S:=phi_M^S-phi_N^S compose rho_MN,
DeltaH_MN^S:=H_M^S-H_N^S compose rho_D,MN.        (BC-5)
```

They satisfy the three-stage cocycle by telescoping.  V002 does **not** claim

```text
rho_C,N(Crit_M^S)=Crit_N^S                       (BC-6)
```

for a cycle-creating arrow.  Shape CK is subject to the adjudication's
explicit countermodel; Shape K inherits only whatever base-critical
naturality R5 independently proves.  No new stationary-root naturality is
deduced from `(BC-5)`.

```text
CYCLE_CREATING_ACTION_COCYCLE = proved
CYCLE_CREATING_HESSIAN_COCYCLE = proved
CYCLE_CREATING_STATIONARY_RESTRICTION = TYPE-U | not claimed
G7_OVERCLAIM = removed
```

### 4.4 NO_IMPLICIT_CROSS_SECTOR_UNIT

Shape K has no mixed member expression.  Shape CK uses only

```text
F_CK:K->C^*,
F_KC:C->K^*,
[F_CK]=[F_KC]=U_action U_C^(-1)U_K^(-1),          (BC-7)
```

the ratified R4 mixed-block seam.  `R_C` and `R_K` act only in their own
sectors.  No bare `C->K`, `K->C`, `U_beta`, unit representative, or
coordinate identity occurs.  In the Schur product,

```text
[H_KC Inv_CC H_CK]=U_action U_K^(-2)=[H_KK],      (BC-8)
```

so subtraction is lawful and `nu` remains symbolic.

---

## 5. DP1–DP10 certificate, run for both shapes

The DP theorem is obeyed rather than weakened: neither shape is advertised
as determined by the thin datum.  The DoR-018 shape tag is explicit authored
input.

Define proposal-level datum carriers

```text
Div_G^S:=Orbit(delta_div,G) x {S}, S in {K,CK},
alpha_Div^S(delta,S):=(alpha_Div delta,S).        (DP-0)
```

The discrete tag is the DoR-018 choice; it is not hidden inside
`delta_div`.

| DP row | Shape K | Shape CK | Certificate/result |
|---|---|---|---|
| DP1 datum | `Div_G^K`, inherited datum units/topology, discrete K tag | `Div_G^CK`, same with CK tag | **PASS_WITHIN_PROPOSAL**; shape tag openly authored |
| DP2 log relation | no shell/C-L3 coefficient consumed | same | **PASS** with `LOG_DIVERGENCE_PROVENANCE=false` |
| DP3 depth | `Depth_K(delta,K)=s_K` as invariant scalar functional | `Depth_CK(delta,CK)=(q_C,s_K)` | executable; image displayed; datum-orbit differences lie in kernel; **PASS_WITH_DISCLOSURE** |
| DP4 accumulation | vertical differences of `s_K` | vertical differences of `(q_C,s_K)` | Hilbert/P2 topology, zero on rank-preserving identity extension, cycle-creating cocycle `(BC-5)`; **PASS** |
| DP5 map handoff | K radius is formed after the ratified prefix-to-cycle descent | same K handoff plus ratified R5 C carrier | no rival CycleMap or endpoint route; **PASS** |
| DP6 generator | `(delta,K)->nu f(s_K)` | `(delta,CK)->nu(1+q_C)f(s_K)` | executable and target-blind; neither output used in membership; **PASS** |
| DP7 naturality | `(BC-2)`–`(BC-4)` | same | stabilizers, reality, batching, identity extension covered; cycle creation scoped by `(BC-5)`; **PASS_WITH_STATED_SCOPE** |
| DP8 finite square | independent finite `b_N^K` | independent finite `b_N^CK` | equals completed restriction by direct formula; active Q-243/Q-279 jets zero; **PASS** |
| DP9 residual disclosure | flat-gate representative, K support, `nu`, stationary branch family authored/disclosed | flat gate, CK support, quadratic factor, `nu`, branch family authored/disclosed | no uniqueness claim; **PASS** |
| DP10 target/origin | DoR-017 datum + DoR-019 geometry; chronology Section 7 | same | no target, continuum import, or output-defined membership; **PASS** |

The independently finite legs are

```text
b_N^K(c_N,k_N):=nu f(||k_N||_K^2),
b_N^CK(c_N,k_N):=nu(1+(1/2)||c_N||_C^2)
                         f(||k_N||_K^2).          (DP-1)
```

They are constructed from finite ratified metrics, not copied from the
completed germ.  Every active reference has `k_N=0`, so every member jet is
zero to all orders and Q-243/Q-279 are reproduced exactly.

```text
DP_CERTIFICATE_K = PASS_WITHIN_PROPOSAL
DP_CERTIFICATE_CK = PASS_WITHIN_PROPOSAL
DIVERGENCE_DETERMINES_SHAPE = false
```

---

## 6. Minimal-stage structural checks

### 6.1 Reciprocal loop

In a temporary orthonormal chart `k=t u` (the result is chart invariant),

```text
F_KK^K=nu[2f_1(t^2)+4t^2f_2(t^2)]R_K,            (MS-1)

F_CC^CK=nu f(t^2)R_C,
F_CK^CK=2nu t f_1(t^2)c^flat tensor u^flat,
F_KK^CK=nu(1+q_C(c))
              [2f_1(t^2)+4t^2f_2(t^2)]R_K.      (MS-2)
```

At `t=0`, every term is exactly zero.  No numerical point or response is
evaluated.

### 6.2 S8-A rank-two stage

For arbitrary `k` in the complete rank-two carrier, use invariant `s=||k||^2`.
The signed exchange preserves `s`, sends `k^flat` covariantly, and conjugates
`k^flat tensor k^flat`.  Equations `(BK-2)` and `(BCK-2)` therefore satisfy
R1-COV without selecting `c_1`, `c_2`, `c_3`, or an orientation.

---

## 7. B4 — DoR-018 fiber and anti-tuning chronology

### 7.1 Exact fiber

| DoR-018 item | Certified authored content | Neutral structural response consequence | Remaining TYPE-U |
|---|---|---|---|
| Shape K | cycle-only `nu f(s_K)`, DP table, K jets, base complement critical family | member correction appears only in K/K; complement inverse and mixed blocks remain base-only | global chart extension; cycle-creating stationary restriction; branch-uniform output |
| Shape CK | `nu(1+q_C)f(s_K)`, DP table, four jet blocks, complete R5 branch family | all four member jet blocks may enter the already-ratified Schur structure | same three doors |
| reject | no component instantiation | response remains at the confirmed TYPE-U jet boundary | shape/jet object remains absent |

No item is recommended.  `nu` remains symbolic in both live shapes.

### 7.2 Order-of-construction ledger

```text
T0  DoR-017 fixes the abstract N member and symbolic nu.
T1  DoR-019 fixes C/K geometry, units, isometries, and R4 routing.
T2  DP theorem fixes the rule: shape is authored and must be target-blind.
T3  enumerate the two minimal carrier support classes {K,CK}; retain both.
T4  fix q_C, s_K, and the parameter-free flat representative by carrier
    invariance, degree, origin normalization, and finite flatness only.
T5  define Gen, finite legs, vertical cocycles, and normalizer.
T6  prove covariance, restriction scope, units, and DP1-DP10.
T7  differentiate to obtain jets.
T8  only now load the pre-existing Schur consumer and report neutral
    block-placement consequences.
```

Because both support classes survive through T8, no consequence can select
between them inside this artifact.

```text
ANTI_TUNING_ATTESTATION = PASS_WITHIN_PROPOSAL
CONSEQUENCE_READ_BEFORE_CHOICE_FIXED = false
```

---

## 8. B5 — hostile battery

| Attack | Shape K | Shape CK | Result |
|---|---|---|---|
| reverse engineer from response support | a tuner seeking mixed blocks would reject K, but K remains live | a tuner might prefer CK, but no preference is made and its definition is fixed by carrier ledger T0–T6 | **PASS**; outcome cannot select because both remain |
| finite flatness/Q-243/Q-279 | every active jet zero | every active jet zero | **PASS** all orders |
| rank-two cycle-selective witness | depends only on full `||k||^2` | depends only on full C/K norms | **PASS**; no selected cycle |
| pendant/tree witness | pendant lies in quotient kernel before norm | same | **PASS**; zero physical norm |
| G7 cycle-creating root attack | no new root claim beyond base R5 scope | explicit countermodel acknowledged; `(BC-6)` not claimed | **PASS_BY_SCOPE** |
| implicit cross-sector unit | no mixed member arrow | only R4 `F_CK/F_KC`; Schur units `(BC-8)` | **PASS** |
| zero degeneration | direct germ/jets linear in `nu`; uniform-chart boundary stated | same | **PASS_WITH_BOUNDARY** |
| stabilizer/orbit attack (fresh) | equal-radius directions receive equal values; tensors transform covariantly | same for both radii; no orbit representative | **PASS** |
| hidden scale/`nu` calibration (fresh) | flat gate has no width; unit classes do not fix `nu` | same; `1/2` is quadratic-form convention, not scale calibration | **PASS** |

The reverse-engineering test does not prove either formula uniquely forced by
the divergence datum; it proves the proposal does not choose between the two
carrier-minimal support classes by reading their consequences.

```text
SELF_KILL_ATTACKS_RUN = 9
SELF_KILL_FAILURE_FOUND = false
J3_RESPONSE_FACING_JUSTIFICATION = absent
```

---

## 9. Doors, operation ledger, and final board

### 9.1 Doors

| Door | Standing | Would build |
|---|---|---|
| global stationary-germ extension | `TYPE-U` beyond certified R5 charts | covariant global extension preserving the chosen shape and R2 cocycles |
| cycle-creating stationary restriction | `TYPE-U` for both shapes | theorem proving `(BC-6)` or a separately ratified stationary transport |
| branch-uniform response | `TYPE-U` | invariance over the complete branch family or a ratified branch rule |
| executable logarithmic provenance | `TYPE-U` | DP2 equality and nontrivial datum-driven DP3–DP6, without shape tag |
| numerical `nu` | later scale gate | independently sealed scale; none supplied here |
| p verdict/value/alpha | fenced | post-DoR-018 response execution and later authorization |

### 9.2 Operation ledger

The DoR-017 member-sensitivity tags are:

| Object/result | Tag |
|---|---|
| ratified C/K metrics, units, restrictions, differentiation, Schur operation | **MEMBER-INDEPENDENT STRUCTURE** |
| shape tag K/CK and corresponding `psi_S`, `phi_S`, direct jets | **MEMBER-SENSITIVE** |
| active-section zero jet | **MEMBER-INDEPENDENT over both proposed shapes** |
| base blocks and Q-243/Q-279 tables | **MEMBER-INDEPENDENT** |
| total blocks, stationary family, inverse instance, Schur/resulting response | **MEMBER-SENSITIVE** |
| covariance, reality, batching, restriction, unit certificates | **MEMBER-INDEPENDENT CERTIFICATES** |

| Operation | Domain | Image/transfer | Restriction/topology | Standing |
|---|---|---|---|---|
| radii | C/K metric carriers | invariant scalars | DoR-019 Hilbert/P2; rank-preserving natural | ratified input |
| flat generator K | K radius | scalar action | finite legs + R2 cocycle | proposed |
| flat generator CK | C/K radii | scalar action | finite legs + R2 cocycle | proposed |
| differentiation | smooth flat germ | R4-typed Hessian blocks | `rho_H,N` cube | proved within proposal |
| stationary solve K | base R5 C equation | complete base branch family | no new cycle-creation claim | member-sensitive output |
| stationary solve CK | modified C equation | complete local branch family | fixed-stage/rank-preserving only | member-sensitive output |
| Schur substitution | total R5 blocks | K-sector operator | R4-only unit routing | consequence only; no value |

```text
GERM_V002 = TWO_SHAPES_COMPLETE_WITHIN_PROPOSAL

SHAPE_K = DP_CERTIFIED_PROPOSAL
SHAPE_CK = DP_CERTIFIED_PROPOSAL
SHAPE_SELECTED = none

R1_COV = proved_on_ratified_metric
RHO_H_N_CUBE = proved_completed_to_finite
CYCLE_CREATING_STATIONARY_NATURALITY = not_claimed | TYPE-U
NO_IMPLICIT_CROSS_SECTOR_UNIT = pass
NU_HOMOGENEITY = manifest
ZERO_DEGENERATION = honest_with_uniform_chart_boundary

DOR018_FIBER = K | CK | reject
DOR018_ITEM_SELECTED_BY_LANE = false
PROPOSAL_READY_FOR_CROSS_REVIEW = yes

P_VERDICT_COMPUTED = false
NUMERIC_RESPONSE_VALUE_COMPUTED = false
NU_EVALUATED = false
ROOT_EVALUATED = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No alpha, `K_*`, physical root, numerical response value, rank ratio, or
measured constant was evaluated.  No p verdict was issued.  No register,
plan, tracker, git, commit, or push action was performed.
