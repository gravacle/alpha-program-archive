# STAGE 8 — DEFAULT-REFUTE AUDIT OF THE TYPING-COVERAGE CENSUS — O51SR AUDIT V001

## AUDIT LANE — DEFAULT VERDICT REFUTED — 2026-08-16

```text
alpha_computed        = false [TERMINAL_FENCE_DECLARATION]
proof_authorized      = false [TERMINAL_FENCE_DECLARATION]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION]
```

**TARGET:** `/Users/bgm/MB Work/alpha-program-archive/workspace/STAGE8_TYPING_COVERAGE_O51SR_V001.md`
**TARGET SHA256 AS READ:** re-verified below, §2.4.

---

## 0. OVERALL VERDICT IN ONE LINE

**CONFIRMED-WITH-CORRECTIONS.** The default refutation is **not** sustained. Every
universal negative the target asserts survives an independent sweep at bytes; its
population is provably identical to mine (six of six type-flag token counts
reproduce **exactly**); its nine-number seed sweep reproduces **exactly**; its four
zero-hit sweeps return zero; and twenty-two of the twenty-three quoted spans I
re-read whole are verbatim at the cited lines. **Eleven corrections follow.** One
of them — COR-A — is a flat refutation of a discipline claim the target made in its
own voice and repeated to its commissioner. Two more — COR-B and COR-C — move
published tallies. **None of the eleven moves the direction of the finding**, and
COR-C moves it the other way: on the base the target's own headline uses, the
age result is *stronger* than the target reports.

---

## 1. CHOICE LEDGER

| # | Choice | Alternative not taken | Why |
|---|---|---|---|
| A1 | **Population re-enumerated from scratch with the target's declared BAR array, then reconciled by mtime against the target's seal timestamp.** | Accept the declared 5,989. | My enumeration returns 5,990 / 3,103. The single surplus is identified by name and mtime at §2.1, so the target's figure is confirmed rather than merely differing. |
| A2 | **Population identity proven, not assumed, before any tally is called wrong.** | Compare tallies directly. | S3's six type-flag counts reproduce to the unit across a 5,989-file population. That is the control that lets me attribute later mismatches to *pattern*, not to *corpus*. |
| A3 | **Where the target's regex is unpublished, I reconstruct a best fit, publish the reconstruction, and grade the exact tally INDETERMINATE-AT-BYTES while grading the direction.** | Grade the headline REFUTED for irreproducibility. | Irreproducibility is a disclosure defect (COR-F), not a falsity. The direction reproduces at 6.9 : 1 against a published 6.7 : 1. Calling that REFUTED would be the distorted answer. |
| A4 | **Sample rows re-read whole, wrap-checked, from the line *before* the cited span to the line *after* it.** | Read the cited range only. | Four "whole" claims fail exactly at the far edge of the cited range (COR-G). Reading only the range cannot detect that. |
| A5 | **The citation ranking is re-derived under the target's own stated rule before the sample is attacked.** | Attack the grades directly. | My re-derivation returns the target's eight published counts *exactly* (258/232/102/94/90/70/65/53). That proves the ranking correct and isolates the defect to the sample's conformity to it — COR-B. |
| A6 | **Both sidecar forms enumerated across all three directories, and the bare-only population counted.** | Spot-probe the named sources. | The count is what decides COR-A: the trap is real at 282 files and fires on neither of the two the target names. |
| A7 | **No re-typing, no adjudication, no proposal.** | — | Bars. This lane reports the divergence between the target's tables and the bytes and stops. |

---

## 2. POPULATION, BAR, AND SEALS — RE-DERIVED

### 2.1 Population — CONFIRMED

Enumerated `.md .txt .json` over both roots plus the 28 rulings, with the target's
BAR array applied to basenames before any read, carried as a Python list:

```text
raw over the two roots                     5,994
the 28 rulings                                28
barred (file instances)                       32
────────────────────────────────────────────────
PERMITTED (today)                          5,990   distinct basenames 3,103
TARGET DECLARES                            5,989   distinct basenames 3,102
```

The single surplus is identified: `STAGE8_JOIN_FRONTIER_O51SR_V001.md`, mtime
**2026-08-16 05:16:45**, which is **after** the target's own mtime of
**2026-08-16 05:15**. Removed from my working set, my population is **5,989 /
3,102 — the target's figure exactly.** **CONFIRMED.**

Independent control that the two populations are the *same* 5,989 files, not merely
the same size — §8 S3's type-flag token counts, re-derived:

```text
TOKEN         MINE     TARGET S3
TYPE-R       6,570         6,570   OK
TYPE-U       9,767         9,767   OK
TYPE-S       3,404         3,404   OK
TYPE-C       1,300         1,300   OK
NO_VERDICT   3,130         3,130   OK
TYPE-P       4,199         4,199   OK
```

**Six of six exact.** Every later mismatch in this audit is therefore a
pattern-level or arithmetic-level fact, not a corpus-level one.

### 2.2 REGISTER BAR — leak counter re-run, CONFIRMED

```text
PATTERN                  MATCHED   LEAKS INTO MY PERMITTED LIST
*REGISTER*                    27   0
*TRACKER*                      0   0
THE_PLAN*                      4   0
ROAD_REMAINING*                0   0
THE_HANDOFF*                   0   0
OBSERVATIONS_REGISTER*         0   0   (subsumed by *REGISTER*)
*DECISION_SHEET*               0   0
SELF (both artifacts)          1   0
```

`QUESTIONSSETTLED_REGISTER_V001.md` confirmed present in the **second root**
(`…/alpha_fundamental_record_action_cleanroom_v003/`) and caught by `*REGISTER*`;
**not opened.** The `*DECISION_SHEET*` files (`ACT3_SPEC5_REVISION_DECISION_SHEET…`
×2, `A32_RATIFICATION_DECISION_SHEET…`) are in `supervision/`, which contributes
only the 28 rulings — the target's stated reason is correct at bytes.

One label defect, non-material: the target's §2.2 prints `TOTAL BARRED (unique) 31`.
31 is the count of barred **file instances excluding self** (27 + 4); the count of
distinct barred **basenames** is 22. The word "unique" misdescribes the arithmetic
it labels. No downstream number depends on it.

### 2.3 THE TWENTY-EIGHT RULINGS — both conventions, CONFIRMED

```text
DOR_NNN_…                  14   016, 017, 018, 019, 020, 020_A1 … 020_A9
DECISION_OF_RECORD_NNN_…   14   003, 004, 005, 006, 007, 008, 009, 010, 011,
                                013, 014, 014_A1, 014_A2, 015
                           ──
                           28   enumerated independently, all opened.
```

The target's numbering note is correct at bytes: the `DECISION_OF_RECORD_` series
skips **001, 002 and 012**, and 28 is a count of files present, not of a contiguous
range. **Seals: 28/28 verify OK** with both sidecar forms probed. **CONFIRMED.**

### 2.4 SEALS AND THE SIDECAR TRAP — one claim REFUTED, see COR-A

Sidecar convention census, all three directories, both forms:

