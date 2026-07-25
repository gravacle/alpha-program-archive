# BID Active-Handle Control Gate v001

Date: 2026-07-23

## Purpose

The first-opening interval was derived on the closed-cell carrier of one
active handle. This gate tests whether the same interval applies to the full
three-edge first-opening star without an independently derived source/access
control. It uses no coupling target.

## Exact full-star check

For the first-opening star with one root, three endpoints, and three incidence
edges, let every unit-incidence edge be simultaneously active. The full
operator has spectrum

```text
{-2,-1,-1,0,1,1,2}.
```

At the handle-conditioned interval

```text
tau_R=pi/sqrt(2),
```

evolution from the root gives:

```text
root amplitude magnitude       = 0.0503084934689;
total endpoint probability     = 0.300637985859;
total edge-intermediate prob.  = 0.696831069626.
```

It is not a completed public record. Therefore the handle-conditioned
interval cannot be applied to the full star by notation alone.

## Required controlled operator

The strict route requires a source/access carrier with orthogonal projectors
`P_h^S` and a controlled record generator

```text
B_controlled
  =sum_(h in {M,Q,G}) P_h^S tensor B_h
```

on the single-active-handle sectors. For a source superposition, this operator
entangles source support with orthogonal record endpoints. For the pure
charged branch, `P_Q^S` must follow from the compact charge-access source
operator before the `Q`-conditioned interval is used.

The labels in `DecRec_2` distinguish handles but do not by themselves derive
the source projectors or prove that exactly one is active. A simultaneous
gravity-plus-charge event may require a separate composite-source sector and
its own first-opening calculation.

The positive-orientation-only v001 activation route is superseded. The
current charged-sector construction is
`BID_GLOBAL_CAR_CHARGE_AND_ACTIVATION_DERIVATION_V001.md`, with the primitive
restricted-sector algebra in
`BID_CHARGED_HANDLE_ACTIVATION_DERIVATION_V002.md`. Its source-access
projector is

```text
P_ch=1_(R\{0})(Q_Sigma),
```

which reduces to `Q_Sigma^2` only on the vacuum-plus-one-excitation quotient.
The simultaneous composite branch remains open.

## Status

```text
full_three_handle_star_checked = true
full_star_completes_at_handle_tau_R = false
handle_conditioning_is_load_bearing = true
pure_charged_source_access_projector_derived = true
pure_charged_single_active_handle_rule_derived = true
composite_handle_branch_derived = false
charged_branch_tau_R_authorized_inside_declared_flux_branch = true
primitive_record_stiffness_computed = false
alpha_computed = false
proof_authorized = false
```

## Next gate

Derive the source/access projectors and their controlled action from the
complete charged carrier. Then rerun first-opening and amplitude selection on
the complete controlled operator before using `tau_R` in a response.
