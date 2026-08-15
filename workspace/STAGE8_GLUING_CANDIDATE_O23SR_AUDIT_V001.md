# STAGE8 — GLUING-AUDIT OF STAGE8_GLUING_CANDIDATE_O23SR_V001

**COMMISSION O23SR — GLUING-AUDIT — 2026-08-15 — DEFAULT-REFUTE**

**DETERMINATION ONLY. THIS ARTIFACT DISPLAYS AND TYPES. IT ADOPTS NOTHING,
RECOMMENDS NO ADOPTION, AND ARGUES FOR NONE.**

```text
alpha_computed          = false
proof_authorized        = false
kappa_record_computed   = false
```

No value originates here. No measured constant appears. No comparison to any
measured quantity is made. No git operation was performed. Numerals below are
either QUOTED from a sealed source or are COUNTS OF ENUMERATED ITEMS, and each
is marked as one or the other where it could matter.

TESTIMONY GIVEN ZERO WEIGHT. Every claim of the build was re-derived at bytes
from the sources themselves, not from the build's report of them.

---

## 0. VERDICT

```text
OVERALL                                   CONFIRMED-WITH-CORRECTIONS

PER DELIVERABLE
  D1  POLARITY OF THE CLAUSE              CONFIRMED
  D2  SIGNATURE OF THE OBJECT             CONFIRMED
  D3  THE TWO-CELL COUNT                  CONFIRMED-WITH-CORRECTIONS   (C3)
  D4  STATUS AND THE ADOPTION GATE        CONFIRMED-WITH-CORRECTIONS   (C4, C7)
  D5  DISTANCE TO THE CONSTRUCTOR         CONFIRMED
  D6  NEIGHBOURHOOD — ALL EIGHT ROWS      CONFIRMED-WITH-CORRECTIONS   (C1, C6)

NO CORRECTION REVERSES A VERDICT OF THE BUILD. The corrections are: one
unmarked elision from inside a quoted block, a repeated undeclared
capitalisation inside spans labelled verbatim, one over-reaching headline on
the count question, two constructed clauses in the adoption gate, one
overbroad declaration in the build's own preamble, and passed-over content in
two rows the build claims to have fully typed.
```

---

## 1. STEP 0 — TARGET SEAL

```text
PROBE     STAGE8_GLUING_CANDIDATE_O23SR_V001.md            PRESENT  49920 bytes
          STAGE8_GLUING_CANDIDATE_O23SR_V001.md.seal.sha256 PRESENT   104 bytes
VERIFY    shasum -a 256 -c, run FROM THE ARTIFACT'S OWN DIRECTORY
          STAGE8_GLUING_CANDIDATE_O23SR_V001.md: OK
SEALED    7ab6e3ffd56ef67a22d31223cd844181fc80a3dc4260278b0eaf13d4ed2d69e8

OUTPUT PATH PROBED ABSENT BEFORE ANY WRITE:
          STAGE8_GLUING_CANDIDATE_O23SR_AUDIT_V001.md       ABSENT
          STAGE8_GLUING_CANDIDATE_O23SR_AUDIT_V001.md.seal.sha256  ABSENT
```

---

## 2. EVERY CONSUMED SEAL, RE-VERIFIED BY THIS AUDIT

All runs executed FROM THE ARTIFACT'S OWN DIRECTORY.

```text
STAGE8_INGREDIENT_CENSUS_O17SR_V001.md                              OK
STAGE8_INGREDIENT_CENSUS_O17SR_AUDIT_V001.md                        OK
STAGE8_GLUED_TOPOLOGY_HUNT_V001.md                                  OK   <- SOURCE
STAGE8_TASK4A_..._CODEX_LANE2_V001.md                               OK   <- NET
STAGE8_TASK4A_..._CODEX_LANE2_V002.md                               OK
STAGE8_TASK4A_..._CODEX_LANE2_V003.md                               OK
STAGE8_TASK4A_..._CODEX_LANE2_V004.md                               OK

LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md          NO SIDECAR — CANNOT BE VERIFIED
```

**F-2 OF THE BUILD IS CONFIRMED AT BYTES, AND IS THE BUILD'S OWN DISCLOSURE.**
No `.seal.sha256` exists for that file in either declared root. Both copies
hash to `b96bef557c150015cf9c0c523f63f4eb53ffe45051b01db9d8b86fe109805645`
(workspace and cleanroom, independently computed by this audit). Cross-root
agreement is corroboration, not verification. The build typed it that way and
did not overstate it.

