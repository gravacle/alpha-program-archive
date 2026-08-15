# STAGE8 — JOIN ADMISSIBILITY: DOES THE JOINER DELIVER INTO THE EMPTY SECTOR?

COMMISSION O28SR · 2026-08-15 · DETERMINATION ONLY · DISPLAY, NOT CONSTRUCTION

---

## 0. THE HEADLINE, BEFORE ANYTHING ELSE

**GATE 1 FAILS. The chain stops there.**

The two invariants are **the same FUNCTION, computed with the same convention, on
objects ONE LEVEL APART in the corpus's own hierarchy.**

```text
b_1(C_j)        — the admissible-set family's index.
                  Vertices counted = THE 0-CELLS INSIDE ONE CELL.
                  K_square, a cell, is counted as FOUR vertices.

H^1 = 1-2+1 = 0 — the joiner's dismissal invariant.
                  Vertices counted = THE CELLS THEMSELVES.
                  Each glued cell is counted as ONE vertex.
```

Both are `E - V + components` over the rationals. Neither is misapplied in its own
source. But the joiner's "2 vertices" **are the two cells** — the source's own final
clause says so: "it glues two cells." A cell that carries `b_1 = 1` in the family's
index contributes a **loop-free point** to the joiner's count. The two numbers are
therefore not commensurable as the question posed requires, and the inference
"H^1 = 0, therefore b_1 = 0, therefore admissible set empty" **cannot be taken.**

The consequence the commission asked me to test **is not displayed by these bytes,
and I do not assert it.** Neither do I assert its negation. See §5.

Gate 2 fails independently, on a different ground, and I display that too — as a
separate determination, not as a continuation of the stopped chain (§4).

---

## 1. SWEEP DECLARATION AND CUTOFF

```text
SWEEP CUTOFF          2026-08-15, all reads completed before this artifact sealed.
CORPUS ROOTS          /Users/bgm/MB Work/alpha-program-archive/workspace  (primary)
                      /Users/bgm/Documents/New project/gravity_emergence_evidence_
                        program/alpha_fundamental_record_action_cleanroom_v003
READS                 SCOPED. Named sections read in full; citations followed to
                      the two PRIMARY sources named by the sealed determinations.
BARRED AND NOT READ   register / tracker / road / plan / continuation files.
                      No such file was opened at any point.
"Q-..." ITEMS         EXPECTED-UNLOCATABLE. None was sought, none consumed.
GIT                   No git action of any kind.
```

**DECLARED SCOPED SWEEPS.** Four, all lawful, all within the named roots:

```text
L1  grep for section headers in the four named sealed artifacts, to locate the
    named sections before reading them in full.
L2  grep for "H^1 | contractible | 1 - 2 + 1 | b_1" across the joiner artifact and
    its audit, to find every site where the vanishing invariant is stated.
L3  grep for "admitted cell | R-CLW | cell-local | domain" across the typing-rule
    PRIMARY source, to locate the rule's own statement and its operative domain.
L4  grep for "node | vertices | vertex" across the topology-hunt PRIMARY source,
    to establish AT BYTES what the joiner's H^1 counts as a vertex. This leg is
    the one that decides the commission.
```

---

## 2. SEALS VERIFIED

Every seal below verified with `shasum -a 256 -c <file>.seal.sha256` executed
**from the artifact's own directory**, `/Users/bgm/MB Work/alpha-program-archive/workspace/`.

```text
COMMISSIONED GROUND
  STAGE8_INDEX_VARYING_SETS_O20SR_V001.md                  OK
  STAGE8_INDEX_VARYING_SETS_O20SR_AUDIT_V001.md            OK
  STAGE8_GLUING_CANDIDATE_O23SR_V001.md                    OK
  STAGE8_GLUING_CANDIDATE_O23SR_AUDIT_V001.md              OK
  STAGE8_INGREDIENT_CENSUS_O17SR_V001.md                   OK
  STAGE8_INGREDIENT_CENSUS_O17SR_AUDIT_V001.md             OK

PRIMARY SOURCES, reached by following the sealed determinations' own citations
  STAGE8_TYPING_RULE_CANDIDATE_V001.md                     OK   <- the selector
  STAGE8_GLUED_TOPOLOGY_HUNT_V001.md                       OK   <- the joiner row
```

**WHY THE PRIMARIES WERE READ.** Both sealed determinations declare that their own
cited spans are compressions pointing at operative sentences elsewhere — O20SR §3.1
("D2 IS NOT THE OPERATIVE SENTENCE — IT POINTS AT ONE"), O23SR §1 (chain of
location to hunt `:262-267`). The commission directs me to follow citations to the
two primary sources. I took the determination from the operative sentences, never
from a summary, a name, or a title.

---

## 3. GATE ONE — ARE THE TWO INVARIANTS THE SAME?

### 3.1 What the family's index actually is, verbatim

`STAGE8_TYPING_RULE_CANDIDATE_V001.md` `:152-161`, the operative sentences —
**not** D2's forward-referencing summary, per O20SR §3.1's own instruction:

> ```
>   LEMMA 1 (exact).  For a 1-chain ell with support(ell) ⊆ C_j^(1), bdry_K(ell) =
>     bdry_{C_j}(ell) (the boundary of an edge of C_j lands on vertices of C_j with
>     the same coefficients).  Hence the conserved cell-local set of cell C_j is
>     exactly the cycle space  Z_1(C_j; Q) = ker(bdry)|_{C_j},  of dimension
>     b_1(C_j) for connected C_j.
>   LEMMA 2 (exact).  If b_1(C_j) = 1 the admissible set is the circuit line
>     Q·gamma_j(C_j) \ {0}  (total-nonzero); if b_1(C_j) = 0 (tree) it is EMPTY —
>     no nonzero conserved cell-local write exists; if b_1(C_j) > 1 it is the
>     b_1(C_j)-dimensional cycle space minus zero, and R-CLW SELECTS NOTHING in it
>     (§8 N1).
> ```

