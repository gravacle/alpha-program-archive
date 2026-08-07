# STAGE 8 / TASK 6 / BUILD A — AUTHORIZATION-CHECK FIX AND AUTHORED-EXPECTATION AUDIT — LANE 2 V001

Lane: Lane 2, Builder A  
Relay: PASTE 653  
Scope: authorization preflight repair, expected-content audit, static regeneration only  
Authority claimed: none

```text
REGISTER_HEAD = Q-592 (registrar-sealed cleanroom snapshot)
REGISTER_SNAPSHOT_SHA256 = 6e9d1fa193f71ae82a37f25334d6987a692ca4a7447bceefb2e613ca4dd5101e
AUTHORIZATION_SHA256 = ff84c4a8ba5c7f8eabfbcc587475d3a5050c21d758a2788c5b9e28b7ee022340
SPEC_V005_SHA256 = f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b
RUNTIME_SNAPSHOT_SHA256 = 50a6fc141a45451678aa7543e4f267ce26beb6e53182170b478acb6fb0e0f5bb
RUNTIME_GATE_SHA256 = 2ad7f72a88184c11e1253f2c47598fca11e60d05e8e71a26db4e19b16bf98d42
CHAIN_INVOKED = false
```

## 1. Preflight

| Check | Result |
|---|---|
| Register head | `REGISTER_HEAD_SNAPSHOT_Q592_2026-08-07.md` rehashed to `6e9d1fa1…`; its text states `HEAD = Q-592`. Its sidecar contains that exact digest. |
| Output collision | This artifact and its sidecar were absent in both the cleanroom and archive immediately before creation. |
| Authorization decision | Rehashed to the required `ff84c4a…` before inspection. |
| Governing spec | V005 rehashed to `f8d1a7dc…`. |
| Runtime subjects | Snapshot and gate rehashed to `50a6fc14…` and `2ad7f72a…`. |
| Prior package state | The sealed D1 evidence-assembly artifact rehashed to `4fa13ab7…`; its package inventory supplied the exact before-state hashes below. |

## 2. H1 — authorization repair

The selected repair is **hash-pin-only**. `parent.py` now executes

```python
verify_bytes(args.authorization, AUTHORIZATION_SHA256)
```

and performs no decoded-content search over the authorization decision. The old `validate_authorization` function and its `AUTHORIZATION_CONTENT` failure path are deleted.

This is the BR-1-clean form because the full-file SHA-256 binds every byte of the sealed decision. Searching those already-bound bytes for independently typed prose or embedded digests adds a second, fallible expectation without strengthening identity. The first invocation demonstrated the failure mode: the code required

```text
Builder A               = Codex Lane 2 (parent + producer)
```

while the sealed decision actually contains

```text
Builder A (producer + parent)  = Codex Lane 2   (GPT family)
```

The three digest-substring checks and the two other prose-substring checks were also removed from authorization validation. They happened to be present, but they were redundant once the full decision digest had passed.

The static self-check now fails if the deleted function, the deleted failure label, or the convicted paraphrase returns, and it separately requires the direct authorization hash-pin call.

## 3. H2 — authored-expectation audit

### 3.1 Audit boundary and method

For this audit, an **expected-content literal** is a string or digest value that code searches for inside a decoded or textual field originating in a content-addressed external source. Closed-JSON field names, schema discriminants, enum values, descriptor opcodes, and internal result/status tags are interface grammar, not claims that prose bytes contain a sentence. Those interface values remain bound through their closed schemas and sealed V005/addendum contracts; they were reviewed separately and no mismatch was found.

The audit enumerated every comparison and membership operation in `parent.py` and `producer.py`, traced operands back to external byte buffers or content-addressed descriptor text, and then fixed-string checked each content literal at the stated source pin. This produced eight content literals: six in the former authorization validator, one runtime-gate token, and one descriptor-predicate token. `producer.py` contains no other search against sealed prose bytes.

### 3.2 Complete expected-content table

