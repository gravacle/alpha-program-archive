# SHAPES-AUDIT OF STAGE8_BOUNDARY_SHAPES_O32SR_V001 — RE-DERIVED AT BYTES

COMMISSION O32SR — SHAPES-AUDIT — 2026-08-15
DEFAULT-REFUTE. TESTIMONY ZERO WEIGHT. Every count, every seal and every
quotation below was re-run by this audit against the files themselves. No claim
of the audited artifact is carried forward on its own authority.
DETERMINATION ONLY. Nothing is constructed, proposed, adopted or supplied.

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

OUTPUT-PATH PROBE, BEFORE ANY WRITE:
`/Users/bgm/MB Work/alpha-program-archive/workspace/STAGE8_BOUNDARY_SHAPES_O32SR_AUDIT_V001.md`
— ABSENT (`ls` exit 1); sidecar `...AUDIT_V001.md.seal.sha256` — ABSENT (`ls` exit 1).
Probed at commission start and again immediately before the first byte was written.

---

## §0 — IMPORT AUDIT, STATED FIRST

```text
*** THE THREE SHAPES — FORCED CONVERGENCE, REACHABILITY EDGE, MATCHING WITH
    RESIDUE — WERE SUPPLIED BY THE COMMISSION FROM OUTSIDE THIS CORPUS. THEY ARE
    NOT THE RECORD'S VOCABULARY, THEY ARE NOT DERIVED FROM IT, AND THEY CARRY NO
    AUTHORITY IN IT. NOTHING IN THE RECORD IS OBLIGED TO INSTANTIATE ANY OF
    THEM, AND NO ABSENCE OF ONE IS A DEFECT OF THE RECORD. ***
```

They are used here exactly as the audited artifact uses them: as three test
templates. This audit's own question is narrower — **did the audited artifact
locate the record's structures correctly, and did it grade vocabulary against
structure honestly?**

FOR EVERY MATCH THIS AUDIT REPORTS, §7 RECORDS WHETHER THE RECORD'S OWN TEXT
**CARRIES THE STRUCTURE** OR ONLY **RESEMBLES THE DESCRIPTION**. A resemblance of
vocabulary is not an instantiation.

The words "spread", "reachability edge", "residue-as-object",
"surface-supported", "defect term" as a shape name, and the three shape names,
are the COMMISSION'S and this audit's. Where they appear in this audit's own
prose they label a TEST. Every corpus object is named in the corpus's own words,
quoted at bytes from a seal-verified file.

---

## §1 — STEP 0: TARGET PROBE AND SEAL

```text
TARGET   /Users/bgm/MB Work/alpha-program-archive/workspace/
         STAGE8_BOUNDARY_SHAPES_O32SR_V001.md        PRESENT, 74525 bytes, 1416 lines
SIDECAR  ...V001.md.seal.sha256                       PRESENT, 103 bytes

shasum -a 256 -c STAGE8_BOUNDARY_SHAPES_O32SR_V001.md.seal.sha256
  RUN FROM: /Users/bgm/MB Work/alpha-program-archive/workspace   (the artifact's
            own directory)
  RESULT:   STAGE8_BOUNDARY_SHAPES_O32SR_V001.md: OK        exit 0
  DIGEST:   4caf153f0e35f5ebbcf6aa36d6650c1e12cdad3de9f657757026cd4537eacd41

STEP 0 PASSED. Audit proceeds.
```

---

## §2 — THIS AUDIT'S DECLARED SWEEPS AND CUTOFF

```text
SWEEP CUTOFF, DECLARED: 2026-08-15, tree state at this audit's run — LATER than
  the audited artifact's own cutoff. Two *.md objects exist in ROOT1 that did not
  exist when the audited artifact ran, plus the audited artifact itself:
    STAGE8_BOUNDARY_SHAPES_O32SR_V001.md          (Aug 15 18:28)  = the target
    STAGE8_SIGN_AUDIT_O33SR_V001.md               (Aug 15 18:30)
    STAGE8_GAUGE_AS_CONTENT_O34SR_V001.md         (Aug 15 18:30)
  NO FINDING BELOW IS CHARGED AGAINST THE AUDITED ARTIFACT ON THE STRENGTH OF A
  FILE THAT POSTDATES IT. Where a post-cutoff file is mentioned it is marked
  OUT-OF-CUTOFF and is never used as a ground for a defect.

  ROOT1 (primary)  /Users/bgm/MB Work/alpha-program-archive/workspace
                   6873 files, 1927 *.md (recursive), at THIS audit's instant.
  ROOT2            /Users/bgm/Documents/New project/gravity_emergence_evidence_
                   program/alpha_fundamental_record_action_cleanroom_v003
                   7805 files, 2308 *.md (recursive).

FILE-CLASS EXCLUSION, APPLIED AT THE PATH FILTER, BEFORE ANY READ.
  Any file whose BASENAME matches (REGISTER|TRACKER|ROAD|PLAN|CONTINUATION),
  case-insensitive, was removed from every match set and never opened.
  Post-filter sets actually swept: ROOT1 1889 *.md ; ROOT2 2264 *.md.

"Q-..." tokens: EXPECTED-UNLOCATABLE. Encountered inside quoted sealed text
  (Q-408, Q-279, Q-247, Q-54). Carried as opaque labels exactly as the sealed
  artifacts carry them. Never chased, never resolved, nothing defaulted.

NO GIT ACTION OF ANY KIND. No existing file edited. Two files written: this
  audit and its seal sidecar.
```

### §2.1 EVERY PATTERN THIS AUDIT RAN, VERBATIM

Run as `grep -lIE` / `grep -nIiE` over the path-filtered lists, `-i` throughout.
Counts are FILE counts, full match-set sizes, no truncation.

```text
REPLICATION OF THE AUDITED ARTIFACT'S DECLARED PATTERNS
 R-S2a  \breachab | \breach\b | \binfluence\b | \bhorizon\b | causal ball |
        causal diamond | causal support | causal cell | causal schedule |
        causal feeding|feeding arrow | can (be )?reach|cannot reach|reaches |
        domain of dependence | domain of influence | causal (past|future) |
        light[- ]?cone|lightcone
 R-S2b  where reach stops|edge of reach|limit of reach
 R-S3b  supported on the (surface|boundary|interface|junction|overlap)
 R-S3c  fails? to match|match(ing)? fails
 R-S3d  residue[^.]{0,70}(overlap|junction|interface|mismatch|glu|joint|seam) |
        (overlap|junction|interface|mismatch|glu|joint|seam)[^.]{0,70}residue
 R-S3e  defect (term|object|class|measure|form|field|density)
 R-S1c  \bmonotone (decreas|non-?increas)|monotonically decreas|
        strictly decreas|decreasing in (n|N|k)\b
 R-S3a-frag  matched carrier | identity cell matching | OVERLAPPING, not IDENTICAL

THIS AUDIT'S OWN PATTERNS — SHAPE THREE PART (b), RUN UNCAPPED (commission item C)
 A1  \bdiscrepanc
 A2  discrepancy cocycle
 A3  \bcocycle\b
 A4  \bcoboundary\b
 A5  \bcech\b|Cech
 A6  \bcocycle\b.{0,60}(discrepanc|defect|residue|mismatch)
 A7  (discrepanc|defect|residue|mismatch).{0,60}\bcocycle\b
 A8  triple[- ]overlap cocycle
 A9  transition function
 A10 line bundle
 A11 gerbe|torsor|transition function
 A12 obstruction class|cohomology class
 A13 chern class|first chern|c_1 of
 A14 \bholonom
 A15 \bwinding number|\bwinding\b
 A16 \bmonodrom
 A17 gluing (map|cocycle|datum|data)
 A18 supp\(beta | support of the (defect|residue|discrepanc)
 A19 zero-defect
 A20 correction term|correction to the|corrective term
 A21 \bexcess\b
 A22 \bjump\b
 A23 surface term | boundary term | corner term | edge term
 A24 supported (on|at|by) the
 A25 surface[- ]supported|boundary[- ]supported|interface[- ]supported
 A26 lives on the (surface|boundary|interface|junction|overlap|seam|face)
 A27 concentrat\w+ on the (surface|boundary|interface|junction|overlap|seam|face)
 A28 missing overlap equality
 A29 silent on multiplicity ; domain restriction ; multiplicit
 A30 beta_f | β_f

THIS AUDIT'S OWN PATTERNS — SHAPE ONE (independent re-hunt)
 B1  (spread|dispersion|diameter|variance)[^.]{0,60}
     (decreas|shrink|contract|tends to zero)
 B2  lieb-robinson
 B3  shrink\w*[^.]{0,50}(family|sequence|famil)
```

---

## §3 — SEAL CLAIMS, RE-VERIFIED INDEPENDENTLY. **30/30 OK.**

The audited artifact claims at §6 "28/28 OK. No mismatch. Nothing consumed
unverified." **THE CLAIM IS TRUE.** Every one of the 28 was re-run by this audit
with `shasum -a 256 -c <sidecar>` FROM THE ARTIFACT'S OWN DIRECTORY. This audit
additionally seal-verified 2 further artifacts it consumed itself. All 30 OK,
zero mismatch.

