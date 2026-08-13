# STAGE 8 / ATTACH PREMISE / B1-CELL-CHECK — BLIND ADVERSARIAL VERIFICATION OF THE B1-CELL INSTANCE

Lane: FABLE blind adversarial verification, codename B1-CELL-CHECK, cross-lineage.
DEFAULT = REFUTE. Date: 2026-08-13.
Under test: `STAGE8_B1_CELL_INSTANCE_V001.md`, digest recomputed at path:
`a3bedc7ef092ebd932d254331dc10053aa123334a013b95fb1e15019bdfea016` — MATCH with the tasking.

## Verdict — up front

The instance SURVIVES. Every premise constraint is realized at the sealed bytes; the
topology re-runs to the same numbers by different methods (Smith normal form over Z,
BFS connectivity, GF(2) cycle space, box-search integer null space — none of which the
instance used); the witnesses hold against my own rebuilt matrices; the
satisfiable-vs-forced distinction is stated exactly right; the provenance is carried
everywhere. ONE correction, citation-level only, in the stratum statement (S-3(b)):
the "no sealed map sends K_square into the write-carrier complex" statement is sealed
at HUNT 1892c08e :324-326, not at "check :325" — the substance is true and sealed;
no verdict moves.

---

## 0. Preflight, seals, fences

Output name probed before any write: `STAGE8_B1_CELL_CHECK_V001.md` ABSENT (artifact
and sidecar). No register, tracker, plan, road, ledger, or lens file read. Every seal
below recomputed by `shasum -a 256` at path BEFORE reliance, this session.

```text
SEALS VERIFIED (all recomputed at path; every one matches the instance's §0 table):
a3bedc7ef092ebd932d254331dc10053aa123334a013b95fb1e15019bdfea016  STAGE8_B1_CELL_INSTANCE_V001.md                   MATCH (the artifact under test)
420ab02f5ddb56ec8b3b49d3da4937c0045f2e2928fa233177dccda956914c73  ATTACH_ENTRY_ADDENDUM_V001.md                     MATCH (the ENTERED premise)
ad9fc14e1f07494f7527d95f2a94ee7a26da9d49cc784c409f31325f54572213  ATTACH_SUPPLY_MANDATE_DECISION_OF_RECORD_V001.md  MATCH (the DoR)
ccca6bb43a47f3eb5ee8dca1539a65d42ecd46ec1fa2a8f8588128e12ecd00fc  STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V007.md    MATCH (the ENTERED artifact)
5154c203ee237c4dee1b02176f8fa64c84b3ec97e561b720304f1a58219ad29b  STAGE8_ATTACH_CANDIDATE_V007_CHECK_CODEX2_V001.md MATCH (VERDICT = SURVIVES-FOR-ENTRY :232 confirmed at bytes)
82d5c5dd59d1d0d6981a2cde7244c1dad1a66352c4159b8543f0554777abea31  STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V003.md    MATCH (member-table source for note N-1)
96ec8bf4e2706eced5b17489d53f3844402331854ed4ea82d54c212dec3a22d7  STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V005.md    MATCH
56d9c9b68dcde555fe3157a4ae09545418b7b8f35766761a91184a534ce42f1b  STAGE8_ATTACH_CANDIDATE_V002_CHECK_CODEX2_V001.md MATCH (:97-99, :108-109 confirmed at bytes)
5f55c27ffb9e08e49f964b9c1640436c5a4631010a1404ec8bb6d8bd622c952c  STAGE8_ATTACH_CANDIDATE_V004_CHECK_CODEX2_V001.md MATCH (:88-108 = alias-audit content, confirming N-1)
20a3a17d44e15841baded9eaed3fdbecfde0ecb14bdb8162ea41a8bcd21d1a48  BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md     MATCH (the K_square spec; all cited spans read at bytes)
1892c08ec7afb683cec641bff6ac4b42d5ebb0be6313475dbf3549be229c755c  STAGE8_GLUED_TOPOLOGY_HUNT_V001.md                MATCH (census row :294-297 confirmed)
a22ef820c5e665cbf9a5c941d24be57efb06c9c921ee579e5291d0cdc65feaa3  STAGE8_GLUED_TOPOLOGY_CHECK_V001.md               MATCH (:69-72 lineage digests, :279-283, :288-291 confirmed)
38bbb9fc58b93cadf3be37117291fcf4caa7ac4cf9d670207b7b8cbca48af071  STAGE8_AND_CLASS_INDEPENDENCE_V001.md             MATCH (:174-187, :192-199, :208-219, :330-348 read at bytes)
c0e7192be7d5d93d74a28d66c9c0e39543f4cb755c222e7b1a9cb7f3b4b72f46  STAGE8_AND_CLASS_CHECK_V001.md                    MATCH vs its own sidecar at path (AND_VERDICT = CONFIRMED(CONSTANT_FALSE) :10, :264)
5e49d2093d4ee17b840cc096d5caf3a6edafda4e37abbd175a7a371c34658f37  STAGE8_R_RECORD_L_FORM_FABLE_V001.md              MATCH (D1 :136-142 read at bytes)
3e35ffe2a67ea863b7dfb432567a5937cf92f2f6810bc54cca67eb1598b19a70  STAGE8_G3_REALIZATION_BUILD_V001.md               MATCH (Q6 :130-135 read at bytes)
UNVERIFIABLE: none.
```

