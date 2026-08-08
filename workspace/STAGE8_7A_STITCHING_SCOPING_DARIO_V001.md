# STAGE 8 / 7A / STEP 8 — THE STITCHING ARC: R9-JII REPAIRS ADJUDICATED, A27 REMAINDER SCOPED

**Lane:** Dario (Opus 5, cross-family from the Codex build lanes)
**Date:** 2026-08-08
**Scope:** PASTE 715 only — Part A the gate, Part B the scoping
**Custody:** archive-side read and write; the registrar owns any mirror
**Governing:** frozen preregistration `9f0d12b4…`; sealed R9-JII carrier `5f4979d5…`
**Charge:** re-derive, not trust. Scoping only; no derivation in this relay.

## Lead determination

```text
PART A  =  ALL THREE REPAIRS ADOPTED.  Nothing contested.  The gate opens.
           Plus the four span-drift findings adopted, and their root cause in my
           own pin-check method named at §1.4.

PART B  =  five RA27 targets mapped; strict linear dependency chain;
           FIRST TARGET = RA27-2, and specifically its SAME-REGION RELATION.

THE FINDING THAT MATTERS:  three independent sealed sources name ONE missing
object -- a relation saying when two complexes represent the same physical
region.  It is RA27-2's demand, it is the JREF build's diagnosed obstruction,
and it is the domain R9-JII's J2 quantifies over.  A27's remainder and U1's J2
are blocked on the same object.

THE COUNTERWEIGHT, STATED UP FRONT:  that object is the one the corpus itself
types as possibly requiring ADOPTION rather than derivation.  The first target
may terminate in an adoption request to the principal, not a certificate.  And
closing A27 would not, by itself, move U1 -- §2.7.
```

---

## 0. Preflight

### 0.1 Pickup-ACK, lane guard, relay

[PROVABLE] The new PICKUP-ACK rule was executed **before** source work:
`relay_outbox/715_ACK.md` was written carrying the relay number, this lane's name,
and the inbox digest.

[PROVABLE] The relay header names **DARIO**. Lane guard satisfied.

[PROVABLE] The relay was read only after its sidecar verified:

```text
relay_inbox/RELAY_PASTE_715_STITCHING_OPENS_DARIO_V001.md
  7e9f3b62f0aeac9ba1a5e0e39af708aedbdc902311e7e06aae4ee95567ab192a   shasum -c OK
```

[PROVABLE] `STAGE8_7A_STITCHING_SCOPING_DARIO_V001.md` and its seal sidecar were
probed before the write and returned ABSENT.

### 0.2 Pins verified before use

```text
ADJ    STAGE8_7A_R9JII_ADJUDICATION_CODEX2_V001.md    b5b4892c7842d06813b7…   sidecar OK
CARR   STAGE8_7A_R9JII_JOINT_LANDING_TEST_V001.md     5f4979d50c905c009c1f…   sidecar OK
S01    STAGE8_7A_JUNCTION_U1_SHARED_CORE_DARIO_V001.md ec96235121896d146e7f…  sidecar OK  (mine)
PREREG STAGE8_7A_OBS22_RECOGNITION_PREREG_V002_FROZEN.md 9f0d12b4556427eb…    unchanged
ATTACK STAGE8_TASK4B_METRIC_V005_RECHECK_LANE1_V001.md d2bbd0ebc7d9bb52…
F1SPL  supervision/DECISION_F1_SPLIT_K2_SLOT_2026-08-08.md e76746aeea351bf6…
SEAM2  STAGE8_TASK5_COMMON_SEAMS_LANE3_V002.md        2525096ba06973b70064…
D012   STAGE8_TASK6_A25_A27_SCOPING_LANE2_V003.md     74bbb7aa971554f83d5c…
D013   STAGE8_TASK6_RA25_2_RA27_1_FINITE_CERTS_LANE3_V001.md 7a07d3b8ac66baa1…
JREF   STAGE8_TASK5_JREF_AND_LOCAL_KERNEL_ESTIMATES_LANE2_V001.md 8dd59b35bb9f…
MATRIX STAGE8_TASK6_LINEAGE_V2_MATRIX_CODEX2_V001.md  fe4c083d915c00824575…
```

