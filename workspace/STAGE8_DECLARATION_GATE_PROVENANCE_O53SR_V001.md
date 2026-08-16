# STAGE 8 — THE DECLARATION GATE: PROVENANCE AUDIT — O53SR — V001

## BUILD LANE — READ-AND-REPORT AT BYTES — [SEALED]

Date: 2026-08-16
Role: BUILD lane of a commissioned pair. Exhaustive byte-level provenance sweep for
the term **"the declaration gate"** across every readable root, to determine whether
a constitutive definition of it exists at bytes. A principal act (road item 20) is
blocked on this return.

**THIS ARTIFACT DECLARES NOTHING, DEFINES NOTHING, AND PROPOSES NOTHING.** It reports
what is and is not written. It does not draft, sketch, or recommend a definition for
the declaration gate; it does not advise whether item 20 should be taken. The
declaration gate is untouched and remains the principal's. GOV-F is untouched.

Fences held: `alpha_computed = false` ; `proof_authorized = false` ;
`kappa_record_computed = false`. Nothing computed; no magnitude approached; no CAS
invoked; no flag flipped; no file edited; no git action. One file written (this
artifact) plus its two seal sidecars. Output path probed before write: ABSENT.

---

## 0. VERDICT IN ONE LINE

**Q1 = ABSENT.** Across 12,935 swept files in three roots, the term "declaration
gate" occurs **46 times in 34 files = 29 distinct occurrences in 20 distinct
artifacts** (mirror pairs collapsed). Of these, **17 are untouched-assertions**, **11
are references/custody-assertions** ("it is the principal's"), **1 is an unrelated
software homonym**, and **0 are definitions** and **0 are constitutions**. No ruling,
spec, plan, register, relay, or instrument anywhere states what the declaration gate
**is**, what it gates, what its criteria are, or what taking it would mean. The term
entered the record on 2026-08-14 already in the untouched/custody form, in a lane
artifact reproducing discipline language from a commission brief that is **not on
disk**, and every one of the 28 subsequent occurrences inherits it. It was never
constituted.

---

## 1. SCOPE, ROOTS, AND SWEEP CONSTRUCTION

### 1.1 Roots read

| root | files in swept corpus |
|---|---|
| `/Users/bgm/MB Work/alpha_supervision` | 993 |
| `/Users/bgm/MB Work/alpha-program-archive` (supervision · workspace · relay_inbox · relay_outbox · cleanroom_output · a32_holdout) | 6,591 |
| `/Users/bgm/Documents/New project/.../alpha_fundamental_record_action_cleanroom_v003` | 5,351 |
| **TOTAL raw files across all three roots** | **23,498** |
| **TOTAL after noise filter** (`.git`, `site-packages`, `dist-info`, `__pycache__`, `*.pyc`, `node_modules`, `.venv`, `.pytest_cache`) | **18,808** | — |
| **TOTAL text candidates** (`.md .txt .json .jsonl .py .sh .csv .yaml .yml`) | **12,952** | — |
| **CORPUS SWEPT** (after commission exclusions) | **12,935** | — |

Relay coverage verified explicitly: `relay_inbox` 442 files, `relay_outbox` 788 files
in the swept corpus. Both returned **zero** hits on the primary pattern.

### 1.2 Exclusion globs (ARRAY) and per-pattern leak counter

```
EXCLUSIONS = [
  "QUESTIONS_SETTLED_REGISTER",
  "QUESTIONSSETTLED_REGISTER",
  "EXECUTION_TRACKER",
  "ROAD_REMAINING",
  "FINISH_B_DECISION_SHEET_2026-08-16",
  "FINISH_B_SEALED_2026-08-16",
  "_DECISION_SHEET_",
  "STAGE8_DECLARATION_GATE_PROVENANCE_O53SR_V001"   # self-exclude
]
```

| pattern | files matched | files removed | **leaks into corpus** |
|---|---|---|---|
| `QUESTIONS_SETTLED_REGISTER` | 2 | 2 | **0** |
| `QUESTIONSSETTLED_REGISTER` | 1 | 1 | **0** |
| `EXECUTION_TRACKER` | 2 | 2 | **0** |
| `ROAD_REMAINING` | 2 | 2 | **0** |
| `FINISH_B_DECISION_SHEET_2026-08-16` | 2 | 2 | **0** |
| `FINISH_B_SEALED_2026-08-16` | 2 | 2 | **0** |
| `_DECISION_SHEET_` | 8 | 8 | **0** |
| self-exclude | 0 | 0 | **0** |
| **TOTAL** | — | **17 distinct files** | **0** |

The 17 removed files, enumerated for audit: `FINISH_B_DECISION_SHEET_2026-08-16.md`,
`EXECUTION_TRACKER.md`, `FINISH_B_SEALED_2026-08-16.md`,
`A32_RATIFICATION_DECISION_SHEET_2026-07-28.md`,
`ACT3_SPEC5_REVISION_DECISION_SHEET_2026-08-15_V001.md`,
`ACT3_SPEC5_REVISION_DECISION_SHEET_2026-08-15_V002.md`,
`QUESTIONS_SETTLED_REGISTER_V001.md`, `ROAD_REMAINING_FLAT_V001.md` — each in both
`alpha_supervision/` and `alpha-program-archive/supervision/` — plus
`QUESTIONSSETTLED_REGISTER_V001.md` in the cleanroom.

**INCIDENT LOG — barred material surfaced and discarded unread:** none opened. All
17 were removed by path-name filter **before** any read. Zero barred bytes entered
this audit. The registrar's own characterization of the declaration gate (in the
`FINISH_B_*` and `*_DECISION_SHEET_*` files) was therefore never seen, and this
audit's ABSENT verdict is independent of it.

### 1.3 The line-wrap correction (a sweep defect found and cured)

The first pass used line-based `grep`. It returned 39 hits / 31 files. Re-running the
same pattern **newline-normalized** (`declaration\s+gate`, whole-file regex) returned
**46 hits / 34 files** — **7 matches were wrapped across a newline** and had been
invisible to the line-based sweep. Three artifacts surfaced only on the normalized
pass: `THE_GRAVITY_CLOSE_SEALED_2026-08-15.md`,
`STAGE8_GRAVITY_CLOSE_RESCORE_T9SR_AUDIT_V001.md`, and additional occurrences inside
`STAGE8_GRAVITY_CLOSE_SCORING_V001.md`, `STAGE8_GRAVITY_CLOSE_RESCORE_T9SR_V001.md`
and `THE_GRAVITY_CLOSE_ASSEMBLY_V001_2026-08-15.md`. **All counts in this artifact are
from the normalized sweep.** A line-based-only sweep of this corpus under-reports by
~15%; recorded here because the commission's ABSENT verdict depends on sweep quality.

### 1.4 Mirror structure (verified by digest, not assumed)

