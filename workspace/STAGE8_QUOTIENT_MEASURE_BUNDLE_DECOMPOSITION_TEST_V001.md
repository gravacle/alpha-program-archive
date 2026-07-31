# Stage 8 Quotient/Measure Bundle Decomposition Test v001

Date: 2026-07-31
Lane: CODEX 1
Register head at issue: Q-106
Road justification: Q-83, `ADVANCES STEP 1`

`alpha_computed = false; proof_authorized = false; kappa_record_computed = false.`

## 0. Premises, scope, and non-actions

This artifact answers relay 199. It decomposes the load-bearing
quotient/measure bundle named by Q-105:

```text
the gauge-fixed physical quotient
the compound index ordering
the CTP branch metric / reality involution
the invariant contour / spacetime measure
```

Premises declared at the outset:

1. No new physical premise is adopted.
2. No value, scale, root, eigenvalue, beta function, response coefficient, or
   measured constant is computed.
3. The correlator-to-Hessian map is used only as a consumer interface stating
   what this bundle must supply; the map is not fixed here.
4. B0 is cited only through already sealed dependency/status declarations; this
   artifact does not categorize B0.
5. Q-91 is followed: no git, no gate, no baseline, no deploy status.

Search scope:

```text
roots:
  /Users/bgm/Documents/New project/gravity_emergence_evidence_program
  /Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003
  /Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md

exclusions:
  a32_holdout/custodian_private/
  new response-map construction
  new B0 categorization

queries:
  gauge-fixed physical quotient
  physical quotient
  gauge quotient
  contour measure
  CTP measure
  invariant spacetime measure
  dmu_C
  delta_phys
  CTP branch metric
  CTP reality
  Hermiticity involution
  compound index
  index order
  A_c
  A_delta
  Keldysh
```

## 1. Lead result

```text
physical_components_definite_as_I_prim = 0/4
components_sealed_as_I_prim = 0/4
bundle_decomposition_result = TWO-COUPLED-PACKAGE-SPLIT
formal_subconventions_definite = 2
physical_instantiations_derived = 0
```

The relay's four entries are not one object. The old bundle was an overbroad
bookkeeping package.

They are also not four independent primitives. Sealed dependency text groups
them as:

```text
U1 = branch/source typing package:
     orientation, metric, involution, compound-index order, source symmetry,
     and branch/source embeddings on C0

U3 = physical-domain package:
     orbit/constraint map, quotient, descended contour/spacetime measure,
     boundary/edge/gluing and endpoint operator domains, and predeclared
     contour prescription
```

The right decomposition is therefore two coupled packages, not one bundle and
not four standalone primitive objects. The compound index and CTP
metric/reality data have a formal convention layer, but their physical
instantiation remains U1-derived and unbuilt.

For the two formal sub-conventions, this artifact uses the subtyping:

```text
FORMAL-LAYER-DEFINITE / PHYSICAL-INSTANTIATION-TYPE-U
```

This is not a new physics class. It is a bookkeeping refinement forced by the
sealed distinction between conventions that can be written before B0 and the
physical package that must descend from B0/C0.

## 2. Governing source text

The primitive selection file states the abstract CTP setup:

`/Users/bgm/Documents/New project/gravity_emergence_evidence_program/primitive_record_cell_selection_principle_v004.md:19-35`

```text
rho_pre ... on the full source-record-field Hilbert space
gauge-fixed physical quotient of the compact unit-character connection
I=(a,mu,x) for CTP branch, physical field label, and spacetime point
oriented CTP branch metric and invariant spacetime measure
R in Sym^2(H_CTP,phys^*)
corresponding CTP reality/Hermiticity involution
```

The same file makes the abstract/physical split explicit at `:57-61`:

```text
This is an abstract Legendre identity on any fixed nondegenerate
gauge-fixed physical quotient. Step 5 must construct that quotient and its
contour measure from the microscopic operator before the identity can be
turned into a physical Dyson kernel.
```

At `:107-113` it also states that the physical Dyson residual waits on:

```text
The CTP metric, index order, Keldysh block inversion, gauge quotient, contact
terms, and boundary terms
```

The package triage gives the current typed status. In Section 0 it names U1
and U3:

`STAGE8_CTP_PHYS_INPUT_PACKAGE_TRIAGE_AND_LOAD_BEARING_FUNCTIONAL_SPEC_V001.md:38-44`