| # | Literal compared by code | Pinned source | Verbatim at pin before repair? | Final disposition |
|---:|---|---|---|---|
| 1 | `f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b` | authorization decision `ff84c4a…` | YES, decision line 8 | Removed as redundant decoded-content expectation; full decision hash remains enforced. |
| 2 | `50a6fc141a45451678aa7543e4f267ce26beb6e53182170b478acb6fb0e0f5bb` | authorization decision `ff84c4a…` | YES, decision line 23 | Removed as redundant decoded-content expectation. Runtime snapshot retains its independent input hash pin. |
| 3 | `2ad7f72a88184c11e1253f2c47598fca11e60d05e8e71a26db4e19b16bf98d42` | authorization decision `ff84c4a…` | YES, decision line 25 | Removed as redundant decoded-content expectation. Runtime gate retains its independent input hash pin. |
| 4 | `Builder A               = Codex Lane 2 (parent + producer)` | authorization decision `ff84c4a…` | **NO**; the exact decision line is displayed in §2 | Removed with the entire prose validator; this is the one non-verbatim finding. |
| 5 | `10 GATED-EXECUTION checks` | authorization decision `ff84c4a…` | YES, decision line 12 | Removed as redundant decoded-content expectation. |
| 6 | `return NOT_RUN_GATE by construction` | authorization decision `ff84c4a…` | YES, decision line 13 | Removed as redundant decoded-content expectation. |
| 7 | `fresh` | runtime gate `2ad7f72a…` | YES, including gate lines 9, 11, 14, 35, 99, and 113 | Retained. It is a verbatim token in the independently hash-pinned runtime gate. |
| 8 | `hits=empty` | V005 `f8d1a7dc…` descriptor predicates | YES, including descriptor lines 547, 572, 573, 580, 583, 584, 591, 595, 607, and 608 | Retained. It is a verbatim predicate fragment; producer removes only spaces before the test. |

Result: eight expected-content literals checked, one non-verbatim, and that one is removed. No non-verbatim expected-content literal remains in `parent.py` or `producer.py`.

### 3.3 Structured-contract cross-check

The audit did not silently discard structured comparisons. Their receiving contracts were checked as follows:

| Carrier | Code-side values | Authority checked | Result |
|---|---|---|---|
| Runtime snapshot | `gravacle.content-addressed-runtime.v012`; `-I/-S/-B`; optimization levels `0/1`; `direct-script-no-c-no-m` | Snapshot `50a6fc14…` and V005 runtime pin | Exact values present. |
| Child manifests | `rd22.child-manifest.v001`; `normal`; `optimized` | Closed child-manifest schema and V005 R0/R1 contract | Exact values present. |
| Producer receipt/output | `rd22.child-receipt.v001`; `rd22.producer-output.v001`; structural/gated status vocabulary | Closed package schemas, V005 §§9.2–9.4 | Exact values present. |
| Verifier manifest | `rd22.verifier-manifest.v001`; `canonical-json`; exits `0/1/2` | Addendum `d17c5e79…` §3 and closed verifier-manifest schema | Exact values present. |
| Verifier stdout | `gravacle.a35.verifier-verdict.v1`; `VERIFIED`; `FAIL` | Sealed Builder B public carrier and closed local verifier-output schema | Exact values present. |
| Descriptor opcodes | Closed V005 opcode vocabulary, including structural-only rejection of `SYMBOLIC` and `SPECTRAL` | V005 `f8d1a7dc…` and `check_map.json` `034ebf3e…` | Exact values present; no decoded-prose expectation. |

## 4. Disclosed delta

Five files changed from the sealed D1 package state. No other package file changed.

