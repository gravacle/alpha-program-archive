# STAGE 8 — THE SALVAGE AUDIT (O56SR)

BUILD LANE · commissioned pair · READ AND CLASSIFY AT BYTES

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

Nothing was computed. No magnitude was approached. No successor design is
recommended, no asset is adopted, kept, or urged. This artifact reports, for
each asset, **what it rests on** — and whether that ground is this program's own
object or something a successor building a finite record carrier would
independently have.

Date: 2026-08-16. Output path probed ABSENT before first write.

---

## §0 — THE GRADE, AND WHAT IT IS NOT

The grades below are applied exactly as commissioned. **They are not quality
grades.** A CONSTRUCTION-DEPENDENT theorem may be true, proved, and audited; a
TRANSFERS-WHOLE constraint may be a single sentence.

```text
TRANSFERS-WHOLE            depends only on objects or facts a successor
                           building a finite record carrier would
                           independently have.  Dependence cited in every case.
TRANSFERS-AS-SPECIFICATION not a result but a statement of what some object
                           must do or be.
CONSTRUCTION-DEPENDENT     true, possibly proved, but about this program's
                           particular ground.  Ground named in every case.
DEPENDS-ON-A-WITHDRAWN-OR-UNBUILT-OBJECT
                           rests on something the corpus itself marks unbuilt,
                           withdrawn, defective, killed, or superseded.
INDETERMINATE-AT-BYTES     the bytes do not decide.
```

---

## §1 — SWEEP CUTOFFS, EXCLUSION GLOBS, LEAK COUNTER

Roots swept (all four permitted, supervision directories in full):

```text
R1  /Users/bgm/MB Work/alpha-program-archive
      (workspace · supervision · relay_inbox · relay_outbox · cleanroom_output)
R2  /Users/bgm/MB Work/alpha_supervision
R3  /Users/bgm/Documents/New project/gravity_emergence_evidence_program/
      alpha_fundamental_record_action_cleanroom_v003
```

EXCLUSION GLOBS AS AN ARRAY, with per-pattern hit counts and per-pattern leak
counter. Self-exclusion of this artifact is the sixth entry.

```text
BARRED = [
  'QUESTIONS_SETTLED_REGISTER'        hits  6   leak 0
  'QUESTIONSSETTLED_REGISTER'         hits  1   leak 0
  'EXECUTION_TRACKER'                 hits  4   leak 0
  'ROAD_REMAINING'                    hits  6   leak 0
  'RECORD_FORMATION_PROGRAM_DESIGN_'  hits  6   leak 0
  'STAGE8_SALVAGE_AUDIT_O56SR_V001'   hits  0   leak 0   (self-exclude)
]

TOTAL FILES IN THE FOUR ROOTS ......................... 23,863
SUM OF PER-PATTERN HITS (with overlap) ................      23
ALLOWED AFTER EXCLUSION ...............................  23,840
ALLOWED, NON-SIDECAR ..................................  17,875
ALLOWED .md ARTIFACTS (the population probed at §2) ...   6,930
*** TOTAL LEAK = 0 ***
```

`RECORD_FORMATION_PROGRAM_DESIGN_*` was excluded and never opened; its
exclusion is the commission's own anti-circularity rail (it is the registrar's
draft of the successor, so treating it as evidence of what should be salvaged
would be circular). No barred file was opened or quoted anywhere below. The
`Q-…` register tokens carried inside sealed artifacts are treated as opaque
labels — EXPECTED-UNLOCATABLE — because their register is barred.

**READ CUTOFF.** The graded assets below were opened and read at bytes. Files
consulted only for filename/locator resolution are not graded. Where a grade
rests on a span, the span is quoted whole, adverse clauses included.

---

## §2 — SIDECAR CONVENTION, PROBED IN BOTH FORMS

Both forms probed for every allowed `.md` artifact in all three roots:
`<stem>.md.seal.sha256` (the normalized form) and `<stem>.seal.sha256` (bare).

```text
ALLOWED .md ARTIFACTS ..................................... 6,930
CARRYING BOTH FORMS .......................................   299
CARRYING ONLY <stem>.md.seal.sha256 (normalized only) .....  4,784
CARRYING ONLY <stem>.seal.sha256 (BARE ONLY) ..............     55
CARRYING NEITHER (unsealed) ...............................  1,792
SIDECAR FILES WITH mtime 2026-08-16 .......................   334
```

**REPORTED AS COMMISSIONED — artifacts still carrying only one form: 4,839.**
Of those, 4,784 carry only the normalized form (which is the form the
convention requires, so they are compliant), and **55 carry ONLY the bare form
and therefore still lack the required `<stem>.md.seal.sha256`.** All 55 are in
two families:

```text
40  review_packets/STAGE7_QSPEC_CANDIDATE_V001/*   (15 files, mirrored in
                                                    R1/workspace and R3)
15  cleanroom_output/11_… through 45_…            (the archived fable
                                                    cleanroom OUTPUT set,
                                                    including 19_ and 45_ —
                                                    the two G3 carriers, §8)
```

The commission's premise was that 282 sidecars were added on 2026-08-16 by
copying verified bare-form sidecars. **At bytes the 2026-08-16 sidecar count in
the permitted roots is 334, not 282** — recorded as an arithmetic discrepancy,
not adjudicated here (the difference may lie in roots or classes outside this
count; INDETERMINATE-AT-BYTES).

**1,792 allowed artifacts carry no sidecar in either form.** This is not a
marginal set: it includes `BID_FINITE_RECORD_DURABILITY_NO_GO_V001.md` (the
single most transferable no-go in the corpus, §4.1) and
`LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md` (the U(1) bundle and connection, §6).
The prior commission recorded the same class in its own words —
`STAGE8_CELL_RECORD_CROSSING_O55SR_V001.md:120-121`: *"FOUR LOAD-BEARING FILES
CARRY NO SIDECAR IN EITHER FORM."*

---

## §3 — SEALS

`shasum -a 256 -c` run from each artifact's own directory, over every artifact
this audit cites as evidence.

```text
CITED ARTIFACTS ............................................ 25
VERIFIED OK by `shasum -c` from own directory ............... 23
VERIFIED OK by digest equality (sidecar carries a stale
  cross-root relative path, digest matches exactly) .......... 1
NO SIDECAR IN EITHER FORM ................................... 1
MISMATCHES .................................................. 0

*** SEALS = 24/25 VERIFIED · 0 MISMATCH · 1 UNSEALABLE ***
```

The one path-stale sidecar, displayed rather than glossed:

```text
FILE     workspace/STAGE8_TRACE_COLLAPSE_AND_GRAVITY_GAUGE_IMPOSSIBILITY_
           REGISTER_RECORD_V001.md
SIDECAR  c470b865…  gravity_emergence_evidence_program/alpha_fundamental_
           record_action_cleanroom_v003/STAGE8_TRACE_COLLAPSE_…_V001.md
ACTUAL   c470b865…  STAGE8_TRACE_COLLAPSE_…_V001.md
=> DIGEST MATCHES EXACTLY.  `shasum -c` fails only because the sidecar names a
   path relative to the OTHER root.  Content verified.
```

The one unsealable file, and the substitute check performed:

```text
FILE     BID_FINITE_RECORD_DURABILITY_NO_GO_V001.md
STATUS   NO SIDECAR IN EITHER FORM, IN EITHER ROOT.
SUBSTITUTE CHECK  both copies hashed at path and compared:
  R1/workspace/BID_FINITE_RECORD_DURABILITY_NO_GO_V001.md
  R3/BID_FINITE_RECORD_DURABILITY_NO_GO_V001.md
  BOTH = 2a13fde30c38bc2670d58ce870c9964527c4591651f5bc504371b26812b97124
  Cross-root byte-identity established.  This is corroboration of
  agreement between two copies, NOT seal verification.  Flagged §10.
```

---

## §4 — Q1: THEOREMS AND PROVED RESULTS

Each item: statement quoted, stated scope or ground, grade, and the explicit
answer to **is its ground this program's own object, or something a successor
would independently have?**

### §4.1 THE PARTITION THEOREM — `STAGE8_PARTITION_THEOREM_T16SR_V001.md` (seal OK)

The theorem is stated over `Σ` = the displayed equation set of the sealed
surface. **Σ IS THIS PROGRAM'S OWN OBJECT**, and the artifact says so in its own
scope clause, `:421-423`:

> "CURRENT GROUND ONLY. The theorem binds Σ AS SEALED — the displayed clause
> set of SURFACE_DEFINITION_OF_RECORD_V003.md at seal c80c09a2, enumerated
> in §1."

The corpus itself displays the theorem in three separately-proved parts with
**different premise sets**, and states at `:368` that "The require-half consumes
even less (one clause and algebra)." The parts are therefore graded separately,
as the bytes separate them.

```text
T-1  REQUIRE-HALF (I), :150-152, whole:
     "In EVERY model of Σ, the quantization class holds: every sector/winding
      label admissible under Σ4's single-valued closure lies in ℤ — exactly ℤ,
      no more — and the definitional pair {+1, −1} inhabits it."

     GROUND, at bytes: Σ4 alone plus exact algebra.  Σ4 is quoted at :83-84 —
     "CHARACTER MAP: z_j^(n) = χ_n(h_j[a_j]), unit modulus, with the
      definitional sector pair n ∈ {+1,−1}".
     The proof chain S1–S4 (:175-190) consumes: that phase data enter as U(1)
     characters; that h and h+2π present the same group point, so
     χ_n(h+2π) = χ_n(h); that exp(2πin) = 1; and that the full solution set of
     exp(2πi·x) = 1 is EXACTLY ℤ.

     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: the single-valuedness of a character of U(1), and the
     solution set of exp(2πix)=1 over ℂ (and over ℝ via the real closure
     component).  This is standard character theory of the circle group.  A
     successor that gives its record carrier ANY U(1)-valued phase comparison
     with integer-labelled characters has this fact without building anything
     of this program's.  The corpus's own §3.1 note makes the boundary exact:
     "the clauses force the CLASS and pin no member" (:199-200) — the class ℤ
     transfers; the member |n| does not (see T-11).
     GROUND IS: something a successor would independently have.

T-2  ALLOW-HALF (II), :153-157, whole:
     "In NO model of Σ is the crossing's magnitude forced: over every model of
      Σ, the expansion by profile f₁, the expansion by profile f₂, and the
      junction-free reduct are all again models of Σ, pairwise disagreeing on
      the junction — so Σ derives no response profile, no profile is pinned in
      any model, and the magnitude sits allow-side in every model, with the
      two-model witness uniform over the whole model class."

     GROUND: the VOCABULARY FACT about this sealed text — :208-209, "No clause
     of Σ carries any junction/response symbol; the response-NAMING clauses
     (D-3, D-4) carry no phase-sector symbol."  That is a fact about the
     seven displayed clauses of SURFACE_DEFINITION_OF_RECORD_V003 and nothing
     else.  The logical engine (S8's invariance lemma: "The satisfaction of a
     clause depends only on the interpretation of the clause's own vocabulary")
     is standard; the PREMISE it is applied to is this corpus's text.

     *** GRADE = CONSTRUCTION-DEPENDENT ***
     GROUND NAMED: the displayed clause set Σ1–Σ7 of
     SURFACE_DEFINITION_OF_RECORD_V003.md at seal c80c09a2 — this program's
     own sealed surface.  The theorem itself says a new displayed clause "is a
     CHANGE OF GROUND and re-poses" (:376).  A successor with a different
     surface has a different Σ and no claim here.
     GROUND IS: this program's own object.

T-3  EXCLUSIVITY (III), :159-163, whole:
     "No model of Σ places them otherwise: (a) no model places the
      quantization class allow-side; (b) no model places the magnitude
      require-side; (c) neither side can be re-read as the other — the class's
      output is an integer label, not a continuum response magnitude, and no
      clause of Σ exists through which a require-chain could reach a
      magnitude."

     *** GRADE = CONSTRUCTION-DEPENDENT ***  (same ground as T-2; (c2)
     explicitly consumes the vocabulary fact "no such clause exists on the
     sealed surface", :253-254).
     GROUND IS: this program's own object.
     ADVERSE CLAUSE CARRIED: sub-part (c1) — "the closure equation's solution
     set is a discrete label set" — is T-1's ground and transfers with it; the
     rest does not.

T-4  COROLLARY COR-2 (G = 1), :270-274:
     "On-record amplitude is uniquely trivial in every model: G·(native
      composite) on record forces G = 1"
     ITS NAMED EXTRA PREMISE, quoted from the same block: "Σ + D-2's DISPLAYED
     sentence — the carried-weight unit-modulus wording of SII.6".
     *** GRADE = CONSTRUCTION-DEPENDENT *** — ground: SII.6 of this program's
     sealed surface.  GROUND IS: this program's own object.
```

**RESIDUE DISPOSITION, carried because it is the theorem's own honesty rail.**
The artifact discharges both residues *for itself* (`:405-414`) — C12 by proven
non-consumption, the finite-text warrant by re-performed enumeration — but
displays exactly what C12 still conditions: the amplitude junction's *fuller*
vacancy claim, "specifically its withheld-content arm" (`:372-374`). That
survives as a conditionality on T-6 below, not on T-1..T-4.

### §4.2 THE VACANCY THEOREM — `STAGE8_AMPLITUDE_JUNCTION_S9AD_V001.md` (seal OK)

Artifact-level status at its own head, `:9-10`, carried because it is adverse:
*"Status of any output here: **PROPOSED-NOT-ADOPTED** — per the design's
acceptance note the result logs CLAIMED and is subject to the panel discipline;
nothing here is record."* Its audit (`STAGE8_AMPLITUDE_JUNCTION_S9AD_AUDIT_V001.md`,
seal OK) returns CONFIRMED-WITH-CORRECTIONS.

```text
T-5  THEOREM I (constant modulus), claim-ledger row K4 (:566):
     "Theorem I (constant modulus on the native algebra; triviality corollary)
      | DERIVED (CAS N1–N4, T1); refinement-stage step CONDITIONAL on C12"
     Verdict text, :26-27: routes through the native multiplicative algebra are
     "killed by proof (modulus identically 1 …)".
     GROUND: the native multiplicative algebra of THIS surface's write
     structure, and SII.6's wording.
     *** GRADE = CONSTRUCTION-DEPENDENT *** ; and its refinement-stage step is
     additionally CONDITIONAL on C12, a premise the corpus never discharges
     (§4.1 residue).  GROUND IS: this program's own object.

T-6  THEOREM II — THE VACANCY / TWO-MODEL CONSERVATIVITY THEOREM, K8 (:570):
     "Theorem II (two-model conservativity: no Class II candidate is forced)
      | DERIVED (CAS M1–M9; model exhibit; derivability ⇒ truth in all models)"
     The verdict statement it supports, :23-24 and :28-34, whole:
     "**VACANCY-CLOSED** — on the sealed ground and nothing else, no
      surface-native route yields a derived, β-invariant, magnitude-valued
      internal→external response junction on the write structure … routes
      adjoining non-displayed structure … killed by the two-model
      conservativity theorem — the ground's displayed equation set contains no
      clause linking any response magnitude to any phase datum (CAS M8), so
      two models of every displayed clause exist that differ on the junction
      (CAS M1–M9), hence no candidate profile is forced and every Class II
      construction necessarily carries an AUTHORED ingredient, which voids it
      as *derived*"
     ITS OWN SCOPE, quoted from the same span: "on the sealed ground and
     nothing else"; and "the closure is relative to exactly the named residue
     (§8.2: the C12 categorical-scope premise inherited from the I-2 pair, and
     the finite sealed text as the warrant for the displayed-operation
     enumeration)".
     *** GRADE = CONSTRUCTION-DEPENDENT ***
     GROUND NAMED: the sealed ground — this program's own displayed equation
     set — plus an undischarged C12 premise (K10 is marked "CONDITIONAL (C12)"
     at :572).  GROUND IS: this program's own object.

T-7  ROUTE-PARTITION TOTALITY, K3 (:565):
     "Route partition I/II/III is total; its inventories are derived | DERIVED
      (§3; definition + finite-text enumeration + I-2 corrected inventory)"
     *** GRADE = CONSTRUCTION-DEPENDENT *** — the enumeration's warrant is
     "the finite sealed text", i.e. this corpus's own bytes.
     GROUND IS: this program's own object.

T-8  THE SUPPLY-ROUTE SHARPENING, K12 (:574):
     "Supply requires a change of ground: exit operation + forcing equation,
      jointly | DERIVED (Theorem II sharpening, §8.3)"
     *** GRADE = TRANSFERS-AS-SPECIFICATION *** — this is not a result about
     the world; it is a statement of what a would-be junction-supplying object
     MUST contain (two things, jointly: an exit operation AND a booked clause
     "in which a response magnitude and phase-sector data co-occur",
     PARTITION:429-431).  Useful to a successor as a requirements line even
     though the ground it was derived over does not transfer.
```

### §4.3 THE FOUNDING IDENTITY: ALPHA-FORCING ↔ FAITHFULNESS
`STAGE8_NEUTRAL_COMPARAND_FAITHFULNESS_FABLE_V001.md` (seal OK)

```text
T-9  THE IDENTITY ITSELF, :215-218, whole:
     "weak distinguishability  =  kernel not everything  =  n != 0   (bedrock,
                                 derived: the zero-variation / charge-flux-
                                 access elimination);
      FULL faithfulness        =  kernel trivial          =  |n| = 1  exactly."
     ITS GROUND, quoted from the sealed kernel ladder it cites (S1:15-47, read
     through this artifact's :210-213): the kernel of χ_n is "all of U(1) for
     n=0, the finite subgroup of |n|th roots of unity for |n|>1, and the
     identity alone for n=+1 or n=-1."
     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: the kernel ladder of the characters of U(1) — pure
     character theory of the circle group.  Nothing in the identity consumes
     this program's surface, action, carrier, or any adopted premise.  A
     successor with a U(1)-valued comparison and integer characters has the
     identity "faithfulness ⟺ |n| = 1" immediately.
     GROUND IS: something a successor would independently have.

T-10 UNIQUENESS-GIVEN-EXISTENCE, :355-357, whole:
     "Uniqueness-given-existence stands as pure structure (injectivity of
      squaring on nonnegative integers: an n-blind X admits at most one |n|)"
     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: injectivity of x ↦ x² on the nonnegative integers.
     Elementary arithmetic.  The artifact itself types it "pure structure".
     GROUND IS: something a successor would independently have.

T-11 THE STATUS VERDICT (what the identity is used for here), :346-352:
     "WINDING_FORCED_BY_NEUTRAL_OR_BOUNDARY = NOT-FORCED. … Route (B): full
      faithfulness is IMPOSED, not forced (§4.6), so it may not be consumed to
      pin |n| under this tasking's own standard"
     and the custody line at :289-291 naming the premise's provenance:
     "TYPE-P | premises: DoR-008, DoR-009 — the ratified faithful …
      RATIFICATION (a principal act)".
     *** GRADE = CONSTRUCTION-DEPENDENT ***
     GROUND NAMED: this corpus's derived content and its ratified premises
     (DoR-008/DoR-009).  The verdict "the record's derived content does not
     force |n|" is a statement about THIS record.  A successor's record could
     force it or not; the bytes decide nothing about a different one.
     **AUTHORED-PREMISE FLAG:** faithfulness enters this program by
     RATIFICATION, not derivation — the artifact says so at :356 ("IMPOSED,
     not forced") and locates the act at DoR-008/009.  See §6, A-6.
     GROUND IS: this program's own object.
     ADVERSE CLAUSE CARRIED (:365-368): "IT DOES NOT negate the sealed |n| = 1
     result … That result runs on the ratified faithfulness premise and stands
     of record AS a ratified-premise result (TYPE-P)."
```

### §4.4 THE TRACE COLLAPSE THEOREM AND THE GRAVITY/GAUGE RATIO IMPOSSIBILITY
`RESULT_TRACE_COLLAPSE_THEOREM_AND_GRAVITY_GAUGE_IMPOSSIBILITY_2026-07-29.md`
(R2, seal OK) · register record `STAGE8_TRACE_COLLAPSE_AND_GRAVITY_GAUGE_IMPOSSIBILITY_REGISTER_RECORD_V001.md`
(R1, digest-verified)

**This is the one place where the commission's suspicion is confirmed at bytes:
the ground is representation theory, not this program's construction.**

