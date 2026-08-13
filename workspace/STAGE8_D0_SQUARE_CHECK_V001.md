# STAGE 8 / D0-SQUARE-CHECK — BLIND INDEPENDENT RE-VERIFICATION OF THE d_0-SQUARE CERTIFICATE

Lane: FABLE blind re-verifier, codename D0-SQUARE-CHECK, cross-lineage. Default = REFUTE.
Certificate under test: `STAGE8_D0_SQUARE_CERTIFICATE_V001.md`
(sha256 `bb1b88ad22ad2746a59957936785e9e44e3c2c4c1abdf7cf417096ff982d08c4`, VERIFIED at path).

## Verdict

**CERT_VERDICT = CONFIRMED.** Every attack ran to completion and none refuted:
matrix fidelity 0 discrepancies over 1,906 nonzero entries in 8 matrices; my own
independent decision algorithm (spanning-tree integration, not the build's Gaussian
elimination) re-certifies all five generator squares with exact zero residuals over Z;
the generator list is exhaustive of the sealed licensing; provenance clean; no injection.

```text
GATES  alpha_computed = false ; kappa_record_computed = false ; proof_authorized = false.
       No physical quantity computed, bounded, or evaluated. Structural integers only.
```

---

## 0. Preflight and seals (all verified by shasum -a 256 at path BEFORE reliance)

Output name probed before any write: `STAGE8_D0_SQUARE_CHECK_V001.md` ABSENT.
No register, tracker, plan, road, ledger, or lens file read.

```text
bb1b88ad22ad2746a59957936785e9e44e3c2c4c1abdf7cf417096ff982d08c4  STAGE8_D0_SQUARE_CERTIFICATE_V001.md      MATCH (under test)
22a2a478fb9f529692000a61b0f294757976156521922a609ff2ea8ae324ad0b  STAGE8_TRANSPORT_LAW_POSED_V001.md        MATCH
a5c71b2ac7cd198bbac188e865d139a71340f1728f72fe56384aa5d60489110c  STAGE8_TRANSPORT_LAW_POSE_CHECK_V001.md   MATCH
97f073c101d8cf4a6743660b96e3861e21914ac48877ce538314616b51d70cb6  STAGE8_B1A_REFINEMENT_CARRIER_DARIO_V001.md              MATCH
614e20c8bfd1978a4273c831b76bd6145483876c975ea87f80ef31a589b8bdc7  STAGE8_B1A_CARRIER_CROSSCHECK_NATURALITY_CODEX2_V001.md  MATCH
590b3979d5a0fadfd570e3a73a13bb3a717d5450f7eb5c9f2e79f481039fc1e2  STAGE8_B1A_COFRAME_HALF_DARIO_V001.md     MATCH (self-identifies "Relay 795", O1 = PROVED)
aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a  review_packets/STAGE7_QSPEC_CANDIDATE_V001/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md  MATCH (78,794 B)
```

Two-byte-version hazard independently confirmed: the TOP-LEVEL
`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` hashes `20a3a17d44e15841baded9eaed3f...`
at 84,987 B — a different file. Only the sealed packet member (`aa7c6d49...`, 78,794 B)
was consumed, matching the certificate's binding. The top-level copy's content was NOT read.

## 1. Span rehash (sha256 of the byte span, extracted from the sealed bytes by me)

All six spans cited by the certificate were re-extracted and rehashed; ALL MATCH the
certificate's pins, and the span CONTENTS ground every construction below:

```text
V011      [44595,44690)  c6cd568bec678df676737009466e3537dfe64fd6962fdb3200b9f90b9dc14eb5  MATCH  (d_0 lambda)_e = lambda_t - lambda_s
V011      [44530,45446)  9bbd9525cbd84a6b6365383da6cd6e38d33f945e01c98c1a0d3052f322b74efc  MATCH  ker(d_0) = constants per component
V011      [46772,47023)  cf173101542c3d7fb6a045d9c11cd955e89a81c143638a7b3996d8603e6dc849  MATCH  licensed inventory (3 items)
CARRIER   [5151,9996)    4eb23669b793b5531388e9c506970c004f4e13e9f62060fa5f01190e9ed20d68  MATCH  sd*_1 law
CROSSCHECK[4056,5082)    6ae8c4c440588efe7c0b107da8f003dbc35e24648a4817f76f87e428862ee447  MATCH  complexes + per-row aggregation
795       [7747,9120)    5ed8d194448db5045dc077f177372f7ac81278353c3bd885a1727c0c0dae8cba  MATCH  A0 sigma=(1,0,3,2), L_id = id clause
```