`/Users/bgm/MB Work/alpha_supervision/` and
`/Users/bgm/MB Work/alpha-program-archive/supervision/` are **byte-identical mirrors**
for every hit-bearing file tested (`ACT5_RULE2_AUTHOR_DECISION` `96bd68e5…`,
`THE_GRAVITY_CLOSE_SEALED` `d287f177…`, `THE_HANDOFF_2026-08-14_V002` `3589241e…`,
`THE_GRAVITY_CLOSE_ASSEMBLY_V001` `74ef6085…` — all IDENTICAL).
`alpha-program-archive/workspace/` and `.../cleanroom_v003/` likewise mirror
(`STAGE8_TASK6_ARGV_PREFIX_FIX_LANE2_V001` `5fb65c12…` IDENTICAL). Six hit-bearing
workspace artifacts are **workspace-only** and not mirrored to the cleanroom (the six
gravity-close scoring/rescore/triage artifacts). All counts below report **distinct
occurrences** with mirror pairs collapsed.

---

## 2. SWEEP CUTOFFS — PATTERNS AND HIT COUNTS

All patterns case-insensitive, whole-file (newline-normalized), over the 12,935-file
corpus. Counts are **raw matches / files**, before mirror collapse.

| # | pattern | matches | files | bearing on Q1 |
|---|---|---|---|---|
| P1 | `declaration\s+gate` | **46** | **34** | the primary term |
| P2 | `declaration[_-]gate` | 0 | 0 | no snake/kebab form; **no file, section, or flag named for it** |
| P3 | `DECLARATION_GATE` / `gate of declaration` / `declaration-gate` | 0 | 0 | no identifier form |
| P4 | `declaration\s+gate\s+(is\|means\|=\|:)\s+` *(definition form, excluding "untouched"/"the principal")* | **2** | 2 | both are `is the principal's` — **custody, not definition** |
| P5 | `(defin\w+)\W{0,40}declaration` \| `declaration\W{0,40}(defin\w+)` | **0** | **0** | **nothing anywhere defines "declaration"** |
| P6 | `DECLARATION\s*=` | 45 | 36 | flag-block field; always `not-made` |
| P7 | `declares?\s+nothing` | 32 | 23 | the negative form only |
| P8 | `scoring\s+is\s+never\s+declaration` | 7 | 6 | separates scoring from declaration; defines neither |
| P9 | `principal's,\s*separately` | 9 | 7 | custody assertion |
| P10 | `(gate\W{0,30}declar \| declar\w*\W{0,30}gate)` *(proximity net)* | 150 | 132 | superset of P1; residue inspected, no definition |
| P11 | `act of declaration` \| `declaring act` \| `declaration act` | 0 | 0 | no alternate name |
| P12 | `release\s+condition` | 520 | 171 | Q3/Q4 candidate |
| P13 | `GOV-F` | 67 | 45 | Q4 candidate — **is defined** (§6.2) |
| P14 | `G-VERDICT` \| `Gv3` | 19 | 4 | Q4 candidate |
| P15 | `comparison\s+ban` | 16 | 12 | Q4 candidate |
| P16 | `the\s+end[- ]test` | 60 | 47 | Q4 candidate |
| P17 | `gate[- ]?6` \| `Gate-6` | 105 | 80 | Q4 candidate |
| P18 | filename glob `*declaration*` | 6 files | — | 3 artifacts + sidecars; **none is the gate** (§3.4) |
| P19 | filename glob `*gate*` | ~60 files | — | all are BID/BCC/GATE1-4 technical gates; **none is the gate** |
| P20 | `road 20` \| `item 20` \| `(road 20)` | **1** | **1** | the sole road binding (§4.3) |

**Targeted sub-corpus sweeps (zero-hit confirmations):**

| sub-corpus | files | `declaration gate` | `release condition` |
|---|---|---|---|
| The 28 rulings — `DOR_NNN_*` (14) + `DECISION_OF_RECORD_NNN_*` (14) | 28 | **0** | **0** |
| `relay_inbox` | 442 | **0** | 6 files |
| `relay_outbox` | 788 | **0** | 9 files |
| All plan versions (`PLAN_TO_ALPHA_V003…V008`, `THE_PLAN_TO_ALPHA_AND_GRAVITY_V001…V004`, `STAGE8_MASTER_PLAN_TO_ALPHA_V001`) | 11 | **0** | 4 files (`…AND_GRAVITY_V001–V004` only) |
| `DECLINE_REGISTER_V001` + `V002` | 2 | **0** | 2 |
| `STAGE8_7A_OBS22_RECOGNITION_PREREG_V002_FROZEN.md` (the governing frozen spec, `9f0d12b4…`, 802 lines) | 1 | **0** | 0 |

The **28 rulings were enumerated under both prefixes as the commission required** and
each read: 14 × `DOR_016…DOR_020_*`, 14 × `DECISION_OF_RECORD_003…015`. (Nine further
artifacts carry `DECISION_OF_RECORD` embedded rather than prefixed —
`ENTRY_ROUND_2_`, `INSTRUMENT_V003_`, `INSTRUMENT_V004_`, `JOINT_ANCHOR_`,
`K_R_FREEZE_`, `LAMBDA_SPIN_FREEZE_`, `LINE6_SITTING_`, `SLOT18_NOMINATION_RULE_`,
`SLOT2_DISCHARGE_CONDITION_REANCHORED_`. These were swept in the general corpus and
also return zero.)

**Where the sweep stops.** Non-text binaries (`.pyc`, `.npz`, `.png`, `.zip`, `.pack`,
`.idx`), vendored dependency trees (`site-packages`, `.proof_deps/sympy`), and VCS
internals were excluded as noise. `.seal.sha256` sidecars (5,747 files) are digests,
not prose. Nothing excluded as noise is a plausible carrier of a governance
definition. The 17 commission-barred files are the only substantive exclusion, and
their exclusion is the point of the commission.

---

## 3. Q1 — DOES THE DECLARATION GATE HAVE A CONSTITUTIVE DEFINITION?

### GRADE: **ABSENT**

Not NAMED-ONLY, and here is the distinction that matters. NAMED-ONLY would mean the
term appears as a name for a thing whose existence some artifact asserts. What the
bytes show is weaker: the term appears **only inside negative clauses and custody
clauses** — statements that the gate was *not* touched and that it belongs to the
principal. No artifact anywhere says the gate exists as an object with content, names
its inputs, states its criteria, or identifies what act passing it would constitute.
There is no constituting instrument, no ruling, no spec section, no flag, no file
named for it, no identifier form of the name (P2/P3 = 0), and **nothing in the corpus
defines the word "declaration" as a program act** (P5 = 0).

### 3.1 Count by speech act — 29 distinct occurrences, 20 distinct artifacts

| speech act | count | share |
|---|---|---|
| (i) **DEFINITION** — states what the gate *is* | **0** | 0% |
| (ii) **CONSTITUTION** — a ruling or spec that establishes it | **0** | 0% |
| (iii) **UNTOUCHED-ASSERTION** — declares only that it was not touched | **17** | 59% |
| (iv) **REFERENCE** — mentions it as existing / assigns custody | **11** | 38% |
| (v) **OTHER** — unrelated software homonym | **1** | 3% |
| **TOTAL** | **29** | 100% |

Raw match total 46 = 32 supervision (16 × 2 mirrors) + 2 TASK6 (1 × 2 mirrors) + 12
workspace-only. Distinct = 16 + 1 + 12 = **29**.

### 3.2 The 17 untouched-assertions (speech act iii)

