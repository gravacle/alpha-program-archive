# STAGE 8 / 7A / STEP 8 — RA27-2: THE SAME-REGION RELATION

**Lane:** Dario (Opus 5, cross-family from the Codex build lanes)
**Date:** 2026-08-08
**Scope:** PASTE 716 only — AA1 generators, AA2 forcing, AA3 the fork, AA4 ledger
**Custody:** archive-side read and write; the registrar owns any mirror
**Governing:** frozen prereg `9f0d12b4…`; sealed R9-JII carrier `5f4979d5…`; my
scoping `b1a834e7…`
**Charge:** re-derive, not trust. Adoption is the principal's; this lane stops at the fork.

## Lead determination

```text
FORCED = NO.  Sealed stock does not force the same-region relation, and the
         non-forcing is REFUTED-strength, not merely undetermined: three
         candidate closures carry sealed TYPE-R verdicts, and a one-parameter
         countermodel exhibits the freedom explicitly.

GENERATORS = 7, all block-covered.  Two are record-native and licensed (G1, G2).
         Four are BUILT but invertible-only, so they cannot relate distinct
         cellulations (G4-G7).  The one generator that would close the set --
         the common-refinement family G3 -- is barred as a SOURCE by DoR-007
         and its breadth is a conflict already before the principal.

THE FREE CHOICE IS NOT WHERE I EXPECTED IT.  It is not "pick a subdivision
rule."  Two things are unfixed, and the corpus names both:
    (1) THE TOPOLOGY -- {tau_norm, tau_cyl, tau_density}; "No authority proves
        these equivalent or selects one."  T_ref's conclusion is quantified
        over "one frozen topology" that has never been frozen.
    (2) THE SHAPE CONDITION -- shape-regular vs all common refinements
        including slivers.  ALREADY A HELD CONFLICT BEFORE THE PRINCIPAL,
        with PRODUCTION PROHIBITED.

MOST OF THIS RELAY'S RESULT WAS ALREADY OF RECORD.  My independent derivation
of the C_ref circularity reproduces a sealed TYPE-R finding from Codex Lane 1
dated 2026-08-02.  I report it as corroboration, not as discovery, and §8
discloses why my own 715 search missed it.
```

---

## 0. Preflight

### 0.1 Pickup-ACK, lane guard, relay, output

[PROVABLE] `relay_outbox/716_ACK.md` was written **before** source work, carrying the
relay number, this lane's name and the inbox digest. The relay header names
**DARIO**; the lane guard is satisfied. The relay was read only after its sidecar
verified:

```text
relay_inbox/RELAY_PASTE_716_RA27_2_SAME_REGION_DARIO_V001.md
  3e62b9cdfe700b6945d27184302dc4b404322b08d25d9e7d9662c7965d6ee255   shasum -c OK
```

[PROVABLE] `STAGE8_7A_RA27_2_SAME_REGION_DARIO_V001.md` and its seal sidecar were
probed before the write and returned ABSENT.

### 0.2 Sources, verified before use

```text
V011   review_packets/.../BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md  aa7c6d49…  (2026-07-23)
D007   BID_CONSOLIDATED_HOSTILE_AUDIT_MATRIX_V005.md                     78f6bb08…
D012   STAGE8_TASK6_A25_A27_SCOPING_LANE2_V003.md                        74bbb7aa…
JREF   STAGE8_TASK5_JREF_AND_LOCAL_KERNEL_ESTIMATES_LANE2_V001.md        8dd59b35…  (Lane 2)
4d     STAGE8_TASK4D_STITCHING_THEOREM_GERM_INDEPENDENT_HALF_V001.md     430f0971…  (Lane 1, 2026-08-02)
CREF3  STAGE8_T7_CREF_VS_D3_FACTUAL_DETERMINATION_V001.md                6934f858…  (2026-07-26)
DoR7   supervision/DECISION_OF_RECORD_007_SMOOTH_FORK_...V001.md         17dc023e…  (2026-08-01, sidecar OK)
CARR   STAGE8_7A_R9JII_JOINT_LANDING_TEST_V001.md                        5f4979d5…
PREREG STAGE8_7A_OBS22_RECOGNITION_PREREG_V002_FROZEN.md                 9f0d12b4…  unchanged
```

### 0.3 Gates

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

No common cell was formed. No junction map was evaluated. **No adoption was
performed.** No member bound, no fixed point, no end test, no numeric, no measured
constant. No register, plan, tracker, git, commit or push action. The frozen
preregistration was not altered.

