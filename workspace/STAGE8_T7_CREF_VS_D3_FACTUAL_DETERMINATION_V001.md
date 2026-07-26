# Stage-8 T7 — C_ref vs D3: Factual Determination V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY FACTUAL DETERMINATION. NOTHING IS RESOLVED, NARROWED OR
ADOPTED HERE.
VERDICT: (i) SAME OBJECT — a genuine conflict between two sealed
authorities exists, and per the principal's instruction it is HIS to
resolve.
CONSEQUENCE, BINDING ON THIS LANE: the
D3_REFINEMENT_NATURAL_VOLUME_WEIGHT_AND_RESPONSE_PULLBACK_V001 spec is
NOT SEALED and is HELD pending the principal's decision.
D3 IS NOT NARROWED. NO SHAPE CONDITION IS ADOPTED. PRODUCTION PROHIBITED.
```

## The three texts, quoted rather than paraphrased

```text
[1] V011 (aa7c6d49…), lines 1396-1412, in the passage headed by "The local
    coefficient must also be cellulation independent":
      "Freeze an admissible class `C_ref` of oriented, shape-regular
       periodic regular-CW cellulations with:
           cubical bisection;
           oriented simplicial/barycentric subdivision;
           and common refinements preserving the same smooth coframe and
           connection."
      "The response map must commute with pullback to a common refinement,
       and the intensive quadratic coefficient must be invariant under each
       elementary refinement up to a boundary term whose ratio to
       four-volume tends to zero."
      "Failure to prove this naturality either blocks the general claim or
       restricts the result explicitly to that cellulation."

