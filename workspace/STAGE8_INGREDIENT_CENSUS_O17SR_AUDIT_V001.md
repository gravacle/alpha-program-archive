# STAGE 8 — AUDIT OF THE INGREDIENT CENSUS (O17SR)

Commission: O17SR. Lane: CENSUS-AUDIT. Date: 2026-08-15.
Posture: DEFAULT-REFUTE. Testimony carries zero weight; every claim re-derived at bytes.
ALL_RESULTS = CLAIMED until checked.

## 0. STEP 0 — TARGET PROBE AND SEAL

```text
TARGET      STAGE8_INGREDIENT_CENSUS_O17SR_V001.md            PRESENT (49383 bytes)
SIDECAR     STAGE8_INGREDIENT_CENSUS_O17SR_V001.md.seal.sha256 PRESENT
SEAL CHECK  shasum -a 256 -c STAGE8_INGREDIENT_CENSUS_O17SR_V001.md.seal.sha256
            run FROM /Users/bgm/MB Work/alpha-program-archive/workspace
            => STAGE8_INGREDIENT_CENSUS_O17SR_V001.md: OK
OUTPUT PATH STAGE8_INGREDIENT_CENSUS_O17SR_AUDIT_V001.md — probed ABSENT before write.
```

```text
GATES  alpha_computed = false ; proof_authorized = false ;
       kappa_record_computed = false.
FENCES HELD: no value, no number, no measured-constant comparison; no git action;
       no register / tracker / road / plan / continuation file read; scoped reads
       and declared scoped sweeps only. DETERMINATION ONLY — this audit types and
       inventories; it proposes nothing and adopts nothing.
NOTE   This auditor is NOT under the blindness bar. The barred band was opened
       for the sole purpose of testing the build for leakage (§5).
```

## 0.1 DECLARED SWEEP AND CUTOFF (THIS AUDIT)

```text
ROOTS   R1  /Users/bgm/MB Work/alpha-program-archive/workspace      (primary)
        R2  /Users/bgm/Documents/New project/gravity_emergence_evidence_program/
            alpha_fundamental_record_action_cleanroom_v003          (secondary)
CUTOFF  2026-08-15, at audit time. R1 top level now: 3588 entries, 1758 *.md,
        1704 *.seal.sha256. The census recorded 3581 / 1754 / 1701. The drift is
        four *.md written after the census sealed; it is disclosed, not charged.

A-SWEEP  the census's own S-A regex, re-run verbatim and uncapped at R1.
B-SWEEP  wider output-side verb band, mine, not the census's:
         (assigns|yields|produces|constructs|returns|outputs|generates|emits|
          builds|creates|delivers)[^.]{0,60}(causal |record |common |primitive )?cells?
         and the same verb set against record / algebra / complex.
C-SWEEP  the barred band opened and searched for leakage signatures.
EXPECTED-UNLOCATABLE: "Q-..." items. Not sought.
```

---
## 1. HEADLINE

```text
OVERALL VERDICT   CONFIRMED-WITH-CORRECTIONS, with one REFUTED deliverable.

REFUTED    §2.1 / FLAG CELL_ON_OUTPUT_SIDE = 1 ("EXACTLY ONE CLAUSE IN THE
           CORPUS").  The corpus carries a sealed, licensed inventory of
           generators whose output side is a complex of new cells.  The census
           did not miss them by sweep: it inventoried them and then filed them
           on the INPUT side of a certificate (row D-1), which is the precise
           frame leakage this commission was told to hunt.

CORRECTED  §2.3 / FLAG JOINING_OF_CELLS_ON_OUTPUT_SIDE = 0.  The category is
           not empty simpliciter.  One rule already resident in the census
           (row B-8) is typed at its own source as gluing two cells.  The
           census's own §1.B entry for it drops that clause.

CORRECTED  §1 / FLAG CENSUS_ENTRIES = 23.  At least five artifacts whose seals
           the census verified in §7 were never typed into the census at all,
           and one sealed parent specification carrying four rules was never
           reached by any of the three declared bands.

CONFIRMED  §3 / FLAG JOINING_ABSENCE_KIND = KIND 1.  Re-derived at the
           absence's own bytes.  The answer stands; the ROUTE to it is
           method-inconsistent and is corrected in §4.

CONFIRMED  §2.2 (record on output side, more than one), §4.1's pairing of the
           certificate family, and the no-leakage claim of §0.3 as to content.
CONFIRMED  Fences: no value, no measured-constant comparison, no git, no
           lens token, no proposal, no adoption. (§7 of this audit.)
```

