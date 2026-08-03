# Stage 8 Task 4a Bohm Depth-Dedup and Cocycle-Bridge Adversarial Verification v001

Date: 2026-08-03  
Lane: CODEX LANE 2  
Task: PASTE 410 / Task 4a  
Register head at freeze: Q-327  
Plan head: C41  
Status: **KILLED. THE DEDUP NON-COLLAPSE SURVIVES WITH NARROWED WORDING, BUT THE COCYCLE AND BRIDGE DO NOT. THE SEALED DEPHASING WEIGHT IS A GLOBAL BERNOULLI MIXTURE, NOT A PER-CELL MULTIPLICATIVE WEIGHT; EVERY ACTUAL ZERO-EXTENSION ARROW HAS ZERO INCREMENT; AND NO MAP CARRIES THAT SOURCE WEIGHT TO AN ORIENTED INCIDENCE CYCLE OR A PHYSICAL ACTION. K1–K8 WERE ALL EXECUTED.**

```text
REVIEW_TARGET = BOHM_DEPTH_DEDUP_AND_COCYCLE_BRIDGE_PROPOSAL_V001.md
REVIEW_TARGET_SHA256 = eaeece6ee2664009090c82c5b88cc5205bd3258d2cd4433245340ddae4c19c9f
REVIEW_TARGET_SEAL = PASS

OVERALL_VERDICT = KILLED
PROPOSAL_REGISTRATION_READY = false | TYPE-R

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

---

## 0. Lead kill

The proposal's central phrase, “the sealed per-cell dephasing factor,” names
no sealed object.

The cited finite source result defines one global equal-history weight

```text
w_N(R):=1-p+p exp[-Q_N(R)/2].                       (KV-1)
```

It does not define factors `w_e` indexed by incidence cells. The product in
the same sealed formula is instead the **conditional charged-character
phase**

```text
product_j r_j^n.                                    (KV-2)
```

The Bernoulli mixture `(KV-1)` sits outside that product. Conflating them is
the proposal's fatal error.

Even granting, more strongly than the current live germ warrants, an
additive decomposition

```text
Q_12=Q_1+Q_2,
u_i=exp(-Q_i/2),
w(Q)=1-p+p exp(-Q/2),
```

exact multiplication gives

```text
w(Q_1+Q_2)-w(Q_1)w(Q_2)
  =p(1-p)(1-u_1)(1-u_2).                            (KV-3)
```

For the admitted symbolic family `0<p<1`, `(KV-3)` is generically nonzero.
Therefore

```text
Log w(Q_1+Q_2) != Log w(Q_1)+Log w(Q_2)            (KV-4)
```

on any common logarithm chart, except on special null factors. The sealed
weight is not multiplicative and its logarithm is not the proposed additive
cell cocycle.

The actual inclusion arrows make the failure sharper. Q-279's
zero-extension theorem is

```text
Q_M(iota_NM R)=Q_N(R),
w_M(iota_NM R)=w_N(R).                              (KV-5)
```

Thus the only increment canonically extractable from the sealed global
weights is

```text
Log w_M(iota_NM R)-Log w_N(R)=0                    (KV-6)
```

for **every** sealed inclusion arrow. This is an additive but trivial
cocycle. It carries no accumulated depth and has no nonzero holonomy.

```text
SEALED_PER_CELL_DEPHASING_WEIGHT_EXISTS = false | TYPE-S
SEALED_GLOBAL_DEPHASING_WEIGHT_IS_MULTIPLICATIVE = false | TYPE-R |
  test: equation KV-3
NONTRIVIAL_SEQUENTIAL_ARROW_COCYCLE_FROM_W_EXISTS = false | TYPE-R |
  test: every sealed zero-extension increment is KV-6
