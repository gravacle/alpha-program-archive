# Register Completeness Audit — Addendum 001: The Section-Level Sweep, Re-Run

STATUS: LANE AUDIT ADDENDUM. **GAP IDENTIFICATION ONLY. NO ROWS WRITTEN.**
Appends to `STAGE8_REGISTER_COMPLETENESS_AUDIT_GAP_REPORT_V001.md` (`373136e1…`), which recorded its
18-gap count as an **explicit lower bound** because this sweep errored mid-stream and never returned.
LANE: EINSTEIN. CHARTER: PASTE #106 item B2. DATE: 2026-07-28.

```text
alpha_computed = false ; proof_authorized = false ; production_authorized = false
NOTHING ADJUDICATED. NO ROW WRITTEN. NO RULING RE-LITIGATED.
```

---

## §0 — THE DELTA

```text
COVERAGE:  235 artifacts indexed, 1,846 sections classified, in four disjoint slices,
           each adversarially verified with a kind test and a presence test.
VERIFIED DECISION GAPS, PER SLICE:  23 + 11 + 9 + 7  =  50
           *** NOT DEDUPLICATED across slices, nor against the prior sweep's 18. The prior 18 are
           largely a subset. THE HONEST STATEMENT IS: THE SECTION-LEVEL PASS ROUGHLY TRIPLES THE
           KNOWN GAP COUNT AND DOES NOT CLOSE IT. ***
DROPPED BY THE VERIFICATION PASSES: 3 + 11 + 6 + 12 = 32 candidates, on the kind test (findings
           inflated into rulings), the presence test, or register scope. ONE REFUTED OUTRIGHT.
```

**THE §3/§4 SHAPE IS CONFIRMED AS THE DOMINANT DEFECT, NOT AN ANECDOTE.** Every slice found it, and
every partial-capture claim that survived verification was checked split-by-split against the
register's own authority citations rather than by inference.

---

## §1 — THE FINDINGS THAT MATTER MOST

### 1.1 **The calibration artifact is still 4-of-6 uncarried — after R-16**

`STAGE8_EXTENSIVITY_VERDICT_AND_RL2B_CAMPAIGN_OPENING_V001`: §3 → R-16, §4 → R-5, §5 correctly
uncarried (self-types "ROUTE, NOT LEMMA"). **Uncarried: §1, §1.1, §1.2, §2.** Of these, §1 and §1.2
failed the kind test in the prior audit as **findings** and are not counted as decision gaps here;
**§2 — the R-L2b campaign chartering, four obligations declared one estimate — survives as a genuine
gap.** R-16 closed one of the gaps in the file that motivated the whole exercise.

### 1.2 **The transport charter: the register carries the refused obligation and none of the accepted ones**

```text
Charter §6, "THE THREE ACCEPTED OBLIGATIONS"; :227  accepted_obligations = O-D1 O-D2 O-D3
                                              :189  "PLUS O-D4, NOT YET ACCEPTED BY THE PRINCIPAL"
                                              :231  charter_remains_a_definition_iff = O-D3_discharged
REGISTER, by direct grep:  "O-D1" 0 · "O-D2" 0 · "O-D3" 0 · "O-D4" 1
*** IT CARRIES THE ONE OBLIGATION THE CHARTER RECORDS AS REFUSED AND NONE OF THE THREE IT RECORDS
AS ACCEPTED — INCLUDING THE ONE THE CHARTER SAYS ITS OWN VALIDITY DEPENDS ON. ***
```

### 1.3 **AMENDMENT_002: zero sections carried, and it amends a carried row's own object** — mine

`STAGE8_MASTER_PLAN_AMENDMENT_002` has **no** presence in the register; the string does not occur.
Its §A is *"the principal's ruling adding a precondition to §D"* — **§D is precisely the object of
R-8**. **THIS IS THE MAINTENANCE RULE'S OWN CASE: a seal that changes a decision's state and does
not touch the register.** It is my seal, as already recorded in the parent report.

### 1.4 **R-17 carries the ruling and is silent on what the ruling left open** — also mine

R-17 carries §1–§6's scope limits. **Uncarried: §6's "LEFT OPEN, NOT DECIDED HERE" block — O-A, O-B,
O-C — and §7's Z.2 header/body seam**, which that artifact's own flag marks
`Z2_header_body_seam_open = true # §7, principal's`. **A row that indexes a decision and drops the
four principal-held items the decision created.** (O-A and O-B have since been disposed inside R-19;
O-C, the kappa naming, and the seam remain unindexed.)

### 1.5 **R-4 carries one clause of eight, and two of the uncarried ones are load-bearing downstream**

`ARCHITECTURE_AMENDMENT_V001`: **A4(3) alone** → R-4. Uncarried: A1, A2, A3, A4(1), A4(2), A4(4),
**A4(5)**, **A5**. A4(5) is load-bearing in **two** later artifacts (AMENDMENT_002 §A; Route-2 §1);
**A5's binding no-promotion list is restated verbatim and declared binding in two later artifacts**
and has no row anywhere.