```text
T-12 THE TRACE COLLAPSE THEOREM, :9-14, whole:
     "Let `X, Y in gl(N,C)` with AT LEAST ONE traceless. For the derivation
      action on `Lambda^k(C^N)`:
        Tr_{Lambda^k}(XY) = C(N-2, k-1) * Tr_fund(XY)          [one traceless]
        Tr_{Lambda^k}(XY) = C(N-2, k-1) * Tr_fund(XY)
                            + C(N-2, k-2) * (Tr X)(Tr Y)       [general]"
     ITS OWN STATED PROOF GROUND, :21-26, whole:
     "CARTAN IS NOT REQUIRED. `(X,Y) |-> Tr_{Lambda^k}(dX dY)` is a `GL(N)`-
      invariant symmetric bilinear form on `gl(N)`. Since
      `gl(N) = sl(N) + center` with `sl(N)` adjoint-irreducible, Schur gives a
      2-dimensional space of such forms spanned by `Tr(XY)` and `(Tr X)(Tr Y)`.
      The identity therefore holds for ALL `X,Y`, non-commuting included.
      Verified the hard way by building full derivation matrices for generic
      non-commuting rational traceless `X,Y` at `N = 3,4,5,6`, every `k`: exact
      match every case."
     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: Schur's lemma applied to the adjoint-irreducible sl(N)
     inside gl(N), plus exterior-power weight combinatorics and Pascal's
     identity (:16-18).  No object of this program appears in the hypotheses.
     The artifact's own §3 records that the identity ALREADY EXISTS in three
     independent layers of this program's trees and was re-derived because the
     reviewer lane lost it (:76-78) — i.e. the corpus itself treats it as a
     standing mathematical fact, not a construction.
     GROUND IS: something a successor would independently have — and would in
     fact have from the mathematics literature without this program at all.
     CARRIED HYPOTHESES, verbatim from :260-263: "at least one generator
     traceless; the carrier a genuine representation of the simple algebra;
     the threshold weighting admissible level-set by level-set; and, in the
     corpus's construction, the Chevalley return map unitary. THE CORPUS'S OWN
     `|H|` FLUX-SECTOR DECOMPOSITION VIOLATES THE THIRD, EXHIBITED IN §5."

T-13 THE SECOND-MOMENT CRITERION (the honest collapse condition), :96-102:
     "Writing the condition as: the second-moment tensor `sum_s w_s mu_s (x)
      mu_s` must be proportional to the Cartan metric, the admissible
      weightings form a **7-dimensional subspace** of the 16-dimensional
      weighting space (codimension 9 …). Enumerating all `2^16` level sets:
      exactly **27 nonempty admissible subsets**, of which only 7 are unions
      of whole `Lambda^k` blocks. … THE HONEST CRITERION IS THE SECOND-MOMENT
      CONDITION, NOT CLASS-FUNCTIONHOOD."
     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: linear algebra on the weight lattice of su(5) and a
     finite exhaustive enumeration over 2^16 subsets.  A successor with any
     su(N) carrier has the criterion by the same argument; the numbers 7, 27,
     16 are specific to Λ^even(C^5) but the CRITERION is not.

T-14 THE GRAVITY/GAUGE RATIO IMPOSSIBILITY ON THE NAMED CARRIER, :165-170,
     whole:
     "**THE CONTRADICTION LOCALISES ENTIRELY ON `Lambda^0`, AND THAT IS THE
      STRUCTURAL CONTENT: THE SINGLET HAS DIMENSION 1 BUT INDEX 0.** The gauge
      sector is blind to it; every gravitational coefficient sees it. The
      sectors are weighted by two LINEARLY INDEPENDENT functionals on the
      representation ring — `dim` and `index` (minors of `[d; t]` are
      `3, 1, -5`). Any construction on this carrier is therefore FORBIDDEN
      from producing an x-independent gravity-to-gauge ratio, no matter how
      the thresholds are arranged."
     THE PROOF ENGINE, :160-163, whole:
     "`I_1(x+c) = E_1(x+c)` has a logarithmic branch point at `x = -c` and is
      analytic elsewhere; the three shifts `0, 12/5, 18/5` are distinct, so the
      three functions are LINEARLY INDEPENDENT. The coefficient of `I_1(x)`
      must vanish: `1/23040 = 0`. CONTRADICTION. No evaluation at any depth is
      involved."

     *** GRADE = TRANSFERS-WHOLE, WITH ONE NAMED CARRIED HYPOTHESIS ***
     DEPENDENCE CITED, in three parts, all of them standard:
       (i)  `dim` and `index` are linearly independent functionals on the
            representation ring of a simple algebra, and the trivial summand
            has dim 1 / index 0 — representation theory;
       (ii) `E_1(x+c)` at distinct shifts are linearly independent, by the
            distinct branch points — standard complex analysis;
       (iii)the named carrier Λ^even(C^5) with `d = (1,10,5)`, `t = (0,3,1)`
            — a standard su(5) carrier, not an object this program built.
     THE ONE HYPOTHESIS THAT IS THIS PROGRAM'S, named exactly and NOT hidden,
     :137-138: "Every coefficient in this construction has the form (rational
     tensor constant) x `sum_a w_a I_n(x + C2_a)`".  That coefficient FORM is
     this program's induced-coefficient construction.
     => A successor that adopts a carrier with a trivial summand and coefficients
     of that spectral form inherits the no-go WHOLE.  A successor whose
     coefficients do not have the `sum_a w_a I_n(x + C2_a)` form does not
     inherit the impossibility, but DOES inherit (i) and (ii) as the
     obstruction's structural core.
     GROUND IS: something a successor would independently have — this is the
     one theorem in the corpus whose engine is entirely outside the program.
     WHAT IT DOES NOT GIVE, carried verbatim from :237-241: "No coupling, no
     depth, no absolute normalisation. `S(x)` is entirely unconstrained by any
     of this, and one unknown function projected three ways is still one
     unknown function."

T-15 THE LIVE COUNTEREXAMPLE INSIDE THE PROGRAM'S OWN OPERATOR, :116-119:
     "NEITHER SECTOR GIVES `(3/2, 1)`. In the `|H|=0` sector `K_H` and `K_QH`
      VANISH OUTRIGHT. Both indicator vectors are INADMISSIBLE under the
      second-moment criterion. So if the induced action is ever assembled flux-
      sector by flux-sector with sector-dependent weights — WHICH IS HOW THE
      CORPUS'S OWN OPERATOR IS CONSTRUCTED — the collapse fails and the ratios
      become x-dependent."
     *** GRADE = CONSTRUCTION-DEPENDENT ***
     GROUND NAMED: `derive_alpha_br_homogeneous_operator_pullback_v001.py`'s
     `internal_abs_h_block(flux_degree)` decomposition — this program's own
     operator.  The FINDING is a defect report against this construction.
     GROUND IS: this program's own object.
```

### §4.5 THE BUNDLE RESULTS — `LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md`
**NO SIDECAR IN EITHER ROOT — UNSEALED, and so marked wherever quoted.** The
prior commission recorded the same at `STAGE8_DISCREPANCY_COCYCLE_O38SR_V001.md`
row 17: *"NO SIDECAR IN EITHER ROOT — UNVERIFIABLE"*.

```text
T-16 THE TRIPLE-OVERLAP COCYCLE AND THE LINE BUNDLE, :27-43, whole span:
     "Two lifts represent the same local ray exactly when, on an overlap,
        z_j = g_ij z_i,
        g_ij = exp(i theta_ij) in U(1).
      On triple overlaps, equality of the represented ray requires
        g_ij g_jk g_ki = 1.
      The local lifts and transition functions therefore define a complex line
      bundle, equivalently a principal `U(1)` comparison bundle. This `U(1)` is
      a local representative redundancy of the adopted projective record field.
      It is not obtained by mistaking a passive basis change for a new physical
      force."
     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: the standard cocycle construction of a complex line
     bundle from U(1)-valued transition functions on overlaps of a cover.  The
     derivation consumes only: rays in a complex two-dimensional carrier,
     normalized local lifts, and the requirement that lifts represent the same
     ray.  Any successor whose record degree is a RAY in a complex carrier
     obtains exactly this, by the same three lines.
     GROUND IS: something a successor would independently have.
     WHAT IS THIS PROGRAM'S AND IS NOT PART OF THE TRANSFER: the antecedent
     "The new principle places one primitive record degree on every admissible
     causal record cell" (:18-19) is an ADOPTED PREMISE of this program (the
     sealed Fundamental Boundary Record Action Principle, cited at :8).  The
     cocycle transfers; the premise that there IS such a ray field does not.
     The artifact types itself accordingly at :13-14: "It is therefore a
     Level-1 result under the newly adopted microscopic principle."

T-17 THE COMPARISON CONNECTION, :47-79, whole span:
     "Ordinary derivatives of different local lifts do not patch:
        d z_j = g_ij (d z_i + i d theta_ij z_i).
      Introduce local one-forms `a_i` and
        D_i = d - i a_i.
      The derivatives patch covariantly,
        D_j z_j = g_ij D_i z_i,
      if and only if
        a_j = a_i + d theta_ij.
      Thus a connection on the projective record bundle is required by the
      adopted local covariant-comparison clause. Its curvature
        f|U_i = d a_i
      is globally defined because `d^2 theta_ij = 0`."
     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: the standard iff-characterization of a connection on a
     U(1) bundle by the gauge-transformation law of local one-forms, and the
     global well-definedness of the curvature from d² = 0.  Standard
     differential geometry, consuming no object of this program beyond the
     bundle of T-16.
     ADVERSE CLAUSE CARRIED, :96-102: "Connections on a fixed line bundle form
     an affine space. Bundle geometry does not choose one `a`, one curvature,
     or one kinetic coefficient. The sealed microscopic principle makes `a`
     auxiliary and sets `K_bare = 0`."  The bundle transfers; NOTHING DYNAMICAL
     comes with it, and the artifact says so.
     Status flags at :128-133 confirm: `unique_connection_selected = false`,
     `dynamical_public_connection_derived = false`,
     `unique_induced_Maxwell_stiffness_derived = false`,
     `identification_with_exterior_EM_derived = false`.

T-18 THE HOLONOMY CHARACTER, :84-92, whole:
     "For a closed comparison path `gamma`, the primitive integer character
      gives
        W_n(gamma) = exp(i n integral_gamma a),
        n in Z.
      The primitive faithful winding is inherited conditionally as `|n|=1`.
      This establishes the normalization of the comparison character. It does
      not establish a spectrum of elementary matter particles."
     *** SPLIT GRADE, because the bytes split it ***
     The formula W_n = exp(in∮a) with n ∈ ℤ: **TRANSFERS-WHOLE** — it is T-16's
     bundle plus T-1's integer character class; dependence is U(1) character
     theory and the holonomy of a connection.
     The clause "`|n|=1`": **CONSTRUCTION-DEPENDENT** — the artifact itself
     says it is "inherited conditionally", and §4.3's T-11 locates the
     condition as this program's RATIFIED faithfulness premise (DoR-008/009),
     not a derivation.
```

### §4.6 FURTHER PROVED RESULTS, GRADED

```text
T-19 DoR-019 DERIVED CORE (carrier metric), quoted from
     DOR_019_CARRIER_METRIC_AND_UNITS_RATIFICATION_2026-08-03.md:10-20:
     "DERIVED CORE (in force as theorems): the forced pullback semiform
      s_G(c,d) = g_A4(u_c, u_d); family-wide FULLNESS (A2-R10 forces
      image(L_G)+image(B_G) = E_G, hence ker(I_K) = 0 — the semiform is
      positive definite on the FULL carrier; every record-visible cycle
      carries nonzero current); the W3 rank-preserving isometry; the finite
      C-side metric, R_C, and quotient-norm formula; the C/K unit-duality
      classes with U_A^-2 Riesz duals"
     *** GRADE = CONSTRUCTION-DEPENDENT *** — every object named (E_G, L_G,
     B_G, I_K, A4, W3, the R4 seam) is this program's constructed carrier
     apparatus.  GROUND IS: this program's own object.
     Its own AUTHORED list, quoted from :22-25, is recorded at §6 A-8.

T-20 THE FORK-8 DIRECT LIMIT RESULT — see §7, B-1.  It is both a proved result
     and the corpus's one built crossing; it is graded once, there.

T-21 THE MEMBERSHIP THEOREM (EQ6) — `STAGE8_TASK5_EQ6_MEMBERSHIP_THEOREM_LANE3_V001/2`.
     Consumed here only through the O38SR census, which records at bytes:
     "Lane theorem build; every claim tagged `[PROVABLE]`, not adopted."
     *** GRADE = INDETERMINATE-AT-BYTES *** for transfer: the theorem was not
     opened in full by this commission, and its own typing is a lane tag, not a
     record status.  Recorded so the gap is visible rather than silent.

T-22 THE PLANE-COVERAGE THEOREM — `STAGE8_TASK3D_PLANE_COVERAGE_THEOREM_V001.md`
     (seal OK).  Its own road standing, :7, whole: "**UNBLOCKS THE FINITE
     PLANE-FAMILY FORM OF STEP 3, CONDITIONAL ON THE DECLARED REDUCED CARRIER.**"
     *** GRADE = CONSTRUCTION-DEPENDENT *** — ground named by the artifact
     itself: "the declared reduced carrier".  GROUND IS: this program's object.

T-23 THE PRE-ROOT HIGHER-DERIVATIVE EQUIVALENCE THEOREM
     (`STAGE8_PRE_ROOT_HIGHER_DERIVATIVE_EQUIVALENCE_THEOREM_V001.md`, seal OK).
     Its own role line, :3: "Road role: UNBLOCKS STEP 3 conditionally."
     *** GRADE = CONSTRUCTION-DEPENDENT *** — it is an equivalence between two
     presentations of this program's own pre-root object.

T-24 THE CELLULATION-INDEPENDENCE / O-D3 VERDICT-INVARIANCE THEOREM
     (`STAGE8_TASK4D_…_V001.md`, seal OK).  Its own lead determination, :5 and
     :11-12, whole: "Status: RESULT / MAXIMAL INVARIANCE THEOREM PROVED / O-D3
     NOT DISCHARGED" … "**The Q-241 move proves a maximal kinematic theorem,
     but it does not discharge cellulation independence or charter O-D3.**"
     *** GRADE = CONSTRUCTION-DEPENDENT *** on this program's cellulation and
     charter O-D3; and its stated obligation (cellulation independence) is
     UNDISCHARGED by the artifact's own words.
```

### §4.7 RESULTS THAT DID NOT CLOSE (enumerated so the theorem count is honest)

```text
T-25 TARGET-INDEPENDENT LOCALIZATION THEOREM.  Its own verdict line, :302:
     "TARGET_INDEPENDENT_LOCALIZATION_BUILD_VERDICT = BLOCKED_BY_MISSING_CANONICAL_BRIDGE"
     *** GRADE = DEPENDS-ON-A-WITHDRAWN-OR-UNBUILT-OBJECT ***
     OBJECT NAMED: the canonical bridge, marked missing by the artifact itself.

T-26 P5-FAMILY EXCLUSION THEOREM.  Its own status line, :7:
     "Status: FORCING PROTOCOL EXECUTED THROUGH COVERAGE; STOPPED AT STEP 4"
     *** GRADE = DEPENDS-ON-A-WITHDRAWN-OR-UNBUILT-OBJECT *** (the theorem is
     not closed; the artifact's filename carries "ATTEMPT").

T-27 GEN_OMEGA NON-CIRCULAR GENERATIVITY NO-GO.  Its own status, :5, and
     verdict, :481: "Status: RESULT -- UNIVERSAL NO-GO REFUTED BY A NAMED
     CONDITION" · "VERDICT = NO-GO FAILS AT A NAMED CONDITION"
     *** GRADE = TRANSFERS-AS-SPECIFICATION *** — what survives is not a no-go
     but the NAMED CONDITION at which a universal no-go of that shape fails;
     that is a requirements statement about any successor attempt of the same
     shape.  See §5, N-7.
```

**Q1 TALLY.** 27 entries (T-1..T-27). T-20 is a cross-reference only and is
graded once, at §7 B-1. T-18 is split by the bytes and is counted on both sides.

```text
TRANSFERS-WHOLE .............................................  9
   T-1, T-9, T-10, T-12, T-13, T-14, T-16, T-17, T-18a
TRANSFERS-AS-SPECIFICATION ..................................  2
   T-8, T-27
CONSTRUCTION-DEPENDENT ......................................  13
   T-2, T-3, T-4, T-5, T-6, T-7, T-11, T-15, T-18b (the |n|=1
   clause), T-19, T-22, T-23, T-24
DEPENDS-ON-A-WITHDRAWN-OR-UNBUILT-OBJECT ....................  2
   T-25, T-26
INDETERMINATE-AT-BYTES ......................................  1
   T-21
GRADED ELSEWHERE (cross-reference) ..........................  1   (T-20)
```
(Exact itemization, with duplicates collapsed across questions, is at §11.)

---

## §5 — Q2: NO-GOS, IMPOSSIBILITIES, AND GENERAL CONSTRAINTS

**A no-go that holds of any construction of this class is the most valuable
salvage there is.** Each entry states, precisely, WHAT CLASS OF CONSTRUCTION IT
BINDS.

### §5.1 THE FINITE-RECORD DURABILITY NO-GO — the commission's named item
`BID_FINITE_RECORD_DURABILITY_NO_GO_V001.md` · **UNSEALED IN BOTH ROOTS**
(digest `2a13fde3…`, cross-root byte-identity established, §3)

The artifact has two distinct halves with two distinct grounds, and the corpus
itself sets them under two headings. **Both are quoted whole.**

```text
N-1  THE GENERAL FINITE-SYSTEM BOUNDARY.  Heading "## General finite-system
     boundary", :57-58, whole:

       "Adding a finite number of closed unitary record degrees does not by
        itself establish irreversible persistence. A finite discrete spectrum
        is recurrent."

     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: the recurrence of unitary evolution generated by an
     operator with finite discrete spectrum.  This is a standard fact of
     finite-dimensional spectral theory — a finite set of eigenphases makes
     exp(-i t H) return arbitrarily close to the identity, so no state written
     is permanently lost or permanently held.  It consumes NOTHING of this
     program: no surface, no carrier, no cell, no adopted principle, no
     ratified premise.  A successor writes the same sentence about its own
     object the moment that object is finite-dimensional and closed.
     GROUND IS: something a successor would independently have.

     *** THE CLASS IT BINDS, STATED PRECISELY ***
     It binds EVERY construction in which the durable record is carried by a
     CLOSED system with FINITELY MANY unitary degrees of freedom — i.e. whose
     record dynamics is generated by an operator with finite discrete
     spectrum.  It does NOT bind: constructions with an infinite limit,
     constructions with an exact superselection sector, constructions with an
     open-system (non-unitary) reduction, or constructions in which the record
     is not carried by the evolving degrees at all.  Those four exclusions are
     not this audit's gloss; they are the artifact's own next four lines
     (N-2).
     It is a NO-GO ABOUT FINITE CLOSED UNITARITY, not about this program's
     cell.  That is what makes it the corpus's most transferable asset.

     *** THE MOST VALUABLE SALVAGE IN THE CORPUS CARRIES NO SEAL IN EITHER
         FORM, IN EITHER ROOT.  FLAGGED §10. ***

N-2  THE FOUR ADMISSIBLE COMPLETION MECHANISMS, :60-67, whole:

       "A completed record can nevertheless be durable if the full action
        derives one of:

          an exact superselection/central sector;
          an invariant post-write pointer algebra;
          an infinite causal/environmental limit with asymptotic outgoing
            sectors;
          or a derived open-system limit from a larger unitary theory.

        These mechanisms are physically inequivalent and may not be selected
        after a response is evaluated."

     *** GRADE = TRANSFERS-AS-SPECIFICATION ***
     This is not a result; it is a statement of what an object must BE for a
     finite-record construction to escape N-1.  It is a four-way requirements
     menu plus an anti-fitting rule ("may not be selected after a response is
     evaluated") that binds the ORDER OF WORK, not the physics.  A successor
     inherits it as a requirements document regardless of whether any of this
     program's ground survives.
     ONLY ONE OF THE FOUR WAS EVER BUILT.  `STAGE8_CELL_RECORD_CROSSING_
     O55SR_V001.md:439-441`, whole: "Fork 8 built the THIRD.  The other three
     remain unbuilt."

N-3  THE STANDING DEMAND ON ANY SUCCESSOR CONSTRUCTION, :76-79, whole:
       "The next candidate must extend the same target-independent incidence
        law to a causal direct limit and prove that a completed record becomes
        an asymptotic recoverable sector. Merely increasing the finite cell
        count or calling orthogonality durability does not pass."
     *** GRADE = TRANSFERS-AS-SPECIFICATION ***, with one caveat displayed:
     the FIRST clause names "the same target-independent incidence law" — this
     program's object — so that clause is construction-bound; the SECOND
     clause ("merely increasing the finite cell count … does not pass") is a
     general bar following directly from N-1 and transfers with it.

N-4  THE ONE-CELL COMPUTATION, :20-53.  Its content, whole:
       "U(tau_R)|r> = |p>, U(tau_R)|p> = |r>, U(2 tau_R) = I. …
        Thus the exact operation that writes the first orthogonal endpoint
        erases it one equal interval later. The endpoint projector also fails
        the nondemolition condition: [c_partial, |p><p|] != 0.
        The one-cell operator therefore provides a reversible write, not a
        durable record."
     *** GRADE = CONSTRUCTION-DEPENDENT ***
     GROUND NAMED: the exact one-cell BID incidence Hamiltonian `c_partial`
     with spectrum {−√2, 0, +√2} and `tau_R = pi/sqrt(2)` — this program's
     particular cell operator.  The NUMBERS are this program's; the LESSON is
     N-1's, and N-1 does not need them.
     GROUND IS: this program's own object.
```

### §5.2 THE GRAVITY/GAUGE RATIO IMPOSSIBILITY (graded at §4.4, T-14)

Restated here because it is a no-go and belongs in this census. **CLASS IT
BINDS:** any construction on a carrier that is a direct sum of representations
of a simple algebra containing a trivial summand, whose sector coefficients
have the form (rational constant) × Σ_a w_a I_n(x + C2_a) with the gauge sector
weighted by `index` and the gravitational sector by `dim`. Within that class no
x-independent gravity-to-gauge ratio exists, by linear independence of the
E_1 shifts and the linear independence of `dim` and `index` as functionals on
the representation ring. **GRADE = TRANSFERS-WHOLE** on (i)+(ii)+(iii) of §4.4,
with the coefficient FORM named as the one carried hypothesis that is this
program's.

What it explicitly does NOT foreclose, verbatim, `:183-185`:

> "DOES NOT foreclose: the ratio route itself, which already carried
> `DEPTH_OPEN` on its face. The result converts an open condition into a PROVEN
> necessity — depth selection is not a gap to be filled opportunistically, it is
> unavoidable."

### §5.3 THE SOURCE-SCALARIZATION NO-GO
`STAGE8_T7_SOURCE_SCALARIZATION_NO_GO_RESULT_V001.md` (seal OK)

Verdict, `:8`: `PRIMITIVE_SOURCE_SCALARIZATION_BLOCKED`. It contains **three
separable arguments with three different grounds**, and the artifact separates
them itself as N1/N2/N3.

