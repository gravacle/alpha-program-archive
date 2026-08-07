# STAGE 8 / TASK 6 / BUILD A — EVIDENCE DECLARED-ROOT FIX — LANE 2 V001

Lane: Lane 2, Builder A  
Relay: PASTE 658  
Context: Q-598 adjudication of the evidence-root meaning  
Scope: Builder A evidence manifest, P0 validation, producer corroboration, schemas, generators, and recursive package hashes only  
Authority claimed: none

```text
SPEC_V005_SHA256 = f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b
PRIOR_EVIDENCE_MANIFEST_SHA256 = dfb29bf2cbc32fd6d4e29421cddff312e10237321a90b76a071b83601406b8af
FINAL_EVIDENCE_MANIFEST_SHA256 = 3da1ab07c3d3c5d3a87064cbfe758f8227bf6e0dca553c37b38329d5342b71e8
DECLARED_ROOT = e7820ca54197fad36d8d2dc4ecad92db9e75d9be0087918d55cb322a6abd1c9a
PAYLOAD_ROWS = 10
CHAIN_INVOKED = false
```

## 1. Preflight and corrected reading

| Check | Result |
|---|---|
| Output collision | Artifact and sidecar were absent in the cleanroom and archive workspace immediately before creation. |
| Governing spec | V005 rehashed to `f8d1a7dc…`; §2.1 lines 285–302 define the content-root construction and P0 equality. |
| Prior package state | The PASTE 656 hashes were rechecked before the edit; the prior evidence manifest was `dfb29bf2…`. |
| Evidence payload census | Ten regular payload files exist; every byte string is still identical to its sealed source under the existing evidence self-check. |
| Chain state | `outputs/` and the normal, optimized, and verifier pycache directories contain no files. |

The corrected reading is plain: `evidence_root_sha256` is the content root declared by the P0-verified evidence manifest. It is not the SHA-256 digest of the evidence-manifest file.

The two values are intentionally distinct:

```text
evidence_manifest_sha256 = 3da1ab07c3d3c5d3a87064cbfe758f8227bf6e0dca553c37b38329d5342b71e8
evidence.declared_root   = e7820ca54197fad36d8d2dc4ecad92db9e75d9be0087918d55cb322a6abd1c9a
```

The first value remains the child-input integrity pin. The second is the value supplied in the parent-created verifier-manifest expectation.

## 2. P1 — manifest inventory and declared root

The manifest now has exactly these six top-level fields:

```text
check_records
declared_root
fixture_records
payload_inventory
schema
subject_lineage_root
```

`payload_inventory` is sorted by its declared `relative_path`. Each row has exactly `{relative_path, byte_length, sha256}`. The declared paths are the content-addressed filenames relative to the evidence payload set; no ambient or absolute directory name participates in the root.

