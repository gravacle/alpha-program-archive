# R3.4 Charged-Incidence Outgoing-State Specification v001

Date: 2026-07-24

## Purpose

Test whether the charged controlled incidence operator can replace the
superseded controlled-X write premise and derive a compatible public
outgoing-record state under the Parent-State Covariance Principle.

This is not a complete-parent, response, coupling, or alpha gate.

## Frozen inputs

On the primitive charge sector:

```text
spec(Q)={-1,0,+1};
P_ch=1_(R\{0})(Q);
B_ch=P_ch tensor gamma^5 tensor c_partial;

c_partial =
  [[0,0,-i],
   [0,0,+i],
   [+i,-i,0]];

tau_R=pi/sqrt(2).
```

Each future record cell has the labeled carrier

```text
span{|r>,|p_Q>,|e_Q>}.
```

The physical source algebra is the gauge-invariant, charge-superselected
algebra. Cross-total-charge coherences are not used.

## Required exact derivations

1. Compute the full active-sector unitary

   ```text
   U_ch=exp(-i tau_R gamma^5 tensor c_partial)
   ```

   without typing an endpoint swap into the computation.
2. Verify that both chiral eigenvalues give the same complete record action:

   ```text
   |r> <-> |p_Q>;
   |e_Q> -> -|e_Q>.
   ```

3. Verify that the neutral sector is the identity and that the complete
   controlled unitary commutes with `Q`.
4. For `N` distinct future cells, derive the product write from the
   edge-local controlled generators and verify order independence.
5. For every charge-superselected source state and ready-cell product state,
   derive the finite outgoing state and verify:

   ```text
   omega_(N+1) restricted to the first N cells = omega_N.
   ```

6. Verify that later-cell writes commute with every earlier public-record
   observable and every physical source observable commuting with `P_ch`.
7. Derive the quasi-local state and central pointer sequence from these
   finite states.

## Causal-support gate

The endpoint construction counts as parent-derived post-write decoupling
only if the existing boundary action binds each local interaction to one
finite causal cell/edge and the future-directed acyclic composition applies
that edge once. A permanently acting static `c_partial` does not pass.

If compact cell support is inherited but its time profile is free, the lane
may pass only when every admissible profile with the same derived integrated
operator gives the same outgoing public state. It may not use profile freedom
in any response calculation.

## Verdicts

Return:

```text
CHARGED_INCIDENCE_OUTGOING_PUBLIC_STATE_DERIVED
```

only if the exact unitary, finite-state compatibility, later-cell
nondemolition, and causal-support gate all pass.

Return:

```text
CHARGED_INCIDENCE_OUTGOING_STATE_CONDITIONAL_ON_CAUSAL_SUPPORT
```

if the algebraic construction passes but one-use causal support is not yet a
live derived parent property.

Return:

```text
CHARGED_INCIDENCE_OUTGOING_STATE_BLOCKED
```

if the incidence unitary does not supply the claimed write or the finite
states fail Parent-State Covariance.

## Prohibitions

The evaluator may not:

```text
reactivate Primitive Reversible Record-Write v001;
insert controlled X;
assume coherent superpositions of different total charges;
select a spectral density;
identify a static one-cell recurrence with durability;
or compute alpha.
```

## Fixed statuses

```text
complete_parent_action_derived = false
physical_response_spectral_measure_derived = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
