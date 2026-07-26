# Transport-Functor Charter — OPTIONS WITH COSTS (nothing adopted) V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY OPTIONS MEMO for the principal's charter. NOTHING ADOPTED. NO
RECOMMENDATION ADOPTED. D3 NOT narrowed. R-L2b NOT treated as unblocked.
Cites: plan 12f204c64f0c0fd9...; amendment 001 c59cc8337913b81b...; this
lane's frozen step-1 determination 83fe2fade220a92c...
HEADLINE: THE FIVE PINS COLLAPSE TO ONE DECISION, and that decision is
WHICH SEALED REQUIREMENT TO RENEGOTIATE — every candidate breaks a
different one. PRODUCTION PROHIBITED. alpha_computed = false.
```

## 0 — SCORING THE FROZEN PREDICTIONS (P-T1..P-T4)

```text
P-T1  independent lane confirms case (b)                        HIT.
P-T2  "identifies the multiple-roles-of-L structure OR SOMETHING
      EQUIVALENT, rather than a single binary"                  HIT,
      and it was the prediction this lane flagged as most likely to fail.
      It reached the WITHHELD causal-diamond observation blind. But score it
      precisely: it produced a FOUR-ITEM list, not this lane's THREE ROLES,
      and the two lists are NOT the same (section 1). Equivalent in spirit,
      different in content.
P-T3  "role 1 (time extent) is mechanism-determined, NOT a free choice"
                                                                PARTIAL.
      The mechanism does force TEMPORALITY — strength = coupling x duration.
      It does NOT force the UNITS, and the independent lane's item (i)
      correctly leaves physical-thickness vs normalized-local-time open.
      This lane over-stated "determined". Downgraded to: the DIMENSION is
      forced, the NORMALIZATION is not.
P-T4  "the causal-diamond point is correct but NOT decisive — narrows
      without closing"                                          HIT.
      Section 3 shows it collapses all five pins into one decision, which is
      a large narrowing; and section 2 shows it does NOT close the question,
      because the single decision still has four incompatible answers. Both
      halves of the prediction hold.
