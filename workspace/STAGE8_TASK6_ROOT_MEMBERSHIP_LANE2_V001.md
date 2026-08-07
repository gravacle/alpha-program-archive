# STAGE 8 TASK 6 — BUILDER A VERIFIER-ROOT MEMBERSHIP CORRECTION

**Lane:** Codex Lane 2 / Builder A  
**Date:** 2026-08-07  
**Disposition:** COMPLETE  
**Scope:** Builder A verifier-root membership, schema/root identity binding, static self-check, and regenerated package pins  
**Authority:** RD-22 implementation; no scientific, proof, or seal authority claimed

## 1. Sealed source and controlling list

The controlling cleanroom source is `STAGE8_TASK6_SCHEMA_IN_ROOT_DARIO_V001.md`, SHA-256:

```text
de9139768c68371310e48245568472273fc19da96c48004ef7819ee6b0dbab79
```

Its seal sidecar has SHA-256 `0a12e26da7cc772c12652b3f01106cb80c2690caf65eabca1acad7938c363409` and verifies. The artifact is byte-identical in the cleanroom and registrar mirror. Builder B's code was not read for this repair.

The sealed artifact declares the exact sorted package-relative membership:

```text
contracts/verifier_verdict.schema.json
run_verifier.py
verifier/__init__.py
verifier/canonical_json.py
verifier/child_manifest.py
verifier/comparison.py
verifier/contracts.py
verifier/hashing.py
verifier/replay.py
verifier/runtime_state.py
verifier/spec_census.py
verifier/verify.py
```

Count: 12. The sealed root is:

```text
dba5377d5ca1e7eebf2932da10e043e96c33f642cf06c8dd81cf26dff3bd3ac0
```

## 2. Builder A correction

The previous Builder A implementation inferred one entry script plus every top-level `verifier/*.py` file. That produced eleven members and omitted the verdict schema added to Builder B's root at 676.

Builder A now carries the sealed twelve-name list as `VERIFIER_ROOT_TRANSCRIBED_MEMBERS`. Before hashing, the parent requires:

- exactly 12 names;
- bytewise sorted order;
- every declared member to resolve safely inside the verifier package;
- every member to exist as a file;
- each member's digest to be computed from its current bytes;
- the root to equal `SHA256(concat(member_sha256_hex in declared sorted order))`.

The digest algorithm is unchanged. Only the member set changed from eleven to the sealed twelve.

The root allowlist now includes `contracts/verifier_verdict.schema.json`. After validating the verifier manifest, the parent additionally requires that this root-covered schema member have the same realpath-normalized identity and SHA-256 as the R0-verified external input used by `verifier_stdout`. A separately pinned schema copy cannot satisfy this check merely by having a similar name.

## 3. Structural note for contract V002 — recorded, not settled

**OPEN CONTRACT-V002 ITEM:** verifier-root membership remains transcribed in Builder A. Builder B owns a membership definition, and Builder A has independently copied the same names so it can recompute the root. Any future membership change can make the two definitions drift again even when both implementations are internally correct.

The durable closing-docs repair is for the verifier-manifest instance to carry the root member list explicitly, so Builder A validates and hashes instance-declared membership rather than a compiled copy. That item must be considered together with Builder B's name-binding observation recorded at 667. This relay does not amend the manifest contract, choose a V002 row shape, or settle that name-binding question.

Current status:

```text
V001 runtime repair: exact sealed twelve-name transcription installed
V002 design item: membership-in-instance + 667 name-binding observation
V002 implemented here: no
```

This note is also adjacent to the Builder A membership constant and is enforced by the static source audit so it cannot disappear silently while the transcription remains.

## 4. Static self-check

The static check does not read Builder B's code. It performs these bounded checks:

1. verifies the sealed 676 artifact at `de913976…`;
2. extracts evidence that all twelve names and `dba5377d…` occur in that sealed source;
3. compares Builder A's membership tuple byte-for-byte with the twelve-name expected tuple;
4. requires length 12 and sorted order;
5. requires the parent to iterate the explicit tuple and forbids the former directory-inference loop;
6. requires the verdict-schema/root binding receiver;
7. requires the contract-V002 note beside the transcription;
8. retains all prior schema, authorization, T-label, trust-root, inventory, syntax, and no-chain checks.

The test reports the sealed root value as a source-bound expectation. It does not recompute that value from Builder B's code in this session.

## 5. Complete disclosed delta

The comparison base is the registrar-mirrored Builder A package accompanying sealed artifact `STAGE8_TASK6_VALIDATE_AGAINST_SCHEMA_LANE2_V001.md`, SHA-256 `c954584fefc766c56932900453d744d8d5e4c39892e9335c8fb4ad9727de4702`. Byte comparison found exactly five changed files and no added or removed package file.

Diff conventions: unified-diff hunks; text insertions/deletions count newline-delimited physical lines. Canonical JSON documents have one physical line, so content changes count as one insertion and one deletion; byte lengths and SHA-256 digests are authoritative.

