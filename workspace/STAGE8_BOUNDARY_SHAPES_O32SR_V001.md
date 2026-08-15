# STAGE 8 — THE THREE BOUNDARY SHAPES, TESTED AT BYTES AGAINST THE SEALED RECORD

COMMISSION O32SR — SHAPES-BUILD — 2026-08-15
DETERMINATION ONLY. Nothing is proposed, authored, adopted, constructed, or supplied.
No mechanism is offered. No shape is installed. Where a shape is absent, the absence is
displayed and the sweep that established it is declared.

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

OUTPUT-PATH PROBE, BEFORE ANY WRITE:
`/Users/bgm/MB Work/alpha-program-archive/workspace/STAGE8_BOUNDARY_SHAPES_O32SR_V001.md`
— ABSENT (`ls` exit 1); sidecar `...V001.md.seal.sha256` — ABSENT (`ls` exit 1).
Both probed at commission start, before the first byte was written.

---

## §0 — THE THREE SHAPES ARE IMPORTS. STATED FIRST, BEFORE ANY TEST.

**THE THREE SHAPES TESTED IN THIS ARTIFACT WERE SUPPLIED BY THE COMMISSION FROM
OUTSIDE THIS CORPUS. THEY ARE NOT THE RECORD'S OWN VOCABULARY, THEY CARRY NO
AUTHORITY IN IT, AND NOTHING IN THE RECORD IS OBLIGED TO INSTANTIATE ANY OF THEM.**

They are used here in exactly one way: as three test templates against which the
record's own sealed bytes are read. The record is the authority; the shapes are the
questions. Where the record's words resemble a shape's description without carrying
the shape's structure, this artifact says so and calls it a resemblance, not an
instantiation. §7 IMPORT AUDIT records, for every match reported below, whether the
record's own text CARRIES THE STRUCTURE or only RESEMBLES THE DESCRIPTION.

The three, restated in the commission's own terms so the test is checkable:

```text
SHAPE ONE   FORCED CONVERGENCE.  A quantity measuring the SPREAD of a family, plus a
            sealed condition (positivity / sign) FORCING that quantity to DECREASE,
            yielding a closed structure.
SHAPE TWO   REACHABILITY EDGE.  A boundary defined as the LIMIT of a reachability /
            influence / support RELATION — the boundary is where reach stops — rather
            than by an index, a cardinality, or a materially given surface.
SHAPE THREE MATCHING WITH RESIDUE.  (a) a matching condition governing when two things
            join, and (b) — the deliverable — an OBJECT carrying the disagreement when
            the matching fails: a residue, a defect term, a surface-supported quantity,
            rather than a verdict of obstruction.
```

---

## §1 — SEALS VERIFIED, THIS SESSION, FROM EACH ARTIFACT'S OWN DIRECTORY

`shasum -a 256 -c <NAME>.seal.sha256` run FROM
`/Users/bgm/MB Work/alpha-program-archive/workspace`, before any reliance. 8/8 OK.

```text
OK  STAGE8_INGREDIENT_CENSUS_O17SR_V001.md
OK  STAGE8_INGREDIENT_CENSUS_O17SR_AUDIT_V001.md
OK  STAGE8_GLUING_CANDIDATE_O23SR_V001.md
OK  STAGE8_GLUING_CANDIDATE_O23SR_AUDIT_V001.md
OK  STAGE8_STRATIFICATION_O27SR_V001.md
OK  STAGE8_STRATIFICATION_O27SR_AUDIT_V001.md
OK  STAGE8_RECORDS_PLURAL_O30SR_V001.md
OK  STAGE8_RECORDS_PLURAL_O30SR_AUDIT_V001.md
```

Further seals verified as the sweeps reached them are listed at §6.

---

## §2 — DECLARED SWEEPS AND CUTOFF

```text
SWEEP CUTOFF, DECLARED: 2026-08-15. Tree state at this commission's run.
  ROOT1 (primary)  /Users/bgm/MB Work/alpha-program-archive/workspace
                   6869 files, 1925 *.md (recursive).
  ROOT2            /Users/bgm/Documents/New project/gravity_emergence_evidence_
                   program/alpha_fundamental_record_action_cleanroom_v003
                   7805 files, 2308 *.md (recursive).
  Newest object in ROOT1 at cutoff other than this artifact:
                   STAGE8_ENVIRONMENT_FACTOR_O31SR_V001.md (Aug 15 18:13).
                   Nothing sealed after that instant is inside this determination.

FILE-CLASS EXCLUSION, APPLIED AT THE PATH FILTER, NOT AFTER READING.
  Any file whose BASENAME matches (REGISTER|TRACKER|ROAD|PLAN|CONTINUATION),
  case-insensitive, was removed from every match set and never opened.

INCLUDE SET: *.md (census counts), widened to *.md *.txt *.json *.py on the
  first-pass shape sweeps of §2.1. Counts below are FILE counts, full match-set
  sizes, no head/tail truncation.

"Q-..." tokens: EXPECTED-UNLOCATABLE. Encountered inside quoted sealed text
  (NET's Q-335, the 7A junction's Q-126, Q-290). Carried as opaque labels
  exactly as the sealed artifacts carry them. Never chased, never resolved,
  nothing defaulted.

NO GIT ACTION OF ANY KIND. No existing file edited. Two files written: this
  artifact and its seal sidecar.
```

### §2.1 EVERY PATTERN, VERBATIM

Run as `grep -rIlE` (files) / `grep -rInE` (lines), `-i` where marked CI.

```text
SHAPE ONE
 S1a  dispersion|variance|std deviation|standard deviation|spread of|diameter of|
      oscillation of|scatter of                                          [CI]
      *** WITHDRAWN AS DEFECTIVE, DISCLOSED (see §3.1). ***
 S1a' token-by-token, word-anchored:  (^|[^oi])\bvariance\b | \bdispersion\b |
      \bspread\b | \bdiameter\b | \boscillation\b | \bscatter\b |
      \bdeviation\b | \bwidth\b | \bmodulus of continuity\b | \bsupremum\b |
      \bdistance between\b | \bmetric on\b | \bseminorm\b
 S1b  \b(contraction mapping|contractive|Cauchy sequence|Banach fixed|
      fixed[- ]point theorem|nested (sequence|family|intervals)|
      shrinking (family|sequence))\b
 S1c  \bmonotone (decreas|non-?increas)|monotonically decreas|strictly decreas|
      decreasing in (n|N|k)\b
 S1d  positivity|positive[- ]semi[- ]?definite|non-?negative|nonnegative|
      sign condition|positive majorant|positive definite
 S1e  (forc\w+)[^.]{0,60}(decreas|converg|shrink|contract)|
      (decreas|converg|shrink|contract)\w*[^.]{0,60}forced

SHAPE TWO                                                                 [CI]
 S2a  \breachab | \breach\b | \binfluence\b | domain of dependence |
      domain of influence | causal (past|future) | light[- ]?cone|lightcone |
      \bhorizon\b | causal ball | causal diamond | causal support |
      causal cell | causal schedule | causal feeding|feeding arrow |
      can (be )?reach|cannot reach|reaches
 S2b  where reach stops|edge of reach|limit of reach

SHAPE THREE                                                               [CI]
 S3a  \bresidue | \bresidual | \bdefect | \bmismatch | \bdiscrepanc |
      \bobstruction | \bjump\b | \bdiscontinuit | surface term |
      boundary term | corner term | edge term | anomal | \bsurplus |
      \bremainder | \bexcess\b
 S3b  supported on the (surface|boundary|interface|junction|overlap)
 S3c  matched carrier | identity cell matching | OVERLAPPING, not IDENTICAL |
      fails? to match|match(ing)? fails
 S3d  residue[^.]{0,70}(overlap|junction|interface|mismatch|glu|joint|seam) |
      (overlap|junction|interface|mismatch|glu|joint|seam)[^.]{0,70}residue
 S3e  defect (term|object|class|measure|form|field|density)
```

---

## §3 — SHAPE ONE: FORCED CONVERGENCE — **ABSENT**

### §3.1 A DEFECT IN MY OWN FIRST PATTERN, DISCLOSED BEFORE ANY COUNT IS USED

S1a as first written returned 1188 ROOT1 files and 1137 ROOT2 files — a number
large enough to look like an instantiation. It is an artefact of my pattern.
`variance` inside S1a is unanchored and matches **covariance** and **invariance**,
two of this corpus's commonest words. The count is meaningless and S1a is
withdrawn. S1a' replaces it, token by token and word-anchored. Recorded rather
than silently repaired, because reporting a shape on a contaminated count is the
precise failure this commission exists to avoid committing.

### §3.2 THE SPREAD-QUANTITY CENSUS — S1a', WORD-ANCHORED, FILE COUNTS

