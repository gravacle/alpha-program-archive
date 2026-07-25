# Complete-Qspec Analytic-Continuation Independent Preflight Failure v001

Date: 2026-07-25

## Verdict

```text
INDEPENDENT_PERIODIC_ANALYTIC_CONTINUATION_BLOCKED
```

The sealed independent verifier passed every repaired analytic,
source-support, reduced/direct, producer-comparison, full-spectrum, and
sampled-point all-volume dominance gate. It failed only the separately
frozen zero-history normalization ceiling:

```text
required maximum error                  < 1.0e-11
observed N=64 zero-history error          1.5351275806203765e-11
```

The same error grows approximately linearly with repeated applications:

```text
N=1    2.774447338538266e-13
N=2    5.261346960606261e-13
N=8    1.968869511932099e-12
N=64   1.5351275806203765e-11
```

This is consistent with accumulated roundoff from using the independent
Taylor exponential on a branch known exactly to be Hermitian/unitary. No
complex row failed.

## Passed findings retained as diagnostics

```text
zero-history reachable support dimension      5
support invariance residual                    2.946714125273096e-14
all eight complex spectral rows pass           true
maximum remainder norm ratio                   0.8115707187802899
maximum N>=5 dominance bound                   0.7872480399679019
maximum analytic derivative residual           1.6669042137962679e-10
```

The dominance bound is below one at all eight frozen boundary directions,
but the overall verifier remains blocked exactly as preregistered.

## Disposition

The threshold is not changed and the v001 verifier is not edited. A
successor may use the spectral theorem for the exactly Hermitian
zero-history half-step while retaining the independently implemented Taylor
exponential for the non-Hermitian analytic branch. This improves the
algorithm rather than relaxing the gate.

## Artifact ledger

```text
e5630cbc9d5d92607773ebb5fc8f8a90075f437d8131311e7d1ec6f5bb84ce0e  COMPLETE_QSPEC_ANALYTIC_CONTINUATION_INDEPENDENT_VERIFIER_PROTOCOL_V001.md
d822621721444d9fab9af32425d8ecc95190933465b974d7883b2740b3c920fe  scripts/verify_complete_qspec_periodic_analytic_continuation_v001.py
32d381c65bce844615c92e5fcd7138e3fb7e772b952fc359f3d947f189c4e744  stage8_execution/work/QSPEC_periodic_analytic_continuation_verification_v001.json
```

## Protected status

```text
independent_analytic_continuation_confirmed = false
sampled_point_all_volume_dominance_confirmed = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