```text
N-5  THE INFINITE-TRACE OBSTRUCTION (N3), :69-85, whole:
       "The physical source carrier is not canonically finite-dimensional. On
        infinite-dimensional `B(H)`, two isometries with orthogonal ranges
        obey:
          V_i^dagger V_i=I;
          V_1 V_1^dagger+V_2 V_2^dagger=I.
        A normalized tracial state would imply:
          1=Tr(I)=Tr(V_1V_1^dagger)+Tr(V_2V_2^dagger)=1+1=2.
        Hence no normalized tracial state exists on the full infinite source
        algebra. The finite normalized trace is regulator-specific and cannot
        be promoted to the continuum scalarization."
     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: the standard two-isometries-with-orthogonal-ranges
     argument on B(H) — three lines of C*-algebra, consuming no object of this
     program.  A successor that wants a normalized trace on an infinite record
     or source algebra meets exactly this wall.
     *** CLASS IT BINDS: any construction that tries to reduce an
     operator-valued response on an infinite-dimensional algebra to a scalar
     via a normalized tracial state.  That class is not this program's; it is
     defined by the algebra's infinite-dimensionality alone. ***

N-6  THE FINITE-COVARIANCE UNIQUENESS (N2), :38-51, whole:
       "For a complex-linear functional on `M_d(C)` invariant under all
        unitary source-basis changes, matrix-unit covariance gives:
          C(E_ij)=0, i!=j;  C(E_ii)=C(E_jj);  C(I)=1.
        Therefore the unique finite-dimensional functional is:
          C(K)=Tr(K)/d."
     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: unitary invariance of a linear functional on M_d(C).
     Standard.  Adverse clause carried, :63-65: "If covariance is restricted to
     a smaller physical symmetry group, the functional is less constrained and
     multiple source-state functionals survive. That does not restore
     uniqueness."
     CLASS IT BINDS: any construction demanding a basis-independent scalar
     readout of a finite matrix response — the answer is forced to be the
     normalized trace, and nothing else is available.

N-7  N1 AND THE VERDICT'S APPLICATION, :11-20 and :22-34.
     "The actual connected parent and completed-record effect determine an
      operator on the source carrier, not one complex scalar. The current
      primitive authorities do not supply a target-free, regulator-independent
      functional …"  with its own scope disclaimer, :17-20, carried:
      "This is a scope result. It does not say that no physical scalar
       amplitude exists."
     *** GRADE = CONSTRUCTION-DEPENDENT ***
     GROUND NAMED: "the sealed completed `11` compression … full rank on the
     12-dimensional finite source regulator" — this program's sealed
     compression object and its regulator.  The witness numbers (Frobenius
     norm; distance from scalar identity) are numbers OF THIS CONSTRUCTION.
     GROUND IS: this program's own object.

N-8  THE EXHAUSTED CLOSURE CLASSES, :89-108, whole block ("source
     vector/covector … requires physical source boundary data; source
     density-state expectation … requires the physical incoming source state;
     finite normalized trace … no canonical continuum extension; determinant
     … nonlinear and quarantined; inclusive equal-branch sandwich … phase
     blind; operator-valued primitive response … well typed, but moves the
     scalar logarithm and coupling extraction to complete Q_spec").
     *** GRADE = TRANSFERS-AS-SPECIFICATION *** — a six-way menu of
     scalarization routes with the cost of each named.  Four of the six costs
     (boundary data, incoming state, no continuum extension, phase blindness)
     are properties of the ROUTE, not of this program, and a successor faces
     the same menu.
```

### §5.4 THE GEN_OMEGA NO-GO THAT FAILED, AND WHY THAT IS AN ASSET
`STAGE8_GEN_OMEGA_NONCIRCULAR_GENERATIVITY_NO_GO_ATTEMPT_V001.md` (seal OK)

```text
N-9  Its own status and verdict, :5 and :481:
       "Status: RESULT -- UNIVERSAL NO-GO REFUTED BY A NAMED CONDITION"
       "VERDICT = NO-GO FAILS AT A NAMED CONDITION"
     *** GRADE = TRANSFERS-AS-SPECIFICATION ***
     A REFUTED universal no-go is a specification in disguise: it tells a
     successor exactly which condition must be supplied for the corresponding
     construction to be possible.  The value is the NAMED CONDITION, not the
     failed no-go.  Its own header carries the custody clause: "It adopts no
     channel condition and does not authorize DoR-013."
```

### §5.5 THE PRODUCTION-GATE NO-GO AND ITS DEFECT CLASS
`STAGE8_T7_PRODUCTION_GATE_NOGO_AND_PIPELINE_REPAIR_BINDING_V001.md` (seal OK)

```text
N-10 The named defect class, :14-17, whole:
       "VERSION-BUMP DESYNCHRONIZATION — detected only at the enforcement point
        AFTER path consumption, with tests stubbed at exactly the failing seam."
     and its prescription A1/A2, :24-40 ("Every generation pin in the chain …
     is enumerated in ONE SEALED TABLE PER GENERATION, and a MECHANICAL CHECK
     verifies they all name the SAME generation BEFORE any lane runs. Six
     cycles have each been one pin lagging one bump." · "FULL REAL-CHAIN
     REHEARSAL, NO STUBS ANYWHERE.").
     *** GRADE = TRANSFERS-AS-SPECIFICATION ***
     This is a process constraint, not a physics result, and it is stated in
     terms (generation pins, launchers, manifests, stubs) that any successor
     running a multi-lane sealed pipeline will have.  Its evidential weight is
     the count: SIX CYCLES OF ONE DEFECT CLASS.
```

### §5.6 THE CONSTRAINT THAT BINDS EVERY MAGNITUDE ROUTE ON THIS SURFACE

```text
N-11 The AJ's FORCED-vs-AUTHORED localization table, S9AD:591-597, read as a
     constraint: for each of the three route classes it names "the ingredient
     necessarily AUTHORED".  Its own framing, :599-601, whole:
       "An authored ingredient presented as forced would void a candidate; here
        the closure shows every would-be candidate REQUIRES one — that is the
        vacancy, proven."
     *** GRADE = CONSTRUCTION-DEPENDENT *** (the route inventory is over THIS
     surface's displayed operations), **but the DISCIPLINE it encodes — locate
     where the authored ingredient necessarily sits, per route class — is
     method, graded at §8, M-2.**
```

**Q2 TALLY (11 items).**

```text
TRANSFERS-WHOLE .............................. 4   (N-1, N-5, N-6, and T-14
                                                   restated at §5.2)
TRANSFERS-AS-SPECIFICATION ................... 5   (N-2, N-3, N-8, N-9, N-10)
CONSTRUCTION-DEPENDENT ....................... 3   (N-4, N-7, N-11)
DEPENDS-ON-A-WITHDRAWN-OR-UNBUILT-OBJECT ..... 0
INDETERMINATE-AT-BYTES ....................... 0
```
(N-3 is split in its own entry — first clause construction-bound, second clause
transfers; it is counted once, as SPECIFICATION, with the split displayed.)

---

## §6 — Q3: THE ADOPTED OBJECTS (all 28 ratified rulings, both prefixes)

**BOTH PREFIXES ENUMERATED. 14 + 14 = 28.** Each ruling exists as a mirror pair
(`alpha-program-archive/supervision/` and `alpha_supervision/`); the pair is one
ruling and is counted once. Two rulings — DoR-020-A4 and DoR-020-A5 — are
recorded here as ABSENT-FROM-ONE-CONSUMER'S-VIEW by a prior commission and that
adverse finding is carried at §10.

```text
PREFIX `DOR_NNN_…`  (14)
  DOR_016_NETWORK_SOURCING_LAW_RATIFICATION_2026-08-03
  DOR_017_ACTION_COMPARISON_SQUARE_N_MEMBER_RATIFICATION_2026-08-03
  DOR_018_N_MEMBER_JETS_SHAPE_K_RATIFICATION_2026-08-03
  DOR_019_CARRIER_METRIC_AND_UNITS_RATIFICATION_2026-08-03
  DOR_020_CONTINUUM_PACKAGE_CONDITIONAL_RATIFICATION_2026-08-04
  DOR_020_A1_WHERE_CLAUSES_AMENDMENT_2026-08-04
  DOR_020_A2_COMPLETED_EXISTENCE_ADOPTED_2026-08-06
  DOR_020_A3_J4_RELATIONAL_INCREMENT_GROUPOID_2026-08-04
  DOR_020_A4_J12_CONTACT_GLUE_STRICT_PUSHOUT_2026-08-04
  DOR_020_A5_CONTACT_LAPLACIAN_REDUCING_2026-08-04
  DOR_020_A6_J2_SCOPED_PROJECTED_LAW_2026-08-05
  DOR_020_A7_EC_BRANCH_CARRIED_2026-08-05
  DOR_020_A8_GAMMA_BOTH_ROUTES_2026-08-05
  DOR_020_A9_XI_N_ADOPTED_2026-08-05

PREFIX `DECISION_OF_RECORD_NNN_…`  (14)
  003_GEOMETRIC_ROUTE_REFRAMED           004_EVALUATION_FENCE_LIFTED_FOR_ONE_ITEM
  005_P7_CONSUMES_THE_ASSEMBLED_SPACE    006_TYPE_P_ADOPTED_LAZY_MIGRATION
  007_SMOOTH_FORK_DERIVE_THE_LIMIT       008_FIELD_CTP_ADOPTION_RATIFIED_WITH_FALSIFIER
  009_THE_TRANSITION_LAW_RATIFIED_E_POST 010_STRUCTURAL_P_DEPENDENCE_AUTHORIZED
  011_TASK4_TRANSPORT_CONSTRUCTION_AUTHORIZED
  013_GEN_OMEGA_RATIFIED_FAMILY_LEVEL    014_SOURCE_GERM_PHYS_RATIFIED
  014_AMENDMENT_1_CB_DERIVED_PAIRING     014_AMENDMENT_2_EVEN_PAIRING_NORMALIZATION
  015_FIELD_SIGNATURE_PHYS_RATIFIED

NUMBERING GAPS AT BYTES, recorded not adjudicated: no 001, 002, or 012 exists
under either prefix in either supervision root.  INDETERMINATE-AT-BYTES.
```

### §6.1 RULINGS THAT ADOPT A PROCEDURE, NOT A MATHEMATICAL OBJECT

Nine of the 28 adopt a procedure, an authorization, a typing scheme, or a
disambiguation. They are enumerated so the count is complete, and each is graded
in one line.

```text
P-1  DoR-004 (evaluation fence lifted for one named item).  Adopts a scoped
     AUTHORIZATION.  *** CONSTRUCTION-DEPENDENT *** — its object is "V011's
     composition-loop matrix experiment and nothing else".
P-2  DoR-005 (P7 consumes the assembled space).  Its own words, :14-16: "This
     ruling disambiguates a self-reference in a specification. It selects no
     physical fork".  *** CONSTRUCTION-DEPENDENT *** — ground: this program's
     P1–P8 build list.
P-3  DoR-006 (TYPE-P adopted, lazy migration).  Adopts a TYPING SCHEME —
     graded as method at §8, M-3.
P-4  DoR-010 (structural p_ch-dependence computation authorized, scoped).
     A scoped authorization.  *** CONSTRUCTION-DEPENDENT ***.
P-5  DoR-011 (Task-4 transport construction authorized).  An authorization.
     *** CONSTRUCTION-DEPENDENT ***.
P-6  DoR-008's STANDING FALSIFIER (quoted at A-2 below) — a procedure, and the
     single most transferable procedural rule in the 28; graded at §8, M-4.
P-7  DoR-017's TEST DISCIPLINE (member-sensitivity tagging;
     void-on-downstream-failure) — procedure; graded at §8, M-5.
P-8  DoR-020-A8 (Γ carried on both routes) — a WORK-ORDER plus one law.  The
     law it institutes is quoted at A-12.
P-9  DoR-003 (geometric route reframed) — an IMPORT FINDING, not an adoption;
     graded at A-0 because what it records is a negative about an object.
```

### §6.2 RULINGS THAT ADOPT A MATHEMATICAL OBJECT — QUOTED AND GRADED

**Every one of these is an adoption of an object into THIS program's
construction. The recurring question is whether the object is derived or
authored, and the corpus answers it explicitly in most cases. AUTHORED PHYSICS
PREMISES ARE FLAGGED IN CAPITALS.**