```

There are two further independent fatal type errors:

1. the zero-extension category has arrows `N->M`; the physical cycle carrier
   has oriented incidence cycles `c in ker(B_N^T)`. No sealed functor maps an
   incidence traversal to a chain of sequential arrows;
2. the current live germ V007 uses `Q_n^even(R)`, a global trace-dual of the
   rank-one tensor `hbar ell_n tensor ell_n`, not Q-279's superseded C-B
   pairing and not a cell label. Its cycle directions lie in the source
   kernel. The proposal silently uses the overloaded symbol `Q_N` for three
   different objects.

The bridge therefore does not reach `K_cycle`, a physical action, Q-408, or a
physical `p` verdict.

---

## 1. Preflight, custody, currency, and authorities

### 1.1 Preflight

```text
DOES_THE_REVIEW_TARGET_EXIST = true
REVIEW_TARGET_SEAL_VERIFIED = true

IS_THE_VERSION_CURRENT = true |
  register head: Q-327 |
  plan head: C41

ARE_THE_REVIEW_INPUTS_PRESENT = true |
  scope: enough to execute K1-K8 and refute the proposal

DOES_THE_PROPOSED_BRIDGE_EXIST_AFTER_REVIEW = false | TYPE-R |
  test: K2, K3, K6, K7, and the category attack independently kill it
```

### 1.2 Roots entered

```text
ROOTS_ENTERED = (
  /Users/bgm/Documents/New project/gravity_emergence_evidence_program/
    alpha_fundamental_record_action_cleanroom_v003,
  /Users/bgm/MB Work/alpha_supervision,
  /Users/bgm/MB Work/alpha-program-archive/workspace
)

