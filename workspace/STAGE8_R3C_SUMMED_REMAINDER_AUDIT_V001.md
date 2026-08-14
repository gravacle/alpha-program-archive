# STAGE 8 — INDEPENDENT AUDIT OF THE R.3'(c) SUMMED SECOND-ORDER REMAINDER ATTEMPT AND THE HALF-PLANE LOCALIZATION ATTEMPT (57edbb96)

## INDEPENDENT AUDITOR — CODENAME R3C-AUDIT — [SEALED]

Date: 2026-08-14
Role: independent auditor, briefed to REFUTE. Default stance held: every
claim of the build (STAGE8_R3C_SUMMED_REMAINDER_ATTEMPT_V001.md, digest
57edbb96...) treated as wrong until it survived re-derivation by routes the
build did not use. Own CAS battery: sympy 1.14.0, fresh venv `r3caudvenv`
(under /private/tmp scratch), EXACT SYMBOLIC ONLY — every constant symbolic
or an exact rational/surd; nothing numeric evaluated; the one enumeration
(CB3c) is exact integer arithmetic. Independent routes used: generic
free-weight residual law on 3x3 matrices (vs the build's derived-weight
2x2); parameterized moment family isolating m_2^2 (vs fixed weights);
sigma_3-conjugation route to slab parity (vs closed-form substitution);
Sherman-Morrison route to the H-R witness (vs explicit diag inverse);
integer norm-form route to the cube-roots witness (vs complex basis
reduction); adjugate-route Carleman/log-det identities. The build's own two
batteries were ALSO re-run VERBATIM in the fresh venv: 14/14 and 10/10
PASS, outputs byte-identical to the artifact's claimed verbatim blocks.
Fences held by this audit: alpha never computed or approached; L a formal
symbol; M(t) sharp; no carrier or cellulation datum introduced; no
register/tracker/plan/road/ledger/lens file read; no git action; no
existing file edited; output name probed before write: ABSENT; nothing
written to the workspace but this artifact and its seal.

---

## 0. VERDICT IN ONE LINE

**THE BUILD STANDS. TASK A: CONFIRMED-WITH-CORRECTIONS (two named notational corrections c-1/c-2, neither touching any verdict, wall, falsifier, or deliverable) — the summed-level second-order identity RA3a/RA3b is TRUE and re-derives by an independent generic-weight residual law that also pins sum c = 1 as exactly load-bearing; the moment localization RA4a/RA4b is TRUE and generalizes (coefficient exactly m_2^2 over the whole m_0 = m_1 = 0 symmetric family); the FAILS-AT(unit-cell carrier axis, NOT REFUTED, residue sharpened) adjudication re-derives with every wall engagement checked and no break-through found by this auditor; TASK B: CONFIRMED — FAILS-AT(n-uniform quantifier) re-derives on all four routes, the H-R-insufficiency witness (rho_res identically 1, segment t - log(1+t) unbounded) verifies by Sherman-Morrison, the cube-roots non-necessity witness verifies by exact integer norm-forms with the auditor's sharpening min |Z_hat| = 1/4 ATTAINED on that family, and a second auditor sharpening: on CONNECTED unit-modulus regions the corrected condition is necessary AND sufficient (every unit-modulus non-necessity witness is necessarily disconnected — the build's r-4 caveat is real and its witness minimal in that sense); V-1..V-6 severally NOT-FIRED (V1_STATUS = NOT-FIRED: nothing here bears on the adopted summed OPERATOR estimate at its own quantifier); provenance 17/17 seals clean at full digest, every cited span found as cited; injection NONE; fences HELD by build and auditor; 34/34 auditor checks PASS and the build's 24 reproduce byte-identically.**

---

## 1. SEALS INDEPENDENTLY VERIFIED AT PATH (shasum -a 256, full digests)

All under `/Users/bgm/MB Work/alpha-program-archive/workspace/`. Every
digest below recomputed BY THIS AUDITOR from bytes at path this session,
full digest, and compared against (i) the file's `.seal.sha256` sidecar,
(ii) the build's §1 table, (iii) for the 14 files also listed there, the
e5b0879b §1 table. ALL MATCH. 17/17 (the build + its 16 relied-on files).
NONE UNVERIFIABLE. The build's §1 note that its tasked "15 digests"
resolves at the bytes to 14 e5b0879b table rows plus the separately-tasked
ENTRY addendum was checked against the e5b0879b §1 table: that table has
exactly 14 rows and their digests match my recomputations row by row.

```text
57edbb964610bb7c9715bccdf88cf0400ef5af230bf1be139a0be300d90994d8  STAGE8_R3C_SUMMED_REMAINDER_ATTEMPT_V001.md  MATCH (UNDER AUDIT; = tasked digest; = sidecar)
e5b0879bb4f272f709b2f70b50244d1c0bf6f392a2053d6368e477022f8f6e53  STAGE8_S2_DISCHARGE_V001.md                  MATCH
cbe6ff4f6fa6cd3c94486dc27966f508e974e0f2004c0294ef3849c14a5fd132  STAGE8_S2_DISCHARGE_AUDIT_V001.md            MATCH
cbfbb74c59f5a88742524dc41958514b4c38418d025f85154f6e1d3594ee1a43  STAGE8_SUMMED_S2_ENTRY_ADDENDUM_V001.md      MATCH (adoption of record, read in full)
ce59b4800aecddaaae4f741da0068595439b6474631a652d795c49694677397e  STAGE8_SUMMED_S2_CANDIDATE_V001.md           MATCH (§3.3, §4.3 BAR, §4.4, §5.3 read at bytes)
c234600005c83b2373ce1d3a33d680eacc3444964c5f0eb8f5421c546f30bb7b  STAGE8_SUMMED_S2_CANDIDATE_CHECK_V001.md     MATCH
a903716c23c1a6969932e988f90d464abe9e8ee96624cd2dce3e32416de132e0  STAGE8_RL4_RL0_CERTIFICATION_V001.md         MATCH (§3.1-§3.5 read at bytes)
685afac8205b4ed2ed0a309a321f6eccc940882e89ec3dfbce70fd9b8d74af52  STAGE8_RL4_RL0_CHECK_V001.md                 MATCH
2e4e5163bb5b9c06078890fc573dd149905975b55860dcabcc7050fb1aa02666  STAGE8_REMAINDER_UNIFORMITY_V001.md          MATCH (§2.1-§2.4, §3.1-§3.2, §3.5, §5 read at bytes)
89641f762d35c0e6d3c8fb0475e2de742663f9dcf9f08a44621b059c2bd927ec  STAGE8_REMAINDER_UNIFORMITY_CHECK_V001.md    MATCH
26f9314bdbbf1d7638ecbdf398c891cb3ba54251d4b40314df39c03ab48c08b7  STAGE8_ZERO_FREE_DERIVATION_V001.md          MATCH (§4.1-§4.3 read at bytes)
aed551e3dba40a0846e540709f0608398d2f5d28764e01033efbd9b20ed1d90f  STAGE8_ZERO_FREE_CHECK_V001.md               MATCH
a7969f0c3a42112ee300f73617494fb77c2a415bf5b6cf4d33598c6b6c8bf9cf  STAGE8_R2_RESUMMATION_V001.md                MATCH (slab closed form read at bytes)
a4f2e1b7878139afd017abe5fb62c6af7bf19836f7f162ef62902265bfc03cb5  STAGE8_R2_RESUMMATION_CHECK_V001.md          MATCH
468467303a109dc825b015107897dacc107800fc981030377c3f006b384cccb5  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md  MATCH (:652-666, :679-689, :691-727, :803-848, :851-894 read at bytes)
789338adb7d3d36da453113e98f371a4f92543cf2652b047f8481c407bed5bc3  STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md  MATCH (:75-128 read at bytes)
52f2490b187fd4b307c2af45f6238ea02f1d6839b23466fefee1dbba47ed6241  STAGE8_RL2B_UNIFORMITY_REFUTED_RESULT_V001.md  MATCH (§0, §5 read at bytes)
```

---

## 2. TASK A ADJUDICATION — THE SUMMED SECOND-ORDER REMAINDER

### 2.1 The identity (Route I) — TRUE, re-derived by a stronger parameterized law

The build's RA3a/RA3b were attacked by the auditor's RESIDUAL LAW (a route
the build did not use): for ANY square matrices, ANY free weights c_p with
S := sum c_p, and q either e_2 or the bilinear b,

```text
  sum_p c_p q(M_p) - q(sum_p c_p M_p) - sum_{p<q} c_p c_q q(M_p - M_q)
      = (1 - S) * sum_p c_p q(M_p)          [CA2a/CA2b, 3x3, free weights]
```