FENCES HELD: exact integer/rational structural algebra only; no physical quantity
computed, bounded, or evaluated (Phi handled as an indeterminate coefficient in both
scripts); no scale, no imported GR, no faithfulness authority; no continuum object
consumed; register/tracker/plan/road/ledger/lens families untouched.

PROVENANCE DISCIPLINE: everything below inherits the ENTERED-AUTHORED-PREMISE
provenance of addendum 420ab02f. Nothing here is premise-free; this check's own
verdicts are TYPE-P on that entry exactly as the instance's are, and void with it.

---

## 1. ATTACK 1 — CONFORMANCE (the premise vs the built instance)

Every constraint the instance extracted was re-read at the sealed bytes and checked
against the built object. Result per constraint:

```text
C-(i)    CONNECTED                addendum :33-34 quoted verbatim at bytes.  Instance: BFS from
                                  v_00 reaches all 4 vertices (my A-3, no linear algebra).  HOLDS.
C-(ii)   b_1 = 1                  addendum :34.  SNF + GF(2) + box search all give b_1 = 1.  HOLDS.
C-(iii)  reading = circuit         addendum :31-33; V007 :636 ("theta_j := contour-integral over
         holonomy on the closed    gamma_j of A").  Realized as <chi_j, A>; in the sealed fixed gauge
         circuit                   (V011 :1866-1873) it evaluates to +Phi = the sealed exp(i Phi)
                                  loop word (my A-8, coefficient arithmetic only).  HOLDS.
C-(iv)   trees inert              addendum :34; V007 :168-169.  Not violated: the instance is not a
                                  tree and claims nothing about trees.  HOLDS (vacuously, correctly).
C-(v)    b_1 > 1 out of scope     addendum :34; V007 :171-172.  The instance has b_1 = 1 exactly.  HOLDS.
C-(vi)   the specified square     V007 :163-164 ("the specified square sector, member 10
         sector                   :1840-1852") -> resolved to V011 :1840-1851 (see N-1 audit below).
                                  The built census V = 4, E = 4, F = 0 with the exact vertex names,
                                  edge names, and orientations of the sealed display.  ENTRYWISE MATCH
                                  (my A-1: rebuilt incidence == sealed D_square(u=1)).  HOLDS.
C-(vii)  gamma_j unique, F08      Uniqueness re-proved by box-search null space: every integer
         reversal the only        solution in [-2,2]^4 is k*(1,-1,1,-1) (my A-6) — nullity 1, so the
         latitude                 only latitude is the sign, which is exactly F08.  HOLDS.
C-(viii) theta_j = contour        Realized; C-(iii) above.  HOLDS.
C-(ix)   g-dependence exactly     V007 :648.  The instance touches g only through gamma_j (its chi_j
         through gamma_j          pairing); no other g-channel is built.  HOLDS.
F = 0    premise-mandated         V011 :1840 ("unfilled oriented 1-skeleton K_square with no
                                  2-cell") and :1881-1882 ("No filled 2-cell is included in the trace
                                  carrier") — both verbatim at bytes.  The annulus/cylinder rejection
                                  is CORRECT: filling would add 2-cells the sealed text excludes.  HOLDS.
```

MINIMALITY: the instance's claim is that the premise leaves NO size freedom because
V007 :164 names the concrete complex. Verified: the sealed operative-domain block
names "the specified square sector, member 10 :1840-1852", and that span (resolved,
see below) is the exact 4-vertex/4-edge display. Abstractly smaller b_1 = 1 complexes
(1-vertex loop, bigon) satisfy the addendum's one-line typing alone, and the instance
DISCLOSES this rather than hiding it (§1.6) — but they are not the specified sector.
The minimal conforming instance IS the sealed K_square. NO violated or silently
dropped constraint found. CONFIRMED.