| # | file:line | text at bytes |
|---|---|---|
| 1 | `SUP/THE_GRAVITY_CLOSE_ASSEMBLY_V001_2026-08-15.md:3` | "The declaration gate is untouched and the principal's, separately" |
| 2 | `SUP/THE_GRAVITY_CLOSE_ASSEMBLY_V001_2026-08-15.md:101` | "touches neither GOV-F nor the declaration gate" |
| 3 | `SUP/THE_GRAVITY_CLOSE_ASSEMBLY_V002_2026-08-15.md:12` | "The declaration gate is untouched and the principal's, separately" |
| 4 | `SUP/THE_GRAVITY_CLOSE_ASSEMBLY_V002_2026-08-15.md:123` | "touches neither GOV-F nor the declaration gate" |
| 5 | `SUP/THE_GRAVITY_CLOSE_SEALED_2026-08-15.md:21` | "GOV-F untouched; the declaration gate untouched; no flag flips by this seal" |
| 6 | `SUP/U2_CLOSURE_FORM_S_SEALED_2026-08-15.md:40` | "GOV-F untouched; the declaration gate untouched" |
| 7 | `SUP/THE_HANDOFF_2026-08-15_V001.md:14` | "GOV-F untouched; the declaration gate untouched" |
| 8 | `SUP/CONTINUATION_STATE.md:26` | "GOV-F flags untouched; the declaration gate untouched" |
| 9 | `SUP/THE_HANDOFF_2026-08-15_V002.md:12` | "GOV-F untouched; declaration gate untouched" |
| 10 | `SUP/THE_CLOSE_CONDITIONAL_WORD_2026-08-15.md:14` | "the declaration gate — untouched; GOV-F — untouched" |
| 11 | `SUP/CLOSE_ASSEMBLY_V001_CHECK_FINDINGS_2026-08-15.md:52` | "declaration gate and GOV-F untouched as stated" |
| 12 | `SUP/ACT5_RULE2_AUTHOR_DECISION_2026-08-15.md:18` | "the declaration gate and GOV-F untouched" |
| 13 | `SUP/RULE2_ENTRY_ADDENDUM_2026-08-15.md:29` | "the rank pair untouched; the declaration gate and GOV-F untouched" |
| 14 | `SUP/THE_HANDOFF_2026-08-15_V003.md:16` | "GOV-F untouched; the declaration gate untouched" |
| 15 | `WS/STAGE8_GRAVITY_CLOSE_SCORING_V001.md:12` | "THE DECLARATION GATE IS UNTOUCHED — it is the principal's, separately" |
| 16 | `WS/STAGE8_GRAVITY_CLOSE_SCORING_V001.md:35` | "declares nothing, declaration gate untouched" |
| 17 | `WS/STAGE8_GRAVITY_CLOSE_SCORING_V001.md:449` | "PROVISIONAL-OF-SCORING; the declaration gate untouched" |

### 3.3 The 11 references / custody-assertions (speech act iv)

| # | file:line | text at bytes |
|---|---|---|
| 18 | `SUP/THE_HANDOFF_2026-08-14_V002.md:78` | "GOV-F flags untouched; scoring never declaration; the declaration gate is the principal's" — **EARLIEST governance occurrence in a supervision artifact** |
| 19 | `SUP/THE_HANDOFF_2026-08-15_V003.md:48` | "The declaration gate (road 20) + the signature (21): his, unhurried." — **the sole road binding in the corpus** |
| 20 | `WS/STAGE8_GRAVITY_CLOSE_SCORING_V001.md:392` | "DECLARATION = not-made (… the declaration gate is the principal's, separately …)" |
| 21 | `WS/STAGE8_GRAVITY_CLOSE_SCORING_AUDIT_V001.md:14` | "GOV-F IS UNTOUCHED. The declaration gate is the principal's." |
| 22 | `WS/STAGE8_GRAVITY_CLOSE_RESCORE_T9SR_V001.md:10` | "THIS ARTIFACT DECLARES NOTHING AND LANDS NOTHING. The declaration gate is the principal's, separately." |
| 23 | `WS/STAGE8_GRAVITY_CLOSE_RESCORE_T9SR_V001.md:399` | "DECLARATION = not-made (… the declaration gate is the principal's, separately …)" |
| 24 | `WS/STAGE8_GRAVITY_CLOSE_RESCORE_T9SR_AUDIT_V001.md:504` | "DECLARATION = not-made (this audit declares nothing; the declaration gate is the principal's, separately)" |
| 25 | `WS/STAGE8_CARRIER_TRIAGE_S9AD_V001.md:14` | "scoring is never declaration; the declaration gate is the principal's" |
| 26 | `WS/STAGE8_CARRIER_TRIAGE_S9AD_V001.md:409` | "DECLARATION = not-made (… the declaration gate is the principal's)" |
| 27 | `WS/STAGE8_CARRIER_TRIAGE_S9AD_AUDIT_V001.md:12` | "scoring is never declaration; the declaration gate is the principal's" |
| 28 | `WS/STAGE8_CARRIER_TRIAGE_S9AD_AUDIT_V001.md:384` | "DECLARATION = not-made (… the declaration gate is the principal's)" |

Occurrence 18 is the fullest statement anywhere, and its content is exhausted by:
*scoring ≠ declaration*, and *the gate is the principal's*. Neither is a definition.

### 3.4 The one homonym (speech act v) — logged, excluded from the chain

`WS/STAGE8_TASK6_ARGV_PREFIX_FIX_LANE2_V001.md:55` (mirrored identically to the
cleanroom, `5fb65c12…`, both mtime 2026-08-07) carries the section heading:

> `### 2.2 Entry declaration gate`

Read at bytes, this is a **software validation predicate**: `verifier_entry_target()`
requiring that a manifest's `entry_point` be a package-relative Python source name,
resolve inside the verifier package, exist, be a member of the digest allowlist, and
rehash to that member's digest. It is a gate on *entry-point declarations in a build
manifest*. It has no relation whatever to the program's governance declaration gate,
shares no vocabulary with it beyond the two words, and predates the governance term by
seven days. **Recorded as a false positive.** It is the earliest occurrence of the
literal string in the corpus, and a naive earliest-occurrence answer that returned it
would be wrong.

### 3.5 What the corpus establishes *around* the gate but never about it

Three things are asserted repeatedly and are **not** definitions of the gate, though a
reader could mistake them for the beginnings of one:

1. **Custody.** "The declaration gate is the principal's" / "his, unhurried" (11
   occurrences). This says *who* may act, never *what* the act is.
2. **Non-identity with scoring.** "Scoring is never declaration" (7 occurrences).
   This excludes one thing from being declaration; it does not say what declaration is.
3. **A negative gloss, once, obliquely.** `SUP/THE_HANDOFF_2026-08-14_V001.md:93`
   describes the endgame sequence as "…gravity close (the frozen recognition spec
   scored — where 'it was GR' gets said of record or not) → THE SIGNATURE." This is
   the only text in the corpus that gestures at the *content* an eventual declaration
   might have. It does not use the term "declaration gate", is not a definition, is
   not in a constituting instrument, and names no criterion. Recorded as the nearest
   adjacent text, explicitly **not** as a definition.

---

## 4. Q2 — THE EARLIEST OCCURRENCE AND THE CHAIN

### 4.1 Earliest occurrence

**Literal string, corpus-wide:** `STAGE8_TASK6_ARGV_PREFIX_FIX_LANE2_V001.md:55`,
mtime **2026-08-07 10:30**, speech act **(v) homonym** — a build-manifest entry-point
predicate. Not the governance term (§3.4).

