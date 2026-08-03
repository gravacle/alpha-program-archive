# Stage 8 Task 4a Finite Record-Refinement Tower Exact Computation v001

Date: 2026-08-03  
Lane: CODEX LANE 2  
Task: PASTE 412 / Task 4a / C43  
Register head at freeze: Q-329  
Plan head at freeze: C43  
Status: **THE REALIZED-BRANCH REFINEMENT TOWER CONSTRUCTS EXACTLY AND YIELDS THE FIRST DEPTH-BEARING FINITE DATUM IN A SHARPLY SCOPED FORM: THE CHARGED DEPHASING EXPONENT IS `D_k=(1/2)sum_t Q_t`, HENCE `kQ/2` FOR IDENTICAL DECLARED TIER PROBES. IT IS LINEAR, NOT LOGARITHMIC, AND SOURCE-CONDITIONED RATHER THAN INTRINSIC TO THE RECORD ALONE. BRANCH WEIGHTS REMAIN `(1-p,p)`, BRANCH DISTINGUISHABILITY IS MAXIMAL AT TIER 1, AND IDENTITY-TIER AMPLITUDES ARE `k`-INVARIANT. THE PHYSICAL MIXTURE LOG IS `Log_0[(1-p)+p exp(k Xi)]`, NOT `Log k`. A FULL RECORD-ALGEBRA/BACKGROUND FEEDBACK TOWER REMAINS TYPE-U.**

```text
REALIZED_BRANCH_QUOTIENT_REFINEMENT_TOWER_CONSTRUCTED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014 |
  scope: finite realized ready/pointer branch quotient, every k>=1

DEFAULT_POSITIVE_STANDING = TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014 |
  rule: every positive tower, restriction, reality, quotient, or falsifier
        claim below inherits these premises unless stated as a bare algebraic
        derivation conditional on the displayed finite matrices

FULL_RECORD_ALGEBRA_REFINEMENT_CHANNEL_CONSTRUCTED = false | TYPE-U |
  would-build: a certified record-output-to-source/background channel on
               the full record algebra, including the unused e-sector,
               source history generation, and its restriction certificates

INTRINSIC_RECORD_ONLY_DEPTH_GROWS_WITH_K = false | TYPE-R |
  scope: the constructed realized-branch tower |
  test: equations RT-8 through RT-13 at identity tier data

SOURCE_CONDITIONED_CHARGED_EXPONENT_GROWS_WITH_K = true | TYPE-P |
  premises: the same ratified stack |
  form: sum_t Xi_t; identical-tier form k Xi

FIRST_DEPTH_BEARING_FINITE_DATUM_EXISTS = true | TYPE-P |
  scope: declared nonidentity tier probes on the realized branch tower |
  datum: D_k=(1/2)sum_t Q_t; identical-tier form kQ/2 |
  growth: linear in k, not logarithmic

FIRST_NEW_INTRINSIC_DEPTH_BEARING_DATUM = false | TYPE-R |
  scope: the constructed tower and requested extracted quantities
O7_ROUTE_T_DEPTH_DATUM_TRANSFERRED_TO_THIS_TOWER = false | TYPE-R |
  test: the sealed O7 transfer determination

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

---

## 0. Lead determination

The requested phrase “apply the write dynamics to its own output” has three
mathematically different readings. They must not be merged.

1. **Reuse the same record cell.** This is executable, but the write toggles
   ready and pointer. It does not add a tier.
2. **Use a fresh record factor controlled by the original source.** This is
   executable and is exactly the already-ratified finite tensor-product law.
   The previous record is not the next source.
3. **Use the completed record as the next source.** This is executable without
   choice only after restricting to the realized classical branch quotient
   `span{ready,pointer}`. The ratified output correlation fixes the quotient
   identifications `ready <-> neutral` and `pointer <-> charged`. It does not
   fix a channel on the full `M_3(C)` record algebra or generate the next
   tier's connection/bilocal background.

The task's state, weights, and scalar amplitude live on the realized branch
quotient, so the finite path tower can be constructed exactly there. The
full operator feedback tower cannot be promoted from that path computation.

Let `t=1,...,k` label refinement tiers. Let

```text
|R_t>:=the fresh ready ray at tier t,
|P_t>:=the completed pointer ray at tier t,
p:=Tr(P_ch rho_S)=p_[A]=r_ch/(r_0+r_ch),
Xi_t:=L_t-(1/2)Q_t
```

be the live finite germ exponent supplied independently at tier `t`. Then the
exact tower is

```text
rho_tower,k
 =P_0 rho_S P_0 tensor_(t=1)^k |R_t><R_t|
  +P_ch rho_S P_ch tensor_(t=1)^k |P_t><P_t|,      (RT-1)

