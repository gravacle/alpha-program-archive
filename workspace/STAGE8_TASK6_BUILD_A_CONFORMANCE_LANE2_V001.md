# STAGE 8 / TASK 6 / BUILD A — CONFORMANCE TO THE SEALED INTEGRATION ADDENDUM — LANE 2 V001

Lane: Lane 2, Builder A of the RD-22 custody graph  
Task: PASTE 650 / conform `evaluator_build_A/` to the sealed V005 integration addendum  
Disposition: three contracts conformed; every changed package file disclosed; static checks only  
Authority claimed by this artifact: none

```text
REGISTER_HEAD = Q-588 (verified before reading the addendum)
GOVERNING_SPEC = f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b
SEALED_ADDENDUM = d17c5e79986bea431dec0b572019096f9c059bcc43876fda9134abc96ce0f260
PRIOR_BUILD_MANIFEST = 767586aff845886c2fb98959dcd05aa278c20008253404731e01c0a9c52f3981
DELTA_BASE = archive mirror of the package inventoried by the prior sealed build manifest
DELTA_CONVENTION = file-level rows; recursive byte diff; canonical one-line JSON counts as one inserted and one deleted line
DELTA_FILES = 17
DELTA_HUNKS = 72
DELTA_INSERTIONS = 468
DELTA_DELETIONS = 171
PACKAGE_FILES = 21 (20 self-addressed rows plus package_inventory.json)
CHAIN_INVOKED = false
```

## 1. Preflight and custody

| Check | Result |
|---|---|
| Register head | Q-588 verified. |
| Governing spec | Cleanroom `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md` rehashed to `f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b`. |
| Sealed addendum | Cleanroom copy rehashed before reading to `d17c5e79986bea431dec0b572019096f9c059bcc43876fda9134abc96ce0f260`; its sidecar rehashed to `9f24d57ca3bc0443c2e800868afa4659e5da4eeb250e9aca392b098cd4bae7d8`. |
| Prior Builder A manifest | Cleanroom sealed copy rehashed to `767586aff845886c2fb98959dcd05aa278c20008253404731e01c0a9c52f3981`; sidecar rehashed to `dc98a025dcc96762ff92410d98165415a2e69c39e19e3a05dfa73d4de440c772`. |
| Delta base | Before modification, the archive package copy matched the sealed Builder A package inventory at the checked files. It was then retained untouched and used only as the old-byte side of the recursive diff. |
| Output collision | Neither the artifact nor its sidecar existed in the cleanroom or archive workspace immediately before creation. |
| Runtime pins | Snapshot `50a6fc141a45451678aa7543e4f267ce26beb6e53182170b478acb6fb0e0f5bb`; gate `2ad7f72a88184c11e1253f2c47598fca11e60d05e8e71a26db4e19b16bf98d42`. |

The addendum is treated as installed law by Q-588. This artifact evaluates implementation conformance only; it does not ratify the addendum, either builder, any evaluator result, or any physical conclusion.

## 2. Contract conformance

### 2.1 A1 — event-ledger carriers

The prior Builder A terminal child object emitted the sealed eleven-field shape and therefore had no lawful digest carriers for process, network, or mutation events. The raw receipt carried process and network ledgers but omitted a mutation ledger. The replacement is exact:

- every terminal `children[]` row has 14 and only 14 fields;
- `process_event_ledger_sha256`, `network_event_ledger_sha256`, and `mutation_event_ledger_sha256` are SHA-256 digests of the canonical JSON arrays in the corresponding receipt;
- empty classes use SHA-256 of canonical `[]\n`, namely `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`, never `null` or omission;
- the raw receipt now has the `mutation_event_ledger` carrier;
- the parent reclassifies the raw event arrays and recomputes all six event/module/native digests when constructing the child row;
- producer mutation events are the two declared exclusive creations, `output` and `receipt`; undeclared process, network, environment, write, or mutation facts fail closed.

The pre-existing `module_ledger_sha256`, `native_ledger_sha256`, and `open_event_ledger_sha256` names were preserved. No harmonising rename was made.

### 2.2 A2 — fixture inventory and its two rules