[PROVABLE] **A drift worth recording.** The settled-questions register has changed
since my 713 read: `6bf7c3bd…` (1,254,120 B) → `ee21e03b…` (1,258,261 B), the growth
being a Q-620 entry appended near the end. My 713 artifact pins the version it read,
which is correct content-addressed practice; I additionally re-resolved all four of
its register spans against the **successor** bytes and every one still carries its
quoted text, because the addition landed after the last cited offset. No 713 citation
is stale.

### 0.3 Gates

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

No common cell was formed. No junction map was evaluated. No derivation was performed
— this relay is scoping only. No member bound, no fixed point, no end test, no
numeric, no measured constant. No register, plan, tracker, git, commit or push action.
The frozen preregistration was not altered.

---

## 1. PART A — THE GATE: CONFIRM OR CONTEST

The relay requires each repair to be adopted **from bytes** or contested with the
sealed span supporting my original. I read each repair's cited source at its own
bytes before deciding. **All three adopt. I contest nothing.**

### 1.1 Repair 1 — J1, the hidden-reciprocal-pair precision — **ADOPTED**

My S01 J1 stated: *"Two separately declared units on one cell is the
paired-hidden-conversion attack, permanently armed by DoR-019."*

[PROVABLE] The attack's sealed definition, `ATTACK` `d2bbd0eb…[12504,13458)`, §5.3
"Fresh attack - paired hidden conversions":

```text
An output-only dimensional test can be evaded by inserting two reciprocal
hidden arrows ... A scalar parameter `s` could be placed in the first arrow and
`s^(-1)` in the second. Their units and parameter cancel in the final round trip, so
a check only on the final Schur/output class would miss them.
... The pair must therefore be omitted or declared as a new seam field even when
always consumed together.
```

[PROVABLE] The attack requires **two conjuncts my sentence had neither of**:
hiddenness, and aggregate cancellation. And **declaration is the source's prescribed
cure** — *"omitted or declared as a new seam field"*. My sentence therefore names the
falsifier against the very act the falsifier's own source prescribes as the remedy.

[YOURS] I searched for any sealed span that would support my original reading — a
statement anywhere that two *declared* units on one cell are unlawful. **Searched
space: `workspace/*.md` and `supervision/*.md`, fixed-string probes on
`paired-hidden`, `paired hidden`, `reciprocal`, and `seam field`.** Nothing supports
it. There is no contest to make.

[YOURS] The severity is not cosmetic and I will not soften it: my formulation would
have **false-killed a lawful configuration** — two visible, separately declared units
that happen to differ. Inverting a control so that it fires on the behaviour it was
written to require is worse than leaving it out, and it is exactly what the anti-scar
guards in my own frozen preregistration exist to prevent. The corrected carrier's
J1 — *"either crossing is undeclared, or an undeclared reciprocal crossing pair is
hidden by aggregate cancellation"* — is right where mine was wrong.

### 1.2 Repair 2 — J3, the F1-split direction — **ADOPTED**

My S01 J3 stated the falsifier as: *"u(e) may not survive as a positive continuous
family (F1)."*

[PROVABLE] `F1SPL` `e76746ae…[99,1236)`, Ruling 1, verbatim in the operative part:

```text
The principal rules: F1 is SUPERSEDED BY SPLIT before the junction arc runs.
Successor F1':
  (i) the weak-rule reading STILL KILLS ...
  (ii) the scale-dependence reading ROUTES TO MEASUREMENT under the §5A
      preregistered kill conditions (K-1 coefficient class, K-3 locus) — it can
      still lose, by those conditions, never by mere family-hood.
```

