# STAGE 8 TASK 4B — N-MEMBER JET INSTANTIATION PROPOSAL — LANE 2 V003

Date: 2026-08-03  
Task: PASTE 467 / Task 4b  
Lane: CODEX LANE 2  
Status: **PROPOSED_NOT_ADOPTED — SHAPE K READY; SHAPE CK RETYPED AS COMPLETE LAMBDA FAMILY**

```text
REGISTER_HEAD_AT_PREFLIGHT = Q-386
PREFLIGHT = PASS

DOR_019 = IN_FORCE
CARRIER_METRIC_V005_SHA256 =
  2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961

LEAD_RESULT = K_CARRIED_VERBATIM_AND_CK_LAMBDA_SUBFIBER_DISCLOSED

SHAPE_K:
  phi_K(c,k)=nu f(||k||_K^2)
  D_C phi_K=D_C^2 phi_K=D_C D_K phi_K=D_K D_C phi_K=0

SHAPE_CK_LAMBDA:
  phi_CK,lambda(c,k)=nu (1+lambda (1/2)||c||_C^2)
                              f(||k||_K^2)
  lambda in R | dimensionless | no value selected
  all four lambda-dependent Hessian blocks displayed below

f(s)=exp(-1/s) for s>0; f(0)=0

DIVERGENCE_PROVENANCE:
  neither shape derived from delta_div
  both shapes openly authored and DP1-DP10 failure-capable
  LOG_DIVERGENCE_PROVENANCE = false

DOR_018_FIBER = {K,CK_lambda_family,reject}
SHAPE_SELECTED_BY_LANE = false
LAMBDA_SELECTED_BY_LANE = false
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
support classes together and leaves the choice to DoR-018.  V003 preserves
Shape K exactly and exposes the complete real CK relative-coupling family.

---

## 0. Preflight, custody, and authorities

The live register was checked before substantive work and its head was
exactly `Q-386`.  The V002 cross-review, DoR-019 decision, and adopted metric were read only
after their hashes matched.

| Authority | Verified SHA-256 | Use |
|---|---|---|
| germ V002 cross-review | `29787542deac3c45d71499e13a042d26ca959deb8a1557efd0ea85d246454331` | lambda-subfiber finding and bounded repair |
| germ V002 | `c673b6f59dda3981e02088676b11fa5606c882880d8f3b7111682e08175c5aa5` | READY Shape K and repair baseline |
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
CK, the proposal carries the complete carrier-lawful family skeleton
`(1+lambda q_C)f(s_K)`: it is origin-normalized and has the lowest even
nonconstant complement degree for every `lambda!=0`, but no carrier theorem
fixes the dimensionless relative coefficient.  `lambda=0` is the K boundary.
Neither support class or CK-family member is preferred, and the DP theorem
says none is forced by `delta_div`.

### 1.2 Authored choice table

| Field | Proposed alternatives carried | Carrier-only minimality | Void condition |
|---|---|---|---|
| support shape | K; CK-lambda family; reject | K and CK are the two lowest invariant support classes; both remain live | either shape selected by a response consequence |
| K radius | `s_K=||k||_K^2` | canonical quadratic invariant of ratified K geometry | selected cycle/basis, extra weight, or failed isometry |
| CK complement factor | complete `1+lambda q_C` family, `lambda in R` | origin-normalized lowest even nonconstant invariant skeleton; relative coefficient not fixed | selected lambda, omitted subfiber, response-block justification, selected covector, or extra width |
| flat gate | displayed `exp(-1/s)` representative; another fully certified nonzero smooth-flat gate; reject | explicit parameter-free representative, with alternatives retained | hidden scale, nonflat finite jet, target-fitted profile |
| generator provenance | authored shape/family tag plus extensional `delta_div` orbit | makes shape and lambda freedom visible under DP9 | calls shape or lambda divergence-determined without DP2–DP6 content |
| normalizer | coefficient extraction `Norm(nu psi_S)=nu` | preserves DoR-017 symbolic scaling line | numeric value, nonlinear hidden scale, or `nu` fixed by carrier units |
| stationary family | complete R5 local branch family | no root/member selected | omitted branch, evaluated root, response-based branch rule |
| cycle creation | R2 vertical cocycle only | strongest statement DoR-019 permits without upward map | assertion of `(BC-6)` without a new theorem |

Everything in this table is `PROPOSED_NOT_ADOPTED` except the consumed
DoR-017/DoR-019 premises.  No lane choice is made among K, the CK family,
its lambda members, and reject.

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

## 3. C2 — Shape CK retyped as the lambda family

### 3.1 Definition and carrier-only justification

```text
lambda in R | dimensionless | symbolic,
a_C,G,lambda(c):=1+lambda q_C,G(c)
                       =1+(lambda/2)||c||_C^2,