The prior package had a five-field build descriptor and a six-field runtime fixture result using the untyped carrier `observed`. Those were Builder A inventions now overridden by the addendum.

The materialized descriptor now carries the ten static fields available before a run:

```text
fixture_id, source, fixture_spec_sha256, primary_check_ids,
execution_class, mutation_ids, deterministic_procedure, prerequisites,
required_gate, expected_verdict_fields
```

The producer emits exactly the addendum's sixteen runtime fields by adding the frozen `input_root_sha256` and the six result-side carriers. Every fixture source span is sliced from the sealed V005 table and rehashed to its `fixture_spec_sha256`. The census remains six fixtures: three STRUCTURAL and three GATED-EXECUTION.

Both rules are executable:

1. `observed_verdict_fields` keys outside the spec-fixed `expected_verdict_fields` key set produce `ERROR` with `FIXTURE_QUARANTINE_UNDECLARED_FIELDS`; they cannot produce `PASS`.
2. Expected values reside only in the content-addressed fixture manifest generated from the sealed §10 table. Evidence records may supply observations and evidence hashes, not expected values. The producer compares the observed record against that sealed record.

The three gated fixtures return `NOT_RUN_GATE`, `procedure_started=false`, empty observed carriers, and do not dispatch a procedure.

### 2.3 A3 — `rd22.verifier-manifest.v001`

The prior package invented a six-field verifier manifest containing `authority`, check/fixture pins, a package inventory, and one `verifier_source` row. The new parent rejects that shape. It requires canonical JSON, a sidecar pin, and exactly these eleven top-level fields:

```text
schema, verifier_root_sha256, entry_point, argv, optimize,
input_roots, output_path, receipt_path, stdout_discipline,
exit_contract, receipt_authoritative
```

The parent then validates:

- exact nested inventories: five `input_roots`, three `stdout_discipline` fields, and three `exit_contract` fields;
- the sealed spec, evidence, runtime snapshot, and runtime gate roots, plus a syntactically valid content root for the ledger that matches exactly one declared argv file;
- module entry-point syntax, string argv, Boolean `optimize`, and the verifier-root digest form;
- canonical one-line JSON stdout and no other stdout;
- declared output/receipt paths, resolved relative to the manifest location when relative;
- `receipt_authoritative=false`;
- the exact exit map `{verified:0,faults_found:1,fail_closed:2}`.

The verifier launches under the pinned interpreter as `-I -S -B`, optionally `-O`, then `-m <entry_point>` and the declared ordered argv. A missing manifest or sidecar stops before launch. Exit 1 is recorded as `R9_VERIFIER_FAULTS_FOUND_EXIT_1`; exit 2 is recorded separately as `R9_VERIFIER_FAIL_CLOSED_EXIT_2`. Both stop the chain, while only exit 0 can proceed toward R10. The verifier receipt remains evidence and is reclassified using the same closed event carriers.

The prior A-only output invention `rd22.verifier-output.v001` was also removed. Because the addendum makes stdout the verdict carrier, the parent and schema now accept the already sealed Builder B public carrier `gravacle.a35.verifier-verdict.v1`, with exact fields and checks for the spec, authorization, runtime, verifier self-root, independence, authority firewall, and success/finding consistency. This is disclosed integration work under A3, not an unstated fourth addendum contract.

## 3. Complete disclosed delta

The count `DELTAS = 17` is a file-level count. Each row accounts for one and only one file reported by the recursive byte diff. Compound changes inside a file are all named in that file's row. Canonical JSON files are one physical line, so the line counts are explicitly not used as a proxy for semantic size.

