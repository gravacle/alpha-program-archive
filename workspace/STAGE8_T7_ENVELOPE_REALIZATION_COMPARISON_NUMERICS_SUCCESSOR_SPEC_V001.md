# Stage-8 T7 Envelope-Realization Comparison Numerics Successor Spec v001

Date: 2026-07-24

## Purpose

Repeat the sealed ER-A/ER-B comparison at the higher time resolution
predeclared after the preserved v001 numerical failure.

## Immutable physics

All physical and mathematical content remains exactly that of:

```text
STAGE8_T7_ENVELOPE_REALIZATION_COMPARISON_SPEC_V001.md
```

In particular:

```text
ER-A: v_A(t)=tau_R 32 r(t)^3;
ER-B: v_B(t)=24 tau_R/pi;
n in {2,4};
ell in {1,sqrt(2)};
both mixed and pure finite state schemes;
both primary and secondary spatial quadratures;
no branch selection.
```

## Only authorized change

```text
primary Strang N_t:          {24,48,96}
secondary quadrature:        N_t=96
independent midpoint N_t:    {96,192}
independent tolerance:       5e-5, unchanged
```

## Verdict

```text
ENVELOPE_BRANCH_BASELINES_VERIFIED
  iff every primary convergence row improves and every independent row
  passes the unchanged tolerance.

ENVELOPE_BRANCH_NUMERICS_BLOCKED
  otherwise.
```

Even a pass does not select ER-A or ER-B.

```text
ER_A_selected = false
ER_B_selected = false
envelope_realization_derived = false
sharp_cell_implementability_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
