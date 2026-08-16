# STAGE 8 — THE TYPING PROTOCOL'S COVERAGE: WHAT THE MANDATE SAYS IT COVERS, AND WHAT IT ACTUALLY REACHES — O51SR V001

## BUILD LANE — COMMISSION O51SR — 2026-08-16

```text
alpha_computed        = false [TERMINAL_FENCE_DECLARATION]
proof_authorized      = false [TERMINAL_FENCE_DECLARATION]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION]
```

---

## 0. VERDICT IN ONE LINE

**THE MANDATE'S SCOPE IS STATED, AND IT IS UNIVERSAL — `TYPE EVERY NEGATIVE`
(`LOCKED_PROCESS.md:97`, in corpus, sealed OK). THE PROTOCOL THAT IMPLEMENTS IT
SCOPES ITSELF TO TWO SYNTACTIC FORMS — "every `= false` flag and every 'not
found'". THE GAP BETWEEN THOSE TWO SENTENCES IS THE WHOLE FINDING.** Censused at
bytes, **untyped barriers outnumber typed ones 5,206 to 778 — a ratio of
6.7 : 1** (mirror-collapsed, core lexicon, ±5-line display). The ratio is not a
window artifact: at ±40 lines, 4,190 of the 5,206 are still untyped, and **59.9%
of untyped barriers sit in files that carry no type flag anywhere at all.**

Three further results, each of which cuts against a natural reading:

- **The untyped are NOT older.** July/August split is 18.7 / 81.3 for untyped
  against 20.3 / 79.7 for typed. The "legacy migration backlog" framing the
  corpus uses for its own untyped mass **does not describe this population.**
- **The untyped ARE analytic.** Analytic vocabulary in the barrier line:
  **26.8% of untyped against 8.6% of typed.** The `diverges` lexeme alone runs
  **38.8 : 1 untyped-to-typed**, against ≈5 : 1 for every other lexeme.
- **The gap WAS noticed — but never at this boundary.** Four artifacts quantify
  an untyped mass (372 identifiers; ~1,050 flag lines; 383–457 identifiers), and
  a **ratified ruling institutes partial coverage by name** — `DECISION_OF_RECORD_006`,
  *"Migration is LAZY … No mass re-typing campaign."* **Every one of those
  remarks scopes the gap to `derived = false` flag identifiers.** Not one remarks
  that a barrier stated in prose rather than in flag form is outside the
  protocol's reach.

Of a weighted sample of 10 untyped barriers favouring downstream reliance:
**7 NAMES-AN-ESCAPE · 0 CLEAN · 2 INDETERMINATE-AT-BYTES · 1 NOT-A-BARRIER.**

---

## 1. CHOICE LEDGER

