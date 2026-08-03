# Stage 8 Task 4a Network-Sourcing Law Adoption Proposal — Codex Lane 2 V002

**PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL RATIFICATION (DoR-016/017 RESERVED)**

Date: 2026-08-03  
Task: PASTE 420 / Task 4a / bounded repair of the authored network-sourcing law  
Lane: CODEX LANE 2  
Register head: Q-337  
Custody: builder repairing its own V001; Lane 1 re-review required  

```text
NETWORK_SOURCING_LAW_V002 = PROPOSED_NOT_ADOPTED
V001_DISPOSITION = KILLED_BY_R7; INDEPENDENTLY_R3_AND_R8
REPAIR_SCOPE = PORT_TYPING_PLUS_STANDING_ONLY

BRANCH_A = CYCLE_CONSTRAINED_SCALAR_EMISSION
BRANCH_B = ENDPOINT_COVARIANT_ACCESS_EMISSION
BRANCH_SELECTED = false | TYPE-S | scope: this two-branch proposal

V001_R1_R2_R4_R5_R6_SEAMS_PRESERVED = true | PASS_WITHIN_PROPOSAL
V001_R3_R7_R8_CLAIMS_INHERITED = false | TYPE-R |
  test: the review's R3/R7/R8 counterexamples bind

AUTONOMOUS_READY_NETWORK_NO_IGNITION = NO_VERDICT / TYPE-U
ONE_TIER_DELAY = AUTHORED_NOT_UNIQUELY_FORCED

TYPE_P_CLAIMS_IN_THIS_PROPOSAL = 0
RANK_PAIR_SELECTED = false | TYPE-S | scope: every displayed formula
RANK_RATIO_EVALUATED = false | TYPE-S | scope: every displayed formula

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

---

## 0. Lead repair

DoR-015 forces a genuine binary typing fork. A scalar physical source must be
a conserved cycle coefficient

```text
q_N in ker(B_N^T),
```

whereas an open path is endpoint-covariant charge/flux transport and is never
a bare scalar coordinate. V001 conflated those objects. V002 retains both
lawful repairs and selects neither:

1. **Branch A** keeps V001's scalar V007 receiver only on the history subdomain
   whose emitted coefficient already lies in `ker(B_N^T)`. It does not project
   generic open-path data. Scalar emission is exactly zero on connected trees;
   the first nonzero two-system carrier is a directed two-edge cycle.
2. **Branch B** keeps generic open-path history, but emits its full
   endpoint-covariant transport to the ratified C5 charge/flux-access receiver.
   It never calls that object a V007 scalar source. The exact access-side phase
   tower survives; V001's scalar `x`, rank-one `R`, and quadratic exponent do
   not survive this typing without a new receiver map.

Both branches retain the same base-case statement at identity history. Neither
branch contains the missing received-port-to-write-history update, so neither
proves autonomous no ignition or autonomous ignition.

```text
LEAD_REPAIR_STATUS = TWO_NONSELECTED_PROPOSAL_BRANCHES
SCALAR_OPEN_PATH_IDENTIFICATION_RETAINED = false | TYPE-R |
  test: R7 one-edge counterexample
CANONICAL_CYCLE_PROJECTOR_CLAIMED = false | TYPE-S |
  scope: Branch-A formulas
ENDPOINT_TRANSPORT_SCALARIZED = false | TYPE-S |
  scope: Branch-B formulas
```

---

## 1. Preflight, seal verification, and bounded authorities

### 1.1 Preflight

```text
DOES_THE_OBJECT_EXIST = yes_partly |
  V001 and its sealed cross-review exist; V002 did not

IS_THE_VERSION_CURRENT = yes_through_Q337

ARE_ITS_INPUTS_PRESENT = yes |
  V001, the cross-review, DoR-009, DoR-014 plus amendments and V007,
  DoR-015/V005, and Q-335 through Q-337

PREFLIGHT = PASS
```

The supplied Lane-1 review was hashed **before** substantive reading:

```text
REVIEW_ARTIFACT =
  STAGE8_TASK4A_NETWORK_SOURCING_LAW_CROSS_REVIEW_LANE1_V001.md
EXPECTED_SHA256 =
  e937869879b4613175c814c6b5a02eabc54607c1f9751a4e758d475ced6de21b
VERIFIED_SHA256 =
  e937869879b4613175c814c6b5a02eabc54607c1f9751a4e758d475ced6de21b