---

## 2. FINDING A-1 — FRAME LEAKAGE, KILL GRADE. THE REFINEMENT GENERATORS YIELD CELLS.

The census row D-1 reads, at the census's own bytes:

```text
D-1  THE D_0-SQUARE CERTIFICATE.
     TAKES   the five generators (L_id, A0, A1, A2-Freudenthal, A2-barycentric)
             and their composites.
     ...
     TYPE    CERTIFICATE. It yields no new complex, chain, or cell — only
             permission to rely on objects already present.
```

The census thereby types the whole of `STAGE8_D0_SQUARE_CERTIFICATE_V001.md` by
what the artifact is FOR — warranting transport-stability — and puts its five
generators on an input side without ever reading their own signatures. Read at
their own bytes, three of the five are cell-yielding rules. Seal verified OK this
session by `shasum -a 256 -c STAGE8_D0_SQUARE_CERTIFICATE_V001.md.seal.sha256`
from the artifact's own directory.

The artifact carries, under its own heading **"The licensed generator inventory"**,
a verbatim quotation of V011 `[46772,47023)`:

```text
cubical bisection;
oriented simplicial/barycentric subdivision;
and common refinements preserving the same smooth coframe and connection.
```
— STAGE8_D0_SQUARE_CERTIFICATE_V001.md :134-140.

and immediately names the instances:

```text
That is: `A1`; the `A2` class, whose two sealed instances of record are Freudenthal
(`A2-F`) and barycentric (`A2-B`); and common refinements = composites, free by the
sealed composite-closure step
```
— ibid. :142-145.

TYPED BY STRUCTURE, which is the only test the census says it applies:

```text
A1      TAKES   the parent complex K.
        YIELDS  a refined complex — at bytes "cubical bisection, 16 subcubes"
                (:17), tabulated against the sealed census as a complex whose
                cells are subcubes of K's (:157).
        TYPE    RULE.  CELLS STAND ON ITS OUTPUT SIDE.

A2-F    TAKES   the parent complex K.
        YIELDS  a refined complex whose cells are "Freudenthal chains of
                Boolean vertices" (:121), simplices (:158).
        TYPE    RULE.  CELLS STAND ON ITS OUTPUT SIDE.

A2-B    TAKES   the parent complex K.
        YIELDS  a refined complex whose cells are "barycentric chains of
                nonempty 4-cube faces" (:122).
        TYPE    RULE.  CELLS STAND ON ITS OUTPUT SIDE.
```

The subdivision relation is not inferred by this audit; it is written into the
artifact's own transported cochain map, which quantifies over subdividing cells:

```text
sd*_1 : C^1(K') -> C^1(K),   (sd*_1 a')_e  = sum_(e' subdividing e) orientation(e',e) a'_(e')
```
— ibid. :109.

and the artifact's own crosscheck span is pinned as **"the three refined
complexes"** (:67).

CONSEQUENCE FOR THE COMMISSION'S MOST IMPORTANT ANSWER. §2.1's headline —
"**EXACTLY ONE CLAUSE IN THE CORPUS**" — and FLAG `CELL_ON_OUTPUT_SIDE = 1` are
false at bytes. A licensed generator inventory of record puts cells on an output
side, and the census had the artifact open when it wrote the sentence.

WHAT SURVIVES, STATED EXACTLY. The refinement generators take a complex and yield
a complex; they do not construct a cell from anything more primitive than a cell.
So the census's narrower sentence — "No object in the census constructs a cell
from anything more primitive than the undrived parent" (:418) — survives. The
sentence that does not survive is the count, the word EXACTLY, and the flag.

---

## 3. FINDING A-2 — FRAME LEAKAGE, SECOND INSTANCE, SAME BYTES. ROW A-3 "TAKES NOTHING".

The census row A-3 reads:

```text
A-3  The working class — five sealed single-cell complexes (parent K, A1,
     A2-F, A2-B, Z).
     TAKES   nothing.
     ...
     TYPE    OBJECT (five of them).
```

