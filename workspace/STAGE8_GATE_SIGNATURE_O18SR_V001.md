# STAGE 8 — GATE SIGNATURE: SELECTOR OR CLASSIFIER? (O18SR) V001

DATE: 2026-08-15
COMMISSION: O18SR (GATE-SIGNATURE-BUILD).
THE QUESTION: does the RECORD'S OWN sealed content about what is REQUIRED and what is
ALLOWED have the signature of a **SELECTOR** (stage/state -> a SET of admissible
continuations) or of a **CLASSIFIER** (a quantity/proposition -> a LABEL)?
STATUS: DETERMINATION ONLY — display of sealed content and typing of displays by
signature. Nothing proposed, authored, adopted or reclassified. No value, no number,
no measured-constant comparison. No git.

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

OUTPUT-PATH PROBE: `/Users/bgm/MB Work/alpha-program-archive/workspace/
STAGE8_GATE_SIGNATURE_O18SR_V001.md` — **ABSENT** at start of commission (probed before
any write; `ls` returned "No such file or directory"; the `.seal.sha256` sidecar likewise
ABSENT).

---

## §0 — THE CRITICAL GUARD: WHAT IS MY SUBJECT AND WHAT IS NOT

The commission names a hazard, and it is real: there exists a **registrar-side ANALYTICAL
inventory** of require-side and allow-side rows, built by a later commission. Typing that
inventory would be typing a registrar's analysis of the record, not the record.

```text
EXCLUDED, NAMED:  STAGE8_ALLOW_REQUIRE_JUNCTION_T14SR_V001.md   (+ its _AUDIT_V001)
```

**HOW I TOLD THEM APART — four independent marks, all checkable at bytes:**

```text
MARK 1  COMMISSION SUFFIX.  T14SR carries the registrar suffix "SR" (as do O9SR, O11SR,
        O12SR, O13SR, T16SR, T17SR, and this artifact O18SR).  The subject artifacts carry
        LANE names (EINSTEIN, DARIO, CODEX2, FABLE, LANE1/2/3) or no lane suffix at all.
MARK 2  SELF-DECLARED OBJECT.  T14SR's own header declares its object to be "the boundary
        between what the record FORCES (requires) and what it PERMITS (allows), displayed
        as an object of record" — i.e. it takes the record as its object.  The subject
        artifacts take PHYSICS/STRUCTURE as their object and USE require/allow as their
        own operative vocabulary.
MARK 3  DATE ORDER.  T14SR is dated 2026-08-15 (today, a later commission).  The require-
        shapes adjudication is dated 2026-07-30; the tree/loop adjudication 2026-08-01;
        the DESC-B03 determinations earlier still.  A later commission's inventory cannot
        be the object-level record it inventories.
MARK 4  DERIVED-vs-ORIGINAL ROWS.  T14SR's content is rows CLASSIFYING other artifacts'
        sentences.  The subject artifacts' content is the operative sentences themselves.
```

**DECLARATION.** I opened `STAGE8_ALLOW_REQUIRE_JUNCTION_T14SR_V001.md` and read **only its
first 20 lines**, for the sole purpose of confirming MARK 2 and MARK 3 so I could EXCLUDE it.
Its seal verified OK. **I quote nothing from it as record content anywhere in this artifact,
and no typing below rests on any line of it.** Its `_AUDIT_V001` companion was never opened.

`STAGE8_FORCING_NOTION_O12SR_V001.md` and `STAGE8_DISCHARGERS_VS_PARTITION_O11SR_V001.md`
surfaced in the same sweeps and carry the same registrar suffix; **both were excluded
unopened** on MARK 1 (filename only — they were never read at all, not even a header).

---

## §1 — SWEEP DECLARATION AND CUTOFF

```text
SWEEP CUTOFF: 2026-08-15, at the byte-states sealed below.  Anything written after this
              artifact's seal is outside my sweep by construction.
ROOTS SWEPT:  (P) /Users/bgm/MB Work/alpha-program-archive/workspace          3581 entries
              (S) /Users/bgm/Documents/New project/gravity_emergence_evidence_program/
                  alpha_fundamental_record_action_cleanroom_v003              3133 entries
DEPTH:        maxdepth 1 for filename sweeps; recursive grep over *.md for content sweeps.
NEVER READ:   no register, tracker, road, plan, or continuation file was opened.  The
              require-shapes adjudication QUOTES a tracker line inside its own sealed text
              (§0, "AS SEALED (two carriers)"); that quotation is consumed AS SEALED TEXT OF
              THE ADJUDICATION, and I did not open the tracker to check it.  Flagged in §6.
"Q-..." :     EXPECTED-UNLOCATABLE and not chased.  Q-64, Q-52, Q-58, Q-56, Q-61, Q-69,
              Q-91, Q-92, Q-54, Q-223, Q-900 appear as register heads inside consumed text
              and are carried as opaque tokens, never resolved.

SWEEP 1 (filenames, both roots): REQUIRE|REQUIRED|SHAPE       -> 62 hits in (P)
SWEEP 2 (filenames, both roots): ALLOW|PERMIT|ADMISS|ELIGIB   -> 20 hits in (P)
SWEEP 3 (content):  'shapes? a requirement|distinct shapes|N shapes|require-shape'
SWEEP 4 (content):  'admissible set|set of admissible|admissible values|permitted values|
                     set of permitted|admissible continuations|admissible next'
```

**SWEEP 3 IS THE ONE THAT LANDED THE PRIMARY SUBJECT.** The commission describes it exactly:
an object-level artifact whose text names a small number of distinct shapes a requirement
can take. Exactly one artifact in either root enumerates them.

