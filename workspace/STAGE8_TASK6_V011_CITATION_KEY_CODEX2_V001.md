# STAGE8 TASK 6 / TRANCHE — V011 citation key and Builder A re-pin

**Artifact:** `STAGE8_TASK6_V011_CITATION_KEY_CODEX2_V001.md`  
**Lane:** Codex 2 / Builder A  
**Date:** 2026-08-08  
**Status:** SEALED BUILD REPORT — specification and static package work only; no evaluator chain invoked

## 1. Preflight and pinned findings

[PROVABLE] The commissioned context identifies register head `Q-615`. Before
writing, the V011 specification, this report, and both sidecars were absent in
the cleanroom and archive workspace.

The immutable V010 carriage base and Builder B's sealed finding verified:

```text
V010 specification = 31ccee9c45c885e4e379fa1750f38695e293151e74bd8f8c15a5f0ccf23bfc19
Builder B resolver report = 08a6bb7bfbc52c57af86f68d55febbd2c2c74859032009c267ff719b6eae2099
Builder B manifest = 1217571eadda90b114bf9f25433d7b8e9e58c6d9a114e3302c9659b637b2522f
Builder B member census = 14 instance-declared rows
Builder B root = ddc09a3d5b29ca1a775f8e9db33c4479baa4bb28c46c6186ca82ebcf8b7385a4
Builder B verdict schema = 93a1feb87df49a0b38784fd34387eaee8d4f87ab1c1cb5c7206991a713da27f5
```

The report's condition-2 finding was adopted without reading or importing
Builder B code. Both reachable unstated mappings are excluded: a payload
filename is producer-chosen, while lookup by the comparison constant collapses
to forbidden digest self-reference.

## 2. The one V011 statement

V011 adds one named law statement only:
`V011-O1 — condition-2 citation-key amendment to
rd22.r9-ground-atom.v001`. Its complete content is one closed JSON Schema; no
free-prose mapping accompanies it.

The schema fixes the resolution rule exactly:

```text
amends = rd22.r9-ground-atom.v001
condition = 2
descriptor citation = SEALED_DESCRIPTOR_ROW.atom[result_name].source_and_span
P0 table = R9.P0.evidence_files_by_citation
key fields = [source_sha256, span]
interval = ZERO_BASED_HALF_OPEN
match = EXACT_TUPLE_EQUALITY
cardinality = EXACTLY_ONE
member binding = MEMBER_KEY_BINDS_EXACT_ROW_MATCHING_DESCRIPTOR_ATOM_CITATION
forbidden mappings = [PAYLOAD_FILENAME, CONSTANT_DIGEST_SELF_REFERENCE, PRODUCER_SUPPLIED]
```

The citation contains a lowercase SHA-256 source identity and exactly two
non-negative span endpoints. The P0 index consumes the source-and-span tuple
carried for that atom by the sealed descriptor; `member_key` binds only the
unique matching row. No filename, comparison-constant lookup, or producer
mapping is admitted.

## 3. Finite specification delta

V011 was built by byte-copy of V010 followed by named replacements. The
carriage census is generated with `/usr/bin/diff -U 3`, excluding only the two
file headers:

```text
V011_SHA256 = d48e0fa7cbb41cb1b347d9c47475d3b2d749112d7c07f9a658df2bce001c1b63
V011_BYTE_LENGTH = 191830
FINAL_HUNKS = 7
FINAL_INSERTIONS = 111
FINAL_DELETIONS = 24
UNASSIGNED_HUNKS = 0
DESCRIPTOR_ROWS_CHANGED = 0
```

| Hunk class | Exact scope |
|---|---|
| header/status | Advance V010 to V011 and state the one-amendment scope. |
| preflight/base pin | Record Q-615 and immutable V010. |
| membership sentence | Remove the stale numerical census; membership remains sealed manifest-instance data. |
| V011-O1 | Install the one closed citation-key schema amendment. |
| fixture spans | Regenerate the three structural-fixture source spans after insertion; row bodies stay unchanged. |
| carriage certificate | Record the complete byte-derived delta. |
| terminal scope | Advance only the version/base statements. |