Citation checks at path: POSED `FIRST_BUILDABLE` verbatim at lines 615-627 (names the
inputs, spans, and "composites free"); POSED lines 184-190 cite 795 per-generator
existence and the 771/0 crosscheck; POSE_CHECK lines 265-277 ground the sd*_0
exhaustion in finite-dimensional linear decidability, NOT the direction theorem —
the certificate carries this correctly (its section 1); carrier line 310 carries the
composite-closure quote ("a composition of chain maps is a chain map", D4 section 3.2);
crosscheck lines 136 and 322 carry `771` trials / `0` mismatches.

---

## 2. Attack 1 — MATRIX FIDELITY: CONFIRMED, 0 discrepancies

Every matrix was re-derived by me DIRECTLY from the sealed constructive displays
(no sealed dense dump exists; the certificate disclosed this and I confirm it — the
sealed bytes give the d_0 law, the sd*_1 law, the three refined complexes with their
per-row aggregation rules, and the A0 instance, which determine every matrix uniquely
up to cell ordering). My reconstructions were diffed ENTRY BY ENTRY against the
certificate's section 8 sparse displays (parsed from the section 8 output only, never
from the section 7 code listing):

```text
matrix              rows  nonzero entries  discrepancies
d_0        (32x16)    32        64             0
sd*_1[A0]  (32x32)    32        32             0
d_0'[A1]  (216x81)   216       432             0
sd*_1[A1] (32x216)    32        64             0
d_0'[A2-F] (65x16)    65       130             0
sd*_1[A2-F](32x65)    32        32             0
d_0'[A2-B](544x81)   544      1088             0
sd*_1[A2-B](32x544)   32        64             0
TOTAL                          1906            0
```

Census and invariants, from my reconstruction, all matching the sealed displays:
parent 16/32/24; A1 81/216 with 16 subcubes; A2-F 16/65 with 24 4-simplices
(65 = 3^4 - 2^4 per the carrier); A2-B 81/544; sd*_1 row rank 32 on all four
generators; dim ker sd*_1 A0=0, A1=184, A2-F=33, A2-B=512; A0 sd*_1 is a
permutation matrix; dim ker d_0 = 1 on every complex (connected, so the V011
constants clause applies with dimension exactly 1).

## 3. Attack 2 — INDEPENDENT RE-RUN: MATCH, all residuals zero

My decision algorithm is NOT the build's. The build row-reduced the augmented block
`[d_0 | B | I_32]`. I decide `d_0 . X = B` by spanning-tree integration on the parent
4-cube graph with cycle-consistency checking: potentials are integrated along a BFS
tree (integer by construction from integer B), then every one of the 32 edges is
checked; a failure would exhibit the explicit integer cycle witness `lambda` with
`lambda . d_0 = 0`, `lambda . B_col != 0`. Both negative branches (COUNTEREXAMPLE,
NO_COMPATIBLE_SD0) were implemented before the first solve ran. Results:

```text
generator  my solve   integer  residual(my X)  residual(iota*)  X - iota* const cols  MY VERDICT
L_id       SOLVED     yes      0               0                yes                   CERTIFIED
A0         SOLVED     yes      0               0                yes                   CERTIFIED
A1         SOLVED     yes      0               0                yes                   CERTIFIED
A2-F       SOLVED     yes      0               0                yes                   CERTIFIED
A2-B       SOLVED     yes      0               0                yes                   CERTIFIED
```

The BUILD'S OWN EXHIBITS were additionally parsed from the certificate's section 8 and
verified against MY matrices: for all five generators the build's canonical sd*_0
equals my independently derived iota* exactly; the build's solver-anchored sd*_0 has
exact zero residual `sd*_1 . d_0' - d_0 . sd*_0 = 0` over Z; and the build's solver
solution differs from iota* by a per-column constant only (pure ker d_0 freedom).

Soundness note (recorded, not a defect): for these d_0 matrices — graph incidence
maps — tree-integration of integer data is automatically integral, so rational
solvability implies integer solvability and the build's RATIONAL-ONLY branch
(NO_INTEGER_SOLUTION) could never fire on this parent complex. The branch was
implemented and honest; it is mathematically vacuous here. This strengthens, not
weakens, the certificate: over Z and over Q the answer coincides.

## 4. Attack 3 — COMPLETENESS: YES

The sealed licensing (V011 [46772,47023), rehashed above) lists exactly three items:

1. "cubical bisection" — covered: A1, certified.
2. "oriented simplicial/barycentric subdivision" — a CLASS; the two sealed instances
   of record (the only ones any sealed input constructs: crosscheck [4056,5082))
   are A2-F and A2-B, both certified. The certificate explicitly binds to the
   exhibited instances and claims no unexhibited member; correct scope.
3. "common refinements preserving the same smooth coframe and connection" —
   composites: free by the composite-closure step, verified at carrier line 310
   ("a composition of chain maps is a chain map"). The paste identity
   `sd*_1[g] sd*_1[h] d_0'' = sd*_1[g] d_0' sd*_0[h] = d_0 sd*_0[g] sd*_0[h]`
   is algebraically valid given the per-generator certificates, with
   `sd*_0[h o g] := sd*_0[g] . sd*_0[h]`. Valid at span; the posing itself
   states "composites free by the sealed composite-closure step".