| # | File | Old shape / fact | New shape / fact | Addendum authority |
|---:|---|---|---|---|
| 1 | `README.md` | Required A's invented six-field manifest, one `verifier_source`, and an unspecified future adapter. | States the exact eleven-field manifest, isolated module launch, receipt evidence, and distinct terminal exits. | A3 §§3.2–3.3. |
| 2 | `fixtures/fixture_manifest.json` | Six rows of five fields: `fixture_id`, `primary_checks`, class, `frozen_input`, expected record. | Six content-addressed ten-field static descriptors feeding the exact sixteen-field runtime row; mutation IDs are explicit. | A2 §§2.2–2.3. |
| 3 | `inputs/structural_evidence_manifest.json` | Subject root excluded the addendum. | Root rebound to the six-file subject lineage that includes the sealed addendum; unavailable evidence facts otherwise unchanged. | Installed addendum as governing content; A2 input-root carrier. |
| 4 | `inputs/subject_lineage_manifest.json` | Five sealed subject files; root `a01065f0…`. | Adds the pinned addendum as the sixth file; root `d09f6b30…`. | All A1–A3; content addressing. |
| 5 | `manifests/normal.json` | No addendum input or mutation class; 14 runtime package files; old roots/hashes. | Pins the addendum, declares mutation events, inventories 15 runtime files including the verifier-manifest schema, and carries regenerated roots/hashes. | A1 and A3. |
| 6 | `manifests/optimized.json` | Same old omissions as normal mode. | Same addendum carriers as normal mode; only the pre-existing mode/optimization/writable-path triplet differs. | A1 and A3. |
| 7 | `manifests/package_inventory.json` | Twenty-file old package inventory. | Twenty self-addressed rows for a 21-file package; the inventory correctly excludes itself and includes the new schema. | E2; all regenerated hashes. |
| 8 | `parent.py` | Eleven-field child rows; no raw mutation carrier; six-field A-invented verifier gate; direct-script launch; generic nonzero-child failure; nine-field A output shape. | Fourteen-field child rows; raw mutation validation; exact A3 gate; isolated declared module launch; separate exit-1/exit-2 failures; canonical stdout parsing; exact fixture quarantine; Builder B public verdict carrier. | A1 §§1.2–1.3; A2 §2.3 rules 1–2; A3 §§3.2–3.3. |
| 9 | `producer.py` | Six-field fixture result with nullable `observed`; receipt omitted mutation events. | Exact sixteen-field fixture result; content roots and evidence hashes; spec-fixed expectation direction; undeclared-key quarantine; raw mutation-event ledger. | A1 §1.3; A2 §§2.2–2.3. |
| 10 | `schemas/child-receipt.schema.json` | Exact raw receipt without `mutation_event_ledger`. | Exact raw receipt with the mutation carrier. | A1 §§1.1–1.3. |
| 11 | `schemas/fixture-manifest.schema.json` | Exact five-field fixture descriptors. | Exact ten-field static descriptors; output-only fields remain outside the build manifest. | A2 §§2.2–2.3. |
| 12 | `schemas/producer-output.schema.json` | `fixtures[]` items were open generic objects. | `fixtures[]` items are closed exact sixteen-field rows with closed status/class enums and pinned source shape. | A2 §2.3 and both rules. |
| 13 | `schemas/terminal-ledger.schema.json` | `children[]` and `fixtures[]` were open generic objects. | Closed fourteen-field child rows and closed sixteen-field fixture rows. | A1 §1.3; A2 §2.3. |
| 14 | `schemas/verifier-manifest.schema.json` | File absent. | New closed schema: eleven top-level, five input-root, three stdout, and three exit fields. | A3 §3.2. |
| 15 | `schemas/verifier-output.schema.json` | A-invented nine-field `rd22.verifier-output.v001`. | Closed thirteen-field `gravacle.a35.verifier-verdict.v1`, matching the sealed Builder B stdout carrier. | A3 §3.3.2, disclosed integration consequence. |
| 16 | `tools/materialize.py` | Hard-coded five-field fixtures; eight generated schemas; addendum absent from roots and manifests. | Derives source-bound fixture descriptors; generates nine schemas; inserts addendum and mutation carriers; regenerates all affected inventories and roots. | A1–A3; E2. |
| 17 | `tools/self_check.py` | Checked the pre-addendum shapes only. | Rehashes the addendum; checks the complete 20-row self-inventory; validates 14/16/11 field counts, exact nested objects, empty-list digests, mutation carrier, fixture source spans, quarantine direction, and distinct exits. | A1–A3; E2 static verification. |

Recursive diff result under the declared convention:

```text
17 changed-or-added files
72 hunks
468 inserted physical lines
171 deleted physical lines
4 old package files byte-identical and absent from the delta:
  checks/check_map.json
  schemas/check-map.schema.json
  schemas/child-manifest.schema.json
  schemas/structural-evidence.schema.json
```

## 4. Updated package inventory

`manifests/package_inventory.json` contains 20 rows and intentionally omits itself to avoid a recursive digest. Its own row below makes the complete delivered package inventory 21 files.

| Relative path | Bytes | SHA-256 |
|---|---:|---|
| `README.md` | 3168 | `dbbc13b8e238015bf3f395109b39be5320e02cc3902a5bc613cc0c5bff4017c1` |
| `checks/check_map.json` | 107235 | `034ebf3e071051d25d5b7f8871a03193da5bc9ab16a7c07c7cae1bbb8f467e26` |
| `fixtures/fixture_manifest.json` | 7894 | `dc635a83fe39e62bdc2b76c8c40cfce977ac67fdaf0eede32344d0b98dabf2db` |
| `inputs/structural_evidence_manifest.json` | 6986 | `5d16733344981b03b8be31f11080b267481d1c5d1c3ea7117025e69464d5fb9b` |
| `inputs/subject_lineage_manifest.json` | 1510 | `e6918e0254d63671dd0fd3652290e4a0b1781abb6c4d63e81043f1d8f3327d54` |
| `manifests/normal.json` | 6741 | `0964e690e1517aa899d413e58fb707c452c69dd821de4cd95b8fedc4fef3e9e7` |
| `manifests/optimized.json` | 6750 | `c3b92f158892ffbab894bf8de33a2213524a5b06aa201c741dfcb2959e96dab5` |
| `manifests/package_inventory.json` | 2938 | `8c935a5683b847e5d22e2e6f47041ce966785b41d3eb52d8a6903ba88be09329` |
| `parent.py` | 36986 | `f07016cb7054d3696cd6e0f7552f81e74b8ee0f35cf8b55b7bd771e633b21831` |
| `producer.py` | 39550 | `810985048e3ca8a7f1250983d2940b814ed43b34de240648e3ed7b80dcd432b7` |
| `schemas/check-map.schema.json` | 456 | `8e971040ca4d96161303710bc391dd322cb581983c881eaf39b1547fb4e68192` |
| `schemas/child-manifest.schema.json` | 1420 | `f5325b40cd49db94e11cc44628ec46b6ac400489d99c574642461e0b8697ef1e` |
| `schemas/child-receipt.schema.json` | 1277 | `0ce216024263ee7b2de3643fc4b44cc1a581d7a2334968da8ebdf8b9d02fa7bf` |
| `schemas/fixture-manifest.schema.json` | 1347 | `3723297f9f9e9aa5b6e16f35a3315966d49997734c223580807b916ebfc4e986` |
| `schemas/producer-output.schema.json` | 2425 | `d3e4dc5c32e265ec5a8373b734f9d277573d862c97cb563f03c3e97f55e534b3` |
| `schemas/structural-evidence.schema.json` | 351 | `5d3ec96abcec19f664665f5a1bf316a9c4fa3d95aa66b8551de8036d85f97174` |
| `schemas/terminal-ledger.schema.json` | 3920 | `5635e68e13932915f6724f7a1aa2533fa52d8cc7170be9a44f09433ae9816af5` |
| `schemas/verifier-manifest.schema.json` | 1691 | `05cb23509293da9d8a184cd48a7f6cc1c36e56c3ab4114d8548bea8824fc9d15` |
| `schemas/verifier-output.schema.json` | 1476 | `145dfdf6aefa40766b9e680dd59714ffbd94133411ea89a0e7d7aab8d6f033ad` |
| `tools/materialize.py` | 29563 | `baf4f7aadc3204336c65b8db12a008302a0b47786e15a16f8516cb8162832c1e` |
| `tools/self_check.py` | 15563 | `6a856a9d98f7aa4c20496e9ed646e7796e2e10b4607294415e3cffbccd6c69af` |

Runtime manifest seals after regeneration:

```text
normal.json    = 0964e690e1517aa899d413e58fb707c452c69dd821de4cd95b8fedc4fef3e9e7
optimized.json = c3b92f158892ffbab894bf8de33a2213524a5b06aa201c741dfcb2959e96dab5
subject root   = d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688
```

