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

## 3. THE DECIDING FACT — F-2 IS FALSE AT BYTES

The build's flag F-2 (`STAGE8_FENCE_PROVENANCE_O50SR_V001.md:668-669`) states:

> "**DOR_001 through DOR_015 do not exist as files** in either supervision root under any casing or
> naming variant (searched)."

They exist. Fourteen files, in **both** supervision roots, all sealed, all verifying OK from their own
directory. In the **permitted** directory `/Users/bgm/MB Work/alpha-program-archive/supervision/`:

```text
DECISION_OF_RECORD_003_GEOMETRIC_ROUTE_REFRAMED_2026-07-31_V001.md
DECISION_OF_RECORD_004_EVALUATION_FENCE_LIFTED_FOR_ONE_ITEM_2026-08-01_V001.md
DECISION_OF_RECORD_005_P7_CONSUMES_THE_ASSEMBLED_SPACE_2026-08-01_V001.md
DECISION_OF_RECORD_006_TYPE_P_ADOPTED_LAZY_MIGRATION_2026-08-01_V001.md
DECISION_OF_RECORD_007_SMOOTH_FORK_DERIVE_THE_LIMIT_2026-08-01_V001.md
DECISION_OF_RECORD_008_FIELD_CTP_ADOPTION_RATIFIED_WITH_FALSIFIER_2026-08-01_V001.md
DECISION_OF_RECORD_009_THE_TRANSITION_LAW_RATIFIED_E_POST_2026-08-02_V001.md
DECISION_OF_RECORD_010_STRUCTURAL_P_DEPENDENCE_AUTHORIZED_2026-08-02_V001.md
DECISION_OF_RECORD_011_TASK4_TRANSPORT_CONSTRUCTION_AUTHORIZED_2026-08-01_V001.md
DECISION_OF_RECORD_013_GEN_OMEGA_RATIFIED_FAMILY_LEVEL_2026-08-02_V001.md
DECISION_OF_RECORD_014_SOURCE_GERM_PHYS_RATIFIED_2026-08-02_V001.md
DECISION_OF_RECORD_014_AMENDMENT_1_CB_DERIVED_PAIRING_2026-08-02_V001.md
DECISION_OF_RECORD_014_AMENDMENT_2_EVEN_PAIRING_NORMALIZATION_2026-08-02_V001.md
DECISION_OF_RECORD_015_FIELD_SIGNATURE_PHYS_RATIFIED_2026-08-02_V001.md
```

**Total ruling files present: 28** (14 `DECISION_OF_RECORD_0*` + 14 `DOR_0*`), **28/28 seals OK**,
0 missing sidecars. Distinct DoR numbers: **003–011, 013–020 = 18** — which is what the brief's
"roughly twenty" describes. The genuine gap is **001, 002 and 012 only**, not 001–015.

**The build did not need to widen its permitted set to find them.** The exact filename is printed
inside the *corpus* — `STAGE8_FIELD_CTP_CARRIER_AND_C0_JOIN_INSTANTIATION_ATTEMPT_V001.md:249`:

> "`DECISION_OF_RECORD_007_SMOOTH_FORK_DERIVE_THE_LIMIT_2026-08-01_V001.md:9-24`
> requires the alpha-facing smooth subset to arise from a derived
> discrete-to-continuum equivalence theorem and takes adoption of `(M,g)` off the
> table. It permits discrete-sufficient algebraic work to proceed."

A search for the string `DoR-007`/`Decision of Record 007` inside the permitted corpus returns 281
raw hits across 54 distinct basenames. The naming convention was recoverable from the corpus alone.

Every universal negative in the build's Q1, Q2 and Q4(a) was asserted over 14 of the 28 ruling files.

---

## 4. D1 — THE CENSUS (Q1) — **REFUTED**

### 4.1 Three clauses originate in ratified rulings

**C1 — RECORD-NATIVE / DERIVED-OBJECTS-ONLY.** Earliest instance is **type (a)**, not (b):
`DECISION_OF_RECORD_003_GEOMETRIC_ROUTE_REFRAMED_2026-07-31_V001.md`, dated in its own line 3
(`DATE: 2026-07-31. PRINCIPAL DECISION. Applies to every relay on the geometric route.`) and carrying
`decision_status = STANDING` at :5. At **:49-50**, quoted whole:

> "\*\*\* THE GEOMETRIC ROUTE IS REBUILT FROM **DERIVED OBJECTS ONLY.** NO IMPORTED ANSATZ. NO POSTULATED
> PARENT ACTION. NO ASSUMED SPATIAL READING OF THE PROJECTIVE DIRECTION. \*\*\*"

**Twelve days before RELAY_PASTE_1101.** The adverse clause the finding must carry is in the same
ruling at **:52-57** — "**WHAT REMAINS AVAILABLE — derived, and untouched by this decision:** … the
unique counting metric — derived; internal normalization FULLY PINNED" — i.e. the ruling bars
*imported* objects while expressly preserving a *derived* metric. It is a provenance requirement, not
a class bar.

**C3 — NO KK / NO RADION.** Earliest instance is **type (a)**: the same ruling, **:24-26**:

> "\*\*\* THE KALUZA-KLEIN FRAMING IS AN IMPORT. THE CORPUS DERIVES A COMPACT `U(1)` COMPARISON GROUP AND
> PROJECTIVE / FUBINI-STUDY RECORD GEOMETRY. IT DOES **NOT** DERIVE THAT THE PROJECTIVE DIRECTION IS A
> PHYSICAL SPACETIME DIMENSION WITH A LENGTH RADIUS. `S^1` IS NOT ESTABLISHED BY `U(1)` ALONE. \*\*\*"

and the radion half at **:76-77**, quoted whole with its adverse clause:

> "\*\*\* THE MASSLESS-RADION IDENTIFICATION (Q-130) -- THE PHYSICS WAS CORRECT **GIVEN THE FRAMING**;
>     THE FRAMING IS NOT DERIVED. RETAINED AS CONDITIONAL, NOT AS ESTABLISHED. \*\*\*"

**C4 — NO METRIC.** Earliest instance is **type (a)**:
`DECISION_OF_RECORD_007_SMOOTH_FORK_DERIVE_THE_LIMIT_2026-08-01_V001.md:12-13`, quoted whole:

> "ADOPTION OF (M,g) FOR THIS SUBSET IS OFF THE TABLE. The ambient metric carries an Einstein-Hilbert
> term; adopting it at the alpha-facing chain would adopt the gravity the program claims to derive."

**Eleven days before RELAY_PASTE_1101.** Scope is on the face of the sentence: *for this subset*, *at
the alpha-facing chain* — and the same ruling's title and line 8-10 supply the discharge route: "THE
SMOOTH FORK: **DERIVE THE LIMIT** … is to be met by a DERIVED DISCRETE-TO-CONTINUUM EQUIVALENCE
THEOREM — the stitching rule as a theorem over refinements."

### 4.2 Three more clauses have earlier lane instances than the build reports

