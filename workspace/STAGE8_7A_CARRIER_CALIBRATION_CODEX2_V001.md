# STAGE 8 / 7A STEP 11 — ONE-CARRIER CALIBRATION — CODEX 2 V001

Lane: Codex 2  
Relay: PASTE 718  
Disposition: `C-B-V010-12` selected; two exact source components assembled into a content-addressed partial carrier; eight underdetermined elements withheld and named; envelope re-authored as partial  
Authority claimed: none

```text
RELAY_SHA256 = 7716c364b5014e40852b9a7e200f1818290caa03c341473ed508190b5573b9b3
Q595_MAP_SHA256 = e85a6113e5b45624d19f987ae2603f63ac418df10f33669cc6a44742e5918ed5
SPEC_V012_SHA256 = 382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504
CHECK_MAP_SHA256 = 280004821c532def203ae81cec35bcac26bd3ab4bdd03752f5196aa7b9c23f3d
BATCH1_SHA256 = 7fda8fa0dde32c82d013cc6d1a84b2ddebefe5fab4703ec68e7b62857db5dcde
SOURCE_SHA256 = 13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd
CHAIN_INVOKED = false
```

## 1. Pickup, jurisdiction, and collision check

The single relay-718 inbox file and its sidecar agree at the displayed digest,
and the file's lane guard says `CODEX 2`. `relay_outbox/718_ACK.md` was written
before substantive work. The carrier, envelope, report, and their sidecar names
were absent in the cleanroom and archive workspace before creation.

The jurisdiction is authoring only. No evidence manifest, descriptor, evaluator
package, board, register, road, plan, tracker, or git state was changed. No
chain ran. `alpha_computed=false`, `proof_authorized=false`, and
`kappa_record_computed=false`; no member binding, fixed-point execution, end
test, physical-quantity evaluation, or measured-constant comparison occurred.

## 2. CC1 — ranking and selection

The ranking criterion is **fraction of the descriptor's consumable carrier
already fixed by exact sealed bytes**, not apparent mathematical simplicity.

| Rank | Batch-1 row | Exact material already of record | Missing load-bearing material | Selection result |
|---:|---|---|---|---|
| 1 | `C-B-V010-12` | one principal-selected 11-node adjacency object and the 11 required report-field names | closed report schema/instances, content-addressed parents, two mutations, rejection records, receiver binding | selected |
| 2 | `C-B-V008-10` | the same graph half | content-addressed parents plus two sealed M-2 corpora | not selected |
| 3 | `C-B-V010-11` | a universal decorated-category schema | no closed finite object/morphism/identity/composition instance | not selected |
| 4 | `C-B-V010-14` | the query name and criterion ordering | claim DAG, corpus, Hessian instance, mutations, and two descriptor opcodes absent from the check-map contract | not selected |
| 5 | `C-B-V009-08` | the two authority classes are named | no citation nodes, claim IDs, typed entailment edges, or sealed corpus | not selected |

`C-B-V010-12` wins because an actual finite machine object—not merely a schema
or requirement—is available. That does not make the full row stateable.

## 3. CC2 — carrier production

### 3.1 Closed carrier interface

The output implements this exact-key schema inventory; all unlisted keys fail:

```json
{"additionalProperties":false,"component_keys":{"report_schema_required_fields":["fields","serialization_sha256","source"],"stage_dependencies":["graph","serialization_sha256","source"]},"required":["check_id","descriptor_sha256","grounded_components","schema","self_check","status","ungrounded_elements"],"schema_const":"rd22.step11-partial-carrier.v001","self_check_keys":["canonical_serializations_reproduced","source_digests_verified","source_spans_verified","ungrounded_not_serialized"],"source_keys":["byte_length","path","sha256","span","span_sha256"],"status_const":"PARTIAL"}
```

The carrier is tight canonical UTF-8 JSON with lexicographically sorted object
keys and no trailing newline.

### 3.2 Exact source extraction and serialization

Only `provenance/boundary_incidence_dynamics_preregistration_v011.json`, sealed
at `13cf1e17…`, supplies positive carrier bytes.

