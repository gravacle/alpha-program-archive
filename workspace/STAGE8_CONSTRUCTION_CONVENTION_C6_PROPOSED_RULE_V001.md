# Stage 8 Construction Convention C6 - Proposed Rule v001

Date: 2026-07-29

Status: PROPOSED / AWAITING PRINCIPAL RATIFICATION. This artifact proposes a
sixth construction convention in the same style as the ratified C1-C5
conventions. It adopts nothing and changes no verdict, register row, seal,
obligation, or evaluator rule.

```text
C6_proposed = true
C6_ratified = false
principal_ratification_required = true
alpha_computed = false
proof_authorized = false
```

## C6 - Distinguish Scheme Breakdown From Physical Obstruction

Proposed rule:

```text
A lane may not record a failed expansion, divergent expansion parameter,
non-convergent series, undefined perturbative regime, regulator failure, or
coordinate/scheme singularity as a physical obstruction unless it separately
identifies the theory-side object that fails. Conversely, a genuine
theory-side obstruction may not be downgraded to a scheme limitation merely
because it first appears through a failing calculation.
```

Rationale:

```text
The statement "this machinery is undefined here" has a different type from
"the physics is singular here". Conflating them can close or block a route
without proving that the underlying object fails. The opposite conflation is
also unsafe: real structural circularity, missing operators, non-positive
physical Hessians, or ungenerated propagators may not be waved away as mere
perturbative inconvenience.
```

Stop case:

```text
When a lane cannot determine whether a breakdown is physical or schematic, it
must stop at that line, report both readings, mark the status UNCLEAR, and
adopt neither. It may record the obstruction as a C2-style sealable result only
with the uncertainty on its face.
```

Required report fields when C6 is invoked:

```text
scheme_object = the expansion, parameter, series, regulator, coordinate, or
  perturbative regime that failed
theory_object = the operator, action, state, measure, spectrum, or physical
  branch claimed to fail
bridge_claim = what would make the scheme failure imply the theory failure
status = PHYSICAL / SCHEME_ONLY / MIXED / UNCLEAR
```

## Flags

```text
rule_adopted = false
awaiting_principal_ratification = true
alpha_computed = false
proof_authorized = false
```
