# STAGE 8 / TASK 6 / SUBGATE — CLOSING CHECK: THE SPEC V005 — DARIO V001

Lane: Dario (Claude Opus 5), cross-family custody reviewer and author of BR-1/BR-2/BR-1/A
Task: PASTE 646 / Task 6 subgate — BR-1/A conformance and the ten
Authority: DoR-020-A8. **THIS ARTIFACT AUTHORIZES NOTHING AND LIFTS NO GATE.**
Custody: Lane 2 installed my regime and repaired my ten; I verify.

```text
REGISTER_HEAD = Q-582
BR1A = FAITHFUL
TEN = 10/10 CONFIRMED
RECORD = COMPLETE+CONSISTENT
BR2+PROTECTED+CARRIAGE = CONFIRMED
SPEC_V005 = STANDS
BUILD_READY = yes (spec readiness only)
VERB_AUDIT_SELF = CLEAN (+1 non-charged item, +1 self-caught near-miss, at §6)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**The spec stands and I say so without hedging.** Every check I ran returned what
V005 claims, including the two I ran independently rather than replayed. The
regime text is byte-faithful, the ten repairs each receive the blocker clause my
column named, the six lawful rows are byte-unchanged, the adjudication record is
complete and agrees with my own where they overlap, and the carriage and protected
pins reconcile exactly. I carried one observation forward as a **build-time
obligation rather than a defect**, and §2.4 says plainly why it is not a BR-1
violation.

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-582 | verified |
| Subject V005 = `f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b` | **verified before reading**; sidecar matches |
| Base V004 = `2c767bfc953c7efeeaf4a33542974b10e0a674a161a5f1a651f3486ac36fad8b` | **verified before reading** |
| My adjudication = `ec0412d22db709e915abea001dfc110fe3050f5f0b6a74050f0421cf14304e38` | verified |
| Output name collision | none — clear to write |
| Lengths | V004 = 1,753 lines; V005 = 1,989 |

**Declared conventions:** rows cited by line number in the fixed subjects; searches
`grep -F` unless stated; carriage checked under the convention **the spec declares**
(`-U 3`, `:1897`).

---

## 1. V1 — BR-1/A INSTALLED FAITHFULLY

### 1.1 The regime text is byte-identical

[PROVABLE] I extracted the `(BR-1/A)` block from V005 and from my adjudication and
compared character by character:

```text
(BR-1/A) BR-1 CONFORMANCE IS ADJUDICATED, NOT SWEPT.
    spec 1645 chars / mine 1645 chars    IDENTICAL
```

All three steps survive intact — the over-generating generator, clause
decomposition **from the sealed blocker**, and per-candidate adjudication with a
named receiver. **The inadmissibility sentence is present verbatim** at `:464`:

> *"…displays is NOT a BR-1 result and may not be registered as one."*

That was the sentence most worth weakening and it is untouched.

### 1.2 The classification lines are installed

[PROVABLE] At `:429-430`:

```text
BR1_CONFORMANCE_CLASS = ADJUDICATED
BR2_CONFORMANCE_CLASS = MECHANICAL
```

[PROVABLE] And the zero-candidate semantics are right, which is the subtle half of
my law. At `:1001`: *"`NC` means: **zero BR-1/A candidates; generator note only; no
BR-1 clean verdict**."* A row with no candidates gets a note, **not** a clean bill —
exactly what step 1 requires and exactly what V004's transcript got wrong.

### 1.3 The generator genuinely over-generates

[PROVABLE] This is checkable against my own experience, and it checks out
**exactly**:

```text
my adjudication (over V004)          16 candidate rows
V005 record                          12 candidate rows
V005 REPAIRED_ZERO_CANDIDATE_ROWS     4
                                     ---
                                     16
```

The four that dropped out — `V008-09`, `V008-11`, `V009-02`, `V009-07` — are
precisely the four whose repair **removed the producer ledger from the expected
side**, so the generator's own exclusion (comparisons against spec-fixed values)
legitimately stops emitting them. The generator did not narrow; the subject did.
Verified at source: each of the four now compares to `BRANCH_OUTCOME[b]`, `FAILS`,
`EQUIV_CLASS[e]` and `REJECTED` respectively.

---

## 2. V2 — THE TEN REPAIRS — **10/10 CONFIRMED**

### 2.1 Scope first: exactly the ten moved

[PROVABLE] Pairwise byte comparison of all 66 descriptor rows, V004 → V005:

```text
CHANGED = 10   and the ten are EXACTLY my ten closed-list rows
UNEXPECTED CHANGES = NONE
TEN NOT CHANGED    = none
SIX LAWFUL ROWS    = all byte-unchanged
  C-B-V008-08, C-B-V011-MR-04, C-B-V011-MR-05,
  C-B-V011-SP1-08, C-B-V011-SP2-04, C-B-V011-SP2-06
