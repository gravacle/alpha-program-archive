# STAGE 8 / TASK 6 / TRANCHE — V009-06 envelope and specification V006 corpus rule

**Artifact:** `STAGE8_TASK6_V009_06_ENVELOPE_SPEC_V006_LANE2_V001.md`  
**Lane:** Codex Lane 2 / Builder A  
**Date:** 2026-08-07  
**Custody:** C77 bounded envelope construction and minimal specification delta; the registrar mirrors  
**Status:** STRUCTURAL BUILD AND SPECIFICATION ONLY; no evaluator-chain invocation, board change, seal change, member binding, physical computation, fixed point, or end test

## 1. Preflight and authority boundary

| Check | Result |
|---|---|
| register head | `Q-607`, verified as the final live questions-register entry; C77 and the Q-604 one-row guard are recorded there |
| no-clobber | this artifact and `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V006.md` were absent from both commissioned locations before creation |
| V005 base | `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md` = `f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b` |
| relocation authority | `STAGE8_TASK6_GROUNDING_RELOCATION_DARIO_V001.md` = `69334875b94679c16da9b8d6153242241ca3c202f0facc6130596b9807189e6f` |
| relocated sealed source | `provenance/boundary_incidence_dynamics_preregistration_v011.json` = `13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd` |
| encoding precedence | `PREREGISTRATION_ENCODING_PRECEDENCE_PRINCIPAL_DECISION_2026-07-29.md` = `70c4080eae018bd644a3f0694557f1c0e854d621aa61097c775737887fec528f` |

The relocation is controlling. Only `stage_dependencies` bytes
`[18898,19830)` populate the two `DAG` arguments. The second encoding and the
status field are barred and do not appear in either new payload.

The existing cross-builder runtime pin remains V005. That pin was authorized
as not Builder A's to vary, and this relay does not authorize an in-place
change to Builder B's sealed manifest or verdict schema. This is compatible
with the envelope because all 66 V006 descriptor rows are byte-identical to
V005. V006 is separately sealed below for registrar disposition.

The execution gates remain:

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 2. C-B-V009-06 envelope

### 2.1 Exact grounding extraction

The source was read only after its full-file digest verified. The relocation's
member and its JSON value have these exact byte facts:

| Object | Source span | Bytes | SHA-256 |
|---|---:|---:|---|
| exact relocated member, including the `"stage_dependencies":` key | `[18898,19830)` | 932 | `47e7c32915bc756fb5f6be25c4fc6dec5c079c8837176dc62499e0f34f4c9d3b` |
| JSON value parsed from that member | `[18920,19830)` | 910 | `889515d30cedf7d3af5da1a9e1ff7c7a88a1bf0d9227bdf37d64113302dfcb86` |

The exact 932 bytes were copied without a newline or any other byte change to:

```text
evaluator_build_A/inputs/evidence/
47e7c32915bc756fb5f6be25c4fc6dec5c079c8837176dc62499e0f34f4c9d3b--C-B-V009-06-stage_dependencies.member
```

Its eleven-node value is:

| Node | Exact parent list, in source order |
|---|---|
| `SPEC-SEAL` | `[]` |
| `CORE-RESULT-SEAL` | `[SPEC-SEAL]` |
| `PARENT-COMPARISON` | `[CORE-RESULT-SEAL]` |
| `HOLDOUT-UNIVERSE-SEAL` | `[SPEC-SEAL]` |
| `QSPEC-SPEC-SEAL` | `[SPEC-SEAL]` |
| `PREDICTION-MAP-SEAL` | `[HOLDOUT-UNIVERSE-SEAL, QSPEC-SPEC-SEAL]` |
| `THOMSON-RESULT-SEAL` | `[CORE-RESULT-SEAL, QSPEC-SPEC-SEAL]` |
| `ALPHA-RESULT-SEAL` | `[THOMSON-RESULT-SEAL, PARENT-COMPARISON, HOLDOUT-UNIVERSE-SEAL, PREDICTION-MAP-SEAL]` |
| `HOLDOUT-RESULT-SEAL` | `[ALPHA-RESULT-SEAL]` |
| `END-TO-END-RECONSTRUCTION-SEAL` | `[ALPHA-RESULT-SEAL, HOLDOUT-RESULT-SEAL]` |
| `FINAL-CLAIM-SEAL` | `[END-TO-END-RECONSTRUCTION-SEAL, HOLDOUT-RESULT-SEAL]` |

### 2.2 Canonical DAG-argument serialization

The descriptor's single program contract is
`r_auto_01_dag := DAG(graph,required_parents)`. Both operands are populated by
the same parsed `stage_dependencies` value, as C77 requires. Tight canonical
JSON uses sorted keys, separators `,` and `:`, UTF-8, no nonfinite values, and
no trailing newline. The exact serialized payload is:

```json
{"graph":{"ALPHA-RESULT-SEAL":["THOMSON-RESULT-SEAL","PARENT-COMPARISON","HOLDOUT-UNIVERSE-SEAL","PREDICTION-MAP-SEAL"],"CORE-RESULT-SEAL":["SPEC-SEAL"],"END-TO-END-RECONSTRUCTION-SEAL":["ALPHA-RESULT-SEAL","HOLDOUT-RESULT-SEAL"],"FINAL-CLAIM-SEAL":["END-TO-END-RECONSTRUCTION-SEAL","HOLDOUT-RESULT-SEAL"],"HOLDOUT-RESULT-SEAL":["ALPHA-RESULT-SEAL"],"HOLDOUT-UNIVERSE-SEAL":["SPEC-SEAL"],"PARENT-COMPARISON":["CORE-RESULT-SEAL"],"PREDICTION-MAP-SEAL":["HOLDOUT-UNIVERSE-SEAL","QSPEC-SPEC-SEAL"],"QSPEC-SPEC-SEAL":["SPEC-SEAL"],"SPEC-SEAL":[],"THOMSON-RESULT-SEAL":["CORE-RESULT-SEAL","QSPEC-SPEC-SEAL"]},"required_parents":{"ALPHA-RESULT-SEAL":["THOMSON-RESULT-SEAL","PARENT-COMPARISON","HOLDOUT-UNIVERSE-SEAL","PREDICTION-MAP-SEAL"],"CORE-RESULT-SEAL":["SPEC-SEAL"],"END-TO-END-RECONSTRUCTION-SEAL":["ALPHA-RESULT-SEAL","HOLDOUT-RESULT-SEAL"],"FINAL-CLAIM-SEAL":["END-TO-END-RECONSTRUCTION-SEAL","HOLDOUT-RESULT-SEAL"],"HOLDOUT-RESULT-SEAL":["ALPHA-RESULT-SEAL"],"HOLDOUT-UNIVERSE-SEAL":["SPEC-SEAL"],"PARENT-COMPARISON":["CORE-RESULT-SEAL"],"PREDICTION-MAP-SEAL":["HOLDOUT-UNIVERSE-SEAL","QSPEC-SPEC-SEAL"],"QSPEC-SPEC-SEAL":["SPEC-SEAL"],"SPEC-SEAL":[],"THOMSON-RESULT-SEAL":["CORE-RESULT-SEAL","QSPEC-SPEC-SEAL"]}}
```

| Canonical object | Bytes | SHA-256 |
|---|---:|---|
| two-argument DAG payload | 1218 | `344fecdc5d86dba727f872b82daecd8347872c0e86ab278262100cfa526f3ac7` |
| two-payload invocation input root | — | `e368211bf54a98b8385cacbe31487bdb08d18743339b36416eeb6997576e3bc2` |

The payload filename is
`344fecdc5d86dba727f872b82daecd8347872c0e86ab278262100cfa526f3ac7--C-B-V009-06-dag-args.json`.
Fixed-byte sweeps over both new payloads find neither `stage_dag` nor a
`status` field.

### 2.3 Manifest binding and opcode consumability

The `C-B-V009-06` record now has `available=true`, descriptor digest
`0effdb712a366338ea392e40c443da365b44222407dd1dc02f7fc57142d85adf`,
the two input-file rows above, the invocation instance
`stage_dependencies@13cf1e17…:[18898,19830)`, and the full relocation/source/
precedence citation. The evidence manifest changed as follows:

```text
payload census  = 10 -> 12
available rows  = 0/56 -> 1/56
absent rows     = 56/56 -> 55/56
declared_root   = e7820ca54197fad36d8d2dc4ecad92db9e75d9be0087918d55cb322a6abd1c9a
               -> 1fbb3c0771e3c58dc87db6fcc5dad286331c25c051c98a1afeac3ec3fecb64a6
manifest SHA-256 = 007b01f7bd35da47e6b7cdcd16f69630f3766e5f4123bbd135fb4129a4840adc
```

The static consumability check loaded the existing producer, verified the
closed four-field evidence contract, recomputed the two-file input root, and
called its existing `DAG` implementation on the one invocation. Result:

```text
program_contract = accepted
DAG.success = true
nodes = 11
structural opcode result = PASS
observed result digest = 87fa71f271b3b1471da2a9b882c79c749b03e5f0f666ba9acba8d6ef3d0fa43a
```

This is an opcode-consumability self-check, not a produced row verdict. The
parent, two producer children, verifier, terminal ledger, and evaluator chain
were not launched.

