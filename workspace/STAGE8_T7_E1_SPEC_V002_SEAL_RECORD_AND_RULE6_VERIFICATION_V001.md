# Stage-8 T7 E1 Spec V002 — Seal Record, Transport Repair, and Rule-6 Verification V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY SEAL RECORD. The spec it seals is NOT EXECUTABLE.
```

## What was sealed

```text
STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md
  seal  468467303a109dc825b015107897dacc107800fc981030377c3f006b384cccb5
  size  145010 bytes / 2344 lines
  head  "SPEC_DRAFT_V002 — APPEND_ONLY SUCCESSOR TO 9cfafde1 ... NOT
         EXECUTABLE UNTIL A FRESH-CONTEXT HOSTILE LANE CLEARS IT"
Predecessor 9cfafde1… is PRESERVED, UNEDITED, and remains non-executable.
```

Hostile pre-execution review LAUNCHED at seal (seven independent attack
lanes plus adversarial refutation). Execution requires: that review's
clearance, the two seal carve-outs below (now DISCHARGED), and the
principal's answer to E-Q1.

## The transport event, and a FALSE ALARM this lane raised and is recording

```text
WHAT HAPPENED. The drafting lane's spec text was emitted as ONE model
message that hit the max_tokens limit at 131,858 characters
(stop_reason = max_tokens) and was auto-continued by a second message of
12,349 characters (stop_reason = end_turn), with NO intervening turn. The
workflow return carried ONLY the second message, so the return alone was
not the spec. The full text was recovered by splicing the two assistant
text blocks byte-exactly out of the lane's own transcript
(subagents/workflows/wf_091417a1-657/agent-a553f6f93c96be67c.jsonl),
verified by round-trip read-back.

THE FALSE ALARM, RECORDED BECAUSE A WRONG ALARM SILENTLY DROPPED IS AS
CORROSIVE AS A WRONG CLAIM SILENTLY KEPT. The two halves joined as
"...D3 (with its frozen standard reading), D4-" + "as-M-2, M-3, ...".
This lane judged that a fragment of the §S reaffirmation list had been
LOST in transport, said so, and prepared to reconstruct the list by
complement from the parent spec. THAT JUDGEMENT WAS WRONG.
"D4-as-M-2" is the drafting author's own idiom and appears VERBATIM in
the sealed parent v001 (9cfafde1…) at line 1393. The continuation resumed
at the exact character. NO CONTENT WAS LOST, and no reconstruction was
performed. Caught by going to the sealed parent instead of trusting the
inference.
```

## The ONE repair made at seal, disclosed

```text
DEFECT: the closing ``` of §S was not re-emitted after the continuation.
From §S onward the document's code fences were off by one — three later
headers (§X, Protected status, §H) fell INSIDE fences and the document
ended at fence depth 1.
REPAIR: this lane inserted the single missing closing fence. FOUR BYTES.
No content byte altered, nothing added, nothing removed. Verified after:
fence depth 0, zero headers inside fences. The sealed bytes ARE the
repaired bytes; the seal above covers them.
This is a formatting repair to a transport artefact, NOT an amendment to
the drafting lane's content, and it is recorded rather than passed over.
```

## Standing operational limitation discovered here

```text
A WORKFLOW LANE CANNOT BE ASKED A FOLLOW-UP QUESTION. This lane attempted
to have the drafting lane re-emit the passage it believed damaged;
SendMessage returned "No transcript found for agent ID:
a553f6f93c96be67c". Workflow lanes are not addressable after return.
CONSEQUENCE, now standing: a drafting lane's product must be recoverable
from its TRANSCRIPT, because the lane itself is gone the moment it
returns. Any long artifact authored by a workflow lane must be spliced
from the transcript and fence-checked before seal, exactly as here.
```

## Rule-6 verification AT SEAL — required, performed, and one revision disclosed