```text
A-0  DoR-003 — WHAT WAS *UN*ADOPTED.  :24-27, whole:
       "*** THE KALUZA-KLEIN FRAMING IS AN IMPORT. THE CORPUS DERIVES A COMPACT
        `U(1)` COMPARISON GROUP AND PROJECTIVE / FUBINI-STUDY RECORD GEOMETRY.
        IT DOES **NOT** DERIVE THAT THE PROJECTIVE DIRECTION IS A PHYSICAL
        SPACETIME DIMENSION WITH A LENGTH RADIUS. `S^1` IS NOT ESTABLISHED BY
        `U(1)` ALONE. ***"
     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: the group-theoretic fact that a compact U(1) comparison
     group does not by itself furnish a spatial circle of any radius.  This is
     a distinction between a structure group and a spacetime fiber, available
     to anyone.  It is a NEGATIVE that a successor inherits unconditionally:
     deriving U(1) is not deriving a fifth dimension.
     Its supporting flags, :19-22, carried whole:
       "projective_state_space_is_spatial_KK_fiber        = false | TYPE-S
        five_dimensional_EH_derived_from_record_structure = false | TYPE-S
        the single-circle ansatz cannot supply an independent squashing mode
                            *** TYPE-R REFUTATION of the granted ansatz ***"

A-1  DoR-007 — THE DISCRETE-TO-CONTINUUM EQUIVALENCE THEOREM AS A NAMED
     OBLIGATION.  :8-14, whole:
       "The smooth-required subset … is to be met by a DERIVED
        DISCRETE-TO-CONTINUUM EQUIVALENCE THEOREM — the stitching rule as a
        theorem over refinements.
        ADOPTION OF (M,g) FOR THIS SUBSET IS OFF THE TABLE. The ambient metric
        carries an Einstein-Hilbert term; adopting it at the alpha-facing chain
        would adopt the gravity the program claims to derive."
     *** GRADE = TRANSFERS-AS-SPECIFICATION ***
     What survives is not an object but a REQUIREMENT WITH A REASON: any
     construction claiming to derive gravity may not import a smooth ambient
     metric at the chain that faces the derived quantity, because that metric
     already carries the term being derived.  That circularity bar is stated in
     terms any successor has.  The object it demands — the equivalence theorem
     — is UNBUILT of record (see §7, S-2).

A-2  DoR-008 — THE FIELD/CTP ALGEBRAIC PRESENTATION (seven adoptions).
     :8-16, the adopted list, whole: "sequential labels on Q-201's N <= M
     system with disclosed zero-extension . the C* field algebra .
     forward/opposite-backward CTP tensor completion . the even spatial join to
     the Q-201 tuple . the Hilbert C*-module representation . the common domain
     . branch embeddings . bounded finite-support source maps (with the four
     proved conditional consequences). Twice adversarially attacked; both found
     defects repaired by REMOVAL; second pass clean (Q-211). Honest count:
     SEVEN."
     *** GRADE = CONSTRUCTION-DEPENDENT ***
     *** AUTHORED PREMISE — the ruling's own word is "RATIFIED as declared
     premises". ***  These are not derived results; a successor inherits them
     only as premises and must know they were authored.
     GROUND NAMED: Q-201's N ≤ M system and this program's CTP doubling.

A-3  DoR-009 — THE SOURCE-COUPLED RECORD-TRANSITION LAW, with E_post.
     :8-13, whole: "is RATIFIED, with the endpoint-charge binary resolved to
     *** E_post: THE TIME-ORIENTED ASSIGNMENT -- charge follows the write's
     direction. *** Grounds: coherence with the sealed character of records
     (thresholded nonreturn, durability, oriented events). **Nothing sealed
     forced the choice; it is the principal's, made in the open.**"
     *** GRADE = CONSTRUCTION-DEPENDENT ***
     *** AUTHORED PHYSICS PREMISE — AND THE RULING SAYS SO IN ITS OWN WORDS:
     "Nothing sealed forced the choice; it is the principal's, made in the
     open."  This is the cleanest authored-premise disclosure in the 28. ***
     Its three ratified rows (:15-17): endpoint charge = E_post · finite
     locality (P2, no cross-cell interaction) · external-parent scope.
     Everything downstream is marked "TYPE-P | premises: DoR-008, DoR-009".

A-4  DoR-013 — Gen_Omega AT FAMILY LEVEL.  :7-16, the adopted content, whole:
       "- A0 — the authored finite scalar source realization.
        - THE ANCHORED GENERATIVE FAMILY — all three convergent anchor classes
          (bistochasticity, finite-trace detailed balance, irreducible symmetry
          covariance) adopted AS A FAMILY.  *** NO MEMBER IS SELECTED, EVER. ***
          The proven p_ch-neutrality certificate … is the license: every member
          forces the same normalized-identity invariant state and the same
          symbolic sector-dimension-ratio form for p_ch."
     *** GRADE = CONSTRUCTION-DEPENDENT ***
     *** AUTHORED PHYSICS PREMISE, self-labelled: "A0 — the authored finite
     scalar source realization." ***
     BUT: the NO-SELECTION PRINCIPLE it instantiates ("NO MEMBER IS SELECTED,
     EVER", licensed by a neutrality certificate) is method — §8, M-6.

A-5  DoR-014 — SOURCE_GERM_PHYS, and THE GERM'S ONE PARAMETER.  :10-12, whole:
       "THE GERM'S ONE PARAMETER: the ordered integer pair (r_0, r_ch),
        r_0 > 0, r_ch > 0 on the durable branch. Same-rank presentations are
        GAUGE (the proven trace-preserving block-unitary quotient; p_A, Z_inc,
        all exported derivatives invariant)."
     and :14-17, carried because adverse: "Pinning of the pair: NO_VERDICT of
     record — refuted on every executable scalar arm; the K_square arm (capped,
     C29) is the NAMED FUTURE DETECTOR; the missing rank-pinning package …
     is the require-shaped would-build."
     *** GRADE = DEPENDS-ON-A-WITHDRAWN-OR-UNBUILT-OBJECT ***
     OBJECT NAMED BY THE RULING ITSELF: "the missing rank-pinning package
     (sealed scalar source representation + rank-preserving intertwiner)".  The
     germ is adopted; its one parameter is unpinned of record.

A-6  DoR-014 AMENDMENTS 1 AND 2 — THE DERIVED PAIRING AND ITS PARITY FIX.
     A1's ruling, :11-15: "the required charge/flux access FORCES the bilocal
     pairing from the linear source. The replacement is the DERIVED pairing:
        b := i·hbar · L (x) L".
     A2's correction, :6-12, whole: "Amendment 1's derived pairing had the right
     CONTENT … and one misplaced factor: the i is Θ-ODD and belongs on the
     OUTPUT side, where the ratified W-convention (W = −iℏ·Log Z) already
     carries it. The corrected derived pairing is:
        b := hbar · L (x) L        (source slot; Θ-EVEN — fits the exponent's
                                    parity)".
     *** GRADE = CONSTRUCTION-DEPENDENT *** — L is this program's linear source.
     WHAT DOES TRANSFER, and is worth naming: the PARITY BOOKKEEPING RULE that
     an odd factor belongs on the side whose convention already carries it.
     That is a general Θ-parity discipline; graded as method at §8, M-7.
     ADVERSE: Amendment 2 SUPERSEDES Amendment 1's form.  Anything resting on
     A1's `i·hbar·L⊗L` rests on a superseded object.

A-7  DoR-015 — FIELD_SIGNATURE_PHYS.  Its provenance line, :22, whole and
     unsoftened: "FOUR FAMILIES DERIVED, SIX STRUCTURES AUTHORED."
     The six, :6-9, whole: "THE SIX OPENLY-AUTHORED AMPLITUDE-SIDE STRUCTURES:
     external background, external realization, connection carrier, source
     rigging, field representation, bilocal class — authored physics, disclosed
     as such (records are phase-rich, amplitude-poor; the mechanism is proven,
     Q-290)."
     *** GRADE = CONSTRUCTION-DEPENDENT ***
     *** SIX AUTHORED PHYSICS PREMISES, THE LARGEST SINGLE BLOCK OF AUTHORED
     PHYSICS IN THE 28, AND THE RULING NAMES ALL SIX. ***
     ITS ONE DERIVED OBJECT WORTH ISOLATING, :11-15: "THE CYCLE CURRENTS u_c
     (c in ker(B^T)), dPhi_c = u_c — THE physical response family: the ALLOWED
     U(1) holonomy of the origin table, derived by the gate. Open-path content
     is ENDPOINT-COVARIANT transport — the REQUIRED charge/flux access — never a
     scalar coordinate."
     The `c ∈ ker(B^T)` cycle space of an incidence matrix is standard graph
     homology, but the object it is asserted OF (the origin table, the gate) is
     this program's; the adoption is therefore CONSTRUCTION-DEPENDENT.
     ADVERSE CLAUSE CARRIED, :24-25: "The W3 precision of record: finite source
     restrictions are ADJOINTS of the retained isometric inclusions; naive
     truncation is invalid."

A-8  DoR-019 — THE CARRIER METRIC AND UNITS.  DERIVED CORE graded at §4.6 T-19.
     ITS AUTHORED HALF, :22-25, whole:
       "AUTHORED (four disclosed items): the R5 completed-carrier
        identification; the positivity/reality completion convention; the A4
        automorphism isometry (beyond W3's reach); the carrier units and the R4
        unit seam."
     *** GRADE = CONSTRUCTION-DEPENDENT ***
     *** FOUR AUTHORED PREMISES, DISCLOSED BY THE RULING. ***
     ITS STANDING DISCIPLINE, :29-30, which does transfer: "Derived-or-declared,
     never implicit (the principal's clarification of record, Q-382): any future
     cross-sector conversion arrow must be separately declared."  Method — §8,
     M-8.

A-9  DoR-016 — THE NETWORK-SOURCING LAW.  :7-19, the adopted object, whole:
       "The law: a record system's emission toward a network neighbor is the
        ordered pair (T₊, T₋) of endpoint-covariant transports read from the
        sender's admitted write history, each carrying its own covariance law.
        Delivery is reciprocal with positive delay (the exact one-tier member is
        AUTHORED, not uniquely forced — flagged residue). The receiver forms the
        relative CTP endomorphism R_CTP = T₋†T₊ and consumes it ONLY through the
        ratified DoR-009 finite doubled ready-record trace
        Z^CTP = ∏ conj(z₋ⁿ)z₊ⁿ, giving the exact per-system charged-projector
        tower A_k = (1−p) + p·∏ Z^CTP with p symbolic. The complete network
        object is the ORDERED PAIR of per-system towers; multiplying amplitudes
        is unlicensed (the joint contraction is an unopened door)."
     *** GRADE = CONSTRUCTION-DEPENDENT ***
     *** AUTHORED, DISCLOSED IN THE RULING'S OWN PARENTHESIS: "the exact
     one-tier member is AUTHORED, not uniquely forced — flagged residue." ***
     GROUND NAMED: DoR-009's ratified trace (itself authored at A-3) — so this
     adoption sits on an authored premise, at two removes.
     ITS SIX DOORS, :23-26, are ALL TYPE-U (unbuilt) by the ruling's own
     heading: "## Doors (all TYPE-U, none opened by this ruling)".

A-10 DoR-017 / DoR-018 — THE N MEMBER AND ITS JETS (SHAPE K).
     DoR-017 :8-10: "RATIFIED as square proposal V004's merged candidate,
     CLOSED BY THE N MEMBER: the certified covariant divergence-generated
     member m = (δ_div, Depth, Accum, Gen, φ, Norm, ν) with its independent
     bottom legs b_N."  DoR-018 :7-13 adopts "germ V003's SHAPE K … the
     cycle-only covariant germ phi_K(k) on DoR-019's ratified norms".
     *** GRADE = CONSTRUCTION-DEPENDENT *** for both.
     GROUND NAMED: the action-comparison/2PI square, this program's own
     diagram, on DoR-019's ratified norms.
     DoR-017 carries FIVE AUTHORED RESIDUES R1–R5 by its own count (:14-16).
     DoR-018 records a PERMANENT REGRESSION (:17): "Shape CK,lambda is RECORDED
     with its unabsorbability theorem and remains available only through a
     future gate that would declare lambda; the lambda-subfiber regression is
     permanent."

A-11 DoR-020 — THE CONTINUUM PACKAGE, RATIFIED **CONDITIONALLY**.  :7-13, whole:
       "THE CONTINUUM PACKAGE is ADOPTED as the program's declared continuum
        theory, in the only form the hostile review certifies as honest
        (Q-421, P3): CONDITIONAL on nonemptiness of the joint J1-J15 equalizer
        over the six irreducible generators:
          B_R1_NATURAL, B_Q408_REFINEMENT, B_C1_COMPLETION,
          B_FAITHFULNESS, B_C2_RESPONSE_BOUNDARY, B_C3_MAXWELL_HODGE."
     and its refutation semantics, :26-31, whole:
       "The six generators are a JOINT premise (a fiber product): separate
        nonemptiness of all six provably does not imply joint inhabitance (the
        permanent equalizer regression). A certified witness inhabits the joint
        equalizer or the condition stands open."
     *** GRADE = DEPENDS-ON-A-WITHDRAWN-OR-UNBUILT-OBJECT ***
     OBJECT NAMED BY THE RULING: the certified witness inhabiting the joint
     J1–J15 equalizer.  Until it exists, the ruling's own §"LICENSED" clause
     (:20-23) FORBIDS "binding a member, executing the fixed-point computation,
     any end test."  **Everything tagged [EQ6] rests on this unbuilt witness.**
     WHAT DOES SURVIVE, and it is not small: the FIBER-PRODUCT SEMANTICS —
     "separate nonemptiness of all six provably does not imply joint
     inhabitance."  That is a general fact about equalizers/fiber products and
     is graded TRANSFERS-WHOLE as a constraint at §11's itemization.

A-12 DoR-020-A1 — THE WHERE-CLAUSES.  :12-15, whole:
       "2. THE LOCAL FIELD MEMBERS — typed as a U(1) BUNDLE WITH CONNECTION
           over the record surface, with the bundle lift/pullback-bundle
           isomorphism, smooth full-rank, and characteristic-class
           compatibility; transport derived from the declared members.
           Law-only."
     *** GRADE = CONSTRUCTION-DEPENDENT as an adoption *** — it declares that
     THIS program's local field members are of that type.  The TYPE ITSELF (a
     U(1) bundle with connection) is the object graded TRANSFERS-WHOLE at T-16
     and T-17; the adoption adds no mathematics, it makes a declaration.
     ADVERSE, AND LOAD-BEARING: A1's closing claim, :17-18, "THE CLAUSE LAYER
     OF THE CONTINUUM THEORY IS COMPLETE. No declarations remain anywhere in
     Task 5" **IS EXPRESSLY SUPERSEDED TWICE** — by A4 (:7, "THIS AMENDMENT
     EXPLICITLY SUPERSEDES DoR-020-A1's clause-layer-completeness statement")
     and by A5 (:8-9, "SUPERSEDES DoR-020-A1's clause-layer-completeness
     statement (as A4 did)").  Anything resting on clause-layer completeness
     rests on a SUPERSEDED statement.
     Also of record at A1 :26-28, its "physical reading … non-binding": "gravity's
     declared contribution is a stage already fibered for charge — the U(1)
     bundle geometry of electromagnetism lives inside the where-declaration."
     Marked NON-BINDING by the ruling; recorded, not relied on.

A-13 DoR-020-A2 — THE COMPLETED-EXISTENCE AXIOM (Arm A).  :7-11, whole:
       "THE COMPLETED-EXISTENCE AXIOM (COMPLETED_EXISTENCE_020, V002 text, FC12
        struck) is ADOPTED — OVER THE SUPPORT-QUALIFIED GUARD (Arm A): the
        guard amended by exactly the two conjuncts the re-adjudication displays,
        FC1–FC10/FC13 untouched. Step 1 of the twelve-step map discharges IN
        CONDITIONAL FORM for F_actual per the membership theorem's final
        statement. The proved permanent violation of the unamended extent
        converts to an OPEN question, its vacuity relocated of record to
        undetermined-pending-ExtSrc ((L0)/the J-II arrow) — reopenable, not
        refuted."
     *** GRADE = CONSTRUCTION-DEPENDENT ***
     *** AN AXIOM — i.e. AUTHORED BY DEFINITION.  A successor inherits it only
     as a premise. ***
     ITS NAMED OPEN, :24, carried: "NAMED OPEN (not amended, not silently
     touched): A_J2's extent clause of A_extent's shape."
     ITS NINE FROZEN CLAUSES (:14-23) each cite a sealed source; the ruling
     states "none authored here" — the authorship sits upstream, in the axiom.

A-14 DoR-020-A3 — J4 AMENDED: THE RELATIONAL INCREMENT GROUPOID.  :10-17, the
     adopted row, whole:
       "For every admitted arrow f: N -> M, an R1 family member supplies a
        relation term (I_N, I_M, v_f) in Rel_f satisfying
          I_M = I_N o rho_f + v_f,
          v_(gf) = v_f o rho_g + v_g,   v_id = 0,
        and the differentiated relation D^2 I_M = rho_f^*(D^2 I_N) + D^2 v_f.
        The admissible flat family acts by
        (I_N, v_f) -> (I_N + psi_N, v_f - psi_N o rho_f), with ALL members
        retained. No source member is selected from a target."
     ITS OWN TAG, :7-8: "Tag: PROVABLE (derived content, no authored parameter);
     adoption required only because it rewrites ratified text."
     *** GRADE = CONSTRUCTION-DEPENDENT ***
     GROUND NAMED: the R1 family, ρ_f, and the admitted-arrow category of this
     program.  WHAT IS RECOGNIZABLY GENERAL: `v_(gf) = v_f ∘ rho_g + v_g`,
     `v_id = 0` is the standard 1-COCYCLE CONDITION for a groupoid acting on a
     module, and the flat action is the standard COBOUNDARY.  A successor with
     any such groupoid has that cocycle/coboundary calculus independently;
     the ADOPTION here binds it to this program's R1 family.
     ITS GROUNDS ARE A REFUTATION, carried, :19-20: "The functional J4 was
     REFUTED on cycle creation (the vertical-increment counterexample; the
     increment is actual cycle-creating action data)."  Anything resting on the
     pre-amendment functional J4 rests on a REFUTED object.
     A CORRIGENDUM (A3-c1, :29+) further amends the flat action for the
     simultaneous family case.

A-15 DoR-020-A4 — J12 CONTACT GLUE: STRICT PUSHOUT.  :10-15, whole:
       "For C_N = R_N^rep ∩ I_contact,N, the represented and boundary transports
        form a gluing datum with
          eta_f^boundary|_(C_N) = Eta_f^rep|_(C_N).
        The total response carrier is the signed pushout
          R_N^phys = R_N^rep ⊕_(C_N) I_contact,N,
        and Eta_f is the unique induced map, obeying J12 composition and the
        J13 cocycle, restriction, reality, unit, Ward, support, and
        subextensivity laws."
     ITS OWN TAG, :7-8, whole: "Tag: YOURS (authored member — the sealed
     contact/Ward stock provably does not force the overlap law; the first
     authored member since DoR-019)."
     *** GRADE = CONSTRUCTION-DEPENDENT ***
     *** AUTHORED PHYSICS PREMISE, AND THE RULING PROVES IT IS AUTHORED: "the
     sealed contact/Ward stock PROVABLY DOES NOT FORCE the overlap law." ***
     ITS OWN UPGRADE PATH, :19-21, carried: "zero-intersection (PART-PROVABLE —
     if a separation theorem later proves C_N = {0}, this authored row becomes
     CONTENTLESS and upgrades to derived; that upgrade path stays open)."
     THE PUSHOUT ITSELF is standard category theory; what is authored is the
     CHOICE of the strict pushout over the twisted alternative.

A-16 DoR-020-A5 — CONTACT_LAPLACIAN_REDUCING.  :10-13, whole:
       "For every admitted finite stage and relevant degree, the actual contact
        subspace I_contact,N is invariant under the ratified Hodge Laplacian:
          Delta_N^Hdg (I_contact,N) ⊂ I_contact,N,
          equivalently   [E_C,N, Delta_N^Hdg] = 0."
     ITS OWN TAG, :7-8: "Tag: YOURS (authored — provably not derivable, provably
     not obstructed; the second authored member since DoR-019)."
     *** GRADE = CONSTRUCTION-DEPENDENT ***
     *** AUTHORED PHYSICS PREMISE, with the strongest possible disclosure:
     "provably not derivable, provably not obstructed." ***
     ITS DIRECTLY FALSIFIABLE VOID CONDITION, :17-18, carried: "1 an actual
     contact vector with a noncontact component in Delta_N^Hdg c — DIRECTLY
     FALSIFIABLE".

A-17 DoR-020-A6 — J2 RE-SCOPED: THE PROJECTED OLD-IMAGE LAW.  :7-9, whole:
       "Cycle-creating J2 is REPLACED by the scoped projected law on the
        old-image P_H sector:
          r_f^Bot ∘ pi_Mx,M ∘ Loc_M ∘ eta_f = pi_Mx,N ∘ Loc_N  (SCOPED_J2_SQUARE)"
     with the adverse half kept, :10-13: "FULL J2 on the new-cycle factor is
     retained as an explicitly typed POST-SCOPE CONDITION, pending an
     INDEPENDENT construction of Loc/pi_Mx on that factor — both lawful routes
     from current stock are proven closed (unconstrained lift = selection;
     reader-derived pi_Mx = the F_PLDEC circularity class)."
     *** GRADE = DEPENDS-ON-A-WITHDRAWN-OR-UNBUILT-OBJECT ***
     OBJECT NAMED BY THE RULING: an independent construction of Loc/π_Mx on the
     new-cycle factor; both routes from current stock PROVEN CLOSED.
     WHAT SURVIVES AS A CONSTRAINT: the two closure reasons — "unconstrained
     lift = selection" and "reader-derived π_Mx = circularity" — are general
     failure modes (selecting a member; deriving the reader from the thing the
     reader is meant to decide).  Graded as method at §8, M-9.

A-18 DoR-020-A7 — THE E_C FREEDOM: BOTH BRANCHES CARRIED.  :7-11, whole:
       "The contact-versus-loop-class freedom is CARRIED, not chosen: both
        branches
          (ZERO)     E_C,RL c_RL = 0   — the loop's flux is bulk-physical;
                                          the pairing decides;
          (IDENTITY) E_C,RL c_RL = c_RL — the loop's flux is interface content;
                                          reciprocal vanishing forced;
        run conditionally through the period machinery … NO SELECTION"
     *** GRADE = INDETERMINATE-AT-BYTES *** as an adopted object: the ruling
     adopts NO object; it adopts the refusal to choose between two, and states
     "each branch's content remains untyped-by-stock (the freedom is genuine)."
     The bytes therefore do not decide which object, if either, a successor
     would inherit.  The DISCIPLINE (carry, do not select) is method — M-6.

A-19 DoR-020-A8 — THE IDENTIFICATION FALSIFIER.  :12-15, whole:
       "THE IDENTIFICATION FALSIFIER is law: wherever both routes are formed,
        their periods MUST agree; a displayed disagreement on any commonly-formed
        cell is a first-order finding that voids the disagreeing
        construction(s) pending adjudication. No lane may assume the
        identification."
     *** GRADE = TRANSFERS-AS-SPECIFICATION ***
     This is a REQUIREMENT ON ANY TWO-ROUTE CONSTRUCTION: if two routes to the
     same quantity are both formed, agreement is mandatory and may not be
     assumed in advance.  Stated in terms — two routes, a commonly-formed cell,
     a period — that any successor building redundant routes will have.  Its
     particular objects (Loc, Ξ_N, the H/HOL routes) are this program's; the
     law is not.

A-20 DoR-020-A9 — Ξ_N V004, THE WHAT-ENCIRCLES-WHAT CLAUSE.  :8-16, whole:
       "The Ξ_N where-clause (V004) is ADOPTED: the assignment of which loop a
        source encircles becomes lawful structure — a set map into the integral
        cycle lattice, positive-scale invariant, with the topological-charge
        typing AS LAW (discontinuity at the zero stratum and at typed
        support-birth boundaries; constancy only on oriented addressed strata),
        the relative holonomy consumed per the derived display, the winding
        class in R/2πZ with gated log extraction, native units, exact
        transports, the authored anti-counterterm fence (Z13), and the real A7
        identity-branch obligation (Z-A7). ADOPTION LICENSES; IT INHABITS
        NOTHING: the gates ExtSrc, G4-D, G5, FULL-G4, G2-N remain displayed and
        open."
     *** GRADE = DEPENDS-ON-A-WITHDRAWN-OR-UNBUILT-OBJECT ***
     OBJECT NAMED BY THE RULING ITSELF: five open gates — ExtSrc, G4-D, G5,
     FULL-G4, G2-N — and its own sentence "ADOPTION LICENSES; IT INHABITS
     NOTHING."  The clause is law with no inhabitant of record.
     *** ONE AUTHORED ITEM DISCLOSED INSIDE IT: "the authored anti-counterterm
     fence (Z13)." ***
     WHAT IS GENERAL: the topological-charge typing — a winding-type assignment
     is constant only on strata and discontinuous at the zero stratum — is a
     standard property of topological charge, not this program's discovery.
```

### §6.3 THE AUTHORED-PHYSICS ROLL, EXTRACTED

A successor may inherit these as premises, **but must know they were authored,
because the corpus says so of each one, in its own ruling:**

```text
DoR-008   seven adoptions       "RATIFIED as declared premises"
DoR-009   E_post                "Nothing sealed forced the choice; it is the
                                 principal's, made in the open."
DoR-013   A0                    "the authored finite scalar source realization"
DoR-015   six structures        "FOUR FAMILIES DERIVED, SIX STRUCTURES AUTHORED"
DoR-016   one-tier member       "AUTHORED, not uniquely forced — flagged residue"
DoR-017   R1–R5                 "the five authored residues R1–R5"
DoR-019   four items            "AUTHORED (four disclosed items)"
DoR-020-A2 the axiom            an axiom, adopted
DoR-020-A4 strict pushout       "YOURS (authored member — the sealed contact/Ward
                                 stock provably does not force the overlap law)"
DoR-020-A5 Laplacian reducing   "YOURS (authored — provably not derivable,
                                 provably not obstructed)"
DoR-020-A9 Z13 fence            "the authored anti-counterterm fence (Z13)"
faithfulness / |n| = 1          "IMPOSED, not forced" (§4.3 T-11), entering by
                                 ratification at DoR-008/009

*** TWENTY-EIGHT-PLUS AUTHORED ITEMS ACROSS ELEVEN RULINGS, EVERY ONE
    DISCLOSED BY THE RULING THAT ADOPTED IT.  The disclosure discipline is
    itself the most transferable thing here — graded at §8, M-1. ***
```

**Q3 TALLY.** 28 rulings. Nine adopt a procedure (P-1..P-9, §6.1, several graded
as method at §8). Twenty-one entries adopt or un-adopt an object (A-0..A-20).

```text
TRANSFERS-WHOLE .............................. 1   (A-0)
TRANSFERS-AS-SPECIFICATION ................... 2   (A-1, A-19)
CONSTRUCTION-DEPENDENT ....................... 13  (A-2, A-3, A-4, A-6, A-7,
                                                   A-8, A-9, A-10, A-12, A-13,
                                                   A-14, A-15, A-16)
DEPENDS-ON-A-WITHDRAWN-OR-UNBUILT-OBJECT ..... 4   (A-5, A-11, A-17, A-20)
INDETERMINATE-AT-BYTES ....................... 1   (A-18)
                                              ----
OBJECT-BEARING ENTRIES ....................... 21
PROCEDURAL ENTRIES (§6.1) ..................... 9
```

A-13 (the completed-existence axiom) is graded CONSTRUCTION-DEPENDENT — it is an
adopted axiom, not a dependence on an unbuilt object — and its NAMED OPEN
("A_J2's extent clause of A_extent's shape") is flagged at §10 rather than
counted as the grade.

---

## §7 — Q4: BUILT OBJECTS, AND SPECIFICATIONS OF UNBUILT ONES

**THE CATEGORY THE COMMISSION WARNED IS EASY TO MISS IS FLAGGED THROUGHOUT WITH
`[SPEC]`.** An item marked `[SPEC]` has its value as a statement of what
something must do or be — not as a result — and is transferable on that footing
whether or not its ground survives.

### §7.1 BUILT OBJECTS