[PROVABLE] Unconditional F1 is not current law, and the ruling says so with a
deadline that this relay is past: *"before the junction arc runs."* Citing raw F1 in a
junction-arc artifact is citing a superseded falsifier.

[YOURS] This is the sharpest of the three against me, and the reason is in the
ruling's own text: *"Finding of record (Dario, 707; registrar-verified)"*, and *"F1' is
authored into the frozen preregistration"* — **I made that finding, and I authored F1'
into the frozen preregistration at relay 709.** Six days later, at 713, I wrote J3
against the falsifier my own successor had replaced. A lane that installs a law and
then reasons past it is a worse failure mode than one that never had the law, because
the law's existence is what everyone downstream is relying on. Adopted without
reservation.

### 1.3 Repair 3 — J4, the explicit pair-adoption — **ADOPTED**

[PROVABLE] Two distinct defects, and both hold.

**The span.** My citation was `SEAM2 [1786,2042)`. Its bytes end
`"...route-return sections as one\n  a"` — the span **does not contain** the phrase
`associated-orbit object on each A8-common formed instance` on which my whole J4
depends. The corrected span `[1786,2100)` carries it.

**The status.** The R9-V002 repair is stated for the H/HOL route-return pair. It does
not name the Ward-symbol/`beta` pair. Applying its shape to this pair is an
**adoption**, lawful when done expressly, and not a fact recoverable from `SEAM2`'s
bytes.

[YOURS] My §2.4 did tag the transfer `[YOURS]` and my §2.5 called the comparison
"structurally identical", so the reasoning was typed honestly. But §2.5's sentence
*"J4 is grounded on a sealed repair"* reads stronger than the truth, which is: the
template is sealed, the application is adopted. The carrier's "TEMPLATE CARRIED;
application to this pair is adopted by this carrier and not back-dated into S08" is
the correct formulation.

### 1.4 The four span-drift findings — **ADOPTED**, with the root cause in my method

[PROVABLE] GF-01 through GF-04 all confirm. Each of my four spans stops mid-word and
fails to carry the token I displayed under it:

| Finding | My span | Ends | Token I displayed | Carried? | Corrected |
|---|---|---|---|---|---|
| GF-01 | `eaeffd37…[1069,1360)` | `…dimensionless parame` | `No invisible dimensionless parameter.` | **no** | `[1069,1365)` |
| GF-02 | `6ab72b0c…[737,878)` | `…exists undeclar` | `nu remains symbolic` | **no** | `[737,904)` |
| GF-03 | `6ab72b0c…[1140,1325)` | `…tagging an` | `paired-hidden-conversion` | **no** | `[1140,1533)` |
| GF-04 | `2525096b…[1786,2042)` | `…as one\n  a` | `associated-orbit object on each…` | **no** | `[1786,2100)` |

[YOURS] **The root cause is in my own pin check, and it is the finding I most want on
the record.** My 713 check tested `probe in bytes[a:b]` — that the span *contains a
short probe string*. It never tested that the span *covers the block I displayed under
it*. So a span could truncate the quote by any amount and still pass, which is exactly
what happened four times. The check passed 10/10 while four citations were defective.

The repair is one line and generalizes: **test the span against the whole displayed
block, not against a probe.** Concretely — extract the fenced text under each citation
and assert it is a substring of `bytes[a:b]`. I state it here rather than only fixing
it, because a verification method that can pass while its subject is wrong is a defect
of the same kind as the ones this lane exists to catch, and it was mine.

[YOURS] Related and disclosed: this is the third consecutive relay in which my *search
or citation scope* rather than my reasoning was the defect — 711's archive-boundary
question, 713's workspace-only search and character-vs-byte offsets, and now
probe-vs-block span coverage. The SEARCHED-SPACE CLAUSE now in force addresses the
first two. It does not address this one, which is why I name the span-coverage rule
separately above.

### 1.5 Gate verdict

