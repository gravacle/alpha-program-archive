# F'-5 Provenance Erratum, and a Correction to One Forcing Ground V001

Date: 2026-07-27

## Status

```text
APPEND-ONLY ADDENDUM to STAGE8_IS_RL2B_FAILURE_FORCED_BY_F5_DETERMINATION_V001
  83750234b1fc072e915580c230bad796ca5d66df2332795356713062786fb242
THAT ARTIFACT IS NOT EDITED. Its ANSWER — NOT FORCED — IS UNCHANGED AND IS STRENGTHENED.
ONE OF ITS FOUR GROUNDS IS CORRECTED, and a separate erratum is raised against a different
sealed artifact.
No spec edited. F'-5 not amended. PRODUCTION PROHIBITED. alpha_computed = false.
```

## 1. ERRATUM AGAINST F'-5 ITSELF — it claims verbatim binding of a clause it strengthens

F'-5 opens `"SPEC-HEADER SCOPING CLAUSE 1 BINDS VERBATIM."` **The clause it cites says
materially less than F'-5 says.** Both quoted, verified at source by this lane:

```text
PARENT — STAGE8_T7_CONNECTED_LINKED_CLUSTER_MAJORANT_DERIVATION_SPEC_V001.md:61-72, VERBATIM:
  "1. CONSTANTS ARE CARRIER-INDEX-BLIND. Every constant, radius, decay rate,
      and tolerance in this spec — including `eta` and `epsilon_star` — is an
      explicit functional of the tuple
         (||b_D||, tau_R, sea-kernel decay data, p_lambda)
      ONLY. No constant may depend on the Hermite carrier index `n`, on `ell`,
      on a truncation level, or on any cellulation-family index. A constant
      whose derivation smuggles in a carrier index is a spec violation and
      BLOCKS."

F'-5 — STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:1671-1677, VERBATIM:
  "SPEC-HEADER SCOPING CLAUSE 1 BINDS VERBATIM. Every constant, radius,
   decay rate and tolerance is an explicit functional of (||b_D||, tau_R,
   sea-kernel decay data, |w_lambda|) ONLY. No carrier index n, no ell, no
   truncation level, no cellulation-family index, AND NO CELLULATION
   GEOMETRIC DATUM. The SUPREMUM OVER ADMITTED CELLS is the ENFORCEMENT
   MECHANISM of this clause (CR.R5), not a definitional convenience — which
   is why R-L0 is a real obligation and not a formality. Violation BLOCKS."

THREE MATERIAL DIFFERENCES UNDER A "BINDS VERBATIM" CLAIM:
  (i)  *** "AND NO CELLULATION GEOMETRIC DATUM" IS NOT IN THE PARENT. ***
       The parent forbids a cellulation-family INDEX — a label. F'-5 forbids any cellulation
       GEOMETRIC DATUM — |C|_4, diameter, aspect ratio. THESE ARE DIFFERENT PROHIBITIONS, and
       the second is the one the forcing question is entirely about.
  (ii) THE ENFORCEMENT-MECHANISM SENTENCE IS NOT IN THE PARENT. "cellulation geometric datum"
       and "enforcement mechanism" both return ZERO occurrences in the parent spec.
  (iii) THE TUPLE'S FOURTH ENTRY DIFFERS: parent `p_lambda`, F'-5 `|w_lambda|`. Different
       objects, in the admissible-tuple that defines what every constant may depend on.

AND THE PARENT'S CLAUSE IS TITLED "CONSTANTS ARE CARRIER-INDEX-BLIND." Its subject is the
CARRIER axis. The cellulation-GEOMETRY axis is F'-5's own extension.

WHY THIS IS A DEFECT AND NOT PEDANTRY: a lane reading F'-5 would believe the
cellulation-geometric-datum prohibition carries PARENTAL authority. It does not — it is this
program's own addition, presented under a verbatim-binding claim. F'-5 is a governing fence
whose violation BLOCKS, so the provenance of each of its prohibitions is load-bearing.
NOT ACTED ON. F'-5 is not edited, not weakened, and still binds as sealed. Reported as a
finding for the principal, who alone may touch it.
```

## 2. CORRECTION TO GROUND (A) OF THE FORCING DETERMINATION

```text
WHAT I SEALED: "F'-5 IS A TRANSMITTER, NOT THE SOURCE OF THE DEMAND."
WHAT IS CORRECT: F'-5 transmits the PER-CELL demand — that is genuinely parental, sealed in
  parent D5 (818083a5:192-196) and O4/M2 — but it ORIGINATES the CELLULATION-GEOMETRIC-DATUM
  PROHIBITION, which is the specific clause the forcing question asks about.
SO GROUND (A) DOES NOT CARRY THE WEIGHT I PUT ON IT. Half of it stands; the half that mattered
most to the forcing question does not.
THE ANSWER IS UNCHANGED. It rests on grounds (B), (C), (D) and the two counterexamples:
  (B) the seven closed mechanisms are closed by algebra and physics; not one is F'-5.
  (C) where F'-5 bites, the operative clause is the CARRIER-INDEX prohibition — NOW REINFORCED,
      because the parental authority is titled "CARRIER-INDEX-BLIND" and is about that axis and
      no other.
  (D) the corpus's own prescribed repair (B-5 arm (a)) contemplates a per-cell functional with a
      compensating scale weight, which a forced incompatibility would not.
  AND M2's certification was still BLOCKED before F'-5 existed, which stands independently.
```