```text
DIRECTORY        .md   BARE-ONLY   BOTH FORMS   .md.seal ONLY   NO SIDECAR
workspace      1,820         141            9           1,509          161
cleanroom      1,523         141            0           1,217          165
supervision      979           0            0             886           93
```

The target's §2.3 table reads `workspace 1516 / 256 · cleanroom 1217 / 242 ·
supervision 886 / 1`. Backing out the two artifacts sealed to both forms since its
sweep (its own, and `STAGE8_JOIN_FRONTIER_O51SR_V001.md`), my workspace figures are
**1,516 and 256** — exact. Cleanroom **1,217 / 242** — exact. Supervision
**886 / 1** — exact. **That table is CONFIRMED.**

**The trap itself is real: 282 files across the two roots carry ONLY the bare
`<stem>.seal.sha256` form.** The target names none of them. The two files it does
name are not among them — see COR-A.

Target artifact re-hashed from its own directory:

```text
7c941eb3c34c8bfe32b4172baf313ffe9162e2cd6dbe9c26c91f9b702f14f041  STAGE8_TYPING_COVERAGE_O51SR_V001.md
```

Matches the value reported to the commissioner. Both its sidecar forms present and
both verify OK.

---

## 3. IMPORT AUDIT

| Import | Source | Status | Does the finding survive without it? |
|---|---|---|---|
| Target artifact | `STAGE8_TYPING_COVERAGE_O51SR_V001.md` | **PRIMARY, the object of audit.** Self-excluded from every sweep. | n/a |
| `LOCKED_PROCESS.md` | cleanroom root = corpus root B, sealed OK | **PRIMARY, IN CORPUS.** The target's §3/D3 correction is right at bytes: the file is at the cleanroom root, and only there. | Not an import. |
| `NEGATIVE_RESULT_TYPING_PROTOCOL_V001.md` | `supervision/`, **not one of the 28** | **IMPORT**, inherited from the target's own declaration. Opened at bytes, sealed OK, `.md.seal` form. | **YES.** Only COR-F's demonstration and COR-G item 4 touch it. Every tally in this audit is independent of it. |
| Reconstructed TIER B lexicon | **authored by this lane as a verification instrument**, published verbatim at §5.2 | **IMPORT, NAMED.** It is *not* the target's lexicon, which is unpublished. | **The direction survives; the exact tallies do not depend on it** — they are graded INDETERMINATE-AT-BYTES precisely because it is a reconstruction. |
| Logic used | file enumeration; substring and word-boundary regex; line-window adjacency; set collapse over (basename, line, pattern); counting. **No mathematics of the object domain.** | Named | — |

**No numeric value of any coupling, scale, root, eigenvalue, norm or constant was
computed, transcribed, approached, or compared.** Every number in this artifact's
own voice is a count of files, lines, or text occurrences. Where a source's symbolic
expression must be named to adjudicate a transcription defect (COR-J), it is named
as a **character sequence** and nothing is evaluated from it.

---

## 4. DIMENSION 1 — POPULATION AND SWEEPS

**GRADE: CONFIRMED-WITH-CORRECTIONS.**

### 4.1 What survives

Every universal negative the target asserts was re-run with patterns it did not
publish, over the independently enumerated 5,989:

```text
SWEEP                        TARGET   MINE   VERDICT
"coverage of the typing"          0      0   CONFIRMED
"partial coverage"                0      0   CONFIRMED
"escaped typing"                  0      0   CONFIRMED
"outside the protocol"            0      0   CONFIRMED
'untyped', basenames, excl.
  the two O46SR artifacts         82     82   CONFIRMED (83 incl. them)
'untyped', file-occurrences      284    284   CONFIRMED
```

A further universal negative the target states in prose and never sweeps — §4.2's
*"The bytes do not show a ratification of this file"* — I ran: **`NEGATIVE_RESULT_TYPING_PROTOCOL`
appears in ZERO of the 28 rulings.** The claim is **CONFIRMED at bytes**, and the
target gets credit for a negative it asserted without running the sweep that would
have supported it.

The seed re-derivation at §7.5 is **exact on all nine published numbers**:

```text                              TARGET   MINE
Shale-Stinespring  raw files            27     27
                   basenames            19     19
                   occurrences          52     52
                   near-hits ±5         10     10   all inside the two O46SR artifacts
                   genuine typings       0      0
"Equal-time localization"  9 bn/17 occ/1 near   9 / 17 / 1   near-hit is O46SR itself
"FP-2"                    35 bn/356 occ/10     35 / 356 / 10
                          "9 in O46SR, 1 in an unrelated audit"
```

The target's unnamed "unrelated audit" I locate and name:
`STAGE8_DISCREPANCY_COCYCLE_O38SR_AUDIT_V001.md:1370`. **CONFIRMED, and the
predecessor-strengthening claim — that the result holds over all five flags plus
`NO_VERDICT`, not TYPE-R alone — holds.**

### 4.2 What does not

**S12 is wrong under both of the target's own flag sets** — COR-D. **The TIER A and
TIER B patterns are nowhere published** — COR-F.

---

## 5. DIMENSION 2 — EVERY GRADED ROW

**GRADE: CONFIRMED-WITH-CORRECTIONS.** The grades' *deciding text* is verbatim
almost everywhere. The **sample's selection basis is not what the artifact says it
is**, and that is where the headline lives.

### 5.1 Deciding text, re-read whole and wrap-checked

| Row | Locator | Deciding text verbatim? | ±5 type flag? | Grade held? |
|---|---|---|---|---|
| S1 | `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:353-358` | **YES, exact** | **none** (checked :345-372; whole file region flag-free) | HELD |
| S1 adverse | same file `:359-366` | YES, elision marked with `[…]`; truncated mid-:365 | — | HELD |
| S2 | `STAGE8_CERTIFICATION_RULES_O8SR_V001.md:586-590` | **YES, exact** | **none** (file carries **zero** type flags anywhere) | HELD |
| S3 | same `:591-598` | **YES, exact** | none | HELD |
| S4 | same `:599-601` + `:609-613` | **YES, exact, both** | none | HELD, with the target's own block-level caveat |
| S5 | same `:602-608` (fragment) + `:619-623` | `:619-623` **exact**; `:602-608` quoted as a fragment, `(§5.3)` dropped | none | HELD, block-level |
| S6 | same `:508-515` | **truncated mid-:515** — COR-G | none | HELD |
| S7 | `STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md:316-321` | **truncated mid-:321** — COR-G | none (file carries zero type flags) | HELD |
| S8 | `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:55-56` | **YES, exact**; the surrounding `:50-62` is a defect enumeration as described | — | HELD (INDETERMINATE-AT-BYTES is right) |
| S9 | `STAGE8_GEN_OMEGA_…_V003.md:177`, body `:242 :245 :273` | **YES, exact**; `= false \| TYPE-R` with `test:` at all three; distances 65 and 96 lines **exact** | headline untyped at ±5 | HELD |
| S10 | `STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_…_V001.md:414-415`, sibling `:1065` | **YES, exact, both** | — | HELD (NOT-A-BARRIER is right) |

**No grade in the sample is wrong at the row level.** The escape the target reads in
each row is present in the source's own words, and the ±5 untyped determination is
correct in every case I re-ran.

### 5.2 The sample is not drawn from the ranking it declares — COR-B

§5.4 states the selection rule and declares it byte-decidable: *"for each basename
carrying ≥1 untyped core barrier, count the distinct **other** basenames in the
population containing its stem. Sample drawn from the top of that ranking."*

I re-derived that ranking. **It returns the target's eight published counts
exactly:**

```text
CITES  BASENAME                                                       ROWS DRAWN
  258  LOCKED_PROCESS.md                                                   0
  232  BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md                       1  (S8)
  102  STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V012.md                       0
   94  STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V003.md   1  (S9)
   90  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md                         1  (S1)
   70  STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md          0
   65  STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md                            1  (S7)
   53  STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md     1  (S10)
   ──
   17  STAGE8_CERTIFICATION_RULES_O8SR_V001.md   NOT IN THE PUBLISHED
                                                 RANKING AT ALL             5  (S2-S6)
