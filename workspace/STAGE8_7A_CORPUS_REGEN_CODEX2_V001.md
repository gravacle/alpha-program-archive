# Stage 8 / 7A Step 11 — V009-08 corpus candidate regeneration

**Lane:** CODEX 2  
**Relay:** 763  
**Scope:** resolve `INC-08-1`, `INC-08-2`, `EXC-08-1`, and `EXC-08-2` at the Family-4 rule-execution boundary; emit one unsealed replacement candidate

## 1. Pickup, pins, and jurisdiction

The single inbox relay `RELAY_PASTE_763_CORPUS_REGEN_CODEX2_V001.md` passed its adjacent seal before reading: artifact SHA-256 `db88886000a37ece07a95c8ef70e0a9347d504c5336c9f84237afd51dd4d8646`, sidecar SHA-256 `d8bdaee03cab7b963ad13d49ab5b1c97aa0b1241810e60d276a128e3456cfbad`. The CODEX 2 lane guard matched, the report name was absent in the cleanroom and archive workspace, and `relay_outbox/763_ACK.md` was written before task work.

The governing bytes reverified:

| Authority/input | SHA-256 | Seal SHA-256 / custody |
|---|---|---|
| `CORPUS_SELECTION_RULE_V001.md` with V002/V003 amendments | `653581bf54313ef026add193c1d08dde29bcb5e9cde78e5b0383e140114fd495` | `03cb07f7a3206e8bf5725c0891b74735946926b44c522194eeb1fa4f9e85faac` |
| corpus-selection authority decision | `0dfc6e7bb761850e7cb4996c9a0b63e94567c7ae88c7de837f78b3b5628e2ad7` | `27b2c35c70dab9bb4770b61f0b579fda4a08cced10f0196459228f5222eb52ef` |
| verification half A / four findings | `a9fee84efabe86098ec8b656bddca73dcf9a17f6164eb71927b2d8e48bcd6624` | `ff34462b751dc10bcc9716662346f954b9b5bb9f30d985d8de0cd9bf0ccfac9a` |
| evaluator spec V012, packet-manifest pin authority | `382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504` | `74648af1726c861edc4ec8bda1b17e351e572a3296a1090169e526bd5085fde7` |

The selection rule was not amended. Its existing terms already require the full program census, the V002 all-token conjunction, an S1/S2/S3 seal attachment on each member, and an `EXCLUDED-UNSEALED` record. The defect was Family 4's former implementation: it rewrapped the earlier `rd22.sealed-corpus-definition.v001` member list and asserted `ALL_TOKENS_CONJUNCTION_V002` without executing that predicate or the completeness census.

## 2. Rule execution and regenerated candidate

Family 4 now has a single generated rule-execution path for this claim corpus. The default candidate builder delegates to the same implementation exposed by `--regenerate-v009-08`; the old rewrap block is gone. The implementation:

1. enumerates the three standing program roots with the four standing suffixes and directory exclusions;
2. over-generates token hits for `general` AND the `FS`/Fubini-Study surface family;
3. groups identical bytes by SHA-256;
4. resolves S1 sidecars, S2 packet rows, and S3 sealed inventories;
5. separates subject claim sources from process/mention artifacts;
6. emits every unsealed matching digest in `excluded_unsealed` and every attached nonclaim digest in `excluded_attached_nonclaim`;
7. emits members only when the conjunction and attachment both hold; and
8. validates the result against the closed `rd22.step11.corpus-candidate.v002` schema before writing its content-addressed filename.

The pre-output census recorded in the candidate is:

| Root | Path entries |
|---|---:|
| physical program tree | 15,045 |
| `/Users/bgm/MB Work/alpha_supervision` | 906 |
| physical `_external_handoffs` tree | 156 |
| **total** | **16,107** |