```text
B-1  *** THE ONE BUILT CELL-TO-RECORD CROSSING: THE CAUSAL DIRECT LIMIT ***
     `STAGE8_CELL_RECORD_CROSSING_O55SR_V001.md` (seal OK) §4.2, quoting
     `FORK_8_CAUSAL_DIRECT_LIMIT_PROMOTION_RESULT_V001.md:51-62`, whole span:

       "## P2. Direct limit and generators
        The finite record algebras and embeddings define:
          R_infinity=inductive_limit tensor_(j=1)^N M_3(C).
        Their output states are exactly compatible, giving one quasi-local
        state and its GNS representation. The completed-record dynamics is the
        strongly continuous identity automorphism group, whose self-adjoint
        generator is zero on that algebra."

     THE TYPE, BOTH ENDS, from O55SR:378-393:
       SOURCE  the directed system { tensor_(j=1)^N M_3(C) , iota_N },
               "For independent outgoing record cells define A_N = tensor_(j=1)^N
                M_2, iota_N(A)=A tensor I."  One tensor factor per RECORD CELL.
       ARROW   inductive_limit
       TARGET  R_infinity, carrying omega_h and the central sequence.

     *** GRADE = TRANSFERS-WHOLE, AS A CONSTRUCTION SCHEMA ***
     DEPENDENCE CITED: the inductive (direct) limit of a directed system of
     finite-dimensional matrix algebras under unital embeddings A ↦ A⊗I, the
     compatibility condition on states, and the GNS construction.  This is the
     standard UHF/quasi-local construction of AF C*-algebra theory.  A successor
     that indexes finite record algebras by cells and embeds them unitally has
     exactly this arrow, with exactly this proof, without any object of this
     program.  The specific factor `M_3(C)` (and `M_2` in the covector lift
     spec) is this program's cell dimension; the LIMIT is not.
     GROUND IS: something a successor would independently have.

     *** AND IT IS THE ONE OBJECT THAT DISCHARGES N-1. ***  It is the third of
     the four mechanisms N-2 enumerates ("an infinite causal/environmental limit
     with asymptotic outgoing sectors").  O55SR:439-441, whole: "Fork 8 built the
     THIRD.  The other three remain unbuilt."

     ADVERSE, CARRIED: it is NOT the onset gate's crossing.  O55SR's four
     separating bytes (:449-510) include the result's own scope sentence
     (FORK_8:11-14, "The original hypothesis has earned promotion for the
     durability and outgoing-record problem in the ordinary 3+1 flat-asymptotic
     branch") and the onset gate's own next-gate clause naming a different,
     formless object.  O55SR:1093-1096, whole: "*** REPRESENTED-ONLY-AS-TWO-
     ENDPOINTS *** a cell side, a record side, and a named connecting object —
     'durability map' — whose 'form supplied in none' of 5,512 files."
     ALSO ADVERSE: O55SR §4.1 C-3 books the cost — "its GNS apparatus IS Hilbert
     machinery and is marked OFF-SCOPE separately."

B-2  THE RECORD COMPLEX (the chain/cochain complex).  Typed at bytes through
     O55SR's C-6, quoting `STAGE8_STRATIFICATION_O27SR_V001.md:206-208`:
       "For each oriented `k`-cell `e`, let `delta_e in C_N^k` denote its basis
        cochain"
     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: a finite cochain complex on an oriented cell structure,
     with basis cochains indexed by oriented k-cells, and its incidence
     operator B (whose kernel `ker(B^T)` supplies the cycle currents of A-7).
     This is standard simplicial/cellular (co)homology.  Any successor building
     a finite record carrier as a cell structure has it.
     *** THE ADVERSE FINDING THAT MUST TRAVEL WITH IT, quoted whole from
     O27SR via O55SR:100-104: "'Cell' names two objects the corpus says are not
     identical." — the chain-complex k-cell is NOT the primitive causal record
     cell.  O55SR calls this "the single most available level-confusion in this
     corpus," and it is corroborated in a sealed distinctness table
     (`STAGE8_C1_U_OMEGA_TYPED_CODEX2_V001.md:319`: "| continuum diamond vs CW
     cell/complex | KEPT DISTINCT |").  A successor inherits the complex AND
     the warning. ***

B-3  THE CONNECTION ON THE RECORD COMPLEX / PROJECTIVE RECORD BUNDLE.
     Graded whole at §4.5, T-17.  *** TRANSFERS-WHOLE *** — dependence: the
     patching law a_j = a_i + dθ_ij and d² = 0.
     WHAT DOES NOT COME WITH IT, from the same artifact, :96-102: no unique
     connection, no curvature, no kinetic coefficient; `K_bare = 0` is set by
     the sealed microscopic principle, i.e. by adoption.
     **UNSEALED IN BOTH ROOTS — flagged §10.**

B-4  THE U(1) TRANSITION FUNCTIONS AND THE TRIPLE-OVERLAP COCYCLE.
     Graded whole at §4.5, T-16: `z_j = g_ij z_i`, `g_ij = exp(i theta_ij) in
     U(1)`, `g_ij g_jk g_ki = 1`.  *** TRANSFERS-WHOLE ***.
     **UNSEALED IN BOTH ROOTS — flagged §10.**

B-5  THE ONSET GATE — `BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md`
     (BOTH sidecar forms present; BOTH verify OK).
     ITS ADOPTED RULE, :97-99, whole: "## Adopted Gravacle onset rule
       The allow/require boundary is adopted to select first admissible record
       onset through a shortest **relative** projective path on the unique
       physical record"
     ITS BUDGET, :83-88, whole: ">= pi hbar/2." … "This is an energy-uncertainty/
     path-length budget. It is not automatically either branch's dynamical
     action, the action difference, or a coefficient in the microscopic
     Lagrangian."
     *** GRADE = CONSTRUCTION-DEPENDENT ***
     *** AUTHORED PHYSICS PREMISE — the gate's own heading is "Adopted Gravacle
     onset rule", and its own flags mark
     `relative_onset_saturation_derived = false`,
     `relative_onset_saturation_adopted_Level_1 = true`. ***
     GROUND NAMED: the adopted Gravacle allow/require boundary and this
     program's projective record carrier.
     ITS DELIVERY FAILURE, ON ITS OWN FACE, :92-95, whole:
       "Global orthogonality is not yet a durable public record. Perfect readout
        from the designated record subsystem requires orthogonal supports of its
        reduced conditional states. Durability additionally requires persistence
        and recoverability or redundancy."
     with flags `orthogonal_reduced_record_supports_derived = false` and
     `physical_durability_derived = false`.
     THE GATE DOES NOT DELIVER ITS STATED OUTPUT.  O55SR states it flatly at
     :1060-1063.

B-6  THE FLUX GATE — `SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003.md`
     (BOTH sidecar forms present; BOTH verify OK).
     ITS BUILT OBJECT, :81-86, whole:
       "The ready-subspace unitary is
          U_write
            = (I-Q_Sigma) tensor I_R
              + Q_Sigma tensor (-iY_R)."
     ITS OWN IMMEDIATELY FOLLOWING DISCLAIMER, :88-89, whole:
       "This is conditional on the inherited/adopted rules above. It is not a
        complete microscopic action or a durable record instrument."
     *** GRADE = CONSTRUCTION-DEPENDENT ***
     GROUND NAMED: Q_Sigma (the flux projector), Y_R (the chosen equatorial
     representative on this program's record factor), and the inherited/adopted
     rules the gate names.  Its own §"Why v003 exists" (:6-18) records that
     V001 and V002 "are not authority" and lists four overreaches, including
     "the coherent flux superposition may be forbidden by charge
     superselection" and "no admissible source phase reference was supplied."
     A CONTROLLED-UNITARY OF THE FORM (I−Q)⊗I + Q⊗V is a standard controlled
     gate; what is this program's is the identification of Q with the source
     flux projector and of V with (−iY_R).
     *** A SEALED-CONSUMPTION DEFECT OF RECORD ATTACHES TO THIS GATE, and it is
     carried because it is adverse: `STAGE8_JOIN_FRONTIER_O51SR_V001.md:84-108`
     shows a closure-lane artifact refused to consume the flux gate as
     "unsidecared" three weeks after its sidecar was written and verifies.  The
     frontier artifact's words, whole: "A closure-lane artifact declined to
     consume the flux gate on a ground that is false at bytes, and the ground is
     exactly the sidecar-convention split." ***

B-7  THE DISCREPANCY COCYCLE β_f — `STAGE8_DISCREPANCY_COCYCLE_O38SR_V001.md`
     (seal OK).  Its ONE definition anywhere, :67 and :246, whole line:
       "beta_f := rho_f^C2(C2_m^fin) - C2_n^fin = 0       (C1-7)"
     with the scope clause on the SAME line and the following prose, :69-73,
     carried whole because it is the honesty of the object:
       "on the old image. For a cycle-creating arrow, `(C1-7)` says the old
        response restricts exactly; it says nothing false about the target-only
        new-cycle component. The latter remains visible in `C2_m^fin`."
     and the composition law it is said to obey, :303:
       "beta_gf = beta_g + Eta_g(beta_f)"
     and the corpus's own name for it, :271: "The corpus's own word for the
     object being extended is **'zero cocycle'**."

     *** GRADE = DEPENDS-ON-A-WITHDRAWN-OR-UNBUILT-OBJECT ***
     THE OBJECTS IT DEPENDS ON, named by O38SR at bytes:
       (i)  its single definition sits in a lane build the corpus calls KILLED
            — O38SR's source table row 3: "Graded `STAGE1_ASSEMBLY = DEFECTIVE
            (V1,V2,V3,V4,V5,V6)`; called **'killed'** and **'not an authority
            for this proof'** by LANE3.  **Carries the only definition of
            `beta_f`.**";
       (ii) the ruling that would carry the J13 laws it is said to obey is
            **ABSENT** — row "—" of the same table: "`DOR_020_A4_J12_CONTACT_
            GLUE_STRICT_PUSHOUT_2026-08-04.md` | **ABSENT FROM BOTH ROOTS** |
            The claimed adopted authority for the J13 laws. **Not readable. Not
            verified. Cited by SHA only.**";
       (iii)`beta_N` — the map of which β_f would be a value — is, at :333,
            "**never defined anywhere**".
       (iv) β_f is not even a map: :301-303, "`beta_f` is therefore **not** a map
            with its own source and target."
     O38SR's own Q4 answer, :341-350, whole:
       "*** NOTHING IN THIS FINDING IS OF RECORD. ***
        The beta display sits in a CONDITION-TAGGED LANE BUILD graded DEFECTIVE
        by its own review. Its one definition sits in a lane build the corpus
        calls KILLED. … The decision of record that would carry the J13 laws is
        ABSENT FROM THE CORPUS and could not be read.
        A structure that is real but unadopted is a different finding from one
        of record. THIS ONE IS UNADOPTED, AND IN PART KILLED."
     *** NOTE THE COLLISION WITH §6: DoR-020-A4 IS PRESENT AND SEAL-VERIFYING IN
     BOTH SUPERVISION ROOTS AT THIS COMMISSION'S BYTES (§6.2, A-15), AND IS
     QUOTED THERE.  O38SR searched the two ROOTS IT DECLARED (workspace and
     cleanroom) — not the supervision roots.  The absence is an absence FROM
     O38SR's scope, not from the corpus.  RECORDED AS A CORRECTION TO A PRIOR
     COMMISSION'S LOCATOR, NOT AS A REPAIR OF ITS VERDICT: β_f's other three
     dependencies (killed source, undefined β_N, not-a-map) are untouched by it,
     so the grade stands. ***

B-8  THE FINITE RECORD ALGEBRAS AND EMBEDDINGS (B-1's source system).
     `CAUSAL_DIRECT_LIMIT_COVECTOR_RAY_LIFT_SPEC_V001.md:46-50`, via O55SR:
       "For independent outgoing record cells define
          A_N = tensor_(j=1)^N M_2,
          iota_N(A)=A tensor I."
     *** GRADE = TRANSFERS-WHOLE *** — a UHF directed system.  Dependence: the
     tensor-product directed system with unital embeddings.  The cell dimension
     (M_2 here, M_3 in FORK_8 — **a discrepancy at bytes between two artifacts
     of the same construction, recorded and flagged §10**) is this program's.
     **THIS FILE CARRIES ONLY THE BARE SIDECAR FORM (one of the 55, §2).**

B-9  THE CENTRAL SEQUENCE / MACROSCOPIC POINTER AVERAGE.
     `CAUSAL_DIRECT_LIMIT_REDUNDANT_RECORD_SPEC_V001.md:46-56` via O55SR P-6:
       "The macroscopic pointer average
          M_N=(1/N) sum_(j=1)^N Z_j
        is a central sequence: for every observable `O` supported on at most
        `m` cells,
          ||[M_N,O]|| <= 2m ||O||/N."
     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: the elementary norm estimate for a Cesàro average of
     commuting local operators against an m-local observable.  Three lines of
     C*-algebra, no object of this program in the hypotheses.
     **THIS FILE CARRIES ONLY THE BARE SIDECAR FORM (one of the 55, §2).**
```

### §7.2 THE NINE ENUMERATED PROPERTIES A CROSSING MUST PRODUCE `[SPEC]`

**This is the single most transferable specification in the corpus.**
`STAGE8_CELL_RECORD_CROSSING_O55SR_V001.md` §5.3, `:652-673`, quoted whole,
including the adverse tail:

> ```text
> A CROSSING FROM CELL TO RECORD MUST PRODUCE, AT MINIMUM:
>    P-1 durability/irreversibility        (cell side proved recurrent)
>    P-2 persistence under later cells     (a quantifier over cells)
>    P-3 thresholded non-return            (an asymptotic-time limit)
>    P-4 recoverability                    (label separation in the limit)
>    P-5 redundancy                        (copy across N cells)  [or P-4]
>    P-6 asymptotic centrality             (commutes with all finite support)
>    P-7 sector-hood / superselection      (distinct asymptotic sectors)
>    P-8 inductive compatibility           (the limit's existence condition)
>    P-9 orthogonal reduced supports       (perfect readout) — STILL FALSE
>
> THE DIRECT LIMIT OF §4 PRODUCES P-1 through P-8 WITHIN ITS DECLARED SCOPE.
> IT DOES NOT PRODUCE P-9, AND NEITHER DOES ANYTHING ELSE:
>   ONSET_V003:188  orthogonal_reduced_record_supports_derived = false
>   ONSET_V003:189  physical_durability_derived = false
> So even the corpus's one built crossing does not discharge the onset gate's
> own record-side obligation list.  The two are not merely different arrows;
> they do not even have the same codomain conditions.
> ```

```text
S-1  *** GRADE = TRANSFERS-AS-SPECIFICATION *** [SPEC]
     Each of the nine is a property stated in terms a successor's own objects
     will have — durability, persistence under later writes, asymptotic
     non-return, recoverability, redundancy, centrality, superselection,
     inductive compatibility, orthogonal reduced supports.  NONE of the nine
     names this program's surface, action, carrier, germ, member, or gate.
     They were EXTRACTED from this corpus (each is quoted at O55SR §5.1 with
     its source line), but they are stated at a level of generality that
     survives the extraction.
     A successor can use the list as its own completeness check for any
     cell→record crossing it builds, and P-9's status ("STILL FALSE", nowhere
     produced) tells it which one is hardest.
     *** THE ADVERSE PROPERTY IS PART OF THE SPECIFICATION AND MUST TRAVEL WITH
     IT. ***  O55SR §5.2, :625-628, whole: "'PUBLIC' IS PREDICATED OF BOTH
     LEVELS, AND THEREFORE DOES NOT MARK THE CROSSING.  A naive reading of
     'durable public record' would take BOTH adjectives as record-level
     markers.  Only the first is."  And :645-648: "of the two adjectives in the
     onset gate's stated output, DURABLE is the one that requires a crossing and
     PUBLIC is not.  A reader who takes 'public' as the record-level marker will
     locate the crossing in the wrong place."
```

### §7.3 THE SPECIFICATIONS OF UNBUILT OBJECTS `[SPEC]`

```text
S-2  THE DISCRETE-TO-CONTINUUM EQUIVALENCE THEOREM.  Specified at DoR-007
     (§6.2, A-1) as "the stitching rule as a theorem over refinements", with
     its bar ("ADOPTION OF (M,g) … IS OFF THE TABLE"), its bite ("plan Task 4
     … checked at Task 6"), and its content ("the limit's cellulation-
     independence is the theorem's content", :22-23).  UNBUILT — the nearest
     artifact, T-24, proves "a maximal kinematic theorem" and states it "does
     not discharge cellulation independence."
     *** GRADE = TRANSFERS-AS-SPECIFICATION *** [SPEC]

S-3  THE DURABILITY MAP.  Specified by the onset gate's own next-gate clause,
     BOUNDARY_RECORD_ONSET…_V003:170-173, quoted whole:
       "Construct the source-flux-conditioned record-changing operator, then
        derive a complete action that fixes its source-conditioned identity
        phase, post-closure pointer block, causal cell, and durability map.
        No geometric uncertainty budget may be substituted for physical action
        without a theorem."
     STATUS OF ITS FORM, O55SR:1096: "'form supplied in none' of 5,512 files."
     *** GRADE = TRANSFERS-AS-SPECIFICATION *** [SPEC]
     A four-item requirements list on a complete action, plus one general
     anti-substitution bar ("No geometric uncertainty budget may be substituted
     for physical action without a theorem") that is stated in fully general
     terms and transfers on its own.

S-4  THE FOUR DURABILITY COMPLETION MECHANISMS — N-2, §5.1.  [SPEC]

S-5  THE SUPPLY ROUTE FOR A MAGNITUDE JUNCTION — T-8, §4.2.  [SPEC]
     "a change of ground supplying BOTH an exit operation AND a booked forcing
     equation" — two things, jointly.

S-6  THE SIX SCALARIZATION ROUTES AND THEIR COSTS — N-8, §5.3.  [SPEC]

S-7  THE CERTIFIED WITNESS INHABITING THE JOINT J1–J15 EQUALIZER — A-11.
     Specified precisely (six named generators; joint, not separate,
     inhabitance) and UNBUILT.  Its specification transfers as a warning about
     fiber products; its object does not.
     *** GRADE = TRANSFERS-AS-SPECIFICATION *** [SPEC] for the requirement;
     DEPENDS-ON-A-WITHDRAWN-OR-UNBUILT-OBJECT for everything tagged [EQ6].

S-8  THE MISSING RANK-PINNING PACKAGE — A-5.  Specified by DoR-014 as "sealed
     scalar source representation + rank-preserving intertwiner", and called by
     the ruling "the require-shaped would-build".
     *** GRADE = TRANSFERS-AS-SPECIFICATION *** [SPEC]

S-9  THE THREE STANDING DEMANDS W-1 / W-2 / W-3.  Quoted whole at O38SR §5.1
     from `STAGE8_DEMAND_REGISTER_O25SR_V001.md:142-157` (seal OK).  Each names
     a carrier that does not exist: W-1's CN-1 — "member-named topologies with
     continuity proofs … no member exists in the scored corpus to name them";
     W-2's CN-2 — "a member-supplied sealed prequotient rule (JD-3/JD-3a) with
     one displayed evaluation on a named oriented k-cell — absent from the
     scored corpus"; W-3 — the C-L2 certification at its consuming type, "its
     only permitted certification (C-L2 quadratic form)" with "the operator-norm
     route excluded (||[h_0, 1_B]|| = +infinity)".
     *** GRADE = DEPENDS-ON-A-WITHDRAWN-OR-UNBUILT-OBJECT *** as assets;
     *** the W-3 exclusion reason (an operator-norm route with an infinite
     commutator norm is unavailable, forcing a quadratic-form certification) is
     TRANSFERS-WHOLE as a constraint — it is standard unbounded-operator
     analysis. ***
     AND THE ADVERSE FINDING THAT DISPOSES OF THEM, O55SR:1100-1112, whole:
       "ENDPOINTS AT THE RECORD LEVEL: 0 of 6.
        ENDPOINTS AT THIS COMMISSION'S CELL LEVEL: 0 of 6.
        THEREFORE: no property of the cell level can ever reach these three
        demands — not because the crossing is missing, but because the demands
        do not lie on the cell->record axis at all.  Closing the formation
        crossing would not move them."
     A successor inherits the demands as a cautionary structure, not as work.
```

### §7.4 THE CROSSING CENSUS, AS A COUNT

O55SR §12, `:1085-1091`, whole:

> ```text
> Q4  CENSUS: 13 candidates.  BUILT CELL->RECORD CROSSINGS = 1 (X-1).
>     Failed 1 · named-but-unbuilt 4 · not-crossings 4 ·
>     off-scope third-level target 2 · relation-in-words 1.
>     FLATLY: the two levels touch, as a built object, EXACTLY ONCE — and
>     NOT at formation.  The formation chain crosses them ZERO times.
> ```

**Q4 TALLY (18 items: B-1..B-9, S-1..S-9).**

```text
TRANSFERS-WHOLE .............................. 6   (B-1, B-2, B-3, B-4, B-8, B-9)
TRANSFERS-AS-SPECIFICATION ................... 7   (S-1, S-2, S-3, S-4, S-5,
                                                   S-6, S-8)
CONSTRUCTION-DEPENDENT ....................... 2   (B-5, B-6)
DEPENDS-ON-A-WITHDRAWN-OR-UNBUILT-OBJECT ..... 3   (B-7, S-7, S-9)
INDETERMINATE-AT-BYTES ....................... 0
```

---

## §8 — Q5: METHOD

Method is graded on the same test: **does it depend on this program's
construction, or would a successor building a finite record carrier have it?**
Method is the one category where the answer is almost always the second — which
is why it is graded last and not least.