```text
THE INDEX          b_1(C_j) = dim_Q ker(bdry)|_{C_j}.
THE ARGUMENT       C_j, "a connected admitted SUBCOMPLEX of K" (R-CLW, :135).
WHAT IS A VERTEX   A 0-CELL OF THE COMPLEX, INSIDE the cell.  Lemma 1 fixes this
                   in its own words: the boundary of an edge of C_j "lands on
                   VERTICES OF C_j".  The vertices belong to C_j; they are not C_j.
WHAT IS AN EDGE    A 1-CELL of C_j.  Clause (a): support(ell_j) ⊆ C_j^(1).
COEFFICIENTS       Q, stated explicitly in the symbol Z_1(C_j; Q).
SIDE               HOMOLOGY.  A cycle space, ker of a boundary map.
```

The corpus supplies a worked instance at this scale, and it is worth having in
view: `STAGE8_GLUED_TOPOLOGY_HUNT_V001.md` `:226` displays K_square as "vertices
v_00, v_10, v_01, v_11; edges e_a0: v00->v10, e_0b: v00->v01, ..." — **four
vertices for ONE cell** — and `:14` records that this carrier "has H^1 = 1".

### 3.2 What the joiner's vanishing invariant actually is, verbatim

`STAGE8_GLUED_TOPOLOGY_HUNT_V001.md` `:262-267`, row G-9, read at bytes:

> ```
> G-9  THE NETWORK SOURCING PROPOSAL (NET 87f69626, spans 9c6c594b/6a74a4fa).  CONN.
>      Status of record: PROPOSED_NOT_ADOPTED (DoR-016/017 RESERVED) — the artifact
>      is sealed; the LAW is not adopted.  Its combinatorial content: a TWO-NODE
>      network, Adj_2 = [[0,1],[1,0]], "no self-edge", reciprocal, one-tier delayed.
>      As a graph: 2 vertices, one reciprocal edge pair = a tree; H^1 = 1 - 2 + 1
>      = 0.  Even if adopted, it glues two cells into a contractible object.
> ```

And the same artifact's own tabulation of that row, `:316`:

> ```
> NET two-node      2      1      0      1         —         0      tree: E - V + components = 0
> ```

```text
THE INVARIANT      H^1, computed as E - V + components.
THE ARGUMENT       THE TWO-NODE NETWORK GRAPH.  The hunt's fence :468-470 names
                   its own basis for this row exactly: "every topology claim above
                   rests on a sealed COMBINATORIAL presentation (... the Adj_2
                   display)".  Adj_2 IS the network's adjacency.
WHAT IS A VERTEX   *** A CELL. ***  This is the finding.  See §3.3.
WHAT IS AN EDGE    An inter-cell coupling — "one reciprocal edge pair", "no
                   self-edge", between two NODES on matched carriers.
COEFFICIENTS       Not named in the row.  The hunt's fence :464-465 declares the
                   whole artifact's arithmetic "exact mod-p ranks with rational
                   sandwiches, Fraction-exact RREF.  No floats."  Rational.
SIDE               COHOMOLOGY.  H^1, not Z_1.
```

### 3.3 *** THE DECIDING FACT: THE JOINER'S VERTICES ARE THE CELLS ***

This is established at bytes, from **three** independent sites, and it is not an
inference of mine:

```text
SITE 1 — THE HUNT'S OWN FINAL CLAUSE, same row, same sentence family (:266-267):
         "it glues two CELLS into a contractible object."
         The object whose H^1 it just computed is the object made of two cells.
         The graph has 2 vertices.  The gluing has 2 cells.  Same two.

SITE 2 — O23SR §3.1, typing the signature at bytes:
         "INPUT SIDE  TWO NODES on matched carriers. ...
          The input items are CELLS under the source's own identification:
          the transport is declared cell-to-cell ... and the hunt names the
          yield's constituents 'two cells'."
         NODE = CELL, established by the sealed determination itself.

SITE 3 — O23SR §3.1, output side, the identification made explicit:
         "OUTPUT SIDE  TWO CELLS JOINED BY ONE RECIPROCAL EDGE PAIR.
          ... As a glued structure: 2 vertices, 1 reciprocal edge pair."
         The SAME LINE writes "two cells" and "2 vertices" of one object.
```

**THE CONTRAST, IN ONE FRAME.** Both counts are in the same artifact, four hundred
lines apart, and they count different things:

```text
                        WHAT IS A VERTEX        K_square's CONTRIBUTION
b_1(C_j), the index     a 0-cell of the cell    FOUR vertices  ->  b_1 = 1
H^1(NET), the joiner    an entire cell          ONE vertex     ->  b_1 = 0
```

### 3.4 EXACT SYMBOLIC CHECK (CAS, fresh venv, sympy 1.14.0, rationals only)

Both displays were re-derived from the sealed combinatorial data by exact rational
rank of the boundary map `d_1`, never by the stated formula. **This checks
arithmetic already displayed at bytes; it computes nothing new and constructs
nothing.**

```text
NET two-node network  (nodes = CELLS)
   V = 2   E = 1   components = 1
   rank(d_1) exact          = 1
   dim Z_1 = E - rank(d_1)  = 0
   E - V + components       = 0          AGREE = True

K_square  (vertices = 0-CELLS INSIDE ONE CELL)
   V = 4   E = 4   components = 1
   rank(d_1) exact          = 3
   dim Z_1 = E - rank(d_1)  = 1
   E - V + components       = 1          AGREE = True
```

Both sources' arithmetic is **correct in its own frame.** Neither source misapplies
the invariant. The mismatch is not an error in either; it is a mismatch between
them.

### 3.5 GATE ONE VERDICT

The commission's gate is a conjunction of three clauses. I take them one at a time
and I do not let a failure in one contaminate my reading of the others.