REVIEW_SIDECAR_CHECK = PASS
```

The review was then read in full. Its R7 one-edge counterexample is reproduced
as a permanent regression test in Section 4.5. Its R3/R8 correction is adopted
verbatim in Section 8.

### 1.2 Frozen authorities

| Authority | SHA-256 / standing | Use |
|---|---|---|
| `LOCKED_PROCESS.md` | `f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba` | custody, types, act-based fences |
| V001 proposal | `87f696261651567e04242abc1a54d5a2b457a19e07926e9e9856b02dc1719eb1` | repair base; R1/R2/R4/R5/R6 formulas |
| V001 cross-review | `e937869879b4613175c814c6b5a02eabc54607c1f9751a4e758d475ced6de21b` | R3/R7/R8 kills and repair fork |
| DoR-009 | `11632fa30dfe9225c228f07a3be4717c73bdfc9e38b0c76c46d905d3fe193bc5` | C1-C8, `E_post`, charged-write receiver |
| source germ V007 | `bd33e54c27ddb8ed5224637d7888a071026db33a1a17c7127a27ffa647b69896` | live scalar `L`, rank-one `Q`, `Xi`, `Z` |
| DoR-015 | `617bd51a70860d2cfb2066640630ba37ec289d56255ebbe1433bc0dfcba0159d` | physical source/transport fork |
| FIELD_SIGNATURE_PHYS V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | `ker(B_N^T)`, tree theorem, endpoint torsors |
| Q-335 artifact | `e73a3716aa8141bbbb501ae24138050f27f1eca7b66dde05fee25334d6db67e7` | C5 receiver-only chart; no network `R` datum |
| Q-336 | superseded where Q-337 says | V001 receipt only; no-ignition standing not inherited |
| Q-337 | live register head | binding correction and binary repair |

DoR-015 states that `u_c`, `c in ker(B^T)`, are the physical response
family and that open-path content is endpoint-covariant transport, never a
scalar coordinate (`DECISION_OF_RECORD_015...:5-24`). V005 proves the
basis-free duality and the connected-tree consequence
(`STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md:83-124,268-276,
286-327,451-464`).

### 1.3 Scope and custody

No register, plan, tracker, git, commit, or push action is performed. The
fenced holdout was not opened, listed, or searched. This lane does not
self-certify V002; it seals, mirrors, reports, and stops for Lane-1 re-review.

---

## 2. Shared V001 core retained by both branches

**PROPOSED_NOT_ADOPTED — PASS_WITHIN_PROPOSAL ONLY**

For a doubled compact history `h_a`, retain the zero-anchored relative
character and its local additive chart:

```text
u_(a,n)[h_a]_j
  :=conjugate(z_(a,-,j)^n) z_(a,+,j)^n,

eta_(a,n)[h_a]_j:=Log_0(u_(a,n)[h_a]_j).            (NS2-1)
```

The chart is restricted to the common connected `Log_0` domain with
`eta in ell^1`. It obeys, proposal-relatively,

```text
eta[identity]=0,
eta[equal CTP histories]=0,
eta_(-n)[Theta h]=conjugate(eta_n[h]),
rho_N eta_M=eta_N rho_N for N<=M.                   (NS2-2)
```

Retain matched-carrier transport `tau_(ba)` and the receiver-oriented
candidate coordinate

```text
q^0_(a->b)[h_a]
  :=(i n_b)^(-1) tau_(ba) eta_(a,n_a)[h_a].         (NS2-3)
```

`q^0` is only a **candidate emission coordinate**. V002 never declares a
generic `q^0` to be a scalar physical source. Branch A restricts it to the
cycle kernel; Branch B retains its underlying transport before scalarization.

The shared temporal rule is only:

```text
t:    execute the E_post write and retain the untraced history;
t:    evaluate the chosen branch emitter;
t+d:  deliver to the neighbor, for an authored integer d>=1.       (NS2-4)
```

No-post-output supplementation forces `d>0`; it does **not** force `d=1`.
V002 displays the minimal authored representative `d=1` when recomputing the
tower, while retaining the positive-integer delay family in the choice table.

```text
POSITIVE_DELAY_REQUIRED = true | inherited constraint
EXACT_ONE_TIER_DELAY_DERIVED = false | TYPE-R |
  counterfamily: every fixed authored integer delay d>=1 obeys the timing constraints