---

## §2 — GROUND CONSUMED, SEALS VERIFIED

Every seal below was verified with `shasum -a 256 -c` **executed from the artifact's own
directory**, against the artifact's own `.seal.sha256` sidecar.

```text
G1  STAGE8_FORCING_BOUNDARY_ADJUDICATION_EINSTEIN_V001.md          root (P)   OK
    05c832ad9fb905d88de3f6f00a2ef29e011e86fb8ec8747d5d918f54c5ad4b41
    205 lines, 14469 bytes.  LANE: EINSTEIN.  DATE 2026-07-30.
    *** THE REQUIRE-SHAPES ADJUDICATION.  PRIMARY SUBJECT. ***

G2  STAGE8_TREE_LOOP_VERSUS_ALLOW_REQUIRE_ADJUDICATION_EINSTEIN_V001.md  root (P)  OK
    58fd2e60632633786b49053697170224bcac99b9ea28002752f81f5d26bee4bb
    329 lines, 20880 bytes.  LANE: EINSTEIN.  DATE 2026-08-01.

G3  STAGE8_DESC_B03_DARIO_V002.md                                  root (S)   OK
G4  STAGE8_DESC_B03_DARIO_V003.md                                  root (S)   OK
```

Seal-verification note: G1 and G2 sidecars are named `<file>.md.seal.sha256`; the corpus
also uses `<file>.seal.sha256` (no `.md`) for older artifacts. Both conventions were
handled; every consumed artifact verified OK. **No consumed artifact failed its seal, and
no artifact lacking a sidecar was consumed.**

**OUT-OF-ROOT, DECLARED AND NOT READ.** G2 cites two origin files by path —
`field_access_allow_require_unification_v001.md` and
`boundary_access_closure_threshold_principle_v001.md` — at
`/Users/bgm/Documents/New project/gravity_emergence_evidence_program/`, i.e. **one level
ABOVE** my declared secondary root. `find` at maxdepth 1 in both declared roots returns
EMPTY for both names. **They are outside my corpus roots and I did not open them.** Their
operative sentences enter this artifact only as **sealed quotations inside G2**, whose own
seal verified OK, and are marked SECOND-HAND wherever used.

---

## §3 — THE PRIMARY SUBJECT, QUOTED AT ITS SEALED SOURCE

### 3.1 The require-shapes enumeration — G1 `:53-58`

This is the sentence the commission sends me to find. Quoted verbatim:

> `:53` — "POINT 1 ("a number can be forced two ways")            RIGHT IN SUBSTANCE, IMPRECISE IN COUNT."
> `:54` — "  Forcing has ONE criterion (the admissible set is a point) and THREE shapes: a single require"
> `:55` — "  with a unique root; EXACT JOINT DETERMINATION (n conditions, n freedoms — the marker/C_R"
> `:56` — "  case, which the reviewer's "two ways" silently folds in); and overdetermined joint"
> `:57` — "  determination (surplus conditions). The miscount is harmless here but would matter in a"
> `:58` — "  registry of forcing candidates: exact-joint cases are forcing candidates too."

**THE THREE SHAPES, AS THE RECORD NAMES THEM:**

```text
SHAPE 1   a single require with a unique root
SHAPE 2   EXACT JOINT DETERMINATION      (n conditions, n freedoms)
SHAPE 3   overdetermined joint determination  (surplus conditions)
```

### 3.2 The criterion the three shapes share — G1 `:27`

> `:27` — "number is not a fit. Forcing is a fact about the admissible set (it is a point); anti-fitting"
> `:28` — "is a fact about how we know the point was not chosen. The sealed principle fused them."

And at `:25`, the lead sentence the whole adjudication turns on:

> `:25` — "*** A REQUIRE-SHAPED CONDITION WITH DERIVED EXISTENCE AND UNIQUENESS FORCES A NUMBER. ***"

### 3.3 The four-case map — G1 `:133-149`

The record's own tabulation of allow-side and require-side cases. Verbatim, `:134-148`:

> "CASE                         FORCES?   DISTINGUISHABLE FROM A FIT?"
> "ALLOW + RANGE                NO        NO — any selection is a choice. (The slogan's first"
> "                                       sentence, verbatim right.)"
> "ALLOW + UNIQUE SOLUTION      WITHIN    ONLY VIA PROVENANCE OF THE CLASS. The number rides on"
> "                             THE CLASS the class adoption; the verb calibration denies"
> "                                       "derived." AND THIS CASE IS FITTING'S FAVORITE"
> "                                       DISGUISE — a class drawn post hoc to have a unique"
> "                                       point IS a fit (checklist item 13's second cheat)."
> "REQUIRE + UNIQUE SOLUTION    *** YES ***  YES — via §2's certificates (keystones: freeze,"
> "                                       sweep, root counterfactual). THE SLOGAN FAILS EXACTLY"
> "                                       HERE."
> "OVERDETERMINED               YES       YES, WITH STRUCTURAL EVIDENCE — the strongest grade."
> "(Exact joint determination — n conditions, n freedoms — behaves as REQUIRE+UNIQUE with the"
> "require distributed over legs; each leg's status is audited separately; the marker/C_R case's"
> "grade rides on its weakest leg, today an adoption.)"

### 3.4 The allow side's own operative sentence — G1 `:22`, `:30-31`