| Declared relative path | Bytes | SHA-256 |
|---|---:|---|
| `0322763ac48a4428b432124a6947da81826a41f612efa6803ee9a87317929b98--BID_CHARGED_CELLULAR_CPT_INTERTWINER_DERIVATION_V001.md` | 8,478 | `0322763ac48a4428b432124a6947da81826a41f612efa6803ee9a87317929b98` |
| `414067e25dbae39f7767d57144c953a0f98bb11d4c34178ec70097efabc0ebf7--STAGE8_TASK6_A21_OPEN_LEG_DISPOSITION_LANE2_V001.md` | 6,045 | `414067e25dbae39f7767d57144c953a0f98bb11d4c34178ec70097efabc0ebf7` |
| `5c679e3741abe782688b8a75ffa1928c308775248e41af192d03976f01cb4dbf--BID_SOURCE_PARENT_CLOSURE_GATE_V003.md` | 10,997 | `5c679e3741abe782688b8a75ffa1928c308775248e41af192d03976f01cb4dbf` |
| `76589e94bb4af318880c61c3d677dc2518add8480100a7afaf675e4dd3a394a8--STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V005.md` | 78,368 | `76589e94bb4af318880c61c3d677dc2518add8480100a7afaf675e4dd3a394a8` |
| `9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311--STAGE7_PACKET_MANIFEST_V001.sha256` | 13,786 | `9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311` |
| `a83289e67615d6faa2c1c942105ee6b595034f78d31fcf4e16ac5366fd1d7743--STAGE8_TASK6_LP_MATRIX_LEDGER_REVIEW_DARIO_V001.md` | 18,647 | `a83289e67615d6faa2c1c942105ee6b595034f78d31fcf4e16ac5366fd1d7743` |
| `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a--BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` | 78,794 | `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a` |
| `bc6c3e496ffd6e8d06cc3237e47a6a02b76faaa88b63b0ffb38684971c2d1362--STAGE8_TASK6_LP_MATRIX_LEDGER_LANE3_V001.md` | 51,952 | `bc6c3e496ffd6e8d06cc3237e47a6a02b76faaa88b63b0ffb38684971c2d1362` |
| `c09f2c246c48ddfd0df127da26a22f08ba9ffd44f5c2118c178a0a5eba5d00e8--BID_FULL_STACK_REVIEW_LEDGER_V003.md` | 24,108 | `c09f2c246c48ddfd0df127da26a22f08ba9ffd44f5c2118c178a0a5eba5d00e8` |
| `f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b--STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md` | 162,641 | `f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b` |

Independent derivation used the literal V005 construction:

```text
SHA256(
  "A35-CONTENT-ROOT-v1\0" ||
  concat(sort(relative_path || NUL || decimal_byte_length || NUL || lowercase_sha256 || LF))
)
= e7820ca54197fad36d8d2dc4ecad92db9e75d9be0087918d55cb322a6abd1c9a
```

The filename-relative declaration preserves the adjudicated `e7820ca5…` reading. The base is no longer underdetermined: these ten declared strings are the root inputs and therefore the law for this manifest.

## 3. P2 — parent binding and P0 verification

`parent.py` now performs the following fail-closed sequence before accepting a verifier manifest:

1. Verify every normal-manifest package row by byte length and SHA-256.
2. Strict-parse the structural-evidence manifest and require its tight canonical bytes.
3. Require the six exact top-level fields and the evidence-manifest schema identifier.
4. Require a canonically ordered inventory, exact three-field rows, unique basename-relative paths, decimal nonnegative byte lengths, and lowercase 64-hex digests.
5. Recompute the V005 content root from the declared row strings and compare it to `declared_root`.
6. Match every declared row one-for-one to the already parent-verified `inputs/evidence/` package row and verify its supplied bytes again against the declared length and digest.
7. Read the now-P0-verified `declared_root` and use that value as `verifier_expected_roots["evidence_root_sha256"]`.

The verifier expectation is never formed from a directory listing. Directory text does not participate in the root. The parent uses the closed, already hash-verified package rows only to establish that each declared row corresponds to the supplied bytes.

`producer.py` independently enforces the same six evidence fields, inventory ordering, row form, content-root equality, and one-for-one binding to its parent-verified child-manifest package rows. This corroboration does not replace the parent's P0 gate.

## 4. Disclosed finite delta — ten files

