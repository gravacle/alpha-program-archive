# STAGE8 TASK 6 / TRANCHE — V008 + seven-field Builder A delta

**Artifact:** `STAGE8_TASK6_V008_SEVEN_FIELD_CODEX2_V001.md`  
**Lane:** Codex 2 / Builder A  
**Date:** 2026-08-08  
**Register context:** Q-611  
**Custody:** specification V008 and Builder A only; Builder B authors the real V008 verifier-manifest integration separately  
**Execution scope:** static generation, schema checks, producer-row dry execution, and a non-authoritative parent manifest fixture only; evaluator chain not invoked

## 1. Preflight and immutable base

The requested specification and report filenames were absent in the cleanroom
and archive workspace before creation. The V007 base was verified before use:

| Input | Verified SHA-256 | Use |
|---|---|---|
| `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V007.md` | `d38d31719b64839744a98da5ee005fb50119f9a26b2b98b0e1a1de445b5d4973` | immutable V008 base and descriptor-row source |
| Builder A pre-delta package inventory | `1d271eb7c51b952bb08326f66d2d233f1a978db57e3b313089e8a3ded8fdf9d0` | package-delta base |

No register, plan, tracker, git, commit, push, evaluator-chain, fixed-point, end-test,
member-binding, or physical-quantity action was performed.

## 2. Specification V008

The sealed output bytes are `177979` bytes with SHA-256
`3b24fc39f47d4502b01c1f06faf9f02b7828f5ba0cf4b6a882a3b331ae9c0986`.
The V007-to-V008 diff convention is `/usr/bin/diff -U 3`: exclude only the two
file-header lines and count every other added/deleted line, including blank
lines.

```text
HUNKS = 6
INSERTIONS = 160
DELETIONS = 26
DESCRIPTOR_ROWS = 66/66 byte-identical
DESCRIPTOR_ROWS_CHANGED = 0
```

The three and only three new law statements are:

1. `V008-R9-1`: R9 computes all six P0 conjuncts from supplied hash-verified
   carriers; a producer-emitted P0 result is a fault and never an input.
2. `V008-R9-2`: the subject/evidence manifest path-and-digest pairs join the
   existing ledger pattern; the exact 22-position `argv`, exact eleven-field
   verifier manifest, and exact seven-field `input_roots` are JSON Schemas.
3. `V008-R9-3`: `PRECONDITION_NOT_REPLAYABLE` is a closed fail-closed refusal,
   names the missing carrier, records `criterion_evaluated=false`, and is not a
   criterion `FAIL`.

The other five diff surfaces are mechanically consequent carriage: header and
base-pin advance, the R9 insertion, three recomputed fixture-row offsets, the
finite-delta certificate, and the scoped terminal lines. The three structural
fixture rows resolve exactly to `[133496,133684)`, `[133685,133872)`, and
`[133873,134125)` in V008.

Protected carriage also reverified:

| Block | V007 hash | V008 hash | Result |
|---|---|---|---|
| §9.1 runtime pin block | `e8f33ef718f9156c7e3c1bedf24d0234a93b47228b75ae3184769136e08fc09c` | same | byte-identical |
| authority-firewall block | `a2167cf1d46b06531ff89abdd2783d3ba7225418ae8de19ff1e0eabce859d832` | same | byte-identical |
| §9.5 aggregate rule | `2f313acac65cc77bf171fdf0094d9d3fddc9d7bef365249405a7d0fccc65f7aa` | same | byte-identical |

## 3. Seven-field producer carrier

`producer.py` now emits either `invocation:null` or the exact closed seven-field
object defined by `schemas/producer-output.schema.json`:

```text
{opcode,result_name,args,instance_id,source_sha256,span,span_sha256}
```

The dry-executed `C-B-V009-06` row emitted these real values:

```json
{"args":{"authority":"PRINCIPAL_SINGLE_AUTHORITY","graph":{"ALPHA-RESULT-SEAL":["THOMSON-RESULT-SEAL","PARENT-COMPARISON","HOLDOUT-UNIVERSE-SEAL","PREDICTION-MAP-SEAL"],"CORE-RESULT-SEAL":["SPEC-SEAL"],"END-TO-END-RECONSTRUCTION-SEAL":["ALPHA-RESULT-SEAL","HOLDOUT-RESULT-SEAL"],"FINAL-CLAIM-SEAL":["END-TO-END-RECONSTRUCTION-SEAL","HOLDOUT-RESULT-SEAL"],"HOLDOUT-RESULT-SEAL":["ALPHA-RESULT-SEAL"],"HOLDOUT-UNIVERSE-SEAL":["SPEC-SEAL"],"PARENT-COMPARISON":["CORE-RESULT-SEAL"],"PREDICTION-MAP-SEAL":["HOLDOUT-UNIVERSE-SEAL","QSPEC-SPEC-SEAL"],"QSPEC-SPEC-SEAL":["SPEC-SEAL"],"SPEC-SEAL":[],"THOMSON-RESULT-SEAL":["CORE-RESULT-SEAL","QSPEC-SPEC-SEAL"]}},"instance_id":"stage_dependencies@13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd:[18898,19830)","opcode":"DAG","result_name":"r_dag","source_sha256":"13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd","span":[18898,19830],"span_sha256":"47e7c32915bc756fb5f6be25c4fc6dec5c079c8837176dc62499e0f34f4c9d3b"}
```

```text
status = PASS
procedure_started = true
observed_evidence_sha256s = [
  a68204715597d161ece10ac731566e0b55bc3c4b237051b282e43adc1f73c736,
  47e7c32915bc756fb5f6be25c4fc6dec5c079c8837176dc62499e0f34f4c9d3b
]
```

The packed and explicit linkage agree: `source_sha256` and `span` reconstruct
the suffix of `instance_id`, while `span_sha256` rehashes exactly the 932 raw
source bytes. The argument-reproducing graph payload and raw grounding payload
remain the observed evidence. No result trace was promoted into evidence.

## 4. Parent interface and executed dry path

The operative interface is the schema, not this prose summary:

- `schemas/verifier-manifest.schema.json` fixes all 22 `argv` positions with
  `prefixItems`, `minItems=maxItems=22`, and `items=false`.
- Its `input_roots` is closed over exactly
  `{evidence_manifest_sha256,evidence_root_sha256,ledger_sha256,runtime_gate_sha256,runtime_snapshot_sha256,spec_sha256,subject_manifest_sha256}`.
- `parent.py` independently constructs the same ordered instance, requires
  exact equality pre-launch, substitutes all ten path/digest tokens, and then
  reopens and rehashes the ledger, subject manifest, and evidence manifest in
  the post-production binding check.

The non-authoritative fixture was constructed under a temporary directory
whose name contains `NON_AUTHORITATIVE-V008`. It copied the twelve currently
sealed verifier-root members, generated their content root, wrote an exact
eleven-field manifest plus sidecar, and executed these Builder A functions in
order:

```text
validate_verifier_manifest = PASS
bind_verifier_launch = PASS
post_production_verifier_validation = PASS
verifier_process_command construction = PASS
verifier process launch = NOT PERFORMED
parent_manifest_dry_run = PASS
```

Thus each new Builder A path shipped here was exercised without claiming to
author Builder B's real instance or invoking the chain.

## 5. Generated pins and closure

`tools/generate_pins.py` reads the supplied sealed bytes and generates one
canonical closed `rd22.builder-a-pin-manifest.v001`; parent, materializer, and
self-check load values from that manifest. No digest value is transcribed into
those consumers.

```text
pin rows = 22
manifests/pins.json sha256 = 9e2ff9fa3764178b816f2ee82dee56f7f777067c8f956c447d9263edcdf68a29
current specification pin = 3b24fc39f47d4502b01c1f06faf9f02b7828f5ba0cf4b6a882a3b331ae9c0986
immutable base pin = d38d31719b64839744a98da5ee005fb50119f9a26b2b98b0e1a1de445b5d4973
```

The package-wide fixed-string closure searched both the V007 digest and the
V007 filename, excluding only output/pycache directories:

| Search | Hits | Disposition |
|---|---:|---|
| V007 digest | 11 | immutable V008 carriage text; retained V007 evidence inventory; generated `specification_base_v007` pin |
| V007 filename | 15 | the same immutable base/copy uses plus generator source declaration and self-check closure guard |
| Total | 26 | all justified; zero live-runtime V007 references |

No old hit exists in `parent.py`, `producer.py`, `checks/check_map.json`,
`fixtures/fixture_manifest.json`, `inputs/subject_lineage_manifest.json`, any
operative schema, or `README.md`. Those live surfaces all point to V008. The
V007 content-addressed payload remains intentionally as the immutable base and
supersession witness.

Builder B's verdict schema still carries its independently owned V007 const at
this custody point. The generated pin records its currently verified bytes;
Builder B must integrate and re-pin V008 before the next chain run.

## 6. Complete package delta

