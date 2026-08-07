# STAGE 8 / TASK 6 / BUILD A — CANON TRAILING-NEWLINE FIX — LANE 2 V001

Lane: Lane 2, Builder A  
Relay: PASTE 656  
Context: Q-594 adjudication against the trailing LF  
Scope: Builder A canonical encoders, validators, package JSON regeneration, and hashes only  
Authority claimed: none

```text
SPEC_V005_SHA256 = f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b
PRIOR_BUILD_A_CERTIFICATE_SHA256 = 733228c59e8773039457937a4bd1d49681c9b4628dcf39d83810dd365f9239c3
CANONICAL_JSON_ARTIFACTS = 16
CHANGED_CODE_FILES = 5
CHAIN_INVOKED = false
```

## 1. Preflight and adjudicated defect

| Check | Result |
|---|---|
| Output collision | Artifact and sidecar absent in cleanroom and archive immediately before creation. |
| V005 | Rehashed to `f8d1a7dc…` before reading §9.4. |
| Prior Builder A state | Sealed PASTE 653 certificate rehashed to `733228c5…`; its sidecar records that exact digest. |
| Package census | 32 delivered package files: 31 rows inside `package_inventory.json` plus the inventory file itself. |
| Chain state | Output directory and normal/optimized/verifier pycache directories empty. |

V005 §9.4 requires canonical UTF-8 JSON with sorted keys and no insignificant whitespace. The former Builder A encoders returned

```python
(text + "\n").encode("utf-8")
```

so the otherwise canonical object acquired one insignificant trailing LF. The Q-594 adjudication controls: that byte is not part of the canonical form.

All five Builder A encoder/validator sites now use tight bytes:

```python
json.dumps(
    value,
    ensure_ascii=False,
    allow_nan=False,
    sort_keys=True,
    separators=(",", ":"),
).encode("utf-8")
```

The parent and producer return the same form through `canonical_bytes`. The verifier-stdout validator no longer requires one LF; it requires one nonempty JSON value whose entire byte string equals the tight canonical re-encoding. The manifest's `lines=1` remains satisfied by a single logical JSON line containing no line terminator or other output.

The remaining `"\n"` uses in `materialize.py` and `self_check.py` are the sealed Markdown descriptor-row convention—exact source rows include one LF—and human-readable diagnostic `print` output. They are not JSON encoders and were not changed.

## 2. Disclosed code delta — five files

| File | Before | After | Exact change |
|---|---|---|---|
| `parent.py` | 36,465 bytes; `da0c9c4a060985cd39582081e1d5ee0874c91fc6d41bc37385a329eaf42e77b7` | 36,405 bytes; `7a1b35d013875b0f711155f16122b3098022894d7f3730859b13bd3a98e2d638` | Remove terminal LF from `canonical_bytes`; replace LF-count/terminal-LF requirement on verifier stdout with nonempty tight-canonical equality. |
| `producer.py` | 39,567 bytes; `93d717df36807e66ca09919ca90157e79b016831e5200852350d8887a57c3982` | 39,558 bytes; `4297670d4df7a7c9083ec62aba0354538605f44829c2df749e99e93324e6bc44` | Remove terminal LF from `canonical_bytes`. |
| `tools/materialize.py` | 30,629 bytes; `ba3c3ae4e825f3044ae4c9e781dbe1fb096443bc3dc1603b0223c14e129957d3` | 30,620 bytes; `abcea45941b51e6705bac84c07e0e258b3a3b3fbdd42521fba9e9e4dfd18ea82` | Tight canonical artifact writer. |
| `tools/assemble_evidence.py` | 13,582 bytes; `11addee3e9e9764fee711cf4b136bca003948c152f3f04ee8ba4c1cde88cd1a4` | 13,573 bytes; `025d9a083f2ef7e46ab4cc70944dfda65d59b21e8d532f6f1a77ccde67c6a8fd` | Tight canonical evidence-manifest reader/writer form. |
| `tools/self_check.py` | 23,649 bytes; `74050e4444550a51cfadf2e35cfdb342989d90dafb823ac3d78f726b513d1437` | 23,638 bytes; `c0df80441f34b42737937c2d89fb6386cd6cba7ee2fbd4e6e10676428d733913` | Validate tight bytes and change the canonical empty-array digest from `SHA256(b"[]\n")` to `SHA256(b"[]")`. |

