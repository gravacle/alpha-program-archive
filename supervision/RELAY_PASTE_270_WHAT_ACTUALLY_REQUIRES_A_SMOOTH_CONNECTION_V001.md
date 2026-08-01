PASTE 270 — CODEX LANE 2 (HIGH EFFORT) — [TASK 1b] WHAT, DOWNSTREAM, **ACTUALLY REQUIRES** A SMOOTH CONNECTION?

ROAD: *** A RECORD-SIDE CONNECTION IS NOW **DERIVED**. THE SMOOTH ONE IS NOT, AND FOUR BUILDS HAVE
FAILED TRYING. **BEFORE FUNDING A FIFTH, ESTABLISH WHETHER ANYTHING DOWNSTREAM REQUIRES SMOOTHNESS —
OR WHETHER THE DERIVED DISCRETE CONNECTION ALREADY DOES THE WORK.** IF NOTHING REQUIRES IT, TARGET 2
IS NOT BLOCKED. IT IS UNNECESSARY. ***

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false;
coupling_evaluation_authorized = false; production_authorized = false.

*** THIS RELAY IS SELF-CONTAINED. ASSUME NO MEMORY OF ANY PRIOR RELAY. ***

---

## 1. WHAT IS NOW SETTLED

**`STAGE8_PRPS_SMOOTH_PHRASING_IMPORT_ADJUDICATION_V001.md`, `e09349f5…`:**

```text
DISCRETE_GATE4_CONNECTION_CONDITIONAL_EXISTS         = true
GATE4_SATISFIES_DISCRETE_CONNECTION_CONDITIONAL      = true
*** INTERNAL_RECORD_SIDE_CONNECTION_DERIVED = true | DISCRETE_GATE4_SCOPE ***

SMOOTH_PRPS_CONNECTION_DERIVED_FROM_RECORD_STRUCTURE = false | TYPE-U
DISCRETE_CONNECTION_DELIVERS_PRPS_SMOOTH_CONNECTION  = false | TYPE-R
```

**Four attempts to build the smooth bridge failed, each lower than the last:** the bridge does not
build (`TYPE-U`); the functor is a map per chosen cover and "functor" is aspirational; the nerve
realization cannot be tested; and the patches came back **five-way `TYPE-S` — nothing in the corpus
defines a record-side patch space, cover, topology, or smooth structure at all.**

*** SO THE PROGRAM HAS A DERIVED CONNECTION AND A MISSING **UPGRADE**. THE QUESTION IS WHETHER IT
NEEDS THE UPGRADE. ***

---

## 2. THE PROPOSITION UNDER TEST — AND ITS SOURCE IS SEALED TEXT, NOT AN OPINION

**The corpus's own origin definition of the allow/require boundary says, in its summary table:**

> *** "ALLOWED `U(1)` holonomy, **REQUIRED** charge/flux access." ***

**And a sealed adjudication (`58fd2e60…`) established that what decides allow versus require is
A TRACE CONDITION AND FOUR SPECTRAL/SECTOR CONDITIONS — not graph topology, and not smoothness.**

> ***THE PROPOSITION: IF WHAT IS **REQUIRED** IS CHARGE/FLUX ACCESS, AND THE DERIVED DISCRETE
> CONNECTION SUPPLIES COMPARISON AND TRANSPORT, THEN **SMOOTHNESS MAY BE DOING NO REQUIRED WORK** AND
> THE SMOOTH UPGRADE IS OPTIONAL RATHER THAN BLOCKING.***

---

## 3. THE TASK — THIS IS A DEPENDENCY AUDIT, AND IT MUST BE EXHAUSTIVE

**3.1 ENUMERATE EVERY DOWNSTREAM OBLIGATION THAT NAMES A CONNECTION.** *** FOR EACH: **DOES IT REQUIRE
A SMOOTH CONNECTION SPECIFICALLY, OR ONLY A COMPARISON/TRANSPORT STRUCTURE THE DISCRETE ONE ALREADY
SUPPLIES?** QUOTE PATHS AND LINES. **A LIST IS THE DELIVERABLE.** ***

**3.2 THE NAMED CANDIDATE, AND IT IS THE MOST IMPORTANT ROW.** `physical_public_EM_connection_derived`
is step 1 of a four-step discharge route sitting under alpha's normalization. *** DOES STEP 1 REQUIRE
**SMOOTHNESS**, OR DOES IT REQUIRE **CHARGE/FLUX ACCESS** AND A PUBLIC COMPARISON STRUCTURE? **READ
THE ROUTE'S OWN TEXT. DO NOT INFER FROM THE WORD "CONNECTION".** ***

**3.3 WHERE DOES SMOOTHNESS ENTER AS A GENUINE REQUIREMENT, IF ANYWHERE?** *** CANDIDATES TO CHECK
DELIBERATELY: the local Maxwell tensor · curvature and the exterior derivative `d` in `D = d - i a` ·
the continuum/refinement limit · Ward identities · the Thomson response · the CTP continuum sector.
**SOME OF THESE MAY GENUINELY NEED A MANIFOLD. SAY WHICH.** ***

**3.4 WHAT WOULD A DISCRETE-ONLY PROGRAM FORFEIT?** *** NAME IT CONCRETELY. **IF THE ANSWER IS "THE
LOCAL MAXWELL FORM AND THEREFORE THE EM SECTOR", THAT IS A COMPLETE ANSWER AND IT SETTLES THE ROAD IN
THE OPPOSITE DIRECTION.** DO NOT SOFTEN IT. ***

**3.5 VERDICT.** Is the smooth upgrade **REQUIRED**, **OPTIONAL**, or **REQUIRED ONLY FOR A NAMED
SUBSET**? *** NAME THE SUBSET. ***

