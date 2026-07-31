# Stage 8 B0 Codomain-Route Underdetermination Test v001

Date: 2026-07-31
Lane: CODEX 1
Register head at issue: Q-109
Road justification: Q-83, `ADVANCES STEP 1`

`alpha_computed = false; proof_authorized = false; kappa_record_computed = false.`

## 0. Premises, scope, and non-actions

This artifact answers relay 202. It tests the codomain route for constructing
`B0 [CTP-PACKAGE-COMPLETE-MICROSCOPIC-BOUNDARY-OPERATOR]` as primary:

```text
codomain -> B0
```

rather than treating it as a fallback after the primitive-input route fails.

Premises declared at the outset:

1. No new physical premise is adopted.
2. No value, scale, root, eigenvalue, beta function, response coefficient,
   absolute interval, or measured constant is computed.
3. `B0` is not identified with P0, with any flag, or with the T7
   nonvanishing predicate.
4. The adversarial countermodel required by Q-92(f) is being run by another
   lane and is not imported here as passed or failed.
5. Q-91 is followed: no git, no gate, no baseline, no deploy status.

Search scope:

```text
roots:
  /Users/bgm/Documents/New project/gravity_emergence_evidence_program
  /Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003
  /Users/bgm/MB Work/alpha-program-archive/workspace
  /Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md

exclusions:
  a32_holdout/custodian_private/
  Codex 2 response-map internals under relay 200
  Einstein B0/P0 ordering artifacts under relay 201, except the settled Q-109
  register row

queries:
  B0
  COMPLETE_MICROSCOPIC_BOUNDARY_OPERATOR
  complete microscopic operator
  microscopic source-record-field operator
  source-record-field operator/dynamics
  one microscopic source-record-field operator/dynamics
  complete Boundary-Resolved generator
  Boundary-Resolved generator
  U_BR
  A_BR
  source-record-field dynamics
  one complete microscopic operator
```

## 1. Lead result

```text
B0_built = false | TYPE-U |
  would-build: select or derive one member of the codomain-compatible
  boundary-origin realizer family, freeze its mathematical signature and
  descent maps, and pass Q-92 tests including a failed adversarial countermodel

codomain_constraints_determine_B0 = false | TYPE-R |
  test: B0-CODOMAIN-FIBER-UNIQUENESS-TEST

codomain_route_status = UNDERDETERMINED_FIBER
selector_or_uniqueness_theorem_required = true
```

The codomain route is a real constraint. It fixes what any admissible `B0`
must support: `C0`, `U1`, `U2`, `U3`, descent witnesses, common-origin
provenance, and no after-output supplementation.

It does **not** determine what `B0` is. The sealed role permits function,
operator, flow, relation, algebraic generator, or other types; it leaves
type/arity/domain/codomain/parameters, carrier/core, representation data, and
the descent maps unchosen. Multiple inequivalent objects can share the same
production codomain or even the same descendant tuple. Therefore `B0` is not
constructible from codomain constraints alone.

The named family is:

```text
CodomainCompatibleBoundaryOriginRealizer(B0) :=
  (
    Obj_B0,
    Sig_B0,
    Carrier_B0,
    Core_B0,
    Prov_B0,
    DESCEND_B0
  )
```

where `DESCEND_B0` maps the candidate to:

```text
SingleOriginPackageInputs(C0,U1,U2,U3,d_C0,d_U1,d_U2,d_U3)
```

and satisfies the no-supplement/common-origin rules. The corpus has specified
this family but has not selected a unique member.

## 2. What B0 must produce

The B0 stop spec recovers the exact object identity at
`STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md:11-34`:

```text
package_B0_object_identity =
  COMPLETE_MICROSCOPIC_BOUNDARY_OPERATOR

COMPLETE_MICROSCOPIC_BOUNDARY_OPERATOR_derived = false | TYPE-U |
  would-build: construct the single microscopic source-record-field boundary
  operator/dynamics from which C0/U1-U3 must be derived
```

