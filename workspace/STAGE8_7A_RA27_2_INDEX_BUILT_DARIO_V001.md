# STAGE 8 / 7A / STEP 8 — THE RA27-2 INDEX, BUILT — AND THE TRANSPORT FINDING

**Lane:** Dario (Opus 5, cross-family from the Codex build lanes)
**Date:** 2026-08-08
**Scope:** PASTE 727 only — LL1 construct, LL2 verify, LL3 consequences, LL4 ledger
**Custody:** archive-side read and write; the registrar owns any mirror
**Governing:** `DECISION_RA27_2_ADOPTIONS_2026-08-08.md` `31e42812…`;
`DECISION_REFINEMENT_LIMIT_SUBJECT_2026-08-08.md` `112e6acb…`; prereg `9f0d12b4…`
**Charge:** re-derive, not trust. Nothing is adopted beyond the decision's own three.

## Lead determination

```text
LL1 = DELIVERED.  Ref_a is constructed and stated closed.  It does not depend on
      LL2 and it stands.

LL2 = FINDING.  THE BUILD STOPS HERE, as LL2 instructs.

      The decision's FC-1 rests on a premise I must report unsupported:
      "the derived measure's pullback naturality (T11) is the transport law
      along the arrows."  It is not.  T11 derives a CHANGE-OF-COFRAME law --
      same cell, different frame e, pullback by wedge^2(e^-1)|det e|.  The P3
      arrows are SUBDIVISIONS -- same frame, one cell replaced by many.  Those
      are different transformations, and the second is not derived.

      This is not my inference against a lane.  Two non-Dario sources say it:
        4d   -- T11 "does not derive the coframe or the refinement bridge";
        BATT -- "T11's gap is FUNCTORIALITY OF A MEASURE -- does the
                 response-map pullback commute with refinement...?"
      The thing the decision assumed T11 supplies is named, by the corpus, as
      T11's GAP.

      Both generators fail identically and for the same reason.  There is no
      asymmetry to exploit and no patch available; LL2 forbids one.

THE CORRECTION I OWE.  The premise entered the decision through MY 725 package.
I wrote that the measure half was "already done" and that the index "has to be
a system the derived measure already transforms correctly along."  The first
clause is defensible; the second is the error, and it is the one FC-1 leaned
on.  §2.4 states it at full weight.
```

---

## 0. Preflight

[PROVABLE] `relay_outbox/727_ACK.md` was written **before** source work. Lane guard:
the header names **DARIO**. Read only after its sidecar verified:

```text
relay_inbox/RELAY_PASTE_727_RA27_2_BUILD_DARIO_V001.md
  0434a69ef2050d7e19dbeed5bdfb05987234fa3c8a142f9130259795618392f0   shasum -c OK
```

[PROVABLE] `STAGE8_7A_RA27_2_INDEX_BUILT_DARIO_V001.md` and its seal sidecar were
probed before the write and returned ABSENT.

### 0.1 Sources verified before use

```text
FC     supervision/DECISION_RA27_2_ADOPTIONS_2026-08-08.md          31e42812…  sidecar OK
SUBJ   supervision/DECISION_REFINEMENT_LIMIT_SUBJECT_2026-08-08.md  112e6acb…  sidecar OK
V011   review_packets/.../BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md aa7c6d49…
JREF   STAGE8_TASK5_JREF_AND_LOCAL_KERNEL_ESTIMATES_LANE2_V001.md   8dd59b35…
4d     STAGE8_TASK4D_STITCHING_THEOREM_GERM_INDEPENDENT_HALF_V001.md 430f0971…
BATT   STAGE8_T7_CODEX_BATTERY_TIER2_RETURNS_V001.md                14ddfc15…
DEC    supervision/RESULT_STITCHING_RULE_DECOMPOSED_2026-07-30.md   578eb5e9…
D012   STAGE8_TASK6_A25_A27_SCOPING_LANE2_V003.md                   74bbb7aa…
725    STAGE8_7A_RA27_2_ADOPTION_PACKAGE_DARIO_V001.md              2acac49a…  (mine)
PREREG STAGE8_7A_OBS22_RECOGNITION_PREREG_V002_FROZEN.md            9f0d12b4…  unchanged
```