No other Python or Markdown package file changed. `README.md` remains `13634ef6…`; all ten evidence payloads remain byte-identical to their sealed sources.

## 3. Regenerated canonical artifacts — 16 files

Every package JSON artifact was reserialized from its parsed value by the corrected tight encoder. All lost exactly the former terminal LF; artifacts containing hashes also received the recursively updated content references.

| Canonical artifact | Before bytes / SHA-256 | After bytes / SHA-256 |
|---|---|---|
| `checks/check_map.json` | 107,235 / `034ebf3e071051d25d5b7f8871a03193da5bc9ab16a7c07c7cae1bbb8f467e26` | 107,234 / `0daa01f3c4f872b995cee1fef3c2dcb804cee11871b8c56fd22c14d89b1cff51` |
| `fixtures/fixture_manifest.json` | 7,894 / `dc635a83fe39e62bdc2b76c8c40cfce977ac67fdaf0eede32344d0b98dabf2db` | 7,893 / `2e823e627830d882f42cf2fe9f12dccb13ac6ddd8d7a4eb3a08704b84734510e` |
| `inputs/structural_evidence_manifest.json` | 98,663 / `722f4db56fc6e77de258273f06fd1ae487b9bb0143440f73adb76747779a5cb8` | 98,662 / `dfb29bf2cbc32fd6d4e29421cddff312e10237321a90b76a071b83601406b8af` |
| `inputs/subject_lineage_manifest.json` | 1,510 / `e6918e0254d63671dd0fd3652290e4a0b1781abb6c4d63e81043f1d8f3327d54` | 1,509 / `da37ece918c184a0193805042fd6158c7edd1c051f05feb4f2bbef69f05544db` |
| `manifests/normal.json` | 9,172 / `f8c9f05b01203d53da7baf90b7dc8f658485e9019fcfbea4abe722b3bce4723e` | 9,171 / `75ea0020f8a1808269aa87b04f30f059643816abb28a6209cb935a5b7bed5e48` |
| `manifests/optimized.json` | 9,181 / `5484bcdbe64c7a2eb3e48a616150b40b8e5f1cc2a192779a85ea4677a5749a3b` | 9,180 / `04af62ff4b1706276e157a773a9fc3b39672050ac0561259bb7c9d7353eaabed` |
| `manifests/package_inventory.json` | 5,512 / `ea927eb8f3db513aa33cff6464cc47984bafab2ac3f523c6a8699f3de08cf7d5` | 5,511 / `65f3c45da98cf8c5dbbf16c61dddc13ebd55967140444c9264e4dcf20ccedd57` |
| `schemas/check-map.schema.json` | 456 / `8e971040ca4d96161303710bc391dd322cb581983c881eaf39b1547fb4e68192` | 455 / `4f37059e96e62574e10ef4c91121109b12f921e65ba67a0333eac12a2c6c64d4` |
| `schemas/child-manifest.schema.json` | 1,420 / `f5325b40cd49db94e11cc44628ec46b6ac400489d99c574642461e0b8697ef1e` | 1,419 / `d0e199092727a2e0868afb0142bf78b6fc294e1a59fa617b04adab3a6792f5e5` |
| `schemas/child-receipt.schema.json` | 1,277 / `0ce216024263ee7b2de3643fc4b44cc1a581d7a2334968da8ebdf8b9d02fa7bf` | 1,276 / `5289d078a687fdfe8a82c1d001ccb0f13105eabccf3f2f87ea57298f640fb0a3` |
| `schemas/fixture-manifest.schema.json` | 1,347 / `3723297f9f9e9aa5b6e16f35a3315966d49997734c223580807b916ebfc4e986` | 1,346 / `fb19b5c4c834b464bec9887193147edd30b2db3a3992c0039c114cbe041982fa` |
| `schemas/producer-output.schema.json` | 2,425 / `d3e4dc5c32e265ec5a8373b734f9d277573d862c97cb563f03c3e97f55e534b3` | 2,424 / `07cb427cf5f7d337b41d68e9b657f18059ab7bb22522107e65a93ffaec0331a6` |
| `schemas/structural-evidence.schema.json` | 351 / `5d3ec96abcec19f664665f5a1bf316a9c4fa3d95aa66b8551de8036d85f97174` | 350 / `70b8cd958ec74c84be7c1ee062cafdad17d340b29b5d27e5b78a6f94ddc09740` |
| `schemas/terminal-ledger.schema.json` | 3,920 / `5635e68e13932915f6724f7a1aa2533fa52d8cc7170be9a44f09433ae9816af5` | 3,919 / `7b91e10d43be2dfa56bb23cea30388d848ac405161678ee8a06d30992cdf771b` |
| `schemas/verifier-manifest.schema.json` | 1,691 / `05cb23509293da9d8a184cd48a7f6cc1c36e56c3ab4114d8548bea8824fc9d15` | 1,690 / `d10ebe15d1c61a2e395d3199026b214408721fac333754d0a018a319b2d1f481` |
| `schemas/verifier-output.schema.json` | 1,476 / `145dfdf6aefa40766b9e680dd59714ffbd94133411ea89a0e7d7aab8d6f033ad` | 1,475 / `fe64a9cd0a3d5f52d5273110c7b89169c13bc24c7db638deb741f05aec5a181e` |

