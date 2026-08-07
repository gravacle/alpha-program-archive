# STAGE 8 / TASK 6 / BUILD A — PATH-IDENTITY FIX — LANE 2 V001

Lane: Lane 2, Builder A  
Relay: PASTE 663  
Context: Q-600, run 010 `MODULE_UNSEALED` disposition  
Scope: realpath identity, digest-authoritative allowlists, alias observations, alias-sensitive comparison audit, and recursive package hashes  
Authority claimed: none

```text
SPEC_V005_SHA256 = f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b
INTEGRATION_ADDENDUM_SHA256 = d17c5e79986bea431dec0b572019096f9c059bcc43876fda9134abc96ce0f260
PRIOR_PARENT_SHA256 = 0bbf493ac3df83ed70fd2b4a90f6cb535e5af093ce15d208bc15a15ae0343dff
FINAL_PARENT_SHA256 = 10ef12f2449d8694692c81492a208dfa179800722249d7010e536f995b3285bc
CHAIN_INVOKED = false
```

## 1. Preflight and finding

| Check | Result |
|---|---|
| Output collision | This artifact and its sidecar were absent in both the cleanroom and archive workspace immediately before creation. |
| Governing pins | V005 is `f8d1a7dc…`; the integration addendum is `d17c5e79…`; both exact. |
| Prior Builder A state | The archive copy of `parent.py` independently rehashed to `0bbf493a…`, matching the sealed PASTE 662 state. |
| Run-010 evidence | Both producer outputs and receipts exist. Each receipt has 84 module rows, zero native rows, 60 open rows, and the expected write/mutation rows. |
| Alias fact | `/Users/bgm/Documents/New project` is a symlink spelling whose realpath is `/Users/bgm/Documents/Documents - Brian’s MacBook Pro/New project`; the files are one filesystem object, not two trees. |
| Builder B pin | Its manifest and sidecar are `08e6c058…`; the verifier's ten source buffers recompute to its declared root `a8494992…`. |
| Chain state | No producer, verifier, check executor, fixture, or full chain was invoked in this relay. |

The former classifier resolved the observed module path but compared it with roots whose declared spelling had already been collapsed or omitted. In particular, the two producer calls supplied no package module root at all. That made the content-addressed `producer.py` row fail as `MODULE_UNSEALED` even though its receipt digest matched the manifest-pinned bytes.

The repair separates three facts:

```text
declared_path  = spelling retained from the sealed/input declaration
realpath       = canonical filesystem identity used on both sides
sha256         = authoritative byte identity
```

Realpath equality is necessary for path identity but never sufficient for content admission.

## 2. S1 — realpath on both sides, content authoritative

### 2.1 One normalization receiver

`lexical_absolute()` retains the absolute input spelling without following aliases. `real_path()` applies `os.path.realpath` to that spelling. `safe_resolve()`, root checks, run-path checks, ledger binding, and receipt classification all use this receiver; no legacy `.resolve()` call remains in the parent.

At load time, `add_allowlist_entry()` maps the realpath to a row containing:

```text
declared_path
realpath
sha256
source
```

Canonical collisions with different digests fail closed as `ALLOWLIST_COLLISION`.

### 2.2 Exact content allowlists

| Input class | Entries | Content receiver |
|---|---:|---|
| Builder A package | 25 | Each normal/optimized manifest row supplies the declared relative path and expected SHA-256; every row is rehashed before use. |
| Pinned Python runtime | 747 | `python_runtime_files` in snapshot V012 supplies every relative path and expected SHA-256; entries are realpath-normalized when loaded. |
| Builder B verifier | 10 | Every `verifier/*.py` source buffer is individually hashed; the sorted aggregate is independently recomputed and must equal `verifier_root_sha256`. |
| Child/run inputs | Dynamic, exact | Child manifest, output, receipt, specification, runtime snapshot, runtime gate, and post-production ledger receive their independently known digests. |

For module and native rows the parent now requires, in order:

1. observed path realpath identity with an admitted exact file (or the already pinned native-system trust roots);
2. receipt-carried SHA-256 equals a fresh read of the observed bytes;
3. for every exact allowlist file, that fresh digest also equals the independent sealed/runtime/run expectation.

For open-event rows, which carry no digest field, the observed file is freshly rehashed against the exact allowlist expectation. Write and mutation rows are compared by realpath and then the resulting output/receipt bytes are rehashed against the expected output/receipt digest. Therefore a path-spelling match with either a forged receipt digest or a wrong sealed digest remains a terminal failure.

### 2.3 Alias observations in the ledger

When the lexical declaration and observed spelling differ but their realpaths agree, the classifier emits:

```text
child, surface, declared_path, observed_path, realpath, sha256
```

The two producer-child observations are carried in the post-production producer ledger. The final terminal ledger carries those plus verifier-child observations. The event is an `alias observation`, not a violation; it is emitted only after the applicable digest checks pass.