omega_tower,k
 =(1-p) tensor_t |R_t><R_t|
  +p tensor_t |P_t><P_t|,                          (RT-2)

F_tower,k
 =P_0+exp[sum_(t=1)^k Xi_t]P_ch,                   (RT-3)

A_tower,k
 =(1-p)+p exp[sum_(t=1)^k Xi_t].                   (RT-4)
```

For identical declared tier data `Xi_t=Xi`,

```text
A_tower,k=(1-p)+p exp(k Xi).                       (RT-5)
```

The branch weights do **not** become products of independent Bernoulli
weights. The same one-bit branch is copied through the tower, so they remain
`(1-p,p)` at every tier. The two conditional record strings are orthogonal
from tier 1 onward. Consequently

```text
(1/2)||sigma_0,k-sigma_1,k||_1=1,
Fidelity(sigma_0,k,sigma_1,k)=0                    (RT-6)
```

for every `k>=1`. Re-recording does not deepen literal branch
distinguishability.

The charged conditional exponent is additive. For identical real bilocal
probe data, its attenuation exponent is exactly linear:

```text
D_k=(1/2)sum_t Q_t=k Q/2.                          (RT-7)
```

But this is source-conditioned accumulation: the `Q_t` are declared tier
inputs, not content generated by the completed record. At identity tier data
`L_t=Q_t=0`, equations `(RT-3)` and `(RT-4)` give

```text
F_tower,k=I_src,
A_tower,k=1                                        (RT-8)
```

for every `k`. Thus the record alone creates no growing amplitude datum.

On the common local logarithm chart,

```text
Gamma_tower,k
 :=Log_0 A_tower,k
 =Log_0[(1-p)+p exp(sum_t Xi_t)],                  (RT-9)

Gamma_tower,k|_(Xi_t=Xi)
 =Log_0[(1-p)+p exp(k Xi)].                        (RT-10)
```

This is a log of a two-branch mixture, not an additive sum and not a
`Log k` law. No global logarithm is claimed when the tier product leaves the
declared `Log_0` chart.

---

## 1. Custody, preflight, currency, and authorities

### 1.1 Preflight after the type check

```text
DOES_THE_FULL_REFINEMENT_TOWER_EXIST = PARTIAL |
  realized branch quotient: constructed here |
  full record/source/background channel: false | TYPE-U

IS_THE_VERSION_CURRENT = true |
  register head: Q-329 |
  plan head and tracker relay: C43 / 412

ARE_ITS_INPUTS_PRESENT = PARTIAL |
  present: exact finite law, branch state, ready/pointer quotient, germ,
           finite probe forms, O7 carrier-growth warning |
  absent: full record-to-source/background feedback channel
