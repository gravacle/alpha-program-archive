# Stage 8 Task 4a Finite Record-Refinement Tower Cross-Verification Determination V001

Date: 2026-08-03  
Lane: CODEX LANE 1  
Task: PASTE 413 / Task 4a / cross-verification of PASTE 412  
Register head checked: Q-330  
Plan head checked: C43  
Verdict: **CONFIRMED-WITH-NOTES. The tower's load-bearing finite algebra, its tier-one falsifier, the exact branch weights, the source-conditioned amplitude, and the linear dephasing datum independently recompute. The notes are scope protections, not a refutation of Q-330: `D_k=(1/2)sum_t Q_t=kQ/2` is exact for the declared tier-local probe family; it is not an unrestricted completed-bilocal formula, and the artifact's broad line `INTRINSIC_RECORD_ONLY_DEPTH_GROWS_WITH_K=false` must be read as an amplitude/dephasing/log statement because the same artifact correctly exhibits the pre-existing extensive total correlation `(k-1)h_2(p)`.**

```text
REFINEMENT_TOWER_CROSS_VERIFICATION = CONFIRMED_WITH_NOTES

T1_TOWER_ALGEBRA = PASS | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
T2_FALSIFIER_ARMS = PASS | TYPE-P |
  premises: the same ratified stack
T3_SOURCE_CONDITIONING = PASS_WITH_SCOPE_NOTE | TYPE-P |
  scope: declared tier-local source/probe family
T4_O7_CONFINEMENT = PASS
T5_ALLOW_REQUIRE_READING = PASS_WITH_SCOPE_NOTE | TYPE-P |
  require: branch weights invariant for every finite tier |
  allow: charged conditional characters/exponents multiply/add for every
         finite tier with declared nonidentity inputs

CENTRAL_Q330_RESULT_REFUTED = false | TYPE-R |
  test: independent projector, matrix-power, source, and restriction proofs

UNRESTRICTED_COMPLETE_BILOCAL_TOWER_FORMULA_BUILT = false | TYPE-U |
  would-build: one completed-tier source R with its full V007 contraction,
               including any cross-tier bilocal blocks, and a proof that
               its Q decomposes into the declared per-tier Q_t

GLOBAL_INTRINSIC_RECORD_STATISTIC_GROWTH_ABSENT = false | TYPE-R |
  counterexample: T_k=(k-1)h_2(p) already stated in the tower and Q-329 |
  non-inheritance: C42 rejected T_k as the requested nonadditive depth
                   selector; this does not alter D_k or Q-330

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

---

## 1. Custody, current version, and verification standard

### 1.1 Object and seal

The object under review is:

```text
STAGE8_TASK4A_FINITE_RECORD_REFINEMENT_TOWER_EXACT_COMPUTATION_V001.md
SHA-256: 034a7aabe316cdab91093c1fc82170e623c6bd112230676e1069aefe77c2fbe0
sidecar check: PASS
```

The live supervision sources were checked after reading the relay. They remain
at Q-330 / C43, and the tracker identifies relay 413 as the cross-verification
of relay 412. No later register entry supersedes this task.

The cross-check follows the P2 verification standard from
`STAGE8_TASK4A_P2_FOUNDATION_CROSS_VERIFICATION_DETERMINATION_V001.md`
(`78970c69...`): recompute the algebra from the defining matrices and
projectors, do not inherit a displayed derivative sign, execute the finite
restriction checks, and distinguish a scalar exponent coordinate from a
physical phase direction.

### 1.2 Roots entered

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003/

/Users/bgm/MB Work/alpha_supervision/

/Users/bgm/MB Work/alpha-program-archive/workspace/
  custody destination only, after sealing
```

`a32_holdout/custodian_private/` was not entered or touched.

### 1.3 Load-bearing authorities

