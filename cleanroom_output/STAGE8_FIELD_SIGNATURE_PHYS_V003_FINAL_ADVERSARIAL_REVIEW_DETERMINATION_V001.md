# FINAL ADVERSARIAL REVIEW OF FIELD_SIGNATURE_PHYS V003

**Verdict:** `REPAIR_THEN_READY`

**DoR-015 package:** not issued.

**Register head at start:** Q-293, SHA-256
`35eabb92b90d744e1465c10524773eda59982051e243ae4220d9c2d0339699b7`.

```text
alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

---

## 1. Scope, custody, and authorities

This is the final independent gate review requested by relay 376. It reads and
tests V003; it does not repair V003, ratify DoR-015, register a ruling, or
construct any response object.

### 1.1 Frozen authorities

| Authority | SHA-256 | Use |
|---|---|---|
| `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V003.md` | `a5a8420da4878f735553b1cc7870d2e722b0bb039328621070bcb29fc066aaa2` | object under review |
| `STAGE8_FIELD_SIGNATURE_PHYS_V002_ADVERSARIAL_REVIEW_DETERMINATION_V001.md` | `d11c0ffd6b24876ce8da7821fd733c326b41095e8b4a7d3a1e831a19a906641b` | Q-292 repair order and prior counterexamples |
| `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V002.md` | `deaa86ee58edb9f841ae3f7bae8ccf9b1cf659328b99fb60cd290a348641e1ad` | pre-repair six-field baseline |
| `STAGE8_TASK4A_RECORD_SURFACE_TO_PHYSICAL_FIELD_SIGNATURE_DERIVATION_AND_BETA_GAP_ATTACK_V001.md` | `65e4dd6a6e2926c9c100edb162f57352311e73438f23dd19509dda0403e2e4f6` | derived D1-D4 split and R1-R10 residue |
| `STAGE8_TASK4A_P5_MAXIMAL_TRANSPORT_CHAIN_AND_DEPENDENCE_ACCOUNTING_PACKAGE_V002.md` | `31a738ec17696ea01e1cb6a6ee7a37a29e6c0ca24d6fb8cc050d06aed32a583f` | Q-288 mandatory class-formation door schema |
| `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md` | `57c06fcbedf4a486b87b42c02e6d13a92096ac6a56751d3ae5fd55f4b11deb57` | physical quotient, perturbation, and endpoint-intertwiner contract (`:641-688`) |
| `STAGE8_TASK4D_STITCHING_THEOREM_GERM_INDEPENDENT_HALF_V001.md` | `430f09715146cc03dabb0e349c422ae2499cff893d4e46b490fc0870954d1cb4` | D4 `T_cyl` separation and finite retractions (`:213-243`) |

### 1.2 Search scope

```text
ROOTS_ENTERED = (
  current cleanroom root,
  local Q-292 review mirror,
  alpha_supervision register through Q-293
)