a32_holdout/custodian_private/ = NOT_ENTERED | TYPE-S
```

### 1.3 Frozen authorities

| Authority | SHA-256 | Load-bearing use |
|---|---|---|
| `LOCKED_PROCESS.md` | `f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba` | fences, typing, custody |
| `QUESTIONS_SETTLED_REGISTER_V001.md` | `263090a2955ebc6ccb643b9beb993ef569e2b908a4bb0eca67ba229884b36d10` | Q-327 head at freeze |
| `TASK_LIST_HERE_TO_ALPHA_2026-08-01_V002.md` | `02111630f9f1f1ed84ad4c0790ea7c35726a920994f328957825fb1fd40ce5b3` | C41 commission and DoR-016 reservation |
| `RELAY_PASTE_410_VERIFY_THE_COCYCLE_BRIDGE_V001.md` | `c4baf336f94e83bb8fa3c2940d262e80e377a61697edd01c3584f9d56aec7473` | verification contract |
| `BOHM_DEPTH_DEDUP_AND_COCYCLE_BRIDGE_PROPOSAL_V001.md` | `eaeece6ee2664009090c82c5b88cc5205bd3258d2cd4433245340ddae4c19c9f` | proposal under review and K1-K8 |
| `STAGE8_TASK4A_DIVERGENCE_DETERMINED_TRANSVERSE_CYCLE_ACTION_DRAFT_DETERMINATION_V001.md` | `ed49624b6f5f0bcda94ee88a939a5751113b30d73192b2c28a5aec25829e1797` | Q-327 countermodels and eight-item bridge contract |
| `STAGE8_TASK4A_FINITE_NONZERO_R_REFERENCE_EXACT_PROBE_SOURCE_COMPUTATION_V001.md` | `c7624d88aedaa0659755b5c566121b24c2ad0c29a0060daada43a31b22a6ddfb` | cited closed form, global weight, and zero extension |
| `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V007.md` | `bd33e54c27ddb8ed5224637d7888a071026db33a1a17c7127a27ffa647b69896` | live germ and current `Q_n^even` |
| `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md` | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | physical quotient, cycle currents, oriented phase calculus |
| `STAGE8_TASK4A_RATIFIED_BILOCAL_INVOLUTION_REALITY_LAW_DETERMINATION_V001.md` | `323852e8835175c30d503f0383ef735405d8bc40a98109e09f5974e49c603c22` | source involution law |
| `STAGE8_TASK4A_COMPLEMENT_SCOPED_PHYSICAL_STATIONARY_RESPONSE_PACKAGE_FLAT_FAMILY_DETERMINATION_V001.md` | `30532ecb2c08d21e28af05f1228b9c29264be99731f63c8cf5b30273bb51e7b8` | Q-408 exact dependence formulas and flat-family boundary |

All local cleanroom authorities with sidecars above verified `OK`. The Bohm
proposal's archive sidecar also verified `OK` before its contents were used.

### 1.4 Symbol collisions that decide the review

```text
Q_N as carrier       = U(1)^N in the sequential quotient system;
Q_N(R) in Q-279      = historical quadratic bilocal-probe functional;
Q_n^even(R) in V007 = live trace-dual of hbar ell_n tensor ell_n;
Q in exp(-Q/2)       = an argument of the global dephasing factor;
c in V005            = an oriented integer cycle coefficient in ker(B_N^T);
c_dep                = the proposal's alleged sequential-arrow cocycle;
Phi_c                = V005's oriented cycle phase with d Phi_c=u_c;
phi_div              = the proposal's alleged physical transverse action.
```

No identity among these differently typed objects is supplied by the shared
letter `Q`, the word “cell,” or the word “cycle.”

### 1.5 Acts not performed

```text
cycle representative, basis, orientation, or member selected false | TYPE-S
new logarithm branch selected                         false | TYPE-S
source weight renamed physical action                 false | TYPE-S
cycle-direction inverse used                          false | TYPE-S
private holdout entered                               false | TYPE-S
coupling, alpha, scale, root, or physical value evaluated false | TYPE-S
measured constant compared                            false | TYPE-S
register, plan file, tracker, git, commit, or push performed false | TYPE-S
```

---

## 2. Claim I.1 — depth dedup

The non-collapse survives, but its wording must be narrowed.

| Notion | Type | Relation established |
|---|---|---|
| spectral threshold `x` | scalar parameter in a coefficient-function theorem | no sealed map to the other three |
| sequential stage `N` / carrier `U(1)^N` | directed-system index/object | feeds `T_cyl` functorially; is not `T_cyl` |
| `T_cyl` | character/module completion | completion codomain of the sequential system; proved not a depth-action completion |
| probe `Q_N(R)` / live `Q_n^even(R)` | scalar functional on a bilocal source | zero-extension invariant; not the carrier or stage |

Thus no current sealed identification collapses the four. However “no
identification proofs exist to be had” is stronger than the evidence. The
record proves absence of a current sealed identification, not impossibility
of a future bridge theorem.

```text
DEPTH_DEDUP_COLLAPSE_OCCURS = false | TYPE-R |
  scope: current sealed typings

NO_FUTURE_IDENTIFICATION_PROOF_CAN_EXIST = NO_VERDICT
CLAIM_I_1 = SURVIVES_WITH_NARROWED_SCOPE
```

This surviving census result does not supply the bridge.

---

## 3. Claim II.1 — the proposed location theorem

Q-409 Section 6.1 considers the special ansatz

```text
phi_N(y)=D_N.
```

For that ansatz, compatibility forces `D_M=D_N`. It does **not** imply that
every object-level compatible functional is constant. A nonconstant cylinder
family may satisfy

```text
F_M(iota_NM y)=F_N(y)
```

while depending on the retained coordinates of `y`. Indeed the entire
finite-cylinder/restriction machinery uses such compatible object functions.

Therefore:

```text
STAGE_ONLY_CONSTANT_ACCUMULATION_IS_FORCED_CONSTANT = true

ALL_OBJECT_LEVEL_ACCUMULATION_IS_DEAD_AS_A_CLASS = false | TYPE-R |
  counterexample class: nonconstant compatible cylinder functionals

ACCUMULATION_MUST_LIVE_ON_ARROWS = false | TYPE-R |
  test: the 6.1 premise proves only the stage-only ansatz

