# STAGE 8 / TASK 6 / BUILD A — ARGV DIRECT-SCRIPT PREFIX FIX — LANE 2 V001

Lane: Lane 2, Builder A  
Relay: PASTE 666, resumed after Builder B's PASTE 667 root inclusion  
Context: run 013 `VERIFIER_ARGV_PREFIX` disposition  
Scope: verifier root membership, declared entry validation, direct-script argv translation, launch-form negative controls, recursive hashes, and full parent launch audit  
Authority claimed: none

```text
SPEC_V005_SHA256 = f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b
INTEGRATION_ADDENDUM_SHA256 = d17c5e79986bea431dec0b572019096f9c059bcc43876fda9134abc96ce0f260
LAUNCHER_IN_ROOT_ARTIFACT_SHA256 = 259876aeb107b05e6ee6d94d865324f6d2c6c7c68bad54394cc7cbaff5967aff
VERIFIER_MANIFEST_SHA256 = 91d264dcbc2da49ccb4e28e19eb0e775dd654eb1d16b60bfef5a132f0f3a4d7d
VERIFIER_ROOT_SHA256 = 8732646c2bfec9b0e98dbb2ae4ab4733d0348b20bc09a6792805f97104a36275
PRIOR_PARENT_SHA256 = 7b95464a7141f29d8c5c8b3be9a785f1e49e1649f98803502c55b31a41cef717
FINAL_PARENT_SHA256 = a5b99a1a5c3594084d7793b024ee1ad6b4b7bd8a75fb1934c20b8ccb1f637e31
CHAIN_INVOKED = false
```

## 1. Resumed preflight and finding

| Check | Result |
|---|---|
| Output collision | This artifact and sidecar were absent in the cleanroom and archive workspace immediately before creation. |
| Governing pins | V005 is `f8d1a7dc…`; the integration addendum is `d17c5e79…`; both exact. |
| Prior Builder A state | The sealed PASTE 664 artifact is `21ad01a3…`; the archive Builder A package matches its declared parent/manifests/inventory base. |
| Root-inclusion correction | Builder B's sealed correction is `259876ae…`; its sidecar verifies. It defines one root over the entry script plus ten `verifier/*.py` members. |
| B manifest | Canonical manifest and sidecar verify at `91d264dc…`; `entry_point="run_verifier.py"`; argv begins `python3, run_verifier.py`. |
| Root predicate | The globally sorted 11-member digest independently recomputes to `8732646c…`; `run_verifier.py` is included with digest `2c8caad0…`. |
| Chain state | No producer, verifier, launcher dry run, check executor, fixture, or full chain was invoked in this relay. |

The former parent authored this prefix regardless of the sealed manifest:

```text
python3 [-O] -m manifest.entry_point
```

Under the pinned `-I -S -B` runtime, `-m verifier.verify` cannot resolve because isolated mode removes the package directory and cwd from module search. The parent already launches both producer children as direct scripts. The hard-coded verifier module form was therefore inconsistent with both the declared verifier manifest and the parent's own established launch pattern.

## 2. Direct-script validation and command construction

### 2.1 Root membership receiver

The parent now derives the verifier root over exactly:

```text
manifest.entry_point
every verifier/*.py source file
```

Member names are package-relative and globally sorted. For the sealed current manifest this is Builder B's exact 11-member list: `run_verifier.py` followed by the ten `verifier/*.py` files. The parent freshly hashes each member, creates its realpath/digest allowlist entry, concatenates the member digest strings in sorted member-name order, and requires the resulting SHA-256 to equal `manifest.verifier_root_sha256`.

The entry is therefore part of the root by construction rather than appended to an already-computed core root.

### 2.2 Entry declaration gate

`verifier_entry_target()` requires all of the following:

1. `entry_point` is a package-relative Python source name matching the closed slash-separated identifier form ending in `.py`;
2. `safe_resolve(verifier_package, entry_point)` remains inside the verifier package after realpath normalization;
3. the resulting file exists;
4. its realpath is a member of the allowlist used to compute the verified `verifier_root_sha256`;
5. its bytes freshly rehash to that member's digest.

Absolute paths, empty names, backslashes, `.`/`..`, traversal, option-like tokens, non-Python entries, nonexistent entries, and package files outside the covered member set fail before command construction.

### 2.3 Exact argv prefix and runtime command

The admitted manifest prefix is now exactly:

```text
normal:    ["python3", manifest.entry_point]
optimized: ["python3", "-O", manifest.entry_point]
```

The optional `-O` is accepted only when `manifest.optimize` is true. The launch-position token is rejected if it is `-c`, `-m`, or any other string beginning with `-`. The declared argv entry must equal `manifest.entry_point` exactly.

Only after those checks does the parent construct the executable command:

```text
[pinned_python, "-I", "-S", "-B", ["-O"], absolute_root_covered_entry, remaining_argv]
```

The concrete entry path is the realpath-normalized, root-covered file. Remaining bound argv operands retain their declared order and values. The manifest's `python3` token does not choose an interpreter; the parent still uses the snapshot-pinned, freshly rehashed Python executable.

