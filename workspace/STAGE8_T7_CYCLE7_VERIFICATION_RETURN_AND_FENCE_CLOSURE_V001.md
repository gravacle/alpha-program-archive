# Stage-8 T7 Cycle-7 Verification Return, and Fence/Manifest Closure V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY VERIFICATION RETURN WITH ITS ACTUAL NUMBERS.
Closes items 1, 2 and 3 of the cross-family cycle-7 NO-GO verdict
(Codex against Bohm's ten-point checklist; two of three BLOCKING
findings independently reconfirmed from source by Bohm).
PRODUCTION REMAINS PROHIBITED. The 34-component diagnosis is NOT
this lane's and is NOT touched here.
```

Item 3 of the verdict was that no cycle-7 verification-return transcript
existed to seal-check — third recurrence of that class. This artifact is
that return. The pipeline author lane's return is sealed VERBATIM
alongside it:

```text
STAGE8_T7_CYCLE7_PIPELINE_AUTHOR_LANE_RETURN_VERBATIM_V001.txt
  11626 bytes / 11566 chars
  sha256 027708f05df3caa16c5e4810a2022ad9b6d4ca6cb1ea065683ad800e20662f96
  byte-exact from the lane's own return value; round-trip verified.
```

EVERY NUMBER BELOW IS LABELLED BY WHO ESTABLISHED IT. Numbers marked
REPORTED are the author lane's rehearsal figures, carried unaltered.
Numbers marked VERIFIED HERE were re-established by this lane directly.

## ITEM 1 — FENCE NOT AT REST: closed, with the cause diagnosed

### The fix (VERIFIED HERE, each step by observation not assumption)

```text
BEFORE      stage8_execution/work  drwx------ (0700)
            provenance             drwx------ (0700)
RESTORED    chmod 555 both         dr-xr-xr-x (0555) each
LIVE PROBE  write attempt into provenance at rest
            -> "permission denied", and NO FILE LEAKED (checked)
AFTER the L4 raise and all three preflight invocations:
            both directories dr-xr-xr-x (0555)
```

### The at-rest assertion now ACTUALLY FIRES — three independent witnesses

```text
(1) The L4 raise record emitted by the manifest builder carries
    "provenance_was_fenced_at_rest": true — the builder OBSERVED the
    fence at rest before raising, and reported
    "fence_state_after_drop": {"provenance":"0555",
                               "stage8_execution/work":"0555"}.
(2) fence_at_rest is PRECONDITION #3 of the frozen thirteen-precondition
    tuple, which the preflight output enumerates in order:
      runtime_attestation, generation_coherence, fence_at_rest,
      implementation_manifest, authority_digests, bridge_binding,
      push_capability, prior_receipts, primary_route1_readiness,
      comparison_bundle_stamps, comparison_bundle_provenance,
      comparator_authority, canonical_absences
(3) All three preflight invocations report fence_anomalies: [] and
    fence_state_after_preflight 0555/0555 — the assertion ran, found the
    fence at rest, and had nothing to self-heal.
FENCE_AT_REST_MODE = 0o555 at run_..._v007.py:585 (0o555 = 365 decimal,
which is the at_rest_mode the coherence row reports).
```

### WHAT RE-OPENED THEM — the three named candidates are excluded on the observed mode value

The verdict asked: my own manifest-sealing raise, a lane exit path that
missed the drop, or the SIGKILL window?

```text
ALL THREE ARE EXCLUDED BY ONE OBSERVATION. Every program path sets
either 0o555 (FENCE_AT_REST_MODE) or 0o755 (FENCE_RAISED_MODE) and
NOTHING ELSE — verified by reading every chmod in controller v007 and
in the manifest builder. A missed drop, a hard kill inside the raised
window, and an interrupted raise ALL LEAVE 0755. The observed mode was
0700, which NO code path in this program produces.
  - manifest-sealing raise: additionally excluded by time. Manifest v006
    did not exist on 2026-07-26 at 09:07:04 and was first built at 10:18
    today; that build recorded its raise and dropped to 0555.
  - lane exit path / SIGKILL window: excluded as above on the mode value.

POSITIVE EVIDENCE, VERIFIED HERE:
  - both directories carry ctime 2026-07-26 09:07:04 — THE IDENTICAL
    SECOND. One operation over both.
  - mtime unchanged on both (work 08:35:39, provenance 01:14:11) and NO
    file inside either directory was created or modified. chmod
    semantics, not a write.
  - THE DISCRIMINATING TEST: of 279 directories in the cleanroom tree,
    EXACTLY TWO deviate from 0755 — and they are precisely the two the
    fence had set to 0555. Nothing else in the tree deviates at all.
    Whatever acted selected exactly the anomalous pair and normalised it
    to 0700 — not to 0555 (the fence value) and not to 0755 (the tree's
    prevailing mode).
  - the parent stage8_execution is untouched: 0755, ctime 02:09:39.
  - NO LOGGED TOOL CALL from the construction lane or the pipeline author
    lane touched either directory at that second. The author-lane calls
    bracketing 09:07:04 (09:06:55 and 09:07:12) are both Edits to files
    under scripts/. The command that began at 09:06:21 only cp'd three
    files inside scripts/ and issued no chmod.

