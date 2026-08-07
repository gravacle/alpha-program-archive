# STAGE 8 TASK 6 — BUILDER A DESCRIPTOR-BOUNDARY AND EVENT-PAYLOAD CORRECTION

**Lane:** Codex Lane 2 / Builder A  
**Date:** 2026-08-07  
**Disposition:** COMPLETE  
**Scope:** sealed-descriptor byte boundaries, six event-ledger payload carriers, derived package pins, and static validation  
**Authority:** RD-22 implementation only; no scientific, proof, or seal authority claimed

## 1. Pins and bounded diagnosis

The governing specification was verified before derivation:

```text
STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md
SHA-256 f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b
```

The comparison base is the Builder A package sealed with `STAGE8_TASK6_ROOT_MEMBERSHIP_LANE2_V001.md`, SHA-256 `792db074b65079c62b41285021dcdb9a6f158bcf655fe16bec30864fca6f73fa`. Its sidecar has SHA-256 `e005306fbf86fb2141cf90522d3c04b22f85345b1f3d95aabe60b35fe6c8190d` and names the artifact digest correctly.

Run 021 was read only as the fault observation. Its relevant local artifacts are:

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `rd22_run_021/verifier.output.json` | 24,554 | `81084fb5053e480fca3019ee96d5768192046fee8ae350b658b7905ef86da5b0` |
| `rd22_run_021/producer.ledger.json` | 118,027 | `f7578b63c5f9069685a20ff5cfc0632e659bff23bc84903f6bcd3ac4262cf562` |
| `rd22_run_021/normal.receipt.json` | 24,974 | `dbfb84673f3b2edcc104c5ef6aab24af3e3c3552db204c969e8dbcf7b6acb721` |
| `rd22_run_021/optimized.receipt.json` | 24,992 | `f9fe87e91164d37cb67a32ddcd43fc37028d7cb875e436a77c865daa085962e5` |

The observation contained 66 `DESCRIPTOR_DIGEST` findings and two early `EVENT_LEDGER` fetch failures. Builder B's code and digest list were not read or copied. All replacement descriptor values were derived independently from the sealed specification bytes.

## 2. Descriptor boundary correction

### 2.1 Derivation

`tools/materialize.py` now performs the following byte procedure:

1. read the pinned specification bytes;
2. identify the closed 66-row descriptor census through the existing five-column table parser and execution-class filter;
3. take the exact UTF-8 bytes of each Markdown row body returned by `splitlines()`;
4. hash that body without appending `LF`, `CR`, or `CRLF`;
5. place the same body digest in `descriptor_sha256` and `descriptor_bytes_sha256`.

The declared convention is now:

```text
SHA256 of the exact UTF-8 Markdown descriptor row excluding its line terminator
```

For the three `C-D-*` descriptors whose source span is in the specification itself, the source-span endpoint was moved to the end of the row body so the recorded span likewise excludes the terminator. Blocker-ledger source spans remain unchanged.

The structural-evidence manifest's 56 structural `descriptor_sha256` references were regenerated from the new check map. No evidence availability, payload byte, search record, fixture observation, or subject-lineage root changed.

### 2.2 Independent boundary check

The static checker reads the sealed specification as bytes and deliberately over-generates every displayed row beginning with each check ID. Four IDs have more than one displayed row elsewhere in the specification; the checker therefore requires exactly one body candidate to match the check-map digest rather than assuming the first display.

For every one of the 66 mapped descriptors it verifies:

- exactly one exact row-body candidate matches;
- the matched body ends in neither `CR` nor `LF`;
- the physical line has an observed `LF` or `CRLF` terminator;
- hashing `body + observed terminator` does not equal the declared digest;
- `descriptor_bytes_sha256 == descriptor_sha256`.

Result:

```text
mapped descriptors                 66
exact body matches                 66
terminator-covered map digests      0
descriptor_terminators_excluded 66/66
first derived value
  C-B-V008-01  bed9041f0fa42646120dbd4a9d3f377c1f03d94bb56113486586d3bf2fa9fe31
last derived value
  C-D-A35-03-PHYSICAL-RESIDUE  2c1baa1f1643d58fcf0ab5e58a677f43b0c26585b30b74d5045b592efb1346a8
```

These values are examples from the independently regenerated map, not a copied expected list.

## 3. Six event-ledger payload carriers

### 3.1 Closed carrier map

The parent now has one explicit six-class map:

| Child-row digest field | Receipt payload field | Materialized bytes |
|---|---|---|
| `module_ledger_sha256` | `module_ledger` | tight canonical JSON list |
| `native_ledger_sha256` | `native_ledger` | tight canonical JSON list |
| `open_event_ledger_sha256` | `open_event_ledger` | tight canonical JSON list |
| `process_event_ledger_sha256` | `process_event_ledger` | tight canonical JSON list |
| `network_event_ledger_sha256` | `network_event_ledger` | tight canonical JSON list |
| `mutation_event_ledger_sha256` | `mutation_event_ledger` | tight canonical JSON list |

