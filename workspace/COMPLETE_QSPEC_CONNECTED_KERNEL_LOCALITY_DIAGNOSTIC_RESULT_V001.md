# Complete-Qspec Connected-Kernel Locality Diagnostic Result v001

Date: 2026-07-25

## Verdict

```text
PERIODIC_CONNECTED_KERNEL_LOCALITY_DIAGNOSTIC_PASS
INDEPENDENT_PERIODIC_CONNECTED_KERNEL_LOCALITY_CONFIRMED
```

The frozen period-two sequential Qspec regulator has a rapidly decaying
bulk connected response kernel and a stable low-frequency expansion.

## Primary result

The primary calculation finite-differenced `-log|Z|` for pairs of
perturbed supercells at separations `r=0,...,10`, using two bulk anchors,
two field increments, and two time discretizations.

```text
minimum tested amplitude absolute       0.999827471174916
fitted connected-kernel decay q         0.44344643960446345
decay-fit R^2                            0.9515572717606359
C_8                                      -0.20804496026212033
C_10                                     -0.2057726611406342
|C_10-C_8|/|C_10|                       0.011042764908080484
```

The two anchor kernels agree below `2.2e-9` relative on the frozen
`r=0,...,8` comparison rows. Truncated Fourier responses are positive at
`k=0`, `pi/16`, and `pi/8` for both cutoffs.

## Independent verification

The verifier used a different calculation:

```text
five-point derivatives of the one-supercell transfer map;
step counts {48,96}, distinct from the primary {32,64};
an iterated zero-field bulk state;
direct T', T'', and T_0^(r-1) connected-correlation formulas.
```

It found:

```text
maximum primary/independent kernel difference   8.476943813175236e-05
independent decay q                             0.44343214480831733
independent decay-fit R^2                       0.9515551991908217
independent C_10                                -0.20577401362814848
independent cutoff difference                   0.011041496371097649
```

The independently generated bulk state passes the frozen trace and
stationarity gates.

## Interpretation

The sign-alternating tail is exponentially suppressed rather than
long-ranged. The stable second moment supplies a well-defined
low-frequency quadratic coefficient for this regulator. This is the
correct prerequisite for a later temporal-gradient/Maxwell comparison; it
is not itself that comparison.

## Scope

This result is limited to the frozen strictly sequential period-two
regulator. It does not prove:

```text
all-cellulation locality;
a volume-uniform complex zero-free neighborhood;
a universal linked-cluster density;
the Maxwell tensor;
kappa_record;
the Thomson limit;
alpha;
or proof authorization.
```

## Artifact ledger

```text
1073e8d7c4aa590d1f45c0d1376b97ae7895181d22e2479ce2af9493f410a6b7  COMPLETE_QSPEC_CONNECTED_KERNEL_LOCALITY_DIAGNOSTIC_SPEC_V001.md
2795e2b6c9e3176911508445bf13e1145e4cb258361432413939b9c86cbebfcf  scripts/derive_complete_qspec_connected_kernel_locality_v001.py
f22706d4d2a72c764a35b6e5874a52f25e4bd56ee88dabd9405541cce5b5ea4b  stage8_execution/work/QSPEC_connected_kernel_locality_v001.json
349d56e6b884664a8d99aa84c9a2fa2f2d833fa58018bda824bc623932ba09bf  COMPLETE_QSPEC_CONNECTED_KERNEL_INDEPENDENT_VERIFIER_PROTOCOL_V001.md
087a12b8e6fe588bc93df0c8da231185b57732d9c62cfb1ae702bf243aa2a94c  scripts/verify_complete_qspec_connected_kernel_locality_v001.py
d591fa677cf1e6ae0b2fecb49de1cb936fdd11d6f199f47f88eb90bd30cd04a2  stage8_execution/work/QSPEC_connected_kernel_locality_verification_v001.json
```

## Status

```text
periodic_connected_kernel_locality_diagnostic_passed = true
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
local_Maxwell_response_derived = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
