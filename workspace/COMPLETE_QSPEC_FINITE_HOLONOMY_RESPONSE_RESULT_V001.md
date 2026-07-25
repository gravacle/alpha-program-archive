# Complete-Qspec Finite-Holonomy Response Result v001

Date: 2026-07-25

## Verdict

```text
FINITE_QSPEC_HOLONOMY_RESPONSE_DIAGNOSTIC_PASS
INDEPENDENT_FINITE_QSPEC_HOLONOMY_RESPONSE_CONFIRMED
```

The derived complete-Qspec relative-history CTP scalar carries a strictly
positive response to the frozen total Wilson-loop coordinate on the existing
three-site finite regulator.

This result closes the finite global-holonomy diagnostic only.

## Sealed execution lineage

The first two convergence attempts remain preserved as numerical blocks:

```text
COMPLETE_QSPEC_FINITE_HOLONOMY_RESPONSE_NUMERICAL_BLOCK_V001.md
COMPLETE_QSPEC_FINITE_HOLONOMY_RESPONSE_NUMERICAL_BLOCK_V002.md
```

Neither failure was erased by a tolerance change. The only successor change
was the preregistered RK4 resolution increase to `1600/3200` time steps.

Primary v003 artifacts:

```text
ec91dd9c2a283aa2306bebd92b275e4a6e680c0dd05164fb9d305fd6451bec43  scripts/derive_complete_qspec_finite_holonomy_response_v003.py
49deb24656a3655f59b429c8590566da296d7d4d18fca7e6f15cf1937abf28db  stage8_execution/work/QSPEC_finite_holonomy_response_v003.json
```

Independent-verifier artifacts:

```text
f5302ee851bc8c76e4abf91ca7fdbddaca9569202b556db4ef59f0235c592ebe  COMPLETE_QSPEC_FINITE_HOLONOMY_INDEPENDENT_VERIFIER_PROTOCOL_V001.md
7eea0931a6b8d062e111a7eecfd2d1727e69e44d7917317c26891f9b85446648  scripts/verify_complete_qspec_finite_holonomy_response_v001.py
f4a96ade58da7224d5bb77c2fa0de90bb315090fff77e42542712b04264d8af3  stage8_execution/work/QSPEC_finite_holonomy_response_verification_v001.json
```

## Primary computation

The primary calculation used:

```text
frozen three-site periodic source regulator;
uniform-link representative U=exp(i theta/3);
two-cell complete source-record parent;
complete final source-record identity;
split-exponential finite evolution for the CTP and FS responses;
independently integrated Duhamel tangent at 1600 and 3200 steps.
```

The Duhamel results were:

```text
N=1600: g_Duhamel = 0.06481888682485776
        state norm error = 1.3798406861553758e-11

N=3200: g_Duhamel = 0.06481888687124183
        state norm error = 4.305444889496357e-13
```

The certified primary intervals were:

```text
H_CTP:
  [0.0648119115562134, 0.06485648035527754]

g_FS:
  [0.06479796016495462, 0.06481889473271849]

g_Duhamel:
  [0.06481887685578047, 0.0648188968867032]
```

All three intervals are positive and mutually overlap.

## Independent computation

The independent verifier did not import the primary script. It used:

```text
integer bit-mask CAR creation/annihilation parity;
direct unsplit RK4 integration of the full source-record equation;
N=800/1600 time-step extrapolation;
h=1/80 and 1/160 centered holonomy differences;
time and holonomy Richardson extrapolation;
no tangent-evolution routine from the primary calculation.
```

Its extrapolated values and intervals were:

```text
H_CTP = 0.06481700348995766
interval:
  [0.06481252286132844, 0.06482148411858688]

g_FS = 0.06481888686785846
interval:
  [0.06481844080411259, 0.06481933293160433]
```

The independent intervals are positive, overlap each other, and overlap the
primary Duhamel interval.

## Structural checks

The following checks passed:

```text
active one-particle dimension = 8
occupied rank = 4
four-particle Fock dimension = 70
record dimension = 9
connection anti-Hermiticity error = 0
Wilson-loop error = 0
maximum finite-component Hermiticity error < 1e-15
maximum independent state-norm error < 4.42e-10
regulator-subspace leakage < 2e-15
complete final identity retained
no record outcome postselected
no final source state postselected
no determinant inserted
```

## Scope ceiling

This result establishes:

```text
the complete-Qspec scalar closure carries nonzero finite global holonomy;
the CTP Hessian, finite-difference FS metric, and Duhamel response agree;
the positive response is reproduced by an independent numerical route.
```

It does not establish:

```text
a local transverse or plaquette Maxwell response;
continuum or regulator independence;
packing independence;
a volume-uniform zero-free neighborhood;
a connected linked-cluster density;
the intensive Duhamel-Hessian theorem;
kappa_record;
the physical Thomson stiffness;
alpha;
or proof authorization.
```

## Protected status

```text
complete_Qspec_CTP_scalar_closure_derived = true
finite_Qspec_holonomy_response_diagnostic_passed = true
interacting_continuum_CTP_amplitude_derived = false
local_Maxwell_response_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
Duhamel_intensive_Hessian_equality_proved = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