```text
CLAUSE                          VERDICT
(a) the same homological        *** SATISFIED. ***  Both are the cycle rank
    quantity?                   E - V + components of a finite graph over a field
                                of characteristic 0.  The nominal homology /
                                cohomology difference (Z_1 vs H^1) does NOT bite:
                                over a field the two have equal dimension for a
                                graph.  I record this so the failure is not
                                mislocated in a duality that is harmless here.

(b) computed on the same        *** NOT SATISFIED.  THIS IS THE FAILURE. ***
    KIND of object?             The index's argument is a CELL, counted by its own
                                0-cells.  The joiner's argument is a NETWORK OF
                                CELLS, counted with each cell as one point.  These
                                are objects one level apart in the corpus's own
                                hierarchy, and the corpus itself keeps the levels
                                apart: R-CLW :134 distinguishes the CARRIER K from
                                its ADMITTED CELLS {C_j}.  A network of cells is
                                an object of the K level; b_1(C_j) is an invariant
                                of the C_j level.

(c) with the same               *** SATISFIED, with one silence recorded. ***
    conventions?                Same formula, same characteristic-0 field.  The
                                joiner's row does not NAME its coefficient ring;
                                the hunt's fence supplies rational arithmetic for
                                the artifact.  I mark this a silence, not a
                                divergence — it does not affect the value.
```

```text
*** GATE ONE FAILS, ON CLAUSE (b). ***

AND THE FAILURE IS EXACTLY THE ONE THAT MATTERS.  It is not a technicality about
notation.  Collapsing a cell to a node DISCARDS THAT CELL'S b_1 — the CAS display
above shows K_square carrying b_1 = 1 as a cell and contributing b_1 = 0 as a
node of a network.  The very quantity the family is indexed by is the quantity the
joiner's count throws away.

SO THE TWO DO NOT "MERELY SHARE A NAME" — that would understate the relationship
and I decline to say it.  They share a NAME, a FORMULA, and a FIELD.  What they do
not share is an ARGUMENT.  They are two values of one function at two different
kinds of input, and no sealed text displayed to me identifies the inputs.

*** THE CHAIN STOPS HERE.  Deliverable three does not fire. ***
```

**WHAT WOULD HAVE BEEN NEEDED, NAMED EXACTLY.** For the chain to run, some sealed
text would have to display that the joiner's yield, *considered as a complex with
its cells' interiors present*, has `b_1 = 0`. The hunt displays no such thing. Its
row computes the network's `H^1`, and its own final clause tells us the network's
points are cells — that is, that the interiors were **not** counted.

---

## 4. GATE TWO — IS THE JOINED OBJECT IN THE FAMILY'S DOMAIN?

**STATUS OF THIS SECTION.** The chain stopped at §3.5. What follows is an
**INDEPENDENT determination**, not a continuation. I display it because the
commission's own verdict menu turns on it and because it fails on a ground
entirely different from gate 1's — so the two failures corroborate rather than
duplicate each other. **Nothing here revives the chain.**

### 4.1 What the family is defined ON, verbatim

`STAGE8_TYPING_RULE_CANDIDATE_V001.md`, the rule's own opening, `:134-136`:

> ```
> R-CLW.  Let K be a connected multi-cell record complex and let {C_j} be its
> ADMITTED CELLS, each a connected admitted subcomplex of K (admission is a separate,
> unsupplied act — §8 N2).
> ```

And §6, OPERATIVE DOMAIN, `:313-332`, in full:

> ```
> D1  CARRIERS: connected multi-cell record complexes K with a declared admitted-cell
>     family {C_j}, each C_j a connected admitted subcomplex.  On the one-cell
>     degenerate case (K itself a single admitted cell) R-CLW reduces to the sealed
>     containment law — no new content.
> D2  CELLS: the rule TYPES any connected admitted cell (Lemmas 1-2 give its
>     admissible set at every b_1); its non-vacuous single-line sector is b_1 = 1,
>     the entered shape.  At b_1 > 1 the rule types the SPACE and selects no class
>     (§8 N1).  At b_1 = 0 the admissible set is empty (K-2).
> D3  ADMISSION IS OUTSIDE THE RULE: which subcomplexes of K are admitted cells is
>     an unsupplied, separate act (§8 N2).  R-CLW is conditional on an admission it
>     does not perform.  In particular R-CLW does NOT extend the entered Attach
>     map's domain: the Attach entry stands at b_1 = 1 (S3) and this rule supplies
>     no cycle selector beyond it.
> D4  STRATUM: the rule binds the WRITE TYPING only.  It licenses no gluing
>     (O11/O12/O-D1 remain unbuilt acts; the min-carrier ledger L-1..L-5 statuses
>     are unchanged by this rule — f1881511 §7, ca7fa457 §4), promotes no candidate
>     carrier (K_dd, K_3 remain candidate/audit stratum; NONE_SEALED at the
>     physical write-carrier stratum stands), and decides nothing post-limit.
> ```

**THE ANSWER TO THE COMMISSION'S QUESTION, EXACTLY.** The family is defined **not**
on "cells only", **not** on "any object of that type", and **not** on something
wider. It is defined on:

```text
*** CONNECTED ADMITTED SUBCOMPLEXES OF A GIVEN CONNECTED MULTI-CELL
    RECORD COMPLEX K, WHERE ADMISSION IS AN ACT THE RULE DOES NOT PERFORM. ***
```

Two restrictions, and they are independent. The object must be **a subcomplex of a
carrier** (a level), and it must be **admitted** (an act).

### 4.2 Is the joiner's output such an object? — NO, ON BOTH RESTRICTIONS

```text
RESTRICTION 1 — LEVEL.  *** FAILS. ***
  The family's domain elements are C_j, the CONSTITUENTS of a carrier.
  The joiner's output is a structure WHOSE CONSTITUENTS ARE CELLS —
  "TWO CELLS JOINED BY ONE RECIPROCAL EDGE PAIR" (O23SR §3.1).
  It stands at the K level, not the C_j level.  It is a candidate CARRIER,
  and a carrier is what a cell sits INSIDE, not an instance of one.
  R-CLW's own first sentence keeps these apart: "Let K be a connected
  multi-cell record complex and let {C_j} be its ADMITTED CELLS."
  The joined object is on the K side of that "and".

RESTRICTION 2 — ADMISSION.  *** FAILS, AND FAILS FOR EVERYTHING. ***
  §8 N2, verbatim:
      "N2  NO CELL ADMISSION.  The rule admits no subcomplex as a cell;
       admission is unsealed of record and stays so (ca7fa457 §4 L-2:
       admission itself unsealed)."
  D3, verbatim: "R-CLW is conditional on an admission it does not perform."
  So the domain is not merely unpopulated BY THE JOINED OBJECT — the
  admitting act is unsealed of record, and the rule says it "stays so."
  No object enters this domain by anything the corpus displays.
```

