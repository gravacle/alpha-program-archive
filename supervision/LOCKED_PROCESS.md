LOCKED PROCESS — FOUR STEPS. NOT TO BE REVISED.

Ruled by the principal 2026-08-01: "lock one simple process structure that ensures the integrity of
the results. Nothing more."

---

## THE FOUR STEPS — *** THESE ARE **REVIEWER** STEPS. LANES DO NOT DO THEM. ***

*** LANES: SEAL, MIRROR ARTIFACT AND SIDECAR, REPORT HASHES, **STOP**. DO NOT REGISTER. DO NOT
COMMIT. DO NOT PUSH. DO NOT ASK FOR AUTHORITY TO — IT WILL NOT BE GRANTED. Q-91 MAKES THE REVIEWER
SOLE REGISTRAR AND COMMITTER, AND TWO LANES STALLED ON THIS AMBIGUITY ON 2026-08-01 BECAUSE THIS
HEADING DID NOT SAY SO. THAT WAS A REVIEWER DEFECT. ***


```text
1  VERIFY THE HASH.  shasum -a 256 the artifact against the hash the lane stated.
                     MISMATCH -> STOP. Do not read further, do not register.

2  FENCE-SCAN.       grep for a computed alpha, kappa_record, kappa_Thomson, coupling, scale,
                     root, eigenvalue, or any comparison to a measured constant.
                     HIT -> STOP and report it.

3  REGISTER ONE ENTRY.  Q-number, artifact name, hash, the flag block, ONE sentence of what
                     changed. *** NOT AN ESSAY. THE ARTIFACT HOLDS THE DETAIL. ***

4  COMMIT AND PUSH.  Mirror artifact and sidecar. Push. Done means pushed.
```

## LANES — 2026-08-01. *** EINSTEIN RETIRED. NOT A RESERVE — IDLE. ***

```text
CODEX 1 . CODEX 2 . BOHM   -- THREE LANES. ALL THREE CONSTRUCT.
*** BOHM IS A WORKING LANE, NOT ONLY A REVIEWER. When both Codex lanes are busy, Bohm computes. ***
*** WHEN BOHM CONSTRUCTS, A CODEX LANE VERIFIES IT under the adversarial brief below.
Q-91's separation of constructor and verifier does not lapse because a lane was retired. ***
```

## PREFLIGHT — THREE LINES, BEFORE ANY RELAY SHIPS

```text
DOES THE OBJECT EXIST?   IS THE VERSION CURRENT?   ARE ITS INPUTS PRESENT?
*** IF ANY ANSWER IS NO, **THAT** IS THE RELAY. ***
```

*** AND PREFLIGHT RUNS AT **SEND TIME**, NOT ONLY AT WRITE TIME. A relay loaded later than the
register head it was written under is RE-CHECKED against every entry since, before pbcopy.
Installed 2026-08-01 after relay 270 shipped four hours stale across fifteen register entries and
needed a mid-run addendum (283) to repair — a defect the principal caught, not the reviewer. ***

*** ADDED 2026-08-01 AFTER FOUR RELAYS ON TARGET 2 (259, 261, 263, 265) EACH RETURNED "THE THING
UNDERNEATH YOU DOES NOT EXIST." THE FOURTH QUESTION SHOULD HAVE BEEN THE FIRST. AND THE WHOLE
RESEARCH PLAN WAS BUILT ON A `Gamma_K` FORMULA TWO LANES LATER FOUND SUPERSEDED. ***

**AND: the reviewer tests his own hypotheses BEFORE they become relays.** Eight collapse proposals,
six refuted. Seam 10 cost a full lane cycle to refute what a three-second computation would have
killed. *** LANES ARE FOR WHAT THE REVIEWER CANNOT DO IN MINUTES. ***

## PLAN GOVERNANCE — RULED BY THE PRINCIPAL 2026-08-01

```text
THE GOVERNING PLAN IS  alpha_supervision/TASK_LIST_HERE_TO_ALPHA_2026-08-01_V002.md
*** EVERY RELAY HEADER CARRIES A TASK NUMBER (1-6, or SUPPORT) FROM ITS SECTION 9. WORK WITH NO TASK ID DOES
NOT SHIP. A NEEDED CHANGE IS LOGGED IN THE PLAN'S SECTION 10 FIRST, SURFACED TO THE PRINCIPAL, AND
ONLY THEN EXECUTED. THE PLAN IS WHAT WE FOLLOW. ***
```

## FENCES — ACT-BASED, NOT TOKEN-BASED (implements Q-198 + DoR 006's scoping; C19)

