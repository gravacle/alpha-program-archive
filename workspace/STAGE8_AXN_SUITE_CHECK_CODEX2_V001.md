CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = DECLARED-FIRST
CLOSURE_BEGIN_BYTE = 00000000
PREDECLARATION_REGION = EMPTY (closure opens at byte 0; no text precedes it)
PREDECLARATION_OUTPUT_SCAN = 0 hits in authored prose (27-token sweep)
VERDICT_BEARING_SET = exactly the 10 content-addressed members below
UNDECLARED_SEARCH_SURFACE_VERDICT_WEIGHT = forbidden
LANE = CODEX 2   ROLE_THIS_RELAY = OPPOSITE-LANE CHECKER / INSTRUMENT AUTHOR
SUBJECT_STATUS = CLAIMED until this check
```

| # | Closed member | SHA-256 / bounded-span SHA-256 | Role |
|---:|---|---|---|
| 01 | `relay_inbox/RELAY_PASTE_972_SUITE_CHECK_CODEX2_V001.md` | `d2ae2239584568d648fafb052cd5c33a994e61c41b43b43aeb3a8870b830d866` | assignment and authorial-interpretation authority |
| 02 | `PROGRAM_STATE_BRIEF_V005.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c` | state pin |
| 03 | `STAGE8_AXN_SUITE_INSTANCE_DARIO_V001.md` | `b384c473a338717eb6f351b6c48bcf6ab1ee6c2d76f9d9749e36fe859362bacd`; replay object `[3692,4437)` `c66c349a710527704f851539940c48a966144c72714d42f4da67bb0d11602d3e`; final suite JSON `[5986,9244)` raw-byte SHA-256 `c566edb9969a838bda1db282bbb0d46771acdf5f76dc2c8b0ff611902ea00345` | subject, authored replay procedure, final canonical object |
| 04 | `STAGE8_AXN_FAMILIES_V004_CROSSCHECK_CODEX2_V001.md` | `3cb349ea0d945d21c3f49d04ab9636f2cf1c6302c761bb58ddf3d2c3c0499eec` | seven wrapper defects to recheck |
| 05 | `STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V004.md` | `a195edb03b36be44bf8ce1b71dbf1a01a3a0956c4afc65ddf17382cdca4ed0ab`; closed suite schema `[21854,24285)` `e8b7132a2cbaa05e2eb4a45f2fbbe60a8ca12a0bfeef4cb12ce4a71956eb4167` | governing schema authored by this lane |
| 06 | `STAGE8_AXN_FOR_CLASS_FAMILIES_DARIO_V004.md` | `28bc43a0a8e841f11d382a11d83634938f5eab0b94fe0f59737b290dbc1d6222` | eight family payloads and certificate bodies |
| 07 | `STAGE8_AXN_STAGE_RULE_CONSTRUCTION_CODEX2_V002.md` | `f450b0a356b249509fb59b897c4f6a14e6996ba7da5ea513e69112a89907eed9`; ordered receipt-list payload SHA-256 `9451020e12f72fe5ede31a7e75692e784c559a3854981db00105657d9d6bdb41` | seven receipt payloads, list order, root, and gate 3 |
| 08 | `JOINT_ANCHOR_DECISION_INSTANCE_V003.md` | `089af246cbc0d66e6ce70971dbb14d355a78ee0f5e294706a1acaeacd0d4236d` | entered carrier and blind A0 fiber digest |
| 09 | `LOCKED_PROCESS.md` | `38149496a2b5d89d20b614d972bffef1867d7cde573b26d77dfb207ece3446fb` | process and custody law |
| 10 | `DECLINE_REGISTER_V002.md` | `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a` | S01-S37 flattening guard |

All ten whole-file members and all available adjacent seals verified before use. The output name and
sidecar were absent before write. No physical quantity was evaluated.

CLOSURE_DECLARATION_END

# STAGE 8 — AXN JOINT-ANCHOR SUITE INSTANCE — OPPOSITE-LANE CHECK
## CODEX 2 — RELAY 972 — `[PLAN:AXN-BUILD-C71]`

Date: 2026-08-10  
Status: **FAILURES NAMED. The suite is field-exact, the seven 970 wrapper defects are closed, the
staged digest convention is accepted as the schema's reading of record, the freeze is lawful, both
receipt lists and the external certificates replay, and all recorded hashes reproduce. The sole new
blocker is the authored replay entry: its seven steps do not validate the suite against the closed
schema, field types, constants, or exactly-one-variant rule. A replay point that would not catch the
970 defect class is insufficient. RUN 4 does not go.**

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member_binding = false
fixed_point_execution = false
end_test = false
JOINT_ANCHOR_DERIVED = false
```

