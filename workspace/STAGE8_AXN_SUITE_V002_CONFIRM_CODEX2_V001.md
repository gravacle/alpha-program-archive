CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = DECLARED-FIRST
CLOSURE_BEGIN_BYTE = 00000000
CLOSURE_END_BYTE = 00002065
PREDECLARATION_REGION = EMPTY (closure opens at byte 0; no text precedes it)
PREDECLARATION_OUTPUT_SCAN = 0 hits in authored prose (27-token sweep)
VERDICT_BEARING_SET = exactly the 8 content-addressed members below
UNDECLARED_SEARCH_SURFACE_VERDICT_WEIGHT = forbidden
LANE = CODEX 2   ROLE_THIS_RELAY = OPPOSITE-LANE CHECKER / INSTRUMENT AUTHOR
SUBJECT_STATUS = CLAIMED until this independent check
```

| # | Closed member | SHA-256 | Role |
|---:|---|---|---|
| 01 | `relay_inbox/RELAY_PASTE_974_SUITE_V002_CONFIRM_CODEX2_V001.md` | `21a5c9f5c5254e726ce89a5f751401fefda5ef6bce96c3712eb250a5b72c5c89` | assignment and closure authority |
| 02 | `PROGRAM_STATE_BRIEF_V005.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c` | state pin |
| 03 | `STAGE8_AXN_SUITE_INSTANCE_DARIO_V002.md` | `520d5f34f94316d8023990a1cab9da106f40d4fc7dc55ef0cac77a05b038dc40` | subject; replay object `[2686,3926)` and final JSON `[5773,9031)` |
| 04 | `STAGE8_AXN_SUITE_CHECK_CODEX2_V001.md` | `b2d266579c29d477a88ba21af164f9266c39a6ce119ab6fe044385cc1c824423` | relay 972 insufficiency finding and accepted staged convention |
| 05 | `STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V004.md` | `a195edb03b36be44bf8ce1b71dbf1a01a3a0956c4afc65ddf17382cdca4ed0ab` | governing closed suite schema |
| 06 | `STAGE8_AXN_SUITE_INSTANCE_DARIO_V001.md` | `b384c473a338717eb6f351b6c48bcf6ab1ee6c2d76f9d9749e36fe859362bacd` | old cascade, carried suite body, and external certificate bodies |
| 07 | `LOCKED_PROCESS.md` | `38149496a2b5d89d20b614d972bffef1867d7cde573b26d77dfb207ece3446fb` | process and custody law |
| 08 | `DECLINE_REGISTER_V002.md` | `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a` | S01-S37 flattening guard |

All eight whole-file digests and all eight available adjacent seals were verified before use. The
output name and sidecar were absent before write. No physical quantity was evaluated.

CLOSURE_DECLARATION_END

# STAGE 8 — AXN JOINT-ANCHOR SUITE V002 — INDEPENDENT CONFIRMATION
## CODEX 2 — RELAY 974 — `[PLAN:AXN-BUILD-C73]`

Date: 2026-08-10  
Status: **SUITE-BOOKS-RUN-4-GOES.** My implementation of the governing schema's five validation
classes passes the final object 5/5. The subject's step 8 tests the same five classes without a weaker
or missing receiver. The cascade, freeze, replay pointer, external certificates, and carried content
all reproduce.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member_binding = false
fixed_point_execution = false
end_test = false
JOINT_ANCHOR_DERIVED = false
```

## 1. Independent step-8 implementation

I derived these checks from `JointAnchorCertificateSuite.v001` in governing V004, not from the
subject's procedure text. The implementation parsed the final JSON line, constructed the three exact
key sets, tested the schema-typed leaf values and list receivers, compared the three const values,
counted the inventory variants, and reserialized independently.

| Class | Independently implemented acceptance condition | Result |
|---|---|---|
| exact keys | outer exactly 9 keys; `BOUNDED_CLASS` exactly 8; `for_class` exactly 8; zero missing, extra, or renamed | PASS: 9/9, 8/8, 8/8 |
| value types | all 15 typed digest receivers are lowercase 64-hex strings; the two receipt receivers are lists of strings; the remaining governed leaves are strings | PASS |
| consts | `schema`, `escape_text`, and `canonical_serialization` equal the governing bytes | PASS |
| one variant | `finite_stage_inventory` has exactly `BOUNDED_CLASS` | PASS |
| canonical form | sorted keys, compact separators, ASCII-safe encoding, and no terminal linefeed reproduce the displayed 3258 bytes | PASS |

Independent transcript:

```text
8a=True ; outer=9 ; BOUNDED_CLASS=8 ; for_class=8
8b=True ; typed_digests=15 ; list_receivers=2
8c=True ; consts=3
8d=True ; variants=['BOUNDED_CLASS']
8e=True ; canonical_bytes=3258 ; terminal_linefeed=false
raw_final_sha256=27fc5db17f38f735865645798c6dd4d49538c7696d3515093720038fc444f14c
STEP8_INDEPENDENT_RESULT=PASS-5/5
```

### 1.1 Comparison with the subject's step 8

The subject's 8a checks the same three closed key sets; 8b checks lowercase SHA values and both list
receivers; 8c names the same three const fields; 8d enforces exactly one variant; 8e enforces the same
canonical byte form. Its field-type report also checks the eight family digests, which is consistent
with the governing exact replay-object representation in this instance. No class is weaker and none
of my five checks is missing. The implementations are **EQUIVALENT** for the final suite.

## 2. Cascade, freeze, and replay pointer

I extracted the V001 and V002 JSON objects and the two replay-entry lines, then recomputed in the
accepted order. Every recorded value matches:

| Stage | Old bytes / digest | New bytes / digest | Independent result |
|---|---|---|---|
| replay object | 745 / `c66c349a710527704f851539940c48a966144c72714d42f4da67bb0d11602d3e` | 1240 / `7683259aa41b310bab781e74f805e06ff73c4e38c33da2f8f7b1f23fb7507f4e` | exact |
| stage 0 | 3074 / `dec168f2254712e8cfe3f0364096e67d5c6a0d9acc3e20fcc7b4ba67c13e72b2` | 3074 / `d20ae8d983f7002656392e91b6d094b2ff561863a3dddd76a43084e188e0bc24` | exact |
| stage 1 | 3156 / `0aef54371edbe0dccff332d190e72cabe6b99192289ffb835e9131b0043dd048` | 3156 / `f415957d3acf34dc072f7bba5e8758a2c240b047c76a9fa0abc176bc8111e171` | exact |
| final canonical suite | 3258 bytes | 3258 bytes | exact |

The equal stage and final byte counts are explained and verified: each moved suite field replaces one
lowercase 64-hex digest with another lowercase 64-hex digest. Values changed; widths did not. The new
freeze receipt is exactly SHA-256 of the new stage-1 bytes, so it was re-performed over the right
object rather than carried.

The V002 replay line at `[2686,3926)` is 1240 bytes, parses as the declared seven-field tuple, and
hashes to `7683259a...f4e`; that is exactly `replay_entry_point_sha256` in the final suite. The pointer
therefore resolves to the procedure object that contains step 8.

## 3. External certificates

V001 displays the two eight-field certificates outside its suite at `[11709,12665)` and
`[12679,13629)`. I rebuilt each V002 object from those sealed bytes by replacing only the
`instantiates` receiver's old staged identity with `d20ae8d...bc24`.

| Certificate | Bytes | Fields | Independently derived V002 SHA-256 | Changed field |
|---|---:|---:|---|---|
| `CERT-IF-JOINT` | 956 | 8 | `381e3f85c5199dc5cead8c87e74eda8d1fc93aa0c51b411744dfbfcecc34daa8` | `instantiates` only |
| `CERT-A-JOINT-BI` | 950 | 8 | `56610e0d7de18997ae0b744a7eb59c7c27d3443c21096e3b430b7f6a20932f67` | `instantiates` only |

These reproduce the subject's new digest prefixes, retain the declared counts, bind the new staged
suite identity, and remain outside the nine-field suite object. All non-identity certificate fields
are byte-identical to their sealed V001 bodies.

## 4. Carriage and relay-972 disposition

After deleting only `replay_entry_point_sha256`, `suite_sha256`, and
`frozen_pre_output_receipt_sha256` from both parsed suite objects, V001 and V002 compare equal. Thus
the carrier, blind A0-fiber digest, bounded-class object, receipt lists and root, outer identity,
trigger, and all eight family values are byte-carried. The certificate comparison above likewise has
exactly one changed field per certificate.

Relay 972 named five missing validation classes: exact keys, value/list types, consts, one variant,
and canonical form. Step 8 contains all five, and the independent run proves each bites the final
object. **No named absence remains; the insufficiency is closed.**

Every named RUN 4 precondition now stands: the eight families, the two rebound certificates, the
closed suite, the entered instance, and V004 as governing schema are all content-addressed and at
their required receivers. This is the registrar's run-cut line; it does not itself invoke the chain.

## 5. FREEDOMS-CONSUMED

```text
JOINT_ANCHOR_INPUT = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  the governing V004 schema;
  the V001 suite body, eight family values, receipt lists, and two certificate bodies;
  the accepted staged-digest convention.

AUTHORED HERE:
  an independent implementation of the five schema-validation classes;
  this opposite-lane disposition.

SUBSTITUTED:
  NOTHING. No schema receiver, key, variant, basis, matrix, candidate, or certificate body.

SCALING WEIGHTS: NONE CONSUMED; NONE FIXED; NONE SUBSTITUTED.
```

## 6. Custody and audits

- **S01-S37 FLATTENING CHECK:** walked. Digest replay was not identified with schema validation;
  staged identity was not identified with the raw final-line digest; equal byte counts were not
  identified with unchanged bytes; an external certificate was not identified with a suite field;
  independent confirmation was not identified with chain execution.
- **F_PLDEC:** only structural bytes, field counts, canonical serialization, and digests were used.
- **BLIND:** held. The A0 fiber remained a digest copy; nothing rank-shaped was opened.
- **PE-1..PE-15:** pointer-only, zero verdict weight.
- **PIN CHECK:** all closure-member digests were recomputed in full. No truncated prefix was used as
  an input. The output name and sidecar were absent before write.
- **CHAIN:** no anchor act, member binding, fixed-point execution, end test, numerical evaluation, or
  comparison with a measured constant was invoked.

Self verb audit: “PASS” refers to the displayed independent structural checks; “confirmed” refers to
byte/digest equality recomputed here; “books” is the relay-authorized suite disposition, not an anchor
act or proof authorization. `VERB_AUDIT_SELF = CLEAN`.

## 7. Final lines

```text
CLOSURE = declared-first (byte position 0, scan 0 hits)
STEP8_INDEPENDENT = PASS-5/5 (independent implementation from governing V004 schema)
STEP8_COMPARISON = EQUIVALENT
CASCADE = REPLAYED (equal-bytes explanation verified: fixed-width 64-hex substitutions)
FREEZE = CONFIRMED
POINTER = RESOLVES
CERTS = CONFIRMED
CARRIED = CONFIRMED
INSUFFICIENCY = CLOSED
VERDICT = SUITE-BOOKS-RUN-4-GOES
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