The 16,107 path entries collapse to 9,588 distinct byte digests. The deliberately over-generating four-mode probe found 248 path entries / 182 digests. Classification is exhaustive over that probe surface: 1 selected digest, 37 attached-but-nonclaim digests, and 144 unsealed digests. Attachment coverage over matching digests was S1=37, S2=1, S3=0, UNSEALED=144. These counts are generated current-state counts, not the withdrawn historical denominator or a hand-curated list.

The emitted candidate is:

```text
step11_tooling_family4/generated/corpus_candidates/
0a1348591c1ab30a15abb5a0849e90beb00f2b6a9458b563896d9131d15693f2--C-B-V009-08_general_FS_claim_REGENERATED.json
```

| Field | Generated value |
|---|---|
| candidate SHA-256 / bytes | `0a1348591c1ab30a15abb5a0849e90beb00f2b6a9458b563896d9131d15693f2` / 85,115 |
| schema | `rd22.step11.corpus-candidate.v002` (closed) |
| member count | 1 |
| declared root | `af9d8c3299338b18b57d842183311cf63f8a0329e683350104fa3e755e88ea77` |
| selected member | `review_packets/STAGE7_QSPEC_CANDIDATE_V001/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` |
| selected member SHA-256 / bytes | `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a` / 78,794 |
| attachment | `S2_PACKET_MANIFEST`; manifest `9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311`; exact row `[7694,7808)`, span SHA-256 `ed618aff5543920d9ec300ac360b3b06ca3e8bef9680e44ceed8f752f1f3c8d4` |
| alias-table status | `NONE_OF_RECORD`; query and empty pin list displayed |
| custody status | `CANDIDATE_REGENERATED_UNSEALED_AWAITING_DUAL_VERIFY_AND_REGISTRAR` |

The candidate records all eight `general` byte spans and all eight `FS`/Fubini-Study byte spans in the selected source, the 12 observed in-universe copies of that digest, the authoritative packet member, its exact S2 row, every excluded-unsealed digest, and every attached nonclaim digest. Its declared root recomputes over the selected member's content ref.

## 3. Four findings resolved

| Finding | Rule-level cause in the old path | Generated resolution | Why the disposition follows the rule |
|---|---|---|---|
| `INC-08-1` | The old implementation trusted the inherited member list and never evaluated the V002 conjunction. | The old 603-byte premise is in `excluded_token_miss` with `missing_tokens:["general"]` and reason `TOKEN_CONJUNCTION_MISS`; it is absent from `candidate_members`. | Its `FS` occurrences do not discharge the independently required `general` token. The negative control checks this exact miss. |
| `INC-08-2` | Old member records had only `{relative_path,byte_length,sha256}`; no receiving field existed for S1/S2/S3. | Candidate-v002 member records require `seal_attachment`; the sole selected member carries `mode:S2_PACKET_MANIFEST`, the manifest pin, exact row, row digest, and packet member name. | A content digest alone is no longer sufficient. Validation replays the manifest span and requires the member digest inside it. |
| `EXC-08-1` | The old implementation never searched, so it could not discover the sealed V011 source. | The census sees 12 in-universe copies of digest `aa7c6d49…`, resolves that digest through the spec-pinned packet manifest to the authoritative V011 bytes, verifies both tokens, and includes it. | V011 is the unique matching subject-source digest with a lawful S2 attachment; it is use, not a process mention. Omitting the selected digest now makes validation refuse. |
| `EXC-08-2` | No search roots, glob/exclusion census, unsealed table, or alias-table state existed. | The candidate carries three roots with per-root counts, suffixes, exclusions, total/distinct/probe counts, attachment counts, complete `excluded_unsealed` and `excluded_attached_nonclaim` arrays, and an alias-table query with `NONE_OF_RECORD` plus `pins:[]`. | The absence of a sealed general/FS alias table is a rule-level corpus fact, not permission to invent aliases. Because no alias expansion was used, the explicit bounded absence closes the prior silent gap while surfacing the fact for registrar review. |

No member list was hand-edited. The selected set, the rejected old member, all tables, the content root, and the filename digest were generated from current bytes.

## 4. Tool and contract delta

