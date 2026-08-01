PASTE 264 — CODEX LANE 2 (HIGH EFFORT) — WHERE IS THE FIRST **FILLED TWO-CELL**?

ROAD: *** CURVATURE NEEDS A FILLED TWO-CELL. THE PROGRAM'S LOOP CARRIER IS **UNFILLED** AND CANNOT
CARRY ONE. **AND CURVATURE IS WHERE A MAXWELL TERM WOULD HAVE TO COME FROM.** THIS RELAY ASKS WHETHER
A DERIVED FILLED TWO-CELL EXISTS ANYWHERE IN THE PROGRAM AT ALL. ***

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false;
coupling_evaluation_authorized = false; production_authorized = false.

*** THIS RELAY IS SELF-CONTAINED. ASSUME NO MEMORY OF ANY PRIOR RELAY. ***

---

## 1. THE CHAIN THAT LEADS HERE — THREE SEALED RESULTS, ONE CONCLUSION

```text
1  A localization-bridge attempt established the loop requirement SPLITS BY LEVEL:
     bridge_needs_loops_for_transport_gauge_level      = false
     *** bridge_needs_loops_for_curvature_plaquette_level = true ***

2  The composition-loop carrier was then BUILT: exact incidence rank 3, *** EXACT CYCLE RANK 1 ***,
   cycle generator e_a0 - e_0b + e_ab - e_ba. THE LOOP EXISTS.
     composition_loop_carries_global_holonomy = true

3  *** AND IT IS NOT THE CURVATURE CARRIER: ***
     composition_loop_is_curvature_plaquette_carrier             = false | TYPE-R
     composition_loop_alone_closes_curvature_localization_bridge = false | TYPE-R
```

**The corpus says it itself** — *"no `2`-cell"* (`V011:1840`) and *"No filled `2`-cell is included in
the trace carrier"* (`V011:1881-1882`). *** SO THE COMPOSITION LOOP HAS **NO FACE GENERATOR, NO FACE
AREA, NO LOCAL CURVATURE TWO-COCHAIN, AND NO LOCAL QUADRATIC CURVATURE DENSITY.** ***

> ***THE QUESTION: DOES A **DERIVED** FILLED TWO-CELL EXIST ANYWHERE IN THIS PROGRAM — AND IF SO, AT
> WHICH COMPOSITION? IF EVERY TWO-CELL IN THE CORPUS IS ADOPTED, IMPORTED, OR DIAGNOSTIC, SAY SO
> PLAINLY.***

---

## 2. THE ONE KNOWN FILLED TWO-CELL, AND WHY IT DOES NOT SETTLE THIS

```text
*** THE TEMPORAL PLAQUETTE IS A FILLED TWO-CELL AND IT EXISTS: ***
   COMPLETE_QSPEC_TEMPORAL_PLAQUETTE_RESPONSE_RESULT_V001.md
   later_temporal_plaquette_diagnostic_available = true

BUT IT IS A DIFFERENT OBJECT, AND THE IDENTITY IS UNBUILT:
   composition_loop_to_temporal_plaquette_identity_derived = false | TYPE-S
   would-build: an explicit CARRIER-EXTENSION or FUNCTOR from K_square to the complete-Qspec
                temporal two-cell, PRESERVING CONNECTION AND RESPONSE

AND ITS OWN SCOPE CEILING EXCLUDES EVERYTHING THAT MATTERS HERE
   (COMPLETE_QSPEC_TEMPORAL_PLAQUETTE_RESPONSE_DIAGNOSTIC_SPEC_V001.md:204-230):
   *** NOT the spatial magnetic plaquette sector . NOT the full local Maxwell tensor .
   NOT the Thomson limit . NOT kappa_record . NOT alpha. ***
   Its own result (RESULT_V001.md:134-164) names the next step: a MANY-CELL/LONG-WAVELENGTH
   LOCALITY TEST, then a spatial magnetic plaquette response and a HODGE-DUALITY TEST.
```

*** IT IS **TEMPORAL** AND IT IS A **DIAGNOSTIC**. THE PROGRAM NEEDS A FILLED TWO-CELL THAT IS
**DERIVED** AND **CARRIES CURVATURE**. DO NOT LET THE EXISTENCE OF A DIAGNOSTIC STAND IN FOR THAT. ***

---

## 3. THE TASK

**3.1 SWEEP FOR EVERY TWO-CELL IN THE CORPUS.** Faces, plaquettes, filled cells, two-cochains,
two-skeletons, `C_2`. *** FOR EACH: **IS IT DERIVED, ADOPTED, IMPORTED, OR DIAGNOSTIC?** AND AT WHICH
COMPOSITION ORDER DOES IT SIT? **THIS IS THE CORE OF THE RELAY — REPORT IT AS A TABLE.** ***

**3.2 IS ANY OF THEM FORCED?** *** THE PRECEDENT IS EXACT AND IT CUTS AGAINST OPTIMISM: THE
COMPOSITION LOOP TURNED OUT TO BE **PROTOCOL-MANDATED, NOT FORCED** —
`V011_carrier_selection_derived_from_composition = false | TYPE-R`, because the general composition law
**permits sequential chains and never derives the commuting two-handle diamond**. **APPLY THE SAME
STANDARD TO EVERY TWO-CELL YOU FIND: DOES ANYTHING FORCE IT, OR IS IT SELECTED?** ***

