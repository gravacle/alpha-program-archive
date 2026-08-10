CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = CLAIMED
CLOSURE_BEGIN_BYTE = 0000000000
CLOSURE_END_BYTE = 0000002553
PREDECLARATION_OUTPUT_SCAN = 0 hits for this artifact and its sidecar
READ_SET = exactly the nine content-addressed members below
UNDECLARED_SOURCE_VERDICT_WEIGHT = forbidden
JOINT_ANCHOR_INPUT = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false
```

| # | Closed member | SHA-256 / bounded span SHA-256 | Role |
|---:|---|---|---|
| 01 | `relay_inbox/RELAY_PASTE_923_GAUNTLET_RUN_CODEX2_V001.md` | `b646c47e3db32941571d6d2ab66b8bf482ed691f8de226c85d337f8f99f77948` | assignment |
| 02 | `PROGRAM_STATE_BRIEF_V005.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c` | state pin |
| 03 | `LOCKED_PROCESS.md` | `38149496a2b5d89d20b614d972bffef1867d7cde573b26d77dfb207ece3446fb` | process law |
| 04 | `DECLINE_REGISTER_V002.md` | `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a` | S01–S37 flattening guard |
| 05 | `QUESTIONS_SETTLED_REGISTER_V001.md` | `a527cd538f53570099b0a8f59d1c5b768f647bffbdf0b33d0949da318934cc9d` | required question-index check; no later entry supplies a run input |
| 06 | `JOINT_ANCHOR_DECISION_OF_RECORD_V001.md` | `f0179d43b4b2ed89f4cfb9adc1daa8c7cc0c9c5f038e3bbe7332727fdddaaa8f`; field block `[241,1113)` = `31b88440590d7da33fcb99151899963f761bc80b9c84f4dcdef87aa43076132a` | executed decision under test |
| 07 | `JOINT_ANCHOR_CERTIFICATE_MANIFEST_V001.md` | `589c12f7cb76b5f4a2ba895d5942061ec3d801d6983f656304b172bfde964b27`; entry block `[1636,2206)` = `b72cb7abc0794d32dc9edf3cd207597e01d7e2b9b694f7402d8fc13beb300a9c` | certificate commitment under test |
| 08 | `STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V002.md` | `58b966ed371b23b29b9e3ceed280eb30c804484becb2b17ca6ea465668e951bc` | governing G0–G8 instrument |
| 09 | `STAGE8_TASK4A_ORIGIN_FED_REFINEMENT_TOWER_GENOMEGA_PORT_TYPECHECK_DETERMINATION_CODEX_LANE2_V001.md` | whole file `4e00c7edbec105cd9c60cba483f11c1888a541e5963f3c1168fc6d00085669b0`; `[738,989)` = `9bcee6a4472597fecaebd445dbadce9d8265274ce44f60abe256d5803ab7cf38`; `[8215,9375)` = `da6a9e94797d8e126e89ba0e7bf86c91a11147432af31f11a1fb5a1ea3029a7c` | instrument-pinned source/fiber formula and fixed-fiber theorem |

Every whole-file member and available sidecar verified before use. The decision sidecar itself hashes
to `6abd5f1416c15d88e2e1f42b225527446e454cc76c422d05de6e0da295d4c1ad`.
An earlier ACK was viewed only as a custody-format template and carries zero premise, citation,
inference, or verdict weight.

CLOSURE_DECLARATION_END

# STAGE 8 — AXN JOINT-ANCHOR GAUNTLET RUN — CODEX 2 V001 [CLAIMED]

Date: 2026-08-10  
Scope: fail-closed execution of the adopted joint-anchor packet against the sealed V002 instrument.  
Status: **REJECTED AT G0; ORDERED STOP**. The anchor remains **ADOPTED-AND-FROZEN, NOT DERIVED**.
Every run verdict below is **CLAIMED** until the opposite lane cross-checks this run.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member_binding = false
fixed_point_execution = false
end_test = false
physical_numeric_evaluation = false
measured_constant_comparison = false
```

## 1. Instrument-exact stage map [CLAIMED]

