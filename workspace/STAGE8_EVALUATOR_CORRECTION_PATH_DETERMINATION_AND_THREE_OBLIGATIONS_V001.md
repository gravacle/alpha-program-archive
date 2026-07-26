# Evaluator Correction-Path Determination, and Three Append-Only Obligations V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY. DETERMINATION + ESCALATION. NO REPORT REWRITTEN. NO MECHANISM
BUILT. Cites canonical plan 12f204c64f0c0fd9... and amendment 001
c59cc8337913b81b...
VERDICT ON THE MECHANICAL QUESTION: option 3, THIRD BRANCH —
*** THE BATTERY CANNOT CURRENTLY REFLECT A CORRECTED REPORT STATUS. THAT IS
A BLOCKING DEFECT IN THE EVALUATOR CONTRACT ITSELF. ***
PRODUCTION PROHIBITED. alpha_computed = false.
```

## Q1 — WHAT DOES THE EVALUATOR READ? FIXED, CONSTRUCTED FILENAMES. Read from code.

```text
    T_IDS = [f"T{i:02d}" for i in range(0, 17)]        # T00 .. T16
    for tid in T_IDS:
        p = exec_dir / "t_reports" / f"{tid}.json"
Same construction for every other input:
    controls/{nc}.json ; core_reports/{role}.json ;
    reconstruction/report.json ; predictions.json ; result.json ;
    artifact_manifest.txt
THE FILENAME IS BUILT, NOT DISCOVERED. No directory scan reaches the
t_reports at all.
THE COMPLETE SET of version/scan-related tokens in the whole script — this
is the entire grep result, not a sample:
  line 154  p.resolve() == canonical.resolve()     (transform fence, not
                                                    version resolution)
  line 166  (exec_dir/"commitments").glob("*.commit")
  line 168  (exec_dir/"reveals").glob("*.reveal")
NO "supersede", NO "version", NO "latest", NO iterdir/listdir/scandir
ANYWHERE. The only two globs in the evaluator are the commitment and reveal
directories.
```

## Q2 — IS THERE A SUPERSESSION MECHANISM? NO. Categorically.

```text
A successor file — T02_v002.json or any other name — WOULD NEVER BE OPENED,
because the path is constructed from T_IDS rather than discovered. An
erratum sealed BESIDE a report is invisible to the evaluator for the same
reason. The verdict logic reads exactly one field:
    nodes[tid] = obj.get("pass") is True
```

### THE ASYMMETRY — and this is the actual defect, sharper than "no mechanism"

```text
THERE IS A PARTIAL ESCAPE HATCH, AND IT ONLY OPENS ONE WAY:
    if not nodes[tid]:
        item = obj.get("open_item")
        if item in DECLARED_OPEN:  -> notes (routes to CONDITIONAL)
        else:                      -> failures ("pass is not true")
That branch is reachable ONLY FROM pass: false.
MEASURED STATE of the three over-claimed reports:
    T01  pass=True   open_item=None
    T02  pass=True   open_item=None
    T11  pass=True   open_item=None
ALL THREE SAY pass: true WITH NO open_item. THEY NEVER REACH THE HATCH.
*** SO THE CONTRACT CAN EXPRESS "AUTHORED AS OPEN" BUT CANNOT EXPRESS
"DISCOVERED TO BE OVER-CLAIMED". For an append-only program, where every
correction is by construction discovered AFTER the artifact is sealed, that
is exactly backwards. ***
COLLATERAL OBSERVATION, not part of the question but found in the same read:
    T07  pass=False  open_item=None
T07's open_item is null, so it does NOT route to CONDITIONAL — it routes to
failures with "pass is not true". T07 currently BLOCKS the battery hard.
That is correct behaviour (T7(ii)/(iii) genuinely are blocked) but it means
the CONDITIONAL path is presently unexercised, which is the same
never-executed-accepting-branch shape recorded for the comparator.
```

## Q3 — SO WHICH OPTION IS IT? THE THIRD, AND artifact_manifest CANNOT SERVE AS THE OVERRIDE

```text
artifact_manifest.txt IS NOT AN INPUT-AUTHORITY MANIFEST. Verified at
source: it is consumed by the TRANSFORM FENCE — the evaluator walks each
listed path, strips ".", and greps for kappa_record digit-strings to catch
leakage into any non-canonical artifact. Repurposing it as an authority
override would change its meaning and damage the fence it exists to be.
THEREFORE, of the three options posed:
  (i)  an evaluator-input manifest naming the authoritative version —
       DOES NOT EXIST; artifact_manifest cannot be it without breaking the
       transform fence.
  (ii) a supersession field the evaluator honours — DOES NOT EXIST; the
       evaluator reads "pass" and, only when that is false, "open_item".
  (iii) *** THE FINDING: THE BATTERY CANNOT CURRENTLY REFLECT A CORRECTED
       REPORT STATUS. This is a BLOCKING DEFECT IN THE EVALUATOR CONTRACT,
       and it is prior to the three overclaims rather than a consequence of
       them. ***
