CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = DECLARED-FIRST
CLOSURE_BEGIN_BYTE = 00000000
PREDECLARATION_REGION = EMPTY (closure opens at byte 0; no text precedes it)
PREDECLARATION_OUTPUT_SCAN = 0 hits in authored prose (27-token sweep)
VERDICT_BEARING_SET = exactly the 5 content-addressed members below
UNDECLARED_SEARCH_SURFACE_VERDICT_WEIGHT = forbidden
LANE = DARIO   ROLE_THIS_RELAY = BUILDER (not verifier)
ALL_OBJECTS = CLAIMED until the opposite-lane spot-confirm
DIGEST_RULE = every pinned digest computed from its file; a truncated relay digest is a PREFIX
              TO VERIFY AGAINST, and completing one is forbidden
```

| # | Closed member | SHA-256 | Role |
|---:|---|---|---|
| 01 | `relay_inbox/RELAY_PASTE_973_REPLAY_ENTRY_V002_DARIO_V001.md` | `98c0a6aeb410fbffaa609facd94b38dd7541c77e5853c76c6f23bec10a905ec9` | assignment |
| 02 | `STAGE8_AXN_SUITE_INSTANCE_DARIO_V001.md` | `b384c473a338717eb6f351b6c48bcf6ab1ee6c2d76f9d9749e36fe859362bacd` | my 971 — everything but the validation step, byte-carried |
| 03 | `STAGE8_AXN_SUITE_CHECK_CODEX2_V001.md` | `b2d266579c29d477a88ba21af164f9266c39a6ce119ab6fe044385cc1c824423` | the check: one item open, the convention accepted of record |
| 04 | `STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V004.md` | `a195edb03b36be44bf8ce1b71dbf1a01a3a0956c4afc65ddf17382cdca4ed0ab` | the governing closed schema step 8 validates against |
| 05 | `PROGRAM_STATE_BRIEF_V005.md`; `LOCKED_PROCESS.md`; `DECLINE_REGISTER_V002.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c`; `38149496a2b5d89d20b614d972bffef1867d7cde573b26d77dfb207ece3446fb`; `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a` | state pin, process law, S01-S37 |

```text
BOTH SUBJECT DIGESTS WERE GIVEN IN FULL BY THE RELAY AND VERIFIED IN FULL, NOT COMPLETED.
BLIND HELD; BASIS INDEPENDENCE PRESERVED; THE FAMILIES AND SUITE CONTENT ARE BYTE-CARRIED.
```

CLOSURE_DECLARATION_END

# STAGE 8 — AXN SUITE INSTANCE — DARIO LANE — V002
## RELAY 973 — `[PLAN:AXN-BUILD-D72]` — STEP 8 AND THE DIGEST CASCADE

Date: 2026-08-10
Status: **STEP 8 ADDED, THE CASCADE RECOMPUTED IN ORDER, AND THE PROCEDURE RUN AGAINST ITS OWN
FINAL OBJECT: PASS on all five validation classes. CLAIMED.**

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1. Step 8, added

The check found the replay procedure complete but for one thing: it re-verified the object's digests
without ever validating the object against the **schema**. A replay that recomputes every hash of a
structurally wrong object still returns PASS. Step 8 closes that, making the 970/972 defect classes
mechanical:

```text
JAC14-REPLAY-ENTRY|v=001|id=SUITE-REPLAY-ENTRY|scope=JointAnchorCertificateSuite.v001|procedure=1-re-parse-every-closed-tuple-at-its-declared-field-count;2-recompute-each-for_class-member-digest-from-its-displayed-payload-bytes;3-recompute-each-of-the-seven-universal-receipt-digests-and-their-ordered-root;4-verify-outer_receipts_identity-as-byte-and-digest-equality-between-the-two-list-receivers;5-verify-every-content-addressed-ground-resolves-to-its-sealed-source;6-recompute-suite_sha256-under-the-displayed-two-stage-convention;7-recompute-frozen_pre_output_receipt_sha256-over-the-suite-completed-through-step-6;8-VALIDATE-the-final-canonical-JSON-against-the-governing-closed-schema:8a-exact-key-sets-at-all-three-levels-outer-and-BOUNDED_CLASS-and-for_class-with-zero-missing-zero-extra-zero-renamed;8b-value-types-lowercase_sha256-where-typed-and-list-where-a-list-receiver-is-typed;8c-const-fields-byte-exact-namely-schema-and-escape_text-and-canonical_serialization;8d-EXACTLY-ONE-inventory-variant-present;8e-canonical-form-conformance-sorted-keys-compact-separators-ensure_ascii-no-terminal-linefeed|determinism=byte-exact-and-order-fixed-no-clock-no-randomness-no-network|accept=every-recomputation-equals-its-recorded-value
```

```text
REPLAY_ENTRY_POINT_SHA256 = 7683259aa41b310bab781e74f805e06ff73c4e38c33da2f8f7b1f23fb7507f4e
BYTES = 1240  (was 745)   FIELDS = 7, the declared count
```

Its five sub-checks are the failure modes this build actually hit: **8a** exact key sets at all three
levels — the 969 wrapper's invented names; **8b** value types, list where a list receiver is typed —
the 969 collapse of both receipt receivers to a root; **8c** const fields byte-exact; **8d** exactly
one inventory variant; **8e** canonical-form conformance. Deterministic, byte-exact, no clock, no
randomness, no network, as steps 1-7.

## 2. The cascade, displayed old to new [PROVABLE]

Recomputed strictly in order, each stage over the previous stage's bytes:

| Stage | Old | New |
|---|---|---|
| replay-entry object | 745 B, `c66c349a71052770…` | **1240 B, `7683259aa41b310b…`** |
| `suite.replay_entry_point_sha256` | `c66c349a71052770…` | `7683259aa41b310b…` |
| stage-0 bytes → `suite_sha256` | 3074 B, `dec168f2254712e8…` | **3074 B, `d20ae8d983f70026…`** |
| stage-1 bytes → freeze receipt | 3156 B, `0aef54371edbe0dc…` | **3156 B, `f415957d3acf34dc…`** |
| final suite bytes | 3258 B | **3258 B** |
| `CERT-IF` | `a30ca4a7970e35fb…` | `381e3f85c5199dc5…` |
| `CERT-A` | `65d825d7aaa76ddc…` | `56610e0d7de18997…` |

**The freeze act was RE-PERFORMED, not carried.** The old receipt covered the old bytes; a receipt
carried across a byte change would certify a freeze that never happened. It is still pre-output — no
gauntlet output exists — so re-performing it is lawful, and it is the only honest option.

The stage byte counts are unchanged because a 64-hex digest replaced a 64-hex digest; only the values
moved. I state that rather than let equal numbers look like an un-recomputed cascade.

## 3. The final suite

```json
{"a0_rank_fiber_sha256":"5eaa8277097121cbe6fcfefc7fa2d0ac2b74c48f983a033ff40102a3549afe46","canonical_serialization":"canonical bytes; closed fields; no extras","carrier_sha256":"1467ab9850022931e68dc9ffa625d95099d8f6bb74d734dc9d0466f169bd00b6","finite_stage_inventory":{"BOUNDED_CLASS":{"bounded_class_definition":"positive-integers-N>=1-with-unique-arrow-N-to-M-iff-N<=M","escape_text":"or state a bounded class and explicit reopening trigger","explicit_reopening_trigger":"reopen on any byte change to the stage-rule ground, N>=1 class or arrows, receipt payload/list/order/root, outer-receipts identity, certificate receiver semantics, or on failure of any universal replay","for_class":{"anchor_certificate_family":"f743aee3ce8cc616f35ad33029896bf6c65fc92f356209b01957ae34e446f0e1","charge_covariance_certificate_family":"65aedce4c423b427adea9dfca8099223c600b637991adb4e07e30506340dd634","cptp_certificate_family":"b07339b7599fdc2e05f41815f77c9e6e9340a57d35396f7ad75286a835d453fb","delta0_basis_family":"8215042bb8e60b15a310b1c8a4438015ee55039312a4ccc7f6a450a566463d3e","factorization_and_inverse_family":"06233b1d5771903af2d5a723bb9d6e1fc9170467d1d7f2b129087a999350ca38","fixed_space_and_mixing_certificate_family":"5b939147f0779f787a4f4cc5250372d83610a0112561060ddbfd23a9834cf03f","phi_restriction_matrix_family":"8bb6080205f6451cb6b5fc9852711ddf9f5431aaf7987fbee05ecf078548a7ad","superselection_commutation_certificate_family":"03698d14572cc91914bc5f4f7346bdedd9fc2f61f9bdef59daeeed34382dad5b"},"ordered_receipt_root_sha256":"9451020e12f72fe5ede31a7e75692e784c559a3854981db00105657d9d6bdb41","outer_receipts_identity":"exact same ordered receipt bytes and root as restriction_and_limit_square_receipts","stage_rule_ground_sha256":"42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269","universal_restriction_and_limit_square_receipts":["RL-01:9c8a59013b4fca4f50dbe6371326532b5b1757a785ebf31a32df18dcb46f6913","RL-02:da32d82e0790391df7de262cab00df2c0a32e1008ca37227824ae083f1b85aaf","RL-03:295c8410b1d919a2cbb7c2d13a5896e6a36c76be4e37073ee72e149d81b717cd","RL-04:93d96b38d4f0e36ab8baab7e8d69b654abe6797005bafaaa02fa533c5631d8af","RL-05:eff9ea75626eb283d7d3919329cc6890211d137ec747c1bc2813a6b4c5acc79f","RL-06:37244a9ee40ae7dad0bdd66e94b6f088773f9ca26c594aa9791316d2379d10af","RL-07:cb265f2b5471f2417b0a40e27f75b11f1f638bbfc597c483546cd273e3dba3c1"]}},"frozen_pre_output_receipt_sha256":"f415957d3acf34dc072f7bba5e8758a2c240b047c76a9fa0abc176bc8111e171","replay_entry_point_sha256":"7683259aa41b310bab781e74f805e06ff73c4e38c33da2f8f7b1f23fb7507f4e","restriction_and_limit_square_receipts":["RL-01:9c8a59013b4fca4f50dbe6371326532b5b1757a785ebf31a32df18dcb46f6913","RL-02:da32d82e0790391df7de262cab00df2c0a32e1008ca37227824ae083f1b85aaf","RL-03:295c8410b1d919a2cbb7c2d13a5896e6a36c76be4e37073ee72e149d81b717cd","RL-04:93d96b38d4f0e36ab8baab7e8d69b654abe6797005bafaaa02fa533c5631d8af","RL-05:eff9ea75626eb283d7d3919329cc6890211d137ec747c1bc2813a6b4c5acc79f","RL-06:37244a9ee40ae7dad0bdd66e94b6f088773f9ca26c594aa9791316d2379d10af","RL-07:cb265f2b5471f2417b0a40e27f75b11f1f638bbfc597c483546cd273e3dba3c1"],"schema":"rd22.axn-joint-anchor-certificate-suite.v001","suite_sha256":"d20ae8d983f7002656392e91b6d094b2ff561863a3dddd76a43084e188e0bc24"}
```

```text
SUITE_SHA256                     = d20ae8d983f7002656392e91b6d094b2ff561863a3dddd76a43084e188e0bc24
FROZEN_PRE_OUTPUT_RECEIPT_SHA256 = f415957d3acf34dc072f7bba5e8758a2c240b047c76a9fa0abc176bc8111e171
```

## 4. Step 8 run on the final object [PROVABLE — PASS]

The relay requires the procedure to pass its own validation. Run, output displayed:

```text
8a exact key sets              PASS      (outer 9/9, BOUNDED_CLASS 8/8, for_class 8/8)
8b value types                 PASS      (five typed digests + two class digests + eight family
                                          digests all lowercase 64-hex; both list receivers are lists)