**C7 — CLASSICAL READING UNLAWFUL.** Earliest instance is
`RELAY_PASTE_820_COMPLETION_AUDIT_DARIO_V001.md:7` (mtime 2026-08-09 16:23) — **three days before**
the build's claim of 2026-08-12 16:37 — and in a materially *different, qualified* form. Quoted whole
from the end of that line:

> "A demand that types RECORD-NATIVE and is met by the proved colimit stock is SCORED MET, not open —
> the classical detour ("pretend a classical continuum, translate back") **is not a lawful reading
> unless a sealed sentence explicitly demands it**."

The same paste's GATES line, **:15**: "SIZING ONLY — nothing constructed, no completion attempted, the
T1/T5 fences untouched; **no smooth import**; no EM identification."

The build examined the *output* of that relay (`STAGE8_AXN_COMPLETION_AUDIT_DARIO_V001.md:292`) and
excluded it as "a finding reached by reading". It did not examine the *instruction* that produced it.
The lane's own later statement makes the chain explicit —
`STAGE8_AXN_BUILD_DIRECTION_RELATION_DARIO_V001.md:36-37`: "That is the same record-native-versus-
classical axis I found decisive **at 820** — where I established that the completion's demands type
record-native and that classical readings are unlawful **absent a sealed sentence**."

**C5 — NO VARIATIONAL.** Earliest instance is `RELAY_PASTE_1101`, **16:37**, not `RELAY_PASTE_1102` at
17:11. The variational bar is in the founding paste twice — **:12**: "even the NOTATION OF VARIATION
('L + eps\*delta L') SMUGGLES A LINEARITY THE RECORD NEVER LICENSED. THEREFORE the DEFAULT for every
continuum-named object AND every continuum notation is BARRED" — and **:18**: "do NOT let
variational/additive/smooth NOTATION smuggle linearity the record does not license." Type is
unchanged; the date and locator are wrong by 34 minutes and one file.

**C2 / C4 in lane-instruction form.** "no smooth import (S26)" is a **standing GATES line in relay
pastes from 2026-08-09 10:05** (`RELAY_PASTE_791_CURRENT_DENSITY_HUNT_CODEX2_V001.md:15`), and "no
metric adopted" from 2026-08-09 10:55 (`RELAY_PASTE_795_COFRAME_HALF_DARIO_V001.md:15`) — both three
days before 1101, both citing a **decline-register row S26** whose home is a register barred to both
lanes. `793_DONE.md:56` names it: "Preserved decline-register rows S08 and S26."

### 4.3 What the build got right on D1

- The label `RECORD-NATIVE FENCE` originates at `RELAY_PASTE_1101:6`, 2026-08-12 16:37, and every
  instance is dated 2026-08-12. **CONFIRMED** (8 distinct basenames; the build's raw count of 11 vs
  my 13 is an enumeration-scope difference, not a finding).
- The slash-compound `continuum/KK/radion/variational` exists in exactly **3** files — 1105:6,
  1105_ACK:67, 1106:13. **CONFIRMED at bytes.**
- **C6 — NO IMPOSED DECOMPOSITION**: exactly **2** carriers corpus-wide (`RELAY_PASTE_1105:6` and
  `1105_ACK:67`), **0** across all **28** rulings. Earliest 2026-08-12 17:42, type (b).
  **CONFIRMED, and confirmed over the full ruling set.**
- The 2026-08-02 "no continuum limit" hit at
  `STAGE8_TASK4A_DOOR_D_FALSIFIER_CARRIER_AND_CHECK_DIAGNOSIS_V001.md:299` is a provenance report, not
  a clause. **CONFIRMED** — correctly excluded.
- F-6: the exact phrase "KK reduction" has 5 carriers, all 2026-08-15 or later. **CONFIRMED at bytes.**

### 4.4 Corrected Q1 census

| Clause | Earliest instance (corrected) | Date | Type | Build said |
|---|---|---|---|---|
| C1 record-native / derived-only | `DECISION_OF_RECORD_003_…:49-50` | **2026-07-31** | **(a) ratified ruling** | (b), 2026-08-12 |
| C2 no continuum limit | `RELAY_PASTE_791:15` "no smooth import (S26)" (smooth half); `RELAY_PASTE_1101:7` (continuum-machinery half) | **2026-08-09** / 2026-08-12 | (b) lane-scoping | (b), 2026-08-12 |
| C3 no KK / radion | `DECISION_OF_RECORD_003_…:24-26, :76-77` | **2026-07-31** | **(a) ratified ruling** | (b), 2026-08-12 |
| C4 no metric | `DECISION_OF_RECORD_007_…:12-13` | **2026-08-01** | **(a) ratified ruling** | (b), 2026-08-12 |
| C5 no variational | `RELAY_PASTE_1101:12, :18` | 2026-08-12 **16:37** | (b) lane-scoping | (b), 1102 @ 17:11 |
| C6 no imposed decomposition | `RELAY_PASTE_1105:6` | 2026-08-12 17:42 | (b) lane-scoping | **same — confirmed** |
| C7 classical reading unlawful | `RELAY_PASTE_820:7` | **2026-08-09 16:23** | (b) lane-scoping, **qualified form** | (b), 2026-08-12 |

**CORRECTED Q1 TALLY — TYPE (a) RATIFIED RULING 3 · TYPE (b) LANE-SCOPING 4 · TYPE (c) 0.**

The build's headline — "**All seven earliest instances are type (b). None is type (a). Zero ratified
rulings originate any clause**" (`:254-255`) — is **REFUTED**. Six of the seven dated locators are
wrong; three of the seven types are wrong.

**D1 GRADE: REFUTED.**

---

## 5. D2 — STATED GROUNDS AND THE UNIVERSAL NEGATIVES (Q2) — **REFUTED**

The brief directed me to test every universal negative by running sweeps the build did not. Three of
the build's universals fail; one holds.

### 5.1 "ADOPTED-BY-RULING is zero" — FALSE

The build's basis (`:344-347`): "all 14 `DOR_*` rulings read in full or grepped for every clause term
… **zero hits for every term except 'continuum'**." Re-run over all **28** ruling files:

| Term | Build's basis (14 files) | Full ruling set (28 files) | Where |
|---|---|---|---|
| `KK` / `Kaluza` | 0 | **2 files** | DoR-003 (`KK` ×2, `Kaluza` ×1) |
| `radion` | 0 | **1 file** | DoR-003:76 |
| `metric` | 1 file | **4 files** | DoR-003 (×5), DoR-007, DoR-015, DOR_019 |
| `continuum` | 3 files | **5 files** | DoR-007 (×3), DoR-008, DOR_016, DOR_020, DOR_020_A1 |
| `variation` | 0 | **1 file** | DoR-010 (×3) |
| `Hessian` | 1 file | **2 files** | DoR-011, DOR_017 |
| `smooth` | 1 file | **2 files** | DoR-007, + 1 |
| `variational` / `extremal` / `extremiz` / `action principle` / `least action` / `Euler-Lagrange` / `saddle` | 0 | **0** | — |
| `record-native` / `no-import` / `imposed decomposition` / `classical reading` / `unlawful` | 0 | **0** | — |

