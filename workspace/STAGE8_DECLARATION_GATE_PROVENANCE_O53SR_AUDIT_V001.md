# STAGE 8 — THE DECLARATION GATE PROVENANCE — DEFAULT-REFUTE AUDIT — O53SR — V001

## AUDIT LANE — ADVERSARIAL BY MANDATE — DEFAULT VERDICT REFUTED — [SEALED]

Date: 2026-08-16
Role: AUDIT lane of commission O53SR. Default verdict REFUTED; every load-bearing
claim of the build re-derived at bytes before any grade was raised above it. A
principal act is blocked on this pair's return.

**THIS ARTIFACT DECLARES NOTHING, DEFINES NOTHING, AND PROPOSES NOTHING.** It does not
draft, sketch, or recommend a definition for the declaration gate, and takes no
position on whether road item 20 should be taken. The declaration gate is untouched
and remains the principal's. GOV-F is untouched.

Fences held: `alpha_computed = false` ; `proof_authorized = false` ;
`kappa_record_computed = false`. Nothing computed; no magnitude approached; no CAS
invoked; no flag flipped; no file edited; no git write action (read-only `git log`
metadata queries only, §1.5). One file written (this artifact) plus its two seal
sidecars.

TARGET: `/Users/bgm/MB Work/alpha-program-archive/workspace/STAGE8_DECLARATION_GATE_PROVENANCE_O53SR_V001.md`
TARGET SHA256 (recomputed this audit): `20b902496d5dc99424cf17f8ef5120e96beaf069b7268c4c1737f8c867faa87e`
Both target sidecars verified OK independently (`shasum -a 256 -c` on
`.md.seal.sha256` and `.md.sha256`).

---

## 0. VERDICT IN ONE LINE

**OVERALL: CONFIRMED-WITH-CORRECTIONS.** The build's central finding survives a wider,
independently-constructed sweep: **my own independent Q1 grade is ABSENT.** Every one
of the 29 cited occurrences verifies at its cited file:line, no occurrence is a
definition, and a check the build never ran — the full git object history — closes the
last plausible hiding place by showing that **no deleted or superseded artifact ever
carried the term**. But the build's bar declaration is refuted by its own bytes: three
passages assert the *content* of road item 20 while §8 and the flag block declare that
road item 20's text was never read and that no barred bytes entered the audit. That is
**COR-A**, and dimension **D5 is REFUTED** on it.

---

## 1. AUDIT CONSTRUCTION — WIDER THAN THE BUILD'S, ON PURPOSE

### 1.1 Corpus (built independently, not inherited)

| stage | files |
|---|---|
| raw across the three commissioned roots | **23,514** |
| after the exclusion ARRAY (§1.2) | **23,475** |
| **UTF-8-decodable text corpus actually swept** | **18,839** |

I did **not** adopt the build's `.md .txt .json .jsonl .py .sh .csv .yaml .yml`
extension filter and did **not** drop `.git` internals, `.seal.sha256` sidecars,
`site-packages`, or `__pycache__`. My corpus is **5,904 files larger** than the build's
12,935 and is a strict superset of it on every text file. Every count below is from
this wider corpus, whole-file, newline-normalized (`re.sub(r'\s+',' ',text)`),
case-insensitive.

Per-root reconciliation with the build's §1.1, checked because a corpus figure that
cannot be reproduced is a sweep that cannot be trusted:

| root | build's swept figure | re-derived at bytes | verdict |
|---|---|---|---|
| `alpha_supervision` | 993 | 1,001 text-ext − 8 barred = **993** | **EXACT** |
| `alpha-program-archive` | 6,591 | 6,607 text-ext − 8 barred = 6,599 | within 8 |
| cleanroom `_v003` | 5,351 | 5,357 text-ext − 1 barred = 5,356 | within 5 |
| **total swept** | **12,935** | 12,948 | within 13 (0.1%) |

`relay_inbox` **442** and `relay_outbox` **788**: I first read these as impossible
(the archive's own `relay_outbox` holds 492 files total) and drafted a correction.
**I withdraw it.** The figures are the `.md` counts summed across *both* roots that
carry relay directories — inbox 236 (archive) + 206 (cleanroom) = **442**; outbox 392
(archive) + 396 (cleanroom) = **788**. Both **EXACT**. Logged here because an audit
that suppresses its own withdrawn refutation is not reporting its method. The build's
§1.1 does attribute these to the archive row alone, which misplaces ~602 files by
root; immaterial to every finding.

### 1.2 Exclusion globs (ARRAY) and per-pattern leak counter

```
EXCLUSIONS = [
  "QUESTIONS_SETTLED_REGISTER",   "QUESTIONSSETTLED_REGISTER",
  "EXECUTION_TRACKER",            "ROAD_REMAINING",
  "FINISH_B_DECISION_SHEET_2026-08-16", "FINISH_B_SEALED_2026-08-16",
  "_DECISION_SHEET_",
  "STAGE8_DECLARATION_GATE_PROVENANCE_O53SR_AUDIT_V001"   # self-exclude
]
```

| pattern | files removed | **leaks into corpus** |
|---|---|---|
| `QUESTIONS_SETTLED_REGISTER` | 6 | **0** |
| `QUESTIONSSETTLED_REGISTER` | 1 | **0** |
| `EXECUTION_TRACKER` | 4 | **0** |
| `ROAD_REMAINING` | 6 | **0** |
| `FINISH_B_DECISION_SHEET_2026-08-16` | 6 | **0** |
| `FINISH_B_SEALED_2026-08-16` | 6 | **0** |
| `_DECISION_SHEET_` | 10 | **0** |
| self-exclude | 0 | **0** |
| **TOTAL** | **39** | **0** |

39 vs the build's 17 because my filter also removes the `.sha256` sidecars of barred
files, which the build's extension filter had already dropped. Same substantive set.

**INCIDENT LOG.** No barred file was opened at any point in this audit. One incident:
a read-only `git log --pickaxe` **path listing** (§1.5) returned four barred paths
among its results. Only path names were displayed; no blob, no diff, and no content
of any barred file was fetched or read. Recorded rather than suppressed because the
fact that barred paths appear in that list is itself load-bearing on the *scope* of
ABSENT (§2.4).

### 1.3 Sidecar trap — both conventions probed

Probed `<stem>.seal.sha256` **and** `<stem>.sha256` on every artifact whose seal is
reported below. The target artifact is one of the rare files carrying **both** forms;
both verified OK. Both release-condition drafts carry **only** `.seal.sha256`; the
bare form is absent for both, confirming the build's §5.1 row.

### 1.4 Self-exclusion arithmetic (the build's counts are not self-inflated)

The target artifact itself contains **71** occurrences of `declaration gate`, and its
filename contains the string `DECLARATION_GATE`. Excluding the target and its two
sidecars, the corpus returns **46 matches / 34 files** — **exactly** the build's
headline figure. The build's self-exclusion is therefore real and correctly applied.

### 1.5 Git-history check — a check the build did not run

`git log --all -i -S"declaration gate" --pickaxe-regex --name-only` over
`alpha-program-archive`. Result: **22 distinct paths**, and **every one of them exists
in the working tree today**. Separately, the repository's complete deleted-file set is
**14 paths** (relay pastes, evaluator schemas, one provenance-hold sidecar), and **none
of them** appears in the pickaxe result.

**Consequence, and it is the strongest single support for ABSENT in either artifact:
no deleted, superseded, or rewritten artifact ever carried the term.** The universal
negative therefore cannot be defeated by "it was there and got removed". The build did
not test this.

Two further git observations, both non-definitional:
- The term occurs **twice** in `.git/logs/HEAD` and `.git/logs/refs/heads/main` — commit
  `63c27f46`, message: *"…Rule-2 and the declaration gate not covered"*. Speech act
  **reference/custody**, class unchanged. Outside the build's declared corpus (it
  excluded VCS internals as noise, §2 "Where the sweep stops"), so not a defect — but
  the term does exist in commit metadata and this audit records it.