| Authority | SHA-256 | Use |
|---|---|---|
| `LOCKED_PROCESS.md` | `f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba` | process, gates, custody, fences |
| `RELAY_PASTE_413_VERIFY_THE_TOWER_V001.md` | `6d3126b131ebc44f9938b8c3c44fe05d02eef306c1aa3faa50c80b81c022fd6b` | T1--T5 contract |
| `QUESTIONS_SETTLED_REGISTER_V001.md` | `39ff49198f737d32f5a29ea9447f74b80a897d3263b1ef140f22242589e21d18` | Q-330 current head |
| `TASK_LIST_HERE_TO_ALPHA_2026-08-01_V002.md` | `03ad086fe616dcc09dd40c5a74d2e9898ef420c0a38b01f122a12b7664a0c376` | C43 commission |
| `EXECUTION_TRACKER.md` | `55b7748480893848ffe58494d0f61da9c997ab17f5bb2494abc2504d221f6c37` | relay 413 status |
| tower V001 | `034a7aabe316cdab91093c1fc82170e623c6bd112230676e1069aefe77c2fbe0` | object under test |
| transition-law V002 | `db1808e4da38cbfed8b12017885aff1bf63b0378e9971c37294e21fa08766fee` | one-cell matrix, tensor-product law, C1--C8 |
| PathCert finite subtrace | `74a1f903ce79fc76a0f32a036a872b2d59b8944aa9e4211135d65ba8e9800db0` | admitted block-diagonal source state and finite completed node |
| source germ V007 | `bd33e54c27ddb8ed5224637d7888a071026db33a1a17c7127a27ffa647b69896` | current exponent and bilocal coefficient |
| finite nonzero-`R` reference | `c7624d88aedaa0659755b5c566121b24c2ad0c29a0060daada43a31b22a6ddfb` | exact finite probe closed form and zero extension |
| O7 status/transfer record | `3c81647eb55ad01d4d71e23b2b45161427f82390098c95afa5721065206a7df2` | Route-T witness and failed-transfer boundary |
| redundancy draft | `a98a955069a9941d8d65a7adbdec012eaf44663bff30b78a68cd16a92be1061b` | status of `(k-1)h_2(p)` under C42 |

All listed cleanroom sidecars used in the calculation were checked and
matched before consumption.

---

## 2. T1 — independent exact recomputation

### 2.1 One-cell matrix and the non-refinement control

Starting only from the ratified one-cell matrix,

```text
W(z) = [[0,1,0],
        [z,0,0],
        [0,0,-1]],

U(z) = P_0 tensor I_3 + P_ch tensor W(z),
```

direct multiplication gives

```text
W(z)^2 = diag(z,z,1).
```

Induction on `m` therefore gives, for every `m>=0`,

```text
W(z)^(2m)|r>   = z^m |r>,
W(z)^(2m+1)|r> = z^(m+1)|p_Q>.
```

With `q=conjugate(z_-)z_+`, the doubled sandwich is consequently

```text
<r|(W(z_-)^k)^dagger W(z_+)^k|r> = q^ceil(k/2).
```

This was also recomputed in exact polynomial arithmetic for `k=1,...,8` as
a finite regression. The proof for all `k` is the displayed induction. It
confirms the tower's first kill-pass: literal reuse of one cell toggles the
ready/pointer ray and is not refinement.

### 2.2 Fresh factors and projector algebra

For fresh record factors, write

```text
U_t = P_0 tensor I_t + P_ch tensor W_t.
```

Using

```text
P_0^2=P_0,  P_ch^2=P_ch,
P_0 P_ch=P_ch P_0=0,
P_0+P_ch=I,
```

an induction gives

```text
product_(t=1)^k U_t
 = P_0 tensor I_(1...k)
   +P_ch tensor product_(t=1)^k W_t.               (CV-1)
```

This is the ratified finite product law, not a new operator class. PathCert's
admitted source family is charge-superselected,

```text
rho_S=P_0 rho_S P_0+P_ch rho_S P_ch,
```

and each unit character cancels in the single-history density. Therefore

```text
rho_k
 =P_0 rho_S P_0 tensor sigma_0,k
  +P_ch rho_S P_ch tensor sigma_1,k,                (CV-2)

sigma_0,k=tensor_t |R_t><R_t|,
sigma_1,k=tensor_t |P_t><P_t|.
```

Tracing the source yields

```text
omega_k=(1-p)sigma_0,k+p sigma_1,k,
p=Tr(P_ch rho_S).                                  (CV-3)
```

No factor in `(CV-1)` redraws the branch. Hence the weights are `(1-p,p)`,
not `((1-p)^k,p^k)`, for every finite `k`.

### 2.3 Realized-branch relay and all-tier induction

On

```text
C_rec,t=span_C{E_R,t,E_P,t} isomorphic to C^2,
```

the one-cell output labels fix the unique label-preserving unital
star-isomorphism

```text
beta_t(E_R,t)=P_0,
beta_t(E_P,t)=P_ch.                                (CV-4)
```

The resulting copier on the two orthogonal realized rays is