```

**Half the sample is drawn from a basename with 17 downstream citations — outside
the published frame, below its floor of 53, and never shown to the reader** — while
rank 1 (258), rank 3 (102) and rank 6 (70) contribute nothing. The ranking is
right; the sentence "Sample drawn from the top of that ranking" does not describe
the sample.

The consequence lands on the headline. Of the seven NAMES-AN-ESCAPE grades,
**five (S2, S3, S4, S5, S6) come from that one out-of-frame artifact**, and two of
those five (S4, S5) are graded by the target itself as **block-level, not
row-level**. Restricted to rows the declared rule actually selects:

```text
                              AS PUBLISHED    ON THE DECLARED RULE
NAMES-AN-ESCAPE                  7 / 9  78%          2 / 4   50%
CLEAN                            0 / 9   0%          0 / 4    0%
INDETERMINATE-AT-BYTES           2 / 9  22%          2 / 4   50%
NOT-A-BARRIER (excluded)             1                   1
```

§5.5's comparison — *"the sampled untyped barriers name an escape at least as often
as the typed ones do — 7 of 9 against 2 of 3"* — becomes **2 of 4 against 2 of 3**,
which supports no comparison in either direction. **The corrected reading is that
the sample is too small and too concentrated to compare escape rates at all.**
Notably, this cuts *against* the target's own headline framing, and the target's
§9.4 claims pressure in both directions without catching it.

### 5.3 Rows and objects the target missed

Hunted and reported: `STAGE8_CERTIFICATION_RULES_O8SR_V001.md` carries **57**
untyped core barriers under my reconstructed lexicon and **zero type flags in the
entire file** — a larger untyped mass than every published top-8 entry except the
E1 spec. Its absence from the target's own §5.4 table, while supplying half the
sample, is the object the target should have surfaced and did not. I do not grade
its 57 rows; that is a principal-scale reading and is barred to me.

---

## 6. DIMENSION 3 — TYPE COMPARISONS

**GRADE: CONFIRMED-WITH-CORRECTIONS.** Proximity is *not* read as identity in the
load-bearing comparison. It is read loosely in the corroboration.

### 6.1 The §4.3 side-by-side — both sides ARE definitions. CONFIRMED.

```text
LOCKED_PROCESS:97          TYPE EVERY NEGATIVE                    <- a SEMANTIC CLASS
PROTOCOL Rule 1 (:59)      every `= false` flag and every         <- TWO SYNTACTIC FORMS
                           "not found"
```

Left side, re-read at bytes: `LOCKED_PROCESS.md:97` sits inside the fenced normative
block at `:95-101`, verbatim as quoted. Right side: `NEGATIVE_RESULT_TYPING_PROTOCOL_V001.md:59`
is item **1** under the heading `## 3. THE RULES` at `:57`, verbatim as quoted —
one source line, which the target re-wrapped across two display lines without loss.
**Both terms are normative rule text, not prose commentary. The comparison the whole
finding rests on is definition-vs-definition and it holds.**

The target's restraint here is correct and worth recording: §4.3 states that the
corpus *"does not anywhere state that the second should be read under the first;
that is left as the reader's inference and is **not drawn here**."* I re-read the
surrounding text and confirm no inference is drawn.

Counter-evidence the target itself carried, re-verified: `:104` *"every negative gets
four extra fields"* and `:72` *"A NEGATIVE CARRIES THE SAME EVIDENTIARY BURDEN AS A
POSITIVE"* — both present, both wider than Rule 1. The target quoted the material
that cuts against its own reading rather than suppressing it.

### 6.2 The §4.1 corroboration is prose, not a definition — COR-I

§4.1 offers `STAGE8_ACCESSOR_THEOREM_SUBSTITUTION_ADJUDICATION_EINSTEIN_V001.md:346`
under a heading reading *"The mandate — PRIMARY, IN CORPUS"*. The line is verbatim.
Its setting is not. At bytes it sits inside `## 8. DISCIPLINE` (`:343`) as one bullet
of a lane's **self-report of its own compliance**:

```text
343 ## 8. DISCIPLINE
344
345 - **Q-52:** nothing discharged, nothing declared derived. Q-94's `NO_VERDICT` untouched.
346 - **Q-54:** every negative typed with test, would-build, scope, or release.
347 - **Q-69:** flags kept distinct from discharge objects throughout; …
```

That is a lane saying *it complied*, not the corpus stating the mandate's scope. The
target's gloss of the four field names onto the four pre-DoR-006 types is defensible
at bytes — the protocol assigns `test` to TYPE-R, `would-build` to TYPE-U, `scope`
to TYPE-S, and a release condition to TYPE-C — but the citation is presented as
mandate text and is compliance prose. **Q1's answer does not depend on it**: it is
carried in §4.1 as corroboration of a claim already made at PRIMARY from
`LOCKED_PROCESS:97`.

### 6.3 The mandate's governing heading is outside the quoted block — COR-H

§4.1 quotes `LOCKED_PROCESS.md:95-101` as the "whole block" and concludes: *"It is
not restricted by grade, by artifact, by date, or by form."* The block's own heading,
four and two lines above the quoted range, is not quoted and is not listed among
§4.4's carve-outs:

```text
91 ## THE THREE THINGS IN A RELAY THAT PROTECT THE RESULT
92
93 *** THESE EARNED THEIR KEEP. NOTHING ELSE IN A RELAY DID. ***
94
95 ```text
96 A  "HUNT YOUR OWN COUNTEREXAMPLE, AND LEAD WITH IT IF YOU FIND ONE."
97 B  TYPE EVERY NEGATIVE:  …
```

The heading restricts by **process locus — "IN A RELAY"** — which is not one of the
four axes the target enumerates, so the sentence as written is not false. But a
scope-bearing header sitting two lines above a block declared "whole" belongs inside
the quoted range or inside §4.4. **The Q1 answer survives; the completeness claim
around it does not.**

---

## 7. DIMENSION 4 — QUOTATION INTEGRITY AND LOCATORS

**GRADE: CONFIRMED-WITH-CORRECTIONS.**

### 7.1 Verbatim at the cited line — CONFIRMED

Re-read whole and wrap-checked, all exact at the cited locator:

```text
LOCKED_PROCESS.md:95-101                                     EXACT
LOCKED_PROCESS.md:112-113 (non-revision clause)              EXACT
NEGATIVE_RESULT_TYPING_PROTOCOL_V001.md:5                    EXACT
NEGATIVE_RESULT_TYPING_PROTOCOL_V001.md:59                   EXACT (re-wrapped, no loss)
STAGE8_ACCESSOR_…_EINSTEIN_V001.md:346                       EXACT
STAGE8_RAW_CORRELATOR_…_SPEC_V001.md:131                     EXACT ("The adopted protocol at")
DECISION_OF_RECORD_006_…:6-14                                EXACT, whole, both blocks
STAGE8_TYPER_ESCAPES_O46SR_V001.md:96                        EXACT
STAGE8_TYPER_ESCAPES_O46SR_V001.md:636-641                   EXACT, whole
STAGE8_SOURCE_GERM_PHYS_V002_…_DETERMINATION_V001.md:474-489 EXACT (elision marked)
STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V003.md:189        EXACT
STAGE8_GRAPH_BOUNDARY_WALK_EINSTEIN_V001.md:51-56            EXACT
STAGE8_ALPHA_DEPENDENCY_CLOSURE_CENSUS_EINSTEIN_V001.md:34-36 EXACT
STAGE8_CANONICAL_IDENTIFIER_REGISTRY_EINSTEIN_V001.md:29-32   EXACT
STAGE8_CANONICAL_IDENTIFIER_REGISTRY_EINSTEIN_V001.md:66-76   EXACT (elision marked)
STAGE8_CERTIFICATION_RULES_O8SR_V001.md:586-590, :591-598,
  :599-601, :609-613, :619-623                               EXACT, all five
STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:353-358          EXACT
BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:55-56          EXACT
STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_…_V001.md:414-415, :1065    EXACT, both
STAGE8_GEN_OMEGA_…_PROPOSAL_V003.md:177, :242, :245, :273    EXACT, all four
```

**Adverse clauses were carried, not trimmed, in every case I checked.** S2 keeps
*"the one place at FP-3 where mathematics genuinely closes a door"*; S3 keeps the
three lines that make the escape unavailable inside the admitted class; S1 keeps
*"MAY NOT FIX THE OBSTRUCTION AT ALL"*; §4.4 keeps *"but it must be repaired before
a principal ratifies the artifact"*. This is the dimension on which the target is
strongest.

### 7.2 The two corrections to the target's own import audit — both CONFIRMED

`STAGE8_TYPER_ESCAPES_O46SR_V001.md:96` reads at bytes, whole:

> | The FP-2 / C6 quantifier finding | `STAGE8_CERTIFICATION_RULES_O8SR_V001.md:541-578` and `STAGE8_CERTIFICATION_RULES_O8SR_AUDIT_V001.md:410-440` | PRIMARY as to those two artifacts; **SECOND-HAND as to the E1 spec v002 itself**, which is not in the permitted corpus. |

`STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md` is present in **both roots**, byte-identical
(145,010 bytes each), each with a `.md.seal.sha256` sidecar. **The target's
correction is right, and its statement that the E1 half is wrong while the
`O8SR` half is right is also correct at bytes.** Its self-flagged D3 — that
`LOCKED_PROCESS.md` is in corpus root B despite being cited corpus-wide from
`/Users/bgm/MB Work/alpha_supervision/` — is likewise confirmed; the misleading
citation path is visible at `STAGE8_RAW_CORRELATOR_…_SPEC_V001.md:132`.

### 7.3 Four spans declared "whole" that are truncated — COR-G

Locator drift, all at the far edge of the cited range, all detectable only by
reading one line past it. None of the dropped material is adverse to the target's
reading; the defect is the word "whole".

---

## 8. DIMENSION 5 — BARS AND FENCES

**GRADE: CONFIRMED.**

```text
COMPOSITION PERFORMED BY THE TARGET LANE                       none found
OBJECT AUTHORED                                                none found
ADVOCACY / ADOPTION / PROPOSAL                                 none found
INFERENCE IN A SECTION BARRED FROM INFERENCE (§6, Q3)          none found
NEGATIVES TYPED OR RE-TYPED BY THE TARGET LANE                 0
BARRED FILES OPENED BY THE TARGET                              0 detectable
FENCE VIOLATION                                                none found
```

**§6 is the section barred from inference, and it holds.** The no-inference
sentence is printed under each of §6.1, §6.2, §6.3, §6.4 and it is not decoration:
§6.3 states the analytic co-occurrence and then explicitly declines the mechanism —
*"This lane does not infer that being analytic causes a barrier to go untyped, and
the corpus nowhere states it."* §6.5 refuses the load-bearing question outright
rather than guessing. §6.6 quotes the one stated dependence (DoR 006) and confines
it: *"It governs the TYPE-C → TYPE-P re-typing, not the base mandate."* DoR 006 at
bytes says exactly that and no more.

**§4.3 stops at the divergence.** It describes two sentences and declines to propose
a reading, an amendment, or a re-typing campaign. That restraint is correct: all
three would be principal acts.

**FENCES HELD.** Every number in the target's own voice is a count of text
occurrences. The symbolic expressions enumerated at its §9.1 appear only inside
quoted spans of other artifacts, reproduced because the adverse clauses around them
required it, and nothing is evaluated, compared, or approached from any of them. One
character-level transcription defect inside such a span is recorded as COR-J; it
alters a separator, not a magnitude, and no magnitude is approached by it.

**The target's self-reported defects D1–D5 are all real and all verified**, including
D4, which cuts against its own ratio and which it found in its own sample. A lane
that publishes the sub-class inflating its own headline is doing the thing the
default-refute posture is meant to force, without being forced.

---

## 9. DIMENSION 6 — HEADLINE VERSUS EVIDENCE

**GRADE: CONFIRMED-WITH-CORRECTIONS.**

### 9.1 The headline ratio — direction CONFIRMED, exact tally INDETERMINATE-AT-BYTES

The target publishes `778 : 5,206 = 6.7 : 1` and never publishes the patterns that
produce it. Reconstructing a best-fit lexicon from the six published row labels —

```text
cannot-exist  (?:cannot|can not|does not|do not|will not|may not|need not|did not)\s+exist
impossible    \bimpossib\w*
diverges      \bdiverg\w*
refuted       \brefut\w*
ruled-out     rule[sd]?\s+out|ruling\s+out|ruled-out
no-X-can      \bno\s+\w+\s+can\b
```

— collapsed by `(basename, line, pattern)`, ±5 window, over the identical 5,989:

```text
PATTERN         MINE T   MINE U   U:T      TARGET T   TARGET U   TARGET U:T
cannot-exist        64      346    5.4           70        360      5.1
impossible         114      578    5.1          113        561      5.0
diverges            48    1,336   27.8           32      1,241     38.8
refuted            631    3,651    5.8          538      2,856      5.3
ruled-out            3       37   12.3            4         29      7.2
no-X-can             8       62    7.8           21        159      7.6
────────────────────────────────────────────────────────────────────────
TOTAL              868    6,010    6.9          778      5,206      6.7
```

**The direction, the order of magnitude, and the `diverges` outlier all reproduce.**
The exact tallies do not, and cannot, because the target's "sweep/exclusion
bookkeeping lines suppressed" filter is undisclosed. **Graded: direction CONFIRMED,
exact tally INDETERMINATE-AT-BYTES, disclosure REFUTED (COR-F).**

Window sensitivity and the file-level split reproduce directionally on the same
reconstruction:

```text
                          TARGET          MINE
