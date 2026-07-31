# Stage 8 C_R Selector S3 Energy-Identification Join Specification V001

Date: 2026-07-31
Lane: CODEX 2
Authority: relay 179; register head at issue Q-81; pre-authoring register head Q-83;
pre-seal currency check through Q-86
Road status: ADVANCES STEP 2 — the Hamilton-Jacobi scale bridge
Status: Q-52 TEST SPECIFICATION ONLY

## 0. Lead, authority currency, and declarations

### 0.1 Lead finding

S3 cannot presently derive the named energy identification from the current
S1/S2/S4 interfaces. The sealed skeleton correctly places S3 at the join, but
the current contracts do not supply an executable join. Six inputs remain
unbuilt or unassigned, in three distinct layers:

```text
CORE CONSTRUCTION
1. one common nonempty first-durable stationary domain and pullback certificate;
2. an adapter applying S4's forced reference prescription to S2's symbolic
   Hamilton-Jacobi energy on that common domain;
3. a gravitating-closure-energy functional derived from the same S1 action;

CORE NONVACUOUS VALIDATION
4. a complete nontrivial equivalent-representation class with exact transports;

FULL GATE / NAMED CLASSIFICATION
5. the correspondence from S1's time-flow parameter to the proper-interval
   parameter required by the primary bridge gate;
6. complete domain/boundary/time-flow/reference/applicability-or-
   inapplicability signatures for
   both named comparison candidates.
```

The first three prevent construction of the sealed S3 equality proof. The
fourth prevents a nonvacuous representation-invariance PASS. The fifth and
sixth belong to the full bridge/named-classification leg, not to core S3, and
prevent the bare equality proof from naming either candidate. Therefore:

```text
S3_core_construction_executable_from_current_S1_S2_S4_interfaces = false | TYPE-U |
  would-build: actual S1, S2, and S4 objects plus P8, P10, and P11 below,
  followed by the S3 core construction witness

S3_core_representation_test_nonvacuous_from_current_inputs = false | TYPE-U |
  would-build: P13 below, then execute T8A/T8B with independent checkers

S3_can_presently_derive_named_energy_identification = NO_VERDICT |
  reason: the core construction, P9 time correspondence, and P12 candidate
  applicability-or-inapplicability packet are unbuilt
```

This is missing information, so Q-80 does not require a new class today. The
sealed S3 role fits an ordinary equality/correspondence proof certificate. If
a future fully derived S3 energy fits neither named candidate after complete
applicability tests, Q-80 would fire then; today that outcome is `NO_VERDICT`.

### 0.2 Authority currency: Q-83 through Q-86

Relay 179 named Q-81 as its register head. Before authoring, the settled head
had advanced to Q-83 at
`QUESTIONS_SETTLED_REGISTER_V001.md:3408-3442`. Q-83 states:

> `STEP 2   THE SCALE FIXED         C_R = 1 selects, via the Hamilton-Jacobi bridge;`

and preserves:

> `Q-52, Q-54, Q-69, Q-76, Q-80, the sqrt(2) prohibition`

This item therefore advances Road Step 2. Q-83 does not authorize a candidate
choice or relax any fence.

The register advanced to Q-84 during review at
`QUESTIONS_SETTLED_REGISTER_V001.md:3446-3482`. Its heading is:

> ## Q-84. "Does the `tau = 1` pin collapse?"

```text
Q84_disposition_for_this_artifact = REVIEWED_NONCONTROLLING_FOR_S3
  [PROCESS_AUTHORITY_ATTESTATION; NON-Q54_RESULT]
```

It is recorded for authority currency only and is neither consumed nor
adjudicated here.

The register then advanced through Q-85 and Q-86. Q-85 at
`QUESTIONS_SETTLED_REGISTER_V001.md:3486-3510` states:

> `STEP 2 IS THE SCALE SELECTOR PATH AND IS SEPARATE FROM THEM.`

That reaffirms this artifact's Road Step 2 placement. Q-86 at
`QUESTIONS_SETTLED_REGISTER_V001.md:3512-3555` is a Step 1 fixed-point-reading
ruling and leaves Q-69 standing. Currency dispositions are:

```text
Q85_disposition_for_this_artifact = REAFFIRMS_STEP_2_SCOPE
  [PROCESS_AUTHORITY_ATTESTATION; NON-Q54_RESULT]
Q86_disposition_for_this_artifact = REVIEWED_NONCONTROLLING_FOR_S3
  [PROCESS_AUTHORITY_ATTESTATION; NON-Q54_RESULT]
```

### 0.3 Q-52 object declaration

`QUESTIONS_SETTLED_REGISTER_V001.md:2195-2212` authorizes a missing-object
specification only when it is declared, marked `derived = false`, and never
reported as derived. This artifact declares:

```text
artifact_type = Q52_S3_ENERGY_CORRESPONDENCE_AND_CLASSIFICATION_SPECIFICATION

BRIDGE_SELECTOR_S3_HJ_CLOSURE_ENERGY_CORRESPONDENCE_CERTIFICATE_specified_for_test = true

BRIDGE_SELECTOR_S3_HJ_CLOSURE_ENERGY_CORRESPONDENCE_CERTIFICATE_derived =
  false | TYPE-U |
  would-build: consume actual same-origin S1/S2/S4 objects plus P8, P10, and
  P11; prove the reference-fixed HJ/closure functional identity over the full
  common domain; then execute the core tests with P13 in Section 6

S3_energy_classification_leg_derived = false | TYPE-U |
  would-build: after the core S3 identity exists, derive and apply P9 and the
  complete P12 candidate applicability-or-inapplicability/signature packet
  without formula name-matching or pointwise evaluation

S3_tests_executed = false | TYPE-U |
  would-execute: supply concrete independently derived inputs, candidate
  certificate, fixtures, and failure oracles for T-1A/B, T0A/B, T1, T2A,
  T3-T6, T7A/B, T8A/B, T9A/B, T10A/B, T11A/B, T12A/B, and T13A/B

physical_verdict = NO_VERDICT |
  reason: the S1/S2/S4 construction objects and P8-P13 are TYPE-U; no S3
  physical correspondence or named-candidate test has executed
```

### 0.4 F-GK3 premises declared at the outset

P0. Q-52 authorizes specification for testing. Specification is not
derivation.

P1. Q-54 negative typing, Q-69 node identity, Q-80 new-territory discipline,
and Q-83 Road Step 2 remain binding.

P2. S1 is specified but not derived. At
`STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md:317-327`
the artifact says:

> `The first load-bearing object is now specified as a test object, not derived.`

and records:

> `BRIDGE_S1_COMPLETE_LORENTZIAN_CTP_ACTION_BOUNDARY_TIME_FLOW_DATA_derived = false | TYPE-U`

P3. S2 is specified but not derived. At
`STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md:282-292` it says:

> `The second load-bearing object is now specified as a test object, not derived.`

and records:

> `BRIDGE_S2_CONSTANT_HAMILTON_JACOBI_RECORD_ENERGY_CERTIFICATE_derived = false | TYPE-U`

P4. S4 is specified but not derived. At
`STAGE8_C_R_SELECTOR_S4_REFERENCE_CO_PARTICIPATION_SPEC_V001.md:735-743` it
records:

> `BRIDGE_SELECTOR_S4_REFERENCE_CO_PARTICIPATION_CERTIFICATE_derived = false | TYPE-U`

P5. The primary bridge gate at
`BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:33-45` requires the same
microscopic theory to prove, among other conditions:

> `the CTP branch-energy difference equals the complete gravitating cell energy after one fixed reference subtraction`

and:

> `the energy is the one used by the chosen gravitational closure condition.`

P6. The reference-energy obstruction at the same gate, `:155-167`, states:

> `record branch-energy difference -> total gravitating energy`

and says that map:

> `requires a derived state, reference subtraction, and no-spectator theorem.`

P7. Q-59 at register `:2488-2500` rules that the bridge would derive the
identification rather than choose it, and warns:

> `The sqrt(2) must be derived, never chosen.`

P8. `S3_COMMON_NONEMPTY_FIRST_DURABLE_DOMAIN_AND_PULLBACK_CERTIFICATE_derived =
false | TYPE-U`. Would-build: derive a nonempty first-durable stationary
solution domain and exact pullbacks showing that S2's energy, S4's reference
and sector certificates, and the S1 closure functional all apply to that same
domain.

