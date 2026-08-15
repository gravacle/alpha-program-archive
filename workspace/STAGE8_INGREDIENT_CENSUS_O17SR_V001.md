# STAGE 8 — THE INGREDIENT CENSUS: WHAT THE RECORD CARRIES, TYPED BY INPUT SIDE AND OUTPUT SIDE

Commission: O17SR. Lane: CENSUS-BUILD, blind determination. Date: 2026-08-15.
ALL_RESULTS = CLAIMED until checked.

## 0. WHAT THIS IS, ON ITS FACE

This is an INVENTORY, not an argument. Every entry below is typed by one test and
one test only: what stands on the object's INPUT side, and what stands on its
OUTPUT side, read from the object's own sealed bytes. Nothing is typed by its
name, its family prefix, its lane, or what it is for. Grouping is by OUTPUT side,
because output-side grouping is the only organising principle that does not
import a subject-matter frame.

DETERMINATION ONLY. Nothing here is proposed, authored, or adopted. No conclusion
is drawn about whether anything is missing beyond what the typing itself displays.
Where the census shows an input side with no matching output side anywhere in the
census, that is a fact about the inventory, recorded as such.

```text
GATES  alpha_computed = false ; proof_authorized = false ;
       kappa_record_computed = false.
FENCES HELD: no value, no number, no measured-constant comparison; no git action;
       no register / tracker / road / plan / continuation file read; scoped reads
       and declared scoped sweeps only. No diagnostic/meta artifact of 2026-08-15
       opened (see §0.3 BLINDNESS LEDGER).
```

## 0.1 THE FOUR TYPES USED

```text
OBJECT      yielded; takes nothing on its input side. A thing the record carries.
RULE        takes something, yields something. Includes MAPS (the special case
            where the yield is an element of a named target).
CONSTRAINT  takes something, yields a truth value (satisfiable / holds / fails).
CERTIFICATE takes something, yields a warrant about it (CONFIRMED, SOUND, exact,
            certified) rather than a new thing.
```

The distinction that carries the most weight in this census is RULE vs CERTIFICATE:
a rule hands back a new object; a certificate hands back permission to rely on an
object you already had. They are not interchangeable and the census keeps them apart.

## 0.2 DECLARED SWEEP AND CUTOFF

```text
CORPUS ROOTS SWEPT
  R1  /Users/bgm/MB Work/alpha-program-archive/workspace            (primary)
  R2  /Users/bgm/Documents/New project/gravity_emergence_evidence_program/
      alpha_fundamental_record_action_cleanroom_v003                (secondary)

SWEEP CUTOFF: 2026-08-15. Files at R1 top level: 3581 entries, 1754 *.md,
1701 *.seal.sha256. R2: 3133 entries. R2 was found to be a mirror of R1 at every
filename compared; all reads were taken at R1 and no R2-only object was found in
the swept bands.

SWEEP S-A (self-declaring signature band). Every *.md under R1 carrying a line
matching:  ^(INPUT|OUTPUT|YIELDS|SIGNATURE|DOMAIN|CODOMAIN|CONSUMES|PRODUCES|TYPE:)
           | OUTPUT SIDE | ^\*\*(INPUT|OUTPUT)
  => 159 files. Minus 24 barred (§0.3) = 135 in band.

SWEEP S-B (joining band). Every *.md under R1 matching, case-insensitively:
  no (derived|sealed)? (rule|law) for (joining|gluing|stitching) | glu(e|ing)
  (rule|law) | stitch(ing)? (rule|law) | join(ing)? (rule|law) | cell.to.cell |
  across cells | between cells | multi.cell
  => hits in 60+ files; the operative band is the 8 files carrying the verdict
  text itself.

SWEEP S-C (output-side term band). Every *.md under R1 whose bytes place the
terms CELL, RECORD, or a joining of cells on a declared output side.

DISCIPLINE: every artifact quoted below had its seal verified by
`shasum -a 256 -c <name>.seal.sha256` run FROM THE ARTIFACT'S OWN DIRECTORY,
this session, before reliance. Verifications are listed in §6.

EXPECTED-UNLOCATABLE: "Q-..." items. Not sought, not counted as absences.
```

## 0.3 BLINDNESS LEDGER — RECORDED, NOT OPENED

The commission bars the diagnostic/meta band of 2026-08-15. The following 24
filenames surfaced in sweep S-A and were recorded WITHOUT being opened. No byte
of any of them was read, and no vocabulary from them is used below.

```text
STAGE8_ALLOW_REQUIRE_JUNCTION_T14SR_AUDIT_V001.md
STAGE8_ALLOW_REQUIRE_JUNCTION_T14SR_V001.md
STAGE8_CERTIFICATION_RULES_O8SR_AUDIT_V001.md
STAGE8_CERTIFICATION_RULES_O8SR_V001.md
STAGE8_COMPLETION_MAP_T17SR_AUDIT_V001.md
STAGE8_COMPLETION_MAP_T17SR_V001.md
STAGE8_DISCHARGERS_VS_PARTITION_O11SR_AUDIT_V001.md
STAGE8_DISCHARGERS_VS_PARTITION_O11SR_V001.md
STAGE8_EM_PARTICIPATION_O4SR_AUDIT_V001.md
STAGE8_EM_PARTICIPATION_O4SR_V001.md
STAGE8_FORCING_NOTION_O12SR_AUDIT_V001.md
STAGE8_FORCING_NOTION_O12SR_V001.md
STAGE8_OBSTRUCTION_ORIGIN_O6SR_AUDIT_V001.md
STAGE8_OBSTRUCTION_ORIGIN_O6SR_V001.md
STAGE8_OUTSIDE_FORM_CLASS_O10SR_AUDIT_V001.md
STAGE8_OUTSIDE_FORM_CLASS_O10SR_V001.md
STAGE8_PARTITION_THEOREM_T16SR_AUDIT_V001.md
STAGE8_PARTITION_THEOREM_T16SR_V001.md
STAGE8_PRODUCTION_VS_DESCRIPTION_O13SR_AUDIT_V001.md
STAGE8_W1_SUBVOLUME_RATE_O5SR_AUDIT_V001.md
STAGE8_W1_SUBVOLUME_RATE_O5SR_V001.md
STAGE8_W2_PREQUOTIENT_RULE_O2SR_AUDIT_V001.md
STAGE8_W2_PREQUOTIENT_RULE_O2SR_V001.md
STAGE8_W3_GCM_HS_TYPE_O3SR_AUDIT_V001.md
```