So the build's sentence at `:108-111` — "No `DOR_*` ruling contains the phrase … `KK`, `radion`, or
`variational` in any form. Verified across all 14 rulings — hits: … `KK` **0**, `radion` **0**" — is
false over the ruling series. `KK` and `radion` are in DoR-003, on the **barring** side, and they are
the origin of C3.

### 5.2 The universal that HOLDS — C6

`imposed decomposition`: **2 carriers corpus-wide, 0 across all 28 rulings.** Independently re-run.
The build's **NEVER-JUSTIFIED** grade for C6 is **CONFIRMED**, and now confirmed over the full ruling
set rather than half of it. This is the one clause with no ground anywhere at bytes.

### 5.3 C3's ground is not a lane paste — it is a sealed corpus artifact

The build graded C3 **LANE-SCOPING** with the ground "circularity: 'imported KK gravity → circular'"
from `RELAY_PASTE_1101:9`. The actual ground is older and is in the permitted **corpus**, not in
supervision at all: `STAGE8_KK_FRAMING_DERIVED_OR_IMPORTED_AUDIT_V001.md` (workspace and cleanroom,
mtime 2026-07-31 19:55, **seal OK**), which DoR-003:14-15 cites by name and hash `5c08253c…`. Quoted
whole from **:7-9**:

> "The KK framing is **imported/adopted, not derived**. The corpus derives a compact `U(1)` comparison group
> and a projective/Fubini–Study record geometry, but it does not derive that this internal state space is a
> spatial fifth dimension with a physical length radius."

and **:35-37**, quoted whole with its own qualifier:

> "A single-circle ansatz cannot
> supply an independent squashing mode; this is a **TYPE-R refutation of the granted ansatz as a complete
> saddle**, not merely missing physics."

and **:41-44**, carrying the adverse clause:

> "The parent construction introduced `S5=(1/2κ5²)∫√−G R5` as a standard KK choice, explicitly marked
> imported/choice (`STAGE8_PARENT_KK_ACTION_ELL_P_DEFINITION_AND_REDUCTION_V001.md`). No corpus derivation of
> 5D Einstein–Hilbert gravity from record structure was found. Thus the geometric route assumes gravitational
> dynamics at its parent level while claiming gravity emergence downstream."

**This is a derivation, not a scoping instruction.** C3's Q2 grade is **DERIVED**, and the derivation
is reachable without opening any supervision file at all.

### 5.4 C4's Q2 grade — the build's basis was outside its permission

The build graded C4 **DERIVED** on `INSTINCTS_AND_TESTS_LEDGER_V001.md:27` (row I-1). The brief
permits that ledger "**for the method-correction row only**". Row I-1 is not the method-correction
row. Under AL-2 I did not open it, so I cannot confirm or refute the quotation; I re-grade C4 on
material inside my permitted set: `DECISION_OF_RECORD_007_…:12-13` is a **ratified ruling** that takes
`(M,g)` off the table for a named subset, with a stated ground (circularity) and a named discharge
route. C4's Q2 grade is therefore **ADOPTED-BY-RULING (scoped)**.

### 5.5 The build's one-grounds-paragraph claim

`:268-270`: "There is exactly **one** passage anywhere in the corpus that argues *why* these classes
are excluded." **REFUTED.** At least three more exist, all predating it:
`STAGE8_KK_FRAMING_DERIVED_OR_IMPORTED_AUDIT_V001.md` in full (2026-07-31); DoR-003 §1–§2 and §6
(2026-07-31); DoR-007:12-13 (2026-08-01). The build's quotation of `RELAY_PASTE_1101:12` is itself
**accurate at bytes** — I re-read the line and it matches word for word, including "the barred default
is PROVEN, not a caution" and the closing burden-shift. What is wrong is the word "exactly one".

### 5.6 Corrected Q2 tally

| Clause | Build's grade | Corrected grade | Deciding bytes |
|---|---|---|---|
| C1 | LANE-SCOPING | **ADOPTED-BY-RULING** (scoped: "every relay on the geometric route") | `DECISION_OF_RECORD_003_…:3, :49-50` |
| C2 | LANE-SCOPING | **LANE-SCOPING** (unchanged; ruling-level treatment runs the *other* way — DoR-007 "DERIVE THE LIMIT", DOR_020 adopts a continuum theory) | `DECISION_OF_RECORD_007_…:1, :8-10`; `DOR_020_…:7` |
| C3 | LANE-SCOPING | **DERIVED** | `STAGE8_KK_FRAMING_DERIVED_OR_IMPORTED_AUDIT_V001.md:7-9, :35-37` |
| C4 | DERIVED (via I-1) | **ADOPTED-BY-RULING** (scoped) | `DECISION_OF_RECORD_007_…:12-13` |
| C5 | LANE-SCOPING | **LANE-SCOPING** (unchanged; ground reaches notation only — confirmed) | `RELAY_PASTE_1101:12` |
| C6 | NEVER-JUSTIFIED | **NEVER-JUSTIFIED** (confirmed over 28 rulings) | 2 carriers; 0/28 |
| C7 | LANE-SCOPING | **LANE-SCOPING** (unchanged) | `RELAY_PASTE_820:7`; `RELAY_PASTE_1101:12` |

**CORRECTED Q2 TALLY — DERIVED 1 (C3) · ADOPTED-BY-RULING 2 (C1, C4) · LANE-SCOPING 3 (C2, C5, C7) ·
NEVER-JUSTIFIED 1 (C6).** Build reported 1 / **0** / 5 / 1.

**D2 GRADE: REFUTED.**

---

## 6. D3 — THE METHOD-CORRECTION TEST (Q3) — **CONFIRMED-WITH-CORRECTIONS**

### 6.1 Is the correction quoted whole from its own source, not paraphrased? — YES

I re-read `/Users/bgm/MB Work/alpha_supervision/INSTINCTS_AND_TESTS_LEDGER_V001.md` **line 29** (row
I-7), seal **OK**. The build's §4.1 reproduces the statement cell and the attribution cell **word for
word**, including the escape-stripped `|n|` pipes, including "Barring faithfulness blindly … is the
same unexamined error as accepting it blindly", and including "Faithfulness is NOT proven machinery —
its status is open." **No paraphrase. CONFIRMED at bytes.**

One scope note, not a fabrication: the build declared it was quoting "statement cell" and "attribution
cell", and it did. It did not carry the row's later cells, one of which is the row's own worked
example of the standard being met — "**ran CLEAN — neither assumed nor barred**; two independent
cross-lineage fenced lanes". That cell is favourable to the build's own framing, so its omission is
not adverse-clause suppression.

### 6.2 The correction has an earlier, RATIFIED statement the build missed

`DECISION_OF_RECORD_004_EVALUATION_FENCE_LIFTED_FOR_ONE_ITEM_2026-08-01_V001.md:103-106`, §7 **STANDING
RULE GOING FORWARD**, quoted whole:

> "\*\*\* A FENCE THAT BLOCKS A **FULLY SPECIFIED, PRE-REGISTERED, MANDATED, PRE-ROOT** COMPUTATION IS A
> REVIEWER DEFECT AND MUST BE SURFACED TO THE PRINCIPAL AS A DECISION — **NOT CARRIED SILENTLY INTO THE
> NEXT RELAY.** THE FENCE'S PURPOSE IS TO BAR **DISTORTING THE ALGEBRA TO REACH A KNOWN ANSWER**, WHICH
> IS THE PRINCIPAL'S OWN STATED LINE. IT IS NOT TO BAR EVALUATING A SPECIFIED STRUCTURE. \*\*\*"

and the same ruling's diagnosis at **:28-30**:

> "\*\*\* THE LANE WAS RIGHT TO STOP. THE FENCE
> AND THE MANDATE CONFLICTED, AND THE REVIEWER WROTE THE FENCE. `TYPE-C` MEANT CONSTRAINT-BLOCKED **BY
> THE RELAY**, NOT BY PHYSICS. \*\*\*"

This is the method correction, at ruling level, **2026-08-01 — twelve days before I-7 (2026-08-13)**.
The same doctrine appears in disposal form at DoR-003:80-81:

> "\*\*\* NONE OF THIS IS DELETED OR RETRACTED. IT IS RE-TYPED AS CONDITIONAL ON AN UNDERIVED FRAMING. IF
> THE FRAMING IS LATER DERIVED, IT ALL RETURNS INTACT. \*\*\*"

The build treated I-7 as the sole and originating source ("the principal's correction", `:356`). At
bytes the correction is a **standing ruling of 2026-08-01 restated in the ledger on 2026-08-13**.

### 6.3 Attacking the grades in both directions

**Toward VIOLATES (attacks on the build's four COMPLIES):**
- **C4**: the build's COMPLIES rests partly on "status was independently determined (I-1, proven
  pre-metric)" — outside its permission. **The grade nevertheless survives on ruling bytes**:
  DoR-007's own sentence is scoped ("FOR THIS SUBSET", "at the alpha-facing chain"), grounded
  (circularity), and carries a discharge route (the derived equivalence theorem, :9-10). COMPLIES
  stands on a corrected basis.
- **C1/C2/C3**: I could not break these. The founding paste's verbs are exactly as the build reports,
  and C3 is now *stronger*, because status was determined by a TYPE-R refutation **before** the class
  was fenced — the precise sequence I-7 demands.

**Toward COMPLIES (attacks on the build's VIOLATES and INDETERMINATE):**
- **C7** moves. The build graded INDETERMINATE-AT-BYTES because the ground is cited to the barred
  Q-727. But the **earliest** wording (§4.2 above) is not categorical: `RELAY_PASTE_820:7` bars the
  classical reading "**unless a sealed sentence explicitly demands it**" — a status test with a named
  discharge route. On the founding generation C7 **COMPLIES**; on the compressed generation
  ("the classical reading is unlawful", 1101:12, 1106:13) it VIOLATES.
- **C5** does not move. Re-verified: the only ground reaches *notation* (`RELAY_PASTE_1101:12`;
  `SPEC_1107:15`), while 1105:6 and O37SR:1687 bar *machinery* and *principle*. And the ruling series
  runs the other way — DoR-010:8-13 **lifts** a fence on second variation and PERMITS "its first and
  second variations in the holonomy data". **VIOLATES confirmed, on a stronger basis than the build had.**
- **C6** does not move. **VIOLATES confirmed.**

### 6.4 Corrected Q3 tallies

**On the founding wording (2026-07-31 → 2026-08-12 16:37):**
**COMPLIES 5 (C1, C2, C3, C4, C7) · VIOLATES 2 (C5, C6) · INDETERMINATE-AT-BYTES 0.**
Build reported 4 / 2 / 1.

**On the compressed wording that governed lanes after 2026-08-12 17:42:**
**COMPLIES 1 (C4) · VIOLATES 6 · INDETERMINATE-AT-BYTES 0.** Build reported 1 / 5 / 1.

Both are reported. Which generation governs is an authority question **barred to this lane**.

The build's F-5 drift finding — 65 minutes from role-filling form to flat list on one evening — is
**CONFIRMED at bytes** (1101 mtime 16:37 → 1105 mtime 17:42), and it is now longer than the build
said: the founding generation begins at **DoR-003, 2026-07-31**, so the drift runs **twelve days**,
from a ruling that expressly declines to strip to a flat list of `NO`s.

**D3 GRADE: CONFIRMED-WITH-CORRECTIONS.**

---

## 7. D4 — THE VARIATIONAL CASE (Q4) — **CONFIRMED-WITH-CORRECTIONS**

### 7.1 Q4(a) — the answer survives; the basis was half the result set

I re-ran every pattern over all **28** ruling files, not 14:

| Pattern | Ruling files hit (28) | Verdict |
|---|---|---|
| `variational` | **0** | no ruling bars or names it |
| `extremal` | **0** | — |
| `extremiz` | **0** | — |
| `action principle` | **0** | — |
| `least action` | **0** | — |
| `Euler-Lagrange` | **0** | — |
| `saddle` | **0** | — |
| `variation` | **1** (DoR-010, ×3) | **not 0, as the build claimed** — and the occurrence is an ADOPTION/LIFT |
| `stationary` | **2** (DOR_017, DOR_018) | both adopting |

**Q4(a)'s ANSWER — no ratified ruling bars variational, extremal, stationary or action structure — is
CONFIRMED, and now over the full ruling set.** Its stated **basis** was wrong: `variation` is not 0.

The one ruling that carries the word does the opposite of barring.
`DECISION_OF_RECORD_010_STRUCTURAL_P_DEPENDENCE_AUTHORIZED_2026-08-02_V001.md:8-15`, quoted whole
including its adverse "STILL BARRED" clause at :17-20:

> "The evaluation fence on second variation / kernel structure is LIFTED FOR ONE SCOPED QUESTION:
> the p_ch-DEPENDENCE STRUCTURE of the finite influence action's second variation, at finite N,
> symbolically.
>
> PERMITTED: Gamma_N = -log A_N^(p) with A_N = (1-p) + p Z_N (the sealed Q-236 family) . its first
> and second variations in the holonomy data AT AND NEAR COINCIDENCE, symbolic in p . the exact
> p-dependence factor of the connected bilinear . whether that factor CANCELS or SURVIVES in the
> residual/root-condition RATIO structure (the phase condition Delta Phi = pi, structurally).
>
> STILL BARRED: any numerical kernel value . any K, K_*, B_ind value . alpha . any scale . any
> comparison to anything measured . anything beyond finite N and symbolic p."

Two things follow, and I state both. (1) There **was** a standing fence touching second variation
before the record-native fence existed — but it is an **evaluation** fence (it bars *computing*
values), not an **import** fence, and the two rulings that touch it (DoR-004, DoR-010) both **lift**
it. (2) Therefore the fenced class "no variational principle" has, at ruling level, no ancestor at
all — it is the one fence class with **zero** ruling-level footprint in either direction.

### 7.2 Q4(b) — both named rulings opened and verified at bytes

**DOR_017**, seal OK. The build's quotation of lines 9–24 and 28–30 is **exact**, including "quotient
action functionals" (:15), "Hessians" (:19), "the R5-generated Hessian class" (:20), "every downstream
result in the stationary package" (:28), and the adverse clause it correctly carried, "**No number is
licensed by this ruling**" (:23). **CONFIRMED.**

**DOR_019**, seal OK. The build's quotation of lines 7–22 is **exact**, including "The CARRIER METRIC
AND UNITS are RATIFIED as metric proposal V005" (:7) and "the finite C-side metric, R_C, and
quotient-norm formula" (:14). **CONFIRMED.**

**DOR_020**, seal OK. Quotation of lines 7–24 **exact**, including the adverse "FORBIDDEN until a
certified witness exists: binding a member, executing the fixed-point computation, any end test"
(:22-23). **CONFIRMED.**

**The build UNDERSTATED its own strongest exhibit.** `DOR_018_N_MEMBER_JETS_SHAPE_K_RATIFICATION_2026-08-03.md`
is titled, at **:1**:

> "# DECISION OF RECORD 018 — THE N-MEMBER **STATIONARY** JETS, SHAPE K (RATIFIED)"

and rules at **:7**: "The N member's **stationary jet** instantiation is RATIFIED as germ V003's SHAPE
K". A ratified ruling whose **subject** is a stationary object. The build listed this only as
"`stationary` 2 — both adopting."

**The ruling-versus-fence contradiction the build reports is CONFIRMED at bytes**, on both sides, with
the build's own qualification intact and correct: the O36SR/O37SR sentences (verified verbatim at
`:1686-1692` and `:1395-1399`, line wraps preserved) are self-attestations scoped to one artifact, and
the live conflict is with the unqualified compressed form at `RELAY_PASTE_1105:6` / `1106:13`.

