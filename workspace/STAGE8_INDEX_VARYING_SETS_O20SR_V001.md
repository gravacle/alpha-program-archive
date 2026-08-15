# STAGE8 — INDEX-VARYING ADMISSIBLE SETS: DETERMINATION AT BYTES

COMMISSION O20SR — INDEX-BUILD — 2026-08-15
STATUS: **DETERMINATION ONLY.** Nothing here is proposed, authored, adopted, or
reclassified. No object is promoted. No class is changed. This artifact TYPES and
DISPLAYS what two already-sealed artifacts say, and nothing else.

FENCES CARRIED: `alpha_computed = false`; `proof_authorized = false`;
`kappa_record_computed = false`. No value, no number of physical import, and no
measured-constant comparison appears below. **Index values (b_1 = 0, 1, >1) and
vector-space dimensions ARE displayed** — they are the subject of the commission,
not quantities; combinatorial censuses attached to complex labels are ELIDED and
marked `[census elided]` wherever they are not load-bearing.

---

## §1 — SWEEP DECLARATION AND CUTOFF

```text
SWEEP CUTOFF: 2026-08-15, at the byte-states sealed in §2.  Anything written
              after this artifact's seal is outside my sweep by construction.
ROOTS:        (P) /Users/bgm/MB Work/alpha-program-archive/workspace   [PRIMARY]
              (S) /Users/bgm/Documents/New project/gravity_emergence_evidence_
                  program/alpha_fundamental_record_action_cleanroom_v003
DEPTH:        maxdepth 1, *.md, both roots, for the sweep legs below.
NEVER READ:   no register, tracker, road, plan, or continuation file was opened.
"Q-..." :     EXPECTED-UNLOCATABLE; not chased; carried as opaque tokens.

MY SWEEP LEGS, DECLARED AND EXECUTED:
  L1  The two tasked artifacts, read at bytes (spans + surrounding context).
  L2  The prior build and its audit, read at bytes for §8.
  L3  RE-EXECUTION of the prior build's own declared SWEEP 4 string, verbatim,
      over (P).  Hit count DISPLAYED in §8.
  L4  RE-EXECUTION of the audit's AS2 pattern, verbatim, over (P) and (S).
      Hit lists DISPLAYED in §8.
SCOPE LIMIT DISCLOSED: L3/L4 are PATTERN-BOUND.  An index-varying admissible set
  phrased without these tokens would not be returned by either.  I make no
  corpus-wide existence or absence claim beyond what these legs return.
```

---

## §2 — SEALS VERIFIED

Every seal below was verified with `shasum -a 256 -c` **executed from the
artifact's own directory**, against that artifact's own `.seal.sha256` sidecar.

```text
K1  STAGE8_TYPING_RULE_CANDIDATE_V001.md              root (P)   *** OK ***
    74f9470189a72d0d214ce72153559e17f1dfb65abeb159afb30538f6774b954a
    618 lines, 40100 bytes.  Head status: PROPOSED_NOT_ADOPTED.

K2  STAGE8_ACT2_CARRIER_PACKAGE_S9AD_V001.md          root (P)   *** OK ***
    38239f93de8b3a720659beba62f52dc2899e507f0fca72b57d88053dd59a09d8
    829 lines, 49196 bytes.

P1  STAGE8_GATE_SIGNATURE_O18SR_V001.md               root (P)   *** OK ***
    3bb7be90bdd47ade2b928e65bab29e0cd6b7951207136e2cbd85711bb5dd59b6
    730 lines, 41514 bytes.  THE PRIOR BUILD (§8).

P2  STAGE8_GATE_SIGNATURE_O18SR_AUDIT_V001.md         root (P)   *** OK ***
    b3d73333ca4920e23dc50ff16a7bd56c016bf8b39afba3a3cc7aa8d85f84eb79
    589 lines, 33208 bytes.  THE AUDIT THAT KILLED THE CLAIM (§8).

NEITHER K1 NOR K2 EXISTS IN ROOT (S).  Both are primary-root-only (L4, §8).
```

---

## §3 — DISPLAY 1: K1, `STAGE8_TYPING_RULE_CANDIDATE_V001.md`

### 3.1 The cited span, verbatim (`:318-321`)

> ```
> D2  CELLS: the rule TYPES any connected admitted cell (Lemmas 1-2 give its
>     admissible set at every b_1); its non-vacuous single-line sector is b_1 = 1,
>     the entered shape.  At b_1 > 1 the rule types the SPACE and selects no class
>     (§8 N1).  At b_1 = 0 the admissible set is empty (K-2).
> ```

**D2 IS NOT THE OPERATIVE SENTENCE — IT POINTS AT ONE.** "Lemmas 1-2 give its
admissible set at every b_1" is a forward reference. The operative content is at
`:152-161` and I take the determination from there, per the rule that where a
summary and the sentence it summarises could diverge, the sentence governs.

### 3.2 The operative sentences, verbatim (`:152-161`)

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

### 3.3 WHAT IS THE INDEX, AND WHAT THE SET CONTAINS AT EACH VALUE