P9. `S3_TIMEFLOW_TO_REQUIRED_PROPER_INTERVAL_CORRESPONDENCE_derived = false |
TYPE-U`. Would-build: derive the correspondence between the S1-declared
time-flow parameter used by S2 and the proper-interval parameter required by
the primary bridge gate, including a checkable chain-rule/conjugacy-preservation
proof and exact domain transport. This artifact does not resolve, normalize,
or evaluate that parameter. The primary gate states this separately from S3
equality, so P9 is a full-gate/named-classification input and not a core S3
input.

P10. `S3_REFERENCE_APPLICATION_ADAPTER_derived = false | TYPE-U`.
Would-build: from exact common S1 provenance, construct the map taking S2's
symbolic HJ energy and S4's forced reference prescription to one
reference-fixed HJ branch-energy functional while preserving S2 constancy and
S4 support/sector data.

P11. `S3_GRAVITATING_CLOSURE_ENERGY_FUNCTIONAL_derived_from_S1 = false |
TYPE-U`. Would-build: derive from the complete S1 action, on the S4
retained/excluded support partition, the target-independent energy functional
actually consumed by the gravitational closure condition. A named candidate
or adopted closure-side formula is not this discharge object.

P12. `S3_NAMED_CANDIDATE_FUNCTIONAL_SIGNATURE_AND_APPLICABILITY_PACKET_derived = false |
TYPE-U`. Would-build: for each named candidate derive its exact variational
origin, domain, stationary class, boundary class, time-flow conjugacy,
reference rule, retained-sector support, closure role, and applicability map
on the S1 history-support domain, before inspecting an S3 result. It must also
carry the exact symbolic candidate functional, exact transport into the P8
domain, and independently checkable full-domain identity/nonidentity proof
inputs. Each map must carry a proved applicable or proved inapplicable outcome;
proved inapplicability is a valid non-match, not a malformed packet.

P13. `S3_EQUIVALENT_REPRESENTATION_TEST_PACKET_derived = false | TYPE-U`.
Would-build: derive an exhaustive, nontrivial class of admitted equivalent
representations for the complete core input package, at least one nonidentity
representative, exact transport maps for every core field and certificate,
an independently checkable completeness witness, and pre-result,
target-independent provenance for the class generator, transports, and
checker. P13 is a test input; it is not part of the physical equality domain.

P13's exhaustive/nontrivial test-fixture requirement is imported proof-testing
discipline, not a sealed physical premise. It applies here because S2 already
requires at
`STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md:178-190`:

> `The certificate must show that the constancy statement is stable under the boundary and time-flow choices fixed by S1.`

P13 adds the nonvacuity/completeness witness needed for that stability check to
be failure-capable; it does not enlarge the physical S3 equality domain.

premise_manifest_status = CLOSED_AT_P0_THROUGH_P13
  [PROCESS_ATTESTATION; NON-Q54_RESULT]

### 0.5 Absolute fences and ownership

This artifact does not construct S1, S2, S3, S4, or P8-P13; execute a test;
evaluate an energy expression; select a named candidate; derive a closure,
interval, scale, response, or value; or compare anything with a measured
constant. It does not enter, list, or infer protected holdout content. The
rank-1 producer, PATHLESS roster, pin spectral condition, and unit-value
convention work are excluded and not used.

## 1. Bounded correspondence and namespace checks

### 1.1 Roots, exclusions, and method

Roots:

```text
R1 = current cleanroom governing packet
R2 = /Users/bgm/MB Work/alpha-program-archive/workspace
R3 = /Users/bgm/MB Work/alpha_supervision
```

Controlling packet:

```text
BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md
STAGE8_BRIDGE_ITEM1_SIX_OBJECT_TRIAGE_V001.md
STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md
STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md
STAGE8_BRIDGE_ITEM4_SIX_OBJECT_DEPTH_REPORT_V001.md
STAGE8_C_R_SELECTOR_S4_REFERENCE_CO_PARTICIPATION_SPEC_V001.md
STAGE8_GRAVITY_EVIDENCE_ADMISSION_AND_FIVE_STRATA_BINDING_V001.md
STAGE8_NAMESPACE_REGISTER_DRAFT_V004.md
QUESTIONS_SETTLED_REGISTER_V001.md
RELAY_PASTE_179_2026-07-31.md
```

Exclusions:

```text
a32_holdout/custodian_private/ [pruned; not entered or listed]
.git objects, binaries, attachments, and measured-data payloads
rank-1 producer-algebra and PATHLESS-CLAIMED work
pin spectral-condition and unit-value-convention work
unrelated S1-S6 taxonomies except the exact S3 collision carrier
candidate-formula evaluation and every downstream numerical target
this artifact itself for the pre-existing-spec correspondence question
```

The semantic set used the exact families
`record_energy_equals_total_gravitating_energy`, `branch-energy difference
equals gravitating closure energy`, and `equality-to-closure-energy
certificate`. The independent spec-shape set used only the exact declarations
`specified_for_test = true`, `Status: Q-52 TEST SPECIFICATION`, and
`Q-52 TEST SPECIFICATION ONLY`. Both sets were generated with recursive
NUL-delimited searches, converted to sorted path lists, and intersected with
`comm -12`. Identifier-boundaried `S3` was then used during candidate
inspection. Mirrors were retained in the file list and hash-deduplicated only
after inspection.

```text
search_path_list_reused_as_second_search_input =
  PROHIBITED_AND_NOT_PERFORMED
  [PROCESS_METHOD_ATTESTATION; NON-Q54_RESULT]
```

Reviewed input hashes:

```text
S1 = e6bf47f6a7b21c89ae1142e5e0d57d5169d011cb64b3e3b0e906df67bbf0d77e
S2 = ecfbab95138b55cbf1b469e6bb66eb8dfba8d53f3250dff149f7c1ccafc27b8d
S4 = f305e0d77cc39f811f647c11401f902a94ac1c792b4280ae966cb1a103148d39
primary_gate = b00683c2c7a508a0fec7f2fe089ce64656bd4de832b8c8f189ce1c1007157dd6
depth_report = 6f09985d93db95aadd79d42f74fec75bb13751f3f08ea6ad19ff61d4bdf47e42
```

### 1.2 Pre-existing dedicated S3 specification

The exact semantic/spec-shape intersection produced six paths containing
three byte-distinct payloads. Inspection found the R1 and R2 mirrors of the
neighboring S1, S2, and S4 specifications, but no independently declared S3
domain, codomain, relation, stop, and failure-capable test suite.

```text
preexisting_dedicated_selector_ladder_S3_Q52_spec_found = false | TYPE-S |
  roots: R1, R2, R3 and the controlling packet in Section 1.1 |
  excl: Section 1.1; this artifact; role statements and neighboring specs do
  not count as the Q-69-distinct S3 discharge object |
  fences: semantic and exact Q-52 declaration sets generated independently;
  NUL-safe sorted intersection; identifier-boundaried S3 candidate inspection;
  mirrors retained in the path list and hash-deduplicated afterward |
  query: (record_energy_equals_total_gravitating_energy OR exact branch-energy/
  closure-energy equality family) INTERSECT (specified_for_test = true OR
  exact Q-52 TEST SPECIFICATION status) |
  candidate_files_inspected:
    R1/STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md
    R1/STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md
    R1/STAGE8_C_R_SELECTOR_S4_REFERENCE_CO_PARTICIPATION_SPEC_V001.md
    R2/STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md
    R2/STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md
    R2/STAGE8_C_R_SELECTOR_S4_REFERENCE_CO_PARTICIPATION_SPEC_V001.md
  byte_hash_groups:
    S1 R1=R2 e6bf47f6a7b21c89ae1142e5e0d57d5169d011cb64b3e3b0e906df67bbf0d77e
    S2 R1=R2 ecfbab95138b55cbf1b469e6bb66eb8dfba8d53f3250dff149f7c1ccafc27b8d
    S4 R1=R2 f305e0d77cc39f811f647c11401f902a94ac1c792b4280ae966cb1a103148d39
  qualifying_evidence_file_list: EMPTY
```

