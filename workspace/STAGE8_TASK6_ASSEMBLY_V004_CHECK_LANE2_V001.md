# STAGE 8 / TASK 6 / SUBGATE — assembly V004 bounded check — Lane 2 V001

**Artifact:** `STAGE8_TASK6_ASSEMBLY_V004_CHECK_LANE2_V001.md`  
**Lane:** Codex Lane 2  
**Date:** 2026-08-07  
**Scope:** the five Q-572 §5.3 certificate fixes, V003→V004 diff scope, and the disclosed Q-566 digest defect only  
**Status:** BOUNDED CHECK — three fixes fully confirm; Z2's C-V5 reading is refuted and Z5 inherits that defect; the operative assembly is byte-identical

```text
FIXES = 3/5 CONFIRMED (+Z2 C-V5 contradiction; +Z5 inherited carriage/audit defect)
SCOPE = CONFIRMED untouched (+0 operative-region hunks; 17/17 outside)
DIGEST_PINS = CONFIRMED
ASSEMBLY_V004 = NEEDS_V005 (+certificate prose only; operative content stands)
VERB_AUDIT_SELF = CLEAN
```

## 0. Preflight, custody, and fences

The commissioned live head is `Q-576`; the under-review artifact's own `Q-574`
field is historical build metadata, not a competing current-head claim. No
accessible cleanroom or archive register copy disclosed a contradictory later
head. The stated live-append tolerance therefore permits this bounded check.

| Sealed cleanroom subject | Expected SHA-256 | Independently computed | Result |
|---|---|---|---|
| `STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V004.md` | `5e46e8f437ee34d8493dee02195df464e31a20829181542264bc01b23e1f0066` | same | MATCH |
| V003 base `STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V003.md` | `c205602d4db6f30df3999deb4f2a1af425e14e38120cc8904af2480e04911aa4` | same | MATCH |
| Q-572 conviction `STAGE8_TASK6_ASSEMBLY_V003_DELTA_CHECK_LANE2_V001.md` | `85a7a9c32e19d0713845dd1bd7ef50d96c0b27190878e433b55de24559444d56` | same | MATCH |
| V001 fidelity source `STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V001.md` | `a2fdd7c0502083cc9973b766464a30807a3ba3b36b9305011df404671635422c` | same | MATCH |
| C-V5 source `STAGE8_TASK6_EVALUATION_DOR_LANE3_V005.md` | `6b4c96a067bfc7159211909b9fa449cb305bc92fe00005e8ce929cddbccbe773` | same; sidecar verifies | MATCH |
| Q-566 conviction `STAGE8_TASK6_ASSEMBLY_V002_DELTA_CHECK_LANE3_V001.md` | `9456b1a6e279c44289bfd97dc782942a5430dd851a82b345effeb9ada6a7ef59` | same; seal verifies | MATCH |

The cleanroom and archive copies of V004, V003, and the Q-572 conviction are
byte-identical at those pins. Before this artifact was written, neither its
requested filename nor its seal sidecar existed in either location.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
MEMBER_BOUND = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false
MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

This check compares text, hashes, finite diff headers, and word tokens only. No
descriptor, physical object, member, fixed point, end test, or measured constant
is formed or evaluated.

## 1. Y1 — the five fixes

| Fix | Bounded test | Result |
|---|---|---|
| Z1 | `H12`→`H13` for rows V7–V11 | **CONFIRMED** |
| Z2 | seven shared hunks displayed, and the asserted lawfulness tested against C-V5 | **NOT CONFIRMED** — the seven-hunk census is right; the C-V5 reading is false |
| Z3 | both alleged reflows reclassified; quoted word deltas checked against V001/V003 | **CONFIRMED** |
| Z4 | residual seven/eight count fixed under self-reference scope; S06 untouched | **CONFIRMED** |
| Z5 | audit lines consistent with Z2–Z4 | **NOT CONFIRMED** — the Z3/Z4 wording is corrected, but the carriage/CLEAN audit inherits Z2's false C-V5 reading and a false line-count display |

The verdict-line scope is therefore `3/5 CONFIRMED`, not `5/5`: a partially
correct display is not a complete repair when its stated conformance rule is
false.

### 1.1 Z1 — H13, not H12

The V003 hunk-assignment table gives:

```text
H12 = -67                  -> V6 only
H13 = -68,0 +104,140       -> V7,V8,V9,V10,V11
```

V004 changes the prose reference to H13 at §5.3 and repeats the correct spans in
its terminal repair display. Z1 is closed.