The CTP package triage states the relevant direct outputs at
`STAGE8_CTP_PHYS_INPUT_PACKAGE_TRIAGE_AND_LOAD_BEARING_FUNCTIONAL_SPEC_V001.md:38-44`:

```text
B0 | Complete microscopic source-record-field boundary operator/dynamics
C0 | Narrow full source-record-field CTP carrier extension
U1 | Branch/source typing on C0
U2 | Microscopic action/evolution on C0; positive normalized pre-state,
     inclusive identity, admitted effects, action/source contact rules, and
     common domains
U3 | Physical-domain package: orbit/constraint map, quotient, descended
     contour/spacetime measure, boundary/edge/gluing and endpoint operator
     domains, and predeclared contour prescription
```

The same artifact gives the forward graph at `:737-763`:

```text
B0 COMPLETE_MICROSCOPIC_BOUNDARY_OPERATOR
  |
  +--> C0 narrow carrier/algebra extension
  +--> U1 physical branch/source typing on C0
  +--> U2 action/evolution + state/effects + action contact rules on C0
  +--> U3 quotient + descended measure + boundary/edge/gluing and endpoint
       operator domains + predeclared contour prescription on C0
```

It also warns at `:765-772` that C0 is narrow and that U1-U3 are co-derived
siblings; item 4 has a formal convention layer before B0, but the physical
instantiation is U1.

The B0 stop spec restates the exact load-bearing outputs at
`STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md:830-861`:

```text
C0 | B0
U1 | B0,C0
U2 | B0,C0
U3 | B0,C0
item 1 | B0,C0,U1,U2,U3
```

and records the common-origin constraint:

```text
The state, action, carrier, sources, quotient, measure, and domains must all
descend from B0
```

The formal production codomain is stated at
`STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md:977-1037`:

```text
DESCEND_B0 :
  CompleteMicroscopicBoundaryOriginCandidate
    ->
  SingleOriginPackageInputs(
    C0,
    U1,
    U2,
    U3,
    d_C0,
    d_U1,
    d_U2,
    d_U3
  ).
```

with:

```text
d_C0 : B0_candidate -> C0
d_Ui : (B0_candidate,C0) -> Ui,  i in {1,2,3}

C0 = d_C0(B0_candidate)
Ui = d_Ui(B0_candidate,C0),  i in {1,2,3}

no required physical datum in C0 or any Ui may be supplied by an undeclared
external supplement after any descendant output is inspected
```

Thus:

```text
B0_must_produce_C0_U1_U2_U3 = true
B0_must_supply_common_origin = true
B0_must_produce_item1_directly = false | TYPE-R |
  test: B0-DEPENDENCY-DIRECTION-TEST already recorded at
  STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md:1041-1065;
  item 1 also requires C0/U1/U2/U3
```

## 3. Does the codomain determine B0?

### 3.1 The codomain route is meaningful

The principal's boundary reading is not dismissed. The codomain route has
content: it says a candidate boundary origin is admissible only if it supplies
the complete descendant package from one source, with fixed descent witnesses
and no later supplements.

This is stronger than a label. It is a filter:

```text
Candidate B0 must be in the fiber of DESCEND_B0 over admissible
SingleOriginPackageInputs(C0,U1,U2,U3,d_C0,d_U1,d_U2,d_U3).
```

### 3.2 The uniqueness test

Test:

```text
test_id = B0-CODOMAIN-FIBER-UNIQUENESS-TEST
hypothesis =
  The production codomain and no-supplement/common-origin rules determine one
  B0 object, up to a sealed equivalence relation, without an additional
  primitive-input rule.
failure_criterion =
  The sealed corpus leaves two or more of Type_B0, Arity_B0, Dom_B0, Cod_B0,
  Params_B0, Carrier_B0, Core_B0, representation data, equivalence relation,
  or descent maps unselected while still allowing them under the same
  production-codomain role.
observed =
  The B0 role spec leaves all of those fields open and expressly refuses to
  force the candidate into one arrow/type class.
execution_status = EXECUTED
verdict_owner = CODEX 1 for this structural uniqueness test; adversarial
  countermodel owner is EINSTEIN under relay 203 and is not imported here.
```