```text
REPAIRS ADOPTED   = 3 / 3   (J1 hidden-reciprocal precision; J3 F1-split direction;
                             J4 explicit pair-adoption)
CONTESTED         = none
SPAN FINDINGS     = 4 / 4 adopted (GF-01..GF-04), root cause named at §1.4
GOVERNING CARRIER = 5f4979d5… stands unamended; this lane proposes no change to it
```

[YOURS] The corrected carrier is better than my proposal on every one of the three
counts, and my proposal's two virtues — the falsifier typing and the Q-126 warning —
both survive into it intact. That is the outcome the two-builder arrangement is for.
**Part B proceeds.**

---

## 2. PART B — THE STITCHING SCOPING

### 2.1 What A27 needs, at source

[PROVABLE] The PASS condition, `D012` `74bbb7aa…[48748,48902)`:

```text
A27_PASS iff
  RA27-1 + RA27-2 + RA27-3 + RA27-4 + RA27-5 + RA27-6
  jointly satisfy every elementary and common-refinement quantifier in C_ref.
```

[PROVABLE] RA27-1 is closed inside the held-out certificate; `D013`
`7a07d3b8…[20236,20480)` records C27.3, C27.4, C27.5 as `untouched / TYPE-U` and C27.6
as untouched/conditional. The board's named blocker, `MATRIX` `fe4c083d…[21469,21735)`,
is RA27-2 through RA27-6.

[PROVABLE] And the standing bar on shortcuts, `D012` `74bbb7aa…[48916,49123)`:

```text
No subset of the already decided local geometry can substitute for the
missing family-level theorem. Conversely, adoption of a premise does not count
as derivation of the theorem that consumes it.
```

### 2.2 The recurring missing object

[PROVABLE] Three independent sealed sources, two of them non-Dario lanes in different
tasks, name the same absent object:

| Source | Words |
|---|---|
| `D012` `[44324,44664)` — the demand | `Ref_a` with generators, **same-region relation**, common refinements, and composition |
| `JREF` `8dd59b35…[524,994)` — the build's diagnosis | *"no relation saying when two complexes represent the **same physical region**"* |
| `JREF` `8dd59b35…[13461,14260)` — the square that fails | *"no completed response assignment on geometric refinements, density map, or **common-region relation** is present"* |

[PROVABLE] `JREF`'s sealed status block, `8dd59b35…[14156,14268)`:

```text
RESPONSE_NATURALITY_ON_J_REF = NOT_BUILT / TYPE-U
COMMON_GEOMETRIC_REFINEMENT = NOT_BUILT / TYPE-U
```

[YOURS] The A27 remainder is not five independent gaps. It is one missing relation and
four consequences of not having it.

### 2.3 The five targets

| # | Object that must exist | Sealed sources bearing on it | Corpus typing | My effort estimate | Order |
|---|---|---|---|---|---|
| **RA27-2** | `Ref_a`: refinement generators, **same-region relation**, common refinements, composition, on addressed record complexes; plus a generator completeness/reachability proof | `D012 [44324,44664)`; `JREF [524,994)`, `[13461,14260)`, `[14156,14268)` | `TYPE-U`; *"grammar may require **adoption** if stock does not force it; one member may not be selected"* | **high**, and bimodal: the grammar may be an adoption, the completeness proof is a derivable certificate | **1** |
| **RA27-3** | full `J_ref` realization carrying incidence, degree, coframe, connection, volume, support, current density; natural transports on every RA27-2 generator and composite | `D012 [44665,45007)`; `JREF [524,994)` (skeleton BUILT / geometric arrows OBSTRUCTED); DoR-007 bar `JREF [921,1108)` | `TYPE-U`; **derivation** once grammar/premises lawful; importing smooth `(M,g)` as source **barred by DoR-007** | high; partially pre-built (the finite skeleton exists) | 2 |
| **RA27-4** | `eta_resp`, a named response topology/quotient, and an **exactly commuting** common-refinement square with zero naturality defect | `D012 [45008,45355)`; `JREF [13461,14260)` square `(D2-5)`, status `NOT_BUILT` | `TYPE-U`; *"exact equality must be **derived**; no boundary/contact or asymptotic tolerance may substitute"* — **no adoption escape** | high; pure derivation | 3 |
| **RA27-5** | named `tau_ker`, coefficient-boundary/contact object, density normalization, `CoefficientBoundaryCert`; uniform coefficient-residual support and boundary/four-volume decay on cofinal families | `D012 [45356,45772)` | `TYPE-U`; premises may require disclosed adoption; subextensivity must be **derived** and *"cannot weaken RA27-4"* | high | 4 |
| **RA27-6** | cellulation-independent local coefficient theorem plus negative controls, applied to **both legs** of every common-refinement cospan | `D012 [45773,46053)` | *"conditional theorem exists; premises absent"*; **derivation only; no hypercubic-only promotion**; *"flips A27 to PASS"* | highest; consumes 2–5 | 5 |