---

## 1. AA1 — THE GENERATOR SET

Every operation sealed stock already licenses that relates two complexes. Seven, each
block-covered against its span.

### 1.1 The subdivision families — licensed, record-native

[PROVABLE] `V011` `aa7c6d49…[46389,47444)` freezes the class:

```text
Freeze an admissible class `C_ref` of oriented, shape-regular periodic regular-CW
cellulations with:

cubical bisection;
oriented simplicial/barycentric subdivision;
and common refinements preserving the same smooth coframe and connection.
```

```text
G1  cubical bisection                        -- combinatorial, smooth-free
G2  oriented simplicial/barycentric subdivision -- combinatorial, smooth-free
G3  common refinements preserving the same smooth coframe and connection
                                             -- SEE §1.3; this is the problem
```

[PROVABLE] `D012` `74bbb7aa…` records that the filled-carrier census classifies
`C_ref` as a frozen **audit class**, and that *"No theorem in that source derives it
as the unique physical record complex."*

### 1.2 The BUILT arrows — real, but invertible-only

[PROVABLE] `JREF` `8dd59b35…[278,662)`:

```text
BUILT: the maximal derived finite realization skeleton: admitted finite
Gate-4 complexes, identity/isomorphism/relabeling arrows, their conserved
current and bilocal-kernel realizations, and every already-ratified W3
restriction square.
```

```text
G4  identity arrows
G5  isomorphism arrows
G6  relabeling arrows
G7  already-ratified W3 restriction squares
```

[YOURS] G4–G6 are **invertible**: they relate a complex to itself up to renaming.
Their closure is the relabeling groupoid, and it identifies exactly those complexes
that are isomorphic **as labelled complexes**. That is strictly weaker than
"represents the same physical region": two genuinely different cellulations of one
region are not isomorphic, so no composite of G4–G6 relates them. G7 is directional
(a restriction), so it does not supply the missing symmetry either. **The BUILT half
of the generator set cannot, by its own type, express the relation RA27-2 demands.**

### 1.3 G3 — the generator that would close the set, and why it cannot be used as one

[PROVABLE] `DoR7` `17dc023e…[253,579)` rules the object must be **derived**:

```text
The smooth-required subset ... is to be met by a DERIVED DISCRETE-TO-CONTINUUM
EQUIVALENCE THEOREM — the stitching rule as a theorem over refinements.
```

and at `[531,771)` closes the obvious escape:

```text
ADOPTION OF (M,g) FOR THIS SUBSET IS OFF THE TABLE. The ambient metric carries an
Einstein-Hilbert term; adopting it at the alpha-facing chain would adopt the gravity
the program claims to derive.
```

[PROVABLE] G3's admissibility clause names *"the same **smooth** coframe and
connection."* DoR-007 grounds base-smoothness as existing *"only as a refinement
limit"* whose *"cellulation-independence is the theorem's content."* So G3 consults,
as an input to the refinement relation, an object that the refinement theorem is
supposed to produce.

[PROVABLE] **This is already of record, and stronger than my own reading.** `4d`
`430f0971…[20198,20680)` and `[20690,20945)`, Codex Lane 1, 2026-08-02:

```text
That is a valid target interface, but it cannot by itself derive the smooth limit
from Gate-4 data: the smooth coframe and connection already appear in the
admissibility clause. Using that clause as the source of the smooth object would be
circular under DoR-007.

C_REF_AS_WRITTEN_DERIVES_SMOOTH_DATA_FROM_GATE4 = false | TYPE-R |
  test: the class definition takes the same smooth coframe and connection as
        input before the refinement conclusion is posed

C_REF_USABLE_AS_TARGET_INTERFACE = true
```

[YOURS] I derived this circularity independently from `V011` + `DoR7` before finding
`4d`. It is not my finding. The typing that matters is `4d`'s and it is exact:
**C_ref is usable as a target interface and refuted as a source.** It tells a builder
what success looks like; it cannot be the thing that gets you there.

### 1.4 Generator census

```text
GENERATORS = 7, all block-covered

  G1 cubical bisection                       LICENSED, record-native, smooth-free
  G2 barycentric/simplicial subdivision      LICENSED, record-native, smooth-free
  G3 common refinements (smooth-preserving)  TARGET INTERFACE ONLY -- refuted as source
  G4 identity                                BUILT, invertible
  G5 isomorphism                             BUILT, invertible
  G6 relabeling                              BUILT, invertible
  G7 W3 restriction squares                  BUILT, directional, ratified
```