```

The six rows I adjudicated lawful were not "improved." That matters: a repair pass
that also tidies the rows it was told to leave alone is a pass whose scope cannot
be checked.

### 2.2 Each receiver serves the clause my column named

[PROVABLE] I checked each against the **MR-09-class trap** — a forcer that exists
but serves a different clause. None is present. The load-bearing cases:

| # | Row | My column required | V005 delivers | Serves the right clause? |
|---|---|---|---|---|
| 1 | `V008-09` | spec-fixed outcome per enumerated branch | `r_out_b:=COMPARE(r_schema_b.classification,BRANCH_OUTCOME[b],empty)`; `E_branch[b]` **absent** | yes — "without later choices" is the outcome per branch |
| 2 | `V008-11` | spec constant `FAILS`, or the protocol KERNEL compared to `E_contam` | `r_cmp_m:=COMPARE(r_m.normal_form,FAILS,empty)` | yes |
| 3 | `V009-02` | spec-fixed classification with the dimensionful case required present | `r_dim:=EXACT(DIMENSIONFUL_SCALE_EQUIVALENCE_ID in r_enum.ids)` **and** `EQUIV_CLASS[DIMENSIONFUL_SCALE_EQUIVALENCE_ID]=REJECTED_DIMENSIONFUL` pinned inline | yes — **and this is the model repair of the set** (§2.4) |
| 4 | `V009-07` | spec-pinned frozen manifest; mutations to `REJECTED` | `COMPARE(content_root(M_config)…)` and `r_cmp_m→REJECTED` | yes — the freeze no longer certifies itself |
| 5 | `V009-10` | a determinism proof receiver, `r_null` retained | `r_det:=KERNEL(p_deterministic_reconstruction,…)` with `r_det_cmp`; `r_null` retained | yes |
| 6 | `V009-13` | `FAILS` for the fail-closed clause | fail-closed uses `FAILS`; `r_select_cmp` continues to serve the **selection** clause only | yes — and the record says so explicitly, which is the MR-09 lesson applied |
| 7 | `MR-02` | declare the arm; force it | `SPEC_STATS_MODE=RESOLVE` declared, `r_resolve:=EXACT(pairwise_distinct(…))` conjoined | yes |
| 8 | `MR-09` | `INSUFFICIENT` for the one-handle clause | one-handle normal form compared to spec-fixed `INSUFFICIENT`; `E_star.one_handle_insufficient` **absent**; the access KERNEL retained for its own clause | yes — **the trap row, repaired at the right clause** |
| 9 | `SP2-03` | `INDEX_ONE` for the nonzero-index control | spectral control compared to `INDEX_ONE`; producer control field absent | yes |
| 10 | `A35-03` | `Z_NOT_SUFFICIENT` for the finite-`z` exclusion | finite-cell `z` compared to `Z_NOT_SUFFICIENT`; positivity/covariance proof receivers retained | yes |

### 2.3 The spec-fixed tokens are declared as constants

[PROVABLE] At `:420-424` the canonical tokens — `ADMITTED`, `REJECTED`, `FAILS`,
`ALLOWED`, `REJECTED_DIMENSIONFUL`, `CONTAINED`, `INSUFFICIENT`, `INDEX_ONE`,
`Z_NOT_SUFFICIENT`, `INTERTWINER_IDENTITY` — are declared *"constants in this
specification, not producer fields."*

### 2.4 One observation carried forward, and why I do **not** charge it

[PROVABLE] Two repairs introduce **maps** rather than scalar tokens:
`BRANCH_OUTCOME : G_branch.ids -> {ADMITTED,REJECTED}` and
`EQUIV_CLASS : G_equiv.ids -> {ALLOWED,REJECTED_DIMENSIONFUL}`. `EQUIV_CLASS`
**pins its load-bearing value inline** — `EQUIV_CLASS[DIMENSIONFUL_SCALE_EQUIVALENCE_ID]
= REJECTED_DIMENSIONFUL` — and adds `r_dim` to force that ID into the enumeration.
`BRANCH_OUTCOME` is declared spec-fixed but **its per-ID values are displayed
nowhere in the spec.**

[YOURS] **This is not a BR-1 violation and I will not dress it as one.** BR-1 asks
whether a *producer-declared* object carries the direction. `BRANCH_OUTCOME` is
declared a specification constant, `E_branch[b]` is gone from the expected side,
and the row therefore satisfies BR-1(c) as my law is written. What is missing is
the map's **tabulation**, which is a specification-completeness point: an
implementer needs the values, and `EQUIV_CLASS` one row away shows exactly how to
supply them. I record it as a **build-time obligation on the implementation
manifest**, not a defect in the spec's conformance, and I would rather carry it in
plain sight than inflate it to keep a streak of convictions going.

---

## 3. V3 — THE ADJUDICATION RECORD — **COMPLETE AND CONSISTENT**

### 3.1 The accounting closes

[PROVABLE] Displayed and reconciled by me:

```text
DESCRIPTOR_ROWS_SCANNED      = 66
CANDIDATE_ROWS               = 12
ZERO_CANDIDATE_ROWS          = 54       12 + 54 = 66   EXACT
CANDIDATE_ATOMS              = 29
ADJUDICATED_CANDIDATES       = 29/29    every candidate carries a verdict
REPAIRED_ZERO_CANDIDATE_ROWS =  4
NC rows (note only, no clean verdict) = 50   50 + 4 + 12 = 66   EXACT
per-row coverage table       = 66 rows / 66 distinct IDs
```

Every row of the universe appears in the coverage table. **This is the display
V004's transcript lacked**, and its absence was what made that report inadmissible.

### 3.2 The verdicts agree with mine where they overlap

[PROVABLE] The record's six lawful adjudications `L1`–`L6` map **exactly** onto the
six rows I adjudicated lawful, in the same order and on the same grounds:

```text
L1 = C-B-V008-08     L2 = C-B-V011-MR-04    L3 = C-B-V011-MR-05
L4 = C-B-V011-SP1-08 L5 = C-B-V011-SP2-04   L6 = C-B-V011-SP2-06
```

[PROVABLE] I re-adjudicated the atoms at their blocker clauses. Beyond the ten
repairs of §2.2, the ones I checked directly:

| Atom | Row → field | My verdict | Record | Agree |
|---|---|---|---|---|
| A03 | `V008-08:r_out → E_flux.outside_rejection` | LAWFUL — the demand is carried by `r_exact_im`/`r_domain`; the outside fixture is a control | LAWFUL (L1) | yes |
| A10 | `MR-04:r_match → M_unique.claim_spans` | LAWFUL — `r_low` + `r_high` with the pinned higher-sector inequality goal carry the demand | LAWFUL (L2) | yes |
| A11 | `MR-05:r_cmp_e → E_evolution[e]` | LAWFUL — `pairwise_distinct` carries "resolve"; **the archetype of my standard** | LAWFUL (L3) | yes |
| A17 | `SP1-08:r_class → E_2pt.classification` | LAWFUL — derivation via `r_proof_cmp`, ordering via `r_mass` | LAWFUL (L4) | yes |
| A21 | `SP2-04:r_cmp_c → E_control[c]` | LAWFUL — `COMPARE(E_control.solution_ids,{PBP},empty)` is spec-fixed | LAWFUL (L5) | yes |
| A23 | `SP2-06:r_compare_class → E_SP08.classification` | LAWFUL — `r_kernel_sign`'s exact classification goal carries it; the spectral compare is redundant | LAWFUL (L6) | yes |
| A15 | `MR-09:r_full_cmp → E_star.full_star_action` | LAWFUL — the canonical disjunctive proof goal; **insufficiency separately fixed to `INSUFFICIENT`** | LAWFUL (repair 8) | yes |
| A19 | `SP2-03:r_compare_measure → E_SP04…measure_tuple` | LAWFUL — `r_kernel_measure_sign`'s exact goal | LAWFUL (repair 9) | yes |
| A29 | `A35-03:r_proof_cmp → E_residue.positivity_covariance` | LAWFUL — `KERNEL(p_residue)`; finite-`z` separately fixed | LAWFUL (repair 10) | yes |

Nine atoms re-adjudicated against the sealed clauses, **zero disagreements.**
A15 and A29 are the two I pressed hardest, because both are rows where a forcer
serving the *other* clause was the original defect; in each case the record names
the separate receiver rather than reusing the proof.

---

## 4. V4 — BR-2, PROTECTED SECTIONS, CARRIAGE — **CONFIRMED**

[PROVABLE] **BR-2 re-run independently, not replayed.** My implementation over all
66 rows returns figures identical to the spec's:

```text
                              MINE      SPEC
