# STAGE 8 / TASK 6 / BUILD — EVALUATOR BUILDER A MANIFEST — LANE 2 V001

**Date:** 2026-08-07  
**Lane/custody:** Codex Lane 2, Builder A (parent + producer only)  
**Register head checked:** Q-585  
**Status:** code/package build and syntax/schema self-check only; no evaluator chain or descriptor procedure was invoked

## 0. Preflight and pins

The authorization, specification, and runtime objects were hash-verified before
their contents were used. The output artifact and `evaluator_build_A/` did not
exist in either the cleanroom or archive workspace at the no-clobber check.

| Input | SHA-256 | Result |
|---|---|---|
| sealed RD-22 authorization `DECISION_RD22_BUILD_AUTHORIZED_2026-08-07.md` | `ff84c4a8ba5c7f8eabfbcc587475d3a5050c21d758a2788c5b9e28b7ee022340` | verified and read |
| governing spec `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md` | `f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b` | verified and read |
| `provenance/primitive_step6_runtime_snapshot_v012.json` | `50a6fc141a45451678aa7543e4f267ce26beb6e53182170b478acb6fb0e0f5bb` | verified |
| `primitive_step6_content_addressed_runtime_gate_v010.md` | `2ad7f72a88184c11e1253f2c47598fca11e60d05e8e71a26db4e19b16bf98d42` | verified |
| blocker census `BID_FULL_STACK_REVIEW_LEDGER_V003.md` | `c09f2c246c48ddfd0df127da26a22f08ba9ffd44f5c2118c178a0a5eba5d00e8` | verified |
| packet manifest | `9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311` | verified |

The unique runtime subject is the authorization's v012 pair. The trust root was
extracted from the snapshot, not restated from a path:

```text
machine       = arm64
platform      = macOS-26.5-arm64-arm-64bit
sw_vers       = ProductName macOS; ProductVersion 26.5; BuildVersion 25F71
SIP_status    = System Integrity Protection status: enabled.
policy        = SIP-protected dyld shared cache and System Library paths are a
                revalidated mutable host trust base; every non-system loaded
                native image must be a hashed runtime file
```

The pinned CPython is
`/Users/bgm/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3.12`,
SHA-256 `eb9d74b9c7cfdfb2c9b91614edb2c3607360ba46c5aa7fc4557b3a4a23e97cff`.

