# Stage 8 / 7A Step 11 — Instance Batch 1 (Codex 2)

## 1. Scope and custody

This artifact records the bounded execution of sealed relay 726. It authors the five contract-ready targets named by `step11_tooling_family1/targets.generated.json`, runs the sealed Family-1 compiler against each authored instance, and reports the resulting row census. It does not admit a component, invoke the evaluator chain, alter a board, or execute any gated physical evaluation.

The relay bytes were verified before reading:

| object | SHA-256 |
|---|---|
| `relay_inbox/RELAY_PASTE_726_INSTANCE_AUTHORING_CODEX2_V001.md` | `f00bd9e7fd20c3a41636094ea43526c4aa6c3be22db6661cb39cdeca10250eca` |
| target manifest | `477d038935d69ada049e570a693a3218e4c7bf2706330f8ae3888fe0cc56cdf6` |
| box-schema delta | `b52e66b79787a55bad1553c05dfa8df52e7b11153879589d9627073a8e06bba9` |
| Family-1 compiler | `e5ac5f578ae82bb0e89590bf7dc4528c599502e5e9f9a6c7597b5d6416f8fbac` |
| compiler contract | `055e05ca59d04e6e4c3876dde50ac580b9033a11b9555cad81d2056fa1beaca7` |

Output-name collision checks were clear in the cleanroom and archive workspace before writing. `relay_outbox/726_ACK.md` was written before task work.

## 2. Authoring law and method

The authoring tool verifies the full digest of every cited sealed source and then the digest of the exact half-open span. Grounded span bytes are copied byte-for-byte to content-addressed payload files. Missing fields are represented only by a named owner, a reason code, and an exact absence-finding citation. Requirement prose is not serialized as evidence.

The partial carrier is closed by `step11_instance_batch1/contracts/partial_instance.schema.json`. Every instance declares:

- `completeness = PARTIAL`;
- exact source/span bindings for grounded material and absence findings;
- grounded field paths and content-addressed payloads;
- missing field paths with their 7A owners; and
- `admission = BARRED_STEP11_SUBGATE`.

The sealed corpus-wide M-2/object-name probes are carried by `STAGE8_TASK6_GROUNDING_RELOCATION_DARIO_V001.md`, SHA-256 `69334875b94679c16da9b8d6153242241ca3c202f0facc6130596b9807189e6f`. Its four-mode searches and near-miss adjudications are the absence authority used here; no fresh negative conclusion is substituted for them.

## 3. Authored instances

### 3.1 Per-target census

| target | completeness | grounded sealed material | missing elements and owner | instance SHA-256 |
|---|---|---|---|---|
| `CS:C-B-V008-05:universal-word-representation` | PARTIAL | representation: packet V011 `aa7c6d49…` `[32278,32330)` -> `9384b3c9…`; universal word `[33012,33051)` -> `6828baed…`; target/global word `[33855,33923)` -> `da5ffdac…` | `inverse_competitor`: 7A canonical inverse/opposite holonomy competitor normal form; `fixture_assignments`: 7A noncommuting fixture assignments. Absence finding `69334875…` `[8485,8696)`, `c25c6b23…` | `310a913f18367f0ad2c2a78620fc33ec290c0876652f94b9f2753ae41fd96fdd` |
| `MG:C-B-V008-05:inverse-opposite-holonomy-competitor` | PARTIAL | same three sealed positive fields; they delimit the known side of BX01 without inventing the competitor | same two missing fields. The superseded opposite-word near miss is expressly refused by `69334875…` `[8913,9460)`, `01a094ee…` | `6387f8962206a48d00029413d271f2778921697da758306f700ffcc0480384ca` |
| `CS:C-B-V008-10:seal-stage-graph` | PARTIAL | sealed preregistration `13cf1e17…` `[18920,19830)` -> `889515d3…`, preserving the displayed name-parent adjacency only | content-addressed stage artifacts; artifact-digest parent bindings; parent-map root. Owner: 7A formalization. Absence finding `69334875…` `[7550,7719)`, `dbade4c2…` | `b9deb520dc5400110d650d90778420e111fa58cf9991e961ae55f8502e4ce774` |
| `CS:C-B-V009-08:citation-claim-graph` | PARTIAL | no required BX09 element is sufficiently determined; the instance contains the sealed absence binding, not requirement prose | authority nodes and stable IDs; claim nodes and stable IDs; typed entailment edges; bounded general-FS premise carrier. Owner: 7A formalization. Absence finding `69334875…` `[8069,8221)`, `6e698bb4…` | `9c0bf9ffa4e4b8901e51d505a1da2416ebbcb778c3d4a578c6e17eced7fc8c5f` |
| `CS:C-B-V010-11:decorated-category` | PARTIAL | no required BX13 element is sufficiently determined; the instance contains the sealed absence binding, not a fabricated category | closed finite object list; complete decorated morphism triples; identity table; complete composition table; distinguished generator IDs. Owner: 7A formalization. Absence finding `69334875…` `[7901,8068)`, `fe5d699a…` | `a727c0bb361006d6256b2ba720c7c1fae03738be428510691e01276bd8b7bf04` |

Packet V011 is `review_packets/STAGE7_QSPEC_CANDIDATE_V001/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md`, SHA-256 `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a`. The preregistration is `provenance/boundary_incidence_dynamics_preregistration_v011.json`, SHA-256 `13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd`.

Four distinct positive payloads were emitted after content-addressed deduplication. Their SHA-256 values are `9384b3c9328738d742902c76a8588c0d48891ccf2b984de6732490bc03f54108`, `6828baed8c450bda097c5e9e0b4185f4a1bd1cd9882be3eb1fcaf3b9f1e138ec`, `da5ffdaca00f942dbad5b41caff46ccd21d5265362921305de19c703906d1c97`, and `889515d30cedf7d3af5da1a9e1ff7c7a88a1bf0d9227bdf37d64113302dfcb86`.