EXACT_ONE_TIER_DELAY = AUTHORED_NOT_UNIQUELY_FORCED
```

---

## 3. V002 choice table — one fork, neither branch selected

**PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL RATIFICATION**

| Row | Proposed content | Live alternatives | What it adds | Void condition |
|---|---|---|---|---|
| `H` shared | V001's zero-anchored relative-character `Log_0` chart | `u-1`; other branch; arbitrary history function | exact local history coordinate | finite C5 character, reality, or restriction fails |
| `A-J` | Admit only histories for which the whole emitted coefficient `q^0_N` lies in `ker(B_N^T)`; use it unchanged as the scalar difference source | an unratified projector; selected cycle basis; zero source | conserved scalar emission with exact character unchanged | any emitted scalar has nonzero boundary, or C5 closed-cycle character changes |
| `A-R` | Symmetric rank-one bilocal over the admitted cycle source | zero `R`; nonunit weight; general kernel | lowest-rank V007 bilocal on the corrected base carrier | base source leaves `J_phys`, trace class fails, or V007 formula fails |
| `B-T` | Emit the full endpoint-covariant open-path transport with its source/target endpoint objects to C5's charge/flux-access side | bare scalar; selected endpoint frame; closed-cycle-only source | lawful generic open-path emission | endpoint covariance, C5 access, or no-selection fails |
| `B-R` | No network `R` receiver is proposed | scalarized rank-one `R`; arbitrary transport bilocal | an explicit door rather than a hidden port | any `R` output is consumed without a ratified receiver |
| `N` shared | Reciprocal matched two-node delivery after authored delay `d>=1`; examples use `d=1` | any positive integer delay; larger graph; self-edge | temporal incidence only | retroaction, E_post reversal, hidden edge/member selection |

This is a two-member proposal family, not one indivisible physics selection.
Branch A and Branch B are mutually exclusive typings of the emitted object.
Nothing in their downstream behavior is used to choose between them.

```text
PROPOSAL_BRANCH_COUNT = 2
BRANCH_FAMILY = {A_cycle_scalar, B_endpoint_transport}
BRANCH_SELECTION = NONE | TYPE-S | scope: choice table and all computations
R_NORMALIZATION_DERIVED_FROM_C5 = false | TYPE-R | test: Q-335 C5 audit
ENDPOINT_FRAME_SELECTED = false | TYPE-S | scope: Branch B
CYCLE_BASIS_SELECTED = false | TYPE-S | scope: Branch A
```

---

## 4. Branch A — cycle-constrained scalar emission

**PROPOSED_NOT_ADOPTED — BRANCH A PASS_WITHIN_PROPOSAL**

### 4.1 Why restriction, not projection

For a finite realized stage with incidence operator

```text
(B_N theta)_e=theta_t-theta_s,
```

DoR-015 fixes the physical scalar dual to `ker(B_N^T)`. It does not ratify an
inner product, splitting, cycle basis, or projector

```text
P_cyc:E_N -> ker(B_N^T).
```

Moreover, replacing `q^0` by a nontrivial projection generally changes

```text
exp(i n_b sum_e q_e),
```

and therefore can break the exact C5 character equation that passed R1. A
projection would be a new authored field, not a consequence of DoR-015.

V002 instead uses the forced domain restriction:

```text
Hist_emit,A,N^(a->b)
  :={h in Hist_emit,N^(a): B_N^T q^0_(a->b)[h]=0},

q^A_(a->b)[h]:=q^0_(a->b)[h]
  for h in Hist_emit,A,N^(a->b).                    (NS2-A1)
```

Equivalently, `q^A` is the restriction/corestriction of `q^0` through the
canonical inclusion `ker(B_N^T) -> R^(E_N)`. No map is defined on rejected
open-path histories. This is the least repair that both honors DoR-015 and
leaves V001's exact local character untouched.

There is one forced total-map exception: when `ker(B_N^T)={0}`, the scalar
codomain itself is the zero space, so the unique scalar emission on **every**
history is the zero map. Any nontrivial open-path content remains available
only to Branch B. This is not a chosen orthogonal projection; there is only
one map into the zero object.

The scalar and bilocal emissions are then

```text
d_J^A[h]:=T_(CTP,J)^(-1)(0,q^A[h]),
v^A[h]:=K_J(d_J^A[h])=iota_delta q^A[h],
d_R^A[h]:=v^A[h] symtensor v^A[h].                  (NS2-A2)
```

The `R` row remains authored exactly as in V001. Its port type is repaired
because its base vector is now in the DoR-015 scalar source domain.

### 4.2 Connected-tree zero theorem

Let `G_N` be a connected finite directed graph with `V` vertices and `E`
edges. Its incidence matrix has rank `V-1`. Rank-nullity for
`B_N^T:R^E->R^V` gives

```text
dim ker(B_N^T)=E-(V-1)=E-V+1.                       (NS2-A3)
```

For a connected tree, `E=V-1`; hence

```text
ker(B_N^T)={0}.
```

Therefore `(NS2-A1)` forces

```text
q^A=0,
d_J^A=0,
d_R^A=0                                             (NS2-A4)
```

on every connected tree stage.

**Two systems joined by open paths alone exchange no scalar drive.** This is
a theorem of Branch A from DoR-015's kernel, not a claim that the same open
paths carry no charge/flux access; that access belongs to Branch B.

### 4.3 Minimal driving stage

For two vertices, a connected one-edge graph has `E-V+1=0`. To obtain a
nonzero scalar cycle without adding a third system, at least two edges are
required. Take the reciprocal directed multigraph

```text
e_12:1->2,
e_21:2->1,

B_2=[[-1, 1],
     [ 1,-1]].                                      (NS2-A5)
```

Then

```text
B_2^T(q_12,q_21)^T
  =(-q_12+q_21, q_12-q_21)^T,

