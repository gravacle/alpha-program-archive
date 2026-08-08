# Stage 8 / 7A Step 11 — V008-10 Stage Binding (Codex 2)

## 1. Scope and preflight

This artifact records sealed relay 728. The relay was verified at SHA-256 `d70cb2df67f321e20a683e4e261982da60fd61f31b03d46fea2e93b33b9adc61`; the lane guard matched `CODEX 2`; and `relay_outbox/728_ACK.md` was written before task work. The output report, seal sidecar, and `step11_v008_10_stage_binding/` package were absent in the cleanroom and archive workspace before writing.

The task is confined to `CS:C-B-V008-10:seal-stage-graph`. It does not change the sealed adjacency, descriptor, box schema, board, admission state, or evaluator chain.

## 2. Grounded adjacency and searched spaces

The authoritative adjacency remains the `review_stage_semantics.stage_dependencies` value in `provenance/boundary_incidence_dynamics_preregistration_v011.json`, full-file SHA-256 `13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd`, bytes `[18920,19830)`, span SHA-256 `889515d30cedf7d3af5da1a9e1ff7c7a88a1bf0d9227bdf37d64113302dfcb86`. It contains 11 nodes and 17 child-to-parent edges.

The stage-status authority is the same sealed source, bytes `[23996,30395)`, span SHA-256 `b368767d8f9f1034ac39b392389e32910f09737684dd722f0f2b2715ad6ad1d3`. Every status field corresponding to an adjacency node is `false`.

The probe searched three overlapping custody surfaces deliberately, so a cleanroom/archive spelling or broader-program location could not create a false negative:

| searched space | files seen | UTF-8 text files searched | large text candidates skipped |
|---|---:|---:|---:|
| cleanroom | 5,711 | 5,117 | 0 |
| archive workspace | 5,025 | 4,938 | 0 |
| broader `gravity_emergence_evidence_program` space | 49,203 | 25,276 | 40 |

The 40 larger files were still filename-probed; they were not decoded as text. All candidate stage records are textual custody artifacts, so no binary object was treated as a stage record. Newly written `step11_v008_10_stage_binding/` bytes were writer-excluded from the search.

For every node the probe used four surfaces: exact hyphenated name in content, punctuation/case-normalized filename, exact JSON `stage`/`stage_id` value, and direct seal-attachment names (`.seal.sha256`, packet manifests, and sealed inventories). Reference-only occurrences do not realize a stage. The closed machine record is `step11_v008_10_stage_binding/generated/search_record.generated.json`, SHA-256 `bf0e4fc9883b40b65d09b9bdd8c76cd0d251b18909a10bdad46a77e29e152dfc`.

## 3. Per-stage disposition

The provenance source names the stage definitions and their prerequisites. It does not name a content-addressed artifact realizing any stage, and the same source expressly records every realization status as false.

| stage node | literal parents | status field | sealed realizing artifact | disposition |
|---|---|---|---|---|
| `SPEC-SEAL` | none | `BID_v011_specification_sealed=false` | none | `ABSENT_OF_RECORD` |
| `CORE-RESULT-SEAL` | `SPEC-SEAL` | `BID_core_result_sealed=false` | none | `ABSENT_OF_RECORD` |
| `PARENT-COMPARISON` | `CORE-RESULT-SEAL` | `BID_parent_comparison_completed=false` | none | `ABSENT_OF_RECORD` |
| `HOLDOUT-UNIVERSE-SEAL` | `SPEC-SEAL` | `holdout_universe_sealed=false` | none | `ABSENT_OF_RECORD` |
| `QSPEC-SPEC-SEAL` | `SPEC-SEAL` | `Qspec_specification_sealed=false` | none | `ABSENT_OF_RECORD` |
| `PREDICTION-MAP-SEAL` | `HOLDOUT-UNIVERSE-SEAL`, `QSPEC-SPEC-SEAL` | `prediction_map_sealed=false` | none | `ABSENT_OF_RECORD` |
| `THOMSON-RESULT-SEAL` | `CORE-RESULT-SEAL`, `QSPEC-SPEC-SEAL` | `Thomson_result_sealed=false` | none | `ABSENT_OF_RECORD` |
| `ALPHA-RESULT-SEAL` | `THOMSON-RESULT-SEAL`, `PARENT-COMPARISON`, `HOLDOUT-UNIVERSE-SEAL`, `PREDICTION-MAP-SEAL` | `alpha_result_sealed=false` | none | `ABSENT_OF_RECORD` |
| `HOLDOUT-RESULT-SEAL` | `ALPHA-RESULT-SEAL` | `holdout_result_sealed=false` | none | `ABSENT_OF_RECORD` |
| `END-TO-END-RECONSTRUCTION-SEAL` | `ALPHA-RESULT-SEAL`, `HOLDOUT-RESULT-SEAL` | `independent_end_to_end_reconstruction_sealed=false` | none | `ABSENT_OF_RECORD` |
| `FINAL-CLAIM-SEAL` | `END-TO-END-RECONSTRUCTION-SEAL`, `HOLDOUT-RESULT-SEAL` | `BID_final_claim_sealed=false` | none | `ABSENT_OF_RECORD` |

Thus `path`, full-file digest, and seal-attachment mode are null for all 11 nodes. Supplying a specification, result, prediction, assembly, or report that merely mentions a node would approximate a missing stage seal with a prerequisite or near-match and is barred.

