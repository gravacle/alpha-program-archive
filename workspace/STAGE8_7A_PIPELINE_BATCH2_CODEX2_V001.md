# Stage 8 / 7A Step 11 — Pipeline Batch 2: five C-class rows

**Lane:** CODEX 2  
**Relay:** 771  
**Disposition:** four rows component-complete with admission barred; one row preserved as an `ABSENT_OF_RECORD` gap

## 1. Pickup, preflight, and custody

The single relay file `RELAY_PASTE_771_PIPELINE_BATCH2_CODEX2_V001.md` verified before reading at SHA-256 `1f05eed8bb08d71c097a231996023cce6b2901787b4cbbf3b0606e10e5ee88b6`. Its adjacent sidecar hashes to `b4276a6e9223a5f20a2fe248f60433195a194ee476f8130f9b6263bff2a6e0c6`, and `sha256sum -c` passed from the inbox directory. The CODEX 2 lane guard matched. `relay_outbox/771_ACK.md` was written before task work.

The report, seal, package, and DONE names were absent at preflight. All writes are confined to the cleanroom. No register, plan, tracker, git, ruling, adoption, or evaluator-chain action was taken.

The generated input pins are:

| Input | Verified SHA-256 | Verification carrier |
|---|---|---|
| evaluator spec V012 | `382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504` | adjacent registrar seal |
| current check map | `280004821c532def203ae81cec35bcac26bd3ab4bdd03752f5196aa7b9c23f3d` | Builder-A package inventory |
| sealed V011 packet member | `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a` | `STAGE7_PACKET_MANIFEST_V001.sha256` |

The packet member was read only after its digest was reproduced from the sealed packet manifest. The instance serializer copies exact packet spans to content-addressed `.bin` payloads and separately records the source-file digest, half-open span, and span digest.

## 2. Five-row selection

The selection follows the sealed C/D/U split in row order. These are the next five previously untreated rows whose box decomposition contains no `D` or `U` owner:

| Row | Split | Why selected |
|---|---:|---|
| `C-B-V008-01` | `2/0/0` | carrier/map schema and five carrier manifests are schema-instance work grounded in displayed maps |
| `C-B-V008-02` | `2/0/0` | decorated categories, identities, composition, and label rules are displayed finite structure |
| `C-B-V008-04` | `3/0/0` | periodic global shifts and the nonperiodic negative competitor are displayed together |
| `C-B-V008-07` | `2/0/0` | component quotient and real/complex seams are displayed as typed maps and identities |
| `C-B-V008-09` | `4/0/0` | its box class is wholly constructible, so it is eligible for derive-or-gap treatment; close reading determines whether the required finite objects actually exist |

This selection does not assert that every nominally constructible object is already displayed. The fifth row demonstrates the distinction: a C-class box can be lawful formalization work yet still be absent from the present sealed corpus.

Rows involving an unselected object carrier, corpus authority, or principal mapping were not advanced ahead of these five. No ruling-shaped element occurred in the selected source spans.

## 3. Package and closed interfaces

Package root: `step11_pipeline_batch2/`.

| Object | Purpose | SHA-256 |
|---|---|---|
| `build_pipeline_batch2.py` | authority checks, exact span extraction, instance authoring, Families 1–4, controls, inventory, replay | `cc807c7606d33fc26399ed9c695668376c963a4484b6ab89b441e51aaaf70bd5` |
| `contracts/pipeline_batch2.schema.json` | closed instance, citation, span, and seven-field invocation interfaces | `cee21677da54f5e160717f4e6fd8aa69f569030b8980eaed613479da8bb7a708` |
| `generated/run_result.json` | bounded run result | `0af1606edfd483a438ac3f1373946b6e593acb55bddace41dcfb8e16a4d4a02c` |
| `generated/self_check.generated.json` | twelve positive checks and five named negative controls | `91cd50c92c4a4307fed64a7f1c52e8cf90285581bb18f9ee0fa92e3fe1c1d99d` |
| `inventory.generated.json` | self-excluding 44-member inventory | `8605cc01ff3faff83141939daffc9d1dbb45655d4e154d6e77694efbad53b575` |