±5                         5,206         6,010
±40                        4,190 (-19.5%) 4,984 (-17.1%)
in files typing nothing    59.9%          61.4%
```

**§5.3's claim that the finding is not a window artifact is CONFIRMED.**

### 9.2 The target's own internal arithmetic — CONFIRMED

Every published table sums and every published ratio divides. Checked to the unit:
TIER B rows sum to 778 and 5,206; the six per-row ratios round correctly; §5.2's
ex-`refuted` figures `2,350 : 240 = 9.8 : 1` follow exactly from the TIER B table;
§8 S6's `9,404 raw → 5,984 collapsed` matches §5.1 exactly; §6.2, §6.3 and §6.4 all
sum to 778 and 5,206 and every percentage is correct on those bases; §5.3's four
window figures and the 40.1/59.9 split are correct; §5.5's 7/9 = 78% and 29/44 = 66%
are correct. **No arithmetic error found anywhere in the artifact.**

### 9.3 Disagreements the target's §8 reconciliation failed to reconcile

**§6.1 is on a different base from §6.2–6.4 and from the headline — COR-C.**
**The Q4 artifact count is four in two places and six in a third — COR-E.**
**§5.4's per-file UNTYPED column appears mirror-doubled — COR-K.**

The §8 reconciliation block is otherwise sound: it correctly restates the claim as
*"the protocol's coverage falls roughly an order of magnitude short of the class its
mandate names"* and explicitly disclaims the stronger reading — *"it does not say
5,206 findings escaped adjudication"* — which is the honest boundary and is the
boundary the evidence supports.

---

## 10. CORRECTIONS, IN SEVERITY ORDER

### COR-A — THE SIDECAR-TRAP CLAIM IS FALSE AT THE LOCATION IT NAMES. **REFUTED.**

**Deciding bytes:** `/Users/bgm/MB Work/alpha-program-archive/workspace/` directory listing.
**Target text:** `STAGE8_TYPING_COVERAGE_O51SR_V001.md:160-161` and `:169-172`.

The target's §2.3 table marks both predecessor artifacts as using the bare form:

```text
STAGE8_TYPER_ESCAPES_O46SR_V001.md                        .seal        OK  <-- BARE FORM
STAGE8_TYPER_ESCAPES_O46SR_AUDIT_V001.md                  .seal        OK  <-- BARE FORM
```

and concludes at `:169-172`, whole:

> **The two O46SR artifacts — the direct predecessors of this commission — use the
> bare `<stem>.seal.sha256` form.** A probe of only `<stem>.md.seal.sha256` would
> have reported the immediate prior work unsealed. That is the trap, and it fires
> exactly here.

At bytes, **both files carry BOTH sidecar forms, and all four verify OK**:

```text
STAGE8_TYPER_ESCAPES_O46SR_V001.md.seal.sha256          101 B   OK
STAGE8_TYPER_ESCAPES_O46SR_V001.seal.sha256             101 B   OK   <- identical content
STAGE8_TYPER_ESCAPES_O46SR_AUDIT_V001.md.seal.sha256    107 B   OK
STAGE8_TYPER_ESCAPES_O46SR_AUDIT_V001.seal.sha256       107 B   OK   <- identical content
```

Both `_V001` sidecars contain the same single line:
`0372e2937c408058dcb955a2f003d01551dd987f1c8aace7f1114d2af506e78c  STAGE8_TYPER_ESCAPES_O46SR_V001.md`.

**A probe of only `<stem>.md.seal.sha256` would have found the immediate prior work
sealed.** The sentence *"That is the trap, and it fires exactly here"* is false, and
it was repeated to the commissioner as *"Sidecar trap fired live."*

**Aggravating, and the reason this is COR-A:** the trap is real and the target had
the data to locate it. **282 files across the two roots carry ONLY the bare form**
(141 in workspace, 141 in cleanroom) — and the target names none of them. It counted
the bare-form sidecars correctly in its own §2.3 table (256 / 242, both confirmed
here) and then attached the finding to two files that are among the **nine** in
workspace carrying both. **CORRECTED CLAIM: the two O46SR artifacts carry both
sidecar forms; the bare-only population is 282 files, named nowhere in the target.**
No census number depends on this.

### COR-B — THE WEIGHTED SAMPLE DOES NOT FOLLOW ITS DECLARED SELECTION RULE. **REFUTED as to conformity; the ranking itself CONFIRMED.**

**Deciding bytes:** `STAGE8_TYPING_COVERAGE_O51SR_V001.md:425-439` against a
re-derivation of its own stated rule.

Five of ten rows (S2–S6, `:472-554`) come from `STAGE8_CERTIFICATION_RULES_O8SR_V001.md`,
downstream-citation count **17** — absent from the published ranking and below its
floor of 53. Ranks 1, 3 and 6 (258, 102, 70) contribute zero rows. My re-derivation
returns the target's eight published counts exactly, so the defect is conformity,
not method.

**CORRECTED TALLY.** On rows the declared rule actually selects:
**NAMES-AN-ESCAPE 2 / 4 (50%) · CLEAN 0 / 4 · INDETERMINATE-AT-BYTES 2 / 4 (50%) ·
NOT-A-BARRIER 1 excluded** — against the published **7 / 9 (78%) · 0 · 2 / 9 (22%) ·
1 excluded**. §5.5's comparison *"7 of 9 against 2 of 3"* corrects to **"2 of 4
against 2 of 3"**, which supports no comparison of escape rates in either direction.
**The corrected reading is that the sample is too small and too concentrated to
compare escape rates at all.** The residue of 5,196 ungraded rows and the refusal to
extrapolate onto it are unaffected and stand.

### COR-C — §6.1 IS COMPUTED ON THE RAW BASE WHILE §6.2–6.4 AND THE HEADLINE USE THE COLLAPSED BASE. **Undeclared; the finding survives and strengthens.**

**Deciding bytes:** `STAGE8_TYPING_COVERAGE_O51SR_V001.md:641-644`.

```text
                 2026-07        2026-08