| File | Before bytes / SHA-256 | After bytes / SHA-256 | Disclosed change |
|---|---|---|---|
| `parent.py` | 36,405 / `7a1b35d013875b0f711155f16122b3098022894d7f3730859b13bd3a98e2d638` | 39,480 / `a3833419dcf08b522f9005762b14f9960ed1267a849b44115cfd91edd66f2040` | Add strict inventory/content-root/P0 validation and bind the verifier expectation to the returned manifest `declared_root` instead of `evidence_manifest_sha256`. |
| `producer.py` | 39,558 / `4297670d4df7a7c9083ec62aba0354538605f44829c2df749e99e93324e6bc44` | 41,324 / `14a679f75a15b96f93e70685ff422fbc74465038f8ae68b95ca3df16b8d76b45` | Add independent evidence inventory, content-root, and child-package binding checks. |
| `tools/assemble_evidence.py` | 13,573 / `025d9a083f2ef7e46ab4cc70944dfda65d59b21e8d532f6f1a77ccde67c6a8fd` | 14,212 / `ce7bcf0d7fac3906a09a93fb8d0f37937c625906310bd59ca133f808817e1286` | Generate the sorted ten-row payload inventory and its V005 content root. |
| `tools/materialize.py` | 30,620 / `abcea45941b51e6705bac84c07e0e258b3a3b3fbdd42521fba9e9e4dfd18ea82` | 31,300 / `94f63527cdbc5b2ad8235806bc4ee23495d89c78efddf16fcbf95268909507e7` | Materialize/validate the two new evidence fields, closed row schema, declared root, and declared-row-derived runtime payload paths. |
| `tools/self_check.py` | 23,638 / `c0df80441f34b42737937c2d89fb6386cd6cba7ee2fbd4e6e10676428d733913` | 24,554 / `fc0d9f4ef64a770d5f0bafadaaaff569e547844fc9f7cbe828473ab8a7ec8117` | Check the exact inventory, independent content-root derivation, and the parent's declared-root receiver. |
| `inputs/structural_evidence_manifest.json` | 98,662 / `dfb29bf2cbc32fd6d4e29421cddff312e10237321a90b76a071b83601406b8af` | 101,037 / `3da1ab07c3d3c5d3a87064cbfe758f8227bf6e0dca553c37b38329d5342b71e8` | Add `payload_inventory` with ten rows and `declared_root=e7820ca5…`; all 56 check records and three fixture records retain their prior evidence status/content. |
| `schemas/structural-evidence.schema.json` | 350 / `70b8cd958ec74c84be7c1ee062cafdad17d340b29b5d27e5b78a6f94ddc09740` | 735 / `d6e0d92c878b7c45da3d47abb423a920e849ca52f50fe4abc0e8a03efaa43dc0` | Require `declared_root` and a closed array of exact `{byte_length,relative_path,sha256}` rows. |
| `manifests/normal.json` | 9,171 / `75ea0020f8a1808269aa87b04f30f059643816abb28a6209cb935a5b7bed5e48` | 9,172 / `25d9495ff04d0f7f849b79c3e614468f1ff8d9b1f3379ea87cb49c74795dab12` | Recursively update parent, producer, evidence-manifest, and structural-schema rows and hashes. |
| `manifests/optimized.json` | 9,180 / `04af62ff4b1706276e157a773a9fc3b39672050ac0561259bb7c9d7353eaabed` | 9,181 / `29592726fd7f099211e4c6a6a882d006e7b93a58bd8a8e6eed7ae3c2afbc33fd` | Same closed package delta for optimized mode. |
| `manifests/package_inventory.json` | 5,511 / `65f3c45da98cf8c5dbbf16c61dddc13ebd55967140444c9264e4dcf20ccedd57` | 5,512 / `041a9c7de586469cc6eb18cbaf6ec2ed7e7bed381e4fbfbae3801c5c474ff498` | Recursively update all five edited Python/tool rows and five regenerated JSON rows. |

No other package file changed. The check map, fixture manifest, subject-lineage manifest, the other eight schemas, `README.md`, and all ten evidence payloads retained their bytes. The normal and optimized manifests each contain 25 package rows; `package_inventory.json` contains 31 rows and remains external to its own inventory.

## 5. Static self-check transcript

Only evidence-manifest assembly, deterministic package materialization, source compilation, canonical JSON/schema validation, and hash/inventory checks ran. Neither parent nor producer was invoked, and no check executor, fixture, verifier, or full chain ran.