Before this artifact, the exact mathematical domain/codomain of S3 was
therefore `NO_VERDICT`; its semantic proof role was named, but not specified.

### 1.3 `S3` surface-token collision

Word boundaries do not disambiguate S3.

`STAGE8_GRAVITY_EVIDENCE_ADMISSION_AND_FIVE_STRATA_BINDING_V001.md:55-70`
defines:

> `S3 - Coupled record-bundle modulus gate`

By contrast,
`STAGE8_BRIDGE_ITEM4_SIX_OBJECT_DEPTH_REPORT_V001.md:194-230` defines:

> `S3. Branch-energy difference equals gravitating closure energy`

```text
five_strata_S3_is_selector_ladder_S3 = false | TYPE-R |
  test: S3-SCOPE-SIGNATURE-TEST; compare the cited carriers, inputs, semantic
  roles, and output obligations; one is a coupled-bundle modulus gate and the
  other is an HJ/closure-energy equality proof
```

`STAGE8_NAMESPACE_REGISTER_DRAFT_V004.md:25-30` contains only the two proposed
`Gamma_K` rows.

```text
S3_namespace_register_row_found = false | TYPE-S |
  roots: exact file STAGE8_NAMESPACE_REGISTER_DRAFT_V004.md |
  excl: every other namespace artifact and all concurrent namespace work |
  fences: identifier-boundaried S3 query; no row authored here |
  query: "(^|[^A-Za-z0-9_])S3([^A-Za-z0-9_]|$)" |
  qualifying_evidence_file_list: EMPTY
```

Local author names used here are:

```text
S3 [FIVE-STRATA-COUPLED-RECORD-BUNDLE-MODULUS-GATE]
S3 [SELECTOR-LADDER-HJ-CLOSURE-ENERGY-CORRESPONDENCE]
```

They are local disambiguators, not a namespace adoption.

## 2. What sealed S3 is and what the join must produce

### 2.1 Sealed semantic type

`STAGE8_BRIDGE_ITEM1_SIX_OBJECT_TRIAGE_V001.md:135-176` classifies S3 as
partially existing and states the would-build:

> `proof that the CTP branch-energy difference is the same energy entering the gravitational recoverability/closure condition`

`STAGE8_BRIDGE_ITEM4_SIX_OBJECT_DEPTH_REPORT_V001.md:225-230` repeats that
exact proof role. The S4 specification at
`STAGE8_C_R_SELECTOR_S4_REFERENCE_CO_PARTICIPATION_SPEC_V001.md:903-906`
calls it:

> `the separately owed equality-to-closure-energy certificate.`

The semantic type is therefore an ordinary equality/correspondence proof
certificate, not a scalar, energy value, candidate choice, or derived flag.
The terms **join** and **fork-join** are imported from graph/dependency
analysis. They apply because sealed text gives two directed prerequisite edges
into one proof object; they add no physical premise.

```text
Q80_new_class_required_for_S3_specification =
  NOT_TRIGGERED [PROCESS_CLASSIFICATION; NON-Q54_RESULT]

Q52_OBJECT_TYPE = HJ_CLOSURE_ENERGY_CORRESPONDENCE_CERTIFICATE
```

### 2.2 Explicit and missing dependency edges

The depth report at
`STAGE8_BRIDGE_ITEM4_SIX_OBJECT_DEPTH_REPORT_V001.md:198-208` gives:

> `S3 branch-energy equals gravitating closure energy`
>
> `  -> S2 constant HJ energy certificate`
>
> `  -> S4 reference-subtraction / no-spectator theorem`

Item 1 at `STAGE8_BRIDGE_ITEM1_SIX_OBJECT_TRIAGE_V001.md:329-342`
independently gives `S2 -> S3`, `S4 -> S3`, and labels `S3 -> S5` inferred.

But the S3 depth report at `:210-215` also names:

> `gravitating closure energy definition in the complete action = false | TYPE-U`
>
> `proof branch-energy difference is that closure energy = false | TYPE-U`

and the primary gate at
`BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:171-180` requires:

> `one target-independent complete source-record-gravity action`

to derive the HJ energy, equality, reference, and exclusions. Thus the printed
DAG is a valid compressed/topological skeleton, but not a complete S3 input
manifest. The join must carry a common S1 provenance handle and an S1-derived
closure-energy functional in addition to the S2 and S4 certificates.

```text
compressed_selector_dependency_skeleton_survives = true

printed_S3_dependency_manifest_complete = false | TYPE-R |
  test: S3-PRINTED-EDGE-SCHEMA-COMPLETENESS-TEST; compare the printed S2/S4
  edge list at the depth report :198-208 with its separately listed TYPE-U
  complete-action closure-energy definition at :210-215 and the same-action
  requirement at the primary gate :171-180; the printed edge list omits the
  closure-functional/common-origin input

S3_timeflow_to_required_proper_interval_correspondence_is_core_S3_input =
  false | TYPE-R |
  test: PRIMARY-GATE-CLAUSE-ROLE-DECOMPOSITION; the primary gate :38-39 states
  branch/closure-energy equality as condition 2, while :42-43 states the
  required time correspondence separately as condition 4; the sealed S3
  dependency carrier :194-215 assigns only the equality role to S3
```

Supported skeleton:

```text
S1 -> {S2, S4} -> S3 -> S5 [SEALED INFERENCE] -> S6
```

Expanded S3 input shape specified here:

```text
CORE
same S1 instance -> S2 HJ/constancy certificate -------------+
                 -> S4 reference/co-participation certificate +-> S3_CORE
                 -> S1-derived closure-energy functional -----+
P8 common domain + P10 reference adapter --------------------+

CORE TEST
P13 nontrivial equivalent-representation packet -> T8A/T8B only

FULL GATE / NAMED CLASSIFICATION
S3_CORE + P9 time correspondence + P12 applicability packet -> classifier
```

### 2.3 Exact output required

For the identification to follow, S3 must produce five distinct outputs:

```text
O1. one common-origin certificate tying every input to the exact same S1
    action, state, boundary/time-flow data, and stationary problem;
O2. one reference-fixed HJ branch-energy functional obtained through P10;
O3. one S1-derived gravitating-closure-energy functional, proven to be the
    energy actually consumed by the closure condition;
O4. an extensional functional-identity proof O2 = O3 on all of P8, after the
    S4 retained/excluded support partition, not at one endpoint;
O5. a separately routed applicability/classification result that compares the
    derived O3 signature with both named candidate signatures and yields one
    of: unique identity, ambiguity, or a Q-80 new-class record.
```

O4 is the core sealed S3 role. O5 is required to turn that derived energy into
a named-candidate identification. O4 without O5 is necessary but insufficient
to close the named fork because the primary gate at `:74-79` says:

> `These are both standard, geometrically meaningful energies, but they are conjugate to different boundary/time choices.`

and:

> `neither finite-boundary Brown-York energy nor asymptotic ADM/Misner-Sharp energy is automatically the Hamiltonian conjugate to the local tip-to-tip proper interval.`

output_fence_status = NO_VALUE_SCALE_INTERVAL_ROOT_OR_DOWNSTREAM_S5_S6_VERDICT
  [PROCESS_FENCE_ATTESTATION; NON-Q54_RESULT]

## 3. Hostile audit of S1, S2, and S4 interfaces

### 3.1 S1

At `STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md:64-89`,
S1 is a finite package with cell domain, field content, CTP branch data,
action/boundary terms, state/preparation, time flow, stationary problem, and
provenance. Its output is:

> `enough data to define an on-shell CTP action difference and its Hamilton-Jacobi conjugate energy.`

The tuple has no gravitating-closure-energy functional output. Its field
completeness condition at `:107-120` anticipates a future closure-energy
comparison, but does not construct the right-hand-side object. The S3 depth
report separately keeps that definition TYPE-U.

```text
S1_gravitating_closure_energy_functional_export_found = false | TYPE-S |
  roots: exact S1 spec and S3 depth report |
  excl: prose completeness requirements, future-use flags, and a named
  closure-side candidate that do not export a Q-69-distinct functional |
  fences: exact tuple/output/codomain inspection; no formula promoted to object |
  query: gravitating closure energy; closure energy; Output; S1 tuple |
  candidate_files_inspected:
    STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md
    STAGE8_BRIDGE_ITEM4_SIX_OBJECT_DEPTH_REPORT_V001.md
  qualifying_output_slot_file_list: EMPTY

S1_spec_contract_sufficient_for_S3_closure_RHS = false | TYPE-R |
  test: S1-TO-S3-CODOMAIN-COMPARISON; the exact S1 tuple/output lacks the
  closure-energy functional that the S3 depth report independently lists TYPE-U
```

