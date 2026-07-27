# B3/B4 Status Determination, and an Unfenced v001 Route V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY FINDING. Answers the principal's question of this date:
  "Confirm: are B3 and B4 discharged by the fence, pending the rehearsal, or genuinely
   awaiting a ruling? Do not re-present them as principal decisions if the fence closed them."
DETERMINATION: **B3 IS DISCHARGED. B4 IS NOT.**
NOTHING IS FIXED HERE. The principal's standing stop rule is in force verbatim: "if fixing
this reveals ANOTHER layer beneath it ... DO NOT FIX IT. Report it and STOP." Rule 8
(pipeline feature freeze) is also in force. NO chmod was run. NO script was edited.
PRODUCTION PROHIBITED on both gates independently of everything below.
alpha_computed = false. proof_authorized = false.
```

## 1. B3 — DISCHARGED BY THE FENCE

The directory-permission fence was the principal's own third option, not a lane invention.
It was probed (probes 9-18); its one open adoption condition — the item-2 "legitimate
production still completes" probe — was run inside the A2 rehearsal and answered YES; and
the follow-on question of whether an environment that resets the mode bits permits the fence
to stand was answered in the record: **adoption rests on the controller's L3 pre-flight
re-assertion, not on the bits.**

**B3 is not awaiting a ruling.** The "TWO ESCALATIONS THE PRINCIPAL MUST DECIDE" header on
`STAGE8_T7_PRODUCTION_GATE_NOGO_AND_PIPELINE_REPAIR_BINDING_V001.md` is a **stale label** that
the append-only corpus never edited. It should not be read as a live escalation for B3.

## 2. B4 — NOT DISCHARGED. Its obligation is an ENUMERATION.

B4 verbatim, `STAGE8_T7_PRODUCTION_GATE_NOGO_AND_PIPELINE_REPAIR_BINDING_V001.md:145-151`:

```text
B4 THE v001 CHAIN SELF-BLOCKS ONLY AFTER A WRITE-CAPABLE STEP: it seals
   an immutable BLOCKED artifact at a canonical path in the course of
   blocking. The disarm disposition's v001-exclusion rationale is
   therefore PARTIALLY REFUTED. Obligation accepted: re-verify which
   v001 invocation routes reach the write and fence them; the fix class
   is B3's, so it is escalated with B3 rather than decided separately.
```

**"Re-verify WHICH v001 invocation routes reach the write" is an enumeration obligation.**
It is discharged only by covering the whole route set. It is not discharged by the fence
being adopted, because the fence is a *mechanism* and B4 asks for a *census*.

## 3. THE ROUTE THAT WAS NOT ENUMERATED — verified directly by this lane

```text
FILE:   scripts/launch_stage8_t7_content_addressed_runtime_v001.py
STATE:  EXISTS, 8843 bytes, at a CANONICAL, NON-QUARANTINED path.
        UNSEALED — no adjacent .seal.sha256.   [verified by this lane]

VERIFIED BY READING THE FILE, not relayed:
  line  27   RUNTIME_MARKER = "_stage8_t7_content_addressed_runtime_v001"
  lines 28-42 ALLOWED_TARGETS frozenset includes primary_v001.py,
             independent_v001.py, v001.py, response_v001.py, and
             scripts/run_stage8_t7_actual_parent_car_pipeline_v001.py
  line 211   require(relative in ALLOWED_TARGETS, ...)
  line 218   setattr(sys, RUNTIME_MARKER, attestation)      <-- THE LAUNCHER SETS THE MARKER
```

**Why this matters, stated as the mechanism rather than as an alarm:**

```text
(1) The v001 derive scripts gate on a runtime marker. LAUNCHER v001 SUPPLIES THAT MARKER.
(2) Probes 18a/18b were run WITHOUT a launcher. The marker was therefore absent and the
    gate blocked them. THE PROBES PASSED BECAUSE NO LAUNCHER WAS PRESENT — they did not
    test the launcher-present case, so they are not evidence about it.