All 66 descriptor row bodies are byte-identical V010 to V011. The protected
anchor-bounded blocks remain unchanged:

```text
runtime pin §9.1 = 712a861aaf5f2f43590f41405435663dff8efd52a93e30d33cc2399636442172
authority firewall = a9e7e50afb466ead16c43b45352d1c04273bb9c3e5671f5f7c386df70cdf0afa
aggregate rule §9.5 = bfad44417f766cc97a8942a8ffab7f9accd5791a2c2f1169a6534f3643543648
```

## 4. Code finding and complete package delta

The producer's single `C-B-V009-06` invocation remains `r_dag`; its citation
linkage already carries `source_sha256` and the half-open span. The parent
already consumes verifier-root membership from the sealed manifest instance.
Neither evaluator program needs to adopt the independently owned R9 mapping.

Direct byte comparison with the registrar-mirrored V010 package passed:

```text
parent.py   = a09f333a133deb28f57f4dda5b78fd54f708c553b0c5ec1df98d3682c79100cc  UNCHANGED
producer.py = 3c27890533eebe485f1f41688a7268d3898e6b1582ce933164113db28ba737a8  UNCHANGED
```

The complete package delta relative to the sealed 42-file V010 package is:

| Path | Before SHA-256 | After SHA-256 | Reason |
|---|---|---|---|
| `README.md` | `15ba021ae3294cd152021e2af30d6c4f9c1473631cb2df8f70841856627569cb` | `cea73388830ebc7d2f9e0b8baa792b31f1d5b4b48726206b8da82d6423b5a262` | V011 and 14-member B-instance disclosure. |
| `checks/check_map.json` | `f2028759d84f2c12894157ab67738e6220542e7abc1d39d16844bea5d887f82f` | `76ff7bd91c4e2b9c059e84f4b3ec1a9df406c7e91d2a16f8772c98b089ee8025` | Current spec root only; 66 descriptor digests unchanged. |
| `fixtures/fixture_manifest.json` | `7711cd092cf138f4d96229dc0b9c1b294e8343d805e0cb879f04d8187439e2a6` | `a79225e054ed028f6158206e84de40dba54a4686a9295ade89f71be280618f8b` | V011 path/root and generated spans. |
| `inputs/evidence/d48e0fa7…--STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V011.md` | absent | `d48e0fa7cbb41cb1b347d9c47475d3b2d749112d7c07f9a658df2bce001c1b63` | Content-addressed V011 copy. |
| `inputs/structural_evidence_manifest.json` | `6d1a49f96e6b6e9718ba1d3f79a989fd34ba7f2b01c1d74102f2e0b5251e87d1` | `3bc82fc66f7dfa435462a233e4a71ab00cf741d28146f37e116e2ea11d753af4` | V011 references, inventory, declared root. |
| `inputs/subject_lineage_manifest.json` | `8bb35b3ec27a1d3e2494cbfb940fdf47de1cc10182df0970f57192ac263ea0ae` | `15ae97ed3171054febc425a6bc69eda3436fb0c89b2fd813ec487c929d8fb4b1` | Regenerated roots. |
| `manifests/normal.json` | `8f897b4044d7ceb404023eed4a6fbc68db668993137ba0a6d27a178739d2f030` | `0192739185412dab7dd5a5f3db343db7eb15038aca87731cfee017f96815a5f6` | V011 and current B pins. |
| `manifests/optimized.json` | `94b0562c7bddc0c50a48a609f9ee321012d0e0d62d3e6b004951fce8df90a278` | `11a114d420aa3535389960c8ceebc55613ba723f4ec49fa4636a85455835868e` | Same, optimized mode. |
| `manifests/pins.json` | `b8ea0ef93c6d5850a727c643f710580e9e995b211d372f3c7cd274014e1d865d` | `09e3db560ee5e642c69a9dbfc63882c4c119eaa5340ed0ce5b557a39a33db29c` | 26 generated pins, including V010 base and current B resolver artifacts. |
| `tools/generate_pins.py` | `e5b20edd038f64a0cbf410520d57b6d5c1cdea81835ecfa3bc629c4f82bb19bd` | `8143839b25418b8cbe6e9e1d720be843e0ad717dac06e159a467851002725e74` | V011/base/current-B pin sources. |
| `tools/materialize.py` | `df49bbb02dd3d2d8ee0486a45bd572ec588f25392dee4f0bb9882561c94c0199` | `071d61880083905db3cfe88de3f1e70fd9802d050032af168034d12133dbce7a` | V011 carrier materialization. |
| `tools/self_check.py` | `5f95c3d7c2c2d6e195d8ab7f66d09911f8aee9d787397080160ab4c4b4292d77` | `1184c6b137be2cdf1f6de771f2bfd9a0e7f915665e2e839ad4e63e8bbba7841f` | Citation-schema, 14-member, closure, and V011 dry-run guards. |
| `manifests/package_inventory.json` | `b4c103e66f609bece182ce757004b643139348ca8ce56baa1f1d49cca3b311f3` | `d1cd7e700229d83baf5327429fc007bc65d1fc9dcd8439f48df8c73c3a1b0760` | Complete 43-file inventory. |

