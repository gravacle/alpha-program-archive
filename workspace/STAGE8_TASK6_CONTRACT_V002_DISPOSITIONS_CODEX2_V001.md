# STAGE 8 TASK 6 — CONTRACT V002 DEFERRED-ITEM DISPOSITIONS

Lane: CODEX 2 / Builder A custody lane  
Version: V001  
Date: 2026-08-08  
Scope: closing-ledger compilation from sealed bytes; no specification, evaluator, register, plan, tracker, or git mutation

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
MEMBER_BOUND = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false
MEASURED_CONSTANT_COMPARISON = none
```

## 0. Preflight, census, and conventions

The artifact and seal-sidecar names were absent in the cleanroom before this
file was written. `relay_outbox/710_DONE.md` was also absent. The six atomic
rows below are the complete decomposition of the five commissioned headings:
the fifth heading contains two independently deferred schema fields and is
therefore two rows. No item is merged away, and no partial implementation is
reported as a disposition.

Closed disposition schema:

```json
{
  "type":"object",
  "additionalProperties":false,
  "required":["item_id","commissioned_item","record_origin","disposition","discharging_bytes_or_7a_owner","why_complete_or_lawful","citations"],
  "properties":{
    "item_id":{"pattern":"CV2-(0[1-4]|05[ab])","type":"string"},
    "commissioned_item":{"type":"string","minLength":1},
    "record_origin":{"type":"string","minLength":1},
    "disposition":{"enum":["RESOLVED-BY","IMPLEMENT-NOW","DEFER-TO-7A"],"type":"string"},
    "discharging_bytes_or_7a_owner":{"type":"string","minLength":1},
    "why_complete_or_lawful":{"type":"string","minLength":1},
    "citations":{"type":"array","minItems":1,"items":{"type":"string","minLength":1}}
  }
}
```

`RESOLVED-BY` requires both a sealed law/interface and evidence that the live
path consumes it. `IMPLEMENT-NOW` would require Builder A jurisdiction, a
complete schema/code delta, every affected pin, and executed success and
fail-closed fixtures. `DEFER-TO-7A` is used only with a named road step and an
entry condition that prevents the gap from being exercised silently.

### 0.1 Pinned source manifest

`CR` means this cleanroom. `SUP` means
`/Users/bgm/MB Work/alpha-program-archive/supervision`. All thirteen sealed
artifact sidecars verified against the listed bytes. R01–R03 are exact current
machine bytes; R01 is certified by S12, R02 is sidecar-sealed and certified by
S13, and R03 is generated and certified by S13.

| ID | Root / source | SHA-256 | Load-bearing span or field |
|---|---|---|---|
| S01 | SUP `LOCKED_PROCESS.md` | `51b2b95a93f94bae3aced9843be301c666eb26ca829251c736f9b1e4f0aa3653` | first-time-right law, L316–L335; jurisdiction check, L353–L370 |
| S02 | SUP `ROAD_FROM_HERE_THROUGH_GRAVITY_V001.md` | `3f8fac1f270f8526a08048ba4109d9ce32a6b2236ac9fee29c76c1f82260e082` | Task 6 closing, L6–L13; 7A Step 11, L15–L32 |
| S03 | CR `STAGE8_TASK6_ROOT_MEMBERSHIP_LANE2_V001.md` | `792db074b65079c62b41285021dcdb9a6f158bcf655fe16bec30864fca6f73fa` | original Contract-V002 membership item, L59–L69 |
| S04 | CR `STAGE8_TASK6_LAUNCHER_IN_ROOT_DARIO_V001.md` | `259876aeb107b05e6ee6d94d865324f6d2c6c7c68bad54394cc7cbaff5967aff` | original name/length-binding finding, L65–L85 |
| S05 | CR `STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V012.md` | `382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504` | closed manifest/member schema, L1391–L1439; instance law, L1476–L1488; ground/citation schemas, L1490–L1594; seven-field carrier, L1686–L1720 |
| S06 | CR `STAGE8_TASK6_G2_MEMBERS_FIX_CODEX2_V001.md` | `4186bb8012f6918fe7d255ade357ac6e5b71ed0d539e3f591a2a986580cd59d7` | sole sealed-instance carrier and real validation, L30–L81 |
| S07 | CR `STAGE8_TASK6_V008_SEVEN_FIELD_CODEX2_V001.md` | `c597153ed5a108a4116001c2c97f52ac021898dde6b5909437a52aca973d2b2b` | seven-field emitted carrier, L64–L91; generated single pin manifest, L124–L136 |
| S08 | CR `STAGE8_TASK6_V010_GROUND_ATOMS_CODEX2_V001.md` | `bf6a132d97faab823b8aad096444d3a70d91512069ce6538edf77ae6d06b5f46` | exact ground-atom class and lawful producer omission, L27–L52; code finding, L88–L100 |
| S09 | CR `STAGE8_TASK6_V011_CITATION_KEY_CODEX2_V001.md` | `82873bd53d70fcd20059094562e3f7beae01d98c127d63875ce08d92cd80280d` | exact source/span name binding, L30–L56; unchanged A programs, L93–L105 |
| S10 | CR `STAGE8_TASK6_RUN022_CERTIFICATION_DARIO_V001.md` | `e6e0a8a42839b0b3de1c18775c38061e690decc40bab1ff61b0ff48e8472486b` | positional fixture finding, L99–L115 and L200–L208; incomplete replay ledgers, L210–L223 |
| S11 | CR `STAGE8_TASK6_ROW_CONTRACT_DARIO_V001.md` | `ce9ff15818307366ae93dd3082cb27398ff0705a07933864b76f1a88f5572925` | dead-helper removal and two unsurfaced fields, L217–L232 |
| S12 | SUP `CERTIFICATION_FIRST_LAWFUL_PASS_2026-08-08.md` | `e086a5cea8bab1c2f4b70200fcbda104b89252aa91a9fb4da4b7a62a8959b47f` | run-033 certification and 58-item remainder, L5–L24 and L35–L42 |
| S13 | CR `STAGE8_TASK6_BOUNDARY_REPIN_CODEX2_V001.md` | `d3fc9442a6574072707a69841b45678bfaaf8b1a4d5b3c2b6b0befc18549a3cc` | current generated pins and live sealed instance, L10–L33, L39–L46, L82–L113 |
| R01 | CR `rd22_run_033/verifier.output.json` | `aea5d4a89347d963e26853dc3280d36823dd2592e43effcff810b906eec727a7` | `findings[55..57].detail`; `checks_replayed`; `fixtures_replayed` |
| R02 | CR `evaluator_build_B/rd22.verifier-manifest.v001.json` | `b43912455db38ebdebe603547d8a733b294b7a16b9f5999f1180da16a7d11961` | sealed twelve-field instance; `verifier_root_members[0..13]` |
| R03 | CR `evaluator_build_A/manifests/pins.json` | `c450b90dc93dfd0ae041d939a34ffa60e9bc286a81a7ff5efd044b3474d2b101` | generated `rd22.builder-a-pin-manifest.v001`, 27 pin rows |

## 1. Closed disposition ledger

| Item | Commissioned item | Record origin | Disposition | Discharging bytes or 7A owner | Why the disposition is complete and lawful | Citations |
|---|---|---|---|---|---|---|
| CV2-01 | pin manifest + membership in instance | Builder A recorded the stale private census as a Contract-V002 item. | RESOLVED-BY | V008 installed the single generated pin manifest. V009/V012 installed the closed `verifier_root_members` array in the sealed verifier-manifest instance, and G2 removed Builder A's redundant copy. The current generated pins are R03; the current sealed instance is R02. | The parent consumes the sealed instance, requires sorted unique package-relative paths, verifies each `{byte_length,relative_path,sha256}` row against package bytes, and derives the declared root. A membership change now requires a reissued B instance and regenerated A pin manifest, not an A source census. | S03:L59–L69; S05:L1391–L1439; S05:L1476–L1488; S06:L30–L81; S07:L124–L136; S13:L20–L46; R02:`verifier_root_members`; R03:`pins` |
| CV2-02 | name-binding scheme | The 667 review found that the content-root formula alone did not bind member names or lengths. | RESOLVED-BY | The sealed manifest-instance digest binds every member row's `relative_path`, `byte_length`, and `sha256`; the parent validates those fields against resolved package bytes before accepting the content root. The seven-field invocation separately binds `result_name` to opcode, source digest, half-open span, and span digest. V011 binds a ground atom's `member_key` by exact `(source_sha256,span)` tuple, exactly-one cardinality, with filename/self-digest/producer mappings forbidden. | This does **not** rewrite history by claiming that `verifier_root_sha256 = SHA256(concat(row.sha256))` itself binds names. The name and length are authoritative because they are closed fields inside separately hash-pinned R02 and are checked against the files. The later invocation/citation laws close the analogous runtime symbolic-name ambiguity without producer choice. | S04:L65–L85; S05:L1423–L1439; S05:L1476–L1488; S05:L1552–L1594; S05:L1686–L1720; S06:L55–L76; S07:L64–L91; S09:L30–L56; R02:`verifier_root_members` |
| CV2-03 | positional fixture identity | Run 022 findings used `fixtures[2]`, `[3]`, `[4]` rather than fixture IDs. | DEFER-TO-7A | **Owner: 7A Step 11, Builder B contract/replay subgate, before the first fixture envelope is admitted.** Required whole fix: finding schema and emitter carry `fixture_id`; success and fault fixtures prove identity survives fixture-order permutation; B reissues schema/root/instance and A's boundary pins regenerate in the same delta. | The defect is still visible in certified run 033: R01 `findings[55..57].detail` remains positional. It did not affect the one confirmed check row or Task 6's honest aggregate FAIL, and all three missing fixture observations belong to the 58-item formalization remainder. Deferral is lawful only as a Step-11 entry condition; it may not survive into the first fixture-envelope execution. Builder A cannot implement Builder B's verdict schema or verifier emitter in this lane. | S10:L99–L115; S10:L200–L208; S12:L5–L24; S12:L35–L42; S02:L27–L28; R01:`findings[55..57].detail` |
| CV2-04 | replay-ledger coverage | Run 022 recorded only non-running rows in `checks_replayed`/`fixtures_replayed`, leaving faulted rows findings-only. | DEFER-TO-7A | **Owner: 7A Step 11, Builder B contract/replay subgate, before the first remainder envelope is admitted.** Required whole fix: exactly one replay row per 66 checks and per 6 fixtures, explicit `PASS|FAIL|NOT_RUN_GATE|ERROR`, ID-keyed, plus totality/uniqueness tests and updated sealed schema/root/instance/pins. | Certified run 033 improves the check side only by adding the one replayed PASS: R01 still has 11/66 `checks_replayed` and 3/6 `fixtures_replayed`; the 55 check and 3 fixture evidence faults remain findings-only. Task 6's n=1 certification is not weakened, but Step 11 cannot distinguish `FAIL` from unrecorded without this carrier. | S10:L210–L223; S12:L5–L24; S12:L35–L42; S02:L27–L28; R01:`checks_replayed`; R01:`fixtures_replayed`; R01:`findings` |
| CV2-05a | `unrequired_args` reporting schema amendment | `classify_payloads` computes `unrequired_args`, but the value has no verdict field. | DEFER-TO-7A | **Owner: 7A Step 11, Builder B verdict-contract subgate, before new opcode/envelope classes are accepted.** Required whole fix: closed schema field, deterministic per-invocation emission, empty/nonempty cases, extra/missing-field refusals, and same-delta B root/instance plus A re-pin. | The classification exists internally but sealed S11 says it is not emitted. A report-only patch would be partial and a Builder A edit would violate builder custody. The field becomes operationally material when Step 11 introduces diverse envelope arguments, so Step 11 is the first lawful execution boundary. | S11:L217–L232; S02:L27–L28; S01:L320–L335 |
| CV2-05b | coverage-direction reporting schema amendment | Declared-but-not-recorded invocation coverage has no verdict carrier; the unused helper was removed. | DEFER-TO-7A | **Owner: 7A Step 11, Builder B verdict-contract/replay subgate, before any additional envelope is admitted.** Required whole fix: report every descriptor assignment as producer-carried, independently R9-resolved, or missing; require total declared-assignment coverage; exercise each state and duplicate/unknown-result negatives; reissue all dependent schemas, roots, instances, and boundary pins together. | V008's seven-field carrier, V010's closed ground-atom exception, and V011's exact citation mapping fully discharge the special `C-B-V009-06` omission (`r_dag` producer-carried; `r_ground` independently R9-resolved). They do **not** create a general verdict field, so they are not misreported as closing this queue item. The general absent-vs-empty carrier is required before Step 11 broadens the replay surface. | S07:L64–L91; S08:L27–L52; S09:L30–L56; S05:L1490–L1594; S11:L217–L232; S02:L27–L28 |

Disposition partition:

```text
RESOLVED-BY = {CV2-01,CV2-02}                 = 2
IMPLEMENT-NOW = {}                            = 0
DEFER-TO-7A = {CV2-03,CV2-04,CV2-05a,CV2-05b} = 4
TOTAL = 6
```

## 2. Why no `IMPLEMENT-NOW` item ships here

All four live gaps are on Builder B's independently owned verifier/verdict
surface. A whole repair necessarily changes B's schema, verifier bytes, root,
sealed instance, and self-checks, followed by an A-side generated boundary
re-pin. Builder A altering only its mirror would neither govern B's package nor
ship the cross-boundary state change whole. The First-Time-Right Rules therefore
bar a one-sided patch; the custody boundary is a reason for the named Step-11
entry condition, not a reason to drop the item.

No evaluator package file changed in this relay. The only writes are this
closing artifact, its seal sidecar, and the non-evidentiary completion pointer
required at `relay_outbox/710_DONE.md` after sealing.

## 3. Jurisdiction check

| Question of record | Applied answer |
|---|---|
| What was the rule written to protect, and is the risk present? | Positional identity, replay totality, and the two reporting fields protect independent replay from aliasing `false`, `not run`, and `not recorded`. That risk is present when Step 11 turns the 58 absent envelopes into inputs. The rules keep full force. |
| Does the outcome space distinguish false from cannot-see/not-recorded? | Not yet for CV2-03 through CV2-05b. Their Step-11 entry conditions require explicit IDs and total status/report carriers before any new envelope verdict. `PRECONDITION_NOT_REPLAYABLE` remains distinct from criterion FAIL; nothing here collapses it. |
| If the theory is right, would the rule permit the evidence to appear? | Yes. The required repairs add identity and observation carriers; they do not change a criterion, evidence threshold, opcode result, halt condition, or aggregate rule. A lawful PASS, FAIL, gate, or inability-to-replay remains reportable under its own name. |

No 7A criterion is authored here. No kill condition is weakened, and none of
the four deferred items may be invoked as a reason to reject evidence before
their reporting contracts exist.

## 4. Pin closure and battery

The thirteen sealed artifact bytes and their sidecars were rehashed. R01 and
R03 rehashed to the values certified by S12/S13; R02 and its own sidecar
verified. That is sixteen pinned or certified byte targets, with zero mismatch.
Every source ID referenced by the six ledger rows resolves in §0.1.

The live current boundary facts reproduce from bytes:

```text
R03 schema = rd22.builder-a-pin-manifest.v001
R03 pins = 27
R02 schema = rd22.verifier-manifest.v001
R02 fields = 12
R02 verifier_root_members = 14
R02 member-row fields = {byte_length,relative_path,sha256}
R01 checks_replayed = 11
R01 fixtures_replayed = 3
R01 findings = 58
R01 positional fixture findings = 3
```

`F_PLDEC`: CLEAN. No disposition consumed a desired physical answer, member,
reader output, fixed-point value, target constant, or measured quantity.

Verb audit: `RESOLVED-BY` is restricted to interfaces both sealed and exercised.
`DEFER-TO-7A` does not mean harmless or optional: each row names Step 11 and a
pre-execution entry condition. No code execution, evaluator chain, member
binding, fixed point, end test, numerical physical evaluation, or comparison to
a measured constant occurred.

---

ITEMS = 6 (2 resolved-by / 0 implemented / 4 deferred, each cited)
CODE_CHANGED = none
PIN_CLOSURE = 16 hits, all resolved
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
