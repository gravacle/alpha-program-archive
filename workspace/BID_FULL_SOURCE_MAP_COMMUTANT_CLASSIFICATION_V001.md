# BID Superseded Restricted Source-Map Commutant Attempt v001

Date: 2026-07-23

**Superseded:** hostile review showed that this file used the full Lorentz
commutant where the normal-dependent little-group commutant was required and
treated an axial source redefinition as an unproved physical equivalence.
The authoritative replacements are
`BID_ROOT_INCIDENCE_IDENTITY_DERIVATION_V001.md` and
`BID_COMPLETE_NORMAL_DEPENDENT_ENDPOINT_MAP_CLASSIFICATION_V001.md`.

## Question

What is the complete local proper-Lorentz-covariant source-map family before
the one-arrow source-record incidence weights are evaluated?

No alpha, mass, endpoint, or response number is used.

## Complete proper-Lorentz commutant

On the disclosed `3+1` Dirac carrier, the complex commutant of the connected
proper Lorentz spin representation is

```text
Comm(Spin^+(1,3)) = span_C{I,gamma^5}
                  = C P_L direct-sum C P_R.
```

Therefore the general invertible root-fiber map compatible with proper
Lorentz covariance and vector `U(1)` is

```text
R = r_L P_L + r_R P_R
  = r exp((xi+i theta) gamma^5)
```

after separating an overall nonzero complex scalar. The earlier scalar
identity ansatz was not the full competitor class.

Using only the future unit normal `n`, every isotropic chiral-odd endpoint
map is `slash(n)` times an element of the same commutant:

```text
E = slash(n)(e_L P_L+e_R P_R)
  = e slash(n) exp((eta+i delta) gamma^5).
```

This admits the nonunitary chiral rescalings `xi` and `eta`.

## Record-isometry reduction

The source-decorated object type requires its fiber maps to preserve the
positive hypersurface metric:

```text
h_(n_p)(U_e psi,U_e phi)=h_(n_r)(psi,phi).
```

The Elementary Record Hilbertization hypothesis separately requires the
fiber maps attached to elementary record inclusions to be isometries. In a
unit normal frame, these conditions reduce to

```text
R^dagger R=I,
E^dagger E=I.
```

For the complete chiral families above, this is equivalent to

```text
|r_L|=|r_R|=1,
|e_L|=|e_R|=1.
```

Hence

```text
xi=eta=0.
```

The nonunitary competitors were admitted first and rejected by the declared
record-isometry condition rather than silently omitted.

## Rejected source-frame quotient

Write the surviving maps as

```text
R=exp(i chi_r) exp(i theta gamma^5),
E=exp(i chi_e) slash(n) exp(i delta gamma^5).
```

Algebraically, right composition can remove `R` from the incidence column.
But an axial rotation does not preserve the fixed Clifford action unless the
Clifford representation and connection are simultaneously transformed. That
category equivalence was not defined. This quotient is therefore not
authorized as a physical source-frame equivalence.

```text
I at the root,
slash(n) exp(i delta_rel gamma^5) at the endpoint.
```

The algebraic relative-angle identity remains true, but it does not establish
that exactly one physical axial phase survives.

## Earned result and boundary

Given:

```text
the disclosed 3+1 proper-Lorentz Dirac carrier;
vector U(1);
the unit boundary normal;
metric-compatible edge transport;
and the adopted elementary-record isometry condition;
```

the constant full-Lorentz commutant calculation and the isometry rejection of
chiral rescalings are correct. They do not exhaust normal-dependent endpoint
maps or authorize the axial quotient.

## Status

```text
proper_Lorentz_Dirac_commutant_dimension_two = true
root_I_gamma5_competitor_family_admitted = true
endpoint_nonunitary_chiral_rescaling_family_admitted = true
metric_compatible_edge_transport_required = true
record_isometry_forces_root_xi_zero = true
record_isometry_forces_endpoint_eta_zero = true
unitary_source_frame_quotient_algebraically_computed = true
unitary_source_frame_quotient_physically_authorized = false
one_physical_relative_axial_phase_established = false
normal_dependent_source_map_family_exhausted = false
superseded_as_authoritative_classification = true
physical_record_Hilbertization_derived = false
charged_boundary_CPT_intertwiner_derived = false
global_connected_source_record_action_derived = false
alpha_computed = false
proof_authorized = false
```
