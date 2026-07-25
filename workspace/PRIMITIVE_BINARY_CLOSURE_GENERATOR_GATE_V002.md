# Primitive Binary Comparator Orthogonalization Gate v002

## Authority correction

This file supersedes v001. Version 001 incorrectly promoted a balanced-state
autocorrelation identity to a physical durable-record generator. It also left
the all-time endpoint-stability premise implicit.

The v001 arithmetic remains valid, but its physical status is rejected.

## Conditional algebra

Grant:

```text
a time-independent Hermitian two-state generator H;
all-time endpoint invariance U(t) P_i U(t)^dagger = P_i;
a common energy removed as an unobservable constant.
```

Then

```text
H = Delta P_1
```

for a real signed gap `Delta`. The endpoint labels alone do not select its
sign.

For the general normalized comparator state

```text
|psi_p,chi>
  = sqrt(p)|0> + exp(i chi)sqrt(1-p)|1>,
```

the autocorrelation is

```text
zeta_p(t)
  = p + (1-p) exp(-i Delta t/hbar).
```

Its minimum magnitude over phase is

```text
min |zeta_p| = |2p-1|.
```

Therefore an exact autocorrelation zero exists only for the separately chosen
balanced calibration `p=1/2`. For that calibration,

```text
|Delta| tau_orth/hbar = pi
```

at the first positive orthogonalization time.

## Physical limitation

This result maps a balanced comparator to an orthogonal comparator state. It
does not create conditional record states, copy or amplify a source
alternative, or make the orthogonality persistent. The state returns after a
further equal interval under the same autonomous generator.

Consequently:

```text
tau_orth is not yet tau_record;
|Delta| is not yet a physical record gap;
the sign of Delta is not fixed;
and no source mass follows.
```

A durable-record generator must be derived from a source-conditioned
record-write interaction and a persistence/closure rule.

## Status

```text
all_time_endpoint_invariance_required = true
balanced_calibration_derived = false
conditional_balanced_orthogonalization_relation = true
gap_interval_relation_is_conditional = true
durable_record_condition_established = false
physical_record_generator_derived = false
source_mass_identified_with_record_gap = false
finite_response_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
