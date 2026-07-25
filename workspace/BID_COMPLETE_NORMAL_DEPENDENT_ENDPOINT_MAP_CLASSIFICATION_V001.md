# BID Complete Normal-Dependent Endpoint Zero-Form Classification v001

Date: 2026-07-23

## Purpose

Classify every local proper-Lorentz-covariant endpoint zero-form constructed
from a Dirac carrier and one future unit normal, without imposing chiral
oddness or using alpha. These maps are parent-action competitors. They are not
coefficients of the covariant cellular incidence boundary.

## Little-group classification

At a reference normal `n_0`, covariance reduces the classification to the
commutant of its `Spin(3)` little group. On one Dirac carrier,

```text
End_(Spin(3))(S) is isomorphic to M_2(C)
```

and has complex basis

```text
I,
gamma^5,
slash(n_0),
slash(n_0) gamma^5.
```

Transporting this basis with `Spin^+(1,3)` gives the complete natural family
at every future unit normal `n`:

```text
E(n)=a I+b gamma^5+c slash(n)+d slash(n) gamma^5.
```

The chiral-odd family `slash(n)(c I+d gamma^5)` is a proper subfamily. It is
not assumed to be the complete endpoint class.

## Conditional source-independent normalization lemma

Before normalization, all matrices in this four-complex-dimensional family
are admitted, including full-rank nonunitary, rank-deficient, and zero maps.
No isometry condition is imposed on `E`.

If an endpoint zero-form is inserted into the restricted pure off-diagonal
source-record model, its decorated column is

```text
D_(a,b,E)=[-a I;b E(n_p) U_e].
```

Calculations below may be reduced to the endpoint frame, where the
metric-compatible transport `U_e` is suppressed.

The additional requirement

```text
D_(a,b,E)^sharp D_(a,b,E)=kappa I
```

for every source spinor is a source-independent scaled-normalization premise.
It is not a consequence of QR1--QR7, which fix the record-label metric rather
than the norm of a dynamical transition map. Conditional on this premise and
nonzero completed endpoint support,

```text
E^(sharp_n) E=lambda I,
lambda=(kappa-|a|^2)/|b|^2.
```

Here `sharp_n` is the adjoint in the positive hypersurface metric
`H_n=gamma^0 slash(n)`. At the reference normal `H_(n_0)=I`, so it is the
ordinary matrix adjoint. Completion for every source direction requires
`lambda>0`. The positive-metric polar decomposition then gives

```text
E=sqrt(lambda) U,
U^(sharp_n) U=I.
```

The positive factor `sqrt(lambda)` is absorbed into `b`. At the reference
normal, `U` is the `U(2)` family acting on the two equivalent spin-`1/2`
multiplicity sectors. Covariance transports the same classification to every
future unit normal.

For `E=A tensor I_2` at the reference normal, the complete possible ranks are
`0`, `2`, and `4`. Completed endpoint support rejects the zero map. The
conditional normalization equation rejects every nonzero rank-`2` map and
every anisotropic full-rank rescaling. It does not select one `U(2)` element
or force the endpoint into the chiral-odd subfamily.

## Bare incidence and conditional transfer

The actual covariant cellular boundary is already fixed:

```text
partial_U(e tensor psi)
  =p tensor U_e psi-r tensor psi.
```

Thus the bare incidence column is `[-I;U_e]`. A separate root dressing
`R(n_r)` or endpoint dressing `E(n_p)` is a degree-zero parent operator, not
an alternate incidence coefficient. Both belong to the still-open complete
parent classification.

Conditional on excluding all diagonal zero-form detuning and choosing the
restricted pure off-diagonal model

```text
B=[[0,D],[D^sharp,0]],
D=[-a I;b U],
```

the bright-mode transfer calculation has

```text
P_endpoint,max
  =4 |a|^2 |b|^2/(|a|^2+|b|^2)^2
  <=1.
```

Exact completed transfer holds only at `|a|=|b|`. Unit one-record
normalization then fixes `|a|=|b|=1`, independently of `U`. This is a
conditional result for the pure off-diagonal model; parent zero-forms can
detune the transfer and remain open.

## Earned result and boundary

The complete normal-dependent complex-linear endpoint zero-form family is
derived. Given the additional scaled-normalization premise, it reduces to a
transported `U(2)` family. Given the further pure off-diagonal and exact
transfer premises, the effective endpoint magnitudes are equal independently
of the unresolved `U(2)` element.

This does not derive scaled normalization, select the endpoint `U(2)` element,
derive CPT/CP restrictions, exclude root or endpoint zero-form detuning,
construct the connected action, or compute alpha.

## Status

```text
normal_dependent_little_group_commutant_dimension_four = true
I_gamma5_slashn_slashn_gamma5_basis_complete = true
chiral_even_endpoint_competitors_admitted = true
chiral_odd_endpoint_subfamily_only = false
endpoint_zero_form_is_incidence_coefficient = false
endpoint_zero_form_competitor_class_complete_given_one_normal = true
endpoint_rank_strata_zero_two_four_complete = true
all_spinor_scaled_normalization_derived_from_QR1_through_QR7 = false
conditional_scaled_normalization_forces_E_sharp_E_scalar = true
conditional_rank_deficient_endpoint_rejected = true
conditional_anisotropic_endpoint_rescaling_rejected = true
h_n_adjoint_used_away_from_reference_normal = true
conditional_scaled_unitary_factor_absorbed_into_weight = true
conditional_endpoint_family_reduces_to_U2 = true
endpoint_U2_element_selected = false
root_source_frame_axial_quotient_used = false
bare_covariant_incidence_column_is_minusI_plus_Ue = true
conditional_pure_offdiagonal_equal_transfer_independent_of_U2 = true
parent_zero_form_detuning_excluded = false
complete_parent_zero_form_family_enumerated = false
global_connected_source_record_action_derived = false
alpha_computed = false
proof_authorized = false
```
