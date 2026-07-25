# One-Cell Fidelity Action Selector Gate v001

Date: 2026-07-23

## Question

Does the sealed candidate

```text
S_cell(theta) = -hbar log[cos^2(theta/2)]
```

uniquely select the public Maxwell stiffness?

## Algebraic result

Given the explicitly adopted equality

```text
exp(-S_cell/hbar) = F_R(theta),
F_R(theta) = cos^2(theta/2),
```

the real principal-log action follows. This is an inversion of the adopted
weight rule, not a consequence of the Born rule alone.

The candidate remains target-value-free. Its pointwise comparator algebra is
valid.

## Why it does not yet select stiffness

### Overall information scale

Continuity and independent composition imply

```text
I(F) = -kappa log(F),
```

but do not fix `kappa`. Setting `kappa=1` is exactly the adopted weight
postulate.

### Preparation

For a general primitive preparation

```text
|r_p> = sqrt(p)|0> + sqrt(1-p)|1>,
```

the fidelity is

```text
F_p(theta)
  = 1 - 4 p(1-p) sin^2(theta/2).
```

The quadratic response therefore depends on `p`. The balanced state is a
frozen candidate preparation, not yet the output of a state-selection
theorem.

### Measure-action ambiguity

Before the complete measure is fixed,

```text
dmu' = J dmu,
S' = S + hbar log(J)
```

leaves the full Euclidean weight unchanged. A one-cell action cannot be
declared absolutely normalized in isolation from the measure.

### Multiplicity and correlations

The primitive one-handle carrier does not prove that a complete causal cell
contains exactly one independent fidelity factor. Replacing `F` by `F^N`, or
introducing cross-cell kernels, changes the continuum coefficient while
preserving the pointwise comparator law.

### Continuum tensor

For cell density `rho`, oriented area bivectors `B_p`, and independent
multiplicities `m_p`, the quadratic continuum response has the form

```text
M^(mu nu rho sigma)
  = integral dmu rho
      sum_p m_p B_p^(mu nu) B_p^(rho sigma).
```

A scalar Maxwell coefficient exists only when this tensor is proportional to
the identity on two-forms. Cell scale cancels from the leading four-dimensional
`F^2` term for a self-similar ensemble, but shape, filling, incidence,
multiplicity, and orientation normalization do not.

### Lorentzian/CTP meaning

The fidelity is a probability-level reference-preservation quantity. It does
not by itself distinguish:

```text
a single-branch amplitude action;
a doubled CTP probability/influence action;
a dissipative/noise kernel;
or the real unitary Maxwell kinetic action.
```

A positive Euclidean bivector ensemble also does not directly determine the
indefinite Lorentzian two-form metric. The contour, branch, state, and CTP
completion must be derived from one parent transition kernel.

### Finite deformation

Nothing in the one-cell formula excludes an independent finite `c F^2`
deformation after regularization and coarse graining.

## Decision

```text
pointwise_fidelity_formula = PASS
conditional_principal_log_action = PASS
standalone_absolute_stiffness_selector = BLOCK
complete_Q_spec_from_fidelity_action = BLOCK
Lorentzian_public_Maxwell_action_derived = false
finite_c_F2_deformation_excluded = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```

The candidate is retained as a possible diagonal probability observable of a
later complete CTP theory. It is retired as a standalone microscopic action
or absolute-stiffness selector.

## Reopen condition

The route may be reopened only if one complete parent transition kernel,
fixed before response evaluation, jointly derives:

```text
the physical state;
the path-integral/CTP measure;
the number and statistics of record/source degrees;
cell composition and correlations;
the causal-cell ensemble and orientation tensor;
the real and imaginary response kernels;
and the finite matching prescription.
```

The next active task is therefore the parent kernel, not a cell coefficient
extracted from `-log fidelity`.

