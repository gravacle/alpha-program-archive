# STAGE 8 / TASK 6 / BUILDER A — SPEC V007 AND COORDINATED RE-PIN — LANE 2 V001

Lane: Codex Lane 2, Builder A  
Date: 2026-08-07  
Scope: PASTE 687 only  
Invocation: none

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member_bound = false
fixed_point_executed = false
end_test_executed = false
numeric_physical_evaluation = false
measured_constant_comparison = false
```

## 1. Preflight and pins

The live settled-questions register was read at `Q-610`; it records the exact
V007 sequence commissioned here. Before construction, neither requested output
name existed in the cleanroom or archive workspace.

| Input | Verified SHA-256 | Use |
|---|---|---|
| `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V006.md` | `1b8b03e4b2688acb30d8c3f5afea3529be8322f8541406adae520aa51e654995` | immutable spec base |
| `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md` | `f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b` | prior chain pin and descriptor control |
| `STAGE8_TASK6_ENVELOPE_V006_CHECK_DARIO_V001.md` | `759caa1c0232d89f82cee6f46d0c6d01d4f4c069894c54ecc4cb31ac5c0bda83` | Q-608 findings and migration requirements |
| `STAGE8_TASK6_REPLAY_ROLES_DARIO_V001.md` | `3fa5461f6639a02003a72e2ae667c527a5583522e1b111f5081092b5af48763f` | Q-610 invocation/linkage obligation |
| `STAGE8_TASK6_GROUNDING_RELOCATION_DARIO_V001.md` | `69334875b94679c16da9b8d6153242241ca3c202f0facc6130596b9807189e6f` | V009-06 grounding authority |
| precedence decision | `70c4080eae018bd644a3f0694557f1c0e854d621aa61097c775737887fec528f` | principal single-encoding ruling |

The two Dario cleanroom sidecars were independently matched before their bytes
were consumed.

## 2. V007: five repair classes

The output specification is
`STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V007.md`, SHA-256
`d38d31719b64839744a98da5ee005fb50119f9a26b2b98b0e1a1de445b5d4973`.

### 2.1 Q-608 four-item repair

1. The V005→V006 insertion count is corrected from 58 to 63. The four V006
   hunk ranges themselves sum to 63 insertions and 21 deletions, net +42.
2. The no-optimizer/stochastic-search/target/measured-constant/reader/network
   fence is again catalogue-scoped: it occurs immediately after the full
   fourteen-opcode table and before the `M2` subsection.
3. The closed `M2(q,S)` table entry now requires a P0-verified
   `SEALED_CORPUS_DEFINITION`. The type is a closed canonical JSON schema with
   `schema`, sorted unique `members`, and `declared_root=content_root(members)`.
4. The full implementation obligation is load-bearing in the law and the table:
   the definition bytes, closed schema, root, and every member's length/digest
   are verified before `M2` starts.

### 2.2 V009-06 single-authority criterion

Only `C-B-V009-06` changes among the 66 descriptor rows. Its criterion is now
fully opcode-reducible:

```text
r_ground := COMPARE(P0.evidence_files[stage_dependencies_member].sha256,
                    STAGE_DEPENDENCIES_MEMBER_SHA256, empty)
r_dag    := DAG(stage_dependencies, PRINCIPAL_SINGLE_AUTHORITY)
PASS iff P0 and r_ground.success and r_dag.success
```

`r_dag` parses and types the node/parent lists and rejects cycles,
self-parenting, and missing parents. The row states explicitly that the
principal ruling makes `stage_dependencies` one sealed object serving as both
graph and required-parent schema. The parent-comparison clause is discharged
by that authority identity; no second object and no `COMPARE(X,X)` parent test
is synthesized.

The descriptor digest transition, derived from the exact UTF-8 row without its
line terminator, is:

```text
C-B-V009-06
  0effdb712a366338ea392e40c443da365b44222407dd1dc02f7fc57142d85adf
  ->
  b63a1335f20f71a3cd02f2192b4d696576344fd6ae28464ba543e6efba4643c0