```text
U1 | Branch/source typing on C0: orientation, metric, involution,
compound-index order, source symmetry, and branch embeddings | derived=false
U3 | Physical-domain package: orbit/constraint map, quotient, descended
contour/spacetime measure, boundary/edge/gluing and endpoint operator domains,
and predeclared contour prescription | derived=false
```

Its dependency graph at `:737-772` says B0 feeds C0, U1, U2 and U3; U1-U3 are
co-derived siblings; item 4 has a formal convention layer before B0, but its
physical instantiation is U1.

Its conditional domain at `:866-899` repeats the split:

```text
U1: branch orientation/metric, reality involution, compound-index order,
source symmetry, and branch/source embeddings on C0

U3: the physical quotient, descended contour/spacetime measure,
boundary/edge/gluing domains, endpoint operator domains, and predeclared
contour prescription
```

It further states that lacking B0 or any C0/U1-U3 input returns
`NO_VERDICT`.

Q-105 records why this relay exists:

`/Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md:4271-4291`

```text
quotient/measure, raw-correlator map, B0   INDEFINITE construction/interface objects
```

and:

```text
AN INDEFINITE OBJECT IN LOAD-BEARING USE IS WORSE THAN A MISSING ONE
```

## 3. Per-component determination

### 3.1 Gauge-fixed physical quotient

Type:

```text
physical-domain quotient object: an orbit/constraint map plus quotient domain,
physical identity, stabilizer/null-direction removal, and representation-specific
ghost/Jacobian data if the derived quotient presentation requires them
```

Domain:

```text
the compact unit-character connection and source-record-field CTP physical
field space on the yet-unbuilt C0/common domain
```

What currently supplies it:

- `primitive_record_cell_selection_principle_v004.md:21-22` names the
  prospective gauge-fixed physical quotient.
- The same source at `:57-61` says Step 5 must construct the quotient and its
  contour measure from the microscopic operator.
- `STAGE8_CTP_PHYS_INPUT_PACKAGE_TRIAGE_AND_LOAD_BEARING_FUNCTIONAL_SPEC_V001.md:461-497`
  classifies it as PARTIAL and gives:

```text
completed_gauge_fixed_physical_quotient_derived = false | TYPE-U |
  would-build: derive the full orbit/constraint map, stabilizers, quotient
  domain, physical identity, and the ghost/Jacobian datum only where the
  independently derived quotient presentation requires it
```

Determination:

```text
gauge_fixed_physical_quotient_individually_definite = false | TYPE-U |
  would-build: derive U3's orbit/constraint map, quotient domain, physical
  identity, and required ghost/Jacobian or reduced-variable descent from B0/C0
```

It is not an I_prim candidate on present evidence. It is a U3 descendant
obligation.

### 3.2 Compound index ordering

Type:

```text
formal source-coordinate/index ordering convention for CTP branch, physical
field label, and spacetime point; physically, a branch/source typing component
of U1 on C0
```

Domain:

```text
I=(a,mu,x), with a the CTP branch, mu the physical field label, and x the
spacetime point; Keldysh variables use A_c=(A_+ + A_-)/2 and
A_delta=A_+ - A_-
```

What currently supplies it:

- `primitive_record_cell_selection_principle_v004.md:21-25` fixes
  `I=(a,mu,x)` and the DeWitt contraction's branch/measure ingredients.
- `alpha_complete_dimension_convention_ledger_v004.md:260-267` fixes the
  Keldysh variables.
- The package triage at
  `STAGE8_CTP_PHYS_INPUT_PACKAGE_TRIAGE_AND_LOAD_BEARING_FUNCTIONAL_SPEC_V001.md:541-584`
  classifies the complete physical branch package as missing.

Determination:

```text
compound_index_ordering_formal_layer_definite = true

compound_index_ordering_as_physical_I_prim_definite = false | TYPE-U |
  would-build: derive U1's compound-index order and its action on the completed
  physical quotient from B0/C0
```

The formal index syntax is definite. The physical object consumed by the
response interface is not merely the syntax; it is U1's action on C0 and the
quotient. That physical instantiation is unbuilt.

### 3.3 CTP branch metric / reality involution

Type:

```text
formal CTP branch metric plus CTP reality/Hermiticity involution restricting
the symmetric bilocal source domain; physically, a branch/source typing
component of U1 on C0
```