[2] BATTERY SPEC T13 (the authority D3 ITSELF CITES), line 277ff:
      "Pinned: family A = cubical bisection sequence; family B = oriented
       simplicial/barycentric subdivision sequence (DISTINCT C_ref
       GENERATORS, V011 1397-1412 — 'one hypercubic sequence is a
       regression fixture, not proof of universality')."

[3] D3 (majorant spec 818083a5…, line 151ff), opening words "Per the
    battery authority's T13 pinning":
      "skeleton: the primary hypercubic fixture ...;
       family A: the cubical bisection sequence;
       family B: the oriented simplicial/barycentric subdivision sequence;
       plus:     all common refinements of members of A and B."
      "The theorem's quantifier ranges over the skeleton, A, B, and common
       refinements. Pinning the quantifier to any finite list is NOT
       available to any lane under any outcome (F-2)."
```

## Why the verdict is (i) SAME OBJECT

```text
THE LINKAGE IS TEXTUAL AND EXPLICIT, NOT INFERRED. D3 does not define its
families independently. It says "Per the battery authority's T13 pinning",
and T13 in turn names families A and B as "DISTINCT C_ref GENERATORS" and
CITES V011 1397-1412 BY LINE NUMBER — which is precisely the C_ref
passage. The chain is:
        D3  <--  T13  <--  V011's C_ref, cited by line
So D3's A and B are not merely similar to C_ref's generators; they ARE
C_ref's generators, by the explicit words of D3's own cited authority.
This is not "two different things that merely look alike."

MEASURED FACTS SUPPORTING THE READING:
  - "C_ref" occurs EXACTLY ONCE in all of V011 — in its defining sentence.
    Nothing else in V011 quantifies over it under that name.
  - "shape-regular" occurs ZERO times in the battery spec (both versions)
    and ZERO times in the majorant spec. The adjective is introduced in
    V011 and is NOT carried forward by T13 or by D3.
  - "C_ref" occurs ZERO times in the majorant spec. D3 inherits the
    generators through T13 without ever naming the class.

THEREFORE THE PRECISE SHAPE OF THE CONFLICT:
  SAME generating data (cubical bisection; oriented barycentric; common
  refinements), by explicit citation.
  DIFFERENT ADMISSIBILITY PREDICATE:
      V011's C_ref   = ... SHAPE-REGULAR ... + common refinements
                       preserving the same smooth coframe and connection
      D3 as frozen   = ALL common refinements of members of A and B,
                       no shape condition, and F-2 forbidding any
                       finite-list narrowing
  D3's CLASS IS STRICTLY LARGER THAN C_ref's. A common refinement of a
  cubical bisection with a barycentric subdivision generically produces
  SLIVERS, which are not shape-regular. Those cellulations are INSIDE D3
  and OUTSIDE C_ref.
  NO SEALED ARTIFACT ANYWHERE RECONCILES THE DIFFERENCE. There is no text
  that says D3 drops shape-regularity deliberately, and none that says it
  inherits it.
```

## The honest counter-reading, stated because it is available

```text
A (ii)-READING EXISTS AND THIS LANE DOES NOT ADOPT IT: one could argue
T13's phrase means only that A and B are generators OF C_ref — i.e. that
T13 borrows the two families without importing C_ref's full admissibility
predicate — leaving D3 free to close them under all common refinements as
its own independent choice.
WHY THIS LANE DOES NOT REST ON IT: that reading requires D3 to have
silently taken a strictly broader closure than the class it cites, with no
sealed text recording the broadening. Treating an unrecorded divergence
from a cited authority as intentional is exactly the kind of
convenience-reading this program's discipline exists to refuse — and it
would be convenient HERE, because it would let the object spec proceed
today. The principal decides; this lane reports the conflict rather than
reading it away in the direction that unblocks its own work.
```

## What V011 itself already provides, recorded because it bears on the resolution

```text
V011 DOES NOT ASSERT THAT NATURALITY HOLDS ON C_ref. It ISSUES AN
OBLIGATION and pre-registers the failure mode:
    "Failure to prove this naturality either blocks the general claim or
     restricts the result explicitly to that cellulation."
So V011 anticipated that refinement-naturality might not extend, and named
the honest response in advance. That is materially relevant to how the
conflict can be resolved without either authority being wrong — but the
choice among V011's own two branches (block, or restrict-and-say-so), and
whether D3's breadth survives, IS THE PRINCIPAL'S AND IS NOT TAKEN HERE.
```

## The irony, recorded plainly as the principal asked

```text
This lane froze the D3 reading in the BROAD direction, on four grounds
sealed before either consuming lemma existed, precisely BECAUSE it cost
this lane — it made Q6 bite rather than retire — and because F-2 forbids
narrowing the quantifier. That freeze was ratified.
IT NOW APPEARS THAT THE DISCIPLINED CHOICE IS ALSO THE ONE V011 DOES NOT
SUPPORT. The broad reading is the honest reading of D3's own text and of
F-2; it is broader than the class V011 asked to be frozen. Better to know
that plainly now than to discover it inside a proof, which is why the
determination was ordered before the spec.
NOTHING ABOUT THE FREEZE IS WITHDRAWN HERE. The freeze stands as sealed;
what is now on the record is that its breadth exceeds C_ref's.
```

## Consequence for the object spec, and for the three items it feeds

```text
THE SPEC IS NOT SEALED. Codex's
D3_REFINEMENT_NATURAL_VOLUME_WEIGHT_AND_RESPONSE_PULLBACK_V001 is HELD.
Sealing it now would require choosing an admissible class, and that choice
IS the conflict.
IF the principal resolves toward D3's breadth: the spec proceeds as Codex
wrote it, targeting all common refinements INCLUDING slivers, and Codex's
sharp conditional governs — if a sliver of volume eps*|C|_4 produces an
O(|C|_4) response defect, the object FAILS and recast Q6 becomes
ILL-POSED rather than merely unproved. That is a FINDING, to be reported
as such.
IF the principal resolves toward C_ref's restriction: then the object is
proved on a class STRICTLY SMALLER than the one A-L5 and recast Q6
quantify over, and those two remain unserved — which must be said in the
verdict language rather than left implicit.
EITHER WAY the weight clause (items 2 and 3: |C|_4 = integral |det e|,
exact reaggregation, and the negative control against w=1 and w=diam^4) is
INDEPENDENT of the shape question and is unaffected. Codex's frozen
prediction that the volume weight survives slivers and is derivable from
sealed authorities is not disturbed by this determination.
```

## Protected status

```text
cref_vs_D3_verdict = (i)_SAME_OBJECT_CONFLICT
conflict_resolved = false
resolution_holder = principal
D3_narrowed = false
shape_condition_adopted = false
D3_freeze_withdrawn = false
D3_class_strictly_larger_than_C_ref = true
sliver_cellulations_in_D3_and_outside_C_ref = true
shape_regular_in_battery_spec = 0_occurrences
shape_regular_in_majorant_spec = 0_occurrences
C_ref_occurrences_in_V011 = 1
D3_object_spec_sealed = false
D3_object_spec_status = HELD_PENDING_PRINCIPAL
weight_clause_unaffected_by_conflict = true
pass_reachability_control_complete = false
v003_started = false
production_authorized = false
alpha_computed = false
proof_authorized = false
```
