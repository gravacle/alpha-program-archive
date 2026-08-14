# STAGE 8 — ZERO-FREE-CHECK: BLIND ADVERSARIAL VERIFICATION OF STAGE8_ZERO_FREE_DERIVATION_V001

## BLIND VERIFIER — CODENAME ZERO-FREE-CHECK — CROSS-LINEAGE — [SEALED]

Date: 2026-08-14
Role: BLIND adversarial verifier, cross-lineage, DEFAULT = REFUTE. Under
test: STAGE8_ZERO_FREE_DERIVATION_V001.md (sha256 26f9314b..., verified at
path from bytes this session against the tasked digest — MATCH). Attacks
run: (1) the simultaneous-vanishing condition re-derived from scratch and
the missed-zero hunt (marginality region, domain boundary, polydisc
status); (2) the normalization and nonvanishing region re-derived; (3) the
selection audit (DERIVED vs covert act) and the reverse hunt (a derivation
the build missed); (4) the Route B quantifier/content separation; (5)
provenance + injection. Independent CAS battery (39/39 PASS, §6) built on
derivation paths the build did not use: the slab amplitude from the matrix
exponential from scratch, a TWO-SLAB test of the transversality engine,
CLOSED-domain zero solves, the branch-conjugation identity, and the
per-phase-class factorization probe of the o-2(ii) block.

Gates: `alpha_computed = false` ; `kappa_record_computed = false` ;
`proof_authorized = false`. ALL_RESULTS = CLAIMED until checked.

Fences held: EXACT SYMBOLIC ANALYSIS ONLY — one CAS script (sympy 1.14.0,
fresh venv `zfcheckvenv`), reproduced in full in §6 with output verbatim;
NOTHING numeric evaluated; every constant symbolic or an exact
rational/surd. No physical quantity computed, bounded numerically, or
evaluated. No scale, imported GR, or faithfulness authority. M(t) sharp;
equal-time FALSE by C6 (the omega = 0 slice is consumed only as the sealed
bookkeeping intermediate of record, R2 §4). No
register/tracker/plan/road/ledger/lens file read. Output name probed
before write: ABSENT. No git action.

---

## 0. VERDICT IN ONE LINE

