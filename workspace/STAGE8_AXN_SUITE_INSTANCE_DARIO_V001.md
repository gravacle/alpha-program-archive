CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = DECLARED-FIRST
CLOSURE_BEGIN_BYTE = 00000000
PREDECLARATION_REGION = EMPTY (closure opens at byte 0; no text precedes it)
PREDECLARATION_OUTPUT_SCAN = 0 hits in authored prose (27-token sweep)
VERDICT_BEARING_SET = exactly the 6 content-addressed members below
UNDECLARED_SEARCH_SURFACE_VERDICT_WEIGHT = forbidden
LANE = DARIO   ROLE_THIS_RELAY = BUILDER (not verifier)
ALL_OBJECTS = CLAIMED until the opposite-lane check
SEAL_DISCIPLINE = tuple-parse replay + numeral grep + FIELD-BY-FIELD SCHEMA DIFF, all run below
```

| # | Closed member | SHA-256 | Role |
|---:|---|---|---|
| 01 | `relay_inbox/RELAY_PASTE_971_SUITE_INSTANCE_DARIO_V001.md` | `cf44dc200fe583990ac6ff37fae7ffcd5674d2032b43e9aa1f4157cc6a10b1e1` | assignment |
| 02 | `STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V004.md` | `a195edb03b36be44bf8ce1b71dbf1a01a3a0956c4afc65ddf17382cdca4ed0ab` | the **governing** closed schema and the §5.1.1 instantiation template |
| 03 | `STAGE8_AXN_FOR_CLASS_FAMILIES_DARIO_V004.md` | `28bc43a0a8e841f11d382a11d83634938f5eab0b94fe0f59737b290dbc1d6222` | my 969 — the eight families and two certificates, byte-carried |
| 04 | `STAGE8_AXN_FAMILIES_V004_CROSSCHECK_CODEX2_V001.md` | `3cb349ea0d945d21c3f49d04ab9636f2cf1c6302c761bb58ddf3d2c3c0499eec` | the check whose finding 3 lists the wrapper items |
| 05 | `STAGE8_AXN_STAGE_RULE_CONSTRUCTION_CODEX2_V002.md` | `f450b0a356b249509fb59b897c4f6a14e6996ba7da5ea513e69112a89907eed9` | the seven receipts and their ordered root, re-derived here |
| 06 | `JOINT_ANCHOR_DECISION_INSTANCE_V003.md`; `PROGRAM_STATE_BRIEF_V005.md`; `LOCKED_PROCESS.md`; `DECLINE_REGISTER_V002.md` | `089af246cbc0d66e6ce70971dbb14d355a78ee0f5e294706a1acaeacd0d4236d`; `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c`; `38149496a2b5d89d20b614d972bffef1867d7cde573b26d77dfb207ece3446fb`; `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a` | the entered carrier and fiber; state pin, process law, S01-S37 |

```text
BLIND HELD: the A0 fiber enters as a digest copy; every rank-shaped object stays closed.
BASIS INDEPENDENCE PRESERVED.  THE FAMILIES AND CERTIFICATES ARE BYTE-CARRIED FROM 969.
```

CLOSURE_DECLARATION_END

# STAGE 8 — AXN JOINT-ANCHOR CERTIFICATE SUITE INSTANCE — DARIO LANE — V001
## RELAY 971 — `[PLAN:AXN-BUILD-D70]` — THE LAST OBJECT, AT EXACT SCHEMA

Date: 2026-08-10
Status: **THE SUITE IS INSTANTIATED FIELD-EXACT. Schema diff 0/0/0; both lists enumerated and bound
by identity; the replay entry point built and sealed; the two-stage digest convention displayed; the
pre-output freeze performed. CLAIMED.**

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1. What my 969 wrapper got wrong

Three things, all packaging, all mine: I named the eight members `fc_01..` instead of **their schema
names**; I collapsed both receipt receivers to a **root digest** instead of **enumerated lists**; and
I put `cert_if_joint_sha256` and `cert_a_joint_sha256` **inside** the suite as undeclared fields. The
schema diff in §5 is the discipline that would have caught all three, and it is now part of my seal.

I also pointed `bounded_class_definition` and `explicit_reopening_trigger` at the **candidate
grammar**. Read at V004 §5.1.1, the template points them at the **stage-rule ground and the sealed
reopening predicate** — a different object. Corrected.

## 2. The replay entry point, built as part of this act [PROVABLE]

No sealed replay-entry object existed, so the relay authorises building one. It is a deterministic
procedure over the suite's own members — no clock, no randomness, no network:

```text
JAC14-REPLAY-ENTRY|v=001|id=SUITE-REPLAY-ENTRY|scope=JointAnchorCertificateSuite.v001|procedure=1-re-parse-every-closed-tuple-at-its-declared-field-count;2-recompute-each-for_class-member-digest-from-its-displayed-payload-bytes;3-recompute-each-of-the-seven-universal-receipt-digests-and-their-ordered-root;4-verify-outer_receipts_identity-as-byte-and-digest-equality-between-the-two-list-receivers;5-verify-every-content-addressed-ground-resolves-to-its-sealed-source;6-recompute-suite_sha256-under-the-displayed-two-stage-convention;7-recompute-frozen_pre_output_receipt_sha256-over-the-suite-completed-through-step-6|determinism=byte-exact-and-order-fixed-no-clock-no-randomness-no-network|accept=every-recomputation-equals-its-recorded-value
```

```text
REPLAY_ENTRY_POINT_SHA256 = c66c349a710527704f851539940c48a966144c72714d42f4da67bb0d11602d3e   (745 B)
```

## 3. The self-reference convention, read and displayed [PROVABLE]

**The schema states no convention.** It types `suite_sha256: lowercase_sha256` and
`frozen_pre_output_receipt_sha256: lowercase_sha256` and says nothing about what bytes each covers.
A field cannot contain the digest of bytes that include itself, so a convention must be supplied —
and I display mine rather than assume it:

```text
STAGE 0  canonical suite with BOTH digest fields omitted        3074 B
         suite_sha256 := sha256(stage-0 bytes)                  dec168f2254712e8...