8c const fields byte-exact     PASS      (schema, escape_text, canonical_serialization)
8d exactly one variant         PASS      (['BOUNDED_CLASS'])
8e canonical form              PASS      (sorted keys, compact separators, ensure_ascii, no terminal LF)

STEP 8 RESULT: PASS
```

Steps 1-7 re-run alongside it, all PASS: the receipts list and root, `outer_receipts_identity`
byte-wise, `suite_sha256` over stage-0, the freeze receipt over stage-1, and
`replay_entry_point_sha256` equal to the new object's own digest — **the object points at the
procedure that validates it, and the pointer resolves.**

**One checker correction, mine.** My first pass expected 6 fields for the replay tuple and flagged 7.
The tuple is `JAC14-REPLAY-ENTRY|v=001|id|scope|procedure|determinism|accept` — **7 by design**, so the
payload was right and my expectation was wrong. Same shape as the CERT-A false alarm I corrected at
969: a checker with an unverified expectation reports defects that are not there.

## 5. FREEDOMS-CONSUMED

```text
JOINT_ANCHOR_INPUT = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  the whole 971 suite content, the eight families, and both certificate bodies -- byte-carried;
  the digest convention, now accepted of record by the check.

AUTHORED HERE, AND ONLY THIS:
  step 8 and its five validation classes.