Classifier-only replay over an in-memory copy of the already-existing normal run-010 receipt produced ten alias observations across `module`, `open`, `receipt_write_set`, and `receipt_mutation_set`. No child was launched for that replay.

## 3. S2 — full alias-sensitive comparison audit

The final parent declares and statically checks eight comparison sites:

| # | Comparison site | Final receiver and byte rule |
|---:|---|---|
| 1 | R0 package/program/run roots | Preserve lexical roots; derive realpath roots for identity/existence. The run directory itself must still not be a symlink. |
| 2 | Subject, evidence, package, and external-input resolution | `safe_resolve()` realpaths both base and candidate, enforces containment, then the existing expected SHA-256/length checks admit bytes. |
| 3 | Runtime interpreter | Realpath both snapshot declaration and `sys.executable`; rehash the executable against the snapshot pin. |
| 4 | Verifier output/receipt declarations | Resolve relative declarations against the run root through `safe_resolve()`; compare both sides by realpath. Absolute declarations remain rejected. |
| 5 | Post-production ledger argv binding | Realpath both the bound argv file and produced ledger path; require exact produced digest and rehash the existing file. |
| 6 | Receipt write/mutation rows | Realpath declared and observed paths; independently rehash output/receipt bytes. |
| 7 | Module and native-load rows | Realpath exact allowlists on load and observation; require receipt digest, actual digest, and independent allowlist digest to agree. |
| 8 | Open-event rows | Realpath observed path into the exact allowlist; freshly rehash because the event row itself has no digest carrier. |

Static source inspection found zero `.resolve()` calls and zero string-prefix path containment checks in the final parent. The only `relative_to()` uses operate on values already passed through `real_path()`.

Audit result:

```text
AUDIT = 8 comparison sites normalized
```

## 4. Disclosed finite delta — five files

The archive workspace supplied the exact pre-relay package bytes. A complete recursive file-hash comparison found no added or removed package file and exactly five changed files.

| File | Before bytes / SHA-256 | After bytes / SHA-256 | Disclosed change |
|---|---|---|---|
| `evaluator_build_A/parent.py` | 45,626 / `0bbf493ac3df83ed70fd2b4a90f6cb535e5af093ce15d208bc15a15ae0343dff` | 53,690 / `10ef12f2449d8694692c81492a208dfa179800722249d7010e536f995b3285bc` | Add lexical/realpath identity helpers, canonical digest allowlists and collision gate; return the package allowlist; normalize external/runtime inputs; materialize the 747-file runtime allowlist; replace module/native classification with digest-authoritative exact-file admission; classify open/write/mutation paths; recompute Builder B's ten-source root; normalize output, ledger, and substitution comparisons; retain declared R0/run spellings; pass exact package/runtime/verifier inputs to all child classifiers; carry alias observations in producer and terminal scopes. Unified diff: 22 hunks, 262 insertions, 75 deletions. |
| `evaluator_build_A/tools/self_check.py` | 24,554 / `fc0d9f4ef64a770d5f0bafadaaaff569e547844fc9f7cbe828473ab8a7ec8117` | 25,159 / `05596a4e29d6828c72793667400058c05d15f38e6294caa99eaeeefb82aa1951` | Add static receiver/carriage presence checks and reject any legacy `.resolve()` call. One hunk, 12 insertions. |
| `evaluator_build_A/manifests/normal.json` | 9,172 / `fc191a3e86ebd658f2351be8e3edb91ba32cee6061181cd9305f94b02a4a252a` | 9,172 / `839ef774114d9431ba3df47b812c1ea6649c06db1539e989b5b49640888e792b` | Update only the parent package row's byte length/SHA-256 and the recursive manifest digest. |
| `evaluator_build_A/manifests/optimized.json` | 9,181 / `d8861f319e211f84e22beeb76f6a370f4a57d91db4705dea2d75f8849fcd8d23` | 9,181 / `d75b5c90427f3922eefb7a37d48cd274e9ec2156402b36fb6ab06ef593ef0101` | Same parent package-row update for optimized mode. |
| `evaluator_build_A/manifests/package_inventory.json` | 5,512 / `d8c49cd729ced2906e15486ccec6850ae8b0f4a41a1c4915e16a700df59e7650` | 5,512 / `fcec4b82cfd29533cdabc18962f6f8d0b3fcf344afaee955cbeadfb55fadbeaf` | Update only the normal/optimized manifest, parent, and self-check inventory rows. |

No producer, materializer, schema, evidence manifest, payload, check map, fixture manifest, subject-lineage manifest, Builder B, or README byte changed.

## 5. Static self-check transcript

Only source compilation, path/digest controls, receipt-classifier replay over copied existing metadata, verifier-source rehashing, deterministic materialization, and static schema/inventory checks ran.