**A THIRD BAR, STATED BY THE RULE ITSELF ABOUT EXACTLY THIS.** `§8 N3`:

> ```
> N3  NO GLUING LICENSE.  No O11/O12/O-D1 act is licensed; the anchoring law (*)
>     and its fork resolution (§9) license no cell-to-cell port chaining — under
>     this rule the ports are inert (S5 §2.3a) and chain nothing.
> ```

The rule that owns the admissible-set family **expressly disclaims any relation to
cell-to-cell joining.** It does not merely fail to cover the joined object; it says
in its own voice that it licenses no such act and that the joining ports "chain
nothing" under it. D4 repeats this: "It licenses no gluing."

### 4.3 GATE TWO VERDICT, AND WHAT GOVERNS THE JOINED OBJECT INSTEAD

```text
*** GATE TWO FAILS.  THE JOINED OBJECT FALLS OUTSIDE THE DOMAIN.
    THE QUESTION DOES NOT ARISE IN THE FORM POSED. ***
```

The commission directs me, on this outcome, to display what the joined object's
admissibility is governed by instead, **if anything**. At bytes, **three things
govern it, and the admissible-set family is none of them:**

```text
(1) PRINCIPAL RATIFICATION — the status gate.
    "PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL RATIFICATION (DoR-016/017
    RESERVED)", identical across all four sealed versions (O23SR §4.1).
    O23SR §4.2 establishes the gate is PRINCIPAL, not evidentiary: the
    proposal PASSES its own checks and remains unadopted —
    "PROPOSED_NOT_ADOPTED — PASS_WITHIN_PROPOSAL ONLY" (NET V002 :142).

(2) THE HUNT'S LOOP-CARRYING CRITERION — the substantive ground of dismissal.
    Hunt :372-377, the wanted object: "a glued record complex with H^1 > 0".
    G-9's yield is H^1 = 0 ON THE NETWORK OF CELLS.  O23SR §2.2:
    "The hunt's criterion of interest is loop-carrying (H^1 > 0). G-9's yield
    is H^1 = 0.  It is dismissed for failing the criterion the whole sweep is
    organised around, not for a shortfall in cell count."
    *** NOTE THE SCALE: this criterion is stated at the SAME level the hunt
    computes on — the glued complex / network — so unlike the admissible-set
    family it is commensurable with the displayed number.  THIS is the
    invariant that actually bites on the joined object. ***

(3) NOTHING ELSE.  Hunt :322-326 records what the sealed data does NOT
    determine, including: "(iv) any relation between K_square/K_L and the
    write-carrier complex — no sealed map sends either audit object onto the
    working class or vice versa."
```

```text
*** THE ADMISSIBLE-SET FAMILY DOES NOT GOVERN THE JOINED OBJECT AT ALL. ***
It governs writes on admitted cells.  The joined object is not an admitted cell,
the admitting act is unsealed, and the rule expressly licenses no gluing.
```

---

## 5. DELIVERABLE THREE — DOES NOT FIRE

The commission conditions deliverable three on **both** gates passing. Gate 1 fails
(§3.5) and gate 2 fails independently (§4.3). **I therefore do not display the
consequence, because the bytes do not display it.**

I state the negative precisely, because a stopped chain is easy to over-read in
either direction:

```text
NOT ESTABLISHED   That the joiner's output lands at the index value whose
                  admissible set is empty.  The two invariants are not
                  commensurable (gate 1) and the output is not in the family's
                  domain (gate 2).  No sealed text displayed to me draws this
                  inference, and I do not draw it.

ALSO NOT ESTABLISHED  That the joiner's output does NOT land there.  Gate failure
                  is not a refutation.  I have shown the question is not answered
                  by these bytes, NOT that its answer is no.  Anyone reading this
                  artifact as a clearance of the joiner is misreading it.

WHAT IS ESTABLISHED   Exactly two things, both at bytes:
                  (i)  The joiner's H^1 = 0 counts each glued cell as ONE point,
                       so it reports nothing about any cell's own b_1.
                  (ii) The joined object is outside the admissible-set family's
                       domain on two independent restrictions, and the rule that
                       owns that family expressly licenses no gluing.
```

**THE ONE THING BOTH SIDES DO SAY, PLACED SIDE BY SIDE AS THE COMMISSION ASKED —
and it is a NON-COINCIDENCE, not a match:**

> the family, `STAGE8_TYPING_RULE_CANDIDATE_V001.md` `:158`:
> ```
> if b_1(C_j) = 0 (tree) it is EMPTY — no nonzero conserved cell-local write exists
> ```

> the joiner, `STAGE8_GLUED_TOPOLOGY_HUNT_V001.md` `:265-266`:
> ```
> 2 vertices, one reciprocal edge pair = a tree; H^1 = 1 - 2 + 1 = 0
> ```

**BOTH SAY "TREE". THAT IS THE WHOLE OF THE APPARENT CONTACT, AND IT IS A CONTACT
BETWEEN TWO DIFFERENT OBJECTS.** The family's tree is *a cell with no circuit in
its own 1-skeleton*. The joiner's tree is *a network of two cells with no circuit
among the cells*. A network of two loop-carrying cells is a tree in the second
sense and says nothing whatever in the first. The word is shared; the referent is
not. This is precisely the coincidence the commission was right to test, and it
does not survive the test.

---

## 6. DELIVERABLE FOUR — THE STATUS QUALIFIER

The commission is right that the difference matters, and it matters here in an
unexpected way: **the qualifier separates cleanly, and the separation survives the
gate failures.** I take it in the form the bytes permit.

### 6.1 The consequence at issue does not exist, so nothing attaches to it

```text
The gates failed.  There is no consequence "the joiner delivers into the empty
sector" for a status qualifier to modify.  I do not manufacture one in order to
qualify it.
```