EXCLUSIONS = (
  a32_holdout/custodian_private,
  all response/value/root/rank-member evaluation,
  all unregistered drafts later than Q-293,
  all register/plan/tracker/git/commit/push acts
)
```

No premise beyond the frozen stack is used except ordinary principal-bundle,
associated-bundle, quotient, inverse-limit, and normed-space mathematics. Each
applies only because V003 itself proposes the corresponding carrier.

---

## 2. Lead finding: the full framed tangent defeats A4 separation

V003 correctly retains the full endpoint-frame family. It then defines

```text
X_N=(Conn(P_M) x Fr_N)/Gauge_c
```

with a residual endpoint-frame action which is explicitly retained as
covariance data (`V003:282-315`). Its path coordinate obeys

```text
h_e -> g_t h_e g_s^(-1)
```

under `p_v->p_v g_v^(-1)` (`V003:302-315`). The visibility tangent is then
defined on the full framed carrier:

```text
T_vis,x = T_x X_inf / intersection_N ker(dH_N|x).
```

But A4 defines its purportedly separating covectors only on the connection
component:

```text
u_e(a)=integral_(gamma_e) a.
```

### 2.1 Explicit counterexample

Take one realized edge `e:s->t`, one framed point `x=[A,p]`, and the smooth
curve

```text
A(epsilon)=A,
p_s(epsilon)=p_s,
p_t(epsilon)=p_t exp(-i epsilon),
```

with all other endpoint frames fixed. V003's own transformation law gives

```text
h_e(epsilon)=exp(i epsilon) h_e(0),
dH_e/d epsilon|0 = i h_e(0) != 0.
```

Therefore the tangent `v` of this curve is not in the common kernel of the
finite `dH_N`, so `[v] != 0` in V003's `T_vis,x`. Its connection component is
`a=0`, hence

```text
u_f(v)=integral_(gamma_f) 0=0
```

for every edge `f`. Thus every A4 current annihilates a nonzero visible
tangent.

The same witness directly refutes V003's A5 statement that the differentials
of its relative phases are the A4 currents. On this curve,

```text
d phi_e(v) = 1,
u_e(v) = 0.
```

The omitted term is the endpoint-frame coboundary `delta theta_t-delta
theta_s`.

```text
A4_CURRENTS_SEPARATE_V003_FULL_VISIBLE_TANGENT = false | TYPE-R |
  test: fixed-connection endpoint-frame curve above

A5_PHASE_DIFFERENTIAL_EQUALS_A4_CURRENT_ON_FULL_FRAME_FAMILY = false | TYPE-R |
  test: d phi_e(v)=1 while u_e(v)=0 on the same curve

S5_SOURCE_KERNEL_AND_VISIBLE_SEPARATION_HOLDS_AS_WRITTEN = false | TYPE-R |
  test: V003 S5 consumes the refuted A4 separation statement
```

### 2.2 Why the Ward residue does not save the current text

The counterexample direction is the residual frame/vertex action and may
eventually be declared gauge-null. V003 cannot use that answer now: it says
the residual action is retained (`:314-315`) and repeatedly types its Ward
descent unbuilt (`:351-353,524-526,642-644,772-774`). The proposed tangent at
`:375-383` is the tangent of `X_inf`, not a connection-only vertical tangent
at fixed frame.

```text
V003_ALREADY_QUOTIENTS_THE_COUNTEREXAMPLE_DIRECTION = false | TYPE-R |
  test: residual-frame/Ward descent is explicitly TYPE-U in V003

WARD_TYPE_U_MAY_BE_USED_AS_CURRENT_NULL_RELATION = false | TYPE-R |
  test: an unbuilt quotient cannot discharge a present separation theorem
```

This is a defect in the proposed typing, not evidence against the existence of
a lawful repair.

---

## 3. T1: the torsor-family scalarization itself survives

The lead finding does not reinstate Q-292's S3 counterexample. V003 repairs S3
at the carrier level.

### 3.1 Family-wide scalar transport

For every endpoint-frame tuple `p`, principal parallel transport supplies the
unique scalar `h_e(A,p)` through

```text
PT_A(gamma_e)(p_s)=p_t h_e(A,p).
```

The scalar is invariant under the diagonal physical bundle-gauge action and
equivariant under independent endpoint-frame change. The construction is a
function on the whole framed carrier `X_N`; no frame member is evaluated or
selected.

### 3.2 `C_Emb`, S7, and Door A

Conditional on A2-R9, `H_N:X_N->U(1)^(E_N)` is continuous and onto. Therefore
pullback

```text
f -> f compose H_N
```

is injective and isometric in sup norm. The finite maps are natural under
A2-R6/R8. Any finite frame tuple extends to later endpoint fibers because
`Fr_M->Fr_N` is the product projection and every principal fiber is nonempty;
the same global connection remains available. Hence each finite coordinate
surjection is also reached from the compatible family. D4's norm universal
property then gives the family-wide `Emb_cyl`.

This proof quantifies over all frame tuples. It does not choose one.

```text
T1_TORSOR_FAMILY_SCALARIZATION = SURVIVED
C_EMB_REQUIRES_A_SELECTED_FRAME_MEMBER = false | TYPE-R |
  test: C_Emb is pullback on the complete framed carrier, not evaluation at p
