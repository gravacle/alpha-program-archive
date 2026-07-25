# Stage-8 T7 Relayed Connected-Preparation Retest Result v001

Date: 2026-07-24

## Verdict

```text
T7_CONNECTED_PREPARATION_BLOCKED_AFTER_RELAY
```

The relay dependency and the five-coordinate residual family are resolved,
but a completed-record compression of the shared-source parent remains an
operator on the source. The relay does not select a scalar source
expectation.

## Exact compressed operator

For exact controlled writes on the three-cell incidence chain:

```text
K_1=P_0;
K_2=P_1P_0;
K_3=P_2P_1P_0.
```

The completed record factors have been removed. What remains is not a
complex number.

## Exact state-expectation table

```text
             rho=P0   rho=P1   rho=P2   rho=I/4
N=1            1        1/4       0        1/4
N=2            1/4      1/4       0        1/16
N=3            0        1/16      0        0
```

Thus the current state-expectation closure is source-state dependent and
has zero baselines on admitted source states. It cannot provide C1's
state-independent nonzero normalization.

The separately reported in/out transition is:

```text
<e_(N-1)|K_N|e_0> = 1, -1/2, 1/4  for N=1,2,3.
```

It remains nonzero, but it is an off-diagonal boundary functional rather
than a state expectation. It was not substituted into this failed gate.

## State-selection status

The sealed authority requires the microscopic parent to supply its state,
but the current ordinary-branch quasifree in-state is disclosed, and a
finite-energy incoming charged excitation is boundary data. The current
parent does not derive one unique physical charged in-state.

Stationarity and charge superselection cannot supply uniqueness by
themselves: on any charged sector of dimension greater than one, distinct
normalized spectral functions of `h_0` commute with both `h_0` and charge.

## Independent verification

The independent verifier reconstructed the result from the exact Gram
matrix:

```text
[[1,   -1/2, 0],
 [-1/2, 1,  -1/2],
 [0,   -1/2, 1]].
```

It reproduced every table entry and in/out amplitude without importing the
construction script:

```text
pass = true
```

## Consequence

This negative result does not reopen the relay or family-resolution gates.
It identifies the remaining typed question:

```text
Should the primitive connected scalar be a full-source state expectation,
or the already-selected linear connection-returned in/out amplitude between
the causal initial and final source lines?
```

The second route is not adopted here. It must be derived from the sealed
linear closure, fixed causal endpoint lines, and source connection before it
can supersede the failed state-expectation C1 formulation.

## Artifact hashes

```text
47fe0d5f6b97899ae17a5ea682222fd0ca48f81c16d4e581219af64f6135f111  STAGE8_T7_RELAYED_CONNECTED_PREPARATION_RETEST_SPEC_V001.md
11f9c36408eff9ebe2ed0886762aea5788880d3872f7e9e7b048646f3e2ee1a1  scripts/derive_stage8_t7_relayed_connected_preparation_retest_v001.py
e2c9299819fbc85a4fbf2b7016d4f34bdfac18be672bb2bb9cfdecbbceb31882  stage8_execution/work/T07_relayed_connected_preparation_retest.json
06eedbef368ef5568e14aecdfa37f54c35498022944b37fa8e43d6d8e8798664  scripts/verify_stage8_t7_relayed_connected_preparation_retest_v001.py
de865b099a2f4cb7eaf28c12e53e5825ad175ccd8c4efabb9f67d4a22d9db9ba  stage8_execution/work/T07_relayed_connected_preparation_retest_verification.json
```

## Fixed status

```text
relay_dependency_resolved = true
relayed_family_resolved = true
connected_preparation_derived = false
all_finite_connected_baselines_nonzero_proved = false
connected_primitive_amplitude_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
