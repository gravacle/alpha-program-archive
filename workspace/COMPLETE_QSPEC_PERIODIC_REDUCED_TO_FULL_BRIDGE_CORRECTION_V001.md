# Complete-Qspec Periodic Reduced-to-Full Bridge Correction v001

Date: 2026-07-25

## External adjudication authority

```text
83a59120eb09e4d058602234d89aacfe6aeedaa792d4983f3ae8e3389f6efcf2
/Users/bgm/MB Work/alpha_supervision/OVERNIGHT_PROOF_ADJUDICATION_RETURN_V001.md
```

The return was hash-verified before this correction was written.

## Finding

The exact-dyadic ball certificate and the nonautonomous anchor inequalities
are sound for the emitted `350 x 350` reduced transfer. The bridge from that
transfer to the full completed-record amplitude uses a five-dimensional
zero-history support obtained by binary64 SVD/Krylov construction.

The measured support-invariance residual

```text
1.556582229217841e-14
```

was gated numerically but was not enclosed by ball arithmetic and was not
propagated through every volume. A hostile recomputation found that the
existing reduced lower bound can fall below a conservative accumulated-leak
bound near `N=2400--2600`. Therefore the sealed certificates do not currently
authorize an every-volume theorem for the full completed-record amplitude.

## Append-only status correction

The surviving earned result is:

```text
frozen_dyadic_reduced_transfer_zero_free_for_all_volumes = true
frozen_dyadic_reduced_transfer_thermodynamic_log_density_proved = true
```

The stronger statuses are suspended:

```text
full_completed_record_amplitude_zero_free_for_all_volumes = false
full_completed_record_amplitude_thermodynamic_log_density_proved = false
frozen_periodic_local_source_polydisc_proved = false
periodic_connected_linked_cluster_density_proved = false
```

No sealed artifact is rewritten.

## Precommitted repair route

The program requires the full completed-record amplitude downstream.
Accordingly, the repair route is fixed before any coupling result:

1. reconstruct the exact-dyadic leakage blocks from the frozen zero-history
   Kraus operators and the emitted five-dimensional support;
2. ball-certify the support-invariance residual;
3. derive a leak-propagation lemma that compares the full and reduced
   amplitudes uniformly in volume, including the off-support dynamics;
4. if the lemma cannot dominate the certified reduced floor for every
   volume, build and certify a full-space invariant splitting or an exact
   symmetry-derived invariant support;
5. only after that bridge passes may the local-source polydisc spec be sealed
   and executed for the full amplitude.

The route may not be changed because one alternative produces a preferred
downstream number.

## Fixed flags

```text
kappa_record_computed=false
physical_Thomson_stiffness_computed=false
coupling_evaluation_authorized=false
alpha_computed=false
proof_authorized=false
```
