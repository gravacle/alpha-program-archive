# Complete-Qspec Periodic Zero-Free Promotion Spec v001

Date: 2026-07-25

## Purpose

Decide whether the accepted exact-dyadic `R0` certificate closes the frozen
periodic zero-free theorem and its thermodynamic logarithm. This is a fresh
composition gate, not a status edit.

It must recompute every remaining verdict-bearing scalar inequality with
outward-rounded Arb arithmetic. It may not inherit the original
round-to-nearest Decimal booleans.

## Frozen authorities

```text
54c972914b180d694517ed7598ac3344fd4dde3aa953d139a7a1572ddb281690  COMPLETE_QSPEC_PERIODIC_UNIFORM_ZERO_FREE_THEOREM_SPEC_V001.md
048d18a2ac666639a44ec0d52b584a412ece9fdeb90837abffa86e831fc652e0  stage8_execution/work/QSPEC_periodic_uniform_zero_free_theorem_v001.json
8d2ab3a0102cb4e8ba7ab925773e1a6fd08b763202859688b14ea4cd12f39650  COMPLETE_QSPEC_PERIODIC_UNIFORM_ZERO_FREE_THEOREM_REVIEW_CORRECTION_V001.md
ada56f525f4a5a9708545e29e62e7e5f0e2dd762d37f168429284194c7babd95  COMPLETE_QSPEC_ZERO_TRANSFER_DYADIC_BALL_CERTIFICATE_SPEC_V001.md
26e76a3f3625bdcddf3324bde28b94dd58f75454a8edbcacc5872c43356db015  scripts/certify_complete_qspec_zero_transfer_dyadic_v001.py
93a37fb83fe9b7264808a80b2f7bffb487af642180affb6918c5b98b65dbb74b  stage8_execution/work/QSPEC_zero_transfer_dyadic_ball_certificate_v001.json
2c193f34786c2eeff57a6ea611116448926076d676fd177b5f9c73980ec6496a  COMPLETE_QSPEC_ZERO_TRANSFER_DYADIC_BALL_CERTIFICATE_RESULT_V001.md
1cd9528bc6872a3a28df828a452a165f8672cccc455a64323edab9e0905bf69d  scripts/verify_complete_qspec_periodic_analytic_continuation_v003.py
```

The exact emitted objects are identified by:

```text
transfer       69d6a95de251be3e3aa83d7344c7961b2023f41416399b760d3096fcde83718b
trace column   07506154f602a1fa17e32c81f4bc377e547868eb4bf540ed11248949afea0876
start vector   510205f86d4b068828d0a2ca0bfa4d6e43c62f44c555b7a627d25b20e0d4e4c7
```

Any mismatch aborts execution.

## P1: anchor data

Use the orthogonal trace anchor

```text
P = |t><t| / <t|t>,
Q = I-P,
R = Q T0 Q,
A = P+R.
```

Import only the proved bounds:

```text
||R||_2 < 0.812,
||T0-A||_2 < 1e-10.
```

Certify with exact dyadic balls:

```text
||trace||_2,
||start||_2,
trace * start,
|trace * start - 1|.
```

Because `trace Q=0`, the anchor amplitude is exactly
`trace A^N start = trace start` for every `N>=1`.

## P2: analytic transfer perturbation

For `|z|<=1/500`, recompute at no less than 192-bit Arb precision:

```text
L_free = (2/3) [1 + (2R/3) exp(R/3)],
delta_free = L_free R,
epsilon = 3 [exp(2 delta_free)-1],
eta = epsilon + 1e-10.
```

Here `eta` bounds `||T(z)-A||_2`. No sampled transfer norm may carry this
step.

## P3: invariant graph

With

```text
r = 0.812,
X = 1/20,
```

prove by outward-rounded interval bounds:

```text
separation = 1 - eta - eta X - (r+eta) > 0,
eta/separation < X,
(eta/separation)^2 < 1.
```

Then compute:

```text
lambda_min = 1-eta(1+X),
B_max = r+eta+eta X,
projector_delta = (2X+2X^2)/(1-X^2),
kappa_S = (1+X)/(1-X).
```

## P4: coefficient and finite volumes

Prove

```text
coefficient_min =
  |trace start|
  - ||trace|| ||start|| projector_delta
  > 0.
```

For each `1<=N<=6`, require:

```text
|trace start-1|
+ ||trace|| ||start|| N eta (1+eta)^(N-1)
< 1.
```

## P5: all larger volumes

Define

```text
q = B_max/lambda_min,
prefactor =
  ||trace|| ||start|| kappa_S / coefficient_min.
```

Require:

```text
q < 1,
prefactor q^7 < 1.
```

This proves nonzero amplitude for every integer `N>=1` throughout the
closed disk and gives the uniform periodic thermodynamic logarithm
`Log lambda(z)`.

## Pass rule and scope

Only if P1-P5 all pass, return:

```text
FROZEN_DYADIC_PERIODIC_ZERO_FREE_AND_LOG_DENSITY_PROVED
```

and set:

```text
frozen_dyadic_periodic_zero_free_neighborhood_proved = true
frozen_dyadic_periodic_thermodynamic_log_density_proved = true
```

Even on pass:

```text
continuous_time_parent_zero_free_proved = false
periodic_connected_linked_cluster_density_proved = false
all_stage8_regulators_zero_free_proved = false
all_connected_cellulations_linked_cluster_proved = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
