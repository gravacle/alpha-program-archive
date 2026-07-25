# Primitive Additive Record-Fidelity Action v001

Date: 2026-07-23

## Status and scope

This file freezes a parameter-free charged-record action candidate before its
small-curvature expansion, cell assembly, determinant, flow, or coupling is
evaluated.

It uses:

```text
the sealed Fundamental Boundary Record Action Principle v001;
the local projective record bundle;
the primitive balanced two-alternative comparator;
the primitive additive-action character;
Born record probabilities.
```

It contains no electromagnetic target value or endpoint normalization.

## Balanced primitive comparison

In a primitive cell with no declared preference between its two endpoint
alternatives, endpoint exchange symmetry fixes the balanced comparison
representative

```text
|r_0> = (|0> + |1>) / sqrt(2).
```

A relative comparison holonomy `theta` acts by

```text
U(theta) = diag(1, exp(i theta)).
```

The fidelity of the transported comparator with the null-holonomy reference
is

```text
F_R(theta)
  = |<r_0|U(theta)|r_0>|^2
  = cos^2(theta/2).
```

This is the same primitive overlap law already fixed by the action character;
it is not fitted here.

## Why the action is logarithmic

For independent record cells, fidelities multiply:

```text
F_total = product_c F_c.
```

The Euclidean effective action of independent cells must add:

```text
S_total = sum_c S_c.
```

Let one cell's dimensionless record cost depend continuously only on its
fidelity, vanish at `F=1`, and obey

```text
I(F_1 F_2) = I(F_1) + I(F_2).
```

The continuous solutions are

```text
I(F) = -kappa log(F).
```

One primitive cell is one Bernoulli record trial. Requiring its Euclidean
weight to equal its Born fidelity,

```text
exp(-S_R,E/hbar) = F_R,
```

fixes `kappa=1`. Therefore the sealed one-cell action is

```text
S_R,E(theta)
  = -hbar log[cos^2(theta/2)].
```

For a cell ensemble `C`,

```text
S_R,E[a,g,R]
  = -hbar sum_(c in C)
      log F_R[Hol_c(a,g,R)].
```

The holonomy and cell ensemble must be derived by the later causal-cell and
measure gates. They are not chosen in this file.

## Physical interpretation

This action is the additive large-deviation cost of preserving the reference
record relation under charged comparison transport. Orthogonal transport has
zero reference fidelity and infinite reference-preservation cost; it is a
fully distinguishable closure outcome, not a negative probability.

The action weights record distinguishability. It is not yet asserted to be
the complete Lorentzian electromagnetic action. That identification requires
the derived causal-cell ensemble, analytic continuation/CTP rule, and a
public long-wavelength Maxwell limit.

## Zero-bare clause

The microscopic connection carries no separate curvature action:

```text
K_bare = 0.
```

All charged stiffness must come from the sealed record-fidelity action and
the rest of the same complete `Q_spec`. No later `c F^2` term or multiplicity
may be added.

## Frozen choices

```text
primitive_record_state = balanced_two_alternative_state
one_cell_probability_weight = Born_fidelity
independent_cell_composition = product
one_cell_additive_cost = negative_log_fidelity
one_cell_information_multiplicity = 1
bare_Maxwell_stiffness = 0
```

## Evaluation remains blocked

```text
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

No expansion coefficient or response number may be evaluated until this file
is sealed and the pending cell/measure gates are resolved.
