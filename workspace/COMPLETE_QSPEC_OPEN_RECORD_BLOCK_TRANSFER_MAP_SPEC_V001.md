# Complete-Qspec Open-Record Block Transfer-Map Specification v001

Date: 2026-07-25

## Purpose

Extend the exact sequential transfer theorem to finite causal schedules with
overlapping open record incidences. This is required before connected
cellulations may be represented without a hidden Markov approximation.

No response value, coupling target, alpha value, or measured constant may
enter.

## Event state

At event boundary `e`, let `A_e` be the ordered set of records that have
opened and have not passed their last incident unitary. Propagate a
cross-history operator:

```text
X_e on H_source tensor (tensor_(r in A_e) H_r).
```

Allowed exact event operations are:

```text
OPEN(B):
  X -> X tensor (tensor_(r in B) |ready_r><ready_r|);

EVOLVE(U_e^plus,U_e^minus):
  X -> U_e^plus X U_e^- dagger;

CLOSE(C):
  X -> Tr_C X,
```

where `C` may contain a record only after its last incident evolution.

## Liveness rule

For every record `r`, compute:

```text
last(r) = maximum event index whose unitary support contains r.
```

Closing `r` before `last(r)` is invalid and must be rejected before
execution. Closing at or after `last(r)` is exact because all later
unitaries act as identity on `H_r`.

## Theorem obligation

Freeze an explicit induction proving that the event-driven block operator
equals the partial trace of the full global relative-history operator at
every valid event boundary. The proof must include:

```text
open step;
evolution step;
valid close step;
reduction to the one-record sequential theorem;
invalid early-close exclusion.
```

## Regression

Use a target-free generic schedule with:

```text
source dimension       3
record dimensions      2 and 2
U_1 support            {source,R1}
U_12 support           {source,R1,R2}
U_2 support            {source,R2}
```

Use independent plus/minus random unitaries and distinct source ket/bra
vectors. Compare the final source cross-operator from:

1. full `source x R1 x R2` branch-state evolution;
2. event-driven cross-operator evolution that closes `R1` after `U_12` and
   closes `R2` after `U_2`.

Require relative Frobenius disagreement below `1e-12`.

The predeclared schedule that closes `R1` immediately after `U_1` must be
rejected by the liveness validator.

## Verdict

Return:

```text
COMPLETE_QSPEC_OPEN_RECORD_BLOCK_TRANSFER_MAP_DERIVED
```

only if the proof and regression pass. Otherwise return:

```text
COMPLETE_QSPEC_OPEN_RECORD_BLOCK_TRANSFER_MAP_BLOCKED
```

## Scope ceiling

A pass supplies the exact finite-width representation. It does not prove a
uniform bound on open width, a linked-cluster density, a zero-free
neighborhood, Maxwell form, kappa_record, alpha, or proof authorization.

## Fixed status

```text
sequential_relative_history_transfer_map_derived = true
concurrent_open_record_block_map_derived = false
connected_K_cell_amplitude_constructed = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
local_Maxwell_response_derived = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
