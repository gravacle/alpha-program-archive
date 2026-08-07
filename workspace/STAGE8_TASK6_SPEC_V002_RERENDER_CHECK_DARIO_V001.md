# STAGE 8 / TASK 6 / SUBGATE — BOUNDED CHECK OF THE EIGHT RE-RENDERED CRITERIA — DARIO V001

Lane: Dario (Claude Opus 5), cross-family custody reviewer
Task: PASTE 630 / Task 6 subgate — bounded check of spec V002
Authority: DoR-020-A8. **THIS ARTIFACT AUTHORIZES NOTHING AND LIFTS NO GATE.**
Custody: Codex 3 re-rendered per my Q-561/Q-565 reviews; I check the re-renders.

```text
REGISTER_HEAD = Q-565
RE_RENDERS = 5/8 CONFIRMED (+3 items: SP1-07, SP2-06, SP2-07)
SWEEP = NOT SOUND (+2 confirmed missed rows: C-B-V009-10, C-B-V010-06;
                    the class is wider than those two)
CARRIAGE = FULLY_ACCOUNTED
SPEC_V002 = NEEDS_V003
BUILD_READY = no (spec only; RD-22, builder custody and the runtime pin remain
                  principal acts and are untouched by this verdict)
VERB_AUDIT_SELF = CLEAN
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none of my own
```

**The re-render work is real and mostly excellent — five of eight are model
repairs.** But one re-render introduces a scope qualifier the sealed blocker does
not grant, with a concrete path to a PASS on zero derived IDs; and the 66/66
sweep that was supposed to find every remaining instance **missed at least two
rows of the very class it was built to find.** The second fact is the decisive
one: it means the eight re-renders are a *sample*, not the complete set.

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-565 | verified |
| V002 = `25e89ed24933d66fcb6991b83bb971775be834070f8570a8b89cd0248f22edb7` | **verified before reading** |
| Base V001 = `eb2073ebb4f23cbc0c0bfa20a36c482e24c59dc6b6e1ccbcd1ef1bd1150d0ecb` | verified |
| 1,391 lines (V001: 1,006) | verified |
| Output name collision | none — clear to write |

M-2 applied with all four false-negative guards; bounded zeros reported as bounded.

---

## 1. R1 — THE EIGHT RE-RENDERS — **5/8 CONFIRMED**

| Row | Positive half | Boolean | Class | Drift | Verdict |
|---|---|---|---|---|---|
| C-B-V011-SP1-07 | PARTIAL | YES | YES | **PRESENT** | **DEFECTIVE** |
| C-B-V011-SP2-03 | YES | YES | YES | NONE | CONFIRMED |
| C-B-V011-SP2-05 | YES | YES | YES | NONE | CONFIRMED |
| C-B-V011-SP2-06 | PARTIAL | YES | YES | — | **DEFECTIVE (gap)** |
| C-B-V010-03 | YES | YES | YES | NONE | CONFIRMED |
| C-B-V011-MR-04 | YES | YES | YES | NONE | CONFIRMED |
| C-B-V011-SP1-06 | YES | YES | YES | NONE | CONFIRMED |
| C-B-V011-SP2-07 | — | — | YES | **PRESENT** | **DEFECTIVE** |

All eight class assignments are unchanged and correct. All four newly-found rows
were **genuinely defective in V001** — the sweep did not inflate its own
thoroughness.

### 1.1 SP2-05 — verified by me, and a model repair

[PROVABLE] This was my sharpest Q-561 finding, so I checked it personally. Both
halves are repaired:

- The undefined term is **gone**. `all structural laws hold` survives in V002 only
  at line 610, inside the sentence *"The undefined criterion `all structural laws
  hold` has been deleted"* — a report of the deletion, not the defect.
- The missing predicate is **back with the right instrument**: my finding was that
  the blocker demands *"full source-record orientation covariance"* and the
  executable row had none. V002 now carries
  `r_enum_orientation := ENUM(G_orientation, p_orientation_complete)` plus
  `r_compare_orientation_index := COMPARE(r_enum_orientation.ids, p_orientation.index, empty)`.
- The criterion is now a **pure conjunction of opcode success bits**:
  `P0 and r_schema_global.success and … and r_compare_axioms.success`, including
  `r_kernel_covariance` and `r_kernel_quartic` — the KERNEL proof-replay
  instrument my standard named for the positive half.

That is precisely the repair the standard asked for, and it is worth saying so.

### 1.2 ITEM 1 — SP1-07 introduces an unbound scope qualifier (survived attack)

[PROVABLE] The sealed blocker, byte-extracted, reads:

> *"compose one global fermionic CAR source algebra with distinguishable
> record-cell factors and **derive** connected gluing, overlap, and ordering;"*

**No branch, no scope, no carriage carve-out.** The re-rendered row adds a
coverage manifest with modes `{DERIVED_IN_SCOPE, CARRIED_OUT_OF_SCOPE}` and a
required-scope manifest, permitting `CARRIED_OUT_OF_SCOPE` when
`M_required_scope.in_scope = false`.

**The concrete failure:** `M_required_scope`, `S_required_scope`, `M_coverage`,
`in_scope`, `DERIVED_IN_SCOPE` and `CARRIED_OUT_OF_SCOPE` occur **at that row and
nowhere else in V002** — not in `BASE`, not in the checks inventory, not bound to
any authority. And `SCHEMA` validates **fields, not values**, so no success bit
can force `in_scope = true` anywhere. A producer supplying a manifest that marks
every ID out of scope satisfies every conjunct, with `r_kernel` **vacuously
quantified — the row PASSES with the gluing/overlap/ordering derivation replayed
for zero IDs.**

[YOURS] The asymmetry inside the same re-render set is the tell: **SP2-05 binds
its completeness to the proof index itself**, leaving no excusable subset;
SP1-07 binds its completeness to a manifest that can excuse IDs. One of these is
a repair and one is a hole, and they were written in the same pass.

This is exactly the weakened-direction failure I flagged at Q-565: an overstated
demand gets noticed by the repairing lane, an understated one does not. A warrant
for a branch scope exists **downstream** in the source-parent packet, but the
sealed ledger blocker grants none, and the row cites no opcode tying its manifest
to that packet.

### 1.3 ITEMS 2 and 3 — SP2-07 and SP2-06

[PROVABLE] **SP2-07 — weakened drift, confirmed and load-bearing.** The attack
refuted one of the auditor's legs and over-claimed another, but the drift leg is
independently confirmed on the sealed and executable text.

[PART-PROVABLE] **SP2-06 — a gap, not a kill, at reduced severity.** V002 supplies
a named carrier for eight of the blocker's nine clauses; the reality-factor
carrier is the one left unnamed. Two of the three alleged grounds were refuted.

### 1.4 A quotation-discipline note, carried from Q-565

[PART-PROVABLE] Three block quotes presented as span-pinned (V002:571-575,
594-599, 616-620) silently drop opening or closing sentences without ellipsis.
**In each case the omissions are non-directional** — the omitted prohibitions are
separately instrumented — so I record this as a discipline lapse and do not charge
it as a defect. It is the same class I raised at Q-565 and it has narrowed, not
disappeared.

---

## 2. R2 — THE SWEEP — **NOT SOUND**

**Sample: 19 of the 58 CLEAN rows**, across all six families plus the `C-D-A35-*`
rows. Seventeen are CLEAN-earned. **Two are not, and both survived attack.**

### 2.1 C-B-V010-06 — a missed defect of the exact class the sweep was built to find

[PROVABLE] The row is **byte-identical to V001** and marked CLEAN. Its criterion
requires that *"a unique preparation is claimed only after all alternatives are
excluded by **displayed premises**"* — and `displayed premises` occurs **once in
V002: in that row**. Not in the opcode table, not in `BASE`/`P0`, not in any
schema block, and nowhere in the sealed ledger. `target-independent` is likewise
never defined.

Worse, the row's procedure says *"compare uniqueness proof"* while V002's own rule
states a proof *"contributes a Boolean only through `KERNEL(proof,axioms).success`"*
— and the row has **no KERNEL**, and the proof is not even among its
content-addressed inputs. That is the sweep's **own listed defect class**
(*"a missing proof replay"*), and it is the same shape the sweep did re-render
V010-03 for.

[PROVABLE] **And the drift is internal to V002.** Its own requirement-of-record
line keeps the verb — *"**Derive** a target-independent preparation domain"* —
while the criterion column asks only that the domain *"is target-independent"*,
instrumented by `TYPE`. That closes the scoping defence: it is V002's own
requirement line that carries the verb it then drops.

### 2.2 C-B-V009-10 — second missed row

[PROVABLE] Also byte-identical to V001, also CLEAN, its procedure invoking exactly
one opcode against a criterion whose conjuncts are not all normal-form
comparisons. Confirmed on the spec's own stated standard.

### 2.3 Why this is the decisive finding

[PROVABLE] V002 claims *"After the eight in-place replacements, **every PASS atom
in all 66 rows** is opcode-reducible under §2.2."* That is an affirmative claim
about every CLEAN row, so a single missed row falsifies it — and two are
confirmed.

[YOURS] The attack on V010-06 further warns the class extends to rows it did not
formally charge — `MR-06` (*"silently selects one"*), `SP1-04` (*"no phase is
silently set … proven phase-independent"*), `V010-10` (*"every certified
composite"*) — all carrying words V002's **own rule** says *"have no Boolean force
by themselves."*

**So the eight re-renders are a sample of a larger population, not the complete
set, and a single-row repair would leave the blanket claim false.** Whoever costs
the V003 cycle should scope it to the **class**, not to the named rows.

---

## 3. R3 — CARRIAGE — **FULLY_ACCOUNTED**

[PROVABLE] I re-diffed independently: `/usr/bin/diff -U 0` on V001→V002 emits
**exactly 36 hunks**, matching the declared 36-hunk table.

[PROVABLE] **The untouched-section claim verifies structurally.** Hunk old-side
positions against the three protected regions:

```text
runtime-pin §9.1        V001:484-514   nearest hunks 481(insert), 683   UNTOUCHED
authority firewall      V001:777       between 683 and 826              UNTOUCHED
aggregate rule          V001:813       between 683 and 826              UNTOUCHED
```

The hunk at `481,0` is a **pure insertion** before §9.1's heading with zero old-side
lines — it modifies nothing. So the runtime pin, the firewall and the aggregate
rule I confirmed at Q-559 and Q-561 are carried unchanged, and my prior
confirmations of them stand.

---

## 4. R4 — BATTERY

### 4.1 `F_PLDEC` and fences

[PROVABLE] Nothing in this check consumed a reader output, a desired outcome, a
measured value, or any physical quantity. The work is criterion-language auditing
and hash arithmetic. No descriptor was executed; V002 itself states it is *"a
criterion-language audit; no descriptor was executed."*

### 4.2 M-2, all four modes

Applied throughout. The two decisive absence findings (`displayed premises`,
`M_required_scope`) were each tested raw, whitespace-normalized, and in
hyphen/space/underscore variants, then read in context — and both are reported as
**bounded** findings over V002 and the sealed ledger, not as impossibility.

### 4.3 Self verb audit

| My verb | Check |
|---|---|
| `RE_RENDERS = 5/8` | Five are model repairs and I say so; three carry defects that survived adversarial attack. I did not round either way. |
| SP2-05 `CONFIRMED` | **Verified by me personally**, both halves — the deleted term and the restored ENUM/KERNEL instruments. My own sharpest prior finding, checked rather than assumed. |
| SP1-07 `DEFECTIVE` | The concrete failure path is displayed (PASS on zero derived IDs), and the intra-set asymmetry with SP2-05 is the evidence that it is a hole rather than a licensed scoping. |
| SP2-06 | Graded a **gap at reduced severity**, not a kill — two of three alleged grounds were refuted and I carry the refutations. |
| `SWEEP = NOT SOUND` | Two missed rows **confirmed on attack**; the wider class is flagged as the attacker's warning, not as my own charged finding. Sample stated: 19 of 58. |
| `CARRIAGE = FULLY_ACCOUNTED` | 36 hunks re-diffed by me; the protected-section claim verified by hunk position, not by trust. |
| `SPEC_V002 = NEEDS_V003` | Because the blanket 66-row claim is falsified and one re-render can pass vacuously — **not** because the re-render work is poor. It is mostly good. |
| `BUILD_READY = no` | Scoped to the **spec**. RD-22, builder custody and the runtime pin are principal acts, untouched by this verdict and not implied by it. |
| Quotation notes | Recorded as a **discipline lapse, expressly not charged**, because the omissions are non-directional. |
| Agent reliance | 9 agents; every proposed defect was adversarially attacked and I report post-attack state. One kill (`C-B-V009-12`) was **refuted** and the row stands CLEAN. I verified SP2-05, the carriage and the protected sections myself. |

---

```text
RE_RENDERS = 5/8 CONFIRMED (+3 items:
  SP1-07 introduces a {DERIVED_IN_SCOPE, CARRIED_OUT_OF_SCOPE} coverage manifest
    the sealed blocker does not grant -- the blocker says "derive connected
    gluing, overlap, and ordering" with no carve-out. M_required_scope,
    M_coverage and in_scope occur at that row and NOWHERE ELSE in V002, bound to
    no authority, and SCHEMA validates fields not values, so nothing can force
    in_scope=true. A manifest marking every ID out of scope PASSES the row with
    the derivation replayed for ZERO IDs. Contrast SP2-05 in the same pass, which
    binds completeness to the proof index and leaves no excusable subset.
  SP2-07 carries a confirmed, load-bearing weakened-direction drift.
  SP2-06 leaves the reality-factor carrier unnamed -- a GAP at reduced severity,
    not a kill; two of three alleged grounds were refuted.
  The other five -- SP2-03, SP2-05, V010-03, MR-04, SP1-06 -- are model repairs,
    and all four newly-found rows were genuinely defective in V001.)
