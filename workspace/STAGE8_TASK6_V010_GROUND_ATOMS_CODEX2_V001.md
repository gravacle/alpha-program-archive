# STAGE8 TASK 6 / TRANCHE — V010 ground-atom resolution and Builder A re-pin

**Artifact:** `STAGE8_TASK6_V010_GROUND_ATOMS_CODEX2_V001.md`  
**Lane:** Codex 2 / Builder A  
**Date:** 2026-08-08  
**Status:** SEALED BUILD REPORT — specification and static package work only; no evaluator chain invoked

## 1. Preflight and custody

[PROVABLE] The commissioned context identifies register head `Q-614` and the
single run-031 replay fault: `C-B-V009-06` lacked a producer-carried
`r_ground`. The adjudication makes that omission conformant because both
comparison operands are available independently to R9 through P0 and the
sealed descriptor.

[PROVABLE] The immutable carriage base verified before use:

```text
STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V009.md
SHA-256 = 900a240df2bfdee5867eb589ae88c7f282810a8c7718999ad5cdf2bfb3f80698
BYTE_LENGTH = 182779
```

Before writing, the V010 specification, this report, and their sidecars were
absent in both the cleanroom and archive workspace. V009 was not overwritten.

## 2. The one V010 law statement

`STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V010.md` is a byte-copy of V009 plus
one named law statement, `V010-M1 — R9 alone resolves closed ground atoms`, and
only the mechanically consequent header, base-pin, fixture-span, carriage, and
terminal-scope updates.

The qualifying atom class is closed, not example-driven:

```text
schema = rd22.r9-ground-atom.v001
atom_class = P0_EVIDENCE_SHA256_EQ_SEALED_SPEC_SHA256
opcode = COMPARE
evidence operand = P0.evidence_files[member_key].sha256, recomputed by R9
constant operand = a literal *_SHA256 value in the same sealed descriptor
mask = []
producer dependency = none
```

The closed schema admits either operand order and requires the complete atom,
result name, P0 member binding, and literal constant to occur in the same
sealed descriptor. All non-`COMPARE` opcodes and every other `COMPARE` form are
excluded. R9 constructs and evaluates the atom from those sources alone. A
producer invocation or result object for the atom is a BR-1 contract fault.
The row's singular seven-field invocation remains the structured-evidence
carrier; for `C-B-V009-06` it remains `r_dag`, while R9 resolves `r_ground`.

## 3. Byte-derived finite delta

The carriage census was generated with `/usr/bin/diff -U 3`, excluding only
the two file headers. A provisional transcription of `5/112/15` was rejected;
the byte-derived result includes the distinct preflight hunk:

```text
FINAL_HUNKS = 6
FINAL_INSERTIONS = 118
FINAL_DELETIONS = 21
UNASSIGNED_HUNKS = 0
DESCRIPTOR_ROWS_CHANGED = 0
V010_BYTE_LENGTH = 187737
V010_SHA256 = 31ccee9c45c885e4e379fa1750f38695e293151e74bd8f8c15a5f0ccf23bfc19
```

| Hunk class | Authorized content |
|---|---|
| header/status | Advance V009 to V010 and state the one-law scope. |
| preflight/authority | Record Q-614 and pin immutable V009. |
| V010-M1 | Install the one closed ground-atom schema and R9/BR-1 rule. |
| fixture spans | Regenerate the three structural-fixture byte spans after the insertion; fixture row bodies are unchanged. |
| carriage certificate | Record this complete byte-derived delta. |
| terminal scope | Advance the terminal version/base statements only. |

All 66 descriptor row bodies compare byte-identically V009 to V010. The
protected anchor-bounded blocks also remain unchanged:

```text
runtime pin §9.1 = 712a861aaf5f2f43590f41405435663dff8efd52a93e30d33cc2399636442172
authority firewall = a9e7e50afb466ead16c43b45352d1c04273bb9c3e5671f5f7c386df70cdf0afa
aggregate rule §9.5 = bfad44417f766cc97a8942a8ffab7f9accd5791a2c2f1169a6534f3643543648
```

