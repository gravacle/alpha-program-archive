# STAGE 8 TASK 6 — BUILDER A VALIDATION AGAINST BUILDER B'S SEALED VERDICT SCHEMA

**Lane:** Codex Lane 2 / Builder A  
**Date:** 2026-08-07  
**Disposition:** COMPLETE  
**Scope:** verdict-contract ingestion and validation, external-input manifests, static tests, and content-addressed inventory only  
**Authority:** RD-22 implementation; no scientific, proof, or seal authority claimed

## 1. Sealed authority and R0 binding

Builder B's cleanroom contract is:

```text
evaluator_build_B/contracts/verifier_verdict.schema.json
byte_length = 5154
SHA-256 = 300a475ead3c17cd5b759ffcc3733418029030404af262632583fff077f2907f
seal-sidecar SHA-256 = 4973bb2da031f9e4e8152ce1584f3648334b96e70ac5224fdef66c65d8446c53
```

The schema sidecar verifies. Its bytes are identical in the cleanroom and registrar mirror. The accompanying sealed Builder B disposition is `STAGE8_TASK6_VERDICT_SCHEMA_CONFORM_DARIO_V001.md`, SHA-256 `0b7f47df011409d6deeb95a4e62b0d3a3b86a06199082b2f5e76d9b19b3f7418`; its sidecar verifies.

Both Builder A child manifests now carry one external-input row:

```json
{"byte_length":5154,"kind":"verifier_verdict_schema","relative_path":"alpha_fundamental_record_action_cleanroom_v003/evaluator_build_B/contracts/verifier_verdict.schema.json","sha256":"300a475ead3c17cd5b759ffcc3733418029030404af262632583fff077f2907f"}
```

At R0, `verify_external_inputs` resolves this declared path under the program root, verifies its SHA-256 and byte length, and returns those verified bytes. The parent parses exactly those bytes with duplicate-key, UTF-8, and nonfinite-number rejection, then checks the schema-definition subset before any producer child starts. The verdict validator never loads an unpinned directory candidate and never substitutes a locally generated output contract.

## 2. Supported schema subset

The implementation names and enforces this complete keyword set appearing in B's sealed document:

```text
$comment
$schema
additionalProperties
const
enum
items
oneOf
pattern
properties
required
type
```

`$comment` and `$schema` are recognized metadata and must have string values. The validation-bearing keywords are executed recursively. Unsupported keywords anywhere in the schema fail `VERDICT_SCHEMA_KEYWORD`; malformed keyword values fail `VERDICT_SCHEMA_DEFINITION`. Supported JSON types are object, array, string, boolean, integer, number, and null. `pattern` uses regular-expression search as draft-07 specifies. `oneOf` must match exactly one branch.

This set includes the task's required `type`, `required`, `additionalProperties`, `oneOf`, and `const`, plus every other keyword present in the sealed schema that affects its instances. No load-bearing schema keyword is silently ignored.

## 3. Document-kind validation and semantic checks

`verifier_stdout` first enforces one tight canonical JSON value and then passes the parsed value to the sealed-schema validator. The matching `oneOf` branch—not a Builder A field census—defines the declared surface.

| Document kind selected by the sealed schema | Schema result | Builder A semantic checks |
|---|---|---|
| full verdict, 14 required fields, closed | accepted only on exactly one matching branch | schema name; expected verdict from exit 0/1; authorization and specification digests; verifier self digest; runtime subject; independence; authority firewall; no findings on `VERIFIED` |
| fault document, 3 required fields, closed | accepted only on exactly one matching branch | schema name and expected `FAIL` from exit 2; the branch declares no authorization/specification fields, so none are fabricated or compared |

The authorization/specification pair is checked whenever the selected schema branch declares it. A branch that declares only one member of the pair fails `VERIFIER_SCHEMA_AUTHORITY_PAIR`. B's full branch declares both; B's fault branch declares neither, preserving the sealed absent-vs-empty rule.

Exit 2 remains a terminal fail-closed fact. The ordering is corrected so its stdout is first accepted or rejected against the lawful three-field branch, then the parent terminates with `R9_VERIFIER_FAIL_CLOSED_EXIT_2` carrying the sealed fault text. Accepting the document kind does not turn an exit-2 run into success.

## 4. Transcription audit

The convicted runtime transcription was removed:

```text
REMOVED: verifier_stdout's hard-coded 13-field set and exact_keys comparison
```

The package sweep found and removed one additional transcription:

```text
REMOVED: evaluator_build_A/schemas/verifier-output.schema.json
REMOVED: its materializer definition
REMOVED: its required-package entry and inventory references
```

That local file was Builder A's obsolete 13-field restatement of Builder B's output shape. The static self-check now fails if the path reappears or if the former field-list validator returns.

The remaining Builder B-related checks are not output-shape transcriptions:

- `entry_point` syntax, exit mapping, and stdout discipline are shared integration-addendum contract items.
- authorization/specification, verifier identity, runtime identity, independence, and firewall checks are post-schema semantic bindings required by the parent.
- the static full and fault documents are positive/negative test instances; they do not define the accepted field set.

No other runtime validator or local schema claims authority over Builder B's output shape.

## 5. Static demonstrations

Positive cases:

```text
full 14-field verdict  -> accepted by exactly one branch; semantic pins pass
fault 3-field document -> accepted by exactly one branch; expected FAIL passes
```

Negative cases:

```text
old 13-field verdict                    -> rejected (fixtures_replayed missing)
full verdict plus undeclared field      -> rejected
fault document plus undeclared field    -> rejected
full verdict with wrong spec_sha256     -> rejected by sealed const
```

The first schema-driven static attempt also rejected Builder A's former synthetic firewall fixture because it supplied only the six fixed-false gate fields while B's full schema requires all nine firewall fields. The test fixture was corrected to use the manifest's complete nine-field firewall object. This was a test-data correction exposed by the new validator; no runtime contract was weakened.

## 6. Complete disclosed delta

The comparison base is the registrar-mirrored package sealed with `STAGE8_TASK6_REMOVE_T4_FABRICATION_LANE2_V001.md`, SHA-256 `71ccf0718ed1289496ba6b2c244c9cd5be2d328d8b52c7bf3804c97323695807`. Byte comparison found exactly six changed files and one removed file.

Diff conventions: unified-diff hunks; text insertions/deletions count newline-delimited physical lines. Canonical JSON files have one physical line, so their content changes count as one deletion plus one insertion; their byte lengths and SHA-256 digests are authoritative.

| File | Base bytes / SHA-256 | Final bytes / SHA-256 | Diff | Disclosed delta |
|---|---|---|---|---|
| `parent.py` | 56,828 / `5e94efc64d38977bcfa030305c7c7ac7f07c85a45e4413eb27861c6561c94638` | 62,496 / `3415cbc2c6ceb656a32ff149ed18031a7b41f6214d887f2081a92beb2c2d138b` | 8 hunks; +146/-28 | schema subset, R0 verified-byte carrier, schema-driven stdout validation, both exit document kinds, field-list deletion |
| `tools/materialize.py` | 32,330 / `dc2cbbef651109f51f4a0cb8d9edeaacb58b34339b646ed759202d42088839c1` | 31,681 / `33a00a8c8b7c3dada0cabaa3860c4c625e60ba45e07d1614a0d152de4193a948` | 4 hunks; +4/-6 | pin/add B schema external input; delete local output-schema generator |
| `tools/self_check.py` | 38,530 / `737d15f75909151337191513b08567a3c4fd082990c06ae4306af7b6be987da1` | 42,244 / `0b64a2ef3992ae8fe301589fbc5eaa06e5810bb26e68f561ea174245ab456396` | 8 hunks; +51/-5 | external pin, two positives, four negatives, transcription audit, keyword audit, transcript |
| `manifests/normal.json` | 8,850 / `53b57459b27cfe3427af4389ebb532df2626cb05778ffd0be2c4c5b79fdd2aeb` | 8,951 / `ca450c8b37831fff2416b98ed1ce9c4de5b9a52963901118f5d670d1c90fec23` | 1 hunk; +1/-1 | new external-input pin and refreshed 30-file package inventory |
| `manifests/optimized.json` | 8,859 / `f0adc15abb751430fec3969df01a4f25704eaaf6c28a8abe15f28991c2516ef5` | 8,960 / `de5c4282b4b783d90fad86f6d2807cceea54578eac32376e31601540493ce765` | 1 hunk; +1/-1 | same external-input pin and refreshed inventory |
| `manifests/package_inventory.json` | 5,512 / `de3b0c616fcea090f7917630658d794b87d94b8464fb2ae7d95ce86fd6190490` | 5,361 / `c8a723615cbec9e829bcc529e927d5e3d1e3284a7d6038014310b8f886c51443` | 1 hunk; +1/-1 | changed hashes and removal of the local transcribed schema |
| `schemas/verifier-output.schema.json` | 1,475 / `fe64a9cd0a3d5f52d5273110c7b89169c13bc24c7db638deb741f05aec5a181e` | absent | 1 hunk; +0/-1 | obsolete Builder A output-contract transcription deleted |

