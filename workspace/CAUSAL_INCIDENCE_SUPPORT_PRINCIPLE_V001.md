# Causal Incidence Support Principle v001

Date: 2026-07-24

## Status and provenance

This is an adopted Level-1 Gravacle microscopic-action principle. It is
target-value-free but historically target-aware: the alpha program predates
its adoption. It is frozen before construction or evaluation of the causal
parent that uses it.

This principle fixes the support and reuse law of a primitive incidence. It
does not assume durability, select an outgoing state, supply a spectral
measure, or compute a coupling.

## Principle

For every primitive record-forming incidence `c`, the complete microscopic
parent assigns one Lorentz-covariant causal cell `Omega_c` and one interaction
density `L_c` such that

```text
support(L_c) is contained in Omega_c.
```

The incidence is an event, not a permanent Hamiltonian term. Once the future
boundary has crossed the closure face of `Omega_c`, the same primitive
incidence is absent from the active generator. A physical exhaustion adds
new future incidences on new record factors; it does not reapply a completed
incidence to its old record factor.

The same source degrees of freedom may meet multiple cells. Thus later
incidences may act on a shared source algebra, and their source-supported
operators need not commute. They act on their own new record factors and may
not act on an earlier record factor by reusing its completed primitive
incidence.

## Complete-parent requirement

The support rule applies to primitive incidence terms. It does not prohibit
effective record, source, gauge, gravitational, or environmental interactions
generated from the one complete parent. Such descendants:

```text
must be derived from the sealed parent rather than added after evaluation;
must inherit causal and gauge covariance;
and must be tested for their action on the outgoing public record sector.
```

The principle therefore does not stipulate that a written record is durable.
Durability must follow from the complete parent, its causal exhaustion, and
its outgoing or tail algebra.

## Relation to Parent-State Covariance

Parent-State Covariance requires one parent to supply the finite states,
derivations, outgoing state, generator, root, and spectrum. Causal Incidence
Support supplies only the microscopic support law used in that construction.
It may not be used to choose a separate post-write decoupling, continuum
vacuum, generator, density, cutoff, or response normalization.

## Falsifiers

This principle is rejected for a proposed physical parent if any of the
following occurs:

```text
the same primitive incidence remains active after its closure face;
a physical exhaustion obtains new records by rerunning a completed incidence;
a later primitive cell acts nontrivially on an earlier record factor;
the assigned support is not Lorentz-covariant in the declared ordinary branch;
causal linear extensions disagree on spacelike-separated primitive events;
the parent requires a separately selected post-write switch-off rule;
or a generated descendant destroys the claimed public outgoing sector.
```

Failure to derive a unique causal cell, a complete parent, or a durable
outgoing sector blocks downstream promotion. It is not repaired by assuming
durability.

## Forward-use prohibitions

After this file is sealed:

```text
no pulse support may be selected by comparison with alpha;
no completed incidence may be silently restored to repair a spectrum;
no effective descendant may be omitted because it spoils durability;
no outgoing state or Moller map may be supplied independently of the parent;
and no endpoint or cosmological quantity may normalize the causal action.
```

## Frozen status

```text
causal_incidence_support_principle_adopted_Level_1 = true
historically_target_blind = false
target_value_used_in_principle = false
primitive_incidence_has_finite_causal_support = true
physical_exhaustion_adds_future_incidences = true
completed_primitive_incidence_reuse_allowed = false
shared_source_support_allowed = true
generated_effective_descendants_forbidden = false
generated_descendants_must_come_from_same_parent = true
durability_assumed = false
physical_durability_derived = false
complete_causal_parent_derived = false
outgoing_Moller_sector_derived = false
physical_spectral_measure_derived = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