```

### 1.2 Frozen authorities

| Authority | SHA-256 | Load-bearing use |
|---|---|---|
| `LOCKED_PROCESS.md` | `f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba` | fences, typing, custody |
| `QUESTIONS_SETTLED_REGISTER_V001.md` | `9589a5581f66a71d4dd0101d3ceb1ad67192e7e1948b3773be59d6ebad53bb2c` | Q-329 head at freeze |
| `TASK_LIST_HERE_TO_ALPHA_2026-08-01_V002.md` | `03ad086fe616dcc09dd40c5a74d2e9898ef420c0a38b01f122a12b7664a0c376` | C43 commission |
| `EXECUTION_TRACKER.md` | `ef30554e1e3e500fd2cf1a1ee072fbdd938d442aaa140a94d56f51c024fbf5d4` | relay 412 sent under C43 |
| `RELAY_PASTE_412_THE_FIRST_DEPTH_COMPUTATION_V001.md` | `9525412e528ea025232f16ef943428888218d4d4e9acdbbca00ea8a5e27506d4` | task contract |
| Decision of Record 009 | `11632fa30dfe9225c228f07a3be4717c73bdfc9e38b0c76c46d905d3fe193bc5` | ratified `E_post` law |
| `STAGE8_SOURCE_COUPLED_RECORD_TRANSITION_LAW_ADOPTION_PROPOSAL_V002.md` | `db1808e4da38cbfed8b12017885aff1bf63b0378e9971c37294e21fa08766fee` | exact one-cell and tensor-product write |
| `STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_FUNCTIONAL_RESULT_V001.md` | `2cd1ffcefd68ac03c6c09a4eca0dc9fe8d1adc8ac564cc0d050dfd41d79e6d0f` | `U_N`, `F_N`, ready/pointer states |
| `STAGE8_ENVELOPE_FINITE_PATHCERT_DYNAMICS_SUBTRACE_CONSTRUCTION_V001.md` | `74a1f903ce79fc76a0f32a036a872b2d59b8944aa9e4211135d65ba8e9800db0` | exact completed state and record restrictions |
| `STAGE8_SHARED_FINITE_STATE_EFFECT_CONDITIONED_AMPLITUDE_SHARP_STOP_V001.md` | `2cbec1f0adefaa7f962bde505117c95a0f8c08cd6a8ea508aec4eef006fd6c12` | exact scalar contraction |
| `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V007.md` | `bd33e54c27ddb8ed5224637d7888a071026db33a1a17c7127a27ffa647b69896` | live `Xi`, `Q_even`, and `Log_0` interface |
| `STAGE8_TASK4A_FINITE_NONZERO_R_REFERENCE_EXACT_PROBE_SOURCE_COMPUTATION_V001.md` | `c7624d88aedaa0659755b5c566121b24c2ad0c29a0060daada43a31b22a6ddfb` | exact source/probe closed forms |
| `STAGE8_TASK4A_COLLECTIVE_BRANCH_REDUNDANCY_DEPTH_FUNCTIONAL_DRAFT_DETERMINATION_V001.md` | `a98a955069a9941d8d65a7adbdec012eaf44663bff30b78a68cd16a92be1061b` | Q-329 branch-state and saturation facts |
| `STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V003.md` | `1be5f6a7e40c34586f3b5ab78f9129de0b5d2041cb6695b0e549443ddd6c6ee0` | common source, ready, and law generation; no feedback field |
| `STAGE8_O7_RESPONSE_PULLBACK_TRANSFER_CHECK_V001.md` | `dcf29eeae27c25ee17c93671acb32336c5e227d97a2280a3fa8668f17610c57d` | O7 transfer-failure boundary |
| `STAGE8_RESPONSE_MAP_O7_ANALOGUE_WITNESS_CHECK_V001.md` | `6f8f0dd3209e3bf10ba6c1e1ab766cdccafc226f507486b216a0d33d2b2cb3ad` | response-transfer prohibition |
| `STAGE8_T7_MAJORANT_PHASE2_STATUS_AND_O7_ESCALATION_V001.md` | `3c81647eb55ad01d4d71e23b2b45161427f82390098c95afa5721065206a7df2` | exact O7 tensor-power witness |

The relay and every local authority above having a sidecar verified `OK`
before use. No private holdout root was entered.

### 1.3 Roots entered

```text
ROOTS_ENTERED = (
  /Users/bgm/Documents/New project/gravity_emergence_evidence_program/
    alpha_fundamental_record_action_cleanroom_v003,
  /Users/bgm/MB Work/alpha_supervision,
  /Users/bgm/MB Work/alpha-program-archive/workspace,
  /Users/bgm/MB Work/alpha-program-archive/cleanroom_output,
  /Users/bgm/MB Work/alpha-program-archive/supervision
)

a32_holdout/custodian_private/ = NOT_ENTERED | TYPE-S
```

### 1.4 Bearing symbol distinctions

```text
N in the ratified law = number of fresh finite record cells;
k in this artifact    = number of record-of-record tiers;

|R_t>                 = ready record ray at tier t;
R in Q_t(R)           = bilocal probe source, not a ready ray;

F_law,tower,k         = record-sandwiched source operator;
Fidelity              = state distinguishability functional, not F_N;

Q_t                   = tier-t live bilocal quadratic functional;
Q_N^phys              = historical relative-history quotient carrier;

(3/8)^k               = O7 Route-T transfer-operator singular datum;
exp(sum_t Xi_t)       = this tower's charged source factor.
```

No equality is inferred from a shared index or the words “tier,” “record,”
or “refinement.”

---

## 2. The input and output types

For one record cell, the ratified write is

```text
W(z)=D(z)S
    =[[0,1,0],
      [z,0,0],
      [0,0,-1]],

