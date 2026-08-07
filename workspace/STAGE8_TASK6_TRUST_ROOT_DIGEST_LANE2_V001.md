# STAGE 8 / TASK 6 / BUILD A — TRUST-ROOT DIGEST, SINGLE DEFINITION — LANE 2 V001

Lane: Lane 2, Builder A  
Relay: PASTE 668  
Context: run 014 verifier diagnostic `runtime_subject.trust_root: not a lowercase sha256 hex digest`  
Scope: trust-root representation, all parent trust carriers, manifest materialization, boundary schemas, static agreement test, recursive hashes, and disclosed finite delta  
Authority claimed: none

```text
SPEC_V005_SHA256 = f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b
INTEGRATION_ADDENDUM_SHA256 = d17c5e79986bea431dec0b572019096f9c059bcc43876fda9134abc96ce0f260
RUNTIME_SNAPSHOT_SHA256 = 50a6fc141a45451678aa7543e4f267ce26beb6e53182170b478acb6fb0e0f5bb
RUNTIME_GATE_SHA256 = 2ad7f72a88184c11e1253f2c47598fca11e60d05e8e71a26db4e19b16bf98d42
PRIOR_PARENT_SHA256 = a5b99a1a5c3594084d7793b024ee1ad6b4b7bd8a75fb1934c20b8ccb1f637e31
FINAL_PARENT_SHA256 = 175068a311feaf90711874a502dda68b9ef561e92121dda0f9fb5f588c5dcce4
TRUST_ROOT_SHA256 = 7a80a5d52fd35701d8da02239178f63ef80e4f80ce8557636db99a326cf4c73c
CHAIN_INVOKED = false
```

## 1. Preflight and defect disposition

| Check | Result |
|---|---|
| Output collision | This artifact and sidecar were absent in both the cleanroom and archive workspace immediately before creation. |
| Governing pins | V005, the integration addendum, runtime snapshot v012, and runtime gate v010 verify at the exact hashes above. |
| Builder A base | The archive mirror is the exact PASTE 666 base: parent `a5b99a1a…`, normal manifest `4f09af9f…`, optimized manifest `7b6ad45d…`, and package inventory `f9ebe36c…`. |
| Prior sealed artifact | `STAGE8_TASK6_ARGV_PREFIX_FIX_LANE2_V001.md` verifies at `5fb65c12484469a5dc0af35f46b05d005f86adb7446fffe9f69ef95c1a204ca3`. |
| Run 014 evidence | The retained producer ledger has a raw object at `runtime_subject.trust_root` while its `T0..T4` values are already the digest `7a80a5d5…`. This is the exact split representation described by the relay. |
| Chain state | No producer, verifier, check executor, fixture, launcher, or full chain was invoked in this relay. |

The old build materialized the sealed snapshot's `native_system_trust_root` object directly into both child manifests. The parent then had two incompatible receivers:

```text
verifier output expectation: trust_hash(runtime["native_system_trust_root"])
R0 manifest comparison:      runtime_subject["trust_root"] == runtime["native_system_trust_root"]
```

Because `verdict_ledger()` carries `normal_manifest.runtime_subject`, the raw object entered the post-production producer ledger and reached the verifier. Separately, `trust_snapshot()` returned the raw object and the ledger construction hashed it, explaining why run 014's `T0..T4` were digests while `runtime_subject.trust_root` was not.

## 2. Single definition

The only value definition is now:

```text
trust_root_digest(native_system_trust_root)
    = SHA256(canonical_bytes(native_system_trust_root))
    = 7a80a5d52fd35701d8da02239178f63ef80e4f80ce8557636db99a326cf4c73c
```

`canonical_bytes` is the existing tight canonical JSON encoder: UTF-8, sorted keys, `ensure_ascii=false`, no nonfinite numbers, separators `,` and `:`, and no trailing newline. `trust_root_digest()` also enforces the lowercase 64-hex form before returning.

The static materializer does not duplicate this formula. It explicitly loads the Builder A parent source by path and calls the parent's `trust_root_digest()` when creating both child manifests. Thus runtime and materialization consume the same function, not two parallel implementations.

The raw trust structure is now local only to construction of a hash input. `trust_snapshot()` constructs the observed raw tuple, hashes both the observed and authorized structures through `trust_root_digest()`, compares those digests, and returns only the digest. No raw trust object is emitted into a manifest, child row, producer ledger, verifier-visible ledger, verifier-output receiver, or terminal ledger.