[PROVABLE] **The writer-exclusion rule** — installed from my own 725 disclosure — was
applied to every census below: searches exclude `*_DARIO_V001.md` so this lane cannot
count itself.

### 0.2 Gates

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

No common cell formed, no junction map evaluated, no member bound, no fixed point, no
end test, no numeric evaluation, no measured constant. No register, plan, tracker, git
action. The frozen preregistration was not altered.

---

## 1. LL1 — THE INDEX, CONSTRUCTED

### 1.1 The base, already BUILT

[PROVABLE] `JREF` `8dd59b35…[11610,11743)` gives `Ref_0`'s arrows, and
`8dd59b35…[12001,12049)` its status `FINITE_REALIZATION_SKELETON_J_0 = BUILT / TYPE-P`:

```text
identity arrows;
certified signed relabelings/isomorphisms;
already-ratified rank-preserving W3 restriction/inclusion squares. (D2-2)
```

### 1.2 The two licensed moves, at their frozen span

[PROVABLE] `V011` `aa7c6d49…[46882,47019)`:

```text
cubical bisection;
oriented simplicial/barycentric subdivision;
and common refinements preserving the same smooth coframe and connection.
```

[PROVABLE] Per `FC` `31e42812…`, P3's arrows are finite compositions of **the first
two only**. The third family remains barred as a source (TYPE-R,
`430f0971…[20690,20930)`), and is not used here.

### 1.3 The object, stated closed

```text
Ref_a  —  THE RA27-2 REFINEMENT INDEX                    (per FC-1, 31e42812…)

OBJECTS
  admissible finite oriented record complexes carrying the Gate-4 data,
  restricted to the SHAPE-REGULAR admission class            [ADOPTED, FC-2]

ARROWS  generated by, and closed under finite composition of:
  A0  every arrow of Ref_0 — identities, certified signed
      relabelings/isomorphisms, ratified rank-preserving W3
      restriction/inclusion squares                          [BUILT, JREF]
  A1  cubical bisection                                      [LICENSED, V011]
  A2  oriented simplicial/barycentric subdivision            [LICENSED, V011]

P3  (refines)      K -> R iff R is reachable from K by a finite composite of
                   A1/A2 arrows (A0 arrows carry identity of region).
P1  (cells shrink) carried by the moves' own construction: A1 and A2 each
                   replace a cell by a finite family of strictly smaller cells.
                   NOT an added axiom — a property of the licensed moves.
P2  (same region)  K ~ L iff K and L are ZIGZAG-CONNECTED under P3:
                   a finite chain K = X_0, X_1, ..., X_n = L in which each
                   consecutive pair is related by a P3 arrow in ONE of the two
                   directions.  Reflexive by A0, symmetric by construction of
                   the zigzag, transitive by concatenation — an equivalence
                   relation on objects.

DIRECTEDNESS       *** ADOPTED AS AXIOM ***                   [ADOPTED, FC-1]
                   For any K, L with K ~ L there exists M with K -> M and
                   L -> M in P3.
                   THIS IS NOT DERIVED.  Q-624 established stock cannot supply
                   it (three TYPE-R verdicts; the span closure was the located
                   obstruction).  It is adopted by DECISION_RA27_2_ADOPTIONS
                   and must be recorded as adopted wherever Ref_a is used.

TYPE               a category with a distinguished class of refinement arrows,
                   an equivalence relation P2 on objects, and an ADOPTED
                   directedness axiom making each P2-class a directed system.
```

[YOURS] Two constructions above are mine and neither is an adoption. **P2's zigzag
form** is the standard closure of a directional relation into an equivalence, and I use
it because P3 alone is directional — 716 established that a directional generator set
cannot express "same region" without closing under spans. **P1's status** is a reading
of the moves: bisection and barycentric subdivision each replace a cell with strictly
smaller cells by their own construction, so P1 need not be adopted separately. If the
registrar reads P1 as requiring its own adoption, that is a one-line addition to the
ledger and changes nothing else.

[PROVABLE] **Directedness is adopted, not derived, and is marked so in the object
itself** — as `FC` requires: *"Adopted, not derived, and recorded as such wherever the
index is used."*

---

## 2. LL2 — MEASURE TRANSPORT: THE VERIFICATION, AND THE FINDING

### 2.1 What must be proven