TYPED       281  (20.3%)   1,102  (79.7%)      281 + 1,102 = 1,383
UNTYPED   1,499  (18.7%)   6,522  (81.3%)    1,499 + 6,522 = 8,021
```

1,383 and 8,021 are the **raw uncollapsed** totals named at `:378`. §6.2 (`:661`),
§6.3 (`:681`) and §6.4 (`:715-717`) are all stamped `TYPED (n=778) UNTYPED
(n=5,206)` — the collapsed base. The switch is not declared and §8's reconciliation
does not address it. **Aggravating:** §6.1's own method disclosure (`:653-656`) names
mirror copying as the mtime hazard — and the raw base is precisely the one that
double-counts mirrored files.

**CORRECTED TALLY**, same ±5 window, mirror-collapsed by (basename, line, pattern),
on the reconstructed lexicon:

```text
                 2026-07        2026-08
TYPED        188  (21.7%)     680  (78.3%)
UNTYPED      835  (13.9%)   5,175  (86.1%)
```

**The direction is unchanged and the separation is roughly five times larger** —
7.8 points against the 1.6 the target reports. On the correct base the untyped
population is not "marginally younger" but **materially younger**. §6.1's conclusion
— *"The 'legacy migration backlog' framing … does not describe this population"* —
is **CONFIRMED and strengthened**; only its table is on the wrong base.

### COR-D — S12 IS WRONG UNDER BOTH OF THE TARGET'S OWN FLAG SETS. **REFUTED.**

**Deciding bytes:** `STAGE8_TYPING_COVERAGE_O51SR_V001.md:912`, against the 28 rulings.

Published: *"typing tokens across the 28 rulings | supervision | **9 of 28** carry
any; 19 carry none."*

```text
FLAG SET USED                                          CARRY ANY   CARRY NONE
TYPE-R|TYPE-U|TYPE-S|TYPE-C|NO_VERDICT   (the set
  the target declares at :345)                                8           20
  + TYPE-P  (the live fifth type the target itself
  insists on at :241-243)                                    15           13
TARGET S12                                                    9           19
```

**Neither of the target's own flag sets reproduces 9 / 19.** **CORRECTED TALLY:
8 of 28 under the declared five-flag set; 15 of 28 under the live six-flag scheme.**
The eight are DOR_016 and DECISION_OF_RECORD_003, 004, 005, 006, 007, 011, 014_SOURCE_GERM.
S12 is a context row; no §5–§7 number depends on it.

### COR-E — THE Q4 ARTIFACT COUNT IS STATED AS FOUR AND AS SIX IN THE SAME ARTIFACT, AND THREE ARE EXHIBITED. **Unreconciled.**

**Deciding bytes:** `:32-33` — *"**Four artifacts** quantify an untyped mass (372
identifiers; ~1,050 flag lines; 383–457 identifiers)"*; `:773` — *"### 7.2
QUANTIFIED: the corpus counts its own untyped mass, **four times**"*; `:1041-1042` —
*"Q4 came back **YES — six artifacts quantifying the gap**, one ratified ruling
instituting it, and 82 artifacts carrying the vocabulary"*.

§7.2 exhibits **three** distinct artifacts (`STAGE8_GRAPH_BOUNDARY_WALK_EINSTEIN_V001.md`,
`STAGE8_ALPHA_DEPENDENCY_CLOSURE_CENSUS_EINSTEIN_V001.md`,
`STAGE8_CANONICAL_IDENTIFIER_REGISTRY_EINSTEIN_V001.md`, the last quoted twice).
§7.4 then lists **five** counts. The commissioner was told **six**. §8's
reconciliation block does not touch it. Relatedly, §7.4's *"the corpus's twelve
remarks about untyped negatives"* (`:859-860`) is supported by no row in §8.
**CORRECTED TALLY: three artifacts are exhibited as quantifying an untyped mass;
six artifacts are reachable if DoR 006 and the two §7.3 items are counted; the
artifact never states which convention it is using.** Every underlying quotation is
verbatim and every underlying count (372, ~1,050, 383–457, 487, six bare `false`) is
correct at bytes — only the tally of sources disagrees with itself.

### COR-F — THE TIER A AND TIER B PATTERNS ARE NOWHERE PUBLISHED; THE HEADLINE IS NOT REPRODUCIBLE FROM THE ARTIFACT. **Disclosure REFUTED; direction CONFIRMED.**

**Deciding bytes:** `:351-379` — six English row labels, no regex, plus an
undisclosed suppression filter (*"sweep/exclusion bookkeeping lines suppressed"*).

That the labels are not the patterns is demonstrable: `STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md`
contains **zero** occurrences of `cannot exist`, `impossib`, `diverg`, `refut` or
`ruled out` in the whole file, yet supplies sample row **S7** and an entry in the
§5.4 table. S7's barrier line is `:319` — *"The required Hamilton-Jacobi conjugate
energy does not exist yet."* — so the row labelled `cannot-exist` must match **"does
not exist"**. Confirming the reconstruction: `(?:cannot|can not|does not|do not|will
not|may not|need not|did not)\s+exist` returns **typed = 113**, the target's TIER A
`cannot-exist` typed count **exactly**. **S7 is therefore a legitimate member of the
population and its grade stands** — but only under a pattern the reader is never
shown. **CORRECTED STATEMENT: the six TIER A/B row labels are display names, not the
patterns; the headline 778 / 5,206 cannot be reproduced from the artifact as
published.** Best-fit reconstruction lands at **868 / 6,010 = 6.9 : 1**, published
here so a reader can see how far the direction is from the disclosure gap.

### COR-G — FOUR SPANS DECLARED "WHOLE" ARE TRUNCATED MID-LINE.

1. `:541` cites `STAGE8_CERTIFICATION_RULES_O8SR_V001.md:508-515, whole`; the quote
   ends at *"derives the opposite.**"*, dropping the remainder of `:515` —
   **"W1-AUDIT KILL 1, re-derived here exactly:"** — and the derivation it opens.
2. `:558` cites `STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md:316-321, whole`; the quote
   ends at *"Misner-Sharp or Brown-York."*, dropping the remainder of `:321` —
   **"`BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:33-48`"** — and `:322`
   **"states:"**. The dropped pointer is the thing that makes the row's own scope
   paragraph checkable, which matters because S7 is graded on that paragraph.
3. `:822` cites `STAGE8_INGREDIENT_CENSUS_O17SR_AUDIT_V001.md:239-243, whole`;
   the quote ends mid-`:242`, dropping **"Seals re-verified OK this session, from
   the artifact's own directory, for all three examined below."**
4. `:268-273` cites protocol `:72` and `:104` for quotes that stop mid-line, dropping
   `:72-75` (**"Today the cheapest legitimate action is to report an absence, which
   biases the whole corpus toward negatives"**) and the remainder of `:104`
   (**"Some existing negatives will need retyping…"**).

**None of the dropped material is adverse to the target's reading.** The defect is
the word "whole" and the locator, not suppression. Marked elisions elsewhere
(`[…]` at S1, §4.4, §7.2) are correctly signposted.

### COR-H — THE Q1 SCOPE QUOTE OMITS ITS OWN GOVERNING HEADING.

**Deciding bytes:** `LOCKED_PROCESS.md:91` — *"## THE THREE THINGS IN A RELAY THAT
PROTECT THE RESULT"* — and `:93` — *"*** THESE EARNED THEIR KEEP. NOTHING ELSE IN A
RELAY DID. ***"*. Target text `:216-227`.

The target quotes `:95-101` as the "whole block" and concludes *"It is not restricted
by grade, by artifact, by date, or by form."* The heading supplies a stated locus —
**IN A RELAY** — which is not one of those four axes, so the sentence is not false.
But it is a scope word sitting two lines above a block declared whole, and §4.4's
carve-out inventory (*"Two exemptions are stated"*) does not mention it. **CORRECTED
STATEMENT: the mandate's scope over negatives is universal as the target says; the
block carrying it is headed as a property of a relay, and that heading is outside
the quoted range and outside the carve-out inventory.**

### COR-I — THE Q1 CORROBORATION IS COMPLIANCE PROSE PRESENTED AS MANDATE TEXT.

**Deciding bytes:** `STAGE8_ACCESSOR_THEOREM_SUBSTITUTION_ADJUDICATION_EINSTEIN_V001.md:343-347`.
Target text `:234-243`. The line is verbatim; its setting is `## 8. DISCIPLINE`, a
lane's bulleted self-report of its own compliance. **Q1's answer does not depend on
it** — the mandate is quoted at PRIMARY from `LOCKED_PROCESS:97`. **The §4.3
side-by-side is unaffected: both its terms are normative rule text and it holds.**