```text
OK  STAGE8_INGREDIENT_CENSUS_O17SR_V001.md          OK  STAGE8_RECORDS_PLURAL_O30SR_V001.md
OK  STAGE8_INGREDIENT_CENSUS_O17SR_AUDIT_V001.md    OK  STAGE8_RECORDS_PLURAL_O30SR_AUDIT_V001.md
OK  STAGE8_GLUING_CANDIDATE_O23SR_V001.md           OK  CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md
OK  STAGE8_GLUING_CANDIDATE_O23SR_AUDIT_V001.md     OK  COMPLETE_QSPEC_OPEN_RECORD_BLOCK_TRANSFER_MAP_SPEC_V001.md
OK  STAGE8_STRATIFICATION_O27SR_V001.md             OK  STAGE8_TASK4A_NETWORK_SOURCING_LAW_ADOPTION_PROPOSAL_CODEX_LANE2_V001.md
OK  STAGE8_STRATIFICATION_O27SR_AUDIT_V001.md       OK  STAGE8_CONTRACTIBILITY_SCOPE_O26SR_V001.md
OK  STAGE8_7A_JUNCTION_U1_SHARED_CORE_DARIO_V001.md OK  STAGE8_TASK6_JII_BETA_IDENTIFICATION_DARIO_V001.md
OK  STAGE8_GALERKIN_COMMUTATOR_T12SR_V001.md        OK  STAGE8_R2_KAPPA_N_DETERMINATION_S9AD_V001.md
OK  STAGE8_WALL_BOUNDARY_CLOSURE_S9AD_V001.md       OK  STAGE8_REQUIRE_G3_CHECK_V001.md
OK  STAGE8_REQUIRE_G1_COLD_V001.md                  OK  STAGE8_G1_KERNEL_CERTIFICATE_V001.md
OK  STAGE8_OVERLAP_LAW_T11SR_V001.md                OK  STAGE8_OVERLAP_LAW_T11SR_AUDIT_V001.md
OK  STAGE8_JOIN_ADMISSIBILITY_O28SR_V001.md         OK  STAGE8_REFINEMENT_AFTER_JOIN_O29SR_V001.md
OK  STAGE8_7A_HANDOFF_PACKAGE_V001.md               OK  STAGE8_REQUIRE_CLUSTER_CHECK_V001.md
OK  STAGE8_REQUIRE_BUILD_CLUSTER_SUMMABILITY_V001.md OK STAGE8_COMPLETION_MAP_T17SR_V001.md
CONSUMED BY THIS AUDIT, ADDITIONALLY VERIFIED:
OK  STAGE8_TASK6_B_V007_REPIN_DARIO_V001.md         OK  STAGE8_GLUED_TOPOLOGY_HUNT_V001.md
OK  STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V001.md
OK  STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V003.md
OK  STAGE8_TASK5_EQ6_DIAMONDS_REVIEW_LANE1_V001.md
OK  STAGE8_TASK5_EQ6_ZERO_DEFECT_SECTION_BUILD_LANE2_V001.md
OK  STAGE8_TASK5_EQ6_AXIOM_V002_AND_EXHIBITION_LANE2_V001.md
OK  STAGE8_TASK5_EQ6_SECTION_DEEPER_CONSTRUCTION_LANE1_V001.md
OK  STAGE8_TASK5_EQ6_DETERMINATION_MAP_LANE1_V001.md
OK  STAGE8_TASK5_EQ6_MEMBERSHIP_THEOREM_LANE3_V001.md
OK  STAGE8_TASK5_EQ6_FLIP_SECTION_CHECK_AND_SCOPED_WITNESS_LANE2_V001.md
OK  STAGE8_POST_GATE_FORCING_AND_SELECTION_BOUNDARY_CENSUS_V001.md

UNSEALED, AND SO NOT USED AS GROUND BY EITHER ARTIFACT:
--  LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md   *** NO SIDECAR IN EITHER ROOT ***
    This audit confirms the audited artifact's ground-source O23SR F-2 on the
    point. This audit does NOT quote it as ground either.
```

**SEAL DISCIPLINE: CONFIRMED, WITHOUT QUALIFICATION.**

---

## §4 — CENSUS CLAIMS, RE-RUN. **THE COUNTS REPRODUCE.**

Every delta below is exactly this-artifact-plus-the-two-post-cutoff-files, i.e.
a self-hit, not an error. Run with the audited artifact's own anchors.

```text
PATTERN                 CLAIMED R1/R2   RE-RUN R1/R2   DELTA      DISPOSITION
\breachab                  157 / 132      157 / 132     0 / 0      EXACT
\binfluence\b               98 /  95       98 /  95     0 / 0      EXACT
\breach\b                  298 / 232      300 / 232    +2 / 0      self-hits
\bhorizon\b                 10 /   7       12 /   7    +2 / 0      self-hits
causal ball                 10 /   5       11 /   5    +1 / 0      self-hit
causal diamond              76 /  64       77 /  64    +1 / 0      self-hit
causal support              61 /  66       62 /  66    +1 / 0      self-hit
causal cell                 80 /  81       82 /  81    +2 / 0      self-hits
causal schedule              4 /   3        5 /   3    +1 / 0      self-hit
causal feeding|feeding arrow 3 /   1        4 /   1    +1 / 0      self-hit
can reach|cannot reach|reaches 366/315    368 / 315    +2 / 0      self-hits
ROOT2 tree size          7805 / 2308 md  7805 / 2308   0 / 0      EXACT
```

### §4.1 THE EXACT ABSENCES — INDEPENDENTLY CONFIRMED

```text
"domain of dependence"    RE-RUN: 1 ROOT1 file, 0 ROOT2.  THE ONE ROOT1 FILE IS
"domain of influence"     THE AUDITED ARTIFACT ITSELF (its §2.1 pattern block and
                          §4.1 census row).  CORPUS COUNT: *** ZERO IN BOTH
                          ROOTS. ***  CLAIM CONFIRMED.
"where reach stops|edge of reach|limit of reach"
                          RE-RUN: 1 ROOT1 file, 0 ROOT2 — again the audited
                          artifact's own §0.  CORPUS: ZERO BOTH ROOTS.
                          CLAIM CONFIRMED, and the artifact disclosed the
                          self-hit itself at F-2 before this audit reached it.
"supported on the (surface|boundary|interface|junction|overlap)"
                          RE-RUN: 1 ROOT1 file, 0 ROOT2 — the audited artifact's
                          own §2.1/§5.4.  CORPUS: ZERO BOTH ROOTS.
                          CLAIM CONFIRMED.
```

**The audited artifact's three headline absences are real at bytes.** The
self-hit disclosure at F-2 is honest and was made before any auditor forced it.
Recorded to the artifact's credit.

### §4.2 THE ARTIFACT'S OWN DISCLOSED PATTERN DEFECT — CONFIRMED HONEST

§3.1 withdraws S1a because unanchored `variance` matches **covariance** and
**invariance**. This audit re-ran the anchored replacement and confirms the
mechanism is real and the withdrawal correct. **Disclosing a self-inflicted
count contamination rather than silently repairing it is the behaviour this
commission wants and it is recorded as such.**

---

## §5 — SHAPE ONE AND SHAPE TWO: **BOTH VERDICTS CONFIRMED**

This audit hunted independently for a missed instantiation of each (commission
item B), with its own patterns, not the artifact's.

### §5.1 SHAPE ONE — FORCED CONVERGENCE — **ABSENT. CONFIRMED.**

```text
B1  (spread|dispersion|diameter|variance)[^.]{0,60}(decreas|shrink|contract|
    tends to zero)                                       4 ROOT1, 1 ROOT2.
    EVERY ONE INSPECTED AT BYTES.  Not one is a spread of a family decreasing:
      - "the covariance contraction route is dead n-uniformly; the covariance
         contraction does not rescue" — a route reported DEAD.
      - "no joint contraction" — inside a PASS row listing what is absent.
      - the fourth is the AUDITED ARTIFACT's own flag line
        "positivity_forcing_a_spread_to_decrease_located = false".
B2  lieb-robinson    3 ROOT1, 0 ROOT2 — a propagation-speed bound, not a family
                     spread; the artifact already types the "operator-norm
                     spread ... controlled by a Lieb-Robinson" hit at §3.2.
B3  shrink\w*[^.]{0,50}(family|sequence|famil)   2 ROOT1, 1 ROOT2 — nothing
                     forced by a sign condition.
R-S1c  9 ROOT1, 1 ROOT2 — declared by the artifact and never reported (see
       DEFECT D-2), but re-run here: no monotone-decrease of any spread.

FINDING: THIS AUDIT LOCATED NO QUANTITY IN EITHER ROOT MEASURING THE SPREAD OF A
FAMILY, AND NO CONDITION FORCING SUCH A QUANTITY TO FALL. The artifact's ABSENT
verdict is re-derived independently and stands.
```

### §5.2 SHAPE TWO — REACHABILITY EDGE — **ABSENT. CONFIRMED.**

The vocabulary census reproduces exactly (§4). This audit re-opened the three
carriers and confirms each typing at bytes:

```text
CARRIER 1  CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md, quoted by the artifact at
           §4.2.  RE-READ WHOLE AT :17-24.  The clause is reproduced by the
           artifact EXACTLY, including the code-fenced "support(L_c) is contained
           in Omega_c."  The cell IS assigned by the parent and the support IS
           constrained into it — the relation runs cell -> support, the reverse
           of the shape.  TYPING CONFIRMED.
CARRIER 2  r(t) = min(t, 1-t) with "sharp consumption is MANDATED (D6', AR-2)".
           A materially given sphere with a formula attached.  CONFIRMED.
CARRIER 3  "causal feeding arrow, not E_post endpoint charge".  A direction
           disambiguation.  CONFIRMED, and this audit independently re-read
           O26SR :1142-1144, which states of the same joiner that it "never
           touches the cells."  CONFIRMED AT SOURCE.
last(r)    COMPLETE_QSPEC ... :40-48 RE-READ WHOLE.  The artifact's quotation is
           EXACT and complete to the section break, and the disqualifier is
           sound: last(r) governs the validity of CLOSE.  The co-located
           "event boundary `e`" is an index.  CONFIRMED.

FINDING: NO BOUNDARY DEFINED AS THE LIMIT OF A REACHABILITY RELATION WAS LOCATED
BY THIS AUDIT IN EITHER ROOT. The artifact's ABSENT verdict stands, and its
prominent reporting of last(r) as the strongest near-miss BEFORE disqualifying it
(CL-3) is the correct handling.
```

