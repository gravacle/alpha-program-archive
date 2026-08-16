# STAGE 8 — FENCE PROVENANCE AUDIT (O50SR)

**Lane:** BUILD (commissioned pair). **Mode:** READ AND REPORT AT BYTES. **Date:** 2026-08-16.
**Subject:** the program's own record-native / no-import fence.

**Gates:** `alpha_computed = false` · `proof_authorized = false` · `kappa_record_computed = false`.
No numeric value of any coupling, scale, root, eigenvalue, norm or constant was computed or
approached anywhere in this artifact.

**Bars observed:** no authoring, no advocacy, no adoption. This artifact does not say whether any
fence clause *should* stand — that is a principal's question and is barred to this lane. It reports
provenance and grounds only. `INDETERMINATE-AT-BYTES` wherever the bytes do not decide.

---

## 0. CHOICE LEDGER

Every discretionary choice this lane made, and what turns on it.

| # | Choice | Alternatives available | Why taken | What would change if reversed |
|---|---|---|---|---|
| CL-1 | **Chronology proxy = filesystem mtime**, cross-checked against in-filename dates and relay-paste sequence numbers. | In-file "Date:" headers only; relay numbering only. | mtimes span 2026-07-23 → 2026-08-16 monotonically and agree with both filename dates and paste numbering wherever both exist (spot-checked on DOR_016–020 and pastes 1101/1105/1106). | If mtimes were rewritten by a copy operation, "earliest instance" claims would move. The **relay-paste sequence numbers independently corroborate** the single decisive finding (fence originates at paste 1101, before 1105/1106), so Q1's headline survives mtime failure. |
| CL-2 | **Workspace and cleanroom treated as mirrors**; counts reported both raw and deduped-by-basename. | Count every path separately. | Same basenames, same content, mtimes within ~1 min. Counting both would double every figure. | Raw counts are also reported, so nothing is hidden. No grade depends on the choice. |
| CL-3 | **A "clause" = a distinct excluded class**, not a distinct sentence. | One clause per wording variant. | The brief asks for "every distinct clause … in its several variants", which presupposes variants group under a class. | More rows, same grades. |
| CL-4 | **"Ratified ruling" = a `DOR_*` file** in the permitted supervision set. | Treat any artifact saying "RATIFIED" as a ruling. | The brief names `DOR_*` as the rulings and permits exactly those. Other artifacts *report* ratification; they are not the instrument. | Q2's ADOPTED-BY-RULING count could rise. I flag one boundary case (F-4) where a lane artifact carries "RATIFIED AUTHORED PHYSICAL REQUIREMENT" language. |
| CL-5 | **Graded the compressed and the founding forms of the fence separately** in Q3 rather than averaging them. | Grade "the fence" as one object. | They *do different things* at bytes — the brief expressly warns that a provenance requirement and a categorical bar look alike in short form. | Collapsing them would erase the single most load-bearing Q3 finding. |
| CL-6 | **Did not open the barred register file** that would likely carry fence-adoption history. | Read it. | REGISTER BAR is absolute and stands. | Several NEVER-JUSTIFIED grades are therefore *at-bytes-available-to-me*, not absolute. Stated explicitly in the FLAG BLOCK (F-1). |

---

## 1. SWEEP CUTOFFS

**Corpus assembled:** `/Users/bgm/MB Work/alpha-program-archive/{workspace,relay_inbox,relay_outbox}`
+ `/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003`
+ the 14 `DOR_*.md` under `…/alpha-program-archive/supervision/`
+ `INSTINCTS_AND_TESTS_LEDGER_V001.md` under `/Users/bgm/MB Work/alpha_supervision/` (method-correction row only).

Files enumerated: **6626**. After exclusions: **6595**.

**Exclusion globs (array) and per-pattern leak counter:**

| # | Pattern | Files removed |
|---|---|---|
| 1 | `*REGISTER*` | 27 |
| 2 | `*TRACKER*` | 0 |
| 3 | `THE_PLAN*` | 4 |
| 4 | `ROAD_REMAINING*` | 0 |
| 5 | `THE_HANDOFF*` | 0 |
| 6 | `OBSERVATIONS_REGISTER*` | 0 |
| 7 | `*DECISION_SHEET*` | 0 |
| 8 | `STAGE8_FENCE_PROVENANCE_O50SR_V001*` (self-exclude) | 0 |

**Leak counter: 0 barred files entered any sweep.** `QUESTIONS_SETTLED_REGISTER_V001.md` (present in
both supervision roots) was caught by pattern 1 and never read. Self-exclusion was armed before the
artifact existed; count 0 is therefore expected, not a miss.

**Sweeps run (pattern → raw file hits → distinct basenames):**

| Pattern | Raw | Distinct |
|---|---|---|
| `record-native` | 195 | 138 |
| `RECORD-NATIVE FENCE` | 11 | 8 |
| `continuum machinery` | 20 | 13 |
| `no continuum limit` | 7 | 6 |
| `KK reduction` | 5 | 5 |
| `KK/radion` | 6 | 5 |
| `Kaluza` | 26 | — |
| `no metric` | 119 | 89 |
| `variational` | 91 | — |
| `variational machinery` | 6 | 5 |
| `variational notation` | 14 | 10 |
| `no variational` | 15 | 12 |
| `imposed decomposition` | 2 | 2 |
| `classical reading` | 11 | 8 |
| `classical reading is unlawful` | 5 | 4 |
| `classical-gravity reading` | 2 | 2 |
| `continuum/KK/radion/variational` (compound) | 3 | 3 |
| `stationary` | 795 | — |
| `Hessian` | 999 | — |
| `saddle` | 213 | — |
| `saturat` | 183 | — |
| `extremal` | 20 | — |
| `extremiz` | 3 | — |
| `action functional` | 50 | — |
| `second variation` | 40 | — |
| `DO NOT IMPORT` | 6 | — |
| `standing NO-IMPORT` | 2 | 2 |

**SEALS.** `shasum -a 256 -c` run from each artifact's own directory. Both sidecar forms
(`<stem>.md.seal.sha256` and `<stem>.seal.sha256`) checked before calling anything unsealed.
- 14 `DOR_*` rulings: **14/14 OK**, no missing sidecars.
- 5 further cited artifacts (INSTINCTS ledger, paste 1101 [via 1105 pair], O36SR, O37SR,
  TASK4B_COMPLETED_STATIONARY_DEPENDENCY_AUDIT): **5/5 OK**.
- **Total 19/19 OK.**

---

## 2. Q1 — CENSUS OF THE FENCE

### 2.0 The decisive structural fact, stated first

