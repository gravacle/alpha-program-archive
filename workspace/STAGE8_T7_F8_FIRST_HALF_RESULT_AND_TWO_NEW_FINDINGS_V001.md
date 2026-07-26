# Stage-8 T7 F-8 First Half — Result and Two New Findings V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY_RESULT + ESCALATION
```

The F-8 gate's first half (fresh-context re-derivation) is discharged.
Transcript sealed at /Users/bgm/MB Work/alpha_supervision/
F8_REDERIVATION_RETURN_SEALED_TRANSCRIPT_V001.md (11512a7d…). The lane
was forbidden to read the claiming lane's phase-1/phase-2 drafts and
primary JSONs — the exact exposure the reviewer's audit named. The
second half (hostile review) is NOT yet run; the gate is not closed.

## 1. Route-Q independence: INDEPENDENTLY CONFIRMED

```text
VERDICT: ROUTE_Q_INDEPENDENT
```

Reproduced from the sealed text with the lane's own derivation, via a
full twelve-input trace (Q1-Q12) of the M3 colored-Kotecky-Preiss
schema, plus THREE adversarial refutation attempts, all of which failed.
No Route-T artifact (transfer operator, spectral gap, TT1/TT2/TT3,
the O7 intertwiner) appears among M3's inputs. The principal's Q1 answer
and the reviewer's audit are therefore reproducible from scratch, which
is what F-8 exists to establish.

## 2. NEW FINDING (highest value in the return): the sealed O1 display is defective

```text
The sealed majorant spec's O1 display
  R_comp^(K)(a_+,a_-) = sum_((mu_c),(lambda_c)) prod_c w_(mu_c)^* w_(lambda_c)
                          Gamma( u_(mu_c)^(c)(a_-)^dagger u_(lambda_c)^(c)(a_+) )
is, read literally with prod_c scoping the whole term, the INTERLEAVED
reading — a per-cell product of Gammas. THAT READING IS FALSE IN
GENERAL. If prod_c instead scopes only the weights, the Gamma-argument
carries a free index c and the display is ILL-FORMED.
THE CTP-NESTED READING IS FORCED. The lane established this with an
exact witness and independently of the phase-1 lane's D-N1 flag (which
it could not read).
```

CONSEQUENCE, stated plainly: the readings coincide on DISJOINT cells but
diverge on overlapping/adjacent ones — which is precisely where the
linked-cluster activities live. A downstream determinant factorization
built on the interleaved reading would be wrong exactly at the terms
that carry the cluster activities. The nested reading governs of record;
the sealed display is corrected here, not edited.

## 3. NEW FINDING: Q6 is a second underived obligation of Route Q

```text
Q6: a bound on #{connected clusters of size n containing a given cell C},
    uniform over the D3 quantifier — which requires
        sup over admitted cellulations X of the maximum cell-adjacency
        degree Delta(X)  <  infinity.
STATUS: UNDERIVED. It is Route-Q-internal (polymer combinatorics), NOT a
Route-T artifact, so it does not disturb the re-scope; but it is a
SECOND gap alongside E1.
```

This QUALIFIES the re-scope's consequence clause. The accurate statement
is now:

```text
Route Q carries the full D3 quantifier alone contingent on BOTH
  (i) a successor E1 activity architecture (the Phase-1 K_sea being
      divergent as defined — independently reconfirmed here as Q8), and
  (ii) Q6, uniform bounded cell-adjacency degree over D3.
```

Named blocker added: `Q6_UNIFORM_CELL_ADJACENCY_DEGREE_UNDERIVED`, owner
= the parent majorant spec's Route-Q line (not the E1 successor spec,
which owns E1 only).

## 4. Escalation to the principal

```text
The Q1/O7 retirement STANDS — Route-Q independence is now
independently reproduced, which strengthens it rather than weakening it.
BUT the re-scope's consequence clause ("Route Q carries the quantifier
alone, contingent on E1") was INCOMPLETE: there are two contingencies,
not one. This lane records the correction and does not treat Q6 as
absorbed by the E1 program. Whether Q6 is commissioned now, in parallel
with the E1 routes, or deferred, is the principal's scheduling call —
its difficulty is not yet assessed and this lane makes no claim about it.
```

## Protected status

```text
F8_rederivation_first_half_discharged = true
F8_hostile_review_discharged = false
route_Q_independence_reproduced = true
O1_display_nested_reading_forced = true
Q6_uniform_cell_adjacency_degree_underived = true
connected_linked_cluster_density_proved = false
kappa_record_computed = false
alpha_computed = false
proof_authorized = false
```