CLAIM_II_1 = KILLED_BY_OVERGENERALIZATION
```

Whether a lawful nontrivial accumulation object actually exists remains
`NO_VERDICT`; the refutation concerns the claimed location theorem.

---

## 4. Mandatory K1–K8 execution

### K1 — identity-cell increment

The exact sealed zero-extension equations are Q-279:542-554:

```text
Q_M(iota_NM R)=Q_N(R),
w_M(iota_NM R)=w_N(R).
```

On the anchored common logarithm chart, the global ratio increment is zero.
This passes the numerical-free structural check.

But the sealed text does not factor that equality into individual appended
objects `w(cell)=1`. V007 makes the issue stronger: its current quadratic is
the global tensor `hbar ell tensor ell`; it is not a list of cell weights.

```text
K1_GLOBAL_ZERO_EXTENSION_INCREMENT = PASS
K1_SEALED_PER_CELL_IDENTITY_FACTOR = false | TYPE-U |
  would-build: a local cell factorization of the live source weight
```

### K2 — additivity of the sealed weight

K2 fails exactly by `(KV-3)`. The only sealed product in Q-279:275-285 is
`product_j r_j^n`; `w_N(R)` is a global sector mixture multiplying that
conditional charged term inside a sum with the neutral term.

Defining a sum of chosen local `Log w_e` would be combinatorially additive,
but the local `w_e` are not sealed. Defining the increment from the actual
global weights gives the trivial zero `(KV-6)` on every inclusion arrow.

```text
K2_GLOBAL_W_MULTIPLICATIVE = false | TYPE-R
K2_NONTRIVIAL_ADDITIVE_COCYCLE = false | TYPE-R
K2 = FAIL_FATAL
```

### K3 — descent to the physical cycle carrier

The source weight is invariant under the common source gauge action. That is
not the required cycle descent.

V005 types a physical cycle by an oriented coefficient

```text
c in ker(B_N^T),
u_c([L_N a])=<c,L_N a>,
Phi_c=-i Log_0 product_e h_e^(c_e).
```

The exponent `c_e`, its sign, and the telescoping equation `B_N^T c=0` are
what make `Phi_c` representative-independent. The Bohm formula has none of
these data: it sums an untyped `w(cell)` over “cells traversed.” No map

```text
R or Q_n^even(R) -> incidence edge cochain -> K_cycle
```

is sealed, and no all-finite visibility certificate is supplied.

```text
K3_SOURCE_GAUGE_DESCENT = PASS_WITH_SOURCE_SCOPE
K3_GATE4_CYCLE_DESCENT = false | TYPE-U
K3_VISIBILITY_QUOTIENT_DESCENT = false | TYPE-U
K3_PHI_DIV_WELL_DEFINED_ON_K_CYCLE = false | TYPE-U
K3 = FAIL_FATAL
```

### K4 — reality covariance

At the source level, the ratified law

```text
Q_(-n)(Theta_R R)=conjugate(Q_n(R))
```

and real symbolic `p` imply

```text
w_(-n)(Theta_R R)=conjugate(w_n(R)).
```

On a shared nonzero `Log_0` chart, the local logarithm inherits this
covariance. This is a source-local conditional pass.

It does not certify the proposed cycle functional. V005 sends a cycle to its
orientation reverse. A genuine additive cochain integral uses signed
coefficients and changes sign under reversal. The proposal's unsigned
“cells traversed” sum of a real attenuation is even under reversal. No rule
reconciles that with the oriented cocycle claim, and no global log branch is
declared outside P4's local chart.

```text
K4_SOURCE_LOCAL_LOG_REALITY = PASS_ON_SHARED_LOG0_CHART
K4_ORIENTED_CYCLE_REALITY = false | TYPE-U
K4_GLOBAL_LOG_BRANCH = false | TYPE-U
K4 = FAIL_AT_PHYSICAL_CYCLE_LEVEL
```

### K5 — flat-family membership

Let

```text
F_p(Q):=Log_0[1-p+p exp(-Q/2)],
omega(Q):=p exp(-Q/2)/[1-p+p exp(-Q/2)].
```

Exact differentiation gives

```text
F_p'(Q)=-(1/2)omega(Q),
F_p''(Q)=(1/4)omega(Q)[1-omega(Q)],
F_p'(0)=-p/2.                                      (KV-7)
```

Thus under the proposal's direct identification of `Q` with a transverse
normal coordinate, the candidate has a nonzero finite-order jet and is not
in `Flat(S)`. Under the actual source-kernel relation used by Q-308/Q-408,
the physical cycle direction is killed by `ell`, so the live
`Q_n^even=hbar ell tensor ell` gives `Q_n^even=0` on that direction and the
candidate is identically zero there. A third possibility requires the
missing source-to-cycle/action map.

```text
K5_DIRECT_Q_CANDIDATE_IS_ALL_ORDERS_FLAT = false | TYPE-R |
  test: KV-7