Declared diff convention: recursive file census excluding only `outputs/` and
`pycache/`; UTF-8 text diff by unified three-line context, added files treated
as one hunk. Result: 18 files, 61 hunks, 2896 insertions, 130 deletions. No file
was removed.

| File | State | Before SHA-256 | After SHA-256 | Authorization |
|---|---|---|---|---|
| `README.md` | changed | `ab6913dd6246f8eab872c6ec9352e8753cd8144fad08483ba1e7c585f1e78a6d` | `2ef0f51e621cee2176a828400aff3a64b8b231f841a95ed1db4816245bdfbbda` | H1–H3 interface/custody documentation |
| `checks/check_map.json` | changed | `4fe53c2d1b22429318fd960238344110d9c36e530e52350df877669276e9a751` | `65a2674dae7c75753b47324fb230393ef159c785d740de03e2a2aba026efe9c1` | H3 V008 re-pin; descriptor bodies unchanged |
| `fixtures/fixture_manifest.json` | changed | `bf9d7950bc1d784bf55b0bb439aefa1648bf1ae098f5052482b9610952a9fbd5` | `dd3a70f3d9d00670a266c89f5ac9335ff7be977591b2e2ee815a7554434cad51` | H3 V008 source pin and recomputed spans |
| `inputs/evidence/3b24fc39f47d4502b01c1f06faf9f02b7828f5ba0cf4b6a882a3b331ae9c0986--STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V008.md` | added | — | `3b24fc39f47d4502b01c1f06faf9f02b7828f5ba0cf4b6a882a3b331ae9c0986` | H3 content-addressed V008 carrier |
| `inputs/structural_evidence_manifest.json` | changed | `64e16a98753103215116bbd86169fee5c07ac621372f83a573047aa63995d48d` | `142ce3b8b7eec841e3bdf6f95e0b9c74ad18d84bd377490540c132057787ffba` | H3 V008 references/payload inventory/root |
| `inputs/subject_lineage_manifest.json` | changed | `7ad2291398370168e3a1f364401399eb7fdd9f642bb12a8633398bf842390aef` | `34c84ac64d76e15a9d5ff876397b4b36a53f541cb25e8510d88cf1ad819a81cb` | H3 current spec member/root |
| `manifests/normal.json` | changed | `3258bc96b98561cf24414d71be984d5a8d99546c4d6c17276eb96af00838ecc7` | `c06494a29156ee7cb257944536430d93657d0b3fe6d53e4959896d0b54b4fd35` | H3 full normal inventory/hash closure |
| `manifests/optimized.json` | changed | `446e54e52db767a1e8a879672a4d4407764d5a23bb1f19da1419d7f7d3612e96` | `e73a8f5e78f6de526f5ac33f455a8b0c4d73c235d6995f199680f121d69dc238` | H3 full optimized inventory/hash closure |
| `manifests/package_inventory.json` | changed | `1d271eb7c51b952bb08326f66d2d233f1a978db57e3b313089e8a3ded8fdf9d0` | `1e89b685767239d52d62fdfa5adce632f794e822a6dd57b77cd17994f59662f5` | H3 complete 38-file inventory |
| `manifests/pins.json` | added | — | `9e2ff9fa3764178b816f2ee82dee56f7f777067c8f956c447d9263edcdf68a29` | H3 generated one-pin-manifest law |
| `parent.py` | changed | `571041c82c5143c2e34e8b2b3436b5f3c95a012397d9e3f19f91febd3c020712` | `4e54dece3536e353a9eb01ddc0993fa16a80f95e40bad09abe4190df27acd53b` | H1/H3 exact manifest validation, carriers, generated pins |
| `producer.py` | changed | `dc312240d3babae501eb1edf52e3d4b6510b266058b5e797492d99e4775f751b` | `3c27890533eebe485f1f41688a7268d3898e6b1582ce933164113db28ba737a8` | H2 seven-field output carrier |
| `schemas/pin-manifest.schema.json` | added | — | `456e110bc6d4ebf1d14200caff9e94bf6e681a5c773141fdcf091c50f3248045` | H3 closed generated-pin interface |
| `schemas/producer-output.schema.json` | changed | `409a8459d50ef8afd77f27be445c9ea1b75ae30e4f7287f601d774c7ffcbd9fd` | `83b61850fc1ac644802de523c9ede4d8fd528d8b046b5239f3f6319d7deb3bb0` | H2 closed seven-field invocation union |
| `schemas/verifier-manifest.schema.json` | changed | `d10ebe15d1c61a2e395d3199026b214408721fac333754d0a018a319b2d1f481` | `748dc7b414738d8753be5ecfe0af9a722dfffd4273d2eca78617667f4cddeb98` | H1/H3 exact 22-position argv and seven roots |
| `tools/generate_pins.py` | added | — | `ec5e7608ef0668114b9113f9c230a572147a8005b6401cd7f68075712c0e39a2` | H3 generated pins, no copied values |
| `tools/materialize.py` | changed | `9faa386b2badf0c32b90001f69e09d4bf8e9c1b83b22eb8ee352589d6d802db6` | `5c4d5efdfc62e66f21ffdc8bc694e45b7093164fd6b6b9a7a3df8a645f25b7d7` | H1–H3 whole-state regeneration |
| `tools/self_check.py` | changed | `c7f71b73d357fa0749b4d726c24b4d0b77b7ad726a3d488ef61657d4c8b24f0b` | `c60a3bde9029cdffbc10950ee56a300cdc26dbc14c79f30d91cdb9ef3db05cff` | H4 executed dry paths, descriptor/pin/interface guards |