---

## 2. AA2 — THE FORCING QUESTION

### 2.1 What IS forced

[PART-PROVABLE] From the licensed generators alone, the following closure properties
are forced and nothing else is:

```text
REFLEXIVITY   forced -- G4 (identity) is BUILT.
SYMMETRY      forced ONLY on the invertible part -- G5, G6 have inverses by type.
              NOT forced across G1, G2, G7, which are directional.
COMPOSITION   forced -- composites of BUILT arrows are BUILT (the skeleton is a
              category); subdivisions compose with subdivisions.
TRANSITIVITY-AS-EQUIVALENCE   NOT forced.  Getting an equivalence from directional
              generators requires closing under spans K <= M => L through a COMMON
              refinement M, and the common-refinement family is exactly G3.
```

[YOURS] So the licensed set is a **category with a groupoid core**, not an
equivalence. The gap between what is forced and what RA27-2 demands is precisely the
span closure, and the span closure needs G3.

### 2.2 What is REFUTED — three sealed TYPE-R verdicts

[PROVABLE] `JREF` `8dd59b35…[12881,13280)` disposes of the natural repair — build the
relation formally out of G1/G2:

```text
Likewise, an abstract barycentric subdivision of one complex gives a formal
combinatorial chain, but it does not prove that two different complexes
represent the same physical region, furnish a common geometric refinement,
or transport coframes, volumes, sources, and connected response.  Taking the
free category on formal subdivision symbols merely moves the missing data
into unproved generators.
```

[PROVABLE] and records the verdicts, `8dd59b35…[13290,13460)`:

```text
INCIDENCE_FORCES_GEOMETRIC_SCALE = false | TYPE-R |
THIN_ZERO_EXTENSION_FORCES_REFINEMENT = false | TYPE-R
FREE_REFINEMENT_CATEGORY_DISCHARGES_J_REF = false | TYPE-R
```

[YOURS] `TYPE-R` is refuted, not undetermined. The three closures a builder would
reach for first are each closed off by name.

### 2.3 Uniqueness — refuted by an explicit countermodel

[PROVABLE] `JREF` `8dd59b35…[12383,12879)`:

```text
The same finite incidence and holonomy data admit distinct positive coframe
and cell-volume assignments.  For a scale parameter `lambda>0`, the
assignments

ell_e -> lambda ell_e,
V_cell -> lambda^d V_cell                       (D2-4)

leave the sealed incidence, boundary, character, restriction, and finite
holonomy equations unchanged.  They change current-density normalization and
the order-two local symbol.  Neither DoR-007 nor DoR-008 chooses `lambda` or
supplies a scale law.
```

[PROVABLE] This settles AA2's uniqueness question in the negative and does so
constructively: a **one-parameter family** of assignments is consistent with every
sealed equation, and no sealed rule picks a member. Uniqueness of the closure is not
open — it is **refuted**.

### 2.4 The completeness / reachability certificate

The relay asks for this certificate as the deliverable either way. It is deliverable,
and it is a negative certificate — which is a result, not a failure.

```text
CERTIFICATE — COMPLETENESS AND REACHABILITY OVER THE GENERATOR SET

COMPLETENESS (is the generator list exhaustive?)
  The seven generators of §1.4 are every operation relating two complexes that
  sealed stock licenses.  SEARCHED SPACE: workspace/ + supervision/, --include=*.md,
  recursive; probes: regular-CW, regular CW, elementary subdivision,
  common-refinement move, subdivision, barycentric, relabeling, cofinal, Ref_a.
  No eighth licensed operation was found.  Per the LANE_STATUS caveat this is a
  LOWER BOUND on what is ruled, not a proof of exhaustiveness.

REACHABILITY (what does the set reach?)
  From {G1,G2,G4,G5,G6,G7} the reachable relation on complexes is:
      K ~ L  iff  K and L are isomorphic as labelled complexes,
                 or L is obtained from K by a finite composite of subdivisions
                 and ratified restrictions.
  This is a PREORDER WITH A GROUPOID CORE.  It is not symmetric across
  subdivision, hence not an equivalence, hence not a same-region relation.

UNREACHABLE, AND WHY
  The span closure K <= M => L requires the common-refinement family G3.
  G3 is refuted as a source (4d, TYPE-R) and its breadth is a held conflict.
  Adding G3 as a FORMAL generator is refuted by name
  (FREE_REFINEMENT_CATEGORY_DISCHARGES_J_REF = false | TYPE-R).

VERDICT
  RA27_2_FORCED_BY_STOCK = false
  RA27_2_CLOSURE_UNIQUE  = false   (countermodel (D2-4), one-parameter)
  CERTIFICATE_TYPE       = negative; the obstruction is located at the span
                           closure, not spread across the demand.
```

