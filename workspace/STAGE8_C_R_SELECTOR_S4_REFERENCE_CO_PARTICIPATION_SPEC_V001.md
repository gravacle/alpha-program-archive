# Stage 8 C_R Selector S4 Reference Co-Participation Specification V001

Date: 2026-07-31
Lane: CODEX 2
Authority: relay 177; register head at issue Q-80; pre-seal register head Q-81
Status: Q-52 TEST SPECIFICATION ONLY

## 0. Leads, declarations, and protected boundary

### 0.1 Lead findings

Three classifications control this artifact.

First, the specified S4 role supplies a necessary non-choosing route through
the energy-identification fork, but S4 cannot close that fork alone. The route
is:

```text
S1 boundary/time-flow data
  + S2 Hamilton-Jacobi conjugate/constancy certificate
  + S4 reference co-participation certificate
  -> S3 equality-to-closure-energy certificate
```

This is a route declaration, not a derivation, selection, or evaluation.
Section 5 states its stop condition and tests.

Second, the inherited string

```text
S1 -> S2 -> S4 -> S3 -> S5 -> S6
```

survives as one permissible work schedule, but it is TYPE-R refuted as a
literal chain of consuming edges. The sealed prerequisite graph is:

```text
S1 -> {S2, S4} -> S3 -> S5 [SEALED INFERENCE] -> S6
```

The evidence and executed graph-typing test are in Section 2. S2 and S4 are
sibling consumers of S1. S4 was the correct next pre-authoring specification
target because S1 and S2 already had Q-52 specifications; this artifact now
supplies S4's test specification.

Third, Q-80 fires on the sealed debt roster. The four named bins contain 63
entries, and the sealed total adds one separately named live entry. That entry
fits a new bookkeeping class defined and tested in Section 7:

```text
NEW_CLASS = UNBINNED_LIVE_ROSTER_DEBT
member = primitive_source_scalarization_derived
```

It is not silently forced into the response bin. The selector bin directly
contains 10 debts, not the 64-debt mass. Exact transitive unblock rank remains
NO_VERDICT because the direction-bearing graph is incomplete.

### 0.2 Authority currency and Q-80 discipline

The pre-seal register check found that Q-81 had landed at
`QUESTIONS_SETTLED_REGISTER_V001.md:3366-3406`. Q-81 is producer-algebra
territory assigned to Codex 1. Its settled row says that a pure extension
classification was TYPE-R refuted, a new class was required, and Q-78's
producer dominance survived only in reduced form. The underlying producer
artifact was excluded and not opened here. The effects enumerated in the Q-81
row are producer-class retyping and reduced producer dominance. This artifact
continues to source S4 typing and the roster/feed/count determinations from the
separate Q-52/Q-69/Q-75/Q-78/Q-79 authorities cited below.

The cited row says verbatim:

> `IT IS NOT AN EXTENSION AT ALL.`
>
> `The dominance claim survives in reduced form.`

```text
Q81_effect_on_this_artifact =
  METHODOLOGICAL_CONFIRMATION_NO_S4_LOCAL_CHANGE
  [AUTHORITY-CURRENCY-ATTESTATION; NON-Q54_RESULT]
```

`QUESTIONS_SETTLED_REGISTER_V001.md:3331-3357` rules:

> `NAME A NEW CLASS. DO NOT FORCE, DO NOT REPORT AS A DEFECT, DO NOT DISPOSE OF IT WITH NO_VERDICT.`

and distinguishes:

> `NO_VERDICT means information is missing; a NEW CLASS means the categories are wrong.`

It also requires:

> `A new class must be DEFINED, must say what it EXCLUDES, and must be FALSIFIABLE in the Q-54 sense`

Every new class below therefore has a definition, exclusions, and a
failure-capable membership test. No class is used to escape a verdict.

### 0.3 Q-52 and Q-54 status

`QUESTIONS_SETTLED_REGISTER_V001.md:2195-2212` permits:

> `a lane may write a specification if it is declared, marked derived = false, and never reported as derived`

and says:

> `a check that cannot return evidence against what it checks is not a test`

`QUESTIONS_SETTLED_REGISTER_V001.md:2267-2285` defines:

> `TYPE-R refuted`
>
> `TYPE-U unbuilt`
>
> `TYPE-S scope-empty (must carry roots, exclusions, fences in force, query)`
>
> `TYPE-C constraint-blocked`

and makes `NO_VERDICT` legal when required information is absent.

This artifact therefore declares:

```text
artifact_type = Q52_S4_ROLE_SPECIFICATION_AND_TEST_DESIGN
BRIDGE_SELECTOR_S4_REFERENCE_CO_PARTICIPATION_CERTIFICATE_specified_for_test = true

BRIDGE_SELECTOR_S4_REFERENCE_CO_PARTICIPATION_CERTIFICATE_derived = false | TYPE-U |
  would-build: from one independently completed S1 package, derive a
  target-independent reference prescription, complete sector
  co-participation/exclusion proof, and same-support certificate; then supply
  a construction witness and execute the separately routed tests in Section 6

S4_tests_executed = false | TYPE-U |
  would-execute: after a concrete independently derived S1 package, a concrete
  S4 candidate, fixed admissible classes, and independent failure oracles exist

physical_verdict = NO_VERDICT |
  reason: S1, S2, S3, and the four S4 domain auxiliaries are TYPE-U; no S4
  construction or failure-capable physical test has executed
```

### 0.4 F-GK3 premises declared at the outset

P0. Q-52 authorizes this specification for testing. Specification is not
derivation.

P1. The S1 package remains TYPE-U. Its own artifact says at
`STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md:317-327`:

> `The first load-bearing object is now specified as a test object, not derived.`

and records:

> `BRIDGE_S1_COMPLETE_LORENTZIAN_CTP_ACTION_BOUNDARY_TIME_FLOW_DATA_derived = false | TYPE-U`

P2. The S2 certificate remains TYPE-U. Its artifact says at
`STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md:282-292`:

> `The second load-bearing object is now specified as a test object, not derived.`

and records:

> `BRIDGE_S2_CONSTANT_HAMILTON_JACOBI_RECORD_ENERGY_CERTIFICATE_derived = false | TYPE-U`

P3. The primary bridge gate at
`BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:155-167` states:

> `The record phase is insensitive to adding the same constant Hamiltonian to both CTP branches, while total gravitational compactness is not generally insensitive to adding physical spectator energy.`

and:

> `requires a derived state, reference subtraction, and no-spectator theorem. It cannot be supplied by a convention chosen after the record phase is known.`

P4. A governing domain principle already declares a slot called a fixed
reference subtraction. At
`primitive_causal_record_cell_domain_principle_v004.md:19-23` it says:

> `The gravitational action on the actual global time slab uses the sign-matched non-null Dirichlet completion: Einstein-Hilbert bulk term, GHY terms on the initial/final and asymptotic-regulator boundaries, their joint terms, and a fixed reference subtraction.`

This declaration is not carried forward as the S4 theorem. The primary bridge
gate separately owes derivation of the baseline/reference subtraction at
`BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:169-182`:

> `derives the baseline/reference subtraction and excludes spectator energy`

P5. Q-69 at register `:2861-2867` says:

> `THE FLAG AND ITS DISCHARGE OBJECT ARE NOT THE SAME NODE`
>
> `NEVER IDENTIFY A FLAG WITH THE OBJECT THAT DISCHARGES IT`

The flag `reference_subtraction_and_no_spectator_theorem_derived`, the S4
certificate specified here, the S1 reference slot, and any energy candidate
remain distinct.

P6. The current named energy candidates are not adopted as premises. The
bridge gate at `:67-79` says:

> `These are both standard, geometrically meaningful energies, but they are conjugate to different boundary/time choices.`

and:

> `neither finite-boundary Brown-York energy nor asymptotic ADM/Misner-Sharp energy is automatically the Hamiltonian conjugate to the local tip-to-tip proper interval.`

P7. Q-75 at register `:3114-3116` establishes only the cross-chain connection:

> `THE CHAINS CONNECT THROUGH THE T_R -> k_R MISSING BRIDGE AND THE PROSE EDGE WHERE k_R APPEARS IN THE EQUATION FIXING K_*.`

No independence between selector and response work is assumed.

P8. The floor-unit convention is an input not resolved here. No premise or
test in this artifact selects it.

P9. `S4_admissible_stationary_class_derived = false | TYPE-U`.
Would-build: derive from the completed S1 stationary problem the full class on
which reference and sector statements must hold.

P10. `S4_complete_sector_and_support_inventory_derived = false | TYPE-U`.
Would-build: enumerate every admitted record, source, vacuum, binding,
boundary, edge, environment, and other physical contribution, with its
action-difference and closure-support roles.

P11. `S4_complete_admissible_reference_inventory_and_equivalence_relation_derived
= false | TYPE-U`. Would-build: from the reference-free S1
variational/boundary core, enumerate every admissible target-independent
reference completion, prove the inventory exhaustive, and derive its
equivalence relation without choosing one by a downstream result.

P12. `S4_complete_admissible_shift_and_physical_extension_inventory_derived =
false | TYPE-U`. Would-build: derive a nonempty exhaustive transformation and
physical-extension inventory, including the primary gate's nontrivial
branch-common additive family, on which invariance, non-erasure, and spectator
tests are meaningful.

No premise beyond P0-P12 is adopted.

### 0.5 Absolute fences

This artifact does not construct the complete action, derive the S4 theorem,
execute a test, choose either named energy candidate, close the energy fork,
derive an interval, or evaluate an expression. It does not enter, list, or
infer any masked holdout content.

## 1. Bounded scope, correspondence check, and namespace collision

### 1.1 Roots, exclusions, and search method

Roots:

```text
R1 = /Users/bgm/Documents/New project/gravity_emergence_evidence_program
R2 = /Users/bgm/MB Work/alpha-program-archive/workspace
R3 = /Users/bgm/MB Work/alpha_supervision
```

Exclusions:

```text
a32_holdout/custodian_private/ [pruned; not entered or listed]
.git objects
relay-176 producer-algebra extension and crossed-product work
the Q-81 rank-1 producer artifact; only its settled register row was read
relay-175 boundary re-typing and floor-unit convention work
binaries, attachments, and measured-data payloads
for exact type/dependency adjudication, every file outside the controlling
  packet enumerated below
```

All identifier searches were word/identifier-boundaried. Path lists were
NUL-delimited before newline rendering; no whitespace-splitting `xargs`
pipeline was used.

Controlling packet:

```text
BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md
STAGE8_BRIDGE_ITEM1_SIX_OBJECT_TRIAGE_V001.md
STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md
STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md
STAGE8_BRIDGE_ITEM4_SIX_OBJECT_DEPTH_REPORT_V001.md
STAGE8_C_R_SELECTOR_NONSELECTION_DIAGNOSIS_V001.md
STAGE8_GRAVITY_EVIDENCE_ADMISSION_AND_FIVE_STRATA_BINDING_V001.md
primitive_causal_record_cell_domain_principle_v004.md
alpha_complete_dimension_convention_ledger_v004.md
STAGE8_CLOTHING_DISCHARGE_CONDITIONS_AND_LEDGER_FLOOR_EINSTEIN_V001.md
QUESTIONS_SETTLED_REGISTER_V001.md
STAGE8_NAMESPACE_REGISTER_DRAFT_V004.md
```

### 1.2 Dedicated-spec correspondence result

The pre-authoring correspondence check used two independent query families and
intersected their path sets without whitespace splitting.

```text
semantic family A:
  reference_subtraction_and_no_spectator
  reference[- ]subtraction near spectator/no-spectator
  no-spectator near reference subtraction
  same support / same physical support

spec-shape family B:
  Q-52
  TEST SPECIFICATION
  specified_for_test
  failure-capable
  heading-level Domain or Codomain
```

The current draft was excluded from the pre-existing-object question. Every
candidate in the intersection was inspected for an independently declared
domain, codomain, relation, derived-false status, and failure-capable test of
the selector-ladder S4 role.

```text
preexisting_dedicated_S4_Q52_spec_found = false | TYPE-S |
  roots: R1, R2, R3 |
  excl: Section 1.1; this artifact itself; post-authoring mirrors |
  fences: word/identifier boundaries; the two path sets were intersected
  before semantic inspection; mirrors remain listed as mirrors; a flag,
  requirement, relay assignment, or neighboring S1/S2 spec does not count as
  the dedicated S4 discharge object under Q-69 |
  query: semantic family A INTERSECT spec-shape family B above |
  candidate_files_inspected:
    R1/alpha_fundamental_record_action_cleanroom_v003/
      STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md
    R1/alpha_fundamental_record_action_cleanroom_v003/
      STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md
    R1/alpha_fundamental_record_action_cleanroom_v003/
      STAGE8_C_R_FALSIFIER_DESIGN_AND_FLOOR_SOURCE_VALUE_RECONCILIATION_V001.md
    R1/alpha_fundamental_record_action_cleanroom_v003/
      STAGE8_C_R_SELECTOR_NONSELECTION_DIAGNOSIS_V001.md
    R1/primitive_causal_record_cell_domain_principle_v004.md
    R2/STAGE8_ALPHA_DEPENDENCY_CLOSURE_CENSUS_EINSTEIN_V001.md
    R2/STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md
    R2/STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md
    R2/STAGE8_CLOTHING_DISCHARGE_CONDITIONS_AND_LEDGER_FLOOR_EINSTEIN_V001.md
    R2/STAGE8_C_R_FALSIFIER_DESIGN_AND_FLOOR_SOURCE_VALUE_RECONCILIATION_V001.md
    R2/STAGE8_C_R_SELECTOR_NONSELECTION_DIAGNOSIS_V001.md
    R3/QUESTIONS_SETTLED_REGISTER_V001.md
    R3/RELAY_PASTE_167_BRIDGE_CRITICAL_PATH_2026-07-30.md
    R3/RELAY_PASTE_177_CR_SELECTOR_CHAIN_2026-07-31.md
  qualifying_evidence_file_list: EMPTY
```

