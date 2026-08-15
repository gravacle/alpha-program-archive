CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = CLAIMED
CLOSURE_BEGIN_BYTE = 00000000
PREDECLARATION_OUTPUT_SCAN = 0 hits for this artifact and its sidecar
POSTURE = DEFAULT-REFUTE. Testimony carries zero weight. Every claim re-derived at bytes.
UNDECLARED_SOURCE_VERDICT_WEIGHT = forbidden
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

| # | Consumed artifact | SHA-256 (recomputed by me) | `shasum -c` from its own directory | Role |
|---:|---|---|---|---|
| 01 | `STAGE8_CONSTRUCTION_ROUTES_O16SR_V001.md` | `b6ca4f8b58245fb4de385f09d986089d560d6a311604a66ec250dfd6659f6fcc` | OK | **THE TARGET** |
| 02 | `STAGE8_AXN_ENTRY_DECISION_INSTRUMENT_CODEX2_V001.md` | `c650c578c8625ffba7e1e33713e65a10623adb41444a5bb95f76d76c4ced5046` | OK (both roots) | the instrument, V001 |
| 03 | `STAGE8_AXN_ENTRY_DECISION_INSTRUMENT_CODEX2_V002.md` | `af26ab0354420f64718942b9bdcc61a4e6826a885b7ac0440988a25d7f0c95e1` | OK (both roots) | the instrument, V002 |
| 04 | `STAGE8_PRODUCTION_VS_DESCRIPTION_O13SR_V001.md` | `587872a33596e81cb128aa62f77504da592df3831666b2e271356dd819276e14` | OK | the absence claim |
| 05 | `STAGE8_PRODUCTION_VS_DESCRIPTION_O13SR_AUDIT_V001.md` | `82d822dd09d33d9a464a18d6120405ef47510e35c4d62ff779b29fd3724abce7` | OK | correction C-5 |
| 06 | `STAGE8_FORCING_NOTION_O12SR_V001.md` | `839f5079bb4ff89f2d02e35a60333fc888643300feda8b0e17d610fb54e207bb` | OK | the absence result |
| 07 | `STAGE8_FORCING_NOTION_O12SR_AUDIT_V001.md` | `31949c577ec8dcbfc8ace72adc7fb19542e7f5f9c9c48e29f3cca97ebe0f9afd` | OK | its audit |
| 08 | `JOINT_ANCHOR_DECISION_INSTANCE_V002.md` | `72191e0115d6f36d2327236e7a6d16e21f953422ba3fb2188b75e3db009cea99` | OK | the record instance the target consumed |
| 09 | `STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V002.md` | `58b966ed371b23b29b9e3ceed280eb30c804484becb2b17ca6ea465668e951bc` | OK | instrument member 07; opened to re-derive span digests |

Artifact 09 is outside the target's own read set. I opened it because the target's §2.1
and §5.1 both rest on span digests pinned *by the instrument* into member 07, and a
DEFAULT-REFUTE audit may not accept a pin on the pinning artifact's word. It is a sealed
decision instrument, not a register/tracker/road/plan/continuation file.

CLOSURE_DECLARATION_END

# STAGE 8 — AUDIT OF THE CLAIMED-EXHAUSTIVE PRICED ENUMERATION OF CONSTRUCTION ROUTES

## ROUTES-AUDIT — COMMISSION O16SR — 2026-08-15 — [CLAIMED]

---

## §0 — PROBE, SEALS, SWEEPS, CUTOFF

### §0.1 STEP 0

```text
TARGET             STAGE8_CONSTRUCTION_ROUTES_O16SR_V001.md              PRESENT
TARGET SIDECAR     STAGE8_CONSTRUCTION_ROUTES_O16SR_V001.md.seal.sha256  PRESENT
shasum -a 256 -c, run from the artifact's own directory                  OK
MY OUTPUT PATH     STAGE8_CONSTRUCTION_ROUTES_O16SR_AUDIT_V001.md        ABSENT before I wrote
MY OUTPUT SIDECAR  ...AUDIT_V001.md.seal.sha256                          ABSENT before I wrote
-> lawful to proceed.
```

### §0.2 SEAL VERIFICATION — MINE, NOT THE TARGET'S

Ten `shasum -a 256 -c` verifications, each **run from the artifact's own directory**: eight
in ROOT 1, and the two instrument versions again in ROOT 2. Ten `OK`, zero `FAILED`. I also
recomputed all nine whole-file digests independently: **every digest in the target's closure
table reproduces exactly.** The two instrument versions are byte-identical across both roots,
as the target claims.

### §0.3 MY SWEEPS, AS RUN

```text
ROOT 1 = /Users/bgm/MB Work/alpha-program-archive/workspace                    (3592 entries)
ROOT 2 = .../alpha_fundamental_record_action_cleanroom_v003                    (3133 entries)

A-1  RE-RUN OF THE TARGET'S S-1.  grep -rl "every lawful construction route and price",
     both roots, uncapped, no --include.
     ROOT 1 -> 6 paths; ROOT 2 -> 2 paths.
     The sixth ROOT 1 path is the target artifact itself, written at 15:30, AFTER the
     target's declared cutoff of 15:24:55. Discounting it, ROOT 1 -> 5 paths, exactly the
     five the target names (V001, V002, O12SR, O12SR-AUDIT, O13SR-AUDIT).
     *** TARGET'S S-1 CONFIRMED AT BYTES, INCLUDING ITS COUNTS. ***

A-2  RE-RUN OF THE TARGET'S S-3.  grep -niE "both|mutually|exclusive|disjoint|at most
     one|either" over V002 :205-266.
     -> 7 hit lines, each opened. NONE asserts the pairing families are mutually exclusive.
     *** TARGET'S S-3 CONFIRMED. F-1's basis holds. ***

A-3  PRICE CENSUS.  Mechanical count of all nine price prefixes over the whole of V002.
A-4  NEGATIVE-CLAUSE CENSUS.  Mechanical count of all eight closing denial strings.
A-5  ROUTE-TABLE CENSUS.  grep -nE '\| `(P-|EJ-|E-|F-|S-|IA-|PCH-)' over V002, plus the
     complete heading list.
A-6  QUOTATION AUDIT.  Every line-cited quotation in the target checked against its source
     span. Results in §5.
A-7  FENCE-SCAN of the target: fences, lens tokens, measured constants, program numbers,
     first-person adoption/proposal verbs.

