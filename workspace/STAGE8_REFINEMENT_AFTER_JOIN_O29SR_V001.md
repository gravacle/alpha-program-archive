# STAGE 8 — REFINEMENT AFTER JOINING: DOES IT PRODUCE CYCLE CONTENT AT THE NETWORK LEVEL?

Commission O29SR, REFINEMENT-BUILD, 2026-08-15. DETERMINATION ONLY.
Nothing here is proposed, authored, adopted, constructed, or repaired.

## VERDICT — NO-ESCAPE-BY-COMPOSITION

```text
*** NO-ESCAPE-BY-COMPOSITION ***

THE COMPOSITION "REFINEMENT APPLIED AFTER JOINING" IS NOT AVAILABLE AT BYTES.

(1) NO JOINED OBJECT WITH CELL INTERIORS EXISTS OF RECORD.  What the joiner
    yields, of record, is an ADJACENCY — Adj_2 = [[0,1],[1,0]] (NET V001 :449,
    NS-14).  O28SR :894-895 and its audit :215-216 both record that no glued
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
carrier :93:

```text
sd*_1 : C^1(K') -> C^1(K),   (sd*_1 a')_e  = sum_(e' subdividing e) orientation(e',e) a'_(e')
```

**Read the index of summation.** It ranges over the child cells `e'` **subdividing
one parent cell `e`**. Every child in the sum lies inside a single parent. The map
is defined parent-cell by parent-cell and never quantifies over a relation
between two different parent cells. The carrier states the mechanism in its own
voice at :111-112: *"Interior edges of a subdivided parent face are shared by
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
use (O28SR AUDIT :189-196 computes it on K_square at "4 vertices / 4 edges /
NO 2-cell").
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

`STAGE8_JOIN_ADMISSIBILITY_O28SR_V001.md` :894-895, verbatim, the target's own record
(the same sentence also stands at :506 and :621):

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
```

---

## 3. DELIVERABLE THREE — THE COMPOSITION GRANTED ARGUENDO, AND COMPUTED

The composition is not available (§2). I nevertheless run the row, **arguendo**,
because the commission's question deserves an answer that does not rest on an
absence alone. **Nothing in this section constructs anything of record.** It
computes what the network's cycle rank WOULD be, and the answer is the same by
two independent routes.

### 3.1 The level distinction, stated exactly as it is of record, and obeyed here

`STAGE8_JOIN_ADMISSIBILITY_O28SR_V001.md` :861-871, verbatim:

```text
THE TWO INVARIANTS ARE NOT THE SAME.  They are one function — cycle rank
E - V + components over a characteristic-0 field — evaluated at TWO DIFFERENT
KINDS OF ARGUMENT:

  the family's index   b_1(C_j)   counts the 0-CELLS INSIDE ONE CELL
                                  (K_square: four vertices, b_1 = 1)
  the joiner's H^1     1-2+1 = 0  counts THE CELLS THEMSELVES as points
                                  (two cells: two vertices, b_1 = 0)
```

and its ground at :245-250:

```text
                                are objects one level apart in the corpus's own
                                hierarchy, and the corpus itself keeps the levels
                                apart: R-CLW :134 distinguishes the CARRIER K from
                                its ADMITTED CELLS {C_j}.  A network of cells is
                                an object of the K level; b_1(C_j) is an invariant
                                of the C_j level.
```

**I hold the two apart at every step below.** §1.5 computed the C_j level and got
17 / 136 / 50 / 464. §3.2-3.4 compute the K level and get 0 every time. The two
sets of numbers are never combined, compared, or substituted for one another.

### 3.2 The joined pair reproduced exactly, in a fresh environment

Fresh venv, sympy 1.14.0, Python 3.9.6, exact integers only, no floats. A
reciprocal pair counts as ONE edge — this is the corpus's own arithmetic, taken
from the hunt's own display "2 vertices, one reciprocal edge pair = a tree;
H^1 = 1 - 2 + 1 = 0" (`STAGE8_GLUED_TOPOLOGY_HUNT_V001.md` :266, requoted at
O23SR :143), and not a convention I chose.

```text
Adj_2 reproduced = [[0, 1], [1, 0]]   sealed NS-14 [[0,1],[1,0]]   MATCH=True
  diagonal zero (no self-edge) = True
  symmetric (reciprocal)       = True
JOINED NETWORK  V=2  E=1  rank(d_0)=1  components=1   CYCLE RANK = 0
  corpus display 'H^1 = 1 - 2 + 1 = 0' reproduced: 1-2+1 = 0   agree=True
```

### 3.3 REFINE AFTER JOINING — EXHAUSTIVE SEQUENCE SWEEP, EXACT

The commission asks whether **any sequence** of the three generators can raise the
network rank above zero. I do not sample. I enumerate.

```text
EXHAUSTIVE SEQUENCE SWEEP over the three generators, applied AFTER the join.
Each state = (word applied to C_1, word applied to C_2). Depth 0..3 each side.
  words per cell (len<=3) = 40   ordered pairs of words = 1600
  DISTINCT NETWORK CYCLE RANKS OVER ALL 1600 SEQUENCES = [0]
  MAX = 0    ANY SEQUENCE RAISES IT ABOVE ZERO?  False
```

**AND THE SWEEP IS NOT WHY THE ANSWER IS ZERO — the sweep only confirms it.** The
reason is structural and holds at every depth, not merely to depth 3:

```text
THE INVARIANCE ARGUMENT, FROM §1.3-1.4, IN ONE LINE.
A refinement generator's output side carries only cells OF THE SAME PARENT.
Its sd*_1 row for a parent cell e sums over "e' subdividing e" — one parent.
So refinement changes:  the interior complex of a node.
So refinement does NOT change:  the NODE SET of the network (a refined cell is
   still one cell), nor the INTER-CELL EDGE SET (no generator emits an edge whose
   two ends lie in different parents).
Cycle rank of the network is a function of the node set and the inter-cell edge
set ALONE.  Both are refinement-invariant.  THEREFORE THE NETWORK CYCLE RANK IS
REFINEMENT-INVARIANT — AT ANY DEPTH, FOR ANY WORD, IN ANY ORDER.
It is 0 before refining and 0 after.
```

```text
*** WHICH CASE OBTAINS, IN THE COMMISSION'S OWN WORDS. ***
"A subdivision that merely refines within cells while leaving the inter-cell
incidence a tree leaves the network rank at zero."
THIS IS THE CASE THAT OBTAINS.  All three generators refine within cells (§1.4);
the inter-cell incidence is untouched; the network rank is 0.  Displayed above.
```

### 3.4 THE ONE COUNTERFACTUAL THAT COULD HAVE GONE THE OTHER WAY — AND DOES NOT

The only way refinement could reach the network level is if subdividing a cell
were read as REPLACING ONE NODE BY ITS CHILDREN. That reading is the level
conflation the commission forbids, and it is not of record. But it is the
strongest form of the escape, so I compute it rather than dismiss it.

```text
COUNTERFACTUAL (NOT OF RECORD): grant that refining a cell replaces one node by
its child cells, then join the children by the rule of record.
  A1     children=   16   connected with   15 reciprocal pairs -> V=16   E=15   c=1  CYCLE RANK=0
  A2-F   children=   24   connected with   23 reciprocal pairs -> V=24   E=23   c=1  CYCLE RANK=0
  A2-B   children= 1232   connected with 1231 reciprocal pairs -> V=1232 E=1231 c=1  CYCLE RANK=0
```

**Even granted the conflation, the rank is still zero** — because a connected
network on N nodes assembled from N-1 reciprocal pairs is a tree by arithmetic.
Multiplying the cells does not by itself multiply the CYCLES; it multiplies the
nodes, and nodes and edges grow together along a tree. To get cycle content one
needs **an edge the joining rule does not supply**, which is §4.

---

## 4. DELIVERABLE FOUR — THE ORDER QUESTION

### 4.1 Does refining BEFORE joining differ from refining AFTER?

```text
BEFORE:  K --(A1/A2-F/A2-B)--> K'  then join two cells of K'.
         AVAILABLE.  K' is exactly what the generators yield, and the joiner
         takes "two nodes on matched carriers" — cells.  This composition is
         the one the corpus can form.
AFTER:   join, then refine the joined object.
         NOT AVAILABLE.  §2.  No joined complex to refine; no generator domain
         that admits a network.

SO THE ORDERS DIFFER — BUT NOT IN THEIR RESULT.  THEY DIFFER IN AVAILABILITY.
One order is formable and the other is not; and the formable one yields the
same network cycle rank, 0, as §3.3's arguendo run of the unformable one.
```

**Does refinement multiply the cells available to be joined?** YES, and this is
the honest strong point of the escape. Of record, at bytes:

```text
parent K   ONE oriented unit 4-cube.
A1         16 subcubes          (certificate :157 "81 / 216 / 16 subcubes")
A2-F       24 simplices         (certificate :158)
A2-B       1232 triangles       (crosscheck [4056,5082), F'_2 column)
```

One cell becomes many. **So the escape's premise is CORRECT: refinement really
does multiply the candidate cells.** The question is whether joining more cells
can yield a non-tree network. That is §4.2.

### 4.2 THE DECISIVE SUB-QUESTION, FROM THE RULE'S FORM ALONE

The rule's form of record, NET V001 :242 row `N`, selected column:

```text
On matched carriers, use the reciprocal two-node swap, no self-edge, identity
cell matching, and one-tier delay.
```

and its REJECTED-ALTERNATIVES column, same row, verbatim:

```text
Directed graph; weighted edge; self-sourcing; a nontrivial cell
permutation/intertwiner; same-tier/retroactive feeding.
```

Three properties are fixed by the form, and I take each from the rule's own words:

```text
SIMPLE      "weighted edge" is REJECTED; Adj_2 is a 0/1 matrix (NS-14).  So a
            second application between an already-joined pair adds NO new edge —
            it reproduces the same 1.  Parallel edges are unavailable.
LOOPLESS    "no self-edge" is in the SELECTED column.  The one-node loop, which
            is the cheapest possible cycle, is excluded BY THE RULE.
SYMMETRIC   "reciprocal"; and "Directed graph" is REJECTED.  Each pair is ONE
            undirected edge, per the corpus's own arithmetic (§3.2).
```

**Exact computation from these three properties alone.** The maximum number of
edges of a simple loopless graph on N nodes is N(N-1)/2; at connectivity 1 the
maximum attainable cycle rank is therefore N(N-1)/2 - N + 1. Symbolic, exact:

```text
symbolic max cycle rank(N) = n**2/2 - 3*n/2 + 1
identity check  max - (n-1)(n-2)/2 == 0   ->  True   (sympy simplify, exact)

  N=1: max edges= 0   MAX CYCLE RANK = 0
  N=2: max edges= 1   MAX CYCLE RANK = 0   <- THE RULE'S FORM OF RECORD: THE TWO-NODE SWAP
  N=3: max edges= 3   MAX CYCLE RANK = 1
  N=4: max edges= 6   MAX CYCLE RANK = 3
  N=5: max edges=10   MAX CYCLE RANK = 6
  N=6: max edges=15   MAX CYCLE RANK = 10
```

### 4.3 THE ANSWER, AND THE CORRECTION IT CARRIES

```text
AT N=2 — THE NODE COUNT THE RULE ITSELF FIXES — THE MAXIMUM IS ZERO.
A tree is forced, and forced absolutely: not by a choice among admissible edge
families but because on two loopless simple nodes there is only ONE possible
edge and one edge on two nodes is a tree.  No sequence of refinements, and no
choice by any party, can raise it.  THE JOINING RULE'S FORM FORCES A TREE AT THE
NUMBER OF CELLS IT ADMITS.

*** BUT NOT "AT ANY NUMBER OF CELLS", AND THAT MATTERS. ***
At N >= 3 the maximum is (N-1)(N-2)/2, which is positive.  So reciprocity,
"no self-edge", and simplicity DO NOT force a tree on their own.  A three-node
reciprocal family with three pairs has cycle rank 1, exactly.  What forces the
tree is the TWO-NODE SCOPE, and the corpus itself says the scope is a scope:

  NET V001 :347, verbatim:
    "V001 instantiates only the matched two-node class, so no permutation or
     intertwiner is selected."
  NET V001 :340-345, verbatim:
    "On a general reciprocal edge family, the proposal would require isometric
     intertwiners with  tau_(ab)=Theta_a tau_(ba)^* Theta_b.   (NS-8)"
  NET V001 :892-893, verbatim:
    "every member of the matched two-node class is instantiated. It limits what
     the tower proves."

O23SR §3.3 reached this and named it exactly — "two is an instantiation scope,
not a structural ceiling" — and it is right at bytes.  I confirm it independently.
```

```text
WHY THIS DOES NOT REOPEN THE ESCAPE.  Three things hold at once and dropping any
one misstates the record:
 (i)   the general reciprocal edge family is NOT SELECTED (:347, flat indicative);
 (ii)  NS-8 is written in the SUBJUNCTIVE — "WOULD require" — and the intertwiners
       it would require are NAMED, NOT BUILT (:347, "no ... intertwiner is
       selected"); row N REJECTS "a nontrivial cell permutation/intertwiner";
 (iii) NOTHING IN THIS SECTION IS A REFINEMENT GENERATOR.  The three generators
       contribute NOTHING to the inter-cell edge set at any N (§3.3).  Every
       edge in the N>=3 counterfactual would have to come from a joining family
       that is not of record.  So even where a tree is NOT forced, the escape
       route is not through refinement — refinement is inert at this level either
       way.  The commission's question is about the generators, and the
       generators are the one thing that provably cannot supply the missing edge.

I DO NOT ASSERT THAT AN ESCAPE EXISTS AT N >= 3.  No such family is of record,
and asserting one would be the invented escape O28SR AUDIT :507 (row E-3) warns against:
"NEITHER FORECLOSED NOR TAKEN IS NOT AN ESCAPE."  I record the arithmetic and
the three limitations, and stop.
```

---

## 5. DELIVERABLE FIVE — STATUS OF EACH GENERATOR. NO RECOMMENDATION.

Status is displayed as the record carries it. **This artifact recommends nothing,
endorses no adoption, and takes no position on whether any status should change.**

```text
GENERATOR   STATUS OF RECORD                                         WHERE
A1          LICENSED-BY-A-PROPOSED-LAW; its d_0-square CERTIFIED,
  cubical   the certificate itself CLAIMED-THEN-CONFIRMED.
  bisection   - the licensing clause sits in V011, which self-describes
                at :11 as "a proposed Level-1 microscopic law", and
                the span consumed is from the CANDIDATE review packet
                STAGE7_QSPEC_CANDIDATE_V001.                          V011 :11
              - certificate: "D0_SQUARE = CERTIFIED_ALL", but headed
                "All headline results CLAIMED until checked."         CERT :4, :6
              - independently checked: "CERT_VERDICT = CONFIRMED."    CHECK :9
            NOT ADOPTED as a law.  NOT PROPOSED as a joiner.

A2-F        SAME STATUS AS A1, with one narrower qualification of
  Freudenthal record: the certificate binds to the EXHIBITED instance
            only — "no unexhibited class member is claimed."          CERT :234

A2-B        SAME STATUS AS A1, same instance-binding qualification.   CERT :234
  barycentric

COMPOSITES  "common refinements = composites, free by the sealed
            composite-closure step"; not recomputed by the
            certificate, carried from CARRIER §4 / D4 §3.2.           CERT :143-145, :237-241

THE JOINER (context for the above, not itself a generator)
NET V001    PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL RATIFICATION
            (DoR-016/017 RESERVED).                                   NET [80,162)
```

```text
ONE STATUS FACT THAT BEARS ON THE WHOLE QUESTION AND IS RECORDED, NOT ARGUED.
The clause that would license refinement on a WIDER domain than the exhibited
instances is "common refinements preserving the same smooth coframe and
connection" (V011 [46772,47023)).  The refinement carrier records that the
coframe half is NOT DELIVERED and that V011's only two "coframe" occurrences are
both on the S26-barred smooth side (CARRIER :187-192, :423-424).  So the widest
reading of the inventory is conditioned on something the corpus marks undelivered.
I display this and draw no further consequence from it.
```

---

## 6. CHOICE LEDGER

Every choice this determination made, the alternative rejected, and why.

```text
C-1  WHICH INVARIANT.  Cycle rank as E - rank(d_0), cross-checked against
     E - V + components with components by independent exact union-find.
     ALTERNATIVE REJECTED: simplicial H^1 with 2-cells attached.  REASON: the
     corpus's own displays compute the graph invariant (O28SR AUDIT :189-196, on a
     complex with "NO 2-cell"), and the joiner's number 1-2+1=0 is that one.
     Changing the invariant would have compared my number to a different one.
     THE LIMITATION IS STATED, NOT HIDDEN (§1.5 closing block).

C-2  RECIPROCAL PAIR = ONE EDGE.  Taken from the corpus's own arithmetic,
     "2 vertices, one reciprocal edge pair = a tree; H^1 = 1 - 2 + 1 = 0".
     ALTERNATIVE REJECTED: counting a->b and b->a as two edges, which would give
     2-2+1 = 1 and a spurious cycle at the joined pair.  REASON: it would
     contradict the source's own displayed value and would have MANUFACTURED an
     escape out of a counting convention.  This is the single most load-bearing
     convention in the artifact and it is the corpus's, not mine.

C-3  RAN THE ARGUENDO COMPUTATION DESPITE §2 CLOSING THE COMPOSITION.
     ALTERNATIVE REJECTED: stopping at "not available", which the commission
     expressly allows as complete.  REASON: a determination resting only on an
     absence is defeated by anyone who later supplies the absent object.  §3
     survives the absence being waived.

C-4  DID NOT CONSTRUCT A GLUED COMPLEX WITH CELL INTERIORS.
     ALTERNATIVE REJECTED: building one so that refinement could be applied
     literally.  REASON: that is authoring, barred; and it would have decided by
     my construction what the corpus does not display.  §3 instead reasons from
     the generators' own summation index, which needs no such object.

C-5  DECLINED THE NO-ESCAPE-BY-FORM VERDICT.
     ALTERNATIVE REJECTED: selecting it, since composition-unavailability and
     form-forcing both point the same way and NO-ESCAPE-BY-FORM reads as the
     stronger result.  REASON: its wording contains "at any number of cells",
     which is FALSE at bytes ((N-1)(N-2)/2 > 0 for N >= 3).  Selecting a verdict
     whose stated ground is false, because its conclusion is right, is exactly
     the defect the O28SR audit's X-1 corrected.  I do not repeat it.

C-6  ENUMERATED SEQUENCES TO DEPTH 3 RATHER THAN SAMPLING, AND DID NOT REST ON
     THE ENUMERATION.  ALTERNATIVE REJECTED: presenting the 1600-case sweep as
     the proof.  REASON: a finite sweep cannot settle "any sequence".  The
     structural invariance argument (§3.3) settles all depths; the sweep is
     corroboration and is labelled as such.

C-7  RESOLVED NET BY CONTENT HASH, NOT BY FILENAME.  Four versions exist.
     ALTERNATIVE REJECTED: reading the highest version number.  REASON: the
     hunt pins 87f69626 = V001; V004 is a different object and its content was
     not read.
```

---

## 7. TOY_SEPARATION

```text
WHAT IS ACTUAL SURFACE HERE.
 - The three generators exist, are sealed, and are cell-yielding.  Their
   constructions are of record and I reproduced every sealed census exactly
   (16/32; 81/216/16; 16/65/24; 81/544).  REAL.
 - The subdivision map's summation index "e' subdividing e" is of record and is
   what makes refinement inter-cell-inert.  REAL, and it is the actual load-
   bearing fact of this determination.
 - The joiner's Adj_2 = [[0,1],[1,0]], its "no self-edge", and its two-node
   scope are of record at NET V001's own bytes.  REAL.
 - The level distinction is of record, quoted verbatim, and obeyed throughout.  REAL.

WHAT IS NOT SURFACE AND IS LABELLED AS SUCH EVERYWHERE IT APPEARS.
 - The joined complex with cell interiors.  DOES NOT EXIST.  Never constructed
   here.  §3 is explicitly ARGUENDO and says so in its heading.
 - The node-multiplication reading of refinement (§3.4).  NOT OF RECORD; it is
   the level conflation, computed only to show it does not help either.
 - The N >= 3 reciprocal edge family (§4.2-4.3).  NOT SELECTED, intertwiners NOT
   BUILT, and REJECTED in row N's own alternatives column.  The arithmetic is
   displayed; the family is not asserted to be available.

NO TOY WAS SUBSTITUTED FOR THE SURFACE.  The question asked was whether three
specific sealed generators can move a specific sealed number.  I computed the
number the corpus computes, on the objects the corpus seals, in the corpus's own
frame, and reported that they cannot — and separately that they cannot even be
composed with the joiner in the first place.

NO PHYSICAL QUANTITY APPEARS.  No alpha, kappa, coupling, norm, scale, or
measured constant is computed, bounded, compared, or mentioned as a target.
```

---

## 8. IMPORT AUDIT

```text
IMPORTED AND USED
  O17SR AUDIT      the kill-grade finding A-1 naming the three generators;
                   its typed TAKES/YIELDS rows.                  USED, §1.1
  D0_SQUARE CERT   the licensed generator inventory; the three constructions at
                   bytes; the sealed censuses; the instance-binding scope note;
                   the sd*_1 quotation.                          USED, §1.2-1.5, §2.3, §5
  D0_SQUARE CHECK  the independent CERT_VERDICT = CONFIRMED.     USED, §5
  B1A CARRIER      the sd*_1 subdivision law and the interior-cancellation
                   mechanism; the coframe-half STOP.             USED, §1.3, §2.3, §5
  O23SR            the joiner typed by signature; the output side; the
                   instantiation-scope finding.                  USED, §2.1, §4.1-4.3
  O23SR AUDIT      consulted; its content reaches me through O23SR's own
                   requotes, which I checked against NET's bytes. USED, §2.1
  NET V001         row N; NS-8; NS-14; :347; :892-893; the status line.
                   Hash-resolved.                                USED, §2.1, §4.2-4.3, §5
  O28SR            the level distinction verbatim; the "NOTHING SEALED EXISTS"
                   line; the joiner-vs-cell contrast.            USED, §2.2, §3.1
  O28SR AUDIT      X-1 (the unsurveyed refinement class and the refuted premise);
                   :215-216 that no glued complex was constructed. USED, §1.1, §2.2
  V011 (packet)    the licensed inventory span; the d_0 law; the self-description
                   at :11.  Bound to the PACKET MEMBER only.     USED, §1.2, §1.5, §5

IMPORTED AND NOT USED AS EVIDENCE
  O17SR CENSUS     read for the rows the audit corrects; NO determination here
                   rests on it, because its §2.1 is REFUTED of record.
  V002/V003/V004 of NET — NOT READ FOR CONTENT.  Hashed only, to prove they are
                   not the pinned object.

NOT IMPORTED
  Any register, tracker, road, plan, continuation, ledger, or lens file — none
  read, none opened, none listed.
  Any "Q-..." file — none sought (EXPECTED-UNLOCATABLE per commission).
  The TOP-LEVEL V011 copy — the two-byte-version hazard is carried from the
  certificate's own :55-58 and the top-level copy was NOT read.

MACHINERY  reads; shasum -a 256 -c from each artifact's own directory; scoped
  greps; exact integer/rational linear algebra in a fresh venv.  No member
  binding, no fixed-point execution, no end test, no git action, no network.
```

---

## 9. FLAG BLOCK

```text
F-1  THE PREMISE IS REFUTED AND THE ROW IS NOW RUN.  The prior commission's
     no-escape claim rested on "the corpus's only rule with a cell on its output
     side", which its own consumed ground marks REFUTED (O17SR AUDIT :570).  The
     unsurveyed class is surveyed here.  ITS BOTTOM LINE IS UNDISTURBED, BUT IT
     IS NOW SUPPORTED RATHER THAN ASSUMED.  That is the whole value of this
     artifact and it is stated without inflation.

F-2  A FOURTH SUBDIVISION FAMILY EXISTS IN THE CORPUS AND IS OUTSIDE MY SCOPE.
     The declared sweep (§0.2) surfaces "edgewise subdivision" — Ref_PL,
     "objects = order-complex/edgewise subdivisions sd_n(G)", with
     "CommonRef(n,m) = lcm(n,m)".  IT IS NOT ONE OF THE THREE.  Of record it is
     (a) classified a DIFFERENT INDEX from the A-family — "Ref_0 != full
     Ref_PL/P4 generator category" — (b) rooted at Q-408, which this commission
     declares EXPECTED-UNLOCATABLE, and (c) located "inside a proposal ... A
     pointer, not a supply" (RA27_3 FRONTIER :271-279).  I DID NOT SURVEY IT and
     I do not claim my answer covers it.  Named so that no later reader mistakes
     my three-generator scope for a corpus-wide one.

F-3  A SECOND-ORDER DOUBT OF RECORD, CARRIED NOT RESOLVED.  The completeness
     proof reports "zero occurrences, corpus-wide, of any text equating the
     barycentric subdivision with the order-simplex/Freudenthal/edgewise
     subdivision", and that A2's instantiation may rest on "an unstated
     identification" (:479-488).  This does not affect my determination — both
     A2-F and A2-B are computed here SEPARATELY, at their own bytes, and both
     give network rank 0 — but the doubt is of record and I carry it forward
     rather than let my separate treatment silently paper over it.

F-4  THE INVARIANT IS THE 1-SKELETON CYCLE RANK, NOT H^1 OF THE FULL COMPLEX.
     Stated at §1.5 and repeated here so it cannot be lost: the cell-level
     numbers 17 / 136 / 50 / 464 are E - rank(d_0) on the 1-skeleton.  With the
     2-cells attached they are not those numbers.  I use the corpus's invariant
     because the joiner's number is that invariant; comparing across the two
     would be a second level conflation.

F-5  WHAT WOULD CHANGE THIS DETERMINATION.  Exactly one thing at the refinement
     side: a generator of record whose output side carries an edge with ENDS IN
     TWO DIFFERENT PARENT CELLS.  None of the three does; the summation index
     forbids it.  And exactly one thing at the joining side: a selected edge
     family on N >= 3 with at least N pairs.  Neither exists of record today.
     NAMED AS FALSIFIERS, NOT AS THINGS TO BUILD.  I propose neither.

F-6  NO REPAIR PERFORMED.  The refuted premise at O17SR §2.1 and the false
     universal in the NO-ESCAPE-BY-FORM wording are DISPLAYED and left standing.
     I renumber nothing, correct no other artifact, and author no replacement.
```

---

## 10. VERDICT, RESTATED WITH ITS GROUND

```text
*** NO-ESCAPE-BY-COMPOSITION ***

THE QUESTION.  Do the corpus's cell-yielding refinement generators, applied
after joining, produce cycle content at the network level?

THE ANSWER.  NO — and at bytes the composition cannot be formed at all.

  DELIVERABLE 1  Three generators located at their own bytes, seals OK.  All
                 three SUBDIVIDE A SINGLE CELL INTO FINER CELLS.  NONE alters
                 the incidence pattern AMONG cells.  Sealed censuses reproduced
                 exactly: 16/32 ; 81/216/16 ; 16/65/24 ; 81/544.
  DELIVERABLE 2  COMPOSITION NOT AVAILABLE, on two independent affirmative legs:
                 no joined object with cell interiors exists of record, and no
                 generator's domain of record contains anything but the parent
                 4-cube.
  DELIVERABLE 3  Granted arguendo and computed anyway.  Joined network
                 V=2 E=1 rank(d_0)=1 c=1 CYCLE RANK 0, reproducing the corpus's
                 own 1-2+1=0.  All 1600 sequences of the three generators to
                 depth 3 on both cells: DISTINCT RANKS = [0], MAX = 0.  And the
                 structural argument settles ALL depths, not just three.
                 THE COMMISSION'S CASE OBTAINS: refinement refines within cells,
                 the inter-cell incidence stays a tree, the network rank stays 0.
  DELIVERABLE 4  The orders differ in AVAILABILITY, not in result.  Refinement
                 DOES multiply the cells (1 -> 16 / 24 / 1232).  But at the
                 rule's own two-node form the maximum attainable cycle rank is
                 EXACTLY 0 — forced.  The tree is forced AT N=2 and NOT at any
                 number of cells: at N >= 3 the maximum is (N-1)(N-2)/2 > 0.
                 The generators contribute nothing to the inter-cell edge set at
                 ANY N, so no escape runs through them either way.
  DELIVERABLE 5  A1, A2-F, A2-B: licensed by a PROPOSED law, d_0-square
                 CERTIFIED and independently CONFIRMED, instance-bound.  NOT
                 ADOPTED.  The joiner: PROPOSED_NOT_ADOPTED.  No recommendation.

NO ESCAPE IS ASSERTED AND NONE IS INVENTED.  NO ESCAPE IS FORECLOSED BEYOND
WHAT THE BYTES FORECLOSE.  The refinement generators cannot reach the network
level, and the reason is not a limitation anyone chose — it is the summation
index of the corpus's own subdivision map.

FENCES AT CLOSE  alpha_computed = false ; proof_authorized = false ;
  kappa_record_computed = false ; coupling_evaluation_authorized = false.
  NOTHING PROPOSED.  NOTHING AUTHORED.  NOTHING ADOPTED.  NO RULE OR COMPOSITE
  CONSTRUCTED.  NOTHING REPAIRED.  NO VALUE.  NO PROGRAM QUANTITY.  NO
  MEASURED-CONSTANT COMPARISON.  NO GIT.
ALL_RESULTS = CLAIMED until checked.
```

---

## APPENDIX — ENVIRONMENT AND REPRODUCIBILITY

```text
Fresh virtual environment created for this commission; nothing reused.
  python 3.9.6
  sympy 1.14.0
  exact arithmetic only: sympy Integer / Rational.  NO FLOATS ANYWHERE.
  every rank is Matrix.rank() over Q; every component count is cross-checked by
  an independent exact union-find; every cycle rank is cross-checked as
  E - rank(d_0) against E - V + components, and all agree.

CONSTRUCTIONS reproduced independently from the sealed byte-spans, not copied
from any artifact's stored matrices; the certificate discloses at :147-148 that
no sealed artifact stores a dense matrix dump, so reproduction from the
constructive displays is the only available route and is the one taken.
```