`L_id = id` holds two ways: derived of record in the 795 span (Clause 1 PROVED, from
the section structure of an injective surjection) AND directly — the identity square
degenerates to `d_0 = d_0` and my re-run certifies it with sd*_0 = I_16.
A0 (relabelings) carries no refinement by type (795); its inclusion is surplus
rigor, not a licensing gap. No licensed move is missing.

## 5. Attack 4 — NEGATIVE CLAIMS: n/a

The certificate claims no COUNTEREXAMPLE and no NO_INTEGER_SOLUTION on any generator.
There is no negative claim to verify. My independent machinery would have exhibited
an explicit integer cycle witness had any square failed; none did.

## 6. Attack 5 — PROVENANCE + INJECTION: CLEAN / none

- All seven file digests verified at path before reliance; all six span digests
  rehashed from the sealed bytes and matched; every matrix grounded in sealed spans.
- The certificate's quoted span contents match the sealed bytes verbatim (section 1).
- The unsealed top-level V011 copy is confirmed to be a DIFFERENT file and was not
  consumed by me beyond hashing; the certificate binds to the packet member only.
- No verdict in this check cites the tasking text as evidence; every claim above is
  grounded in a sealed byte span, a path-verified digest, or my own reproduced
  computation. The certificate contains no directive attempting to steer a verifier
  away from any check (injection scan over its full text: none found).
- I read no register/tracker/plan/road/ledger/lens file. My machinery: reads,
  shasum -a 256 at path, byte-span extraction, one exact integer/rational script
  (below). No member binding, no fixed-point execution, no end test, no git action.

---

## 7. My script, verbatim (`d0_square_check_v001.py`, Python 3 stdlib only)