[PROVABLE] **Dependency order is the corpus's, not mine.** RA27-3 acts *"on every
RA27-2 generator and composite"*; RA27-5 *"cannot weaken RA27-4"*; RA27-6 *"apply
RA27-2 through RA27-5 to both legs of every common-refinement cospan"*. The chain is
strictly linear: **RA27-2 → RA27-3 → RA27-4 → RA27-5 → RA27-6.**

[PROVABLE] **Nothing supplies RA27-2 or RA27-5's certificate.** Searched space:
`workspace/*.md` and `supervision/*.md`, recursive, fixed-string. `Ref_a` occurs in
**3** files — `D012`, its Lane-3 companion `STAGE8_TASK6_A25_A27_SCOPING_LANE3_V002.md`,
and **this artifact**. Both pre-existing hits *demand* it; none supplies it.
`CoefficientBoundaryCert` occurs in **2** files: the demand in `D012`, and this
artifact. (Counts stated as a reader re-running the search after this seal will find
them; before this artifact existed they were 2 and 1.) By contrast `J_ref` (35 files), `eta_resp` (13) and
`tau_ker` (19) have substantial prior work, chiefly `JREF`.

[YOURS] That inversion is the scoping's most useful fact: **the root of the chain has
the least material behind it, and the downstream objects have the most.** Effort will
not fall where the file counts suggest.

### 2.4 U1 / R9-JII linkage — stated

The relay flags that the stitching rule is where any gluing of per-cell unit
declarations would live, and that the common-cell quantifier gap is adjacent. It is
adjacent, and more than adjacent in one place.

[PART-PROVABLE] **RA27-2 ↔ J2 — the same missing object.** The sealed carrier's J2
fires when the common value *"is not invariant under cell re-presentation"*. That
predicate quantifies over a family of re-presentations of a cell. The family is
`Ref_a`, and `Ref_a`'s same-region relation is precisely *"when two complexes
represent the same physical region"*. **Without RA27-2, J2 has no domain to quantify
over — it is not false, it is unquantifiable.** A27's root and U1's J2 are blocked on
one object.

[PART-PROVABLE] **RA27-4 ↔ J1 + J4 — the gluing site.** If a cross-sector unit is
declared per cell, the common-refinement square is exactly where two cells'
declarations must be shown to agree. So U1 *adds a demand* to RA27-4 that A27 alone
does not make: the exactly-commuting square must commute for the **declared-unit
assignment**, not only for the response. This is the stitching rule the relay names.

[PART-PROVABLE] **RA27-5 ↔ J2's admissible-data list.** F'-5's prohibited data — `ell`,
truncation level, cellulation-family index, cellulation geometric datum — is carried
verbatim into J2. RA27-5's certificate must avoid the same list, so the constraint is
now doubly binding rather than an A27-local hygiene rule.