| Component | Exact source value span | Raw span SHA-256 | Canonical serialization | Canonical SHA-256 | Transformation |
|---|---|---|---:|---|---|
| `report_schema_required_fields` | `[16621,16875)` | `3346cd18b453a7cd58ee39895748cea9d06fa2a043a7516186f479634e40462c` | 172 bytes | `95c182a9f08f59053c1c46b3144b084a2ce219f7071f9fd8c34051f3a61c95f7` | parse the exact JSON array; serialize the same ordered strings tightly |
| `stage_dependencies` | `[18920,19830)` | `889515d30cedf7d3af5da1a9e1ff7c7a88a1bf0d9227bdf37d64113302dfcb86` | 594 bytes | `a68204715597d161ece10ac731566e0b55bc3c4b237051b282e43adc1f73c736` | parse the exact JSON object; sort keys only; retain every parent array byte-value |

The graph serialization digest independently reproduces the graph payload used
by the lawful `C-B-V009-06` envelope. The second `stage_dag` encoding and
`status.stage_dependency_graph_acyclic` are excluded: the former is not the
principal-selected encoding, and the latter is a status the criterion expressly
forbids as evidence.

The exact report-field array is:

```text
schema_version, bundle_sha256, stage, reviewer_role, process_id, verdict,
blockers, full_matrix_attestation, no_edit_attestation, artifact_hashes,
created_utc
```

The exact adjacency serialized into the carrier is:

```text
SPEC-SEAL                      <- []
CORE-RESULT-SEAL               <- [SPEC-SEAL]
HOLDOUT-UNIVERSE-SEAL          <- [SPEC-SEAL]
QSPEC-SPEC-SEAL                <- [SPEC-SEAL]
PARENT-COMPARISON              <- [CORE-RESULT-SEAL]
PREDICTION-MAP-SEAL            <- [HOLDOUT-UNIVERSE-SEAL, QSPEC-SPEC-SEAL]
THOMSON-RESULT-SEAL             <- [CORE-RESULT-SEAL, QSPEC-SPEC-SEAL]
ALPHA-RESULT-SEAL               <- [THOMSON-RESULT-SEAL, PARENT-COMPARISON,
                                    HOLDOUT-UNIVERSE-SEAL, PREDICTION-MAP-SEAL]
HOLDOUT-RESULT-SEAL             <- [ALPHA-RESULT-SEAL]
END-TO-END-RECONSTRUCTION-SEAL  <- [ALPHA-RESULT-SEAL, HOLDOUT-RESULT-SEAL]
FINAL-CLAIM-SEAL                <- [END-TO-END-RECONSTRUCTION-SEAL,
                                    HOLDOUT-RESULT-SEAL]
```

### 3.3 Searched-space result and ungrounded elements

The current cleanroom search examined 5,591 files, including 478 JSON files;
475 parsed. A recursive exact-key search found:

```text
objects satisfying the source's 11 report_schema_required_fields = 0
parent_mutation/core_alpha_mutation key candidates                 = 0
```

This present search agrees with the sealed corpus-wide relocation finding at
`STAGE8_TASK6_GROUNDING_RELOCATION_DARIO_V001.md[7249,7549)`.

Eight elements remain `UNGROUNDED` and are serialized only as names in the
carrier's refusal list, never as invented arguments:

| Ungrounded element | Why the procedure cannot consume it |
|---|---|
| `CLOSED_REPORT_SCHEMA_TYPES_AND_EXTRA_FIELD_RULE` | the source fixes required names but no field types or closed extra-field rule |
| `CONTENT_ADDRESSED_STAGE_PARENT_KEYS` | all twenty parent references are stage names, not content digests |
| `CONTENT_ADDRESSED_STAGE_REPORT_INSTANCES` | zero conforming report objects exist in the searched sealed corpus |
| `PARENT_MUTATION_INSTANCE` | no target parent/edge and mutation operation are fixed |
| `PARENT_MUTATION_EXPECTED_REJECTION` | no content-addressed expected result is fixed |
| `FORBIDDEN_CORE_ALPHA_MUTATION_INSTANCE` | no exact inserted field/path/value is fixed |
| `FORBIDDEN_CORE_ALPHA_MUTATION_EXPECTED_REJECTION` | no content-addressed expected result is fixed |
| `MUTATION_RECEIVER_BINDING` | the current check map exposes one nonrepeatable `DAG` result and no carrier binding for the positive graph plus two mutations |