| File | Old state | New state | Reason |
|---|---|---|---|
| `parent.py` | 36,986 bytes; `f07016cb7054d3696cd6e0f7552f81e74b8ee0f35cf8b55b7bd771e633b21831` | 36,465 bytes; `da0c9c4a060985cd39582081e1d5ee0874c91fc6d41bc37385a329eaf42e77b7` | Two hunks: delete the 15-line authorization-content validator; replace its two-line call site with the direct hash-pin call. Net 1 insertion / 15 deletions. |
| `tools/self_check.py` | 23,114 bytes; `d10e40432f9f995105f78f1323d586054e8ba206aaba056b0765b5ceebdb2baf` | 23,649 bytes; `74050e4444550a51cfadf2e35cfdb342989d90dafb823ac3d78f726b513d1437` | Add regression checks forbidding the authored expectation and requiring the authorization hash-pin call. |
| `manifests/normal.json` | 9,172 bytes; `7697fb8c20d8b0589247c352d93dc91e4cc6351f570a8b8ba6e739567f1dee40` | 9,172 bytes; `f8c9f05b01203d53da7baf90b7dc8f658485e9019fcfbea4abe722b3bce4723e` | Regenerated package inventory row for the changed parent. |
| `manifests/optimized.json` | 9,181 bytes; `8449ac7d29ba7a1297f183949d75826e45ede86249af9940ec9e75cba5780cbe` | 9,181 bytes; `5484bcdbe64c7a2eb3e48a616150b40b8e5f1cc2a192779a85ea4677a5749a3b` | Same parent-row regeneration in optimized mode. |
| `manifests/package_inventory.json` | 5,512 bytes; `80b71e4639b248d25c87b3221db2977c9e4b92c3af6e1ebe49c93f8829da8489` | 5,512 bytes; `ea927eb8f3db513aa33cff6464cc47984bafab2ac3f523c6a8699f3de08cf7d5` | Regenerated hashes for parent, self-check, and both child manifests. |

`producer.py` is byte-identical at `93d717df…`. The evidence manifest, evidence payloads, check map, fixtures, schemas, materializer, and subject-lineage root are unchanged.

## 5. Updated inventory and hashes

`package_inventory.json` contains 31 self-addressed rows and excludes itself. Its separately displayed digest gives 32 delivered package files.

