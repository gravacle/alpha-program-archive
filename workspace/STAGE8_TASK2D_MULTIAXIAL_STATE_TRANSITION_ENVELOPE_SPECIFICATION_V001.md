# Stage 8 Task 2d Multiaxial State-Transition Envelope Specification v001

Date: 2026-08-01  
Lane: CODEX LANE 2  
Task: Task 2d — state-transition envelope  
Register head at issue: Q-225  
Road: advances the physical-input package by typing the state path before any forcing protocol is run

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 0. Lead determination

**The joint dynamics edge is the first load-bearing blocker.** The corpus has
an exact finite source-record transition and an exact outgoing **record-only**
inductive-limit state, but it has no full-carrier transition connecting the
declared `rho_pre` role to a completed source-record-field/CTP state and then to
a full outgoing state. The missing edge is exactly the already specified
`DynPort_U2_008`; its physical object is the common-origin doubled CTP
influence-functional instance.

This is the same missing physical instance already consumed by:

1. U2's dynamics port;
2. Task 3a's Lorentzian/CTP record functional;
3. Task 3c's complete source-inclusive physical amplitude; and
4. this transition envelope.

It is therefore **one gap with four consumers**, not four independent missing
objects. This identification is by interface and codomain, not by a shared
name.

The envelope is specifiable today as a typed partial graph:

```text
N_pre^C0  --E_joint [TYPE-U]-->  N_completed^C0  --E_out^C0 [TYPE-U]--> N_out^C0
   |                                      
   | Res_N [TYPE-U as physical descent]
   v
N_ready,N^SR --E_finite,N [DERIVED]--> N_N^SR --E_record,N [DERIVED]--> N_out^R
```

The bottom row is real but narrower than the top row. It cannot be transported
upward: its middle carrier is `A_src tensor R_N`, and its endpoint is the
record algebra `R_infinity`, not the completed `C0_008` carrier or a global
source-inclusive outgoing algebra.

The forcing protocol is **not runnable**. Step 1 cannot declare an instantiated
family of complete paths. Two independent prerequisites are absent:

- the full common-origin dynamics path (`TYPE-U`); and
- a completed-carrier quasifree/finitely-correlated predicate (`TYPE-S` for a
  found predicate; `TYPE-U` for constructing one).

The minimal first build is the common-origin doubled CTP influence-functional
instance realizing `StatePort_U2_008`, `EffectPort_U2_008`, and
`DynPort_U2_008`. That build would instantiate a path, but it would **not by
itself prove coverage** of a candidate family. Coverage additionally needs a
frozen manifest of complete path instances and executable completed-carrier
class predicates.

```text
MULTIAXIAL_STATE_TRANSITION_ENVELOPE_SPECIFIED = true
  scope: typed nodes, typed edges, provenance-witness interface, and blockers

MULTIAXIAL_STATE_TRANSITION_ENVELOPE_INSTANTIATED = false | TYPE-U |
  missing: full-carrier state, dynamics, effects/domains, full outgoing state,
           and one common-origin path witness

JOINT_DYNAMICS_EDGE_INSTANTIATED = false | TYPE-U |
  would-build: the common-origin doubled CTP influence-functional instance
               satisfying DynPort_U2_008

END_TO_END_FULL_CARRIER_STATE_PATH_EXISTS = false | TYPE-U |
  missing: E_joint, a full completed node, and E_out^C0

FORCING_PROTOCOL_RUNNABLE_NOW = false | TYPE-C |
  constraint: protocol step 1 requires instantiated complete path members;
              schemas and disconnected narrow-carrier nodes do not qualify

NO_STATE_CLASS_SELECTED = true
  scope: this specification performs no forcing and emits no survivor count
```

The last line is an asserted scope mark, not a hypothetical future verdict.

## 1. Preflight, premises, scope, and currency

### 1.1 Preflight