**CL-1 CONFIRMED INDEPENDENTLY.** Exactly four proposal versions exist. The
hunt's import line :56 pins NET by full hash and reads, at bytes:

```text
87f696261651567e04242abc1a54d5a2b457a19e07926e9e9856b02dc1719eb1
  STAGE8_TASK4A_NETWORK_SOURCING_LAW_ADOPTION_PROPOSAL_CODEX_LANE2_V001.md
  SIDECAR (NET: two-node proposal)
```

`shasum -a 256` over the four returns `87f69626` for V001 only; V002 `9b2e42f8`,
V003 `51724fae`, V004 `69f4d93b`. NET = V001. The build's hash-not-name
resolution is sound and is the correct choice against four same-stem files.

**BYTE SPANS RE-READ AT OFFSETS BY THIS AUDIT.**

```text
NET [80,162)      exactly "**PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL
                  RATIFICATION (DoR-016/017 RESERVED)**"          EXACT
NET [18095,18214) "For the two-node matched network, the adjacency is /
                  ```text / Adj_2=[[0,1],[1,0]].   (NS-14)"       EXACT
                  (build normalised interior whitespace before "(NS-14)";
                  no word added, dropped, or altered)
```

---

## 3. (A) POLARITY READ WISHFULLY — TESTED HARDEST, NOT SUSTAINED

The commission's standard: kill a CAPABILITY reading resting on the clause
alone or on the absence of an explicit dismissal; equally kill a CONCESSION
reading asserted from the phrase "even if" without surrounding support. The
deliverable must rest on CONTEXT, NOT ON GRAMMAR.

### 3.1 The source span, re-read at bytes by this audit

`STAGE8_GLUED_TOPOLOGY_HUNT_V001.md` :262-267, seal OK, read directly:

```text
G-9  THE NETWORK SOURCING PROPOSAL (NET 87f69626, spans 9c6c594b/6a74a4fa).  CONN.
     Status of record: PROPOSED_NOT_ADOPTED (DoR-016/017 RESERVED) — the artifact
     is sealed; the LAW is not adopted.  Its combinatorial content: a TWO-NODE
     network, Adj_2 = [[0,1],[1,0]], "no self-edge", reciprocal, one-tier delayed.
     As a graph: 2 vertices, one reciprocal edge pair = a tree; H^1 = 1 - 2 + 1
     = 0.  Even if adopted, it glues two cells into a contractible object.
```

REPRODUCES EXACTLY, including the source's lowercase in the final clause. The
build's §2.1 statement that the clause does not end at "two cells" is a byte
fact, not an inference.

### 3.2 Does the concession reading rest on grammar? — NO. It rests on two
### surrounding contexts, both verified independently at bytes.

```text
SUPPORT 1 — THE IMMEDIATELY PRECEDING SENTENCE, SAME ROW, hunt :266.
  "As a graph: 2 vertices, one reciprocal edge pair = a tree; H^1 = 1 - 2 + 1 = 0."
  The source reaches H^1 = 0 BEFORE writing "Even if adopted." The concessive
  follows a stated topological result. This is context, not grammar, and it
  settles the force without appeal to the words "even if."

SUPPORT 2 — THE SWEEP'S OWN STATED QUARRY, hunt :274-281, re-read at bytes.
  "a sealed multi-cell glued record complex EXISTS — two of them, K_square and
   K_L, both inside V011, both loop-carrying — but both are sealed at the
   AUDIT/PREDICTION stratum. At the PHYSICAL write-carrier stratum ... NO glued
   multi-cell complex exists: composition is disjoint-only (G-1/G-2), the
   finite-N law is a tensor row (G-3), the ports are unanchored (G-4), the
   connected case is an open obligation with no built instance (G-5), and
   C_ref is an unrealized class declaration (G-8)."
  REPRODUCES EXACTLY. The criterion the sweep is organised around is
  LOOP-CARRYING. G-9's yield is H^1 = 0. It fails the sweep's own criterion.
