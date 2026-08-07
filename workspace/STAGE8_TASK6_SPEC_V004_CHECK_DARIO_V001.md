# STAGE 8 / TASK 6 / SUBGATE — BOUNDED LIST-CHECK: THE SPEC V004 — DARIO V001

Lane: Dario (Claude Opus 5), cross-family custody reviewer
Task: PASTE 641 / Task 6 subgate — BR conformance and the closed list
Authority: DoR-020-A8. **THIS ARTIFACT AUTHORIZES NOTHING AND LIFTS NO GATE.**
Custody: Lane 2 installed my laws and repaired my closed list; I verify. Bounded —
a LIST check, not an open sweep.

```text
REGISTER_HEAD = Q-576
BR_LAWS = FAITHFUL
BR_SWEEPS_RERUN = BR-2 0/0 confirmed / BR-1 NOT confirmed (+5 failures, all carried rows)
CLOSED_LIST = 11/11 CONFIRMED
OUT_OF_LIST_CHANGES = none
PROTECTED+CARRIAGE = CONFIRMED
SPEC_V004 = NEEDS_V005 (narrow; the law and the closed list are exemplary)
BUILD_READY = no (spec readiness only)
VERB_AUDIT_SELF = CLEAN (+3 self-caught over-claims, recorded at §6)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**The closed list is the best repair work I have checked in this program, and the
BR-1 zero-failure claim is false.** Both are true, and neither softens the other.
Every one of the eleven repairs does what my repair column said, several do it
better, and no row outside the list moved. But BR-1 is now *law over all 66 rows*,
and my own re-run finds **five carried rows that violate it** — including two that
are the same defect classes my closed list repaired in named instances. **V004 did
not introduce them; V004 declared them clean.**

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-576 | verified |
| Subject V004 = `2c767bfc953c7efeeaf4a33542974b10e0a674a161a5f1a651f3486ac36fad8b` | **verified before reading**; sidecar matches |
| Base V003 = `f910815c84fd29d3dc6ca55f43ebe5d4c7015f457ddcde7bd7a69afdf81658dc` | **verified before reading** |
| My closed list = `1f588534257ef274db43f3015ee3c587c76c114467a77acc38c62f354d248a5a` | verified |
| Output name collision | none — clear to write |
| Line counts | V003 = 1,490; V004 = 1,754 |

Archive-side only. **Declared conventions:** row citations are line numbers in the
fixed byte subjects; searches are `grep -F` fixed-string unless stated; carriage is
checked under the convention **the spec itself declares** (`-U 3`, `:1652`), not the
`-U 0` I habitually use.

---

## 1. D1 — THE LAW INSTALLATION

### 1.1 The texts are byte-faithful — **no weakening**

[PROVABLE] I extracted both law blocks from V004 and from my own correction and
compared them character by character:

```text
(BR-1) NO PRODUCER-DECLARED OBJECT MAY CARRY A CRITERION'S DIRECTION
       spec 742 chars / mine 742 chars   IDENTICAL
(BR-2) A REDUCTION OPCODE'S .success IS NOT A TRUTH VALUE
       spec 513 chars / mine 513 chars   IDENTICAL
```

Both scope clauses survive intact — BR-1's *"carries a criterion's direction"* and
its closing sentence that a computed-to-producer `COMPARE` *"is a SELF-CONSISTENCY
check and carries NO directional force by itself"*; BR-2's *"is not a truth value"*
and its permission clause. The rationale of record — *hash-pinning prevents
substitution, not fabrication* — is carried verbatim.

### 1.2 The one new construct, examined — **not a weakening**

[PROVABLE] Lane 2 added `ASSERTION_FREE_FORMATION(r)`, which my text did not
contain. It is the obvious place a weakening would hide, so I checked it directly.

It is **not** self-certifying. The BR-2 procedure's clause (iii) accepts a row only
if *"the row contains `ASSERTION_FREE_FORMATION(r)` **and** no value/result field of
`r` reaches a criterion atom."* The marker alone exempts nothing; the second
conjunct is objective and mechanically checkable. And the marker is used in
**exactly one descriptor row** — `C-B-V010-01`'s `r_response` — which is precisely
the case I myself identified as assertion-free when I found MR-07. It is spec-side
descriptor metadata, not a producer input, so it raises no BR-1 question.

### 1.3 The conformance tests are genuinely mechanical

[PROVABLE] Both procedures are named, closed, and runnable from the spec alone
(`:427-447`). I implemented both from the printed text without consulting Lane 2's
results, which is the property that matters: a reviewer can reproduce them.

### 1.4 **BR-2 re-run — 0 failures, confirming the claim**

[PROVABLE] My independent implementation over all 66 parsed descriptor rows:

```text
BR-2 (Dario re-run)
  descriptor rows parsed        = 66
  reduction assignments found   = SYMBOLIC/SPECTRAL across 7 rows
  bare .success with no receiver = 0
  FAILURES = 0                    <- matches the spec's claim