SWEEP CUTOFF: 2026-08-15T15:40:39-0500. Nothing entering either root after that instant is
consumed or claimed about.
```

---

## §1 — WHAT I RE-DERIVED, AND WHAT REPRODUCED

Everything below was recomputed from bytes. The target's testimony was given no weight.

```text
REPRODUCED EXACTLY:
  - all 9 whole-file digests in the closure table
  - 10 seal verifications from own directories, both roots
  - sweep S-1 (5 / 2 paths) and sweep S-3 (zero exclusivity clause)
  - the price census: FILLED 21, BLANK 7, TOTAL 28
  - the negative-clause census: 21 of 21 filled drafts close with a denial
  - all four CAS checks C1-C4, in a fresh venv (sympy 1.14.0), exact symbolic
  - the V001/V002 identity of the four pairing-route rows (byte-identical row hashes)
  - three member-07 span digests, recomputed from member 07's own bytes

DID NOT REPRODUCE:
  - the count "six priced route tables". The true count is SEVEN.   -> CORRECTION X-1
  - the count "three of the classes are open residuals" as displayed. The block shows
    FOUR, and the fourth is sustained only by an elided proviso.     -> CORRECTIONS X-2/X-3
```

### §1.1 THE PIN CHECK THE TARGET DID NOT RUN

The target quotes member 07's schema-demand bytes through the *instrument's own* pin rows
(V002 :67, :70, :77-80) and never opens member 07. Under DEFAULT-REFUTE that is a pin on the
pinning artifact's word. I opened it and recomputed:

```text
member 07 = STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V002.md
  whole-file SHA-256 = 58b966ed371b23b29b9e3ceed280eb30c804484becb2b17ca6ea465668e951bc
  -> identical to the const pinned at V002 :232 (delta0_definition_source_sha256).
     The member-07 identification is confirmed at bytes, not by testimony.

  [10078,10161)  -> 88f6f781...c9a87e   MATCH
                    "  scalar_pairing_or_trace: faithful declared pairing with
                     normalization convention,"
  [10504,10586)  -> ecae37fa...ce62af   MATCH
                    "  physical_price: explicit statement of every authored
                     carrier/pairing/fiber datum"
  [12531,13022)  -> ac54740d...7bb094   MATCH   (the reverse-A2 receiver)

*** THREE FOR THREE. The instrument's pins are sound and the target's §2.1 and §5.1
    quotations of them are exact at the byte level. This strengthens the target. ***
```

---

## §2 — HARDEST HUNT: IS THIS A DOMAIN-CANDIDATE VERDICT IN DISGUISE?

The commission's first hunt is for a DOMAIN-CANDIDATE verdict where the enumeration in fact
ranges over objects **within an existing record** — the wishful outcome that would falsely
revive a closed question. I hunted it first and hardest.

### §2.1 THE VERDICT AS WRITTEN

```text
TARGET §7 bottom line, :732 verbatim:
  "=> COULD IT SERVE AS THE DOMAIN A GENERATIVE NOTION OF FORCING LACKS?  NO."
TARGET §11 flag block, :856 verbatim:
  "DOMAIN FOR A GENERATIVE NOTION OF FORCING = NO."

*** THE TARGET RETURNS **NO**, TWICE, IN TWO SEPARATE TERMINAL BLOCKS.
    IT DOES NOT DELIVER A DOMAIN-CANDIDATE VERDICT. THE CLOSED QUESTION IS NOT REVIVED. ***
```

The one phrase that could be misread is the §7 right-margin tag `[DOMAIN-CANDIDATE HORN —
GRANTED]` at :707-708. Read at its own scope it grants **one horn of the commission's
two-horn question** — that the elements are makings — and the very next numbered block
grants the opposing horn while the third denies the domain outright. Quoted alone the tag
would mislead; in place it does not. **No defect, but I record it as the artifact's one
quotable-out-of-context line.**

### §2.2 THE DEMAND: THE INSTRUMENT'S OWN WORDS ON RECORD-VS-OBJECT

I demanded, as instructed, the instrument's own words establishing that these are routes to
an **object in a record** rather than to a **record**. The target supplies four independent
byte-level grounds. I verified all four in their source spans, unelided:

```text
G-1  THE RECEIVER'S TYPE.  member 07 [10078,10161), digest recomputed by me above:
       "scalar_pairing_or_trace: faithful declared pairing with normalization convention,"
     -> the thing constructed is A PAIRING. A pairing is not a record.

G-2  THE VALUE SPACE IS EMPTY.  V002 :105, verified verbatim in the authority table:
       Record-native exact-value space: EMPTY
       Authority: "member 05 §3.3; the two located pairings are source-sector objects,
                   not joint-carrier pairings"
       Lawful completion route: "author a cross-sector extension of either seed, or
                                 author an independent joint pairing"
     -> the object is absent from the record; the route makes it. Not a selection.

G-3  THE RECORD FACTOR PRE-EXISTS THE ROUTES.  V002 :319 and :354, both verified verbatim:
       :319  `E_joint = E_ch (x) id_R_inf (x) id_B`
       :354  `i_src(a)=a tensor 1_R_inf tensor 1_B`
     and V002 :319's required column names the sectors: "the record/history actions are
     trivial". V002 :213 P-HS likewise: "extend the source-fiber pairing across record and
     history sectors". The three-sector reading source / RECORD / history is RECORD-NATIVE,
     not the target's import.
     -> R_inf is a factor of the carrier. EJ-TRIVIAL acts on it by id_R_inf; EJ-NONTRIVIAL
        acts on it nontrivially. NO ROUTE IN ANY TABLE HAS R_inf AS ITS OUTPUT.

G-4  THE RECORD INSTANCE PRE-EXISTS THE ROUTES.  JOINT_ANCHOR_DECISION_INSTANCE_V002 :334,
     verified verbatim and unelided:
       "the entries — transcribed perfectly — POPULATE TWENTY FIELDS AND LEAVE NINETEEN
        EMPTY. Reformatting cannot close that; those fields need new principal entries."
     and V002's own closure row 06, verified verbatim:
       "current partial instance; all eight receivers remain open"
     -> the routes fill empties in an instance that already exists and is sealed.

*** ALL FOUR GROUNDS CONFIRMED AT BYTES. THE ROUTES ARE ROUTES TO AN OBJECT IN A RECORD.
    THE TARGET DEMANDED THE RIGHT WORDS AND GOT THEM. ***