U(z)=P_0 tensor I_3+P_ch tensor W(z).              (RT-11)
```

Its domain and codomain are both

```text
H_src tensor H_rec,
H_rec=C^3=span{|r>,|p_Q>,|e_Q>}.
```

But the next application requires two logically separate inputs:

```text
source branch/background: (P_0,P_ch; a or J,R),
fresh ready record: |r>.
```

The completed record supplies a ready/pointer record ray. It does not supply
a new connection history, bilocal source, or full source density. PathCert's
record restriction retains the source only through `p`; Gen_Omega generates
the source state, ready ray, and law from common primitives by three separate
maps. Neither authority defines a feedback map from an output record to the
next source/background port.

```text
LAW_OUTPUT_TYPE_EQUALS_NEXT_COMPLETE_INPUT_TYPE = false | TYPE-R |
  test: record ray versus source branch/background plus fresh ready ray

SEALED_RECORD_TO_NEXT_BACKGROUND_MAP_EXISTS = false | TYPE-S |
  scope: cleanroom, archive workspace, archive cleanroom_output, supervision
SEALED_FULL_RECORD_TO_SOURCE_CHANNEL_EXISTS = false | TYPE-S |
  scope: the same word-boundaried source sweep
```

### 2.1 Literal same-carrier iteration is a toggle

Direct matrix multiplication gives

```text
W(z)^2=diag(z,z,1).
```

Therefore, for `m>=0`,

```text
W(z)^(2m)|r>=z^m|r>,
W(z)^(2m+1)|r>=z^(m+1)|p_Q>.                      (RT-12)
```

At zero background this is simply `S^2=I`: repeated writes alternate ready
and pointer. The carrier dimension remains three. In a doubled history with
`q=conjugate(z_-)z_+`, the same-cell sandwich is

```text
<r|(W(z_-)^k)^dagger W(z_+)^k|r>
  =q^ceil(k/2).                                    (RT-13)
```

This is exact, but it is not a `3^k` tier and it does not retain a completed
record while creating a new one. It is excluded as the requested refinement
interpretation by proof, not preference.

```text
SAME_CELL_SELF_ITERATION_IS_RECORD_REFINEMENT = false | TYPE-R
SAME_CELL_SELF_ITERATION_IS_MONOTONE_COMMITMENT = false | TYPE-R
```

### 2.2 Fresh factors controlled by the original source

For fresh record legs, source-projector orthogonality gives

```text
product_(t=1)^k U_t
 =P_0 tensor I+P_ch tensor_(t=1)^k W_t.            (RT-14)
```

This is exactly the ratified `U_N` product with the cell index renamed `t`.
It yields `(RT-1)` through `(RT-4)`, but the original source controls every
leg. It is the correct algebraic shadow of the tower and an internal check;
by itself it is not proof that the previous record became the next source.

```text
FRESH_FACTOR_SHARED_SOURCE_TOWER_IS_NEW_OPERATOR_CLASS = false | TYPE-R |
  test: RT-14 is the ratified finite-locality formula
```

---

## 3. The realized-branch quotient refinement

### 3.1 The quotient and its unique relay

On the realized path, only two record projections occur:

```text
E_R,t:=|R_t><R_t|,
E_P,t:=|P_t><P_t|,
C_rec,t:=span_C{E_R,t,E_P,t} isomorphic to C^2.
```

The ratified completed state fixes their source labels:

```text
P_0 rho_S P_0 -> E_R,t,
P_ch rho_S P_ch -> E_P,t.
```

Hence there is one label-preserving unital star-isomorphism on the realized
branch algebras,

```text
beta_t:C_rec,t -> C_src,
beta_t(E_R,t)=P_0,
beta_t(E_P,t)=P_ch.                                (RT-15)
```

This map is derived on `C_rec,t`: swapping the images would contradict the
sealed one-cell state, and any other image would fail minimal projections or
unitality. No assertion is made about `|e_Q><e_Q|` or record coherences,
which do not occur in the ready-path output.

The next tier uses `beta_t` to carry the same branch fact and the ratified
law on a fresh ready leg. On the two conditional rays this is the copier

```text
C_t:
  |R_t> -> |R_t>|R_(t+1)>,
  |P_t> -> |P_t>|P_(t+1)>.                        (RT-16)
```

It is an isometry on the realized two-dimensional branch span. Equation
`(RT-16)` is not a universal quantum cloner: its domain is the declared
orthogonal classical branch basis, and no action on arbitrary superpositions
or the unused `e` sector is consumed.

```text
REALIZED_BRANCH_RELAY_UNIQUE = true | TYPE-P |
  premises: sealed ready/pointer labeling and branch quotient |
  scope: C_rec,t only

