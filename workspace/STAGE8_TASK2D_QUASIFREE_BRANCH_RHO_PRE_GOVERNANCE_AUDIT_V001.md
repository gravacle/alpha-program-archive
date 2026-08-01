# Stage 8 Task 2d Quasifree-Branch `rho_pre` Governance Audit v001

Date: 2026-08-01  
Lane: Codex lane 1  
Task: 2d  
Register head at construction start: Q-222

## Lead determination

**The adopted stationary quasifree branch does not govern the completed
physical `rho_pre`. It governs the free source-CAR in-state and derives its
free contour.**

This is a scoped physical branch input, not merely a computational device. Its
scope is nevertheless decisive. The branch fixes the source covariance from
the positive/negative spectral projectors of `h_0`; conditional on that
disclosed branch, the source quasifree state and source-sector GNS are
constructed. It does not supply a state on the completed source-record-field
CTP carrier.

Two later authorities state the stop directly:

1. `STAGE8_GAMMA_K_QUASIFREE_ROOT_ROUTE_ATTEMPT_V001.md:163-217` returns
   `STEP_3_DIFFERENT_ALGEBRA`; and
2. `STAGE8_CTP_PHYS_INPUT_PACKAGE_U2_DOR008_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md:254-285`
   says that the source-sector quasifree state is not transported to the
   field/CTP factor, completed joint density, or effects.

The active v004 response functional does not retire the source branch. It also
does not carry its quasifree restriction into the full `rho_pre`: v004 requires
only a positive normalized trace-class density on the full
source-record-field Hilbert space. Q-219 proves that the currently executable
positivity, normalization, U1-reality, and one-cell constraints leave a
continuum.

There is also a name/type trap. The adopted **Global Boundary Descent /
Quasi-Free Completeness** principle is a restriction on the primitive
source-record **generator**. Its own text says it does not select a continuum
vacuum, CTP state, durability state, or clustering state. It cannot be used as
a state-selection law.

Therefore Q-222's new-physics ask does not collapse to an already fixed
two-point function on the ratified carrier. The source-source covariance is
fixed inside the disclosed branch; the joint field/record covariance,
cross-sector correlations, and common-origin physical state remain unbuilt.
D6 remains a principal-level physical-input question, now honestly narrowed:
derive or adopt the response-relevant joint state/covariance class on the
ratified carrier and its common-origin relation to the dynamics.

```text
SOURCE_QUASIFREE_BRANCH_IS_MERE_COMPUTATIONAL_DEVICE = false | TYPE-R |
  test: Stage 6/7 and the parent spec call it disclosed ordinary-branch state
        content and physical incoming boundary data

SOURCE_QUASIFREE_BRANCH_CURRENT_SCOPE = FREE_SOURCE_CAR_AND_FREE_CTP

SOURCE_QUASIFREE_BRANCH_GOVERNS_COMPLETED_RHO_PRE = false | TYPE-R |
  test: the source state and completed rho_pre have different algebras and
        domains, and the current U2 authority explicitly denies transport

V004_PROMOTES_SOURCE_QUASIFREE_STATE_TO_FULL_RHO_PRE = false | TYPE-R |
  test: v004 types rho_pre only by full-carrier positivity, trace class, and
        unit trace; Q-219 exhibits a continuum satisfying the executable
        completed-carrier constraints

GLOBAL_QUASI_FREE_COMPLETENESS_SELECTS_RHO_PRE = false | TYPE-R |
  test: its defining artifact restricts the primitive generator and expressly
        withholds continuum-vacuum and CTP-state selection

COMPLETED_RESPONSE_RELEVANT_QUASIFREE_STATE_CLASS_DERIVED = false | TYPE-U |
  would-build: one common-origin state construction on the ratified carrier
               that fixes its joint covariance and proves the required
               response-cumulant reduction

CONSTRUCTION_VERDICT = SOURCE_BLOCK_FIXED__COMPLETED_RHO_PRE_NOT_GOVERNED__D6_REMAINS
```

No physical state, covariance extension, response, or value is selected or
evaluated here.

## 1. Preflight, scope, and method

### 1.1 Three-line preflight

```text
DOES_THE_OBJECT_EXIST = YES
  object: the stationary quasifree source-state branch and its claimed P5 role

IS_THE_VERSION_CURRENT = YES_AT_SOURCE_SCOPE__NO_PROMOTION_TO_FULL_RHO_PRE
  basis: current inventory retains the source-sector state; Q-222 and U2_008
         retain the completed-state question

ARE_THE_INPUTS_PRESENT = YES_FOR_STANDING_AUDIT__NO_FOR_COMPLETED_STATE_BUILD
  present: source covariance, source CAR/GNS, ratified carrier, U1 constraints
  absent: joint covariance, completed density, effects, common-origin map
```

