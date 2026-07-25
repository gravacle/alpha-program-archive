# Complete-Qspec Zero-Transfer Dyadic Ball-Certificate Result v001

Date: 2026-07-25

## Sealed authorities

```text
ada56f525f4a5a9708545e29e62e7e5f0e2dd762d37f168429284194c7babd95  COMPLETE_QSPEC_ZERO_TRANSFER_DYADIC_BALL_CERTIFICATE_SPEC_V001.md
26e76a3f3625bdcddf3324bde28b94dd58f75454a8edbcacc5872c43356db015  scripts/certify_complete_qspec_zero_transfer_dyadic_v001.py
93a37fb83fe9b7264808a80b2f7bffb487af642180affb6918c5b98b65dbb74b  stage8_execution/work/QSPEC_zero_transfer_dyadic_ball_certificate_v001.json
```

The exact transfer object is additionally pinned by the canonical
binary64-hex hash

```text
69d6a95de251be3e3aa83d7344c7961b2023f41416399b760d3096fcde83718b
```

## Result

The 192-bit Arb execution returned

```text
FROZEN_DYADIC_ZERO_TRANSFER_R0_CERTIFIED
```

for the exact dyadic `350 x 350` transfer emitted by the frozen 96-slice
reconstruction.

The proof does not use a floating-point singular value as authority. It:

1. converts every binary64 component to its exact dyadic value;
2. constructs the exact rational trace anchor and complement;
3. proves the congruence preconditioner is invertible;
4. proves `0.812^2 I - R^dagger R` positive by interval Gershgorin;
5. applies exact-rational graph and Sylvester bounds; and
6. includes the `|lambda-1| ||P_lambda||` correction required to bound
   `T0-P_lambda`, not merely `T0-lambda P_lambda`.

The decisive certified margins are:

```text
anchor defect upper bound       < 1.598689e-13
Gram Gershgorin lower margin    > 0.9999999999999644
H Gershgorin lower margin       > 7.360680e-4
||T0-P_lambda||_2 upper bound   < 0.812000032580001
required ceiling                  0.813
```

The complete `python-flint` wheel payload was checked against its pinned
`RECORD`: 185 hashed files, including all 33 native shared-library files.
The execution ran in isolated Python mode.

## Hostile review

Two separate post-execution hostile reviews checked the current sealed
specification, source, output, interval margins, graph conversion, runtime
pinning, and scope. Both returned no remaining blocker and accepted only
the exact verdict above.

## Earned scope

```text
validated_frozen_dyadic_R0_enclosure_proved = true
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

This certificate supplies the rigorous `R0` input requested by the
append-only review correction. Any promotion of the periodic zero-free or
thermodynamic-density result must occur in a separate successor that
checks the remaining theorem inputs and preserves the linked-cluster
distinction.
