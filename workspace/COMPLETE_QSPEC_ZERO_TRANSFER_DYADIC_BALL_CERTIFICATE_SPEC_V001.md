# Complete-Qspec Zero-Transfer Dyadic Ball-Certificate Spec v001

Date: 2026-07-25

## Purpose and exact object

Certify the zero-transfer contraction required by the periodic invariant-
graph theorem using rigorous complex-ball arithmetic.

The exact object in this certificate is the `350 x 350` dyadic matrix whose
entries are the exact IEEE-754 binary64 values emitted by the sealed v003
zero-transfer reconstruction. This is a theorem about the frozen
96-slice numerical regulator. It is not a validated enclosure of the
continuous-time parent.

## Frozen authorities

```text
1cd9528bc6872a3a28df828a452a165f8672cccc455a64323edab9e0905bf69d  scripts/verify_complete_qspec_periodic_analytic_continuation_v003.py
048d18a2ac666639a44ec0d52b584a412ece9fdeb90837abffa86e831fc652e0  stage8_execution/work/QSPEC_periodic_uniform_zero_free_theorem_v001.json
8d2ab3a0102cb4e8ba7ab925773e1a6fd08b763202859688b14ea4cd12f39650  COMPLETE_QSPEC_PERIODIC_UNIFORM_ZERO_FREE_THEOREM_REVIEW_CORRECTION_V001.md
```

Ball runtime:

```text
python-flint 0.6.0
d6b5be0f3a94ff92ad45f8e9d8991ac8face10ab71e362b8b9f25819df4ef06b  python_flint-0.6.0.dist-info/METADATA
9b76e8ba99a8555fa73c855c2459614714f25136238c1c96fa6c82dad5b9cf94  python_flint-0.6.0.dist-info/RECORD
b959e94c11c23633c0cbfea849a07955b8f252fc3100fd2ed52bd3c35118ba93  flint/__init__.py
```

Any mismatch aborts execution.

## D1: exact dyadic conversion

Every real and imaginary binary64 component is converted through
`float.as_integer_ratio()` to an exact Arb rational. Decimal parsing is
forbidden.

## D2: orthogonal anchor

From the normalized exact dyadic trace vector construct

```text
P = |p><p|,  Q=I-P,
A=P+Q T0 Q,
R_bar=Q T0 Q.
```

Require the binary64 diagnostic

```text
||T0-A||_2 < 1e-10.
```

This diagnostic is subsequently enclosed by the zero-anchor perturbation
allowance; it is not set to zero.

## D3: rigorous singular-value bound

Set

```text
c_bar = 0.812,
H = c_bar^2 I - R_bar^dagger R_bar.
```

Use an approximate eigenvector matrix only as a congruence preconditioner.
Convert that matrix to exact dyadic balls and compute

```text
G = V^dagger V,
C = V^dagger H V
```

at 192-bit Arb precision.

Prove by interval Gershgorin bounds:

```text
G positive definite  -> V invertible;
C positive definite  -> H positive definite.
```

Therefore, rigorously:

```text
||R_bar||_2 < 0.812.
```

No NumPy singular value may carry this verdict.

## D4: exact-T0 graph enclosure

Treat `T0=A+(T0-A)` and apply the same invariant-graph lemma with:

```text
r_bar = 0.812,
delta_anchor = 1e-10,
X_anchor = 1e-8.
```

Require the self-map and contraction inequalities and certify that the exact
dyadic `T0` has one leading mode whose complementary block satisfies

```text
r0_certified < 0.813.
```

## Verdict and scope

Return

```text
FROZEN_DYADIC_ZERO_TRANSFER_R0_CERTIFIED
```

only if D1-D4 pass.

Even on pass:

```text
continuous_time_parent_R0_certified = false
periodic_volume_uniform_zero_free_neighborhood_proved = false
periodic_thermodynamic_log_density_proved = false
periodic_connected_linked_cluster_density_proved = false
all_stage8_regulators_zero_free_proved = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```

The periodic zero-free theorem may be promoted only to the same exact
dyadic-regulator scope after this certificate and an independent review
pass.
