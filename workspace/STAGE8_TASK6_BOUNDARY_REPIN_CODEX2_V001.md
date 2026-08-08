# STAGE 8 TASK 6 — BUILDER A TWO-BOUNDARY RE-PIN

**Lane:** Codex 2 Lane / Builder A  
**Date:** 2026-08-08  
**Scope:** PASTE 705 only  
**Custody:** cleanroom write; registrar mirrors

## 1. Scope and preflight

The assigned artifact and its seal sidecar were absent from both the cleanroom and the checked archive workspace before this relay began. Builder B's V012 confirmation was verified at its sealed bytes:

| Sealed input | Verified SHA-256 | Result |
|---|---|---|
| `STAGE8_TASK6_V012_CONFIRM_DARIO_V001.md` | `2a2194211ff7e31187682b3d0a1d601b7ae736f522e21eaa7d00c4be8799dfe4` | sidecar and bytes agree |
| `evaluator_build_B/contracts/verifier_verdict.schema.json` | `1674aada096dba33c7026d70fb5df8705429224b2d3e81b2911e508851bfe9e8` | sidecar and bytes agree |
| `evaluator_build_B/rd22.verifier-manifest.v001.json` | `b43912455db38ebdebe603547d8a733b294b7a16b9f5999f1180da16a7d11961` | sidecar and bytes agree |

The current Builder B instance declares 14 root members and verifier root `2294dfe53a77a6069913822616bedffb4e16d062b1e968deeb727552f9f906db`. The relay did not change the specification, code, descriptor rows, register, plan, tracker, or git state, and it did not invoke the chain.

## 2. Generated re-pins

The existing `evaluator_build_A/tools/generate_pins.py` read Builder B's current sealed files and regenerated the closed pin manifest. Neither new digest was transcribed into source code.

| Pin kind | Superseded SHA-256 | Generated SHA-256 | Verified byte length |
|---|---|---|---:|
| `verifier_verdict_schema` | `757943f84d60be88d098cca3bfcde5f04ed3c85b02b807481ac0a2f959f9edb1` | `1674aada096dba33c7026d70fb5df8705429224b2d3e81b2911e508851bfe9e8` | 5154 |
| `verifier_manifest_v011` | `d4219a53f26aa19dad3b1119ee7f1cc7d4c9816b64b02b3f1c1efbea7a884d8a` | `b43912455db38ebdebe603547d8a733b294b7a16b9f5999f1180da16a7d11961` | 3513 |

Generation transcript:

```text
{"pins": 27, "sha256": "c450b90dc93dfd0ae041d939a34ffa60e9bc286a81a7ff5efd044b3474d2b101"}
```

## 3. Complete finite package delta

A recursive comparison against the registrar-mirrored pre-relay V012 package found exactly four changed files, all generated carriers. There were no additions or removals.

| File | Exact semantic delta | Old file SHA-256 | New file SHA-256 |
|---|---|---|---|
| `evaluator_build_A/manifests/pins.json` | two pin-row digest values | `8eac1df48a828f754ff1142498c4d80a8955fd06429ba86f3fb8a89a0533cb70` | `c450b90dc93dfd0ae041d939a34ffa60e9bc286a81a7ff5efd044b3474d2b101` |
| `evaluator_build_A/manifests/normal.json` | verdict-schema external-input pin plus regenerated `pins.json` package-row digest | `a386e8a98f47eff914345bff777df2ed5921cbf7fb6d8347a1455c6f6e08376a` | `b01a91c584615f2b38b847525901ffd02d61c1ab824b82a4c782e9744c8cc18e` |
| `evaluator_build_A/manifests/optimized.json` | verdict-schema external-input pin plus regenerated `pins.json` package-row digest | `be6c1f178c02fb90e968e5aae23de9fec8301734c22faad9de5a4fb8e2c9ab66` | `a3cee4fa8a58935814fb8df48a06341cb4a5843344dc6347d36b9a1ccd31dc29` |
| `evaluator_build_A/manifests/package_inventory.json` | regenerated hashes for `normal.json`, `optimized.json`, and `pins.json` | `fbcd75f25a935be75de928452b74436c411603277a4cf07f6b8aa89cd1fa15b9` | `9884f019a0883f0b40dc32445645e57f3479c6bfeebc9be9141eb5c898351cbc` |

The canonical-JSON comparison found 2, 2, 2, and 3 leaf changes respectively. Every leaf is one of the two generated boundary pins or a downstream inventory hash. No other field moved.

Invariants verified from bytes:

| Item | SHA-256 before and after |
|---|---|
| V012 specification | `382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504` |
| `parent.py` | `a09f333a133deb28f57f4dda5b78fd54f708c553b0c5ec1df98d3682c79100cc` |
| `producer.py` | `3c27890533eebe485f1f41688a7268d3898e6b1582ce933164113db28ba737a8` |
| 66-row `check_map.json` | `280004821c532def203ae81cec35bcac26bd3ab4bdd03752f5196aa7b9c23f3d` |

Thus the specification, parent, producer, and every descriptor row remain byte-identical.

## 4. Pin closure

Before regeneration, the two superseded full values occupied four live-reference occurrences: the verdict-schema value in `pins.json`, `normal.json`, and `optimized.json`, and the verifier-instance value in `pins.json`. After regeneration, fixed-string sweeps over `evaluator_build_A/` returned:

```text
757943f84d60be88d098cca3bfcde5f04ed3c85b02b807481ac0a2f959f9edb1  0
d4219a53f26aa19dad3b1119ee7f1cc7d4c9816b64b02b3f1c1efbea7a884d8a  0
```

The four replacement occurrences bind to the two independently rehashed Builder B inputs. There is no stale live package value.

## 5. Regeneration and static self-check

The derived manifests and package inventory were regenerated from the new pin manifest:

```text
{"checks": 66, "fixtures": 6, "gated": 10,
 "normal_sha256": "b01a91c584615f2b38b847525901ffd02d61c1ab824b82a4c782e9744c8cc18e",
 "optimized_sha256": "a3cee4fa8a58935814fb8df48a06341cb4a5843344dc6347d36b9a1ccd31dc29",
 "structural": 56,
 "subject_lineage_root": "4697b33a91077b0da005f78f7a7c8013b916b2998d1d99537fb3f5c6d57a7749"}
```

The static self-check passed. Material transcript fields:

```text
SELF_CHECK_OK
canonical_json=all
pin_manifest=27:c450b90dc93dfd0ae041d939a34ffa60e9bc286a81a7ff5efd044b3474d2b101
pin_source=generated
verifier_manifest=b43912455db38ebdebe603547d8a733b294b7a16b9f5999f1180da16a7d11961
verifier_root_members=14
verifier_root=2294dfe53a77a6069913822616bedffb4e16d062b1e968deeb727552f9f906db
verdict_schema=1674aada096dba33c7026d70fb5df8705429224b2d3e81b2911e508851bfe9e8
b_spec_repin=ALIGNED
inventory=45
checks=66
structural=56
gated=10
chain_invoked=false
```

## 6. Real-instance boundary dry-run

The parent validation path was executed directly against Builder B's actual current sealed instance and sidecar. Expected roots were independently derived from Builder A's current generated pins, evidence manifest, and subject manifest. The local closed verifier-manifest schema validated that same real instance. The parent also hash-verified and validated Builder B's actual verdict-schema definition using its supported keyword set. A temporary run root supplied only the expected output/receipt resolution base and was removed at exit; no child process ran.

```text
DRY_RUN_OK source=B_REAL_CURRENT_SEALED_INSTANCE
manifest_sha256=b43912455db38ebdebe603547d8a733b294b7a16b9f5999f1180da16a7d11961
manifest_schema=PASS fields=12
manifest_parent_validation=PASS members=14 root=2294dfe53a77a6069913822616bedffb4e16d062b1e968deeb727552f9f906db
verdict_schema_sha256=1674aada096dba33c7026d70fb5df8705429224b2d3e81b2911e508851bfe9e8
verdict_schema_definition=PASS supported=$comment,$schema,additionalProperties,const,enum,items,oneOf,pattern,properties,required,type
temporary_run_root_removed_on_exit=true
chain_invoked=false
```

## 7. PRE-SEAL PIN CHECK and scope audit

- Builder B schema and instance sidecars re-verified against their current bytes.
- Generated pin manifest rehashed to `c450b90dc93dfd0ae041d939a34ffa60e9bc286a81a7ff5efd044b3474d2b101`.
- Normal and optimized manifests rehashed to the values displayed above.
- Package inventory rehashed to `9884f019a0883f0b40dc32445645e57f3479c6bfeebc9be9141eb5c898351cbc`.
- Output-file census under `evaluator_build_A/outputs/` is zero.
- Assigned report path was checked absent immediately before creation.

Gate state remains `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false`. No member binding, fixed-point execution, end test, numeric evaluation of a physical quantity, or comparison to a measured constant occurred. The self verb audit found no claim outside this bounded generated re-pin and static validation scope.

REPINNED = 2 (schema, instance), generated
PIN_CLOSURE = 4 hits, all resolved (old values return zero)
DRY_RUN = executed against B's current instance
CODE_CHANGED = none
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