This does not say the S4 concept is absent. The primary gate, triage, depth
report, and neighboring specs state partial obligations. The scoped finding is
only that no pre-existing dedicated Q-52 S4 test object survived the semantic
correspondence test.

### 1.3 Partial constituents already present

The dimension/convention ledger at
`alpha_complete_dimension_convention_ledger_v004.md:75-106` writes an action
with a reference slot and says:

> `S_ref is the fixed asymptotic reference subtraction and carries no charged response coefficient.`

The domain principle at
`primitive_causal_record_cell_domain_principle_v004.md:31-39` distinguishes the
history-support edge from a material wall and says:

> `The null edge of D is not a reflecting material wall`

and:

> `Those are Step 5 obligations; they are not obtained from the definition of a causal diamond.`

The S4 depth report at
`STAGE8_BRIDGE_ITEM4_SIX_OBJECT_DEPTH_REPORT_V001.md:156-192` names three
separate unbuilt leaves:

> `baseline/reference subtraction rule = false | TYPE-U`
>
> `spectator/vacuum/binding/edge/environment exclusion theorem = false | TYPE-U`
>
> `proof that compactness and record-action energy use the same support = false | TYPE-U`

These are partial inputs and obligations, not a recovered S4 certificate.

### 1.4 Exact `S4` surface-token collision

Word boundaries alone do not disambiguate `S4`.

`STAGE8_GRAVITY_EVIDENCE_ADMISSION_AND_FIVE_STRATA_BINDING_V001.md:75-89`
defines:

> `S4 - BID minimal cell and Hamilton-Jacobi bridge`

and its open condition contains the entire multi-object bridge.

By contrast,
`STAGE8_BRIDGE_ITEM4_SIX_OBJECT_DEPTH_REPORT_V001.md:156-174` defines:

> `S4. Reference-subtraction / no-spectator theorem`

and gives it three leaves.

```text
five_strata_S4_is_selector_ladder_S4 = false | TYPE-R |
  test: S4-SCOPE-SIGNATURE-TEST; compare the two cited definitions, carriers,
  and codomain obligations; the five-strata token denotes the whole BID
  minimal-cell/HJ bridge while the selector-ladder token denotes one sibling
  certificate inside that bridge
```

`STAGE8_NAMESPACE_REGISTER_DRAFT_V004.md:25-30` contains only the two proposed
`Gamma_K` rows.

```text
S4_namespace_register_row_found = false | TYPE-S |
  roots: exact file STAGE8_NAMESPACE_REGISTER_DRAFT_V004.md |
  excl: every other namespace artifact and all concurrent namespace work |
  fences: exact identifier-boundaried S4 query; no register row authored here |
  query: "(^|[^A-Za-z0-9_])S4([^A-Za-z0-9_]|$)" |
  file_list: EMPTY
```

Local author names used below:

```text
S4 [FIVE-STRATA-BID-MINIMAL-CELL-HJ-BRIDGE]
S4 [SELECTOR-LADDER-REFERENCE-CO-PARTICIPATION-CERTIFICATE]
```

These names are local disambiguators, not a namespace adoption. The namespace
register remains unchanged.

## 2. Order verification and re-ranking

### 2.1 What the inherited artifacts print

`STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md:271-280`
states:

> `The dependency order from Item 1 remains unchanged:`
>
> `S1 -> S2 -> S4 -> S3 -> S5 -> S6`

and correctly adds:

> `S2 cannot be attempted as a proof until S1 exists.`

### 2.2 What their explicit edges actually say

`STAGE8_BRIDGE_ITEM1_SIX_OBJECT_TRIAGE_V001.md:329-342` lists:

> `S1 -> S2`
>
> `S2 -> S3`
>
> `S4 -> S3`

and labels:

> `S3 -> S5: inferred`

It supplies no consuming edge from S2 into S4.

The independent depth report at
`STAGE8_BRIDGE_ITEM4_SIX_OBJECT_DEPTH_REPORT_V001.md:120-130` gives S2:

> `S2 constant HJ energy certificate`
>
> `  -> S1 complete Lorentzian CTP action / boundary / time-flow data`

The same report at `:156-166` gives S4:

> `S4 reference-subtraction / no-spectator theorem`
>
> `  -> S1 complete Lorentzian CTP action / boundary / time-flow data`

At `:194-208` it gives S3 two prerequisites:

> `S3 branch-energy equals gravitating closure energy`
>
> `  -> S2 constant HJ energy certificate`
>
> `  -> S4 reference-subtraction / no-spectator theorem`

### 2.3 Executed graph-typing test

Test `SELECTOR-LADDER-ADJACENCY-TEST`:

```text
input:
  inherited displayed arrow string
  Item-1 explicit edge list
  Item-4 per-object prerequisite chains

pass condition for a strict chain:
  every adjacent displayed arrow is an independently supported consumes-edge

failure witness:
  S2 and S4 are both depth-2 consumers of S1; S3 consumes both; no independent
  S2-to-S4 consuming edge occurs in the controlling packet
```

Result:

```text
strict_linear_dependency_chain_holds = false | TYPE-R |
  test: SELECTOR-LADDER-ADJACENCY-TEST above; the independent depth manifest
  refutes the S2-to-S4 adjacent-arrow reading

inherited_linear_order_is_valid_work_schedule = true
```

Bounded supporting negative:

```text
independent_S2_to_S4_prerequisite_evidence_found = false | TYPE-S |
  roots: the five bridge artifacts and Q-67 register row in the controlling
  packet of Section 1.1 |
  excl: unrelated S1-S6 taxonomies, Section 1.1 exclusions, and the inherited
  arrow string itself as independent support |
  fences: word-boundaried S1-S6 plus expanded object names; only direction-
  bearing prerequisite statements count |
  query: exact "S2 -> S4", Unicode-arrow equivalent, and expanded-object
  consumes/requires/blocked-by clauses |
  candidate_files_inspected:
    STAGE8_BRIDGE_ITEM1_SIX_OBJECT_TRIAGE_V001.md
    STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md
    STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md
    STAGE8_BRIDGE_ITEM4_SIX_OBJECT_DEPTH_REPORT_V001.md
    QUESTIONS_SETTLED_REGISTER_V001.md
  qualifying_evidence_file_list: EMPTY
```

