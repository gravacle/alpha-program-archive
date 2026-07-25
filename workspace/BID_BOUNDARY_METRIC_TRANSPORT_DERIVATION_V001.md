# BID Boundary-Metric Transport Derivation v001

Date: 2026-07-23

## Question

When does spin/`U(1)` edge transport preserve the positive boundary
hypersurface metric used by the source-record incidence operator?

## Construction

For a future unit timelike normal `n`, define

```text
h_n(psi,phi)=bar(psi) slash(n) phi
            =psi^dagger gamma^0 slash(n) phi.
```

Let an oriented edge carry a proper-orthochronous Lorentz transport
`Lambda_e`, its spin lift `S_e`, and a unit `U(1)` phase. The endpoint normal
is not independent data; it is transported:

```text
n_p=Lambda_e n_r.
```

The spin representation obeys

```text
S_e^dagger gamma^0=gamma^0 S_e^-1,
S_e^-1 slash(n_p) S_e=slash(n_r).
```

Therefore

```text
h_(n_p)(S_e psi,S_e phi)
 =psi^dagger S_e^dagger gamma^0 slash(n_p) S_e phi
 =psi^dagger gamma^0 slash(n_r) phi
 =h_(n_r)(psi,phi).
```

The unit `U(1)` phase cancels between the two arguments. Hence the combined
edge transport is an isometry.

## Earned result and boundary

Boundary-metric compatibility follows from standard spin covariance once the
endpoint normal is required to be the Lorentz transport of the root normal.
It is not an independent numerical assumption.

This does not select an improper-Lorentz/CPT branch, an axial phase, a
connected action, a mass, or alpha.

## Status

```text
endpoint_normal_transport_law_typed = true
spin_pseudounitarity_used = true
Clifford_normal_covariance_used = true
U1_phase_cancels_in_hypersurface_metric = true
boundary_metric_edge_transport_isometry_derived = true
proper_orthochronous_scope_only = true
charged_boundary_CPT_intertwiner_derived = false
alpha_computed = false
proof_authorized = false
```