S3_OPEN_TRANSPORT_REPAIR = SURVIVED_CONDITIONALLY |
  premises: A1, A2-R6/R8/R9, A3, and the full frame family
S7_APPLICATION = SURVIVED_CONDITIONALLY |
  premises: the same finite surjections plus D4
DOOR_A_MATHEMATICAL_MAP = SURVIVED_CONDITIONALLY |
  premises: the same family-wide pullback theorem
```

T1 therefore passes. The failure is in A4's later choice of tangent and
covectors, not in the family-wide scalar map.

---

## 4. T2: the set quotient passes; the source-level theorem fails

### 4.1 Independent set-level separation proof

V003 defines

```text
x ~vis y iff H_N(x)=H_N(y) for every N.
```

Let `H=(H_N)_N`. The induced map

```text
Hbar:X_inf/~vis -> image(H)
```

is well defined and injective by the defining relation. Thus the finite
coordinate family separates the **set quotient** exactly.

### 4.2 Visible witness pair survives

Fix endpoint frames and choose, under A2-R10, a connection tangent `a` with
nonzero `u_e(a)` for one admitted edge coordinate. For sufficiently small
nonzero epsilon,

```text
x=[A,p],
y=[A+epsilon a,p]
```

have `H_N(x)!=H_N(y)` at a finite stage containing `e`. Hence `x` and `y` are
not identified. A difference witnessed by one finite record coordinate
survives the quotient.

```text
PATH_VISIBLE_SET_QUOTIENT_IS_SEPARATED = true |
  PROPOSAL-CONDITIONAL MATHEMATICS
RECORD_VISIBLE_PAIR_IDENTIFIED_BY_VISIBILITY_QUOTIENT = false | TYPE-R |
  test: fixed-frame connection witness above
```

### 4.3 Six-field compatibility audit

| Structure | Quotient verdict | Independent reason |
|---|---|---|
| A1 background | PASS | quotient does not act on `(M,g,o,t;P_M)` |
| A2 realization | PASS | paths, endpoints, supports, and incidence remain explicit |
| A3 transport | PASS at set level | the quotient is defined by its total framed transport coordinates |
| A4 source rigging | **FAIL** | connection currents omit visible endpoint-frame tangent directions |
| A5 field algebra | PARTIAL | bounded holonomy cylinders factor, but the claimed local differential identity fails |
| A6 bilocal class | WOUNDED | abstract class on A4's span is separated, but that span does not cover V003's full visible tangent/source carrier |

The correct determination is therefore split:

```text
T2_SET_LEVEL_QUOTIENT = SURVIVED
T2_ALL_SIX_STRUCTURES_QUOTIENT_COMPATIBLE_AS_CLAIMED = false | TYPE-R |
  test: A4/A5 frame-tangent counterexample; A6 inherits the source omission
```

Q-293's recorded phrase "A4/A5 separate it by construction" does not survive
this final test. Separation by definition applies to `H`; it does not identify
the separately defined connection-only covectors `u_e` with all components of
`dH`.

---

## 5. T3: R6 endpoint intertwiner survives

For the associated line

```text
L_v=(P_M)_(iota(v)) x_ch C,
```

every frame member supplies

```text
I_(v,p):C_chi->L_v,
I_(v,p)(z)=[p_v,z].
```

This is an isomorphism and transforms equivariantly under frame change. The
parallel-transport square

```text
PT_A(gamma_e) I_(s,p)
  = I_(t,p) multiplication_by(h_e(A,p))