No other package path changed. No evaluator schema, descriptor, parent, or
producer code was edited.

## 5. Pin closure and dry run

The V010 filename and full digest were searched across every package file.
Every survivor is an explicit immutable-base reference or its
content-addressed payload:

```text
V010_NAME_HITS = 15
V010_VALUE_HITS = 11
PIN_CLOSURE_HITS = 26
UNJUSTIFIED_HITS = 0
```

The parent dry-run used Builder B's real sealed V010 manifest and all fourteen
declared package members as the source of a clearly non-authoritative
V011-shaped fixture. Only the input roots were replaced with current V011
values and the lawful unbound-ledger sentinel. Manifest validation,
post-production ledger binding, carrier validation, and direct-script command
construction all executed; no child process launched.

```text
DRY_RUN_INSTANCE = NON_AUTHORITATIVE_V011_REPIN_FIXTURE
PARENT_MANIFEST_VALIDATION = PASS
POST_PRODUCTION_BINDING = PASS
DIRECT_SCRIPT_COMMAND_CONSTRUCTION = PASS
B_REPIN_STATE = PENDING_PARALLEL_B_V011_REPIN
```

## 6. Static transcript and batteries

```text
generate_pins: pins=26 sha256=09e3db560ee5e642c69a9dbfc63882c4c119eaa5340ed0ce5b557a39a33db29c
materialize: checks=66 structural=56 gated=10 fixtures=6
self_check: syntax=6 canonical_json=all local_schemas=10
self_check: verifier_root_members=14 verifier_root=ddc09a3d5b29ca1a775f8e9db33c4479baa4bb28c46c6186ca82ebcf8b7385a4
self_check: descriptor_delta=0:V010_to_V011 v011_bsd_diff=7/111/24
self_check: ground_atom_schema=PASS citation_key_schema=PASS ground_atom_omission=PASS
self_check: evidence_payloads=19 inventory=43 pin_closure=26:PASS
self_check: parent_manifest_dry_run=PASS_NON_AUTHORITATIVE_V011_REPIN_FIXTURE
self_check: chain_invoked=false
```

F_PLDEC is CLEAN; no physical quantity was evaluated. Anti-tuning and M-2 are
unchanged. The ten gated rows remain non-starting. No member binding,
fixed-point execution, end test, numerical evaluation, measured-constant
comparison, authorization claim, board mutation, or seal mutation occurred.
`evaluator_build_A/outputs/` contains zero files.

The verb audit follows the verdict-line scope rule. Present-tense action claims
are supported by the displayed pins, byte comparisons, schema checks, finite
diff, generated inventory, and dry-run transcript.

SPEC_DELTA = one statement only / (+7 hunks, 111 insertions, 24 deletions)
ROWS_CHANGED = 0
CODE_CHANGED = none
PIN_CLOSURE = 26 hits, all resolved
DRY_RUN = executed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