---

## 3. AA3 — THE FORK, SURFACED AND NOT DECIDED

### 3.1 Stock does not force the relation

Established at §2. The fork is therefore live, and this section states it without
taking it.

### 3.2 The free choice — two unfixed things, and the corpus names both

**(1) The topology.** [PROVABLE] `4d` `430f0971…[11152,11540)` and `[11420,11682)`:

```text
tau_norm    = C-star/module norm on the ratified completion;
tau_cyl     = projective convergence of every finite restriction;
tau_density = local-response/action-density convergence over C_ref.

No authority proves these equivalent or selects one. `tau_cyl` alone admits a
bidual tail; `tau_norm` excludes that tail but lacks geometric realization;
`tau_density` is named operationally by V011 but not defined as a complete
topological carrier.
```

[PROVABLE] And `T_ref`'s conclusion is quantified over *"one frozen topology"* —
`4d` §3.2. **No topology has been frozen.** This is the first free choice and it is
prior to any construction: the theorem's own statement is incomplete without it.

**(2) The shape condition — already before the principal.** [PROVABLE] `CREF3`
`6934f858…[177,391)`:

```text
VERDICT: (i) SAME OBJECT — a genuine conflict between two sealed
authorities exists, and per the principal's instruction it is HIS to
resolve.
CONSEQUENCE, BINDING ON THIS LANE: the D3_REFINEMENT_NATURAL_VOLUME_W...
```

with the spec **HELD** and **PRODUCTION PROHIBITED** pending his decision. The
conflict is C_ref's *shape-regular* restriction against D3's breadth — all common
refinements **including slivers**.

[PROVABLE] Whether that conflict has since been ruled: **not found.** SEARCHED SPACE:
`supervision/*.md`, content probes (`sliver`, `shape-regular`, `admissible class`,
`refinement class`) intersected with ruling markers, plus the held spec's own name.
The only hits naming the held spec are two Bohm audit files of 2026-07-27 and
07-29, both **earlier** than `4d`. Per `STAGE8_LANE_STATUS.md`'s own caveat —
*"THIS FILE IS NOT AUTHORITATIVE ON WHAT HAS BEEN RULED … search the corpus by
CONTENT, not by label"* — I record this as **no ruling found**, which is a lower
bound and not a finding that none exists.

### 3.3 The smallest adoption that closes it

[YOURS] Not a subdivision rule, and not a same-region relation written by hand:

```text
SMALLEST ADOPTION = FREEZE ONE TOPOLOGY from {tau_norm, tau_cyl, tau_density}.
```

Why this is smallest: `4d` already supplies the would-build package —
`D_ref`, `eta_K`, `P_KR`, `Resp_K` with the two commuting equations
(`430f0971…[10671,10885)`) — and the germ-independent half is **proved**. What that
package cannot state without a topology is its own conclusion, *"independent of the
cofinal refinement family in one frozen topology."* Freezing the topology adds no
generator, no member, no shape condition and no smooth import; it fixes the sense in
which the limit is taken. Everything else in the chain is then a derivation target
rather than a choice.

[YOURS] It is emphatically **not** sufficient on its own — the shape conflict (§3.2)
and the `lambda` freedom (§2.3) remain. It is the smallest thing whose absence
currently makes the theorem unstateable.

### 3.4 What each candidate commits downstream

| Choice | Commits | Cost, in the corpus's own words |
|---|---|---|
| `tau_norm` | the ratified C*/module completion; excludes the bidual tail | *"lacks geometric realization"* — the very thing RA27-3 must carry |
| `tau_cyl` | projective convergence of finite restrictions | *"admits a bidual tail"* — a tail the response must then be shown blind to |
| `tau_density` | local-response/action-density convergence over `C_ref` | *"named operationally by V011 but not defined as a complete topological carrier"* — closest to the physics, furthest from being a defined object |