Domain:

```text
Sym^2(H_CTP,phys^*) with antisymmetric bilocal directions excluded
```

What currently supplies it:

- `primitive_record_cell_selection_principle_v004.md:24-35` names the oriented
  CTP branch metric, symmetric dual, and corresponding CTP
  reality/Hermiticity involution.
- `COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_AMPLITUDE_RESULT_V001.md:28-37,59-67`
  supplies an executed finite/algebraic CTP Hermiticity subgate, as quoted in
  the package triage at `STAGE8_CTP_PHYS_INPUT_PACKAGE_TRIAGE_AND_LOAD_BEARING_FUNCTIONAL_SPEC_V001.md:561-569`.
- The same triage at `:571-584` says the complete physical package is still
  missing.

Determination:

```text
CTP_branch_metric_reality_formal_layer_definite = true

CTP_branch_metric_reality_as_physical_I_prim_definite = false | TYPE-U |
  would-build: derive U1's oriented branch metric, involution, source symmetry,
  branch/source embeddings, and action on the completed physical quotient from
  B0/C0
```

The finite/algebraic Hermiticity result does not construct the full physical
U1 package.

### 3.4 Invariant contour / spacetime measure

Type:

```text
descended contour/spacetime measure used in DeWitt contractions and in the
physical convolution inverse, including representation-specific gauge and
boundary measure data where the quotient presentation requires them
```

Domain:

```text
the physical quotient's contour/spacetime history domain, including boundary,
edge, gluing, endpoint, prescription, and physical identity data supplied by U3
```

What currently supplies it:

- `primitive_record_cell_selection_principle_v004.md:21-25` names the invariant
  spacetime measure inside DeWitt contraction.
- `alpha_complete_dimension_convention_ledger_v004.md:289-302`, as quoted in
  `STAGE8_CTP_PHYS_INPUT_PACKAGE_TRIAGE_AND_LOAD_BEARING_FUNCTIONAL_SPEC_V001.md:508-513`,
  supplies ordinary spacetime factors.
- The package triage at `:499-539` says the adjacent face-measure result is not
  a contour/path-integral measure and records:

```text
complete_invariant_contour_spacetime_measure_derived = false | TYPE-U |
  would-build: descend the full contour, spacetime, representation-specific
  gauge, and boundary measure from B0/C0/U1-U3 and prove its common-domain
  invariance
```

Determination:

```text
invariant_contour_spacetime_measure_individually_definite = false | TYPE-U |
  would-build: descend the full U3 measure on the completed quotient from
  B0/C0/U1-U3 and prove common-domain invariance
```

It is not independent of the quotient. The measure must be a descended measure
on that quotient.

## 4. Four objects or one?

The answer is neither.

Not one object:

```text
old_quotient_measure_bundle_is_one_object = false | TYPE-R |
  test: U1/U3-SPLIT-TEST; the package graph separates branch/source typing
  U1 from physical-domain package U3 at
  STAGE8_CTP_PHYS_INPUT_PACKAGE_TRIAGE_AND_LOAD_BEARING_FUNCTIONAL_SPEC_V001.md:737-772
```

Not four independent primitive objects:

```text
four_entries_are_four_independent_I_prim_objects = false | TYPE-R |
  test: COUPLED-PACKAGE-TEST; compound index ordering and CTP
  branch metric/reality are U1 components, while quotient and descended measure
  are U3 components; the measure's domain is the quotient and the physical
  inverse equations use dmu_C and delta_phys on that quotient
```

Positive decomposition:

```text
bundle_decomposes_as =
  U1_formal_plus_physical_branch_source_typing_package
  +
  U3_physical_domain_quotient_measure_package
```

The bundling was a bookkeeping choice, and it did cost the program precision.
The corrected bookkeeping does not produce four new primitives.

## 5. What the correlator-to-Hessian consumer needs

This artifact names the requirement without fixing the map:

```text
RAW_TO_RETHESS_PHYSICAL_DOMAIN_AND_CONTRACTION_PACKAGE :=
  C0 common physical domain
  + U1 physical branch/source typing:
      branch orientation/metric,
      CTP reality/Hermiticity involution,
      compound-index order,
      symmetric source convention,
      branch/source embeddings
  + U3 physical domain package:
      gauge-null removal by completed physical quotient,
      physical identity,
      descended invariant measure dmu_C,
      physical delta delta_phys,
      boundary/edge/contact/endpoint domains,
      predeclared contour prescription
```