```

### 1.5 **BR-1 re-run — 5 failures, refuting the claim**

[PROVABLE] My BR-1 implementation first produced **20 candidate flags**. I did not
report twenty: most were artifacts of a crude matcher that could not see forcers
reached through a chain. After per-row reading, **fifteen are properly forced** and
**five are not**. Every one of the five is a **carried** row — unchanged from V003,
never touched by the closed list.

| Row | The atom whose truth depends on producer content | Forcer present? |
|---|---|---|
| `C-B-V008-09` | `r_out_b := COMPARE(r_schema_b.normalized, E_branch[b], empty)` | **none** — `SCHEMA(S_branch,b)` validates the enumerated item, not `E_branch`'s values; no KERNEL; no spec-fixed constant |
| `C-B-V008-11` | `r_cmp_m := COMPARE(r_m.normal_form, E_contam[m], empty)` | **none for `E_contam`** — the row *has* `r_protocol := KERNEL(p_holdout,…)`, but its conclusion is never compared to `E_contam` |
| `C-B-V009-02` | `r_cmp_e := COMPARE(r_units_e.classification, E_equiv[e], empty)` | **none** — no KERNEL anywhere in the row; the *"dimensionful-scale rejection"* exists only as prose in the inputs column |
| `C-B-V009-07` | `r_cmp_m := COMPARE(r_m.normal_form, E_config_mut[m], empty)` | **none** — the mutation-rejection direction is producer-declared |
| `C-B-V009-10` | `r_cmp_u`/`r_cmp_p := COMPARE(r_*.normal_form, E_reconstruct[…], empty)` | **partial only** — `r_null := EXACT(reconstruct(T_top)=0)` is genuinely spec-fixed, but the per-basis and per-parity outcomes are producer-declared |

[PROVABLE] **No global rule rescues them.** A fixed-string sweep for a rule forcing
expected-ledger *content* returns hits only inside BR-1's own text and its
procedure. There is no other constraint on `E_*` values anywhere in the file.

[PROVABLE] **`C-B-V009-02` is the cleanest display.** Its entire procedure is
`ENUM`, an ID-set `COMPARE`, and per-item `UNITS(e)` compared to `E_equiv[e]`. A
producer that declares `E_equiv[e] = ALLOWED` for the dimensionful-scale
equivalence passes every conjunct — and rejecting that equivalence is what the
blocker asks for. The rejection is named in the inputs column and received by
nothing.

[YOURS] **Why the sweep missed them.** The transcript at `:898-930` declares
exactly the right convention — *"a producer expectation used only for
self-consistency is not credited as a directional forcer"* — and then lists only
`repaired_directional_slices` (the six closed-list rows) before emitting
`failures = []` and `outside_closed_list_findings = []`. **There is no per-row
accounting for the other sixty rows.** The procedure as written scans all 66; the
transcript evidences only 6. A sweep that reports its conclusion without its
coverage is the same shape as a carriage certificate that reports a count without
its partition, and it fails the same way.

[YOURS] **This finding is against my own prior work as much as Lane 2's.**
`C-B-V009-07` is the post-hoc-rejection class I repaired at `C-B-V010-01`;
`C-B-V008-11` is the contamination-direction class I repaired at `C-B-V010-13`. My
closed list named instances; BR-1 governs the class. I wrote the law that catches
what my own list missed, and the right conclusion is not that the list was wrong —
it was closed by construction — but that **the law must actually be run over the
carried rows, which is the one thing the closed list could never do.**

---

## 2. D2 — THE CLOSED LIST — **11/11 CONFIRMED**

I verified **all eleven personally against my own repair column.** Deviation from
the column is a finding even when plausible; there were none.

| # | Row / subject | My column required | V004 delivers | Verdict |
|---|---|---|---|---|
| 1 | `C-B-V009-04` | spec-fixed disjointness **and** exactly-one receivers; conjoin the three `DOMAIN` bits | `r_distinct_x:=EXACT(pairwise_disjoint(D_formal[x],D_principal[x],D_taylor[x]))`; `r_one_x:=EXACT(exactly_one_in_domain(...))`; all three `DOMAIN` `.success` conjoined; **and `E_log` deleted entirely**, `r_ids` now against `boundary_fixtures.ids` | **CONFIRMED +** |
| 2 | `C-B-V011-MR-07` | pair the reduction with `COMPARE` against a spec-fixed constant | `r_cmp_f:=COMPARE(r_f.result,CONTAINED,empty)`; **and** containment now takes `r_tau.conclusion`/`r_zero.conclusion` directly, so the ledger no longer feeds the test | **CONFIRMED +** |
| 3 | `C-B-V011-SP1-05` | `M2` ordering receiver with `hits=empty`; name the `ENUM` receiver | `r_order:=M2(q_selection_before_enum,selection_sources)`; `r_order.hits=empty` conjoined; `r_enum.success` named; both banned adjectives gone | **CONFIRMED** |
| 4 | `C-B-V010-01` | fix the expected classification to spec constant `REJECTED` | `r_cmp_m:=COMPARE(r_m.classification,REJECTED,empty)`; **`E_factor` deleted** | **CONFIRMED** |
| 5 | `C-B-V010-13`(a) | a **relational** independence receiver, or a KERNEL independence proof | `r_indep:=KERNEL(p_independence,proof_axioms)` **with exact goal `G_custodian.principal != M_holdout.producer_principal`** — the KERNEL variant my column offered | **CONFIRMED** |
| 6 | `C-B-V010-13`(b) | fix contamination/drift to spec constant `FAILS` | `r_cmp_m:=COMPARE(r_m.normal_form,FAILS,empty)` | **CONFIRMED** |
| 7 | `C-B-V011-MR-05` | `EXACT(pairwise_distinct(...))` conjoined | `r_distinct:=EXACT(pairwise_distinct({r_e.normal_form : e in r_enum.items}))`, conjoined | **CONFIRMED** |
| 8 | `C-B-V011-SP1-02` | compare Lorentz squares to a spec-fixed intertwiner identity | `r_cmp_g:=COMPARE(r_g.normal_form,INTERTWINER_IDENTITY,empty)` | **CONFIRMED** |
| 9 | `C-B-V010-14` | rewrite the atom as `r_m2.hits = empty` | `r_m2:=M2(q_silent_conversion,preseal_sources)`; criterion names `r_m2.success and r_m2.hits=empty` | **CONFIRMED** |
| 10 | §12.7A statistic | set `FINAL_INSERTIONS` to 261 | `FINAL_INSERTIONS = 261` at `:1600`; **and I re-verified the arithmetic against the real files: 1392 − 163 + 261 = 1490 = V003's actual length** | **CONFIRMED** |
| 11 | §3 `B-V011-SP2-07` | restore the blocker's parse — "load-bearing" on *audit* | `:221` now reads *"Every **load-bearing audit** must be free of Python `assert`…"* | **CONFIRMED** |

[YOURS] Items 1, 2 and 4 exceed the column in the safe direction: they **delete the
producer object** rather than merely forcing it. That is the stronger repair, and I
record it as such rather than as a deviation, because removing the object removes
the class of defect instead of constraining it.

---

## 3. D3 — OUT-OF-LIST CHANGES — **NONE**

[PROVABLE] I extracted all 66 descriptor rows from both files and compared them
pairwise:

```text
V003 descriptor rows = 66 ; V004 = 66
UNCHANGED = 58        CHANGED = 8
changed = C-B-V009-04, C-B-V010-01, C-B-V010-13, C-B-V010-14,
          C-B-V011-MR-05, C-B-V011-MR-07, C-B-V011-SP1-02, C-B-V011-SP1-05