ker(B_2^T)={s(1,1):s in R}.                         (NS2-A6)
```

Thus the reciprocal two-edge loop is the minimal two-system scalar-driving
stage in the directed multigraph class. If parallel/oppositely directed
edges are forbidden and the network must be simple, no two-vertex cycle
exists; the minimal simple carrier is a three-vertex triangle. These are two
graph categories, not two physics selections.

No cycle orientation is selected physically. `(1,1)` is a calculation
representative for the displayed edge orientations; reversing an edge sends
both its incidence row and coefficient sign together, leaving the contraction
and kernel class unchanged.

### 4.4 Exact NS-17–NS-26 recomputation on the minimal cycle

Let the reciprocal histories satisfy the Branch-A admissibility equation

```text
q^0_12=q^0_21=s_t,
q^A_t=s_t c_2,
c_2=(1,1).                                          (NS2-A7)
```

Let system `i` retain its symbolic origin weight

```text
p_i=r_(ch,i)/(r_(0,i)+r_(ch,i)),                    (NS2-A8)
```

with no rank selected and no ratio evaluated. The exact scalar consumed by
the V007 receiver is the invariant contraction

```text
x_(i,t):=ell_(i,n_i)(iota_delta q^A_t).
```

On the matched local C5 chart used by V001,

```text
x_(i,t)=i n_i sum_(e in {12,21}) q^A_(t,e)
       =2 i n_i s_t.                                (NS2-A9)
```

The displayed formula is orientation-covariant: reorienting an edge changes
the coordinate and receiver covector together. It is not a selected cycle
orientation.

V007's exact rank-one formula now applies on the corrected scalar carrier:

```text
Q_i^even(d_R^A[t])=hbar x_(i,t)^2,

Xi_(i,t)=x_(i,t)-(hbar/2)x_(i,t)^2
         =2 i n_i s_t+2 hbar s_t^2,                 (NS2-A10)

S_(i,k)=sum_(t=1)^k Xi_(i,t),
D_(i,k)=(hbar/2)sum_(t=1)^k x_(i,t)^2,

A_(i,k)=(1-p_i)+p_i exp(S_(i,k)).                   (NS2-A11)
```

No reality or positivity is inferred from the algebraic sign of the local
chart representative. The invariant statement is the first line of
`(NS2-A10)` and the symbolic contraction in `(NS2-A9)`.

For repeated admitted cycle history `s_t=s`,

```text
Xi_i=2 i n_i s+2 hbar s^2,
S_(i,k)=k Xi_i,
D_(i,k)=k(hbar/2)(2 i n_i s)^2,

A_(i,k)=(1-p_i)+p_i exp(k[2 i n_i s+2 hbar s^2]).  (NS2-A12)
```

More generally, `(NS2-A11)` is exact for the actual admitted history
sequence. Multiplying the two system amplitudes remains unlicensed without a
joint state/effect contraction, as in V001.

The result is the repaired meaning of NS-17–NS-26: `x`, `Xi`, and `A_k`
remain defined, but only on the cycle-constrained history subdomain. The
one-edge and general-tree formulas collapse to their zero values by
`(NS2-A4)`.

### 4.5 Permanent R7 one-edge regression

Use the review's exact one-edge stage

```text
B_1=[-1,1],
u_e=exp(i epsilon),
eta_e=i epsilon,
q^0_e=(i)^(-1)eta_e=epsilon !=0.                    (NS2-A13)
```

Then

```text
B_1^T q^0=(-epsilon,epsilon)^T !=0.
```

The history is rejected by `Hist_emit,A,1`, and the only admitted Branch-A
scalar on this stage is

```text
q^A=0,
d_J^A=0,
d_R^A=0,
x=Xi=0,
A_1=1.                                              (NS2-A14)
```

No projection of `epsilon` is reported as physical. This test will kill any
successor that again emits a nonzero one-edge scalar.

```text
R7_ONE_EDGE_SCALAR_EMISSION = ZERO | PASS_WITHIN_PROPOSAL
CONNECTED_TREE_SCALAR_EMISSION = ZERO | PASS_WITHIN_PROPOSAL
MINIMAL_TWO_SYSTEM_SCALAR_CYCLE = TWO_RECIPROCAL_EDGES
```

---

## 5. Branch B — endpoint-covariant emission

**PROPOSED_NOT_ADOPTED — BRANCH B PASS_WITHIN_PROPOSAL**

### 5.1 Emission object and covariance

Let `E_e^s` and `E_e^t` be the source and target endpoint fibers retained by
DoR-015's full endpoint torsor/intertwiner family. The relative compact
history on an oriented open edge defines a transport morphism

```text
mathcal T_(a->b,e)[h_a]:E_e^s -> E_e^t,             (NS2-B1)
```

with the endpoint law

```text
mathcal T_e[g.h]=g_t mathcal T_e[h] g_s^(-1).       (NS2-B2)
```

The Branch-B emitter is the full covariant tuple, not its frame coordinate:

```text
d_acc^B[h_a]
  :=(E_e^s,E_e^t,mathcal T_(a->b,e)[h_a])_(e in path),

d_acc^B[h_a] in Trans_ep(a,b).                      (NS2-B3)
```

It is delivered to the neighbor's C5 charge/flux-access side after the
authored positive delay. No endpoint frame, torsor member, logarithm branch,
or scalar contraction is selected. Common endpoint changes act covariantly,
not invariantly.

```text
BRANCH_B_OUTPUT_TYPE = ENDPOINT_COVARIANT_TRANSPORT
BRANCH_B_OUTPUT_CALLED_SCALAR_SOURCE = false | TYPE-S |
  scope: all Branch-B signatures
BRANCH_B_ENDPOINT_MEMBER_SELECTED = false | TYPE-S |
  scope: full torsor/intertwiner family retained
