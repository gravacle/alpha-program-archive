# BID Root Incidence Identity Derivation v001

Date: 2026-07-23

## Purpose

Determine the root component of the source-decorated cellular incidence map
without selecting a spinor endomorphism.

## Covariant cellular boundary

For an oriented edge `e:r->p` in a local coefficient system with transport
`U_e:E_r->E_p`, the covariant cellular boundary is

```text
partial_U(e tensor psi)
  =p tensor U_e psi-r tensor psi.
```

The root coefficient is the identity transport on `E_r`. This follows from
the identity-morphism axiom of the coefficient functor:

```text
U_(id_r)=I_(E_r).
```

Replacing the root term by `R(n_r) psi` would no longer be the cellular
incidence map. It would add a separate root zero-form endomorphism. Such
zero-forms belong to the complete parent-action competitor class, but they
are not alternate root coefficients of `partial_U`.

Therefore normal-dependent matrices such as `slash(n_r)` and
`slash(n_r) gamma^5` are valid zero-form competitors in the parent action,
not omitted competitors to the root incidence identity.

## Earned result and boundary

The root incidence component is canonically `-I` for every source fiber. This
does not forbid independent source zero-forms elsewhere in the complete
action and does not select the endpoint transport, source pole, or alpha.

## Status

```text
local_coefficient_identity_transport_typed = true
covariant_edge_boundary_formula_derived = true
root_incidence_component_is_negative_identity = true
normal_dependent_root_zero_forms_forbidden_in_complete_action = false
normal_dependent_root_zero_forms_are_incidence_coefficients = false
complete_parent_zero_form_family_enumerated = false
alpha_computed = false
proof_authorized = false
```
