# Stage-8 T7 Pure Hermite-Vacuum Strong-Convergence Result v001

Date: 2026-07-24

## Verdict

```text
PURE_HERMITE_VACUUM_STRONG_CONVERGENCE_DERIVED
```

The finite pure covariances

```text
C_n^(pure)=1_(-infinity,0)(Q_n h_0 Q_n)
```

are not nested. The embedded `n=2` and `n=4` projectors differ in operator
norm by `0.166124...`; that fact is retained.

Nevertheless, the truncated momentum matrices are Hermite Jacobi matrices,
so their joint spectral representation is tensor Gauss-Hermite quadrature.
At every nonzero quadrature node,

```text
C_n^(pure)(p_node)
 =[I-alpha.p_node/|p_node|]/2.
```

Direct diagonalization agrees with this functional-calculus construction to
`1.56e-15` for `n=2` and `3.68e-15` for `n=4`. Fixed low-mode blocks
converge to the exact mixed covariance. Since the only symbol discontinuity
is the measure-zero point `p=0`, convergence on the dense finite Hermite span
and the uniform contraction bound imply:

```text
C_n^(pure) -> P_- strongly.
```

## Scope

Strong convergence of one-particle covariances does not by itself imply
convergence of growing-dimensional quasifree determinants.

```text
pure_state_sequence_nested = false
pure_state_strong_convergence_derived = true
global_determinant_convergence_derived = false
kappa_record_computed = false
alpha_computed = false
proof_authorized = false
```

## Artifacts

```text
de961915388eedc70c7cf29889b6f5b542c55464781a97d77acd1e4aecfc866f  STAGE8_T7_PURE_HERMITE_VACUUM_STRONG_CONVERGENCE_SPEC_V001.md
fc15500e61c4a7d055633825516575334ece808ab830187fc0962711cbfa0783  scripts/audit_stage8_t7_pure_hermite_vacuum_strong_convergence_v001.py
73cc4f6d4f661d8f2d7f4d09c83b805e8215b60690bc40e00ba31a10be116ffe  stage8_execution/work/T07_pure_hermite_vacuum_strong_convergence.json
```
