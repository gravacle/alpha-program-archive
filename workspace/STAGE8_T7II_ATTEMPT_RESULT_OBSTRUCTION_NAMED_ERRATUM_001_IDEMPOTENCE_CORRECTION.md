# T7(ii) Attempt Result Erratum 001 - Idempotence Correction

Date: 2026-07-28

Status: append-only erratum to
`STAGE8_T7II_ATTEMPT_RESULT_OBSTRUCTION_NAMED_V001.md`
(`0f76ab73d7b226899ad00e24a0be10636b49982620375bd10491b898ecc917c7`).
The source artifact is not edited in place.

## Scope

This erratum corrects one supporting clause in
`STAGE8_T7II_ATTEMPT_RESULT_OBSTRUCTION_NAMED_V001.md:96-102`.
It does not alter that artifact's conclusion:

```text
T7(ii) does not close.
The obstruction remains named at STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:346-352.
The live residue remains H-ANGLE: a uniform Friedrichs-angle lower bound between
consecutive per-cell ranges, proved from parent acts.
```

## Correction

The T7(ii) attempt conditionally consumed C-L1 and stated that, under C-L1,
the zero-history in-cell Kraus operator is the odd-parity projector `Pi_odd`,
"AN IDEMPOTENT."

That supporting clause is false.

`STAGE8_CL1_ATTEMPT_RESULT_REFUTED_V001.md`
(`efb08860b888e24acaa50fdafdbe4afdb868450f79ec23120c2bd3eb1d40ddbb`)
derives the corrected object in its section 7:

```text
sum_lambda w_lambda R_lambda = cos^2(8 pi rho^4) * I
```

Therefore, the zero-history in-cell Kraus operator is

```text
cos^2(8 pi rho^4) * I,
```

not `Pi_odd`, and it is not idempotent except at special radii where the scalar
factor is 0 or 1.

## Why The T7(ii) Conclusion Stands

The T7(ii) obstruction did not require idempotence. It required failure of a
simple leading mode with a uniform gap. The corrected scalar multiplier is still
a degenerate scalar action on the relevant leading sector, so the same
degeneracy obstruction remains. The attempted transfer-gap route still receives
no certified record-sector damping from C4, and the gap burden remains on the
uncertified sea tier unless H-ANGLE is proved from parent acts.

## Flags

```text
append_only_erratum = true
source_artifact_edited_in_place = false
T7ii_conclusion_changed = false
supporting_idempotence_clause_corrected = true
correct_zero_history_in_cell_Kraus_operator = "cos^2(8 pi rho^4) * I"
incorrect_zero_history_in_cell_Kraus_operator = "Pi_odd"
T7ii_zero_free_neighbourhood = false
alpha_computed = false
proof_authorized = false
```