[PROVABLE] **RA27-3 ↔ nothing new.** The transport of a declared unit along a
refinement arrow would ride on `J_ref`, but no sealed text states that demand. I
record the linkage as **absent**, not as weak, and do not manufacture one.

### 2.5 First target — **RA27-2**, and within it the same-region relation

[YOURS] Justification, strongest first:

1. **It is the unique root.** Every other row consumes it, by the corpus's own
   quantifiers (§2.3). No work on RA27-3–6 can be certified before it exists.
2. **It is shared with U1.** It is the only one of the five whose delivery would
   change U1's status — by making J2 quantifiable (§2.4). One object, two rails.
3. **Three independent sealed sources already agree it is the gap** (§2.2), so the
   target needs no new diagnosis before work starts.
4. **Nothing supplies it** (§2.3, searched space stated).
5. **It has a decomposition with a derivable certificate in it.** `D012` asks for
   both a grammar *and* a *"generator completeness/reachability"* proof. The grammar
   may be an adoption; the completeness proof, once a generator set is fixed, is a
   derivation. So the target yields a certificate even on the adoption branch.

[YOURS] **The counterweight, and it is substantial.** RA27-2 is also the row most
likely to terminate in a principal act rather than a proof. `D012` types the grammar
*"may require adoption if stock does not force it"*, and `JREF` independently reports
that *"a free or barycentric formal category can be authored, but it does not derive
the missing geometric data"*. A scoping that promised a derivation here would be
promising what two sealed sources say may not be available. **The honest deliverable
from target 1 is: a completeness/reachability certificate over a generator set,
plus — if the stock does not force the same-region relation — a surfaced adoption
request naming exactly what must be adopted and why the stock fails to force it.**

### 2.6 What closing A27 would and would not do for U1

[PART-PROVABLE] RA27-6 would produce a *derived* cellulation-independent local
coefficient — a new junction on the record cell. U1's second blocker is Q-126's
census: no junction is presently both **derived** and **`beta`-sensitive**.

[YOURS] Two things must be said, and the second is the one that matters.

The census is a census of the thirteen *present* interface quantities. It is not a
theorem that every future derived junction is `beta`-invariant, and I do not read it
as one.

But a cellulation-**independent** coefficient is, on its face, a quantity built to be
invariant under exactly the re-presentation freedom that a length normalization would
act through. **So the live risk is that A27 flips to PASS and U1 does not move at
all** — the new junction joining the derived-and-`beta`-invariant column with the
other twelve. That check should be preregistered now, before RA27-6 is attempted,
rather than discovered afterwards: *is the RA27-6 coefficient `beta`-sensitive?* If
the answer is no, closing A27 leaves U1 exactly where the 713 artifact left it, and
the program should know that before spending the effort, not after.

---

## 3. SEARCHED SPACES — declared with every absence

[PROVABLE] Per the SEARCHED-SPACE CLAUSE now in force, every absence claimed above was
produced by a stated search:

| Absence claimed | Searched space | Method |
|---|---|---|
| No sealed span supports my original J1 | `workspace/*.md` + `supervision/*.md`, recursive | fixed-string: `paired-hidden`, `paired hidden`, `reciprocal`, `seam field` |
| Nothing supplies `Ref_a` / RA27-2 | `workspace/*.md` + `supervision/*.md`, recursive | fixed-string `Ref_a`; 3 hits post-seal — two demands plus this artifact; no supplier |
| Nothing supplies `CoefficientBoundaryCert` | same | fixed-string; 2 hits post-seal — the demand plus this artifact; no supplier |
| No sealed text demands unit-transport along `J_ref` (RA27-3 linkage absent) | same | fixed-string `J_ref`, `transport`, cross-read against the carrier's J1–J4 |

[YOURS] Not searched, and therefore not claimed about: the cleanroom mirror, the
origin corpus outside the archive, and non-`.md` files other than those named in §0.2.
Absences above are archive-side, `.md`-scoped absences.

---

## 4. GROUNDING TABLE

