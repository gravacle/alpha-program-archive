# Stage-8 T7 Finite-Fock Completed-Record Amplitude Spec v001

Date: 2026-07-24

## Status

```text
SPECIFICATION_SEALED_BEFORE_EXECUTION
```

This gate constructs the first scalar completed-record amplitude from the
actual operator-valued CAR parent and the inherited finite quasifree state.
It evaluates no electromagnetic coupling or target.

## Hash-pinned authorities

```text
3a6ff6173573a7d9dd99bdd1a6bb7eaa02c433ab50bc769e144d94c983b4f0ff  STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_RESULT_V001.md
5f4336bfb636d25ab7e27d015b46502314bcbb4635ce685607eedc777f7537ca  stage8_execution/t7_parent_state_regulator_restriction/T07_PARENT_STATE_REGULATOR_RESTRICTION_V001.seal.sha256
5026afb89b52ead9f309168cb2fa4f06b81039f8dd01b8940f40e64aad679a7e  STAGE7_QSPEC_REVIEW_CANDIDATE_V002.md
40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9  R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md
949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd  BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md
6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb  BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md
e12fffcc0f94d6896bc5607898db6b3a1ea343aeaf557b1f6f70e58db061fab6  STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md
7aafba8667ac01f1c4326b0d714e838bf068eec7c8f4ce28ef03c8bef9d62098  STAGE8_T7_ACTUAL_PARENT_RECORD_AMPLITUDE_ADJUDICATION_RESULT_V001.md
```

## F1 - Same-parent finite spectral sector

In the exact three-site Galerkin parent, use the nonzero spectral subspace
of the free source Hamiltonian. This is a finite regression of the already
derived continuum restriction rule, not a new physical cutoff. It has eight
one-particle modes and the inherited negative-energy covariance has rank
four.

Compress the same source kinetic term and both same-parent cell incidence
operators to this subspace. No projector-chain transition replaces the
time-dependent parent.

## F2 - Exact number sector

Construct the four-particle sector:

```text
wedge^4 C^8
```

and the number-preserving lift

```text
dGamma(B)=sum_(ij) B_ij a_i^dagger a_j
```

for the free source and each record-coupled cell operator. Verify the
one-particle and many-particle action conventions independently.

The incoming source vector is the Slater state occupying all four
negative-energy modes. The two record qutrits begin in `|r,r>`.

## F3 - Actual causal evolution

Evolve:

```text
H(t)
 =dGamma(h_0) tensor I_R
  +sum_c v_c(t) dGamma(B_c) tensor iota_c(c_c)
```

with the sealed intrinsic diamond envelope, `tau_R=pi/sqrt(2)`, and causal
cell order. Use no post-write Hamiltonian.

## F4 - Scalar record amplitudes

After each completed cell, project only the record factors and evaluate the
source with the same incoming Slater bra:

```text
a_p(0)
 =<Omega_- tensor p,r | U_1 | Omega_- tensor r,r>;

a_pp(0)
 =<Omega_- tensor p,p | U_2 U_1 | Omega_- tensor r,r>.
```

Report both complex amplitudes and require them to be nonzero before any
normalization.

The zero-particle neutral sector must also be executed. Its completed
charged-record amplitude is expected to follow from the parent rather than
being conditioned away.

## F5 - Gaussian-shortcut negative control

For a completed record label orthogonal to the ready label, the vacuum block
of its Kraus operator is zero. If a one-particle completed transfer is
nonzero, that Kraus operator cannot equal one `Gamma(k)`, whose vacuum block
is one. Record this type obstruction and do not use:

```text
det(I-C+C K_h).
```

## F6 - Verification and scope

Use two independently coded time integrators and require agreement of the
complex amplitudes within the frozen numerical tolerance. Preserve state
norm and report time-step convergence.

```text
FINITE_FOCK_COMPLETED_RECORD_BASELINE_DERIVED
```

requires F1-F6 and nonzero `a_p(0)` and `a_pp(0)`.

```text
FINITE_FOCK_COMPLETED_RECORD_BASELINE_BLOCKED
```

is mandatory if either baseline vanishes, the two integrators disagree, or
the result requires a determinant or final source state chosen after
evolution.

Passing this gate derives only finite baselines in one inherited regulator.
It does not prove response factorization, regulator independence, a
volume-uniform zero-free neighborhood, linked-cluster density, or a
thermodynamic Duhamel identity.

## Fixed status

```text
finite_fock_completed_record_baseline_derived = false
finite_actual_parent_record_amplitude_derived = false
connected_primitive_amplitude_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