The imported terms **directed acyclic graph**, **fork-join**, and **topological
linearization** come from mathematics/software dependency analysis. They apply
here because the corpus itself labels directed `Edges` and `Dependency chain`
records and asks which object must exist before another.

Correct dependency order:

```text
S1 -> {S2, S4} -> S3 -> S5 [SEALED INFERENCE] -> S6
```

One valid schedule remains:

```text
S1 -> S2 -> S4 -> S3 -> S5 -> S6
```

S2 and S4 may exchange schedule order after S1. S4 was nevertheless the next
pre-authoring unspecified object because S1 and S2 already had Q-52
specifications. This artifact supplies the S4 specification; it does not
derive S4.

### 2.4 S1/S2 hostile interface findings

The main status discipline survives. S1 prevents an S1 pass from silently
flipping S2-S6 at
`STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md:297-315`:

> `check that no S1 pass is treated as a pass for S2-S6.`

S2 refuses execution without S1 at
`STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md:76-92`:

> `If S1 is absent, the S2 constancy test must return: NO_VERDICT | prerequisite S1 package absent | TYPE-U`

Two interface hazards remain and are reported, not repaired.

**Hazard A — S1 reference slot versus S4 derived reference.** S1 at
`STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md:138-153`
requires boundary terms and says a boundary/reference term cannot be left to
later target-aware choice. Its T4 at `:283-295` accepts a boundary/reference
slot that is either fixed or explicitly missing. The primary gate at
`BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:169-181` separately requires
the action to:

> `fixes the global/subregion boundary terms and time-flow vector`

and later:

> `derives the baseline/reference subtraction`

No sealed correspondence in the exact S1/S4 packet equates the two reference
roles.

```text
S1_boundary_reference_slot_equals_S4_derived_energy_baseline = NO_VERDICT |
  reason: the object-level correspondence is missing; Q-69 forbids merging
  them by shared word

explicit_S1_reference_to_S4_reference_correspondence_found = false | TYPE-S |
  roots: primary bridge gate, S1 spec, S2 spec, S4 triage/depth packet |
  excl: Section 1.1; shared token "reference" without a direction-bearing map |
  fences: no object/flag merge; fixed declaration is not a derivation |
  query: boundary/reference term, reference slots, baseline/reference
  subtraction, derives, consumes, supplies, maps-to |
  candidate_files_inspected:
    BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md
    STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md
    STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md
    STAGE8_BRIDGE_ITEM4_SIX_OBJECT_DEPTH_REPORT_V001.md
  qualifying_evidence_file_list: EMPTY
```

This S4 specification therefore requires a provenance-bearing S1 reference
slot or an explicitly open slot. It does not consume a preselected reference
as proof.

**Hazard B — S2 advertised domain.** S2 at
`STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md:69-74` advertises:

> `constant on the first durable-record saddle`

S1 at
`STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md:183-195`
supplies only:

> `the class of stationary solutions/saddles it admits`

and S2's T3 at `STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md:247-259`
tests:

> `the S1 stationary record-cell solution class.`

```text
S1_first_durable_record_saddle_designation_found = false | TYPE-S |
  roots: primary bridge gate, exact S1 spec, exact S2 spec |
  excl: Section 1.1; generic stationary classes without a first-durable
  designation |
  fences: domain designation is not inferred from the S2 target label |
  query: first durable, durable-record, stationary solution class |
  candidate_files_inspected:
    BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md
    STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md
    STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md
  qualifying_evidence_file_list: EMPTY

S2_test_sufficiency_for_advertised_first_durable_domain = NO_VERDICT |
  reason: the S1-to-first-durable domain-selection interface is unbuilt
```

S2 also calls S4 downstream at `:192-204`, while the executed graph test above
places S4 as a sibling prerequisite.

```text
S4_is_dependency_downstream_of_S2 = false | TYPE-R |
  test: SELECTOR-LADDER-ADJACENCY-TEST; the explicit depth manifest gives both
  S2 and S4 as direct S1 consumers and joins them only at S3
```

The S2 isolation guard remains safe because preventing an S2 pass from flipping
S4 is still required. Only the dependency label is refuted.

## 3. Q-52 object type for S4

### 3.1 Why the existing single-theorem label is too narrow

The primary gate's obstruction at
`BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:155-167` simultaneously
requires a derived state, reference subtraction, and a no-spectator theorem.
The depth report at
`STAGE8_BRIDGE_ITEM4_SIX_OBJECT_DEPTH_REPORT_V001.md:168-174` separates a
reference rule, an exclusion theorem, and a same-support proof.

The S4 object therefore needs a composite proof-certificate type:

```text
Q52_OBJECT_TYPE = REFERENCE_CO_PARTICIPATION_CERTIFICATE
```

This does **not** require a Q-80 new category. A composite proof certificate is
an ordinary specification type: its three legs are distinct but can be jointly
carried and separately tested. Q-80 would fire only if a concrete future
object resisted that type rather than merely carrying several proof duties.
The phrase **composite proof certificate** is imported from ordinary formal
specification/proof-engineering practice. It applies here because sealed text
already separates three proof duties and the contract below gives each a
failure-capable leg; it does not add a physical premise.

Definition:

```text
A composite interface certificate that:
  (1) derives a target-independent reference prescription from the supplied
      complete action/boundary/time-flow package;
  (2) partitions every admitted physical contribution into closure-retained
      or derivably closure-excluded sectors, proves that each retained sector
      participates in the record action difference, and proves that each
      excluded sector does not contribute to closure; and
  (3) proves that closure energy and record-action energy use the same physical
      support on the declared class.
```

Exclusions:

```text
not a conventional choice of zero
not a fixed reference slot without derivation provenance
not a blanket assertion that all spectator energy vanishes
not a selector that names Misner-Sharp or Brown-York
not S3's later equality-to-gravitating-closure-energy certificate
not the derived flag that the certificate would discharge
```

Failure-capable type-conformance test:

