# Source-Flux-Conditioned Record-Write Gate v001

Date: 2026-07-23

## Purpose

This gate derives the record-changing part of the primitive charged
source-record operator from:

```text
the unit-character charged source branch;
the primitive two-endpoint record carrier;
the relative record-onset action rule;
the operational statement that the charged record channel is inactive when
no charged boundary flux crosses the cell.
```

It uses no mass, coupling, endpoint radius, or earlier alpha coefficient.

## Boundary source handle

On the declared zero-or-one primitive source sector, the conserved
unit-character flux through the causal-cell boundary is

```text
Q_Sigma = integral_Sigma j^mu dSigma_mu,
spec(Q_Sigma)={0,1}.
```

The charged record channel compares:

```text
Q_Sigma=0: no charged boundary access;
Q_Sigma=1: one primitive charged access.
```

The zero-flux/no-charged-write rule is an operational branch rule for this
charged handle. It does not say that gravity or unrelated record channels
cease evolving when `Q_Sigma=0`.

## Constant first-onset generator

Write the active record-factor Hamiltonian as

```text
h = a I + v_x X + v_y Y + v_z Z.
```

For a constant generator, the amplitude to remain in `|0_R>` after proper
interval `tau_*` is

```text
exp(-i a tau_*/hbar)
[
  cos(theta)
  - i (v_z/|v|) sin(theta)
],

theta = |v| tau_*/hbar.
```

At the first orthogonalization onset:

```text
theta=pi/2,
v_z=0,
v_x^2+v_y^2=E_rel^2,
E_rel tau_*/hbar=pi/2.
```

The equatorial angle of `(v_x,v_y)` is changed by endpoint rephasing. Choose
the representative `Y_R`. The record-changing part of the integrated
source-record action is therefore

```text
K_write = (pi/2) Q_Sigma tensor Y_R
```

up to endpoint rephasing and orientation reversal. Its unitary is

```text
U_write
  = (I-Q_Sigma) tensor I_R
    + Q_Sigma tensor (-iY_R).
```

It leaves the zero-flux branch unchanged in the charged record channel and
maps `|1_S,0_R>` to `|1_S,1_R>` up to phase.

## Exact unresolved source phase

The orthogonalization condition does not fix `a`. The integrated mutation

```text
delta K = chi Q_Sigma tensor I_R
```

changes no conditional record density matrix, while it changes the relative
source-branch phase. Thus the record-changing operator is unique only modulo:

```text
endpoint rephasing;
orientation reversal;
a source-conditioned identity phase.
```

The identity phase cannot be discarded as a global phase because it acts
only on the charged source branch. It can contribute to source propagation
and must remain until the complete boundary action fixes or excludes it.

## Relation to the pointer and source-odd blocks

The write direction `Y_R` is off-diagonal and does not preserve the endpoint
projectors. The post-closure pointer contrast `P_1-P_0` is diagonal. The
source-record odd-component principle permits a scalar/pseudoscalar source
block, but this gate does not derive its coefficient from the write angle.

Therefore:

```text
the charged source-to-record write operator is fixed modulo the listed
equivalences;
the complete closure operator and source mass are not fixed.
```

## Exact next gate

Derive the source-conditioned identity phase and the post-closure
scalar/pseudoscalar block from the same parameter-free boundary action, or
prove that the complete physical response is independent of them. A rule
chosen after response evaluation is forbidden.

## Status

```text
unit_source_flux_spectrum_inherited = true
zero_flux_no_charged_write_adopted = true
first_onset_equatorial_write_direction_derived = true
integrated_record_changing_coefficient_fixed = true
source_flux_conditioned_write_operator_derived = true
endpoint_rephasing_equivalence_retained = true
source_conditioned_identity_phase_fixed = false
complete_source_record_operator_derived = false
post_closure_pointer_coefficient_derived = false
source_odd_scalar_pseudoscalar_coefficient_derived = false
physical_durability_derived = false
record_generated_source_mass_derived = false
spectral_evaluation_authorized = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