STAGE 1  canonical suite with suite_sha256 inserted             3156 B
         frozen_pre_output_receipt_sha256 := sha256(stage-1)    0aef54371edbe0dc...
FINAL    canonical suite with both inserted                     3258 B
```

Each digest is taken over **strictly earlier** bytes, so the construction is non-circular and exactly
replayable. This is the only reading under which both fields can be filled at all; if the registrar
means a different one, the object rebuilds mechanically from step 0.

**Gate 3 is satisfied the only lawful way — by completing the object first.** The freeze receipt is
sealed over the completed suite bytes, before any gauntlet output exists. At 969 I left this field
absent precisely because the suite was incomplete; completing the suite is what makes filling it
honest rather than manufactured.

## 4. The suite instance

```json
{"a0_rank_fiber_sha256":"5eaa8277097121cbe6fcfefc7fa2d0ac2b74c48f983a033ff40102a3549afe46","canonical_serialization":"canonical bytes; closed fields; no extras","carrier_sha256":"1467ab9850022931e68dc9ffa625d95099d8f6bb74d734dc9d0466f169bd00b6","finite_stage_inventory":{"BOUNDED_CLASS":{"bounded_class_definition":"positive-integers-N>=1-with-unique-arrow-N-to-M-iff-N<=M","escape_text":"or state a bounded class and explicit reopening trigger","explicit_reopening_trigger":"reopen on any byte change to the stage-rule ground, N>=1 class or arrows, receipt payload/list/order/root, outer-receipts identity, certificate receiver semantics, or on failure of any universal replay","for_class":{"anchor_certificate_family":"f743aee3ce8cc616f35ad33029896bf6c65fc92f356209b01957ae34e446f0e1","charge_covariance_certificate_family":"65aedce4c423b427adea9dfca8099223c600b637991adb4e07e30506340dd634","cptp_certificate_family":"b07339b7599fdc2e05f41815f77c9e6e9340a57d35396f7ad75286a835d453fb","delta0_basis_family":"8215042bb8e60b15a310b1c8a4438015ee55039312a4ccc7f6a450a566463d3e","factorization_and_inverse_family":"06233b1d5771903af2d5a723bb9d6e1fc9170467d1d7f2b129087a999350ca38","fixed_space_and_mixing_certificate_family":"5b939147f0779f787a4f4cc5250372d83610a0112561060ddbfd23a9834cf03f","phi_restriction_matrix_family":"8bb6080205f6451cb6b5fc9852711ddf9f5431aaf7987fbee05ecf078548a7ad","superselection_commutation_certificate_family":"03698d14572cc91914bc5f4f7346bdedd9fc2f61f9bdef59daeeed34382dad5b"},"ordered_receipt_root_sha256":"9451020e12f72fe5ede31a7e75692e784c559a3854981db00105657d9d6bdb41","outer_receipts_identity":"exact same ordered receipt bytes and root as restriction_and_limit_square_receipts","stage_rule_ground_sha256":"42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269","universal_restriction_and_limit_square_receipts":["RL-01:9c8a59013b4fca4f50dbe6371326532b5b1757a785ebf31a32df18dcb46f6913","RL-02:da32d82e0790391df7de262cab00df2c0a32e1008ca37227824ae083f1b85aaf","RL-03:295c8410b1d919a2cbb7c2d13a5896e6a36c76be4e37073ee72e149d81b717cd","RL-04:93d96b38d4f0e36ab8baab7e8d69b654abe6797005bafaaa02fa533c5631d8af","RL-05:eff9ea75626eb283d7d3919329cc6890211d137ec747c1bc2813a6b4c5acc79f","RL-06:37244a9ee40ae7dad0bdd66e94b6f088773f9ca26c594aa9791316d2379d10af","RL-07:cb265f2b5471f2417b0a40e27f75b11f1f638bbfc597c483546cd273e3dba3c1"]}},"frozen_pre_output_receipt_sha256":"0aef54371edbe0dccff332d190e72cabe6b99192289ffb835e9131b0043dd048","replay_entry_point_sha256":"c66c349a710527704f851539940c48a966144c72714d42f4da67bb0d11602d3e","restriction_and_limit_square_receipts":["RL-01:9c8a59013b4fca4f50dbe6371326532b5b1757a785ebf31a32df18dcb46f6913","RL-02:da32d82e0790391df7de262cab00df2c0a32e1008ca37227824ae083f1b85aaf","RL-03:295c8410b1d919a2cbb7c2d13a5896e6a36c76be4e37073ee72e149d81b717cd","RL-04:93d96b38d4f0e36ab8baab7e8d69b654abe6797005bafaaa02fa533c5631d8af","RL-05:eff9ea75626eb283d7d3919329cc6890211d137ec747c1bc2813a6b4c5acc79f","RL-06:37244a9ee40ae7dad0bdd66e94b6f088773f9ca26c594aa9791316d2379d10af","RL-07:cb265f2b5471f2417b0a40e27f75b11f1f638bbfc597c483546cd273e3dba3c1"],"schema":"rd22.axn-joint-anchor-certificate-suite.v001","suite_sha256":"dec168f2254712e8cfe3f0364096e67d5c6a0d9acc3e20fcc7b4ba67c13e72b2"}
```

```text
SUITE_SHA256                     = dec168f2254712e8cfe3f0364096e67d5c6a0d9acc3e20fcc7b4ba67c13e72b2
FROZEN_PRE_OUTPUT_RECEIPT_SHA256 = 0aef54371edbe0dccff332d190e72cabe6b99192289ffb835e9131b0043dd048
FINAL SUITE BYTES                = 3258
```

## 5. The field-by-field schema diff [PROVABLE — FIELD-EXACT]

Run against the closed schema at V004's own bytes, level by level:

```text
outer           schema  9 | instance  9 | missing none | extra none
BOUNDED_CLASS   schema  8 | instance  8 | missing none | extra none
for_class       schema  8 | instance  8 | missing none | extra none