```

is the standard associated-line transport identity. It is family-wide and
selects no member.

The provenance split is accurate:

```text
finite endpoint labels = D1/D2 | TYPE-P;
physical principal fibers and realization = A1/A2 | PROPOSED;
complete frame family = mathematical consequence of A1/A2;
endpoint intertwiner family = mathematical consequence of those premises;
Ward generator/domain/descent = TYPE-U.
```

```text
T3_R6_ENDPOINT_INTERTWINER_FAMILY = SURVIVED
R6_WARD_DESCENT_COMPLETED = false | TYPE-U |
  would-build: residual-frame quotient, Ward generator, invariant common
               domain, and completed physical restriction square
```

---

## 6. Second defect: `X_inf` class formation is outside every door

V003 first forms

```text
X_inf = compatible family of all finite framed presentations
```

and gives the later quotient the projective topology generated by all `H_N`
(`V003:324-334`). This is an inverse/projective class-formation step from the
finite `X_N` system. Door V begins **after** that step:

```text
input_class = X_inf,
formation_operation = quotient by intersection_N ker(H_N).
```

Thus Door V accounts for `X_inf->Conn_fr,vis`, not for
`{X_N}->X_inf`. No other door names the inverse-limit carrier, its input
topologies, transition maps, output topology, projection surjectivity, or
created-tail proof.

Q-288 requires every physical class-forming passage to fill the mandatory
door block. The topology is not forbidden, and no weak-star or bidual operation
is present, but the door declaration is missing.

```text
UNFLAGGED_CLASS_FORMATION_STEP_FOUND = true | STRUCTURAL_FINDING |
  test: X_inf is formed and topologized before Door V takes it as input

V003_UNFLAGGED_CLASS_FORMATION_STEP_FOUND_FALSE_FLAG = REFUTED_BY_AUDIT |
  test: compare V003:324-334 with Door V:835-871 and Q-288:572-613

PROJECTIVE_FRAME_LIMIT_DOOR_BUILT = false | TYPE-U |
  would-build: a Door F block for {X_N}->X_inf naming finite input classes,
               transition maps, projective topology, finite projections,
               nonemptiness/projection surjectivity, restriction square,
               separation, and created-tail image
```

The likely zero-tail proof is short because two compatible families equal in
every finite projection are the same family. That proof belongs in the missing
door; this review does not patch it into V003 after output.

---

## 7. T4 full regression

### 7.1 Seam matrix

| Seam | Final review | Reason |
|---|---|---|
| S1 orientation/causal path | conditional pass | A2-R2 remains explicit and failure-capable |
| S2 incidence/support | conditional pass | A2-R4/R5 preserve inherited incidence |
| S3 framed transport | conditional pass | T1 family-wide scalarization proof |
| S4 CTP reality | conditional pass | frame covariance does not alter D3 branch exchange |
| S5 physical source kernel | **TYPE-R as written** | full visible tangent contains frame directions absent from `u_e` |
| S6 zero-extension | conditional pass on A4's connection-current subspace | finite coefficient maps commute; completeness is wounded by S5 |
| S7 T_cyl pullback | conditional pass as a bounded cylinder map | T1; projective formation door still missing |

```text
SEVEN_SEAMS_V003_PASS_AS_AGGREGATE = false | TYPE-R |
  test: S5 frame-tangent counterexample