CLASS_ASSIGNMENTS unchanged and correct on all eight.
SWEEP = NOT SOUND (+2 confirmed missed rows, both byte-identical to V001 and both
  marked CLEAN: C-B-V010-06, whose criterion turns on "displayed premises" -- a
  term occurring once in V002, in that row, and defined nowhere -- and which says
  "compare uniqueness proof" while V002's own rule requires a proof to contribute
  a Boolean ONLY through KERNEL.success, with no KERNEL present and the proof not
  even a pinned input; and C-B-V009-10. The drift is internal: V002's own
  requirement line says "DERIVE a target-independent preparation domain" while
  its criterion asks only that the domain "is target-independent". The class is
  wider than these two -- MR-06, SP1-04 and V010-10 carry words V002's own rule
  says have no Boolean force. V002's claim that "every PASS atom in all 66 rows
  is opcode-reducible" is therefore false, and the eight re-renders are a sample,
  not the complete set.)
CARRIAGE = FULLY_ACCOUNTED (36 hunks re-diffed independently, matching the
  declared table; the runtime-pin section, the authority firewall and the
  aggregate rule are structurally untouched -- the nearest hunk, 481,0, is a pure
  insertion before §9.1's heading that modifies nothing)
SPEC_V002 = NEEDS_V003 (scope the repair to the CLASS, not to the named rows:
  a single-row fix leaves the blanket 66-row claim false)
BUILD_READY = no (readiness of the SPEC only; RD-22, builder custody and the
  runtime pin remain principal acts and are untouched by this verdict)
VERB_AUDIT_SELF = CLEAN
```

Five of eight re-renders are exactly what the standard asked for — SP2-05 in
particular deletes the undefined term and restores the missing predicate with an
ENUM completeness certificate and KERNEL proof-replay. The V003 cycle is needed
not because that work was poor but because the sweep meant to guarantee its
completeness did not, and because one repaired row can now pass having derived
nothing at all.