## 1. Independent three-level schema diff

I extracted the `JointAnchorCertificateSuite.v001` block from its opening token through its matching
closing brace, established that block's own zero indentation, and derived child levels from brace
depth. I did not slice by a presumed surrounding-document indent. The final JSON was parsed
independently and compared by exact key set at each closed level.

| Level | Governing keys | Instance keys | Missing | Extra/renamed | Verdict |
|---|---:|---:|---|---|---|
| outer | 9 | 9 | 0 | 0 | EXACT |
| `finite_stage_inventory.BOUNDED_CLASS` | 8 | 8 | 0 | 0 | EXACT |
| `for_class` | 8 | 8 | 0 | 0 | EXACT |

`finite_stage_inventory` has exactly one member, `BOUNDED_CLASS`. The eight family values occur under
the schema's exact semantic names. No `cert_if_joint_sha256`, `cert_a_joint_sha256`, `fc_01`, or
other private key remains. Exact const values for `schema`, `escape_text`, and
`canonical_serialization` match. The displayed final JSON is byte-identical to independently
serialized canonical JSON with sorted keys, tight separators, and no terminal linefeed.

### 1.1 The seven 970 defect classes

| 970 defect | V001 observation | Disposition |
|---|---|---|
| `suite_sha256` absent | present as `dec168f2...` | CLOSED |
| `frozen_pre_output_receipt_sha256` absent | present as `0aef5437...` | CLOSED |
| undeclared certificate fields inside suite | absent; certificates moved outside | CLOSED |
| universal receipt list renamed/collapsed to a root | exact seven-entry list under exact key | CLOSED |
| outer receipt list replaced by a root | exact separate seven-entry list present | CLOSED |
| eight `for_class` keys renamed `fc_01..fc_08` | all eight exact schema keys present | CLOSED |
| class/trigger pointers and replay entry unbound | V004 template values present; replay object displayed and hash-bound | CLOSED as a wrapper defect |

The last row's replay object is content-addressed; its **procedural sufficiency** is a separate new
finding in §5.

## 2. Digest convention — authorial ruling

The schema types two lowercase SHA-256 fields but states no coverage convention. As the instrument's
author, under the relay's express authority, I accept this staged reading as the **schema reading of
record**:

```text
stage 0 = canonical suite with suite_sha256 and frozen_pre_output_receipt_sha256 omitted
suite_sha256 = SHA-256(stage-0 bytes)

stage 1 = canonical suite with suite_sha256 inserted and freeze field omitted
frozen_pre_output_receipt_sha256 = SHA-256(stage-1 bytes)

final = canonical suite with both fields inserted
```

This is not a claim that either digest covers bytes containing itself. Each field covers strictly
earlier canonical bytes, avoiding circularity while binding every prior field. The reconstruction is:

| Stage | Independently serialized bytes | Independently derived SHA-256 | Recorded value |
|---|---:|---|---|
| 0 | 3074 | `dec168f2254712e8cfe3f0364096e67d5c6a0d9acc3e20fcc7b4ba67c13e72b2` | exact `suite_sha256` |
| 1 | 3156 | `0aef54371edbe0dccff332d190e72cabe6b99192289ffb835e9131b0043dd048` | exact freeze receipt |
| final | 3258 | `c566edb9969a838bda1db282bbb0d46771acdf5f76dc2c8b0ff611902ea00345` | raw final-object byte digest, displayed here to prevent conflation |