```text
TOKEN                        ROOT1   ROOT2   WHAT IT IS AT BYTES
variance (not co-/in-)          40      37   Categorical/functorial VARIANCE
                                             (co- vs contra-), and branch
                                             variance in a redundancy functional.
                                             Not a second moment of a family.
dispersion                       4       3   The PHYSICS sense: "the MASSLESS
                                             dispersion", "a quadratic
                                             dispersion", "non-flat dispersion
                                             bands" — omega(k), not a spread.
spread                          13       9   Hodge "spread component"; "operator-
                                             norm spread ... controlled by a
                                             Lieb-Robinson"; spatial spreading.
                                             A component or a propagation range.
diameter                         6       5   A CELLULATION GEOMETRIC DATUM of ONE
                                             cell ("|C|_4, diameter, aspect
                                             ratio"), used in the SLIVER
                                             direction. Not a family's diameter.
oscillation                     11       0   Oscillatory integrals/channels.
scatter                          1       0   Scattering, physics sense.
deviation                       64      76   Deviation from a stated value.
width                           62      53   Band/strip width.
modulus of continuity            0       0   *** ZERO IN BOTH ROOTS. ***
supremum                        33      25   sup-norms.
distance between                 5       5   
metric on                       14      13   
seminorm                        42      35   Seminorm FAMILIES — the topology
                                             carrier's generators (W-1's CN-1).
```