FULL_M3_RELAY_UNIQUE = false | TYPE-R |
  counterfamily: inequivalent extensions on the unused e-sector and
                 off-diagonal record operators agree on C_rec,t
```

### 3.2 Exact induction

Tier 1 is the sealed completed state. Suppose tier `k` is `(RT-1)`. Applying
`C_k` maps each conditional tensor string to the same string with one copy
appended and leaves its central source block unchanged. This proves `(RT-1)`
and `(RT-2)` for `k+1`. The same branch split gives

```text
F_tower,k+1
 =P_0+exp(Xi_(k+1))exp(sum_(t=1)^k Xi_t)P_ch,
```

which is `(RT-3)` at `k+1`. Contracting with the ratified source state gives
`(RT-4)`. Thus the formulas hold for every finite `k>=1`.

No post-output datum is introduced. The sequence of tier source/probe inputs
`{Xi_t}` is frozen as part of the tower input. It is not generated after an
output is observed.

---

## 4. Closed forms and exact `k`-dependence

### 4.1 Tier state and weights

Let

```text
sigma_0,k:=tensor_t E_R,t,
sigma_1,k:=tensor_t E_P,t.
```

Then

```text
omega_tower,k=(1-p)sigma_0,k+p sigma_1,k.          (RT-17)
```

The weights are exactly

```text
weight_0(k)=1-p,
weight_ch(k)=p.                                    (RT-18)
```

They are not `(1-p)^k` and `p^k`. Such powers would describe independent
branch draws, not repeated testimony about one shared fact.

### 4.2 Branch distinguishability

Because `<R_t|P_t>=0` already at one tier,

```text
<sigma_0,k,sigma_1,k> support overlap =0,
trace distinguishability=1,
fidelity=0,
optimal branch error=0                              (RT-19)
```

for all `k>=1`. There is no approach-to-orthogonality law to extract: the
ratified ideal write is already at the orthogonal endpoint.

The standard total correlation of `(RT-17)` is

```text
T_k=(k-1)h_2(p).                                   (RT-20)
```

Q-329 already computed this shared-branch extensive count and rejected it as
the C42 redundancy selector. C43 does not turn that pre-existing extensive
statistic into a new refinement observable.

### 4.3 Pure holonomy amplitude

For relative tier characters

```text
q_t:=product_j conjugate(z_(-,t,j))z_(+,t,j),
```

the pure-law forms are

```text
Z_law,tower,k=product_(t=1)^k q_t,
F_law,tower,k=P_0+Z_law,tower,k P_ch,
A_law,tower,k=(1-p)+p Z_law,tower,k.              (RT-21)
```

If every tier carries the same declared `q`, then

```text
Z_law,tower,k=q^k,
A_law,tower,k=(1-p)+p q^k.                         (RT-22)
```

Since `|q|=1`, the conditional charged branch accumulates phase but no
attenuation. The scalar modulus is

```text
|A_law,tower,k|^2
 =1-2p(1-p)[1-Re(product_t q_t)].                  (RT-23)
```

It is bounded and generally oscillatory; no monotone record depth follows.

### 4.4 Probe-on germ amplitude

The live tier input is

```text
Xi_t=L_t-(1/2)Q_t.
```

Therefore `(RT-4)` is the exact probe-on answer. If every tier receives the
same frozen probe/history datum,

```text
A_probe,tower,k=(1-p)+p exp[kL-kQ/2].              (RT-24)
```

The charged-sector dephasing exponent and charged log are

```text
D_k=kQ/2,
Log(charged factor)=k(L-Q/2)                       (RT-25)
```

on the declared chart. They are linear, not logarithmic, in tier count. The
physical mixture log remains `(RT-10)`. Its nonadditivity is exact:

```text
Log_0[(1-p)+p exp((k+l)Xi)]
 !=Log_0[(1-p)+p exp(kXi)]
   +Log_0[(1-p)+p exp(lXi)]                        (RT-26)