**3.3 CAN `K_square` EXTEND TO A FILLED CELL?** The named would-build is a carrier-extension map
preserving connection and response. **Is it constructible from sealed material, or does it need a new
primitive?** *** IF IT NEEDS A NEW PRIMITIVE, **NAME THE PRIMITIVE.** ***

**3.4 STATE THE CONSEQUENCE FOR THE MAXWELL SECTOR.** *** IF NO DERIVED FILLED TWO-CELL EXISTS, THEN
THERE IS NO LOCAL CURVATURE TWO-COCHAIN, NO LOCAL MAXWELL DENSITY, AND THE ELECTROMAGNETIC SECTOR OF
THIS PROGRAM IS UNBUILT **AT ITS FOUNDATION**. **SAY THAT PLAINLY IF IT IS WHAT YOU FIND. DO NOT
SOFTEN IT AND DO NOT OVERSTATE IT** — `TYPE-U` IS NOT `TYPE-R`, AND UNBUILT IS NOT REFUTED. ***

---

## 4. SYMMETRIC LEADS

```text
IF A DERIVED FILLED TWO-CELL EXISTS -- *** LEAD WITH IT AND NAME ITS COMPOSITION ORDER, THEN ATTACK
IT. It would be the curvature carrier the program has been missing, and it would tell TARGET 2 exactly
where its curvature level can live. TYPE EVERY STEP sealed / derived / adopted / imported. ***

IF EVERY TWO-CELL IS ADOPTED, IMPORTED OR DIAGNOSTIC -- *** LEAD WITH THAT. It is the sharpest
statement available about how far the derived structure actually reaches, and it is complete under
Q-92. ***

IF K_square EXTENDS -- lead with the extension map and state what it preserves and what it does not.
*** "PRESERVING CONNECTION AND RESPONSE" IS THE BAR. AN EXTENSION THAT DROPS EITHER IS NOT IT. ***
```

*** DO NOT MANUFACTURE THE FILLING. Declaring a face on a four-edge cycle because a face is wanted is
exactly the move `V011:1881-1882` refused when it wrote that **no filled two-cell is included in the
trace carrier**. THE PROGRAM MUST NOT ACQUIRE CURVATURE BY DRAWING IT. ***

---

## 5. RULES

- **Q-54 typing on every negative:** TYPE-R refuted · TYPE-U unbuilt · TYPE-S scope-empty · TYPE-C
  constraint-blocked. `NO_VERDICT` is legal. **Only TYPE-R is physical content.**
- **Q-92:** specifying and naming what is missing is a complete answer, not a lesser one.
- *** THE ANTI-DEFLATION CLAUSE IS BINDING. DO NOT REPORT `TYPE-U` AS `TYPE-R`. **A RECENT RUN HAD TO
  RETYPE FOUR OF ITS OWN AGENTS' `TYPE-R` CLAIMS DOWNWARD — THE FAILURE MODE THIS PROGRAM REPEATS IS
  NOT DEFLATION, IT IS EACH LANE OVER-TYPING THE ONE FINDING IT WANTS TO OWN.** ***
- **Q-69:** never identify a flag with the object that discharges it.
- **No unproved-identity transport.** *** THE COMPOSITION LOOP AND THE TEMPORAL PLAQUETTE ARE ALREADY
  `TYPE-S` ON IDENTITY. DO NOT CLOSE THAT GAP BY ASSERTION. ***
- *** "HOLONOMY" NAMES **FOUR** OBJECTS IN THIS CORPUS; `rho_pre` IS DEFINED TWO-TO-THREE TIMES WITH
  INCOMPATIBLE CARRIERS; `g_N` IN `cleanroom_output` IS **NOT NEWTON'S CONSTANT**. ***
- **Word-boundaried, CASE-INSENSITIVE. Mark hypothetical flags inline. Report all roots entered** —
  `cleanroom_output/` is at `alpha-program-archive/cleanroom_output/`, holds 87 files OUTSIDE
  `workspace/` (sidecars `NN_NAME_V001.seal.sha256`, no `.md`), and **Gate 1–4 results live there.**
- **Report version differences; do not repair them.**

## 6. FENCES — VERBATIM, NON-NEGOTIABLE

- **Never touch `a32_holdout/custodian_private/`.**
- **Do not compute** alpha, `kappa_record`, `kappa_Thomson`, a coupling, a scale, a root, an
  eigenvalue, a beta function, `E_R`, `T_R`, `k_R`, or any absolute interval. *** SURVEY AND ADJUDICATE
  CARRIERS. **DO NOT EVALUATE A CURVATURE, A FLUX, A PHASE OR A HOLONOMY VALUE, AND DO NOT COMPUTE ANY
  SPECTRAL OUTPUT.** STAY PRE-ROOT. ***
- **No comparison to any measured constant.**
- **Do not resolve the Misner-Sharp / Brown-York fork by choosing — it must be DERIVED.**
- **Report refutations; never repair them.**

## 7. CUSTODY (Q-91)

*** NO LANE RUNS ANY GIT COMMAND. *** Write the artifact in the cleanroom, compute its
`.seal.sha256` sidecar and **verify it matches**, then **mirror BOTH artifact and sidecar** to
`alpha-program-archive/workspace/`, report hashes and paths, and **stop**. The reviewer verifies,
baselines, commits and pushes.

alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