```text
REFERENCE-CO-PARTICIPATION-TYPE-CONFORMANCE-TEST

exact target verdict: S4_object_type_conforms
non-targets: physical validity, derivation, S3, and energy-fork closure

fail conformance if:
  any mandatory Cert_S4 output slot is absent;
  OR the mandatory slots cannot route evidence to separately named verdicts;
  OR the declared codomain contains S2, S3, S5, S6, interval-selection, or
  named-energy-selection output;
  OR the object identifies itself with S3 or with its derived flag rather than
  remaining a distinct certificate node.
```

Substantive failures are deliberately outside this type test: reference
provenance/forcedness routes to T1A/T1B, common-shift and non-erasure to
T2A/T2B, closure-only witnesses to T4, and downstream choice or silent flag
movement to T6.

This type is not asserted physically realized. It is the testable contract of
the missing S4 object. The object remains TYPE-U.

## 4. Q-52 specification of S4

### 4.1 Object name and epistemic type

To avoid the collision in Section 1.4, the full author name is:

```text
BRIDGE_SELECTOR_S4_REFERENCE_CO_PARTICIPATION_CERTIFICATE
```

```text
BRIDGE_SELECTOR_S4_REFERENCE_CO_PARTICIPATION_CERTIFICATE_specified_for_test = true
BRIDGE_SELECTOR_S4_REFERENCE_CO_PARTICIPATION_CERTIFICATE_derived = false | TYPE-U |
  would-build: construct the certificate from an independently completed S1
  package and separately derived admissible-sector/support and reference-
  equivalence inputs, then prove each codomain property
```

### 4.2 Domain

Declared domain:

```text
Dom(S4_SPEC) =
  (
    S1_complete_package,
    S4_admissible_stationary_class,
    S4_complete_sector_and_support_inventory,
    S4_complete_admissible_reference_inventory_and_equivalence_relation,
    S4_complete_admissible_shift_and_physical_extension_inventory
  )
```

The S1 package type is already specified at
`STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md:64-89`
as a finite package containing the cell domain, field content, CTP branch data,
action/boundary terms, state/preparation, time flow, stationary problem, and
provenance. That artifact says:

> `It does not output a value, an interval, a response, or any stiffness.`

The remaining four domain components are the P9-P12 test prerequisites
declared at the outset, not constructions made here:

```text
S4_admissible_stationary_class_derived = false | TYPE-U |
  would-build: derive from the completed S1 stationary problem the full class
  on which reference and sector statements must hold

S4_complete_sector_and_support_inventory_derived = false | TYPE-U |
  would-build: enumerate every record, source, vacuum, binding, boundary,
  edge, environment, and other physical contribution admitted by S1, with its
  action-difference and closure support roles

S4_complete_admissible_reference_inventory_and_equivalence_relation_derived =
  false | TYPE-U |
  would-build: from the reference-free S1 variational/boundary core enumerate
  every admissible target-independent reference completion, prove inventory
  exhaustiveness, and derive the equivalence relation without selecting one by
  a downstream result

S4_complete_admissible_shift_and_physical_extension_inventory_derived =
  false | TYPE-U |
  would-build: derive a nonempty exhaustive transformation/extension
  inventory, including the primary gate's nontrivial branch-common additive
  family, on which invariance, non-erasure, and spectator tests are meaningful
```

Specification stops before these prerequisites. It does not construct S1 or
any one of them.

### 4.3 Codomain

For complete domain inputs, the declared codomain is:

```text
Cod(S4_SPEC) = Cert_S4 union Failure_S4

Cert_S4 =
  (
    forced_reference_prescription,
    common_shift_invariance_certificate,
    physical_energy_non_erasure_certificate,
    sector_co_participation_or_exclusion_certificate,
    same_support_certificate,
    target_independence_certificate,
    downstream_isolation_certificate,
    provenance_and_fences
  )
```

`Failure_S4` contains separately routed counterexamples to one of these
properties. Missing or inapplicable prerequisites are not complete members of
`Dom(S4_SPEC)`. A separate partial-input evaluation protocol records that
fact:

```text
Eval_S4(partial_input) = NO_VERDICT |
  reason: name the absent or inapplicable domain prerequisite
```

The codomain expressly excludes S2 constancy, S3 equality, S5 marginality, S6
interval selection, an energy-candidate choice, and every numerical value.

### 4.4 Required relations

For every admissible physical contribution `j` in the supplied S1 inventory,
the candidate must prove an exhaustive, exclusive partition:

```text
exactly_one(
  retained_in_gravitating_closure(j),
  excluded_from_gravitating_closure(j)
)

retained_in_gravitating_closure(j)
  iff contributes_to_gravitating_closure(j)

retained_in_gravitating_closure(j)
  implies participates_in_record_action_difference(j)

derived_exclusion_from_gravitating_closure(j)
  implies
    excluded_from_gravitating_closure(j)
    AND NOT contributes_to_gravitating_closure(j)

excluded_from_gravitating_closure(j)
  requires derived_exclusion_from_gravitating_closure(j)
```

This is a predicate specification, not an evaluated energy relation.

It must also prove:

```text
purely representational branch-common additive offsets remain null for the
  CTP record difference;
the reference prescription does not erase a physical contribution retained
  in gravitating closure;
closure and record-action supports coincide after derived exclusions;
the reference prescription is forced before downstream targets are inspected;
equivalent allowed representations of the same S1 package give equivalent
  S4 certificates.
```

These relations encode the primary gate's statements at `:155-167` that a
common branch shift leaves the record phase insensitive while a physical
spectator may affect compactness, and that a convention chosen after the phase
is known cannot supply the bridge.

### 4.5 Construction witness and stop

```text
S4_CONSTRUCTION_WITNESS_derived = false | TYPE-U |
  would-build: a target-independent construction from the exact S1 provenance,
  four independently derived domain auxiliaries, and proof terms for every
  Cert_S4 component
```

This artifact stops at `S4_CONSTRUCTION_WITNESS`. It does not choose a
reference functional, prove a sector theorem, or instantiate a closure energy.

## 5. Bearing on the energy-identification fork

### 5.1 What sealed text says

`BID_MINIMAL_PUBLIC_CAUSAL_CELL_DERIVATION_V001.md:38-47` says:

> `On the maximal spherical section, the Misner-Sharp compactness must obey`

The bridge gate at
`BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:58-79` separately describes
a reference-subtracted Brown-York energy and then says the two candidates are
conjugate to different boundary/time choices and neither is automatically the
required conjugate energy.

S1 supplies the boundary/time-flow type; S2 supplies the symbolic conjugate and
constancy type; S4 supplies the forced reference and co-participation type; S3
is the separately owed equality-to-closure-energy certificate. The explicit
edge manifest in Section 2 supports this fork-join route.

### 5.2 Route verdict

S4 therefore offers a route by which the identification can be derived rather
than chosen, but only at the S3 join.

