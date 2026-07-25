# Stage-8 T7 Exact Hermite Mixed-Covariance Result v001

Date: 2026-07-24

## Verdict

```text
EXACT_HERMITE_MIXED_COVARIANCE_DERIVED
```

For the nested three-dimensional Hermite carrier, every matrix element of

```text
C_n^(mix)=Q_n P_- Q_n,
P_-(p)=[I-alpha.p/|p|]/2,
```

was reduced to finite Hermite-polynomial sums and the exact radial-angular
moment

```text
I_(a,b,c)
 = Gamma(S+1)
   Gamma(a+1/2) Gamma(b+1/2) Gamma(c+1/2)
   / Gamma(S+3/2),

S=a+b+c.
```

The resulting `n=2` and `n=4` matrices are Hermitian contractions and nest
exactly:

```text
Q_2 C_4^(mix) Q_2 = C_2^(mix).
```

The independent verifier used the separate factorial identity

```text
I_(a,b,c)/pi
 =4 S!(S+1)! product_j (2a_j)!
  /[(2S+2)! product_j a_j!]
```

and reproduced both matrix artifacts to approximately `1e-14`. Tensor
Gauss-Hermite quadrature converges toward the analytic matrices but is not
used as authority.

## Scope

This derives the inherited mixed-state restriction on the genuine nested
Galerkin family. It does not prove convergence of a global determinant or
select an envelope realization.

```text
exact_mixed_covariance_derived = true
global_determinant_convergence_derived = false
kappa_record_computed = false
alpha_computed = false
proof_authorized = false
```

## Artifacts

```text
0ade34aa99b150756960d6dfbbc2c59749f7d638ce3bf59096148fde4514e55c  STAGE8_T7_EXACT_HERMITE_MIXED_COVARIANCE_SPEC_V001.md
e0f399de59642da2e6609951010d69b312d694c8c540c6d97ab93580360e38db  scripts/derive_stage8_t7_exact_hermite_mixed_covariance_v001.py
be73577dc66ab712457ec1f6ac3bebdc30cbd983a3cb7113092aacbf057c3973  stage8_execution/work/T07_exact_hermite_mixed_covariance.json
395141f2d3146d638b5c395b14a06eaa347701aec4f3cd6715befc6f8cda2464  stage8_execution/work/T07_exact_hermite_mixed_covariance.npz
bf1cfea6eb7dac66e4f6509f1cd5796d68c1f9aa3eaf13126d206b80326b4852  scripts/verify_stage8_t7_exact_hermite_mixed_covariance_v001.py
7484f436ee2b1b241b6ab6bf75b6b76645b5b456f729ccaeea124baceb6be5ca  stage8_execution/work/T07_exact_hermite_mixed_covariance_verification.json
```