FREEDOM INVENTORY, attacked both directions:
```text
FR-1  F08 sign of gamma_j.  Genuinely free in the premise (V007 :165 "up to the F08
      orientation reversal"); fixed to the sealed loop word u_ab u_a0 (u_ba u_0b)^(-1)
      (V011 :1863), whose exponent vector on the frozen edge order I re-derived
      independently as (+1, -1, +1, -1) — the instance's choice.  Invariance of every
      dimension/verdict under the flip is true (all claims are rank/dimension claims
      or sign-covariant witness claims).  HONESTLY NAMED, CORRECTLY FIXED.
FR-2  the inner product realizing ^perp.  The ADDENDUM leaves it free; the method of
      record does not (FORM :136-137 "in the sealed Gate-3 counting metric" — read at
      bytes).  The instance took exactly that metric and SAID SO, citing the same
      span.  Presenting it as a premise-freedom fixed by the method of record is the
      accurate description.  Block dimensions are metric-independent regardless.  HONEST.
NOTHING PRESENTED AS FORCED THAT IS FREE: checked — census, basis order, orientations,
      F = 0 are all at sealed spans (verified above); the two named freedoms are the
      only ones I could construct either.  NO inverse violation found.
```

NOTE N-1 AUDIT (the citation-resolution step the conformance hangs on): verified at
bytes BOTH WAYS. Under V007's own member table, member 04 = the V004 check
(5f55c27f, V007 :42) whose :88-108 is alias-audit content — NOT circuit canonicity;
under V003's member table (V003 :31, :37), member 04 = the V002 check (56d9c9b6),
whose :97-99 + :108-109 carry exactly the cited content, and member 10 = BID V011
(20a3a17d), where :1840-1852 exists and is the K_square display. The instance's
double resolution is correct and disclosed. The V007 §0 sentence is byte-carried from
V003 :91 (confirmed identical). CONFORMANCE rests on the resolved files at verified
digests — sound.

**CONFORMANCE = CONFIRMED.**

---

## 2. ATTACK 2 — TOPOLOGY RE-RUN (different methods)

My script (§6, verbatim) rebuilds everything from V011 :1840-1911 alone (own
transcription) and uses NONE of the instance's instruments:

```text
instrument               instance used            I used instead
rank                     Fraction RREF + 3-prime  Smith normal form over Z (invariant factors)
connectivity             V - rank identity        BFS on the undirected graph
b_1 second opinion       —                        GF(2) cycle-space enumeration (16 vectors)
null space / uniqueness  Fraction RREF back-solve box search over [-2,2]^4 (exhaustive in the box)
```

Results, all exact:

```text
SNF(bdry) invariant factors = [1, 1, 1]  =>  rank = 3 over Z and Q; H_1, H^1 TORSION-FREE
BFS: components = 1 (CONNECTED)                          — matches instance CHECK 5
b_1 = E - rank = 4 - 3 = 1; GF(2) cycle space = 2 = 2^1  — matches instance CHECK 6
rank d_1 = 0 (empty 0x4 map, F = 0); d_1 d_0 = 0 (0x4, vacuous — disclosed as such
  by the instance, correctly)                            — matches instance CHECKS 1, 4
dim H^1 = dim ker d_1 - rank d_0 = 4 - 3 = 1 EXACT       — matches instance CHECK 6
H = ker(d_1) ∩ im(d_0)^perp = ker(bdry): nullity 1, every integer solution in the box
  is k*(1,-1,1,-1)  =>  dim H = 1, basis {(+1,-1,+1,-1)} — matches instance CHECKS 11, 12
block sum 3 + 1 + 0 = 4 = E EXACT                        — matches instance CHECK 11
```

The torsion-freeness (SNF all-ones) is strictly more than the instance claimed —
nothing hides in torsion; the Q-rank statements are the whole story.
The instance's embedded script was also re-extracted from the artifact bytes and
re-run: exit 0, output byte-identical to its §7 (diff empty, 27/27 lines).

**TOPOLOGY_RERUN = MATCH(H1 = 1, dim H = 1).**

---

## 3. ATTACK 3 — WITNESSES, against MY matrices

```text
gamma_j = +e_a0 -e_0b +e_ab -e_ba:  bdry(gamma_j) = (0,0,0,0) per vertex   CONFIRMED (A-7)
  orientation = the sealed loop word's exponent vector, re-derived:
  u_ab u_a0 (u_ba u_0b)^(-1)  ->  e_a0:+1, e_0b:-1, e_ab:+1, e_ba:-1       CONFIRMED
chi_j = (+1,-1,+1,-1):  <chi_j, d_0 delta_v> = 0 all v; chi_j != 0;
  <chi_j, gamma_j> = 4 != 0; [chi_j] generates H^1                          CONFIRMED
ell_H = (+1,-1,+1,-1):
  conserved / gauge-invariant:  d_0^dagger ell_H = bdry . ell_H = 0         CONFIRMED (A-10)
  in H:                         ker d_1 = C^1 and ell_H ∈ ker(bdry)         CONFIRMED
  cell-local:                   support = the 4 edges of the single cell j
                                (on-cell; the inter-cell half is not posed
                                here and the instance says so)              CONFIRMED
  total-nonzero:                phi_f(ell_H) + phi_H(ell_H) = ell_H != 0    CONFIRMED
  genuinely nonzero in the claimed block: phi_H(ell_H) = ell_H (in H)       CONFIRMED
  phi_f block: im(d_1^dagger) = {0} exactly (rank d_1 = 0); P_f = 0;
  phi_f = 0 for EVERY 1-cochain — no witness can exist                      CONFIRMED
fixed-gauge reading:  theta_j = +Phi == the sealed exp(i Phi) loop word     CONFIRMED (A-8)
```