```text
nonchoosing_energy_identification_route_specified_for_test = true

nonchoosing_energy_identification_route_executed = false | TYPE-U |
  would-execute: independently complete S1, S2, and S4, construct S3, and run
  the joint correspondence test without a post-target candidate choice

S4_alone_sufficient_for_fork_closure = false | TYPE-R |
  test: FORK-REQUIREMENT-CODOMAIN-TEST; compare S4's declared codomain with the
  primary gate's independently required boundary/time-flow, HJ constancy, and
  equality outputs; S4 lacks S2 and S3 outputs by construction

energy_identification_fork_closed = false | TYPE-U |
  would-build: independently complete S1, S2, and S4, then construct and pass
  the S3 equality/correspondence certificate without candidate-specific choice
```

The route can also return evidence against compatibility. It is not required
to force either named candidate. If a future derived S3 object fits neither
candidate, Q-80 requires a new class at that time; today that outcome is
NO_VERDICT because the object is missing, not because the candidate categories
have already failed.

### 5.3 No fork choice

```text
energy_candidate_choice_status =
  PROHIBITED_AND_NOT_PERFORMED
  [PROCESS_FENCE_ATTESTATION; NON-Q54_RESULT]

future_physical_energy_identification_derived = false | TYPE-U |
  would-build: complete the non-choosing S1-plus-S2-plus-S4-to-S3 route and
  derive a functional correspondence before comparing its output class with
  either named candidate
```

The process attestation is not a physical refutation of either candidate.

## 6. Failure-capable tests and verdict wiring

### 6.1 Wiring rule

Each test reports only to the property it actually tests. A missing prerequisite
returns NO_VERDICT and cannot refute S4. A property failure cannot be routed to
generic existence, another property, S3, marginality, interval selection, or
the energy-fork verdict. No pass sets `derived = true`.

### 6.2 Test table

| Test | Input and failure-capable method | Exact target verdict | Non-targets |
|---|---|---|---|
| T-1 — object-type conformance | Execute only the structural Section 3 type-conformance checks against a concrete candidate: mandatory output slots, separate verdict routes, codomain exclusions, and node identity. | `S4_object_type_conforms` | No reference provenance/forcedness, physical-validity, derivation, S3, or fork verdict |
| T0 — domain applicability | Require one concrete independently derived S1 and all four P9-P12 auxiliaries. An absent or inapplicable prerequisite returns NO_VERDICT from `Eval_S4`; a supplied object of the wrong declared type fails domain applicability. | `S4_domain_applicability` | No S4 property or derivation flag |
| T1A — reference-inventory provenance/completeness | Require P11 to be nonempty, pre-target, and exhaustive over every admissible reference completion of the same reference-free S1 core, with a derived equivalence relation. If P11 is absent, return NO_VERDICT; if supplied empty, unsupported, downstream-selected, or incomplete, fail inventory validity. | `S4_reference_inventory_valid_and_complete` | No forcedness, spectator, support, S3, or fork verdict |
| T1B — reference forcing | After T1A PASS, hold the reference-free S1 core fixed and compare the proposed prescription—whether S1 originally presented its slot as open or fixed—against every P11-admissible completion and equivalence class. Any inequivalent survivor refutes forcedness. Provenance or equivalent-representation invariance alone cannot pass this test. | `S4_reference_prescription_forced` | No inventory-completeness or downstream-interface verdict |
| T2P — shift/extension-inventory validity | Require P12 to have pre-target provenance, be nonempty, contain the primary gate's nontrivial branch-common additive family, and carry an exhaustiveness witness for admissible physical extensions relative to P10. If P12 is absent, return NO_VERDICT; if supplied empty, unsupported, or incomplete, fail inventory validity. | `S4_shift_extension_inventory_valid_and_complete` | No common-shift invariance or physical-energy non-erasure verdict |
| T2A — common-shift invariance | After T2P PASS, apply every P12-admissible purely representational common branch shift. One changed record-action difference refutes invariance. | `S4_common_shift_invariance_valid` | No inventory-validity or physical-energy non-erasure verdict |
| T2B — retained-energy non-erasure | After T2P PASS, apply every P12-admissible physical-sector extension retained in gravitating closure. One retained contribution erased by the reference prescription refutes non-erasure; a separately proved closure exclusion is outside this failure class. | `S4_retained_physical_energy_non_erasure_valid` | No inventory-validity, common-shift, or generic-existence verdict |
| T3 — sector completeness | Compare the candidate inventory with every S1 field, boundary, edge, environment, state, and source sector. One omitted admitted sector refutes completeness. | `S4_sector_inventory_complete` | No no-spectator physical verdict |
| T4 — no closure-only spectator | Seek a contribution retained in gravitating closure that does not participate in the record action difference. An exclusion token defeats the witness only if it independently proves both exclusion and non-contribution to closure. One surviving witness refutes this leg. | `S4_no_closure_only_spectator_energy` | No reference or S3 equality verdict |
| T5 — same support | Compare closure and record-action supports term by term after independently proved exclusions. One unmatched retained support contribution refutes correspondence. | `S4_same_support_correspondence` | No named-energy selection |
| T6 — target blindness and isolation | Trace every reference/exclusion input to pre-target S1 provenance and check that an S4 pass flips no S2, S3, S5, S6, interval, or fork flag. Any downstream-selected input or silent flip fails. | Split: `S4_target_independence`; `S4_downstream_isolation` | Each leg is isolated from the other |
| T7 — joint fork interface | Given independently completed S1, S2, S4, and a candidate S3 interface, test whether their boundary/time-flow and functional correspondence yields a unique identification without post-target choice. Accepting incompatible candidates or requiring an extra reference choice refutes interface sufficiency. | `JOINT_S1_S2_S4_S3_ENERGY_IDENTIFICATION_INTERFACE_SUFFICIENT` | Not an S4 property verdict and not `fork_closed` |
| T8 — complete S4 candidate | Require T-1, T0, T1A, T1B, T2P, T2A, T2B, T3, T4, T5, and both T6 legs to be applicable and PASS over the full declared S1 class. Any failed leg routes its witness to that leg and fails the composite; any required NO_VERDICT makes the composite NO_VERDICT. | `S4_candidate_valid_on_declared_S1_class` | Never `S4_derived`; never the T7 interface verdict |

### 6.3 Unexecuted-test status

```text
S4_Tminus1_T0_T1A_T1B_T2P_T2A_T2B_T3_through_T8_executed = false | TYPE-U |
  would-execute: supply the exact concrete inputs and independent failure
  oracles listed in Section 6.2, then run each separately routed leg

JOINT_S1_S2_S4_S3_ENERGY_IDENTIFICATION_INTERFACE_SUFFICIENT = NO_VERDICT |
  reason: independently completed S1, S2, S4, and candidate S3 interface do
  not exist
```