```text
DOES_THE_OBJECT_EXIST = YES_AS_A_SPECIFIABLE_PARTIAL_GRAPH
  present: named temporal roles, one exact finite edge, one exact record-limit
           endpoint, U2 port interfaces, and common-origin certificate schema
  absent: one instantiated full-carrier path

IS_THE_VERSION_CURRENT = YES
  basis: Q-225 and the full 1421bfc7 artifact were read first; Q-223 through
         Q-225 scope corrections are applied

ARE_THE_INPUTS_PRESENT = PARTIAL
  present: C0_008/U1_008 under DoR-008, exact finite dynamics, record GNS limit
  absent: StatePort, EffectPort, DynPort, completed joint state, full outgoing
          state, completed cumulant predicate, and path provenance witness
```

### 1.2 Declared premises

This specification freezes the following premises before declaring any path
member:

```text
P1  DoR-008 supplies the algebraic joint carrier and U1 conventions only as
    TYPE-P premises; it supplies no scalar state, dynamics, trace, measure, or
    physical quotient.

P2  The finite charged-incidence transition is accepted exactly on its stated
    finite source-record domain.

P3  The outgoing record GNS result is accepted exactly on the inductive-limit
    record algebra; it is not a global source-inclusive limit.

P4  Parent-State Covariance and the P5 common-origin presentation govern
    provenance. They do not themselves instantiate a state or dynamics.

P5  No state-class predicate, dynamics edge, or bridge identity is added merely
    to make protocol step 1 runnable.
```

Every carrier claim using DoR-008 is `TYPE-P | premises: DoR-008`. No physical
state is promoted by that mark.

### 1.3 Frozen authorities

| Authority | SHA-256 | Use |
|---|---|---|
| `STAGE8_TASK2D_MULTIAXIAL_STATE_CLASS_ENVELOPE_FORCING_PROTOCOL_RESULT_V001.md` | `1421bfc788ee577cb2673a3c394c7ac8f1f62d53f9e512e9d0a080df56e394db` | Q-225 correction and transition-envelope type |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_U2_DOR008_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md` | `2b6291227b7ac5967796014c2ad217c9eb084b5bb6df23fed0a7bca464e8bfab` | State/effect/dynamics port interfaces |
| `R3_4_CHARGED_INCIDENCE_OUTGOING_STATE_RESULT_V002.md` | `2be95d5b58ea000df9a30b717a809374a90693f78a893d87b73a12e4be97fa21` | Exact finite transition and completed states |
| `R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md` | `10909b5c21e73ecf655462339a27bd645b8d35e3ad11fb6f8cb204c601992995` | Exact record-only inductive limit and GNS |
| `CAUSAL_DIRECT_LIMIT_RECORD_PRINCIPLE_V002.md` | `7333204581ef3183665c9dd056d79f2caa073724e3566295ab888ccc5494c53a` | Durable outgoing-record meaning |
| `STAGE8_P5_COMMON_ORIGIN_DESCENT_REQUIREMENT_V001.md` | `a33be83c1ee7cbfbda2cc3857425cb9e7e90a23bbe3d61c9ec89432e50b77874` | Operational descent maps and certificate |
| `PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md` | `532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb` | Same-parent path covariance |
| `STAGE8_TASK2D_QUASIFREE_BRANCH_RHO_PRE_GOVERNANCE_AUDIT_V001.md` | `8aad619a542aba5991288485509c91a41425aa2fed81fb77d95c73119c0db84d` | Source-CAR versus completed-state boundary |
| `STAGE8_TASK3A_FOUR_LORENTZIAN_FORMS_AND_DURABILITY_ADJUDICATION_V001.md` | `056c30481c9c2a055e9b4c7cd7d381e25caf4eaf5aa4ec8a170aa6ba67f65b00` | Complete Lorentzian/CTP instance debt |
| `STAGE8_T7_PHYSICAL_ACTION_MULTIPLIER_FORCING_PROTOCOL_STEP1_STOP_V001.md` | `5209d3cd77dcb9f71c909a10c10715ce47640b24313b3da223ee067d859e48cd` | Complete physical-amplitude consumer |

### 1.4 Roots, exclusions, and searches

Roots entered:

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha-program-archive/workspace
/Users/bgm/MB Work/alpha-program-archive/cleanroom_output
/Users/bgm/MB Work/alpha_supervision
```

