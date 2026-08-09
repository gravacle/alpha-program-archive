# Stage 8 / 7A Step 11 — Tooling Family 2 and the V009-08 corpus binding

**Lane:** CODEX 2  
**Relay:** 752  
**Disposition:** deterministic finite-family/expectation-ledger generator built and executed; admission barred

## 1. Pickup, custody, and scope

| Object | SHA-256 | Result |
|---|---|---|
| `relay_inbox/RELAY_PASTE_752_TOOLING_FAMILY2_CODEX2_V001.md` | `ba49ca3df004bb616d006ae57751abe31d3d3b439c80d428f919f78c524079e6` | seal sidecar verified before reading |
| pickup acknowledgement | `752 \| CODEX 2 \| ba49ca3df004bb616d006ae57751abe31d3d3b439c80d428f919f78c524079e6` | written before task work |

The requested report, report seal, `752_DONE.md`, and `step11_tooling_family2/` were absent in the cleanroom and archive workspace at preflight. All writes are cleanroom-only.

Family 2 was run over the four sealed complete instances named by the relay and the five-target batch lineage. It generates a finite family and exact expectation ledger for each complete instance. The expectation ledgers contain exact member IDs and digests projected from the sealed instances; they are **not** copied from prior PASS results and do not carry evaluator criterion directions. The sealed V009-08 corpus is separately bound to its existing CD target by generated data.

This bounded run does not claim to discharge every planned FG/EL element in the Q-626 map. Rows without a sealed input instance were not started or inferred from requirement prose.

## 2. Generated input manifest and pins

The tool generated `inputs.generated.json` from current bytes; no digest is embedded in source. Input-manifest SHA-256: `e3e62dc34f2be62eadda4e2f1ce5327c659f4a48399edf4e37e2152ddeb0c762`.

### 2.1 Complete instances

| Row | Instance SHA-256 | Closed-schema SHA-256 | Sealing-report SHA-256 |
|---|---|---|---|
| `C-D-A35-02-QUASIFREE-CAR-LIFT` | `47485f836710f3819bfda19744b9303e0f9cd065d93fa6859df4b27efb7eb03a` | `f47236e6033112f76801a515e2b2b9fc3ba71aa569bbd5153cb39bed028a9d7a` | `04eab6a7e6264abcb0f04647967de4e0378650b229365cec3ebed74585969cf3` |
| `C-B-V010-11` | `664059f4b10f1b78b1e04f111b77adc556644378a741622603bfbba957aa2b2d` | `d7c283070669c546b87ff5185b2432cbfb641c917de618108c0fcddc2d0e1e58` | `a8ceb54a22f026e8f2953cd5289e7c1172aa1a5c096788cd9ea23e0866ff2c9e` |
| `C-B-V009-08` | `c41f5d05c0bc784281206aede14e310b7b7e68304cbb81c8b43e787a0ac23f84` | `96853a3751ae8e6dc149377f45517b1ac329d4729883d86c61d2fcfbbdd2b1b2` | `dff7e3506022559dff7a25d90ec97dea6838bfb775f3e1f434ea7d1ad923c38c` |
| `C-B-V008-05` | `0a400a1d19c436edd1a407c95390916a908f57281176ec22491eb139fb107775` | `aeea1f6183d76155b122b985ef7442f6f73f8a1116bf6e7e99b6c5d14c161331` | `7e9e7772df33d21ac46833539af8d561bf986f9153c34a85333c944376c24ae5` |

Each sealing-report sidecar was verified. Each instance passed its closed schema. All nested content references were checked by path, byte length, and digest; source citations were checked against complete source-file hashes, half-open bounds, and span hashes. On the instance surfaces there are 12 content references and 28 span references; nested referenced JSON payloads were opened and their additional references verified as well.

### 2.2 Batch, target, and corpus pins

| Input | SHA-256 |
|---|---|
| batch manifest, 5 targets | `51fd7481750ba59b26c7dec8325889d86a2d4b8052fdd0b2885644e4dea8fbc9` |
| Family-1 target manifest | `477d038935d69ada049e570a693a3218e4c7bf2706330f8ae3888fe0cc56cdf6` |
| Family-1 validator/compiler | `e5ac5f578ae82bb0e89590bf7dc4528c599502e5e9f9a6c7597b5d6416f8fbac` |
| current V008-10 partial | `09116f010d3168bb4bd9d9875e1da61369b9e3ee949decd83b441400a7b994e8` |
| V008-10 binding result | `09cb94eeb6fb844292faad142747e1b6dc8edb8931d3704882636a2ab8f13ef5` |
| sealed general-FS corpus definition | `2584d89444bb17ec335b89dfc32a6b38176e8a05bdef10bcdff1235f1699dacf` |
| sealed-corpus-definition schema | `7d4ffe726fe11231fa2445410d8733bb0e98270e75a3e99573bba1f4ad67ab60` |

The batch, Family-1, and stage-binding reports and their seals are also content-addressed in the input manifest. The corpus's own seal sidecar reverified.

