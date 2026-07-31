PASTE 220 — CODEX LANE 2 — THE STALE-CRITERIA SWEEP: FIND EVERY GATE THAT WOULD KILL A CORRECT ANSWER

ROAD: **UNBLOCKS ALL THREE STEPS.** *** A LIVE FALSIFIER EMBEDDING A STRUCK RULE WOULD WRONGLY REJECT
A CORRECT CANDIDATE. ONE SUCH FALSIFIER HAS ALREADY BEEN FOUND POINTING AT THE PROGRAM'S OWN
DELIVERABLE. THIS IS THE MOST DIRECT OBSTACLE-REMOVAL AVAILABLE. ***

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false;
coupling_evaluation_authorized = false; production_authorized = false.

*** THIS RELAY IS SELF-CONTAINED. ASSUME NO MEMORY OF ANY PRIOR RELAY. ***

---

## 1. WHAT HAPPENED, AND WHY IT IS URGENT

The program struck a rule and **the specs kept enforcing it.**

```text
Q-65   REFUTED "only overdetermination forces a number." A REQUIRE whose EXISTENCE AND UNIQUENESS
       ARE BOTH DERIVED forces a number on its own. Three forcing shapes, not one.
Q-76   STRUCK overdetermination by principal act -- "not retained even as an aspiration."

AND YET:
  STAGE8_CROSS_SECTOR_METRIC_RULE_ADMISSIBILITY_SPEC_V001.md -- the spec defining the success
  criterion for the cross-sector metric rule, "equivalently a determination of beta" --
  *** POSES THE DELIVERABLE AS AN OVERDETERMINATION TARGET ***, with falsifier F3 (:265-267) and
  minimal-pass item 3 (:292) each demanding a second independent overdetermining requirement.

  A beta candidate scored against F3 as written TODAY WOULD BE WRONGLY KILLED.
```

*** THE PROGRAM WROTE A GATE THAT REJECTS THE VERY THING IT IS TRYING TO PROVE. AND IT WAS FLAGGED
ONCE ALREADY — `STAGE8_FORCING_BOUNDARY_ADJUDICATION_EINSTEIN_V001.md:44` — AND NEVER REPAIRED. ***

**This is now amended:** `PRINCIPAL_AMENDMENT_002_OVERDETERMINATION_BAR_STRUCK_EVERYWHERE_2026-07-31_V001.md`
(`f1c50042…`). **But that amendment was written from two accidental discoveries. Nobody has swept.**

**Scoping counts already taken (verify them; do not trust them):** ~101 files carry live
falsifier / minimal-pass / acceptance-battery language; `overdetermin` appears in ~24;
`derived ground` ~9; generative/formation ~6; bare-existence ~4; disjoint-critical-path ~2.

---

## 2. THE TASK — BUILD THE STALE-CRITERIA LEDGER

**2.1 ENUMERATE THE LIVE ACCEPTANCE SURFACES.** Every falsifier battery, minimal-pass list,
acceptance criterion, gate condition and gate release currently in force. **For each: path, the
criterion as written, and what it would reject.**

**2.2 FOR EACH, CHECK IT AGAINST THE CURRENT RULING SET.** *** THIS IS THE WHOLE POINT AND IT IS
WHAT NOTHING IN THIS PROGRAM DOES. *** The register `QUESTIONS_SETTLED_REGISTER_V001.md` is indexed
by question — **grep it.** Known struck or refuted framings to check against, **and this list is
NOT exhaustive — find others**:

```text
"only overdetermination forces a number"     REFUTED Q-65, STRUCK Q-76
"no chain reaches derived ground"            REFUTED
"two disjoint critical paths"                REFUTED Q-75
"which extension is it"                      MALFORMED Q-81 -- it is a new class
the generative / formation binary            REFUTED Q-90 -- both, on different axes
the bare-existence shortcut                  REFUTED Q-94, nine ways
"enumerate the admitted family"              WITHDRAWN Q-124 -- an infinite tower is what a
                                             non-renormalizable gravitational EFT looks like
```