The governing gates remain exact:

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member_binding = false
fixed_point_executed = false
end_test = false
physical_quantity_evaluated = false
measured_constant_comparison = false
```

## 1. Implemented Builder A package

### 1.1 Parent, R0–R10

`evaluator_build_A/parent.py` is self-contained and directly executable under
`-I -S -B`; it does not depend on the script directory being added to
`sys.path`. Every precondition is an explicit fail-closed branch with nonzero
exit. There is no Python `assert` statement.

| State | Builder A implementation |
|---|---|
| R0 | checks isolated flags and optimize level; hashes its exact source; parses canonical manifests; verifies authorization, spec, runtime, package, subject, schemas, output absence, and three empty pycache roots |
| R1 | admits distinct canonical normal/optimized manifests with exact runtime-file and external-input inventories; their only differences are mode, optimization, and writable paths |
| R2 | reads live `machine`, `platform`, `sw_vers`, SIP status, and policy as T0; requires exact equality with the snapshot-extracted trust root |
| R3 | launches the self-contained producer with the pinned CPython, `-I -S -B`, a cleared environment, normal manifest, and exclusive output/receipt paths |
| R4 | rereads T1 and requires T1=T0 |
| R5 | launches a second fresh producer with the same source and roots plus a real `-O`; paths and writable state are separate |
| R6 | rereads T2 and requires T2=T1=T0 |
| R7 | rehashes module/native records; rejects bytecode, unhashed or non-runtime modules, process/network/environment events, and any write set other than the two exclusive child files; child receipts remain non-authoritative |
| R8 | recursively removes only `process_id`, `monotonic_duration`, and `python_optimize`, then byte-compares the remaining canonical outputs; separately enforces 66 IDs, 56/10 classes, six fixtures, and gate discipline |
| R9 | requires a separately sealed Builder B manifest/source, verifies its inventory without importing it, takes T3/T4, launches it as a third isolated child, validates its output/receipt, and requires T4=T3=T2=T1=T0 |
| R10 | constructs the exact terminal-ledger top field set and exact child records, binds the verifier result, computes `terminal_content_sha256` with the hash field initially empty, and exclusively writes the terminal ledger; signing remains with the signature custodian |

The R9 interface is intentionally fail-closed. The independently sealed Builder
B public contract became visible only after this package was built. Its sealed
manifest copy is
`STAGE8_TASK6_EVALUATOR_BUILD_B_MANIFEST_DARIO_V001.md`, SHA-256
`f79b50ac951522c636193e7fdbc3e4c216b9373be58c3ada8523f8bd7505133b`.
That public contract uses `python3 -m`, stdout schema
`gravacle.a35.verifier-verdict.v1`, and no §9.4 child receipt. Those three facts
do not satisfy this parent's isolated direct-child, verifier-manifest, and
receipt contract. No Builder B source was imported or reused. A separately
sealed custody-approved integration adapter/contract is therefore D2 below;
until it exists, the parent stops before R9 rather than manufacture a receipt or
weaken isolation.

### 1.2 Producer and check executors

`evaluator_build_A/producer.py` is also self-contained. The shipped check map
contains all 66 exact descriptor rows, each with:

```text
blocker/stable ID
sealed source SHA-256 and zero-based half-open byte span
descriptor SHA-256 (exact UTF-8 Markdown row plus one LF)
execution class and required gate
exact inputs, deterministic procedure, and PASS predicate text
ordered program_contract = [{result_name, opcode, repeatable}, ...]
```

The structural executor admits an evidence record only if the descriptor hash,
input-file content root, invocation names, opcode sequence, instance IDs, and
invocation cardinalities match the closed contract. The result predicate is
derived from the descriptor; it is not supplied by the producer or evidence
record. Missing/extra inputs and unknown/malformed opcodes fail closed.

The complete closed opcode engine implements `STRICT`, `SCHEMA`, `TYPE`,
`EXACT`, `KERNEL`, `ENUM`, `DOMAIN`, `UNITS`, `DAG`, `M2`, `COMPARE`, and
`RUNTIME`. `M2` includes fixed-string, whitespace, AST/scope, and joint
hyphen/space/underscore modes. `SYMBOLIC` and `SPECTRAL` have no structural
dispatch entry. Encountering either in a structural row returns `ERROR` before
formation.

All ten `GATED-EXECUTION` rows are handled before evidence lookup or opcode
dispatch:

```text
status = NOT_RUN_GATE
procedure_started = false
reason = RD22_STRUCTURAL_ONLY_GATE_CLOSED
```

The six fixture descriptors are separately content-addressed. The three gated
fixtures follow the same no-start rule. Structural fixture observations are not
copied into live output fields.

### 1.3 Roots and closed manifests

| Object | SHA-256/root |
|---|---|
| check map (66 exact descriptors) | `034ebf3e071051d25d5b7f8871a03193da5bc9ab16a7c07c7cae1bbb8f467e26` |
| fixture manifest (6 descriptors) | `6620d3243ae4c30c35fa395c484c8ae27ae473e4aadd0c0ec4cf3497a76e790e` |
| sealed-document subject-lineage manifest bytes | `bd425bb0cedb0ce1da7c74ae861112f39fb36352d8e1f85fa59b3fde5bffd1eb` |
| subject-lineage content root | `a01065f022ca7c66d3b943a78d3fae3816938c78cb68f2db369ab86965032e87` |
| structural-evidence manifest | `03f870d8f0f3bbc158fd613df6c67378afb19d2928a1b876d581e4bbb5d24729` |
| normal child manifest | `ae0d2f419cdc8b26f49038395510794e0e3c04ebaef53d863ea1e0fdeb8ba01a` |
| optimized child manifest | `6da7c16e122ed74e769ae7226e3a21eede91c71861db4a83f23058c725fa5a80` |

The subject root uses the spec's exact domain-separated formula over the sealed
spec, blocker ledger, packet manifest, V011 packet principle, and source-parent
gate. The child manifests each inventory 14 runtime files and six external
inputs by byte length and SHA-256. No path string is authority.

## 2. `BRANCH_OUTCOME` — Q-583 obligation discharged

The sealed descriptor names a finite candidate/tie/failure grammar but leaves
its per-ID values to the build. This map is a specification constant present
byte-identically in the check map and both child manifests:

| `G_branch` ID | `BRANCH_OUTCOME[id]` | Directional reason |
|---|---|---|
| `BRANCH-CANDIDATE-TYPED-COMPLETE` | `ADMITTED` | the candidate has a deterministic typed completion |
| `BRANCH-FAILURE-UNRESOLVED` | `REJECTED` | a failure cannot become a later choice |
| `BRANCH-TIE-UNRESOLVED` | `REJECTED` | an unresolved tie cannot become a later choice |

The branch-ID `ENUM` output must match the expected ID ledger; every item is
validated by `SCHEMA` and its classification is compared to this map. The map
is never read from producer evidence.

## 3. Implemented versus deferred — complete finite list

The Builder A implementation is complete for the parent, producer, structural
opcode engine, descriptor/check map, fixture descriptors, schemas, manifests,
receipts, comparison, and terminal-ledger construction. The following are not
silently filled:

| ID | Deferred/external item | Reason and fail-closed consequence |
|---|---|---|
| D1 | per-check structural proof/evidence payloads and three structural fixture observations | no separately sealed payloads were present in the governing input set; the evidence manifest names all 56/3 absences, and a run returns `FAIL(INPUT_INTEGRITY)` rather than fabricate PASS evidence |
| D2 | Builder B integration adapter/contract | the sealed B public launch, stdout schema, and missing child receipt differ from R9's required isolated child contract; the parent requires a separately sealed `rd22.verifier-manifest.v001` and stops if it is absent |
| D3 | first structural chain invocation | custody belongs to Custodian C; Builder A did not create a run directory or execute a descriptor |
| D4 | detached signature/public integrity deployment | custody occurs only after a successful complete fresh chain; Builder A claims no terminal assurance |

D1 and D2 mean the current package does not predict a successful first run.
They do not create a PASS escape hatch: absence is visible and fail-closed.

## 4. Complete file inventory — 20 files

The child inventories cover every runtime-consumed file. This build manifest
additionally covers the README and build/self-check tools. Empty `outputs/` and
the three empty pycache directories contain no files and are not counted.

| Relative path under `evaluator_build_A/` | Bytes | SHA-256 |
|---|---:|---|
| `README.md` | 3269 | `ac003fa3b1a377ece59a8a1b0656f6d6a9773118d6dcf355c0eb89157eece013` |
| `checks/check_map.json` | 107235 | `034ebf3e071051d25d5b7f8871a03193da5bc9ab16a7c07c7cae1bbb8f467e26` |
| `fixtures/fixture_manifest.json` | 2353 | `6620d3243ae4c30c35fa395c484c8ae27ae473e4aadd0c0ec4cf3497a76e790e` |
| `inputs/structural_evidence_manifest.json` | 6986 | `03f870d8f0f3bbc158fd613df6c67378afb19d2928a1b876d581e4bbb5d24729` |
| `inputs/subject_lineage_manifest.json` | 1289 | `bd425bb0cedb0ce1da7c74ae861112f39fb36352d8e1f85fa59b3fde5bffd1eb` |
| `manifests/normal.json` | 6303 | `ae0d2f419cdc8b26f49038395510794e0e3c04ebaef53d863ea1e0fdeb8ba01a` |
| `manifests/optimized.json` | 6312 | `6da7c16e122ed74e769ae7226e3a21eede91c71861db4a83f23058c725fa5a80` |
| `manifests/package_inventory.json` | 2782 | `a24a533f6ec023ad3fac0512c278a3cc7dd023d54ef7dcb44128b79035697993` |
| `parent.py` | 30651 | `c4e85941ea975362ff51dd64405137db74da066b1671398d1ce7ab853e6da2b6` |
| `producer.py` | 37734 | `9c786a449e4778ea0ced5715eff920754e534cdd154a1408d0156c72f47337e2` |
| `schemas/check-map.schema.json` | 456 | `8e971040ca4d96161303710bc391dd322cb581983c881eaf39b1547fb4e68192` |
| `schemas/child-manifest.schema.json` | 1420 | `f5325b40cd49db94e11cc44628ec46b6ac400489d99c574642461e0b8697ef1e` |
| `schemas/child-receipt.schema.json` | 1186 | `e1267ed66a0a79f3665c9399584de4dffde00abc8d394888017c17df0b35081d` |
| `schemas/fixture-manifest.schema.json` | 353 | `cb8ed7ac91509ba74311ac47838dcb39bb4ff4690948bcbe29f08a8f2907a1dc` |
| `schemas/producer-output.schema.json` | 1014 | `f3c135f9c3670e381b9aaf79121a6e4e6ae025e8a77b86d55819584c18daa847` |
| `schemas/structural-evidence.schema.json` | 351 | `5d3ec96abcec19f664665f5a1bf316a9c4fa3d95aa66b8551de8036d85f97174` |
| `schemas/terminal-ledger.schema.json` | 1274 | `c44060482a406817e2c3c50e27dcd837dbf1858703ab7d52849478c0387ddf58` |
| `schemas/verifier-output.schema.json` | 823 | `b4878c1d7a42a2f29aa17bc4d6d86a1d7f417fe83213cb9c536c3e0403b5f826` |
| `tools/materialize.py` | 24921 | `4b1de0a230b3815c961e35eb8763c04a7154cace30f39d67321b4499d3e558e4` |
| `tools/self_check.py` | 9163 | `ca05d2d51ad6cb3e08132baf654688ddbbbe4fcb6301884e9c0e6be61c292918` |

`manifests/package_inventory.json` inventories the other 19 files and excludes
itself to avoid a false self-referential hash claim.

## 5. Entry points and Custodian C invocation contract

Entry points:

```text
R0 parent       evaluator_build_A/parent.py
R3/R5 producer evaluator_build_A/producer.py
build-only map evaluator_build_A/tools/materialize.py
syntax/schema   evaluator_build_A/tools/self_check.py
```

The literal R0 contract below is the exact command shape. The named
`evaluator_build_B_adapter/manifests/verifier.json` is D2 and does not yet
exist; **Custodian C must not execute these lines until that artifact and its
`.seal.sha256` sidecar are separately sealed.** The run directory must also be
new; D3 leaves it absent now.

```sh
/usr/bin/install -d -m 0700 '/Users/bgm/Documents/Documents - Brian’s MacBook Pro/New project/gravity_emergence_evidence_program/evaluator_run_RD22_first_structural_v001'