`FC` states the transport law and commissions its verification: *"the derived measure's
pullback naturality (T11: 'the measure is forced, not chosen') is the transport law
along the arrows and its verification is part of the build."*

So the obligation is: **prove that the forced measure transforms along every P3 arrow —
both generator types.**

### 2.2 What T11 actually derives

[PROVABLE] `V011` `aa7c6d49…[46183,46387)`:

```text
For a general coframe `theta^a=e^a_mu dx^mu`,
the same map is defined by pulling the bivector through
`wedge^2(e^(-1))` and multiplying by `|det e|`. The diagonal formula above
is a mandatory exact check.
```

[PROVABLE] This is a **change-of-coframe** law. Its quantifier is *"for a general
coframe"*: one cell, one bivector, two frames `e`. It says how the per-cell object
re-expresses when the frame changes.

[PROVABLE] `4d` `430f0971…[21855,21975)` states its limit in as many words:

```text
This proves the local density transformation given the coframe. It does not
derive the coframe or the refinement bridge.
```

### 2.3 What a P3 arrow requires — and why it is a different transformation

[YOURS] A P3 arrow is a **subdivision**: one cell is replaced by a finite family of
sub-cells; the frame is not changed. Transporting the measure along it requires that

```text
   V_cell * sum_(mu<nu) F_(mu nu)^2      (the parent's contribution)
```

be recovered by summing the sub-cells' contributions — which requires a rule
assigning `F` on each new sub-face. **The change-of-coframe law says nothing about
this**: it re-expresses one cell's object in a new frame; it does not relate one cell's
object to many cells' objects.

[PROVABLE] And the corpus names the missing rule. `BATT` `14ddfc15…[4496,4636)`:

```text
T11's gap is FUNCTORIALITY OF A MEASURE — does the response-map pullback
  commute with refinement, and is the boundary term subextensive?
```

[PROVABLE] with the failure mode stated, `BATT` `14ddfc15…[4321,4455)`:

```text
the SAME FAILURE MODE — refinement-dependence, where a quantity that
  looks fine on a fixed cellulation degrades under subdivision.
```

[PROVABLE] **The property the decision assumed T11 supplies is exactly what a
non-Dario lane names as T11's gap.**

### 2.4 The correction I owe — this premise entered through my own package

[YOURS] `FC`'s transport clause did not arise from nowhere. My 725 package told the
principal the measure half was settled. I wrote, at 725 §1.3:

> *"An intensive coefficient needs two things a bare combinatorial index cannot give: a
> per-cell measure, and a naturality law for it **under change of coframe**. Both are
> derived and sealed. So the index does **not** have to supply, adopt, or choose a
> measure — it has to be a system **the derived measure already transforms correctly
> along**."*

The first clause is right and correctly names the law as a *coframe* law. **The last
clause is the error**: I slid from "there is a derived coframe-change law" to "the
measure transports along the refinement arrows," which does not follow and which the
sealed text contradicts. I also quoted `DEC`'s *"the measure's own stitching is done"*
approvingly. `DEC` contains **zero** occurrences of `subdivision` (writer-excluded
count); its claim is extensivity over a **fixed** cellulation — the total is a sum of
per-cell contributions — which is precisely the property `BATT` says can hold while the
quantity still *"degrades under subdivision."*

[YOURS] So my 725 §1.3 over-read one sealed sentence and under-read another, and FC-1's
transport clause rests on it. The decision is sound in its adoptions; the premise it
attached to them is not, and the premise is mine.

### 2.5 A further weakening, recorded because it bears on any repair

[PROVABLE] `V011` `aa7c6d49…[45848,45901)`:

```text
xi_(mu nu)=ell_mu ell_nu F_(mu nu)+higher-order terms
```

The relation grounding `V_cell sum F^2` carries an **unquantified remainder**. Any
future refinement-transport proof must control that remainder under subdivision, not
only the leading term. I record it so a repair attempt does not discover it late.

### 2.6 Searched, not assumed

[PROVABLE] SEARCHED SPACE: `workspace/` + `supervision/`, `*.md`, recursive,
**writer-excluded**. Probes for a subdivision rule for the face field:
`flux additivity` **0 files**; `flux adds` **0 files**; `subdivided face` **0 files**;
`under subdivision` **2 carriers**, one of which is a `.py` audit script and the other
is `BATT` — where the phrase appears in the sentence naming the failure mode, not in a
rule supplying it. `refinement bridge` occurs in **1 file**, `4d`, where it is named as
**not derived**.