The observed text is at
`STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md:938-969`:

```text
Because sealed text does not choose a representation, Q-52 specifies B0 as an
abstract single-origin object role, not as a concrete linear, bounded,
self-adjoint, C-star, path-integral, or transfer-matrix construction
```

and:

```text
For a function- or operator-typed candidate, Sig_B0 must state the applicable
map from Dom_B0 to Cod_B0. For a flow, family, relation, algebraic generator,
or other type, it must state that type's full arity, parameter, domain, and
codomain data without forcing it into a single Hilbert-valued arrow.
```

It then says the conformance relation:

```text
does not assert linearity, boundedness, self-adjointness, unitarity, locality,
a particular representation, or existence.
```

Therefore:

```text
codomain_constraints_determine_B0 = false | TYPE-R |
  test: B0-CODOMAIN-FIBER-UNIQUENESS-TEST; the sealed codomain route leaves
  the candidate type, signature, representation, internal properties,
  equivalence relation, and descent maps unselected
```

This is a structural result, not a negative preference. The boundary can be
fixed by what it supports only after the support condition is strengthened
into a uniqueness or universal property. The corpus has not supplied that
property.

### 3.3 What remains checkable

The codomain constraints make candidate testing possible once a candidate is
supplied. They do not themselves supply the candidate.

The B0 stop spec's tests at `:1124-1325` require:

- T1: an independently frozen `Obj_B0`, `Sig_B0`, carrier/core data where
  applicable, declared properties, and an independent domain/codomain oracle.
- T2: a frozen B0 candidate, exhaustive C0/U1/U2/U3 checklist, descent maps,
  and frozen allowed-label/chart/convention data.
- T3: candidate, descent map, independently derived reference descendant, and
  comparison oracle for each of C0, U1, U2, U3.
- T4: frozen B0 candidate and independently specified `U_BR`, `rho_pre`,
  admitted-effect family and domains.
- T5: independently constructed B0 candidate and Boundary-Resolved generator
  for correspondence, plus a separately constructed generator for causal and
  boundary-form conformance.

For each, missing candidates, maps, references, or oracles return
`NO_VERDICT`, not derivation.

## 4. What the theory's own content supplies independently of B0's spec

The independent corpus does not supply B0 content. It supplies constraints any
candidate must satisfy or realize.

### 4.1 Complete microscopic operator hard gate

`/Users/bgm/Documents/New project/gravity_emergence_evidence_program/primitive_complete_boundary_transition_functional_principle_v002.md:106-124`
requires:

```text
U_BR, rho_pre, every admitted record effect, and their domains follow from one
complete microscopic operator
```

and:

```text
the mixed response kernel, noise kernel, and first-record overlap are derived
from that same functional
```

but records:

```text
complete_transfer_operator_constructed=false
```

This is a single-origin and output constraint, not an internal B0 signature.

### 4.2 Boundary-Resolved unitary pre-record transfer

`/Users/bgm/Documents/New project/gravity_emergence_evidence_program/primitive_unitary_prerecord_transfer_principle_v001.md:3-27`
states an adopted pre-record transfer principle:

```text
Before a durable public record forms, a complete Gravacle cell evolves by a
strongly continuous unitary family on its complete pre-record Hilbert space.
```

with:

```text
U_BR(Delta tau) = exp(-i Delta tau A_BR)
```

for:

```text
the complete self-adjoint Boundary-Resolved generator A_BR
```

At `:37-58` it also states the active charged source carrier as the
unit-character line-twisted Dirac carrier, but says:

```text
Microscopic unitarity does not itself specify the additional record register,
the interaction generating A_BR, or the closure map C_BR. Each must be
derived on the active carrier.
```

This supplies a unitary/generator constraint for a Boundary-Resolved
generator, not a B0 construction.

### 4.3 Causal-domain and boundary-form obligations

`/Users/bgm/Documents/New project/gravity_emergence_evidence_program/primitive_causal_record_cell_domain_principle_v004.md:25-39`
fixes the causal support diamond and requires:

