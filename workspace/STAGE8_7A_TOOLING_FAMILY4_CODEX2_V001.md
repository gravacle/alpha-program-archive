# Stage 8 / 7A Step 11 — Tooling Family 4: corpus candidates, pins, and envelope shells

**Lane:** CODEX 2  
**Relay:** 759  
**Disposition:** deterministic Family-4 package built and run; corpus-instance custody preserved; admission barred

## 1. Pickup, preflight, and custody

The single relay file `RELAY_PASTE_759_TOOLING_FAMILY4_CODEX2_V001.md` verified at SHA-256 `c72a8c709c63064e62a9c5e75bf8c9671c474d40712129e6251c3b65adc83fe9` before reading. Its sidecar hashes to `3657c56b48a221be0ff9976395e02c4d266ea9af529eaa1de9d8f433adcee509`, and the CODEX 2 lane guard matched. `relay_outbox/759_ACK.md` was written before task work. The report, seal, package, ACK, and DONE names were absent in the cleanroom and archive workspace at preflight.

The governing corpus authorities reverified through their adjacent registrar seals:

| Authority | Artifact SHA-256 | Seal-sidecar SHA-256 |
|---|---|---|
| principal selection-authority decision | `0dfc6e7bb761850e7cb4996c9a0b63e94567c7ae88c7de837f78b3b5628e2ad7` | `27b2c35c70dab9bb4770b61f0b579fda4a08cced10f0196459228f5222eb52ef` |
| corpus-selection rule V001 with V002/V003 amendments | `653581bf54313ef026add193c1d08dde29bcb5e9cde78e5b0383e140114fd495` | `03cb07f7a3206e8bf5725c0891b74735946926b44c522194eeb1fa4f9e85faac` |

The tool contract makes the custody boundary executable data:

```json
{"candidate_is_instance":false,"dual_verification_required":true,"generator_may_seal_instance":false,"registrar_seals_instance":true}
```

Accordingly, Family 4 emits corpus **candidates and packaging**, never a corpus seal. A candidate cannot enter an M2 invocation until the registrar has sealed the instance and both lanes have checked wrong inclusion and wrong exclusion.

## 2. Tool and generated inputs

Package root: `step11_tooling_family4/`.

| Package object | Purpose | SHA-256 |
|---|---|---|
| `generate_corpora_pins_envelopes.py` | authority verification, corpus typing/candidate packaging, schema-instance replay, descriptor extraction, root/pin generation, seven-field shell emission, controls | `d1f486035f6edf75a9fc0e97a70115d60db130583b292d037b25843dfb617899` |
| `contracts/tooling_family4.schema.json` | closed corpus-candidate, selection-type, pin-manifest, seven-field invocation, and envelope-shell interfaces | `d34f261f665f33e3d8237b76d0bf0a2185f4b9d2b1c621f79e9ac9b355906b77` |
| `inputs.generated.json` | current-byte pins for V012, check map, box delta, Families 1–3, corpus authorities, and tool contract | `5b180e99defab8248ffa804dc89ba86b554fd3bb56f9780e93019c89861cc60c` |
| `generated/run_result.json` | generated output census | `cc39cc7bc3cd689608a1f0b2878ba2b9137035edbd02d9e4a13c53427c939ee0` |
| `generated/self_check.json` | typing, custody, descriptor, schema, inventory, and digest controls | `7f108d90348ec86eab404bba447d104525706e358b197d8158808749d927cab6` |
| `generated/row_census.json` | eight-row ready/owner disposition | `855ca75fc08f4cdbf94573c26de4fe07def31685856dcf5fa252c0d958931c69` |
| `inventory.generated.json` | self-excluding 20-member package inventory | `cad220a2c96831b850aed33cacb522e3622d641f305e1564cf4b3c4289fdee67` |

The direct script ran under `python3 -I -S -B`, uses standard-library code only, emits tight sorted UTF-8 canonical JSON without a trailing newline, bars NaN, has no load-bearing `assert`, and refuses absolute or escaping cleanroom component paths. External corpus-law inputs are read-only, adjacent-seal verified, and recorded by resolved path, byte length, digest, seal path, and seal digest.

Pins were generated from current bytes. The tool did not embed artifact digests in source: content-addressed inputs were discovered by suffix/pattern and then rehashed. V012 and the current check map reverified at `382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504` and `280004821c532def203ae81cec35bcac26bd3ab4bdd03752f5196aa7b9c23f3d`; the sealed box-schema delta reverified at `b52e66b79787a55bad1553c05dfa8df52e7b11153879589d9627073a8e06bba9`.

## 3. Corpus-rule implementation and candidates

The closed selection interface distinguishes all three rule types:

| Type | Enforced law | Actual output in this bounded run |
|---|---|---|
| `CLAIM_SCOPED` | tokens come from the operand; all tokens match conjunctively under V002; four probe modes and backticked objects are carried | one V009-08 candidate |
| `PROVENANCE_SCOPED` | members are citation closure from a named sealed root; closure depth is recorded; content matching is false | no real candidate source in this bounded input set; exercised synthetic non-authoritative positive control |
| `REGISTRY` | members accrue only by declared decision authority; a claim sweep is forbidden; current state may lawfully be empty under V003 | one empty V009-01 candidate |