```

**THE CONCESSION READING SURVIVES DEFAULT-REFUTE.** It is grounded in the
sentence before the clause and in the artifact's own statement of what it is
hunting. It does not lean on "even if."

### 3.3 Does the capability half rest on the clause alone, or on absence of
### dismissal? — NO. It rests on the source's own indicative.

The build affirms the joining predicate from `"it glues two cells"` — an
unhedged indicative assertion in the source's own voice. That is an affirmative
statement, not an argument from silence, and not the absence of a dismissal.
The build does not claim the source endorses the object; it claims the source
STATES that the object joins, while dismissing what the join yields.

**THE FORCE/PREDICATE SPLIT IS NOT A HEDGE.** This audit tested whether CL-4
("split polarity into force vs predicate") is a way of having both readings.
It is not. The two are attached to different constituents of one compound
sentence, each constituent quoted, and the build assigns the DISMISSAL wholly
to the result complement and the ASSERTION wholly to the main verb. Nothing is
left undecided: the sentence's force is concession, full stop.

### 3.4 One test the build did not run, run here, and it does not disturb D1

Could the source be dismissing the CAPABILITY as well? The hunt's sweep answer
states that at the physical stratum NO glued multi-cell complex EXISTS. Two
cells is multi-cell. If G-9 were being counted as an existing physical-stratum
glued complex, the two statements would collide. They do not collide, because
G-9 is a PROPOSED_NOT_ADOPTED rule and not a sealed complex, and because the
hunt does not list G-9 in that enumeration at all (see C8). No byte in the span
denies that the object joins.

**D1 VERDICT: CONFIRMED.** Polarity is CONCESSION; the surrendered term is
SUFFICIENCY; the joining predicate is asserted by the source. Contextually
grounded, not grammatically asserted.

---

## 4. (B) SIGNATURE WISHFUL — TESTED, NOT SUSTAINED

The hunt: an object typed as TAKING CELLS and YIELDING A JOINED STRUCTURE where
its own definition shows otherwise. The tension is real and this audit found it
before checking whether the build had: **the census's own B-8 row says
"TAKES two nodes," not "two cells."**

Census `STAGE8_INGREDIENT_CENSUS_O17SR_V001.md` :249-255, re-read at bytes:

```text
B-8  THE TWO-NODE NETWORK SOURCING PROPOSAL (NET 87f69626).
     TAKES   two nodes.
     YIELDS  Adj_2 = [[0,1],[1,0]], "no self-edge", reciprocal, one-tier delayed.
```

**THE BUILD DOES NOT HIDE THIS.** §3.1 quotes the census's weaker wording in
its own words — `Census B-8 TAKES row: "two nodes."` — and then grounds the cell
identification on two independent byte citations, both re-verified here:

```text
NET V001 :242, row `N`, EXACT:
  "On matched carriers, use the reciprocal two-node swap, no self-edge,
   identity cell matching, and one-tier delay."
  The rule's own content names CELL MATCHING across the edge. Its void
  condition, same row, EXACT: "a cell matching is silently selected outside
  the matched-carrier class."

NET V001 :332-340, §4.2 Edge transport, EXACT:
  "For a matched-carrier edge `a->b`, let / tau_(ba):ell^1_a -> ell^1_b /
   be the declared identity label match."

HUNT G-9, EXACT: "it glues two cells."
```

So the cell-typing is carried by NET's own rule text and by the source's own
indicative, not by the build. The build's move from the census's `Adj_2` to a
glued pair is not its own identification either — the hunt itself performs it
inside G-9, going from `Adj_2 = [[0,1],[1,0]]` to "2 vertices, one reciprocal
edge pair = a tree" to "it glues two cells." The build reports a chain the
source already walks.

ONE SOFT POINT, NOT A DEFECT: §3.2's sentence "An adjacency matrix and a glued
pair of cells are the same object under two descriptions" is stated as a general
proposition in the build's own voice rather than attributed. It is supportable
from G-9's own progression, and nothing turns on it.

**D2 VERDICT: CONFIRMED.**

---

## 5. (C) THE TWO-CELL COUNT — CORRECTION C3

The hunt: determine independently whether "two" is a property of the OBJECT or
of the EXAMPLE it was displayed on; the build may have taken an illustrative
instance for a bound, **or the reverse**. This audit finds THE REVERSE.

### 5.1 What the build claims

§3.3 headline: **"OF THE DISPLAY — and the source declares this in its own
voice."** It then carries three qualifiers (a) the general form is subjunctive,
(b) the selector is expressly not made, (c) "larger graph" is a live
alternative — and a TYPING CONSEQUENCE stating both halves.

### 5.2 What the bytes show — the discriminator the build passed over

`STAGE8_TASK4A_..._CODEX_LANE2_V002.md` :208, the `N` row of the V002 choice
table, re-read at bytes, EXACT and in the source's own lowercase:

```text
| `N` shared | Reciprocal matched two-node delivery after authored delay `d>=1`;
  examples use `d=1` | any positive integer delay; larger graph; self-edge |
  temporal incidence only | retroaction, E_post reversal, hidden edge/member
  selection |