SCHEMA_DIFF = FIELD-EXACT (0 missing / 0 extra / 0 renamed)
finite_stage_inventory carries EXACTLY ONE variant: ['BOUNDED_CLASS']
cert_if_joint_sha256 present: False    cert_a_joint_sha256 present: False
```

The eight members appear under **their schema names** — `delta0_basis_family`,
`phi_restriction_matrix_family`, `factorization_and_inverse_family`, `cptp_certificate_family`,
`charge_covariance_certificate_family`, `superselection_commutation_certificate_family`,
`fixed_space_and_mixing_certificate_family`, `anchor_certificate_family` — not `fc_01..`.

**A note on how I ran this, because my first attempt was wrong.** My initial extractor sliced the
schema by assumed indentation and reported 43 discrepancies. Those were an artifact of the extractor,
not the suite: the schema sits inside a fence at a different base indent. I re-derived the levels from
the block itself and re-ran. **A diff tool that has not been checked against a known-good case can
manufacture defects as easily as it can miss them**, and I would not have shipped the first number.

## 6. Both lists, enumerated and bound [PROVABLE]

```text
universal_restriction_and_limit_square_receipts : 7 entries, content-addressed RL-01..RL-07
restriction_and_limit_square_receipts           : 7 entries, same
outer_receipts_identity holds byte-wise         : True
```

The seven digests were **re-derived here** from the receipt payloads in member 05, not copied from
memory. Both receivers carry the same enumerated list, and the identity field states the binding — so
the outer receiver is separately present rather than filled by category substitution, which is the
distinction my own 952 ruling turned on.

## 7. The two certificates, rebound to the final digest [PROVABLE]

They live **outside** the suite and instantiate it by reference, per JAC-14's aligned row:

```text
JAC14-CERT|v=002|id=CERT-IF-JOINT|instantiates=JointAnchorCertificateSuite.v001@dec168f2254712e8cfe3f0364096e67d5c6a0d9acc3e20fcc7b4ba67c13e72b2|quantifier=JOINTLY-TOTAL-over-(N>=1)x(Phi_joint-in-G_joint)|inputs=FC-01;FC-02;FC-03;DELTA0-DEF@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13565,13639)#bb73a8ec8816bddc9c84d84e48ca81bd8d315f316092cdf295dc8fb474e2826f;G-GRAMMAR@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13731,14294)#105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f|procedure=exhibit-input-faithfulness-ker(Phi_joint-restricted-to-Delta_0,N)-equal-zero-by-LEMMA-B=injectivity-restricts-since-Delta_0,N-subset-Delta_0-forces-ker(Phi-restricted-to-Delta_0,N)-subset-ker(Phi-restricted-to-Delta_0)-equal-zero-by-predicate-5-and-replay-it-on-the-FC-01-witness-at-arbitrary-N|accept=Cert_IF_joint(Phi_joint)-is-an-exact-replayable-certificate-for-every-N>=1-and-every-Phi_joint-in-G_joint
```

```text
JAC14-CERT|v=002|id=CERT-A-JOINT-BI|instantiates=JointAnchorCertificateSuite.v001@dec168f2254712e8cfe3f0364096e67d5c6a0d9acc3e20fcc7b4ba67c13e72b2|quantifier=JOINTLY-TOTAL-over-(N>=1)x(Phi_joint-in-G_joint)|inputs=FC-08;BI-TAG@089af246cbc0d66e6ce70971dbb14d355a78ee0f5e294706a1acaeacd0d4236d:[7250,7299)#9a42dac44da482d07f186040d6e62edb85c23c0c886858a14ba8ce63e0d3a72c;BI-CONTENT@089af246cbc0d66e6ce70971dbb14d355a78ee0f5e294706a1acaeacd0d4236d:[7300,7469)#19585bb3d660895ca65f1c52b0d97903f96257ec02ec5fd4b21b3b26a2146d38;G-GRAMMAR@79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e:[13731,14294)#105f8d5ce972eb122b5c73c26530c63f49d6ec480277e7c226ad8d4e001a187f|procedure=exhibit-the-entered-tag-A-equal-BI-at-the-instance-bytes-and-replay-the-entered-BI-equations-on-the-stage-unit-witness-at-arbitrary-N|accept=Cert_A_joint(Phi_joint)-is-exact-and-replayable-for-every-N>=1-and-every-Phi_joint-in-G_joint-with-the-tag-class-exactly-BI
```

```text
CERT-IF  956 B  fields 8  a30ca4a7970e35fb496d328314dc070c54ebe17e9575456f3222347ff6c6b42c
CERT-A   950 B  fields 8  65d825d7aaa76ddc071b15f51bfb6c66714f6c3d7c23fcf04ccf3fe86296d658
```

## 8. FREEDOMS-CONSUMED

```text
JOINT_ANCHOR_INPUT = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  the eight families and two certificates from 969, byte-carried;
  the V004 closed schema and its §5.1.1 instantiation template;
  the seven receipts and ordered root; the entered carrier and A0 fiber digest.