K5_LIVE_KERNEL_PULLBACK_IS_NONZERO = false | TYPE-R |
  test: cycle direction lies in ker ell
K5_PHYSICAL_ACTION_MEMBERSHIP = NO_VERDICT |
  missing: physical action comparison map
K5 = FAIL
```

### K6 — eight-item bridge-package checklist

| Q-409 item | Proposal's candidate | Verification |
|---|---|---|
| 1. `DivergenceDatum` | `Log w` | **FAIL:** finite source attenuation; no divergence/growth datum |
| 2. `DepthMap` | “appended cells” | **FAIL:** zero-extension index is not incidence depth; all actual increments vanish |
| 3. `CycleMap` | “evaluate around the cycle” | **FAIL:** no functor/cochain map from sequential arrows or bilocal `R` to `K_cycle` |
| 4. `AccumulationRule` | sum of local logs | **FAIL:** local weights absent; global weight nonmultiplicative; topology/normalization absent |
| 5. `ActionComparisonSquare` | claimed arrow evasion | **FAIL:** an arrow cocycle is not a physical action value; Q-324 square still absent |
| 6. generator/uniqueness | `Log` declaration | **FAIL:** log, local decomposition, traversal, and normalization are unforced choices |
| 7. form certificates | K3-K5 | **FAIL:** cycle descent absent; flatness fails or becomes trivial; global reality/log unresolved |
| 8. provenance | “sealed dephasing data” | **FAIL:** no common-origin descent from source weight through depth to physical cycle action |

```text
K6_PASS_COUNT = 0
K6_FAIL_COUNT = 8
K6 = FAIL_FATAL
```

### K7 — relabeling and target tuning

The proposal relabels two missing maps as one phrase:

```text
sequential inclusion arrows -> “cells” -> incidence-cycle traversal.
```

Those arrows live in different categories. The identification is precisely
Q-409's missing `DepthMap` plus `CycleMap`, not a derived fact.

The use of `Log` is also not forced. A logarithm converts products to sums,
but K2 proves that the sealed `w` does not form the required product. Once
that premise fails, many functions `g(w)` with `g(1)=0` satisfy the identity
normalization, and no sealed criterion selects `Log`. The proposal itself
justifies the choice by the desired “log divergence is the coupling” and
Wilson-loop consequences at lines 55-59. That is consequence-driven.

```text
K7_RELABELING_CLEAN = false | TYPE-R
K7_TARGET_TUNING_CLEAN = false | TYPE-R
K7_HIDDEN_CHOICE_COUNT_AT_LEAST = 4 |
  choices: local cell factorization, logarithm/branch, incidence traversal
           map, action normalization
K7 = FAIL_FATAL
```

### K8 — Q-408 consequences

If, hypothetically, cell functions `Q_e(C,K)` and one common log chart were
supplied, the exact formal derivative would be

```text
D_C D_K phi_div
 =sum_e {
    F_p''(Q_e) D_C Q_e tensor D_K Q_e
    +F_p'(Q_e) D_C D_K Q_e
  },                                                  (KV-8)

delta G_K[delta phi_div]
 =-H_CC^(-1)D_C(delta phi_div).                       (KV-9)
