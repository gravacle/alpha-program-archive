# STAGE 8 — ADVERSARIAL AUDIT OF THE MO-4 ATTEMPT (STAGE8_MO4_CANCELLATION_S9AD_V001) — S9AD V001

## ADVERSARIAL AUDITOR — CODENAME MO4-AUDIT — COMMISSION S9AD — [SEALED]

Date: 2026-08-15 (session CDT). Role: adversarial auditor, NOT told the
build's outcome, default REFUTE, my verdict governs. Stake as tasked: a
false DERIVED here would falsely discharge R-L4b and retire three
standing witnesses.

Gates: `alpha_computed = false` ; `proof_authorized = false` ;
`kappa_record_computed = false`. EXACT SYMBOLIC ONLY; no floats as
ground; no value frozen. No fenced-class file opened (no file matching
register|road_|ledger|lens|plan|tracker|THE_HANDOFF; the supervision
grep hits in §5 are filename-level only, files unopened). "Q-..." tokens
EXPECTED-UNLOCATABLE, noted never chased. No git. ONE output (this
artifact) + seal sidecar at the commission-distinct path, probed ABSENT
immediately before write.

SWEEP CUTOFF, DECLARED: all sweeps in this audit executed against the
tree state as of **2026-08-15 00:20:38 CDT**.

---

## 0. VERDICT IN ONE LINE

**CONFIRMED-WITH-CORRECTIONS — all corrections cosmetic/check-form, NONE
verdict-chain. The build's PARTIAL verdict is CORRECT and, by this
audit's independent countermodel, FORCED: no product-level cancellation
identity valid at the sealed-hypothesis grade can close MO-4, so the
build's refusal to deliver o(kappa_n) is a necessity, not a shortfall —
and every load-bearing DERIVED partial survives attack: the profile-split
Gram factorization (exact), the §4.2 trace chain (trace-norm discipline
CLEAN — every ||.||_1 is paid with two genuine HS halves, no op/HS bound
quoted at trace grade, the rank x op budget NEVER re-entered, the dead
coincidence-vanishing NEVER consumed), the two-sided Gram mass G_n ≍
n^{3/2} (ceiling and floor both derived exactly from CL-A's SEALED
statement bytes at MO-2's authorized discipline), COR-1 (the sub-volume
trace rate n^{3/2} = r-3's MO-3 as named, legitimately within G-5's
left-open class), COR-2 (HS rate n^{3/4}, contradicting nothing sealed —
52f2490b carries no rate display, re-verified at bytes), COR-3, the
crossing identity (re-proved here at a higher-rank instance), and the
residual MO-4-R exactly as named. Uniformity at the closed polydisc
boundary is exact (Duhamel is an identity, not a truncation — no Cauchy
margin is ever needed); the s_i -> 1/2 strata are handled of record
(frame-defined members only; rho_n symbolic everywhere; H-R never
defaulted; WB8's poisoning ceiling displayed, never consumed). Seal
verified (0e894372, bytes at path); all 9 consumed seals independently
recomputed and MATCH; the build's CAS battery re-run VERBATIM in a fresh
venv: 14/14 PASS, output byte-identical; this audit's own battery (23
checks across 4 parts, incl. a decisive 4x4 countermodel) all PASS.
Nothing fires: r-3 NOT discharged, R-L4b NOT discharged, all three R-L4
witnesses STAND — exactly as the build says. Corrections c-1..c-5 (§4)
are cosmetic. AUDIT-YIELD (new, for MO-4-R's commissioning): the
countermodel EXACTLY characterizes when product-level cancellation
exists — pairing-plane-preserving (phase-only) perturbations cancel in
det IDENTICALLY at every compression, while plane-mixing breaks the
cancellation at jet order 2 even though jet order 1 always dies; the
first-jet kill is real and NEVER extends. MO-4-R therefore needs a
family-specific localization/plane statement — precisely the shape the
build named.**

---

## 1. INDEPENDENCE DISCIPLINE (executed as tasked)

The identity question was worked INDEPENDENTLY and the verdict FIXED AND
HASHED BEFORE the build was opened. Record:

```text
PRE-VERDICT file: MO4_AUDIT_PREVERDICT.md (session scratchpad)
  sha256 = 0b761382bcaef214b8021e2d2946ee3299abb28e824a01a97bd6fa686ac12d54
PRE-BATTERY files (run before opening the build):
  mo4_audit_battery.py   0923e172c4c76235f82cf19a4301c0b12264055a5fd31053fc078a8e0b81fc51
  mo4_audit_battery2.py  e00c6a0f405259fb8d3a3898443ec9f3e5784ebcc79e063d7911d9235d9ec216
  mo4_audit_battery3.py  dc4c0a8901e7b0a134c04e3001ef4deafb4c4b4e668851c52b2556eabb0480c0
CONTEXT OPENED BEFORE THE BUILD (sealed priors only, seals verified):
  bebc0f08 r-3 (the frame, the MO list, s-6); MO-4-mention lines of the
  wall/refuting-branch/linkage artifacts (grep-level). The build file
  itself was NOT opened until after the pre-verdict hash above.
PRE-FIXED VERDICT (verbatim substance): MO-4 (trace-grade,
  polydisc-uniform o(-log|det_n(0)|)) is NOT DERIVABLE from the sealed
  stock — countermodel at the sealed-hypothesis grade (§2 below); if the
  build claimed full DERIVED it must contain one of seven named faults
  (H1-H7); if it refused with blockers matching the compression/
  commutator obstruction, the missing coincidence-approach law, or the
  jet-order-2 breakage, default CONFIRMED subject to seal, verbatim CAS
  re-run, fence scan, and no silent budget re-entry in the partials.
OUTCOME OF THE COMPARISON: the build claims PARTIAL (no full closure;
  residual named; nothing fires) — the pre-verdict's second branch. Its
  DERIVED partials were then attacked one by one (§3). None of H1-H7 is
  committed anywhere in the build.
```

---

## 2. THE INDEPENDENT COUNTERMODEL (the audit's own ground, fixed pre-open)

Exact, sympy 1.14.0, fresh venv `mo4auditvenv` (battery part 3, verbatim
in §6): W = sigma_x tensor I_2 (the involution; V(0) = 1 - 2P shape);
V(a) = W e^{iaG} unitary path; G = sigma_z tensor [[1,1],[1,2]] with
{G, W} = 0 EXACTLY (the anticommutation GRANTED though unsealed);
C = diag(t, 1/2, 3/4, 1/2) a contraction with [C, P] != 0; spec(CPC) =
{(16 t^2 + 9)/32, 1/4, 0, 0}, so s_A -> 1/2 exactly as t -> t* =
sqrt(7)/4 (the coincidence stratum). Then, all exact:

```text
  d(a, t) := det(1 + C(V(a) - 1)C):    d(0, t) = -(16 t^2 - 7)/32 -> 0,
  d(a, t*) = (15/256) a^2 + O(a^3)  — NOT identically zero;
  first jet at the coincidence: 0 (the involution's genuine kill);
  hence at fixed small real a != 0, as t -> t*:
  [log|d(a,t)| - log|d(0,t)|] / (-log|d(0,t)|) -> 1,  NOT 0.
```

Every hypothesis the sealed stock supplies is satisfied; the MO-4
conclusion fails. Corollaries: (i) no identity derivable from the sealed
hypotheses alone can close MO-4 — the build's PARTIAL is FORCED; (ii)
the first-jet cancellation (tr(WD) = 0 under {D,W} = 0; uncompressed
pairing det(1+WD)det(1-WD) = det(1+D^2), trace -> HS^2, the recurring
"short one power" shape) is REAL and breaks at jet order 2 under plane
mixing; under compression its error is [C,P]-driven (battery part 1:
first jet of the compressed product = z(1/c^2 - 1), vanishing iff the
pairing planes are C-isotropic) — and of record [C_n, P] carries HS mass
kappa_n; (iii) phase-only perturbations (generator diagonal in the
W-adapted pairing frame) cancel in det IDENTICALLY at every compression
(battery part 2: d(a) = d(0) exactly) — an exact cancellation identity
EXISTS for that subclass; nothing sealed places Delta_n in it. These
three exactly bracket what MO-4-R must decide.

TOY STATUS: the countermodel is a countermodel — it refutes derivability
claims quantified over the sealed hypotheses; it asserts NOTHING about
the record family's own ratio, which stays UNDECIDED (both the build and
this audit hold that line).