| # | Choice | Alternative not taken | Why |
|---|---|---|---|
| C1 | **The unit of an untyped barrier is a LINE matching a declared barrier lexicon, graded typed/untyped by whether any type flag falls within ±5 lines.** | Reuse the prior commission's unit (`X = false \| TYPE-R` flag form). | The flag form is unavailable by construction: an untyped barrier is precisely one **not** written as a flag. A line-plus-window unit is the only unit that can hold both populations. ±5 matches the seed's own stated method. |
| C2 | **Two lexicon tiers reported, not one.** TIER A is the commission's six verbs verbatim; TIER B drops `fails` and bare `excluded`. | Report only the six verbs. | `fails`/`excluded` are the corpus's process vocabulary ("the test fails", "sweep exclusions") and carry 24,725 of TIER A's 34,513 hits. Reporting only TIER A would inflate the ratio on noise. **Both are shown; the headline uses TIER B.** |
| C3 | **Headline ratio is mirror-collapsed by (basename, line, pattern).** | Raw site counts across both roots. | The two roots duplicate heavily. Raw is 8,021 : 1,383 = 5.8 : 1; collapsed is 5,206 : 778 = 6.7 : 1. **Collapsing moves the ratio against neither side and is reported both ways.** |
| C4 | **Window sensitivity is run and published (±5/±10/±20/±40), not assumed.** | Report ±5 alone. | The single most available attack on this finding is "your window is too tight." It is answered with numbers at §5.3, not with argument. |
| C5 | **`LOCKED_PROCESS.md` is treated as PRIMARY, IN CORPUS.** | Treat the typing mandate as second-hand, as the prior commission did. | It sits at the cleanroom root, which is corpus root B. See §3 — **this reverses a SECOND-HAND marking carried by O46SR.** |
| C6 | **The weighted sample is 10 rows, selected by downstream citation count, and declared as a sample.** | Grade all 5,206. | Whole-span reading of 5,206 sites is not reachable. The selection rule is byte-decidable (distinct basenames containing the source's stem) and the residue is counted, not hidden. |
| C7 | **One sample row is graded NOT-A-BARRIER and kept visible.** | Drop it silently. | `B0_LOAD_BEARING_STOP_SPEC:415` reads *"not a corpus-wide impossibility claim"* — the lexeme fires on a sentence **denying** an impossibility. This is the lexicon's own false-positive mode and burying it would misrepresent the sample. |
| C8 | **Q3 reports co-occurrence only, with an explicit no-inference line under every pattern.** | State the obvious mechanism. | The commission bars it, and the bar is right: the corpus states no dependence for any of these except DoR 006, which is quoted as the one stated dependence. |

---

## 2. CORPUS, BAR, AND SEALS

### 2.1 Roots entered

```text
ROOT A  /Users/bgm/MB Work/alpha-program-archive/workspace
ROOT B  /Users/bgm/Documents/New project/gravity_emergence_evidence_program/
        alpha_fundamental_record_action_cleanroom_v003
PLUS    the TWENTY-EIGHT ratified rulings under
        /Users/bgm/MB Work/alpha-program-archive/supervision/
```

**BOTH RULING CONVENTIONS ENUMERATED, AS REQUIRED.** The standing discipline
warns that a recent commission and the registrar each swept only the `DOR_`
prefix and ran universal negatives over half the rulings. Both prefixes were
listed and all 28 opened:

```text
DOR_NNN_…                 14   DOR_016, 017, 018, 019, 020,
                               020_A1 … 020_A9
DECISION_OF_RECORD_NNN_…  14   003, 004, 005, 006, 007, 008, 009, 010, 011,
                               013, 014, 014_A1, 014_A2, 015
                          ──
                          28   ALL OPENED. Nothing else in that directory
                               entered the corpus.
```

Numbering note, recorded because a later reader will look for it: the
`DECISION_OF_RECORD_` series skips 001, 002 and 012. **28 is the count of files
present, not of a contiguous range**, and no claim here rests on the range being
complete.

Permitted file list after exclusions: **5,989 files** (`.md`, `.txt`, `.json`),
**3,102 distinct basenames**. The prior commission's count was 5,949; the
difference is artifacts landed since, including its own two.

### 2.2 REGISTER BAR — exclusion globs as an ARRAY, per-pattern leak counter

Carried as a Python list, never a string; applied to basenames before any read.

```text
BAR = ['*REGISTER*', '*TRACKER*', 'THE_PLAN*', 'ROAD_REMAINING*',
       'THE_HANDOFF*', 'OBSERVATIONS_REGISTER*', '*DECISION_SHEET*',
       'STAGE8_TYPING_COVERAGE_O51SR_V001.md']          <-- SELF-EXCLUDE
```

Per-pattern counter, run against the raw enumeration:

```text
PATTERN                  | MATCHED | LEAKS INTO PERMITTED LIST
*REGISTER*               |      27 | 0
*TRACKER*                |       0 | 0
THE_PLAN*                |       4 | 0
ROAD_REMAINING*          |       0 | 0
THE_HANDOFF*             |       0 | 0
OBSERVATIONS_REGISTER*   |       0 | 0   (subsumed by *REGISTER*)
*DECISION_SHEET*         |       0 | 0   (the two ACT3_SPEC5_… and
                         |         |      A32_RATIFICATION_… sheets are in
                         |         |      supervision, which contributes only
                         |         |      the 28 rulings — never enumerated)
SELF                     |       0 | 0   [live in every sweep]
                         ───────────
TOTAL BARRED (unique)    |      31
```

`QUESTIONSSETTLED_REGISTER_V001.md` in the second root is caught by `*REGISTER*`
and **was never opened**, as were `DECLINE_REGISTER_V001/V002`, four
`REGISTER_HEAD_SNAPSHOT`/`NAMESPACE_REGISTER` drafts, three
`REGISTER_COMPLETENESS_AUDIT` files, and four `THE_PLAN_TO_ALPHA_AND_GRAVITY`
versions. The self-exclude is live in every sweep, so this artifact cannot read
itself back.

### 2.3 SIDECAR TRAP — both forms probed, convention reported per source

**Both conventions are live in this corpus and neither directory uses one
exclusively.** Every seal below was probed at `<stem>.md.seal.sha256` **and**
`<stem>.seal.sha256` before any file was called unsealed.

```text
DIRECTORY                 <stem>.md.seal.sha256   <stem>.seal.sha256
workspace                          1516                    256
cleanroom_v003                     1217                    242
supervision                         886                      1
```

Verified from each artifact's own directory:

```text
SOURCE                                                    CONVENTION   VERIFY
STAGE8_CERTIFICATION_RULES_O8SR_V001.md                   .md.seal     OK
STAGE8_CERTIFICATION_RULES_O8SR_AUDIT_V001.md             .md.seal     OK
STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md               .md.seal     OK
STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md                  .md.seal     OK
STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC…  .md.seal     OK
STAGE8_GEN_OMEGA_…_ADOPTION_PROPOSAL_V003.md              .md.seal     OK
STAGE8_ALPHA_DEPENDENCY_CLOSURE_CENSUS_EINSTEIN_V001.md   .md.seal     OK
STAGE8_GRAPH_BOUNDARY_WALK_EINSTEIN_V001.md               .md.seal     OK
STAGE8_CANONICAL_IDENTIFIER_REGISTRY_EINSTEIN_V001.md     .md.seal     OK
STAGE8_SOURCE_GERM_PHYS_V002_ADVERSARIAL_REVIEW_DETER….md .md.seal     OK
STAGE8_ACCESSOR_THEOREM_SUBSTITUTION_ADJUDICATION_….md    .md.seal     OK
STAGE8_TYPER_ESCAPES_O46SR_V001.md                        .seal        OK  <-- BARE FORM
STAGE8_TYPER_ESCAPES_O46SR_AUDIT_V001.md                  .seal        OK  <-- BARE FORM
LOCKED_PROCESS.md                                         .md.seal     OK
NEGATIVE_RESULT_TYPING_PROTOCOL_V001.md                   .md.seal     OK
DECISION_OF_RECORD_006_TYPE_P_ADOPTED_LAZY_MIGRATION….md  .md.seal     OK

ALL 28 RATIFIED RULINGS                                   .md.seal     28/28 sealed
```

**The two O46SR artifacts — the direct predecessors of this commission — use the
bare `<stem>.seal.sha256` form.** A probe of only `<stem>.md.seal.sha256` would
have reported the immediate prior work unsealed. That is the trap, and it fires
exactly here.

---

## 3. IMPORT AUDIT

| Import | Source | Status | Does the finding survive without it? |
|---|---|---|---|
| **The typing mandate, `TYPE EVERY NEGATIVE`** | `LOCKED_PROCESS.md:97-99` — **corpus root B**, sealed OK | **PRIMARY, IN CORPUS.** | Not an import. **This reverses O46SR's marking** — see the correction below. |
| **The Q-54 mandate sentence** | `STAGE8_ACCESSOR_THEOREM_SUBSTITUTION_ADJUDICATION_EINSTEIN_V001.md:346` | PRIMARY, in corpus | — |
| **The protocol file's own scope clause and Rule 1** | `NEGATIVE_RESULT_TYPING_PROTOCOL_V001.md:5, 59` — in the supervision directory but **not one of the 28 rulings**, therefore outside the declared corpus | **IMPORT.** Read at bytes and sealed OK. Reported under the standing import discipline: *evaluating a specified structure is not barred; reaching a known answer by distorting it is.* | **YES, WEAKENED IN ONE DIRECTION ONLY.** Without it, Q1 answers "scope stated and universal" from `LOCKED_PROCESS:97` alone, and the §4.3 divergence between the mandate and its implementing rule cannot be shown. **The census, the ratio, Q3 and Q4 are untouched.** |
| **TYPE-P as a fifth type** | `DECISION_OF_RECORD_006` (ratified, in corpus) and `LOCKED_PROCESS:98` | PRIMARY | — |
| **The prior grades (32/43 → 29/44; 0/19 → 0/18)** | `STAGE8_TYPER_ESCAPES_O46SR_V001.md` and its AUDIT | PRIMARY as to those artifacts; **not relied on for any count here.** | Yes — every count in §5 is re-derived from bytes. |
| Logic used | Set difference over basenames; line-window adjacency; counting. **No mathematics of the object domain.** | Named | — |

**A CORRECTION TO THE PRIOR COMMISSION'S IMPORT AUDIT, FOUND AT BYTES.**
`STAGE8_TYPER_ESCAPES_O46SR_V001.md:96` records the FP-2 finding as
*"**SECOND-HAND as to the E1 spec v002 itself**, which is not in the permitted
corpus."* At bytes, `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md` **is present in
both roots** —

```text
/Users/bgm/Documents/New project/…/alpha_fundamental_record_action_cleanroom_v003/STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md
/Users/bgm/MB Work/alpha-program-archive/workspace/STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md
```

— sealed OK, and it carries the C6 barrier verbatim at `:353-358`. **The seed
instance is therefore gradeable at PRIMARY in this commission, not second-hand**,
and §5.4/S1 grades it there. Its `:96` twin about `STAGE8_CERTIFICATION_RULES_O8SR`
was correct; only the E1-spec half is wrong. Nothing in O46SR's tallies turns on
it — the row was excluded from its population for being untyped, which is
independently true and re-derived here.

**No numeric value of any coupling, scale, root, eigenvalue, norm or constant was
computed, approached, or transcribed.** Quoted spans in §5.4 contain symbolic
expressions belonging to their sources; they are reproduced whole for quotation
integrity and nothing was evaluated from them. See §8.1.

---

## 4. Q1 — WHAT IS THE PROTOCOL'S STATED SCOPE?

### 4.1 The mandate — PRIMARY, IN CORPUS, scope stated and UNIVERSAL

`LOCKED_PROCESS.md:95-101`, whole block, verbatim — corpus root B, sealed OK:

```text
A  "HUNT YOUR OWN COUNTEREXAMPLE, AND LEAD WITH IT IF YOU FIND ONE."
B  TYPE EVERY NEGATIVE:  TYPE-R refuted . TYPE-U unbuilt . TYPE-S scope-empty . TYPE-C
                         constraint-blocked CHECKS ONLY . TYPE-P premise-conditional (DoR 006).
                         ONLY TYPE-R IS PHYSICAL CONTENT.
C  NAME THE SYMBOL COLLISIONS THAT BEAR ON THIS QUESTION. Nothing generic.
```

**The scope is `EVERY NEGATIVE`.** It is not restricted by grade, by artifact, by
date, or by form. The same file carries its own non-revision clause at `:112-113`:

```text
*** THIS FILE IS NOT REVISED. IF SOMETHING HERE IS WRONG, IT IS RULED ON BY THE PRINCIPAL AND
REPLACED WHOLE — NOT AMENDED, NOT EXTENDED, NOT VERSIONED. ***
```

Corroborated in corpus at
`STAGE8_ACCESSOR_THEOREM_SUBSTITUTION_ADJUDICATION_EINSTEIN_V001.md:346`, whole line:

```text
- **Q-54:** every negative typed with test, would-build, scope, or release.
```

Four fields, for the four pre-DoR-006 types. `LOCKED_PROCESS:98` adds TYPE-P as a
fifth. **The commission's premise of "four fields" is the pre-2026-08-01 state;
the live scheme has five types plus `NO_VERDICT`.**

### 4.2 The implementing protocol's own scope — IMPORT, and it is NARROWER

`NEGATIVE_RESULT_TYPING_PROTOCOL_V001.md:5`, whole line:

```text
protocol_status = PROPOSED_FOR_ADOPTION; applies to every lane and to the reviewer.
```

That clause scopes the protocol over **agents**, not over statements. The
statement-level scope is Rule 1, `:59`, whole:

```text
1. **Every `= false` flag and every "not found" carries its type.** Untyped negatives are not
   findings.
```

Recorded because it bears against this lane's own reading: `:104` uses the wider
phrasing —

```text
**COSTS:** every negative gets four extra fields.
```

— and `:72` states the burden clause in the widest form of all:

```text
5. *** A NEGATIVE CARRIES THE SAME EVIDENTIARY BURDEN AS A POSITIVE. *** Reporting "not found"
   requires stating the search.
```

**Two byte-level facts about this file must be carried, not glossed.** First, its
status line reads `PROPOSED_FOR_ADOPTION`, while the corpus refers to it as
adopted — `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:131`:
*"The adopted protocol at …"*. **The bytes do not show a ratification of this
file; `LOCKED_PROCESS:97` and DoR 006 carry the live authority.** Second, it sits
in the supervision directory but is **not one of the 28 rulings**, hence outside
this commission's declared corpus — an import, audited at §3.

### 4.3 THE DIVERGENCE — this is the Q1 finding

```text
LOCKED_PROCESS:97          TYPE EVERY NEGATIVE                    <- a SEMANTIC CLASS
PROTOCOL Rule 1 (:59)      every `= false` flag and every         <- TWO SYNTACTIC FORMS
                           "not found"
```

**A statement that something is impossible, diverges, or is excluded, written as
prose and never written as a `= false` flag and never using the words "not
found", satisfies Rule 1 vacuously while standing squarely inside
`TYPE EVERY NEGATIVE`.** The corpus's own instrument law anticipates exactly this
failure mode in a different setting — `LOCKED_PROCESS.md:460-465`, whole:

```text
## THE MEANING-PROBE RULE (2026-08-08, from Q-642 — the sixth scope-class law)

A NEGATIVE EXISTENTIAL is probed by MEANING, not phrase: enumerate the ways
the corpus could state the condition (name-forms, condition-forms, verb-forms)
and probe each — or do not claim absence.
```

**The meaning-probe rule governs how a lane searches for a negative. Rule 1
governs how a lane types one, and it is stated in phrases, not meanings.** The
corpus holds both sentences. It does not anywhere state that the second should be
read under the first; that is left as the reader's inference and is **not drawn
here**.

### 4.4 Stated carve-outs found at bytes

Two exemptions are stated, and neither was invented by this lane.

`STAGE8_SOURCE_GERM_PHYS_V002_ADVERSARIAL_REVIEW_DETERMINATION_V001.md:474-489`,
whole span including the adverse clause:

> V002 contains seven nonterminal bare `false` occurrences representing six
> distinct claims: […] The terminal fence declarations at `:409-411` are exempt.
> The six claims above are not. LOCKED_PROCESS/Q-54 requires every negative to
> carry TYPE-R/U/S/C/P. This is a record-typing defect, not a physical failure,
> but it must be repaired before a principal ratifies the artifact.

Two things are visible there at once: **a stated exemption** (terminal fence
declarations), **a stated scope word** (`nonterminal`), and **a lane treating an
untyped bare `false` as a defect requiring repair** — which is the protocol
working, at the flag form. The corresponding flag appears in corpus as
`Q54_NONTERMINAL_NEGATIVE_TYPING_COMPLETE = true`
(`STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V003.md:189`, verified at the cited
line).

The second carve-out is ratified, and it is quoted whole at §7.1.

---

## 5. Q2 — THE UNTYPED-BARRIER CENSUS

### 5.1 Population and patterns, declared

```text
POPULATION      5,989 files (.md .txt .json), both roots + the 28 rulings,
                after the §2.2 bar. 3,102 distinct basenames.
UNIT            one LINE matching a barrier pattern.
DISPLAY         +-5 lines, matching the seed's own stated method.
TYPE FLAG       TYPE-R | TYPE-U | TYPE-S | TYPE-C | NO_VERDICT
                (TYPE-P added for the §5.3 sensitivity run)
TYPED           a barrier line with >=1 type flag inside its display.
UNTYPED         a barrier line with none.
```

**TIER A — the commission's six verbs, verbatim, no suppression:**

```text
PATTERN            TYPED   UNTYPED     TOTAL
cannot-exist         113       511       624
fails              1,404    17,042    18,446
diverges              62     1,789     1,851
excluded             622     5,657     6,279
impossible           203       964     1,167
refuted            1,048     5,098     6,146
────────────────────────────────────────────
TOTAL              3,452    31,061    34,513      ratio  9.0 : 1
```

**TIER B — CORE. `fails` and bare `excluded` dropped as process vocabulary;
`ruled out` and `no X can` added; sweep/exclusion bookkeeping lines suppressed:**

```text
PATTERN            TYPED   UNTYPED   ratio U:T      (mirror-collapsed)
cannot-exist          70       360      5.1 : 1
impossible           113       561      5.0 : 1
diverges              32     1,241     38.8 : 1   <-- the outlier
refuted              538     2,856      5.3 : 1
ruled-out              4        29      7.2 : 1
no-X-can              21       159      7.6 : 1
──────────────────────────────────────────────
TOTAL                778     5,206      6.7 : 1   <-- HEADLINE
raw (uncollapsed)  1,383     8,021      5.8 : 1
```

**FOR CONTEXT — the protocol's own unit**, re-derived here across all five types:

```text
flag-form typed-negative SITES               10,827
distinct identifiers so typed                 4,109
```

(The prior commission found 4,602 sites / 1,939 identifiers for `TYPE-R` alone;
these are consistent, this run covering four further flags.)

### 5.2 THE RATIO, STATED PLAINLY IN BOTH DIRECTIONS

**Untyped barriers outnumber typed barriers 5,206 to 778 — 6.7 : 1 — and
excluding `refuted` (which is protocol-commentary-heavy, since a TYPE-R *is* a
refutation and the corpus says so constantly) the ratio is 2,350 : 240 =
9.8 : 1.**

**What this does NOT say, and the distinction is the whole of the honesty here:**
it does not say 5,206 findings escaped adjudication. A barrier line is not a
finding; many are restatements, table cells, quotations of other artifacts, and
summary headlines standing above flag blocks that *are* typed further down. **The
claim the numbers support is narrower and it is enough:** the protocol's coverage
is *not* co-extensive with the class its mandate names, the shortfall is roughly
an order of magnitude, and it is **not concentrated in old files**.

### 5.3 WINDOW SENSITIVITY — run, because it is the obvious attack

```text
DISPLAY WINDOW     UNTYPED (mirror-collapsed)   fall from +-5
+-5                        5,206                     —
+-10                       4,881                   -6.2%
+-20                       4,549                  -12.6%
+-40                       4,190                  -19.5%

UNTYPED sites in a file that types SOMETHING somewhere    2,088   (40.1%)
UNTYPED sites in a file with NO type flag anywhere at all  3,118   (59.9%)
```

**Widening the display eightfold removes under a fifth of the population, and
three in five untyped barriers sit in files that type nothing at all.** The
finding is not an artifact of the window.

### 5.4 THE WEIGHTED SAMPLE — 10 rows, favouring downstream reliance

Selection rule, byte-decidable: for each basename carrying ≥1 untyped core
barrier, count the distinct **other** basenames in the population containing its
stem. Sample drawn from the top of that ranking. Top of the ranking, published:

```text
CITES  UNTYPED  BASENAME
  258        7  LOCKED_PROCESS.md
  232       10  BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md
  102        6  STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V012.md
   94        4  STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V003.md
   90      136  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md
   70        2  STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md
   65        2  STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md
   53       14  STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md
```

Graded exactly as the typed ones were: **read at the barrier and in the text
immediately following it.**

---

**S1 · THE SEED INSTANCE, AT PRIMARY — `NAMES-AN-ESCAPE` (CLASS-DISPLAYED-VIABLE)**
`STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:353-358`, whole, sealed OK:

> C6  THE BLOCK IS CONFINED TO n = 1 — AND ITS LOCUS IS THE VOLUME DIAGONAL.
>     Equal-time localization of the 3-D massless Dirac sea fails
>     Shale-Stinespring: ||[C, 1_B]||_2 = +infinity; a Lipschitz cutoff still
>     gives int d^3 r · r^2/r^6 = int dr/r^2, divergent. Only TWO-TIME /
>     scattering-type objects, where the cell time integration supplies the
>     missing decay, can work.

The escape is the barrier's own last sentence. **Adverse clause, carried because
quotation integrity requires it** — the very next lines narrow a *different*
candidate escape, `:359-366`:

> *** LOCUS REFINEMENT, ADOPTED OF RECORD (binding R5, from the independent
> system): THE FATAL LOCAL INTEGRAL IS THE VOLUME DIAGONAL x = y, NOT THE
> SHARP BOUNDARY. SMOOTHING ONLY THE BOUNDARY WILL NOT REMOVE A |x-y|^-3
> POSITIVE MAJORANT. *** […] THIS BEARS DIRECTLY ON Q2: a
> smoothed-localizer successor MAY NOT FIX THE OBSTRUCTION AT ALL

**The source names one kind that can work and one kind that may not. A consumer
reading only the first half or only the second would be wrong in opposite
directions.** Type flag within ±5 lines: **none.**

---

**S2 · `IMPOSSIBILITY 1 — THE OPERATOR-NORM EXCLUSION` — `NAMES-AN-ESCAPE`**
`STAGE8_CERTIFICATION_RULES_O8SR_V001.md:586-590`, whole:

> IMPOSSIBILITY 1 — THE OPERATOR-NORM EXCLUSION.  ||[h_0, 1_B]|| = +infinity,
>   mechanism-exact (CERT §3.4: surface-distribution type; the L^2 witness
>   family; the form does not extend to L^2).  QUANTIFIER: **the operator-norm
>   type.**  It excludes ONE type.  DERIVED, and it is the one place at FP-3
>   where mathematics genuinely closes a door.

The quantifier is displayed and it is one type; the escape is the complement.
**The adverse clause is in the same breath — *"the one place at FP-3 where
mathematics genuinely closes a door"* — and is quoted rather than trimmed.**

---

**S3 · `IMPOSSIBILITY 2 — THE SEA-SANDWICH OBSTRUCTION` — `NAMES-AN-ESCAPE`**
`STAGE8_CERTIFICATION_RULES_O8SR_V001.md:591-598`, whole:

> IMPOSSIBILITY 2 — THE SEA-SANDWICH OBSTRUCTION (W-3 §4).  C h_0 C is a
>   NONZERO TRANSLATION-INVARIANT multiplier, hence not compact, hence not HS.
>   QUANTIFIER: **translation-invariant inputs.**  W-3's own escape clause says
>   so: "the only way past is an INPUT that is NOT translation-invariant."
>   AND TRANSLATION-INVARIANCE IS EXACTLY WHAT F3-b GUARANTEES: H(c)'s defining
>   functional reads psi ONLY through ||h_0 psi|| and ||psi||, both invariant,
>   so H(c) assigns the SAME bound to a state and to all its translates
>   [CAS R1a/R1b].  THE THEOREM'S HYPOTHESIS IS SUPPLIED BY THE ADMISSION RULE.

The source uses the words *"escape clause"*. **The adverse half is the last three
lines and it matters: inside the admitted class the escape is unavailable,
because the admission rule supplies the theorem's hypothesis.** Both halves are
in one untyped block.

---

**S4 · `IMPOSSIBILITY 3 — THE GRONWALL ESCALATION` — `NAMES-AN-ESCAPE` (block-level)**
`:599-601` and its block conclusion `:609-613`, both whole:

> IMPOSSIBILITY 3 — THE GRONWALL ESCALATION (W-3 §7).  Its own headline names
>   its quantifier: "THE CERTIFIED CLASS IS NOT CLOSED UNDER ITS OWN
>   PROPAGATION GRONWALL."  A statement ABOUT THE CLASS, verbatim.

> AND THE RECORD SAYS THE CONCLUSION IN ITS OWN WORDS (W-3 §8, verbatim):
>   "(o4) — 'Supplies S2b' — is now shown to be NOT A CONSEQUENCE of (o1)-(o3)
>    AT ANY STRENGTH.  Therefore W-3 CANNOT LAND ON C-L2's OWN PERMITTED ROUTE
>    ALONE: its landing requires an input from OUTSIDE THE FORM CLASS."
>   "OUTSIDE THE FORM CLASS" IS THE ADMISSION RULE'S NAME FOR ITS OWN BOUNDARY.

**Declared limitation of this grade: the escape is stated for the FP-3 block, not
for impossibility 3 in its own three lines.** Graded NAMES-AN-ESCAPE on the
immediately-following-text rule, with that qualification on the record.

---

**S5 · `IMPOSSIBILITY 4 — THE beta KERNEL FACT` — `NAMES-AN-ESCAPE` (block-level)**
`:602-608` displays its quantifier — *"**objects whose cell-dependence is
constant** — and the constancy is CERT u-b, which is the admission rule's own
doing"*. The affirmative non-exclusion is at `:619-623`, whole:

> CLASSIFICATION [DERIVED]: **RULE-IMPOSED.**  Exactly one of the four
>   impossibilities (no. 1) excludes a type outright; the other three each
>   quantify over the admitted class or over objects with a property the
>   admission rule supplies.  No impossibility is displayed for an object of
>   the required kind as such.

Same declared limitation as S4: block-level, not row-level.

---

**S6 · `F1-b` AT FP-1 — `NAMES-AN-ESCAPE`, the strongest in the sample**
`STAGE8_CERTIFICATION_RULES_O8SR_V001.md:508-515`, whole:

> THE DISPLAYED IMPOSSIBILITY (F1-b): re-derived here exactly.
>   rank x op delivers 4n^3 · k against an n-FREE target; against any same-power
>   carrier object (2n^3) the ratio is 2k — n-free, constant, never o(1)
>   [CAS R4a/R4b].  THIS IS REAL AND EXACT.
> ITS QUANTIFIER: **the rank x op ROUTE.**  It says that ONE conversion cannot
>   close.  It says nothing about the existence of a sub-volume trace/HS rate.
> IS AN OBJECT OF THE REQUIRED KIND EXCLUDED?  **NO — and the record positively
>   derives the opposite.**

**The source asks the over-reading question of itself and answers it.** No type
flag in the display.

---

**S7 · `The required Hamilton-Jacobi conjugate energy does not exist yet` — `NAMES-AN-ESCAPE` (WOULD-BUILD-NAMED)**
`STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md:316-321`, whole:

> Scope for this negative: this claim is scoped to the cited
> `BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md` status block and the
> readiness record quoted in Section 2.1; it is not a corpus-wide search claim.
> The required Hamilton-Jacobi conjugate energy does not exist yet. It must be
> specified and derived as part of the stationary cell target; this spec does
> not choose Misner-Sharp or Brown-York.

**Worth naming precisely: this negative carries a scope paragraph, a would-build,
and a refusal to select — every field the protocol asks of a TYPE-S/TYPE-U row —
and carries no type flag.** It is a fully disciplined untyped negative. The
shortfall here is notation, not rigour, and saying otherwise would be unfair to
the source.

---

**S8 · `an impossible equality between a positive fidelity metric and the indefinite Lorentz bivector form` — `INDETERMINATE-AT-BYTES`**
`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:55-56`. The line is item ~6 of a
long defect enumeration (`:50-62`); the lines before and after it are further
defect items. **Neither an escape nor a closing is displayed** — the display is a
list, not an adjudication.

---

**S9 · `THREE SPECIFIC TRANSPORTS REFUTED` — `INDETERMINATE-AT-BYTES`, and it exposes a real sub-class**
`STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V003.md:177`:

> **RESULT: NO SEALED ANCHOR DERIVATION; THREE SPECIFIC TRANSPORTS REFUTED**

The headline is untyped at ±5. **Its body is typed** — `:242`, `:245`, `:273`
carry `= false | TYPE-R` with `test:` fields, at 65–96 lines' distance. **This is
a genuine and previously unnamed sub-class of the untyped population: SUMMARY
HEADLINES STANDING OVER TYPED BODIES.** They inflate an untyped count without
representing an untyped adjudication. This lane found the sub-class in its own
sample and reports it against its own ratio; §5.3's file-level figure (40.1% of
untyped sites sit in files that type something) is the honest bound on how large
it could be.