Exclusions:

```text
a32_holdout/custodian_private/
.git/
external/
third_party/
seal sidecars as substantive evidence
byte-identical archive mirrors as independent authorities
```

The private-custodian path was not entered. Case-insensitive,
word-boundaried searches included:

```text
rho_pre | finite completed | outgoing state | outgoing GNS
StatePort_U2_008 | EffectPort_U2_008 | DynPort_U2_008
common-origin | common construction trace | projective limit state
joint quasifree | completed-carrier quasifree | Wick-determined
finitely-correlated | finite-correlation state | cumulant closure
source-inclusive outgoing | influence functional | physical amplitude
G_joint
```

The broad `cumulant` hits in historical review packets concern coefficient
expansions and target equations, not a completed-state predicate on `C0_008`.
They do not instantiate this axis and were not imported.

### 1.5 Symbol-collision correction

The Q-225 artifact used `G_joint` at `:296,314` as a placeholder for a
fundamental joint generator family. That token is already defined in
`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V008` through `V011` as

```text
G_joint = R^3 / K_sum ~= U(1),
```

the additive-action comparison group. The objects are not identical.
This specification reserves:

```text
Gen_C0 := a future named response-generating set on the completed carrier.
```

`Gen_C0` is an interface name only; it is not an asserted existing object.

```text
Q225_PLACEHOLDER_G_joint_IS_BID_COMPARISON_GROUP = false | TYPE-R |
  test: the two occurrences have different signatures and codomains

COMPLETED_RESPONSE_GENERATOR_SET_FOUND = false | TYPE-S |
  scope: roots/exclusions/queries in Section 1.4
```

## 2. Node specification

### 2.1 `N_pre^C0` — declared full-carrier pre-state role

The live v004 source at `primitive_record_cell_selection_principle_v004.md:19-20`
declares `rho_pre` as positive trace-class on the full source-record-field
Hilbert space with unit trace. The U2 determination shows why this is not yet
an instance on `C0_008`: `C0_008` is a Hilbert C-star-module presentation, not
a scalar Hilbert space with a trace (`U2_008:148-227`).

The node interface is therefore:

```text
N_pre^C0 := (
  A_C0,
  omega_phys : B -> C,
  H_omega,
  pi_omega : A_C0 -> B(H_omega),
  rho_pre in trace_class(H_omega),
  rho_pre >= 0,
  Tr_omega(rho_pre)=1,
  D_state,
  d_state,
  Cert_state
).
```

This is the `StatePort_U2_008` signature at `U2_008:259-285`, not an
instantiated state.

**State description and axes.** Its algebra has the ratified split

```text
A_C0 = A_SR graded-tensor_min A_F_CTP                 [TYPE-P: DoR-008].
```

On an actual state, the `SR|F` coordinate would be one of product or
nonproduct; a joint character is excluded by the `M_3(C)` record factor.
Because `rho_pre` itself is absent, this node has no instantiated coordinate
value. The source-versus-record coordinate and the CTP-branch coordinate have
not been appointed as one universal factorization axis.

```text
N_PRE_C0_STATE_INSTANCE_EXISTS = false | TYPE-U |
  would-build: StatePort_U2_008

N_PRE_SR_F_SPLIT_IS_TYPED = true | TYPE-P | premises: DoR-008

N_PRE_SR_F_FACTOR_VALUE_ASSIGNED = false | TYPE-C |
  constraint: no state instance exists to test for product/nonproduct

N_PRE_GLOBAL_FACTORIZATION_INDEX_FROZEN = false | TYPE-S |
  scope: no sealed rule selects among SR|F, source|record, and branch splits
```

### 2.2 `N_ready,N^SR` and `N_N^SR` — exact finite source-record nodes

For each finite `N`, the record algebra is

```text
R_N = tensor_(j=1)^N M_3(C),
```

and the exact finite transition accepts a charge-superselected source state
and ready-cell product record state. The completed state is

