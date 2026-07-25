# Stage-8 T7 Parent-State Regulator Restriction Spec v001

Date: 2026-07-24

## Status

```text
SPECIFICATION_SEALED_BEFORE_EXECUTION
```

This gate attempts to derive a finite-regulator incoming state from the
already-disclosed continuum stationary quasifree state. It adopts no
zero-mode filling, finite-volume vacuum, thermal parameter, final source
state, or coupling target.

## Hash-pinned authorities

```text
532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb  PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md
6f6b822ac8ccf9ea19659f4ccf811268f60a27a361f817ee6513479d63b62546  BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001.md
5026afb89b52ead9f309168cb2fa4f06b81039f8dd01b8940f40e64aad679a7e  STAGE7_QSPEC_REVIEW_CANDIDATE_V002.md
40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9  R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md
7aafba8667ac01f1c4326b0d714e838bf068eec7c8f4ce28ef03c8bef9d62098  STAGE8_T7_ACTUAL_PARENT_RECORD_AMPLITUDE_ADJUDICATION_RESULT_V001.md
322510075e1f8f6616eb47b1325f47963d90e8adaf20e83f7209c8be5f048b40  stage8_execution/t7_actual_parent_record_amplitude/T07_ACTUAL_PARENT_RECORD_AMPLITUDE_V001.seal.sha256
0fe3905aa14ed744bda883dd68aa799dc9bb90f4f5647b477be3f6de65330f57  BID_FULL_DIRAC_CAR_SOURCE_TYPING_DERIVATION_V001.md
```

## S1 - Continuum covariance

On the disclosed stationary source space, let

```text
C=1_(-infinity,0)(h_0).
```

For the massless flat source, the set `p=0` has Lebesgue measure zero.
Changing the representative of `C(p)` at that one point does not change the
bounded multiplication operator on `L2(R^3;C^4)`. The continuum quasifree
state is therefore unambiguous without a zero-mode filling convention.

## S2 - Covariant finite restrictions

Choose a nested finite-rank spectral Galerkin exhaustion `Q_n` such that:

```text
Q_n Q_(n+1)=Q_n;
[Q_n,h_0]=0;
[Q_n,C]=0;
the momentum cohort is closed under p -> -p and charge conjugation;
and union_n im(Q_n) is dense in the continuum one-particle space.
```

Define:

```text
C_n=Q_n C Q_n.
```

Then `0<=C_n<=I`, and for `m>=n`:

```text
Q_n C_m Q_n=C_n.
```

The finite quasifree state is the CAR restriction determined by `C_n`.
It is inherited from the continuum state rather than selected from the
spectrum of a later finite toy Hamiltonian.

## S3 - Same-parent interaction

Project every component of the same finite parent with the same `Q_n`:

```text
h_(K,n)(t)=Q_n h_K(t) Q_n;
H_(K,n)(t)=dGamma_R(h_(K,n)(t)).
```

The incoming state and the finite interaction therefore live on the same
finite CAR carrier. The state need not be stationary under the interacting
parent; it is the stationary incoming state of `h_0`.

The old three-site periodic regression remains a valid operator regression
but is not a state regulator, because its four exact zero modes were not
inherited from a specified continuum restriction.

## S4 - Executable regression

Using two nested, target-free nonzero-momentum cohorts, verify:

```text
h_0(p)^2=|p|^2 I;
C_n^2=C_n=C_n^dagger;
rank(C_n)=half the finite source dimension;
Q_n C_m Q_n=C_n;
no finite zero eigenvalue is introduced;
and the corresponding finite pure quasifree density has unit trace and
one-particle covariance C_n.
```

The sampled cohorts are regressions of the general spectral-restriction
argument, not a preferred physical cutoff.

## Verdicts

```text
PARENT_STATE_REGULATOR_RESTRICTION_DERIVED
```

requires S1-S4.

```text
PARENT_STATE_REGULATOR_RESTRICTION_BLOCKED
```

is required if a finite zero-mode filling, thermal weight, boundary state,
or regulator-dependent state choice remains.

Passing this gate does not derive the completed-record Fock amplitude,
one-handle factorization, a thermodynamic determinant, or any coupling.

## Fixed status

```text
parent_state_regulator_restriction_derived = false
finite_actual_parent_record_amplitude_derived = false
connected_primitive_amplitude_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