'/Users/bgm/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3.12' -I -S -B '/Users/bgm/Documents/Documents - Brian’s MacBook Pro/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/evaluator_build_A/parent.py' --package-root '/Users/bgm/Documents/Documents - Brian’s MacBook Pro/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/evaluator_build_A' --program-root '/Users/bgm/Documents/Documents - Brian’s MacBook Pro/New project/gravity_emergence_evidence_program' --authorization '/Users/bgm/MB Work/alpha-program-archive/supervision/DECISION_RD22_BUILD_AUTHORIZED_2026-08-07.md' --normal-manifest '/Users/bgm/Documents/Documents - Brian’s MacBook Pro/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/evaluator_build_A/manifests/normal.json' --normal-manifest-sha256 'ae0d2f419cdc8b26f49038395510794e0e3c04ebaef53d863ea1e0fdeb8ba01a' --optimized-manifest '/Users/bgm/Documents/Documents - Brian’s MacBook Pro/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/evaluator_build_A/manifests/optimized.json' --optimized-manifest-sha256 '6da7c16e122ed74e769ae7226e3a21eede91c71861db4a83f23058c725fa5a80' --verifier-manifest '/Users/bgm/Documents/Documents - Brian’s MacBook Pro/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/evaluator_build_B_adapter/manifests/verifier.json' --run-root '/Users/bgm/Documents/Documents - Brian’s MacBook Pro/New project/gravity_emergence_evidence_program/evaluator_run_RD22_first_structural_v001'
```

The parent requires the verifier manifest's sidecar, validates the manifest's
single `verifier_source` inventory row, and refuses any source containing a
Python `assert` statement. No `-c`, parent `-m`, undeclared `PYTHONPATH`,
`PYTHONHOME`, startup/inspect, `DYLD_*`, or `LD_*` mechanism appears in the
contract.

## 6. Self-check transcript — syntax/schema only

Only the following permitted static check was run, using the pinned CPython:

```text
$ /Users/bgm/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3.12 -I -S -B evaluator_build_A/tools/self_check.py
SELF_CHECK_OK syntax=4 canonical_json=all schemas=8 checks=66 structural=56 gated=10 fixtures=6 chain_invoked=false
exit = 0
```

The check performed:

- AST parse/compile of `parent.py`, `producer.py`, `materialize.py`, and
  `self_check.py`;
- zero Python `assert` nodes in all four sources;
- strict/canonical JSON parsing of every shipped JSON file;
- available-instance validation for the check-map, fixture, evidence, and both
  child manifests, plus exact top-level inventories for output/receipt/
  verifier/terminal schemas;
- all 66 descriptor hashes rebound to the sealed V005 rows;
- all 63 blocker byte spans bounded and beginning at their numbered sealed
  blocker item;
- exact 56 structural / 10 gated and six-fixture censuses;
- exact package inventory rehashes and normal/optimized finite-delta check;
- empty output directory and three empty pycache roots.

It did not call `parent.py`, `producer.py`, or a verifier; did not create a run
root; did not execute a descriptor; and did not form a physical quantity.

## 7. Battery and verdict scope

### F_PLDEC

The structural engine accepts no floating physical quantity, desired target,
reader result, measured constant, optimizer, or stochastic input. Its exact
algebra consumes integer/rational or declared canonical objects. A structural
attempt to dispatch `SYMBOLIC` or `SPECTRAL` returns `ERROR`; every descriptor
that lawfully names those opcodes is gated and returns `NOT_RUN_GATE` before
dispatch. `F_PLDEC = CLEAN` for the syntax/schema build.

### Anti-tuning

Descriptor text, procedure contracts, expected predicates, source spans,
fixtures, class partition, branch outcomes, runtime, and manifests are hashed
before a child receives control. The producer cannot add a result name, change
an opcode, weaken an enumeration, alter the three-field comparison mask, or
supply `BRANCH_OUTCOME`. Missing evidence produces FAIL; it never selects a
favourable default.

### Verb audit and scope

The verbs “implements,” “validates,” and “constructs” in this artifact refer to
shipped code paths or static checks. They do not claim that a descriptor ran,
that Builder B integrated, that a terminal ledger exists, that a signature was
made, or that any physical/proof/seal result follows. The four deferred items
are therefore included in the package verdict itself.

PACKAGE = complete (+deferred list D1 structural evidence, D2 Builder B integration adapter, D3 Custodian run, D4 detached signature)
FILES = 20 (+inventory hashed)
GATED_ROWS = emit NOT_RUN_GATE without starting
BRANCH_OUTCOME = displayed per-ID
SELF_CHECK = syntax/schema only (+transcript)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+deferred items remain explicit)