```

### 5.2 Receiving end and the C5 seam

DoR-009/C5 is a ratified receiver for an external compact history acting on
the charged write. DoR-015 identifies exactly this open-path object as the
required charge/flux-access side. Thus Branch B has a receiver:

```text
Trans_ep(a,b)
  -> C5 external-history input
  -> endpoint-covariant charged-write modification.                (NS2-B4)
```

What does **not** survive is V001's global claim

```text
d_J^B:Trans_ep(a,b)->E_J,b.
```

The R1 equality

```text
exp(i n_b sum q)=product u_e
```

still holds after choosing a common local endpoint chart, and it remains a
correct check on a presentation of `(NS2-B4)`. It is not a descended scalar
source map. Globally, an open-edge character is endpoint-covariant; only a
closed-cycle product or contraction with matching endpoint data is scalar.

Therefore:

```text
C5_ACCESS_RECEIVER_FOR_BRANCH_B = EXISTS | PASS_WITHIN_PROPOSAL
V001_LOCAL_CHARACTER_SEAM = SURVIVES_AS_ACCESS_CHART_CHECK
V007_SCALAR_d_J_SEAM = DOES_NOT_SURVIVE_GLOBALLY | TYPE-R |
  counterexample: the R7 one-edge endpoint transformation

NETWORK_R_RECEIVER_ON_ACCESS_SIDE = NOT_FOUND / TYPE-U |
  missing: ratified endpoint-covariant bilocal receiver and its finite formula
```

This is a door, not a defect papered over with V001's scalar rank-one `R`.

### 5.3 Exact surviving tower

For tier `t`, let the charged character of the received endpoint-covariant
transport, evaluated by C5 with its matching endpoint data, be

```text
zeta_(i,t):=chi_(n_i)(mathcal T_(neighbor->i,t)),
|zeta_(i,t)|=1.                                     (NS2-B5)
```

`zeta` is not a bare gauge-invariant open-edge scalar; the notation denotes
the covariant C5 contraction. The ratified charged-write projector structure
then gives exactly

```text
F_(i,t)^B=P_(0,i)+zeta_(i,t)P_(ch,i),

product_(t=1)^k F_(i,t)^B
  =P_(0,i)+[product_(t=1)^k zeta_(i,t)]P_(ch,i),

A_(i,k)^B
  =(1-p_i)+p_i product_(t=1)^k zeta_(i,t).          (NS2-B6)
```

For repeated endpoint-covariant history `zeta_(i,t)=zeta_i`,

```text
A_(i,k)^B=(1-p_i)+p_i zeta_i^k.                    (NS2-B7)
```

This is the exact access-side tower. It is inherited from the ratified write
and projector multiplication, not from V007's scalar source exponent.

The V001 equation map is therefore:

| V001 equation | Branch-B status |
|---|---|
| NS-17 symbolic `p_i` | unchanged, symbolic only |
| NS-18 scalar `x_i=ell_i(v_i)` | removed; replaced by endpoint-covariant `zeta_i` after C5 contraction |
| NS-19 `Q^even(d_R)=hbar x^2` | not typed; no network `R` receiver |
| NS-20 `Xi=x-(hbar/2)x^2` | removed as a physical Branch-B equation |
| NS-21 exponent sum | replaced globally by the ordered/product transport in `(NS2-B6)`; a log sum is local-chart bookkeeping only |
| NS-22 quadratic dephasing sum | not typed without the missing endpoint-covariant bilocal receiver |
| NS-23/24 ordered amplitudes and weights | survive in the access form `(NS2-B6)`; weights unchanged |
| NS-25/26 repeated histories | survive as `zeta_i^k`, not as `exp(k[x-(hbar/2)x^2])` |

Thus Branch B transmits generic open-path access exactly but does not provide
the scalar/bilocal V007 drive package V001 claimed. A future map from
endpoint transport to a scalar source would be a new choice and would have
to descend family-wide; V002 contains none.

### 5.4 Branch-B one-edge regression

On the review's one-edge history, Branch B may carry the nontrivial transport

```text
mathcal T_e != identity,
```

but it reports no scalar `q_e`. Under endpoint rephasing it transforms by
`(NS2-B2)`. C5 may consume it on the access side; V007's scalar source port
may not.

```text
R7_ONE_EDGE_NONZERO_TRANSPORT_ALLOWED = true | PASS_WITHIN_PROPOSAL
R7_ONE_EDGE_NONZERO_SCALAR_EMITTED = false | PASS_WITHIN_PROPOSAL
```

---

## 6. Reciprocity, delay, and scope boundary after the repair

**PROPOSED_NOT_ADOPTED — BOTH BRANCHES**

For either branch, node exchange swaps

```text
1 at t -> 2 at t+d,
2 at t -> 1 at t+d
```

without reversing `t<t+d`. `E_post` remains the local write orientation.
Reciprocity does not identify the two histories and does not select a branch.

The displayed computations use the authored minimal member `d=1`. The
proposal family permits every fixed positive integer delay. No-post-output
supplementation excludes `d=0` and negative delay, but no ratified statement
distinguishes `1` from `2,3,...`.

Neither branch contains a map

```text
F_hist:(received source or access object, current history)
       -> next compact write history.                              (NS2-5)