```text
INDEX NAME      b_1(C_j) — the first Betti number of a connected admitted cell C_j.
INDEX RANGE     the non-negative integers, displayed in THREE SECTORS.

  b_1 = 0   (C_j a tree)   A = EMPTY.  Verbatim: "it is EMPTY — no nonzero
                           conserved cell-local write exists".
  b_1 = 1                  A = Q·gamma_j(C_j) \ {0}, the CIRCUIT LINE punctured
                           at zero.  One-dimensional.
  b_1 > 1                  A = the b_1(C_j)-dimensional cycle space MINUS ZERO,
                           with "R-CLW SELECTS NOTHING in it".
```

### 3.4 *** IS THE VARIATION DISPLAYED, OR MERELY ASSERTED? ***

```text
*** DISPLAYED. ***  Not a constant family.  The artifact does not say "an
admissible set is attached at every b_1" and leave the content fixed; it WRITES
OUT a different set at each of three index sectors, in one sentence, at bytes.

TWO DISTINCT INDEX VALUES WITH DISTINCT ADMISSIBLE SETS — EXHIBITED:
  b_1 = 0  ->  A = EMPTY
  b_1 = 1  ->  A = Q·gamma_j(C_j) \ {0}
DISTINCTNESS REQUIRES NO COMPUTATION: one set is empty, the other is not.
A THIRD is exhibited (b_1 > 1: a space of dimension b_1, not a line).

EACH ENDPOINT ALSO CARRIES A RECORD-SIDE WITNESS, so the display is not merely
formal:
  K-1 (:165-167)  at b_1 = 1, on the ENTERED cell K_square, "the admissible set
                  is Q·gamma_j — the entered read theta_j = <A, gamma_j> is
                  EXACTLY a cell-local write under R-CLW".
  K-2 (:168-170)  at b_1 = 0, the empty set "reproduc[es] the entered
                  disposition 'b_1 = 0 ... INERT ... a DETERMINATION made on
                  purpose' ... as a theorem of the typing rather than a
                  stipulation".
Both endpoints are thus pinned to named sealed dispositions, not to the
formula alone.
```

---

## §4 — DISPLAY 2: K2, `STAGE8_ACT2_CARRIER_PACKAGE_S9AD_V001.md`

### 4.1 The cited span, verbatim (`:769-773`), censuses elided

> ```
> FORCING_DETERMINATION = NOT-FORCED(the sealed record does not close the
>   admissible physical-cell-family class; WIDER-CLASS display included: at the
>   full require set R-a..R-g the admissible class = the [N] K_dd variants ∪ every
>   larger conforming complex (A2 [census elided], A2b [census elided], A1 [census
>   elided], W2 [census elided], A5 [census elided], unbounded upward); under the
>   unwritten strict horn the minimum moves to A5; on an Attach void KLf-type
>   complexes return and W1 stays out ...
> ```

