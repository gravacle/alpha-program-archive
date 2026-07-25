# Complete-Qspec Analytic-Continuation Preflight Failure v001

Date: 2026-07-25

## Verdict

```text
ANALYTIC_CONTINUATION_V003_PREFLIGHT_BLOCKED
```

The sealed v003 repair stopped before the complex-disk calculation because
the preregistered Cauchy-Riemann residual was required to decrease when the
centered-difference step changed from `1e-5` to `5e-6`.

## Observed values

At the three frozen points, the repaired residuals were:

```text
theta=i/200
  h=1e-5: 6.01831768023092e-11
  h=5e-6: 1.6530131332838935e-10

theta=(1+i)/(200 sqrt(2))
  h=1e-5: 7.8059544294538e-11
  h=5e-6: 1.6669042137962679e-10

theta=(-1+2i)/1000
  h=1e-5: 6.71138269870618e-11
  h=5e-6: 1.663529070025398e-10
```

All repaired residuals are far below the frozen `1e-8` accuracy threshold,
but halving the step increases cancellation error at double precision. The
monotonic-decrease clause therefore fails exactly as written.

The superseded conjugate-based construction returned residuals near
`1.1547` at every point, so the negative control fires by more than three
orders of magnitude.

The repaired generator agrees exactly, to the emitted floating-point
representation, with the sealed Hermitian generator at all five real-axis
points.

## Disposition

No threshold is changed and the blocked v003 executable is not edited.
The successor must compare the centered differences to the independently
written exact derivative of:

```text
exp(+i theta/3), exp(-i theta/3).
```

That derivative check avoids treating non-monotone roundoff at an already
`1e-10` residual as a physical failure. The successor remains bound to the
same `1e-8` accuracy ceiling and the same conjugate-based negative control.

## Artifact ledger

```text
1f7e78a8a71dffb6ccf80614a78344ab170381d633fa91ce7483187673512c57  COMPLETE_QSPEC_ANALYTIC_CONTINUATION_REPAIR_SPEC_V001.md
776651fd0c7732e6eb0d91a6efa16d53290a1d4bdbbb632d2d09e32069491a40  scripts/derive_complete_qspec_periodic_analytic_continuation_v003.py
```

## Protected status

```text
analytic_complex_continuation_repaired = false
periodic_analytic_continuation_diagnostic_passed = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
