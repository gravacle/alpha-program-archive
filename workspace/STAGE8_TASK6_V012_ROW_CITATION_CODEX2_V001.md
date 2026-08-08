# STAGE8 TASK 6 / TRANCHE — V012 row citation and source supply

**Artifact:** `STAGE8_TASK6_V012_ROW_CITATION_CODEX2_V001.md`  
**Lane:** Codex 2 / Builder A  
**Date:** 2026-08-08  
**Status:** SEALED BUILD REPORT — one descriptor-linkage amendment and evidence supply; no evaluator chain invoked

## 1. Preflight and pins

[PROVABLE] The commissioned context identifies register head `Q-616`. Before
writing, the V012 specification, this report, and both sidecars were absent in
the cleanroom and archive workspace.

The governing and Builder B inputs verified before use:

```text
V011 specification = d48e0fa7cbb41cb1b347d9c47475d3b2d749112d7c07f9a658df2bce001c1b63
Builder B citation-resolver report = 883bd089433596ce749f579806019e58d3c6ae441d0397be30eb1d09d214abf3
Builder B manifest = d4219a53f26aa19dad3b1119ee7f1cc7d4c9816b64b02b3f1c1efbea7a884d8a
Builder B member census = 14 instance-declared rows
Builder B root = 2cf5f313a44e12859d199184c863e92bc8662073a3695ffb2c0ea7f535900652
Builder B verdict schema = 757943f84d60be88d098cca3bfcde5f04ed3c85b02b807481ac0a2f959f9edb1
provenance source = 13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd
provenance source bytes = 36108
source span [18898,19830) = 932 bytes, SHA-256 47e7c32915bc756fb5f6be25c4fc6dec5c079c8837176dc62499e0f34f4c9d3b
```

The sealed source digest occurs zero times in V011. V012 supplies both missing
parts: the row's own source identity and the full sealed source bytes.

## 2. Whole descriptor-row display

The complete exact row before and after follows. Each diff marker is outside
the row bytes; removing it yields the full UTF-8 row, excluding only its line
terminator.

```diff
-| `C-B-V009-06` | STRUCTURAL | principal-ruled sealed `stage_dependencies` encoding at `provenance/boundary_incidence_dynamics_preregistration_v011.json` bytes `[18898,19830)`; `STAGE_DEPENDENCIES_MEMBER_SHA256=47e7c32915bc756fb5f6be25c4fc6dec5c079c8837176dc62499e0f34f4c9d3b`; precedence decision `70c4080eae018bd644a3f0694557f1c0e854d621aa61097c775737887fec528f` | `r_ground:=COMPARE(P0.evidence_files[stage_dependencies_member].sha256,STAGE_DEPENDENCIES_MEMBER_SHA256,empty)`; `r_dag:=DAG(stage_dependencies,PRINCIPAL_SINGLE_AUTHORITY)` parses/types the node-parent lists and rejects cycles, self-parenting, and missing parents. By principal ruling, `stage_dependencies` is one sealed object serving as both graph and required-parent schema; the parent-comparison clause is discharged by that identity, never by synthesizing `COMPARE(X,X)` or duplicating the object as two independently authored arguments. | `P0 and r_ground.success and r_dag.success` |
+| `C-B-V009-06` | STRUCTURAL | principal-ruled sealed `stage_dependencies` encoding at `provenance/boundary_incidence_dynamics_preregistration_v011.json` with `source_sha256=13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd` bytes `[18898,19830)`; `STAGE_DEPENDENCIES_MEMBER_SHA256=47e7c32915bc756fb5f6be25c4fc6dec5c079c8837176dc62499e0f34f4c9d3b`; precedence decision `70c4080eae018bd644a3f0694557f1c0e854d621aa61097c775737887fec528f` | `r_ground:=COMPARE(P0.evidence_files[stage_dependencies_member].sha256,STAGE_DEPENDENCIES_MEMBER_SHA256,empty)`; `r_dag:=DAG(stage_dependencies,PRINCIPAL_SINGLE_AUTHORITY)` parses/types the node-parent lists and rejects cycles, self-parenting, and missing parents. By principal ruling, `stage_dependencies` is one sealed object serving as both graph and required-parent schema; the parent-comparison clause is discharged by that identity, never by synthesizing `COMPARE(X,X)` or duplicating the object as two independently authored arguments. | `P0 and r_ground.success and r_dag.success` |
```

The byte-level delta is one insertion:

```text
OLD_ROW_BYTE_LENGTH = 957
NEW_ROW_BYTE_LENGTH = 1043
COMMON_PREFIX_BYTES = 154
INSERT_OFFSET = 154
INSERTED_UTF8 = with `source_sha256=13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd` 
INSERTED_HEX = 776974682060736f757263655f7368613235363d313363663165313738613966646365643838353930393938393834656330346538346564383363303638316236386463636431316234653337643661666163646020
INSERTED_BYTE_LENGTH = 86
COMMON_SUFFIX_BYTES = 803
OLD_ROW_SHA256 = b63a1335f20f71a3cd02f2192b4d696576344fd6ae28464ba543e6efba4643c0
NEW_ROW_SHA256 = da486b9a044bd8c1354f809ba5212a9da78a66dd0fcddaee18a19ed740707560
```