## 4. Code finding and package re-pin

The adjudicated producer behavior was inspected from bytes. The emitted
`C-B-V009-06` check row has one seven-field invocation, `r_dag`; its observed
payloads reproduce the graph argument and raw grounding span; no emitted
`r_ground` result object exists. That is exactly V010-M1.

The evaluator code therefore required zero change. Direct byte comparisons
against the registrar-mirrored pre-task package passed:

```text
parent.py   = a09f333a133deb28f57f4dda5b78fd54f708c553b0c5ec1df98d3682c79100cc  UNCHANGED
producer.py = 3c27890533eebe485f1f41688a7268d3898e6b1582ce933164113db28ba737a8  UNCHANGED
```

The package's generated pins, manifests, evidence copy, and static guards did
move as required. This is the complete final package delta relative to the
sealed 41-file G2 package:

| Path | Before SHA-256 | After SHA-256 | Reason |
|---|---|---|---|
| `README.md` | `b0e32d772a98abf52f65592d1fbe784ea3a06d280fccb498f6189d3bfc439327` | `15ba021ae3294cd152021e2af30d6c4f9c1473631cb2df8f70841856627569cb` | V010 scope and pending B re-pin disclosure. |
| `checks/check_map.json` | `a5bf6148a37095e857c0ef4b1bb32bfe078874f9b89b7773f27f8c35109c0ba3` | `f2028759d84f2c12894157ab67738e6220542e7abc1d39d16844bea5d887f82f` | Current spec root only; all 66 descriptor digests unchanged. |
| `fixtures/fixture_manifest.json` | `5548a26304351eaba0160d54d6ac1084d426413429a17fc8c3501f123869dd49` | `7711cd092cf138f4d96229dc0b9c1b294e8343d805e0cb879f04d8187439e2a6` | V010 source path/root and three generated spans. |
| `inputs/evidence/31ccee9c…--STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V010.md` | absent | `31ccee9c45c885e4e379fa1750f38695e293151e74bd8f8c15a5f0ccf23bfc19` | Content-addressed V010 evidence copy. |
| `inputs/structural_evidence_manifest.json` | `aabed7c27d2ee9baa905af5f6843c63bd6c5d8e8deb388de04c38055962a554a` | `6d1a49f96e6b6e9718ba1d3f79a989fd34ba7f2b01c1d74102f2e0b5251e87d1` | V010 references, payload inventory, declared root. |
| `inputs/subject_lineage_manifest.json` | `3ddd0530494a65456e5bc7f371b215d84591c34cd130dcb288c96d670831f8ee` | `8bb35b3ec27a1d3e2494cbfb940fdf47de1cc10182df0970f57192ac263ea0ae` | Regenerated manifest roots. |
| `manifests/normal.json` | `2b979384fa3fb2fc8b0add0e2e063831b81bf3786e69ca9c45cb1d371bd2f1d5` | `8f897b4044d7ceb404023eed4a6fbc68db668993137ba0a6d27a178739d2f030` | V010 pin and regenerated package carriers. |
| `manifests/optimized.json` | `c06cce955351d6138171cd8c9a482e2debaeea931ca58b512d0e18352dc10cb9` | `94b0562c7bddc0c50a48a609f9ee321012d0e0d62d3e6b004951fce8df90a278` | Same, optimized mode. |
| `manifests/pins.json` | `92b80de0a57615fd2d9f2e9a337d62e314ca86608d9dc86a4e3d16b5ecdbce9b` | `b8ea0ef93c6d5850a727c643f710580e9e995b211d372f3c7cd274014e1d865d` | 25 generated pins: V010 current plus V009 immutable base. |
| `tools/generate_pins.py` | `50f5afd8c865a4a904d3e0845b56a14aa35173c378a1cc13d89a652414a2a898` | `e5b20edd038f64a0cbf410520d57b6d5c1cdea81835ecfa3bc629c4f82bb19bd` | Generate V010 and V009-base pins. |
| `tools/materialize.py` | `3849138ccf51f18e647958820da13caf4336261ef762c4230d1dab59373b68b8` | `df49bbb02dd3d2d8ee0486a45bd572ec588f25392dee4f0bb9882561c94c0199` | Materialize V010 carriers and prune only superseded generated V010 copies. |
| `tools/self_check.py` | `246e0d5426f0f275c6a209c65fad9f61d5866c2cfb2f0288e45900513be5d436` | `5f95c3d7c2c2d6e195d8ab7f66d09911f8aee9d787397080160ab4c4b4292d77` | V010 row/schema/carriage/omission guards and dry-run fixture. |
| `manifests/package_inventory.json` | `fa394d58bc1799f2d0b6c4ec0b7a89d05f0ba22c2d79cffc030d41736b2744d4` | `b4c103e66f609bece182ce757004b643139348ca8ce56baa1f1d49cca3b311f3` | Complete 42-file final inventory. |

