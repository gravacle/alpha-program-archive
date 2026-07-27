# E1 SUCCESSOR PROGRAM SPEC V002 — AMENDMENT 001
## Carrying U1/U2/U3 and the projection-tail conditional into the governing chain

Date: 2026-07-26

## Status and authority

```text
APPEND_ONLY AMENDMENT. V002 IS NOT EDITED. Where they conflict, this
amendment governs, and it governs ONLY BY ADDING OBLIGATIONS.
AUTHORIZED BY THE PRINCIPAL, this date, explicitly and on the record:
  "U3 AMENDMENT — YES. WRITE IT. Append-only, carrying U1/U2/U3 and the
   projection-tail conditional into E1 v002's governing chain with the
   verdict-language requirement stated."
Rationale of record, the principal's: it makes the spec STRICTER, not
looser, so it cannot manufacture a passing verdict; it closes a defect the
construction lane logged against itself; it has been load-bearing three
times.

AMENDS:
  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md
  468467303a109dc8...  (145,010 bytes / 2,344 lines)
CARRIES INTO IT:
  STAGE8_T7_ARM2_SHARPENING_AND_PROJECTION_TAIL_BINDING_V001.md
  782495ea...
CLOSES THE DEFECT RECORDED IN:
  STAGE8_T7_CONSTRUCTION_LANE_THREE_DEFECT_ERRATUM_AND_REVIEW_INCOMPLETENESS_V001.md
  11d12ead...   (DEFECT 1: binding sealed, then not propagated)

PRODUCTION PROHIBITED. alpha_computed = false. proof_authorized = false.
coupling_evaluation_authorized = false.
```

## 1. THE DEFECT THIS CLOSES, stated plainly

On the morning of the arm-2 sharpening, this lane sealed a binding whose own
text ordered the successor spec to carry a conditional obligation. It then
sealed that successor spec — v002 — containing **zero** of the binding's
markers. The seal-time verification checked hashes and Rule-6 compliance and
did not check the binding. That was the second instance of *seal an
obligation, then fail to propagate it*.

This amendment is the propagation. It is late by one spec generation, and
that lateness is part of the record rather than something the amendment
erases.

## 2. THE NAMED LEMMA AND ITS THREE UNCERTIFIED COMPONENTS

Carried verbatim from `782495ea` lines 39–51:

```text
NAMED LEMMA:
  E1_FREE_LINE_HUYGENS_COLLAR_AND_TIME_INTEGRATION_R_MINUS_ONE
UNCERTIFIED COMPONENTS, each to be authored as its own obligation with
its own witness:
  U1 uniform control of the time-profile W^{1,1} / BV norms;
  U2 LIGHT-CONE TRANSVERSALITY over ALL common A/B refinements in D3
     (note: under the RATIFIED standard D3 reading, this quantifier is
     the unrestricted one — U2 is therefore the harder statement, not the
     overlay-only one);
  U3 the finite-Q PROJECTION-TAIL issue, if that cutoff is retained.
```

**U1, U2 and U3 are hereby numbered obligations of E1 v002**, attached to
`§O.A0` and specifically to `§O.A0.2` (A-L0 arm 2, the Huygens-bound target,
BOTH factors required). Each requires its own witness. None may be
discharged by the discharge of another.

## 3. THE PROJECTION-TAIL CONDITIONAL OBLIGATION

Carried verbatim from `782495ea` lines 59–70:

```text
IF the certified route RETAINS a finite-Q (Galerkin/finite-carrier)
cutoff, THEN factor (i) requires a PROJECTION-TAIL / LIMIT LEMMA ON TOP:
the nonlocal projector can destroy exact light-cone support at finite
cutoff, so collar support must be re-established either uniformly in Q or
in the Q -> infinity limit with certified tails.
THIS DEPENDENCY IS BOUND HERE so no lane discovers it mid-execution. The
E1 v002 spec must carry it as an explicit conditional obligation attached
to U3, and its verdict language must state which of the two it relies on
(uniform-in-Q, or limit-with-certified-tails).
```

**That conditional obligation is now attached to U3 and binds v002.**

## 4. F'-17 — VERDICT-LANGUAGE REQUIREMENT (NEW; ADDITIVE ONLY)

The F' clause list of v002 runs F'-1 through F'-16. This amendment adds one
clause. It is numbered F'-17 to avoid collision and it only forbids.