The consumer evidence is
`STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:641-673`.
It requires the compound indices, branch metric and invariant measure, fixed
reality/Hermiticity, completed physical quotient, physical identity, operator
domains, inverse prescription, and contact/boundary/edge data. The same source
at `:710-722` defines the inverse using `dmu_C` and `delta_phys`; at `:757-819`
it says the Keldysh block extraction inherits all branch metric, DeWitt,
contact, and boundary conventions from the package.

Thus:

```text
raw_to_retarded_hessian_needs_bare_formal_index_only = false | TYPE-R |
  test: consumer-domain test at STAGE8_RAW...:641-673 and :710-819

raw_to_retarded_hessian_needs_completed_U1_U3_physical_package = true
```

If any domain datum is absent, that consumer returns `NO_VERDICT`, as
`STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:672-673` states.

## 6. Q-92 sealing decision

No component is sealed as an `I_prim` member in this artifact.

Reason:

```text
Q92_component_sealing_authorized = false | TYPE-C |
  constraint: Q-92(c,e,f), Q-100
  release: construct the relevant physical U1/U3 prerequisite from B0/C0,
  attach failure-capable tests with dedicated verdict owners, and record an
  adversarial countermodel attempt that fails; for any proposed I_prim member,
  also prove it is upstream of Obj_0 rather than a descendant or a port-time
  sector/reference value
```

Per component:

```text
gauge_fixed_physical_quotient_sealed_as_I_prim = false | TYPE-C |
  constraint: U3 is unbuilt and Q-92 prerequisites/tests/owner/countermodel are
  absent; release: derive U3 quotient package from B0/C0 and execute tests

compound_index_ordering_sealed_as_I_prim = false | TYPE-C |
  constraint: formal syntax exists, but the consumer object is U1's physical
  index/action package on C0; Q-92 tests and adversarial countermodel are
  absent; release: derive U1 or separately charter a formal-convention primitive
  with an upstreamness test under Q-100

CTP_branch_metric_reality_sealed_as_I_prim = false | TYPE-C |
  constraint: formal/finite reality evidence exists, but the physical U1
  instantiation is unbuilt; Q-92 tests and adversarial countermodel are absent;
  release: derive U1 and execute its physical branch/reality tests

invariant_contour_spacetime_measure_sealed_as_I_prim = false | TYPE-C |
  constraint: U3 descended measure is unbuilt and depends on the quotient;
  release: derive the complete U3 measure on the quotient and execute
  common-domain invariance tests
```

## 7. Typed negatives summary

```text
gauge_fixed_physical_quotient_individually_definite = false | TYPE-U |
  would-build: U3 quotient/domain package from B0/C0

compound_index_ordering_as_physical_I_prim_definite = false | TYPE-U |
  would-build: U1 physical index/action package on C0

CTP_branch_metric_reality_as_physical_I_prim_definite = false | TYPE-U |
  would-build: U1 physical branch metric/reality/source package on C0

invariant_contour_spacetime_measure_individually_definite = false | TYPE-U |
  would-build: U3 descended measure on completed quotient

old_bundle_is_one_object = false | TYPE-R |
  test: U1/U3-SPLIT-TEST

four_independent_primitives = false | TYPE-R |
  test: COUPLED-PACKAGE-TEST

components_sealed_as_I_prim = 0/4 | TYPE-C |
  constraint: Q-92(c,e,f) plus Q-100 upstreamness
```

## 8. Relay answers

1. Each of the four is stated in Section 3 with type, domain, supplier, and
   status.
2. Individually definite as physical `I_prim` members: zero of four. Two have
   definite formal layers; none has a derived physical instantiation.
3. They are not one object and not four independent objects. They are two
   coupled packages: U1 and U3.
4. The correlator-to-Hessian consumer needs the
   `RAW_TO_RETHESS_PHYSICAL_DOMAIN_AND_CONTRACTION_PACKAGE`: C0 plus completed
   U1/U3 data sufficient to contract, quotient, invert, choose a physical
   block, and carry contact/boundary/domain conventions.
5. Under Q-92, nothing is sealed as `I_prim`. What is indefinite is specified
   by the `would-build` fields above.

No git, commit, push, gate, baseline, or deploy action was performed.