```

**THE SOURCE ITSELF MARKS WHAT IS ILLUSTRATIVE, AND IT IS NOT THE NODE COUNT.**
Within one row the source writes "examples use `d=1`" for the DELAY, flagging
that parameter as exemplary. It applies no such flag to the node count:
"Reciprocal matched **two-node** delivery" sits in the PROPOSED CONTENT column,
while "larger graph" sits in the LIVE ALTERNATIVES column — the column of things
NOT taken. A live alternative is by construction something the proposal could
have selected and did not.

```text
CORRECTED TYPING OF THE COUNT
  "two" is THE CONTENT OF A SELECTION MADE — a property of the rule as
  proposed, sitting in the proposed-content column of the source's own choice
  table, beside a parameter the source does mark as merely exemplary.
  A LARGER GRAPH IS AN UNSELECTED, UNFORECLOSED LIVE ALTERNATIVE.
  The general form NS-8 is subjunctive ("would require") and its intertwiners
  are expressly unselected (V001 :347-348).
```

### 5.3 The scope of the correction

`V001 :347-348`, EXACT: "V001 instantiates only the matched two-node class, so
no permutation or intertwiner is selected." The build reads "instantiates only"
as evidence that two is a display bound. That reading is available, but the word
"instantiates" describes what the proposal DOES, and the choice table shows the
two-node class is what it PROPOSES, not what it happens to illustrate.

`V001 :892-893`, EXACT: "This does not make the commissioned maps schematic:
every member of the matched two-node class is instantiated. It limits what the
tower proves." The build quotes from "every member" onward, dropping the leading
clause. The dropped clause does not reverse the sense — but see C2/C1 on the
build's handling of quoted spans generally.

**C3 IS A HEADLINE AND WEIGHTING DEFECT, NOT A REVERSAL.** The build's own (a),
(b), (c) and its TYPING CONSEQUENCE ("Display-limited, and the display is all
there is") land close to the corrected typing. Only the headline "OF THE
DISPLAY" overshoots, and §12's "A LIMITATION OF THE DISPLAY, self-declared"
repeats the overshoot. Both should read: a selected scope, with a larger graph
unselected and unforeclosed.

**D3 VERDICT: CONFIRMED-WITH-CORRECTIONS.**

---

## 6. (D) ADOPTION-GATE INVENTED — PARTLY. CORRECTION C4

The gate must be QUOTED from the corpus, not constructed. Taking §4.2 clause by
clause and demanding a quoted source for each.

### 6.1 What is quoted and verified

```text
CLAUSE                              STATUS AT BYTES
"PENDING PRINCIPAL RATIFICATION"    QUOTED. NET V001 byte span [80,162), and
                                    line :3 of all four versions, EXACT.
"(DoR-016/017 RESERVED)"            QUOTED. Same span, EXACT.
"the artifact is sealed; the LAW    QUOTED. Hunt G-9 :263-264, EXACT.
 is not adopted"
NOT A CHECK — passes and stays      QUOTED, TWO SOURCES, BOTH EXACT:
 unadopted                            V002 :142 "**PROPOSED_NOT_ADOPTED —
                                      PASS_WITHIN_PROPOSAL ONLY**"
                                      V001 :757 row B6 reciprocity,
                                      "**PASS_WITHIN_PROPOSAL** on the matched
                                      two-node swap"
                                    (V003 :166 carries the same heading; the
                                    build cited it and it reproduces.)
