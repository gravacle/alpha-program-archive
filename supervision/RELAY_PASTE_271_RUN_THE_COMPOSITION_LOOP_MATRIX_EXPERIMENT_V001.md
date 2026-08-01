PASTE 271 — CODEX LANE 1 (HIGH EFFORT) — RUN V011's COMPOSITION-LOOP MATRIX EXPERIMENT

ROAD: *** THE EVALUATION FENCE HAS BEEN **LIFTED BY THE PRINCIPAL FOR THIS ONE ITEM**. IT IS FULLY
SPECIFIED, PRE-REGISTERED, PRE-ROOT, AND **MANDATED FOR CORE-RESULT-SEAL AT `V011:1790`** — AND IT HAS
NEVER BEEN RUN, BECAUSE A PRIOR RELAY'S FENCE BARRED IT. **THAT FENCE WAS A REVIEWER DEFECT. RUN
IT.** ***

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false;
coupling_evaluation_authorized = false; production_authorized = false.

*** THIS RELAY IS SELF-CONTAINED. ASSUME NO MEMORY OF ANY PRIOR RELAY. ***

---

## 1. *** THE AUTHORIZATION, AND ITS EXACT SCOPE ***

**`DECISION_OF_RECORD_004`, ruled by the principal 2026-08-01.** The evaluation fence is lifted for
**V011's composition-loop matrix experiment and nothing else.**

```text
PERMITTED -- and ONLY these six outputs, on B_square(Phi) over C_0(K_square) (+) C_1(K_square):
  the exact characteristic polynomial p_Phi(z) = det(z I_8 - B_square(Phi))
  the eight real eigenvalues in nondecreasing order, WITH MULTIPLICITY
  the exact kernel multiplicity
  Tr[B_square^2] over the full eight-dimensional carrier
  Tr[B_square^4] over the full eight-dimensional carrier
  R_square = Tr[B_square^4] / Tr[B_square^2]^2

*** STILL BARRED, UNCHANGED: alpha . kappa_record . kappa_Thomson . any coupling . any scale .
ANY ROOT OF C_record . any beta function . E_R . T_R . k_R . any absolute interval . any comparison
to any measured constant. THE LIFT IS ONE MATRIX AT ONE FROZEN PARAMETER VALUE AND EXTENDS TO
NOTHING ELSE. ***
```

---

## 2. THE OBJECT — VERBATIM FROM `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:1836-1935`

**Read it at source and use the spec's text, not this summary, wherever they could differ.**

```text
vertices: v_00, v_10, v_01, v_11
edges:    e_a0: v_00 -> v_10   e_0b: v_00 -> v_01   e_ab: v_10 -> v_11   e_ba: v_01 -> v_11

ordered loop holonomy:   u_ab u_a0 (u_ba u_0b)^(-1) = exp(i Phi)
fixed gauge:             u_a0 = 1, u_ab = 1, u_0b = 1, u_ba = exp(-i Phi)
per edge:                partial_rho,e x = u_e x v_target - x v_source
*** USE THE HILBERT FORMS PRODUCED BY GATE 3. NO FILLED 2-CELL IS IN THE TRACE CARRIER. ***

frozen ordered bases:    C_0: (v_00, v_10, v_01, v_11)     C_1: (e_a0, e_0b, e_ab, e_ba)

D_square(Phi) =
  [[-1, -1,  0,            0],
   [ 1,  0, -1,            0],
   [ 0,  1,  0,           -1],
   [ 0,  0,  1,  exp(-i Phi)]]

B_square(Phi) = [[0_(4x4), D_square(Phi)], [D_square(Phi)^dagger, 0_(4x4)]]
p_Phi(z) = det(z I_8 - B_square(Phi))

*** THE PREREGISTERED EVALUATION POINT IS  Phi = pi.  IT IS FROZEN IN THE SPEC. DO NOT EVALUATE AT
ANY OTHER VALUE, AND DO NOT SCAN. ***
```

---

## 3. THE TEST PROTOCOL — THIS IS THE CONDITION THE AUTHORIZATION RESTS ON

```text
1  *** SYMBOLIC IS AUTHORITATIVE. *** Compute p_Phi(z), the spectrum, the kernel multiplicity and
   both traces EXACTLY. "Zero means an exact algebraic zero" -- the spec's words.

2  *** THEN CODE A **SEPARATE** 100-DECIMAL NUMERICAL DIAGONALIZATION AS A CHECK. *** The spec
   requires it. **WRITE IT INDEPENDENTLY -- DO NOT DERIVE IT FROM THE SYMBOLIC PATH, OR IT CHECKS
   NOTHING.** Report agreement to stated precision.

3  *** IF SYMBOLIC AND NUMERICAL DISAGREE, THAT IS THE RESULT. LEAD WITH IT. DO NOT RECONCILE THEM
   AND DO NOT PICK ONE. ***

4  *** "No result may modify BID." *** The output is ONE-WAY. Do not adjust any spec, principle or
   flag to match it, and do not carry it into any downstream construction.
```