```

Equations `(KV-7)` give the symbolic coefficients. But the `Q_e` maps,
physical action carrier, stationary locus, and `H_CC` instance do not exist.
The derivatives cannot be evaluated as physical operations, and no
`Pi_R,ind` or `p` trace follows.

```text
K8_FORMAL_INTERFACE_FORMULAS = derived_conditionally
K8_PHYSICAL_DELTA_M_COMPUTED = false | TYPE-C |
  constraint: Q_e/cycle/action map and physical stationary blocks absent
K8_PHYSICAL_DELTA_G_K_COMPUTED = false | TYPE-C |
  constraint: physical action, stationary locus, and H_CC absent
K8_P_TRACE_EXECUTED = false | TYPE-U
K8 = FAIL
```

---

## 5. Additional attacks

### 5.1 The 6.1-square evasion fails

An arrow cocycle is not automatically an object-level action. To integrate a
1-cocycle into object potentials requires a base object/trivialization and
gives

```text
phi_M(iota_NM y)-phi_N(y)=c_dep(iota_NM).           (KV-10)
```

The strict physical action restriction square requires the left side to be
zero, unless an independently certified additive-counterterm quotient says
otherwise. No such quotient exists. For the actual sealed arrows, `(KV-6)`
makes `(KV-10)` trivial and supplies no accumulation. For nonzero increments,
the square is violated rather than evaded.

```text
ARROW_COCYCLE_AUTOMATICALLY_PASSES_ACTION_SQUARE = false | TYPE-R
SEALED_NONTRIVIAL_COUNTERTERM_QUOTIENT_EXISTS = false | TYPE-S
```

### 5.2 Category and holonomy mismatch

The sequential category is the thin directed poset of stages `N<=M`. It has
no nontrivial directed loops. An incidence cycle is a closed integer chain in
`ker(B_N^T)` at one finite stage. Evaluating a sequential-arrow cocycle
“around” an incidence cycle requires a functor from incidence paths to the
sequential category and an orientation-bearing cochain pullback. Neither is
defined. On the thin stage category, any loop is an identity and the sealed
cocycle value is zero.

```text
SEQUENTIAL_ARROW_COCYCLE_HAS_INCIDENCE_HOLONOMY = false | TYPE-R |
  test: different categories and no connecting functor
