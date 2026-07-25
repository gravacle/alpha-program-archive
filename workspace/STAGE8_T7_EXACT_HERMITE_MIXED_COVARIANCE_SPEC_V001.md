# Stage-8 T7 Exact Hermite Mixed-Covariance Spec v001

Date: 2026-07-24

## Purpose

Replace the under-converged Cartesian Gauss-Hermite approximation of

```text
C_n^mix=Q_n P_- Q_n,
P_-(p)=[I-alpha.p/|p|]/2
```

with an analytic matrix-element calculation in the Hermite basis.

This is a regulator-state calculation. It uses no response, coupling, alpha,
endpoint, or measured constant.

## Analytic integral

Expand each product of normalized Hermite polynomials into Cartesian
monomials. Every direction-matrix element reduces to integrals

```text
I_(e_x,e_y,e_z)
 =integral_R3 x^e_x y^e_y z^e_z |p|^(-1) exp(-|p|^2) d^3p.
```

If any exponent is odd, `I=0`. For

```text
(e_x,e_y,e_z)=(2a,2b,2c),  S=a+b+c,
```

the exact radial-angular separation gives

```text
I
 =Gamma(S+1)
  Gamma(a+1/2)Gamma(b+1/2)Gamma(c+1/2)
  /Gamma(S+3/2).
```

The numerator polynomial for direction `j` has one additional power of
`p_j`. The Fourier-Hermite phase is fixed as `(-i)^degree`.

## Obligations

For `n in {2,4}`:

1. construct all three direction matrices analytically;
2. verify Hermiticity and the compressed-covariance bounds;
3. verify exact nested-subspace compatibility of the `n=2` block inside
   `n=4`;
4. report full operator-norm differences from Cartesian GH orders
   `16,20,24,28,32`;
5. show whether the GH sequence approaches the analytic matrix;
6. save the analytic covariance matrices for downstream reuse.

The old GH20 values remain finite diagnostics and may not be silently
rewritten.

## Verdict

```text
EXACT_HERMITE_MIXED_COVARIANCE_DERIVED
  iff the analytic construction is Hermitian, contractive, nested, and the
  independent GH sequence converges toward it.

EXACT_HERMITE_MIXED_COVARIANCE_BLOCKED
  otherwise.
```

```text
exact_mixed_covariance_derived = false
physical_regulator_completed_record_baseline_derived = false
sharp_cell_implementability_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