[YOURS] The honest reading: `tau_density` is what the physics wants and is the least
built; `tau_norm` is the most built and the least geometric. That trade is the
decision, and it is not mine.

### 3.5 U1_J2_EFFECT — and a correction to my own 715 finding

[PART-PROVABLE] At 715 I wrote that R9-JII's J2 is *unquantifiable* for want of a
domain. That was right but under-specified, and this relay sharpens it into two
distinct lacks:

```text
J2 needs, and lacks, BOTH:
  (a) A DOMAIN     -- the category Ref of admissible complexes and certified
                      refinement morphisms.  4d states its would-build shape; it is
                      not instantiated.
  (b) A TOPOLOGY   -- "invariant under cell re-presentation" asserts a limit
                      statement, and the limit's sense is unfrozen.  Even with Ref
                      in hand, J2 has no determinate truth condition until one of
                      {tau_norm, tau_cyl, tau_density} is frozen.
```

[YOURS] So freezing the topology does more than unblock A27: **it is the first of
J2's two lacks and the one nothing else supplies.** It does not make J2 runnable —
the R9-JII carrier stays PENDING on its common-cell quantifier regardless, and
Q-126's census is untouched — but it converts J2 from *not-yet-meaningful* to
*meaningful-and-unquantified*, which is a different and better kind of open.

[PART-PROVABLE] **A candidate identification I decline to make.** The `lambda` of
(D2-4) is an undetermined positive scale on the record cell; so is `beta`. If they
are the same free parameter, one adoption would close both RA27-2's uniqueness gap
and U1's `beta` gap. **The corpus does not say they are the same**, and Q-08's
standing habit with exactly this shape of question is *"TWO OBJECTS, NO BRIDGE"*.
I record it as a question for the adoption request, not as a linkage, and its
*resemblance* goes to the ledger at zero weight (L2).

### 3.6 The adoption request, stated — not made

```text
TO THE PRINCIPAL, from the Dario lane, RA27-2 / road step 8.
NOTHING IS ADOPTED HERE.  This lane stops at the fork, as commissioned.

REQUEST 1 (the smallest, and the blocker):
  FREEZE ONE TOPOLOGY from {tau_norm, tau_cyl, tau_density} in which T_ref's
  cofinal-independence conclusion is asserted.  Costs of each at §3.4.
  Until this is frozen, T_ref is not a statement, and R9-JII's J2 has no truth
  condition.

REQUEST 2 (already yours, recorded so it is not lost):
  The C_ref-vs-D3 SHAPE CONFLICT of 2026-07-26 appears still HELD, with
  PRODUCTION PROHIBITED on the D3 refinement spec.  RA27-2 cannot be closed
  while it is held, because the generator G3's breadth is exactly that question.
  I found no later ruling; see §3.2 for the searched space and its limits.

QUESTION 3 (not a request; do not answer by fiat):
  Is (D2-4)'s `lambda` the same free parameter as U1's `beta`?  If yes, one
  adoption closes two gaps; if no, closing RA27-2 leaves U1 exactly as it is.
  The corpus does not say, and this lane will not assume it.

WHAT IS *NOT* BEING ASKED:
  No smooth coframe, connection, metric or background.  DoR-007 forecloses that
  adoption and this request does not reopen it.
```

---

## 4. AA4 — CORRESPONDENCE LEDGER (verdict weight = 0)

| # | Encountered at | Classical likeness | Weight |
|---|---|---|---|
| L1 | span closure `K <= M => L` through a common refinement | the calculus of fractions / localization at a class of morphisms; and an atlas whose charts agree on overlaps | 0 |
| L2 | (D2-4)'s `lambda` rescaling `ell -> lambda ell`, `V -> lambda^d V` | choice of lattice spacing; a dimensionless coupling defined only up to a scale convention | 0 |
| L3 | `{tau_norm, tau_cyl, tau_density}` as competing senses of one limit | inequivalent operator topologies, where a theorem's content depends on which is meant | 0 |
| L4 | the relabeling groupoid as too small to relate distinct cellulations | gauge/diffeomorphism redundancy versus genuine physical equivalence | 0 |

[YOURS] L1 is the seductive one: the span construction *looks* like a standard
localization, which makes it feel available. It is not — `FREE_REFINEMENT_CATEGORY_
DISCHARGES_J_REF = false | TYPE-R` closes exactly that move by name, and the
resemblance played no part in §2, which rests on sealed text.