**FINDING.  NO QUANTITY IN EITHER ROOT MEASURES THE SPREAD OR DISPERSION OF A
FAMILY.** "diameter" is a datum of one cell; "dispersion" is omega(k);
"variance" is functorial variance; "spread" is a decomposition component or a
propagation range. The one family-indexed apparatus present — seminorm families
— is the W-1 topology carrier, and the corpus's own verdict on it is that its
two localization maps are **owed, not held** (O27SR MM-1a, "the half of the
bridge that descends is the half that is missing").

### §3.3 CONVERGENCE IS PRESENT — AND IT IS OF THE WRONG KIND

S1b returns 45 ROOT1 files. Read at bytes, the corpus's convergence apparatus is
GALERKIN APPROXIMATION, sealed as an INPUT, not forced by any condition.
`STAGE8_R2_KAPPA_N_DETERMINATION_S9AD_V001.md` (seal verified OK this session),
§2.2(a) and §2.2(d), verbatim:

```text
(a) THE CARRIER. H_(n,ell) = span{Hermite triples, 0 <= a,b,c < n} tensor
    C^4; NESTED in n; CONVERGES STRONGLY to the continuum carrier
    (equivalently Q_n -> I strongly, the successor-construction requirement
    G-12 restated at PA A1); ell in {1, sqrt2} both frozen and retained.
(d) STRONG CONVERGENCE OF THE FAMILY, SEALED: C_n^(pure) =
    1_(-infinity,0)(Q_n h_0 Q_n) -> P_- strongly, verdict DERIVED.
```

TYPED AGAINST SHAPE ONE, clause by clause:

```text
A FAMILY?                       YES.  {H_(n,ell)}, NESTED in n; {C_n}.
A QUANTITY MEASURING ITS SPREAD? NO.  No functional of the family is displayed.
                                Convergence is stated in the STRONG OPERATOR
                                sense — pointwise on vectors — with no scalar
                                spread quantity anywhere on the page.
FORCED BY A POSITIVITY?          NO.  Both convergences are FROZEN INPUTS
                                ("sealed", "frozen input", "verdict DERIVED"
                                from the sealed stock), not consequences of a
                                sign condition.
A CLOSED STRUCTURE RESULTS?      NO.  What the same section records is the
                                OPPOSITE: "(c) SEALED DIVERGENCES.
                                tr(C_n P C_n) -> infinity ... ||CPC||_2 =
                                +infinity ... ||[C, 1_B]||_2 = +infinity."
                                The family converges; the quantities the
                                program needs DIVERGE on it.
```

### §3.4 WHAT THE POSITIVITY CONDITIONS ACTUALLY DO — FOUR ROLES, NONE OF THEM SHAPE ONE

S1d returns 565 ROOT1 / 549 ROOT2 files. Read at bytes, every role is one of
four, and the commission's question — "does any of them force a spread to
decrease" — is answered NO in each.

```text
ROLE 1  A POSITIVITY DEFICIT THAT BOUNDS ONE SCALAR.  This is the corpus's
        CLOSEST approach to Shape One, and it is quoted in full so the distance
        is visible.  STAGE8_GALERKIN_COMMUTATOR_T12SR_V001.md (seal verified OK
        this session), §4 GC-2, verbatim:
          "STEP 1 (the defect formula). B~ >= 0, so B~^{1/2} exists (spectral),
           and for each j, with D_j := B~^{1/2} W_j B~^{1/2} (Hermitian):
             tr(W_j B~ W_j B~) = tr(D_j^2) = ||D_j||_2^2 >= 0   EXACT.
           With the sealed OP-1 trace form:
             A_n = tr B~^2 - sum_j ||B~^{1/2} W_j B~^{1/2}||_2^2 <= tr B~^2 ."
        and the same artifact's own summary of what it achieved, verbatim:
          "an exact defect formula making the ceiling a POSITIVITY
           DEFICIT statement (GC-2: A_n = tr B~^2 - sum_j ||D_j||_2^2 — the
           question is how much of tr B~^2 the direction field's Hermitian
           squares recapture)".
        WHY IT IS NOT SHAPE ONE, at the artifact's own bytes:
          (i)  A_n IS NOT A SPREAD OF A FAMILY.  It is a commutator mass at
               fixed n — one scalar attached to one operator pair.
          (ii) THE POSITIVITY LOWERS A BOUND, IT DOES NOT DRIVE A LIMIT.  Its
               own scope line, verbatim: "SCOPE (the honesty rail, displayed):
               CONSTANT-grade ONLY.  No exponent moves; the exact-3/2 bulk
               stands; per the audited c-1 discipline this decides NOTHING (no
               sub-3/2 gain of any size is claimed anywhere in this artifact)."
          (iii) NO CLOSED STRUCTURE RESULTS.  Nothing is glued, closed, formed,
               or bounded-as-a-region.  The yield is an inequality.

ROLE 2  *** A POSITIVITY THAT FORBIDS A DECREASE. ***  The corpus's most
        load-bearing positivity runs in the DIRECTION OPPOSITE to Shape One.
        STAGE8_WALL_BOUNDARY_CLOSURE_S9AD_V001.md :176-177 (seal verified OK
        this session), verbatim:
          "VOLUME DIAGONAL x = y, NOT THE SHARP BOUNDARY. SMOOTHING ONLY THE
           BOUNDARY WILL NOT REMOVE A |x-y|^-3 POSITIVE MAJORANT."
        Here positivity is what makes a quantity IMPOSSIBLE to cancel.  It is a
        NON-DECREASE guarantee.  A Shape One reading of this corpus's positivity
        would have the sign pointing the wrong way.

ROLE 3  A MEMBER-LEVEL INEQUALITY.  STAGE8_GALERKIN_COMMUTATOR_T12SR_V001.md,
        verbatim: "16 b_1^2 + 32 b_2^2 >= 0 (subset positivity at the member)".
        A sum of squares is non-negative at one member.  Yields a valuation,
        not a limit.

ROLE 4  AN OPERATOR PROPERTY.  "P_x is positive semidefinite, rank one";
        "The pulled-back Fubini-Study response K is positive semidefinite".
        A property of an object already in hand.
```

### §3.5 THE ONE FORCING LINE THAT WOULD HAVE CLOSED A STRUCTURE — AND IT IS BARRED

S1e's ten ROOT1 files converge on a single object, and it is worth displaying
because it is the closest the corpus comes to "a sign/geometric condition forcing
a closure", and the corpus REFUSES it.
`STAGE8_REQUIRE_G3_CHECK_V001.md` (seal verified OK this session), verbatim:

```text
"the strongest forcing line (cell-local => contractible => phi_H=0) requires the
 forbidden import of Omega_c's continuum-diamond contractibility and is unsealed
 on connection-only bedrock"
```
and, at :136-139:
```text
"To run the forcing I would have to IMPORT Omega_c's diamond contractibility as
 authority — a forbidden SCALE/GR import BY the verifier. A refutation must stand
 on connection-only bedrock; this one cannot."
```
and the verdict at :148: **"NO FORCING FOUND."**

NOTE ON THE WORD.  "Contractible" here is TOPOLOGICAL contractibility of a
diamond — not a metric contraction of a family. The two senses of "contract" are
unrelated, and this artifact does not let the shared syllable stand for a
structure. (Same word, different object; recorded as a resemblance at §7.)

### §3.6 SHAPE ONE — VERDICT

```text
*** ABSENT. ***

REQUIRED BY THE SHAPE            STATE OF RECORD
a family                         PRESENT ({H_(n,ell)} nested in n; {C_n})
a quantity measuring its SPREAD  *** ABSENT.  Displayed exactly: S1a' returns
                                 zero occurrences of "modulus of continuity" in
                                 both roots, and every one of the 40/13/6/4
                                 variance/spread/diameter/dispersion hits is a
                                 different object (§3.2). ***
a condition FORCING it to fall   *** ABSENT.  Positivity in this corpus bounds a
                                 scalar (ROLE 1), forbids a cancellation
                                 (ROLE 2), values a member (ROLE 3), or types an
                                 operator (ROLE 4).  None acts on a spread. ***
a closed structure resulting     *** ABSENT.  The corpus's own convergences
                                 deliver DIVERGENCES on the quantities of
                                 interest (§3.3(c)), and its one forcing line is
                                 refused as an illegal import (§3.5). ***

THE POSITIVITY CONDITIONS THE RECORD CARRIES SERVE OTHER PURPOSES.  That is the
commission's own alternative, and it is the answer.
```

---

## §4 — SHAPE TWO: REACHABILITY EDGE — **ABSENT**
### (vocabulary richly present; the boundary-defining RELATION is not)

The commission's instruction governs this section: *the distinction between a
reachability RELATION with a boundary at its limit, and a LABEL on an object
defined some other way, is the whole of the test; do not let the vocabulary
decide it.* The vocabulary is abundant. Each carrier is opened and typed.

### §4.1 THE VOCABULARY CENSUS — S2a/S2b, FILE COUNTS

```text
TOKEN                          ROOT1  ROOT2
reachab                          157    132
reach (bare)                     298    232
influence                         98     95
domain of dependence               0      0   *** ZERO IN BOTH ROOTS ***
domain of influence                0      0   *** ZERO IN BOTH ROOTS ***
causal past | causal future        1      1
light-cone / lightcone            27     28
horizon                           10      7
causal ball                       10      5
causal diamond                    76     64
causal support                    61     66
causal cell                       80     81
causal schedule                    4      3
causal feeding | feeding arrow     3      1
can reach|cannot reach|reaches   366    315
"where reach stops|edge of reach|limit of reach"
                                   1      0   — and the ONE ROOT1 hit is THIS
                                              ARTIFACT's own §0 restatement of
                                              the imported shape. The corpus
                                              itself: ZERO in both roots.
```

The two tokens that name a reachability REGION in the standard way — *domain of
dependence*, *domain of influence* — are **absent from both roots entirely**.

### §4.2 CARRIER 1 — THE CAUSAL CELL. THE CELL IS **ASSIGNED**, NOT REACHED

The corpus's one cell-yielding clause, read at its own bytes this session from
`CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md` (seal verified OK this session by
`shasum -a 256 -c CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.seal.sha256` from the
artifact's own directory), verbatim and whole:

```text
For every primitive record-forming incidence `c`, the complete microscopic
parent assigns one Lorentz-covariant causal cell `Omega_c` and one interaction
density `L_c` such that

support(L_c) is contained in Omega_c.
```

TYPED AGAINST SHAPE TWO:

```text
IS THERE A RELATION?      YES, ONE: containment, support(L_c) subset Omega_c.
WHICH WAY DOES IT RUN?    *** THE WRONG WAY FOR THE SHAPE. ***  The cell comes
                          FIRST, by ASSIGNMENT from the parent; the support is
                          then CONSTRAINED to fit inside it.  Shape Two needs
                          the reverse: the region computed AS the extent of
                          something's reach.  Here nothing is computed; a cell
                          is handed over and a density is required to fit.
WHO DEFINES THE BOUNDARY? "the complete microscopic parent" — an ASSIGNING
                          AGENT.  And that agent is the census's U-1, unpaired
                          at the root: the same artifact's own frozen status
                          block reads "complete_causal_parent_derived = false".
IS Omega_c's BOUNDARY THE
LIMIT OF ANY REACH?       NOT OF RECORD.  No clause anywhere derives Omega_c's
                          extent from what c can influence.  Its own falsifier
                          section says the opposite is still owed: "Failure to
                          derive a unique causal cell, a complete parent, or a
                          durable outgoing sector blocks downstream promotion."
```

THE NEAREST INFLUENCE-FLAVOURED CLAUSES IN THE SAME FILE, quoted so nothing is
suppressed, and typed:

```text
"Once the future boundary has crossed the closure face of `Omega_c`, the same
 primitive incidence is absent from the active generator."
   -> A CONSEQUENCE about an already-given face.  The face is not derived here;
      it is the boundary of the assigned cell, and this sentence says what stops
      happening after it is crossed.  The reach follows the boundary; the
      boundary does not follow the reach.

"a later primitive cell acts nontrivially on an earlier record factor"
"causal linear extensions disagree on spacelike-separated primitive events"
   -> Two of the SEVEN FALSIFIERS.  Both are genuine influence conditions.  Both
      YIELD A TRUTH VALUE about a proposed parent (census type CONSTRAINT).
      Neither defines a region, a boundary, or an edge.
```

**VERDICT ON CARRIER 1: the words "causal cell" and "causal support" are LABELS
on an assigned region and a containment test. No reachability relation defines
the boundary.**

### §4.3 CARRIER 2 — THE CAUSAL BALL. A **MANDATED FORMULA**, AND ITS BOUNDARY IS RULED OUT

`STAGE8_R2_KAPPA_N_DETERMINATION_S9AD_V001.md` (seal verified OK this session),
§2.1, verbatim:

```text
P  (the record projector): the SHARP causal-ball projector. ...
   P = multiplication by 1_(|x| <= r(t)) (spinor-diagonal); sharp
   consumption is MANDATED (D6', AR-2). r(t) = min(t, 1-t).
```

THIS IS THE CORPUS'S CLOSEST SURFACE TO SHAPE TWO, and it fails the test twice
over, both times at the record's own bytes:

```text
(a) THE RADIUS IS A FROZEN INPUT, NOT A DERIVED REACH.  r(t) = min(t, 1-t) is
    DISPLAYED as a formula and its consumption is "MANDATED (D6', AR-2)".  No
    clause of record derives r(t) as the extent of any influence, and none is
    cited.  The sphere |x| = r(t) is a materially given surface with a formula
    attached — the commission's second alternative, exactly.

(b) THE RECORD EXPRESSLY DENIES THAT THIS BOUNDARY IS WHERE THE ACTION IS.
    STAGE8_WALL_BOUNDARY_CLOSURE_S9AD_V001.md :176-177 (seal verified OK this
    session), verbatim:
      "VOLUME DIAGONAL x = y, NOT THE SHARP BOUNDARY. SMOOTHING ONLY THE
       BOUNDARY WILL NOT REMOVE A |x-y|^-3 POSITIVE MAJORANT."
    The corpus's adopted locus ruling moves the load OFF the ball's boundary and
    onto the volume diagonal.  A shape that reads this surface as a reachability
    edge would be reading the one surface the record has ruled not load-bearing.
```

### §4.4 CARRIER 3 — THE CAUSAL FEEDING ARROW. A **DIRECTION LABEL**, THREE FILES

S2a returns three ROOT1 files for the feeding arrow, and all three carry one
clause. `STAGE8_TASK4A_NETWORK_SOURCING_LAW_ADOPTION_PROPOSAL_CODEX_LANE2_V001.md`
(seal verified OK this session) :221, verbatim:

```text
network edge      causal feeding arrow, not E_post endpoint charge
```

and `STAGE8_CONTRACTIBILITY_SCOPE_O26SR_V001.md` (seal verified OK this session)
:654 and :1143, verbatim:

```text
"The joiner of record types its own edge as 'causal feeding arrow, not
 E_post endpoint charge'"
"The only joiner of record joins in the SOURCING direction — its edge is typed
 'causal feeding arrow, not E_post endpoint charge' — and never touches the
 cells."
```

TYPED. The clause is a DISAMBIGUATION of what an edge of `Adj_2` carries: a
sourcing direction rather than an endpoint charge. It is a label on an arrow of
a two-node adjacency matrix that already exists. It defines no region, bounds
nothing, and — at the corpus's own words — **"never touches the cells."**

### §4.5 THE ONE GENUINE LIMIT-OF-INFLUENCE QUANTITY IN THE CORPUS — AND WHAT IT BOUNDS

Reported prominently because it is the strongest thing the sweeps found, and
because suppressing it would hide the sweep's one real result.
`COMPLETE_QSPEC_OPEN_RECORD_BLOCK_TRANSFER_MAP_SPEC_V001.md` (seal verified OK
this session), Liveness rule, :43-48, verbatim and whole:

```text
For every record `r`, compute:

last(r) = maximum event index whose unitary support contains r.

Closing `r` before `last(r)` is invalid and must be rejected before
execution. Closing at or after `last(r)` is exact because all later
unitaries act as identity on `H_r`.
```

WHAT IS GENUINELY HERE, granted in full:

```text
A RELATION:  "whose unitary support CONTAINS r" — a support/influence relation
             between an event's unitary and a record.
A LIMIT OF IT: last(r) = the MAXIMUM index at which anything still acts on r.
             This is, in substance, the point past which r is beyond reach —
             and the artifact says exactly why: "all later unitaries act as
             identity on H_r."
```

**AND WHY IT IS STILL NOT SHAPE TWO — three reasons, each at bytes:**

```text
(i)   THE LIMIT IS NOT CALLED A BOUNDARY AND NO BOUNDARY IS DEFINED BY IT.
      last(r) governs the VALIDITY OF AN OPERATION (CLOSE).  It is a scheduling
      admissibility condition.  Nothing of record forms a region, a face, a
      surface, or an edge from it.

(ii)  *** THE THING THE ARTIFACT DOES CALL A BOUNDARY IS AN INDEX. ***  The same
      file's opening, verbatim: "At event boundary `e`, let `A_e` be the ordered
      set of records that have opened and have not passed their last incident
      unitary."  `e` is an EVENT INDEX in a finite schedule, and `A_e` is
      evaluated AT it.  The index defines the boundary; the boundary does not
      define the index.  This is precisely the commission's named alternative —
      a boundary given by an index — and the record instantiates the
      alternative, not the shape.

(iii) THE OBJECT IS A SPECIFICATION WITH ITS THEOREM OWED.  Its own next section,
      verbatim: "Theorem obligation.  Freeze an explicit induction proving that
      the event-driven block operator equals the partial trace of the full global
      relative-history operator at every valid event boundary."  The rule is
      stated and sealed; the theorem that would make it sound is DEMANDED.
```

### §4.6 THE REACHABILITY STRUCTURE THE CORPUS NAMES — AND COUNTS AS MISSING

The nearest thing in either root to a reachability relation over cells is named
once, as an ABSENCE, and its possibility is judged NO.
`STAGE8_REQUIRE_G1_COLD_V001.md` (seal verified OK this session) :205-215,
verbatim and whole:

```text
MISSING CONNECTION-ONLY SUB-ESTIMATE (would suffice, if it existed):
  a refinement-INVARIANT, per-cell (non-4-volume) OPERATOR-NORM activity bound
      |Phi_gamma(a)| <= eta^{|gamma|}
  on a purely COMBINATORIAL cell-adjacency connectivity, together with an
  operator-norm (not spatial-Schatten-2) decay of the connected write-generator
  covariance in COMBINATORIAL cell-separation — equivalently, UNIFORM (not
  power-law) clustering of the prepared state.
```

with the same artifact's answer on what the sealed realization actually carries,
verbatim:

```text
"'Decay of the connected covariance in cell-separation' is thus a power law in a
 METRIC DISTANCE, and the object is controlled in the spatial Schatten-2
 (Hilbert-Schmidt) norm ... In the sealed realization NEITHER is
 connection-only ... The required rate is a SCALE/VOLUME/METRIC statement, not a
 connection-only one."
```

and its cold judgment on whether the combinatorial version is even possible,
verbatim: **"NO."**

TWO THINGS FOLLOW, AND BOTH ARE DISPLAYED WITHOUT INFERENCE:

```text
(1) The combinatorial cell-adjacency CONNECTIVITY — the one object in either
    root that would be a reachability relation ON CELLS — is named inside a
    MISSING sub-estimate.  And the graph it would run on is the census's exact
    absence: "the inter-cell incidence set is EMPTY"
    (STAGE8_INGREDIENT_CENSUS_O17SR_V001.md §2.3, seal verified OK, quoting
    STAGE8_GLUED_TOPOLOGY_HUNT_V001.md G-3).
(2) EVEN HAD IT EXISTED, IT IS NOT SHAPE TWO.  Its office is CLUSTER
    SUMMABILITY — a decay condition certifying an expansion.  It defines no
    boundary.  Shape Two would additionally require a boundary set as the limit
    of that connectivity, and no clause of record poses one.
```

### §4.7 SHAPE TWO — VERDICT

```text
*** ABSENT. ***

The corpus's causal vocabulary is dense and every occurrence of it is a LABEL ON
AN OBJECT DEFINED SOME OTHER WAY:

  causal cell        a region ASSIGNED by an underived parent; the only relation
                     attached is a CONTAINMENT TEST running the wrong way.
  causal support     that containment test, and its seven falsifiers, which
                     yield TRUTH VALUES about a proposed parent.
  causal ball        a MANDATED indicator 1_(|x| <= r(t)) with r(t) a frozen
                     formula — and the record's adopted ruling moves the load
                     OFF its boundary and onto the volume diagonal.
  causal feeding     a direction disambiguation on an edge of a 2x2 adjacency
    arrow            matrix, which "never touches the cells".
  causal schedule    a finite ordered list of EVENT INDICES.

ONE GENUINE LIMIT-OF-INFLUENCE QUANTITY EXISTS — last(r), the maximum event
index still acting on r — AND IT BOUNDS AN OPERATION, NOT A REGION.  At the same
site, the thing the record calls a "boundary" is an EVENT INDEX.

EXACT ABSENCES DISPLAYED:
  "domain of dependence"                 0 files, BOTH roots.
  "domain of influence"                  0 files, BOTH roots.
  "where reach stops|edge of reach|limit of reach"
                                         0 files in the corpus, BOTH roots.
  a boundary defined as the limit of a reachability relation
                                         NOT LOCATED, either root, under S2a/S2b.
```

---

## §5 — SHAPE THREE: MATCHING WITH RESIDUE — **PARTIALLY INSTANTIATED**
### (a) MATCHING CONDITIONS: PRESENT, TWO OF THEM.
### (b) THE RESIDUE: THE MISMATCH IS GIVEN A **CONTENT** — BUT NOT AN OBJECT ON THE SURFACE.

This is the commission's priority deliverable and the only shape of the three
that the record part-carries. It is reported in two parts, as asked.

### §5.1 PART (a) — WHAT MUST MATCH, AND WHAT "MATCHED" MEANS AT BYTES

**MATCHING CONDITION 1 — THE JOINING RULE'S MATCHED CARRIERS.**
`STAGE8_TASK4A_NETWORK_SOURCING_LAW_ADOPTION_PROPOSAL_CODEX_LANE2_V001.md`
(NET V001, seal verified OK this session), row `N` at :242, quoted WHOLE — all
five columns, including the void column, because the void column is part (b)'s
answer for this rule:

```text
| `N` — network incidence | On matched carriers, use the reciprocal two-node
  swap, no self-edge, identity cell matching, and one-tier delay. | Directed
  graph; weighted edge; self-sourcing; a nontrivial cell permutation/intertwiner;
  same-tier/retroactive feeding. | The sender/receiver assignment and causal
  delivery rule. | Voids if reciprocity or E_post orientation fails, a cell
  matching is silently selected outside the matched-carrier class, or output
  feeds the tier that produced it. |
```

and the same artifact's §4.2, :332-340, verbatim:

```text
For a matched-carrier edge `a->b`, let

tau_(ba):ell^1_a -> ell^1_b

be the declared identity label match. On a general reciprocal edge family, the
proposal would require isometric intertwiners with

tau_(ab)=Theta_a tau_(ba)^* Theta_b.                (NS-8)
```

**WHAT MUST MATCH, ESTABLISHED AT BYTES:**

```text
THE MATCHED THING   THE CARRIERS.  Not the cells' geometry, not their boundaries,
                    not any induced structure on a shared face.  The transport
                    across the edge is tau_(ba): ell^1_a -> ell^1_b, and it is
                    "the declared IDENTITY LABEL MATCH."
WHAT "MATCHED"      A LABEL IDENTITY, DECLARED.  The carriers are in the matched
MEANS               class when their labels are identical, so that transport is
                    the identity map.  Nothing is compared, computed, or
                    restricted-and-checked; the identity is DECLARED.
THE CORPUS'S OWN    STAGE8_CONTRACTIBILITY_SCOPE_O26SR_V001.md (seal verified OK
TYPING OF IT        this session), verbatim: matched carriers are
                    "a domain restriction, silent on multiplicity".
                    A DOMAIN RESTRICTION — it says which inputs the rule accepts.
                    It is NOT an agreement condition evaluated on a shared
                    surface.
THE GENERAL CASE    NS-8's isometric intertwiners are the general-family
                    condition — and NET :347, verbatim: "V001 instantiates only
                    the matched two-node class, so NO PERMUTATION OR INTERTWINER
                    IS SELECTED."  Stated in the subjunctive ("WOULD require"),
                    never displayed.
```

**MATCHING CONDITION 2 — R9 / JOINT LANDING AT A CELL.**
This is the corpus's *other* matching condition and it is the one closest in
form to Shape Three, because it is an agreement condition at a junction.
`STAGE8_7A_JUNCTION_U1_SHARED_CORE_DARIO_V001.md` (seal verified OK this
session), §2.5, verbatim and whole:

```text
Let e be a cell of the record complex N and [e] its presentation class.

  (A)  Phitilde_N(.)(delta_e) : Sigma_N^(2),Ward -> C        the Ward-symbol map at e
  (B)  beta                    : -> R_(>0)                    the length normalization
                                                              for the same cell,
                                                              R = beta c Delta tau

JOINT LANDING at e holds iff there is a SINGLE declared cross-sector unit u(e),
routed through the one R4 seam, such that:

  J1  DECLARATION IS SHARED. ...
  J2  PRESENTATION-INVARIANT.  u(e) depends only on [e] ...
  J3  NOT IMPLICITLY ONE, AND DETERMINATE. ...
  J4  ONE OBJECT, NOT TWO RETURNS.  (A) and (B) are compared as one associated
      object on e, per R9-V002's repair — never as two independently formed
      returns ...
```

**THIS IS A GENUINE AGREEMENT CONDITION**: two maps at one locus join exactly
when an induced quantity — the cross-sector unit u(e) — is a SINGLE shared
object there. That is the first half of Shape Three, carried by the record's own
sealed text. It is reported as such.

### §5.2 PART (b) — WHAT HAPPENS WHEN THE MATCHING FAILS
### *** THE COMMISSION'S PRIORITY QUESTION, ANSWERED IN THREE FINDINGS ***

**FINDING B-1 — FOR THE JOINING RULE, MISMATCH IS A VOID. A VERDICT.**
NET row `N`'s fifth column, quoted again for this purpose, verbatim: *"Voids if
reciprocity or E_post orientation fails, a cell matching is silently selected
outside the matched-carrier class, or output feeds the tier that produced it."*
A failed match VOIDS THE RULE. No term is produced, no object is formed, nothing
is carried on the edge. **OBSTRUCTION, NOT RESIDUE.**

**FINDING B-2 — FOR R9, MISMATCH KILLS, AND THE RECORD TYPES IT SO IN ITS OWN
WORDS.** `STAGE8_7A_JUNCTION_U1_SHARED_CORE_DARIO_V001.md`, immediately after
J1-J4, verbatim and whole:

```text
TYPING.  Joint landing is a FALSIFIER, not a constructor.  Failure of J1–J4 kills;
satisfaction of J1–J4 builds neither map.  Neither map's residue is discharged by the
other's (both residues stand, per the OVERLAPPING determination).
```

with the discipline governing whether the test may be run at all, quoted at the
same artifact §2.4, verbatim:

```text
"R9 is a falsifier, not a constructor"
"keep R9 PENDING until one common physical cell exists"
"| A8/R9 | one common physical cell on which both typed returns exist
  independently | no common cell is presently formed |"
```

**THIS IS THE DECISIVE SENTENCE OF THE WHOLE SHAPE-THREE TEST, AND IT IS THE
RECORD'S OWN, NOT MINE: "a FALSIFIER, not a constructor."** A falsifier yields a
truth value. Shape Three requires the failed matching to yield an OBJECT. The
record types its matching condition into the census's CONSTRAINT class and says
explicitly that satisfying it *"builds neither map."*

**FINDING B-3 — AND YET THE MISMATCH IS GIVEN A CONTENT. THE RECORD DOES MORE
THAN RETURN A VERDICT.**
This is the part the commission most wanted, and the answer is not the expected
one in either direction. `STAGE8_TASK6_JII_BETA_IDENTIFICATION_DARIO_V001.md`
(seal verified OK this session), §J2.3, quoted WHOLE:

```text
SHARED CORE (sealed on both sides):
  THE CROSS-SECTOR JUNCTION. The record's internal structure is fully pinned,
  unit-normalized and dimensionless; no sealed rule carries it across to an
  external, dimensional, physically comparable carrier; and any lawful crossing
  must DECLARE a cross-sector unit rather than set one implicitly to 1.

(A)'s RESIDUE — not supplied by (B):
  the sector/type crossing proper: a rule eating an order-two Ward symbol class
  with a cotangent variable and quantization data and producing finite cochain
  coefficients; plus presentation independence, contact-ideal annihilation,
  orientation covariance, continuity. None of this is a spacetime-length question.

(B)'s RESIDUE — not supplied by (A):
  the dimensional normalization to SPACETIME geometry: beta in R = beta c Delta tau
  against Lorentzian causal-diamond geometry of the same cell; plus the two arms
  already closed by theorem (the unbounded bilocal lift; the amplitude-poverty of
  unit-modulus structure). None of this is a symbol-evaluation question.
```

```text
**`IDENTIFICATION = OVERLAPPING`.** One junction, two maps, two residues.
```

**"ONE JUNCTION, TWO MAPS, TWO RESIDUES."** The record, at a junction it has
determined to be OVERLAPPING rather than IDENTICAL, does not stop at the
verdict: it decomposes the disagreement and NAMES BOTH HALVES, itemized. So the
commission's question — *is a mismatch treated as an obstruction, or is it given
an object?* — has a third answer at bytes, and it must be stated exactly:

```text
THE MISMATCH IS GIVEN A CONTENT.  It is not merely "they do not match."  It is
"(A) has this, which (B) does not supply; (B) has that, which (A) does not
supply", each side enumerated clause by clause.

BUT THE CONTENT IS OF THE WRONG TYPE FOR SHAPE THREE, and the difference is
structural, not verbal:

  SHAPE THREE WANTS   an object SUPPORTED ON THE JOINING SURFACE — a defect term,
                      a surface-supported quantity — which is what the
                      disagreement IS, and which enters the theory as a term.
  THE RECORD CARRIES  TWO LISTS OF UNSUPPLIED OBLIGATIONS.  Each "residue" is
                      the set-theoretic complement of one side's demands in the
                      other's: what A owes that B does not discharge, and
                      conversely.  It has no support, no locus, no carrier, and
                      no place in any expression.  It is a bookkeeping remainder
                      of two requirement sets, not a quantity on a surface.

AND THE RECORD ITSELF SAYS THE RESIDUES DO NOTHING: "Neither map's residue is
discharged by the other's (both residues stand, per the OVERLAPPING
determination)."  They STAND.  They are not consumed, not transported, not
integrated, and not made into a term.
```

### §5.3 THE NEAR-END CELL, AND WHERE ITS MISMATCH GOES

The commission names it: one near-end cell described as "overlapping, not
identical" with another, treated as a reason a bridge fails. Located and typed.
`STAGE8_STRATIFICATION_O27SR_V001.md` (seal verified OK this session) §3.2
B2-iv, quoting W2 §5 OWED-2(2b), verbatim:

```text
"an identification of `(JD-3)`'s named oriented k-cell with the admissibility
 spec's record cell, currently OVERLAPPING, not IDENTICAL; no common cell
 formed; R9-JII PENDING, run_state NOT_RUN. [H-2]"
```

and O27SR's own consequence sentence, verbatim:

```text
"*** THE BRIDGE FAILS BEFORE IT LEAVES THE CELL.  W-2's cell and the record's
cell are not the same object of record. ***"
```

TYPED AGAINST SHAPE THREE, exactly:

```text
IS THE MISMATCH GIVEN AN OBJECT?    NO, AT THIS SITE.  The disposition is
                                    threefold and every part is a status:
                                    "no common cell formed" (an absence),
                                    "R9-JII PENDING" (a pending test),
                                    "run_state NOT_RUN" (an unrun test).
IS IT TREATED AS AN OBSTRUCTION?    YES.  O27SR grades it as a failed bridge
                                    candidate; the census records
                                    "common cell formed = false".
DOES ANYTHING SUPPORT A TERM ON     *** NO. ***  See §5.4's exact absence.
THE OVERLAP OF THE TWO CELLS?
```

Note carefully, because the two sites are linked and must not be conflated: the
cell-level mismatch (H-2) is stated *pointing at* R9-JII, and R9-JII is the
determination that returned OVERLAPPING with two residues (§5.2 B-3). So the
record's own route from this mismatch leads to a content — and the content is
the pair of obligation lists, not a quantity on the cells' overlap.

### §5.4 THE EXACT ABSENCE, DISPLAYED

```text
SWEEP S3b, run recursively over BOTH roots, case-insensitive, path-filtered:
  supported on the (surface|boundary|interface|junction|overlap)
RESULT:  0 files in ROOT1.  0 files in ROOT2.  *** ZERO IN BOTH ROOTS. ***

SWEEP S3c, "fails? to match|match(ing)? fails", BOTH roots:
  ROOT1 returns 2 files.  One is THIS ARTIFACT's own §0 restatement of the
  imported shape.  The other is STAGE8_TASK6_B_V007_REPIN_DARIO_V001.md:314,
  about a FILENAME self-check — "The self-check failing was the guard working,
  not a defect" — and is not about joining anything.
  *** THE CORPUS CONTAINS NO CLAUSE ABOUT A JOINING MATCH FAILING. ***
  What it contains instead is a VOID clause (§5.2 B-1) and a KILL typing
  (§5.2 B-2).

SWEEP S3e, "defect (term|object|class|measure|form|field|density)":
  Every hit is one of exactly two things, checked line by line:
   (i)  GC-2's "defect formula" — A_n = tr B~^2 - sum_j ||D_j||_2^2 — an
        operator-trace identity at fixed n (§3.4 ROLE 1).  Not at a surface,
        not from a mismatch, and by its own words deciding NOTHING.
   (ii) "defect class" in the PROCESS sense — a class of DOCUMENT defects the
        program's audits hunt ("the sweep's own listed defect class", "Every
        hunted defect class came back ...").  Paperwork, not physics.
```

### §5.5 THE ONE SURFACE-SUPPORTED REMAINDER IN THE CORPUS — AND WHY IT IS NOT THIS

Reported because it is the only thing in either root shaped like a
surface-supported residue, and suppressing it would hide the sweep's result.
`STAGE8_G1_KERNEL_CERTIFICATE_V001.md` (seal verified OK this session) OBL-D,
quoting V011 :1397-1412, verbatim:

```text
"The response map must commute with pullback to a common refinement, and the
 intensive quadratic coefficient must be invariant under each elementary
 refinement up to a boundary term whose ratio to four-volume tends to zero."
```

TYPED:

```text
IS IT SUPPORTED ON A SURFACE?   YES, in name: it is a "boundary term".
IS IT A RESIDUE OF A MATCHING   *** NO. ***  It is the error term of a
FAILURE BETWEEN TWO JOINED          REFINEMENT-INVARIANCE comparison — one
REGIONS?                            complex against its own refinement — not two
                                    regions joined across a shared surface.
IS IT AN OBJECT THE THEORY      *** NO — THE OPPOSITE. ***  The clause REQUIRES
CARRIES?                            it to be asymptotically negligible: "whose
                                    ratio to four-volume tends to zero."  Shape
                                    Three's residue is a term the theory KEEPS.
                                    This is a term the condition demands
                                    VANISH.
STATUS OF RECORD                Its own status flags, same span, verbatim:
                                "cellulation_independence_proved = false".
```

### §5.6 SHAPE THREE — VERDICT

```text
*** PARTIALLY INSTANTIATED. ***

PART (a) MATCHING CONDITION — *** PRESENT, TWO OF THEM, BOTH SEALED. ***
  1. NET row `N`: "On matched carriers ... identity cell matching".  WHAT
     MATCHES: the CARRIERS, by a DECLARED IDENTITY LABEL MATCH (tau_(ba) is
     "the declared identity label match").  The record's own typing of it:
     "a domain restriction, silent on multiplicity."  It restricts the rule's
     domain; it does not test agreement of an induced structure on a shared
     surface.
  2. R9 / JOINT LANDING at e (J1-J4): two maps join at one cell iff a SINGLE
     declared cross-sector unit u(e) exists and is shared, presentation-
     invariant, determinate, and one object rather than two returns.  THIS IS A
     GENUINE AGREEMENT CONDITION AT A JUNCTION.

PART (b) THE RESIDUE — *** ABSENT AS AN OBJECT; PRESENT AS AN ITEMIZED
CONTENT; THE RECORD'S OWN TYPING IS "FALSIFIER". ***
  MISMATCH AT THE JOINING RULE  ->  "Voids."                     A VERDICT.
  MISMATCH AT R9                ->  "Failure of J1-J4 kills."    A VERDICT, and
      the record types the whole condition in its own words: "Joint landing is a
      FALSIFIER, not a constructor ... satisfaction of J1-J4 builds neither map."
  MISMATCH AT THE NEAR-END CELL ->  "no common cell formed; R9-JII PENDING,
      run_state NOT_RUN."                                        A STATUS.
  AND YET, AT J-II              ->  "One junction, two maps, TWO RESIDUES", each
      residue itemized clause by clause.  THE MISMATCH IS GIVEN A CONTENT.

  SO THE COMMISSION'S EITHER/OR IS ANSWERED BOTH WAYS, AND THE DIVISION IS
  STRUCTURAL:  the record assigns the mismatch a CONTENT — two enumerated lists
  of what each side does not supply the other — and assigns it NO OBJECT: no
  support, no locus, no carrier, no term in any expression, and by its own
  sentence the residues merely "stand", undischarged.

  A LIST OF UNMET OBLIGATIONS IS NOT A DEFECT TERM.  The corpus has the noun and
  not the structure, and "supported on the surface/boundary/interface/junction/
  overlap" returns ZERO FILES IN BOTH ROOTS.
```

---

## §6 — SEALS VERIFIED THIS SESSION (FULL LIST)

Each verified with `shasum -a 256 -c <sidecar>` executed FROM THE ARTIFACT'S OWN
DIRECTORY, before any reliance on its content. **28/28 OK. No mismatch. Nothing
consumed unverified.** Both sidecar naming conventions were probed
(`NAME.md.seal.sha256` and `NAME.seal.sha256`).

```text
COMMISSIONED GROUND
OK  STAGE8_INGREDIENT_CENSUS_O17SR_V001.md
OK  STAGE8_INGREDIENT_CENSUS_O17SR_AUDIT_V001.md
OK  STAGE8_GLUING_CANDIDATE_O23SR_V001.md
OK  STAGE8_GLUING_CANDIDATE_O23SR_AUDIT_V001.md
OK  STAGE8_STRATIFICATION_O27SR_V001.md
OK  STAGE8_STRATIFICATION_O27SR_AUDIT_V001.md
OK  STAGE8_RECORDS_PLURAL_O30SR_V001.md
OK  STAGE8_RECORDS_PLURAL_O30SR_AUDIT_V001.md

REACHED BY THE DECLARED SWEEPS, QUOTED ABOVE
OK  CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md        (sidecar: .seal.sha256 form)
OK  COMPLETE_QSPEC_OPEN_RECORD_BLOCK_TRANSFER_MAP_SPEC_V001.md
OK  STAGE8_TASK4A_NETWORK_SOURCING_LAW_ADOPTION_PROPOSAL_CODEX_LANE2_V001.md
OK  STAGE8_CONTRACTIBILITY_SCOPE_O26SR_V001.md
OK  STAGE8_7A_JUNCTION_U1_SHARED_CORE_DARIO_V001.md
OK  STAGE8_TASK6_JII_BETA_IDENTIFICATION_DARIO_V001.md
OK  STAGE8_GALERKIN_COMMUTATOR_T12SR_V001.md
OK  STAGE8_R2_KAPPA_N_DETERMINATION_S9AD_V001.md
OK  STAGE8_WALL_BOUNDARY_CLOSURE_S9AD_V001.md
OK  STAGE8_REQUIRE_G3_CHECK_V001.md
OK  STAGE8_REQUIRE_G1_COLD_V001.md
OK  STAGE8_G1_KERNEL_CERTIFICATE_V001.md

REACHED, SEAL-VERIFIED, INSPECTED, AND DISPOSED WITHOUT BEING QUOTED AS GROUND
OK  STAGE8_OVERLAP_LAW_T11SR_V001.md          (see F-3)
OK  STAGE8_OVERLAP_LAW_T11SR_AUDIT_V001.md
OK  STAGE8_JOIN_ADMISSIBILITY_O28SR_V001.md
OK  STAGE8_REFINEMENT_AFTER_JOIN_O29SR_V001.md
OK  STAGE8_7A_HANDOFF_PACKAGE_V001.md
OK  STAGE8_REQUIRE_CLUSTER_CHECK_V001.md
OK  STAGE8_REQUIRE_BUILD_CLUSTER_SUMMABILITY_V001.md
OK  STAGE8_COMPLETION_MAP_T17SR_V001.md
```

---

## §7 — IMPORT AUDIT

### §7.1 THE THREE SHAPES ARE IMPORTS — STATED PLAINLY, AS THE COMMISSION REQUIRES

```text
*** THE THREE SHAPES TESTED IN THIS ARTIFACT — FORCED CONVERGENCE, REACHABILITY
    EDGE, MATCHING WITH RESIDUE — WERE SUPPLIED BY THE COMMISSION FROM OUTSIDE
    THIS CORPUS. THEY ARE NOT THE RECORD'S VOCABULARY, THEY ARE NOT DERIVED FROM
    IT, AND THEY CARRY NO AUTHORITY IN IT. ***

They entered this artifact as TEST TEMPLATES ONLY. Nothing about them was
adopted, installed, proposed, or recommended. No sentence below or above asserts
that the record OUGHT to instantiate any of them, that a shape is a defect when
absent, or that any absence should be filled. Two of the three came back ABSENT
and one PARTIAL, and that is reported as a fact about the record, not a
shortfall of it.

VOCABULARY DISCIPLINE: the shape names, and the words "spread", "reachability
edge", "residue-as-object", "surface-supported", are MINE (the commission's).
Where they appear in this artifact's own prose they label a TEST, never a corpus
object. Every corpus object is named in the corpus's own words, quoted at bytes
and attributed to a seal-verified file.

NOTHING WAS IMPORTED FROM OUTSIDE THE TWO DECLARED ROOTS. No external
mathematics, no textbook theorem, no physical constant, no measured value, no
imported GR, no scale. Every operator identity, every exponent, every degree,
every H^1 value appearing above is a QUOTATION from a corpus artifact at cited
bytes. This commission computed nothing and derived nothing.
```

### §7.2 STRUCTURE OR RESEMBLANCE — EVERY MATCH REPORTED, GRADED

The commission requires this table. **CARRIES = the record's own text carries the
shape's structure. RESEMBLES = the record's text resembles the shape's
description without carrying its structure.**

```text
#     THE RECORD'S OBJECT                        GRADE       WHY
------------------------------------------------------------------------------
SHAPE ONE
1.1   GC-2 positivity halving + defect formula   RESEMBLES   Positivity does force
      A_n = tr B~^2 - sum_j ||D_j||_2^2                      a decrease — of ONE
                                                             SCALAR BOUND at fixed
                                                             n. No family, no
                                                             spread functional, no
                                                             closed structure; its
                                                             own words: "decides
                                                             NOTHING".
1.2   Nested carrier family; Q_n -> I strongly;  RESEMBLES   A real convergent
      C_n^(pure) -> P_- strongly                             family — but sealed as
                                                             a FROZEN INPUT, not
                                                             forced by any sign
                                                             condition, and the
                                                             same page records the
                                                             quantities of interest
                                                             DIVERGING on it.
1.3   The |x-y|^-3 POSITIVE MAJORANT             RESEMBLES   Positivity present and
                                                 (INVERTED)  load-bearing — in the
                                                             OPPOSITE role: it
                                                             FORBIDS a cancellation.
1.4   "cell-local => contractible => phi_H=0"    RESEMBLES   Shared syllable only.
                                                 (LEXICAL)   Topological
                                                             contractibility, not
                                                             metric contraction —
                                                             and BARRED as an
                                                             illegal import:
                                                             "NO FORCING FOUND."
SHAPE TWO
2.1   causal cell Omega_c; support(L_c) c Omega_c RESEMBLES  A containment TEST on
                                                             an ASSIGNED region.
                                                             Relation runs cell ->
                                                             support, the reverse of
                                                             the shape.
2.2   P = 1_(|x| <= r(t)), r(t) = min(t,1-t)      RESEMBLES  A MANDATED formula on a
                                                             materially given
                                                             sphere; the record's
                                                             own ruling moves the
                                                             load OFF that boundary.
2.3   "causal feeding arrow"                      RESEMBLES  A direction label on an
                                                 (LEXICAL)   Adj_2 edge that "never
                                                             touches the cells".
2.4   last(r) = max event index whose unitary     PARTLY     *** THE ONE GENUINE
      support contains r                          CARRIES    INFLUENCE RELATION WITH
                                                             A COMPUTED LIMIT. ***
                                                             But it bounds an
                                                             OPERATION (CLOSE), no
                                                             boundary is defined by
                                                             it, and the co-located
                                                             "event boundary e" is
                                                             AN INDEX.
2.5   COMBINATORIAL cell-adjacency connectivity   DOES NOT   Named inside a MISSING
      + decay in COMBINATORIAL cell-separation    CARRY       sub-estimate; its
                                                             possibility judged
                                                             "NO"; and it would
                                                             certify summability,
                                                             not bound a region.
SHAPE THREE
3.1   NET row N: "On matched carriers ...         CARRIES    A matching condition
      identity cell matching"                     (part a)   governing when two
                                                             cells join. What
                                                             matches: CARRIERS, by
                                                             DECLARED LABEL
                                                             IDENTITY; typed of
                                                             record as "a domain
                                                             restriction".
3.2   R9 / JOINT LANDING at e, J1-J4, u(e)        CARRIES    A genuine agreement
                                                  (part a)   condition at a
                                                             junction: joins iff a
                                                             single induced unit is
                                                             shared there.
3.3   NET's void column: "Voids if ... a cell     CARRIES    Answers part (b):
      matching is silently selected outside the   (part b)   MISMATCH -> VOID.
      matched-carrier class"                                 An OBSTRUCTION.
3.4   "Joint landing is a FALSIFIER, not a        CARRIES    Answers part (b) in the
      constructor. Failure of J1-J4 kills."       (part b)   record's own words:
                                                             MISMATCH -> A VERDICT.
3.5   "One junction, two maps, two residues",     RESEMBLES  The noun is the shape's.
      each residue itemized                                  The object is not: two
                                                             lists of UNSUPPLIED
                                                             OBLIGATIONS, with no
                                                             support, no locus, no
                                                             carrier, no term — and
                                                             which "stand",
                                                             undischarged.
3.6   "invariant under each elementary refinement RESEMBLES  A boundary-named term —
      up to a boundary term whose ratio to                   but the error term of a
      four-volume tends to zero"                             REFINEMENT comparison,
                                                             REQUIRED TO VANISH,
                                                             inside an obligation
                                                             flagged
                                                             cellulation_independence
                                                             _proved = false.
------------------------------------------------------------------------------
TOTALS   CARRIES 4 (all in Shape Three) ; PARTLY CARRIES 1 ; RESEMBLES 7 ;
         DOES NOT CARRY 1.
```

### §7.3 READ REFUSALS HONOURED

```text
NO register / tracker / road / plan / continuation file was opened. The bar was
  applied AT THE PATH FILTER of every sweep, before any read, and no file whose
  basename matched was ever passed to a reader.
"Q-..." tokens: EXPECTED-UNLOCATABLE. Encountered inside quoted sealed text
  (Q-335 in NET's table cells; Q-126 in the 7A junction; Q-290; Q-42/Q-43
  referenced by O30SR). Carried as opaque labels, never chased, never resolved,
  nothing defaulted.
NO GIT COMMAND OF ANY KIND was run.
NOTHING under supervision/ was opened; it is outside the two declared roots.
FILES WRITTEN: exactly two — this artifact and its seal sidecar, at the
  commission's distinct path, probed ABSENT before the first write. No existing
  file was edited.
TOOLS: ls, find, grep -rIlE / -rInE, sed, wc, shasum -a 256 -c. No CAS. No
  numeric evaluation. No execution of corpus content.
```

---

## §8 — CHOICE LEDGER

```text
CL-1  DISCLOSED MY OWN DEFECTIVE PATTERN RATHER THAN REPAIRING IT SILENTLY.
      TAKEN        S1a's unanchored `variance` matched covariance/invariance and
                   returned 1188 ROOT1 files. Withdrawn in the artifact's own
                   text (§3.1), replaced by the word-anchored S1a'.
      ALTERNATIVE  Re-run quietly and report only the corrected census.
      WHY          A shape reported on a contaminated count is exactly the defect
                   this commission tests for in others. It would be incoherent to
                   commit it while reporting on it.

CL-2  GRADED EVERY MATCH CARRIES / RESEMBLES IN A TABLE (§7.2) RATHER THAN IN
      PROSE.
      ALTERNATIVE  Rely on the prose typing in §3-§5.
      WHY          The commission's central instruction is that a resemblance of
                   vocabulary is not an instantiation. A table forces the grade
                   to be stated once per match and prevents a favourable reading
                   accumulating across paragraphs.

CL-3  REPORTED THE STRONGEST NEAR-MISSES PROMINENTLY INSTEAD OF OMITTING THEM.
      TAKEN        GC-2's positivity halving (§3.4), last(r) (§4.5), and the
                   J-II residues (§5.2 B-3) are each displayed at full strength
                   BEFORE being disqualified.
      ALTERNATIVE  Omit them; none instantiates its shape.
      WHY          Suppressing the sweep's best result because it fails on
                   structure would hide the only thing the sweep found. Each is
                   granted in full and then typed.

CL-4  SPLIT SHAPE THREE (b) INTO "CONTENT" AND "OBJECT" INSTEAD OF ANSWERING THE
      COMMISSION'S EITHER/OR.
      TAKEN        Reported that the mismatch IS given a content (two itemized
                   residues) AND is given no object (no support, no locus, no
                   term).
      ALTERNATIVE  Answer "obstruction" flat, on the Voids/kills/PENDING
                   evidence.
      WHY          "Obstruction" alone would have erased the J-II decomposition,
                   which is a real and non-trivial thing the record does with a
                   mismatch. "Object" alone would have promoted a bookkeeping
                   remainder into a defect term. Both halves are true; both are
                   recorded. THIS IS THE DECISION THAT DETERMINES §5.

CL-5  READ THE NEAR-END CELL'S MISMATCH THROUGH TO R9-JII RATHER THAN STOPPING
      AT ITS STATUS LINE.
      TAKEN        Followed "R9-JII PENDING" to the J-II determination and
                   reported what it found.
      ALTERNATIVE  Report "no common cell formed; PENDING; NOT_RUN" and stop.
      WHY          The commission asked whether the corpus ANYWHERE assigns that
                   mismatch a content. Stopping at the status line would have
                   returned ABSENT on a question the record actually answers,
                   two files away, in its own sealed bytes.

CL-6  DID NOT TREAT "CONTRACTIBLE" AS A CONTRACTION (§3.5), NOR "OVERLAP LAW"
      AS AN OVERLAP RESIDUE (F-3), NOR "DISPERSION" AS A SPREAD (§3.2).
      WHY          The commission's standing instruction. Each of the three is a
                   token that a vocabulary-led sweep would have scored as a hit;
                   each is a different object at bytes. Recorded as lexical
                   resemblances in §7.2.

CL-7  LET THE SWEEPS LEAD OUT OF THE COMMISSIONED GROUND, WITH SEALS FIRST.
      TAKEN        The eight ground artifacts named nothing that instantiates
                   Shape One or Shape Two; the patterns led to CIS, NET, R9/J-II,
                   GC-2, G1-COLD, R2-KAPPA, the transfer-map spec. Every one was
                   seal-verified from its own directory BEFORE being read.
      ALTERNATIVE  Answer all three shapes from the eight ground files alone.
      WHY          Two of the three shapes would then have been returned ABSENT
                   without the corpus's best candidates ever being tested, and
                   the answer would have been about the ground, not the record.

CL-8  COUNTED FILES, NOT LINES, IN EVERY CENSUS TABLE.
      WHY          A file count cannot be inflated by one artifact repeating a
                   phrase. Where a token's whole weight sits in one file
                   (dispersion, feeding arrow), that is stated in the reading
                   column.

CL-9  NO SHAPE WAS SCORED PARTIAL FOR HAVING VOCABULARY.
      Shape One and Shape Two both have rich matching vocabulary and are returned
      ABSENT. Only Shape Three, which has a sealed matching condition and a
      sealed void/falsifier answer at bytes, is scored PARTIAL.
```

---

## §9 — TOY_SEPARATION

```text
IS ANY OBJECT IN THIS ARTIFACT A TOY, A MODEL, A STAND-IN, OR AN ILLUSTRATION?
NO. This artifact contains no constructed object at all. It contains sweeps,
file counts, quotations at bytes, seal results, and typings of quotations.
Nothing here is built, so nothing here could be mistaken for a built thing.

THE ACTUAL SURFACE, NOT A TOY: the question asked was whether the REAL corpus at
REAL bytes instantiates three imported shapes. Every answer above is a property
of files on disk at the declared cutoff, re-checkable by re-running the declared
patterns of §2.1 against the declared roots.

THE THREE PLACES A TOY COULD HAVE CREPT IN, EACH NAMED:
  1. THE THREE SHAPES THEMSELVES could have been treated as objects of the
     record. They are not. §0 and §7.1 state, before and after every test, that
     they are imports with no authority here. They are never used as premises,
     never cited as requirements, and no absence is called a defect.
  2. THE CARRIES/RESEMBLES TABLE (§7.2) is one short step from a proposed
     typology. It is not one: every row's object is transcribed from quoted bytes
     of a seal-verified artifact, and every grade is justified by that artifact's
     own words, not by a general principle of mine.
  3. THE NEAR-MISSES (GC-2, last(r), the J-II residues) are the corpus's own
     sealed objects, quoted as the corpus states them, including the corpus's own
     limiting sentences ("decides NOTHING"; "Theorem obligation"; "both residues
     stand"). Nothing is done with any of them here.

NO MECHANISM IS SUPPLIED ANYWHERE. Where a shape is absent, the absence is
displayed and the sweep is declared. No route to instantiating it is named,
costed, hinted, or ranked.
```

---

## §10 — FLAG BLOCK

```text
F-1  SEVERITY: DISCLOSED DEFECT IN THIS COMMISSION'S OWN INSTRUMENT.
     Sweep pattern S1a was defective (unanchored `variance` matching
     covariance/invariance; 1188 ROOT1 files returned). Withdrawn in the
     artifact's own text at §3.1 and replaced by S1a'. No count from S1a is used
     anywhere. Recorded rather than repaired silently.

F-2  SEVERITY: NOTE — ONE SWEEP HIT IS THIS ARTIFACT ITSELF.
     S2b ("where reach stops|edge of reach|limit of reach") returns exactly one
     ROOT1 file, and it is THIS artifact's §0 restatement of the imported Shape
     Two. S3c likewise returns this artifact's §0. Both are disclosed at the
     point of use (§4.1, §5.4) so no self-hit is counted as corpus evidence. The
     corpus's own count for both patterns is ZERO.

F-3  SEVERITY: NOTE — A TITLE-LEVEL NEAR-MISS, INSPECTED AND DISPOSED.
     STAGE8_OVERLAP_LAW_T11SR_V001.md (seal verified OK) carries "OVERLAP LAW"
     in its title and would be scored a hit by any vocabulary-led Shape Three
     sweep. Its own opening states its subject: "the overlap/angular-
     localization law for the B_pp' matrix elements", a ball-overlap MATRIX
     ELEMENT estimate in the Plancherel-Rotach regime. It concerns spectral
     overlap of Hermite data, not the joining of two regions across a surface.
     Disposed on subject, not on name; not quoted as ground.

F-4  SEVERITY: MATERIAL — A GENUINE INFLUENCE-LIMIT QUANTITY EXISTS AND IS NOT
     WHAT SHAPE TWO ASKS FOR. last(r) (§4.5) is a real limit of influence, and
     the artifact carrying it is a SPECIFICATION WITH ITS THEOREM OWED
     ("Theorem obligation. Freeze an explicit induction ..."). A future reading
     that scored Shape Two INSTANTIATED on last(r) would be scoring an unbuilt
     theorem's scheduling condition as a boundary definition. Flagged so it is
     not rediscovered as a positive.

F-5  SEVERITY: MATERIAL — SHAPE THREE'S PART (b) SPLITS, AND THE SPLIT IS THE
     RESULT. The record gives the mismatch a CONTENT and gives it NO OBJECT
     (§5.2). Either half quoted alone misreports the record. Any downstream use
     of this determination must carry both halves.

F-6  SEVERITY: NOTE — NO STRATUM TYPING IS PERFORMED HERE. Where the record
     leaves an object's stratum untyped (NET, per O23SR D-6 and O27SR OB-7),
     this artifact leaves it untyped. No shape verdict above turns on a stratum
     assignment.

NO FENCE WAS APPROACHED.
  alpha_computed = false        — no alpha quantity appears in this artifact.
  proof_authorized = false      — nothing here is offered as a proof.
  kappa_record_computed = false — kappa_n is named only inside a quotation of
                                  STAGE8_R2_KAPPA_N_DETERMINATION_S9AD_V001's
                                  own sealed display; no kappa was computed,
                                  evaluated, or relied on.
  No value originates here. No number is used as a program quantity. No measured
  constant appears. No comparison to any measured quantity is made. No git
  operation was performed. No mechanism, route, or construction is supplied.
```

```text
FLAGS
shapes_supplied_from_outside_the_corpus              = true
shape_one_forced_convergence                         = ABSENT
shape_two_reachability_edge                          = ABSENT
shape_three_matching_with_residue                    = PARTIALLY INSTANTIATED
shape_three_part_a_matching_condition                = PRESENT (two, both sealed)
shape_three_part_b_residue_as_object                 = ABSENT
shape_three_part_b_mismatch_given_a_content          = true  (J-II, two residues)
spread_or_dispersion_functional_of_a_family_located  = false
positivity_forcing_a_spread_to_decrease_located      = false
boundary_defined_as_limit_of_a_reachability_relation = false
influence_relation_with_a_computed_limit_located     = true  (last(r); bounds an
                                                              operation, not a region)
domain_of_dependence_files_both_roots                = 0
domain_of_influence_files_both_roots                 = 0
supported_on_the_surface_boundary_interface_junction_overlap_files_both_roots = 0
matches_graded_CARRIES                               = 4
matches_graded_PARTLY_CARRIES                        = 1
matches_graded_RESEMBLES                             = 7
matches_graded_DOES_NOT_CARRY                        = 1
seals_verified                                       = 28 OK / 0 mismatch
own_sweep_pattern_defect_disclosed                   = true  (S1a, §3.1)
alpha_computed                                       = false
proof_authorized                                     = false
kappa_record_computed                                = false
value_computed_of_any_kind                           = false
number_used_as_program_quantity                      = false
measured_constant_compared                           = false
git_operation_performed                              = false
existing_file_edited                                 = false
register_tracker_road_plan_continuation_file_opened  = false
mechanism_supplied                                   = false
anything_proposed_adopted_or_constructed             = false
ALL_RESULTS                                          = CLAIMED until checked.
```

---

## §11 — VERDICT

```text
SHAPE ONE   — FORCED CONVERGENCE.   *** ABSENT. ***  No quantity in either root
              measures the spread of a family; the corpus's positivity conditions
              bound a scalar, forbid a cancellation, value a member, or type an
              operator, and its one "forcing line" is refused as an illegal
              import ("NO FORCING FOUND").

SHAPE TWO   — REACHABILITY EDGE.    *** ABSENT. ***  The causal vocabulary is
              dense and every occurrence is a LABEL on an object defined
              otherwise: the cell is ASSIGNED by an underived parent and carries
              only a containment TEST; the ball is a MANDATED indicator whose
              boundary the record's own ruling declares not load-bearing; the
              feeding arrow "never touches the cells".  One genuine limit of
              influence exists — last(r) — and it bounds an OPERATION, while the
              thing called a "boundary" at that same site is an EVENT INDEX.

SHAPE THREE — MATCHING WITH RESIDUE. *** PARTIALLY INSTANTIATED. ***
              (a) PRESENT: two sealed matching conditions — NET's matched
                  carriers (a DECLARED IDENTITY LABEL MATCH, typed of record as
                  "a domain restriction"), and R9's joint landing at a cell
                  (a genuine agreement condition on a single shared unit u(e)).
              (b) ABSENT AS AN OBJECT.  Mismatch at the joining rule "Voids";
                  mismatch at R9 "kills", and the record types the condition in
                  its own words as "a FALSIFIER, not a constructor" that
                  "builds neither map"; mismatch at the near-end cell is
                  "no common cell formed; PENDING; NOT_RUN".
                  BUT THE MISMATCH IS GIVEN A CONTENT: at J-II the record writes
                  "One junction, two maps, two residues" and itemizes both.
                  THOSE RESIDUES ARE LISTS OF UNSUPPLIED OBLIGATIONS — no
                  support, no locus, no carrier, no term — and by the record's
                  own sentence they merely "stand".  A list of unmet obligations
                  is not a defect term.

OVERALL     — THE RECORD INSTANTIATES NONE OF THE THREE SHAPES OUTRIGHT.  It
              part-carries SHAPE THREE and only its first half: it has a
              matching condition, and it answers a failed match with a verdict
              rather than an object.  For SHAPES ONE and TWO it carries the
              vocabulary and not the structure — which is the finding the
              commission said would be as valuable as an instantiation and
              considerably more likely, and it is what the bytes return.

NOTHING IS CONSTRUCTED, PROPOSED, ADOPTED, OR SUPPLIED ANYWHERE IN THIS
ARTIFACT.  Every absence is displayed with the sweep that established it.

FENCES AT CLOSE: alpha_computed = false ; proof_authorized = false ;
kappa_record_computed = false.
```

```text
END STAGE8_BOUNDARY_SHAPES_O32SR_V001
COMMISSION O32SR — SHAPES-BUILD — 2026-08-15 — DETERMINATION ONLY
```