```

generically for the symbolic interior branch family.

The first local jets with respect to one repeated tier parameter `Xi` are

```text
D_Xi Gamma_tower,k|_(Xi=0)=k p,
D_Xi^2 Gamma_tower,k|_(Xi=0)=k^2 p(1-p).           (RT-27)
```

These powers reflect applying the same external source variation to every
tier simultaneously. They are not generated when the record is refined at
fixed identity source. With independent tier variables,

```text
D_(Xi_s)Gamma|_0=p,
D_(Xi_s)D_(Xi_t)Gamma|_0=p(1-p) for s!=t,          (RT-28)
```

which exposes the one shared branch correlation.

### 4.5 `k`-dependence table

| Quantity | Exact tier-`k` form | Intrinsic record-only growth? |
|---|---|---|
| branch weights | `(1-p,p)` | no |
| branch trace distinguishability | `1` for `k>=1` | no; saturated |
| branch fidelity | `0` for `k>=1` | no; saturated |
| total correlation | `(k-1)h_2(p)` | pre-existing extensive statistic, not a refinement selector |
| charged relative phase | `product_t q_t`; identical `q^k` | only with declared nonidentity histories |
| charged dephasing exponent | `(1/2)sum_t Q_t`; identical `kQ/2` | only with declared probes |
| scalar amplitude | `(1-p)+p exp(sum_t Xi_t)` | identity input gives `1` |
| scalar log | `Log_0[(1-p)+p exp(sum_t Xi_t)]` | no universal additive or `Log k` law |
| O7 Route-T singular datum | `(3/8)^k` | yes on O7's transfer operator only; not this tower |

```text
LOGARITHMIC_IN_K_DEPTH_LAW_FOUND = false | TYPE-R |
  scope: the admitted exact tower family RT-17 through RT-28
LINEAR_CHARGED_PROBE_EXPONENT_FOUND = true | TYPE-P |
  scope: declared repeated nonidentity tier probe
MONOTONE_SCALAR_AMPLITUDE_DEPTH_FOUND = false | TYPE-R |
  scope: the admitted symbolic pure-phase and probe-on family
```

---

## 5. Tier restriction and refinement versus extension

### 5.1 State restriction

Define the observable embedding and state restriction

```text
iota_(k,k+1)(A)=A tensor I_(t=k+1),
Res_(k+1,k)=partial trace over tier k+1.
```

Equations `(RT-17)` and trace normalization give

```text
omega_tower,k+1 o iota_(k,k+1)=omega_tower,k,
Res_(k+1,k)(rho_tower,k+1)=rho_tower,k.            (RT-29)
```

This is exact for all tier source data because the single-history density is
phase-blind.

### 5.2 Amplitude restriction

The amplitude remembers the relative history. If the removed tier is an
identity tier, `Xi_(k+1)=0`, then

```text
F_tower,k+1=F_tower,k,
A_tower,k+1=A_tower,k.                             (RT-30)
```

This is the exact analogue of zero extension. A nonidentity tier instead
multiplies the charged factor by `exp(Xi_(k+1))`; forgetting it is not an
amplitude restriction square. That difference is source-conditioned and is
not present at identity background.

### 5.3 What is genuinely different from dead zero extension

Zero extension appends a factor whose **relative-history** contribution is
the identity, even though the single-history write still maps a fresh ready
record to a pointer on the charged branch. The quotient refinement tower
adds a new record witness at every tier, but without a nonidentity declared
tier source its scalar amplitude remains invariant. Therefore:

```text
TIER_STATE_CARRIER_GROWS = true | TYPE-P
TIER_RECORD_COPY_COUNT_GROWS = true | TYPE-P
TIER_RELATIVE_AMPLITUDE_GROWS_AT_IDENTITY_INPUT = false | TYPE-R
```

Carrier growth and repeated testimony are exact. They are not yet the
nontrivial intrinsic depth datum Q-329 says the bridge needs.

---

## 6. Reality, quotient, rank, and tier-1 falsifier

### 6.1 Tier 1

At `k=1`, `(RT-1)` is PathCert's exact completed state and `(RT-3)` through
`(RT-4)` are the ratified one-cell operator and scalar amplitude. Thus the
one-cell falsifier passes exactly.

```text
TIER1_STATE_REPRODUCTION = PASS | TYPE-P
TIER1_OPERATOR_REPRODUCTION = PASS | TYPE-P
TIER1_SCALAR_AMPLITUDE_REPRODUCTION = PASS | TYPE-P
```

### 6.2 Reality

The ratified character and source involutions act factorwise. Hence

```text
Xi_(-n),t(Theta inputs)=conjugate(Xi_n,t(inputs)),

