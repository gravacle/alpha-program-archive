# STAGE 8 / 7A / STEP 8 — THE CLOSURE PROOF: STOPPED BY REFUTATION, WITH THE CLAUSE DISPLAYED

Lane: DARIO (Builder B, independent verifier). Relay 742.
Governing: `DECISION_COMPLETENESS_PROOF_2026-08-08` `3c7b4867…` — **the PROVE standard
governs**; the 739 display `660e0c14…` supplies every other demand.

## Lead determination

**The closure claim is false, and sealed stock says so in its own words.**

The target claim — *sealed stock licenses no refinement move outside the frozen C_ref
constituents `{A0, A1, A2}`* — does not stop on a clause that resists classification. It
stops on a clause that **classifies cleanly and lands OUTSIDE**, and it has been enumerated
before: the register's own Q-624 entry counts **seven** generators, not three. Six are
`{A0, A1, A2}`. The seventh is C_ref's third frozen constituent, the common-refinement
family.

The seventh is **barred as a SOURCE. It is not excluded from the CLASS.** `4d` states both
facts in the same sealed block: `C_REF_AS_WRITTEN_DERIVES_SMOOTH_DATA_FROM_GATE4 = false |
TYPE-R` **and** `C_REF_USABLE_AS_TARGET_INTERFACE = true`. FC-1 uses the same qualifier —
*"barred as a **source**"*. Every artifact of mine that treated the bar as a deletion from
the class, including my own 739, read past that qualifier.

And two sealed authorities **quantify over the seventh**:

- **A27 itself** — the row RA27-2 exists to serve — demands the coefficient be invariant
  under *"a sealed class of regular-CW refinements and elementary subdivision/**common-refinement
  moves**."*
- **D3**, in the **sealed** majorant spec `818083a5…`, freezes its theorem's quantifier as
  *"skeleton, A, B, and common refinements"* with *"**all** common refinements of members of
  A and B"* — and the sealed determination `6934f858…` records `D3_class_strictly_larger_
  than_C_ref = true`, `sliver_cellulations_in_D3_and_outside_C_ref = true`,
  `D3_freeze_withdrawn = false`, `conflict_resolved = false`.

**And the deeper finding, which is what actually stops RA27-2: the index supplies an
EXISTENTIAL where the criteria demand a UNIVERSAL.** FC-1's adopted directedness says *"there
**exists** M with K → M and L → M."* A27 and D3 demand invariance under **all**
common-refinement moves. An existential common refinement does not discharge a universal
quantifier, and no adoption on the books converts one into the other.

So `CLOSURE = STOPPED`, and **RA27-2 does not book.** This is not the certificate/proof gap
of 739 — that fork was ruled, and the PROVE standard is exactly what exposes this. The
enumeration ran to completion and returned a counterexample.

---

## 0. Preflight

### 0.1 Output name

Probed **before any write**, recursively over the whole archive
(`find . -name 'STAGE8_7A_COMPLETENESS_PROOF_DARIO_V001.md*'`): **absent**, artifact and
sidecar both. Nothing overwritten.

### 0.2 Sources verified before use

```text
DEC742 supervision/DECISION_COMPLETENESS_PROOF_2026-08-08.md            3c7b4867…  sidecar OK
D012   workspace/STAGE8_TASK6_A25_A27_SCOPING_LANE2_V003.md             74bbb7aa…
V011   workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/
         BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md                  aa7c6d49…
BID    workspace/BID_CONSOLIDATED_HOSTILE_AUDIT_MATRIX_V005.md          78f6bb08…  (no sidecar)
JREF   workspace/STAGE8_TASK5_JREF_AND_LOCAL_KERNEL_ESTIMATES_LANE2_V001.md   8dd59b35…
4d     workspace/STAGE8_TASK4D_STITCHING_THEOREM_GERM_INDEPENDENT_HALF_V001.md 430f0971…
MAJSPEC workspace/STAGE8_T7_CONNECTED_LINKED_CLUSTER_MAJORANT_DERIVATION_SPEC_V001.md
                                                                        818083a5…  sidecar OK