**Report `B_square` is Hermitian and the spectrum is real and symmetric about zero if that is what you
find** — *** AND IF IT IS **NOT**, SAY SO LOUDLY: A BIPARTITE BLOCK STRUCTURE PREDICTS `+/-` PAIRING,
AND A VIOLATION WOULD MEAN THE CONSTRUCTION IS WRONG SOMEWHERE. **THAT IS A FREE INTERNAL CONSISTENCY
CHECK AND YOU SHOULD RUN IT.** ***

---

## 4. WHAT THIS DISCHARGES — AND WHAT IT DOES **NOT**

```text
DISCHARGES  V011_composition_loop_prediction_sealed -- TYPE-U today, MANDATED at V011:1790 for
            CORE-RESULT-SEAL, never executed
```

*** IT DOES **NOT** MAKE THE COMPOSITION LOOP **FORCED**. A sealed result stands:
`V011_carrier_selection_derived_from_composition = false | TYPE-R` — V011's composition law **permits
sequential chains and never derives the commuting two-handle diamond** that would necessitate
`K_square`. `K_square_protocol_mandated = true`. **STRUCTURE DERIVED, SELECTION NOT DERIVED, AND
EVALUATING THE SPECTRUM CHANGES NEITHER. DO NOT REPORT OTHERWISE.** ***

*** AND STATE THE STANDING THE SPEC ITSELF DECLARES: **"This is a new forward mathematical
consequence, NOT AN EMPIRICAL HOLDOUT"** and **"It remains TARGET-AWARE because the broader program
knows its desired structures."** **BOTH SENTENCES MUST APPEAR IN YOUR ARTIFACT.** ***

---

## 5. RULES

- **Report every number you produce, including intermediate ones.** *** NO SUMMARY-ONLY REPORTING.
  THE SIX OUTPUTS ARE THE DELIVERABLE AND THEY GO IN THE ARTIFACT IN FULL. ***
- **Q-54 typing on every negative:** TYPE-R · TYPE-U · TYPE-S · TYPE-C. `NO_VERDICT` is legal.
- **Q-92:** naming what is missing is a complete answer.
- **Q-69:** never identify a flag with the object that discharges it. *** COMPUTING THE SPECTRUM IS
  NOT THE SAME AS SEALING THE PREDICTION — **SAY WHICH ONE YOU DID.** ***
- *** IF THE SPEC IS AMBIGUOUS ANYWHERE, **STOP AND REPORT THE AMBIGUITY. DO NOT RESOLVE IT BY
  CHOOSING.** A resolved-by-choice convention would silently become part of a CORE-RESULT-SEAL
  item. ***
- *** "HOLONOMY" NAMES **FOUR** OBJECTS IN THIS CORPUS. THE `Phi` HERE IS **SENSE 3, THE COMPOSITION
  LOOP**. IT IS **NOT** THE SEALED QUARTER-TURN `pi/2`. **DO NOT IDENTIFY THEM, DO NOT COMPARE THEM,
  AND DO NOT REMARK ON THEIR RELATIONSHIP.** ***
- **Report all roots entered.** `cleanroom_output/` is at `alpha-program-archive/cleanroom_output/`,
  87 files outside `workspace/`; **Gate 3's Hilbert forms are needed and Gates 1–4 live there.**
- **Report version differences; do not repair them.**

## 6. FENCES — VERBATIM

- **Never touch `a32_holdout/custodian_private/`.** *** THIS AUTHORIZATION DOES NOT TOUCH A32 AND MUST
  NOT BE CITED AS IF IT DID. ***
- **Beyond the six permitted outputs: compute nothing.** *** NO alpha, `kappa_record`,
  `kappa_Thomson`, coupling, scale, root of `C_record`, beta function, `E_R`, `T_R`, `k_R`, or
  absolute interval. **STAY PRE-ROOT.** ***
- **No comparison to any measured constant.** *** `R_square` IS DIMENSIONLESS. **DO NOT COMPARE IT TO
  ANYTHING.** REPORT IT AND STOP. ***
- **Do not resolve the Misner-Sharp / Brown-York fork by choosing.**
- **Report refutations; never repair them.**

## 7. CUSTODY (Q-91)

*** NO LANE RUNS ANY GIT COMMAND. *** Write the artifact in the cleanroom, compute its
`.seal.sha256` sidecar and **verify it matches**, then **mirror BOTH artifact and sidecar** to
`alpha-program-archive/workspace/`, report hashes and paths, and **stop**. The reviewer verifies,
baselines, commits and pushes.

alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