Independent recomputation from the pinned snapshot produced:

```text
INDEPENDENT_TRUST_DIGEST=7a80a5d52fd35701d8da02239178f63ef80e4f80ce8557636db99a326cf4c73c
CANONICAL_INPUT_BYTES=388
```

## 3. Complete trust-root touchpoint audit — 10 sites

The count below is by logical carrier/receiver site. A site that contains five labels or the normal/optimized pair is counted once and its entire closed set was checked.

| # | Site | Final receiver and result |
|---:|---|---|
| 1 | Definition | `parent.py:437-445` defines `trust_hash()` and the sole value-level `trust_root_digest()` receiver. It returns `7a80a5d5…` in 64-hex form. |
| 2 | Bound child manifests | `tools/materialize.py` loads the parent and calls that exact function. Both normal and optimized `runtime_subject.trust_root` fields equal `7a80a5d5…`; no raw object remains. |
| 3 | R0 uniqueness check | The former raw comparison at old line 1015 is replaced by `authorized_trust_root = trust_root_digest(...)`, then the manifest field is compared with that digest. |
| 4 | T0–T4 acquisition and comparisons | `trust_snapshot()` returns a digest. R4 compares `T1=T0`, R6 compares `T2=T1`, and R9 compares `T4=T3=T2`; all operands are already the single digest. |
| 5 | Per-child runtime pair | `child_record()` requires both values to be lowercase 64-hex and copies them to `runtime_before_sha256` / `runtime_after_sha256`. The former second hash was removed, preventing digest-of-digest drift. |
| 6 | Producer-ledger runtime subject | `verdict_ledger()` carries the digest-form manifest `runtime_subject`; the post-production ledger bound into the verifier launch therefore contains `trust_root="7a80a5d5…"`. |
| 7 | Producer-ledger T0–T4 | The R8 ledger writes `T0..T4` directly from digest-valued snapshots. No `trust_hash(tN)` double hash remains. |
| 8 | Verifier launch context and output receiver | The bound 11-field verifier manifest continues to bind the producer ledger by path and digest. The verifier's OS environment remains the required empty object; the trust value reaches it only inside that content-addressed ledger. The parent's verifier-output expectation independently calls `trust_root_digest(...)` and requires the same value. |
| 9 | Terminal-ledger runtime subject | The terminal `verdict_ledger()` invocation carries the same digest-form manifest runtime subject. |
| 10 | Terminal-ledger T0–T4 | The R10 ledger writes digest-valued `T0..T4` directly, including the post-verifier T4. All five are required equal to the authorized digest. |

The synthetic static agreement receiver exercised the helper, both manifests, the R0 receiver value, the T0–T4 carrier, both child-row fields, producer runtime/T fields, verifier-output receiver, and terminal runtime/T fields. Its value set had exactly one member:

```text
definition
= manifests
= main_receiver
= T0_T4
= child_rows
= producer_runtime
= producer_T0_T4
= verifier_receiver
= terminal_runtime
= terminal_T0_T4
= 7a80a5d52fd35701d8da02239178f63ef80e4f80ce8557636db99a326cf4c73c
```

## 4. Boundary contracts

The representation is now enforced rather than merely produced:

| Contract | Added receiver |
|---|---|
| `rd22.child-manifest.v001` | `runtime_subject` is closed to exactly `{gate_sha256,snapshot_sha256,trust_root}` and every value is lowercase 64-hex. |
| `rd22.terminal-ledger.v001` | `runtime_subject` has the same closed digest contract; `trust_snapshots` is closed to exactly `T0..T4`, each lowercase 64-hex. |
| Child row | Existing schema already required `runtime_before_sha256` and `runtime_after_sha256` as lowercase 64-hex; the parent now validates form before constructing the row. |
| Verifier output | Existing schema already required the three-field runtime subject and digest-form trust root; unchanged. |

The self-check validates all three closed runtime-subject boundaries and the closed five-label trust-snapshot boundary. A raw object can no longer pass those schemas.

## 5. Disclosed finite delta — eight files

Method: recursive cleanroom-versus-archive comparison excluding empty runtime output/pycache directories, then a per-file no-index diff. Exactly eight files differ; no file was added or removed. Text counts are informational. Canonical JSON files occupy one line, so their substantive field changes are stated explicitly.

