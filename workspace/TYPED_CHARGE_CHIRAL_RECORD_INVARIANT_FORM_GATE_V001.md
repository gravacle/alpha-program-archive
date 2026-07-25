# Typed Charge-Chiral-Record Invariant-Form Gate v001

Date: 2026-07-23

## Question

Does placing the charged source and record write inside one graded operator
force one common normalization, or do the typed factors admit independent
invariant weights?

This gate addresses that question before a complete environment or response is
constructed. It uses no alpha, mass, or endpoint value.

## Typed reduced carrier

For this identifiability calculation, keep three logically distinct binary
factors:

```text
H_typed
  = C^2_flux
    tensor C^2_chirality
    tensor C^2_record.
```

They represent:

```text
flux:
  the declared zero/one local unit-character source sector;

chirality:
  the left/right factor of the vectorlike source;

record:
  the two-endpoint comparison factor.
```

This reduced tensor product is declared for the calculation. It is not the
complete Dirac/Fock/environment carrier.

Let

```text
Q = (I-Z_flux)/2.
```

The two real chiral-odd source directions are

```text
M_X = Q tensor X_chi tensor I_record,
M_Y = Q tensor Y_chi tensor I_record.
```

The two real flux-conditioned record-changing directions are

```text
W_X = Q tensor I_chi tensor X_record,
W_Y = Q tensor I_chi tensor Y_record.
```

All four commute with the flux projector and are vector-`U(1)` neutral as
operators. The `M` plane rotates under chiral rephasing; the `W` plane rotates
under record-basis rephasing.

## Exact invariant-form calculation

On the real coefficient space

```text
V = span_R{M_X,M_Y,W_X,W_Y},
```

the independent infinitesimal rephasings act as

```text
A_chi = J_2 direct-sum 0_2,
A_record = 0_2 direct-sum J_2,

J_2 = [[0,-1],[1,0]].
```

For a real symmetric quadratic form `G`, invariance requires

```text
A_chi^T G + G A_chi = 0,
A_record^T G + G A_record = 0.
```

The exact linear system on the ten-dimensional symmetric-matrix space has
rank `8` and nullity `2`. Its invariant forms are

```text
G = diag(kappa_M,kappa_M,kappa_W,kappa_W).
```

Thus the typed symmetries permit independent source-odd and record-write
normalizations. Positivity restricts their signs; it does not force
`kappa_M=kappa_W`.

If one additionally imposes an exact swap of the chirality and record planes,
the invariant-form nullity becomes `1`. But no sealed premise derives such a
swap. Chirality and a public pointer have different transformation laws,
operational roles, and anomaly obligations. Adding the swap solely to obtain
one normalization would be a selector insertion.

## Consequence for the superconnection route

A single block matrix or superconnection can contain both `M` and `W`. That
packaging alone does not supply a unique norm. The common-normalization claim
requires one of:

1. a derived total-space geometry whose automorphism group forces the swap or
   another unique invariant form;
2. a complete microscopic dilation in which both outputs are calculated from
   the same off-diagonal matrix elements and resolvent; or
3. a separate target-independent physical law fixing
   `kappa_M/kappa_W`.

The second route remains the preferred strict route because it can calculate
the ratio without declaring an equality.

## Exact next gate

Construct the physical source-record-environment/edge dilation and compute:

```text
the reduced record channel;
the chiral-odd Schur self-energy;
the dimension of all surviving independent rescalings.
```

The same sealed microscopic matrix elements must generate both outputs. If an
independent `kappa_M/kappa_W`, closure gap, cell interval, or edge weight
remains, the alpha route stays blocked.

## Status

```text
typed_flux_chirality_record_factor_declared = true
complete_physical_carrier_derived = false
typed_candidate_operator_dimension = 4
vector_U1_neutrality_verified = true
independent_rephase_invariant_form_dimension = 2
invariant_form_has_independent_mass_and_record_weights = true
chirality_record_swap_reduces_form_dimension_to_one = true
chirality_record_swap_derived = false
single_superconnection_forces_common_normalization = false
unique_full_carrier_coupling_ray_derived = false
complete_source_record_environment_operator_derived = false
record_onset_to_source_self_energy_ratio_derived = false
record_generated_source_mass_derived = false
spectral_evaluation_authorized = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