OUT-OF-LIST CHANGES = NONE
CLOSED-LIST ROWS NOT CHANGED = none
```

Exactly the eight closed-list descriptors moved, and every one of them moved. The
58 carried rows are byte-identical. **Scope discipline is exact.**

---

## 4. D4 — PROTECTED SECTIONS AND CARRIAGE — **CONFIRMED**

[PROVABLE] **Protected blocks, recomputed by me, not taken on trust.** All three
regions are byte-identical between V003 and V004, and my independently computed
digests equal the declared pins:

```text
region                lines   V003==V004   my digest == declared pin
runtime-pin §9.1        31        yes                yes   712a861aaf5f2f43…
authority firewall      18        yes                yes   a9e7e50afb466ead…
aggregate rule §9.5     20        yes                yes   bfad44417f766cc9…
```

[PROVABLE] **Carriage under the spec's own declared convention** (`-U 3`, `:1652`):

```text
              ACTUAL      DECLARED
HUNKS           26           26      MATCH
INSERTIONS     350          350      MATCH
DELETIONS       86           86      MATCH

line arithmetic: 1490 − 86 + 350 = 1754 = V004's actual length   VERIFIED
(for reference, the same diff under -U 0 gives 56 hunks; the convention is declared
 before the counts, so the two are consistent rather than contradictory)
