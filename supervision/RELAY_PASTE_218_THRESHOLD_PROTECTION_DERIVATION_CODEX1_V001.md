PASTE 218 — CODEX LANE 1 — DERIVE THE PROTECTION ARGUMENT FOR `DeltaPhi = pi`

ROAD: **ADVANCES STEP 1 AND STEP 3 TOGETHER.** *** THIS IS A BUILD TASK, NOT AN AUDIT. THE
DELIVERABLE IS AN ARGUMENT, NOT AN INVENTORY. ***

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false;
coupling_evaluation_authorized = false; production_authorized = false.

*** THIS RELAY IS SELF-CONTAINED. ASSUME NO MEMORY OF ANY PRIOR RELAY. ***

---

## 1. THE QUESTION, AND WHY IT IS PHYSICS RATHER THAN BOOKKEEPING

```text
C_record(K) = DeltaPhi[K; X_K] - pi        and       alpha = 1/(4 pi K_*)
                                                     K_* = the root of C_record(K) = 0
```

**A prior manifest (`STAGE8_OPEN_ACTION_FORM_MEMBER_MANIFEST_V001.md`, `e042f0aa…`) established that
the admitted action-form family contains three schematic classes, all `UNDECIDABLE | TYPE-U`:**

```text
1. higher-derivative source terms          *** AN INFINITE TOWER. NOT ENUMERABLE. ***
2. different finite causal updates
3. record-curvature / dissipative mutations
```

*** AN INFINITE TOWER IS NOT A DEFECT. IT IS WHAT A NON-RENORMALIZABLE GRAVITATIONAL EFFECTIVE ACTION
LOOKS LIKE. NOBODY ENUMERATES IT. THE PRIOR FRAMING — "ENUMERATE THE FAMILY" — WAS THE REVIEWER
IMPORTING A BOOKKEEPING STANDARD WHERE PHYSICS HAS BETTER MACHINERY. THAT FRAMING IS WITHDRAWN. ***

**The right question:** `C_record` is a **phase/threshold condition**, not an amplitude.
**Phase and threshold conditions are frequently PROTECTED** — index-like, topological, and
periodicity-set quantities do not shift under higher-derivative corrections, because those
corrections move coefficients rather than winding or periodicity.

> ***DOES THE HIGHER-DERIVATIVE TOWER MOVE `DeltaPhi`, OR NOT?***

---

## 2. THE TASK — BUILD THE ARGUMENT

**2.1 ESTABLISH WHAT `DeltaPhi` IS, STRUCTURALLY.** From sealed text, with paths and lines: what
kind of object is it — a holonomy, a winding, a spectral flow, an accumulated geometric phase, a
Berry-type phase, something else? **What sets its periodicity, and what fixes the `pi`?** *** THIS
IS THE FOUNDATION OF EVERYTHING BELOW; DO NOT SKIP IT TO GET TO THE VERDICT. ***

**2.2 DERIVE THE PROTECTION ARGUMENT, OR EXHIBIT ITS FAILURE.** Given 2.1, determine whether adding
a higher-derivative source term to the action can shift `DeltaPhi`.

```text
IF PROTECTED   *** DERIVE IT. *** State the structural reason -- topological invariance, index
               theorem, periodicity fixed by a discrete datum, gauge/diffeo invariance of the
               phase, or whatever the actual mechanism is. Give the argument in full, with its
               hypotheses stated, and NAME WHAT WOULD BREAK IT.

IF NOT         *** EXHIBIT THE LEADING CORRECTION STRUCTURALLY. *** Which term at which derivative
               order first moves DeltaPhi, through what mechanism, and what suppression (if any)
               it carries. NO NUMERICAL VALUE -- the structure only.
```

**2.3 EXTEND TO THE OTHER TWO CLASSES.** Whatever the argument is, state whether it covers
**different finite causal updates** and **record-curvature/dissipative mutations**, or whether those
need separate treatment. *** DISSIPATIVE MUTATIONS ARE THE MOST LIKELY TO BREAK A PROTECTION
ARGUMENT — non-unitary evolution does not respect the invariances that usually protect a phase.
TREAT THAT CASE EXPLICITLY RATHER THAN FOLDING IT IN. ***

