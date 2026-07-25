# R3.4 Concurrent-Cell Scope Erratum v001

Date: 2026-07-24

## Superseded breadth

The sentence in
`R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md` saying that the exact
compatibility proof applies to "every finite M>N" is too broad when read as
including arbitrary spacetime-overlapping concurrent cell additions.

The sealed v001 result is preserved. This erratum is its append-only scope
successor.

## Correct theorem scope

Exact completed-record restriction compatibility is established for
causally sequential exhaustions:

```text
every cell added at stage M opens only after all closure faces belonging to
stages <=N have completed.
```

Within that class, later stage maps act identically on completed record
factors and the v001 inductive-state/GNS argument applies.

## Concurrent counterexample

The independent Stage-7 mathematical review supplied a finite interacting
counterexample for spacetime-overlapping concurrent cells:

```text
restriction difference at reported overlap = 5.6e-6;
larger-overlap difference                  = 3.2e-4;
causally sequential control                = 4e-13.
```

The review reported stability to five significant figures under
step-quartering. The construction lane has not independently reproduced
that external calculation, so these values are recorded as review evidence,
not as a new local computation.

The counterexample blocks an unconditional concurrent-cell theorem. It does
not invalidate the causally sequential theorem or its completed-record GNS.

## Reopen condition

The theorem may be extended to spacelike-concurrent exhaustions only after a
sealed derivation of a spacelike causal-factorization/light-cone lemma for
the interacting finite-cell parent and an independent counterexample
recheck.

## Fork-8 inheritance

Fork-8 P1 inherits this restriction. "Cofinal physical exhaustion" in the
promoted principle means a cofinal causally sequential exhaustion in the
current branch. Packing- or ordering-independent extension beyond that
class remains open.

## Status

```text
causally_sequential_exact_compatibility = DERIVED
spacetime_concurrent_exact_compatibility = NOT_DERIVED
concurrent_counterexample = EXTERNAL_REVIEW_EVIDENCE
spacelike_factorization_lemma = OPEN

fork_8_scoped_promotion_retained = true
complete_parameter_free_Q_spec_frozen = false
alpha_computed = false
proof_authorized = false
```