The inventory root is `94f9d62a22b07e5b8916358ccf01f106ed8ec7a4c54358cbe9c9eb6ae27b6b0b` under `A35-CONTENT-ROOT-v1`. JSON outputs are sorted-key, tight UTF-8, NaN-barred, and have no trailing newline. The direct script uses standard-library Python only, contains no load-bearing `assert`, refuses occupied outputs, and has a read-only `--check` path.

The closed instance interface requires exactly:

```text
{schema,check_id,status,descriptor,source_bindings,meaning_probe,
 object,gap,admission,chain_invoked}
```

A derived instance must have at least one content-addressed sealed span, a non-null object, and no gap. A gap instance must have a null object and a non-null bounded-search record. Both forms fix `admission=BARRED_STEP11_SUBGATE` and `chain_invoked=false`.

## 4. Instance grounding and meaning probes

All spans below are half-open byte intervals in the sealed packet member unless identified as descriptor spans in V012.

| Row | V012 descriptor span / digest | Sealed prose span(s) / digest(s) | Serialization and meaning probe |
|---|---|---|---|
| `C-B-V008-01` | `[36271,36607)` / `bed9041f0fa42646120dbd4a9d3f377c1f03d94bb56113486586d3bf2fa9fe31` | `[8271,9983)` / `ea74efa54e773fcc1f4e169f74152199fdf25449609a18629629078a2ecfaaa0`; `[44405,45319)` / `d5290d750a8d850676b7ce05306d94d6bd97b258dc971694667922600f91a889` | five distinct carrier classes become typed graph nodes; `iota_open`, `d_0`, `d_1`, and `c_2` retain displayed domains/codomains. Probe rejects identifying `A_R^1`, `C_1`, or endpoint alternatives. |
| `C-B-V008-02` | `[36608,36894)` / `c477b6e72e7bf60be0f08ecf3ba76aef3409243e4d813c4f162c8e0e201b8bc5` | `[13010,16857)` / `2c91db76cecdfce75b5e6e50987f17b77b1b800afe4401ddcece16abc539206b` | `BareRec_2`, `OpenRec_2`, and `DecRec_2` become typed category objects with the displayed identity, composition, first-opening reflection, and label equations. Probe distinguishes `U_label` from `U_open`. |
| `C-B-V008-04` | `[37288,37626)` / `f13ffcdfbe7d03f44406036b17e5239001649949f413ae59d629bbe0a98b0881` | `[29318,30557)` / `7d81c132980e65bc0b318036215075aa51d41f660efe58f55ab3542eed29d3c9` | the periodic `K_L`, global `T_mu`, and `nabla_mu` declarations are separated from the nonperiodic interior-compression fixture. Probe rejects a free-group representation claim on the partial shift. |
| `C-B-V008-07` | `[38226,38520)` / `cb4a07bdea12c69736301711e04abdbad181888cda23d127e27e447044dda161` | `[44405,45319)` / `d5290d750a8d850676b7ce05306d94d6bd97b258dc971694667922600f91a889`; `[9630,9831)` / `708cdd94b2a74c93541baecb5eb8d8fb733c4ed75b821a91c710b168e6452af9` | component-indexed `ker(d_0)`, quotient, `d_0`, `d_1`, `c_2`, and complexification seam become a typed graph. Probe rejects one global constant stabilizer and `A_R^1=C_1`. |
| `C-B-V008-09` | `[39377,40055)` / `3d85c31db2924f2f378ce957ab098117d5cc6dff38e5aade6a7dc07bfaf8ddb3` | no derivation span bound | exact case-sensitive whole-packet probes found zero occurrences of `G_branch`, `p_branch`, `E_branch`, and `BRANCH_OUTCOME`. Public-closure and Maxwell prose does not instantiate the required finite grammar, certificate, per-ID values, or dependency proof. The object is null and the gap is explicit. |