No other package path changed. No schema, descriptor, parent, or producer code
was edited.

## 5. Pin closure and dry run

A full package search used both the superseded current-spec filename and its
full digest. Every remaining occurrence is an explicit immutable-base
reference or content-addressed base payload:

```text
V009_NAME_HITS = 15
V009_VALUE_HITS = 11
PIN_CLOSURE_HITS = 26
UNJUSTIFIED_HITS = 0
```

Builder B's currently sealed V009 instance remains pinned and byte-verified:
thirteen members, root
`10622f170b979ae83ad8b496bafac41087b976512025669f5b38a97c028af488`.
Because Builder B performs the V010 re-pin next, the parent dry-run derived a
clearly non-authoritative V010-shaped fixture from that sealed instance,
preserved its exact thirteen-member package root, and replaced only the seven
input roots with the current V010 values and the lawful unbound ledger
sentinel. The parent then executed manifest validation, run-scoped ledger
binding, post-production carrier validation, and isolated direct-script command
construction. It launched no process.

```text
DRY_RUN_INSTANCE = NON_AUTHORITATIVE_V010_REPIN_FIXTURE
PARENT_MANIFEST_VALIDATION = PASS
POST_PRODUCTION_BINDING = PASS
DIRECT_SCRIPT_COMMAND_CONSTRUCTION = PASS
B_REPIN_STATE = PENDING_PARALLEL_B_V010_REPIN
```

## 6. Static transcript and batteries

```text
generate_pins: pins=25 sha256=b8ea0ef93c6d5850a727c643f710580e9e995b211d372f3c7cd274014e1d865d
materialize: checks=66 structural=56 gated=10 fixtures=6
self_check: syntax=6 canonical_json=all local_schemas=10
self_check: descriptor_delta=0:V009_to_V010 v010_bsd_diff=6/118/21
self_check: ground_atom_schema=PASS ground_atom_omission=PASS
self_check: evidence_payloads=18 inventory=42 pin_closure=26:PASS
self_check: parent_manifest_dry_run=PASS_NON_AUTHORITATIVE_V010_REPIN_FIXTURE
self_check: chain_invoked=false
```

F_PLDEC is CLEAN: no physical quantity was evaluated. Anti-tuning is CLEAN.
M-2 remains unchanged. The ten gated rows remain non-starting. No member
binding, fixed-point execution, end test, numerical evaluation, measured-
constant comparison, authorization claim, board mutation, or seal mutation
occurred. `evaluator_build_A/outputs/` contains zero files.

The final artifact pin check is the sealed sidecar comparison reported with
this artifact. The verb audit applies the verdict-line scope rule: historical
and quoted verbs are not present-tense action claims; the present-tense claims
above are supported by displayed byte, diff, schema, inventory, and dry-run
checks.

SPEC_DELTA = one statement only / (+6 hunks, 118 insertions, 21 deletions)
ROWS_CHANGED = 0
CODE_CHANGED = none
PIN_CLOSURE = 26 hits, all resolved
DRY_RUN = executed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