- `git log --all` over all commit subjects and bodies returns **110** `declar*` hits.
  Read at bytes, these record principal *declarations* of subject matter (Q-1070,
  Q-1072, the Act-2 package) and never the declaration gate. No definition.

---

## 2. D1 — THE ABSENT VERDICT — **CONFIRMED**

### 2.1 The build's declared counts, re-run

All over the 18,839-file corpus, target self-excluded, `.git` internals broken out.

| # | pattern | build | **re-derived** | verdict |
|---|---|---|---|---|
| P1 | `declaration\s+gate` | 46 / 34 | **46 / 34** | **EXACT** |
| P1-distinct | after mirror collapse | 29 / 20 | **29 / 20** | **EXACT** |
| P2 | `declaration[_-]gate` | 0 / 0 | **0 / 0** | **EXACT** |
| P3 | `DECLARATION_GATE`, `gate of declaration`, `declaration-gate` | 0 / 0 | **0 / 0** | **EXACT** |
| P5 | `(defin\w+)\W{0,40}declaration` and reverse | 0 / 0 | **0 / 0** | **EXACT** |
| P6 | `DECLARATION\s*=` | 45 / 36 | **45 / 36** | **EXACT** |
| P11 | `act of declaration`\|`declaring act`\|`declaration act` | 0 / 0 | **0 / 0** | **EXACT** |
| P14 | `G-VERDICT`\|`Gv3` | 19 / 4 | 19 / 4 raw, **12 / 2 genuine** | **COR-E** |
| P20 | `road 20`\|`item 20` | 1 / 1 | **2 / 2 raw, 1 distinct** | **COR-D** |
| — | rulings `DOR_*` (14) + `DECISION_OF_RECORD_*` (14) | 28 files, 0 hits | **28 distinct names, 0 hits** | **EXACT** |
| — | `relay_inbox` + `relay_outbox`, both roots | 0 hits | **0 hits** | **EXACT** |
| — | all plan artifacts | 0 hits | **0 hits over 24 plan basenames** | **EXACT** (wider) |

Note P2/P3: the hyphen and underscore forms **do** occur — 7 and 5 matches — but
**every one is inside the target artifact itself** (it quotes its own patterns and its
own filename) or in the target's two sidecars. In the pre-target corpus the build's
zero is right.

### 2.2 Patterns the build did **not** run

The commission required me to attack ABSENT with nets the build never cast. Fourteen
were run; none surfaces a definition.

| net | matches / files | what the residue is at bytes |
|---|---|---|
| `declarat\w*\W{1,60}gate` (60-char proximity) | 57 / 43 | 46 are P1; the 11-match residue: `DECLARATION / GATE_MAP` lane report-board fields, "ledger declarations, gate prose", "Gate history … where-declaration". **Homonyms.** |
| `gate\w*\W{1,60}declarat` (reverse) | 7 / 7 | "the three gate declarations" = fence lines in lane fence-scans; "false gate declarations"; "Gate4 declarations". **Homonyms.** |
| `declar\w*\W{1,80}principal` / reverse | 2 / 2 · 17 / 15 | principal *declarations of subject matter*; never the gate. |
| `declaration sheet` | 2 / 1 | `STAGE8_ACT2_CARRIER_PACKAGE_S9AD_V001.md` §5, PROPOSED-NOT-DECLARED. Not the gate. |
| `the principal's declaration` | 13 / 11 | the ACT-2 declarations and certificate `declaration_source` pins. Not the gate. |
| `declaration of record` | 7 / 5 | scope declarations in 7A restricted booking. Not the gate. |
| `declarable` | 32 / 21 | a **typing class** (derivable/constructible/declarable). Not the gate. |
| `declaration (is\|means\|=\|:\|shall\|must\|consists)` | 266 / 203 | flag fields and `DOOR_7_DECLARATION`; residue read, **no definition**. |
| `decl\.?\s*gate`, `d-?gate`, `dec gate` abbreviations | 0 / 0 | no abbreviated form exists. |
| **`the principal's gate`** | **6 / 6** | **a candidate the build never surfaced — graded in §5.4.** |
| `the gate\W{0,60}principal` / reverse | **0 / 0** | the two words are never brought together in that order anywhere. |
| `gate\s*\(?\s*(road\s*)?2[01]` | 2 / 2 | the `THE_HANDOFF_2026-08-15_V003.md:48` line only. |
| filename `*declaration*` | 3 artifacts | ACT2 ×2 + PRIMARY_ROUTE. **EXACT** — build's figure confirmed. |
| **git object history** (§1.5) | 22 paths, 0 deleted | **no removed carrier ever existed.** |

### 2.3 My independent Q1 grade