```text
|R_t> -> |R_t>|R_(t+1)>,
|P_t> -> |P_t>|P_(t+1)>.                           (CV-5)
```

Applying `(CV-5)` to `(CV-2)` proves the state formula at `k+1`. It neither
splits nor reweights a branch, proving `(CV-3)` for all `k>=1`. The same
branch decomposition applied to the frozen tier exponents gives

```text
F_(k+1)
 =P_0+exp(Xi_(k+1))exp(sum_(t=1)^k Xi_t)P_ch,
```

so

```text
F_k=P_0+exp(sum_t Xi_t)P_ch,
A_k=Tr(rho_S F_k)=(1-p)+p exp(sum_t Xi_t).          (CV-6)
```

For `Xi_t=Xi`,

```text
A_k=(1-p)+p exp(kXi).                              (CV-7)
```

These are identities for every finite `k`; they were not inferred from a
finite enumeration.

### 2.4 Dephasing exponent and the P2 sign check

For declared tier probes,

```text
Xi_t=L_t-(1/2)Q_t,
```

so the charged factor in `(CV-6)` is

```text
exp(sum_t L_t) exp[-(1/2)sum_t Q_t].
```

Thus

```text
D_k=(1/2)sum_t Q_t,
D_k=kQ/2 when Q_t=Q.                               (CV-8)
```

The sign is correct: `D_k` is the positive attenuation exponent and appears
as `exp(-D_k)`. On the local exponent coordinate

```text
Gamma_k(Xi)=Log_0[(1-p)+p exp(kXi)],
```

direct differentiation gives

```text
D_Xi Gamma_k(0)=k p,
D_Xi^2 Gamma_k(0)=k^2 p(1-p).                      (CV-9)
```

There is no recurrence of the P2 sign defect. If instead `Xi=i theta`, the
second derivative with respect to the real phase coordinate is

```text
D_theta^2 Gamma_k(0)=-k^2 p(1-p),                 (CV-10)
```

because `i^2=-1`. The tower's positive `(CV-9)` is explicitly an `Xi`
derivative, so it is correct.

### 2.5 Tier one

At `k=1`, `(CV-2)` is PathCert's exact completed node, `(CV-6)` is the live
one-cell source-inserted operator and scalar contraction, and `(CV-8)` is the
one-cell attenuation `Q/2`. The tier-one state, operator, scalar, and probe
forms reproduce the sealed one-cell structures exactly.

```text
T1_TIER_STATE = PASS
T1_TIER_WEIGHT = PASS
T1_TIER_AMPLITUDE = PASS
T1_DEPHASING_SIGN_AND_FACTOR = PASS
```

---

## 3. T2 — falsifier arms

### 3.1 Identity input

For every tier set `L_t=Q_t=0`, hence `Xi_t=0`. Then `(CV-6)` gives

```text
F_k=P_0+P_ch=I,
A_k=(1-p)+p=1                                      (CV-11)
```

for every finite `k`. This is an algebraic identity, not an observation at
selected tiers.

### 3.2 Tier restrictions

For the observable inclusion and state restriction

```text
iota_(k,k+1)(A)=A tensor I_(k+1),
Res_(k+1,k)=partial trace over tier k+1,
```

normalization of `E_R,k+1` and `E_P,k+1` gives

```text
Res_(k+1,k)(rho_(k+1))=rho_k,
omega_(k+1) composed with iota_(k,k+1)=omega_k.    (CV-12)
```

For amplitudes the restriction square closes exactly when the appended tier
is an identity tier:

```text
Xi_(k+1)=0  =>  F_(k+1)=F_k and A_(k+1)=A_k.       (CV-13)
```

A nonidentity tier multiplies the charged factor and is correctly not called
an amplitude restriction. This distinction matches the ratified
zero-extension certificate.

### 3.3 Reality, quotient, and rank

Factorwise reality gives

```text
Xi_(-n),t(Theta inputs)=conjugate(Xi_n,t(inputs)),
```

and therefore conjugates the sum and exponential. With symbolic real `p`,
the scalar amplitude is reality-covariant. Each tier character and declared
`Q_t` descends before multiplication, so the finite quotient certificate is
stable under the product. The only rank-sensitive datum remains

```text
p=r_ch/(r_0+r_ch),
```

which is carried symbolically; no rank is selected and no ratio is evaluated.