```

### §2.3 THE COUNTER-BYTES I WENT LOOKING FOR

DEFAULT-REFUTE obliges me to hunt for bytes that would *undo* the within-record finding. I
found the strongest candidate and record it rather than suppress it:

```text
THE ROUTES REQUIRE AN ACT ABOUT THE CARRIER ITSELF.
  V002 :213 and :214, P-HS and P-CT required columns, both open:
      "declare the exact joint carrier; ..."
  V002 :351-355 repeatedly: "into entered `A_C0`" ; :354 "after the principal binds the
      source factor of entered `A_C0`".
  -> A_C0 is ENTERED and its source factor is BOUND by the principal. So the carrier that
     carries R_inf is not simply lying about untouched.

WHY IT DOES NOT UNDO THE FINDING, AT BYTES:
  V002 :344-345 verbatim: "Member 09 `[10436,10550)`, span SHA-256 `7cae6616...`, declares
  the tensor presentation ending in `A_C0`." The FACTORISATION is sealed at member 09; what
  the entry supplies is a DECLARATION/IDENTIFICATION of the exact carrier and a typed
  embedding into it. Declaring which sealed carrier one means is not producing its record
  factor. No route's output column names R_inf.

WEIGHT: the target's §4.5(a) phrase "already there, sealed, before any route is taken" is
  stronger than the bytes strictly license, and §4.5 never reconciles it with the "declare
  the exact joint carrier" requirement. But the target DISPLAYS that requirement in full,
  verbatim, in its own §1.2, eleven pages earlier. It hid nothing. The conclusion stands on
  the output columns alone.
  -> NOTED, NOT A CORRECTION. The target's restraint here is real.
```

### §2.4 VERDICT ON HUNT 1

```text
*** NOTHING FOUND. The target does not deliver a DOMAIN-CANDIDATE verdict, does not revive
    the closed question, and establishes object-in-a-record from the instrument's own words
    at four independent byte-level grounds, all of which I reproduced. ***
```

---

## §3 — HUNT 2: IS THE EXHAUSTIVENESS CLAIM READ AS DERIVED?

The commission's second hunt: an exhaustiveness claim read as **derived** where the
instrument flags it as **claimed**. The target grades it CLAIMED-WITH-A-FLAG. I checked each
of its three grounds in source, unelided.

```text
(a) V002 :205 heading, verbatim:
      "## 3. Pairing root: every lawful construction route and price [CLAIMED]"
    CONFIRMED. The tag is on the heading itself.
    V002 :51-52, verbatim, complete sentence:
      "Every substantive heading and disposition is **CLAIMED** until opposite-lane or
       registrar review."
    CONFIRMED verbatim, bold as in source.

(b) V002 :84-85, verbatim, complete, both sentences, bold as in source:
      "The option list is complete by **route class**. A route class may receive
       content-addressed instance bytes later; this document supplies no such bytes and
       chooses no class."
    CONFIRMED. *** ZERO ELISION. This is the target's load-bearing quotation and it is
    reproduced whole, including the scope-narrowing second sentence. ***

(c) V002 :457-458, verbatim, complete:
      "**BUILDER-NEVER-VERIFIES:** this artifact is CLAIMED. Member 05 supplies the
       opposite-lane census; this builder does not confirm its own option completeness or
       price adequacy."
    CONFIRMED verbatim.

CORROBORATION AT :532, verified verbatim:
  "OPTION_SPACES = COMPLETE / (V001 classes retained; E_joint adds trivial-extension,
   lawful-nontrivial, and blank classes with labelling costs pinned)"

*** NOTHING FOUND. The grade CLAIMED-WITH-A-FLAG is correct and is the instrument's own.
    The target nowhere reads the exhaustiveness as derived. ***
```

### §3.1 F-1 RE-DERIVED INDEPENDENTLY, AND CORROBORATED

The target's finding F-1 — that the cell (extends_HS=1, extends_CT=1) is unassigned —
reproduces in my fresh venv (§6). I add one corroboration the target did not find:

```text
THE INSTRUMENT SUPPLIES AN EXCLUSIVITY SENTENCE FOR THE **EJ** FAMILY AND NOT FOR **P**.
  V002 :323-324 verbatim: "These three classes are exhaustive by whether the exact joint map
  is the displayed trivial extension, a different lawful joint expectation, or absent."
  That sentence makes EJ-* disjoint by construction. No sentence of that form exists
  anywhere for P-HS / P-CT / P-NEW.
-> The asymmetry is displayed in the instrument's own bytes. F-1 is not an artifact of the
   target's reading; the instrument knew how to write the missing clause and wrote it once,
   for a different receiver. THIS STRENGTHENS F-1 AND IS MY CONTRIBUTION, NOT THE TARGET'S.

WEIGHT, UNCHANGED FROM THE TARGET'S OWN GRADING: a disjointness gap, not a coverage
counterexample. I do not close it and I propose no clause.
```

---

## §4 — HUNT 3: ARE THE PRICE SEMANTICS INVENTED OR QUOTED?

The commission's third hunt: price semantics invented rather than quoted. This is the
target's §5. I audited every load-bearing element.

```text
QUOTED, AND VERIFIED BY ME AT BYTES:
  :70   the physical_price schema demand   -- and I recomputed its span digest from
        member 07's own bytes: [10504,10586) -> ecae37fa...ce62af  MATCH
  :108  "**EMPTY BY TYPE** ... this is a **disclosure of what the entry authors**"
        CONFIRMED; the ellipsis is MARKED and elides only the member-05 citation.
  :77-80 the reverse-A2 receiver, complete, including "That receiver governs every price
        draft below."  CONFIRMED verbatim; span digest ac54740d...  MATCH.
  :291  "A PARTIAL PRICE IS NOT A FILLED OPTION."  CONFIRMED verbatim.
  :261  "Each combination inherits the family price plus the branch price."  CONFIRMED.
  :445-447 the anti-tuning prohibition, COMPLETE, all three sentences.  CONFIRMED.
  :533  "PRICES_DRAFTED = per-option / (no filled option unpriceable; blank routes
        expressly retain incompleteness)"  CONFIRMED verbatim.

COUNTED, AND RECOUNTED BY ME MECHANICALLY OVER V002's OWN BYTES:
  AUTHORED: 3 | HISTORY PRICE: 3 | SUPERSELECTION 2+1 | EQUIVALENCE 2+1 | FIBER 2+1
  EMBEDDING 5+1 | I_A 2+1 | P_ch 2+1 | NO AUTHORED PAIRING PRICE 1
  FILLED 21   BLANK 7   TOTAL 28
  *** THE TARGET'S §5.3 CENSUS REPRODUCES EXACTLY, PREFIX BY PREFIX. ***

  Negative-clause census, all eight strings counted mechanically:
    2 + 1 + 2 + 2 + 4 + 5 + 1 + 1 = 18, plus the three H-* clauses = 21.
  *** 21 OF 21 FILLED DRAFTS CLOSE WITH A DENIAL. THE TARGET'S §5.5 FINDING REPRODUCES. ***