### COR-J — CHARACTER-LEVEL DRIFT INSIDE A SPAN DECLARED VERBATIM.

**Deciding bytes:** `STAGE8_CERTIFICATION_RULES_O8SR_V001.md:509` reads
`4n^3 . k`. Target `:544` and `:952` render it `4n^3 · k`. A separator character was
substituted inside a quoted expression, in the one place the fence block enumerates
quoted expressions by name. **No magnitude is altered, evaluated, or approached, and
the fences hold.**

### COR-K — §5.4's PER-FILE UNTYPED COLUMN IS INCONSISTENT WITH THE COLLAPSED BASE IT FEEDS. **INDETERMINATE-AT-BYTES on the exact figure.**

**Deciding bytes:** `:430-439`. The table is introduced as a **per-basename** count
(*"for each basename carrying ≥1 untyped core barrier"*), which implies the collapsed
base. Two entries pin exactly against my reconstruction at a factor of two —
`STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md` reads **14**
against **7** distinct (line, pattern) sites; `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md`
reads **136** against **71**. Both files are present in both roots. Two further
entries do not fit that pattern, and the lexicon is unpublished (COR-F), so the exact
figures are **INDETERMINATE-AT-BYTES**. **The column is CONFIRMED inconsistent with
the 5,206 collapsed base used everywhere else.** No headline depends on it.

---

## 11. SWEEP CUTOFFS — PATTERN, HITS, LEAK COUNTER

Every sweep below was executed. Counts are actual.

| # | Pattern / rule | Scope | Hits | Leaks |
|---|---|---|---|---|
| A1 | file enumeration `.md .txt .json` minus BAR array (both artifacts self-excluded) | both roots + 28 rulings | **5,990** / 3,103 → **5,989** / 3,102 after removing the post-build file | 0 (per-pattern §2.2) |
| A2 | ruling enumeration, **both prefixes**, independently | supervision | `DOR_` **14** + `DECISION_OF_RECORD_` **14** = **28**, all opened | 0 non-ruling files entered |
| A3 | type-flag tokens, six | population | R 6,570 / U 9,767 / S 3,404 / C 1,300 / NO_VERDICT 3,130 / P 4,199 — **6 of 6 exact vs target** | — |
| A4 | TIER A reconstruction, six stems, ±5 | population | 14,451 literal / ~20,000 stem — **target 34,513 not reproducible**; ratio 9.1 : 1 vs target 9.0 : 1 | — |
| A5 | TIER B reconstruction, six patterns, ±5, collapsed | population | **868 / 6,010 = 6.9 : 1** vs target 778 / 5,206 = 6.7 : 1 | — |
| A6 | window sensitivity ±5/±10/±20/±40 | my 6,010 | 6,010 / 5,704 / 5,368 / 4,984 (−17.1%) vs target −19.5% | — |
| A7 | file-level type-flag presence | my 6,010 | 2,320 (38.6%) / 3,690 (61.4%) vs target 40.1 / 59.9 | — |
| A8 | age split by mtime, **both bases** | population | raw 337/1,648 Jul; collapsed **188/835** Jul — see COR-C | — |
| A9 | downstream-citation rank by stem containment | 3,102 basenames | target's 8 published counts **reproduced exactly**; `CERTIFICATION_RULES_O8SR_V001` = **17** | — |
| A10 | `Shale-Stinespring` / `Equal-time localization` / `FP-2` × 6 flags, ±5 | population | 52 / 17 / 356 occ; **0 genuine typings** — **9 of 9 numbers exact** | 10 / 1 / 10 near-hits, all attributed; the 1 non-O46SR located at `STAGE8_DISCREPANCY_COCYCLE_O38SR_AUDIT_V001.md:1370` |
| A11 | the four claimed zero-hit propositions | population | 0 / 0 / 0 / 0 — **all four CONFIRMED** | — |
| A12 | `untyped`, case-insensitive substring | population | **83** basenames (**82** excl. O46SR), **284** file-occurrences — **both exact** | — |
| A13 | `NEGATIVE_RESULT_TYPING_PROTOCOL` in the rulings | the 28 | **0** — the target's unswept universal negative CONFIRMED | 0 |
| A14 | typing tokens across the 28 rulings | supervision | **8 of 28** (5-flag) / **15 of 28** (6-flag) — **target's 9 refuted, COR-D** | 0 |
| A15 | sidecar census, both forms, three directories | all `.md` | **282 bare-only** across the two roots; the two O46SR artifacts among the **9 BOTH** — **COR-A** | 0 |
| A16 | seal verify, 28 rulings + target + both predecessors, both forms probed | own directories | **all OK** | 0 |
| A17 | per-file untyped core barriers, 9 named basenames | population | see COR-K | — |

**DECLARED CUTOFFS — three, and all discard evidence.**

1. **I re-read 23 quoted spans whole; I did not re-read every line the target cites.**
   The spans chosen are all deciding text for a grade, a tally, or a universal negative.
2. **My TIER A/B reconstructions are mine, not the target's.** They can establish
   direction and expose the disclosure gap; they cannot convict an exact tally, and I
   have graded accordingly rather than claiming a refutation the bytes do not license.
3. **I did not grade the 5,206 (or my 6,010) barriers.** Grading them is the
   principal-scale reading the target correctly declined, and it is barred to me.