---

**S10 · `not a corpus-wide impossibility claim` — `NOT-A-BARRIER`**
`STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md:414-415`, whole:

> The second line is bounded evidence for exactly two recovered standalone
> families, not a corpus-wide impossibility claim.

The lexeme fires on a sentence **denying** an impossibility. **This is the
lexicon's false-positive mode**, kept visible rather than dropped. The sibling at
`:1065` — *"This is a graph-direction refutation, not a physical impossibility
claim."* — is the same kind.

### 5.5 SAMPLE TALLY

```text
POPULATION: 10 untyped core barriers, selected by downstream-citation rank,
            read at the barrier and at the text immediately following it.
            DECLARED SAMPLE of 5,206. Residue: 5,196, not read.

NAMES-AN-ESCAPE            7 / 9 graded   (78%)
  CLASS-DISPLAYED-VIABLE     6
  WOULD-BUILD-NAMED          1
CLEAN                      0 / 9          ( 0%)
INDETERMINATE-AT-BYTES     2 / 9          (22%)
NOT-A-BARRIER              1 of the 10, excluded from the denominator (S10)
```

**Set against the typed population's corrected 29/44 = 66%: the sampled untyped
barriers name an escape at least as often as the typed ones do — 7 of 9 against
2 of 3. Nothing in this sample suggests untyped barriers are more absolute; if
anything the reverse, and the sample is far too small to claim even that.** The
declared residue is 5,196 rows and **no rate is extrapolated onto it.**

