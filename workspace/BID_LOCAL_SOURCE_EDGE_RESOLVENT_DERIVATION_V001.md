# BID Local Source-Edge Resolvent Derivation v001

Date: 2026-07-23

## Purpose

This derives the source-channel poles of the finite chiral source-record
incidence parent. It keeps source support and public record zero modes
separate and uses no measured mass or coupling.

## Source and record sectors

For

```text
B_SR=[[0,D_SR],[D_SR^dagger,0]],
D_SR^dagger D_SR=2 I_2,
```

the vertex block `C_0` carries root/endpoint record alternatives and the edge
block `C_1` carries the source incidence support. The source two-point object
at this finite-cell level is the edge compression of the resolvent:

```text
G_source(z)
  =P_1 (z I-B_SR)^(-1) P_1.
```

## Exact Schur result

Block inversion gives

```text
G_source(z)
  =z (z^2 I_2-D_SR^dagger D_SR)^(-1)
  =[z/(z^2-2)] I_2.
```

Therefore:

```text
source poles: z=+sqrt(2), -sqrt(2);
residue at each pole: (1/2) I_2;
no source pole at z=0.
```

The two zero modes of `B_SR` lie in `ker(D_SR^dagger)` inside the vertex
record sector and have zero source-edge residue. They must not be counted as
massless charged source species.

## Record-interval relation

The physical cell generator is

```text
H_SR=(hbar tau_R/T_R) B_SR,
tau_R=pi/sqrt(2).
```

The magnitude of the local source-channel pole is consequently

```text
E_SR
  =sqrt(2) hbar tau_R/T_R
  =pi hbar/T_R,

E_SR T_R/hbar=pi.
```

This is the local source-record pole relation forced by the same operator that
completes the record transition.

## Scope boundary

`E_SR` is not yet identified with an observed particle pole mass. That
identification requires:

```text
the Lorentz-covariant spacetime Dirac extension;
the CTP prescription and physical source two-point function;
the complete public quotient and edge modes;
regulator-independent continuation;
and a pole with positive physical residue after interactions.
```

If the spacetime completion introduces an independent mass, shifts the pole by
an uncomputed finite subtraction, or restores a source zero pole, this route
does not derive a physical mass.

## Status

```text
finite_cell_source_resolvent_derived = true
source_resolvent_equals_z_over_z2_minus_2 = true
source_poles_paired_at_plus_minus_sqrt2 = true
source_zero_pole_absent = true
record_zero_modes_have_zero_source_residue = true
local_source_record_phase_equals_pi = true
Lorentz_covariant_source_pole_derived = false
physical_source_mass_computed = false
complete_Q_spec_sealed = false
alpha_computed = false
proof_authorized = false
```