```

### 5.3 The overloaded-`Q_N` and current-version defect

The proposal cites Q-279's `Q_N(R)` while its arrow carrier uses
`Q_N=U(1)^N`. These are explicitly distinct in the proposal's own Part I.
It then treats the scalar functional as a cell label, contradicting that
dedup.

Moreover, the live V007 germ uses `Q_n^even(R)`. V006's version accounting
states that Q-279's historical C-B-dependent nonzero-`R` rows are
scope-superseded; only its J-only and `R=0` rows are reproduced exactly.
The proposal did not report this version difference.

```text
PROPOSAL_USES_RIGHT_Q_OBJECT = false | TYPE-R
PROPOSAL_REPORTS_LIVE_PAIRING_VERSION = false | TYPE-R
```

### 5.4 Representative, orientation, and selection

V005 deliberately avoids a selected cycle basis. Physical phases use the
complete family of signed coefficients `c_e` and a local `Log_0` chart.
The Bohm formula neither weights by `c_e` nor states how repeated, reversed,
or homologously represented traversals act. An unsigned traversal sum is
orientation-even; an additive cochain integral is orientation-odd. Choosing a
representative traversal would reintroduce the selection V005 excludes.

```text
PHI_DIV_REPRESENTATIVE_INDEPENDENT = false | TYPE-U
PHI_DIV_ORIENTATION_COMPATIBLE = false | TYPE-U
HIDDEN_CYCLE_TRAVERSAL_SELECTION = present_in_definition | TYPE-R
```

### 5.5 Nonlinearity and “scalar functional” ambiguity

`Log w` is nonlinear in the quadratic bilocal source. A scalar-valued map
need not be linear to be an action, but a 1-cocycle/cochain pairing on the
cycle group must state its group law and orientation behavior. The proposal
uses “scalar functional,” “cocycle,” and “holonomy” as if they supplied one
another's missing axioms. They do not.

```text
NONLINEAR_ACTION_FUNCTIONAL_FROM_LOG_W = NO_VERDICT
ADDITIVE_CYCLE_GROUP_COCYCLE_FROM_LOG_W = false | TYPE-R
```

---

## 6. K1–K8 summary

| Test | Verdict | Decisive reason |
|---|---|---|
| K1 | **limited pass / per-cell claim `TYPE-U`** | global zero-extension ratio is one; no cell factor exists |
| K2 | **FAIL — fatal** | exact Bernoulli mixture defect `(KV-3)`; actual arrow cocycle is zero |
| K3 | **FAIL — fatal** | no source/bilocal-to-oriented-cycle descent |
| K4 | **source-local pass; physical FAIL** | local involution covariance does not supply oriented cycle covariance or global log |
| K5 | **FAIL** | direct candidate has nonzero finite jet; live kernel pullback is trivial; physical map absent |
| K6 | **FAIL 8/8** | none of the bridge-package items is completed |
| K7 | **FAIL — fatal** | category relabeling plus unforced, consequence-driven choices |
| K8 | **FAIL** | only conditional formulas; physical maps/blocks absent |

```text
MANDATORY_KILL_LIST_EXECUTED = K1,K2,K3,K4,K5,K6,K7,K8
MANDATORY_KILL_LIST_COMPLETE = true
```

---

## 7. What survives and what does not

### 7.1 Survives

```text
CURRENT_SEALED_DEPTH_NOTIONS_DO_NOT_DEDUP = true | TYPE-R |
  scope: no current sealed identity collapses them

STAGE_ONLY_CONSTANT_ANSATZ_CANNOT_ACCUMULATE = true

GLOBAL_DEPHASING_WEIGHT_IS_ZERO_EXTENSION_INVARIANT = true | TYPE-P |
  premises: Q-279 historical source scope

SOURCE_LOCAL_LOG_REALITY_CAN_HOLD = true | TYPE-P |
  premises: one shared nonzero Log_0 chart and ratified involution
```

### 7.2 Killed

```text
OBJECT_LEVEL_ACCUMULATION_DEAD_AS_A_CLASS = false | TYPE-R
ACCUMULATION_MUST_LIVE_ON_SEQUENTIAL_ARROWS = false | TYPE-R
SEALED_PER_CELL_DEPHASING_FACTOR_EXISTS = false | TYPE-S
SEALED_W_DEFINES_NONTRIVIAL_ARROW_COCYCLE = false | TYPE-R
ARROW_COCYCLE_HAS_INCIDENCE_CYCLE_HOLONOMY = false | TYPE-R
PHI_DIV_IS_SCALAR_ACTION_ON_K_CYCLE = false | TYPE-U
PHI_DIV_RESTRICTION_COMPATIBLE_AUTOMATICALLY = false | TYPE-R
PHI_DIV_CONSTRUCTED_FROM_SEALED_DATA = false | TYPE-U
```

### 7.3 Not executed

```text
DIVERGENCE_DRAFT_RERUN_WITH_CONSTRUCTED_PHI_DIV = false | TYPE-S
Q408_PHYSICAL_CONSEQUENCES_EXECUTED = false | TYPE-U
PI_R_IND_FROM_PHI_DIV_EXISTS = false | TYPE-U
P_APPEARS_IN_DIVERGENCE_DETERMINED_PHYSICAL_RESPONSE = NO_VERDICT
P_CANCELS_FROM_DIVERGENCE_DETERMINED_PHYSICAL_RESPONSE = NO_VERDICT
```

---

## 8. Six-account and door ledger

| Operation | Kernel/applicability | Image | Sector transfer | Restriction square | Tail action | Verdict |
|---|---|---|---|---|---|---|
| global source weight `w_N` | local nonzero source chart | scalar source function | none to incidence | exact zero-extension invariance | no response tail | **PASS / source scope** |
| alleged local factorization | no `w_e` objects | none | source to cells absent | none | none | **TYPE-U / kills K2** |
| sequential-arrow difference | sealed inclusions only | zero cocycle | none | strict square passes trivially | none | **derived zero; no accumulation** |
| incidence-cycle holonomy | needs cochain/functor and signed traversal | none | sequential arrows to cycle absent | no quotient square | `Tail_R` not reached | **TYPE-U / TYPE-R claim** |
| physical action formation | needs Q-409 items 1-8 | none | cycle to action absent | Q-324 square absent | `Tail_R` `NO_VERDICT` | **TYPE-U** |
| Q-408 response | needs physical phi, locus, blocks, `H_CC` | none | routes uninstantiated | physical restrictions absent | `Tail_R` `NO_VERDICT` | **TYPE-U / TYPE-C checks** |

Door flags:

```text
DOOR_GLOBAL_LOG = LOCAL_ONLY |
  domain: anchored nonzero Log_0 chart |
  global branch: TYPE-U