exp(sum_t Xi_(-n),t(Theta inputs))
 =conjugate(exp(sum_t Xi_n,t(inputs))).            (RT-31)
```

With symbolic real `p`, `(RT-31)` proves tower reality. No global logarithm
is inferred; the `Log_0` statement is local on one common nonzero chart.

### 6.3 Quotient and rank discipline

Each relative holonomy factor and each `Q_t` descends under its existing
finite quotient certificate. The tensor product of descended factors
therefore descends tierwise. The branch weight remains

```text
p=p_[A]=r_ch/(r_0+r_ch)
```

symbolically. No rank pair is selected and no ratio is evaluated.

```text
TOWER_REALITY = PASS | TYPE-P
TOWER_FINITE_QUOTIENT_DESCENT = PASS | TYPE-P
TOWER_RANK_VALUE_SELECTED = false | TYPE-S
```

---

## 7. O7 transfer discipline

O7's exact witness says that, for the Route-T transfer operator, replacing
one coarse three-color record factor by `k` independent refined factors
changes the leading record-tier singular datum from

```text
3/8 to (3/8)^k
```

and the color dimension from `3` to `3^k`. It also proves there is no exact
intertwiner preserving that singular data and no small refinement parameter.

The O7 transfer check then states that this witness does **not** transfer to
the response-map pullback. The present calculation respects both facts:

1. it uses the tensor-power/fresh-ready-root **carrier shape** as a warning
   that refinement needs new factors;
2. it does not insert `3/8`, the O7 transfer operator, `tau_R`, a spectral
   gap, a response pullback, or a sea-tier functional into `(RT-1)` through
   `(RT-31)`;
3. it makes no continuum or bridge claim.

```text
O7_CARRIER_SHAPE_USED = true |
  scope: finite tensor-power/fresh-root distinction only

O7_SINGULAR_VALUE_IMPORTED_INTO_RECORD_LAW = false | TYPE-S
O7_RESPONSE_PULLBACK_CLAIMED = false | TYPE-S
O7_EXACT_INTERTWINER_REVIVED = false | TYPE-S
```

The O7 datum remains the corpus's depth-adjacent exact result on its own
Route-T object. It does not become the new tower's weight, amplitude, or
response by shared vocabulary.

---

## 8. Kill passes and counterexamples

### 8.1 Counterexample to a unique unrestricted tower

The same ratified `W` supports two exact operations with different outputs:

```text
same carrier k applications -> q^ceil(k/2), ready/pointer toggle;
fresh factors k applications -> q^k, k retained record copies.
```

Thus the word “iterate” does not select a refinement operation. The
fresh-factor and branch-relay declarations are load-bearing.

### 8.2 Counterexample to full-channel uniqueness

On the realized branch algebra, `beta_t` is unique. On the full record
algebra, two channels may agree on `E_R,E_P` and differ on the unused
`E_e=|e_Q><e_Q|` projection or on off-diagonal coherences. The ready-path
state and every displayed amplitude cannot distinguish them. Therefore the
path construction cannot be upgraded to a unique full channel.

### 8.3 Counterexample to intrinsic amplitude depth

Set every tier input to the lawful identity datum `Xi_t=0`. The carrier and
record-copy count grow, but `(RT-8)` holds for all `k`. Hence carrier growth
alone does not force relative amplitude or log growth.

### 8.4 Counterexample to a universal logarithmic law

The exact family `(RT-10)` contains:

```text
Xi=0: Gamma_tower,k=0;
pure phase Xi: bounded/oscillatory scalar amplitude;
real attenuating Xi: branch mixture log of exp(kXi).
```

No single `Log k` dependence covers the admitted symbolic family. Choosing a
tier source to force such behavior would be target tuning.

```text
TARGET_TUNING_USED = false | TYPE-S
CONTINUUM_OBJECT_USED = false | TYPE-S
BRIDGE_CLAIM_MADE = false | TYPE-S
PHYSICAL_RESPONSE_PULLBACK_USED = false | TYPE-S
```

---

## 9. Six-account and door ledger

| Operation class | Kernel/applicability | Image | Sector transfer | Restriction square | Tail action | Verdict |
|---|---|---|---|---|---|---|
| literal same-cell iteration | full finite one-cell carrier | same carrier; toggling path | none | not a refinement square | none | exact negative control |
| shared-source fresh-factor product | finite source plus fresh ready factors | `H_src tensor R^(tensor k)` | source branch copied to records | state restriction exact; amplitude exact on identity tier | none | built; existing `U_N` class |
| realized branch relay `beta_t` | `C_rec,t=span{E_R,E_P}` | `C_src` | ready→neutral, pointer→charged | exact on realized quotient | none | built and unique in scope |
| full record feedback | full `M_3` plus source/background ports | not constructed | e/coherence and background transfers untyped | absent | none | `TYPE-U` |
| scalar contraction | central two-sector operator | scalar `A_tower,k` | no new transfer | exact on identity tier | none | built |
| local logarithm | nonzero common `Log_0` chart | scalar local germ | none | only where chart is shared | none | built locally; no global branch |

Door flags:

```text
DOOR_FINITE_BRANCH_QUOTIENT = OPENED_AND_ACCOUNTED
DOOR_FRESH_TENSOR_CLASS_FORMATION = FINITE_ONLY |
  topology: finite matrix norm |
  kernel: none on retained branch span |
  Tail_R: not entered

