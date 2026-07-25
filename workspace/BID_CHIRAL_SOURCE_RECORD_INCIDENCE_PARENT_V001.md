# BID Chiral Source-Record Incidence Parent v001

Date: 2026-07-23

## Purpose

This derivation constructs the local joint source-record operator required by
the adopted source-record odd-component identification. It uses the BID unit
incidence law and no mass, alpha, endpoint, or response value.

## Spin-suppressed local carrier

The finite matrix audit uses the spin-suppressed rest-frame chirality factor

```text
H_chi=span_C{|L>,|R>}
```

This `C^2` is not the full physical source carrier and is not called a
particle/antiparticle space. The full local Dirac lift is derived in
`BID_LORENTZ_COVARIANT_SOURCE_BOUNDARY_MAP_DERIVATION_V001.md`: on an oriented
boundary it is the spin-degenerate rest-frame block of

```text
M_(n,delta)=slash(n) exp(i delta gamma^5).
```

Use the pure charged first-opening chain carrier. The finite vertex sector is

```text
C_0
  =(H_chi tensor |r>)
   direct-sum
   (H_chi tensor |p_Q>),
```

and the edge sector is

```text
C_1=H_chi tensor |e_Q>.
```

All source states carry the same primitive vector charge. Chiral transfer is
therefore vector-`U(1)` neutral.

## Complete chiral-odd incidence family

Let `Z_chi=diag(1,-1)`. The endpoint map `C:H_chi->H_chi` must be:

```text
unitary;
chiral odd, {C,Z_chi}=0;
vector-U(1) neutral;
and CPT-even as a scalar/pseudoscalar boundary bilinear.
```

The complete unitary chiral-odd family is

```text
C_(alpha,beta)
  =[[0,exp(i alpha)],
    [exp(i beta),0]].
```

The record category supplies one common endpoint-fiber rephasing. Write

```text
phi=(alpha+beta)/2,
delta=(alpha-beta)/2.
```

The common endpoint phase removes `phi` and leaves

```text
C_delta
  =[[0,exp(i delta)],
    [exp(-i delta),0]]
  =cos(delta) X_chi-sin(delta) Y_chi.
```

Removing `delta` would require a relative left/right, or axial, rephasing.
That is not an ordinary record-fiber gauge change. Its physical status depends
on the complete fermion measure, anomaly, topology, and CP branch.

Thus the family retains one unresolved axial phase. Every member has the same
unit singular values and is Hermitian after the common phase is removed.
`C=X_chi` is only the `delta=0` representative, not a proved unique choice.

## Complete incidence-weight exhaustion

Before selecting the incidence column, admit

```text
D_(a,b,C)=[-a I_2; b C_delta],
a,b in C, not both zero.
```

One-record normalization requires

```text
D_(a,b,C)^dagger D_(a,b,C)
  =(|a|^2+|b|^2)I_2
  =2 I_2.
```

Let

```text
s=sqrt(|a|^2+|b|^2).
```

At the first bright-mode half-turn `tau=pi/s`, evolution from a normalized
root source has endpoint probability

```text
P_endpoint,max
  =4 |a|^2 |b|^2/(|a|^2+|b|^2)^2
  <=1.
```

Equality holds exactly when `|a|=|b|`. Exact completed first-record transfer
therefore forces equal endpoint magnitudes. Combined with the norm equation,

```text
|a|=|b|=1.
```

The common edge phase fixes `a=1`; the phase of `b` joins the removable common
endpoint phase already separated above. The axial phase `delta` remains.
Thus the complete magnitude family reduces to the unit-incidence column
without comparing a response value.

## Joint incidence operator

The unit-incidence column is

```text
D_SR:H_chi tensor |e_Q> -> C_0,

D_SR |chi,e_Q>
  =-|chi,r>+|C_delta chi,p_Q>.
```

In chirality blocks, for every admitted `delta`,

```text
D_SR=[-I_2; C_delta],
D_SR^dagger D_SR=2 I_2.
```

The self-adjoint joint operator is

```text
B_SR=[[0,D_SR],[D_SR^dagger,0]].
```

Its spectrum is

```text
{-sqrt(2),-sqrt(2),0,0,+sqrt(2),+sqrt(2)}.
```

At the first-opening interval

```text
tau_R=pi/sqrt(2),
```

it gives the exact completed records

```text
|chi,r> -> |C_delta chi,p_Q>.
```

The same unit matrix element therefore performs the record transition and the
chiral-odd source transfer. No independent relative source/record
normalization exists in this finite dilation.

## What this closes

The earlier finite invariant-form audit showed that merely placing source and
record operators in one block leaves two invariant weights. In the restricted
pure off-diagonal model, `B_SR` supplies both effects as matrix elements of
one incidence column. Its scaled normalization and the absence of parent
zero-form detuning are model premises, not consequences of record
Hilbertization.

This is a local one-source/one-record-sector representation. The global
composition is one shared source CAR algebra with labeled record factors, as
typed in `BID_GLOBAL_CAR_RECORD_COMPOSITION_DERIVATION_V001.md`; the source
factor is not copied once per record cell.

An added source-only mass term, record-only transfer multiplier, or
`lambda |11><11|` overlap term is absent only inside the adopted
Single-Operator Completeness branch. The complete parent zero-form inventory
is classified separately and its coefficient selection remains open.

## What remains open

The finite spectrum is not yet a physical mass spectrum. That requires:

```text
the spatial Dirac kinetic operator and causal domain;
the complete CTP state and boundary conditions;
the physical source two-point function;
durability/environment completion;
connected-cell stitching;
and pole/residue extraction.
```

No eigenvalue in this file is named an electron mass or inserted into a
coupling calculation.

## Status

```text
spin_suppressed_local_chirality_carrier_typed = true
full_local_Dirac_lift_derived_in_companion = true
global_particle_antiparticle_CAR_parent_derived = false
complete_unitary_chiral_odd_endpoint_family_classified = true
common_endpoint_phase_removed = true
relative_axial_phase_removed_as_record_equivalence = false
relative_axial_phase_unresolved = true
complete_incidence_weight_family_admitted = true
perfect_transfer_bound_derived = true
conditional_pure_offdiagonal_perfect_transfer_forces_equal_endpoint_magnitudes = true
conditional_scaled_norm_and_perfect_transfer_force_a_b_magnitudes_one = true
restricted_joint_unit_incidence_column_constructed = true
joint_operator_self_adjoint = true
joint_operator_spectrum_computed = true
record_transition_and_chiral_transfer_share_one_matrix_element = true
independent_source_record_relative_weight_survives_within_restricted_model = false
parent_zero_form_detuning_derived_absent = false
complete_physical_source_record_parent_derived = false
completed_chiral_flipped_record_at_tau_R = true
physical_source_mass_computed = false
connected_many_record_parent_derived = false
complete_Q_spec_sealed = false
alpha_computed = false
proof_authorized = false
```