CONCLUSION, STATED AT THE STRENGTH THE EVIDENCE SUPPORTS: no program
route and no logged lane action produced this. An agency outside the
program altered the fence bits, and it targeted exactly the two
directories whose modes were unusual. The specific external actor is NOT
identified and is NOT claimed — most plausibly a platform agent
normalising modes under a synced ~/Documents tree, but that remains a
hypothesis.

THE VERDICT'S OWN CONSEQUENCE IS ACCEPTED IN FULL: the B3/B4 probe
evidence was gathered under 0555 and does not count as live pre-GO
protection for any state that is not 0555. It now IS 0555 and the
assertion fires; but limitation L2 must be read in its widened form —
the bits can be reset with no human act and no program route involved,
so L3 pre-flight is LOAD-BEARING, not defensive.
```

## ITEM 2 — CANONICAL G7 MANIFEST: sealed (VERIFIED HERE)

```text
Built and sealed through the authorized route, not by hand:
  <pinned python> -I -S scripts/launch_..._runtime_v007.py \
    scripts/build_..._implementation_manifest_v006.py --l4-raise-and-record
RESULT
  provenance/stage8_t7_actual_parent_regulated_car_operator_response_
    implementation_v006.json
  sha256   642d10c0ef86020e3377695ebc9544427e4df363f31d56a9e96a48bf3da1b212
  rows     12
  adjacent .seal.sha256 written by the builder INSIDE the raise;
    verified OK by shasum -c from the containing directory
  both artifacts left mode 0444; fence dropped back to 0555 and verified
COHERENCE NOW RESOLVES, which is the point of the item: preflight for
lane independent returns PREFLIGHT_OK and reports
  implementation_manifest_sha256 = 642d10c0…  (the file just built)
  bridge_manifest_sha256         = f573ae21…  (the sealed v001-path bridge)
so controller v007's pin at line 230 and the on-disk manifest now agree.
The G7 coherence record is amended by this artifact (append-only; the
sealed table d77dda56… is NOT edited): manifest_v006_sealed = TRUE,
digest as above.
```

### A fail-closed behaviour worth recording, found while firing the assertion

```text
Invoked DIRECTLY (not through the launcher), the controller blocked:
  "pipeline requires the sealed runtime launcher"
— precondition #1 refusing an unattested runtime. Correct, and it caught
this lane's own first attempt.
Through the launcher, lane ORDER also enforces itself:
  lane primary    -> PREFLIGHT_BLOCKED "lane-order violation: the
                     independent receipt is absent; run --lane
                     independent (and anchor it) first"
  lane comparison -> PREFLIGHT_BLOCKED, same reason
Both blocked with the fence still at rest and no artifact written.
PREFLIGHT_OK IS NOT STARTABILITY EVIDENCE (A2). It is not offered as
such here. The only accepted startability evidence remains the no-stubs
end-to-end rehearsal, and THAT REHEARSAL SAYS THE COMPARISON DOES NOT
PASS.
```

## ITEM 3 — THE VERIFICATION RETURN, with its actual numbers

### Rehearsal (REPORTED by the author lane; not re-run, per instruction)

```text
A2 REAL-CHAIN REHEARSAL — 184 s, no stubs, no monkeypatches, disposable
copy starting from the canonical at-rest state.
  L4 manifest build            OK, raise recorded, fence dropped
  superseded-route probe (B3)  launcher v002 -> derive independent v002,
                               fence at rest -> PermissionError on
                               '…_v001.json.blocked.tmp', rc 1,
                               ZERO artifacts
  --preflight-only             PREFLIGHT_OK (recorded; explicitly NOT
                               offered as evidence)
  lane independent   84.6 s  SUCCEEDED  raised, 2 outputs + receipt,
                                        dropped, verified closed
  lane primary       11.2 s  SUCCEEDED  raised, 2 outputs + receipt,
                                        dropped, verified closed
  lane comparison     2.6 s  BLOCKED    raised, comparator wrote its
                                        sealed verdict, dropped, verified
                                        closed; NO RECEIPT SEALED
                                        (A4 held in the real chain)
  FENCE ADOPTION PROBE  -> YES on function: every lane raised and dropped
    both directories, every lane wrote through the raised fence, the fence
    was verified closed after every lane BY ATTEMPTING A WRITE, and the
    superseded route wrote nothing.
  PIPELINE VERDICT      -> NOT A PASS
    ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_BLOCKED,
    "34 component comparison(s) failed"