---

## 6. Q3 — DO THE UNTYPED ONES DIFFER FROM THE TYPED ONES?

**Co-occurrence only. Under every pattern below, the no-inference statement is
stated in full and it is not decoration.**

### 6.1 AGE — NO SIGNAL. The natural hypothesis fails.

```text
                 2026-07        2026-08
TYPED       281  (20.3%)   1,102  (79.7%)
UNTYPED   1,499  (18.7%)   6,522  (81.3%)
```

**These co-occur; the corpus states no dependence.** And the co-occurrence is
*null*: the untyped population is, if anything, marginally **younger** than the
typed one. **This is the finding that most needed to come out negative and did.**
The corpus's own framing of its untyped mass — "pre-Q-54", "legacy", "lazy
migration" (§7) — describes a backlog of old flags. **It does not describe the
population censused here.**

*Method disclosure:* month is **filesystem mtime**, which is metadata, not corpus
content, and is disturbed by mirror copying. It is declared as a proxy and no
claim rests on any individual file's date — only on the two distributions being
indistinguishable, which is robust to per-file error.

### 6.2 ARTIFACT KIND — SIGNAL. Typed tracks deciding; untyped tracks reviewing.

```text
BASENAME TOKEN            TYPED (n=778)      UNTYPED (n=5,206)
_AUDIT                     77   ( 9.9%)      1,042   (20.0%)   <-- 2.0x untyped
_SPEC                      82   (10.5%)        233   ( 4.5%)   <-- 2.3x typed
DETERMINATION              83   (10.7%)        225   ( 4.3%)   <-- 2.5x typed
PROPOSAL                   48   ( 6.2%)        154   ( 3.0%)   <-- 2.1x typed
_CHECK                     56   ( 7.2%)        420   ( 8.1%)
_RESULT                    18   ( 2.3%)         79   ( 1.5%)
RULE/PRINCIPLE/PROCESS     17   ( 2.2%)        158   ( 3.0%)
DOR / ratified ruling       3   ( 0.4%)          9   ( 0.2%)
```