COINED, AND SELF-FLAGGED BY THE TARGET:
  "anti-derivation declaration" — declared IMPORTED at IA-2 with the words
  "Reject the name freely; the count stands."
  "epistemic currency" — declared IMPORTED at IA-7 as "a metaphor", with the bytes
  restated plainly: "derived independently or priced expressly".

*** NOTHING FOUND. The price semantics are quoted, not invented. Every magnitude claim is a
    count I reproduced. The two coinages are flagged by the target itself, in advance, with
    the underlying byte-facts stated separately so the reader can discard the names. ***
```

---

## §5 — HUNT 4: THE DAY'S RECURRING DEFECT — HEDGES DROPPED FROM INSIDE QUOTED SENTENCES

Every line-cited quotation in the target was checked against its source span. I count
**43 distinct cited spans**: 30 in V002, 1 in V001, 1 the V002 closure row 06, 3 in O12SR,
1 in O12SR-AUDIT, 1 in O13SR, 4 in O13SR-AUDIT, 2 in JOINT_ANCHOR_DECISION_INSTANCE_V002.

```text
40 of 43  EXACT IN SUBSTANCE — every word of the quoted span reproduced, elisions marked.
 3 of 43  DEFECTIVE:  X-3  the E-CLASS proviso, elided unmarked from inside the sentence
                      X-4  the S-NEW truncation at :355, unmarked
                      X-7  the :43-44 self-title, dropping "[PLAN:AXN-BUILD-C33] — [CLAIMED]"
 7 of 43  carry emphasis or dash normalization not present in the source, with no words
          added, dropped, or reordered. Logged at X-7, no substance at risk.
```

One of the three is the day's pattern exactly.

### §5.1 CORRECTION X-2 / X-3 — THE E-CLASS PROVISO

This is the finding of this audit.

```text
TARGET §4.3 :427-428, presented as a quotation with a line cite:

    E-CLASS        "covers a singleton nonidentity change and ANY LARGER FINITE OR
                    GRAMMAR-CERTIFIED CLASS"                                  (:297)

V002 :297-299, THE SOURCE SPAN, IN FULL:

    "`E-CLASS` also covers a singleton nonidentity change and any larger finite or
     grammar-certified class, provided its membership and invariance test are exact.
     An unbounded adjective without a receiver is not an option."

WHAT WAS DROPPED, UNMARKED, FROM INSIDE THE QUOTED SENTENCE:
    *** "provided its membership and invariance test are exact" ***
AND WHAT SITS IMMEDIATELY AFTER IT, UNDISPLAYED:
    *** "An unbounded adjective without a receiver is not an option." ***
```

The elided proviso is the exact clause that **bounds** the class, and the undisplayed next
sentence **names and bars the very word the target then uses**. The passage's purpose is to
argue that E-CLASS is an "open residual" of "unbounded size". V002 :293 reinforces what was
dropped: `E-CLASS` requires "a content-addressed, **closed member list** of representation
changes, exact induced maps, and a commuting/invariance certificate".

```text
X-2  E-CLASS DOES NOT BELONG IN THE OPEN-RESIDUAL LIST. Strike it.
X-3  THE QUOTATION MUST CARRY ITS PROVISO, and the barring sentence at :298-299 must be
     displayed beside it.
```

**And the target's own text already agrees.** Its §4.3 sentence introducing the block says
"**three** of the classes are expressly open residuals" — then displays **four**. Its own
CAS check C4 lists exactly three: `P-NEW / S-NEW / EJ-NONTRIVIAL`. Its §4.6 and §7(3) both
say "three classes". **E-CLASS is the odd item out by the target's own count, in four
separate places.** Striking it makes the artifact self-consistent and costs it nothing.

```text
WEIGHT, STATED HONESTLY: the finding of §4.3 is that the enumeration bounds the PARTITION
and leaves the POPULATION unbounded. That rests on :84-85 — quoted whole, unelided, with
its scope-narrowing sentence intact — and on three residual classes, which survive.
*** THE ELISION IS REAL AND IT IS THE DAY'S PATTERN. IT DOES NOT MOVE THE FINDING. ***
```

### §5.2 CORRECTION X-4 — AN UNMARKED MID-SENTENCE TRUNCATION

```text
TARGET §4.3 :423-424, cited (:355):
    "author ANY OTHER exact total typed embedding from the required source carrier into
     entered A_C0"
V002 :355 in full:
    "author any other exact total typed embedding from the required source carrier into
     entered `A_C0` and seal its proof obligations"
DROPPED, UNMARKED: "and seal its proof obligations".
```

Lower weight than X-2/X-3: the dropped clause is an obligation on each instance, not a bound
on the class, so the residual-openness point survives untouched. But it is the same hygiene
failure and I record it at the same standard.

### §5.3 THE ELISIONS THAT DID **NOT** HAPPEN — WHERE THE TARGET HELD

Under DEFAULT-REFUTE the negative result must be displayed as carefully as the positive one.
These are the four places where the day's defect would have paid best, and the target held:

```text
H-1  O12SR :482-484. The "shape sought" sentence carries a parenthetical hedge:
       "(named here as the search target, NOT proposed and NOT adopted)"
     *** THE TARGET REPRODUCES THE HEDGE IN FULL, INSIDE ITS OWN BLOCKQUOTE, AND REPEATS
         "(and expressly not adopted there)" IN ITS OWN LEAD-IN. ***

H-2  V002 :84-85. Both sentences, whole, bold intact. This is the sentence the target's
     entire deliverable (4) turns on. No trim.

H-3  V002 :445-447. All three sentences of the anti-tuning prohibition, whole. The target
     could have quoted only "No route is selected, ranked, ... called cheaper" and dropped
     the equal-treatment sentence. It did not.

H-4  O13SR-AUDIT :445-447. The target quotes "the thing made is a JOINT PAIRING on a joint
     carrier, not a RECORD" and stops. The dropped continuation is "So it does NOT overturn
     the target's category (b) verdict, and I do not claim it does." — but the target
     RESTATES that content itself, twice, at §4.5 and §7(2): "O13SR's category (b) verdict
     SURVIVES INTACT." The substance is carried, not lost. NOT A DEFECT.
