# STAGE 8 / 7A / [PLAN:B1a-7] — FULL-SPACE EXACT SOLVE

## Lead determination — CLAIMED

The whole 864-parameter linear child-coframe law space is **UNSATISFIABLE** against the record's incidence and intrinsic-quadratic constraints on the licensed Freudenthal A2 generator. This is stronger than 797's two-candidate `EMPTY` result.

The linear constraints alone admit a 264-dimensional affine family of genuine, curvature-nonzero sections. The intrinsic quadratic eliminates **all** of it. An exact certificate is the parent two-form direction

```text
F_* = (1,-1,0,0,0,0)
```

in the ordered bivector basis `(01,02,03,12,13,23)`: even the minimum-energy incidence section has intrinsic quadratic value

```text
352886/122871,
```

where the parent value required by the sealed quadratic is `2`. The exact excess is

```text
107144/122871 > 0.
```

Every other incidence section is the minimum section plus a kernel term whose energy contribution is positive semidefinite. No choice in the remaining 264 linear parameters can remove the excess.

All headlines are this lane's `CLAIMED` determinations pending registration/cross-check. No law, metric, member, or cellulation representative is adopted.

## 0. Preflight and custody

| object | SHA-256 | result |
|---|---|---|
| `PROGRAM_STATE_BRIEF_V005.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c` | pinned and adjacent seal verified before task work |
| governing 797, `STAGE8_B1A_FULL_SOLUTION_SET_CODEX2_V001.md` | `78882cbe04c460bf7a7000277e3d24048c4639d3cdcaa6e37dd04050a8bfb5d9` | adjacent seal verified before use |
| 795, `STAGE8_B1A_COFRAME_HALF_DARIO_V001.md` | `590b3979d5a0fadfd570e3a73a13bb3a717d5450f7eb5c9f2e79f481039fc1e2` | adjacent seal verified |
| packet `review_packets/STAGE7_QSPEC_CANDIDATE_V001/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` | `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a` | packet-sealed copy used exclusively this relay |

Decisive spans:

| content | span | span SHA-256 |
|---|---:|---|
| 797 seven-constraint assembly and exact C7 receiver | 797 `[3779,5818)` | `e38ad757c1b3af5ce6a5bb6f0a52c2f19d06de6ec8d20a100c2bce3c178eda5f` |
| 797 rebuilt A2 receiver, candidate tests, and common-refinement diagnostic | 797 `[5818,10686)` | `3226a775db557c6c7fbda0c800f946b1dc88aca6a50d8e127a93a4ec4f3e9d35` |
| packet tolerance-free common-refinement conjunct | packet V011 `[47025,47247)` | `9ff6852634e78e6d886896c27bce16b4ec9e092620642a86bae00848df2f276c` |

The unsealed root V011 copy was not opened or searched this relay. PE-1..7 were not consulted and have zero weight. Output and both sidecar spellings were absent before write.

## 1. AS1 — the joint system

### 1.1 Exact A2 variables

The parent constant-curvature input is `V = Q^6`. The independently rebuilt Freudenthal receiver has a 50-dimensional curvature quotient after vertex gauge:

```text
H = im(d'_1),        dim H = 50,
C : H -> V,          rank C = 6,
```

where `C` is curvature aggregation to the six parent coordinate-face components.

Choose any exact rational basis of `H`. Let

```text
S in Mat_(50 x 6)(Q)
```

be the lift on the six-dimensional parent coframe sector. Let

```text
M = (M_1,...,M_24),  M_p in Mat_(6 x 6)(Q)
```

be the full child-coframe law: 24 children times 36 entries is the complete **864-parameter** space named by 795.

The derived frames give an exact rational, full-column-rank map

```text
L : H -> Q^(24*6)
```

which converts a global compatible refined curvature to its six local components on every child. No local component law is assumed; `M` is free before the equations below.

### 1.2 The decisive system and exact counts

The A2 block is

```text
(I)    M - L S = 0                         864 linear scalar equations
(II)   C S = I_6                            36 linear scalar equations
(III)  (1/24) M^T M = I_6                  21 independent quadratic equations
```

Thus the decisive full-A2 subsystem has exactly

```text
variables = 864 + 300 = 1164
equations = 864 + 36 + 21 = 921
          = 900 linear + 21 quadratic.
```

Gauge is not a hidden variable: the 50 coordinates are already the quotient by the 15-dimensional vertex-gauge kernel in the 65-edge presentation.

### 1.3 The other four atomic blocks

The full seven-constraint system is the conjunction

```text
Sigma_full = Sigma_A2 AND Sigma_A1 AND Sigma_A0
             AND Sigma_composition AND Sigma_common-refinement.
```

The remaining blocks are posed exactly as in 797:

- `Sigma_A0`: the identity/relabeling lift equals the sealed action; `L_id=id`.
- `Sigma_A1`: the cubical receiver carries the same three equations `(I)`–`(III)` with its derived frames, aggregation, and intrinsic child volumes.
- `Sigma_composition`: for each composable generator pair, `S_(h o g)-S_h S_g=0`; when composite maps are eliminated definitionally, this adds no independent variables.
- `Sigma_common-refinement`: on the `A1/A2` cospan into the 384-cell `Z`, `S_(r1)S_A1-S_(r2)S_A2=0`, together with equality of the pulled response. These are exact bilinear/polynomial equations; no tolerance attaches.

The nonlinear blocks are therefore the 21 Gram equations per elementary receiver and the bilinear composition/common-refinement equations. They are handled lawfully by exact elimination. Since `Sigma_A2` is a conjunct and is already infeasible, adjoining any number of A0/A1/composite variables and equations cannot restore a solution. The `1164`-variable, `921`-equation block is an exact infeasible subsystem certificate for the whole joint system, not a sampling or a truncation of its A2 law parameters.

## 2. AS2 — exact solve

### 2.1 Eliminate the law variables

Substituting `(I)` into `(III)` gives

```text
S^T G S = I_6,       where G = (1/24) L^T L.
```

`L` has column rank 50, so `G` is exact rational positive definite. The incidence constraint is `CS=I_6`.

All linear sections form

```text
S = S_0 + N,
C S_0 = I_6,
C N = 0.
```

Because `dim ker C = 44`, the affine linear-section space has dimension

```text
6 * 44 = 264.
```

In particular, the zero parent-curvature map found for 797's `(a2)` point is **not** forced across the full space. Every point of this 264-dimensional affine space obeys `CS=I_6` and is curvature-nonzero. The question is whether any point also satisfies the quadratic.

### 2.2 Minimum section and orthogonal decomposition

The exact `G`-minimum section is

```text
S_0 = G^-1 C^T (C G^-1 C^T)^-1.
```

It is `G`-orthogonal to `ker C`. Therefore every section has Gram matrix

```text
S^T G S = G_0 + N^T G N,
G_0 := (C G^-1 C^T)^-1,
N^T G N positive semidefinite.
```

Exact fraction elimination gives

```text
                 1
G_0 = --------------------------- *
                 368613

[ 362389  -166940  -166940   166940   166940        0 ]
[ -166940  362389  -166940  -166940        0   166940 ]
[ -166940 -166940   362389        0  -166940  -166940 ]
[ 166940  -166940        0   362389  -166940   166940 ]
[ 166940        0  -166940  -166940   362389  -166940 ]
[      0   166940  -166940   166940  -166940   362389 ].
```

### 2.3 Exact infeasibility certificate

For

```text
F_* = (1,-1,0,0,0,0)^T,
```

the parent quadratic is

```text
F_*^T I_6 F_* = 2 = 245742/122871.
```

The minimum possible refined quadratic among **all** incidence sections is

```text
F_*^T G_0 F_* = 352886/122871.
```

Hence

```text
F_*^T (I_6-G_0) F_* = -107144/122871 < 0.
```

But the quadratic equation would require

```text
I_6-G_0 = N^T G N,
```

whose right side is positive semidefinite. Evaluating at `F_*` would make the right side nonnegative, contradicting the displayed negative rational. This is an exact infeasibility witness; no floating threshold, physical approximation, or trial count appears.

```text
SOLUTION_SET(Sigma_A2) = EMPTY
therefore SOLUTION_SET(Sigma_full) = EMPTY.
```

### 2.4 Transcript and controls

```text
curvature quotient dimension       50
rank(C)                              6
linear section dimension          264
law parameters                     864 (all included)
quadratic equations                 21
G inversion                         exact Fraction elimination
certificate direction               (1,-1,0,0,0,0)
minimum minus required              107144/122871 > 0
```

Controls:

- `G` inverted exactly, confirming positive definiteness from `L`'s full column rank.
- The certificate uses the minimum over the **entire** linear section space, so it dominates every possible lift parameter choice.
- The zero-map degeneracy is not generalized: the full linear system has many nonzero sections, but the quadratic excludes them all.
- Adding identity, composition, A1, or common-refinement equations can only shrink an already empty set.

## 3. AS3 — consequences

### 3.1 What the record's constraints prove

Within the declared full class of linear per-child coframe laws—one arbitrary `6 x 6` matrix on each of the 24 Freudenthal children—there is **no** refinement transport that simultaneously:

1. is globally integrable as refined curvature;
2. aggregates to the parent curvature as a section; and
3. preserves the sealed intrinsic-`Vol_4` quadratic for all six parent two-form components.

The obstruction occurs on one licensed elementary A2 generator before identity, composition, or common-refinement coherence can weaken or strengthen it. This is a finite structural no-go theorem about the record's own joint constraints. It is not a failure of a search and not a physical-value computation.