```

The insertion count is now blank-line-safe and reconciles with the file's own
length — the defect I convicted in V003 is not repeated.

---

## 5. BATTERY

### 5.1 `F_PLDEC`

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. This is criterion-language auditing, byte comparison and
hash arithmetic; document line counts and digests are not physical quantities. No
descriptor was executed. `F_PLDEC = CLEAN`.

### 5.2 M-2, four modes, conventions declared

| Mode | Execution | Result |
|---|---|---|
| regex / metacharacter | `grep -F` for law texts, spec-fixed constants, `ASSERTION_FREE_FORMATION`, each `E_*`/`M_*` identifier | as displayed |
| line-wrap / whitespace | descriptor rows parsed as **one logical row per stable ID**, matching the spec's own declared convention | wrap-independent |
| self-reference / scope | the transcript block and the repair tables were **excluded** when testing whether a row's own procedure contains a forcer, so a mention in a summary cannot certify a receiver | five failures survive that exclusion |
| hyphenation / identifier | `{PBP}`, `REJECTED`, `FAILS`, `CONTAINED`, `INTERTWINER_IDENTITY` and spaced/underscored variants | `{PBP}` found only by reading — see §6 |

### 5.3 Coverage, stated exactly (VERDICT-LINE SCOPE RULE)

[YOURS] What I verified **personally and in full**: both law texts character by
character; both conformance procedures re-implemented and run by me over all 66
rows; all eleven closed-list items against my own repair column; all 66 descriptor
rows compared pairwise V003↔V004; all three protected blocks recomputed; the
carriage under the declared convention; and each of the twenty BR-1 candidates read
individually before charging five.

What I did **not** do: re-adjudicate the 58 carried rows against their sealed
blockers on any dimension other than BR-1/BR-2 conformance. This was a list check,
and outside BR conformance the carried rows stand on their prior review. **My
verdict lines claim BR conformance, closed-list fidelity, scope and carriage — and
nothing else.** A breadth check was commissioned in parallel and had not returned
when this artifact was sealed; nothing here depends on it.

---

## 6. SELF VERB AUDIT

| My verb | Check |
|---|---|
| `BR_LAWS = FAITHFUL` | Character-count identity displayed for both blocks, and the one added construct examined rather than assumed benign. |
| `BR-2 0/0 confirmed` | My own implementation, run before I read Lane 2's transcript. |
| `BR-1 +5 failures` | Each read individually and displayed with the missing forcer named. **Not** reported as 20. |
| `CLOSED_LIST = 11/11` | All eleven verified by me against my own column; three noted as exceeding it in the safe direction rather than counted as deviations. |
| `OUT_OF_LIST = none` | Pairwise comparison of all 66 rows, both directions checked (nothing extra moved, nothing on the list failed to move). |
| `PROTECTED+CARRIAGE` | Digests recomputed; carriage checked under the spec's declared `-U 3`, and I say what `-U 0` gives so the two cannot be mistaken for a discrepancy. |
| `NEEDS_V005` | Scoped narrow and stated with the praise it deserves: the law and the list are exemplary; the false claim is the zero-failure line, not the repair work. |
| **Near-miss 1 — self-caught** | My BR-2 sweep first flagged `C-B-V011-SP1-04`. **False positive from my own regex**: `r_spectral_p` *is* paired, via `COMPARE({r_spectral_p.result, …}, …)`, and my pattern did not allow the brace. Checked before reporting. |
| **Near-miss 2 — self-caught** | My BR-1 sweep first produced **20 flags**. Reporting them would have repeated my 33-of-38 error exactly one relay after I recorded it. Fifteen were forcers reached through a chain my matcher could not see. |
| **Near-miss 3 — self-caught** | I nearly charged `C-B-V011-SP2-04`. It contains `r_unique := COMPARE(E_control.solution_ids, {PBP}, empty)` — a comparison against the **spec-fixed literal `{PBP}`**, a genuine BR-1(c) forcer absent from my constant list. **Refuted, by reading rather than by matching.** |
| Agent reliance | None. Every finding and every confirmation in this artifact rests on my own reading and my own runs. |
| Relitigation | None. No grade, appeal, ruling or freeze text is touched. |

---

```text
BR_LAWS = FAITHFUL (both texts byte-identical to my statements -- BR-1 742 chars,
  BR-2 513 chars -- with the "carries a criterion's direction" scope and the
  "not a truth value" rule intact, and the rationale of record carried verbatim.
  The one added construct, ASSERTION_FREE_FORMATION, is NOT a weakening: its
  acceptance clause carries a second objective conjunct -- "no value/result field
  of r reaches a criterion atom" -- and it is used in exactly one row, C-B-V010-01's
  r_response, the case I myself identified as assertion-free.)