| Relative path | Bytes | SHA-256 |
|---|---:|---|
| `README.md` | 3516 | `13634ef622aeae92ac69e790fee5aba86b67cafdda0321b1c1f9d3382b1611c7` |
| `checks/check_map.json` | 107235 | `034ebf3e071051d25d5b7f8871a03193da5bc9ab16a7c07c7cae1bbb8f467e26` |
| `fixtures/fixture_manifest.json` | 7894 | `dc635a83fe39e62bdc2b76c8c40cfce977ac67fdaf0eede32344d0b98dabf2db` |
| `inputs/evidence/0322763ac48a4428b432124a6947da81826a41f612efa6803ee9a87317929b98--BID_CHARGED_CELLULAR_CPT_INTERTWINER_DERIVATION_V001.md` | 8478 | `0322763ac48a4428b432124a6947da81826a41f612efa6803ee9a87317929b98` |
| `inputs/evidence/414067e25dbae39f7767d57144c953a0f98bb11d4c34178ec70097efabc0ebf7--STAGE8_TASK6_A21_OPEN_LEG_DISPOSITION_LANE2_V001.md` | 6045 | `414067e25dbae39f7767d57144c953a0f98bb11d4c34178ec70097efabc0ebf7` |
| `inputs/evidence/5c679e3741abe782688b8a75ffa1928c308775248e41af192d03976f01cb4dbf--BID_SOURCE_PARENT_CLOSURE_GATE_V003.md` | 10997 | `5c679e3741abe782688b8a75ffa1928c308775248e41af192d03976f01cb4dbf` |
| `inputs/evidence/76589e94bb4af318880c61c3d677dc2518add8480100a7afaf675e4dd3a394a8--STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V005.md` | 78368 | `76589e94bb4af318880c61c3d677dc2518add8480100a7afaf675e4dd3a394a8` |
| `inputs/evidence/9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311--STAGE7_PACKET_MANIFEST_V001.sha256` | 13786 | `9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311` |
| `inputs/evidence/a83289e67615d6faa2c1c942105ee6b595034f78d31fcf4e16ac5366fd1d7743--STAGE8_TASK6_LP_MATRIX_LEDGER_REVIEW_DARIO_V001.md` | 18647 | `a83289e67615d6faa2c1c942105ee6b595034f78d31fcf4e16ac5366fd1d7743` |
| `inputs/evidence/aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a--BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` | 78794 | `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a` |
| `inputs/evidence/bc6c3e496ffd6e8d06cc3237e47a6a02b76faaa88b63b0ffb38684971c2d1362--STAGE8_TASK6_LP_MATRIX_LEDGER_LANE3_V001.md` | 51952 | `bc6c3e496ffd6e8d06cc3237e47a6a02b76faaa88b63b0ffb38684971c2d1362` |
| `inputs/evidence/c09f2c246c48ddfd0df127da26a22f08ba9ffd44f5c2118c178a0a5eba5d00e8--BID_FULL_STACK_REVIEW_LEDGER_V003.md` | 24108 | `c09f2c246c48ddfd0df127da26a22f08ba9ffd44f5c2118c178a0a5eba5d00e8` |
| `inputs/evidence/f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b--STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md` | 162641 | `f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b` |
| `inputs/structural_evidence_manifest.json` | 98663 | `722f4db56fc6e77de258273f06fd1ae487b9bb0143440f73adb76747779a5cb8` |
| `inputs/subject_lineage_manifest.json` | 1510 | `e6918e0254d63671dd0fd3652290e4a0b1781abb6c4d63e81043f1d8f3327d54` |
| `manifests/normal.json` | 9172 | `f8c9f05b01203d53da7baf90b7dc8f658485e9019fcfbea4abe722b3bce4723e` |
| `manifests/optimized.json` | 9181 | `5484bcdbe64c7a2eb3e48a616150b40b8e5f1cc2a192779a85ea4677a5749a3b` |
| `parent.py` | 36465 | `da0c9c4a060985cd39582081e1d5ee0874c91fc6d41bc37385a329eaf42e77b7` |
| `producer.py` | 39567 | `93d717df36807e66ca09919ca90157e79b016831e5200852350d8887a57c3982` |
| `schemas/check-map.schema.json` | 456 | `8e971040ca4d96161303710bc391dd322cb581983c881eaf39b1547fb4e68192` |
| `schemas/child-manifest.schema.json` | 1420 | `f5325b40cd49db94e11cc44628ec46b6ac400489d99c574642461e0b8697ef1e` |
| `schemas/child-receipt.schema.json` | 1277 | `0ce216024263ee7b2de3643fc4b44cc1a581d7a2334968da8ebdf8b9d02fa7bf` |
| `schemas/fixture-manifest.schema.json` | 1347 | `3723297f9f9e9aa5b6e16f35a3315966d49997734c223580807b916ebfc4e986` |
| `schemas/producer-output.schema.json` | 2425 | `d3e4dc5c32e265ec5a8373b734f9d277573d862c97cb563f03c3e97f55e534b3` |
| `schemas/structural-evidence.schema.json` | 351 | `5d3ec96abcec19f664665f5a1bf316a9c4fa3d95aa66b8551de8036d85f97174` |
| `schemas/terminal-ledger.schema.json` | 3920 | `5635e68e13932915f6724f7a1aa2533fa52d8cc7170be9a44f09433ae9816af5` |
| `schemas/verifier-manifest.schema.json` | 1691 | `05cb23509293da9d8a184cd48a7f6cc1c36e56c3ab4114d8548bea8824fc9d15` |
| `schemas/verifier-output.schema.json` | 1476 | `145dfdf6aefa40766b9e680dd59714ffbd94133411ea89a0e7d7aab8d6f033ad` |
| `tools/assemble_evidence.py` | 13582 | `11addee3e9e9764fee711cf4b136bca003948c152f3f04ee8ba4c1cde88cd1a4` |
| `tools/materialize.py` | 30629 | `ba3c3ae4e825f3044ae4c9e781dbe1fb096443bc3dc1603b0223c14e129957d3` |
| `tools/self_check.py` | 23649 | `74050e4444550a51cfadf2e35cfdb342989d90dafb823ac3d78f726b513d1437` |
| `manifests/package_inventory.json` (self, excluded from its own rows) | 5512 | `ea927eb8f3db513aa33cff6464cc47984bafab2ac3f523c6a8699f3de08cf7d5` |

