# STAGE 8 / TASK 6 / SUBGATE — assembly V005 closing check — Lane 2 V001

**Artifact:** `STAGE8_TASK6_ASSEMBLY_V005_CHECK_LANE2_V001.md`  
**Lane:** Codex Lane 2  
**Date:** 2026-08-07  
**Scope:** the seven C-V5a decompositions, the two line-count reconciliations,
and V004→V005 operative-byte preservation only  
**Status:** BOUNDED CLOSING CHECK — the decomposition, counts, and scope claims
are confirmed; assembly V005 stands

```text
DECOMPOSITION = CONFIRMED (+H20 never_shared; both inserted lines are V16 renumber)
COUNTS = CONFIRMED (+759-26+244=977; +977-49+214=1142)
SCOPE = CONFIRMED untouched
ASSEMBLY_V005 = STANDS
VERB_AUDIT_SELF = CLEAN
```

## 0. Preflight, subjects, and fences

[PART-PROVABLE] The commissioned preflight identifies live register head
`Q-582`. The readable local snapshot does not yet expose that append; under the
stated live-append tolerance it is accepted because no conflicting local record
was found. Live appends recording the parallel outputs do not alter the fixed
subjects checked here.

| Sealed cleanroom subject | Expected SHA-256 | Independently computed | Copy/seal result |
|---|---|---|---|
| assembly V005 `STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V005.md` | `76589e94bb4af318880c61c3d677dc2518add8480100a7afaf675e4dd3a394a8` | same | cleanroom sidecar matches; archive copy and sidecar byte-agree |
| assembly V004 `STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V004.md` | `5e46e8f437ee34d8493dee02195df464e31a20829181542264bc01b23e1f0066` | same | cleanroom sidecar matches; archive copy and sidecar byte-agree |
| Q-577 conviction `STAGE8_TASK6_ASSEMBLY_V004_CHECK_LANE2_V001.md` | `f37e04fd400739d4118432d898a00b503ec8f42fd3e4d1d0a679c831685a3e8c` | same | cleanroom and archive seals match |
| assembly V003 `STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V003.md` | `c205602d4db6f30df3999deb4f2a1af425e14e38120cc8904af2480e04911aa4` | same | sidecar matches |
| assembly V002 `STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V002.md` | `11e4e6e4a37572dad1f86ed91fb6ed692195ec282876456418c4fcdac5021037` | same | sidecar matches |

Before this artifact was written, neither its requested filename nor its seal
sidecar existed in the cleanroom or archive workspace. No input was read before
its required pin was checked.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
MEMBER_BOUND = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
NUMERIC_PHYSICAL_EVALUATION = false
MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

This check reads sealed text, hashes bytes, counts newline-terminated lines, and
compares finite diff spans. It executes no assembly member, evaluator, physical
procedure, fixed point, end test, or comparison to a measured constant.

## 1. U1 — the decomposition

### 1.1 Subject discipline

[PROVABLE] V005's seven-span table in §5.3 decomposes the **V002→V003** hunks
`H05`, `H10`, `H11`, `H13`, `H19`, `H20`, and `H25`; those are the hunk IDs and
line coordinates printed by its declared `/usr/bin/diff -U 0 V002 V003`.
Accordingly, each decomposition was checked against that actual diff. The
task's phrase “actual V003→V004 diff” is also satisfied separately below: that
distinct diff has 17 hunks and its 17/17 spans match V005 §5.5, but it is not the
coordinate subject of the seven decompositions. Mixing the two coordinate
systems would make the check false by construction.

The raw V002→V003 replay returns:

```text
ZERO_CONTEXT_HUNKS = 38
INSERTIONS = 445
DELETIONS = 55
RAW_SPANS_EQUAL_V005_5_3_TABLE = 38/38
```

### 1.2 Seven disjoint span partitions

