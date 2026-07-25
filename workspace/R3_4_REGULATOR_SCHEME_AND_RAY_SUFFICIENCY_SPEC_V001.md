# R3.4 Regulator-Scheme and Ray-Sufficiency Specification v001

## Purpose

This target-independent gate tests two proposed inferences:

1. whether the common `t^-3` late-time return-probability class of the
   half-line, radial-tree, and cubic-lattice regulators establishes full
   scheme equivalence; and
2. whether the finite registration-counting covector ray and its quasi-local
   state lift determine the outgoing spectral measure.

No alpha, measured coupling, mass, endpoint, or cosmological value may enter.

## Frozen objects

Use the three already computed regulator amplitudes:

```text
A_half(t)=J_1(2t)/t,
A_tree(t)=A_half(sqrt(3)t),
A_cubic(t)=J_0(2t)^3.
```

Their root measures are represented by:

```text
half-line: endpoint measure of the unit-weight half-line adjacency;
radial tree: the same measure under E -> sqrt(3) E;
cubic lattice: origin measure of the nearest-neighbor adjacency on Z^3.
```

The quasi-local public-record algebra and compatible label states are the
objects already derived in
`CAUSAL_DIRECT_LIMIT_COVECTOR_RAY_LIFT_RESULT_V001.md`.

## Test A: decay-class versus measure equivalence

Compute the exact even root moments through order six for all three
regulators. Compare the scale-invariant standardized moments

```text
m4/m2^2,
m6/m2^3.
```

Two measures can be equivalent under an overall energy rescaling only if
these invariants agree. Common decay exponents alone are insufficient.

Return:

```text
FULL_THREE_REGULATOR_MEASURE_EQUIVALENCE
```

only if all standardized moments agree exactly. Otherwise return:

```text
COMMON_DECAY_CLASS_ONLY
```

and report every inequivalent row.

## Test B: covector-ray sufficiency

The quasi-local algebra and its compatible public-label state determine a
state space. They determine a spectral measure only if they also determine
one self-adjoint generator or one automorphism group.

Use the regulator generators as explicit witnesses. Their countable cell
sets yield isomorphic abstract quasi-local UHF record algebras and the same
product-label-state construction, while their root moments test whether the
spectral measures differ.

If distinct local generators on that same abstract algebraic/state
construction yield inequivalent root measures, return:

```text
OUTGOING_ALGEBRA_DOES_NOT_FIX_DYNAMICS
```

The geometry/locality structure is allowed to distinguish those generators;
that distinction is precisely data that must come from the microscopic
parent action rather than from the covector ray alone.

## Interpretation rule

The common `t^-3` class may be used as evidence of decay-class robustness and
as a regulator crosscheck. It may not be used as evidence that the full
spectral density, absolute response, or coupling normalization is
scheme-independent unless Test A passes.

The quasi-local ray lift may close the outgoing-record-algebra obligation. It
may not close the generator or spectral-measure obligation unless Test B
shows uniqueness.

## Fixed statuses

Regardless of outcome:

```text
hypothesis_promoted_to_principle = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