The six cited packet spans are copied byte-for-byte into five unique content-addressed payloads; the shared tangent-complex span is intentionally deduplicated. No requirement sentence was serialized as its own proof or certificate.

## 5. Family-1 compilation

The Family-1 path consumes each closed instance and performs row-specific structural checks:

| Row | Result | Components |
|---|---|---|
| `C-B-V008-01` | `COMPILED` | `carrier_manifest`, `map_graph` |
| `C-B-V008-02` | `COMPILED` | `category_schema`, `finite_generator_list` |
| `C-B-V008-04` | `COMPILED` | `periodic_shift_schema`, `partial_shift_fixture` |
| `C-B-V008-07` | `COMPILED` | `component_quotient_schema`, `real_complex_seam_schema` |
| `C-B-V008-09` | `GAP_PROPAGATED` | none; the exact missing-object reason is retained |

Compilation checks the distinctions that carry meaning: five carrier classes and typed arrow endpoints; three category layers and label preservation; global inverse only on the periodic object; componentwise stabilizer quotient; and a non-collapsed real/complex seam.

## 6. Family-2 finite families and expected ledgers

Family 2 generates only finite objects already displayed in the sealed spans:

| Row | Generated IDs | Expected ledger |
|---|---|---|
| `C-B-V008-01` | `carrier_graph_canonical` | `TYPED_COMPOSITES_PRESENT` |
| `C-B-V008-02` | `BareRec_2`, `OpenRec_2`, `DecRec_2` | `IDENTITY_ASSOCIATIVE_LABEL_PRESERVING` for each |
| `C-B-V008-04` | `periodic_global_shift`, `nonperiodic_partial_shift` | `ADMITTED_REPRESENTATION`, `REJECTED_REPRESENTATION_CLAIM` |
| `C-B-V008-07` | `component_quotient`, `real_complex_seam` | `TYPED_COMPONENTWISE`, `TYPED_SEAM` |
| `C-B-V008-09` | none | `GAP_PROPAGATED`; no zero-item completeness claim |

The positive family certificates are tagged `EXACT_DISPLAYED_LIST`. The V008-09 record has `certificate=null`; zero items are not misreported as an exhaustive branch grammar.

## 7. Family-3 mutations and rejection receivers

| Row | Mutation | Expected receiver |
|---|---|---|
| `C-B-V008-01` | drop `c_2` | `MANDATORY_MAP_MISSING` |
|  | retarget `c_2` to `C_1` | `MAP_CODOMAIN_MISMATCH` |
| `C-B-V008-02` | erase the `lambda` rule | `DECORATION_LOST` |
|  | alter the identity | `IDENTITY_LAW_MISMATCH` |
| `C-B-V008-04` | claim a global inverse for the partial shift | `NONPERIODIC_GLOBAL_INVERSE` |
|  | erase periodicity | `SHIFT_DOMAIN_UNSEALED` |
| `C-B-V008-07` | merge `A_R^1` with `C_1` | `TYPE_SEAM_COLLAPSE` |
|  | replace component kernels by one global stabilizer | `COMPONENT_KERNEL_MISSING` |
| `C-B-V008-09` | none | gap propagated; no mutation family invented |

Each mutation changes a displayed structural distinction and names its receiving failure. No ruling-shaped mutation or expected outcome was generated.

## 8. Family-4 pins and envelope shells

Four pin manifests enumerate the exact instance and Family-1/2/3 bytes and compute their roots under `A35-CONTENT-ROOT-v1`. Four shells bind those roots to the exact V012 descriptor and expand the current check-map program slots into the seven-field carrier:

```text
{opcode,result_name,args,instance_id,source_sha256,span,span_sha256}
```