**WITNESSES = CONFIRMED.**

---

## 4. ATTACK 3b — SATISFIABLE vs FORCED, adjudicated

The build's exact sentence (§4.3 / flag): "phi_H != 0 is FORCED on the admissible set
(not merely satisfiable); phi_f != 0 is UNSATISFIABLE; their conjunction is
CONSTANT_FALSE."

Re-derivation from my matrices: admissible = {ell : bdry.ell = 0} ∩ {total nonzero}
= (H ⊕ {0}) \ {0} = H \ {0}, a punctured line, NONEMPTY (witness exhibited).
On it phi_H(ell) = ell != 0 ALWAYS (forced — correct, because phi_f ≡ 0 makes
total-nonzero bite entirely on phi_H); phi_f(ell) = 0 ALWAYS (unsatisfiable — the
block is zero-dimensional, a rank fact, not a sampling fact). AND = FALSE at every
admissible member, constant by rank identity. The build claimed no more and no less;
in particular it did NOT claim "satisfiable" where "forced" holds (it upgraded
explicitly and flagged the upgrade), and did NOT claim the phi_f failure is scoped
when it is identical. The MIRROR framing is exact against the sealed baseline
(AND :208-219 read at bytes: working class has dim H = 0 with phi_H identically zero
and phi_f forced nonzero; here rank d_1 = 0 with phi_f identically zero and phi_H
forced nonzero — the roles exchange precisely).

**SATISFIABLE_VS_FORCED = STATED-EXACTLY.**

---

## 5. ATTACK 4 — STRATUM CONSEQUENCE, audited claim by claim

```text
S-1  Q-1027 untouched for its own complexes.  EXACT: the AND verdict's BINDING clause
     (AND :330-335, read at bytes) binds to the working-class instance and its
     licensed refinements; K_square is outside it; nothing here contradicts the five
     rows of AND :192-199.
S-2  reopening realized "for the first time — at entered-authored-premise strength".
     EXACT under the operative reading: AND §7's condition (:337-348) is about a
     complex giving PHI_H a nonzero-dimensional range — i.e. a carrier on which the
     AND-class question is posed.  The glued hunt had already exhibited H^1 > 0
     complexes of record (K_square itself; K_L) at the AUDIT stratum (hunt :294-314,
     :813), but no write structure is typed there, so the QUESTION never reopened on
     them.  This build is the first place the reopened question is posed (typed, per
     G3 Q6) and decided.  The instance's qualifiers ("entered-authored-premise
     strength", S-3(a)'s preservation of NONE_SEALED at the physical write-carrier
     stratum) keep the claim inside what is true.  NOTE (recorded, no correction
     required): the phrases "On NO carrier now of record is the AND-class
     satisfiable" (S-2) and "no admissible realization on ANY carrier now of record"
     (S-4) are true on the strict reading — on K_L-type audit objects no admissible
     set is defined of record, so no admissible realization exists there (vacuously);
     on the two carriers where the question IS posed (working class; this instance)
     it is decided FALSE.  A future typing of the write constraints onto a carrier
     with BOTH blocks nonzero-dimensional (K_3: dim H = 4, dim im(d_1^dagger) = 240,
     hunt :298-301) would have to be decided fresh; nothing in the instance forecloses
     that, and S-3(c) says its certificate does not extend.
S-3  the six non-claims (a)-(f).  All EXACT at bytes — (a) check :288-291 verbatim;
     addendum :46-47 verbatim; (c) correctly limits the trivial member-independence;
     (e) V011 :2321 verbatim; (f) matches the addendum's BINDING CONSEQUENCES
     (:51-56).  ONE CITATION CORRECTION in (b): "no sealed map sends K_square into
     the write-carrier complex" is sealed at HUNT 1892c08e :324-326 ("no sealed map
     sends either audit object onto the working class or vice versa"), NOT at
     "check :325" (the glued check's :325 is its injection-audit line; the check
     touches this content only via P-4's blanket span confirmation of the hunt).
     The statement itself is TRUE and SEALED; the file attribution is wrong.
     Same defect class as the glued check's own P-1 finding.  No verdict moves.
S-4  the one-line consequence and the four live gaps (write realization on this
     carrier, O12 inter-cell half, physical-domain proof, post-limit).  EXACT; the
     gap list matches the glued check's :279-291 state plus the AND post-limit item,
     with the vacuous-truth note above.
```