DOOR_CELL_FACTORIZATION = NOT_OPENED | TYPE-U
DOOR_SEQUENTIAL_TO_INCIDENCE_FUNCTOR = NOT_OPENED | TYPE-U
DOOR_CYCLE_QUOTIENT = NOT_OPENED | TYPE-U
DOOR_PHYSICAL_ACTION_COMPARISON = NOT_OPENED | TYPE-U
DOOR_STATIONARY_RESPONSE = NOT_OPENED | TYPE-U

DOOR_WEAK_STAR_USED = false | TYPE-S
DOOR_BIDUAL_USED = false | TYPE-S
DOOR_DISTRIBUTIONAL_COMPLETION_USED = false | TYPE-S
DOOR_NEW_MEASURE_USED = false | TYPE-S
DOOR_NEW_CONTOUR_USED = false | TYPE-S
DOOR_NEW_BOUNDARY_RULE_USED = false | TYPE-S
DOOR_CYCLE_INVERSE_USED = false | TYPE-S
C40_VOID_CLAUSE_FIRED = false | TYPE-S
```

---

## 9. Repair assessment

Repair-by-removal preserves only:

1. the four-way current sealed non-dedup, with the future-impossibility phrase
   removed;
2. the special theorem that a stage-only constant ansatz cannot accumulate;
3. the global source weight's zero-extension invariance and local reality.

Removing the nonexistent per-cell factor, the sequential/incidence
relabeling, the unforced logarithm, and the unsigned traversal removes the
entire bridge. No bounded textual repair leaves Claim II.2 or III.1 intact.
A successor needs the same eight-item package Q-409 already named; this
proposal supplies none of it.

```text
REPAIR_BY_REMOVAL_PRESERVES_BRIDGE = false | TYPE-R
SUCCESSOR_MINIMUM = DIVERGENCE_TO_CYCLE_ACTION_BRIDGE_ITEMS_1_THROUGH_8
DoR_016 = RESERVED
```

---

## 10. Final verdict

```text
CLAIM_I_1_DEPTH_NONDEDUP = SURVIVES_WITH_NARROWED_SCOPE
CLAIM_II_1_OBJECT_LOCATION_THEOREM = KILLED
CLAIM_II_2_NONTRIVIAL_ARROW_COCYCLE = KILLED
CLAIM_III_1_COCYCLE_HOLONOMY_BRIDGE = KILLED

PROPOSAL_VERDICT = KILLED
PROPOSAL_REGISTRATION_READY = false | TYPE-R

PHI_DIV_CONSTRUCTED = false | TYPE-U
DIVERGENCE_TO_CYCLE_ACTION_BRIDGE_EXISTS = false | TYPE-U
Q408_CONSEQUENCE_CHAIN_EXECUTED = false | TYPE-U
PHYSICAL_P_VERDICT = NO_VERDICT

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