The fence's **entire compound form originates on a single day, 2026-08-12, inside relay pastes** —
not in any ratified ruling. The label `RECORD-NATIVE FENCE` has **eleven** instances corpus-wide, all
dated 2026-08-12, the earliest being `RELAY_PASTE_1101_SADDLE_FOUNDATION_BUILD_DARIO_V001.md` at
16:37. The compressed compound `continuum/KK/radion/variational` exists in exactly **three** files:
paste 1105, its ACK, and the paired check paste 1106.

No `DOR_*` ruling contains the phrase `record-native fence`, `no-import`, `KK`, `radion`, or
`variational` in any form. Verified across all 14 rulings — hits: `record-native` **0**, `no-import`
**0**, `KK` **0**, `radion` **0**, `variational` **0**, `imposed decomposition` **0**,
`classical reading` **0**, `unlawful` **0**.

The mirror-image sweep is the finding's other half. The same 14 rulings **do** carry the classes the
fence names, on the adopting side: `continuum` **3** (DOR_016, DOR_020, DOR_020_A1), `metric` **1**
(DOR_019), `Hessian` **1** (DOR_017), `action functional` **1** (DOR_017). **Every ruling-level
occurrence of a fenced class is an adoption; none is a bar.**

### 2.1 Clause census

Ordered by first appearance. Type key: **(a)** ratified ruling · **(b)** lane-scoping instruction
inside a relay paste or brief · **(c)** unattributed repetition.

---

**C1 — RECORD-NATIVE ONLY (the umbrella clause).**

Wording variants, quoted:
- Founding, `RELAY_PASTE_1101_…_DARIO_V001.md:6-7`:
  > "RECORD-NATIVE FENCE (the principal's standing caution — HOLD IT HARD; violating it repeats the 1093 circularity):
  > - BUILD FROM THE RECORD'S OWN STRUCTURE ONLY (the discrete record cells and the sealed primitives). Do NOT import continuum / field-theory machinery."
- Compressed, `RELAY_PASTE_1105_…_DARIO_V001.md:6`:
  > "(2) DO NOT IMPORT — assemble from the record's OWN native structure only; NO continuum/KK/radion/variational machinery, NO imposed decomposition."
- Hard form, `RELAY_PASTE_1106_…_CODEX2_V001.md`:
  > "RECORD-NATIVE FENCE (HARD): the finite discrete record IS the surface; the continuum limit is imported. No continuum/KK/radion/variational machinery; the classical reading is unlawful."

**Earliest instance:** `RELAY_PASTE_1101_SADDLE_FOUNDATION_BUILD_DARIO_V001.md`, 2026-08-12 16:37.
**Type of earliest instance: (b) LANE-SCOPING INSTRUCTION.**

*Note on an older, different sense.* The bare adjective "record-native" appears from 2026-07-23
(`MICROSCOPIC_EXHAUSTION_IDENTIFIABILITY_GATE_V001.md:106`), three weeks earlier — but there it is a
**requirement to discharge, not a bar**: "must establish, rather than assume, that every physically
active generator in one causal record cell: 1. is represented in a uniquely specified finite
record-native algebra". That earlier usage is not this clause. Carriers: 138 distinct artifacts use
the adjective; **8** carry the fence *label*.

---

**C2 — NO CONTINUUM LIMIT / no continuum machinery.**

Variants:
- `RELAY_PASTE_1101:7`: "Do NOT import continuum / field-theory machinery."
- `RELAY_PASTE_1101:9`: "REFUSE any step that presupposes … any continuum structure the record does not natively carry."
- `RELAY_PASTE_1106`: "the finite discrete record IS the surface; the continuum limit is imported."
- `STAGE8_COMPLETION_AND_FORCING_O37SR_V001.md:1687`: "no continuum limit; no KK reduction; no metric; no variational principle; no" (line wraps; continues at 1688) "classical-physics reading as premise".

**Earliest instance of the clause as a bar:** `RELAY_PASTE_1101`, 2026-08-12 16:37. **Type: (b).**
**Carriers:** 13 distinct artifacts use "continuum machinery"; 6 use "no continuum limit".

*Line-wrap check performed.* The earliest *string* hit for "no continuum limit" is
2026-08-02, `STAGE8_TASK4A_DOOR_D_FALSIFIER_CARRIER_AND_CHECK_DIAGNOSIS_V001.md:299`, but re-reading
at the cited line shows it is **not a fence clause** — it is a provenance report about one
derivation: "No value of `p`, no rank choice, and no continuum limit enters this / equivalence. It
is a tensor-compatibility condition between the two finite / source ports." Excluded from the census
as a different speech act.

---

**C3 — NO KK REDUCTION / no KK compactification / no radion.**

Variants:
- `RELAY_PASTE_1101:8`: "any Kaluza-Klein compactification — are ROLES/SHADOWS to be FILLED by RECORD-NATIVE objects, NOT machinery to import."
- `RELAY_PASTE_1101:9`: "REFUSE any step that presupposes a smooth extra dimension, an assumed background metric, a KK compactification, an imported length scale (ell_P) …"
- `RELAY_PASTE_1105:6`: "NO continuum/KK/radion/variational machinery".
- `STAGE8_COMPLETION_AND_FORCING_O37SR_V001.md:1687`: "no KK reduction".

**Earliest instance:** `RELAY_PASTE_1101`, 2026-08-12 16:37. **Type: (b).**
**Carriers:** 5 distinct artifacts contain "KK reduction" — and **all five post-date 2026-08-15**,
i.e. the exact phrase "KK reduction" enters the corpus only in the lane self-attestations that
*claim to be obeying* it, plus paste 1122. The governing wording before that is "KK compactification".

---

**C4 — NO METRIC (and no imported length / normalization).**

Variants:
- `RELAY_PASTE_1101:9`: "an assumed background metric".
- `STAGE8_SADDLE_FOUNDATION_PARENT_ACTION_DARIO_V001.md:243-244`: "No metric, no compactification, no length, no smooth structure, no / variational notation is used".
- `STAGE8_COMPLETION_AND_FORCING_O37SR_V001.md:1687`: "no metric".

**Earliest instance as a bar:** `RELAY_PASTE_1101`, 2026-08-12 16:37. **Type: (b).**
**Carriers:** 89 distinct artifacts contain "no metric" — but the great majority are *findings*
("connection-only, no metric") rather than *instructions*. Earliest "no metric" string overall:
2026-07-31, `STAGE8_RECORD_CELL_SURFACE_AND_BETA_CLOSURE_HUNT_EINSTEIN_V001.md` — a finding, not a bar.

---

**C5 — NO VARIATIONAL PRINCIPLE / no variational machinery / no variational notation.**

Variants:
- `RELAY_PASTE_1105:6`: "NO continuum/KK/radion/variational machinery".
- `RELAY_PASTE_1102`: "NO variational notation (the notation-smuggles-linearity fence)".
- Paste-form (brief §): "no variational/additive/smooth NOTATION smuggle linearity the record does not license".
- `STAGE8_COMPLETION_AND_FORCING_O37SR_V001.md:1687`: "no variational principle".

