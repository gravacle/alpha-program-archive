# Complete-Qspec Periodic Connected-Amplitude Diagnostic Specification v001

Date: 2026-07-25

## Purpose

Use the exact relative-history transfer map to construct a connected
many-record amplitude without an exponentially growing record Hilbert space,
and test whether the existing period-two finite regression has a convergent
intensive global-holonomy susceptibility.

This is a regulator diagnostic only. Repeating the two existing source masks
does not constitute the Lorentz-covariant continuum exhaustion and cannot
prove the linked-cluster, packing-independence, or Maxwell gates.

No coupling target, alpha value, endpoint value, or measured constant may
enter.

## Frozen authorities

```text
7e79583981dd97b2fb5e0ebb6a3498b7bdc03a29cb46f8e2c654f62bc52315ef  COMPLETE_QSPEC_RELATIVE_HISTORY_TRANSFER_MAP_SPEC_V001.md
3800b661ea0dacb052aeb0a843f331a13eddc9c838949e5e224c2a5c288271d1  scripts/derive_complete_qspec_relative_history_transfer_map_v001.py
b202278190c5e440713abbea247fcfcb92c1dc4fba1a1b08d8db648f3579caaf  stage8_execution/work/QSPEC_relative_history_transfer_map_v001.json
0a928509699a6d2a827c95bce7311e438e49424c22fc88142b1578d67a2368f6  scripts/verify_complete_qspec_relative_history_transfer_map_v001.py
868e14f16e75e17cfd7b50112354ec911286789fd4e482cec1931e956fd6b5e0  stage8_execution/work/QSPEC_relative_history_transfer_map_verification_v001.json
```

## C1 - Period-two regression

Let one supercell consist of the two already frozen intrinsic interactions:

```text
cell 0: source mask diag(1,1,0);
cell 1: source mask diag(0,1,1).
```

Repeat this supercell causally in time with one fresh ready record factor per
cell and no return interaction with a closed record. The shared source is
propagated by the exact cross-history transfer maps.

This repetition is fixed before execution. It is a computational regression,
not a claim that the two masks exhaust physical four-dimensional cells.

## C2 - Frozen grid

Use:

```text
supercell counts N = 1,2,4,8,16,32
cells = 2N
Strang steps per cell = 32 and 64
total Wilson-loop angles theta = 1/20 and 1/40
relative histories (+theta,0) and (-theta,0)
```

For each row compute:

```text
Z_N(theta)
 = Tr_S [(T_1^(theta,0) o T_0^(theta,0))^N(rho_in)].
```

The full record space is never built.

## C3 - Intensive response

For each time resolution and angle:

```text
H_N(theta)
 = [-log|Z_N(+theta)|-log|Z_N(-theta)|]/theta^2;

h_N(theta)=H_N(theta)/(2N).
```

Extrapolate second-order Strang error:

```text
h_N,inf(theta)
 = h_N,64(theta)+[h_N,64(theta)-h_N,32(theta)]/3.
```

Then extrapolate the centered angle:

```text
h_N(0)
 = [4 h_N,inf(1/40)-h_N,inf(1/20)]/3.
```

The radius is the maximum absolute time correction plus the absolute angle
correction plus `1e-8`.

## C4 - Diagnostic pass rule

Return:

```text
PERIODIC_CONNECTED_AMPLITUDE_DIAGNOSTIC_PASS
```

only if:

1. every frozen hash matches;
2. every tested amplitude is nonzero;
3. diagonal branch normalization remains one to `1e-9`;
4. every intensive-response interval is strictly positive;
5. the tail differences decrease:

```text
|h_32-h_16| < |h_16-h_8|;
```

6. and:

```text
|h_32-h_16| < 1e-6.
```

Otherwise return:

```text
PERIODIC_CONNECTED_AMPLITUDE_DIAGNOSTIC_BLOCKED
```

The numerical value may appear only as a regression susceptibility. It may
not be named `kappa_record`, transformed into alpha, or used to select any
operator.

## Mandatory limitations

Even a pass does not prove:

```text
a volume-uniform zero-free neighborhood;
an all-cellulation linked-cluster density;
Lorentz-covariant continuum convergence;
low-frequency temporal locality;
spatial plaquette response;
the Maxwell tensor;
kappa_record;
the Thomson limit;
alpha;
or proof authorization.
```

## Fixed status

```text
relative_history_transfer_map_derived = true
periodic_connected_amplitude_constructed = false
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