psi_CK,G,lambda(c,k):=a_C,G,lambda(c)f(s_K,G(k)),
phi_CK,G,lambda(c,k):=nu psi_CK,G,lambda(c,k).    (BCK-1)
```

Every defining justification is carrier-structural:

| Choice | Carrier-only justification | Response content consulted? |
|---|---|---|
| `s_K=||k||^2` | least nonconstant isometry invariant on K | no |
| `q_C=||c||^2/2` | canonical quadratic energy of the ratified C metric | no |
| `1+lambda q_C` | complete origin-normalized lowest-even-degree family | no |
| `lambda in R` | maximal reality-compatible dimensionless domain; no positivity premise narrows it | no |
| `f(s)` | explicit nonzero parameter-free smooth-flat representative | no |
| product | lowest algebraic coupling of the two declared scalar invariants | no |
| coefficient `nu` | already-ratified symbolic N-member normalizer | no |

No line cites `H_CC`, `H_CK`, Schur support, cancellation, survival, p, or a
desired output.  The killed V001 J3 justification and V002's hidden
`lambda=1` selection are absent.

### 3.2 Unabsorbability theorem

Suppose a CK-family member could be rewritten with no relative parameter:

```text
nu(1+lambda q)f(s)=nu'(1+q)f(s)                  (BCK-2)
```

for all `q` and some point with `f(s)!=0`.  Comparing the constant terms
gives `nu'=nu`; comparing the coefficients of `q` then gives
`nu lambda=nu`, hence `lambda=1` for the nonzero N member.  More generally,

```text
nu(1+lambda q)=nu'(1+lambda' q)
=> nu'=nu and lambda'=lambda.                    (BCK-3)
```

Thus `lambda` cannot be absorbed into `nu`.  It is a genuine dimensionless
relative complement coupling.  No value is selected.

### 3.3 Exact family jets

Write `c^flat=R_C c`, `k^flat=R_K k`.  For `s>0`,

```text
D_C phi_CK,lambda=nu lambda f(s)c^flat,
F_CC^(CK,lambda):=D_C^2 phi_CK,lambda
 =nu lambda f(s)R_C,

F_CK^(CK,lambda):=D_C D_K phi_CK,lambda
 =2nu lambda f_1(s)c^flat tensor k^flat,

F_KC^(CK,lambda):=D_K D_C phi_CK,lambda
 =(F_CK^(CK,lambda))^T,

D_K phi_CK,lambda
 =2nu(1+lambda q_C(c))f_1(s)k^flat,
F_KK^(CK,lambda):=D_K^2 phi_CK,lambda
 =nu(1+lambda q_C(c))[2f_1(s)R_K
             +4f_2(s)k^flat tensor k^flat].      (BCK-4)
```

All jets vanish at `k=0`.  The mixed tensor is an R4-typed bilinear map
`K->C^*` (and its reality adjoint), not a vector conversion between C and K.

At `lambda=1`, `(BCK-4)` reproduces V002 exactly.  At `lambda=0`, all C and
mixed jets vanish and the germ equals Shape K.  Every member is all-orders
flat at `k=0`.

### 3.4 Stationary structure and neutral response consequence

Retain the complete local R5 branch family solving

```text
D_C Gamma_base(p;c,k)
 +nu lambda f(s_K(k))R_C c=0.                    (BCK-5)
```

No branch or root is evaluated.  Structurally all four total blocks may
receive the displayed member jets:

```text
H_AB^(CK,lambda)=H_AB^base+F_AB^(CK,lambda).      (BCK-6)
```