> `:22` — "AS SEALED (two carriers): "Permissions compose and never force a number. Only overdetermination"
> `:30` — "  "Permissions never force a number. A derived require with derived existence-and-uniqueness"
> `:31` — "   forces one, and is graded SINGLY-ATTESTED. Overdetermination adds independent structural"

**CARRIED WITH ITS STATUS, NOT FLATTENED.** The `:30-31` sentence is the artifact's own
**PROPOSED CORRECTION**, self-typed at `:29` as "(proposed, derived = false, principal's to
adopt)" and at `:6-7` as offered "under Q-52 discipline". The `:22` sentence is the
**standing sealed** one, which the same artifact declares false in its second half. **Both
are displayed; neither is adopted here, and O18SR does not rule between them.** For
signature-typing purposes they agree on the allow side and differ only on the require side's
sufficiency, so the typing in §4 is stable across the disagreement — stated in §4.5.

---

## §4 — TYPED BY SIGNATURE, AT BYTES

**METHOD, STATED SO IT CAN BE ATTACKED.** For each object I take the **operative sentence**
— the one that says what the object DOES — and read off two things only: what stands on its
INPUT side, and what stands on its OUTPUT side. **I never type from the object's name or
purpose.** Where the name and the sentence disagree, the sentence wins and I say so.

### 4.0 The vocabulary sweep that fixes the input side

Executed by me over G1, word-boundaried, case-insensitive, whole file:

```text
stage          0        admissible     3
step           0        set            2
transition     0        range          1
continuation   0        class          8
next           0        point         11
configuration  0        unique        10
state          1        grade          6
                        label          0
```

**The single `state` hit is not a state space.** It is line 70-71's hyphen-split phrase
`CORRECT-AS-` / `STATE`, inside Point 4's ruling. Verified by direct read of `:71`.

*** THE ARTIFACT THAT ENUMERATES THE REQUIRE SHAPES CONTAINS NO STAGE, NO STEP, NO
TRANSITION, NO CONTINUATION, NO NEXT, AND NO CONFIGURATION. ITS INPUT SIDE CANNOT BE A
STAGE, BECAUSE IT HAS NO WORD FOR ONE. ***

### 4.1 OBJECT A — "the admissible set"

```text
OPERATIVE SENTENCE   G1 :27 "Forcing is a fact about the admissible set (it is a point)"
                     G1 :54 "ONE criterion (the admissible set is a point)"
INPUT SIDE           a CONDITION together with the freedoms it constrains.
                     NOT a stage.  NOT a state.  (§4.0: the words are absent.)
OUTPUT SIDE          a SET of permitted values.
TYPING               *** SELECTOR-SHAPED ON ITS OUTPUT SIDE, CONDITION-INDEXED ON ITS
                     INPUT SIDE. ***  A HALF-SELECTOR: it yields a set, but it is not
                     indexed by anything that could be called a stage or a state.
```

**THE NAME/SENTENCE CHECK.** The name "admissible set" would let one call it a selector
outright. The sentence does not: it says the admissible set is a fact *about* — a property
possessed by a condition — not a map evaluated *at* a stage. **I type it half-selector on
the sentence, not selector on the name.**

### 4.2 OBJECT B — "Forcing" (the ONE criterion)

```text
OPERATIVE SENTENCE   G1 :54 "Forcing has ONE criterion (the admissible set is a point)"
                     G1 :25 "A REQUIRE-SHAPED CONDITION WITH DERIVED EXISTENCE AND
                             UNIQUENESS FORCES A NUMBER."
INPUT SIDE           the admissible set — and specifically ONE QUANTITY OF IT, its
                     cardinality ("is a point" = card 1).
OUTPUT SIDE          a LABEL.  The four-case map's column reads FORCES?  with values
                     YES / NO / "WITHIN THE CLASS".
TYPING               *** CLASSIFIER. EXACTLY AND WITHOUT RESIDUE. ***
                     quantity (cardinality) -> label (forces / does not / within-class).
```

### 4.3 OBJECT C — THE THREE SHAPES THEMSELVES

```text
OPERATIVE SENTENCE   G1 :54-57 "Forcing has ONE criterion ... and THREE shapes: a single
                     require with a unique root; EXACT JOINT DETERMINATION (n conditions,
                     n freedoms ...); and overdetermined joint determination (surplus
                     conditions)."
INPUT SIDE           a forcing CANDIDATE — a condition (or a bundle of conditions) paired
                     with a count of freedoms.  The discriminant is a COUNT COMPARISON:
                     1-vs-unique-root, n-vs-n, surplus-vs-n.
OUTPUT SIDE          one of THREE names.  A three-valued label.
TYPING               *** CLASSIFIER. ***
CORROBORATION FROM   G1 :57-58 states the shapes' intended use in the record's own words:
THE RECORD'S OWN     "would matter in a registry of forcing candidates: exact-joint cases
STATED USE           are forcing candidates too."  A REGISTRY OF CANDIDATES IS A
                     CLASSIFICATION TABLE.  The record does not say the shapes generate,
                     admit, or continue anything.
```

*** THIS IS THE COMMISSION'S CENTRAL FINDING AND I STATE IT PLAINLY: THE "SHAPES" ARE NOT
SHAPES OF A SELECTOR. THEY ARE THREE BUCKETS INTO WHICH A FORCING CANDIDATE FALLS,
DISCRIMINATED BY COMPARING TWO COUNTS. THE WORD "SHAPE" INVITES A GEOMETRIC OR GENERATIVE
READING THAT THE SENTENCE DOES NOT SUPPORT. ***

### 4.4 OBJECT D — THE FOUR-CASE MAP (G1 §3)