```

### 7.2 Door D0 re-proof

Let `r_N i_N=id`, with every `r_N` contractive, and let finite cylinders be
dense in the D4 norm. If `r_N x=0` for every `N`, choose finite `y=i_N y_N`
with `||x-y||<epsilon`. Then

```text
||y||=||r_N y||=||r_N(y-x)||<=||y-x||<epsilon,
||x||<2 epsilon.
```

Hence `x=0`. No weak-star limit is used.

```text
DOOR_D0_RECONFIRMED = CLOSED_SEPARATED_ZERO_CREATED_TAIL
```

### 7.3 Remaining doors

| Door | Final review |
|---|---|
| Door V quotient | set-level conditional pass; input formation unaccounted |
| Door A | bounded family-wide pullback passes conditionally; source differential claim not part of this pass |
| Door B | Hilbert completion is tail-free on the declared A4 span; physical-source completeness wounded by S5 |
| Door C | trace-norm completion remains tail-free on Door B's declared carrier; same physical-source wound |
| Door D | abstract bilinear separation survives; physical image correctly remains `NO_VERDICT` |

No weak-star, bidual, nonseparating, or distributional completion is invoked.
The projective limit is a permitted structural operation whose accounting is
missing, not a forbidden creator.

### 7.4 Choice-table regression

The six top-level authored structures remain a coherent count. However, the
choice table omits the physical status of endpoint-frame directions at the
A3/A4 boundary. It neither:

1. declares frames presentation parameters held fixed under source
   differentiation;
2. quotients frame directions before defining the visible tangent; nor
3. includes endpoint-frame coboundary covectors in A4.

Those three choices have different source domains and Ward obligations. The
choice is load-bearing and must be disclosed before ratification.

```text
V003_INDEPENDENT_AUTHORED_STRUCTURE_COUNT_SIX = SURVIVED
V003_CHOICE_TABLE_COMPLETE_FOR_FRAME_TANGENT_STATUS = false | TYPE-R |
  test: three inequivalent repairs above are absent from A2-A5 and the choice table
```

### 7.5 Derived and restriction regressions

* `E_post` remains the finite endpoint-charge orientation and is not promoted
  to a physical frame.
* Gate-4 incidence is consumed equivariantly; no duplicate incidence operator
  is authored.
* `T_cyl` remains the D4 norm cylinder algebra; no identity with full raw-G is
  claimed.
* Finite framed holonomy restriction reproduces the finite edge transport
  conditionally through S3.
* Full Q-279/raw-G reproduction remains TYPE-U and is not falsely claimed.
* The Q-290 unit-modulus no-go remains in force.

```text
DOR008_FULL_PHYSICAL_RESTRICTION_REPRODUCTION_COMPLETE = false | TYPE-U |
  would-build: repaired A4/A5 source interface, Door F, physical raw-G image,
               and the complete restriction run
```

### 7.6 Target-awareness and forbidden-content scan

The only occurrences of alpha, `p_ch`, stiffness, response value, or measured
targets in V003 are fences and audit queries. No A1-A6 membership predicate
reads a downstream output. No value or member is selected.

```text
TARGET_AWARE_MEMBERSHIP_PREDICATE_FOUND = false | TYPE-S |
  roots: V003 A1-A6, R1-R11, choice table, seams, and doors |
  exclusions: fences, search queries, and downstream status prose |
  fences: no evaluation performed |
  query: word-boundaried alpha; p_ch; stiffness; response value; residual;
         measured; target

WEAK_STAR_BIDUAL_OR_DISTRIBUTIONAL_COMPLETION_INVOKED = false | TYPE-S |
  roots: V003 every quotient, topology, completion, closure, and door |
  exclusions: alternatives and TYPE-U future operations |
  fences: no physical class formation executed |
  query: weak-star; bidual; distributional completion; nonseparating extension
```

---

## 8. Bounded repair package

The proposal is not dead. The defects have two exact repair obligations.

### 8.1 Repair F-TAN: freeze the status of frame directions

V004 must choose and disclose one target-independent construction:

```text
FIBERWISE:
  frames remain a complete parameter family;
  source differentiation is explicitly vertical only in Conn(P_M) at fixed p;
  T_conn,vis = T_A Conn / intersection_N ker(d_A H_N);
  d_A phi_e = u_e;

WARD-FIRST:
  quotient residual endpoint-frame directions before A4;
  instantiate the required Ward/vertex descent and its domain;

AUGMENTED-SOURCE:
  retain full T_x X_inf and enlarge A4 by endpoint-frame coboundary covectors
  so d phi_e = u_e + delta theta_t-delta theta_s.
