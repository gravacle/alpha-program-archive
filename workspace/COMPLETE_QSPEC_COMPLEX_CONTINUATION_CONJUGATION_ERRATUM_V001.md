# Complete-Qspec Complex-Continuation Conjugation Erratum v001

Date: 2026-07-25

## Finding

The complex continuation used by
`derive_complete_qspec_periodic_complex_zero_free_v002.py` is not
holomorphic in the declared complex field.

The inherited real-axis covariant difference constructs

```text
p(theta) = exp(i theta/3)
```

and uses `p(theta).conjugate()` for the oppositely oriented edge. For real
`theta`, this is correctly

```text
exp(-i theta/3).
```

For complex `theta`, however, it becomes

```text
exp(-i conjugate(theta)/3),
```

so the resulting matrix depends on both `theta` and `conjugate(theta)`.
That is not the analytic continuation required for a complex zero-free or
winding theorem.

## Consequence

The following claims from the v002 complex diagnostic are withdrawn from
proof-tier use:

```text
complex-disk zero-free evidence;
boundary winding numbers as an argument-principle diagnostic;
and any analytic spectral inference from those complex samples.
```

The real-axis preflight and every independently real-axis transfer,
intensive-limit, and connected-kernel calculation remain valid. This
erratum does not alter those results.

## Required repair

The successor continuation must define the two directed edge factors
independently:

```text
p_forward(theta)  = exp(+i theta/3)
p_backward(theta) = exp(-i theta/3),
```

without complex conjugation. It must then:

```text
1. prove entrywise holomorphy;
2. reproduce the frozen Hermitian operator on the real axis;
3. pass an independent complex Cauchy-Riemann/derivative check;
4. rerun all complex-disk, winding, and transfer-spectrum diagnostics;
5. retain volume_uniform_zero_free_neighborhood_proved = false unless a
   separate all-volume analytic theorem is supplied.
```

## Supersession

```text
periodic_complex_zero_free_diagnostic_v002_valid = false
periodic_complex_zero_free_diagnostic_passed = false
complex_zero_free_analytic_evidence_reestablished = false
```

The invalid diagnostic is preserved as historical output and is not edited.
This erratum is append-only.

## Artifact ledger

```text
fc2ca9ff890f3833a495107ae4619b3b341e009a1357ae2943836fd5ecf5456d  COMPLETE_QSPEC_PERIODIC_COMPLEX_ZERO_FREE_DIAGNOSTIC_SPEC_V001.md
704f5498d8ace502d1c23787a6d44436bb2dde2d1872c3048bc60a7dc7c8770f  scripts/derive_complete_qspec_periodic_complex_zero_free_v002.py
6ad27a95f1b480c694162f36694ec9f5dd91302e94e34094946babb93c33b089  stage8_execution/work/QSPEC_periodic_complex_zero_free_v002.json
2fdfe7463ee8f3c2b7a4a0ce7befe9f78e6e2d744d875b0724a3f1ee758920ee  COMPLETE_QSPEC_PERIODIC_COMPLEX_ZERO_FREE_DIAGNOSTIC_RESULT_V001.md
3800b661ea0dacb052aeb0a843f331a13eddc9c838949e5e224c2a5c288271d1  scripts/derive_complete_qspec_relative_history_transfer_map_v001.py
d109fc1ad7e7c65292631a1eafafe07d53c946f153521994be8e57315732fdec  scripts/derive_complete_qspec_periodic_connected_amplitude_v001.py
```

## Protected status

```text
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