The governing bytes control the stage names. They assign G2 to the anchor theorem and certificate
replay, G3 to SM-1..SM-8, G4 to `res_B`, G5 to K1..K3, G6 to K4, and G7 to K5..K7. The relay's
compressed stage gloss shifts G2–G4 by one and omits the instrument's G2 receiver. No stage was
renamed or weakened here. Because G0 fails, the difference changes no downstream execution result:
G1–G7 are `NOT_RUN_ORDERED_STOP`; G8 records the terminal stop/mutation guard without advancing the
acceptance run.

## 2. Input and pin verification [CLAIMED]

| Check | Exact observation | Verdict/status |
|---|---|---|
| Decision seal | file digest equals `f0179d43...daaa8f` and its sidecar verifies | `PASS / CLAIMED` |
| Certificate-manifest seal | file digest equals `589c12f7...b27` and its sidecar verifies | `PASS / CLAIMED` |
| Instrument seal | file digest equals `58b966ed...951bc` and its sidecar verifies | `PASS / CLAIMED` |
| Instrument pin in decision | exact 64-hex value matches the verified instrument | `PASS / CLAIMED` |
| Manifest pin in decision | exact 64-hex value matches the verified manifest | `PASS / CLAIMED` |
| Disposition | exact value `APPROVE` | `PASS / CLAIMED` |
| Output pre-existence | recursive filename/sidecar scan before write returned zero paths | `PASS / CLAIMED` |

## 3. G0 decision/schema replay [CLAIMED]

### 3.1 Top-level `JointAnchorDecision.v002` fields [CLAIMED]

The procedure parsed only explicit field labels in decision bytes `[241,1113)`. A verified file hash
or a seal sidecar was not inserted into an absent principal field: doing so would be supplementation.

| Required field | Packet observation | Verdict/status |
|---|---|---|
| `schema` | exact `rd22.axn-joint-anchor-decision.v002` | `PASS / CLAIMED` |
| `disposition` | exact `APPROVE` | `PASS / CLAIMED` |
| `decision_artifact_sha256` | no field occurs in the decision | `FAIL / CLAIMED` |
| `decision_time` | declared `2026-08-10` | `PASS / CLAIMED` |
| `governing_instrument_sha256` | present and hash-matched | `PASS / CLAIMED` |
| `scope` | exact required scope | `PASS / CLAIMED` |
| `joint_carrier_entry` | label occurs, but its value is a prose reference, not a `JointCarrierEntry.v002` instance | `FAIL / CLAIMED` |
| `anchor_tag_class_entry` | `{BI}`, a nonempty allowed subset | `PASS / CLAIMED` |
| `anchor_content_entry` | BI equations named; carrier/fiber binding cannot validate without the typed carrier/fiber instance | `FAIL-BINDING / CLAIMED` |
| `certificate_manifest_sha256` | present and hash-matched | `PASS / CLAIMED` |
| `prospective_freeze_receipt_sha256` | no field occurs; the external sidecar is not a lawful backfill | `FAIL / CLAIMED` |
| `supersession_rule` | exact constant present | `PASS / CLAIMED` |
| `post_freeze_mutation` | exact `FORBIDDEN` present | `PASS / CLAIMED` |
| `member_selection` | exact `FORBIDDEN` present | `PASS / CLAIMED` |

The first failure in schema order is `decision_artifact_sha256 = MISSING`. This is the first failed
clause of the complete run.

### 3.2 Required nested carriers [CLAIMED]

The decision supplies descriptions such as “the sealed A_C0 realization” and “the sealed DoR-013
fixed-A0 fiber.” Those are not the closed field inventories the instrument requires. The
instrument-pinned source spans show the symbolic formulas
`rho_S,[A]=I_A/Tr_A(I_A)` and `p_[A]=r_ch/(r_0+r_ch)` plus fixed-fiber neutrality; they do not
instantiate the required content-addressed objects.