## 6. Static self-check transcript

Only deterministic materialization, syntax/schema validation, hashing, and source inspection ran. The parent, producer, check executors, fixtures, and verifier did not run.

```text
$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/materialize.py
{"checks": 66, "fixtures": 6, "gated": 10, "normal_sha256": "f8c9f05b01203d53da7baf90b7dc8f658485e9019fcfbea4abe722b3bce4723e", "optimized_sha256": "5484bcdbe64c7a2eb3e48a616150b40b8e5f1cc2a192779a85ea4677a5749a3b", "structural": 56, "subject_lineage_root": "d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688"}

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/self_check.py
SELF_CHECK_OK syntax=5 canonical_json=all schemas=9 inventory=31 evidence_payloads=10 evidence=0/56 absent=56 fixture_obs=0/3 checks=66 structural=56 gated=10 fixtures=6 fixture_fields=16 child_fields=14 verifier_manifest_fields=11 exits=0/1/2 chain_invoked=false
```

The check confirms canonical JSON, all package hashes, closed schemas, 66 = 56 structural + 10 gated descriptors, empty output/pycache directories, the evidence census, no load-bearing Python `assert`, absence of the convicted authorization expectations, and presence of the direct authorization hash pin.

## 7. PIN CHECK, fences, and verb audit

### 7.1 PRE-SEAL PIN CHECK

| Pin or invariant | Final check |
|---|---|
| Q-592 snapshot | Artifact digest `6e9d1fa1…`; sidecar content agrees. |
| Authorization decision | `ff84c4a8…`, exact immediately before artifact creation. |
| V005 / integration addendum | `f8d1a7dc…` / `d17c5e79…`, exact and unchanged. |
| Runtime snapshot / gate | `50a6fc14…` / `2ad7f72a…`, exact and unchanged. |
| Prior D1 certificate | `4fa13ab7…`, exact; its sidecar records that digest. |
| Normal/optimized manifests | `f8c9f05b…` / `5484bcdb…`; regenerated from the final parent bytes. |
| Package inventory | 31 declared rows rehashed; self digest `ea927eb8…`. |
| Output collision | Clear in cleanroom and archive immediately before this artifact was created. |
| Chain products | Output directory and all three pycache directories remain empty. |

### 7.2 Fences

No check, fixture, parent, producer, or verifier executed. No member was bound; no fixed point or end test ran; no physical quantity was evaluated; and no measured constant was read or compared. `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false`. No fence blocked this structural repair, so `MACHINERY_APPEAL = none`.

### 7.3 Self verb audit under the verdict-line scope rule

| Verb | Scoped meaning |
|---|---|
| `fix` | The parent no longer rejects the exact pinned authorization decision because of an authored prose expectation. This does not claim a successful chain invocation. |
| `hash-pin-only` | The exact decision bytes must hash to `ff84c4a8…`; it does not mean authorization is inferred from a filename or path. |
| `audit` | Complete for code literals searched in external content by `parent.py` and `producer.py`, with structured interface grammar separately cross-checked. |
| `passed` | Applies only to the displayed static syntax/schema/hash/inventory check. |
| `sealed` | Applies only after adjacent sidecar creation; it grants no execution or proof authority. |

FIX = hash_pin_only (+full-file digest binds every decision byte; redundant decoded-content expectations removed)
AUDIT = 8 literals checked (+non-verbatim count 1, all fixed)
SELF_CHECK = passed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN / (+hash-only authorization identity; complete expected-content scope; static-only pass; authorization not claimed)