```text
$ /usr/bin/python3 -I -S -B - '<parent compile, alias and negative controls>'
PARENT_COMPILE=PASS assert_nodes=0
PATH_IDENTITY_CONTROL=PASS lexical_diff=true realpath_equal=true alias_recorded=true
CLASSIFIER_REPLAY=PASS prior_receipt_copy alias_observations=10 surfaces=module,open,receipt_mutation_set,receipt_write_set
CONTENT_AUTHORITY_NEGATIVE=PASS claimed_mismatch=MODULE_REHASH sealed_mismatch=MODULE_ALLOWLIST_DIGEST
PATH_AUDIT=PASS sites=8 legacy_resolve_calls=0

$ /usr/bin/python3 -I -S -B - '<verifier source-root check>'
VERIFIER_SOURCE_ROOT=PASS declared=a8494992fdd5c631ec9df76ac394f9558a0253a2cf008de2be5116ae3e4e50ed recomputed=a8494992fdd5c631ec9df76ac394f9558a0253a2cf008de2be5116ae3e4e50ed files=10

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/materialize.py
{"checks": 66, "fixtures": 6, "gated": 10, "normal_sha256": "839ef774114d9431ba3df47b812c1ea6649c06db1539e989b5b49640888e792b", "optimized_sha256": "d75b5c90427f3922eefb7a37d48cd274e9ec2156402b36fb6ab06ef593ef0101", "structural": 56, "subject_lineage_root": "d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688"}

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/self_check.py
SELF_CHECK_OK syntax=5 canonical_json=all schemas=9 inventory=31 evidence_payloads=10 evidence=0/56 absent=56 fixture_obs=0/3 checks=66 structural=56 gated=10 fixtures=6 fixture_fields=16 child_fields=14 verifier_manifest_fields=11 exits=0/1/2 chain_invoked=false

$ '<independent manifest/inventory rehash>'
normal package_rows 25 ok manifest_sha256 839ef774114d9431ba3df47b812c1ea6649c06db1539e989b5b49640888e792b
optimized package_rows 25 ok manifest_sha256 d75b5c90427f3922eefb7a37d48cd274e9ec2156402b36fb6ab06ef593ef0101
inventory_rows 31 sha256 fcec4b82cfd29533cdabc18962f6f8d0b3fcf344afaee955cbeadfb55fadbeaf
```

The two negative controls are the task's content-authority requirement in executable form: a realpath-equal module with a forged claimed digest failed `MODULE_REHASH`; a realpath-equal module whose bytes disagreed with the sealed allowlist failed `MODULE_ALLOWLIST_DIGEST`.

## 6. PIN CHECK, fences, and verb audit

### 6.1 PRE-SEAL PIN CHECK

| Pin or invariant | Final result |
|---|---|
| V005 / addendum | `f8d1a7dc…` / `d17c5e79…`, exact and unchanged. |
| Prior state | Archive parent `0bbf493a…`; archive normal/optimized/inventory `fc191a3e…` / `d8861f31…` / `d8c49cd7…`; all match the declared base. |
| Alias control | Lexical spellings differ; both normalize to the same realpath; observation retains both. |
| Content authority | Both claimed-digest and sealed-digest mismatch controls fail despite realpath equality. |
| Builder B | Manifest/sidecar `08e6c058…`; ten source buffers recompute to root `a8494992…`. |
| Parent | `10ef12f2…`; 53,690 bytes; syntax clean; zero `assert` nodes; zero `.resolve()` calls. |
| Runtime manifests | `839ef774…` / `d75b5c90…`; 25/25 package rows independently rehashed in both. |
| Package inventory | 31/31 rows rehashed; digest `fcec4b82…`. |
| Delta census | No added/removed package file; exactly the five disclosed files changed. |
| Output collision | Artifact and sidecar absent in both required locations immediately before creation. |
| Chain products | Builder A `outputs/` and all package pycache directories contain no files. |

### 6.2 Fences

The classifier replay consumed only copied receipt metadata from the already-existing run-010 files and did not launch a child. No member was bound; no fixed point or end test ran; no physical quantity was evaluated; and no measured constant was read or compared. `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false`.

No fence blocked a structural path/digest result; no MACHINERY-APPEAL is required.

### 6.3 Self verb audit under the verdict-line scope rule

| Verb | Scoped meaning |
|---|---|
| `normalize` / `realpath` | Establish filesystem path identity on both sides of a comparison; never substitutes for a byte digest. |
| `admit` / `pass` | A static path/content receiver or displayed syntax/schema/hash check accepted its exact inputs; no evaluator verdict is claimed. |
| `replay` | Run the parent classifier over an in-memory copy of already-existing receipt metadata; no child or check executor ran. |
| `fail` | The displayed static negative control raised the named parent failure; not a board or physics result. |
| `sealed` | Applies only after adjacent sidecar creation and grants no chain, result, authorization, or proof authority. |

IDENTITY = realpath-normalized + digest-authoritative
AUDIT = 8 comparison sites normalized
SELF_CHECK = passed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN / (+normalize/admit/replay/fail scopes; alias observations are non-violations only after digest checks; no chain result, authorization, or proof claimed)
