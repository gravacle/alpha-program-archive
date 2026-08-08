# STAGE 8 / 7A / STEP 8 — THE CLOSURE PROOF: STOPPED BY REFUTATION, WITH THE CLAUSE DISPLAYED

Lane: DARIO (Builder B, independent verifier). Relay 742.
Governing: `DECISION_COMPLETENESS_PROOF_2026-08-08` `3c7b4867…` — **the PROVE standard
governs**; the 739 display `660e0c14…` supplies every other demand.

## Lead determination

**The closure claim is false, and the refuting clause is the root licensing act itself.**

`V011` performs one admissibility act over refinement moves — *"Freeze an admissible class
`C_ref` … **with**: cubical bisection; oriented simplicial/barycentric subdivision; **and
common refinements preserving the same smooth coframe and connection**."* Three items. Items
one and two are `A1` and `A2`. Item three is not `A0`; `A0` comes from `JREF`, not from
C_ref. The target set `{A0, A1, A2}` **substitutes `A0` for C_ref's third constituent**, and
that substitution is the entire question.

**The third constituent is barred as a SOURCE. It is not excluded from the CLASS**, and
sealed text says both things in one block — `4d` `430f0971…[20690,20930)`:
`C_REF_AS_WRITTEN_DERIVES_SMOOTH_DATA_FROM_GATE4 = false | TYPE-R` **and**
`C_REF_USABLE_AS_TARGET_INTERFACE = true`. FC-1 uses the same qualifier: *"barred **as a
source**."* A TYPE-R verdict forbids deriving *from* a clause; it does not delete the moves
from the class it froze.

The register already counted this. `REG` Q-624: *"**Seven generators**, all block-covered:
the two record-native licensed moves …, **four invertible-only built moves** whose closure is
the relabeling groupoid (by TYPE it cannot relate two genuinely different cellulations of one
region), and **the seventh — the common-refinement family — BARRED AS CIRCULAR**."* Six are
`{A0, A1, A2}`; `A0`'s four carry no refinement at all by TYPE. **The seventh is the answer,
and the enumeration was already on the books.**