## 7. Static battery

Commands executed:

```text
python3 -B evaluator_build_A/tools/generate_pins.py
  -> pins=22; pins_sha256=9e2ff9fa3764178b816f2ee82dee56f7f777067c8f956c447d9263edcdf68a29

python3 -B evaluator_build_A/tools/materialize.py
  -> checks=66; structural=56; gated=10; fixtures=6
  -> normal=c06494a29156ee7cb257944536430d93657d0b3fe6d53e4959896d0b54b4fd35
  -> optimized=e73a8f5e78f6de526f5ac33f455a8b0c4d73c235d6995f199680f121d69dc238

python3 -B evaluator_build_A/tools/self_check.py
  -> SELF_CHECK_OK
  -> syntax=6; canonical_json=all; local_schemas=9
  -> pin_manifest=22; pin_source=generated; pin_closure=value:11,name:15,total:26:PASS
  -> invocation_fields=opcode,result_name,args,instance_id,source_sha256,span,span_sha256
  -> descriptor_delta=0:V007_to_V008; descriptor_terminators_excluded=66/66
  -> verifier_manifest_fields=11; verifier_input_roots=7; verifier_argv=22:closed
  -> parent_manifest_dry_run=PASS; chain_invoked=false
```

An earlier `python3 -m py_compile` attempt was denied before writing because
that interpreter targeted a macOS cache outside the sandbox. The successful
`-B` self-check performed AST parse and `compile()` over all six Python files
without bytecode output. Package `outputs/` and all three `pycache/` roots are
empty.

Battery disposition:

| Check | Result |
|---|---|
| F_PLDEC | CLEAN — no physical quantity, measured constant, member, fixed point, end test, alpha, or `kappa_record` was evaluated |
| anti-tuning | CLEAN — all 66 V007 descriptor rows and their expected predicates are byte-identical; only the carrier/interface class changed |
| M-2 | CLEAN — fixed-string, whitespace-normalized, self-reference-scope, and hyphen/space/underscore modes remain present and validated |
| gate discipline | CLEAN — 10 gated rows still emit `NOT_RUN_GATE` without starting |
| authority | CLEAN — authorization not claimed; firewall values remain false |
| no-unexecuted-new-path | CLEAN within Builder A custody — pin generation, materialization, seven-field row emission, pre-launch validation, runtime binding, post-binding validation, and command construction all executed statically |

## 8. PIN CHECK and scope

```text
V008_SHA256 = 3b24fc39f47d4502b01c1f06faf9f02b7828f5ba0cf4b6a882a3b331ae9c0986
PACKAGE_INVENTORY_SHA256 = 1e89b685767239d52d62fdfa5adce632f794e822a6dd57b77cd17994f59662f5
PACKAGE_FILES = 38
NORMAL_MANIFEST_SHA256 = c06494a29156ee7cb257944536430d93657d0b3fe6d53e4959896d0b54b4fd35
OPTIMIZED_MANIFEST_SHA256 = e73a8f5e78f6de526f5ac33f455a8b0c4d73c235d6995f199680f121d69dc238
CHAIN_OUTPUT_FILES = 0
```

The board, prior seals, and authorization state are untouched. Builder B's
V008 integration is not claimed here; run 031 remains barred until that
independent custody step is sealed and the registrar invokes it.

SPEC_DELTA = three statements only / mechanical carriage displayed
ROWS_CHANGED = 0
SEVEN_FIELD_EMITTED = displayed
PIN_CLOSURE = grep value+name, 26 hits, all resolved
DRY_RUN = executed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN / +items: none