| # | Step | Source + span | Tag |
|---|---|---|---|
| 1 | Paired-hidden attack requires hiddenness + aggregate cancellation; declaration is the cure | `d2bbd0eb…[12504,13458)` | PROVABLE |
| 2 | My J1 inverted it | S01 `ec962351…`, §2.5 J1 | PROVABLE |
| 3 | F1 is superseded by split before the junction arc runs | `e76746ae…[99,1236)` | PROVABLE |
| 4 | F1' was authored by this lane into the frozen prereg | `e76746ae…[99,1236)`; `9f0d12b4…` | PROVABLE |
| 5 | My J4 span omits the phrase J4 depends on | `2525096b…[1786,2042)` vs `[1786,2100)` | PROVABLE |
| 6 | R9-V002 does not name the Ward/`beta` pair | `2525096b…[1786,2100)` | PROVABLE |
| 7 | GF-01..GF-04 span truncations | four spans, each re-read at its endpoints | PROVABLE |
| 8 | My pin check tested probe-containment, not block-coverage | S01's own check, re-run | PROVABLE |
| 9 | A27 PASS condition | `74bbb7aa…[48748,48902)` | PROVABLE |
| 10 | No subset substitutes; adoption ≠ derivation | `74bbb7aa…[48916,49123)` | PROVABLE |
| 11 | C27.3–C27.6 untouched | `7a07d3b8…[20236,20480)` | PROVABLE |
| 12 | Board's named A27 blocker | `fe4c083d…[21469,21735)` | PROVABLE |
| 13 | RA27-2 … RA27-6 rows | `74bbb7aa…[44324,44664)`, `[44665,45007)`, `[45008,45355)`, `[45356,45772)`, `[45773,46053)` | PROVABLE |
| 14 | JREF obstruction names the same-region relation | `8dd59b35…[524,994)` | PROVABLE |
| 15 | JREF §2.4 square and its missing common-region relation | `8dd59b35…[13461,14260)` | PROVABLE |
| 16 | `RESPONSE_NATURALITY_ON_J_REF = NOT_BUILT` | `8dd59b35…[14156,14268)` | PROVABLE |
| 17 | DoR-007 bars importing the smooth background | `8dd59b35…[921,1108)` | PROVABLE |
| 18 | Strict linear dependency order | the row texts at 13 | PROVABLE |
| 19 | Nothing supplies `Ref_a` or `CoefficientBoundaryCert` | §3 searches | PROVABLE |
| 20 | J2 is unquantifiable without RA27-2 | `5f4979d5…` J2 + row 14 | PART-PROVABLE |
| 21 | RA27-4 is the per-cell-declaration gluing site | `5f4979d5…` J1/J4 + row 15 | PART-PROVABLE |
| 22 | RA27-5 inherits F'-5's list doubly | `5f4979d5…` J2 + `3c008ecc…[5052,5150)` | PART-PROVABLE |
| 23 | RA27-3 linkage is absent, not weak | §3 search | PROVABLE |
| 24 | First-target choice | §2.5 | **YOURS** |
| 25 | The A27-closes-without-moving-U1 risk, and the check to preregister | §2.6 | **YOURS** |
| 26 | Effort estimates | §2.3 right column | **YOURS** |

```text
GROUNDED_STEPS = 23 / 26
YOURS, NAMED, NOT BRIDGED: 24 (target choice), 25 (forward risk + proposed check),
26 (effort estimates).  None is used as a premise for any PROVABLE row.
```

---

## 5. JURISDICTION CHECK

**The paired-hidden control.** Written to stop a conversion hidden in a reciprocal
pair that cancels in aggregate. Present here — U1 is exactly a two-object crossing.
Its outcome space distinguishes false from cannot-see: undeclared pairs fire, declared
ones pass. And it permits the evidence: a lawful joint landing declares both units and
survives. **My original reading failed this third question**, which is how I know it
was wrong and not merely unsupported.