| Required object | Closed inventory required by V002 | Packet instance | Verdict/status |
|---|---:|---:|---|
| `JointCarrierEntry.v002` | 14 fields | no structured instance; prose pointer only | `FAIL / CLAIMED` |
| `A0RankFiber.v001` | 8 fields including five content digests and the freeze-receipt digest | no structured instance | `FAIL / CLAIMED` |
| `HistoryPairingControl.v001` | 6 fields including pairing/function digests and exact certificate digest | enum disclosure only: `NEITHER_EQUIVALENCE_PROVED` | `FAIL / CLAIMED` |
| carrier/fiber inventory | exact content-addressed inventory | absent | `FAIL / CLAIMED` |
| candidate grammar and admission predicates | frozen complete scan surface | absent | `FAIL / CLAIMED` |

No path name, word “sealed,” status enum, or already verified outer-file digest was treated as one
of these missing objects. That preserves JAC-01, JAC-05, JAC-10, S05, and S12 rather than flattening
them.

### 3.3 Certificate-manifest census [CLAIMED]

The manifest logically enumerates fourteen commitments: explicit items 1–6, a grouped 7–13 block,
and item 14. Its own bytes say the GAUNTLET certificates are still “to be produced and verified.”
It supplies no `JointAnchorCertificateSuite.v001`, finite-stage inventory, basis, exact matrix,
factorization/inverse, replay entry point, or pre-output suite receipt.

| Manifest item | Manifest state at G0 | Production status |
|---|---|---|
| `M01` target independence; `M02` no supplementation | adoption-time prose commitments | not promoted to exact replay objects |
| `M03` common provenance; `M04` three-marginal square | assigned to gauntlet | `NOT_PRODUCED_G0_STOP` |
| `M05` prospective freeze | adoption-time commitment | external receipt exists, required decision field absent |
| `M06` derivation supersession | standing rule | rule present; no supersession object invoked |
| `M07` finite compatibility; `M08` coverage; `M09` fiber reproduction; `M10` equivalence/naturality; `M11` fixed-space/mixing; `M12` CPTP/charge/superselection; `M13` anchor closure | grouped and assigned to gauntlet | `NOT_PRODUCED_G0_STOP` |
| `M14` exact certificate format | assigned to gauntlet | `NOT_PRODUCED_G0_STOP` |

Creating the missing carrier, fiber, certificate suite, control certificate, or receipt field in
this run would author or supplement an adopted entry after freeze. The run therefore produces zero
manifest-assigned certificates rather than papering over the failure.

## 4. JAC-03 rejection scan and blind-fiber guard [CLAIMED]

The scan surface was exactly the decision field block `[241,1113)` and manifest entry block
`[1636,2206)`. The forbidden set was the instrument's named list: `p_[A]`, `r_0`, `r_ch`, rank
ratio, branch weight, identity-supported Dirac, product Haar, K4–K7, response, coupling, residual,
and measured-target forms.

| Mode | Mechanical result | Verdict/status |
|---|---|---|
| exact fixed-string | 0 hits for every forbidden term | `PASS / CLAIMED` |
| normalized token-name | 0 token-sequence hits; hyphen/underscore/spacing folded | `PASS / CLAIMED` |
| line-wrap and case variants | 0 hits | `PASS / CLAIMED` |
| semantic receiver | no forbidden term receives an entry-selection predicate; `NEITHER_EQUIVALENCE_PROVED` occurs only in the designated pairing disclosure | `PASS / CLAIMED` |
| complete frozen-manifest scan | candidate grammar and admission predicates are not supplied | `FAIL-NOT-REPLAYABLE / CLAIMED` |

Blindness was preserved. The run did not use the visible symbolic ratio, did not select a rank pair,
and did not compare a value to the entry before computing it. Because no content-addressed
`A0RankFiber.v001` supplies the expected source/fiber identity, there is no lawful first computation
and hence no lawful last comparison. The comparison is `NOT_RUN`, not a fabricated match or
mismatch.

## 5. G0 verdict and ordered-stop receipt [CLAIMED]