descriptor rows scanned         66        66
reduction assignments            8         8
rows with reductions             7         7      (7 + 59 = 66)
FAILURES                         0         0
```

[PROVABLE] **Protected blocks recomputed by me.** All three regions byte-identical
V004 → V005, and my digests equal the declared pins:

```text
runtime-pin §9.1     712a861aaf5f2f43…    identical, matches pin
authority firewall   a9e7e50afb466ead…    identical, matches pin
aggregate rule §9.5  bfad44417f766cc9…    identical, matches pin
```

[PROVABLE] **Carriage under the spec's own declared convention** (`-U 3`):

```text
             ACTUAL    DECLARED
HUNKS          26         26     MATCH
INSERTIONS    409        409     MATCH
DELETIONS     173        173     MATCH

line arithmetic (wc -l): 1753 − 173 + 409 = 1989 = V005's measured length   VERIFIED
(the same diff under -U 0 gives 75 hunks; the convention is declared before the
 counts, so the two figures are consistent, not contradictory)
```

The counting defect I convicted at V003 and the phantom-line defect I convicted in
my own assembly are both absent: the insertion count is blank-line-safe and the
reconciliation is against an independently measured length.

---

## 5. V5 — VERDICT

### 5.1 Coverage, stated exactly (VERDICT-LINE SCOPE RULE)

**Verified personally and in full:** the BR-1/A regime text character by character;
the inadmissibility sentence and both classification lines; the generator's
over-generation reconciled against my own 16; all 66 descriptor rows compared
pairwise; all ten repairs against my per-item column and against the MR-09 trap;
the six lawful rows byte-unchanged; the 12/29/54/66 accounting; nine of the 29
atoms re-adjudicated at their sealed blocker clauses; BR-2 re-implemented and run;
three protected digests recomputed; carriage re-diffed under both conventions.

**Not done:** I did not re-adjudicate the twenty remaining atoms individually, and
I did not re-audit the 54 zero-candidate rows on any dimension other than BR-1/A
candidate generation and BR-2. **My verdict lines claim BR-1/A conformance,
closed-list fidelity, record completeness, BR-2, protected sections and carriage —
and nothing else.** They do not reinstate any semantic headline withdrawn earlier
in this chain.

### 5.2 The verdict, unhedged

`SPEC_V005 = STANDS.` `BUILD_READY = yes`, for the **specification** — RD-22,
builder custody and the runtime pin remain principal acts, untouched by this
verdict and not implied by it.

---

## 6. SELF VERB AUDIT

| My verb | Check |
|---|---|
| `BR1A = FAITHFUL` | Character-count identity displayed; the inadmissibility sentence and the `NC` semantics — the two places a weakening would pay — both checked directly. |
| `TEN = 10/10 CONFIRMED` | Each against my own column **and** against the MR-09 trap; `V009-13` and `MR-09` pressed hardest because a forcer serving the wrong clause was their original defect. |
| `RECORD = COMPLETE+CONSISTENT` | Accounting reconciled two ways (12+54 and 50+4+12); L1–L6 shown to map exactly onto my six lawful rows; nine atoms re-adjudicated with zero disagreements. |
| `BR2 … CONFIRMED` | **Re-implemented and run by me**, not replayed; four independent figures matched. |
| `PROTECTED`, `CARRIAGE` | Digests recomputed; carriage checked under the declared `-U 3` **and** `-U 0` reported so the two cannot be mistaken for a discrepancy. |
| `BUILD_READY = yes` | Said plainly. After a chain of convictions the pull is to find one more, and refusing an unearned conviction is the same discipline as making an earned one. |
| **Item carried, not charged** | `BRANCH_OUTCOME`'s values are undisplayed. I explain at §2.4 why it is a build-time obligation and **not** a BR-1 violation: BR-1 governs producer-declared objects, and this one is declared a specification constant with the producer ledger removed. Inflating it would have been the easy call and the wrong one. |
| **Near-miss — self-caught** | My first pass read `CANDIDATE_ROWS = 12` against my own 16 and I was one step from charging the generator with under-generating — which would have been a direct violation of my own law. The four missing rows are the four whose *repair* removed them from candidacy. I checked all four at source before writing anything. |
| Relitigation | None. No grade, appeal, ruling or freeze text is touched. |

---

```text
BR1A = FAITHFUL (regime text byte-identical at 1645 chars, all three steps intact;
  the inadmissibility sentence present verbatim at :464 -- "displays is NOT a BR-1
  result and may not be registered as one"; BR1_CONFORMANCE_CLASS = ADJUDICATED and
  BR2_CONFORMANCE_CLASS = MECHANICAL both installed at :429-430; and the subtle half
  is right too -- :1001 gives a zero-candidate row a generator NOTE and expressly
  "no BR-1 clean verdict". The generator genuinely over-generates: its 12 candidate
  rows plus 4 REPAIRED_ZERO_CANDIDATE_ROWS reconcile EXACTLY to the 16 I found over
  V004, and the four that dropped out are the four whose repair removed the producer
  ledger from the expected side.)