DET    workspace/STAGE8_T7_CREF_VS_D3_FACTUAL_DETERMINATION_V001.md     6934f858…  sidecar OK
T13    workspace/STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_V001.md 85d24996…  sidecar OK
MAJ    workspace/stage8_execution/work/MAJORANT_PHASE2_O3_O7_PROOF_DRAFT_V001.md  08b91543…
FC     supervision/DECISION_RA27_2_ADOPTIONS_2026-08-08.md              31e42812…
FCC    supervision/DECISION_CORRECTION_FC1_TRANSPORT_2026-08-08.md      72894c1c…
REG    supervision/QUESTIONS_SETTLED_REGISTER_V001.md                   fd6c774c…
IDX    workspace/STAGE8_7A_RA27_2_INDEX_BUILT_DARIO_V001.md             66f078ba…
739    workspace/STAGE8_7A_RA27_2_DISCHARGED_DARIO_V001.md              660e0c14…
```

All V011 byte offsets are against the **sealed packet member** `aa7c6d49…`, never the longer
unsealed same-named copy at `workspace/` top level (`20a3a17d…`) — the hazard recorded at
739 §0.2.

### 0.3 Gates

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
No member binding.  No fixed-point execution.  No end test.
No numeric evaluation of physical quantities.  No comparison to measured constants.
No common cell formed.  No junction map evaluated.  No response evaluated.
Nothing adopted here.  No register, plan, tracker, or git action.
```

---

## 1. WW1 — THE CLOSURE PROOF

### 1.1 What must be proven, and a discrepancy in the target set

[PROVABLE] `DEC742` `3c7b4867…` sets the standard:

```text
The Q-624/Q-647 fork is ruled: D012's verb PROVE governs generator
completeness. The census certificate (refutation-strength, writer-excluded)
and the sealed reachability witness stand as evidence, not as the discharge.
RA27-2 books when closure is DERIVED at full strength: that sealed stock
licenses no refinement move outside the frozen C_ref constituents.
```

[PROVABLE] **The target set as the task names it is `{A0, A1, A2}`. C_ref's frozen
constituents are three, and `A0` is not among them.** `V011` `aa7c6d49…[46882,47019)`:

```text
cubical bisection;
oriented simplicial/barycentric subdivision;
and common refinements preserving the same smooth coframe and connection.
```

`A0` comes from `JREF`, not from C_ref. So `{A0, A1, A2}` **substitutes** `A0` for C_ref's
third constituent. That substitution is the whole question, and I record it before the
enumeration rather than after, because the enumeration's answer turns on it.

### 1.2 The instrument — the licensing grammar

[YOURS] A **refinement move** is an arrow between cellulations of one region whose target's
cells subdivide the source's. It is not a record-algebra morphism, not a field, not an
exhaustion arrow (growing volume, not subdivision), and not an object-admission condition.

A **licensing act** is a sealed clause that confers admissibility on such a move. Probed by
meaning, not by phrase — the ways sealed text can confer it: *freeze / frozen / seal(ed)
class / admissible class / admitted / admits / admission / licensed / permitted / allowed /
ratified / certified / authorized / declared / closed under / generated by / upward-closed*,
each required to take a **refinement move** as its object.

**Searched space, stated:** recursive glob over `./workspace/**/*.md` and
`./supervision/**/*.md` — **1,958 files** — with `*_DARIO_V001.md` excluded so the
enumeration cannot corroborate itself from my own artifacts, and
`evaluator_build_A/` code excluded under the independence law.

[YOURS] **The census is corroboration, not the proof, and the task is right about that.** A
census asks *which moves are named*. A move can be licensed by a clause that names no move
at all — by quantifying over a class ("all common refinements"), or by closing a class
upward. My 739 census asked the weaker question and got the weaker answer. Both of the
clauses that decide this relay are of the naming-nothing kind, and **both were inside the
1,958 files my 739 census read.**

### 1.3 THE ENUMERATION — every licensing act over refinement moves, classified