```text
The complete Boundary-Resolved generator must still prove microcausal support
of the history difference and make the global Dirac boundary form vanish under
the CTP preparation/gluing variations.
```

At `:62-75` it further says the required total-charge symplectic reduction,
boundary gauge orbit, and edge variables remain Step 5 outputs.

The B0 spec already notes at
`STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md:862-876`
that the causal-domain source does not equate this generator with package B0:

```text
B0_TO_BOUNDARY_RESOLVED_GENERATOR_CORRESPONDENCE_derived = false | TYPE-U |
  would-build: independently type both objects and derive a direction-bearing
  map showing how the package B0 candidate realizes or produces the complete
  Boundary-Resolved generator without identifying either object with a flag
```

### 4.4 Generated-carrier closure rules

`/Users/bgm/Documents/New project/gravity_emergence_evidence_program/primitive_boundary_generated_carrier_principle_v001.md:87-115`
says the principle:

```text
does not supply G_BR, a pole spectrum, a field-space metric, B_pub, or a
coupling
```

and the carrier closes only if, among other things:

```text
the complete primitive generator set is derived from one microscopic BR
action and measure
```

plus connected spectral support, absence of arbitrary copies/sectors, gauge
quotient and field-space metric, and construction of nontrivial `B_pub`.

It records:

```text
complete_generated_physical_carrier_derived=false
B_pub_constructed=false
```

This is further constraint language. It does not supply the B0 object.

### 4.5 Common-origin producer algebra

`STAGE8_COMMON_ORIGIN_GENERATIVE_VS_FORMATION_TYPING_V001.md:408-419`
quotes the common-origin producer definition:

```text
a completed source-record-field CTP algebraic carrier together with faithful
source and record embeddings, a physical field/CTP quotient package, a
positive normalized pre-state, admitted record effects and domains,
source-record-field dynamics, and a raw contour-correlator output interface,
all derived from one microscopic source-record-field operator/dynamics.
```

and records:

```text
COMMON_ORIGIN_CTP_PRODUCER_ALGEBRA_derived = false | TYPE-U
```

At `:426-459` it repeats P0-P7, including:

```text
P0. One microscopic source-record-field operator/dynamics B0-like source.
```

Again, this supplies a signature to be instantiated, not the instantiation.

Therefore:

```text
independent_B0_content_constructor_found = false | TYPE-S |
  roots: search scope in Section 0 |
  excl: B0's own spec as circular constructor, response-map construction,
  B0/P0 ordering work, custodian_private |
  fences: word-boundaried object search; flags and output rows are not
  constructors under Q-69 |
  query: microscopic source-record-field operator, complete microscopic
  operator, Boundary-Resolved generator, U_BR, A_BR, source-record-field
  dynamics, complete source-record operator/dynamics |
  result: obligations and constraints found, no exact construction rule or
  unique internal signature found
```

## 5. How underdetermined is B0?

The underdetermination is not a single missing scalar. It is a fiber over the
production codomain.

Named family:

```text
CodomainCompatibleBoundaryOriginRealizer :=
  {
    (Obj_B0, Sig_B0, Carrier_B0, Core_B0, Prov_B0, DESCEND_B0)
    such that
      Obj_B0 conforms_to Sig_B0,
      DESCEND_B0(Obj_B0) =
        SingleOriginPackageInputs(C0,U1,U2,U3,d_C0,d_U1,d_U2,d_U3),
      every physical datum in C0/U1/U2/U3 descends through those witnesses,
      no descendant datum is supplied by an undeclared post-output supplement,
      and every independently applicable B0 property test returns PASS
  }.
```

Open coordinates of that family, from the sealed B0 role spec:

```text
Type_B0        open: function/operator/flow/family/relation/algebraic generator/other
Arity_B0       open
Dom_B0         open
Cod_B0         open
Params_B0      open
Carrier_B0     open if required by the selected type
Core_B0        open if required by the selected type
representation open
descent maps   open: d_C0,d_U1,d_U2,d_U3
equivalence    open: no sealed relation identifies candidates with the same
               descendant package
```