---

## 5. SEARCHED SPACES

| Absence claimed | Searched space | Method |
|---|---|---|
| No eighth licensed generator | `workspace/` + `supervision/`, `*.md`, recursive | fixed-string: `regular-CW`, `regular CW`, `elementary subdivision`, `common-refinement move`, `subdivision`, `barycentric`, `relabeling`, `cofinal`, `Ref_a` |
| No ruling resolving the shape conflict | `supervision/*.md` | content probes (`sliver`, `shape-regular`, `admissible class`, `refinement class`) ∩ ruling markers; plus the held spec's own name |
| No sealed statement identifying `lambda` with `beta` | `workspace/` + `supervision/`, `*.md`, recursive | fixed-string on both names, cross-read |

[YOURS] Not searched, therefore not claimed about: the cleanroom mirror, the origin
corpus outside the archive, non-`.md` files, and `rd22_run_*/evidence/` mirrors
(which duplicate workspace bytes under digest-prefixed names). Per
`STAGE8_LANE_STATUS.md`'s own caveat, every absence here is a **lower bound**.

---

## 6. GROUNDING TABLE

| # | Step | Source + span | Tag |
|---|---|---|---|
| 1 | `C_ref` freeze; G1/G2/G3 | `aa7c6d49…[46389,47444)` | PROVABLE |
| 2 | G4–G7 BUILT | `8dd59b35…[278,662)` | PROVABLE |
| 3 | G4–G6 invertible ⇒ cannot relate distinct cellulations | §1.2, by type | PART-PROVABLE |
| 4 | DoR-007 requires a derived theorem | `17dc023e…[253,579)` | PROVABLE |
| 5 | DoR-007 forecloses adopting (M,g) | `17dc023e…[531,771)` | PROVABLE |
| 6 | C_ref circular as a source; usable as target interface | `430f0971…[20198,20680)`, `[20690,20945)` | PROVABLE |
| 7 | Free subdivision category refuted | `8dd59b35…[12881,13280)` | PROVABLE |
| 8 | Three TYPE-R verdicts | `8dd59b35…[13290,13460)` | PROVABLE |
| 9 | (D2-4) `lambda` countermodel; no rule chooses it | `8dd59b35…[12383,12879)` | PROVABLE |
| 10 | Three candidate topologies | `430f0971…[11152,11540)` | PROVABLE |
| 11 | No authority selects one; each cost | `430f0971…[11420,11682)` | PROVABLE |
| 12 | `T_ref` would-build maps | `430f0971…[10671,10885)` | PROVABLE |
| 13 | Shape conflict held; principal's to resolve | `6934f858…[177,391)` | PROVABLE |
| 14 | No later ruling found | §5, searched space stated | PROVABLE (lower bound) |
| 15 | What is forced: reflexivity, partial symmetry, composition | §2.1, from 1–3 | PART-PROVABLE |
| 16 | Not forced: the span closure | §2.1, §2.4 | PART-PROVABLE |
| 17 | Uniqueness refuted | from 9 | PROVABLE |
| 18 | The completeness/reachability certificate | §2.4 | PART-PROVABLE |
| 19 | Smallest adoption = freeze one topology | §3.3 | **YOURS** |
| 20 | J2 lacks a domain **and** a topology | §3.5, from 10–12 + `5f4979d5…` | PART-PROVABLE |
| 21 | `lambda` ≟ `beta` declined, routed to the request | §3.5 | **YOURS** |
| 22 | Downstream commitments per topology | §3.4, quoting 11 | PART-PROVABLE |

```text
GROUNDED_STEPS = 20 / 22
YOURS, NAMED, NOT BRIDGED: 19 (the smallest-adoption judgment), 21 (the declined
identification).  Neither is used as a premise for any PROVABLE row.
```

---

## 7. JURISDICTION CHECK

**DoR-007.** Written to stop the program adopting the gravity it claims to derive.
Squarely present: the natural fix for RA27-2 is to import a smooth coframe, which is
precisely the adoption DoR-007 forecloses. Its outcome space distinguishes false from
cannot-see — it does not say the limit is unreachable, it says it must be *derived*.
And it permits the evidence: a derived cellulation-independence theorem is exactly
what it asks for. **I applied it to bar a source, not to bar the object.**

**The TYPE-R refutations.** Written against formal constructions that relocate the
missing data into unproved generators. Present — §2's most tempting move is exactly
that. They refute named constructions, not the possibility of a theorem.

