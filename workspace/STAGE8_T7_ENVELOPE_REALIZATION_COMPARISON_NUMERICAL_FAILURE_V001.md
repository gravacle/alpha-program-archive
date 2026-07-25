# Stage-8 T7 Envelope-Realization Comparison Numerical Failure v001

Date: 2026-07-24

## Preserved failure

The primary ER-A/ER-B calculation completed all predeclared cases with
second-order time convergence. The independent midpoint verifier nevertheless
returned:

```text
pass=false
```

under the predeclared `5e-5` tolerance.

The blocking row was the `n=2`, `ell=1`, ER-B pure-state comparison:

```text
midpoint 48 to 96             = 8.843933693263647e-5
midpoint 96 to Strang 48      = 9.127694452617308e-5
```

The ER-B interaction is stronger than ER-A and the discrepancy follows the
observed second-order time-step trend. No tolerance is changed and no row is
dropped.

## Authorized remediation

A successor may change only numerical resolution:

```text
primary Strang steps:        24,48,96
independent midpoint steps:  96,192
tolerance:                   unchanged at 5e-5
all branches/states/cases:   retained
```

No envelope, state, operator, quadrature rule, or physical interpretation may
change in that successor.

```text
envelope_comparison_v001_verified = false
ER_A_selected = false
ER_B_selected = false
envelope_realization_derived = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
