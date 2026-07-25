# Complete-Qspec Finite-Holonomy Independent Verifier Protocol v001

Date: 2026-07-25

## Status and purpose

This protocol is written after the primary v003 diagnostic completed and
before the independent verifier is executed. It is therefore a verification
protocol, not a target-blind prediction.

The verifier must independently reconstruct the frozen finite model and test
whether a direct integration route confirms the nonzero global-holonomy
response. It must not import the primary derivation script or reuse its
functions.

## Frozen primary artifacts

```text
ec91dd9c2a283aa2306bebd92b275e4a6e680c0dd05164fb9d305fd6451bec43  scripts/derive_complete_qspec_finite_holonomy_response_v003.py
49deb24656a3655f59b429c8590566da296d7d4d18fca7e6f15cf1937abf28db  stage8_execution/work/QSPEC_finite_holonomy_response_v003.json
```

The verifier may read the primary JSON only to check its sealed hash, scope
flags, and certified intervals. It may not call or import the primary script.

## Independent reconstruction

1. Reconstruct the Dirac and three-site covariant-derivative data directly.
2. Construct the four-particle CAR lift with integer bit masks and explicit
   creation/annihilation parity. Do not use the primary tuple-deletion lift.
3. Reconstruct the same frozen active subspace, incoming Slater state,
   two intrinsic interactions, record quadratures, and total Wilson-loop
   coordinate required by the sealed diagnostic specification.
4. Integrate the full source-record differential equation directly with a
   separately implemented classical RK4 method. Do not use the primary
   split-exponential pulse or its tangent integrator.

## Frozen numerical grid

Use:

```text
time steps: N = 800 and 1600 per pulse
holonomy steps: h = 1/80 and 1/160
branches: theta = 0, +h, -h
```

For each `(N,h)`, compute:

```text
Z_+(h)=<Psi_0|Psi_+h>
Z_-(h)=<Psi_0|Psi_-h>
H_CTP(N,h)=(-log|Z_+|-log|Z_-|)/h^2
g_FS(N,h)=<d_h Psi|d_h Psi>-|<Psi_0|d_h Psi>|^2
d_h Psi=(Psi_+h-Psi_-h)/(2h)
```

First Richardson-extrapolate each response in time using fourth-order RK4:

```text
R_inf(h)=R_1600(h)+(R_1600(h)-R_800(h))/15.
```

Then extrapolate the central holonomy difference:

```text
R_0=(4 R_inf(1/160)-R_inf(1/80))/3.
```

The independent uncertainty radius is the sum of the absolute time and
holonomy extrapolation corrections plus `1e-8`. No response value is used to
choose this radius.

## Pass conditions

The verifier passes only if all of the following hold:

1. Every frozen authority hash matches.
2. The reconstructed active dimension is 8, occupied rank is 4, Fock
   dimension is 70, and record dimension is 9.
3. The covariant derivative is anti-Hermitian, the Wilson-loop product is
   `exp(i theta)`, and all finite Hamiltonian components are Hermitian to
   `1e-12`.
4. Every directly integrated state has norm error below `2e-9`.
5. The independently extrapolated `H_CTP` and `g_FS` intervals are strictly
   positive and overlap one another.
6. Each independent interval overlaps the primary v003 Duhamel interval.
7. The primary v003 CTP, FS, and Duhamel intervals remain mutually
   overlapping and strictly positive.
8. The complete final identity is retained, no record outcome or final
   source state is postselected, and no determinant is inserted.
9. Every protected coupling and proof flag remains false.

## Verdict and scope

A pass returns:

```text
INDEPENDENT_FINITE_QSPEC_HOLONOMY_RESPONSE_CONFIRMED
```

A failure returns:

```text
INDEPENDENT_FINITE_QSPEC_HOLONOMY_RESPONSE_BLOCKED
```

Even a pass establishes only a finite global-holonomy response in the
complete-Qspec scalar closure. It does not establish a local Maxwell
response, continuum or packing independence, a linked-cluster density,
`kappa_record`, a Thomson-limit stiffness, alpha, or proof authorization.