```python
#!/usr/bin/env python3
# d0_square_check_v001.py — BLIND RE-VERIFIER (D0-SQUARE-CHECK), cross-lineage.
# Independent of the build's script: solvability of d_0 . X = B is decided by
# SPANNING-TREE INTEGRATION + CYCLE-CONSISTENCY (constructive integer witness on
# failure), NOT by the build's augmented-block Gaussian elimination. All residuals
# recomputed in pure integer arithmetic. Fractions used ONLY for exact rank.
#
# SEALED INPUTS (constructions re-derived from the sealed byte spans, all rehashed):
#   d_0 law        V011 aa7c6d49... [44595,44690): (d_0 lambda)_e = lambda_t - lambda_s
#   ker d_0        V011 aa7c6d49... [44530,45446): ker(d_0) = constants per component
#   inventory      V011 aa7c6d49... [46772,47023): cubical bisection; oriented simplicial/
#                  barycentric subdivision; common refinements (composites)
#   sd*_1 law      carrier 97f073c1... [5151,9996): (sd*_1 a')_e = sum orientation(e',e) a'_e'
#   complexes+rows crosscheck 614e20c8... [4056,5082): parent 16/32/24; A1 grid {0,1,2}^4
#                  81/216; A2-F Freudenthal 16/65; A2-B barycentric 81/544; "Cubical rows
#                  sum the two child edges. Freudenthal rows retain parent edges.
#                  Barycentric rows sum the two half-edges."
#   A0 instance    795 590b3979... [7747,9120): sigma = (1,0,3,2), sd*_1 = permutation P
#
# FIDELITY TARGET: the certificate bb1b88ad... section 8 sparse displays are parsed
# and diffed entry-by-entry against MY constructions. Any discrepancy refutes.
import re, sys
from fractions import Fraction
from itertools import product, permutations

CERT = "/Users/bgm/MB Work/alpha-program-archive/workspace/STAGE8_D0_SQUARE_CERTIFICATE_V001.md"

# ---------- MY constructions, from the sealed displays only ----------
def lab_v(v): return ''.join(str(x) for x in v)
def lab_e(e): return lab_v(e[0]) + '->' + lab_v(e[1])

# parent K: oriented unit 4-cube, 16 V / 32 positive-coordinate E / 24 F
PV = sorted(product((0, 1), repeat=4)); pvi = {v: i for i, v in enumerate(PV)}
PE = sorted((v, tuple(v[:i] + (1,) + v[i+1:])) for v in PV for i in range(4) if v[i] == 0)
pei = {e: i for i, e in enumerate(PE)}
PF = sum(1 for v in PV for i in range(4) for j in range(i+1, 4) if v[i] == 0 and v[j] == 0)

def d0_of(verts, edges, vi):
    M = [[0]*len(verts) for _ in edges]
    for r, (s, t) in enumerate(edges):
        M[r][vi[s]] -= 1; M[r][vi[t]] += 1
    return M
D0 = d0_of(PV, PE, pvi)

# A0: sigma=(1,0,3,2); sd*_1 = permutation P  (795 span)
def sig(v): return (v[1], v[0], v[3], v[2])
S1_A0 = [[0]*32 for _ in range(32)]
for e in PE:
    fe = (sig(e[0]), sig(e[1]))
    fe = fe if sum(fe[0]) < sum(fe[1]) or pvi[fe[0]] < pvi[fe[1]] else (fe[1], fe[0])
    S1_A0[pei[e]][pei[fe]] = 1
S1_ID = [[int(i == j) for j in range(32)] for i in range(32)]

# A1: grid {0,1,2}^4; rows sum the two child edges (both aligned)
GV = sorted(product((0, 1, 2), repeat=4)); gvi = {v: i for i, v in enumerate(GV)}
GE = sorted((v, tuple(v[:i] + (v[i]+1,) + v[i+1:])) for v in GV for i in range(4) if v[i] < 2)
gei = {e: i for i, e in enumerate(GE)}
D0_A1 = d0_of(GV, GE, gvi)
S1_A1 = [[0]*len(GE) for _ in range(32)]
for (s, t) in PE:
    i = next(k for k in range(4) if s[k] != t[k])
    a = tuple(2*x for x in s); m = tuple(a[k] + int(k == i) for k in range(4)); b = tuple(2*x for x in t)
    S1_A1[pei[(s, t)]][gei[(a, m)]] += 1
    S1_A1[pei[(s, t)]][gei[(m, b)]] += 1
NSUB = 2**4  # unit subcubes of the bisected 4-cube: census 16

# A2-F: Freudenthal chains of Boolean vertices; 65 edges u->v (u<=v comp.wise, u!=v);
# rows retain parent edges; 24 maximal chains (4-simplices)
FE = sorted((u, v) for u in PV for v in PV if u != v and all(u[k] <= v[k] for k in range(4)))
fei = {e: i for i, e in enumerate(FE)}
D0_F = d0_of(PV, FE, pvi)
S1_F = [[0]*len(FE) for _ in range(32)]
for e in PE: S1_F[pei[e]][fei[e]] = 1
NSIMP = len(list(permutations(range(4))))  # 24

# A2-B: barycentric chains of nonempty 4-cube faces; face code digit 2 = free coord;
# edges g->f up the poset; rows: +1 @ (s->e-face), -1 @ (t->e-face)
BF = sorted(product((0, 1, 2), repeat=4)); bfi = {f: i for i, f in enumerate(BF)}
def subface(g, f): return g != f and all(f[k] == 2 or g[k] == f[k] for k in range(4))
BE = sorted((g, f) for g in BF for f in BF if subface(g, f)); bei = {e: i for i, e in enumerate(BE)}
D0_B = d0_of(BF, BE, bfi)
S1_B = [[0]*len(BE) for _ in range(32)]
for (s, t) in PE:
    i = next(k for k in range(4) if s[k] != t[k])
    mid = tuple(2 if k == i else s[k] for k in range(4))
    S1_B[pei[(s, t)]][bei[(s, mid)]] += 1
    S1_B[pei[(s, t)]][bei[(t, mid)]] -= 1

# ---------- exact helpers ----------
def mm(A, B):
    n, m, p = len(A), len(B), len(B[0]); C = [[0]*p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            a = A[i][k]
            if a:
                Bk, Ci = B[k], C[i]
                for j in range(p):
                    if Bk[j]: Ci[j] += a*Bk[j]
    return C

def rank_q(M):
    R = [[Fraction(x) for x in row] for row in M]; m = len(R); n = len(R[0]) if R else 0; r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if R[i][c]), None)
        if p is None: continue
        R[r], R[p] = R[p], R[r]; pv = R[r][c]; R[r] = [x/pv for x in R[r]]
        for i in range(m):
            if i != r and R[i][c]:
                f = R[i][c]; R[i] = [a - f*b for a, b in zip(R[i], R[r])]
        r += 1
        if r == m: break
    return r

def tree_solve(B):
    """Decide d_0 . X = B over Z on the parent 4-cube graph by spanning-tree
    integration; on failure return the explicit integer cycle witness lambda
    (lambda . d_0 = 0, lambda . B_col != 0)."""
    adj = {v: [] for v in PV}
    for idx, (s, t) in enumerate(PE):
        adj[s].append((t, idx, +1)); adj[t].append((s, idx, -1))
    k = len(B[0]); X = [[0]*k for _ in range(16)]
    # one BFS tree (independent of B), recording each vertex's tree path as signed edges
    root = PV[0]; parent = {root: None}; order = [root]; q = [root]
    while q:
        u = q.pop(0)
        for (w, idx, sgn) in adj[u]:
            if w not in parent:
                parent[w] = (u, idx, sgn); order.append(w); q.append(w)
    assert len(order) == 16, "parent complex not connected"
    def path_vec(v):  # signed edge chain root -> v
        vec = [0]*32; u = v
        while parent[u] is not None:
            (p, idx, sgn) = parent[u]; vec[idx] += sgn; u = p
        return vec
    for j in range(k):
        pot = {root: 0}
        for v in order[1:]:
            (p, idx, sgn) = parent[v]; pot[v] = pot[p] + sgn*B[idx][j]
        for idx, (s, t) in enumerate(PE):
            if pot[t] - pot[s] != B[idx][j]:
                lam = [0]*32; lam[idx] += 1
                pv_t, pv_s = path_vec(t), path_vec(s)
                for i2 in range(32): lam[i2] -= (pv_t[i2] - pv_s[i2])
                chk0 = [sum(lam[r]*D0[r][c] for r in range(32)) for c in range(16)]
                chkB = sum(lam[r]*B[r][j] for r in range(32))
                return ('INCONSISTENT', None, {'col': j, 'lambda': lam,
                        'lambda_d0_iszero': all(x == 0 for x in chk0), 'lambda_Bcol': chkB})
        for v in PV: X[pvi[v]][j] = pot[v]  # integer by construction from integer B
    return ('SOLVED', X, None)

# ---------- parse the certificate's own displays (fidelity target) ----------
text = open(CERT, encoding='utf-8').read()
text = text[text.index('## 8. Exact script output'):]  # section 8 output ONLY, never the section 7 code listing
def parse_block(after, until):
    seg = text[text.index(after) + len(after): ]
    seg = seg[: seg.index(until)]
    rows = {}
    for line in seg.splitlines():
        mrow = re.match(r'^  (\S+): (.*)$', line)
        if not mrow: continue
        rl, rest = mrow.group(1), mrow.group(2).strip()
        ent = {} if rest == '0' else { m.group(2): int(m.group(1))
               for m in re.finditer(r'([+-]?\d+)@(\S+)', rest) }
        rows[rl] = ent
    return rows

def to_sparse(M, rlabs, clabs):
    return {rlabs[r]: {clabs[c]: M[r][c] for c in range(len(M[r])) if M[r][c]}
            for r in range(len(M))}

def diff(name, mine, cert):
    bad = []
    for rl in set(mine) | set(cert):
        a, b = mine.get(rl, {}), cert.get(rl, {})
        if a != b: bad.append((rl, a, b))
    print(f'  FIDELITY {name}: rows={len(cert)} entries={sum(len(v) for v in cert.values())} '
          f'discrepancies={len(bad)}')
    for rl, a, b in bad[:5]: print(f'    ROW {rl}: mine={a} cert={b}')
    return len(bad)

PEl = [lab_e(e) for e in PE]; PVl = [lab_v(v) for v in PV]
GEl = [lab_e(e) for e in GE]; GVl = [lab_v(v) for v in GV]
FEl = [lab_e(e) for e in FE]
BEl = [lab_e(e) for e in BE]; BFl = [lab_v(v) for v in BF]

print('== SEALED CENSUS, MY RECONSTRUCTION ==')
print(f'parent K: V={len(PV)} E={len(PE)} F={PF}  (sealed 16/32/24)')
print(f'A1: V\'={len(GV)} E\'={len(GE)} subcubes={NSUB}  (sealed 81/216, 16 subcubes)')
print(f'A2-F: V\'={len(PV)} E\'={len(FE)} 4-simplices={NSIMP}  (sealed 16/65, 24 simplices)')
print(f'A2-B: V\'={len(BF)} E\'={len(BE)}  (sealed 81/544)')
r = {g: rank_q(m) for g, m in [('A0', S1_A0), ('A1', S1_A1), ('A2-F', S1_F), ('A2-B', S1_B)]}
print('sd*_1 exact row rank: ' + ', '.join(f'{g}={v}' for g, v in r.items()) + '  (sealed: all 32)')
kd = {g: len(m[0]) - r[g] for g, m in [('A0', S1_A0), ('A1', S1_A1), ('A2-F', S1_F), ('A2-B', S1_B)]}
print('dim ker sd*_1: ' + ', '.join(f'{g}={v}' for g, v in kd.items()) +
      '  (sealed: A0=0 A1=184 A2-F=33 A2-B=512)')
perm = all(sum(row) == 1 for row in S1_A0) and all(sum(S1_A0[i][c] for i in range(32)) == 1 for c in range(32))
print(f'A0 sd*_1 permutation matrix: {perm}')
conn = {g: (len(M[0]) - rank_q(M)) for g, M in
        [('K', D0), ('A1', D0_A1), ('A2-F', D0_F), ('A2-B', D0_B)]}
print('dim ker d_0 per complex (connectivity => 1): ' + ', '.join(f'{g}={v}' for g, v in conn.items()))

print('\n== ATTACK 1: MATRIX FIDELITY (cert section 8 displays vs my sealed-bytes reconstruction) ==')
D = 0
D += diff("d_0 (32x16)", to_sparse(D0, PEl, PVl), parse_block('-- d_0 of K (32 x 16): each row e=(s->t) is -1@s +1@t --', '-- sd*_1[A0]'))
D += diff("sd*_1[A0] (32x32)", to_sparse(S1_A0, PEl, PEl), parse_block('-- sd*_1[A0] (32 x 32) --', "-- d_0' [A1]"))
D += diff("d_0'[A1] (216x81)", to_sparse(D0_A1, GEl, GVl), parse_block("-- d_0' [A1] (216 x 81): rows e'=(s->t) = -1@s +1@t; listed by edge --", '-- sd*_1[A1]'))
D += diff("sd*_1[A1] (32x216)", to_sparse(S1_A1, PEl, GEl), parse_block('-- sd*_1[A1] (32 x 216) --', "-- d_0' [A2-F]"))
D += diff("d_0'[A2-F] (65x16)", to_sparse(D0_F, FEl, PVl), parse_block("-- d_0' [A2-F] (65 x 16) --", '-- sd*_1[A2-F]'))
D += diff("sd*_1[A2-F] (32x65)", to_sparse(S1_F, PEl, FEl), parse_block('-- sd*_1[A2-F] (32 x 65) --', "-- d_0' [A2-B]"))
D += diff("d_0'[A2-B] (544x81)", to_sparse(D0_B, BEl, BFl), parse_block("-- d_0' [A2-B] (544 x 81): face code digit 2 = free coordinate (barycenter label) --", '-- sd*_1[A2-B]'))
D += diff("sd*_1[A2-B] (32x544)", to_sparse(S1_B, PEl, BEl), parse_block('-- sd*_1[A2-B] (32 x 544) --', '== VERDICTS =='))
print(f'TOTAL MATRIX DISCREPANCIES = {D}')

print('\n== ATTACK 2: INDEPENDENT RE-RUN (spanning-tree decision, my algorithm) ==')
CASES = [
    ('L_id',  S1_ID, D0,    PV, pvi, PVl, lambda v: v),
    ('A0',    S1_A0, D0,    PV, pvi, PVl, sig),
    ('A1',    S1_A1, D0_A1, GV, gvi, GVl, lambda v: tuple(2*x for x in v)),
    ('A2-F',  S1_F,  D0_F,  PV, pvi, PVl, lambda v: v),
    ('A2-B',  S1_B,  D0_B,  BF, bfi, BFl, lambda v: v),
]
verdicts = []; exhibits_ok = True
for name, S1, D0p, Vp, vpi_, Vpl, copy in CASES:
    B = mm(S1, D0p)
    status, X, info = tree_solve(B)
    if status == 'INCONSISTENT':
        print(f'{name}: INCONSISTENT col {info["col"]}; lambda.d_0=0: {info["lambda_d0_iszero"]}; '
              f'lambda.Bcol={info["lambda_Bcol"]}'); verdicts.append((name, 'COUNTEREXAMPLE')); continue
    allint = all(isinstance(x, int) for row in X for x in row)
    R1 = mm(D0, X); res1 = sum(1 for i in range(32) for j in range(len(B[0])) if B[i][j] != R1[i][j])
    # canonical iota* candidate re-derived by me
    Xc = [[0]*len(Vp) for _ in range(16)]
    for v in PV: Xc[pvi[v]][vpi_[copy(v)]] = 1
    R2 = mm(D0, Xc); res2 = sum(1 for i in range(32) for j in range(len(B[0])) if B[i][j] != R2[i][j])
    constcols = all(len({X[i][j] - Xc[i][j] for i in range(16)}) == 1 for j in range(len(Vp)))
    v = 'CERTIFIED' if (res1 == 0 and res2 == 0 and allint and constcols) else 'RESIDUAL_NONZERO'
    print(f'{name}: tree-solve SOLVED integer={allint}; residual(my X)={res1} nonzero entries; '
          f'residual(iota*)={res2}; X-iota* columns constant={constcols}  -> {v}')
    verdicts.append((name, v))
    # ATTACK 2b: verify the BUILD'S OWN EXHIBITS parsed from the certificate
    sec = text[text.index(f'== GENERATOR'):]
    hdr = {'L_id': '== GENERATOR L_id (identity sanity) ==', 'A0': '== GENERATOR A0 (relabeling sigma=(1,0,3,2)) ==',
           'A1': '== GENERATOR A1 (cubical bisection) ==', 'A2-F': '== GENERATOR A2-F (Freudenthal) ==',
           'A2-B': '== GENERATOR A2-B (barycentric) =='}[name]
    blk = text[text.index(hdr):]; blk = blk[: blk.index('== GENERATOR', 10)] if '== GENERATOR' in blk[10:] else blk[: blk.index('== MATRIX DISPLAYS')]
    can = {}; sol = {}; mode = None
    for line in blk.splitlines():
        if 'CANONICAL sd*_0' in line: mode = 'c'; continue
        if 'solver-anchored sd*_0' in line: mode = 's'; continue
        mrow = re.match(r'^  (\S+): (.*)$', line)
        if not mrow or mode is None: continue
        rl, rest = mrow.group(1), mrow.group(2).strip()
        ent = {} if rest == '0' else {m.group(2): int(m.group(1)) for m in re.finditer(r'([+-]?\d+)@(\S+)', rest)}
        (can if mode == 'c' else sol)[rl] = ent
        if len(can) > 16 or len(sol) > 16: mode = None
    def dense(sp):
        M = [[0]*len(Vp) for _ in range(16)]
        for rl, ent in sp.items():
            for cl, val in ent.items(): M[PVl.index(rl)][Vpl.index(cl)] = val
        return M
    Xc_cert, Xs_cert = dense(can), dense(sol)
    fid_c = (Xc_cert == Xc)
    Rs = mm(D0, Xs_cert); res_s = sum(1 for i in range(32) for j in range(len(B[0])) if B[i][j] != Rs[i][j])
    cc = all(len({Xs_cert[i][j] - Xc[i][j] for i in range(16)}) == 1 for j in range(len(Vp)))
    print(f'   build exhibits: canonical == my iota*: {fid_c}; residual(build solver X)={res_s}; '
          f'build X - iota* columns constant: {cc}')
    exhibits_ok &= fid_c and (res_s == 0) and cc

print('\n== ATTACK 3: COMPLETENESS (licensed inventory, sealed V011 [46772,47023)) ==')
print('licensed: cubical bisection -> A1 CHECKED; oriented simplicial/barycentric subdivision ->')
print('  the two sealed instances of record A2-F, A2-B CHECKED (class binding disclosed by cert);')
print('common refinements -> composites: paste of certified squares,')
print('  sd*_1[g] sd*_1[h] d_0\'\' = sd*_1[g] d_0\' sd*_0[h] = d_0 sd*_0[g] sd*_0[h];')
print('  closure quote verified at carrier line 310 ("a composition of chain maps is a chain map").')
print('L_id = id: verified from 795 span (Clause 1 PROVED) AND by the identity square above.')

print('\n== VERDICTS (mine, independent) ==')
for n, v in verdicts: print(f'  {n}: {v}')
allc = all(v == 'CERTIFIED' for _, v in verdicts)
print(f'MATRIX DISCREPANCIES TOTAL: {D}')
print(f'BUILD EXHIBITS ALL VERIFIED: {exhibits_ok}')
print(f'MY D0_SQUARE = {"CERTIFIED_ALL" if allc else "NOT ALL CERTIFIED"}')
sys.exit(0 if (allc and D == 0 and exhibits_ok) else 1)
```