| Row | Pin manifest SHA-256 | Envelope-shell SHA-256 | Status |
|---|---|---|---|
| `C-B-V008-01` | `9084a72b080aef48008953d581c918d5796c08a5e135813985bf64547aad2389` | `52fde57460b6bd8916b8461eb074e753aa3e61adb917d07df36682331fd93efd` | component-complete; admission barred |
| `C-B-V008-02` | `00df9df0be1b70eccf8eb76b0657bf75b5cfdb7672d6d7c200fc0277ac415eb8` | `5d0d622b7ffd4caa3084cdb8c0f6a331cf3e8280e5878279891bc5e311b145be` | component-complete; admission barred |
| `C-B-V008-04` | `b10b2cdec137cfb3e767480ef48b3728261736a0c5d97fd793c9c4c8a9449713` | `f7ec8c026e22fd169d0c647cec4b9e8d2409c7d96c95a019d192ed78787a2721` | component-complete; admission barred |
| `C-B-V008-07` | `d63398de212f069b42cc6c1d15dc9919b407771ed274dea0efa7cb5d022dd996` | `4dda6ffcddfafd68661d708ad76f4caa2ab0d85bff26ac739cf5fd0fcb6179ed` | component-complete; admission barred |
| `C-B-V008-09` | none | none | `GAP_ABSENT_OF_RECORD_NO_ENVELOPE` |

Every shell fixes `execution_allowed=false`, `admission=BARRED_STEP11_SUBGATE`, and `chain_invoked=false`. “Envelope-ready” in this report means component bytes and invocation shells exist. It does not mean admitted, independently verified, executed, replayed, or passed.

## 9. Static check, dry-run, and controls

The build and replay transcript is:

```text
BATCH2_BUILD=PASS rows=5 envelope_ready=4 gap=1 chain_invoked=false
BATCH2_REPLAY=PASS inventory=44 rows=5 envelope_ready=4 gap=1
COLLISION_RC=2
BATCH2_REFUSE OUTPUT_COLLISION:generated
```

The read-only replay rehashed all 44 inventory members, recanonicalized every JSON member, recomputed the package content root, replayed every bound source span, validated all five closed instances, required the exact seven-field invocation shape, and reconfirmed the four shell custody flags. The occupied-output control exercised the write refusal.

The self-check additionally records named controls for descriptor-terminator inclusion, source-span perturbation, a derived instance without grounding, a gap carrying an authored object, and an executable envelope. These are contract-level refusal cases; none is silently converted to a row verdict.

## 10. Gate and verb audit

F_PLDEC is clean. This relay performs byte hashing, exact span extraction, closed-schema serialization, finite list generation, structural type checks, mutation generation, pinning, and replay only. It performs no member binding, fixed-point execution, end test, numeric evaluation of a physical quantity, or comparison to a measured constant. `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false` remain in force.

M-2 checks covered exact and normalized token forms, hyphenation-sensitive concepts, backticked symbolic names, and source-span meaning. The decisive V008-09 search is intentionally exact-token and is accompanied by a semantic probe of the nearby public-closure/Maxwell prose; neither mode supplies the missing machine objects.

PRE-SEAL PIN CHECK: the output path and adjacent seal path were absent before authoring; the final artifact is sealed only after its complete bytes are written, and the adjacent digest is rechecked before return.

Verb audit: **CLEAN**. “Derived” means serialized from the cited sealed displays. “Generated” means a bounded tooling output. “Envelope-ready” means component-complete with admission barred. None asserts a scientific result, a row PASS, registrar authority, corpus adoption, or evaluator closure.

ROWS = 5 selected (justified)
STATUSES = C-B-V008-01:ENVELOPE_READY_COMPONENTS_COMPLETE_ADMISSION_BARRED; C-B-V008-02:ENVELOPE_READY_COMPONENTS_COMPLETE_ADMISSION_BARRED; C-B-V008-04:ENVELOPE_READY_COMPONENTS_COMPLETE_ADMISSION_BARRED; C-B-V008-07:ENVELOPE_READY_COMPONENTS_COMPLETE_ADMISSION_BARRED; C-B-V008-09:GAP_ABSENT_OF_RECORD_NO_ENVELOPE
SKIPPED = none (no ruling-shaped element encountered; V008-09 is a propagated evidence gap, not a skipped ruling)
ENVELOPE_READY += 4
ADMISSION = barred, stated
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