### 6.2 But the underlying separation IS displayed, and I display it

The corpus draws exactly this distinction, in its own voice, about this object.
There are **two** facts in the neighbourhood and they carry **different** status:

```text
FACT A — THE TOPOLOGICAL FACT ABOUT THE PROPOSAL AS WRITTEN.
  "2 vertices, one reciprocal edge pair = a tree; H^1 = 1 - 2 + 1 = 0."
  *** STRUCTURAL.  HOLDS WHETHER OR NOT THE RULE IS EVER ADOPTED. ***
  It is computed from Adj_2 — the proposal's sealed combinatorial content — and
  Adj_2 is fixed by the sealed bytes.  Ratification is a PRINCIPAL ACT (O23SR
  §4.2); it changes the LAW's force, not a matrix's cycle rank.
  THE SOURCE SAYS THIS ITSELF, and it is the whole work of its concessive:
      "Even if adopted, it glues two cells into a contractible object."
  O23SR §2.2 reads the grammar exactly: the concessive "grants the adoption gate
  ARGUENDO ... It neutralises adoption as the thing that would decide the matter."
  And O23SR §12: "ADOPTION CLOSES NONE OF THEM."

FACT B — THE EXISTENCE OF A JOINED OBJECT IN THE RECORD.
  *** HYPOTHETICAL.  REQUIRES ADOPTION, AND MORE THAN ADOPTION. ***
  Nothing joined stands in the record today.  Hunt :446 —
      "NOTHING SEALED EXISTS: a physical-stratum glued multi-cell record complex"
  The joiner is PROPOSED_NOT_ADOPTED across all four sealed versions.  So any
  sentence of the form "the joined object is/does X" is, today, a sentence about
  an object the record does not contain.
```

### 6.3 The exact statement, and it is narrower than the commission's frame allows

```text
*** WHAT IS STRUCTURAL:  a fact about A WRITTEN PROPOSAL'S OWN ARITHMETIC —
    that Adj_2 = [[0,1],[1,0]] has cycle rank zero as a two-node graph.
    This is true now, of a sealed document, and adoption is irrelevant to it.

*** WHAT IS HYPOTHETICAL:  every claim about what a joined object WOULD BE,
    because there is no joined object.

*** AND A THIRD THING, WHICH IS NEITHER:  the claim the commission set out to
    test — that joining forces the empty admissible set — is NOT structural and
    NOT hypothetical.  It is UNSUPPORTED: it fails at the invariants (§3) and at
    the domain (§4) before adoption is ever reached.  Adoption is not what stands
    between the corpus and that claim, and neither is non-adoption.  A reader who
    files this under "would follow if adopted" has mislocated it.
```

**WHY THIS MATTERS AND NOT MERELY AS A DISTINCTION.** If the consequence had held,
the status qualifier would have been the whole of its interest — a structural
consequence binds a future adopter, a hypothetical one does not. Because the
consequence does not hold, the qualifier's real service here is negative: it
prevents the H^1 = 0 display, which IS structural, from being read as carrying an
admissibility consequence it does not carry. **The structural half of the pair is
real; what it is structural ABOUT is narrower than it looks.**

---

## 7. DELIVERABLE FIVE — THE ESCAPE SURVEY

The commission asks whether anything sealed would let a joined object acquire a
nonzero index. **Silence is silence, not permission**, and I apply that strictly:
a row is marked ADMITS only where sealed text affirmatively supplies the move.

**SCOPE NOTE, STATED SO THE SURVEY IS NOT OVER-READ.** §3 established that the
joiner's H^1 and the family's b_1 are invariants of different arguments. So
"nonzero index" splits into two questions, and I keep them apart in every row:

```text
(N)  could the NETWORK of cells acquire a cycle?   — the joiner's own invariant
(C)  could a CELL acquire a nonzero b_1?           — the family's index
```

### 7.1 The five candidate escapes

