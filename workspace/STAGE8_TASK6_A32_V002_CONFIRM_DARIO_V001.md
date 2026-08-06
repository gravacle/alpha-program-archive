# STAGE 8 / TASK 6 / STEP 1 — BOUNDED CONFIRM: A32 PREP V002 — DARIO V001

Lane: Dario (Claude Opus 5), cross-family review lane
Task: PASTE 602 / Task 6, Step 1
Authority to review: DoR-020-A8. **THIS ARTIFACT RATIFIES NOTHING AND LIFTS NO GATE.**
Custody: bounded confirm of the repair of my own 600 findings; the ratification follows.

```text
REGISTER_HEAD = Q-535
A32_PREP_V002 = CONFIRMED (+1 NOTE, not ratification-blocking)
READY_FOR_RATIFICATION = yes
VERB_AUDIT_SELF = CLEAN
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none of my own
```

**Scope.** Bounded to the repair. I did not re-open the fourteen source hashes,
the 20-obligation extraction, or the mapping rows I already confirmed at 600.

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-535 | verified |
| `STAGE8_TASK6_A32_PREP_LANE3_V002.md` = `c5d1090b1ec1862c59c1281845c9ad74d0b143e9a57f195c099adb16e56ae4ea` | **verified before reading** |
| 956 lines as stated (867 → 956, +89) | verified |
| My 600 review = `d13bcf1fdadc5f70fd6e2d1a854a8d5b103c5756197f8fb039bad3ce08a126fa` | verified — and V002's lead cites it at that hash |
| Output name collision (workspace + cleanroom) | none — clear to write |

---

## H1. THE SIXTEENTH SOURCE'S LANDING — **PASS**

### H1.1 Admitted at its ruled strength

[PROVABLE] `PREREGISTRATION_ENCODING_PRECEDENCE_PRINCIPAL_DECISION_2026-07-29.md`
is now census row **16** at `70c4080eae018bd644a3f0694557f1c0e854d621aa61097c775737887fec528f`,
with its payload read directly rather than summarized:
`:9-19` both encodings and the evaluator; `:25-32` the four structural
differences; `:36-50` `stage_dependencies` authoritative **while preserving every
`stage_dag` non-seal precondition**; `:59-63` creates no seal and authorizes no
computation. `A32_SOURCE_CENSUS = 16_LOAD_BEARING_SOURCES`.

The verb board grades the act *"authoritative/scoping verb used only at its ruled
strength"*, and the artifact states the limit itself: the act *"ranks encodings
already present. It edits no immutable bytes, discharges no A-matrix row, creates
no seal, supplies no missing subject, and authorizes no computation."*

### H1.2 The eleven nodes, re-walked by me

[PROVABLE] I parsed `review_stage_semantics.stage_dependencies` from the sealed
V011 machine encoding directly and compared node-by-node against V002's `(G1)`
display. **All eleven match exactly — every parent list, in insertion order:**

```text
SPEC-SEAL                      <- []                                           MATCH
CORE-RESULT-SEAL               <- [SPEC-SEAL]                                  MATCH
PARENT-COMPARISON              <- [CORE-RESULT-SEAL]                           MATCH
HOLDOUT-UNIVERSE-SEAL          <- [SPEC-SEAL]                                  MATCH
QSPEC-SPEC-SEAL                <- [SPEC-SEAL]                                  MATCH
PREDICTION-MAP-SEAL            <- [HOLDOUT-UNIVERSE-SEAL, QSPEC-SPEC-SEAL]     MATCH
THOMSON-RESULT-SEAL            <- [CORE-RESULT-SEAL, QSPEC-SPEC-SEAL]          MATCH
ALPHA-RESULT-SEAL              <- [THOMSON-RESULT-SEAL, PARENT-COMPARISON,
                                   HOLDOUT-UNIVERSE-SEAL, PREDICTION-MAP-SEAL] MATCH
HOLDOUT-RESULT-SEAL            <- [ALPHA-RESULT-SEAL]                          MATCH
END-TO-END-RECONSTRUCTION-SEAL <- [ALPHA-RESULT-SEAL, HOLDOUT-RESULT-SEAL]     MATCH
FINAL-CLAIM-SEAL               <- [END-TO-END-RECONSTRUCTION-SEAL,
                                   HOLDOUT-RESULT-SEAL]                        MATCH
```