NO MECHANISM IS BUILT AND NONE IS ADOPTED. Escalated to the principal.

WHY IT ORDERS AHEAD OF AUTHORING: five reports remain to be authored (T05,
T09, T12, T13, T14, T15 — six by Amendment 001's count, five needing new
work per this lane's correction, since T09 is harvestable). Authored onto
this contract, each becomes another node whose status can never afterwards
be corrected. The mechanism must land BEFORE they are written, or they
inherit the same defect.

AND A GAP THE EVALUATOR'S OWN SELF-TEST CANNOT CLOSE: --selftest builds a
deliberate transform-leak artifact and a bad commitment and asserts both are
detected. IT CANNOT TEST "a report asserting pass on an unsupported basis",
because no mechanism in the contract could detect one. That is the
"gate whose accepting branch has no constructible witness" principle sealed
earlier today, encountered from the other side: here it is a REJECTING
branch that has no constructible witness.
```

## THE THREE OVERCLAIMS, recorded append-only as OBLIGATIONS

```text
STATED PRECISELY, and the phrasing matters: AN OVER-CLAIMED REPORT IS NOT A
WRONG RESULT. IT IS A REAL RESULT FILED UNDER A LABEL IT HAS NOT EARNED.
None of the three is refuted. All three are OPEN.

T01  OVER-CLAIMED. Passes a REPRESENTED curvature obligation on a
     FORMULA-level derivation.
     WHAT WOULD MAKE IT HONEST: the represented basepoint link/holonomy
     object, with a machine-checkable chain back to Gate-4 F1.
     STATUS: open; not found in the corpus.
T02  OVER-CLAIMED — the clearest of the three. Its
     represented_nonzero_gr2_witness field is insufficient unless sealed as
     a witness in the ACTUAL REPRESENTED associated-graded quotient. V011
     states universal membership is only a LOWER BOUND, and flat/commuting
     representations can kill the represented class.
     WHAT WOULD MAKE IT HONEST: a sealed witness in the represented
     associated-graded quotient. The universal computation STANDS and is
     explicitly INSUFFICIENT.
     NOTE OF RECORD: this is the same gap this lane sealed independently
     earlier today in the battery tier-2 return. Two lanes, same defect,
     arrived at separately.
T11  OVER-CLAIMED. Proves local volume/face-measure behaviour; RECORDS
     response-level naturality.
     WHAT WOULD MAKE IT HONEST: response-map pullback commutation plus
     boundary-subextensive invariance — WHICH IS R-L2b's OPEN QUESTION.
     T11 AND R-L2b ARE THE SAME OPEN QUESTION WEARING TWO LABELS.
T07  mildly UNDER-claimed on progress; its blocking verdict is CORRECT and
     the finite conditioned Duhamel work is not reflected. NOTED, NOT
     FIXED, per instruction.
SOUND AS WRITTEN: T00, T03, T04, T06, T08, T10, T16.
```

## STANDING TRIPWIRE — EXTENDED TO A FOURTH FORM

```text
The tripwire this lane created for universal-vs-represented is extended, as
directed, to the family the independent lane has now named:
  1. UNIVERSAL vs REPRESENTED          (T2)
  2. OPERATOR vs SCALAR                (the gamma fork; a 1e-13 numerical
                                        cancellation refused as a theorem)
  3. OBJECT vs BOUND                   (the Q2 tripwire)
  4. FORMULA / LOCAL-MEASURE PROOF vs REPRESENTED / RESPONSE-LEVEL
     NATURALITY                        (T01, T11)
IN EVERY ONE: THE PROVED OBJECT IS REAL BUT WEAKER THAN THE VERDICT LABEL.
Four or five instances across two eras. THIS IS THE PROGRAM'S
CHARACTERISTIC FAILURE MODE, not a run of bad luck, and it is now recorded
as such rather than as four separate cautions.
STANDING CHECK, binding on this lane: before writing any verdict label, name
the category the proof actually lives in and the category the label claims,
and if they differ, the label loses. This lane walked into instance 1 one
artifact after naming it, which is the argument for a mechanical check
rather than a remembered one.
```

## Protected status

```text
evaluator_reads = fixed_constructed_filenames_T00..T16
directory_scan_of_t_reports = false
supersession_mechanism_exists = false
successor_report_would_be_read = false
adjacent_erratum_visible_to_evaluator = false
verdict_field_read = "pass" (then "open_item" only if pass is false)
correction_path_for_a_passing_report = NONE
contract_defect = BLOCKING
artifact_manifest_is_input_authority = false   (it is the transform fence)
overclaimed_reports = T01 T02 T11        (all pass=true, open_item=null)
overclaimed_reports_refuted = false      (all OPEN, none wrong)
T07_routes_to_failures_not_conditional = true
CONDITIONAL_path_currently_unexercised = true
selftest_can_detect_overclaim = false
mechanism_built_by_this_lane = none
report_rewritten_by_this_lane = none
escalated_to_principal = true
tripwire_forms = 4
production_authorized = false
alpha_computed = false
proof_authorized = false
```
