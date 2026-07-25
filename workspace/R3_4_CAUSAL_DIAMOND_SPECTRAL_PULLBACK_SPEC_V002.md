# R3.4 Causal-Diamond Spectral Pullback Specification v002

## Purpose

This specification supersedes v001 as the audit authority. Version 001
correctly computed a conditional scalar transform but had three audit defects:

1. it did not distinguish a bounded graph-incidence limit from an unbounded
   positive-energy continuum generator;
2. it encoded analytic regularity conclusions as booleans instead of
   checking their hypotheses; and
3. its provenance parser could pass when an expected negative status merely
   disappeared.

Version 002 preserves the conditional calculation and closes those audit
defects. It does not assume that the candidate is the physical root spectral
measure.

No measured coupling, mass, endpoint, cosmological value, or alpha may enter.

## Hash-pinned authorities

The evaluator must verify every file and exact status fact in
`R3_4_CAUSAL_DIAMOND_SPECTRAL_PULLBACK_PROVENANCE_V002.json`. A missing file,
hash mismatch, missing status key, duplicate status key, or changed expected
value is a hard failure. Absence of a negative statement is never evidence
for a positive statement.

## Layer M: conditional mathematical calculation

For the unit-tip-separation flat causal diamond,

```text
D={x: -1/2 <= t <= 1/2, |x_spatial| <= 1/2-|t|},
Vol(D)=pi/24,
d mu_D=d^4x/Vol(D).
```

Under the explicitly conditional scalar convention

```text
positive shell E=|k|;
radial Hilbert weight E^2 dE;
constant diamond smearing;
```

the evaluator must independently compute:

1. the full four-dimensional null-shell Fourier transform;
2. its agreement with direct quadrature over the shrinking spatial balls;
3. the normalization of `E^2 |F_D(E)|^2`;
4. positivity and the threshold Taylor expansion;
5. integrability and absolute continuity;
6. the boundary terms and derivative hypotheses needed for the decay law;
7. the return-amplitude and return-probability asymptotic classes.

The evaluator may use the standard identity

```text
integral_0^infinity J_nu(x)^2 dx/x = 1/(2 nu), nu>0,
```

provided the reduction to that identity is displayed.

## Layer P: physical provenance

Layer M is not a physical spectral derivation unless the corpus supplies:

1. a refinement/scaling map from finite BID cochains to the continuum
   outgoing field;
2. strong-resolvent convergence to the unbounded continuum generator, or an
   independently derived continuum parent;
3. its self-adjoint outgoing-sector domain;
4. the positive-energy projector and radial spectral measure, including
   multiplicities;
5. a derived map from the finite BID root or quasi-local state to the
   continuum one-particle Hilbert space;
6. an actual computation of `<r,P(dE)r>` from that operator;
7. exclusion of gapped, point-spectrum, and inequivalent preparation
   sectors; and
8. identification of the selected sector as the carrier of recoverable
   durability.

The existing bounded-incidence direct-limit theorem may not be used as a
theorem about an unbounded `E=|k|` generator.

## Regulator statement

The three discrete regulators have return **probability** class `t^-3`. The
sealed covariant representative has probability class `t^-6`. The conditional
diamond density must be compared to those exact classes. No common decay
class may be asserted unless it is actually reproduced.

## Sealed outcomes

```text
all Layer-M checks pass and all Layer-P obligations are derived:
  DERIVED_COVARIANT_ROOT_SPECTRAL_MEASURE

all Layer-M checks pass but any Layer-P obligation remains open:
  CONDITIONAL_SCALAR_DIAMOND_DENSITY_ONLY

any Layer-M check fails:
  SCALAR_DIAMOND_CALCULATION_FAILED
```

Regardless of outcome:

```text
hypothesis_promoted_to_principle = false
spectral_evaluation_authorized = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```