```text
M-1  *** THE CUSTODY DISCIPLINE ***
     WHAT IT IS, at bytes.  Three separable rules, each quoted from an artifact
     that practises it:
       (a) CONSUMPTION STRENGTH IS DECLARED AND NEVER UPGRADED.
           `STAGE8_NEUTRAL_COMPARAND_FAITHFULNESS_FABLE_V001.md:369-373`, whole:
             "CUSTODY: T1, T2, RF, W are CLAIMED artifacts, consumed at CLAIMED
              strength and never upgraded; PROVEN is used only where the citing
              artifact records it (N4's conservation blindness; the closed ratio
              mechanism); S1 has no sidecar and was rehashed at path with its
              lines pinned by T2's sealed table."
       (b) AUTHORSHIP IS DISCLOSED AT THE POINT OF ADOPTION.  Eleven rulings do
           it; the roll is §6.3.  The sharpest instances are DoR-020-A4's "the
           sealed contact/Ward stock provably does not force the overlap law"
           and DoR-009's "Nothing sealed forced the choice; it is the
           principal's, made in the open."
       (c) ASSEMBLIES ARE MARKED AS THE COMMISSION'S OWN.
           Same artifact, :374-380: "YOURS assemblies, marked: the organizing
           dichotomy of §3.1 …; the survey typings N1-N11 (each row cites its
           sealed ground); … None consumes a value, a scale, a metric, or a
           faithfulness premise."
     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: nothing but the existence of a corpus with artifacts of
     differing evidential strength.  The discipline is a bookkeeping rule over
     citations; it names no object of this program.  Any successor with lanes,
     drafts, and rulings can run it on day one.
     *** ITS DEMONSTRATED VALUE, AT BYTES: it is the ONLY reason this audit
     could separate the twenty-eight-plus authored items (§6.3) from the derived
     ones.  Without (b), every ruling would read as a derivation.  A successor
     that drops the custody discipline loses the ability to answer the question
     this commission was asked. ***

M-2  *** THE ADVERSARIAL BUILD-PLUS-REFUTE PAIRING ***
     WHAT IT IS, at bytes, and the coverage count this commission ran:
       In `alpha-program-archive/workspace`, artifacts named
       `…_{O|T|S}NN{SR|AD}_V001.md` number **94**; those carrying a paired
       `…_AUDIT_V001.md` number **88**.  Six builds are unpaired and are named
       so the coverage claim is exact:
         STAGE8_5D_SYMMETRIC_AUDIT_T13SR_V001   STAGE8_CONDITION_STATEMENT_O22SR_V001
         STAGE8_COUNTING_BOUND_O24SR_V001       STAGE8_GRAVITY_ACT_DRAFTS_S9AD_V001
         STAGE8_JD_MEMBER_CANDIDATE_T2SR_V001   STAGE8_RULE2_CANDIDATE_T15SR_V001
       *** PAIRING COVERAGE = 88/94 = 93.6%. ***
     ITS STRONGEST FORM — PRE-REGISTRATION OF THE REFUTER'S VERDICT BEFORE THE
     BUILD IS OPENED.  `STAGE8_AMPLITUDE_JUNCTION_S9AD_AUDIT_V001.md:291`,
     whole:
       "INDEPENDENCE = protocol executed — route enumeration, pre-verdict
        (VACANCY-CLOSED conditional on C12, by a different closure route), and
        attack checklist fixed in hashed notes (c29d0247) BEFORE the build was
        opened; build then read once in full and attacked at bytes; convergent
        verdicts by independent engines"
     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: two agents, a hash, and an ordering rule.  Nothing of
     this program's construction enters.  A successor gets the whole protocol —
     enumerate routes, fix a pre-verdict and an attack checklist under hash,
     THEN open the build — from the four lines above.
     *** WHAT MAKES IT MORE THAN A SLOGAN AT BYTES: the pairing produced
     CORRECTIONS THAT SURVIVED, and the audits name them.  The AJ audit's
     C-1/C-2/C-3 (a candidate family never named in the route tables; a
     mis-scoped Gleason kill; a CAS check covering only half the co-occurrence
     claim) were each found by the refuter, each repaired, and each recorded as
     "none load-bearing, verdict chain intact."  A discipline that produces
     corrections and records that they did not move the verdict is doing work
     that a self-review cannot do. ***
     ITS COST, CARRIED: the six unpaired builds are unrefuted, and this audit
     does not treat their verdicts as pair-tested.

M-3  THE TYPING SCHEME ITSELF (DoR-006).  Quoted whole from
     `DECISION_OF_RECORD_006_TYPE_P_ADOPTED_LAZY_MIGRATION_2026-08-01_V001.md:12-14`:
       "Typing scheme from this ruling forward:
          TYPE-R refuted . TYPE-U unbuilt . TYPE-S scope-empty . TYPE-C
          constraint-blocked (checks only) . TYPE-P premise-conditional .
          NO_VERDICT legal. Only TYPE-R is physical content."
     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: none.  Six categories over negative outcomes, with the
     load-bearing clause "**Only TYPE-R is physical content**" — i.e. a negative
     result is a fact about the world only when something was REFUTED; when it
     was merely unbuilt, out of scope, blocked, or premise-conditional, it is a
     fact about the program.  That distinction is the whole reason this audit
     could separate §4.7 from §5.  A successor can adopt the six-way scheme
     without adopting anything else in the corpus.
     ADVERSE, AND IT IS PART OF THE SAME RULING, :9-11: "Migration is LAZY: new
     artifacts use the new scheme immediately; the 487 existing TYPE-C mentions
     are re-typed only when their artifact is next touched. **No mass re-typing
     campaign.**"  See M-10.

M-4  *** THE RESTRICTION FALSIFIER (DoR-008's standing condition) ***
     Quoted whole, `:19-24`:
       "*** THE COMPLETED FRAMEWORK MUST REPRODUCE EVERY SEALED FINITE RESULT ON
        RESTRICTION TO ITS COMPLEX — Gate 1-4 structures, the composition-loop
        spectrum (R_square = 3/16), the four kernel planes, and every
        subsequently sealed finite theorem. ANY DISAGREEMENT ON RESTRICTION
        VOIDS THIS DECISION AND EVERYTHING TYPE-P ON IT. THE FINITE RESULTS ARE
        THE AUTHORITY; THE COMPLETION IS ANSWERABLE TO THEM, NEVER THE
        REVERSE. ***"
     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: the general relation between a finite object and a
     completion of it.  The rule — "the finite results are the authority; the
     completion is answerable to them, never the reverse" — is stated in fully
     general terms and names this program's objects only as INSTANCES (Gate 1-4,
     R_square, the kernel planes).  Strip the instances and the rule is intact.
     A successor building any continuum completion of a finite record structure
     inherits it whole.
     ITS PRINCIPAL'S BASIS, quoted at :26-27: "All we have to worry about is the
     finite if we assert that the infinite is simply an emergent"

M-5  MEMBER-SENSITIVITY TAGGING AND VOID-ON-DOWNSTREAM-FAILURE (DoR-017).
     Quoted whole, `:34-41`:
       "1. MEMBER-SENSITIVITY TAGGING: every downstream result in the stationary
           package and the response computation must be tagged member-sensitive
           or member-independent; the N/Z difference stays visible at every
           stage and is never silently absorbed.
        2. VOID-ON-DOWNSTREAM-FAILURE: the member's certificates (covariance,
           reality, batching, restriction) must continue to pass through the
           complement inverse, the Schur blocks, and the retarded extraction;
           any member-sensitive downstream failure VOIDS this ruling and reverts
           the square to the covariant fiber (Door-D style)."
     *** GRADE = TRANSFERS-WHOLE for rule 1; CONSTRUCTION-DEPENDENT for rule 2 ***
     Rule 1's dependence: the existence of a family from which a member was
     chosen.  Whenever a construction picks a member out of a family, every
     downstream result must carry a tag saying whether it depended on the
     choice.  That is a general anti-silent-absorption rule.
     Rule 2 names this program's certificates and blocks, and is bound to them.

M-6  THE NO-SELECTION PRINCIPLE, AND CARRIAGE INSTEAD OF CHOICE.
     Instituted at DoR-013 (":*** NO MEMBER IS SELECTED, EVER. ***", with the
     p_ch-neutrality certificate named as "the license"), and again at
     DoR-020-A3 ("with ALL members retained. No source member is selected from a
     target"), DoR-020-A7 (both branches carried, "NO SELECTION — the program's
     no-selection principle applied to its own boundary condition"), and
     DoR-015 ("under STRICT NO-SELECTION").
     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: the existence of a family and a certificate that the
     downstream object is neutral across it.  The principle has a precise
     content that is not merely cautious: **you may work with a family instead
     of a member exactly when you can certify that the quantity you want is the
     same for every member** — and where you cannot, you carry both branches
     conditionally and let a later test decide.  Both halves are general.
     ITS COST, CARRIED FROM A-18: carrying rather than choosing leaves an object
     INDETERMINATE, and DoR-020-A7 says so ("each branch's content remains
     untyped-by-stock").

M-7  THE Θ-PARITY BOOKKEEPING (DoR-014 Amendment 2).  The rule as practised,
     :7-10: an odd factor belongs on the side whose convention already carries
     it; the object is then EVEN and "fits the exponent's parity".
     *** GRADE = TRANSFERS-WHOLE *** — dependence: a doubled/CTP-style
     construction with a parity involution.  Any successor with a CTP doubling
     has the same bookkeeping obligation and the same failure mode.

M-8  DERIVED-OR-DECLARED, NEVER IMPLICIT (DoR-019).  :29-30, whole: "Derived-or-
     declared, never implicit (the principal's clarification of record, Q-382):
     any future cross-sector conversion arrow must be separately declared."
     With the mechanism that enforces it, :17-19: "R4-ONLY conversion routing
     with the failure-capable NO_IMPLICIT_CROSS_SECTOR_UNIT certificate
     (residual-parameter audit: none exists undeclared)".
     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: the existence of two sectors with different units and an
     arrow between them.  The rule and — importantly — the FAILURE-CAPABLE
     certificate that enforces it are both general.  Note the qualifier
     "failure-capable": a certificate that cannot fail is worthless, and the
     corpus knows this (see M-11).

M-9  THE TWO GENERAL FAILURE MODES NAMED AT DoR-020-A6.  :12-13, whole: "both
     lawful routes from current stock are proven closed (unconstrained lift =
     selection; reader-derived pi_Mx = the F_PLDEC circularity class)."
     *** GRADE = TRANSFERS-WHOLE ***
     Two named traps, both general: **an unconstrained lift is a selection in
     disguise**, and **deriving the reader from the thing the reader is meant to
     decide is circular**.  Neither names an object of this program; both are
     stated as classes ("the F_PLDEC circularity class").

M-10 *** THE TYPED-NEGATIVE PROTOCOL, AND ITS KNOWN COVERAGE LIMIT ***
     `STAGE8_TYPING_COVERAGE_O51SR_V001.md` (seal OK) is the artifact that
     measures it, and its audit `…_AUDIT_V001.md` (seal OK) is the paired
     refuter.

     THE PROTOCOL'S RULES, quoted from the implementing file via O51SR §4.2:
       Rule 1, `NEGATIVE_RESULT_TYPING_PROTOCOL_V001.md:59`, whole:
         "1. **Every `= false` flag and every 'not found' carries its type.**
             Untyped negatives are not findings."
       Rule 5, `:72`, whole:
         "5. *** A NEGATIVE CARRIES THE SAME EVIDENTIARY BURDEN AS A POSITIVE.
             *** Reporting 'not found' requires stating the search."
       Its own status line, `:5`: "protocol_status = PROPOSED_FOR_ADOPTION;
       applies to every lane and to the reviewer."

     *** THE KNOWN COVERAGE LIMIT, STATED AS PART OF THE GRADE — three distinct
         limits, each measured at bytes: ***

       (L-i) THE MANDATE/IMPLEMENTATION GAP.  O51SR §0, whole:
             "THE MANDATE'S SCOPE IS STATED, AND IT IS UNIVERSAL — `TYPE EVERY
              NEGATIVE` (`LOCKED_PROCESS.md:97`, in corpus, sealed OK). THE
              PROTOCOL THAT IMPLEMENTS IT SCOPES ITSELF TO TWO SYNTACTIC FORMS
              — 'every `= false` flag and every "not found"'. THE GAP BETWEEN
              THOSE TWO SENTENCES IS THE WHOLE FINDING."
             MEASURED: "untyped barriers outnumber typed ones 5,206 to 778 — a
             ratio of 6.7 : 1", surviving an eightfold window widening
             (4,190 of 5,206 still untyped at ±40 lines), and "59.9% of untyped
             barriers sit in files that carry no type flag anywhere at all."
             *** THE PROTOCOL REACHES FLAG-FORM AND "NOT FOUND" NEGATIVES.  A
             BARRIER STATED IN PROSE IS OUTSIDE ITS REACH. ***

       (L-ii) THE LIMIT IS NOT A LEGACY BACKLOG, AND THAT MATTERS FOR TRANSFER.
             O51SR §0, whole: "**The untyped are NOT older.** July/August split
             is 18.7 / 81.3 for untyped against 20.3 / 79.7 for typed. The
             'legacy migration backlog' framing the corpus uses for its own
             untyped mass **does not describe this population.**"
             AND: "**The untyped ARE analytic.** Analytic vocabulary in the
             barrier line: **26.8% of untyped against 8.6% of typed.** The
             `diverges` lexeme alone runs **38.8 : 1 untyped-to-typed**."
             *** A SUCCESSOR ADOPTING THE PROTOCOL UNCHANGED WILL MISS ITS
             ANALYTIC BARRIERS AT ROUGHLY THREE TIMES THE BASE RATE. ***

       (L-iii) PARTIAL COVERAGE IS RATIFIED BY NAME.  O51SR §7.1 quotes
             DoR-006 whole and concludes, :768-770: "**'No mass re-typing
             campaign' is a ratified acceptance that typing coverage will be
             partial and uneven.**  Its scope is the C→P migration of 487
             mentions, and it is not read here as governing anything wider."
             AND, at S12: "typing tokens across the 28 rulings … **9 of 28**
             carry any; 19 carry none."

     THE ARTIFACT'S OWN RECONCILIATION, quoted whole because it bounds its own
     claim and that bound is part of the honest grade, :944-950:
       "The headline does **not** say 5,206 adjudications escaped the protocol —
        S9's own sample found the summary-headline sub-class (§5.4/S9) that
        inflates any such reading, and S8 bounds it at 40.1%. **What the
        evidence supports is exactly: the protocol's coverage falls roughly an
        order of magnitude short of the class its mandate names; the shortfall
        is not explained by age or by inheritance; and it concentrates in
        analytic barriers and in reviewing artifacts.**"

     *** GRADE = TRANSFERS-WHOLE, WITH THE COVERAGE LIMIT AS PART OF THE
         GRADE ***
     DEPENDENCE CITED: two syntactic forms and a six-way type scheme.  The
     protocol names no object of this program and a successor can run it
     immediately.  **What transfers is the protocol TOGETHER WITH its measured
     limit: it covers flag-form and "not found" negatives, it does not reach
     prose barriers, the shortfall is roughly an order of magnitude, it is
     concentrated in analytic statements, and partial coverage was ratified
     rather than merely tolerated.**  A successor that adopts Rule 1 and Rule 5
     without adopting the measurement will believe its negatives are typed when
     6.7 in 7.7 of them are not.
     Rule 5 alone — "A NEGATIVE CARRIES THE SAME EVIDENTIARY BURDEN AS A
     POSITIVE.  Reporting 'not found' requires stating the search." — is
     TRANSFERS-WHOLE on its own and is the single sentence this audit relied on
     most in constructing §1's leak counter and §2's probe.

M-11 THE CANNOT-FAIL-CHECK CLASS.  Named at
     `RESULT_TRACE_COLLAPSE…_2026-07-29.md:211-217`, whole:
       "(a) **THE PRODUCER GATE IS PARTLY TAUTOLOGICAL.** … makes `K_H = 1.5
        K_Q` and `K_QH = K_Q` PASS/FAIL conditions at `2e-14`; … ALL THREE ARE
        IDENTITIES OF THE CONSTRUCTION AND CANNOT FAIL. The
        `PASS_COMMON_BR_LOCAL_COEFFICIENT_FUNCTIONS_DEPTH_OPEN` flag is
        correspondingly weaker than it reads. THIS IS A THIRD AND FOURTH
        INSTANCE OF THE CANNOT-FAIL-CHECK CLASS (baseline had 2)."
     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: none.  **A check whose passing is an identity of the
     construction tests nothing, and its flag reads stronger than it is.**  The
     corpus names the class, counts instances (4 of record), and the diagnosis
     is available to any successor with automated gates.  This is the single
     most portable defect class in the corpus, and it is paired with M-8's
     "failure-capable" requirement as its remedy.

M-12 *** THE QUESTION-INDEXED REGISTER FORM ***
     WHAT IT IS, observed at bytes ACROSS THE RULINGS ONLY (the register itself
     is a BARRED file and was never opened; the form is graded from its
     citations, which are everywhere):
       Every ruling carries a register head or evidence range as its provenance
       anchor — DoR-004 "Register head Q-175"; DoR-005 "Register head Q-198";
       DoR-008 "Evidence: Q-203, Q-207, Q-208, Q-211"; DoR-009 "Evidence: Q-229
       through Q-233"; DoR-013 "Q-265, independently verified Q-266";
       DoR-016 "the forced diagram (derived, Q-358)"; DoR-018 a full provenance
       chain "Germ V001 killed (Q-372) -> DP certificate (Q-373) -> DoR-019
       geometry (Q-374-384) -> germ V002 (Q-385/386) -> V003 lambda retype
       (Q-387) -> mispaste event and build agreement (Q-388/389)";
       DoR-020 a gate history "Package V001 killed (Q-413) -> V002's F_PLDEC
       witness killed by the hostile check (Q-415) -> V003 two routes (Q-416)
       -> V004 square derived, P bound (Q-418) -> P_CM020 killed on proof
       burden (Q-419) -> V005 honest obstruction (Q-420) -> the six-generator
       bedrock theorem (Q-421)."
     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: a monotone integer index and the rule that every
     decision cites the question it answers.  Nothing of this program's physics
     enters.  **What it buys, demonstrated at bytes: a ruling's provenance is a
     CHAIN OF KILLS, not a chain of successes — DoR-018 and DoR-020 both record
     their own dead candidates in order, by index.  A successor that indexes
     questions rather than answers inherits the ability to say which attempts
     died and when.**
     *** ITS KNOWN FAILURE MODE, CARRIED, AND IT IS SEVERE: the index resolves
     only if the register exists and is reachable.  This commission could not
     resolve a single `Q-…` token, because the register is barred; the T16SR
     partition theorem records the same condition in its own sweep cutoff
     ("'Q-…' tokens EXPECTED-UNLOCATABLE, treated as opaque labels carried
     inside sealed artifacts").  **AN INDEX THAT POINTS INTO A SINGLE
     NON-REDUNDANT FILE IS A SINGLE POINT OF FAILURE FOR THE WHOLE PROVENANCE
     LAYER.** ***

M-13 THE PROCESS-DEFECT DISCIPLINE (the loss-class finding).
     `RESULT_TRACE_COLLAPSE…:76-78`, whole:
       "REVIEWER FINDING ON PROCESS: the reviewer lane lost its OWN result
        within 24 hours and ordered a re-derivation of it. Same loss class as
        the deleted rescaling-exclusion section and the 718 uncited root
        artifacts, at a 1-day timescale inside the supervision layer itself."
     and the erratum obligation it books, :219-226 ("An erratum pointer is
     owed, by the same append-only mechanism as `ERRATUM_001`", against four
     supervision artifacts that "remain unamended", one of them SEALED).
     *** GRADE = TRANSFERS-WHOLE ***
     The named loss class — a result derived, unrecorded in prose, and lost
     inside 24 hours — plus the append-only erratum mechanism as its remedy,
     are both general.  So is the sharper finding: **a retraction that is
     "SINGLE-SOURCE AND UNSEALED" does not amend four sealed artifacts that
     cite the retracted claim.**

M-14 THE SEALED-BEFORE-AUTHORING DESIGN DISCIPLINE.  Practised at
     `STAGE8_AMPLITUDE_JUNCTION_S9AD_V001.md:3-5`, whole: "Governing design:
     `BARE_SURFACE_AMPLITUDE_JUNCTION_DESIGN_V001.md` (sealed BEFORE any run;
     read in full; its question, ground, honest-outcome menu, and every
     requirement bind verbatim)"; and at
     `STAGE8_T7_PRODUCTION_GATE_NOGO…:6`: "APPEND_ONLY_REPAIR_BINDING_SEALED_
     BEFORE_AUTHORING".
     *** GRADE = TRANSFERS-WHOLE ***
     DEPENDENCE CITED: a hash and an ordering.  The load-bearing element is the
     **HONEST-OUTCOME MENU sealed before the run** — the set of verdicts the
     build is permitted to return, fixed before it can know which one it wants.
     That is the anti-fitting device that makes VACANCY-CLOSED a finding rather
     than a preference, and it is fully general.
```

**Q5 TALLY (14 items).**

```text
TRANSFERS-WHOLE .............................. 13  (M-1, M-2, M-3, M-4,
                                                   M-5(rule 1), M-6, M-7, M-8,
                                                   M-9, M-10, M-11, M-12,
                                                   M-13, M-14)
   — counted as 13 whole items; M-5 is split (rule 1 transfers, rule 2 does not)
CONSTRUCTION-DEPENDENT ....................... 1   (M-5 rule 2)
TRANSFERS-AS-SPECIFICATION ................... 0
DEPENDS-ON-A-WITHDRAWN-OR-UNBUILT-OBJECT ..... 0
INDETERMINATE-AT-BYTES ....................... 0
```

**METHOD IS THE CATEGORY WITH THE HIGHEST TRANSFER RATE IN THE CORPUS, AND IT IS
NOT CLOSE.** That is a report of what the bytes show, not a recommendation.

---

## §9 — Q6: WHAT EXPLICITLY DOES NOT TRANSFER

Stated plainly, and named. Each item is a thing a successor **cannot take**, with
the byte that makes it so.

### §9.1 ASSETS RESTING ON WITHDRAWN, KILLED, DEFECTIVE, OR SUPERSEDED OBJECTS

```text
X-1  THE DISCREPANCY COCYCLE beta_f, AND EVERYTHING QUOTING IT.
     Its only definition sits in a build the corpus calls KILLED and grades
     "STAGE1_ASSEMBLY = DEFECTIVE (V1,V2,V3,V4,V5,V6)"; `beta_N` — the map it
     would be a value of — is "never defined anywhere"; and beta_f "is
     therefore **not** a map with its own source and target."  O38SR's verdict,
     whole: "THIS ONE IS UNADOPTED, AND IN PART KILLED."
     *** DOES NOT TRANSFER. ***

X-2  ANYTHING RESTING ON DoR-020-A1's CLAUSE-LAYER-COMPLETENESS STATEMENT.
     Superseded TWICE, by A4 (":7") and A5 (":8-9"), each in its own words.
     *** DOES NOT TRANSFER. ***

X-3  ANYTHING RESTING ON THE PRE-AMENDMENT FUNCTIONAL J4.
     DoR-020-A3 :19-20: "The functional J4 was REFUTED on cycle creation (the
     vertical-increment counterexample …)."
     *** DOES NOT TRANSFER. ***

X-4  ANYTHING RESTING ON DoR-014 AMENDMENT 1's FORM `b := i·hbar·L⊗L`.
     Amendment 2's title says it: "THE PAIRING NORMALIZATION CORRECTED
     (SUPERSEDES AMENDMENT 1's FORM)".
     *** DOES NOT TRANSFER (the CONTENT does; the FORM does not). ***

X-5  ANYTHING RESTING ON THE CHOICE C-B PAIRING.  DoR-014 Amendment 1 :6-8:
     "Choice C-B … is VOID — its own raw-G-disagreement void condition fired
     (Q-300)."
     *** DOES NOT TRANSFER. ***

X-6  ANYTHING TAGGED [EQ6].  DoR-020's own licence clause, :20-22:
     "FORBIDDEN until a certified witness exists: binding a member, executing
      the fixed-point computation, any end test."  The witness is unbuilt; the
     six generators are a joint premise and "separate nonemptiness of all six
     provably does not imply joint inhabitance."
     *** DOES NOT TRANSFER while the joint equalizer is uninhabited. ***

X-7  ANYTHING RESTING ON Ξ_N HAVING AN INHABITANT.  DoR-020-A9's own sentence:
     "ADOPTION LICENSES; IT INHABITS NOTHING: the gates ExtSrc, G4-D, G5,
      FULL-G4, G2-N remain displayed and open."
     *** DOES NOT TRANSFER. ***

X-8  ANYTHING RESTING ON FULL J2 ON THE NEW-CYCLE FACTOR.  DoR-020-A6:
     "both lawful routes from current stock are proven closed."
     *** DOES NOT TRANSFER. ***

X-9  THE PINNED GERM PARAMETER (r_0, r_ch).  DoR-014: "Pinning of the pair:
     NO_VERDICT of record — refuted on every executable scalar arm."
     *** DOES NOT TRANSFER — the germ is adopted, its parameter is unpinned. ***

X-10 THE KALUZA-KLEIN FRAMING AND THE 5D EINSTEIN-HILBERT ROUTE.
     DoR-003, TYPE-S on two flags and a TYPE-R refutation of the granted
     ansatz.  *** DOES NOT TRANSFER — and DoR-003 IS the transferable asset
     here (A-0): the NEGATIVE transfers, the framing does not. ***

X-11 THE SIX UNPAIRED BUILDS' VERDICTS AS PAIR-TESTED RESULTS (M-2).
     They may be correct; they are not refuter-tested, and this audit does not
     grade them as though they were.
     *** DOES NOT TRANSFER AT PAIR-TESTED STRENGTH. ***

X-12 THE FOUR SUPERVISION ARTIFACTS CITING THE RATIOS AS EXECUTED DYNAMICAL
     EVIDENCE.  `RESULT_TRACE_COLLAPSE…:219-226`, whole: four named artifacts
     assert "the forced-ratio mechanism has been EXECUTED in-tree … numerically
     asserted to 2e-14 per sampled depth" and "not a hope — it is an executed
     in-tree result"; "The 2026-07-29 retraction at `CONTINUATION_STATE.md:2347`
     is SINGLE-SOURCE AND UNSEALED and those four remain unamended. THE FIRST IS
     SEALED. An erratum pointer is owed".
     *** DOES NOT TRANSFER — and a successor reading the sealed one first would
     inherit a retracted claim at sealed strength.  This is the corpus's own
     sharpest warning about its own record. ***
```

### §9.2 ASSETS RESTING ON THE THREE FENCES' RATIONALE