---

## §6 — SHAPE THREE: **THE DETERMINATION IS REFUTED AT BYTES**

The artifact's headline for Shape Three — PARTIALLY INSTANTIATED, part (a)
PRESENT — is not contradicted. **What is refuted is its part (b) determination,
which is the commission's stated priority deliverable, and the grounds it gives
for that determination.**

### §6.1 THE DISQUALIFIER THE ARTIFACT RESTS PART (b) ON

`STAGE8_BOUNDARY_SHAPES_O32SR_V001.md` §5.2 B-3, §5.6 and §11, verbatim and
whole, the sentence that carries the whole of part (b):

```text
"THE RECORD CARRIES  TWO LISTS OF UNSUPPLIED OBLIGATIONS.  Each "residue" is
                     the set-theoretic complement of one side's demands in the
                     other's: what A owes that B does not discharge, and
                     conversely.  It has no support, no locus, no carrier, and
                     no place in any expression.  It is a bookkeeping remainder
                     of two requirement sets, not a quantity on a surface."
```

and the verdict it feeds, §5.6, verbatim:

```text
"the record assigns the mismatch a CONTENT — two enumerated lists
  of what each side does not supply the other — and assigns it NO OBJECT: no
  support, no locus, no carrier, no term in any expression"
```

That sentence is TRUE of the J-II residues. **It is FALSE of the corpus**, and
the corpus was not swept for the thing that falsifies it.

### §6.2 *** DEFECT D-1 — A RESIDUE-OBJECT WITH A SUPPORT, A COMPOSITION LAW, AND A PLACE IN AN EXPRESSION, NOT LOCATED BY THE ARTIFACT ***

**SEVERITY: MATERIAL. This is the missed instantiation the commission asked for
under item (B) and item (C).**