`(G6)`'s alpha stop reproduces the four `ALPHA-RESULT-SEAL` parents exactly, and
`(G5)`'s pre-evaluation rail `SPEC-SEAL -> {HOLDOUT-UNIVERSE-SEAL,
QSPEC-SPEC-SEAL} -> PREDICTION-MAP-SEAL` is precisely the ancestor set of
`PREDICTION-MAP-SEAL` in the authoritative graph — neither short nor padded.

### H1.3 Nothing survives by inheritance — the repair is structural

This was the half of my finding that mattered, and it is closed at the root
rather than by patching two names:

```text
Certified(node) :=
  SealTokenVerified(node)
  and every PreservedNonSealConjunct(node) certified
  and for every p in stage_dependencies[node], Certified(p).   (G3)
```

[PROVABLE] Because `(G3)` quantifies over the parent list of the **authoritative**
encoding, no demoted-prose dependency can survive by abbreviation, and no future
node can inherit a weaker ancestry by being named without its parents. V002 states
the consequence in the exact terms of my defect: *"a child token cannot stand in
for an unnamed or uncertified parent."*

The ruling's preservation clause is honoured too: the descriptive encoding's **24
non-seal terms** are re-bound to their matching authoritative nodes in a displayed
table, and *"Ranking the encodings does not discard A-matrix, Gate,
composition-loop, beacon, Qspec, report, or A33 obligations."* My 600 sub-finding
— that those preconditions were carried as no row — is repaired.

[PROVABLE] `(G4a)` handles the one term that could not simply be carried, and
handles it the right way: the holdout `independent salted commitments` term is
**retained rather than deleted**, with Q-25 bounding what may be certified about
it — cryptographic binding verified, permanent limitation carried, process
independence and independent attestation **not claimed**. V002 names the hazard
itself: *"This is not a weakening by silent reinterpretation."* Deleting the term
(because it cannot be satisfied) or certifying it (because commitments exist) were
both available and both wrong; neither was taken.

---

## H2. (M5a-V002) — **PASS. One hunt run; no remaining weakening found.**

### H2.1 Ruled parents and sequence, exactly per the act

[PROVABLE] Every node in the pre-evaluation rail is named with its ruled parent
list inside the predicate:

```text
evaluator_certified(SPEC-SEAL <- [])
evaluator_certified(HOLDOUT-UNIVERSE-SEAL <- [SPEC-SEAL])
evaluator_certified(QSPEC-SPEC-SEAL <- [SPEC-SEAL])
evaluator_certified(PREDICTION-MAP-SEAL <- [HOLDOUT-UNIVERSE-SEAL, QSPEC-SPEC-SEAL])
```

each with that node's non-seal conjuncts inlined at it, and the sequence `(M5b)`
`SPEC-SEAL -> {HOLDOUT-UNIVERSE-SEAL, QSPEC-SPEC-SEAL} -> PREDICTION-MAP-SEAL`
with the sibling-order freedom correctly stated. The ruling's binding phrase
travels with the sequence and is quoted: **"This act cannot loosen any gate."**

**The eleventh node is correctly excluded from readiness, with its reason
displayed** — *"it depends on `ALPHA-RESULT-SEAL` and `HOLDOUT-RESULT-SEAL`, so
requiring it before evaluation would be circular."* I record this against my own
600 wording: I listed `END-TO-END-RECONSTRUCTION-SEAL` as "absent from the prep
entirely," and a literal repair would have pushed it into `(M5a)`. V002's
treatment — display it in the full ladder, keep it downstream, say why — is more
correct than the repair my phrasing invited.

### H2.2 The conjunct list is complete — checked by mapping V001 forward

[PROVABLE] I mapped each of V001's eight `(M5a)` conjuncts into `(M5a-V002)`:

| V001 conjunct | In V002 |
|---|---|
| `instrument_ratified` | retained |
| `schema_and_canonical_ID_tensions_resolved` | retained |
| `current_scalar_commitment_qualification_carried` | retained as `Q25_current_scalar_commitment_disposition_carried` |
| `executable_eligibility_and_comparator_interfaces_frozen` | **retained** |
| `HOLDOUT-UNIVERSE-SEAL` | retained, now with parent |
| `immutable_all_eligible_ID_prediction_map_code` | retained, `..._before_alpha` |
| `PREDICTION-MAP-SEAL` | retained, now with both parents |
| `every type in (O2) preserved` | retained as `every_type_in_Task6TypedPayload_preserved` |

**All eight survive**, and the predicate adds `SPEC-SEAL`, `QSPEC-SPEC-SEAL`, and
roughly ten non-seal conjuncts. `(M5a-V002)` is strictly stronger than `(M5a)`.

### H2.3 The hunt for a remaining inherited weakening — none found

[YOURS] My best candidate was the classic risk of a rewrite reorganized around a
new axis: that the graph-driven restructuring would drop a **non-graph** conjunct.
I targeted `executable_eligibility_and_comparator_interfaces_frozen`, because it
is the one V001 conjunct with no node in the seal graph to attach to and therefore
the easiest to lose. It is retained verbatim.

I also checked three narrower exposures and found each closed: the pre-evaluation
rail is neither short nor padded against the true ancestor set; `CORE-RESULT-SEAL`
is correctly *outside* readiness (it is a sibling, not an ancestor, of
`PREDICTION-MAP-SEAL`); and `(G6)`'s later parents plus *"their own non-seal
conjuncts"* are expressly kept binding rather than absorbed early.

One formalism nit, recorded and not charged: `(G3)` defines `Certified(node)`
while `(M5a-V002)` invokes `evaluator_certified(node <- parents)`. The two are
bridged in prose — *"The evaluator certifies every conjunct individually under
`(G3)`"* — so the transitivity attaches. A future text could use one symbol.

### H2.4 Nothing manufactured

`(M5c)` books every seal in the rail `false_of_record`,
`instrument_ratified = false`, `A32_PRE_EVALUATION_READY = false`, and the artifact
states *"No predicate in this artifact makes any token in `(G1)` true."* The
necessary/sufficient distinction is drawn correctly: future truth of `(M5a-V002)`
would be *"necessary for the Step-2 conditional scope DoR, not sufficient for
alpha evaluation."*

---

## H3. THE INSTRUMENT'S OPERATIVE TEXT — **PASS**

All checks below are on lines inside the single operative blockquote.

**M9's permanence — present and correctly stated.** *"process independence …
and independent attestation were never established; that permanent limitation
travels with"* every headline, and — the clause that closes the restatement
attack — *"This is permanent carriage, not a condition `(M5a-V002)` resolves."*
The body agrees: M9 *"is a permanent disclosed limitation, not something graph
completion can discharge."*

**P4's J-II identity — present and correctly stated.** The instrument names it:
the bridge *"is the same J-II type-crossing obstruction of record, not a new A32"*
requirement. The mapping row is retyped to carry the identity in its verdict —
**`IN-TENSION — J-II TYPE-CROSSING`** — with *"The exact bridge from `LOCAL-SHADOW`
to the physical alpha-adjacent carrier is the same Q-521/Q-534 J-II object of
record. It is TYPE-U, not supplied by A32."* That is my N2 landed at full
strength, including the point that readiness does not close it.

**The entry-pinned register citation — correct.** Census row 10 now reads
**`LIVE; BY ENTRY ONLY`** with the entries enumerated (Q-05, Q-25, Q-27, Q-28,
Q-521, Q-522, Q-532, Q-534) and *"No whole-file hash is asserted."* The operative
text carries the method itself: citations are by entry *"—never by a whole-file
hash."* This is exactly the repair I proposed at N1, and it is in the gate text
rather than only in the census.

**The four required items — all retained inside the operative text.**

| Carry | Status |
|---|---|
| the number's type | `COMPUTATION_SCOPE = LOCAL` / `PRODUCT_TYPE = LOCAL-SHADOW` / `TRIAL = ONE-SIDED…` / `PERIOD_NATIVE = false`, with the anti-rename clause |
| the one-sided rider | *"a nonzero seed may confirm inside the licensed local lattice, while seed zero is a pole/out-of-lattice condition and is not a negative verdict"* |
| the Q-25 permanent limitation | present, with the "permanent carriage" clause above |
| the scalar-only caveat | present **twice** — in type preservation and again in the masking qualification — both with *"collector revision **and recommitment before any prediction exists**"* |

**Attainment still refused by enumeration — and strengthened.** V001 denied
creating five named seals; V002 denies creating **all eleven**, alongside
authorizing evaluation, binding a member, executing a fixed point or end test,
computing a number, comparing with a measured central value, or changing a
protected flag. The enumeration now matches the graph it governs.

---

## H4. FRESH ATTACK AND VERB AUDIT

### N1 — NOTE: the readiness board reports six conjuncts of roughly twenty-three

[PART-PROVABLE] `(M5c)` is the status board a ratifying principal will read. It
reports **six** items: `instrument_ratified`, the four rail seals, and the summary
`A32_PRE_EVALUATION_READY`. But `(M5a-V002)` now contains roughly **twenty-three**
conjuncts. The unreported ones include `schema_and_canonical_ID_tensions_resolved`,
`executable_eligibility_and_comparator_interfaces_frozen`,
`immutable_V011_specification_artifacts`, `passed_A01_A29_and_A35`,
`three_unanimous_specification_reports`, `exhaustive_registry_snapshot`,
`eligibility_implementation`, `external_randomness_beacon_rule`,
`complete_target_free_Q_spec`, `three_unanimous_Qspec_reviews`, and
`every_type_in_Task6TypedPayload_preserved`.

This is the cost of the repair succeeding: absorbing the ruling's preserved
non-seal conjuncts made the predicate much stronger, and the status display did
not grow with it. The information is not missing from the artifact — several
statuses are derivable from the twenty-row mapping (schema/ID from M3/M4/M6,
enumeration from P6) — but it is **not collected at the gate where it will be
certified**, and some conjuncts (the A-matrix rows, the unanimous report counts,
the Q_spec completeness) have no row in the twenty at all.

Why it matters, stated without inflation: `A32_PRE_EVALUATION_READY = false` is
correct and the logic is sound, so this blocks nothing. But a board showing five
falses reads as a shorter distance than a board showing which of twenty-three
conjuncts are already true, which are cheap, and which are the long poles. Several
of these are plausibly already satisfied; the principal cannot tell from `(M5c)`.

**Repair: one status column on the `(M5a-V002)` conjunct list.** Not
ratification-blocking — the instrument binds correctly whatever the column would
say.

### Verb audit on my own board

| My verb | Check |
|---|---|
| `CONFIRMED` | Confirms **the repair** within the bounded scope. Not a ratification, not a finding that any seal is true — every seal in the rail remains `false_of_record`. |
| "all eleven match exactly" | I parsed the sealed JSON myself and compared node by node; this is a transcription check, not an endorsement of the graph's content. |
| "structural, not cosmetic" | `(G3)`'s quantifier over the authoritative parent list is what makes it structural; I quote the mechanism rather than assert the quality. |
| "strictly stronger than `(M5a)`" | Established by mapping all eight V001 conjuncts forward and finding the additions; not inferred from the line count. |
| "no remaining weakening found" | A **failed hunt**, reported as such. I name the specific candidate I targeted and why it was the likeliest, so the negative result is checkable. |
| H2.1 self-correction | Recorded against my own 600 phrasing: my wording invited a worse repair than the one V002 chose. |
| N1 | Graded a **reporting** gap, explicitly not a logic gap, and marked not ratification-blocking. I did not inflate it to preserve a finding. |
| `READY_FOR_RATIFICATION = yes` | The two 600 defects are closed and the instrument's carries and refusals are intact. It is the principal's act, not mine. |

---

```text
A32_PREP_V002 = CONFIRMED (+1 NOTE: (M5c) reports 6 of ~23 (M5a-V002) conjuncts,
  so the readiness board understates the remaining distance and shows no long
  poles; the information is largely derivable from the twenty-row mapping but is
  not collected at the gate where it will be certified; repair is one status
  column; not ratification-blocking)
READY_FOR_RATIFICATION = yes
VERB_AUDIT_SELF = CLEAN
```

Both 600 findings are closed, and closed better than a literal repair would have
managed. The sixteenth source is admitted at its ruled strength; the eleven-node
graph is transcribed exactly, as I verified by direct parse; `(G3)` makes parent
certification transitive so that no demoted dependency survives by abbreviation;
the twenty-four preserved non-seal conjuncts are re-bound rather than discarded;
the register is pinned by entry inside the operative text; and M9's permanence and
P4's J-II identity are stated in the gate text as carriage rather than as
conditions readiness resolves.