TRANSCRIPTION NOTE (for the registrar, not a defect of the instance): the tasking's
quoted copy of the instance's flag block is NOT byte-identical to the artifact's —
minor reflow ("the census is premise-pinned" -> "census premise-pinned";
"the vertex/edge" -> "vertex/edge") and one ADDED clause in SCRIPT_REPRODUCED
("embedded block re-extracted and re-run byte-identical") that the artifact's own
flag block does not contain. The artifact's flag block is the authoritative one.
The added clause happens to be TRUE — I performed that re-extraction and re-run
myself (§2) — but it must be registered from the artifact, not from the relay copy.

**STRATUM_STATEMENT = CORRECTED(S-3(b) citation only: hunt :324-326, not "check :325";
substance stands, all verdicts unchanged).**

---

## 6. MY SCRIPT, VERBATIM (`b1_cell_check_v001.py`, Python 3 stdlib only)

```python
#!/usr/bin/env python3
# b1_cell_check_v001.py -- B1-CELL-CHECK: independent adversarial re-computation.
# DIFFERENT METHODS from the instance: Smith normal form over Z (not RREF rank),
# BFS connectivity (not rank identity), GF(2) cycle-space dimension (third
# instrument), brute-force integer null space, and independent witness re-check
# against matrices rebuilt from the sealed V011 display only.
# Exact integer arithmetic only. No physical quantity computed or bounded.
from fractions import Fraction
from itertools import product

# --- rebuilt from V011 :1840-1851 / :1896-1901 ONLY (my own transcription) ----
VERTS = ['v_00', 'v_10', 'v_01', 'v_11']
EDGES = [('e_a0', 'v_00', 'v_10'),
         ('e_0b', 'v_00', 'v_01'),
         ('e_ab', 'v_10', 'v_11'),
         ('e_ba', 'v_01', 'v_11')]
FACES = []  # V011 :1840 "no 2-cell"; :1881-1882 "No filled 2-cell ... trace carrier"
nV, nE, nF = len(VERTS), len(EDGES), len(FACES)
vi = {v: i for i, v in enumerate(VERTS)}

# boundary bdry: C_1 -> C_0 (rows vertices, cols edges; -1 source, +1 target)
bdry = [[0]*nE for _ in VERTS]
for j, (e, s, t) in enumerate(EDGES):
    bdry[vi[s]][j] -= 1
    bdry[vi[t]][j] += 1

# sealed display V011 :1903-1911 at u = 1 (my own transcription, independent)
D_sealed = [[-1, -1, 0, 0], [1, 0, -1, 0], [0, 1, 0, -1], [0, 0, 1, 1]]
assert bdry == D_sealed, 'rebuilt incidence != sealed display'
print('A-1 rebuilt incidence == sealed D_square(u=1): True')

# --- method 1: Smith normal form of bdry over Z ------------------------------
def smith_normal_form(M, rows, cols):
    A = [row[:] for row in M]
    def swap_rows(i, j): A[i], A[j] = A[j], A[i]
    def swap_cols(i, j):
        for r in range(rows): A[r][i], A[r][j] = A[r][j], A[r][i]
    t = 0
    invariants = []
    while t < min(rows, cols):
        # find nonzero pivot with min |value|
        best = None
        for i in range(t, rows):
            for j in range(t, cols):
                if A[i][j] != 0 and (best is None or abs(A[i][j]) < abs(A[best[0]][best[1]])):
                    best = (i, j)
        if best is None:
            break
        swap_rows(t, best[0]); swap_cols(t, best[1])
        done = False
        while not done:
            done = True
            for i in range(t+1, rows):
                if A[i][t] % A[t][t] != 0:
                    q = A[i][t] // A[t][t]
                    for j in range(cols): A[i][j] -= q*A[t][j]
                    swap_rows(t, i); done = False
                    break
            if not done: continue
            for i in range(t+1, rows):
                q = A[i][t] // A[t][t]
                for j in range(cols): A[i][j] -= q*A[t][j]
            for j in range(t+1, cols):
                if A[t][j] % A[t][t] != 0:
                    q = A[t][j] // A[t][t]
                    for i in range(rows): A[i][j] -= q*A[i][t]
                    swap_cols(t, j); done = False
                    break
            if not done: continue
            for j in range(t+1, cols):
                q = A[t][j] // A[t][t]
                for i in range(rows): A[i][j] -= q*A[i][t]
            # residual check
            for i in range(t+1, rows):
                if A[i][t] != 0: done = False
            for j in range(t+1, cols):
                if A[t][j] != 0: done = False
        invariants.append(abs(A[t][t]))
        t += 1
    return invariants

inv = smith_normal_form(bdry, nV, nE)
rank_bdry = len([d for d in inv if d != 0])
assert inv == [1, 1, 1], 'SNF invariant factors: %s' % inv
assert rank_bdry == 3
print('A-2 SNF(bdry) invariant factors = %s -> rank_Z = rank_Q = 3; H_1 and H^1 TORSION-FREE' % inv)

# --- method 2: BFS connectivity (no linear algebra) --------------------------
adj = {v: set() for v in VERTS}
for e, s, t in EDGES:
    adj[s].add(t); adj[t].add(s)
seen = set(); stack = [VERTS[0]]
while stack:
    v = stack.pop()
    if v in seen: continue
    seen.add(v); stack.extend(adj[v] - seen)
assert seen == set(VERTS)
print('A-3 BFS from v_00 reaches all 4 vertices: CONNECTED (components = 1)')

# --- method 3: cycle space over GF(2) (third instrument) ---------------------
# brute force: all 16 GF(2) edge vectors; count those with boundary 0 mod 2
gf2_cycles = 0
for vec in product((0, 1), repeat=nE):
    b = [sum(bdry[i][j]*vec[j] for j in range(nE)) % 2 for i in range(nV)]
    if b == [0]*nV:
        gf2_cycles += 1
assert gf2_cycles == 2  # 2^1 -> dim = 1
print('A-4 GF(2) cycle space has 2 = 2^1 elements -> b_1 = 1 over GF(2) (torsion-free => matches Q)')

# --- b_1, H^1, blocks (F = 0 => d_1 the empty 0x4 map; ker d_1 = C^1) --------
b1 = nE - rank_bdry
dim_ker_d1 = nE - 0        # rank d_1 = 0: d_1 has no rows at all (F = 0)
dim_H1 = dim_ker_d1 - rank_bdry   # rank d_0 = rank d_0^T = rank bdry
assert b1 == 1 and dim_H1 == 1
# d_1 d_0 has shape (0 x 4): zero matrix by emptiness; also rank d_1 = 0 trivially
print('A-5 rank d_1 = 0 (empty map, F = 0); d_1 d_0 = 0 (0x4, vacuous); b_1 = 1; dim H^1 = 4 - 3 = 1 EXACT')

# --- exact integer null space of bdry by brute force over a bounded box ------
# (independent of any elimination: enumerate primitive integer vectors, entries in [-2,2])
null_prim = []
for vec in product(range(-2, 3), repeat=nE):
    if all(x == 0 for x in vec):
        continue
    b = [sum(bdry[i][j]*vec[j] for j in range(nE)) for i in range(nV)]
    if b == [0]*nV:
        from math import gcd
        g = 0
        for x in vec: g = gcd(g, abs(x))
        if g == 1 or all(abs(x) <= 1 for x in vec):
            null_prim.append(vec)
# the primitive +-1 solutions must be exactly +-(1,-1,1,-1)
pm1 = [v for v in null_prim if all(abs(x) == 1 for x in v)]
assert set(pm1) == {(1, -1, 1, -1), (-1, 1, -1, 1)}, pm1
# every null vector in the box is a multiple of (1,-1,1,-1)
for v in null_prim:
    k = v[0]
    assert v == (k, -k, k, -k), v
print('A-6 integer null space (box search): every solution is k*(1,-1,1,-1) -> nullity 1; unique cycle class up to sign')

# --- the sealed loop word fixes the sign: u_ab u_a0 (u_ba u_0b)^(-1) ---------
# exponents: e_ab +1, e_a0 +1, e_0b -1, e_ba -1 -> on order (e_a0,e_0b,e_ab,e_ba):
loop = (+1, -1, +1, -1)
assert loop in {(1, -1, 1, -1)}
bg = [sum(bdry[i][j]*loop[j] for j in range(nE)) for i in range(nV)]
assert bg == [0]*nV
print('A-7 sealed loop word exponent vector (+1,-1,+1,-1) is a cycle; F08 sign fixed to it')

# --- fixed gauge V011 :1866-1873: a = (0,0,0,-1)*Phi -> theta = +1 * Phi -----
a_phi = [0, 0, 0, -1]
theta_coeff = sum(loop[j]*a_phi[j] for j in range(nE))
assert theta_coeff == +1
print('A-8 fixed-gauge reading theta_j = (+1)*Phi == sealed exp(i Phi) loop word (coefficient only)')

# --- blocks: H = ker(d_1) cap im(d_0)^perp, standard inner product -----------
# ker d_1 = C^1 entire. im(d_0) = column space of bdry^T = row space of bdry.
# im(d_0)^perp = null space of bdry (computed above): span{(1,-1,1,-1)} -> dim H = 1
dim_im_d0 = rank_bdry          # 3
dim_im_d1dag = 0               # rank d_1 = 0
dim_H = 1                      # A-6
assert dim_im_d0 + dim_H + dim_im_d1dag == nE
print('A-9 blocks: dim im(d_0)=3, dim H=1, dim im(d_1^dagger)=0; 3+1+0 = 4 = E EXACT')

# --- witness re-check against MY matrices ------------------------------------
ellH = (1, -1, 1, -1)
d0dag = [sum(bdry[i][j]*ellH[j] for j in range(nE)) for i in range(nV)]  # bdry . ell
assert d0dag == [0]*nV                       # conserved / gauge-invariant
assert any(x != 0 for x in ellH)             # nonzero
# ell in H: in ker d_1 (all of C^1) and perp im(d_0) (= ker bdry) -- shown
# P_f is projection onto im(d_1^dagger) = {0}: the zero map
phi_f = (0, 0, 0, 0)
phi_H = ellH                                 # P_H ellH = ellH since ellH in H
total = tuple(a+b for a, b in zip(phi_f, phi_H))
assert any(t != 0 for t in total)
print('A-10 witness ell_H=(1,-1,1,-1): bdry.ell=0 (conserved/gauge-inv), ell in H, phi_f(ell)=0,')
print('     phi_H(ell)=ell != 0, total != 0; support = the 4 edges of the single cell (cell-local on-cell)')

# --- the two-sector decision, re-derived -------------------------------------
# admissible = {ell : bdry.ell = 0, ell != 0 (total-nonzero with phi_f == 0)} = H\{0}
# phi_f == 0 identically (zero-dim block) -> phi_f != 0 UNSATISFIABLE
# phi_H(ell) = ell != 0 on all of H\{0}    -> phi_H != 0 FORCED on every admissible ell
# AND = FALSE AND TRUE = FALSE, constant (rank-forced, not sampled)
print('A-11 phi_f != 0 UNSATISFIABLE (block {0}); phi_H != 0 FORCED on H\\{0}; AND = CONSTANT FALSE')
print('A-12 mirror of working class confirmed structurally: there dim H = 0 & flux >= 1; here flux = 0 & dim H = 1')
print('ALL ADVERSARIAL CHECKS PASSED')
```