Under this accepted convention, `dec168f2...` is the schema-defined suite identity used by the
certificates; `c566edb9...` is the ordinary digest of the final canonical line. They are deliberately
different objects and must not be substituted for one another.

## 3. Freeze act

Gate 3 requires the replay entry, suite hash, and freeze receipt to follow complete earlier suite
material and bars computation over a partial suite. That ordering now holds. Stage 0 contains every
nondigest suite field including the replay-entry digest; stage 1 inserts the accepted suite identity;
the receipt hashes stage 1 before any gauntlet output; the final serialization then inserts the
receipt itself. The enclosing subject was sealed afterward.

Under the accepted staged convention, this is a lawful pre-output freeze. It authors no clock value,
state, rank, candidate, or downstream result.

## 4. Receipt lists and identity

Every stage-ground receipt payload was rehashed independently, excluding terminal linefeeds:

| Receipt | Bytes | SHA-256 |
|---|---:|---|
| RL-01 | 326 | `9c8a59013b4fca4f50dbe6371326532b5b1757a785ebf31a32df18dcb46f6913` |
| RL-02 | 379 | `da32d82e0790391df7de262cab00df2c0a32e1008ca37227824ae083f1b85aaf` |
| RL-03 | 389 | `295c8410b1d919a2cbb7c2d13a5896e6a36c76be4e37073ee72e149d81b717cd` |
| RL-04 | 414 | `93d96b38d4f0e36ab8baab7e8d69b654abe6797005bafaaa02fa533c5631d8af` |
| RL-05 | 356 | `eff9ea75626eb283d7d3919329cc6890211d137ec747c1bc2813a6b4c5acc79f` |
| RL-06 | 525 | `37244a9ee40ae7dad0bdd66e94b6f088773f9ca26c594aa9791316d2379d10af` |
| RL-07 | 561 | `cb265f2b5471f2417b0a40e27f75b11f1f638bbfc597c483546cd273e3dba3c1` |

The ordered `JAC14-RL-LIST` line is 530 bytes and rehashes to
`9451020e12f72fe5ede31a7e75692e784c559a3854981db00105657d9d6bdb41`.
Both suite receivers contain the same seven strings in the same order. They are distinct JSON list
instances and compare byte-for-byte equal; the root agrees with `ordered_receipt_root_sha256`.
`outer_receipts_identity` is therefore received rather than asserted over absent operands.

## 5. Replay-entry sufficiency — new blocker

The authored replay line at `[3692,4437)` is 745 bytes, has seven pipe-separated fields, and rehashes
to the suite's `replay_entry_point_sha256`,
`c66c349a710527704f851539940c48a966144c72714d42f4da67bb0d11602d3e`.
Its procedure is deterministic and covers useful work:

1. tuple field counts;
2. eight family digests;
3. seven receipt digests and ordered root;
4. byte/digest equality of the two receipt lists;
5. resolution of content-addressed grounds;
6. the accepted stage-0 suite digest; and
7. the stage-1 freeze receipt.

It does **not** parse the final suite against `JointAnchorCertificateSuite.v001` or validate:

- the exact outer / `BOUNDED_CLASS` / `for_class` key sets;
- missing and additional properties;
- exact const values and field value types;
- the exactly-one-variant rule; or
- canonical serialization conformance as a schema property.

Those are not cosmetic omissions. They are precisely the class of failures in the 969 wrapper that
970 caught. A replay entry that can recompute self-consistent hashes without detecting an extra,
renamed, missing, wrong-type, or second-variant field is not sufficient to re-verify the closed
suite. `scope=JointAnchorCertificateSuite.v001` is a label, not an executable schema check.

The bounded repair is one additional first step: parse the final JSON under the governing V004
schema and fail on any key-set, type, const, one-variant, or canonical-serialization deviation.
Because that edit changes the replay-entry digest, it mechanically changes stage 0, both staged
digests, the final suite, and the two external certificate bindings. All descendants must be rebuilt
together; none may be silently patched.