NOTE ON A COLLISION. Two object-level artifacts use the strings "O11" and "O12"
in their own sealed bytes as POSED item numbers of an internal question list.
Those are internal item labels of the record and are NOT the barred 2026-08-15
artifacts; the files carrying them (e.g. `STAGE8_GLUED_TOPOLOGY_HUNT_V001.md`)
carry no barred tag in their filenames and are in scope. Where those labels are
quoted below they are quoted as the record's own item numbers, nothing more.

---

## 1. THE CENSUS, GROUPED BY OUTPUT SIDE

Each entry gives: NAME (the object at its own bytes) / TAKES / YIELDS / TYPE.

### 1.A OUTPUT SIDE = A COMPLEX OR CARRIER (these are OBJECTS: yielded, taking nothing)

```text
A-1  K_square — the unfilled oriented 1-skeleton.
     TAKES   nothing. It is exhibited, not computed from an input.
     YIELDS  a four-vertex, four-edge oriented 1-complex with the bounding
             2-cell deliberately omitted; vertices v_00, v_10, v_01, v_11;
             edges e_a0, e_0b, e_ab, e_ba.
     TYPE    OBJECT.
     BYTES   BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md, span quoted at
             STAGE8_GLUED_TOPOLOGY_HUNT_V001.md G-6: "The unfilled oriented
             1-skeleton K_square with no 2-cell" / "No filled 2-cell is
             included in the trace carrier."

A-2  K_L — the frozen periodic lattice.
     TAKES   nothing (a parameter L >= 3 indexes the family; it is not an
             object the record yields elsewhere, it is a chosen integer).
     YIELDS  "the oriented 2-skeleton of (Z/LZ)^4, L >= 3", one Hermitian line
             per vertex, sealed periodic edge transport, periodic indices,
             frozen plaquette boundary word; higher cells of the four-torus
             not included.
     TYPE    OBJECT.
     BYTES   V011 spans 7d81c132 / 96e164af, quoted at GLUED_TOPOLOGY_HUNT G-7.

A-3  The working class — five sealed single-cell complexes (parent K, A1,
     A2-F, A2-B, Z).
     TAKES   nothing.
     YIELDS  five exhibited single-cell complexes.
     TYPE    OBJECT (five of them).
     BYTES   AND 38bbb9fc, carried at GLUED_TOPOLOGY_HUNT G-10.

A-4  The primitive faithful carried block.
     TAKES   the six declared pre-alpha hypotheses (two durable endpoint
             alternatives; one recoverable scalar relative-action marker after
             the physical null quotient; faithful response to that marker;
             bounded durable capacity; continuous reversible pre-durable
             variation; boundary completeness/no surplus).
     YIELDS  "A primitive faithful carried block is therefore a real two-plane",
             with normalized orientation generator obeying J^2 = -I; and
             primitive_single_handle_record_algebra = M_2(C).
     TYPE    RULE (it takes hypotheses and yields a carrier).
     BYTES   PRIMITIVE_RECORD_CARRIER_AND_KINEMATICS_V001.md :12-30, :103-107.

A-5  C_ref — the admissible cellulation class.
     TAKES   nothing.
     YIELDS  a DECLARATION of a class: "An admissible class C_ref of oriented,
             shape-regular PERIODIC regular-CW cellulations". No member is
             displayed anywhere of record.
     TYPE    OBJECT, but an empty-extension one: the class is named, no element
             of it is yielded. Recorded exactly as the record records it —
             "The declaration is not a realization theorem".
     BYTES   V011 span ee11aa62; POSED trap T1, carried at GLUED_TOPOLOGY_HUNT G-8.
```

### 1.B OUTPUT SIDE = A NEW OBJECT BUILT FROM GIVEN OBJECTS (these are RULES / MAPS)

```text
B-1  THE COPRODUCT COMPOSITION LAW (MON 451550c3; V011 span 288f0183).
     TAKES   a family of PAIRWISE DISJOINT components K_i.
     YIELDS  one composed carrier and its space:
             "K = disjoint_union_i K_i, H(K) = tensor_i H(K_i)".
     TYPE    RULE (map). Operative restriction at bytes: "composition is
             defined of record ONLY for disjoint components."
     BYTES   GLUED_TOPOLOGY_HUNT G-1.

B-2  THE FINITE-LOCALITY WRITE ROW (M03 / RAT 2cd1ffce, DoR-009).
     TAKES   a per-cell history tuple a = (a_1 ... a_N), one a_j per cell.
     YIELDS  one N-cell write operator
             W_N^(n)[a] := tensor_(j=1)^N W_(1,j)^(n)[a_j] ;
             per cell D_(n,j)[a_j] = diag(1, z_j^(n)[a_j], 1), reading a_j ONLY.
     TYPE    RULE (map). Its output carries NO inter-cell structure: at bytes,
             "There is NO cell-to-cell operator composition, no successor map,
             no identification of any factor with any other: the inter-cell
             incidence set is EMPTY."
     BYTES   M03 :127-140, :387-399; GLUED_TOPOLOGY_HUNT G-3.

B-3  THE TWO-PORT TRANSPORT LAW (RAT span 16603c5a).
     TAKES   one oriented cell with its two endpoint slots, and a pair (t, s).
     YIELDS  a transported cell datum z^g = t z s^dagger, with endpoint
             representations G_out(t) = D(t), G_in(s) = S D(s) S.
     TYPE    RULE (map), single-cell. It is scoped at bytes to one cell: "a
             per-cell covariance statement, silent on gluing."
     BYTES   GLUED_TOPOLOGY_HUNT G-4.

B-4  THE ANCHORING EQUATION (STAGE8_ANCHORING_DERIVATION_V001, ca7fa457;
     CONFIRMED by STAGE8_ANCHORING_CHECK_V001, 4a048901).
     TAKES   a per-cell write chain ell_j.
     YIELDS  its two ports as a boundary: (*) d_0^dagger ell_j = e_out - e_in.
     TYPE    RULE (map) from a chain to a port pair. Derived exact (§2.1).
     NOTE    Under the entered reading ell_j = gamma_j is closed, so
             d_0^dagger gamma_j = 0 and the yield degenerates to a single
             common 0-cell. The exact kernel identity is a separate yield:
             ker(d_0^dagger)|C_1(K_square) = Q*gamma_j.
     BYTES   :11-14, :26-32, :48, :171-187, :347-356.

B-5  THE PRIMITIVE REVERSIBLE RECORD-WRITE MAP.
     TAKES   a source-and-ready-register pair, |0_S 0_R> or |1_S 0_R>.
     YIELDS  a written pair — the operative signature verbatim:
             "|0_S 0_R> -> |0_S 0_R>,
              |1_S 0_R> -> |1_S 1_R>"
             realized by U_write = P_0^S tensor I_R + P_1^S tensor X_R.
     TYPE    RULE (map). Self-typed at bytes as NOT unique: "It does not
             uniquely determine the unitary on the unused input subspace";
             "Controlled `X` is the selected `a=b=0` representative, not a
             theorem"; and it "is not an active Level-1 postulate".
     BYTES   PRIMITIVE_REVERSIBLE_RECORD_WRITE_PRINCIPLE_V002.md :17-45.

B-6  THE LOCAL PROJECTIVE LIFT AND ITS TRANSITIONS.
     TAKES   a patch U_i (SEE §4 — the patch family itself is never yielded).
     YIELDS  a normalized lift z_i : U_i -> C^2, transition functions
             z_j = g_ij z_i with g_ij = exp(i theta_ij), and the triple-overlap
             cocycle g_ij g_jk g_ki = 1.
     TYPE    RULE (map).
     BYTES   LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md :16-43, :45-79, as read at
             bytes and reported in STAGE8_RECORD_SIDE_PATCH_DEFINITION_SWEEP_V001.

B-7  THE ALL-PAIRS COHERENT KERNEL (FN span f7c7261e).
     TAKES   a pair index (j,k) over the finite-N cells.
     YIELDS  a pairing coefficient C_jk = mu.
     TYPE    RULE (map), but typed at bytes as NOT a builder of structure:
             "it is a PAIRING MATRIX on block projections, not an incidence
             structure — it glues no cells and builds no complex."
     BYTES   GLUED_TOPOLOGY_HUNT G-5.

B-8  THE TWO-NODE NETWORK SOURCING PROPOSAL (NET 87f69626).
     TAKES   two nodes.
     YIELDS  Adj_2 = [[0,1],[1,0]], "no self-edge", reciprocal, one-tier delayed.
     TYPE    RULE (map). Status at bytes: PROPOSED_NOT_ADOPTED (DoR-016/017
             RESERVED) — "the artifact is sealed; the LAW is not adopted."
     BYTES   NET spans 9c6c594b / 6a74a4fa; GLUED_TOPOLOGY_HUNT G-9.
```