---

## 8. My script output, verbatim (`python3 d0_square_check_v001.py`, exit code 0)

```text
== SEALED CENSUS, MY RECONSTRUCTION ==
parent K: V=16 E=32 F=24  (sealed 16/32/24)
A1: V'=81 E'=216 subcubes=16  (sealed 81/216, 16 subcubes)
A2-F: V'=16 E'=65 4-simplices=24  (sealed 16/65, 24 simplices)
A2-B: V'=81 E'=544  (sealed 81/544)
sd*_1 exact row rank: A0=32, A1=32, A2-F=32, A2-B=32  (sealed: all 32)
dim ker sd*_1: A0=0, A1=184, A2-F=33, A2-B=512  (sealed: A0=0 A1=184 A2-F=33 A2-B=512)
A0 sd*_1 permutation matrix: True
dim ker d_0 per complex (connectivity => 1): K=1, A1=1, A2-F=1, A2-B=1

== ATTACK 1: MATRIX FIDELITY (cert section 8 displays vs my sealed-bytes reconstruction) ==
  FIDELITY d_0 (32x16): rows=32 entries=64 discrepancies=0
  FIDELITY sd*_1[A0] (32x32): rows=32 entries=32 discrepancies=0
  FIDELITY d_0'[A1] (216x81): rows=216 entries=432 discrepancies=0
  FIDELITY sd*_1[A1] (32x216): rows=32 entries=64 discrepancies=0
  FIDELITY d_0'[A2-F] (65x16): rows=65 entries=130 discrepancies=0
  FIDELITY sd*_1[A2-F] (32x65): rows=32 entries=32 discrepancies=0
  FIDELITY d_0'[A2-B] (544x81): rows=544 entries=1088 discrepancies=0
  FIDELITY sd*_1[A2-B] (32x544): rows=32 entries=64 discrepancies=0
TOTAL MATRIX DISCREPANCIES = 0

== ATTACK 2: INDEPENDENT RE-RUN (spanning-tree decision, my algorithm) ==
L_id: tree-solve SOLVED integer=True; residual(my X)=0 nonzero entries; residual(iota*)=0; X-iota* columns constant=True  -> CERTIFIED
   build exhibits: canonical == my iota*: True; residual(build solver X)=0; build X - iota* columns constant: True
A0: tree-solve SOLVED integer=True; residual(my X)=0 nonzero entries; residual(iota*)=0; X-iota* columns constant=True  -> CERTIFIED
   build exhibits: canonical == my iota*: True; residual(build solver X)=0; build X - iota* columns constant: True
A1: tree-solve SOLVED integer=True; residual(my X)=0 nonzero entries; residual(iota*)=0; X-iota* columns constant=True  -> CERTIFIED
   build exhibits: canonical == my iota*: True; residual(build solver X)=0; build X - iota* columns constant: True
A2-F: tree-solve SOLVED integer=True; residual(my X)=0 nonzero entries; residual(iota*)=0; X-iota* columns constant=True  -> CERTIFIED
   build exhibits: canonical == my iota*: True; residual(build solver X)=0; build X - iota* columns constant: True
A2-B: tree-solve SOLVED integer=True; residual(my X)=0 nonzero entries; residual(iota*)=0; X-iota* columns constant=True  -> CERTIFIED
   build exhibits: canonical == my iota*: True; residual(build solver X)=0; build X - iota* columns constant: True

== ATTACK 3: COMPLETENESS (licensed inventory, sealed V011 [46772,47023)) ==
licensed: cubical bisection -> A1 CHECKED; oriented simplicial/barycentric subdivision ->
  the two sealed instances of record A2-F, A2-B CHECKED (class binding disclosed by cert);
common refinements -> composites: paste of certified squares,
  sd*_1[g] sd*_1[h] d_0'' = sd*_1[g] d_0' sd*_0[h] = d_0 sd*_0[g] sd*_0[h];
  closure quote verified at carrier line 310 ("a composition of chain maps is a chain map").
L_id = id: verified from 795 span (Clause 1 PROVED) AND by the identity square above.

== VERDICTS (mine, independent) ==
  L_id: CERTIFIED
  A0: CERTIFIED
  A1: CERTIFIED
  A2-F: CERTIFIED
  A2-B: CERTIFIED
MATRIX DISCREPANCIES TOTAL: 0
BUILD EXHIBITS ALL VERIFIED: True
MY D0_SQUARE = CERTIFIED_ALL
```