`TAKES nothing` is the census's own definition of OBJECT (§0.1: "yielded; takes
nothing on its input side"). At bytes, four of these five do take something. A1,
A2-F and A2-B are, by the same artifact quoted in §2 of this audit, the results of
applying the licensed generators to the parent complex K — the sealed census table
sets them side by side as parent and refinements:

```text
                       reproduced        sealed (carrier / crosscheck / 795)
parent K               16 / 32 / 24      16 vertices / 32 edges / 24 squares
A1                     81 / 216 / 16     81 / 216 / 16 subcubes
A2-F                   16 / 65 / 24      16 / 65 / 24 simplices (Freudenthal chains)
```
— STAGE8_D0_SQUARE_CERTIFICATE_V001.md :155-158.

`A1` is not a complex that stands on its own; it is the cubical bisection OF the
parent. Its input side carries K. The census typed the row from the AND artifact's
LIST of five, carried at GLUED_TOPOLOGY_HUNT G-10 — that is, from the name of a
grouping ("the working class"), which is exactly what §0 forbids: "Nothing is typed
by its name, its family prefix, its lane, or what it is for."

TYPING NOT FOLLOWING FROM THE SIGNATURE — KILLED:
```text
A-3 as written   five OBJECTs, each TAKES nothing.
A-3 at bytes     one OBJECT (parent K) and one further complex Z not shown by
                 this audit to be a refinement; plus THREE outputs of the
                 generators of §2, whose input side carries K.
```

This audit records the correction and stops. It does not renumber the census.

---

## 4. FINDING B — CENSUS INCOMPLETENESS. RE-SWEPT UNCAPPED, WITH WIDER PATTERNS.

### 4.1 THE DECLARED BANDS DO NOT CLOSE

The census's S-A regex was re-run verbatim and uncapped at R1. It returns 163
files now against the census's 159; the difference is four `*.md` written after
the census sealed, and is disclosed, not charged.

The load-bearing failure is not the count. It is that the census's own CH-3
mitigation is untestable: bands S-B and S-C are the declared guard against an
object that carries no signature line, and **S-C is stated with no reproducible
predicate** — "Every *.md under R1 whose bytes place the terms CELL, RECORD, or a
joining of cells on a declared output side" (:69-71). S-A and S-B are given as
regexes and re-run here; S-C cannot be re-run by anyone, so the census's
completeness claim over its own declared bands is unverifiable at S-C.

### 4.2 FIVE ARTIFACTS: SEALS VERIFIED IN §7, NEVER TYPED INTO THE CENSUS

Counting occurrences of each §7 roster name in the census's own bytes, five appear
exactly once — the §7 line itself — and nowhere in §1 through §4:

```text
1  LOCAL_COVARIANT_CELL_MEASURE_SELECTOR_SPEC_V001
1  SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003
1  STAGE8_CANONICAL_PATCH_COVER_TO_INCIDENCE_GRAPH_FUNCTOR_ATTEMPT_V001
1  STAGE8_GLUED_TOPOLOGY_CHECK_V001
1  STAGE8_TRANSPORT_LAW_POSED_V001
```

§7's own words are "Each verified by `shasum -a 256 -c <sidecar>` ... **before any
reliance on its content**." Five artifacts were verified and then not relied on,
not typed, and not disclosed as untyped. Three of the five sit squarely in the
categories this commission named as answer-inverting. Seals re-verified OK this
session, from the artifact's own directory, for all three examined below.

**LOCAL_COVARIANT_CELL_MEASURE_SELECTOR_SPEC_V001** — a rule the census never
entered. Its input side is fixed at bytes: "the primitive cell is a finite causal
diamond with tips `p` and `q`" (:18). Its output side is a measure on that cell.
TYPE: RULE. NOT a cell on the output side — so §2.1 is not inverted by this one —
but its input side carries a further requirement the census's §2.1 never reckoned
with: "the response is natural under admissible **subdivisions and common
refinements**" (:22-23), and "compatible with **subdivision of the same parent
cell**" (:65). Subdivision of a cell yields cells. This is the second, independent
sealed witness to the finding of §2 above.

