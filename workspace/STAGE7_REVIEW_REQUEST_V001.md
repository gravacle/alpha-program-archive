# Stage-7 Independent Review Request v001

Date: 2026-07-24

## Division of labor

The construction lane stops after this packet is assembled.

The following three reviews must be performed in separate fresh Fable
contexts:

```text
R1 mathematical and operator review;
R2 physical and QED-completeness review;
R3 provenance, target-blindness, and implementation review.
```

The construction lane has supplied one optional self-review voice. It is
labeled non-independent and cannot count toward R1-R3.

## Governing rule

Use the least-favorable status when a summary conflicts with a detailed
result. Do not repair or reinterpret the candidate during review. Report the
exact failed obligation and preserve all negative results.

## Required review outputs

Each reviewer should return:

```text
PASS, BLOCK, or PASS_WITH_EXPLICIT_SCOPE;
findings ordered by severity;
the exact authority file and line or equation involved;
whether any premise is hidden or relocated;
whether the candidate is target-value-free in execution;
and whether Stage 8 cross-execution may begin.
```

Unanimity is required before any Stage-8 seal. A disagreement is a block
until reconciled in a new append-only construction version.

## Fixed status

```text
reviews_R1_R2_R3_executed_by_construction_lane = false
independent_review_unanimity_obtained = false
stage8_authorized = false
alpha_computed = false
proof_authorized = false
```