```text
E-1  A REFINEMENT APPLIED AFTER JOINING
     SEALED OBJECT   T_ref, GEOMETRIC REFINEMENT STITCHING (census §3, quoting
                     STAGE8_DESC_STITCHING_RULE_HUNT_DARIO_V001.md :139-181).
     VERBATIM        "** NOT INSTANTIATED **, but fully typed as a work order:
                     a functor D_ref ... refinement pushforwards P_KR, response
                     maps Resp_K, two commuting-square identities, and
                     refinement-invariance of the INTENSIVE response up to a
                     boundary term whose ratio to four-volume vanishes —
                     ALL IN ONE FROZEN TOPOLOGY."
     VERDICT (N)     *** BARS. ***  Two independent bars.  (i) NOT INSTANTIATED.
                     (ii) Even as typed, the whole apparatus is declared to run
                     "ALL IN ONE FROZEN TOPOLOGY" — a refinement that holds the
                     topology fixed cannot move a Betti number.  This is the one
                     row where the corpus does not merely fail to help; it says
                     the opposite of what an escape would need.
     VERDICT (C)     *** BARS, same two grounds. ***
     ALSO            The census keeps the scope straight and so do I: this
                     absence "joins the finite to the completed carrier, NOT
                     CELL TO CELL."  It is not a post-joining refinement at all.

E-2  THE ONE CELL-YIELDING RULE, APPLIED AFTER JOINING
     SEALED OBJECT   CIS (census §2.1), the corpus's only rule with a cell on its
                     output side.
     VERBATIM        "TAKES (i) a primitive record-forming incidence c, and
                     (ii) 'the complete microscopic parent' — the assigning agent.
                      YIELDS a pair: one cell Omega_c, and one interaction
                      density L_c.   TYPE  RULE. A cell stands on its output side."
     VERDICT (N)     *** DOES NOT APPLY. ***  Its input is an INCIDENCE, not a
                     joined object.  It cannot be "applied after joining"; there
                     is no slot for a joined object on its input side.
     VERDICT (C)     *** BARS, at its own bytes. ***  Its second input is unpaired
                     at the root — census U-1: "YIELDED BY nothing in the census",
                     and at its own bytes
                         complete_causal_parent_derived = false
                     (CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md :110).
                     The one rule that makes cells cannot fire.

E-3  A DIFFERENT ATTACHMENT (self-edge, larger graph, general edge family)
     SEALED TEXT     NET V001 row N: "no self-edge" — EXCLUDED IN THE PROPOSAL.
                     NET V001 :340-345 (NS-8): on a general reciprocal edge
                       family the proposal "WOULD REQUIRE isometric intertwiners".
                     NET V001 :347: "V001 instantiates only the matched two-node
                       class, so NO PERMUTATION OR INTERTWINER IS SELECTED."
                     NET V002 §3 choice table, "Live alternatives" column, row N:
                       "any positive integer delay; LARGER GRAPH; self-edge."
     VERDICT (N)     *** SILENT — AND I RECORD IT AS SILENCE. ***
                     This is the row where the temptation is greatest, so I state
                     it exactly.  A self-edge or a larger graph WOULD be the way a
                     network acquires a cycle, and the corpus knows it: O23SR §12,
                     "a cycle needs both the rule's excluded self-edge and a scope
                     past two nodes."  But: the self-edge is EXCLUDED by the rule
                     as written; the general family is SUBJUNCTIVE ("would
                     require") and its required intertwiners are EXPRESSLY NOT
                     SELECTED; and "larger graph" sits in an UNSELECTED
                     live-alternatives column.  O23SR §3.3: "It is neither
                     foreclosed nor taken."
                     *** NEITHER FORECLOSED NOR TAKEN IS NOT AN ESCAPE.
                         NOTHING SEALED SUPPLIES THE MOVE. ***
     VERDICT (C)     *** DOES NOT BEAR. ***  Changing the network's edges changes
                     the network, not any cell's own 1-skeleton.

E-4  AN IDENTIFICATION OF FACES / PORTS
     SEALED TEXT     Hunt :446-448, verbatim:
                       "NOTHING SEALED EXISTS: a physical-stratum glued multi-cell
                        record complex; A PORT IDENTIFICATION RULE; A CONNECTED
                        COMPOSITION LAW; a CTP trace; a sealed contour; a C_ref
                        member."
                     R-CLW §8 N3, verbatim: "the anchoring law (*) and its fork
                       resolution license no cell-to-cell port chaining — under
                       this rule THE PORTS ARE INERT and chain nothing."
     VERDICT (N)     *** SPLIT, AND I SPLIT IT RATHER THAN ROUND IT. ***
                     UNDER R-CLW ITSELF: *** BARS. ***  N3 is affirmative — the
                     ports "are inert and chain nothing."  The rule that owns the
                     admissible-set family forbids the move outright.
                     IN THE WIDER CORPUS: *** SILENT-BY-ABSENCE. ***  The
                     identification rule is named as nonexistent, not as
                     forbidden.  Either way NOTHING SUPPLIES THE MOVE.
     VERDICT (C)     *** SAME SPLIT, same texts. ***
     ALSO            Census U-3: a connected composition of cells is "YIELDED BY
                     nothing in the census — this is exactly the empty category."
     THE COUNTER-    The hunt ALSO says the H^1 > 0 carrier "is NOT sealed at the
     TEXT, RAISED    physical stratum, is NOT forbidden, and has a NAMED
     AGAINST MYSELF  constructor (O11 + O12 + connected composition)" (:372-377),
                     and lists it under "CONSTRUCTIBLE, CONSTRUCTOR NAMED"
                     (:449-453).  A careful reader will press this, so I meet it.
                     IT DOES NOT MOVE THE ROW.  The same lines call the
                     constructor "the UNBUILT O11 successor incidence-sum law +
                     O12 port anchoring", and the hunt's own summary of the gap
                     is "a CONSTRUCTION gap, not a formalism gap."  A named
                     unbuilt constructor is the corpus stating precisely what it
                     does NOT have.  NAMING IS NOT SUPPLYING, and "not
                     forbidden" is the definition of silence, not of permission.

E-5  A PASSAGE TO ANOTHER STRATUM
     SEALED TEXT     Hunt :441-442: "FOUND, WITH H^1 > 0: K_square (H^1 = 1),
                       K_L (H^1 = 4) — sealed, exact, but AUDIT/PREDICTION
                       STRATUM ONLY."
                     Hunt :322-326, what the sealed data does NOT determine:
                       "(iv) any relation between K_square/K_L and the
                        write-carrier complex — NO SEALED MAP SENDS EITHER AUDIT
                        OBJECT ONTO THE WORKING CLASS OR VICE VERSA."
                     R-CLW §8 N4: "NO CARRIER PROMOTION.  K_dd and K_3 remain
                       candidate/audit-stratum objects; NONE_SEALED at the
                       physical write-carrier stratum survives this candidate
                       untouched."
     VERDICT (N)     *** BARS — and this is the sharpest bar in the survey. ***
                     Loop-carrying objects DO exist in the corpus.  They are at
                     the wrong stratum, and the transporting map is named as
                     absent in the same breath.  The escape is not silent; it is
                     affirmatively blocked by a named missing map.
     VERDICT (C)     *** BARS, same text, plus N4's explicit no-promotion clause.
```

### 7.2 Escape survey verdict

```text
ADMITS      *** NONE. ***  No row.  Nothing sealed supplies a move that would
            give a joined object a nonzero index at either scale.
BARS        E-1 (frozen topology + not instantiated), E-2 (input underived),
            E-5 (no sealed map between strata + no carrier promotion),
            and E-4 UNDER R-CLW ITSELF (N3: ports inert, chain nothing).
SILENT      E-3, and E-4's wider-corpus half.
            E-3: the self-edge and the larger graph are the moves that would
            work, and the corpus neither supplies them nor forecloses them.
            E-4 (wider): the identification rule is named NONEXISTENT and the
            H^1 > 0 carrier is called "NOT forbidden" with a constructor named
            but UNBUILT — absence, not prohibition, and equally not provision.
            *** I RECORD THIS AS SILENCE AND DRAW NOTHING FROM IT. ***
            An unselected column is not a permission, and I do not treat the
            corpus's awareness of a move as its provision of one.

*** THEREFORE: NO ESCAPE IS DISPLAYED.  The verdict ESCAPE-EXISTS IS NOT
    RETURNED — not because the consequence stands unrelieved, but because the
    consequence never stood (§5).  A survey finding no escape from a consequence
    that does not hold relieves nothing and establishes nothing further. ***
```