**The governance term, earliest at bytes:**
`/Users/bgm/MB Work/alpha-program-archive/workspace/STAGE8_GRAVITY_CLOSE_SCORING_V001.md:12`
— in-document `Date: 2026-08-14`, mtime **2026-08-14 13:40**. Speech act **(iii)
untouched-assertion**, in the artifact's opening discipline block:

> "**THIS ARTIFACT DECLARES NOTHING. THE DECLARATION GATE IS UNTOUCHED — it is
> the principal's, separately. GOV-F IS UNTOUCHED — sealed-spec flags belong
> to the Gate-6 evaluator alone.**"

The second-earliest is its paired hostile audit,
`STAGE8_GRAVITY_CLOSE_SCORING_AUDIT_V001.md:14` (Date 2026-08-14, mtime 14:01), and
the third is `THE_HANDOFF_2026-08-14_V002.md:78` (mtime 14:05).

**Standing caveat, stated because it bears on the chain:** filesystem mtime is not
authorship date and the supervision mirror rewrites mtimes. The ordering above is
corroborated by in-document `Date:` headers (both scoring artifacts self-date
2026-08-14) and by the handoff's own account of the scoring pair as "IN FLIGHT AT
WRITING". Where mtime alone would decide, the finding is marked
**INDETERMINATE-AT-BYTES** rather than asserted.

### 4.2 The term entered from an off-disk brief

`THE_HANDOFF_2026-08-14_V002.md:75-79` records the commission under which the scoring
artifact was produced:

