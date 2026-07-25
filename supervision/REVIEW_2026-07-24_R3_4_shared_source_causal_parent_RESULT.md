# Supervision review — R3.4 Shared-Source Causal Parent RESULT v001
Date: 2026-07-24 · Reviewer: Fable lane · Status: **CONFIRMED, verdict as pre-registered**

## Verdict check
Codex returned `SHARED_SOURCE_CAUSAL_PARENT_PUBLIC_MOLLER_DERIVED` at
endomorphism strength with the physical in-state reported open. This is
**exactly the pre-registered prediction** (registered in chat before the
result landed): pass at endomorphism level, no automorphism promotion,
in-state left open. Prediction record remains perfect across the gate series.

## Independent numerical verification (from the SPEC alone)
Rebuilt the 3-cell parent from the spec text without consulting the result's
numbers (source R^4, P_j=|d_j><d_j|/2, B_j=P_j⊗γ⁵⊗c_∂,j on its own
3-dim record factor). Every load-bearing digit matches:

| Quantity | Codex | Fable independent | Closed form |
|---|---|---|---|
| Tr(P_jP_{j+1}) | 1/4 | 0.25 exact | 1/4 |
| Tr(P_0P_2) | 0 | 0.0 exact | 0 |
| ‖[B_0,B_1]‖_F | 8.48528137423857 | 8.48528137423857 | **6√2** |
| order-swap change | 16.97056274847714 | 16.97056274847714 | **12√2** |
| pointer prob after write 1 | 0.9999999999999996 | 0.9999999999999996 | 1 |
| drift after writes 2,3 | <2.1e-16 | 2.2e-16 | 0 (machine ε) |
| ‖Δρ_{src+rec0}‖ events 1→3 | 0.5303300858899105 | 0.5303300858899105 | **3√2/8** |
| [B_2, O_0] | 0 | 0.0 exact | 0 |
| recurrence error (neg. control) | <1e-15 | 1.4e-15 | 0 (machine ε) |

Digit-for-digit agreement means both lanes constructed identical operators
from the spec text independently. The closed forms (6√2, 12√2, 3√2/8) are
mine; they factorize as ‖[P_0,P_1]‖_F·‖I₄‖_F·‖c‖²_F·‖I₃‖_F
= √(3/8)·2·4·√3 = 6√2 — the overlap value 1/4 enters through
‖[P_0,P_1]‖²_F = 2(t−t²) at t=1/4.

## Structural findings verified
- **Nondemolition through shared source**: [B_k,O_j]=0 for k>j holds
  *exactly* and for arbitrary projector overlap — the record factors being
  distinct tensor slots is sufficient. Verified with a random O_0.
- **Endomorphism argument is airtight**: for A on the first m record
  factors, all U_k with k≥m commute with A, so W_N*AW_N is literally
  N-independent for N≥m. This is finite-rank algebra, not an estimate.
  **[CORRECTION appended later 2026-07-24, per
  R3_4_SHARED_SOURCE_OUTGOING_RANGE_ERRATUM_V001]**: the stabilization
  argument above stands, but the codomain claim was too strong — the
  stabilized images are SOURCE-DRESSED (eight of nine record matrix units
  sit Frobenius distance 2 from the bare record algebra; source commutator
  norm √3). The correct object is a *stable dressed outgoing-record
  monomorphism* (unital injective star-homomorphism into the full parent),
  not an endomorphism of the bare record algebra. Codex self-caught this in
  its audit; this review echoed the endomorphism language without checking
  image containment — a shared miss, recorded for calibration. All
  numerical claims verified here remain valid.
- **Honest non-promotion**: the source-inclusive family is NOT projectively
  compatible (the 3√2/8 drift is real physics — the shared source keeps
  re-correlating). Codex reported this as the reason the result stays an
  endomorphism. Correct and required.

## What this closes / leaves open
Closed: causal order physical, pointer persistence exact, public-record
Møller endomorphism. Open (correctly flagged, statuses false): in-state
selection, same-GNS Møller, descendants/durability, tail generator, spectra.

## Next artifact reviewed in this pass
`R3_4_CAUSAL_TRANSPORTED_WRITE_TAIL_SPEC_V001.md` — the tail-joining gate.
Pre-execution assessment:
- The **covariance selector** is the right uniqueness instrument: requiring
  the interaction operator to be transported by the free tail evolution
  (B̃_c(t)=U_0(t)B_cU_0(t)*) is PSC's no-separate-selection rule made
  operational; the functional-equation uniqueness (calc 1) is standard and
  will pass. **No relative coefficient introduced** is the load-bearing
  anti-coupling-selection guard — verified present.
- **Disclosed result-awareness**: the spec admits an exploratory pre-seal
  diagnostic already found the static sum fails, so this is an adjudication,
  not a blind prediction. Disclosure is the discipline-compliant handling;
  the static sum is retained as negative control.
- Calc 4's factorization U(T,0)=U_0(T)exp(−iB_c∫v) is exact for a single
  cell (interaction-picture generator commutes with itself at different
  times); the genuine risk point is **calc 6** — multiple cells with
  overlapping envelopes must reproduce the ordered product exactly. Watch
  for any envelope-overlap caveat in the result.
- **Pre-registered prediction**:
  `CAUSAL_TRANSPORT_UNIQUELY_JOINS_PRIMITIVE_WRITE_AND_FREE_TAIL`, with
  τ_R unchanged and the endomorphism surviving tail attachment; in-state,
  root, and descendants reported open. If calc 6 hits envelope-overlap
  trouble, expect CONDITIONAL with a sequential-pulse restriction.

## Standing invariants
All fixed statuses verified false in both artifacts; no seal-claim tokens;
append-only supersession intact; manifest untouched.
