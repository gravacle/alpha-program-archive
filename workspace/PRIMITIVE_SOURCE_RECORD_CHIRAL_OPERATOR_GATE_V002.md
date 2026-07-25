# Primitive Source-Record Chiral Operator Gate v002

Date: 2026-07-23

## Why v002 exists

Version 001 correctly computed a determinant but described a fixed-time
Hermitian kernel as though it were the covariant Dirac operator, called a
determinant zero a physical pole, and let a source-only block stand in for a
complete closure map. Version 002 corrects those statements.

Version 001 is rejected as authority.

## Scope

This gate computes only the free quadratic consequence of a supplied constant
scalar/pseudoscalar closure background, on flat Minkowski spacetime or as the
local tangent-space principal symbol, under
`PRIMITIVE_SOURCE_RECORD_PAIRED_RETURN_IDENTIFICATION_PRINCIPLE_V002.md`.

Natural units `hbar=c=1` are used within the displayed operator algebra.

## Covariant operator

For real supplied constants `a_R` and `b_R`, define

```text
D_SR(p)
  = slash(p) - a_R - i b_R gamma^5.
```

This is the covariant Dirac quadratic operator. The proper-Lorentz invariant
bilinear is

```text
a_R bar(psi) psi + b_R bar(psi) i gamma^5 psi.
```

In a chiral basis, the fixed-time Hermitian kernel

```text
K_H = gamma^0 D_SR = p_0 - H_SR
```

has the block form

```text
K_H(p,a_R,b_R) =
  [ p.bar_sigma          -(a_R+i b_R) I_2 ]
  [ -(a_R-i b_R) I_2       p.sigma       ].
```

Ordinary Hermiticity applies to `K_H` for real four-momentum. Covariance
applies to `D_SR`. These are related statements, not the same statement.

## Exact algebra

The Pauli identity gives

```text
(p.sigma)(p.bar_sigma) = p^2 I_2,
p^2 = p_0^2 - p_1^2 - p_2^2 - p_3^2.
```

The exact determinant is

```text
det K_H
  = [p^2 - (a_R^2+b_R^2)]^2.
```

The supplied constant background therefore defines the free quadratic
mass-shell locus

```text
p^2 = m_free^2,
m_free^2 = a_R^2+b_R^2.
```

This gate does not establish an `i epsilon` prescription, propagator residue,
self-energy, renormalized 1PI zero, or interacting pole mass.

## Fixed-frame chiral-odd block

The mass-like Hamiltonian block is

```text
C_H(a_R,b_R) =
  [       0             (a_R+i b_R) I_2 ]
  [ (a_R-i b_R) I_2           0         ].
```

It obeys

```text
{Gamma_ch,C_H}=0,
C_H^2=(a_R^2+b_R^2) I_4.
```

Its ordinary singular value in the declared time-slice Hilbert structure is
`sqrt(a_R^2+b_R^2)`. The invariant statement is the mass-shell equation
above, not the singular value by itself.

## Gauge basis

The physical fields have

```text
q(psi_L)=q(psi_R)=+1,
```

so `bar(psi_L) psi_R` is vector-`U(1)_rel` neutral. In the all-left-handed
anomaly basis the same inventory is

```text
q(psi_L)=+1,
q(psi_R^c)=-1.
```

## What the exact audit verifies

The dependency-free script
`scripts/audit_primitive_source_record_chiral_operator_v002.py` verifies:

```text
the displayed 4x4 determinant identity;
chirality oddness of C_H;
C_H^2=(a_R^2+b_R^2)I_4;
ordinary Hermiticity of the supplied K_H.
```

It does not verify representation-theoretic uniqueness, a complete
record-forming interaction, CPT, durability, or a physical pole.

## Hard next gate

Construct the complete parameter-free source-record closure action and derive,
without mass or alpha input:

1. the recorded source observable;
2. source-conditioned distinguishable record states;
3. stable pointer sectors and persistence;
4. an isolated closure background `(a_*,b_*)`;
5. causal and gauge-compatible cell stitching;
6. the full source two-point function and positive physical residue.

Only after those results may a spectral measure act on the complete
source-record operator.

## Status

```text
scalar_pseudoscalar_quadratic_form_declared = true
displayed_fixed_time_block_algebra_verified = true
free_mass_shell_relation_for_supplied_background_derived = true
complete_source_record_generator_derived = false
closure_background_derived = false
record_generated_free_mass_parameter_derived = false
interacting_pole_and_residue_derived = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