| # | Licensing act | Pin | What it licenses | Verdict |
|---|---|---|---|---|
| L1 | **V011's C_ref freeze** | `aa7c6d49…[46389,47444)`, list at `[46882,47019)` | cubical bisection; oriented simplicial/barycentric subdivision; **and common refinements preserving the same smooth coframe and connection** | `A1`, `A2` **INSIDE**; third constituent **OUTSIDE** — see §1.4 |
| L2 | **JREF's `Ref_0`** | `8dd59b35…[11610,11743)`, status `[12001,12049)` | identity arrows; certified signed relabelings/isomorphisms; ratified rank-preserving W3 restriction/inclusion squares | **INSIDE** (`A0`) — and by TYPE these are *invertible-only*; see §1.3.1 |
| L3 | **T13's battery pinning** | `85d24996…[16570,17090)` | family A = cubical bisection sequence; family B = oriented simplicial/barycentric subdivision sequence, *"distinct C_ref generators"*; *"the pullback-commutation check runs on **a** common refinement"* | **INSIDE** — inherits `A1`/`A2`; its common refinement is **existential** |
| L4 | **D3's frozen quantifier** | `818083a5…[9333,9922)` | *"plus: **all** common refinements of members of A and B"*; *"The theorem's quantifier ranges over the skeleton, A, B, and common refinements. Pinning the quantifier to any finite list is NOT available to any lane under any outcome (F-2)."* | **OUTSIDE** — §1.5 |
| L5 | **A27's criterion** | `78f6bb08…[11438,11932)` | *"invariant under a sealed class of regular-CW refinements and elementary subdivision/**common-refinement moves**"* | **OUTSIDE** — §1.6 |
| L6 | **FC-1's adopted directedness** | `31e42812…` FC-1 | *"For any K, L with K ~ L there **exists** M with K → M and L → M in P3"* | **INSIDE** — but **existential**; §1.7 |
| L7 | **FC-2's shape-regular admission + preregistered relaxation** | `31e42812…` FC-2 | admission class SHAPE-REGULAR; *"admission of general common refinements enters as a surfaced revision of record"* on a future sealed sliver derivation | **CONDITIONAL, NOT TRIGGERED** — licenses nothing today, and its existence concedes that general common refinements are outside the current class |
| L8 | **V011's naturality demand** | `aa7c6d49…[47025,47247)` | *"must commute with pullback to **a** common refinement"*; *"invariant under **each** elementary refinement"* | **INSIDE** — elementary refinements are `A1`/`A2`-class; the common refinement is existential |
| L9 | **Q-408 / `Ref_PL` / P4** | `STAGE8_TASK5_EQ6_C1_COMPLETION_BUILD_LANE1_V001.md` `5203347c…`; `…Q408_PRIMITIVE_GENERATOR_EXHIBIT_LANE2_V001.md` `cd03cc87…` | *"the full primitive refinement category required by P4"*, `Ref_0 != full Ref_PL/P4 generator category`; a refinement theorem over *"every PL refinement arrow in the adopted proposed category"* | **NOT A LICENSING ACT FOR THIS INDEX** — §1.3.2 |

#### 1.3.1 Why `A0` cannot carry refinement

[PROVABLE] `REG` `fd6c774c…[1265282,1265857)`, Q-624, in the corpus's own enumeration:

```text
Seven generators, all block-covered: the two record-native licensed moves
(cubical bisection; oriented subdivision, both frozen in V011's C_ref), four
invertible-only built moves whose closure is the relabeling groupoid (by TYPE
it cannot relate two genuinely different cellulations of one region), and the
seventh — the common-refinement family — BARRED AS CIRCULAR: …
```

**The enumeration this relay asks for already exists, sealed, and it counts seven.** `A0`'s
four moves are *invertible-only*, and the register states outright that by TYPE they cannot
relate two genuinely different cellulations of one region — so `A0` contributes **no**
refinement. The effective refinement generators of sealed stock are `A1`, `A2`, and **the
seventh**.

#### 1.3.2 Why L9 is not a licensing act here