**2.3 CLASSIFY EACH FINDING:**

```text
STALE-BLOCKING    the criterion embeds a struck rule AND would reject a correct candidate.
                  *** REPORT THESE FIRST. EACH IS A LIVE OBSTACLE. ***
STALE-INERT       embeds a struck rule but cannot reject anything (descriptive, historical,
                  or already superseded in force).
CURRENT           consistent with the ruling set. *** SAY SO — a clean gate is a real result and
                  most of them will be clean. ***
```

**2.4 FOR EACH `STALE-BLOCKING`, STATE THE REPLACEMENT CRITERION** the current ruling set implies.
**Name it; do not apply it, and do not edit any spec.**

---

## 3. WHAT NOT TO DO

*** DO NOT REPAIR ANY SPEC. REPORT ONLY. *** Amendments are principal acts and will be issued
centrally. **A lane editing a sealed gate is exactly the failure this sweep exists to prevent.**

*** DO NOT WEAKEN ANYTHING THAT IS CURRENT. *** The goal is removing rules the program already
struck — **not lowering live standards.** **If a criterion is strict but current, mark it CURRENT and
move on.** These stand and are NOT candidates for this sweep:

```text
permissions never force -- an allow-shaped structure outputs a SET, not a number
the condition must CLOSE, not merely touch
    (boundary_access_closure_threshold_principle_v001.md was retired as CELL_CONSTRAINT_ONLY
     for touching both geometries without closing -- THAT RETIREMENT IS CORRECT AND STANDS)
§5.3 IN FULL, including NO NARROWING OF THE ADMITTED FAMILY AFTER THE ROOT IS SEEN
every fence; Q-54 typing; Q-69; the sqrt(2) derived-never-chosen rule
```

---

## 4. SYMMETRIC LEADS

```text
IF STALE-BLOCKING GATES EXIST -- *** LEAD WITH THEM, MOST CONSEQUENTIAL FIRST. Each one removed is
an obstacle the program put in its own path. ***

IF THE SWEEP COMES BACK MOSTLY CLEAN -- LEAD WITH THAT. It would mean the cross-sector spec was an
isolated lapse rather than a systematic rot, and that is genuinely good news worth stating plainly.
```

---

## 5. RULES

- **Q-54 typing on every negative:** TYPE-R refuted · TYPE-U unbuilt · TYPE-S scope-empty · TYPE-C
  constraint-blocked. `NO_VERDICT` is legal.
- **Q-92:** specifying and naming what is missing is a complete answer, not a lesser one.
- **Word-boundaried matching, CASE-INSENSITIVE on identifiers.** *** A CAPITALIZED FLAG WAS INVISIBLE
  TO A REVIEWER SCAN TODAY. ***
- **Mark hypothetical flags inline** — a `= true` under "what does not exist" or "possible future
  verdicts" must say so on the same line.
- **Report search scope**: roots, exclusions, queries run. **Verify the scoping counts in §1 rather
  than inheriting them.**

## 6. FENCES — VERBATIM, NON-NEGOTIABLE

- **Never touch `a32_holdout/custodian_private/`.**
- **Do not compute** alpha, `kappa_record`, `kappa_Thomson`, a coupling, a scale, a root, an
  eigenvalue, a beta function, `E_R`, `T_R`, `k_R`, or any absolute interval.
- **No comparison to any measured constant.**
- **Do not resolve the Misner-Sharp / Brown-York fork by choosing — it must be DERIVED.**
- **Report refutations; never repair them.**

## 7. CUSTODY (Q-91)

*** NO LANE RUNS ANY GIT COMMAND. *** Write the artifact in the cleanroom, compute its
`.seal.sha256` sidecar and **verify it matches**, mirror artifact + sidecar to
`alpha-program-archive/workspace/`, report hashes and paths, and **stop**. You may run
`corpus_check.py --report` on your own artifact; `--gate` is not your concern and **a red gate is
never a reason to stop working.** The reviewer verifies, baselines, commits and pushes.

alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
