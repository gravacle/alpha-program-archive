# Complete-Q_spec Relative-History CTP Amplitude Result v001

Date: 2026-07-25

## Verdict

```text
COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_CLOSURE_DERIVED
```

The complete source-record parent and the disclosed incoming state canonically
define a scalar relative-history functional:

```text
Z_K[A_+,A_-]
 =omega_in(W_K[A_-]^dagger W_K[A_+]).
```

The final identity retains every source and record outcome. No record outcome
is postselected, and no final source ray, finite normalized trace,
determinant, or regulator-dependent scalarization is introduced.

This resolves the scalar-closure type problem at complete `Q_spec`. It does
not retroactively scalarize primitive Stage 8.

## Exact properties

State positivity and unitarity give:

```text
Z_K[A,A]=1;
Z_K[A_+,A_-]^*=Z_K[A_-,A_+];
|Z_K[A_+,A_-]|<=1.
```

A common gauge transformation of both histories conjugates both evolutions
and the incoming state coherently, leaving the scalar unchanged.

For disjoint systems with factorized incoming states:

```text
Z_(K1 disjoint K2)=Z_K1 Z_K2;
-log|Z_(K1 disjoint K2)|
 =-log|Z_K1|-log|Z_K2|.
```

This supplies exact disjoint monoidality. Connected cellulations still
require the linked-cluster theorem.

## One-cell exact regression

For the complete two-outcome comparator:

```text
Z(theta_+,theta_-)
 =[1+exp(i(theta_+-theta_-))]/2.
```

The primary and independent outcome-sum implementations verified:

```text
diagonal CTP normalization                PASS
CTP Hermiticity                           PASS
contractivity                             PASS
disjoint amplitude factorization          PASS
additivity of -log|Z|                      PASS
```

Near zero:

```text
Z(delta,0)=exp(i delta/2) cos(delta/2);
-log|Z(delta,0)|=delta^2/8+O(delta^4);
[-log|Z(delta,0)|]''_(delta=0)=1/4.
```

The independent verifier recovered `1/4` from exact Taylor coefficients.
The exclusive preserved-reference probability is different from the
complete diagonal CTP kernel and was not substituted.

## Relation to the primitive no-go

The primitive completed-record compression remains an operator on the
source. Here the already-disclosed physical incoming state supplies the
functional:

```text
omega_in: A_source-record -> C.
```

That is why the scalar exists at complete `Q_spec` without existing
canonically at the primitive layer. This is a typed resolution, not a
numerical workaround.

## Next obligation

The next sealed gate must insert the target-independent compact connection
history into the actual finite source-record parent and compute:

```text
the reference-branch relative-history amplitude;
its nonzero local transverse Hessian;
its equality with the independently computed Duhamel covariance;
and the finite zero-free neighborhood.
```

Only after the continuum gauge/edge completion, linked-cluster limit,
packing independence, threshold map, and Thomson matching may a physical
coupling be evaluated.

## Artifact hashes

```text
ddb51c32e1ec45e6145be4c688f2af5fa87823ab20b4f523fc4657823165e544  COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_AMPLITUDE_SPEC_V001.md
ba4dcee42905f862208881c8b0ad25c94c608267fd5583de9874a1880602f457  scripts/derive_complete_qspec_relative_history_ctp_amplitude_v001.py
235f9016fd6fec510f5efa6ce2c029c120b84ac406ebb12a53c66e969caefe0a  stage8_execution/work/QSPEC_relative_history_CTP_closure.json
37abdd0109a68ee26418eae7cd16d34a924bbb11a0162088219bd1d4a303d620  scripts/verify_complete_qspec_relative_history_ctp_amplitude_v001.py
f47d81adccf2c27682205fb1771d413b453333d2adff05b0cf1c0f5f2a764afe  stage8_execution/work/QSPEC_relative_history_CTP_closure_verification.json
```

## Fixed status

```text
primitive_source_scalarization_derived = false
complete_Qspec_CTP_scalar_closure_derived = true
interacting_continuum_CTP_amplitude_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
Duhamel_intensive_Hessian_equality_proved = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