> "3. gravity-close-scoring (wf_4f6835c2-2ef): the FROZEN OBS-22 recognition spec
> (9f0d12b4, bytes govern; GOV-F flags untouched; scoring never declaration; the
> declaration gate is the principal's) scored against the sealed corpus."

This is the registrar restating the brief given to lane `wf_4f6835c2-2ef`. **That
brief does not exist on disk.** A corpus-wide sweep for `4f6835c2` returns exactly two
files — the two mirrors of this handoff. A sweep for `gravity-close-scoring` or
`GRV-SCORE` returns only the scoring artifact itself and this handoff. There is **no
`RELAY_PASTE_*` file, no staging artifact, and no commission record** carrying the
brief. The term's point of entry into the record is therefore a **brief authored
off-disk**, and its first surviving byte-instance is the lane artifact that received
it — already in the untouched/custody form, already presupposing the gate as a known
object.

### 4.3 The chain, forward — every link inherits, none constitutes

```
[off-disk brief to wf_4f6835c2-2ef]           ← term originates here; NOT ON DISK
  │  "GOV-F flags untouched; scoring never declaration;
  │   the declaration gate is the principal's"
  ▼
2026-08-14 13:40  STAGE8_GRAVITY_CLOSE_SCORING_V001.md:12,35,392,449   (iii)(iii)(iv)(iii)
  │               ← first bytes; discipline block; declares nothing
  ▼
2026-08-14 14:01  STAGE8_GRAVITY_CLOSE_SCORING_AUDIT_V001.md:14        (iv)
  │               ← hostile audit repeats the discipline verbatim
  ▼
2026-08-14 14:05  THE_HANDOFF_2026-08-14_V002.md:78                    (iv)
  │               ← registrar records the brief in the session-transfer instrument
  ▼
2026-08-14 18:53  STAGE8_CARRIER_TRIAGE_S9AD_V001.md:14,409            (iv)(iv)
2026-08-14 19:09  STAGE8_CARRIER_TRIAGE_S9AD_AUDIT_V001.md:12,384      (iv)(iv)
2026-08-14 21:24  U2_CLOSURE_FORM_S_SEALED_2026-08-15.md:40            (iii)
2026-08-14 22:21  THE_HANDOFF_2026-08-15_V001.md:14                    (iii)
2026-08-14 23:43  CONTINUATION_STATE.md:26                             (iii)
2026-08-15 00:57  THE_HANDOFF_2026-08-15_V002.md:12                    (iii)
2026-08-15 05:01  STAGE8_GRAVITY_CLOSE_RESCORE_T9SR_V001.md:10,399     (iv)(iv)
                  STAGE8_GRAVITY_CLOSE_RESCORE_T9SR_AUDIT_V001.md:504  (iv)
2026-08-15 07:23  THE_GRAVITY_CLOSE_ASSEMBLY_V001_2026-08-15.md:3,101  (iii)(iii)
2026-08-15 07:25  THE_CLOSE_CONDITIONAL_WORD_2026-08-15.md:14          (iii)
2026-08-15 08:04  CLOSE_ASSEMBLY_V001_CHECK_FINDINGS_2026-08-15.md:52  (iii)
2026-08-15 08:05  THE_GRAVITY_CLOSE_ASSEMBLY_V002_2026-08-15.md:12,123 (iii)(iii)
2026-08-15 ~08:1  THE_GRAVITY_CLOSE_SEALED_2026-08-15.md:21            (iii)
2026-08-15 08:13  ACT5_RULE2_AUTHOR_DECISION_2026-08-15.md:18          (iii)
2026-08-15 10:30  RULE2_ENTRY_ADDENDUM_2026-08-15.md:29                (iii)
2026-08-15 11:25  THE_HANDOFF_2026-08-15_V003.md:16                    (iii)
2026-08-15 11:25  THE_HANDOFF_2026-08-15_V003.md:48                    (iv)  ← "(road 20)"
```

**Plainly: the term entered as a custody-plus-untouched assertion in a lane discipline
block on 2026-08-14, and was never constituted.** In the 28 occurrences after the
first, the speech act never changes class. Not one is a definition. Not one is a
ruling. The term propagates by quotation of a boilerplate discipline line — the same
five-to-twelve words recur across supervision instruments, lane builds, hostile
audits, sealed closures and session handoffs — accreting authority through repetition
while its referent is never fixed. The single semantic addition across the whole chain
is the road binding at `THE_HANDOFF_2026-08-15_V003.md:48`, "The declaration gate
(road 20) + the signature (21): his, unhurried", which attaches the undefined term to
a road slot without saying what the slot contains. That line is also the **only**
occurrence of `road 20` / `item 20` in the entire swept corpus (P20 = 1).

### 4.4 Does any occurrence cite a definition elsewhere?

**No.** All 28 governance occurrences were read in context. **Zero** carry a citation,
digest, file reference, section pointer, or "per …" clause attached to the declaration
gate. This is conspicuous because the surrounding text is dense with citations: the
same sentences that leave the declaration gate bare pin GOV-F to `V011 :1763-1765`,
the frozen spec to `9f0d12b4…`, the guard to `2baa4c31…`, the held design to
`506bfe2a…` / `5fa46838`. The corpus cites everything it touches **except** this. There
is therefore **no dangling citation to check** — the failure mode is not a broken
pointer to a missing target, it is the **complete absence of any pointer**.

---

## 5. Q3 — THE TWO RELEASE-CONDITION ARTIFACTS

### 5.1 Standing at bytes

| | `RELEASE_CONDITION_DRAFT_V001.md` | `RELEASE_CONDITION_F2_DRAFT_V001.md` |
|---|---|---|
| path | `alpha_supervision/` + supervision mirror + **cleanroom mirror** | `alpha_supervision/` + supervision mirror — **NOT mirrored to cleanroom** |
| live sha256 | `503767bbd0e5bd1c3137ce3ab6396a434eae7589c85e2093a8e32979a8106d4e` | `5a94a1dd7bd606b4a4303a9a4c0e869ebe6f516b869845d70418048b47b44d5a` |
| `.seal.sha256` sidecar | present, **MATCH** | present, **MATCH** |
| bare `<stem>.sha256` sidecar | absent | absent |
| mtime | 2026-08-10 06:21 | 2026-08-13 08:21 |
| self-declared standing | **"STATUS: FROZEN — PRINCIPAL APPROVED 2026-08-10"** | **"Status: DRAFT for review."** / title "for the principal's review" |
| structure | FENCE 1 / 2 / 3, criteria R1.1–R3.4 | GATE 1 / 2 / 3, criteria G1.1–G3.3, plus FALSIFIERS |
| **standing of record** | **FROZEN; the release condition of record** | **DRAFT; never acted on** |

Both sealed under the `<stem>.seal.sha256` convention only; the bare `<stem>.sha256`
form is absent for both (sidecar trap probed on both conventions, as required).

**The CARRIED GIVEN checks out against the artifacts.** The register row handed to
this lane states the release condition is frozen, that
`RELEASE_CONDITION_DRAFT_V001.md` carries the freeze at `503767bbd0e5bd1c…`, that it
holds three fences in strict order (kappa_record → alpha → comparison), and that the
order is the law with a failed condition stopping the sequence. **Every clause
verifies at bytes.** The live digest is `503767bbd0e5bd1c…` (exact prefix match); the
document's three fences are titled exactly `FENCE 1 — kappa_record_computed`,
`FENCE 2 — alpha_computed`, `FENCE 3 — comparison to the measured constant`; and §"THE
ORDER IS THE LAW" reads "The fences flip in order 1 -> 2 -> 3; no fence may be
evaluated out of order; a failed condition stops the sequence and is registered as a
stop, not routed around." The given's *consequence* line ("zero open principal
decisions" in the endgame) is a characterization, not a byte, and is **outside** what
this audit can confirm — but see §5.5, where it bears directly on the problem.

### 5.2 Relationship — the later **neither supersedes nor amends** the frozen one

**Grade: PARALLEL / UNRESOLVED — the later is an independent, differently-structured
draft of the same plan obligation (plan item F2), authored after the obligation was
already discharged by freeze, and never reconciled with it.**

The evidence:

- **Same obligation.** The frozen one opens: "The comparison ban's release condition,
  never authored of record (four files assert its nonexistence — Q-691 item 9; **plan
  F2**)." The later one is *named* `F2` and its release order line begins "`author F2
  (this)`". Both are the plan's F2 item.
- **No supersession language in either direction.** `RELEASE_CONDITION_F2_DRAFT_V001`
  contains no reference to `RELEASE_CONDITION_DRAFT_V001`, no digest of it, no
  "supersedes", "amends", or "replaces". `RELEASE_CONDITION_DRAFT_V001` predates it and
  cannot refer to it. **Neither artifact mentions the other.**
- **The frozen one forbids silent amendment.** "amendments only by decision-of-record
  with the change log updated and the principal's freeze renewed." No such
  decision-of-record exists (§5.4). Under the frozen document's own terms, the later
  draft therefore **cannot** have amended it.
- **Not a duplicate.** The two differ substantively (§5.3).
- **Not unrelated.** They address the identical governance obligation with the
  identical three-stage ordering.

### 5.3 What differs substantively

| | frozen V001 (2026-08-10) | F2 draft V001 (2026-08-13) |
|---|---|---|
| **naming** | FENCE 1/2/3 | GATE 1/2/3 |
| **fence-1 content** | record-chain completeness: d_K formed with ten member components; Theorem 3's five S32 hypotheses PROVED; forced M11 route with mechanical certificate (802/807 standard), opposite-lane cross-check; freedoms-consumed SUBSTITUTED: NONE | **winding-forcing closure**: Q-1011 residuals *closed* not adjudicated — q_N completeness (U3 PARTIAL→complete), U(1)_rel determinacy cross-confirmed by an independent lane, no un-discharged TYPE-R/TYPE-U dependency; plus computand-by-citation (F0), record-native/blind, rationality-first |
| **fence-2 content** | F0's four absences discharged; K_* computed with certificate-grade replayability, exact-rationality typing **registered before the value is inspected**; assembly α = f(K_*, 4π); **R2.4: 7A must stand CLOSED (E3) unless severed by decision-of-record** | κ_record/K_* computed under Gate 1 blind and opposite-lane checked; assembly formula frozen as `α = 1/(4πK_*)` before the number; α from derived K_* and pure geometric 4π only. **No 7A-closure condition at all** |
| **fence-3 content** | fences 1–2 flipped with artifacts cited; **A32 instrument custody holds (holdout seal intact; SPEC-SEAL true at the graph root — currently FALSE; three long poles discharged)**; protocol frozen before the value is known, three-outcome form; run once by a lane that has never seen the measured value, cross-checked once | α computed under Gates 1–2 blind and sealed; comparison spec frozen before the comparison is looked at; run once, no re-run, no adjustment. **No A32/SPEC-SEAL custody condition at all** |
| **falsifiers** | **none stated as such** | **an explicit armed FALSIFIERS block** — five falsifiers, one per gate, each blocking the corresponding flip |
| **who flips** | not attributed clause by clause | **each flip explicitly the principal's**, in an ORDER OF RELEASE chain |
| **live state** | static since freeze | carries an **UPDATE 2026-08-13** recording that G1.1's falsifier **FIRED** (Q-1012): "Gate 1 is NOT passable. κ_record stays fenced." |

The three substantive divergences that matter most: (a) the frozen document conditions
α on **7A closure** (R2.4, default not severed) and the later draft does **not**; (b)
the frozen document conditions the comparison on **A32 instrument custody and
SPEC-SEAL at the graph root** (R3.2, noted "currently FALSE") and the later draft does
**not**; (c) the later draft carries **armed falsifiers** and a **fired one**, and the
frozen document has no falsifier apparatus at all. **Neither document's conditions are
a subset of the other's.** They are not two versions of one text; they are two
different gate systems for the same obligation.

### 5.4 Has any act been taken on the later draft?

**No. No act on `RELEASE_CONDITION_F2_DRAFT_V001.md` exists anywhere in the swept
corpus — no ruling, no freeze, no adoption, no decline, no rejection.**

The complete set of references to it, corpus-wide (P: `RELEASE_CONDITION_F2` = 3
matches, 3 files, = **2 distinct** after mirror collapse):

1. `SUP/THE_HANDOFF_2026-08-14_V001.md:102` — in a KEY DOCUMENTS list:
   "RELEASE_CONDITION_F2 — the anti-fitting gate." A **listing**, no act.
2. `WS/KSTAR_TYPING_DETERMINATION_AUDIT_V001.md:249` — "`RELEASE_CONDITION_F2_DRAFT_V001.md`
   G1.3 'RECORD-NATIVE AND BLIND' is a **DRAFT gate REQUIREMENT on a future
   computation** … not a typing". This is an audit **explicitly refusing to treat it
   as load-bearing** on the ground that it is a draft. A **non-act**, and the closest
   thing to an adjudication of its standing anywhere.

Zero hits in all 28 rulings. Zero in both decline registers. Zero in every plan
version. Zero in `relay_inbox` and `relay_outbox`. No `.seal` beyond its own sidecar,
no freeze line, no supersession notice, no change-log entry naming it.

By contrast the frozen one is **cited as authority** where it appears:
`WS/STAGE8_AXN_SLOT2_DISCHARGE_PATH_CODEX2_V001.md:72` lists it in a sealed-source
table as "`RELEASE_CONDITION_DRAFT_V001.md` (frozen) | `503767bb…` | three fence
prerequisites", and `THE_PLAN_TO_ALPHA_AND_GRAVITY_V004.md:173,183-184` twice states
"the frozen release condition … unchanged" / "the release condition of record governs
the endgame as frozen."

**Stated exactly as the commission asks: the later draft has never been acted on.** It
was authored three days after the obligation it addresses was closed by freeze, it
sits sealed at `5a94a1dd…` in a state its own title calls "for the principal's
review", it is not mirrored to the cleanroom, one audit has declined to rely on it
because it is a draft, and no instrument of record has ever ruled on, adopted,
declined, rejected, or reconciled it.

### 5.5 The consequence this bears on Q1 — reported, not resolved

The carried given's consequence line says the endgame contains "zero open principal
decisions". Against the artifacts, that is true **of the frozen release condition's
three fences** — R1.1–R3.4 are conditions on evidence, and the frozen document
pre-authorizes the sequence once they are met. It is **not** true of the record as a
whole, because two objects sit outside that document: (a)
`RELEASE_CONDITION_F2_DRAFT_V001.md`, an unacted parallel draft carrying a **fired
falsifier** ("Gate 1 is NOT passable") that the frozen document has no apparatus to
represent; and (b) **the declaration gate**, which no document represents at all. The
frozen release condition governs the path from κ_record to the end test. Nothing in it
mentions declaration, gravity recognition, or road item 20.
**INDETERMINATE-AT-BYTES** whether the given's consequence line was intended to cover
these; the bytes do not say.

---

## 6. Q4 — IS THE DECLARATION GATE THE SAME OBJECT AS SOMETHING DEFINED?

Each candidate tested at bytes. A SAME verdict on any would dissolve the problem, so
each was pursued for identifying text rather than dismissed.

### 6.1 The frozen release condition — **DISTINCT**

*Separating text.* The two are named in the same sentences and enumerated as
**different items**, repeatedly. `THE_GRAVITY_CLOSE_SEALED_2026-08-15.md:21-23`:
"GOV-F untouched; the declaration gate untouched; no flag flips by this seal.
**Fences: alpha_computed = false · proof_authorized = false · kappa_record_computed =
false.**" The three fences *are* the frozen release condition's objects (FENCE 1/2/3
govern exactly those three flags); the declaration gate is listed **separately from
them**, in its own clause, in this and 12 further artifacts. Further: the frozen
document's subject matter is the computation of α and its comparison to a measured
constant; road item 20 pairs the declaration gate with **the gravity close**, a
different track that the plan states "neither gates the other"
(`THE_PLAN_TO_ALPHA_AND_GRAVITY_V004.md:183-184`). And the frozen document contains
**zero** occurrences of "declaration". **DISTINCT.**