```text
rho_N
 = P_0 rho_S P_0 tensor |r><r|^tensor_N
 + P_ch rho_S P_ch tensor |p_Q><p_Q|^tensor_N.
```

This is the executed object at
`R3_4_CHARGED_INCIDENCE_OUTGOING_STATE_RESULT_V002.md:48-106` and the Q-225
control at `STAGE8_TASK2D_MULTIAXIAL_STATE_CLASS_ENVELOPE_FORCING_PROTOCOL_RESULT_V001.md:476-518`.

Its proper algebra and coordinate are:

```text
A_N^SR = A_src tensor R_N,
Pi_S|R,N = A_src | R_N.
```

If exactly one charge-sector weight is nonzero, `rho_N` is product across
`S|R_N`. If both are nonzero, it is nonproduct and classically correlated.
Thus the coordinate is executable member by member; neither value is
universally selected.

The node contains no field/CTP factor. An `SR|F` class at this node is therefore
scope-empty, not unknown physics.

```text
FINITE_SOURCE_RECORD_NODES_EXIST = true
  authority: exact finite result

FINITE_S_R_FACTORIZATION_TEST_EXECUTABLE = true

FINITE_COMPLETED_STATE_ALWAYS_NONPRODUCT = false | TYPE-R |
  test: a source state supported in one charge sector gives a product output

FINITE_NODE_HAS_SR_F_COORDINATE = false | TYPE-S |
  scope: the finite carrier contains no field/CTP state
```

### 2.3 `N_out^R` — exact outgoing record-only node

Restriction-compatible positive normalized functionals on the `R_N` define a
unique state `omega_out` on the algebraic inductive limit and its quasi-local
C-star completion. The GNS triple and strongly continuous identity dynamics on
completed records are derived at
`R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md:65-99,175-183`.

```text
R_infinity = inductive_limit_N R_N,
omega_out : R_infinity -> C,
(pi_out,H_out,Omega_out) = GNS(R_infinity,omega_out).
```

This is a record-sector node. The same result explicitly withholds a projective
limit of full source-record states, an infinite-future source Moller unitary,
and a complete source-inclusive GNS (`:22-23,163-183`).

```text
OUTGOING_RECORD_NODE_EXISTS = true

OUTGOING_RECORD_GNS_EXISTS = true

N_OUT_R_IS_COMPLETE_SOURCE_INCLUSIVE_OUTGOING_NODE = false | TYPE-R |
  test: the authority expressly excludes the full source-state limit and
        complete source-inclusive GNS

OUTGOING_RECORD_NODE_HAS_SOURCE_RECORD_FACTORIZATION_VALUE = false | TYPE-S |
  scope: its algebra is R_infinity alone
```

### 2.4 `N_completed^C0` and `N_out^C0` — required full nodes

The doubled influence-functional architecture names a completed physical
source-record-field/CTP object, but no common-origin physical instance exists.
Likewise Parent-State Covariance requires

```text
A_infinity = inductive_limit A_K,
omega_infinity = projective_limit omega_K,
GNS(A_infinity,omega_infinity),
```

with outgoing evolution derived from the same parent
(`PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md:28-55`). Those are requirements,
not present nodes.

```text
FULL_COMPLETED_C0_STATE_NODE_EXISTS = false | TYPE-U |
  missing: StatePort, EffectPort, DynPort, quotient/domain, and common origin

FULL_SOURCE_INCLUSIVE_OUTGOING_NODE_EXISTS = false | TYPE-U |
  would-build: one restriction-compatible projective state system and outgoing
               evolution from the same parent

RECORD_ONLY_OUTGOING_NODE_EQUALS_FULL_OUTGOING_NODE = false | TYPE-R |
  test: different algebras and explicit scope ceiling
```

### 2.5 Node inventory

