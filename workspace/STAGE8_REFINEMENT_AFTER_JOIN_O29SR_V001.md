# STAGE 8 — REFINEMENT AFTER JOINING: DOES IT PRODUCE CYCLE CONTENT AT THE NETWORK LEVEL?

Commission O29SR, REFINEMENT-BUILD, 2026-08-15. DETERMINATION ONLY.
Nothing here is proposed, authored, adopted, constructed, or repaired.

## VERDICT — NO-ESCAPE-BY-COMPOSITION

```text
*** NO-ESCAPE-BY-COMPOSITION ***

THE COMPOSITION "REFINEMENT APPLIED AFTER JOINING" IS NOT AVAILABLE AT BYTES.

(1) NO JOINED OBJECT WITH CELL INTERIORS EXISTS OF RECORD.  What the joiner
    yields, of record, is an ADJACENCY — Adj_2 = [[0,1],[1,0]] (NET V001 :449,
    NS-14).  O28SR :866-871 and its audit :215-216 both record that no glued
    complex with cell interiors was ever constructed.  A refinement generator
    consumes a complex with cells.  There is no such joined complex to consume.

(2) NO GENERATOR'S DOMAIN OF RECORD CONTAINS ANYTHING BUT THE PARENT 4-CUBE.
    All three are constructed at bytes from the oriented unit 4-cube's own
    coordinate data and from nothing else (§1.4).  None takes a network, an
    adjacency, or an arbitrary complex.  A joined network is in no generator's
    domain.

BOTH LEGS ARE AFFIRMATIVE AND EITHER ALONE CLOSES THE COMPOSITION.

AND THE ESCAPE DOES NOT SURVIVE BEING GRANTED THE COMPOSITION ARGUENDO (§3):
    refinement subdivides WITHIN one cell.  Its output side carries only cells
    of the SAME parent — the corpus's own transported map sums over
    "e' subdividing e", strictly inside one parent cell.  It adds no node and
    no inter-cell edge.  Over all 1600 sequences of the three generators applied
    to a joined pair, the NETWORK cycle rank is 0, without exception, exactly.

*** I DECLINE NO-ESCAPE-BY-FORM, AND THE REASON IS A CORRECTION (§4.3). ***
The verdict option as worded — "the joining rule's form forces a tree at ANY
number of cells" — is FALSE AT BYTES.  Reciprocity and "no self-edge" alone do
not force a tree: at N >= 3 the maximum attainable cycle rank is (N-1)(N-2)/2 > 0.
What forces the tree is the TWO-NODE scope written into row N, which is a scope,
not a consequence of the edge form.  The tree is forced AT N=2 and nowhere else.
Selecting NO-ESCAPE-BY-FORM would have carried a false universal quantifier into
the record.  The composition leg is affirmative and does not need it.
```

```text
FENCES HELD.  alpha_computed = false ; proof_authorized = false ;
kappa_record_computed = false ; coupling_evaluation_authorized = false.
No value, no number as a program quantity, no measured-constant comparison.
Every integer below is a cell count, an incidence-matrix rank, a component
count, or a cycle rank.  No git action.  No register/tracker/road/plan/
continuation file read.
```

---

## 0. PREFLIGHT

Output name probed ABSENT before any write:
`STAGE8_REFINEMENT_AFTER_JOIN_O29SR_V001.md` — ABSENT, and its `.seal.sha256` — ABSENT.

### 0.1 Seals verified — `shasum -a 256 -c` FROM EACH ARTIFACT'S OWN DIRECTORY

