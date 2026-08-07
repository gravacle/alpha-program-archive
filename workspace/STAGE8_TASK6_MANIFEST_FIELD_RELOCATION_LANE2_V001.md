# STAGE 8 / TASK 6 / BUILD A — MANIFEST-FIELD RELOCATION — LANE 2 V001

Lane: Lane 2, Builder A  
Relay: PASTE 664  
Context: run 011 `PRODUCER_SEMANTIC_DRIFT` disposition  
Scope: producer-output compared surface, receipt manifest carrier, parent launch/receipt binding, output schema, recursive hashes, and mode-variance audit  
Authority claimed: none

```text
SPEC_V005_SHA256 = f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b
INTEGRATION_ADDENDUM_SHA256 = d17c5e79986bea431dec0b572019096f9c059bcc43876fda9134abc96ce0f260
PRIOR_PARENT_SHA256 = 10ef12f2449d8694692c81492a208dfa179800722249d7010e536f995b3285bc
FINAL_PARENT_SHA256 = 7b95464a7141f29d8c5c8b3be9a785f1e49e1649f98803502c55b31a41cef717
PRIOR_PRODUCER_SHA256 = 14a679f75a15b96f93e70685ff422fbc74465038f8ae68b95ca3df16b8d76b45
FINAL_PRODUCER_SHA256 = d565221e701cadea3d75dc21003b322d097decb2f1913a868901064bc81cde9e
CHAIN_INVOKED = false
```

## 1. Preflight and run-011 finding

| Check | Result |
|---|---|
| Output collision | This artifact and sidecar were absent in the cleanroom and archive workspace immediately before creation. |
| Governing pins | V005 is `f8d1a7dc…`; the integration addendum is `d17c5e79…`; both exact. |
| Prior Builder A state | The sealed PASTE 663 artifact is `cc7cda3d…`; the archive package independently matches its parent, producer, schemas, tools, and manifest hashes. |
| Run-011 evidence | Both producer outputs and receipts exist. The registrar's claim was independently reproduced from those bytes. |
| Chain state | No producer, verifier, check executor, fixture, or full chain was invoked in this relay. |

The raw run-011 top-level differences were exactly:

```text
manifest_sha256
monotonic_duration
process_id
python_optimize
```

The latter three are the sealed mask and remain unchanged. After applying that exact mask, the sole remaining difference was `manifest_sha256`:

```text
normal    = 839ef774114d9431ba3df47b812c1ea6649c06db1539e989b5b49640888e792b
optimized = d75b5c90427f3922eefb7a37d48cd274e9ec2156402b36fb6ab06ef593ef0101
```

Those are correctly different because they address different launch manifests. The same two values were already present in their respective child receipts. Thus the defect was duplicate placement on the semantically compared output surface, not missing custody.

## 2. T1 — relocation to the existing receipt carrier

### 2.1 Producer

`manifest_sha256` was removed from the producer's output object. It remains a mandatory field in the producer receipt:

```text
receipt.manifest_sha256 = args.manifest_sha256
```

The receipt schema remains the same closed 16-field contract and retains `manifest_sha256` in both `properties` and `required`. Its bytes and digest are unchanged:

```text
child-receipt.schema.json = 5289d078a687fdfe8a82c1d001ccb0f13105eabccf3f2f87ea57298f640fb0a3
```

This is a de-duplication into the already lawful carrier; no fresh identity field was invented.

### 2.2 Parent custody

The parent now admits a closed 13-field producer output with no `manifest_sha256`. Per-child identity remains checked before R8 in `classify_receipt`:

```text
receipt.manifest_sha256 == expected manifest digest from the parent's launch record
```

`child_record` repeats that exact launch/receipt equality gate and then carries the receipt's verified value into the existing 14-field terminal child row. A static mismatch control raised `CHILD_RECORD_MANIFEST`. Therefore the terminal ledger still records each child's manifest identity, but that per-child identity never enters `compare_producers`.

### 2.3 Schema

`producer-output.schema.json` is still closed and exact, now with 13 fields. `manifest_sha256` was deleted from both its `properties` and `required` arrays. The schema/materializer and the parent's handwritten exact-key parser agree on the same 13-field inventory.

No semantic mask field was added or removed:

```text
MASK_FIELDS = {process_id, monotonic_duration, python_optimize}
```

## 3. T2 — audit of every output field

### 3.1 Per-child-by-construction census

| Field or class | Varies by construction? | Final treatment |
|---|---|---|
| `manifest_sha256` | Yes: normal and optimized manifests are distinct content-addressed launch records. | Removed from output; mandatory in receipt; verified against parent launch record; carried in terminal child row. |
| `python_optimize` | Yes: mode declaration is 0 versus 1. | Remains one of the three sealed mask fields; not part of the compared surface. |
| `process_id` | Per process. | Remains one of the three sealed mask fields; not part of the compared surface. |
| `monotonic_duration` | Per process. | Remains one of the three sealed mask fields; not part of the compared surface. |
| `mode`, `optimization`, `writable_paths` | Launch-manifest fields that differ by mode. | Never present in producer output. |
| All remaining output fields | No mode-specific construction found. | Remain on the compared surface. |

