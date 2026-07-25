# Complete-Qspec Temporal-Plaquette Response Result v001

Date: 2026-07-25

## Verdicts

```text
FINITE_TEMPORAL_PLAQUETTE_RESPONSE_PRESENT
INDEPENDENT_TEMPORAL_PLAQUETTE_RESPONSE_CONFIRMED
FINITE_TEMPORAL_RESPONSE_NONLOCAL_OR_INHOMOGENEOUS
```

The already frozen two-cell complete-Qspec parent has a strictly positive
response to connection histories whose initial and final Wilson-loop
holonomies are both the identity. The response is therefore not merely an
overlap between different endpoint holonomies.

The finite response is not proportional to the local derivative norm. This
two-cell object has not earned a local Maxwell coefficient and its numerical
response may not be called `kappa_record`, a Thomson stiffness, or alpha.

## Sealed artifacts

Primary:

```text
632aa96ab2b3e5c77d329e4a2f1bbef4eda50e7d6e7b2211a06a0ae372c27909  COMPLETE_QSPEC_TEMPORAL_PLAQUETTE_RESPONSE_DIAGNOSTIC_SPEC_V001.md
c29a7456a6cfb965662678ddee1ee82360d790bab444d38a96c8952496f31e94  scripts/derive_complete_qspec_temporal_plaquette_response_v001.py
0db640eeb1fd5274b89c004791e0f7b9f9c437a70b4ee831316aaea5071b5c6e  stage8_execution/work/QSPEC_temporal_plaquette_response_v001.json
```

Independent:

```text
d5ca397a4ced62840a0934d0c9641c7c5f66e9701d35c75a8400a44f20b9a95a  COMPLETE_QSPEC_TEMPORAL_PLAQUETTE_INDEPENDENT_VERIFIER_PROTOCOL_V001.md
76bc1d19c59f1bc8fe29e3a0eaac34e8de0b2afed921b317fca3e2e14be07fc7  scripts/verify_complete_qspec_temporal_plaquette_response_v001.py
7eb2175203263765ad9f4b15b4e54778e9e19c45e34ef0c29a5d611a33be2afb  stage8_execution/work/QSPEC_temporal_plaquette_response_verification_v001.json
```

## What was varied

On total duration `0 <= t <= 2`, the three profiles were:

```text
f_n(t)=sin(n pi t/2)/(n pi/2), n=1,2,3.
```

They obey:

```text
f_n(0)=f_n(2)=0;
integral dot(f_n) dot(f_m) dt=delta_nm.
```

For each profile and each pairwise sum, the uniform link connection was:

```text
U_(j,j+1)(t)=exp[i a f(t)/3].
```

Thus the total loop holonomy returned to the identity at the end while the
interior history carried nonzero `F_0x` proportional to `dot(f)`.

## Positive temporal-curvature result

The primary response matrix was:

```text
[[ 0.0141087775271990, -0.0025745206416017, -0.0004510333883955],
 [-0.0025745206416017,  0.0009197147051080, -0.0000275681184769],
 [-0.0004510333883955, -0.0000275681184769,  0.0003161656631048]]
```

Its center eigenvalues were:

```text
0.0002400870325792
0.0004976251906886
0.0146069456721441
```

After the preregistered radius-matrix correction, the certified minimum
response eigenvalue remained positive:

```text
0.0002266831024104.
```

The independent verifier used an integer-bitmask CAR lift and unitary
midpoint Strang splitting instead of the primary tuple CAR lift and direct
RK4. It found:

```text
certified minimum response eigenvalue =
0.0002402659981777.
```

All corresponding primary and independent intervals overlap.

## Why local Maxwell form failed

Because the profile derivatives are orthonormal, a time-local
constant-coefficient electric response would produce:

```text
M = kappa I.
```

It did not.

The independently verified diagonal intervals were:

```text
f1: [0.0141105345068396, 0.0141111250389386]
f2: [0.0009217040300253, 0.0009218303227882]
f3: [0.0003181521916264, 0.0003182839427072]
```

They have no common intersection. The independently verified off-diagonal
intervals were:

```text
f1,f2: [-0.0025758858743389, -0.0025752078051707]
f1,f3: [-0.0004523668271358, -0.0004517525637093]
f2,f3: [-0.0000286897107020, -0.0000284992817240]
```

None contains zero.

The finite parent therefore has a positive, frequency-dependent response
kernel with cross-profile correlations. This is a nonlocal or temporally
inhomogeneous susceptibility, not yet a local Maxwell coefficient.

## Consequence for the proof path

The next admissible step is not to select one diagonal entry or average the
matrix. It is to derive the connected translation-invariant many-cell limit
and test whether:

```text
the response kernel becomes local at long wavelength;
the normalized low-frequency diagonals converge to one value;
cross-frequency terms vanish;
the intensive result is independent of cellulation and packing.
```

Only after that temporal locality gate passes is it meaningful to combine
the result with a spatial magnetic plaquette response and run the full
Maxwell tensor/Hodge-duality test.

## Scope and protected status

```text
complete_Qspec_CTP_scalar_closure_derived = true
finite_Qspec_holonomy_response_diagnostic_passed = true
finite_temporal_plaquette_response_computed = true
finite_temporal_local_Maxwell_form_supported = false
local_Maxwell_response_derived = false
interacting_continuum_CTP_amplitude_derived = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
