# Durable-Pointer Closure-Operator Selector Gate v001

Date: 2026-07-23

## Purpose

This gate asks whether the primitive two-endpoint record algebra selects a
dimensionless durable closure-operator direction without a radial potential,
mass, alpha, or response target.

It is a candidate-analysis gate until hostile review and sealing.

## Inputs

From the primitive record carrier:

```text
record algebra = M_2(C);
durable endpoint projectors = P_0, P_1;
P_0+P_1=I;
P_i P_j=delta_ij P_i.
```

For the post-closure pointer component only, impose nondemolition
compatibility:

```text
[C_ptr,P_0]=[C_ptr,P_1]=0.
```

This condition says that the closure component used to stabilize/read the
record does not itself mix the two declared durable endpoint sectors. It does
not say that `C_ptr` writes, amplifies, or redundantly copies the record.

## Exact commutant

A Hermitian element of `M_2(C)` has Pauli expansion

```text
C = c_0 I + c_x X + c_y Y + c_z Z.
```

The two commutators force

```text
c_x=c_y=0,
```

so the real Hermitian commutant is

```text
span_R{I,Z}.
```

The common identity part changes neither endpoint contrast nor any relative
record. It is response-null in the declared comparison context. Quotienting
that common mode leaves the one-dimensional public closure direction

```text
C_0 = P_1-P_0 = +/- Z,
```

where the sign is endpoint relabeling.

The dimensionless endpoint contrast is canonically normalized:

```text
C_0^2=I,
spec(C_0)={-1,+1}.
```

This normalization belongs to the record observable. It does not fix the
dimensionful coefficient multiplying it in a Hamiltonian or action.

## Source-record implication

Under the sealed source-record odd-component identification, a parity-even
endpoint-population closure component can enter the source bilinear as

```text
S_odd,ptr
  = -integral d^4x sqrt(-g)
      kappa_R C_0 bar(psi) psi.
```

In a declared pointer sector this supplies a free quadratic parameter
`+/- kappa_R`. The sign is sector labeling; the magnitude `|kappa_R|` remains
open.

The orientation/coherence generators `X` and `Y` do not commute with the
pointer projectors. Therefore they cannot be the post-closure nondemolition
pointer component. This does not prohibit them in the pre-closure write
dynamics, and it does not prove that every possible pseudoscalar boundary
field is absent from the complete theory.

## What this gate does not derive

```text
the write interaction;
pointer-state production;
environmental amplification or redundancy;
the dimensionful coefficient kappa_R;
the physical causal-cell interval;
an interacting source pole;
the spectral measure or EM response;
alpha.
```

An energy splitting proportional to `C_0` makes the endpoint sectors
stationary under that component. Stationarity alone is not durability.

## Exact next gate

Derive the dimensionful coefficient `kappa_R` and the full record-writing and
stabilizing action from one parameter-free causal cell. The derivation must
also prove that no additional pointer-preserving term changes the source or
EM response.

## Status

```text
primitive_record_algebra_input_derived = true
durable_endpoint_projectors_input_declared = true
nondemolition_pointer_condition_adopted_for_selector = true
hermitian_pointer_commutant_dimension = 2
response_null_identity_quotient_dimension = 1
dimensionless_pointer_contrast_direction_selected = true
dimensionless_pointer_contrast_spectrum_fixed = true
complete_closure_operator_selected = false
record_write_dynamics_derived = false
physical_durability_derived = false
kappa_R_derived = false
record_generated_source_mass_derived = false
spectral_evaluation_authorized = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
