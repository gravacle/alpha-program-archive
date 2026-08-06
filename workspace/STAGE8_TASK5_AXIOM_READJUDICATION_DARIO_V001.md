# STAGE 8 / TASK 5 / STEP 7 — THE AXIOM RE-ADJUDICATION — DARIO V001

Lane: Dario (Claude Opus 5), cross-family review/adjudication lane
Task: PASTE 598 / Task 5 / Step 7
Authority: DoR-020-A8. **THIS ARTIFACT ADOPTS NOTHING, RATIFIES NOTHING, AND REGISTERS NOTHING.**
Custody: the adjudication that gates DoR-020-A2. No preference between arms is imposed.

```text
REGISTER_HEAD = Q-528
AXIOM_V002_VS_34 = 32 PASS_OUTRIGHT + 2 PASS_CONDITIONAL (N2, N8)
                   + 0 NEEDS_SUPPORT_GUARD + 0 FAIL   [34/34 satisfied]
ARM_A = ADOPTABLE, and what it discharges is exactly A_scope (+1 NOTE)
ARM_B = typed: ROUTE-CLOSURE, NOT REFUTATION
A2_CLAUSE_SET = ASSEMBLED (9 clauses; 8 sealed-and-citable, 1 referent-unbound)
READY_FOR_A2_RULING = yes
VERB_AUDIT_SELF = CLEAN (+1 CORRECTION TO MY OWN RECORD — see §0.1)
MEMBER_BOUND = false ; FIXED_POINT_EXECUTED = false ; END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MACHINERY_APPEAL = none of my own
```

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-528 | verified |
| Axiom V002 = `a681c784b451790c1163d083865988d2256170d1f0c468609b9a803864a0ab4b` | **verified before reading** |
| 34-constraint arm = `96cd90b5bdcc2b77f510ebd21882b215aa5b70c944c9d58b2bdd8855fd52bf11` | verified |
| First adjudication = `9fe38e932a4c892b1cd9cefec3977bffdd562db1441fdd477bbe5b31035c0a6d` | verified — it is `STAGE8_TASK5_EQ6_AXIOM_ADJUDICATION_LANE1_V001.md` |
| Membership V002 = `9b019ae3…` ; my confirmation = `1e9ce3ce…` | verified |
| Output name collision (workspace + cleanroom) | none — clear to write |

### 0.1 CORRECTION TO MY OWN RECORD — the PASTE 577 artifact **is** of record

[PROVABLE] **I was wrong, three times, and the correction matters.**

At Q-517, Q-521 and Q-527 I disclosed that
`STAGE8_TASK5_AUDIT_V002_REVIEW_DARIO_V001.md` (PASTE 577) had *"never been
written, sealed, or mirrored"* because its `Write` returned a
classifier-availability error, and I stated that *"that relay's verdict is not of
record."* **That disclosure is false.** Verified this relay:

```text
workspace  file present, 23,853 bytes
cleanroom  file present, 23,853 bytes, same timestamp
computed   af955f8159e1cc4c464966d38070ddbda501828b39630a9f585e86ce7693e610
seal       af955f8159e1cc4c464966d38070ddbda501828b39630a9f585e86ce7693e610   (match)
cited      STAGE8_TASK5_GAMMA_H_ROUTE_LANE3_V001.md:71 keys it as input `RV2`
           under exactly that hash
```

The artifact is complete and substantive: it grades
`AUDIT_V002 = DEFECTIVE (+2 substantive, both in the CONSERVATIVE direction)`,
carries `(M9) = EXISTENTIALLY TRIVIAL off chi = 0` and
`(M5;Q) = VACUOUS under (M2)`, and closes with my own disclosed defect — that my
574 modulus fix was offered as a disjunction whose arms are not independent.

**Consequences I must state plainly.** (i) The Write succeeded despite the error
I saw; I reported the failure without re-checking the filesystem, and then
carried that unverified report forward into three sealed artifacts. (ii) A
downstream build has been consuming the artifact as a hash-keyed input while my
lane was telling the record it did not exist — a live contradiction now resolved
in favour of the file. (iii) Its content **is** of record and may be relied upon,
including by this adjudication. (iv) My three prior disclosures should be read as
withdrawn; the register may wish to note the withdrawal where they were sealed.