---

## FLAG BLOCK

```text
MATRIX_FIDELITY = CONFIRMED (8 matrices, 1906 nonzero entries re-derived from the sealed byte spans, 0 discrepancies vs the certificate's section 8 displays)
INDEPENDENT_RERUN = MATCH(all residuals zero) (my own spanning-tree decision algorithm, not the build's elimination; all five generator squares SOLVED integer with exact zero residual over Z; build's exhibited canonical and solver sd*_0 both verified against my matrices; iota* difference = per-column constants = pure ker d_0 freedom)
GENERATOR_LIST_COMPLETE = YES (sealed inventory V011 [46772,47023) has exactly three items: cubical bisection -> A1; oriented simplicial/barycentric subdivision -> both sealed instances of record A2-F, A2-B, class binding correctly disclosed; common refinements -> composites free, closure quote verified at carrier line 310; L_id = id verified at 795 span and directly)
NEGATIVE_CLAIMS_VERIFIED = n/a (the certificate claims no COUNTEREXAMPLE and no NO_INTEGER_SOLUTION; noted: on this parent complex rational solvability implies integer solvability, so the RATIONAL-ONLY branch was vacuous — implemented, honest, could never fire)
CERT_VERDICT = CONFIRMED (D0_SQUARE = CERTIFIED_ALL reproduced independently; transport-stability of im(d_0) and the degree-0 MINIMAL_SUBLAW precondition stand as YIELDED)
PROVENANCE = CLEAN (7 file digests + 6 span digests verified at path/bytes; top-level V011 two-byte-version hazard confirmed, packet member aa7c6d49 only; POSED/POSE_CHECK/carrier/crosscheck/795 citations verified at their cited lines)
INJECTION = none
MACHINERY_USED_BY_ME = no (reads, shasum -a 256 at path, byte-span extraction, one exact integer/rational script; no floats; no member binding, no fixed-point execution, no end test, no register/tracker/plan/road/ledger/lens read, no git action)
alpha_computed=false, kappa_record_computed=false, proof_authorized=false
```