### 3.2 Mode-invariant compared surface

After the sealed mask, the compared surface contains only:

```text
authority_firewall
check_map_sha256
checks
fixture_manifest_sha256
fixtures
schema
scope
spec_sha256
subject_lineage_root
summary
```

Each is either a common manifest/input pin, a fixed schema/scope/firewall fact, or a deterministic product of the same check map, evidence manifest, and fixture manifest. The parent already requires those common roots to agree before child launch.

An in-memory static R8 control removed only the misplaced field from copies of the existing run-011 outputs and then called the final `compare_producers`. Result:

```text
R8_STATIC_COMPARISON = PASS
checks = 66/66 equal
fixtures = 6/6 equal
summary = equal
unmasked differences = 0
```

No other field was relocated. No mask widening occurred.

## 4. Disclosed finite delta — eight files

The archive workspace supplied the exact pre-relay package. A recursive hash comparison found no added or removed package file and exactly eight changed files.

| File | Before bytes / SHA-256 | After bytes / SHA-256 | Disclosed change |
|---|---|---|---|
| `evaluator_build_A/producer.py` | 41,324 / `14a679f75a15b96f93e70685ff422fbc74465038f8ae68b95ca3df16b8d76b45` | 41,275 / `d565221e701cadea3d75dc21003b322d097decb2f1913a868901064bc81cde9e` | Delete the single `manifest_sha256` producer-output entry; retain its existing receipt entry. One deletion. |
| `evaluator_build_A/parent.py` | 53,690 / `10ef12f2449d8694692c81492a208dfa179800722249d7010e536f995b3285bc` | 53,849 / `7b95464a7141f29d8c5c8b3be9a785f1e49e1649f98803502c55b31a41cef717` | Remove `manifest_sha256` from the output parser; require launch/receipt equality again in `child_record`; source the terminal child-row manifest field from the verified receipt. Three insertions, two deletions. |
| `evaluator_build_A/schemas/producer-output.schema.json` | 2,424 / `07cb427cf5f7d337b41d68e9b657f18059ab7bb22522107e65a93ffaec0331a6` | 2,345 / `409a8459d50ef8afd77f27be445c9ea1b75ae30e4f7287f601d774c7ffcbd9fd` | Remove `manifest_sha256` from the closed output properties and required inventory; 14 fields become 13. |
| `evaluator_build_A/tools/materialize.py` | 31,300 / `94f63527cdbc5b2ad8235806bc4ee23495d89c78efddf16fcbf95268909507e7` | 31,254 / `1ab3b44f229afc4eafc43e6d794532783a652fc8d9951dd75ca813c2164cc997` | Generate the corrected 13-field producer-output schema. Two insertions, two deletions. |
| `evaluator_build_A/tools/self_check.py` | 25,159 / `05596a4e29d6828c72793667400058c05d15f38e6294caa99eaeeefb82aa1951` | 26,816 / `cedf2c8b82957be18415f3f15d3feac656117339ef552fab15973578f9aea51f` | Enforce 13 output fields, 16 receipt fields, absence of unmasked per-child fields, exact unchanged mask, no output occurrence, and exactly one producer receipt occurrence. Transcript now displays both field counts. |
| `evaluator_build_A/manifests/normal.json` | 9,172 / `839ef774114d9431ba3df47b812c1ea6649c06db1539e989b5b49640888e792b` | 9,172 / `7ef05faa9bcfcbb9fec6c31ae8e1a368317341059594ace0057c3ebddad8b6ea` | Update only the parent, producer, and producer-output-schema package rows. |
| `evaluator_build_A/manifests/optimized.json` | 9,181 / `d75b5c90427f3922eefb7a37d48cd274e9ec2156402b36fb6ab06ef593ef0101` | 9,181 / `724f73b4c38842e8b3e5afe5e4e393a7717b7ebd5c380f2b7670b3ff9ed1bdcc` | Same three package-row updates for optimized mode. |
| `evaluator_build_A/manifests/package_inventory.json` | 5,512 / `fcec4b82cfd29533cdabc18962f6f8d0b3fcf344afaee955cbeadfb55fadbeaf` | 5,512 / `ec60dfeb4f9a8d850e06dd92e71f1de179cc174682c8af489fc43c8c682a2f33` | Update the parent, producer, producer schema, materializer, self-check, and two child-manifest rows. |

No receipt schema, terminal schema, check map, fixture manifest, evidence manifest/payload, subject-lineage manifest, other schema, Builder B, or README byte changed.