**C_ref.** Written as an audit interface. I used it as a target interface and
explicitly refused it as a source, which is `4d`'s own typing and the corpus's.

**The held shape conflict.** Written so a lane cannot settle by production what the
principal has reserved. Present, and binding: §3.6 records the conflict rather than
resolving it, and takes no shape condition.

**R9-JII / R9.** Unchanged by anything here. No common cell was formed and no
identification assumed; §3.5 declines the `lambda`/`beta` identification for exactly
the reason R9 exists.

---

## 8. SELF VERB AUDIT

| Verb or status | Warrant |
|---|---|
| `NOT FORCED` | three sealed TYPE-R verdicts plus an explicit one-parameter countermodel |
| `refuted` | used only where the corpus types a result `TYPE-R`, never for my own negative results |
| `forced` | §2.1, and only for reflexivity, partial symmetry, and composition |
| `certificate` | negative certificate, with the obstruction located rather than asserted |
| `smallest adoption` | tagged YOURS; the reasoning displayed and its insufficiency stated |
| `request, not made` | §3.6 adopts nothing and names what is not being asked |
| `no ruling found` | with searched space and the corpus's own lower-bound caveat |

[YOURS] Disclosures against myself:

1. **This relay's central finding was already of record, and my 715 search missed
   it.** The C_ref circularity I derived from `V011` + `DoR-007` is a sealed TYPE-R
   result of Codex Lane 1, dated 2026-08-02. At 715 I reported that *"nothing
   supplies `Ref_a`"* — true, and it left the reader believing the ground was
   untouched. It was not: a theorem family was stated, its germ-independent half
   proved, and the circularity typed. **My search failed because I probed the
   demand's vocabulary (`Ref_a`, `CoefficientBoundaryCert`) and the prior work uses
   the object's (`T_ref`, `C_ref`, `Ref`).** Right space, wrong words.
2. **That is a fourth consecutive scope failure, of a fourth kind** — 711's archive
   boundary, 713's workspace-only search and character offsets, 715's span coverage,
   and now vocabulary. The SEARCHED-SPACE CLAUSE and the SPAN-COVERAGE RULE do not
   catch this one. The missing companion is: **probe the object's names, not only the
   demand's; when a demand names an object you cannot find, search for what the
   object would be called by whoever built it.**
3. **I expected the free choice to be the subdivision rule.** It is the topology, and
   the corpus named it before I looked. My prior framing at 715 — "the grammar may be
   an adoption" — pointed at the wrong slot; the grammar's generators are largely
   licensed already, and what is missing is the sense of the limit.
4. **I declined an identification I would have liked to make.** `lambda` and `beta`
   are both undetermined positive scales on the record cell, and treating them as one
   would have produced a much stronger result. The corpus does not say they are one,
   and Q-08's habit with this exact shape is "TWO OBJECTS, NO BRIDGE."
5. **Three of my spans were short — in the relay after I installed the rule that
   catches it.** The block-coverage check I proposed at 715 fired on its first real
   use: `4d [20198,20547)`, `JREF [12881,13256)` and `JREF [12383,12758)` each stopped
   before the end of the text displayed under them, and each is corrected above. The
   rule works; my habit of estimating an endpoint rather than generating it has not
   yet caught up with it. The durable fix is mechanical and I am stating it so it is
   not left as a resolution: **generate the end offset from the quote's last token,
   never from a guess at its length.**
6. No verb here proves, authorizes, computes, binds a member, forms a common cell,
   evaluates a junction map, adopts anything, or grants a seal.

```text
GENERATORS = 7, all block-covered
FORCED = NOT FORCED (fork stated, adoption request displayed at §3.6)
  -- and the non-forcing is refuted-strength: 3 sealed TYPE-R verdicts + the
     one-parameter (D2-4) countermodel refuting uniqueness
CERTIFICATE = completeness/reachability over the generator set, §2.4 (negative;
  reachable relation = preorder with groupoid core; obstruction located at the
  span closure, which needs the one generator that is refuted as a source)
U1_J2_EFFECT = stated (§3.5): J2 lacks BOTH a domain and a frozen topology;
  freezing the topology supplies the second and nothing else does; the carrier
  stays PENDING on its common-cell quantifier regardless
LEDGER_ENTRIES = 4
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+6 disclosures at §8)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
