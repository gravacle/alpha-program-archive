# Stage-8 T7 Exact-State Envelope Comparison Spec v001

Date: 2026-07-24

## Purpose

Repeat the higher-resolution ER-A/ER-B Hermite-Galerkin calculation after
replacing the under-converged mixed-state quadrature by the independently
verified analytic covariance.

## Pinned state authority

```text
395141f2d3146d638b5c395b14a06eaa347701aec4f3cd6715befc6f8cda2464  stage8_execution/work/T07_exact_hermite_mixed_covariance.npz
be73577dc66ab712457ec1f6ac3bebdc30cbd983a3cb7113092aacbf057c3973  stage8_execution/work/T07_exact_hermite_mixed_covariance.json
7484f436ee2b1b241b6ab6bf75b6b76645b5b456f729ccaeea124baceb6be5ca  stage8_execution/work/T07_exact_hermite_mixed_covariance_verification.json
```

The pure finite state remains:

```text
C_n^pure=1_(-infinity,0)(Q_n h_0 Q_n).
```

Its finite non-nesting and strong convergence are both retained explicitly.

## Immutable branch and numerical data

```text
ER-A: v_A(t)=tau_R 32 r(t)^3;
ER-B: v_B(t)=24 tau_R/pi;
n in {2,4};
ell in {1,sqrt(2)};
primary Strang N_t in {24,48,96};
secondary spatial quadrature at N_t=96;
all three record histories;
both exact-mixed and finite-pure states.
```

No branch, state, case, or history may be selected after evaluation.

## Verification expansion

The independent verifier must:

1. cover all four `(n,ell)` cases and both envelope branches;
2. compare every history unitary before determinant evaluation;
3. compare every mixed and pure history determinant before signed summation;
4. compare the final completed amplitudes;
5. retain the independent full-Hamiltonian midpoint check for
   `n=2,ell=1`;
6. retain the existing exact small-Fock Klich identity as a separate
   algebraic authority;
7. report cancellation factors and determinant condition numbers.

High-precision determinant confirmation is required for the worst
conditioned or most strongly cancelled `n=2` row. It checks numerical
stability only; it cannot validate the physical continuum.

## Verdict

```text
EXACT_STATE_ENVELOPE_DIAGNOSTICS_VERIFIED
  iff the primary convergence checks and the expanded independent verifier
  all pass.

EXACT_STATE_ENVELOPE_DIAGNOSTICS_BLOCKED
  otherwise.
```

Even a pass does not select ER-A or ER-B and does not establish determinant
or response convergence.

```text
ER_A_selected = false
ER_B_selected = false
envelope_realization_derived = false
exact_mixed_covariance_derived = true
pure_state_strong_convergence_derived = true
global_determinant_convergence_derived = false
sharp_cell_implementability_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
