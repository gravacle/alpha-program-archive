# STAGE 8 / TASK 6 / SUBGATE — BOUNDED DELTA RE-CHECK: ASSEMBLY V003 — LANE 2 V001

Date: 2026-08-07  
Lane: Codex Lane 2  
Subject: `STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V003.md`  
Base: `STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V002.md`  
Verdict: **NEEDS_V004 — the mechanical delta and operative repairs pass; the
carriage/fidelity certificate contains false statements.**

## 0. Preflight, custody, and fences

[PROVABLE] The live register ended at Q-571. The output filename and proposed
seal sidecar were absent in both the cleanroom and archive workspace before this
write. All commissioned subjects matched before content was read:

| Subject | Expected SHA-256 | Computed SHA-256 | Result |
|---|---|---|---|
| assembly V003 | `c205602d4db6f30df3999deb4f2a1af425e14e38120cc8904af2480e04911aa4` | same | MATCH |
| base V002 | `11e4e6e4a37572dad1f86ed91fb6ed692195ec282876456418c4fcdac5021037` | same | MATCH |
| Q-566 conviction | `9456b1a6e279c44289bfd97dc782942a5430dd851a82b345effeb9ada6a7ef59` | same | MATCH |
| V001 restoration source | `a2fdd7c0502083cc9973b766464a30807a3ba3b36b9305011df404671635422c` | same | MATCH |

[PROVABLE] The cleanroom and archive copies of V002 and V003 reproduce the same
respective hashes. This check used the cleanroom copies. The Q-557 decision used
for X3 was separately verified against its adjacent seal before reading:
`DECISION_S03_EXPLICIT_INCOMPLETENESS_2026-08-06.md` =
`f0a535214f946b6813f4896c8bc1b7be7a6e34c16278fc6cc18ed688a0194d67`;
sidecar verification returned `OK`.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
MEMBER_BOUND = false
NUMERIC_EVALUATION = false
MEASURED_CONSTANT_COMPARISON = none
```

No fence blocked a structural check. `MACHINERY-APPEAL = none`.

## 1. X1 — independent V002 to V003 re-diff

### 1.1 Totals and raw-span comparison

[PROVABLE] An independent `/usr/bin/diff -U 0 V002 V003` gives:

```text
ZERO-CONTEXT HUNKS = 38
V003 LINES ADDED   = 445
V002 LINES DELETED = 55
```

The 38 raw headers, H01 through H38, were compared mechanically with the 38
spans in V003 §5.3. Every span matches exactly; every V1–V23 delta row is cited
by at least one raw hunk. Inspection of each hunk against its cited §0.3 row
found no unassigned or uncovered hunk. Therefore there is no content-bearing
uncovered instance to quote and no harmless-editorial uncovered residue to
classify.

### 1.2 The delta is complete, but its certificate prose is not clean

[PROVABLE] Four defects occur *inside assigned hunks*. They do not change the
38/445/55 totals or create an uncovered hunk, but they falsify V003's own
carriage/fidelity audit:

1. **Wrong shared-hunk identifier (H32 content).** Section 5.3 says
   *"Rows V7–V11 share H12"*. The raw diff and its own table show those rows share
   **H13**; H12 belongs only to V6.
2. **False PRESEAL statement (H32 content).** Section 5.3 defines the check as
   *"unassigned hunks empty and multiply-assigned hunks empty"* and says both are
   displayed as counts. The table itself assigns seven hunks to more than one
   delta row: H05, H10, H11, H13, H19, H20, and H25. No multiply-assigned count is
   displayed. Multiple logical-row coverage by one raw hunk is explainable, but
   the asserted empty set is false and must be replaced by an explicit seven-hunk
   shared-assignment ledger or by a non-overlapping assignment rule.
3. **The alleged two reflows change words (H23–H27 content).** Details are in X2.
4. **The caught miscount remains (H38 content).** The closing paragraph says
   *"The seven restored survivors"* even though §4.5 says that “seven” was caught
   and corrected to eight Q-566 items; THOMSON is separately the ninth
   restoration.

[YOURS] X1's finite-delta question therefore passes: all bytes changed from V002
are assigned. The stronger claim that the displayed PRESEAL certificate is true
does not pass.

## 2. X2 — nine restored survivor blocks against V001

[PROVABLE] All nine demanded content blocks are present. Seven preserve the
relevant V001 bytes; two preserve the substance but are neither byte-verbatim nor
reflow-only.

| # | Survivor | V003 presence and V001-fidelity result |
|---|---|---|
| 1 | target-awareness standard plus both target-adjacent references | **BYTE-VERBATIM body**: V001:40-57 = V003:170-187; both references present |
| 2 | ten-component `Q_spec` demand | **BYTE-VERBATIM body**: V001:61-72 = V003:197-208 |
| 3 | C7 nine-member order and anti-selection equation | **BYTE-VERBATIM core**: V001:76-97 = V003:216-237 |
| 4 | S17 in ledger order | **BYTE-VERBATIM row** from V001; positioned between S16 and S18 rather than as V002's footnote |
| 5 | OBS-22 declination | **BYTE-VERBATIM core**: V001:218-225 = V003:423-430; V003 then adds separately tagged commentary |
| 6 | parameter-free qualifier | **BYTE-VERBATIM demanded phrase** `parameter-free, target-value-free object`; V003 expands its explanation without weakening the qualifier |
| 7 | explicit M-2 mechanics | **WORDING CHANGED, substance retained and strengthened**; not reflow-only |
| 8 | surface-anchor inventory and observation | **WORDING CHANGED and expanded, all V001 objects/rails retained**; not reflow-only |
| 9 | THOMSON lead field | **BYTE-VERBATIM lead field** from V001; final-board expansion is consistent with it |

The two strict-fidelity failures are mechanical, not interpretive:

- V001 M-2 begins *"Applied throughout by all five researchers and by me"*;
  V003 deletes that phrase and adds *"then hyphenation and identifier variants"*.
  The four-mode extension is useful and tabled, but it is a wording change.
- V001's anchor says *"The anchor's load-bearing observation:"*; V003 changes it
  to *"The anchor's load-bearing observation, restored:"* and adds a new judgment
  to the same paragraph. The rails change from *"every one of S01–S17"* to
  *"all eighteen slots"* and add further rails. All V001 members remain, but this
  is expansion, not reflow.

[YOURS] The Q-566 lost-content list is fully covered in substance. V003's §4.5
claim *"seven byte-verbatim, two reflowed ... with no word changed"* and its final
`all from V001's bytes` description are false in the two named blocks. Under X2's
strict byte-verbatim-or-reflow-only bar, the result is 7/9, not 9/9.