For each receipt and each class, the parent now canonicalizes the actual list, computes its digest, exclusively creates `<digest>.json`, re-reads it, and requires both exact byte equality and digest equality. A pre-existing content-addressed path is accepted only when it is a regular non-symlink file with exactly the same bytes. Equal payloads across classes or children lawfully share one content-addressed file; absent and empty remain distinct, and an empty class is the two canonical bytes `[]` with digest `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`.

### 3.2 Run-root resolution

The prior verifier substitution pointed `${EVIDENCE_DIR}` at Builder A's immutable package. A run-scoped event list could therefore be declared by digest but could not lawfully be written at the fetch location.

The parent now:

1. requires `run_root/evidence` to be absent at R0;
2. creates it exclusively as a run-local directory;
3. copies every sealed structural evidence payload from the verified package into it byte-for-byte, preserving filenames and digests;
4. materializes all six event classes from each child receipt into the same run-local content-addressed directory;
5. binds `${EVIDENCE_DIR}` to that run-root directory before verifier launch;
6. adds every staged structural payload and event payload to the verifier-child content allowlist so later open-event classification remains digest-authoritative.

The declared structural evidence content root is unchanged: it remains the manifest-defined root over the ten sealed structural payload inventory rows. Run-scoped event files are additional digest carriers, not members silently added to that sealed structural inventory. The package receives no runtime writes.

The verifier child is handled by the same six-class materializer before its terminal child row is emitted. Thus both the pre-verifier producer ledger and the terminal ledger contain only child-row event digests whose canonical payload bytes have been materialized.

## 4. Static event-payload test

The self-check exercises the filesystem contract in a temporary directory only. It stages one synthetic sealed payload and provides six distinct synthetic event-class lists, with `native_ledger` empty. It requires:

- the parent carrier tuple to equal the six-field table above;
- all six digest fields to be returned;
- every `<digest>.json` file to exist;
- every file's bytes to equal the parent's tight canonical serialization;
- the empty file's bytes to be exactly `[]`;
- six distinct synthetic event files to be present;
- the parent source to bind `${EVIDENCE_DIR}` to `run_evidence_directory`, not the package directory.

Result: six of six classes materialized and bound. This was a synthetic static contract test; no producer, verifier, check executor, fixture, or subject lineage ran.

## 5. Complete disclosed delta

The base is the byte snapshot of the sealed 677 Builder A package taken before editing. Exactly eight package files changed; no package file was added or removed.

Diff conventions: unified-diff hunks; insertions and deletions count newline-delimited physical lines. Canonical JSON documents occupy one physical line, so a content change counts as one insertion and one deletion; byte lengths and SHA-256 digests are authoritative.

| File | Base bytes / SHA-256 | Final bytes / SHA-256 | Diff | Disclosed delta |
|---|---|---|---|---|
| `parent.py` | 62,956 / `31e4bccae6b30ca33d491f6a7a208e896c0fc9353a4e16188f6546374653badc` | 65,955 / `061a2a303bcdf3fae23100e79a3f03c182029f448bdad4cd18cfc3d10d91a509` | 8 hunks; +82/-12 | install six-class carrier map; stage immutable evidence into the run root; materialize/rehash event payloads; bind verifier to run-local evidence; allowlist staged files |
| `tools/materialize.py` | 31,681 / `33a00a8c8b7c3dada0cabaa3860c4c625e60ba45e07d1614a0d152de4193a948` | 31,878 / `1594c137d1e63825aeb1c3e3dca3601d2ccc9b292586dd5011dffe51eea7ef93` | 3 hunks; +6/-3 | exclude descriptor terminators; shorten the three specification-row spans; regenerate 56 evidence bindings |
| `tools/self_check.py` | 44,618 / `b9badc4b7054497813048bd70b9dc7f9e7bbc4bcd70cf13b3e79dc1edfc2eb3a` | 49,389 / `c4168e8cf37a635273e20cada8b3a6fb50a7c7e72e6fd3525e3c9908768b4370` | 8 hunks; +80/-9 | exact byte-boundary census; no-terminator guard; six-class synthetic materialization test; run-root receiver audit; transcript |
| `checks/check_map.json` | 107,234 / `0daa01f3c4f872b995cee1fef3c2dcb804cee11871b8c56fd22c14d89b1cff51` | 107,238 / `1197e8b8ebaef433bf5c96f83d4324e3f48e66fb6d4425c830c953b13317e7d0` | 1 hunk; +1/-1 | regenerate all 66 descriptor digests, convention, and three source endpoints |
| `inputs/structural_evidence_manifest.json` | 101,037 / `3da1ab07c3d3c5d3a87064cbfe758f8227bf6e0dca553c37b38329d5342b71e8` | 101,037 / `cbb85f6f2c2bae7fe50e2213a2c55a04ee93ac40a41755461faf81c3e34632b3` | 1 hunk; +1/-1 | refresh the 56 structural descriptor references only |
| `manifests/normal.json` | 8,951 / `fe3a0a27d90c6ced7a29bd75e049e567eb8d5fb5db34dc58724f597a8196e6a9` | 8,951 / `d35541620b3b75bebdd4c83aac161fd83c23675c0ec4e8748c5c1c0835c07c14` | 1 hunk; +1/-1 | refresh parent, check-map, and evidence-manifest pins |
| `manifests/optimized.json` | 8,960 / `fa8d36fc5a237ece34ceb24bd23e302d9d353d0a8bede366822786526710adb5` | 8,960 / `3d939a4bd6c875fff0fe15a2925c79eedcfe9b15c6f538a383d1952ecca11698` | 1 hunk; +1/-1 | refresh parent, check-map, and evidence-manifest pins |
| `manifests/package_inventory.json` | 5,361 / `53cf9ec36a1412b006cd28ee4f7f39b710bde52ccb4fe78626c27a4a54c4fddf` | 5,361 / `c1d1af4721952e6d12e312ae98b2948a0ff3e1a36aca32984c2fbb128f85a349` | 1 hunk; +1/-1 | refresh all changed-file and derived-manifest pins |

