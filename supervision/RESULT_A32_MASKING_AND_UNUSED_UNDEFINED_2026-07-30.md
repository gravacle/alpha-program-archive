# SLOT 18: "UNUSED" IS UNDEFINED, AND A32's MASKING DISCIPLINE IS NOT ESTABLISHED AS COMPLIANT

Reviewer verification of Codex lane 2's paste-132 return, plus one deviation the lane did not name.
2026-07-30. Both lane hashes verified (`3a1a9d98…`, `880575cb…`); the custodian directory is untracked,
unread by this lane, and absent from every tracked path.

## 1. VERIFIED: "UNUSED" HAS NO SEALED DEFINITION

The obligation, `STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V002.md:119-139`: "and one **unused**
structure-sensitive prediction."

The nearest sealed conditions, `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:2080-2089`:
"be absent as an outcome or target from the complete historical lineage" and "be structure-sensitive:
BID and at least one preregistered comparator calibrated to the same alpha must make distinct
predictions."

**Nothing in the bounded two-root search equates those conditions with "unused" or supplies a
machine-testable predicate.** So "structure-sensitive" IS operationally defined and "unused" is NOT.
Slot 18's admissibility condition is therefore half-written, and slot 18 is what `FINAL-CLAIM` rests on.

CONSEQUENCE FOR THE Q-18 CHAIN, which is why this matters beyond slot 18: Q-18 established that alpha's
conditionality equals the induced-only axiom's status, and that slot 18 is the mechanism that would EARN
that axiom. **An earning mechanism with an undefined admissibility condition cannot be relied on to
earn anything.** The chain Q-18 → Q-22 assumed slot 18 was well-posed. It is not, yet.

DISPOSITION: defining "unused" is a PRINCIPAL ACT. It cannot be a lane definition, because a lane
choosing the predicate that decides which predictions are admissible is selecting the test after seeing
the candidate space.

## 2. VERIFIED AND EXTENDED: THE MASKING DISCIPLINE

The requirement, `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:2008-2011`, rule 9 verbatim:

> "Custodian commitments: **independent custodian**, one 256-bit salt per candidate from auditable
> external randomness or hardware entropy. Payload = RFC-8785 JSON of canonical outcome value,
> uncertainty, **covariance**, units, source identifier. Commitment =
> SHA256(salt || RFC8785(canonical_outcome_payload)). **Custodian attests that no payload was
> disclosed.**"

Against `a32_holdout/collector_v001.py:301-326`, which I read directly:

**(a) CONFIRMED — THERE IS NO INDEPENDENT CUSTODIAN.** One program, in one run, reads
`/dev/urandom` for the salts, writes `custodian_private/custodian.jsonl` containing **both payload and
salt**, and writes the public `commitments.jsonl`. The lane's phrasing was careful and correct: this
does not disprove an independent operator, but the inspected evidence does not establish
process/operator independence. I would put it more sharply on one point — **"Custodian attests that no
payload was disclosed" cannot be satisfied by self-attestation.** An attestation by the party that
generated the payloads is not the thing rule 9 asks for.

**(b) NOT CONFIRMED AS A DEFECT — the salt source is arguably compliant.** Rule 9 permits "auditable
external randomness **or** hardware entropy." `/dev/urandom`, 32 bytes, with a fail-closed short-read
check, plausibly satisfies the second disjunct. It leaves no audit trail, so it fails the first. Since
the requirement is disjunctive, I do not call this a violation. **Recorded so nobody later claims the
salts were non-compliant.**

**(c) NEW — THE COMMITTED PAYLOAD OMITS COVARIANCE, AND THIS ONE HAS TEETH.** The code builds:

```
payload_obj = {"source_id": SOURCE_ID,
               "uncertainty": uncertainty,
               "units": units,
               "value": value}
```

Four fields. Rule 9 requires five: value, uncertainty, **covariance**, units, source identifier.
**Covariance is not in the payload, so the commitment does not bind it.**