## 3. X3 — V002 delta rows 2, 6, and 7 at their pins

### 3.1 Row 2 and the four-time board-drift mode

[PROVABLE] Delta-table/self-reference hits were excluded and the operative lead
board and final board were compared as separate blocks:

| Field | Operative lead board | Final board | Consistency |
|---|---|---|---|
| `THOMSON` | `TYPE-U`; S16; `MISSING_SPECIFICATION`; transport `UNDETERMINED` | same four atoms, plus the sealed-unexecuted protocol and re-posed source detail | CONSISTENT |
| `UNUSED_PREDICTION` | `TYPE-U (candidate shape carried, not chosen)` | same status and phrase, plus the withdrawal/eligibility/OBS-22 grounds | CONSISTENT |

Thus row 2 is operative at both boards; the table and audit occurrences do not
substitute for either operative occurrence.

### 3.2 Row 6

[PROVABLE] The S03 row points to §1.1. The displayed release condition preserves
the decision's complete lines 30-35, with Markdown quotation punctuation only.
The displayed scope excerpt preserves the object-side inheritance and unaffected
demand-side sentences from decision lines 25-27. The decision hash and sidecar
both verify.

### 3.3 Row 7

[PROVABLE] S05, S07, and S08 each contain the required object-side inheritance
note and the unaffected-demand-side clause at the row itself. S04 already carried
the object-side inheritance in V002. No note changes a grade.

[YOURS] Rows 2, 6, and 7 are confirmed at their promised pins.

## 4. X4 — protected state did not move