```text
receipt_schema = rd22.axn-gauntlet-stage-receipt.v001
stage = G0
decision_sha256 = f0179d43b4b2ed89f4cfb9adc1daa8c7cc0c9c5f038e3bbe7332727fdddaaa8f
manifest_sha256 = 589c12f7cb76b5f4a2ba895d5942061ec3d801d6983f656304b172bfde964b27
instrument_sha256 = 58b966ed371b23b29b9e3ceed280eb30c804484becb2b17ca6ea465668e951bc
first_failed_clause = G0.1 JointAnchorDecision.v002.decision_artifact_sha256 MISSING
additional_G0_failures = joint carrier not schema-instantiated;
                         A0 fiber not schema-instantiated;
                         history-pairing control certificate not supplied;
                         prospective_freeze_receipt_sha256 MISSING;
                         complete JAC-03 frozen-manifest surface absent
state_output_exposed = false
post_freeze_mutation = false
verdict = FAIL
status = CLAIMED
```

This receipt is a finite-visible diagnostic of why execution stopped. It is not relabeled as a
JAC-14 certificate and does not satisfy any missing adoption object.

## 6. G1–G8 execution ledger [CLAIMED]

| Stage | Instrument-exact receiver | Result/status | Reason |
|---|---|---|---|
| G0 | decision/pins/approval completeness | `FAIL / CLAIMED` | first failure and complete G0 diagnostic in §5 |
| G1 | seven-item no-go benchmark | `NOT_RUN_ORDERED_STOP / CLAIMED` | G0 did not open G1 |
| G2 | JPO-01..11 plus JAC-01..14 replay and perturbations | `NOT_RUN_ORDERED_STOP / CLAIMED` | no carrier/certificate suite; G0 failed |
| G3 | SM-1..SM-8 | `NOT_RUN_ORDERED_STOP / CLAIMED` | G2 not reached |
| G4 | `res_B(Omega_C0)` | `NOT_RUN_ORDERED_STOP / CLAIMED` | no `Omega_C0`; no state solve |
| G5 | K1..K3 | `NOT_RUN_ORDERED_STOP / CLAIMED` | no generated history member |
| G6 | full-fiber K4 | `NOT_RUN_ORDERED_STOP / CLAIMED` | no generated bases/measures; no fiber comparison |
| G7 | K5..K7 | `NOT_RUN_ORDERED_STOP / CLAIMED` | K4 not reached |
| G8 | terminal stop/mutation guard | `PASS / CLAIMED` | ordered stop recorded; no rerun, mutation, narrowing, swap, line movement, or discard |

G8 is reported as the stop/mutation guard over this failed run, not as advancement past G0. The
adopted anchor remains on the books. No downstream line closes or unblocks.

## 7. Run consequence [CLAIMED]

```text
JOINT_ANCHOR_INPUT = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false
CORE_ACCEPTANCE = FAIL at G0
CORE_LINES_DIRECTLY_CLOSED = 0/5
DEPENDENT_LINES_UNBLOCKED = 0/4
RETROSPECTIVE_REPAIR = forbidden
STATE_OUTPUT = not exposed
```

`REJECTED` is the acceptance-run verdict, not a reversal of the principal's adoption and not a
derivation no-go. A later non-equivalent act remains principal-only; a future same-receiver
derivation remains prospective and equivalence-bound exactly as V002 states.

## 8. FREEDOMS-CONSUMED [CLAIMED]

```text
CARRIED-AS-PARAMETER:
  JointAnchorDecision.v002 disposition APPROVE;
  JOINT_ANCHOR_INPUT = ADOPTED-AND-FROZEN;
  JOINT_ANCHOR_DERIVED = false;
  anchor tag class {BI};
  the decision, manifest, and instrument hashes;
  the V002 fail-closed stage order and stop semantics.

CONDITIONED-ON:
  no downstream acceptance statement unless every preceding instrument stage passes;
  no fiber comparison without a content-addressed A0RankFiber.v001;
  no manifest-assigned certificate credit without its exact replay object.

SUBSTITUTED:
  nothing. Missing decision fields, carrier fields, fiber fields, control-certificate fields,
  candidate predicates, certificate-suite fields, and receipt fields were not backfilled.

SCALING WEIGHTS:
  none consumed, fixed, selected, or evaluated.

DERIVED HERE:
  only the structural G0 schema/pin/scan verdict and the ordered-stop consequence.

FREEDOMS NOT CONSUMED:
  no carrier, fiber, tag member, channel, state, marginal, measure, history member, rank pair,
  ratio, K-test outcome, certificate content, downstream movement, or supersession object was
  chosen, generated, inferred, or repaired.
```