---

## 8. CHOICE LEDGER

```text
C-1  READ THE PRIMARY SOURCES, NOT THE SEALED DETERMINATIONS' REQUOTES.
     TAKEN.  Both determinations declare their own cited spans compressions
     (O20SR §3.1; O23SR §1).  The commission directed following citations.
     LIVE ALTERNATIVE  Rest on O20SR/O23SR alone.
     CONSEQUENCE OF THE ALTERNATIVE  The decisive fact — that the joiner's
     "2 vertices" are the two cells — is legible only by putting hunt :226
     (K_square, four vertices for ONE cell) beside hunt :265 (2 vertices for
     TWO cells).  Sweep leg L4 found it.  The alternative misses the commission.

C-2  LOCATED GATE 1's FAILURE IN CLAUSE (b), NOT IN "MERELY SHARE A NAME".
     TAKEN.  The two ARE the same function, over the same field, by the same
     formula.  Only the argument differs.
     LIVE ALTERNATIVE  Return "they merely share a name."
     WHY DECLINED  It is false at bytes and would overstate the finding.  The
     relationship is closer than name-sharing and that closeness is exactly what
     makes the trap worth marking.

C-3  DISPLAYED GATE 2 THOUGH THE CHAIN HAD STOPPED.
     TAKEN, and marked throughout as an INDEPENDENT determination (§4 preamble).
     LIVE ALTERNATIVE  Stop dead at §3.5.
     WHY DECLINED  The commission's verdict menu turns on gate 2, and its failure
     ground (level + admission + N3's express disclaimer) is disjoint from gate
     1's.  Two independent failures are worth more to the record than one.
     GUARD  Nothing in §4 is used to support §3, or the reverse.

C-4  DECLINED TO COMPUTE b_1 OF A GLUED COMPLEX WITH CELL INTERIORS PRESENT.
     DECLINED — and this was the sharpest temptation in the commission.
     Such a number would answer the question the gates blocked.  But no sealed
     text displays that object: the hunt displays Adj_2 and nothing beneath it,
     and NET displays no cell interiors at all.  Computing it would CONSTRUCT a
     complex the corpus does not carry.  DETERMINATION ONLY was the fence and I
     kept it.  I display the scale mismatch; I do not resolve it.

C-5  TREATED E-3 (self-edge / larger graph) AS SILENCE.
     TAKEN.  "Neither foreclosed nor taken" is not permission.
     LIVE ALTERNATIVE  Return ESCAPE-EXISTS on the strength of the corpus naming
     the moves that would produce a cycle.
     WHY DECLINED  The commission's own instruction is explicit: silence is
     silence.  The self-edge is EXCLUDED by the rule as written; the intertwiners
     a general family needs are EXPRESSLY NOT SELECTED.

C-6  DID NOT ASSERT THE NEGATION OF THE CONSEQUENCE.
     TAKEN.  §5 states both non-establishments symmetrically.  A failed gate
     shows a question unanswered by these bytes, not answered in the negative.

C-7  USED K_square AS THE WORKED CONTRAST INSTANCE.
     TAKEN.  It is displayed at bytes in the SAME artifact as the joiner row
     (hunt :14, :226), so the contrast is internal to one source and needs no
     import.  LIVE ALTERNATIVE  An abstract cell.  Declined: less probative.
```

---

## 9. TOY_SEPARATION

```text
IS ANYTHING HERE A TOY?   *** NO.  NOTHING IN THIS ARTIFACT IS A STAND-IN. ***

THE OBJECTS DETERMINED ARE THE RECORD'S OWN ACTUAL OBJECTS:
  - R-CLW is the corpus's one selector-shaped object, sealed in
    STAGE8_TYPING_RULE_CANDIDATE_V001.md, verified OK.
  - NET / G-9 is the corpus's one cell-joining rule, sealed in
    STAGE8_TASK4A_...CODEX_LANE2_V001.md and rowed in the sealed hunt.
  - K_square is a sealed carrier of the actual record, displayed with its own
    named vertices and edges.

THE CAS RAN ONLY ON SEALED COMBINATORIAL DISPLAYS:
  Adj_2 = [[0,1],[1,0]]           — hunt :262-267, the joiner's own display
  K_square's 4 vertices / 4 edges — hunt :226, the record's own vertex/edge list
  NO INVENTED COMPLEX.  NO MODEL GRAPH.  NO ILLUSTRATIVE EXAMPLE.  Had I needed
  a graph the corpus does not display, that would have been C-4's forbidden act
  and I would have stopped instead — as I did.

NO SURFACE WAS SIMULATED.  The determination is about what two sealed documents
say and about the arithmetic they themselves display.  It touches no physical
quantity, no carrier promotion, no adoption, and no program value.
```

---

## 10. IMPORT AUDIT

```text
IMPORTED FROM OUTSIDE THE CORPUS — ONE ITEM, AND ONLY ONE:
  For a finite graph over a field, dim H^1 = dim H_1 = dim Z_1 = E - V + comps
  (rank-nullity applied to the boundary map d_1).
  USED FOR   Certifying that each source's own stated number follows from its own
             stated combinatorial data, and that the nominal homology/cohomology
             difference between the two sources does not affect any value.
  NOT USED FOR  Deciding anything about the corpus's content.  Every substantive
             finding rests on quoted sealed bytes.
  WHY SAFE   It is the identity BOTH sources already use.  The hunt writes
             "E - V + components" at :316 and the typing rule writes
             "of dimension b_1(C_j)" at :156.  I imported no convention they
             do not already share.

EXPRESSLY NOT IMPORTED:
  - Continuum contractibility.  The GC-barred route; the hunt's own fence
    :467-471 bars it and I did not take it.  Every topology statement above
    rests on a sealed COMBINATORIAL presentation.
  - Any physical quantity, scale, coupling, or measured constant.
  - Any relation between strata.  Hunt :325-326 names that map absent; I did not
    supply one, and E-5 turns on its absence.
  - Any admission act, any adoption, any gluing license.
  - Any content from register / tracker / road / plan / continuation files.
    None was read.
```