```

### §5.4 THE SCOPE QUESTION THE TARGET GOT RIGHT

The one place a scope error would have been fatal:

```text
O13SR :378-380 reads, in full:
  "THERE IS NO SET, CLASS, CATEGORY, SPACE, MODULI, OR INDEXED FAMILY OF RECORD
   PRODUCTIONS ANYWHERE IN EITHER ROOT.  There is nothing for a quantifier to range over."

The first sentence is scoped to RECORD PRODUCTIONS. The second, as written, is not. The
target declares the second FALSE AT BYTES — while its own §4.5 concludes the routes are NOT
record productions. Read carelessly that is self-contradiction.

IT IS NOT, AND THE BYTES SETTLE IT:
  O13SR-AUDIT C-5(iii) :461-463 verbatim: "IT IS WHAT MAKES §1.5's BROAD SENTENCE FALSE. A
  corpus that enumerates 'every lawful construction route' and prices each one HAS something
  for a quantifier to range over."
  The audit falsifies the sentence *as broadly phrased*, and I confirmed :378-380 sits in
  O13SR §1.5 (§1.6 opens at :382). The target's cite maps to the audit's scope exactly.
  And the target narrows it itself, in the same paragraph, :401 verbatim: "Something
  enumerable does exist." — then §4.3 states precisely WHAT: four labels, not the makings.

*** COHERENT. The target falsifies the broad sentence, grants the narrow one, and never
    claims the routes are record productions. NO SCOPE DEFECT HERE. ***
```

---

## §6 — CAS BATTERY, RE-RUN INDEPENDENTLY (FRESH VENV; EXACT SYMBOLIC)

```text
VENV: created for this audit only, in my scratchpad. sympy 1.14.0, python 3.9.6.
  I did not run, read, or import the target's `cas_o16.py`. Checks re-specified from the
  instrument's bytes and run blind.
SCOPE DECLARATION: every quantity below is DOCUMENT COMBINATORICS — counts of labels in a
  markdown table and algebraic properties of string concatenation. NO PHYSICAL VALUE, NO
  PROGRAM QUANTITY, AND NO MEASURED CONSTANT IS COMPUTED, QUOTED, OR COMPARED.
  alpha_computed = false · proof_authorized = false · kappa_record_computed = false.
```

```text
[A-C1] REPRODUCES.  sympy FiniteSet: |P|=3, |H|=3, |P x H|=9, and Integer(9)==Integer(9)
       True. The instrument's own arithmetic at :259-261 is correct. Filled families
       including P-BLANK = 4.

[A-C2] REPRODUCES.  Concatenation: associative True, commutative False, identity ""
       present -> free monoid, as the target says. No order relation is definable from
       anything the instrument supplies; comparability is not a well-formed question.
       Independently grounded at :445-447, which I verified verbatim and complete.

[A-C3] REPRODUCES.  (0,0)->P-NEW  (0,1)->P-CT  (1,0)->P-HS  (1,1)-> UNASSIGNED.
       Uncovered cells = [(1,1)]. Sweep A-2 confirms no exclusivity clause. F-1 STANDS,
       at the target's own weight: a disjointness gap, not a coverage counterexample.

[A-C4] REPRODUCES IN SUBSTANCE, WITH ONE WORDING CORRECTION.
       |route classes at the pairing root| = 4, finite and displayed.  CONFIRMED.
       The population of P-NEW / S-NEW / EJ-NONTRIVIAL is never fixed anywhere in the
       instrument.  CONFIRMED — I grepped for any cardinality statement and found none.
       CORRECTION X-5: the target calls n "an unbounded positive integer symbol".
       In sympy, Symbol('n', integer=True, positive=True).is_finite returns True. The
       operative and correct claim is that n is NEVER FIXED — which the target also says,
       in the same line, in capitals. "Unfixed", not "unbounded". Wording only; the
       partition-bounded / population-unfixed result is unaffected.
```

---

## §7 — CORRECTIONS, IN FULL

```text
X-1  COUNT ERROR: "SIX PRICED ROUTE TABLES". THE TRUE COUNT IS SEVEN.
     The target's §1.4 says the instrument runs the route table "at FIVE further receivers"
     — and then displays a table with SIX rows. It concludes the enumeration is "a
     six-receiver family of priced route tables, OF WHICH THE PAIRING ROOT IS ONE" — but
     the pairing root is not among the six rows.
     MY CENSUS (A-5), from V002's own ID-labelled rows:
       §3.1  P-*    4 IDs   pairing root
       §4    E-*    3 IDs   equivalence_scope
       §4.1  EJ-*   3 IDs   joint_superselection_map
       §5    F-*    3 IDs   fiber_label
       §6    S-*    6 IDs   i_src
       §7    IA-*   3 IDs   I_A_sha256
       §8    PCH-*  3 IDs   P_ch_sha256
       -> SEVEN ID-labelled priced route tables at SEVEN receivers.
          (The H-* branch table at §3.2 is a second AXIS on the pairing root, not a seventh
          receiver; the target treats it that way and is right to. The two remaining schema
          fields, entered_pairing_sha256 and physical_price, receive numbered option lists
          at §4 without ID labels — which is why FIELDS_COVERED = 9.)
     PROPAGATION: "six" recurs at §4.5 (twice) and §7(1). The target's own §3.3 states it
     CORRECTLY — "six route tables plus the pairing root" — so the artifact contradicts
     itself, and the correct form is already in it.
     DIRECTION OF THE ERROR: it UNDERSTATES the object. The target uses the count to show
     C-5 was understated ("six, not one"); at seven the point is stronger. No conclusion
     depends on the value.

X-2  STRIKE E-CLASS FROM THE OPEN-RESIDUAL LIST (§4.3). The instrument requires a
     "content-addressed, closed member list" (:293) with "membership and invariance test
     ... exact" (:297-298). Three residuals remain, which is what the target's own prose,
     its C4, its §4.6 and its §7(3) all already say.

X-3  RESTORE THE ELIDED PROVISO AND ITS NEIGHBOUR (§4.3, cite :297). Add "provided its
     membership and invariance test are exact", and display :298-299 "An unbounded
     adjective without a receiver is not an option."

X-4  MARK THE TRUNCATION AT :355 (§4.3). "...into entered `A_C0`" drops "and seal its
     proof obligations" with no ellipsis.

X-5  "UNFIXED", NOT "UNBOUNDED", FOR n (§4.3, C4). Wording only.