## 5. Static self-check transcript

Only source parsing, schema validation, in-memory comparison of existing run-011 metadata, launch/receipt binding controls, deterministic materialization, and package rehashing ran.

```text
$ /usr/bin/python3 -I -S -B - '<source parse>'
AST_OK evaluator_build_A/parent.py
AST_OK evaluator_build_A/producer.py
AST_OK evaluator_build_A/tools/materialize.py
AST_OK evaluator_build_A/tools/self_check.py
assert_nodes = 0 in all four

$ /usr/bin/python3 -I -S -B - '<run-011 copied-metadata audit>'
RUN011_AUDIT raw_top_differences=manifest_sha256,monotonic_duration,process_id,python_optimize
COMPARED_SURFACE_CONTROL=PASS removed=manifest_sha256 mask=monotonic_duration,process_id,python_optimize unmasked_differences=0
RECEIPT_BINDING_CONTROL=PASS receipt_to_child_row=true mismatch=CHILD_RECORD_MANIFEST
R8_STATIC_COMPARISON=PASS checks=66 fixtures=6 summaries_equal=True

$ /usr/bin/python3 -I -S -B - '<schema controls>'
SCHEMA_CONTROLS=PASS output_fields=13 receipt_fields=16 normal=PASS optimized=PASS

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/materialize.py
{"checks": 66, "fixtures": 6, "gated": 10, "normal_sha256": "7ef05faa9bcfcbb9fec6c31ae8e1a368317341059594ace0057c3ebddad8b6ea", "optimized_sha256": "724f73b4c38842e8b3e5afe5e4e393a7717b7ebd5c380f2b7670b3ff9ed1bdcc", "structural": 56, "subject_lineage_root": "d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688"}

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/self_check.py
SELF_CHECK_OK syntax=5 canonical_json=all schemas=9 inventory=31 evidence_payloads=10 evidence=0/56 absent=56 fixture_obs=0/3 checks=66 structural=56 gated=10 fixtures=6 producer_fields=13 receipt_fields=16 fixture_fields=16 child_fields=14 verifier_manifest_fields=11 exits=0/1/2 chain_invoked=false
```

## 6. PIN CHECK, fences, and verb audit

### 6.1 PRE-SEAL PIN CHECK

| Pin or invariant | Final result |
|---|---|
| V005 / addendum | `f8d1a7dc…` / `d17c5e79…`, exact and unchanged. |
| Prior state | Sealed PASTE 663 artifact `cc7cda3d…`; archive package matches every declared before-hash. |
| Run-011 diagnosis | Exactly one non-masked difference: `manifest_sha256`; all check, fixture, and summary content agrees. |
| Mask | Exactly `monotonic_duration`, `process_id`, `python_optimize`; unchanged in parent and producer. |
| Output schema | Closed 13-field schema `409a8459…`; no `manifest_sha256`. |
| Receipt schema | Closed 16-field schema `5289d078…`; mandatory `manifest_sha256`; byte-unchanged. |
| Receipt custody | Parent classification and child-row construction both compare receipt identity with the parent's launch record. |
| Parent / producer | `7b95464a…` / `d565221e…`; syntax clean; zero `assert` nodes. |
| Runtime manifests | `7ef05faa…` / `724f73b4…`; 25/25 package rows rehashed in both. |
| Package inventory | 31/31 rows rehashed; digest `ec60dfeb…`. |
| Delta census | No package file added/removed; exactly the eight disclosed files changed. |
| Output collision | Artifact and sidecar absent in both required locations immediately before creation. |
| Chain products | Builder A `outputs/` and all package pycache directories contain no files. |

### 6.2 Fences

The static R8 control used only in-memory copies of existing run-011 JSON and did not invoke either producer, the verifier, or a check executor. No member was bound; no fixed point or end test ran; no physical quantity was evaluated; and no measured constant was read or compared. `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false`.

No fence blocked a structural schema/custody result; no MACHINERY-APPEAL is required.

### 6.3 Self verb audit under the verdict-line scope rule

| Verb | Scoped meaning |
|---|---|
| `relocate` / `remove` | Delete the duplicate output occurrence while retaining the pre-existing mandatory receipt carrier. |
| `compare` / `PASS` | Static R8 function call over copied existing JSON or displayed syntax/schema/hash check only; no chain verdict. |
| `verify` / `bind` | Compare the receipt manifest digest with the exact parent launch record before carrying it into the terminal child row. |
| `sealed` | Applies only after adjacent sidecar creation and grants no chain, result, authorization, or proof authority. |

RELOCATED = manifest_sha256 -> receipt (+others: none; receipt carrier remains mandatory)
COMPARED_SURFACE = mode-invariant by construction
SELF_CHECK = passed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN / (+relocate/remove/compare/verify/bind scopes; sealed mask unchanged; no chain result, authorization, or proof claimed)
