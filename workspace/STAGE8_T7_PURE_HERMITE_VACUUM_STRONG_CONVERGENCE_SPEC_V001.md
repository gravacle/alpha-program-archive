# Stage-8 T7 Pure Hermite-Vacuum Strong-Convergence Spec v001

Date: 2026-07-24

## Purpose

Decide whether

```text
C_n^pure=1_(-infinity,0)(Q_n h_0 Q_n)
```

converges strongly to the continuum negative-frequency projector even though
the finite spectral projectors are not nested.

This is a state-provenance theorem. It uses no response or coupling target.

## Structural route

The one-dimensional truncated momentum matrix is the Jacobi matrix of the
Hermite system. Its eigenvalues are the order-`n` Gauss-Hermite nodes, and
its eigenvectors are the corresponding discrete-variable-representation
transform.

The three Cartesian momentum matrices commute. In their joint finite
spectral representation:

```text
Q_n h_0 Q_n = alpha.p_node
```

at every tensor-product node. For even `n`, no node is at `p=0`, and the
negative spectral block is exactly:

```text
P_-(p_node)=[I-alpha.p_node/|p_node|]/2.
```

Therefore every fixed low-mode block of `C_n^pure` is a tensor
Gauss-Hermite quadrature of the same matrix-valued symbol whose exact
compression defines `C_m^mix`.

## Obligations

1. prove the finite DVR identity;
2. verify it numerically against direct diagonalization for `n=2,4`;
3. show fixed-block convergence toward the analytic mixed covariance for
   low-mode blocks `m=2,4`;
4. state the strong-convergence proof:
   - Gauss-Hermite measures converge on bounded functions continuous almost
     everywhere for the Gaussian spectral measure;
   - the only discontinuity of `P_-` is `p=0`, which has zero continuum
     spectral measure;
   - convergence on the dense finite Hermite span plus
     `0<=C_n^pure<=I` extends to all vectors.

No claim of operator-norm convergence on the full growing carrier is
required or permitted.

## Verdict

```text
PURE_HERMITE_VACUUM_STRONG_CONVERGENCE_DERIVED
  iff the finite identity, fixed-block convergence, and dense-set extension
  all pass.

PURE_HERMITE_VACUUM_STRONG_CONVERGENCE_BLOCKED
  otherwise.
```

```text
pure_state_sequence_nested = false
pure_state_strong_convergence_derived = false
global_determinant_convergence_derived = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
