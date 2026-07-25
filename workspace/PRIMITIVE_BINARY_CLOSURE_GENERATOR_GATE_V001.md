# Primitive Binary Closure Generator Gate v001

## Scope

This gate derives the intrinsic generator of the primitive two-endpoint
record comparator after granting the Level-1 unique record interval. It does
not evaluate a gauge response or alpha.

## Inputs

The active branch supplies:

```text
one primitive carrier H_R = C^2;
orthogonal endpoint projectors P_0 and P_1;
P_0 + P_1 = I;
one unique positive first-record interval tau_R;
unitary primitive pre-record evolution;
zero reference energy assigned to the closed endpoint;
no additional carried direction.
```

For the calibrated comparison that tests whether the two endpoint actions
have separated, the comparator is population-unbiased:

```text
|+> = (|0> + |1>)/sqrt(2).
```

This is a calibration state, not a claim that every physical source has equal
Born weights.

## Generator form

Stability of the two endpoint alternatives requires the intrinsic generator
to commute with both endpoint projectors. After removing the common
gauge-independent energy,

```text
H_R = Delta_R P_1,
Delta_R > 0.
```

There is no second independent Hermitian direction compatible with the
declared stable endpoint decomposition.

The return amplitude of the calibrated comparison is

```text
zeta_R(tau)
  = <+| exp(-i H_R tau/hbar) |+>
  = [1 + exp(-i Delta_R tau/hbar)]/2.
```

The first positive orthogonality condition is

```text
zeta_R(tau_R) = 0,
Delta_R tau_R/hbar = pi.
```

Therefore

```text
H_R = (pi hbar/tau_R) P_1.
```

Higher odd windings solve the same orthogonality equation but are excluded by
the declared *first* positive record interval and primitive faithful winding.

## What is fixed

The result removes the free Hamiltonian frequency in the reversible primitive
comparator:

```text
omega_R = pi/tau_R.
```

The fundamental evolution remains unitary. A dephasing or Lindblad rate is
not a primitive coefficient; decoherence and durable amplification must be
computed from downstream degrees under the transport-only principle.

## What is not fixed

This gate does not establish:

- that the Dirac source pole has energy `Delta_R`;
- the spacetime support, orientation measure, or cell density;
- the physical value of `tau_R`;
- the complete source-record interaction;
- the induced Maxwell stiffness; or
- the Thomson matching map.

Identifying a source mass with `Delta_R/c^2` requires a separate
source-record pole theorem.

## Status

```text
primitive_binary_generator_form_derived = true
balanced_state_used_as_calibration_only = true
first_record_gap_times_interval = pi_hbar
primitive_record_frequency_derived = true
source_mass_identified_with_record_gap = false
causal_cell_measure_derived = false
finite_response_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
