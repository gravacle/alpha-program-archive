# STAGE 8 — DEFAULT-REFUTE AUDIT OF THE RESERVATION UNION (O46SR V001) — AUDIT V001

## AUDIT LANE — DEFAULT VERDICT REFUTED — 2026-08-16 — RE-DERIVED AT BYTES

```text
TARGET   /Users/bgm/MB Work/alpha-program-archive/workspace/
         STAGE8_RESERVATION_UNION_O46SR_V001.md
TARGET SHA256 (verified by me, from the target's own directory)
         520363e616d96463df455615b8792dfdbcb0c0146dca1e84b3daeaf8663a0124
TARGET SIDECARS  2/2 OK (`.seal.sha256`, `.sha256`)

FENCES HELD THROUGHOUT THIS AUDIT:
  alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
No numeric value of any coupling, scale, root, eigenvalue, norm or constant was
computed, estimated, bounded, or approached. Where a symbolic root appears below
(`beta = 0`, `G = 1`, `p = -3`) it is the corpus's own display, quoted, never
re-derived, never evaluated, never adopted.
NOTHING IS AUTHORED HERE. Gaps are described and never filled. Where the bytes do
not decide, the entry reads INDETERMINATE-AT-BYTES.
```

---

## §0 — VERDICT

```text
PER DIMENSION
  1  POPULATION AND SAMPLING .......... REFUTED
  2  EVERY GRADED ROW ................. CONFIRMED-WITH-CORRECTIONS
  3  QUOTATION INTEGRITY .............. CONFIRMED-WITH-CORRECTIONS
  4  SECOND-HAND RELIANCE ............. REFUTED
  5  HEADLINE VERSUS EVIDENCE ......... CONFIRMED-WITH-CORRECTIONS
  6  BARS ............................. CONFIRMED-WITH-CORRECTIONS

OVERALL ............................... CONFIRMED-WITH-CORRECTIONS

BOTH OF THE TARGET'S TWO ANSWERS SURVIVE RE-DERIVATION AT BYTES.
  Q1 "no other site; the class is empty, including at the known site" — SURVIVES,
     and is OVERDETERMINED: a sealed of-record corrected grade the target never
     opened defeats the reference site on TWO MORE legs than the target found.
  Q2 "every stated lift condition is disjoint" — SURVIVES in its operative form.
     Its bolded supporting universal ("the corpus does not link them") does NOT.

NINE CORRECTIONS, COR-A .. COR-I, in severity order at §11. Two dimensions are
REFUTED on grounds that do not move either answer: the target reached the right
two negatives, and reached them through a population it mis-declared, a sample it
did not disclose, and a source that is not in the corpus.

THE SINGLE MOST CONSEQUENTIAL FINDING (COR-A): the target's own §6 sweep for
"derived existence AND derived uniqueness" returned FOUR basenames. The target
read three. The fourth is STAGE8_COMPLETION_AND_FORCING_O37SR_AUDIT_V001.md,
whose §2.3 carries a CORRECTED GRADE for exactly the sentence the target rests
Candidate 1's (E) and (U) on — and the target re-quotes that sentence whole,
uncorrected, as the ground of its "class genuinely wider" finding.
```

---

## §1 — DIMENSION 1: POPULATION AND SAMPLING — **REFUTED**

### §1.1 WHAT THE TARGET DECLARED, AND WHAT IS TRUE

The target's §6 population block, `STAGE8_RESERVATION_UNION_O46SR_V001.md:719-731`,
declares three roots, a mirror ratio, a barred count, and an admitted-basename
total. I re-measured every figure.

```text
FIGURE (target §6)                          TARGET   MY MEASUREMENT   VERDICT
text-bearing .md/.json/.py, both roots       10179    10181            CONFIRMED*
barred by name (excluded), paths                31    31               CONFIRMED
admitted distinct basenames                   4829    4831             CONFIRMED*
root 2 top-level .md files                    1523    1523             CONFIRMED
  of which mirror root 1                      1488    1488             CONFIRMED
supervision DOR_*.md                            14    14               CONFIRMED
O43SR / O44SR / O45SR present?                  no    0 paths each     CONFIRMED
O42SR present (highest predecessor)?           yes    6 paths          CONFIRMED

* +2 on both figures. Two text-bearing files entered the workspace between the
  target's sweep and mine (the roots are live; a concurrent lane is writing).
  The +2 is consistent across both figures and I read it as drift, not error.
  The target's figures are accepted as correct AT ITS OWN RUN TIME.
```

**That block is accurate.** The mirror ratio, the barred count and the
admitted-basename total all reproduce exactly. The target's `CH-5` choice to
count distinct basenames rather than paths is the right choice and is honoured in
29 of 31 sweep rows (the two exceptions are COR-D).

### §1.2 THE DEFECT: A THIRD OF THE DECLARED POPULATION IS A VENDORED LIBRARY

The population is declared as "Text-bearing files (.md/.json/.py), both roots,
recursive". Measured:

```text
POPULATION SEGMENT                                     PATHS    DISTINCT BASENAMES
all text-bearing, both roots                           10181    4852
  of which under `.proof_deps/` (sympy + mpmath)        3240    (1300 of the
  of which under `.cache/`                                 3     admitted 4831)
corpus proper (library and cache removed)               6934    3531
```

`.proof_deps/` is a vendored `sympy` / `mpmath` installation. It is **31.8% of the
declared paths and 26.9% of the admitted distinct basenames.** The target nowhere
discloses this, and it is not inert: it contaminates the uniqueness-vocabulary
rows the target reports and then explains.

**The contamination, at bytes.** For `"unique root"` the target reports 34 distinct
basenames. Eight of those 34 are sympy's Lie-algebra root-system modules:

```text
root_system.py   type_a.py   type_b.py   type_c.py   type_d.py
type_e.py        type_f.py   type_g.py
```

These carry "unique root" in the Lie-theoretic sense (roots of a root system).
They are not citations of anything in the corpus. For `"unique solution"`, 20 of
the returned case-insensitive paths are library files.

**And the target states a verification the bytes contradict.** Its §6
reconciliation, `:791-793`, quoted whole:

> "uniqueness-vocab
>    hits (34/48) vastly exceed candidates (7) because most are citations of the
>    same W-3 root across commissions. I verified this by reading the hits, not
>    by counting them."

Eight of the 34 are sympy modules about Lie algebra root systems. They are not
"citations of the same W-3 root across commissions", and a reader who had read
them could not have written that sentence about them. The explanation is wrong
for those hits and the stated method could not have been applied to them.

```text
CORRECTED, corpus-only (case-insensitive, distinct basenames, `.proof_deps`
removed, barred removed):
  "unique root"        34  ->  26
  "unique solution"    48  ->  37   (see also COR-D(i): 48 is not reproducible
                                     under the target's own declared scope)
```

### §1.3 THE DEFECT: UNDECLARED SAMPLING, TWICE, AT THE TWO DECIDING PLACES

The dimension asks whether the build sampled without saying so. It did, twice,
and both times at a place that decides an answer.

**SAMPLE 1 — the Q2 overlap test: 1 of 17.** §2.2 runs the sweep
`"stitching" ∩ "common cell"` and reports **17 distinct basenames**. I reproduce
that figure exactly (17 basenames / 30 admitted paths / 6 barred leaks, case-
insensitive). The target then examines **one** of the seventeen —
`STAGE8_7A_STITCHING_SCOPING_DARIO_V001.md`, which it calls "the on-point one" —
and from that one file asserts a universal negative over all seventeen: "**No
artifact states that a stitching rule would form the common cell.**" The other
sixteen are neither quoted nor reported as read. See COR-B: one of the sixteen
contradicts the bolded form of the claim.

**SAMPLE 2 — the tightest predicate: 3 of 4.** The target's §6 reports
`"derived existence AND derived uniqueness"` at 4 distinct basenames. I reproduce
4 (case-insensitive, self and barred removed):

```text
STAGE8_COMPLETION_AND_FORCING_O37SR_AUDIT_V001.md      <- NOT OPENED BY THE TARGET
STAGE8_DISCHARGERS_VS_PARTITION_O11SR_V001.md          <- used, §1.1
STAGE8_F6b_EMBEDDING_TYPING_FABLE_V001.md              <- used, §1.7
STAGE8_RECORD_CELL_SURFACE_AND_BETA_CLOSURE_HUNT_EINSTEIN_V001.md  <- used, §1.6
```

Three of the four are used and cited. The fourth appears nowhere in the target —
not in its body, not in its 24-file seal list, not in its second-hand markings.
It is the audit of one of the target's two principal sources, and it carries a
CORRECTED GRADE for the exact sentence the target rests Candidate 1 on. See COR-A.

### §1.4 THE DEFECT: ONE SWEEP ROW IS OVER A SCOPE THE TARGET SAYS IT NEVER OPENED

The target's §6 declares its third root, `:723-724`, quoted whole:

> "  ROOT 3  /Users/bgm/MB Work/alpha-program-archive/supervision — DOR_*.md ONLY
>           (14 files; nothing else in that directory was opened)"

Thirty of the thirty-one sweep rows reproduce over root 1 + root 2. **One does
not.** `"unique solution" = 48` reproduces under exactly one scope I could find:

```text
SCOPE                                        cs paths / bn    ci paths / bn
root1 + root2                                   56 / 35          67 / 46
root1 + root2 + supervision DOR_*.md ONLY       56 / 35          67 / 46
root1 + root2 + THE WHOLE supervision dir       58 / 37          69 / 48   <- 48
```

48 is the whole-supervision figure. The supervision directory holds **965 non-DOR
`.md` files** outside the permitted corpus. And the wider scope was **not applied
uniformly** — under it the other rows would read `"unique root"` 37 (target: 34),
`"existence and uniqueness"` 58 (target: 34), `"principal act"` 201 (target: 146),
`"derived existence"` 16 (target: 14). Every one of those matches root1+root2
instead. So a single row of thirty-one ranges over a different population from
the other thirty, while §6 declares one scope for all of them.

That falsifies the target's own closing line at `:801`:

> "  NO COUNT IN THIS ARTIFACT IS SET AGAINST A COUNT OVER A DIFFERENT POPULATION."

Corrected under the declared scope: `"unique solution"` **48 -> 46**; corpus-only
(library removed) **37**.

### §1.5 DIMENSION 1 GRADE

```text
REFUTED — on three independent grounds, none of which moves either answer:
  (a) 26.9% of the admitted basenames are a vendored sympy/mpmath install,
      undisclosed, and it contaminates two reported tallies which the target
      then explains with a verification the bytes contradict (§1.2);
  (b) sampling was undeclared at both deciding places — 1 of 17 in the Q2
      overlap test, 3 of 4 in the tightest Q1 predicate — and the unread rows
      carried, respectively, a counterexample to a bolded claim and a corrected
      grade for the headline site (§1.3);
  (c) one sweep row ranges over 965 files the artifact states were never opened
      (§1.4).
WHAT SURVIVES: every structural figure in the population block — the mirror
ratio, the barred count, the admitted-basename total, the predecessor check —
reproduces exactly. The declared population is REAL. It is not the corpus.
```

---

## §2 — DIMENSION 2: EVERY GRADED ROW — **CONFIRMED-WITH-CORRECTIONS**

I re-read the deciding text of all seven rows whole, wrap-checked, and ran an
independent hunt for rows the target missed.

### §2.1 THE ROW THAT CARRIES THE HEADLINE — CANDIDATE 1 (W-3, the `beta = 0` root)

The target grades this row **FAILS — another blocker also stands**, on legs
`(E) DERIVED`, `(U) DERIVED`, `(R) present but not sole`.

**The (E)/(U) source text verifies exactly.** `STAGE8_W3_GCM_HS_TYPE_O3SR_V001.md`
`:538-546` (seal OK) is reproduced by the target character-for-character,
including the headline and the word `Suppose`. So is `(g-3)` at `:547-554`. So is
the `(d-3)` verdict at `:558-563`. **No quotation defect in this row.**

**But the leg grades are corrected of record, by a file the target never opened.**
`STAGE8_COMPLETION_AND_FORCING_O37SR_AUDIT_V001.md` (seal verified OK by me),
`:457-475`, quoted whole:

> "**WHAT THE ELLIPSIS HIDES: the word `Suppose`.** The uniqueness is the unique
> solution of a SUPPOSITION's equation — a conditional uniqueness inside a
> reductio — and the row's own headline states a NEGATIVE: *a cell-constant bound
> DETERMINES NO EXPONENT*. W-3's own CAS label at `:952` and `:1071` names the
> item the same way: "W6 — beta NON-EXTRACTABILITY FROM A CELL-CONSTANT BOUND".
>
> The build's §1.5, in its own voice and outside any quotation, writes: "at
> **W-3**, the corpus displays a genuine unique root with derived existence AND
> derived uniqueness — `beta = 0`". **That inverts the polarity of the row it
> cites.** O11SR's gloss ("derived existence AND derived uniqueness on the
> admitted asset") is sealed and the build may carry it — but not without the
> row's own headline, which says the opposite about what the bound determines.
>
> **CORRECTED GRADE.** W-3's (a) is **(a) CONDITIONAL-ON-A-SUPPOSITION, at the
> wrong type, refused by rule, and stated by its own carrier as a
> NON-EXTRACTABILITY result.** The build's §2.4 bracket "[ (a) PROVEN exists, for
> beta = 0, AT THE WRONG TYPE, and REFUSED ]" must carry the supposition and the
> polarity. **The build's disposal of it — wrong type, stopped by rule not
> mathematics — I verified whole at O11SR :311-316 and it stands unchanged.**"

Three consequences, each at bytes:

1. **The target's flat leg labels `(E) DERIVED` / `(U) DERIVED` are the reading
   this corrected grade forecloses.** The target's own quotation contains
   `Suppose` and the negative headline; its *grade labels* carry neither.

2. **The target re-quotes the corrected sentence, uncorrected, as load-bearing
   ground.** Its §1.10 quotes O37SR §1.5 whole, including the bullet the audit
   names: *"at **W-3**, the corpus displays a genuine unique root with derived
   existence AND derived uniqueness — `beta = 0` — and **REFUSES to adopt it**,
   by rule"*. That bullet is the target's evidence for "the class is genuinely
   wider". It is the exact sentence graded polarity-inverting at
   `O37SR_AUDIT:465-466`.

3. **The same file the target cites for `(E)` says the opposite 24 lines later,
   and the target does not carry it.** `STAGE8_DISCHARGERS_VS_PARTITION_O11SR_V001.md:337-338`,
   quoted whole:

   > "NONE of the three meets C-REQUIRE: uniqueness is displayed 3/3, EXISTENCE IS DERIVED
   >   0/3, and the forcing criterion needs both.  [CAS C3.]"

   The reconciliation is the type split, and the target knows the type split — its
   §1.1 says "the derived root is a root of the FORM-typed asset while the demanded
   object is HS-typed". But its own bar at §1.0 reads **"(E) EXISTENCE of the
   NEEDED object is DERIVED"**, and by its own admission this root is not a root
   of the needed object. On the target's own bar, `(E)` fails here.

   The independent audit of O11SR keeps both halves straight and confirms both:
   `STAGE8_DISCHARGERS_VS_PARTITION_O11SR_AUDIT_V001.md:322` — *"THE PIVOT (target §2.1):
   uniqueness DISPLAYED 3/3, existence DERIVED 0/3.  I checked both halves."*; and
   `:370-371` — *"W-3's beta = 0 is derived existence AND uniqueness on the ADMITTED
   asset — I re-derived it exactly [audit G1-G3 PASS]"*. Derived on the ADMITTED
   asset; 0/3 on the DEMANDED objects.

```text
CORRECTED GRADE, CANDIDATE 1
  TARGET     FAILS — another blocker also stands (WRONG TYPE; PRODUCTION PROHIBITED)
             with (E) DERIVED, (U) DERIVED, (R) not sole.
  CORRECTED  FAILS — on ALL THREE legs, of record:
             (E) NOT DERIVED for the needed (HS-typed) object — "EXISTENCE IS
                 DERIVED 0/3" (O11SR:337-338); what is derived is existence on the
                 ADMITTED FORM asset (O11SR_AUDIT:370);
             (U) CONDITIONAL-ON-A-SUPPOSITION, inside a reductio whose own headline
                 is a NON-EXTRACTABILITY negative (O37SR_AUDIT:457-461, 470-473);
             (R) present but not sole — UNCHANGED, and expressly re-verified whole
                 at O37SR_AUDIT:474-475.
  THE VERDICT IS UNCHANGED AND IS NOW OVERDETERMINED.
```