### 3.2 B1a

B1a is **closed as UNSATISFIABLE on the declared full linear coframe-law class**, but it is not closed by supplying a transport. The connection/coframe transport demanded by B1a remains absent because the current constraints prohibit one on the licensed A2 receiver.

Progress now requires authority to change scope: either revise/relax at least one of incidence-section, intrinsic-quadratic, or generator requirements, or authorize a broader non-linear/non-cellwise law class not present in the 864-parameter problem. No such revision is made here.

### 3.3 B1c member and B2

`JOINT_A1_A2_FIELD_EXT_MEMBER` is **impossible under the current joint system**, hence remains uninhabited. B2 is **not runnable** because its required B1 transport input does not exist under those constraints.

### 3.4 Genuine principal question

There is no candidate-selection question left inside the declared law class. The genuine principal question is whether to:

```text
(i) accept the finite no-go and terminate this B1a carrier route; or
(ii) authorize a specified revision of the mutually inconsistent constraint package
     or a broader law class, followed by a fresh solution-set test.
```

That is a scope/specification decision, not a mathematical tie-break among surviving laws.

## 4. AS4 — freedoms consumed and flattening check

### 4.1 `FREEDOMS_CONSUMED`

| datum | treatment |
|---|---|
| all 24 child laws `M_p` | **CARRIED AS VARIABLES** — all 864 entries included; no ansatz, symmetry, or candidate selected |
| lift `S` | **CARRIED AS VARIABLE** on the complete 50-dimensional curvature quotient; all 300 entries included |
| vertex gauge | **QUOTIENTED**, not fixed physically; 15 gauge directions removed only to give an exact independent basis |
| parent two-form `F` | **CARRIED SYMBOLICALLY**; `F_*` is an infeasibility probe required to refute a universal matrix identity, not an adopted field value |
| child frames and orientations | **CARRIED AS DERIVED** from sealed 753/797 stock |
| intrinsic `Vol_4` | **CARRIED AS FORCED/CLASSIFIED**; no alternate measure or compensator inserted |
| A2 representative | Freudenthal used as one licensed universal-claim obstruction; not adopted as the only member and no cellulation eliminated |
| A0/A1/common-refinement laws | **POSED AND NOT CONSUMED TO SELECT**; infeasible A2 conjunct short-circuits them logically |
| metric / counting inner product | **NOT ADOPTED**; `G` is the sealed intrinsic-`Vol_4` quadratic pulled through the derived coframe map, not an adjustable metric |
| scaling weights (law 2a) | **NONE CONSUMED** |
| smooth coframe/connection constituent | **NOT CONSUMED; BARRED (S26)** |

`SUBSTITUTED: none.` The ordered basis and gauge quotient are exact coordinate choices; the certificate is basis-invariant in meaning and consumes no physical free datum.

### 4.2 `FLATTENING_CHECK`

- S26: clean. No smooth `C_ref` coframe or connection was imported; the packet-sealed clause is a constraint only.
- S08: clean. The finite cochains and two-form coordinates are not identified with electromagnetism, Maxwell data, or a smooth public field.
- S28: clean. No member, connection profile, or coframe law is selected by desired outcome.
- S01–S07, S09–S27, and S29–S37: untouched.

`FLATTENING_CHECK = clean (37 rows walked; S26, S08, and S28 live, all discharged).`

## 5. Gates, jurisdiction, and self verb audit

The computation is exact solution-set geometry on displayed finite rational systems, the class expressly authorized by relay 802. No physical quantity was numerically evaluated; no measured constant was consulted. No member binding, fixed-point execution, end test, common cell, or junction-map evaluation occurred. No law or metric was adopted. The evaluator chain was not invoked.

Self verb audit: `UNSATISFIABLE`, `no-go`, and `closed` are confined to the declared 864-parameter linear coframe-law system on the licensed finite generators. They are not promoted to a physical impossibility or to an unrestricted theorem over unsealed law classes. All headlines remain `CLAIMED`. **CLEAN.**

```text
SYSTEM = posed (1164 decisive variables = 864 law + 300 gauge-quotient lift; 921 decisive equations = 900 linear + 21 quadratic; nonlinear blocks: exact Gram completion, with composition/common-refinement bilinear conjuncts short-circuited by the exact infeasible A2 subsystem)
SOLUTION_SET = UNSATISFIABLE (certificate displayed: F_*=(1,-1,0,0,0,0), minimum excess 107144/122871)
B1A = closed as a finite no-go on the declared full linear coframe-law class; transport not supplied
MEMBER = JOINT_A1_A2_FIELD_EXT_MEMBER impossible under the current joint system
B2_RUNNABLE = no
PRINCIPAL_QUESTION = accept/terminate this carrier route, or authorize a specified constraint/law-class revision and fresh solve
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