S1 also specifies a stationary solution class but not an actual nonempty
first-durable class at `:183-195`.

### 3.2 S2

At `STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md:94-110`, S2 is:

> `a proof certificate over the S1 stationary problem.`

It defines the symbolic HJ record energy as the conjugate derivative of the
on-shell branch-action difference and proves constancy on the declared
stationary class. F1-F6 at `:114-190` require exact S1 provenance, a conjugate
variable, differentiability domain, stationary class, full-class constancy,
and boundary/reparametrization stability. These are the correct future left-
hand-side ingredients.

Two hostile checks fail the present interface.

First, S2 advertises constancy on the first durable-record saddle at `:69-74`,
while S1 supplies only the class of stationary saddles it admits. The earlier
S4 audit records the missing designation at
`STAGE8_C_R_SELECTOR_S4_REFERENCE_CO_PARTICIPATION_SPEC_V001.md:598-635`.

Second, S2 T3 at `:247-259` quantifies over the S1 stationary solution class
without requiring that class to be nonempty.

```text
S2_stationary_domain_nonempty_gate_found = false | TYPE-S |
  roots: exact S1 and S2 specs |
  excl: a generic class declaration without existence/nonemptiness proof |
  fences: no first-durable member inferred from a target label |
  query: nonempty; non-empty; existence of stationary solution/saddle;
  first durable |
  candidate_files_inspected:
    STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md
    STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md
  qualifying_evidence_file_list: EMPTY

S2_constancy_test_nonvacuous_as_written = false | TYPE-R |
  test: EMPTY-STATIONARY-CLASS-COUNTERMODEL; an empty admitted class has no
  constancy counterexample, while current T3 contains no nonemptiness failure
  leg
```

The S2 specification therefore partially supplies the correct future LHS
type, but it supplies no executable object today and cannot by itself certify
the nonempty common S3 domain.

### 3.3 S4

S4's future codomain at
`STAGE8_C_R_SELECTOR_S4_REFERENCE_CO_PARTICIPATION_SPEC_V001.md:798-829`
contains:

> `forced_reference_prescription`
>
> `sector_co_participation_or_exclusion_certificate`
>
> `same_support_certificate`

plus common-shift/non-erasure, target-independence, isolation, and provenance.
Its partition at `:831-869` requires every retained closure contribution to
participate in the record-action difference and every exclusion to prove
non-contribution. Those are the correct future S4 inputs.

But S4 explicitly stops before construction and says at `:886-887`:

> `It does not choose a reference functional, prove a sector theorem, or instantiate a closure energy.`

Its local S4.P9 stationary class at `:771-774` is not required nonempty. S4's
T0/T8 at `:964-976` contain no explicit empty-S4.P9 rejection.

```text
S4_stationary_domain_nonempty_gate_found = false | TYPE-S |
  roots: exact S4 specification |
  excl: S4.P11/S4.P12 nonemptiness; generic full-class language without
  existence |
  fences: exact S4.P9/T0/T8 inspection |
  query: nonempty stationary; non-empty stationary; stationary existence |
  candidate_files_inspected:
    STAGE8_C_R_SELECTOR_S4_REFERENCE_CO_PARTICIPATION_SPEC_V001.md
  qualifying_evidence_file_list: EMPTY

S4_candidate_test_nonvacuous_on_S4_P9_as_written = false | TYPE-R |
  test: EMPTY-P9-COUNTERMODEL; a derived empty S4.P9 plus otherwise universal
  certificates has no counterexample, while T0/T8 does not reject emptiness
```

This is a defect in the earlier S4 specification authored by this lane. It is
reported here and not repaired.

### 3.4 Missing cross-interface adapters

S1 permits its reference slot to be fixed or explicitly missing at
`STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md:283-295`.
S2 then defines its HJ energy from that S1 action. S4 derives a forced reference
from the reference-free S1 core. No current contract maps that S4 prescription
onto the S2 energy or proves that an S1-fixed reference is the S4-derived
baseline.

```text
S2_energy_to_S4_reference_application_adapter_found = false | TYPE-S |
  roots: exact S1, S2, and S4 specifications |
  excl: shared token "reference", future S4.T7 promise, flags, and this S3 spec |
  fences: Q-69 object separation; a fixed slot is not a derived adapter |
  query: reference with HJ_record_energy; referenced HJ energy;
  branch-energy with forced reference; adapter; apply; map |
  candidate_files_inspected:
    STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md
    STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md
    STAGE8_C_R_SELECTOR_S4_REFERENCE_CO_PARTICIPATION_SPEC_V001.md
  qualifying_evidence_file_list: EMPTY
```

The primary gate at `:42-43` separately requires:

> `the time parameter conjugate to that energy is the tip-to-tip proper interval T_R`

The bounded S1/S2 packet specifies a time-flow parameter, but no correspondence
to that required interval parameter.

```text
S1_S2_timeflow_to_required_proper_interval_correspondence_found = false | TYPE-S |
  roots: primary bridge gate and exact S1/S2 specs |
  excl: pin and unit-value work; conventions; downstream interval solutions |
  fences: input typing only; no normalization or value inferred |
  query: tip-to-tip proper interval; time parameter conjugate; time-flow;
  correspondence; map |
  candidate_files_inspected:
    BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md
    STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md
    STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md
  qualifying_evidence_file_list: EMPTY
```

### 3.5 Exact input map

| Producer | Exact future output S3 consumes | Present audit |
|---|---|---|
| S1 | One concrete package instance carrying the action, state/preparation, CTP branches, boundary data, time flow, stationary problem, and provenance; P11 must derive the closure-energy functional from that same instance. | Package type specified; object and P11 unbuilt. |
| S2 | `HJ_record_energy`, its conjugate variable and differentiability domain, proof of constancy on the full common nonempty domain, stability, and exact S1 provenance. | Correct future LHS type specified; object unbuilt; nonempty first-durable domain guard absent. |
| S4 | `forced_reference_prescription`, common-shift invariance, retained-energy non-erasure, exhaustive sector co-participation/exclusion, same-support, target-independence, isolation, and exact S1 provenance. | Correct future reference/support bundle specified; object unbuilt; S4.P9 nonemptiness and the S2-reference adapter absent. |
| P8, P10, P11 | Common nonempty domain, reference adapter, and S1-derived closure-energy functional. | All TYPE-U core-construction inputs. |
| P13 | Complete nontrivial equivalent-representation class and exact transports. | TYPE-U; independent core-test input, not physical equality input. |
| P9, P12 | Required time correspondence plus complete pre-target signatures and proved applicability-or-inapplicability maps for both named candidates. | TYPE-U; required only for the separately routed full-gate/named-classification leg. |

input_map_flag_substitution_status = PROHIBITED
  [PROCESS_Q69_ATTESTATION; NON-Q54_RESULT]

### 3.6 Interface verdict

The objects and their status flags remain distinct under Q-69. A true flag can
never substitute for the S1 package, S2 certificate, S4 certificate, P10
adapter, or P11 closure functional.

```text
S3_join_inputs_dischargeable_by_status_flags = false | TYPE-R |
  test: Q69-NODE-IDENTITY-TEST; compare each exact object type and provenance
  carrier with its separately named derived/status/test flag

current_S1_S2_S4_specs_supply_complete_S3_interface = false | TYPE-R |
  test: S3-INPUT-SIGNATURE-COMPARISON; P8, P10, and P11 are absent from the
  current core-construction exports, P13 is absent from the nonvacuous core
  test inputs, P9/P12 are absent from the full-gate/named leg, and the S2/S4
  empty-domain countermodels fire
```

The current specifications are valuable partial interfaces, but they do not
make S3 executable.

## 4. Q-52 specification of S3

### 4.1 Object names and epistemic type

The Q-69-distinct core object is:

```text
BRIDGE_SELECTOR_S3_HJ_CLOSURE_ENERGY_CORRESPONDENCE_CERTIFICATE
```