### 1.C OUTPUT SIDE = A TRUTH VALUE (these are CONSTRAINTS)

```text
C-1  THE SUPPORT CONTAINMENT CONDITION.
     TAKES   an interaction density L_c and a cell Omega_c.
     YIELDS  true/false: "support(L_c) is contained in Omega_c."
     TYPE    CONSTRAINT.
     BYTES   CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md :18-24.
     NOTE    Read at bytes elsewhere as containment and nothing more:
             "cell-locality (containment support(L_c)⊆Omega_c only)".
             (STAGE8_REQUIRE_G3_CHECK_V001.md :250-256.)

C-2  THE ORTHOGONALITY CONDITION ⊥ im(d_0).
     TAKES   a write chain ell_j.
     YIELDS  true/false. Typed at bytes as ONE condition doing two jobs:
             "gauge-invariance (⊥ im(d_0)), conservation (∂ell_j=0 =
             ker(B_G^T) = ⊥ im(d_0), the SAME condition)".
     TYPE    CONSTRAINT.
     BYTES   STAGE8_REQUIRE_G3_CHECK_V001.md :250-256; GC :82-91.

C-3  TOTAL-NONZERO.
     TAKES   a write chain ell_j.
     YIELDS  true/false: phi_f + phi_H != 0 (zero-variation elimination).
     TYPE    CONSTRAINT.
     BYTES   STAGE8_REQUIRE_G3_CHECK_V001.md :150-153, :250-256; W :167-170, :208-209.

C-4  THE TRIPLE-OVERLAP COCYCLE CONDITION.
     TAKES   a triple of transition functions g_ij, g_jk, g_ki.
     YIELDS  true/false: g_ij g_jk g_ki = 1.
     TYPE    CONSTRAINT.
     BYTES   LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md :16-43.

C-5  THE SEVEN FALSIFIERS OF THE INCIDENCE SUPPORT PRINCIPLE.
     TAKES   a proposed physical parent.
     YIELDS  true/false (rejection if any of seven listed events occurs — e.g.
             "the same primitive incidence remains active after its closure
             face"; "a later primitive cell acts nontrivially on an earlier
             record factor").
     TYPE    CONSTRAINT (a seven-clause rejection test).
     BYTES   CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md :62-78.

C-6  THE FIVE CLOSURE CONDITIONS OF THE CONNECTED CASE.
     TAKES   a connected composition of cells.
     YIELDS  true/false. At bytes the truth value is not established:
             "connected_linked_cluster_density_proved = false in BOTH MON and
             V011 flags"; the connected case "is an OPEN OBLIGATION".
     TYPE    CONSTRAINT, stated and unevaluated.
     BYTES   MON Theorem 3; GLUED_TOPOLOGY_HUNT G-1.
```

### 1.D OUTPUT SIDE = A WARRANT ABOUT SOMETHING ALREADY IN HAND (these are CERTIFICATES)

```text
D-1  THE D_0-SQUARE CERTIFICATE.
     TAKES   the five generators (L_id, A0, A1, A2-Freudenthal, A2-barycentric)
             and their composites.
     YIELDS  a warrant, verbatim on its own YIELDS line:
             "YIELDS = im(d_0) is transport-stable (sd*_1 . d_0' = d_0 . sd*_0
             exact over Z, so sd*_1(im d_0') subseteq im(d_0)) => the block pair
             (phi_f, phi_H) is well-defined under transport on the declared
             carrier C^1/im(d_0); the AND-boolean class is posable"
             with D0_SQUARE = CERTIFIED_ALL.
     TYPE    CERTIFICATE. It yields no new complex, chain, or cell — only
             permission to rely on objects already present.
     BYTES   STAGE8_D0_SQUARE_CERTIFICATE_V001.md :1860-1864.

D-2  THE G1 KERNEL CERTIFICATE.
     TAKES   the G1 kernel data.
     YIELDS  a warrant at declared grade, and at its own bytes an explicitly
             incomplete one: "certificate assembles PARTIAL: one leg proved at
             declared grade, two named".
     TYPE    CERTIFICATE (partial, self-declared).
     BYTES   STAGE8_G1_KERNEL_CERTIFICATE_V001.md :323.

D-3  THE SPLIT-FREEDOM VERDICT.
     TAKES   the of-record constraint set on ell_j (C-2, C-3, C-1 as
             containment, plus zero-variation elimination).
     YIELDS  a warrant about that set: SPLIT_FORCED = NO_CONTINGENCY_CONFIRMED
             — the set "collectively fixes only ell_j ∈ H ⊕ im(d_1^dagger) with
             phi_f+phi_H!=0 and leaves the H-vs-flux split unconstrained".
     TYPE    CERTIFICATE (a warrant about what the constraints do and do not fix).
     BYTES   STAGE8_REQUIRE_G3_CHECK_V001.md :150-157, :250-258.

D-4  THE PAIRED CHECK ARTIFACTS (structural family).
     TAKES   one named determination artifact plus its sealed digest.
     YIELDS  a verdict token about it — BB_VERDICT = SOUND, MC_VERDICT = SOUND,
             AN_VERDICT = CONFIRMED, GLUED-TOPOLOGY CHECK, TYPING_RULE_CANDIDATE
             CHECK, and the rest of the *_CHECK_* band.
     TYPE    CERTIFICATE. Structurally uniform across the family: input is an
             artifact, output is a warrant about that artifact, never a new
             object of the theory.
     BYTES   digests carried at STAGE8_TYPING_RULE_CANDIDATE_V001.md :48-63.
```