This statement is reported only after the full family `(BCK-1)` and its
carrier-only choice ledger were frozen.  It neither favors CK, selects
`lambda`, nor states a response outcome.

---

## 4. B3 — common certificates on ratified geometry

### 4.1 `nu` homogeneity and zero degeneration

For Shape K or any fixed Shape CK family member and dimensionless symbolic
scaling parameter `tau`,

```text
nu->tau nu =>
phi_S->tau phi_S,
D phi_S->tau D phi_S,
D^2 phi_S->tau D^2 phi_S,                        (BC-1)
```

with the CK relative parameter `lambda` held fixed.  The carrier-unit
classes do not change and no equation fixes `nu` or `lambda`.  At
`nu=0`, each germ and every direct jet equals the Z member exactly.  A
stationary family converges to its base family only on a uniform R5 inverse
chart; no statement crosses an inverse-support jump.

### 4.2 R1-COV and the completed Hessian cube

DoR-019 makes every admitted realization automorphism isometric on C and K.
Because `lambda` is a family coordinate with trivial action under every
realization automorphism, equations `(B0-2)` give, for every family member,

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

for a cycle-creating arrow.  Every Shape CK lambda member is subject to the adjudication's
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

Shape K has no mixed member expression.  Every Shape CK lambda member uses only

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
Div_G^K:=Orbit(delta_div,G) x {K},
Div_G^CK:=Orbit(delta_div,G) x {CK} x R_lambda,
alpha_Div^CK(delta,CK,lambda)
 :=(alpha_Div delta,CK,lambda).                   (DP-0)
```

The support tag and the real dimensionless `lambda` coordinate are the
DoR-018 fiber data; neither is hidden inside `delta_div`.

| DP row | Shape K | Shape CK-lambda family | Certificate/result |
|---|---|---|---|
| DP1 datum | `Div_G^K`, inherited datum units/topology, discrete K tag | `Div_G^CK`, inherited datum plus CK tag and real dimensionless `lambda` | **PASS_WITHIN_PROPOSAL**; full residual coordinates explicit |
| DP2 log relation | no shell/C-L3 coefficient consumed | same | **PASS** with `LOG_DIVERGENCE_PROVENANCE=false` |
| DP3 depth | `Depth_K(delta,K)=s_K` as invariant scalar functional | `Depth_CK(delta,CK,lambda)=(lambda,q_C,s_K)` | executable; image displayed; datum-orbit differences lie in kernel; **PASS_WITH_DISCLOSURE** |
| DP4 accumulation | vertical differences of `s_K` | vertical differences of `(lambda,q_C,s_K)`, with `lambda` unchanged by stage transport | Hilbert/P2 topology, zero on rank-preserving identity extension, cycle-creating cocycle `(BC-5)`; **PASS** |
| DP5 map handoff | K radius is formed after the ratified prefix-to-cycle descent | same K handoff plus ratified R5 C carrier | no rival CycleMap or endpoint route; **PASS** |
| DP6 generator | `(delta,K)->nu f(s_K)` | `(delta,CK,lambda)->nu(1+lambda q_C)f(s_K)` | executable and target-blind; neither output nor jets used in membership; **PASS** |
| DP7 naturality | `(BC-2)`–`(BC-4)` | same for every scalar `lambda` | stabilizers, reality, batching, identity extension covered; cycle creation scoped by `(BC-5)`; **PASS_WITH_STATED_SCOPE** |
| DP8 finite square | independent finite `b_N^K` | independent family `b_N^(CK,lambda)` | equals completed restriction for every `lambda`; active Q-243/Q-279 jets zero; **PASS** |
| DP9 residual disclosure | flat-gate representative, K support, `nu`, stationary branch family authored/disclosed | flat gate, CK support, full `lambda in R`, `nu`, branch family authored/disclosed | no uniqueness claim or omitted relative coefficient; **PASS** |
| DP10 target/origin | DoR-017 datum + DoR-019 geometry; chronology Section 7 | same | no target, continuum import, or output-defined membership; **PASS** |

The independently finite legs are

```text
b_N^K(c_N,k_N):=nu f(||k_N||_K^2),
b_N^(CK,lambda)(c_N,k_N)
 :=nu(1+(lambda/2)||c_N||_C^2)f(||k_N||_K^2).    (DP-1)