| File | Before | After | Bounded change |
|---|---|---|---|
| `step11_tooling_family4/generate_corpora_pins_envelopes.py` | `d1f486035f6edf75a9fc0e97a70115d60db130583b292d037b25843dfb617899` | `308931d6076d0da079778a0724075711c64522f32bfe07d2ca745c37b8634c9d` | Replace V009-08 list rewrap with generated census, token, attachment, classification, validation, refusal-control, and regeneration paths. |
| `step11_tooling_family4/contracts/tooling_family4.schema.json` | `d34f261f665f33e3d8237b76d0bf0a2185f4b9d2b1c621f79e9ac9b355906b77` | `b12636faea124ae6d488599ddb3fcf38244c45e12e8e7380db20f9a0f44afd50` | Add the closed candidate-v002 interface, including member attachments and completeness carriers. |
| `step11_tooling_family4/inventory.generated.json` | `cad220a2c96831b850aed33cacb522e3622d641f305e1564cf4b3c4289fdee67` | `f66d9107be27663c74df14963450c609bb6b6a8862814666e35127ce0c118bd7` | Regenerate the 21-member package inventory over the fixed tool, contract, and new candidate. |

The tool deliberately over-generates probe candidates, then classifies them under closed reasons. It does not promote any process artifact merely because it mentions both tokens. The new candidate remains unsealed and is not substituted into an admitted envelope.

## 5. Controls and static replay

The generation run executed four named controls:

| Control | Expected | Observed |
|---|---|---|
| old member requires all tokens | `general missing` | `general missing` — PASS |
| selected member carries attachment | `S2_PACKET_MANIFEST` | `S2_PACKET_MANIFEST` — PASS |
| selected member omitted | refusal | `CLAIM_V002_ROOT` — PASS |
| excluded-unsealed census | 144 | 144 — PASS |

An independent post-generation static replay returned:

```text
01 AST_PARSE PASS
02 CONTRACT_GENERATED_BYTES PASS b12636faea124ae6d488599ddb3fcf38244c45e12e8e7380db20f9a0f44afd50
03 CANDIDATE_CANON_AND_NAME PASS 0a1348591c1ab30a15abb5a0849e90beb00f2b6a9458b563896d9131d15693f2
04 CANDIDATE_RULE_REPLAY PASS
05 CLOSED_SCHEMA PASS
06 S2_MEMBER_AND_SPAN PASS
07 OLD_MEMBER_NEGATIVE_CONTROL PASS
08 OMISSION_REFUSAL PASS CLAIM_V002_ROOT
09 INVENTORY_REPLAY PASS 21 f66d9107be27663c74df14963450c609bb6b6a8862814666e35127ce0c118bd7
10 CHAIN_INVOKED false
```

PIN CHECK: candidate filename/content, packet member, packet manifest and exact row, generated contract, tool, and all 21 inventory rows rehashed. Canonical JSON and the closed schema both validated. The report filename remained clear immediately before authoring.

## 6. Custody and verb audit

This relay generated a **candidate**, not a sealed corpus instance. It did not supply Dario's independent half, seal or register the candidate, bind it into an evaluator envelope, invoke M2, or invoke the chain. The board and existing seals are unchanged. `alpha_computed=false`, `proof_authorized=false`, and `kappa_record_computed=false`; there was no member binding, fixed-point execution, end test, physical-quantity evaluation, or measured-constant comparison.

Verb audit: **CLEAN**. “Resolved” is scoped to the four defects in the regenerated candidate carrier and selection path. It does not mean the candidate has passed half B, been sealed by the registrar, been admitted, or closed any evaluator row.

FINDINGS_RESOLVED = 4/4 (each displayed; rule-level causes named)
TOOL = fixed (displayed, controlled)
CANDIDATE = regenerated (0a1348591c1ab30a15abb5a0849e90beb00f2b6a9458b563896d9131d15693f2)
STATUS = unsealed, awaiting half B + registrar
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
