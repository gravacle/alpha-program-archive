# Findings Against the Canonical Master Plan V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY FINDINGS. Reported under PART E CLAUSE 2 of the canonical plan:
"Any lane finding this plan wrong reports it as a finding and does not act
on the correction until the principal rules."
THE PLAN IS NOT EDITED. THIS LANE CONTINUES WORKING TO IT AS SEALED.
Plan cited by hash:
  STAGE8_MASTER_PLAN_TO_ALPHA_V001.md
  12f204c64f0c0fd92cc77527309deb48e48610eb78772500870a1cfb884708dd
  201 lines / 12209 bytes
PRODUCTION PROHIBITED. alpha_computed = false.
```

## F-1 — INTERNAL INCONSISTENCY: the plan states the independent family's record as both three and four

```text
SEVERITY: MAJOR. It is the ground of a standing rule.
PART F:  "...three consecutive cycles in this one where the independent
          family was right and the construction lane was not."
PART G:  "CODEX ... Best record in the program: four consecutive prediction
          cycles landed."
THE LEDGER, verified: FOUR. P-C5, P-C6, P-C7 and P-C8 have all landed with
explicit constructions; CALIBRATION_LEDGER.md reads "P-C7 and P-C8 landed
with explicit constructions. FOUR CONSECUTIVE CYCLES". P-C8 (the D3 object:
volume weight survives slivers and is derivable; response pullback not
automatically proved) landed on BOTH clauses earlier today.
SO PART G IS RIGHT AND PART F UNDERCOUNTS BY ONE.
WHY IT MATTERS RATHER THAN BEING PEDANTRY: Rule 6's weighting obligation is
grounded on that count, and the recovery judgment is the principal's ON THE
REVIEWER LANE'S READING OF THE LEDGER. A canonical plan that states the
count two different ways gives a future lane a choice of grounds, which is
exactly what Rule 6's amendment closed.
NOT ACTED ON. This lane continues to weight the independent family at the
ledger's four, because the ledger is the sealed authority Rule 6 names —
and records here that it is doing so against Part F's number.
```

## F-2 — STALE SIZING: Part G's step-4 precondition has been met without producing the enabling condition

```text
SEVERITY: MAJOR, because it makes a critical-path item look ready when it
is not.
PART G:  "| 4 C_ref/D3 | S once sliver returns | Brian | method already set |"
THE SLIVER ATTEMPT HAS RETURNED. Verdict:
UNDETERMINED_ON_SEALED_INPUTS (STAGE8_T7_SLIVER_NATURALITY_ATTEMPT_RESULT_
V001, and the addendum). It did NOT settle C_ref/D3: neither of the
principal's two branches is earned — the broad class is not vindicated and
the restriction is not earned, because no counterexample was produced.
AND the sliver work established something stronger that bears on step 4
directly: RESTRICTING TO C_ref WOULD NOT RESCUE THE OBJECT (R-L0 and R-L2b
are word-for-word the same obligations on C_ref, and the one recorded
alpha = 0 pathology arises under isotropic dilation, INSIDE the
shape-regular class).
SO step 4 is not "S once sliver returns". The sliver returned; step 4 is now
blocked on step 1 (the transport rule) instead, and Part A4's own text
already says step 4 is "currently deferrable". Part G's row contradicts
Part A's disposition.
NOT ACTED ON. Step 4 stays where the plan puts it in the ordering.
```

## F-3 — UNDER-SCOPED SEALED STEP: Part B step 2 drops two of its three clauses

```text
SEVERITY: MINOR in wording, but Part B is marked [SEALED] and lanes will
work to it, so an under-scoped step under-scopes the work.
PART B:  "2. Gauge fixing"
THE SEALED SOURCE, EM_DEPENDENCY_ORDER_FREEZE_V001 verbatim:
         "2. gauge fixing, ghosts, and gauge edge modes;"
