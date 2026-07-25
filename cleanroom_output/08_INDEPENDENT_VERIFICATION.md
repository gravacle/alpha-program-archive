# 08 — Independent Verification

`OUTPUT/verify_independently.py` re-verifies from scratch (no package
imports, `require()`-based, `python -O`-safe) every identity this run's
conclusions rely on:

1. Bridge overlap minimum (2p−1)² at θ=π; orthogonality iff p=1/2 (200
   random populations).
2. Binary-closure autocorrelation minimum |2p−1|; exact zero only at
   (p=1/2, x=π).
3. Conditioned-star characteristic polynomial λ(λ²−2) → spectrum
   {−√2, 0, +√2}; τ_R = π/√2 is the least positive orthogonality zero
   (zero-clustering scan over 200k points).
4. Causal-diamond four-volume πT⁴/24 (quadrature vs closed form, <1e-9).
5. Closure trial potentials V1/V2: exact rational stationarity, positive
   curvature 8n, distinct stable radii 1 vs √2 (Fraction arithmetic).
6. Many-record counterfamily B_λ: identical one-record data, five distinct
   full spectra.

Result of both runs on this host (`/usr/bin/python3`, 3.9.6):

```
ALL CHECKS PASS  (normal run exit 0; python -O run exit 0)
```

Additionally, within the sealed lanes: the two negative-gate scripts and
their 6 pytest tests re-executed with byte-identical sealed outputs; the
Schur-pole compression was re-verified at 50 independent random momenta; the
chiral-gate algebra at 100 random trials; every other packaged script that
exists in the handoff ran with outputs matching its contract-frozen record.

Scope statement: this verification covers the run's re-derived mathematics
and the package's present executables. It does not — and cannot — verify
the 21 absent subordinate audit scripts, the V013 authority execution, the
V156 conditional base, or any unexecuted BID gate. `alpha_computed = false`.