---

## 4. *** THIS IS THE PRINCIPAL'S PROPOSAL AND THE TRACK RECORD ON THIS TERRAIN IS BAD ***

*** THE PRINCIPAL'S PREVIOUS ALLOW/REQUIRE HYPOTHESIS WAS **REFUTED THREE WAYS** BY A LANE EXPLICITLY
TOLD NOT TO FLATTER HIM, AND THAT WAS THE CORRECT OUTCOME. THE REVIEWER HAS PROPOSED SIX COLLAPSES:
FOUR REFUTED, ONE HALF RIGHT. **THE SOURCE OF A PROPOSAL CHANGES NOTHING ABOUT THE STANDARD OF
PROOF.** ***

```text
IF NOTHING DOWNSTREAM REQUIRES SMOOTHNESS -- *** LEAD WITH IT, THEN ATTACK IT HARDEST. It would
convert four failed builds from a blockage into a MOOT ROAD, and it would mean the program's derived
connection is already sufficient for what comes next. THAT IS A LARGE CLAIM AND NEEDS THE STRONGEST
EVIDENCE IN THE FILE. ***

IF SOMETHING DOES -- *** LEAD WITH IT AND NAME IT EXACTLY. One genuine requirement settles this, and
the program then knows TARGET 2 must be built or explicitly adopted. That is worth more than a
comfortable "optional". ***

IF IT SPLITS -- *** LEAD WITH THE SPLIT. "Required for the local Maxwell tensor, not required for
comparison and transport" would be the most useful sentence in this file. ***
```

*** DO NOT MANUFACTURE INDEPENDENCE. An obligation that "does not mention smoothness" is not thereby
smoothness-free — **CHECK WHAT ITS OWN MACHINERY USES.** `D = d - i a` contains an exterior derivative;
anything consuming that consumes a smooth structure whether or not it says so. ***

---

## 5. RULES

- **Q-54 typing on every negative:** TYPE-R refuted · TYPE-U unbuilt · TYPE-S scope-empty · TYPE-C
  constraint-blocked. `NO_VERDICT` is legal. **Only TYPE-R is physical content.**
- **Q-92:** specifying and naming what is missing is a complete answer, not a lesser one.
- *** THE ANTI-DEFLATION CLAUSE IS BINDING. DO NOT REPORT `TYPE-U` AS `TYPE-R`. ***
- **Q-69:** never identify a flag with the object that discharges it.
- **No unproved-identity transport.** *** "A CONNECTION", "A COMPARISON STRUCTURE", "A TRANSPORT" AND
  "A SMOOTH `U(1)` GAUGE FIELD" ARE **NOT SYNONYMS**, AND THIS RELAY TURNS ENTIRELY ON KEEPING THEM
  APART. ***
- *** "HOLONOMY" NAMES **FOUR** OBJECTS IN THIS CORPUS; `rho_pre` IS DEFINED TWO-TO-THREE TIMES WITH
  INCOMPATIBLE CARRIERS; `g_N` IN `cleanroom_output` IS **NOT NEWTON'S CONSTANT**. ***
- *** THE GATE **RESULTS** REPORT PASSES BUT THE **GOVERNING SPEC'S OWN GATE FLAGS ARE STILL FALSE**,
  AND GATE 4's P2 TREE HALF IS PRINTED AS PASSED AND COVERED BY NO `require()`. **LEAN ONLY ON WHAT A
  GATE ACTUALLY EXECUTED.** ***
- **Word-boundaried, CASE-INSENSITIVE. Mark hypothetical flags inline. Report all roots entered** —
  `cleanroom_output/` is at `alpha-program-archive/cleanroom_output/`, holds 87 files OUTSIDE
  `workspace/` (sidecars `NN_NAME_V001.seal.sha256`, no `.md`), and **GATES 1–4 LIVE THERE.**
- *** 151 OF 649 `workspace/*.md` FILES HAVE NO SEAL SIDECAR. UNSEALED IS NOT DEFECTIVE HERE. DO NOT
  DISCOUNT AN ARTIFACT FOR BEING UNSEALED, AND DO NOT SEAL ANYTHING. ***
- **Report version differences; do not repair them.**

## 6. FENCES — VERBATIM, NON-NEGOTIABLE

- **Never touch `a32_holdout/custodian_private/`.**
- **Do not compute** alpha, `kappa_record`, `kappa_Thomson`, a coupling, a scale, a root, an
  eigenvalue, a beta function, `E_R`, `T_R`, `k_R`, or any absolute interval. *** THIS IS A DEPENDENCY
  AUDIT. IT EVALUATES NOTHING AND STAYS PRE-ROOT. ***
- **No comparison to any measured constant.**
- **Do not resolve the Misner-Sharp / Brown-York fork by choosing — it must be DERIVED.**
- *** DO NOT SUPPLY A SMOOTH DOMAIN FROM THE ADOPTED `(M,g)`. The adopted global-domain principle
  fixes a globally hyperbolic metric and carries an EINSTEIN-HILBERT BULK TERM three lines below.
  **IF AN OBLIGATION IS ONLY SATISFIABLE VIA `(M,g)`, RECORD THAT AS ITS PRICE — DO NOT PAY IT.** ***
- **Report refutations; never repair them.**

## 7. CUSTODY (Q-91)

*** NO LANE RUNS ANY GIT COMMAND. *** Write the artifact in the cleanroom, compute its
`.seal.sha256` sidecar and **verify it matches**, then **mirror BOTH artifact and sidecar** to
`alpha-program-archive/workspace/`, report hashes and paths, and **stop**. The reviewer verifies,
baselines, commits and pushes.

alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