**Earliest instance:** `RELAY_PASTE_1101`-day cluster; the specifically *variational* bar first at
`RELAY_PASTE_1102_SADDLE_FOUNDATION_CHECK_CODEX2_V001.md`, 2026-08-12 17:11. **Type: (b).**
**Carriers:** 5 distinct artifacts say "variational machinery"; 10 say "variational notation";
12 say "no variational". Against this, **91 artifacts use the word "variational"** substantively.

*Older, different sense.* "variational" appears from 2026-07-24
(`BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md`) — as structure in use, not as a barred class.

---

**C6 — NO IMPOSED DECOMPOSITION.**

Wording (single form, no variants):
- `RELAY_PASTE_1105_…_DARIO_V001.md:6`: "NO imposed decomposition."
- `SPEC_1107_…`/fence-restatement form: "No continuum, KK, radion or variational machinery; no imposed / decomposition." (line wraps)

**Earliest instance:** `RELAY_PASTE_1105_SURFACE_ASSEMBLY_DARIO_V001.md`, 2026-08-12 17:42.
**Type: (b).**
**Carriers: 2** — the paste and its own ACK (`relay_outbox/1105_ACK.md`). This is the **thinnest**
clause in the fence: it has no independent carrier anywhere in the corpus.

---

**C7 — CLASSICAL READING UNLAWFUL.**

Variants:
- `RELAY_PASTE_1101_…_DARIO_V001.md`: "the classical reading is unlawful".
- `RELAY_PASTE_1106`: "No continuum/KK/radion/variational machinery; the classical reading is unlawful."
- `STAGE8_CONSTRAIN_OR_CREATE_O36SR_V001.md:1395-1396`: "NO CLASSICAL-GRAVITY READING WAS USED AS A PREMISE ANYWHERE IN THIS ARTIFACT."

**Earliest instance:** `RELAY_PASTE_1101`, 2026-08-12 16:37. **Type: (b).**
**Carriers:** 8 distinct artifacts mention "classical reading"; 4 carry "classical reading is unlawful".

*Older, different sense.* 2026-08-09, `STAGE8_AXN_COMPLETION_AUDIT_DARIO_V001.md:292` — "the
classical reading is rejected on the sentences' words" — a **finding reached by reading**, expressly
not a bar, and it cites row S26 as "context, never as the argument".

### 2.2 Q1 summary table

| Clause | Earliest instance | Date | Type of earliest instance | Distinct carriers |
|---|---|---|---|---|
| C1 record-native only | `RELAY_PASTE_1101` | 2026-08-12 16:37 | **(b) lane-scoping** | 8 (label) |
| C2 no continuum limit | `RELAY_PASTE_1101` | 2026-08-12 16:37 | **(b) lane-scoping** | 13 / 6 |
| C3 no KK / radion | `RELAY_PASTE_1101` | 2026-08-12 16:37 | **(b) lane-scoping** | 5 |
| C4 no metric | `RELAY_PASTE_1101` | 2026-08-12 16:37 | **(b) lane-scoping** | 89 (mostly findings) |
| C5 no variational | `RELAY_PASTE_1102` | 2026-08-12 17:11 | **(b) lane-scoping** | 5 / 10 / 12 |
| C6 no imposed decomposition | `RELAY_PASTE_1105` | 2026-08-12 17:42 | **(b) lane-scoping** | **2** |
| C7 classical reading unlawful | `RELAY_PASTE_1101` | 2026-08-12 16:37 | **(b) lane-scoping** | 8 / 4 |

**All seven clauses' earliest instances are type (b). None is type (a). Zero ratified rulings
originate any clause of this fence.**

Everything after 2026-08-12 18:00 — including the four STAGE8 self-attestations of 2026-08-15 that
recite the full seven-part formula — is **type (c) unattributed repetition**. The clearest instance:
`STAGE8_COMPLETION_AND_FORCING_O37SR_V001.md:1686` cites "the standing NO-IMPORT rule", and the
phrase "standing NO-IMPORT" occurs in exactly **two** files corpus-wide — that artifact and its own
audit. **The cited standing rule has no referent at bytes.**

---

## 3. Q2 — IS THERE A STATED GROUND?

### 3.1 The one substantial grounds paragraph in the corpus

There is exactly **one** passage anywhere in the corpus that argues *why* these classes are
excluded. It sits inside the founding lane-scoping paste itself —
`RELAY_PASTE_1101_SADDLE_FOUNDATION_BUILD_DARIO_V001.md:12` — and is quoted here whole, adverse
clauses included:

> "SEALED NON-TRANSLATION RESULTS (CARRIED — the barred default is PROVEN, not a caution): the
> program has re-derived gauge theory's skeleton PIECE BY PIECE, RECORD-NATIVELY, and 'NEVER
> IMPORTED' it (Q-509), catching the continuous-additive-into-discrete 'type error of exactly the
> kind I audit others for'; the CLASSICAL READING IS UNLAWFUL (Q-727); a smooth/Banach/Frechet/
> Sobolev regularity class is a BARRED IMPORT — 'the continuum cell does not license smooth bumps';
> and even the NOTATION OF VARIATION ('L + eps*delta L') SMUGGLES A LINEARITY THE RECORD NEVER
> LICENSED. THEREFORE the DEFAULT for every continuum-named object AND every continuum notation is
> BARRED; the burden is on exhibiting a RECORD-NATIVE re-derivation (as Q-509 did for gauge), not on
> justifying an import."

Three observations at bytes, none of them advocacy:

1. The paragraph's own self-description is **"the barred default is PROVEN, not a caution"** — it
   claims proof status.
2. The proof is carried by **two register citations, Q-509 and Q-727**. Neither appears in any of the
   14 `DOR_*` rulings (checked: 0 hits). Their home is the register, which is **barred to this lane**.
   The ground is therefore **cited but not verifiable at bytes available to me** (FLAG F-1).