The general lesson, which I book against myself: **a tool error is a report about
a call, not an observation about the filesystem.** I should have verified before
disclosing, and certainly before repeating.

**Method disclosure.** I re-walked the kills, the FC12 strike and re-homing, Step
1's conditional discharge, and every clause of §3 personally, and ran a parallel
adjudication (13 agents, adversarially verified). Where a refuter overturned a
finder I took the refuter's reading only after checking the sealed text myself.

---

## F1. THE 34 CONSTRAINTS RE-WALKED

### F1.1 Enumeration and result

The standard states its own identifiers: `MUST = 16 constraint families (M1–M16)`
and `MUST_NOT = 18 exclusions (N1–N18)` — 34 items.

| Category | Count | Items |
|---|---|---|
| PASS_OUTRIGHT | **32** | M1–M16, N1, N3–N7, N9–N18 |
| PASS_CONDITIONAL | **2** | N2, N8 |
| NEEDS_SUPPORT_GUARD | **0** | — |
| FAIL | **0** | — |

The two conditionals are the honest ones: `N2` and `N8` hold *because the
membership statement remains an implication*, and `N8`'s conservativity of record
is guard-relative.

### F1.2 The structural finding — and it decides how A2 must be argued

[PROVABLE] **No constraint in the 34 requires the support-qualified guard. Under
either arm the axiom satisfies the standard 34/34.**

The reason is structural, not lucky. Every one of the 34 is a constraint on the
axiom's **form** — the shape of its antecedent, the shape of its conclusion, or
what it must not assert. Not one requires the guard to be *inhabited* by any
datum. `PASS_CONDITIONAL` and `NEEDS_SUPPORT_GUARD` are therefore largely
unavailable as grades here: there is nothing in M1–M16/N1–N18 that a membership
implication or a guard amendment could repair.

**Consequence for the ruling:** the fork **cannot be decided on the 34**. The
inhabitance question lives in the constraint arm's §1.3 (the minimal-lawful-domain
requirement, a forcing but not an M-row) and §7 adjudication standard, and in the
first adjudication's T3/T4/T5 heads. An A2 ruling that argued from the 34 would be
arguing from the one instrument that is silent on the question actually at issue.

### F1.3 The two original kills

**M16 / N7 — CLOSED, and the exclusion is re-homed rather than lost.** I checked
this personally because a struck condition whose content silently vanishes is a
loss, not a repair.