### 3.1 V009-08 worked example

The tool consumed the existing sealed general-FS corpus definition and Family-2 binding, rehashed the 603-byte member, recomputed declared root `7c6c3455e386610dcd78cfd7b8c46789ddeff42d3f442591c36088c50a39abc9`, and emitted an unsealed candidate wrapper:

```text
cfa8db997637f724c31131a14c068850fc0d0ba08351c77ba0c50bc685339ed5
step11_tooling_family4/generated/corpus_candidates/
  cfa8db997637f724c31131a14c068850fc0d0ba08351c77ba0c50bc685339ed5--C-B-V009-08_general_FS_claim.json
```

Its type is `CLAIM_SCOPED`; tokens are exactly `FS` and `general`; its match law is `ALL_TOKENS_CONJUNCTION_V002`. It reproduces sealed material for packaging but does not reseal it. Dual verification remains explicitly named in the V009-08 row owner list before M2.

### 3.2 V009-01 registry candidate and surfaced schema boundary

The registrar snapshot `CORPUS_INSTANCE_BX07_ALIAS_REGISTRY_V001.json` reverified at `5a14e376032f372f5f696c89e5ba3327a8f711cdc259be13b04f7f9dd2a0d43f`. Family 4 correctly typed it `REGISTRY`, rejected the prior 267-mention claim-sweep shape, retained its principal/registrar accrual authority, and emitted the present empty-state candidate:

```text
722a7ea616eb159a188987646f345c6423d1764b59a717af7fc941d5b9aff2d3
declared empty content root = 6a666c3166fd15026fe5996065f32d5e84a92edd7e99439f72cc0c7b4d496054
```

The candidate is not promoted to a `rd22.sealed-corpus-definition.v001` instance. V003 expressly permits an empty current registry, while the present v001 instance schema says `members.minItems=1`; that interface boundary requires registrar/spec reconciliation plus dual verification. It is displayed as a remaining owner, not silently overridden.

## 4. Generated pin manifests and envelope shells

Each pin manifest lists exact `{relative_path,byte_length,sha256}` members in bytewise UTF-8 path order and recomputes `A35-CONTENT-ROOT-v1`. Each shell:

- binds the exact V012 descriptor row with its line terminator excluded;
- verifies that span digest against the current check-map descriptor digest;
- expands every current check-map program slot into the exact seven-field shape `{opcode,result_name,args,instance_id,source_sha256,span,span_sha256}`;
- packs the descriptor citation in `instance_id`;
- names all component and corpus-candidate digests through a generated root;
- states `execution_allowed=false`, `BARRED_STEP11_SUBGATE`, and `chain_invoked=false`.

These are envelope shells, not producer observations or evaluator inputs.

| Row | Components pinned | Program slots | Pin manifest SHA-256 | Envelope-shell SHA-256 |
|---|---:|---:|---|---|
| `C-B-V008-05` | 6 | 1 | `4e60b69ad89fc766648fd9191cd440c4d18e4441ed65a3c3ac353e0722603b1b` | `2637aa4f3a8d16ad11a417d93d5e2fe81c95a57d88cb8ee6ac15b1e3e42b8c32` |
| `C-B-V009-08` | 7 + corpus candidate | 2 | `9a0bef5bed3e48ba55160fbee7d7209ca0e424eab4a47416a42f6a780a1816ba` | `7f0801765edeae71d873c8958a6e53481c97f21709083d6809c27ffcf05533dd` |
| `C-B-V010-11` | 4 | 1 | `ae2f88a5633dc59d570a4b7838bcfe568278ab33d3fe22f892ec2f8444d3989b` | `322f1aad0757543379d85005a30cfba7f730cb30ef138090e35aefac292152c2` |
| `C-D-A35-02-QUASIFREE-CAR-LIFT` | 6 | 2 | `22abaa007443f6d09c32e7c14e734e2ecc9f359e3e23e6665377909d5e553d3a` | `5919f5571f7ff654ef4a6136ec4dad894a5c7363540756db8911f8fa34c4d6ee` |
| `C-B-V011-SP1-07` | 26 | 10 | `e09a993903a96e1b31d3fe5dfdde4d17bc2f6dd0df73682cf91fadd5c64a4460` | `5d56dd45f018fe3315332e76f076f8d31df47bdc4ad93e9bd2ade36ddae3dd2a` |
| `C-B-V011-SP2-05` | 28 | 11 | `30d1136775e2f32dfc78f0fff2b85856de07109adaf863ee83ce8653db6fa5ad` | `d4b6fb7158b355fa973145d10b2af0555583376239741c1609d7bf34609d486a` |
| **Total** | **77 component references + 1 candidate reference** | **27** | **6** | **6** |