## 3. COUNTEREXAMPLE 2 IS STRENGTHENED BY THIS ERRATUM

```text
Route T / O3+O7 lives in the PARENT majorant spec, where F'-5 does not exist. Given §1, that
means Route T operated under a fence that forbade CARRIER INDICES and CELLULATION-FAMILY
INDICES ONLY — and did NOT forbid cellulation geometric data at all.
IT FAILED ANYWAY, and it failed for O7's REFUTED INTERTWINER: the (3/8)^k record-tier witness
plus the absence of a small parameter.
SO A ROUTE THAT WAS FREE OF THE VERY PROHIBITION IN QUESTION FAILED FOR REASONS UNRELATED TO IT.
That is a cleaner counterexample than the determination stated, and it is the strongest single
piece of evidence for NOT FORCED in the whole investigation.
```

## 4. SEPARATE ERRATUM — A SEALED NEGATIVE EXISTENTIAL CONTRADICTED BY ITS OWN ARTIFACT

```text
STAGE8_T7_REFINEMENT_DEPENDENCE_ADDENDUM_V001.md:52-60 records, as VERIFIED AT SOURCE:
    "aspect ratio"       0
MEASURED THIS DATE: "aspect ratio" occurs THREE TIMES IN THAT SAME FILE — at :58 (the count line
itself) and SUBSTANTIVELY at :158-159, "unbounded aspect ratio; companion beta for G_cm.
Downstream: the common wall B-L2*, in a form blind to ASPECT RATIO as well as to carrier".
It also occurs elsewhere in the corpus: the sliver attempt (:99-108, :122-124) and the C_ref
determination (:85-88).

THE IRONY IS ON THE RECORD AND BELONGS THERE: the passage introducing that count says it used
"multiple spellings deliberately, because a negative existential from a single grep pattern is
exactly the error that produced this lane's P-X4 miss." It then produced the same error.
EITHER the count predates :158-159 within the same artifact, OR it is simply wrong. Both are
possible; this lane does not adjudicate which, and either way A SEALED NEGATIVE EXISTENTIAL IS
CONTRADICTED BY ITS OWN DOCUMENT.

WHAT SURVIVES: the addendum's §4 conclusion — SHAPE IS NOT THE DECIDING AXIS — does NOT rest on
this count. It rests on the alpha = 0 pathology arising INSIDE the shape-regular class, which is
a different and undisturbed ground. THE CONCLUSION STANDS; THE SUPPORTING COUNT DOES NOT.
WHAT DOES NOT SURVIVE: any use of "the corpus never discusses aspect ratio" as evidence. It
discusses unbounded aspect ratio in at least three artifacts, and the admitted class is sealed
as having it.
```

## 5. DISCLOSURE OF METHOD

```text
BOTH ERRATA ORIGINATED WITH AN INVESTIGATING AGENT THAT FLAGGED THEM AGAINST ITSELF, under the
invention-check requirement, as reasoning the corpus does not contain and as non-load-bearing for
its verdict. It was right to flag them and right that they did not change its verdict. This lane
VERIFIED BOTH AT SOURCE BEFORE SEALING THEM and is recording them because they bear on artifacts
other lanes read.
NEITHER ERRATUM WAS SOUGHT. Both were found while checking a claim that pointed the other way.
```

## Protected status

```text
amends = STAGE8_IS_RL2B_FAILURE_FORCED_BY_F5_DETERMINATION_V001 (83750234...)
prior_artifact_edited = false
answer_changed = false                  (NOT FORCED stands, and is strengthened)
ground_A_corrected = true               (transmitter claim half-right; the load-bearing half wrong)
grounds_carrying_the_answer = B, C, D + both counterexamples
counterexample_2_strengthened = true
F5_claims_verbatim_binding_of_a_clause_it_strengthens = true
  added_by_F5_not_in_parent = "AND NO CELLULATION GEOMETRIC DATUM"; the enforcement sentence
  tuple_discrepancy = parent p_lambda  vs  F'-5 |w_lambda|
parent_clause_title = "CONSTANTS ARE CARRIER-INDEX-BLIND"
F5_edited = false
F5_weakened = false
sealed_count_contradicted = STAGE8_T7_REFINEMENT_DEPENDENCE_ADDENDUM_V001:58 ("aspect ratio" 0)
measured_occurrences_in_that_file = 3
addendum_section4_conclusion_survives = true   (rests on a different ground)
adjudicated_which_cause = false
production_authorized = false
alpha_computed = false
proof_authorized = false
```