```

Branch A therefore gives exact tower formulas only for an externally supplied
sequence of cycle-admissible histories. Branch B gives exact access products
only for an externally supplied sequence of endpoint transports. Neither is
a complete autonomous network evolution.

```text
RECIPROCITY = PASS_WITHIN_PROPOSAL
E_POST_NETWORK_ORDER = PASS_WITHIN_PROPOSAL
POSITIVE_DELAY = PASS_WITHIN_PROPOSAL
ONE_TIER_DELAY = AUTHORED_NOT_UNIQUELY_FORCED
PORT_TO_WRITE_HISTORY_UPDATE = NOT_BUILT / TYPE-U
AUTONOMOUS_NETWORK_CLOSURE = NO_VERDICT / TYPE-U
```

---

## 7. Restriction, quotient, and account ledger

**PROPOSED_NOT_ADOPTED — NO RATIFICATION CREDIT CLAIMED**

| Operation | Domain | Image | Kernel | Restriction / quotient | Tail / class | Standing |
|---|---|---|---|---|---|---|
| shared `eta` | local doubled histories | `ell^1` coordinate | equal/common histories | finite restriction natural in common chart | no globalization | proposed shared field |
| Branch-A restriction | histories with `B_N^Tq^0=0`; all histories when the kernel is zero | `ker(B_N^T)` | nonconserved histories are outside the nonzero-kernel domain; zero-kernel stages have the unique zero map | old cycles remain conserved under zero-extension | finite cycle core | PASS_WITHIN_PROPOSAL |
| Branch-A `d_J` | conserved coefficient | V007 scalar difference source | source quotient kernel | DoR-015 quotient; exact closed-cycle character | `J_phys` finite core | PASS_WITHIN_PROPOSAL |
| Branch-A `d_R` | admitted cycle vector | rank-one symmetric bilocal | sign identification of quadratic map | trace-class finite corner | no new tail | PASS_WITHIN_PROPOSAL |
| Branch-B transport | open history plus endpoints | endpoint-covariant morphism | common-history identity only | equivariant, not scalar invariant | full torsor family | PASS_WITHIN_PROPOSAL |
| Branch-B C5 receiver | endpoint transport | charged-write modification | receiver character kernel | exact finite access restriction | finite law side | PASS_WITHIN_PROPOSAL |
| Branch-B scalarization | no map | none | unbuilt | no square | new choice class | TYPE-U |
| Branch-B `R` receiver | no map | none | unbuilt | no square | new bilocal class | TYPE-U |
| next-tier delivery | tier `t` emitted object | tier `t+d` receiver | missing edge | prefix exact for fixed authored `d` | finite tier | PASS_WITHIN_PROPOSAL |
| autonomous history update | no map | none | unbuilt | absent | new dynamics | TYPE-U |

Door board:

```text
DOOR_A_CYCLE_SCALAR_EMISSION = PROPOSED_OPENING
DOOR_A_TREE_SCALAR_EMISSION = CLOSED_BY_KERNEL_THEOREM
DOOR_B_ENDPOINT_ACCESS_EMISSION = PROPOSED_OPENING
DOOR_B_SCALAR_SOURCE = NOT_OPENED / TYPE-U
DOOR_B_NETWORK_R = NOT_OPENED / TYPE-U
DOOR_PORT_TO_HISTORY_UPDATE = NOT_OPENED / TYPE-U
DOOR_JOINT_SCALAR_NETWORK = NOT_OPENED / TYPE-U
DOOR_CONTINUUM_RESPONSE = NOT_OPENED / TYPE-U
```

No continuum measure, contour, response operator, bridge, physical root,
coupling, or scale is introduced.

---

## 8. Mandatory standing correction: NS-27 is only a base case

**PROPOSED_NOT_ADOPTED — Q-337 CORRECTION APPLIED TO BOTH BRANCHES**

At the initial ready/equal-history surface,

```text
eta_1=eta_2=0.
```

Branch A emits `q^A=d_J^A=d_R^A=0`. Branch B emits identity endpoint
transport. The first delivered receiver object is therefore the identity
object in the relevant branch. This is NS-27 and no more.

The exact corrected standing is:

```text
READY_IDENTITY_FIRST_EMISSION = ZERO_OR_IDENTITY |
  PASS_WITHIN_PROPOSAL

ALL_ZERO_EXTERNALLY_STIPULATED_HISTORY_SEQUENCE = IDENTITY_TOWER |
  CONDITIONAL

AUTONOMOUS_READY_NETWORK_NO_IGNITION = NO_VERDICT / TYPE-U |
  missing: the port-to-write-history update and a zero-fixed-point certificate
```

The identity tower is conditional on an externally stipulated all-zero
history sequence. There is no induction from the first delivered object to
the next compact history. V002 makes no `TYPE-R` promotion and does not infer
ignition from the failure of no-ignition.

```text
NS27_BASE_CASE = PASS_WITHIN_PROPOSAL
NS28_AUTONOMOUS_INDUCTION = NOT_AVAILABLE / TYPE-U
V001_TYPE_R_NO_IGNITION_PROMOTION_RETAINED = false | TYPE-R |
  test: the missing induction arrow