### 6.4 Wiring audit

The T8 defect class from the prior package work is excluded here by an explicit
target column. T-1 reports only to object-type conformance. T1A prevents an
empty, incomplete, or self-selected reference inventory from making T1B pass
vacuously; T1B ranges over all P11-admissible completions even when S1 presents
a fixed slot. T2P prevents an empty or incomplete transformation inventory
from making T2A/T2B pass vacuously. T2A and T2B route representational
invariance and physical non-erasure separately. T7 tests a joint external interface and reports only
to its joint-interface verdict. T8 requires every mandatory S4 leg and reports
only to the S4 candidate-property verdict. Neither T7 nor T8 reports into the
other's verdict.

```text
S4_test_verdict_wiring_audited = true
test_can_set_S4_derived_flag = false | TYPE-R |
  test: TEST-CODOMAIN-ROUTER-AUDIT; inspect every target verdict in Section 6.2;
  none has BRIDGE_SELECTOR_S4_REFERENCE_CO_PARTICIPATION_CERTIFICATE_derived
  as codomain
```

## 7. Debt-roster dominance and Q-80 classes

### 7.1 Exact sealed bins

`STAGE8_CLOTHING_DISCHARGE_CONDITIONS_AND_LEDGER_FLOOR_EINSTEIN_V001.md:188-230`
states:

> `RESPONSE CHAIN (Q-51/Q-57), 39:`
>
> `SELECTOR CHAIN (Q-59), 10, STATUS ONLY:`
>
> `WRITE CHAIN, 13:`
>
> `FOURTH-HORN SUCCESSOR, 1:`
>
> `TOTAL 63 + primitive_source_scalarization_derived ... = 64.`

The 64th live entry is counted but not assigned to any of the four named bins.

### 7.2 New class: UNBINNED_LIVE_ROSTER_DEBT

Definition:

```text
A live debt that is explicitly counted in the sealed roster total but is not
listed as a member of any sealed named chain bin.
```

What it resists: the four Q-78 bins classify named roster membership, yet the
sealed total expressly carries this live entry outside their combined 63. It
cannot be forced into a bin without adding an unsealed semantic assignment.

Exclusions:

```text
not a retired identifier
not an off-path identifier
not an UNKNOWN identifier
not an entry explicitly listed in response, selector, write, or fourth-horn
not a semantic reassignment made from name resemblance
```

Failure-capable membership test:

```text
UNBINNED-LIVE-ROSTER-MEMBERSHIP-TEST

membership requires:
  exact inclusion in the sealed live total;
  exact absence from every enumerated named bin;
  explicit live rather than retired/off-path/unknown status.

fail membership if:
  a sealed bin contains the exact identifier;
  OR the identifier is not part of the live total;
  OR it is retired, off-path, or UNKNOWN.
```

Executed result:

```text
primitive_source_scalarization_roster_class = UNBINNED_LIVE_ROSTER_DEBT
UNBINNED_LIVE_ROSTER_MEMBERSHIP_TEST = PASS
```

This is a bookkeeping-class finding, not a physical verdict. It does not amend
the roster or force the entry into another bin.

### 7.3 Selector's direct roster membership

The sealed selector bin at `:213-220` names exactly ten entries, including the
S4 flag. Therefore:

```text
selector_direct_roster_debt_count = 10

selector_is_maximum_under_direct_roster_bin_metric = false | TYPE-R |
  test: SEALED-ROSTER-BIN-COMPARISON; compare the four sealed bin counts;
  response has 39 direct entries and selector has 10
```

The earlier register statement at
`QUESTIONS_SETTLED_REGISTER_V001.md:3258-3262` says the selector clears:

> `the ladder head dominating the ~64-debt mass: maximum debt movement`

The executed roster-bin comparison does not support that claim under direct
bin membership.

### 7.4 Cross-chain input feed, not demonstrated dominator

Q-75 at register `:3114-3116` proves a direction-bearing connection from the
selector output into the response-facing chain. That relation fits a role not
represented by Q-78's four debt bins:

```text
NEW_CLASS = CROSS_CHAIN_INPUT_FEED
```

Definition:

```text
A direction-bearing relation in which an output of one construction chain
supplies an input to a separately named construction chain. Membership makes
no claim about discharge count, domination, or completion of either chain.
```

What it resists: Q-78's four categories classify debt members, not
direction-bearing relations between chains. Forcing this edge into a debt bin
would conflate an edge with a node and manufacture a discharge claim.

Exclusions:

```text
not graph disjointness
not an inference that any receiving-chain debt is discharged
not a graph dominator merely because one outgoing feed exists
not a claim that either chain completes when the input feed exists
```

Failure-capable membership test:

```text
CROSS-CHAIN-INPUT-FEED-MEMBERSHIP-TEST

fail membership if:
  the feed edge is refuted;
  OR the alleged source is not an output of the first named chain;
  OR the alleged destination is not an input to the second named chain;
  OR the chains are shown to be disjoint after all.
```

The Q-75 edge passes this positive relation test. The selector-to-response
relation is therefore classified as a `CROSS_CHAIN_INPUT_FEED`. Whether that
feed discharges any receiving-chain debt is a separate scoped question.

```text
CROSS_CHAIN_INPUT_FEED_MEMBERSHIP_TEST = PASS
```

Bounded negative:

```text
selector_proved_to_discharge_response_write_or_fourth_horn_debts = false | TYPE-S |
  roots: Q-68, Q-75, Q-78, Q-79 register rows; Q-78 roster artifact; five
  selector-bridge artifacts |
  excl: Section 1.1; the proved terminal feed itself; semantic identity inferred
  from shared quantities |
  fences: exact roster identifiers and direction-bearing edges only; feed is
  not treated as discharge |
  query: exact 64 roster identifiers; S1-S6 expanded names; T_R, k_R, K_*;
  discharg*, unblock*, advanc*, feed*, connect*, enter*, appear*, depend*,
  require*, suppl*, blocked*, would-build |
  candidate_files_inspected:
    QUESTIONS_SETTLED_REGISTER_V001.md
    STAGE8_CLOTHING_DISCHARGE_CONDITIONS_AND_LEDGER_FLOOR_EINSTEIN_V001.md
    BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md
    STAGE8_BRIDGE_ITEM1_SIX_OBJECT_TRIAGE_V001.md
    STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md
    STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md
    STAGE8_BRIDGE_ITEM4_SIX_OBJECT_DEPTH_REPORT_V001.md
  qualifying_evidence_file_list: EMPTY
```