### 2.7 The verdict, per generator

| Generator | Is it a change of coframe? | Does T11's law cover it? | Transport proven? |
|---|---|---|---|
| **A1** cubical bisection | no — a subdivision at fixed frame | no | **NO** |
| **A2** oriented simplicial/barycentric subdivision | no — a subdivision at fixed frame | no | **NO** |

```text
MEASURE_TRANSPORT = FINDING.  BUILD STOPPED.

Both generators fail, identically, for one reason: they are subdivisions and the
derived law is a coframe-change law.  There is no asymmetry between them to
exploit, and no patch is offered — LL2 forbids one, and a patch here would be
authoring the refinement bridge the corpus records as underived.
```

---

## 3. LL3 — CONSEQUENCES, STATED OF RECORD

The build stopped at LL2. What follows is therefore what LL1 **does** deliver and what
is **not** discharged — booked at that strength and no higher.

### 3.1 RA27-2 against D012's own text — **NOT discharged**

[PROVABLE] `D012` `74bbb7aa…[44324,44664)` demands `Ref_a` *"with generators,
same-region relation, common refinements, and composition"*, and *"prove generator
completeness/reachability"*.

| D012's demand | Status after LL1 |
|---|---|
| generators | **supplied** — A0/A1/A2, §1.3 |
| same-region relation | **supplied** — P2 zigzag, §1.3 |
| common refinements | **supplied by ADOPTED AXIOM**, not derived |
| composition | **supplied** — closure under finite composition |
| generator completeness/reachability proof | **NOT supplied** — and now unreachable in this build |

[YOURS] Four of five are supplied and one rests on the adopted axiom. But **RA27-2
cannot be booked as discharged**, because the object D012 demands is a *refinement*
index for the coefficient's limit, and §2 shows the measure does not transport along
its arrows. An index whose arrows the subject does not survive is not the index RA27-2
asks for. **RA27-2 = blocked (named): the measure's refinement functoriality.**

### 3.2 J2's domain — instantiated; the predicate still has no truth value

[PART-PROVABLE] `Ref_a` does instantiate J2's re-presentation family: P2's classes are
exactly the re-presentations J2 quantifies over. That much is delivered.

[PROVABLE] But J2 fires on whether the common value *"is not invariant under cell
re-presentation"* — and evaluating that requires the value to transport across those
re-presentations, which §2 shows is unproven. **So J2 has a domain and still no truth
condition on it.**

[PROVABLE] And independently of all of this, `SUBJ` and `FC` both record it: **the
R9-JII carrier remains PENDING on its common-cell quantifier.** This build does not
make the junction test runnable, and nothing here should be read as moving it.

### 3.3 The T_ref remainder

```text
SUPPLIED BY LL1     4d's would-build field 1 — an instantiated Ref.
NOT SUPPLIED
  the refinement functoriality of the measure          [ §2 — THE FINDING ]
  field 2  J_ref                                       [ unbuilt ]
  fields 4-5  eta_conn / eta_curv / eta_resp           [ unbuilt ]
  field 6  BoundaryCert                                [ NO_VERDICT of record ]
  fields 7-8  PhysInterface / PublicEquiv              [ unbuilt ]
  the exhaustion-vs-refinement gap: the sealed density instance remains
  exhaustion-indexed.  LL1 supplies a refinement index; it does NOT transport
  the sealed instance onto it, because that transport is the measure
  functoriality §2 finds unproven.
  THE S5.3 BURDEN — undischargeable here and not touched: an instantiated
  coefficient limit must PROVE (H1)/(H2)-class convergence, never assume it.
```

### 3.4 RA27-3 — partially unblocked, demand restated

[PROVABLE] `D012` `74bbb7aa…[44665,45007)` demands the full `J_ref` realization
carrying incidence, degree, coframe, connection, volume, support and current density,
with *"natural transports on every RA27-2 generator and composite"*, **derivation**
once the grammar is lawful, and importing smooth `(M,g)` as source **barred by
DoR-007**.

