# STAGE 8 — FENCE PROVENANCE AUDIT (O50SR) — DEFAULT-REFUTE AUDIT

**Lane:** DEFAULT-REFUTE AUDIT (paired check). **Default verdict:** REFUTED. **Mode:** RE-DERIVE AT
BYTES. **Date:** 2026-08-16.
**Subject artifact:** `/Users/bgm/MB Work/alpha-program-archive/workspace/STAGE8_FENCE_PROVENANCE_O50SR_V001.md`
**Subject sha256 (recomputed here):** `e51dd61f9df85b5e590e4d38fe72fc2f0dfb258f0a852d59292e10cf3a4563cd` — matches the build's reported value.

**Gates:** `alpha_computed = false` · `proof_authorized = false` · `kappa_record_computed = false`.
No numeric value of any coupling, scale, root, eigenvalue, norm or constant was computed or
approached anywhere in this artifact. The only numbers here are file counts, line numbers, dates and
hashes.

**Bars observed:** no authoring, no advocacy, no adoption. This artifact does not say whether any
fence clause *should* stand. `INDETERMINATE-AT-BYTES` wherever the bytes do not decide.

---

## 0. HEADLINE

**OVERALL: REFUTED.**

The build's three headline claims are each false at bytes:

1. *"All seven earliest instances are type (b). None is type (a). Zero ratified rulings originate any
   clause."* — **REFUTED.** Three clauses (C1, C3, C4) originate in **ratified rulings** dated
   2026-07-31 and 2026-08-01, eleven and twelve days before the build's claimed origin.
2. *"ADOPTED-BY-RULING 0."* — **REFUTED**, by the same rulings.
3. *"STANDARD-MET 0 … the scale met the standard and is not a fence clause; no fence clause met the
   standard … the two sets are disjoint at bytes."* — **REFUTED.** C3 (KK/radion) carries, at
   ruling level, a proof of exactly the exemplar's shape, with a TYPE-R refutation cited.

The single deciding fact behind all three: the build's flag **F-2** asserts that
"**DOR_001 through DOR_015 do not exist as files** in either supervision root under any casing or
naming variant (searched)." **They exist.** Fourteen of them sit in the *permitted* directory
`/Users/bgm/MB Work/alpha-program-archive/supervision/` under the naming convention
`DECISION_OF_RECORD_NNN_…_V001.md`, all sealed, all verifying OK. The build swept 14 of the 28
ruling files present and asserted universals over the corpus of rulings from that 50% sample.

---

## 1. CHOICE LEDGER

| # | Choice | Alternatives | Why taken | What would change if reversed |
|---|---|---|---|---|
| **AL-1** | **Treated `DECISION_OF_RECORD_NNN_*.md` in `…/alpha-program-archive/supervision/` as within the brief's "all `DOR_*` rulings … there are roughly twenty and they are central here."** | Read the literal glob `DOR_*` only (14 files), as the build did. | (i) The brief says "roughly twenty"; the literal glob yields 14, the ruling *series* yields 18 distinct numbers (003–011, 013–020) across 28 files. (ii) The surviving `DOR_*` files cite the earlier ones in the same idiom — DOR_017:14–17 cites "DoR-016", "the DoR-009 every-prefix traces", "the five DoR-008 restriction obligations" — so they are one instrument, renamed at 016. (iii) The REGISTER BAR's barred list (REGISTER, TRACKER, THE_PLAN, ROAD_REMAINING, THE_HANDOFF, OBSERVATIONS_REGISTER, DECISION_SHEET) does not reach them: `DECISION_OF_RECORD` ≠ `DECISION_SHEET`. | **This is the audit's load-bearing choice and I say so.** Under the narrow reading, COR-A/COR-B/COR-C/COR-E survive as *documented existence* findings (the files are there and sealed; F-2's universal negative is false as stated) but their *content* could not be cited, and D1/D2/D5 would degrade to INDETERMINATE-AT-BYTES rather than REFUTED. Every finding that depends on opening these files is marked **[AL-1]** below. |
| **AL-2** | **Read only line 29 (row I-7) of `INSTINCTS_AND_TESTS_LEDGER_V001.md`.** | Read rows I-1 and I-3 too, as the build did (it cites `:27` and `:31`). | The brief permits that file "**for the method-correction row only**." | I therefore cannot independently re-verify the build's I-1 quotation. I report the scope excess as a finding (COR-F) rather than repeating it. C4's Q2 grade and the Q5 exemplar are graded **INDETERMINATE-AT-BYTES-TO-THIS-LANE** as a result, not confirmed. |
| **AL-3** | **Chronology = filesystem mtime, cross-checked against in-filename dates and relay sequence numbers.** | In-file dates only. | Same as the build's CL-1; mtimes agree with filename dates on all 28 rulings and with paste numbering. | The decisive corrections (COR-A/B) do **not** depend on mtime: DoR-003 carries `DATE: 2026-07-31` in its own line 3, DoR-007 carries `2026-08-01` in its line 3, and both are in their filenames. |
| **AL-4** | **A "clause" = a distinct excluded class**, C1–C7 as the build numbered them. | Renumber. | Keeps the audit commensurable with the subject. | No grade turns on it. |
| **AL-5** | **Graded the build's claims, not the fence.** Where the build's *answer* survives but its *basis* is wrong, the grade is CONFIRMED-WITH-CORRECTIONS, not CONFIRMED. | Grade only the answers. | A universal negative asserted over half the result set is not established even when it happens to hold. | Several dimensions would rise a grade. |