**ABSENT.** Reached without adopting the build's taxonomy as authority: I asked only
whether any byte in the unbarred corpus states what the declaration gate *is*, what it
gates, what its criteria are, what act passing it constitutes, or where such a
statement lives. The answer over 18,839 files, 14 additional patterns, and the full git
object history is **no**. The distinction the build draws between ABSENT and NAMED-ONLY
(§3, CL-6) survives attack: the term never once appears in a clause asserting the gate
has content — only in negative clauses (untouched) and custody clauses (the
principal's) — and "declaration" itself is nowhere defined as a program act.

### 2.4 The scope qualification the build's headline omits — **COR-B**

The pickaxe path listing (§1.5) shows that **four of the 22 paths carrying the term are
barred files**: `supervision/ROAD_REMAINING_FLAT_V001.md`,
`supervision/QUESTIONS_SETTLED_REGISTER_V001.md`,
`supervision/FINISH_B_DECISION_SHEET_2026-08-16.md`,
`supervision/FINISH_B_SEALED_2026-08-16.md`. No content of any of them was read.

The build's §8 IMPORT AUDIT states this limit correctly and honestly. But its **§0
verdict line** and **§3 grade paragraph** do not carry it: §0 says *"No ruling, spec,
plan, register, relay, or instrument **anywhere** states what the declaration gate
is"*, and §3 says *"There is no constituting instrument, no ruling, no spec section…"*.
The word **register** appears in that list, and the register is barred and unread.
**ABSENT is a verdict over the unbarred corpus.** The correct headline is: absent from
every artifact this commission may read, with four barred artifacts known to contain
the term and known to be unexamined. The build's own §8 supports this reading; its
headline overstates it. **CORRECTION, not refutation** — the grade does not move.

**D1: CONFIRMED**, with COR-B on the scope of the headline.

---

## 3. D2 — EARLIEST OCCURRENCE AND CHAIN — **CONFIRMED-WITH-CORRECTIONS**

### 3.1 Every cited occurrence verified at bytes

All **29** file:line citations in §3.2/§3.3/§3.4 were opened and checked
programmatically. **29 / 29 carry the term.** Zero mis-citations, zero out-of-range
lines, zero fabricated quotes. Five are newline-wrapped matches
(`ASSEMBLY_V001:3`, `CLOSE_SEALED:21`, `SCORING_V001:392`, `RESCORE_T9SR_V001:399`,
`RESCORE_T9SR_AUDIT:504`); in each the build anchors the citation to the line where the
match **begins**, which is the correct and checkable convention. This is the single
most falsifiable part of the build and it does not fall.

Mirror structure independently digest-checked, not assumed — all four pairs the build
named plus two more: `96bd68e5` `ACT5_RULE2_AUTHOR_DECISION`, `d287f177`
`THE_GRAVITY_CLOSE_SEALED`, `3589241e` `THE_HANDOFF_2026-08-14_V002`, `74ef6085`
`ASSEMBLY_V001`, `070e2e7a` `THE_HANDOFF_2026-08-15_V003`, `9970594a`
`CONTINUATION_STATE`, and `5fb65c12` `TASK6_ARGV` workspace↔cleanroom. **All
IDENTICAL.** The "6 workspace-only hit-bearing artifacts" claim re-derives exactly.

### 3.2 Speech-act classification

Re-graded independently from the quoted bytes. **No occurrence is a definition or a
constitution** — this is the load-bearing classification and it holds at 29/29. The
iii/iv boundary is softer than the build presents it: rows 1, 3 and 15 carry *both* an
untouched clause and a custody clause ("is untouched **and** the principal's,
separately") and were assigned (iii), while rows 20/23/24 carry the same conjunction
inside a flag field and were assigned (iv). The split is by dominant clause, is
defensible, and is **immaterial** — both classes are non-definitions, so the 17/11
partition can move without touching Q1. The build did not ledger this judgment; a
ninth ledger entry would have been the disciplined move. **Noted, not corrected.**

### 3.3 The homonym

`STAGE8_TASK6_ARGV_PREFIX_FIX_LANE2_V001.md:55`, `### 2.2 Entry declaration gate`,
read at bytes: a `verifier_entry_target()` build-manifest predicate. Mirrored to the
cleanroom byte-identically (`5fb65c12…`). **Homonym CONFIRMED**, and the build's
decision to keep it inside the occurrence count as class (v) rather than delete it
silently is the correct disposition. Its priority in date over the governance term is
real, and the build's warning that a naive earliest-string answer would be wrong is
sound.

### 3.4 The off-disk brief — **CONFIRMED, corroborating sentence corrected (COR-C)**

The substantive claim holds at bytes: `4f6835c2` returns **exactly 2 matches in 2
files**, both mirrors of `THE_HANDOFF_2026-08-14_V002.md`. The commission text at
`:75-79` verifies **verbatim**. No `RELAY_PASTE_*`, staging artifact, or commission
record anywhere carries the brief — checked independently against all 3,257
`RELAY_PASTE_*` files. **The term entered from a brief that is not on disk.**

But the sentence offered as corroboration is false as written. The build says: *"A
sweep for `gravity-close-scoring` or `GRV-SCORE` returns only the scoring artifact
itself and this handoff."* At bytes:
- `gravity-close-scoring` (exact literal) → **2 / 2, both mirrors of the handoff. The
  scoring artifact does not contain the string at all.**
- `GRV-SCORE` → **6 / 1, the scoring artifact only. The handoff does not contain it.**

Neither pattern returns the pair the sentence claims; the claim is true only of their
union. Relaxing to `gravity[- ]?close[- ]?scoring` additionally returns
`FIVE_C_PRINCIPAL_ACTS_STAGING_V001.md` ("The gravity-close scoring (road 11, parallel
track)") and `STAGE8_CARRIER_TRIAGE_S9AD_V001.md`, neither of which the build reports.
I opened both: **neither carries the brief**, so the conclusion is undamaged and in
fact strengthened — the off-disk finding survives a looser net than the build ran.
**COR-C: a corroborating sweep sentence that does not reproduce.**

### 3.5 The chain, and the citation question

The forward chain re-derives: the speech act never changes class across all 28
inheriting occurrences, and the sole semantic addition is
`THE_HANDOFF_2026-08-15_V003.md:48`. The build's §4.4 claim — **zero** citations,
digests, or section pointers attached to the declaration gate anywhere, in text
otherwise dense with them — I tested by reading every occurrence's surrounding
sentence. **CONFIRMED.** GOV-F is pinned to `V011 :1763-1765` (verified at
`STAGE8_G1_KERNEL_CERTIFICATE_V001.md:130`, exact line, quote verbatim); the gate is
pinned to nothing. **There is no dangling citation to chase, because there is no
pointer.** The commission's D2 instruction to check any citation whose target the build
said does not exist is therefore satisfied vacuously, and I say so rather than
manufacture a check.

**COR-D:** §2 declares its table reports *"raw matches / files, before mirror
collapse"*, and every row obeys that except **P20**, reported as 1/1 where the raw
figure is **2/2** (both mirrors of `THE_HANDOFF_2026-08-15_V003.md`). One distinct
occurrence — the build's substantive point, that this is the sole road binding in the
corpus, is **correct**; the table cell silently applies a collapse the table says it
does not apply.

**D2: CONFIRMED-WITH-CORRECTIONS** (COR-C, COR-D).

---

## 4. D3 — THE TWO RELEASE-CONDITION DRAFTS — **CONFIRMED**

Both files opened and read in full, independently of the build's account.

### 4.1 Standing at bytes

| | `RELEASE_CONDITION_DRAFT_V001.md` | `RELEASE_CONDITION_F2_DRAFT_V001.md` |
|---|---|---|
| live sha256 | `503767bbd0e5bd1c3137ce3ab6396a434eae7589c85e2093a8e32979a8106d4e` | `5a94a1dd7bd606b4a4303a9a4c0e869ebe6f516b869845d70418048b47b44d5a` |
| `.seal.sha256` | present, **MATCH** | present, **MATCH** |
| bare `<stem>.sha256` | **absent** | **absent** |
| copies corpus-wide | 3 (supervision, mirror, **cleanroom**) | 2 (supervision, mirror — **no cleanroom**) |
| self-declared standing | line 55 `STATUS: **FROZEN — PRINCIPAL APPROVED 2026-08-10**` | line 38 `**Status: DRAFT for review.**`, title "for the principal's review" |

Every cell of the build's §5.1 table **verifies exactly**, including the negative
sidecar probe on both conventions and the asymmetric cleanroom mirroring.

### 4.2 The carried given

Checked clause by clause against the artifacts, as the commission requires — as a
claim, not authority.

- "RELEASE_CONDITION_DRAFT_V001.md now carries the freeze" → line 55. **TRUE.**
- "`503767bbd0e5bd1c…`" → live digest, exact prefix. **TRUE.**
- "draft-at-freeze hash recorded inside" → line 55, `Draft hash at freeze:
  ecd79ad37fa70b60…`. **TRUE**, and `ecd79ad3` independently corroborated at
  `THE_PLAN_TO_ALPHA_AND_GRAVITY_V004.md:24`.
- "three fences in strict order — kappa_record …, alpha …, comparison …" → headings at
  lines 8 / 19 / 34, exactly those three objects in that order. **TRUE.**
- "The order is the law; a failed condition stops the sequence" → §"THE ORDER IS THE
  LAW", lines 49–51, verbatim. **TRUE.**

One apparent tension I checked and resolved rather than reported as a defect:
`THE_PLAN_TO_ALPHA_AND_GRAVITY_V004.md:24` lists "the release-condition freeze
(drafted, ecd79ad3…)" among **PRINCIPAL ITEMS OUTSTANDING**, which would contradict the
freeze. It does not: that STATUS BLOCK is stamped "current to Q-746, **2026-08-09**
evening", one day *before* the freeze, while the same file's 2026-08-10 change-log
entries at `:173` and `:183-184` say "the release condition of record governs the
endgame as frozen" and "All fences and the frozen release condition unchanged". Both
build citations are **line-exact**. No contradiction.

The given's *consequence* line ("zero open principal decisions") is a characterization,
and the build's refusal to confirm it while showing exactly what it does and does not
cover (§5.5) is the correct disposition. I reach the same reading independently and
mark it **INDETERMINATE-AT-BYTES**.

### 4.3 Relation — PARALLEL / UNRESOLVED sustained

Re-derived clause by clause rather than accepted:
- **Same obligation.** Frozen line 3-4: "The comparison ban's release condition … **plan
  F2**". F2 line 36: "`author F2 (this)`". **Both are plan item F2.** CONFIRMED.
- **Neither mentions the other.** Verified by full read of both files and by sweeping
  each digest and filename across the corpus. CONFIRMED.
- **The amendment rule was not satisfied.** Frozen lines 51-53 and 55 require
  "decision-of-record with the change log updated and the principal's freeze renewed";
  no such decision-of-record exists (§4.4). CONFIRMED.
- **Neither's conditions are a subset of the other's.** Re-derived directly: R1.2
  (Theorem 3's five S32 hypotheses) and R2.4 (7A closure) and R3.2 (A32 custody +
  SPEC-SEAL, "currently FALSE") have **no F2 counterpart**; G1.1 (Q-1011 winding-forcing
  closure) and the entire **FALSIFIERS** block have **no frozen counterpart**.
  **CONFIRMED.** The build's three named "divergences that matter most" are each exact
  at bytes, including the fired falsifier at line 42 — "**Gate 1 is NOT passable.**
  κ_record stays fenced."

The build's refusal to force one of the commission's four offered relations, and its
naming of a fifth, is ledgered at CL-8 and is the honest call.

### 4.4 Independent hunt for any act on the later draft

Hunted independently and more widely than the build, per the D3 mandate: by filename,
by digest `5a94a1dd`, by the phrase "anti-fitting gate", across all 28 rulings, both
decline registers, every plan artifact, **both** relay directories in **both** roots,
all 3,257 relay pastes, and the git commit history.

**Result: no act exists.** `RELEASE_CONDITION_F2` returns 5 matches / 5 files — two
mirror pairs plus one — reducing to exactly the **two distinct non-acts** the build
reported:
1. `THE_HANDOFF_2026-08-14_V001.md:102`, a KEY DOCUMENTS listing, verified at bytes.
2. `KSTAR_TYPING_DETERMINATION_AUDIT_V001.md:249`, verified at bytes: an audit
   **declining to rely on it** because it is a draft.

The only object I found that the build did not report is a **git commit message**
(`9178b744`): "Release condition F2 DRAFT (the never-authored anti-fitting gate)…".
Committing a file is not an act of record, and the message's own words call the gate
"never-authored". It does not disturb the finding — it corroborates it.

**D3: CONFIRMED.** No correction.

---

## 5. D4 — THE IDENTIFICATIONS — **CONFIRMED-WITH-CORRECTIONS**

The commission is explicit that a missed SAME is the most consequential error
available. I attacked each DISTINCT for being too quick, and the one non-DISTINCT for
being a name coincidence.

### 5.1 Every DISTINCT grade's separating text verified at bytes

| candidate | build | separating text re-read at bytes | my grade |
|---|---|---|---|
| frozen release condition | DISTINCT | the frozen file contains **0** occurrences of "declaration" (verified by count); the gate is listed in a clause separate from the three fences in 13 artifacts | **DISTINCT — sustained** |
| GOV-F | DISTINCT | `STAGE8_G1_KERNEL_CERTIFICATE_V001.md:130` — quote **verbatim**, line **exact**; GOV-F reserved to the *Gate-6 evaluator*, the gate to *the principal*; conjoined by "and"/"nor" | **DISTINCT — sustained** |
| Gate-6 evaluator | DISTINCT | `STAGE8_CARRIER_TRIAGE_S9AD_V001.md:14` — one sentence, two custodians, explicitly different | **DISTINCT — sustained** |
| the signature (21) | DISTINCT | `THE_HANDOFF_2026-08-15_V003.md:48` — "(road 20) **+** … (21)" | **DISTINCT — sustained** |
| the end test | DISTINCT | frozen R3.4 read in full: a lane-run comparison; the gate is a principal act asserted untouched while `alpha_computed = false` | **DISTINCT — sustained** |
| the comparison ban | DISTINCT | `RESULT_FENCE_INVENTORY…:20` "THE ONE GENUINE COMPARISON BAN IS G3"; the frozen doc names itself its release condition | **DISTINCT — sustained** |
| §7 "THE GATE" of the close assembly | DISTINCT | `ASSEMBLY_V002:123` "touches neither GOV-F nor the declaration gate" vs `:125` "## 7. THE GATE"; and `THE_GRAVITY_CLOSE_SEALED:3` "**THE PRINCIPAL'S WORD: SEAL**" while `:21` still records the declaration gate untouched | **DISTINCT — sustained, and decisive** |
| F2 "anti-fitting gate" | DISTINCT | a gate on *fitting*, never acted on | **DISTINCT — sustained** |
| the three `*DECLARATION*` files | DISTINCT | 3 artifacts confirmed by filename glob | **DISTINCT — sustained (see 5.3)** |
| `DECLARATION` flag field | DISTINCT | its own parenthetical separates them | **DISTINCT — sustained** |

**No SAME survives. The problem is not dissolved by identification.** I reach this
independently.

### 5.2 The one non-DISTINCT, attacked for name coincidence

`G-VERDICT` / `Gv3` — **CANNOT-DETERMINE sustained.** The decisive test is the
build's: do the vocabularies ever co-occur? Re-run independently across the full
unbarred corpus: **FILES WITH BOTH = [] — zero.** No artifact anywhere uses both terms.
The plan's `Gv3` line quoted at `V004:118,127-129` verifies. The semantic fit is real
and the bytes neither identify nor separate. Declining to resolve is correct.

**COR-E.** The build's P14 count is inflated by a substring false positive it did not
catch: `G-VERDICT` matches inside "**clearin*g-verdict*** gate" in `1091_DONE.md`. Of
19 raw matches in 4 files, **7 matches in 2 files are that artifact**; the genuine
count is **12 matches in 2 files = one distinct artifact**,
`THE_PLAN_TO_ALPHA_AND_GRAVITY_V004.md`. The build's gloss "all plan documents" is
therefore wrong for half its files. The finding **strengthens** on correction — the
`Gv3` vocabulary is confined to a single artifact — but a sweep that reports a
false-positive count as evidence is a defect.

### 5.3 Candidates the build did not surface — **COR-F**

Three real candidates were missed. All three grade out, so Q4's net is unchanged; the
defect is in the completeness of the candidate set on the dimension where completeness
matters most.

1. **"the principal's gate"** — 6 matches / 6 files, a phrase the build never swept.
   Two senses at bytes. (a) `THE_HANDOFF_2026-08-15_V002.md` and
   `STAGE8_5D_SYMMETRIC_AUDIT_T13SR_V001.md`: "the carrier triage proved **the close** a
   principal's gate (Q-1078)" — an object the corpus *does* constitute (Q-1078: exactly
   three acts, no fourth road). **DISTINCT**, on the build's own §6.8 evidence: that
   gate was **taken** ("THE PRINCIPAL'S WORD: SEAL") while the same sealed file records
   the declaration gate untouched. (b) `STAGE8_TASK5_EQ6_DETERMINATION_MAP_LANE1_V001.md`
   / `STAGE8_TWIST_EVIDENCE_O40SR_V001.md`: "YOURS = a genuine law/member choice
   requiring the principal's gate" — a **typing category**, not an act. **DISTINCT.**

2. **The principal's declaration act-form** (as distinct from the three
   `*DECLARATION*`-named files the build graded). The corpus constitutes a declaration
   *mechanism*: staged sheets (`STAGE8_ACT2_CARRIER_PACKAGE_S9AD_V001.md` §5,
   PROPOSED-NOT-DECLARED), then the act ("**THE ACT.** The principal's declaration of
   2026-08-14"). **DISTINCT, and decisively so at timestamps the build never used:**
   `ACT2_CARRIER_ADMISSION_DECLARATION` (17:18) and `ACT2_DOMAIN_EXTENSION_DECLARATION`
   (17:55) record principal declarations *made* on 2026-08-14, while
   `U2_CLOSURE_FORM_S_SEALED` (21:24), `CONTINUATION_STATE` (23:43) and every artifact
   through 2026-08-15 11:25 assert the declaration gate **untouched**. Declarations were
   taken and the gate stayed untouched: the gate is not the declaration act-form.

3. **"the gate" of the principal's standing authorization** — `CONTINUATION_STATE.md`,
   THE QUEUE heading, quoting the principal directly: *"proceed through the open work
   until we reach the gate before computing alpha"* (STANDING AUTHORIZATION 2026-08-14).
   This is the principal's own word "gate", in the same artifact that three lines
   earlier writes "the declaration gate untouched". Nothing identifies them; nothing
   separates them. "Before computing alpha" points to the fence structure rather than to
   road 20, and the authorization itself distinguishes "principal acts **and** fences" —
   but that is inference, not a byte. **CANNOT-DETERMINE / INDETERMINATE-AT-BYTES**, and
   it is a second place where the principal's own knowledge could decide what the bytes
   cannot. Flagged rather than resolved.

4. `FINISH B` — the build's fifth §6.8 row, **untested because its instrument is
   barred**. I confirm the bar applies and confirm (§1.5, paths only) that the barred
   `FINISH_B_*` artifacts do contain the term. Untestable under this commission, and
   the build's decision to flag rather than silently omit is correct.

**D4: CONFIRMED-WITH-CORRECTIONS** (COR-E, COR-F). No SAME. The problem is not
dissolved.

---

## 6. D5 — BARS — **REFUTED**

### 6.1 COR-A — road item 20's content asserted against the artifact's own bar declaration

The artifact makes **four** claims about what road item 20 *contains*:

- **:537** — "road item 20 pairs the declaration gate with **the gravity close**"
- **:582** — "road item 20 pairs exactly those two" (the gravity close and a declaration)
- **:589** — "road 20 already treats **\"THE GRAVITY CLOSE consumed\"** as a separate
  conjunct" — presented in double quotation marks, i.e. as quoted road text
- **:653** — "the sealed gravity close (`8c9e7d47…`) **that road 20 pairs it with**"

Against the same artifact's own declarations:

- **:671** — "Its source (`ROAD_REMAINING_FLAT_V001.md`) is **BARRED** … **The road's own
  text was never read.**"
- **:741** — "`BARRED_BYTES_READ = none`"
- **:92-96** — "**none opened** … **Zero barred bytes entered this audit.**"

Tested at bytes over the entire unbarred corpus:

| test | result |
|---|---|
| `gravity\s+close\s+consumed` (case-insensitive, newline-normalized, 18,836 unbarred files) | **0 matches, 0 files** |
| `road 20` \| `item 20`, unbarred corpus | **2 matches, 1 distinct artifact** — `THE_HANDOFF_2026-08-15_V003.md:48` |
| what that sole binding actually says | "The declaration gate (road 20) **+ the signature (21)**: his, unhurried." |
| nearest unbarred text joining the close and "consumed" | `FIVE_D_REREAD_INSTRUMENT_V001_*:` "The gravity close's sealed scoring artifacts, **consumed at the U2-closed strength**" — the 5d re-read instrument's consumption rules, **not road 20** |
| `8c9e7d47` | real: the digest of `THE_GRAVITY_CLOSE_ASSEMBLY_V002_2026-08-15.md`, verified at `THE_GRAVITY_CLOSE_SEALED_2026-08-15.md` — but **no unbarred byte links it to road 20** |

**The only unbarred statement of road 20's content pairs the gate with road item 21,
not with the gravity close.** The quoted string "THE GRAVITY CLOSE consumed" does not
exist anywhere in the unbarred corpus. Its only possible source is a barred artifact.

Two mechanisms are possible and the bytes do not distinguish them: barred content was
read from the file, or barred content was carried in from outside the corpus and used
as evidence. **Which one obtains is INDETERMINATE-AT-BYTES.** What is *not*
indeterminate is that **the artifact asserts the content of a document it declares
itself unable to see**, and that its flag block certifies `BARRED_BYTES_READ = none`
while §6.1/§6.4/§7 rely on barred content. That is an internal contradiction readable
entirely from the artifact's own bytes, and it is the defect the commission's D5 exists
to catch.

**Blast radius, stated exactly.** The corrupted claims are contributory, never sole:
- §6.1's DISTINCT rests independently on the frozen document's **0** "declaration"
  occurrences and on 13 artifacts listing the gate in a clause separate from the three
  fences. **Survives.**
- §6.4's CANNOT-DETERMINE rests independently on the zero co-occurrence result, which I
  re-derived. **Survives** (and CANNOT-DETERMINE is the non-committal grade regardless).
- §7's mention is one item in a list of relations. **Survives.**
- **Q1 does not touch road 20's content at all. ABSENT is untouched.**

So COR-A refutes the artifact's **bar declaration**, not its findings.

### 6.2 The other bars — clean

- **Drafted definition / proposed content / recommendation.** §7 enumerates the *slots* a
  statement of GOV-F's class would fill (referent, admissible inputs, criteria, custody
  and act form, relations) and supplies **content for none of them**. Q5 asked for the
  shape of the gap; describing slots without filling them is reporting. It sits close to
  the line and I record that, but it does not cross it.