```

## 1 — Q1: RECONCILIATION. FIVE PINS. NEITHER LIST WAS COMPLETE.

```text
THIS LANE'S THREE ROLES OF L (from A-L4) versus THE INDEPENDENT LANE'S FOUR
UNPINNED ITEMS, mapped:

 P1  CELL TIME EXTENT.
     mine Role 1 ("in-cell strength <= eps ||b_D||_inf x (cell time extent)
     ~ eps L")  ==  its (i) (physical thickness vs normalized local time).
     SAME PIN. Its version is sharper: it names the units question mine
     assumed away. See P-T3.
 P2  THE VOLUME SYMBOL.
     mine Role 2 (A-L4's shell-count normalization R^3 dR / L^4, and the
     L^8 of the pair activity)  ==  its (ii) (A-L1's |D_1|, |D_2|).
     SAME PIN SEEN AT TWO SITES, and the two sites connect: A-L4's L^8 IS
     A-L1's |D_1||D_2| with both volumes set to L^4. Verified: A-L1 reads
     || 1_{D_1} C 1_{D_2} ||_2^2 <= |D_1||D_2| / (pi^4 R^6). So its (ii) is
     the SEALED site and my Role 2 is the DERIVED site of one ambiguity.
 P3  MINIMUM SPATIAL SEPARATION — the lower cutoff of int_L^inf R^-3 dR,
     i.e. the smallest R at which two atoms count as distinct.
     *** MINE ONLY. THE INDEPENDENT LANE DOES NOT NAME IT. *** And A-L1
     defines R = dist(D_1, D_2), so on non-diamond atoms "dist" between
     what and what is itself unpinned.
 P4  tau_R: DIMENSIONLESS full record interval vs PHYSICAL duration per
     atom.
     *** ITS ONLY. THIS LANE FOLDED IT INTO P1 AND WAS WRONG TO. *** They
     are different questions: P1 asks what the atom's time extent IS; P4
     asks whether tau_R is a pure number on [0,1] or a physical duration
     that must fit inside it.
 P5  b_D^(C) / M_C — what "the cell's causal diamond" MEANS on a
     non-diamond atom.
     *** ITS ONLY AS A LISTED PIN. *** This lane flagged it as an
     observation and explicitly declined to rely on it; it does not appear
     as an L in A-L4's algebra, which is why a decomposition of A-L4 alone
     could not surface it.

ANSWER TO Q1: THE LISTS ARE NOT THE SAME LIST IN DIFFERENT VOCABULARY. Each
lane missed something the other found. THE UNION IS FIVE PINS. Neither
three nor four was complete, and this is the strongest argument in today's
record for blind cross-checking as a standing method rather than an
occasional one.
```

## 2 — Q3 FIRST, because it reorganises Q2: THE FIVE PINS COLLAPSE TO ONE DECISION

```text
TAKE THE CAUSAL-DIAMOND CONSTRAINT SERIOUSLY. Phase-A A1/A2's support is
0 < t < 1, |x| < min(t, 1-t) — EXACTLY the causal diamond of the unit time
interval, with spatial extent FIXED BY temporal extent at the light cone.
A diamond therefore has ONE parameter.
CONSEQUENCE: choose which diamond construction carries the insertion, and
ALL FIVE PINS FOLLOW.
    P5 is the choice itself.
    P1 follows: the diamond's temporal extent is determined by the
       construction.
    P2 follows: the response weight is that diamond's 4-volume.
    P4 follows: local time on [0,1] is the diamond's own parameter, so
       tau_R stays DIMENSIONLESS — unless the chosen construction forces a
       physical duration, which is where P4 becomes a new principle (§4).
    P3 follows: A-L1 already fixes R = dist(D_1, D_2) — distance between
       the DIAMONDS, once the diamonds are defined.
*** SO THE CHARTER IS ONE DECISION, NOT FOUR OR FIVE. That is worth
knowing, and it is what the principal asked. ***
BUT IT DOES NOT CLOSE THE QUESTION, because the one decision has at least
four incompatible answers, and EACH BREAKS A DIFFERENT SEALED REQUIREMENT.
```

## 3 — Q2: THE FOUR CANDIDATES AND WHAT EACH COMMITS THE PROGRAM TO

```text
NOTE ON GEOMETRY, used throughout: a diamond is ISOTROPIC. Its spatial
radius equals half its temporal extent. So a diamond inscribed in an
anisotropic atom is limited by the atom's SMALLEST extent, in EITHER
direction — thin-in-time and thin-in-space both give a small diamond.

C-A  INSCRIBED DIAMOND (largest diamond inside the atom).
     volume ~ (min extent)^4, which is << |C|_4 on slivers in BOTH
     directions.
     D5 action-density:  SATISFIED WITH ROOM. Activity per unit |C|_4 -> 0
                         as aspect ratio grows.
     R-L2b:              FAVOURABLE. Effective exponent >= 1; the estimate
                         becomes easier, not harder.
     A-L5 shell counts:  unaffected.
     T11 naturality:     *** FAILS. *** Inscribed-diamond volume is NOT
                         additive under refinement — the children's
                         inscribed diamonds do not reassemble the parent's.
     *** THE FATAL COST: THE ATOM IS NOT COVERED. Most of a sliver lies
     OUTSIDE its inscribed diamond, so the response is blind to most of the
     atom's volume. Under sliver refinement the covered fraction -> 0, and
     the total response scales with total inscribed-diamond volume rather
     than total 4-volume. THAT BREAKS EXTENSIVITY AND THE
     CELLULATION-INDEPENDENT THERMODYNAMIC LIMIT — which is T7(iii)'s core
     requirement and the reason D3 exists. ***

C-B  CIRCUMSCRIBED DIAMOND (smallest diamond containing the atom).
     volume ~ (max extent)^4 >> |C|_4 on slivers.
     Covering:           yes, but diamonds of neighbouring atoms OVERLAP,
                         so atoms double-count.
     D5:                 *** FAILS. *** Activity per unit |C|_4 DIVERGES
                         with aspect ratio; this is precisely the
                         normalization D5 declares a spec violation.
     R-L2b:              IMPOSSIBLE as stated — the required exponent goes
                         negative.
     Dismissible on D5 alone, and recorded so the charter shows the full
     option space rather than a pre-filtered one.

C-C  ATOM INDICATOR: M_C = Q 1_C Q, dropping the ball for the atom itself.
     volume = |C|_4 EXACTLY.
     D5:                 EXACT action-density form, trivially.
     T11 naturality:     HOLDS — indicators are exactly additive over any
                         partition, slivers included. This is the same
                         measure-additivity that made P-S2 land.
     R-L2b:              plausibly PROVABLE with exponent 1 by construction.
     *** THE FATAL COST: 1_C IS NOT 1_{|x| <= r(t)}. The light-cone tie is
     severed, M(t)'s support stops being a ball, and THE HUYGENS STRUCTURE
     A-L0 ARM 2 REQUIRES IS DESTROYED — the collar argument (shell count
     R^3 -> R^2) has no support to run on. It trades the
     highest-risk-of-never-closing item for the earliest-unmet
     prerequisite. ***

C-D  DIAMOND DECOMPOSITION: cover the atom with disjoint diamonds.
     volume:             ADDITIVE and equal to |C|_4 if the family tiles.
     Covering:           yes.
     Huygens:            PRESERVED per diamond — arm 2's mechanism survives.
     D5:                 satisfied, exactly.
     T11 naturality:     holds by additivity.
     R-L2b:              plausible.
     ON THE TECHNICAL CRITERIA THIS IS THE ONLY CANDIDATE THAT BREAKS
     NOTHING. ITS COSTS ARE OBLIGATIONS RATHER THAN CONTRADICTIONS:
       1. DIAMONDS DO NOT TILE. A general region is not a finite disjoint
          union of diamonds; a tiling needs countably many, or leaves gaps.
          Either is a new analytic obligation.
       2. THE NUMBER OF DIAMONDS GROWS WITH ASPECT RATIO (~A^3 for aspect
          ratio A). So "every cell runs at FULL tau_R" becomes "every cell
          runs ~A^3 record cycles". THE BASELINE BLOW-UP IS HARMLESS —
          a-independent content cancels in Z_comp(a)/Z_comp(0), which is
          exactly the result that refuted this lane's own P-S1 — BUT IT
          CONTRADICTS D2's SEALED WORDING, which says every cell runs one
          full cycle. That is a sealed-text conflict needing an amendment,
          not a silent reading.
       3. THE DECOMPOSITION IS NOT UNIQUE, so naturality requires a NEW
          obligation that does not exist today: DECOMPOSITION-INDEPENDENCE
          of the response.

THE STRUCTURE OF THE CHOICE, stated plainly because it IS the charter:
    C-A breaks EXTENSIVITY / the thermodynamic limit.
    C-B breaks D5.
    C-C breaks HUYGENS, hence A-L0 arm 2.
    C-D breaks NOTHING but adds THREE new obligations, one of which
        conflicts with sealed D2 text.
*** SO THE CHARTER IS NOT "PICK A DEFINITION". IT IS "CHOOSE WHICH SEALED
REQUIREMENT TO RENEGOTIATE, OR ACCEPT THREE NEW OBLIGATIONS INSTEAD." That
is why it is the principal's and not a lane's. ***
```

## 4 — Q4: WHICH CANDIDATES ARE NEW PRINCIPLES RATHER THAN DEFINITIONS

```text
DEFINITIONS (canonical, no free parameter, no new posited physics):
    C-A inscribed diamond.
    C-B circumscribed diamond.
NEW PRINCIPLE, FLAGGED:
    C-C atom indicator. It does not merely define a transport; it CHANGES
    THE SEALED FORM of A1/A2 by severing the light-cone tie. Dropping
    causality from the construction is a physics posit, not a bookkeeping
    choice.
MIXED, AND THE PRINCIPAL SHOULD SEE THE SPLIT:
    C-D diamond decomposition is a DEFINITION if the decomposition is
    canonical (e.g. a fixed dyadic scheme), and a NEW PRINCIPLE if it is
    not — because a non-canonical choice makes the response depend on an
    unphysical selection, and the decomposition-independence obligation
    would then be a new physical requirement rather than a lemma.
SEPARATELY, AND THIS ONE IS A HARD FLAG:
    *** ANSWERING P4 AS "tau_R IS A PHYSICAL DURATION" IS NOT A DEFINITION
    AT ALL. It would presuppose an ABSOLUTE PHYSICAL T_R — which is a NAMED
    PART-C BLOCKER, listed as an undischarged whole-program obligation
    (confirmed in COMPLETE_QSPEC_ABSOLUTE_SCALE_AND_CONTINUUM_PREREQUISITE_
    AUDIT_V001 and the Stage-7 review candidates), and contradicted by
    BID_MINIMAL_PUBLIC_CAUSAL_CELL's "a half-line of allowed durations and
    NO ABSOLUTE RECORD SCALE". Any charter branch that makes tau_R physical
    discharges a Part-C blocker by fiat. That is the one branch this lane
    would flag as inadmissible without a separate principal decision on the
    blocker itself. ***
```

## 5 — WHAT THIS DOES NOT DO

```text
IT DOES NOT UNBLOCK R-L2b, and is not to be treated as if it does. The
independent lane's R-L2b return stands: the bound class fails in the sliver
direction and the named missing estimate is real. Step 1 constrains what
R-L2b may be STATED OVER; it supplies no estimate. Under C-A the estimate
gets easier; under C-B it becomes impossible; under C-C and C-D it stays
open at roughly its present difficulty. THAT IS A CONSTRAINT ON THE
STATEMENT, NOT A PROOF.
IT DOES NOT NARROW D3. No shape condition is adopted or recommended.
IT DOES NOT RESOLVE C_ref/D3, which remains the principal's and is still
devalued on the restriction side by the earlier finding.
IT ADOPTS NOTHING. Four candidates, costed, none chosen.
```

## Protected status

```text
pins_reconciled = 5        (P1..P5; neither lane's list was complete)
pin_unique_to_this_lane = P3_minimum_separation
pins_unique_to_independent_lane = P4_tau_R_units, P5_diamond_on_nondiamond
five_pins_collapse_to_one_decision = true      (via the diamond constraint)
candidates_costed = 4
C_A_breaks = extensivity_thermodynamic_limit
C_B_breaks = D5_action_density
C_C_breaks = Huygens_hence_A_L0_arm2
C_D_breaks = nothing; adds_3_new_obligations; conflicts_with_sealed_D2_text
new_principle_flags = C_C; C_D_if_noncanonical; tau_R_as_physical_duration
tau_R_physical_branch = INADMISSIBLE_without_a_separate_Part_C_decision
charter_is_one_decision = true
charter_decides = which_sealed_requirement_to_renegotiate
option_adopted = none
R_L2b_unblocked = false
D3_narrowed = false
P_T1 = HIT ; P_T2 = HIT ; P_T3 = PARTIAL ; P_T4 = HIT
production_authorized = false
alpha_computed = false
proof_authorized = false
```