X-6  IMPORT AUDIT OMITS ITS MOST LOAD-BEARING NOTION: **"record"**. §10 declares ten
     notions and never declares this one. The deliverable is whether the makings are
     makings OF A RECORD, and §4.5 answers it in TWO DIFFERENT SENSES without saying so:
       (a) the RECORD FACTOR R_inf, a tensor factor of the carrier A_C0;
       (b) the RECORD INSTANCE, a sealed markdown artifact with twenty populated fields.
     Both are record-native usages — (a) at V002 :213/:319, (b) at the closure row 06 —
     but they are different objects, and O12SR/O13SR's "productions of a RECORD" is a
     third usage matching neither exactly.
     WEIGHT: the D-iii determination is ROBUST ACROSS ALL THREE READINGS — no route outputs
     a record under any of them — so the conclusion is untouched. The defect is the
     UNDECLARED SHIFT, in the one audit section built to catch exactly that.

X-7  QUOTATION-FORMATTING HYGIENE, LOW WEIGHT, NO SUBSTANCE AT RISK.
     - Bold emphasis added inside blocks headed "verbatim" at :62-63, :77-80, :108,
       :378-380, :445-447, :477. In each case the source carries no such bold.
     - "Hilbert–Schmidt" (en dash) rendered "Hilbert-Schmidt" (hyphen) throughout §1.2,
       a block headed VERBATIM. Note the instrument's own :449 lists "Hilbert–Schmidt
       spellings" among its M-2 normalized-name checks, so the corpus treats this as a
       known variant axis.
     - §1 renders the :43-44 self-title as a quotation while silently dropping
       "`[PLAN:AXN-BUILD-C33]` — [CLAIMED]".
```

### §7.1 WHAT I COULD NOT FAULT

```text
- Every whole-file digest, every seal, both roots.                    REPRODUCED.
- Sweeps S-1 and S-3, including their counts.                         REPRODUCED.
- The 28-draft price census, prefix by prefix.                        REPRODUCED.
- The 21-of-21 negative-clause census.                                REPRODUCED.
- All four CAS results, re-specified and run blind in a fresh venv.   REPRODUCED.
- The V001/V002 byte-identity of the four pairing rows (CL-1).        REPRODUCED.
- The three member-07 span digests the target took on the pins.       REPRODUCED.
- The exhaustiveness grade CLAIMED-WITH-A-FLAG.                       CORRECT.
- The within-record determination, on four independent grounds.       CORRECT.
- The price semantics, quoted with both coinages self-flagged.        CORRECT.
- Fences, lens tokens, program numbers, adoption verbs.               CLEAN (§8).
```

---

## §8 — FENCE-SCAN OF THE TARGET

```text
FENCES        alpha_computed / proof_authorized / kappa_record_computed = false, declared
              at :9-11, restated in the §6 CAS scope line at :665 and in §11 at :824-826.
              UNCHANGED THROUGHOUT. No step in the target touches any of them.
LENS TOKENS   grep -niE "\blens\b|lensing|\bLENS_"  ->  ZERO HITS.
CONSTANTS     grep for 137, fine-structure, CODATA, 1/137, 7.29e-3, "alpha =", "α ="
              ->  ZERO HITS. No measured constant is consulted, quoted, or compared.
NUMBERS       Every integer in the target is a count of labels or drafts in a markdown
              table (4, 3, 9, 21, 7, 28, 20, 19), or a line/byte cite, or a digest. I
              checked each occurrence. NO NUMBER APPEARS AS A PROGRAM QUANTITY.
              The §11 VALUES line declares this and the declaration is accurate.
PROPOSAL /    grep -niE "I adopt|we adopt|I propose|we propose|I select|I recommend|
ADOPTION      is adopted by me|hereby"  ->  ZERO HITS.
              The nearest approach is §7's closing note, which names a hypothetical
              construction ("if a future artifact enumerated the instances ... and ordered
              them by extension") in order to disclaim it: "That is a construction, not a
              reading, and I neither perform nor propose it." It is doubly hedged — it also
              says such a domain would be "still not for record productions". I looked hard
              at this as a covert revival and it is not one: it states a counterfactual and
              refuses it in the same sentence. NOT A DEFECT; recorded because it is the
              artifact's closest approach to one.
ENTRIES       0. The target selects no route, fills no receiver, prices nothing.
GIT           NOT USED, by me or (on its own declaration, which I did not need to trust)
              by the target — no git artefacts exist in either root path I touched.
```

---

## §9 — VERDICT

```text
PER DELIVERABLE:

(1) DISPLAY OF THE ENUMERATION (target §1)      CONFIRMED-WITH-CORRECTIONS
    Every route, price, and branch reproduced verbatim from V002 :209-261. The four
    pairing rows are byte-identical in V001 and V002, as CL-1 claims.
    CORRECTION X-1: seven priced route tables, not six; and §1.4's "five further
    receivers" contradicts its own six-row table. Understates the object.
    CORRECTION X-7: en dash normalized to hyphen inside a VERBATIM block.

(2) ROUTES FOR CONSTRUCTING WHAT (target §2)    CONFIRMED
    An OBJECT — a faithful pairing on the joint carrier — not a record, not an entry,
    not a member. Established at bytes on the receiver's own type (span digest recomputed
    by me from member 07), the EMPTY record-native value space at :105, and the act-verbs
    at :477. All three reproduce.

(3) THE EXHAUSTIVENESS CLAIM (target §3)        CONFIRMED
    CLAIMED-WITH-A-FLAG is the correct grade and it is the instrument's own, at three
    stacked markings I verified whole and unelided. Nowhere read as derived.
    F-1 reproduces in my own venv, at the target's own honest weight, and I ADD a
    corroboration: the instrument writes the missing exclusivity sentence for EJ-* at
    :323-324 and never for P-*.

(4) THE DOMAIN QUESTION (target §4)             CONFIRMED-WITH-CORRECTIONS
    (D-i) PASSES, (D-ii) FAILS, (D-iii) FAILS, (D-iv) FAILS: each re-derived.
    The determination NO is correct and is not a disguised DOMAIN-CANDIDATE verdict.
    CORRECTIONS X-2/X-3: E-CLASS is not an open residual, and its proviso was elided
    from inside a quoted sentence — the day's recurring defect, present here.
    CORRECTION X-4: unmarked mid-sentence truncation at :355.
    CORRECTION X-6: "record" is used in two senses in §4.5 and is absent from the
    IMPORT AUDIT.
    The finding survives all four: it rests on :84-85, quoted whole.

(5) WHAT A PRICE IS (target §5)                 CONFIRMED
    A disclosure, not a cost; denominated in authored content; governed by reverse-A2;
    composing by concatenation; unordered by express prohibition. Every quotation exact,
    every count reproduced mechanically, both coinages self-flagged in advance.