DOOR_FULL_RECORD_FEEDBACK = NOT_OPENED | TYPE-U
DOOR_BACKGROUND_GENERATION = NOT_OPENED | TYPE-U
DOOR_GLOBAL_LOG = NOT_OPENED | TYPE-U
DOOR_CONTINUUM_COMPLETION = NOT_OPENED | TYPE-S
DOOR_RESPONSE_PULLBACK = NOT_OPENED | TYPE-S
DOOR_CYCLE_ACTION = NOT_OPENED | TYPE-S
DOOR_CYCLE_INVERSE = NOT_OPENED | TYPE-S
```

---

## 10. Final determination and next exact object

The C43 computation yields a finite, exact realized-branch refinement tower.
It establishes:

```text
TIER_STATE_EXACT_FOR_ALL_FINITE_K = true | TYPE-P
TIER_WEIGHTS_EXACT_FOR_ALL_FINITE_K = (1-p,p)
TIER_AMPLITUDE_EXACT_FOR_ALL_FINITE_K
  = (1-p)+p exp(sum_t Xi_t)

BRANCH_DISTINGUISHABILITY_DEEPENS_AFTER_TIER1 = false | TYPE-R
IDENTITY_TIER_DEPHASING_EXPONENT_GROWS = false | TYPE-R
NONIDENTITY_REPEATED_PROBE_EXPONENT_IS_LINEAR_IN_K = true | TYPE-P
PHYSICAL_MIXTURE_LOG_IS_LOG_K = false | TYPE-R
FIRST_DEPTH_BEARING_FINITE_DATUM
  = D_k=(1/2)sum_t Q_t | identical-tier form kQ/2 | TYPE-P |
    scope: declared nonidentity tier probes
```

The exact `k`-dependence is therefore a separation:

```text
record-only content: carrier/copy count grows; weights and literal
                     distinguishability saturate;

declared source content: charged phase and dephasing exponents add across
                         tiers; identical-tier exponent is linear in k;

physical scalar mixture: Log_0[(1-p)+p exp(kXi)], neither additive nor Log k.
```

The source-conditioned `D_k` is the first exact depth-bearing finite datum
created by C43. No intrinsic record-only depth-bearing scalar is forced. The
smallest next finite
object that would make the stronger tower executable is

```text
FULL_FINITE_RECORD_TO_SOURCE_BACKGROUND_REFINEMENT_CHANNEL := (
  beta_full on M_3 record operators,
  next-tier source-density map,
  next-tier J/R or holonomy-generation map,
  fresh-ready carrier assignment,
  restriction/reality/quotient certificates,
  tier-1 falsifier
).
```

That object must be derived or proposed before any nonidentity tier source
can be called **generated by the previous record**. Until then, the exact
nonidentity `k`-growth in this artifact is source-conditioned, not an
intrinsic record-of-record law.

```text
FINITE_REFINEMENT_PROGRAM_HAS_EXACT_GROUND_TOWER = true | TYPE-P |
  scope: realized branch quotient

FINITE_REFINEMENT_PROGRAM_HAS_INTRINSIC_DEPTH_LAW = false | TYPE-U |
  would-build: FULL_FINITE_RECORD_TO_SOURCE_BACKGROUND_REFINEMENT_CHANNEL

FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-S

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

---

## 11. Custody

This lane seals this artifact, mirrors the artifact and sidecar, reports the
hashes, and stops. It does not edit the register, governing plan, or tracker,
and performs no git, commit, or push action.