Consequently the carrier is **partial**. Manufacturing any one of these objects
would encode a choice the descriptor is supposed to test.

Carrier produced:

```text
PATH = STAGE8_7A_CARRIER_C_B_V010_12_CODEX2_V001.json
BYTES = 2274
SHA256 = 725a66656b0ac0e15d3911ab79fd8b49e251a9f2e0a15485b7ece228bfc54f52
STATUS = PARTIAL
```

## 4. CC3 — re-authored envelope

### 4.1 Closed partial-envelope interface

```json
{"additionalProperties":false,"admission_keys":["allowed","bar","chain_invoked"],"authoring_result_keys":["candidate_record","carrier","missing_carriers","stateable","status"],"criterion_keys":["descriptor_sha256","execution_class","expected_predicate","opcodes","procedure"],"grounding_keys":["required_candidate_fields","subject_payloads"],"required":["admission","authoring_result","check_id","criterion","grounding","schema","self_check"],"schema_const":"rd22.step11-partial-envelope.v001","self_check_keys":["admission_bar_present","candidate_absence_matches_partial","carrier_digest_verified","citation_keys_unique","closed_opcode_language","descriptor_digest_matches","schema_keys_exact","span_coverage"],"status_const":"PARTIAL","subject_payload_keys":["byte_length","role","source_path","source_sha256","span","span_sha256"]}
```

The V002 envelope binds the carrier as a whole-file content-addressed payload,
binds both exact source spans, the current V012 descriptor row, and the blocker
span. It preserves the descriptor's `DAG` criterion and expected predicate
byte-for-byte. Because the carrier is incomplete, `candidate_record=null`,
`stateable=false`, and no seven-field invocation is emitted.

The admission record is exactly:

```json
{"allowed":false,"bar":"STEP11_BUILDER_B_CONTRACT_SUBGATE","chain_invoked":false}
```

Envelope produced:

```text
PATH = STAGE8_7A_ENVELOPE_C_B_V010_12_CODEX2_V002.json
BYTES = 3031
SHA256 = 92b5d374b811ce90c5de70dfad8df09f24b363f0b3315d617ac04aa1e7e50426
STATUS = PARTIAL
STATEABLE = false
```

## 5. Static self-check transcript

No evaluator opcode was executed. The graph parse below is a static carrier
integrity check, not a row verdict.

```text
CARRIER_SCHEMA_KEYS                    PASS
CARRIER_TIGHT_CANON                    PASS
CARRIER_TRAILING_NEWLINE               absent
SOURCE_FILE_SHA256                     2/2 PASS
SOURCE_SPAN_SHA256_AND_LENGTH           2/2 PASS
CANONICAL_COMPONENT_SERIALIZATION      2/2 PASS
STAGE_GRAPH_PARSE                      11 nodes / 20 references / all declared
STAGE_GRAPH_ACYCLIC_STATIC_CHECK       PASS
UNGROUNDED_SERIALIZED_AS_ARGUMENTS     0/8
ENVELOPE_SCHEMA_KEYS                   PASS
ENVELOPE_TIGHT_CANON                   PASS
CARRIER_WHOLE_FILE_BINDING             PASS
ENVELOPE_SUBJECT_DIGESTS               5/5 PASS
ENVELOPE_SUBJECT_SPANS                 5/5 PASS
ENVELOPE_CITATION_KEYS                 5/5 UNIQUE
CURRENT_DESCRIPTOR_DIGEST_BINDING      PASS
SEVEN_FIELD_FUTURE_CANDIDATE_INVENTORY PASS
ADMISSION_BAR                          PASS
CHAIN_INVOKED                          false
```

## 6. CC4 — observed cost and remaining-57 projection

### 6.1 Actual calibration cost drivers