**RECONCILIATION AGAINST MY OWN SWEEP BLOCK.** My overall grade is
CONFIRMED-WITH-CORRECTIONS, not REFUTED. A11, A12, A13 and A10 confirm every
universal negative and the seed sweep to the unit; A3 proves the populations
identical; A5–A7 reproduce the headline's direction, magnitude and robustness under
an independent lexicon; §7.1 confirms 22 of 23 quoted spans verbatim with adverse
clauses carried. Against that: A15 refutes one discipline claim outright (COR-A),
A9 refutes the sample's conformity to its own rule (COR-B), A14 refutes one context
row (COR-D), A8 relocates the age table to the wrong base while **strengthening its
conclusion** (COR-C), and A4/A5 establish that the headline is not reproducible as
published (COR-F). **Headline and evidence agree that the default refutation is not
sustained: the target's central finding — that the typing protocol's coverage falls
roughly an order of magnitude short of the class its mandate names, that the
shortfall is not explained by age or inheritance, and that it concentrates in
analytic barriers — survives every attack I could run at bytes.** What does not
survive is one sidecar claim, one sampling claim, one ruling-census row, and the
reproducibility of the exact tallies.

---

## 12. PER-DIMENSION GRADES

```text
DIMENSION                                    GRADE
1  Population and sweeps                     CONFIRMED-WITH-CORRECTIONS   (COR-D, COR-F)
2  Every graded row                          CONFIRMED-WITH-CORRECTIONS   (COR-B, COR-K)
3  Type comparisons                          CONFIRMED-WITH-CORRECTIONS   (COR-I, COR-H)
4  Quotation integrity and locators          CONFIRMED-WITH-CORRECTIONS   (COR-G, COR-J)
5  Bars and fences                           CONFIRMED
6  Headline versus evidence                  CONFIRMED-WITH-CORRECTIONS   (COR-C, COR-E, COR-A)
────────────────────────────────────────────────────────────────────────
OVERALL                                      CONFIRMED-WITH-CORRECTIONS
```

**The default verdict of REFUTED is NOT sustained**, and the reason is recorded
rather than assumed: the target's population is provably identical to mine, its six
type-flag counts and its nine seed-sweep numbers reproduce exactly, all four of its
zero-hit propositions return zero, its arithmetic contains no error anywhere, and its
self-reported defects D1–D5 are all real. Eleven corrections stand. **None reverses
the finding; COR-C strengthens it.**

---

## 13. FLAG BLOCK

### 13.1 Fences

```text
alpha_computed        = false   [held; no coupling value approached]
proof_authorized      = false   [held; nothing proved, nothing authored]
kappa_record_computed = false   [held]
```

No numeric value of any coupling, scale, root, eigenvalue, norm, or constant was
computed, transcribed, compared, or approached by this lane. COR-J names a
**separator character** inside a source's quoted expression and evaluates nothing
from it. Every number in this artifact's own voice is a count of files, lines, or
text occurrences.

### 13.2 Bar incidents

```text
BARRED FILES OPENED                                   0
  QUESTIONSSETTLED_REGISTER_V001.md (second root)     NOT OPENED (caught by *REGISTER*)
  all *REGISTER* (27), THE_PLAN* (4)                  NOT OPENED (leak counters 0)
  any *TRACKER*, ROAD_REMAINING*, THE_HANDOFF*,
    *DECISION_SHEET*                                  NOT OPENED (0 matched in the roots)
SELF-EXCLUSION                                        LIVE in every sweep; BOTH this
                                                      artifact and the target's own
                                                      artifact excluded from my census
SUPERVISION DIRECTORY                                 the 28 rulings opened;
                                                      NEGATIVE_RESULT_TYPING_PROTOCOL_V001.md
                                                      opened as a DECLARED IMPORT (§3),
                                                      inherited from the target. No other
                                                      file there opened.
AUTHORING / ADVOCACY / ADOPTION                       none
NEGATIVES TYPED OR RE-TYPED BY THIS LANE              0
COMPOSITION PERFORMED / OBJECT AUTHORED               none
GAPS FILLED                                           none; COR-K stands
                                                      INDETERMINATE-AT-BYTES
```

### 13.3 Own-draft defects — found by this lane, in this lane's work

**E1 — MY FIRST POPULATION DISAGREED WITH THE TARGET AND I NEARLY CALLED IT AN
ERROR.** My enumeration returned 5,990 against a declared 5,989. Before reporting a
discrepancy I checked mtimes and found `STAGE8_JOIN_FRONTIER_O51SR_V001.md` landed
at 05:16:45, ninety seconds after the target sealed. **The target's count was right
and my first reading of it was wrong.** The same check is what let me confirm its
§2.3 sidecar table, which is also off by exactly the artifacts sealed since.

**E2 — MY FIRST TIER A RECONSTRUCTION WAS LITERAL AND WOULD HAVE PRODUCED A FALSE
REFUTATION.** Literal verbs returned 14,451 against a published 34,513 — a 2.4×
gap that, reported straight, would have read as a fabricated census. Stem and
word-boundary variants closed most of it and one variant reproduced a published
typed count **exactly** (`impossib`, 203). **The gap is a disclosure defect, not a
fabrication, and I graded it COR-F rather than a refutation.**

**E3 — I BRIEFLY GRADED S7 OUTSIDE THE POPULATION AND IT WAS NOT.** `GAMMA_K` has
zero literal core-lexeme hits, which reads as a row invented outside the census.
Testing a broadened negated-existence pattern reproduced the target's TIER A typed
count of 113 exactly and put S7 legitimately in the population. **The correction
travelled toward the target, and I record it because the opposite finding would have
been the more striking one to publish.**

**E4 — COR-C CUTS TOWARD THE TARGET AND I PUBLISHED IT ANYWAY.** Recomputing the age
split on the correct collapsed base does not weaken §6.1; it multiplies its
separation roughly fivefold. A default-refute lane that only published corrections
running against its target would be doing the same selective thing it audits for.

**E5 — MY TIER B LEXICON IS AN AUTHORED INSTRUMENT AND I HAVE SAID SO IN THE IMPORT
AUDIT.** It is published verbatim at §9.1 so a reader can reject it and re-run.
Every grade resting on it is marked INDETERMINATE-AT-BYTES on the exact figure and
CONFIRMED only on direction.

### 13.4 Discipline

- **Q-54 / LOCKED_PROCESS B:** every negative this lane reports carries its type —
  REFUTED (COR-A, COR-B conformity, COR-D, COR-F disclosure) with the deciding bytes
  named; INDETERMINATE-AT-BYTES where the bytes do not decide (COR-K, TIER A/B exact
  tallies). **This lane typed no negative belonging to another artifact and re-typed
  none.**
- **Q-80:** no new class constituted. "bare-only sidecar population" and
  "reconstructed lexicon" are this lane's own display devices, named as such.
- **BARS:** no authoring, no advocacy, no adoption, no performing of any step. Where
  an available step is described — regrading the 5,206, re-running the sample under
  the declared rule, re-typing anything — it is described as available and **not
  taken**. Those are principal acts.
- **PRESSURE, BOTH DIRECTIONS:** the default verdict was REFUTED and it did not
  survive contact with the bytes. Four of the target's strongest claims — the four
  zero-hit propositions, the nine-number seed sweep, the six type-flag counts, and
  the population — were the ones I attacked first and hardest, and every one of them
  held to the unit. The corrections that did land are named, ranked, and each states
  whether the finding survives it.
- **No `git` of any kind.** Artifact and both sidecars written in the archive
  workspace from its own directory. Nothing published.

```text
alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
```