GHOSTS and GAUGE EDGE MODES are dropped. Edge modes in particular are not a
detail in a cellular/boundary-incidence setting — they are where boundary
degrees of freedom live, and this program is a boundary-incidence theory.
NOT ACTED ON. Recorded so that whoever executes step 2 reads the freeze,
not the plan's compression of it.
```

## F-4 — CITATION HAZARD: "A4" names two different things

```text
SEVERITY: MINOR, but Part E clause 5 requires lanes to cite this plan, so
ambiguous labels will propagate into artifacts.
PART A SECTION "A4" = Battery, steps 17-21.
PART A STEP 23     = "A4 audit" — which is CONDITION A4 of the v003
                     authorization (the full audit of v003 before
                     production), an entirely different object.
A lane writing "per A4 of the master plan" is ambiguous between the battery
section and the v003 audit condition.
NOT ACTED ON. This lane will disambiguate in its own artifacts by writing
"Part A section A4 (Battery)" or "v003 condition A4 (audit)" and never the
bare token.
```

## F-5 — PRECISION: "Stage 10 — ZERO files" is true only of one spelling

```text
SEVERITY: MINOR.
PART D:  "Stage 10 — ZERO files. Appears only as a scoping adjective."
MEASURED: "Stage 10" (space) -> 0 files. "Stage-10" (hyphen) -> 4 files, in
EM_DEPENDENCY_ORDER_FREEZE_V001, both battery specs, and
STAGE7_QSPEC_SCOPE_AND_PREMISE_SUCCESSOR_V001.
The two sentences together are accurate — the second concedes the
hyphenated occurrences — but "ZERO files" read alone would support the false
claim that the label never appears. It appears four times and its
guardrails BIND.
NOT ACTED ON. Flagged only so no lane cites "Stage 10: zero files" as
evidence that nothing constrains Stage 10.
```

## VERIFIED CORRECT — one thing this lane doubted and checked

```text
PART C's arithmetic firewall, marked [SEALED]: "no function of it may ever
be computed (explicitly including 1/(4π·κ))".
THIS LANE DOUBTED THE PARENTHETICAL AND VERIFIED IT. The battery spec
authority contains, verbatim: "composition — explicitly including
1/(4π·kappa_record)) may be computed". THE [SEALED] MARKING IS CORRECT and
the clause is quoted faithfully. Recorded because a doubt raised and then
resolved against itself belongs on the record as much as a defect does.
```

## A HAZARD THE PLAN DOES NOT NAME — offered as an observation, not a defect

```text
kappa_record AND kappa_Thomson ARE DIFFERENT QUANTITIES, and conflating
them would BE the firewall violation.
  the firewall forbids computing any function of kappa_record, explicitly
  1/(4π·kappa_record);
  but the sealed audit matrix A28 reads: "Only kappa_Thomson may enter
  alpha(0) = 1/(4π kappa_Thomson)";
  and V011: "alpha(0) = e^2/(4 pi) = 1/(4 pi kappa_Thomson)".
So alpha is reached from kappa_THOMSON — obtained downstream through Part B
step 8's Thomson matching, itself conditioned on step 7's pole-vs-
infraparticle outcome — and NOT from Stage 8's kappa_record. The plan is
correct that step 8 is "the nearest thing to alpha appears"; it simply does
not say that the kappa entering alpha there is a DIFFERENT kappa.
WHY IT IS WORTH NAMING: the two symbols differ by one subscript, the
formula 1/(4π·kappa) is identical in shape for both, and one of them is
forbidden to compute while the other is the goal. That is a well-formed trap
for any lane reading quickly, including this one.
NOT A FINDING AGAINST THE PLAN. Offered for the principal's judgement as to
whether the canonical plan should say it.
```

## Disposition

```text
plan_edited = false
plan_hash_cited = 12f204c64f0c0fd92cc77527309deb48e48610eb78772500870a1cfb884708dd
findings_reported = 5   (1 MAJOR ledger-count inconsistency, 1 MAJOR stale
                         sizing, 3 MINOR)
verified_correct_against_this_lane_s_doubt = 1
unnamed_hazard_offered = 1   (kappa_record vs kappa_Thomson)
acted_on_without_ruling = none
this_lane_continues_to_plan_as_sealed = true
production_authorized = false
alpha_computed = false
proof_authorized = false
```
