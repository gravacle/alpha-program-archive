# Stage-8 T7 Construction-Lane Erratum — Three Self-Defects, and an Incomplete Review V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY ERRATUM. NOTHING IS PATCHED. Every artifact named below is
preserved exactly as sealed; this document corrects the record.
Three defects are this lane's own. All three were surfaced by the hostile
review and then VERIFIED BY THIS LANE AT SOURCE before being recorded.
A fourth item is a defect in this lane's REVIEW APPARATUS, not in a claim.
```

## DEFECT 1 — the arm-2 binding was never carried into the spec it binds

```text
WHAT THIS LANE SEALED, at 2026-07-26 09:39:15:
  STAGE8_T7_ARM2_SHARPENING_AND_PROJECTION_TAIL_BINDING_V001.md
  (782495eaa9bcfd123803f973ae4346a4cdaa2021a57e0eaba234666f979271e3)
  Its own line 8:  "APPEND_ONLY_BINDING SUPPLEMENT — BINDS THE E1
                    SUCCESSOR SPEC v002 (applied AT SEAL by the
                    construction lane)"
  Its lines 67-70: "THIS DEPENDENCY IS BOUND HERE so no lane discovers it
                    mid-execution. The E1 v002 spec must carry it as an
                    explicit conditional obligation attached to U3, and
                    its verdict language must state which of the two it
                    relies on (uniform-in-Q, or limit-with-certified-
                    tails)."

WHAT THIS LANE THEN SEALED, 17 MINUTES LATER at 09:56:26:
  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md, 2344 lines, containing:
    "ARM2_SHARPENING"        0 occurrences
    "U1" / "U2" / "U3"       0 occurrences
    "Galerkin"               0 occurrences
    "finite-Q" / "finite Q"  0 occurrences
    "projection-tail"        0 occurrences
    "782495ea"               0 occurrences   (no A0 row for the binding)
  And this lane's own seal record
  (STAGE8_T7_E1_SPEC_V002_SEAL_RECORD_AND_RULE6_VERIFICATION_V001.md)
  contains ZERO occurrences of the same seven markers.

SO THE OBLIGATION WAS BOUND IN ONE ARTIFACT AND CARRIED INTO NOTHING.
This lane performed a seal-time verification of that very spec — it
checked 36 A0 hashes and Rule-6 compliance in §P — and DID NOT CHECK
WHETHER THE BINDING IT HAD SEALED SEVENTEEN MINUTES EARLIER WAS
CARRIED. The principal's instruction was explicit: "Bind that dependency
explicitly rather than discovering it at execution." It is bound, and
v002 does not carry it, which is the failure mode the instruction named.

SECOND RECURRENCE OF AN IDENTIFIED CLASS. The A-L0 arm-1 lapse was:
sealed a two-armed obligation one artifact after the erratum whose
witness had already killed arm 1. Both are the same defect —
THIS LANE SEALS AN OBLIGATION AND THEN FAILS TO PROPAGATE IT TO THE
ARTIFACT IT GOVERNS. Once is a slip; twice is a process gap.

A REFUTATION OF THIS FINDING IS ITSELF REFUTED, and recorded because it
nearly buried the defect: a skeptic lane killed the finding on the ground
that the governance legs "were in fact discharged — in the place the
corpus mandates — by an artifact the reviewer did not open." No such
artifact exists. The only candidate was this lane's seal record, and the
marker count above is zero. The finding STANDS.

CONSEQUENCE, NOT REPAIRED HERE: v002 may not be executed until U1/U2/U3
and the U3 projection-tail conditional obligation are carried into its
governing chain by an append-only amendment, with the verdict-language
requirement (uniform-in-Q vs limit-with-certified-tails) stated. U3 is
LIVE, not hypothetical: D6' freezes M(t) = Q 1_{|x|<=r(t)} Q with the
nonlocal projector Q inside the sealed record vertex.
```

## DEFECT 2 — this lane asserted a false negative about the tolerance freeze, in the pessimistic direction

```text
WHAT THIS LANE SEALED, TOLD THE PRINCIPAL, AND PUT IN A COMMIT MESSAGE:
  "*** 3.0e-4 IS NOT STATED IN ANY SEALED PROSE SPEC. It appears nowhere
  in the Phase-A execution binding and nowhere in any sealed .md except
  the cycle-7 coherence table written today. Its 'preregistered' status
  rests on CODE PROVENANCE hashed into sealed manifests, NOT on a spec
  clause. ***"
  (STAGE8_T7_CYCLE7_PACKAGE_RECORD_AND_THREE_FINDINGS_V001.md, and
   restated in STAGE8_T7_CYCLE7_VERIFICATION_RETURN_AND_FENCE_CLOSURE_V001.md)