| Node | Temporal role | Algebra | State standing | Factorization standing | Cumulant standing |
|---|---|---|---|---|---|
| `N_pre^C0` | pre | `A_C0` through a scalar realization | interface only, `TYPE-U`; carrier is `TYPE-P` | `SR|F` split typed, value blocked; global split index `TYPE-S` | completed predicate `TYPE-S` |
| `N_ready,N^SR` | finite input | `A_src tensor R_N` | exact admitted finite family | product on `S|R_N` | no completed-carrier axis |
| `N_N^SR` | finite completed | `A_src tensor R_N` | exact `rho_N` | product or correlated by charge support | no completed-carrier axis |
| `N_out^R` | outgoing record | `R_infinity` | exact `omega_out` and GNS | source/joint split scope-empty | record-only; no joint predicate |
| `N_completed^C0` | full completed | completed joint algebra, not instantiated | `TYPE-U` | `NO_VERDICT` | `TYPE-S` predicate, `TYPE-U` build |
| `N_out^C0` | full outgoing | `A_infinity`, not instantiated | `TYPE-U` | `NO_VERDICT` | `NO_VERDICT` |

## 3. Edge specification

### 3.1 `E_finite,N` — built exact edge

The finite unitary/product of controlled record writes maps

```text
E_finite,N : rho_S tensor ready_N -> rho_N.
```

The source state is charge-superselected; the record inputs are ready-cell
product states; the output is the exact two-block formula above. This edge is
finite, source-record only, and target-independent on its stated construction.

```text
FINITE_STATE_TRANSITION_EDGE_EXISTS = true
FINITE_STATE_TRANSITION_EDGE_IS_FULL_C0_DYNAMICS = false | TYPE-R |
  test: its carrier omits the field/CTP state and full physical effects/domains
```

### 3.2 `E_record,N` and the limit edge — built record restriction

For `A in R_N`, the finite state supplies a compatible record functional.
The inclusions `iota_NM:R_N->R_M` satisfy

```text
omega_M o iota_NM = omega_N,
```

and therefore define `omega_out`. This is a restriction/limit edge on records,
not the full physical evolution.

```text
FINITE_TO_OUTGOING_RECORD_EDGE_EXISTS = true
FINITE_TO_OUTGOING_RECORD_EDGE_PRESERVES_FULL_SOURCE_STATE = false | TYPE-R |
  test: the construction restricts to record observables and expressly does
        not build the source-inclusive limit
```

### 3.3 `Res_N` — required full-to-finite physical descent

An abstract state can be restricted along a certified algebra inclusion, but
the corpus has no physical `rho_pre` instance and no sealed commutative square
identifying its restriction with the ready input used by `E_finite,N`.

A physical edge would have to certify:

```text
Res_N(d_state(Omega)) = rho_S(Omega) tensor ready_N(Omega),
```

on the actual embedded finite algebra, with the same origin and no
post-output supplementation.

```text
FULL_PRESTATE_TO_FINITE_READY_INPUT_CERTIFIED = false | TYPE-U |
  would-build: StatePort instance, finite embedding, marginal/restriction map,
               and common-origin commutative-square certificate
```

### 3.4 `E_joint` — the missing dynamics edge

The exact interface at `U2_008:376-416` is:

```text
DynPort_U2_008 := (
  S_CTP or U_BR[A,g],
  D_dyn,
  action on a scalar realization of C0_008,
  compatibility with U1 orientation/reality conventions,
  consumption of StatePort_U2_008 and EffectPort_U2_008,
  predeclared contact prescription,
  zero-source normalization,
  CTP reality and gauge/source covariance,
  common-origin descent and construction trace,
  output to the doubled complex CTP influence functional
).
```

The complete observable interface is

```text
Z_r[A_+,g_+;A_-,g_-]
 = Tr(E_r U_BR[A_+,g_+] rho_pre U_BR[A_-,g_-]^dagger)
   / Tr(E_r U_BR[0,g_0] rho_pre U_BR[0,g_0]^dagger),
Gamma_r = -i log Z_r.
```

The formula is an architecture. Its common-origin physical instance is absent.
Neither of seam 11's durability-refuted trial potentials fills it.