The record names, defines and uses an object it calls a **DISCREPANCY COCYCLE**.
`STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V001.md` (seal verified OK
by this audit, from the artifact's own directory), :242-254, quoted WHOLE and to
the end of its span:

```text
Define the response/contact transport `rho_f^C2` by the same test/current
pullback, including the endpoint and bundle data supplied by DoR-020-A1.
Its discrepancy cocycle is

beta_f := rho_f^C2(C2_m^fin) - C2_n^fin = 0       (C1-7)

on the old image. For a cycle-creating arrow, `(C1-7)` says the old response
restricts exactly; it says nothing false about the target-only new-cycle
component. The latter remains visible in `C2_m^fin`. The local orthogonal
excision certificate ensures contact and disjoint support pieces do not leak
into the old response coordinate.
```

**THE STRUCTURE DISPLAYED DOING THE WORK THE SHAPE DESCRIBES.**
`STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V003.md` (seal verified OK),
:386-396, quoted WHOLE:

```text
More explicitly, with `q_N` the quotient map and with all expressions on their
declared scopes, the induced data satisfy

Eta_g Eta_f q_N = Eta_gf q_N,
beta_gf          = beta_g + Eta_g(beta_f),
Res_f Eta_f       = id on each licensed old-image scope,
Theta_M Eta_f    = Eta_f Theta_N,
Ward_M Eta_f     = Ward_N,
supp(Eta_f x)    subset f(supp x) union supp(beta_f).          (J13-1)
```

and, from the same artifact's structure table at :380 and :375, verbatim:

```text
| support | support is the union of the represented and contact supports modulo
  their actual overlap |
| cocycle/composition | equation (J12-4) on both injections |
```

**TYPED AGAINST THE ARTIFACT'S OWN FOUR DISQUALIFIERS, CLAUSE BY CLAUSE:**

```text
ARTIFACT SAYS            THE RECORD'S OWN BYTES SAY
"no support"             *** supp(beta_f) — the record writes the support of the
                         defect explicitly, and uses it. ***
"no locus"               "support is the union of the represented and contact
                         supports MODULO THEIR ACTUAL OVERLAP" — a locus, and it
                         is an overlap.
"no carrier"             beta_f is valued in the C2 finite response data; it is
                         a difference of two objects of that carrier.
"no place in any         *** (J13-1): supp(Eta_f x) subset f(supp x) union
 expression"             supp(beta_f).  It is a term in a sealed inclusion. ***
                         And beta_gf = beta_g + Eta_g(beta_f) is a composition
                         law FOR THE DEFECT ITSELF.
"a bookkeeping           A difference of a transported object and its target,
 remainder of two        with a cocycle composition law.  Not a set-theoretic
 requirement sets"       complement of two requirement lists.
```

**GRADE (§7): PARTLY CARRIES.** Honestly stated, and this audit refuses to
overclaim it: `beta_f` lives in the REFINEMENT / TRANSPORT direction (does the
old response restrict exactly under `rho_f`), not in the two-regions-joined-
across-a-shared-face direction; and (C1-7) asserts it `= 0` on the old image.
Those are real distances from Shape Three, and a fair reading may still decline
to call Shape Three INSTANTIATED on it.

**BUT THAT IS NOT WHAT THE ARTIFACT DID.** It never located `beta_f`, never
displayed it, never graded it, and wrote a disqualifier — "no support ... no
term in any expression" — that the record contradicts in a sealed line. A
determination of the commission's priority question cannot stand on a
characterisation of the corpus that the corpus falsifies.

### §6.3 THE SAME OBJECT UNDER THE COMMISSION'S OWN WORD "BOUNDARY"

The record does not only carry the discrepancy cocycle; it carries a named
**BOUNDARY** version of it, and adjudicates its absence.
`STAGE8_TASK5_PACKAGE_ADJUDICATION_AND_WITNESS_LANE1_V001.md` (seal verified OK
by this audit, from the artifact's own directory), :16-17 and :137, quoted WHOLE
and to the end of each sentence:

```text
"(3) P7 does not state the J13 boundary-discrepancy cocycle needed for
     refinement-path independence."

"| J9, J12-J13, J15 | naturality and subextensivity are stated, but no boundary
  discrepancy cocycle under refinement composition is required |"
```

The record therefore names the boundary-supported discrepancy object, states
what it would be FOR — "refinement-path independence" — and records that one
package does not state it and one requirement set does not require it. That is a
determinate status for a residue-object, held in the record's own words.

This is the record, in its own vocabulary, discussing a **boundary-supported
discrepancy object under composition** — and recording where it is and is not
required. The audited artifact's §5.4 displays "supported on the
(surface|boundary|interface|junction|overlap) — ZERO IN BOTH ROOTS" as its exact
absence for part (b). The zero is real (§4.1). **But it is a zero for one
phrasing, and the corpus expresses the same idea in a phrasing the artifact
never swept for.** That is precisely the failure mode the commission named under
item (B): "a structure that carries a shape under vocabulary that does not
resemble it."

### §6.4 *** DEFECT D-2 — THREE DECLARED PATTERNS WERE NEVER REPORTED, AND ONE OF THEM IS THE PATTERN THAT FINDS D-1 ***

**SEVERITY: MATERIAL. This is the mechanism of the miss, and it is visible in
the audited artifact's own bytes.**

The artifact declares twelve patterns at §2.1 under the heading "EVERY PATTERN,
VERBATIM". Counting every occurrence of each pattern label in the whole 1416-line
artifact:

```text
LABEL   OCCURRENCES IN THE ARTIFACT   RESULT REPORTED ANYWHERE?
S1a     13                            YES (withdrawn, §3.1 — honestly)
S1a'     -                            YES (§3.2 census)
S1b      2                            YES ("45 ROOT1 files", §3.3)
S1c      1   *** DECLARATION ONLY *** *** NO. NEVER REPORTED. ***
S1d      2                            YES ("565 ROOT1 / 549 ROOT2", §3.4)
S1e      2                            YES ("ten ROOT1 files", §3.5)
S2a      4                            YES (§4.1 census)
S2b      4                            YES (§4.1, §4.7)
S3a      1   *** DECLARATION ONLY *** *** NO. NEVER REPORTED. ***
S3b      2                            YES (zero/zero, §5.4)
S3c      3                            YES (2 files, §5.4)
S3d      1   *** DECLARATION ONLY *** *** NO. NEVER REPORTED. ***
S3e      2                            YES (§5.4)
```

**S3a AND S3d ARE THE TWO BROADEST SHAPE-THREE PATTERNS, AND BOTH ARE THE
COMMISSION'S PART-(b) PATTERNS.** S3a as the artifact itself wrote it:

```text
 S3a  \bresidue | \bresidual | \bdefect | \bmismatch | \bdiscrepanc |
      \bobstruction | \bjump\b | \bdiscontinuit | surface term |
      boundary term | corner term | edge term | anomal | \bsurplus |
      \bremainder | \bexcess\b
```

`\bdiscrepanc` is a declared branch of S3a. **Running the artifact's own S3a
branch would have returned the discrepancy cocycle of D-1.** This audit ran it:

```text
\bdiscrepanc            131 ROOT1, 116 ROOT2
"discrepancy cocycle"     5 ROOT1,   4 ROOT2
S3d (as declared)        16 ROOT1  — 15 of them corpus files, one self-hit

THE 5 ROOT1 "discrepancy cocycle" FILES:
  STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V001.md:244
  STAGE8_TASK5_HOSTILE_WITNESS_CROSS_CHECK_LANE1_V001.md:189
  STAGE8_TASK5_PACKAGE_ADJUDICATION_AND_WITNESS_LANE1_V001.md:16,:137
  STAGE8_TASK5_HUNT_CROSS_CHECK_AND_FRONTIER_LANE2_V001.md:208
  STAGE8_GAUGE_AS_CONTENT_O34SR_V001.md   [OUT-OF-CUTOFF — NOT CHARGED]
```

A pattern declared under a heading reading "EVERY PATTERN, VERBATIM" and then not
run to report is worse than a pattern never declared: the declaration certifies
a search that the artifact does not display. **The artifact's part-(b) absence
therefore rests on S3b and S3c — two narrow phrase patterns — while the two broad
patterns it announced went unreported.**

### §6.5 *** DEFECT D-3 — A FALSE EXACTNESS CLAIM ABOUT S3e ***

**SEVERITY: MATERIAL.** §5.4, verbatim and whole:

```text
SWEEP S3e, "defect (term|object|class|measure|form|field|density)":
  Every hit is one of exactly two things, checked line by line:
   (i)  GC-2's "defect formula" — A_n = tr B~^2 - sum_j ||D_j||_2^2 — an
        operator-trace identity at fixed n (§3.4 ROLE 1).  Not at a surface,
        not from a mismatch, and by its own words deciding NOTHING.
   (ii) "defect class" in the PROCESS sense — a class of DOCUMENT defects the
        program's audits hunt ("the sweep's own listed defect class", "Every
        hunted defect class came back ...").  Paperwork, not physics.
```

**"EVERY HIT IS ONE OF EXACTLY TWO THINGS" IS FALSE AT BYTES.** This audit
enumerated every distinct S3e phrase in ROOT1:

```text
PHRASE            OCCURRENCES   ACCOUNTED FOR BY §5.4?
defect class            30      YES — (ii)
defect classes           4      YES — (ii)
defect formula          21      YES — (i)
defect term             11      *** NO. A THIRD THING. ***
defect terms             7      *** NO. A THIRD THING. ***
```

Excluding the audited artifact's own five self-hits, the third class is a live
corpus family, and it is Shape Three's own deliverable noun:

```text
STAGE8_TASK5_EQ6_DIAMONDS_REVIEW_LANE1_V001.md:17 (seal verified OK), verbatim:
  "the contact defect term `β_f := rho_f^C2(C2_m^fin)-C2_n^fin` vanishes on
   old-image (`β_f=0`)"

STAGE8_TASK5_EQ6_FLIP_SECTION_CHECK_AND_SCOPED_WITNESS_LANE2_V001.md:299
(seal verified OK), verbatim:
  "zero-defect terms form a nonempty common-refinement equalizer:"

STAGE8_TASK5_EQ6_CERT_CHECK_AND_ZERO_DEFECT_SECTION_LANE1_V001.md:41, verbatim:
  "conditionally when their actual legs carry coherent zero-defect terms."
```

Neither GC-2 nor paperwork. The artifact's final Shape Three sentence is **"A
LIST OF UNMET OBLIGATIONS IS NOT A DEFECT TERM"** — written while the corpus
carries eighteen occurrences of the literal phrase *defect term*, attached to a
named object with a support, and the artifact's own S3e sweep is reported as
having found none of them.

### §6.6 *** DEFECT D-4 — A THIRD MATCHING CONDITION, ON OVERLAPS, INSIDE THE ARTIFACT'S OWN COMMISSIONED GROUND ***

**SEVERITY: MATERIAL.** §5.1 reports part (a) as "PRESENT, TWO OF THEM" — NET
row `N` and R9. There is a third, and it is not in some remote corner of the
corpus: **it is in two of the eight artifacts the audited artifact seal-verified
and listed at its own §1.**

`STAGE8_INGREDIENT_CENSUS_O17SR_V001.md` (the artifact's ground #1; seal verified
OK by this audit) :283-287, quoted WHOLE:

```text
C-4  THE TRIPLE-OVERLAP COCYCLE CONDITION.
     TAKES   a triple of transition functions g_ij, g_jk, g_ki.
     YIELDS  true/false: g_ij g_jk g_ki = 1.
     TYPE    CONSTRAINT.
     BYTES   LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md :16-43.
```

`STAGE8_GLUING_CANDIDATE_O23SR_V001.md` (the artifact's ground #3; seal verified
OK by this audit) :555-565, quoted WHOLE:

```text
B-6  THE LOCAL PROJECTIVE LIFT AND ITS TRANSITIONS.   *** THE FIND ***
     TAKES   a patch U_i.
     YIELDS  a normalized lift z_i : U_i -> C^2; transition functions
             z_j = g_ij z_i with g_ij = exp(i theta_ij) in U(1); and the
             triple-overlap cocycle g_ij g_jk g_ki = 1.
     JOINER? THIS IS THE ONE ROW OF GLUING-SHAPED SIGNATURE THAT NEITHER THE
             CENSUS NOR THE AUDIT SURFACED. Transition functions on overlaps
             obeying a triple-overlap cocycle ARE gluing data in the exact
             technical sense — the source itself says they "define a complex line
             bundle, equivalently a principal U(1) comparison bundle" (bytes
             :38-41), and a bundle is a glued object.
```

**THIS IS A MATCHING CONDITION, IT IS EVALUATED ON OVERLAPS, AND ITS OWN GROUND
ARTIFACT MARKS IT "*** THE FIND ***".** It is closer in form to Shape Three (a)
than either of the two the artifact reports: NET row `N` matches by a DECLARED
LABEL IDENTITY and R9 by a shared unit at a cell, whereas C-4 is an agreement
condition on triple overlaps — the classical form the shape describes.

**AND THE ARTIFACT WAS RIGHT TO DISQUALIFY IT — HAD IT LOOKED.** O23SR states the
disqualifier itself, :572-581, quoted WHOLE:

```text
       (b) ITS INPUT DOES NOT EXIST OF RECORD. The census's own §4 already types
           this, and states it more sharply than anything it says about B-8:
             "actual_PRPS_endpoint_comparison_cover_definitions = 0
              record_side_topology_or_smooth_structure_definitions_for_U_i = 0
              'Nothing in the swept corpus defines the record-side patches U_i or
               an actual PRPS endpoint-comparison cover.'"
           and: "B-6 consumes patches and yields lifts and transitions; C-4 tests
           a cocycle on those transitions. Both run on an input the census never
           produces. This is THE CLEANEST UNPAIRED ITEM in the list: the count is
           zero and it is counted at bytes."
```

**THE DEFECT IS NOT THAT THE ANSWER WOULD HAVE CHANGED. THE DEFECT IS THAT THE
ARTIFACT REPORTED "TWO OF THEM" WITHOUT LOCATING, DISPLAYING OR GRADING THE
THIRD, WHICH ITS OWN SEALED GROUND FLAGS AS "THE FIND".** An import audit that
grades "every match reported" cannot be complete when the match set is
under-collected — the grading is honest and the collection is not.

This audit records for completeness, and does not rely on it: C-4's and B-6's
source `LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md` carries **no sidecar in either
root** and is unsealed (§3). C-4 and B-6 themselves sit in sealed artifacts and
are quoted from those.

---

## §7 — COMMISSION ITEM (A): VOCABULARY READ AS STRUCTURE. THE FOUR **CARRIES** ROWS, RE-TESTED

For every row the artifact grades CARRIES, this audit demanded the sealed
sentence carrying the structure and a display of the structure doing the work.

### §7.1 ROW 3.2 (R9 / JOINT LANDING) — **CARRIES. UPHELD.**

Re-read whole at `STAGE8_7A_JUNCTION_U1_SHARED_CORE_DARIO_V001.md` :375-397. The
condition is displayed with all four clauses and the structure does the work:

```text
"JOINT LANDING at e holds iff there is a SINGLE declared cross-sector unit u(e),
 routed through the one R4 seam, such that:"
   J1 DECLARATION IS SHARED ... J2 PRESENTATION-INVARIANT ...
   J3 NOT IMPLICITLY ONE, AND DETERMINATE ... J4 ONE OBJECT, NOT TWO RETURNS ...
```

Two maps join at one locus **iff** an induced quantity is a single shared object
there. That is a matching condition carried by structure, not by vocabulary —
note that the word "match" does not occur in it. **The artifact's grade is
correct and its abbreviation of J1–J4 is marked with explicit ellipses.
UPHELD.**

### §7.2 ROW 3.1 (NET ROW `N`) — **DOWNGRADE TO PARTLY CARRIES.**

The row is graded CARRIES on text reading "On matched carriers ... identity cell
matching" — three matching words in one clause. This audit re-read NET :242
WHOLE (all five columns; the artifact's transcription is EXACT) and O26SR
:1150-1155, which types it:

```text
"CAUSE       ISOLATED: the COUNTING CATEGORY, not the rule's content. Tested and
            rejected as causes: matched carriers (a domain restriction, silent
            on multiplicity); the support condition (per-cell containment only,
            names no second cell); the cells themselves (never touched by the
            joiner)."
```

**THE ARTIFACT'S OWN PROSE STATES THE DISQUALIFIER** — "It is NOT an agreement
condition evaluated on a shared surface" — **and then grades the row CARRIES
anyway.** Shape Three (a) asks only for "a matching condition governing when two
things join", which a domain restriction on admissible carriers arguably is; so
this audit downgrades rather than strikes. **PARTLY CARRIES.** Recorded to the
artifact's credit: it quoted the sentence that undercuts its own grade.

### §7.3 ROWS 3.3 AND 3.4 — *** DEFECT D-5. THESE CANNOT BE "CARRIES" UNDER THE TABLE'S OWN DEFINITION. ***

**SEVERITY: CORRECTION.** The table defines its grades at §7.2, verbatim:

```text
"**CARRIES = the record's own text carries the shape's structure.  RESEMBLES =
the record's text resembles the shape's description without carrying its
structure.**"
```

The commission's Shape Three (b), verbatim from the artifact's own §0 restatement:

```text
"(b) — the deliverable — an OBJECT carrying the disagreement when
      the matching fails: a residue, a defect term, a surface-supported quantity,
      rather than a verdict of obstruction."
```

Rows 3.3 and 3.4 are graded **CARRIES (part b)** with WHY columns reading, in the
artifact's own words, "MISMATCH -> VOID. An OBSTRUCTION." and "MISMATCH -> A
VERDICT."

**A VERDICT OF OBSTRUCTION IS THE ALTERNATIVE THE SHAPE EXPLICITLY EXCLUDES. IT
CANNOT CARRY THE STRUCTURE OF THE THING IT IS DEFINED AGAINST.** Those two rows
record that the record ANSWERS part (b)'s question in the negative — which is a
real and correctly-reported finding — but under the table's own definition their
grade is not CARRIES. The consequence is visible in the totals line:

```text
ARTIFACT:  "TOTALS   CARRIES 4 (all in Shape Three)"
AT BYTES:  Under the table's stated definition, 2 rows carry a shape's structure
           (3.1 partly, 3.2 fully).  The other 2 record the shape's negation.
FLAG:      matches_graded_CARRIES = 4  carries the same inflation.
```

This is the commission's item (A) occurring **inside the instrument built to
prevent it**: the grade tracks the presence of matching-shaped material rather
than the structure the shape describes.

### §7.4 *** DEFECT D-6 — THE IMPORT AUDIT'S TALLY IS ARITHMETICALLY WRONG ***

**SEVERITY: CORRECTION, AND IT RUNS IN THE FLATTERING DIRECTION.**

The §7.2 table has fifteen rows: 1.1 1.2 1.3 1.4 2.1 2.2 2.3 2.4 2.5 3.1 3.2 3.3
3.4 3.5 3.6. This audit extracted the grade of each:

```text
RESEMBLES  1.1  1.2  1.3  1.4  2.1  2.2  2.3  3.5  3.6      = 9
CARRIES    3.1  3.2  3.3  3.4                               = 4
PARTLY CARRIES  2.4                                         = 1
DOES NOT CARRY  2.5                                         = 1
                                                       TOTAL = 15  = rows. OK.

ARTIFACT'S TOTALS LINE, verbatim:
  "TOTALS   CARRIES 4 (all in Shape Three) ; PARTLY CARRIES 1 ; RESEMBLES 7 ;
            DOES NOT CARRY 1."
  4 + 1 + 7 + 1 = 13.  THE TABLE HAS 15 ROWS.  TWO ROWS ARE UNCOUNTED.

ARTIFACT'S FLAG BLOCK repeats it:
  "matches_graded_RESEMBLES                             = 7"
```

**RESEMBLES IS 9, NOT 7.** The error under-reports, by two, the count of matches
that are vocabulary-only — the single quantity this commission exists to measure.
The artifact states it twice, in the import audit and in the flag block, and
neither is checkable against the other because both carry the same wrong number.

---

## §8 — COMMISSION ITEM (F): QUOTATION INTEGRITY, EVERY QUOTATION CHECKED TO ITS SPAN END

Eleven quoted spans re-opened at bytes. **Nine are exact and complete.** Two
carry alterations, both non-distorting, neither disclosed.

```text
CLEAN — VERIFIED EXACT AND WHOLE TO SENTENCE END
  §4.2  CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md :17-24 — the Principle clause,
        code fence included.  EXACT.  The two "nearest influence-flavoured
        clauses" it then quotes are also exact and are correctly attributed.
  §4.5  COMPLETE_QSPEC ... _SPEC_V001.md :40-48 — the Liveness rule, whole, and
        the "Theorem obligation" that follows it.  EXACT.
  §3.4  STAGE8_GALERKIN_COMMUTATOR_T12SR_V001.md :295-299 — GC-2 STEP 1.  EXACT,
        including "EXACT." and the A_n line.
  §3.4  "16 b_1^2 + 32 b_2^2 >= 0" — present at :419.  EXACT.
  §5.1  NET :242 row `N` — all five columns.  EXACT, and the claim "quoted WHOLE"
        is true.
  §5.1  NET §4.2 :332-340 (tau_(ba), NS-8).  EXACT.
  §5.2  7A_JUNCTION :395-397 TYPING.  EXACT, whole, to the paragraph end
        including "(both residues stand, per the OVERLAPPING determination)."
  §5.1  7A_JUNCTION :375-393 J1-J4.  Abbreviated WITH EXPLICIT ELLIPSES.  Lawful.
  §5.5  STAGE8_G1_KERNEL_CERTIFICATE_V001.md :118-121 OBL-D.  EXACT to the
        sentence end "tends to zero."  The source continues "One hypercubic
        sequence is a regression fixture, not proof of universality." — a
        truncation AT a sentence boundary, which is lawful, and which would have
        strengthened the artifact's own point had it been kept.
  §5.1  O26SR "a domain restriction, silent on multiplicity" — THIS AUDIT FIRST
        FAILED TO FIND IT and was preparing a fabrication finding.  The phrase is
        real, at O26SR :1151-1152, line-WRAPPED across the newline, which is why a
        single-line grep misses it.  *** THE ATTRIBUTION IS CORRECT AND THE
        QUOTATION IS FAITHFUL.  NO FABRICATION.  This audit's near-miss is
        recorded here rather than discarded. ***

D-7  SEVERITY: NOTE — A SILENT MID-SENTENCE START, PRESENTED AS VERBATIM.
     Used twice, at §3.4 ROLE 2 and again at §4.3(b).  The artifact prints:
       "VOLUME DIAGONAL x = y, NOT THE SHARP BOUNDARY. SMOOTHING ONLY THE
        BOUNDARY WILL NOT REMOVE A |x-y|^-3 POSITIVE MAJORANT."
     The source sentence, STAGE8_WALL_BOUNDARY_CLOSURE_S9AD_V001.md :175-177,
     whole, is:
       "THE FATAL LOCAL INTEGRAL IS THE VOLUME DIAGONAL x = y, NOT THE SHARP
        BOUNDARY. SMOOTHING ONLY THE BOUNDARY WILL NOT REMOVE A |x-y|^-3
        POSITIVE MAJORANT."
     The subject — "THE FATAL LOCAL INTEGRAL IS THE" — is dropped from inside the
     quoted span with no ellipsis.  NON-DISTORTING: the full sentence supports the
     artifact's use MORE strongly than the truncation does.  Cite drift: the span
     begins at :175, not :176.

D-8  SEVERITY: NOTE — EMPHASIS ADDED INSIDE A "VERBATIM" SPAN.
     §5.1 prints NET :347 as: "V001 instantiates only the matched two-node class,
     so NO PERMUTATION OR INTERTWINER IS SELECTED."  The source reads
     "...so no permutation or intertwiner is selected."  Capitalisation is the
     artifact's, introduced inside a span labelled verbatim, undisclosed.

D-9  SEVERITY: NOTE — LINE-CITE DRIFT.
     §3.5 attributes "NO FORCING FOUND" to STAGE8_REQUIRE_G3_CHECK_V001.md :148.
     The verdict occurs at :56, :85, :100 and :145; not at :148.  The quotation
     itself is faithful and the :136-139 span is faithful.  The finding is
     unaffected.

D-10 SEVERITY: NOTE — TREE-STATE ARITHMETIC.
     §2 declares ROOT1 "6869 files, 1925 *.md".  Reconstructed at this audit's
     instant and rolled back over the three later objects, the total 6869 EXCLUDES
     the artifact and its sidecar while the 1925 INCLUDES the artifact — an
     internal off-by-one between the two numbers on the same line.  ROOT2's
     "7805 files, 2308 *.md" reproduces EXACTLY.  §2 also gives
     STAGE8_ENVIRONMENT_FACTOR_O31SR_V001.md as "Aug 15 18:13"; its mtime on disk
     is Aug 15 18:22.  Neither point bears on any verdict.
```

---

## §9 — COMMISSION ITEMS (D), (E), (G)

### §9.1 ITEM (D) — THE IMPORT AUDIT: **PASSES ON ORIGIN, FAILS ON COMPLETENESS AND TALLY**

```text
DOES IT STATE THE SHAPES' EXTERNAL ORIGIN?   *** YES, AND EXEMPLARILY. ***
  §0, before any test, and §7.1, after every test, both in block capitals:
  "THE THREE SHAPES TESTED IN THIS ARTIFACT WERE SUPPLIED BY THE COMMISSION FROM
   OUTSIDE THIS CORPUS. THEY ARE NOT THE RECORD'S OWN VOCABULARY, THEY CARRY NO
   AUTHORITY IN IT, AND NOTHING IN THE RECORD IS OBLIGED TO INSTANTIATE ANY OF
   THEM."
  It further declares which words are the commission's ("spread", "reachability
  edge", "residue-as-object", "surface-supported") and states that no absence is
  a defect of the record.  THIS AUDIT UPHOLDS ALL OF IT.

DOES IT GRADE EVERY MATCH HONESTLY?          *** PARTLY. ***
  HONEST:  the CARRIES/RESEMBLES column is applied per row, the LEXICAL and
           INVERTED sub-grades are real distinctions, and CL-6 names three
           tokens a vocabulary-led sweep would have scored as hits and refuses
           them ("contractible", "overlap law", "dispersion").  That is the
           discipline this commission asks for and the artifact keeps it.
  FAILS:   (i) the match set is UNDER-COLLECTED — C-4/B-6 (D-4) and the
               discrepancy cocycle family (D-1) are never collected, so they are
               never graded;
          (ii) two rows are graded CARRIES for carrying the shape's NEGATION
               (D-5);
         (iii) the tally is wrong by two in the flattering direction (D-6).
```

### §9.2 ITEM (E) — CONSTRUCTED MECHANISM, PROPOSAL, OR ADOPTION: **NONE. CLEAN.**

```text
Swept the artifact for proposal-shaped language:
  we propose|i propose|recommend|should be adopted|is adopted here|hereby|
  suggest that|would fix|remedy
ONE HIT IN 1416 LINES, and it is the artifact's own denial at :1005:
  "adopted, installed, proposed, or recommended. No sentence below or above
   asserts"
NO MECHANISM, ROUTE, REPAIR, OR CONSTRUCTION IS SUPPLIED ANYWHERE IN THE AUDITED
ARTIFACT.  Where a shape is absent the absence is displayed and the sweep is
declared, with no route to filling it named, costed, hinted or ranked.
ITEM (E): CLEAN, AND THIS AUDIT CONSTRUCTS, PROPOSES AND ADOPTS NOTHING EITHER.
```

### §9.3 ITEM (G) — LENS TOKENS AND NUMBERS OF PROGRAM IMPORT

```text
MEASURED CONSTANTS / PROGRAM VALUES IN THE AUDITED ARTIFACT:  *** NONE. ***
  Probed for 137.0|1/137|0.00729|7.297|fine-structure|CODATA|measured value of
  — ZERO hits in 1416 lines.  Every numeral in the artifact is either a FILE
  COUNT from its own declared sweeps or a numeral inside a quotation of a sealed
  corpus artifact ("exact-3/2", "|x-y|^-3", "16 b_1^2 + 32 b_2^2", "r(t) =
  min(t, 1-t)").  No value originates in the artifact.  CONFIRMED.

D-11  SEVERITY: NOTE — ONE OVERSTATEMENT IN §7.1.
  §7.1 states, verbatim: "NOTHING WAS IMPORTED FROM OUTSIDE THE TWO DECLARED
  ROOTS. No external mathematics, no textbook theorem, no physical constant, no
  measured value, no imported GR, no scale."
  The clause "no external mathematics, no textbook theorem" is contradicted by
  the artifact's own §2.1, which lists as search tokens: "modulus of continuity",
  "contraction mapping", "Cauchy sequence", "Banach fixed", "fixed-point
  theorem".  These are external mathematical vocabulary.
  DISPOSITION: NOT A LENS IMPORT.  They are used ONLY as grep strings against the
  corpus, never as authority, never as a premise, and the artifact reports
  "modulus of continuity" as ZERO IN BOTH ROOTS rather than reasoning from it.
  The sentence overstates; the practice is clean.  Recorded, not charged.

LENS TOKENS BEYOND THE THREE DECLARED SHAPES:  NONE LOCATED.  The artifact's own
  prose vocabulary stays inside the three shapes plus the four words it declares
  as the commission's.  "Obstruction" is used as a type-name and is drawn from
  the commission's own Shape Three statement ("rather than a verdict of
  obstruction"), not imported separately.
```

---

## §10 — THIS AUDIT'S OWN IMPORT AUDIT: EVERY MATCH IT REPORTS, GRADED

**THE THREE SHAPES WERE SUPPLIED BY THE COMMISSION FROM OUTSIDE THE CORPUS
(§0).** For every match this audit reports, the grade below records whether **the
record's own text CARRIES THE STRUCTURE** or **only RESEMBLES THE DESCRIPTION**.

```text
#    THE RECORD'S OBJECT (this audit's finds)      GRADE      WHY
-------------------------------------------------------------------------------
A.1  beta_f := rho_f^C2(C2_m^fin) - C2_n^fin,      PARTLY     The record's own
     the record's own "discrepancy cocycle";       CARRIES    name is
     supp(beta_f) in (J13-1); composition law                 "discrepancy
     beta_gf = beta_g + Eta_g(beta_f)                         cocycle". It is a
                                                              DIFFERENCE, it has
                                                              a SUPPORT, and it
                                                              is a TERM in a
                                                              sealed inclusion —
                                                              the three things
                                                              the audited
                                                              artifact says the
                                                              corpus has none of.
                                                              NOT full CARRIES:
                                                              it lives in the
                                                              REFINEMENT/TRANSPORT
                                                              direction, not across
                                                              a joining face, and
                                                              (C1-7) sets it = 0 on
                                                              the old image.
A.2  "the J13 boundary-discrepancy cocycle needed  PARTLY     The record names a
     for refinement-path independence"; "no        CARRIES    BOUNDARY-supported
     boundary discrepancy cocycle under                       discrepancy object
     refinement composition is required"                      and adjudicates its
                                                              status. Structure
                                                              named and located;
                                                              not displayed as
                                                              built.
A.3  "the contact defect term                      PARTLY     Shape Three's
     β_f := rho_f^C2(C2_m^fin)-C2_n^fin vanishes   CARRIES    deliverable noun,
     on old-image (β_f=0)"                                    attached to the
                                                              object of A.1. The
                                                              vanishing is a
                                                              RESULT about it, not
                                                              a denial of it.
A.4  "zero-defect terms form a nonempty            RESEMBLES  A defect term at an
     common-refinement equalizer"                             equalizer — but the
                                                              structure displayed
                                                              is the EQUALIZER;
                                                              the term's role is
                                                              to be zero.
A.5  C-4 THE TRIPLE-OVERLAP COCYCLE CONDITION.     CARRIES    A genuine matching
     "YIELDS true/false: g_ij g_jk g_ki = 1."      (part a)   condition evaluated
     TYPE CONSTRAINT.                                         ON OVERLAPS. Closer
                                                              in form to the shape
                                                              than either matching
                                                              condition the audited
                                                              artifact reports.
A.6  B-6 THE LOCAL PROJECTIVE LIFT AND ITS         CARRIES    Transition functions
     TRANSITIONS. "*** THE FIND ***" — z_j =       (part a)   on overlaps obeying a
     g_ij z_i; "a bundle is a glued object"                   cocycle. Its own
                                                              ground artifact calls
                                                              it gluing data "in
                                                              the exact technical
                                                              sense".
A.7  A.5/A.6's disqualifier: "Both run on an       DOES NOT   The input is counted
     input the census never produces. This is      CARRY      at ZERO of record.
     THE CLEANEST UNPAIRED ITEM in the list:                  The condition is
     the count is zero and it is counted at                   stated on an object
     bytes."                                                  the corpus does not
                                                              define.
A.8  R9 / JOINT LANDING at e, J1-J4, u(e)          CARRIES    Re-derived at bytes;
                                                   (part a)   the audited
                                                              artifact's grade
                                                              UPHELD (§7.1).
A.9  NET row `N`, "On matched carriers ...         PARTLY     Three matching words
     identity cell matching"; typed of record      CARRIES    in one clause; the
     as "a domain restriction, silent on                      record's own typing
     multiplicity"                                            is a DOMAIN
                                                              RESTRICTION.
                                                              Downgraded from the
                                                              audited artifact's
                                                              CARRIES (§7.2).
A.10 NET's void column; "Joint landing is a        RESEMBLES  These record the
     FALSIFIER, not a constructor"                            NEGATION of part (b).
                                                              They answer the
                                                              question; they do not
                                                              carry the structure.
                                                              Regraded from the
                                                              audited artifact's
                                                              CARRIES (§7.3).
A.11 "BOUNDARY-supported" decay assets             RESEMBLES  The token is the
     ("b_D vanishes to all orders at the           (LEXICAL)  shape's; the object is
     diamond edge")                                           a DECAY ASSET, not a
                                                              residue of a matching.
A.12 "force the incidence to be a MATCHING,        RESEMBLES  A GRAPH-THEORETIC
     hence b_1 = 0 for every V up to 8"            (LEXICAL)  matching (degree <= 1).
                                                              A homonym of Shape
                                                              Three's "matching".
                                                              Neither artifact uses
                                                              it; recorded so it is
                                                              not scored later.
-------------------------------------------------------------------------------
TOTALS, ROW BY ROW, SO THE TALLY IS CHECKABLE AGAINST THE TABLE — this is the
discipline whose absence D-6 records:
  CARRIES         A.5  A.6  A.8                             = 3
  PARTLY CARRIES  A.1  A.2  A.3  A.9                        = 4
  RESEMBLES       A.4  A.10 A.11 A.12                       = 4
  DOES NOT CARRY  A.7                                       = 1
  3 + 4 + 4 + 1 = 12 = the twelve rows A.1 through A.12.  BALANCED.
```

### §10.1 READ REFUSALS HONOURED

```text
NO register / tracker / road / plan / continuation file was opened.  The bar was
  applied AT THE PATH FILTER of every sweep, before any read: ROOT1 1927 -> 1889
  *.md swept, ROOT2 2308 -> 2264.  No excluded basename was passed to a reader.
"Q-..." tokens: EXPECTED-UNLOCATABLE.  Encountered inside quoted sealed text
  (Q-408, Q-279, Q-247, Q-54).  Carried as opaque labels, never chased, never
  resolved, nothing defaulted.
NO GIT COMMAND OF ANY KIND was run.
POST-CUTOFF FILES: STAGE8_SIGN_AUDIT_O33SR_V001.md and
  STAGE8_GAUGE_AS_CONTENT_O34SR_V001.md postdate the audited artifact.  NO
  FINDING IS CHARGED ON THEIR CONTENT.  Where the latter appears in a file list
  it is marked OUT-OF-CUTOFF.
FILES WRITTEN: exactly two — this audit and its seal sidecar, at the commission's
  distinct path, probed ABSENT twice before the first write.  No existing file
  was edited.
TOOLS: ls, find, grep -lIE / -nIiE, sed, awk, wc, shasum -a 256 -c, xargs.  No
  CAS.  No numeric evaluation.  No execution of corpus content.
```

---

## §11 — CHOICE LEDGER

```text
CL-1  DISCLOSED MY OWN NEAR-MISS FABRICATION FINDING RATHER THAN DELETING IT.
      TAKEN        My first grep for "a domain restriction, silent on
                   multiplicity" returned ONLY the audited artifact — which reads
                   as a fabricated quotation attributed to a named sealed file.
                   Before writing that finding I re-searched on the fragments and
                   found the phrase at O26SR :1151-1152, LINE-WRAPPED across a
                   newline, which no single-line grep can match.  THE ARTIFACT IS
                   INNOCENT AND MY INSTRUMENT WAS AT FAULT.
      ALTERNATIVE  Delete the episode and report only the confirmed attribution.
      WHY          A DEFAULT-REFUTE audit that silently discards its own false
                   positives cannot be checked for how many it generated.  The
                   audited artifact disclosed its own defective S1a pattern; an
                   auditor who would not do the same has no standing to grade it.
                   Recorded at §8 in full.

CL-2  GRADED THE DISCREPANCY COCYCLE **PARTLY CARRIES**, NOT **CARRIES**.
      TAKEN        beta_f has a support, a composition law and a place in a
                   sealed expression — but it runs in the refinement/transport
                   direction, not across a joining face, and (C1-7) sets it = 0
                   on the old image.
      ALTERNATIVE  Grade it CARRIES and declare Shape Three (b) INSTANTIATED.
      WHY          That would be the same error in the opposite direction: reading
                   the words "discrepancy cocycle" and "defect term" as the
                   structure.  The refutation of the audited artifact does not
                   require the stronger grade — D-1 stands on the artifact's
                   disqualifier ("no support ... no term in any expression") being
                   FALSE OF THE CORPUS, which it is at either grade.
                   THIS IS THE DECISION THAT DETERMINES §6 AND THE VERDICT.

CL-3  DID NOT CHARGE ANY FINDING TO POST-CUTOFF FILES.
      TAKEN        STAGE8_GAUGE_AS_CONTENT_O34SR_V001.md (Aug 15 18:30) contains
                   "NEAR-HIT A — the direct/two-step discrepancy cocycle `beta`"
                   and the line "DEFECT the triple-overlap cocycle
                   g_ij g_jk g_ki = 1 is the surface-supported ...".  It postdates
                   the audited artifact by two minutes.
      ALTERNATIVE  Cite it as proof the object was findable.
      WHY          An artifact cannot be faulted against a file that did not exist
                   when it ran.  Every ground for D-1 through D-4 is a file that
                   PREDATES the audited artifact, and most are files it
                   seal-verified itself.  The post-cutoff file is marked and set
                   aside.

CL-4  CONFIRMED SHAPES ONE AND TWO INSTEAD OF HUNTING HARDER FOR A REFUTATION.
      TAKEN        Ran independent patterns (B1-B3, and S1c which the artifact
                   declared and never reported), opened every near-hit, and found
                   nothing the artifact missed.
      ALTERNATIVE  Keep sweeping until something turned up.
      WHY          DEFAULT-REFUTE is a standard of proof, not a quota of kills.
                   Two of the three verdicts are correct and independently
                   re-derived, and saying so plainly is part of the finding.

CL-5  SEPARATED "THE ANSWER WOULD NOT HAVE CHANGED" FROM "THE SEARCH WAS SOUND".
      TAKEN        For D-4 (C-4/B-6) the corpus's own disqualifier — the input is
                   counted at ZERO — means a complete search would still have
                   returned part (a) PRESENT.  The defect is charged anyway.
      WHY          The commission's instruction is that an INSTANTIATED verdict
                   must rest on structure carried, not words present.  The
                   converse binds equally: an ABSENT or PARTIAL verdict must rest
                   on a search performed, not a search declared.  A right answer
                   from an under-run sweep is not a determination.

CL-6  COUNTED FILES, NOT LINES, IN EVERY CENSUS — matching the audited artifact's
      CL-8 so the two are directly comparable.  Where a token's weight sits in one
      file, that is stated.

CL-7  RE-RAN THE ARTIFACT'S PATTERNS WITH ITS OWN ANCHORS BEFORE JUDGING ITS
      COUNTS.
      TAKEN        My first pass used unanchored tokens and produced apparent
                   discrepancies (horizon 53 vs 10; reach 732 vs 298).  Re-running
                   with the artifact's declared `\b` anchors reproduced its counts
                   exactly.
      WHY          Charging a count defect that was an artefact of MY pattern is
                   precisely the failure the artifact disclosed in itself at §3.1.
                   The near-miss is recorded here rather than buried.
```

---

## §12 — TOY_SEPARATION

```text
IS ANY OBJECT IN THIS AUDIT A TOY, A MODEL, A STAND-IN, OR AN ILLUSTRATION?
NO. This audit contains no constructed object at all: seal results, file counts
from declared patterns, quotations at bytes, and typings of quotations.  Nothing
is built here, so nothing here can be mistaken for a built thing.

THE ACTUAL SURFACE, NOT A TOY: the question was whether a specific sealed
artifact's determination survives re-derivation against the real corpus at real
bytes.  Every finding above is a property of files on disk at the declared
cutoff, re-checkable by re-running the declared patterns of §2.1 against the
declared roots.

THE THREE PLACES A TOY COULD HAVE CREPT IN, EACH NAMED:
  1. beta_f COULD HAVE BEEN TREATED AS AN INSTANTIATION OF SHAPE THREE.  It is
     not.  It is graded PARTLY CARRIES (CL-2), its distances from the shape are
     stated in the same breath as its strengths, and NO CLAIM IS MADE that the
     record instantiates Shape Three (b).  Locating an object the audited
     artifact missed is not the same as installing it, and this audit installs
     nothing.
  2. THE THREE SHAPES COULD HAVE BEEN TREATED AS OBJECTS OF THE RECORD.  They are
     not.  §0 and §10 state, before and after every test, that they are imports
     with no authority in the corpus.  No absence is called a defect OF THE
     RECORD; every defect charged is a defect of the AUDITED ARTIFACT's search or
     tally, never of the corpus.
  3. THIS AUDIT'S OWN GRADING TABLE (§10) is one step from a proposed typology.
     It is not one: every row's object is transcribed from quoted bytes of a
     seal-verified artifact, and every grade is justified by that artifact's own
     words.

NO MECHANISM IS SUPPLIED ANYWHERE.  Nothing is proposed to repair the audited
artifact, no route to instantiating any shape is named, costed, hinted or ranked,
and no successor build is specified.  Where a defect is found, the defect is
displayed and the bytes that establish it are quoted.
```

---

## §13 — FLAG BLOCK

```text
F-1  SEVERITY: MATERIAL — THE PART-(b) DISQUALIFIER IS FALSE OF THE CORPUS.
     The audited artifact's Shape Three (b) determination rests on the sentence
     "It has no support, no locus, no carrier, and no place in any expression."
     The record writes supp(beta_f) and uses it inside a sealed inclusion
     (J13-1), and gives the defect a composition law.  The sentence is true of
     the J-II residues it was written about and FALSE as the statement about the
     corpus that §5.6 and §11 turn it into.  (D-1, §6.2.)

F-2  SEVERITY: MATERIAL — A DECLARED SWEEP WAS NOT REPORTED, AND IT IS THE ONE
     THAT FINDS F-1.  S3a, S3d and S1c occur exactly once each in the whole
     artifact — inside the §2.1 block headed "EVERY PATTERN, VERBATIM".  No
     result for any of the three appears anywhere.  S3a's declared branch
     `\bdiscrepanc` returns 131 ROOT1 files and locates the discrepancy cocycle
     directly.  (D-2, §6.4.)

F-3  SEVERITY: MATERIAL — A FALSE EXACTNESS CLAIM.  §5.4's "Every hit is one of
     exactly two things, checked line by line" is false: "defect term"/"defect
     terms" is a third class — 18 occurrences in ROOT1, of which 5 are the
     audited artifact's own prose and 13 are corpus — attached to the object of
     F-1.  (D-3, §6.5.)

F-4  SEVERITY: MATERIAL — A THIRD MATCHING CONDITION, ON OVERLAPS, INSIDE THE
     ARTIFACT'S OWN SEALED GROUND.  C-4 (INGREDIENT_CENSUS O17SR :283) and B-6
     (GLUING_CANDIDATE O23SR :555, self-marked "*** THE FIND ***") are in two of
     the eight artifacts listed at the audited artifact's own §1.  Part (a) is
     reported as "TWO OF THEM".  The corpus's own disqualifier (input counted at
     ZERO) means the verdict would not have changed — the search, not the answer,
     is what fails.  (D-4, §6.6.)

F-5  SEVERITY: CORRECTION — TWO ROWS GRADED "CARRIES" FOR CARRYING THE SHAPE'S
     NEGATION.  Rows 3.3 and 3.4 record MISMATCH -> VOID and MISMATCH -> VERDICT,
     which is the alternative Shape Three (b) is defined against.  Under the
     table's own stated definition of CARRIES they are not carriers.  (D-5, §7.3.)

F-6  SEVERITY: CORRECTION — THE IMPORT AUDIT'S TALLY IS WRONG BY TWO, IN THE
     FLATTERING DIRECTION.  §7.2 TOTALS and the §10 flag both state RESEMBLES =
     7; the table has 9.  4 + 1 + 7 + 1 = 13 against 15 rows.  The under-count is
     of vocabulary-only matches — the quantity this commission exists to measure.
     (D-6, §7.4.)

F-7  SEVERITY: NOTE — QUOTATION.  One silent mid-sentence start presented as
     verbatim, used twice (D-7); one capitalisation added inside a verbatim span
     (D-8); one line-cite drift (D-9); one tree-state off-by-one and one mtime
     discrepancy (D-10); one overstatement about external mathematics that the
     artifact's own practice does not commit (D-11).  NONE DISTORTS A FINDING.
     Nine of eleven checked spans are exact and complete to sentence end.

F-8  SEVERITY: NOTE — WHAT THE AUDITED ARTIFACT GOT RIGHT, RECORDED SO IT IS NOT
     LOST IN THE REFUTATION.  Seals 28/28 genuinely OK (this audit makes it
     30/30).  Census counts reproduce EXACTLY under its own anchors.  Its three
     headline zero-counts are real in the corpus.  It disclosed its own defective
     S1a pattern rather than repairing it silently.  It disclosed its own
     self-hits at F-2 before any auditor forced it.  It reported its strongest
     near-misses at full strength before disqualifying them (CL-3).  It refused
     three lexical traps by name (CL-6).  Shapes One and Two are independently
     re-derived here and both verdicts stand.

F-9  SEVERITY: NOTE — THIS AUDIT'S OWN NEAR-MISS, DISCLOSED.  A single-line grep
     failed to match a line-WRAPPED quotation and this audit came within one
     re-check of charging a fabricated-quotation finding against an innocent
     attribution.  Recorded at §8 and CL-1.  No finding above rests on a
     single-line grep of a phrase that could wrap.

NO FENCE WAS APPROACHED.
  alpha_computed = false        — no alpha quantity appears in this audit.
  proof_authorized = false      — nothing here is offered as a proof.
  kappa_record_computed = false — kappa is not named outside a filename.
  No value originates here.  No number is used as a program quantity.  No
  measured constant appears.  No comparison to any measured quantity is made.  No
  git operation was performed.  No mechanism, route, repair or construction is
  supplied.
```

```text
FLAGS
shapes_supplied_from_outside_the_corpus                = true
target_seal_verified_from_own_directory                = true (OK, exit 0)
seals_reverified_independently                         = 30 OK / 0 mismatch
audited_artifact_seal_claim_28_of_28                   = TRUE, CONFIRMED
census_counts_reproduce_under_declared_anchors         = true (deltas = self-hits)
shape_one_verdict_absent                               = CONFIRMED
shape_two_verdict_absent                               = CONFIRMED
shape_three_part_a_present                             = CONFIRMED (under-collected)
shape_three_part_b_determination                       = *** REFUTED ***
part_b_disqualifier_false_of_the_corpus                = true  (supp(beta_f); J13-1)
residue_object_with_support_located_by_this_audit      = true  (discrepancy cocycle)
declared_patterns_never_reported                       = 3     (S1c, S3a, S3d)
s3e_exactly_two_things_claim                           = FALSE (a third class, 18 hits)
matching_conditions_reported_by_artifact               = 2
matching_condition_missed_in_its_own_sealed_ground     = 1     (C-4 / B-6)
import_audit_states_external_origin                    = true  (exemplary)
import_audit_tally_correct                             = FALSE (RESEMBLES 9, not 7)
rows_graded_CARRIES_that_carry_the_shapes_negation     = 2     (3.3, 3.4)
quotation_spans_checked                                = 11
quotation_spans_exact_and_whole                        = 9
quotation_spans_with_undisclosed_alteration            = 2     (non-distorting)
fabricated_quotation_located                           = false (near-miss disclosed)
mechanism_or_proposal_in_audited_artifact              = false
measured_constant_in_audited_artifact                  = false
findings_charged_to_post_cutoff_files                  = 0
alpha_computed                                         = false
proof_authorized                                       = false
kappa_record_computed                                  = false
value_computed_of_any_kind                             = false
number_used_as_program_quantity                        = false
measured_constant_compared                             = false
git_operation_performed                                = false
existing_file_edited                                   = false
register_tracker_road_plan_continuation_file_opened    = false
mechanism_supplied                                     = false
anything_proposed_adopted_or_constructed               = false
ALL_RESULTS                                            = CLAIMED until re-checked.
```

---

## §14 — VERDICT

```text
SHAPE ONE   — FORCED CONVERGENCE.  *** CONFIRMED. ***
              ABSENT, and independently re-derived.  This audit ran its own
              spread-decrease patterns and the artifact's own unreported S1c, and
              located no quantity measuring the spread of a family and no
              condition forcing such a quantity to fall.  The four near-hits are
              a dead covariance-contraction route, an absence inside a PASS row,
              and the artifact's own flag line.

SHAPE TWO   — REACHABILITY EDGE.   *** CONFIRMED. ***
              ABSENT, and independently re-derived.  The vocabulary census
              reproduces exactly; the three carriers re-open at bytes as an
              ASSIGNED cell with a containment test, a MANDATED indicator, and a
              direction label that "never touches the cells"; last(r) is a real
              limit of influence that bounds an OPERATION, and the co-located
              "boundary" is an index.  Reporting last(r) at full strength before
              disqualifying it is the correct handling and is upheld.

SHAPE THREE — MATCHING WITH RESIDUE.  *** REFUTED. ***
              The headline "PARTIALLY INSTANTIATED" is not contradicted, and part
              (a) PRESENT is correct.  WHAT IS REFUTED IS THE PART-(b)
              DETERMINATION — the commission's stated priority deliverable — AND
              THE GROUNDS GIVEN FOR IT:
                (1) The disqualifier "no support, no locus, no carrier, and no
                    place in any expression" is FALSE OF THE CORPUS.  The record
                    names a "discrepancy cocycle" beta_f, writes supp(beta_f),
                    uses it as a term in the sealed inclusion (J13-1), and gives
                    it the composition law beta_gf = beta_g + Eta_g(beta_f).
                (2) The sweep that would have found it — S3a, whose declared
                    branch `\bdiscrepanc` returns 131 ROOT1 files — was DECLARED
                    UNDER A HEADING READING "EVERY PATTERN, VERBATIM" AND ITS
                    RESULT NEVER REPORTED.  So were S3d and S1c.
                (3) §5.4's "every hit is one of exactly two things" is false:
                    "defect term" is a third class — 18 ROOT1 occurrences, 13 of
                    them corpus and 5 the artifact's own prose — attached to the
                    object of (1), while the artifact's closing
                    sentence is "A LIST OF UNMET OBLIGATIONS IS NOT A DEFECT
                    TERM."
                (4) Part (a) is reported as "TWO OF THEM" while a third matching
                    condition, evaluated ON OVERLAPS, sits in two of the eight
                    artifacts the determination seal-verified itself, one of them
                    self-marked "*** THE FIND ***".
              This audit does NOT find Shape Three (b) instantiated.  beta_f is
              graded PARTLY CARRIES: it runs in the refinement/transport
              direction rather than across a joining face, and (C1-7) sets it = 0
              on the old image.  THE REFUTATION IS OF THE DETERMINATION AND ITS
              SEARCH, NOT A REVERSAL OF ITS ANSWER.

OVERALL     — *** REFUTED. ***
              Two of three shape verdicts are CONFIRMED and stand unqualified.
              The refutation is localised and it lands on the commission's own
              priority question: the part-(b) determination rests on a
              characterisation the corpus falsifies at bytes, established by a
              sweep the artifact declared and did not report.  A right answer
              from an under-run search is not a determination.  The import audit
              states the shapes' external origin exemplarily and grades what it
              collects honestly, but it under-collects the match set and
              mis-tallies it by two in the flattering direction.

              THE ARTIFACT'S INSTRUMENT IS SOUND — 28/28 SEALS GENUINELY OK,
              CENSUS COUNTS EXACT, THREE REAL ZERO-COUNTS, ITS OWN PATTERN DEFECT
              AND ITS OWN SELF-HITS DISCLOSED UNFORCED.  THE FAILURE IS NOT
              CARELESSNESS AND IT IS NOT VOCABULARY READ AS STRUCTURE, WHICH THE
              ARTIFACT GUARDS AGAINST WELL.  IT IS THE MIRROR DEFECT THE
              COMMISSION NAMED SECOND: A STRUCTURE CARRYING THE SHAPE UNDER A
              WORD THE SWEEP NEVER REPORTED.

NOTHING IS CONSTRUCTED, PROPOSED, ADOPTED, OR SUPPLIED ANYWHERE IN THIS AUDIT.
Every defect is displayed with the bytes that establish it, and every confirmed
claim is re-derived rather than accepted.

FENCES AT CLOSE: alpha_computed = false ; proof_authorized = false ;
kappa_record_computed = false.
```

```text
END STAGE8_BOUNDARY_SHAPES_O32SR_AUDIT_V001
COMMISSION O32SR — SHAPES-AUDIT — 2026-08-15 — DETERMINATION ONLY
```