AUTHORED HERE, AND ONLY THIS:
  the replay entry-point procedure object, which the relay authorises building;
  the two-stage digest convention, displayed in §3 because the schema states none.

SUBSTITUTED:
  NOTHING.  No basis, matrix, coordinate, candidate selection, invented field, or invented path.

SCALING WEIGHTS: NONE CONSUMED; NONE FIXED; NONE SUBSTITUTED.
```

## 9. Flattening, custody, byte audit

- **S01-S37 FLATTENING CHECK:** walked. A convenient key name was not identified with the schema's own
  (§1). A root digest was not identified with an enumerated list (§6). A certificate was not identified
  with a suite field (§5). A supplied convention was not identified with a stated one (§3). **And a
  diff tool's output was not identified with a finding (§5).**
- **F_PLDEC:** digests and canonical serialization only. No physical quantity evaluated.
- **BLIND:** held. The A0 fiber is a digest copy; nothing rank-shaped is opened.
- **PE-1..PE-15:** pointer-only, zero verdict weight.
- **BUILDER-NEVER-VERIFIES:** every object **CLAIMED**. Press §3's convention first — if the registrar
  reads the self-reference differently, both digests move and the object rebuilds from stage 0.
- **DIGEST PROVENANCE, a recurrence I record rather than bury.** My first draft pinned member 04 by
  completing the relay's truncated  with sixteen invented bytes — the same slip I
  caught and corrected at 969. I caught it again in the same pre-seal check and replaced it with the
  computed digest. Twice is a pattern, not an accident: **a truncated digest in a relay is a prefix to
  verify against, never a stem to complete.** Every pinned digest in this artifact was computed from
  the file.
- **CHAIN:** no anchor act, member binding, fixed-point execution, end test, gauntlet run, numerical
  evaluation, or comparison with a measured constant was invoked.

```text
CLOSURE_BEGIN_BYTE = 0
CLOSURE_END_BYTE = 2228
PREDECLARATION_OUTPUT_SCAN = 0 hits
SCHEMA_DIFF = 0/0/0 ; LISTS = 7 and 7, identity true ; UNDECLARED_FIELDS = 0
SUITE_BYTES = 3258 ; TUPLES_REPARSED = 3/3 at 8 fields
```

Self verb audit: "field-exact" is used of the schema diff, re-run after my first extractor proved
faulty and reported the correction rather than the first number. "Displayed" is used of the digest
convention, which I supply because the schema states none. "Built" is used of the replay entry point,
which the relay authorises. Three packaging errors in §1 are stated as mine, and a fourth is recorded in §9: I completed a truncated member digest from nowhere for the second relay running, caught it in the same pre-seal check both times, and corrected it before sealing. `VERB_AUDIT_SELF = CLEAN`.

## 10. Final lines

```text
CLOSURE = declared-first (byte position 0, closure end 2228; scan 0 hits)
SCHEMA_DIFF = FIELD-EXACT (0 missing / 0 extra / 0 renamed) at all three levels -- outer 9/9, BOUNDED_CLASS 8/8, for_class 8/8 -- with finite_stage_inventory carrying exactly one variant and the eight members under THEIR SCHEMA NAMES rather than fc_01... MY 969 WRAPPER GOT THREE THINGS WRONG, ALL MINE: invented key names, both receipt receivers collapsed to a root instead of lists, and the two certificates placed INSIDE the suite as undeclared fields. A NOTE ON THE DIFF ITSELF: my first extractor sliced the schema by assumed indentation and reported 43 discrepancies, which were an artifact of the extractor rather than the suite; I re-derived the levels from the block and re-ran. A diff tool unchecked against a known-good case can manufacture defects as easily as miss them, and I did not ship the first number
LISTS = BOTH-ENUMERATED (identity bound): universal_restriction_and_limit_square_receipts and restriction_and_limit_square_receipts each carry the seven content-addressed receipts RL-01..RL-07, RE-DERIVED HERE from their payloads rather than copied, with outer_receipts_identity holding byte-wise -- so the outer receiver is separately present rather than filled by category substitution, the distinction my own 952 ruling turned on
POINTERS = STAGE-GROUND+PREDICATE (not the grammar). bounded_class_definition is the N>=1 stage class with its unique arrows and explicit_reopening_trigger is the sealed reopening predicate, both per V004's §5.1.1 template; my 969 had pointed them at the candidate grammar, which is a different object
REPLAY_ENTRY = BOUND (object sealed). No sealed entry point existed, so one was built as the relay authorises: a seven-step deterministic procedure re-parsing every tuple at its declared count, recomputing every member digest, the receipts and root, the outer-receipts identity, every content-addressed ground, and both digests under the displayed convention -- byte-exact, order-fixed, no clock, no randomness, no network. 745 B, c66c349a71052770...
SUITE_SHA = COMPUTED-OVER-COMPLETE (convention shown). THE SCHEMA STATES NO CONVENTION, and a field cannot contain the digest of bytes including itself, so I supply and DISPLAY one rather than assume it: stage 0 is the canonical suite with both digest fields omitted (3074 B) giving suite_sha256 = dec168f2254712e8...; stage 1 inserts it (3156 B) giving the freeze receipt; the final object is 3258 B. Each digest covers STRICTLY EARLIER bytes, so the construction is non-circular and exactly replayable, and if the registrar reads the self-reference differently the object rebuilds mechanically from stage 0
FREEZE_RECEIPT = SEALED-PRE-OUTPUT (0aef54371edbe0dc..., sealed over the completed suite bytes before any gauntlet output exists). GATE 3 IS SATISFIED THE ONLY LAWFUL WAY -- BY COMPLETING THE OBJECT FIRST. At 969 I left this field absent precisely because the suite was incomplete; completing the suite is what makes filling it honest rather than manufactured
CERTS = REBOUND-TO-FINAL-DIGEST (CERT-IF a30ca4a7970e35fb, 956 B; CERT-A 65d825d7aaa76ddc, 950 B; both OUTSIDE the suite, instantiating it by its final digest per JAC-14's aligned row, both parsing at 8 fields)
CARRIED = VERIFIED (the eight families and the two certificate bodies byte-carried from 969; only the wrapper and the certificates' instantiates field moved)
BLIND = HELD (the A0 fiber enters as a digest copy; nothing rank-shaped opened)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