The classification consumer carried in the same test package is:

```text
S3_ENERGY_CLASSIFICATION_CERTIFICATE
```

They are separate certificate nodes and separate verdict owners. The second
cannot substitute for the first, and the first cannot silently name a
candidate.

```text
BRIDGE_SELECTOR_S3_HJ_CLOSURE_ENERGY_CORRESPONDENCE_CERTIFICATE_derived =
  false | TYPE-U |
  would-build: construct Cert_S3_CORE from complete Dom(S3_CORE), then supply
  an independent construction witness, P13, and execute T-1A, T0A, T1, T2A,
  T3 through T6, T7A/B, T8A/B, T11A, T12A, and T13A

S3_ENERGY_CLASSIFICATION_CERTIFICATE_derived =
  false | TYPE-U |
  would-build: consume a derived Cert_S3_CORE plus P9 and P12, then execute
  T-1B, T0B, T9A, T9B, T10A, T10B when applicable, T11B, T12B, and T13B
  without a post-target choice
```

### 4.2 Domain

Core domain:

```text
Dom(S3_CORE) =
  (
    exact_S1_package_instance,
    exact_S2_HJ_constancy_certificate_instance,
    exact_S4_reference_co_participation_certificate_instance,
    P8_common_nonempty_first_durable_domain_and_pullbacks,
    P10_reference_application_adapter,
    P11_S1_derived_gravitating_closure_energy_functional
  )
```

Classification domain:

```text
Dom(S3_CLASSIFICATION) =
  (
    Cert_S3_CORE,
    P9_timeflow_to_required_proper_interval_correspondence,
    P12_named_candidate_functional_signature_and_applicability_packet
  )
```

Every core member must carry the same S1 provenance identifier or a derived
identity/pullback witness to it. P9 must be derived from that S1 time flow.
P12 instead carries independent pre-target source provenance plus exact maps
to the core domain; it is not asserted to originate in S1. A list of true
flags is not a domain member.

### 4.3 Codomain and partial-input protocol

For complete core inputs:

```text
Cod(S3_CORE) = Cert_S3_CORE union Failure_S3_CORE

Cert_S3_CORE =
  (
    common_S1_provenance_certificate,
    common_nonempty_first_durable_domain_certificate,
    reference_fixed_HJ_energy_functional,
    closure_energy_functional_and_role_certificate,
    S4_sector_and_support_transport_certificate,
    HJ_closure_extensional_identity_certificate,
    representation_invariance_certificate,
    target_independence_certificate,
    downstream_isolation_certificate,
    provenance_and_fences
  )
```

For complete classification inputs:

```text
Cod(S3_CLASSIFICATION) =
  UNIQUE_NAMED_FUNCTIONAL_IDENTITY
  union AMBIGUOUS_NAMED_MATCH_FAILURE
  union Q80_NEW_ENERGY_CLASS_RECORD
  union Failure_S3_CLASSIFICATION
```

`UNIQUE_NAMED_FUNCTIONAL_IDENTITY` carries an abstract identifier for exactly
one candidate and its functional-identity proof; this specification does not
instantiate that identifier. `AMBIGUOUS_NAMED_MATCH_FAILURE` carries two or
more surviving identities. `Failure_S3_CLASSIFICATION` carries the exact
failed structural, input, packet, Q-80-record-validity, target-blindness, or
isolation verdict and its witness.

Complete derived zero-match inputs must emit a constituted Q-80 record rather
than a bare trigger:

```text
Q80_NEW_ENERGY_CLASS_RECORD =
  (
    new_class_name,
    definition_from_the_unmatched_derived_signature,
    explicit_exclusions_from_each_existing_candidate_class,
    exact_existing_category_assumptions_resisted_by_the_object,
    failure_capable_membership_and_nonmembership_tests,
    complete_zero_match_and_named_pair_nonexhaustiveness_proof,
    provenance_and_fences
  )
```

This artifact cannot instantiate that record before a complete zero-match
result exists. The record type ensures that a future zero match does not end
at `NAMING_REQUIRED`; it must name, define, exclude, and make the new class
falsifiable as Q-80 requires.

Missing or inapplicable prerequisites are outside the complete domains:

```text
Eval_S3(partial_input) = NO_VERDICT |
  reason: name every absent or inapplicable domain member
```

The codomains exclude S5 marginality, S6 interval selection, every numerical
value, and every alpha/response conclusion.

### 4.4 Required core relations

All relations are symbolic specifications, not evaluations.

Core common origin:

```text
origin(S2) = origin(S4) = origin(P8) = origin(P10) = origin(P11)
           = exact_S1_package_instance
```

Reference application:

```text
E_HJ_ref := P10(
  S2.HJ_record_energy,
  S4.forced_reference_prescription,
  P8.common_domain
)
```

P10 must preserve S2's constancy certificate and S4's common-shift,
non-erasure, sector, and support certificates. It may not replace either by a
new convention.

Closure-energy provenance:

```text
E_closure := P11(exact_S1_package_instance, S4.retained_excluded_partition)

closure_condition_consumes(E_closure) = true
```

The second line is a role certificate, not a numerical use of the closure
condition.

Core equality:

```text
for every configuration q in P8.common_domain:
  E_HJ_ref[q] = E_closure[q]
```

This must be extensional functional identity on the full nonempty domain. A
single endpoint equality, equality after a target-dependent subtraction, or
equality only after deleting a retained S4 sector does not satisfy it.

### 4.5 Required named-candidate relations

Full-gate time conjugacy is supplied only here:

```text
P9 maps the S1/S2 conjugate time-flow parameter to the proper-interval
parameter required by the primary gate, with domain and provenance preserved.
```

This artifact does not supply that map or assign a value to either parameter.

From the derived core object form the structural signature:

```text
Sig_full(E_closure; P9) =
  (
    variational_origin,
    physical_domain,
    stationary_class,
    boundary_class,
    time_flow_conjugacy,
    reference_rule,
    retained_sector_support,
    closure_role
  )
```

P12 supplies the same fields, exact symbolic candidate functionals, exact
domain transports, independently checkable proof inputs, and an exact proved
applicability-or-inapplicability map for each named candidate. A proved-
inapplicable candidate is a valid non-match. An applicable candidate matches
only with a checkable full-domain extensional functional-identity proof.
Shared notation, formula resemblance, one endpoint, unsuccessful
counterexample search, or agreement after an extra reference choice is not a
match.

```text
match(candidate_i) :=
  P12 proves candidate_i applicable on P8.common_domain
  AND Sig(candidate_i) = Sig_full(E_closure; P9)
  AND candidate_i[.] = E_closure[.] extensionally on that domain
```

Outcome partition:

```text
exactly one match  -> UNIQUE_NAMED_FUNCTIONAL_IDENTITY
two or more matches -> AMBIGUOUS_NAMED_MATCH_FAILURE
zero matches with all inputs complete -> Q80_NEW_ENERGY_CLASS_RECORD and a
  TYPE-R named-pair-nonexhaustiveness witness
invalid complete packet/test input -> Failure_S3_CLASSIFICATION
missing/inapplicable input -> NO_VERDICT
```

### 4.6 Construction witness and stop

```text
S3_CORE_CONSTRUCTION_WITNESS_derived = false | TYPE-U |
  would-build: one target-independent candidate witness constructing every
  physical relation field from complete Dom(S3_CORE), with separately
  checkable proof terms; P13 and the core tests would certify it

S3_CLASSIFICATION_WITNESS_derived = false | TYPE-U |
  would-build: one pre-target witness applying complete P9/P12 to Cert_S3_CORE
  and producing exactly one declared classification outcome, including a
  fully constituted Q-80 record on complete zero match
```

This artifact stops before P8-P13 and both witnesses. It neither instantiates
the closure functional nor applies a named candidate formula.

## 5. Shape of the non-choosing identification argument

### 5.1 Necessary sequence

The identification would follow only in this order:

```text
A. Complete one S1 instance and prove P8 common-domain pullbacks.
B. Consume S2 to obtain its symbolic constant HJ energy on that domain.
C. Use P10 to apply S4's forced reference and carry S4's sector/support proof.
D. Derive P11 from the same S1 action and prove it is the closure-consumed energy.
E. Prove the full-domain functional identity between the outputs of C and D.
F. Validate representation invariance nonvacuously with P13.
G. Apply P9 to attach the primary gate's required time-conjugacy correspondence.
H. Derive the full signature of E's identified energy.
I. Apply P12's pre-target applicability-or-inapplicability maps and checkable
   functional identities.
J. Only an exactly-one-match theorem yields a named identification; complete
   zero match instead requires the constituted Q-80 record.
```

```text
argument_choice_target_use_and_expression_evaluation_status =
  PROHIBITED_AND_NOT_PERFORMED
  [PROCESS_FENCE_ATTESTATION; NON-Q54_RESULT]
```

### 5.2 Bare equality is not enough

The core equality certificate lacks the exact boundary/time-flow applicability
maps for the two named candidates. The primary gate's statement that the
candidates are conjugate to different boundary/time choices supplies the
counterexample to automatic identification.

```text
bare_S3_equality_certificate_sufficient_to_name_energy_candidate = false | TYPE-R |
  test: NAMED-CANDIDATE-APPLICABILITY-CODOMAIN-TEST; compare Cert_S3_CORE with
  P9/P12 and the gate's distinct boundary/time-flow conjugacies; the core
  codomain contains no required time correspondence, complete candidate
  applicability map, or unique match proof

full_S3_package_named_identification_status = NO_VERDICT |
  reason: Cert_S3_CORE, P9, and P12 are unbuilt and no classification test ran
```

### 5.3 No winner named

```text
energy_candidate_choice_status =
  PROHIBITED_AND_NOT_PERFORMED
  [PROCESS_FENCE_ATTESTATION; NON-Q54_RESULT]

named_candidate_winner_recorded =
  NONE [PROCESS_FENCE_ATTESTATION; NON-Q54_RESULT]

energy_identification_fork_closed = false | TYPE-U |
  would-build: complete and derive the core and classification certificate
  nodes, then obtain an exactly-one-match result without candidate-specific
  fitting

future_complete_S3_matches_neither_named_candidate = NO_VERDICT |
  reason: no S3 energy or complete P9/P12 packet exists; if a future complete
  execution establishes zero matches, it refutes named-pair exhaustiveness and
  must emit the constituted Q-80 class record
```

## 6. Failure-capable tests and verdict wiring

### 6.1 Wiring rule

Each test reports only to the property named in its target column. Missing
prerequisites return `NO_VERDICT`, not a physical refutation. Core equality,
named applicability, unique classification, Q-80 triggering, S5/S6, and the
derived flag are distinct verdict owners.

### 6.2 Test table

| Test | Failure-capable method | Exact target verdict | Non-targets |
|---|---|---|---|
| T-1A — core structural type | Require the core node, exact core domain/codomain, Q-69 object/flag separation, and no named-classification output in the core codomain. A missing slot, merged node/flag, or classification output fails. | `S3_core_object_type_conforms` | No physical equality, P9/P12, or classification verdict |
| T-1B — classification structural type | Require the distinct classification node, its P9/P12 domain, all four codomain branches, and Q-69 separation from core. A missing failure/Q-80 branch or merged node fails. | `S3_classification_object_type_conforms` | No core type or equality verdict |
| T0A — core-input applicability | Require actual derived S1/S2/S4 objects plus P8, P10, and P11. Missing/inapplicable inputs return `Eval_S3 = NO_VERDICT`; wrong supplied types fail applicability. | `S3_core_input_applicability` | No equality, classification, P9/P12/P13, or derived flag |
| T0B — classification-input applicability | Require a derived `Cert_S3_CORE` plus correctly typed P9 and P12. Missing inputs return `NO_VERDICT`; wrong supplied types return `Failure_S3_CLASSIFICATION`. | `S3_classification_input_applicability` | No core type/equality or match-cardinality verdict |
| T1 — common S1 provenance | Resolve the S2, S4, P8, P10, and P11 provenance handles. Any unmatched S1 action/state/boundary/time-flow/stationary origin refutes common origin. | `S3_common_S1_provenance` | No functional equality or P9/P12 verdict |
| T2A — common-domain nonemptiness/completeness | Require P8 to be nonempty, first-durable, and exhaustive for every configuration on which S2/S4/P11 claims are made. An empty class, missing pullback, or omitted admitted configuration fails. | `S3_common_domain_valid_and_nonempty` | No time-conjugacy or equality verdict |
| T3 — S2 LHS export | Verify S2 exports a well-typed symbolic HJ energy, differentiability domain, and nonvacuous full-domain constancy certificate. Residual dependence or missing export fails. | `S3_HJ_energy_input_well_typed_and_constant` | No closure-functional verdict |
| T4 — reference application | Apply P10 and test that it uses exactly S4's forced prescription, preserves S2 constancy, and introduces no additional reference/subtraction, whether pre-target or post-target. Any unforced extra constant or other subtraction refutes the adapter. | `S3_reference_application_adapter_valid` | No S4 derivation or core equality verdict |
| T5 — closure-functional provenance/role | Trace P11 to the same S1 action and verify that the stated closure condition consumes it. A foreign functional, named-candidate substitution, or post-target definition fails. | `S3_closure_energy_functional_well_typed` | No candidate winner or equality verdict |
| T6 — S4 sector/support transport | Apply S4's exhaustive retained/excluded partition and same-support certificate to both sides. One retained closure contribution missing from the referenced HJ side, or one unjustified exclusion, refutes transport. | `S3_S4_sector_support_transport_valid` | No generic S4 or equality verdict |
| T7A — identity-proof certificate validity | Require a checkable symbolic proof quantified over the P8-certified exhaustive domain; an independent checker must validate the domain and every inference branch. A malformed or invalid proof fails certificate validity and leaves physical identity `NO_VERDICT`. | `S3_extensional_identity_proof_certificate_valid` | No physical identity or classification verdict |
| T7B — extensional identity | After T7A PASS, a valid total proof passes identity. Independently, one checked symbolic residual or admissible counterexample refutes identity. Unsuccessful counterexample search without a valid total proof returns `NO_VERDICT`, never PASS. | `S3_HJ_closure_extensional_identity` | No proof-certificate-validity or classification verdict |
| T8A — P13 packet validity/nonvacuity | Require P13's exhaustive class, at least one nonidentity representative, exact transports, a checkable completeness witness, and pre-result target-independent provenance for its generator, transports, and checker. Missing P13 returns `NO_VERDICT`; an invalid or tailored supplied packet fails packet validity and leaves physical invariance `NO_VERDICT`. | `S3_equivalent_representation_test_packet_valid` | No representation-invariance, original-equality, or classification verdict |
| T8B — representation invariance | After T8A PASS, check every certified representative and transport. One checked inequivalent transported identity refutes invariance; checking the entire certified class without discrepancy passes. | `S3_correspondence_representation_invariant` | No P13-validity, original-equality, or classification verdict |
| T9A — required time correspondence | Test P9 for a target-independent domain-preserving correspondence between the S1/S2 conjugate time flow and the primary gate's required proper-interval parameter, plus a checkable chain-rule proof that HJ conjugacy is preserved under the map. Missing P9/proof returns `NO_VERDICT`; invalid proof, domain loss, or downstream selection fails P9. | `S3_required_time_conjugacy_correspondence_valid` | No unit-value, interval solution, or core verdict |
| T9B — P12 validity/completeness | Require pre-target, separately sourced complete signatures, exact symbolic functionals, exact P8-domain transports, checkable identity/nonidentity proof inputs, and a proved applicable-or-proved-inapplicable map for each named candidate. Omission, unproved applicability status, missing field/object/transport, or post-result construction fails. A proved empty applicability domain is a valid inapplicability result. | `S3_named_candidate_packet_valid_and_complete` | No match-cardinality verdict |
| T10A — definitive match cardinality | After T9A/T9B PASS, classify each candidate by either a checked full-domain identity proof, a proved inapplicability, or a checked nonidentity witness. Unresolved identity returns `NO_VERDICT`. Exactly one match yields unique correspondence; both matches refute uniqueness; zero definitive matches refutes named-pair exhaustiveness and activates T10B. | `S3_named_candidate_match_cardinality` | No core equality, Q-80 record validity, or derived flag |
| T10B — Q-80 zero-match record | Applicable only after a complete zero-match T10A result. Require a concrete new class name, definition, exclusions, an exact statement of which existing category assumptions the object resists, failure-capable membership/nonmembership tests, zero-match proof, and provenance. Missing record is TYPE-U/`NO_VERDICT`; an invalid supplied record fails; a complete record passes. | `S3_Q80_new_energy_class_record_valid` | No match cardinality, core equality, or named winner |
| T11A — core target blindness | Trace every core input/rule and the P13 generator/transports/checker to pre-result provenance. Use of a desired value, selected endpoint, downstream response, tailored representation class, or post-hoc reference fails. | `S3_core_target_independence` | No equality or named-candidate verdict |
| T11B — classification target blindness | Trace P9, P12, and every matching rule to pre-result provenance. Candidate-specific domain narrowing, post-result candidate signature/functional construction, or preferred-name routing fails. The Q-80 record is intentionally formed only after a definitive zero match, but its schema/router/tests must be pre-result and its contents may depend only on the already-derived unmatched signature and zero-match proof. | `S3_classification_target_independence` | No core equality or match-cardinality verdict |
| T12A — core downstream isolation | Check that no core pass flips S5, S6, interval, response, coupling, alpha, or classification flags. One silent flip fails. | `S3_core_downstream_isolation` | No core physical-property verdict |
| T12B — classification downstream isolation | Check that no classification outcome flips S5, S6, interval, response, coupling, or alpha flags. One silent flip fails. | `S3_classification_downstream_isolation` | No core or classification-content verdict |
| T13A — core composite | Require T-1A, T0A, T1, T2A, T3 through T6, T7A, T7B, T8A, T8B, T11A, and T12A to be applicable and PASS. Any failed mandatory leg fails the core composite; any required `NO_VERDICT` makes the composite `NO_VERDICT`. | `S3_core_candidate_valid_on_declared_domain` | Never `S3_derived`; never classification |
| T13B — classification composite | Require T-1B, T0B, T13A, T9A, T9B, T10A, T11B, and T12B, plus T10B only on the zero-match branch. An exactly-one T10A outcome yields unique named identity; both matches yield ambiguity; zero matches completes only with T10B PASS and yields the Q-80 record; missing input returns `NO_VERDICT`; invalid complete input returns `Failure_S3_CLASSIFICATION`. | `S3_energy_classification_outcome` | Never core equality, S5/S6, or `S3_derived` |

