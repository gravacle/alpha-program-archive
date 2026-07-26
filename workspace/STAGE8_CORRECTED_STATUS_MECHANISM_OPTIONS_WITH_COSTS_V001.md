# Corrected-Status Mechanism — OPTIONS WITH COSTS (no option adopted) V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY OPTIONS MEMO. NOTHING BUILT. NO OPTION CHOSEN. The principal
picks; this lane does not.
Cites: canonical plan 12f204c64f0c0fd9...; amendment 001 c59cc8337913b81b...;
the correction-path determination sealed immediately prior.
STOP-RULE CHECK PERFORMED AND REPORTED IN SECTION 5: NO THIRD LAYER FOUND.
PRODUCTION PROHIBITED. alpha_computed = false.
```

## 1 — THE FINDING THAT RE-COSTS EVERY OPTION, read from code

```text
DECLARED_OPEN, complete, verbatim from the evaluator:
    DECLARED_OPEN = {
        "SPEC-SEAL", "holdout_registry_freeze",
        "independent_evaluator_implementation",
    }
THREE KEYS. NONE OF THEM DESCRIBES ANY OF THE THREE OBLIGATIONS:
  T01 needs the represented basepoint link/holonomy object;
  T02 needs a witness in the represented associated-graded quotient;
  T11 needs response-map pullback commutation + boundary-subextensive
      invariance (= R-L2b).
THE ROUTING RULE:  CONDITIONAL requires  open_item IN DECLARED_OPEN.
                   Otherwise -> failures -> GATE5_CORE_BLOCKED.
BINDING CONSTRAINT (b) FORBIDS CHANGING THE DECLARED_OPEN SET.

*** THEREFORE, AND IT IS TRUE OF ALL THREE OPTIONS EQUALLY: UNDER
CONSTRAINT (b), NO MECHANISM CAN MOVE T01, T02 OR T11 TO CONDITIONAL. THE
ONLY HONEST STATUS REACHABLE FOR THEM IS BLOCKED. ***

CONSEQUENCE THE PRINCIPAL SHOULD SEE BEFORE CHOOSING, because it is the
substance rather than the plumbing: step 4 of the stated ordering — "the
three over-claims are expressed through it, T01/T02/T11 move to a status
that reads honestly" — WILL TURN THE BATTERY FROM "PASSES ON THREE
UNSUPPORTED NODES" INTO "BLOCKED". Not conditional-but-alive. BLOCKED.
That is the correct outcome and this lane is not arguing against it; it is
flagged so it is chosen rather than discovered.

AND A TENSION BETWEEN TWO BINDING CONSTRAINTS, resolvable but needing to be
said: (d) requires the control to demonstrate "that a corrected status
reaches CONDITIONAL", while (b) forbids the DECLARED_OPEN change that would
let a REAL corrected report reach it. RESOLUTION, offered not adopted: the
control demonstrates the BRANCH works using a SYNTHETIC fixture whose
open_item is an existing DECLARED_OPEN key (e.g. "SPEC-SEAL"), which
exercises the path without touching the set. Under that reading (d) is
satisfiable and (b) is intact — but the demonstration is then about the
mechanism, NOT about T01/T02/T11, and the artifact must say so.
```

## 2 — THE OPTIONS

### OPTION 1 — successor report at the canonical path; original preserved and hash-recorded

```text
MECHANISM: preserve T0X.json's exact bytes at a new location with its sha256
recorded, then write the corrected report AT THE CANONICAL PATH
t_reports/T0X.json with pass:false and an honest open_item.
EVALUATOR CHANGE REQUIRED: *** NONE. *** The path is constructed
(f"{tid}.json"), so new content at that path is consumed automatically.
RULE-8 EXPOSURE: MINIMAL — arguably this is not new machinery at all, which
is why it deserves to be on the list even though it was not among the three
posed.
COSTS:
  - PATH STABILITY IS LOST. Any artifact citing the PATH now resolves to
    different content. Rule 7 makes hash-citation the ordering authority, so
    the record survives; but the corpus will contain path references whose
    content changed, and reproduction-by-a-stranger (already flagged in G1)
    gets murkier, not clearer.
  - The "append-only" question is real and should be ruled on rather than
    assumed: replacing the file AT a path while preserving its bytes and
    hash elsewhere is not destruction, but it is also not obviously
    "append-only". This lane does not decide it.
  - Content-addressing is unaffected: each report self-addresses via
    sha256_of_body with that field blanked, so a new report computes its own
    cleanly.
VERIFICATION BURDEN: LOWEST of the four. Nothing enters the trust root.
```

### OPTION 2 — a supersession field the evaluator honours

```text
MECHANISM: add e.g. superseded_by to the report schema; a successor
evaluator follows the pointer.
EVALUATOR CHANGE REQUIRED: YES — new sealed evaluator, v001 preserved and
both cited per (a).
COSTS:
  - IT ADDS RESOLUTION TO A SCRIPT WHOSE ENTIRE VIRTUE IS THAT IT RESOLVES
    NOTHING. Today every input path is constructed and nothing is
    discovered; that is why the contract is auditable in one reading. A
    pointer introduces dangling pointers, pointer chains, successors that
    themselves point onward, and backwards-pointing successors.
  - HIGHEST VERIFICATION BURDEN. The evaluator is the SOLE verdict
    authority; every added line sits in the trust root, and the program's
    documented characteristic failure is claiming more than was proved —
    which is exactly what a resolution step could hide.
