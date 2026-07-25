# Stage-8 Verification-Phase Charters (pre-staged)
Fable lane · 2026-07-24 evening · ready-to-launch the moment Stage-8 execution completes
Purpose: the sealed battery requires three NEW unanimous core reports in the
SEALED roles (not the Stage-7 supervision roles), plus one independent
full-chain reconstruction, plus the blind lanes. These charters are frozen
now — before any execution outcome is known — so the reviewers' scope cannot
be shaped by results.

## Launch conditions
Fire when: every T-report and NC-report exists content-addressed in
stage8_execution/, the dependent T-chain is complete (or the execution is
declared final with named blocks), and the evaluator's inputs are in place.
Do NOT fire on a partial execution unless Codex declares it final.

## Lane 1 — Formal type/category review (sealed role: formal)
Fresh context. Charter: verify every object in the T0–T16 chain is
well-typed against the sealed definitions — carriers, tensor factors,
domain/codomain of every map (especially the relay isometry
R_c: L_p → E_c ⊗ L_r and the amplitude functional's type), the
content-address schema of every report, and that no obligation's claimed
type exceeds its authority (the day's recurring failure mode: operator
mistaken for scalar; endomorphism mistaken for map-into-parent). Verdict
PASS / NO-CORE-RESULT-SEAL with the sealed 10-field report schema
(schema_version, bundle hash, stage, reviewer_role=formal, process_id,
verdict, blockers, full_matrix_attestation, no_edit_attestation,
artifact_hashes, created_utc).

## Lane 2 — Physics/operator review (sealed role: physics_operator)
Fresh context. Charter: verify the physics content — self-adjointness and
propagator claims at the strength actually proven (mild vs strong), the
inherited-state legitimacy (restriction-not-selection; the fiberwise
caveat recorded, not hidden), pointer persistence and causal-order claims,
the amplitude's reduction to the pinned one-handle value, and that every
negative control exercised real physics (the packing-dependent variant
FAILED for the right reason; the cos(Nτ_R A) control behaves). Same report
schema, reviewer_role=physics_operator.

## Lane 3 — Independent full-stack RED-TEAM (sealed role: red_team)
Fresh context, maximum hostility. Charter: assume the execution is wrong or
gamed and try to prove it. Priority attack surfaces (from the day's record):
(1) any place a discretionary choice survived the F-family resolution;
(2) the transform fence — grep every artifact for kappa's digit string and
elementary transforms including 1/(4π·κ); (3) the prediction file — lexical
check that no undisclosed numerical prediction was recorded; (4) commitment/
reveal ordering on every blind lane; (5) the tautology class — any verifier
that constructs what it then checks (the layer-6 catch); (6) cross-hash
combination (V011 2081); (7) result-awareness — any spec written after its
own exploratory result without disclosure. One confirmed exploit =
NO-CORE-RESULT-SEAL. Same schema, reviewer_role=red_team.

## Lane 4 — Independent full-chain reconstruction
Fresh context. Rebuild T0 → kappa_record from the sealed spec text ONLY
(no execution artifacts), using the Frozen Numerics rules (odd-L schedule,
exact rational arithmetic, certified enclosures). Must reproduce
kappa_record within the enclosure-intersection rule. Emits a salted
commitment BEFORE seeing any produced value.

## Blind numeric lanes (fire per-object as T-reports land, if not already run)
- T13 family A (cubical bisection) and family B (simplicial/barycentric):
  two mutually blind fresh lanes; commitments before reveal.
- Every undisclosed load-bearing value (T7 limits, T14 kappa components):
  independent reproduction with commitments.

## Evaluator run
After all reports land: the sealed evaluator
(stage8_battery_evaluator_v001.py, hash b053b4b1…) is run with --selftest
first (recorded), then on the execution directory. ITS output is the Stage-8
verdict. No human or model summary may precede or paraphrase it in any
sealed artifact.

## Unanimity and veto
Any lane returning NO-CORE-RESULT-SEAL blocks. Disagreement is reconciled
append-only or Stage 8 closes blocked. No majority vote. No report reuse
from Stage 7 ("no stage may inherit a review from an earlier stage").