The rehearsal test exits nonzero on that verdict by design, and fence
evidence is collected for every lane BEFORE the numerical outcome, so a
numerical result can never be reported as a fence failure or vice versa.
```

### Suites (REPORTED, at the final byte state)

```text
test_stage8_t7_launcher_v007.py       6/6   PASS
test_stage8_t7_controller_v007.py    10/10  PASS
   incl. 8 one-pin skews each blocking BY PIN ID; manifest-row skew;
   fence raise/drop; L3 self-heal; a REAL SIGTERM inside the raised
   window; A4 twice
test_compare_..._v006.py              5/5   PASS
```

### The 34 — recorded, NOT diagnosed here

```text
34 of 157 component comparisons exceed TRANSPORTED_MATRIX_TOLERANCE
= 3.0e-4: propagators 10, cross_operators 24; split ell0 28 / ell1 6.
  worst    8.411e-4  = 2.80x budget
  typical  4.206e-4  = 1.40x budget
  the 104 PASSING transported rows top out at 2.941e-4 — the whole
  population sits AT the budget scale.
Bit-for-bit reproducible across two independently produced bundle pairs
(one built under launcher v006, one under v007).
*** THIS DIAGNOSIS IS NOT THIS LANE'S AND IS NOT PRE-EMPTED HERE. ***
No budget, tolerance, threshold, quadrature or basis pin has been
adjusted by this lane; the rehearsal has NOT been re-run to confirm any
reading of the failure; no numerical value anywhere has been touched.
The independent lane is diagnosing it under the constraint that nothing
numerical may be revised, and routes the outcome to the principal.
```

### Tolerance freeze status (VERIFIED HERE, and stated precisely)

```text
TRANSPORTED_MATRIX_TOLERANCE = 3.0e-4 is byte-identical in comparators
v002, v005 and v006, and SEALED implementation manifest v001 — the
earliest, the one the byte-frozen derive lanes verify row-by-row at
canonical paths — HASHES COMPARATOR v002. Manifests v004 and v005 hash
comparator v005. The number was therefore hash-pinned into a sealed
manifest generations before any comparison result existed: the freeze is
REAL and OUTCOME-BLIND.
PRECISION, because the stronger word was used: 3.0e-4 IS NOT STATED IN
ANY SEALED PROSE SPEC. "Preregistered" rests on code provenance hashed
into sealed manifests, not on a spec clause. Recorded so the gap cannot
be exploited later; it does not license revision.
```

## What cycle 6's finding B2 cost, and what it bought — recorded of record

```text
The no-stubs rehearsal did exactly what it was built to do. Cycle 6's
finding B2 — "the production combination executed in NO test on disk" —
is now CONFIRMED BY EXECUTION rather than by inspection, and executing
it surfaced a real discrepancy that SIX audit cycles, TWO hostile review
rounds, and every unit test on disk all missed.
That is the single most valuable thing the pipeline work has produced.
It is also the argument, now evidenced rather than asserted, for A2's
permanence: PREFLIGHT_OK and a green suite are not startability
evidence, and only running the real combination end to end found this.
```

## Cross-family confirmations carried forward (from the verdict)

```text
NO UNEXPLAINED DRIFT in the sampled functional diffs.
Hoists CONDITION-IDENTICAL (comparator v006 pre-consumption prologue plus
  the in-try recheck).
RECEIPT ORDER CLEAN (sealing follows the returncode and target checks).
Tolerance / quadrature / basis-key pins INTACT.
```

## Protected status

```text
cycle7_verdict = NO_GO
verdict_item_1_fence_at_rest = CLOSED       (0555 both, assertion fires)
verdict_item_2_manifest_v006 = CLOSED       (642d10c0…, 12 rows, sealed)
verdict_item_3_verification_return = CLOSED (this artifact + verbatim txt)
fence_at_rest_mode_observed = 0555
fence_reopening_attributable_to_program_route = false
fence_reopening_external_actor_identified = false
manifest_v006_sealed = true
manifest_v006_sha256 = 642d10c0ef86020e3377695ebc9544427e4df363f31d56a9e96a48bf3da1b212
preflight_independent = PREFLIGHT_OK
preflight_primary = PREFLIGHT_BLOCKED_lane_order
preflight_comparison = PREFLIGHT_BLOCKED_lane_order
preflight_ok_is_startability_evidence = false
real_chain_passes = false
comparison_capable_of_passing = false        (additional GO requirement)
thirty_four_component_diagnosis_owner = independent_lane
numerical_values_adjusted_by_this_lane = none
rehearsal_rerun_by_this_lane = false
production_gate_verdict = NO_GO
production_authorized = false
typed_authorization_recorded = false
alpha_computed = false
proof_authorized = false
```