### 1.2 Frozen authorities

| Authority | SHA-256 | Use |
|---|---|---|
| `R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md` | `40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9` | Source-state and spectral-projector scope |
| `BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001.md` | `6f6b822ac8ccf9ea19659f4ccf811268f60a27a361f817ee6513479d63b62546` | Free source contour and status flags |
| `STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V002.md` | `7995f6fda75e78795cbfe167f8c8df634170ea3b43affd5bbe6e22bcda8f6ffe` | Current disclosed-input classification |
| `STAGE7_QSPEC_REVIEW_CANDIDATE_V002.md` | `5026afb89b52ead9f309168cb2fa4f06b81039f8dd01b8940f40e64aad679a7e` | Ordinary-branch state and open interacting CTP scope |
| `STAGE7_QSPEC_SCOPE_AND_PREMISE_SUCCESSOR_V001.md` | `202f8d8db60046a8069b1cd8fcc38f505eb95fa29578e094e005f56e967c3a35` | State disclosed, free contour derived |
| `STAGE8_ROUTE2_COMPLETE_QSPEC_STATE_BINDING_V001.md` | `5cbcd28ee493ba43e3d36158d80c4202230f056808caf2b36420f08c38fbd0d7` | Finite source-record binding and ceiling |
| `STAGE8_GAMMA_K_QUASIFREE_ROOT_ROUTE_ATTEMPT_V001.md` | `8980666fa51350fa3f794748a84c28941bbc641083ba49df90a27311c35bc6ee` | Source GNS construction and different-algebra stop |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_U2_DOR008_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md` | `2b6291227b7ac5967796014c2ad217c9eb084b5bb6df23fed0a7bca464e8bfab` | Current state port and explicit nontransport |
| `STAGE8_SECTION53_P5_AXIS_COVERAGE_AND_EXCLUSION_AUDIT_V001.md` | `1274b1b71b46e6a34b641c0053d61ce1ed16c94e8d570317a7831f558bcfef58` | P5 state/contour branch ledger |
| `STAGE8_FROZEN_PRIMITIVE_INVENTORY_PREFREEZE_RESULT_V001.md` | `476baa18b1e2e97f8b8c8a349bf803627f53c47224b030f538527848f3fb8deb` | Current source-sector object classification |
| `BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md` | `949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd` | Generator-class homonym check |
| `STAGE8_TASK2D_SCALARIZATION_FUNCTIONAL_FORCING_PROTOCOL_RESULT_V001.md` | `d13920e2a7687ac53a896e70cd0d12168f74fe0f368425179a455a8ae249ae98` | Q-219 continuum and nonselecting constraints |
| `STAGE8_RESPONSE_STATE_FACTORIZATION_TEST_FIXTURE_RESULT_V001.md` | `e8ce5095f02d8291b43350880fff40b0362d1c81f2d1bbc5b51b41db3926d770` | Q-222 localized response sensitivity |
| `PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md` | `532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb` | Same-parent candidate principle |
| `R3_4_PARENT_STATE_COVARIANCE_ADJUDICATION_RESULT_V001.md` | `34faec38fbbe5c958bc71fcde9314b6d9f34186a82051f17ab35428d1331635d` | Current parent fails that principle |
| `primitive_record_cell_selection_principle_v004.md` | `13d227ceb2198d96b0e4e2fef57b874cea71cb755320508fbf4c6d64a00c507e` | Active full-state response signature |
| `primitive_zero_bare_induced_response_projection_principle_v004.md` | `d386bb74c28424a55a68a1bdb78108711537a7bc36ffffd1a76fe5ffd8a4eb80` | Active zero-bare state signature |

### 1.3 Roots and exclusions

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
mirrored duplicates when a byte-identical cleanroom authority was available
response evaluation and physical-state construction
```

No private-custodian path was entered.

### 1.4 Queries

Word-boundaried, case-insensitive searches included:

```text
stationary quasifree | quasi-free state | quasifree state | covariance
positive-energy state | spectral projector | free CTP | full CTP matrix
rho_pre | state port | state descent | source-record-field
KMS | FDT | Tomita | passivity | vacuum selection | ground state
Hadamard | extremality | thermal state | Gibbs state | clustering state
Parent-State Covariance | Quasi-Free Completeness | state selection
supersede | successor | retire | withdraw | current | live
```

