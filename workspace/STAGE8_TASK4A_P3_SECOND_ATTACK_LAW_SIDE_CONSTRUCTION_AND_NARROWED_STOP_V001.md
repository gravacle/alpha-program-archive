# Stage 8 Task 4a P3 Second Attack: Law-Side Construction and Narrowed Stop V001

Date: 2026-08-02  
Task: 4a / P3 second attack  
Lane: Codex lane 2  
Status: CERTIFIED LAW-SIDE SUBPACKAGE BUILT; COMPLETE U3 INSTANCE REMAINS UNBUILT

Marks on premise-dependent positives:

```text
TYPE-P | premises: DoR-008, DoR-009, DoR-013, DoR-014
```

Gates: `alpha_computed=false`; `proof_authorized=false`;
`kappa_record_computed=false`.

## 0. Lead determination

**The law-side attack does not build any of the four missing U3 fields. It
does sharpen every stop and constructs the maximal law-generated subpackage.**
The four proposed identifications fail at their type boundaries:

1. `C7` is pullback consistency of amplitudes along the **zero section**; it is
   not Kolmogorov marginal consistency of measures under a projection. The
   law supplies a contravariantly compatible cylinder-amplitude family, not a
   branch-joint prequotient measure.
2. DoR-009 calls `E_post` a time-oriented endpoint-charge assignment: charge
   follows the write. It does not supply an epsilon-indexed analytic operator,
   a pole/boundary-value rule, or a limiting topology. It constrains a future
   contour but does not construct one.
3. The finite sequential glue has two honest completions: the P2 norm source
   completion and PathCert's outgoing **record-only** GNS direct limit. Their
   joint law-side receipt is built below. Neither is the complete physical CTP
   boundary/edge package.
4. `GNS_out` represents the outgoing record algebra by bounded operators. No
   named unbounded physical endpoint operator descends to it. Dense finite GNS
   vectors therefore cannot be certified as a common invariant core, and
   pure phase does not prove essential self-adjointness of an absent operator.

The maximal new receipt is

```text
P3_LAW_SIDE_SUBPACKAGE := (
  OscCyl={Fbar_N,Abar_N^[A],j_NM^Q},
  EpostEndpointOrientation,
  BdGlue_law_src,
  BdGlue_law_rec,
  Dom_bdd,GNS_out,
  CommonOriginTrace
).
```

It is exact and restriction-compatible, but it has the wrong or incomplete
signature at all four U3 ports.

```text
P3_LAW_SIDE_SUBPACKAGE_BUILT = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

P3_MEASURE_BUILT = false | TYPE-U |
  would-build: actual finite branch-joint measures or complex measures with
               marginal consistency, then completed descent q_*nu
P3_INTERACTING_CONTOUR_BUILT = false | TYPE-U |
  would-build: common-origin epsilon-indexed analytic operator family,
               insertion/boundary-value rule, domains, and limit topology
P3_COMPLETE_BOUNDARY_EDGE_BUILT = false | TYPE-U |
  would-build: completed joint physical carrier and preparation/boundary data
P3_UNBOUNDED_ENDPOINT_DOMAINS_BUILT = false | TYPE-U |
  would-build: named unbounded operators plus a common invariant closure core

U3_008_INSTANCE_EXISTS = false | TYPE-U |
  would-build: the four fields above on the discharged common-origin trace
P5_COMPLETE_INPUT_READY = false | TYPE-U |
  would-build: completed U3 tuple
```

This is a narrowed stop, not a refutation of U3 or of any field's existence.

## 1. Preflight, currency, scope, and authorities

### 1.1 Send-time preflight

```text
DOES_THE_OBJECT_EXIST = PARTIAL
  the law-side finite objects and common-origin trace exist;
  the four complete U3 fields do not

IS_THE_VERSION_CURRENT = true
  checked through Q-276;
  Q-276 corrects the sign of D^2 Log Z in P2 V001 and is incorporated through
  P2 V002; that correction does not alter any P3 carrier or verdict

ARE_THE_INPUTS_PRESENT = PARTIAL
  U_N, F_N, A_N^[A], PathCert_N, GNS_out, P2, and the germ exist;
  finite history measures, analytic regulator family, completed joint
  boundary carrier, and unbounded operator/domain pairs do not
```

### 1.2 Roots entered and exclusions

