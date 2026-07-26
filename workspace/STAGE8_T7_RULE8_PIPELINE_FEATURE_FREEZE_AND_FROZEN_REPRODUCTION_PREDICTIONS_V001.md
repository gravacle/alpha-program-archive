# Stage-8 T7 Rule 8 — Pipeline Feature Freeze, and Frozen Predictions on the Cold-Reproduction Attempt V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY STANDING RULE + FROZEN PREDICTIONS SEALED BEFORE THE
INDEPENDENT LANE REPORTS.
Cites STAGE8_T7_RULE7_ORDERING_AUTHORITY_AND_TIMESTAMP_CLAIM_AUDIT_V001.md
and the v003 authorization 810467de9d8274e5… (which this artifact does NOT
reopen). PRODUCTION REMAINS PROHIBITED ON BOTH GATES.
```

## RULE 8 (PIPELINE FEATURE FREEZE) — standing, effective immediately

```text
THE PRINCIPAL'S REASONING, RECORDED BECAUSE IT IS THE JUSTIFICATION AND
NOT MERELY THE ORDER: six audit cycles, and EVERY BLOCKING FINDING WAS IN
THE PIPELINE. ZERO WERE IN THE PHYSICS. Seven generations of
launcher/controller/comparator now exist to run two calculations and
compare them. Each integrity mechanism ADDED SURFACE THAT ITSELF NEEDED
VERIFYING — the directory fence took eighteen probes; the manifest bridge
created the quarantine row conflict; sealing manifest v006 made the sealed
rehearsal harness unrunnable. THE MARGINAL FENCE NOW COSTS MORE THAN THE
RISK IT REMOVES.

PERMITTED FROM HERE, AND NOTHING ELSE:
  - derive-primary v003 EXACTLY as authorized (resolution ladder only;
    conditions A1-A4 binding);
  - repairs to defects found by audit;
  - nothing else. NO new fences. NO new generations for convenience. NO
    new provenance mechanisms. NO hardening of things that are not broken.
IF A NEW MECHANISM SEEMS REQUIRED: DO NOT BUILD IT. Bring the principal
the RISK IT REMOVES and the VERIFICATION BURDEN IT ADDS. THE DEFAULT
ANSWER IS NO.
```

### This lane's acknowledgement, since it built most of the surface

```text
The three examples in the reasoning are all this lane's: the eighteen
fence probes, the bridge/quarantine conflict, and the harness break — the
last of which this lane reported itself, one paste before the freeze. The
pattern was visible from inside and was not acted on from inside. Rule 8
is accepted without qualification, and this lane records that the correct
time to have proposed it was several cycles ago.
ONE STANDING CONSEQUENCE, so the rule is self-enforcing rather than
remembered: any future artifact by this lane that adds a mechanism must
name Rule 8 and show the principal's authorization by hash, or it is
itself a defect.
```

## WHERE THE FREED CAPACITY GOES — and this lane's part

```text
1. REPRODUCIBILITY BY A STRANGER. The real guarantee is not that ordering
   can be shown; it is that a third party can re-run the work FROM THE
   PUBLIC ARCHIVE and land on the same numbers. The independent lane is
   attempting exactly that, COLD, from the public repo only.
2. NEGATIVE CONTROLS. An instrument is trusted because IT FAILS CORRECTLY,
   not because of its build history. Every control that provably bites
   RETIRES a piece of the provenance apparatus. The independent lane is
   finding which controls are MISSING.
THIS LANE'S PART, as directed: when gaps come back in either, fixing them
takes PRIORITY over anything else in the pipeline, and CLOSING A CONTROL
GAP COUNTS AS RETIRING PROVENANCE BURDEN, NOT AS ADDING WORK.
```

## FROZEN PREDICTIONS on the cold-reproduction attempt

Sealed BEFORE the independent lane reports, and deliberately NOT acted on.

```text
WHY THIS LANE IS NOT PRE-EMPTIVELY FIXING THE ARCHIVE: the value of a cold
attempt is discovering what is missing. Repairing the reproduction path
first would spoil the only instrument that can measure it. So the analysis
is FROZEN AS PREDICTIONS instead — testable, and scored when the lane
returns.

P-X1  THE PINNED RUNTIME IS NOT IN THE ARCHIVE AND IS NOT OBTAINABLE FROM
      IT. Every production invocation uses
      /Users/bgm/.cache/codex-runtimes/codex-primary-runtime/dependencies/
      python/bin/python3, which lives OUTSIDE the repository. REPRODUCING.md
      says only "a pinned 3.12.13 runtime" and gives no source, version
      pin, or hash. A stranger cannot obtain it. Confidence: HIGH.