```text
INPUT SIDE           an ordered pair (VERB, SOLUTION-STRUCTURE), VERB in {ALLOW, REQUIRE},
                     SOLUTION-STRUCTURE in {RANGE, UNIQUE SOLUTION, OVERDETERMINED}.
                     Both coordinates are PROPOSITIONS about a condition.
OUTPUT SIDE          a PAIR OF LABELS: (FORCES?, DISTINGUISHABLE-FROM-A-FIT?).
TYPING               *** CLASSIFIER, two-output. ***
NOTE                 the ALLOW rows are classified too — ALLOW+RANGE -> (NO, NO).  The
                     allow side is here an INPUT COORDINATE of a classifier, not a
                     set-yielding operation.
```

### 4.5 STABILITY ACROSS THE ARTIFACT'S OWN INTERNAL DISAGREEMENT

G1 displays a standing sealed sentence (`:22`) and its own proposed correction (`:30-31`),
and declares the first false. **The signature typing is unchanged by which one stands.**
Both put a VERB on the input side and a FORCES/DOES-NOT-FORCE verdict on the output side;
they differ only over which input values map to which label. **A dispute about a
classifier's truth table is not a dispute about its signature.** So §4.2-§4.4 hold whether
or not the principal adopts the correction, and O18SR rules on neither.

---

## §5 — THE SELECTOR-SHAPED PIECE, DISPLAYED (DELIVERABLE 3)

Object A is the only selector-shaped thing in the subject. Deliverable 3 asks three
questions of it, and asks the disguise test **in both directions**. Additional sealed
ground consumed here, seals verified from each artifact's own directory:

```text
G5  STAGE8_TASK5_EQ6_WHERE_CLAUSES_LANE2_V005.md            root (S)   OK
G6  STAGE8_AXN_BUILD_H1_INTEGRAND_DARIO_V001.md             root (S)   OK
G7  STAGE8_7A_REFINEMENT_BRIDGE_DARIO_V001.md               root (S)   OK
```

### 5.1 WHAT IT SELECTS OVER

```text
IT SELECTS OVER   the FREEDOMS OF A CONDITION — the values a constrained quantity may
                  still take once the condition is imposed.  G1 :55 names the carrier
                  by counting it: "n conditions, n freedoms."
IT DOES NOT       select over stages, steps, transitions, continuations, or next objects.
SELECT OVER       §4.0: those six words have ZERO occurrences in G1.
ONE EXCEPTION,    G3 :283 does index an admissible set by a STATE SPACE, verbatim:
AND IT IS         "V001 asked for a condition whose admissible set over `State(B)` is a
WITHDRAWN         singleton. **Under the reframe that is the wrong question**"
                  — and G3 :283-284 gives the reason: "not because such a condition would
                  be unwelcome, but because the object it would range over is not where
                  the record locates the freedom."
                  *** THE RECORD'S ONE STATE-INDEXED ADMISSIBLE SET IS THE ONE IT
                  EXPLICITLY WITHDRAWS AS THE WRONG QUESTION. ***
                  G3 :284-288 also forecloses the selector family by name:
                  "NO sealed KMS, passivity, Hadamard, extremality, Gibbs, or thermal
                  selector exists in scope."
```

### 5.2 PER-STAGE OR GLOBAL?

*** NEITHER. IT IS PER-CONDITION. ***

There is no stage index to be per-stage over, and it is not global either — each condition
carries its own admissible set, and G1 §3's four cases differ precisely by which condition
is in hand. **A per-condition family is not a per-stage family**, because conditions are
not ordered, not indexed by position in any chain, and carry no notion of "the next one."
Naming this "global" would be an upgrade the bytes do not support; naming it "per-stage"
would be an import. **It is per-condition, and that is a third thing.**

### 5.3 THE CARDINALITY CHECK — FORWARD DIRECTION

Is the admissible set ever displayed NON-SINGLETON? **YES, at four distinct cardinalities.**

```text
CARD 0   EMPTY        G5 :606  "both laws explicitly permit empty admissible sets"
CARD 1   SINGLETON    G1 :54   "the admissible set is a point"
                      G3 :283  "whose admissible set over `State(B)` is a singleton"
CARD >1  A FAMILY     G1 :135  "ALLOW + RANGE   NO   NO — any selection is a choice."
                      G7 :303  "a `k−1`-parameter family of admissible values"
                      G2 :51   [SECOND-HAND, quoting an out-of-root origin file]
                               "a loop, handle, sector, component, or operator block."
                               with G2 :53's own gloss: "A loop is ONE of five admissible
                               values, co-equal with four non-loop values."
CARD inf UNBOUNDED    G6 :125  "the situation is the opposite, an unbounded admissible set"
```

*** A CLASSIFIER CANNOT RETURN THE EMPTY SET AND CANNOT RETURN AN UNBOUNDED FAMILY. THE
ADMISSIBLE SET IS GENUINELY SET-VALUED, ACROSS FOUR CARDINALITIES, AT FOUR SEPARATELY
SEALED SITES. IT IS NOT A CLASSIFIER IN DISGUISE. ***

### 5.4 THE DISGUISE CHECK — REVERSE DIRECTION, AS COMMISSIONED

The commission requires the check run both ways. **Are Objects B, C, D selectors in
disguise — i.e. is their output ever a set?**

