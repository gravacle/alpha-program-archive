# STAGE 8 / TASK 6 / SUBGATE — BOUNDED CLASS-CHECK: THE SPEC V003 BINDING REPAIR — DARIO V001

Lane: Dario (Claude Opus 5), cross-family custody reviewer
Task: PASTE 635 / Task 6 subgate — bounded class-check of the A35 evaluator spec V003
Authority: DoR-020-A8. **THIS ARTIFACT AUTHORIZES NOTHING AND LIFTS NO GATE.**
Custody: Codex 2 repaired per my Q-567 findings; I verify. Bounded — not a fresh
full-spec review.

```text
REGISTER_HEAD = Q-571
NAMED_REPAIRS = 3/3 CONFIRMED
RE_RENDERS = 28/28 CONFIRMED (mechanical on all 28; semantic in full on 3)
BOUND_SAMPLE = NOT CLEAN (+2 rows: C-B-V010-14, C-B-V011-SP1-05)
PROTECTED+CARRIAGE = CONFIRMED (+1 false declared statistic)
SPEC_V003 = NEEDS_V004 (narrow; the binding architecture STANDS)
BUILD_READY = no (spec readiness only)
VERB_AUDIT_SELF = CLEAN (+2 self-caught near-miss over-claims, recorded at §6)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**The binding repair is real, and it is the repair I asked for.** The escape hatch
is dead under all four M-2 modes; the class was fixed *at the class*, not at the
row; and all twenty-eight re-renders carry criteria that are pure conjunctions of
opcode results. What blocks a clean STANDS is not the binding: it is one false
declared statistic, two rows graded BOUND against the spec's own stated rule, and
one "Requirement of record" line that still carries the convicted weakened parse.
All four are one-line repairs. None is an escape hatch, and none lets a producer
pass a row while violating its blocker.

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-571 | verified |
| Subject V003 = `f910815c84fd29d3dc6ca55f43ebe5d4c7015f457ddcde7bd7a69afdf81658dc` | **verified before reading**; sidecar matches |
| Base V002 = `25e89ed24933d66fcb6991b83bb971775be834070f8570a8b89cd0248f22edb7` | **verified before reading** |
| Blockers of record = `c09f2c246c48ddfd0df127da26a22f08ba9ffd44f5c2118c178a0a5eba5d00e8` | verified |
| Output name collision | none — clear to write |
| Line counts | V002 = 1,392 lines; V003 = 1,490 lines |

Archive-side only. The Documents tree was not touched.

---

## 1. C1 — THE THREE NAMED REPAIRS — **3/3 CONFIRMED**

### 1.1 SP1-07 — the escape hatch is genuinely dead

[PROVABLE] **M-2 mode 1 (fixed string).** All six scope identifiers of my Q-567
finding are present exactly once in V002 and **zero times** in V003:

```text
identifier              V002   V003
M_required_scope          1      0
S_required_scope          1      0
M_coverage                1      0
DERIVED_IN_SCOPE          1      0
CARRIED_OUT_OF_SCOPE      1      0
in_scope                  1      0
```

[PROVABLE] **M-2 mode 4 (hyphenation / identifier variant).** Zero hits in V003
for `in-scope`, `out_of_scope`, `out-of-scope`, `out of scope`, `inScope`,
`required_scope`, `requiredScope`, `scope manifest`, `scope_manifest`,
`coverage manifest`, `M_scope`.

[PROVABLE] **M-2 mode 3 (scope / self-reference).** The two surviving `in scope`
hits are **not** the coverage semantics: `:215` is about the title not truncating
a universal sentence, and `:1147` is the V008/V009 census remaining in scope. The
only surviving `*SCOPE*` identifier anywhere is `RESTRICTED_SCOPE` at `:458`,
unrelated to coverage. **The hatch has no residual spelling.**

[PROVABLE] **Completeness is bound so zero-derived-IDs cannot pass.** The
re-rendered row at `:488` closes the hole four ways:

```text
r_enum        := ENUM(G_overlap_order, p_complete)
r_nonempty    := EXACT(cardinality(r_enum.ids) > 0)
r_required_ids:= COMPARE(r_enum.ids, E_SP1_07.required_ids, empty)
r_proof_ids   := COMPARE(r_enum.ids, P_SP1_07.ids, empty)
for every d in r_enum.items:
    r_d     := KERNEL(P_SP1_07[d].proof, proof_axioms)
    r_cmp_d := COMPARE(r_d.conclusion, E_SP1_07[d], empty)