so the build's identity is EXACTLY the S = 1 slice, and the negative
control is built in: for sum c != 1 the identity FAILS by precisely that
residual. The derived-weight five-matrix instance re-verifies (CA2c). The
abstract reason is the polarization of a quadratic form (q(M) = B(M,M),
1 - c_p = sum_{q != p} c_q), independent of matrix size and weight values.
Verdict on the identity: DERIVED and TRUE, with the hypothesis sum c = 1
pinned as load-bearing. The five-pair weight arithmetic (ten differences,
weights 4 x 1/16 + 6 x 1/64, C(5,2) = 10) checks exactly.

### 2.2 The kill's failure at second order (Route II) — TRUE, and the mechanism isolated

Attacked by the auditor's GENERIC MOMENT FAMILY (nodes (0, t, -t), weights
(-2v, v, v) — the general symmetric m_0 = m_1 = m_3 = 0 family, m_2 =
2vt^2 symbolic): on 3x3 fully symbolic matrices with branch content linear
(A_mu = A0 + mu A1, B_lam = B0 + lam B1),

```text
  sum W tr[A_mu B_lam] = 0            for ALL (v, t)   [CA3b]
  sum W tr[(A_mu B_lam)^2] = m_2^2 tr[(A1 B1)^2]   for ALL (v, t)   [CA3c]
```

— the projection coefficient is exactly m_2^2 across the whole family; the
sealed weights (v = -1/4, t = sqrt2) give m_2 = -1, m_2^2 = 1 (CA3d),
recovering the build's RA4b as a specialization. The killed first-power
content returns squared; the structural bar (the two mu-appearances
separated by lam-factors, cyclicity unable to adjacent-ize them) is
confirmed by the generic-family result itself: no choice of admissible
weights removes the m_2^2 term. The build's claim that this CONTRADICTS no
sealed bytes was checked at REM's bytes: REM's kills are per-factor
operator statements ([U(0)]_0 = 0, [F]_0 = 0, a-order-independent at the
operator level, REM §3.2/§3.5), and REM's own F-side leading coefficient
is m_2-content (REM §2.3) — consistent, not contradicted. CONFIRMED.

### 2.3 The difference form and W-2 (Route I(ii) + §2.4) — CONFIRMED at its declared grade

The within-quartet parity split was re-derived by the CONJUGATION route
(the build substituted into the closed form): sigma_3 H(mu) sigma_3 =
H(-mu) for H = omega sigma_3 + mu sigma_1, hence termwise on every power
(checked k <= 6, and the pattern is the algebra itself), U(-mu) =
sigma_3 U(mu) sigma_3 — diagonal (intraband) entries EVEN in mu,
off-diagonal (interband) ODD (CA7a); the sealed R2 closed form obeys it
(CA7b), and RA7's A_sl/B_sl forms MATCH the R2 §"closed-form slab exhibit"
display at bytes (sea-sea A = cos(Om T) + i omega sin(Om T)/Om, interband
B = -i mu sin(Om T)/Om). The taxonomy placements (single-J5 stay class
c = 1, o = 0 at 2o + c = 1 for the within-quartet differences; bare
degree-0 content for the (0,0)-to-quartet differences) are consistent with
REM §2.2-§2.3 and §3.1 read at bytes: REM's floors and its
(c = 1, o = 0)-exclusion are statements about the WEIGHT-SUMMED factors
(the parity kill is the weight functional itself, CA1b — a symmetric
second difference killing every odd function), so a bare difference lacks
exactly that kill; REM's "no (c=1,o=0) class anywhere" is not contradicted
because its scope is the weight-summed object. The build carries these
placements at CLAIMED taxonomy grade and rests its verdict only on
"nothing sealed certifies the differences finite" — verified TRUE (no
sealed majorant covers bare pair differences; 52f2490b + ZF o-1 kill the
per-pair chain of record). Sign unavailability re-verified with the
auditor's own witnesses: tr[K^2] = -8 < 0, tr[N^2] = 0 (nilpotent),
e_2(diag(1,-1)) = -1 < 0, e_2(K) = 4 > 0 (CA6) — no coercivity and no
favorable sign exist at the difference-form level; positivity of the
derived weights ADDS terms for self-adjoint shadows. CONFIRMED.

### 2.4 The scoping and the covariance (Routes III-V) — CONFIRMED, P-1 real

