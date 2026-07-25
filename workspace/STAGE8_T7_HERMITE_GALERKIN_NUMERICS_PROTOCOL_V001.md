# Stage-8 T7 Hermite-Galerkin Numerics Protocol v001

Date: 2026-07-24

This protocol fixes numerical verdict thresholds before the Hermite-Galerkin
baseline is evaluated.

```text
maximum Hermiticity error                 < 1e-11
maximum Clifford error                    < 1e-12
maximum mixed-covariance bound violation  < 5e-8
maximum pure-covariance projector error   < 1e-10
maximum propagated-unitary error          < 2e-10
```

For every fixed `(n,ell,state scheme)`, time convergence is accepted when:

```text
|a_24-a_48| < |a_12-a_24|;
```

and is classified as second-order-consistent when additionally:

```text
|a_12-a_24| / |a_24-a_48| > 3.
```

Primary/secondary quadrature agreement at 48 time steps requires:

```text
|a_primary-a_secondary| < 5e-4.
```

Movement with `n` and `ell` is reported but has no pass threshold at two
levels. It cannot establish regulator independence.

No tolerance may be widened after execution. A failed numerical verdict
may be followed only by a newly sealed successor protocol that identifies
the numerical cause without changing the physical construction.

All protected status flags remain false.