```text
ALL VERIFIED OK THIS SESSION, workspace/ = /Users/bgm/MB Work/alpha-program-archive/workspace/

COMMISSIONED GROUND
  STAGE8_INGREDIENT_CENSUS_O17SR_AUDIT_V001.md            OK    (the kill-grade finding)
  STAGE8_INGREDIENT_CENSUS_O17SR_V001.md                  OK
  STAGE8_GLUING_CANDIDATE_O23SR_V001.md                   OK    (the joiner, typed)
  STAGE8_GLUING_CANDIDATE_O23SR_AUDIT_V001.md             OK
  STAGE8_JOIN_ADMISSIBILITY_O28SR_V001.md                 OK    (the level distinction)
  STAGE8_JOIN_ADMISSIBILITY_O28SR_AUDIT_V001.md           OK    (X-1, the unsurveyed escape)

FOLLOWED BY CITATION (the generators' own source and its inputs)
  STAGE8_D0_SQUARE_CERTIFICATE_V001.md                    OK    (generator inventory + subdivision map)
  STAGE8_D0_SQUARE_CHECK_V001.md                          OK    (its independent check)
  STAGE8_B1A_REFINEMENT_CARRIER_DARIO_V001.md             OK    (the sd*_1 subdivision law)

RESOLVED BY CONTENT HASH, NOT BY NAME (four versions exist; the hunt pins one)
  STAGE8_TASK4A_NETWORK_SOURCING_LAW_ADOPTION_PROPOSAL_CODEX_LANE2_V001.md
      computed 87f696261651567e04242abc1a54d5a2b457a19e07926e9e9856b02dc1719eb1
      pinned   87f696261651567e...  (O23SR :66-76, from the hunt's own import line)
      MATCH.  V002 9b2e42f8 / V003 51724fae / V004 69f4d93b — NOT the pinned object,
      NOT read for content.
```

### 0.2 Declared scoped sweep, and the CUTOFF

```text
SWEEP CUTOFF (UTC):  2026-08-15T22:05:12Z
R1  workspace/                     1,778  *.md at top level
R2  ...cleanroom_v003/             2,308  *.md
S-1 lexical, both roots, uncapped:
      "cubical bisection" | "Freudenthal" | "barycentric subdivision"
      R1 hits in 55 files ; R2 hits in 63 files.
S-2 fourth-generator probe, R1, uncapped:
      "edgewise|stellar|midpoint subdivision" | "sd^n"
      ONE further family surfaces — see FLAG F-2.  It is not one of the three.
"Q-..." items: EXPECTED-UNLOCATABLE per commission; Q-408 is encountered by
      reference only (F-2) and no Q-file was sought or read.
```

---

## 1. DELIVERABLE ONE — THE THREE GENERATORS AT THEIR OWN BYTES

### 1.1 Where the commission's ground names them

`STAGE8_INGREDIENT_CENSUS_O17SR_AUDIT_V001.md` :83, heading verbatim:

```text
## 2. FINDING A-1 — FRAME LEAKAGE, KILL GRADE. THE REFINEMENT GENERATORS YIELD CELLS.
```

and :98-99 verbatim: *"Read at their own bytes, three of the five are cell-yielding
rules."* The audit's consequence line, :153-156, is that the prior census's
`CELL_ON_OUTPUT_SIDE = 1` and the word EXACTLY *"are false at bytes"*, and its
verdict table :570 marks §2.1 `*** REFUTED ***`. I re-read all of this at bytes and
it is exactly as the O28SR audit's X-1 reports it. **The premise on which the
no-escape claim rested is refuted by the commission's own ground, and my survey
below is the row that was never run.**

### 1.2 Following the audit to the artifact that holds the inventory

The audit cites `STAGE8_D0_SQUARE_CERTIFICATE_V001.md`. Seal verified OK from its
own directory. Its **"The licensed generator inventory"** carries V011
`[46772,47023)` verbatim (certificate :137-139):

```text
cubical bisection;
oriented simplicial/barycentric subdivision;
and common refinements preserving the same smooth coframe and connection.
```

and names the instances (:142-145): `A1`; the `A2` class with sealed instances
Freudenthal (`A2-F`) and barycentric (`A2-B`); *"common refinements = composites"*.

### 1.3 The subdivision map, which fixes the LEVEL

The relation is not inferred. It is written into the corpus's own transported
cochain map — CARRIER `[5151,9996)`, quoted identically at certificate :109 and
carrier :92:

```text
sd*_1 : C^1(K') -> C^1(K),   (sd*_1 a')_e  = sum_(e' subdividing e) orientation(e',e) a'_(e')
```

