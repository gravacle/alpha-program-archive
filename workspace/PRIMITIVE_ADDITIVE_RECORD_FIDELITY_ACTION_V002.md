# Primitive Additive Record-Fidelity Action v002

Date: 2026-07-23

## Status and provenance

This file freezes a parameter-free one-cell charged-record action candidate
before any small-holonomy expansion, cell assembly, determinant, flow, or
coupling is evaluated.

Version 002 removes the invalid dependency on the common-phase projective-lift
bundle. It uses:

```text
the pointwise active relative-phase stabilizer;
the Level-1 adopted principal U(1)_rel connection;
the primitive balanced two-endpoint comparator;
the primitive unit action character;
Born record probabilities.
```

The connection is adopted Level-1 field content. It is not claimed to have
been derived from projective lift redundancy.

## Balanced primitive comparison

For the primitive comparison with no declared preference between its two
endpoint alternatives, endpoint exchange symmetry gives

```text
|r_0> = (|0> + |1>) / sqrt(2).
```

A pointwise active relative-phase transport acts as

```text
U(theta) = diag(1, exp(i theta)).
```

The fidelity with the null-holonomy reference is

```text
F_R(theta)
  = |<r_0|U(theta)|r_0>|^2
  = cos^2(theta/2).
```

This is a kinematic comparator result. By itself it is not a field action.

## Adopted record-weight rule

The microscopic theory adopts the following Level-1 rule for one primitive
record cell:

```text
the Euclidean weight for preserving the declared reference relation equals
its Born fidelity,

exp(-S_R,E/hbar) = F_R.
```

This is a new action postulate. It is target-value-free and forward-sealed,
but it is not derived merely from Born statistics.

For independent record cells, fidelities multiply. Additive Euclidean action
therefore gives the continuous information cost

```text
I(F_1 F_2) = I(F_1) + I(F_2),
I(1) = 0,
I(F) = -log(F).
```

The frozen one-cell candidate is consequently

```text
S_R,E(theta)
  = -hbar log[cos^2(theta/2)].
```

No numerical expansion coefficient is evaluated in this file.

## Candidate ensemble action

Once a causal-cell ensemble and its orientation measure have been derived,
the candidate record action is

```text
S_R,E[a,g,R]
  = -hbar sum_(c in C)
      log F_R[Hol_boundary(c)(a)].
```

The holonomy uses the primitive unit character. The set `C`, its density,
orientation, incidence multiplicity, continuum limit, Lorentzian/CTP
continuation, and edge treatment are not chosen here.

## Physical meaning

The action is the additive reference-preservation cost under active relative
phase transport. Orthogonal transport has zero reference fidelity and
infinite preservation cost. That statement concerns preservation of the
declared relation; it is not the probability normalization of all possible
outcomes.

This candidate is not yet identified with the complete electromagnetic
action. That identification requires a derived public transverse continuum
limit and the exclusion of every independent finite curvature term.

## Compositeness condition

The separate bare Maxwell coefficient is absent under the adopted Level-1
condition

```text
K_bare[Q_spec, regulator, causal-cell scale] = 0.
```

The record-fidelity action itself may generate a curvature stiffness after
the continuum limit. No extra `c F^2` term or multiplicity may be added.

## Frozen choices

```text
active_phase_group = pointwise_U1_rel
charged_connection_status = adopted_Level_1_field_content
primitive_record_state = balanced_two_endpoint_state
one_cell_weight_postulate = Born_reference_fidelity
independent_cell_composition = product
one_cell_additive_cost = negative_log_fidelity
one_cell_information_multiplicity = 1
separate_bare_Maxwell_stiffness = 0
```

## Hard failure conditions

This route fails if:

```text
the one-cell weight must be rescaled after evaluation;
the cell density or orientation is selected by target comparison;
the continuum limit permits an arbitrary finite c F^2 deformation;
the Lorentzian/CTP completion violates gauge covariance or unitarity;
or the unused prediction fails.
```

## Evaluation remains blocked

```text
one_cell_action_candidate_frozen = true
causal_cell_ensemble_derived = false
Lorentzian_CTP_continuation_derived = false
cell_orientation_measure_derived = false
long_wavelength_Maxwell_limit_derived = false
complete_Q_spec_frozen = false
finite_c_F2_deformation_excluded = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```