Roots entered:

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha_supervision
/Users/bgm/MB Work/alpha-program-archive/workspace
```

The archive workspace was used to check mirrored authorities, not as an
independent source when the cleanroom copy existed.

Excluded:

```text
a32_holdout/custodian_private/                   NOT ENTERED
alpha/kappa/coupling/root/scale evaluation       NOT PERFORMED
comparison to a measured constant                NOT PERFORMED
register, plan, tracker, git, commit, push        NOT TOUCHED
```

Search identifiers included `measure`, `branch-joint`, `projective`,
`zero-extension`, `marginal`, `E_post`, `time-orientation`, `contour`,
`i-epsilon`, `boundary`, `glue`, `GNS_out`, `domain`, `self-adjoint`,
`PathCert`, `F_N`, and `A_N`. Searches were case-insensitive where applicable.
`rg` was unavailable; `find`/`grep` and direct source reads were used.

### 1.3 Current authorities

| Authority | Binding content |
|---|---|
| `STAGE8_TASK4A_P3_COMPLETE_U3_PACKAGE_CONSTRUCTION_AND_FOUR_FIELD_STOP_V001.md` (`f97ee43e...`) | Q-275 first stop and exact four would-builds |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_U3_DOR008_DOR009_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md:99-119,337-398,402-509,511-586` | U3 signature, finite grammar, boundary/domain and measure bars |
| `DECISION_OF_RECORD_009_THE_TRANSITION_LAW_RATIFIED_E_POST_2026-08-02_V001.md:8-17` | `E_post` as adopted time-oriented endpoint-charge assignment |
| `STAGE8_SOURCE_COUPLED_RECORD_TRANSITION_LAW_ADOPTION_PROPOSAL_V002.md:166-253,281-440` | endpoint-charge content, finite law, C7, finite trace and scope ceiling |
| `STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_FUNCTIONAL_RESULT_V001.md:10-50,117-218,385-440,552-586` | exact `F_N`, zero-extension, operator-valued scope and no parent/domain datum |
| `STAGE8_ENVELOPE_FINITE_PATHCERT_DYNAMICS_SUBTRACE_CONSTRUCTION_V001.md:10-60,190-303,360-395,482-503` | lower-row path, outgoing record GNS, absent full fields, record-only ceiling |
| `STAGE8_TASK4A_P2_PHYSICAL_SOURCE_TOPOLOGY_AND_DIFFERENTIAL_CALCULUS_CONSTRUCTION_V002.md:167-265,270-337,339-490` | current source topology/calculus, dense finite core and moving-tail exclusion |
| `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V004.md` and DoR-014 | common-origin germ and family-wide rank discipline |
| DoR-013 | generative common-origin trace and no member selection |

No ordered rank pair is instantiated and no rank ratio is evaluated.

## 2. Frozen law-side input

For every finite `N`, the ratified law gives

```text
U_N[a]=P_0 tensor I + P_ch tensor W_N[a],

F_N[a_+,a_-]
  =<R_N|U_N[a_-]^dagger U_N[a_+]|R_N>
  =P_0+Z_N[a_+,a_-]P_ch,

Z_N[a_+,a_-]
  =product_(j=1)^N conjugate(z_(-,j)) z_(+,j),

A_N^([A])[a_+,a_-]
  =(1-p_[A])+p_[A] Z_N[a_+,a_-].
```

On the finite quotient `Q_N=U(1)^N`, write these as `Fbar_N` and
`Abar_N^([A])`. For `N<=M`, C7 supplies the zero-section embedding

```text
j_NM^Q(r_1,...,r_N)=(r_1,...,r_N,1,...,1)
```

and exact pullback identities

```text
Fbar_M compose j_NM^Q=Fbar_N,
Abar_M^([A]) compose j_NM^Q=Abar_N^([A]).          (2.1)
```

PathCert supplies the law-side state path

```text
rho_ready,N --U_N--> rho_N --Rec_N--> omega_N
  --GNS embeddings--> (R_infinity,omega_out,GNS_out),               (2.2)
```

with

```text
omega_M compose iota_NM=omega_N.                                  (2.3)
```

Equation (2.3) is consistency of states on an inductive system of **record
algebras**. It must not be identified with consistency of a measure on doubled
source histories.

## 3. Field (1): measure from law amplitudes

### 3.1 The object that does construct

Define the law-side cylinder-amplitude system

```text
OscCyl_N := (Q_N,Fbar_N,Abar_N^([A])),

OscCyl := {OscCyl_N,j_NM^Q}_{N<=M}.
```

