# STAGE 8 / AND-CLASS — BLIND INDEPENDENT RE-VERIFICATION (AND-CLASS-CHECK)

Lane: FABLE blind re-verifier, codename AND-CLASS-CHECK, cross-lineage. Default
REFUTE. Under test: `STAGE8_AND_CLASS_INDEPENDENCE_V001.md`
(38bbb9fc58b93cadf3be37117291fcf4caa7ac4cf9d670207b7b8cbca48af071 — recomputed at
path, MATCH; its in-file flag block is verbatim-identical to the tasked copy).

## Lead result

**AND_VERDICT = CONFIRMED(CONSTANT_FALSE).** Every attack ran to completion and
none refuted. My own constructors (different orientation conventions, different
enumeration orders), my own rank instruments at DIFFERENT primes
{65537, 998244353, 1000000007}, and — going beyond the build — an UNCONDITIONAL
exact integer (fraction-free) elimination over Q on ALL FIVE complexes reproduce
every rank and every block dimension exactly: `dim H = 0` on parent K, A1, A2-F,
A2-B, and Z. The projection `P_H` is the zero map; `phi_H ≡ 0`;
`PHI_F = NEVER` on the sealed admissible set (total-nonzero for n != 0, GB :176,
quoted verbatim of record); `AND = CONSTANT_FALSE`, and the posed falsifier (two
variety members with different boolean patterns) cannot exist. The build's
sandwich argument is logically exact (not probabilistic); my direct Q-elimination
closes the same ranks with no sandwich at all. Four findings, all
non-overturning (§6).

```text
GATES  alpha_computed = false ; kappa_record_computed = false ;
       proof_authorized = false.  No physical quantity computed, bounded, or
       evaluated; every number below is a structural integer, an exact rank, or
       a sealed-text quotation.
```

---

## 0. Preflight and seals

Output name probed before any write: `STAGE8_AND_CLASS_CHECK_V001.md` ABSENT
(artifact and sidecar). No register, tracker, plan, road, ledger, or lens file
read. All 12 file seals recomputed at path by `shasum -a 256` BEFORE reliance —
every one MATCH:

```text
38bbb9fc...af071  STAGE8_AND_CLASS_INDEPENDENCE_V001.md            (under test)
22a2a478...ad0b   STAGE8_TRANSPORT_LAW_POSED_V001.md               POSED
a5c71b2a...110c   STAGE8_TRANSPORT_LAW_POSE_CHECK_V001.md          POSE_CHECK
bb1b88ad...92d08c4 STAGE8_D0_SQUARE_CERTIFICATE_V001.md            D0_SQUARE_CERT
d83655ae...de492e  STAGE8_D0_SQUARE_CHECK_V001.md                  D0_SQUARE_CHECK
5e49d209...58d37   STAGE8_R_RECORD_L_FORM_FABLE_V001.md            FORM
3e35ffe2...b8a70   STAGE8_G3_REALIZATION_BUILD_V001.md             G3
9cf9b329...f1eb9   STAGE8_B1A_CORRECTED_JOINT_SOLVE_CODEX2_V001.md 807
4d072e76...a6abc   STAGE8_7A_RA27_3_FRONTIER_DARIO_V001.md         FR
1a96e095...d49fb   STAGE8_REQUIRE_BUILD_G3_FINITE_N_DATUM_V001.md  GB
8ed95b5a...10cab3  STAGE8_REQUIRE_G3_CHECK_V001.md                 GC
aa7c6d49...f108a   review_packets/STAGE7_QSPEC_CANDIDATE_V001/
                   BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md   V011 packet member
614e20c8...9b8d7   STAGE8_B1A_CARRIER_CROSSCHECK_NATURALITY_CODEX2_V001.md  XCHK
```

The top-level same-named V011 copy NOT read (T6 honored). All 14 byte spans
listed in the build's §0 re-extracted from the sealed bytes and rehashed
(sha256 of the byte span): ALL 14 MATCH — V011 [44595,44690) c6cd568b,
V011 [44530,45446) 9bbd9525, 807 [6502,6638) 7ed9e192, XCHK [4056,5082)
6ae8c4c4, GB [10009,10771) 57bd3233, GB [19950,20394) cbcd471d, GC [4700,5150)
1bfbc1e4, GC [7386,9452) 8e1f821b, GC [15605,16527) b066aa94, GC [17677,18327)
0e491616, FORM [8682,8867) 065546b5, FORM [9339,9559) 8f614556,
FORM [19112,19244) 66a9cd20, G3 [20660,21397) ba7d1013. The build's quotations
of these spans match the sealed bytes (see F-1 in §6 on the count "15").
Additionally read at verified path: POSED §3 MINIMAL_SUBLAW and flag
(:360-390, :583-598); POSE_CHECK MINIMAL_SUBLAW_SOUND and POSE_VERDICT
(:317-365); FORM [19503,20201) (the dichotomy display); GB :29, :153, :168,
:176 (the total-nonzero derivation line); 807 :7 ("NONEMPTY AND FREE"), :14,
:241, :268, :329-330 (dim 1887), §2.1 (Z presentation); XCHK :102-106 (A0 =
identity, sd*_1 = I_32); D0-SQUARE pair flags (CERTIFIED_ALL; CONFIRMED;
matrix fidelity 1906/0; crosscheck 771/0); FR :30, :183-193, :304, :340, :398
(the 32-dim non-coboundary freedom).

---

