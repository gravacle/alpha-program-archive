# HOSTILE REVIEW — `STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001` — READY_WITH_CONDITIONS

Reviewer lane, 2026-07-30. Subject: `STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md`, sha256
`2d63dfadbb741c467b812f21e14f9e0e66015f1d86e2aa8307d8ae77acfe3d69`, 685 lines, cleanroom sidecar
verifies. Written by Codex lane 1 under relay paste 133.

**VERDICT: READY_WITH_CONDITIONS. TWO CONDITIONS MUST DISCHARGE BEFORE EXECUTION.** Both are cheap now
and expensive later, which is the entire reason a spec is reviewed before it is run.

**INDEPENDENCE LIMITATION, STATED FIRST BECAUSE IT QUALIFIES EVERYTHING BELOW.** I wrote the paste that
specified this spec, and I am now reviewing it. **This review is NOT independent of the specification.**
It can catch internal inconsistency and undefined terms; it cannot catch a defect I built into the
instruction. An independent lane should re-review it. The program has a recorded case of a
cross-family independence claim being false, and I am not adding a second.

## WHAT THE SPEC DOES BETTER THAN IT WAS ASKED TO

Recorded because a lane that strengthens its own constraints should have that noticed, and because
these are the parts a later reader should not weaken.

1. **SECTION 4 CLOSES A FAILURE MODE PASTE 133 DID NOT NAME.** It independently pulled in
   `primitive_zero_bare_induced_response_projection_principle_v004.md:131-138`, whose failure rule reads
   in part: the route fails "if the scalar projection passes while the full operator residual does not."
   The spec therefore requires that "every complementary residual required by the same operator vanishes
   before a scalar root is used." **That is a stronger requirement than I specified**, and it closes the
   most likely way a scalar-root construction produces a number that means nothing.
2. **THREE FALSIFIERS ADDED BEYOND THE FIVE FROZEN IN THE CHARTER:** F-GK6 (old `L_open` route reused),
   F-GK7 (scalar residual defined to pass), F-GK8 (current-carrier conditionality hidden). F-GK8 is the
   right instinct — it makes hiding the Q-22 conditionality a named failure rather than an oversight.
3. **SECTION 2.2 REFUSES TO CHOOSE THE ENERGY AND SCOPES ITS NEGATIVE HONESTLY.** It states the gate's
   five conditions, quotes `E_BY/E_MS = 2/[1+sqrt(1-C)]`, and says plainly that "this spec does not
   choose Misner-Sharp or Brown-York." And its scope line — "this claim is scoped to the cited status
   block; it is not a corpus-wide search claim" — is exactly the discipline the bounded-negative erratum
   was written to install, applied the same day, unprompted.
4. **SECTION 5.1 CARRIES THE PREREGISTERED EVALUATION ORDER VERBATIM** and draws the right consequence:
   a root solve before the gates voids the result.

## CONDITION 1 — THE ADMITTED MUTATION FAMILY IS NOT ENUMERATED. THIS IS THE MAIN FINDING.

Section 5.2 names five channels — geometry, clock, measure, regulator, action-partition — and sets the
pass condition as "every admitted target-independent mutation is either physically equivalent under a
derived equivalence relation or excluded by an upstream principle."

**NOWHERE DOES THE SPEC ENUMERATE WHAT COUNTS AS AN ADMITTED MUTATION IN ANY CHANNEL.**

Why that is not a detail: the audit's scope is then choosable at execution time. Section 5.3 forbids
uniqueness "obtained only by narrowing the admitted family after seeing the root", and F-GK4 forbids an
audit restricted to a pinned skeleton or cellulation. **Both guards act on narrowing that happens after
the root or on a pinned carrier. Neither prevents a family chosen narrowly BEFORE the root by a lane
that can already see which mutations would be awkward.** An audit over an unenumerated family is not
falsifiable, because there is no fixed set against which its completeness can be checked.

**REQUIRED:** enumerate, per channel, the admitted target-independent mutations the audit will run —
in the spec, before execution. If a channel's family cannot be enumerated in advance, say so and state
why; an honestly open family is better than an implicitly narrow one. This is the same discipline as
frozen predictions: the set must exist before the outcome does.

## CONDITION 2 — "A DERIVED EQUIVALENCE RELATION" IS UNDEFINED AND DOES DECISIVE WORK

The pass condition turns on mutations being "physically equivalent under a derived equivalence
relation." **No such relation is specified, cited, or named anywhere in the spec.**

That undefined term is load-bearing: it is one of only two ways a mutation can pass. As written, a
mutation that changes the root could be declared equivalent under a relation constructed for the
purpose, and the audit would record a pass.

This is the program's characteristic failure in its recognized form. Q-11 recorded it as
match-by-name/fail-by-type, and Q-23 found the same shape yesterday in slot 18, where "unused" governs
admissibility and has no sealed definition. **An admissibility condition with an undefined predicate is
not a condition.**

**REQUIRED:** either cite the derived equivalence relation at file:line, or state that it does not yet
exist and that the audit's equivalence arm is therefore unavailable — in which case the only currently
usable pass route is "excluded by an upstream principle," and the spec should say so.

Note the precedent that makes this urgent rather than pedantic: the selector principle already lists
"gauge, public isometry, orientation paired with charge conjugation, and Boundary-Resolved equivalence"
as transformations "already proved physically null", and says "A continuous modulus that changes any
action integral or response coefficient is not a null transformation." **That is a candidate relation
and the spec does not cite it.** If it is the intended one, citing it discharges this condition
immediately.

## NOTED, NOT A CONDITION — SECTION 5 IS NOT YET A COMPLETE FROZEN GATE

Section 5.3 states honestly: "No numerical tolerance is set in this spec because no numerical
representation has been constructed. Any later executable spec must freeze exact arithmetic, certified
enclosure, or reproducibility tolerances before execution and before any root value exists."

That is the correct call at this stage. **But it means Section 5 must not be cited as a complete
acceptance gate.** The gate is complete only when the tolerances land, and they must land before any
root value exists — not before the root solve is written, before the root VALUE exists. Recorded so
that a later lane does not read "acceptance criteria, frozen before execution" as meaning all of them
are frozen.

## WHAT I CHECKED AND FOUND SOUND

- Section 0's four declared conditions are present and correctly placed first: the induced-only axiom as
  a condition rather than an output; the rank-6 current-carrier statement; the F-GK3 declaration; and a
  hook for where a future stitching/continuum rule would enter. The Q-22 conditionality is not buried.
- Section 4 does not define `C_record` to vanish anywhere, and explicitly forbids a renamed `L_open`.
- Section 5.1's evaluation order matches the preregistration verbatim.
- No computed value, coupling, root, scale, radius or eigenvalue appears anywhere in the spec.
- Section 1's eleven missing pieces are named individually rather than gestured at, which is what makes
  the MISSING SPECIFICATION verdict actionable.

## WHAT I DID NOT CHECK

- Whether the eleven missing Section-1 pieces are the COMPLETE set. That needs an independent inventory,
  not a read of the spec that names them.
- Sections 1.2, 1.3 and 3 in line-by-line detail against their cited sources. Spot checks passed; a full
  citation audit is a separate pass and belongs to an independent lane.

## DISPOSITION

Discharge Conditions 1 and 2 by amendment to the spec, append-only, before execution begins. Neither
requires re-authoring: Condition 2 may close by a single citation, and Condition 1 is an enumeration the
lane is better placed to write than I am.

Execution remains barred until then, and independently barred by the preregistered evaluation order
until the mutation and uniqueness gates are specified completely.

`alpha_computed = false`; `proof_authorized = false`; `kappa_record_computed = false`.
