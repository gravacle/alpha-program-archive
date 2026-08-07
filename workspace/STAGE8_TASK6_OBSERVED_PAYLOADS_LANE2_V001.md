# STAGE 8 TASK 6 — BUILDER A OBSERVED-PAYLOAD REPAIR

**Lane:** Codex Lane 2 / Builder A  
**Date:** 2026-08-07  
**Scope:** PASTE 692 only  
**Custody:** cleanroom write; registrar mirrors  

## 1. Preflight and finding

The assigned artifact and its `.seal.sha256` sidecar were absent from both the cleanroom and archive workspace before work began.

The run-029 finding is confirmed in the pre-repair producer: `execute_structural` serialized the opcode-result list, hashed that trace, and returned the trace digest as `observed_evidence_sha256s`. That made execution testimony look like an input and left the consumable `graph` argument without a digest-verified reproduction.

The repair adopts the governing distinction:

```text
observed evidence = bytes consumed by the check
execution trace   = testimony about what the check did
```

## 2. Observed evidence now is the payload set

`C-B-V009-06` now reports exactly two observed payloads, in this order:

| Role | Byte form | Bytes | SHA-256 |
|---|---|---:|---|
| Args-reproducing payload | tight-canonical serialization of the single-authority `graph` object | 594 | `a68204715597d161ece10ac731566e0b55bc3c4b237051b282e43adc1f73c736` |
| Byte-grounding payload | exact relocated raw member span | 932 | `47e7c32915bc756fb5f6be25c4fc6dec5c079c8837176dc62499e0f34f4c9d3b` |

The graph bytes are made from the object already present in the hash-pinned evidence invocation, before opcode execution, using the package's tight canonical encoder. The producer hashes those exact bytes, materializes them under their digest, and passes the same object to `DAG`. V007's single-authority identity therefore has one canonical graph object, not separately invented graph and required-parent objects.

The raw member is selected by the `left` and `right` digest references in the `COMPARE` invocation and by the evidence manifest's pinned input inventory. The producer copies those exact 932 bytes to the run-scoped content-addressed carrier and rehashes them. The filename retains the established `evidence/<digest>.json` contract spelling, but the carrier is format-neutral: this source span is intentionally a raw JSON member fragment, not a standalone JSON document. Content identity remains SHA-256-authoritative.

Observed result:

```json
[
  "a68204715597d161ece10ac731566e0b55bc3c4b237051b282e43adc1f73c736",
  "47e7c32915bc756fb5f6be25c4fc6dec5c079c8837176dc62499e0f34f4c9d3b"
]
```

The former trace digest is not in this list and is not materialized as evidence.

## 3. Consumable-argument coverage

The new static guard derives the payload demand from the invocation itself:

1. Every object-valued argument is serialized with the producer's tight canonical encoder; that digest must occur in `observed_evidence_sha256s`, and the materialized bytes must parse back to the exact argument object.
2. Every argument that is a 64-hex reference to an input-inventory member must occur in `observed_evidence_sha256s`, and the materialized bytes must rehash to that reference.
3. Duplicate references are deduplicated without losing coverage.

For this row, `graph` produces `a6820471…`; `left` and `right` both resolve to the one `47e7c329…` raw member. The spec-fixed `authority` string and empty `mask` are not payload-valued arguments under the sealed object/digest carrier rule. The computed consumable set and observed set are equal.

```text
CONSUMABLE_ARGS_REPRODUCED = PASS
graph bytes equal invocation.args.graph = PASS
raw member length = 932
raw member digest = 47e7c32915bc756fb5f6be25c4fc6dec5c079c8837176dc62499e0f34f4c9d3b
observed/materialized digest sets equal = PASS
```

## 4. Trace custody

The full opcode-result JSON list is no longer hashed, materialized, or counted as evidence. It is redundant with the deterministic invocation plus the child row's `status` and `reason`, so the list is dropped after the aggregate predicate is computed. Child custody remains receipt-side: the child output retains the invocation and compact result row, and the receipt's `output_sha256` binds those output bytes. No receipt schema field was invented and no evidence digest names execution testimony.

## 5. Complete disclosed delta

A recursive before/after comparison found exactly seven changed files under `evaluator_build_A/`, with zero additions and zero removals.