| Hunk | Raw changed extent | Replayed disjoint partition | Attribution check | Verdict |
|---|---|---|---|---|
| H05 | old 14–15; new 17–22 (`-2/+6`) | new 17–18 → V2; old 14–15 and new 19–22 → V3 | V2 is the restored `THOMSON`/`UNUSED_PREDICTION` pair; V3 is the other lead-board/certificate replacement | EXACT |
| H10 | old 46; new 55–61 (`-1/+7`) | old 46 → V6; new 55–61 → V5 | old §0.2 heading is V6; the seven-line false-certificate finding is V5 | EXACT |
| H11 | new 63–80 (`-0/+18`) | new 63–73 → V5; new 74–80 → V6 | construction-method admission closes V5; the relabeled/incompleteness §0.2 opening is V6 | EXACT |
| H13 | new 104–243 (`-0/+140`) | 104–137 → V7; 138–167 → V8; 168–194 → V9; 195–213 → V10; 214–243 → V11 | the five spans begin at the displayed §0.3, §0.4, §0.5, §0.6, and §0.7 boundaries | EXACT |
| H19 | old 107; new 279–309 (`-1/+31`) | old 107 → V16; new 279–283 → V15; new 284–309 → V12 | old §1.1 heading is displaced/renumbered; the five-line table close is V15; the 26-line release display is V12 | EXACT |
| H20 | new 311–312 (`-0/+2`) | both lines → V16 | line 311 is the renumbered `### 1.2 Scheme covariance…` heading; line 312 is its following blank; neither line belongs to V12 | EXACT / NEVER SHARED |
| H25 | old 289; new 524–526 (`-1/+3`) | old 289 → V20; new 524–526 → V19 | old `### 4.4 M-2` heading is V20; the three surface-anchor lines are V19 | EXACT |

The arithmetic independently re-adds as:

```text
H05  old 2; new 2+4 = 6
H10  old 1; new 7
H11  new 11+7 = 18
H13  new 34+30+27+19+30 = 140
H19  old 1; new 5+26 = 31
H20  new 2 = 2
H25  old 1; new 3
```

The intervals are pairwise disjoint on each hunk side, their unions equal the
raw changed extents, and every interval has one row. No line is omitted or
assigned twice:

```text
DECOMPOSITIONS = 7/7
UNASSIGNED_SPANS = 0
MULTIPLY_ASSIGNED_SPANS = 0
GENUINELY_SHARED_HUNKS = 6
H20_SHARED = false
```

### 1.3 H20 at the bytes

The actual zero-context hunk is exactly:

```diff
@@ -108,0 +311,2 @@
+### 1.2 Scheme covariance, carried (replacing V001's contradiction section)
+
```

The two inserted bytes-lines hash to
`37f37b171baf5962fd2cad03cfbd534bfecdc945a236ae36f06e69a9cacd152c`
including their terminating newlines. V12 ends at new line 309; unchanged blank
line 310 separates it from H20. H20 is therefore V16 alone, and V004's earlier
seven-shared-hunk census is correctly narrowed to six.

## 2. U2 — counts and declared methods

### 2.1 V003→V004

The declared zero-context diff was regenerated from the pinned subjects. Every
raw header matches V005 §5.5 in order:

```text
RAW_HUNKS = 17
RAW_HEADERS_MATCH_TABLE = 17/17
HUNK_HEADER_INSERTIONS = 244
HUNK_HEADER_DELETIONS = 26
```

The endpoint lengths were measured independently, not derived from the same
equation:

| Subject | `wc -l` | `awk NR` | `sed -n '$='` | Last byte |
|---|---:|---:|---:|---|
| V003 | 759 | 759 | 759 | `0a` |
| V004 | 977 | 977 | 977 | `0a` |

Thus:

```text
759 - 26 + 244 = 977
```

All four terms are independently reproduced. Retaining the terminal empty
element of `split("\n")` returns 760/978 because both files terminate in LF;
the phantom element explains the former off-by-one and why it cancelled on both
sides of the old equation.

### 2.2 V004→V005

The V005 declared convention was also rerun from the sealed subjects:

```text
RAW_HUNKS = 20
RAW_HEADERS_MATCH_TABLE = 20/20
HUNK_HEADER_INSERTIONS = 214
HUNK_HEADER_DELETIONS = 49
V004_WC_LINES = 977
V005_WC_LINES = 1142
977 - 49 + 214 = 1142
```

The §5.7 table has exactly twenty hunk rows. Each row cell contains one of
`M1`–`M5` or `W1`–`W4`, every such delta row is exhibited, and no physical hunk
has multiple assignments. The V004→V005 certificate therefore satisfies C-V5a
by construction:

```text
SPANS_ACCOUNTED = 20/20
UNASSIGNED_SPANS = 0
MULTIPLY_ASSIGNED_SPANS = 0
ROWS_WITHOUT_A_SPAN = 0
```