P-X2  RUNTIME ATTESTATION WILL BLOCK A STRANGER OUTRIGHT, and this is the
      structural finding. Precondition #1 is runtime_attestation, and
      provenance/stage8_t7_numpy_runtime_manifest_v001.json hashes 899
      numpy files. ANY stranger whose numpy is not byte-identical fails at
      precondition 1 and never reaches a number.
      *** THE INTEGRITY MECHANISM IS IN DIRECT TENSION WITH
      REPRODUCIBILITY-BY-A-STRANGER: the pipeline is, BY DESIGN, runnable
      only on this machine's exact bytes. That is the sharpest instance of
      Rule 8's reasoning that exists, and it was built by this lane. ***
      Confidence: HIGH.
P-X3  REPRODUCING.md IS STALE WITH RESPECT TO THE WHOLE G7 PIPELINE. It
      documents the v011 gates, the Stage-6 ledger, the blind lanes and
      the evaluator, and says NOTHING about launcher/controller/comparator,
      manifests, the bridge, generations, the fence, or how to run the CAR
      comparison at all. A stranger following it would verify seals
      successfully and never reach the pipeline. Confidence: HIGH.
P-X4  SEAL VERIFICATION ITSELF WILL SUCCEED. shasum -c from the containing
      directory works on the whole corpus, and this lane's own coverage
      sweep found 100% coverage of post-custody artifacts. The stranger
      will be able to verify WHAT WAS CLAIMED even where they cannot RERUN
      it. Confidence: HIGH.
P-X5  THE DISTINCTION THE ATTEMPT WILL FORCE, predicted as the useful
      outcome: "reproducible" splits into (i) VERIFY THE RECORD — works
      today; (ii) RE-DERIVE THE MATHEMATICS independently from the sealed
      specs — works today, and is what the independent lane has repeatedly
      done; (iii) RE-RUN THE PIPELINE BIT-FOR-BIT — does NOT work for a
      stranger, by construction. This lane predicts the returned gaps will
      be concentrated almost entirely in (iii). Confidence: MODERATE-HIGH.
P-X6  MAGNITUDE, stated with this lane's standing calibration — every
      prediction it has made about how big a nonzero effect would be has
      missed, so weight this weakly and credit a landing weakly: the
      number of distinct BLOCKING reproduction gaps returned lands in
      3..8. Deliberately wide.
```

## FROZEN PREDICTIONS on the missing negative controls

```text
P-Y1  THE LARGEST CONTROL GAP IS THAT NOTHING TESTS THE COMPARATOR AGAINST
      A KNOWN-WRONG BUNDLE. Every control this lane built tests PROVENANCE
      (wrong launcher, wrong manifest, skewed pin, superseded route) or
      ORDERING (lane order, receipt order). This lane can name no control
      that perturbs a NUMBER in a bundle and demonstrates the comparator
      reports BLOCKED for that reason — i.e. nothing shows the machinery
      would catch a wrong ANSWER, as opposed to a wrong PEDIGREE.
      Confidence: HIGH. This is offered as the single most likely finding.
P-Y2  A SECOND GAP: no control demonstrates that a PASS is reachable at
      all. The comparison has never returned PASS in this program's
      history. A verdict function whose accepting branch has never
      executed is untested in the direction that matters most — and P-D2
      predicts N_t = 96 will exercise it for the first time.
      Confidence: MODERATE-HIGH.
P-Y3  A THIRD: the |dlam| = 0 rows sit at 3e-13..6e-9, five orders inside
      budget, and NOTHING checks that a component in that class WOULD fail
      if it were wrong. Those rows are the offset bound the whole (b)
      diagnosis rests on, and they are the least-controlled rows in the
      table. Confidence: MODERATE.
P-Y4  PREDICTED NON-GAP: the fence controls are OVER-covered, not under-.
      Eighteen probes plus the rehearsal's write-attempt verification.
      This lane predicts the independent lane finds NO missing fence
      control and possibly says so explicitly. Confidence: MODERATE.
      Stated because a prediction that a gap will NOT be found is scoreable
      and this lane's apparatus-building bias runs the other way.
```

## Protected status

```text
rule8_pipeline_feature_freeze_adopted = true
new_mechanisms_permitted = false
v003_permitted_as_authorized = true
audit_defect_repairs_permitted = true
reproduction_path_pre_emptively_repaired = false   (deliberate; would
                                                    spoil the cold test)
P_X1..P_X6_frozen_before_return = true
P_Y1..P_Y4_frozen_before_return = true
control_gap_closure_counts_as_burden_retirement = true
v003_authorization_reopened = false
P_D1_P_D2_P_D3_reopened = false
production_authorized = false
alpha_computed = false
proof_authorized = false
```