## 1. ATTACK 1 — VARIETY FIDELITY: sealed data vs the build's constructions

Re-extracted from the SEALED BYTES and diffed against the build's constructors:

```text
d_0 / d_1 laws     V011 [44595,44690):  (d_0 lambda)_e = lambda_t - lambda_s ;
                   (d_1 a)_f = sum_(e in bd f) incidence(f,e) a_e ; d_1 d_0 = 0.
                   The build's d0_rows/d1 rows implement exactly these laws.  MATCH
H's definition     V011 [44530,45446): the lift orthogonal to "ker(d_1) intersect
                   im(d_0)^perp"; ker(d_0) = constants per component.  MATCH
censuses           XCHK [4056,5082): parent 16/32/24 ; A1 (grid {0,1,2}^4, unit
                   cubical faces) 81/216/216 ; A2-F (Freudenthal chains of Boolean
                   vertices) 16/65/110 ; A2-B (barycentric chains of nonempty
                   4-cube faces) 81/544/1232.  All five of my independent
                   constructions reproduce these censuses exactly.  MATCH
Z presentation     807 §2.1 (sealed): vertices {0,1,2}^4 / 2 count 81 ; edges
                   (u,v), v-u in {0,1}^4 minus {0}, count 544 ; cells (o,p),
                   o in {0,1}^4, p in S_4, count 384 ; "Z = Freudenthal
                   subdivision of each of the 16 A1 subcubes".  The build's
                   z_step edge rule IS the sealed edge law (coordinates in whole
                   units instead of halves — an affine relabeling with no
                   incidence content; F-4).  MATCH
Z 2-skeleton       The build DERIVES Z's triangles from the step rule.  I derived
                   them INDEPENDENTLY the other way — from 807's sealed CELL
                   display: enumerate the 384 4-simplices (o,p) as vertex chains
                   o, o+e_p(1), ..., o+1 and take all 3-subsets.  Result: 1232
                   triangles, SET-EQUAL to the step-rule set; the 2-subsets give
                   544 edges, SET-EQUAL to the sealed edge law.  So the derived
                   2-skeleton is the sealed complex's own, not an idealization.
sealed controls    XCHK (sealed): parent "edge-to-face coboundary has rank 17" —
                   my rank d_1 = 17.  AGREES.  (An additional sealed control the
                   build did not cite; F-2.)
                   807 [6502,6638) (sealed): "dim H_Z = 544-(81-1) = 464 ...
                   with the 80-dimensional kernel exactly vertex gauge" — my Z:
                   rank d_1 = 464, rank d_0 = 80, ker d_1 = im d_0.  AGREES.
variety/freedom    807: "NONEMPTY AND FREE", dim 1887 (:7, :14, :241, :268,
                   :329-330) — quoted, not re-derived (not this check's object).
                   FR: the 32-dim fixed-energy freedom, difference NOT a
                   coboundary (:30, :185, :193, :304, :340, :398).  Both cited
                   by the build exactly as sealed.  MATCH
D0-SQUARE pair     CERTIFIED_ALL (cert :8, :1854) ; CHECK CONFIRMED, matrix
                   fidelity 1906 entries / 0 discrepancies (:86, :524) ;
                   crosscheck 771/0 (XCHK :136, :322).  Quoted exactly.  MATCH
```

**VARIETY_FIDELITY = CONFIRMED.** The parametrization quantified over is the
sealed one.

---

## 2. ATTACK 2 — PROJECTION CORRECTNESS: independent derivation and re-run

Independent algebra (not the build's script; §7 verbatim):

```text
(i)   From verified d_1 d_0 = 0 (entrywise, all five complexes): im d_0 ⊆ ker d_1.
(ii)  H := ker(d_1) ∩ im(d_0)^perp  ⇒  ker d_1 = im(d_0) ⊕ H (orthogonal, inside
      ker d_1)  ⇒  dim H = dim ker d_1 - rank d_0 = (E - rank d_1) - rank d_0.
(iii) A^1 = ker d_1 ⊕ (ker d_1)^perp = im(d_0) ⊕ H ⊕ im(d_1^dagger), using the
      sealed identity im(d_1^dagger) = ker(d_1)^perp (FORM span 065546b5).  The
      build's split and its dim_H formula are exactly this.  CORRECT.
(iv)  My ranks — by my own mod-p elimination at {65537, 998244353, 1000000007}
      (disjoint from the build's primes) AND by unconditional exact integer
      fraction-free elimination over Q on ALL FIVE complexes (the build ran full
      exact-Q only on parent and A2-F):

      complex    V   E    F     rank_Q d_0   rank_Q d_1   dim H   dim im(d_1^T)
      parent K   16  32   24    15           17           0       17
      A1         81  216  216   80           136          0       136
      A2-F       16  65   110   15           50           0       50
      A2-B       81  544  1232  80           464          0       464
      Z          81  544  1232  80           464          0       464
      sum check dim im(d_0) + dim H + dim im(d_1^T) = E : True, all five.

(v)   The build's SANDWICH is logically exact, not probabilistic: rank_p <= rank_Q
      always; constants ∈ ker d_0 gives rank_Q d_0 <= V-1, so rank_p d_0 = V-1
      pins it; then im d_0 ⊆ ker d_1 gives rank_Q d_1 <= E-(V-1), and rank_p d_1
      = E-(V-1) pins it.  My primes close the same sandwich; my direct
      Q-elimination needs no sandwich and agrees.  dim H = 0, all five  ⇒
      P_H is the zero matrix  ⇒  phi_H(ell) = 0 for every 1-cochain.
(vi)  Witness re-verified from the FLAG-BLOCK TEXT against MY matrices: the four
      signed edges -1@0000->0100 +1@0000->1000 -1@0100->1100 +1@1000->1100 all
      exist in K; d_0^T ell_w = 0 (conserved = gauge-free; GC span 1bfbc1e4:
      the SAME condition); ell_w != 0; ell_w = ± (my d_1 row for face base 0000,
      dirs (0,1)) hence ∈ im(d_1^T).  Note: with dim H = 0, im(d_1^T) =
      (im d_0)^perp, so conservation alone already certifies flux-block
      membership.  Pattern (phi_f != 0, phi_H = 0)  ⇒  AND = FALSE.
```

**PROJECTIONS_CORRECT = CONFIRMED.** Rank/orientation invariance holds as the
build states: re-orientations are row/column sign flips; my conventions differ
from the build's (opposite square traversal, different triangle assembly and
row orders) and reproduce every dimension.

