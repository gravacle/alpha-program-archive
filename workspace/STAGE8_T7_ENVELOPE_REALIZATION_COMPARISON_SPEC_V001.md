# Stage-8 T7 Envelope-Realization Comparison Spec v001

Date: 2026-07-24

## Purpose

Execute the two envelope realizations already disclosed at Stage 7 on the
same genuine Hermite-Galerkin parent, with both admissible finite state
schemes and no response-based branch selection.

This is a branch-sensitivity diagnostic. It does not decide the physical
envelope, compute a continuum response, or compute alpha.

## Pinned authorities

```text
e4cfaef14309b3acf5674f8c8faee756f744fec4691d5e01d9de0fa422592be2  R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md
202f8d8db60046a8069b1cd8fcc38f505eb95fa29578e094e005f56e967c3a35  STAGE7_QSPEC_SCOPE_AND_PREMISE_SUCCESSOR_V001.md
80aa4e1722c117e8195ce0fb2ae3fc37262bc8fc2ba5d79a6dd38cd1029bc26d  STAGE8_T7_HERMITE_GALERKIN_BASELINE_SPEC_V001.md
950e957ec2aa1022509b57df48f4f701e717e5dcbb18731332abbf55bf57dadd  STAGE8_T7_HERMITE_GALERKIN_NUMERICS_PROTOCOL_V001.md
```

The v001 scalar-density audit and its scope correction remain visible. The
support-projector theorem establishes that ER-A is internally normalized;
it does not select ER-A over ER-B.

## Frozen branches

For unit cell duration, `r(t)=min(t,1-t)`,
`V_4(D)=pi/24`, and `M(t)=1_(|x|<=r(t))`:

```text
ER-A:
  v_A(t)=tau_R * 32 r(t)^3.

ER-B:
  v_B(t)=tau_R / V_4(D)=24 tau_R/pi.
```

ER-A uses the intrinsic time marginal as the interaction amplitude. ER-B is
the unit-duration slice operator obtained from uniform spacetime density at
action level. Neither may be rescaled after evaluation.

## Frozen computation

Use exactly the Hermite-Galerkin carriers and numerics of the v001 baseline:

```text
n in {2,4};
ell in {1,sqrt(2)};
N_t in {12,24,48};
primary ball quadrature 10x10x20;
secondary N_t=48 quadrature 12x12x24;
C_mix=Q_n P_- Q_n;
C_pure=1_(-infinity,0)(Q_n h_0 Q_n).
```

For every `(envelope,n,ell,state,N_t)`, compute the signed three-history
completed amplitude. Report all values and all movements. The code may not
drop or rank branches by proximity to any coupling.

## Independent verification

For `n=2`, `ell=1`, independently reconstruct both branches with:

```text
24-node covariance quadrature;
14x14x28 ball quadrature;
full-Hamiltonian midpoint exponentials at N_t=48 and 96.
```

Compare each branch/state result with the primary Strang value under one
predeclared numerical tolerance.

## Predeclared verdicts

```text
ENVELOPE_BRANCH_BASELINES_COMPUTED
  iff every construction and numerical check passes.

ENVELOPE_BRANCH_NUMERICS_BLOCKED
  otherwise.
```

A positive verdict means only that both branch baselines are reproducibly
computed. It cannot select the physical branch. If the later normalized local
responses differ, the envelope selector remains load-bearing.

```text
ER_A_selected = false
ER_B_selected = false
envelope_realization_derived = false
physical_regulator_completed_record_baseline_derived = false
sharp_cell_implementability_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
