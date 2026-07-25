# BID Lorentz-Covariant Source-Boundary Map Derivation v001

Date: 2026-07-23

## Scope

This derivation replaces the bare two-state chirality label with the local
Dirac bundle appropriate to an oriented spacelike record boundary. It derives
the finite chiral map from the boundary normal. It does not derive the global
fermionic Fock/CAR parent, a physical mass, or alpha.

The following are disclosed spacetime inputs:

```text
3+1 Lorentz signature (+---);
a spin structure;
one vectorlike Dirac source;
the ordinary vector U(1) charge action;
and CPT for a local Lorentz-covariant fermion theory.
```

They are not counted as Gravacle outputs.

## Dirac and boundary carriers

Let

```text
S=S_L direct-sum S_R
```

be the four-complex-dimensional Dirac fiber and let `L^q` be the charge-`q`
line. The pointwise charged source fiber is

```text
E_q=S tensor L^q.
```

Quantized particles and antiparticles require the later global CAR
construction from charged solutions and their conjugates. They are not
obtained by calling the pointwise `C^4` fiber a particle/antiparticle space.

An oriented spacelike record boundary has a future unit timelike normal `n`,

```text
g(n,n)=1.
```

The positive boundary inner product is

```text
h_n(psi,phi)
  =bar(psi) slash(n) phi
  =psi^dagger gamma^0 slash(n) phi.
```

In the rest boundary frame `n=(1,0,0,0)`, `h_n` is the ordinary positive
spinor product.

## Complete local scalar/pseudoscalar family

For one vectorlike Dirac source, the local algebraic proper-Lorentz scalar
chiral-odd Hermitian bilinears form the real span

```text
bar(psi) psi,
i bar(psi) gamma^5 psi.
```

Before physical magnitude selection the complete family is

```text
L_odd(rho,delta)
  =rho bar(psi) exp(i delta gamma^5) psi
  =rho cos(delta) bar(psi)psi
   +rho sin(delta) i bar(psi)gamma^5 psi,

rho>0.
```

No electromagnetic target value enters this classification.

## Boundary Riesz map

The operator representing `L_odd(delta)` on the positive boundary Hilbert
fiber is fixed by

```text
h_n(psi,M_(n,rho,delta) phi)
  =rho bar(psi) exp(i delta gamma^5) phi
```

for every `psi,phi`. Because `slash(n)^2=1`,

```text
M_(n,rho,delta)=rho slash(n) exp(i delta gamma^5).
```

This is the missing covariant origin of the finite chiral map. In the rest
boundary frame and Weyl basis, the unit representative `rho=1` is

```text
M_(n0,1,delta)
  =gamma^0 exp(i delta gamma^5)
  =[[0,exp(i delta) I_2],
    [exp(-i delta) I_2,0]].
```

After suppressing the untouched spin multiplicity, this is exactly the
`C_delta` used in the finite incidence parent. The physical unit magnitude is
not derived in this file; it belongs to the complete incidence-weight and
record-Hilbertization gates.

For `rho=1` the map is:

```text
chiral odd;
neutral under the vector U(1);
self-adjoint in h_n;
unitary in h_n;
and proper-orthochronous Lorentz covariant:
M_(Lambda n,1,delta)
  =S(Lambda) M_(n,1,delta) S(Lambda)^(-1),
Lambda in SO^+(1,3).
```

The boundary normal is load-bearing. Without it, there is no nonzero complex
linear Lorentz intertwiner between the inequivalent Weyl representations.

## CPT

Use the conventional antiunitary Dirac-field action in the Weyl
representation

```text
Theta_CPT psi(x) Theta_CPT^(-1)
  =U_X psi^*(-x),

U_X=gamma^5 gamma^2=i gamma^0 gamma^1 gamma^3,
```

up to an irrelevant constant phase. The complete four-gamma intertwining,
future-normal convention, charge-line action, and transported record-edge
equation are derived and audited in
`BID_CHARGED_CELLULAR_CPT_INTERTWINER_DERIVATION_V001.md`. The earlier
`i (gamma^5)^*` shortcut is not used because it fails the full Weyl-basis
Clifford intertwining test.

For fermion bilinears, standard Dirac/CAR CPT maps both the scalar and
pseudoscalar terms above to their Hermitian conjugates at `-x`. Since
`L_odd(rho,delta)` is Hermitian for real `rho,delta`,

```text
Theta_CPT L_odd(rho,delta,x) Theta_CPT^(-1)
  =L_odd(rho,delta,-x).
```

Thus CPT admits the entire real `delta` family; it does not select
`delta=0`. This agrees with the earlier phase audit rather than erasing its
open axial/topological question.

This file imports the standard bilinear parity but does not independently
derive it from the CAR field algebra. The charged source-record intertwiner
is supplied by the dedicated CPT derivation rather than by this local
Lorentz-map file.

The CPT convention and bilinear rule are standard Dirac-field results; see:

```text
M. Socolovsky, The CPT Group of the Dirac Field,
arXiv:math-ph/0404038.

C. Jarlskog, CPT, Majorana Fermions, and Particle Physics Beyond the
Standard Model, Prog. Theor. Exp. Phys. 2024, 08C101.
```

## What is now derived

This file derives, without a coupling or mass target:

```text
the four-component local Dirac source fiber;
the positive hypersurface metric;
the complete isotropic algebraic scalar/pseudoscalar family;
the boundary-normal Riesz map;
the proper-orthochronous Lorentz-covariant lift of C_delta;
vector-U(1) neutrality;
and neutral-bilinear CPT evenness of the whole delta family.
```

## What remains

The following are not implied by the local map:

```text
the global charged-solution and antiparticle CAR carrier;
the source-decorated record category and all alternative incidence graphs;
the anomaly/topology/CP selection or irrelevance of delta;
the charged-current derivation of the active-handle projector;
connected source-record gluing and preparation;
the physical source two-point function and pole;
the complete Q_spec;
or alpha.
```

## Status

```text
three_plus_one_Lorentz_spin_CPT_disclosed_input = true
local_Dirac_source_fiber_typed = true
pointwise_Dirac_fiber_called_particle_antiparticle_space = false
positive_boundary_hypersurface_metric_derived = true
minimal_isotropic_scalar_pseudoscalar_family_classified = true
boundary_normal_Riesz_map_derived = true
finite_C_delta_recovered_with_spin_multiplicity = true
proper_orthochronous_Lorentz_covariance_derived = true
improper_Lorentz_delta_transformation_classified = false
vector_U1_neutrality_derived = true
CPT_field_action_disclosed = true
neutral_bilinear_CPT_evenness_of_delta_family_disclosed_standard = true
neutral_bilinear_CPT_evenness_of_delta_family_derived_here = false
charged_boundary_CPT_intertwiner_derived = false
CPT_selects_delta_zero = false
relative_axial_phase_unresolved = true
unit_magnitude_rho_derived_here = false
global_particle_antiparticle_CAR_carrier_derived = false
complete_source_decorated_category_derived = false
connected_many_record_parent_derived = false
physical_source_mass_computed = false
complete_Q_spec_sealed = false
alpha_computed = false
proof_authorized = false
```