Equation (2.1) proves exact contravariant compatibility. `Fbar_N` is unitary
on the source-sector fiber; `Abar_N^([A])` is generally a complex scalar
amplitude. Positivity is neither asserted nor imposed.

```text
LAW_SIDE_CYLINDER_AMPLITUDE_SYSTEM_BUILT = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
LAW_SIDE_CYLINDER_AMPLITUDE_IS_POSITIVE_PROBABILITY_MEASURE = false | TYPE-R |
  test: it is a point function/amplitude; no event sigma-algebra or setwise
        additivity map occurs in its signature
```

There is a second positive law-side object: `(R_infinity,omega_out)` is a
state on the outgoing **record algebra**. Its carrier is not the doubled
history space and `Rec_N` has removed the source except for its record-visible
quotient. It is not transported into the U3 measure slot.

### 3.2 C7 is not Kolmogorov consistency

Let `pi_MN:Q_M->Q_N` delete the last `M-N` coordinates. A projective family of
finite complex measures would require

```text
(pi_MN)_* nu_M = nu_N,                                             (3.1)
```

meaning equality after integration over every appended-coordinate fiber.
C7 instead proves

```text
j_NM^{Q,*} Abar_M=Abar_N,                                         (3.2)
```

meaning equality only after fixing all appended coordinates to the identity.
Projection `pi_MN` and section `j_NM^Q` have opposite directions. Equation
(3.2) neither defines `nu_N` nor implies (3.1).

The distinction is failure-capable. If one provisionally tests product Haar
only as a counterexample, integration of an appended nontrivial character
annihilates that character, whereas evaluation at the identity preserves it.
Thus the Haar marginal of the amplitude-weighted candidate does not reproduce
the zero-section pullback for the nontrivial charged term. Conversely, a
Dirac measure concentrated on identity-appended histories would reproduce the
section but would be a new, selected history law with no common-origin descent.
Neither candidate is adopted.

```text
C7_IMPLIES_KOLMOGOROV_MARGINAL_CONSISTENCY = false | TYPE-R |
  test: section pullback and projection pushforward are different commuting
        conditions; the provisional Haar and identity-Dirac tests separate them
```

### 3.3 Oscillatory-measure route and exact residual datum

A complex/oscillatory measure is lawful in principle, but it still requires:

```text
nu_N: Sigma(Hist_+,N x Hist_-,N) -> C,
bounded total variation or another declared extension class,
(pi_MN)_*nu_M=nu_N,
gauge/boundary/contour transformation laws.
```

The amplitudes could become densities only after a base family
`lambda_N` is supplied:

```text
dnu_N=A_N d lambda_N.
```

No such base family or equivalent history-event functional is generated by
the ratified law, germ, P2, or PathCert. Intrinsic Haar remains refuted as the
required descended measure by Q-239: it bypasses prequotient provenance and
omits spacetime, contour, boundary, and representation data.

```text
BRANCH_JOINT_COMPLEX_MEASURE_BUILT = false | TYPE-U |
  would-build: finite complex history measures with (3.1), variation control,
               common-origin provenance, and the required invariances
DESCENDED_DMU_C_BUILT = false | TYPE-U |
  would-build: completed q, nu_phys, q_*nu_phys, delta_phys, and all U3
               contour/spacetime/boundary/domain compatibility certificates
```

The law-side attack narrows the measure gap from “some measure” to **a
covariant projective family of history-event functionals**. The cylinder
amplitudes are the integrands/characteristic data such a family must reproduce;
they are not the family itself.

## 4. Field (2): contour from `E_post`

### 4.1 What `E_post` actually supplies

DoR-009:8-13 ratifies

```text
E_post: time-oriented endpoint-charge assignment -- charge follows the
write's direction.
```

The underlying proposal defines its physical content more precisely:

```text
the character attaches once to the written output;
incoming ready and outgoing pointer carry the same faithful character;
W_post(z)=D(z)S.
```

Therefore `E_post` supplies an endpoint-charge arrow and selects it over the
conjugated two-sided endpoint package. It combines consistently with the
already-ratified CTP order `U_-^dagger U_+`.

Define the exact orientation receipt

```text
ContourOrient_law := (
  branch order +/-,
  U_-^dagger U_+,
  E_post endpoint-charge arrow,
  U1 reality/branch involution
).
```