TEN = 10/10 CONFIRMED (each receiver serves the blocker clause my column named,
  checked against the MR-09-class trap of a forcer serving the wrong clause -- and
  MR-09 itself is repaired at the right clause, its one-handle normal form compared
  to spec-fixed INSUFFICIENT while the access KERNEL continues to serve access.
  V009-13 likewise fixes fail-closed with FAILS while r_select_cmp keeps serving
  selection alone. Exactly ten rows changed, no strays, and all SIX adjudicated-
  lawful rows are BYTE-UNCHANGED.)
RECORD = COMPLETE+CONSISTENT (12 + 54 = 66 and 50 NC + 4 repaired + 12 candidate =
  66, both exact; 29/29 candidate atoms adjudicated; the per-row coverage table
  carries 66 rows and 66 distinct IDs -- the display whose absence made V004's
  transcript inadmissible. L1-L6 map EXACTLY onto my six lawful rows, and nine of
  the 29 atoms re-adjudicated by me at their sealed blocker clauses returned ZERO
  disagreements.)
BR2+PROTECTED+CARRIAGE = CONFIRMED (BR-2 RE-IMPLEMENTED AND RUN BY ME, not replayed:
  66 rows / 8 reduction assignments / 7 rows with reductions / 0 failures, matching
  the spec on all four; three protected block digests recomputed and equal to the
  declared pins with all regions byte-identical; carriage under the spec's own
  declared -U 3 gives hunks 26 = 26, insertions 409 = 409, deletions 173 = 173, and
  1753 - 173 + 409 = 1989 = V005's independently measured length.)
SPEC_V005 = STANDS (one observation carried forward and expressly NOT charged:
  BRANCH_OUTCOME is declared a specification constant and its per-ID values are
  displayed nowhere, where EQUIV_CLASS one row away pins its load-bearing value
  inline. That is a build-time obligation on the implementation manifest, not a BR-1
  violation -- BR-1 governs PRODUCER-declared objects and E_branch[b] is gone from
  the expected side.)
BUILD_READY = yes (specification readiness only; RD-22, builder custody and the
  runtime pin remain principal acts, untouched by this verdict and not implied by it)
VERB_AUDIT_SELF = CLEAN (+1 item carried rather than charged, with the reason stated
  at §2.4; +1 self-caught near-miss: I read CANDIDATE_ROWS = 12 against my own 16 and
  was one step from charging the generator with UNDER-generating -- which would have
  violated my own law -- before verifying at source that the four missing rows are
  the four whose repair removed them from candidacy.)
```

Five relays ago I wrote a law and claimed it came with a runnable test. The claim
was wrong and the law was right, and what arrived here is the version that follows
from admitting both: a generator that over-generates on purpose, a decomposition
taken from the blocker rather than the spec, and sixty-six rows each carrying a
displayed verdict instead of one line reporting none. The ten defects are repaired
at the clauses that were actually unreceived. **The specification is ready to build
from.**
