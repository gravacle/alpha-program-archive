# STAGE 8 / TASK 6 / BUILD A — RESOLUTION-BASE FIX — LANE 2 V001

Lane: Lane 2, Builder A  
Relay: PASTE 662  
Context: run 009 `VERIFIER_OUTPUT_CONTRACT` disposition  
Scope: verifier output/receipt declaration base, absolute/traversal policy, post-production ledger-path base, and recursive package hashes  
Authority claimed: none

```text
SPEC_V005_SHA256 = f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b
PRIOR_PARENT_SHA256 = e98e9644459ce56ead6aa22235aa339fa790466b3173d5463ab1abf997ed90da
FINAL_PARENT_SHA256 = 0bbf493ac3df83ed70fd2b4a90f6cb535e5af093ce15d208bc15a15ae0343dff
VERIFIER_MANIFEST_SHA256 = 08e6c05862f5e826b912dbcc512125098d494fbfa78d158e2079c34c5aa5bdd1
CHAIN_INVOKED = false
```

## 1. Preflight and finding

| Check | Result |
|---|---|
| Output collision | Artifact and sidecar were absent in the cleanroom and archive workspace immediately before creation. |
| V005 | `f8d1a7dc…`, unchanged. |
| Prior Builder A state | The PASTE 660 artifact and sidecar verify; `parent.py` was 45,424 bytes, `e98e9644…`. |
| B manifest | `08e6c058…`; its sidecar states the same digest and verifies. The declarations are the correct relative names `verifier.output.json` and `verifier.receipt.json`. |
| Run/package separation | The verifier manifest is in Builder B's immutable package; writable outputs belong under Custodian C's run root. |
| Chain state | No chain or evaluator component was invoked; Builder A output and pycache directories contain no files. |

The former validator assigned

```python
base = Path(manifest_path).resolve().parent
```

and used that package directory for relative output and receipt declarations. It then compared those package paths with `run_root/verifier.output.json` and `run_root/verifier.receipt.json`. Correct relative names could never satisfy both bases.

## 2. Resolution-base repair

`validate_verifier_manifest` now receives the run root explicitly and keeps two bases with disjoint roles:

```text
manifest_base = parent of the sealed verifier manifest
run_base      = explicit Custodian C run root
```

The manifest base is returned only as the verifier package launch/import base. The two writable declarations are resolved by:

```python
declared_output  = safe_resolve(run_base, value["output_path"])
declared_receipt = safe_resolve(run_base, value["receipt_path"])
```

They must then equal the parent's exact expected run-root paths.

### Absolute-declaration policy

Absolute `output_path` and `receipt_path` declarations are rejected outright with `VERIFIER_ABSOLUTE_RUN_PATH`, even if their current bytes happen to equal a particular run directory. This is the chosen policy because a package sealed before Custodian C creates a run cannot seal an honest absolute run path. A relative declaration remains portable and becomes concrete only under the parent's explicit run root.

`safe_resolve` also rejects empty/absolute/escaping paths. The negative control `../verifier.output.json` failed with `PATH_ESCAPE`; an existing symlink that resolves outside the run root is rejected by the same containment check.

### Post-production ledger path

The PASTE 660 binder substitutes `${LEDGER_PATH}` with an absolute path under the run root. Its post-production check no longer has a package-base fallback: a nonabsolute bound ledger argv value fails with `VERIFIER_LEDGER_PATH_NOT_ABSOLUTE`. The exact file/digest check remains after producer-ledger creation.

## 3. Disclosed finite delta — four files

| File | Before bytes / SHA-256 | After bytes / SHA-256 | Disclosed change |
|---|---|---|---|
| `evaluator_build_A/parent.py` | 45,424 / `e98e9644459ce56ead6aa22235aa339fa790466b3173d5463ab1abf997ed90da` | 45,626 / `0bbf493ac3df83ed70fd2b4a90f6cb535e5af093ce15d208bc15a15ae0343dff` | Pass `run_root` explicitly to verifier-manifest validation; resolve relative output/receipt declarations only through `safe_resolve(run_base, ...)`; reject absolute declarations; keep `manifest_base` solely for launch/import; reject relative post-bind ledger argv paths instead of resolving them against the package. |
| `evaluator_build_A/manifests/normal.json` | 9,172 / `2b0ee3aeb4c1634b5522fa878d79a920a2412e80d285e57acb2601b1d960ee9c` | 9,172 / `fc191a3e86ebd658f2351be8e3edb91ba32cee6061181cd9305f94b02a4a252a` | Update the parent package row and recursive manifest digest. |
| `evaluator_build_A/manifests/optimized.json` | 9,181 / `713177580acaacaab1229f2681ca1e5c984d5fd58dc5ddee3a1937b3e93b2739` | 9,181 / `d8861f319e211f84e22beeb76f6a370f4a57d91db4705dea2d75f8849fcd8d23` | Same parent package-row update for optimized mode. |
| `evaluator_build_A/manifests/package_inventory.json` | 5,512 / `cf5db3ba818aba39f013b98538a7988a6b21e09942fa63c93db61d32b7ab6910` | 5,512 / `d8c49cd729ced2906e15486ccec6850ae8b0f4a41a1c4915e16a700df59e7650` | Recursively update the parent and two child-manifest rows. |

