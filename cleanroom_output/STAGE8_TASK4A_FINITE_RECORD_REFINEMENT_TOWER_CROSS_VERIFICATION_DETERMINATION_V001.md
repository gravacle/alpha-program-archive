# Stage 8 Task 4a Finite Record-Refinement Tower Cross-Verification Determination V001

Date: 2026-08-03  
Task: PASTE 413 / Task 4a  
Lane: CODEX LANE 1  
Status: **INDEPENDENT CROSS-VERIFICATION COMPLETE**

```text
VERDICT = CONFIRMED_WITH_NOTES

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 0. Lead determination

**The refinement tower recomputes exactly. No mathematical defect is found.**
The controlled-write product, realized-branch induction, tier-one reduction,
identity-input falsifier, state restrictions, reality, quotient descent, rank
discipline, source-conditioning boundary, O7 confinement, and the all-tier
allow/require split each survive independent reconstruction.

For every finite `k>=1`, on the declared independently supplied tier source
family,

```text
omega_k=(1-p)|R...R><R...R|+p|P...P><P...P|,
F_k=P_0+exp(sum_(t=1)^k Xi_t)P_ch,
A_k=(1-p)+p exp(sum_(t=1)^k Xi_t),
D_k=(1/2)sum_(t=1)^k Q_t.
```

For identical declared tier inputs, this is

```text
A_k=(1-p)+p exp(k Xi),
D_k=kQ/2.
```

At identity tier data, `Xi_t=0` for every tier, so `F_k=I_src` and `A_k=1`.
The branch weights remain exactly `(1-p,p)` for every `k`; they are not
Bernoulli powers. Tier 1 is the sealed one-cell state, operator, and scalar
amplitude exactly.

`CONFIRMED_WITH_NOTES` freezes two interpretation boundaries rather than
requesting a repair:

1. `D_k=kQ/2` is a theorem on the artifact's declared tierwise C-B source
   family. The live C-B functional is the same-cell trace contraction, so its
   finite direct-sum restrictions are additive and off-diagonal inter-tier
   trace-class blocks do not add a hidden cross term. A future nonlocal
   inter-tier kernel would be a new source functional and is not covered.
2. The registered phrase "allow-side accumulation without bound" is correct
   only for the additive lifted exponent `sum_t Xi_t` (and its real attenuation
   part when present). The U(1) holonomy `q^k` lies on the unit circle, and the
   scalar amplitude is bounded/possibly oscillatory. The reviewed artifact
   itself makes this distinction correctly.

No amendment to the reviewed tower is required.

```text
T1_EXACT_TOWER = PASS
T2_FALSIFIER_AND_COVARIANCE = PASS
T3_SOURCE_CONDITIONING = PASS
T4_O7_CONFINEMENT = PASS
T5_ALLOW_REQUIRE_ALL_TIERS = PASS_WITH_SCOPE_NOTE

TOWER_REPAIR_REQUIRED = false | TYPE-R |
  test: every displayed tower equation and requested certificate recomputes

PROPAGATING_MATHEMATICAL_DEFECT_FOUND = false | TYPE-S |
  roots: reviewed tower, ratified law, finite influence functional, PathCert,
         live germ, P2 V002, nonzero-R reference, and O7 transfer boundary |
  exclusions: full record-to-source/background feedback, future nonlocal
              inter-tier source kernels, continuum response, protected holdout |
  query: tower equations, restrictions, source support, O7 symbols, and all
         five PASTE-413 checks
```

## 1. Preflight, custody, and frozen authorities

### 1.1 Preflight

```text
DOES_THE_OBJECT_EXIST = true
  object: STAGE8_TASK4A_FINITE_RECORD_REFINEMENT_TOWER_EXACT_COMPUTATION_V001.md
  verified SHA-256:
    034a7aabe316cdab91093c1fc82170e623c6bd112230676e1069aefe77c2fbe0

IS_THE_VERSION_CURRENT = true
  register head: Q-330
  register SHA-256 at start:
    39ff49198f737d32f5a29ea9447f74b80a897d3263b1ef140f22242589e21d18

ARE_ITS_INPUTS_PRESENT = true
  exact finite law, one-cell completed state, finite source/probe forms,
  realized ready/pointer quotient, and O7 transfer boundary are sealed
```

The reviewed artifact's sidecar verified `OK`, and its workspace mirror was
byte-identical before the review.

### 1.2 Roots and exclusions

Roots entered:

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003/
/Users/bgm/MB Work/alpha_supervision/
/Users/bgm/MB Work/alpha-program-archive/workspace/
```

Excluded:

```text
a32_holdout/custodian_private/                       NOT ENTERED
physical response, residual, root, or coupling        NOT EVALUATED
rank-pair value                                       NOT SELECTED
comparison to a measured constant                     NOT PERFORMED
register, governing plan, tracker, git, commit, push  NOT TOUCHED
```

### 1.3 Frozen hashes

| Authority | SHA-256 | Use |
|---|---|---|
| `LOCKED_PROCESS.md` | `f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba` | fences, typing, custody |
| `RELAY_PASTE_413_VERIFY_THE_TOWER_V001.md` | `6d3126b131ebc44f9938b8c3c44fe05d02eef306c1aa3faa50c80b81c022fd6b` | task contract |
| reviewed tower V001 | `034a7aabe316cdab91093c1fc82170e623c6bd112230676e1069aefe77c2fbe0` | object under review |
| law proposal V002 | `db1808e4da38cbfed8b12017885aff1bf63b0378e9971c37294e21fa08766fee` | exact controlled write |
| finite influence result V001 | `2cd1ffcefd68ac03c6c09a4eca0dc9fe8d1adc8ac564cc0d050dfd41d79e6d0f` | `U_N`, `F_N`, identity and reality |
| PathCert V001 | `74a1f903ce79fc76a0f32a036a872b2d59b8944aa9e4211135d65ba8e9800db0` | completed state and restrictions |
| source germ V007 | `bd33e54c27ddb8ed5224637d7888a071026db33a1a17c7127a27ffa647b69896` | live `Xi`, `Q_even`, `Log_0` |
| P2 V002 | `40b2af34443e051fffdc7bf2ec7025c811a98c501a82d19164596ee6f37f00c1` | finite source restrictions |
| nonzero-R reference V001 | `c7624d88aedaa0659755b5c566121b24c2ad0c29a0060daada43a31b22a6ddfb` | C-B same-cell trace source |
| O7 transfer check V001 | `dcf29eeae27c25ee17c93671acb32336c5e227d97a2280a3fa8668f17610c57d` | non-transfer boundary |
| O7 analogue witness check V001 | `6f8f0dd3209e3bf10ba6c1e1ab766cdccafc226f507486b216a0d33d2b2cb3ad` | response-transfer prohibition |
| O7 escalation V001 | `3c81647eb55ad01d4d71e23b2b45161427f82390098c95afa5721065206a7df2` | `(3/8)^k` Route-T witness |

## 2. T1 - exact tower recomputation

### 2.1 One-cell matrix and the two iteration controls

The ratified one-cell record matrix is

```text
W(z)=[[0,1,0],[z,0,0],[0,0,-1]].
```

Direct multiplication gives

```text
W(z)^2=diag(z,z,1),
W(z)^(2m)|r>=z^m|r>,
W(z)^(2m+1)|r>=z^(m+1)|p>.
```

Thus same-cell repetition toggles ready/pointer and has doubled sandwich
`q^ceil(k/2)`. It is not the refinement tower.

For fresh record factors,

```text
U_t=P_0 tensor I+P_ch tensor W_t.
```

Using `P_0P_ch=P_chP_0=0` and `P_0+P_ch=I` gives by induction

```text
product_(t=1)^k U_t
 =P_0 tensor I+P_ch tensor product_(t=1)^k W_t.       (CV-1)
```

This independently recovers the reviewed artifact's fresh-factor control and
shows that no mixed source-projector term was omitted.

### 2.2 State induction and fixed weights

At tier 1, the sealed completed state is

```text
rho_1=P_0 rho P_0 tensor E_R,1+P_ch rho P_ch tensor E_P,1.
```

The realized-branch copier appends `E_R,k+1` to the neutral conditional
string and `E_P,k+1` to the charged conditional string. Therefore

```text
rho_k=P_0 rho P_0 tensor_t E_R,t
      +P_ch rho P_ch tensor_t E_P,t                 (CV-2)
```

for all finite `k` by induction. Tracing the source gives

```text
omega_k=(1-p)sigma_0,k+p sigma_1,k.                 (CV-3)
```

The weights are fixed because one source branch is copied; no independent
branch draw occurs at a later tier. Since the two strings are orthogonal at
tier 1, trace distinguishability is `1` and fidelity is `0` for every
`k>=1`.

### 2.3 Amplitude and depth

The tier source factor is

```text
exp(Xi_t),
Xi_t=L_t-(1/2)Q_t.
```

Equation `(CV-1)` and source-sector orthogonality give

```text
F_k=P_0+product_t exp(Xi_t)P_ch
   =P_0+exp(sum_t Xi_t)P_ch.                         (CV-4)
```

Scalarization with `(CV-3)` gives

```text
A_k=(1-p)+p exp(sum_t Xi_t).                        (CV-5)
```