## 3. U3 — operative scope

### 3.1 Raw-hunk exclusion

V004's operative region begins at `## 1` on line 277 and ends immediately before
`### 4.5` on line 599; its closed old-side interval is therefore 277–598. The
V004→V005 zero-context hunk starts are:

```text
1, 4, 7, 18, 30, 40,
620, 703, 708, 724, 733, 803, 805, 847, 856, 857, 860, 879, 883, 956.
```

The first six finish by old line 42 and the remaining fourteen begin at old line
620 or later. No insertion point or replaced interval reaches 277–598:

```text
OPERATIVE_REGION_HUNKS = 0
```

### 3.2 Anchor-bounded byte comparisons

The corresponding anchor-bounded regions were extracted independently from
both files:

| Protected content | V004/V005 result | Shared SHA-256 |
|---|---|---|
| complete operative block, `## 1` through §4.4 | byte-identical, 322 lines | `a265288a5488394c5ae96dee2aef3b3d0939e2a0b8f21997c7e9d43bb1c571cd` |
| eighteen S01–S18 table rows | 18/18 byte-identical; all 18 status cells contain `TYPE-U` | `63d07d1b1a8c0fa684060135d41bcc66d0ea3ea8007b5fb68bc3a50ede4d4ceb` |
| complete `## 3. Q3 — THE FREEZE` section | byte-identical, 54 lines | `334660c80e56adfa719f3c3dae7a60e56e101f1ad0482f92f531e8c27c6b866e` |

This establishes, without reasserting the semantics, that all eighteen grades,
the Q-557 ruling/release display, the three appeal dispositions, rows 2/6/7,
both physics demands, the freeze statement, and §§4.1–4.4 are untouched.

## 4. U4 — battery, pin check, and verdict

### 4.1 `F_PLDEC` and anti-tuning

`F_PLDEC = CLEAN`. The check consumes only fixed source bytes and diff metadata.
No reader value, shadow response, desired result, member, physical quantity, or
measured constant participates in a count, attribution, or verdict. The STANDS
verdict follows from the displayed structural checks, not from a favorable
assembly output.

### 4.2 M-2 — all four false-negative modes

| Mode | Execution | Result |
|---|---|---|
| regex/metacharacter | fixed-string extraction of all hunk headers and `H20`, followed by structural parsing | all three raw/table span sequences match |
| line-wrap/whitespace | zero-context hunk coordinates and anchor-bounded byte blocks, not visual wrapping, determine scope | no wrapped prose creates or hides an operative hunk |
| self-reference/scope | §5 certificate tables are excluded from operative-block and 18-row counts; historical H20 statements do not supply its bytes | H20 verdict rests on V003 lines 311–312 only |
| hyphenation/identifier | `TYPE-U`, `MULTIPLY_ASSIGNED_SPANS`, `newline-terminated`, and their prose variants are searched in their containing sections | 18/18 and both zero exceptional-set counts remain exact |

### 4.3 Pre-seal pin check and self verb audit

| Claim in this check | Replayed result |
|---|---|
| source pins, sidecars, and clean/archive equality | exact; no collision |
| V002→V003 raw diff | 38/445/55; 38/38 table spans match |
| seven C-V5a decompositions | disjoint; sums exact; row meanings agree with their byte spans |
| H20 | two inserted lines are V16 only; never shared |
| V003→V004 counts | 17/244/26 and `759-26+244=977` |
| V004→V005 counts | 20/214/49 and `977-49+214=1142` |
| V004→V005 C-V5a table | 20 physical hunks, one row each, zero exceptional spans |
| operative scope | no hunk in old lines 277–598; operative hash equal |
| grades and freeze | 18/18 TYPE-U rows and complete freeze section byte-identical |

The verbs `CONFIRMED`, `untouched`, and `STANDS` are limited to these fixed
structural subjects. They do not claim a slot filling, freeze, evaluator run,
seal, physical result, or authorization. No MACHINERY-APPEAL was required.

DECOMPOSITION = CONFIRMED (+H20 never_shared; both inserted lines are V16 renumber)
COUNTS = CONFIRMED (+759-26+244=977; +977-49+214=1142)
SCOPE = CONFIRMED untouched
ASSEMBLY_V005 = STANDS
VERB_AUDIT_SELF = CLEAN