Required by STAGE8_T7_D3_FREEZE_RATIFICATION_AND_PREDICTION_WEIGHTING_
RULE_V001 Part 2 ("because the drafting lane was launched before this rule
was sealed, the construction lane will verify Rule-6 compliance AT SEAL
and record any revision it makes").

```text
VERDICT: COMPLIANT, AND MORE THAN COMPLIANT. §P(3) states the
disagreement explicitly, weights the independent family higher, and then
does the thing that costs something: it CHANGES THE SPEC'S OVERALL
PREDICTED OUTCOME to E1S_BLOCKED to match the independent family's P-C1,
WITHDRAWING v001's prediction of a certified n >= 2 sector — and records
that it did so and why. (a), (b) and (c) of Rule 6 are all discharged.

ONE REVISION, DISCLOSED AND NOT SILENTLY APPLIED. §P(2) states the
independent family "HAS LANDED TWICE CONSECUTIVELY". At seal it is THREE:
P-C7 (arm-2 C(ii)) LANDED VERBATIM after the drafting lane was launched.
The sealed spec text is NOT edited. This record supersedes the count.
DIRECTION OF THE ERROR: wherever §P's arm-2 predictions rest on a
two-cycle record they in fact rest on a THREE-cycle record, so the
weighting §P applies is if anything UNDER-stated, not over-stated.

DEFERENCE CHECK NOT SELF-CERTIFIED. Whether any individual prediction was
changed to agree with the independent family WITHOUT an independent
ground — the drafting author's own reviewer-target F — is assigned to the
hostile review, not answered here. A lane cannot certify its own
calibration; that is the same loophole the Rule-6 recovery amendment
closed.
```

## §P(1) — the ledger defect the spec flagged, fixed and then SHARPENED

```text
The spec's N-19 notes that CALIBRATION_LEDGER.md's standing header said
MISSED TWICE while three misses were recorded in its table, and that the
spec's THREE is right. This lane found and fixed the same defect
independently, before reading the spec. Two lanes converging on one
ledger defect from opposite directions.
FIXED FURTHER, and this is now the wording of record: there are THREE
magnitude misses (theta_kappa, gamma P2, control-4 S3(a)) and ONE
magnitude HIT (S3(b)) — and S3(b) predicted a NULL/bound, not the size of
a nonzero effect. So "three CONSECUTIVE" was itself contestable with a
hit sitting two rows above. The defensible statement, which every future
magnitude window must cite:
  EVERY PREDICTION THIS LANE HAS MADE ABOUT HOW BIG A NONZERO EFFECT
  WOULD BE HAS MISSED.
```

## §A0 authority verification, performed by this lane not accepted on report

```text
36 rows parsed. 35 VERIFIED EXACTLY — recomputed sha256 matched the
pinned hash AND the adjacent-seal state matched the row's claim
(SEAL_MATCH / NO_SEAL_FILE) in every case.
1 DRIFT, and it is the declared drift-exempt row (H-1):
  CALIBRATION_LEDGER.md — living document, unsealed by design.
  NEW HASH OF RECORD:
  8dde09887e2529f835795614c5679ff922fc628e58279410030c0d54debfec7c
  (moved by this lane's own P-C7 entry and the §P(1) sharpening above)
No other drift. The executor must re-verify all rows again before any
computation; this verification does not substitute for that.
```

## §H seal-time items — disposition

```text
H-1  DONE (above).
H-2  CARVE-OUTS DISCHARGED. Both unsealed sole-source authorities are now
     SEALED by this lane:
       CARVE-OUT A  STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_RESULT_V001.md
                    (3a6ff617…) — SOLE source of C1, the derived starting
                    point of the whole program, including the A-L1 kernel
                    constant, the C-L3 log coefficient and 2/pi.
       CARVE-OUT B  BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_DERIVATION_V001.md
                    (b786db3a…) — tau_R = pi/sqrt2, on which every exact
                    phase collapse in C4 and C-L1 depends.
     Rows 3-8 of H-2 remain hash-pinned with mandatory executor
     re-verification, as the spec requires.
H-3  RESOLVED AS SCRATCH, with a finding. verify_v002.py (47589c71…) DOES
     NOT EXIST ON DISK — a filesystem-wide search finds no such file. The
     drafting lane hash-pinned a file it did not persist. Excluded from
     the sealed record; carries no verdict authority; ITS PINNED HASH IS
     UNVERIFIABLE and no lane may cite it. Recorded as a defect of the
     handoff, minor but real.
H-4  Corrections-of-record acceptability: NOT self-certified. Routed to
     the hostile review together with H-5 and H-6.
H-5  D5' split / S-7,S-8 supersessions / O6 re-verbing scope: routed to
     the hostile review.
H-6  Parent's Route-Q line update: OPEN, owned by the parent majorant
     spec, not by v002 and not closed here.
```

## Escalated to the principal — MANDATORY BEFORE EXECUTION

```text
E-Q1 SCOPING QUESTION the spec may not answer by executing:
     "Is the pinned skeleton's cell 4-volume an admissible constant under
     spec-header scoping clause 1?"
     Weakening F'-5 is not a lane's act, and the spec may not be executed
     carrying an obligation that is unsatisfiable under its own fence. If
     the principal DECLINES the relief and both R-L0 grounds and R-L0b
     fail, then R-L0 fails with its named witness and THAT IS THE HONEST
     OUTCOME — stated here in advance so it cannot be answered by
     execution after the fact.
E-Q3 Whether v002 executes before F-8 closes is the principal's
     scheduling call. F-8 clause (3) cannot discharge before Phase A
     executes; that is a sequencing fact, not a lane failure.
E-Q2 CLOSED: the reconciliation slot reserved by R7 was filled by
     fc4368c7…. No new slot is reserved. Any further independent-system
     return arrives as a fresh append-only amendment; if it contradicts a
     repair here, THE CONTRADICTION IS REPORTED, NOT RESOLVED SILENTLY.
```

## Protected status

```text
E1_successor_spec_v002_sealed = true
E1_successor_spec_v002_seal = 468467303a109dc8…
E1_successor_spec_v002_hostile_review_cleared = false
E1_successor_spec_v002_executable = false
rule6_verified_at_seal = true
rule6_seal_time_revision_disclosed = true    (two cycles -> THREE)
independent_family_consecutive_landings = 3
A0_rows_verified_by_construction_lane = 35_of_36  (1 drift-exempt)
H2_carve_out_A_sealed = true
H2_carve_out_B_sealed = true
H3_verify_script_absent_from_disk = true
E_Q1_scoping_answer_from_principal = pending   (BLOCKS EXECUTION)
transport_repair_disclosed = true              (one closing code fence)
false_alarm_recorded = true                    (no content was lost)
production_authorized = false
alpha_computed = false
proof_authorized = false
```