## 3. Negative controls and launch-form audit

### 3.1 Bidirectional controls

The current manifest passed in normal and optimized forms. Six adverse forms were then checked in memory:

| Control | Result |
|---|---|
| `python3 -c ...` | `VERIFIER_ARGV_FORBIDDEN_LAUNCH_FORM` |
| `python3 -m verifier.verify` | `VERIFIER_ARGV_FORBIDDEN_LAUNCH_FORM` |
| `python3 --inspect ...` | `VERIFIER_ARGV_FORBIDDEN_LAUNCH_FORM` |
| argv script differs from `entry_point` | `VERIFIER_ARGV_PREFIX` |
| `entry_point=../outside.py` | `VERIFIER_ENTRY_POINT` |
| existing package script outside the verified member map | `VERIFIER_ENTRY_UNCOVERED` |

No child was launched for these controls.

### 3.2 Entire-parent audit

Every `subprocess.run` and every Python command construction in the final parent was inspected:

| Site | Form |
|---|---|
| Normal producer child | Pinned Python + `-I -S -B` + absolute content-addressed `producer.py`. |
| Optimized producer child | Pinned Python + `-I -S -B -O` + the same absolute content-addressed `producer.py`. |
| Verifier child | Pinned Python + `-I -S -B` (+ declared `-O`) + absolute root-covered manifest entry. |
| Trust probes | Fixed non-Python `/usr/bin/sw_vers` and `/usr/bin/csrutil`; not launch-form expectations for a Python child. |

There are zero authored module-form command constructors, zero command-string `-c` constructors, and zero other Python child launch sites. The runtime snapshot's existing `direct-script-no-c-no-m` declaration remains the sole runtime launch-mode statement and agrees with all three children.

Audit result:

```text
AUDIT = no other authored launch-form
```

## 4. Disclosed finite delta — five files

The archive workspace supplied the exact pre-relay Builder A package. A recursive hash comparison found no added or removed package file and exactly five changed files.

| File | Before bytes / SHA-256 | After bytes / SHA-256 | Disclosed change |
|---|---|---|---|
| `evaluator_build_A/parent.py` | 53,849 / `7b95464a7141f29d8c5c8b3be9a785f1e49e1649f98803502c55b31a41cef717` | 55,610 / `a5b99a1a5c3594084d7793b024ee1ad6b4b7bd8a75fb1934c20b8ccb1f637e31` | Add the relative-script/coverage/digest entry receiver; compute the root over the declared entry plus core modules; replace the authored `-m` prefix with exact direct-script validation; reject forbidden option forms; construct the actual command with the covered absolute entry; pass verified package base/member map to the command builder. Unified diff: four hunks, 44 insertions, eight deletions. |
| `evaluator_build_A/tools/self_check.py` | 26,816 / `cedf2c8b82957be18415f3f15d3feac656117339ef552fab15973578f9aea51f` | 27,600 / `20b15151324c1eb21a34de4c517a0ff3d7e7cab5719fb820c5db9b939aa3d056` | Change the synthetic verifier to direct-script form and require the entry, root-coverage, forbidden-form, absolute-script, and final-call receivers; reject reintroduction of authored module-form constructors. Two hunks, 14 insertions, two deletions. |
| `evaluator_build_A/manifests/normal.json` | 9,172 / `7ef05faa9bcfcbb9fec6c31ae8e1a368317341059594ace0057c3ebddad8b6ea` | 9,172 / `4f09af9f23672b6b3e5394a33f78d99cc28ac58c9f05c46849d672dc2a086277` | Update only the parent package row. |
| `evaluator_build_A/manifests/optimized.json` | 9,181 / `724f73b4c38842e8b3e5afe5e4e393a7717b7ebd5c380f2b7670b3ff9ed1bdcc` | 9,181 / `7b6ad45d4902730f0f77ea31c16ecf0f416412a7bdbd359c507080fe6db888ca` | Same parent package-row update for optimized mode. |
| `evaluator_build_A/manifests/package_inventory.json` | 5,512 / `ec60dfeb4f9a8d850e06dd92e71f1de179cc174682c8af489fc43c8c682a2f33` | 5,512 / `f9ebe36cdaef0cd5c8c9e13fb6f6b53d131586b1ee9ac225ec7c1280fceaeedb` | Update the parent, self-check, and two child-manifest rows. |

No producer, materializer, schema, evidence, payload, check-map, fixture, subject-lineage, Builder B, or README byte was changed by Builder A.

## 5. Static self-check transcript

Only source parsing, manifest/root validation, command construction without execution, negative controls, deterministic materialization, and package rehashing ran.