The widened query recovered the Q-75 feed/connect statement and Q-78's bin
membership, but no direction-bearing statement that the selector ladder
discharges a response, write, or fourth-horn debt. The TYPE-S result does not
extend beyond the listed packet.

### 7.5 Exact transitive rank

Q-68 at register `:2738-2743` earlier said:

> `By transitive unblock count the package wins`

Q-75 at `:3128-3132` later says:

> `EXACT COUNT IS NO_VERDICT`

and requires an adjudication rule for remaining prose candidates. Q-79 at
`:3311-3327` reports prose-rule recall `0.641` and that it misses its motivating
edge.

The graph-theory term **dominator** is imported. It would require every path to
a target node to pass through the proposed dominator. That standard applies to
the corpus only after the direction-bearing graph and node identities are
complete enough to test all paths. Q-75/Q-79 say they are not.

```text
selector_exact_transitive_unblock_rank = NO_VERDICT |
  reason: the current direction-bearing graph remains incomplete and no complete
  all-path dominator test can run

selector_maximum_debt_movement_claim_status =
  REFUTED_UNDER_DIRECT_BIN_METRIC_AND_NO_VERDICT_UNDER_TRANSITIVE_METRIC
  [PROCESS_CLASSIFICATION; NON-Q54_PHYSICAL_RESULT]
```

## 8. Q-54 negative registry

| Negative | Type | Evidentiary carrier |
|---|---|---|
| Strict inherited arrow string is a literal consuming-edge chain | TYPE-R | SELECTOR-LADDER-ADJACENCY-TEST, Section 2.3 |
| Independent S2-to-S4 prerequisite evidence recovered | TYPE-S | Roots, exclusions, query, and file list in Section 2.3 |
| Five-strata S4 is selector-ladder S4 | TYPE-R | S4-SCOPE-SIGNATURE-TEST, Section 1.4 |
| Namespace V004 contains an S4 row | TYPE-S | Exact file/query in Section 1.4 |
| Pre-existing dedicated S4 Q-52 spec recovered | TYPE-S | R1-R3 candidate and empty qualifying-evidence lists in Section 1.2 |
| Explicit S1-reference to S4-reference correspondence recovered | TYPE-S | Exact packet/query in Section 2.4 |
| S1 first-durable saddle designation recovered | TYPE-S | Exact packet/query and file list in Section 2.4 |
| S4 is dependency-downstream of S2 | TYPE-R | SELECTOR-LADDER-ADJACENCY-TEST, Section 2.4 |
| S4 alone is sufficient to close the energy fork | TYPE-R | FORK-REQUIREMENT-CODOMAIN-TEST, Section 5.2 |
| Future physical energy identification is derived | TYPE-U | Complete the non-choosing functional correspondence, Section 5.3 |
| Non-choosing energy-identification route has executed | TYPE-U | Complete S1/S2/S4/S3 and execute the joint test, Section 5.2 |
| S4 and its domain auxiliaries/construction witness are derived | TYPE-U | Construct each exact object and prove the declared relations, Section 4 |
| S4 property/interface tests have executed | TYPE-U | Supply exact candidates, fixtures, and oracles, Section 6.3 |
| A test can set S4 derived | TYPE-R | TEST-CODOMAIN-ROUTER-AUDIT, Section 6.4 |
| Selector is maximum under direct roster-bin metric | TYPE-R | SEALED-ROSTER-BIN-COMPARISON, Section 7.3 |
| Selector discharges response/write/fourth-horn debts | TYPE-S | Bounded packet/query/file list, Section 7.4 |
| Exact selector transitive-unblock rank is known | NO_VERDICT | Incomplete direction-bearing graph, Section 7.5 |
| S1 boundary/reference slot is the S4 derived baseline | NO_VERDICT | Missing object correspondence and Q-69, Section 2.4 |
| S2 test suffices for its advertised first-durable domain | NO_VERDICT | Missing S1-to-first-durable domain-selection interface, Section 2.4 |
| Energy-identification fork is closed | TYPE-U | Complete S1/S2/S4 then execute S3, Section 5.2 |

No TYPE-S finding escapes its declared scope. The TYPE-R findings refute graph,
identity, router, or direct-bin hypotheses; they do not refute a future S4
construction or either physical energy candidate.

## 9. Five requested answers

1. **Order.** Qualified refutation. The inherited linear string is a valid
   schedule but not the dependency graph. The supported graph is
   `S1 -> {S2,S4} -> S3 -> S5 [sealed inference] -> S6`.
   S4 was the next pre-authoring unspecified object; this artifact now supplies
   its Q-52 test specification without deriving it.
2. **S4 specification.** Sections 3-4 define
   `BRIDGE_SELECTOR_S4_REFERENCE_CO_PARTICIPATION_CERTIFICATE`, its domain,
   codomain, relations, TYPE-U prerequisites, and construction stop. Nothing is
   derived.
3. **Fork.** S4 supplies the necessary reference/co-participation discriminator
   in a non-choosing S1+S2+S4-to-S3 route. S4 alone is TYPE-R refuted as
   sufficient; the fork remains TYPE-U.
4. **Tests.** T-1, T0, split T1A/T1B, T2P, split T2A/T2B, and T3-T8 are
   failure-capable and separately wired. The joint fork interface reports only
   to joint-interface sufficiency; the complete S4 candidate test requires
   every mandatory leg and reports only to S4 candidate validity; no test
   reports to `derived`.
5. **Debt dominance.** The direct selector-bin roster size is 10. The 64th
   debt is `UNBINNED_LIVE_ROSTER_DEBT`; the selector-to-response edge is a
   `CROSS_CHAIN_INPUT_FEED`, not a demonstrated dominator. Maximum direct-bin
   movement is TYPE-R refuted; exact transitive rank is NO_VERDICT.

```text
order_audit_completed = true
S4_correspondence_check_completed = true
S4_surface_token_collision_found = true
S4_role_contract_specified = true
S4_test_verdict_wiring_audited = true
Q80_new_classes_named =
  UNBINNED_LIVE_ROSTER_DEBT,
  CROSS_CHAIN_INPUT_FEED

Q52_object_type_named = REFERENCE_CO_PARTICIPATION_CERTIFICATE

BRIDGE_SELECTOR_S4_REFERENCE_CO_PARTICIPATION_CERTIFICATE_derived = false | TYPE-U |
  would-build: Section 4 construction witness and all declared proof terms
S4_Tminus1_T0_T1A_T1B_T2P_T2A_T2B_T3_through_T8_executed = false | TYPE-U |
  would-execute: Section 6 concrete inputs and independent failure oracles

physical_verdict = NO_VERDICT |
  reason: S1, S2, S3, and P9-P12 remain TYPE-U and no physical test executed
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
```