[YOURS] RA27-3 now has its generators to quantify over — A0/A1/A2 — which is real
progress and the only thing LL1 unblocks for it. It is **not** fully unblocked: its
transports must be natural on exactly the arrows whose measure transport §2 finds
unproven, so RA27-3 inherits the finding rather than escaping it. The honest statement
is **RA27-3 = generators supplied; demand otherwise unchanged and now carrying §2's
finding as a prerequisite.**

---

## 4. LL4 — THE ADOPTION LEDGER

| # | Element | Adopted or derived | Authority |
|---|---|---|---|
| 1 | **Directedness of `Ref_a`** | **ADOPTED AXIOM** | `FC` `31e42812…`, FC-1 — "the one element Q-624 proved stock cannot supply" |
| 2 | **Shape-regular admission class** | **ADOPTED** | `FC` FC-2 |
| 3 | **The preregistered relaxation condition** | **ADOPTED**, and recorded before any computation exists | `FC` FC-2 |
| 4 | `Ref_0`'s arrows (A0) | DERIVED / BUILT | `JREF` `8dd59b35…[12001,12049)` |
| 5 | A1, A2 as licensed moves | LICENSED of record | `V011` `aa7c6d49…[46882,47019)` |
| 6 | P1 cells shrink | DERIVED from the moves' construction | §1.3 |
| 7 | P2 zigzag equivalence | CONSTRUCTED (standard closure; no new content) | §1.3 |
| 8 | Measure transport along P3 | **NEITHER** — the finding | §2 |

```text
ADOPTION LEDGER = 3 adopted entries (1-3), all citing DECISION_RA27_2_ADOPTIONS.
Nothing else in this build is adopted.
```

### 4.1 Named refusals

[YOURS] Each of these was available and each is refused:

1. **Patching the transport.** A rule assigning `F` on sub-faces would make LL2 pass in
   one line. It would be authoring the refinement bridge, which `4d` records as
   underived and which no decision authorises. **Refused.**
2. **Reading `DEC`'s "additive, extensive form" as subdivision-invariance.** It is
   extensivity over a fixed cellulation; `BATT` names precisely the gap between the
   two. I made this over-reading at 725 and will not repeat it to rescue the build.
3. **Using the third C_ref family** to supply common refinements directly. Barred as a
   source, TYPE-R. **Refused.**
4. **Booking RA27-2 as discharged on four of five D012 items.** Four are supplied; the
   object as demanded is not delivered. **Refused.**
5. **Treating directedness as derived** because P2's zigzag makes it *look* natural. It
   is adopted, and §1.3 says so inside the object.

---

## 5. GROUNDING, JURISDICTION, VERB AUDIT

### 5.1 Grounding

| # | Step | Source + span | Tag |
|---|---|---|---|
| 1 | The two decisions' content | `31e42812…`, `112e6acb…` (sidecars OK) | PROVABLE |
| 2 | `Ref_0`'s arrows; BUILT status | `8dd59b35…[11610,11743)`, `[12001,12049)` | PROVABLE |
| 3 | The two licensed moves | `aa7c6d49…[46882,47019)` | PROVABLE |
| 4 | The third family barred as source | `430f0971…[20690,20930)` | PROVABLE |
| 5 | T11's law is a change-of-coframe law | `aa7c6d49…[46183,46387)` | PROVABLE |
| 6 | T11 does not derive the refinement bridge | `430f0971…[21855,21975)` | PROVABLE |
| 7 | T11's gap IS the measure's refinement functoriality | `14ddfc15…[4496,4636)` | PROVABLE |
| 8 | The failure mode: fine on a fixed cellulation, degrades under subdivision | `14ddfc15…[4321,4455)` | PROVABLE |
| 9 | The `xi`↔`F` relation carries a remainder | `aa7c6d49…[45848,45901)` | PROVABLE |
| 10 | No rule for the face field under subdivision | §2.6, writer-excluded counts | PROVABLE |
| 11 | D012's RA27-2 demand | `74bbb7aa…[44324,44664)` | PROVABLE |
| 12 | D012's RA27-3 demand | `74bbb7aa…[44665,45007)` | PROVABLE |
| 13 | A P3 arrow is a subdivision, not a frame change | §2.3 | PART-PROVABLE |
| 14 | Both generators fail transport identically | §2.7, from 5–8 + 13 | PART-PROVABLE |
| 15 | The 725 over-reading, and that FC-1's premise rests on it | §2.4 | **YOURS** |
| 16 | `Ref_a`'s closed statement | §1.3 | PART-PROVABLE |
| 17 | P2 zigzag; P1 by construction | §1.3 | **YOURS** |
| 18 | RA27-2 not discharged | §3.1 | PART-PROVABLE |
| 19 | J2: domain yes, truth condition no | §3.2 | PART-PROVABLE |