CAS BATTERY                                     CONFIRMED (X-5, wording only)
FENCE-SCAN                                      CLEAN
SEALS                                           10 verified by me, 10 OK, 0 FAILED
```

```text
=====================================================================
OVERALL VERDICT:            *** CONFIRMED-WITH-CORRECTIONS ***
=====================================================================

The three defects the commission ranked hardest are ABSENT:
  - no DOMAIN-CANDIDATE verdict, disguised or otherwise; the closed question is not
    revived, and the object-in-a-record finding is established on FOUR independent
    grounds in the instrument's own words, all of which I reproduced at bytes;
  - the exhaustiveness claim is read at exactly the grade the instrument flags;
  - the price semantics are quoted and counted, never invented, with the two coined
    names flagged by the target itself before use.

The fourth — the day's recurring defect, hedges dropped from inside quoted sentences —
IS PRESENT, ONCE, MATERIALLY: the E-CLASS proviso at :297-298, dropped unmarked from a
passage arguing that E-CLASS is unbounded, with the sentence "An unbounded adjective
without a receiver is not an option" sitting undisplayed on the next line.
It is a real defect and I do not soften it. It also does not move the finding, because
the target's own count of "three" residuals — repeated in four places, including its
CAS check — already excludes E-CLASS. Striking it makes the artifact self-consistent.

Seven corrections in all. NOT ONE OF THEM REVERSES A DELIVERABLE. Six of the seven
either understate the target's own object (X-1), tidy its wording (X-5, X-7), or name
an undeclared shift whose conclusion is robust across every reading of the shifted term
(X-6). The seventh (X-2/X-3/X-4) is a quotation-hygiene failure in one paragraph whose
load-bearing quotation — :84-85 — is reproduced whole.
```

---

## §10 — CHOICE LEDGER (commission O16SR audit; every unforced choice I made)

| # | Choice | Alternatives available | Why I chose it | Forced? |
|---|---|---|---|---|
| AL-1 | Opened member 07 (`STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V002.md`), outside the target's read set | accept the instrument's pin rows at :67/:70/:77-80 as the target did | DEFAULT-REFUTE cannot accept a pin on the pinning artifact's word; three span digests recomputed, three matched | UNFORCED — declared in closure table |
| AL-2 | Re-specified the CAS checks from the instrument's bytes and ran them blind, without reading `cas_o16.py` | run the target's own script | reproducing a script proves the script runs, not that the result is true | UNFORCED |
| AL-3 | Graded X-1 (six vs seven tables) a CORRECTION, not a refutation | treat a self-contradicting count as a failure of §1.4 | the error understates the target's own object and no conclusion depends on the value; and the target's §3.3 already states it correctly | UNFORCED |
| AL-4 | Graded X-2/X-3 (E-CLASS) a CORRECTION, not a refutation of deliverable (4) | refute (4) on the elision | the finding rests on :84-85, quoted whole; and the target's own count of three residuals already excludes E-CLASS in four places | UNFORCED |
| AL-5 | Displayed the counter-bytes in §2.3 ("declare the exact joint carrier") that cut against the within-record finding, and then explained why they do not defeat it | omit them, since the finding survives | DEFAULT-REFUTE means displaying the best case against the conclusion I confirm | UNFORCED |
| AL-6 | Added §5.3, an explicit census of the elisions that did NOT occur | report only the defects found | a hunt that reports only hits cannot be checked for a hunt that was not run | UNFORCED |
| AL-7 | Added the EJ-*/P-* exclusivity asymmetry (§3.1) as my own corroboration of F-1 | confirm F-1 on the target's own basis alone | re-derivation that finds nothing new has not tested the claim independently | UNFORCED |
| AL-8 | Recorded the `[DOMAIN-CANDIDATE HORN — GRANTED]` tag (§2.1) as quotable-out-of-context but NOT a defect | flag it as a covert revival | the same §7 block denies the domain outright two entries later, and §11 repeats NO | UNFORCED |
| AL-9 | Recorded X-7 (added bold, en dash, dropped title fragment) at all, at low weight | suppress formatting notes as noise | the commission ordered every quotation checked against its source span; a silent pass on formatting would misreport the check's scope | UNFORCED |
| AL-10 | Did not test falsifier F-C (a third sealed source-sector seed) | run a seed census across both roots | outside my declared sweeps, as it was outside the target's; I leave it open rather than close it silently | UNFORCED |
| AL-11 | CAS restricted to document combinatorics and string algebra | model the carrier; run no CAS | fences bar program quantities; the four checks touch only labels and concatenation | FORCED by fences |

---

## §11 — TOY_SEPARATION

```text
THIS ARTIFACT IS AN AUDIT OF SEALED BYTES. IT IS NOT A CONSTRUCTION.

WHAT IS ACTUAL SURFACE (all of it):
  - Ten seal verifications, each run by me from the artifact's own directory.
  - Nine whole-file digests and three byte-span digests, all recomputed by me.
  - Two sweeps re-run from scratch over both roots, uncapped.
  - Two censuses (28 price drafts, 21 negative clauses) counted mechanically from V002's
    own bytes, not read off the target.
  - Four CAS checks re-specified from the instrument and run blind in a fresh venv.
  - 43 cited spans checked against their sources; the three failures are displayed with
    the full source span beside them so any reader can check the diff.

WHAT IS NOT CLAIMED, AND WOULD BE A TOY IF IT WERE:
  - I construct no forcing notion, no domain, no partial order, no generic object.
  - I do not close F-1, do not supply the missing exclusivity clause, and do not propose
    one. I only observe that the instrument wrote such a clause once, for EJ-*.
  - I do not enumerate the members of any route class, nor fix n.
  - I do not reclassify the pairing root, adopt it, or move O13SR's category (b) verdict.
  - I do not select, rank, price, or recommend any route. Zero principal entries are
    filled by this artifact, exactly as zero are filled by the target and by the
    instrument.
  - I neither ratify nor repair the target. I state seven corrections and leave the
    artifact where its builder put it.