**And this retires a live alternative the target recorded.** Its `CH-2` and `D-6`
state that under a narrower reading of "sole blocker" ("no other *authorship*
blocker") **W-3 would grade PASS**, and the target records that reading as open,
calling `CH-2` "the most consequential choice in the artifact". Under the sealed
corrected grade that reading is **foreclosed, not open**: W-3 cannot grade PASS on
any reading of "sole blocker", because it now fails `(E)` and `(U)` before "sole
blocker" is reached. The target's most consequential recorded choice is not a live
choice at bytes.

### §2.2 THE REMAINING SIX ROWS — RE-READ WHOLE

```text
ROW                              TARGET GRADE                    MY RE-DERIVATION
2  W-2, cell_N(e) = gamma_RL     FAILS — existence not derived   CONFIRMED
3  W-1, sub-volume rate          FAILS — existence not derived   CONFIRMED
4  r-1 regularization naming     FAILS — uniqueness not derived  CONFIRMED (see COR-G(iii))
5  S3 at R2                      FAILS — existence not derived   CONFIRMED
6  beta-fixing require (12 subs) FAILS — existence not derived   CONFIRMED
7  F6b embedding forcing         FAILS — existence not derived   CONFIRMED (see COR-G(ii))
```

**Row 2.** `STAGE8_W2_PREQUOTIENT_RULE_O2SR_V001.md:436-440` reproduces exactly;
`:457` `"THE DISPLAYED EVALUATION IS NOT CONSTRUCTIBLE ON THE RATIFIED RULE TODAY."`
reproduces exactly; `§4.3` head at `:404-405` and `H-3` at `:442-447` reproduce
exactly. Two small carries the target dropped, neither moving the grade: `:457-458`
continues *"Not because the rule is deficient — it is complete, proved, and
check-confirmed"*; and the flags string the target prints as one block is assembled
from two places — `COMMON_CELL_FORMED / MEMBER_BOUND / W2_SUPPLIED` sit in the flag
block at `:23`, while `MEMBER_FOUND = none` sits at `:117` and `:153`.
The target also prints *"Three independent obstructions ... Each is sufficient alone"*
without carrying that the source labels `H-1` *"(the binding one)"* (`:408`) and
`H-3` *"(residual, non-binding but displayed)"* (`:442`) — labels in tension with
"each sufficient alone" in the source itself. The target does carry `H-3`'s label
later, at its §2.3.

**Row 3.** `STAGE8_W1_SUBVOLUME_RATE_O5SR_V001.md:58-60` and `:25` reproduce
exactly; the half-line disposal at `STAGE8_DISCHARGERS_VS_PARTITION_O11SR_V001.md:213-218`
reproduces exactly, whole, including `[CAS W1c.]`.

**Row 4.** `a1-1` (`:150-155`) and `RESULT` (`:203-208`) reproduce exactly. `h-1`
(`:319-321`) reproduces exactly. The `a1-4` span carries an unmarked elision —
COR-G(iii).

**Row 5.** `:275`, `:278-280`, and the flag block at `:298`/`:300` all reproduce
exactly at `STAGE8_R2_DETERMINATION_ERRATUM_001_R1_RULING_REACH.md`. The target's
reading — a worth-the-cycles DECISION reservation, not an AUTHORSHIP reservation —
is correct at bytes. The second `"SOLE BLOCKER"` string at
`STAGE8_T7_MANIFEST_BINDING_BRIDGE_AMENDMENT_SUPPLEMENT_V001.md:11-14` is, as the
target says, a launcher `ALLOWED_TARGETS` enumeration defect: *"the pinned launcher
v003's frozen ALLOWED_TARGETS cannot launch the v004 comparator or v004 test
files"*. **Tooling, not a reservation. NOT A CANDIDATE — CONFIRMED.**

**Row 6.** `STAGE8_RECORD_CELL_SURFACE_AND_BETA_CLOSURE_HUNT_EINSTEIN_V001.md:35-40`
reproduces exactly and whole, including the both-ways clause *"No closure was
manufactured; none was withheld"*. The target's judgment that this is the single
most probative negative for Q1 is sound: its bar is the commission's bar verbatim
and its population is a built-out twelve-member set. One reliance note at §4.

**Row 7.** `STAGE8_F6b_EMBEDDING_TYPING_FABLE_V001.md:237-241` reproduces, but the
span closes mid-sentence at a line wrap — COR-G(ii). The grade survives: `:241-242`
continues *"and nothing sealed bars it: the two barred routes ... are routes the W1
recipe does not consume"*, which sustains rather than defeats the target's reading
that no reservation stands at this site.

**§1.8's non-candidates.** O39SR's six POINT rows reproduce exactly at
`STAGE8_REQUIRE_TYPOLOGY_O39SR_V001.md:467-468`. The `R-2/G` disposal reproduces
exactly at `STAGE8_ALLOW_REQUIRE_JUNCTION_T14SR_AUDIT_V001.md:318-322`. The
target's reason for excluding them — already of record, no entry pending, so no
reservation stands over them — holds at bytes.

### §2.3 MY INDEPENDENT HUNT FOR ROWS THE TARGET MISSED — NO EIGHTH CANDIDATE

I swept the corpus for the both-derived predicate independently of the target's
candidate list and opened every carrier it returned that the target did not.

```text
CARRIER (not in the target's 24-file ground set)          BEARS AN 8TH CANDIDATE?
STAGE8_COMPLETION_AND_FORCING_O37SR_AUDIT_V001.md         NO — it CORRECTS row 1
                                                             (COR-A)
STAGE8_DISCHARGERS_VS_PARTITION_O11SR_AUDIT_V001.md       NO — confirms 0/3 and
                                                             the admitted-asset split
STAGE8_CONSTRAIN_OR_CREATE_O36SR_AUDIT_V001.md            NO — quotes W-2's own
                                                             refusal sentence (:455)
STAGE8_GATE_SIGNATURE_O18SR_V001.md                       NO — general principle only
STAGE8_FORCING_BOUNDARY_ADJUDICATION_EINSTEIN_V001.md     NO — general principle only
STAGE8_C1_COMMON_CELL_POSED_CODEX2_V001.md                NO — the common cell is
                                                             UNFORMED, posed only
```

The two "general principle" carriers are the sharpest test and both fail it. Their
sentence is `"*** A REQUIRE-SHAPED CONDITION WITH DERIVED EXISTENCE AND UNIQUENESS
FORCES A NUMBER. ***"` — a criterion, not a site. And its corrected form is
self-typed at `STAGE8_FORCING_BOUNDARY_ADJUDICATION_EINSTEIN_V001.md:29` as
*"CORRECTED FORM (proposed, derived = false, principal's to adopt)"* — proposed and
underived on its own face, so it supplies no both-derived site.

```text
INDEPENDENT RESULT: the Q1 class is EMPTY. I found no eighth candidate, and the
one row the target missed runs AGAINST the reference site, not for it.
Q1's headline is CONFIRMED and STRENGTHENED.
```

### §2.4 DIMENSION 2 GRADE

```text
CONFIRMED-WITH-CORRECTIONS — all seven FAILS verdicts survive at bytes; no
eighth candidate exists on an independent hunt; Candidate 1's leg grades are
corrected by COR-A and its recorded PASS-alternative (CH-2 / D-6) is foreclosed.
```

---

## §3 — DIMENSION 3: QUOTATION INTEGRITY — **CONFIRMED-WITH-CORRECTIONS**

I checked every quoted span in the target against source bytes for early closure,
for mid-sentence line wraps, and for dropped adverse clauses.

### §3.1 SPANS THAT VERIFY EXACT AND WHOLE

```text
SPAN                                                     SOURCE:LINES        VERDICT
O11SR "SOLE-NESS IS A PROPERTY OF THE DEMAND"            O11SR:190-195       EXACT, WHOLE
W-3 (g-2), the cell-constant bound                       O3SR:538-546        EXACT, WHOLE
W-3 (g-3), the refusal                                   O3SR:547-554        EXACT, WHOLE
LC-1, the (d-3) verdict ("or not at all")                O3SR:558-563        EXACT, WHOLE
O33SR restatement of the beta refusal                    O33SR:744-745       EXACT, WHOLE
W-2 CARRY-1 / "would BE the identification"              W-2:436-440         EXACT, WHOLE
LC-3, the domain halt                                    W-2:417-420         EXACT, WHOLE
W-2 §4.3 head, "each is sufficient alone"                W-2:404-405         EXACT, WHOLE
W-2 H-3, the gauge halt                                  W-2:442-447         EXACT, WHOLE
W-1 §0 "PARTIAL. The rate is NOT certified"              W-1:58-60           EXACT, WHOLE
O11SR half-line disposal                                 O11SR:213-218       EXACT, WHOLE
R1 a1-1 and RESULT                                       R1_AUDIT:150-155,
                                                            203-208          EXACT, WHOLE
LC-4 h-1                                                 R1_AUDIT:319-321    EXACT, WHOLE
R2 erratum S3 / SOLE BLOCKER / re-put                    R2_ERRATUM:275,
                                                            278-280          EXACT, WHOLE
T7 launcher blocker                                      T7_SUPP:11-14       EXACT, WHOLE
EINSTEIN twelve-candidate negative                       EINSTEIN:35-40      EXACT, WHOLE
O39SR six POINT rows                                     O39SR:467-468       EXACT, WHOLE
T14SR-AUDIT R-2/G adjudication                           T14SR_AUDIT:318-322 EXACT, WHOLE
O13SR uniqueness-without-existence block                 O13SR:1064-1070     EXACT, WHOLE
O37SR §1.5 executed-precedent search                     O37SR:455-462       EXACT
LC-5 lift condition text                                 GAMMA_K:106-109     EXACT (but see COR-C)
LC-6 A_c row                                             AXN:297             EXACT, WHOLE
LC-7 C_R sentence                                        C_R:711             EXACT, WHOLE
7A stitching fence declarations                          7A_STITCH:84, 501   EXACT
```

That is a strong record. The target's quotation discipline is, in the main, good:
it carries adverse clauses that hurt it (the W-2 "CORRECTION CARRIED ... the
residual is NOT shown nonzero"; F6b's "and nothing sealed bars it"; the R2
erratum's own warning against lanes that count blockers), and it quotes `(g-2)`
with the word `Suppose` intact where a weaker lane would have elided it.

### §3.2 THE THREE DEFECTS — ALL UNDER AN EXPLICIT "QUOTED WHOLE" LABEL

**(i) §1.1 — the O11SR §2.4 disposal, closed early, adverse continuation dropped.**
The target labels it *"`O11SR` §2.4 as O37SR carries it whole"* and closes at
*"(ii) what stops it is a rule, not mathematics"*. At
`STAGE8_DISCHARGERS_VS_PARTITION_O11SR_V001.md:314-316` the sentence continues:

> "and (ii)
> what stops it is a rule, not mathematics — O8SR §4.4: "it is F3-d,
> not mathematics, that stops it." **Both facts are carried forward into §5 unchanged, because
> this is the single place in the discharger set where a forcing shape is displayed at all.**"

Two things are dropped: the naming of the stopping rule (`F3-d` — a certification-route
rule, which bears on whether the blocker is an *authorship* reservation at all), and
a population statement ("the single place in the discharger set"). The target had
O11SR open and sealed and quotes it directly three other times; it did not need
O37SR's rendering. O37SR's rendering at `:654-660` also closes at "not mathematics",
so the label "as O37SR carries it whole" describes O37SR's truncation, not O11SR's
sentence.

**(ii) §1.7 — the F6b span, closed MID-SENTENCE at a line wrap.** The target labels
it *"quoted whole including the both-ways precedent clause"* and ends at *"and
nothing sealed bars it"*. At bytes, `STAGE8_F6b_EMBEDDING_TYPING_FABLE_V001.md:241`
ends with the words *"and nothing sealed bars"* and `:242` opens *"it: the two barred
routes (C_ref's third constituent ... DoR-007's bar on importing smooth `(M,g)`) are
routes the W1 recipe does not consume."* This is the exact failure mode the standing
discipline names — a span called complete at a line wrap. The dropped clause names
two barred routes; it does not defeat the target's grade (the routes are ones the
recipe does not consume), but "quoted whole" is not true of the span as printed.

**(iii) §1.4 — `a1-4`, an unmarked elision of ~13 lines under a "quoted whole" label.**
The target prints *"`a1-4`, quoted whole:"* and closes at *"is verified at its
grounds"*, then prints *"and its closing clause, quoted whole:"*. Between the two,
`STAGE8_R1_NAMING_CANDIDATE_AUDIT_V001.md:186-198` is silently dropped, with no
ellipsis and no gap marker. The dropped text contains the audit's own hunt result:

> "My hunt for a SECOND
>      of-record family that renders 2 C~ P C~ trace class per member
>      (slab families — symbol level, wrong axis; D3 cell refinements —
>      spatial, not the operator axis; the omega = 0 slice — bookkeeping
>      intermediate; polydisc radius — domain parameter; Moebius/connected
>      truncation — cluster axis, not a compression of CPC) found NONE."

That runs **against** the target's `(U) FAILS` grade in the narrow scope, and it is
the strongest uniqueness material at the site. The target does concede the scoped
lemma in its prose, so the grade survives; the elision is nevertheless unmarked and
adverse.

### §3.3 A FOURTH, LOWER-SEVERITY NOTE

`§1.5`'s quotation of the R2 erratum's trap sentence closes before `:268`'s
explanatory clause *"S1 stopped blocking because it was answered *against* R2's
tractable form."*, and the same section omits the co-located flag
`r2_standalone_form_startable = true` (`:299`) while reporting the two adjacent
flags. Neither moves the grade. Recorded, not elevated.

### §3.4 DIMENSION 3 GRADE

```text
CONFIRMED-WITH-CORRECTIONS — 24 of 27 checked spans verify exact and whole,
including several adverse clauses the target carried against its own interest.
Three spans carry an explicit "quoted whole" label that the bytes do not support
(COR-G), one of them a mid-sentence line-wrap close. No elision flips a grade.
```

---

## §4 — DIMENSION 4: SECOND-HAND RELIANCE — **REFUTED**

The standing discipline is explicit: if a file the lane needs sits outside the
permitted corpus, it must say so and mark anything resting on it **SECOND-HAND**
rather than quietly relying on a quotation of it. The target declares two
second-hand markings, `SH-1` (register content) and `SH-2` (W-2's CARRY-1 and
W-3's CERT quotations). Both are properly made. A third is missing, and it is
load-bearing.

### §4.1 LC-5 RESTS ON A FILE THAT IS NOT IN THE CORPUS, UNMARKED

`LC-5` cites `STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md:103-110`, which quotes
`RESULT_FFL1_SMALL_S_END_2026-07-30.md:108-110`. I searched both roots:

```text
find both roots -iname "*FFL1*"          -> 0 paths
find both roots -iname "RESULT_FFL*"     -> 0 paths
files containing the string "RESULT_FFL1_SMALL_S_END":
   QUESTIONSSETTLED_REGISTER_V001.md        (BARRED — not opened)
   STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md (the target's source)
   STAGE8_PROSE_FLAG_DEPENDENCY_EXTRACTION_V001.md
   STAGE8_RESERVATION_UNION_O46SR_V001.md   (the target itself)
```

**`RESULT_FFL1_SMALL_S_END_2026-07-30.md` does not exist anywhere in either corpus
root.** LC-5's lift condition is therefore a quotation of a quotation of an absent
file, and the target marks it as neither second-hand nor absent. It presents it in
the same register as LC-2 and LC-3, whose sources it did open.

**It is load-bearing on four counts.** LC-5 is (a) one of the seven lift conditions
whose pairwise disjointness IS the Q2 answer; (b) one of only three the target types
as "NOT SATISFIABLE BY AN AUTHORED ACT", and one of only two where it says so in
bold; (c) one half of the single structural overlap candidate tested in §2.2; and
(d) the whole content of `I-2`, the target's one named byte on which a YES to Q2
would turn.

```text
CORRECTED: LC-5 -> SECOND-HAND. Its ultimate source is outside the permitted
corpus and absent from both roots. The GAMMA_K spec's rendering is sealed and
verifies OK, so the quotation is a sealed rendering — but it is a rendering, and
the target does not say so.
```

### §4.2 THE O37SR §1.5 SENTENCE IS RE-USED AFTER IT WAS CORRECTED OF RECORD

Covered at §2.1 and COR-A, and it belongs here too: the target's §1.10 rests the
"class genuinely wider" finding on a quotation of O37SR §1.5 that the sealed audit
of O37SR grades as inverting the polarity of the row it cites. Relying on a source
whose audit exists, without consulting the audit, is second-hand reliance of the
most consequential kind — the corrected text was one `grep` away and appeared in
the target's own four-hit sweep.

### §4.3 A THIRD, LOWER-SEVERITY UNMARKED RELIANCE

§1.6 — the target's "single most probative negative" — rests on
`EINSTEIN:35-40`, whose bar is stated as *"the corrected bar (Q-65/Q-76, verified
at the **register**)"*. The target's `SH-1` asserts *"Nothing in my gradings rests
on a register row"*. That grading rests on a bar the source says was register-
verified, one level removed. The quotation is admitted and sealed and I do not
treat this as a bar incident; it is an unmarked second-hand element in the row the
target itself calls most probative. Recorded at lower severity than §4.1.

### §4.4 DIMENSION 4 GRADE

```text
REFUTED — LC-5 rests entirely on a file absent from both corpus roots and is not
marked SECOND-HAND, in direct breach of the standing discipline, and it is
load-bearing on four counts (§4.1). The O37SR §1.5 sentence is re-used uncorrected
where its own sealed audit corrects it (§4.2). A third reliance is unmarked (§4.3).
WHAT SURVIVES: SH-1 and SH-2 are correctly made, and the Q2 answer does not
change — LC-5's disjointness from the other six is unaffected by its provenance.
```

---

## §5 — DIMENSION 5: HEADLINE VERSUS EVIDENCE — **CONFIRMED-WITH-CORRECTIONS**

### §5.1 Q1's HEADLINE AGAINST ITS OWN SWEEP BLOCK

The target is careful here and says the right thing at `:788-793`: the sweep block
"does not by itself establish the headline and is not claimed to". That is correct
and is the disciplined position. Two defects sit inside it:

- the stated verification of the uniqueness-vocab hits is contradicted by the hits
  (COR-E, §1.2);
- the reported figures for the two rows it names (34/48) are corpus-contaminated
  and, for 48, outside the declared scope (COR-D, COR-E).

The headline itself — "no other site; the class is empty, including at the known
site" — **reconciles with the evidence and survives my independent hunt** (§2.3).

### §5.2 THE "SIX OF SEVEN" TALLY, CORRECTED

The target's §0 binding-constraint claim, `:33-35`, quoted whole:

> "    BINDING CONSTRAINT, and it binds before uniqueness or reservations are
>     reached: DERIVED EXISTENCE is the scarce predicate. Six of seven
>     candidates fail on existence alone."

Under COR-A, Candidate 1 fails `(E)` for the needed object as well.

```text
CORRECTED TALLY:  "Six of seven candidates fail on existence alone"
               -> "SEVEN of seven candidates fail on existence for the NEEDED
                   object." The scarcity claim is UNCHANGED and STRENGTHENED.
```

The same correction applies to §1.10's closing clause *"and where it is present
(W-3) a type blocker stands beside the reservation"*: derived existence of the
**needed** object is present nowhere in the candidate set; what stands at W-3 is
derived existence on the ADMITTED FORM asset, which is a different object, as both
O11SR:337-338 and O11SR_AUDIT:322/:370 keep straight.

A minor internal note: §1.10's summary table gives Candidate 4's ground as
"uniqueness not derived (class open of record)" and does not list existence, while
§1.4's prose asserts *"**(E) is likewise not derived**"*. The two reconcile via the
prose; the table under-reports. Not elevated to a correction.

### §5.3 Q2's HEADLINE AGAINST ITS OWN §2.2

The Q2 headline — "every stated lift condition is disjoint" — survives. Its
supporting universal does not, in the bolded form the target gives it. See COR-B
and §6.2 below. The target's `x-1..x-4` "what would have changed this grade" block
is honest and its four negatives reproduce.

### §5.4 THE ONE STRUCTURAL OVERLAP TEST — THE BOLDED CLAIM IS FALSE, THE NARROW ONE IS TRUE

The target's §2.2, `:541-548`, asserts in bold: **"The corpus does not link them."**
followed by **"No artifact states that a stitching rule would form the common cell."**

I read all 17 basenames the sweep returned. Sixteen carry "common cell" only inside
fence declarations, exactly as the target found for its one sample. **The
seventeenth does not.** `STAGE8_ITEMS_1_6_COVERAGE_AUDIT_FABLE_V001.md` (seal
verified OK), `:168-177`, quoted whole:

> "- **Disambiguation booked, adversarially.** The 7A gluing grammar contains a DIFFERENT object
>   with a similar name: the "common junction cell" / common-refinement cell of two complexes.
>   That object is NOT covered by item 5 and is not formed anywhere of record ("common junction
>   cell formed = false", 808; "No common cell formed", 751 gates), and its prerequisite
>   same-region relation is of record NOT forced and NOT unique (RA27-2:
>   `RA27_2_FORCED_BY_STOCK = false`, `RA27_2_CLOSURE_UNIQUE = false`, one-parameter
>   countermodel; the stitching scoping types it as possibly requiring ADOPTION). The anchor's
>   row 5 claim is the free-orbit reading and is genuine on that reading; any reading of row 5
>   as supplying the gluing grammar's common junction cell would be a gloss and is here flagged
>   as NOT claimed."

Two findings in one span.

**(a) The corpus DOES link them, in one clause.** `:174` — *"the stitching scoping
types it as possibly requiring ADOPTION"*, where "it" is the common junction cell's
**prerequisite same-region relation**. That is a stated relation between the
stitching material and the common-cell prerequisite. It is not the link the target
denied in its narrow sentence — it does not say a stitching rule would FORM the
common cell — but it flatly falsifies the bolded generality "**The corpus does not
link them.**"

**(b) "Common cell" names at least three different objects, and the target's string
sweep conflated them.** `:168-169` books the disambiguation adversarially: the "common
junction cell" / common-refinement cell of two complexes is *"a DIFFERENT object with
a similar name"* from item 5's free-orbit presentation. W-2's `LC-2` demands a third
thing again — *"one common physical cell on which both typed returns exist
independently"*. The target ran one string across all three and concluded about
`LC-2`'s object. That is the COUNT HYGIENE defect the discipline names, inside the
one test the target calls decisive for Q2.

**A second missed row, running the target's way.** `STAGE8_INGREDIENT_CENSUS_O17SR_V001.md`
(seal OK), `:429-431`, quoted whole, is directly on point and the target never
reached it:

> "with
> the accompanying typing at :90-91: "a formed common cell alone does not supply
> the junction, and a derived-plus-`beta`-sensitive junction alone would not
> identify the common cell.""

That is a stated NON-implication in both directions between the junction and the
common cell — evidence FOR the target's disjointness answer, found by neither the
target's sample nor its reasoning. Its source, `STAGE8_C1_COMMON_CELL_POSED_CODEX2_V001.md`
(seal OK), is the corpus's dedicated common-cell artifact; it contains **zero**
occurrences of "stitching", so the target's `∩` sweep design could never have
returned it.

```text
CORRECTED, §2.2
  "The corpus does not link them."                     -> FALSE at bytes
                                                          (ITEMS_1_6:174)
  "No artifact states that a stitching rule would
   form the common cell."                              -> SURVIVES
  I-2, restated: it must be posed over DISAMBIGUATED objects — the free-orbit
  presentation, the common junction / common-refinement cell, and W-2's one
  common PHYSICAL cell are three objects of record, not one.
  Q2's ANSWER IS UNCHANGED. Its stated ground is narrowed.
```

### §5.5 DIMENSION 5 GRADE

```text
CONFIRMED-WITH-CORRECTIONS — both headlines reconcile with the evidence and both
survive independent re-derivation. Three statements inside the reconciliation
blocks do not: the "I verified this by reading the hits" claim (COR-E), the
"NO COUNT ... OVER A DIFFERENT POPULATION" claim (COR-D), and the bolded
"the corpus does not link them" (COR-B). One tally corrected: six of seven ->
seven of seven.
```

---

## §6 — DIMENSION 6: BARS — **CONFIRMED-WITH-CORRECTIONS**

### §6.1 FENCES

```text
alpha_computed        = false   HELD in the target; HELD in this audit
proof_authorized      = false   HELD in the target; HELD in this audit
kappa_record_computed = false   HELD in the target; HELD in this audit
```

I read the target end to end for a computed value of any coupling, scale, root,
eigenvalue, norm or constant. **There is none.** Symbolic roots appear only inside
quotations of corpus displays (`beta = 0`, `G = 1`, `p = -3`), each carried with
its provenance and each expressly left unadopted. The target's census-bar
declaration also holds at bytes: no count of reservation-blocked sites is reported
anywhere in it.

### §6.2 AUTHORING, ADVOCACY, ADOPTION

I hunted for a drafted, proposed or recommended object and for advocacy.

```text
CLAIM (target §2.4 :594-597, §8 :909-923)                          MY FINDING
"no act is drafted, proposed, sketched, or recommended here"        HOLDS at bytes
"does not say the corpus SHOULD lift any reservation, nor which
  one is nearest to lifting, nor in what order"                     HOLDS at bytes
"does not reclassify any site, overturn any verdict, or add any
  row anywhere"                                                     HOLDS at bytes
§4 TOY_SEPARATION: lattice / dependency graph / closeness scoring
  "NOT BUILT"                                                       HOLDS — absent
```

The target's §2.2 explicitly declines to construct the stitching-to-common-cell
link on the ground that authoring it is barred, and records at §4 that doing so
"would have produced a YES for Q2 — a strong, quotable, and AUTHORED result".
That is the bar working, and it is the target's best moment. **No bar incident of
the authoring kind.**

### §6.3 THE REGISTER BAR

No file matching a barred pattern is cited as a source anywhere in the target. The
two mentions of `QUESTIONSSETTLED_REGISTER_V001.md` (`CH-7`, `§7`) are declarations
that it was excluded, not uses of it. My own reproduction of the target's 31 sweep
rows shows barred files were correctly suppressed: every row I ran returned a
non-zero count of excluded-by-name paths that never entered the tallies, matching
the target's leak discipline. **Per-pattern leak counter = 0 into counts —
INDEPENDENTLY CONFIRMED.**

### §6.4 THE SCOPE DEFECT

One false statement about scope, already stated as COR-D(i): §6 `:723-724` declares
of the supervision directory *"nothing else in that directory was opened"*, and the
`"unique solution" = 48` row reproduces only over the whole of that directory —
965 non-DOR `.md` files. A `grep -rl` over a directory reads the contents of the
files it traverses. Barred-by-name files there (27 `.md`) were still correctly
excluded from the count, so this is a **permitted-corpus scope breach, not a
REGISTER-BAR incident**. No finding in the target rests on that row.

### §6.5 RE-READ NEGATIVES

I found no instance of the target re-reading a catalogued negative for the purpose
of reopening it. Its §1.8 treatment of the six POINT rows is the nearest approach,
and it uses them as evidence FOR the negative, not as an attempt to reopen them.

### §6.6 DIMENSION 6 GRADE

```text
CONFIRMED-WITH-CORRECTIONS — fences held, no authoring, no advocacy, no adoption,
no re-read negative, register bar honoured and leak discipline independently
confirmed. One false scope statement (COR-D(i)): 965 non-permitted files were
traversed by one sweep row while the artifact states nothing else there was opened.
```

---

## §7 — CHOICE LEDGER (every unforced choice this audit made)

```text
AC-1  I GRADED DIMENSION 1 REFUTED THOUGH EVERY STRUCTURAL FIGURE IN THE
      POPULATION BLOCK REPRODUCES EXACTLY. Alternative: CONFIRMED-WITH-
      CORRECTIONS, on the ground that the mirror ratio, barred count and
      admitted-basename total are all exact. REJECTED because the dimension's
      own test is whether the build sampled without saying so, and it did, at
      both deciding places — and one unread row carried the correction to its
      headline grade. This is a choice, not a finding, and a reader who weights
      the exact figures above the undeclared sampling would grade it
      CONFIRMED-WITH-CORRECTIONS.

AC-2  I TREATED THE O37SR AUDIT AS GOVERNING CANDIDATE 1. Alternative: treat it
      as one more commission's opinion, co-equal with O11SR's. REJECTED: it is
      sealed, it is the audit OF the artifact the target quotes, it states a
      "CORRECTED GRADE" in terms, and it re-verifies the part of O11SR's disposal
      that survives. Its authority over that sentence is of record, not mine.

AC-3  I DID NOT GRADE THE TARGET'S Q1 ANSWER REFUTED THOUGH ITS REFERENCE-SITE
      LEG GRADES ARE WRONG. Alternative: REFUTE Q1. REJECTED because the leg
      corrections all run in the SAME direction as the target's verdict — the
      site fails harder, not less — and the class is empty on my independent
      hunt as well. Correcting the ground of a right answer is CONFIRMED-WITH-
      CORRECTIONS, not REFUTED.

AC-4  I SEPARATED THE BOLDED "the corpus does not link them" FROM THE NARROW
      "no artifact states that a stitching rule would form the common cell" and
      graded them differently. Alternative: read the bold sentence as a mere
      restatement of the narrow one and let both stand. REJECTED: the two differ
      in scope at bytes, and ITEMS_1_6:174 decides between them.

AC-5  I DID NOT ATTEMPT TO DECIDE I-2. The corpus's non-implication byte
      (O17SR:429-431) concerns the junction and the common cell, not the
      stitching rule and the common cell. Extending it would be authoring the
      link the target correctly refused to author. LEFT INDETERMINATE-AT-BYTES.

AC-6  I REPORTED BOTH cs AND ci FIGURES FOR EVERY SWEEP ROW rather than picking
      one and declaring the target wrong. REJECTED alternative: report only my
      preferred mode. The target's table is a MIX of the two modes, and a
      single-mode comparison would have manufactured discrepancies that are
      really method differences.

AC-7  I USED A PRIVATE, UNIQUELY-NAMED SCRATCH DIRECTORY after discovering that
      the shared scratchpad is contended — a concurrently running lane
      overwrote my sweep helper mid-audit. All figures in §9 were re-run from
      scratch in isolation after that discovery. Disclosed at §10 D-1.
```

---

## §8 — IMPORT AUDIT

```text
AIMP-1  "leg grades" ((E)/(U)/(R)) — the target's own three-part bar at its §1.0.
        I adopt its structure and its words to grade it on its own terms. Not
        an import from outside the two roots.

AIMP-2  "library contamination" — mine, describing text-bearing files under
        `.proof_deps/` entering a corpus tally. No corpus term corresponds.

AIMP-3  "undeclared sampling" — the commission's dimension language ("Did the
        build sample without saying so?"). Used as the commission's term.

AIMP-4  "scope breach" — mine, for a sweep row ranging outside the artifact's
        own declared root list. Not attributed to any artifact.

NOTHING ELSE IMPORTED. No mathematical notion, no physics, no external standard,
no definition from outside the two roots and the DOR_* rulings.

SECOND-HAND MARKINGS FOR THIS AUDIT:
  ASH-1  I did not open QUESTIONSSETTLED_REGISTER_V001.md, EXECUTION_TRACKER.md,
         or any REGISTER/TRACKER/THE_PLAN/ROAD_REMAINING/THE_HANDOFF/
         DECISION_SHEET file. Where such a name appears above it appears only as
         a name inside an admitted file's text or inside a sweep-exclusion list.
         Nothing in my findings rests on any of them.
  ASH-2  RESULT_FFL1_SMALL_S_END_2026-07-30.md is ABSENT from both roots. I do
         not rely on its content for anything; my finding at §4.1 is about its
         ABSENCE, which I measured directly.
  ASH-3  The `.proof_deps/` files are third-party library sources. I opened none
         of them; I counted them by path and read only the basenames returned by
         grep -l. My §1.2 finding rests on the file list, not on their content.
```

---

## §9 — SWEEP CUTOFFS (pattern, hits, leak counter)

```text
CORPUS AND POPULATION UNIT — MINE
  ROOT 1  /Users/bgm/MB Work/alpha-program-archive/workspace
  ROOT 2  /Users/bgm/Documents/New project/gravity_emergence_evidence_program/
          alpha_fundamental_record_action_cleanroom_v003
  ROOT 3  /Users/bgm/MB Work/alpha-program-archive/supervision — DOR_*.md ONLY
          (14 files; I opened nothing else in that directory and my sweeps did
          not traverse it except through the explicit DOR_*.md glob)
  UNIT: distinct basename unless a line says "paths". Every figure below states
  its mode (cs = case-sensitive, ci = case-insensitive) because the target's
  table mixes the two and a single-mode report would misrepresent it.

EXCLUSION GLOBS — SUPPLIED AS A ZSH ARRAY, NEVER A STRING VARIABLE
  O46EXCL=( '*REGISTER*' '*register*' '*TRACKER*' '*tracker*' 'THE_PLAN*'
            'ROAD_REMAINING*' 'THE_HANDOFF*' 'OBSERVATIONS_REGISTER*'
            '*DECISION_SHEET*' '*decision_sheet*'
            'STAGE8_RESERVATION_UNION_O46SR_V001.md'
            'STAGE8_RESERVATION_UNION_O46SR_AUDIT_V001.md' )
  SELF-EXCLUSION: this audit's own basename is the last array member and was in
  place before the first sweep that could have matched it. The TARGET is also
  excluded from all counts, so target text never inflates a corpus tally.

REPRODUCTION OF THE TARGET'S 31-ROW TABLE
(leak = returned paths whose basename matches an exclusion member; all leaks
 were suppressed and none entered any count)

  PATTERN                              TARGET   MY cs bn / ci bn   LEAK  VERDICT
  "single principal act"                    0     0 / 0              1   MATCH
  "one principal act"                       0     0 / 0              1   MATCH
  "principal act"                    146(261p)  137 / 146            8   MATCH (ci)
  "new authorship"                         18    15 / 18             2   MATCH (ci)
  "would be authorship"                    19    19 / 19             2   MATCH
  "IS NEW AUTHORSHIP"                      10     4 / 10             1   MATCH (ci)
  "authorship reservation"                  1     1 / 1              1   MATCH
  "sole blocker"                            2     0 / 2              3   MATCH (ci)
  "only blocker"                            5     3 / 3              1   ** UNIT **
  "would lift"                              2     1 / 2              2   MATCH (ci)
  "lift condition"                          4     2 / 2              1   ** UNIT **
  "unique root"                            34    34 / 34             2   MATCH, but
                                                                         CONTAMINATED
  "unique solution"                        48    35 / 46             2   ** SCOPE **
  "exists and is unique"                    3     3 / 3              2   MATCH
  "existence and uniqueness"               34    20 / 34             2   MATCH (ci)
  "derived existence"                      14    13 / 14             2   MATCH (ci)
  "existence is derived"                    5     2 / 5              1   MATCH (ci)
  "derived existence AND derived
     uniqueness"                            4     3 / 4              1   MATCH (ci)
  "REFUSED, NOT ADOPTED"                    3     3 / 3              1   MATCH
  "REFUSED here"                           11    11 / 15             1   MATCH (cs)
  "left unadopted"                          5     5 / 5              1   MATCH
  "would BE the identification"             6     6 / 6              1   MATCH
  "adoption act"                            5     5 / 5              1   MATCH
  "reserved to the principal"               5     5 / 5              3   MATCH
  "PRINCIPAL-ONLY"                          3     3 / 15             3   MATCH (cs)
  "unless and until"                        6     6 / 6              2   MATCH
  "until a principal"                       2     2 / 2              1   MATCH
  "lifts only"                              2     2 / 2              1   MATCH
  "determination alone"                     1     1 / 1              1   MATCH
  "executed.precedent" (regex)              5     — / 5              1   MATCH (ci)
  "stitching" ∩ "common cell"              17     9 / 17             6   MATCH (ci)
  ────────────────────────────────────────────────────────────────────────────
  TOTAL LEAKS INTO ANY COUNT                                          0
  ROWS REPRODUCED EXACTLY                                            28 / 31
  ROWS WITH A UNIT VIOLATION                                          2 (paths
                                                                       reported
                                                                       under a
                                                                       basename
                                                                       header)
  ROWS OUTSIDE THE DECLARED SCOPE                                     1

METHOD FINDING ON THE TABLE AS A WHOLE
  The table declares "unit = distinct basenames" and declares no case mode.
  In fact it is a MIX: at least 11 rows are case-insensitive, at least 2 rows
  ("PRINCIPAL-ONLY", "REFUSED here") are case-sensitive, and 2 rows report PATH
  counts under the basename header. A row-by-row mode is not itself an error;
  an undeclared and non-uniform one makes the table non-reproducible as stated.
  I could reproduce 28 of 31 only by trying both modes on every row.

POPULATION SEGMENTATION (mine, disclosed because the target's is not)
  text-bearing .md/.json/.py, both roots, recursive       10181 paths
    under `.proof_deps/` (vendored sympy + mpmath)         3240 paths
    under `.cache/`                                           3 paths
    corpus proper                                          6934 paths
  admitted distinct basenames (barred removed)              4831
    of which under `.proof_deps/`                           1300
    corpus proper                                           3531

CUTOFFS DECLARED
  - Binary files excluded (grep -I). No cutoff on file size or hit count; every
    pattern above ran to completion over both roots.
  - Directory recursion full in roots 1 and 2; root 3 reached only through the
    explicit DOR_*.md glob.
  - Sweeps are over file CONTENT.

SWEEP-TO-HEADLINE RECONCILIATION (run before sealing)
  My Q1 finding ("class empty; reference site fails on all three legs") rests on
    O37SR_AUDIT:457-475, O11SR:337-338, O11SR_AUDIT:322/:370 — read whole, not
    on any count in the table above.
  My Q2 finding ("bolded universal false; narrow claim survives") rests on
    ITEMS_1_6:168-177 read whole — a file surfaced by the target's own 17-row
    sweep, not by a count of my own.
  My §1.2 contamination finding rests on the FILE LIST returned by grep -l, whose
    members I name (root_system.py, type_a..g.py), not on a ratio.
  NO COUNT IN THIS AUDIT IS SET AGAINST A COUNT OVER A DIFFERENT POPULATION. In
    particular the 31 sweep rows and the 7 graded candidates are different sets
    over different populations and are never compared.
```

---

## §10 — FLAG BLOCK

```text
FENCES
  alpha_computed              = false   UNTOUCHED
  proof_authorized            = false   UNTOUCHED
  kappa_record_computed       = false   UNTOUCHED
  No coupling, scale, root, eigenvalue, norm or constant was computed, estimated,
  bounded, or approached at any point in this audit.

SEALS — VERIFIED BY `shasum -a 256 -c` FROM EACH ARTIFACT'S OWN DIRECTORY
  TARGET                      2/2 OK  (.seal.sha256 and .sha256)
  TARGET'S DECLARED GROUND   24/24 OK — I re-verified every one of the 24 files
    the target lists at its §7, independently, and all 24 verify. The target's
    §7 header figure "24/24" is CORRECT and its enumeration carries 24 entries
    (18 + 6). See COR-I for the contradicting figure inside its own D-4.
  MY ADDITIONAL GROUND         8/8 OK
    STAGE8_COMPLETION_AND_FORCING_O37SR_AUDIT_V001.md ................. OK
    STAGE8_DISCHARGERS_VS_PARTITION_O11SR_AUDIT_V001.md ............... OK
    STAGE8_ITEMS_1_6_COVERAGE_AUDIT_FABLE_V001.md ..................... OK
    STAGE8_INGREDIENT_CENSUS_O17SR_V001.md ............................ OK
    STAGE8_C1_COMMON_CELL_POSED_CODEX2_V001.md ........................ OK
    STAGE8_CONSTRAIN_OR_CREATE_O36SR_AUDIT_V001.md .................... OK
    STAGE8_FORCING_BOUNDARY_ADJUDICATION_EINSTEIN_V001.md ............. OK
    STAGE8_GATE_SIGNATURE_O18SR_V001.md ............................... OK
  TOTAL VERIFIED BY THIS AUDIT: 34/34 OK. NO UNSEALED SOURCE IS USED ANYWHERE.

BAR INCIDENTS
  NONE BY ME. No file matching a barred pattern was opened or read. Barred names
  appear above only as names inside admitted text or inside exclusion arrays.
  No authoring, no advocacy, no adoption. No catalogued negative was re-read for
  the purpose of reopening it. No census was run and no count of reservation-
  blocked sites is reported.
  ONE SCOPE BREACH FOUND IN THE TARGET (COR-D(i)) — 965 non-permitted supervision
  files traversed by one sweep row against an explicit statement that nothing
  else there was opened. Not a REGISTER-BAR incident: barred-by-name files there
  were still excluded from the count.

OWN-DRAFT DEFECTS — DISCLOSED
  D-1  MY SWEEP HELPER WAS OVERWRITTEN MID-AUDIT BY A CONCURRENT LANE. The shared
       scratchpad is contended: a second session replaced my `sweep.sh` with its
       own (self-excluding an O47SR artifact) between two of my calls, and one
       of my commands sourced the foreign file and emitted its output instead of
       mine. Caught immediately from the anomalous output. I moved to a private,
       uniquely-named directory and RE-RAN EVERY FIGURE in §9 from scratch in
       isolation. No number in this artifact comes from a pre-discovery run. The
       first-pass figures I had taken before the discovery agreed with the re-run
       in every case I could compare, but they are not relied on.
  D-2  I INITIALLY RECORDED "unique solution = 48" AS UNREPRODUCIBLE UNDER ANY
       SCOPE. That was wrong and I kept testing: it reproduces exactly over
       root1 + root2 + the WHOLE supervision directory (ci, distinct basenames).
       The corrected characterisation — a scope breach rather than an arithmetic
       error — is materially different and more serious, and is what COR-D(i)
       reports.
  D-3  I NEARLY GRADED CANDIDATE 1 "REFUTED" ON THE STRENGTH OF O11SR:337-338
       ("EXISTENCE IS DERIVED 0/3") ALONE. That would have been wrong: O11SR's
       0/3 is over the DEMANDED objects while its §2.4 statement is over the
       ADMITTED asset, and O11SR_AUDIT:322/:370 keeps both and confirms both.
       The correction that actually governs is O37SR_AUDIT's supposition-and-
       polarity grade, which I found only after opening the fourth basename of
       the target's own four-hit sweep. Recorded because the near-miss is the
       same population error the discipline warns against.
  D-4  MY FIRST READING OF THE TARGET'S D-4 TREATED "23/23" AS THE SEAL COUNT
       AND I BRIEFLY RECORDED A 23-FILE GROUND SET. The target's §7 header says
       24/24 and its enumeration carries 24. Independent verification: 24/24 OK.
       The defect is the target's internal contradiction (COR-I), not its ground.
  D-5  THE +2 DRIFT IN THE POPULATION FIGURES (10179 -> 10181, 4829 -> 4831) is
       reported as drift on the strength of its consistency across both figures
       and the roots being demonstrably live (D-1). I did not establish which two
       files arrived, and a reader who wants that established should treat the
       CONFIRMED marks on those two rows as CONFIRMED-SUBJECT-TO-DRIFT.

INDETERMINATE-AT-BYTES
  AI-1  Whether a derived stitching/continuum rule would also produce W-2's one
        common PHYSICAL cell. The target's I-2, and I leave it where the target
        left it. O17SR:429-431 supplies a non-implication between the JUNCTION
        and the common cell, which is adjacent but not the same pair. Deciding
        the actual pair would require authoring the link. NOT DECIDED.
  AI-2  Whether the target's `(E) DERIVED` label at Candidate 1 was a considered
        type-level choice (grading existence of `beta` rather than of `G_cm`) or
        an unnoticed slip. Its §1.1 prose shows it knew the type split; its bar
        at §1.0 says "the NEEDED object". The bytes of the target do not say
        which. The CORRECTION at COR-A does not depend on resolving this.
  AI-3  Whether the target read STAGE8_COMPLETION_AND_FORCING_O37SR_AUDIT_V001.md
        and declined it, or never reached it. It appears nowhere in the target —
        body, seal list, or second-hand markings — which is consistent with
        either. NOT DECIDED; COR-A does not depend on which.
```

---

## §11 — CORRECTIONS, IN SEVERITY ORDER

```text
COR-A  ** CANDIDATE 1'S (E) AND (U) GRADES ARE CORRECTED OF RECORD BY A FILE THE
       TARGET NEVER OPENED — AND THE TARGET RE-QUOTES THE CORRECTED SENTENCE AS
       LOAD-BEARING GROUND. **
       DECIDING: STAGE8_COMPLETION_AND_FORCING_O37SR_AUDIT_V001.md:457-475
                 (seal OK), with STAGE8_DISCHARGERS_VS_PARTITION_O11SR_V001.md:337-338
                 and STAGE8_DISCHARGERS_VS_PARTITION_O11SR_AUDIT_V001.md:322, :370.
       The audit grades the sentence "the corpus displays a genuine unique root
       with derived existence AND derived uniqueness — beta = 0" as one that
       "inverts the polarity of the row it cites", and states a CORRECTED GRADE:
       "(a) CONDITIONAL-ON-A-SUPPOSITION, at the wrong type, refused by rule, and
       stated by its own carrier as a NON-EXTRACTABILITY result."
       The target quotes that exact sentence whole, uncorrected, at its §1.10 as
       the ground of "the class is genuinely wider", and grades (E)/(U) DERIVED
       at its §1.1 on O11SR's companion gloss.
       The file is the FOURTH basename of the target's own four-hit sweep for
       "derived existence AND derived uniqueness"; the target used the other three.
       CORRECTED GRADE  Candidate 1: FAILS on ALL THREE legs, not one.
       CORRECTED TALLY  "Six of seven candidates fail on existence alone"
                        -> SEVEN of seven fail on existence for the NEEDED object.
       CORRECTED STATUS CH-2 / D-6's recorded alternative ("under a narrower
                        reading of 'sole blocker', W-3 would grade PASS") is
                        FORECLOSED, not live. The target's self-declared "most
                        consequential choice" is not a choice at bytes.
       EFFECT ON THE ANSWER: NONE. Q1's headline survives and is overdetermined.

COR-B  ** §2.2's BOLDED UNIVERSAL IS FALSE AT BYTES; THE TARGET READ 1 OF THE 17
       BASENAMES ITS OWN SWEEP RETURNED. **
       DECIDING: STAGE8_ITEMS_1_6_COVERAGE_AUDIT_FABLE_V001.md:168-177 (seal OK),
                 the operative clause at :174 — "the stitching scoping types it
                 as possibly requiring ADOPTION" — where "it" is the common
                 junction cell's prerequisite same-region relation.
       Also decisive at :168-169: the corpus books, adversarially, that the
       "common junction cell" is "a DIFFERENT object with a similar name" from
       item 5's free-orbit presentation; W-2's LC-2 demands a third object again.
       The target ran one string across three objects of record.
       SECOND MISSED ROW, running the target's way:
                 STAGE8_INGREDIENT_CENSUS_O17SR_V001.md:429-431 (seal OK) — "a
                 formed common cell alone does not supply the junction, and a
                 derived-plus-beta-sensitive junction alone would not identify
                 the common cell." Its source artifact,
                 STAGE8_C1_COMMON_CELL_POSED_CODEX2_V001.md (seal OK), contains
                 ZERO occurrences of "stitching" and could never be returned by
                 the target's `∩` sweep design.
       CORRECTED  "The corpus does not link them."          -> FALSE
                  "No artifact states that a stitching rule
                   would form the common cell."             -> SURVIVES
                  I-2 must be posed over disambiguated objects.
       EFFECT ON THE ANSWER: NONE. Q2's disjointness survives on the narrow claim.

COR-C  ** LC-5 RESTS ENTIRELY ON A FILE ABSENT FROM BOTH CORPUS ROOTS AND IS NOT
       MARKED SECOND-HAND. **
       DECIDING: STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md:103-110 quotes
                 RESULT_FFL1_SMALL_S_END_2026-07-30.md:108-110; `find` over both
                 roots for that name returns ZERO paths, and the only files
                 carrying the string are the GAMMA_K spec, a prose-extraction
                 artifact, a BARRED register, and the target itself.
       LOAD-BEARING on four counts: 1 of 7 lift conditions; 1 of 3 typed "NOT
       SATISFIABLE BY AN AUTHORED ACT"; one half of the sole §2.2 overlap test;
       the entire content of I-2.
       CORRECTED  LC-5 -> SECOND-HAND, source outside the permitted corpus.
       EFFECT ON THE ANSWER: NONE. LC-5's disjointness from the other six is
       unaffected by its provenance.

COR-D  ** THE SWEEP TABLE'S ROWS ARE NOT OVER A COMMON POPULATION, CONTRARY TO
       ITS OWN DECLARATION AND ITS OWN CLOSING LINE. **
       DECIDING: STAGE8_RESERVATION_UNION_O46SR_V001.md:723-724, :730, :741-775,
                 :801, against reproduction.
       (i) SCOPE. "unique solution = 48" reproduces ONLY over root1 + root2 + the
           WHOLE supervision directory (965 non-DOR .md files), while :723-724
           declares "DOR_*.md ONLY (14 files; nothing else in that directory was
           opened)". The wider scope was NOT applied to the other 30 rows.
           CORRECTED  48 -> 46 (declared scope, ci, distinct basenames).
           This also falsifies :801, "NO COUNT IN THIS ARTIFACT IS SET AGAINST A
           COUNT OVER A DIFFERENT POPULATION."
       (ii) UNIT. Two rows report PATH counts under a header declaring distinct
           basenames.
           CORRECTED  "only blocker"    5 -> 3 basenames
                      "lift condition"  4 -> 2 basenames, of which 1 is the
                                             false positive the target itself
                                             identified, leaving 1 GENUINE
                                             basename carrying the term.
       (iii) CASE. Case-folding is undeclared and non-uniform: at least 11 rows
           case-insensitive, at least 2 case-sensitive ("PRINCIPAL-ONLY" 3,
           "REFUSED here" 11). 28 of 31 rows reproduce only by trying both modes.
       EFFECT ON THE ANSWERS: NONE. No graded row rests on a table figure.

COR-E  ** THE DECLARED POPULATION SILENTLY INCLUDES A VENDORED LIBRARY, AND THE
       §6 RECONCILIATION STATES A VERIFICATION THE BYTES CONTRADICT. **
       DECIDING: 3240 of 10181 text-bearing paths and 1300 of 4831 admitted
                 distinct basenames sit under `.proof_deps/` (sympy + mpmath).
                 For "unique root", 8 of the 34 reported basenames are sympy
                 Lie-algebra modules: root_system.py, type_a.py .. type_g.py.
                 For "unique solution", 20 ci-paths are library files.
       AGAINST STAGE8_RESERVATION_UNION_O46SR_V001.md:791-793: "uniqueness-vocab
                 hits (34/48) vastly exceed candidates (7) because most are
                 citations of the same W-3 root across commissions. I verified
                 this by reading the hits, not by counting them."
                 Eight of the 34 are not citations of anything in the corpus.
       CORRECTED  corpus-only (library removed, ci, distinct basenames):
                  "unique root"      34 -> 26
                  "unique solution"  48 -> 37
       EFFECT ON THE ANSWERS: NONE.

COR-F  ** Q2's POPULATION OF "SEVEN RESERVATIONS" IS HETEROGENEOUS UNDER THE
       TARGET'S OWN TAXONOMY. **
       DECIDING: STAGE8_W2_PREQUOTIENT_RULE_O2SR_V001.md:408 — H-1 is "THE DOMAIN
                 HALT (the binding one)", whose ground is that JB-2 has not
                 landed. The target's own bar at §1.0(R) lists "an unlanded
                 input" as a blocker DISTINCT from an authorship reservation, and
                 its CH-3 excluded S3 (a decision reservation) and T7 (tooling)
                 from Q1 on exactly that ground.
       LC-3 is therefore the lift condition of a HALT, not of a reservation. The
       same question can be put to LC-6 (a multiplicity-retention instruction)
       and LC-7 (an untested-class status).
       CORRECTED  §2.1's heading "THE RESERVATIONS THAT STATE A LIFT CONDITION"
                  overstates: the set is seven STATED LIFT CONDITIONS over a
                  mixed population of reservations, halts and statuses.
       EFFECT ON THE ANSWER: NONE. Disjointness is unaffected; the label is not.

COR-G  ** THREE "QUOTED WHOLE" LABELS ATTACH TO SPANS THAT ARE NOT WHOLE. **
       (i) §1.1, the O11SR §2.4 disposal. DECIDING:
           STAGE8_DISCHARGERS_VS_PARTITION_O11SR_V001.md:314-316 — the sentence
           continues past "not mathematics" with "— O8SR §4.4: 'it is F3-d, not
           mathematics, that stops it.'" and a following population sentence
           ("the single place in the discharger set"). Both dropped.
       (ii) §1.7, the F6b span. DECIDING:
           STAGE8_F6b_EMBEDDING_TYPING_FABLE_V001.md:241-242 — the span closes
           MID-SENTENCE at a line wrap: :241 ends "and nothing sealed bars",
           :242 opens "it: the two barred routes (...)". This is the exact
           defect the standing discipline names.
       (iii) §1.4, a1-4. DECIDING:
           STAGE8_R1_NAMING_CANDIDATE_AUDIT_V001.md:186-198 — ~13 lines are
           elided with no ellipsis between two spans each labelled "quoted
           whole". The elided text contains the audit's own "found NONE" hunt,
           which runs against the target's (U) FAILS grade in the narrow scope.
       EFFECT ON THE GRADES: NONE. No elision flips a candidate grade.

COR-H  ** §1.9 MIS-STATES THE POPULATION OF THE COUNT IT IS ADJUDICATING. **
       DECIDING: STAGE8_PRODUCTION_VS_DESCRIPTION_O13SR_V001.md:1065-1066 —
                 "existence fails 3/3 INDEPENDENT of shape — W-2, the PROCESS
                 demand and the posable site, fails existence too."
       The target's §1.9 states: "Its '3/3' is explicitly over the W-set (W-1,
       W-2, W-3) — a three-member population." The triple NAMED AT THE BYTE is
       W-2, the PROCESS demand, and the posable site. That is not the W-set.
       The error sits inside the very section where the target performs its
       COUNT HYGIENE ruling.
       CORRECTED  The INDETERMINATE-AT-BYTES ruling on the trailing clause
                  SURVIVES and is if anything strengthened — the "3/3" population
                  is not the W-set, so its relation to "the one place" is even
                  less determinate than the target argued. Its stated ground is
                  corrected.
       EFFECT ON THE ANSWER: NONE.

COR-I  ** INTERNAL TALLY CONTRADICTION ON THE SEAL COUNT. **
       DECIDING: STAGE8_RESERVATION_UNION_O46SR_V001.md:886 (D-4) says "the seal
                 count corrected 17/17 -> 23/23", while :823 declares "24/24 OK"
                 and the enumeration at :824-850 carries 24 entries (18 + 6).
       INDEPENDENT VERIFICATION: 24/24 OK. The header and the enumeration are
       right; D-4's figure is wrong.
       NOTE FOR THE PARENT: the build report restated this as "17/17 -> 24/24",
       which is not what the artifact says at :886.
       EFFECT ON THE ANSWERS: NONE.
```

---

## §12 — WHAT THIS AUDIT DOES NOT SAY

```text
It does not say the target's two answers are wrong. Both survive re-derivation at
bytes, and Q1's central negative is stronger after correction than before it.
It does not reclassify any site, overturn any verdict, or add any row anywhere.
It does not lift, weaken, or reopen any reservation, halt, or status.
It does not decide I-2, and it does not supply the stitching-to-common-cell link
whose absence the target correctly declined to fill.
It does not draft, propose, sketch, or recommend any act, and it names no act's
content.
It does not claim the target opened any barred file. It reports one sweep row that
traversed files outside the permitted corpus, which is a scope finding, not a
register-bar finding.
It does not count reservations corpus-wide; no census was run.
It does not assert that the Q1 class is empty as a matter of the mathematics —
only that it is empty at the corpus's bytes, on seven graded candidates plus an
independent hunt that found no eighth.
```