**One addition the build missed, which strengthens its own finding:** the contradiction is not only
nine days wide, it is **bidirectional in time**. DoR-003 (2026-07-31) names KK and the radion as
imports; DoR-007 (2026-08-01) takes `(M,g)` off the table for a named subset; then DOR_019
(2026-08-03) ratifies a metric and DOR_020 (2026-08-04) adopts a continuum theory — **the ruling
series itself moves from barring to adopting within four days**, before any lane paste wrote a fence.

### 7.3 Q4(c) — NATIVE / IMPORTED grades, checked hardest

The brief flags calling an imported structure native as the severest available error. I re-read every
graded specimen at its cited line.

| # | Build grade | My check | Verdict |
|---|---|---|---|
| N-1 | NATIVE | `STAGE8_P5_SECTOR_ASSIGNMENT_V001.md:163-165` reads exactly: "says the / native skeleton is finite stationary incidence/source-record structure and / does not reach the external continuum source/field side." Quote exact, line wrap correctly noted. | **CONFIRMED** |
| N-2 | NATIVE | `STAGE8_AXN_BUILD_EXITB_SCHEME_DARIO_V001.md:129` and `:271` both present verbatim: "without `δ`, because it is algebraic in the square rather than variational"; "FRAGMENT P1, DERIVED WITHOUT delta because it is ALGEBRAIC IN THE SQUARE, not variational". | **CONFIRMED** |
| N-3 | INDETERMINATE ("third category") | `STAGE8_TASK4B_COMPLETED_STATIONARY_DEPENDENCY_AUDIT_LANE2_V001.md:156` reads exactly as quoted, typed "**RATIFIED AUTHORED PHYSICAL REQUIREMENT**; not derived from DoR-008/009". | **CONFIRMED** |
| N-4 | INDETERMINATE | `…:157` reads exactly as quoted, typed "**RATIFIED AUTHORED IMPLEMENTATION** of the Q-408/2PI route". | **CONFIRMED** |
| N-5 | **IMPORTED** | `BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md:107-108` reads exactly: "The lower bound is derived from the imported theorem. Saturation is adopted, / not derived. Historical target blindness is not claimed." Flags at :180-182 present as reported: `relative_orthogonalization_bound_imported = true`, `relative_onset_saturation_derived = false`, `relative_onset_saturation_adopted_Level_1 = true`. | **CONFIRMED — correctly graded IMPORTED** |
| N-6 | INDETERMINATE | survivor-topology flags carried as LIVE, as reported. | **CONFIRMED** |

**No imported structure was graded native.** The severest error available here was not committed. The
build's "third category — authored, ratified, and neither derived nor imported" is a fair reading of
the corpus's own typing, and I add that the same category is visible at ruling level: DoR-003:80-81
re-types the KK/radion content "as CONDITIONAL on an underived framing" — neither kept nor stripped.

**D4 GRADE: CONFIRMED-WITH-CORRECTIONS.** The answers hold and the quotations are exact; the sweep
basis was 14 of 28 rulings, `variation` is not 0, and the ruling-level KK/radion/second-variation
footprint was missed.

---

## 8. D5 — THE STRIPPING STANDARD (Q5) — **REFUTED**

### 8.1 The standard, restated from within my permitted set

From **I-7** itself (line 29, the permitted row): "**An entity is stripped as machinery only AFTER
PROVEN machinery (as the scale was: metric needed, none exists).**"

The exemplar's shape is legible from that parenthetical alone: *X is needed for Y · X does not exist ·
therefore Y is machinery.* The build derived the same shape from row I-1 at `:27`, outside its
permitted scope; the shape does not require it.

### 8.2 C3 MEETS the standard — the build's "STANDARD-MET 0" is refuted

Instantiate the exemplar against `STAGE8_KK_FRAMING_DERIVED_OR_IMPORTED_AUDIT_V001.md:7-9` (permitted
corpus, seal OK, 2026-07-31):

| Exemplar (scale) | C3 (KK framing) |
|---|---|
| a **metric** is needed to have a length | a **spatial fifth dimension with a physical length radius** is needed to have a KK framing |
| **no metric exists** at the origin | the corpus "does not derive that this internal state space is a spatial fifth dimension with a physical length radius" (:8-9) |
| therefore the scale is machinery | therefore "The KK framing is **imported/adopted, not derived**" (:7) |

The proof is not merely asserted: it is carried by two flagged determinations in the same artifact —
`projective_state_space_is_spatial_KK_fiber = false | TYPE-S` (:21) and
`five_dimensional_EH_derived_from_record_structure = false | TYPE-S` (:46) — plus a **TYPE-R
refutation** at :36-37. DoR-003 then adopts the result as a **STANDING** principal decision.

**This is the same proof shape as the exemplar, performed for a fence class, twelve days before the
fence was written.** The build's Q5 reasoning for C3 — "The stated ground is **circularity** …, which
is a different proof shape and does not instantiate the exemplar" (`:606`) — is wrong because it
graded the *lane paste's compressed restatement* of the ground instead of the ground.