```

`r_nonempty` alone kills the zero-ID pass. `r_required_ids` is stronger: the
enumeration must **equal** the mandatory set with empty difference, so a narrowed
enumeration fails too.

[YOURS] **And the mandatory set is not producer-suppliable.** That was the residual
question, because `SCHEMA(s,x)` constrains fields and not values — the precise
weakness that made V002's row passable on zero IDs. It is closed at the class
level by `:340-342`:

> *"Every indexed manifest must carry the SHA-256 of the graph, grammar, proof, or
> result it indexes and must match the `P0`-verified supplied bytes."*

`E_SP1_07` and `P_SP1_07` are indexed manifests, so their contents are
content-addressed and `P0`-verified rather than declared. **SP1-07 is genuinely
rebound**, and the fix is architectural rather than local.

### 1.2 SP2-06 — the reality-factor carrier is a real consumed input

[PROVABLE] My Q-567 grade was a **gap**: eight of nine blocker clauses carried,
the reality-factor carrier unnamed and therefore consumed by nothing. V003 names
it as a content-addressed input — `(S_reality, E_reality)` with named factor
`rho_L`, carrier/domain `D_reality`, signature and resolvent hash — and, decisively,
**consumes it**:

```text
r_reality        := SCHEMA(S_reality, E_reality)
r_reality_domain := DOMAIN(E_reality.rho_L, E_reality.D_reality)
r_spectral       := SPECTRAL({E_reality, E_interacting_support})
```

Naming without consumption would have been vocabulary. `DOMAIN` and `SPECTRAL`
both receive the carrier, and the sign/positivity/durability/dressing/no-mass-shift
obligations are each a `KERNEL` replay compared to a pinned expected record. The
criterion is a conjunction of twenty-one success bits. **Class GATED-EXECUTION is
unchanged** — correct, since `SPECTRAL` is gated-only under the class discipline.

### 1.3 SP2-07 — the weakened direction is reversed, and the reversal is right

[PROVABLE] The sealed blocker, at ledger bytes `[23527,23774)`:

> *"7. Every load-bearing audit must be free of Python `assert`, agree under
> normal and optimized execution, run under a content-addressed isolated
> runtime, and pass a terminal seal. A sanitized but unsealed interpreter is
> not final closure."*

[YOURS] **The grammar is the whole finding.** `load-bearing` modifies **audit**,
not **assert**. So freedom from `assert` is *unqualified within a load-bearing
audit*. V002's drift shifted the modifier onto `assert`, which licensed keeping
any assert a producer deemed non-load-bearing — a weakening produced by a
misparse rather than by a judgment.

V003 restores the blocker's actual reading: `r_assert := M2(q_assert, {...})` with
criterion atoms `r_assert.success and r_assert.hits = empty`, and the spec states
that **no proof may relabel a hit as non-load-bearing**. All four legs are present
and bound: `RUNTIME` on the normal, optimized and independent-verifier contracts;
`COMPARE` on child manifests and verdicts under declared masks; closed receipt and
terminal schemas; and the terminal seal as `KERNEL(p_terminal, trust_root_axioms)`
with its conclusion compared to the expected seal record.

[YOURS] I record that I tested the opposite hypothesis first — that `hits = empty`
**over-demands** relative to a blocker saying only "remove load-bearing asserts."
The sealed span refutes that reading. This is a restoration, not an escalation.

---

## 2. C2 — THE TWENTY-EIGHT RE-RENDERS — **28/28 CONFIRMED**

### 2.1 The mechanical result, on all twenty-eight

[PROVABLE] I extracted the criterion cell of every one of the 28 re-rendered rows
and tested each atom against the spec's own reducibility rule. **Zero rows carry a
residual prose atom or a banned adjective.** Every criterion is a conjunction of
`P0`, opcode `.success` bits, named result fields (`.ids`, `.hits`, `.conclusion`),
`=empty` comparisons, cardinality tests, and finite universals over `ENUM` results.

```text
RE-RENDERED rows                        = 28
rows with residual prose/banned atoms   = 0
classes changed from V002               = 0
```

### 2.2 The class repair is at the class, not the row

[PROVABLE] This was my Q-567 instruction — scope the repair to the class, not the
named rows — and `:355-362` does exactly that:

> *"Words such as `certified`, `derived`, `proved`, `silently`, `displayed`,
> `target-independent`, `exhaustive`, or `all structural laws` have no Boolean
> force by themselves… A criterion atom using one of the listed adjectives must
> name its receiving opcode result or be deleted."*

Every adjective I convicted is named there, together with the routing rule: proofs
only through `KERNEL`, completeness only through `ENUM(grammar,cert)`, comparison
only through `COMPARE` on enumerated IDs or result records.

### 2.3 The three rows I read in full

[PROVABLE] **`C-B-V010-06` — my prior confirmed missed defect — is repaired.** Both
of its undefined terms now have receivers, and the proof is a pinned input:

```text
r_domain     := KERNEL(p_domain, proof_axioms)            <- "target-independent"
r_domain_cmp := COMPARE(r_domain.conclusion, E_prep.domain, empty)
for every c in r_enum.items:
    r_c     := KERNEL(P_competitor[c].decision_proof, proof_axioms)
    r_c_cmp := COMPARE({r_c.conclusion, r_c.used_axiom_hashes}, E_prep[c], empty)