The audit treats a state on `CAR(H_src)`, a product state on a finite
source-record algebra, and a density on the completed source-record-field CTP
carrier as different typed objects unless a sealed transport map relates them.

## 2. Exact standing through the lineage

### 2.1 Parent and free subgate

`R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md:148-151`
states:

> The source state is the stationary quasifree state of `h_0`, with any
> declared finite-energy incoming excitation treated as boundary data.

At `:228-232`, the asymptotic state is fixed by the positive/negative spectral
projectors of the same `h_0`, while finite-energy source excitation remains
variable boundary data.

`BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001.md:32-79` fills the
negative-energy spectral subspace, leaves the positive-energy subspace empty,
and derives the greater, lesser, time-ordered, anti-time-ordered, retarded, and
advanced **free source** propagators. Its status block at `:107-124` says:

```text
stationary_quasifree_state_disclosed = true
complete_free_quasifree_CTP_contour_derived = true
physical_durability_derived = false
gauge_invariant_dressed_source_spectrum_derived = false
interacting_isolated_pole_proved = false
```

This is the first decisive status split: state choice disclosed; free contour
derived conditional on it; interacting physical state not supplied.

### 2.2 Stage 6/7 successor standing

`STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V002.md:42-56` lists the stationary
quasifree in-state of `h_0` among **disclosed branch and standard inputs**.
At `:58-75`, it lists the free contour as derived and states that the free
in-state itself is disclosed, not derived.

`STAGE7_QSPEC_REVIEW_CANDIDATE_V002.md:60-63,176-200` repeats that the state is
disclosed ordinary-branch content, derives the free contour from its spectral
projectors, and leaves the normalized interacting CTP amplitude and
gauge/ghost/edge measure open.

`STAGE7_QSPEC_SCOPE_AND_PREMISE_SUCCESSOR_V001.md:160-170` gives the same
classification and explicitly withholds intermediate interacting
implementability.

The branch is therefore a physical branch law at source/free scope. It is not
merely a regulator convenience. Its disclosed/adopted status also means the
choice of this branch is not theorem-derived.

### 2.3 What is derived inside the branch

`STAGE8_GAMMA_K_QUASIFREE_ROOT_ROUTE_ATTEMPT_V001.md:121-150` constructs the
source covariance

```text
C(p)=(I-h_0(p)/|p|)/2,
```

defines `A_src=CAR(H_src)`, and fixes the gauge-invariant quasifree state by

```text
omega_C(a^*(f)a(g))=<g,Cf>,
omega_C(a(f)a(g))=0,
omega_C(a^*(f)a^*(g))=0,
```

with all even source moments given by the CAR determinant/Pfaffian rule. The
source GNS triple follows. The `p=0` representative is irrelevant to the
continuum multiplication operator because it is a measure-zero set.

Thus the source two-point function is a point, not a continuum, **conditional
on the disclosed positive-energy branch and `h_0`**. The branch selection is
adopted; the covariance-to-state construction is derived within it.

### 2.4 Route-2 finite source-record binding

The strongest apparent counterexample to the scope boundary is
`STAGE8_ROUTE2_COMPLETE_QSPEC_STATE_BINDING_V001.md:23-54`. It combines the
source quasifree state with ready record factors and calls the product the
already-disclosed `omega_in` on the complete source-record algebra.

Its own ceiling at `:56-76` withholds the interacting continuum CTP amplitude,
source-inclusive projective-limit state, regulator independence, linked
cluster density, response coefficient, and unique interacting-vacuum
derivation. It has no field/CTP factor. It is therefore a real finite/algebraic
binding, not transport to v004's `rho_pre`.

### 2.5 Active v004 and ratified carrier

The active response authority,
`primitive_record_cell_selection_principle_v004.md:17-68`, asks for

```text
rho_pre >= 0,
rho_pre trace-class on the full source-record-field Hilbert space,
Tr rho_pre=1,
```

inside the inclusive CTP trace. It states no quasifree condition.
`primitive_zero_bare_induced_response_projection_principle_v004.md:24-49`
likewise assumes only normalization and leaves the physical `Log_0`
neighborhood and induced response as later outputs.

This v004 reformulation supersedes earlier **response typing**, not the
source/free-state branch. It neither declares the source branch retired nor
supplies a map from the source state to the full `rho_pre`.