```text
*** WHAT IS BARRED IS THE ACT, NEVER THE WORD: ***
BARRED   computing or bounding ALPHA, kappa_record, kappa_Thomson, or K_* / any root of the
         physical residual . comparing ANYTHING to a measured constant . choosing a physical
         fork that must be derived (Misner-Sharp/Brown-York etc.) . fitting any construction
         toward a known target . touching a32_holdout/custodian_private/
PERMITTED, EXPLICITLY: all structural mathematics of DECLARED objects -- spectra and
         eigenvalues of declared finite/fixture objects (DoR 004 precedent) . operator
         comparisons . existence/uniqueness arguments . gap-existence arguments . proofs about
         infinite families (the Q-205 precedent: A PROOF ABOUT A FAMILY COUNTS AS
         INSTANTIATION; the Q-200 rule bars SCHEMAS-PASSED-AS-INSTANCES, not structural
         arguments)
```

*** THE MACHINERY-APPEAL RULE: ANY LANE THAT STOPS BECAUSE A FENCE (NOT PHYSICS) BLOCKS A
STRUCTURAL RESULT MUST SAY SO IN ITS ARTIFACT WITH THE FLAG
`FENCE_BLOCKED_STRUCTURAL_RESULT = true | what: ... | fence: ...`
-- SO ARTIFICIAL CONSTRAINTS SURFACE AS FINDINGS INSTEAD OF DISSOLVING INTO NO_VERDICTs. The
reviewer routes every such flag to the principal. A fence that blocks a non-fitting result is a
DEFECT (DoR 004's ruling) and gets scoped or lifted, never silently obeyed. ***

## THE THREE THINGS IN A RELAY THAT PROTECT THE RESULT

*** THESE EARNED THEIR KEEP. NOTHING ELSE IN A RELAY DID. ***

```text
A  "HUNT YOUR OWN COUNTEREXAMPLE, AND LEAD WITH IT IF YOU FIND ONE."
B  TYPE EVERY NEGATIVE:  TYPE-R refuted . TYPE-U unbuilt . TYPE-S scope-empty . TYPE-C
                         constraint-blocked CHECKS ONLY . TYPE-P premise-conditional (DoR 006).
                         ONLY TYPE-R IS PHYSICAL CONTENT.
C  NAME THE SYMBOL COLLISIONS THAT BEAR ON THIS QUESTION. Nothing generic.
```

## WHAT IS RETIRED

```text
the pre-commit corpus_check GATE   -- blocked 5 commits on 2026-08-01, found 0 real defects
four parallel status documents     -- EXECUTION_TRACKER.md is the only one maintained
relay boilerplate                  -- the standing fences are read once, not repeated per relay
register entries as essays         -- capped at the flag block plus one sentence
```

*** THIS FILE IS NOT REVISED. IF SOMETHING HERE IS WRONG, IT IS RULED ON BY THE PRINCIPAL AND
REPLACED WHOLE — NOT AMENDED, NOT EXTENDED, NOT VERSIONED. ***

alpha_computed = false; proof_authorized = false; kappa_record_computed = false.

## MIRROR-VERIFY RULE (2026-08-01, after the C5-C25 loss)
After EVERY edit to the plan, register, or tracker: cp to the archive mirror, then VERIFY the
mirror is byte-identical (shasum both) BEFORE committing. On session resume: verify the plan's
section-10 head (highest Cnn) matches the tracker's recorded C-head before any new work.
C5-C25 were written, announced, and then lost because the pushed mirror never carried them.

## LOCAL-SIDECAR RULE (added 2026-08-03, Q-351)

The reviewer-owned seal sidecars that live NEXT TO the supervision files
(alpha_supervision/*.seal.sha256) must be refreshed in the SAME step as every
write to those files — the mirror-side sidecars alone are not enough. Lanes
preflight against the local sidecars; five were stale for two days and produced
repeated false custody alarms (Q-349, Q-351). The register/tracker/plan write
step is: edit file -> refresh LOCAL sidecar -> cp to mirror -> write mirror
sidecar -> shasum-verify both -> commit -> push.

## SURFACE-GEOMETRY-VERSUS-RAILS RULE (principal's steer, 2026-08-04, Q-427)

Every review of an exhibit, witness, or new-physics typing must separate two
questions and answer both explicitly:
1. SURFACE GEOMETRY: does the object prove something about the actual record
   surface's geometry (its real incidence/cycle/refinement structure), with
   the proof anchored in ratified surface data?
2. RAILS: or does it merely satisfy conditions our own formalism installed
   (the categories, functors, refinement machinery, certificate shapes) —
   conditions that could be met by formal bookkeeping with no geometric
   content?
Additionally: any object previously typed GENUINELY_NEW_PHYSICS must be
re-examined for RAIL-ARTIFACT status — a requirement imposed by our
scaffolding rather than by the physics is not new physics and must not cost
declaration; it is a candidate for removal or derivation at the rail level.
A review verdict that does not state the geometry/rails split is incomplete.