**Read the index of summation.** It ranges over the child cells `e'` **subdividing
one parent cell `e`**. Every child in the sum lies inside a single parent. The map
is defined parent-cell by parent-cell and never quantifies over a relation
between two different parent cells. The carrier states the mechanism in its own
voice at :110-111: *"Interior edges of a subdivided parent face are shared by
exactly two subfaces with opposite induced incidence, so they cancel; boundary
edges survive with the parent sign."* **This is the decisive structural fact of
this artifact and everything in §3 follows from it.**

### 1.4 EXACTLY WHAT EACH TAKES AND YIELDS, AND AT WHICH LEVEL

Each generator's construction is reproduced at bytes from the certificate's own
verbatim script (:371-423). I display the domain each one actually reads:

```text
A1 — CUBICAL BISECTION
  TAKES   the parent complex K = the oriented unit 4-cube.  At bytes the
          construction reads the 4-cube's coordinates and nothing else:
          "GV = sorted(product((0,1,2), repeat=4))"                    (:372)
          and sd*_1 is built by iterating "for (s,t) in PE" — the PARENT edges —
          and depositing each parent edge's TWO CHILD EDGES               (:382-389)
  YIELDS  a refined complex, 81 / 216 / 16 subcubes.
  LEVEL   SUBDIVIDES A SINGLE CELL INTO FINER CELLS.
  INTER-CELL INCIDENCE ALTERED?   NO.  Every child it emits is a subcube OF the
          one parent.  Its sd*_1 row for parent edge e touches only e's own
          two children.

A2-F — FREUDENTHAL SUBDIVISION
  TAKES   the parent complex K.  At bytes: vertices are the parent's own
          ("FV, fvi = PV, pvi", :394) and edges are the parent's Boolean
          coordinate order, "u != v and all(u[k] <= v[k] ...)"           (:395-396)
  YIELDS  a refined complex, 16 / 65 / 24 simplices ("Freudenthal chains of
          Boolean vertices").
  LEVEL   SUBDIVIDES A SINGLE CELL INTO FINER CELLS.
  INTER-CELL INCIDENCE ALTERED?   NO.  Its sd*_1 is the identity on parent edges
          ("Freudenthal rows retain parent edges", :407) — it adds interior
          structure and leaves the parent's own boundary edges intact.

A2-B — BARYCENTRIC SUBDIVISION
  TAKES   the parent complex K.  At bytes the node set is the poset of NONEMPTY
          FACES OF THE 4-CUBE, coordinate 2 encoding a free direction
          ("BF = sorted(product((0,1,2), repeat=4))  # 81 faces", :410) and the
          edges are the proper-subface relation of that same cube    (:412-415)
  YIELDS  a refined complex, 81 / 544 ("barycentric chains of nonempty 4-cube
          faces").
  LEVEL   SUBDIVIDES A SINGLE CELL INTO FINER CELLS.
  INTER-CELL INCIDENCE ALTERED?   NO.  Its sd*_1 row for parent edge e carries
          exactly e's two half-edges, one along and one against         (:419-421)
```

```text
*** THE ANSWER TO DELIVERABLE ONE, STATED FLAT. ***
ALL THREE SUBDIVIDE A SINGLE CELL INTO FINER CELLS.
NONE ALTERS THE INCIDENCE PATTERN *AMONG* CELLS.  Each alters incidence only
WITHIN one cell.  This is not my reading imposed on them: it is the index of
summation in the corpus's own sd*_1, and it is the parent-by-parent form of all
three constructions at bytes.
```

### 1.5 THE GENERATORS ARE NOT INERT — AT THE CELL LEVEL. EXACT, CAS.

To keep the level distinction honest in both directions I compute what refinement
**does** change. Fresh venv, sympy 1.14.0, Python 3.9.6, exact `Integer`/`Rational`
only, no floats. Cycle rank of the 1-skeleton = `E - rank(d_0)`, cross-checked
against `E - V + components` with components obtained independently by exact
union-find. `d_0` per V011 `[44595,44690)`: `(d_0 lambda)_e = lambda_t - lambda_s`.