**The adverse half, carried in full.** DoR-003 performs the proof and then **expressly declines to
strip**, at :80-81: "\*\*\* NONE OF THIS IS DELETED OR RETRACTED. IT IS RE-TYPED AS CONDITIONAL ON AN
UNDERIVED FRAMING. IF THE FRAMING IS LATER DERIVED, IT ALL RETURNS INTACT. \*\*\*" So the honest
statement is: **the proof the standard demands was performed for C3; the disposal chosen was
retention-as-conditional rather than stripping.** Either way, the build's two headline claims —
"STANDARD-MET **0**" and "the two sets are **disjoint** at bytes" (F-7, `:696-698`) — are **false**.

### 8.3 The other clauses, re-checked

- **C1** STANDARD-NOT-MET. **CONFIRMED**; nothing proves the umbrella a class, and DoR-003:52-57
  expressly preserves derived objects.
- **C2** STANDARD-NOT-MET. **CONFIRMED and strengthened**: DoR-007 makes the continuum limit a **named
  obligation to be derived** (:9-10, :19-20), and DOR_020:7 adopts a continuum theory. Nothing proves
  it machinery.
- **C4** STANDARD-NOT-MET. **CONFIRMED on a corrected basis.** The build's reason cited I-1 (out of
  scope). Independent bytes suffice: DoR-003:57 lists "the unique counting metric — **derived**;
  internal normalization FULLY PINNED", and DOR_019:7 ratifies a carrier metric. A class the record
  derives and a ruling ratifies is not proven machinery. The build's sharpest observation here — "In
  the exemplar the metric is **the absent thing that does the stripping, not the thing stripped**" —
  is correct and survives.
- **C5** STANDARD-NOT-MET. **CONFIRMED**; ground reaches notation only, DOR_017 ratifies the structure.
- **C6** STANDARD-NOT-MET. **CONFIRMED**; nothing to prove anything about.
- **C7** INDETERMINATE-AT-BYTES. **CONFIRMED** — Q-727's home is the barred register; the earliest
  wording (820:7) supplies a status test but not a stripping proof.

### 8.4 Corrected Q5 tally

**STANDARD-MET 1 (C3, with the ruling expressly declining to strip) · STANDARD-NOT-MET 5 (C1, C2, C4,
C5, C6) · INDETERMINATE-AT-BYTES 1 (C7).** Build reported **0** / 6 / 1.

The build's §6.4 / F-7 structural claim must be withdrawn: the set of things proven machinery and the
set of things the fence excludes are **not disjoint** — they intersect at C3.

**D5 GRADE: REFUTED.**

---

## 9. D6 — BARS — **CONFIRMED-WITH-CORRECTIONS**