**STAGE8_CANONICAL_PATCH_COVER_TO_INCIDENCE_GRAPH_FUNCTOR_ATTEMPT_V001** — a rule
the census never entered, on the exact subject of §2.3 and U-2. At its own bytes:

```text
PATCH_COVER_TO_INCIDENCE_GRAPH_DATA_MAP_PER_FIXED_COVER = true |
IMPORTED_CONDITIONAL |
condition: a fixed indexed cover and chosen overlap-to-edge realization are
supplied before the map is formed.
```
— ibid. :177-181, seal verified OK.

```text
TAKES   a fixed indexed cover {U_i} and a chosen overlap-to-edge realization.
YIELDS  "one graph-like object" (:184-185): "vertices: one vertex v_i for each
        patch U_i; edges: one edge e_ij for each nonempty pairwise overlap
        U_i cap U_j" (:192-196).
TYPE    RULE.  An INCIDENCE STRUCTURE stands on its output side.
```

It is a joining of PATCHES, not of cells, and the artifact itself blocks the
promotion: `CANONICAL_PATCH_COVER_TO_INCIDENCE_GRAPH_FUNCTOR_BUILT = false`
(:27), `PATCH_COVER_TO_INCIDENCE_GRAPH_FUNCTOR_AS_SEALED = false` (:171), and
"The current sealed corpus does not supply that theorem" (:213-214). So §2.3's
answer on CELLS is not inverted. But a rule with an incidence graph on its output
side, sealed and seal-verified by the census itself, is missing from a census
whose organising principle is the output side.

### 4.3 AN ENTIRE SEALED SPECIFICATION NO DECLARED BAND REACHED

`R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md` (seal verified OK this
session from its own directory) matches **neither S-A nor S-B** — both re-run here
against it return zero — and is not in the census at any point. It is reached from
inside the swept band: `STAGE8_AXN_FORM_QUESTION_AUDIT_CODEX2_V001.md` (seal OK)
pins it by file SHA and span in its supply inventory (:159-160).

It carries at least four rules the census does not have:

```text
h_K(t)     TAKES   a finite causal complex K and the Dirac Hamiltonian h_0[g,a].
           YIELDS  "the one-particle parent"
                   h_K(t) = h_0[g,a] + sum_(c in K) v_c(t) M_c(t) tensor S_n
                            tensor iota_c(c_c).
           TYPE    RULE.  A PARENT stands on its output side.   (:126-134)

H_K(t)     TAKES   h_K(t).   YIELDS "the many-source parent ... the
           operator-valued number-preserving quasifree lift" H_K = dGamma_R(h_K).
           TYPE    RULE.                                          (:141-146)

D_K        TAKES   the same cell data.  YIELDS "the covariant first-order kernel"
           and its square's descendant terms.  TYPE  RULE.        (:159-173)

R(K)       TAKES   the set of cells of K.  YIELDS the record factorisation
           R(K) = tensor_(c in K) R_c, with "one global source CAR algebra"
           and record factors "even and distinguishable".
           TYPE    RULE.  A RECORD ALGEBRA stands on its output side.  (:61-70)
```

CONSEQUENCE, STATED WITHOUT GOING BEYOND THE TYPING:

- `R(K)` is a **fourth** object with a record on its output side. FLAG
  `RECORD_ON_OUTPUT_SIDE = 3` understates the census's own subject matter.
- `h_K` does **not** kill U-1. Its output-side "parent" is an operator built by
  summing over cells already given; the U-1 parent is the agent that ASSIGNS the
  cell. Different signatures, and this audit declines to merge them on the shared
  noun "parent" — that would be the very error charged in §2. Further, the
  artifact's own status line reads "Forward-sealed construction specification.
  The complete-parent result **has not been executed**" (:7-8). U-1 SURVIVES,
  and is now corroborated by a witness the census never had.
- §2.3's supporting sentence "**the only other object taking many cells at once**"
  (of B-2) is false at bytes: `h_K`, `D_K` and `R(K)` all take many cells at once.
  And `D_K^2` carries, on its own output side, terms indexed by cell PAIRS —
  "overlap terms for causally overlapping cells" (:180) — with the evolution gate
  requiring "causal-factorization for spacelike-separated cells" (:201). These are
  inter-cell relations. They are NOT a glued complex, so §2.3's answer stands; but
  the census's absolute phrasing ("the inter-cell incidence set is EMPTY") is
  quoted from one artifact's per-object scope and generalised to the corpus.

