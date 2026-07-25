# Source-Record Generator Structure Gate v001

Date: 2026-07-23

## Purpose

This gate asks what operator structure is fixed before choosing a closure
dynamics. It uses no mass, alpha, endpoint, response, or trial potential.

This is a candidate-analysis gate, not active authority until hostile review
and sealing.

## Minimal product carrier

For the primitive local write event only, use:

```text
H_SR = C^2_source-grading tensor C^2_record-endpoint.
```

Let

```text
Z_S = source left/right grading,
Z_R = record endpoint grading.
```

A local Hermitian generator component that both changes source chirality and
changes the primitive record endpoint must obey

```text
{G,Z_S tensor I}=0,
{G,I tensor Z_R}=0.
```

## Exact allowed space

Using the Pauli basis, the complete real Hermitian solution space is

```text
span_R {
  X_S tensor X_R,
  X_S tensor Y_R,
  Y_S tensor X_R,
  Y_S tensor Y_R
}.
```

It is four-dimensional. Therefore source oddness plus record change does not
select one generator.

## Conditional capacity-transfer reduction

If one adds the further condition

```text
[G,Z_S tensor I + I tensor Z_R]=0,
```

then the allowed space reduces to

```text
span_R {
  X_S tensor X_R + Y_S tensor Y_R,
  X_S tensor Y_R - Y_S tensor X_R
}.
```

The two terms are the real and imaginary parts of one complex exchange
amplitude. A record-basis phase rotation relates them, leaving one positive
magnitude after a phase convention.

The commutator condition says that the primitive event transfers one unit
between source grading and record endpoint without creating or destroying the
combined local grading. That physical condition is not yet an active
cleanroom theorem. The reduction is therefore conditional.

## Conditional write action

For the phase convention

```text
G_ex = (g/2)(X_S tensor X_R + Y_S tensor Y_R),
```

the one-excitation sector obeys

```text
|1_S,0_R>
  -> cos(g tau/hbar)|1_S,0_R>
     - i sin(g tau/hbar)|0_S,1_R>.
```

At

```text
g tau/hbar = pi/2
```

the endpoint is transferred exactly. This is a reversible primitive write or
premeasurement. It is not a durable record: persistence, amplification,
redundancy, and protection against reversal remain absent.

## Relation to the source mass block

`G_ex` is a joint source-record operator. It is not the supplied c-number
background used in the free chiral-block gate. A source-only mass parameter
would require one of:

```text
a dynamically derived record-field background;
an exact reduction of the joint source-record propagator;
or a derived self-energy after the record sector is integrated out.
```

No such reduction is performed here.

## What is learned

```text
source oddness plus endpoint change -> four real generator directions;
adding combined-grading conservation -> one complex exchange amplitude;
phase convention -> one positive magnitude;
exact transfer -> fixes only the product g tau/hbar = pi/2.
```

Neither `g` nor `tau` is separately fixed, and durability is not derived.

## Exact next gate

Determine whether closed boundary accounting independently requires the
combined-grading conservation law at the primitive source-record cell. If it
does, derive the physical interval and irreversible/redundant completion
without importing a measured mass or coupling.

## Status

```text
minimal_source_record_product_carrier_declared = true
source_odd_record_changing_hermitian_space_dimension = 4
combined_grading_conservation_derived = false
conditional_exchange_space_dimension = 2
exchange_phase_is_basis_convention_conditionally = true
exchange_magnitude_derived = false
physical_record_interval_derived = false
durable_record_dynamics_derived = false
source_mass_derived = false
spectral_evaluation_authorized = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