## 9. Flattening, jurisdiction, and batteries [CLAIMED]

- **FLATTENING CHECK:** S01–S37 walked. Load-bearing here: S05 forbids treating named/co-located
  source and record objects as the joint extension; S12 forbids treating status prose, seal status,
  a manifest commitment, or `NEITHER_EQUIVALENCE_PROVED` as the object/certificate it names.
  No decline or conditional grant is reversed.
- **JURISDICTION CHECK:** the run evaluates only packet conformance at the instrument's receivers.
  It neither revises the principal act nor manufactures the absent carriers. The G0 structural
  verdict is within lane jurisdiction and remains CLAIMED pending opposite-lane review.
- **F_PLDEC:** hashes, schemas, symbolic formulas, field presence, and control flow only. No physical
  quantity was numerically evaluated and no measured constant was consulted.
- **M-2:** exact-name, normalized-token, hyphen/spacing/underscore/line-wrap, and semantic-receiver
  modes ran over the bounded entry blocks. The complete-manifest surface is separately and honestly
  `NOT_REPLAYABLE`, not reported as a zero-hit pass.
- **ANTI-TUNING:** no fiber value, state, K-result, or downstream term was used to add or choose an
  input. The first failure was retained even though it prevents an all-pass result.
- **PE-1..PE-13:** pointer-only, zero verdict weight, and not consulted as evidence.
- **BUILDER-NEVER-VERIFIES:** this run applies the lane's sealed instrument to a principal-authored
  decision artifact; it does not cross-confirm its own stage verdicts. Every verdict remains
  CLAIMED for the opposite lane.
- **RULING-LAST:** no principal ruling is requested. The closed packet was checked before the
  fail-closed result was stated.
- **CORRECTION PROPAGATION:** no correction was authored. The affected consumers are named as
  `G1–G8`, all held `NOT_RUN_ORDERED_STOP`.
- **PE-POINTER-ONLY:** satisfied; no expectation statement appears in a proof or verdict receiver.
- **MACHINERY-APPEAL:** not invoked; the structural G0 result is available without crossing a fence.

## 10. Byte-position and verb audit [CLAIMED]

The closure declaration begins at byte 0. The final seal-time audit recomputes its end byte, checks
that the output filename and sidecar had zero predeclaration hits, verifies all nine declared members,
and scans the final artifact for unscoped verdict language. `PASS`, `FAIL`, `REJECTED`, and
`NOT_RUN_ORDERED_STOP` are stage/run verdicts marked CLAIMED. “Adopted” describes the principal's
sealed input; it is never restated as derived. “Produced” is denied for every manifest-assigned
certificate. `VERB_AUDIT_SELF = CLEAN`.

## 11. Final lines [CLAIMED]

```text
CLOSURE = declared-first (byte position 0; scan 0 hits)
G0 = FAIL (JointAnchorDecision.v002 missing decision_artifact_sha256; required nested carriers and prospective_freeze_receipt_sha256 not instantiated)
G1 = NOT_RUN (ordered stop after G0 FAIL)
G2 = NOT_RUN (instrument G2 JPO/JAC replay; ordered stop)
G3 = NOT_RUN (instrument G3 SM-1..SM-8; ordered stop)
G4-G7 = NOT_RUN (K1-K7 and res_B receivers never opened)
G8 = PASS (stop/mutation guard only; no advancement)
FIBER_COMPARISON = NOT_RUN (no lawful A0RankFiber.v001 carrier; no rank or ratio evaluated)
CERTIFICATES_PRODUCED = 0/10 (none; assigned list M03,M04,M07,M08,M09,M10,M11,M12,M13,M14; G0 stopped before production)
RUN_VERDICT = REJECTED (G0)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