(3) Fence adoption was rested on the CONTROLLER's L3 pre-flight self-heal. A launcher-v001
    route DOES NOT GO THROUGH THE CONTROLLER. So the adopted protection does not fire on
    this route. THIS IS THE SAME BYPASS ARGUMENT B3 ITSELF USED against probe #8.
(4) The fallback protection is the at-rest mode bits, and they are DOWN right now (§4).
```

So the one route the census missed is precisely the route on which the adopted protection
does not fire, while the fallback is not in place. That conjunction is the finding.

## 4. THE FENCE IS NOT AT REST — measured this date

```text
MEASURED, not inferred:
  drwxr-xr-x   stage8_execution              = 0755   NOT 0555
  drwxr-xr-x   stage8_execution/t_reports    = 0755   NOT 0555
  drwx------   stage8_execution/work         = 0700   NOT 0555
```

**This is a RECURRENCE, and the recurrence is the point.** The cycle-7 fence finding
established the cause as external agency — iCloud Desktop-and-Documents sync
(`FXICloudDriveDocuments = 1`), confirmed by the reviewer lane, after this lane's own rsync
hypothesis was tested and refuted. The bits going back down is therefore *expected* under
the sealed diagnosis, which is exactly why adoption was rested on pre-flight re-assertion
rather than on the bits. **The defect is not that the bits are down. It is that the one
route which skips the pre-flight was never enumerated.**

**NOT FIXED, DELIBERATELY.** Re-running chmod would restore the bits, produce a fresh
"at rest" reading, and mask a live gap behind a green light — which is the failure this
program logged as the Stage-12 fabrication class. The bits are left as measured.

## 5. WHAT THIS DOES AND DOES NOT MEAN

```text
IT DOES NOT MEAN A WRITE HAS OCCURRED. No claim is made that anything was written. This is
  a reachability finding, not an incident report. No evidence of any write was sought or found.
IT DOES NOT UNBLOCK OR BLOCK PRODUCTION. Production is prohibited on both gates for reasons
  entirely independent of this. Nothing here changes that in either direction.
IT DOES MEAN B4 CANNOT BE REPORTED CLOSED. The enumeration is incomplete by at least one
  route, and that route is unsealed.
```

## 6. THE THREE OPTIONS, AND WHY NONE IS TAKEN HERE

```text
OPTION A  SEAL AND ENUMERATE. Seal launcher v001, complete the v001 route census, re-probe
  with a launcher PRESENT (the case probes 18a/18b could not test). Cost: real work, and it
  is pipeline work, so it needs a Rule-8 exception. Closes B4 properly.
OPTION B  QUARANTINE LAUNCHER v001, folding it into the open v005/v006 quarantine decision.
  Cost: cheapest; does not complete the census, so B4 closes by removal rather than by proof.
OPTION C  ACCEPT AND DISCLOSE. Record B4 as permanently partial with this route named.
  Cost: an honest but standing hole in the production gate's own evidence.
NONE IS SELECTED. Rule 8's default answer is no, and the stop rule says report and STOP.
```

## Protected status

```text
B3 = DISCHARGED_BY_THE_FENCE
B4 = NOT_DISCHARGED_ENUMERATION_INCOMPLETE
prodgate_header_two_escalations = STALE_LABEL_never_edited (append-only corpus)
unfenced_route = scripts/launch_stage8_t7_content_addressed_runtime_v001.py
unfenced_route_sealed = false
launcher_sets_the_runtime_marker = true        [verified by reading lines 27/211/218]
probes_18a_18b_tested_launcher_present_case = false
adopted_protection_fires_on_this_route = false (controller bypass)
fence_at_rest = false                          [measured: 0755 / 0755 / 0700]
fence_reopening_cause = iCloud_Desktop_and_Documents_sync (sealed, cycle 7)
anything_fixed_here = NOTHING
chmod_run = false
script_edited = false
write_occurred_claim = NONE_MADE_NONE_SOUGHT
option_selected = none
production_authorized = false
alpha_computed = false
proof_authorized = false
```