**These co-occur; the corpus states no dependence.** Barriers in artifacts that
*decide* something — specs, determinations, adoption proposals — carry a type
flag about twice as often as barriers in artifacts that *review* something.

### 6.3 SUBJECT MATTER — THE STRONGEST SIGNAL, and it is analytic-vs-combinatorial

Vocabulary present in the barrier line itself:

```text
                        TYPED (n=778)      UNTYPED (n=5,206)
analytic-only         67   ( 8.6%)      1,396   (26.8%)    <-- 3.1x untyped
combinatorial-only    34   ( 4.4%)        104   ( 2.0%)    <-- 2.2x typed
both                   3                    25
neither              674   (86.6%)      3,681   (70.7%)

analytic     = integral|integrat|diverg|norm|operator|Hilbert|Schmidt|spectr|
               kernel|measure|continuum|analytic|Sobolev|resolvent|majorant|asymptot
combinatorial= graph|cycle|incidence|simplic|combinator|vertex|edge|face|lattice|
               finite set|cardinal|enumerat|groupoid|pushout|colimit
```

And the single-lexeme ratio from §5.1 points the same way with no vocabulary
proxy at all:

```text
diverges          38.8 : 1  untyped-to-typed
every other core lexeme   5.0 – 7.6 : 1
```

**These co-occur; the corpus states no dependence.** The commission asked whether
untyped barriers are "analytic rather than combinatorial". **At bytes, on two
independent measures, they are** — and the seed instance is itself an analytic
divergence barrier, sitting in the sub-class with the worst coverage in the
corpus. **That the confirmed instance falls in the worst-covered class is a
co-occurrence and is reported as one. This lane does not infer that being
analytic causes a barrier to go untyped, and the corpus nowhere states it.**