---

## 3. THE BUILD UNDER ATTACK — EVERY LOAD-BEARING CLAIM

Seal first: `0e894372d1c53dc6d66d171da08b13c4a756bea9da9bcd7c4c2863645300e127`
recomputed from bytes at path, MATCHES sidecar. 959 lines, read in full
AFTER the §1 hash. The build's 9 consumed seals independently recomputed:
9/9 MATCH (bebc0f08, 72c95d42, 6997ff61, baab38c2, 9fdc3d1c, 549362d4,
d66a922c, 80db260f, 48ecdabe — full digests vs sidecars, prefixes vs the
build's pins).

```text
A-1 THE PROFILE SPLIT (§4.1): re-derived by hand and CAS (W2a/b/c):
    Q b Q = (Q b^{1/2})(b^{1/2} Q) needs only b >= 0 multiplication +
    associativity; b_D = e^{16-1/s} >= 0 at PA bytes via G-5 (:124
    verified at bytes this session). HOLDS. The spinor bookkeeping
    ||(Q b^{1/2} tensor 1_4)||_2^2 = 4 tr(QbQ) = ||(b^{1/2} Q tensor
    alpha_x)||_2^2 verified exactly (tr alpha_x^2 = 4).
A-2 THE TRACE CHAIN (§4.2) — the tasked hazard (op/HS quoted at trace
    grade): NOT COMMITTED. Full hand re-derivation: the two-factor
    decomposition is exact (my W1); each s-integrand's ||.||_1 is paid
    as ||A||_2 ||B||_2 with BOTH factors genuinely HS (the halves of
    A-1), all op-norm spectators bounded by sealed facts (||u(0;1,s)||
    = 1 unitary; ||u(a;s,0)||, ||u_mu(a_-)|| <= e^{eps_*} by K-5 with
    C_b <= 1; ||C_n|| <= 1); the e-power bookkeeping (e^{2eps} on the
    a_+ term, e^{eps} on the a_- term) re-derived and matches; K(eps_*)
    = eps_*(e^{2eps_*} + e^{eps_*}) confirmed (V12 re-run). The rank
    4n^3 appears NOWHERE in the chain. Polydisc-boundary uniformity is
    EXACT: Duhamel is an identity, no series truncation, no Cauchy
    margin needed — the H4 hazard has no purchase. Adjoint branch
    closed of record (|conj a_-| = |a_-|, r-3 CH-d inherited).
A-3 THE GRAM MASS TWO-SIDED (§4.3): the ONLY classical contact, and it
    is FAITHFUL: CL-A's sealed statement (MO-2 :262-269, verified at
    bytes) is phi_k = A_k[cos theta_k + eps_k], A_k^2 = (2/pi)
    (2k)^{-1/2}, sup|eps_k| <= e_k -> 0 on each fixed compact — the
    CEILING phi_k^2 <= A_k^2 (1 + e_k)^2 is exact algebra ON that
    sealed statement (not a new import); K_0 exists by e_k -> 0;
    integral-test grounds exact (V9; my W5 absorb check). The FLOOR
    consumes MO-2's own sealed display (theta = 1/2, k_n(t,t) >=
    sqrt(2n)/(2pi), scaling exact) on an exact-rational window (V10
    re-run: s_-, s_+ >= 33/256, b_min = e^{16 - 65536/1089}, measure
    1/2048 — all re-checked, |x| <= sqrt(3)/16 < 3/8 inside the diamond
    support). Both n-powers exactly 3/2 (my W5/W6). CH-1 blast radius
    correctly drawn (identity §4.1/§4.2 and crossing §4.5 consume NO
    classical analysis — verified by inspection).
A-4 COR-1 (MO-3 SUPPLIED): the object matches r-3's naming at :811-813
    (certified SUB-VOLUME trace-norm rate; uniform constant refuted,
    rate the only survivor — n^{3/2} is a rate). G-5's left-open clause
    verified at bytes (:394-397): the operative class is "routes that
    do not pass through coincidence vanishing" — this route does not
    (the rate comes from support x UV density; p = -3 untouched); the
    parenthetical's two examples are exemplary, not exhaustive (a
    negative verdict at one route cannot close unnamed others — c-3).
    CONSISTENCY: contradicts NOTHING sealed — 52f2490b re-checked at
    bytes this session: NO rate display exists there (the "carrier
    volume" phrase does not even occur in it; r-3 n-3's paraphrase
    ruling re-confirmed). Grade correctly humble (CANDIDATE, registrar
    consumes). INDEPENDENT CORROBORATION: the p = -3 CZ kernel smeared
    at UV scale Lambda = sqrt(2n)/ell over unit-ball support gives
    HS^2 ~ Lambda^3 = n^{3/2} i.e. ||.||_2 ~ n^{3/4} and a mode count
    ~ Lambda^3 at trace grade — COR-1/COR-2's exponents are exactly
    the smearing arithmetic MO-3's own Galerkin note (:474) predicts.
A-5 COR-2/COR-3: interpolation ||T||_2^2 <= ||T||_op ||T||_1 exact
    (V14 conjunct re-run); n^{3/4} = o(n) exact; the P-5 floor stays
    respected (numerator still diverges); no contradiction hunt
    succeeded (X-2's reading confirmed).
A-6 THE CROSSING IDENTITY (§4.5): re-proved at a STRICTER instance than
    the build's (rank-2 P, rank-2 C, 4x4 — my W4) plus the general
    distributivity layer (V5 re-run): (1 + A_n(0))^2 = 1 - 4 Y_n
    Y_n^dag, Y_n = C_n P C_n^perp, tr Y_n Y_n^dag = sum s_i(1 - s_i) =
    kappa_n/2, R_n = (1 + A_n(0))(1 - 4 Y_n Y_n^dag)^{-1}. EXACT,
    given the named premise C_n^2 = C_n (CH-8, properly inherited as
    r-2 CH-A / r-3 CH-g — correctly ledgered PREMISE, and the §4.1-4.3
    chain is genuinely scheme-blind: it compresses through Q_n).
A-7 THE FOUR REFUSALS (§3): each verified at its display; my
    countermodel independently confirms the typology (first-jet kills
    are real — AC8 = 0 — and never extend — AC9 != 0; symmetries are
    norm-invariant — V8's ground; support separation fails at G-5's
    ray witness, re-read at bytes :264-278). The refusals attack
    nothing they need and concede nothing they shouldn't.
A-8 THE RESIDUAL (MO-4-R) AND THE CLOCK ARITHMETIC (§4.6): V13 exact;
    the sqrt(n) gap statement is conditional on the CERTIFIED clocks
    and says so; no floor for the numerator is claimed (F-d correctly
    NOT exhibited); the tightening of "MO-1+MO-2+MO-3 close Route 1"
    is arithmetic at the certified grades and correctly displayed as
    such. MO-4-R's shape (near-1/4 eigenvectors of Y_n Y_n^dag vs the
    b_D-bulk Gram mass) is exactly the bracket my countermodel's
    corollaries (i)-(iii) draw: UNDECIDED is right, in both directions.
A-9 FENCES AND HYGIENE: float scan — no numeric ground (all decimal
    hits are section numbers / the sympy version); fenced-name scan —
    disclaimers and sweep-key listings only; no git tokens beyond the
    no-git declarations; gates present top and bottom; rho_n symbolic
    at every occurrence (H-R held; grep-verified); WB8 ceiling
    displayed only as poisoned (V14's min >= prod core is right — my
    AA5 pins the two-factor case symbolically); the stricken display
    absent; ONE file + sidecar written (post-cutoff mtime scan: only
    the build pair and two OTHER lanes' outputs, which touch no MO-4
    bit — §5); no existing file edited.
```

---

## 4. CORRECTIONS (all cosmetic; none verdict-chain)

```text
c-1 V14's universal conjunct "abc <= min(a,b,c) on (0,1]^3" is verified
    at three exact-rational instances plus displayed reasoning; the CAS
    conjunct is instance-grade while the check name states the
    universal. The fact is trivially true (my AA5 pins the two-factor
    core symbolically; induction on spare factors <= 1). Check-form
    only.
c-2 §4.3's support-volume ceiling int int b_D <= pi/6 over-estimates:
    the exact value of the bounding volume int (4pi/3) min(s,1-s)^3 ds
    is pi/24 (my W3). Valid as a ceiling and ledgered IMMATERIAL
    (CH-4); the constant C_G is symbolic anyway. Cosmetic.
c-3 COR-1 quotes G-5's left-open clause without its parenthetical (two
    example routes named there). The operative class includes the
    build's route regardless (§3 A-4); the elision changes nothing.
    Cosmetic; noted for the registrar's quote hygiene.
c-4 NOTATIONAL COLLISION: §4.5/V6 name the crossing operator "G_n"
    (1 - 4 Y_n Y_n^dag) while §4.2/§4.3/the flag block use G_n for the
    scalar Gram mass. Context disambiguates everywhere; a successor
    consuming §4.5 in isolation should rename one. Cosmetic.
c-5 The flag block's "G_n = 4 int int b_D K3(x,x)" drops the measure
    symbols present in §4.2 (dx ds). Cosmetic.
```

---

## 5. THE AUDIT'S OWN SWEEP (cutoff 2026-08-15 00:20:38 CDT)

```text
ROOTS: /Users/bgm/MB Work/alpha-program-archive and /Users/bgm/MB Work/
alpha_supervision, recursive, minus the fenced name classes (register|
road_|ledger|lens|plan|tracker|THE_HANDOFF, case-insensitive).
KEYS: profile split / Gram factoriz / b_D^{1/2} / sqrt(b_D); MO-4 /
MO4; post-build-cutoff mtimes.
u-1 The ONLY profile-split/Gram-factorization carrier in either root is
    the build itself — its s-2 (the identity is NEW) CONFIRMED at this
    cutoff.
u-2 MO-4 occupation: no other artifact claims MO-4. Files sealed after
    the build's cutoff (WALL_SUMMED_REQUANT, EXTSRC_ROUND3 + audit)
    checked: the EXTSRC audit itself records that MO4_CANCELLATION and
    WALL_SUMMED_REQUANT "touch no deciding bit" of its question; no
    double-count, no interference (the two-lanes-one-worktree hazard
    checked and absent here).
u-3 The build's sweep findings s-1..s-6 re-keyed and consistent at my
    later cutoff; nothing sealed in the window 2026-08-14 23:55:31 ->
    2026-08-15 00:20:38 CDT touches R_n Delta_n(a), MO-4, or the
    residual.
```

---

## 6. THE AUDIT CAS BATTERY (VERBATIM) AND OUTPUTS (VERBATIM)

Two fresh venvs under the session scratchpad, both sympy 1.14.0:
`mo4auditvenv` (this audit's own batteries, parts 1-4) and
`mo4auditvenv2` (the build's battery re-run, VERBATIM extraction from
the sealed §7 block, extraction sha256 d34281b3...). The build re-run:
exit 0, 14/14 PASS, output BYTE-IDENTICAL to the artifact's recorded
block (diff empty). This audit's own 23 checks: all PASS/expected.

### 6.1 Part 1 — `mo4_audit_battery.py` (pre-open; hash in §1)

```python
# MO4-AUDIT independent battery -- EXACT SYMBOLIC ONLY (sympy 1.14.0, fresh
# venv mo4auditvenv under the session scratchpad). Run BEFORE opening the
# build. Every constant symbolic or exact rational. No floats as ground.
# Frame under audit (r-3 of record, bebc0f08):
#   A_n(a) = C_n (V(a) - 1) C_n on ran C_n;  A_n(0) = -2 C_n P C_n;
#   Delta_n(a) = C_n (V(a) - V(0)) C_n;  R_n = (1 + A_n(0))^{-1};
#   V(0) = 1 - 2P an involution on the opposite-phase sector.
# Question: does a product-level cancellation identity for R_n Delta_n(a)
# exist (trace-grade, polydisc-uniform, o(-log|det_n(0)|))?
import sympy as sp

ok = []

# ===== AA1 -- frame sanity, division-free (independent re-derivation) =====
# (1+A0)(D0*I + adj(1+A0)(A-A0)) = D0 (1+A) for any square A0, A (3x3 symbolic)
n = 3
A0 = sp.Matrix(n, n, lambda i, j: sp.Symbol(f'p{i}{j}'))
A  = sp.Matrix(n, n, lambda i, j: sp.Symbol(f'q{i}{j}'))
I  = sp.eye(n)
M0 = I + A0
lhs = M0 * (M0.det() * I + M0.adjugate() * (A - A0))
rhs = M0.det() * (I + A)
ok.append(("AA1 frame division-free", sp.simplify(lhs - rhs) == sp.zeros(n, n)))

# ===== AA2 -- the involution-pairing cancellation, UNCOMPRESSED level =====
# W^2 = 1, {D, W} = 0, D self-adjoint  ==>  tr(WD) = 0 exactly, and
# det(1+WD) * det(1-WD) = det(1+D^2); on a symbolic anticommuting pair the
# pairing converts trace grade to HS^2 grade ("short one power" shape).
x = sp.Symbol('x', complex=True)
W2 = sp.Matrix([[0, -1], [-1, 0]])                    # W = 1-2P, P onto (1,1)/sqrt2
D2 = sp.Matrix([[sp.Symbol('z', real=True), 0], [0, -sp.Symbol('z', real=True)]])
z = sp.Symbol('z', real=True)
anti = sp.simplify(W2 * D2 + D2 * W2)
tr_first_jet = sp.simplify((W2 * D2).trace())
pair = sp.simplify((I2 := sp.eye(2), )[0] + W2 * D2).det() * (sp.eye(2) - W2 * D2).det()
hs   = (sp.eye(2) + D2 * D2).det()
ok.append(("AA2a anticommutation exact", anti == sp.zeros(2, 2)))
ok.append(("AA2b first jet tr(WD)=0", tr_first_jet == 0))
ok.append(("AA2c det(1+WD)det(1-WD)=det(1+D^2)", sp.simplify(pair - hs) == 0))

# ===== AA3 -- COMPRESSION KILLS THE PAIRING; the killer is [C,P] =====
# Same W, D; contraction C = diag(c, 1), 0 < c < 1. Compressed objects:
#   A0c = C(W-1)C, Dc = C D C, R = (1+A0c)^{-1}.
# Show: tr(R Dc) != 0 generically, and its size at the near-coincidence
# stratum s -> 1/2 diverges like the resolvent, with coefficient
# proportional to the commutator content (c^2 - 1)-driven.
c = sp.Symbol('c', positive=True)
C = sp.diag(c, 1)
P2 = sp.Rational(1, 2) * sp.Matrix([[1, 1], [1, 1]])
A0c = C * (W2 - sp.eye(2)) * C
Dc = C * D2 * C
M = sp.eye(2) + A0c
detM = sp.factor(M.det())
R = M.inv()
first_jet_c = sp.simplify(sp.factor((R * Dc).trace()))
comm = sp.simplify(C * P2 - P2 * C)
ok.append(("AA3a det(1+A0c) exact", detM))
ok.append(("AA3b tr(R CDC) compressed", first_jet_c))
ok.append(("AA3c [C,P] nonzero iff c!=1", sp.simplify(comm) ))

# eigenvalues s_i of CPC and the coincidence locus min|1-2s|:
sic = sp.Matrix(C * P2 * C).eigenvals()
ok.append(("AA3d spec(CPC)", dict(sic)))

# ===== AA4 -- the pairing survives compression IFF [C,P]=0 (c=1 limit) ====
ok.append(("AA4 first jet at c=1", sp.simplify(first_jet_c.subs(c, 1))))

# ===== AA5 -- poisoning ceiling re-pin: ||R||_op <= exp(-log|det(0)|) =====
# min_i |1-2s_i| >= prod_j |1-2s_j| when every factor <= 1: exact for two
# symbolic factors u, v in (0,1]: u >= u*v.
u, v = sp.symbols('u v', positive=True)
ok.append(("AA5 min>=prod on (0,1]", sp.simplify(u - u * v) == sp.simplify(u * (1 - v))))

# ===== AA6 -- Cauchy/jet tail at the closed-polydisc BOUNDARY diverges ====
# sum_{k>=2} (|a|/eps)^k at |a| = eps is a divergent series; on a strict
# sub-radius theta*eps it sums to theta^2/(1-theta). Exact symbolic:
theta = sp.Symbol('theta', positive=True)
k = sp.Symbol('k', integer=True, nonnegative=True)
tail = sp.summation(theta**k, (k, 2, sp.oo))
ok.append(("AA6 jet tail closed form (|theta|<1 branch)", sp.simplify(tail)))

# ===== AA7 -- rank x op cannot close: n-free ratio (D10 re-pin) =========
nn, ceps = sp.symbols('n c_eps', positive=True)
ratio = (4 * nn**3 * ceps) / (2 * nn**3)
ok.append(("AA7 rank-x-op ratio n-free", sp.simplify(ratio)))

for name, val in ok:
    print(name, "->", val)
```

```text
AA1 frame division-free -> True
AA2a anticommutation exact -> True
AA2b first jet tr(WD)=0 -> True
AA2c det(1+WD)det(1-WD)=det(1+D^2) -> True
AA3a det(1+A0c) exact -> -c**2
AA3b tr(R CDC) compressed -> -z + z/c**2
AA3c [C,P] nonzero iff c!=1 -> Matrix([[0, c/2 - 1/2], [1/2 - c/2, 0]])
AA3d spec(CPC) -> {(c**2 + 1)/2: 1, 0: 1}
AA4 first jet at c=1 -> 0
AA5 min>=prod on (0,1] -> True
AA6 jet tail closed form (|theta|<1 branch) -> Piecewise((-theta**2/(theta - 1), theta < 1), (Sum(theta**k, (k, 2, oo)), True))
AA7 rank-x-op ratio n-free -> 2*c_eps
```

### 6.2 Part 2 — `mo4_audit_battery2.py` (pre-open; hash in §1)

```python
# MO4-AUDIT battery part 2 -- det-level (all-orders) check in the countermodel.
# V(a) = W exp(i a G), W = involution, {G, W} = 0 (grant the unsealed
# anticommutation in the adversary's favor), C = diag(c, 1) contraction.
# d(a,c) = det(1 + C (V(a) - 1) C).  Question: is log|d(a)| - log|d(0)|
# = o(-log|d(0)|) as c -> 0 (the coincidence stratum s -> 1/2)?
import sympy as sp

a, z = sp.symbols('a z', real=True)
c = sp.Symbol('c', positive=True)
W = sp.Matrix([[0, -1], [-1, 0]])
G = sp.Matrix([[z, 0], [0, -z]])
ok = []
ok.append(("AB0 {G,W}=0", sp.simplify(W*G + G*W) == sp.zeros(2,2)))
expG = sp.Matrix([[sp.exp(sp.I*a*z), 0], [0, sp.exp(-sp.I*a*z)]])
# exact matrix exponential of i a G (diagonal): verified exactly
ok.append(("AB1 exp exact", sp.simplify(expG.diff(a) - sp.I*G*expG) == sp.zeros(2,2)))
V = W * expG
ok.append(("AB2 V unitary on real slice", sp.simplify(V * V.H - sp.eye(2)) == sp.zeros(2,2)))
C = sp.diag(c, 1)
d = sp.factor(sp.simplify((sp.eye(2) + C*(V - sp.eye(2))*C).det()))
d0 = sp.simplify(d.subs(a, 0))
ok.append(("AB3 d(a,c) exact", d))
ok.append(("AB4 d(0,c)", d0))
# the race: numerator N = log|d(a)| - log|d(0)|, denominator -log|d(0)|.
# c -> 0 limit of d(a,c) at fixed a:
dlim = sp.simplify(sp.limit(d, c, 0))
ok.append(("AB5 lim_{c->0} d(a,c)", dlim))
# leading behavior: series of d in c around 0
ser = sp.series(d, c, 0, 3).removeO()
ok.append(("AB6 series of d at c=0", sp.simplify(ser)))
# |d(a)|^2 exact (real a):
mod2 = sp.factor(sp.simplify(sp.expand(d * sp.conjugate(d)).rewrite(sp.cos)))
ok.append(("AB7 |d|^2 exact", mod2))
for name, val in ok:
    print(name, "->", val)
```

```text
AB0 {G,W}=0 -> True
AB1 exp exact -> True
AB2 V unitary on real slice -> True
AB3 d(a,c) exact -> -c**2
AB4 d(0,c) -> -c**2
AB5 lim_{c->0} d(a,c) -> 0
AB6 series of d at c=0 -> -c**2
AB7 |d|^2 exact -> c**4
```

(Reading: with a PHASE-ONLY generator the det is a-INDEPENDENT — exact
all-orders cancellation at every compression; the probative case needs
plane mixing, part 3. The same phase-only degeneracy was verified for
the 4x4 diagonal-H case in-session before part 3 was fixed.)

### 6.3 Part 3 — `mo4_audit_battery3.py` (pre-open; hash in §1)

```python
# MO4-AUDIT battery part 3 -- the decisive 4x4 countermodel.
# W = sigma_x (x) I2 involution; G = sigma_z (x) H, H = [[1,1],[1,2]] (mixes
# the two W-pairing planes); {G, W} = 0 EXACTLY (granting the adversary the
# unsealed anticommutation); V(a) = W exp(iaG) unitary on the real slice;
# C = diag(t, 1/2, 3/4, 1/2) contraction, [C,P] != 0 in plane A when t != 3/4;
# coincidence stratum: s_A = (t^2 + 9/16)/2 -> 1/2 as t -> sqrt(7)/4.
# QUESTION: does d(a,t) = det(1 + C(V(a)-1)C) vanish at the coincidence for
# all a (product-level cancellation) or only at a = 0 (no cancellation)?
import sympy as sp

a = sp.Symbol('a', real=True)
t = sp.Symbol('t', positive=True)
I2, I4 = sp.eye(2), sp.eye(4)
sx = sp.Matrix([[0, 1], [1, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
H = sp.Matrix([[1, 1], [1, 2]])
W = sp.Matrix(sp.kronecker_product(sx, I2))
G = sp.Matrix(sp.kronecker_product(sz, H))
ok = []
ok.append(("AC0 W^2=1", sp.simplify(W*W - I4) == sp.zeros(4,4)))
ok.append(("AC1 {G,W}=0", sp.simplify(G*W + W*G) == sp.zeros(4,4)))
expH = sp.simplify((sp.I*a*H).exp())
expG = sp.Matrix(sp.BlockDiagMatrix(expH, expH.subs(a, -a)).as_explicit())
ok.append(("AC2 d/da exp = iG exp", sp.simplify(expG.diff(a) - sp.I*G*expG) == sp.zeros(4,4)))
V = W * expG
ok.append(("AC3 V unitary (real a)", sp.simplify(sp.expand_complex(V*V.H - I4)) == sp.zeros(4,4)))
P = (I4 - W) / 2
C = sp.diag(t, sp.Rational(1,2), sp.Rational(3,4), sp.Rational(1,2))
ok.append(("AC4 [C,P] != 0 (t sym)", sp.simplify(C*P - P*C) != sp.zeros(4,4)))
# spectrum of CPC: s_A = (t^2 + 9/16)/2, s_B = 1/4  (exact check)
sspec = (C*P*C).eigenvals()
ok.append(("AC5 spec(CPC)", dict(sspec)))
d = sp.simplify((I4 + C*(V - I4)*C).det())
d0 = sp.simplify(d.subs(a, 0))
ok.append(("AC6 d(0,t) exact", sp.factor(d0)))
tstar = sp.sqrt(7)/4
dstar = sp.simplify(sp.expand_complex(d.subs(t, tstar)))
ok.append(("AC7 d(0, t*) = 0", sp.simplify(dstar.subs(a, 0))))
# is d(a, t*) identically 0 in a?  series coefficients at a = 0:
ser = sp.series(dstar, a, 0, 3).removeO()
c2 = sp.simplify(sp.expand(ser).coeff(a, 2))
c1 = sp.simplify(sp.expand(ser).coeff(a, 1))
ok.append(("AC8 jet1 of d at (0,t*)", c1))
ok.append(("AC9 jet2 of d at (0,t*)", c2))
for name, val in ok:
    print(name, "->", val)
```

```text
AC0 W^2=1 -> True
AC1 {G,W}=0 -> True
AC2 d/da exp = iG exp -> True
AC3 V unitary (real a) -> True
AC4 [C,P] != 0 (t sym) -> True
AC5 spec(CPC) -> {(16*t**2 + 9)/32: 1, 0: 2, 1/4: 1}
AC6 d(0,t) exact -> -(16*t**2 - 7)/32
AC7 d(0, t*) = 0 -> 0
AC8 jet1 of d at (0,t*) -> 0
AC9 jet2 of d at (0,t*) -> 15/256
```

### 6.4 Part 4 — `mo4_audit_battery4.py` (post-open, build-specific)

```python
# MO4-AUDIT battery part 4 -- build-specific attack checks. EXACT SYMBOLIC ONLY.
import sympy as sp
from sympy import Rational as R
ok = []

# ===== W1 -- the two-factor decomposition, exact operator algebra =====
n = 3
um_a = sp.Matrix(n, n, lambda i, j: sp.Symbol(f'm{i}{j}'))
um_0 = sp.Matrix(n, n, lambda i, j: sp.Symbol(f'r{i}{j}'))
ul_b = sp.Matrix(n, n, lambda i, j: sp.Symbol(f'l{i}{j}'))
ul_0 = sp.Matrix(n, n, lambda i, j: sp.Symbol(f'k{i}{j}'))
lhs = um_a.T*ul_b - um_0.T*ul_0
rhs = um_a.T*(ul_b - ul_0) + (um_a - um_0).T*ul_0
ok.append(("W1 two-factor decomposition exact", sp.expand(lhs - rhs) == sp.zeros(n, n)))

# ===== W2 -- Gram/spinor bookkeeping: ||Q b^{1/2} (x) 1_4||_2^2 = 4 tr(QbQ),
# ||b^{1/2} Q (x) alpha_x||_2^2 = 4 tr(QbQ)  (tr(alpha_x^2) = 4 exact) =====
q = sp.Matrix(2, 2, lambda i, j: sp.Symbol(f'q{i}{j}', real=True))
b0, b1 = sp.symbols('b0 b1', nonnegative=True)
bh = sp.diag(sp.sqrt(b0), sp.sqrt(b1))
sx = sp.Matrix([[0,1],[1,0]]); s0 = sp.eye(2); Z = sp.zeros(2,2)
alx = sp.Matrix(sp.BlockMatrix([[Z, sx],[sx, Z]]))
X1 = sp.Matrix(sp.kronecker_product(q*bh, sp.eye(4)))
X2 = sp.Matrix(sp.kronecker_product(bh*q, sp.eye(2)))  # spatial part; spinor via alx below
hs1 = sp.simplify((X1*X1.T).trace() - 4*(q*sp.diag(b0,b1)*q.T).trace())
tr_alx2 = sp.simplify((alx*alx).trace())
hs2_spatial = sp.simplify(((bh*q)*(bh*q).T).trace() - (q.T*sp.diag(b0,b1)*q).trace())
ok.append(("W2a HS of (Qb^1/2 x 1_4) = 4 tr(QbQ)", hs1 == 0))
ok.append(("W2b tr(alpha_x^2) = 4", tr_alx2 == 4))
ok.append(("W2c spatial HS symmetric-side equal", hs2_spatial == 0))

# ===== W3 -- exact support volume: int_0^1 (4pi/3) min(s,1-s)^3 ds = pi/24 <= pi/6 =====
s = sp.Symbol('s', positive=True)
vol = sp.Rational(4,3)*sp.pi*(sp.integrate(s**3, (s, 0, R(1,2))) + sp.integrate((1-s)**3, (s, R(1,2), 1)))
ok.append(("W3 exact diamond volume", sp.simplify(vol)))

# ===== W4 -- tr(C P Cperp P C) = tr(CPC) - tr((CPC)^2) for projections, general
# symbolic proof shape at a nontrivial exact instance (rank-2 P, rank-2 C, 4x4) =====
v1 = sp.Matrix([1, 1, 1, 1])/2
v2 = sp.Matrix([1, -1, 1, -1])/2
P4 = v1*v1.T + v2*v2.T
C4 = sp.diag(1, 1, 1, 0)
I4 = sp.eye(4)
lhs4 = (C4*P4*(I4 - C4)*P4*C4).trace()
rhs4 = (C4*P4*C4).trace() - ((C4*P4*C4)*(C4*P4*C4)).trace()
ok.append(("W4 crossing trace = kappa/2 shape (rank-2 instance)", sp.simplify(lhs4 - rhs4) == 0))

# ===== W5 -- ceiling asymptotics: (M + B sqrt(2n))^3 has leading B^3 (2n)^{3/2};
# existence of symbolic C_G with (M + B sqrt(2n))^3 <= C_G n^{3/2} for n >= n_c:
# take C_G = 8 B^3 2^{3/2} + M-terms absorbed for sqrt(2n) >= M/B  (exact algebra:
# M + B sqrt(2n) <= 2 B sqrt(2n) once sqrt(2n) >= M/B) =====
M, B, nn = sp.symbols('M B n', positive=True)
cond = sp.simplify((2*B*sp.sqrt(2*nn))**3 - 8*B**3*(2*nn)**R(3,2))
ok.append(("W5 ceiling absorb: (2B sqrt(2n))^3 = 8 B^3 (2n)^{3/2}", cond == 0))

# ===== W6 -- the floor constant assembly: 4 b_min (1/2048) (sqrt(2n)/(2 pi ell))^3
# = (b_min 2^{1/2} / (2048 pi^3 ell^3)) n^{3/2} -- pure exact algebra =====
bmin, ell = sp.symbols('b_min ell', positive=True)
fl = 4*bmin*R(1,2048)*(sp.sqrt(2*nn)/(2*sp.pi*ell))**3
lead = sp.simplify(fl / nn**R(3,2))
ok.append(("W6 floor n-power exactly 3/2, coefficient n-free", sp.simplify(sp.diff(lead, nn)) == 0))

for name, val in ok:
    print(name, "->", val)
```

```text
W1 two-factor decomposition exact -> True
W2a HS of (Qb^1/2 x 1_4) = 4 tr(QbQ) -> True
W2b tr(alpha_x^2) = 4 -> True
W2c spatial HS symmetric-side equal -> True
W3 exact diamond volume -> pi/24
W4 crossing trace = kappa/2 shape (rank-2 instance) -> True
W5 ceiling absorb: (2B sqrt(2n))^3 = 8 B^3 (2n)^{3/2} -> True
W6 floor n-power exactly 3/2, coefficient n-free -> True
```

---

## 7. CHOICE LEDGER (every unforced choice of this audit, classified)

```text
CH-A PRE-OPEN CONTEXT SET (r-3 in full + grep-level MO-4 mentions of the
     wall/refuting-branch/linkage): FORCED-minimal — the identity
     question is defined by bebc0f08 and cannot be worked without its
     frame; the build stayed unopened until the §1 hash was fixed.
CH-B COUNTERMODEL SHAPE (4x4, kronecker, H = [[1,1],[1,2]], C = diag(t,
     1/2, 3/4, 1/2)): IMMATERIAL(derived) — any plane-mixing G and any
     pairing-anisotropic contraction with a tunable coincidence works;
     the 2x2 and diagonal-H degeneracies are REPORTED (§2, §6.2), not
     hidden, and are themselves informative (the phase-only subclass).
CH-C GRANTING {G, W} = 0 IN THE COUNTERMODEL: adversary-favoring — the
     anticommutation is unsealed for the record family; granting it
     makes the countermodel STRONGER (even with it, no closure).
CH-D SECOND VENV FOR THE VERBATIM RE-RUN (mo4auditvenv2, sympy pinned
     1.14.0): hygiene — the build's battery ran in an environment never
     touched by this audit's own scripts.
CH-E CORRECTIONS KEPT AT COSMETIC (c-1..c-5) rather than forcing a
     REFUTED-AT: FORCED by the menu's semantics — none changes any
     displayed inequality, exponent, grade, or the verdict boundary;
     each is displayed with its exact repair.
CH-F THE UV-SMEARING CORROBORATION OF COR-1/COR-2 (§3 A-4): stated as
     CORROBORATION only (heuristic arithmetic agreeing with the derived
     exponents), never as ground — the derived chain stands on §4.2/4.3
     alone.
MACHINERY/RELEVANCE: classical linear algebra and one countermodel
     construction; CAS exact throughout; SURFACE-DERIVED, not
     surface-native; no surface verdict beyond the named conditionals.
```

## 8. TOY_SEPARATION (self-assessment)

```text
CLAIMED CLEAN at the stated quantifiers. The countermodel (AB/AC) is
used ONLY against derivability-from-hypotheses claims (universally
quantified over the sealed hypothesis class), which a single exact
countermodel lawfully refutes; it is NEVER used to assert anything
about the record family's own ratio (§2 TOY STATUS). The W-series and
AA-series instances are identity-grade exhibits of displayed general
facts. No spectral datum of the actual family is valued anywhere;
rho_n, eps_*, ell, C_G, c_G, C_*, all thresholds stay symbols. The
2x2/diagonal-H degeneracies are disclosed in place.
```

## 9. FLAG BLOCK

```text
MO4_AUDIT = CONFIRMED-WITH-CORRECTIONS( verdict boundary EXACT as
  built: MO-4 NOT closed, PARTIAL stands; corrections c-1..c-5 all
  cosmetic/check-form, none verdict-chain; every DERIVED partial
  survives adversarial re-derivation; the named hazards (op/HS at trace
  grade; rank x op re-entry; dead coincidence-vanishing; polydisc-
  boundary uniformity; s_i -> 1/2 strata; H-R default) are each checked
  and NOT committed. )
INDEPENDENCE = EXECUTED( verdict fixed and hashed BEFORE the build was
  opened: MO4_AUDIT_PREVERDICT.md sha256 0b761382...; the build landed
  in the pre-verdict's refusal branch; none of the pre-named faults
  H1-H7 present. )
COUNTERMODEL_OF_RECORD = YES( 4x4 exact: all sealed hypotheses + the
  granted anticommutation, yet [log|d(a)| - log|d(0)|] / (-log|d(0)|)
  -> 1 at the coincidence — NO sealed-hypothesis-grade identity can
  close MO-4: the build's PARTIAL is FORCED. Bracket: first jet always
  dies; jet order 2 breaks under plane mixing; phase-only perturbations
  cancel identically at every compression. MO-4-R needs a family-
  specific plane/localization statement — exactly the build's naming. )
CONSUMPTION_GUIDANCE = FOR-THE-REGISTRAR( the build is consumable at
  audited grade. COR-1 (MO-3 supplied, grade DERIVED-given-CL-A) is
  GENUINE and its left-open-route reading verified at G-5's bytes;
  whether COR-1 discharges any R-L2b-adjacent obligation is the
  registrar's call, not made here. The MO-map after this pair: MO-2
  DERIVED (audited), MO-3 SUPPLIED-here (this audit confirms), MO-1
  and MO-4-R OPEN — r-3 and R-L4b remain undischarged; the three R-L4
  witnesses STAND. )
NOTHING_FIRES = CONFIRMED( no flag flips, no witness retires, no gate
  moves; F-d NOT exhibited; the race UNDECIDED both directions of
  record. )
SEALS = VERIFIED( build 0e894372 at bytes; 9/9 consumed seals
  recomputed MATCH; battery extraction d34281b3; re-run 14/14 PASS
  byte-identical; audit pre-verdict 0b761382. )
SWEEP_CUTOFF = 2026-08-15 00:20:38 CDT( u-1 the profile split is NEW —
  sole carrier is the build; u-2 no MO-4 occupation conflict, post-
  cutoff lanes touch no deciding bit; u-3 nothing in the window touches
  R_n Delta_n(a). )
FORBIDDEN_IMPORTS = none( exact symbolic only; no floats as ground; no
  value frozen; fences alpha_computed = false, proof_authorized =
  false, kappa_record_computed = false held; no fenced-class file
  opened; "Q-..." tokens noted EXPECTED-UNLOCATABLE, never chased; no
  git; ONE output + sidecar, path probed ABSENT before write. )
MACHINERY_INVOKED = yes(CAS) — sympy 1.14.0, fresh venvs mo4auditvenv
  (own battery, 4 parts, 23 checks) and mo4auditvenv2 (verbatim re-run,
  14/14 PASS, diff empty); scripts and outputs reproduced verbatim §6.
alpha_computed = false ; proof_authorized = false ;
kappa_record_computed = false
MO4_AUDIT_RESULT = SEALED.
```