NO SIMPLIFIED MODEL, NO ILLUSTRATIVE CASE, AND NO STAND-IN OBJECT APPEARS ANYWHERE IN THIS
ARTIFACT. Every object named here is a sealed byte range in a named, digest-pinned file.
```

---

## §12 — IMPORT AUDIT (every notion I used, declared record-native or imported)

| # | Notion I used | Status | Basis / flag |
|---|---|---|---|
| AI-1 | "construction route", "price", "route class", "receiver", "authored", "pairing family", "history branch" | **RECORD-NATIVE** | the instrument's own vocabulary, quoted at bytes with line cites |
| AI-2 | **"record"** | **RECORD-NATIVE IN THREE DISTINCT USAGES — FLAGGED BY ME, AND THIS IS THE ONE THAT MATTERS** | (a) the carrier's record FACTOR `R_inf`, at V002 :213 "across record and history sectors" and :319 "the record/history actions are trivial"; (b) the record INSTANCE, at closure row 06 "current partial instance"; (c) "productions of a RECORD" at O12SR :482-484 and O13SR :378-380. All three are corpus usages; none is mine. I use all three and I am declaring the shift, because the target's §10 does not — that omission is my correction X-6, and I will not repeat it silently while reporting it |
| AI-3 | "domain", "quantify over", "range over", "invariant across" | **RECORD-NATIVE** | O12SR :482-484 and O13SR :378-380 use all four; I match their usage and do not extend it |
| AI-4 | "partition vs population" | **IMPORTED — ordinary set-theoretic vocabulary. FLAGGED, low weight.** | I inherit this name from the target. The distinction it names is record-native at :84-85. I could have avoided the name and did not, because the correction X-2 is stated most compactly in it |
| AI-5 | "free monoid", "associative", "commutative", "identity element", "partial order", "truth table", "uncovered cell" | **IMPORTED — standard algebra and logic. FLAGGED.** | Used only to characterise string concatenation, its absence of order, and a two-bit case split. No corpus object is modelled by them. If the import is unwelcome, §6's results survive on the quoted prohibition at :445-447 and the displayed table at :213-216 alone |
| AI-6 | "condition", "extends/refines", "generic", "forcing order" | **IMPORTED — FLAGGED, and used only NEGATIVELY.** | I invoke these solely to restate what the target found the enumeration LACKS. I never assert the corpus has them. **This is the axis this program has repeatedly imported without noticing; the target confined it to denials at its IA-6 and I have done the same. No corpus object is typed as a condition, an order, or a generic by me anywhere in this artifact** |
| AI-7 | "quotation hygiene", "elision", "proviso", "unmarked truncation" | **IMPORTED — MY VOCABULARY FOR THE DEFECT CLASS. FLAGGED.** | The corpus does not use these terms. They name a comparison anyone can run: the target's quoted string against the source span, both displayed in §5. Reject the names freely; the diffs stand |
| AI-8 | "counter-bytes" (§2.3) | **IMPORTED — MY COINAGE. FLAGGED, low weight.** | My name for bytes that cut against a conclusion I nonetheless confirm. The bytes named are :213/:214/:351-355, all quoted with cites |

```text
SELF-FLAGGED DEFECT COUNT: 5 imported axes (AI-4, AI-5, AI-6, AI-7, AI-8).
AI-6 IS THE ONE THAT MATTERS, and I have restricted every use of it to a statement about
ABSENCE, as the target did.
AI-2 IS THE ONE I ADDED. It is not an import — all three usages are the corpus's own — but
the SHIFT BETWEEN THEM is undeclared in the target, and declaring it here is the only
honest way to report correction X-6.
```

---

## §13 — FLAG BLOCK — STAGE8_CONSTRUCTION_ROUTES_O16SR_AUDIT_V001

```text
POSTURE:           DEFAULT-REFUTE. Testimony zero weight. Every consumed claim re-derived
                   at bytes before use. Where I confirm, I confirm from my own recomputation.
FENCES:            alpha_computed = false
                   proof_authorized = false
                   kappa_record_computed = false
                   -- unchanged from entry; no step in this artifact touched any of them.
VALUES:            NONE. No number appears as a program quantity. The integers here are
                   counts of labels, drafts, routes, tables, seals, and cited spans
                   (4, 3, 9, 21, 7, 28, 43, 10), byte offsets, line cites, and digests.
                   Declared as document combinatorics in §6's scope line.
MEASURED CONSTANT: NONE consulted, quoted, or compared.
CAS:               fresh venv created for this audit only; sympy 1.14.0; python 3.9.6;
                   four checks re-specified from the instrument and run blind; exact
                   symbolic; no floats. The target's script was not read or run.
GIT:               NOT USED.
SEALS:             10 verified by me, 10 OK, 0 FAILED, each `shasum -a 256 -c` run FROM THE
                   ARTIFACT'S OWN DIRECTORY. Eight in ROOT 1; the two instrument versions
                   verified again in ROOT 2 and confirmed byte-identical across roots.
                   9 whole-file digests and 3 byte-span digests independently recomputed.
SWEEP CUTOFF:      2026-08-15T15:40:39-0500. DECLARED.
FORBIDDEN READS:   No register, tracker, road, plan, or continuation file was opened.
                   "Q-..." treated as EXPECTED-UNLOCATABLE; not sought, not read.
DECLARED SWEEPS:   A-1 through A-7, §0.3. Scoped reads of named artifacts otherwise.
ENTRIES FILLED:    0. This artifact selects no route, fills no receiver, prices nothing,
                   adopts nothing, and proposes nothing.
GRADE:             CLAIMED. This is an audit, offered for registrar review. I do not verify
                   my own findings.
OPEN, HONESTLY:    F-1 (the (1,1) both-seeds cell) is unresolved; I confirm it and do not
                   close it. F-C (a possible third sealed source-sector seed) is UNTESTED
                   by me as it was by the target — outside both declared sweeps.
                   The A_C0 "entered carrier" tension (§2.3) is displayed, not dissolved.
```

```text
VERDICT = CONFIRMED-WITH-CORRECTIONS
  (1) enumeration displayed .......... CONFIRMED-WITH-CORRECTIONS  (X-1, X-7)
  (2) routes construct an OBJECT ..... CONFIRMED
  (3) exhaustiveness = CLAIMED ....... CONFIRMED  (+ my corroboration of F-1)
  (4) domain question = NO ........... CONFIRMED-WITH-CORRECTIONS  (X-2, X-3, X-4, X-6)
  (5) price = disclosure ............. CONFIRMED
  CAS battery ........................ CONFIRMED  (X-5, wording)
  FENCE-SCAN ......................... CLEAN
HARDEST HUNT (disguised DOMAIN-CANDIDATE over objects-within-a-record): NOTHING FOUND.
RECURRING DEFECT (hedge elided from inside a quoted sentence): FOUND ONCE, X-3, MATERIAL,
  AND IT DOES NOT MOVE THE FINDING.
```

END OF ARTIFACT.