SUBSTITUTED:
  NOTHING.  No schema field, key name, variant, basis, matrix, or candidate selection.

SCALING WEIGHTS: NONE CONSUMED; NONE FIXED; NONE SUBSTITUTED.
```

## 6. Flattening, custody, byte audit

- **S01-S37 FLATTENING CHECK:** walked. Digest re-verification was not identified with schema
  validation — that gap is exactly what step 8 closes (§1). A carried receipt was not identified with a
  performed freeze (§2). Unchanged byte counts were not identified with an un-recomputed cascade (§2).
  A checker's expectation was not identified with the schema's requirement (§4).
- **F_PLDEC:** digests and canonical serialization only. No physical quantity evaluated.
- **DIGEST PROVENANCE:** the relay supplied both subject digests **in full**; both were verified in
  full. Nothing was completed from a prefix.
- **BLIND:** held. The A0 fiber remains a digest copy; nothing rank-shaped opened.
- **PE-1..PE-15:** pointer-only, zero verdict weight.
- **BUILDER-NEVER-VERIFIES:** all objects **CLAIMED**. Press §4 first — a self-validating procedure is
  only as good as the independence of the run, and I ran it on my own object.
- **CHAIN:** no anchor act, member binding, fixed-point execution, end test, gauntlet run, numerical
  evaluation, or comparison with a measured constant was invoked.

```text
CLOSURE_BEGIN_BYTE = 0
CLOSURE_END_BYTE = 1944
PREDECLARATION_OUTPUT_SCAN = 0 hits
STEP8 = added, 5 classes ; SELF_VALIDATION = PASS ; CASCADE_STAGES_RECOMPUTED = 7
FREEZE = re-performed pre-output ; UNDECLARED_FIELDS = 0
```

Self verb audit: "added" is used of step 8 and its five classes. "Re-performed" is used of the freeze,
which was recomputed rather than carried. "PASS" is used of a run whose output is displayed in full.
One checker error is stated as mine in §4. `VERB_AUDIT_SELF = CLEAN`.

## 7. Final lines

```text
CLOSURE = declared-first (byte position 0, closure end 1944; scan 0 hits)
STEP8 = ADDED (validation classes enumerated): 8a exact key sets at all three levels with zero missing, extra or renamed; 8b value types, lowercase 64-hex where typed and LIST where a list receiver is typed; 8c const fields byte-exact -- schema, escape_text, canonical_serialization; 8d EXACTLY ONE inventory variant; 8e canonical-form conformance. THESE ARE THE FAILURE MODES THIS BUILD ACTUALLY HIT, made mechanical: 8a is the 969 wrapper's invented key names and 8b is its collapse of both receipt receivers to a root. The gap the check found was real -- a replay that recomputes every hash of a STRUCTURALLY WRONG object still returns PASS, and steps 1-7 could not have caught that
CASCADE = DISPLAYED (each digest old/new), recomputed strictly in order: replay-entry object 745 -> 1240 B with digest c66c349a71052770... -> 7683259aa41b310b...; the suite's replay_entry_point_sha256 tracking it; stage-0 -> suite_sha256 dec168f2254712e8... -> d20ae8d983f70026...; stage-1 -> freeze receipt 0aef54371edbe0dc... -> f415957d3acf34dc...; final bytes 3258; CERT-IF a30ca4a7970e35fb... -> 381e3f85c5199dc5...; CERT-A 65d825d7aaa76ddc... -> 56610e0d7de18997... . THE STAGE BYTE COUNTS ARE UNCHANGED BECAUSE A 64-HEX DIGEST REPLACED A 64-HEX DIGEST -- only the values moved -- and I state that rather than let equal numbers look like an un-recomputed cascade
FREEZE = RE-PERFORMED-PRE-OUTPUT. The old receipt covered the old bytes; carrying it across a byte change would certify a freeze that never happened. No gauntlet output exists, so re-performing is lawful and is the only honest option
SELF_VALIDATION = STEP8-RUN-ON-FINAL: PASS (output shown). All five classes pass, and steps 1-7 re-run alongside also pass -- including replay_entry_point_sha256 equalling the new object's own digest, so THE OBJECT POINTS AT THE PROCEDURE THAT VALIDATES IT AND THE POINTER RESOLVES. ONE CHECKER CORRECTION, MINE: my first pass expected 6 fields for the replay tuple and flagged 7, but the tuple is 7 by design, so the payload was right and my expectation was wrong -- the same shape as the CERT-A false alarm I corrected at 969, and a reminder that a checker with an unverified expectation reports defects that are not there
CERTS = REBOUND (CERT-IF 381e3f85c5199dc5..., 956 B; CERT-A 56610e0d7de18997..., 950 B; both outside the suite, both at 8 fields, both instantiating the new staged identity)
CARRIED = VERIFIED (the entire 971 suite content, the eight families and both certificate bodies byte-carried; only step 8 and the cascaded digests moved)
BLIND = HELD (the A0 fiber remains a digest copy; nothing rank-shaped opened)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