Because the equivalence relation is itself unsealed, even two candidates with
the same `DESCEND_B0` output cannot be collapsed by the current corpus.

Thus:

```text
B0_underdetermination_degree = FIBER-WITH-OPEN-SIGNATURE-AND-OPEN-DESCENT
B0_underdetermined_by_consumers = true
B0_unique_member_selected = false | TYPE-U |
  would-build: a derived uniqueness/universal property, a frozen primitive
  construction rule, or a principal-adopted premise selecting one admissible
  member of the family
```

## 6. Q-92 build decision

Q-92(c) is vacuously satisfied only in the descent-DAG sense: no C0/U1/U2/U3
node is an input to B0. It does not make the candidate's content exist.

Q-92(a)-(f) do not all pass:

```text
Q92a_premises_declared = true
Q92b_tests_attached = partial
Q92c_descent_prerequisites_exist = vacuous for B0 as root
Q92c_candidate_content_exists = false | TYPE-U |
  would-build: a frozen Obj_B0/Sig_B0/Carrier_B0/Core_B0/Prov_B0 member
Q92d_road_step_named = true
Q92e_dedicated_verdict_owner_exists = partial
Q92f_adversarial_countermodel_failed = false | TYPE-U |
  would-build: receive and adjudicate Einstein relay 203's countermodel
```

Therefore:

```text
B0_constructed_under_Q92 = false | TYPE-C |
  constraint: no unique codomain-determined candidate, no frozen candidate
  content, no independently executed Q-92(f) failed countermodel
  release: select or derive one family member and pass the wired tests
```

If the principal wants a concrete B0 member, a premise must be added or a
uniqueness theorem must be chartered. This artifact does not add that premise.

## 7. Typed negatives summary

```text
B0_built = false | TYPE-U |
  would-build: select/derive a family member, freeze its signature and descent
  maps, execute Q-92 tests, and survive adversarial countermodel

codomain_constraints_determine_B0 = false | TYPE-R |
  test: B0-CODOMAIN-FIBER-UNIQUENESS-TEST

independent_B0_content_constructor_found = false | TYPE-S |
  roots: Section 0 |
  excl: Section 0 |
  fences: Q-69, word-boundaried object search |
  query: Section 0 object queries

B0_TO_BOUNDARY_RESOLVED_GENERATOR_CORRESPONDENCE_derived = false | TYPE-U |
  would-build: independently type B0 and the Boundary-Resolved generator and
  derive a direction-bearing map

B0_unique_member_selected = false | TYPE-U |
  would-build: derived uniqueness/universal property, primitive construction
  rule, or principal-adopted selector

B0_constructed_under_Q92 = false | TYPE-C |
  constraint: candidate content and Q-92(f) failed countermodel absent
```

## 8. Relay answers

1. B0 must produce `C0` and, with `C0`, `U1/U2/U3`; it must supply descent
   witnesses and common-origin/no-supplement provenance. It is necessary but
   not sufficient for item 1.
2. What it must produce does not determine what it is. The codomain route
   fixes an admissibility fiber, not a unique B0. The corpus route is therefore
   still the only specified construction route unless a new uniqueness or
   boundary-selector principle is supplied.
3. The theory's own content supplies obligations: single-origin microscopic
   operator, unitary Boundary-Resolved pre-record evolution, causal support,
   boundary-form vanishing, generated-carrier requirements, and common-origin
   producer signature. It supplies no independent B0 constructor.
4. Under Q-92, B0 is not built. Building it would require adding or deriving a
   selector for one member of the named family, then executing the tests and
   receiving a failed adversarial countermodel.
5. The underdetermination family is
   `CodomainCompatibleBoundaryOriginRealizer`: a fiber with open signature,
   open representation/carrier/core coordinates, open descent maps, and no
   sealed equivalence relation collapsing candidates with the same descendants.

No git, commit, push, gate, baseline, or deploy action was performed.