```text
=== PART 1 - CELL LEVEL (counting the 0-CELLS INSIDE ONE CELL) ===
parent K (oriented unit 4-cube)
   V=16  E=32   rank(d_0)=15  components=1 (union-find 1, agree=True)
   cycle rank = E - rank(d_0) = 17    check E-V+c = 17   agree=True
A1  cubical bisection
   V=81  E=216  rank(d_0)=80  components=1 (union-find 1, agree=True)
   cycle rank = 136                   check E-V+c = 136  agree=True
A2-F  Freudenthal subdivision
   V=16  E=65   rank(d_0)=15  components=1 (union-find 1, agree=True)
   cycle rank = 50                    check E-V+c = 50   agree=True
A2-B  barycentric subdivision
   V=81  E=544  rank(d_0)=80  components=1 (union-find 1, agree=True)
   cycle rank = 464                   check E-V+c = 464  agree=True

CENSUS CHECK against the sealed displays (certificate :155-158):
   parent K  reproduced (16, 32)        sealed (16, 32)        MATCH=True
   A1        reproduced (81, 216, 16)   sealed (81, 216, 16)   MATCH=True
   A2-F      reproduced (16, 65, 24)    sealed (16, 65, 24)    MATCH=True
   A2-B      reproduced (81, 544)       sealed (81, 544)       MATCH=True
```

**Every sealed census reproduces exactly from my own independent construction.**
And the generators plainly DO move the cell-level number: 17 -> 136, 50, 464.
**That is the whole point of the level distinction.** A rule that is highly active
at the C_j level can be completely inactive at the K level, and these three are.

```text
STATED LIMITATION, NOT ELIDED.  The four numbers above are cycle ranks of the
1-SKELETON — E - rank(d_0) — which is the invariant the corpus's own displays
use (O28SR :190-196 computes it on K_square at "4 vertices / 4 edges / NO 2-cell").
It is NOT the complex's H^1 once 2-cells are attached; with the 24 parent faces
attached the parent's H^1 is not this number.  I compute the corpus's invariant,
in the corpus's frame, and claim nothing about the other one.
```

---

## 2. DELIVERABLE TWO — THE COMPOSITION QUESTION. *** NOT AVAILABLE. ***

The question: can refinement be applied to a joined object at all — is a joined
network in any generator's domain, or do the generators act only on a carrier
prior to joining?

### 2.1 What the joiner actually yields, at bytes

`STAGE8_GLUING_CANDIDATE_O23SR_V001.md` :218-222, the typed output side:

```text
OUTPUT SIDE TWO CELLS JOINED BY ONE RECIPROCAL EDGE PAIR.
            Combinatorially: Adj_2 = [[0,1],[1,0]], "no self-edge", reciprocal,
            one-tier delayed  (NET span 6a74a4fa, NS-14).
            As a glued structure: 2 vertices, 1 reciprocal edge pair.
```

I re-read the underlying NET V001 at its own bytes (hash-resolved, §0.1). Row `N`
at :242, verbatim, the SELECTED content:

```text
| `N` — network incidence | On matched carriers, use the reciprocal two-node
swap, no self-edge, identity cell matching, and one-tier delay. | Directed graph;
weighted edge; self-sourcing; a nontrivial cell permutation/intertwiner;
same-tier/retroactive feeding. | ...
```

and :446-449:

```text
For the two-node matched network, the adjacency is
Adj_2=[[0,1],[1,0]].                                (NS-14)
```

**The yield of record is an ADJACENCY MATRIX. It is not a cell complex.** It has
nodes and one reciprocal edge pair. It has no 0-cells, no 1-cells, no faces, no
coordinates, no coframe, and no connection.

### 2.2 LEG ONE — THERE IS NO JOINED COMPLEX TO REFINE

`STAGE8_JOIN_ADMISSIBILITY_O28SR_V001.md` :884-886, verbatim, the target's own record:

```text
"NOTHING SEALED EXISTS: a physical-stratum glued multi-cell record complex."
```

and its audit `STAGE8_JOIN_ADMISSIBILITY_O28SR_AUDIT_V001.md` :215-216, verbatim,
recording what the target did and did not build:

```text
I computed NOTHING the corpus does not display.  No glued complex with cell
interiors was constructed, exactly as the target's C-4 declined to construct one.
```

```text
LEG ONE, STATED EXACTLY.
A refinement generator's input side is a COMPLEX WITH CELLS — that is the whole
content of "TAKES the parent complex K", and sd*_1's summation index requires
parent cells to have interiors for children to subdivide.
The joined object of record HAS NO CELL INTERIORS.  It is an adjacency.
There is therefore no joined object in the corpus for a generator to consume.
Constructing one would be an authoring act this commission bars.  I do not
perform it, exactly as O28SR's C-4 declined, and exactly as O28SR's audit A-3
recorded that running this row was barred to IT.  It is not barred to me as a
DETERMINATION — but the determination is that the object is absent, not that I
should supply it.
```

### 2.3 LEG TWO — NO GENERATOR'S DOMAIN ADMITS A NETWORK

This is the independent leg, and it does not depend on leg one. Even granting a
joined complex arguendo, is it in any generator's domain?

```text
GENERATOR   DOMAIN AT BYTES (certificate :371-423, verbatim constructions)
A1          product((0,1,2), repeat=4) over the 4-cube's coordinates;
            sd*_1 built by iterating the PARENT 4-cube's 32 edges.
A2-F        the 4-cube's own 16 Boolean vertices and their coordinate order.
A2-B        the poset of nonempty faces OF THE 4-CUBE, encoded {0,1,2}^4.

NOT ONE OF THE THREE READS ANY INPUT OTHER THAN THE ORIENTED UNIT 4-CUBE'S OWN
COORDINATE DATA.  There is no generator of record that takes an arbitrary
complex, a network, an adjacency matrix, or a family of cells.
```

The certificate says so in its own voice, at :231-235:

```text
**Scope of the A2 class.** V011 licenses `A2` as a class ("oriented simplicial/
barycentric subdivision"). Both sealed instances of record (`A2-F`, `A2-B` ...)
are certified by explicit algebra. The certificate binds to these exhibited
instances; no unexhibited class member is claimed
```

**"The certificate binds to these exhibited instances."** The class is named; the
domain of record is the two exhibited instances on the parent 4-cube. An
unexhibited class member that took a joined network is not of record, and the
certificate expressly declines to claim one.

And the inventory clause itself carries a domain restriction that is fatal here —
V011 `[46772,47023)`: *"common refinements preserving the same smooth coframe and
connection."* The refinement carrier records at :187-192 that this half is **NOT
DELIVERED**:

```text
STOP.  THE COFRAME HALF OF THE CARRIER IS NOT DERIVED.
   ... And the word "coframe" occurs in the sealed V011 exactly twice (46197,
   46996) — BOTH on the SMOOTH tetrad side, which S26 bars as a source.
```

So the very clause that would license "common refinements" on a wider domain is
conditioned on a coframe half that the corpus records as undelivered and barred.

### 2.4 THE ANSWER

```text
*** THE COMPOSITION IS NOT AVAILABLE. ***

IS A JOINED NETWORK IN ANY GENERATOR'S DOMAIN?          NO.  (§2.3)
DO THE GENERATORS ACT ONLY ON A CARRIER PRIOR TO JOINING? YES — and on ONE
                                                        SPECIFIC CARRIER, the
                                                        oriented unit 4-cube.
IS THERE EVEN A JOINED OBJECT OF THE RIGHT KIND TO FEED THEM?  NO.  (§2.2)

Per the commission: "If the composition is not available, say so and display why;
that is a complete answer."  IT IS NOT AVAILABLE, AND §2.2-2.3 DISPLAY WHY.

I do not stop here.  §3 grants the composition arguendo and runs it anyway,
because a determination that rests only on an absence is weaker than one that
also survives the absence being waived.