```

They are constructed from finite ratified metrics, not copied from the
completed germ.  Every active reference has `k_N=0`, so every member jet is
zero to all orders and Q-243/Q-279 are reproduced exactly.

```text
DP_CERTIFICATE_K = PASS_WITHIN_PROPOSAL
DP_CERTIFICATE_CK_LAMBDA_FAMILY = PASS_WITHIN_PROPOSAL
DIVERGENCE_DETERMINES_SHAPE = false
LAMBDA_DERIVED_FROM_DIVERGENCE = false
```

---

## 6. Minimal-stage structural checks

### 6.1 Reciprocal loop

In a temporary orthonormal chart `k=t u` (the result is chart invariant),

```text
F_KK^K=nu[2f_1(t^2)+4t^2f_2(t^2)]R_K,            (MS-1)

F_CC^(CK,lambda)=nu lambda f(t^2)R_C,
F_CK^(CK,lambda)=2nu lambda t f_1(t^2)c^flat tensor u^flat,
F_KK^(CK,lambda)=nu(1+lambda q_C(c))
              [2f_1(t^2)+4t^2f_2(t^2)]R_K.      (MS-2)
```

At `t=0`, every term is exactly zero.  No numerical point or response is
evaluated.

### 6.2 S8-A rank-two stage

For arbitrary `k` in the complete rank-two carrier, use invariant `s=||k||^2`.
The signed exchange preserves `s`, sends `k^flat` covariantly, and conjugates
`k^flat tensor k^flat`.  Equations `(BK-2)` and `(BCK-4)` therefore satisfy
R1-COV without selecting `c_1`, `c_2`, `c_3`, or an orientation.

---

## 7. B4 — DoR-018 fiber and anti-tuning chronology

### 7.1 Exact fiber

| DoR-018 item | Certified authored content | Neutral structural response consequence | Remaining TYPE-U |
|---|---|---|---|
| Shape K | cycle-only `nu f(s_K)`, DP table, K jets, base complement critical family | member correction appears only in K/K; complement inverse and mixed blocks remain base-only | global chart extension; cycle-creating stationary restriction; branch-uniform output |
| Shape CK-lambda family | complete `{nu(1+lambda q_C)f(s_K):lambda in R}`, family-level DP table, lambda jets, complete R5 branch family | for `lambda!=0`, all four member jet blocks may enter the already-ratified Schur structure; `lambda=0` is the K boundary | same three doors; future lambda disposition |
| reject | no component instantiation | response remains at the confirmed TYPE-U jet boundary | shape/jet object remains absent |

No item or lambda member is recommended.  `nu` and `lambda` remain symbolic.
The top-level fiber is a union with identified boundary, not a duplicate:
the `lambda=0` CK member is exactly Shape K.

### 7.2 C3 — free-input accounting

The program's declared free inputs under each alternative are:

```text
Shape K:
  (r_0,r_ch) + nu;

Shape CK-lambda family:
  (r_0,r_ch) + nu + lambda;

reject:
  no new germ input; the jet object remains TYPE-U.            (FI-1)
```

The rank pair remains symbolic and unselected.  `lambda` is not a rank
ratio, unit conversion, or rescaling of `nu`.  If CK is ratified as a family,
the future disposition of `lambda` is exactly one of:

```text
derive lambda from new target-blind ratified structure;
or ratify lambda at its own explicit gate.                      (FI-2)
```

No such disposition is executed here.

### 7.3 Order-of-construction ledger

```text
T0  DoR-017 fixes the abstract N member and symbolic nu.
T1  DoR-019 fixes C/K geometry, units, isometries, and R4 routing.
T2  DP theorem fixes the rule: shape is authored and must be target-blind.
T3  enumerate the two minimal carrier support classes {K,CK}; retain both.
T4  enumerate the CK skeleton (1+lambda q_C)f(s_K); carry every real
    dimensionless lambda because no carrier premise narrows it.