| File | Base bytes / SHA-256 | Final bytes / SHA-256 | Diff | Disclosed delta |
|---|---|---|---|---|
| `parent.py` | 62,496 / `3415cbc2c6ceb656a32ff149ed18031a7b41f6214d887f2081a92beb2c2d138b` | 62,956 / `31e4bccae6b30ca33d491f6a7a208e896c0fc9353a4e16188f6546374653badc` | 4 hunks; +26/-17 | install sealed twelve-member tuple; replace 11-member inference; bind schema external input to root member; record V002 note |
| `tools/self_check.py` | 42,244 / `0b64a2ef3992ae8fe301589fbc5eaa06e5810bb26e68f561ea174245ab456396` | 44,618 / `b9badc4b7054497813048bd70b9dc7f9e7bbc4bcd70cf13b3e79dc1edfc2eb3a` | 5 hunks; +37/-1 | sealed-source pin, exact twelve-name census, source/receiver audits, V002-note guard, transcript |
| `manifests/normal.json` | 8,951 / `ca450c8b37831fff2416b98ed1ce9c4de5b9a52963901118f5d670d1c90fec23` | 8,951 / `fe3a0a27d90c6ced7a29bd75e049e567eb8d5fb5db34dc58724f597a8196e6a9` | 1 hunk; +1/-1 | refresh changed Builder A code pins |
| `manifests/optimized.json` | 8,960 / `de5c4282b4b783d90fad86f6d2807cceea54578eac32376e31601540493ce765` | 8,960 / `fa8d36fc5a237ece34ceb24bd23e302d9d353d0a8bede366822786526710adb5` | 1 hunk; +1/-1 | refresh changed Builder A code pins |
| `manifests/package_inventory.json` | 5,361 / `c8a723615cbec9e829bcc529e927d5e3d1e3284a7d6038014310b8f886c51443` | 5,361 / `53cf9ec36a1412b006cd28ee4f7f39b710bde52ccb4fe78626c27a4a54c4fddf` | 1 hunk; +1/-1 | refresh parent, self-check, and manifest pins |

Total under the declared convention: 12 hunks, 66 inserted physical lines, 21 deleted physical lines. Every other Builder A package file is byte-identical to the registrar mirror.

## 6. Static transcript and idempotence

Only the materializer and static self-check ran under `/usr/bin/python3 -I -S -B`. No parent, producer, verifier, check executor, fixture, or subject lineage was invoked.

```text
MATERIALIZE_OK checks=66 fixtures=6 gated=10 structural=56 normal_sha256=fe3a0a27d90c6ced7a29bd75e049e567eb8d5fb5db34dc58724f597a8196e6a9 optimized_sha256=fa8d36fc5a237ece34ceb24bd23e302d9d353d0a8bede366822786526710adb5 subject_lineage_root=d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688
SELF_CHECK_OK syntax=5 canonical_json=all local_schemas=8 verifier_root_members=12 verifier_root=dba5377d5ca1e7eebf2932da10e043e96c33f642cf06c8dd81cf26dff3bd3ac0 root_membership_source=de9139768c68371310e48245568472273fc19da96c48004ef7819ee6b0dbab79 membership_in_instance_note=RECORDED_FOR_CONTRACT_V002 verdict_schema=300a475ead3c17cd5b759ffcc3733418029030404af262632583fff077f2907f verdict_schema_keywords=$comment,$schema,additionalProperties,const,enum,items,oneOf,pattern,properties,required,type verdict_documents=full:accepted,fault:accepted negatives=old13,full_extra,fault_extra,wrong_spec:rejected inventory=30 evidence_payloads=10 evidence=0/56 absent=56 fixture_obs=0/3 checks=66 structural=56 gated=10 fixtures=6 producer_fields=13 receipt_fields=16 fixture_fields=16 child_fields=14 verifier_manifest_fields=11 authorization_fields=artifact_sha256,scope authorization_digest=ff84c4a8ba5c7f8eabfbcc587475d3a5050c21d758a2788c5b9e28b7ee022340 authorization_scope=equals_ledger_scope authorization_forward=producer,terminal,verifier_receiver t_labels=producer:T0,T1,T2,T3(no_T4);terminal:T0,T1,T2,T3,T4(actual_T4) t4_before_sample_guard=PASS trust_root=7a80a5d52fd35701d8da02239178f63ef80e4f80ce8557636db99a326cf4c73c trust_sites=10 trust_agreement=definition,manifests,main_receiver,T0_T3,child_rows,producer_runtime,producer_T0_T3_value_only,verifier_receiver,terminal_runtime,terminal_T0_T4 exits=0/1/2 chain_invoked=false
```

The second materialization/self-check pass returned the same values. Before and after that pass:

```text
normal.json             fe3a0a27d90c6ced7a29bd75e049e567eb8d5fb5db34dc58724f597a8196e6a9
optimized.json          fa8d36fc5a237ece34ceb24bd23e302d9d353d0a8bede366822786526710adb5
package_inventory.json  53cf9ec36a1412b006cd28ee4f7f39b710bde52ccb4fe78626c27a4a54c4fddf
```

The 30-file carried inventory validates. Package `outputs/` and `pycache/` directories remain empty.

## 7. PIN CHECK, gates, and verb audit

- Output artifact and sidecar names were absent in cleanroom and archive workspace before creation.
- The sealed 676 artifact and sidecar verified before reading; the artifact matches the registrar mirror byte-for-byte.
- The five base hashes were recomputed from the registrar-mirrored 675 package before diffing.
- Final parent and self-check hashes agree across both child manifests and the package inventory.
- Two materialization/self-check passes produced identical top-level manifest hashes.
- This artifact is hashed only after its final byte is written; its `.seal.sha256` records that post-write digest. The registrar, not Builder A, mirrors it.

Gate audit: `alpha_computed = false`; `proof_authorized = false`; `kappa_record_computed = false`. No member binding, fixed-point execution, end test, physical-quantity evaluation, or measured-constant comparison occurred.

Verb audit under the verdict-line scope rule: CLEAN. “Members” refers only to the verifier-package root census, not mathematical member binding. No evaluator, check, fixture, authorization, or scientific verdict is claimed.

MEMBERS = 12 (per the sealed 676 list)
NOTE = membership-in-instance recorded for contract V002
SELF_CHECK = passed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