### 3.1 Near-match adjudication

The normalized filename probe found `stage8_execution/spec_seal.sha256`, SHA-256 `57890038a7b60d8c328e8b305cfe5a9d9498af49a2306a8d16567dd2856ec715`. It correctly verifies the file `STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_AUTHORITY_FABLE_V002.md`, SHA-256 `ddb36cbfe4edfc2a0520e9ae58063295214c64afed5cad5a64e9f311826358f5`.

It is not the BID `SPEC-SEAL` artifact. Its own ceiling at bytes `[1214,2057)`, span SHA-256 `41cde04fe5d34e9362acaaf584176652ac9633b2914ee7107d68a68752091d90`, states that `SPEC-SEAL` is unattainable, that the strongest possible result is pending, and that `BID_core_result_sealed` remains false. The candidate is therefore `REJECTED_NEAR_MATCH`, not located stage evidence.

No exact JSON `stage` or `stage_id` self-identification was found for any of the 11 names. No packet-manifest or sealed-inventory member supplies such a record.

## 4. Digest parents and parent-map root

Digest parents are mechanically determined only after each literal parent has a realizing artifact digest. Because all 11 stage artifacts are absent, all 17 parent edges remain named but their `artifact_sha256` operands are null. No `COMPARE(X,X)` construction, status digest, reference-document digest, or shared provenance-file digest was substituted.

The root-formula probe found 14 files containing the term `parent_map_root` or its punctuation variants. They consist of the BX03 schema field declaration, prior partial-instance/report records, and this relay request; none defines a sealed serialization and hashing formula for the BX03 parent-map root. The document-root formula in the lineage-V2 matrix is scoped to a different schema and was not borrowed.

Accordingly:

```text
PARENT_DIGEST_BINDINGS = 0 / 17
PARENT_MAP_ROOT_FORMULA = ABSENT_OF_RECORD
PARENT_MAP_ROOT_VALUE = null
ROOT_STATUS = GAP_NO_SEALED_FORMULA
```

The updated partial instance is `step11_v008_10_stage_binding/CS_C-B-V008-10_seal-stage-graph.partial.v002.json`, SHA-256 `09116f010d3168bb4bd9d9875e1da61369b9e3ee949decd83b441400a7b994e8`. It retains all 11 literal nodes and parents, binds both authoritative source spans, records every missing artifact and parent digest, and leaves the root null. It validates against the closed local partial schema `urn:rd22:step11:v008-10:stage-binding-partial:v002`.

A second gap is displayed rather than repaired silently: the sealed BX03 full schema accepts exactly three differently named stages (`SPECIFICATION_SEAL`, `EXECUTED_CORE_RESULT`, `FINAL_ALPHA_CLAIM`), while the principal-selected grounded object has 11 named nodes. No sealed mapping from the 11-node adjacency to that three-stage instance shape is of record.

## 5. Compiler rerun

The existing Family-1 compiler, SHA-256 `e5ac5f578ae82bb0e89590bf7dc4528c599502e5e9f9a6c7597b5d6416f8fbac`, was rerun with a target-specific source manifest, SHA-256 `5c6fe82e766f6b0a00d45d77d2cdadded7aaae462c77eab9ec6d164bd09a5e38`. The result was the required fail-closed outcome:

```text
EXIT = 2
STATUS = SCHEMA_CONFORMANCE
COMPONENT_BOUND = false
STDERR_SHA256 = 87a6333746461576fd0464180d0a3a03e201058bc9691e7538fc649ec5b6de90
```

The remaining fields are: 11 stage realization artifacts; their 17 digest-parent bindings; a sealed parent-map-root formula and value; and a sealed mapping, if one is intended, between the 11-node authoritative adjacency and the BX03 three-stage schema. The closed result record is `step11_v008_10_stage_binding/generated/binding_result.generated.json`, SHA-256 `09cb94eeb6fb844292faad142747e1b6dc8edb8931d3704882636a2ab8f13ef5`.

## 6. Gates and verb audit

The probe and compiler rerun performed only file discovery, hashing, schema validation, and fail-closed compilation. `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false`. No member binding, fixed-point execution, end test, physical-quantity evaluation, or measured-constant comparison occurred. Admission remains `BARRED_STEP11_SUBGATE`; the evaluator chain was not invoked.

Verb audit: this report distinguishes a node definition from a realized stage, cites false statuses and exact search results, and claims no mathematical proof, stage seal, row PASS, admission, or authorization. CLEAN.

STAGES = 0 located / 11 absent-of-record (SPEC-SEAL, CORE-RESULT-SEAL, PARENT-COMPARISON, HOLDOUT-UNIVERSE-SEAL, QSPEC-SPEC-SEAL, PREDICTION-MAP-SEAL, THOMSON-RESULT-SEAL, ALPHA-RESULT-SEAL, HOLDOUT-RESULT-SEAL, END-TO-END-RECONSTRUCTION-SEAL, FINAL-CLAIM-SEAL)
ROOT = gap named (no sealed BX03 parent-map-root formula; 17 parent digest bindings unavailable)
COMPILE = SCHEMA_CONFORMANCE (remaining fields named)
ADMISSION = barred, stated
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