---

## 5. FINDING C — THE UNPAIRED LIST. ONE KILL, ONE OMISSION, EIGHT STANDING.

The census's derivation rule for §4 is mechanical and stated: "for every object in
§1, read its input side; ask whether any object in §1 has that item on its output
side; if none does, it is unpaired." Applied against the census's own §1, the rule
was not run to completion on one entry.

### 5.1 KILL — U-3's ENUMERATION SKIPS THE ONE ROW THAT WOULD HAVE COMPLICATED IT

U-3 (A CONNECTED COMPOSITION OF CELLS) discharges itself in one line:

```text
YIELDED BY     nothing in the census — this is exactly the empty category of
               §2.3. B-1 yields only disjoint unions; B-2 yields a row with an
               empty inter-cell side.
```

Two rows are checked. The census's §1.B has eight. The row not checked is B-8,
and B-8 is the one whose source clause, at the same artifact and the same sweep
the census leaned on for §2.3, reads verbatim:

```text
G-9  THE NETWORK SOURCING PROPOSAL (NET 87f69626, spans 9c6c594b/6a74a4fa).  CONN.
     Status of record: PROPOSED_NOT_ADOPTED (DoR-016/017 RESERVED) — the artifact
     is sealed; the LAW is not adopted.  Its combinatorial content: a TWO-NODE
     network, Adj_2 = [[0,1],[1,0]], "no self-edge", reciprocal, one-tier delayed.
     As a graph: 2 vertices, one reciprocal edge pair = a tree; H^1 = 1 - 2 + 1
     = 0.  Even if adopted, IT GLUES TWO CELLS into a contractible object.
```
— STAGE8_GLUED_TOPOLOGY_HUNT_V001.md :262-267, seal verified OK. Emphasis added
by this audit; the words are the source's.

The census's own row B-8 reproduces every clause of that span EXCEPT the last one.
It carries "TWO-NODE", "Adj_2", "no self-edge", "reciprocal", "one-tier delayed",
and "PROPOSED_NOT_ADOPTED", and it drops "it glues two cells". That is a typing
that does not follow from the signature at bytes: the source states the output
side, and the census's entry replaces it with the output's combinatorial data.

The independently sealed source artifact carries the same content at its own
bytes — `STAGE8_TASK4A_NETWORK_SOURCING_LAW_ADOPTION_PROPOSAL_CODEX_LANE2_V001.md`
(sidecar present at path as `.md.seal.sha256`), row `N`: "On matched carriers, use
the reciprocal two-node swap, no self-edge, **identity cell matching**, and one-tier
delay" (:242), with §4.2 "Edge transport ... For a matched-carrier edge `a->b` ...
the declared identity label match" (:332-340).

WHAT THIS DOES AND DOES NOT DO:
```text
DOES NOT   overturn §3.  The glue is unadopted, and its yield is contractible
           (H^1 = 0 at the source's own words), so it is not the loop-creating
           constructor whose absence §3 types.  §3 stands.
DOES       overturn the flat statements.  "NOTHING. THE CATEGORY IS EMPTY" (:469)
           and FLAG JOINING_OF_CELLS_ON_OUTPUT_SIDE = 0 are not what the census's
           own inventory supports.  The supportable statement is narrower:
           NOTHING ADOPTED, AT THE PHYSICAL STRATUM, YIELDS A JOINED COMPLEX;
           one census-resident PROPOSED rule glues two cells and yields a
           contractible object.
DOES       overturn U-3 as written.  U-3's "nothing in the census yields it" is
           asserted after checking two of eight candidate rows.
```

### 5.2 OMISSION — A PAIR THE CENSUS DID NOT TEST

U-6 (AN INHABITANT OF `L_c`, AND A CELL PAIRING) records "YIELDED BY nothing in
the census," resting on a quotation scoped to one item (T1) of one crosscheck.
The census never tested it against `R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_
SPEC_V001.md`, which displays a fixed per-cell envelope `v_c(t)` on an explicit
interval and assembles `C_K(x) = sum_c v_c(x) M_c(x) iota_c(c_c)` (:103-113,
:159-163), and which additionally supplies the cell-pairing side U-6 names —
"overlap terms for causally overlapping cells" (:180).