```text
GROUNDED_STEPS = 17 / 19
YOURS, NAMED: 15 (the self-correction), 17 (the two constructions).
```

### 5.2 Jurisdiction check

**The adopted directedness axiom.** Applied only where `FC` authorises it, marked
adopted inside the object, and never used to make a derived claim. Its jurisdiction is
the index's arrows; I did not let it reach the measure.

**The T11 measure law.** Applied strictly inside its own quantifier — *"for a general
coframe"*. §2 is the record of refusing to stretch it past that quantifier, which is
the same discipline I applied to JD-3's four obligations at 713 and for the same
reason.

**DoR-007 and the TYPE-R bars.** Untouched. No smooth structure imported; the third
family unused; no free/formal generator substituted.

**R9 / R9-JII.** §3.2 records the carrier still PENDING and declines to read a domain
as a truth condition. The finding at §2 is stated as *not proven*, never as *false* —
the refinement functoriality may well hold; nothing here shows it fails.

### 5.3 Self verb audit

| Verb or status | Warrant |
|---|---|
| `BUILT` / `DELIVERED` | `Ref_a`'s closed statement, which does not depend on LL2 |
| `ADOPTED` | three entries, each citing `DECISION_RA27_2_ADOPTIONS` |
| `FINDING` / `BUILD STOPPED` | LL2's own instruction, on two non-Dario sources |
| `not proven` | the transport — never `false`; §2 shows it underived, not refuted |
| `blocked (named)` | RA27-2, with the blocking object named |
| `refused` | five named refusals, §4.1 |

[YOURS] Disclosures against myself:

1. **The premise this build failed on is one I supplied.** My 725 §1.3 told the
   principal the measure half was settled and that the index need only be "a system the
   derived measure already transforms correctly along". FC-1 attached its transport
   clause to that. The sealed text says the opposite, and one of the two sources saying
   so — `BATT` — I had already read and cited in the same package for a different
   sentence. **I read the file that contained the refutation and did not see it.**
2. **I over-read `DEC` and I quoted it approvingly twice.** *"The measure's own
   stitching is done"* is a strong sentence about extensivity on a fixed cellulation.
   `DEC` never says `subdivision`. That distinction is the whole of §2.
3. **A patch was one line away and I refused it.** Assigning `F` on sub-faces would have
   let this artifact report a completed build. It would also have authored the exact
   object the corpus records as underived, inside a relay that told me a failure is a
   finding and not a patch.
4. **P1 and P2 are my constructions, not adoptions**, and §1.3 marks them. If the
   registrar disagrees about P1, it becomes a fourth ledger entry and nothing else
   moves.
5. No verb here proves, authorizes, computes, binds a member, forms a common cell,
   evaluates a junction map, adopts anything beyond the decision's three, or grants a
   seal.

```text
INDEX = built (closed statement at §1.3; adoption ledger 3 entries)
MEASURE_TRANSPORT = FINDING (build stopped) — both generators; the decision's premise
    that T11's pullback naturality is the transport law is unsupported: T11 derives a
    CHANGE-OF-COFRAME law, the P3 arrows are SUBDIVISIONS, and the corpus names the
    missing property as T11's own gap (4d "does not derive ... the refinement bridge";
    BATT "T11's gap is FUNCTORIALITY OF A MEASURE")
RA27_2 = blocked (named): the measure's refinement functoriality. Four of D012's five
    demands are supplied (§3.1) and the object as demanded is not delivered
J2_DOMAIN = instantiated (P2's classes are the re-presentation family); NO truth
    condition on it absent transport; R9-JII carrier remains PENDING on its
    common-cell quantifier — this build does not make the junction test runnable
T_REF_REMAINDER = stated (§3.3), incl. the exhaustion-vs-refinement gap untransported
    and the S5.3 burden undischargeable here
RA27_3 = generators supplied; demand otherwise unchanged and now carrying §2's finding
    as a prerequisite
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+5 disclosures at §5.3)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