```

All other 65 exact row digests match V006.

### 2.3 Fixture span migration

The final V007 bytes independently resolve the three structural fixture rows as:

| Fixture | V007 half-open byte span |
|---|---|
| `FX-A35-03-C-FAMILY` | `[129056,129245)` |
| `FX-A35-04-TAU-FAMILY` | `[129245,129433)` |
| `FX-A35-05-PRIMITIVE-THOMSON-CONFLATION` | `[129433,129686)` |

The fixture manifest and the three absent-observation evidence records carry
these exact spans, the V007 path, and the final V007 digest.

### 2.4 Precedence and fifth false-negative surface

V007 states a total classification order: `P0=false` terminates as
`FAIL(INPUT_INTEGRITY)` before `SPEC-INCOMPLETE` is considered; only a P0-clean
row may receive the latter classification.

Section 12.4 now registers corpus membership as the fifth M-2 false-negative
surface. A sealed but underinclusive corpus cannot exculpate a row by producing
an empty hit set; membership must be authorized independently of the query.

## 3. Coordinated Builder A re-pin

### 3.1 Roots and manifests

| Carrier | Old | V007 |
|---|---|---|
| parent/spec/check-map spec pin | `f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b` | `d38d31719b64839744a98da5ee005fb50119f9a26b2b98b0e1a1de445b5d4973` |
| check-map file | `1197e8b8ebaef433bf5c96f83d4324e3f48e66fb6d4425c830c953b13317e7d0` | `4fe53c2d1b22429318fd960238344110d9c36e530e52350df877669276e9a751` |
| evidence declared root | `1fbb3c0771e3c58dc87db6fcc5dad286331c25c051c98a1afeac3ec3fecb64a6` | `fcaa97a01a9796a6313ce2f81f7710d9848ca972ede5699b84c914e09a15d364` |
| subject-lineage root | `d09f6b3036ef5447cb747265a3e523d26ad4c2461661135c165dcebd226b1688` | `43aee49596ee384f3d1bed8f7e92fcbf471909681927cc3726d53ef3b311beee` |
| normal manifest | `16534f20ba096ae0a3ea78638d744f3bae2ffae1633940db59b8fa765f55b104` | `9accbf318a9a15e1a7df1c7d153b0435b4a6aaae6409bf55ff08efc20ca6f5f0` |
| optimized manifest | `dd9d72229a903834b60dba68b11b8904f28291ee08cba591a0f8a573fe153094` | `72f31d82c7e98e480f268db915a2ec9e7bf977d759f8dc2098e9221b1a061d2f` |

The evidence manifest still records one available structural envelope and 55
honest absences. Its V009-06 program now contains the digest comparison and the
single-authority DAG invocation. The current canonical DAG-argument payload is
645 bytes at SHA-256
`b5f15a9cf70acc8d439d74ce8425c89c5fcc71b077f6ac03a307d1f835823cb9`.
The former paired-argument payload is retained by digest as a supersession
witness and is not an active invocation input.

### 3.2 Byte-span linkage emitted

Every produced check row now has `invocation:null` or a closed recorded
invocation. The V009-06 row emits:

```text
opcode          = DAG
result_name     = r_dag
instance_id     = stage_dependencies@13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd:[18898,19830)
source_sha256   = 13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd
span            = [18898,19830)
span_sha256     = 47e7c32915bc756fb5f6be25c4fc6dec5c079c8837176dc62499e0f34f4c9d3b
```

The producer fails the row's input integrity if a consumed invocation lacks
this citation linkage. The blocker-ledger `source` field is not used as a
surrogate.

### 3.3 Cross-builder handoff item

At this seal, Builder B's sealed verdict schema still contains the V005 full-
verdict `spec_sha256` const. The Builder A static check records
`PENDING_PARALLEL_B_REPIN`; it validates the present sealed schema and fault
document, but does not falsely claim cross-builder V007 alignment. Per Q-610,
the registrar must relay the V007 const re-pin to Builder B before run 026.
No chain invocation was attempted here.

## 4. Complete finite delta

### 4.1 Specification delta

Declared convention: `/usr/bin/diff -U 3`; exclude only `---`/`+++` file
headers; count every other added/deleted line, including blank lines. Result:

```text
V006 -> V007
physical hunks = 13
insertions      = 122
deletions       = 34
unassigned      = 0
multiply owned  = 0
```

Hunk headers are:

```text
@@ -1,15 +1,16 @@
@@ -20,21 +21,23 @@
@@ -306,6 +309,12 @@
@@ -322,35 +331,51 @@
@@ -370,9 +395,6 @@
@@ -598,7 +620,7 @@
@@ -1400,6 +1422,7 @@
@@ -1407,6 +1430,20 @@
@@ -1479,6 +1516,16 @@
@@ -1594,10 +1641,10 @@
@@ -1619,8 +1666,13 @@
@@ -2009,7 +2061,42 @@
@@ -2022,9 +2109,10 @@
```

Every line is assigned in V007 §12.7D to E1(a–e), E2/686, E3, or the scoped
output update.

### 4.2 Package delta

File-level convention: compare the pre-relay package snapshot with the final
package; record every changed/new/removed file, full SHA-256 on both sides,
and classify every other file unchanged. Result: 12 changed, 2 new, 0 removed,
21 unchanged.

| File | Old SHA-256 | New SHA-256 | Authority |
|---|---|---|---|
| `README.md` | `20302996db734eedfb358d72708c768bace325d7534db17178a10a47e14c388c` | `af28b5c39a91b0e70a985ac566373bf9c3c5f0174dd10a2c51d6c09ff7b2b73c` | E2 handoff and linkage disclosure |
| `checks/check_map.json` | `1197e8b8ebaef433bf5c96f83d4324e3f48e66fb6d4425c830c953b13317e7d0` | `4fe53c2d1b22429318fd960238344110d9c36e530e52350df877669276e9a751` | E2 spec/descriptor re-pin |
| `fixtures/fixture_manifest.json` | `2e823e627830d882f42cf2fe9f12dccb13ac6ddd8d7a4eb3a08704b84734510e` | `bf9d7950bc1d784bf55b0bb439aefa1648bf1ae098f5052482b9610952a9fbd5` | E1(c)/E2 span migration |
| `inputs/structural_evidence_manifest.json` | `007b01f7bd35da47e6b7cdcd16f69630f3766e5f4123bbd135fb4129a4840adc` | `64e16a98753103215116bbd86169fee5c07ac621372f83a573047aa63995d48d` | E2 refs, descriptor, program, inventory/root |
| `inputs/subject_lineage_manifest.json` | `da37ece918c184a0193805042fd6158c7edd1c051f05feb4f2bbef69f05544db` | `7ad2291398370168e3a1f364401399eb7fdd9f642bb12a8633398bf842390aef` | E2 V007 subject |
| `manifests/normal.json` | `16534f20ba096ae0a3ea78638d744f3bae2ffae1633940db59b8fa765f55b104` | `9accbf318a9a15e1a7df1c7d153b0435b4a6aaae6409bf55ff08efc20ca6f5f0` | E2 regenerated pins/inventories |
| `manifests/optimized.json` | `dd9d72229a903834b60dba68b11b8904f28291ee08cba591a0f8a573fe153094` | `72f31d82c7e98e480f268db915a2ec9e7bf977d759f8dc2098e9221b1a061d2f` | E2 regenerated pins/inventories |
| `manifests/package_inventory.json` | `1dcb3517db383fadfdbb1bbad4fd6c7f314ce62c91e19cc323887a78f0789b46` | `94f60f2add33835fbd36eca7c02e92f49bdbc961e1f1eae0a8e078855cb127c0` | E3 complete inventory |
| `parent.py` | `78d99947447e6688202f3071cce37980d944bf747a8ee3379eba88afa65c953b` | `cd86374ca12fdb4822d789684de794a16eb0c790deee6069affe17099d887b75` | E2 V007 const |
| `producer.py` | `8bbd11e4289bf8da5c5b589daf971054eb6c8f5efe3d789f70777f0a59a7523b` | `8ec03d1e8af12fa10fc402f52482cde867fbd703f76b293e14189c5db8e17eda` | E1(b)/E2 single-authority DAG and linkage carrier |
| `tools/materialize.py` | `8c4d370f65b00b15ec5b49630187f54f6aa35aac9a82c0ffee76a313f56d1e86` | `b5f8f8cda7dfbc6a7d5c8a22904102dbad22c0e92ec9d25c04c62aa3d9bc6fc8` | E2 deterministic regeneration |
| `tools/self_check.py` | `adfddf6fe89e8e0d4ca2240e6a1c7e928bf69e1ec6abd359538668a1ac19299a` | `d912e628b1bfed1afe7e0ebac2ccbbc18c72fd30759290b5f43206c036c79921` | E3 static assertions/transcript |
| new single-authority DAG payload | — | `b5f15a9cf70acc8d439d74ce8425c89c5fcc71b077f6ac03a307d1f835823cb9` | E1(b)/E2 |
| new V007 sealed-byte payload copy | — | `d38d31719b64839744a98da5ee005fb50119f9a26b2b98b0e1a1de445b5d4973` | E1(c)/E2 evidence refs |

## 5. PIN CHECK and battery

### 5.1 Protected sections

Direct byte comparisons V006/V007 returned true for all three protected
anchor-bounded blocks:

| Block | Byte equality | Independent slice SHA-256 | V006 established pin retained |
|---|---:|---|---|
| §9.1 runtime subject | true | `e8f33ef718f9156c7e3c1bedf24d0234a93b47228b75ae3184769136e08fc09c` | `712a861aaf5f2f43590f41405435663dff8efd52a93e30d33cc2399636442172` |
| authority firewall | true | `a2167cf1d46b06531ff89abdd2783d3ba7225418ae8de19ff1e0eabce859d832` | `a9e7e50afb466ead16c43b45352d1c04273bb9c3e5671f5f7c386df70cdf0afa` |
| §9.5 aggregate rule | true | `2f313acac65cc77bf171fdf0094d9d3fddc9d7bef365249405a7d0fccc65f7aa` | `bfad44417f766cc97a8942a8ffab7f9accd5791a2c2f1169a6534f3643543648` |

The independent slice hashes use the displayed heading/anchor boundaries;
the established pins use V006's pre-existing pin-check convention. Byte
equality is the carriage result.

### 5.2 Static transcript

Executed only:

```text
python3 evaluator_build_A/tools/materialize.py
python3 evaluator_build_A/tools/self_check.py
```

The final static result was `SELF_CHECK_OK` with:

```text
canonical_json=all
checks=66 structural=56 gated=10 fixtures=6
descriptor_delta=1:C-B-V009-06
descriptor_terminators_excluded=66/66
evidence=1/56 absent=55 fixture_obs=0/3
v009_06_opcodes=COMPARE+DAG:PASS
v009_06_observed=c4e99047921bf060e5a38409c48e5ed4e9614f2cd609151c2c32fa99d8a9765f
byte_span_linkage=invocation+source_sha256+span+span_sha256
consumed_implies_materialized=PASS
b_spec_repin=PENDING_PARALLEL_B_REPIN
chain_invoked=false
```

The opcode execution above is a synthetic/static executor check over the
already-cited V009 envelope. It is not a parent-chain invocation or a new board
verdict.

### 5.3 F_PLDEC, anti-tuning, M-2, and verb scope

- F_PLDEC: no physical opcode, quantity, gate, member, fixed point, end test, or
  measured constant was executed or evaluated.
- Anti-tuning: the principal decision and exact relocated bytes determine the
  one graph; no alternative encoding, status field, desired result, or
  post-query corpus member was selected.
- M-2: fixed string, whitespace normalization, self-reference/scope,
  hyphen/space/underscore, and corpus-membership surfaces are all registered.
- Verdict-line scope: `PASS` in the static transcript describes the local
  executor self-check only. It does not change a board, seal, or aggregate.
- Custody disclosure: one exploratory identifier search returned Builder B
  module names and function-match lines. No Builder B implementation body was
  used; the linkage shape was derived from the sealed 686 artifact and Q-610.
  Builder B's sealed verdict schema was read only as the content-addressed
  external contract already required by Builder A.

## 6. Does not do

This relay does not invoke the parent, either producer child, or the verifier;
does not register or mirror its own outputs; does not edit a plan, tracker, or
git state; does not move the board; and does not claim evaluator closure. The
Q-604 guard remains in force: one envelope and one local opcode self-check are
not an evaluator seal.

V007 = 5 repairs (+delta)
REPIN = parent+check_map+manifest (+C-B-V009-06 `0effdb712a366338ea392e40c443da365b44222407dd1dc02f7fc57142d85adf` -> `b63a1335f20f71a3cd02f2192b4d696576344fd6ae28464ba543e6efba4643c0`)
SPAN_LINKAGE = emitted per B's spec
SELF_CHECK = passed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+verdict scope and non-load-bearing custody disclosure recorded)