The first adjudication's kills were a single defect seen from two sides: `M16`
(*"FC12 makes its interval/convex-or-AC branch condition part of EQ6
eligibility"*) and `N7` (*"FC12 imports exactly the branch-regularity clause
reserved to `C_ret`"*). Its own repair specification was: remove FC12, and state
that disconnected return data remain eligible for A2 and fail only when `C_ret` is
separately attempted.

V002 executes both:

> `FC12` | **STRUCK (M16/N7).** `FiniteCoherent_020` contains no condition about a
> stationary-return domain, connectivity, interval/convex structure, absolute
> continuity, branch regularity, return, modulus, or fixed point. The number is
> retained only so all other cross-references remain stable.

and the propagation ledger records the re-homing explicitly — the final board
*"says axiom silent / `C_ret` reject"*, which is precisely where M16's standard
said the exclusion belongs. The exclusion has a home: the independent stationary
return certificate, separately sealed at `b569a89e…`, itself honestly typed
`CERTIFICATE = BLOCKED_AT_INHABITANT`. Retaining the number without the condition
is good hygiene against renumbering drift. **Both kills stay closed.**

**The vacuity kill (T3/T5-triviality, and T4 on Step 1) — resolution differs by
arm, and must be stated separately.**

- **Under ARM A:** the full-extent demand is removed, so the guard no longer
  demands FC11 where it cannot be met. The vacuity kill is **resolved in form**:
  the resulting statement is not vacuous *by construction*. But see N1 below — it
  is not thereby made *non-vacuous in fact*, because the support it retreats to is
  not established nonempty.
- **Under ARM B:** `ANTE_full` is geometrically unsatisfiable, so `(T0)` is
  **permanently** vacuous as a material implication. The kill is not resolved in
  the sense of being removed; it is resolved in the sense of being **honestly
  typed as permanent incompleteness**. That is a legitimate resolution — the
  program's own discipline says an unformed antecedent is not a passed clause —
  but it is a different thing from repair, and the ruling should not conflate them.

---

## F2. THE TWO ARMS, ADJUDICATED SEPARATELY

### F2.1 ARM A — the axiom adopted over the SUPPORT-QUALIFIED GUARD

**What exactly the amended guard says.** The amendment is **exactly two conjunct
changes and nothing else**:

1. **FC11's quantifier** is replaced. The ratified row — *"On overlaps and common
   refinements, the six generator components agree as one finite fiber-product
   term, including the contact cocycle"* — is demanded only on `D_form^cert(L)`,
   per `(D3.6)`.
2. **FC10's J7 row** is demanded only at `FORM_stage(L)` / `FORM_arrow(L)` /
   `FORM_route(L)`, per `A_J7`.

FC1–FC10 and FC13 are untouched; FC12 stays STRUCK. The support is
`D_form^cert(L) := {D ∈ D_cert : every boundary e ∈ A_RP^+(L)}`, with
`A_RP^+(L)` built from `P(L) := {X : m_T,X(L) ≠ 0}`. Out-of-support positions
carry four typed residues and **never a vacuous pass**.

**Which constraints it satisfies that the unchanged guard does not: none at the
34-constraint level.** Its one real gain is at constraint-arm §1.3: under ARM B
the minimal-lawful-domain containment is *proved* unavailable by the only proved
route, for every `L`; under ARM A it returns to **TYPE-U**. **ARM A converts a
proved permanent violation into an open question. It does not satisfy it.**

**What Step 1 then discharges — exactly `A_scope`, and nothing else.** V002 is
explicit: a support-qualified A2 *"would discharge `A_scope` and replace/remove
the false full-extent condition `A_extent`; **it could not supply `A_vi`,
`A_pkg`, `A_J2`, or `A_J7`**."* So `ANTE_support` moves from FALSE to
**UNDISCHARGED**, not to true, and `(S2)` — Step 1 in conditional form — remains
without a discharged antecedent.

**What an adopting text must freeze.** V002 names the list: `(D3.4)`, the O1/O2
out-of-scope board, `CR1`–`CR7`, and the corresponding conditional Step 1
consequent, explicitly. To that the M9/no-selection row adds one load-bearing
item: the typing of the `L`-formulas as *"predicates inside an antecedent"* that
*"do not produce `L`"* is presently a property of the **membership artifact**, not
of the guard; if ARM A is taken, freezing that typing into the guard text is
required to keep the amended guard clear of selection.

**What the escrow inherits.** The independent `C_ret` certificate remains
downstream and is *"not smuggled back into the membership guard"* — the M16/N7
discipline survives the amendment. Neither arm can inhabit either route family,
build ExtSrc, form or evaluate the seed, compare Γ routes under R9, execute
`C_ret` Steps 3–4, certify the computational witness, run Steps 5–12, bind a fixed
point, perform an end test, or evaluate a number.

**ARM A verdict: ADOPTABLE.** Its content is lawful, its amendment is minimal and
exactly specified, it flips no constraint, and it buys precisely one package.
Subject to N1.

### F2.2 ARM B — the axiom retained over the UNCHANGED GUARD

**What is closed forever — exactly one thing, plus its definitional dependents.**
`A_extent`; and by containment `ANTE_full`, the discharge of `(T0)`/`(D6.2)`, the
composed Step-1 statement `(S2)`, and the unchanged-guard branch of `CR2`. FC11
quantifies over *"overlaps and common refinements"*, and `I_F` clause (v) puts the
two built `D_CC` common refinements in the datum's arrow set, so those cells are
**demanded**; by the leftmost-factor geometry they lie outside `D_form^cert(L)`
for every `L`.

**The exact type of the closure — and this is the item the ruling most needs
stated precisely:**

> **ROUTE-CLOSURE, NOT REFUTATION.**

The only *proved sufficient condition* for FC11 — implication `(D3.6)` on
`D_form^cert(L)` — is permanently unavailable. But **no sealed text derives
"FC11 is false."** §4.3 types the acyclic position `NOT FORMED`; §4.4 says
inhabitance is *"not established"*; Part B declines to claim the family empty.
Therefore membership of `F_actual^+` is **PERMANENTLY UNDECIDED for this datum,
not permanently refuted.** My own re-review said the same of itself: the finding
*"is a claim about `A_extent`, not a claim that any family is empty."*

**What remains reopenable.** Everything else, blocked only by missing machinery:
`A_vi`, `A_pkg`, `A_J7`, the HOL route, ExtSrc, the seed end test, the four A9
gates, R9, the FC6 asymmetric far cell, the full `I_F` diamond enumeration, and
the exhibition debt on `Scope_component`.

**Which of the 34 ARM B leaves unsatisfied: none.** The only two constraint-level
kills were FC12 artifacts and are repaired by the strike.

**Is the axiom still coherent and adoptable as a text under ARM B? Yes.** An axiom
may be perfectly well-formed while its membership predicate is uninhabited by
present stock; the 34 test the former and are silent on the latter. ARM B's cost
is a permanently blocked *route*, not a defective *axiom*.

---

## F3. THE A2 CLAUSE SET — **ASSEMBLED (9 clauses)**

Nothing below is authored here. Each clause is cited to its sealed source.

| # | Clause | Sealed source | Status |
|---|---|---|---|
| 1 | **The guard** (per arm) | unchanged: axiom V002 `a681c784…` Part A. Support-qualified variant: membership V002 `9b019ae3…` §4.2, a CARRIED CANDIDATE | citable |
| 2 | **Deferral criterion + anti-excuse** | `73524d7a…` §300–303; anti-excuse restated `9c232579…` §300–301 | citable |
| 3 | **One-sided-trial rider + period cure's condition** | seed adjudication `e287b057…` §294–297; carried as `CR6` in `9b019ae3…` §6 | citable |
| 4 | **Period threshold, carried-conditional** | `73524d7a…` §311–314 | **text citable, referent not version-bound — see N2** |
| 5 | **Law-with-address + three-tier authority rule + three riders** | J7 adjudication `f76139e5…` §398–432 | citable |
| 6 | **FC11's supported treatment** | `9b019ae3…` §4.2–4.4, `(D3.4)`/`(D3.6)`/`(D3.7)` | citable |
| 7 | **CARRY-1** | JII `fdf20bd4…` §7.4; seven-row expansion `9b019ae3…` §6, incl. `A7: BOTH E_C branches affirmatively retained` | citable |
| 8 | **Cross-sector-unit obligation** | DoR-019 `NO_IMPLICIT_CROSS_SECTOR_UNIT`; obligation stated in my JII review `ba9430c1…` §K6.1 | citable |
| 9 | **Residue ledger** | `9b019ae3…` §4.3 (four typed positions + "no verdict" row) | citable |

**Clause 2, verbatim:** *a condition may be carried as pre-fixed-point undetermined
only if its subject term is **constructed** and the loop **produces** rather than
consumes it; and an unbuilt map is never a pre-fixed-point undetermination.*

**Clause 3, verbatim in substance:** a nonzero `q_T,RL` **confirms** (the anchor
exists, the typing dissolves, `A_RP^+` is inhabited); a zero does **not refute**
but exits the licensed lattice, because `chi_K^Mx` carries `q_T,RL` in a
denominator and the licensed case lattice has no infinite-`chi_K` cell — *"unless
an independent period route is formed"* (the period cure's condition).

**Clause 5** must be frozen whole or not at all: the principle, **plus** the three
riders (address intensional and upstream; address of the statement not of the
admitted family; every address carries an extensional obligation), **plus** the
three tiers (ratified-row re-address → principal ruling, full gate;
already-qualified guard row → no ruling needed; strike/no-op → recordable but not
callable an amendment). Written as one undifferentiated principle, tier two is a
doorway by which any lane could declare its row "already qualified" and
self-authorize.

---

## F4. FRESH ATTACK, SURFACE ANCHOR, VERB AUDIT

### N1 — FRESH ATTACK: ARM A's value is gated on the J-II obstruction

[PROVABLE — chain verified link by link from sealed text]

ARM A retreats FC11 from the full tower onto `D_form^cert(L)`. The question the
ruling must ask is whether that support is **inhabited**. It is not established,
and the chain that would establish it terminates in the obstruction I adjudicated
at Q-521:

```text
ARM A's FC11 row is non-vacuous
  <== D_form^cert(L) nonempty
  <== A_RP^+(L) inhabited, i.e. P(L) = {X : m_T,X(L) != 0} inhabited
  <== q_T,RL != 0                      [seed adjudication: nonzero => "A_RP^+ is inhabited"]
  <== Loc built                        [seed adjudication: "the seed and the (F3)
                                        defect are one missing object -- Loc"]
  <== (L0) the cross-sector symbol-to-cochain arrow   [the J-II TYPE-U obstruction]
```

Every link is sealed. And the record already reports the top of the chain as
undetermined: of the three executed prototypes, `D_CC^disjoint` and
`D_CC^contact` are **permanently out** (acyclic sources), and `D_RsubRsub` is
*"not known to lie in `D_form^cert(L)`"* because stock has **no formed physical
`L`**.

**Therefore ARM A does not eliminate the vacuity risk; it relocates it** — from
*permanently unsatisfiable* (ARM B) to *undetermined pending an object the J-II
adjudication types TYPE-U*. That is a genuine improvement, because undetermined is
reopenable and refuted is not, and it removes a proved violation of §1.3. But its
practical value is contingent: **if `(L0)` is never supplied, ARM A yields an open
question that can never be closed** — outwardly similar to ARM B, differing in
that ARM B knows its own status.

A second, independent exposure points the same way: `A_J2` carries an extent
clause of exactly `A_extent`'s shape (*"every rank-preserving arrow on which FC10
demands scalar J2 belongs to `A_RP^+(L)`"*). If any FC10-demanded rank-preserving
arrow touches an acyclic position, `A_J2` inherits the same permanence by the same
leftmost-factor argument — and **neither arm amends `A_J2`**. I flag this as an
exposure to be checked, not as an established result: I did not find a sealed
enumeration of FC10's demanded rank-preserving arrows against the acyclic
positions, and without it the question is open in both directions.

**This is not an argument against ARM A.** It is the price tag. ARM A buys
`A_scope`, removes a proved violation, and converts a closed route into an open
one; it does not buy inhabitance, and what would buy inhabitance is the J-II
cross-sector arrow. The principal should choose knowing that, which is why it
belongs in this adjudication rather than in a later surprise.

### N2 — NOTE: the period-threshold clause's referent is not version-bound

[PART-PROVABLE] Clause 4 is sealed and quotable as text, but it names its referent
only by its defects — *"its modulus is mis-stated, its two certs are unproved, and
its `Gamma` is unbuilt on both routes"* — and the record has moved under two of
those three. The modulus was repaired by chain-conformance audit V002; that repair
was then reviewed `DEFECTIVE ×2` (both conservative) — **in the PASTE 577 artifact
whose existence I wrongly disavowed, and which is therefore available to A2**. No
sealed line binds "the period threshold" to a version, and at least two candidate
"gate lists" exist without designation.

Freezing clause 4 verbatim would import a justification whose limbs no longer all
hold. The headline standing — `CARRIED_CONDITIONAL`, not adopted-for-certification
— **is** independently re-affirmed on the repaired object, so the clause's
*standing* is sound and only its *justification* is stale. Repair: designate the
version and the gate list. **Not a bar to ruling.**

### Surface anchor

Present. The residue ledger (clause 9) is the anchor's real work: four typed
positions plus an explicit "no verdict" row for unclassified consumer arrows,
with the acyclic position carrying a displayed geometric reason rather than a
vacuous pass. The distinction between *absence of proof* and *proof of absence* is
drawn correctly on both O1 branches, and ARM B's closure is typed as route-closure
rather than refutation on exactly that discipline.

### Verb audit on my own board

| My verb | Check |
|---|---|
| "34/34 satisfied" | Satisfied as **form** constraints. This is explicitly **not** a finding that the guard is inhabited, and I state that the 34 are silent on inhabitance. |
| `ARM_A = ADOPTABLE` | Adoptable as a **text**, with its purchase named exactly (`A_scope`, nothing else) and its contingency booked at N1. Not a recommendation. |
| `ARM_B = typed` | Typed, not graded. I record no preference; both arms satisfy the standard. |
| "closed forever" (ARM B) | **Route-closure**, not refutation — membership permanently *undecided*, not *refuted*. Stated wherever the phrase is used. |
| N1's chain | Each link cited to sealed text. The `A_J2` exposure is flagged as **unchecked in both directions**, not as an established second permanence. |
| `A2_CLAUSE_SET = ASSEMBLED` | Assembled by **citation**. Nothing is authored here; clause 4 is flagged as referent-unbound rather than silently frozen. |
| `READY_FOR_A2_RULING = yes` | Ready because both arms are typed, the standard is met under both, and the clause set is citable. It is not a claim that either arm resolves the mathematics. |
| §0.1 | A correction against myself, stated first and without hedging, including the general lesson. |
| Agent reliance | 13 agents; where a refuter overturned a finder I verified the sealed text myself before adopting either reading. |

---

```text
AXIOM_V002_VS_34 = 32 PASS_OUTRIGHT + 2 PASS_CONDITIONAL (N2, N8)
                   + 0 NEEDS_SUPPORT_GUARD + 0 FAIL
  (+M16 and N7 both CLOSED: FC12 struck to the first adjudication's own repair
   spec, exclusion re-homed to "axiom silent / C_ret reject" with C_ret's
   independent certificate separately sealed and typed BLOCKED_AT_INHABITANT;
   +the vacuity kill resolves IN FORM under ARM A and AS HONEST PERMANENT
   INCOMPLETENESS under ARM B; +no constraint in the 34 requires the
   support-qualified guard, so the fork cannot be decided on the 34)
ARM_A = ADOPTABLE (+discharges exactly A_scope and removes A_extent; supplies
   none of A_vi, A_pkg, A_J2, A_J7; converts a proved permanent violation of the
   minimal-lawful-domain requirement into TYPE-U; must freeze (D3.4), the O1/O2
   board, CR1-CR7, the conditional Step 1 consequent, and the "predicates inside
   an antecedent" typing of the L-formulas; +1 NOTE at N1)
ARM_B = typed: ROUTE-CLOSURE, NOT REFUTATION (+closed forever: A_extent and by
   containment ANTE_full, the discharge of (T0)/(D6.2), (S2), and CR2's
   unchanged-guard branch; +membership PERMANENTLY UNDECIDED, not refuted;
   +reopenable: A_vi, A_pkg, A_J7, HOL, ExtSrc, the seed, the four A9 gates, R9,
   the FC6 far cell, the I_F enumeration; +the axiom remains coherent as a text)
A2_CLAUSE_SET = ASSEMBLED (9 clauses; 8 sealed-and-citable, clause 4 citable as
   text but referent not version-bound)
READY_FOR_A2_RULING = yes
VERB_AUDIT_SELF = CLEAN (+1 CORRECTION TO MY OWN RECORD: the PASTE 577 artifact
   STAGE8_TASK5_AUDIT_V002_REVIEW_DARIO_V001.md af955f81... exists, is correctly
   sealed, is mirrored in both locations, and is hash-cited downstream as RV2;
   my three prior disavowals at Q-517/Q-521/Q-527 are WITHDRAWN and its content
   is of record)
```

The axiom meets the 34-constraint standard under both arms. The fork is therefore
not a question about the axiom's form but about which incompleteness the program
prefers to carry: ARM A's open-but-unclosable-without-J-II question, or ARM B's
known permanent route-closure. Both are lawful; the mathematics of each is
displayed above; the choice is the principal's.
