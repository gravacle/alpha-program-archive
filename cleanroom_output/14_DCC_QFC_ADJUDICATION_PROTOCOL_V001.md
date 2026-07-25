# 14 — Adjudication Protocol: DCC vs Quasi-Free Completeness (v001)

Frozen before any adjudication argument is produced. No lane executing this
protocol may prefer a verdict for its downstream consequence (in particular,
not for what it implies about the availability or location of any coupling).
No measured constant may be used. Evidence is confined to the workspace.

## The question

Two principles govern connected many-cell dynamics and appear to conflict:

- **DCC/DC1** (OUTPUT/11, sealed ec559cb7…): on durable-record sectors,
  admissible generators satisfy [B, N_i] = 0 for every registration-content
  observable — content is superselected; only phases evolve.
- **QFC** (Global Boundary Descent and Quasi-Free Completeness, as stated in
  CURRENT_WORK/source_parent/BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md
  and as used by the closure gate): the connected parent is quasi-free
  (quadratic in CAR fields); quartic terms are excluded.

Prima facie, a quasi-free generator contains hopping terms (content
transfer, DC1-forbidden) and excludes diagonal quartic terms (the only
cross-talk DC1 admits). Adjudicate:

**Q1.** Is DC1 derivable from the in-package primitives (action-character
exp(iS/ħ); persistence/durability obligations; the single-cell return
theorem), or is it independent adopted content? State whether the derivable
form is exact commutation or an asymptotic/emergent superselection, and
whether that difference is load-bearing.

**Q2.** Is QFC derivable from any in-package primitive, or adopted? (Its own
file's status language controls; quote it.)

**Q3.** Do DCC and QFC actually conflict within a shared declared scope, or
do their scopes split (e.g., QFC governing pre-registration source dynamics;
DCC governing post-registration record dynamics)? Read the declared scopes
in the files; do not assume.

## Allowed verdicts (exactly one per question)

- Q1: DC1_DERIVED_EXACT | DC1_DERIVED_ASYMPTOTIC_ONLY | DC1_ADOPTED
- Q2: QFC_DERIVED | QFC_ADOPTED
- Q3: CONFLICT_REAL_SHARED_SCOPE | SCOPES_DISJOINT | CONFLICT_UNDECIDABLE_IN_PACKAGE

## Resolution rule (declared in advance)

If one principle is derived and the other adopted, and the conflict is real
within a shared scope, the derived principle prevails *in that scope* and
the adopted one must be re-scoped or retired there. If both are adopted and
the conflict is real, the fork goes to NEEDS_THEORY_DECISION as a new
numbered fork. If scopes are disjoint, both stand with scopes made explicit,
and the interface between them becomes a named object. No other resolution
is permitted; in particular, no resolution may cite downstream numerical or
structural convenience.

## Blindness constraints on the lanes

- Q1 and Q2 lanes receive the principle texts and primitives only; they are
  not told of the conflict, the seat identity, or any coupling implication.
- The Q3 lane reads both principles' scope declarations and the closure
  gate's usage; it does not receive the Q1/Q2 lanes' outputs.
- A separate judge lane applies the resolution rule to the three verdicts.