---

## 11. FLAG BLOCK

```text
FENCES, CARRIED UNCHANGED
  alpha_computed              = false
  proof_authorized            = false
  kappa_record_computed       = false
  No value.  No number as a program quantity.  No measured-constant comparison.
  The only numbers in this artifact are cycle ranks of two sealed graphs and the
  vertex/edge counts they are computed from.

ACTS NOT TAKEN
  Nothing proposed.  Nothing authored.  Nothing adopted.  No joiner constructed.
  No cell admitted.  No carrier promoted.  No stratum crossed.  Nothing repaired.

F-1  *** AN OBSERVATION I AM FLAGGING AND EXPRESSLY NOT REPAIRING. ***
     The hunt's stated quarry is "a glued record COMPLEX with H^1 > 0" (:372-377),
     which is a property of a glued complex.  Its G-9 row computes H^1 of the
     two-node NETWORK (Adj_2), in which each cell is one point.  Whether those two
     quantities coincide for G-9's yield depends on the joined cells' own b_1 —
     which NET does not display, since it displays no cell interiors.
     STATUS  UNRESOLVED AT BYTES.  I record it because it is the same scale
     distinction that decided gate 1, and a reader of this artifact will see it.
     I DO NOT REPAIR IT, do not recompute the hunt's row, do not claim the hunt
     erred, and draw NO consequence from it anywhere in this determination.
     The commission barred repair and the bar is right: resolving this needs the
     cell interiors, and no sealed text supplies them.

F-2  THE COMMISSION'S PREMISE, CORRECTED AT ONE POINT, FOR THE RECORD.
     The commission characterises the joiner as yielding "an object whose first
     cohomology VANISHES — a tree."  That is verbatim correct as to the source's
     words.  What the commission's framing does not carry, and what §3 supplies,
     is WHAT THE TREE IS A TREE OF: a network of two cells, not a cell.

F-3  EXPECTED-UNLOCATABLE ITEMS.  "Q-..." — none sought, none consumed, none
     required by any finding above.

F-4  SCOPE OF THE GATE-2 FINDING.  §4.2's Restriction 2 (admission unsealed)
     defeats domain membership for EVERY object, not only the joined one.  I
     record this so Restriction 2 is not read as a fact about the joiner
     specifically.  Restriction 1 (level) IS specific to the joined object, and
     it alone suffices.
```

---

## 12. VERDICT

```text
*** GATE-1-FAILS ***

THE TWO INVARIANTS ARE NOT THE SAME.  They are one function — cycle rank
E - V + components over a characteristic-0 field — evaluated at TWO DIFFERENT
KINDS OF ARGUMENT:

  the family's index   b_1(C_j)   counts the 0-CELLS INSIDE ONE CELL
                                  (K_square: four vertices, b_1 = 1)
  the joiner's H^1     1-2+1 = 0  counts THE CELLS THEMSELVES as points
                                  (two cells: two vertices, b_1 = 0)

The corpus's own display makes the difference decisive: the same K_square carries
b_1 = 1 as a cell and contributes b_1 = 0 as a node.  The joiner's vanishing
number reports on the network AMONG cells and says nothing about any cell's own
first Betti number — which is the family's index.

THE CHAIN STOPS AT GATE 1.  Deliverable three does not fire.  The consequence
"the joining operation delivers its output into the empty-admissible-set sector"
IS NOT DISPLAYED BY THESE BYTES AND IS NOT ASSERTED HERE.  Neither is its
negation: this is an unanswered question, not a cleared one.

INDEPENDENTLY, GATE 2 ALSO FAILS.  The admissible-set family is defined on
CONNECTED ADMITTED SUBCOMPLEXES of a carrier K, under an admission the rule
declares it does not perform (D1, D3, N2).  The joined object is a K-level
object — a network WHOSE CONSTITUENTS ARE CELLS — not a C_j.  And R-CLW §8 N3
disclaims the whole subject in its own voice: "NO GLUING LICENSE ... the ports
are inert and chain nothing."  What governs the joined object instead is (i)
PRINCIPAL RATIFICATION (PROPOSED_NOT_ADOPTED, DoR-016/017 RESERVED) and (ii) the
hunt's LOOP-CARRYING criterion — which, unlike the admissible-set family, is
stated at the same scale the joiner's number is computed on.

STATUS QUALIFIER (deliverable 4).  The topological fact — Adj_2 has cycle rank
zero — is STRUCTURAL: it holds of the sealed proposal whether or not the rule is
ever adopted, and the source's own concessive says so ("Even if adopted";
"ADOPTION CLOSES NONE OF THEM").  The EXISTENCE of any joined object is
HYPOTHETICAL: "NOTHING SEALED EXISTS: a physical-stratum glued multi-cell record
complex."  The consequence at issue is NEITHER — it is unsupported, failing
before adoption is reached.

ESCAPE SURVEY (deliverable 5).  NO ESCAPE DISPLAYED.  NO ROW ADMITS.  Three rows
BAR outright (E-1 frozen topology and not instantiated; E-2 input underived;
E-5 no sealed map between strata), and E-4 bars under R-CLW's own N3 while the
wider corpus is silent-by-absence there.  E-3 (self-edge / larger graph) is
SILENT, and silence is recorded as silence — the corpus names the moves that
would produce a cycle without supplying either.  ESCAPE-EXISTS is not returned —
and it would be idle if it were, since no consequence stands in need of relief.
```

```text
DETERMINATION ONLY.  Displayed, not constructed.  Nothing proposed, authored,
adopted, or repaired.  alpha_computed = false; proof_authorized = false;
kappa_record_computed = false.
```

*** END OF DETERMINATION — STAGE8_JOIN_ADMISSIBILITY_O28SR_V001 ***
