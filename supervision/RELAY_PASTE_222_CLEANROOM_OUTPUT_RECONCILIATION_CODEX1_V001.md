PASTE 222 — CODEX LANE 1 — RECONCILE `cleanroom_output/`: 87 FILES NOBODY SWEEPS

ROAD: **UNBLOCKS ALL THREE STEPS.** *** THERE ARE PASSED GATES AND DERIVED RESULTS IN THIS DIRECTORY
THAT THE SUPERVISION REGISTER RECORDS AS UNBUILT OR NEVER RUN. WE MAY BE STANDING ON MORE THAN WE
THINK — AND AT LEAST FOUR REGISTER ENTRIES WRITTEN TODAY CONTRADICT IT. ***

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false;
coupling_evaluation_authorized = false; production_authorized = false.

*** THIS RELAY IS SELF-CONTAINED. ASSUME NO MEMORY OF ANY PRIOR RELAY. ***

---

## 1. WHAT HAPPENED

**`/Users/bgm/MB Work/alpha-program-archive/cleanroom_output/` contains 87 files and sits OUTSIDE the
`workspace/` subtree that every lane, every sweep and every audit script enters.** It was found by
accident on 2026-07-31 when a lane went looking for the Stage-10 geometric brief and the register's
citation of it proved stale.

**The reviewer has verified six seals there — all OK — and read enough to establish the following,
which the register currently contradicts:**

```text
GATE 1  (35)  "The Comparison Group Is U(1), Target-Independently"
GATE 2  (41)  "r = 3 Is a Theorem; the Accounting Is Exact"
GATE 3  (38)  "Hilbert-Functor Uniqueness -- The Forms Are Derived"
GATE 4  (32)  exactly ONE normalized differential equivalence class, P1-P4 all confirmed
GATE 4  (44)  one public-collapse covector ray; "Gate 4 Core Complete"

*** THE SUPERVISION REGISTER SAYS GATES 2/3/4 WERE "NEVER RUN" (Q-114 N6, OBS-09).
    RELAY 208 REPORTED GATE 2 AS "DESIGNATED BY PREMISE, GATE UNPASSED."
    BOTH ARE WRONG. ***
```

**And Gate 4's P3 states:** *"What the spec had as an axiom ('independent primitive F²… axiomatically
disallowed') is, at the differential level and within the enumerated family, now **derived**."*
*** THAT IS A DEBT-IN-AXIOM-CLOTHING WITH A DERIVATION. THE SUPERVISION LANE BELIEVED NONE HAD EVER
BEEN CLOSED. ***

**But `STATUS.json` reads `final_status: BLOCKED`** — a concluded phase that hit a stop rule — **and
its `unresolved_load_bearing_items` already contain findings the supervision lane rediscovered
independently today**, including *"Family E: connected many-record generator fixed only by adopted
quasi-free completeness"* and *"Family F: parent zero-form/Pauli competitors excluded only by adopted
single-operator completeness."*

---

## 2. THE TASK — BUILD THE RECONCILIATION LEDGER

**2.1 SWEEP ALL 87 FILES.** Verify every seal (**note the sidecar convention differs here:
`NN_NAME_V001.seal.sha256`, with NO `.md` before `.seal`**). Report any seal that does not verify
**immediately and separately** — that would be a custody issue, not a physics one.

**2.2 FOR EACH SUBSTANTIVE RESULT, CLASSIFY AGAINST THE SUPERVISION REGISTER**
(`/Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md`, indexed by question —
**grep it**):

```text
CONTRADICTS      cleanroom_output establishes something the register records as unbuilt, never run,
                 or absent. *** REPORT THESE FIRST. EACH IS EITHER A RECOVERED RESULT OR A
                 SUPERSESSION NOBODY TRACKED. ***
CORROBORATES     both agree -- note it briefly; it raises confidence and costs nothing.
SUPERSEDED BY    the register's entry is LATER and defeats the cleanroom result. *** SAY SO
REGISTER         EXPLICITLY WITH DATES — a passed gate that was later refuted must NOT be revived. ***
NOVEL            present there, absent from the register entirely. These are the recoveries.
```

**2.3 FOR EVERY `CONTRADICTS` AND `NOVEL`, STATE THE SCOPE PRECISELY.** *** THIS IS THE PART THAT
MATTERS MOST. *** Gate 4's derivation is explicitly *"at the differential level and within the
enumerated family"* — **that is a scoped result, not a universal one.** **A scoped result reported as
universal would be worse than not finding it at all.** For each: what exactly was established, over
what family, under what hypotheses, and **what it does NOT establish.**

**2.4 THE FORK/FAMILY LIST.** `STATUS.json` names Families A–G and a stop rule. **Map each to the
supervision register's current state** — still open, since resolved, or since refuted.

---

## 3. WHAT NOT TO DO

- *** DO NOT REVIVE A RESULT THE REGISTER LATER DEFEATED. *** `final_status: BLOCKED` means this
  phase concluded. Some of it may have been superseded on purpose. **Check dates.**
- *** DO NOT REPAIR, RE-RUN OR RE-SEAL ANYTHING. *** Report only.
- *** DO NOT TREAT `PRECOMPARISON_MANIFEST.sha256`, `NEEDS_THEORY_DECISION.md`,
  `NEEDS_EXTERNAL_EXECUTION.md` OR `DEPENDENCY_REQUEST.md` AS DECORATION *** — they name what the
  phase itself said was missing, and that is exactly the information the supervision lane lacks.
- **Never touch `a32_holdout/custodian_private/`.** *** `09_HOLDOUT_STATUS.md` MAY DISCUSS THE
  HOLDOUT — READING **ABOUT** IT IS PERMITTED; ENTERING IT IS NOT. ***

---

## 4. SYMMETRIC LEADS

```text
IF THERE ARE SUBSTANTIAL RECOVERIES -- *** LEAD WITH THEM. Passed gates and derived results the
program does not know it has are the single cheapest progress available, and the reviewer's
register is demonstrably wrong on at least three counts. ***

IF ALMOST EVERYTHING IS SUPERSEDED OR ALREADY KNOWN -- LEAD WITH THAT. It would mean the register is
in better shape than today's discovery suggests, and that is worth establishing plainly rather than
leaving the program to assume a hidden trove exists.
```

---

## 5. RULES

- **Q-54 typing on every negative:** TYPE-R refuted · TYPE-U unbuilt · TYPE-S scope-empty · TYPE-C
  constraint-blocked. `NO_VERDICT` is legal. **Only TYPE-R is physical content.**
- **Q-92:** specifying and naming what is missing is a complete answer, not a lesser one.
- **Q-69:** never identify a flag with the object that discharges it.
- **No unproved-identity transport.** *** A SEAL REACHES WHAT IT NAMES AND NO FURTHER — AND THAT
  APPLIES DOUBLY TO SCOPED DERIVATIONS RECOVERED FROM A CONCLUDED PHASE. ***
- **Word-boundaried matching, CASE-INSENSITIVE on identifiers.**
- **Mark hypothetical flags inline.**
- **Report search scope**: roots, exclusions, queries run.

## 6. FENCES — VERBATIM, NON-NEGOTIABLE

- **Never touch `a32_holdout/custodian_private/`.**
- **Do not compute** alpha, `kappa_record`, `kappa_Thomson`, a coupling, a scale, a root, an
  eigenvalue, a beta function, `E_R`, `T_R`, `k_R`, or any absolute interval. *** SOME FILES HERE ARE
  EXECUTABLE `.py`. DO NOT RUN THEM. READ THEM. ***
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