### 6.4 INHERITED vs DERIVED — NO SIGNAL

```text
Barrier sits in a file carrying frozen/inherited-input vocabulary
  ("FROZEN INPUT" | "inherited" | "EXTERNAL INPUT" | "independent system"
   | "binding verbatim")

TYPED     277 / 778     (35.6%)
UNTYPED 1,924 / 5,206   (37.0%)
```

**These co-occur; the corpus states no dependence.** And again the co-occurrence
is null. **The hypothesis that untyped barriers are systematically the inherited
ones is not supported at bytes**, even though the commission's own seed instance
is an inherited one. A single instance's provenance does not reproduce as a
population property, and this lane records that its seed's most salient feature
turns out **not** to be the distinguishing one.

### 6.5 LOAD-BEARING vs INCIDENTAL — NOT DETERMINED

The commission asks whether untyped barriers are load-bearing rather than
incidental. **This lane could not settle it at bytes and does not guess.** The
citation ranking at §5.4 measures reliance on the *artifact*, not on the
*barrier*; the corpus contains no barrier-level citation graph (the prior
commission established the same absence for TYPE-R rows). **INDETERMINATE-AT-BYTES.**

### 6.6 THE ONE STATED DEPENDENCE

Every pattern above is bare co-occurrence with one exception, and it is ratified.
It is quoted whole at §7.1: **DoR 006 states that typing-scheme migration is
deliberately partial and keyed to when an artifact is next touched.** That is a
stated dependence of coverage on artifact-touch, and it is the only one in the
corpus. **It governs the TYPE-C → TYPE-P re-typing, not the base mandate**, and
it is not extended here beyond its own words.

---

## 7. Q4 — WAS THE COVERAGE GAP EVER NOTICED?

**YES — repeatedly, quantified, and once ratified. But never at the boundary this
commission is about.** Both halves are stated, and the second is the finding.
Scale of the noticing: **82 distinct artifacts in the permitted corpus carry the
token `untyped`** (excluding the two O46SR artifacts). The corpus is not unaware
of untyped negatives; §7.4 states exactly what it is aware *of*.

### 7.1 RATIFIED: partial coverage is instituted by name

`DECISION_OF_RECORD_006_TYPE_P_ADOPTED_LAZY_MIGRATION_2026-08-01_V001.md:6-14`,
whole, sealed OK — one of the 28:

> ## THE DECISION
>
> TYPE-P is ADOPTED for premise-conditional claims. TYPE-C returns to CONSTRAINT-BLOCKED CHECKS ONLY.
> Migration is LAZY: new artifacts use the new scheme immediately; the 487 existing TYPE-C mentions
> are re-typed only when their artifact is next touched. No mass re-typing campaign.
>
> Typing scheme from this ruling forward:
>   TYPE-R refuted . TYPE-U unbuilt . TYPE-S scope-empty . TYPE-C constraint-blocked (checks only) .
>   TYPE-P premise-conditional . NO_VERDICT legal. Only TYPE-R is physical content.

**"No mass re-typing campaign" is a ratified acceptance that typing coverage will
be partial and uneven.** Its scope is the C→P migration of 487 mentions, and it
is not read here as governing anything wider.

### 7.2 QUANTIFIED: the corpus counts its own untyped mass, four times

`STAGE8_GRAPH_BOUNDARY_WALK_EINSTEIN_V001.md:51-56`, whole (sealed OK):

> ## §2 — THE UNTYPED MASS IS NOW A NUMBER: 372 IDENTIFIERS, ~17% LIVE
>
> DISTINCT UNTYPED IDENTIFIERS: 372 (the sweep's 361 + 11 recovered by the verifier from a
> first-match-per-line extractor bug — all 11 verified UNKNOWN; the bug did not touch the LIVE
> set). OCCURRENCES: 1,176 (972 workspace + 204 supervision; cleanroom adds nothing non-mirror).

`STAGE8_ALPHA_DEPENDENCY_CLOSURE_CENSUS_EINSTEIN_V001.md:34-36`, whole:

> PLUS the
> untyped mass, counted separately per the charter: ~1,050 pre-Q-54 "derived = false" flag
> lines ≈ 350 distinct identifiers with no would-build (UNTYPED-LEAF).

`STAGE8_CANONICAL_IDENTIFIER_REGISTRY_EINSTEIN_V001.md:66-76`, whole span
including its adverse clause:

> ## §2 — THE COLLISION SWEEP OVER THE UNTYPED MASS
>
> WITHIN the line-anchored untyped 'derived = false' population (383-457 identifiers depending on
> pattern width; see item-3 artifact for the governed count): ZERO case/separator/plural/suffix/
> reorder collisions. […]
>   F1  FULL_SOURCE_RECORD_FIELD_CTP_PRODUCER_DERIVED (untyped, TYPING_TESTS :98/:459) vs
>       full_source_record_field_CTP_producer_derived = false | TYPE-U (typed, on a blocked_by-
>       prefixed line the anchored pattern cannot match, THEORY_001 :157). A CASE-FOLD DOUBLET
>       MIXING TYPED AND UNTYPED

That same file, `:29-32`, contains the closest thing in the corpus to the present
finding, and it is stated as an aside about **naming**, not about coverage:

> THE NAMESPACE IS CLEANER THAN FEARED, NOT COLLISION-FREE: zero spelling collisions inside the
> line-anchored untyped population; TWO collision families outside that regex scope (below); 18
> identifiers confirmed ONE-NAME across eras; the disease's worst instances are prose-vs-flag,
> not flag-vs-flag.

**"Prose-vs-flag" names the exact boundary — but as an aliasing hazard, not as a
typing-coverage hazard.** The corpus has the distinction and does not apply it to
the protocol's reach.

### 7.3 AT THE FLAG FORM: a lane treats untyped negatives as a defect

`STAGE8_SOURCE_GERM_PHYS_V002_ADVERSARIAL_REVIEW_DETERMINATION_V001.md:472-489`
(quoted whole at §4.4) opens a section headed **"Untyped negative regression"**,
enumerates six untyped claims, and calls them *"a record-typing defect … it must
be repaired before a principal ratifies the artifact."* **The protocol's
enforcement machinery exists and works — on bare `false` flags.**

Also `STAGE8_INGREDIENT_CENSUS_O17SR_AUDIT_V001.md:239-243`, whole:

> §7's own words are "Each verified by `shasum -a 256 -c <sidecar>` ... **before any
> reliance on its content**." Five artifacts were verified and then not relied on,
> not typed, and not disclosed as untyped. Three of the five sit squarely in the
> categories this commission named as answer-inverting.

### 7.4 THE ANSWER, STATED EXACTLY

**Every coverage remark in the corpus scopes the gap to `derived = false` /
bare-`false` FLAG IDENTIFIERS.** 372 identifiers; ~1,050 flag lines; 383–457
identifiers; 487 TYPE-C mentions; six bare `false` occurrences. **Every one is a
count of flags awaiting a type — a migration backlog.**

**No artifact in the permitted corpus states that a barrier written as prose, and
never written as a flag, is outside the typing protocol's reach.** The sweep for
that proposition returns nothing:

```text
"coverage of the typing"    0 hits      "escaped typing"           0 hits
"typing … coverage"         0 hits      "outside the protocol"     0 hits
"partial coverage"          0 hits      "protocol … not applied"   0 hits
```

**The sole exception is this commission's own predecessor**, and it says it in
two sentences, both of which this lane confirms at bytes —
`STAGE8_TYPER_ESCAPES_O46SR_V001.md:636-641`, whole:

> **Zero.** The one barrier known to have been consumed downstream as a general
> wall where its source drew a door **was never run through the Q-54 typing
> protocol**. It entered as an untyped impossibility sentence in a frozen external
> input and was consumed as such.
>
> This is not a defect of TYPE-R. It is the boundary of TYPE-R's coverage.

**So: the coverage gap was noticed, on 2026-08-16, once, by the immediately
preceding commission — and it was noticed as a property of one instance, not of a
population. Before that artifact, the corpus's twelve remarks about untyped
negatives are all about flags awaiting migration. The population this artifact
censuses had never been counted.**

### 7.5 THE SEED INSTANCE, RE-DERIVED AND STRENGTHENED

The predecessor checked `TYPE-R` only. **This lane re-ran it over all five type
flags plus `NO_VERDICT`**, which is the stronger test and the one that could have
overturned the result:

```text
SWEEP: is the C6 barrier typed under ANY flag anywhere in the permitted corpus?
  raw files containing "Shale-Stinespring"                      27
  distinct basenames                                            19
  occurrences                                                   52
  ANY of TYPE-R/U/S/C + NO_VERDICT within +-5 lines             10
    of which inside the two O46SR commission artifacts —
    i.e. inside artifacts ABOUT the gap, not typings of it      10
  ────────────────────────────────────────────────────────────────
  GENUINE TYPINGS OF THE BARRIER                                 0
```

```text
"Equal-time localization"   9 basenames, 17 occurrences,  1 near-hit
                            (that 1 is O46SR itself)  -> 0 genuine
"FP-2"                     35 basenames, 356 occurrences, 10 near-hits
                            (9 in O46SR, 1 in an unrelated audit) -> 0 genuine
```

**Confirmed and strengthened. The result does not depend on the restriction to
TYPE-R.** Count discrepancy declared: the predecessor reported 25 files; this run
finds 27 raw files / 19 basenames — two artifacts landed since, both of them its
own.

---

## 8. SWEEP CUTOFFS — PATTERN, HITS, LEAK COUNTER

Every sweep was executed. Counts are actual.

| # | Pattern / rule | Scope | Hits | Leaks |
|---|---|---|---|---|
| S1 | file enumeration `*.md *.txt *.json` minus BAR array | both roots + 28 rulings | **5,989 files** / 3,102 basenames | 0 (per-pattern table §2.2) |
| S2 | ruling enumeration, **both prefixes** | supervision | `DOR_` 14 + `DECISION_OF_RECORD_` 14 = **28**, all opened | 0 non-ruling files entered |
| S3 | type-flag tokens | population | R 6,570 / U 9,767 / S 3,404 / C 1,300 / NO_VERDICT 3,130 / P 4,199 | — |
| S4 | flag-form typed-negative sites (incl. value-on-next-line) | population | **10,827 sites / 4,109 identifiers** | — |
| S5 | TIER A barrier lexicon (6 patterns) | population | **34,513** (3,452 typed / 31,061 untyped) | — |
| S6 | TIER B core lexicon (6 patterns), process lines suppressed | population | **9,404** raw → **5,984** mirror-collapsed | — |
| S7 | window sensitivity ±5/±10/±20/±40 | the 5,206 | 5,206 / 4,881 / 4,549 / 4,190 | — |
| S8 | file-level type-flag presence | the 5,206 | 2,088 in typing files / 3,118 in files typing nothing | — |
| S9 | downstream-citation rank by stem containment | 1,107 basenames | top-8 published §5.4 | — |
| S10 | `Shale-Stinespring` / `Equal-time localization` / `FP-2` × 6 flags, ±5 | population | 52 / 17 / 356 occ; **0 genuine typings** | 10 / 1 / 10 near-hits each opened and attributed |
| S11 | Q4 coverage-remark set (14 patterns) | population | 0/0/0/3/5/0/15/**284**/2/1/35/55/0/0 | the 284 `untyped` hits reviewed; §7 quotes the substantive ones |
| S12 | typing tokens across the 28 rulings | supervision | **9 of 28** carry any; 19 carry none | 0 |
| S13 | seal probe, **both sidecar forms**, 16 named sources + 28 rulings | own directories | **44/44 OK**; 2 sources use the bare form | 0 |
| S14 | Q3 vocabulary proxies (analytic 16 / combinatorial 15 / inherited 5) | the 5,984 | §6.3, §6.4 | — |

**DECLARED CUTOFFS — two, and both discard evidence.**

1. **§5.4 grades 10 of 5,206.** The residue of 5,196 is counted, not hidden, and
   **no grade rate is extrapolated onto it.**
2. **TIER A's `fails` and bare `excluded` (24,725 hits) are excluded from the
   headline.** They are reported in full at §5.1 rather than dropped, so a reader
   who disagrees with C2 can compute the 9.0 : 1 figure instead of the 6.7 : 1
   one. **Neither choice changes the direction of the finding.**