## 3. Specification V006: sealed-corpus law

### 3.1 Installed law

`STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V006.md` has SHA-256
`1b8b03e4b2688acb30d8c3f5afea3529be8322f8541406adae520aa51e654995`.
Its only new operative law is in §2:

> Every `M2(q,S)` operand `S` must name a sealed, content-addressed corpus
> definition of record with member paths, byte lengths, SHA-256 values, and a
> content root. Without one, the row is `SPEC-INCOMPLETE`, its evidence remains
> unavailable, `M2` does not start, and the row cannot PASS.

The law rejects directory inference, inline ad hoc sets, generic source-set
labels, and post-query member choice. It does not rewrite a row criterion.

### 3.2 Complete affected-row registry

The generator swept all 66 final descriptor program contracts and
over-generated every row containing the `M2` opcode. Its 17 generated IDs are
exactly the 17 V006 registry IDs:

| Check ID | Current `S` operand or shorthand corpus | State |
|---|---|---|
| `C-B-V008-06` | unnamed FS/uniqueness claim sources | `SPEC-INCOMPLETE` |
| `C-B-V008-10` | unnamed alpha/core and reconstruction/review sources | `SPEC-INCOMPLETE` |
| `C-B-V008-11` | `preseal_sources` | `SPEC-INCOMPLETE` |
| `C-B-V009-01` | unnamed abstract-line-alias sources | `SPEC-INCOMPLETE` |
| `C-B-V009-08` | unnamed general-FS-claim sources | `SPEC-INCOMPLETE` |
| `C-B-V010-02` | `{p_c_status,G_c_selector_parents}` | `SPEC-INCOMPLETE` |
| `C-B-V010-03` | `{p_selector_status,G_selector_parents}` | `SPEC-INCOMPLETE` |
| `C-B-V010-04` | unnamed `kappa_record`/`kappa_Thomson`/alpha occurrence sources | `SPEC-INCOMPLETE` |
| `C-B-V010-10` | `output_claim_sources` | `SPEC-INCOMPLETE` |
| `C-B-V010-13` | `preseal_sources` | `SPEC-INCOMPLETE` |
| `C-B-V010-14` | `preseal_sources` | `SPEC-INCOMPLETE` |
| `C-B-V011-MR-02` | `selector_sources` | `SPEC-INCOMPLETE` |
| `C-B-V011-MR-04` | `S_claim` | `SPEC-INCOMPLETE` |
| `C-B-V011-MR-06` | `{p_prep_selector,G_prep_parents}` | `SPEC-INCOMPLETE` |
| `C-B-V011-SP1-04` | `response_sources` | `SPEC-INCOMPLETE` |
| `C-B-V011-SP1-05` | `selection_sources` | `SPEC-INCOMPLETE` |
| `C-B-V011-SP2-07` | `{producer_sources,verifier_sources}` | `SPEC-INCOMPLETE` |

This includes all four Q-606 seeds (`V008-10`, `V010-14`, `V009-08`, and
`V009-01`) plus 13 additional mechanically found rows.

### 3.3 Complete finite delta

Declared conventions:

```text
CARRIAGE_BASE = STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md
CARRIAGE_BASE_SHA256 = f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b
CARRIAGE_OUTPUT = STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V006.md
DIFF = diff -U 3 CARRIAGE_BASE CARRIAGE_OUTPUT
RANGE_CONVENTION = raw unified-diff headers in final-file order
COUNT_CONVENTION = exclude only ---/+++; count every other leading + or -, including blank lines
ASSIGNMENT_CONVENTION = each physical hunk appears exactly once below
```

| Hunk | Unified range | Complete assignment |
|---|---|---|
| H01 | `-1,18 +1,17` | advance title/artifact/custody/status to V006 and replace the lead disposition block |
| H02 | `-21,20 +20,23` | record Q-607/no-clobber and pin the V005 base plus relocation authority |
| H03 | `-326,6 +328,47` | add only the §2 sealed-corpus law and complete 17-row registry |
| H04 | `-1979,11 +2022,10` | replace the terminal disposition block with the V006-scoped result |

```text
FINAL_HUNKS = 4
FINAL_INSERTIONS = 58
FINAL_DELETIONS = 21
UNASSIGNED_HUNKS = 0
MULTIPLY_ASSIGNED_HUNKS = 0
```

Parsing §§3–8 in both files yields the same 66 IDs and byte-identical row
bytes for all 66. The runtime §9.1, specification-time authority firewall,
and aggregate §9.5 anchor blocks are byte-identical V005/V006, so their carried
pins remain respectively `712a861a…`, `a9e7e50a…`, and `bfad4441…`.

## 4. Package delta and static battery

