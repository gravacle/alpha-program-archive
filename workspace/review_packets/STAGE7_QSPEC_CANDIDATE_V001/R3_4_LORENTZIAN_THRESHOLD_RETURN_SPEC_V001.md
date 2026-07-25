# R3.4 Lorentzian Threshold-Return Specification v001

Date: 2026-07-24

## Purpose

Determine whether the already derived translation-invariant Lorentzian
source-record Hamiltonian has thresholded local nonreturn for every
normalizable continuum root. This is an operator theorem. It does not assume
that this Hamiltonian, a particular root, or a positive-frequency state is
already the complete physical outgoing sector.

No measured mass, coupling, endpoint, cosmological quantity, or alpha is
used.

## Hash-pinned authorities

```text
BID_LORENTZIAN_SOURCE_SCHUR_POLE_DERIVATION_V001.md
  dc0498615a94218c56ed91a3e679a2aa55e32d4fcb96220a50a7a88669a8fc34

R3_4_LORENTZIAN_JOINT_ENDPOINT_COMPATIBILITY_RESULT_V001.md
  1868656d1881e67c8f6263062b27806f71bcc9de03d7eec0e612085fb47de0cf

R3_4_CAUSAL_SHARED_SOURCE_MOLLER_DURABILITY_RESULT_V001.md
  1d114e71c29c3a39b7afd1b7a80b47afb52fe77e8ee1e4e19b604defe3c69305

PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md
  532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb

CAUSAL_DIRECT_LIMIT_RECORD_HYPOTHESIS_V001.md
  60c82b021a7f5ffcb514ae8c20f083a7b2c9b42872586922b1c0464c4822d73f
```

## Frozen Hamiltonian

Use

```text
H(p)=alpha_D dot p + mu S tensor c_partial,
S=-i gamma^0 gamma^5,
```

where `alpha_D` denotes the Dirac matrices, not the fine-structure
constant. The record operator has eigenvalues

```text
lambda in {0,-sqrt(2),+sqrt(2)}.
```

Hence

```text
H_lambda(p)^2=|p|^2+mu^2 lambda^2.
```

No branch or operator may be selected by the decay result.

## Required theorem

For `Psi` in

```text
L2(R^3;C^4 tensor C^3),
```

let `Q_lambda` be the record eigenspace projector and

```text
Pi_(lambda,sigma)(p)
 =Q_lambda tensor
  [I+sigma H_lambda(p)/E_lambda(p)]/2,
sigma in {-1,+1}.
```

The coarea formula must give an `L1` spectral density on every non-flat band:

```text
rho_(lambda,sigma)(E)
 =E p_lambda(E)
  integral_(S^2)
    Psi(p_lambda(E)Omega)^*
    Pi_(lambda,sigma)
    Psi(p_lambda(E)Omega) dOmega,

p_lambda(E)=sqrt(E^2-mu^2 lambda^2).
```

The complete return amplitude is the Fourier transform of the sum of these
densities. The gate must prove:

```text
A_Psi(t)->0
```

and therefore:

```text
for every delta>0 there exists finite T_delta such that
sup_(t>=T_delta)|A_Psi(t)|^2<delta.
```

The theorem fails if the Hamiltonian contains a flat band with nonzero root
weight or if the proposed root contains a point-spectrum atom.

## Numerical regression

Use a normalized isotropic Gaussian radial profile only as a regression
example, never as the physical root. Compare:

1. radial integration of the zero and massive cosine phases; and
2. direct matrix evolution averaged over an inversion-symmetric angular
   quadrature.

Report several late-time values without using monotonic decay as a proof.

## Mandatory scope

The operator theorem does not establish:

```text
that this H is the complete physical outgoing generator;
that the parent selects a particular L2 root;
that the selected root is in the limiting quadratic-form domain;
that the positive-frequency state is derived;
that generated descendants preserve absolute continuity;
that the complete write defect has no bound state;
or that the public pointer and spectral representation are joined in one
complete parent-selected GNS construction.
```

## Verdicts

```text
LORENTZIAN_L2_THRESHOLD_RETURN_THEOREM_DERIVED
LORENTZIAN_THRESHOLD_RETURN_BLOCKED
```

## Fixed statuses

```text
complete_outgoing_generator_identified = false
parent_selected_physical_root_derived = false
finite_energy_physical_root_derived = false
positive_frequency_state_derived_from_parent = false
generated_descendant_spectrum_exhausted = false
complete_write_defect_bound_states_excluded = false
complete_physical_durability_derived = false
complete_parameter_free_Q_spec_frozen = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