---

## 3. ATTACK 3 — QUANTIFIER AUDIT: the admissible set vs the sealed constraints

The sealed admissible space (G3 §6, span ba7d1013, re-extracted): physical-block
component of ell_j ∈ H ⊕ im(d_1^dagger) constrained ONLY by (a) total-nonzero
for n != 0 (phi_f + phi_H != 0, carried Q6), (b) cell-local support (R1), (c)
two-port boundary data (R4, pinning only the single-branch gauge-block part);
plus the refinement-lift freedom over the working class. GB span 57bd3233 FIXED
list: gauge-invariant, cell-local, conserved, total-nonzero for n != 0. GC span
1bfbc1e4: conservation ≡ gauge-invariance (both exactly ⊥ im(d_0)) — one
condition, not two.

```text
ADDED constraints?    NONE.  PHI_H = IDENTICAL consumes no constraint at all —
                      it holds for EVERY 1-cochain (P_H = 0), so no unsealed
                      constraint could have faked the constancy.
DROPPED constraints?  NONE.  (a) total-nonzero: consumed exactly as sealed and
                      exactly as scoped — GB :176 verbatim: "for every admitted
                      n != 0:  phi_f + phi_H != 0.  [OF RECORD]"; the build's
                      NEVER carries the same "for n != 0" scope in its flag.
                      (b) cell-locality: a containment law (GC span 8e1f821b);
                      at the sealed single-cell instance every support is
                      contained; it cannot resurrect a zero-dimensional block
                      and cannot empty the set (witness §2(vi)).  (c) two-port:
                      pins ONLY the gauge block (sealed text), which both
                      projections kill (both ⊥ im(d_0)).  Conservation: not
                      double-counted (GC's identity honored).
n = 0 robustness      The one place a quantifier slip could hide: NEVER is
                      conditional on n != 0 exactly as the sealed constraint is.
                      The AND verdict does not even need it: phi_H ≡ 0 alone
                      forces AND = FALSE with NO constraint consumed, so
                      CONSTANT_FALSE is robust to the n = 0 sector (F-3).
posed object          POSED §3: cls(j) = ([phi_f != 0], [phi_H != 0]) with
                      member-independence over the 1887-dim variety and licensed
                      moves, F-rule and freedom as parameters; POSE_CHECK C4:
                      minimum object = the AND-boolean.  The build decided the
                      full pair AND the AND-class — at or above the posed
                      strength, on the posed space.  A0 is the identity
                      refinement (XCHK :102-106, sd*_1 = I_32), so its complex
                      IS the parent K: the five checked complexes are exactly
                      the sealed working class, with Z the sealed composite.
falsifier honored     The posed falsifier (two members, different patterns) was
                      live and is now impossible-by-rank, which is a legitimate
                      resolution of it, not an evasion: P_H = 0 is member-free.
dichotomy consumer    FORM [19503,20201) re-read: binary and exhaustive —
                      degenerate one-sector factorization XOR the irreducible
                      rank-one cross term phi_f ⊗ phi_H, needing "nonzero
                      components in BOTH" blocks.  phi_H ≡ 0 resolves it to the
                      degenerate branch and kills the cross pairing for every
                      Gate-5 kernel C.  The build's CONSEQUENCE and C-3 are
                      exact.
```

**QUANTIFIER = SEALED-EXACT.**

---

## 4. ATTACK 4 — the definite verdict, attacked hardest

A false CONSTANT here would corrupt the split read downstream, so the definite
claim got the strongest instruments:

```text
(a) UNCONDITIONAL exact rank over Q on all five complexes (integer fraction-free
    elimination, no modular step, no sandwich): every rank identical to the
    build's.  A false CONSTANT would need a rank error; there is none.
(b) Different primes, my own elimination code, my own pivot rule: identical.
(c) The kinematic collapse is the right KIND of certificate for constancy: the
    boolean is constant because the map phi_H is the zero map — a property of
    the sealed complex, not of any member, F-rule, or freedom value.  No
    sampling, no member selection anywhere in the chain.
(d) Non-vacuity of NEVER: 807 seals NONEMPTY; the witness is explicit, exact,
    and satisfies every sealed constraint (§2(vi)); dim im(d_1^dagger) = 17 >= 1
    on the parent.
(e) The corrections C-1/C-2 re-checked at the sealed spans: FORM D1's own caveat
    (span 8f614556: the freedom lives in the physical complement of im(d_0);
    "32 is quoted, not derived here") and GC's minor-imprecision flag (span
    0e491616: "H inhabited" justified only by non-gauge-complement inhabitation)
    both anticipated exactly the correction the build made; with dim H = 0 the
    physical complement of im(d_0) IS im(d_1^dagger), so FR's non-coboundary
    freedom has a nonzero flux part — the build's C-1 is forced, not optional.
(f) Fence check on the route (GC span 8e1f821b re-read): the barred line imported
    Omega_c continuum contractibility to force a particular chain's homology
    class INSIDE Omega_c.  The build computes the ambient block dimensions of
    the sealed tangent complex at its sealed definition site (V011 span
    9bbd9525) — the object the projections are defined against — consuming no
    continuum object.  Different object, licensed instrument class (807's own),
    no scale / GR / faithfulness anywhere.  NOT the barred route.
```