```text
DYNPORT_U2_008_INTERFACE_COMPLETE = true
DYNPORT_U2_008_PHYSICAL_INSTANCE_EXISTS = false | TYPE-U
DOUBLED_CTP_INFLUENCE_FUNCTIONAL_COMMON_ORIGIN_INSTANCE_EXISTS = false | TYPE-U
```

### 3.5 `E_out^C0` — missing full outgoing edge

Parent-State Covariance requires the finite states and derivations to be
restriction-compatible, the limiting derivation to generate strongly
continuous outgoing evolution, and no outgoing state or generator to be
chosen separately (`PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md:28-55,64-106`).

No present object connects the completed joint state to that limit.

```text
FULL_COMPLETED_TO_OUTGOING_EDGE_EXISTS = false | TYPE-U |
  would-build: covariant finite joint system, projective state limit,
               limiting derivation, and locally normal GNS certificates
```

## 4. Common-origin provenance on the whole path

### 4.1 What the sealed requirements license

The P5 common-origin interface is operational, not merely verbal:

```text
d_state(Omega)    = rho_pre,
d_effect(Omega,r) = E_r,
d_domain(Omega)   = (D_dyn,{D_r}),
d_dynamics(Omega) = U_BR or S_CTP.
```

It also requires one certificate covering carrier identity, state/effect
properties, domain compatibility, dynamics compatibility, covariance and
causality, provenance, and pre-root admissibility
(`STAGE8_P5_COMMON_ORIGIN_DESCENT_REQUIREMENT_V001.md:68-125`).

Parent-State Covariance adds compatible finite restrictions and derivations,
one outgoing limit, and the no-separate-selection rule.

### 4.2 Path-level witness specification

A path-level witness is therefore the tuple

```text
PathCert(Omega) := (
  Omega,
  d_C0, d_U1,
  d_state, d_effect, d_domain, d_dynamics,
  {d_fin,N}, {iota_NM}, d_out,
  Cert_carrier, Cert_state, Cert_effect, Cert_domain, Cert_dyn,
  Cert_restriction, Cert_derivation_covariance, Cert_limit,
  Cert_target_independence, Cert_no_post_output_supplementation
).
```

It must make the following squares commute on every declared finite member:

```text
Res_N(d_state(Omega))
  = rho_S(Omega) tensor ready_N(Omega),

d_fin,N(Omega)
  = E_finite,N[d_dynamics(Omega)](Res_N(d_state(Omega))),

omega_M(Omega) o iota_NM
  = omega_N(Omega),

d_out(Omega) o iota_N
  = omega_N(Omega),

delta_M(Omega) o iota_NM
  = iota_NM o delta_N(Omega)
```

on stabilized interior observables, with any boundary correction derived from
the same parent. The trace is frozen before any response output; no state,
effect, domain, boundary rule, or outgoing generator may be appended later.

This is what “common origin on the path” means. Merely placing separately
declared objects on `C0_008` does not satisfy it.

```text
PATH_LEVEL_PROVENANCE_WITNESS_SPECIFIED = true
PATH_LEVEL_PROVENANCE_WITNESS_INSTANTIATED = false | TYPE-U

PARENT_STATE_COVARIANCE_ALONE_INSTANTIATES_PATH = false | TYPE-R |
  test: it is an adopted selection/falsification principle whose own flags
        retain parent_to_outgoing_limit_derived = false

COMMON_CARRIER_COLOCATION_EQUALS_COMMON_ORIGIN = false | TYPE-R |
  test: the sealed P5 requirement demands executable descent maps and one trace
```

## 5. The cumulant axis

### 5.1 What exists

The adopted source branch defines a gauge-invariant quasifree state on
`CAR(H_src)`. On that source algebra, ordinary source-field moments are fixed
by the two-point covariance via graded Wick/Pfaffian relations. Composite
current cumulants need not vanish; they are determined by the two-point data
(`STAGE8_TASK2D_QUASIFREE_BRANCH_RHO_PRE_GOVERNANCE_AUDIT_V001.md:223-270,371-400`).

That result does not transport to `rho_pre` or the completed carrier. V004
types `rho_pre` only by full-carrier positivity, trace class, and normalization.