### 3.2 Generated authoring records

| record | SHA-256 |
|---|---|
| `step11_instance_batch1/generated/instances.generated.json` | `51fd7481750ba59b26c7dec8325889d86a2d4b8052fdd0b2885644e4dea8fbc9` |
| `step11_instance_batch1/row_status.generated.json` | `ff88652b543adb70ddb569e24146fa287b506d55be449c3f5ece1a03b5873860` |

## 4. Compiler execution

The existing compiler was invoked separately for each target with a target-specific, digest-pinned source manifest. Each partial instance was presented as available; the compiler verified its pinned inputs and then refused at the sealed full box schema. Exit `2 / SCHEMA_CONFORMANCE` is the honest result for an instance with named missing required fields. No `components/` object and no successful `compilation_result.json` was emitted.

| target | source-manifest SHA-256 | compiler result | refusal transcript SHA-256 | bound component |
|---|---|---|---|---|
| `CS:C-B-V008-05:universal-word-representation` | `a198983a6e42c80a290167e6d4e31f51f6207dc515098badbd0b309d386427b9` | exit 2, `SCHEMA_CONFORMANCE` | `c4ffb68c19adef2e917fd24ba9244511eb635bcb51ae9c8effd7e70c5b3e0743` | none |
| `MG:C-B-V008-05:inverse-opposite-holonomy-competitor` | `01aaaeb7cda8c39b7329309618c1c36a3441231614497da79c5f3d3f303f9dc3` | exit 2, `SCHEMA_CONFORMANCE` | `c4ffb68c19adef2e917fd24ba9244511eb635bcb51ae9c8effd7e70c5b3e0743` | none |
| `CS:C-B-V008-10:seal-stage-graph` | `debe79c630505beae1dff7543f4ac501649a82672ba94896e6704e35a727203e` | exit 2, `SCHEMA_CONFORMANCE` | `613429822ba3d64d9c50685529d6141a67c9630f606099a7a316f7ba23da26ca` | none |
| `CS:C-B-V009-08:citation-claim-graph` | `b90d2b62a087565db877142557c2a1e6db29cb3782f9c76e3253c94fdaa3bd4a` | exit 2, `SCHEMA_CONFORMANCE` | `d88f845384aeb9bad71bc5af2e943e377786cede302c7291e7fc711172fe59ae` | none |
| `CS:C-B-V010-11:decorated-category` | `295bfa39c0fc18bfe1fea7551aa324cffcd6269adad1e139b09aff49829d1afb` | exit 2, `SCHEMA_CONFORMANCE` | `31fe4989d783611237308e44c99760767d0c4a5528bb16261d96dcc4dcd95bf8` | none |

The closed compiler-attempt record is `step11_instance_batch1/compile_attempts/compile_attempts.generated.json`, SHA-256 `52bace82c379582e34d8b929b6ce676ff07aa23340d1aca03a528f2e0ed00736`.

## 5. Row census

| row | components produced | still missing | recomputed status |
|---|---:|---|---|
| `C-B-V008-05` | 0/2 | canonical inverse/opposite competitor; noncommuting fixture assignments | `PARTIAL_INSTANCE_PRESENT_SCHEMA_INCOMPLETE` |
| `C-B-V008-10` | 0/1 | content-addressed stage artifacts; artifact-digest parents; parent-map root | `PARTIAL_INSTANCE_PRESENT_SCHEMA_INCOMPLETE` |
| `C-B-V009-08` | 0/1 | authority nodes; claim nodes; typed entailment edges; bounded general-FS premise | `PARTIAL_INSTANCE_PRESENT_SCHEMA_INCOMPLETE` |
| `C-B-V010-11` | 0/1 | objects; morphisms; identities; composition; generator IDs | `PARTIAL_INSTANCE_PRESENT_SCHEMA_INCOMPLETE` |

These rows advance only in documentary status: a sealed, machine-readable partial instance and a compiler refusal now exist. They do not advance to a stateable or admitted component.

## 6. Self-check, inventory, and gates

The static self-check parsed all three tools, rehashed all five instance files and all four payloads, confirmed five `SCHEMA_CONFORMANCE` refusals, confirmed zero component bindings, and checked the admission value. It is recorded at `step11_instance_batch1/self_check.generated.json`, SHA-256 `25d50b52a33bb9234947a000bc91451566563aca443fe1e3d6926ff24fe573d0`.

The package inventory contains 33 self-excluding file rows at `step11_instance_batch1/inventory.generated.json`, SHA-256 `776c745d081d0e561fa10f4dc006eec265d55aa71b8a102acce5de1c3e338955`.

Gate audit: `alpha_computed = false`; `proof_authorized = false`; `kappa_record_computed = false`. No member binding, fixed-point execution, end test, physical-quantity evaluation, or measured-constant comparison occurred. `CHAIN_INVOKED = false`.

Verb audit under the verdict-line scope rule: the verbs in this artifact report file verification, byte extraction, local schema/compiler execution, and status compilation only. They do not claim mathematical proof, evaluator admission, board closure, or authorization. Result: CLEAN.

INSTANCES = 5 authored (0 complete / 5 partial; gaps named)
COMPILED = 0 bound (compiler output digests displayed; 5 SCHEMA_CONFORMANCE refusals)
ROWS_ADVANCED = C-B-V008-05, C-B-V008-10, C-B-V009-08, C-B-V010-11 (PARTIAL_INSTANCE_PRESENT_SCHEMA_INCOMPLETE)
ADMISSION = barred, stated
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