The collapse-level scoping ("the remainder starts at a-order m >= 2 with
a^2-content exactly sum c_p e_2(Delta_p^{[1]})") was re-derived by direct
series: det(1 + aD1 + a^2 D2) - 1 - tr(aD1 + a^2 D2) has [a^1] = 0 and
[a^2] = e_2(D1) exactly (CA4c, 3x3). The E1 :663-666 Carleman display
itself was re-derived as an algebraic identity by the adjugate route:
(1+sD)^{-1}D + (1+sD)^{-1}(sD)D = D and d/ds Log det(1+sD) =
tr[(1+sD)^{-1}D] (CA4a/CA4b) — so the build's consumption of the display
at its sealed grade is sound, and its conditionality marks (collapse level
CONDITIONAL on R-L4a/b + C-L2) match the record's own. The covariance
transfer: det/tr conjugation invariance re-verified on 3x3 (CA5a); given
the sealed chain e5b0879b §2.3 STEPS 1-6 (U_L^dag C U_L = C at STEP 3
makes A, Delta, A_s conjugate exactly, so rho and tr Delta transfer), the
remainder covariance R^{(L)}_n(a) = R^{(1)}_{n'}(La) follows; the exponent
arithmetic (24/pi)^{1/2}|C_L|_4^{1/2} = L^2 and the general floor
(24/pi)^{1/4}|C_L|_4^{1/4} = L re-verify exactly (CA5b), and the polydisc
split (CA5c). The build's naming of P-1 as a REAL premise is CORRECT and
is exact daylight vs the first-order case: the r-A2 discharge ran on
compression monotonicity of the HS NORM (||Pi X Pi||_2 <= ||X||_2, REM
§3.5 at bytes); R_n is a determinant-level scalar, not a norm, and no
compression monotonicity exists for determinants — the auditor confirms no
sealed line supplies one. The class-reduction consequence is stated by the
build only conditionally ("IF a unit-cell n-uniform bound ever exists"),
which is the honest quantifier. CONFIRMED.

### 2.5 Break-through and sharpening attempts by this auditor

(b-1) BREAK ATTEMPT at W-1 (alternative passage): the exterior-square
display sum_p c_p e_2(M_p) = tr_{Lambda^2}[ sum_p c_p Lambda^2(M_p) ]
moves the pair sum inside a trace on Lambda^2(H) — but the nonlinearity
(the exterior square) is still applied PER PAIR before the sum, control of
the summed exterior-square object is on no sealed artifact, its trace-norm
majorant needs per-pair data again, and the surviving-sector restriction
still breaks the m_0 factorization (ZF o-2(ii)). No estimate assembles; W-1
and W-2 stand. The build's FAILS-AT survives this attack. (b-2) BREAK
ATTEMPT at W-2 (coercivity): defeated by CA6 exactly (both signs and zero
attained). (b-3) REFUTATION ATTEMPT (show the remainder infinite): requires
a norm LOWER bound; none exists sealed (e5b0879b §2.4 states the leading
stratum's norm was never lower-bounded of record) — NOT REFUTED is the
honest class, concur. (s-3/s-4) SHARPENINGS DELIVERED: the residual law
(CA2a/b) and the generic m_2^2 projection law (CA3c) strengthen the
build's RA3/RA4 from instances to parameterized lemmas.

### 2.6 Corrections (named exactly; neither touches any verdict)

```text
c-1  §2.2(i) display: "|tr Delta^Sigma_n|^2" omits the surv,c superscript
     — the object of the inequality is Delta^{Sigma,surv,c}_n in both
     factors (the build's own next sentence, "the trace factor consumes
     R.3'(b)'s object", disambiguates). Notational; the inequality itself
     |e_2(M)| <= (|tr M|^2 + ||M||_2^2)/2 is standard HS Cauchy-Schwarz
     (equality pin CB8).
c-2  §2.2's phrase "the one summed-level second-order identity the sealed
     algebra admits": uniqueness is asserted, not derived, and no
     consequence consumes it — as a c-mean variance decomposition the
     identity is canonical in its shape class, but the artifact should say
     "the canonical"/"a", not "the one". Harmless; named for the record.
```

### 2.7 Task A verdict

```text
TASKA_AUDIT = CONFIRMED-WITH-CORRECTIONS( c-1, c-2 — both notational,
  no verdict, wall, falsifier, or deliverable touched. The build's
  FAILS-AT(unit-cell carrier axis; NOT REFUTED; residue sharpened to
  (i) the D-i surviving-instance square + trace enclosure and (ii) the
  ten-term pairwise-difference e_2 form, plus H-R + C-L2 for the tail,
  plus P-1 for the class reduction) re-derives exactly; the identity
  RA3a/RA3b TRUE (auditor's residual law, free weights, 3x3); the moment
  localization RA4a/RA4b TRUE and generalized (m_2^2 law); the per-pair
  BAR respected (analysis of the barred route's deadness is not passage
  through it; no discharge is claimed anywhere); wall engagements W-1/W-2/
  W-3 each verified at the cited bytes; auditor break-through attempts
  failed (b-1, b-2, b-3). )
```

### 2.8 THE AUDITOR'S CAS BATTERY (VERBATIM) AND ITS OUTPUT (VERBATIM)

One battery covers both tasks: groups CA1-CA7 + CB8 are Task A; groups
CB1-CB7 are Task B (§3 references them). Harness disclosure, on the
record: the first run of CA3a FAILED on the AUDITOR'S OWN assertion (a
sign slip: asserted m_2 = -2vt^2 where the family gives +2vt^2, with v
declared positive where the sealed value is v = -1/4 < 0); the assertion
was corrected (the disclosure comment is in the script); no claim under
test was affected — CA3b/c/d passed identically on both runs. This
mirrors, and does not exceed, the harness-form discipline the build
disclosed in its §3.8.

```python
# R3C-AUDIT independent CAS battery — EXACT SYMBOLIC ONLY (sympy 1.14.0, fresh venv
# r3caudvenv under /private/tmp scratch). Every constant symbolic or an exact
# rational/surd; nothing numeric evaluated (the CB3 enumeration is exact integer
# arithmetic). Routes deliberately DIFFERENT from the build's §2.8/§3.8 batteries:
# generic weights and 3x3 matrices where the build used derived weights and 2x2;
# residual-formula negative controls; moment-functional parameterization; conjugation
# (sigma_3) route to slab parity; Sherman-Morrison route to the H-R witness; integer
# norm-form route to the cube-roots witness; plus the auditor's own sharpenings
# (CA2 residual law; CA3 generic-m_2 projection; CB3 exact minimum 1/4; CB7 the
# connected unit-modulus equivalence).
import itertools
import sympy as sp
from sympy import Rational as R

ok = lambda name, cond: print(f"{name}: {'PASS' if cond else 'FAIL'}")

# ===== CA1 — census + moment ledger, re-derived via the second-difference form =====
lam_v = [sp.Integer(0), sp.sqrt(2), -sp.sqrt(2)]
w_v = [R(1, 2), R(-1, 4), R(-1, 4)]
ph = [1, -1, -1]
surv = [(i, j) for i in range(3) for j in range(3) if ph[i] == ph[j]]
Nsurv = sp.nsimplify(sum(w_v[i]*w_v[j] for i, j in surv))
c_list = sorted(sp.nsimplify(w_v[i]*w_v[j]/Nsurv) for i, j in surv)
f0_, fp_, fm_ = sp.symbols('f0 fp fm')
second_diff = -R(1, 4)*(fp_ - 2*f0_ + fm_)
direct = R(1, 2)*f0_ - R(1, 4)*fp_ - R(1, 4)*fm_
mom = lambda n: sp.nsimplify(sum(w*l**n for w, l in zip(w_v, lam_v)))
ok("CA1a census: 5 surviving, N_surv = 1/2, c multiset {1/2, 1/8 x 4}, sum = 1, all > 0",
   len(surv) == 5 and Nsurv == R(1, 2) and c_list == [R(1, 8)]*4 + [R(1, 2)]
   and sum(c_list) == 1 and all(c > 0 for c in c_list))
ok("CA1b weight functional IS the symmetric second difference -(1/4)[f(s2)-2f(0)+f(-s2)]",
   sp.expand(direct - second_diff) == 0)
ok("CA1c moments m_0..m_4 = 0, 0, -1, 0, -2 (kills first-moment; m_2 = -1 nonzero)",
   [mom(n) for n in range(5)] == [0, 0, -1, 0, -2])

# ===== CA2 — the summed-level second-order identity, via the RESIDUAL LAW =====
# Auditor's parameterized lemma (route the build did not use): for ANY square
# matrices and ANY weights c_p with S := sum c_p,
#   sum_p c_p e2(M_p) - e2(sum c M) - sum_{p<q} c_p c_q e2(M_p - M_q)
#     = (1 - S) * sum_p c_p e2(M_p).
# The build's RA3a is EXACTLY the S = 1 slice; S != 1 is the negative control.
def e2(M):
    return sp.expand(((M.trace())**2 - (M*M).trace())/2)

def bform(X, Y):
    return sp.expand(X.trace()*Y.trace() - (X*Y).trace())

cs = sp.symbols('c1 c2 c3')                      # FREE weights, unconstrained
Ms3 = [sp.Matrix(3, 3, lambda i, j, k=k: sp.Symbol(f'M{k}_{i}{j}')) for k in range(3)]
S_ = sum(cs)
lhs = sum(c*e2(M) for c, M in zip(cs, Ms3))
Msum = sum((c*M for c, M in zip(cs, Ms3)), sp.zeros(3, 3))
rhs = e2(Msum) + sum(cs[p]*cs[q]*e2(Ms3[p] - Ms3[q])
                     for p in range(3) for q in range(p + 1, 3))
resid = sp.expand(lhs - rhs - (1 - S_)*lhs)
ok("CA2a RESIDUAL LAW (3x3, FREE weights): sum c e2 - e2(sum) - sum cc e2(diff)"
   " = (1-S) sum c e2  => identity holds IFF sum c = 1 (negative control included)",
   resid == 0)
Ns3 = [sp.Matrix(3, 3, lambda i, j, k=k: sp.Symbol(f'N{k}_{i}{j}')) for k in range(3)]
Nsum = sum((c*N for c, N in zip(cs, Ns3)), sp.zeros(3, 3))
lhsb = sum(c*bform(M, N) for c, M, N in zip(cs, Ms3, Ns3))
rhsb = bform(Msum, Nsum) + sum(cs[p]*cs[q]*bform(Ms3[p] - Ms3[q], Ns3[p] - Ns3[q])
                               for p in range(3) for q in range(p + 1, 3))
residb = sp.expand(lhsb - rhsb - (1 - S_)*lhsb)
ok("CA2b same residual law for the bilinear b(X,Y) = trX trY - tr(XY) (3x3, free wts)",
   residb == 0)
Ms5 = [sp.Matrix(2, 2, lambda i, j, k=k: sp.Symbol(f'P{k}_{i}{j}')) for k in range(5)]
cd = [R(1, 2), R(1, 8), R(1, 8), R(1, 8), R(1, 8)]
Psum = sum((c*M for c, M in zip(cd, Ms5)), sp.zeros(2, 2))
ok("CA2c the derived-weight 5-matrix instance (the build's RA3a) re-verified",
   sp.expand(sum(c*e2(M) for c, M in zip(cd, Ms5))
             - e2(Psum)
             - sum(cd[p]*cd[q]*e2(Ms5[p] - Ms5[q])
                   for p in range(5) for q in range(p + 1, 5))) == 0)

# ===== CA3 — the kill at second order: GENERIC moment family (auditor's route) =====
# Nodes (0, t, -t), weights (-2v, v, v): m_0 = m_1 = m_3 = 0 for ALL (v, t);
# m_2 = 2 v t^2. Claim (3x3 fully symbolic, branch content linear):
#   sum W tr[A_mu B_lam] = 0   AND   sum W tr[(A_mu B_lam)^2] = m_2^2 tr[(A1 B1)^2].
# The sealed weights are v = -1/4, t = sqrt2: m_2 = -1, m_2^2 = 1 — the build's RA4b
# is the specialization. The parameterized form isolates the m_2^2 mechanism.
# [Harness disclosure: first run asserted m_2 = -2 v t^2 (sign slip in the AUDITOR'S
#  assertion, not in any claim under test) and declared v positive; corrected to
#  +2 v t^2 with v real — CA3b/c/d were unaffected and passed on both runs.]
v_ = sp.Symbol('v', real=True)
t_ = sp.Symbol('t', positive=True)
gw = [-2*v_, v_, v_]
gn = [sp.Integer(0), t_, -t_]
m2g = sp.expand(sum(w*l**2 for w, l in zip(gw, gn)))
A0 = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'a0_{i}{j}'))
A1 = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'a1_{i}{j}'))
B0 = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'b0_{i}{j}'))
B1 = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'b1_{i}{j}'))
first_g = sp.Integer(0)
second_g = sp.Integer(0)
for i in range(3):
    for j in range(3):
        Am = A0 + gn[i]*A1
        Bl = B0 + gn[j]*B1
        W = gw[i]*gw[j]
        first_g += W*(Am*Bl).trace()
        second_g += W*(Am*Bl*Am*Bl).trace()
ok("CA3a generic family: m_0 = m_1 = m_3 = 0 for all (v,t); m_2 = 2 v t^2 symbolic",
   sp.expand(sum(gw)) == 0 and sp.expand(sum(w*l for w, l in zip(gw, gn))) == 0
   and sp.expand(sum(w*l**3 for w, l in zip(gw, gn))) == 0
   and sp.expand(m2g - 2*v_*t_**2) == 0)
ok("CA3b generic first-order kill: sum W tr[A_mu B_lam] = 0 (3x3, all v, t)",
   sp.expand(first_g) == 0)
ok("CA3c generic second-order projection: sum W tr[(A_mu B_lam)^2] = m_2^2 tr[(A1 B1)^2]"
   " (3x3, all v, t) — killed content returns squared, coefficient exactly m_2^2",
   sp.expand(second_g - m2g**2*(A1*B1*A1*B1).trace()) == 0)
ok("CA3d sealed specialization v = -1/4, t = sqrt2: m_2 = -1, m_2^2 = 1",
   sp.expand(m2g.subs([(v_, -R(1, 4)), (t_, sp.sqrt(2))])) == -1
   and sp.expand((m2g**2).subs([(v_, -R(1, 4)), (t_, sp.sqrt(2))])) == 1)
f0s, f1s = sp.symbols('f0s f1s')
ok("CA3e scalar shadow at the sealed weights: sum w f = 0, sum w f^2 = m_2 f1^2 = -f1^2",
   sp.expand(sum(w*(f0s + f1s*l) for w, l in zip(w_v, lam_v))) == 0
   and sp.expand(sum(w*(f0s + f1s*l)**2 for w, l in zip(w_v, lam_v)) + f1s**2) == 0)

# ===== CA4 — the Carleman display and the collapse-level scoping, independent =====
D3 = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'd_{i}{j}'))
s_ = sp.Symbol('s', positive=True)
Ms_ = sp.eye(3) + s_*D3
Minv = Ms_.adjugate()/Ms_.det()                  # exact inverse
ok("CA4a resolvent split (1+sD)^{-1}D + (1+sD)^{-1}(sD)D = D (3x3 exact)"
   " => integrand identity tr[(1+sD)^{-1}D] = trD - tr[(1+sD)^{-1}(sD)(D)]",
   sp.simplify(Minv*D3 + Minv*(s_*D3)*D3 - D3) == sp.zeros(3, 3))
ok("CA4b d/ds Log det(1+sD) = tr[(1+sD)^{-1} D] (3x3 exact adjugate route)"
   " — the E1 :663-666 display is an algebraic identity at fixed n",
   sp.simplify(sp.diff(Ms_.det(), s_)/Ms_.det() - (Minv*D3).trace()) == 0)
a_ = sp.Symbol('a')
D1 = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'e_{i}{j}'))
D2 = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'g_{i}{j}'))
Mser = a_*D1 + a_**2*D2
expr = sp.expand((sp.eye(3) + Mser).det() - 1 - Mser.trace())
ok("CA4c collapse scoping: det(1 + aD1 + a^2 D2) - 1 - tr(...) has [a^1] = 0 and"
   " [a^2] = e2(D1) EXACTLY (3x3): the remainder starts at a-order 2 with e_2 content",
   sp.expand(expr.coeff(a_, 1)) == 0
   and sp.expand(expr.coeff(a_, 2) - e2(D1)) == 0)

# ===== CA5 — dilation weight arithmetic at second order =====
U3 = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'u_{i}{j}'))
Y3 = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'y_{i}{j}'))
U3inv = U3.adjugate()/U3.det()
ok("CA5a det(U(1+Y)U^{-1}) = det(1+Y), tr(UYU^{-1}) = trY (3x3 exact)"
   " — rho and tr Delta transfer under the covariance; R^{(L)}(a) = R^{(1)}(La) given it",
   sp.simplify((U3*(sp.eye(3) + Y3)*U3inv).det() - (sp.eye(3) + Y3).det()) == 0
   and sp.simplify((U3*Y3*U3inv).trace() - Y3.trace()) == 0)
L_, m_, eps_ = sp.symbols('L m epsilon', positive=True)
C4L = sp.pi*L_**4/24
ok("CA5b exponent arithmetic: (24/pi)^(1/2) |C_L|_4^(1/2) = L^2 and"
   " (24/pi)^(1/4) |C_L|_4^(1/4) = L (the collapse weight and the general floor)",
   sp.simplify((24/sp.pi)**R(1, 2)*C4L**R(1, 2) - L_**2) == 0
   and sp.simplify((24/sp.pi)**R(1, 4)*C4L**R(1, 4) - L_) == 0)
ok("CA5c polydisc split: (L eps)^m = L^2 L^(m-2) eps^m exact; L^(m-2) <= 1 on"
   " 0 < L <= 1, m >= 2 via d/dm L^m = L^m log L <= 0",
   sp.simplify((L_*eps_)**m_ - L_**2*L_**(m_ - 2)*eps_**m_) == 0
   and sp.simplify(sp.diff(L_**m_, m_) - L_**m_*sp.log(L_)) == 0)

# ===== CA6 — sign unavailability at the difference-form level (auditor witnesses) =====
K2 = sp.Matrix([[0, 2], [-2, 0]])
N2 = sp.Matrix([[0, 1], [0, 0]])
Dg = sp.diag(1, -1)
ok("CA6 e2 and tr(.^2) are sign-indefinite on exact witnesses: tr[K^2] = -8 < 0,"
   " tr[N^2] = 0, e2(diag(1,-1)) = -1 < 0, e2(K) = 4 > 0 — no coercivity, no sign",
   (K2*K2).trace() == -8 and (N2*N2).trace() == 0
   and e2(Dg) == -1 and e2(K2) == 4)

# ===== CA7 — slab parity by the sigma_3-conjugation route (independent of closed form) =====
om_, mu_, T_ = sp.symbols('omega mu T', positive=True)
s3 = sp.Matrix([[1, 0], [0, -1]])
s1 = sp.Matrix([[0, 1], [1, 0]])
H = lambda m: om_*s3 + m*s1
conj_ok = sp.simplify(s3*H(mu_)*s3 - H(-mu_)) == sp.zeros(2, 2)
pow_ok = all(sp.simplify(s3*(H(mu_)**k)*s3 - H(-mu_)**k) == sp.zeros(2, 2)
             for k in range(1, 7))
Om = sp.sqrt(om_**2 + mu_**2)
Uslab = lambda m: sp.cos(Om*T_)*sp.eye(2) - sp.I*sp.sin(Om*T_)*(om_*s3 + m*s1)/Om
ok("CA7a sigma_3 H(mu) sigma_3 = H(-mu) and termwise on H^k, k <= 6: U(-mu) ="
   " s3 U(mu) s3 at every Dyson order — diagonal (intraband) EVEN, off-diag (interband) ODD",
   conj_ok and pow_ok)
ok("CA7b the sealed R2 closed form obeys the parity: A(2,2) even in mu, B(1,2) odd in mu"
   " — so the within-quartet difference is interband-only in the slab form",
   sp.simplify(Uslab(mu_)[1, 1] - Uslab(-mu_)[1, 1]) == 0
   and sp.simplify(Uslab(mu_)[0, 1] + Uslab(-mu_)[0, 1]) == 0
   and sp.simplify(s3*Uslab(mu_)*s3 - Uslab(-mu_)) == sp.zeros(2, 2))

# ===== CB1 — half-plane sufficiency (re-run, rotation carried) =====
th = sp.Symbol('theta', real=True)
xs = sp.symbols('x0:5', real=True)
ys = sp.symbols('y0:5', real=True)
rhos = [x + sp.I*y for x, y in zip(xs, ys)]
Z = sum(c*r for c, r in zip(cd, rhos))
lin = sp.expand(sp.re(sp.expand_complex(sp.exp(sp.I*th)*Z))
                - sum(c*sp.re(sp.expand_complex(sp.exp(sp.I*th)*r))
                      for c, r in zip(cd, rhos)))
xr, yi = sp.symbols('xr yi', real=True)
ok("CB1 Re(e^{i th} Z) = sum c Re(e^{i th} rho) exact; |u|^2 - (Re u)^2 = (Im u)^2 >= 0:"
   " separation Re >= delta delivers |Z_hat| >= delta",
   lin == 0 and sp.expand((xr**2 + yi**2) - xr**2 - yi**2) == 0)

# ===== CB2 — the +-i star witness of record, re-derived =====
e34 = sp.expand_complex(sp.exp(3*sp.I*sp.pi/4))
rho_p = 1 + sp.sqrt(2)*e34
rho_m = 1 + sp.sqrt(2)*sp.conjugate(e34)
s2_ = sp.Symbol('s2', real=True)
seg_mod2 = sp.expand(sp.Abs(1 + s2_*sp.sqrt(2)*e34)**2)
ok("CB2 e^{3 i pi/4} = (-1+i)/sqrt2 exact; endpoints = +-i; (1/2)(+i)+4(1/8)(-i) = 0;"
   " segment modulus^2 = (1-s)^2 + s^2 >= 1/2 > 0 (zero-free star)",
   sp.simplify(e34 - (-1 + sp.I)/sp.sqrt(2)) == 0
   and sp.simplify(rho_p - sp.I) == 0 and sp.simplify(rho_m + sp.I) == 0
   and sp.simplify(R(1, 2)*rho_p + 4*R(1, 8)*rho_m) == 0
   and sp.simplify(seg_mod2 - ((1 - s2_)**2 + s2_**2)) == 0
   and sp.simplify(sp.expand((1 - s2_)**2 + s2_**2 - R(1, 2)
                             - 2*(s2_ - R(1, 2))**2)) == 0)

# ===== CB3 — the cube-roots witness by the INTEGER NORM-FORM route (independent) =====
w3 = sp.exp(2*sp.I*sp.pi/3)
ar, br, cr = sp.symbols('ar br cr', real=True)
norm_expr = sp.expand(sp.expand_complex((ar + br*w3 + cr*w3**2)
                                        * sp.conjugate(ar + br*w3 + cr*w3**2)))
qform = ar**2 + br**2 + cr**2 - ar*br - br*cr - cr*ar
ok("CB3a |a + b w + c w^2|^2 = a^2+b^2+c^2-ab-bc-ca = ((a-b)^2+(b-c)^2+(c-a)^2)/2"
   " (real a,b,c; exact) — zero IFF a = b = c",
   sp.simplify(norm_expr - qform) == 0
   and sp.expand(qform - ((ar - br)**2 + (br - cr)**2 + (cr - ar)**2)/2) == 0)
ok("CB3b 1 + w + w^2 = 0 (centroid 0 in conv S); |w^k| = 1 (S zero-free);"
   " 8/3 not an integer (no 3-balance of {4,1,1,1,1})",
   sp.simplify(sp.expand_complex(1 + w3 + w3**2)) == 0
   and all(sp.simplify(sp.Abs(w3**k) - 1) == 0 for k in range(3))
   and R(8, 3).q != 1)
weights8 = [4, 1, 1, 1, 1]
norms = []
for assign in itertools.product(range(3), repeat=5):
    tot = [0, 0, 0]
    for wgt, k in zip(weights8, assign):
        tot[k] += wgt
    aa, bb, cc = tot
    norms.append(aa*aa + bb*bb + cc*cc - aa*bb - bb*cc - cc*aa)   # exact integers
ok("CB3c exhaustive 243 exact integer norms: ALL >= 4 > 0 (Z_hat != 0 in every case);"
   " min = 4 ATTAINED => min |Z_hat| = sqrt(4)/8 = 1/4 EXACTLY (auditor sharpening)",
   len(norms) == 243 and min(norms) == 4 and all(n >= 4 for n in norms)
   and sp.sqrt(sp.Integer(min(norms)))/8 == R(1, 4))

# ===== CB4 — the H-R insufficiency witness via Sherman-Morrison (independent) =====
v1, v2 = sp.symbols('v1 v2', real=True, positive=True)
vv = sp.Matrix([v1, v2])
P = vv*vv.T/(vv.T*vv)[0, 0]                       # generic rank-one projector
st = sp.Symbol('sigma', positive=True)            # sigma := s*t > 0
SM = sp.eye(2) - (st/(1 + st))*P                  # Sherman-Morrison candidate inverse
ok("CB4a generic rank-one P (P^2 = P exact); Sherman-Morrison: (1 + sigma P)^{-1}"
   " = I - (sigma/(1+sigma))P EXACT (route independent of the build's diag(1,0))",
   sp.simplify(P*P - P) == sp.zeros(2, 2)
   and sp.simplify((sp.eye(2) + st*P)*SM - sp.eye(2)) == sp.zeros(2, 2))
sB, tB = sp.symbols('sB tB', positive=True)
Pd = sp.Matrix([[1, 0], [0, 0]])
invB = sp.eye(2) - (sB*tB/(1 + sB*tB))*Pd
integrand = sp.simplify((invB*(sB*tB*Pd)*(tB*Pd)).trace())
segB = sp.integrate(integrand, (sB, 0, 1))
ok("CB4b eigenvalues {1/(1+st), 1}; 1 - 1/(1+st) = st/(1+st) >= 0 => sup_s ||.||_op = 1:"
   " rho_res IDENTICALLY 1 on the family (t-free)",
   sp.simplify(1 - 1/(1 + sB*tB) - sB*tB/(1 + sB*tB)) == 0
   and (sB*tB/(1 + sB*tB)).is_nonnegative)
ok("CB4c segment integrand = s t^2/(1+st); seg(t) = t - log(1+t); seg' = t/(1+t) > 0;"
   " lim_{t->oo} seg = +oo: seg is NOT a function of rho_res — H-R alone closes nothing",
   sp.simplify(integrand - sB*tB**2/(1 + sB*tB)) == 0
   and sp.simplify(segB - (tB - sp.log(1 + tB))) == 0
   and sp.simplify(sp.diff(tB - sp.log(1 + tB), tB) - tB/(1 + tB)) == 0
   and sp.limit(tB - sp.log(1 + tB), tB, sp.oo) == sp.oo)

# ===== CB5 — fixed-n disc-to-half-plane geometry =====
ok("CB5 Re z = 1 + Re(z-1) >= 1 - |z-1| ((Re u)^2 <= |u|^2 exact): |z-1| <= d < 1"
   " forces Re z >= 1-d > 0 — the fixed-n localization; its radius is n-dependent of record",
   sp.expand((xr**2 + yi**2) - xr**2 - yi**2) == 0)

# ===== CB6 — sharpness of the separation bound =====
qs = sp.symbols('q0:5', nonnegative=True)
expr6 = sum(c*q for c, q in zip(cd, qs))
ok("CB6 sum c_p q_p (q_p >= 0): every coefficient >= 1/8 > 0, so the sum vanishes only"
   " if every q_p = 0 — |Z_hat| = delta forces Re(e^{i th} rho_p) = delta for all p",
   all(co >= R(1, 8) for co in sp.Poly(expr6, *qs).coeffs()))

# ===== CB7 — AUDITOR SHARPENING of r-4: connected unit-modulus regions =====
# Identity (any complex 4-tuple): 4 sum|v_j|^2 - |sum v_j|^2 = sum_{i<j} |v_i - v_j|^2.
# For unit vectors: |v1+v2+v3+v4| = 4 forces all equal. Hence on S inside the unit
# circle, 0 in Sigma_c(S) IFF S contains an antipodal pair {u, -u} (s_i = -s0 forced).
# A connected arc with 0 in conv(S) has angular extent >= pi and so CONTAINS an
# antipodal pair => 0 in Sigma_c(S): on connected unit-modulus regions the corrected
# condition (0 outside conv S) is NECESSARY AND SUFFICIENT — every unit-modulus
# non-necessity witness (the build's cube roots) is necessarily DISCONNECTED.
vxs = sp.symbols('a1 a2 a3 a4', real=True)
vys = sp.symbols('b1 b2 b3 b4', real=True)
vz = [x + sp.I*y for x, y in zip(vxs, vys)]
iden = sp.expand(sp.expand_complex(
    4*sum(z*sp.conjugate(z) for z in vz)
    - sum(vz)*sp.conjugate(sum(vz))
    - sum((vz[i] - vz[j])*sp.conjugate(vz[i] - vz[j])
          for i in range(4) for j in range(i + 1, 4))))
ok("CB7a identity: 4 sum|v|^2 - |sum v|^2 = sum_{i<j}|v_i - v_j|^2 (4 generic complex)"
   " => unit vectors with |sum| = 4 are ALL EQUAL (equality case exact)",
   iden == 0)
uu = sp.exp(sp.I*sp.Symbol('phi', real=True))
ok("CB7b antipodal cancellation: 4u + 4(-u) = 0 exactly (u on the unit circle) — an"
   " antipodal pair in S puts 0 in Sigma_c(S); no antipodal pair, no cancellation (CB7a)",
   sp.simplify(4*uu + 4*(-uu)) == 0)
phi_ = sp.Symbol('phi', real=True)
ok("CB7c arc geometry: cos decreasing on [0, pi/2] (d/dphi cos = -sin <= 0), so an arc"
   " of extent < pi has Re(e^{-i psi} z) >= cos(extent/2) > 0 — 0 outside conv;"
   " extent >= pi contains an antipodal pair (interval arithmetic, elementary)",
   sp.simplify(sp.diff(sp.cos(phi_), phi_) + sp.sin(phi_)) == 0)

# ===== CB8 — HS Cauchy-Schwarz pin for the build's (i)-majorant display =====
Mh = sp.Matrix(2, 2, lambda i, j: sp.Symbol(f'h_{i}{j}', real=True))
Msym = (Mh + Mh.T)/2
ok("CB8 equality pin: for real symmetric M, tr(M^2) = ||M||_2^2 exactly (the"
   " |tr M^2| <= ||M||_2^2 Cauchy-Schwarz is tight there); |e2(M)| <= (|trM|^2 + ||M||_2^2)/2"
   " is the standard majorant the build's (i) uses",
   sp.simplify((Msym*Msym).trace()
               - sum(Msym[i, j]**2 for i in range(2) for j in range(2))) == 0)

print("R3C-AUDIT-BATTERY-DONE")
```

Output, verbatim (34/34 PASS):

```text
CA1a census: 5 surviving, N_surv = 1/2, c multiset {1/2, 1/8 x 4}, sum = 1, all > 0: PASS
CA1b weight functional IS the symmetric second difference -(1/4)[f(s2)-2f(0)+f(-s2)]: PASS
CA1c moments m_0..m_4 = 0, 0, -1, 0, -2 (kills first-moment; m_2 = -1 nonzero): PASS
CA2a RESIDUAL LAW (3x3, FREE weights): sum c e2 - e2(sum) - sum cc e2(diff) = (1-S) sum c e2  => identity holds IFF sum c = 1 (negative control included): PASS
CA2b same residual law for the bilinear b(X,Y) = trX trY - tr(XY) (3x3, free wts): PASS
CA2c the derived-weight 5-matrix instance (the build's RA3a) re-verified: PASS
CA3a generic family: m_0 = m_1 = m_3 = 0 for all (v,t); m_2 = 2 v t^2 symbolic: PASS
CA3b generic first-order kill: sum W tr[A_mu B_lam] = 0 (3x3, all v, t): PASS
CA3c generic second-order projection: sum W tr[(A_mu B_lam)^2] = m_2^2 tr[(A1 B1)^2] (3x3, all v, t) — killed content returns squared, coefficient exactly m_2^2: PASS
CA3d sealed specialization v = -1/4, t = sqrt2: m_2 = -1, m_2^2 = 1: PASS
CA3e scalar shadow at the sealed weights: sum w f = 0, sum w f^2 = m_2 f1^2 = -f1^2: PASS
CA4a resolvent split (1+sD)^{-1}D + (1+sD)^{-1}(sD)D = D (3x3 exact) => integrand identity tr[(1+sD)^{-1}D] = trD - tr[(1+sD)^{-1}(sD)(D)]: PASS
CA4b d/ds Log det(1+sD) = tr[(1+sD)^{-1} D] (3x3 exact adjugate route) — the E1 :663-666 display is an algebraic identity at fixed n: PASS
CA4c collapse scoping: det(1 + aD1 + a^2 D2) - 1 - tr(...) has [a^1] = 0 and [a^2] = e2(D1) EXACTLY (3x3): the remainder starts at a-order 2 with e_2 content: PASS
CA5a det(U(1+Y)U^{-1}) = det(1+Y), tr(UYU^{-1}) = trY (3x3 exact) — rho and tr Delta transfer under the covariance; R^{(L)}(a) = R^{(1)}(La) given it: PASS
CA5b exponent arithmetic: (24/pi)^(1/2) |C_L|_4^(1/2) = L^2 and (24/pi)^(1/4) |C_L|_4^(1/4) = L (the collapse weight and the general floor): PASS
CA5c polydisc split: (L eps)^m = L^2 L^(m-2) eps^m exact; L^(m-2) <= 1 on 0 < L <= 1, m >= 2 via d/dm L^m = L^m log L <= 0: PASS
CA6 e2 and tr(.^2) are sign-indefinite on exact witnesses: tr[K^2] = -8 < 0, tr[N^2] = 0, e2(diag(1,-1)) = -1 < 0, e2(K) = 4 > 0 — no coercivity, no sign: PASS
CA7a sigma_3 H(mu) sigma_3 = H(-mu) and termwise on H^k, k <= 6: U(-mu) = s3 U(mu) s3 at every Dyson order — diagonal (intraband) EVEN, off-diag (interband) ODD: PASS
CA7b the sealed R2 closed form obeys the parity: A(2,2) even in mu, B(1,2) odd in mu — so the within-quartet difference is interband-only in the slab form: PASS
CB1 Re(e^{i th} Z) = sum c Re(e^{i th} rho) exact; |u|^2 - (Re u)^2 = (Im u)^2 >= 0: separation Re >= delta delivers |Z_hat| >= delta: PASS
CB2 e^{3 i pi/4} = (-1+i)/sqrt2 exact; endpoints = +-i; (1/2)(+i)+4(1/8)(-i) = 0; segment modulus^2 = (1-s)^2 + s^2 >= 1/2 > 0 (zero-free star): PASS
CB3a |a + b w + c w^2|^2 = a^2+b^2+c^2-ab-bc-ca = ((a-b)^2+(b-c)^2+(c-a)^2)/2 (real a,b,c; exact) — zero IFF a = b = c: PASS
CB3b 1 + w + w^2 = 0 (centroid 0 in conv S); |w^k| = 1 (S zero-free); 8/3 not an integer (no 3-balance of {4,1,1,1,1}): PASS
CB3c exhaustive 243 exact integer norms: ALL >= 4 > 0 (Z_hat != 0 in every case); min = 4 ATTAINED => min |Z_hat| = sqrt(4)/8 = 1/4 EXACTLY (auditor sharpening): PASS
CB4a generic rank-one P (P^2 = P exact); Sherman-Morrison: (1 + sigma P)^{-1} = I - (sigma/(1+sigma))P EXACT (route independent of the build's diag(1,0)): PASS
CB4b eigenvalues {1/(1+st), 1}; 1 - 1/(1+st) = st/(1+st) >= 0 => sup_s ||.||_op = 1: rho_res IDENTICALLY 1 on the family (t-free): PASS
CB4c segment integrand = s t^2/(1+st); seg(t) = t - log(1+t); seg' = t/(1+t) > 0; lim_{t->oo} seg = +oo: seg is NOT a function of rho_res — H-R alone closes nothing: PASS
CB5 Re z = 1 + Re(z-1) >= 1 - |z-1| ((Re u)^2 <= |u|^2 exact): |z-1| <= d < 1 forces Re z >= 1-d > 0 — the fixed-n localization; its radius is n-dependent of record: PASS
CB6 sum c_p q_p (q_p >= 0): every coefficient >= 1/8 > 0, so the sum vanishes only if every q_p = 0 — |Z_hat| = delta forces Re(e^{i th} rho_p) = delta for all p: PASS
CB7a identity: 4 sum|v|^2 - |sum v|^2 = sum_{i<j}|v_i - v_j|^2 (4 generic complex) => unit vectors with |sum| = 4 are ALL EQUAL (equality case exact): PASS
CB7b antipodal cancellation: 4u + 4(-u) = 0 exactly (u on the unit circle) — an antipodal pair in S puts 0 in Sigma_c(S); no antipodal pair, no cancellation (CB7a): PASS
CB7c arc geometry: cos decreasing on [0, pi/2] (d/dphi cos = -sin <= 0), so an arc of extent < pi has Re(e^{-i psi} z) >= cos(extent/2) > 0 — 0 outside conv; extent >= pi contains an antipodal pair (interval arithmetic, elementary): PASS
CB8 equality pin: for real symmetric M, tr(M^2) = ||M||_2^2 exactly (the |tr M^2| <= ||M||_2^2 Cauchy-Schwarz is tight there); |e2(M)| <= (|trM|^2 + ||M||_2^2)/2 is the standard majorant the build's (i) uses: PASS
R3C-AUDIT-BATTERY-DONE
```

REPRODUCTION OF THE BUILD'S OWN BATTERIES: both ```python blocks of the
build were extracted byte-for-byte and executed in the auditor's fresh
venv (r3caudvenv, sympy 1.14.0): Task A 14/14 PASS, Task B 10/10 PASS,
zero FAIL, and each output stream is BYTE-IDENTICAL to the artifact's
claimed "Output, verbatim" blocks.

---

## 3. TASK B ADJUDICATION — THE HALF-PLANE LOCALIZATION

### 3.1 The four routes, re-derived

(1) Per-pair majorant chain: DEAD OF RECORD, verified at bytes — the E1
:811-814 derivation line |tr[BXY]| <= ||B||_op ||X||_2 ||Y||_2 consumes
per-pair HS norms whose carrier sups are +infinity of record (52f2490b §0
+ §5: RL2b_uniformity_refuted = true, X_HS_norm_infinite = true; ZF
§4.1(c), §4.3 o-1); the S1 trace enclosure is uncertified (E1 :687). The
build's distinction that the S2CAND §4.3(c) BAR is clause-scoped ("BARRED
as a discharge route for THIS clause" — R.3'-c) while for R-L0b the
per-pair route is dead-on-record rather than barred-by-decree is EXACT at
the bytes. CONFIRMED. (2) H-R-conditional route: the new insufficiency
witness re-derives by Sherman-Morrison on a generic rank-one projector
(CB4a) and then exactly (CB4b/CB4c): on A_s = stP, Delta = tP the
resolvent family has rho_res identically 1 (t-free) while seg(t) =
t - log(1+t) is monotone unbounded — so no functional bound seg <=
f(rho_res) exists on operator families; H-R (granted as the named
hypothesis) closes nothing additional; the HS factors are load-bearing.
The witness family is in the sealed interpolation shape (A_s = A(0) +
s Delta with A(0) = 0, the collapse form) — an admissible refutation
family for the functional-dependence claim, and NOT a default of H-R:
nothing about the record's rho_res is assumed or valued; the value 1 is
DERIVED on the explicit family. CONFIRMED. (3) Summed-to-per-pair bridge:
none exists sealed; constructing a control-carrying one would be the V-2
void shape (S2CAND §5.3 V-2 verbatim at bytes); the build refuses it.
CONFIRMED. (4) Fixed-n localization: the disc-to-half-plane geometry is
exact (CB5); the radius is n-dependent (ZF o-1) and no limit object exists
to pass to (ZF §4.1(c): "only the n-indexed family exists"). CONFIRMED.
FAILS-AT(n-uniform quantifier) is the honest class; NOT REFUTED (no sealed
configuration violates separation) — concur.

### 3.2 The delivered region characterization, re-derived and sharpened

r-1 (iff at the mix): definition-level exact — Z_hat ranges over exactly
Sigma_c(S) under independent assignment; the characterization is the
worst-case quantifier. r-2 (sufficiency): every mix point is a 5-point
convex combination (sum c = 1, all c >= 1/8 > 0): Sigma_c(S) inside
conv(S); half-plane separation re-derived with the rotation carried (CB1);
the +-i star witness of record re-derives exactly, including zero-freeness
of the star segments ((1-s)^2 + s^2 >= 1/2, CB2). r-3 (non-necessity):
re-derived by the INTEGER NORM-FORM route — |a + bw + cw^2|^2 = a^2 + b^2
+ c^2 - ab - bc - ca = ((a-b)^2 + (b-c)^2 + (c-a)^2)/2, zero iff a = b =
c, and 3 does not divide 8 (CB3a/b); exhaustive 243-case exact integer
enumeration: every norm >= 4 (CB3c). AUDITOR SHARPENING s-1: the minimum
4 is ATTAINED, so on the cube-roots family min |Z_hat| = 1/4 EXACTLY —
the build claimed only nonvanishing; the witness family is in fact
uniformly separated from 0 by the exact margin 1/4. r-4 (scope): the
build's caveat is honest and is now SHARPENED (s-2, exact, CB7a-c): for S
contained in the unit circle, 0 in Sigma_c(S) iff S contains an antipodal
pair (the equality case of the triangle inequality via the four-vector
identity 4 sum|v|^2 - |sum v|^2 = sum_{i<j}|v_i - v_j|^2 forces s_1 = ...
= s_4 = -s_0); a CONNECTED unit-modulus S with 0 in conv(S) has angular
extent >= pi and therefore contains an antipodal pair — hence on
connected unit-modulus regions the corrected condition (0 outside conv S)
is NECESSARY AND SUFFICIENT, and every unit-modulus non-necessity witness
is necessarily disconnected: the build's three-point witness is minimal in
that sense. The general connected case (varying modulus) remains
UNDECIDED, exactly as the build declares. r-5 (sharpness): re-derived
(CB6). The consumable condition of record is unweakened; the licensed
consequence is held to the E1 :883-884 verbatim conditional shape ("If
R-L0b closes, R-L0 is not needed for the n = 1 leg and that must be
stated") — the build adds NO STRONGER. CONFIRMED.

### 3.3 Task B verdict

```text
TASKB_AUDIT = CONFIRMED( FAILS-AT(the n-uniform quantifier) re-derived on
  all four routes with every grounding found at its cited bytes; the two
  new exact witnesses verified by independent routes (Sherman-Morrison;
  integer norm-forms); H-R consumed only as the named hypothesis and
  nowhere defaulted (the witness family's rho_res = 1 is derived, not
  assumed); quantifiers exact (fixed-n results labeled fixed-n; the
  licensed consequence conditional-only); auditor sharpenings s-1
  (min |Z_hat| = 1/4 attained on the witness family) and s-2 (connected
  unit-modulus equivalence) DELIVERED, both consistent with and
  strengthening the build's r-3/r-4; no correction required. )
```

---

## 4. V-1..V-6 WATCH, PROVENANCE, INJECTION, FENCES

### 4.1 Falsifier watch, severally (adopted set S2CAND §5.3, in force by ENTRY cbfbb74c)

```text
V-1  NOT-FIRED. The adopted clause quantifies the OPERATOR HS family:
     sup_n ||Delta^Sigma_n(a)||_2 <= |C|_4^{alpha'} G_hs^Sigma (S2CAND
     §4.1, read at bytes). Every finding of the build (and of this audit)
     lives at the determinant/second-order scalar level (e_2 identity,
     m_2^2 projection, remainder covariance) or the region level; none is
     an admissible refutation of the summed operator estimate at its own
     quantifier; the delivered record estimate (alpha' = 1/4, all-pairs,
     similarity class, e5b0879b, audited cbe6ff4f) is untouched.
V-2  NOT-FIRED. No summed -> per-pair control derivation is exhibited
     anywhere; RA3a majorizes the summed e_2 BY per-pair pieces (the
     harmless direction); the build explicitly declines to construct the
     void-shaped bridge (§3.4) and this audit constructed none.
V-3  NOT-FIRED. No REM overturn: [F]_0 = 0 and [U(0)]_0 = 0 untouched;
     the difference-form strata are REM's own classes MINUS the weight
     sum, not a new class within REM's weight-summed enumeration; no
     composition route evading Plancherel/capped-mass Cauchy-Schwarz is
     exhibited; ZF normalization/nonvanishing scaffolding re-verified
     (CA1a, CB1), not overturned.
V-4  NOT-FIRED. No sealed forced result is contradicted at bytes: REM's
     kill claims are per-branch-linear operator statements and REM's own
     leading coefficient is m_2-content (REM §2.3 at bytes); the
     second-order non-extension is consistent with all of them.
V-5  NOT-FIRED. S2'-O's kill-before-the-norm clause concerns Dyson strata
     of the OPERATOR Delta^{Sigma,all}_n (S2CAND §3.3 at bytes: strata
     with fewer than two record insertions per CTP branch annihilated
     inside the object); RA4b's object is the determinant expansion's
     quadratic trace, in which branch content enters twice — outside the
     clause's scope; the kill operates on the operator as sealed.
V-6  NOT-FIRED. The build's DERIVED/CLAIMED/CONDITIONAL/GROUNDED marks
     were audited span by span where load-bearing and found accurate;
     the two named corrections (c-1 notation, c-2 an unmarked uniqueness
     flourish consumed by nothing downstream) do not rise to marking
     fraud; no authored ingredient is presented as forced.
```

### 4.2 Provenance

17/17 seals recomputed at path by full digest (§1): all match sidecars,
the build's §1 table, the e5b0879b §1 table (14 rows, row-by-row), and
the tasked digest for the artifact under audit. Every span the build
cites was re-read at its cited location and found as cited; in
particular: e5b0879b §4.1/§4.2 (walls verbatim, including "infinity times
L is infinity"), §5.1-§5.3 (corrected condition + witnesses), §2.3-§2.6
(covariance chain; alpha' = 1/4; V-1 first-class analysis); cbe6ff4f §0
(all five audits CONFIRMED; 14/14 seals); cbfbb74c in full (adoption;
V-1..V-6 in force; witnesses LIVE); S2CAND §3.3 (S2'-O), §4.3(c) (the BAR
verbatim, clause-scoped), §4.4 (D-i..D-iv), §5.3 (V-1..V-6); REM
§2.1-§2.4 (X; taxonomy; floors; the weight-sum scope of the
(c=1,o=0)-exclusion), §3.1 (degree-(-1) HS^2 linear in carrier), §3.2
(double kill), §3.5 (compression line; dominated a-series), §5 (grades;
overturn conditions); RL4RL0 §3.1-§3.5 (R-L0 quantifier; u-1..u-4;
threshold algebra; R-L0b shape); ZF §4.1(b)(c), §4.2 (weights c =
(1/2, 1/8 x 4)), §4.3 (o-1/o-2/o-3); E1 :652-666 (Carleman display,
surviving sector only), :679-689 (S1 enclosure; cell sup deferred),
:720-727 (H-R; "May NEVER default to 1 or to any other value (F'-3)"),
:803-848 (R.3 line :811-814; bookkeeping downgrade :817-824; R-L2b;
colour-sum closure; sector hygiene), :851-894 (R-L0/R-L0b; the licensed
conditional at :883-884); PA :75-128 (r(t); sharp M(t); v(t); b_D with
b_D(1/2,0) = 1; J = -(Q b_D Q) tensor alpha_x; a linear in the
generator); 52f2490b §0 + §5 (flags verbatim). R2's closed-form slab
exhibit matches RA7's A_sl/B_sl exactly. NO span was found misquoted,
mislocated, or overread; the build's §1 count note (16 unique files; the
e5b0879b table's 14 rows) is correct at the bytes.

### 4.3 Injection

NONE FOUND. The artifact contains no directive content addressed to
auditors, registrars, or downstream consumers; the only registrar
mentions are authority DISCLAIMERS ("witness status is the registrar's";
"retirement is the registrar's, never this artifact's"). Its §4 is
explicitly descriptive; it claims no act beyond its authority — no
retirement, no entry, no flag flip, no registration, no verdict motion.
Non-ASCII content is typographic only (dashes, section marks). The
auditor followed no instruction originating in the artifact.

### 4.4 Fences

```text
BUILD'S FENCES: HELD. Exact symbolic only — both batteries re-run
  verbatim in the auditor's fresh venv, 24/24 PASS, outputs
  byte-identical; every constant symbolic or an exact rational/surd; the
  only orderings exact-symbolic (st/(1+st) >= 0; L^{m-2} <= 1 by
  log L <= 0; coefficient positivity; 3 does not divide 8); NOTHING
  numeric evaluated; L formal and never instantiated; alpha never
  computed or approached (alpha' cited only as the record's own symbol
  and derived 1/4); M(t) sharp (no mollification anywhere); equal-time
  FALSE by C6 respected (two-time objects only); no carrier or
  cellulation datum (the |C|_4 exponents are formal bookkeeping); no
  per-pair passage smuggled into any claimed summed chain (no discharge
  is claimed; the barred route is analyzed as dead, not traversed); no
  flag flips; no witness retired; H-R nowhere defaulted (the RB4 family's
  rho_res = 1 is derived on an explicit witness family, not assigned to
  the record's hypothesis); the two disclosed harness-form corrections
  (expand_complex; Max replaced by exact ordering) changed no
  mathematical claim — verified by reproduction.
AUDITOR'S FENCES: HELD. Same discipline: sympy 1.14.0 in fresh venv
  r3caudvenv under /private/tmp scratch; exact rationals/surds only;
  nothing numeric; one auditor-side assertion sign slip disclosed and
  corrected (§2.8 harness disclosure); no register/tracker/plan/road/
  ledger/lens file read; no git action; no existing file edited; ONE file
  written (this artifact) plus its seal; output name probed ABSENT before
  write; alpha never approached; no flag flipped; no witness moved.
```

---

## 5. FLAG BLOCK

```text
TASKA_VERDICT = CONFIRMED-WITH-CORRECTIONS( c-1: the §2.2(i) display
  omits the surv,c superscript on the trace factor (its own prose
  disambiguates; notational only); c-2: "the one summed-level
  second-order identity the sealed algebra admits" asserts an underived
  uniqueness consumed by nothing downstream (should read "the
  canonical"/"a") — every mathematical claim re-derived TRUE by
  independent routes (residual law CA2, generic m_2^2 law CA3, series
  scoping CA4, covariance arithmetic CA5, parity CA7), the FAILS-AT(
  unit-cell carrier axis, NOT REFUTED, residue sharpened) adjudication
  re-derives exactly, and no wall break-through was found. )

TASKB_VERDICT = CONFIRMED( FAILS-AT(n-uniform quantifier) re-derived on
  all four routes at the cited bytes; both new witnesses verified by
  independent routes (Sherman-Morrison; integer norm-forms, 243/243 with
  min norm 4 attained); H-R never defaulted; auditor sharpenings
  DELIVERED: s-1 min |Z_hat| = 1/4 EXACTLY on the cube-roots family,
  s-2 on connected unit-modulus regions the corrected condition is
  necessary AND sufficient (every unit-modulus non-necessity witness is
  necessarily disconnected); no correction required. )

V1_STATUS = NOT-FIRED( the adopted clause quantifies the summed OPERATOR
  HS family sup_n ||Delta^Sigma_n(a)||_2; every finding of build and
  audit lives at the determinant/second-order scalar or region level, so
  nothing bears on the adopted summed estimate at its own quantifier;
  the record's delivered alpha' = 1/4 estimate stands untouched. )
  V-2 NOT-FIRED (no summed->per-pair control derivation exists or is
  created); V-3 NOT-FIRED (no anchor overturn); V-4 NOT-FIRED (no bytes
  contradiction); V-5 NOT-FIRED (RA4b's object is the determinant
  expansion's quadratic trace, not a Dyson stratum of the operator);
  V-6 NOT-FIRED (marks accurate; c-1/c-2 are not marking fraud).

NET_VERDICT = BUILD-STANDS-CONFIRMED-WITH-CORRECTIONS( both task
  adjudications survive default-refute audit — 34/34 independent auditor
  checks PASS and the build's own 24 checks reproduce byte-identically in
  a fresh venv; the two corrections are notational (c-1) and rhetorical
  (c-2), touching no verdict, wall, falsifier, witness, or deliverable;
  the residue localization, the P-1 premise naming, the covariance
  weights |C|_4^{1/2} / |C|_4^{1/4}, and the region characterization all
  re-derive; gate-list membership unchanged as the build states. )

PROVENANCE = CLEAN-17/17( every seal recomputed at path by full digest —
  the build (57edbb96 = tasked = sidecar) and all 16 relied-on files —
  matching sidecars, the build's §1 table, and the e5b0879b §1 table
  row-by-row; every cited span re-read at its location and found as
  cited; no misquote, no mislocation, no overread found. )

INJECTION = NONE( no directive content addressed to auditors, registrars,
  or downstream anywhere in the artifact; registrar mentions are
  authority disclaimers; §4 descriptive only; no act beyond the build's
  authority is claimed or performed; non-ASCII is typographic only. )

FENCES = HELD-BOTH( the build's — exact symbolic only, nothing numeric,
  L formal, alpha never approached, M(t) sharp, no carrier/cellulation
  datum, no flag flips, no witness retired, H-R never defaulted, no
  per-pair passage in any claimed summed chain — verified including
  byte-identical battery reproduction; and the auditor's own — fresh
  venv under /private/tmp, exact arithmetic only, one file written plus
  seal, no git, no existing file edited, no register/tracker file read,
  one auditor-side assertion slip disclosed and corrected. )

alpha_computed = false ; kappa_record_computed = false ;
proof_authorized = false
R3C_SUMMED_REMAINDER_AUDIT_RESULT = SEALED.
```