| File | Before bytes / SHA-256 | After bytes / SHA-256 | Diff / disclosed change |
|---|---|---|---|
| `evaluator_build_A/parent.py` | 55,610 / `a5b99a1a5c3594084d7793b024ee1ad6b4b7bd8a75fb1934c20b8ccb1f637e31` | 56,101 / `175068a311feaf90711874a502dda68b9ef561e92121dda0f9fb5f588c5dcce4` | 8 hunks; 25 insertions, 14 deletions. Add the sole digest function; make snapshots return it; change R0 and verifier receivers; remove child/T double hashing; add child-field form gate. |
| `evaluator_build_A/tools/materialize.py` | 31,254 / `1ab3b44f229afc4eafc43e6d794532783a652fc8d9951dd75ca813c2164cc997` | 32,102 / `8c9f3737e556812c4cf5185b23d45d01e6bf0eeb195a510e98a4c44efffd617e` | 7 hunks; 21 insertions, 4 deletions. Import and call the parent's function; materialize digest-form runtime subject; close child/terminal runtime and T schemas. |
| `evaluator_build_A/tools/self_check.py` | 27,600 / `20b15151324c1eb21a34de4c517a0ff3d7e7cab5719fb820c5db9b939aa3d056` | 33,940 / `e094446aa67f5aff2f42542407b52e7a174f2ec1ac3576c27e0617a7facb9747` | 6 hunks; 93 insertions, 1 deletion. Import the parent helper, check manifest/schema/form agreement, exercise ten static carrier/receiver sites, prohibit the old raw/double-hash forms, and display the agreement. |
| `evaluator_build_A/schemas/child-manifest.schema.json` | 1,419 / `d0e199092727a2e0868afb0142bf78b6fc294e1a59fa617b04adab3a6792f5e5` | 1,695 / `cfa83d229f55b8a577ac6c262614648955005c290f41b3e5556a07e3f644d57f` | 1 canonical line replaced. Close and type the runtime subject as three digests. |
| `evaluator_build_A/schemas/terminal-ledger.schema.json` | 3,919 / `7b91e10d43be2dfa56bb23cea30388d848ac405161678ee8a06d30992cdf771b` | 4,517 / `b005c8ed00966fe3ee79c3f1fa0e0990fc9df94af5eed99f3a71dc687a9c9b03` | 1 canonical line replaced. Close/type the runtime subject and five T labels. |
| `evaluator_build_A/manifests/normal.json` | 9,172 / `4f09af9f23672b6b3e5394a33f78d99cc28ac58c9f05c46849d672dc2a086277` | 8,850 / `b74b50aaffc6ab52c9003cdea83a4f5dc1b3549e797a5b0dfa595c7e458ffb04` | 1 canonical line replaced. Raw trust object becomes `7a80a5d5…`; parent and two changed schema rows rehashed. |
| `evaluator_build_A/manifests/optimized.json` | 9,181 / `7b6ad45d4902730f0f77ea31c16ecf0f416412a7bdbd359c507080fe6db888ca` | 8,859 / `2d7cc8dc19248e05b0bad56efa2feb6b935e35f4758e06c4e16970ec98f55d9f` | 1 canonical line replaced. Same digest/root and package-row changes in optimized mode. |
| `evaluator_build_A/manifests/package_inventory.json` | 5,512 / `f9ebe36cdaef0cd5c8c9e13fb6f6b53d131586b1ee9ac225ec7c1280fceaeedb` | 5,512 / `02c74ac76f94c86fe70dee37c01e747cd947fd4302926b65480652bae293d0b3` | 1 canonical line replaced. Rehash the seven other changed package files, including both child manifests. |

Total no-index text diff: 26 hunks, 144 insertions, 24 deletions. `producer.py`, the other seven schemas, check map, fixture manifest, evidence manifest and payloads, subject lineage, Builder B package, and every other Builder A package file are byte-identical to the archive base.

## 6. Static self-check transcript

Only deterministic materialization, source parsing, schema validation, pure in-memory carrier construction/validation, and file rehashing ran.