Total under the declared convention: 24 hunks, 173 inserted physical lines, 29 deleted physical lines. Every other Builder A package file is byte-identical to the sealed base snapshot.

## 6. Static transcript and idempotence

Only `tools/materialize.py` and `tools/self_check.py` ran under `/usr/bin/python3 -I -S -B`. The second materialization/self-check pass reproduced the first pass's bytes and hashes.

```text
MATERIALIZE_OK checks=66 fixtures=6 gated=10 structural=56
normal_sha256=d35541620b3b75bebdd4c83aac161fd83c23675c0ec4e8748c5c1c0835c07c14
optimized_sha256=3d939a4bd6c875fff0fe15a2925c79eedcfe9b15c6f538a383d1952ecca11698
subject_lineage_root=d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688

SELF_CHECK_OK syntax=5 canonical_json=all local_schemas=8
inventory=30 evidence_payloads=10 evidence=0/56 absent=56 fixture_obs=0/3
checks=66 descriptor_terminators_excluded=66/66 structural=56 gated=10 fixtures=6
event_payload_classes=6 event_payload_files=6(static_synthetic)
empty_event_bytes=[] run_evidence_base=run_root
producer_fields=13 receipt_fields=16 fixture_fields=16 child_fields=14
verifier_manifest_fields=11 exits=0/1/2 chain_invoked=false
```

Stable post-pass pins:

```text
checks/check_map.json                    1197e8b8ebaef433bf5c96f83d4324e3f48e66fb6d4425c830c953b13317e7d0
inputs/structural_evidence_manifest.json cbb85f6f2c2bae7fe50e2213a2c55a04ee93ac40a41755461faf81c3e34632b3
manifests/normal.json                    d35541620b3b75bebdd4c83aac161fd83c23675c0ec4e8748c5c1c0835c07c14
manifests/optimized.json                 3d939a4bd6c875fff0fe15a2925c79eedcfe9b15c6f538a383d1952ecca11698
manifests/package_inventory.json         c1d1af4721952e6d12e312ae98b2948a0ff3e1a36aca32984c2fbb128f85a349
```

The 30-file inventory validates. Package `outputs/` and all three `pycache/` directories remain empty.

## 7. PIN CHECK, battery, and verb audit

- The output artifact and sidecar names were absent in both the cleanroom and archive workspace before creation.
- The governing specification pin and sealed 677 base artifact pin verify.
- All 66 descriptor digests were derived from the governing specification bytes; no Builder B digest list was used.
- The no-terminator assertion is executable and reports 66/66 body-bound digests with zero terminator-covered map values.
- The event test verifies six declared classes, actual content-addressed files, exact canonical bytes, empty-list bytes, and run-root binding.
- Normal and optimized manifests carry identical package inventories and differ only in their already-lawful mode fields.
- Two static passes produced identical derived pins.
- This artifact is hashed only after its final byte is written; its `.seal.sha256` records that post-write digest. The registrar, not Builder A, mirrors it.

F_PLDEC: CLEAN. No physical quantity is present in either repaired path. Anti-tuning: CLEAN; the descriptor rule is uniform over the 66-row census, and the event materializer is uniform over the six closed carrier classes. M-2: fixed-string, whitespace, hyphen/space/underscore, and display-context checks were retained in the static battery.

Gate audit: `alpha_computed = false`; `proof_authorized = false`; `kappa_record_computed = false`. No member binding, fixed-point execution, end test, physical-quantity evaluation, or measured-constant comparison occurred.

Verb audit under the verdict-line scope rule: CLEAN. “Matches,” “verifies,” and “materialized” refer only to byte-level build and synthetic static-contract facts. No evaluator, check, fixture, proof, authorization, or scientific verdict is claimed.

DESCRIPTORS = 66 recomputed sans terminator (derived from spec bytes)
EVENT_PAYLOADS = 6 classes materialized at declared paths
SELF_CHECK = passed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