### 1.2 Z2 — factual seven-hunk census, unlawful C-V5 reading

Parsing only the `Rows` cell of V003's §5.3 table returns exactly:

| Hunk | Assigned delta rows |
|---|---|
| H05 | V2, V3 |
| H10 | V5, V6 |
| H11 | V5, V6 |
| H13 | V7, V8, V9, V10, V11 |
| H19 | V12, V15, V16 |
| H20 | V12, V16 |
| H25 | V19, V20 |

V004 displays those same seven physical hunks and gives a truthful proximity
explanation for why `diff` merged adjacent logical edits. That verifies the
census and the mechanics. It does **not** verify the claimed lawfulness.

The sealed C-V5 text is exact:

```text
CLAIM_V005 := DELTA_DOMAIN
              = disjoint_union_(R in DELTA_ROWS) EXACT_HUNKS(R).

PRESEAL_CHECK := UNASSIGNED_HUNKS = empty
                 and MULTIPLY_ASSIGNED_HUNKS = empty.
```

It then states that either nonempty exceptional set stops sealing. V004 instead
says the required relation is “total and surjective, not injective,” records
`MULTIPLY_ASSIGNED_HUNKS = 7` for V002→V003, and records
`MULTIPLY_ASSIGNED_HUNKS = 3` for its own V003→V004 certificate. This contradicts
both `disjoint_union` and the explicit second PRESEAL_CHECK conjunct.

The fact that a physical diff hunk can contain several logical edits explains
why a certificate needs a composite assignment row; it does not authorize
assigning one hunk to several rows. A C-V5-conforming repair must assign each
physical hunk exactly once, while listing every authorizing logical subitem
inside that one composite row. Z2 is therefore not closed.

### 1.3 Z3 — the two word deltas

A Markdown-normalized, order-preserving word diff over the sealed V001 and V003
blocks reproduces V004's quotations exactly:

```text
M-2 DELETED (7): by all five researchers and by me
M-2 ADDED   (5): then hyphenation and identifier variants

ANCHOR DELETED (0)
ANCHOR ADDED: restored + the appended V002-deletion commentary
```

For the anchor, the entire V001 word sequence remains in order; the mechanical
word diff finds zero deletions and 43 additions. “Wording-preserving-in-substance
expansions” is accurate; “reflowed with no word changed” was not. Z3 is closed.

### 1.4 Z4 — eight, nine with THOMSON; S06 preserved

V003 has one operative occurrence of the residual sentence:

```text
The seven restored survivors ...
```

V004's closing account now says:

```text
The eight restored survivors — nine counting THOMSON ...
```

The exact old phrase still has two V004 hits, but both are scoped historical
quotations in the Z4 hunk/correction displays; neither asserts the current count.
The lead board says `SURVIVORS = restored (8 items, Q-566 list)`, the verb board
says **Eight**, and the final board enumerates eight Q-566 items. The unrelated
S06 row's “seven-condition Admissible Galerkin class” is byte-identical V003/V004.
Z4 is closed under all four M-2 modes, including self-reference and hyphenation.

### 1.5 Z5 — audit prose is not clean

V004 correctly changes the survivor, restoration, and fidelity audit rows to
eight items and two expansions. Those lines agree with Z3 and Z4.

They do not make the whole audit consistent with Z2. The audit retains
`CARRIAGE = complete_finite_delta`, while §5.3/§5.5 disclose nonempty
multiply-assigned sets that fail C-V5. The lead and terminal
`VERB_AUDIT_SELF = CLEAN` fields consequently overstate the certificate.

The V003→V004 arithmetic display has an independent fixed-subject error:

```text
V004 states: 760 - 26 + 244 = 978
actual lines: 759 - 26 + 244 = 977
```

`diff -U 0` still yields the correctly stated 17 hunks, 244 insertions, and 26
deletions; only both endpoint line counts are one too high. `wc -l`, `awk NR`,
and `sed -n '$='` independently return 759 and 977, and both files end in LF.
The §5.6 claim that line arithmetic was verified is therefore false. Z5 is not
closed.

## 2. Y2 — V003→V004 scope

The declared `diff -U 0` convention independently reproduces every V004 table
header with zero span mismatches:

```text
ZERO_CONTEXT_HUNKS = 17
INSERTIONS = 244
DELETIONS = 26
HUNK_TABLE_SPAN_MISMATCHES = 0
```