Runtime/inventory summary after recursive regeneration:

```text
normal.json            = 75ea0020f8a1808269aa87b04f30f059643816abb28a6209cb935a5b7bed5e48
optimized.json         = 04af62ff4b1706276e157a773a9fc3b39672050ac0561259bb7c9d7353eaabed
package_inventory.json = 65f3c45da98cf8c5dbbf16c61dddc13ebd55967140444c9264e4dcf20ccedd57
subject_lineage_root    = d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688
```

The subject-lineage root is unchanged because it addresses the same sealed external subject files; only the serialization of its manifest changed.

## 4. M3 — no-other-deviation audit

The audit covered the encoder functions in `parent.py`, `producer.py`, `materialize.py`, `assemble_evidence.py`, and `self_check.py`, then strict-parsed and exact-re-encoded all 16 JSON artifacts.

| §9.4 canon property | Encoder fact | Audit result |
|---|---|---|
| Key order | `sort_keys=True` at all five encoder/validator sites. | Sorted; a reversed-key object re-encodes in key order. |
| Separators / whitespace | `separators=(",", ":")`; encoder returns the UTF-8 bytes directly. | No spaces, CR, LF, or terminal byte outside the JSON value. |
| Unicode | `ensure_ascii=False` followed by `.encode("utf-8")`. | Direct UTF-8 is canonical; an equivalent `\u00e9` input does not survive exact re-encoding. |
| Number forms | `allow_nan=False`; strict parsers reject `NaN`/infinities; exact re-encoding fixes one finite spelling. | Nonfinite values rejected; alternate spellings `1e0`, `1.00`, and `-0` do not equal their canonical re-encoding. §9.4 states no narrower external numeric profile. |
| Duplicate keys | Runtime strict parsers use an object-pairs hook; final static audit uses the same rule. | Duplicates rejected before canonical admission. |
| Undeclared fields | Closed schemas and exact-field checks remain unchanged. | No canon-related relaxation. |

Audit transcript line:

```text
CANON_AUDIT_OK keys=sorted separators=tight unicode=utf8 numbers=finite_unique trailing_newline=false
CANON_ARTIFACTS_OK 16
```

