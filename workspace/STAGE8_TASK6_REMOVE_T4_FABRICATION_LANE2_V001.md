# STAGE 8 TASK 6 — BUILDER A T4 FABRICATION REMOVAL

**Lane:** Codex Lane 2 / Builder A  
**Date:** 2026-08-07  
**Disposition:** COMPLETE  
**Scope:** parent, generated terminal-ledger schema, static self-check, and their content-addressed manifests only  
**Authority:** implementation under RD-22; no seal or proof authority claimed

## 1. Adjudicated defect and correction

The pre-verifier producer ledger formerly carried this five-label map:

```text
{T0: t0, T1: t1, T2: t2, T3: t3, T4: t3}
```

That last association did not report a T4 observation. It copied T3 into a label whose sampling time had not occurred. The association is removed, not renamed or annotated.

The two lawful carriers are now disjoint by construction:

| Carrier | Exact labels | Construction time | T4 source |
|---|---|---|---|
| verifier-input producer ledger | T0, T1, T2, T3 | before verifier launch | no T4 key |
| terminal ledger | T0, T1, T2, T3, T4 | after the verifier process returns | `t4 = trust_snapshot(runtime)` |

The parent builds `producer_trust_snapshots` with exactly T0–T3. Immediately before that map is handed to `verdict_ledger`, the parent has the explicit fail-closed guard:

```python
if "T4" in producer_trust_snapshots:
    fail("T4_BEFORE_SAMPLE", sorted(producer_trust_snapshots))
```

The call to `run_verifier_process` still precedes the true T4 sample. The terminal ledger still receives the map `{T0: t0, T1: t1, T2: t2, T3: t3, T4: t4}`. No other T4 constructor exists in `parent.py`.

## 2. Schema treatment

Both the producer ledger sent to the verifier and the later terminal ledger use `rd22.terminal-ledger.v001`. Its `trust_snapshots` object is therefore closed over the five lawful label names, requires T0–T3, and permits T4 only as the post-verifier extension. The runtime constructions and the static self-check impose the carrier-specific exact sets:

```text
producer ledger: exactly {T0,T1,T2,T3}
terminal ledger: exactly {T0,T1,T2,T3,T4}
```

This does not use an optional schema property to manufacture a value. The producer object omits T4; the terminal object supplies the independently sampled T4.

## 3. Self-check guard and coverage

The static self-check now has three independent defenses:

1. Its synthetic producer map is T0–T3 and immediately fails `T4_BEFORE_SAMPLE` if T4 is present.
2. It requires the synthetic producer ledger to have exactly T0–T3 and the synthetic terminal ledger to have exactly T0–T4.
3. It inspects the parent source, requires the T0–T3 constructor and guard, requires the post-verifier T0–T4 terminal constructor, and fails if the former fabricated literal `"T4": t3` remains anywhere.

The new guard line reported by the transcript is:

```text
t4_before_sample_guard=PASS
```

## 4. Complete disclosed delta

The comparison base was the registrar-mirrored Builder A package accompanying sealed artifact `STAGE8_TASK6_AUTH_SCOPE_LANE2_V001.md`, SHA-256 `fcdda5e5fcd0dca17c7019b74b32cff5e43b7a893bf63ce2f5e6da0e115dbd69`. A file-by-file byte comparison found exactly the seven rows below and no others.

Diff conventions: unified-diff hunks; text insertions/deletions count newline-delimited lines; each regenerated canonical JSON document has one physical line, so a content change in such a document counts as one deletion plus one insertion. Byte lengths and SHA-256 digests are authoritative for canonical JSON deltas.

| File | Base bytes / SHA-256 | Final bytes / SHA-256 | Diff | Disclosed change |
|---|---|---|---|---|
| `parent.py` | 56,674 / `776255fac3f533017e01a57931f8097d5eab033bc3ac5676df0847e1d6fb28bb` | 56,828 / `5e94efc64d38977bcfa030305c7c7ac7f07c85a45e4413eb27861c6561c94638` | 1 hunk; +4/-1 | replace copied T3-as-T4 map with exact T0–T3 map and `T4_BEFORE_SAMPLE` guard |
| `tools/materialize.py` | 32,196 / `14c184ba422df2066c651d6c7e1d6a404752cccfa2a4302fd2930b1e903c7053` | 32,330 / `dc2cbbef651109f51f4a0cb8d9edeaacb58b34339b646ed759202d42088839c1` | 1 hunk; +6/-1 | generate the closed T0–T4 property set with T0–T3 required |
| `tools/self_check.py` | 37,644 / `1f3b08fdf4662f3bb567fe1a9e511766aba8daece253ae17727d3b9efc10a51e` | 38,530 / `737d15f75909151337191513b08567a3c4fd082990c06ae4306af7b6be987da1` | 7 hunks; +19/-9 | separate producer/terminal maps; add exact-set, sequence, source-literal, and pre-sample guards; correct transcript |
| `schemas/terminal-ledger.schema.json` | 4,687 / `960bee5560b314297a5ae17606f95bcd5b7943f11803ddf78984d55d1ec9acd6` | 4,682 / `af500aab2ec6037887286a65283272e2df7499f702951cf6baa19e326652912c` | 1 hunk; +1/-1 | regenerated nested `trust_snapshots` requirement |
| `manifests/normal.json` | 8,850 / `70123e515cadd09c21db5b4e0e24554ae089a9bb9458082f37fffdeceed74ae1` | 8,850 / `53b57459b27cfe3427af4389ebb532df2626cb05778ffd0be2c4c5b79fdd2aeb` | 1 hunk; +1/-1 | refresh parent and schema inventory pins |
| `manifests/optimized.json` | 8,859 / `68de7be02a0fe6bff1dd35b417b53a2f779f19856e2c63972b32a41ece98c875` | 8,859 / `f0adc15abb751430fec3969df01a4f25704eaaf6c28a8abe15f28991c2516ef5` | 1 hunk; +1/-1 | refresh parent and schema inventory pins |
| `manifests/package_inventory.json` | 5,512 / `4675570ebc1758484ccf285f374610eae6626e3e09dceb31118bc60b7098ad06` | 5,512 / `de3b0c616fcea090f7917630658d794b87d94b8464fb2ae7d95ce86fd6190490` | 1 hunk; +1/-1 | refresh all changed package-file pins and normal/optimized manifest pins |

