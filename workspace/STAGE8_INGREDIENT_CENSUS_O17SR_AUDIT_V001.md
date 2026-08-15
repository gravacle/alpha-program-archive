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