### 5.2 What a completed predicate would have to contain

The following is a **HYPOTHETICAL INTERFACE ONLY; it is not an asserted
predicate and none of its missing fields is assigned by this artifact**:

```text
QF_C0[omega] requires (
  Gen_C0,                 # named response-generating set on A_C0
  Ord_CTP,                # U1-compatible contour ordering
  Cov_omega on Gen_C0,    # complete two-point covariance
  Wick_C0,                # graded ordered moment rule on the chosen generators
  ResponseMap,            # proof that physical response factors through Cov
  DomainCert,
  CommonOriginCert
).
```

Only after these objects exist could one state the candidate predicate

```text
QF_C0(omega) iff all Ord_CTP-ordered moments of Gen_C0 obey Wick_C0 and the
physical response is determined by Cov_omega on the certified domain.
```

That displayed line is a would-be definition, not a corpus verdict. It imports
the standard quasifree/Wick pattern already used on the source CAR, but its
transfer to the mixed completed carrier is unproved. `finitely-correlated`
has no sealed transfer object, filtration, bond bound, or response predicate.

```text
COMPLETED_CARRIER_QUASIFREE_PREDICATE_FOUND = false | TYPE-S |
  roots/exclusions/queries: Section 1.4

SOURCE_CAR_QUASIFREE_PREDICATE_TRANSPORTS_TO_C0 = false | TYPE-R |
  test: different algebras; no extension/descent map or joint covariance exists

COMPLETED_CARRIER_QUASIFREE_PREDICATE_BUILT = false | TYPE-U |
  would-build: Gen_C0, Ord_CTP, joint covariance, Wick rule, response
               factorization, domains, and common-origin certificate

FINITELY_CORRELATED_COMPLETED_PREDICATE_FOUND = false | TYPE-S |
  scope: the exact and cognate searches found labels but no executable
         completed-carrier definition

CUMULANT_AXIS_VALUE_SET_EXISTS = false | TYPE-U |
  would-build: executable predicates plus a proved residual/complement class
```

## 6. Is the forcing protocol runnable?

No. Protocol step 1 requires a frozen family of **instantiated candidate
paths**, not a product of schemas or a singleton declared after the desired
output is known.

Present corpus objects do not compose end to end:

1. `N_pre^C0` is an uninstantiated role;
2. `E_finite,N` starts from a narrower ready source-record input whose descent
   from `N_pre^C0` is uncertified;
3. `N_out^R` is record-only;
4. `E_joint`, `N_completed^C0`, `E_out^C0`, and `N_out^C0` are absent;
5. the completed cumulant predicates needed to type a node are absent; and
6. no coverage proof enumerates all admitted common-origin paths.

```text
PROTOCOL_STEP1_COMPLETE_PATH_FAMILY_DECLARABLE = false | TYPE-C |
  constraint: no instantiated end-to-end path member exists

PROTOCOL_STEP1_SINGLETON_BY_DECLARATION_ALLOWED = false | TYPE-R |
  test: Q-200 requires instances; declaring one schema does not prove coverage

PROTOCOL_STEPS_2_THROUGH_5_EXECUTED = false | TYPE-C |
  constraint: mandatory stop at step 1

SURVIVOR_COUNT = NO_VERDICT
STATE_CLASS_REQUIRED = NO_VERDICT
```

### 6.1 Minimal build order

The smallest **first** build is:

```text
B1  one common-origin doubled CTP influence-functional instance on C0_008,
    jointly instantiating StatePort_U2_008, EffectPort_U2_008,
    DynPort_U2_008, domains, contacts, and the physical completion node.
```

It is the same interface needed by U2, Task 3a, Task 3c, and this envelope.
This is why it is one gap with four consumers.

To make the forcing protocol runnable, B1 must be followed by:

```text
B2  certified restriction/transition/limit maps connecting B1 to the exact
    finite nodes and a full outgoing node, all in one PathCert;

B3  executable completed-carrier class predicates, including Gen_C0 and the
    response-relevant quasifree/finitely-correlated distinction;

B4  a frozen target-independent manifest of instantiated complete paths and a
    coverage proof over the admitted path family.
```