**THE CITED SPAN IS THE FLAG BLOCK — A COMPRESSION.** Read alone, the variation
across the index is carried in a trailing parenthesis ("under the unwritten
strict horn ...; on an Attach void ..."), which is closer to ASSERTION than to
DISPLAY. **The artifact discharges it elsewhere**, in a section whose own title
names the act. I take the determination from there.

### 4.2 The DISPLAY, verbatim (`§3.3`, `:181-190`), censuses elided

> ```
> AT THE FULL REQUIRE SET (R-a..R-g, confirmed reading):
>   ADMISSIBLE = { the [N] K_dd variants }  ∪  { A2, A2b, A1, W2, A5, ... }  —
>   INFINITE, closed under conforming enlargement.  K_dd is distinguished ONLY by
>   the lane's minimality instrument.
> UNDER THE STRICT-HORN READING of R-g (unwritten, disclosed):  K_dd leaves the
>   class; A5 is the minimal member; the class remains infinite.
> ON AN ATTACH VOID (R-f/R-g dissolve):  the class WIDENS further — KLf-type
>   complexes ([census elided]) return (they fail only the sector pin);
>   W1 ([census elided]) stays OUT either way (its monogon face fails
>   derivation-strength R-c).
> ```

### 4.3 WHAT IS THE INDEX, AND WHAT THE CLASS CONTAINS AT EACH VALUE

```text
INDEX NAME      THE REQUIRE SET IN FORCE, together with the READING of R-g.
INDEX RANGE     three values EXHIBITED, each a distinct conjunction of requires:

  I    R-a..R-g, R-g on the CONFIRMED (trace-carrier-specific) reading
       CLASS = { K_dd variants } ∪ { A2, A2b, A1, W2, A5, ... }, infinite,
               closed under conforming enlargement.
  II   R-a..R-g, R-g on the STRICT UNWRITTEN horn (a disclosed reading supply,
       "never ruled" — :143-144)
       CLASS = K_dd LEAVES IT; A5 is the minimal member; still infinite.
  III  ATTACH VOID: R-f and R-g DISSOLVE, leaving R-a..R-e
       CLASS = WIDER still; KLf-type complexes RETURN; W1 stays OUT.

A FOURTH AXIS IS DISPLAYED AT §3.2 (:163-169): dropping R-c (the sealed face
shape) at the same census leaves the floor standing but MULTIPLIES the labelled
realizations [counts elided] — "B4 is load-bearing only for uniqueness".  So the
require set indexes the class even WITHIN value I.
```

### 4.4 *** IS THE VARIATION DISPLAYED, OR MERELY ASSERTED? ***

```text
*** DISPLAYED — and by the strongest available exhibition. ***

Not a constant family.  The display does not merely change a cardinality or a
dimension: A NAMED MEMBER CHANGES MEMBERSHIP ACROSS TWO INDEX VALUES, in the
same ambient, verbatim —

  K_dd  ∈ CLASS(I)    "ADMISSIBLE = { the [N] K_dd variants } ∪ ..."
  K_dd  ∉ CLASS(II)   "K_dd leaves the class"

That is a display of variation, not an assertion of it: the two index values are
named, the member is named, and the membership verdict is written out at each.

A SECOND, CONVERSE EXHIBIT: a named NON-member that is invariant —
  W1  ∉ CLASS(I), CLASS(II), CLASS(III)   "W1 stays OUT either way", grounded on
      derivation-strength R-c, which no displayed index value dissolves.

A THIRD: a member that ENTERS at the widest value —
  KLf-type  ∉ CLASS(I)/(II) (fails the sector pin R-f), ∈ CLASS(III).
```

---

## §5 — TYPE THE SIGNATURE

Derived from the operative sentences (§3.2, §4.2), never from a name or a title.

### 5.1 K1 — the signature is a GENUINE MAP, but NOT the one D2's phrasing suggests

```text
LEMMA 1 IS THE MAP.  Its operative sentence takes a CELL and yields a SET:

        A : C_j  |-->  Z_1(C_j; Q) \ {0}      (Lemma 2 supplies the puncture)

  INPUT  side of the sentence: "the conserved cell-local set OF CELL C_j".
  OUTPUT side: "is exactly the cycle space Z_1(C_j; Q) = ker(bdry)|_{C_j}".
  This is a map from an object to a set.  NOT an annotation.

LEMMA 2 IS ITS PUSHFORWARD ALONG b_1.  Lemma 2's three clauses are keyed on
b_1(C_j), and what they yield at each key is a SHAPE:

        Shape : b_1  |-->  { EMPTY | punctured line | punctured b_1-space }

*** THE DISTINCTION THAT DECIDES THE TYPING. ***  b_1 |--> A is NOT well defined
as a map to LITERAL SETS, and the artifact's own bytes show why:
  (a) at b_1 = 1 the yielded set is Q·gamma_j(C_j) — it depends on WHICH cell,
      through gamma_j(C_j), not on the integer 1 alone;
  (b) the ambient itself moves: Z_1(C_j;Q) sits inside the edge space of C_j, so
      two cells with different edge sets yield sets in DIFFERENT ambient spaces.
Two distinct cells sharing b_1 = 1 therefore have distinct literal admissible
sets.  The integer does not determine the set; it determines the set's SHAPE.

SIGNATURE VERDICT (K1):
  As a map from the CELL: *** GENUINE MAP, object -> set. ***
  As a map from the INDEX b_1: *** GENUINE MAP TO SHAPES, and only to shapes. ***
    Non-constant (three distinct shapes) — so b_1 is NOT a mere annotation.
    But NOT a map to literal sets — so "the admissible set at b_1 = 1" does not
    name one set; it names one set PER CELL of that Betti number.
```

### 5.2 K2 — the signature is a GENUINE MAP, and to literal classes

```text
THE OPERATIVE SENTENCES ARE §3.3's THREE HEADED LINES.  Each takes a require-set
value on its INPUT side ("AT THE FULL REQUIRE SET ...", "UNDER THE STRICT-HORN
READING of R-g ...", "ON AN ATTACH VOID (R-f/R-g dissolve) ...") and yields a
class on its OUTPUT side ("ADMISSIBLE = { ... }", "K_dd leaves the class; A5 is
the minimal member", "the class WIDENS further — ... return ... stays OUT").

        C : (require set, reading)  |-->  a class of connected complexes

  INPUT  side: a conjunction of named requires drawn from R-a..R-g, plus which
               horn of R-g is read.
  OUTPUT side: a class whose MEMBERS ARE NAMED (K_dd, A2, A2b, A1, W2, A5,
               KLf-type) and whose NON-MEMBERS ARE NAMED (W1).

*** ALL THREE VALUES YIELD CLASSES IN ONE AND THE SAME AMBIENT *** — connected
complexes — so unlike K1 there is no moving ambient.  The map is to LITERAL
classes, comparable member-by-member across index values, and §4.4 exercises
exactly that comparability.

SIGNATURE VERDICT (K2): *** GENUINE MAP, index value -> literal class. ***
  The index is NOT an annotation: the map is provably non-constant on named
  members (K_dd flips), and it is ANTITONE — the artifact's own word for the
  III direction is "WIDENS", and III's require set is a SUBSET of I's and II's.
```

---

## §6 — WHAT IS THE INDEX? (the kinds, established at bytes)

```text
                 K1                              K2
KIND             A CARDINALITY.                  A REQUIRE SET / A SET OF
                 Specifically dim_Q Z_1(C_j;Q),   CONDITIONS, together with a
                 fixed by Lemma 1's own words     READING of one of them.
                 "of dimension b_1(C_j)".
RANGES OVER      non-negative integers, i.e.      conjunctions drawn from the
                 an INVARIANT OF THE OBJECT       named requires R-a..R-g, i.e.
                 BEING TYPED.                     a PARAMETER OF THE CONDITION.
A STAGE?         *** NO. ***  Nothing in D2 or   *** NO. ***  Nothing orders the
                 Lemmas 1-2 orders the sectors,   three values as steps; they are
                 supplies a successor, or names   alternative hypotheses in force,
                 a construction step.  The three  two of them counterfactual
                 sectors are a case split on an   ("unwritten", "on an Attach
                 invariant, not a sequence.       void").
ORDERING         total (integers) — but see §7    PARTIAL, by inclusion of
PRESENT?         for why the order does not       requires; the class map is
                 give a usable direction here.    ANTITONE along it.

*** THE TWO INDICES ARE OF DIFFERENT KINDS AND ARE NOT THE SAME OBJECT. ***
K1's index is an invariant computed FROM the thing being typed.  K2's index is a
selection of PREMISES under which typing happens.  Neither is a stage.  A claim
that these two artifacts exhibit "the same index-varying admissible set" would
be false at bytes; they exhibit two, of different type.
```

---

## §7 — THE INVARIANCE QUESTION

The question: **can "what lies in the admissible set at every index" be STATED
over either object, and is its domain populated with more than one exhibited
member?** I determine this. **I do not build such an invariance, and none is
proposed, authored, or adopted below.**

### 7.1 Over K2's object — *** STATABLE, POPULATED, AND WITNESSED ***

```text
PIECES REQUIRED                            PRESENT AT BYTES?
(1) a named index                          YES — the require set + R-g reading.
(2) more than one EXHIBITED index value    YES — three: I, II, III (§4.3).
(3) a COMMON AMBIENT for the yielded sets  YES — all three are classes of
                                           connected complexes; membership is
                                           comparable across values.
(4) at least one EXHIBITED member of the   YES — A5.
    intersection
(5) at least one EXHIBITED non-member      YES — W1, "stays OUT either way".

*** ALL FIVE PIECES ARE PRESENT.  NOTHING IS MISSING.  The invariance is
STATABLE over K2's object, and its domain is populated with three exhibited
values — more than one. ***

THE WITNESS, TRACED:
  A5 ∈ CLASS(I)    literal — listed in the §3.3 union and in §3.2's row list.
  A5 ∈ CLASS(II)   literal — "A5 is the minimal member".
  A5 ∈ CLASS(III)  *** DERIVED-FROM-DISPLAYED, ONE STEP, MARKED AS SUCH ***:
                   III's require set (R-a..R-e, R-f/R-g dissolved) is a SUBSET
                   of I's (R-a..R-g); the artifact's own word for that direction
                   is that the class "WIDENS".  A member of the narrower class
                   is a member of the wider.  I mark this as an inference from
                   displayed text, not as a literal listing.

*** BUT THE INTERSECTION IS NOT DETERMINED, AND I SAY SO. ***  The artifact never
displays CLASS(II)'s full membership — only that K_dd leaves and A5 is minimal.
So the intersection is BOUNDED (it contains A5; it is contained in CLASS(I)) and
its exact extent is UNDISPLAYED.  The invariance is statable and witnessed; it is
NOT thereby computed.  Stating it would be a further act, and I do not take it.
```

### 7.2 Over K1's object — *** STATABLE ONLY IN A FORM THAT CARRIES NO CONTENT ***

```text
PIECES REQUIRED                            PRESENT AT BYTES?
(1) a named index                          YES — b_1(C_j).
(2) more than one EXHIBITED index value    YES — three sectors: 0, 1, >1.
(3) a COMMON AMBIENT for the yielded sets  *** NO. ***
(4) an EXHIBITED member of the             *** NO — and one cannot exist. ***
    intersection

*** MISSING PIECE 1 — THE AMBIENT MOVES (this is the one that decides it). ***
By Lemma 1 the admissible set of C_j lies in the edge space of C_j.  To move
across the index you must CHANGE THE CELL — because for a FIXED cell, b_1(C_j)
is a single determined integer, so the family over a fixed object is a SINGLETON
and there is nothing to intersect.  Changing the cell changes the ambient.  A
set-theoretic intersection ACROSS index values is therefore ILL-POSED for want of
an identification of Z_1(C_j;Q) across distinct cells.

  *** THE ARTIFACT NAMES THIS ABSENCE ITSELF. ***  F3 (:350-355) records "the
  sealed-absent diamond-to-complex transport ... the Ref_a-indexed
  current-density receiver + the exhaustion<->refinement index bridge, the two
  UNSUPPLIED slots of record".  That is precisely the transport an intersection
  across cells would need, and it is marked UNSUPPLIED at bytes.

*** MISSING PIECE 2 — THE b_1 > 1 SECTOR IS DELIBERATELY UNNARROWED. ***  Lemma 2:
"R-CLW SELECTS NOTHING in it"; N1 (:379-383) carries the entered bar verbatim —
a selector "this artifact does not supply and MAY NOT FREEZE".  So the sector
cannot be sharpened into anything a cross-index invariance could bite on without
an act the artifact expressly bars.

*** WHAT IS STATABLE ANYWAY, AND WHY IT IS EMPTY. ***  If one intersects over the
whole displayed range regardless, the answer is FORCED EMPTY: the b_1 = 0 sector
yields the EMPTY SET (Lemma 2; K-2), and any intersection containing an empty
member is empty.  So over K1's object the invariance is statable, VACUOUS, and
carries no content — a constant answer forced by one sector, not a fact about
the family.  Restricting to b_1 >= 1 does not rescue it: MISSING PIECE 1 then
governs, and the restricted question is ill-posed rather than empty.
```

### 7.3 Across BOTH objects jointly — *** NOT STATABLE ***

```text
The two indices range over different kinds (§6), and the two admissible sets have
members of different type: K1's members are 1-CHAINS inside one cell's cycle
space; K2's members are WHOLE COMPLEXES.  No sealed text displayed to me supplies
a map between the two index sets.
MISSING PIECE, NAMED EXACTLY: any displayed correspondence carrying a require-set
value to a b_1 sector, or conversely.

*** THE NEAR-MISS, RECORDED SO IT IS NOT MISTAKEN FOR THE BRIDGE. ***  K2 §3.3
(:191-196) DOES evaluate its own members at K1's index: "every admitted CELL of
K_dd — the trace cell K_square and the face closure — has b_1 = 1 ... A5's cells
are likewise b_1 = 1 cell-wise".  This is a genuine point of contact.  But it
pins BOTH named members to the SAME b_1 value, so it supplies a CONSTANT SECTION
over K1's index, not a variation across it.  A constant section is not a bridge:
it exhibits no pair of distinct b_1 values arising from distinct require-set
values, which is what a joint invariance would need.
```

---

## §8 — THE SUPPRESSION, OF RECORD

Displayed without editorialising: what the prior build DECLARED it swept, what it
DISPLAYED, and what its own declared sweep returns when re-executed at bytes.

### 8.1 What the prior build DECLARED (P1 `:80-85`, verbatim)

> ```
> SWEEP 1 (filenames, both roots): REQUIRE|REQUIRED|SHAPE       -> 62 hits in (P)
> SWEEP 2 (filenames, both roots): ALLOW|PERMIT|ADMISS|ELIGIB   -> 20 hits in (P)
> SWEEP 3 (content):  'shapes? a requirement|distinct shapes|N shapes|require-shape'
> SWEEP 4 (content):  'admissible set|set of admissible|admissible values|permitted values|
>                      set of permitted|admissible continuations|admissible next'
> ```

**SWEEPS 1 AND 2 CARRY HIT COUNTS. SWEEPS 3 AND 4 DO NOT.** Sweep 3's result is
narrated in the next line of the build (`:87-89`). **Sweep 4's result is narrated
nowhere in the build.** No hit count, no hit list, no member of its return is
displayed anywhere in P1.

### 8.2 What the prior build CONCLUDED on the strength of it (P1 `:420-428`)

> ```
> **BOTH CARRY A DEFINITE ARTICLE AND NEITHER STATES A DOMAIN.** Not "the admissible set of
> X", not "the admissible set over Y" — just "the admissible set", attached to whichever
> condition is in hand. Across the whole subject exactly **one** occurrence anywhere states a
> domain, G3 `:283`'s "admissible set over `State(B)`", **and that is the occurrence G3
> withdraws as the wrong question** (§5.1).
>
> *** THERE IS NO SINGLE SELECTOR. THERE IS A PER-CONDITION FAMILY OF ADMISSIBLE SETS WITH NO
> INDEX SET. "INVARIANT ACROSS EVERY APPLICATION OF IT" HAS NO REFERENT FOR "IT" AND NO RANGE
> FOR "EVERY". THE DOMAIN IS NOT MERELY UNPOPULATED — IT IS UNFORMED. ***
> ```

### 8.3 What the audit found (P2 `:49-50`, `:517-522`, verbatim)

> ```
> **AS1 AND AS2 ARE THE SWEEPS THAT DECIDE THIS AUDIT.** They are the sweeps the build itself
> declared as its SWEEP 4 and whose hit count it never displayed. §5 reports what they return.
> ```

> ```
> M12 *** build_absence_claim_holds_at_corpus_scope = false | TYPE-R | EXECUTED ***
>       K1 (TYPING_RULE_CANDIDATE :318-321, sealed, primary root, no excluding mark) states
>       an admissible set "at every b_1" and displays it taking different values at different
>       index values.  K2 (ACT2_CARRIER_PACKAGE_S9AD :769-773, sealed, primary root, no
>       excluding mark) states an admissible class at a named require set, non-singleton and
>       unbounded upward.  §6.1's "exactly one occurrence ANYWHERE", §5.1's "ONE EXCEPTION",
>       §5.2's "no stage index", N6, N7 and F6's immunity claim are REFUTED as stated.
> ```

### 8.4 THE RE-EXECUTION, AT BYTES (my sweep legs L3 and L4)

```text
L3 — THE BUILD'S OWN SWEEP 4 STRING, VERBATIM, over (P), maxdepth 1, *.md:
       returns 45 FILES.
       STAGE8_TYPING_RULE_CANDIDATE_V001.md  ...  7 matching lines.   [K1 RETURNED]
       STAGE8_ACT2_CARRIER_PACKAGE_S9AD_V001.md  ...  0 matching lines.
     *** THE BUILD'S LITERAL SWEEP-4 STRING RETURNS K1 AND DOES NOT RETURN K2. ***
     K2 says "admissible CLASS", a token absent from the literal Sweep 4 string.

L4 — THE AUDIT'S AS2 PATTERN, VERBATIM
     'admissible (set|class|values)[^.]{0,60}(every|each|all|per |indexed)'
     — which P2 :49-50 states IS the build's Sweep 4 — over (P), maxdepth 1:
       returns 11 FILES, among them BOTH:
         STAGE8_ACT2_CARRIER_PACKAGE_S9AD_V001.md      [K2 RETURNED]
         STAGE8_TYPING_RULE_CANDIDATE_V001.md          [K1 RETURNED]
       (also returned: STAGE8_7A_COMPLETENESS_PROOF_DARIO_V001.md,
        STAGE8_7A_PUBLIC_LAYER_CROSSCHECK_CODEX2_V001.md,
        STAGE8_DISCHARGERS_VS_PARTITION_O11SR_V001.md and its AUDIT,
        STAGE8_GATE_SIGNATURE_O18SR_V001.md and its AUDIT,
        STAGE8_R1_NAMING_CANDIDATE_V001.md,
        STAGE8_TASK4A_SOURCE_TO_OUTPUT_NORMALIZATION_..._V001.md,
        STAGE8_TASK5_EQ6_WHERE_CLAUSES_FINAL_CHECK_LANE1_V001.md)
     Same pattern over (S), maxdepth 1: returns 4 files; NEITHER K1 NOR K2 is
     among them — both are primary-root-only.

THE OMISSION, STATED FLATLY AND WITHOUT CHARACTERISATION:
  The build declared a content sweep whose purpose was to find stated admissible
  sets.  It displayed hit counts for its two filename sweeps and a narrated
  result for one of its two content sweeps.  For Sweep 4 it displayed no count,
  no list, and no member.  It then wrote that exactly one occurrence anywhere
  states a domain and that the domain is UNFORMED.  Re-executed at bytes, the
  build's own declared Sweep 4 string returns 45 files including K1; the pattern
  the audit identifies as that same sweep returns 11 files including both K1 and
  K2.  Both K1 and K2 are sealed, in the primary root, and carry no mark the
  build declared as excluding.
```

---

## §9 — INSTRUMENT: EXACT SYMBOLIC CHECK OF K1's LEMMA 1 ARITHMETIC

One claim in §3 needs an instrument rather than a reading: that the family K1
displays is genuinely NON-CONSTANT, i.e. that Lemma 1's "of dimension b_1(C_j)"
delivers different sets at different index values. Checked exactly, over Q, in a
FRESH venv (sympy 1.14.0), no floats, no physical quantity. Exit 0.

```text
CHECK OBJECTS (instrument only — see TOY_SEPARATION §11):
  T   path on 3 vertices, 2 edges        (a tree)
  S   4-cycle, 4 vertices, 4 edges       (the b_1 = 1 shape)
  TH  theta: 2 vertices, 3 parallel edges

RESULT (exact rational nullspaces of the boundary map d_1):
  T   rank(d_1)=2   b_1 = 0   dim ker = 0   ->  A = EMPTY
  S   rank(d_1)=3   b_1 = 1   dim ker = 1   ->  A = ker\{0}, a punctured LINE
  TH  rank(d_1)=1   b_1 = 2   dim ker = 2   ->  A = ker\{0}, a punctured PLANE

  b_1 = E - rank(d_1) agreed with dim ker(d_1) on every object (in-script
  assertion; it held on all three, else the run would have aborted non-zero).
  EMPTY vs NONEMPTY  (b_1=0 vs b_1=1):  True
  dim 1 vs dim 2     (b_1=1 vs b_1=2):  True
  NON-CONSTANT FAMILY (three distinct dimensions):  True
  b_1=1: d_1(c·gamma) = 0 identically for symbolic c:  True   [the line is a line]
  b_1=2: d_1(a·k1 + b·k2) = 0 identically for symbolic a,b:  True
  b_1=2: k2 is NOT a scalar multiple of k1 (rank of [k1|k2] = 2):  True
         [so the b_1 > 1 sector is genuinely NOT a line — the shape differs from
          the b_1 = 1 sector, confirming Lemma 2's three-way split is a real
          three-way split and not a relabelling]

WHAT THIS DOES AND DOES NOT ESTABLISH:
  DOES     — K1's displayed family is non-constant as a function of b_1, exactly.
  DOES NOT — it establishes nothing about which cells are admitted, nothing about
             any carrier, and nothing physical.  It checks arithmetic K1 already
             states; it adds no content to the record.
```

---

## §10 — CHOICE LEDGER

```text
C1  TOOK THE DETERMINATION FROM LEMMAS 1-2 (:152-161) RATHER THAN FROM THE CITED
    SPAN D2 (:318-321).  BASIS: D2's own text defers ("Lemmas 1-2 give its
    admissible set at every b_1").  COST IF WRONG: none to the verdict — D2 alone
    already displays three sectors with three sets; the Lemmas sharpen the
    content and supply the ambient fact that decides §7.2.
C2  TOOK K2's DISPLAY FROM §3.3 (:181-190) RATHER THAN FROM THE CITED FLAG-BLOCK
    SPAN (:769-773).  BASIS: the FLAG BLOCK compresses the variation into a
    parenthesis; §3.3 is titled "THE DISPLAY" and writes each index value out on
    its own line.  DISCLOSED CONSEQUENCE: at the CITED span alone, K2's variation
    reads closer to ASSERTED than DISPLAYED.  I record both readings rather than
    silently upgrading the cited span (§4.1).
C3  MARKED "A5 ∈ CLASS(III)" AS DERIVED-FROM-DISPLAYED, NOT LITERAL.  Could have
    stated it flatly.  Chose to expose the one inference step (§7.1).  COST IF
    WRONG: the witness would rest on values I and II only — still more than one
    exhibited index value, so §7.1's verdict survives.
C4  DECLARED THE JOINT INVARIANCE NOT STATABLE (§7.3) DESPITE THE K_dd/A5
    CELL-WISE FACT.  BASIS: that fact is a constant section over b_1, not a
    variation.  COST IF WRONG: §7.1 and §7.2 are unaffected; only §7.3 retargets.
C5  ELIDED COMBINATORIAL CENSUSES AND VARIANT COUNTS.  BASIS: the fence bars
    numbers; the determination never needs them — it needs only that classes are
    non-singleton and that named membership flips.  Index values and vector-space
    dimensions ARE displayed, because they are the commission's subject.
C6  RE-EXECUTED BOTH THE BUILD'S LITERAL SWEEP-4 STRING AND THE AUDIT'S AS2,
    AND REPORTED THAT THEY DIFFER ON K2 (§8.4).  Could have reported only AS2,
    per the audit's identification of the two.  Chose to display the discrepancy
    at bytes rather than adopt the audit's equation of them unexamined.
C7  DID NOT OPEN ANY REGISTER, TRACKER, ROAD, PLAN, OR CONTINUATION FILE, and did
    not resolve any "Q-..." token, including those appearing inside consumed text.
```

---

## §11 — TOY_SEPARATION

```text
THE THREE CHECK GRAPHS IN §9 (T, S, TH) ARE INSTRUMENT OBJECTS AND NOTHING ELSE.
They are not carriers, not candidates, not admitted cells, and not physical.  They
were constructed by me to check an arithmetic identity K1 already states; none is
proposed for admission, none is compared to any sealed object, and no property of
any of them transfers to the record.  S is the 4-cycle SHAPE only; it is not
K_square and I make no identification with it.

EVERYTHING ELSE IN THIS ARTIFACT IS QUOTATION OR TYPING OF QUOTATION.  The strata
of the consumed artifacts are carried unchanged: K1 remains PROPOSED_NOT_ADOPTED
at its own head; K2's objects remain at the CANDIDATE stratum with NONE_SEALED at
the physical write-carrier stratum surviving untouched, exactly as K2's own
TOY_SEPARATION (:746-762) states.  Displaying that an artifact states a varying
admissible set PROMOTES NOTHING — not the artifact, not its class, not any member
of any class named in it.  No stratum was crossed by this determination.
```

---

## §12 — IMPORT AUDIT

```text
IMPORTED INTO THIS ARTIFACT — the complete list:
  I1  K1's spans :152-161, :165-170, :318-321, :350-355, :379-383  — QUOTED.
  I2  K2's spans :141-149, :155-176, :181-197, :746-762, :769-773  — QUOTED,
      censuses elided and marked.
  I3  P1's spans :80-85, :420-428  — QUOTED for §8 only.
  I4  P2's spans :42-50, :227-248, :517-522  — QUOTED for §8 only.
  I5  sympy 1.14.0, fresh venv, for §9's exact linear algebra ONLY.

NOT IMPORTED — asserted:
  N1  NO PHYSICS PREMISE.  No quantity computed, compared, or carried.
  N2  NO NUMBER OF PHYSICAL IMPORT.  No constant, measured or derived, appears.
  N3  NO SEALED TEXT AMENDED, re-read against its own reading, or reclassified.
  N4  NO CLAIM ABOUT WHETHER K1's RULE OR K2's ADMISSION SHOULD BE ENTERED.  The
      commission bars it and I take no position.
  N5  NO CORPUS-WIDE EXISTENCE OR ABSENCE CLAIM.  My sweep legs are pattern-bound
      (§1) and I claim only what they returned.
  N6  NO INVARIANCE BUILT.  §7 determines statability; it states no invariance.
```

---

## §13 — FLAG BLOCK

```text
BOTH_SEALS_VERIFIED = true (K1, K2 — plus P1, P2 consumed for §8; all four
  recomputed with shasum -a 256 -c from each artifact's OWN directory, §2).
K1_VARIATION = *** DISPLAYED *** (three index sectors, three sets written out;
  two exhibited with distinct sets requiring no computation to separate —
  b_1 = 0 EMPTY vs b_1 = 1 the punctured circuit line; both endpoints carry a
  named record-side witness, K-1 and K-2).
K2_VARIATION = *** DISPLAYED *** (three exhibited require-set values; a NAMED
  member flips membership across two of them — K_dd ∈ I, K_dd ∉ II, verbatim
  "K_dd leaves the class"; a named non-member W1 is invariant OUT; a named
  member KLf-type enters at III).
CONSTANT_FAMILY_VERDICT = NEITHER IS A CONSTANT FAMILY.  Both were tested against
  the trap and both pass on their own bytes.
K1_SIGNATURE = GENUINE MAP cell -> set (Lemma 1).  As a map from the INDEX b_1 it
  is a GENUINE MAP TO SHAPES ONLY — non-constant, so b_1 is not a mere
  annotation, but it does NOT determine a literal set: at b_1 = 1 the set is
  Q·gamma_j(C_j), cell-dependent, in a cell-dependent ambient.
K2_SIGNATURE = GENUINE MAP index value -> LITERAL CLASS, one fixed ambient
  (connected complexes), antitone in the require set ("WIDENS", K2 :187).
K1_INDEX_KIND = A CARDINALITY — dim_Q Z_1(C_j;Q), an invariant OF THE OBJECT
  TYPED.  NOT a stage: nothing orders the sectors or supplies a successor.
K2_INDEX_KIND = A REQUIRE SET plus a READING — a parameter OF THE CONDITION.
  NOT a stage.  Partially ordered by inclusion of requires.
INDICES_ARE_DISTINCT_OBJECTS = true.  Different kind, different member type in
  the yielded sets (1-chains vs whole complexes).
INVARIANCE_OVER_K2 = *** STATABLE, DOMAIN POPULATED (three exhibited values),
  WITNESS EXHIBITED (A5) *** — all five required pieces present, none missing.
  NOT DETERMINED: CLASS(II)'s full membership is undisplayed, so the exact
  intersection is bounded (⊇ {A5}, ⊆ CLASS(I)) and not computed.  NOT BUILT HERE.
INVARIANCE_OVER_K1 = *** NOT STATABLE WITH CONTENT. ***  MISSING, exactly:
  (M1) a COMMON AMBIENT / transport identifying Z_1(C_j;Q) across distinct cells
       — K1 itself marks this UNSUPPLIED at F3 :350-355 (the exhaustion<->
       refinement index bridge, "the two UNSUPPLIED slots of record");
  (M2) any narrowing at the b_1 > 1 sector — barred, not merely absent: N1
       :379-383 carries "may not freeze" verbatim.
  STRUCTURAL REASON: for a FIXED cell b_1 is a single determined integer, so the
  family over a fixed object is a SINGLETON; moving the index requires moving the
  object, which moves the ambient.  Intersecting anyway over the displayed range
  yields EMPTY, forced by the b_1 = 0 sector — statable but vacuous.
INVARIANCE_JOINT = NOT STATABLE.  MISSING: any displayed correspondence between
  require-set values and b_1 sectors.  The K_dd/A5 cell-wise fact (K2 :191-196)
  is a CONSTANT SECTION over b_1, not a bridge.
SUPPRESSION_OF_RECORD = the prior build declared SWEEP 4 over admissible-set
  tokens, displayed hit counts for its two filename sweeps and a narrated result
  for one content sweep, and displayed NO count, NO list and NO member for
  SWEEP 4; it then wrote that exactly one occurrence anywhere states a domain and
  that the domain is UNFORMED.  Re-executed: the build's literal Sweep 4 string
  returns 45 files in (P) including K1; the audit's AS2 — which the audit states
  is that same sweep — returns 11 files in (P) including BOTH K1 and K2.  Both
  are sealed, primary-root, and carry no mark the build declared as excluding.
CONSISTENCY = ALL-MATCH (sympy 1.14.0, fresh venv, exit 0; §9).
FENCES = alpha_computed false; proof_authorized false; kappa_record_computed
  false; no value, no number of physical import, no measured-constant comparison.
ACTS_TAKEN = NONE beyond determination.  Nothing proposed, authored, adopted,
  reclassified, or promoted.  No git.
SWEEP_CUTOFF = 2026-08-15, at the byte-states in §2.  Sweep legs pattern-bound
  and disclosed (§1); no corpus-wide existence or absence claim is made.
```

---

## §14 — VERDICT

```text
*** BOTH ARTIFACTS DO STATE ADMISSIBLE SETS THAT VARY ACROSS AN INDEX, AND IN
BOTH THE VARIATION IS DISPLAYED RATHER THAN MERELY ASSERTED.  NEITHER IS A
CONSTANT FAMILY.  THE PRIOR BUILD'S ABSENCE CLAIM IS FALSE AT BYTES. ***

But they are TWO DIFFERENT OBJECTS, and the difference is the finding:

  K1 indexes by a CARDINALITY computed from the thing being typed, and yields a
     SHAPE, not a literal set — the ambient moves with the index, and the index
     cannot be moved without moving the object.  An invariance over it is
     statable only in a form forced empty by the b_1 = 0 sector.  The two pieces
     that would give it content are missing, and K1 marks one of them UNSUPPLIED
     itself (F3) and the other BARRED (N1).

  K2 indexes by a SET OF CONDITIONS, and yields LITERAL CLASSES in one fixed
     ambient, comparable member by member.  An invariance over it is STATABLE,
     its domain is POPULATED with three exhibited values, and it has an EXHIBITED
     WITNESS (A5) and an exhibited invariant non-member (W1).  Nothing needed to
     STATE it is missing.  What is missing is only what would DETERMINE it:
     CLASS(II)'s full membership is never displayed.

*** THE SHARPEST WAY TO PUT THE DIFFERENCE: K1 has a genuine variation over an
index whose invariance question is ill-posed; K2 has a genuine variation over an
index whose invariance question is well-posed, statable, witnessed, and left
undetermined by the record.  A build that treats the two as one object — in
either direction — is wrong at bytes. ***

I STATE NO INVARIANCE, BUILD NOTHING, AND PROPOSE NOTHING.  DETERMINATION ENDS.
```

--- END OF ARTIFACT ---