### 6.3 Unexecuted status and wiring audit

```text
S3_Tminus1A_through_T13B_suite_executed = false | TYPE-U |
  would-execute: provide actual independently derived domain members,
  construction witnesses, fixtures, and independent failure oracles

S3_core_candidate_valid_on_declared_domain = NO_VERDICT |
  reason: outstanding prerequisites are the actual S1/S2/S4 objects,
  P8/P10/P11, and P13

S3_named_energy_identification_valid = NO_VERDICT |
  reason: outstanding prerequisites are the core certificate, P9, and P12
```

T7A and T7B separate proof-certificate validity from physical identity. T8A
and T8B separate P13 validity from physical representation invariance. T9A
reports only to the required time correspondence; T9B reports only to packet
validity; T10A reports only match cardinality; T10B reports only Q-80 record
validity. The A/B structural, applicability, target-blindness, and isolation
splits prevent classification inputs from gating core. T13A cannot name a
candidate; T13B cannot change the core equality verdict. No test reports to a
derived flag.

```text
S3_test_verdict_wiring_audited = true

test_can_set_S3_derived_flag = false | TYPE-R |
  test: S3-TEST-CODOMAIN-ROUTER-AUDIT; inspect every target in Section 6.2;
  neither S3 derived flag occurs in a test codomain
```

### 6.4 Pre-seal hostile-review refutations

The pre-seal draft failed five specification tests. They are recorded rather
than hidden by the corrected wiring:

```text
preseal_unsplit_core_and_classification_router_valid = false | TYPE-R |
  test: CORE-CLASSIFICATION-DEPENDENCY-SEPARATION; the former T-1/T0/T13A
  route made P12 gate the core equality despite the declared domain split

preseal_counterexample_search_only_T7_has_a_valid_PASS_route = false | TYPE-R |
  test: T7-PASS-WITNESS-CODOMAIN; absence of a found residual does not prove
  full-domain identity, so a total checked proof was missing

preseal_representation_test_nonvacuous_without_P13 = false | TYPE-R |
  test: EMPTY-OR-SINGLETON-REPRESENTATION-CLASS-COUNTERMODEL; the former T8
  could pass without a nonidentity equivalent representation

preseal_proved_empty_candidate_applicability_domain_makes_P12_invalid =
  false | TYPE-R |
  test: APPLICABILITY-PARTITION-TEST; proved inapplicability is a valid
  non-match, whereas only missing or unproved applicability status is invalid

preseal_bare_Q80_naming_required_token_satisfies_Q80 = false | TYPE-R |
  test: Q80-RECORD-SCHEMA-COMPARISON; the token lacked a class name,
  definition, exclusions, falsifiable tests, and provenance
```

These refute draft interfaces only. They are not evidence about either energy
candidate or a future constructed S3 object.

## 7. Falsifiers and present verdict

### 7.1 Failure witnesses

A complete proposed S3 candidate/package is failure-capable through:

```text
F1. S2, S4, P8, P10, or P11 carries a different S1 origin.
F2. The common first-durable stationary domain is empty or incomplete.
F3. S4's forced reference cannot be applied to S2 without changing constancy.
F4. The closure functional is not derived from S1 or is not closure-consumed.
F5. A retained S4 sector appears on only one side.
F6. A checked symbolic residual or admissible counterexample refutes
    extensional identity.
F7. A checked transported representative yields an inequivalent identity and
    refutes representation invariance.
F8. The proof uses a downstream target, selected endpoint, or post-hoc subtraction.
```

An invalid identity proof fails T7A and leaves physical identity `NO_VERDICT`.
An invalid P13 packet fails T8A and leaves physical representation invariance
`NO_VERDICT`. Neither is misrouted as physical content.

The named leg has these additional failure witnesses:

```text
F9. P9 fails the required correspondence, loses the domain, has foreign S1
    provenance, or is target-selected.
F10A. Missing/incomplete P12 or an unproved applicability status leaves the
      higher named-identification claim at NO_VERDICT / TYPE-U.
F10B. A supplied complete-but-malformed, wrong-typed, or post-result P12 emits
      Failure_S3_CLASSIFICATION. It does not refute either physical candidate.
F11. Both named candidates survive full functional identity and applicability;
     this refutes uniqueness.
F12. Naming one candidate requires an extra reference or boundary/time-flow
     choice; this refutes derivation without selection.
F13. Complete derived inputs produce zero named matches; this refutes
     exhaustiveness of the current named pair and triggers Q-80 class naming.
```

Zero fully tested matches is not forced into the ambiguity bin or `NO_VERDICT`:
with complete derived inputs it is both a refutation of named-pair
exhaustiveness and a Q-80 new-class trigger. Before those inputs exist,
zero-match status is `NO_VERDICT` because information is missing.

### 7.2 Present verdict

```text
S3_core_derivation_claim_status = NO_VERDICT |
  reason: P8/P10/P11, P13, and the actual S1/S2/S4 objects are unbuilt

S3_named_identification_claim_status = NO_VERDICT |
  reason: the core identity and P9/P12 applicability packet are unbuilt

S3_failure_capable_test_interfaces_specified = true
  [PROCESS_SPECIFICATION_ATTESTATION; NON-Q54_RESULT]

S3_test_suite_physical_execution_sufficiency = NO_VERDICT |
  reason: the independently derived inputs, P13 fixtures, proof checkers, and
  classification oracles do not yet exist
```

The specification attestation is a test-design statement, not a physical
result or derivation.

## 8. Q-54 negative registry