T5  fix q_C, s_K, the parameter-free flat representative, Gen, finite legs,
    vertical cocycles, and normalizer without reading jets.
T6  prove covariance, restriction scope, units, and DP1-DP10.
T7  differentiate to obtain jets.
T8  only now load the pre-existing Schur consumer and report neutral
    block-placement consequences.
```

Because both support classes and every lambda member survive through T8, no
consequence can select between or within them inside this artifact.

```text
ANTI_TUNING_ATTESTATION = PASS_WITHIN_PROPOSAL
CONSEQUENCE_READ_BEFORE_CHOICE_FIXED = false
```

---

## 8. B5 — hostile battery

| Attack | Shape K | Shape CK-lambda family | Result |
|---|---|---|---|
| reverse engineer from response support | a tuner seeking mixed blocks would reject K, but K remains live | a tuner might prefer nonzero lambda or a particular value, but the complete real family is fixed before jets | **PASS**; outcome selects neither support nor coefficient |
| finite flatness/Q-243/Q-279 | every active jet zero | every active jet zero | **PASS** all orders |
| rank-two cycle-selective witness | depends only on full `||k||^2` | depends only on full C/K norms | **PASS**; no selected cycle |
| pendant/tree witness | pendant lies in quotient kernel before norm | same | **PASS**; zero physical norm |
| G7 cycle-creating root attack | no new root claim beyond base R5 scope | explicit countermodel applies family-wide; `(BC-6)` not claimed | **PASS_BY_SCOPE** |
| implicit cross-sector unit | no mixed member arrow | only R4 `F_CK/F_KC`; Schur units `(BC-8)` | **PASS** |
| zero degeneration | direct germ/jets linear in `nu`; uniform-chart boundary stated | same | **PASS_WITH_BOUNDARY** |
| stabilizer/orbit attack (fresh) | equal-radius directions receive equal values; tensors transform covariantly | same for both radii; no orbit representative | **PASS** |
| hidden scale/`nu` calibration (fresh) | flat gate has no width; unit classes do not fix `nu` | `lambda` is declared separately and cannot be hidden in `nu`; `1/2` remains the quadratic-form convention | **PASS** |
| reviewer lambda-subfiber regression | not applicable; overall amplitude is absorbed into `nu` | constructs every `nu(1+lambda q_C)f(s)` and every certificate sees `lambda` | **PASS**; no omitted CK member |

The reverse-engineering test does not prove either formula uniquely forced by
the divergence datum; it proves the proposal does not choose between the two
carrier-minimal support classes by reading their consequences.

```text
SELF_KILL_ATTACKS_RUN = 10
SELF_KILL_FAILURE_FOUND = false
J3_RESPONSE_FACING_JUSTIFICATION = absent
LAMBDA_SUBFIBER_REGRESSION = installed_and_passed
```

---

## 9. C5 — true delta versus V002

| V002 content | V003 standing | Exact delta |
|---|---|---|
| artifact metadata | V003 / PASTE 467 / Q-386 | bounded commission and current-register update |
| authority ledger | V002 authorities retained | V002 cross-review and V002 baseline hashes added |
| Shape K Section 2 | **VERBATIM** | none |
| common metric/flat gate | retained | none |
| CK factor `1+q_C` | widened | complete `1+lambda q_C`, `lambda in R` |
| CK justification | carrier structural | consequence phrase removed; coefficient not fixed |
| CK jets | correct at implicit `lambda=1` | all jets retyped as functions of `lambda` |
| CK stationarity | implicit `lambda=1` | `nu lambda f(s)R_C c` family |
| `nu` homogeneity | retained | scaling symbol renamed `tau`; `lambda` held fixed |
| R1-COV/`rho_H,N` | retained | rerun uniformly for every scalar `lambda` |
| cycle creation | retained bounded scope | vertical cocycles family-wide; no root naturality |
| DP1–DP10 | K retained | CK DP1/DP3/DP4/DP6/DP8/DP9 see `lambda` explicitly |
| finite legs | K and CK at implicit 1 | CK finite leg parameterized by `lambda` |
| reciprocal loop/S8-A | K retained | CK formulas parameterized by `lambda` |
| DoR-018 fiber | K/CK/reject | K/CK-lambda-family/reject |
| free inputs | not explicit | K: ranks + `nu`; CK: ranks + `nu+lambda` |
| battery | nine attacks | reviewer subfiber installed as tenth permanent regression |
| doors | retained | lambda disposition door added |
| final board | V002 labels retained in meaning | V003 and CK-lambda-family labels replace V002/CK labels; `LAMBDA_SELECTED=none` added |

All V002 content outside the rows above is carried without mathematical
change.  No V002 passing Shape K clause, metric certificate, G7 scope,
fence, or gate standing is weakened.

```text
DELTA_V002 = complete
SHAPE_K_VERBATIM = verified
```

---

## 10. Doors, operation ledger, and final board

### 10.1 Doors

| Door | Standing | Would build |
|---|---|---|
| global stationary-germ extension | `TYPE-U` beyond certified R5 charts | covariant global extension preserving the chosen shape and R2 cocycles |
| cycle-creating stationary restriction | `TYPE-U` for both shapes | theorem proving `(BC-6)` or a separately ratified stationary transport |
| branch-uniform response | `TYPE-U` | invariance over the complete branch family or a ratified branch rule |
| executable logarithmic provenance | `TYPE-U` | DP2 equality and nontrivial datum-driven DP3–DP6, without shape tag |
| numerical `nu` | later scale gate | independently sealed scale; none supplied here |
| CK `lambda` disposition | `TYPE-U` after any CK-family ratification | derive target-blindly or ratify separately |
| p verdict/value/alpha | fenced | post-DoR-018 response execution and later authorization |

### 10.2 Operation ledger

The DoR-017 member-sensitivity tags are:

| Object/result | Tag |
|---|---|
| ratified C/K metrics, units, restrictions, differentiation, Schur operation | **MEMBER-INDEPENDENT STRUCTURE** |
| shape tag K/CK, `lambda`, corresponding `psi_S`, `phi_S`, direct jets | **MEMBER-SENSITIVE** |
| active-section zero jet | **MEMBER-INDEPENDENT over both proposed shapes** |
| base blocks and Q-243/Q-279 tables | **MEMBER-INDEPENDENT** |
| total blocks, stationary family, inverse instance, Schur/resulting response | **MEMBER-SENSITIVE** |
| covariance, reality, batching, restriction, unit certificates | **MEMBER-INDEPENDENT CERTIFICATES** |

| Operation | Domain | Image/transfer | Restriction/topology | Standing |
|---|---|---|---|---|
| radii | C/K metric carriers | invariant scalars | DoR-019 Hilbert/P2; rank-preserving natural | ratified input |
| flat generator K | K radius | scalar action | finite legs + R2 cocycle | proposed |
| flat generator CK-lambda | C/K radii plus real `lambda` | scalar action family | finite legs + R2 cocycle for every `lambda` | proposed family |
| differentiation | smooth flat germ | R4-typed Hessian blocks | `rho_H,N` cube | proved within proposal |
| stationary solve K | base R5 C equation | complete base branch family | no new cycle-creation claim | member-sensitive output |
| stationary solve CK-lambda | lambda-dependent C equation | complete local branch family for every `lambda` | fixed-stage/rank-preserving only | member-sensitive output |
| Schur substitution | total R5 blocks | K-sector operator | R4-only unit routing | consequence only; no value |

```text
GERM_V003 = K_READY_AND_CK_LAMBDA_FAMILY_COMPLETE_WITHIN_PROPOSAL

SHAPE_K = DP_CERTIFIED_PROPOSAL
SHAPE_CK_LAMBDA = DP_CERTIFIED_FAMILY_PROPOSAL
SHAPE_SELECTED = none
LAMBDA_SELECTED = none

R1_COV = proved_on_ratified_metric
RHO_H_N_CUBE = proved_completed_to_finite
CYCLE_CREATING_STATIONARY_NATURALITY = not_claimed | TYPE-U
NO_IMPLICIT_CROSS_SECTOR_UNIT = pass
NU_HOMOGENEITY = manifest
ZERO_DEGENERATION = honest_with_uniform_chart_boundary

DOR018_FIBER = K | CK_lambda_family | reject
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