BR_SWEEPS_RERUN = BR-2 0/0 CONFIRMED; BR-1 NOT CONFIRMED (+5 failures, every one a
  CARRIED row the closed list never touched: C-B-V008-09 (E_branch[b] outcomes
  producer-declared; SCHEMA validates the enumerated item, not the ledger's values);
  C-B-V008-11 (E_contam[m] transitions producer-declared -- the row HAS a KERNEL but
  its conclusion is never compared to E_contam); C-B-V009-02 (E_equiv[e]
  classifications producer-declared, no KERNEL in the row at all, and the
  "dimensionful-scale rejection" exists only as PROSE in the inputs column);
  C-B-V009-07 (E_config_mut[m] rejections producer-declared); C-B-V009-10
  (E_reconstruct outcomes producer-declared, though r_null is genuinely spec-fixed).
  No global rule forces expected-ledger CONTENT -- a fixed-string sweep finds such
  language only inside BR-1 itself. The transcript at :898-930 declares exactly the
  right convention and then lists only the six repaired slices before emitting
  failures = [], with NO per-row accounting for the other sixty. C-B-V011-SP2-04 was
  examined and REFUTED: COMPARE(E_control.solution_ids,{PBP},empty) is a genuine
  spec-fixed BR-1(c) forcer.)
CLOSED_LIST = 11/11 CONFIRMED (all verified personally against my own repair column;
  items 1, 2 and 4 EXCEED it in the safe direction by DELETING the producer object --
  E_log, E_factor -- rather than merely forcing it, and MR-07 now feeds containment
  from the KERNEL conclusions themselves; item 10's arithmetic re-verified against
  the real files at 1392 - 163 + 261 = 1490)
OUT_OF_LIST_CHANGES = none (66 descriptor rows compared pairwise: 58 byte-identical,
  8 changed, and the 8 are exactly the closed-list descriptors -- nothing extra
  moved and nothing on the list failed to move)
PROTECTED+CARRIAGE = CONFIRMED (three protected block digests RECOMPUTED BY ME and
  equal to the declared pins, all regions byte-identical V003/V004; carriage under
  the spec's OWN declared -U 3 convention gives hunks 26 = 26, insertions 350 = 350,
  deletions 86 = 86, and 1490 - 86 + 350 = 1754 = V004's actual length. The blank-line
  insertion defect I convicted in V003 is not repeated.)
SPEC_V004 = NEEDS_V005 (NARROW. The law installation is faithful and the closed list
  is 11/11 with three repairs stronger than asked. What needs a V005 is the BR-1
  zero-failure claim, which is false over the carried rows, and the sweep transcript,
  which must show per-row coverage rather than only the repaired slices. Repair scope:
  bind the direction in the five rows -- spec-fixed constants are available and
  already used elsewhere for exactly these classes -- and re-emit BR1 with its
  coverage displayed. V004 did NOT introduce these defects; it declared them clean.)
BUILD_READY = no (spec readiness only; RD-22, builder custody and the runtime pin
  remain principal acts, untouched by this verdict. A build should not start from a
  spec whose own installed law is violated by five of its rows while its transcript
  reports zero failures.)
VERB_AUDIT_SELF = CLEAN (+3 self-caught over-claims: a BR-2 false positive on
  SP1-04 from a regex that disallowed a brace; a BR-1 candidate list of 20 that I
  reduced to 5 by reading rather than reporting -- the same error I recorded one
  relay ago at 33-of-38; and SP2-04, which I nearly charged before finding its
  spec-fixed {PBP} forcer. All three were caught before this artifact claimed
  anything.)
```

The law works. That is the finding, and it cuts both ways: BR-1 was installed to
make a class visible instead of chasing instances, and the first honest run of it
surfaces five rows nobody had re-examined — two of them the very classes my own
closed list repaired one instance at a time. A closed list is closed by
construction and cannot reach the carried rows; a law can, but only if it is
actually run over them and the run shows its coverage. V005's work is small. The
lesson is not: it is that installing a law and reporting its verdict are two
different acts, and only the second one is evidence.
