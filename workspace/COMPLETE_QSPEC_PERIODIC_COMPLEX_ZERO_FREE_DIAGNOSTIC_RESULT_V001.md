# Complete-Qspec Periodic Complex Zero-Free Diagnostic Result v001

Date: 2026-07-25

## Verdict

```text
PERIODIC_COMPLEX_ZERO_FREE_DIAGNOSTIC_PASS
```

The frozen period-two sequential Qspec amplitude has no detected zero in
the preregistered complex disk `|theta|<=1/100` through volume 64.

## Results

```text
complex sample count                         113
volumes checked                              1 through 64
minimum sampled amplitude absolute           0.9941168003252292
maximum 48/96-step relative disagreement     2.3387483015482335e-05
largest boundary ratio discrepancy           4.013763891936296e-16
largest adjacent boundary phase increment    8.809367916627098e-04
nonzero winding numbers                      none
```

The minimum occurred at volume 64 on the disk boundary. Every volume had
zero winding around the sampled boundary.

## Runtime portability

The sealed v001 execution stopped before evaluating physics because SciPy
was unavailable. The append-only v002 implementation used a self-contained
order-13 Pade scaling-and-squaring exponential under a separately sealed
portability addendum:

```text
expm(0) identity error            2.220446049250313e-16
maximum Pade/eigh difference      1.094393863507478e-14
maximum real-axis unitarity error 2.860848553017826e-15
```

No scientific threshold changed.

## Scope

This is a numerical search, not a certified analytic zero-free theorem.
The finite angular/radial sample does not control every point between
samples, every volume above 64, arbitrary field profiles, or arbitrary
connected cellulations. It therefore does not authorize the thermodynamic
logarithm or linked-cluster theorem by itself.

## Artifact ledger

```text
fc2ca9ff890f3833a495107ae4619b3b341e009a1357ae2943836fd5ecf5456d  COMPLETE_QSPEC_PERIODIC_COMPLEX_ZERO_FREE_DIAGNOSTIC_SPEC_V001.md
01501e04a9935c6714599076c0503353350245ce094e6ad18e3e146d7ff9d53b  COMPLETE_QSPEC_COMPLEX_ZERO_FREE_RUNTIME_PORTABILITY_ADDENDUM_V001.md
704f5498d8ace502d1c23787a6d44436bb2dde2d1872c3048bc60a7dc7c8770f  scripts/derive_complete_qspec_periodic_complex_zero_free_v002.py
6ad27a95f1b480c694162f36694ec9f5dd91302e94e34094946babb93c33b089  stage8_execution/work/QSPEC_periodic_complex_zero_free_v002.json
```

## Status

```text
periodic_complex_zero_free_diagnostic_passed = true
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
local_Maxwell_response_derived = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