Corroborating, and independent of everything above: **A27 — the row RA27-2 exists to serve —
quantifies over the moves in question**, in a sealed instance: *"invariant under a sealed
class of regular-CW refinements and elementary subdivision/**common-refinement moves**."*

**And the finding underneath, which is what actually stops RA27-2: the index supplies an
EXISTENTIAL where the criteria demand a UNIVERSAL.** FC-1's adopted directedness says *"there
**exists** M with K → M and L → M."* A27 demands invariance under **all** common-refinement
moves. No sealed act converts one quantifier into the other, and the adoption that was made
is not the adoption that would be needed.

So `CLOSURE = STOPPED` — by **refutation**, not by an unclassifiable clause — and **RA27-2
does not book.** The enumeration ran to completion and returned a counterexample.

---

## 0. Preflight

### 0.1 Output name

Probed **before any write**, recursively over the whole archive
(`find . -name 'STAGE8_7A_COMPLETENESS_PROOF_DARIO_V001.md*'`): **absent**, artifact and
sidecar both. Nothing overwritten.

### 0.2 Sources verified before use

```text
DEC742 supervision/DECISION_COMPLETENESS_PROOF_2026-08-08.md              3c7b4867…  SEALED-OK
D012   workspace/STAGE8_TASK6_A25_A27_SCOPING_LANE2_V003.md               74bbb7aa…
V011   workspace/review_packets/STAGE7_QSPEC_CANDIDATE_V001/
         BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md                    aa7c6d49…  (packet-manifest sealed)
A27s   workspace/STAGE8_TASK6_LP_MATRIX_LEDGER_LANE3_V001.md              bc6c3e49…  SEALED-OK
BID    workspace/BID_CONSOLIDATED_HOSTILE_AUDIT_MATRIX_V005.md            78f6bb08…  NO SIDECAR
JREF   workspace/STAGE8_TASK5_JREF_AND_LOCAL_KERNEL_ESTIMATES_LANE2_V001.md 8dd59b35…
4d     workspace/STAGE8_TASK4D_STITCHING_THEOREM_GERM_INDEPENDENT_HALF_V001.md 430f0971…
MAJSPEC workspace/STAGE8_T7_CONNECTED_LINKED_CLUSTER_MAJORANT_DERIVATION_SPEC_V001.md
                                                                          818083a5…  SEALED-OK
D3FRZ  workspace/STAGE8_T7_D3_QUANTIFIER_READING_FREEZE_AND_LEMMA_CONSUMPTION_V001.md
                                                                          9a0c2045…  SEALED-OK
D3RAT  workspace/STAGE8_T7_D3_FREEZE_RATIFICATION_AND_PREDICTION_WEIGHTING_RULE_V001.md
                                                                          c373adba…  SEALED-OK
DET    workspace/STAGE8_T7_CREF_VS_D3_FACTUAL_DETERMINATION_V001.md       6934f858…  SEALED-OK
SLIV   workspace/STAGE8_T7_SLIVER_NATURALITY_ATTEMPT_RESULT_V001.md       218be86d…  SEALED-OK
T13    workspace/STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_V001.md   85d24996…  SEALED-OK
MAJ    workspace/stage8_execution/work/MAJORANT_PHASE2_O3_O7_PROOF_DRAFT_V001.md  08b91543…
FC     supervision/DECISION_RA27_2_ADOPTIONS_2026-08-08.md                31e42812…
FCC    supervision/DECISION_CORRECTION_FC1_TRANSPORT_2026-08-08.md        72894c1c…
REG    supervision/QUESTIONS_SETTLED_REGISTER_V001.md                     12cbcb6c…  SEALED-OK
IDX    workspace/STAGE8_7A_RA27_2_INDEX_BUILT_DARIO_V001.md               66f078ba…
739    workspace/STAGE8_7A_RA27_2_DISCHARGED_DARIO_V001.md                660e0c14…
```

**Three grounding hazards, disclosed.**

1. **`REG`'s digest changed during this relay** — `fd6c774c…` at the start, `12cbcb6c…` now,
   seal current in both cases. It is append-only, and I **re-located both cited spans against
   the new bytes** rather than assuming they held: Q-624 at `[1265282,1265857)` and the
   certificate fork at `[1261941,1262121)`, unchanged. A digest change on an append-only file
   invalidates nothing before the append — but only a re-read establishes that.
2. **`BID` `78f6bb08…` carries no seal sidecar.** A27's criterion is therefore cited from the
   **sealed** instance `A27s` `bc6c3e49…[37467,37661)`, verbatim identical.
3. **`V011`'s packet copy carries no adjacent sidecar**; its seal is membership in
   `STAGE7_PACKET_MANIFEST_V001.sha256`, which lists `aa7c6d49…`. All V011 offsets here are
   against that copy, never the longer unsealed same-named file at `workspace/` top level
   (`20a3a17d…`).

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

[PROVABLE] `DEC742` `3c7b4867…`:

```text
The Q-624/Q-647 fork is ruled: D012's verb PROVE governs generator
completeness. … RA27-2 books when closure is DERIVED at full strength: that
sealed stock licenses no refinement move outside the frozen C_ref constituents.
```

[PROVABLE] **C_ref's frozen constituents are three, and `A0` is not one of them.** `A0` is
`JREF`'s `Ref_0` (`8dd59b35…[11610,11743)`), a different authority. The task's target set
`{A0, A1, A2}` therefore silently trades C_ref's third constituent for an import. I record
this before the enumeration, because the enumeration's answer turns on it.

### 1.2 The instrument — the licensing grammar

[YOURS] A **refinement move** is an arrow between cellulations of one region whose target's
cells subdivide the source's. Not a record-algebra morphism, not a field, not an exhaustion
arrow (growing volume, not subdivision), not an object-admission condition.

A **licensing act** is a sealed clause that confers admissibility on such a move. Probed by
meaning: *freeze / frozen / sealed class / admissible class / admitted / admits / admission /
licensed / permitted / allowed / ratified / certified / authorized / declared / closed under
/ generated by / upward-closed*, each required to take a **refinement move** as its object.

**Searched space, stated:** recursive glob over `./workspace/**/*.md` and
`./supervision/**/*.md` — **1,958 files** by my recipe — `*_DARIO_V001.md` excluded so the
enumeration cannot corroborate itself, and `evaluator_build_A/` code excluded under the
independence law.

[YOURS] **The task is right that the census is corroboration, not the proof, and this is why
739's census could not have found this.** A census asks *which moves are named*. The refuting
clause names its move in a list of three and is invisible to a move-name probe precisely
because the probe was looking for *new* names, and this one is the name I had already
classified as barred. A licensing enumeration asks a different question — *what confers
admissibility* — and that is the question that finds it.

### 1.3 THE ENUMERATION — every licensing act over refinement moves, classified

| # | Licensing act | Pin | Verdict |
|---|---|---|---|
| **L1** | **`V011`'s C_ref freeze** — *"Freeze an admissible class `C_ref` … with: cubical bisection; oriented simplicial/barycentric subdivision; and common refinements preserving the same smooth coframe and connection."* | `aa7c6d49…[46772,47023)` | `A1`,`A2` **INSIDE**; **third constituent OUTSIDE** — §1.4 |
| **L2** | **`JREF`'s `Ref_0`** — identities; certified signed relabelings/isomorphisms; ratified rank-preserving W3 restriction/inclusion squares | `8dd59b35…[11610,11743)`, `[12001,12049)` | **INSIDE** (`A0`) — and carries **no refinement**, §1.3.1 |
| **L3** | **T13's battery pinning** — families A and B as *"distinct C_ref generators"*; *"the pullback-commutation check runs on **a** common refinement"* | `85d24996…[16570,17090)` | **INSIDE** — its common refinement is **existential** |
| **L4** | **D3's frozen quantifier** — *"plus: **all** common refinements of members of A and B"*; F-2 forbids finite-list narrowing | `818083a5…[9333,9922)` | **CONTESTED** — §1.5 |
| **L5** | **A27's criterion** — *"invariant under a sealed class of regular-CW refinements and elementary subdivision/**common-refinement moves**"* | `bc6c3e49…[37467,37661)` | **OUTSIDE** — §1.6 |
| **L6** | **FC-1's adopted directedness** — *"there **exists** M with K → M and L → M in P3"* | `31e42812…` FC-1 | **INSIDE**, but **existential** — §1.7 |
| **L7** | **FC-2's shape-regular admission + preregistered relaxation** | `31e42812…` FC-2 | **CONDITIONAL — and now HALF-MET**, §1.8 |
| **L8** | **`V011`'s naturality demand** — *"commute with pullback to **a** common refinement"*; *"invariant under **each** elementary refinement"* | `aa7c6d49…[47025,47247)` | **INSIDE** |
| **L9** | **Q-408 / `Ref_PL` / P4** — *"the full primitive refinement category required by P4"*; `Ref_PL objects = order-complex/edgewise subdivisions sd_n(G)`, `CommonRef(n,m) = lcm(n,m)`; DoR-020 adopts *"the PL refinement core"* | `5203347c…`; `ee69fd1c…[38100,38420)`; `bead32b7…[644,737)` | **DIFFERENT INDEX** — §1.9 |

#### 1.3.1 `A0` carries no refinement

[PROVABLE] `REG` `12cbcb6c…[1265282,1265857)`, Q-624:

```text
Seven generators, all block-covered: the two record-native licensed moves
(cubical bisection; oriented subdivision, both frozen in V011's C_ref), four
invertible-only built moves whose closure is the relabeling groupoid (by TYPE
it cannot relate two genuinely different cellulations of one region), and the
seventh — the common-refinement family — BARRED AS CIRCULAR: …
```

**The enumeration this relay commissions already exists, sealed, and it counts seven.** `A0`'s
four moves are invertible-only and by TYPE cannot relate two genuinely different cellulations
of one region — so they contribute **no** refinement. Sealed stock's effective refinement
generators are `A1`, `A2`, and **the seventh**.

### 1.4 The refuting clause: barred as a SOURCE, not excluded from the CLASS

[PROVABLE] `V011` `aa7c6d49…[46772,47023)` — the licensing act, in full:

```text
Freeze an
admissible class `C_ref` of oriented, shape-regular periodic regular-CW
cellulations with:

cubical bisection;
oriented simplicial/barycentric subdivision;
and common refinements preserving the same smooth coframe and connection.
```

[PROVABLE] **Grammatically the three items are one list under one verb.** *Freeze an
admissible class … **with**:* governs all three. Items one and two are uncontestedly moves —
they are `A1` and `A2`, and the whole program treats them so. Item three sits in the same list
under the same verb. **If items one and two are licensed moves, item three is a licensed
move.** There is no reading on which the first two are admitted and the third is not, short of
a later act removing it — and the later act does something else.

[PROVABLE] What the later act does — `4d` `430f0971…[20690,20930)`:

```text
C_REF_AS_WRITTEN_DERIVES_SMOOTH_DATA_FROM_GATE4 = false | TYPE-R |
  test: the class definition takes the same smooth coframe and connection as
        input before the refinement conclusion is posed

C_REF_USABLE_AS_TARGET_INTERFACE = true
```

[PROVABLE] `FC` FC-1 uses the same qualifier — *"the smooth common-refinement family remains
barred **as a source** (TYPE-R)"* — and `REG`'s Q-624 gives a **source** reason: *"its
admissibility clause consults 'the same SMOOTH coframe and connection' while DoR-007 grounds
smoothness as existing only as a refinement limit … The generator consults, as input, the
object the theorem must produce."*

[PROVABLE] **So the bar is on derivation-from, not membership-in**, and
`C_REF_USABLE_AS_TARGET_INTERFACE = true` says so in one line. Sealed stock licenses a
refinement move outside `{A0, A1, A2}`. **The claim is false.**

[YOURS] **I read past that qualifier for four relays.** 725, 727, 731 and 739 each treated the
bar as a deletion from the class; 739 §1.2 says the third family *"is not used as a
generator"* and proceeds as though the generator set were closed. *Not-used-as-a-source* and
*not-in-the-class* are different propositions; the sealed text distinguishes them explicitly;
I collapsed them. The distinguishing line sits 60 bytes from a span I had already cited.

### 1.5 D3 — contested, and reported as contested

I commissioned adversarial verification of this leg (§4) and **it went against me.** Recording
the contest rather than the version that suited my conclusion.

[PROVABLE] **What is sealed.** `MAJSPEC` `818083a5…[9333,9922)`: *"plus: all common refinements
of members of A and B"*, *"The theorem's quantifier ranges over the skeleton, A, B, and common
refinements. Pinning the quantifier to any finite list is NOT available to any lane under any
outcome (F-2)."* The broad reading is frozen at `D3FRZ` `9a0c2045…` (`APPEND_ONLY_TYPING_FREEZE`:
*"ANY cellulation refining BOTH parents — unrestricted, universally quantified. It is NOT the
minimal overlay"*) and **ratified by the principal** at `D3RAT` `c373adba…`
(`APPEND_ONLY_PRINCIPAL_RATIFICATION`: *"The principal holds that the sealed INTENT does NOT
differ from the sealed TEXT … STANDS"*). `DET` `6934f858…` records
`D3_class_strictly_larger_than_C_ref = true`, `sliver_cellulations_in_D3_and_outside_C_ref =
true`, `D3_freeze_withdrawn = false`, `conflict_resolved = false`.

[PROVABLE] **What the verifiers established against it, and I confirmed from bytes.**
`MAJSPEC` line 11 reads *"Drafting-lane return only. **Nothing in this file is sealed
authority.**"* — sealed as *text*, self-disclaiming as *authority*. And the operative
objection is a real distinction: **D3's clause states a theorem's quantifier range over
cellulations (objects); it does not admit an arrow into any index.** The principal ratification
ratifies a *reading*, not an admissibility grant.

[YOURS] **Verdict on this leg: CONTESTED, and it is not load-bearing.** The refutation in §1.4
stands without it. What D3 still contributes, at a strength I will defend: sealed stock's
own consolidated position is that a class strictly larger than C_ref — containing slivers, and
upward-closed — is the one the surrounding theorems are written against, and no sealed artifact
reconciles the difference. That is context for the registrar, not a second proof.

### 1.6 A27 — the row RA27-2 serves names the moves

[PROVABLE] `A27s` `bc6c3e49…[37467,37661)`, the **sealed** instance of A27's requirement:

```text
The local coefficient is invariant under a sealed class of regular-CW
refinements and elementary subdivision/common-refinement moves; one
hypercubic sequence alone cannot establish universality.
```

[PROVABLE] **This says "moves", not "cellulations".** The verifiers' objection to D3 — that a
quantifier over objects is not a licensing act for arrows — does not reach here: A27's
quantifier ranges over **moves** by its own noun. RA27-2 exists to supply A27's index, and an
index that excludes common-refinement moves does not carry A27's quantifier.

### 1.7 The quantifier gap — existential supplied, universal demanded

[PROVABLE] Supplied, `FC` FC-1, carried inside the object at `IDX` §1.3:

```text
DIRECTEDNESS  *** ADOPTED AS AXIOM ***
   For any K, L with K ~ L there EXISTS M with K -> M and L -> M in P3.
```

[PROVABLE] Demanded, `A27s` `[37467,37661)`: invariance under **all** elementary
subdivision/common-refinement moves.

[YOURS] **An existential does not discharge a universal.** FC-1 asserts that *some* common
refinement is reachable by `A1`/`A2` composites — `MAJ`'s `Z = A2 ∘ A1` is one witness. A27
demands the coefficient survive *every* common-refinement move. `MAJ`'s Z is the coarsest
common refinement of its pair; the class is upward-closed and one witness does not exhaust it.
No sealed act converts the one quantifier into the other, and the adoption that was made — a
carefully bounded existential — is not the adoption that would be needed. **This is what
actually stops RA27-2**, and it would stop it even if §1.4's clause did not exist.

### 1.8 FC-2's relaxation is not merely untriggered — it is half-met, and the remainder is named

[PROVABLE] `SLIV` `218be86d…` — **sealed**, and neither mine nor the producer's — protected
status:

```text
volume_weight_natural_on_full_D3 = true      (measure additivity, exact)
response_pullback_natural_on_full_D3 = UNDETERMINED
sliver_naturality_verdict = UNDETERMINED_ON_SEALED_INPUTS
missing_sealed_object = R_L2b_HS_scaling_exponent_derived_in_the_sliver_direction
cref_vs_D3_conflict_resolved = false
```

[PROVABLE] FC-2's trigger is *"a later sealed derivation proves slivers leave the
boundary/four-volume ratio of the ruled intensive subject intact."* The **volume-weight half
is derived and exact on full D3** — *"slivers, needles, star-refined atoms of unbounded facet
count — with no regularity hypothesis whatever."* The **response half is UNDETERMINED**, and
the missing object is named: `R_L2b_HS_scaling_exponent_derived_in_the_sliver_direction`.

[YOURS] **This also strengthens 739's functoriality result beyond what I claimed there, from a
source that is not mine.** 739 §1.6 derived the measure's refinement functoriality over `A1`,
`A2` and composites and flagged the cubical free space as untested. `SLIV` states the volume
weight is natural on **full D3**, exactly, by measure additivity — a strictly larger class than
I reached, sealed since 2026-07-26. My scope flag was honest and it was also unnecessary; the
result was already stronger than my derivation of it.

[YOURS] And it sharpens the shape of what remains: **the volume weight transports; the response
pullback is undetermined.** That is the same binary I typed at 739 §3 — the energy is
functorial, the response is the open consumer — arriving here from an entirely different
direction. Two independent routes now name the response, not the measure, as the object that
decides this thread.

### 1.9 L9 — a different index, recorded rather than dismissed

[PART-PROVABLE] `Ref_PL` is specified (`ee69fd1c…[38100,38420)`: objects = order-complex/edgewise
subdivisions `sd_n(G)`, arrows `n→m` for `n|m`, `CommonRef(n,m) = lcm(n,m)`), and
`DOR_020_CONTINUUM_PACKAGE_CONDITIONAL_RATIFICATION` `bead32b7…[644,737)` lists *"the PL
refinement core"* in its adopted content. But this is the **Q-408 continuum root's** index, not
C_ref's coefficient index, and the same lane records `Ref_0 != full Ref_PL/P4 generator
category` with `Ref_0` *"the largest physical refinement scope available to this lane."*
**Classified DIFFERENT INDEX** — and recorded anyway, because it is a third place where sealed
stock reaches for a refinement class wider than `{A1, A2}`.

### 1.10 The verdict

```text
CLOSURE = STOPPED — by REFUTATION, not by an unclassifiable clause.
```

The enumeration completed over the stated glob. It did not fail to classify: it classified
**L1's third constituent** and **L5** as OUTSIDE, **L4** as CONTESTED and not load-bearing,
**L7** as conditional-and-half-met, **L9** as a different index. The claim *"sealed stock
licenses no refinement move outside `{A0, A1, A2}`"* is **false**, and the counterexample is
C_ref's own third frozen constituent — the one the target set replaced with `A0`.

### 1.11 What IS proven, at its exact strength

[PART-PROVABLE] A **scoped** result survives:

```text
Within the index's FC-2-ruled SHAPE-REGULAR admission class, and taking the
seventh generator as excluded rather than source-barred, the licensed
refinement moves are exactly A1, A2 and their finite composites — A0
contributing identity of region and no refinement (REG Q-624, by TYPE).
```

[YOURS] That is closure **relative to a class chosen to make it true**, and it is not D012's
demand. Answering "the generators exhaust what stock licenses, after removing what they do not
cover" is the shape of argument this program's discipline exists to refuse. I state it and
decline to book it.

---

## 2. WW2 — RA27-2 DOES NOT BOOK

[PROVABLE] `DEC742`: *"RA27-2 books when closure is DERIVED at full strength."* Closure is
refuted, not derived. **RA27-2 does not book.**

[YOURS] **And the failure is not confined to demand 5.** §1.7's quantifier gap reaches back
into demand 3, which 739 booked as *supplied AS ADOPTED* on FC-1's directedness. That axiom is
existential; the consumer is universal. I qualify the earlier booking here rather than let it
stand unmarked:

| D012 demand | 739 status | Status now |
|---|---|---|
| 1 generators | SUPPLIED | unchanged |
| 2 same-region relation | SUPPLIED | unchanged |
| 3 common refinements | SUPPLIED AS ADOPTED | **SUPPLIED AS ADOPTED, EXISTENTIALLY ONLY** — does not carry A27's universal |
| 4 composition | SUPPLIED | unchanged |
| — precondition: measure refinement functoriality | SUPPLIED (`A1`/`A2` + composites; cubical free space flagged) | **SUPPLIED, AND STRONGER THAN CLAIMED** — `SLIV`: `volume_weight_natural_on_full_D3 = true`, exact |
| 5a reachability | SUPPLIED AS ADOPTED | unchanged, same existential qualification |
| 5b generator completeness | certificate only, proof absent | **REFUTED at the PROVE standard** |

```text
RA27_2 = stopped.
```

[YOURS] **What would unblock it — three routes, each a principal act.** The distance is no
longer one ruling, and the registrar should not have to infer that from a stop.

1. **Restrict and say so.** `V011` pre-registered this branch in its own text
   (`aa7c6d49…[47025,47247)`): *"Failure to prove this naturality either blocks the general
   claim or restricts the result explicitly to that cellulation."* Restricting A27's quantifier
   to the shape-regular class discharges RA27-2 immediately on §1.11 — and `DET` requires the
   cost be said aloud: *"the object is proved on a class STRICTLY SMALLER than the one A-L5 and
   recast Q6 quantify over, and those two remain unserved — which must be said in the verdict
   language rather than left implicit."*
2. **Finish FC-2's trigger.** It is **half-met** (§1.8): the volume weight is exact on full D3;
   the response pullback is undetermined; the missing object is named
   `R_L2b_HS_scaling_exponent_derived_in_the_sliver_direction`. This is the shortest technical
   route and it is a named, scoped obligation rather than an open question.
3. **Resolve the C_ref/D3 conflict**, open since 2026-07-26 with `resolution_holder =
   principal`. Routes 1 and 3 are one act seen from two sides.

---

## 3. WW3 — RA27-3's INCIDENCE-COMPOSITES ITEM

The closure machinery stopped, so it yields nothing — but the item does not need it, and the
answer is not the one I set up at 739.

[PROVABLE] **The composite step is free.** Let `g = g_n ∘ … ∘ g_1` be a `P3` arrow, each
`g_i ∈ {A1, A2}` (FC-1: P3's arrows are finite compositions of the two licensed moves). Suppose
each generator satisfies cell-wise four-volume additivity. Then `g` does.

*Proof.* Induction on `n`. `n = 1` is the hypothesis. For `n > 1` put `g' = g_(n-1) ∘ … ∘ g_1`.
Each `g_i` partitions each cell, so children of distinct cells are distinct and
`children_g(c) = ⊔_(c' ∈ children_g'(c)) children_g_n(c')` is disjoint. Hence

```text
sum_(c'' in children_g(c)) |c''|_4
  = sum_(c' in children_g'(c)) sum_(c'' in children_g_n(c')) |c''|_4
  = sum_(c' in children_g'(c)) |c'|_4        [generator hypothesis]
  = |c|_4                                     [induction hypothesis]
```

∎ No transverse multiplicity enters: this counts four-volume, not sub-faces, which is exactly
where my 731 trichotomy failed.

[PROVABLE] **And the generator-level hypothesis is now supplied on a larger class than I
assumed.** `SLIV` `218be86d…`: `volume_weight_natural_on_full_D3 = true (measure additivity,
exact)`. So the four-volume component of `incidence` is natural on full D3 — beyond `A1`/`A2`
entirely — and the composite question dissolves above it.

[YOURS] **739 §2.2 was imprecise and I correct it.** I wrote *"supplied on the generators, not
on composites"*, treating composites as the gap. Composites were never the gap: the induction
is one line, and the generator-level statement is sealed on a wider class than the index's own.

[PROVABLE] **The other half of `incidence` is untouched and stays named.** RA27-3's `incidence`
field is also the incidence numbers `incidence(f,e)` of `d_1` (`aa7c6d49…[44595,44690)`).
Naturality of that cochain structure under subdivision is a different object; the induction does
not reach it and nothing here supplies it.

```text
RA27_3_INCIDENCE = taken — the composite question is ANSWERED (it dissolves by
    induction, and its generator-level hypothesis is sealed on full D3).
    The cochain-incidence component is left named for its own relay.
```

---

## 4. THE COMMISSIONED SWEEP — WHAT IT CHANGED

[YOURS] Because the last three relays turned on defects in my instruments rather than my
reasoning, I commissioned five blind hunters over the same searched space with **different
search modalities** — by class name, by permission language, by move name, by criterion
quantifier, and by the bar — each candidate then handed to an adversarial verifier instructed
to refute and to default to refuted under uncertainty. Hunters were denied my own artifacts and
the producer's code.

**It earned its cost, and part of what it earned was against me:**

| What it produced | Effect |
|---|---|
| `D3FRZ` `9a0c2045…` and `D3RAT` `c373adba…` — the typing freeze and its **principal ratification** | Two sealed files I had **never opened**. Initially strengthened my D3 leg |
| The `MAJSPEC` self-disclaimer, line 11: *"Nothing in this file is sealed authority"* | **Refuted my D3 leg.** I verified it myself and demoted L4 to CONTESTED |
| The objects/arrows distinction — a quantifier range is not an admissibility grant | Forced the proof onto §1.4 and §1.6, which is where it belongs |
| `A27s` `bc6c3e49…` — a **sealed** instance of A27's criterion | Corrected my citation: `BID` `78f6bb08…` has **no sidecar** |
| `SLIV` `218be86d…` | §1.8 and §3 — and a **strengthening of 739's own result** |
| `V011`'s seal is the packet manifest, not a sidecar | Corrected my grounding statement |

[YOURS] **Two honest limits on the sweep, stated rather than left to be assumed.** Its
verification stage was capped at **four candidates per hunter**, so some candidates — including
the sealed A27 instance — were never adversarially tested; §1.6 rests on my own reading of
bytes I verified. And at the time of sealing, one hunter's chain had returned; the remaining
four were still running, so this section reports what one modality plus its verifiers produced,
not five. **No conclusion here depends on the unreturned hunters**, and any clause they surface
can only add to an enumeration that is already refuted.

[PART-PROVABLE] **One secondary observation from the sweep, flagged and not built on.** It
reports **zero** occurrences, corpus-wide, of any text equating the barycentric subdivision with
the order-simplex/Freudenthal/edgewise subdivision — yet C_ref's `A2` is *"oriented
simplicial/barycentric subdivision"* while `MAJ` instantiates family B as *"the oriented
order-simplex (Freudenthal) subdivision"*, and these are different operations. The identification
runs through the shared label *"family B"* (T13 → `MAJ`), not through any equation. I did not
pursue it and it changes nothing here; it is named because if it holds, the instantiation of
`A2` itself rests on an unstated identification.

---

## 5. GROUNDING, JURISDICTION, VERB AUDIT

### 5.1 Grounding

| # | Claim | Pin | Tag |
|---|---|---|---|
| 1 | PROVE governs; RA27-2 books only on derived closure | `3c7b4867…` | PROVABLE |
| 2 | The freeze act and its three-item list under one verb | `aa7c6d49…[46772,47023)` | PROVABLE |
| 3 | The bar is source-only; `C_REF_USABLE_AS_TARGET_INTERFACE = true` | `430f0971…[20690,20930)` | PROVABLE |
| 4 | FC-1's own qualifier "barred as a source" | `31e42812…` FC-1 | PROVABLE |
| 5 | Seven generators; `A0`'s four invertible-only, no refinement by TYPE | `12cbcb6c…[1265282,1265857)` | PROVABLE |
| 6 | A27 quantifies over "common-refinement **moves**" (sealed instance) | `bc6c3e49…[37467,37661)` | PROVABLE |
| 7 | FC-1's directedness is existential | `31e42812…` FC-1; `66f078ba…` §1.3 | PROVABLE |
| 8 | D3's frozen quantifier; F-2 | `818083a5…[9333,9922)` | PROVABLE |
| 9 | The broad reading frozen, then principal-ratified | `9a0c2045…`; `c373adba…` | PROVABLE |
| 10 | `MAJSPEC` self-disclaims sealed authority (line 11) | `818083a5…` | PROVABLE |
| 11 | D3's class strictly larger; slivers outside C_ref; conflict unresolved | `6934f858…` | PROVABLE |
| 12 | T13 says "**a** common refinement" — the broadening is downstream | `85d24996…[16570,17090)` | PROVABLE |
| 13 | `volume_weight_natural_on_full_D3 = true`; response pullback UNDETERMINED; missing object named | `218be86d…` | PROVABLE |
| 14 | FC-2's relaxation and its trigger | `31e42812…` FC-2 | PROVABLE |
| 15 | `Ref_PL` specified; DoR-020 adopts "the PL refinement core"; different index | `ee69fd1c…`; `bead32b7…`; `5203347c…` | PART-PROVABLE |
| 16 | V011 pre-registers "restrict the result explicitly to that cellulation" | `aa7c6d49…[47025,47247)` | PROVABLE |
| 17 | The composite additivity induction | §3 | YOURS |
| 18 | The existential/universal quantifier gap | §1.7 | YOURS |
| 19 | The barycentric ≠ Freudenthal naming observation | §4 | PART-PROVABLE, **not built on** |

**Pin check: 19/19.** Every span re-read from bytes this relay against the stated digest,
including both `REG` spans re-located after its digest changed mid-relay.

### 5.2 Jurisdiction check

**On returning a refutation where a proof was commissioned.** *What was the rule written to
protect?* D012's PROVE verb protects against a generator set that silently omits a move the
program needs. The risk was live: the omitted move is named in the criterion the index serves,
and in the freeze that created the class. *Does the outcome space distinguish false from
cannot-see?* Yes — this returns **false**, the stronger and rarer of the two, and §1.11 states
exactly what a restriction would buy. *Would it permit the evidence to appear if the theory is
right?* Yes: each of §2's three routes makes the claim true or makes it unnecessary.

**On the VOID CONDITION.** Nothing here is chosen from a desired coefficient. The refutation
runs **against** my own lane's interest — closure would have booked RA27-2 today — which is the
disposition `DET` records for itself in the same conflict.

**On BR-1.** The relay header reads *"THE CLOSURE PROOF, AND RA27-2 BOOKS"*; the task text
supplies the stop and I took it. A producer-declared header may accuse; it may never exculpate,
and it may not carry a criterion's direction.

**On R9 / R9-JII.** Untouched; the carrier stays PENDING on its common-cell quantifier.

### 5.3 Self verb audit — **CLEAN, with six disclosures**

1. **I collapsed "barred as a source" into "not in the class" across four relays** — 725, 727,
   731, 739 — while the sealed text distinguished them in a line
   (`C_REF_USABLE_AS_TARGET_INTERFACE = true`) sitting 60 bytes from a span I had already cited.
   Same failure mode as 727 and 739: the refutation living in bytes I had already consumed for
   another purpose. **Third occurrence.**
2. **My D3 leg was refuted by verification I commissioned**, on a distinction I had not drawn —
   a theorem's quantifier over objects is not an admissibility grant for arrows — and by a
   self-disclaimer on line 11 of a file I had read the middle of. §1.5 reports the contest and
   the proof no longer rests there. **Third consecutive relay in which commissioned verification
   reversed something of mine.**
3. **The instrument fix came from the commission, not from me.** 739's census could not have
   found this; the licensing-enumeration shape could and did. My eight-relay run of
   search-shaped defects ends with the task specifying the instrument.
4. **A shell bug nearly produced six false SEAL-MISMATCH reports** — I ran `shasum -c` from the
   archive root against sidecars carrying bare filenames. Caught by disbelieving a result that
   said six sealed files were all corrupt at once.
5. **`REG`'s digest changed mid-relay** (`fd6c774c…` → `12cbcb6c…`). I re-located both cited
   spans rather than assuming an append-only file leaves earlier offsets alone. It does — but
   only a re-read establishes it.
6. **739's demand-3 booking is qualified here, and 739 §2.2's incidence framing corrected.**
   Neither is withdrawn; both are restated at the strength the bytes support.

One thing to the record's credit rather than mine: **`SLIV` made 739's own functoriality result
stronger than I had derived it**, and it has been sealed since 2026-07-26.

---

```text
CLOSURE = STOPPED (clauses displayed) — by REFUTATION, not by an unclassifiable
    clause. Enumeration completed over 1,958 files, recursive glob
    ./workspace/**/*.md + ./supervision/**/*.md, writer-excluded, producer's code
    excluded. Nine licensing acts classified. THE REFUTING CLAUSE IS THE ROOT ACT
    ITSELF: V011 aa7c6d49...[46772,47023) freezes C_ref "with" THREE items under
    one verb — cubical bisection; oriented simplicial/barycentric subdivision; AND
    common refinements preserving the same smooth coframe and connection. The third
    is not A0; the target set {A0,A1,A2} substitutes an import from JREF for it. Its
    bar is SOURCE-ONLY by the corpus's own words — 4d 430f0971...[20690,20930):
    C_REF_USABLE_AS_TARGET_INTERFACE = true; FC-1: "barred as a source" — and the
    register's Q-624 already enumerated SEVEN generators, with A0's four carrying no
    refinement by TYPE. CORROBORATED, independently, by A27's SEALED criterion
    bc6c3e49...[37467,37661): "elementary subdivision/common-refinement MOVES" —
    moves, not cellulations. The D3 leg (818083a5, principal-ratified broad reading)
    is reported CONTESTED and is NOT load-bearing: commissioned adversarial
    verification refuted it as a theorem's quantifier range over objects, and its
    spec self-disclaims sealed authority at line 11.
    UNDERLYING FINDING: the index supplies an EXISTENTIAL common refinement (FC-1's
    adopted directedness) where A27 demands a UNIVERSAL over all common-refinement
    moves. No sealed act converts one into the other. That stops RA27-2 on its own.
RA27_2 = stopped.  739's display stands; demand 5b moves from certificate-only to
    REFUTED at the PROVE standard; demand 3 is qualified to EXISTENTIAL ONLY; and the
    measure-functoriality precondition is STRONGER than 739 claimed — SLIV 218be86d:
    volume_weight_natural_on_full_D3 = true (measure additivity, exact). Three
    principal routes displayed at section 2; route 2 (FC-2's relaxation) is HALF-MET
    with the missing object named: R_L2b_HS_scaling_exponent_derived_in_the_sliver
    _direction.
RA27_3_INCIDENCE = taken — the composite question dissolves by a one-line induction
    on composite length, and its generator-level hypothesis is sealed on FULL D3, not
    merely on the exhibited instances. The cochain-incidence component is left named.
VOID = clean
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+6 disclosures at section 5.3)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