3. The paragraph ends in a **burden-shift with a discharge route** ("the burden is on exhibiting a
   RECORD-NATIVE re-derivation"), not an absolute prohibition. This matters in Q3.

The second grounds statement, `SPEC_1107_BETA_SURFACE_DERIVATION_ATTACK_V001.md:15`, compresses the
same citations: "NO variational/additive notation (smuggles linearity, Q-509/Q-727)."

The third — and the only *mechanism* ground — is the circularity argument for KK,
`RELAY_PASTE_1101:9`, quoted whole:

> "REFUSE any step that presupposes a smooth extra dimension, an assumed background metric, a KK
> compactification, an imported length scale (ell_P), or any continuum structure the record does not
> natively carry. If a required object can ONLY be met by such an import, STOP and report it as an
> IMPORT-BLOCK finding (the circular import to reject) — that is a full result, not a failure. This
> is exactly the 1093 error (imported KK gravity → circular); do not repeat it."

### 3.2 The one clause with a proven ground outside the fence's own paste

C4's ground is **not** in the fence pastes; it is in the permitted method-correction ledger, row I-1,
`INSTINCTS_AND_TESTS_LEDGER_V001.md:27`, quoted whole:

> "The origin is **pre-metric** (connection-only) so it structurally has **no scale**; expecting one
> at the beginning is a category error — length needs a metric, and there is none. | **PROVEN-grounded,
> not conjecture:** connection-only/no-metric (1101/1102, both-lane); dimensionless + forces only
> dimensionless content; `absolute_SI_record_duration_derived=false` (identifiability gate); scale
> objects (fiber radius, K_KK, metric) are ADOPTED/constructed; Q-1001 seals the record's content as
> NON-IDENTIFIABLE as a length | CONFIRMED (bedrock)"

Read exactly, this establishes **the origin carries no metric** — an absence finding. It does **not**
establish that a metric is machinery to be barred; the same row says in its own words that "scale
objects (fiber radius, K_KK, metric) are **ADOPTED/constructed**", i.e. the program builds metrics
downstream. The ground is real and proven, and it is **scoped to the origin/bare surface**.

### 3.3 Grades, clause by clause

| Clause | Ground stated anywhere? | Where | Grade |
|---|---|---|---|
| **C1** record-native only | Yes — the Q-509 gauge precedent + burden-shift | `RELAY_PASTE_1101:12` (a lane paste) | **LANE-SCOPING** |
| **C2** no continuum limit | Yes — "the finite discrete record IS the surface; the continuum limit is imported"; "continuous-additive-into-discrete type error" | `RELAY_PASTE_1101:12`, `1106:13` (lane pastes) | **LANE-SCOPING** |
| **C3** no KK / radion | Yes — circularity: "imported KK gravity → circular" | `RELAY_PASTE_1101:9` (a lane paste) | **LANE-SCOPING** (best-grounded clause of the seven) |
| **C4** no metric | Yes — the origin is proven pre-metric, connection-only, both-lane | `INSTINCTS_AND_TESTS_LEDGER_V001.md:27` (I-1) | **DERIVED — but scoped to the origin only** (see §3.2) |
| **C5** no variational | Partly — the ground covers **notation** only: "even the NOTATION OF VARIATION ('L + eps*delta L') SMUGGLES A LINEARITY THE RECORD NEVER LICENSED" | `RELAY_PASTE_1101:12`; `SPEC_1107:15` | **LANE-SCOPING** — and the ground is **narrower than the clause** (notation vs. principle/structure) |
| **C6** no imposed decomposition | **No.** No artifact anywhere defines "imposed decomposition" or says why it is excluded. Two carriers total, both the same paste and its ACK. | — | **NEVER-JUSTIFIED** |
| **C7** classical reading unlawful | Cited only — "the CLASSICAL READING IS UNLAWFUL (Q-727)" — with Q-727 unreachable at bytes | `RELAY_PASTE_1101:12` | **LANE-SCOPING** (ground cited, not exhibited) |

### 3.4 Q2 TALLY

| Grade | Count | Clauses |
|---|---|---|
| **DERIVED** | **1** | C4 (scoped to origin) |
| **ADOPTED-BY-RULING** | **0** | — |
| **LANE-SCOPING** | **5** | C1, C2, C3, C5, C7 |
| **NEVER-JUSTIFIED** | **1** | C6 |

**ADOPTED-BY-RULING is zero.** Sweep basis: all 14 `DOR_*` rulings read in full or grepped for every
clause term (`record-native`, `no-import`, `continuum machinery`, `KK`, `Kaluza`, `radion`,
`variational`, `imposed decomposition`, `classical reading`, `unlawful`) — **zero hits for every
term except "continuum", which appears only in a ruling that ADOPTS a continuum theory** (Q4b below).

---

## 4. Q3 — THE METHOD-CORRECTION TEST

### 4.1 The method correction, quoted whole from its source

`/Users/bgm/MB Work/alpha_supervision/INSTINCTS_AND_TESTS_LEDGER_V001.md:29`, row
**I-7 (CORRECTED 2026-08-13, principal)**, statement cell, quoted whole including its adverse and
qualifying clauses:

> "**Faithfulness/full source-distinguishability has UNDETERMINED status — it must be DETERMINED, not
> barred.** Weak distinguishability (kills n=0) is genuine bedrock; the UPGRADE to full faithfulness
> (resolving which winding → pins |n|) is either FORCED (a genuine structural feature of the record's
> dynamics, or required by the emergent boundary → |n| forced → Finish A) or IMPOSED (an epistemic
> demand the dynamics does not need → |n| free → Finish B). **METHOD CORRECTION:** the fence is
> "don't ACCEPT machinery blindly" = determine status before letting it be load-bearing — NOT "bar
> anything suspect." Barring faithfulness blindly (as the Z_Q build did to reach DOES-NOT-FORCE) is
> the same unexamined error as accepting it blindly (as the ether builder did to reach |n|=1). An
> entity is stripped as machinery only AFTER PROVEN machinery (as the scale was: metric needed, none
> exists). Faithfulness is NOT proven machinery — its status is open."

Attribution cell of the same row, quoted whole:

> "the principal's correction: we said we would not accept machinery blindly; we did not say we would
> bar it if it had value"

**Both facts the brief asked me to verify rather than assume are CONFIRMED at bytes**, at the cited
line, seal OK.

### 4.2 The test, clause by clause

The brief warns that a provenance requirement and a categorical bar look alike in short form. At
bytes they are **separable here**, because the fence exists in two generations with different verbs:

- **Founding generation (paste 1101, 16:37)** — verbs: *FILL*, *RECOGNIZE … AS EMERGENT LIMIT*,
  *REPORT AS IMPORT-BLOCK*, *the burden is on exhibiting a RECORD-NATIVE re-derivation*. These
  **determine status** and supply a discharge route.
- **Compressed generation (pastes 1105/1106, 17:42–17:55, and the 2026-08-15 recitations)** — verb:
  *NO*. Flat list, no status test, no discharge route.

| Clause | Deciding wording (quoted) | Grade |
|---|---|---|
| **C1** | Founding: "the burden is on exhibiting a RECORD-NATIVE re-derivation (as Q-509 did for gauge), not on justifying an import." A rebuttable default with a named discharge route. | **COMPLIES** |
| **C2** | Founding: continuum objects are "ROLES/SHADOWS to be FILLED by RECORD-NATIVE objects, NOT machinery to import … recognize the continuum object only as its EMERGENT LIMIT, never as an input." Status-determining. | **COMPLIES** |
| **C3** | Founding: "If a required object can ONLY be met by such an import, STOP and report it as an IMPORT-BLOCK finding … that is a full result, not a failure." The class is not barred; its necessity is *tested*, and a positive finding of necessity is a *result*. | **COMPLIES** |
| **C4** | "REFUSE any step that **presupposes** … an assumed background metric". Bars presupposition, not use; and status was independently determined (I-1, proven pre-metric). | **COMPLIES** |
| **C5** | Compressed: "NO continuum/KK/radion/**variational machinery**" (1105:6) and "no variational principle" (O37SR:1687). The only ground reaches **notation** — "even the NOTATION OF VARIATION ('L + eps*delta L') SMUGGLES A LINEARITY". A bar on *principle* and *machinery* is asserted with no status determination for that wider class. | **VIOLATES** |
| **C6** | "NO imposed decomposition." No definition, no ground, no discharge route, no carrier beyond the issuing paste and its ACK. A class barred in advance of determining its status is the exact shape I-7 names as error. | **VIOLATES** |
| **C7** | "the classical reading is **unlawful**". Categorical on its face; the ground is cited to Q-727, which is unreachable at bytes under the REGISTER BAR. Whether Q-727 determined status or barred in advance cannot be read. | **INDETERMINATE-AT-BYTES** |

### 4.3 Q3 TALLY

| Grade | Count | Clauses |
|---|---|---|
| **COMPLIES** | **4** | C1, C2, C3, C4 |
| **VIOLATES** | **2** | C5, C6 |
| **INDETERMINATE-AT-BYTES** | **1** | C7 |

### 4.4 The drift finding (reported, not argued)

Graded instead on the **operative compressed wording that actually governed lanes after 17:42 on
2026-08-12**, C1, C2 and C3 also read as categorical bars: "DO NOT IMPORT … NO continuum/KK/radion/
variational machinery, NO imposed decomposition" carries none of the founding paste's role-filling,
emergent-limit or IMPORT-BLOCK language. On that reading the tally is **COMPLIES 1 (C4) /
VIOLATES 5 / INDETERMINATE 1**.

Both tallies are reported because the bytes support both readings of *which* wording governs, and
choosing between them is an authority question barred to this lane (CL-5). What is **not**
indeterminate is that the compression happened, that it happened within 65 minutes on one evening,
and that the compressed form is the one recited by the 2026-08-15 artifacts.

---

## 5. Q4 — THE VARIATIONAL CASE SPECIFICALLY

### 5.1 Q4(a) — Does any ratified ruling bar variational, extremal, stationary or action structure?

**No. Not one.** All 14 `DOR_*` files swept:

| Pattern | DOR files hit | Which |
|---|---|---|
| `variational` | **0** | — |
| `extremal` | **0** | — |
| `extremiz` / `extremis` | **0** | — |
| `action principle` | **0** | — |
| `least action` | **0** | — |
| `Euler-Lagrange` | **0** | — |
| `saddle` | **0** | — |
| `variation` | **0** | — |
| `stationary` | **2** | DOR_017, DOR_018 — **both in ADOPTING senses** |
| `vary` | **1** | DOR_016 — ordinary-language use, not a bar |

**The preliminary check the brief asked me to verify is CONFIRMED: no ratified ruling mentions
variational structure at all — and the only ruling-level occurrences of the adjacent term
"stationary" are adoptions, not bars.**

### 5.2 Q4(b) — The two named rulings

#### DOR_017 — THE ACTION-COMPARISON SQUARE, N MEMBER (RATIFIED)

`…/supervision/DOR_017_ACTION_COMPARISON_SQUARE_N_MEMBER_RATIFICATION_2026-08-03.md`, seal OK.

What it **adopts**, quoted whole from lines 9–24:

> "The ACTION-COMPARISON/2PI SQUARE is RATIFIED as square proposal V004's merged candidate, CLOSED BY
> THE N MEMBER: the certified covariant divergence-generated member m = (δ_div, Depth, Accum, Gen, φ,
> Norm, ν) with its independent bottom legs b_N.
>
> In force:
> - The forced diagram (derived, Q-358): DoR-016 doubled access → the DoR-009 every-prefix traces →
>   the descent D_G → **the canonical pullback D_G\* on quotient action functionals**; T^char on its
>   sealed square / zero-extension scope only; the Q-408 placement; the five DoR-008 restriction
>   obligations.
> - The five authored residues R1–R5, with R1-COV across members, generators, normalizers, bottom
>   legs, **Hessians**, and restrictions, including the proven ρ_H,N naturality cube on the
>   R5-generated **Hessian class** (inverse, Schur, retarded-extraction covariance).
> - The consumer certificate (Q-358): quotient-only for the φ_div square; the QE record BANKED
>   (lawful endpoint-consumer typing preserved, adopted nowhere).
> - The scale ν remains SYMBOLIC. No number is licensed by this ruling; the scale meets its own gate
>   at A32 and the final evaluation DoR."

And from its standing falsifier, lines 28–30:

> "MEMBER-SENSITIVITY TAGGING: every downstream result in **the stationary package** and the response
> computation must be tagged member-sensitive or member-independent"

**Does its content fall inside a class the fence purports to exclude? YES.** The ruling adopts
**action functionals**, a **Hessian class** (second-variation structure), and **"the stationary
package"** — squarely inside the class the fence names "variational machinery" / "no variational
principle".

#### DOR_019 — THE CARRIER METRIC AND UNITS (RATIFIED)

`…/supervision/DOR_019_CARRIER_METRIC_AND_UNITS_RATIFICATION_2026-08-03.md`, seal OK.

What it **adopts**, quoted whole from lines 7–22:

> "The CARRIER METRIC AND UNITS are RATIFIED as metric proposal V005
> (`STAGE8_TASK4B_CARRIER_METRIC_AND_UNITS_PROPOSAL_LANE2_V005.md`, `2a379098…`).
>
> DERIVED CORE (in force as theorems): the forced pullback semiform s_G(c,d) = g_A4(u_c, u_d);
> family-wide FULLNESS (A2-R10 forces image(L_G)+image(B_G) = E_G, hence ker(I_K) = 0 — **the semiform
> is positive definite on the FULL carrier**; every record-visible cycle carries nonzero current); the
> W3 rank-preserving isometry; **the finite C-side metric, R_C, and quotient-norm formula**; the C/K
> unit-duality classes with U_A^-2 Riesz duals; R4-ONLY conversion routing with the failure-capable
> NO_IMPLICIT_CROSS_SECTOR_UNIT certificate (residual-parameter audit: none exists undeclared; nu
> remains symbolic).
>
> AUTHORED (four disclosed items): the R5 completed-carrier identification; the positivity/reality
> completion convention; the A4 automorphism isometry (beyond W3's reach); **the carrier units and the
> R4 unit seam**."

**Does its content fall inside a class the fence purports to exclude? YES.** The ruling ratifies a
**metric** and **units** — the fence's C4 ("no metric") and the O37SR recitation's "no unit; no
dimensional quantity".

#### A third, unprompted: DOR_020 — THE CONTINUUM PACKAGE (RATIFIED CONDITIONALLY)

Found while sweeping; reported because it bears directly on C2. Lines 7–24, quoted whole:

> "THE CONTINUUM PACKAGE is ADOPTED as **the program's declared continuum theory**, in the only form
> the hostile review certifies as honest (Q-421, P3): CONDITIONAL on nonemptiness of the joint J1-J15
> equalizer over the six irreducible generators: B_R1_NATURAL, B_Q408_REFINEMENT, B_C1_COMPLETION,
> B_FAITHFULNESS, B_C2_RESPONSE_BOUNDARY, B_C3_MAXWELL_HODGE.
>
> The adopted content: package V005's eight clauses + the fifteen derived compatibility families
> (`09883a0d…`), with the derived path-subdivision square, the PL refinement core, the typed
> P4/P5/P7/P8 rules, and all permanent regressions (the abstract-kernel, circular-pi, misstated-
> nonemptiness, and joint-equalizer attacks).
>
> LICENSED: downstream conditional derivation, every result carrying the condition tag [EQ6].
> FORBIDDEN until a certified witness exists: binding a member, executing the fixed-point
> computation, any end test. The physical reader's nonemptiness stands as DERIVED-CONDITIONAL from
> three generators."

### 5.3 The ruling-versus-fence contradiction, stated plainly

**A ratified ruling adopts what the fence bars. Three times.** Both sides quoted whole:

**THE FENCE SAYS** — `STAGE8_COMPLETION_AND_FORCING_O37SR_V001.md:1686-1692` (line wraps preserved,
checked at the cited lines):

> "NOTIONS DELIBERATELY NOT USED, checked against the standing NO-IMPORT rule:
>   no continuum limit; no KK reduction; no metric; no variational principle; no
>   classical-physics reading as premise; no faithfulness premise as authority; no
>   measured constant; no physical magnitude; no scale; no unit; no dimensional
>   quantity; no comparison to any observed value. Where a consumed artifact's own
>   text contains such a notion inside a quotation, it is carried as that
>   artifact's carriage and is used here for no inference."

and `STAGE8_CONSTRAIN_OR_CREATE_O36SR_V001.md:1395-1399`:

> "NO CONTINUUM LIMIT, NO KK REDUCTION, NO METRIC, NO VARIATIONAL PRINCIPLE, AND NO
> CLASSICAL-GRAVITY READING WAS USED AS A PREMISE ANYWHERE IN THIS ARTIFACT.  Where
> the corpus's own quoted text contains such notions (e.g. the FS/Mandelstam-Tamm
> theorem at CS-8, "imported" by the corpus's own word), they appear only inside
> quotation and carry no inferential weight in any grade I assigned."

**THE RULINGS SAY** — DOR_017: "the canonical pullback D_G* on **quotient action functionals** …
**Hessians** … the R5-generated **Hessian class**"; and "every downstream result in **the stationary
package**". DOR_019: "**The CARRIER METRIC AND UNITS are RATIFIED**". DOR_020: "THE CONTINUUM PACKAGE
is ADOPTED as **the program's declared continuum theory**."

**Three of the five classes the fence names — continuum, metric, variational — are the explicit
subject matter of three ratified rulings, all dated 2026-08-03/04, i.e. NINE DAYS BEFORE the fence
was first written on 2026-08-12.**

A qualification the bytes require, stated so the finding is not overread: the O36SR/O37SR sentences
are **self-attestations about one artifact's own premises**, not program-wide legislation. Read
strictly as scope statements ("was used as a premise anywhere in *this artifact*"), they conflict
with nothing. The conflict is with the **compressed lane-scoping form** — "NO continuum/KK/radion/
variational machinery" (1105:6) and "the finite discrete record IS the surface; the continuum limit
is imported" (1106:13) — which is unqualified and which the rulings contradict directly. Which of
those two readings governs is an authority question **barred to this lane**.

### 5.4 Q4(c) — Native extremal / stationary / saturation / action-like structure

The corpus is **saturated** with this structure, and it predates the fence by three weeks:
`stationary` 795 files, `Hessian` 999, `saddle` 213, `saturat` 183, `action functional` 50,
`second variation` 40, `extremal` 20. Earliest instances 2026-07-23. Graded specimens:

| # | Structure, with the corpus's own definition quoted | Grade |
|---|---|---|
| N-1 | **Native finite-algebra stationary skeleton.** `STAGE8_P5_SECTOR_ASSIGNMENT_V001.md:163-165`: "`STAGE8_ROUTE4_NATIVE_FINITE_ALGEBRA_THEOREM_AUDIT_V001.md:90-126` says the **native skeleton is finite stationary incidence/source-record structure** and does not reach the external continuum source/field side." Stationarity here is a property of the record's own incidence algebra. | **NATIVE** |
| N-2 | **Algebraic-not-variational cross-term generation.** `STAGE8_AXN_BUILD_EXITB_SCHEME_DARIO_V001.md`: "one fragment is derivable without `δ`, **because it is algebraic in the square rather than variational**"; "FRAGMENT P1, DERIVED WITHOUT delta because it is ALGEBRAIC IN THE SQUARE, not variational: D_prim = sum_c A_c … => D_prim^2 = sum_c A_c^2 + sum_{c != c'} A_c A_{c'} … CONSEQUENCE: CELL-LOCAL INTEGRANDS GENERATE OVERLAP DESCENDANTS AUTOMATICALLY, BY CROSS TERMS." A record-native derivation that reaches an extremal-adjacent result **without** variational notation — the discharge route the founding fence asked for, actually performed. | **NATIVE** |
| N-3 | **The completed stationary condition / critical set.** `STAGE8_TASK4B_COMPLETED_STATIONARY_DEPENDENCY_AUDIT_LANE2_V001.md:156`: "live value path: `B_ind(K)=p_loc[Pi_R,ind[G_K]]`, with `G_K` a candidate normalized saddle satisfying the full residual/stationarity system; R5-2: `Crit_m={y in D_017:D_C Gamma_phi(y)=0}`" — typed by the corpus itself as "**RATIFIED AUTHORED PHYSICAL REQUIREMENT**; not derived from DoR-008/009". | **INDETERMINATE** — the corpus's own typing is a **third category**, "authored-and-ratified": neither derived from the record nor imported from outside. |
| N-4 | **Hessian / Schur second-variation stack.** Same file, same table: "divergence draft §8: `delta G_K=-H_CC^(-1)D_C(delta phi)`; R5-2: `Inv_CC` on `C_red`, `Schur=H_KK-H_KC Inv_CC H_CK`" — typed "**RATIFIED AUTHORED IMPLEMENTATION** of the Q-408/2PI route". | **INDETERMINATE** (same third category) |
| N-5 | **Saturation-as-extremization at the onset bound.** `BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md:107-108`: "**The lower bound is derived from the imported theorem. Saturation is adopted, not derived.** Historical target blindness is not claimed." Own flags at :182-183: `relative_onset_saturation_derived = false`, `relative_onset_saturation_adopted_Level_1 = true`, and at :180 `relative_orthogonalization_bound_imported = true`. | **IMPORTED** — by the corpus's own word, three times over |
| N-6 | **Joint-stationarity survivor topologies.** AXN structural-coupling graph, `survivor_topologies`: `{"id":"K_stationarity","status":"LIVE_EXPLICIT_PARTIAL","topology":"shared_variational_variables_and_joint_stationarity"}` and `{"id":"K_direct_mixed","status":"LIVE_NOT_EXHIBITED_NOT_EXCLUDED","topology":"shared_variational_variables_plus_direct_mixed_Gamma_rest_dependency"}`. Carried as **LIVE** surviving structure, not as barred machinery. | **INDETERMINATE** — status carried as live-and-partial by the corpus's own flags |

**Q4(c) answer: YES, the corpus contains native extremal/stationary structure.** N-1 and N-2 are
record-native by the corpus's own words. N-5 is imported by the corpus's own words. N-3, N-4 and N-6
sit in a third category the fence's binary (native / imported) does not have a slot for:
**authored, ratified, and neither derived nor imported** — which is precisely the status the method
correction says must be *determined* rather than assumed in either direction.

---

## 6. Q5 — WHICH CLASSES HAVE MET THE STRIPPING STANDARD?

### 6.1 The standard, and the shape of the one worked exemplar

From I-7: **"An entity is stripped as machinery only AFTER PROVEN machinery (as the scale was: metric
needed, none exists)."**

The exemplar's logical shape, read off I-1: *X is needed for Y · Y does not exist · therefore X is
machinery · therefore strip X.* Instantiated: **the scale** was stripped because **a metric** is
needed to have a length and **no metric exists at the origin** — "expecting one at the beginning is a
category error — length needs a metric, and there is none", graded "PROVEN-grounded, not conjecture …
CONFIRMED (bedrock)".

### 6.2 Has that proof been performed, clause by clause?

| Clause | Has the "needed for X, X does not exist" proof been performed for this class? | Grade |
|---|---|---|
| **C1** record-native only | No. C1 is the umbrella, not a class; nothing is proven machinery. The nearest thing is the Q-509 gauge precedent, which proves the *opposite* direction — that a record-native re-derivation **succeeded** — and so licenses a burden-shift, not a stripping. | **STANDARD-NOT-MET** |
| **C2** no continuum limit | No. No artifact proves the continuum limit is machinery. **DOR_020 ratifies it in use**: "THE CONTINUUM PACKAGE is ADOPTED as the program's declared continuum theory." | **STANDARD-NOT-MET** |
| **C3** no KK / radion | No. The stated ground is **circularity** ("imported KK gravity → circular"), which is a different proof shape and does not instantiate the exemplar. I-1 types the KK objects as "ADOPTED/constructed", not stripped; I-3 ("'α rides an absolute scale' is a machinery artifact … it was derived through the carrier/KK") carries result **"PENDING"** at :31 — the ledger's own word. | **STANDARD-NOT-MET** |
| **C4** no metric | No — and this is the subtle one. In the exemplar the metric is **the absent thing that does the stripping**, not the thing stripped. Nothing proves a metric is machinery; the ledger says the opposite, that metrics are "ADOPTED/constructed", and **DOR_019 ratifies one**: "The CARRIER METRIC AND UNITS are RATIFIED." What is proven is the scoped absence at the origin, which is a finding, not a stripping of the class. | **STANDARD-NOT-MET** |
| **C5** no variational | No. The only ground reaches **notation** ("the NOTATION OF VARIATION … SMUGGLES A LINEARITY"), never the structure. **DOR_017 ratifies the structure**: "quotient action functionals", "Hessians", "the R5-generated Hessian class", "the stationary package". | **STANDARD-NOT-MET** |
| **C6** no imposed decomposition | No. The class is never defined, never grounded, and carried by two files that are the same paste and its own ACK. There is nothing to have proven anything about. | **STANDARD-NOT-MET** |
| **C7** classical reading unlawful | Cannot be read. The ground is cited to **Q-727**, whose home is the register and which is **barred to this lane**. Whether a stripping proof was performed there is not visible at bytes. | **INDETERMINATE-AT-BYTES** |

### 6.3 Q5 TALLY — the commission's deliverable

| Grade | Count | Clauses |
|---|---|---|
| **STANDARD-MET** | **0** | — |
| **STANDARD-NOT-MET** | **6** | C1, C2, C3, C4, C5, C6 |
| **INDETERMINATE-AT-BYTES** | **1** | C7 |

### 6.4 The structural observation this tally exposes

**The one entity in the program that demonstrably met the stripping standard — the scale — is not a
fence clause. And no fence clause has met it.** The set of things proven machinery and the set of
things the fence excludes are, at bytes, **disjoint**.

Three of the seven clauses (C2, C4, C5) name classes that ratified rulings **adopt**, nine days
before the fence was written. One (C6) has no content at bytes at all. One (C3) has a real argument
of a **different** shape (circularity) that the exemplar's standard does not cover either way. One
(C1) is an umbrella whose cited precedent runs the other way. One (C7) is unreadable under the
REGISTER BAR.

This is reported as provenance. Whether any clause *should* stand is a principal's question and is
barred to this lane.

---

## 7. IMPORT AUDIT

Every notion I used that is not the corpus's own, with a statement of whether the finding survives
without it. This is a provenance requirement, not a bar — the distinction is this commission's subject.

| # | Non-corpus notion | Where used | Does the finding survive without it? |
|---|---|---|---|
| IA-1 | **Filesystem mtime as a chronology** | Every "earliest instance" claim; CL-1 | **YES, for the headline.** Relay-paste *sequence numbers* (1101 < 1102 < 1105 < 1106 < 1107) are corpus-internal and independently order the fence's origin. DOR dates are in the filenames. Only the fine-grained minute-level ordering depends on mtime. |
| IA-2 | **"Kaluza-Klein reduction", "radion", "variational principle", "Euler-Lagrange", "action functional", "Hessian", "second variation" as search terms** | Sweeps in §1, §5.1 | **YES.** These were used only as *string patterns* to find corpus text. Every reported hit and every count is a property of the bytes, not of the physics the terms name. No inference rests on what these terms mean outside the corpus. |
| IA-3 | **Critical-point reading of `Crit_m={y in D_017:D_C Gamma_phi(y)=0}`** | N-3, §5.4 | **YES.** The corpus itself calls this "the completed **stationary** condition" and "a candidate normalized **saddle** satisfying the full residual/**stationarity** system". I report the corpus's own typing; I do not add a theory of critical points. |
| IA-4 | **"Circularity" as a logical notion** | C3's ground, §3.1, §6.2 | **YES.** The corpus supplies the word and the argument: "imported KK gravity → circular". I quote, not extend. |
| IA-5 | **"Burden-shift" / "rebuttable default" as descriptive vocabulary** | §3.1 obs. 3; §4.2 C1 | **YES.** The quoted wording carries it explicitly — "the **DEFAULT** … is BARRED; the **burden is on** exhibiting a RECORD-NATIVE re-derivation". My vocabulary labels what the sentence already does. |
| IA-6 | **"Mirror" (workspace ≅ cleanroom)** | CL-2, all deduped counts | **YES.** Established at bytes: identical basenames, mtimes within ~1 minute. Raw counts are reported alongside deduped ones, so no grade depends on it. |
| IA-7 | **The distinction "categorical bar" vs "provenance requirement"** | All of Q3 | **YES — and it is the brief's own frame**, taken from the method correction's "determine status before letting it be load-bearing — NOT 'bar anything suspect'". Corpus-internal. |

**No non-corpus notion is load-bearing for any grade in Q1, Q2, Q3, Q4 or Q5.**

---

## 8. FLAG BLOCK

**F-1 — REGISTER BAR limits three grades, and I say which.** The grounds for C1, C5 and C7 are cited
to register entries **Q-509 and Q-727**, and C7's Q5 grade turns entirely on them. Neither appears in
any `DOR_*` ruling (0 hits across all 14). Their home is the barred register. **C7's
INDETERMINATE-AT-BYTES is caused by the bar, not by an incomplete search.** If the register were
opened, C7 could move to STANDARD-MET or STANDARD-NOT-MET, and C1/C5's Q2 grades could move to
DERIVED. C2, C3, C4 and C6 are **not** affected: their status is settled by the rulings and by the
ledger, both of which I could read.

**F-2 — The DOR series has a numbering gap I could not close.** The brief expected "roughly twenty"
rulings; **14** exist as files, numbered **016, 017, 018, 019, 020** plus nine `020_A1`–`020_A9`
amendments. **DOR_001 through DOR_015 do not exist as files** in either supervision root under any
casing or naming variant (searched). They are referenced from inside the surviving rulings — DOR_017
cites "DoR-016", "the DoR-009 every-prefix traces", "the five DoR-008 restriction obligations". **Q4(a)'s
"no ratified ruling bars variational structure" is therefore established over the 14 rulings that
exist at bytes, not over 001–015, which I could not read.** This is the largest single limit on this
audit.

**F-3 — A cited standing rule with no referent.** `STAGE8_COMPLETION_AND_FORCING_O37SR_V001.md:1686`
invokes "the standing NO-IMPORT rule". The string "standing NO-IMPORT" occurs in exactly **two** files
corpus-wide: that artifact and its own audit. The rule it defers to **is not locatable at bytes**.

**F-4 — CL-4 boundary case.** `STAGE8_TASK4B_COMPLETED_STATIONARY_DEPENDENCY_AUDIT_LANE2_V001.md:156-158`
types objects as "**RATIFIED AUTHORED PHYSICAL REQUIREMENT**", "**RATIFIED AUTHORED IMPLEMENTATION**",
"**RATIFIED R5 STRUCTURE**" — ratification language in a lane artifact, not a `DOR_*` file. Under CL-4
I did not count these as rulings. Had I, Q2's ADOPTED-BY-RULING count would rise and C5's Q2 grade
would likely move off LANE-SCOPING. Flagged rather than decided, because deciding it is an authority
question barred to this lane.

**F-5 — The compression is 65 minutes wide.** The fence goes from the founding role-filling form
(1101, 16:37) to the flat compressed list (1105, 17:42) in **65 minutes on one evening**, and every
later recitation — including the four artifacts of 2026-08-15 — carries the compressed form. Both Q3
tallies are reported (§4.3, §4.4) because the bytes do not decide which generation governs.

**F-6 — "KK reduction" is younger than the artifacts that disclaim it.** The exact phrase enters the
corpus on **2026-08-15**, in the four STAGE8 self-attestations that claim to be obeying it, plus paste
1122 (2026-08-16). The governing wording before that date is "KK compactification". A reader matching
the brief's clause wording against the corpus will find the phrase only in its own disclaimers.

**F-7 — The proven stripping and the fence are disjoint sets.** Restated from §6.4 because it is the
audit's sharpest single fact: the scale met the standard and is not a fence clause; no fence clause
met the standard.

**F-8 — C6 may be an artifact of transcription.** "No imposed decomposition" has **two** carriers,
which are one paste and that paste's own ACK. It has no definition anywhere. It is possible at bytes
that it entered as phrasing rather than as an adopted clause; nothing in the corpus decides this.
**INDETERMINATE-AT-BYTES** as to origin; **NEVER-JUSTIFIED** as to ground, which is what Q2 asked.

---

## 9. CUSTODY AND SELF-AUDIT

- **BUILDER NEVER VERIFIES OWN WORK.** All findings **CLAIMED** until the paired lane's check.
- **No register, plan, tracker, handoff, observations-register or decision-sheet file was read.**
  Leak counter: **0** across all 8 exclusion patterns. Self-exclusion armed.
- **No authoring, no advocacy, no adoption.** No recommendation is made about any fence clause.
- **Numeric fences held:** `alpha_computed = false`, `proof_authorized = false`,
  `kappa_record_computed = false`. No coupling, scale, root, eigenvalue, norm or constant was
  computed or approached. The only numbers in this artifact are file counts, line numbers and dates.
- **Quotation integrity:** every quoted span was re-read at its cited line; mid-sentence line wraps
  are preserved and marked where they occur (O37SR:1687-1688, O36SR:1395-1396, the SPEC_1107 and
  1105 fence lines). Adverse clauses are included inside every quotation — notably DOR_017's "No
  number is licensed by this ruling", DOR_020's "FORBIDDEN until a certified witness exists", and
  I-7's "Faithfulness is NOT proven machinery — its status is open".
- **Seals: 19/19 OK.** Both sidecar forms checked before calling anything unsealed.

---

*End of artifact.*
