# Stage-8 T7 L1 Multi-Cell Lemma Assessment V001

Date: 2026-07-26 (autonomous window; disposition item 5.3 / queue D5)

## Status

```text
APPEND_ONLY_ASSESSMENT_SEALED
```

## The question

Is L1 — the per-cell-to-K multi-cell lemma flagged by the gamma memo —
required by T7(iii) INDEPENDENTLY of the dead gamma route?

## The answer: YES, and it is not an extra lemma — it is constitutive

T7(iii)'s linked-cluster thermodynamic density is ITSELF a
per-cell-to-K statement: it asserts that -log Z_K decomposes into
anchored connected-cluster activities whose sum converges uniformly
(the majorant) and whose intensive limit exists with subextensive
boundary corrections. The majorant route memo (ROUTE_MEMO_2026-07-25_
linked_cluster_majorant.md) already names the constitutive pieces:

```text
Lemma 0  — the exact relayed multi-cell composition identity for Z_K
           (every route's FIRST numbered obligation; new, underived);
B-L3/M4  — uniform absolute convergence of the DIFFERENTIATED cluster
           series (convergence of the series does not imply it);
item 4   — linked-cluster density + subextensive boundary corrections
           as corollaries of the same theorem.
```

Together these ARE L1. What died with gamma was only gamma's specific
use of the lift (transporting a per-cell ENVELOPE-DIFFERENCE identity
to K-level). The lift machinery itself sits on the critical path
through T7(iii) regardless of the ER fork.

## Blocker-list entry (named, append-only)

```text
NAMED BLOCKER: T7III_MULTICELL_COMPOSITION_AND_LIFT
  = Lemma 0 (relayed multi-cell composition identity for the completed
    chain per the L2 typing freeze) + uniform differentiated-series
    convergence + the K-level density statement.
  Owner: the T7(iii) majorant spec (queue D6). Not commissioned for
  gamma. Blocks: T7(iii), hence T7(iv) instantiation, hence
  kappa_record.
```

Typing note binding on the D6 spec: per the sealed L2 freeze
(STAGE8_T7_L2_INTENSIVE_HESSIAN_TYPING_FREEZE_V001), Lemma 0 and the
cluster expansion must be stated on the COMPLETED chain (pointer-sum
functional), with the exhaustive closure retained as companion; the
memo's Lemma-0 display (written for the exhaustive Z_K) transfers with
the pointer weights replacing the trace weights, and that restatement
is part of the spec's frozen definitions, not an executor choice.

## Protected status

```text
connected_linked_cluster_density_proved = false
kappa_record_computed = false
alpha_computed = false
proof_authorized = false
```
