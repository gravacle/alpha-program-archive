# STAGE 8 / TASK 6 / STEP 2 — THE BOUNDED CLOSING SWEEP OF DoR V006 — DARIO V001

Lane: Dario (Claude Opus 5), cross-family review lane
Task: PASTE 616 / Task 6, Step 2
Authority to review: DoR-020-A8. **THIS ARTIFACT RULES NOTHING AND LIFTS NO GATE.**
Custody: bounded closing sweep. My two standing items from 614 are the entire scope.

```text
REGISTER_HEAD = Q-551
DOR_V006 = CONFIRMED (both standing items closed; no new item)
RULING_READY_PENDING_SUBGATE = yes
VERB_AUDIT_SELF = CLEAN (+2 method notes, §5)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none of my own
```

`RULING_READY_PENDING_SUBGATE = yes` means: **ready except for the subgate.**
`(M5a-V002)` remains `false_of_record` and `SPEC-SEAL` is false at the graph root,
so no gate above 0 is open. Nothing here opens one.

## 0. Preflight

| Check | Result |
|---|---|
| Register head Q-551 (live-append tolerant) | verified |
| `STAGE8_TASK6_EVALUATION_DOR_LANE3_V006.md` = `30b17b2a0cedd09046a12d5733109cfedc74d181d394a23eecfb00597be2cc0b` | **verified before reading** |
| 872 lines (719 → 872, +153) | verified |
| V005 `6b4c96a0…`; my 614 sweep `970e4f4d…`; V003 `da5b03e1…`; the 612 order `f651b34b…` | verified |
| Output name collision | none — clear to write |

**Scope discipline.** I examined only the two regions and the mechanical
properties of the delta. I did not re-open the four closures, the carriage
witnesses, or the gate map, all of which I confirmed at 614 — except to verify
mechanically that this delta did not touch them (§3.3).

---

## 1. ITEM 1 — THE X1–X9 ADDENDUM — **CLOSED**

### 1.1 Against 612's order

The order, verbatim from `f651b34b…`:

> *"enumerate X1–X9 **and every P-1 consumer** in §0.2, or revert those edits
> line-for-line to V003."*

Both halves are discharged.

[PROVABLE] **X1–X9.** Nine rows, each present exactly once, at §0.3. The
construction is sound in three respects I checked specifically:

```text
BASE_X   := sealed V003, da5b03e151bc1b391ba1c666b3c3500f3f474461d4f1e669184ad09ce905b913
            [matches my independently verified hash]
X_REGION_DOMAIN := nine pairwise-disjoint, ANCHOR-BOUNDED comparisons
ADDENDUM_EXCLUSION := remove §0.3 from SUBJECT_X before extracting every X body
                      region
```

`ADDENDUM_EXCLUSION` is not decorative. Because each X row **quotes** its V003
anchor phrase, an addendum that did not exclude itself would match its own
citations and every probe would pass trivially. I proved the clause is
load-bearing by needing it — see §5, note (a).

[PROVABLE] **Every P-1 consumer.** My literal-phrase probe for `"P-1 consumer"`
returned zero, and had I stopped there I would have charged a false negative. The
content is present, carried verbatim from my own V004:

```text
V006:621  | P-1 | (V1-5) one-sided rider; (V4-2); (V5-2)'s new cure row; (V5-3) rails |
V004:531  | P-1 | (V1-5) one-sided rider; (V4-2); (V5-2)'s new cure row; (V5-3) rails |
```

and V006's F4 row additionally names the P-1 mode-typing destinations
(`V1-5; V5-2; V5-3; V5-5`).

**Residual, observed and not charged:** the order said *"in §0.2"*; X1–X9 landed
in §0.3 and the P-1 consumers sit in the V5-4 dependency table. That is placement,
not content — and §0.3 **must** be its own section precisely because
`ADDENDUM_EXCLUSION` has to remove it from the body projection, which it could not
do if it lived inside §0.2's delta board. The placement is a consequence of
getting the construction right.

### 1.2 Faithfulness — spot-checked against the actual V003→V004 transition

I did not accept the addendum's self-description. I diffed V003→V004 myself (64
raw hunks; X1–X9 describe the substantive clause edits, not raw hunks) and probed
four rows under whitespace normalization:

| Row | Claimed edit | V003 | V004 | V006 body | Verdict |
|---|---|---|---|---|---|
| X3 | **add** "the ladder is unformed at its root, not partway up" | 0 | 1 | 1 | faithful |
| X5 | **add** the before-any-value timing rule | 0 | 1 | 1 | faithful |
| X6 | **add** the alternate-metric-rescue attack note | 0 | 1 | 1 | faithful |
| X8 | **delete** the D2 self-correction paragraph | 1 | 0 | 0 | faithful |

X8's whole-file probe returned 1 in V006; the sole occurrence is at **line 168,
inside §0.3**, i.e. the addendum's own anchor citation. Under
`ADDENDUM_EXCLUSION` the body count is 0 and the deletion is retained exactly as
X8 states. Four of nine checked; each faithful in both direction and content.

