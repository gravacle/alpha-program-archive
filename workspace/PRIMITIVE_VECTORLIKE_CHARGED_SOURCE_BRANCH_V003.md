# Primitive Vectorlike Charged Source Branch v003

Date: 2026-07-23

## Why v003 exists

Version 003 preserves every frozen input of version 002 and makes the anomaly
basis explicit. Version 002 listed the left-handed anomaly charges
`(+1,-1)` and later described a vectorlike Dirac field without stating that
the second left-handed field is the charge conjugate of the physical
right-handed field.

This is a representation-basis clarification, not a change of source
inventory, charge, statistics, or action.

## Frozen branch inputs

```text
3+1 Lorentzian spacetime;
local Lorentz covariance and spin-statistics;
CPT compatibility;
one primitive charged spinor source psi;
the active U(1)_rel unit character;
the Level-1 adopted principal U(1)_rel bundle and auxiliary connection.
```

## Physical vector-charge basis

The physical chiral components of the Dirac source carry the same vector
charge:

```text
q(psi_L) = +1,
q(psi_R) = +1.
```

Consequently the local mass-like bilinear is gauge neutral:

```text
bar(psi_L) psi_R -> bar(psi_L) psi_R.
```

## Left-handed anomaly basis

Anomaly sums are conventionally written using left-handed fields only. The
right-handed field is therefore represented by its left-handed charge
conjugate:

```text
q(psi_L)   = +1,
q(psi_R^c) = -1.
```

The smallest vectorlike completion then obeys

```text
sum_i q_i   = (+1) + (-1) = 0,
sum_i q_i^3 = (+1)^3 + (-1)^3 = 0.
```

The `(+1,-1)` anomaly pair and the unit-vector-charge Dirac field are the same
physical inventory in different bases.

## Frozen source inventory

```text
source_bundle = adopted_principal_U1_rel_bundle
physical_source_charges = q(psi_L)=q(psi_R)=+1
left_handed_anomaly_charges = (+1,-1)
primitive_charge_magnitude = 1
primitive_fundamental_vectorlike_pairs = 1
primitive_source_representation = four_component_Dirac
primitive_source_statistics = fermionic
primitive_bare_mass = 0
```

Additional vectorlike pairs are consistent and are not proved impossible.
They may not be added after response evaluation. Composite durable
excitations are not counted as independent ultraviolet flavors unless the
sealed parent dynamics derives them.

## What remains open

```text
spinor_source_derived_from_pre_alpha_record_principles = false
complete_source_record_generator_derived = false
record_generated_mass_derived = false
fermion_measure_and_regulator_derived = false
universal_matter_spectrum_derived = false
complete_Q_spec_frozen = false
charged_determinant_evaluation_authorized = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```

## No-retuning rule

The representation, pair count, charge, statistics, and zero bare mass remain
frozen. If the branch fails, these choices may not be changed within version
003.