- **Should-language.** Four occurrences of `should` in the artifact, **all four inside
  its own disclaimers** ("does not advise whether item 20 should be taken", "no
  should-language is used", "takes no position on whether road item 20 should be
  taken"). Zero directive uses. `ought`, `recommend`, `advis` appear only in the same
  disclaimers. **CLEAN.**
- **`must`.** Two occurrences: one inside a verbatim quote of frozen R2.4, one
  describing what a criteria slot would contain. Neither is directed at the principal.
  **CLEAN.**
- **Fences.** `alpha_computed = false`, `proof_authorized = false`,
  `kappa_record_computed = false` present and correct; no number computed, no magnitude
  approached, no flag flipped, no file edited, no git action. **CLEAN.** The artifact
  neither declares nor moves the gate.

**D5: REFUTED** on COR-A. All other bars clean.

---

## 7. SWEEP CUTOFFS — THIS AUDIT'S OWN PATTERNS

Corpus 18,839 UTF-8 text files, whole-file, newline-normalized, case-insensitive.
Exclusion leak counter: §1.2, **0 on every pattern**. Target self-excluded where noted.

| pattern | matches | files |
|---|---|---|
| `declaration\s+gate` (full corpus, incl. target) | 119 | 37 |
| `declaration\s+gate` (target + sidecars excluded, `.git` excluded) | **46** | **34** |
| `declaration\s+gate` (`.git` logs only) | 2 | 2 |
| `declaration[_-]gate` / `DECLARATION_GATE` / `gate of declaration` | 7 / 5 / 1 | all **target-internal** |
| `declarat\w*\W{1,60}gate` | 57 | 43 |
| `gate\w*\W{1,60}declarat` | 7 | 7 |
| `declar\w*\W{1,80}principal` · `principal\W{1,80}declar\w*` | 2 · 17 | 2 · 15 |
| `declaration sheet` · `the principal's declaration` · `declaration of record` | 2 · 13 · 7 | 1 · 11 · 5 |
| `declarable` · `declaration (is\|means\|=\|:\|shall\|must)` | 32 · 266 | 21 · 203 |
| `act of declaration`\|`declaring act`\|`declaration act` | **0** | **0** |
| `decl\.?\s*gate` \| `dec gate` | **0** | **0** |
| `the principal's gate` | **6** | **6** |
| `the gate\W{0,60}principal` · reverse | **0** · **0** | **0** · **0** |
| `road 20`\|`item 20` (unbarred) | 2 | 2 (1 distinct) |
| `gravity close consumed` (unbarred) | **0** | **0** |
| `G-VERDICT`\|`Gv3` raw · genuine | 19 · **12** | 4 · **2** |
| `RELEASE_CONDITION_F2` · `5a94a1dd` · `anti-fitting gate` | 5 · 2 · 6 | 5 · 2 · 6 |
| `4f6835c2` · `gravity-close-scoring` · `GRV-SCORE` | 2 · 2 · 6 | 2 · 2 · 1 |
| 28 rulings (`DOR_*` 14 + `DECISION_OF_RECORD_*` 14), both prefixes enumerated | **0** | **0** |
| `relay_inbox` (442) + `relay_outbox` (788), both roots | **0** | **0** |
| all plan artifacts (24 basenames) | **0** | **0** |
| git: `-S"declaration gate"` paths · of which deleted | 22 · **0** | — |

**Where this sweep stops.** 4,636 files are binary or non-UTF-8 (`.pyc`, `.npz`,
`.png`, `.zip`, git pack/idx) and were not decoded. Git *packed object contents* beyond
what `--pickaxe` reaches were not enumerated; the pickaxe result is the check that
matters and it returned no deleted carrier. Four barred artifacts are known to contain
the term and were not opened (§2.4).

---

## 8. IMPORT AUDIT

| import | status | load-bearing? | finding survives? |
|---|---|---|---|
| "the declaration gate" | **UNDEFINED — the subject** | the whole commission | **YES.** The finding is the absence; every classification is of speech act, readable regardless of referent. |
| "declaration" as a program act | **UNDEFINED** (0 defining forms corpus-wide) | underlies "scoring is never declaration" | **YES.** Nothing here relies on what declaration means. |
| speech-act taxonomy | **commission-supplied**, not a corpus notion | structures §3 | **YES.** I re-graded from quoted bytes, not from the build's labels; the load-bearing class (definition = 0) is stable under any reasonable re-partition. |
| "constitutive definition" | **commission's term** | the Q1 grade | **YES.** Operationalized at bytes; count is 0 under every reading tested. |
| **road item 20's wording** | source **BARRED**; confirmed (paths only) to contain the term | COR-A; the framing of item 20 | **IMPORT-BLOCK.** My finding is precisely that the build's road-20 content claims have no unbarred support — that finding *requires* the block and is stated because of it, not despite it. |
| **the register row (carried given)** | source **BARRED**; handed over by the registrar | §4.2 | **YES.** Treated as a claim, checked clause by clause against bytes; every factual clause verified; the consequence line marked INDETERMINATE-AT-BYTES. |
| mtime as authorship date | filesystem metadata | the chain order in §3.5 | **PARTIALLY.** Corroborated by in-document `Date:` headers for the two earliest artifacts. The chain's *conclusion* — no occurrence is a definition — is order-independent and survives entirely. |
| git commit metadata as evidence of file history | not a corpus notion | §1.5, §2.2 | **YES, with a stated limit.** It supports a *negative* (no deleted carrier). It cannot show what an unreachable object contained; nothing here needs it to. |

**TWO IMPORT-BLOCKS RECORDED** — road item 20's wording, and the register row. Both are
complete results, not failures. The one place a barred source could change a finding —
whether road 20's own text defines the gate — is named here, and is exactly the place
where the build asserted content it could not have lawfully seen.

---

## 9. CHOICE LEDGER

| # | choice | type | basis |
|---|---|---|---|
| CL-1 | Built my own corpus (18,839 text files) rather than adopting the build's 12,935 | **PREMISE (named)** | An ABSENT verdict re-derived on the same filter is not re-derived. Mine is a strict superset on text; the primary count reproduces exactly on it. |
| CL-2 | Retained `.git` internals and `.seal.sha256` sidecars, which the build dropped | **PREMISE (named)** | They yielded two real occurrences (commit metadata) and the §1.5 negative. Reversible: excluding them returns the build's numbers exactly. |
| CL-3 | Verified all 29 cited file:line programmatically rather than sampling | **PREMISE (method)** | Citation integrity is the most falsifiable surface of a provenance claim. 29/29 pass. |
| CL-4 | Counted a wrapped match as belonging to the line where it **begins** | **PREMISE (named)** | The build's convention; adopting it is what makes its citations checkable. Stated so a reader can re-grade under the other convention. |
| CL-5 | Withdrew my own drafted refutation of the relay counts after reconciling both roots | **JUDGMENT (stated)** | 236+206=442 and 392+396=788 exactly. Recorded in §1.1 rather than deleted, because a suppressed near-miss hides the method. |
| CL-6 | Reached Q1 **ABSENT** independently rather than confirming the build's grade | **JUDGMENT (stated)** | Asked the byte question directly over a wider corpus, 14 new patterns, and the full git history. Reversal path: any single artifact stating what the gate is, what it gates, or its criteria. None exists. |
| CL-7 | Graded COR-A a **refutation of D5** but **not** of D1–D4 | **JUDGMENT (stated)** | The corrupted claims are contributory in §6.1/§6.4/§7 and absent from Q1 entirely; each affected grade has independent byte support that I re-derived. Grading it fatal to the artifact would misstate the blast radius. |
| CL-8 | Declined to determine *how* barred content entered (read vs. carried in) | **JUDGMENT (stated)** | The bytes do not decide, and the internal contradiction is established without deciding. INDETERMINATE-AT-BYTES. |
| CL-9 | Graded the standing authorization's "the gate" **CANNOT-DETERMINE** rather than DISTINCT | **JUDGMENT (stated)** | The reading that separates them ("before computing alpha" = the fence structure) is inference, not a byte. Declining to resolve at bytes what the bytes do not decide. |
| CL-10 | Did not open any barred file, including after `--pickaxe` surfaced four barred paths | **PREMISE (commission)** | Paths only; no blob, diff, or content fetched. Incident logged at §1.2. |

**ZERO OPEN.** All ten are named premises or stated judgments with basis and reversal
path.

**TOY_SEPARATION: clean.** Nothing constructed, modelled, simulated, or stood in for the
record. This artifact is a re-derivation over the existing corpus; every finding rests
on quoted bytes at a cited file:line, and every count is reproducible from the patterns
in §7 against the corpus construction in §1.

---

## 10. GRADES

### Per dimension

| dim | subject | grade |
|---|---|---|
| **D1** | the ABSENT verdict (Q1) — heaviest | **CONFIRMED** |
| **D2** | earliest occurrence and speech-act chain (Q2) | **CONFIRMED-WITH-CORRECTIONS** |
| **D3** | the two release-condition drafts (Q3) | **CONFIRMED** |
| **D4** | the identifications (Q4) | **CONFIRMED-WITH-CORRECTIONS** |
| **D5** | bars | **REFUTED** |

### Overall

**CONFIRMED-WITH-CORRECTIONS.** The default REFUTED verdict is displaced on D1–D4: the
build's factual spine — 46/34, 29/20, 29/29 citations exact, definition count 0, both
drafts' standing, no act on the later draft, no SAME identification — reproduces
independently and survives every net I could cast, including one it never ran that
closes the deleted-artifact hole. It is not displaced on D5.

### My independent Q1 grade

**ABSENT** — over the unbarred corpus, and **only** over the unbarred corpus (COR-B).

---

## 11. CORRECTIONS IN SEVERITY ORDER

**COR-A — the bar declaration is refuted by the artifact's own bytes.**
Deciding file:line: `STAGE8_DECLARATION_GATE_PROVENANCE_O53SR_V001.md:589` —
`road 20 already treats "THE GRAVITY CLOSE consumed" as a separate conjunct.`
Corroborating: `:537`, `:582`, `:653`. Contradicted by `:671` ("The road's own text was
never read"), `:741` (`BARRED_BYTES_READ = none`), `:92-96` ("none opened"). The quoted
string returns **0 matches over 18,836 unbarred files**; the sole unbarred road-20
binding, `THE_HANDOFF_2026-08-15_V003.md:48`, pairs the gate with **road 21**, not the
gravity close. Findings survive (§6.1); the bar declaration does not.

**COR-B — the ABSENT headline overstates its scope.**
Deciding file:line: `…O53SR_V001.md:30-31` — "No ruling, spec, plan, **register**,
relay, or instrument **anywhere** states what the declaration gate **is**". The register
is barred and unread, and `git log --pickaxe` path listing shows **four barred
artifacts contain the term**. The artifact's own §8 (`:671`) states the limit
correctly; §0 and §3 do not carry it. ABSENT holds over the unbarred corpus.

**COR-C — a corroborating sweep sentence that does not reproduce.**
Deciding file:line: `…O53SR_V001.md:326-327` — "A sweep for `gravity-close-scoring` or
`GRV-SCORE` returns only the scoring artifact itself and this handoff." At bytes
`gravity-close-scoring` → handoff only (the scoring artifact does not contain it);
`GRV-SCORE` → scoring artifact only. A looser net additionally returns
`FIVE_C_PRINCIPAL_ACTS_STAGING_V001.md` and `STAGE8_CARRIER_TRIAGE_S9AD_V001.md`, both
opened, neither carrying the brief. **The off-disk-brief conclusion survives and
strengthens.**

**COR-D — P20 breaks the table's declared counting convention.**
Deciding file:line: `…O53SR_V001.md:152` — P20 reported `1 | 1` where the raw,
pre-collapse figure the table declares at `:129` is **2 / 2** (both mirrors of
`THE_HANDOFF_2026-08-15_V003.md`). One distinct occurrence; the substantive claim is
correct.

**COR-E — P14 reports a substring false positive as evidence.**
Deciding file:line: `…O53SR_V001.md:146` — `G-VERDICT | Gv3 → 19 | 4`, glossed at
`:583-585` as "all plan documents". 7 matches in 2 files are matches inside
"clearin**g-verdict** gate" in `1091_DONE.md`, which is a relay DONE report, not a plan.
Genuine: **12 matches, 2 files, 1 distinct artifact**. The zero-co-occurrence finding
re-derives independently and **strengthens**.

**COR-F — the Q4 candidate set is incomplete by three, on the dimension where a missed
SAME is most consequential.**
Deciding file:line: `…O53SR_V001.md:631-633` ("Net: no SAME verdict"). Missed:
(i) **"the principal's gate"**, 6/6, `THE_HANDOFF_2026-08-15_V002.md` — graded
**DISTINCT** (that gate was taken; the declaration gate stayed untouched in the same
sealed file); (ii) **the principal's declaration act-form** — graded **DISTINCT** at
timestamps (`ACT2_CARRIER_ADMISSION_DECLARATION_2026-08-14.md`, 17:18, records a
declaration *made*, while the gate is asserted untouched at 21:24, 23:43 and through
2026-08-15); (iii) **"the gate" of the standing authorization**,
`CONTINUATION_STATE.md` THE QUEUE heading, the principal's own words — graded
**CANNOT-DETERMINE / INDETERMINATE-AT-BYTES**, a second place where the principal's own
knowledge could decide what the bytes cannot. **Net unchanged: no SAME. The problem is
not dissolved.**

---

## 12. FLAG BLOCK

```
DECLARATION            = not-made (this audit declares nothing; the declaration
                         gate is the principal's, separately)
GOV_F                  = untouched (no flag flipped; sealed-spec flags remain the
                         Gate-6 evaluator's)
DECLARATION_GATE       = UNTOUCHED — and, per this audit independently, UNDEFINED
                         AT BYTES ACROSS THE UNBARRED CORPUS

OVERALL                = CONFIRMED-WITH-CORRECTIONS
D1_ABSENT_VERDICT      = CONFIRMED
D2_EARLIEST_AND_CHAIN  = CONFIRMED-WITH-CORRECTIONS (COR-C, COR-D)
D3_TWO_DRAFTS          = CONFIRMED
D4_IDENTIFICATIONS     = CONFIRMED-WITH-CORRECTIONS (COR-E, COR-F)
D5_BARS                = REFUTED (COR-A)

AUDIT_Q1_GRADE         = ABSENT (independent; unbarred corpus only)
Q1_COUNTS_REDERIVED    = 46 raw / 34 files ; 29 distinct / 20 artifacts — EXACT
CITATIONS_VERIFIED     = 29 / 29 at bytes, 0 mis-cited, 5 wrapped and correctly anchored
MIRRORS_VERIFIED       = 7 digest pairs, all IDENTICAL
GIT_HISTORY_CHECK      = 22 paths carry the term; 0 deleted; 14 deleted paths, none
                         a carrier — NO REMOVED CARRIER EVER EXISTED
NEW_PATTERNS_RUN       = 14; none surfaces a definition
BARRED_PATHS_SURFACED  = 4 (paths only, via git metadata; no content read)
BARRED_BYTES_READ      = none
EXCLUSION_LEAKS        = 0 on every pattern (39 files removed by name, none opened)
SIDECAR_PROBE          = both conventions probed on every artifact reported
CORPUS                 = 18,839 UTF-8 text files (23,514 raw → 23,475 after
                         exclusions → 18,839 decodable); superset of the build's 12,935
CHOICE_LEDGER          = 10 entries, all PREMISE(named)/JUDGMENT(stated), zero OPEN
IMPORT_AUDIT           = 8 imports; 2 IMPORT-BLOCKS (road item 20's wording; the
                         register row). All findings survive; limits named.
TOY_SEPARATION         = clean

alpha_computed         = false
proof_authorized       = false
kappa_record_computed  = false
NUMERIC_EVALUATION     = false ; CAS = not invoked ; MEASURED_CONSTANT_COMPARISON = none
CHAIN_INVOKED          = false ; MEMBER_BOUND = false ; MACHINERY_APPEAL = none
FILES_WRITTEN          = 1 (this artifact) + 2 seal sidecars
FILES_EDITED           = 0 ; GIT_WRITE_ACTION = none (read-only log queries only)
SWEEP_CUTOFF           = 2026-08-16
```

---

## 13. CUSTODY

Audit lane of commission O53SR, 2026-08-16, default-refute, adversarial by mandate.
Every count is reproducible from the patterns in §7 against the corpus construction in
§1. Every grade is shown with the bytes that justify it at a cited file:line, and where
the bytes do not decide this artifact says INDETERMINATE-AT-BYTES or CANNOT-DETERMINE
rather than choosing. One refutation of my own was drafted and withdrawn on
re-derivation; it is recorded at §1.1 rather than removed.

This artifact neither drafts nor proposes a definition for the declaration gate, quotes
no barred file, and takes no position on whether road item 20 should be taken. The
declaration gate remains untouched and the principal's.