---

## 3. WHY BOTH OUTCOMES MATTER, AND NEITHER IS THE ONE THIS RELAY WANTS

```text
IF PROTECTED   the infinite tower becomes IRRELEVANT rather than merely suppressed. 5.3's "no
               inequivalent admitted positive root" is then satisfied over the whole infinite class
               BY AN ARGUMENT, not a list. *** AND IT WOULD EXPLAIN WHY ALPHA COULD BE AN EXACT PURE
               NUMBER RATHER THAN A LEADING-ORDER COEFFICIENT. LEAD WITH IT. ***

IF NOT         then K_* carries EFT corrections and alpha = 1/(4 pi K_*) is a LEADING-ORDER RESULT,
               NOT AN EXACT ONE. *** THAT IS A CLAIM ABOUT WHAT THIS PROGRAM CAN DELIVER, AND IT IS
               WORTH FAR MORE BEFORE THERE IS A NUMBER THAN AFTER. LEAD WITH IT. ***
```

*** THE PROGRAM PRESENTS ALPHA AS EXACT. EXACTNESS IS A STRONG CLAIM IN A GRAVITATIONAL EFT AND IT
NEEDS A PROTECTION ARGUMENT BEHIND IT. AS FAR AS THE REVIEWER HAS SEEN, NO SUCH ARGUMENT EXISTS
ANYWHERE IN THE CORPUS. IF YOU FIND ONE ALREADY WRITTEN, QUOTE IT AND SAY SO — THAT IS THE BEST
POSSIBLE OUTCOME AND IT ENDS THE QUESTION. ***

**Do not manufacture a protection argument.** A protection claim that fails later would be worse than
none, because everything downstream would inherit an exactness claim it cannot support. **State every
hypothesis your argument needs and attack it yourself before reporting.**

---

## 4. RULES

- **Q-54 typing on every negative:** TYPE-R refuted · TYPE-U unbuilt · TYPE-S scope-empty · TYPE-C
  constraint-blocked. `NO_VERDICT` is legal. **Only TYPE-R is physical content.**
- **Q-92:** specifying and naming what is missing is a complete answer, not a lesser one.
- **Q-69:** never identify a flag with the object that discharges it.
- **No unproved-identity transport.** A seal reaches what it names and no further.
- **Word-boundaried matching, CASE-INSENSITIVE on identifiers.**
- **Mark hypothetical flags inline** — if a `= true` sits under "what does not exist" or "possible
  future verdicts", say so on the same line.
- **Report search scope**: roots, exclusions, queries run.

## 5. FENCES — VERBATIM, NON-NEGOTIABLE

- **Never touch `a32_holdout/custodian_private/`.**
- **Do not compute** alpha, `kappa_record`, `kappa_Thomson`, a coupling, a scale, a root, an
  eigenvalue, a beta function, `E_R`, `T_R`, `k_R`, or any absolute interval.
  *** THIS RELAY ASKS WHETHER A THRESHOLD MOVES, NOT WHERE IT SITS. STRUCTURAL ARGUMENT ONLY — DO
  NOT EVALUATE `DeltaPhi`, DO NOT SOLVE `C_record(K) = 0`, DO NOT PRODUCE A NUMERICAL SHIFT. ***
- **No comparison to any measured constant.**
- **Do not resolve the Misner-Sharp / Brown-York fork by choosing — it must be DERIVED.**
- **Report refutations; never repair them.**

## 6. CUSTODY (Q-91)

*** NO LANE RUNS ANY GIT COMMAND. *** Write the artifact in the cleanroom, compute its
`.seal.sha256` sidecar and **verify it matches**, mirror artifact + sidecar to
`alpha-program-archive/workspace/`, report hashes and paths, and **stop**. You may run
`corpus_check.py --report` on your own artifact; `--gate` is not your concern and **a red gate is
never a reason to stop working.** The reviewer verifies, baselines, commits and pushes.

alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