```

---

## 9. Refreshed hostile battery — both branches

**PROPOSED_NOT_ADOPTED — NO INHERITED CREDIT**

### 9.1 The six V001 attacks, rerun

| Attack | Branch A | Branch B |
|---|---|---|
| 1. additive/replacement offset | **PASS_WITHIN_PROPOSAL**: the restricted map is still zero-anchored; fixed `J_0/R_0` is excluded | **PASS_WITHIN_PROPOSAL**: identity history gives identity transport; a fixed nonidentity morphism is excluded |
| 2. state-valued freedom | **PASS_WITHIN_PROPOSAL**: `d_R^A` contains only the admitted cycle vector twice; no density/covariance slot | **PASS_WITHIN_PROPOSAL**: no `R` emission is proposed, so no state-valued bilocal slot is hidden |
| 3. declared-data disguise | **PASS_WITHIN_PROPOSAL**: the input is actual untraced history satisfying the cycle constraint | **PASS_WITHIN_PROPOSAL**: the input is actual open-path history and endpoints, not a declared probe |
| 4. circularity/target awareness | **PASS_WITHIN_PROPOSAL**: the kernel restriction comes from DoR-015, not the computed tower | **PASS_WITHIN_PROPOSAL**: transport typing comes from DoR-015, not its access-side phase behavior |
| 5. hidden normalization | **PASS_WITHIN_PROPOSAL with residue**: C5 fixes the local scalar coefficient on admitted cycles; `R` unit normalization remains openly authored | **PASS_WITHIN_PROPOSAL**: no scalar normalization exists; character normalization belongs to the ratified receiver |
| 6. history-update attack | **FINDS TYPE-U**: cycle ports do not generate the next compact history | **FINDS TYPE-U**: received access transport does not generate the next compact history |

Attack 6 is not called a pass on autonomous dynamics. It is the explicit
scope boundary and enforces Section 8's no-verdict.

### 9.2 R7 conserved-domain attack, rerun

Branch A passes because every emitted scalar is in `ker(B_N^T)` by domain
definition and the one-edge scalar is exactly zero. Branch B passes because
the one-edge object remains endpoint-covariant and is never inserted into a
scalar V007 port.

```text
R7_BRANCH_A = PASS_WITHIN_PROPOSAL
R7_BRANCH_B = PASS_WITHIN_PROPOSAL
R7_COUNTEREXAMPLE_REPRODUCED = true
```

### 9.3 Fresh Branch-A attack: hidden projector / empty-domain attack

**Attack.** A nominal repair could write `P_cyc q^0` without a ratified
splitting, or constrain histories so severely that no nonzero member remains.

**Result.** V002 uses no projector. The domain is nonempty: identity histories
are admitted, and the reciprocal two-edge family `(NS2-A7)` supplies explicit
nonzero members for any sufficiently small `s` in the common chart. The
emission is therefore neither an unlicensed projection nor a vacuous zero
schema. Independent one-sided histories generally fail the conservation
equation and are honestly outside Branch A.

```text
HIDDEN_CYCLE_PROJECTOR = false | TYPE-S | scoped formula audit
BRANCH_A_NONZERO_DOMAIN = NONEMPTY | PASS_WITHIN_PROPOSAL
ARBITRARY_INDEPENDENT_RECIPROCAL_HISTORIES_ADMITTED = false | TYPE-R |
  counterexample: a reciprocal pair with q_12!=q_21
```

### 9.4 Fresh Branch-B attack: endpoint-frame scalarization attack

**Attack.** Choose endpoint frames, evaluate every open transport as a
number, and quietly feed that number to V007; this would reproduce R7 under
a different name.

**Result.** Branch B retains the full endpoint torsor/intertwiner family. Its
receiver is C5's covariant access side. Any scalar chart appears only inside
the finite receiver check and changes covariantly with matching endpoint
data. There is no map from that chart value to `E_J` or `E_R`.

```text
ENDPOINT_FRAME_SELECTED = false | TYPE-S | scope: Branch-B definitions
ENDPOINT_COORDINATE_FED_TO_SCALAR_PORT = false | TYPE-S |
  scope: Branch-B operation ledger