---

## 2. SWEEP CUTOFFS

**Corpus enumerated independently of the build.** Roots:
`/Users/bgm/MB Work/alpha-program-archive/{workspace,relay_inbox,relay_outbox}` +
`/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003`
+ the ruling files under `…/alpha-program-archive/supervision/` + row I-7 of
`…/alpha_supervision/INSTINCTS_AND_TESTS_LEDGER_V001.md`.

Files enumerated: **15760**. After exclusions: **15696**. Text subset swept: **10848**
(`.md .json .txt .jsonl .py .sh`); markdown subset: **4878**. (The build reported 6626/6595; the
difference is enumeration scope, not exclusion behaviour — the build appears not to have enumerated
seal sidecars and vendored `.py`. No finding turns on it.)

**Exclusion globs (array) with per-pattern removal count and leak counter:**

| # | Pattern | Files removed | Leaked into a sweep |
|---|---|---|---|
| 1 | `*REGISTER*` | 53 | **0** |
| 2 | `*TRACKER*` | 0 | **0** |
| 3 | `THE_PLAN*` | 8 | **0** |
| 4 | `ROAD_REMAINING*` | 0 | **0** |
| 5 | `THE_HANDOFF*` | 0 | **0** |
| 6 | `OBSERVATIONS_REGISTER*` | 0 | **0** |
| 7 | `*DECISION_SHEET*` | 0 | **0** |
| 8 | `STAGE8_FENCE_PROVENANCE_O50SR_AUDIT_V001*` (self-exclude) | 0 | **0** |
| 9 | `STAGE8_FENCE_PROVENANCE_O50SR_V001*` (subject-exclude) | 3 | **0** |

**Leak counter: 0 across all patterns.** `QUESTIONS_SETTLED_REGISTER_V001.md` was caught by pattern 1
and never opened. Self-exclusion armed before this artifact existed.

**SEALS.** `shasum -a 256 -c` run from each artifact's own directory; both sidecar forms
(`<stem>.md.seal.sha256`, `<stem>.seal.sha256`) checked before calling anything unsealed.
- **All 28 ruling files** in `…/alpha-program-archive/supervision/` (14 `DOR_*` + 14
  `DECISION_OF_RECORD_0*`): **28/28 OK**, 0 missing sidecars.
- `INSTINCTS_AND_TESTS_LEDGER_V001.md`: **OK**.
- Subject artifact `STAGE8_FENCE_PROVENANCE_O50SR_V001.md`: sha256 recomputed, matches the build's
  reported value; both sidecars present and verifying.

---
