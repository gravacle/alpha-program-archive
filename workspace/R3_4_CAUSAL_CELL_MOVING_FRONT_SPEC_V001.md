# R3.4 Causal-Cell Moving-Front Specification v001

Date: 2026-07-24

## Purpose

Determine whether finite causal-cell support and the derived charged
incidence endpoint map produce a durable public outgoing-record sector
without selecting a pulse profile, spectral density, or topology.

This gate concerns the pure charged public-record sector. It does not claim
full Parent-State Covariance for source, gauge, gravity, or environment
observables.

## Frozen branch

Use any locally finite future-directed acyclic exhaustion of distinct
physical record cells. Each cell `j` has one interaction support interval
`I_j` and one record factor `R_j`.

The charged incidence generator on that cell is:

```text
B_j=P_ch tensor gamma^5 tensor c_partial,j.
```

Its time-dependent coefficient `v_j(t)` must satisfy:

```text
support(v_j) subset I_j;
integral v_j(t) dt=tau_R=pi/sqrt(2).
```

No shape of `v_j` is selected. The gate must test multiple inequivalent
profiles and prove profile independence analytically from the fixed
generator.

## Required derivations

1. For every admissible profile:

   ```text
   T exp[-i integral v_j(t) B_j dt]
     =exp(-i tau_R B_j).
   ```

2. For distinct cells, prove:

   ```text
   [B_j,B_k]=0.
   ```

   Hence overlapping spacelike supports and different causal linear
   extensions give the same completed public map.
3. On the public algebra of the first `N` completed record cells, every later
   pulse must act trivially at all intermediate times.
4. The completed finite states must be restriction-compatible and define a
   charge-superselected quasi-local state.
5. The pointer averages must form a central sequence distinguishing neutral
   and charged outgoing sectors.
6. For every fixed local public-record observable, the moving-front dynamics
   must eventually stabilize it. The induced asymptotic public derivation is
   then zero, its automorphism group is strongly continuous, and its point
   spectrum is explicitly inventoried rather than hidden.
7. Contrast the result with the rejected stationary-all-cells evolution,
   which acts forever on completed factors and is not this moving-front
   parent.

## Authority and scope gate

The mathematical result is promoted to a live parent-derived public-sector
result only if the active principles already bind:

```text
each primitive interaction to one finite causal cell;
distinct future cells to distinct record factors;
and physical exhaustion to future cell addition rather than repeated action
on a completed cell.
```

If those bindings remain only part of the Causal Direct-Limit Record
Hypothesis, the output remains conditional on that hypothesis.

## Verdicts

```text
MOVING_FRONT_PUBLIC_RECORD_DYNAMICS_DERIVED
MOVING_FRONT_PUBLIC_RECORD_DYNAMICS_CONDITIONAL
MOVING_FRONT_PUBLIC_RECORD_DYNAMICS_BLOCKED
```

## Fixed statuses

```text
full_parent_state_covariance_derived = false
complete_parent_action_derived = false
physical_response_spectral_measure_derived = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