| Work class | What consumed the relay |
|---|---|
| locating | rank five candidates; follow the Q-595 spans, sealed relocation, current V012 descriptor, check map, and provenance source |
| source discrimination | reject `stage_dag` and the status flag; retain only the principal-selected `stage_dependencies` object |
| span work | resolve and rehash two exact JSON value spans rather than copying enclosing prose or keys |
| derivation | parse and tightly serialize the exact array and graph; independently check declared references and acyclicity |
| binding | bind source file, spans, component serializations, current descriptor, whole carrier, and envelope citation keys |
| negative search | parse 475 JSON documents for conforming report instances and mutation objects |
| interface audit | identify that one nonrepeatable `DAG` receiver does not bind the positive graph and two mutation cases |

The calibration is decisive for SI/S source work: one relay can locate, extract,
bind, and self-check a small finite carrier **when bytes determine it**, but one
relay cannot lawfully complete absent report instances, mutations, or receiver
law. This row itself still needs separately authorized source production and a
closed receiver contract before it can become stateable.

### 6.2 Remaining 57 rows

After excluding the already lawful `C-B-V009-06` and this calibration row, the
Q-595 cross-census is:

```text
SI = 26  (S:15, M:8, L:3)
EC =  7  (M:4, L:3)
KP =  1  (L:1)
MX = 23  (M:4, L:19)
TOTAL = 57
```

The relay-equivalent bands below assume one row is carried independently and
include source-gap resolution, but not Builder B admission work or chain runs.
Only the SI/S band has a direct one-row calibration; the other bands are
map-complexity projections and are marked lower confidence.

| Class | Rows | Evidence-based carrier work | Projected authoring relays | Confidence |
|---|---:|---|---:|---|
| SI | 26 | finite schema/table/graph extraction; calibration shows one relay reaches a checked partial and a second source act may be needed | 26–60 | moderate for S, low for M/L |
| EC | 7 | carrier plus independently replayable grammar/completeness certificate and ID binding | 14–28 | low |
| KP | 1 | proof formalization, axiom pinning, kernel replay, and conclusion binding | 3–6 | low |
| MX | 23 | two or more load-bearing SI/EC/KP components plus integration and cross-binding | 69–138 | low |
| **Total** | **57** | authoring only | **112–232** | planning band, not commitment |

The calibration row's own completion debt is outside the remaining-57 band. Its
eight names collapse into at least three separate bounded source/contract acts:
(1) close and instantiate report schemas, (2) bind stage parents to those report
digests, and (3) define both mutations, their expected rejection records, and
their receivers.

## 7. Does-not-do and verb audit

The carrier is evidence assembly, not evidence of a passing criterion. The
static graph check does not supply the absent parent digests, reports, mutations,
or receiver binding. The partial envelope is not admitted, the evidence manifest
is untouched, and no row, board, physical claim, or seal changes state.

Verb audit under the verdict-line scope rule: CLEAN. “Produced” means the two
source-determined components were serialized into a partial carrier. “Derived”
means deterministic parsing/canonicalization and static graph integrity only.
“Projected” is a planning band. No proof, physical, evaluator, board, or seal
verdict is claimed.

ROW = C-B-V010-12 (ranking displayed)
CARRIER = partial (ungrounded elements named: CLOSED_REPORT_SCHEMA_TYPES_AND_EXTRA_FIELD_RULE; CONTENT_ADDRESSED_STAGE_PARENT_KEYS; CONTENT_ADDRESSED_STAGE_REPORT_INSTANCES; PARENT_MUTATION_INSTANCE; PARENT_MUTATION_EXPECTED_REJECTION; FORBIDDEN_CORE_ALPHA_MUTATION_INSTANCE; FORBIDDEN_CORE_ALPHA_MUTATION_EXPECTED_REJECTION; MUTATION_RECEIVER_BINDING)
ENVELOPE = partial
SELF_CHECK = displayed
PROJECTION = SI 26 rows / 26-60 relays; EC 7 / 14-28; KP 1 / 3-6; MX 23 / 69-138 (112-232 total; authoring only)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN / (+partial carrier only; no candidate invocation, admission, PASS, board change, or seal claim)