The current carrier authority makes that absence affirmative rather than an
argument from silence. At
`STAGE8_CTP_PHYS_INPUT_PACKAGE_U2_DOR008_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md:254-285`,
the physical state port requires `omega_phys`, a scalar Hilbert realization,
`rho_pre`, a state domain, descent map, and provenance certificate. Lines
`:276-279` state that the source-sector quasifree state is **not transported**
across this gap and supplies neither the field/CTP scalarization nor the joint
density or effects.

### 2.6 Current inventory

`STAGE8_FROZEN_PRIMITIVE_INVENTORY_PREFREEZE_RESULT_V001.md:176-188` lists the
source Hilbert space, source CAR, source quasifree state, and source-sector GNS
as real derived **sectoral** objects and expressly excludes record factors,
field degrees, quotient, measure, `S_CTP`, effects, and the raw response map.

The source branch remains live at exactly that scope. It is neither retired nor
promoted.

## 3. Does the branch govern `rho_pre`?

No.

The proposition tested is:

```text
Every admissible physical rho_pre on the ratified source-record-field CTP
carrier is the extension of omega_C and is quasifree on all response-coupled
generators.
```

It fails the existing type test before any state census:

1. `omega_C` has domain `CAR(H_src)`.
2. Route 2 reaches a finite source-record algebra but no field/CTP factor.
3. v004's `rho_pre` is a density on the full physical source-record-field
   carrier.
4. U2_008 expressly supplies no transport, joint density, or effects.

```text
SOURCE_STATE_DOMAIN = CAR(H_src)
ROUTE2_STATE_DOMAIN = FINITE_SOURCE_RECORD_ALGEBRA
RHO_PRE_DOMAIN = COMPLETED_SOURCE_RECORD_FIELD_CTP_CARRIER

SEALED_STATE_TRANSPORT_SOURCE_TO_RHO_PRE = false | TYPE-U |
  would-build: a common-origin positive state extension preserving the source
               covariance and fixing the field, record, and cross-sector
               covariance blocks on the ratified carrier
```

The P5 census phrase “adopted CTP state/contour branch” does not overcome this
typing. Its own row at
`STAGE8_SECTION53_P5_AXIS_COVERAGE_AND_EXCLUSION_AUDIT_V001.md:266-274` says
the full CTP matrix is open and the completed Hilbert/quotient is not built.
At `:288-304` it says alternative states/contours are not excluded and names
either a uniqueness derivation or an explicit branch-conditional adoption as
the decider.

## 4. What the source branch actually constrains

The following inventory does not run the next census. It identifies the
failure-capable constraints and their present reach.

| Constraint | Exact reach | Current survivor shape |
|---|---|---|
| Stationarity under `h_0` | Source CAR only | By itself nonunique: distinct spectral functions can commute with `h_0` |
| Disclosed positive-energy filling | Source CAR only | Selects the negative-energy projector covariance `C` within the branch |
| Gauge-invariant source quasifree rule | Source CAR only | Sets anomalous two-point functions to zero and all source moments by Wick/Pfaffian data |
| Finite regulator restriction `C_n=Q_n C Q_n` | Source finite restrictions | Derives compatible finite source states away from the measure-zero `p=0` representative |
| U1 branch/reality compatibility | Ratified field/CTP factor | Leaves a continuum; Q-219 gives explicit fixed-point states |
| Positivity, trace class, and unit trace | Full state role | Existence/type constraint only; leaves a continuum |
| One-cell tensor-unit restriction | Ratified carrier face | Passes every normalized Q-219 candidate; selects no state |
| Record effects and instruments | Record-probability sector | Concrete effects and common-origin domains are absent; no state selector follows |
| Parent-State Covariance | Full common-origin route | Requires same-parent state/dynamics descent; current parent is blocked and no identity is selected |

`STAGE8_T7_RELAYED_CONNECTED_PREPARATION_RETEST_RESULT_V001.md:51-60`
supplies the direct nonuniqueness control: stationarity and charge
superselection alone do not select a unique charged in-state when the charged
sector has dimension greater than one.

`STAGE8_TASK2D_SCALARIZATION_FUNCTIONAL_FORCING_PROTOCOL_RESULT_V001.md:303-430`
then proves that positivity/normalization, U1 compatibility, and the one-cell
restriction leave a continuum of ratified-carrier scalarizations intact. It
does not promote that continuum to a continuum of physical `rho_pre`
instances; physical placement remains unbuilt.

The net shape is therefore:

```text
SOURCE_TWO_POINT_WITHIN_DISCLOSED_BRANCH = ONE COVARIANCE C
COMPLETED_JOINT_TWO_POINT_ON_RATIFIED_CARRIER = UNBUILT
RATIFIED_CARRIER_SCALARIZATION_SURVIVORS = CONTINUUM
PHYSICAL_RHO_PRE_SURVIVOR_SET = NO_VERDICT
```

## 5. Cumulant typing correction

The relay's motivating statement needs a scope qualification.

**Imported standard CAR mathematics:** for a quasifree state, truncated
correlators of the fundamental linear CAR fields vanish above second order,
and all ordinary source-field moments are determined by the two-point
covariance.

That does not imply that all connected response cumulants of composite
observables vanish. A one-mode CAR check already gives a counterexample: for
`n=a^*a` in a quasifree state with `omega(n)=p`, the projection identity
`n^k=n` gives the third cumulant

```text
kappa_3(n)=p-3p^2+2p^3=p(1-p)(1-2p),
```

which is not identically zero as a function of the admissible covariance
entry `p`. This is imported standard CAR probability algebra, not a physical
state choice for this program.

The charged connection couples through the bilinear Dirac current; connected
current cumulants can therefore be nonzero even in a quasifree fermionic
state, although Wick's rule determines them from the fermion two-point
function. The sealed current is bilinear,
`j^mu=:bar(psi) gamma^mu psi:`, at
`BID_GLOBAL_CAR_CHARGE_AND_ACTIVATION_DERIVATION_V001.md:14-25`.

Accordingly, if a joint quasifree physical state were derived, it could reduce
the independent **state data** needed for response to a two-point covariance.
It would not by itself prove that every higher composite-current response
cumulant vanishes. Q-222 concerns the connected second-response operator, so
the two-point covariance is the immediate relevant datum there.

```text
QUASIFREE_FUNDAMENTAL_FIELD_MOMENTS_FIXED_BY_TWO_POINT = true |
  standing: imported standard CAR/Wick mathematics already used by the source
            GNS construction

QUASIFREE_IMPLIES_ALL_COMPOSITE_RESPONSE_CUMULANTS_VANISH = false | TYPE-R |
  test: Wick contraction of bilinear current insertions admits connected loop
        contractions beyond second source-field order
```

This correction does not add a physical state premise. It prevents a
fundamental-field Gaussian statement from being transported to the composite
response without a proof.

## 6. Candidate-principle sweep

### 6.1 Stationary positive-energy quasifree branch

This is the strongest existing candidate. It is already adopted/disclosed and
fixes the source covariance. It remains only a candidate for the full P5 state
because no joint extension or common-origin certificate is supplied.

### 6.2 Parent-State Covariance

`PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md:15-55` requires one parent to
supply the algebra, state, derivation, record algebra, and root data as a
covariant system. At `:64-81` it forbids choosing a continuum vacuum, state,
generator, spectral density, or regulator separately.

It is a common-origin and compatibility principle, not a formula for the state
identity. `R3_4_PARENT_STATE_COVARIANCE_ADJUDICATION_RESULT_V001.md:3-10,47-65`
says the current parent does not pass it and exhibits two covariant local nets
with different responses. It does not fix the joint covariance.

### 6.3 Global Boundary Descent / Quasi-Free Completeness

This is not another state candidate. Its definition at
`BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md:12-25` requires
the primitive connected action to be the operator-valued CAR lift of the
one-particle boundary superconnection. Lines `:115-151` constrain the
generator and reject a primitive quartic competitor inside the adopted class.

The same artifact says at `:153-166` that it does **not** select a continuum
vacuum, CTP state, durability sector, or clustering state. Similar vocabulary
does not establish object identity.

### 6.4 KMS, vacuum/passivity, extremality, and thermal alternatives

The bounded sweep found no sealed KMS/FDT/Tomita, passivity, Hadamard,
extremality, Gibbs, or thermal-state rule that governs the completed
`rho_pre`. `STAGE8_ONE_OPERATOR_PREMISE_ADJUDICATION_EINSTEIN_V001.md:195-208,270-284`
independently records the KMS/FDT/Tomita instrument as an undeployed import.

Thermal, ground-state, entangled, product, and clustering preparations are
named as response-distinguishable alternatives at
`BID_FULL_STACK_REVIEW_LEDGER_V003.md:325-348`; no selector is attached.