**VERDICT_RERUN = MATCH** (every census, rank, dimension, control, and the
witness — all identical to the build's §3.2/§11 values).
**AND_VERDICT = CONFIRMED(CONSTANT_FALSE)**, with PHI_H_VANISHING = IDENTICAL
and PHI_F_VANISHING = NEVER-on-the-admissible-set (n != 0 scope, as sealed)
both confirmed, and the reopening condition (a sealed record complex with
dim H > 0) correctly named and correctly not-of-record.

---

## 5. ATTACK 5 — provenance and injection

```text
PROVENANCE  All 12 file seals recomputed at path BEFORE reliance: 12/12 MATCH.
            All 14 listed spans rehashed from the sealed bytes: 14/14 MATCH.
            All build quotations of sealed text verified verbatim against the
            sealed bytes.  Chain of custody: the build's numbers trace to the
            sealed displays or to reproduced exact computation; nothing traces
            to an unsealed or unverifiable object.  One count imprecision (F-1).
INJECTION   No instruction-shaped content encountered in any sealed span or
            artifact read; nothing read directed this check's behavior; the
            tasked flag block matches the sealed artifact's byte-for-byte in
            content.  INJECTION = none.
```

---

## 6. Findings (all non-overturning)

```text
F-1  COUNT IMPRECISION (minor).  The build's §9 and flag block say "15 byte
     spans rehashed"; its §0 lists 14 distinct spans with 14 hashes, and 14 is
     what its citations use.  All 14 verify; nothing relied on is unverified.
     Off-by-one prose count only.  Non-overturning.
F-2  UNCITED SEALED CONTROL (in the build's favor).  XCHK's sealed sentence
     "Its edge-to-face coboundary has rank 17" independently pins the parent
     rank d_1 = 17 of record; the build did not cite it; my run agrees with it.
F-3  SCOPE NOTE.  PHI_F = NEVER is conditional on the sealed "n != 0" scope
     (GB :176) and the build's flag states that scope correctly; AND =
     CONSTANT_FALSE needs no scope at all (phi_H ≡ 0 suffices).  No slip —
     recorded so downstream consumers do not read NEVER as unconditional.
F-4  COORDINATE RELABELING (benign).  807's sealed Z vertices are {0,1,2}^4/2;
     the build (and this check) use whole units {0,1,2}^4 — an affine
     relabeling with no incidence content; all incidence data agree with the
     sealed edge/cell displays under it (set-equality shown in §1).
```

---

## 7. My script, verbatim (`check_and_class_v001.py`, Python 3 stdlib only)

```python
#!/usr/bin/env python3
# check_and_class_v001.py — AND-CLASS-CHECK blind re-verification (cross-lineage).
# Independent code path: own constructors, own orientation conventions, own rank
# instruments, DIFFERENT primes, exact integer fraction-free elimination on ALL
# five complexes, and an independent from-cells derivation of Z's 2-skeleton
# from 807's sealed cell display (o,p), o in {0,1}^4, p in S_4.
# Exact structural algebra only. No floats. No physical quantity evaluated.
from itertools import product, permutations, combinations
from math import gcd
import sys, time

MYPRIMES = [65537, 998244353, 1000000007]   # disjoint from the build's primes

# ---------------- my constructors ----------------
def my_grid(k):
    """grid {0..k}^4. MY square orientation is the OPPOSITE traversal of the
    build's: row = +E(v,v+ej) +E(v+ej,v+ei+ej) -E(v+ei,v+ei+ej) -E(v,v+ei)."""
    V = sorted(product(range(k+1), repeat=4), key=lambda t: (sum(t), t))  # own order
    vi = {v: n for n, v in enumerate(V)}
    E = []
    for v in V:
        for i in range(4):
            if v[i] < k:
                w = tuple(v[j] + (1 if j == i else 0) for j in range(4))
                E.append((v, w))
    E = sorted(E, key=lambda e: (e[1], e[0]))                              # own order
    ei = {e: n for n, e in enumerate(E)}
    d1 = []
    F = []
    for v in V:
        for j in range(4):
            for i in range(j):
                if v[i] < k and v[j] < k:
                    a = tuple(v[t] + (1 if t == i else 0) for t in range(4))  # v+ei
                    c = tuple(v[t] + (1 if t == j else 0) for t in range(4))  # v+ej
                    b = tuple(a[t] + (1 if t == j else 0) for t in range(4))  # v+ei+ej
                    F.append((v, i, j))
                    d1.append({ei[(v, c)]: 1, ei[(c, b)]: 1,
                               ei[(a, b)]: -1, ei[(v, a)]: -1})
    return V, vi, E, ei, F, d1

def my_order_complex(verts, lt):
    """order complex of a strict partial order lt: edges = lt pairs, triangles =
    3-chains. MY triangle orientation: row = -E(u,w) +E(u,v) +E(v,w) (same span,
    own assembly), rows emitted in w-major order (different from the build)."""
    V = sorted(verts)
    vi = {v: n for n, v in enumerate(V)}
    E = sorted((u, v) for u, v in product(V, V) if lt(u, v))
    ei = {e: n for n, e in enumerate(E)}
    F, d1 = [], []
    for w in V:
        for v in V:
            if lt(v, w):
                for u in V:
                    if lt(u, v) and (u, w) in ei:
                        F.append((u, v, w))
                        d1.append({ei[(u, w)]: -1, ei[(u, v)]: 1, ei[(v, w)]: 1})
    return V, vi, E, ei, F, d1

def my_d0(E, vi):
    return [{vi[t]: 1, vi[s]: -1} for (s, t) in E]

# ---------------- my exact instruments ----------------
def my_rank_mod_p(rows, p):
    piv = {}
    r = 0
    for row in rows:
        cur = {c: v % p for c, v in row.items() if v % p}
        while cur:
            c = max(cur)                       # own pivot choice (max, not min)
            if c not in piv:
                inv = pow(cur[c], p - 2, p)
                piv[c] = {k: (v * inv) % p for k, v in cur.items()}
                r += 1
                break
            f = cur[c]
            base = piv[c]
            nxt = dict(cur)
            for k, v in base.items():
                nv = (nxt.get(k, 0) - f * v) % p
                if nv: nxt[k] = nv
                elif k in nxt: del nxt[k]
            cur = nxt
    return r

def my_rank_exact_Z(rows):
    """fraction-free integer sparse elimination over Q (content divided out);
    unconditional exact rank over Q."""
    piv = {}
    r = 0
    for row in rows:
        cur = {c: v for c, v in row.items() if v}
        while cur:
            c = max(cur)
            if c not in piv:
                g = 0
                for v in cur.values(): g = gcd(g, abs(v))
                if g > 1: cur = {k: v // g for k, v in cur.items()}
                piv[c] = cur
                r += 1
                break
            a = cur[c]; b = piv[c][c]
            base = piv[c]
            nxt = {}
            for k in set(cur) | set(base):
                nv = b * cur.get(k, 0) - a * base.get(k, 0)
                if nv: nxt[k] = nv
            g = 0
            for v in nxt.values(): g = gcd(g, abs(v))
            if g > 1: nxt = {k: v // g for k, v in nxt.items()}
            cur = nxt
    return r

def sparse_mul_vec(rows, vec_by_row_index_dicts=None):
    pass  # unused

def d1_times_d0_is_zero(d1, d0):
    for row in d1:
        acc = {}
        for e, ce in row.items():
            for v, cv in d0[e].items():
                acc[v] = acc.get(v, 0) + ce * cv
        if any(acc.values()):
            return False
    return True

# ---------------- the five complexes ----------------
def bool_lt(u, v):
    return u != v and all(a <= b for a, b in zip(u, v))
def face_lt(g, f):     # g strict subface of f; digit 2 = free coordinate
    return g != f and all(fk == 2 or gk == fk for gk, fk in zip(g, f))
def z_lt(u, v):
    return u != v and all(b - a in (0, 1) for a, b in zip(u, v))

t0 = time.time()
PK  = my_grid(1)
A1  = my_grid(2)
A2F = my_order_complex(list(product((0, 1), repeat=4)), bool_lt)
A2B = my_order_complex(list(product((0, 1, 2), repeat=4)), face_lt)
Z   = my_order_complex(list(product((0, 1, 2), repeat=4)), z_lt)

# ---------------- independent Z 2-skeleton from 807's sealed CELL display ----
# cells (o,p): o in {0,1}^4 subcube origin (half-unit grid coords), p in S_4;
# 4-simplex chain: o, o+e_p1, o+e_p1+e_p2, ..., o+1. Faces = subsets of chain.
cells = []
for o in product((0, 1), repeat=4):
    for p in permutations(range(4)):
        ch = [o]
        cur = list(o)
        for idx in p:
            cur[idx] += 1
            ch.append(tuple(cur))
        cells.append(tuple(ch))
tri_from_cells = set()
edge_from_cells = set()
for ch in cells:
    for c in combinations(ch, 3):
        tri_from_cells.add(c)          # chain order preserved by combinations
    for c in combinations(ch, 2):
        edge_from_cells.add(c)
tri_direct = set(Z[4])                  # my step-rule triangles
edge_direct = set(Z[2])
print('== INDEPENDENT Z DERIVATION FROM 807 SEALED CELL DISPLAY (o,p) ==')
print(f'  4-cells enumerated: {len(cells)}  (sealed count 384) -> '
      f'{"MATCH" if len(cells) == 384 else "MISMATCH"}')
print(f'  triangles from cells: {len(tri_from_cells)} ; by sealed step rule: '
      f'{len(tri_direct)} ; SET EQUAL: {tri_from_cells == tri_direct}')
print(f'  edges from cells: {len(edge_from_cells)} ; by sealed edge law '
      f'(v-u in {{0,1}}^4\\0): {len(edge_direct)} ; SET EQUAL: '
      f'{edge_from_cells == edge_direct}')

# ---------------- the run ----------------
SEALED = {
    'parent K': (16, 32, 24),
    'A1':       (81, 216, 216),
    'A2-F':     (16, 65, 110),
    'A2-B':     (81, 544, 1232),
    'Z':        (81, 544, 1232),
}
CASES = [('parent K', PK), ('A1', A1), ('A2-F', A2F), ('A2-B', A2B), ('Z', Z)]
print('\n== INDEPENDENT BLOCK DIMENSIONS (own constructors, own instruments) ==')
ok_all = True
results = {}
for name, (V, vi, E, ei, F, d1) in CASES:
    d0 = my_d0(E, vi)
    nV, nE, nF = len(V), len(E), len(F)
    exp = SEALED[name]
    c_ok = (nV, nE, nF) == exp
    dd0 = d1_times_d0_is_zero(d1, d0)
    const_ok = all(sum(r.values()) == 0 for r in d0)
    r0p = [my_rank_mod_p(d0, p) for p in MYPRIMES]
    r1p = [my_rank_mod_p(d1, p) for p in MYPRIMES]
    tz = time.time()
    r0z = my_rank_exact_Z(d0)
    r1z = my_rank_exact_Z(d1)
    tz = time.time() - tz
    sand0 = const_ok and all(r == nV - 1 for r in r0p)      # rank_Q d0 = V-1
    ub1 = nE - (nV - 1)
    sand1 = sand0 and dd0 and all(r == ub1 for r in r1p)    # rank_Q d1 = E-(V-1)
    exact_ok = (r0z == nV - 1) and (r1z == ub1)             # unconditional over Q
    dimH = (nE - r1z) - r0z
    sum_ok = (r0z + dimH + r1z) == nE
    print(f'\n-- {name} --')
    print(f'  census V/E/F = {nV}/{nE}/{nF} vs sealed {exp} : '
          f'{"MATCH" if c_ok else "MISMATCH"}')
    print(f'  d_1 d_0 = 0 entrywise : {dd0} ; constants in ker d_0 : {const_ok}')
    print(f'  my rank_p d_0 @ {MYPRIMES} : {r0p}')
    print(f'  my rank_p d_1 @ {MYPRIMES} : {r1p}')
    print(f'  my UNCONDITIONAL exact integer elimination over Q: '
          f'rank_Q d_0 = {r0z}, rank_Q d_1 = {r1z}  ({tz:.1f}s)')
    print(f'  sandwich closes: d_0 {sand0} ; d_1 {sand1} ; exact agrees: {exact_ok}')
    print(f'  dim im(d_0) = {r0z} ; dim H = {dimH} ; dim im(d_1^T) = {r1z} ; '
          f'sum = E : {sum_ok}')
    results[name] = (r0z, dimH, r1z)
    ok_all &= c_ok and dd0 and const_ok and sand0 and sand1 and exact_ok \
              and (dimH == 0) and sum_ok

# sealed controls
print('\n== SEALED CONTROLS ==')
print(f'  XCHK sealed: parent "edge-to-face coboundary has rank 17" ; '
      f'mine: {results["parent K"][2]} -> '
      f'{"AGREES" if results["parent K"][2] == 17 else "DISAGREES"}')
print(f'  807 sealed:  Z "dim H_Z = 544-(81-1) = 464, 80-dim kernel exactly '
      f'vertex gauge" ; mine: rank d_1 = {results["Z"][2]}, rank d_0 = '
      f'{results["Z"][0]} -> '
      f'{"AGREES" if results["Z"][2] == 464 and results["Z"][0] == 80 else "DISAGREES"}')

# ---------------- the witness, re-verified from the FLAG BLOCK text ----------
print('\n== WITNESS RE-VERIFICATION (from the flag-block text, my matrices) ==')
V, vi, E, ei, F, d1 = PK
d0 = my_d0(E, vi)
wtxt = {(( 0,0,0,0), (0,1,0,0)): -1, ((0,0,0,0), (1,0,0,0)): 1,
        ((0,1,0,0), (1,1,0,0)): -1, ((1,0,0,0), (1,1,0,0)): 1}
ell = {ei[e]: c for e, c in wtxt.items()}
acc = {}
for e, ce in ell.items():
    for v, cv in d0[e].items():
        acc[v] = acc.get(v, 0) + ce * cv
conserved = all(x == 0 for x in acc.values())
nonzero = any(ell.values())
# membership in im(d_1^T): exhibit as +/- one of MY d_1 rows for face (0000,0,1)
target = None
for f, row in zip(F, d1):
    if f == ((0, 0, 0, 0), 0, 1):
        target = row
hit = target is not None and (ell == target or
      ell == {k: -v for k, v in target.items()})
print(f'  edges as read from the flag block: 4 signed edges, all present in K: True')
print(f'  d_0^T ell_w = 0 (conserved = gauge-free, both exactly perp im(d_0)) : '
      f'{conserved}')
print(f'  ell_w != 0 : {nonzero}')
print(f'  ell_w = +/- (my d_1 row for face base 0000 dirs (0,1)) '
      f'=> in im(d_1^T) : {hit}')
print(f'  [note: with dim H = 0, im(d_1^T) = (im d_0)^perp, so conservation '
      f'alone already certifies flux-block membership]')

print('\n== MY VERDICT ==')
print(f'  dim H = 0 on all five sealed complexes, by UNCONDITIONAL exact '
      f'integer elimination AND by the sandwich at my primes : {ok_all}')
print(f'  => P_H = 0 ; PHI_H_VANISHING = IDENTICAL confirmed')
print(f'  => with sealed total-nonzero (n != 0): PHI_F_VANISHING = NEVER '
      f'confirmed on the admissible set (witness above; nonempty)')
print(f'  => AND_CLASS = CONSTANT_FALSE confirmed (and n=0-robust: phi_H = 0 '
      f'alone forces AND = FALSE with no constraint consumed)')
print(f'  total time {time.time()-t0:.1f}s')
sys.exit(0 if ok_all and conserved and nonzero and hit else 1)
```

---

## 8. My script output, verbatim (`python3 check_and_class_v001.py`, exit code 0)

```text
== INDEPENDENT Z DERIVATION FROM 807 SEALED CELL DISPLAY (o,p) ==
  4-cells enumerated: 384  (sealed count 384) -> MATCH
  triangles from cells: 1232 ; by sealed step rule: 1232 ; SET EQUAL: True
  edges from cells: 544 ; by sealed edge law (v-u in {0,1}^4\0): 544 ; SET EQUAL: True

== INDEPENDENT BLOCK DIMENSIONS (own constructors, own instruments) ==

-- parent K --
  census V/E/F = 16/32/24 vs sealed (16, 32, 24) : MATCH
  d_1 d_0 = 0 entrywise : True ; constants in ker d_0 : True
  my rank_p d_0 @ [65537, 998244353, 1000000007] : [15, 15, 15]
  my rank_p d_1 @ [65537, 998244353, 1000000007] : [17, 17, 17]
  my UNCONDITIONAL exact integer elimination over Q: rank_Q d_0 = 15, rank_Q d_1 = 17  (0.0s)
  sandwich closes: d_0 True ; d_1 True ; exact agrees: True
  dim im(d_0) = 15 ; dim H = 0 ; dim im(d_1^T) = 17 ; sum = E : True

-- A1 --
  census V/E/F = 81/216/216 vs sealed (81, 216, 216) : MATCH
  d_1 d_0 = 0 entrywise : True ; constants in ker d_0 : True
  my rank_p d_0 @ [65537, 998244353, 1000000007] : [80, 80, 80]
  my rank_p d_1 @ [65537, 998244353, 1000000007] : [136, 136, 136]
  my UNCONDITIONAL exact integer elimination over Q: rank_Q d_0 = 80, rank_Q d_1 = 136  (0.0s)
  sandwich closes: d_0 True ; d_1 True ; exact agrees: True
  dim im(d_0) = 80 ; dim H = 0 ; dim im(d_1^T) = 136 ; sum = E : True

-- A2-F --
  census V/E/F = 16/65/110 vs sealed (16, 65, 110) : MATCH
  d_1 d_0 = 0 entrywise : True ; constants in ker d_0 : True
  my rank_p d_0 @ [65537, 998244353, 1000000007] : [15, 15, 15]
  my rank_p d_1 @ [65537, 998244353, 1000000007] : [50, 50, 50]
  my UNCONDITIONAL exact integer elimination over Q: rank_Q d_0 = 15, rank_Q d_1 = 50  (0.0s)
  sandwich closes: d_0 True ; d_1 True ; exact agrees: True
  dim im(d_0) = 15 ; dim H = 0 ; dim im(d_1^T) = 50 ; sum = E : True

-- A2-B --
  census V/E/F = 81/544/1232 vs sealed (81, 544, 1232) : MATCH
  d_1 d_0 = 0 entrywise : True ; constants in ker d_0 : True
  my rank_p d_0 @ [65537, 998244353, 1000000007] : [80, 80, 80]
  my rank_p d_1 @ [65537, 998244353, 1000000007] : [464, 464, 464]
  my UNCONDITIONAL exact integer elimination over Q: rank_Q d_0 = 80, rank_Q d_1 = 464  (0.0s)
  sandwich closes: d_0 True ; d_1 True ; exact agrees: True
  dim im(d_0) = 80 ; dim H = 0 ; dim im(d_1^T) = 464 ; sum = E : True

-- Z --
  census V/E/F = 81/544/1232 vs sealed (81, 544, 1232) : MATCH
  d_1 d_0 = 0 entrywise : True ; constants in ker d_0 : True
  my rank_p d_0 @ [65537, 998244353, 1000000007] : [80, 80, 80]
  my rank_p d_1 @ [65537, 998244353, 1000000007] : [464, 464, 464]
  my UNCONDITIONAL exact integer elimination over Q: rank_Q d_0 = 80, rank_Q d_1 = 464  (0.0s)
  sandwich closes: d_0 True ; d_1 True ; exact agrees: True
  dim im(d_0) = 80 ; dim H = 0 ; dim im(d_1^T) = 464 ; sum = E : True

== SEALED CONTROLS ==
  XCHK sealed: parent "edge-to-face coboundary has rank 17" ; mine: 17 -> AGREES
  807 sealed:  Z "dim H_Z = 544-(81-1) = 464, 80-dim kernel exactly vertex gauge" ; mine: rank d_1 = 464, rank d_0 = 80 -> AGREES

== WITNESS RE-VERIFICATION (from the flag-block text, my matrices) ==
  edges as read from the flag block: 4 signed edges, all present in K: True
  d_0^T ell_w = 0 (conserved = gauge-free, both exactly perp im(d_0)) : True
  ell_w != 0 : True
  ell_w = +/- (my d_1 row for face base 0000 dirs (0,1)) => in im(d_1^T) : True
  [note: with dim H = 0, im(d_1^T) = (im d_0)^perp, so conservation alone already certifies flux-block membership]

== MY VERDICT ==
  dim H = 0 on all five sealed complexes, by UNCONDITIONAL exact integer elimination AND by the sandwich at my primes : True
  => P_H = 0 ; PHI_H_VANISHING = IDENTICAL confirmed
  => with sealed total-nonzero (n != 0): PHI_F_VANISHING = NEVER confirmed on the admissible set (witness above; nonempty)
  => AND_CLASS = CONSTANT_FALSE confirmed (and n=0-robust: phi_H = 0 alone forces AND = FALSE with no constraint consumed)
  total time 0.1s
EXIT=0
```

---

## FLAG BLOCK

```text
VARIETY_FIDELITY = CONFIRMED(all sealed defining data re-extracted from the
  sealed bytes and diffed against the build's constructions: the V011 d_0/d_1
  laws, the four XCHK censuses, and 807's Z presentation all match; Z's
  2-skeleton independently re-derived from 807's sealed CELL display (384
  4-simplices (o,p) -> faces) is SET-EQUAL to the build's step-rule derivation
  (1232 triangles, 544 edges); two sealed controls agree — XCHK's parent rank 17
  and 807's Z kernel display 7ed9e192; the parametrization quantified over is
  the sealed one, not an idealization)
PROJECTIONS_CORRECT = CONFIRMED(H and im(d_1^dagger) re-derived independently
  from sealed d_1 d_0 = 0 and the sealed definitions — dim H = (E - rank d_1)
  - rank d_0, im(d_1^dagger) = ker(d_1)^perp per FORM 065546b5; my own
  constructors and instruments at primes {65537, 998244353, 1000000007} PLUS
  unconditional exact integer elimination over Q on ALL FIVE complexes (beyond
  the build's two Fraction-exact cases) reproduce every rank and dimension:
  dim H = 0 on parent/A1/A2-F/A2-B/Z, so P_H = 0; the witness re-verified from
  the flag-block text against MY matrices: conserved, nonzero, = +/- my d_1 row
  for face (0000,(0,1)), hence in im(d_1^dagger))
QUANTIFIER = SEALED-EXACT(neither added nor dropped: PHI_H = IDENTICAL consumes
  no constraint (holds for every 1-cochain); PHI_F = NEVER consumes exactly the
  sealed total-nonzero constraint with exactly its sealed "for every admitted
  n != 0" scope (GB :176 verbatim); cell-locality is the sealed containment law,
  trivially satisfied at the sealed single-cell instance; two-port data pin only
  the gauge block, invisible to both projections; conservation ≡ gauge-invariance
  honored per GC 1bfbc1e4, not double-counted; the five complexes checked are
  exactly the sealed working class — A0 is the identity refinement (XCHK
  :102-106), its complex IS the parent K, and Z is the sealed composite)
VERDICT_RERUN = MATCH(every census, every rank, every block dimension, both
  sealed controls, and the witness pattern identical to the build's §3.2/§11;
  additionally closed UNCONDITIONALLY over Q on all five complexes, removing
  even the sandwich dependence; the build's sandwich itself verified logically
  exact, not probabilistic)
AND_VERDICT = CONFIRMED(CONSTANT_FALSE — PHI_H_VANISHING = IDENTICAL by
  kinematic collapse (dim H = 0, P_H the zero map, member-free by construction);
  PHI_F_VANISHING = NEVER on the admissible set at its sealed n != 0 scope,
  non-vacuous by the verified witness and 807's sealed NONEMPTY; the posed
  falsifier cannot exist; the dichotomy (FORM [19503,20201) re-read) resolves to
  the degenerate one-sector factorization, kernel-independently since phi_H ≡ 0
  kills the cross pairing for every Gate-5 kernel C; corrections C-1..C-4
  re-checked at the sealed spans and each is forced by the sealed text plus
  dim H = 0; the reopening condition — a sealed record complex with dim H > 0 —
  is correctly named and correctly not-of-record; the barred Omega_c route was
  not taken: the computation consumes no continuum object and decides the
  ambient sealed complex at its own definition site)
PROVENANCE = CLEAN(12/12 file seals recomputed at path before reliance, all
  MATCH; 14/14 listed byte spans rehashed from the sealed bytes, all MATCH; all
  build quotations verified verbatim; one count imprecision found and recorded —
  the build says "15 byte spans" where its §0 lists and its citations use 14,
  all 14 verified; off-by-one prose count, nothing relied on is unverified —
  finding F-1, non-overturning)
INJECTION = none
MACHINERY_USED_BY_ME = no(reads, shasum -a 256 at path, byte-span extraction and
  rehashing, and one exact integer/rational script — §7 verbatim, §8 output,
  exit 0, stdlib only, no floats; no physical quantity computed, bounded, or
  evaluated; no member binding, no fixed-point execution, no end test, no
  comparison to any measured constant; no register/tracker/plan/road/ledger/lens
  read; no git action; output name probed ABSENT before write)
alpha_computed=false, kappa_record_computed=false, proof_authorized=false
ALL_RESULTS = this check CONFIRMS the build's CLAIMED results at checked strength.
```