### 1.3 Scope discipline of the claim

`(X-EQ)` is scoped as *"a finite equality over these nine named historical regions
only; it is not a whole-file V003→V006 carriage claim, does not enlarge the
V005→V006 delta domain, and asserts nothing about an unnamed region or version
pair."* That is the `(C-V5)` discipline applied to a historical pair rather than
abandoned for one — the addendum discharges the order **without** reintroducing a
universal.

[YOURS] This closes item 1 as I framed it at 614. My finding was not that the
re-scope was wrong but that a lane had substituted its own remedy for an ordered
one **on its own authority**. Q-550 regularized the substitution and the ordered
enumeration has now also been executed, so `(C-V5)` stands *and* the order is
discharged. Both, not either.

---

## 2. ITEM 2 — THE CLAUSE-8 LINE — **CLOSED**

[PROVABLE] The operative row, V006:566:

```text
| set a cross-sector unit silently to one | every required factorization
  displayed in the propagation trace; NO CONVERSION SILENTLY SET TO ONE;
  undeclared conversion is an armed falsifier.
  **Sealed provenance: DoR-020-A2's frozen clause 8.** | clean |
```

All three anchors coexist in the **operative** row — not in an audit table, not in
the addendum:

| Anchor | Status |
|---|---|
| the **prohibition** "no conversion silently set to one" | **restored** |
| the **falsifier** "undeclared conversion is an armed falsifier" | retained |
| the **sealed provenance** "DoR-020-A2's frozen clause 8" | retained |

So V005's gain is kept and V005's loss is repaired in the same row. That is the
correct repair: the falsifier catches a conversion after the fact, the prohibition
bars the act, and a factor of one is the conversion that does not look like one.

**Residual, observed and not charged.** `"cross-sector-unit factorization"` still
reads `"every required factorization"`. At 614 I flagged both losses and graded the
prohibition the material half; I hold to that grading rather than escalate now
that the material half is fixed. The row's own attack column reads *"set a
cross-sector unit silently to one"* and its provenance names clause 8, so the
subject is unambiguous within the row. Recording it so the record shows I saw it
and declined it, not that I missed it.

---

## 3. THE RE-DIFF, RECOMPUTED INDEPENDENTLY

### 3.1 Hunk count and line counts

```text
/usr/bin/diff -U 0 <V005> <V006> | grep -c '^@@'   ->  19     [V006 declares 19]
added   173 net (174 incl. the +++ header)         ->  declares 173
deleted  20 net ( 21 incl. the --- header)         ->  declares  20
```

All three match exactly.

### 3.2 Disjointness and exhaustiveness

```text
G1 = {H01-H10, H12-H19}   = 18   the X1-X9 addendum and its control/audit renderings
G2 = {H11}                =  1   the clause-8 operative-row replacement
                            ----
                            19
```

Checked by hand: `18 + 1 = 19`; the union is exactly `{H01…H19}` with **no gap and
no duplicate**. Therefore

```text
UNASSIGNED_HUNKS_V006        = empty   [verified]
MULTIPLY_ASSIGNED_HUNKS_V006 = empty   [verified]
```

The partition is also *interpretable*: G2 is a single hunk because item 2 is a
single-row repair, and G1 carries the addendum. A one-hunk region for a one-line
repair is the shape the claim should have.

### 3.3 The delta is genuinely confined — protected regions untouched

`OTHER_SUBSTANTIVE_REGIONS = empty` is a claim I could test structurally rather
than take on trust. The hunks' old-side positions in V005 line numbers are:

```text
1, 4-5, 7-9, 45, 49-51, 53, 57, 83, 87, 107, 488, 557, 577, 598, 635, 669,
678, 679, 718
```

Against the regions that must not move:

| Protected region | V005 line | Touched? |
|---|---|---|
| gate map **row 8** (the numeric-alpha stop) | 350 | **no** |
| the six-cell lattice `3 x 2 = 6 … six_of_record` | 167 | **no** |
| `CONTACT = VACUOUS_PROVEN` | 261 | **no** |

Every hunk falls in §0 (1–107: header, preflight, addendum), at 488 (the clause-8
row), or in the audit/board tail (557–718). The gate map, the lattice, the contact
determination and the disposition tables are structurally untouched.

---

## 4. FRESH ATTACK, BOUNDED TO THE TWO REGIONS

[YOURS] **My attack: the order had two halves, and the second is the kind that
gets dropped.** 612 required *"X1–X9 **and every P-1 consumer**."* A lane
executing a nine-row enumeration under time pressure would plausibly satisfy the
salient half and let the conjunct go. My probe for `"P-1 consumer"` returned
**zero**, which is exactly what a dropped conjunct looks like.

**It fails.** The consumers are enumerated at V006:621, carried verbatim from my
own V004's Table D, and the F4 row names the mode-typing destinations
independently. The zero was a literal-phrase artifact: the record enumerates the
consumers **as a table row**, not under the phrase the order used.