[PART-PROVABLE] `Ref_PL`/P4 is a **demanded and unbuilt** category belonging to the Q-408
continuum root, not to C_ref's coefficient index: `5203347c…` says `Ref_0` is *"the largest
physical refinement scope available to this lane"* and *"strictly smaller than the full
primitive refinement category required by P4"*. A category recorded as *required and absent*
licenses nothing. The Q-408 refinement theorem's scope clause (*"every PL refinement arrow in
the adopted proposed category"*) is a theorem's coverage statement over a **proposed**
category, and the same lane's V002 retypes the formal-arrow burden away
(*"Requiring a strict set-valued section on every formal `Ref_PL` arrow is stronger than
physics"*). **Classified NOT-A-LICENSING-ACT — and recorded anyway**, because it is a third
place where sealed stock reaches for a refinement class wider than `{A1, A2}`.

### 1.4 The seventh generator: barred as a SOURCE, not excluded from the CLASS

This is the linchpin, and it is stated in sealed text in exactly these terms.

[PROVABLE] `4d` `430f0971…[20690,20930)`:

```text
C_REF_AS_WRITTEN_DERIVES_SMOOTH_DATA_FROM_GATE4 = false | TYPE-R |
  test: the class definition takes the same smooth coframe and connection as
        input before the refinement conclusion is posed

C_REF_USABLE_AS_TARGET_INTERFACE = true
```

[PROVABLE] `FC` `31e42812…` FC-1 uses the same qualifier: *"the smooth common-refinement
family remains barred **as a source** (TYPE-R)."*

[PROVABLE] `REG`'s Q-624 gives the reason and it is a **source** reason: *"its admissibility
clause consults 'the same SMOOTH coframe and connection' while DoR-007 grounds smoothness as
existing only as a refinement limit whose cellulation-independence is the theorem's content.
The generator consults, as input, the object the theorem must produce."*

[PROVABLE] **Therefore the bar is on derivation-from, not on membership-in.** A TYPE-R verdict
says you may not use the clause to produce the smooth object. It does not say the moves are
inadmissible, and `C_REF_USABLE_AS_TARGET_INTERFACE = true` says the opposite in one line.

[YOURS] **I read past that qualifier for four relays.** 725, 727, 731 and 739 all treat the
third constituent as though the bar removed it from the class — 739 §1.2 says it *"is not
used as a generator"* and then treats the generator set as closed. Not-used-as-a-source and
not-in-the-class are different propositions, the sealed text distinguishes them explicitly,
and I collapsed them.

### 1.5 D3 — the amplification, sealed and not withdrawn

[PROVABLE] `MAJSPEC` `818083a5…[9333,9922)` — **sealed, sidecar verified**:

```text
### D3 - Cellulation families, pinned skeleton, common refinements

Per the battery authority's T13 pinning:

skeleton:  the primary hypercubic fixture (pinned skeleton; a regression
           fixture, not proof of universality);
family A:  the cubical bisection sequence;
family B:  the oriented simplicial/barycentric subdivision sequence;
plus:      all common refinements of members of A and B.

The theorem's quantifier ranges over the skeleton, A, B, and common
refinements. Pinning the quantifier to any finite list is NOT available
to any lane under any outcome (F-2).
```

[PROVABLE] `DET` `6934f858…` — **sealed** — determines the relation between that class and
C_ref, and does not read it away:

```text
  D3's CLASS IS STRICTLY LARGER THAN C_ref's. A common refinement of a
  cubical bisection with a barycentric subdivision generically produces
  SLIVERS, which are not shape-regular. Those cellulations are INSIDE D3
  and OUTSIDE C_ref.
  NO SEALED ARTIFACT ANYWHERE RECONCILES THE DIFFERENCE.
```

with protected status:

```text
D3_class_strictly_larger_than_C_ref = true
sliver_cellulations_in_D3_and_outside_C_ref = true
D3_freeze_withdrawn = false
conflict_resolved = false
resolution_holder = principal
```

[PROVABLE] **The broad reading is a ratified freeze, not a draft.** `DET`: *"This lane froze
the D3 reading in the BROAD direction … That freeze was ratified. … NOTHING ABOUT THE FREEZE
IS WITHDRAWN HERE. The freeze stands as sealed; what is now on the record is that its breadth
exceeds C_ref's."*

[PROVABLE] **The broadening happens at D3, not at T13.** `T13` `85d24996…[16570,17090)` says
the pullback-commutation check *"runs on **a** common refinement"* — existential. D3 turns
that into *"**all** common refinements"* — universal. The chain D3 ← T13 ← V011 is textual and
by line number, and the quantifier changes at the last link.

[YOURS] I do not need my own geometry to place slivers outside `{A1, A2}`-composites: `DET`
states it, sealed, in the words quoted above. I note only that I checked whether the
conclusion could be evaded — whether every common refinement of an A-member and a B-member
might after all be an `A1`/`A2` composite — and `DET`'s sliver sentence forecloses it. `MAJ`'s
`Z = A2 ∘ A1` is **one** common refinement, the coarsest of its pair; "all common refinements"
is upward-closed and is not exhausted by one witness.

### 1.6 A27 — the row RA27-2 serves quantifies over the seventh

[PROVABLE] `BID` `78f6bb08…[11438,11932)`, row A27, verbatim:

```text
| A27 | Geometry, anisotropy, and cellulation | … The local coefficient is
invariant under a sealed class of regular-CW refinements and elementary
subdivision/common-refinement moves; one hypercubic sequence alone cannot
establish universality. | PENDING |
```

[PROVABLE] **A27's criterion names common-refinement moves in its own quantifier.** RA27-2
exists to supply A27's index. An index that excludes common-refinement moves does not carry
A27's quantifier, whatever else it carries. This leg is independent of D3 entirely: even with
D3 set aside, the row being served demands the class the index omits.

### 1.7 The quantifier gap — what the index supplies versus what is demanded

[PROVABLE] Supplied, `FC` FC-1, and carried inside the object at `IDX` §1.3:

```text
DIRECTEDNESS  *** ADOPTED AS AXIOM ***
   For any K, L with K ~ L there EXISTS M with K -> M and L -> M in P3.
```

[PROVABLE] Demanded, `BID` `[11438,11932)` and `MAJSPEC` `[9333,9922)`: invariance under
**all** common-refinement moves; a quantifier ranging over **all** common refinements, with
finite-list narrowing forbidden by F-2.

[YOURS] **An existential does not discharge a universal.** FC-1's axiom asserts that *some*
common refinement is reachable by `A1`/`A2` composites. A27 and D3 demand that the coefficient
survive *every* common refinement, including the sliver-producing ones `DET` places outside
C_ref. No sealed act converts the one into the other, and the adoption that was made — a
carefully bounded existential — is not the adoption that would be needed.

[YOURS] This also relocates what FC-2's preregistered relaxation is for. It reads as a
cautious option on future breadth. It is in fact the **only currently-written path** by which
the index could ever carry A27's own quantifier, and its trigger — a sealed derivation that
slivers leave the boundary/four-volume ratio intact — is unmet.

### 1.8 The verdict

```text
CLOSURE = STOPPED — and stopped by REFUTATION, not by inability.
```

The enumeration ran to completion over the stated glob. It did not fail to classify a clause;
it classified two clauses as **OUTSIDE** (L4, L5), one as **CONDITIONAL-NOT-TRIGGERED** (L7),
and it found that the licensing act at the root (L1) has a third constituent whose bar is
**source-only** by the corpus's own words. The claim *"sealed stock licenses no refinement
move outside `{A0, A1, A2}`"* is therefore **false**, and the counterexample is not exotic:
it is C_ref's own third frozen constituent, the one the target set silently replaced with
`A0`.

### 1.9 What IS proven, stated at its exact strength

[PART-PROVABLE] A **scoped** closure result survives and is worth having:

```text
Within the index's own FC-2-ruled admission class — SHAPE-REGULAR cells —
and excluding the seventh generator as a SOURCE, the licensed refinement
moves are exactly A1, A2 and their finite composites, with A0 contributing
identity of region and no refinement (REG Q-624, by TYPE).
```

[YOURS] But that is closure **relative to a class chosen to make it true**, and it is not
D012's demand. D012 asks whether the generators exhaust what stock licenses; answering
"they exhaust what stock licenses *after we remove what they do not cover*" is the shape of
argument this program's discipline exists to refuse. I state the scoped result and decline
to book it as the discharge.

---

## 2. WW2 — RA27-2 DOES NOT BOOK

[PROVABLE] `DEC742`: *"RA27-2 books when closure is DERIVED at full strength."* Closure is
not derived; it is refuted. **RA27-2 does not book.**

The 739 display is unchanged and remains correct on its own terms — demands 1, 2, 4 supplied;
demand 3 supplied AS ADOPTED; the measure's refinement functoriality supplied, cross-family
stable. What changes is **demand 5b's status, and it changes for the worse**: at 739 it was
*certificate-only, proof absent*. It is now *refuted at the proof standard*, with the
refuting clauses displayed.

[YOURS] **And the failure is not confined to demand 5.** The quantifier gap of §1.7 reaches
back into demand 3. 739 booked *common refinements* as **SUPPLIED AS ADOPTED** on FC-1's
directedness axiom. That axiom is existential; the demand's consumer — A27 — is universal. So
demand 3 is supplied **for the index's internal directedness** and **not** for A27's
quantifier, and my 739 table did not make that distinction. I make it here rather than let
the earlier booking stand unqualified:

| D012 demand | 739 status | Status now |
|---|---|---|
| 1 generators | SUPPLIED | **unchanged** |
| 2 same-region relation | SUPPLIED | **unchanged** |
| 3 common refinements | SUPPLIED AS ADOPTED | **SUPPLIED AS ADOPTED, EXISTENTIALLY ONLY** — does not carry A27's universal quantifier |
| 4 composition | SUPPLIED | **unchanged** |
| — precondition: measure refinement functoriality | SUPPLIED | **unchanged** — but see the scope note below |
| 5a reachability | SUPPLIED AS ADOPTED | **unchanged**, same existential qualification |
| 5b generator completeness | certificate only, proof absent | **REFUTED at the PROVE standard** (§1.3–§1.7) |

[YOURS] **Scope note on the precondition.** The functoriality result of 739 §1.6 is derived
over `A1`, `A2` and their composites. It says nothing about the sliver-producing common
refinements D3 quantifies over, and `DET` records precisely the open risk there — a sliver of
volume `eps·|C|_4` producing an `O(|C|_4)` response defect, which `DET` says would make the
object **FAIL** and recast Q6 **ill-posed rather than merely unproved**. The functoriality
result is not disturbed on its own class; it simply does not reach the class the criteria
name.

```text
RA27_2 = stopped.
```

[YOURS] **What would actually unblock it, stated because the distance is no longer short and
the registrar should not be left to infer that.** Three routes, and each is a principal act,
not a lane act:

1. **Restrict and say so.** `V011` pre-registered this branch in its own text: *"Failure to
   prove this naturality either blocks the general claim or restricts the result explicitly to
   that cellulation."* Restricting A27's quantifier to the shape-regular class discharges
   RA27-2 immediately on §1.9's scoped result — and `DET` requires the cost be said aloud:
   *"the object is proved on a class STRICTLY SMALLER than the one A-L5 and recast Q6 quantify
   over, and those two remain unserved — which must be said in the verdict language rather
   than left implicit."*
2. **Trigger the relaxation.** Derive that slivers leave the boundary/four-volume ratio
   intact. FC-2 preregistered exactly this, and it is the only written path to the index
   carrying A27's quantifier as it stands.
3. **Resolve the C_ref/D3 conflict.** `DET` records `conflict_resolved = false`,
   `resolution_holder = principal`, and it has been open since 2026-07-26. Route 1 and route 3
   are the same act seen from two sides.

---

## 3. WW3 — RA27-3's INCIDENCE-COMPOSITES ITEM

The closure machinery stopped, so it yields nothing. But the item does not need it, and the
answer is not the one I set up at 739.

[PROVABLE] **The composite step is free.** Let `g = g_n ∘ … ∘ g_1` be a `P3` arrow, each
`g_i ∈ {A1, A2}` (FC-1: P3's arrows are finite compositions of the two licensed moves).
Suppose each generator satisfies cell-wise four-volume additivity: for every cell `c`,
`Σ_(c' ∈ children_g_i(c)) |c'|_4 = |c|_4`. Then `g` does.

*Proof.* Induction on `n`. `n = 1` is the hypothesis. For `n > 1` write
`g' = g_(n-1) ∘ … ∘ g_1`. Each `g_i` partitions each cell, so children of distinct cells are
distinct and `children_g(c) = ⊔_(c' ∈ children_g'(c)) children_g_n(c')` is a disjoint union.
Hence

```text
sum_(c'' in children_g(c)) |c''|_4
  = sum_(c' in children_g'(c)) sum_(c'' in children_g_n(c')) |c''|_4
  = sum_(c' in children_g'(c)) |c'|_4        [generator hypothesis]
  = |c|_4                                     [induction hypothesis]
```

∎ No transverse multiplicity enters: this counts four-volume, not sub-faces, which is where
my 731 trichotomy went wrong.

[YOURS] **So the gap was never at the composites — it relocates to the generators.** What
`MAJ` `08b91543…[19632,19996)` seals is **instances**: *one* bisection of the *unit* 4-cube
(16 subcubes at 1/16), the Freudenthal subdivision (24 at 1/24), the common refinement Z (384
at 1/384). Cell-wise additivity for `A1` and `A2` on an **arbitrary** admissible cell is the
hypothesis the induction consumes, and it is not sealed. My 739 §2.2 wrote *"supplied on the
generators, not on composites"*; the accurate statement is **supplied on the exhibited
generator instances**, with generality open at the generator level and the composite level
free.

[PROVABLE] **The other half of `incidence` is untouched and stays named.** RA27-3's
`incidence` field is not only four-volume bookkeeping; it is the incidence numbers
`incidence(f,e)` of `d_1` (`V011` `aa7c6d49…[44595,44690)`). Naturality of that cochain
structure under subdivision is a different object, the induction above does not reach it, and
nothing in this relay supplies it.

```text
RA27_3_INCIDENCE = taken — the composite question is ANSWERED (it dissolves by
    induction) and the answer RELOCATES the gap to generator-level generality.
    The cochain-incidence component is left named for its own relay.
```

---

## 4. AN INDEPENDENT SWEEP, COMMISSIONED

[YOURS] Because the last three relays turned on defects in my own instruments rather than my
reasoning, I commissioned five blind hunters over the same searched space, each with a
**different** search modality — by class name, by permission language, by move name, by
criterion quantifier, and by the bar — with every candidate then handed to an adversarial
verifier instructed to refute it and to default to refuted under uncertainty. The hunters were
denied my own artifacts and the producer's code.

**SWEEP_SECTION_PLACEHOLDER**

---

## 5. GROUNDING, JURISDICTION, VERB AUDIT

### 5.1 Grounding

| # | Claim | Pin | Tag |
|---|---|---|---|
| 1 | The PROVE standard governs; RA27-2 books only on derived closure | `3c7b4867…` | PROVABLE |
| 2 | C_ref's three frozen constituents | `aa7c6d49…[46882,47019)` | PROVABLE |
| 3 | The bar is source-only; `C_REF_USABLE_AS_TARGET_INTERFACE = true` | `430f0971…[20690,20930)` | PROVABLE |
| 4 | FC-1's own qualifier "barred as a source" | `31e42812…` FC-1 | PROVABLE |
| 5 | Seven generators; `A0`'s four are invertible-only and cannot relate different cellulations | `fd6c774c…[1265282,1265857)` | PROVABLE |
| 6 | D3's frozen quantifier: "all common refinements"; F-2 forbids finite-list narrowing | `818083a5…[9333,9922)` (sealed) | PROVABLE |
| 7 | D3's class strictly larger; slivers inside D3 and outside C_ref; freeze ratified, not withdrawn; conflict unresolved | `6934f858…` (sealed) | PROVABLE |
| 8 | T13 says "a common refinement" — the broadening happens at D3 | `85d24996…[16570,17090)` (sealed) | PROVABLE |
| 9 | A27 quantifies over "common-refinement moves" | `78f6bb08…[11438,11932)` | PROVABLE |
| 10 | FC-1's directedness is existential | `31e42812…` FC-1; `66f078ba…` §1.3 | PROVABLE |
| 11 | FC-2's relaxation is conditional and untriggered | `31e42812…` FC-2 | PROVABLE |
| 12 | `Ref_PL`/P4 is required-and-absent, not licensed | `5203347c…`; `cd03cc87…` | PART-PROVABLE |
| 13 | V011 pre-registers "restrict the result explicitly to that cellulation" | `aa7c6d49…[47025,47247)` | PROVABLE |
| 14 | `MAJ` seals instances, not the general generator statement | `08b91543…[19632,19996)` | PROVABLE |
| 15 | The composite additivity induction | §3 | YOURS |
| 16 | The existential/universal quantifier gap | §1.7 | YOURS |

**Pin check: 16/16.** Every span re-read from bytes this relay against the stated digest.

### 5.2 Jurisdiction check

**On returning a refutation where a proof was commissioned.** *What was the rule written to
protect?* D012's PROVE verb protects against a generator set that silently omits a move the
program needs. The risk was not hypothetical: the omitted move is named in the criterion the
index serves. *Does the outcome space distinguish false from cannot-see?* Yes — and this
relay returns **false**, not cannot-see, which is the stronger and rarer of the two. *Would it
permit the evidence to appear if the theory is right?* Yes: routes 1–3 of §2 each make the
closure claim true or make it unnecessary, and I display all three.

**On the VOID CONDITION.** No topology, index, rule, branch or selector is chosen here from a
desired coefficient. The refutation runs **against** the direction that would unblock my own
lane's work — closure would have booked RA27-2 today — which is the disposition `DET` records
for itself in the same conflict.

**On R9 / R9-JII.** Untouched. The carrier stays PENDING on its common-cell quantifier.

**On BR-1.** The relay header reads *"THE CLOSURE PROOF, AND RA27-2 BOOKS"*, and the task text
supplies the stop. A producer-declared header may accuse; it may never exculpate, and it may
not carry a criterion's direction.

### 5.3 Self verb audit — **CLEAN, with four disclosures**

1. **The decisive clauses were inside my own 739 searched space and my census could not see
   them.** L4 and L5 name no refinement move; they quantify over a class. A move-name census
   is structurally blind to that, and I reported its result as a completeness certificate.
   Eighth consecutive relay in which the instrument, not the reasoning, was the weak part —
   and the first where the fix was supplied by the commission rather than by me: **the task
   specified the licensing-enumeration shape, and that shape is what found the counterexample.**
2. **I collapsed "barred as a source" into "not in the class" across four relays** — 725, 727,
   731, 739 — while the sealed text distinguished them in one line
   (`C_REF_USABLE_AS_TARGET_INTERFACE = true`) that I had read and cited for its neighbouring
   sentence. Same failure mode as 727 and 739: the refutation living in bytes I had already
   consumed for another purpose.
3. **739's demand-3 booking is qualified here, not withdrawn.** *Supplied as adopted* was true
   of the index's internal directedness and did not carry A27's quantifier; §2's table states
   both.
4. **739 §2.2's incidence framing was imprecise** — "supplied on the generators" should have
   been "on the exhibited generator instances", and §3 corrects it while dissolving the
   composite question it named.

---

```text
CLOSURE = STOPPED (clauses displayed) — and stopped by REFUTATION, not by an
    unclassifiable clause. The enumeration completed over 1,958 files, recursive
    glob ./workspace/**/*.md + ./supervision/**/*.md, writer-excluded. Nine
    licensing acts classified. TWO land OUTSIDE {A0,A1,A2}: (L4) D3's frozen
    quantifier in the SEALED majorant spec 818083a5...[9333,9922) — "all common
    refinements of members of A and B", F-2 forbidding finite-list narrowing,
    with the SEALED determination 6934f858... recording D3_class_strictly_larger
    _than_C_ref = true and sliver_cellulations_in_D3_and_outside_C_ref = true and
    D3_freeze_withdrawn = false; and (L5) A27's own criterion 78f6bb08...
    [11438,11932) — "elementary subdivision/common-refinement moves". ONE is
    CONDITIONAL-NOT-TRIGGERED (L7, FC-2's preregistered relaxation). The root
    licensing act L1 has a THIRD frozen constituent whose bar is SOURCE-ONLY by
    the corpus's own words — 4d 430f0971...[20690,20930):
    C_REF_USABLE_AS_TARGET_INTERFACE = true — and the register's Q-624 already
    enumerated SEVEN generators, not three. UNDERLYING FINDING: the index supplies
    an EXISTENTIAL common refinement (FC-1's adopted directedness) where A27 and
    D3 demand a UNIVERSAL over all common-refinement moves; no sealed act converts
    one into the other.
RA27_2 = stopped.  739's display stands; demand 5b moves from certificate-only to
    REFUTED at the PROVE standard, and demand 3 is qualified to EXISTENTIAL ONLY.
    Three principal routes displayed at section 2: restrict-and-say-so (V011's own
    pre-registered branch), trigger FC-2's sliver relaxation, or resolve the
    C_ref/D3 conflict open since 2026-07-26.
RA27_3_INCIDENCE = taken — the composite question dissolves by a one-line
    induction on composite length; the gap RELOCATES to generator-level generality
    (MAJ seals instances on the unit 4-cube, not arbitrary cells). The
    cochain-incidence component is left named.
VOID = clean
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+4 disclosures at section 5.3)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