### 6.2 GOV-F — **DISTINCT**

*Separating text.* GOV-F **is defined**, and its definition is not the declaration
gate's. `WS/STAGE8_G1_KERNEL_CERTIFICATE_V001.md:130-133` quotes it from the sealed
spec:

> "GOV-F FLAG GOVERNANCE. V011 :1763-1765 (Gate 6): 'The dependency graph is
> computed by a separate evaluator. Manuscript status strings and a script's own
> PASS label have no authority.' — no flag is flipped by this certificate or by any
> lane artifact."

GOV-F is a **flag-governance clause of the sealed V011 spec**, reserving flips of
sealed-spec flags to the separate Gate-6 evaluator. The declaration gate is
repeatedly said to be **the principal's**, not the evaluator's. The two are conjoined
by "and"/"nor" in 14 separate artifacts ("touches neither GOV-F nor the declaration
gate"; "the declaration gate and GOV-F untouched") — a conjunction of two items, not
two names for one. **DISTINCT.** *This is the sharpest contrast in the audit: GOV-F
is the same kind of governance object, and it has a quoted definition, a sealed source,
a line range, and a named custodian. The declaration gate has none of these.*

### 6.3 The Gate-6 evaluator — **DISTINCT**

*Separating text.* `WS/STAGE8_CARRIER_TRIAGE_S9AD_V001.md:13-14`: "GOV-F untouched —
sealed-spec flags are the **Gate-6 evaluator's**; scoring is never declaration; the
declaration gate is **the principal's**." One sentence, two custodians, explicitly
different. Gate-6 is a numbered gate of the sealed V011 dependency-graph spec.
**DISTINCT.**

### 6.4 G-VERDICT (and Gv3) — **CANNOT-DETERMINE**

*The strongest candidate, and it does not close.* `THE_PLAN_TO_ALPHA_AND_GRAVITY_V004.md:118,127-129`
defines a G-VERDICT phase — "G-VERDICT (gates unchanged — the frozen spec and the
junction)" — whose terminal item is:

> "**Gv3 GRAVITY WORK CLOSED: decision-of-record; the claim stated in the record's
> own voice, scored, pushed; the article unlocks ('Where Atoms Come From').**
> EXIT: the program's gravity claim on record, scored, done — CLAIMABLE only through Gv."

*For SAME:* Gv3 is a principal-level decision-of-record that states a gravity claim in
the record's voice after scoring — which is what a "declaration" following a
"gravity close" would plausibly be, and road item 20 pairs exactly those two.
*Against SAME:* the two vocabularies **never touch**. `G-VERDICT`/`Gv3` occurs 19
times in 4 files, all plan documents; `declaration gate` occurs 46 times in 34 files,
none of them a plan document (P: plan versions = 0 hits). **No artifact anywhere uses
both terms.** No text identifies them, glosses one by the other, or cites Gv3 when
naming the gate. Gv3 also carries content the declaration gate is never said to carry
(the article unlock), and the plan's Gv3 is scoped to the *whole* gravity phase while
road 20 already treats "THE GRAVITY CLOSE consumed" as a separate conjunct.
**CANNOT-DETERMINE.** The bytes neither identify nor separate them. This is the one
candidate where a principal's own knowledge could decide what the bytes cannot.

### 6.5 The signature (road item 21) — **DISTINCT**

*Separating text.* `SUP/THE_HANDOFF_2026-08-15_V003.md:48`: "The declaration gate
(road 20) **+** the signature (21): his, unhurried." Explicit enumeration as two road
items with two numbers, joined by "+". **DISTINCT.**

### 6.6 The end test — **DISTINCT**

*Separating text.* The end test is a defined object of the **frozen release
condition**: FENCE 3 / R3.4 — "The end test is run ONCE by a lane that has never seen
the measured value in this program's context, cross-checked once, registered whatever
it says." It is a **comparison of a computed α to a measured constant**, executed by a
lane. The declaration gate is a **principal's** act, and every artifact asserting it
untouched simultaneously asserts `alpha_computed = false` — i.e. the gate is being
left untouched in a state where the end test is not even reachable. `THE_HANDOFF_2026-08-14_V001.md:93`
sequences them as separate stages: "…α = 1/(4πK*) → **end test once** → **gravity
close** … → THE SIGNATURE." **DISTINCT.**