**RECONCILIATION AGAINST MY OWN SWEEP BLOCK, AS REQUIRED BEFORE SEALING.** My
headline says untyped barriers outnumber typed ones ~6.7 : 1 and that the gap is
analytic, not old. S6 gives the ratio; S7/S8 show it survives an eightfold window
widening; §6.1 gives the null age result; §6.3 gives the analytic signal on two
independent measures. **Headline and evidence agree.** The headline does **not**
say 5,206 adjudications escaped the protocol — S9's own sample found the
summary-headline sub-class (§5.4/S9) that inflates any such reading, and S8
bounds it at 40.1%. **What the evidence supports is exactly: the protocol's
coverage falls roughly an order of magnitude short of the class its mandate
names; the shortfall is not explained by age or by inheritance; and it
concentrates in analytic barriers and in reviewing artifacts.**

---

## 9. FLAG BLOCK

### 9.1 Fences

```text
alpha_computed        = false   [held; no coupling value approached]
proof_authorized      = false   [held; nothing proved, nothing authored]
kappa_record_computed = false   [held]
```

No numeric value of any coupling, scale, root, eigenvalue, norm, or constant was
computed, transcribed, or approached. Quoted spans in §5.4 contain symbolic
expressions belonging to their sources (`||[C, 1_B]||_2 = +infinity`,
`int d^3 r · r^2/r^6 = int dr/r^2`, `||[h_0, 1_B]|| = +infinity`, `4n^3 · k`,
`2n^3`). **These are quoted spans of other artifacts, reproduced whole because
quotation integrity requires the adverse clauses around them.** Nothing was
evaluated, compared, or approached from any of them. Every number appearing in
this artifact's own voice is a **count of text occurrences**.

### 9.2 Bar incidents

```text
BARRED FILES OPENED                                   0
  QUESTIONSSETTLED_REGISTER_V001.md (second root)     NOT OPENED (caught by *REGISTER*)
  DECLINE_REGISTER_V001/V002, REGISTER_HEAD_SNAPSHOT
    x2, NAMESPACE_REGISTER_DRAFT x4,
    REGISTER_COMPLETENESS_AUDIT x3, and 4 others      NOT OPENED (27 total)
  THE_PLAN_TO_ALPHA_AND_GRAVITY_V001..V004            NOT OPENED (4 total)
  any *TRACKER*, ROAD_REMAINING*, THE_HANDOFF*,
    *DECISION_SHEET*                                  NOT OPENED (leak counters 0)
SELF-EXCLUSION                                        LIVE in every sweep
SUPERVISION DIRECTORY                                 the 28 rulings opened;
                                                      NEGATIVE_RESULT_TYPING_PROTOCOL_V001.md
                                                      opened as a DECLARED IMPORT (§3),
                                                      not as corpus. No other file
                                                      there opened.
AUTHORING / ADVOCACY / ADOPTION                       none
NEGATIVES TYPED OR RE-TYPED BY THIS LANE              0
GAPS FILLED                                           none; 2 sample rows and all of
                                                      §6.5 stand INDETERMINATE-AT-BYTES
```

One boundary note, and it is the reason §3 carries a survival column: this lane
**opened** `NEGATIVE_RESULT_TYPING_PROTOCOL_V001.md`, which the predecessor
declined to open and marked SECOND-HAND. The import discipline permits evaluating
a specified structure, and Q1 asks for the scope quoted whole, which cannot be
answered from a second-hand fragment. **The provenance is declared, the file is
sealed OK, and §3 states exactly which sentence of this artifact would be lost
without it — one, in §4.3.**

### 9.3 Own-draft defects — found by this lane, in this lane's work

**D1 — MY FIRST LEXICON WOULD HAVE REPORTED 9.0 : 1 ON NOISE.** The commission's
six verbs, run verbatim, put 24,725 of 34,513 hits on `fails` and `excluded` —
overwhelmingly the corpus's process vocabulary ("the test fails", "sweep
exclusions", "excluded from the denominator"). Reporting TIER A as the headline
would have been the stronger-sounding number and the emptier one. **TIER B is
narrower and the finding survives it.** Both are published.

**D2 — MY FIRST POPULATION EXCLUDED `.json` AND UNDERCOUNTED BY 40 FILES.** The
predecessor's population is `.md .txt .json` = 5,949; my first enumeration used
`.md .txt` = 4,310 and was not comparable to the figure I intended to reconcile
against. Corrected to 5,989 before any count was taken.

**D3 — I NEARLY MISSED THAT LOCKED_PROCESS IS IN CORPUS.** The mandate is cited
throughout the corpus as living at `/Users/bgm/MB Work/alpha_supervision/`, which
is outside the declared roots, and the predecessor marked the whole protocol
SECOND-HAND on that basis. `LOCKED_PROCESS.md` also sits at the **cleanroom
root**, which is corpus root B. **Had I not checked, Q1 would have been answered
entirely from an import**, and the strongest quotation in this artifact — `TYPE
EVERY NEGATIVE` — would have been marked second-hand for no reason.

**D4 — THE SUMMARY-HEADLINE SUB-CLASS CUTS AGAINST MY OWN RATIO, AND I FOUND IT
IN MY OWN SAMPLE.** S9 (`GEN_OMEGA:177`) is an untyped headline sitting 65–96
lines above a properly typed flag block. Any count of untyped *lines* includes
such headlines and overstates the number of untyped *adjudications*. **Declared
at §5.4/S9, bounded at §5.3, and carried into the §8 reconciliation** rather than
left for a reviewer to find.

**D5 — THE PREDECESSOR'S IMPORT AUDIT IS WRONG ON ONE ROW AND I CHECKED RATHER
THAN INHERITED.** `O46SR:96` places the E1 spec v002 outside the permitted
corpus. It is in both roots, sealed OK. Correcting it **strengthened** the seed
finding (the barrier is gradeable at primary) rather than weakening it, which is
the direction that made the check worth running honestly.

### 9.4 Discipline

- **Q-54 / LOCKED_PROCESS B:** every negative this lane *reports* is reported with
  its source's own words quoted. **This lane typed no negative and re-typed none.**
- **Q-80:** no new class constituted. The TIER A/TIER B split and the
  "summary-headline" sub-class are **this lane's own display devices**, named as
  such, not proposed as corpus vocabulary.
- **BARS:** no authoring, no advocacy, no adoption, no performing of any step.
  §4.3 describes a divergence between two sentences and **stops there** — it does
  not propose a reading, an amendment, or a re-typing campaign, all of which are
  principal acts.
- **PRESSURE, BOTH DIRECTIONS:** the three Q3 hypotheses most flattering to the
  commission's framing — that untyped barriers are **older**, **inherited**, or
  **load-bearing** — came back **null, null, and indeterminate**. The one that
  survived (analytic) is the one the commission listed last. The sample's escape
  rate came back **higher** for untyped barriers than the typed population's,
  which is the opposite of "untyped barriers are more absolute". Q4 came back
  **YES — six artifacts quantifying the gap, one ratified ruling instituting it,
  and 82 artifacts carrying the vocabulary** — which is the opposite of the flat
  "nothing does" the commission offered as an option.
- **No `git` of any kind.** Artifact and both sidecars written in the archive
  workspace from its own directory. Nothing published.

```text
alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
```
