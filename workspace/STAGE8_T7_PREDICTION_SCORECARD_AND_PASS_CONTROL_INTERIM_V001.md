# Stage-8 T7 Prediction Scorecard (G1/G2/G3), and PASS-Control Interim Record V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY. Two parts: (1) this lane's P-X/P-Y predictions SCORED against
the independent lane's G1/G2/G3 returns, including the misses; (2) the
PASS-reachability control IS NOT COMPLETE — interim state, two obstacles,
corrected design. NOT a result. NOT a clearance.
Cites STAGE8_T7_RULE8_PIPELINE_FEATURE_FREEZE_AND_FROZEN_REPRODUCTION_
PREDICTIONS_V001.md, in which P-X1..P-X6 and P-Y1..P-Y4 were sealed BEFORE
the independent lane reported.
PRODUCTION REMAINS PROHIBITED ON BOTH GATES.
```

## PART 1 — SCORECARD

```text
P-X1  pinned runtime outside the archive, no source/version/hash in
      REPRODUCING.md                                              HIT
      G1: "Scripts hard-code ... the pinned Codex runtime path. Not
      relocatable."
P-X2  runtime attestation blocks a stranger outright (899 hashed numpy
      files at precondition 1)                    HIT ON THE WALL,
                                                  NOT INDEPENDENTLY
                                                  CONFIRMED ON MECHANISM
      G1 found "no environment lock" and "not relocatable" — the same wall
      from outside — but did NOT single out the attestation. This lane
      claims the wall, NOT the mechanism, and records that a prediction
      confirmed only by a differently-described finding is weaker evidence
      than one confirmed in its own terms.
P-X3  REPRODUCING.md stale on the entire G7 pipeline                HIT
      G1: no invocation DAG, evaluator inputs incomplete, environment
      described only at a high level.
P-X4  "seal verification itself will SUCCEED"                    *** MISS ***
      G1: the documented per-seal procedure FAILS FOR 36 OF 505 seal files.
      INDEPENDENTLY RE-MEASURED BY THIS LANE, and it is worse under a
      stricter predicate: 71 OF 507 seal files fail the documented
      containing-directory procedure. The two counts differ because the
      predicates differ — many cleanroom_output seals are not
      "sha256  filename" at all but "sha256  ISO-8601-TIMESTAMP", a format
      `shasum -c` cannot consume in any working directory.
      *** WHY THIS MISS IS THE WORST ONE IN THE SET: this lane HIT THIS
      EXACT BUG ITSELF, earlier in the session, when `shasum -c` failed on
      a basename-relative seal and the fix was to cd into the containing
      directory. It was recorded as a personal tooling quirk and NOT as an
      archive defect. Same class as the other three defects this lane has
      logged today: THE EVIDENCE WAS IN FRONT OF ME. Fourth instance. ***
P-X5  three-way split, gaps "concentrated almost entirely in (iii)
      re-run-bit-for-bit"                    SPLIT HIT / CONCENTRATION MISS
      The split is confirmed and the principal calls it broadly right. The
      CONCENTRATION clause is wrong: 71 failing seals are a defect in
      (i) VERIFY-THE-RECORD, the leg this lane predicted was clean.
P-X6  3..8 blocking gaps                                            HIT
      G1 names 7. Inside the window — and per this lane's standing
      calibration, CREDITED WEAKLY: the window was deliberately wide.
P-Y1  nothing tests the comparator against a known-wrong bundle     HIT
      G2 gap (5): a predeclared honest-resolution scaling control whose
      expected difference is above/below budget BEFORE production.
      Authorized by the principal, lower priority.
P-Y2  no control demonstrates a PASS is reachable at all      HIT, AND NOT
                                                              FOUND BY THE
                                                              INDEPENDENT LANE
      The principal calls it "the most important sentence in the return".
      Two lanes, two different gaps, both real. This is the only item in
      the set that is uniquely this lane's.
P-Y3  the |dlam| = 0 rows are the least-controlled rows            OPEN
      Not in G2's list; neither confirmed nor refuted. Remains this lane's
      open suspicion and is NOT counted as a hit.
P-Y4  predicted NON-gap: fence controls are OVER-covered            HIT
      G2 credits "directory-fence probes" among controls that DO bite and
      names no fence gap. Recorded because it was a prediction AGAINST this
      lane's own apparatus-building bias, and those are the ones worth
      scoring.
G3    "prerequisite, not identity" for T11 / Q6 / A-L5              HIT
      CONFIRMED, and the shared object is now NAMED by the independent
      lane: D3_REFINEMENT_NATURAL_VOLUME_WEIGHT_AND_RESPONSE_PULLBACK_V001
      — it IS T11's open object, it makes recast Q6 WELL-POSED, and it
      supplies the measure side of A-L5. Shared missing OBJECT, not shared
      obligation, not sufficient alone. Recorded as ONE named obligation
      feeding THREE. NOT to be specced now (pipeline first).