### 6.7 The comparison ban — **DISTINCT**

*Separating text.* The comparison ban is identified of record as **G3**, an entry ban
on comparing to measured constants: `SUP/RESULT_FENCE_INVENTORY_AND_WHAT_IS_TESTABLE_TODAY_2026-07-29.md:20`
("THE ONE GENUINE COMPARISON BAN IS G3 — AND … ITS RELEASE CONDITION DOES NOT EXIST"),
and `RELEASE_CONDITION_DRAFT_V001.md:3` opens by naming itself "The comparison ban's
release condition". The comparison ban is thus the object the **frozen release
condition releases** — already shown DISTINCT at §6.1. It predates the declaration
gate by two weeks and shares no text with it. **DISTINCT.**

### 6.8 Additional candidates surfaced by the sweep

| candidate | grade | separating / identifying text |
|---|---|---|
| **§7 "THE GATE" of `THE_GRAVITY_CLOSE_ASSEMBLY_V002`** — the SEAL-or-SEND-BACK decision presented to the principal | **DISTINCT** | The same artifact says at :123 that it "touches neither GOV-F nor **the declaration gate**" while presenting its own §7 gate at :125. An artifact cannot both present a gate and leave that gate untouched. Its gate was moreover **taken** — `THE_GRAVITY_CLOSE_SEALED_2026-08-15.md:3` "THE PRINCIPAL'S WORD: SEAL" — and the same file at :21 still records "the declaration gate untouched". |
| **`RELEASE_CONDITION_F2_DRAFT_V001`, "the program's anti-fitting gate"** (:3; so listed at `THE_HANDOFF_2026-08-14_V001.md:102`) | **DISTINCT** | A gate on *fitting* — conditions before computing α — not on declaring. Also a never-acted draft (§5.4); it could not be the object 17 artifacts call untouched-but-standing. |
| **`ACT2_*_DECLARATION_*` / `PRIMARY_ROUTE_DECLARATION_*`** — the only corpus files named "declaration" | **DISTINCT** | Read at path: carrier-admission, domain-extension, and primary-route declarations. Subject-matter instruments, none referencing a gate, none referenced by any declaration-gate occurrence. |
| **The `DECLARATION` flag field** (`DECLARATION = not-made`, 45 occurrences, 36 files) | **DISTINCT** | A lane flag-block field recording that *the artifact* declared nothing. Its own parenthetical distinguishes them: "DECLARATION = not-made (this artifact declares nothing; **the declaration gate is the principal's**, separately)". The field is a lane's self-report; the gate is a principal's act. |
| **`FINISH B`** (held at the principal's word) | **CANNOT-DETERMINE, not pursued** | Its instrument is `FINISH_B_*`, barred by this commission. Not tested, by design. Flagged so the gap is visible rather than silent. |

**Net: no SAME verdict.** Six DISTINCT on the commission's named candidates, one
CANNOT-DETERMINE (G-VERDICT/Gv3), four further DISTINCT and one untested from the
sweep's own surface. **The problem is not dissolved by identification.**

---

## 7. Q5 — THE SHAPE OF WHAT IS MISSING (report only)

Q1 returned ABSENT, so the shape is reported. **Nothing below is drafted, proposed, or
recommended; no content for any such statement is supplied, and no should-language is
used.** What is absent from the record is a statement of the same *class* as the two
governance objects the corpus does constitute — `GOV-F`, which is quoted from a sealed
spec at a line range with a named custodian and a stated scope of authority, and
`RELEASE_CONDITION_DRAFT_V001.md`, which is a principal-frozen instrument stating
per-fence criteria, an ordering law, and an amendment rule. A statement of that class
for road item 20 would be one that fixes the gate's **referent** (what object is
declared, and in what voice), its **admissible inputs** (which sealed artifacts and
which of their verdicts are consumed, and at what grades), its **criteria** (what must
stand for the gate to be passable, and what would block it), its **custody and act
form** (who may take it, by what instrument, and what the taking produces of record),
and its **relations** to the objects the record already constitutes — the frozen
release condition and its three fences, GOV-F and the Gate-6 evaluator's reserved
flags, the sealed gravity close (`8c9e7d47…`) that road 20 pairs it with, the plan's
Gv3 exit, and road item 21 — since at present the term is bound to none of them by any
byte. Which of those the record actually requires, and what any of them would say, is
a principal act and is not this lane's to state.

---

## 8. IMPORT AUDIT

Notions used above that are **not defined in the corpus**, with a statement of whether
the finding survives without them.

| import | status in corpus | load-bearing? | finding survives? |
|---|---|---|---|
| **"the declaration gate"** | **UNDEFINED — this is the audit's subject** | The whole commission | **YES.** The finding *is* that it is undefined. The audit reports the absence of a definition without needing one; every classification is of the term's *speech act*, which is readable at bytes regardless of referent. |
| **"declaration"** (as a program act) | **UNDEFINED** (P5 = 0 matches corpus-wide for any defining form) | Underlies "scoring is never declaration" | **YES.** The audit never relies on what declaration means; it records that the corpus asserts what declaration is *not* (scoring) and never what it is. |
| **speech-act taxonomy** (definition / constitution / untouched-assertion / reference) | Not a corpus notion — **supplied by the commission** | Structures §3 | **YES.** Supplied by the commissioning brief, applied uniformly, and every classification is shown with the quoted text so a reader can re-grade independently. |
| **"constitutive definition"** | Not a corpus notion — **commission's term** | The Q1 grade | **YES.** Operationalized at bytes as: text stating what the object is, what it gates, or what its criteria are. Under any weaker reading the count is still 0 (P5 = 0). |
| **"road item 20"** and its wording | Its source (`ROAD_REMAINING_FLAT_V001.md`) is **BARRED** | The framing of why item 20 is blocked | **YES, with a stated limit.** The road's own text was never read. The only in-corpus binding is `THE_HANDOFF_2026-08-15_V003.md:48`, "The declaration gate (road 20) + the signature (21)". The audit's findings are about the *term*, not the road; if the road's wording of item 20 contained a definition, this audit could not see it. **Flagged, not resolved.** |
| **mtime as authorship date** | Filesystem metadata, not a corpus notion | The Q2 ordering | **PARTIALLY.** Corroborated by in-document `Date:` headers for the two earliest artifacts. Where mtime alone would decide, marked INDETERMINATE-AT-BYTES (§4.1). The *chain's* conclusion — that no occurrence is a definition — is order-independent and survives entirely. |
| **the CARRIED GIVEN** (register row of 2026-08-10) | Its source is **BARRED**; handed over by the registrar | §5.1 | **YES.** Treated as a claim to check, not authority. Its factual clauses verified against bytes (digest, fence titles, order law). Its consequence line is marked as characterization and explicitly not confirmed (§5.5). |

**IMPORT-BLOCK RECORDED.** Two of the audit's framing notions — the wording of road
item 20, and the register row — have **barred sources**. This is a complete result, not
a failure: the Q1/Q2/Q3/Q4 findings are established from unbarred bytes alone, and the
one place a barred source could change a finding (whether road 20's own text defines
the gate) is named above rather than papered over.