```

`displayed premises` is discharged by comparing **`used_axiom_hashes`** against the
expected ledger — which is the correct instrument, since the defect was that a
uniqueness proof was demanded and the row had no `KERNEL` and did not even take the
proof as an input.

[PROVABLE] **`C-B-V011-MR-06` — "silently selects one" is discharged.**
`r_target := M2(q_prep_target, {...})` with `r_target.hits = empty`. Its
`CARRIED_FAMILY | DERIVED_SELECTOR` status record is **doubly pinned** — a proof
conclusion must equal it (`r_selector_cmp`) *and* it must equal the expected
ledger (`r_member`) — so the mode is not a free choice.

[PART-PROVABLE] **`C-B-V011-SP1-04` — a disjunction, but not the SP1-07 shape.**
`r_branch` admits `CLASSIFIED_ALL` or `RESPONSE_INDEPENDENT`. I examined this
closely because a mode disjunction is exactly where the old hatch lived. It is not
the same object: **each arm carries a replayed proof.** The cheap-looking arm still
requires `KERNEL(p_response_independent)` with its conclusion compared to a pinned
expected record, and `r_no_set.hits = empty` binds **both** arms at the top level.
That is disjunctive discharge, not an exemption.

[YOURS] I name it anyway as the structure to watch. V002's hatch was a disjunction
whose second arm required nothing; SP1-04's second arm requires a proof. The
distance between those two is one clause, and it is the clause a future editor
would be most tempted to soften.

### 2.4 Coverage boundary — stated exactly

[YOURS] My C2 confirmation is **mechanical on all 28 and semantic in full on 3**
(V010-06, MR-06, SP1-04), plus the three named repairs of §1, which are themselves
re-rendered rows — so seven of the twenty-eight were read against their blockers in
full. I did **not** read each of the remaining twenty-one against its sealed blocker
span individually. A breadth check was commissioned for that and did not return
within this relay. **I therefore do not claim row-by-row semantic verification of
all 28, and my `28/28 CONFIRMED` is a confirmation that every re-render satisfies
the binding standard mechanically and that every row read in full also satisfies it
semantically.** An honest partial with an exact stop point beats a complete-looking
artifact.

---

## 3. C3 — THE THIRTY-EIGHT BOUND ROWS — **NOT CLEAN (+2)**

### 3.1 What I tested

[PROVABLE] The board reconciles exactly: **66 rows = 38 BOUND + 28 RE-RENDERED**,
and all 66 IDs resolve to descriptor rows. Rather than the twelve required, **I
tested all thirty-eight** BOUND rows mechanically, then read the flagged ones.

### 3.2 The two findings

[PROVABLE] Two BOUND rows retain criterion atoms of the classes the spec's own rule
says require the explicit named form:

| Row | Retained atom | Class |
|---|---|---|
| `C-B-V010-14` | *"no `A^c`, multiplicity, or later conversion is selected or **silently** inserted"* | banned adjective |
| `C-B-V011-SP1-05` | *"the family is **exhaustive** in the declared class"* | completeness |

The spec states at `:364-369`:

> *"The compact notation does not excuse a proof, completeness certificate,
> enumerated comparison, or load-bearing adjective; those classes require the
> explicit named form used by the 28 V003 re-renders below."*

`silently` is on its own banned list; `exhaustive` is a completeness claim, which
"contributes only through `ENUM(grammar,cert).success`." **Both rows were graded
BOUND under a rule the spec itself says they do not meet.** That is the Q-567 class
persisting — in the sweep, not in the re-renders.

### 3.3 Severity — honestly reduced

[YOURS] These are **materially weaker than V002's SP1-07 hole, and I grade them so.**
In both rows the receiving opcode is *already present in the procedure*:
`C-B-V010-14` runs `M2` (which has a hit set), and `C-B-V011-SP1-05` runs
`ENUM` grammar **with an independent completeness certificate**. So the obligation
is **under-notated, not unbound**: no producer input passes these rows while
violating their blockers. The repair is to name the receiver in the criterion —
one line each — not to rebuild the row.

### 3.4 One row I examined and did **not** charge

[YOURS] `C-B-V010-09`'s criterion says *"every direction in one **certified**
neighborhood is covered…"*, and `certified` is on the banned list. I do not charge
it. The adjective modifies an **object whose certificate is a pinned input** — the
row takes a remainder certificate, replays the uniform theorem and bound under
`KERNEL`, and gives the full neighborhood to `DOMAIN`. That is a descriptive
qualifier on a bound object, not a Boolean floating free. Charging it would be
pattern-matching on a word instead of reading the row.

---

## 4. C4 — PROTECTED SECTIONS AND CARRIAGE

### 4.1 Protected sections — **CONFIRMED, and independently reproduced**

[PROVABLE] I did not take the declared pins on trust. I extracted each region from
both files by its own headings and hashed it myself. **All three of my
independently computed digests equal the declared pins exactly, and all three
regions are byte-identical between V002 and V003:**

```text
region                lines   identical V002/V003   my digest == declared pin
runtime-pin §9.1        31           yes                     yes
authority firewall      18           yes                     yes
aggregate rule §9.5     20           yes                     yes