```text
$ /usr/bin/python3 -I -S -B -c '<compile five Python sources>'
compile=5/5

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/assemble_evidence.py
{"authored_payload_bytes": 0, "checks_absent": 56, "checks_populated": 0, "declared_root": "e7820ca54197fad36d8d2dc4ecad92db9e75d9be0087918d55cb322a6abd1c9a", "fixtures_absent": 3, "fixtures_populated": 0, "payload_files": 10, "search_scope_members": 120, "search_scope_sha256": "691e871e4b2a13f09cdf5481abb1c7a32c05ba9426bf657436a5f5f2597db032"}

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/materialize.py
{"checks": 66, "fixtures": 6, "gated": 10, "normal_sha256": "25d9495ff04d0f7f849b79c3e614468f1ff8d9b1f3379ea87cb49c74795dab12", "optimized_sha256": "29592726fd7f099211e4c6a6a882d006e7b93a58bd8a8e6eed7ae3c2afbc33fd", "structural": 56, "subject_lineage_root": "d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688"}

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/self_check.py
SELF_CHECK_OK syntax=5 canonical_json=all schemas=9 inventory=31 evidence_payloads=10 evidence=0/56 absent=56 fixture_obs=0/3 checks=66 structural=56 gated=10 fixtures=6 fixture_fields=16 child_fields=14 verifier_manifest_fields=11 exits=0/1/2 chain_invoked=false

INDEPENDENT_ROOT_OK rows=10 canonical=true
declared_root=e7820ca54197fad36d8d2dc4ecad92db9e75d9be0087918d55cb322a6abd1c9a
normal package_rows=25 evidence_manifest_sha256=3da1ab07… declared_root=e7820ca5…
optimized package_rows=25 evidence_manifest_sha256=3da1ab07… declared_root=e7820ca5…
```

## 6. PIN CHECK, fences, and verb audit

### 6.1 PRE-SEAL PIN CHECK

| Pin or invariant | Final result |
|---|---|
| V005 | `f8d1a7dc…`, exact and unchanged. |
| Evidence root law | V005 §2.1 lines 285–302 re-read; root domain and delimiter sequence match exactly. |
| Evidence manifest | Tight canonical bytes; six exact fields; ten ordered rows; file digest `3da1ab07…`. |
| Declared root | Independent recomputation equals `e7820ca54197fad36d8d2dc4ecad92db9e75d9be0087918d55cb322a6abd1c9a`. |
| Supplied bytes | Ten/ten declared rows match their parent-verified package rows by path declaration, byte length, and SHA-256. |
| Parent receiver | Static source check finds `"evidence_root_sha256": evidence_declared_root`; the returned value is read from the P0-verified manifest. |
| Runtime manifests | `25d9495f…` / `29592726…`; 25/25 package rows independently rehashed in each. |
| Package inventory | 31/31 declared rows rehashed; inventory digest `041a9c7d…`. |
| Output collision | Artifact and sidecar absent in cleanroom and archive immediately before creation. |
| Chain products | Output and all three pycache directories remain empty. |

### 6.2 Fences

No evaluator component ran. No member was bound; no fixed point or end test ran; no physical quantity was evaluated; and no measured constant was read or compared. `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false`.

### 6.3 Self verb audit under the verdict-line scope rule

| Verb | Scoped meaning |
|---|---|
| `declared` | The ten displayed relative-path strings, lengths, and digests are fields of this specific structural-evidence manifest. |
| `verified` / `P0-verified` | Static canonical/schema/root/byte-binding validation defined in §3; no structural criterion or physical result was run. |
| `binds` | The parent assigns the manifest's validated `declared_root` to the verifier-manifest expected field; it does not claim verifier agreement. |
| `passed` | The displayed static compilation, schema, canonical, inventory, and hash checks only. |
| `sealed` | Applies only after adjacent sidecar creation and grants no chain, result, or proof authority. |

MANIFEST = inventory rows + declared_root (+e7820ca54197fad36d8d2dc4ecad92db9e75d9be0087918d55cb322a6abd1c9a)
PARENT = binds declared_root
SELF_CHECK = passed
DELTAS = 10 disclosed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN / (+declared/P0/binds/pass scopes; no chain, result, authorization, or proof claimed)
