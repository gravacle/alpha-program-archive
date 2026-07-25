# 11 — Durable-Record Closure Criterion (DCC) v001

Status: PROPOSED PRINCIPLE — target-value-free, target-aware (Level-1
posture identical to the package's other principles). Frozen by seal BEFORE
any application to a concrete connected family. No measured constant
appears in this file or may be consulted by anything downstream of it.

## Primitive basis (all already in-package)

1. A record is a comparison of accumulated action-phase, exp(iS/ħ), under
   the unit character (FUNDAMENTAL principle; bridge gate).
2. A completed registration is a persistent public fact; the durability
   obligations (recorded observable, pointer sectors, persistence,
   recoverability) are the package's own unmet SP08 items.
3. The single-cell return theorem (binary closure gate): non-diagonal
   dynamics on a comparison produces recurrence — the state returns; a
   single cell cannot hold a record. Durability is therefore a property of
   the connected many-cell system, not of any cell.
4. Disjoint records compose additively (monoidal extensivity, as claimed by
   the spec; its proof file is a requested dependency).

## The criterion

A connected generator B on the registration complex is
**durability-admissible** iff:

- **DC1 (content superselection / phase-only dynamics on facts).**
  [B, N_i] = 0 for every cell-registration observable N_i.
  Motivation: the only dynamics the action-phase primitive permits on a
  completed public fact is phase accumulation. Any term that transfers
  registered content between cells (e.g. |10⟩⟨01| + h.c.) or erases it
  re-opens the comparison; by the return theorem such dynamics oscillates
  and no durable record exists. Content may not move; only phases evolve.

- **DC2 (disjoint additivity).** For cells with disjoint incidence support,
  phase rates add: E(P ∪ P′) = E(P) + E(P′) for registration patterns P, P′
  on disjoint supports. No registration action at a distance.

- **DC3 (incidence locality of connected corrections).** Deviations from
  additivity are supported only on incident (boundary-sharing) cell
  collections: pairwise corrections on incident pairs, k-fold corrections
  only on jointly incident k-collections.

- **DC4 (relational single-cell rate).** The single-cell phase rate is the
  sealed relational marker rate; no absolute value is imported here.

## Declared predictions (stated before any computation)

P1. Content-transfer (swap-type) members of any connected family are
    excluded by DC1.
P2. The durability-admissible subfamily of any connected family is diagonal
    in the registration basis: B = Σ_P E(P)|P⟩⟨P|.
P3. For a two-cell family on DISJOINT cells, DC2 forces the connected
    correction λ_c ≡ E(11) − E(01) − E(10) + E(00) = 0: the family
    collapses to a point.
P4. For INCIDENT cells, exactly one pairwise coefficient λ_c per incident
    pair survives DC1–DC4. The criterion fixes the FORM of admissible
    cross-talk (diagonal, pairwise, incident-only, phase-type) and locates
    the coupling seat; it does not by itself fix the magnitude λ_c.

P4 is stated in advance deliberately: if the magnitude were to fall out of
DC1–DC4 alone, that would contradict the run's angles-not-amplitudes
finding and should itself be treated with suspicion.

## Failure conditions (fail-closed, declared in advance)

- If the exhibited counterfamily B_λ survives DC1 in full (swap included),
  DCC is vacuous: report and retire it.
- If DCC excludes ALL nontrivial connected dynamics including diagonal
  cross-talk on incident pairs, DCC is too strong: report and retire it.
  It may not be weakened after seeing either outcome.
- No coefficient, filter, or exception may be added to DC1–DC4 after any
  application result is seen.

## Relation to the package's open items (declared targets, not results)

- Family E (connected generator): DCC is the candidate replacement for the
  ADOPTED quasi-free completeness premise. Note the live possibility that
  DCC *contradicts* that premise's exclusion of diagonal quartic
  (n_i n_j-type) terms: under DCC, phase-type cross-talk is exactly what
  survives. If so, the adopted premise was excluding the physical
  cross-talk seat — to be reported as found.
- Fork 2 (absolute interval): DCC's DC1-stable sectors are the objects
  whose L→∞ durable-interval limit the spec's pass conditions require.
- Over-determination tell: DCC counts as load-bearing structure only if it
  decides at least two independent open items (e.g., collapses Family E's
  operator freedom AND constrains the closure-dynamics form of Fork 1).
  If it decides exactly one knob, treat as suspect.

## Sealing

This file is hashed before any application script exists. The application
(B_λ test) is written and run only after this seal is recorded.