No other deviation from the words of V005 §9.4 was found in Builder A's encoder or in the 16 regenerated artifacts.

## 5. Static self-check transcript

Only source compilation, evidence-metadata validation, deterministic materialization, strict JSON/schema validation, hashing, and the canon audit ran. The parent, producer, verifier, check executors, and fixtures did not run.

```text
$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/materialize.py
{"checks": 66, "fixtures": 6, "gated": 10, "normal_sha256": "75ea0020f8a1808269aa87b04f30f059643816abb28a6209cb935a5b7bed5e48", "optimized_sha256": "04af62ff4b1706276e157a773a9fc3b39672050ac0561259bb7c9d7353eaabed", "structural": 56, "subject_lineage_root": "d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688"}

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/assemble_evidence.py
{"authored_payload_bytes": 0, "checks_absent": 56, "checks_populated": 0, "fixtures_absent": 3, "fixtures_populated": 0, "payload_files": 10, "search_scope_members": 120, "search_scope_sha256": "691e871e4b2a13f09cdf5481abb1c7a32c05ba9426bf657436a5f5f2597db032"}

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/materialize.py
{"checks": 66, "fixtures": 6, "gated": 10, "normal_sha256": "75ea0020f8a1808269aa87b04f30f059643816abb28a6209cb935a5b7bed5e48", "optimized_sha256": "04af62ff4b1706276e157a773a9fc3b39672050ac0561259bb7c9d7353eaabed", "structural": 56, "subject_lineage_root": "d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688"}

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/self_check.py
SELF_CHECK_OK syntax=5 canonical_json=all schemas=9 inventory=31 evidence_payloads=10 evidence=0/56 absent=56 fixture_obs=0/3 checks=66 structural=56 gated=10 fixtures=6 fixture_fields=16 child_fields=14 verifier_manifest_fields=11 exits=0/1/2 chain_invoked=false
```

## 6. PIN CHECK, fences, and verb audit

### 6.1 PRE-SEAL PIN CHECK

| Pin or invariant | Final result |
|---|---|
| V005 | `f8d1a7dc…`, exact and unchanged. |
| Prior Builder A certificate | `733228c5…`, exact; sidecar content agrees. |
| Encoders | Five/five canonical encoder/validator sites have sorted keys, tight separators, direct UTF-8, nonfinite rejection, and no appended LF. |
| Canonical artifacts | 16/16 strict-parse and byte-equal their corrected re-encoding; none ends in CR/LF. |
| Runtime manifests | `75ea0020…` / `04af62ff…`; common package files and internal hashes agree. |
| Package inventory | 31 declared rows rehashed; inventory self digest `65f3c45d…`. |
| Evidence payloads | Ten/ten unchanged, byte-identical sealed-source copies. |
| Output collision | Artifact and sidecar absent in cleanroom and archive immediately before creation. |
| Chain products | Output and all three pycache directories remain empty. |

### 6.2 Fences

No evaluator component ran. No member was bound; no fixed point or end test ran; no physical quantity was evaluated; and no measured constant was read or compared. `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false`.

### 6.3 Self verb audit under the verdict-line scope rule

| Verb | Scoped meaning |
|---|---|
| `canon` / `canonical` | Exact V005 §9.4 byte discipline implemented by the displayed encoder; not a claim of RFC 8785 or an unstated numeric profile. |
| `regenerated` | The 16 listed JSON files were deterministically reserialized and rehashed; sealed evidence payload bytes were not regenerated. |
| `audit` | Static source inspection plus representative encodings and exact re-encoding of all package JSON. |
| `passed` | Static syntax/schema/hash/canon validation only. |
| `sealed` | Applies only after adjacent sidecar creation and grants no chain, result, or proof authority. |

CANON = tight, no trailing newline (spec-grounded)
REGENERATED = 16 files (+hashes)
AUDIT = no other deviation
SELF_CHECK = passed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN / (+tight-canon scope; 16 JSON artifacts only; static audit/pass; authorization and proof not claimed)