```text
COMPLETED_RHO_PRE_KMS_PASSIVITY_EXTREMALITY_SELECTOR_FOUND = false | TYPE-S |
  roots: gravity_emergence_evidence_program;
         alpha_fundamental_record_action_cleanroom_v003;
         alpha-program-archive/workspace;
         alpha-program-archive/cleanroom_output;
         alpha_supervision |
  excl: a32_holdout/custodian_private; .git; external; third_party;
        mirrored duplicates |
  query: KMS; FDT; Tomita; passivity; passive state; Hadamard;
         vacuum selection; ground state; extremal state; extremality;
         thermal state; Gibbs state; state selection
```

### 6.5 Full candidate set at current resolution

The state-facing candidate set is therefore not empty and not selected:

```text
1. adopted free source positive-energy quasifree branch, requiring a lawful
   joint extension before it can govern rho_pre;
2. Parent-State Covariance, requiring a common-origin parent construction;
3. explicitly open alternative CTP state/contour and preparation classes;
4. new principal-authored physical input, if no derivation selects among them.
```

No existing candidate supplies a concrete joint state on the ratified carrier.

## 7. Consequence for D6

D6 should not ask the principal to author an unconstrained arbitrary density
matrix. The source marginal is already fixed in the disclosed branch. It also
must not tell the principal that only one source two-point function remains.
The unfinished object has at least these components:

```text
JOINT_STATE_CLASS:
  whether the completed physical state is quasifree on the response-coupled
  algebra, or belongs to another class;

JOINT_COVARIANCE:
  field/CTP, record, and cross-sector two-point blocks extending omega_C;

COMMON_ORIGIN:
  derivation of that state/covariance from the same microscopic source as the
  dynamics and effects;

RESPONSE_REDUCTION:
  proof of which physical response cumulants are fixed by the chosen state
  data, including composite-current rather than only linear-field cumulants.
```

If the principal adopts a completed quasifree branch, that is a new physical
scope extension, not execution of the old source branch. If instead a common
parent derives the joint covariance, D6 becomes a derivation target. Nothing
currently sealed decides between those routes.

## 8. Counterexample hunt

Three plausible affirmative arguments were tested and failed:

1. **“The branch is called a CTP state/contour branch, so it is `rho_pre`.**”
   The P5 row itself says the full CTP matrix and completed carrier are open.
2. **“Route 2 already binds the complete state.”** Its complete object is the
   finite source-record algebra; its own ceiling withholds interacting
   continuum and source-inclusive projective state.
3. **“Quasi-Free Completeness forces a quasifree state.”** The principle's
   object is the primitive generator, and it expressly withholds state
   selection.

The negative result is therefore not an argument from missing search hits. It
is a domain/codomain and scope refutation grounded in explicit successor text.

## 9. Final verdict

```text
BRANCH_STANDING = DISCLOSED_ADOPTED_ORDINARY_SOURCE_STATE_BRANCH
DERIVED_INSIDE_BRANCH = SOURCE_COVARIANCE__SOURCE_QUASIFREE_STATE__FREE_CTP
RHO_PRE_GOVERNANCE = DOES_NOT_REACH
V004_EFFECT = SOURCE_BRANCH_NOT_RETIRED__FULL_STATE_NOT_QUASIFREE_TYPED
SOURCE_TWO_POINT_SURVIVOR_SHAPE = POINT_CONDITIONAL_ON_DISCLOSED_BRANCH
RATIFIED_CARRIER_SCALARIZATION_SURVIVOR_SHAPE = CONTINUUM
PHYSICAL_RHO_PRE_SURVIVOR_SHAPE = NO_VERDICT
D6_DISPOSITION = PRINCIPAL_PHYSICS_QUESTION_REMAINS__NARROWED_TO_JOINT_STATE_COVARIANCE_CLASS
```

## 10. Custody and terminal fences

The lane created this append-only artifact and its hash sidecar, verified the
sidecar, and mirrored only those public files to the archive workspace. It did
not register, baseline, commit, push, or deploy.

```text
alpha_computed = false [TERMINAL_FENCE_DECLARATION]
proof_authorized = false [TERMINAL_FENCE_DECLARATION]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION]
coupling_evaluation_authorized = false [TERMINAL_FENCE_DECLARATION]
production_authorized = false [TERMINAL_FENCE_DECLARATION]
```

No physical state, covariance extension, response, coupling, scale, root,
spectrum, eigenvalue, beta function, interval, or measured comparison was
computed or selected. No register, ruling, source authority, or prior artifact
was edited. No git command was run.
