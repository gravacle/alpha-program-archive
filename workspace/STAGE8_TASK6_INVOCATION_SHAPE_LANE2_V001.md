# STAGE 8 TASK 6 — BUILDER A INVOCATION-SHAPE CONFORMANCE

**Lane:** Codex Lane 2 / Builder A  
**Date:** 2026-08-07  
**Scope:** PASTE 691 only  
**Custody:** cleanroom write; registrar mirrors  

## 1. Preflight and authority

The assigned artifact and its `.seal.sha256` sidecar were absent from both the cleanroom and archive workspace before work began.

Builder B's sealed PASTE 690 contract was verified before implementation:

| Item | Value |
|---|---|
| Artifact | `STAGE8_TASK6_ROW_CONTRACT_DARIO_V001.md` |
| SHA-256 | `ce9ff15818307366ae93dd3082cb27398ff0705a07933864b76f1a88f5572925` |
| Sidecar verification | `OK` |
| Typed invocation inventory | exact `{opcode, result_name, args, instance_id}` |
| Linked instance grammar | `<symbol>@<source_sha256>:[start,end)` |

The four-key inventory is set-valued; Builder A's tight-canonical JSON encoder orders the serialized keys as `args`, `instance_id`, `opcode`, `result_name`.

## 2. Conformance repair

Builder A's stored evidence envelope was already lawful: its linked `r_dag` invocation had exactly the four contract fields and packed the linkage into `instance_id`. The defect was confined to `producer.make_check_row`, which expanded that object during output emission.

Before:

```json
{
  "args": {"authority": "PRINCIPAL_SINGLE_AUTHORITY", "graph": "<sealed DAG object>"},
  "instance_id": "stage_dependencies@13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd:[18898,19830)",
  "opcode": "DAG",
  "result_name": "r_dag",
  "source_sha256": "13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd",
  "span": [18898, 19830],
  "span_sha256": "47e7c32915bc756fb5f6be25c4fc6dec5c079c8837176dc62499e0f34f4c9d3b"
}
```

After:

```json
{
  "args": {"authority": "PRINCIPAL_SINGLE_AUTHORITY", "graph": "<sealed DAG object>"},
  "instance_id": "stage_dependencies@13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd:[18898,19830)",
  "opcode": "DAG",
  "result_name": "r_dag"
}
```

The producer now copies the sealed evidence invocation without adding fields. Before emission it reconstructs the expected packed identifier from the sealed citation's source digest and span and fail-closes with `BYTE_SPAN_LINKAGE_MISMATCH` if the stored identifier disagrees.

## 3. Nothing-lost display

Removing the three duplicate output fields removes no binding information:

| Binding fact | Surviving carrier | Verified value |
|---|---|---|
| Symbol | packed `instance_id` | `stage_dependencies` |
| Source identity | packed `instance_id` | `13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd` |
| Half-open span | packed `instance_id` | `[18898,19830)` |
| Exact span-byte identity | raw content-addressed payload and `r_ground` result | `47e7c32915bc756fb5f6be25c4fc6dec5c079c8837176dc62499e0f34f4c9d3b` |
| Consumed result payload | `observed_evidence_sha256s` and run-root materialization | `c4e99047921bf060e5a38409c48e5ed4e9614f2cd609151c2c32fa99d8a9765f` |

The content-addressed observed payload `c4e990…` contains:

```text
r_ground.result.normal_form = 47e7c32915bc756fb5f6be25c4fc6dec5c079c8837176dc62499e0f34f4c9d3b
r_dag.instance_id = stage_dependencies@13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd:[18898,19830)
```

Thus the packed identifier carries source plus span, and the digest-verified observed payload carries the exact span digest. The original 932-byte raw payload remains content-addressed by that same `47e7…` digest in the evidence package. No provenance byte or content identity was discarded.

## 4. Complete disclosed delta

A recursive comparison against the pre-edit package snapshot found exactly six changed files, zero additions, and zero removals under `evaluator_build_A/`.