**Advocacy / should-language:** I swept the build artifact for `should`, `ought`, `recommend`,
`advis`, `I suggest`, `propose that`. **Three hits, all of them the bar being observed rather than
broken** — `:11`, `:632`, `:712` ("This artifact does not say whether any fence clause *should*
stand"; "Whether any clause *should* stand is a principal's question"; "No recommendation is made
about any fence clause"). **No advocacy. No recommendation. CONFIRMED.**

**Authoring / adoption:** none found. The artifact reports and grades; it constructs no object, binds
no member, adopts nothing. **CONFIRMED.**

**Numeric fences:** `alpha_computed = false`, `proof_authorized = false`, `kappa_record_computed =
false` all declared and held. I swept for decimal numerals, `1/137`, `hbar`, and `= <number>` forms
and found **no** magnitude, coupling, scale, root, eigenvalue, norm or constant anywhere in the build
artifact. Notably, at N-5 the build quoted the surrounding sentences and the boolean flags of
`BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md` while **not** quoting the displayed magnitude
that sits three lines above its quotation — a correct approach-avoidance. **CONFIRMED.**

**One bar finding — scope excess on a permitted-but-restricted file.** The brief permits
`INSTINCTS_AND_TESTS_LEDGER_V001.md` "**for the method-correction row only**." The build read and
quoted beyond that row:
- `STAGE8_FENCE_PROVENANCE_O50SR_V001.md:309` — quotes row **I-1** at ledger line `:27` at length;
- `:330` — C4's Q2 **DERIVED** grade is sourced to `INSTINCTS_AND_TESTS_LEDGER_V001.md:27 (I-1)`;
- `:606` — C3's Q5 reasoning cites row **I-3** at ledger line `:31` ("carries result **PENDING** at
  :31 — the ledger's own word");
- `:591-598` — the Q5 exemplar's shape is stated as "read off I-1".

This is not advocacy and not a register breach, and the material is favourable-to-adverse rather than
self-serving. But it is a permission excess, and it is **load-bearing**: one Q2 grade (C4 = DERIVED)
rests on it entirely. Re-graded in §5.4 above without it.

**D6 GRADE: CONFIRMED-WITH-CORRECTIONS.**

---

## 10. CORRECTIONS, IN SEVERITY ORDER

| ID | Correction | Deciding file:line |
|---|---|---|
| **COR-A** | **F-2 is false at bytes.** "DOR_001 through DOR_015 do not exist as files in either supervision root under any casing or naming variant" — 14 of them exist, in **both** roots, sealed, under `DECISION_OF_RECORD_NNN_…`. 28 ruling files total, 28/28 seals OK. Every universal negative in Q1, Q2 and Q4(a) was run over 14 of 28. The naming convention was printed inside the permitted corpus. | `/Users/bgm/MB Work/alpha-program-archive/supervision/DECISION_OF_RECORD_007_SMOOTH_FORK_DERIVE_THE_LIMIT_2026-08-01_V001.md:1`; corpus pointer at `STAGE8_FIELD_CTP_CARRIER_AND_C0_JOIN_INSTANTIATION_ATTEMPT_V001.md:249` |
| **COR-B** | **Q1 census: three clauses originate in ratified rulings, not lane pastes.** C1 and C3 at 2026-07-31; C4 at 2026-08-01. "All seven earliest instances are type (b) … Zero ratified rulings originate any clause" is refuted. | `DECISION_OF_RECORD_003_…:49-50` (C1); `…003:24-26, :76-77` (C3); `DECISION_OF_RECORD_007_…:12-13` (C4) |
| **COR-C** | **Q5: STANDARD-MET is not 0, and the "disjoint sets" headline (F-7) is false.** C3 carries a proof of exactly the exemplar's shape, in a **permitted corpus** artifact, sealed, dated 2026-07-31 — with the adverse fact that the ruling then declined to strip and re-typed as conditional. | `STAGE8_KK_FRAMING_DERIVED_OR_IMPORTED_AUDIT_V001.md:7-9, :35-37`; adverse at `DECISION_OF_RECORD_003_…:80-81` |
| **COR-D** | **Q2: ADOPTED-BY-RULING is not 0.** C1 and C4 are adopted by ruling (scoped); C3 is DERIVED. Corrected tally 1 / 2 / 3 / 1. | `DECISION_OF_RECORD_003_…:3, :49-50`; `DECISION_OF_RECORD_007_…:12-13` |
| **COR-E** | **The method correction has an earlier RATIFIED statement (2026-08-01), twelve days before I-7.** The build sourced it solely to the ledger row of 2026-08-13. | `DECISION_OF_RECORD_004_…:103-106`, with `:28-30`; disposal form at `DECISION_OF_RECORD_003_…:80-81` |
| **COR-F** | **Permission excess.** The build read and quoted `INSTINCTS_AND_TESTS_LEDGER_V001.md` rows **I-1 (:27)** and **I-3 (:31)** although the brief permits that file "for the method-correction row only". Load-bearing: C4's Q2 DERIVED grade rests on it. | `STAGE8_FENCE_PROVENANCE_O50SR_V001.md:309, :330, :591, :606` |
| **COR-G** | **C7's earliest instance is 2026-08-09, not 2026-08-12 — and in a materially different, qualified form** ("not a lawful reading **unless a sealed sentence explicitly demands it**"), which moves C7's Q3 grade off INDETERMINATE on the founding wording. | `RELAY_PASTE_820_COMPLETION_AUDIT_DARIO_V001.md:7`; chain at `STAGE8_AXN_BUILD_DIRECTION_RELATION_DARIO_V001.md:36-37` |
| **COR-H** | **"No `DOR_*` ruling contains … `KK`, `radion`" is false over the ruling series.** `KK`/`Kaluza` in 2 ruling files, `radion` in 1 — and on the **barring** side, which is where C3 comes from. | `DECISION_OF_RECORD_003_…:24, :76`, `:124` |
| **COR-I** | **Q4(a)'s sweep basis is wrong: `variation` is not 0 across rulings.** DoR-010 carries it ×3 and describes a pre-existing "evaluation fence on second variation / kernel structure" — which it LIFTS. The **answer** (no ruling bars variational structure as an import) survives and is strengthened. | `DECISION_OF_RECORD_010_…:8-15` |
| **COR-J** | **C5's earliest instance is `RELAY_PASTE_1101` at 16:37, not `RELAY_PASTE_1102` at 17:11.** The variational bar is in the founding paste twice. | `RELAY_PASTE_1101_…:12` and `:18` |
| **COR-K** | **"There is exactly one passage anywhere in the corpus that argues why these classes are excluded" is false.** At least three earlier grounds exist. (The build's quotation of `1101:12` is itself exact.) | `STAGE8_KK_FRAMING_DERIVED_OR_IMPORTED_AUDIT_V001.md` (whole); `DECISION_OF_RECORD_003_…:11-31`; `DECISION_OF_RECORD_007_…:12-13` |
| **COR-L** | **F-3 overstated.** "standing NO-IMPORT" as an exact string does have exactly 2 carriers (confirmed), but "the rule it defers to **is not locatable at bytes**" is wrong: a ruling with `decision_status = STANDING` and "NO IMPORTED ANSATZ" exists. | `DECISION_OF_RECORD_003_…:5, :49` |
| **COR-M** | **C2/C4's earliest lane-instruction form is 2026-08-09, not 2026-08-12.** "no smooth import (S26)" is a standing GATES line from `RELAY_PASTE_791`; "no metric adopted" from `RELAY_PASTE_795`. The cited authority S26 is a **decline-register** row — barred to both lanes, so its ground is unreachable here as well. | `RELAY_PASTE_791_…:15`; `RELAY_PASTE_795_…:15`; `793_DONE.md:56` |
| **COR-N** | **The build understated its own strongest Q4(b) exhibit.** DOR_018 is titled "THE N-MEMBER **STATIONARY** JETS, SHAPE K (RATIFIED)" and ratifies a stationary jet instantiation; the build listed it only as "`stationary` 2 — both adopting". | `DOR_018_N_MEMBER_JETS_SHAPE_K_RATIFICATION_2026-08-03.md:1, :7` |

---

## 11. WHAT THE BUILD GOT RIGHT — stated so the refutation is not overread

- **Every quotation I could check is exact at its cited line**, with line wraps preserved: `1101:6-7`,
  `1101:9`, `1101:12`, `1105:6`, `1106:13`, `O37SR:1686-1692`, `O36SR:1395-1399`, `DOR_017:9-24` and
  `:28-30`, `DOR_019:7-22`, `DOR_020:7-24`, `I-7` at ledger line 29, and all six Q4(c) specimens.
  I found **no** fabricated locator and **no** paraphrase presented as a quotation.
- **Adverse clauses were carried inside quotations**, as claimed — DOR_017's "No number is licensed by
  this ruling", DOR_020's "FORBIDDEN until a certified witness exists", I-7's "Faithfulness is NOT
  proven machinery — its status is open".
- **The ruling-versus-fence contradiction is real**, and the build's own qualification of it (that
  O36SR/O37SR are self-attestations, and the live conflict is with the compressed lane form) is
  correct and important.
- **Q4(c)'s NATIVE/IMPORTED grades are correct.** N-5 is correctly IMPORTED by the corpus's own word.
  The severest available error was not committed.
- **C6's NEVER-JUSTIFIED grade is the one universal that holds**, and it now holds over 28 rulings.
- **F-6 (the phrase "KK reduction" is younger than the artifacts disclaiming it)** is confirmed at
  bytes: 5 carriers, all 2026-08-15 or later.
- **F-5 (the 65-minute compression)** is confirmed; my only change is that the drift is longer, not
  shorter, because the founding generation starts twelve days earlier at DoR-003.
- **Numeric fences held; no advocacy; no should-language; no authoring.**

---

## 12. IMPORT AUDIT

Every notion used here that is not the corpus's own, with a statement of whether the finding survives
without it. Provenance requirement, not a bar.

| # | Non-corpus notion | Where used | Survives without it? |
|---|---|---|---|
| IA-1 | **Filesystem mtime as chronology** | dating of relay pastes and corpus artifacts | **YES for every correction.** COR-A/B/C/D/E/H/I/K/L/N rest on in-file dates (`DATE: 2026-07-31`, `2026-08-01`, `2026-08-02`, `2026-08-03`) and on filename dates, not mtime. Only COR-G, COR-J and COR-M (relay-paste minute ordering) use mtime; COR-J is additionally corroborated by paste sequence numbering (1101 < 1102), and COR-G/COR-M by sequence numbering (791/795/820 < 1101). |
| IA-2 | **`Kaluza-Klein`, `radion`, `variational`, `Euler-Lagrange`, `second variation`, `Hessian`, `extremal` as search strings** | all sweeps | **YES.** Used only as byte patterns. Every count is a property of the files. No inference rests on what the terms mean outside the corpus. |
| IA-3 | **The logical form "X needed for Y; X absent; therefore Y is machinery"** | §8.1–8.2 | **YES.** The form is supplied by the corpus's own permitted row I-7 ("as the scale was: metric needed, none exists"); I instantiate it against the corpus's own sentences and add nothing. |
| IA-4 | **"Universal negative" / "result set" as audit vocabulary** | §5, D2 | **YES.** Descriptive labels for an operation the build performed and reported; removing the labels removes no finding. |
| IA-5 | **"Type (a)/(b)/(c)" clause typing** | §4 | **YES — it is the commission's own key**, taken from the build's §2.1 and applied unchanged. |
| IA-6 | **Reading `DECISION_OF_RECORD_NNN_*` as the same instrument as `DOR_NNN_*`** | AL-1, all of §3–§8 | **The existence findings survive; the content findings do not.** The identification is itself corpus-evidenced (DOR_017:14-17 cites "DoR-016 / DoR-009 / DoR-008" in one sentence with the later files), but it is a judgement and is logged as AL-1 with its reversal consequences stated. |

**No non-corpus notion is load-bearing for any grade.** The one load-bearing *judgement* is AL-1, and
it is a permission-scope reading, not an imported concept.

---

## 13. FLAG BLOCK

**AF-1 — AL-1 is the audit's single point of failure, and I name it.** If the principal rules that
`DECISION_OF_RECORD_*` files are outside this commission's permitted set, then COR-B, COR-D, COR-E,
COR-H, COR-I, COR-L and COR-N lose their deciding bytes and D1/D2 drop to
**INDETERMINATE-AT-BYTES** rather than REFUTED. **COR-A survives regardless** (the files exist and are
sealed; F-2's universal negative is false as written). **COR-C survives regardless**, because C3's
proof is in `STAGE8_KK_FRAMING_DERIVED_OR_IMPORTED_AUDIT_V001.md`, a **workspace/cleanroom** artifact
that is unambiguously corpus. **COR-F, COR-G, COR-J, COR-K, COR-M survive regardless.** So the overall
verdict REFUTED does not depend on AL-1.

**AF-2 — The genuine ruling gap is 001, 002 and 012, not 001–015.** No file numbered 001, 002 or 012
exists in either root under `DOR_*` or `DECISION_OF_RECORD_*`. Any universal over "all rulings"
remains limited by those three.

**AF-3 — Two clause-grounds remain unreachable to both lanes.** Q-509 and Q-727 (cited at
`RELAY_PASTE_1101:12`) and the decline-register row **S26** (cited at `RELAY_PASTE_791:15` and
`RELAY_PASTE_820:7`) all live in register-class files barred by this commission. C7's Q5 grade and
C2's smooth half are constrained by that bar, not by an incomplete search. The build named the first
pair; **S26 is a third, and the build did not surface it.**

**AF-4 — The fence's doctrinal origin is a ruling that expressly refused to strip.** DoR-003 performs
the machinery proof for KK/radion and then rules, at :80-81, that the content is "RE-TYPED AS
CONDITIONAL … IF THE FRAMING IS LATER DERIVED, IT ALL RETURNS INTACT", while DoR-004:103-106 rules
that a fence "IS NOT TO BAR EVALUATING A SPECIFIED STRUCTURE". The compressed lane form of
2026-08-12 17:42 carries neither. Reported as provenance; whether that matters is a principal's
question and is barred to this lane.

**AF-5 — One counting discrepancy left open, not load-bearing.** The build reports `RECORD-NATIVE
FENCE` at 11 raw hits; I get 13 over markdown and 15 including the generator `.py`. Distinct
basenames agree at **8**. The difference is enumeration scope. No grade turns on it.

**AF-6 — This lane's own limits.** I did not open row I-1 or I-3 of the INSTINCTS ledger (AL-2), so
the build's C4/Q2 basis is reported as **unverifiable-to-this-lane**, not as refuted. I did not open
any register, tracker, plan, handoff, observations-register or decision-sheet file.

---

## 14. CUSTODY AND SELF-AUDIT

- **DEFAULT-REFUTE lane. Default verdict REFUTED; the default is met on D1, D2 and D5 with deciding
  bytes, and is displaced on D3, D4 and D6.**
- **No register, plan, tracker, handoff, observations-register or decision-sheet file was read.**
  Leak counter **0** across all 9 exclusion patterns. Self-exclusion and subject-exclusion both armed.
- **No authoring, no advocacy, no adoption.** This artifact makes no recommendation about any fence
  clause and does not say whether any clause should stand.
- **Numeric fences held:** `alpha_computed = false`, `proof_authorized = false`,
  `kappa_record_computed = false`. No coupling, scale, root, eigenvalue, norm or constant was computed
  or approached. Where a quoted source displays a magnitude adjacent to a quoted span (e.g.
  `BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md`), the magnitude was not carried.
- **Quotation integrity:** every span quoted here was re-read at its cited line; line wraps preserved;
  adverse clauses carried inside the quotation — notably DoR-003's "NONE OF THIS IS DELETED OR
  RETRACTED … IT ALL RETURNS INTACT", DoR-010's "STILL BARRED", DoR-003:52-57's "WHAT REMAINS
  AVAILABLE — derived", and the KK audit's "No corpus derivation of 5D Einstein–Hilbert gravity from
  record structure was found."
- **Seals:** 28/28 ruling files OK · INSTINCTS ledger OK · subject artifact hash re-verified · every
  further cited corpus artifact checked in both sidecar forms before being called sealed.
- **No git action.**

---

## 15. GRADES

| Dimension | Grade |
|---|---|
| **D1 — the census (Q1)** | **REFUTED** |
| **D2 — stated grounds / universal negatives (Q2)** | **REFUTED** |
| **D3 — the method-correction test (Q3)** | **CONFIRMED-WITH-CORRECTIONS** |
| **D4 — the variational case (Q4)** | **CONFIRMED-WITH-CORRECTIONS** |
| **D5 — the stripping standard (Q5)** | **REFUTED** |
| **D6 — bars** | **CONFIRMED-WITH-CORRECTIONS** |

**OVERALL: REFUTED.**

**Corrected tallies:**
- **Q1** — TYPE (a) RATIFIED RULING **3** · TYPE (b) LANE-SCOPING **4** · TYPE (c) **0**
  *(build: 0 / 7 / 0)*
- **Q2** — DERIVED **1** · ADOPTED-BY-RULING **2** · LANE-SCOPING **3** · NEVER-JUSTIFIED **1**
  *(build: 1 / 0 / 5 / 1)*
- **Q3, founding wording** — COMPLIES **5** · VIOLATES **2** · INDETERMINATE-AT-BYTES **0**
  *(build: 4 / 2 / 1)*
- **Q3, compressed wording** — COMPLIES **1** · VIOLATES **6** · INDETERMINATE-AT-BYTES **0**
  *(build: 1 / 5 / 1)*
- **Q4(a)** — answer CONFIRMED over 28 rulings; basis corrected (`variation` ≠ 0)
- **Q5** — STANDARD-MET **1** · STANDARD-NOT-MET **5** · INDETERMINATE-AT-BYTES **1**
  *(build: 0 / 6 / 1)*

All findings **CLAIMED**. Builder never verifies own work; this lane never verifies its own either.

---

*End of artifact.*