*** WHY THAT IS NOT COSMETIC: THE DISTINCTNESS STATISTIC CONSUMES COVARIANCE. *** `V011:2052-2058`
defines `D = |mu_BID - mu_comp| / sqrt(sigma_BID^2 + sigma_comp^2 + sigma_meas^2)` "after unit conversion
and **covariance projection**." If covariance is not bound by the commitment, then the covariance used in
the projection can be supplied after the prediction exists. **That is a post-hoc freedom inside the one
mechanism whose entire purpose is to remove post-hoc freedom.**

Two innocent readings exist and neither is established: the observables may all be scalar, so covariance
is vacuous; or covariance may be carried elsewhere. **Either would be fine and neither is recorded.**
Until one is shown, the holdout's binding is narrower than its spec.

## 3. THE OTHER STRUCTURAL FACTS, VERIFIED FROM THE LANE'S CITATIONS

- **The 355 rows are NOT the eligible universe.** `collector_v001.py:27-31`: "Lineage exclusion is
  executed later at the eligibility stage… No row was dropped for content." And
  `provenance/bid_stage_subjects_v011.json:22-24`: "No sealed HOLDOUT-UNIVERSE-SEAL immutable subject
  exists." So the universe is collected, not sealed.
- **A32 is ratified but not attained.** `A32_FREEZE_V002_RATIFIED_2026-07-28.md:1-8`: "SPEC-SEAL becomes
  ATTAINABLE, not attained."
- **No concrete comparator exists.** "Same-alpha comparator" is defined as a CLASS — published QED/SM
  expression, identical alpha input, frozen formula-specific order, no candidate-specific fitting — with
  no publication, expression, order, or payload found.
- **`D` is not a comparison to a measured central value.** Measurement enters only through
  uncertainty/covariance. That is a fence-relevant clarification worth keeping: computing `D` does not
  breach the no-comparison fences.
- **The eligible set cannot be shown non-empty before predictions exist**, since eligibility requires
  distinct BID/comparator predictions and `D` consumes both predicted means. No sealed
  `PREDICTION-MAP-SEAL` subject exists either.
- **No impossibility.** Six typed non-alpha output families exist (finite holonomy response,
  temporal-plaquette/connected-kernel susceptibility, flux/retarded response, causal-record durability,
  charged spectrum/threshold response, magnetic form-factor channels), each with its required derivations
  listed.
- **A masking-assurance warning was raised honestly.** A structure-only probe detected a numeric-looking
  candidate-definition suffix; the lane stopped, reproduced nothing, and inferred nothing. **That is the
  correct behavior and it is a second, independent reason to look at masking.**

## 4. WHY THIS IS TIME-SENSITIVE RATHER THAN MERELY IMPORTANT

**A holdout committed late is VOID, not merely weaker.** If the masking discipline has to be redone with
an actual independent custodian, that re-collection must happen before any prediction exists — and both
construction lanes are now working toward predictions. A masking defect found today is cheap. The same
defect found after alpha exists cannot be repaired at all, because re-committing a holdout after seeing
the theory's output is worthless.

## 5. WHAT IS OWED, AND TO WHOM

**PRINCIPAL:** (1) define "unused" as a machine-testable predicate, or rule that the sealed
"absent from the complete historical lineage" condition IS the definition and record that identification;
(2) rule on the custodian independence question — accept the current arrangement with the limitation
recorded, or require re-collection under an independent custodian; (3) rule whether covariance must be
added to the committed payload, which likely forces re-commitment.

**LANE:** nothing until those are ruled. Slot 18 cannot proceed to a prediction while its admissibility
predicate is undefined, and it should not proceed to a commitment whose binding is under review.

## 6. SCOPE

- Discharges no slot. Zero of eighteen remain derived.
- Computes nothing; compares nothing to any measured value.
- Does NOT claim the holdout is compromised. It claims compliance is not ESTABLISHED, on two specific
  points, one of which (covariance) has an innocent reading nobody has recorded.
- Reads no candidate content and no custodian payload. `custodian_private/` was not read, listed,
  statted, hashed, or staged by this lane or by lane 2.

`alpha_computed = false`; `proof_authorized = false`; `kappa_record_computed = false`.