```text
OBJECT B  FORCES?     output values displayed: YES, NO, "WITHIN THE CLASS".  Three names.
                      Never a set.  NOT a selector in disguise.
OBJECT C  THE SHAPES  output values displayed: three named shapes.  Never a set.
                      NOT a selector in disguise.
OBJECT D  FOUR-CASE   output values displayed: (FORCES?, DISTINGUISHABLE?) label pairs.
          MAP         Never a set.  NOT a selector in disguise.
```

**THE ONE PLACE THE REVERSE CHECK NEARLY BITES, REPORTED BECAUSE IT CUTS AGAINST MY
VERDICT'S TIDINESS.** G1 `:137` gives ALLOW+UNIQUE the output value "WITHIN THE CLASS" —
which is not a plain YES/NO but a *scoped* verdict, and scoping is the beginning of
set-talk. **It still does not yield a set.** It names the class as the scope of a label,
not as a returned object; the class is an input coordinate carried into the verdict.
**Reported as a near-miss, not counted as a selector.**

### 5.5 WHAT THIS MAKES THE SUBJECT, AS A WHOLE

```text
LAYER 2 (the record's require/allow ADJUDICATION)   CLASSIFIER  — Objects B, C, D
LAYER 1 (the object it adjudicates ABOUT)           SELECTOR-SHAPED OUTPUT,
                                                    CONDITION-INDEXED INPUT — Object A
```

*** THE RECORD'S REQUIRE/ALLOW CONTENT IS A CLASSIFIER LAYERED ON A HALF-SELECTOR. THE
CLASSIFIER'S SOLE INPUT IS ONE SCALAR EXTRACTED FROM THE HALF-SELECTOR'S OUTPUT — ITS
CARDINALITY. EVERYTHING ELSE ABOUT THE SET IS DISCARDED AT THE LAYER BOUNDARY. ***

---

## §6 — THE CONSEQUENCE, DISPLAYED AND NOT ARGUED (DELIVERABLE 4)

Selector-shaped content exists (Object A, §4.1), so this test is live. The commission asks
exactly two things, and I answer both at bytes and stop.

### 6.1 IS THERE A DOMAIN OVER WHICH SUCH AN INVARIANCE COULD QUANTIFY?

To say "invariant across every application of it" the record must first have an **it** — a
single map — and a **domain** — an index set its applications range over.

**AT BYTES, THE PHRASE "the admissible set" OCCURS EXACTLY TWICE IN G1:**

```text
:27  "Forcing is a fact about the admissible set (it is a point)"
:54  "Forcing has ONE criterion (the admissible set is a point)"
```

**BOTH CARRY A DEFINITE ARTICLE AND NEITHER STATES A DOMAIN.** Not "the admissible set of
X", not "the admissible set over Y" — just "the admissible set", attached to whichever
condition is in hand. Across the whole subject exactly **one** occurrence anywhere states a
domain, G3 `:283`'s "admissible set over `State(B)`", **and that is the occurrence G3
withdraws as the wrong question** (§5.1).

*** THERE IS NO SINGLE SELECTOR. THERE IS A PER-CONDITION FAMILY OF ADMISSIBLE SETS WITH NO
INDEX SET. "INVARIANT ACROSS EVERY APPLICATION OF IT" HAS NO REFERENT FOR "IT" AND NO RANGE
FOR "EVERY". THE DOMAIN IS NOT MERELY UNPOPULATED — IT IS UNFORMED. ***

**THE ONE PLACE THE RECORD NAMES A DOMAIN-SHAPE, AND ITS MOOD:** G1 `:57-58` —

> "The miscount is harmless here but would matter in a
>  registry of forcing candidates: exact-joint cases are forcing candidates too."

**"WOULD MATTER IN A REGISTRY" IS SUBJUNCTIVE.** The record names the container that would
hold the domain and states in the same breath that the question is moot for want of it.
**The registry is a counterfactual object in the sentence that names it.**

### 6.2 IS THAT DOMAIN POPULATED?

Answered for completeness even though §6.1 already disposes of the question, because the
commission asks it separately and an unformed domain could still have candidate members.

```text
CANDIDATE MEMBER          STATUS AT BYTES                                    SOURCE
R-L2b as written          REFUTED | TYPE-R.  "no admissible uniform Hilbert-  G1 :154-156
                          Schmidt bound exists; the obligation AS WRITTEN
                          cannot be met"
                          G1 :163: "The corpus's one require-shaped target
                          was pursued ... and it FAILED — publicly, at a
                          named line, by refutation."
S9-A successor require    UNBUILT | TYPE-U.  G1 :195-197: "is unbuilt; its   G1 :195-197
                          require-status and root-structure certificates
                          cannot be attempted until the response chain
                          exists ... Nothing here starts it."
marker/C_R exact-joint    EXISTS, BUT G1 :147-148: "the marker/C_R case's    G1 :146-148
                          grade rides on its weakest leg, today an adoption."
Gate 4 covector ray       EXECUTED | TYPE-R.  G2 N2 :258-260: "'exactly one  G2 :258-260
                          ray', every deformation violating a named sealed     G2 :144-145
                          constraint".  BUT G2 :144-145: "the covector ray
                          leaves its **positive scale free**. It forces a
                          **direction**, not a magnitude."
```