The three fences — `alpha_computed = false`, `proof_authorized = false`,
`kappa_record_computed = false` — appear on nearly every artifact in the corpus,
including this one. **The fences are a discipline; their RATIONALE is a
program-specific bet, and the rationale is what does not transfer.**

```text
X-13 THE FENCE RATIONALE ITSELF.  What the fences are FOR, at bytes, is an
     ordering: a value is computed only after a named sequence of gates, and is
     compared to a measured constant exactly once, at the end.
     `STAGE8_DECLARATION_GATE_PROVENANCE_O53SR_V001.md:601-608` quotes the
     sequence whole from a barred-adjacent instrument's readable citation:
       "The end test is a defined object of the **frozen release condition**:
        FENCE 3 / R3.4 — 'The end test is run ONCE by a lane that has never seen
        the measured value in this program's context, cross-checked once,
        registered whatever it says.'"
     *** THIS RATIONALE PRESUPPOSES A PROGRAM WHOSE OUTPUT IS ONE NUMBER
     COMPARED ONCE TO ONE MEASURED CONSTANT.  A successor on a different
     footing — one whose output is a structure, a constraint, or a family —
     has no object for the fences to fence, and inherits the ordering rule with
     nothing to order. ***
     *** DOES NOT TRANSFER as rationale. ***
     WHAT DOES SURVIVE, and it is not the same thing: the ANTI-FITTING CONTENT
     — a lane that has never seen the measured value; one comparison; register
     whatever it says.  That is M-14's sealed-honest-outcome-menu discipline in
     another dress, and it is graded TRANSFERS-WHOLE there.

X-14 THE ELEVEN FENCE INSTRUMENTS AS A SYSTEM.
     `RESULT_FENCE_INVENTORY_AND_WHAT_IS_TESTABLE_TODAY_2026-07-29.md:6-14`
     (seal OK), whole in substance: ten of eleven forbid measured quantities
     ENTERING a derivation, selection by value, alpha being evaluated out of
     seal order, target comparison as a repair mechanism, one named external
     lineage, and the confirmatory claim.  Its own conclusion, :16:
       "NONE OF THESE FORBIDS A PRE-REGISTERED DIAGNOSTIC COMPARISON OF A
        DERIVED DIMENSIONLESS RATIO."
     *** DOES NOT TRANSFER as a system *** — the eleven instruments name this
     program's scripts, manifests, and version-pinned files.
     WHAT TRANSFERS is the CLASSIFICATION AXIS the inventory introduces:
     **entry bans are not comparison bans**, and a corpus can carry ten of the
     first while believing it carries the second.  That distinction is general.
```

### §9.3 THE RELEASE CONDITION FOR A COMPUTATION THAT WOULD NOT OCCUR

```text
X-15 *** G3 AND ITS NONEXISTENT AUTHORIZATION. ***
     `RESULT_FENCE_INVENTORY…:18-19`, the ban itself, whole:
       "G3 carriers, both in `_external_handoffs`: … 'no output may be compared
        to any measured constant before Stage 12 authorizes the single
        comparison.'"
     THE THREE FACTS ABOUT IT, from the same artifact, :21-38:
       "(a) BOUNDED NEGATIVE (root: cleanroom): `19_DIMENSIONLESS|45_STAGE10|
            21_DIMENSIONLESS` returns ZERO files. Neither carrier is cited,
            pinned, or hash-bound in the current cleanroom."
       "(b) THE CLEANROOM EXPLICITLY REPLACED IT. … **THE REPLACEMENT CONTAINS
            NO COMPARISON CLAUSE** and binds only kappa_record and functions of
            it"
       "(c) **STAGE 12 DOES NOT EXIST.** … 'stage_12 = NEVER_EXISTED';
            'stage12_exists_in_corpus = false'. … ZERO definitions, ZERO
            authorizations."
     AND THE CONSEQUENCE THE ARTIFACT STATES IN ITS OWN VOICE, :40-43, whole
     and unsoftened:
       "**CONSEQUENCE, STATED WITHOUT SOFTENING. Read literally, G3 does not
        make the program untestable until eighteen obligations are discharged —
        IT MAKES THE PROGRAM UNTESTABLE PERMANENTLY, because the authorization
        it defers to was never written, and the corpus contains no procedure
        for"
     *** DOES NOT TRANSFER. ***
     A RELEASE CONDITION THAT DEFERS TO AN AUTHORIZING STAGE THAT NEVER EXISTED
     IS NOT A CONDITION; IT IS A PERMANENT BAR WITH A DATE ON IT.  Any asset
     whose value is "it will be testable when the gate opens" rests on a gate
     with no opening procedure of record.
     *** AND THE TWO G3 CARRIERS ARE AMONG THE 55 ARTIFACTS CARRYING ONLY THE
     BARE SIDECAR FORM (§2): `cleanroom_output/19_DIMENSIONLESS_RATIO_SPEC_V001.md`
     and `cleanroom_output/45_STAGE10_HANDOFF_GEOMETRIC_BRIEF_V001.md`.  The
     ban that makes the program permanently untestable is carried by two files
     that are outside the normalized sidecar convention. ***

X-16 CONSEQUENTLY: ANY ASSET WHOSE VALUE IS ITS PLACE IN THE END-TEST SEQUENCE.
     The sequence quoted at O53SR:607-608 from a readable citation —
     "…α = 1/(4πK*) → **end test once** → **gravity close** … → THE SIGNATURE."
     Every asset graded here that is valuable ONLY as a step toward that
     sequence carries X-15's defect.
     *** DOES NOT TRANSFER. ***
```

### §9.4 TERMS WITH NO CONSTITUTIVE DEFINITION

```text
X-17 *** "THE DECLARATION GATE." ***
     `STAGE8_DECLARATION_GATE_PROVENANCE_O53SR_V001.md:23-33` (seal OK; paired
     audit seal OK), verdict quoted whole:
       "**Q1 = ABSENT.** Across 12,935 swept files in three roots, the term
        'declaration gate' occurs **46 times in 34 files = 29 distinct
        occurrences in 20 distinct artifacts** (mirror pairs collapsed). Of
        these, **17 are untouched-assertions**, **11 are references/custody-
        assertions** ('it is the principal's'), **1 is an unrelated software
        homonym**, and **0 are definitions** and **0 are constitutions**. No
        ruling, spec, plan, register, relay, or instrument anywhere states what
        the declaration gate **is**, what it gates, what its criteria are, or
        what taking it would mean. The term entered the record on 2026-08-14
        already in the untouched/custody form, in a lane artifact reproducing
        discipline language from a commission brief that is **not on disk**, and
        every one of the 28 subsequent occurrences inherits it. **It was never
        constituted.**"
     The audit's own operationalization check, `…_AUDIT_V001.md:622`: the count
     "is 0 under every reading tested."
     *** DOES NOT TRANSFER — THERE IS NOTHING TO TRANSFER. ***
     A gate asserted untouched 17 times, referenced 11 times, and defined 0
     times is a term, not an object.  A successor cannot inherit it, cannot
     discharge it, and cannot even determine whether it was ever satisfied.
     The commission that found this recorded that "A principal act (road item
     20) is blocked on this return."

X-18 `beta_N`.  O38SR:333, whole: "`beta_N` is **never defined anywhere**."
     Yet the composition law beta_gf = beta_g + Eta_g(beta_f) is written as
     though a map existed.
     *** DOES NOT TRANSFER. ***

X-19 THE "DURABILITY MAP" AS AN OBJECT (as opposed to a specification).
     O55SR:1096: its "form supplied in none" of 5,512 files.  The NAME transfers
     as S-3's specification; the OBJECT does not exist.
     *** THE OBJECT DOES NOT TRANSFER; THE SPECIFICATION DOES. ***

X-20 THE COMMISSION BRIEF THAT INTRODUCED THE DECLARATION-GATE LANGUAGE.
     O53SR: the originating lane artifact reproduced "discipline language from a
     commission brief that is **not on disk**."
     *** DOES NOT TRANSFER — the source of the term is off-corpus. ***
```

### §9.5 THE ONE-LINE STATEMENT OF Q6

```text
A successor cannot take: the discrepancy cocycle and its composition law
(killed source, undefined map, not-a-map); the clause-layer-completeness
statement (superseded twice); the pre-amendment J4 (refuted); Amendment 1's
pairing form and choice C-B (voided); everything tagged [EQ6] (uninhabited
joint equalizer); Ξ_N's inhabitation (five open gates, by its own ruling);
full J2 on the new-cycle factor (both routes proven closed); the pinned germ
parameter (NO_VERDICT); the Kaluza-Klein framing (TYPE-S/TYPE-R); the six
unpaired builds at pair-tested strength; the four unamended supervision
artifacts asserting executed dynamical evidence (retraction single-source and
unsealed, one of the four SEALED); the three fences' RATIONALE (it presupposes
a one-number-compared-once program); the eleven fence instruments as a system;
G3 and anything whose value is its place in the end-test sequence (its
authorizing Stage 12 "NEVER_EXISTED", and the corpus contains no procedure to
supply it); "the declaration gate" (0 definitions in 12,935 files); `beta_N`
(never defined anywhere); the durability map AS AN OBJECT; and the off-disk
commission brief the declaration-gate language came from.
```

---

## §10 — FLAG BLOCK

```text
F-1  *** THE MOST TRANSFERABLE NO-GO IN THE CORPUS IS UNSEALED. ***
     `BID_FINITE_RECORD_DURABILITY_NO_GO_V001.md` carries NO sidecar in either
     form, in either root.  Cross-root byte-identity established (both copies
     2a13fde3…) as a substitute; that is agreement between two copies, not seal
     verification.  N-1, N-2, N-3, N-4 all rest on it.

F-2  THE U(1) BUNDLE AND ITS CONNECTION ARE UNSEALED.
     `LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md` carries no sidecar in either root
     (independently recorded by O38SR: "NO SIDECAR IN EITHER ROOT —
     UNVERIFIABLE").  T-16, T-17, T-18, B-3, B-4 all rest on it.

F-3  1,792 OF 6,930 ALLOWED .md ARTIFACTS CARRY NO SIDECAR IN EITHER FORM
     (25.9%).  55 carry ONLY the bare form and therefore still lack the
     normalized `<stem>.md.seal.sha256`; both G3 carriers are among the 55.

F-4  SIDECAR-COUNT DISCREPANCY.  The commission's premise names 282 sidecars
     added 2026-08-16; at bytes the permitted roots carry 334 with that mtime.
     INDETERMINATE-AT-BYTES; not adjudicated.

F-5  A LOCATOR CORRECTION TO A PRIOR COMMISSION.  O38SR records
     `DOR_020_A4_J12_CONTACT_GLUE_STRICT_PUSHOUT_2026-08-04.md` as "ABSENT FROM
     BOTH ROOTS … Not readable. Not verified. Cited by SHA only."  At this
     commission's bytes it is PRESENT and seal-verifying in BOTH supervision
     roots and is quoted whole at §6.2 A-15.  O38SR's declared roots were
     workspace + cleanroom, not supervision; the absence is an absence from its
     SCOPE.  **REPORTED, NOT REPAIRED — O38SR's verdict on beta_f rests on three
     further dependencies (killed source, undefined beta_N, not-a-map) that this
     correction does not touch, so its grade stands.**

F-6  A CELL-DIMENSION DISCREPANCY INSIDE THE ONE BUILT CROSSING.
     `FORK_8…RESULT_V001.md:51-62` writes `tensor_(j=1)^N M_3(C)`;
     `CAUSAL_DIRECT_LIMIT_COVECTOR_RAY_LIFT_SPEC_V001.md:46-50` writes
     `A_N = tensor_(j=1)^N M_2`.  Both are quoted, as quoted, in O55SR.
     RECORDED, NOT ADJUDICATED — the direct-limit construction is indifferent to
     the factor dimension, so the grade at B-1 is unaffected; the discrepancy is
     flagged because a successor copying either line would copy a number the
     corpus does not agree on.

F-7  A SEALED-CONSUMPTION DEFECT OF RECORD.  A closure-lane artifact refused the
     flux gate as "unsidecared" three weeks after its sidecar was written and
     verifies (O51SR-frontier :84-108).  The refusal's ground is false at bytes;
     its cause is the sidecar-convention split.  Not repaired here.

F-8  FOUR SUPERVISION ARTIFACTS, ONE OF THEM SEALED, STILL ASSERT A RETRACTED
     CLAIM.  The retraction is single-source and unsealed.  An erratum pointer
     is owed by the corpus's own append-only mechanism (X-12).

F-9  A NAMED OPEN INSIDE A RATIFIED AXIOM.  DoR-020-A2: "NAMED OPEN (not
     amended, not silently touched): A_J2's extent clause of A_extent's shape."

F-10 RULING-NUMBER GAPS.  No 001, 002, or 012 under either prefix in either
     supervision root.  INDETERMINATE-AT-BYTES; recorded, not adjudicated.

F-11 NINETEEN OF THE 28 RULINGS CARRY NO TYPING TOKEN AT ALL (O51SR S12: "9 of
     28 carry any; 19 carry none").  The typed-negative protocol does not reach
     the record layer that adopts objects.

F-12 *** BAR INCIDENT, SELF-REPORTED. ***  One content-bearing sweep (a
     line-grep for the string "release condition" across the archive, run
     BEFORE the barred-basename filter was applied to that particular sweep)
     returned ONE matched line from `supervision/QUESTIONS_SETTLED_REGISTER_V001.md:115`,
     a BARRED file.  Recorded exactly:
       - The file was NEVER OPENED; one grep-matched line was displayed.
       - THAT LINE IS CITED NOWHERE IN THIS ARTIFACT AND CARRIES NO PREMISE.
       - The finding it touched (G3's release condition, X-15) is sourced
         ENTIRELY from `supervision/RESULT_FENCE_INVENTORY_AND_WHAT_IS_TESTABLE_
         TODAY_2026-07-29.md` (seal OK, NOT barred) and from
         `STAGE8_DECLARATION_GATE_PROVENANCE_O53SR_V001.md` (seal OK, not
         barred), both of which state it independently and are quoted at §9.3.
       - X-15 survives the incident intact: delete the leaked line and every
         quoted span in X-15 remains, at its own unbarred source.
     Three further sweeps returned BARRED BASENAMES ONLY (filename listings, no
     content): `QUESTIONS_SETTLED_REGISTER_V001.md` and
     `QUESTIONSSETTLED_REGISTER_V001.md` appeared in file-location listings for
     the tokens "vacancy", "onset gate", "flux gate", and "triple-overlap".  No
     content was returned or read from any of them.
     *** THE §1 LEAK COUNTER MEASURES THE FILE-ENUMERATION SWEEP, WHICH LEAKED
     ZERO.  IT DID NOT COVER AD-HOC LINE-GREPS.  THAT IS THE GAP THIS INCIDENT
     EXPOSES, AND IT IS REPORTED RATHER THAN ABSORBED. ***

F-13 THE FOUR PROPERTIES THIS AUDIT COULD NOT REACH.  `Q-…` register tokens are
     EXPECTED-UNLOCATABLE (the register is barred).  The membership theorem
     (T-21) was not opened in full.  `RECORD_FORMATION_PROGRAM_DESIGN_*` was
     excluded and never opened.  `FINISH_B_*` was not consulted.  Each is a
     declared gap, not a silent one.
```

---

## §11 — MASTER ITEMIZATION: EVERY TRANSFERS-WHOLE AND TRANSFERS-AS-SPECIFICATION
## ITEM, WITH ITS DEPENDENCE CITED

Duplicates across categories are collapsed and the collapse is noted, so the
count is of DISTINCT ASSETS.

### §11.1 TRANSFERS-WHOLE — 31 distinct assets

```text
W-01  THE QUANTIZATION CLASS IS EXACTLY ℤ  (T-1)
      DEPENDS ON: single-valuedness of a character of U(1); the solution set of
      exp(2πix) = 1 over ℂ and over ℝ.  Standard character theory.

W-02  FAITHFULNESS ⟺ |n| = 1; WEAK DISTINGUISHABILITY ⟺ n ≠ 0  (T-9)
      DEPENDS ON: the kernel ladder of the characters of U(1) — kernel is all of
      U(1) at n=0, μ_{|n|} for |n|>1, trivial for |n|=1.

W-03  UNIQUENESS-GIVEN-EXISTENCE OF |n|  (T-10)
      DEPENDS ON: injectivity of x ↦ x² on the nonnegative integers.

W-04  THE TRACE COLLAPSE THEOREM  (T-12)
      DEPENDS ON: Schur's lemma applied to adjoint-irreducible sl(N) inside
      gl(N) = sl(N) + center; exterior-power weight combinatorics; Pascal's
      identity.  Verified independently at N = 3,4,5,6, every k.

W-05  THE SECOND-MOMENT ADMISSIBILITY CRITERION  (T-13)
      DEPENDS ON: linear algebra on the weight lattice of a simple algebra
      (proportionality of Σ_s w_s μ_s ⊗ μ_s to the Cartan metric) plus a finite
      exhaustive enumeration.  Replaces class-functionhood as the honest test.

W-06  NO x-INDEPENDENT GRAVITY/GAUGE RATIO ON A CARRIER WITH A TRIVIAL SUMMAND
      (T-14)
      DEPENDS ON: (i) `dim` and `index` are linearly independent functionals on
      the representation ring, and the trivial summand has dim 1 / index 0;
      (ii) E_1(x+c) at distinct shifts are linearly independent (distinct
      logarithmic branch points).  ONE CARRIED HYPOTHESIS THAT IS THIS
      PROGRAM'S, named: every coefficient has the form
      (rational constant) × Σ_a w_a I_n(x + C2_a).

W-07  U(1) TRANSITION FUNCTIONS + TRIPLE-OVERLAP COCYCLE ⟹ A COMPLEX LINE
      BUNDLE  (T-16 = B-4, collapsed)
      DEPENDS ON: g_ij = exp(iθ_ij) ∈ U(1) on overlaps with
      g_ij g_jk g_ki = 1 — the standard cocycle construction.  Antecedent that
      is this program's: that there IS a ray field on record cells.

W-08  THE COMPARISON CONNECTION AND ITS GLOBALLY DEFINED CURVATURE
      (T-17 = B-3, collapsed)
      DEPENDS ON: D_i = d − i a_i patches iff a_j = a_i + dθ_ij; f|U_i = d a_i
      is global because d²θ_ij = 0.  Standard U(1) connection theory.

W-09  THE HOLONOMY CHARACTER W_n(γ) = exp(i n ∮_γ a), n ∈ ℤ  (T-18, first half)
      DEPENDS ON: W-07 + W-08 + W-01.  (The clause |n| = 1 does NOT transfer —
      it is ratified, not derived.)

W-10  *** A FINITE DISCRETE SPECTRUM IS RECURRENT — THE FINITE-RECORD
      DURABILITY NO-GO ***  (N-1)
      DEPENDS ON: recurrence of unitary evolution generated by an operator with
      finite discrete spectrum.  Standard finite-dimensional spectral theory.
      CLASS IT BINDS: every construction whose durable record is carried by a
      CLOSED system with finitely many unitary degrees of freedom.  It does not
      bind constructions with an infinite limit, an exact superselection sector,
      an open-system reduction, or a record not carried by the evolving degrees.

W-11  NO NORMALIZED TRACIAL STATE ON THE FULL INFINITE SOURCE ALGEBRA  (N-5)
      DEPENDS ON: two isometries with orthogonal ranges on B(H); Tr(I) = 1 would
      give 1 = 2.  Three lines of C*-algebra.
      CLASS IT BINDS: any attempt to scalarize an operator response on an
      infinite-dimensional algebra via a normalized trace.

W-12  THE UNIQUE UNITARILY-INVARIANT FUNCTIONAL ON M_d(C) IS Tr/d  (N-6)
      DEPENDS ON: matrix-unit covariance under all unitary basis changes.
      CLASS IT BINDS: any construction demanding a basis-independent scalar
      readout of a finite matrix response.

W-13  ||[M_N, O]|| ≤ 2m||O||/N — THE CENTRAL-SEQUENCE ESTIMATE  (B-9)
      DEPENDS ON: the elementary commutator bound for a Cesàro average of local
      operators against an m-local observable.

W-14  THE CAUSAL DIRECT LIMIT AS A CONSTRUCTION SCHEMA  (B-1)
      DEPENDS ON: the inductive limit of a directed system of finite matrix
      algebras under unital embeddings A ↦ A⊗I; state compatibility
      ω^(N+1)(ι_N(A)) = ω^N(A); the GNS construction.  Standard UHF/quasi-local
      C*-theory.  IT IS THE THIRD OF N-2's FOUR MECHANISMS, AND THE ONLY ONE
      THE CORPUS BUILT.

W-15  THE UHF DIRECTED SYSTEM OF FINITE RECORD ALGEBRAS  (B-8)
      DEPENDS ON: A_N = ⊗_{j=1}^N M_k, ι_N(A) = A ⊗ I.  (Factor dimension is
      this program's and is disputed internally — F-6.)

W-16  THE FINITE CELLULAR RECORD COMPLEX  (B-2)
      DEPENDS ON: a finite cochain complex on an oriented cell structure with
      basis cochains δ_e ∈ C_N^k, and its incidence operator.  Standard cellular
      cohomology.  THE WARNING TRAVELS WITH IT: the chain-complex k-cell is NOT
      the primitive causal record cell — "'Cell' names two objects the corpus
      says are not identical."

W-17  U(1) DOES NOT ESTABLISH S¹  (A-0)
      DEPENDS ON: the distinction between a compact structure group and a
      physical spacetime fiber with a length radius.  A NEGATIVE a successor
      inherits unconditionally.

W-18  SEPARATE NONEMPTINESS DOES NOT IMPLY JOINT INHABITANCE  (from A-11)
      DEPENDS ON: the elementary fact that a fiber product of nonempty objects
      may be empty.  Stated by the corpus as "the permanent equalizer
      regression".

W-19  AN INFINITE COMMUTATOR NORM EXCLUDES THE OPERATOR-NORM ROUTE  (from S-9,
      W-3's exclusion reason)
      DEPENDS ON: ||[h_0, 1_B]|| = +∞ forcing a quadratic-form certification
      instead.  Standard unbounded-operator analysis.

W-20  THE CUSTODY DISCIPLINE  (M-1)
      DEPENDS ON: a corpus with artifacts of differing evidential strength.
      Three rules: consumption strength declared and never upgraded; authorship
      disclosed at the point of adoption; assemblies marked as the commission's
      own.

W-21  THE ADVERSARIAL BUILD-PLUS-REFUTE PAIRING, WITH PRE-REGISTERED VERDICT
      (M-2)
      DEPENDS ON: two agents, a hash, and an ordering rule — route enumeration,
      pre-verdict and attack checklist fixed under hash BEFORE the build is
      opened.  Measured coverage in this corpus: 88/94 = 93.6%.

W-22  THE SIX-WAY NEGATIVE TYPING SCHEME  (M-3)
      DEPENDS ON: nothing.  TYPE-R refuted · TYPE-U unbuilt · TYPE-S scope-empty
      · TYPE-C constraint-blocked · TYPE-P premise-conditional · NO_VERDICT
      legal.  Load-bearing clause: "Only TYPE-R is physical content."

W-23  THE RESTRICTION FALSIFIER  (M-4)
      DEPENDS ON: the general relation between a finite object and a completion
      of it.  "THE FINITE RESULTS ARE THE AUTHORITY; THE COMPLETION IS
      ANSWERABLE TO THEM, NEVER THE REVERSE."

W-24  MEMBER-SENSITIVITY TAGGING  (M-5, rule 1)
      DEPENDS ON: the existence of a family from which a member was chosen.
      Every downstream result carries a tag; "the difference stays visible at
      every stage and is never silently absorbed."

W-25  THE NO-SELECTION PRINCIPLE AND CARRIAGE-INSTEAD-OF-CHOICE  (M-6)
      DEPENDS ON: a family plus a neutrality certificate.  Work with a family
      instead of a member exactly when the wanted quantity is certified the same
      for every member; otherwise carry branches conditionally.

W-26  Θ-PARITY BOOKKEEPING  (M-7)
      DEPENDS ON: a doubled/CTP construction with a parity involution.  An odd
      factor belongs on the side whose convention already carries it.

W-27  DERIVED-OR-DECLARED, NEVER IMPLICIT, WITH A FAILURE-CAPABLE CERTIFICATE
      (M-8)
      DEPENDS ON: two sectors with different units and an arrow between them.

W-28  TWO NAMED GENERAL FAILURE MODES  (M-9)
      DEPENDS ON: nothing.  "unconstrained lift = selection"; "reader-derived
      π_Mx = the F_PLDEC circularity class."

W-29  THE TYPED-NEGATIVE PROTOCOL, TOGETHER WITH ITS MEASURED COVERAGE LIMIT
      (M-10)
      DEPENDS ON: two syntactic forms (`= false` flags; "not found") plus W-22.
      *** THE COVERAGE LIMIT IS PART OF THE ASSET: it reaches flag-form and
      "not found" negatives and DOES NOT REACH PROSE BARRIERS; the shortfall is
      6.7 : 1 (5,206 untyped to 778 typed), survives an eightfold window
      widening, is NOT a legacy backlog (July/August split 18.7/81.3 untyped vs
      20.3/79.7 typed), CONCENTRATES IN ANALYTIC BARRIERS (26.8% vs 8.6%; the
      `diverges` lexeme at 38.8 : 1), and partial coverage is RATIFIED by name
      (DoR-006, "No mass re-typing campaign").  Rule 5 — "A NEGATIVE CARRIES THE
      SAME EVIDENTIARY BURDEN AS A POSITIVE.  Reporting 'not found' requires
      stating the search." — transfers on its own. ***

W-30  THE CANNOT-FAIL-CHECK CLASS  (M-11)
      DEPENDS ON: nothing.  A check whose passing is an identity of the
      construction tests nothing and its flag reads stronger than it is.  Four
      instances of record in this corpus.

W-31  THE QUESTION-INDEXED REGISTER FORM  (M-12)
      DEPENDS ON: a monotone integer index and the rule that every decision
      cites the question it answers.  What it buys: provenance as a CHAIN OF
      KILLS (DoR-018, DoR-020 record their dead candidates in order).
      *** ITS FAILURE MODE TRAVELS WITH IT: an index pointing into a single
      non-redundant file is a single point of failure for the whole provenance
      layer — this commission could not resolve one `Q-…` token. ***

  ALSO TRANSFERS-WHOLE, counted inside M-13/M-14 rather than separately:
  the process LOSS CLASS with its append-only erratum remedy (M-13); the
  SEALED-BEFORE-AUTHORING HONEST-OUTCOME MENU (M-14).  Counting them
  separately gives 33.
```