I report the failure rather than quietly dropping the attack, because the attack
was correct in shape — a two-part order is where a half goes missing — and because
the way it failed is itself the second method note below.

---

## 5. VERB AUDIT AND METHOD NOTES

### Method notes — two more false-negative modes in my own probing

[YOURS] At 614 I disclosed a **line-wrap** false negative. This relay produced two
more, both caught before they reached a finding:

```text
(a) SELF-REFERENCE / SCOPE. My X8 probe searched the whole file and returned 1
    for a phrase the row says was deleted. The hit was the addendum's own anchor
    citation at line 168. The specified ADDENDUM_EXCLUSION projection returns 0.
    A probe must honour the document's own declared extraction scope.

(b) LITERAL-PHRASE vs CONTENT. My "P-1 consumer" probe returned 0 while the
    content was present as a table row. A zero on a phrase the ORDER used is not
    a zero on the OBLIGATION the order imposed.

PROBE PROTOCOL, now three-guarded: fixed strings (defeats regex metacharacters)
+ whitespace normalization (defeats line wrap) + scope-and-synonym check
(defeats self-reference and phrase-vs-content).                          (M-2)
```

### Verb audit

| My verb | Check |
|---|---|
| `CONFIRMED` | Confirms **my two items are closed** and that the delta is confined. It is not a re-confirmation of the whole document; §0 states the scope discipline, and I re-opened nothing I confirmed at 614 except to test that this delta left it alone. |
| item 1 `CLOSED` | Both halves of 612's order discharged, verified against V003 and V004 by my own diffs and probes — not accepted from the addendum's self-description. |
| item 2 `CLOSED` | Verified in the **operative** row, with all three anchors coexisting. |
| "faithful" (X3/X5/X6/X8) | Four of nine rows spot-checked in both directions. I do **not** claim all nine verified; I checked four and say so. |
| re-diff "verified independently" | I ran the diff, counted 19, checked the partition by hand, and reproduced both line counts. |
| protected regions "untouched" | Established by hunk position against three named line numbers — a structural check, not an inspection of intent. |
| Fresh attack | **Fired and failed**, reported as failed, with the reason it failed recorded as a method note. |
| Residuals not charged | Two: the §0.2/§0.3 placement, and the `cross-sector-unit` qualifier. Both stated with my reason for declining, so the record shows they were seen. |
| `RULING_READY_PENDING_SUBGATE = yes` | My two items were the entire remaining scope and both close. This is **not** a statement that any gate is open: `(M5a-V002)` is `false_of_record` and `SPEC-SEAL` is false at the root. |

---

```text
DOR_V006 = CONFIRMED
  ITEM 1 (X1-X9) = CLOSED. Nine anchor-bounded regions at §0.3 against sealed
    V003 as BASE_X, with ADDENDUM_EXCLUSION preventing self-matching; four rows
    spot-checked faithful in both directions against my own V003->V004 diff; and
    the order's second half — every P-1 consumer — enumerated at V006:621,
    carried verbatim from V004. (X-EQ) is scoped as a finite equality over the
    nine named regions and reintroduces no universal, so C-V5 stands AND the
    ordered enumeration is executed.
  ITEM 2 (clause 8) = CLOSED. The prohibition "no conversion silently set to
    one" is restored in the OPERATIVE row at V006:566, coexisting with the
    falsifier and the sealed provenance.
  RE-DIFF = 19 hunks recomputed independently; G1=18 + G2=1 = 19; union
    {H01..H19} with no gap and no duplicate; 173 added / 20 deleted reproduced
    exactly; and no hunk touches gate-map row 8, the six-cell lattice, or
    CONTACT = VACUOUS_PROVEN.
  NO NEW ITEM. Two residuals observed and expressly not charged: the §0.2/§0.3
    placement, and the surviving "factorization" for "cross-sector-unit
    factorization".
RULING_READY_PENDING_SUBGATE = yes
  (ready EXCEPT for the subgate: (M5a-V002) remains false_of_record and
   SPEC-SEAL is false at the graph root, so no gate above 0 is open)
VERB_AUDIT_SELF = CLEAN (+2 method notes: (a) my X8 probe walked into the
  self-reference trap ADDENDUM_EXCLUSION exists to prevent — which is evidence
  that clause is load-bearing; (b) my "P-1 consumer" probe returned a
  literal-phrase zero against present content. Protocol (M-2) now carries three
  guards: fixed strings, whitespace normalization, and scope-and-synonym.)
```

Both items I raised at 614 are closed, and closed in the stronger of the two
available ways: the ordered enumeration was executed **in addition to** the
finite-equality instrument rather than instead of it, and the clause-8 repair put
the prohibition back in the operative row without disturbing the provenance it had
correctly gained. The delta is confined to the two regions by structural test. My
scope was these two items; on that scope, Step 2 is ready for the ruling whenever
the subgate permits it.
