# Stage-8 T7 Intrinsic-Measure Support-Projection Normalization Spec v001

Date: 2026-07-24

## Purpose

Determine whether the sealed causal parent combines the intrinsic time
marginal and spatial support projector with the unique unit-incidence
normalization required by the allow/require boundary.

This specification is sealed before the successor calculation. It uses no
response value, coupling, alpha, endpoint, or measured constant.

## Pinned authorities

```text
e4cfaef14309b3acf5674f8c8faee756f744fec4691d5e01d9de0fa422592be2  R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md
40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9  R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md
b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30  CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md
```

The superseded scalar-density interpretation is retained in:

```text
STAGE8_T7_INTRINSIC_MEASURE_PARENT_NORMALIZATION_SCOPE_CORRECTION_V001.md
```

## Operator semantics

For the unit-duration causal diamond:

```text
w(t)=32 min(t,1-t)^3,
integral_0^1 w(t)dt=1,
M(t)=multiplication by 1_(B_t).
```

For every normalized source state `psi(t)`:

```text
p_psi(t)=<psi(t),M(t)psi(t)>.
```

Because `M(t)` is an orthogonal projection:

```text
0<=p_psi(t)<=1.
```

The accumulated incidence fraction is

```text
f_support[psi]=integral_0^1 w(t)p_psi(t)dt.
```

The physical action coordinate supplied to the unit incidence is

```text
tau_eff[psi]=tau_R f_support[psi].
```

## Required theorem

Prove:

1. `0<=f_support<=1` for every normalized state history;
2. `f_support=1` iff `p_psi(t)=1` for `w(t)dt`-almost every `t`;
3. therefore full support accumulates exactly `tau_R`, while every
   positive-measure support deficit accumulates strictly less;
4. multiplying `M(t)` by an additional scalar changes the unit-incidence
   spectrum and is not an equivalent representation;
5. the candidate `M(t)/V_3(t)` is nonprojective, dimensionful, and unbounded
   at the tips, so it cannot replace the sealed support projector;
6. the earlier scalar-density integral uses an unnormalized test function
   and does not evaluate the parent on a normalized source state.

This is the operator form of the allow/require boundary: geometry supplies a
probability schedule, while source support supplies an occupancy fraction.

## Predeclared verdicts

```text
SUPPORT_PROJECTION_NORMALIZATION_DERIVED
  iff all six statements follow without a new normalization.

SUPPORT_PROJECTION_NORMALIZATION_BLOCKED
  if an additional scalar or slice-volume normalization is required.
```

## Scope

Passing this theorem validates the parent normalization only. It does not
prove that a finite-energy state attains full support, prove sharp-cell Fock
implementability, establish a continuum determinant, or compute a response.

```text
support_projection_normalization_derived = false
finite_energy_full_support_state_derived = false
sharp_cell_implementability_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