Total: 13 hunks, 33 inserted physical lines, 15 deleted physical lines under the declared convention. All other package files are byte-identical to the registrar mirror.

## 5. Static self-check transcript

Only the authorized materializer and static self-check were run, both under `/usr/bin/python3 -I -S -B`. No parent, producer, verifier, fixture, check executor, subject lineage, or full chain was invoked.

First pass:

```text
MATERIALIZE_OK checks=66 fixtures=6 gated=10 structural=56 normal_sha256=53b57459b27cfe3427af4389ebb532df2626cb05778ffd0be2c4c5b79fdd2aeb optimized_sha256=f0adc15abb751430fec3969df01a4f25704eaaf6c28a8abe15f28991c2516ef5 subject_lineage_root=d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688
SELF_CHECK_OK syntax=5 canonical_json=all schemas=9 inventory=31 evidence_payloads=10 evidence=0/56 absent=56 fixture_obs=0/3 checks=66 structural=56 gated=10 fixtures=6 producer_fields=13 receipt_fields=16 fixture_fields=16 child_fields=14 verifier_manifest_fields=11 authorization_fields=artifact_sha256,scope authorization_digest=ff84c4a8ba5c7f8eabfbcc587475d3a5050c21d758a2788c5b9e28b7ee022340 authorization_scope=equals_ledger_scope authorization_forward=producer,terminal,verifier_receiver t_labels=producer:T0,T1,T2,T3(no_T4);terminal:T0,T1,T2,T3,T4(actual_T4) t4_before_sample_guard=PASS trust_root=7a80a5d52fd35701d8da02239178f63ef80e4f80ce8557636db99a326cf4c73c trust_sites=10 trust_agreement=definition,manifests,main_receiver,T0_T3,child_rows,producer_runtime,producer_T0_T3_value_only,verifier_receiver,terminal_runtime,terminal_T0_T4 exits=0/1/2 chain_invoked=false
```

Idempotence pass: the same materializer and self-check returned success; the three top-level generated pins remained byte-identical before and after the second pass:

```text
normal.json             53b57459b27cfe3427af4389ebb532df2626cb05778ffd0be2c4c5b79fdd2aeb
optimized.json          f0adc15abb751430fec3969df01a4f25704eaaf6c28a8abe15f28991c2516ef5
package_inventory.json  de3b0c616fcea090f7917630658d794b87d94b8464fb2ae7d95ce86fd6190490
```

The package inventory validated 31 files. All `outputs/` and package `pycache/` directories remained empty.

## 6. PIN CHECK, gates, and verb audit

Pre-seal checks:

- The output artifact name and its seal-sidecar name were absent in both cleanroom and archive workspace before creation.
- The base hashes in the delta table were recomputed from the registrar mirror before the files were read for comparison.
- The final hashes were recomputed from cleanroom bytes after the idempotence pass and agree with `normal.json`, `optimized.json`, and `package_inventory.json` wherever each file is carried.
- The materializer and self-check both returned exit 0; the self-check validated syntax, nine schemas, canonical JSON, the exact package inventory, the T-label carriers, and the no-output condition.
- This artifact is to be hashed only after its final byte is written; its `.seal.sha256` sidecar records that post-write digest. The registrar, not Builder A, mirrors it.

Gate audit: `alpha_computed = false`; `proof_authorized = false`; `kappa_record_computed = false`. No member binding, fixed-point execution, end test, physical-quantity evaluation, or comparison to a measured constant occurred.

Verb audit under the verdict-line scope rule: CLEAN. Statements about execution are confined to the static materializer/self-check transcript and explicit negative statements about the chain and barred operations. No authorization or scientific verdict is claimed.

INPUT_RECORD = T0-T3 (no T4 key)
TERMINAL = T0-T4 at true sample time
SELF_CHECK = passed (+the new guard line)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