| Raw hunks | V003-side span | Destination class | Operative? |
|---|---|---|---|
| H01–H08 | lines 1–42 | title, lead metadata, preflight, digest disclosure | no |
| H09–H10 | lines 583 and 587 | §4.5 self-verb/certificate audit prose | no |
| H11–H17 | lines 660–759 | §5 carriage certificate and terminal account | no |

V003's operative block begins at `## 1` (line 246) and ends before `### 4.5`
(line 568). Its extracted bytes are identical to V004's corresponding block:

```text
OPERATIVE_BLOCK_SHA256 = a0324e484187cfc5677a4f86cb07de660fe2f696dda3a46a0e3a1484b86be60c
OPERATIVE_BLOCK_DIFF_LINES = 0
OPERATIVE_REGION_HUNKS = 0
```

That byte block includes all 18 slot rows and grades, the three appeal
dispositions, the Q-557 release/ruling text, rows 2/6/7 at their operative pins,
both physics-demand sections, the complete freeze section, and §§4.1–4.4. The
slot table still contains 18/18 TYPE-U rows. The scope claim is confirmed even
though the certificate verdict is not.

## 3. Y3 — disclosed V003 digest defect

The sealed Q-566 conviction computes to:

```text
9456b1a6e279c44289bfd97dc782942a5430dd851a82b345effeb9ada6a7ef59
```

V004's operative preflight pin uses that true digest. Its disclosure accurately
quotes V003's false row:

```text
V003 stated: 9456b1a6e279c44289bfd97dc782942a5428dd851a82b345effeb9ada6a7ef59
true digest: 9456b1a6e279c44289bfd97dc782942a5430dd851a82b345effeb9ada6a7ef59
                                              "28" -> "30"
```

Fixed-string counts find the true full digest twice in V004, the false digest
once inside that disclosure, and the false digest once in sealed V003 at its
preflight row. This is the Q-575 disposition requested: corrected successor pin,
accurate disclosure, no edit to the sealed predecessor. `DIGEST_PINS` confirms.

## 4. Y4 — battery and scoped verdict

### 4.1 F_PLDEC and anti-tuning

`F_PLDEC = CLEAN`. The work consists solely of finite text/hash/diff/token
comparisons. No gated physical row is executed, no member is selected, and no
favorable output is used to choose a certificate classification. The operative
assembly bytes remain unchanged.

### 4.2 M-2 — all four false-negative modes

| Mode | Check | Result |
|---|---|---|
| regex/metacharacter | fixed strings for `H12`, `H13`, both digest strings, `seven restored survivors`, and the C-V5 conjuncts | CLEAN; the C-V5 contradiction is exposed |
| line wrap | whitespace/Markdown-normalized word sequences for both Z3 blocks | exact −7/+5 and anchor-zero-deletion results reproduced |
| self-reference/scope | old seven-count hits separated into one V003 assertion and two V004 historical quotations | no false active-count hit |
| hyphen/identifier | `seven-condition` separated from survivor count; `MULTIPLY_ASSIGNED_HUNKS` searched literally | S06 untouched; both nonempty C-V5 failures visible |

### 4.3 Pre-seal pin check and self verb audit

| Claim in this check | Replayed result |
|---|---|
| source pins and sidecars | all match |
| raw V003→V004 diff | 17/244/26; 17/17 headers match V004's table |
| Z1 | H13 carries V7–V11; H12 carries V6 |
| Z2 | seven-hunk census confirmed; lawfulness refuted by sealed C-V5 |
| Z3 | word deltas independently reproduced |
| Z4 | active count corrected; two old-phrase hits are historical; S06 byte-equal |
| Z5 | audit not clean because C-V5 and line arithmetic fail |
| scope | operative block hash equal; zero operative hunks |
| digest | true pin and false-string disclosure both exact |

The verbs `CONFIRMED`, `refuted`, `untouched`, and `NEEDS_V005` are confined to
the displayed fixed subjects. `NEEDS_V005` does not relitigate or weaken any
grade, appeal, ruling, row, or freeze clause. The necessary V005 repair is
certificate-only: install a disjoint one-hunk/one-row C-V5 partition, update the
dependent carriage/audit verdicts, and correct 760/978 to 759/977.

FIXES = 3/5 CONFIRMED (+Z2 C-V5 contradiction; +Z5 inherited carriage/audit defect and false line arithmetic)
SCOPE = CONFIRMED untouched (+0 operative-region hunks; 17/17 outside)
DIGEST_PINS = CONFIRMED
ASSEMBLY_V004 = NEEDS_V005 (+non-disjoint C-V5 mapping and 760/978 count error; operative content stands)
VERB_AUDIT_SELF = CLEAN