No producer, generator, self-check source, schema, evidence, payload, check-map, fixture, subject-lineage, Builder B, or README byte changed.

## 4. Static self-check transcript

Only source compilation, synthetic path resolution, negative controls, deterministic materialization, and static schema/hash checks ran.

```text
$ /usr/bin/python3 -I -S -B - '<resolution controls>'
RESOLUTION_TEST_OK relative=run_root absolute=REJECTED traversal=REJECTED package_base=launch_only

$ /usr/bin/python3 -I -S -B -c '<compile parent.py>'
parent_compile=PASS

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/materialize.py
{"checks": 66, "fixtures": 6, "gated": 10, "normal_sha256": "fc191a3e86ebd658f2351be8e3edb91ba32cee6061181cd9305f94b02a4a252a", "optimized_sha256": "d8861f319e211f84e22beeb76f6a370f4a57d91db4705dea2d75f8849fcd8d23", "structural": 56, "subject_lineage_root": "d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688"}

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/self_check.py
SELF_CHECK_OK syntax=5 canonical_json=all schemas=9 inventory=31 evidence_payloads=10 evidence=0/56 absent=56 fixture_obs=0/3 checks=66 structural=56 gated=10 fixtures=6 fixture_fields=16 child_fields=14 verifier_manifest_fields=11 exits=0/1/2 chain_invoked=false

$ /usr/bin/python3 -I -S -B - '<AST/source-use audit>'
RUN_PATH_AUDIT_OK run_root_resolutions=2 package_base_run_resolutions=0 absolute_policy=REJECT traversal=REJECT
PACKAGE_BASE_AUDIT_OK uses=launch_cwd,receipt_module_root only
normal package_rows 25 ok
optimized package_rows 25 ok
```

## 5. Run-path audit

The entire final parent was inspected for run-scoped resolution against the package base.

- Output declaration: `safe_resolve(run_base, output_path)`.
- Receipt declaration: `safe_resolve(run_base, receipt_path)`.
- Bound ledger argv path: required absolute and compared directly to the run-root producer-ledger path.
- Normal/optimized output, receipts, producer ledger, bound manifest, verifier output/receipt, and terminal ledger: all constructed directly as `run_root / fixed_name`.
- `manifest_base`/`verifier_base`: used only as verifier launch cwd and as the permitted module-origin root when classifying the verifier receipt. Neither use resolves a writable run path.
- External input paths: resolved under the separately supplied program root, not the verifier package.

Audit line:

```text
AUDIT = no other package-based run-path resolution
```

## 6. PIN CHECK, fences, and verb audit

### 6.1 PRE-SEAL PIN CHECK

| Pin or invariant | Final result |
|---|---|
| V005 | `f8d1a7dc…`, exact and unchanged. |
| B manifest | `08e6c058…`; sidecar exact; relative names are `verifier.output.json` / `verifier.receipt.json`. |
| Base split | Two run-scoped declarations resolve under the explicit run root; zero resolve under the package base. |
| Absolute policy | Both output and receipt absolute declarations fail before equality comparison. |
| Containment | `../` negative control fails; `safe_resolve` retains symlink-aware containment. |
| Ledger path | Bound argv value must be absolute; no package-base fallback remains. |
| Parent | `0bbf493a…`; 45,626 bytes; syntax clean. |
| Runtime manifests | `fc191a3e…` / `d8861f31…`; 25/25 package rows independently rehashed. |
| Package inventory | 31/31 rows rehashed; digest `d8c49cd7…`. |
| Output collision | Artifact and sidecar absent in both required locations immediately before creation. |
| Chain products | No files under Builder A outputs or pycache directories. |

### 6.2 Fences

The temporary controls used only copied manifest metadata and empty path locations. No evaluator component ran. No member was bound; no fixed point or end test ran; no physical quantity was evaluated; and no measured constant was read or compared. `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false`.

### 6.3 Self verb audit under the verdict-line scope rule

| Verb | Scoped meaning |
|---|---|
| `resolve` | Convert a relative declaration to a normalized, containment-checked path under the explicit run root. |
| `reject` | Static fail-closed branch exercised on absolute and traversal controls; not an evaluator verdict. |
| `passed` | The displayed syntax, path-control, schema, canonical, inventory, and hash checks only. |
| `audit` | Static AST/source-use inspection of path-base receivers. |
| `sealed` | Applies only after adjacent sidecar creation and grants no chain, result, authorization, or proof authority. |

BASE = run root (+absolute declarations rejected outright as un-sealable)
AUDIT = no other package-based run-path resolution
SELF_CHECK = passed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN / (+resolve/reject/pass/audit scopes; no chain result, authorization, or proof claimed)