TYPED, NOT RESOLVED. This audit does not rule U-6 paired. The artifact's own
status is "Forward-sealed construction specification. The complete-parent result
has not been executed" (:7-8), and R3.4 is a specification of what an executable
must verify, not an executed yield. The finding is that U-6's "nothing yields it"
was never put to the one sealed artifact in the corpus that displays a candidate,
so the entry does not, as the commission requires, show that nothing in the census
yields what it takes.

### 5.3 THE EIGHT THAT STAND

U-1, U-2, U-4, U-5, U-7, U-8, U-9, U-10 were re-tested against this audit's wider
sweep and against the artifacts of §4 above. Each still shows nothing on any
output side that would supply it.

U-1 is strengthened, not weakened, by §4.3: the one new artifact carrying a
"parent" on an output side carries a different parent by signature, and declares
itself unexecuted. U-2 is strengthened by §4.2: the patch-cover data map CONSUMES
a cover as a stated precondition and does not produce one. U-9 is left standing
but is now under-tested: the census never asked whether the three refined
complexes of §2 are members of `C_ref`, and this audit does not answer it either,
because the answer requires a typing the corpus does not display.

---

## 6. FINDING D — THE JOINING-ABSENCE KIND. ANSWER CONFIRMED, ROUTE CORRECTED.

The commission flags this as the deliverable most likely to be read through a
wanted answer. It was re-derived here from the absence's own bytes, independently
of the census's reading.

`STAGE8_GLUED_TOPOLOGY_HUNT_V001.md` :359-369 and :372-377 were read directly.
The census's quotation of both spans is verbatim and complete; no clause is
dropped, softened, or reordered. The corpus's nouns are as the census reports:
"the UNBUILT constructor pair", "the constructor is the unbuilt
successor/anchoring law", "a NAMED constructor", "neither discharges the
physical-stratum constructor", "a construction gap, not a formalism gap".

KIND 1 IS THE CORRECT DETERMINATION, and it survives the harder test — being
re-derived from the two named pieces' signatures rather than from the corpus's
choice of noun:

```text
O11  the successor law.  The same artifact records, at G-3, what is absent:
     "no successor map, nothing links j to j+1".  A successor law's output side
     therefore carries an adjacency that does not otherwise exist.  KIND 1.
O12  port-to-0-cell anchoring.  Its output side is an identification of two
     slots with cells of a complex; an identification yields a quotient object.
     KIND 1.
```

CORRECTION TO THE ROUTE. §3.1's own heading is "**THE CORPUS'S OWN WORDS DECIDE
IT: KIND 1**", and its stated ground is "The determining evidence is lexical and
repeated, and it is the record's own choice of noun." The signature reading is
offered second, as confirmation — "confirms the noun rather than merely echoing
it". That inverts the census's own governing rule, declared twice: "Nothing is
typed by its name" (§0) and "TYPING BY STRUCTURE, NOT BY NAME" (CH-1). In an
artifact that types by structure, a determination whose primary evidence is a
noun is method-inconsistent even when the answer is right. Here it is right, and
this audit re-derives it from the signatures, which is the ground §3.1 should
have led with.

§3.2 IS CORRECT AND IS THE CENSUS'S STRONGEST PASSAGE. The compound absence is
reported as compound; the third conjunct is typed KIND 2 and kept separate; the
corpus's own grammar ("constructor pair" vs "obligation") is given as the ground.
The closing sentence — "nothing can warrant a joined structure before something
yields one" — was tested against the ban on conclusions beyond the typing and is
held WITHIN bounds: it restates that a Kind 2 object has no argument until a
Kind 1 object supplies one, which is a fact about the two signatures.

§3.3 CHECKED AND CONFIRMED. `STAGE8_DESC_STITCHING_RULE_HUNT_DARIO_V001.md` seal
verified OK. The second absence is a functor — takes a category of complexes,
yields members of a physical class — hence KIND 1, and the census's insistence
that it is a DIFFERENT join (finite-to-completed, not cell-to-cell) is a
distinction the census draws against its own interest and is correct.

---