B1 is minimal for an **instance**. B1-B4 are minimal for a **runnable forcing
protocol**. Conflating those two minima would reproduce the coverage defect
that stopped Q-200.

## 7. Negative ledger — DoR-006 typing

| Negative | Type | Exact scope/reason |
|---|---|---|
| Complete transition envelope instantiated | `TYPE-U` | Full state/dynamics/outgoing path unbuilt |
| Joint dynamics edge instantiated | `TYPE-U` | `DynPort_U2_008` interface exists; physical influence-functional instance does not |
| End-to-end full-carrier state path exists | `TYPE-U` | Full completed and outgoing nodes/edges absent |
| Forcing protocol runnable now | `TYPE-C` | Step 1 cannot declare complete instantiated paths |
| Prior placeholder `G_joint` is the BID comparison group | `TYPE-R` | Signature/codomain mismatch; symbol collision |
| Completed response generator set found | `TYPE-S` | Scoped whole-program and archive search |
| Pre-state instance exists on `C0_008` | `TYPE-U` | Scalarization, trace, density, and provenance missing |
| Pre-state factor value assigned | `TYPE-C` | No state instance to test |
| Universal factorization index frozen | `TYPE-S` | Inequivalent splits used; no selector found |
| Finite completed state always nonproduct | `TYPE-R` | Single-sector support yields product output |
| Finite node has `SR|F` coordinate | `TYPE-S` | Field/CTP state absent from that carrier |
| Record-only outgoing node is full source-inclusive node | `TYPE-R` | Different algebras and explicit scope ceiling |
| Full completed state node exists | `TYPE-U` | Common-origin ports and quotient/domain missing |
| Full outgoing state node exists | `TYPE-U` | Projective state limit and limiting evolution missing |
| Finite edge is full C0 dynamics | `TYPE-R` | Narrow source-record carrier only |
| Record limit preserves full source state | `TYPE-R` | Construction restricts to record observables |
| Full pre-state to finite ready input certified | `TYPE-U` | Physical restriction/descent square absent |
| Full completed-to-outgoing edge exists | `TYPE-U` | Covariant joint limit unbuilt |
| Path provenance witness instantiated | `TYPE-U` | No one-root descent trace/certificates |
| Parent-State Covariance alone instantiates the path | `TYPE-R` | Principle requires but does not construct its objects |
| Common carrier co-location equals common origin | `TYPE-R` | P5 demands executable descent maps and one trace |
| Completed-carrier quasifree predicate found | `TYPE-S` | Source predicate does not reach completed carrier |
| Source quasifree predicate transports to C0 | `TYPE-R` | Algebra/domain mismatch; no transport map |
| Completed-carrier quasifree predicate built | `TYPE-U` | Generator, covariance, Wick/response/domain certificates absent |
| Finitely-correlated completed predicate found | `TYPE-S` | No executable definition in entered roots |
| Cumulant-axis value set exists | `TYPE-U` | Predicates and residual coverage unbuilt |
| Step-1 singleton by declaration is lawful | `TYPE-R` | Schema is not an instantiated covered family |
| Protocol steps 2-5 executed | `TYPE-C` | Mandatory stop at failed step 1 |

No `TYPE-P` claim is promoted to unconditional derived physics. `TYPE-C`
appears only on checks blocked by named prerequisites. `TYPE-S` negatives state
their search/object scope. No missing item is typed `TYPE-R` merely because it
is missing.

## 8. Custody and scope close

This artifact specifies an interface. It does not construct a state, dynamics,
effect, quotient, measure, response, covariance, survivor, or physical
functional. It does not select a state class. It does not compute alpha,
`kappa_record`, a coupling, a scale, a root, an eigenvalue, a beta function,
`E_R`, `T_R`, `k_R`, or an absolute interval. It makes no measured comparison
and does not choose the Misner-Sharp/Brown-York fork.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