### §11.2 TRANSFERS-AS-SPECIFICATION — 12 distinct assets

```text
P-01  *** THE NINE PROPERTIES A CELL→RECORD CROSSING MUST PRODUCE ***  (S-1)
      P-1 durability/irreversibility · P-2 persistence under later cells ·
      P-3 thresholded non-return · P-4 recoverability · P-5 redundancy [or P-4]
      · P-6 asymptotic centrality · P-7 sector-hood/superselection ·
      P-8 inductive compatibility · P-9 orthogonal reduced supports — STILL
      FALSE, produced by nothing in the corpus.
      WHY IT TRANSFERS: none of the nine names this program's surface, action,
      carrier, germ, member, or gate; each is stated in terms a successor's own
      objects will have.  THE ADVERSE HALF IS PART OF THE SPEC: "public" is
      predicated of BOTH levels and does not mark the crossing.

P-02  THE FOUR DURABILITY COMPLETION MECHANISMS  (N-2 = S-4)
      exact superselection/central sector · invariant post-write pointer algebra
      · infinite causal/environmental limit with asymptotic outgoing sectors ·
      derived open-system limit from a larger unitary theory.  Plus the
      anti-fitting rule: "These mechanisms are physically inequivalent and may
      not be selected after a response is evaluated."  ONE OF FOUR BUILT.

P-03  THE STANDING DEMAND ON ANY SUCCESSOR RECORD CONSTRUCTION  (N-3)
      "Merely increasing the finite cell count or calling orthogonality
      durability does not pass."  (Its first clause names this program's
      incidence law and is construction-bound; the quoted clause is not.)

P-04  THE DURABILITY MAP SPECIFICATION  (S-3)
      A complete action fixing four things: source-conditioned identity phase,
      post-closure pointer block, causal cell, durability map.  Plus the general
      bar: "No geometric uncertainty budget may be substituted for physical
      action without a theorem."

P-05  THE SUPPLY ROUTE FOR A MAGNITUDE JUNCTION  (T-8 = S-5)
      Jointly: an exit operation AND a booked clause in which a response
      magnitude and phase-sector data CO-OCCUR.  Two things, not one.

P-06  THE SIX SCALARIZATION ROUTES AND THEIR COSTS  (N-8 = S-6)
      source vector/covector (needs boundary data) · density-state expectation
      (needs the incoming state) · finite normalized trace (no canonical
      continuum extension) · determinant (nonlinear) · inclusive equal-branch
      sandwich (phase blind) · operator-valued response (well typed, moves the
      problem downstream).

P-07  THE DISCRETE-TO-CONTINUUM EQUIVALENCE REQUIREMENT, WITH ITS CIRCULARITY
      BAR  (A-1 = S-2)
      "the stitching rule as a theorem over refinements", and: adopting a smooth
      ambient metric at the alpha-facing chain "would adopt the gravity the
      program claims to derive."  The bar is general; any construction claiming
      to derive a term may not import a structure that already carries it.

P-08  THE IDENTIFICATION FALSIFIER  (A-19)
      "wherever both routes are formed, their periods MUST agree; a displayed
      disagreement … voids the disagreeing construction(s) … No lane may assume
      the identification."  A requirement on any redundant-route construction.

P-09  THE CERTIFIED-WITNESS REQUIREMENT FOR A JOINT EQUALIZER  (S-7)
      A witness must inhabit the JOINT equalizer over all named generators;
      separate nonemptiness is not enough (W-18 is its mathematical half).

P-10  THE RANK-PINNING PACKAGE SPECIFICATION  (S-8)
      "sealed scalar source representation + rank-preserving intertwiner" — the
      corpus's own "require-shaped would-build".

P-11  THE NAMED CONDITION AT WHICH A UNIVERSAL NO-GO OF THAT SHAPE FAILS
      (T-27 = N-9)
      A refuted universal no-go is a specification in disguise: it names exactly
      what must be supplied for the construction to be possible.

P-12  THE VERSION-BUMP DESYNCHRONIZATION DEFECT CLASS AND ITS PRESCRIPTION
      (N-10)
      "detected only at the enforcement point AFTER path consumption, with tests
      stubbed at exactly the failing seam", remedied by A1 (one sealed
      generation table + mechanical check before any lane runs) and A2 (full
      real-chain rehearsal, no stubs).  Six cycles of one defect class.
```

---

## §12 — CHOICE LEDGER

Every unforced choice this commission made, with the byte that decided it.

```text
C-1  THE THREE-PART SPLIT OF THE PARTITION THEOREM (require-half graded apart
     from allow-half and exclusivity).
     DECIDED BY: the theorem's own §5.1 premise-DAG audit and its sentence
     ":368 — 'The require-half consumes even less (one clause and algebra).'"
     ALTERNATIVE: grade the theorem as one item, CONSTRUCTION-DEPENDENT.
     REFUSED: it would hide a TRANSFERS-WHOLE asset inside a
     CONSTRUCTION-DEPENDENT wrapper, which is exactly the error the commission's
     test is designed to catch.  CLASS: FORCED-IN-SUBSTANCE.

C-2  THE GRAVITY/GAUGE IMPOSSIBILITY GRADED TRANSFERS-WHOLE WITH ONE NAMED
     CARRIED HYPOTHESIS, RATHER THAN CONSTRUCTION-DEPENDENT.
     DECIDED BY: its proof engine at :160-170 — Schur, linear independence of
     E_1 shifts, dim ⊥ index — none of which is an object this program built;
     and the commission's own anticipation ("may rest on representation theory
     rather than on this program's construction").
     ALTERNATIVE: grade it CONSTRUCTION-DEPENDENT because the coefficient form
     is this program's.  REFUSED, BUT THE HYPOTHESIS IS DISPLAYED AT W-06 SO A
     READER WHO DISAGREES CAN RE-GRADE IT WITHOUT RE-READING THE SOURCE.
     CLASS: PREMISE(named).

C-3  METHOD GRADED AS ASSETS AT ALL.
     DECIDED BY: the commission's Q5, which asks for grades on the custody
     discipline, the pairing, the register form, and the typed-negative
     protocol.  ALTERNATIVE: treat method as out of scope for a salvage audit.
     REFUSED — it was commissioned.  CLASS: FORCED.

C-4  THE 55 BARE-ONLY ARTIFACTS REPORTED AS THE COMPLIANCE GAP, RATHER THAN THE
     4,784 NORMALIZED-ONLY ONES.
     DECIDED BY: the commission's own statement of the convention — "Every
     artifact should carry `<stem>.md.seal.sha256`" — which makes the
     `.md.seal.sha256` form the required one.  BOTH counts are published at §2
     so a reader using the other reading can compute it.
     CLASS: PREMISE(named).

C-5  O38SR's DoR-020-A4 ABSENCE REPORTED AS A LOCATOR CORRECTION, NOT AS A
     REPAIR OF ITS VERDICT.
     DECIDED BY: this commission's bar on adjudication, and by the fact that
     beta_f's grade rests on three further dependencies the correction does not
     touch.  ALTERNATIVE: re-grade beta_f upward.  REFUSED as adjudication.
     CLASS: FORCED.

C-6  THE `Q-…` TOKENS TREATED AS OPAQUE LABELS.
     DECIDED BY: the register's barred status.  The same disposition is taken by
     the T16SR partition theorem in its own sweep cutoff, so the treatment is
     the corpus's own, not this commission's coinage.  CLASS: FORCED.

C-7  DUPLICATES COLLAPSED IN §11 (T-16 = B-4; T-17 = B-3; N-2 = S-4; T-8 = S-5;
     N-8 = S-6; A-1 = S-2; T-27 = N-9).
     DECIDED BY: the commission's demand that every TRANSFERS-WHOLE and
     TRANSFERS-AS-SPECIFICATION item be ITEMIZED — an itemization that
     double-counts one asset under two question numbers would overstate the
     salvage.  Per-question tallies are published uncollapsed; §11 is the
     distinct-asset count.  CLASS: PREMISE(named).

C-8  M-13 AND M-14 COUNTED INSIDE THEIR ENTRIES RATHER THAN AS SEPARATE §11
     ROWS, WITH THE ALTERNATIVE COUNT (33) PUBLISHED.
     CLASS: IMMATERIAL — displayed both ways.

C-9  THE ONSET GATE AND FLUX GATE GRADED CONSTRUCTION-DEPENDENT DESPITE
     CONTAINING RECOGNIZABLY STANDARD OBJECTS (a Fubini-Study path budget; a
     controlled unitary).
     DECIDED BY: each gate's own self-typing — the onset gate's heading "Adopted
     Gravacle onset rule" with `relative_onset_saturation_derived = false`, and
     the flux gate's "This is conditional on the inherited/adopted rules above."
     The standard objects are named inside each entry so nothing is buried.
     CLASS: FORCED-IN-SUBSTANCE.

C-10 NO GRADE ASSIGNED TO THE MEMBERSHIP THEOREM (T-21).
     DECIDED BY: it was not opened in full; INDETERMINATE-AT-BYTES is the
     honest return.  ALTERNATIVE: infer a grade from O38SR's one-line report.
     REFUSED — a report is not the primary bytes.  CLASS: FORCED.

ZERO ENTRIES IN CLASS OPEN.
```

---

## §13 — IMPORT AUDIT

Non-corpus notions used anywhere above, with the statement of whether the
finding survives without them. **An import found and reported is a full result;
none of these is barred in advance, and each is dispositioned.**

```text
I-1  "TRANSFERS-WHOLE / TRANSFERS-AS-SPECIFICATION / CONSTRUCTION-DEPENDENT /
     DEPENDS-ON-A-WITHDRAWN-OR-UNBUILT-OBJECT" — THE COMMISSION'S TERMS, NOT
     THE CORPUS'S.  Sweep: zero occurrences of any of the four in either root.
     SURVIVAL: the findings survive fully — each grade is a restatement of a
     dependence the corpus itself states in its own words (ground clauses, scope
     clauses, "Tag: YOURS", "TYPE-U", "ABSENT", "killed").  The grade names the
     dependence; it does not supply it.

I-2  "SUCCESSOR" IN THE SENSE OF A DIFFERENT PROGRAM.  The corpus uses
     "successor" in a narrower, internal sense (e.g. the T7 no-go's "The clean
     successor is: retain the primitive completed-record response as an
     operator-valued map…").  The commission's sense is wider.
     SURVIVAL: every finding is stated as a DEPENDENCE ("rests on X"), which is
     a property of the asset, not of any successor.  The findings survive with
     the word deleted.

I-3  POINCARÉ RECURRENCE / QUASI-PERIODICITY as the name for W-10's engine.
     NOT USED AS A PREMISE ANYWHERE ABOVE.  The corpus states the fact in its
     own words — "A finite discrete spectrum is recurrent" — and W-10 cites that
     sentence, not a named theorem.
     SURVIVAL: complete.  The import is a label only and is not load-bearing.

I-4  "UHF / AF C*-ALGEBRA", "QUASI-LOCAL", "GNS".  GNS and "quasi-local" are the
     corpus's own words (FORK_8:56-58, CDLRP_V002:16-17).  "UHF" and "AF" are
     this audit's labels for the construction the corpus describes in full.
     SURVIVAL: complete — W-14 and W-15 cite the corpus's displayed
     construction (directed system, unital embeddings, state compatibility),
     not the classification name.

I-5  "SCHUR'S LEMMA", "DYNKIN INDEX", "CARTAN METRIC", "REPRESENTATION RING".
     ALL FOUR ARE THE SOURCE ARTIFACT'S OWN WORDS (":21-26" names Schur;
     ":57-59" names `dynkin_index`; ":96-102" names the Cartan metric; ":167"
     names the representation ring).  NOT IMPORTS.

I-6  "MODEL THEORY / SOUNDNESS" for the partition theorem's engine.  The
     artifact names its own steps ("the AJ's displayed logical step",
     "invariance lemma") and this audit uses those names.  The phrase "standard
     model theory" appears in this audit's voice at T-2 as a characterization.
     SURVIVAL: complete — T-2's grade rests on the VOCABULARY FACT being about
     this sealed text, which is byte-checkable without any model-theoretic
     vocabulary.

I-7  "COCYCLE / COBOUNDARY" at A-14 (the J4 groupoid row).  The corpus writes
     the equations (v_gf = v_f∘ρ_g + v_g, v_id = 0, and the ψ-action) but does
     not call them a cocycle in that ruling.  It DOES use "cocycle" for the
     triple-overlap relation and for β (":271 'zero cocycle'").
     SURVIVAL: A-14's grade is CONSTRUCTION-DEPENDENT and does not rest on the
     identification; the identification is offered as a recognition note and is
     marked as such.  The finding survives without it.

I-8  "SINGLE POINT OF FAILURE" (W-31's failure mode).  This audit's phrase.
     SURVIVAL: the underlying fact is byte-observed — zero `Q-…` tokens
     resolvable when one file is unavailable — and is stated independently by
     T16SR ("EXPECTED-UNLOCATABLE").  The finding survives; only the phrase is
     imported.

I-9  "CONSTITUTIVE DEFINITION" (X-17).  O53SR's audit flags it explicitly as
     "commission's term" and records that "the count is 0 under every reading
     tested."  IMPORT, DISCLOSED BY ITS OWN SOURCE, AND ROBUST TO THE READING.

*** NO IMPORT ABOVE IS LOAD-BEARING FOR ANY GRADE.  IMPORT-BLOCKS FOUND: 0. ***
```

---

## §14 — TOY_SEPARATION

```text
TOY_SEPARATION = clean.
No toy object, model profile, candidate, or exhibit is asserted as content
anywhere in this artifact.  The two model profiles f₁ and f₂ appear only inside
quoted spans of the partition theorem and the amplitude junction, where they are
their sources' own quarantined meta-level counterexamples about a derivability
relation; they enter no grade, no tally, no flag.  Every load-bearing object is a
sealed (or explicitly unsealed and so-marked) span read at bytes.
No number in this artifact's own voice is a value of anything: every integer is a
count of files, artifacts, occurrences, or graded items, or a quoted digest.
The exact expressions appearing inside quoted spans (π ℏ/2, exp(2πin) = 1,
Tr(K)=Tr(V₁V₁†)+Tr(V₂V₂†), C(N−2,k−1), 1/23040, 3/2, 2e-14, 2.158029616704532,
R_square = 3/16, ||[h_0,1_B]|| = +∞) are reproduced whole because quotation
integrity requires their adverse clauses; NONE was evaluated, compared, or
approached, and none is asserted here.
```

---

## §15 — RESULT BLOCK

```text
SCOPE     four permitted roots · 23,863 files · 6 exclusion globs as an ARRAY ·
          23 per-pattern hits · *** TOTAL LEAK = 0 *** · self-excluded.
SEALS     24/25 cited artifacts verified · 0 MISMATCHES · 1 unsealable (the
          durability no-go), cross-root byte-identity substituted and flagged.
SIDECARS  6,930 allowed .md artifacts probed in BOTH forms: 299 both · 4,784
          normalized-only · 55 BARE-ONLY (named) · 1,792 unsealed.

PER-CATEGORY TALLIES BY GRADE
                                   TW    TAS   CD    DWU   IND   entries
  Q1  theorems / proved results      9     2    13     2     1     27 †
  Q2  no-gos / constraints           4‡    5     3     0     0     12 ‡
  Q3  adopted objects (28 rulings)   1     2    13     4     1     21 (+9 proc)
  Q4  built objects / specs          6     7     2     3     0     18
  Q5  method                        13     0     1     0     0     14 §
                                   ---   ---   ---   ---   ---
  RAW TOTALS                        33    16    32     9     2     92
  † T-18 split by the bytes, counted on both sides; T-20 graded at Q4.
  ‡ Q2's TW count includes T-14 restated from Q1 (one asset, two questions);
    Q2's native TW items are N-1, N-5, N-6.  N-3 is split and counted once.
  § M-5 split (rule 1 transfers, rule 2 does not).
  §11 IS THE AUTHORITATIVE DISTINCT-ASSET COUNT; the raw totals above
  double-count assets that answer more than one question.

DISTINCT-ASSET COUNT (duplicates across questions collapsed, §11):
  TRANSFERS-WHOLE ................ 31   (33 if M-13/M-14 are counted separately)
  TRANSFERS-AS-SPECIFICATION ..... 12

Q6 — WHAT DOES NOT TRANSFER: 20 named items (X-1..X-20), summarized at §9.5.

THE AUDIT'S OWN SHAPE, IN ONE LINE:
  the corpus's THEOREMS are mostly about its own ground; its NO-GOS and its
  METHOD are mostly not.  The four assets that bind any construction of their
  class — a finite discrete spectrum is recurrent; no normalized trace on an
  infinite algebra; the unique unitarily-invariant finite functional; and no
  x-independent gravity/gauge ratio where dim and index are independent
  functionals — rest on spectral theory, C*-algebra, matrix covariance, and
  representation theory respectively, and on nothing this program built.

FENCES HELD   alpha_computed = false · proof_authorized = false ·
              kappa_record_computed = false
BARS HELD     no authoring · no advocacy · no adoption · no recommendation of a
              successor design · no ruling on what should be kept · nothing
              computed · no magnitude approached · NO BARRED FILE OPENED.
              ONE BAR INCIDENT SELF-REPORTED AT F-12: a single ad-hoc line-grep
              displayed one line from a barred register.  That line is cited
              nowhere, carries no premise, and the finding it touched stands
              whole on two independent unbarred sources.
OUTPUT        ONE file at the commissioned path, probed ABSENT before first
              write · sealed to BOTH sidecar forms and verified · no git.
```

---

*END OF ARTIFACT — STAGE8_SALVAGE_AUDIT_O56SR_V001*