## 5. Static self-check transcript

Permitted commands executed only source compilation, deterministic materialization, JSON/schema validation, hashing, and byte diffing. No parent, producer, check executor, fixture procedure, or verifier was launched.

```text
$ /usr/bin/python3 -I -S -B -c '<compile parent.py, producer.py, materialize.py, self_check.py>'
SOURCE_COMPILE_OK 4

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/materialize.py
{"checks": 66, "fixtures": 6, "gated": 10, "normal_sha256": "0964e690e1517aa899d413e58fb707c452c69dd821de4cd95b8fedc4fef3e9e7", "optimized_sha256": "c3b92f158892ffbab894bf8de33a2213524a5b06aa201c741dfcb2959e96dab5", "structural": 56, "subject_lineage_root": "d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688"}

$ /usr/bin/python3 -I -S -B evaluator_build_A/tools/self_check.py
SELF_CHECK_OK syntax=4 canonical_json=all schemas=9 inventory=20 checks=66 structural=56 gated=10 fixtures=6 fixture_fields=16 child_fields=14 verifier_manifest_fields=11 exits=0/1/2 chain_invoked=false

$ recursive byte diff against untouched archive package
DELTA_FILES=17 INSERTIONS=468 DELETIONS=171 HUNKS=72
```

The static check additionally confirmed: no Python `assert` node; all package JSON canonical; package inventories complete and rehashed; 66 unique descriptors split 56 STRUCTURAL / 10 GATED-EXECUTION; six fixtures split 3 / 3; nine schemas closed where required; all output and pycache directories empty.

## 6. PIN CHECK, fences, and verb audit

### 6.1 PRE-SEAL PIN CHECK

| Pin or invariant | Final check |
|---|---|
| Addendum artifact and sidecar | Exact hashes reverified after implementation and before this artifact's seal. |
| Spec V005 | Exact `f8d1a7dc…` reverified; not edited. |
| Prior sealed build manifest | Exact `767586af…` reverified; not edited. |
| Runtime snapshot and gate | Exact `50a6fc14…` and `2ad7f72a…` reverified. |
| Normal/optimized common content | Pair differs only in `mode`, `optimization`, and `writable_paths`; all package files and content roots identical. |
| Package inventory | Complete 20-row self-addressing inventory rehashed; the 21st/self file hash displayed separately. |
| Output and archive collision | Clear immediately before artifact creation; no overwrite performed. |
| Chain products | `evaluator_build_A/outputs/` and all three pycache directories empty. |

### 6.2 F_PLDEC and gate fences

No check descriptor, fixture, producer, parent, or verifier ran against the subject lineage. No physical quantity was evaluated; no measured constant was read or compared; no member was bound; no fixed point or end test executed. `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false` throughout. No fence blocked a structural build result, so `MACHINERY_APPEAL = none`.

### 6.3 Self verb audit under the verdict-line scope rule

| Verb | Audit |
|---|---|
| `conformed` | Limited to the three closed data/launch contracts in the sealed addendum; demonstrated by exact inventories, code branches, schemas, and static checks. It does not mean the chain or evaluator result passed. |
| `validates` | Means deterministic parent-side shape, pin, path, and value checks before or after the declared child launch. It does not attribute authority to a receipt. |
| `distinct terminal facts` | Exit 1 and exit 2 have separate named fail-closed codes and neither can enter R10. No claim is made that either exit was exercised here. |
| `complete delta` | Means every file found by recursive old/new byte diff is one of the 17 displayed rows; four unchanged files are named. It does not claim unchanged bytes outside `evaluator_build_A/`. |
| `self-check passed` | Syntax/schema/hash/static inventory only. The transcript explicitly says `chain_invoked=false`. |
| `sealed` | Applies only after the adjacent sidecar is created and both hashes are reported; it grants no substantive authorization. |

CONFORMED = 3/3 contracts
DELTAS = 17 disclosed (+table)
SELF_CHECK = passed (+transcript)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN / (+scope-limited conformance; distinct unexercised exit facts; static-only self-check; authorization not claimed)