[PROVABLE] The main slot table contains 18 rows and 18 `TYPE-U` status cells.
Against V002, thirteen common row lines are byte-identical; S03, S05, S07, and
S08 preserve their slot/status/anti-tuning fields and change only by the
authorized append-only pin notes; S17 is restored byte-verbatim from V001 and
retains the `TYPE-U` state carried by V002's footnote.

[PROVABLE] Independent block hashes give:

| Protected block | V002 block SHA-256 | V003 block SHA-256 | Result |
|---|---|---|---|
| all three appeal dispositions, Appeal 1 through Appeal 3 | `cee59f09bee3b417f92e54025bd4d1e0e8d494793f50dbd7498fce1e280def3a` | same | BYTE-IDENTICAL |
| `(FR-V002)` corrected freeze display | `6a61a7779c803576753d547c79896c77931cef6b744ed126c4b418921ac2d23d` | same | BYTE-IDENTICAL |
| final-board `FREEZE` statement | `85510347fb5b29b29cf613535796e8b27253df1ae87bc5418a7278a75902a7eb` | same | BYTE-IDENTICAL |

The lead-board two-line freeze statement is also byte-identical. No grade,
appeal disposition, principal ruling, or freeze content moved. The slot table's
authorized changes are the four row-local append-only notes plus S17's return as
a row; only the last changes table structure.

## 5. X5 — battery and verdict

### 5.1 F_PLDEC

[PROVABLE] This check consumed only pinned text, structural hashes, byte diffs,
status fields, and source quotations. It did not consume a reader output,
candidate outcome, local-shadow value, physical response value, measured central
value, fixed point, or end test. `F_PLDEC = PASS`.

### 5.2 M-2, all four false-negative modes

| Mode | Execution and result |
|---|---|
| regex metacharacter | fixed-string probes preceded regex probes for all survivor anchors, board fields, hunk IDs, and final statuses |
| line wrap | whitespace-normalized comparisons joined the V001/V003 survivor blocks; this exposed word changes that raw line-by-line reflow could hide |
| self-reference / scope | delta/assignment/audit tables were excluded when testing the operative and final `UNUSED_PREDICTION` and `THOMSON` boards; both operative pins exist |
| hyphen / space / underscore | joint variants covered `parameter-free`, `target-value-free`, `historically target-aware`, `unused prediction`, and their spaced/underscored forms; context classification separates restored content from its audit mentions |

Bounded zero findings in this artifact apply only to the pinned V002/V003 byte
subjects. No emptiness claim is made.

### 5.3 Self verb audit and minimal V004 repair

| Verb/status | Warrant |
|---|---|
| `FULLY_ACCOUNTED` | raw totals reproduce; 38/38 spans match; V1–V23 all exhibited; zero uncovered hunks |
| `7/9 STRICT-FIDELITY` | seven demanded blocks preserve their V001 bytes/phrase; normalized word diffs convict M-2 and the surface anchor |
| `ROWS_2_6_7 = CONFIRMED` | both operative boards, the sealed decision, and all three row pins checked directly |
| `INVARIANTS = unchanged` | grades counted; appeal and freeze blocks byte-hashed; authorized append-only row changes isolated |
| `NEEDS_V004` | false H12 reference, false multiply-assignment claim, two false reflow assertions, and residual “seven” miscount |

[YOURS] V004 can be bounded to certificate prose: change H12 to H13; display and
explain the seven shared-assignment hunks instead of claiming an empty set;
classify the M-2 and surface-anchor blocks as wording-preserving-in-substance
expansions rather than reflows; change the residual “seven” to eight Q-566
survivors (nine including THOMSON); update both survivor/fidelity audit lines.
The operative assembly, rows 2/6/7, all 18 grades, appeals, rulings, and freeze
text require no change.

DELTA = FULLY_ACCOUNTED (+38/38 spans; 445 insertions; 55 deletions; zero uncovered hunks; certificate prose defects remain)
SURVIVORS = 9/9 PRESENT, 7/9 STRICT-FIDELITY CONFIRMED (+M-2 and surface-anchor wording changes)
ROWS_2_6_7 = CONFIRMED
INVARIANTS = unchanged
ASSEMBLY_V003 = NEEDS_V004 (+repair H12/H13 reference, shared-assignment certificate, two reflow claims, and residual seven/eight count)
VERB_AUDIT_SELF = CLEAN
