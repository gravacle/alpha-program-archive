# Complete-Qspec Temporal-Plaquette Independent Verifier Protocol v001

Date: 2026-07-25

## Role

This is a post-primary independent-verification protocol. It does not claim
target blindness. Its purpose is to test whether a different CAR
construction and a different unitary evolution algorithm reproduce both:

```text
the strictly positive endpoint-trivial temporal-curvature response;
the failure of the finite response matrix to have constant local-Maxwell form.
```

The verifier must not import the primary derivation script.

## Frozen primary artifacts

```text
c29a7456a6cfb965662678ddee1ee82360d790bab444d38a96c8952496f31e94  scripts/derive_complete_qspec_temporal_plaquette_response_v001.py
0db640eeb1fd5274b89c004791e0f7b9f9c437a70b4ee831316aaea5071b5c6e  stage8_execution/work/QSPEC_temporal_plaquette_response_v001.json
632aa96ab2b3e5c77d329e4a2f1bbef4eda50e7d6e7b2211a06a0ae372c27909  COMPLETE_QSPEC_TEMPORAL_PLAQUETTE_RESPONSE_DIAGNOSTIC_SPEC_V001.md
```

## Independent construction

1. Reconstruct the fixed-particle CAR lift using integer occupation masks and
   explicit parity counts.
2. Reconstruct the same sealed finite parent and six endpoint-trivial
   profiles directly from the specification.
3. Replace the primary direct RK4 evolution with midpoint Strang splitting:
   exact free half-step, exact interaction step, exact free half-step.
4. Simultaneously diagonalize the commuting free cosine/sine generators once;
   only their time-dependent phases may vary during evolution.
5. Diagonalize each source interaction and record quadrature independently
   and apply the exact interaction exponential.

## Frozen numerical grid

Use:

```text
Strang steps per cell: N = 400 and 800
amplitudes: a = 1/80 and 1/160
all six profiles and both signs
```

Use second-order time Richardson extrapolation:

```text
H_inf(a)=H_800(a)+(H_800(a)-H_400(a))/3.
```

Use the same centered-amplitude extrapolation as the primary:

```text
H(0)=[4 H_inf(1/160)-H_inf(1/80)]/3.
```

The uncertainty radius is the maximum absolute time correction plus the
absolute amplitude correction plus `1e-8`.

## Pass rule

Pass only if:

1. all authority hashes match;
2. the independent dimensions, Hermiticity, profile endpoints, and endpoint
   loop identities pass;
3. every independently evolved state has norm error below `2e-9`;
4. the independent response matrix is certified positive using the same
   Weyl radius bound;
5. every independent diagonal and off-diagonal interval overlaps the
   corresponding primary interval;
6. the independent and primary calculations agree on the local-form
   classification;
7. no postselection, determinant, coupling evaluation, alpha computation, or
   proof authorization is introduced.

Return:

```text
INDEPENDENT_TEMPORAL_PLAQUETTE_RESPONSE_CONFIRMED
```

or:

```text
INDEPENDENT_TEMPORAL_PLAQUETTE_RESPONSE_BLOCKED
```

## Scope

A pass independently confirms a finite endpoint-trivial temporal-curvature
response and its measured finite nonlocal/inhomogeneous response matrix. It
does not establish a spatial plaquette response, local Maxwell theory,
continuum independence, `kappa_record`, the Thomson limit, alpha, or proof
authorization.