**F1'.** Written so a genuine running normalization is not killed for being a family.
Present. Three-way outcome by construction. Permits the true signal to appear.

**R9 / R9-JII.** Written so two independently formed returns are not declared equal
before a cell exists carrying both. Present — it is U1's whole shape. PENDING is not a
verdict, so inability to see is not converted into falsity.

**D012's "no subset substitutes; adoption ≠ derivation."** Written against closing a
family-level theorem with a local result. Squarely present in a scoping relay, where
the temptation is to call partial prior work on `J_ref`/`eta_resp`/`tau_ker` progress
on the chain. §2.3 records that work as prior material, not as discharge.

---

## 6. SELF VERB AUDIT

| Verb or status | Warrant |
|---|---|
| `ADOPTED` | each repair read at its own sealed bytes before deciding; the supporting span displayed |
| `contested: none` | I searched for spans supporting my originals and state the searched space; none exists |
| `unquantifiable` | J2 has no domain absent `Ref_a` — stated as a domain fact, not as falsity |
| `mapped` | five targets, each with object, sources, corpus typing, and order from the corpus's own quantifiers |
| `first target` | tagged YOURS; the justification and its counterweight both displayed |
| `risk` | §2.6 — a check to preregister, not a prediction of the answer |

[YOURS] Disclosures against myself:

1. **Three of my own errors are adopted in this artifact**, and one of them —
   reasoning past F1' six days after authoring it into the frozen preregistration — is
   the kind that damages a record more than a missing result would, because downstream
   lanes rely on an installed law staying installed.
2. **My J1 formulation would have false-killed a lawful configuration.** I inverted a
   control to fire on the behaviour its own source prescribes. Recorded at full weight
   at §1.1 rather than folded into the span findings.
3. **My pin check could pass while its subject was defective** (§1.4). Four bad
   citations survived a 10/10 check because it tested probe-containment rather than
   block-coverage. The generalized repair is stated so it can be adopted by any lane,
   not only fixed in mine.
4. **Scope, not reasoning, has been my failure mode three relays running.** 711's
   archive boundary, 713's workspace-only search and character offsets, 715's span
   coverage. The new SEARCHED-SPACE CLAUSE covers two of the three; the span-coverage
   rule at §1.4 is the missing third.
5. **I chose the first target knowing it may not yield a derivation.** RA27-2 is the
   root and the U1-shared object, and it is also the one the corpus says may need
   adoption. I state the likely terminus at §2.5 rather than let a scoping read as a
   promise of proof.
6. **My token counts moved when I wrote them down.** I first recorded `Ref_a` at 2
   files and `CoefficientBoundaryCert` at 1; this artifact then became a hit for each,
   so a reader re-running the search after the seal finds 3 and 2. Same self-inclusion
   effect I hit at 713. Corrected to the post-seal numbers with the pre-seal ones
   stated, because a census a reader cannot reproduce is not a census. The substantive
   claim — no artifact *supplies* either object — is unchanged.
7. No verb here proves, authorizes, computes, binds a member, forms a common cell,
   evaluates a junction map, or grants a seal. No derivation was performed.

```text
REPAIRS = adopted 3/3 (contested: none) (+4 span findings GF-01..GF-04 adopted)
RA27_TARGETS = 5 mapped (objects, sources, order: RA27-2 -> RA27-3 -> RA27-4 -> RA27-5 -> RA27-6)
FIRST_TARGET = RA27-2 (unique root; the only one shared with U1's J2; nothing supplies it;
               decomposes into an adoption-or-derivation grammar plus a derivable
               completeness/reachability certificate -- counterweight at §2.5)
U1_LINKAGE = stated (RA27-2 = J2's missing quantifier domain; RA27-4 = the per-cell
             declaration gluing site; RA27-5 inherits F'-5 doubly; RA27-3 linkage absent;
             and the A27-closes-without-moving-U1 risk at §2.6)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+7 disclosures at §6)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