712a861aaf5f2f43590f41405435663dff8efd52a93e30d33cc2399636442172   §9.1
a9e7e50afb466ead16c43b45352d1c04273bb9c3e5671f5f7c386df70cdf0afa   firewall
bfad44417f766cc97a8942a8ffab7f9accd5791a2c2f1169a6534f3643543648   §9.5
```

### 4.2 Carriage — the hunk claim holds; one declared statistic is false

[PROVABLE] Under the spec's **own declared convention** (`diff -U 3`, `:1425`):

```text
                 ACTUAL    STATED
HUNKS              21        21      MATCH
DELETIONS         163       163      MATCH
INSERTIONS        261       248      *** FALSE ***
span mismatches     0                all 21 ranges match the table exactly
```

[PROVABLE] **The arithmetic is decisive.** V002 has 1,392 lines and V003 has 1,490.
`1392 − 163 + 261 = 1490`. The declared 248 would require V003 to be 1,477 lines.
The cause is a counting artifact: `grep -c '^+[^+]'` returns exactly 248, because
it silently drops the **13 inserted blank lines** (an inserted empty line appears
as a bare `+`). An independent `--numstat` returns 261.

[YOURS] I grade this precisely: **the carriage *claim* is intact and the *statistic*
is false.** Every hunk is assigned exactly once, the twenty-one ranges reproduce
exactly, deletions reconcile, and "outside those hunks V003 is byte-identical to
V002" survives. What fails is a displayed number that does not reconcile with its
own file. I hold this to the same standard I applied to myself one relay ago, where
I corrected exactly this class of false statistic rather than seal it.

### 4.3 One further finding — the convicted parse survives in the summary

[PROVABLE] §3's table is headed **"Requirement of record"**, and its SP2-07 row at
`:207` reads:

> *"Remove **load-bearing `assert`**, agree under normal and optimized runs, use a
> content-addressed isolated runtime, and pass a terminal seal."*

That is V002's **weakened parse** — the modifier back on `assert` — in the very row
whose weakening was convicted. Its neighbours confirm the table compresses by
design, so compression is not the defect; **inverting the modifier is.** The atom
carries no Boolean force (the executable row at `:502` and the verbatim quotation
at §8.2 are both correct), but a later lane reading §3 for "the requirement of
record" gets the reading the repair exists to forbid.

---

## 5. C5 — BATTERY

### 5.1 `F_PLDEC`

[PROVABLE] Nothing here consumed a reader output, a desired outcome, a measured
value, or any physical quantity. The work is criterion-language auditing, byte
comparison and hash arithmetic. No descriptor was executed. Document line counts and
SHA-256 digests are not physical quantities. `F_PLDEC = CLEAN`.

### 5.2 M-2, four modes

| Mode | Execution | Result |
|---|---|---|
| regex / metacharacter | fixed-string (`grep -F`) for all six scope identifiers and every quoted span | six-for-six zero in V003 |
| line-wrap / whitespace | zero-context and 3-context diffs; region extraction by heading rather than by line number | wrap-independent |
| self-reference / scope | `in scope` hits read **in context** before judging; delta/hunk tables **excluded** when testing operative occurrences | both hits benign (census prose) |
| hyphenation / identifier | eleven spelling variants of the coverage identifiers | all zero |

Every negative is bounded to the fixed V003 byte subject. No corpus-wide emptiness
is inferred.

### 5.3 Fences

`alpha_computed = false`; `proof_authorized = false`; `kappa_record_computed = false`;
no member bound; no fixed point executed; no end test; no numeric evaluation of any
physical quantity; no comparison to any measured constant. No MACHINERY-APPEAL of
my own.

---

## 6. SELF VERB AUDIT

| My verb | Check |
|---|---|
| `NAMED_REPAIRS = 3/3` | Each read personally against its sealed span. SP1-07's residual question — whether the mandatory set is producer-suppliable — was pursued to `:340-342` and closed there, not waved through. |
| `RE_RENDERS = 28/28` | **Coverage stated exactly at §2.4**: mechanical on all 28, semantic in full on 7. I do not claim row-by-row semantic verification of all 28, and I say which twenty-one I did not read. |
| `BOUND_SAMPLE = NOT CLEAN (+2)` | Tested 38 of 38, not the 12 required. Severity **reduced honestly**: receivers exist, so under-notated rather than unbound. |
| `C-B-V010-09` not charged | Read rather than pattern-matched: `certified` qualifies an object whose certificate is a pinned input. Declining a finding is also a finding. |
| `PROTECTED = CONFIRMED` | All three digests **recomputed by me** and equal to the declared pins; regions byte-identical. Not taken on trust. |
| `INSERTIONS false` | Proven by line arithmetic against the actual file length, with the counting artifact diagnosed (13 inserted blank lines) so the repair is one line. |
| `SPEC_V003 = NEEDS_V004` | Scoped **narrow**, and I say plainly that the binding architecture stands. The named repairs and the re-renders are the subject of this review and they passed. |
| **Near-miss 1 — self-caught** | I first computed **57 hunks against 21 declared** and was one step from charging a catastrophic false carriage. The spec declares `-U 3`, not `-U 0`; under its own convention it is 21/21 with zero span mismatches. **A carriage certificate must be tested against the convention it declares, not the one I habitually use.** |
| **Near-miss 2 — self-caught** | My mechanical BOUND test flagged **33 of 38** rows. Reporting that would have been a gross over-claim: the spec expressly permits compact rows whose criterion is prose, provided each atom maps one-to-one onto a result field. Only the banned-adjective/completeness subset is a real finding, and that subset is **two**, not thirty-three. |
| Relitigation | None. I re-adjudicate no grade of record and open no new appeal. |

---

```text
NAMED_REPAIRS = 3/3 CONFIRMED (SP1-07 escape hatch dead under all four M-2 modes --
  six identifiers 6/6 zero, eleven spelling variants zero, the two residual "in
  scope" hits read in context and benign -- with completeness rebound by
  EXACT(cardinality>0) + COMPARE(enum.ids, E.required_ids, empty) + per-ID KERNEL
  replay, and the mandatory set made non-suppliable by the class rule at :340-342
  that every indexed manifest carry its SHA-256 and match P0-verified bytes;
  SP2-06's reality-factor carrier now a content-addressed input (S_reality,E_reality)
  with rho_L/D_reality genuinely CONSUMED by DOMAIN and SPECTRAL, class
  GATED-EXECUTION unchanged; SP2-07's weakened direction reversed correctly -- the
  sealed blocker's "load-bearing" modifies AUDIT, not ASSERT, so hits=empty is the
  blocker's actual reading and not an over-demand)
RE_RENDERS = 28/28 CONFIRMED (0 of 28 carry a residual prose atom or banned
  adjective; every criterion a pure conjunction of opcode results; 0 class changes.
  Read in full: V010-06 -- my prior confirmed missed defect -- now binds
  "target-independent" to KERNEL(p_domain) with a pinned expected conclusion and
  "displayed premises" to per-candidate KERNEL with used_axiom_hashes compared to
  the expected ledger; MR-06's mode doubly pinned by proof conclusion AND expected
  ledger; SP1-04 a DISJUNCTIVE DISCHARGE with a replayed proof on each arm, which
  is NOT the SP1-07 shape but is the structure to watch.
  COVERAGE STATED: mechanical on all 28, semantic in full on 7; the remaining 21
  were not read against their blocker spans individually and I do not claim it.)
BOUND_SAMPLE = NOT CLEAN (+2 rows, from a test of all 38 rather than the 12 asked:
  C-B-V010-14 retains "silently inserted" and C-B-V011-SP1-05 retains "the family
  is exhaustive" -- atom classes the spec's OWN :364-369 says "require the explicit
  named form used by the 28 V003 re-renders". Severity reduced honestly: in both
  rows the receiver already exists in the procedure (M2 with a hit set; ENUM with
  an independent completeness certificate), so these are UNDER-NOTATED, not
  UNBOUND -- no producer input passes them while violating the blocker. One line
  each. C-B-V010-09's "certified" examined and expressly NOT charged: it qualifies
  an object whose certificate is a pinned input consumed by DOMAIN and KERNEL.)
PROTECTED+CARRIAGE = CONFIRMED (+1 false declared statistic: all three protected
  block digests RECOMPUTED BY ME and equal to the declared pins, regions
  byte-identical V002/V003; under the spec's own declared -U 3 convention hunks
  21 = 21 with ZERO span mismatches and deletions 163 = 163, so the carriage CLAIM
  holds -- but FINAL_INSERTIONS = 248 is FALSE, actual 261. Line arithmetic is
  decisive: 1392 - 163 + 261 = 1490, the true V003 length; 248 implies 1477. Cause
  diagnosed: counting with grep '^+[^+]' drops the 13 inserted BLANK lines.
  Additionally the §3 table headed "Requirement of record" still states SP2-07 as
  "Remove load-bearing assert" -- V002's convicted modifier-shift surviving in the
  document's own statement of the requirement, with no Boolean force but in the one
  row where that parse was the defect.)
SPEC_V003 = NEEDS_V004 (NARROW -- the binding architecture STANDS and is the
  subject that passed. Four one-line repairs: correct FINAL_INSERTIONS to 261;
  name the receiving opcode in C-B-V010-14 and C-B-V011-SP1-05 or re-render them;
  restore the SP2-07 requirement-of-record line to the blocker's parse. No repair
  touches an opcode, a class assignment, or a protected section.)
BUILD_READY = no (spec readiness only; RD-22, builder custody and the runtime pin
  remain principal acts and are untouched by this verdict. A build should not start
  from a spec whose declared diff statistic does not reconcile with its own file
  and whose sweep grades two rows BOUND against its own stated rule -- the pre-seal
  pin check is process law now, and it applies to the spec as it applied to me.)
VERB_AUDIT_SELF = CLEAN (+2 self-caught near-miss over-claims recorded at §6: I
  first measured 57 hunks against 21 declared and nearly charged a catastrophic
  false carriage before checking that the spec declares -U 3, not the -U 0 I
  habitually use; and my mechanical BOUND test flagged 33 of 38 rows, which I did
  NOT report, because the spec expressly permits compact prose criteria whose atoms
  map one-to-one onto result fields -- the real finding is two rows, not
  thirty-three.)
```

The repair I asked for at Q-567 was to scope the fix to the class rather than the
rows, and that is what arrived: the banned adjectives are stripped class-wide at
`:355-362`, the manifest rule at `:340-342` closes the producer-suppliable-set
family that made the escape hatch possible, and twenty-eight rows were re-rendered
rather than the three that were convicted. The four residual items are notation and
arithmetic. None of them would let a producer pass a row while violating its
blocker — which is the only question this review exists to answer, and on that
question the answer is that the spec holds.