| Negative | Type | Evidentiary carrier |
|---|---|---|
| Present S1/S2/S4 interfaces make core S3 construction executable | TYPE-U | Actual objects plus P8/P10/P11 would build it, Sections 0 and 4 |
| Present inputs make core representation testing nonvacuous | TYPE-U | P13 would build the missing test packet, Sections 0 and 6 |
| Pre-existing dedicated selector-ladder S3 Q-52 spec recovered | TYPE-S | Roots/exclusions/query/candidate and empty qualifying lists, Section 1.2 |
| Five-strata S3 is selector-ladder S3 | TYPE-R | S3-SCOPE-SIGNATURE-TEST, Section 1.3 |
| Namespace V004 contains S3 | TYPE-S | Exact file and identifier query, Section 1.3 |
| Printed S3 dependency manifest is complete | TYPE-R | S3-PRINTED-EDGE-SCHEMA-COMPLETENESS-TEST, Section 2.2 |
| P9 time correspondence is a core S3 equality input | TYPE-R | PRIMARY-GATE-CLAUSE-ROLE-DECOMPOSITION, Section 2.2 |
| S1 exports a closure-energy functional | TYPE-S | Exact tuple/output inspection and empty output list, Section 3.1 |
| S1 contract suffices for the S3 RHS | TYPE-R | S1-TO-S3-CODOMAIN-COMPARISON, Section 3.1 |
| S2 has a nonempty stationary-domain gate | TYPE-S | Exact S1/S2 query and empty qualifying list, Section 3.2 |
| S2 constancy test is nonvacuous as written | TYPE-R | EMPTY-STATIONARY-CLASS-COUNTERMODEL, Section 3.2 |
| S4 has a nonempty S4.P9 gate | TYPE-S | Exact S4.P9/T0/T8 query and empty qualifying list, Section 3.3 |
| S4 candidate test is nonvacuous on S4.P9 as written | TYPE-R | EMPTY-P9-COUNTERMODEL, Section 3.3 |
| S2-to-S4 reference adapter recovered | TYPE-S | Exact S1/S2/S4 query and empty qualifying list, Section 3.4 |
| S1/S2 time-flow correspondence recovered | TYPE-S | Primary/S1/S2 query and empty qualifying list, Section 3.4 |
| Status flags can discharge S3 inputs | TYPE-R | Q69-NODE-IDENTITY-TEST, Section 3.6 |
| Current specs supply the complete S3 interface | TYPE-R | S3-INPUT-SIGNATURE-COMPARISON, Section 3.6 |
| S3 core and classification certificate nodes are derived | TYPE-U | Complete domains, test packet, and construction witnesses, Section 4 |
| Bare S3 equality is sufficient to name a candidate | TYPE-R | NAMED-CANDIDATE-APPLICABILITY-CODOMAIN-TEST, Section 5.2 |
| The named fork is closed | TYPE-U | Derive both S3 nodes and pass exactly-one matching, Section 5.3 |
| Future complete S3 fits neither named candidate | NO_VERDICT | Core/P9/P12 missing; a future complete zero match refutes pair exhaustiveness and requires a Q-80 record, Section 5.3 |
| S3 tests have executed | TYPE-U | Supply all concrete inputs and oracles, Section 6.3 |
| A test can set S3 derived | TYPE-R | S3-TEST-CODOMAIN-ROUTER-AUDIT, Section 6.3 |
| Pre-seal unsplit core/classification router was valid | TYPE-R | CORE-CLASSIFICATION-DEPENDENCY-SEPARATION, Section 6.4 |
| Pre-seal counterexample-only T7 had a PASS route | TYPE-R | T7-PASS-WITNESS-CODOMAIN, Section 6.4 |
| Pre-seal representation test was nonvacuous without P13 | TYPE-R | EMPTY-OR-SINGLETON-REPRESENTATION-CLASS-COUNTERMODEL, Section 6.4 |
| Proved empty candidate applicability makes P12 invalid | TYPE-R | APPLICABILITY-PARTITION-TEST, Section 6.4 |
| A bare Q-80 naming-required token satisfies Q-80 | TYPE-R | Q80-RECORD-SCHEMA-COMPARISON, Section 6.4 |
| Core derivation claim is decided | NO_VERDICT | Actual objects, P8/P10/P11, and P13 missing, Section 7.2 |
| Named-identification claim is decided | NO_VERDICT | Core identity and P9/P12 missing, Section 7.2 |
| Physical test-suite execution sufficiency is decided | NO_VERDICT | Inputs, P13, proof checkers, and classification oracles missing, Section 7.2 |

```text
TYPE_S_SCOPE_ESCAPE_STATUS = NONE
  [PROCESS_Q54_ATTESTATION; NON-Q54_RESULT]
```

TYPE-R results refute interface, vacuity, identity, sufficiency, or router
hypotheses; they do not refute a future physical S3 construction or either
named energy candidate.

## 9. Five requested answers

1. **What S3 is.** Sealed text names an ordinary proof that the S2 HJ
   branch-energy difference is the same S1-derived energy entering closure,
   after S4 reference/support transport. Its prior exact mathematical type was
   `NO_VERDICT`; Section 4 now specifies it under Q-52 without derivation.
2. **What it consumes.** S1 supplies the common action/state/boundary/time-flow/
   stationary provenance; S2 supplies the symbolic HJ energy and constancy;
   S4 supplies the forced reference, non-erasure, sector partition, same
   support, and target-blindness. Current core contracts omit P8/P10/P11 and
   the nonvacuous test packet P13; the full classification leg also lacks
   P9/P12. The S2/S4 stationary-domain tests admit empty-class vacuity.
3. **Specification.** `BRIDGE_SELECTOR_S3_HJ_CLOSURE_ENERGY_CORRESPONDENCE_CERTIFICATE`
   and its distinct `S3_ENERGY_CLASSIFICATION_CERTIFICATE` consumer have
   separate domains, codomains, relations, stops, and routed T-1A through
   T13B tests. Both remain TYPE-U.
4. **How identification would follow.** Prove common-origin reference-fixed
   HJ/closure functional identity over the full nonempty domain; validate it
   with P13; add P9's full-gate time correspondence; derive its structural
   signature; then apply P12's complete pre-target applicability-or-
   inapplicability maps. Exactly one checked full functional identity names a
   candidate. No winner is named here.
5. **Falsification.** F1-F13 can return evidence against a routed input, the
   core claim, uniqueness, derivation without selection, or named-pair
   exhaustiveness. F10A leaves the higher claim at `NO_VERDICT`; F10B is a
   classification-input failure, not a physical refutation. Today both claims are `NO_VERDICT`,
   not affirmative: the required inputs are unbuilt. A future complete
   zero-match result refutes named-pair exhaustiveness and requires a
   constituted Q-80 record rather than being forced into the current pair.

```text
authority_head_checked_before_authoring = Q-83
authority_head_checked_before_seal = Q-86
road_step_advanced = STEP_2_HAMILTON_JACOBI_SCALE_BRIDGE
S3_correspondence_check_completed = true
S3_surface_token_collision_found = true
S3_interface_audit_completed = true
S3_role_contract_specified = true
S3_test_verdict_wiring_audited = true

Q80_new_class_named_by_this_artifact =
  NONE [PROCESS_CLASSIFICATION; NON-Q54_RESULT]

BRIDGE_SELECTOR_S3_HJ_CLOSURE_ENERGY_CORRESPONDENCE_CERTIFICATE_derived =
  false | TYPE-U |
  would-build: Section 4 core construction witness and proof terms

S3_ENERGY_CLASSIFICATION_CERTIFICATE_derived =
  false | TYPE-U |
  would-build: Section 4 classification witness after the core exists

S3_Tminus1A_through_T13B_suite_executed = false | TYPE-U |
  would-execute: Section 6 concrete inputs, fixtures, and independent oracles

physical_verdict = NO_VERDICT |
  reason: actual S1/S2/S4 objects and P8-P13 are unbuilt

construction_status = SPECIFICATION_ONLY [PROCESS_ATTESTATION; NON-Q54_RESULT]
namespace_register_status = UNCHANGED [PROCESS_ATTESTATION; NON-Q54_RESULT]
protected_holdout_access_status =
  PROHIBITED_AND_NOT_PERFORMED [PROCESS_FENCE_ATTESTATION; NON-Q54_RESULT]

terminal_fence_declarations_below = Q54_EXEMPT
alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_Thomson_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
coupling_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
radius_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
scale_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
root_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
eigenvalue_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
beta_function_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
E_R_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
T_R_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
k_R_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
absolute_interval_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
measured_constant_comparison_performed = false
  [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```