**CONFIRMED with one required correction. Every re-derivable claim
re-derives: the modulus identity, the simultaneous-vanishing condition,
the single interior zero at (lambda = ±sqrt2, rho* = 2^(-5/4), omega = 0)
as the COMPLETE omega = 0 zero set (closed-domain solves; no missed zero at
either boundary or in the marginality region), the transversality engine
(validated here on the strictly larger two-slab class the build never
tested), the two cancellations, the normalization (N_surv(0) = 1/2,
c = (1/2, 1/8 x 4), kappa_bal = 1), and the nonvanishing region
{kappa_bal x e^x < 1}. The build's own script re-runs 35/35 with output
byte-identical to its §7. No omega-dependence is smuggled into the claimed
neighborhood (the C2 shape does not re-enter). No covert act found; the
NOT-DERIVABLE verdict and the no-new-act determination stand. THE
CORRECTION: the reduction's landing set is under-enumerated. The
volume-uniformity of the reduced neighborhood {x e^x < 1} over ADMITTED
CELLS is exactly E1 obligation R-L0 (cell-scale normalization: x(C,eps) <=
X_*(eps) with kappa_bal X_* e^{X_*} <= 1/2; witness
E1_CELL_SCALE_NORMALIZATION_UNCERTIFIED; alternative R-L0b), a named,
load-bearing, MAY-FAIL obligation the build never mentions — and it sits
inside the very quantifier passage the build cites (E1 :687-689: "the sup
over CELLS is deferred to R-L0"). The summed-S2' act is the
carrier/colour-sum axis and does not deliver the cell sup. The remaining
set of record is therefore summed-S2' + R-L4a/b + R-L0(/R-L0b) + the
C-L2/G_cm input — not "summed-S2' + R-L4a/b" as the build's flag
enumerates. "ACT REMAINING: none NEW" survives literally (R-L0 is already
named in the sealed spec); the enumeration does not.**

---

## 1. SEALS AND PROVENANCE, VERIFIED AT PATH THIS SESSION

All under `/Users/bgm/MB Work/alpha-program-archive/workspace/`; every
digest recomputed from bytes.

```text
26f9314bdbbf1d7638ecbdf398c891cb3ba54251d4b40314df39c03ab48c08b7  STAGE8_ZERO_FREE_DERIVATION_V001.md  MATCH (artifact under test; sidecar matches)
df4514a5b807cbc903465505ad896ffb6e72c7ab9f891a4541226d18398a7034  STAGE8_G1_KERNEL_CERTIFICATE_V001.md         MATCH (tasked df4514a5)
3534ca534709a3c8ac591994a9ae650224a8594b3f1a8b2a96494a69ab9653e6  STAGE8_G1_KERNEL_CERTIFICATE_CHECK_V001.md   MATCH (tasked 3534ca53)
2e4e5163bb5b9c06078890fc573dd149905975b55860dcabcc7050fb1aa02666  STAGE8_REMAINDER_UNIFORMITY_V001.md          MATCH (tasked 2e4e5163)
89641f762d35c0e6d3c8fb0475e2de742663f9dcf9f08a44621b059c2bd927ec  STAGE8_REMAINDER_UNIFORMITY_CHECK_V001.md    MATCH (tasked 89641f76)
a7969f0c3a42112ee300f73617494fb77c2a415bf5b6cf4d33598c6b6c8bf9cf  STAGE8_R2_RESUMMATION_V001.md                MATCH (tasked a7969f0c)
a4f2e1b7878139afd017abe5fb62c6af7bf19836f7f162ef62902265bfc03cb5  STAGE8_R2_RESUMMATION_CHECK_V001.md          MATCH (tasked a4f2e1b7)
468467303a109dc825b015107897dacc107800fc981030377c3f006b384cccb5  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md  MATCH (tasked 46846730)
0a10c0305d4cde8b226d844ed0fb9289f393b670e02b144bf762dd49c853c9c4  STAGE8_ASSEMBLY_QUANTIFIER_V001.md           MATCH (tasked 0a10c030)
331035d393695519eaa061a343abb67129a8ea48fcc47a765daaef1883b0aa22  STAGE8_ASSEMBLY_QUANTIFIER_CHECK_V001.md     MATCH (tasked 331035d3)
aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a  evaluator_build_A/inputs/evidence/aa7c6d49...--BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md  MATCH (V011 sealed member)
52f2490b187fd4b307c2af45f6238ea02f1d6839b23466fefee1dbba47ed6241  STAGE8_RL2B_UNIFORMITY_REFUTED_RESULT_V001.md  MATCH (per-pair refutation, verified HERE — see note N-2)
```

Line-number landings re-verified from the sealed bytes: V011(aa7c6d49)
:1225-1226 (Z_h(A) = a_h(A)/a_h(0), Z_h(0) = 1), :1232-1233 ("must prove a
volume-uniform zero-free neighborhood for the derived amplitude"),
:1253-1258 (Gamma monoidal additivity over disjoint cells), :2184
(volume_uniform_zero_free_neighborhood_proved = false); E1 :660-668
(Carleman displays; Log rho valid only on the surviving sector), :669-674
(F'-14, witness SCAD_COLOR_SUM_LOG_MISUSE), :687-689 (sups over states,
colour pairs on the surviving sector, closed pair polydisc; **"the sup
over CELLS is deferred to R-L0"**), :745-762 (R.2 sector algebra,
phases (+1,-1,-1), V(0) = I same-phase, S_± = ±1/2), :766-790 (R-L4a/b
uncertified, sector-defining), :794-800 (kappa_bal = 1 from surviving
weights), :835-848 (R.3: Z_hat = sum c rho, R.3.a/R.3.b), :850-895 (R.4:
**R-L0 cell-scale normalization, X_*(eps), kappa_bal X_* e^{X_*} <= 1/2,
MAY-FAIL hazard, witness E1_CELL_SCALE_NORMALIZATION_UNCERTIFIED; R-L0b
alternative**); R2 :78-81/:98 (weights, moments, v(t), tau_R = pi/sqrt2),
:352 (V4a closed form), :360/:472 (omega = 0 slice = bookkeeping
intermediate, equal-time stays FALSE), :265 (weighted sum = g); REM
:266-311 (rate chain, slab instance, l1 bounds), :352-383 (dominated
a-series, ||Pi X Pi||_2 <= ||X||_2), :445-519 (e-i/e-ii typing, overturn
conditions, DEBT 2/DEBT 3); AQ Q-2 (:687-689 quoted), §2.3(iii)/§4
(Route B verbatim as the build's D-2 quotes it), §5; G1 §2-§5 (gate list;
52f2490b identified as STAGE8_RL2B_UNIFORMITY_REFUTED_RESULT_V001.md).

UNVERIFIABLE NOTE (reproduced): the working-tree
BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md has no sidecar and
recomputes to 20a3a17d... — drifted, exactly as the build reports. Not
relied on; every V011 citation read from the sealed evidence member.

The build's §7 script was extracted verbatim and re-run in a fresh venv:
35/35 PASS, output BYTE-IDENTICAL to the artifact's claimed verbatim
output (diff empty).

---

## 2. ATTACK 1 — THE SIMULTANEOUS-VANISHING CONDITION AND THE MISSED-ZERO HUNT

Re-derived from scratch, not from the build's steps (§6, C1-C3, C11):

```text
(a) The slab amplitude was NOT taken from R2: U = exp(-i(omega sigma_3 +
    mu sigma_1)T) computed directly by CAS matrix exponential; its sea-sea
    (2,2) entry equals cos(Om T) + i omega sin(Om T)/Om exactly (C1a), and
    U is unitary (C1b). R2 V4a independently reproduced.
(b) Om^2|A|^2 = omega^2 + mu^2 cos^2(Om T) re-derived (C2a); the floor
    |A|^2 - omega^2/Om^2 = (mu cos(Om T)/Om)^2 is a perfect square (C2b).
    Sum of real squares => A = 0 iff omega = 0 AND cos(mu T) = 0: the
    simultaneous-vanishing condition is EXACT, and every slab is zero-free
    on {omega > 0}. MATCH.
(c) THE ZERO HUNT, closed domains. Theta(rho)/tau_R = 1 - 16 rho^4
    re-derived by direct integration (C3a); u = 1 - 16 rho^4 is a monotone
    bijection [0,1/2] -> [0,1] (C3b0); cos(pi u) = 0 on CLOSED [0,1] iff
    u = 1/2 (C3b1); 1 - 16 rho^4 = 1/2 on CLOSED [0,1/2] iff rho =
    2^(-5/4) (C3b2). Both endpoints checked non-zero: A(0) = -1, A(1/2) =
    +1 (C3d). A_{-sqrt2} = A_{sqrt2} exactly (cos even, C3c) — same single
    zero, and lambda = 0 is identically 1 (C3e). Candidate exhaustion:
    |lambda Theta| <= sqrt2 tau_R = pi on the ball, and the only points of
    pi/2 + pi Z in [-pi, pi] are ±pi/2 (C11). THE OMEGA = 0 ZERO SET IS
    COMPLETE AS CLAIMED: one interior zero per non-trivial branch, at
    rho* = 2^(-5/4), and nowhere else. VANISHING_RERUN = MATCH.
(d) TRANSVERSALITY, attacked at its engine. The build verified its
    first-order-in-omega formula only on the single slab. Here it is
    tested on the strictly larger TWO-SLAB class: the exact derivative of
    the two-slab product at omega = 0 equals the claimed integral engine
    i[sin(Phi) int sin(2phi) + cos(Phi) int cos(2phi)] with piecewise
    phases (C6a) — and the general Duhamel integrand identity
    (-i[e^{-i(Phi-p)s1} s3 e^{-i p s1}])_{22} = i[sin(Phi) sin(2p) +
    cos(Phi) cos(2p)] holds for ARBITRARY p (C6b), which validates the
    engine for every piecewise profile, the sealed one included. At the
    zero: dA/drho = 2^(9/4) pi (C7a), Im A(rho,0) = 0 identically (C7b),
    2 phi runs exactly [0, pi] (2 sqrt2 Theta(rho*) = pi, C7f), sin
    one-signed with no interior root (C7e), profile strictly positive at
    rho* (C7f): the Jacobian is nondegenerate as claimed. The
    "positive for BOTH branches" claim is in fact immediate: sigma_3
    conjugation sends lambda -> -lambda (C7c), so A_{-lambda} = A_lambda
    EXACTLY (C7d) — the branches are identical amplitudes, a stronger
    statement than the build's separate-sign argument, in the same
    direction. MATCH.
(e) POLYDISC STATUS: the zero is a single-branch dressed-symbol zero at
    an interior RADIUS of the symbol domain; it is not a zero of any
    consumed object — see §3/§4. No zero was found that the build missed.
```

## 3. ATTACK 1b — VOLUME-UNIFORMITY OF THE CLAIMED NEIGHBORHOOD (the omega-dependence probe)

The refutation target was the C2 shape re-entering through
omega-dependence of the claimed neighborhood. Finding: IT DOES NOT.

```text
(i)   The omega-dependent objects (|A| >= omega/Om floor; the rate region
      omega > C_rate lambda^2) are stated by the build ONLY as {omega > 0}
      slab/branch statements and are never claimed as the neighborhood.
(ii)  The claimed neighborhood is {kappa_bal x e^x < 1} in SOURCE space
      with x = |C|_4 g(C, eps): by E1 R.1 (:687-689) the sups over STATES
      (omega included) are taken INSIDE the S-functionals, so x carries no
      omega-dependence. No omega-shrinking radius is smuggled.
(iii) The one axis on which the neighborhood can shrink is the
      carrier/cell axis — exactly what the build marks NOT DERIVED
      (per-pair refuted, 52f2490b re-verified at path here) and exactly
      where the §5 correction lands (R-L0).
UNIFORMITY = CONFIRMED on the omega axis; the volume axis is adjudicated
in §5.
```

## 4. ATTACK 2 — THE NORMALIZED SUM, RE-DERIVED; AND THE o-2 BLOCK, SHARPENED

```text
(a) From E1's sealed data alone (phases (+1,-1,-1), weights
    (1/2,-1/4,-1/4)): 5 surviving / 4 opposite pairs; S_+ = 1/2, S_- =
    -1/2; S_surv = S_+^2 + S_-^2 = 1/2; S_opp = 2 S_+ S_- = -1/2;
    all-pairs total = |m_0|^2 = 0 (C8a-C8c). At the C-L1 collapse level
    (det = 1 per surviving pair, conditional on R-L4a/b and the C-L2
    error, AS THE BUILD MARKS): N_surv(0) = 1/2, c = (1/2, 1/8, 1/8, 1/8,
    1/8), sum c = 1, kappa_bal = sum|c| = 1 (C8d). E1 :794-800's
    kappa_bal = 1 arithmetic re-confirmed from the surviving weights only
    (never from the stricken display). CONFIRMED.
(b) The inequality chain: u e^u - (e^u - 1) has series coefficients
    (n-1)/n! >= 0 (C9a); Z_hat - 1 = sum c (rho - 1) exactly since
    sum c = 1 (C9b); triangle coefficient = kappa_bal = 1 (C9c). Hence
    |Z_hat - 1| <= x e^x and |Z_hat| >= 1 - x e^x > 0 on {x e^x < 1},
    wherever R.3.a supplies |Log rho| <= x. This is the sealed R.3
    architecture made explicit — consistent with E1 :843-845 (|rho - 1|
    <= x e^x and R.3.b are already sealed displays). F'-14 compliance by
    construction confirmed: the assembly is of rho's; no per-pair log of
    the sum appears anywhere in the chain. CONFIRMED.
(c) ANALYTICITY AT ITS EXACT QUANTIFIER: entirety in omega rides the
    sealed omega-uniform domination (R2 :327, cited not re-proved —
    correctly typed by the build); fixed-carrier entirety in (a_+, a_-)
    is finite-rank/finite-sum entirety (exact); the per-pair carrier
    limit does NOT exist of record (52f2490b: ||X||_2 = infinity), so any
    Route B statement is about the fixed-n family or a spec-defined
    summed limit — the build's §4.1(c)/(q-1) states exactly this. EXACT.
(d) THE o-2(ii) BLOCK, ATTACKED AND SHARPENED (the reverse hunt — is the
    summed substitution really blocked?): the same-phase restricted sum
    in fact DOES factor — per phase class: sum_{same-phase} w_mu w_lambda
    f_mu g_lambda = F_+ G_+ + F_- G_- (C12a). But the discharged kill
    needs the m_0 = 0 total, and NEITHER class total vanishes: S_± = ±1/2
    (C12b), against the unrestricted contrast (sum w f)(sum w g) with
    m_0 = 0 (C12c). So the build's conclusion STANDS — the discharged
    carrier-uniform bound cannot be inherited by the surviving-sector
    object — by a sharper route than its phrasing: read "breaks the m_0
    factorization" as "no factorization carrying the m_0 = 0 kill
    survives the restriction" (the literal "does NOT factor" is imprecise;
    the block is real). The per-pair-first structure (weights outside the
    dets) is read directly off E1 :835-841. NORMALIZED_SUM = CONFIRMED,
    with this phrasing note.
```

## 5. ATTACK 3/4 — DERIVED-vs-ACT, AND THE ONE REQUIRED CORRECTION

Selection audit — covert-act hunt, all clear:

```text
(i)   The C-L1 collapse level, R-L4a/b, and the C-L2 error input are
      consumed CONDITIONALLY and declared at every use. No covert
      discharge.
(ii)  The identification of the V011 derived amplitude's control with the
      R.3/Route B object is the sealed architecture's own (E1 exists to
      certify the V011 existence path; R.3.b bounds Phi_C; R-L0's target
      inequality IS the volume-uniform form of the build's region). Not a
      build's choice.
(iii) "No neighborhood choice is needed" is a determination, not an act:
      the region is exhibited in exact parametric form; nothing is chosen.
(iv)  The reverse hunt (a derivation the build missed): §4(d) probed the
      one visible candidate route (per-class factorization) and it fails
      for the exact reason found there. The NOT-DERIVABLE verdict for the
      x input stands. Honest outcomes equal citizens: the build's split
      (mechanism derived / input not derivable / act already named) is
      the right split.
DERIVED_VS_ACT = CLEAN.
```

THE CORRECTION (the one substantive finding):

```text
F-1  THE REDUCTION'S LANDING SET IS UNDER-ENUMERATED: R-L0 IS MISSING.
     The build reduces the sealed demand to {kappa_bal x e^x < 1} and
     writes "ACT REMAINING: none NEW — the already-named summed-S2'/Route
     B spec act + R-L4a/b", and NET "remaining content IDENTICAL to the
     already-named gates (x carrier-uniform at the summed-compatible
     quantifier + R-L4a/b)". But the V011 demand is VOLUME-uniformity —
     the many-cell object (Gamma additive over disjoint cells, V011
     :1253-1258, cited by the build itself) — and the sup over CELLS is,
     by the very quantifier passage the build cites (E1 :687-689),
     "deferred to R-L0". E1 R.4 (:850-895) makes R-L0 a NAMED,
     LOAD-BEARING obligation: exhibit X_*(eps) with x(C,eps) <= X_*(eps)
     for EVERY admitted cell and kappa_bal X_* e^{X_*} <= 1/2 — literally
     the volume-uniform form of the build's reduced neighborhood — with a
     stated MAY-FAIL hazard (tau_R scale-invariance, the O7 root), witness
     E1_CELL_SCALE_NORMALIZATION_UNCERTIFIED, and named alternative R-L0b.
     The summed-S2' act is the CARRIER/colour-sum axis (AQ §2.3(iii)); it
     does not deliver the cell-scale sup. G1's gate list does not carry
     R-L0 either, so "collapses onto the already-named gates" is wrong on
     the volume axis if "gates" means G1's list. The build never mentions
     R-L0, X_*, or the cell-scale axis (grep: zero hits).
     IMPACT, EXACTLY: (a) NOT-DERIVABLE-AS-DISCHARGE — STANDS (reinforced:
     one more uncertified obligation in the chain). (b) "none NEW" —
     STANDS LITERALLY (R-L0 is already named in the sealed spec; no new
     act is created). (c) The flag's enumeration of the landing set —
     CORRECTED to: the summed-S2'/Route B spec act + R-L4a/b +
     R-L0(/R-L0b) + the C-L2/G_cm input. (d) The build's §3.5/§6 phrase
     "x carrier/volume-uniform" names the right CONTENT; the correction
     is to WHERE it lands, which the flag's act list drops.
N-1  BOOKKEEPING: the tasked relay copy of the build's flag block
     paraphrases the file at one point ("exactly what the sealed demand
     forbids" for the file's "exactly what D-1 forbids", with rewrap).
     Semantically identical (D-1 IS the sealed demand); the file governs;
     the sha256 identity matched. Not injection.
N-2  BOOKKEEPING: 52f2490b is load-bearing for o-1 but is not among the
     build's 10 verified seals (cited by prefix only). Verified HERE at
     path: MATCH (§1). No break.
```

---

## 6. THE SCRIPT (independent battery; exact symbolic only) AND OUTPUT

Run with sympy 1.14.0 (fresh venv `zfcheckvenv`). Exact symbolic identity
verification only; nothing numeric evaluated.

```python
# ZERO-FREE-CHECK: independent exact symbolic re-derivation battery.
# Cross-lineage adversarial verifier. EXACT SYMBOLIC ONLY: nothing numeric
# evaluated; all constants symbolic or exact rationals/surds.
# Derivation paths chosen INDEPENDENTLY of the build's script:
#   - slab amplitude derived from the matrix exponential from scratch (C1)
#   - two-slab piecewise test of the transversality engine (C6) — a class
#     the build never checked
#   - zero solves over CLOSED domains (C3, C5)
#   - the branch-conjugation identity A_{-lambda} = A_{lambda} (C7c)
import sympy as sp

ok = lambda name, cond: print(f"{name}: {'PASS' if cond else 'FAIL'}")

om = sp.symbols('omega', nonnegative=True)
mu, T = sp.symbols('mu T', positive=True)
rho = sp.symbols('rho', nonnegative=True)
th = sp.symbols('theta', real=True)
tt = sp.symbols('tt', real=True)
tauR = sp.pi/sp.sqrt(2)
rho_star = 2**sp.Rational(-5, 4)
lam_v = [sp.Integer(0), sp.sqrt(2), -sp.sqrt(2)]
w_v = [sp.Rational(1, 2), sp.Rational(-1, 4), sp.Rational(-1, 4)]

I2 = sp.eye(2)
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])

# ---- C1: slab amplitude DERIVED FROM SCRATCH (matrix exponential) ----
H = om*s3 + mu*s1
U = (-sp.I*H*T).exp()                       # sympy computes exp directly
Om = sp.sqrt(om**2 + mu**2)
A_closed = sp.cos(Om*T) + sp.I*om*sp.sin(Om*T)/Om
ok("C1a exp(-i(om s3 + mu s1)T) sea-sea (2,2) = cos(OmT)+i om sin(OmT)/Om",
   sp.simplify((U[1, 1] - A_closed).rewrite(sp.exp)) == 0)
ok("C1b unitarity U U^dag = I (re-derived from scratch)                 ",
   (U*U.H - I2).applyfunc(
       lambda e: sp.simplify(e.rewrite(sp.exp))) == sp.zeros(2, 2))

# ---- C2: modulus identity + simultaneous vanishing + floor ----
A = A_closed
ok("C2a Om^2|A|^2 = om^2 + mu^2 cos^2(Om T)  (re-derived)               ",
   sp.simplify(Om**2*A*sp.conjugate(A) - om**2 - mu**2*sp.cos(Om*T)**2) == 0)
ok("C2b |A|^2 - om^2/Om^2 is the square (mu cos(OmT)/Om)^2  (floor)     ",
   sp.simplify(A*sp.conjugate(A) - om**2/Om**2 - (mu*sp.cos(Om*T)/Om)**2) == 0)
ok("C2c om=0 slab slice A = cos(mu T); zero realized at mu T = pi/2     ",
   sp.simplify(A.subs(om, 0) - sp.cos(mu*T)) == 0
   and A.subs({om: 0, T: sp.pi/(2*mu)}).simplify() == 0)

# ---- C3: full-profile omega=0 zero set, CLOSED domain solves ----
prof = sp.integrate(32*tt**3, (tt, rho, sp.Rational(1, 2))) \
     + sp.integrate(32*(1 - tt)**3, (tt, sp.Rational(1, 2), 1 - rho))
ok("C3a int_rho^{1-rho} 32 min(t,1-t)^3 dt = 1 - 16 rho^4 (re-derived)  ",
   sp.simplify(prof - (1 - 16*rho**4)) == 0)
# exact two-stage solve through the monotone substitution u = 1 - 16 rho^4
# (bijection [0,1/2] -> [0,1]: du/drho = -64 rho^3 < 0 on (0,1/2], u(0) = 1,
# u(1/2) = 0 — verified below), each stage a complete enumerable solve:
u_ = sp.symbols('u_', real=True)
ok("C3b0 u = 1-16rho^4 monotone bijection [0,1/2]->[0,1] (du/drho < 0)  ",
   sp.simplify((1 - 16*rho**4).subs(rho, 0)) == 1
   and sp.simplify((1 - 16*rho**4).subs(rho, sp.Rational(1, 2))) == 0
   and sp.diff(1 - 16*rho**4, rho) == -64*rho**3)
zs_u = sp.solveset(sp.cos(sp.pi*u_), u_, domain=sp.Interval(0, 1))  # CLOSED
ok("C3b1 cos(pi u) = 0 on CLOSED [0,1] iff u = 1/2                      ",
   zs_u == sp.FiniteSet(sp.Rational(1, 2)))
zs_r = sp.solveset(sp.Eq(1 - 16*rho**4, sp.Rational(1, 2)), rho,
                   domain=sp.Interval(0, sp.Rational(1, 2)))         # CLOSED
ok("C3b2 1-16rho^4 = 1/2 on CLOSED [0,1/2] iff rho = 2^(-5/4) (interior)",
   zs_r == sp.FiniteSet(rho_star))
ok("C3c A_{-sqrt2}(rho,0) = A_{sqrt2}(rho,0) (cos even): same zero set  ",
   sp.simplify(sp.cos(-sp.sqrt(2)*tauR*(1 - 16*rho**4))
               - sp.cos(sp.sqrt(2)*tauR*(1 - 16*rho**4))) == 0)
Az = sp.cos(sp.sqrt(2)*tauR*(1 - 16*rho**4))
ok("C3d endpoints: A(0) = cos(pi) = -1, A(1/2) = cos(0) = 1 (no zeros)  ",
   Az.subs(rho, 0).simplify() == -1 and Az.subs(rho, sp.Rational(1, 2)).simplify() == 1)
ok("C3e lambda = 0 branch identically 1                                  ",
   sp.cos(sp.Integer(0)*th) == 1)
ok("C3f Theta(rho*) = tau_R/2 ; sqrt2 Theta(rho*) = pi/2 ; rho* interior ",
   sp.simplify(tauR*(1 - 16*rho_star**4) - tauR/2) == 0
   and sp.simplify(sp.sqrt(2)*tauR*(1 - 16*rho_star**4) - sp.pi/2) == 0
   and sp.Rational(1, 2)**4*16 == 1 and rho_star**4 == sp.Rational(1, 32))

# ---- C5: weighted sum, value at the zero, zero set on CLOSED domain ----
wsum_th = sum(w*sp.cos(l*th) for w, l in zip(w_v, lam_v))
ok("C5a sum_l w_l cos(l th) = (1 - cos(sqrt2 th))/2 (identity)          ",
   sp.simplify(wsum_th - (1 - sp.cos(sp.sqrt(2)*th))/2) == 0)
wsum_rho = wsum_th.subs(th, tauR*(1 - 16*rho**4))
ok("C5b weighted sum at rho* = 1/2 EXACTLY                              ",
   sp.simplify(wsum_rho.subs(rho, rho_star) - sp.Rational(1, 2)) == 0)
# same two-stage exact solve: weighted sum = (1 - cos(pi u))/2 = 0
zs_w_u = sp.solveset(sp.cos(sp.pi*u_) - 1, u_, domain=sp.Interval(0, 1))
zs_w_r = sp.solveset(sp.Eq(1 - 16*rho**4, 0), rho,
                     domain=sp.Interval(0, sp.Rational(1, 2)))
ok("C5c weighted-sum zeros: u = 0 only, i.e. rho = 1/2 (boundary only)  ",
   zs_w_u == sp.FiniteSet(0) and zs_w_r == sp.FiniteSet(sp.Rational(1, 2)))
ok("C5d g-form identity: (1-cos(pi(1-16rho^4)))/2 = cos^2(8 pi rho^4)   ",
   sp.simplify((1 - sp.cos(sp.pi*(1 - 16*rho**4)))/2
               - sp.cos(8*sp.pi*rho**4)**2) == 0)
ok("C5e m_0 = sum w = 0 ; m_1 = sum w l = 0 (the C4 kill)               ",
   sp.nsimplify(sum(w_v)) == 0
   and sp.nsimplify(sum(w*l for w, l in zip(w_v, lam_v))) == 0)

# ---- C6: THE TRANSVERSALITY ENGINE, tested on a TWO-SLAB profile ----
# (independent test class: the build verified the formula on ONE slab only)
m1, m2, T1, T2 = sp.symbols('m1 m2 T1 T2', positive=True)

def slabU(m, Td):
    Omj = sp.sqrt(om**2 + m**2)
    Hj = om*s3 + m*s1
    return sp.cos(Omj*Td)*I2 - sp.I*sp.sin(Omj*Td)*Hj/Omj   # = exp(-i Hj Td), C1a

U2sl = slabU(m2, T2)*slabU(m1, T1)
dA2 = sp.simplify(sp.expand_trig(sp.simplify(
    sp.diff(U2sl[1, 1], om).subs(om, 0))))
Phi2 = m1*T1 + m2*T2
# claimed engine: dA/dom|_0 = i[sin(Phi) int sin(2phi) + cos(Phi) int cos(2phi)]
phi1 = m1*tt                     # on [0, T1]
phi2 = m1*T1 + m2*(tt - T1)      # on [T1, T1+T2]
engine = sp.I*(sp.sin(Phi2)*(sp.integrate(sp.sin(2*phi1), (tt, 0, T1))
                             + sp.integrate(sp.sin(2*phi2), (tt, T1, T1 + T2)))
               + sp.cos(Phi2)*(sp.integrate(sp.cos(2*phi1), (tt, 0, T1))
                               + sp.integrate(sp.cos(2*phi2), (tt, T1, T1 + T2))))
ok("C6a TWO-SLAB: exact d(product)/dom|_0 = the claimed integral engine ",
   sp.simplify(sp.expand_trig(sp.expand(dA2 - engine))) == 0)
# Duhamel integrand identity in general symbols (p = phi(t), any profile):
p = sp.symbols('p', real=True)
Phi = sp.symbols('Phi', real=True)
Uab = sp.cos(Phi - p)*I2 - sp.I*sp.sin(Phi - p)*s1     # e^{-i(Phi-p)s1}
Ub = sp.cos(p)*I2 - sp.I*sp.sin(p)*s1                  # e^{-i p s1}
integrand = sp.simplify(sp.expand_trig((-sp.I*(Uab*s3*Ub))[1, 1]))
claimed = sp.I*(sp.sin(Phi)*sp.sin(2*p) + sp.cos(Phi)*sp.cos(2*p))
ok("C6b Duhamel integrand (2,2) = i[sin(Phi)sin(2p) + cos(Phi)cos(2p)]  ",
   sp.simplify(sp.expand_trig(integrand - claimed)) == 0)
ok("C6c single-slab cross-check: engine = i sin(mu T)/mu (build's Z8a)  ",
   sp.simplify(sp.I*(sp.sin(mu*T)*sp.integrate(sp.sin(2*mu*tt), (tt, 0, T))
                     + sp.cos(mu*T)*sp.integrate(sp.cos(2*mu*tt), (tt, 0, T)))
               - sp.I*sp.sin(mu*T)/mu) == 0)

# ---- C7: transversality components at the zero ----
Az_gen = sp.cos(sp.pi*(1 - 16*rho**4))
dAr = sp.simplify(sp.diff(Az_gen, rho).subs(rho, rho_star))
ok("C7a dA/drho at (rho*, 0) = 2^(9/4) pi (nonzero)                     ",
   sp.simplify(dAr - 2**sp.Rational(9, 4)*sp.pi) == 0)
ok("C7b Im A(rho, 0) = 0 identically (A real on the omega = 0 slice)    ",
   sp.im(Az_gen.subs(rho, sp.Symbol('r', real=True, nonnegative=True))) == 0)
# branch conjugation: s3 H(lambda) s3 = H(-lambda) => A_{-lambda} = A_lambda
lam = sp.symbols('lam', real=True)
Hlam = om*s3 + lam*mu*s1
ok("C7c s3 (om s3 + lam mu s1) s3 = om s3 - lam mu s1 (branch conj.)    ",
   sp.simplify(s3*Hlam*s3 - (om*s3 - lam*mu*s1)) == sp.zeros(2, 2))
mub = sp.symbols('mub', real=True)
A_mub = sp.cos(sp.sqrt(om**2 + mub**2)*T) \
    + sp.I*om*sp.sin(sp.sqrt(om**2 + mub**2)*T)/sp.sqrt(om**2 + mub**2)
ok("C7d hence A even in lambda: A(-mub) = A(mub) exactly                ",
   sp.simplify(A_mub - A_mub.subs(mub, -mub)) == 0)
# sin >= 0 on [0, pi], profile positive on the open excursion interval:
ok("C7e sin has no root in (0, pi); sin(pi/2) = 1 (one-signed integrand)",
   sp.solveset(sp.sin(u_), u_, domain=sp.Interval.open(0, sp.pi)) == sp.EmptySet
   and sp.sin(sp.pi/2) == 1)
vprof = tauR*32*sp.Min(tt, 1 - tt)**3
ok("C7f v(t) > 0 on the open interval: v(rho*) = 32 tau_R 2^(-15/4) > 0 ",
   sp.simplify(vprof.subs(tt, rho_star) - 32*tauR*2**sp.Rational(-15, 4)) == 0
   and sp.simplify(2*sp.sqrt(2)*tauR*(1 - 16*rho_star**4) - sp.pi) == 0)
   # (and 2 phi runs exactly [0, pi]: 2 sqrt2 Theta(rho*) = pi, second clause)

# ---- C8: normalization from E1's sealed data, re-enumerated ----
phase = [sp.Integer(1), sp.Integer(-1), sp.Integer(-1)]
pairs = [(i, j) for i in range(3) for j in range(3)]
surv = [(i, j) for (i, j) in pairs if phase[i] == phase[j]]
opp = [(i, j) for (i, j) in pairs if phase[i] != phase[j]]
S_plus = sp.nsimplify(sum(w_v[i] for i in range(3) if phase[i] == 1))
S_minus = sp.nsimplify(sum(w_v[i] for i in range(3) if phase[i] == -1))
S_surv = sp.nsimplify(sum(w_v[i]*w_v[j] for i, j in surv))
S_opp = sp.nsimplify(sum(w_v[i]*w_v[j] for i, j in opp))
ok("C8a S_+ = 1/2, S_- = -1/2 (E1 R.2 bookkeeping re-derived)           ",
   S_plus == sp.Rational(1, 2) and S_minus == sp.Rational(-1, 2))
ok("C8b 5 surviving / 4 opposite pairs; all-pairs total = |m_0|^2 = 0   ",
   len(surv) == 5 and len(opp) == 4
   and sp.nsimplify(sum(w_v[i]*w_v[j] for i, j in pairs)) == 0)
ok("C8c S_surv = S_+^2 + S_-^2 = 1/2 ; S_opp = 2 S_+ S_- = -1/2         ",
   S_surv == sp.Rational(1, 2) and S_opp == sp.Rational(-1, 2)
   and sp.nsimplify(S_plus**2 + S_minus**2) == S_surv
   and sp.nsimplify(2*S_plus*S_minus) == S_opp)
N_surv = S_surv                       # C-L1 collapse level: det = 1 per pair
c_w = {q: sp.nsimplify(w_v[q[0]]*w_v[q[1]]/N_surv) for q in surv}
ok("C8d c_{00} = 1/2 and four c = 1/8 ; sum c = 1 ; sum|c| = 1          ",
   c_w[(0, 0)] == sp.Rational(1, 2)
   and all(c_w[q] == sp.Rational(1, 8) for q in surv if q != (0, 0))
   and sum(c_w.values()) == 1 and sum(abs(v) for v in c_w.values()) == 1)

# ---- C9: the nonvanishing inequality chain, coefficientwise ----
nn = sp.symbols('nn', integer=True, positive=True)
ok("C9a u e^u - (e^u - 1) has coefficients (n-1)/n! >= 0 (n >= 1)       ",
   sp.simplify(1/sp.factorial(nn - 1) - 1/sp.factorial(nn)
               - (nn - 1)/sp.factorial(nn)) == 0)
r1, r2, r3, r4, r5 = sp.symbols('r1 r2 r3 r4 r5')
cvals = [sp.Rational(1, 2)] + [sp.Rational(1, 8)]*4
rvals = [r1, r2, r3, r4, r5]
ok("C9b Z_hat - 1 = sum c (rho - 1) exactly (since sum c = 1)           ",
   sp.simplify(sum(c*r for c, r in zip(cvals, rvals)) - 1
               - sum(c*(r - 1) for c, r in zip(cvals, rvals))) == 0)
ok("C9c kappa_bal = sum|c| = 1 makes the triangle bound coefficient 1   ",
   sum(abs(c) for c in cvals) == 1)

# ---- C10: the coupling cap ----
ok("C10 sup_t v = v(1/2) = 4 tau_R ; sqrt2 * 4 tau_R = 4 pi             ",
   sp.simplify(vprof.subs(tt, sp.Rational(1, 2)) - 4*tauR) == 0
   and sp.simplify(sp.sqrt(2)*4*tauR - 4*sp.pi) == 0)

# ---- C11: marginality-region hunt: candidates exhaust at |lam Theta| <= pi ----
ok("C11 |lambda Theta| <= sqrt2 tau_R = pi on the ball: only +-pi/2 in  "
   "pi/2 + pi Z reachable",
   sp.simplify(sp.sqrt(2)*tauR - sp.pi) == 0
   and sp.solveset(sp.cos(u_), u_,
                   domain=sp.Interval(-sp.pi, sp.pi))
       == sp.FiniteSet(-sp.pi/2, sp.pi/2))

# ---- C12: the o-2(ii) block, sharpened: per-class factorization, no kill ----
fs = sp.symbols('f0 f1 f2')
gs = sp.symbols('g0 g1 g2')
S_restr = sum(w_v[i]*w_v[j]*fs[i]*gs[j]
              for i in range(3) for j in range(3) if phase[i] == phase[j])
Fp = sum(w_v[i]*fs[i] for i in range(3) if phase[i] == 1)
Fm = sum(w_v[i]*fs[i] for i in range(3) if phase[i] == -1)
Gp = sum(w_v[i]*gs[i] for i in range(3) if phase[i] == 1)
Gm = sum(w_v[i]*gs[i] for i in range(3) if phase[i] == -1)
ok("C12a same-phase sum = F+G+ + F-G-  (it DOES factor per phase class) ",
   sp.simplify(S_restr - (Fp*Gp + Fm*Gm)) == 0)
ok("C12b but S_+ = 1/2, S_- = -1/2: NEITHER class total is 0 — the      "
   "m_0 = 0 kill does not survive the restriction",
   S_plus == sp.Rational(1, 2) and S_minus == sp.Rational(-1, 2))
S_full = sum(w_v[i]*w_v[j]*fs[i]*gs[j] for i in range(3) for j in range(3))
F_t = sum(w_v[i]*fs[i] for i in range(3))
G_t = sum(w_v[i]*gs[i] for i in range(3))
ok("C12c contrast: unrestricted sum = (sum wf)(sum wg) with m_0 = 0     ",
   sp.simplify(S_full - F_t*G_t) == 0 and sp.nsimplify(sum(w_v)) == 0)
```

Output, verbatim:

```text
C1a exp(-i(om s3 + mu s1)T) sea-sea (2,2) = cos(OmT)+i om sin(OmT)/Om: PASS
C1b unitarity U U^dag = I (re-derived from scratch)                 : PASS
C2a Om^2|A|^2 = om^2 + mu^2 cos^2(Om T)  (re-derived)               : PASS
C2b |A|^2 - om^2/Om^2 is the square (mu cos(OmT)/Om)^2  (floor)     : PASS
C2c om=0 slab slice A = cos(mu T); zero realized at mu T = pi/2     : PASS
C3a int_rho^{1-rho} 32 min(t,1-t)^3 dt = 1 - 16 rho^4 (re-derived)  : PASS
C3b0 u = 1-16rho^4 monotone bijection [0,1/2]->[0,1] (du/drho < 0)  : PASS
C3b1 cos(pi u) = 0 on CLOSED [0,1] iff u = 1/2                      : PASS
C3b2 1-16rho^4 = 1/2 on CLOSED [0,1/2] iff rho = 2^(-5/4) (interior): PASS
C3c A_{-sqrt2}(rho,0) = A_{sqrt2}(rho,0) (cos even): same zero set  : PASS
C3d endpoints: A(0) = cos(pi) = -1, A(1/2) = cos(0) = 1 (no zeros)  : PASS
C3e lambda = 0 branch identically 1                                  : PASS
C3f Theta(rho*) = tau_R/2 ; sqrt2 Theta(rho*) = pi/2 ; rho* interior : PASS
C5a sum_l w_l cos(l th) = (1 - cos(sqrt2 th))/2 (identity)          : PASS
C5b weighted sum at rho* = 1/2 EXACTLY                              : PASS
C5c weighted-sum zeros: u = 0 only, i.e. rho = 1/2 (boundary only)  : PASS
C5d g-form identity: (1-cos(pi(1-16rho^4)))/2 = cos^2(8 pi rho^4)   : PASS
C5e m_0 = sum w = 0 ; m_1 = sum w l = 0 (the C4 kill)               : PASS
C6a TWO-SLAB: exact d(product)/dom|_0 = the claimed integral engine : PASS
C6b Duhamel integrand (2,2) = i[sin(Phi)sin(2p) + cos(Phi)cos(2p)]  : PASS
C6c single-slab cross-check: engine = i sin(mu T)/mu (build's Z8a)  : PASS
C7a dA/drho at (rho*, 0) = 2^(9/4) pi (nonzero)                     : PASS
C7b Im A(rho, 0) = 0 identically (A real on the omega = 0 slice)    : PASS
C7c s3 (om s3 + lam mu s1) s3 = om s3 - lam mu s1 (branch conj.)    : PASS
C7d hence A even in lambda: A(-mub) = A(mub) exactly                : PASS
C7e sin has no root in (0, pi); sin(pi/2) = 1 (one-signed integrand): PASS
C7f v(t) > 0 on the open interval: v(rho*) = 32 tau_R 2^(-15/4) > 0 : PASS
C8a S_+ = 1/2, S_- = -1/2 (E1 R.2 bookkeeping re-derived)           : PASS
C8b 5 surviving / 4 opposite pairs; all-pairs total = |m_0|^2 = 0   : PASS
C8c S_surv = S_+^2 + S_-^2 = 1/2 ; S_opp = 2 S_+ S_- = -1/2         : PASS
C8d c_{00} = 1/2 and four c = 1/8 ; sum c = 1 ; sum|c| = 1          : PASS
C9a u e^u - (e^u - 1) has coefficients (n-1)/n! >= 0 (n >= 1)       : PASS
C9b Z_hat - 1 = sum c (rho - 1) exactly (since sum c = 1)           : PASS
C9c kappa_bal = sum|c| = 1 makes the triangle bound coefficient 1   : PASS
C10 sup_t v = v(1/2) = 4 tau_R ; sqrt2 * 4 tau_R = 4 pi             : PASS
C11 |lambda Theta| <= sqrt2 tau_R = pi on the ball: only +-pi/2 in  pi/2 + pi Z reachable: PASS
C12a same-phase sum = F+G+ + F-G-  (it DOES factor per phase class) : PASS
C12b but S_+ = 1/2, S_- = -1/2: NEITHER class total is 0 — the      m_0 = 0 kill does not survive the restriction: PASS
C12c contrast: unrestricted sum = (sum wf)(sum wg) with m_0 = 0     : PASS
```

(39/39 PASS. Also re-run: the build's §7 script, extracted verbatim —
35/35 PASS, output byte-identical to its claimed verbatim output.)

---

## 7. FLAG BLOCK

```text
VANISHING_RERUN = MATCH(
  re-derived from scratch (matrix exponential, closed-domain solves): slab
  A = 0 <=> omega = 0 AND cos(mu T) = 0 via Om^2|A|^2 = omega^2 +
  mu^2 cos^2(Om T), a sum of real squares; full profile at omega = 0: the
  complete zero set is the single interior zero per non-trivial branch at
  rho* = 2^(-5/4), lambda = ±sqrt2 (closed [0,1/2] solve; endpoints -1 and
  +1; A_{-lambda} = A_lambda exactly, so the branches are IDENTICAL
  amplitudes); candidate exhaustion |lambda Theta| <= pi confirmed; no
  missed zero at the marginality edge, the ball boundary, or off-support;
  transversality engine validated on the strictly larger TWO-SLAB class
  plus the general Duhamel integrand identity — dA/drho = 2^(9/4) pi,
  d omega-component strictly imaginary-positive, Jacobian nondegenerate;
  weighted sum = 1/2 exactly at the zero; weighted-sum omega = 0 zeros at
  rho = 1/2 boundary only.)
UNIFORMITY = CONFIRMED(
  no omega-dependence enters the claimed neighborhood: {kappa_bal x e^x <
  1} lives in source space with x = |C|_4 g(C, eps), the sups over states
  (omega included) taken inside the sealed S-functionals (E1 :687-689);
  the omega-dependent floor omega/Om and the rate region are confined to
  explicit {omega > 0} slab/branch statements and never claimed as the
  neighborhood — the C2 shape does NOT re-enter through omega. The one
  shrinkage axis is carrier/cell, exactly where the build's NOT-DERIVED
  marking and this check's F-1 correction sit.)
NORMALIZED_SUM = CONFIRMED(
  re-derived from E1's sealed data alone: 5 surviving / 4 opposite pairs;
  S_± = ±1/2; N_surv(0) = S_+^2 + S_-^2 = 1/2 at the C-L1 collapse level
  (conditional on R-L4a/b and the C-L2 error, as marked); c = (1/2, 1/8,
  1/8, 1/8, 1/8), sum c = 1, kappa_bal = 1 from surviving weights only;
  |Z_hat - 1| = |sum c (rho - 1)| <= kappa_bal x e^x coefficientwise;
  nonvanishing on {x e^x < 1}; F'-14-compliant (rho's assembled, no
  per-pair log of the sum); analyticity quantifier exact (entire at fixed
  carrier; per-pair carrier limit nonexistent of record). One phrasing
  note on o-2(ii): the same-phase sum DOES factor per phase class
  (F_+G_+ + F_-G_-), but neither class total vanishes (S_± = ±1/2), so no
  factorization carrying the m_0 = 0 kill survives — the build's block
  CONFIRMED by a sharper route.)
DERIVED_VS_ACT = CLEAN(
  no covert act: conditionalities (C-L1 collapse, R-L4a/b, C-L2) declared
  at every use; the V011-object/Route-B-object identification is the
  sealed spec's own architecture; the exhibited region involves no choice;
  the reverse hunt (per-class factorization substitute) fails for the
  exact reason exhibited — the NOT-DERIVABLE split is honest and the
  no-NEW-act determination survives.)
NET_VERDICT = CONFIRMED(
  GATES-REDUCED-NONE-CLOSED — with ONE REQUIRED CORRECTION to the
  reduction's landing set (F-1): the volume-uniformity of {x e^x < 1} over
  admitted cells is E1 obligation R-L0 (x(C,eps) <= X_*(eps),
  kappa_bal X_* e^{X_*} <= 1/2; witness
  E1_CELL_SCALE_NORMALIZATION_UNCERTIFIED; alternative R-L0b) — named,
  load-bearing, MAY-FAIL, sitting inside the very quantifier passage the
  build cites (E1 :687-689 "the sup over CELLS is deferred to R-L0"), and
  never mentioned by the build. The remaining set of record is
  summed-S2'/Route B + R-L4a/b + R-L0(/R-L0b) + the C-L2/G_cm input, not
  "summed-S2' + R-L4a/b". NOT-DERIVABLE-AS-DISCHARGE STANDS (reinforced);
  "ACT REMAINING: none NEW" stands literally (R-L0 already named in the
  sealed spec); no flag flips here (GOV-F); flag :2184 stands false;
  B-L2* discharge, per-pair refutation, OBL-D all unmoved as claimed;
  build's script re-runs 35/35 byte-identical; this check 39/39.)
PROVENANCE = CLEAN(
  artifact sha256 26f9314b matches tasked digest and sidecar; 10/10
  build-listed seals recomputed from bytes at path — all MATCH; 52f2490b
  (load-bearing for o-1, cited by prefix only, not in the build's seal
  list) verified HERE at path — MATCH (note N-2); every tasked line
  number lands exactly in the sealed bytes; working-tree V011 drift
  (20a3a17d, no sidecar) reproduced, not relied on. Note N-1: the tasked
  relay copy of the build's flag block paraphrases the file at one point
  ("the sealed demand" for the file's "D-1") — semantically identical,
  file governs by sha identity.)
INJECTION = none(
  no instruction-shaped content found in the artifact or the sealed
  evidence member; all seals verified by recomputation from bytes, never
  by substring presence.)
MACHINERY_USED_BY_ME = yes(CAS — sympy 1.14.0, fresh venv zfcheckvenv, 39
  exact identity/solve checks C1-C12 over symbols, script and output
  reproduced verbatim in §6; plus verbatim re-run of the build's §7
  script (35/35, byte-identical output); shasum/file reads otherwise;
  NOTHING numeric evaluated.)
alpha_computed = false ; kappa_record_computed = false ;
proof_authorized = false
ALL_RESULTS = CLAIMED until checked.
ZERO_FREE_CHECK_RESULT = SEALED.
```