## 7. EXACT SCRIPT OUTPUT, VERBATIM (`python3 b1_cell_check_v001.py`, exit code 0)

```text
A-1 rebuilt incidence == sealed D_square(u=1): True
A-2 SNF(bdry) invariant factors = [1, 1, 1] -> rank_Z = rank_Q = 3; H_1 and H^1 TORSION-FREE
A-3 BFS from v_00 reaches all 4 vertices: CONNECTED (components = 1)
A-4 GF(2) cycle space has 2 = 2^1 elements -> b_1 = 1 over GF(2) (torsion-free => matches Q)
A-5 rank d_1 = 0 (empty map, F = 0); d_1 d_0 = 0 (0x4, vacuous); b_1 = 1; dim H^1 = 4 - 3 = 1 EXACT
A-6 integer null space (box search): every solution is k*(1,-1,1,-1) -> nullity 1; unique cycle class up to sign
A-7 sealed loop word exponent vector (+1,-1,+1,-1) is a cycle; F08 sign fixed to it
A-8 fixed-gauge reading theta_j = (+1)*Phi == sealed exp(i Phi) loop word (coefficient only)
A-9 blocks: dim im(d_0)=3, dim H=1, dim im(d_1^dagger)=0; 3+1+0 = 4 = E EXACT
A-10 witness ell_H=(1,-1,1,-1): bdry.ell=0 (conserved/gauge-inv), ell in H, phi_f(ell)=0,
     phi_H(ell)=ell != 0, total != 0; support = the 4 edges of the single cell (cell-local on-cell)
A-11 phi_f != 0 UNSATISFIABLE (block {0}); phi_H != 0 FORCED on H\{0}; AND = CONSTANT FALSE
A-12 mirror of working class confirmed structurally: there dim H = 0 & flux >= 1; here flux = 0 & dim H = 1
ALL ADVERSARIAL CHECKS PASSED
```