| File | Disclosed change | Old SHA-256 | New SHA-256 |
|---|---|---|---|
| `producer.py` | derive observed digests from consumed objects and inventory-backed digest references; exclude trace; allow raw digest-verified materialization | `ed4170ec2042ab6ca7326155b77f3671387cce4469305ab840f9af52db10e9cb` | `dc312240d3babae501eb1edf52e3d4b6510b266058b5e797492d99e4775f751b` |
| `parent.py` | verify run evidence as digest-authoritative bytes, permitting the sealed raw member fragment | `cd86374ca12fdb4822d789684de794a16eb0c790deee6069affe17099d887b75` | `571041c82c5143c2e34e8b2b3436b5f3c95a012397d9e3f19f91febd3c020712` |
| `tools/self_check.py` | assert the exact two-payload set, byte identity, materialization, trace exclusion, and consumable-argument coverage | `0a1a041ea5ecdbf6b0bd632bac4ca9aa97d2670ea56c5588fecc908298817d08` | `c7f71b73d357fa0749b4d726c24b4d0b77b7ad726a3d488ef61657d4c8b24f0b` |
| `README.md` | document payload/trace separation and receipt custody | `51f679578ebc4952cce4605db3544606754f5aea244296a0f6c9c82774b2b4f2` | `ab6913dd6246f8eab872c6ec9352e8753cd8144fad08483ba1e7c585f1e78a6d` |
| `manifests/normal.json` | regenerate parent/producer package-file rows | `1edf31d7317710044405e1173ea7098037f72e3881d71e784de1a314a5ffab6d` | `3258bc96b98561cf24414d71be984d5a8d99546c4d6c17276eb96af00838ecc7` |
| `manifests/optimized.json` | regenerate parent/producer package-file rows | `c831114f70d95d9ce1c1252304f0fa0407ca0ab4a2f00effed36414998116cdd` | `446e54e52db767a1e8a879672a4d4407764d5a23bb1f19da1419d7f7d3612e96` |
| `manifests/package_inventory.json` | regenerate rows for the six affected inventory members | `c94604b944ffe691e9d8b523117603e3b1a5a474816097ef7550df9d80310f5c` | `1d271eb7c51b952bb08326f66d2d233f1a978db57e3b313089e8a3ded8fdf9d0` |

The evidence manifest, its declared root, all evidence-package files, check map, spec, fixture files, schemas, and Builder B package are unchanged.

## 6. Static self-check

Regeneration:

```text
python3 evaluator_build_A/tools/materialize.py
{"checks": 66, "fixtures": 6, "gated": 10, "normal_sha256": "3258bc96b98561cf24414d71be984d5a8d99546c4d6c17276eb96af00838ecc7", "optimized_sha256": "446e54e52db767a1e8a879672a4d4407764d5a23bb1f19da1419d7f7d3612e96", "structural": 56, "subject_lineage_root": "43aee49596ee384f3d1bed8f7e92fcbf471909681927cc3726d53ef3b311beee"}
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
v009_06_observed=a68204715597d161ece10ac731566e0b55bc3c4b237051b282e43adc1f73c736,47e7c32915bc756fb5f6be25c4fc6dec5c079c8837176dc62499e0f34f4c9d3b
observed_payloads=graph+raw_span
consumable_args_reproduced=PASS
trace=evidence_excluded;receipt_output_digest_custody
invocation_fields=args,instance_id,opcode,result_name
consumed_implies_materialized=PASS
descriptor_terminators_excluded=66/66
chain_invoked=false
```

This is a static function-level battery. It does not launch either child over the subject lineage and does not invoke Builder B.

## 7. PIN CHECK and gate audit

PRE-SEAL PIN CHECK:

- Governing spec V007: `d38d31719b64839744a98da5ee005fb50119f9a26b2b98b0e1a1de445b5d4973` — unchanged.
- Check map: `4fe53c2d1b22429318fd960238344110d9c36e530e52350df877669276e9a751` — unchanged.
- Evidence manifest: `64e16a98753103215116bbd86169fee5c07ac621372f83a573047aa63995d48d` — unchanged.
- Verdict schema: `5acf066a01eec3762de6364766424be57ce6a1a19a4a34f0e15edc081b0cc1a2` — unchanged.
- Normal manifest: `3258bc96b98561cf24414d71be984d5a8d99546c4d6c17276eb96af00838ecc7` — regenerated and verified.
- Optimized manifest: `446e54e52db767a1e8a879672a4d4407764d5a23bb1f19da1419d7f7d3612e96` — regenerated and verified.
- Package inventory: `1d271eb7c51b952bb08326f66d2d233f1a978db57e3b313089e8a3ded8fdf9d0` — regenerated and verified.
- Assigned artifact path was rechecked immediately before write and was absent.

Gate state remains `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false`. No member binding, fixed-point execution, end test, numeric evaluation of a physical quantity, or comparison to a measured constant occurred. The verb audit found no claim beyond the static payload-carrier repair and its tests.

OBSERVED = payload set (args-reproducing + grounding)
TRACE = receipt-side (compact output row bound by receipt output_sha256; redundant full trace dropped)
SELF_CHECK = passed (consumable_args_reproduced=PASS)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