```text
LAW_SIDE_CONTOUR_ORIENTATION_RECEIPT_BUILT = true | TYPE-P |
  premises: DoR-008, DoR-009
```

### 4.2 Why no `i epsilon` prescription follows

An interacting prescription additionally needs an instantiated analytic
family, for example abstractly

```text
K_epsilon or U_epsilon,
epsilon-domain and sign/insertion rule,
analytic half-domain and boundary-value map,
common invariant operator domain,
limit epsilon -> 0 in a named topology.
```

No such epsilon-indexed object appears in DoR-009, `E_post`, the finite law,
PathCert, or P2. `topology_src` is a topology on source increments; without an
operator-valued map `epsilon -> K_epsilon` there is no limit to take in it or
in an operator topology.

The decision's phrase “time-oriented assignment” cannot be transported from
endpoint-charge orientation to analytic pole displacement. Indeed, the V002
proposal records at lines 43-45 that no sealed time-orientation rule selected
the endpoint package; DoR-009 made that physical choice openly. Ratification
settles the endpoint package, not every analytically time-oriented completion.

```text
EPOST_ENDPOINT_ORIENTATION_EQUALS_INTERACTING_I_EPSILON_PRESCRIPTION = false |
  TYPE-R |
  test: E_post has endpoint representations and a write arrow but no epsilon
        parameter, analytic operator family, boundary-value map, or limit

INTERACTING_CONTOUR_PRESCRIPTION_BUILT = false | TYPE-U |
  would-build: common-origin analytic family with E_post-compatible
               orientation, regulator insertion, domains, and convergence
I_EPSILON_LIMIT_IN_TOPOLOGY_SRC = NO_VERDICT |
  prerequisite: no epsilon-indexed family exists
```

The three zeros remain distinct: source/probe zero in P2, finite equal-history
identity in the quotient, and physical difference-field zero on the future
interacting domain.

## 5. Field (3): boundary/glue from the two exact limits

### 5.1 Law-side package that constructs

Combine the already-built finite boundary package with the ratified law and
PathCert:

```text
BdGlue_N^law := (
  open-chain endpoints and endpoint gauge actions,
  ready preparation rho_ready,N,
  E_post transition U_N,
  completed finite density rho_N,
  quotient q_N and equal-history identity,
  zero extensions j_NM^Q and iota_NM,
  record restriction Rec_N,
  outgoing state omega_N and GNS embedding J_NM
).
```

There are two exact completion statements:

1. the source maps complete in P2's Banach norm on `E_src`, with finite source
   core dense and moving tails excluded;
2. the record-state embeddings complete to
   `(R_infinity,omega_out,GNS_out)` by the GNS isometries.

Call their non-identified pair

```text
BdGlue_law_limit := (BdGlue_law_src,BdGlue_law_rec).
```

All preparation ends carry the germ's family-wide ready normalization. No
anchor member or rank value is selected.

```text
LAW_SIDE_BOUNDARY_GLUE_LIMIT_PAIR_BUILT = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P2_SOURCE_LIMIT_IDENTIFIED_WITH_RECORD_GNS_LIMIT = false | TYPE-R |
  test: source Banach space and record GNS have distinct carriers and maps
```

### 5.2 Exact remaining boundary datum

PathCert itself states that `GNS_out` is record-only and that `Rec_N` removes
the source. Its absent full fields include physical restriction, joint effects,
joint completed/outgoing nodes, effects, domains, and their full-carrier
certificates. The U3 contract additionally requires preparation/gluing
variation, physical boundary gauge orbit, edge reductions and boundary
functionals, microcausal support, and vanishing global boundary form.

None is fixed by norm density. The two limits above do not produce a completed
joint source-record-field/CTP carrier or an intertwiner between them.

```text
LAW_SIDE_LIMIT_PAIR_EQUALS_COMPLETE_CTP_BOUNDARY_PACKAGE = false | TYPE-R |
  test: completed joint carrier, preparation variation, physical boundary
        orbit/functionals, microcausal support, and boundary-form certificate
        are absent

COMPLETE_CTP_BOUNDARY_EDGE_PACKAGE_BUILT = false | TYPE-U |
  would-build: a common-origin completed joint carrier plus preparation/
               gluing variation, boundary orbit, edge reduction/functionals,
               microcausal support, global boundary-form certificate, and
               intertwiners to both exact limits
```