The real bilocal attenuation in the charged conditional factor is therefore

```text
D_k=(1/2)sum_t Q_t.                                 (CV-6)
```

If `Xi_t=Xi` and `Q_t=Q` are frozen identically before construction,

```text
A_k=(1-p)+p exp(kXi),
D_k=kQ/2.                                           (CV-7)
```

No logarithmic `k` law follows. The physical local log is

```text
Gamma_k=Log_0[(1-p)+p exp(sum_t Xi_t)]              (CV-8)
```

on a common nonzero `Log_0` chart.

### 2.4 Source-family support

The germ and nonzero-R reference define

```text
Q_N(R)=Q_delta,N^Theta(R),
B_delta,N(R)=Tr(P_N R_delta,delta P_N).
```

For pairwise orthogonal tier-support projections `P_t` with
`P_tower=sum_t P_t`, trace additivity gives

```text
B_delta,tower(R)
 =sum_t Tr(P_t R_delta,delta P_t),
Q_tower(R)=sum_t Q_t(P_t R P_t).
```

on the declared U1-real same-cell C-B contraction. Off-diagonal tier blocks
have zero trace and do not alter `(CV-6)`. Hence the independently supplied
`Q_t` sum is compatible with the live source functional, not an ad hoc
replacement for it.

This proof does not authorize a future nonlocal inter-tier kernel. Such a
kernel would change `Q`, not correct the tower.

```text
T1_TIER_CONSTRUCTION = PASS
T1_A_K_CLOSED_FORM = PASS
T1_D_K_LINEAR_FORM = PASS
T1_WEIGHT_INVARIANCE = PASS
T1_TIER_ONE_EXACTNESS = PASS
```

## 3. T2 - falsifier arms and covariance

### 3.1 Identity input

Set every lawful tier input to the identity datum:

```text
L_t=0,
Q_t=0,
Xi_t=0.
```

Then `(CV-4)` and `(CV-5)` give

```text
F_k=P_0+P_ch=I_src,
A_k=(1-p)+p=1                                      (CV-9)
```

for every finite `k`. This is exact, not a finite-sample observation.

### 3.2 Restrictions

Partial trace of the last normalized conditional record factor in `(CV-2)`
returns `rho_k`. For observables, `A -> A tensor I` gives the same state
restriction square. For amplitudes, deleting an identity tier leaves
`exp(Xi_t)=1`, so `F` and `A` also restrict exactly. Deleting a nonidentity
tier is correctly not claimed as an amplitude restriction.

### 3.3 Reality, quotient, and rank

Tierwise U1 reality gives

```text
Xi_(-n),t(Theta s_t)=conjugate(Xi_n,t(s_t)).
```

Summation and exponentiation preserve that identity, proving tower reality.
Each tier character and C-B functional already descends through its finite
quotient; their finite product therefore descends. The only rank dependence
is the unevaluated symbolic coefficient

```text
p=r_ch/(r_0+r_ch).
```

No rank pair is selected.

```text
T2_IDENTITY_A_K = PASS
T2_STATE_RESTRICTION = PASS
T2_IDENTITY_TIER_AMPLITUDE_RESTRICTION = PASS
T2_REALITY = PASS
T2_QUOTIENT = PASS
T2_RANK_DISCIPLINE = PASS
```

## 4. T3 - source conditioning and intrinsic-term audit

The only `k`-dependent charged amplitude in the constructed tower is

```text
product_t exp(Xi_t).
```

When the declared tier sources are identity inputs, this product is one for
all `k`. The branch weights, distinguishability, and scalar amplitude then do
not grow. Therefore `D_k` growth requires the declared nonzero `Q_t` probes.

The converse check also passes in the stated scope. Equations `(CV-1)` and
`(CV-2)` are the complete algebra on the realized ready/pointer path. There
is no additional scalar factor in the ratified write, and no term disappears
under the source-projector multiplication. The quotient discards no sector
that is populated by the sealed ready-path output.

This does not prove that every possible full-record feedback extension has no
intrinsic term. The full `M_3` record-output-to-source/background channel is
unbuilt, and the reviewed artifact types it `TYPE-U`. Thus:

```text
SOURCE_CONDITIONED_GROWTH_REQUIRES_NONIDENTITY_TIER_INPUT = true | TYPE-P |
  scope: constructed realized-branch tower

INTRINSIC_TERM_SUPPRESSED_BY_CONSTRUCTED_PATH_CHOICE = false | TYPE-R |
  test: exact completeness of CV-1 through CV-5 on populated path sectors

EVERY_FULL_FEEDBACK_EXTENSION_HAS_NO_INTRINSIC_TERM = NO_VERDICT |
  would-build: FULL_FINITE_RECORD_TO_SOURCE_BACKGROUND_REFINEMENT_CHANNEL
```

