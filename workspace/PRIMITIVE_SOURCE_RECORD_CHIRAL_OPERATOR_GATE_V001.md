# Primitive Source-Record Chiral Operator Gate v001

Date: 2026-07-23

## Purpose

This gate computes what follows from the adopted
`PRIMITIVE_SOURCE_RECORD_PAIRED_RETURN_IDENTIFICATION_PRINCIPLE_V001.md`
before any closure magnitude or electromagnetic response is evaluated.

## Frozen branch

Use the already frozen ordinary source branch:

```text
3+1 Lorentzian spacetime;
one vectorlike unit-charge Dirac source;
one left Weyl block and one right Weyl block;
no extra flavor index;
zero primitive bare mass;
transport-only U(1)_rel coupling.
```

Let

```text
sigma^mu     = (I_2,  sigma_1,  sigma_2,  sigma_3),
bar_sigma^mu = (I_2, -sigma_1, -sigma_2, -sigma_3),
phi_R        = a + i b.
```

For a constant closure background, the momentum-space source-record kernel is

```text
K_SR(p, phi_R) =
  [ p.bar_sigma      -phi_R I_2 ]
  [ -phi_R^* I_2      p.sigma   ].
```

The corresponding odd closure block is

```text
C_SR(phi_R) =
  [       0       phi_R I_2 ]
  [ phi_R^* I_2        0     ].
```

## Exact algebra

The Pauli identity gives

```text
(p.sigma)(p.bar_sigma) = p^2 I_2,
p^2 = p_0^2 - p_1^2 - p_2^2 - p_3^2.
```

Because the scalar return block commutes with the Weyl blocks,

```text
det K_SR(p, phi_R)
  = (p^2 - |phi_R|^2)^2.
```

The closure block obeys

```text
{Gamma_ch, C_SR} = 0,
C_SR^2 = |phi_R|^2 I_4,
singular_values(C_SR) = {|phi_R|, |phi_R|, |phi_R|, |phi_R|}.
```

Thus any nonzero constant closure saddle generates one doubly spin-degenerate
positive pole scale

```text
m_R c^2 = |phi_R|.
```

The equation identifies the pole with the closure singular value. It does not
calculate that singular value.

## Gauge and Lorentz checks

Both Weyl sectors have the same vector charge. Consequently

```text
psi_L -> exp(i lambda) psi_L,
psi_R -> exp(i lambda) psi_R
```

leaves the paired-return bilinear neutral. The two Weyl kinetic blocks and
their scalar contraction are Lorentz covariant. Including `phi_R` and its
complex conjugate in opposite blocks makes the kernel Hermitian for real
four-momentum.

## What this gate closes

```text
closure/source operator identity: adopted;
non-derivative Lorentz-scalar vector-neutral tensor class: fixed;
left-right domains and adjoint return: fixed;
pole equation for a supplied closure background: derived;
independent post-closure mass insertion: forbidden.
```

## What this gate does not close

```text
existence of a durable closure saddle;
absolute value of phi_R;
unique record duration or cell;
source pole residue in the full interacting theory;
complete state, contour, measure, regulator, or edge data;
absolute electromagnetic stiffness;
alpha.
```

## Hard next gate

Construct one parameter-free boundary closure action whose stable public
solution determines `phi_R` without a measured mass or coupling. The solution
must be checked for:

1. nonzero existence;
2. uniqueness modulo declared symmetries;
3. stability against all admissible cell fluctuations;
4. causal and gauge-compatible cell stitching;
5. an isolated positive source pole and positive residue.

Only after that gate may the frozen spectral measure act on the resulting
source-record operator.

## Status

```text
source_record_operator_block_form_derived = true
source_record_operator_gauge_neutral = true
source_record_operator_chirality_odd = true
source_pole_relation_derived_for_supplied_phi = true
closure_saddle_derived = false
phi_magnitude_derived = false
record_generated_source_mass_derived = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