This narrows the boundary stop: no new finite glue is needed. The missing datum
is the **joint physical completion and its boundary structure**.

## 6. Field (4): domains from PathCert GNS

### 6.1 What the GNS construction proves

For every finite record algebra, standard GNS supplies

```text
H_N=completion(R_N/N_omega_N),
pi_N(A)[B]=[AB],
Omega_N=[I],
```

and the isometries complete to `(pi_out,H_out,Omega_out)`. Every represented
element of the record C*-algebra acts boundedly on the full GNS Hilbert space.
Thus the law-side bounded domain receipt is exact:

```text
Dom_rec^bdd := (H_out,{pi_out(A):A in R_infinity}).
```

```text
OUTGOING_RECORD_BOUNDED_DOMAIN_BUILT = true | TYPE-P |
  premises: DoR-008, DoR-009
```

### 6.2 The proposed unbounded-domain inference fails

PathCert does not name an unbounded endpoint operator. Its certificate lists
`d_domain` among absent full fields, and its `ScopeCeiling` is
`record_only_outgoing`. The finite PathCert vectors are dense in `H_out`, but
density alone does not prove that they are invariant under, form a core for,
or consist of analytic vectors for an uninstantiated operator.

Pure phase proves bounded unitarity of the finite `F_N` source-sector action.
It does not supply a unique logarithm/generator, symmetry on a core,
deficiency-index result, resolvent, or closure theorem for future local fields,
actions, inverses, or response operators.

```text
PATHCERT_NAMES_UNBOUNDED_PHYSICAL_ENDPOINT_OPERATOR = false | TYPE-R |
  test: emitted certificate has ScopeCeiling=record_only_outgoing and lists
        d_domain/full-carrier fields as absent
PURE_PHASE_IMPLIES_ESSENTIAL_SELF_ADJOINTNESS_OF_FUTURE_OPERATOR = false |
  TYPE-R |
  test: bounded unitary data do not instantiate the future operator/domain pair
ESSENTIAL_SELF_ADJOINTNESS_PROVED = NO_VERDICT |
  prerequisite: no named symmetric unbounded operator/domain pair exists

COMPLETE_UNBOUNDED_ENDPOINT_DOMAIN_BUILT = false | TYPE-U |
  would-build: named unbounded operators on the completed physical
               representation, common dense invariant core, symmetry and
               closability, self-adjoint/closed-extension certificates,
               gauge invariance, boundary form, and glue preservation
```

The narrowed domain stop is the **operator realization itself**, not another
density argument.

## 7. Common-origin trace and U3 assembly

DoR-013/014 discharge the origin port. Every object constructed in Sections
3-6 descends without post-output supplementation from the frozen family-level
origin and the ratified law/germ. Therefore:

```text
P3_COMMON_ORIGIN_PROVENANCE_PORT_DISCHARGED = true | TYPE-P |
  premises: DoR-013, DoR-014
```

But a common origin of existing outputs does not generate an output absent
from the maps. The complete tuple is

```text
U3_required := (
  completed quotient,
  dmu_C and delta_phys,
  interacting contour prescription,
  complete boundary/edge/glue package,
  unbounded endpoint domains,
  common-origin trace
).
```

Only the finite quotient skeleton, law-side subpackage, source completion,
bounded record GNS domain, and origin port exist.

```text
U3_008_INSTANCE_EXISTS = false | TYPE-U |
  would-build: measure + interacting contour + complete boundary + unbounded
               domains
d_U3_TOTAL = false | TYPE-U |
  would-build: executable descent maps for all four fields
P3_COMPLETE = false | TYPE-U |
  would-build: the same four fields
P5_COMPLETE_INPUT_READY = false | TYPE-U |
  would-build: completed P3/U3 tuple
```

## 8. DoR-008 restriction and moving-tail recertification

| Port | Law-side receipt | Restriction result | Complete-field status |
|---|---|---|---|
| measure | `OscCyl_N`; `omega_N` on record algebra | zero-section pullback and record-state restriction pass; marginal measure square absent | `TYPE-U` |
| contour | `ContourOrient_law` | finite branch order and E_post endpoint charges reproduce exactly | `TYPE-U` |
| boundary | `BdGlue_N^law` and two exact limits | one-cell, zero-extension, source norm and GNS embeddings pass | `TYPE-U` |
| domains | finite full bounded domains and `Dom_rec^bdd` | every current bounded finite operator restricts exactly | `TYPE-U` |
| provenance | DoR-013/014 frozen trace | family-wide, no member selection | `TYPE-P` |