```

The reviewer does not select among these. The minimal-looking fiberwise route
still needs an explicit proof that every downstream source derivative is
defined fiberwise and no consumer differentiates the frame parameters.

### 8.2 Repair F-LIM: account for the compatible-family formation

Add one Q-288-complete class-formation door for

```text
{X_N,restriction_MN} -> X_inf.
```

It must name the finite input topology, projective output topology, transition
maps, finite projections, topology change, every limit, weak-star/bidual flags,
projection surjectivity, separation, created-tail image, restriction square,
common-origin standing, and target-independence.

### 8.3 Required reruns

After those two repairs, rerun exactly:

```text
A4 separation;
A5 phase differential identity;
A6 physical-source domain statement;
S5 and the S6 scope statement;
Doors B and C physical-source application;
Door A composition through the new projective-limit door;
choice-table completeness;
unflagged-class-formation scan.
```

No other V003 field is ordered reopened.

```text
REPAIR_SCOPE_BOUNDED_TO_F_TAN_AND_F_LIM = true |
  STRUCTURAL_DETERMINATION
REPAIR_REQUIRES_NEW_TARGET_AWARE_PHYSICS = false | TYPE-S |
  roots: F-TAN and F-LIM obligations above |
  exclusions: response outputs and measured data |
  fences: no value evaluation |
  query: every repair antecedent and consequence
```

---

## 9. Final verdict and DoR-015 gate

```text
T1_TORSOR_FAMILY = SURVIVED
T2_VISIBILITY_SET_QUOTIENT = SURVIVED
T2_A4_A5_DIFFERENTIAL_SEPARATION = TYPE-R
T3_R6_ENDPOINT_INTERTWINER = SURVIVED

T4_SEAMS = REPAIR_REQUIRED_AT_S5
T4_DOOR_D0 = CLOSED_SEPARATED_ZERO_CREATED_TAIL
T4_DOOR_V = CONDITIONAL_PASS_WITH_INPUT_DOOR_MISSING
T4_DOOR_A = CONDITIONAL_PASS_WITH_F_LIM_ACCOUNTING_REQUIRED
T4_DOORS_B_C = ABSTRACT_PASS_PHYSICAL_SOURCE_WOUNDED
T4_DOOR_D = NO_VERDICT |
  prerequisite: repaired source interface, scalar physical functional,
                completed quotient, raw-G lift, restrictions, and provenance

OVERALL_VERDICT = REPAIR_THEN_READY

DOR_015_PACKAGE_ISSUED = false | TYPE-C |
  constraint: S5 is TYPE-R on the actual V003 tangent and the X_inf formation
              lacks its mandatory Q-288 door |
  release: V004 freezes one F-TAN route, adds F-LIM, reruns the exact list in
           Section 8.3, and survives independent confirmation

DOR_015_RATIFICATION_READY = false | TYPE-C |
  constraint: two load-bearing conditions of the requested final gate fail now |
  release: the same V004 repair and confirmation required above
```

No DoR-015 package is emitted because the condition "if all pass" is false.
The six-structure count, no-selection torsor family, set-level visibility
quotient, endpoint intertwiner family, D0 proof, and no-target/no-creator
results survive and should be preserved verbatim in the bounded repair.

```text
REGISTER_HEAD_AT_START = Q-293
REGISTER_HEAD_AT_SEND_TIME = Q-293
REGISTER_SHA256_AT_FINAL_CHECK =
  35eabb92b90d744e1465c10524773eda59982051e243ae4220d9c2d0339699b7
LATER_BEARING_RULING_CONSUMED = false | TYPE-S |
  roots: alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md through Q-293 |
  exclusions: no unregistered V004 or DoR-015 draft |
  fences: no cross-lane coordination |
  query: Q-294; FIELD_SIGNATURE_PHYS V004; DoR-015

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

Custody: seal this determination, verify the sidecar, mirror artifact and
sidecar to `alpha-program-archive/cleanroom_output/` and
`alpha-program-archive/workspace/`, report hashes and exact paths, and stop.
No register, plan, tracker, git, commit, push, gate, or deploy action is
performed by this lane.
