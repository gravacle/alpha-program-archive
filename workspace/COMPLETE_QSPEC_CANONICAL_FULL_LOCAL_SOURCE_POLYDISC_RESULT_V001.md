# Complete-Qspec Canonical Full Local-Source Polydisc Result v001

Date: 2026-07-25

## Verdict

```text
CANONICAL_FULL_PERIODIC_LOCAL_SOURCE_POLYDISC_PROVED
```

## Sealed execution chain

```text
4e9a780da0e3e26013f914347563cbb9e556b3d052d9760ff766c17dd01c0e07  COMPLETE_QSPEC_CANONICAL_FULL_LOCAL_SOURCE_POLYDISC_SPEC_V001.md
4c7903265d750da06ab47d5a71f4e664972d2e9a89125ec0ea7868ce0e0c0f24  scripts/certify_complete_qspec_canonical_full_local_source_polydisc_v001.py
ba71b8d613ab1dab4dff248e806c4c306a474d4e72b94d4090b2a15f1145d917  stage8_execution/work/QSPEC_canonical_full_local_source_polydisc_v001.json
```

The isolated executor verified the exact bridge, canonical transfer,
homogeneous full-amplitude theorem, local-source lift, and sealed
nonautonomous factorization lemma directly. No PASS-bearing theorem
condition was hardcoded.

## Result

For every finite integer `N>=1` and every independent source assignment

```text
|z_j|<=1/500,                j=1,...,N,
```

the physical full completed-record amplitude satisfies

```text
|Z_N^full(z_1,...,z_N)|
 >=[1-sqrt(5)/20] d^N
 >0,
```

with certified bounds

```text
d                              > 0.9915775525
1-sqrt(5)/20                   > 0.8881966011
graph-map norm                 < 0.0494388436 < 0.05
graph contraction              < 0.8273865662 < 1
graph contraction margin       > 0.1726134338
```

The physical terminal trace eliminates the stable component exactly. The
proof uses no finite-volume sampling and no finite/large-volume split.

Because `Z_N^full(0,...,0)=1`, the choice

```text
Log Z_N^full(0,...,0)=0
```

fixes a unique holomorphic logarithm on the open polydisc. Its mixed
derivatives are the finite-volume connected cumulants of the ordered local
insertions.

## Scope

```text
canonical_full_periodic_local_source_polydisc_proved=true
full_completed_record_amplitude_local_source_zero_free_for_all_volumes=true
finite_volume_multivariable_log_generator_proved=true
periodic_boundary_graph_contraction_proved=true

physical_continuum_local_source_addressability_derived=false
periodic_connected_linked_cluster_density_proved=false
connected_cumulant_absolute_majorant_proved=false
periodic_connected_cumulant_thermodynamic_limit_proved=false
all_stage8_regulators_zero_free_proved=false
all_connected_cellulations_linked_cluster_proved=false
kappa_record_computed=false
physical_Thomson_stiffness_computed=false
coupling_evaluation_authorized=false
alpha_computed=false
proof_authorized=false
```

The newly supplied Stage-8 direction now takes priority: primitive
amplitude, carrier, causal-exhaustion/cellulation, and one-handle reduction
must be discharged before this Qspec contraction datum is used for the
connected-majorant gate.