```text
$ /usr/bin/python3 -I -S -B - <independent digest recomputation>
INDEPENDENT_TRUST_DIGEST=7a80a5d52fd35701d8da02239178f63ef80e4f80ce8557636db99a326cf4c73c
CANONICAL_INPUT_BYTES=388

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/materialize.py
{"checks": 66, "fixtures": 6, "gated": 10, "normal_sha256": "b74b50aaffc6ab52c9003cdea83a4f5dc1b3549e797a5b0dfa595c7e458ffb04", "optimized_sha256": "2d7cc8dc19248e05b0bad56efa2feb6b935e35f4758e06c4e16970ec98f55d9f", "structural": 56, "subject_lineage_root": "d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688"}

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/self_check.py
SELF_CHECK_OK syntax=5 canonical_json=all schemas=9 inventory=31 evidence_payloads=10 evidence=0/56 absent=56 fixture_obs=0/3 checks=66 structural=56 gated=10 fixtures=6 producer_fields=13 receipt_fields=16 fixture_fields=16 child_fields=14 verifier_manifest_fields=11 trust_root=7a80a5d52fd35701d8da02239178f63ef80e4f80ce8557636db99a326cf4c73c trust_sites=10 trust_agreement=definition,manifests,main_receiver,T0_T4,child_rows,producer_runtime,producer_T0_T4,verifier_receiver,terminal_runtime,terminal_T0_T4 exits=0/1/2 chain_invoked=false
```

The materializer and self-check were run a second time. All displayed hashes were identical, establishing materialization idempotence. Both runtime manifests rehash all 25 package rows; the package inventory rehashes all 31 rows. All Builder A output and pycache directories remain empty.

## 7. PRE-SEAL PIN CHECK, fences, and verb audit

### 7.1 PRE-SEAL PIN CHECK

| Pin or invariant | Final result |
|---|---|
| V005 / addendum | `f8d1a7dc…` / `d17c5e79…`, exact and unchanged. |
| Runtime snapshot / gate | `50a6fc14…` / `2ad7f72a…`, exact and unchanged. |
| Authorized trust value | Independent canonical recomputation and parent helper both produce `7a80a5d5…`. |
| Single definition | Static materializer and checker call `parent.trust_root_digest`; no second formula materializes a trust value. |
| Ten sites | All ten in-memory agreement values equal `7a80a5d5…`; forbidden raw/double-hash source forms absent. |
| Schemas | Child manifest, child rows, terminal runtime subject/T records, and verifier output all require lowercase 64-hex carriers. |
| Parent | `175068a3…`; 56,101 bytes; syntax clean; zero load-bearing `assert` nodes. |
| Runtime manifests | `b74b50aa…` / `2d7cc8dc…`; 25/25 package rows rehashed in both. |
| Package inventory | 31/31 rows rehashed; digest `02c74ac7…`. |
| Delta census | Exactly eight disclosed files differ from the PASTE 666 archive base; none added or removed. |
| Output collision | Artifact and sidecar absent in both required locations immediately before creation. |
| Chain products | Builder A `outputs/` and all package pycache directories contain no files. |

The artifact sidecar is created adjacent only after these final artifact bytes are fixed. Sealing this build report grants no chain, verdict, result, authorization, or proof authority.

### 7.2 Fences

No producer, verifier, fixture, check executor, or full chain ran. The synthetic agreement test constructed only in-memory metadata and called no subprocess. No member was bound; no fixed point or end test ran; no physical quantity was evaluated; and no measured constant was read or compared. `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false`.

No fence blocked this structural carrier repair; no MACHINERY-APPEAL is required.

### 7.3 Self verb audit under the verdict-line scope rule

| Verb | Scoped meaning |
|---|---|
| `define` / `compute` | Applies only to the canonical cryptographic digest of the sealed trust metadata object. It is not a physical computation. |
| `compare` / `agree` | Applies to static digest strings or pure in-memory synthetic carriers; no evaluator check or end test ran. |
| `bind` | Refers to content-addressed manifest/ledger metadata paths and digests, not member binding. |
| `validate` / `verify` | Means source, schema, canonical form, pin, or file-digest checks performed by the static self-check. |
| `sealed` | Applies only after adjacent sidecar creation and grants no chain, result, authorization, or proof authority. |

TRUST_ROOT = single definition, digest everywhere (+10 sites)
SELF_CHECK = passed (+site agreement shown: definition=manifests=main_receiver=T0_T4=child_rows=producer_runtime=producer_T0_T4=verifier_receiver=terminal_runtime=terminal_T0_T4=7a80a5d52fd35701d8da02239178f63ef80e4f80ce8557636db99a326cf4c73c)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN / (+define/compute limited to metadata SHA-256; compare/agree static; bind content-address metadata only; validate/verify structural; no chain result, authorization, or proof claimed)
