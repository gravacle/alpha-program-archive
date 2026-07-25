# Stage-8 T7 Gaussian Path-Sum Reduction Result v001

Date: 2026-07-24

## Verdict

```text
GAUSSIAN_PATH_SUM_REDUCTION_DERIVED
```

The sealed qutrit incidence operator has spectral values
`{-sqrt(2),0,+sqrt(2)}`. Its ready-to-pointer transition weights, computed
from the spectral projectors, are:

```text
w_-=-1/4,  w_0=1/2,  w_+=-1/4.
```

For each record-eigenvalue history `sigma`, the source parent remains a
number-preserving quadratic evolution and therefore supplies a legitimate
one-particle propagator `u_sigma` and its second quantization
`Gamma(u_sigma)`. The completed-record Kraus operator is exactly:

```text
K_(p...p <- r...r)
 =sum_sigma (product_j w_(sigma_j)) Gamma(u_sigma).
```

For the inherited pure quasifree state with occupied-orbital isometry `V`,
the scalar amplitude is consequently:

```text
a_N
 =sum_sigma (product_j w_(sigma_j))
    det(V^dagger u_sigma V).
```

This is a finite signed sum of valid determinants, not the excluded
single-determinant expression. The identity
`w_-+w_0+w_+=0` also reproduces the exact zero vacuum block while allowing
nonzero one- and many-particle completed transfer.

At 400 time steps, the one- and two-cell path sums agree with the direct
70-state finite-Fock calculation to:

```text
|delta a_p|  = 2.94e-14
|delta a_pp| = 2.74e-13
```

The one- and two-cell time-step convergence ratios are respectively
`3.99685` and `3.99923`. An independent algebra verifier reconstructed all
three spectral projectors and weights without importing construction code.

The reduction replaces direct half-filled source-Fock growth by `3^N`
one-particle determinant histories. It is therefore the correct finite
entry point for scaling and cluster analysis.

It does not prove that the signed history sum is nonzero at every finite
volume. Nor does it prove a volume-uniform zero-free neighborhood,
linked-cluster summability, or the thermodynamic Duhamel/Hessian identity.
Those are the next T7 obligations.

```text
gaussian_path_sum_reduction_derived = true
all_finite_connected_baselines_nonzero_proved = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