Total under the declared convention: 24 hunks, 204 inserted physical lines, 43 deleted physical lines. Every other Builder A package file is byte-identical to the registrar mirror.

## 7. Static self-check and idempotence transcript

Only the authorized materializer and static self-check ran under `/usr/bin/python3 -I -S -B`. Neither parent, producer, verifier, check executor, fixture, nor subject lineage was invoked.

```text
MATERIALIZE_OK checks=66 fixtures=6 gated=10 structural=56 normal_sha256=ca450c8b37831fff2416b98ed1ce9c4de5b9a52963901118f5d670d1c90fec23 optimized_sha256=de5c4282b4b783d90fad86f6d2807cceea54578eac32376e31601540493ce765 subject_lineage_root=d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688
SELF_CHECK_OK syntax=5 canonical_json=all local_schemas=8 verdict_schema=300a475ead3c17cd5b759ffcc3733418029030404af262632583fff077f2907f verdict_schema_keywords=$comment,$schema,additionalProperties,const,enum,items,oneOf,pattern,properties,required,type verdict_documents=full:accepted,fault:accepted negatives=old13,full_extra,fault_extra,wrong_spec:rejected inventory=30 evidence_payloads=10 evidence=0/56 absent=56 fixture_obs=0/3 checks=66 structural=56 gated=10 fixtures=6 producer_fields=13 receipt_fields=16 fixture_fields=16 child_fields=14 verifier_manifest_fields=11 authorization_fields=artifact_sha256,scope authorization_digest=ff84c4a8ba5c7f8eabfbcc587475d3a5050c21d758a2788c5b9e28b7ee022340 authorization_scope=equals_ledger_scope authorization_forward=producer,terminal,verifier_receiver t_labels=producer:T0,T1,T2,T3(no_T4);terminal:T0,T1,T2,T3,T4(actual_T4) t4_before_sample_guard=PASS trust_root=7a80a5d52fd35701d8da02239178f63ef80e4f80ce8557636db99a326cf4c73c trust_sites=10 trust_agreement=definition,manifests,main_receiver,T0_T3,child_rows,producer_runtime,producer_T0_T3_value_only,verifier_receiver,terminal_runtime,terminal_T0_T4 exits=0/1/2 chain_invoked=false
```

The second materialization/self-check pass returned the same results. Before and after that pass:

```text
normal.json             ca450c8b37831fff2416b98ed1ce9c4de5b9a52963901118f5d670d1c90fec23
optimized.json          de5c4282b4b783d90fad86f6d2807cceea54578eac32376e31601540493ce765
package_inventory.json  c8a723615cbec9e829bcc529e927d5e3d1e3284a7d6038014310b8f886c51443
```

The package inventory validates 30 carried files; the inventory document itself is the thirty-first package file. `outputs/` and all package `pycache/` directories remain empty.

## 8. PIN CHECK, gates, and verb audit

- The output artifact and seal-sidecar names were absent in both cleanroom and archive workspace immediately before creation.
- Builder B's schema digest and seal were verified before reading; its cleanroom and archive bytes compare equal.
- The six base file hashes and removed-file hash were recomputed from the registrar mirror before diffing.
- Both final manifests carry the 5,154-byte schema at `300a475e…`; R0 requires the exact eight-kind external-input census.
- Final package hashes agree across the child manifests and package inventory; the idempotence pass did not move them.
- This artifact is hashed only after its final byte is written; its `.seal.sha256` records that post-write digest. The registrar, not Builder A, mirrors it.

Gate audit: `alpha_computed = false`; `proof_authorized = false`; `kappa_record_computed = false`. No member binding, fixed-point execution, end test, physical-quantity evaluation, or measured-constant comparison occurred.

Verb audit under the verdict-line scope rule: CLEAN. “Accepted” and “rejected” refer only to static schema test documents. No evaluator result, check result, fixture result, authorization verdict, or scientific verdict is claimed.

VERDICT_VALIDATION = against B's sealed schema (pinned; supported keywords: $comment, $schema, additionalProperties, const, enum, items, oneOf, pattern, properties, required, type)
TRANSCRIPTIONS = removed (+audit: runtime 13-field list and local output schema removed; no other output-shape validator)
SELF_CHECK = passed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