```text
T2_IDENTITY_ARM = PASS
T2_RESTRICTION_ARM = PASS
T2_REALITY_ARM = PASS
T2_QUOTIENT_ARM = PASS
T2_RANK_DISCIPLINE = PASS
```

---

## 4. T3 — source conditioning and the two scope notes

### 4.1 Growth genuinely requires declared tier input

Equation `(CV-8)` contains only the declared `Q_t`. Neither `(CV-1)` nor the
copier `(CV-5)` produces a bilocal source. At identity input, `(CV-11)` holds
and the attenuation exponent is zero. In the pure-law history family the
charged factor is a product of unit characters, so there is phase
accumulation but no attenuation. Therefore the linear `D_k` growth is
genuinely source-conditioned.

The converse attack examined all three meanings of iteration present in the
tower artifact:

1. same cell: toggling and `q^ceil(k/2)`;
2. fresh factors under one source: `product_t q_t`;
3. realized branch relay: the same branch product after `(CV-4)`.

None produces a source-free real attenuation. A term was not suppressed by
choosing the quotient: the full source/background feedback needed to produce
the next `Q_t` from the previous output does not exist. That stronger claim
remains `TYPE-U`, exactly as the tower reports.

### 4.2 Note 1 — tier-local probe scope is load-bearing

The tower freezes a sequence of independently supplied tier inputs
`{Xi_t}` and explicitly scopes the datum to “declared nonidentity tier
probes.” Within that family, `(CV-8)` is exact.

The current complete germ also types the bilocal coefficient as

```text
b^even=hbar ell tensor ell,
Q^even(R)=<b^even,K_R(R)>.
```

On a completed multi-tier source, an arbitrary bilocal `R` need not have
been declared as a direct sum of tier-local pieces. The artifact does not
prove that every such completed `R` decomposes as `Q(R)=sum_t Q_t`; nor does
it need that theorem for its frozen tier-local family. Consequently:

```text
D_k=(1/2)sum_t Q_t = CONFIRMED |
  scope: independently declared tier-local probes

D_k=(1/2)Q_complete(R) WITH Q_complete=sum_t Q_t FOR EVERY R
  = NOT BUILT | TYPE-U
```

This note prevents later consumers from silently upgrading the first formula
to the whole completed bilocal carrier.

### 4.3 Note 2 — “no intrinsic growth” is not a global statistic theorem

The tower itself computes

```text
T_k=(k-1)h_2(p),
```

the total correlation of the shared-branch record state. Q-329 already
computed this exact intrinsic, extensive statistic and C42 rejected it as
the requested nonadditive redundancy/depth selector. Therefore the tower's
line

```text
INTRINSIC_RECORD_ONLY_DEPTH_GROWS_WITH_K = false | TYPE-R
```

cannot be consumed as the global claim “no intrinsic record statistic grows
with `k`.” The correct verified negative is narrower:

```text
INTRINSIC_RECORD_ONLY_RELATIVE_AMPLITUDE_DEPHASING_OR_MIXTURE_LOG_GROWS
  = false | TYPE-R |
  test: identity source CV-11 and unit-character law
```

This is a wording/typing scope note. It does not inherit into Q-330 because
Q-330 expressly distinguishes fixed weights, source-conditioned `D_k`, and
the prior extensive statistic's rejected standing.

```text
T3_SOURCE_CONDITIONING = CONFIRMED
T3_NO_SUPPRESSED_INTRINSIC_ATTENUATION = CONFIRMED
T3_UNRESTRICTED_BILOCAL_UPGRADE = TYPE-U
T3_GLOBAL_NO_GROWING_RECORD_STATISTIC = REFUTED | TYPE-R
```

---

## 5. T4 — O7 confinement

The O7 source says, on the Route-T transfer operator only, refinement changes
the exact singular datum from `3/8` to `(3/8)^k`, changes the color dimension
from `3` to `3^k`, refutes an exact preserving intertwiner, and supplies no
small refinement parameter. The same source expressly does not certify a
response-map pullback.

An equation-by-equation provenance check of the tower finds:

```text
rho_k:      PathCert state + ratified write + realized branch relay
omega_k:    source trace of rho_k
F_k:        ratified conditional characters + declared tier germ inputs
A_k:        source-state contraction
D_k:        declared Q_t terms
```

None contains `3/8`, the Route-T transfer operator, `tau_R`, its spectral
datum, a sea-tier functional, or a response pullback. O7 contributes only
the finite tensor-power/fresh-factor warning. Hence:

```text
O7_3_OVER_8_TO_K_TRANSPORTED = false | TYPE-R |
  test: provenance of every tower factor
O7_ROUTE_T_STRUCTURE_SILENTLY_USED = false | TYPE-R |
  test: the same provenance sweep
O7_CARRIER_SHAPE_WARNING_RESPECTED = true
```

T4 passes.

---

## 6. T5 — allow/require theorem for every tier

### 6.1 Require-side invariance

The require-side statement is the branch commitment. At tier one the source
state fixes the normalized conditional states with weights `(1-p,p)`. The
relay `(CV-5)` maps each conditional state isometrically to the same label
with one normalized factor appended. It neither introduces a new branch nor
changes either trace. Therefore, by induction,

```text
weight_0(k)=1-p,
weight_ch(k)=p
```

for every finite `k>=1`. This is proved, not inferred from computed examples.

### 6.2 Allow-side accumulation

On the charged branch, conditional characters and declared germ factors
multiply:

```text
Z_ch,k=product_t q_t
```

for pure law data and

```text
Z_ch,k=exp(sum_t Xi_t)
```

for the declared source/probe family. Therefore phase/exponent content is
additive before the physical branch mixture. For identical declared inputs,
the charged conditional forms are `q^k` and `exp(kXi)`.

This is exactly the allow-side accumulation Q-330 records. Two qualifications
remain binding:

1. at identity input it is the identity, so no intrinsic nonidentity content
   is generated;
2. the physical scalar amplitude and local mixture log need not grow
   monotonically and are not `Log k`.

Thus “allow accumulates” is an exact conditional-factor statement, not a
claim that a bounded pure-phase scalar grows in magnitude.

```text
REQUIRE_SIDE_INVARIANCE_ALL_FINITE_K = PROVED | TYPE-P
ALLOW_SIDE_MULTIPLICATION_ALL_FINITE_K = PROVED | TYPE-P
ALLOW_SIDE_SOURCE_FREE_NONTRIVIAL_GROWTH = false | TYPE-R
ALLOW_SIDE_PHYSICAL_SCALAR_MONOTONICITY = false | TYPE-R
```

---

## 7. Verdict, inheritance, and next object

### 7.1 Verdict

```text
VERDICT = CONFIRMED_WITH_NOTES

CONFIRMED:
  tower state and weights for every finite k;
  A_k=(1-p)+p exp(sum_t Xi_t);
  identical-tier A_k=(1-p)+p exp(kXi);
  D_k=(1/2)sum_t Q_t and identical-tier kQ/2;
  tier-1 exact reproduction;
  identity-input A_k=1;
  state restrictions and identity-tier amplitude restriction;
  reality, quotient, and symbolic-rank discipline;
  O7 Route-T confinement;
  require-side invariance and allow-side accumulation.

NOTES:
  the D_k formula is tier-local/declared-probe scoped;
  the broad no-intrinsic-growth sentence must be narrowed because the
  already-known total correlation grows extensively;
  RT-27 is positive only in the Xi coordinate; the physical phase-coordinate
  second derivative has the P2-required minus sign.
```

### 7.2 Inheritance

The notes do not impeach the registered Q-330 theorem. They prohibit two
later overextensions:

1. treating the declared tier family as an arbitrary complete bilocal input;
2. treating “no intrinsic amplitude/dephasing depth” as “no growing record
   statistic of any kind.”

The central description remains exact:

```text
require: fixed (1-p,p) branch commitment;
allow:   charged conditional exponent/phase accumulation;
mixture: Log_0[(1-p)+p exp(sum_t Xi_t)].
```

### 7.3 Exact remaining object

Nothing in this cross-check closes the tower's admitted gap. The next object
remains:

```text
FULL_FINITE_RECORD_TO_SOURCE_BACKGROUND_REFINEMENT_CHANNEL := (
  full record-algebra relay including the e/coherence sector,
  next-tier source-density map,
  next-tier J/R or holonomy-generation map,
  fresh-ready assignment,
  restriction/reality/quotient certificates,
  tier-one falsifier
).
```

Until that exists, nonidentity tier data is declared input, not generated by
the previous record.

```text
FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-S

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

---

## 8. Custody

This lane writes and seals this determination, verifies its sidecar, mirrors
the artifact and sidecar byte-identically to the archive workspace, reports
the hashes, and stops. It does not edit the register, plan, or tracker and
performs no git, commit, or push action.