THAT IS FALSE. VERIFIED AT SOURCE:
  STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md
  (789338adb7d3d36da453113e..., PINNED FOUR TIMES IN v002'S OWN A0 TABLE),
  lines 357-361, in prose, in a sealed spec:
      transported propagator difference                   <=3e-4;
      transported one-particle cross-operator difference  <=3e-4;
      transported direct Kraus-member difference          <=3e-4;
      transported direct response difference              <=3e-4;
      transported aggregate-kernel difference             <=3e-4.
  immediately followed by:
      "No aggregation can hide a component failure. Any one failed
       comparison returns ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_
       BLOCKED."
  THE TWO BUDGETS NAMED FIRST ARE EXACTLY THE TWO FAILING FAMILIES
  (propagators 10 failures, cross_operators 24 failures).

CAUSE, AND IT IS NOT SUBTLE — A PATTERN REGRESSION BETWEEN TWO ATTEMPTS
OF THE SAME SEARCH:
  attempt 1: grep -rln "3\\.0e-4\\|3e-4\\|TRANSPORTED_MATRIX_TOLERANCE" --include=*.md .
             -> died on an unquoted zsh glob, returned nothing
  attempt 2: grep -rln "TRANSPORTED_MATRIX_TOLERANCE\\|3\\.0e-4" . --include="*.md"
             -> THE ALTERNATIVE "3e-4" WAS DROPPED. The spec writes 3e-4.
  This lane then asserted a NEGATIVE EXISTENTIAL from the narrowed
  pattern. A negative existential from a grep is only as strong as the
  pattern, and this lane did not re-read its own pattern before
  publishing the negative.

DIRECTION OF THE ERROR, AND WHY IT STILL MATTERS: it ran PESSIMISTIC. It
invented a weakness in the freeze that does not exist and conceded ground
that did not need conceding. The corrected position is STRONGER, and it
strengthens the 34-failure result as a negative result:
  THE TRANSPORTED BUDGET IS FROZEN AT BOTH LEVELS — in sealed PROSE in
  the Phase-A spec that v002's own A0 pins four times, AND in code
  hash-pinned in sealed implementation manifest v001 generations before
  any comparison result existed. THERE IS NO GAP TO EXPLOIT. Revising
  3e-4 after seeing 34 failures would be outcome-driven revision of a
  budget preregistered in prose in a sealed spec.
Every statement of the "not in any sealed prose spec" claim, wherever it
appears, is WITHDRAWN of record.
```

## DEFECT 3 — a false technical dependency in this lane's own F-3 remediation

```text
WHAT THIS LANE WROTE:
  "(a) restore the at-rest state (chmod 555 on both, or one
  --preflight-only invocation once F-2 is closed, which self-heals and
  records it)" — i.e. that the preflight self-heal route DEPENDED on
  manifest v006 being sealed first.
THAT DEPENDENCY DOES NOT EXIST. Verified in the controller's own frozen
tuple (run_..._v007.py:890-894 and the preflight output this lane itself
printed):
  PRECONDITIONS = (runtime_attestation, generation_coherence,
                   FENCE_AT_REST, IMPLEMENTATION_MANIFEST, ...)
  fence_at_rest is index 2; implementation_manifest is index 3.
The fence self-heal fires BEFORE the manifest check, so
--preflight-only would have restored 0555 and recorded the anomaly with
manifest v006 still absent. The ordering was visible in output this lane
had already printed and did not read against its own claim.
WHAT IS NOT WITHDRAWN: the DECISION not to run it. Declining to settle
two open questions with one unilateral act was and remains sound. Only
the stated technical reason was wrong, and a sound decision resting on a
false reason is still a defect in the record.
```

## ITEM 4 — the review that found these was INCOMPLETE, by this lane's own design error

```text
The hostile pre-execution review produced 55 findings across 8 lanes.
ONLY 6 WERE ADVERSARIALLY TESTED. All 6 came back refuted. 29 non-minor
findings — 7 BLOCKING and 22 MAJOR — WERE NEVER TESTED AT ALL, plus 19
minor ones.
CAUSE: this lane's own workflow contained `.slice(0, 6)` on the set sent
to refutation. The count was logged, but the returned structure reported
"confirmed: 0", which reads as a clean bill of health and is not one.
  A SECOND APPARATUS DEFECT: the dedup key was the first 60 characters of
  the attacked claim, and finding ids were not unique across lanes (three
  separate id collisions: two F2, two F3, two F4). Distinct findings could
  have been collapsed. Triage must key on lane plus content, not on id.
"0 CONFIRMED" IS THEREFORE NOT A CLEARANCE AND IS NOT RECORDED AS ONE.
The spec's hostile-review gate remains OPEN. A completion pass is running
over all 30 untested findings, in topic clusters, with the same
refute-by-default instruction; its verdicts will be sealed either way.
Note on the refutation bias, disclosed: skeptics are instructed to
default to refuted when uncertain. That is deliberate — a false finding
sends a lane to rewrite correct work — but it means a refuted finding is
weaker evidence of correctness than a surviving finding is of defect.
```

## What the review confirmed in this lane's favour, recorded for balance

```text
- The independent-family count of THREE (not two) that this lane
  disclosed at seal was independently found by the review (OA0-6).
- §O.A0's exact arithmetic and §O.A0.1's rational witness reproduce
  exactly; the 9a0c2045 citations say what the spec claims.
- The spec is CORRECT that the star-refinement construction does not kill
  A-L5 — a reviewer reproduced the construction and showed 4-volume
  weighting absorbs the unbounded degree exactly.
- SCAD_is_independent_route = false SURVIVES.
- The E1' min's conditionality bookkeeping does NOT launder the premise
  in the direction feared.
- No prediction in §P was found to have been changed to agree with the
  independent family without an independent ground of its own — the
  deference-vs-calibration check this lane refused to self-certify came
  back clean.
```

## Protected status

```text
arm2_binding_carried_into_v002 = false          (DEFECT 1, open)
v002_executable = false
tolerance_not_in_sealed_prose_spec_claim = WITHDRAWN   (DEFECT 2)
transported_budget_frozen_in_sealed_prose_spec = true
transported_budget_frozen_in_sealed_manifest = true
transported_budget_revisable = false
preflight_selfheal_depends_on_manifest_v006 = false    (DEFECT 3)
f3_remediation_decision_withdrawn = false       (only its stated reason)
hostile_review_complete = false
hostile_review_findings_total = 55
hostile_review_findings_adversarially_tested = 6
hostile_review_findings_untested_nonminor = 29
hostile_review_cleared = false
construction_lane_defect_class_repeat = seal_obligation_then_fail_to_propagate
production_authorized = false
alpha_computed = false
proof_authorized = false
```
