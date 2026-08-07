# STAGE 8 TASK 6 — BUILDER A VERDICT-SCHEMA RE-PIN

**Lane:** Codex Lane 2 / Builder A  
**Date:** 2026-08-07  
**Scope:** PASTE 689 only  
**Custody:** cleanroom write; registrar mirrors  

## 1. Scope and stop checks

The assigned artifact name and its `.seal.sha256` sidecar were absent from the cleanroom and the archive workspace before work began. This relay changes no register, plan, tracker, or git state. It does not invoke the RD-22 chain.

The Builder B schema read for this relay is:

| Item | Value |
|---|---|
| Path | `evaluator_build_B/contracts/verifier_verdict.schema.json` |
| Byte length | `5154` |
| Verified current SHA-256 | `5acf066a01eec3762de6364766424be57ce6a1a19a4a34f0e15edc081b0cc1a2` |
| Former Builder A pin | `300a475ead3c17cd5b759ffcc3733418029030404af262632583fff077f2907f` |
| Current governing spec SHA-256 | `d38d31719b64839744a98da5ee005fb50119f9a26b2b98b0e1a1de445b5d4973` |
| Former embedded V005 spec SHA-256 | `f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b` |

## 2. Independent schema-delta verification

The current schema contains the V007 digest exactly once, at JSON path:

```text
["oneOf",0,"properties","spec_sha256","const"]
```

The fault-document branch contains no `spec_sha256` field. To test the claimed single-cause delta without copying Builder B's digest claim, I replaced the 64 bytes at that one full-verdict `const` location in memory:

```text
d38d31719b64839744a98da5ee005fb50119f9a26b2b98b0e1a1de445b5d4973
->
f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b
```

The reconstructed 5154-byte document hashes to:

```text
300a475ead3c17cd5b759ffcc3733418029030404af262632583fff077f2907f
```

That is byte-for-byte the archived Builder A expectation. The equal-length reverse substitution therefore accounts for the entire old-to-new schema movement: only the embedded full-verdict `spec_sha256.const` changed, from V005 to V007. No other schema byte moved.

## 3. Re-pin and disclosed delta

One semantic value was re-pinned from `300a475e…` to the independently verified `5acf066a…`. It has two source carriers and two generated child-manifest carriers. The status prose and finite package inventory were regenerated consistently.

| File | Disclosed change | Old SHA-256 | New SHA-256 |
|---|---|---|---|
| `evaluator_build_A/tools/materialize.py` | `VERDICT_SCHEMA_SHA` value only | `b5f8f8cda7dfbc6a7d5c8a22904102dbad22c0e92ec9d25c04c62aa3d9bc6fc8` | `9faa386b2badf0c32b90001f69e09d4bf8e9c1b83b22eb8ee352589d6d802db6` |
| `evaluator_build_A/tools/self_check.py` | `VERDICT_SCHEMA_SHA256` value only | `d912e628b1bfed1afe7e0ebac2ccbbc18c72fd30759290b5f43206c036c79921` | `0b7ea216e693106162a7698e71132dde5d4181f29b2c8184684384c3309916d8` |
| `evaluator_build_A/manifests/normal.json` | one `verifier_verdict_schema.sha256` value | `9accbf318a9a15e1a7df1c7d153b0435b4a6aaae6409bf55ff08efc20ca6f5f0` | `9b6571e41079afe1b18eb8d63303481bb12478770c6e1ddfe1b2c758a804939f` |
| `evaluator_build_A/manifests/optimized.json` | one `verifier_verdict_schema.sha256` value | `72f31d82c7e98e480f268db915a2ec9e7bf977d759f8dc2098e9221b1a061d2f` | `15a19b2561a7074f86efc58f00f93c5f2e5cba9525f733fccf8f763217c130ce` |
| `evaluator_build_A/README.md` | pending-re-pin notice replaced by the verified V007-aligned pin notice | `af28b5c39a91b0e70a985ac566373bf9c3c5f0174dd10a2c51d6c09ff7b2b73c` | `e36a06cac292e06d12ee903e9b029969aef30f1d72ab56d0f9787d4189d4cbbe` |
| `evaluator_build_A/manifests/package_inventory.json` | five affected inventory rows regenerated | `94f60f2add33835fbd36eca7c02e92f49bdbc961e1f1eae0a8e078855cb127c0` | `a63d86e37afda04429e9c01a9b9f9308bafcc6714e031d318cf836932e8ed0ab` |

The normal and optimized manifest rows retain the independently observed byte length `5154`. A recursive before/after package comparison found exactly these six changed files, with zero additions and zero removals. In particular, `parent.py`, `producer.py`, `check_map.json`, the evidence manifest, fixtures, and schemas under Builder A are unchanged.

The former digest has zero remaining occurrences under `evaluator_build_A/`. The new digest occurs in the two source carriers, both mode manifests, and the README disclosure.

## 4. Regeneration and static self-check

Regeneration command:

```text
python3 evaluator_build_A/tools/materialize.py
```

Transcript:

```text
{"checks": 66, "fixtures": 6, "gated": 10, "normal_sha256": "9b6571e41079afe1b18eb8d63303481bb12478770c6e1ddfe1b2c758a804939f", "optimized_sha256": "15a19b2561a7074f86efc58f00f93c5f2e5cba9525f733fccf8f763217c130ce", "structural": 56, "subject_lineage_root": "43aee49596ee384f3d1bed8f7e92fcbf471909681927cc3726d53ef3b311beee"}
```

Static self-check command:

```text
python3 evaluator_build_A/tools/self_check.py
```

Material results:

```text
SELF_CHECK_OK
syntax=5
canonical_json=all
local_schemas=8
verdict_schema=5acf066a01eec3762de6364766424be57ce6a1a19a4a34f0e15edc081b0cc1a2
b_spec_repin=ALIGNED
verdict_documents=fault:accepted,full_shape:checked
negatives=old13,full_extra,fault_extra,wrong_spec:rejected
inventory=34
checks=66
structural=56
gated=10
fixtures=6
chain_invoked=false
```

The self-check verified the sealed external schema digest before loading it, selected the V007 full-verdict branch, exercised both document kinds, and rejected the recorded negative cases. It performed syntax/schema/static checks only.

## 5. PIN CHECK and gate audit

PRE-SEAL PIN CHECK:

- Builder B verdict schema: `5acf066a01eec3762de6364766424be57ce6a1a19a4a34f0e15edc081b0cc1a2` — verified.
- Builder A V007 specification pin: `d38d31719b64839744a98da5ee005fb50119f9a26b2b98b0e1a1de445b5d4973` — unchanged and aligned with the schema `const`.
- Normal manifest: `9b6571e41079afe1b18eb8d63303481bb12478770c6e1ddfe1b2c758a804939f` — regenerated and verified.
- Optimized manifest: `15a19b2561a7074f86efc58f00f93c5f2e5cba9525f733fccf8f763217c130ce` — regenerated and verified.
- Package inventory: `a63d86e37afda04429e9c01a9b9f9308bafcc6714e031d318cf836932e8ed0ab` — regenerated and verified.
- Assigned artifact path was rechecked immediately before write and was absent.

Gate state remains: `alpha_computed=false`; `proof_authorized=false`; `kappa_record_computed=false`. No member binding, fixed-point execution, end test, numeric evaluation of a physical quantity, or comparison to a measured constant occurred. The self verb audit found no claim beyond this static re-pin and verification scope.

SCHEMA_PIN = re-verified and updated (only embedded spec_sha256.const: V005 -> V007)
SELF_CHECK = passed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