T3 passes without upgrading the source-conditioned datum into an intrinsic
record-only law.

## 5. T4 - O7 confinement

The O7 authorities type `(3/8)^k` as the singular datum of a distinct Route-T
transfer operator under record-color tensor refinement. They explicitly deny
an automatic transfer to the response pullback.

The reviewed tower formulas contain none of:

```text
3/8,
(3/8)^k,
tau_R,
the Route-T transfer operator,
its spectral gap,
an O7 intertwiner,
or an O7 response pullback.
```

Its `3^k` fresh-record carrier shape follows independently from the ratified
three-dimensional record factor and finite tensor product. Shared carrier
dimension is not a transport map. The artifact uses O7 only as a warning that
refinement needs fresh factors and states that limitation explicitly.

```text
T4_O7_SINGULAR_DATUM_TRANSPORTED = false | TYPE-R
T4_ROUTE_T_STRUCTURE_USED = false | TYPE-S
T4_INDEPENDENT_FINITE_CARRIER_TENSORING = PASS
```

## 6. T5 - allow/require surface for every tier

### 6.1 Require side

The require-side datum is the shared branch commitment. From `(CV-3)`,

```text
weight_0(k)=1-p,
weight_ch(k)=p
```

for every finite `k`. The induction in Section 2 proves this for all tiers,
not merely the tiers explicitly displayed in the reviewed computation.
Literal branch distinguishability is already maximal at tier 1 and remains
so. The require-side invariance is therefore proved.

### 6.2 Allow side

The allow-side source factor is exactly

```text
exp(sum_t Xi_t).
```

Each admitted nonidentity tier adds its declared `Xi_t` to the lifted
exponent. Identical inputs give `kXi`, and the dephasing contribution gives
`kQ/2`. This accumulation is exact.

The word "unbounded" needs its carrier stated. The lifted additive exponent
may grow linearly with tier count. For a pure U1 history, however,
`exp(kXi)=q^k` remains on the unit circle, and
`(1-p)+pq^k` is bounded and may oscillate. The reviewed artifact already says
this at its pure-holonomy and identity controls. No contradiction exists once
the lift and physical phase are kept distinct.

```text
T5_REQUIRE_SIDE_INVARIANT_FOR_ALL_FINITE_K = true | TYPE-P
T5_ALLOW_SIDE_LIFT_ACCUMULATES_EXACTLY = true | TYPE-P
T5_PHYSICAL_U1_PHASE_GROWS_UNBOUNDED_IN_MODULUS = false | TYPE-R
T5_SCALAR_AMPLITUDE_MONOTONE_IN_K_FOR_ALL_ADMITTED_INPUTS = false | TYPE-R
```

## 7. Final matrix and verdict

| Check | Independent result | Consequence |
|---|---|---|
| T1 tower, `A_k`, `D_k`, weights, tier 1 | PASS | exact finite tower stands |
| T2 identity, restrictions, reality, quotient, rank | PASS | falsifier and conventions stand |
| T3 source conditioning and converse | PASS | depth datum is scoped, not intrinsic |
| T4 O7 confinement | PASS | no Route-T import |
| T5 allow/require all-tier theorem | PASS WITH SCOPE NOTE | fixed commitment plus additive lifted exponent |

```text
OVERALL_VERDICT = CONFIRMED_WITH_NOTES
Q330_MATHEMATICAL_RESULT_STANDS = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014 and the reviewed tower inputs

Q330_REPAIR_REQUIRED = false | TYPE-R

FIRST_DEPTH_DATUM_STANDING
  = D_k=(1/2)sum_t Q_t | identical declared tier form kQ/2 |
    TYPE-P | source-conditioned | not intrinsic record-only depth

ALLOW_REQUIRE_READING_STANDING
  = require weights fixed for all finite k |
    allow lifted exponent additive for all finite k |
    physical U1 phase and scalar amplitude remain bounded objects

FULL_RECORD_TO_SOURCE_BACKGROUND_FEEDBACK_CHANNEL = false | TYPE-U
O7_ROUTE_T_DATUM_TRANSFERRED = false | TYPE-R
FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-S

REGISTER_HEAD_AT_START = Q-330
REGISTER_SHA256_AT_START =
  39ff49198f737d32f5a29ea9447f74b80a897d3263b1ef140f22242589e21d18

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 8. Custody

This lane seals this determination, verifies its sidecar, mirrors artifact and
sidecar byte-identically to the archive workspace, reports hashes, and stops.
It does not edit the register, governing plan, or tracker, and performs no git,
commit, or push action.