```

```text
TALLY: 6 clean hits, 1 hit-on-the-wall-only, 1 split verdict, 1 clean and
       instructive MISS, 1 open.
THE MISS IS THE USEFUL PART. P-X4 was the one prediction where this lane
asserted its own apparatus was sound, and it was the one that was wrong —
about a bug it had personally encountered and misfiled.
```

## PART 2 — PASS-REACHABILITY CONTROL: INTERIM, NOT COMPLETE

```text
WHAT IS ESTABLISHED, and it enlarges the problem:
THE ACCEPTING BRANCH IS BIGGER THAN "EMIT A VERDICT". After
require(not failures) the comparator runs FIVE further gate functions and
then assembles and seals the PASS record:
    validate_lane_diagnostics
    piece_authenticity gate
    tied_diagnostics gate
    generator_propagator_lineage gate
    validate_current_route2_route1_reduction
NONE OF THESE HAS EVER EXECUTED IN THIS PROGRAM'S HISTORY. The unmeasured
surface is five gates plus the PASS-dict assembly plus the sealed write,
not one branch.

TWO OBSTACLES HIT, BOTH THEMSELVES FINDINGS:
 O-A  THE COMPARATOR REFUSES DIRECT INVOCATION. Imported and called
      directly it raises ComparisonBlocked: "comparison requires the
      sealed Stage-8 runtime launcher". Correct behaviour — precondition 1
      again — but it means the control cannot be a small standalone call:
      it must go through the launcher, and therefore also satisfy the
      CONTROLLER's receipt and provenance chain.
 O-B  THE PIPELINE'S OUTPUTS ARE WRITTEN READ-ONLY (0444) INSIDE A 0555
      FENCE, so constructing a synthetic input requires deliberately
      opening them in the disposable copy.
 TOGETHER THESE ARE THE REASON THE ACCEPTING BRANCH HAS NEVER RUN: THE
 PROVENANCE MACHINERY ACTIVELY RESISTS CONSTRUCTING A PASSING CASE. That
 is by design and it is not a defect — but it means "compare a bundle with
 itself" is NOT a cheap control here, and the cost belongs on the record
 next to Rule 8's reasoning.

THE CONSTRUCTION IS SOUND WHERE IT WAS TESTED:
 back-transporting the primary into a synthetic independent by
 M_ind := O^H M_prim O, with O the pinned basis overlap, is exact —
 MEASURED UNITARITY RESIDUAL OF O: 0.0 EXACTLY. So transported == primary
 identically by construction, and unitary conjugation preserves the
 hermiticity, projector, spectral and reconstruction identities the
 internal gates test.

WHY IT IS NOT YET COMPLETE, stated precisely rather than glossed:
 the synthesis matched arrays BY RAW NPZ NAME between the two bundles and
 converted only 6 of them (24 copied, 330 left as the independent lane's
 own). The two lanes DO NOT SHARE ARRAY NAMES for most components — the
 comparator reads matrices by CATEGORY and IDENTIFIER out of each bundle's
 manifest, not by raw array name. A name-matched synthesis therefore
 leaves most transported components untouched and would still fail. THE
 MAPPING MUST GO THROUGH THE MANIFEST'S COMPONENT STRUCTURE.
 NO PASS HAS BEEN OBSERVED. NO CLAIM IS MADE THAT ONE IS REACHABLE.
 EQUALLY, NO CLAIM IS MADE THAT IT IS NOT — the blocking so far is this
 lane's construction being incomplete, NOT the comparator refusing an
 honest agreeing pair.

NEXT STEP, named so it is not rediscovered: rebuild the synthesis to walk
each bundle's manifest component structure (category, identifier) and
back-transport per component, then invoke through the launcher so
precondition 1 is satisfied, accepting that the controller's receipt chain
must also be satisfied or its bypass explicitly disclosed.
```

## Protected status

```text
predictions_scored = true
P_X4 = MISS                       (seal verification does NOT succeed)
seal_files_total_measured = 507
seal_files_failing_documented_procedure = 71
seal_line_pointing_outside_repo = 1
P_Y2_unique_to_this_lane = true
pass_control_complete = false
pass_control_verdict = NONE_OBSERVED
accepting_branch_gates_never_executed = 5
comparator_refuses_direct_invocation = true
synthesis_overlap_unitarity_residual = 0.0
v003_started = false
production_authorized = false
alpha_computed = false
proof_authorized = false
```