### 1.6 The Q2 standard and the kappa-rule artifact reproduce the same shape

`KAPPA_RULE_ADOPTION_STAGE12_ERRATUM…`: PART 1 → R-9, PART 3 → R-6, PART 4 → R-7, PART 5 → R-8 —
**four of five carried, and the one that reaches nothing is the only section that RETIRES anything.**
(Its own Status block says "Four parts" while five are written; recorded, not adjudicated.)

### 1.7 **The one positive result, and it is the design working**

**Three artifacts of 235 are FULLY carried: R-18, R-19, and the Rule-6 recovery amendment — the
newest three.** They are the artifacts written under the same-act discipline. **The register CAN
hold a whole artifact; the rule works when it is followed.**

---

## §2 — WHAT THE VERIFICATION PASSES KILLED

Recorded because an audit that over-reports would trigger a register rewrite on bad data.

```text
32 of 82 candidates dropped. Representative:
- ONE REFUTED OUTRIGHT: the "production gate Part C / B3 — two escalations, register took one"
  claim. Defeated by a later sealed artifact: "B3 IS DISCHARGED. B4 IS NOT," answering the
  principal's own question and stating "B3 is not awaiting a ruling."
- "The sealed O1 display is defective" — THE SECTION HEADING IS LITERALLY "NEW FINDING". Dropped.
- "C3 and C5 are REFUTED by exact witness" — a lane established a fact. FINDING. Dropped.
- Route-2 §7 "WHAT THIS RULING DOES NOT AUTHORIZE" — a SCOPE FENCE on §3's ruling, not an
  independent ruled item; the same slice classified every other such block as NEITHER. Dropped.
- The W-1..W-4 timestamp withdrawals — the artifact's own flag reads
  conclusions_changed_by_the_audit = 0, and each withdrawal re-grounds and PRESERVES its
  conclusion. The maintenance rule's trigger is not met. Dropped.
```

---

## §3 — **THIS SWEEP DOES NOT CLOSE THE AUDIT EITHER, AND SAYS SO**

```text
SLICE 2 opened 38 of 174 in-scope artifacts at section level and NAMED the 136 it did not, by
  class, with the line "named so this is not read as coverage." It named its own top residual
  risks unprompted — 66 unopened COMPLETE_QSPEC files, and Stage-7 candidates whose heading maps
  show "Adopted premise classes" and "Open Q_spec slots".
SLICE 3 indexed 89 of 117 at HEADING LEVEL ONLY plus a decision-verb grep — and its own verifier
  states this fails the sweep's own standard: "THE UNIT OF INDEXING MUST EQUAL THE UNIT OF SEALING
  ... a header regex is a filter, not an index."
*** SO THE §3/§4 INSTRUMENT HAS NOW BEEN RUN PROPERLY ON ROUGHLY HALF THE CORPUS AND PARTIALLY ON
THE REST. 50 IS A BETTER LOWER BOUND THAN 18. IT IS STILL A LOWER BOUND. ***
COVERAGE HONESTY WAS VERIFIED, NOT ACCEPTED: each slice's enumeration was independently reproduced
by its verifier — 22/2967 lines, 58/487 sections, 117 files — and all matched to the line. Nine
subdirectory duplicates were confirmed byte-identical with cmp before being excluded.
```

## §4 — FLAGS

```text
section_level_sweep_completed            = true       # the errored sweep, re-run
artifacts_indexed                        = 235
sections_classified                      = 1846
verified_decision_gaps_per_slice_sum     = 50         # NOT DEDUPLICATED
prior_reported_gaps                      = 18         # largely a subset
candidates_dropped_on_verification       = 32
candidates_refuted_outright              = 1
partial_capture_artifacts_confirmed      = 8+         # every slice found the §3/§4 shape
fully_carried_artifacts                  = 3          # R-18, R-19, Rule-6 — THE NEWEST THREE
audit_now_complete                       = false      # §3 — still a lower bound
rows_written_by_this_addendum            = 0
```

## §5 — INVENTION CHECK

```text
NO ROWS WRITTEN. NO ROW TEXT DRAFTED. NOTHING ADJUDICATED, NO RULING RE-LITIGATED — per the
charter: "Report the delta; DO NOT write rows beyond what you find, and do not write any row the
principal has not authorized."
THE COUNT IS STATED AS A PER-SLICE SUM AND EXPRESSLY NOT DEDUPLICATED. It is not presented as a
census and the parent report's lower-bound framing is retained rather than replaced.
32 CANDIDATE GAPS WERE DROPPED BY VERIFICATION AND THE DROPS ARE HONOURED HERE, including one
outright refutation that cut against the sweep's own headline.
TWO OF THE FINDINGS ARE THIS LANE'S OWN DEFECTS (§1.3 AMENDMENT_002, §1.4 R-17) and are recorded
as such rather than attributed elsewhere.
kappa NAMING OBSERVED: kappa_record in full, never bare.
```