| File | Disclosed change | Old SHA-256 | New SHA-256 |
|---|---|---|---|
| `producer.py` | emit the exact four-field invocation; verify packed citation linkage | `8ec03d1e8af12fa10fc402f52482cde867fbd703f76b293e14189c5db8e17eda` | `ed4170ec2042ab6ca7326155b77f3671387cce4469305ab840f9af52db10e9cb` |
| `tools/self_check.py` | require exact four-key output and assert span digest occurs in the content-addressed observed payload | `0b7ea216e693106162a7698e71132dde5d4181f29b2c8184684384c3309916d8` | `0a1a041ea5ecdbf6b0bd632bac4ca9aa97d2670ea56c5588fecc908298817d08` |
| `README.md` | document the typed shape and surviving carriers | `e36a06cac292e06d12ee903e9b029969aef30f1d72ab56d0f9787d4189d4cbbe` | `51f679578ebc4952cce4605db3544606754f5aea244296a0f6c9c82774b2b4f2` |
| `manifests/normal.json` | regenerated `producer.py` package-file row only | `9b6571e41079afe1b18eb8d63303481bb12478770c6e1ddfe1b2c758a804939f` | `1edf31d7317710044405e1173ea7098037f72e3881d71e784de1a314a5ffab6d` |
| `manifests/optimized.json` | regenerated `producer.py` package-file row only | `15a19b2561a7074f86efc58f00f93c5f2e5cba9525f733fccf8f763217c130ce` | `c831114f70d95d9ce1c1252304f0fa0407ca0ab4a2f00effed36414998116cdd` |
| `manifests/package_inventory.json` | regenerated rows for the five affected inventory members | `a63d86e37afda04429e9c01a9b9f9308bafcc6714e031d318cf836932e8ed0ab` | `c94604b944ffe691e9d8b523117603e3b1a5a474816097ef7550df9d80310f5c` |

The spec, check map, evidence manifest, evidence payloads, parent, local schemas, fixtures, and Builder B package are unchanged.

## 5. Static self-check

Regeneration:

```text
python3 evaluator_build_A/tools/materialize.py
{"checks": 66, "fixtures": 6, "gated": 10, "normal_sha256": "1edf31d7317710044405e1173ea7098037f72e3881d71e784de1a314a5ffab6d", "optimized_sha256": "c831114f70d95d9ce1c1252304f0fa0407ca0ab4a2f00effed36414998116cdd", "structural": 56, "subject_lineage_root": "43aee49596ee384f3d1bed8f7e92fcbf471909681927cc3726d53ef3b311beee"}
```

Static battery:

```text
python3 evaluator_build_A/tools/self_check.py
SELF_CHECK_OK
syntax=5
canonical_json=all
local_schemas=8
b_spec_repin=ALIGNED
evidence=1/56
v009_06_opcodes=COMPARE+DAG:PASS
v009_06_observed=c4e99047921bf060e5a38409c48e5ed4e9614f2cd609151c2c32fa99d8a9765f
invocation_fields=args,instance_id,opcode,result_name
byte_span_linkage=instance_id+observed_payload_digest
consumed_implies_materialized=PASS
descriptor_terminators_excluded=66/66
chain_invoked=false
```

The static check directly calls the producer's row constructor, rejects any key set other than the four sealed fields, checks the exact packed identifier, rehashes the materialized observed payload, and requires that payload to contain the span digest. It executes no subject-lineage chain.

## 6. PIN CHECK and gate audit

PRE-SEAL PIN CHECK:

- Builder B PASTE 690 contract: `ce9ff15818307366ae93dd3082cb27398ff0705a07933864b76f1a88f5572925` — verified.
- Governing spec V007: `d38d31719b64839744a98da5ee005fb50119f9a26b2b98b0e1a1de445b5d4973` — unchanged.
- Verdict schema: `5acf066a01eec3762de6364766424be57ce6a1a19a4a34f0e15edc081b0cc1a2` — unchanged.
- Normal manifest: `1edf31d7317710044405e1173ea7098037f72e3881d71e784de1a314a5ffab6d` — regenerated and verified.
- Optimized manifest: `c831114f70d95d9ce1c1252304f0fa0407ca0ab4a2f00effed36414998116cdd` — regenerated and verified.
- Package inventory: `c94604b944ffe691e9d8b523117603e3b1a5a474816097ef7550df9d80310f5c` — regenerated and verified.
- Assigned artifact path was rechecked immediately before write and was absent.

Gate state remains `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false`. No member binding, fixed-point execution, end test, numeric evaluation of a physical quantity, or comparison to a measured constant occurred. The verb audit found no claim beyond static conformance and carrier verification.

INVOCATION = 4-field, linkage packed (source+span in instance_id; span digest in content-addressed observed payload; nothing lost)
SELF_CHECK = passed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