```text
$ /usr/bin/python3 -I -S -B - '<direct-prefix controls>'
ROOT_INCLUSION=PASS root=8732646c2bfec9b0e98dbb2ae4ab4733d0348b20bc09a6792805f97104a36275 members=11 entry_digest=2c8caad0d939a2ab716ab57ed077fd79a61a548231de4816d673f0811a861b62
DIRECT_PREFIX=PASS normal=[pinned_python,-I,-S,-B,<absolute run_verifier.py>] optimized=[pinned_python,-I,-S,-B,-O,<absolute run_verifier.py>]
NEGATIVE_CONTROLS=PASS dash_c:VERIFIER_ARGV_FORBIDDEN_LAUNCH_FORM,dash_m:VERIFIER_ARGV_FORBIDDEN_LAUNCH_FORM,flag:VERIFIER_ARGV_FORBIDDEN_LAUNCH_FORM,mismatch:VERIFIER_ARGV_PREFIX,outside:VERIFIER_ENTRY_POINT,uncovered:VERIFIER_ENTRY_UNCOVERED
LAUNCH_FORM_AUDIT=PASS python_child_forms=3 direct_scripts=3 authored_module_forms=0 authored_c_forms=0 assert_nodes=0

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/materialize.py
{"checks": 66, "fixtures": 6, "gated": 10, "normal_sha256": "4f09af9f23672b6b3e5394a33f78d99cc28ac58c9f05c46849d672dc2a086277", "optimized_sha256": "7b6ad45d4902730f0f77ea31c16ecf0f416412a7bdbd359c507080fe6db888ca", "structural": 56, "subject_lineage_root": "d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688"}

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/self_check.py
SELF_CHECK_OK syntax=5 canonical_json=all schemas=9 inventory=31 evidence_payloads=10 evidence=0/56 absent=56 fixture_obs=0/3 checks=66 structural=56 gated=10 fixtures=6 producer_fields=13 receipt_fields=16 fixture_fields=16 child_fields=14 verifier_manifest_fields=11 exits=0/1/2 chain_invoked=false

$ '<independent package rehash>'
normal package_rows 25 ok manifest_sha256 4f09af9f23672b6b3e5394a33f78d99cc28ac58c9f05c46849d672dc2a086277
optimized package_rows 25 ok manifest_sha256 7b6ad45d4902730f0f77ea31c16ecf0f416412a7bdbd359c507080fe6db888ca
inventory_rows 31 sha256 f9ebe36cdaef0cd5c8c9e13fb6f6b53d131586b1ee9ac225ec7c1280fceaeedb
```

## 6. PIN CHECK, fences, and verb audit

### 6.1 PRE-SEAL PIN CHECK

| Pin or invariant | Final result |
|---|---|
| V005 / addendum | `f8d1a7dc…` / `d17c5e79…`, exact and unchanged. |
| Prior Builder A state | Sealed PASTE 664 artifact `21ad01a3…`; archive package matches all declared before-hashes. |
| B root correction | Sealed artifact `259876ae…`; exact 11-member definition; no Builder A write to Builder B. |
| B instance | Manifest/sidecar `91d264dc…`; entry and argv direct-script declarations agree. |
| Root / entry | Root `8732646c…` independently recomputed; 11 members; entry digest `2c8caad0…`; entry realpath is in the verified member map. |
| Isolation | Pinned Python remains rehashed; `-I -S -B` retained; optional `-O` bound to the manifest boolean. |
| Forbidden forms | `-c`, `-m`, arbitrary option, mismatched entry, traversal, and uncovered package file all rejected in static controls. |
| Parent | `a5b99a1a…`; 55,610 bytes; syntax clean; zero `assert` nodes. |
| Runtime manifests | `4f09af9f…` / `7b6ad45d…`; 25/25 package rows rehashed in both. |
| Package inventory | 31/31 rows rehashed; digest `f9ebe36c…`. |
| Delta census | No package file added/removed; exactly the five disclosed files changed. |
| Output collision | Artifact and sidecar absent in both required locations immediately before creation. |
| Chain products | Builder A `outputs/` and all package pycache directories contain no files. |

### 6.2 Fences

The controls constructed command arrays but did not pass them to `subprocess.run`. No launcher or evaluator child ran. No member was bound; no fixed point or end test ran; no physical quantity was evaluated; and no measured constant was read or compared. `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false`.

No fence blocked a structural launch-contract result; no MACHINERY-APPEAL is required.

### 6.3 Self verb audit under the verdict-line scope rule

| Verb | Scoped meaning |
|---|---|
| `accept` | The static manifest/root/argv receiver admitted the exact direct-script declaration and constructed, but did not execute, its command. |
| `cover` / `verify` | The entry's relative name and bytes participate in the independently recomputed 11-member root and exact file digest checks. |
| `reject` | Static adverse command metadata raised the displayed parent failure; no child ran. |
| `launch` | Describes command construction or audited source sites unless explicitly negated; this relay invoked none. |
| `sealed` | Applies only after adjacent sidecar creation and grants no chain, result, authorization, or proof authority. |

PREFIX = direct-script accepted (+validation: entry equality, package containment, 11-member root coverage, digest recheck)
AUDIT = no other authored launch-form / (+3 Python child sites, all direct-script; -c/-m/arbitrary flags rejected)
SELF_CHECK = passed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN / (+accept/cover/verify/reject/launch scopes; commands constructed but not executed; no chain result, authorization, or proof claimed)