## 3. AD1 — tool and closed interfaces

Package root: `step11_tooling_family2/`.

| Package object | Purpose | SHA-256 |
|---|---|---|
| `generate_finite_families.py` | pin generation, sealed-instance validation, deterministic adapters, ledger generation, corpus binding, batch reconciliation, controls | `3e709e784620416b85c2205e771cbed5d71137220c99be39faa427909c6c9469` |
| `contracts/tooling_family2.schema.json` | closed input, family, certificate, ledger, binding, batch, row, and result schemas | `1af6b916bf1714bf8eb87f816d4895eba0a23017a50ba24bccbd0a60660210ff` |
| `inputs.generated.json` | generated content-addressed input manifest | `e3e62dc34f2be62eadda4e2f1ce5327c659f4a48399edf4e37e2152ddeb0c762` |
| `generated/run_result.json` | complete output/row/owner census | `1f25678619ffa6c12f5cd4602b44b028ce4d8a26c37a13a9474f57b1e75056ff` |
| `generated/self_check.json` | exercised controls and verification census | `31a6cf27e30f586ab1c4609288d719a6adb1e363ca1f715ea48279b05e2c4f33` |
| `generated/batch_reconciliation.json` | five old partial targets -> current disposition | `c0a18160980a66f9f8ff40ca9b1d4f15c1babf52d14e59c888ed3938d4755123` |
| `inventory.generated.json` | self-excluding 19-member package inventory | `a89c38894644041bace7067111d107a7b8621054d0bc74902a6cbe79e02886a3` |

The tool is standard-library-only and ran directly under `python3 -I -S -B`. Canonical JSON is tight sorted UTF-8 with no trailing newline and NaN barred. Paths reject absolute forms and traversal outside the cleanroom. There is no load-bearing `assert`.

For each row adapter, the generator enumerates the sealed instance's typed members, sorts IDs by UTF-8 bytes, rejects duplicate IDs, records both the canonical member-value digest and the underlying material digest, and emits a completeness certificate. The certificate records schema validation, source/content verification, the member census, the ordered-ID digest, zero duplicates, and full coverage of that adapter's source slots.

The expectation ledger is generated from the same sealed instance values under the explicit basis `SEALED_INSTANCE_MEMBER_VALUES_NOT_PRIOR_PASS_OUTPUTS`. A ledger must reproduce the family ID set and both digest columns exactly. Thus a prior positive compile cannot author an expectation here.

## 4. AD2 — finite families and expectation ledgers

| Row | Enumerated family | Members | Expected ledger | Projection |
|---|---|---:|---|---|
| `C-D-A35-02-QUASIFREE-CAR-LIFT` | `d1f80d8fe09f6ff781059ae48c09d5fdb5a8f9784b74cd54f772cca7ba5b8ade` | 6 | `ca9a18348cd728c9dc7700cf868337db1a3ca24dcab5845ecc816bf1cbba03d5` | six sealed element IDs and content digests |
| `C-B-V010-11` | `679688a7f02ec0b3b77bfdadd23bc63824c46cd37f92bf45d5ac10ca9679c00f` | 28 | `e9a9ed8c8ceb6c6722a9c65862a1c30124d4af86391b82bdeddc39cc48af6cc1` | 4 objects, 7 morphisms, 4 identities, 10 compositions, 3 generators |
| `C-B-V009-08` | `19b8e390250016e0f3450f4f43f276554dd368d6b374b24ef037041d1fb430a1` | 17 | `ac12fe0f33435457a1966b88713ba15d6894930dc8c7ec80e186d1b4efbb7a79` | 4 authorities, 4 claims, 8 edges, 1 premise |
| `C-B-V008-05` | `e97a6737a52f15c324b39ee7a0134e8957db063402c899e15d48b62f58c7e5b3` | 5 | `7e65a4cb919c94c1c2f5d48020eb287e351d9bd66ce5d5c139328da5618ac329` | universal word, representation, target, competitor, fixture |
| **Total** | **4 families** | **56** | **4 ledgers** | exact, ordered, complete under the four closed adapters |

All eight records are content-addressed by filename. Independent replay confirmed that every family and ledger satisfies its closed schema, every ID order is canonical, no ID is duplicated, and every ledger is an exact two-digest projection of its family.

## 5. Generated V009-08 corpus binding

The generator consumed the sealed corpus definition rather than rewriting its member list. It reverified:

- schema `rd22.sealed-corpus-definition.v001`;
- the one 603-byte member at SHA-256 `696c54751fd572d878f45c1d978fdf668e364aa15df82c64e6a21d8cb223b343`;
- declared content root `7c6c3455e386610dcd78cfd7b8c46789ddeff42d3f442591c36088c50a39abc9` using the sealed `A35-CONTENT-ROOT-v1` construction; and
- the exact existing target row `CD:C-B-V009-08:general-FS-corpus` / `BX10-V009-08-GENERAL-FS-CORPUS` in the generated Family-1 target manifest.

The resulting content-addressed binding record is:

`ce229f5a4a4c10fbd0a05be52e0affbefcd07dbbfbb6a028b9d05f5b85081d80`.

It carries the target-manifest pin, target-definition digest `dfeb42160821bf6b99a6348ee2ceadc3217317b6bd3e651a46989ae2c8a449e8`, corpus-definition/schema pins, member record, and declared root. Its state is `GENERATED_CONTENT_ADDRESSED_BINDING` and its admission is barred.

No corpus member was selected in this relay: membership was already fixed and sealed by relay 747. This relay only generated the requested integration binding from those pre-existing bytes.

## 6. AD3 — rows, batch reconciliation, and remaining owner

### 6.1 Tooling-layer row statuses

| Row | Status-record SHA-256 | New bounded status |
|---|---|---|
| `C-D-A35-02-QUASIFREE-CAR-LIFT` | `b25868258e45ed721d3ab83dcba1f49e7f6b197403f40065e17e163953458ee3` | `TOOLING_FAMILY2_PRESENT_COMPILE_READY_ADMISSION_BARRED` |
| `C-B-V010-11` | `245316f83f79aa5e711b251349b17141f0905fccec3f57893e4f1db371c07b00` | `TOOLING_FAMILY2_PRESENT_COMPONENTS_STATEABLE_ADMISSION_BARRED` |
| `C-B-V009-08` | `c8a0c4bc05d01bd69d8dd8b4a2e8b19efe402884fdfd1093eb26269ff0115a36` | `GRAPH_CORPUS_BOUND_TOOLING_FAMILY2_PRESENT_ADMISSION_BARRED` |
| `C-B-V008-05` | `d275d81bbe01456f697ef3c2dff36ceb0c34adb2793919f9e70daade7d764052` | `BOTH_TARGETS_TOOLING_FAMILY2_PRESENT_ADMISSION_BARRED` |

These are tooling-layer component states. They do not replace the evaluator's row predicates and are not row PASS verdicts.

### 6.2 Five-target batch lineage

The generated reconciliation reports 4 resolved / 1 remaining:

- both V008-05 partial targets resolve to the common complete instance and its family/ledger;
- the V009-08 graph partial resolves to the complete graph family/ledger;
- the V010-11 category partial resolves to the complete category family/ledger; and
- V008-10 remains partial at current instance SHA-256 `09116f010d3168bb4bd9d9875e1da61369b9e3ee949decd83b441400a7b994e8`.

The only remaining owners in this bounded ready-component/batch run are the V008-10 program-future objects already recorded by relay 728:

1. 11 stage realization artifacts;
2. 17 digest-parent bindings;
3. a sealed `parent_map_root` formula/value; and
4. the sealed mapping from the 11-node adjacency to the BX03 three-stage schema.

They were not synthesized. All other rows outside the four-ready-instance manifest remain outside this run; their Q-626 FG/EL ownership is unchanged.

## 7. Exercised controls and final audit

| Negative control | Observed refusal | Result |
|---|---|---|
| perturbed input digest | `HASH_MISMATCH` | PASS |
| required instance schema field removed | `SCHEMA_CONFORMANCE` | PASS |
| source span truncated by one byte | `SPAN_HASH_MISMATCH` | PASS |
| corpus declared root replaced | `CORPUS_ROOT` | PASS |
| duplicate family member ID | `DUPLICATE_MEMBER_ID` | PASS |
| expectation material digest changed | `EXPECTED_FAMILY_MISMATCH` | PASS |

The positive path ran over all four real sealed instances, not a synthetic dry run. A second invocation refused occupied output at the package boundary. Independent replay found 9/9 content-addressed component filenames correct, 19/19 inventory member hashes and lengths correct, 4/4 finite-family schemas valid, 4/4 ledger schemas valid, the binding/batch/row/run schemas valid, and no canonical-JSON or AST failure.

- F_PLDEC: the tool performs only byte hashing, schema checks, finite enumeration, ordering, and structural counts. It evaluates no physical quantity and compares no measured constant.
- Anti-tuning: family membership is the complete closed adapter projection of the sealed instance; expectations come from member bytes, not prior outcomes.
- Admission: every component, row record, batch record, and run record states `BARRED_STEP11_SUBGATE`.
- Chain: every generated record states `chain_invoked=false`; no evaluator chain was called.
- Verb audit: “produced,” “advanced,” and “bound” refer only to the nine generated Family-2 components and tooling-layer statuses. No evaluator PASS, proof authorization, physical result, board change, or admission is claimed.

TOOL = built (negative controls displayed)
PRODUCED = 9 (4 finite families / 4 expected ledgers / 1 corpus binding; 56 family members)
BINDING = generated (ce229f5a4a4c10fbd0a05be52e0affbefcd07dbbfbb6a028b9d05f5b85081d80)
ROWS_ADVANCED = C-D-A35-02-QUASIFREE-CAR-LIFT, C-B-V010-11, C-B-V009-08, C-B-V008-05 (tooling-layer statuses; admission barred)
ADMISSION = barred, stated
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