### 4.1 Disclosed package delta

| File | Old SHA-256 | New SHA-256 / disposition |
|---|---|---|
| `README.md` | `13634ef622aeae92ac69e790fee5aba86b67cafdda0321b1c1f9d3382b1611c7` | `40ee650ab0b3b2fb90fe7dabb84003ca11cd46c785b16d02a452603e4c31913d` |
| exact relocated member payload | absent | `47e7c32915bc756fb5f6be25c4fc6dec5c079c8837176dc62499e0f34f4c9d3b` |
| canonical DAG-argument payload | absent | `344fecdc5d86dba727f872b82daecd8347872c0e86ab278262100cfa526f3ac7` |
| `inputs/structural_evidence_manifest.json` | `cbb85f6f2c2bae7fe50e2213a2c55a04ee93ac40a41755461faf81c3e34632b3` | `007b01f7bd35da47e6b7cdcd16f69630f3766e5f4123bbd135fb4129a4840adc` |
| `manifests/normal.json` | `d35541620b3b75bebdd4c83aac161fd83c23675c0ec4e8748c5c1c0835c07c14` | `ed1d184e0abb9e8780f8247638e41579d2d708d7fd3adeb2c731ffe2d3397bb1` |
| `manifests/optimized.json` | `3d939a4bd6c875fff0fe15a2925c79eedcfe9b15c6f538a383d1952ecca11698` | `58763ead5db1b6c33aabd1e7a735b0b57966a756b4328b2353395e7eb149a209` |
| `manifests/package_inventory.json` | `c1d1af4721952e6d12e312ae98b2948a0ff3e1a36aca32984c2fbb128f85a349` | `3c791abc5e13b5fc8c51a855048f396ccacba574816fa33a26c751f6811f43cd` |
| `tools/materialize.py` | `1594c137d1e63825aeb1c3e3dca3601d2ccc9b292586dd5011dffe51eea7ef93` | `c5ed9995aa30435d6d2fb995b29ed173fddac40b9536a544c5410b79ad974861` |
| `tools/self_check.py` | `c4168e8cf37a635273e20cada8b3a6fb50a7c7e72e6fd3525e3c9908768b4370` | `b36dcfb1640db1f83398a7b1f620de8b9dcaeaa4be9ab3b894c6f92599e6301d` |

`parent.py`, `producer.py`, the 66-row check map, fixtures, schemas, authorized
V005 runtime pin, and subject-lineage root are unchanged. The package inventory
contains 32 hashed package-member rows, including both new payloads.

### 4.2 Static self-check transcript

Commands run:

```text
python3 evaluator_build_A/tools/materialize.py
python3 evaluator_build_A/tools/self_check.py
```

Materialization reported `checks=66`, `structural=56`, `gated=10`,
`fixtures=6`, normal manifest `ed1d184e…`, and optimized manifest
`58763ead…`. The self-check reported:

```text
SELF_CHECK_OK
syntax=5
canonical_json=all
inventory=32
evidence_payloads=12
evidence=1/56
absent=55
v009_06_opcode=DAG:PASS
v009_06_observed=87fa71f271b3b1471da2a9b882c79c749b03e5f0f666ba9acba8d6ef3d0fa43a
fixture_obs=0/3
checks=66
descriptor_terminators_excluded=66/66
structural=56
gated=10
chain_invoked=false
```

The self-check also derives the 17 `M2` IDs from the current check map and
requires exact set equality with V006's registry. F_PLDEC remains clean: the
new envelope is a structural DAG over sealed prose bytes; no `SYMBOLIC` or
`SPECTRAL` opcode, physical quantity, member selection, measured constant,
fixed point, or end test was reached. The existing absent-record searches were
revalidated across M-2's fixed-string, whitespace, scope, and
hyphen/space/underscore modes; the V006 corpus registry was independently
derived from opcode contracts. The self verb audit found no authority,
execution, seal, board, or closure claim.

## 5. Does not do

This batch does not make a row pass until the independently invoked chain
produces and verifies a row ledger. One envelope does not close the evaluator.
It does not change the board or any seal. It does not populate any of the 17
`M2` rows lacking a sealed corpus definition. It does not invoke the parent,
either producer child, Builder B's verifier, or the terminal ledger.

ENVELOPE = built from relocated bytes (+serialization display)
DECLARED_ROOT = e7820ca54197fad36d8d2dc4ecad92db9e75d9be0087918d55cb322a6abd1c9a->1fbb3c0771e3c58dc87db6fcc5dad286331c25c051c98a1afeac3ec3fecb64a6
SPEC_V006 = corpus rule installed (+affected-row registry, 17 rows)
CARRIAGE = complete_finite_delta
SELF_CHECK = passed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