---

## 9. CHOICE LEDGER

| # | choice | type | basis |
|---|---|---|---|
| CL-1 | Treated `alpha_supervision/` and `alpha-program-archive/supervision/` as byte-identical mirrors and collapsed duplicate occurrences | **PREMISE (verified)** | Digest-checked on four hit-bearing files, all IDENTICAL (§1.4). Not assumed. |
| CL-2 | Excluded vendored/VCS/cache trees as noise (4,690 files) | **PREMISE (named)** | `site-packages`, `.proof_deps/sympy`, `__pycache__`, `.git`, `*.pyc`. None is a plausible carrier of a governance definition. Reversible: the primary term does not occur in any of them under the proximity net P10 either. |
| CL-3 | Swept text extensions only (`.md .txt .json .jsonl .py .sh .csv .yaml .yml`) | **PREMISE (named)** | Binaries and digest sidecars carry no prose. |
| CL-4 | Re-ran every count newline-normalized after the line-based sweep under-reported | **PREMISE (corrective)** | 7 wrapped matches and 3 artifacts were invisible to line-grep (§1.3). All reported counts are from the normalized pass. |
| CL-5 | Classified `STAGE8_TASK6_ARGV_PREFIX_FIX_LANE2_V001.md:55` as a homonym and excluded it from the chain | **PREMISE (adjudicated at bytes)** | Read in full context: a `verifier_entry_target()` manifest predicate (§3.4). Retained in the occurrence count as speech act (v) so the exclusion is visible, not silent. |
| CL-6 | Graded Q1 **ABSENT** rather than NAMED-ONLY | **JUDGMENT (stated)** | NAMED-ONLY would require the term to name a thing some artifact asserts to exist with content. All 28 governance occurrences are negative clauses (untouched) or custody clauses (the principal's). No identifier form, no file, no flag, no citation, and "declaration" itself is undefined (P5 = 0). A reader preferring NAMED-ONLY has the full occurrence table in §3.2–3.3 to re-grade from; **the count by speech act is the finding, and it does not move.** |
| CL-7 | Graded G-VERDICT/Gv3 **CANNOT-DETERMINE** rather than DISTINCT | **JUDGMENT (stated)** | The vocabularies never co-occur in any artifact, which is evidence of separation but not of non-identity; the semantic fit to road 20 is real. Declining to resolve at bytes what the bytes do not decide (§6.4). |
| CL-8 | Reported §5.2 as PARALLEL/UNRESOLVED rather than forcing supersedes/amends/duplicates/unrelated | **JUDGMENT (stated)** | None of the four offered relations holds at bytes: neither artifact mentions the other, the frozen one's amendment rule was not satisfied, they are not duplicates, and they are not unrelated. The commission's four options do not exhaust the possibilities; the fifth is reported rather than one of the four forced. |

**ZERO OPEN.** All eight are named premises or stated judgments with their basis and
their reversal path shown.

**TOY_SEPARATION: clean.** Nothing constructed, modelled, or simulated. This artifact
is a byte-level census of an existing corpus and reports only what is and is not
written in it. No surrogate for the record was built at any point, and no finding
rests on anything but quoted bytes at cited file:line.

---

## 10. FLAG BLOCK

```
DECLARATION            = not-made (this audit declares nothing; the declaration
                         gate is the principal's, separately)
GOV_F                  = untouched (no flag flipped; sealed-spec flags remain the
                         Gate-6 evaluator's)
DECLARATION_GATE       = UNTOUCHED — and, per this audit, UNDEFINED AT BYTES

Q1_GRADE               = ABSENT
Q1_OCCURRENCES         = 46 raw / 34 files ; 29 distinct / 20 artifacts
Q1_BY_SPEECH_ACT       = definition 0 · constitution 0 · untouched-assertion 17 ·
                         reference 11 · other(homonym) 1
Q2_EARLIEST_GOVERNANCE = STAGE8_GRAVITY_CLOSE_SCORING_V001.md:12 (2026-08-14,
                         untouched-assertion); term entered from an off-disk brief
                         (wf_4f6835c2-2ef); never constituted; 0 citations anywhere
Q2_EARLIEST_LITERAL    = STAGE8_TASK6_ARGV_PREFIX_FIX_LANE2_V001.md:55 (2026-08-07)
                         — HOMONYM, excluded from the chain
Q3_FROZEN_STANDING     = FROZEN of record, 503767bbd0e5bd1c…, seal MATCH,
                         carried-given verified at bytes
Q3_F2_STANDING         = DRAFT, never acted on, 5a94a1dd7bd606b4…, seal MATCH,
                         not mirrored to cleanroom, 2 references corpus-wide,
                         both non-acts
Q3_RELATION            = PARALLEL / UNRESOLVED (neither supersedes, amends,
                         duplicates, nor is unrelated to the other)
Q4_GRADES              = release condition DISTINCT · GOV-F DISTINCT ·
                         Gate-6 evaluator DISTINCT · G-VERDICT/Gv3
                         CANNOT-DETERMINE · the signature DISTINCT · the end test
                         DISTINCT · the comparison ban DISTINCT ·
                         (+4 surfaced DISTINCT, 1 untested-because-barred)
Q4_NET                 = no SAME verdict; the problem is not dissolved

SWEEP_CORPUS           = 12,935 files across 3 roots (23,498 raw → 18,808 after
                         noise filter → 12,952 text → 12,935 after exclusions)
EXCLUSION_LEAKS        = 0 on every pattern (17 files removed by name, none opened)
BARRED_BYTES_READ      = none
SIDECAR_PROBE          = both conventions probed (<stem>.seal.sha256 and
                         <stem>.sha256) on every artifact whose seal is reported
CHOICE_LEDGER          = 8 entries, all PREMISE(named)/JUDGMENT(stated), zero OPEN
TOY_SEPARATION         = clean
IMPORT_AUDIT           = 7 imports audited; 2 IMPORT-BLOCKS recorded (barred
                         sources: road item 20's wording; the register row).
                         All findings survive without them, limits named.

alpha_computed         = false
proof_authorized       = false
kappa_record_computed  = false
NUMERIC_EVALUATION     = false ; CAS = not invoked ; MEASURED_CONSTANT_COMPARISON = none
CHAIN_INVOKED          = false ; MEMBER_BOUND = false ; MACHINERY_APPEAL = none
FILES_WRITTEN          = 1 (this artifact) + 2 seal sidecars
FILES_EDITED           = 0 ; GIT_ACTION = none
SWEEP_CUTOFF           = 2026-08-16 (all counts as of this session's reads)
```

---

## 11. CUSTODY

Built by the BUILD lane of commission O53SR, 2026-08-16, read-and-report at bytes.
Every count in this artifact is reproducible from the patterns in §2 against the
corpus construction in §1. Every classification in §3 is shown with its quoted text at
a cited file:line so it can be re-graded independently. Where the bytes do not decide,
the artifact says INDETERMINATE-AT-BYTES or CANNOT-DETERMINE rather than choosing.

This artifact neither drafts nor proposes a definition for the declaration gate, and
takes no position on whether road item 20 should be taken. The declaration gate
remains untouched and the principal's.