Column splitting produces five columns before and after. Exact byte comparison
confirms columns 0, 1, 3, and 4 are identical: criterion ID, execution class,
deterministic procedure, and expected predicate. Only the sealed-input/
citation column changes. This is linkage completion, not a criterion,
procedure, or predicate change.

## 3. Specification finite delta

V012 was built by byte-copy of V011 followed by named replacements. The
carriage census uses `/usr/bin/diff -U 3`, excluding only the two file headers:

```text
V012_SHA256 = 382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504
V012_BYTE_LENGTH = 197462
FINAL_HUNKS = 6
FINAL_INSERTIONS = 89
FINAL_DELETIONS = 21
UNASSIGNED_HUNKS = 0
DESCRIPTOR_ROWS_CHANGED = 1
CHANGED_ROW = C-B-V009-06
CHANGE_CLASS = LINKAGE_ONLY
UNCHANGED_ROWS = 65
```

The six hunks are the header/status, Q-616/base pin, exact row insertion,
mechanically regenerated fixture spans, full row/delta carriage certificate,
and terminal scope. No other descriptor row changes. The protected runtime
pin, authority firewall, and aggregate rule remain byte-identical to V011.

## 4. Source supply

The exact 36,108-byte provenance source was copied without modification to:

```text
inputs/evidence/13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd--boundary_incidence_dynamics_preregistration_v011.json
```

The structural evidence manifest now carries it in all applicable closed
surfaces:

```text
payload_inventory row = {relative_path, byte_length:36108, sha256:13cf1e17…}
C-B-V009-06 evidence.input_files = 3 rows (full source, exact span, DAG args)
C-B-V009-06 payload role = SEALED_CITATION_SOURCE_BYTES
PAYLOAD_CENSUS = 21
DECLARED_ROOT = 82d6f1a049a9ee4598fdb52f20e0125b7653007234be104ca68fcbc7ab9fc2ac
```

This raises the prior 19 payloads by exactly two: the retained-base transition
adds the content-addressed V012 specification and Q2 adds the cited source.
The V011 payload remains as the immutable base.

## 5. Dry run and code finding

The producer dry-run loaded the amended descriptor hash, validated the
three-file evidence root, returned the same structural PASS atom set, and
emitted the row's singular seven-field `r_dag` invocation with
`source_sha256=13cf1e17…`, span `[18898,19830)`, and span digest `47e7c329…`.
No `r_ground` producer result was emitted.

The parent evidence-supply dry-run staged all 21 evidence payloads into a fresh
run-root directory. The staged full source rehashed to `13cf1e17…`; the parent
then completed the non-authoritative V012 manifest validation, run-scoped
ledger binding, post-production carrier checks, and direct-script command
construction. No child process launched.

The generic producer and parent paths already support these data changes, so
their bytes remain unchanged from the sealed V011 package:

```text
parent.py   = a09f333a133deb28f57f4dda5b78fd54f708c553b0c5ec1df98d3682c79100cc
producer.py = 3c27890533eebe485f1f41688a7268d3898e6b1582ce933164113db28ba737a8
CODE_CHANGED = none
```

## 6. Complete package delta

The package grows from 43 to 45 inventoried files. The complete final delta
relative to the registrar-mirrored V011 package is:

| Path | Before SHA-256 | After SHA-256 | Reason |
|---|---|---|---|
| `README.md` | `cea73388830ebc7d2f9e0b8baa792b31f1d5b4b48726206b8da82d6423b5a262` | `48d6cb97caf5b436330814bf0ed1346ea4f582f5aa2561cfed775e3b96a0ca9e` | V012 one-row and source-supply scope. |
| `checks/check_map.json` | `76ff7bd91c4e2b9c059e84f4b3ec1a9df406c7e91d2a16f8772c98b089ee8025` | `280004821c532def203ae81cec35bcac26bd3ab4bdd03752f5196aa7b9c23f3d` | V012 root and one amended row hash. |
| `fixtures/fixture_manifest.json` | `a79225e054ed028f6158206e84de40dba54a4686a9295ade89f71be280618f8b` | `c94445a52379a62bfffe79d3a76f3187848600e389b301b005089f002e6c5a9d` | V012 path/root and generated spans. |
| `inputs/evidence/13cf1e17…--boundary_incidence_dynamics_preregistration_v011.json` | absent | `13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd` | Full cited sealed source. |
| `inputs/evidence/382052c4…--STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V012.md` | absent | `382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504` | Content-addressed V012 copy. |
| `inputs/structural_evidence_manifest.json` | `3bc82fc66f7dfa435462a233e4a71ab00cf741d28146f37e116e2ea11d753af4` | `20c68f9cf0eb81238bae0f0835e9d7a6e55a979818e783726b793e2cf0773bb0` | Source row, three-file check input, payload census/root. |
| `inputs/subject_lineage_manifest.json` | `15ae97ed3171054febc425a6bc69eda3436fb0c89b2fd813ec487c929d8fb4b1` | `3183a7477132790f886a4b692eb94c5ee165b8097fb11dfcc4172e59b57c26f9` | Regenerated V012 subject root. |
| `manifests/normal.json` | `0192739185412dab7dd5a5f3db343db7eb15038aca87731cfee017f96815a5f6` | `a386e8a98f47eff914345bff777df2ed5921cbf7fb6d8347a1455c6f6e08376a` | V012, current B, evidence, and package pins. |
| `manifests/optimized.json` | `11a114d420aa3535389960c8ceebc55613ba723f4ec49fa4636a85455835868e` | `be6c1f178c02fb90e968e5aae23de9fec8301734c22faad9de5a4fb8e2c9ab66` | Same, optimized mode. |
| `manifests/pins.json` | `09e3db560ee5e642c69a9dbfc63882c4c119eaa5340ed0ce5b557a39a33db29c` | `8eac1df48a828f754ff1142498c4d80a8955fd06429ba86f3fb8a89a0533cb70` | 27 generated pins including V011 base and current B artifacts. |
| `tools/generate_pins.py` | `8143839b25418b8cbe6e9e1d720be843e0ad717dac06e159a467851002725e74` | `a56bc42ad7d51b4028e63ee324def2df1ebb35c0059ad1e8f3f7f5224dd09258` | V012/base/current-B sources. |
| `tools/materialize.py` | `071d61880083905db3cfe88de3f1e70fd9802d050032af168034d12133dbce7a` | `85334bbe15065984f3469ec7dfbc1b4af3cc500f3467fc8ae7275717b8529ac7` | Row rehash and full source materialization. |
| `tools/self_check.py` | `1184c6b137be2cdf1f6de771f2bfd9a0e7f915665e2e839ad4e63e8bbba7841f` | `5ca2bdc394dd057cd491c8c85bb55e60bc7b25fec9c68df3404e376e386f9e4c` | Full row, column, source-stage, hash-closure, and dry-run guards. |
| `manifests/package_inventory.json` | `d1cd7e700229d83baf5327429fc007bc65d1fc9dcd8439f48df8c73c3a1b0760` | `fbcd75f25a935be75de928452b74436c411603277a4cf07f6b8aa89cd1fa15b9` | Complete 45-file inventory. |

No other package path changed.

## 7. Pin closure and batteries

The package-wide closure sweep reports:

```text
V011_NAME_HITS = 15
V011_VALUE_HITS = 11
OLD_ROW_HASH_HITS = 2
TOTAL_JUSTIFIED_HITS = 28
UNJUSTIFIED_HITS = 0
OLD_ROW_HASH_LIVE_RUNTIME_HITS = 0
```

The old row hash survives only in the content-addressed V012 audit display and
the static closure guard. It is absent from the live check map, evidence
descriptor binding, and child manifests.

```text
self_check: syntax=6 canonical_json=all local_schemas=10
self_check: inventory=45 evidence_payloads=21 citation_source_supply=PASS
self_check: descriptor_delta=1:C-B-V009-06:linkage_only
self_check: row_hash=b63a1335…->da486b9a…
self_check: v012_bsd_diff=6/89/21
self_check: parent_manifest_dry_run=PASS_NON_AUTHORITATIVE_V012_REPIN_FIXTURE
self_check: chain_invoked=false
```

F_PLDEC is CLEAN; no physical quantity was evaluated. Anti-tuning and M-2 are
unchanged. The ten gated rows remain non-starting. No member binding,
fixed-point execution, end test, numerical evaluation, measured-constant
comparison, authorization claim, board mutation, or seal mutation occurred.
`evaluator_build_A/outputs/` contains zero files.

The verb audit follows the verdict-line scope rule. Present-tense claims are
supported by the displayed byte comparison, generated pins, schema validation,
inventory reconciliation, and dry-run transcript.

SPEC_DELTA = row citation + source supply only / (+6 hunks, 89 insertions, 21 deletions)
ROWS_CHANGED = 1 (V009-06, linkage only, before/after displayed, criterion byte-identical)
PAYLOAD_CENSUS = 19 -> 21
ROW_HASH = b63a1335f20f71a3cd02f2192b4d696576344fd6ae28464ba543e6efba4643c0 -> da486b9a044bd8c1354f809ba5212a9da78a66dd0fcddaee18a19ed740707560
CODE_CHANGED = none
PIN_CLOSURE = 28 hits, all resolved
DRY_RUN = executed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