BRANCH_B_SCALARIZATION_DOOR = NOT_OPENED / TYPE-U
```

### 9.5 R3/R8 standing and TYPE scan

The hostile model in which a zero received port is followed by a nonidentity
next history remains compatible because `F_hist` is absent. Accordingly the
all-tier theorem is not asserted. No authored field or proposal consequence
is marked `TYPE-P`; no rank member, ratio, orientation member, endpoint frame,
or branch is selected.

```text
R3_UNSUPPORTED_INDUCTION_REPEATED = false | TYPE-S | scoped claim audit
R8_TYPE_R_OVERPROMOTION_REPEATED = false | TYPE-S | scoped claim audit
POSITIVE_TYPE_P_SMUGGLING_FOUND = false | TYPE-S | scoped claim audit
```

### 9.6 Battery verdict

```text
BRANCH_A_SELF_KILL = SURVIVES_WITH_NAMED_TYPE_U_HISTORY_UPDATE
BRANCH_B_SELF_KILL = SURVIVES_WITH_NAMED_TYPE_U_R_AND_HISTORY_UPDATE
V002_SELF_CERTIFIED_FOR_RATIFICATION = false [PROCESS STATUS; Q54_EXEMPT]
NEXT_ACTION = LANE_1_ADVERSARIAL_REVIEW
```

---

## 10. Branch comparison — no recommendation

| Question | Branch A — cycle-constrained scalar | Branch B — endpoint-covariant access |
|---|---|---|
| DoR-015 object used | conserved coefficient `q in ker(B_N^T)` | full endpoint transport morphism |
| History domain | only histories whose complete emitted coefficient is conserved | generic admitted open-path histories |
| Ratified receiving side | V007 scalar source port, after cycle restriction | DoR-009/C5 charge/flux-access side |
| Scalar on one edge/tree | forbidden; exactly zero | none emitted |
| Nonzero one-edge content | excluded from scalar branch | allowed as endpoint-covariant transport |
| Minimal nonzero two-system carrier | two reciprocal edges, or triangle in simple-graph category | one oriented edge with endpoint data |
| Exact tower | `Xi=x-(hbar/2)x^2`, `A=(1-p)+p exp(sum Xi)` on admitted cycles | `A=(1-p)+p product zeta` on the access side |
| `R` status | rank-one cycle bilocal, openly authored | no ratified receiver; TYPE-U |
| C5 local `d_J` seam | exact on the admitted closed-cycle chart | survives only as an access-chart check, not a global scalar `d_J` |
| What it forbids | scalar drive on trees; unratified projection | bare scalarization; endpoint-member selection |
| Delay | positive required; exact one-tier member authored | positive required; exact one-tier member authored |
| Autonomous no ignition | NO_VERDICT / TYPE-U | NO_VERDICT / TYPE-U |
| Autonomous closure gap | port-to-write-history update plus zero-fixed-point analysis | access-to-write-history update; plus network `R` receiver if scalar germ tower is required |
| Selection made here | none | none |

The table records different physics interfaces. V002 does not recommend,
rank, merge, or choose between them.

---

## 11. Release ceiling and final board

**PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL RATIFICATION AND CROSS-REVIEW**

What is repaired:

```text
R1_LOCAL_C5_SEAM = PRESERVED_WITH_BRANCH_SPECIFIC_SCOPE
R2_EXACT_V007_EXPONENT = PRESERVED_ON_BRANCH_A
R4_HISTORY_UPDATE_ABSENCE = PRESERVED_AND_ENFORCED
R5_RECIPROCITY_EPOST = PRESERVED
R5_EXACT_ONE_TIER_FORCE_CLAIM = REMOVED
R6_TOWER_ECHO = PRESERVED_WITH_BRANCH_SPECIFIC_FORM
R7_PHYSICAL_PORT_DOMAIN = REPAIRED_IN_BOTH_BRANCHES
R3_R8_NO_IGNITION_STANDING = CORRECTED
```

What remains proposed or unbuilt:

```text
BRANCH_A_CYCLE_HISTORY_RESTRICTION = PROPOSED_NOT_ADOPTED
BRANCH_A_RANK_ONE_R = PROPOSED_NOT_ADOPTED
BRANCH_B_ENDPOINT_EMISSION_RULE = PROPOSED_NOT_ADOPTED
POSITIVE_DELAY_MEMBER = PROPOSED_NOT_ADOPTED

PORT_TO_WRITE_HISTORY_UPDATE = TYPE-U
BRANCH_B_NETWORK_R_RECEIVER = TYPE-U
JOINT_NETWORK_STATE_EFFECT_CONTRACTION = TYPE-U
```

No result in this artifact computes or bounds a physical response value. No
root, coupling, scale, or measured comparison is attempted.

```text
NETWORK_SOURCING_LAW_V002_WRITTEN = true [PROPOSAL STATUS]
NETWORK_SOURCING_LAW_V002_RATIFIED = false [PROPOSAL STATUS; Q54_EXEMPT]
NETWORK_SOURCING_LAW_V002_READY_FOR_SELF_CERTIFICATION = false [PROCESS STATUS; Q54_EXEMPT]
REVIEW_CUSTODY = LANE_1

BRANCH_SELECTED = false | TYPE-S | scope: this artifact
TARGET_OUTPUT_USED_TO_SELECT_BRANCH = false | TYPE-S | scoped formula audit
FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-S |
  scope: all requested structural results were permitted

REGISTER_HEAD_AT_BUILD = Q-337

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 12. Custody

This lane seals this lane-tagged V002 artifact, verifies the sidecar, mirrors
the artifact and sidecar byte-identically to
`/Users/bgm/MB Work/alpha-program-archive/workspace/`, reports both hashes,
and stops. It does not edit the register, governing plan, tracker, or any git
state and performs no commit or push action.