STATUS STABLE ACROSS THE FAMILY     VERIFIED INDEPENDENTLY. :3 identical in all
                                    four; :12 carries
                                    NETWORK_SOURCING_LAW_V00n =
                                    PROPOSED_NOT_ADOPTED in V002/V003/V004;
                                    V004 :176 "BRANCH_A_MEMBER_RULE_RATIFIED =
                                    false | TYPE-S", EXACT.
```

**THE SUBSTANCE OF THE GATE IS QUOTED AND STANDS.** The adopting act is a
principal ratification; the doors are named DoR-016/017 and marked RESERVED;
the status does not move on internal passes. None of that is constructed.

### 6.2 C4 — TWO CLAUSES IN §4.2 ARE CONSTRUCTED, NOT QUOTED

```text
(i)  "It is NOT a derivation: nothing in the corpus derives adoption, and no
      proof discharges it."
      A UNIVERSAL NEGATIVE OVER THE CORPUS. No sentence of any source is quoted
      for it, and none of the build's three declared sweeps (§7: NET version
      family; §1.B eight rows; NET identity) covers the question. An unswept
      universal negative is exactly the shape of assertion this line of
      commissions exists to catch.
      WHAT THE BYTES DO SUPPORT: that the status is PROPOSED_NOT_ADOPTED across
      four versions while internal checks read PASS_WITHIN_PROPOSAL. That
      supports "passing checks does not move the status." It does not support
      "nothing in the corpus derives adoption."

(ii) "The doors are named, numbered, and held open; nothing has passed through
      them."
      "named" and "numbered" are quoted (DoR-016/017). "HELD OPEN" and "NOTHING
      HAS PASSED THROUGH THEM" are glosses on the single word RESERVED, and they
      are asserted by a build that expressly did not read the on-point document
      — its own CL-6 and F-4 record that the DoR-016 ratification document
      exists in supervision/ and was left unopened as out-of-root.
      THE SCOPE EXCLUSION ITSELF IS LAWFUL AND CORRECTLY DECLARED. Asserting the
      door's state while declining to read the document that would show it is
      the defect, not the exclusion.

CORRECTION: strike (i) and the "held open / nothing has passed through" half of
(ii), or re-type both as INFERENCE FROM THE STATUS LINE rather than as the
gate's content. The gate as quoted — principal ratification, DoR-016/017
RESERVED, unmoved by internal passes — needs neither.
```

### 6.3 C7 — SELECTIVE QUOTATION OF THE DOOR LEDGER (NOTE)

§4.3 GROUND 1 quotes two doors from V001's ledger:

```text
:921  DOOR_PORT_TO_HISTORY_UPDATE = NOT_OPENED | TYPE-U      EXACT
:922  DOOR_JOINT_SCALAR_NETWORK = NOT_OPENED | TYPE-U        EXACT
```

The same block, immediately above, carries lines the build does not mention:

```text
:918  DOOR_R_EMISSION = PROPOSED_OPENING
:919  DOOR_RECIPROCAL_NETWORK = PROPOSED_OPENING
:920  DOOR_NEXT_TIER = FILLED_WITH_ONE_TIER_DELAY
```

The two quoted lines are exact and the unquoted lines do not reverse GROUND 1 —
a PROPOSED_OPENING is not an opening, and is consistent with
PROPOSED_NOT_ADOPTED. **GROUND 1 STANDS.** The selection is undeclared, and the
build cites the range ":920-928" while quoting only from :921-922, which invites
the reader to assume the range is homogeneous. Recorded as a NOTE.

### 6.4 The other two grounds, checked

```text
GROUND 2  V001 :899, EXACT: "**PROPOSED_NOT_ADOPTED — ACCOUNTING DOES NOT
          RATIFY THE PACKAGE**".  CONFIRMED.
GROUND 3  V002 :210, EXACT: "This is a two-member proposal family, not one
          indivisible physics selection."  CONFIRMED.
          V004 :176, EXACT.  CONFIRMED.
          The V002 §3 HEADING is quoted with altered case — see C2.
EVIDENCE OF REPEATED CONSIDERATION  All four review filenames exist in the
          workspace, verified by listing. The build states it used names only
          and read no content; nothing in its text depends on their contents.
          CONFIRMED AS TYPED.
```

**D4 VERDICT: CONFIRMED-WITH-CORRECTIONS** (C4 material, C7 note).
