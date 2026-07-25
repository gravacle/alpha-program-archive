# Complete-Qspec Periodic Connected-Amplitude Numerical Block v001

Date: 2026-07-25

## Verdict

```text
PERIODIC_CONNECTED_AMPLITUDE_DIAGNOSTIC_BLOCKED
```

The exact transfer map successfully constructed connected amplitudes for as
many as 64 causally ordered fresh-record cells while propagating only one
`70 x 70` source cross-density. The smallest tested overlap remained:

```text
0.9845296106131252.
```

The intensive response was positive and approached a limit, but the
presealed finite-size threshold did not pass:

```text
N supercells   extrapolated intensive response
1              0.03240993550696358
2              0.08176837764623296
4              0.13462808634421108
8              0.16848181504504822
16             0.18574963856906540
32             0.19438495354317922
```

The tail decreased:

```text
|h_16-h_8|  = 0.01726782352401718
|h_32-h_16| = 0.008635314974113822
```

but the final difference was not below the preregistered `1e-6` threshold.
No cutoff or tolerance was changed.

## Disposition

The nearly halved tail is consistent with an `O(1/N)` boundary correction.
Brute-force extension until the threshold happens to pass is forbidden. The
correct successor is to derive the dominant eigenvalue of the period-two
cross-history transfer operator, certify its residual and isolation, and
obtain the infinite-chain intensive limit directly.

This blocked result does not affect the exact transfer-map theorem. It blocks
only the finite-schedule intensive-limit claim.

## Sealed artifacts

```text
ab5f44b8dfcab84ee25964f4184d8b5ca4599b85de2e4af603ab54dd3d353a81  COMPLETE_QSPEC_PERIODIC_CONNECTED_AMPLITUDE_DIAGNOSTIC_SPEC_V001.md
d109fc1ad7e7c65292631a1eafafe07d53c946f153521994be8e57315732fdec  scripts/derive_complete_qspec_periodic_connected_amplitude_v001.py
d8491a0a8008ac407ba3afe074fb253398f079689232d7ef399b048725eb0274  stage8_execution/work/QSPEC_periodic_connected_amplitude_v001.json
```

## Protected status

```text
relative_history_transfer_map_derived = true
periodic_connected_amplitude_constructed = true
periodic_intensive_limit_diagnostic_passed = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
local_Maxwell_response_derived = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