**POPULATION COUNT AT BYTES: ONE EXECUTED MEMBER** (Gate 4's covector ray), and G1 `:163`
independently counts the require-shaped targets it knows of as **"one"** — a different one,
which failed. **The record's own two counts of its require-side population are each 1, and
they do not name the same object.**

**AND THE MEMBERS ARE NOT COMMENSURABLE.** Each ranges over a different carrier: R-L2b over
a Hilbert-Schmidt bound; the covector ray over readout functionals on the first-opening
record complex (G2 `:72-74`); the exact-joint case over n freedoms; the withdrawn one over
`State(B)`. **Applications of *different* maps cannot witness an invariance of *one* map**,
however many of them there are.

### 6.3 THE DETERMINATION

```text
PIECES REQUIRED TO STATE "INVARIANT ACROSS EVERY APPLICATION OF IT":
  (a) a single map to be the "it"                       ABSENT  — §6.1, per-condition
                                                                 family, no index set
  (b) a domain for "every" to range over                ABSENT  — named only in the
                                                                 subjunctive, G1 :58
  (c) that domain populated                             1 executed member; members
                                                        mutually incommensurable
  (d) a quantity held fixed across applications         NOT REACHED — (a) fails first
```

*** THE PIECES ARE NOT PRESENT. NOT BECAUSE THE POPULATION IS THIN — THOUGH IT IS — BUT
BECAUSE THERE IS NO SINGLE SELECTOR FOR AN INVARIANCE TO BE AN INVARIANCE OF. THIS IS A
STRUCTURAL ABSENCE AT (a), AND IT IS PRIOR TO THE COUNTING AT (c). ***

**DISPLAYED, NOT ARGUED, AND NOT REPAIRED.** O18SR states what is absent and stops. It does
not propose a registry, does not propose an index set, does not nominate members, and does
not say whether any of this should be built.

---

## §7 — IMPORT AUDIT

Every term I used that the record does not supply, declared. **The hazard here is real and
G2 §7 item 3 catalogues its own lane committing exactly this class of error four times.**

```text
I1  "SELECTOR" / "CLASSIFIER" as SIGNATURE TYPES        IMPORTED — commission vocabulary.
    *** AND THERE IS A SYMBOL COLLISION, WHICH I KEPT APART. ***
    The record HAS the word "selector", and it does NOT mean what the commission means.
    Record sense, at G2 :105 and :281-283: "the standalone selector typed
    CELL_CONSTRAINT_ONLY" / "allow_require_standalone_selector_status =
    CELL_CONSTRAINT_ONLY | TYPE-C, carried".  And at G3 :288: "NO sealed KMS, passivity,
    Hadamard, extremality, Gibbs, or thermal selector exists in scope."
    In the record, a "selector" is A RULE THAT PICKS A MEMBER — it aims at a singleton.
    In the commission, a SELECTOR is A MAP THAT YIELDS A SET.
    *** THESE ARE DIFFERENT OBJECTS AND I TYPED FROM SENTENCES, NEVER FROM THE WORD.
    NO ARTIFACT WAS TYPED SELECTOR-SHAPED BECAUSE IT CONTAINS THE STRING "selector",
    AND NONE OF THE RECORD'S OWN "selector" SITES IS A SUBJECT OF §4. ***
I2  "input side" / "output side" / "signature"          IMPORTED — commission vocabulary.
I3  "half-selector"                                     *** MY COINAGE, THIS ARTIFACT. ***
    Descriptive shorthand for "set-valued output, non-stage-indexed input".  IT IS NOT
    PROPOSED AS A CLASS, does not enter the record as a type, and nothing rests on it that
    is not already stated in plain terms at §4.1.
I4  "per-condition"                                     MY PHRASING for what §4.0's counts
                                                        show.  Not a record term.
I5  CARD 0 / 1 / >1 / inf                               MY ORGANIZATION of four separately
                                                        sealed displays.  The cardinalities
                                                        are the record's; the table is mine.
I6  NO PHYSICS PREMISE was introduced anywhere.  No quantity was computed, compared, or
    named as a value.  No measured constant appears.  R-L2b, K_*, C_record, C_R, alpha and
    the covector ray are carried as OPAQUE TOKENS inside quotations only.
```

---

## §8 — TOY_SEPARATION

```text
THE SUBJECT IS ACTUAL SURFACE, NOT A TOY, AND HERE IS THE CHECK:
  - Every object typed in §4 is quoted from a sealed artifact at a cited line, with the
    seal verified by shasum -a 256 -c from that artifact's own directory.
  - NO example condition, NO illustrative selector, NO specimen stage, and NO constructed
    admissible set was introduced anywhere in this artifact.
  - §5.3's four-cardinality table is drawn from FOUR SEPARATELY SEALED SITES (G1, G3, G5,
    G6, G7).  It was NOT assembled by inventing cases to fill a spectrum.  Had the record
    displayed only singletons, §5.3 would have said so and the verdict would have changed.
  - Where the actual surface had nothing, I recorded an ABSENCE rather than building a
    stand-in: §4.0's six zero-counts, §5.1's withdrawn state-index, §6.1's unformed domain.
    *** THE CENTRAL FINDING OF §6 IS AN ABSENCE, AND I DID NOT FILL IT. ***
  - The one place a toy would have been tempting — a worked example of a stage-indexed
    selector, to show what the record would need — IS NOT PRESENT AND WAS NOT WRITTEN.
```

---

## §9 — CHOICE LEDGER

```text
C1  WHICH ARTIFACT IS "THE REQUIRE-SHAPES ADJUDICATION".  Chose G1 (FORCING_BOUNDARY)
    over G2 (TREE_LOOP_VERSUS_ALLOW_REQUIRE), which is the more obvious name-match.
    BASIS: the commission's own description — "names a small number of distinct shapes a
    requirement can take".  G1 :54 enumerates THREE shapes; G2 uses "require-shaped" as an
    adjective 4 times and enumerates NO shapes.  Sweep 3 returned exactly one enumerator.
    COST IF WRONG: §4.3 would retarget; §4.1-4.2 and §6 would survive, since they rest on
    G1 :27 and :54 which any competing reading still contains.  G2 IS CONSUMED ANYWAY.
C2  READ 20 LINES OF THE EXCLUDED T14SR.  Could have excluded it unopened on MARK 1 alone.
    Chose to confirm MARK 2 and MARK 3 at bytes rather than trust a filename convention.
    COST: I saw 20 lines of a non-subject.  MITIGATION: quoted as record content nowhere;
    no typing rests on it.  O11SR and O12SR were then excluded unopened, testing whether
    MARK 1 alone suffices — it did, and I am recording that I applied two standards.
C3  DID NOT READ THE TWO OUT-OF-ROOT ORIGIN FILES.  They are visibly the allow/require
    origin definitions, and reading them would have strengthened §5.3.  Chose the declared
    corpus roots over the better exhibit.  COST: the allow-side origin definition and the
    five-valued carrier enter only SECOND-HAND through G2, and are marked so at every use.
C4  TYPED OBJECT A ON BOTH SIDES SEPARATELY rather than forcing it into one bucket.
    Chose this because the commission asks explicitly what each object takes AND yields.
    A forced binary would have had to either call it SELECTOR (over-claiming a stage index
    it does not have) or CLASSIFIER (false — it returns sets, at four cardinalities).
C5  COUNTED THE FOUR-CASE MAP AS ONE OBJECT (D) rather than four classifications.
    Its four rows share one input signature and one output signature.
C6  RAN THE REVERSE DISGUISE CHECK AND REPORTED THE NEAR-MISS at G1 :137's "WITHIN THE
    CLASS", which is the one output value that is not a flat label.  Reported because it
    cuts against the tidiness of the verdict, not because it changes it.
C7  VERDICT MIXED, NOT SELECTOR-SHAPED.  The selector-shaped piece is real and is the
    substrate of everything else, which makes SELECTOR-SHAPED tempting.  Rejected: three
    of the four objects classify, and the layer that IS the record's require/allow
    adjudication is entirely classifier.  MIXED with the split stated exactly is more
    honest than either pure verdict.
```

---

## §10 — FLAG BLOCK

```text
F1  THE LAYER-1 / LAYER-2 SPLIT (§5.5) IS THIS ARTIFACT'S ORGANIZATION of sealed material.
    It is NOT a sealed distinction.  Stated so it can be attacked.
F2  "HALF-SELECTOR" is this artifact's coinage (I3).  Not a class, not proposed.
F3  SECOND-HAND CONTENT, MARKED: G2 :51's quotation of the out-of-root threshold principle
    ("a loop, handle, sector, component, or operator block") was NOT verified at its own
    source, because its source is outside my declared roots.  It is carried on G2's seal
    and G2's own statement that it read the line at source.
F4  G1 :22-23 QUOTES A TRACKER LINE inside its own sealed text.  I consumed it as G1's
    sealed text and DID NOT OPEN THE TRACKER.  If that quotation is inaccurate, §3.4's
    display of the standing sentence inherits the error; §4's typing does not, because
    §4.5 shows the signature is stable across both readings.
F5  G1's §0 CORRECTED FORM is self-typed "proposed, derived = false".  Displayed at §3.4,
    ADOPTED NOWHERE.  O18SR does not rule between it and the standing sentence.
F6  THE POPULATION COUNT AT §6.2 IS BOUNDED BY MY SWEEP CUTOFF and by the never-read
    classes.  A register or tracker I am forbidden to open could name further candidates.
    *** THIS IS A REAL LIMIT ON §6.2 AND I STATE IT RATHER THAN LETTING THE COUNT STAND
    AS COMPLETE.  IT DOES NOT TOUCH §6.1, WHICH IS AN ABSENCE OF STRUCTURE, NOT OF
    MEMBERS. ***
F7  G2's OWN §7 RECORDS THAT FOUR OF ITS CHAINS COMMITTED A SECTOR-TRANSPORT ERROR and
    that its N13 struck a mechanism claim.  I consumed G2 only for N2, :51-53, :72-74 and
    :144-145.  N13's strike does not reach those, but I note that G2 is an artifact that
    corrected itself and I did not re-audit the parts I consumed.
```

---

## §11 — TYPED NEGATIVES

```text
N1  require_allow_content_is_selector_shaped = PARTLY | TYPE-C
      One object of four.  Object A ("the admissible set") yields a SET; Objects B, C, D
      yield LABELS.  Typed from operative sentences at G1 :27, :54, :134-148.
N2  the_three_require_shapes_are_a_classifier = true | TYPE-C
      G1 :54-58.  Input: a forcing candidate + a count of freedoms.  Output: one of three
      names.  The record's own stated use is "a registry of forcing candidates" (:58).
N3  require_shapes_artifact_contains_stage_vocabulary = false | TYPE-R | EXECUTED
      Word-boundaried case-insensitive counts over G1, whole file: stage 0, step 0,
      transition 0, continuation 0, next 0, configuration 0, state 1 (and that one is the
      hyphen-split "CORRECT-AS-STATE" at :70-71, verified by direct read).
N4  admissible_set_is_ever_displayed_non_singleton = true | TYPE-R | EXECUTED
      At FOUR cardinalities across FIVE separately sealed artifacts: EMPTY (G5 :606),
      SINGLETON (G1 :54; G3 :283), FAMILY (G1 :135; G7 :303; G2 :51 second-hand),
      UNBOUNDED (G6 :125).  It is NOT a classifier in disguise.
N5  forcing_criterion_is_a_selector_in_disguise = false | TYPE-R | EXECUTED
      Reverse direction run as commissioned.  Its displayed outputs are YES / NO /
      "WITHIN THE CLASS" — never a set.  Near-miss at :137 reported, not counted.
N6  admissible_set_is_stage_indexed = false | TYPE-R | EXECUTED
      It is CONDITION-indexed.  The corpus's single state-indexed occurrence (G3 :283,
      "over `State(B)`") is the one G3 withdraws: "that is the wrong question".
N7  a_single_selector_with_a_named_domain_exists = false | TYPE-R | EXECUTED
      "the admissible set" occurs twice in G1 (:27, :54), both with a definite article and
      NO stated domain.  A per-condition family with no index set.
N8  domain_for_an_invariance_to_quantify_over_exists = false | TYPE-R
      Named once and in the subjunctive — "would matter in a registry of forcing
      candidates" (G1 :58).  The registry is counterfactual in the sentence naming it.
N9  that_domain_is_populated = ONE EXECUTED MEMBER | TYPE-C, carried
      Gate 4's covector ray (G2 :258-260).  G1 :163 separately counts "the corpus's one
      require-shaped target", a DIFFERENT object, and records that it FAILED.  Members are
      mutually incommensurable — different carriers — so they cannot witness one map's
      invariance.  CARRIED WITH F6's limit.
N10 pieces_present_to_state_invariance_across_every_application = false | TYPE-R
      Fails at (a), the existence of a single "it", which is PRIOR to the population
      count at (c).  A structural absence, not a thin census.
N11 O18SR_typed_the_analytical_inventory = false | TYPE-R
      T14SR excluded by four marks (§0); read to 20 lines for identification only; quoted
      as record content nowhere.  O11SR, O12SR excluded unopened.
N12 new_class_required = false.  Nothing proposed, authored, adopted, or reclassified.
```

---

## §12 — VERDICT

*** **MIXED.** ***

```text
CLASSIFIER-SHAPED — three objects, and they are the record's require/allow ADJUDICATION:

  B  "FORCING", the ONE criterion       G1 :27, :54
     TAKES   one quantity: the cardinality of the admissible set ("it is a point")
     YIELDS  a label: YES / NO / "WITHIN THE CLASS"

  C  THE THREE REQUIRE SHAPES           G1 :54-57
     TAKES   a forcing candidate: a condition (or bundle) plus a count of freedoms
     YIELDS  one of three names — single-require-unique-root / exact-joint (n,n) /
             overdetermined (surplus).  Discriminated by comparing two counts.
     *** THE "SHAPES" THE COMMISSION SENT ME TO TYPE ARE BUCKETS, NOT SHAPES OF A
     SELECTOR.  THE RECORD'S OWN STATED USE FOR THEM IS "a registry of forcing
     candidates" (:58) — A CLASSIFICATION TABLE. ***

  D  THE FOUR-CASE MAP                  G1 :134-148
     TAKES   (VERB, SOLUTION-STRUCTURE), both propositions about a condition
     YIELDS  a pair of labels: (FORCES?, DISTINGUISHABLE-FROM-A-FIT?)

SELECTOR-SHAPED — one object, and it is the SUBSTRATE the three classify:

  A  "THE ADMISSIBLE SET"               G1 :27, :54
     TAKES   a CONDITION together with the freedoms it constrains
             *** NOT a stage.  NOT a state.  NOT a configuration.  Those six words have
             ZERO occurrences in the artifact that enumerates the shapes (N3). ***
     YIELDS  a SET of permitted values — genuinely set-valued, displayed at cardinality
             EMPTY, SINGLETON, k-PARAMETER FAMILY, and UNBOUNDED (N4)

     WHAT IT SELECTS OVER    the freedoms of a condition — "n conditions, n freedoms"
     PER-STAGE OR GLOBAL?    *** NEITHER — PER-CONDITION.  There is no stage index, and
                             each condition carries its own set.  A third thing. ***
     NON-SINGLETON?          YES, at three non-singleton cardinalities (N4).
     REVERSE CHECK?          The classifiers never return a set (N5).  Neither is in
                             disguise; the split is real in both directions.
```

**THE CONSEQUENCE (DELIVERABLE 4), DISPLAYED:**

```text
Selector-shaped content EXISTS, so the invariance question is live — AND THE PIECES TO
STATE "INVARIANT ACROSS EVERY APPLICATION OF IT" ARE NOT PRESENT.

  (a) a single map to be the "it"      ABSENT — a per-condition family with NO index set;
                                       "the admissible set" occurs twice in G1, both times
                                       with a definite article and no stated domain (N7)
  (b) a domain for "every"             ABSENT — named once, in the subjunctive: "would
                                       matter in a registry of forcing candidates" (N8)
  (c) that domain populated            ONE executed member, and the members are mutually
                                       incommensurable — different carriers (N9)
  (d) a quantity held fixed            NOT REACHED — (a) fails first

*** THE FAILURE IS AT (a) AND IS STRUCTURAL, NOT A THIN CENSUS.  THERE IS NO SINGLE
SELECTOR FOR AN INVARIANCE TO BE AN INVARIANCE OF.  ADDING MEMBERS WOULD NOT REPAIR IT. ***
```

**DISPLAY ONLY.** O18SR types what exists and stops. Nothing proposed, nothing authored,
nothing adopted, nothing reclassified. No registry nominated, no index set suggested, no
member put forward, and no statement about whether any of this should be built.

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