Moving-tail status:

1. P2 source/germ moving tails have no limit in `topology_src`.
2. The outgoing record GNS limit is an inductive-algebra limit, not the Q-245
   source moving tail.
3. No measure or contour net exists, so no tail limit is asserted there.
4. No unbounded operator net exists, so no domain-limit claim is asserted.

No field receives an unexecuted DoR-008 pass.

## 9. Mandatory counterexample and import kill-passes

### 9.1 Measure kill

The provisional Haar integration and identity-Dirac section constructions
give different completions of the same zero-section amplitude data. This
proves C7 does not select a branch-joint measure. Neither is installed.

### 9.2 Contour kill

`E_post` is retained as the ratified time-oriented endpoint-charge assignment.
It is not renamed an analytic prescription. No standard Feynman, retarded,
advanced, Euclidean, thermal, or other regulator is imported.

### 9.3 Boundary kill

The P2 source completion and outgoing record GNS are kept as a pair, not
identified. No spacetime boundary is inferred from cell-index completion.

### 9.4 Domain kill

No logarithm of a unitary is selected to manufacture a generator. No source
Fréchet domain is transported to a Hilbert operator domain.

### 9.5 Rank and target discipline

Every receipt is uniform over the ratified rank family. No downstream
response, root, coupling, scale, or measured quantity enters any definition.

```text
IMPORTED_MEASURE_FOUND = false | TYPE-S |
  scope: P3 second attack
IMPORTED_CONTOUR_FOUND = false | TYPE-S |
  scope: P3 second attack
IMPORTED_DOMAIN_ASSUMPTION_FOUND = false | TYPE-S |
  scope: P3 second attack
UNPROVED_SOURCE_GNS_IDENTITY_TRANSPORT_FOUND = false | TYPE-S |
  scope: the two limits remain distinct
RANK_VALUE_SELECTION_FOUND = false | TYPE-S |
  scope: all statements family-wide
TARGET_TUNING_FOUND = false | TYPE-S |
  scope: no downstream output used
P3_SECOND_ATTACK_SURVIVES_MANDATORY_SELF_KILL = true
```

## 10. Final typed ledger

```text
P3_LAW_SIDE_CYLINDER_AMPLITUDE_SYSTEM_EXISTS = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P3_LAW_SIDE_CONTOUR_ORIENTATION_RECEIPT_EXISTS = true | TYPE-P |
  premises: DoR-008, DoR-009
P3_LAW_SIDE_BOUNDARY_GLUE_LIMIT_PAIR_EXISTS = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
P3_OUTGOING_RECORD_BOUNDED_DOMAIN_EXISTS = true | TYPE-P |
  premises: DoR-008, DoR-009
P3_COMMON_ORIGIN_PROVENANCE_PORT_EXISTS = true | TYPE-P |
  premises: DoR-013, DoR-014

P3_MEASURE_EXISTS = false | TYPE-U |
  would-build: projectively consistent finite branch-joint complex measures,
               completed descent, delta_phys, and invariance certificates
P3_INTERACTING_CONTOUR_EXISTS = false | TYPE-U |
  would-build: Epost-compatible epsilon-indexed analytic operator family and
               named convergence topology
P3_COMPLETE_BOUNDARY_EDGE_EXISTS = false | TYPE-U |
  would-build: completed joint physical carrier and boundary structure
P3_UNBOUNDED_ENDPOINT_DOMAINS_EXIST = false | TYPE-U |
  would-build: unbounded physical operator realization and common core

U3_008_INSTANCE_EXISTS = false | TYPE-U |
  would-build: the four fields above
P3_COMPLETE = false | TYPE-U |
  would-build: the four fields above
P5_COMPLETE_INPUT_READY = false | TYPE-U |
  would-build: completed P3/U3 tuple

PHYSICAL_VERDICT = NO_VERDICT
CONSTRUCTION_VERDICT = LAW_SIDE_SUBPACKAGE_BUILT__FOUR_FIELD_STOP_NARROWED

FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-S |
  scope: no structural construction was stopped by a fence

alpha_computed = false [TERMINAL FENCE DECLARATION]
proof_authorized = false [TERMINAL FENCE DECLARATION]
kappa_record_computed = false [TERMINAL FENCE DECLARATION]
```