## 6. External certificates

Both certificate objects remain outside the suite and bind the accepted schema-defined suite
identity `dec168f2...`:

| Certificate | Subject span | Bytes | Fields | SHA-256 | Verdict |
|---|---:|---:|---:|---|---|
| CERT-IF | `[11709,12665)` | 956 | 8 | `a30ca4a7970e35fb496d328314dc070c54ebe17e9575456f3222347ff6c6b42c` | CONFIRMED |
| CERT-A | `[12679,13629)` | 950 | 8 | `65d825d7aaa76ddc071b15f51bfb6c66714f6c3d7c23fcf04ccf3fe86296d658` | CONFIRMED |

Their bodies match the V004 certificate bodies apart from the disclosed `instantiates` extension to
the accepted suite identity. Both parse at their declared eight-field count. CERT-A retains the exact
BI instance spans already confirmed at 970.

## 7. FREEDOMS-CONSUMED, flattening, and fences

```text
JOINT_ANCHOR_INPUT = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  the governing V004 schema and bounded-class template;
  the eight family digests and two certificate bodies;
  the entered carrier and blind A0 fiber digest;
  the seven receipt payloads, lists, and ordered root.

AUTHORED / INTERPRETED HERE:
  ACCEPTED-AS-READING-OF-RECORD -- the displayed stage-0 / stage-1 digest convention.

SUBSTITUTED:
  NOTHING.

REMAINS TO REBUILD:
  replay entry with a closed-schema validation step;
  its digest, stage-0 suite identity, stage-1 freeze receipt, final suite bytes,
  and both certificate instantiates bindings.

SCALING WEIGHTS: NONE CONSUMED; NONE FIXED; NONE SUBSTITUTED.
```

- **FLATTENING CHECK:** held. An exact schema diff performed in this report was not flattened into a
  schema check inside the replay entry; a scope label was not flattened into an operation; stable
  hashes were not flattened into completeness; and the schema-defined staged identity was not
  flattened into the ordinary final-byte digest.
- **BLIND:** held. The A0 fiber remained an unopened digest; no rank-shaped object, ratio, or fiber
  comparison was exposed.
- **PE-1..PE-15:** pointer-only and zero verdict weight.
- **F_PLDEC:** canonical byte strings, tuple arities, schemas, and cryptographic digests only. No
  physical quantity was numerically evaluated and no measured constant was compared.
- **PIN CHECK:** output name absent before write; all whole-file members and available sidecars
  matched; every bounded span and staged digest rehashed.
- No member binding, fixed-point execution, end test, gauntlet run, or downstream chain was invoked.

## 8. Verdict

The suite instance itself is field-exact under the accepted convention, and all seven defects from
970 are closed. The only remaining failure is the replay entry's omission of the governing schema
validation. Because JAC-14 makes the replay entry load-bearing, the suite does not yet book and RUN 4
does not go.

Self verb audit: “accepted” is explicitly an authorial reading of a silent schema, authorized by the
relay. “Exact” is used only for independently compared key sets, consts, lists, bytes, and digests.
The replay object is called deterministic and content-addressed, but not sufficient.

## 9. Final lines

```text
CLOSURE = declared-first (byte position 0, scan 0 hits)
SCHEMA_DIFF = REPLAYED-EXACT
SEVEN_DEFECTS = CLOSED
CONVENTION = ACCEPTED-AS-READING-OF-RECORD (stage 0 omits both digest fields; stage 1 inserts suite_sha256; final inserts the stage-1 freeze receipt)
FREEZE = LAWFUL-NOW
LISTS = CONFIRMED
REPLAY_ENTRY = INSUFFICIENT (no governing closed-schema/key/type/const/exactly-one-variant/canonical-form validation step)
CERTS = CONFIRMED
VERDICT = FAILURES NAMED (REPLAY ENTRY); SUITE DOES NOT BOOK; RUN 4 DOES NOT GO
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
```