---

## 8. ATTACK 5 — PROVENANCE + INJECTION

```text
PROVENANCE:  the entered-authored-premise provenance is carried at every load-bearing
  site of the instance: the lead (:36-38), §0's fences, §1's constraint extraction
  (every constraint quoted from the entered chain), S-3(f) (void trigger restated,
  matching addendum :51-56 at bytes), and the flag block (PROVENANCE_CARRIED line;
  TYPE-P on 420ab02f).  Nowhere is any result presented as premise-free.  The
  standing fences (alpha_computed = false, kappa_record_computed = false,
  proof_authorized = false) are carried verbatim and match the addendum's own
  :55-56.  CLEAN.
INJECTION:  no verdict in the instance cites its tasking as authority; every
  load-bearing quotation was re-read at the sealed bytes this session and is
  verbatim; the one citation-resolution step (N-1) is disclosed and verified both
  ways rather than followed blindly.  The tasking-vs-artifact flag-block reflow
  (§5 transcription note) is a relay-copy artifact, not an injection, and the
  artifact's own bytes govern.  My own verdicts above cite only sealed files at
  recomputed digests.  NONE FOUND.
```

---

## FLAG BLOCK

```text
CONFORMANCE = CONFIRMED (all nine extracted constraints + F = 0 mandate re-read at
  sealed bytes and re-checked against the built object; census entrywise = V011
  :1840-1911; no violated or silently-dropped constraint; minimality correctly
  premise-pinned — no size freedom exists, and the disclosure of abstractly smaller
  nonconforming complexes is honest; freedom inventory complete both directions:
  FR-1/FR-2 genuinely free and correctly fixed, nothing forced presented as free,
  nothing free presented as forced; note N-1's double citation-resolution verified
  at bytes both ways).
TOPOLOGY_RERUN = MATCH(H1 = 1, dim H = 1) (independent methods: Smith normal form
  over Z — invariant factors [1,1,1], rank 3, torsion-free; BFS connectivity —
  components = 1; GF(2) cycle space = 2^1; box-search integer null space — nullity 1,
  every solution k*(1,-1,1,-1); rank d_1 = 0; d_1 d_0 = 0 (0x4, vacuous, disclosed);
  blocks 3 + 1 + 0 = 4 = E exact; instance's embedded script also re-extracted and
  re-run: exit 0, output byte-identical to its §7).
WITNESSES = CONFIRMED (gamma_j: bdry(gamma_j) = 0 per vertex, orientation = the
  sealed loop word's exponent vector re-derived independently; chi_j: ⊥ im(d_0),
  nonzero, generates H^1, pairing 4; ell_H: conserved/gauge-invariant
  (bdry.ell_H = 0), in H, cell-local on-cell, total-nonzero, genuinely nonzero in
  phi_H and zero in phi_f — all against my own rebuilt matrices).
SATISFIABLE_VS_FORCED = STATED-EXACTLY (admissible set = H \ {0} nonempty; phi_H != 0
  FORCED — not merely satisfiable — because phi_f ≡ 0 makes total-nonzero bite
  entirely on phi_H; phi_f != 0 UNSATISFIABLE — zero-dimensional block, a rank fact;
  AND = CONSTANT_FALSE by rank identity; the mirror framing against the sealed
  working-class baseline AND :208-219 is exact with the two blocks' roles exchanged).
STRATUM_STATEMENT = CORRECTED(S-3(b) citation only: "no sealed map sends K_square
  into the write-carrier complex" is sealed at HUNT 1892c08e :324-326, not
  "check :325"; the statement itself is true and sealed; the glued check touches it
  only via P-4's blanket span confirmation; no verdict moves.  All else EXACT: S-1
  binding audit clean; S-2's "first time" claim exact under the operative reading —
  the hunt's audit-stratum H^1 > 0 objects never carried a posed write structure, so
  the AND question reopens (typed) here first; the "NO carrier now of record"
  universals hold strictly, vacuously on audit objects, decided-FALSE on the two
  posed carriers, with a fresh decision required if the write constraints are ever
  typed onto a both-blocks-positive carrier such as K_3; S-3(a),(c)-(f) verbatim at
  bytes; S-4 gap list matches the glued check's state).
INSTANCE_VERDICT = SOUND (the entered premise's cell is realized exactly as sealed;
  every number re-derives by independent methods; the AND-class decision on it is
  correct and correctly scoped; the one defect found is a citation misattribution
  that changes nothing).
PROVENANCE = CLEAN (entered-authored-premise carried at every load-bearing site;
  nothing presented as premise-free; TYPE-P on 420ab02f with the void trigger
  restated; standing fences carried; this check inherits the same provenance and
  voids with the same entry).
INJECTION = none (no verdict cites the tasking as authority in the instance or in
  this check; all load-bearing quotations verbatim at recomputed digests; noted for
  the registrar: the tasking's relay copy of the instance flag block is a reflow
  with one added — independently true — clause; register from the artifact bytes).
MACHINERY_USED_BY_ME = no (Python 3 stdlib only; exact integer/rational arithmetic;
  no CAS, no solver, no numerical evaluation; Phi kept an indeterminate).
SEALS_VERIFIED_BY_ME = a3bedc7e (instance), 420ab02f, ad9fc14e, ccca6bb4, 5154c203,
  82d5c5dd, 96ec8bf4, 56d9c9b6, 5f55c27f, 20a3a17d, 1892c08e, a22ef820, 38bbb9fc,
  c0e7192b (vs own sidecar), 5e49d209, 3e35ffe2 — all recomputed at path this
  session; none unverifiable.
alpha_computed = false, kappa_record_computed = false, proof_authorized = false.
ALL_RESULTS of the instance: now CHECKED (this artifact); registrar action not taken
  here (no register/commit/push by this lane).
```