The four completed box-instance rows passed their closed instance schemas and all nested content/source-span checks through the existing sealed Family-1 validator. The SP1, SP2, and orientation package inventories replayed 23/23, 27/27, and 15/15; the Family-2 and Family-3 inventories replayed 19/19 and 51/51.

`C-B-V010-11` remains honestly mutation-underdetermined in Family 3 because its descriptor names no mutation class or rejection receiver. That does not block this positive TYPE envelope shell: no mutation is a required operand of the current row. Any future negative-control extension remains an S11-SPEC interface item.

## 5. Envelope-ready census and remaining owners

“Envelope-ready” here means all currently required component bytes are present in a generated shell. It does **not** mean admitted, executed, replayed by Builder B, or a row PASS.

| Row | Tooling status | Remaining owners |
|---|---|---|
| `C-B-V008-05` | `ENVELOPE_READY_COMPONENTS_COMPLETE_ADMISSION_BARRED` | Builder B independent contract/replay; registrar admission |
| `C-B-V009-08` | `ENVELOPE_READY_COMPONENTS_COMPLETE_ADMISSION_BARRED` | dual corpus verification before M2; Builder B independent contract/replay; registrar admission |
| `C-B-V010-11` | `ENVELOPE_READY_COMPONENTS_COMPLETE_ADMISSION_BARRED` | Builder B independent contract/replay; registrar admission |
| `C-D-A35-02-QUASIFREE-CAR-LIFT` | `ENVELOPE_READY_COMPONENTS_COMPLETE_ADMISSION_BARRED` | Builder B independent contract/replay; registrar admission |
| `C-B-V011-SP1-07` | `ENVELOPE_READY_COMPONENTS_COMPLETE_ADMISSION_BARRED` | Builder B independent contract/replay; registrar admission |
| `C-B-V011-SP2-05` | `ENVELOPE_READY_COMPONENTS_COMPLETE_ADMISSION_BARRED` | Builder B independent contract/replay; registrar admission |
| `C-B-V009-01` | `NOT_READY_REGISTRY_CUSTODY_PENDING` | registrar resolves V003-empty/v001-minItems interface; both lanes verify inclusion/exclusion; Step-11 integration binds only afterward |
| `C-B-V008-10` | `NOT_READY_PROGRAM_FUTURE` | 11 stage artifacts; 17 digest-parent bindings; sealed root formula/value; 11-node-to-BX03 mapping |

## 6. Executed controls and independent replay

Eight in-tool controls passed:

1. claim-scoped candidate accepted under the V002 conjunction;
2. provenance-scoped candidate accepted only with citation-closure root, recorded depth, and content matching disabled;
3. registry candidate accepted with its declared accrual authority;
4. claim-token disjunction refused `CLAIM_SELECTION_V002`;
5. registry claim-sweep refused `REGISTRY_CLAIM_SWEEP`;
6. generator promotion to corpus-sealing authority refused `CORPUS_CUSTODY`;
7. perturbed component digest refused `HASH_MISMATCH`; and
8. all 6 descriptor rows rehashed with the line terminator excluded.

An independent replay, separate from the generator's checks, returned:

```text
INDEPENDENT_REPLAY=PASS inventory=20 json=20 content_addressed=14
shells=6 slots=27 dual_verify_owner=present
```

It rehashed all 20 inventory members, recanonicalized all JSON, verified all 14 content-addressed filenames, recomputed every pin root, replayed all six descriptor spans, checked all 27 exact seven-field records and packed linkage values, and required V009-08's explicit dual-verification owner. A second real invocation refused occupied outputs with `FAMILY4_REFUSE OUTPUT_COLLISION:package outputs`.

## 7. Does-not-do and gate audit

Every candidate, pin manifest, shell, census, self-check, and run record states `BARRED_STEP11_SUBGATE` and `chain_invoked=false`. No generated corpus candidate was sealed or promoted to an instance. No envelope shell was admitted or executed. No evaluator row, evidence manifest, board, register, plan, tracker, or git state changed.

F_PLDEC is clean: the tool performs byte hashing, schema checking, finite ordering, citation-span verification, and structural counts only. It performs no member binding, fixed-point execution, end test, numeric evaluation of a physical quantity, or comparison to a measured constant. `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false` remain in force.

Verb audit: **CLEAN**. “Built,” “generated,” “produced,” and “envelope-ready” refer only to the Family-4 tool, unsealed candidates, content-addressed packaging, and component-complete non-executable shells. They do not assert corpus-instance authority, dual verification, admission, replay, evaluator PASS, or scientific closure.

TOOL = built (controls displayed; custody boundary in contract)
PRODUCED = 2 corpus candidates / 6 pin manifests / 6 envelope shells (14 content-addressed outputs; 20-member package inventory)
ENVELOPE_READY = C-B-V008-05, C-B-V009-08, C-B-V010-11, C-D-A35-02-QUASIFREE-CAR-LIFT, C-B-V011-SP1-07, C-B-V011-SP2-05
REMAINING_OWNERS = per row displayed in §5 (including dual corpus verification and registrar admission)
ADMISSION = barred, stated
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