```text
F'-17  PROJECTION-TAIL VERDICT-LANGUAGE FENCE.

  (a) NO verdict, grade, status flag or summary line touching A-L0 arm 2,
      factor (i), or the named lemma may be emitted unless it STATES IN THE
      VERDICT ITSELF which of exactly two routes it relies on:
          UNIFORM_IN_Q                  or
          LIMIT_WITH_CERTIFIED_TAILS
      A verdict that states neither is MALFORMED and must be withheld.
      "Uncertain which" is not a third option: it is a BLOCK.

  (b) A verdict relying on LIMIT_WITH_CERTIFIED_TAILS must EXHIBIT the
      tail certificate. Asserting that tails "can be certified" does not
      discharge it.

  (c) A verdict relying on UNIFORM_IN_Q must state the uniformity
      explicitly as a quantifier over Q and must satisfy F'-5, which
      forbids any constant carrying a carrier index or truncation level.
      A bound proved at fixed Q is NOT a UNIFORM_IN_Q verdict.

  (d) IF the certified route does not retain a finite-Q cutoff, the
      conditional is not triggered — but the verdict must SAY SO, naming
      the route as cutoff-free. Silence does not discharge a conditional.

  (e) U1, U2 and U3 each require their own witness. A verdict citing the
      named lemma while any of the three is uncertified must carry the
      OBJECT-VS-BOUND declaration required by the parent binding, or BLOCK.
```

## 5. DISCLOSURE — U3'S SCOPE IS NOW WIDER THAN ARM 2

Recorded as a cross-reference, **not** as a new constraint, and deliberately
framed so that it pre-empts nothing the principal is holding:

```text
U3 was authored as an arm-2 factor-(i) dependency. Two later sealed
artifacts find the same finite-carrier-versus-limit typing question to be
the pivot of R-L2b as well:
  STAGE8_RL2B_DIAGONAL_ATTACK_RESULT_V001.md            07ea1496b3391aa3f514
  STAGE8_RL2B_CONVERGENCE_HYPOTHESIS_RESOLUTION_AND_F5_TRILEMMA_V001.md
                                                        8270721c182468ed96d4
SO: the same typing decision governs two independent obligations. That is a
disclosure of scope, and it is the reason U3 has now been load-bearing three
times.

WHAT THIS AMENDMENT DOES NOT DO: it does not rule on F'-5, which the
principal has expressly HELD pending the independent lane's Trotter-Kato
referral; it does not adopt the trilemma's H1; and it does not weaken,
strengthen or reinterpret F'-5 in any way. F'-5 stands exactly as sealed.
Clause F'-17(c) CITES F'-5; it does not modify it.
```

## 6. RULE 6 — THE WEIGHTING REQUIREMENT, WITH THE COUNT CORRECTED

The parent binding requires that where v002's frozen predictions touch arm 2
they must state the independent family's record, WEIGHT it, and record that
they did. That requirement is carried here unchanged, with one correction of
fact:

```text
THE BINDING SAYS "THIRD CONSECUTIVE CYCLE". It was correct when written.
THE LEDGER NOW READS FOUR: P-C5, P-C6, P-C7, P-C8, per CALIBRATION_LEDGER
and per STAGE8_MASTER_PLAN_AMENDMENT_001 §F-1, which resolved exactly this
count and ruled the ledger's four authoritative over Part F's three.
ANY v002 PREDICTION TOUCHING ARM 2 MUST WEIGHT THE LEDGER'S FOUR.
Recovery of this lane's own family remains THE PRINCIPAL'S judgment on the
reviewer lane's reading. This amendment does not touch that.
```

## 7. EXECUTION GATE

```text
E1 v002 MAY NOT EXECUTE until, for each of U1, U2, U3:
  either a witness is sealed discharging it,
  or it is explicitly BLOCKED with its witness of blockage named;
AND until the projection-tail conditional is either triggered-and-carried
or declared untriggered under F'-17(d).
This gate is IN ADDITION TO every gate v002 already carries. It removes
none of them. The E1 v002 hostile-review gate remains separately OPEN
(five survivors; 19 MINOR untested), and E-Q1 remains separately mandatory
before execution.
```

## 8. STRICTNESS ASSERTION

```text
This amendment adds five obligations, one fence, and one execution gate.
It removes nothing, relaxes nothing, and supplies no constant, no value and
no route. THEREFORE IT CANNOT MANUFACTURE A PASSING VERDICT: every path it
opens ends in either a witness or a BLOCK. Its only possible effect on any
verdict is to withhold one that would otherwise have been emitted.
This is stated so a later lane can verify the claim rather than trust it.
```

## Protected status

```text
amends = STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md (468467303a109dc8)
v002_edited = false
append_only = true
authorized_by_principal = true   (this date, verbatim, quoted in §Status)
defect_closed = DEFECT_1_ARM2_BINDING_UNCARRIED   (11d12ead)
obligations_added = U1, U2, U3, projection_tail_conditional, F'-17
obligations_removed = 0
constants_supplied = 0
routes_supplied = 0
can_manufacture_a_passing_verdict = false
F5_ruled_on = false              (HELD by the principal pending Trotter-Kato)
F5_modified = false
trilemma_H1_adopted = false
rule6_weight_count = 4           (ledger; per MASTER_PLAN_AMENDMENT_001 F-1)
e1_v002_executable = false
hostile_review_gate = OPEN
EQ1 = MANDATORY_BEFORE_EXECUTION_UNRULED
kappa_record_carrier_typing = UNDECIDED_PRINCIPALS
production_authorized = false
alpha_computed = false
proof_authorized = false
```