BENEFIT: path stability is PERFECT. The sealed original stays byte-identical
at its own path forever.
```

### OPTION 3 — an evaluator-input authority list

```text
MECHANISM: a new sealed file mapping tid -> authoritative filename, which a
successor evaluator consults.
EVALUATOR CHANGE REQUIRED: YES.
COSTS:
  - CREATES A NEW SINGLE POINT OF AUTHORITY that itself needs sealing,
    auditing and a control.
  - COLLISION RISK WITH THE TRANSFORM FENCE is avoidable by distinct naming
    and location, but THIS PROGRAM'S MANIFEST TRACK RECORD IS POOR: the
    bridge manifest created the quarantine row conflict, and sealing
    manifest v006 made the sealed rehearsal harness unrunnable. Two
    manifests, two collateral breakages. A third manifest is not a neutral
    act here.
BENEFIT: explicit and auditable in one place; path stability preserved.
VERIFICATION BURDEN: MEDIUM-HIGH.
```

### OPTION 4 — NO NEW MECHANISM AT ALL (this lane's addition to the list)

```text
MECHANISM: exactly Option 1, but named honestly for what it is — USE THE
CONTRACT AS ALREADY DESIGNED. The evaluator ALREADY reads pass and, when
pass is false, open_item. Authoring corrected reports with pass:false and an
honest open_item requires NO new machinery whatsoever. The status is
expressed through a path the evaluator already has.
WHY IT IS LISTED SEPARATELY FROM OPTION 1: Option 1 was posed as a
mechanism. This is the observation that it is not one, and that Rule 8
therefore does not engage at all for it. If the principal picks this, the
Rule-8 exception recorded in the authorization is NOT SPENT and remains
available for something that genuinely needs it.
COSTS: identical to Option 1 (path stability; the append-only ruling).
```

## 3 — THE COMPARISON THAT MATTERS

```text
WHAT OPTIONS 2 AND 3 BUY OVER OPTIONS 1/4:  PATH STABILITY, AND NOTHING
ELSE.
WHAT THEY DO NOT BUY: CONDITIONAL instead of BLOCKED. Section 1 shows that
is unavailable under (b) regardless of which option is chosen. Anyone
assuming the more elaborate mechanisms would keep the battery alive rather
than blocked should read Section 1 first.
SO THE CHOICE REDUCES TO: is byte-level path stability for three sealed
reports worth putting a resolution step or a third manifest into the sole
verdict authority?
This lane states the trade and does not resolve it. Given Rule 8's default
of no, and given that the program's two previous manifests each caused a
collateral breakage, the burden of argument sits with 2 and 3 — but the
append-only question in Options 1/4 is genuine and is the principal's to
rule on, not this lane's to wave through.
```

## 4 — WHAT THE CONTROL MUST DO, under either family

```text
Per (d), and both halves are required or the mechanism is indistinguishable
from one that does nothing:
  C-1  A CORRECTED STATUS REACHES CONDITIONAL. Synthetic fixture, open_item
       set to an existing DECLARED_OPEN key, so (b) is not touched. This
       exercises a branch that HAS NEVER EXECUTED — T07 is pass=false with
       open_item=null and routes to failures, so the CONDITIONAL path is
       unexercised in the program's entire history.
  C-2  AN UNCORRECTED OVER-CLAIM STILL PASSES. Directly demonstrable: T01
       as it stands is pass=true and passes. The control must show the
       mechanism does not silently catch what it was never given.
  C-3  Per (e), the self-test extended to cover the new path, since
       --selftest by construction cannot currently test "a report asserting
       pass on an unsupported basis".
NOTE FOR C-1's ARTIFACT: it demonstrates THE MECHANISM, not the three
reports. T01/T02/T11 will land on BLOCKED. The artifact must say that
plainly or it will read as though the overclaims were routed to CONDITIONAL.
```

## 5 — STOP-RULE CHECK, performed and reported as instructed

```text
THE INSTRUCTION: if fixing this reveals ANOTHER layer beneath — a defect in
what validates the evaluator, or in the sealing discipline itself — do not
fix it, report and STOP.
*** NO THIRD LAYER FOUND. *** Stated with what was actually checked:
  - The evaluator has a --selftest, and it exists and runs its own fixtures.
    Its inability to test an over-claim is NOT a separate layer; it is the
    SAME contract defect seen from inside, and (e) already covers extending
    it.
  - The sealing discipline itself was not found defective by this work.
    Seals verify; content-addressing (sha256_of_body with the field blanked)
    is self-consistent and this lane re-derived the scheme from the code.
  - ONE ADJACENT OBSERVATION, offered as part of the same layer rather than
    a new one: DECLARED_OPEN's three keys match NO real obligation anywhere
    in the program, and the CONDITIONAL branch has never executed. So the
    conditional path appears to have been authored speculatively and never
    exercised — which is the same never-executed-branch finding already on
    the record for the comparator's accepting branch, now in a third place.
    That is a pattern about branches, not a new layer beneath the evaluator.
CONVERGENCE ASSESSMENT, since the principal asked whether this is
stabilizing or circling: the findings did get more fundamental and fewer —
reports, then the contract that reads reports — and NOTHING READS THE
EVALUATOR. On this pass the bottom held. This lane does not claim that
proves convergence; it reports that the predicted last layer behaved like
the last layer.
```

## Protected status

```text
options_presented = 4        (three posed + one this lane added)
option_adopted = none
mechanism_built = none
report_rewritten = none
DECLARED_OPEN_keys = 3
any_option_can_reach_CONDITIONAL_for_T01_T02_T11 = false   (under (b))
honest_reachable_status_for_the_three = BLOCKED
constraint_b_and_d_tension = resolvable_via_synthetic_fixture (offered)
battery_outcome_if_expressed_honestly = GATE5_CORE_BLOCKED
options_2_3_buy_over_1_4 = path_stability_only
CONDITIONAL_branch_ever_executed = false
third_layer_found = false
stop_rule_triggered = false
production_authorized = false
alpha_computed = false
proof_authorized = false
```