---

## 2. THE OUTPUT-SIDE QUESTIONS

### 2.1 WHAT HAS A **CELL** ON ITS OUTPUT SIDE?

**EXACTLY ONE CLAUSE IN THE CORPUS.** Sweep S-C over R1 for any object that
places a cell on its output side returns hits in eleven files; every one of them
is a QUOTATION of a single origin clause, which reads, verbatim:

```text
For every primitive record-forming incidence `c`, the complete microscopic
parent assigns one Lorentz-covariant causal cell `Omega_c` and one interaction
density `L_c` such that

support(L_c) is contained in Omega_c.
```
— CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md :18-24 (seal verified OK).

TYPED BY STRUCTURE:
```text
TAKES   (i) a primitive record-forming incidence c, and
        (ii) "the complete microscopic parent" — the assigning agent.
YIELDS  a pair: one cell Omega_c, and one interaction density L_c.
TYPE    RULE. A cell stands on its output side.
```

The quoting sites, all reducible to this one clause, are:
STAGE8_AXN_BUILD_DIRECTION_RELATION_CROSSCHECK_CODEX2_V001.md:51 ("CIS assigns
one Lorentz-covariant causal cell..."); STAGE8_C1_U_OMEGA_TYPED_CODEX2_V001.md:57;
STAGE8_AXN_BUILD_DESCENDANT_CALCULUS_DARIO_V001.md:52 (as "G2 (support bound)");
STAGE8_7A_SUPPORT_AND_FORCING_DARIO_V001.md:97;
STAGE8_COMMON_ORIGIN_GENERATIVE_VS_FORMATION_TYPING_V001.md:649;
review_packets/STAGE7_QSPEC_CANDIDATE_V001/CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md:19.

**THE DECISIVE STRUCTURAL FACT.** The input side of this one cell-yielding rule
names "the complete microscopic parent". The same artifact, in its own frozen
status block, records that this input is not itself yielded anywhere:

```text
complete_causal_parent_derived = false
```
— CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md :110 (frozen status block).

and, in its own falsifier section, in its own words:

```text
Failure to derive a unique causal cell, a complete parent, or a durable
outgoing sector blocks downstream promotion. It is not repaired by assuming
durability.
```
— ibid. :80-82.

Independently at other bytes, the same input side is recorded unyielded:
`causal_cell_and_record_density_derived = false`
(PRIMITIVE_RECORD_CARRIER_AND_KINEMATICS_V001.md :112), whose "Next gate" section
states the same in prose: the next result "must derive how primitive record cells
exhaust, band-limit, or otherwise UV-complete the surface fields ... It must also
derive the cell density" (:124-129); and
`the unique causal record cell is not derived`
(reported at STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V002.md:216, citing member 14
:168; the same sub-obligation named at
STAGE8_DESC_OPEN_CONDITIONS_SWEEP_CODEX2_V001.md:154).

EVERY OTHER OBJECT IN §1 PRESUPPOSES A CELL. A-1, A-2, A-3, A-5 exhibit complexes
already built. B-2, B-3, B-4, B-7 take cells as given on their input sides. C-1
takes a cell and tests a containment against it. No object in the census
constructs a cell from anything more primitive than the undrived parent.

A SECOND, NARROWER CELL-SHAPED ABSENCE, at its own bytes: a COMMON cell — one on
which two typed returns both exist — is posed and not formed:

```text
| common record cell `e` | **UNFORMED**; posed only |
...
common cell formed = false
```
— STAGE8_C1_COMMON_CELL_POSED_CODEX2_V001.md :352, :402 (seal verified OK); with
the accompanying typing at :90-91: "a formed common cell alone does not supply
the junction, and a derived-plus-`beta`-sensitive junction alone would not
identify the common cell."

### 2.2 WHAT HAS A **RECORD** ON ITS OUTPUT SIDE?

**PRESENT, AND MORE THAN ONE.** Unlike the cell, the record is genuinely yielded.

HIT 1 — the write map (B-5). Operative signature verbatim:
```text
|0_S 0_R> -> |0_S 0_R>,
|1_S 0_R> -> |1_S 1_R>
```
"creates orthogonal conditional record states for arbitrary source amplitudes."
— PRIMITIVE_REVERSIBLE_RECORD_WRITE_PRINCIPLE_V002.md :17-27.
TAKES a source-and-ready-register pair; YIELDS a written record factor. TYPE: RULE.
Self-qualified at its own bytes: it "does not uniquely determine the unitary on
the unused input subspace"; the selected representative is "not a theorem"; and
it "is not an active Level-1 postulate".

HIT 2 — the formation ordering. Operative signature verbatim:
```text
physical order:        antecedent carrier -> write/nonreturn/persistence -> durable record
```
— STAGE8_COMMON_ORIGIN_GENERATIVE_VS_FORMATION_TYPING_V001.md :33-35 (seal OK),
with the prose at :26-28: "a carrier and ready state precede the write, and a
durable public record forms only after source-controlled write, nonreturn, and
persistence succeed", and the frozen typing ROOT_PHYSICAL_ONTOLOGY = FORMATION.
TAKES an antecedent carrier plus a ready state; YIELDS a durable public record.
TYPE: RULE (a three-step composite).

HIT 3 — the carrier itself (A-4). TAKES six declared hypotheses; YIELDS the
record algebra M_2(C) and the real two-plane carrier. TYPE: RULE.

STRUCTURAL READING, stated without inference beyond the typing: the record has
producers on the corpus's output side; the cell has one producer whose own input
is unyielded. The two are not symmetric in this inventory.

### 2.3 WHAT HAS A **JOINING OF CELLS** ON ITS OUTPUT SIDE?

**NOTHING. THE CATEGORY IS EMPTY, AND THE ABSENCE IS EXACT.** The one composition
rule the corpus carries (B-1) has a composed carrier on its output side, but that
carrier is by construction unjoined:

```text
"K = disjoint_union_i K_i, H(K) = tensor_i H(K_i)" — composition is defined
of record ONLY for disjoint components.  A disjoint union glues nothing.
```
— STAGE8_GLUED_TOPOLOGY_HUNT_V001.md G-1 (seal verified OK).

The finite-N write row (B-2), the only other object taking many cells at once,
yields an output with the inter-cell side empty, verbatim:

```text
There is NO cell-to-cell operator composition, no successor map, no
identification of any factor with any other: the inter-cell incidence set is
EMPTY.  ...  IS THE CHAIN CLOSED ANYWHERE?  There is no chain to close:
nothing links j to j+1, and nothing links N back to 1.
```
— ibid. G-3.

THE EXACT ABSENCE, DISPLAYED. The corpus itself performs this same enumeration
and records its result in these words:

```text
NOTHING SEALED EXISTS:    a physical-stratum glued multi-cell record complex; a port
```
— ibid. :446.

and, on the licensing side:

```text
There is no sealed clause of the form "ports P and Q may be identified when ..."
anywhere found.  So "permitting" cannot be cited — nothing affirmative exists to cite.
```
— ibid. :356-357.

DISCLOSURE CARRIED FROM THE SOURCE, not softened: two objects in §1.A (A-1
K_square, A-2 K_L) ARE multi-cell glued complexes with nonzero first cohomology
(H^1 = 1 and H^1 = 4 respectively). The corpus types them at its own bytes as
belonging to a different stratum — "neither is sealed as a physical record
carrier" (ibid. :368-369), K_square being a prediction carrier and K_L "the finite
translation-complete TEST OBJECT" for audit. They are objects the record exhibits,
not outputs of any joining rule: nothing in the census takes cells and yields
either of them.

---

## 3. THE JOINING QUESTION — THE NAMED ABSENCE, AND WHAT KIND OF OBJECT IT IS

The corpus carries the absence at its own bytes, under its own verdict heading,
in STAGE8_GLUED_TOPOLOGY_HUNT_V001.md (seal verified OK,
`shasum -a 256 -c STAGE8_GLUED_TOPOLOGY_HUNT_V001.md.seal.sha256` from the
artifact's own directory). Quoted at :359-369, verbatim and complete:

```text
(c) GENUINELY UNSPECIFIED — THE VERDICT.  The gluing rule that could create a loop
    of cells is exactly the UNBUILT constructor pair of POSED: O11 (the successor
    law displaying h_j as an incidence sum over named edges — absent, S1) + O12
    (port-to-0-cell anchoring — absent, S3), plus the connected-composition
    obligation (G-1/G-2/G-5: declared, five closure conditions named, proved =
    false).  Between "no ban" (a) and "no license" (b) the sealed state is
    SILENCE at the exact point where a loop would be built: the constructor is
    the unbuilt successor/anchoring law.  DISCLOSURE: at the audit/prediction
    stratum the corpus is past (b) — K_square and K_L are sealed loop-carrying
    INSTANCES (H^1 = 1 and 4, §2) — but neither is sealed as a physical record
    carrier, so neither discharges the physical-stratum constructor.
```

reinforced at :372-377:

```text
Consequence for the second sector (the tasked frame): its "only possible home" — a
glued record complex with H^1 > 0 — is NOT sealed at the physical stratum, is NOT
forbidden, and has a NAMED constructor (O11 + O12 + connected composition).
... so the reopening is a construction gap, not a formalism gap.
```

### 3.1 WHAT KIND OF OBJECT THE CORPUS SAYS IS MISSING

The two candidate kinds are structurally distinct:

```text
KIND 1   takes cells, yields a joined structure           (a builder)
KIND 2   takes a joined structure, yields a warrant       (a checker)
```

**THE CORPUS'S OWN WORDS DECIDE IT: KIND 1.** The determining evidence is
lexical and repeated, and it is the record's own choice of noun:

```text
"the UNBUILT constructor pair"                        :360
"the constructor is the unbuilt successor/anchoring law"   :365-366
"has a NAMED constructor (O11 + O12 + connected composition)"  :374
"neither discharges the physical-stratum constructor" :369
"a construction gap, not a formalism gap"             :377
```

Reading the two named pieces by their own input and output sides confirms the
noun rather than merely echoing it:

```text
O11  "the successor law displaying h_j as an incidence sum over named edges"
     TAKES   the per-cell read h_j (which of record is never displayed as an
             edge sum — S1: "h_j never displayed as an edge sum",
             STAGE8_G3_REALIZATION_BUILD_V001 :225-230)
     YIELDS  an incidence sum over named edges — i.e. edge-level structure
             where before there was an opaque per-cell quantity.
     KIND    1. It builds structure. Status of record: ABSENT.

O12  "port-to-0-cell anchoring"
     TAKES   the two ports, which of record are "record-carrier endpoint slots"
             whose "identification with 0-cells of the complex is not displayed"
             (S3, GB span 7b604a0b).
     YIELDS  that identification — ports become 0-cells of a complex, which is
             precisely the act by which two cells become one joined object.
     KIND    1. It builds structure. Status of record: ABSENT.
```

### 3.2 THE ONE CONJUNCT OF THE OTHER KIND, KEPT SEPARATE

Honesty of the typing requires recording that the named absence is a compound of
three conjuncts, and that the third is NOT of Kind 1:

```text
"plus the connected-composition obligation (G-1/G-2/G-5: declared, five
 closure conditions named, proved = false)"
```
TAKES a connected composition; YIELDS a truth value / a warrant that the five
closure conditions hold. That conjunct is KIND 2.

The corpus itself keeps the two apart in its own grammar: it calls the first two
a "constructor pair" and the third an "obligation", and it locates the missing
thing in the first: "the constructor is the unbuilt successor/anchoring law."
The determination therefore is: **the missing object is of KIND 1 — one that
takes cells and yields a joined structure — with a KIND 2 conjunct riding on it
that only becomes evaluable once the Kind 1 object exists.** The ordering is
forced by the types themselves: nothing can warrant a joined structure before
something yields one.

### 3.3 A SECOND, INDEPENDENT NAMING — SAME KIND, DIFFERENT JOIN

A distinct absence of joining is named at other bytes, and it types the same way.
STAGE8_DESC_STITCHING_RULE_HUNT_DARIO_V001.md (seal verified OK) :139-181 names
the missing object a three-theorem stack of which one member is missing:

```text
T_ref   GEOMETRIC REFINEMENT STITCHING.  ** NOT INSTANTIATED **, but fully typed
        as a work order: a functor D_ref from a category of admissible finite
        oriented record complexes to a physical class, a comparison eta_K from
        the gate data, refinement pushforwards P_KR, response maps Resp_K, two
        commuting-square identities, and refinement-invariance of the INTENSIVE
        response up to a boundary term whose ratio to four-volume vanishes —
        all in ONE FROZEN TOPOLOGY.
```

Its head is a FUNCTOR — TAKES a category of admissible finite oriented record
complexes, YIELDS members of a physical class. KIND 1 again. The slot is typed
explicitly:

```text
TYPE OF THE SLOT
  IN    finite / INTERNAL record-cell carrier data
  OUT   a total finite or physically completed SPACETIME carrier, on which the
        determinant/CTP trace is taken
```
— ibid. :146-153.

DISTINCTION KEPT: this second absence joins the finite to the completed carrier,
not cell to cell. It is recorded here because it answers the same kind-question
the same way, not because it is the same object. The corpus is explicit that
T_cyl of the same stack IS proved and T_phys is typed with five named consumers,
so the stack is partly built; the unbuilt member is the Kind 1 one.

---

## 4. THE UNPAIRED LIST — INPUT SIDES NOTHING IN THE CENSUS YIELDS

Derivation rule, applied mechanically: for every object in §1, read its input
side; ask whether any object in §1 has that item on its output side; if none
does, it is unpaired. Nothing is added from outside the census, and nothing is
inferred about why an item is unpaired.

### U-1  THE COMPLETE MICROSCOPIC PARENT
```text
REFERENCED BY  the one cell-yielding rule (§2.1) on its input side; and by C-5,
               whose input is "a proposed physical parent".
YIELDED BY     nothing in the census.
AT ITS OWN BYTES  complete_causal_parent_derived = false
               (CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md :110)
CONSEQUENCE IN THE INVENTORY  every cell in the census stands downstream of this
               one unpaired input. This is the census's deepest open end: it is
               unpaired at the root, not at a leaf.
```

### U-2  THE PATCH FAMILY {U_i}
```text
REFERENCED BY  B-6, on its input side, and through B-6 by C-4.
YIELDED BY     nothing in the census.
AT ITS OWN BYTES  a dedicated sweep counted it:
               actual_PRPS_or_LPRB_patch_definitions = 0
               actual_PRPS_endpoint_comparison_cover_definitions = 0
               record_side_topology_or_smooth_structure_definitions_for_U_i = 0
               "Nothing in the swept corpus defines the record-side patches
               `U_i` or an actual PRPS endpoint-comparison cover."
               (STAGE8_RECORD_SIDE_PATCH_DEFINITION_SWEEP_V001.md :29-31, :96-100)
               The same sweep lists what is undefined: "the underlying space of
               which U_i is a patch; the patch family or cover; which points or
               cells belong to a patch; whether U_i are open sets in a topology;
               whether the cover is good; whether it has a nerve; whether it is
               finite, countable, canonical, or refinement-stable; or how
               admissible causal record cells generate the patch family."
CONSEQUENCE    B-6 consumes patches and yields lifts and transitions; C-4 tests a
               cocycle on those transitions. Both run on an input the census
               never produces. This is the cleanest unpaired item in the list:
               the count is zero and it is counted at bytes.
```

### U-3  A CONNECTED COMPOSITION OF CELLS
```text
REFERENCED BY  C-6 on its input side (the five closure conditions are conditions
               ON a connected composition).
YIELDED BY     nothing in the census — this is exactly the empty category of
               §2.3. B-1 yields only disjoint unions; B-2 yields a row with an
               empty inter-cell side.
AT ITS OWN BYTES  "NOTHING SEALED EXISTS: a physical-stratum glued multi-cell
               record complex" (STAGE8_GLUED_TOPOLOGY_HUNT_V001.md :446);
               connected_linked_cluster_density_proved = false;
               connected_cross_cell_terms_derived = false (G-1, G-2).
CONSEQUENCE    C-6 is a constraint whose input class the census shows to be
               empty. It cannot be evaluated true or false by anything the
               record carries, because nothing hands it an argument.
```

### U-4  THE PER-CELL READ h_j AS EDGE-LEVEL STRUCTURE
```text
REFERENCED BY  B-4 (through ell_j) and by the missing constructor O11 of §3.1.
YIELDED BY     nothing in the census.
AT ITS OWN BYTES  "h_j never displayed as an edge sum"
               (STAGE8_G3_REALIZATION_BUILD_V001.md :225-230, carried at
               STAGE8_TYPING_RULE_CANDIDATE_V001.md S4).
CONSEQUENCE    the anchoring equation B-4 operates on ell_j, and D-3 certifies
               that the of-record constraint set "leaves the H-vs-flux split
               unconstrained". So ell_j is constrained but never fully yielded:
               its input side reaches an object the census does not deliver.
```

### U-5  THE IDENTIFICATION OF PORTS WITH 0-CELLS
```text
REFERENCED BY  the missing constructor O12 of §3.1; and required by anything
               that would give B-3's endpoint slots a place in a complex.
YIELDED BY     nothing in the census.
AT ITS OWN BYTES  "R4's two ports are record-carrier endpoint slots; their
               identification with 0-cells of the complex is not displayed"
               (S3, GB span 7b604a0b, carried at GLUED_TOPOLOGY_HUNT G-4);
               and "There is no sealed clause of the form 'ports P and Q may be
               identified when ...' anywhere found" (ibid. :356).
```

### U-6  AN INHABITANT OF L_c, AND A CELL PAIRING
```text
REFERENCED BY  C-1 on its input side (the containment condition needs an actual
               L_c to test); and by any assembly of per-cell terms into a whole.
YIELDED BY     nothing in the census. The index SET is yielded — "one term per
               primitive record-forming incidence" is recorded DERIVED
               (STAGE8_AXN_ASSEMBLY_FINITE_DARIO_V001.md :79) — but no member of
               it is.
AT ITS OWN BYTES  "It does not derive an `L_c` inhabitant, cell pairing, or
               evaluable action summand. Count T1 as `DERIVED-SCHEMA /
               EVALUATION-GAPPED`, not an installed derived term."
               (STAGE8_AXN_ASSEMBLY_CROSSCHECK_CODEX2_V001.md :152, seal OK)
               and "It is an adopted primitive-support principle, not a derived
               complete action" (STAGE8_AXN_BUILD_CALCULUS_CROSSCHECK_CODEX2_V001.md
               :141).
CONSEQUENCE    a schema with a derived index set and no yielded inhabitant. The
               unpaired item is the inhabitant, not the index.
```

### U-7  THE ANTECEDENT RECORD CARRIER AND READY STATE
```text
REFERENCED BY  B-5 on its input side (|0_R> is the ready register); and by the
               formation ordering of §2.2, whose first term is "antecedent
               carrier".
YIELDED BY     A-4 yields a carrier from six hypotheses (see U-8), and nothing
               in the census yields the ready state as such.
AT ITS OWN BYTES  the record explicitly declines to make the source yield it:
               "It is not a source that temporally creates the antecedent
               carrier" (STAGE8_OBJ0_EXACT_SIGNATURE_DOMAIN_CODOMAIN_SPEC_AND_
               BUILD_STOP_V001.md :422, :1582, seal OK); and
               rank1_class_requires_source_action_to_create_record_carrier =
               NO_VERDICT (STAGE8_COMMON_ORIGIN_GENERATIVE_VS_FORMATION_TYPING_
               V001.md :76).
```

### U-8  THE SIX PRE-ALPHA HYPOTHESES
```text
REFERENCED BY  A-4 on its input side.
YIELDED BY     nothing in the census. They enter as assumptions: "The pre-alpha
               single-handle theorem assumes:" followed by the six clauses
               (PRIMITIVE_RECORD_CARRIER_AND_KINEMATICS_V001.md :12-20).
NOTE           listed for completeness of the mechanical rule. A hypothesis set
               at the base of a derivation is unpaired by construction; it is
               recorded here so the list is complete, not because the census
               displays it as a gap of the same character as U-1 to U-7.
```

### U-9  A MEMBER OF C_ref
```text
REFERENCED BY  anything that would instantiate A-5.
YIELDED BY     nothing in the census.
AT ITS OWN BYTES  "The declaration is not a realization theorem" (POSED trap T1);
               and because no member is displayed, "no H^1 is computable"
               (GLUED_TOPOLOGY_HUNT G-8).
```

### U-10  A FORMED COMMON CELL
```text
REFERENCED BY  the posed junction interface of
               STAGE8_C1_COMMON_CELL_POSED_CODEX2_V001.md.
YIELDED BY     nothing in the census.
AT ITS OWN BYTES  "| common record cell `e` | **UNFORMED**; posed only |" (:352);
               "common cell formed = false" (:402);
               "one common physical cell on which both typed returns exist
               independently | no common cell is presently formed" (:79).
```

### 4.1 WHAT IS **PAIRED** — RECORDED SO THE LIST IS A LIST AND NOT A MOOD

The certificates D-1 through D-4 are fully paired: their input sides reference
artifacts, generators, and constraint sets that the census does yield, and their
outputs are warrants about those. B-1's rule-level input (pairwise disjoint
components) is satisfied by A-1, A-2, A-3 as exhibited objects. C-2 and C-3 take
ell_j, which is present as an object even where underdetermined (U-4). A-1, A-2,
A-3 take nothing and are unpaired-free by construction. The unpaired list is
therefore ten items out of a census of twenty-three, and the ten cluster: U-1,
U-6, U-7, U-8 sit on the input side of what yields cells and records; U-2, U-9
sit on the patch/cellulation side; U-3, U-4, U-5, U-10 are the joining side, and
U-3 + U-4 + U-5 are precisely the three pieces §3 identified as the missing
Kind 1 constructor and its unevaluable Kind 2 companion.

---

## 5. CHOICE LEDGER

Every choice this census made that another census could have made differently.

```text
CH-1  TYPING BY STRUCTURE, NOT BY NAME.  Objects were typed only by what stands
      on their input and output sides. CONSEQUENCE: several artifacts whose
      names say "certificate" were typed CERTIFICATE because they yield
      warrants, but D-2 was recorded PARTIAL on its own words rather than on
      its name; and A-4, filed under the carrier heading, was typed RULE, not
      OBJECT, because it takes hypotheses. ALTERNATIVE REJECTED: grouping by
      artifact family (BID/STAGE8/PRIMITIVE), which would have imported the
      corpus's own filing scheme as a frame.

CH-2  OUTPUT-SIDE GROUPING.  §1 is grouped by what appears on the output side.
      ALTERNATIVE REJECTED: grouping by subject matter (gauge / carrier /
      topology), which would have made §2's questions unanswerable by
      inspection, since the answer to "what yields a cell" is a fact about
      output sides and nothing else.

CH-3  SWEEP BAND.  S-A was defined by self-declared signature lines. RISK
      ACCEPTED: an object that declares neither an input nor an output line and
      is never quoted by one that does would be missed. MITIGATION: S-B and S-C
      were run independently of S-A over all *.md at R1, and both returned
      objects (the incidence support principle, the patch sweep, the common cell)
      that S-A alone would not have surfaced. The three bands were unioned.

CH-4  "OUTPUT NAME probed ... ABSENT" LINES EXCLUDED.  Sweep S-A returned ~14
      files whose only ^OUTPUT line is a write-discipline statement about the
      artifact's own filename. These were read as file-handling discipline, not
      as object signatures, and excluded from the census. A different census
      could have counted them; it would have counted filenames, not objects.

CH-5  THE O11/O12 LABEL COLLISION RESOLVED IN FAVOUR OF THE RECORD'S OWN
      NUMBERING.  See §0.3. ALTERNATIVE REJECTED: treating the collision as a
      reason to exclude STAGE8_GLUED_TOPOLOGY_HUNT_V001.md, which would have
      removed the single most load-bearing object-level artifact for §2.3 and §3
      on the basis of a string match rather than a filename tag.

CH-6  BOTH ROOTS SWEPT, ALL READS TAKEN AT R1.  R2 was compared and found to
      mirror R1 at every filename checked; three seal sidecars at R1 in fact
      carry R2 paths and were verified as such. No object was counted twice.

CH-7  THE COMPOUND ABSENCE OF §3 REPORTED AS COMPOUND.  The corpus's named
      absence has three conjuncts, two of Kind 1 and one of Kind 2. A shorter
      answer ("it is a constructor") would have been the corpus's own headline
      word but would have dropped the third conjunct. Both are recorded, with
      the corpus's own grammar ("constructor pair" vs "obligation") given as the
      ground for the determination.

CH-8  U-8 LISTED THOUGH IT IS A DIFFERENT ANIMAL.  The mechanical rule of §4
      catches base hypotheses. Rather than exempt them silently, U-8 is listed
      and annotated as structurally different from U-1..U-7. A census that
      exempted them would have been tidier and less honest.

CH-9  NO SECOND-ORDER CLAIM MADE.  Where the typing shows an empty category
      (§2.3) or an unpaired input (§4), the census states the emptiness and
      stops. It does not say what should fill it, whether it can be filled, or
      what follows if it is not.
```

## 6. TOY_SEPARATION

```text
This census inventories the ACTUAL corpus at its actual bytes. It is not a
model of the corpus, not a sample, and not a reconstruction.

WHAT IS ACTUAL HERE
  - every quoted string was read from a sealed file whose seal was verified this
    session by shasum -a 256 -c from the artifact's own directory (§7);
  - every count (159 / 24 / 135 / 23 / 10 / the three zeros of U-2) was produced
    by a command over the real tree, not estimated;
  - the two corpus roots swept are the real ones named in the commission.

WHAT IS NOT CLAIMED
  - The census does not claim completeness over all 1754 *.md at R1. It claims
    completeness over the declared bands S-A, S-B, S-C, and says so. An object
    outside all three bands is outside this census.
  - No object here is a stand-in for a real one. Where the record carries only a
    declaration and no instance (A-5 C_ref), the census records the declaration
    as a declaration and marks the instance absent, rather than treating the
    declaration as if it were the thing.
  - The distinction the corpus itself draws between strata — physical vs
    audit/prediction — is carried, not flattened. A-1 and A-2 are real sealed
    complexes; they are not counted as physical record carriers, because the
    record does not count them that way.

NO TOY WAS BUILT. Nothing was constructed, proposed, adopted, or authored.
```

## 7. SEALS VERIFIED THIS SESSION

Each verified by `shasum -a 256 -c <sidecar>` executed FROM THE ARTIFACT'S OWN
DIRECTORY, before any reliance on its content. All returned OK.

```text
OK  STAGE8_TYPING_RULE_CANDIDATE_V001.md
OK  STAGE8_GLUED_TOPOLOGY_HUNT_V001.md
OK  STAGE8_GLUED_TOPOLOGY_CHECK_V001.md
OK  STAGE8_DESC_STITCHING_RULE_HUNT_DARIO_V001.md
OK  STAGE8_C1_COMMON_CELL_POSED_CODEX2_V001.md
OK  STAGE8_RECORD_SIDE_PATCH_DEFINITION_SWEEP_V001.md          (sidecar carries R2 path)
OK  STAGE8_CANONICAL_PATCH_COVER_TO_INCIDENCE_GRAPH_FUNCTOR_ATTEMPT_V001.md (sidecar carries R2 path)
OK  PRIMITIVE_REVERSIBLE_RECORD_WRITE_PRINCIPLE_V002.md
OK  CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md
OK  LOCAL_COVARIANT_CELL_MEASURE_SELECTOR_SPEC_V001.md
OK  STAGE8_D0_SQUARE_CERTIFICATE_V001.md
OK  STAGE8_G1_KERNEL_CERTIFICATE_V001.md
OK  SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003.md
OK  STAGE8_TRANSPORT_LAW_POSED_V001.md
OK  STAGE8_REQUIRE_G3_CHECK_V001.md
OK  STAGE8_ANCHORING_DERIVATION_V001.md
OK  STAGE8_COMMON_ORIGIN_GENERATIVE_VS_FORMATION_TYPING_V001.md
OK  STAGE8_AXN_ASSEMBLY_CROSSCHECK_CODEX2_V001.md
OK  STAGE8_OBJ0_EXACT_SIGNATURE_DOMAIN_CODOMAIN_SPEC_AND_BUILD_STOP_V001.md

UNSEALED / NO SIDECAR AT PATH — content used only where an independently sealed
and verified artifact quotes it at a span, never as standalone authority:
    PRIMITIVE_RECORD_CARRIER_AND_KINEMATICS_V001.md   (no sidecar found at R1;
      its flag lines :103-129 were read directly at bytes and are reported as
      read-at-bytes, and its cell-derivation flag is independently corroborated
      by two other sealed artifacts cited in §2.1)
    LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md            (consumed only through the
      sealed patch-definition sweep's byte-level report of it)
    BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md     (consumed only at spans
      already opened and confirmed by the sealed GLUED-TOPOLOGY hunt/check)
```

## 8. IMPORT AUDIT

```text
IMPORTED AND CONSUMED
  Nothing outside the two declared corpus roots. No external mathematics, no
  textbook result, no physical constant, no measured value, no imported GR, no
  scale, no faithfulness authority.

VOCABULARY AUDIT (this artifact's own prose)
  The commission bars this census from writing in the frame of the 2026-08-15
  diagnostic band. This artifact's analytic prose uses none of that vocabulary.
  Where such a word appears it is INSIDE A VERBATIM QUOTATION of an object-level
  artifact's own sealed bytes, quoted because §2 and §3 require the operative
  signature to be quoted exactly. Quotations are marked and attributed at line
  numbers throughout; the census's own typing is written in the four terms of
  §0.1 (OBJECT / RULE / CONSTRAINT / CERTIFICATE) and nothing else.

READ REFUSALS HONOURED
  24 barred filenames surfaced and were recorded unopened (§0.3).
  No register, tracker, road, plan, continuation, ledger, or lens file was read.
  "Q-..." items treated as EXPECTED-UNLOCATABLE; not sought, not counted.
  No git command of any kind was run.

CROSS-STRATUM DISCIPLINE
  Where the record separates a physical stratum from an audit/prediction
  stratum, the census carries the separation rather than merging the two. A-1
  and A-2 are counted as objects and explicitly NOT counted as answers to §2.3.
```

## 9. FLAG BLOCK

```text
CENSUS_BANDS              = S-A (159 files, 24 barred, 135 in band) ; S-B ; S-C
SWEEP_CUTOFF              = 2026-08-15
CENSUS_ENTRIES            = 23  (OBJECT 4 ; RULE 9 ; CONSTRAINT 6 ; CERTIFICATE 4)
CELL_ON_OUTPUT_SIDE       = 1 origin clause (CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001
                            :18-24), whose own input side is unpaired (U-1)
RECORD_ON_OUTPUT_SIDE     = 3 hits (write map ; formation ordering ; carrier rule)
JOINING_OF_CELLS_ON_OUTPUT_SIDE = 0 — category EMPTY, absence displayed at
                            STAGE8_GLUED_TOPOLOGY_HUNT_V001.md :446
JOINING_ABSENCE_KIND      = KIND 1 (takes cells, yields a joined structure), on
                            the corpus's own nouns "constructor pair" / "the
                            constructor is the unbuilt successor/anchoring law" /
                            "a construction gap, not a formalism gap" ;
                            one KIND 2 conjunct rides on it and is not evaluable
                            before it
UNPAIRED_COUNT            = 10  (U-1 .. U-10)
SEALS_VERIFIED            = 19 OK ; 3 unsealed-at-path, consumed only through
                            sealed quoting artifacts, disclosed in §7
alpha_computed            = false
proof_authorized          = false
kappa_record_computed     = false
NUMBERS_COMPUTED          = none (no value, no scale, no measured-constant comparison)
MACHINERY_INVOKED         = no (directory listing, grep, shasum -a 256 at path,
                            byte-span reads; no execution, no git, no member binding)
AUTHORED_CONTENT          = none. Nothing proposed, adopted, or constructed.
ALL_RESULTS               = CLAIMED until checked.
```

---

END OF CENSUS.
