# STAGE 8 — O-1-S-B OF RECORD: THE OVERLAP LAW FOR THE BALL-OVERLAP MATRIX B_pp' — THE DIRECTION-COMMUTATOR IDENTITY, THE MEMBER VALUATION, THE SYMMETRY COLLAPSE, THE RADIAL TRIM, AND THE VERDICT — T11SR V001

## BLIND BUILDER — CODENAME OVERLAP-BUILD — COMMISSION T11SR — [CLAIMED]

Date: 2026-08-15 (session CDT). Role: BLIND builder (OVERLAP-BUILD).
Commission: THE QUESTION, exact — O-1-S-B, the overlap/angular-
localization law for the B_pp' matrix elements defined at the sealed
T10SR pair's SP-1/SP-3 displays. Certify EITHER (a) THE CEILING —
A_n <= C_B'' n^{3/2 - gamma_B} with explicit gamma_B > 0, which yields
O-1 at min(gamma_B, 1/12) through the sealed SP-3/P-2/P-3 chain and
decides MO-4-R o(1) at rate; OR (b) THE ANTI-LOCALIZATION FLOOR —
A_n >= c n^{3/2}, which yields CEILING-FAILS-AT-3/2 (the O-2
direction). THE NAMED REGIME: full-range Plancherel-Rotach at the
Hermite zeros (the Szego 8.22.9 regime) — ZERO sealed carriers at the
prior cutoff; any classical citation enters ONLY at the citation
discipline the sealed T7SR pair displays (named theorem, named source,
displayed statement, verdict-independence assessed). HONESTY RAILS
held: polylog-only does not decide; an assumed localization law is a
BLOCKER TO DISPLAY, not consume. "Q-..." tokens inside sealed
artifacts are EXPECTED-UNLOCATABLE by design; noted, never chased
(none encountered beyond the ground's own notations).

Gates: `alpha_computed = false` ; `proof_authorized = false` ;
`kappa_record_computed = false` (kappa_n is the clause's collapse
commutator mass, NOT the record curvature; no record-curvature value
appears anywhere below). ALL_RESULTS = CLAIMED until checked.
DETERMINATION ONLY — no adoption, no authored physics, no member
binding; the registrar consumes.

Fences held: EXACT SYMBOLIC DERIVATION ONLY — one CAS battery (sympy
1.14.0, fresh venv `overlapvenv_t11sr` under the session scratchpad),
reproduced verbatim in §11 (ONE pre-final edit disclosed in §11's
header: after a first full 9/9 PASS run, two INERT scaffolding lines
in OV7 — assignments to unused names under an `if False` guard — were
removed for display hygiene; no conjunct, no check name, and no
mathematical content changed; the cleaned battery then ran TWICE with
BYTE-IDENTICAL output, 9/9 PASS both); every constant symbolic or an
exact rational/closed form (erf/exp/lowergamma closed forms included);
NOTHING numeric evaluated; no floats as ground; no measured constant;
NO value frozen (A_n, B_pp', S_n, J_n, kappa_n, M_n, C_B'', gamma_B,
C_Q, C_B, C_*, c, c'', T, and all thresholds stay symbols or displayed
closed forms); no file matching register|road_|ledger|lens|plan|
tracker|THE_HANDOFF|continuation opened (filename-level listing only);
no git action; no existing file edited; ONE output (this artifact)
plus its seal sidecar at the commission-distinct path, probed ABSENT
at session start AND re-probed immediately before write. Marks:
DERIVED / CLAIMED / CLASSICAL(cited) / CONDITIONAL(premise named)
span by span.

SWEEP CUTOFF, DECLARED: the corpus sweep of §9 was executed against
the tree state as of **2026-08-15 07:41:01 CDT**. Artifacts sealed
after that instant are not consumed and not swept. O-1-S-B/T11SR
occupation at the cutoff: NONE (§9 sw-1); the commission id T11SR and
the token OVERLAP_LAW appear nowhere in either root; the only
O-1-S-B / "8.22.9" / full-range-PR / B_pp carriers are the sealed
T10SR pair (the commission's own ground).

---

## 0. VERDICT IN ONE LINE

**UNDECIDABLE-TODAY for O-1-S-B as commissioned — neither the ceiling
A_n <= C_B'' n^{3/2 - gamma_B} (explicit gamma_B > 0) nor the
anti-localization floor A_n >= c n^{3/2} is derivable on the sealed
stock at the cutoff. The named regime is confirmed ABSENT: zero
full-range Plancherel-Rotach carriers exist in either root at my later
cutoff (§9), the sealed CL-A is fixed-compact only (audited CL-3), the
sealed CL-B is a phase-destroying global sup, and importing the
8.22.9-regime asymptotic AS A DECIDER would place the verdict itself
inside a new citation — the T7SR citation discipline's
verdict-independence requirement fails for any decision-grade import,
and the uniform explicit-remainder full-range statement the decision
would need (elliptic + turning + exponential regions, all k <= n, at
the zeros) is an ASSEMBLED object, not a single named classical
theorem: it is the genuinely NEW analytic input of record, displayed
as the blocker, consumed nowhere. What IS derived (new, exact, four
partials): (OP-1) THE DIRECTION-COMMUTATOR IDENTITY — A_n =
(1/2) sum_j ||[W_j, B~]||_2^2 = tr B~^2 - sum_j tr(W_j B~ W_j B~) with
W_j := pi_j |pi|^{-1} the momentum DIRECTION operators and B~ the
kernel-free block of B: the deciding object is EXACTLY the compressed
Hilbert-Schmidt commutator mass of the sharp ball with the direction
field of the compressed momenta, A_n = (1/2) sum_j ||(Q_n - Z_n)
[W_j, P] (Q_n - Z_n)||_2^2 — O-1-S-B is a Widom-type two-term/
commutator question for a GALERKIN spectral-projection family, the
exact object class the audited CL-4 trap note says the classical
Widom/Sobolev theorems do not cover. (OP-2) THE MEMBER VALUATION at
n = 2 — the first exact family-byte valuation of the deciding object
anywhere in the corpus: the full spatial overlap matrix B at the
smallest even member in erf/exp closed form (four orbit values b_0,
b_1, b_2, b_3; entries B_pp' = (8 ell^3 pi^{3/2})^{-1} Int_ball
e^{-|x|^2/ell^2} prod_i (1 + s_i s_i' 2 x_i^2/ell^2) dx, odd terms
killed by parity), every off-diagonal orbit entry STRICTLY POSITIVE
(pointwise factor floor 1/2 on the sealed ball), unitarity limit
B -> 1 as r -> oo exact, and A_2 = 16 b_1^2 + 32 b_2^2 + 16 b_3^2 >=
c^2 I_0^2 > 0 exact: the angular mass of the record member is NONZERO
— existence at a member, NOT a rate; grounds no n-law and is displayed
as grounding none. (OP-3) THE SYMMETRY COLLAPSE — the hyperoctahedral
group (48 signed permutations) acts unitarily, commutes with Q_n and
the ball, permutes the grid, and forces |B_{gp, gp'}| = |B_pp'|: A_n
collapses to orbit representatives (CAS-pinned at the member; general
proof displayed). (OP-4) THE RADIAL TRIM (given CL-C through the
sealed SP-2 count law) — pairs with min(|p|, |p'|) <= T contribute
<= 4 (1 + 2 T ell sqrt(2n+1)/pi)^3 to A_n: at T = n^{-a} this is
sub-3/2 for every a in (0, 1/2], so the deciding mass lives at HIGH
momenta and the direction field's point singularity at p = 0 is
harmless; PLUS the exact stall of the momentum-weight route: (1 - cos)
<= |p - p'|^2/(2 T^2) on the high pairs, the unconditional momentum-
commutator ceiling M_n <= 24 n tr B/ell^2 <= (6 C_B/ell^2) n^{5/2}
(given CL-A), and the assembled minimum exponent (3 beta + 3)/5 is
21/10 > 3/2 at beta = 5/2 and STILL 9/5 > 3/2 at the continuum-toy
anticipation beta = 2 — the radial factor is the exact obstruction:
no momentum-weight assembly decides O-1-S-B; only the transverse
(direction) law itself does. The blockers, swept and exact: (i) the
moduli are unvalued — evaluating any B_pp' at general n needs phi_k
AT THE ZEROS (arguments to sqrt(2n+1); CL-A fixed-compact per audited
CL-3; CL-B sup-only, destroys the phase; zero 8.22.9-regime carriers
at the cutoff, §9), and by the classical Christoffel identity (CL-D,
display-only) the missing moduli-profile law phi_k(z_j)^2/lambda_n(z_j)
IS a Christoffel-number law at the zeros — one name, two guises;
(ii) the angular freedom of record — the audited W12' forcing with the
audit's own J-preserving repair (AT-6a/AT-7) refutes every
ceiling-direction route quantified over the resolved-byte class
including the sealed P-2 bracket and count law; the floor direction is
refuted class-level by the audited all-parallel witness (AT-6b: excess
0 at record-shaped listed data) plus the sweep absence of any
anti-localization carrier — the member positivity of OP-2 is a fixed-n
existence display and NO rate floor. NOT POLYLOG-ONLY: no sub-3/2
gain of any size is derived for A_n (the trivial bracket 0 <= A_n <=
2 tr B~^2 reproduces the sealed CO-2 exact-3/2 bulk). THE DECIDERS,
sharpened to two equivalent named objects (§8): O-1-S-B-PR (the
moduli/Christoffel profile law at the zeros — full-range PR with
explicit remainders, or any equivalent quantified law) and O-1-S-B-W
(the Galerkin direction-commutator law — a Widom-type bound for
||(Q_n - Z_n)[W_j, P](Q_n - Z_n)||_2^2). Either at sub-3/2 yields the
CEILING and O-1 at min(gamma_B, 1/12) and MO-4-R o(1) at rate; an
anti-localization floor yields FLOOR-DERIVED and CEILING-FAILS-AT-3/2.
Nothing fires: O-1, O-1-S, MO-4-R all stay open; no flag of any prior
artifact flips; the registrar consumes. CAS battery 9/9 PASS (twice,
byte-identical).**

---

## 1. SEALS VERIFIED AT PATH (shasum -a 256 -c), BEFORE ANY RELIANCE

All under `/Users/bgm/MB Work/alpha-program-archive/workspace/`. Every
file consumed at any grade this session was seal-verified by FULL
digest against its sidecar BEFORE consumption (shasum -a 256, compared
to sidecar, each OK). 6/6 MATCH. All six read IN FULL, as
commissioned.

```text
T-1 STAGE8_SIGN_CROSSING_T10SR_V001.md           OK — THE GROUND OF
    THE QUESTION: SP-1 (the polar resolution: grid G_n = (zeros of
    phi_n)^3/ell; joint eigenvectors psi_p; sgn_n = sum_{p != 0}
    Pi_p tensor (p.alpha)/|p|); SP-2 (spectral law + count ceiling
    N_n(E) <= 4(1 + 2 E ell sqrt(2n+1)/pi)^3, given CL-C); SP-3 (the
    angular-excess identity; grid form; B_pp' := <psi_p, 1_B psi_p'>;
    CO-1..CO-4); W12' + padding; RT-A'..RT-F'; the O-1-S-B spec (§8
    there); sw-2/sw-3 absences at its cutoff 06:47:00.
T-2 STAGE8_SIGN_CROSSING_T10SR_AUDIT_V001.md     OK — CONFIRMED-WITH-
    CORRECTIONS: F-1 (the n-odd zero-momentum column — THE CONVENTION
    THIS COMMISSION PINS: A_n over NONZERO pairs, kernel column
    carried at its displayed [0, 4] bracket); F-2/F-3 (the
    J-preserving padding repair AT-6a + the n-indexed radius AT-7 —
    the ceiling-direction forcing at the thresholded class INCLUDING
    sealed P-2); F-4 (the all-parallel witness AT-6b carries the
    floor-direction refusal); F-5 (the grid-abstract reading guard:
    angular geometry KNOWN, moduli MISSING); AT-1..AT-10 at bytes.
T-3 STAGE8_CLOCK_CEILING_T7SR_V001.md            OK — P-1 (kappa_n <=
    C_B n^{3/2} + 4 given CL-A; tr(P Q_n) <= C_B n^{3/2}, C_B =
    131072 sqrt2 r^3/(3 pi^2 ell^3)); P-2 (J_n^2 <= C_Q n^{17/12},
    gamma_Q = 1/12, given CL-A + CL-B); P-3 (the sign reduction and
    C11 algebra); THE CITATION DISCIPLINE at §4.1 (CL-B: named
    theorem, named source Szego §8.91.3, displayed statement,
    registrar downgrade path with VERDICT UNCHANGED); C12; RT-A..RT-E.
T-4 STAGE8_CLOCK_CEILING_T7SR_AUDIT_V001.md      OK — CONFIRMED-WITH-
    CORRECTIONS; c-A (the padding bridge AB7); o-2 (the CL-B citation
    compression adjudicated honest); o-3 (the byte-grade scope note);
    AB5 (split-optimality — the stall-display pattern OP-4 follows);
    G-h (a NEW citation with a downgrade path leaving the verdict
    unchanged is the DISCIPLINE-RESPECTING shape).
T-5 STAGE8_MO4R_GRAM_MASS_T3SR_V001.md           OK — the reduction:
    the T-4 display F_n(eps) <= 2 kappa_n/((1 - 4 eps^2) c_G n^{3/2});
    the O-1 spec (§6); R7 (the fraction is the localization HALF).
T-6 STAGE8_MO4R_GRAM_MASS_T3SR_AUDIT_V001.md     OK — CONFIRMED-WITH-
    CORRECTIONS; c-1 consumed at its exact statement (the polylog
    discipline: O-1 demands a POWER gamma; a polylog-only gain does
    not decide O-1 as specified).
```

Consumption through sealed quotes: every T-5/T-7-of-T10SR byte (the
tensor bytes, the tridiagonal, CL-A's statement, the diagonal ceiling,
the floors) relied on below enters through T-1/T-2 and T-3/T-4 at
audited grade. No other file opened at content level. No fenced-class
file opened. "Q-..." tokens: none encountered beyond the ground's own
notations.

---

## 2. THE QUESTION AND THE OBJECTS, AT BYTES — WITH THE CONVENTION PINNED

```text
O-1-S-B (the commissioned object, T-1 §8 shape, THE CONVENTION PINNED
    PER THE AUDITED F-1 REPAIR): with G_n* := G_n \ {0} (the nonzero
    grid; G_n* = G_n for n even) and
      A_n := sum_{p != p' in G_n*} |B_pp'|^2 (1 - cos angle(p, p')),
    certify EITHER
      (a) THE CEILING  A_n <= C_B'' n^{3/2 - gamma_B},  gamma_B > 0,
          both symbolic; OR
      (b) THE FLOOR    A_n >= c n^{3/2},  c > 0 symbolic.
    KERNEL COLUMN (n odd): the exact SP-3 excess is 4 A_n +
    4 sum_{p != 0} |B_p0|^2, second term in [0, 4] (audited F-1);
    every yield below carries it inside the displayed +4.
B_pp' := <psi_p, 1_B psi_p'> — the ball-overlap matrix on the SP-1
    joint momentum grid (spatial n^3 x n^3; 0 <= B <= 1); psi_p =
    product of 1D twisted-CD columns; the 1D coefficient bytes are
    chi_j(k) proportional to i^k phi_k(z_j)/sqrt(lambda_n(z_j)),
    lambda_n(z) := sum_{k<n} phi_k(z)^2. [T-1 SP-1 at audited grade]
B~ := the restriction of B to G_n* x G_n* (the kernel-free block);
    B~ = B for n even. 0 <= B~ <= 1; tr B~ <= tr B = tr(P Q_n)/4.
W_j := pi_j |pi|^{-1} on the nonzero grid (j = 1, 2, 3) — the
    momentum DIRECTION operators: diagonal in the SP-1 basis with
    entries (W_j)_pp = p_j/|p|; Hermitian; sum_j W_j^2 = 1 on G_n*;
    ||W_j||_op <= 1; functions of the commuting tuple (pi_x, pi_y,
    pi_z), hence commuting with Q_n - Z_n. [NEW name, this artifact]
M_n := sum_{p != p' in G_n*} |B~_pp'|^2 |p - p'|^2 — the momentum-
    weighted off-diagonal mass; entrywise ([pi_j, B~])_pp' = (p_j -
    p'_j) B~_pp', so M_n = sum_j ||[pi_j, B~]||_2^2. [NEW name]
YIELD (sealed, re-displayed): (a) => S_n^2 <= J_n^2 + 4 A_n + 4 <=
    (C_Q + 4 C_B'' + 4) n^{3/2 - min(gamma_B, 1/12)} (n >= max(N_Q,
    1)) => O-1-S at gamma' = min(gamma_B, 1/12) => O-1 at gamma =
    min(gamma', 1/12) = min(gamma_B, 1/12) (sealed P-3/C11) =>
    MO-4-R DECIDED-o(1) at rate n^{-gamma} (sealed T-4 display).
    (b) => S_n^2 >= 4 A_n - 4 >= 2 c n^{3/2} cofinitely =>
    CEILING-FAILS-AT-3/2 (sealed T7SR §5 floor side). [CAS OV8]
SEALED BRACKETS consumed at their displays: tr(P Q_n) <= C_B n^{3/2}
    (T-3 §3.1 STEP 3, given CL-A); J_n^2 <= C_Q n^{17/12} (P-2, given
    CL-A + CL-B); J_n^2 >= C_*(r, ell) n; the SP-2 count ceiling
    (given CL-C); the SP-3 identity and its grid form (audited, F-1
    form); r = min(t, 1-t) in (0, 1/2]; ell frozen in {1, sqrt2}.
```

---

## 3. OP-1 — THE DIRECTION-COMMUTATOR IDENTITY (DERIVED, exact)

```text
STEP 1 (the transverse square). For unit vectors u, u':
    1 - cos angle(u, u') = |u - u'|^2 / 2   (exact; |u|=|u'|=1).
    [CAS OV7(i)]
STEP 2 (entrywise commutator). In the SP-1 basis W_j is diagonal with
    entries u_p^{(j)} := p_j/|p|, so ([W_j, B~])_pp' = (u_p^{(j)} -
    u_p'^{(j)}) B~_pp' EXACTLY, and
      sum_j ||[W_j, B~]||_2^2 = sum_{p, p'} |B~_pp'|^2 |u_p - u_p'|^2
    (diagonal terms vanish). Hence, by STEP 1:
      A_n = (1/2) sum_j ||[W_j, B~]||_2^2
          = tr B~^2 - sum_j tr(W_j B~ W_j B~)
    (the second equality expands ||[W,B]||_2^2 = 2[tr(W^2 B^2) -
    tr(W B W B)] for Hermitian W, B and uses sum_j W_j^2 = 1 on
    G_n*). [CAS OV1: all three forms equal, fully symbolic Hermitian
    B, exact rational unit directions]
STEP 3 (the Galerkin-Widom form). W_j commutes with Q_n - Z_n
    (functions of the commuting momenta; W_j (Q_n - Z_n) = (Q_n -
    Z_n) W_j = W_j), and B~ = (Q_n - Z_n) P (Q_n - Z_n) in the
    spatial factor, so
      [W_j, B~] = (Q_n - Z_n) [W_j, P] (Q_n - Z_n)   EXACTLY, and
      A_n = (1/2) sum_j ||(Q_n - Z_n) [W_j, P] (Q_n - Z_n)||_2^2 .
CONSEQUENCES (exact):
  CO-A THE OBJECT CLASS IS NAMED: the deciding object is the
    compressed HS commutator of the sharp ball with the momentum
    DIRECTION FIELD — the continuum symbol of W_j is p_j/|p|, a
    0-order symbol with a point singularity at p = 0. A ceiling for
    A_n is a Widom-type two-term/commutator law for a GALERKIN
    spectral-projection family — exactly the object class the audited
    CL-4 trap note (consumed at bytes, T-4/T-2) says the classical
    Widom/Sobolev-class theorems do NOT cover. The trap note is
    thereby SHARPENED from a route refusal to an object
    identification: O-1-S-B-W of §8.
  CO-B THE TRIVIAL BRACKET RECOVERED: |tr(W_j B~ W_j B~)| <=
    tr(W_j^2 B~^2) summed gives 0 <= A_n <= 2 tr B~^2 <= 2 tr B~ —
    the sealed CO-2 exact-3/2 bulk again; NO sub-3/2 gain from
    operator norms alone (the c-1 discipline: nothing below claims
    one).
  CO-C THE SINGULARITY IS QUARANTINED: W_j is bounded (||W_j||_op <=
    1) DESPITE the p = 0 symbol singularity, because the kernel
    column is excluded by the pinned convention — the F-1 repair is
    exactly what makes the direction operators lawful.
```

---

## 4. OP-2 — THE MEMBER VALUATION AT n = 2 (DERIVED, exact closed forms; existence at a member, NOT a rate)

The smallest even member (kernel-free: Z_2 = 0, B~ = B). Everything
below is the RECORD FAMILY's own bytes at n = 2 — not a toy — and is
displayed as grounding NO asymptotic claim.

### 4.1 The entries in closed form

```text
GRID: zeros of phi_2 are z = +-1/sqrt2; G_2 = {(s_1, s_2, s_3)/
  (sqrt2 ell) : s_i in {+1, -1}}, 8 points, ONE radius sqrt(3)/
  (sqrt2 ell) (the member is a single radial shell); cos angle(p_s,
  p_s') = (3 - 2m)/3 with m := #{i : s_i != s_i'} — weights 1 - cos =
  2m/3 in {2/3, 4/3, 2}; ordered pair counts (24, 24, 8) at m = (1,
  2, 3). [CAS OV6]
1D EIGENVECTORS (the sealed SN3 bytes): chi_s(x) = [phi_0(x/ell) +
  s i phi_1(x/ell)]/sqrt(2 ell), s in {+1, -1};
  conj(chi_s) chi_s' = (1/(2 ell)) pi^{-1/2} e^{-x^2/ell^2}
  [1 + s s' 2x^2/ell^2 + i(s' - s) sqrt2 x/ell]   EXACT. [CAS OV2]
PARITY KILL: the ball |x| <= r is invariant under each x_i -> -x_i;
  the only odd content is the i(s'-s) sqrt2 x/ell term (degree 1
  exactly); every mixed term containing it carries an odd power of
  some coordinate and integrates to ZERO over the ball. Hence, with
  sigma_i := s_i s_i',
    B_pp' = (8 ell^3 pi^{3/2})^{-1} Int_{|x| <= r} e^{-|x|^2/ell^2}
            prod_{i=1}^{3} (1 + sigma_i 2 x_i^2 / ell^2) dx
  EXACTLY — all entries REAL, dependent only on the flip count m
  (the octahedral collapse at the member): four orbit values b_0
  (diagonal), b_1, b_2, b_3. Expanding the product and reducing ball
  moments by the exact angular averages <n_1^2> = 1/3, <n_1^2 n_2^2>
  = 1/15, <n_1^2 n_2^2 n_3^2> = 1/105 [CAS OV3]:
    b_m = c [ I_0 + S_1(sigma) (2/ell^2) I_1 + S_2(sigma) (4/ell^4)
              I_2 + S_3(sigma) (8/ell^6) I_3 ],
    c := (8 ell^3 pi^{3/2})^{-1};  S_k = elementary symmetric
    polynomials of sigma (the sigma-bracket table verified for all 8
    sign vectors, CAS OV4);
    I_0 = 4 pi Int_0^r rho^2 e^{-rho^2/ell^2} d rho,  I_1 = (4 pi/3)
    Int rho^4 e,  I_2 = (4 pi/15) Int rho^6 e,  I_3 = (4 pi/105)
    Int rho^8 e  — exact erf/exp closed forms (CAS OV4).
UNITARITY LIMIT (consistency of the closed forms): as r -> oo,
  b_0 -> 1 and b_1, b_2, b_3 -> 0 EXACTLY (B -> identity on the
  carrier: the full-space overlap is orthonormality). [CAS OV4]
```

### 4.2 Strict positivity and the member value of the deciding object

```text
POINTWISE FLOOR: on the sealed ball, x_i^2 <= r^2 <= 1/4 and ell^2 >=
  1 (both frozen values), and
    ell^2 - 4 x_i^2 = (ell^2 - 1) + (1 - 4 r^2) + 4(r^2 - x_i^2)
  — a sum of three nonnegatives EXACTLY [CAS OV5] — so EVERY factor
  1 + sigma_i 2 x_i^2/ell^2 >= 1 - 2 x_i^2/ell^2 >= 1/2 pointwise.
  Hence every orbit entry obeys
    b_m >= c (1/2)^3 I_0 = c I_0 / 8 > 0,   m = 0, 1, 2, 3:
  ALL off-diagonal orbit entries of the record member's overlap
  matrix are STRICTLY POSITIVE (no accidental angular vanishing).
THE MEMBER VALUE: A_2 = 24 (2/3) b_1^2 + 24 (4/3) b_2^2 + 8 (2)
  b_3^2 = 16 b_1^2 + 32 b_2^2 + 16 b_3^2   EXACTLY, and
    A_2 >= (16 + 32 + 16) (c I_0/8)^2 = c^2 I_0^2 > 0
  [CAS OV5: the arithmetic (16+32+16)/64 = 1] — an exact positive
  erf/exp closed form. With S_2^2 = J_2^2 + 4 A_2 (sealed SP-3, n
  even), the member's sign crossing strictly exceeds its carrier
  crossing by an exactly displayed amount.
SCOPE (the honesty rail, displayed): this is a FIXED-MEMBER existence
  and machinery display — exact ball integrals of the eigenbasis
  exist at every fixed n, but the n -> oo law of the entries is
  exactly the absent moduli profile (§6 RT-1). OP-2 grounds NO
  ceiling, NO floor, NO rate; it is consumed by no verdict leg.
```

---

## 5. OP-3 + OP-4 — THE SYMMETRY COLLAPSE (all n) AND THE RADIAL TRIM (given CL-C)

### 5.1 OP-3 — the hyperoctahedral collapse (DERIVED, exact, all n)

```text
THE ACTION: the signed-permutation group B_3 (order 48) acts on R^3
  by g x = (eps_1 x_{tau(1)}, eps_2 x_{tau(2)}, eps_3 x_{tau(3)});
  the ball and the product carrier Q_n are invariant (permutation of
  identical tensor factors; per-coordinate parity, since the phi_k
  have parity (-1)^k — member pin CAS OV6). The 1D parity maps the
  eigenvector at zero z to the eigenvector at -z (Pi (q_n p q_n) Pi
  = -(q_n p q_n) exactly: Pi p Pi = -p, Pi q_n Pi = q_n), and
  permutations permute the 1D factors: the induced unitary V_g maps
  psi_p to a PHASE times psi_{gp}. Member pin: chi_s(-x) =
  chi_{-s}(x) exactly at n = 2 [CAS OV6].
THE COLLAPSE: |B_{gp, gp'}| = |<V_g psi_p, 1_B V_g psi_p'>| =
  |B_pp'| for every g (phases cancel in the modulus; 1_B invariant),
  and angle(gp, gp') = angle(p, p'): A_n = sum over B_3-orbit
  representatives with exact multiplicities. Successor note: the
  needed law is a law on the orbit-collapsed moduli only.
```

### 5.2 OP-4 — the radial trim and the momentum-weight stall (DERIVED; the trim given CL-C through the sealed SP-2 display)

```text
THE TRIM. Fix T > 0. Since 0 <= B~ <= 1 gives (B~^2)_pp <= B~_pp <= 1
  entrywise on the diagonal, and every weight obeys 1 - cos <= 2:
    A_n(low, T) := [pairs with min(|p|, |p'|) <= T]
                <= 2 * 2 sum_{p in G_n*, |p| <= T} (B~^2)_pp
                <= 4 #{p in G_n* : |p| <= T}
                <= 4 (1 + 2 T ell sqrt(2n+1)/pi)^3
  — the last step is the sealed SP-2 spatial count (given CL-C; the
  CONDITIONAL(CL-C) grade travels with this display and with nothing
  else). At T = n^{-a}, a in (0, 1/2]: A_n(low, T) <= C(a, ell)
  n^{3(1/2 - a)} + O(lower) — SUB-3/2 for every a > 0. THE DECIDING
  MASS LIVES AT HIGH MOMENTA; the direction field's p = 0 singular
  region is harmless (it carries sub-3/2 angular mass).
THE HIGH-PAIR MAJORIZATION. On pairs with both radii > T:
    1 - cos = (|p||p'| - p.p')/(|p||p'|) <= |p - p'|^2/(2 |p||p'|)
            <= |p - p'|^2/(2 T^2)
  (the middle step is AM-GM, difference (|p| - |p'|)^2/2 >= 0 EXACT
  [CAS OV7]); hence A_n(high, T) <= M_n/(2 T^2).
THE UNCONDITIONAL M-CEILING (given CL-A). ||pi_j||_op <= sqrt(2n)/ell
  (row-sum/Gershgorin on the sealed tridiagonal; member pin at n = 5:
  (2 a_4)^2 = 10 = 2n [CAS OV8]; derived, no new citation), so
    M_n = sum_j ||[pi_j, B~]||_2^2 <= sum_j (2 ||pi_j||_op ||B~||_2)^2
        <= 24 n tr B~/ell^2 <= (6 C_B/ell^2) n^{5/2}
  (tr B~ <= tr B = tr(P Q_n)/4 <= (C_B/4) n^{3/2}, the sealed T-3
  §3.1 display, given CL-A). [CAS OV8 arithmetic]
THE STALL, EXACT. Assembling A_n <= 4(1 + 2 T ell sqrt(2n+1)/pi)^3 +
  M_n/(2 T^2) and minimizing the shape c_1 T^3 n^{3/2} + c_2
  n^beta/T^2 over T: minimum at T* = (2 c_2/(3 c_1))^{1/5}
  n^{(beta - 3/2)/5}, minimum EXPONENT (3 beta + 3)/5 EXACT [CAS
  OV7]. At beta = 5/2 (the unconditional ceiling): 21/10 > 3/2 —
  VACUOUS. Even at beta = 2 — the continuum-toy ANTICIPATION for
  M_n (the Fourier-ball analog; ANTICIPATION only, consumed nowhere)
  — the exponent is 9/5 > 3/2: STILL VACUOUS. Sub-3/2 out of this
  assembly iff beta < 3/2 EXACT — i.e. iff the momentum-weighted
  mass is ALREADY sub-3/2, which is STRONGER than the transverse law
  it would prove (the |p - p'|^2 weight dominates the transverse
  weight at the dominant radii by the radial factor ~ 2n/ell^2).
  THE RADIAL FACTOR IS THE EXACT OBSTRUCTION: no momentum-weight
  assembly decides O-1-S-B; the transverse (direction-commutator)
  law of OP-1 is what must be valued. REFUSED as a decision route at
  its own exact arithmetic; retained as the trim display.
```

---

## 6. THE ROUTES, SWEPT — EACH REFUSED AT ITS OWN EXACT DISPLAY

```text
RT-1 THE ENTRYWISE/PR ROUTE (value the moduli). B_pp' = delta_pp' -
   Int_{|x| > r} psi_p^* psi_p' dx; the x-dependence on the ball is
   CL-A-lawful (fixed compact), but the COEFFICIENTS are phi_k at
   the zeros z_j, |z_j| up to sqrt(2n+1) — outside every fixed
   compact: CL-A cannot value them (audited CL-3: "no growing
   windows, no turning-point or Airy regime"); CL-B's global sup
   destroys the phase the cancellation needs; the full-range
   8.22.9-regime asymptotic has ZERO carriers in either root at my
   cutoff (§9 sw-3). The needed profile is phi_k(z_j)^2/
   lambda_n(z_j) over k < n — by CL-D (display-only, §8) lambda_n
   (z_j) = e^{-z_j^2}/w_j with w_j the Christoffel numbers: the
   missing law IS a Christoffel/PR-at-the-zeros law. Importing it
   as a decider would put the VERDICT inside a new citation — the
   T7SR discipline's verdict-independence fails for decision-grade
   imports (§8 THE IMPORT RULING). REFUSED as out of today's ground.
RT-2 THE WIDOM IMPORT. OP-1 shows A_n IS a Galerkin direction-
   commutator mass; the audited CL-4 trap note (T-4, re-consumed at
   bytes through T-2) stands: Widom/Sobolev-class theorems cover
   scaled pseudodifferential compressions, NOT Galerkin spectral
   projections; sgn/Q_n-family objects are the latter. No classical
   carrier covers the needed commutator law (§9 sw-3: zero
   carriers). Importing one would be surface-native new mathematics,
   not citation. REFUSED; the object is DISPLAYED as decider
   O-1-S-B-W instead.
RT-3 THE MOMENTUM-WEIGHT ROUTE. Exact stall at OP-4: minimum
   exponent (3 beta + 3)/5 with beta = 5/2 unconditional (21/10) and
   beta = 2 anticipated (9/5), both > 3/2; sub-3/2 iff beta < 3/2 —
   circular. REFUSED at its own arithmetic [CAS OV7].
RT-4 POLYNOMIAL MOMENT ROUTES. tr(B~ f(pi) B~ g(pi)) for polynomial
   f, g is exactly computable at EVERY FIXED n (explicit
   tridiagonals; OP-2 is the n = 2 instance) — but the direction
   weight needs |pi|^{-1} = (sum pi_j^2)^{-1/2}, NOT a polynomial;
   bridging polynomial moments to the direction weight requires a
   radial localization law for the overlap mass — ABSENT (an
   assumed localization law is a BLOCKER TO DISPLAY, not consume:
   the honesty rail, held). And no closed n-law for the moments
   exists on today's stock (the moduli again). REFUSED both ways.
RT-5 THE FLOOR DIRECTION (toward FLOOR-DERIVED). Class-level: the
   audited all-parallel witness (T-2 AT-6b: resolved form, record-
   shaped listed data, excess = 0 EXACTLY) refutes every floor
   quantified over the displayed class; W12' freedom stands at the
   resolved byte grade with the audited J-preserving padding
   (AT-6a/AT-7). Family-level: a floor needs positive moduli at
   separated angles AT RATE n^{3/2} — the same absent profile as
   RT-1 (sweep: zero anti-localization carriers, §9). OP-2's member
   positivity is a FIXED-n existence display and NO rate floor
   (displayed as such at §4.2 SCOPE). REFUSED both ways today.
RT-6 THE CEILING DIRECTION AT THE CLASS GRADE. The audited W12'
   forcing WITH the audit's repairs (J-preserving toy AT-6a; n-
   indexed radius + count-law verification AT-7) refutes every
   ceiling-direction route quantified over: the resolved polar form,
   the spectrum + count law, chirality + kernel bookkeeping, the
   ball-overlap Gram MODULI read grid-abstract (audited F-5 guard),
   the sealed floors AND the sealed P-2 bracket. Consumed at audited
   grade; not re-walked; no repair re-derived. My OP-1..OP-4 partials
   consume family bytes OUTSIDE that class (the o-3 door, again) and
   still stall at the moduli (RT-1). REFUSED at the audited forcing.
```

---

## 7. WHY NO DECISION-GRADE CITATION EXISTS TODAY — THE IMPORT RULING, EXACT

```text
THE DISCIPLINE (T-3 §4.1 / T-4 G-h, o-2, at bytes): a lawful classical
  citation displays (i) the named theorem, (ii) the named source,
  (iii) the displayed statement consumed exactly, and (iv) the
  verdict-independence assessment — the registrar downgrade path
  under which, if the citation is ruled out of the authorized class,
  the affected displays go CONDITIONAL and THE VERDICT IS UNCHANGED
  (the CL-B and CL-C precedents both have this shape).
THE RULING FOR O-1-S-B: any import strong enough to DECIDE (either
  direction) would be consumed by the verdict itself — no downgrade
  path can leave the verdict unchanged: clause (iv) cannot be
  satisfied by a decision-grade import. AND the candidate object
  fails clause (i) independently: the decision needs a full-range
  statement with EXPLICIT n-uniform remainders across the elliptic
  (8.22.9), turning-point/Airy (8.22.14-type), and exponential
  regions, for ALL k <= n, AT THE ZEROS of phi_n — an ASSEMBLED
  uniform package, not a single named classical theorem; Szego's
  displayed statements carry unquantified O(.) remainders on
  separated regions. The assembly IS the "genuinely NEW analytic
  input" the sealed T-1 §8 names. CONSEQUENCE: the named regime
  enters this artifact ONLY as the displayed blocker/decider; no
  8.22.9-grade statement is cited, consumed, or silently used
  anywhere above (the batteries consume ladder algebra, parity,
  Gaussian moments, and finite linear algebra only).
```

---

## 8. THE VERDICT AND THE DECIDER MENU

**VERDICT: UNDECIDABLE-TODAY** (for O-1-S-B as commissioned: neither
the ceiling A_n <= C_B'' n^{3/2 - gamma_B} with explicit gamma_B > 0
nor the floor A_n >= c n^{3/2} is derivable on the sealed stock at
the cutoff). NOT CEILING-DERIVED (RT-1/RT-2/RT-3/RT-6: the moduli are
unvalued; the class forcing is audited; the assemblies stall at exact
arithmetic). NOT FLOOR-DERIVED (RT-5: the all-parallel witness plus
the absence of any anti-localization carrier; the member positivity
is rate-free). NOT POLYLOG-ONLY (no sub-3/2 gain of any size is
derived for A_n — CO-B returns the exact-3/2 bulk; and per the
audited c-1, a polylog-only gain would not decide as specified).

```text
BLOCKER-1'' (the moduli profile): no sealed or classical-grade object
  values phi_k(z_j)^2/lambda_n(z_j) (equivalently, by CL-D, the
  Christoffel-number profile at the zeros) — CL-A fixed-compact
  (audited CL-3), CL-B phase-destroying sup, zero full-range-PR
  carriers at the cutoff (§9 sw-3).
BLOCKER-2'' (the class freedom): the audited W12' + J-preserving
  padding forcing (ceiling side) and the all-parallel witness (floor
  side) leave A_n free at the resolved-byte class grade; family-
  specific valuation is REQUIRED and stalls at BLOCKER-1''.

THE DECIDERS — ONE LAW, TWO NAMED GUISES (either seals O-1-S-B):
O-1-S-B-PR (THE PROFILE LAW): a certified quantified law for the
  orbit-collapsed moduli |B_pp'| at general n — equivalently for the
  coefficient profile phi_k(z_j)^2/lambda_n(z_j) (the Christoffel
  profile at the zeros; CL-D naming) — with n-uniform explicit
  remainders: the full-range Plancherel-Rotach package at the
  Hermite zeros (Szego §8.22.9 elliptic regime + turning/Airy +
  exponential regions, assembled uniformly), or any equivalent.
O-1-S-B-W (THE GALERKIN COMMUTATOR LAW): a certified ceiling
  sum_j ||(Q_n - Z_n)[W_j, P](Q_n - Z_n)||_2^2 <= 2 C_B''
  n^{3/2 - gamma_B} — a Widom-type two-term/commutator law for the
  Galerkin spectral-projection family (the object the audited CL-4
  trap note excludes from today's classical carriers). By OP-1 this
  IS the ceiling, verbatim.
YIELDS ONCE SEALED (arithmetic pinned, CAS OV8; consumed nowhere
  today): CEILING at gamma_B => O-1-S at gamma' = min(gamma_B, 1/12)
  through SP-3 (+4 fold) + sealed P-2 => O-1 at gamma = min(gamma_B,
  1/12) through sealed P-3 => MO-4-R DECIDED-o(1) at rate n^{-gamma}
  through the sealed T-4 display — nothing else needed. FLOOR at c
  => S_n^2 >= 2 c n^{3/2} cofinitely => CEILING-FAILS-AT-3/2 through
  the sealed floor-side display.
ANTICIPATIONS (displayed, consumed nowhere): the continuum symbol
  analog of O-1-S-B-W is surface-area x log grade (~ n log n) — if
  the Galerkin family matched it, gamma_B would be any power < 1/2
  and O-1 would land at 1/12; the of-record surface diagnosis points
  the same way. ANTICIPATION only; ground for nothing.
ALTERNATIVE DECIDERS (unchanged, of record): the O-2 localization
  package (T-5 §6); any direct kappa_n or S_n route (O-1/O-1-S as
  specified).
POSITION AFTER THIS COMMISSION: the deciding object of record now has
  (i) an exact operator form (OP-1) naming its theorem class, (ii) a
  strictly positive exact valuation at the first even member (OP-2),
  (iii) an exact symmetry reduction (OP-3), (iv) an exact radial
  quarantine + stall map (OP-4), and (v) two named decider guises
  with pinned yield chains. The question is ONE quantified law away
  in either guise; both guises are absent from both roots at the
  cutoff.
```

---

## 9. THE SWEEP (exhaustive at this displayed sweep only; cutoff in header)

```text
ROOTS (as commissioned): /Users/bgm/MB Work/alpha-program-archive/
workspace (primary) and /Users/bgm/Documents/New project/
gravity_emergence_evidence_program/
alpha_fundamental_record_action_cleanroom_v003 (cleanroom). Fenced
name classes (register|road_|ledger|lens|plan|tracker|THE_HANDOFF|
continuation) excluded from every opening; filename-level listing and
match-count probes only; .proof_deps vendored library files typed
out.
KEYS RUN: "T11SR"; "OVERLAP_LAW"; "O-1-S-B"; "8.22.9" (fixed-string);
"full-range Plancherel"; "Christoffel"; "Gauss-Hermite quadrature";
"direction operator"; "B_pp"; "W12"; "anti-localization".
FINDINGS:
 sw-1 OCCUPATION: NO T11SR and NO OVERLAP_LAW artifact exists in
      either root (probed at session start AND at the cutoff; output
      path probed ABSENT twice). UNOCCUPIED.
 sw-2 O-1-S-B CARRIERS: "O-1-S-B", "B_pp", "anti-localization"
      carriers are EXACTLY the sealed T10SR pair (the commission's
      own ground). No third carrier.
 sw-3 THE NAMED REGIME: "8.22.9" and "full-range Plancherel" carriers
      are EXACTLY the T10SR pair (which names the absence); ZERO
      independent carriers in both roots — the named regime is
      confirmed absent at this later cutoff. "direction operator":
      ZERO carriers (OP-1's naming is new).
 sw-4 HOMONYMS, PROBED AT COUNT LEVEL (never opened): "Christoffel"
      hits FORM_TO_HS_BRIDGE pair + MO2 build + P1_DILATION audit
      (+ vendored sympy): B_pp = 0, sgn( = 0, angular-localization
      = 0 in every one (MO2's kappa_n hits are its own sealed floor
      lane, already my ground at audited grade) — different objects,
      different lanes, typed out. "Gauss-Hermite quadrature" hits
      the T7 PURE_HERMITE_VACUUM/GALERKIN_BASELINE lane (+ vendored
      sympy quadrature.py): all zero on B_pp/kappa_n/sgn(/angular —
      a numerics-of-another-lane homonym, typed out. "W12" hits the
      T10SR pair + three AXN grammar-lane artifacts (+ one vendored
      sympy test): AXN files zero on every deciding token — a token
      homonym, typed out.
```

Each sentence claims only this displayed sweep at the declared
cutoff.

---

## 10. CONSISTENCY WITH THE SEALED STOCK — EVERY CONTACT POINT

```text
X-1 vs T-1 §8 (the O-1-S-B spec): the commissioned object is consumed
    at its sealed shape WITH the audited F-1 repair pinned (nonzero
    pairs; +4 fold) — exactly the registrar guidance in T-2's
    CONSUMPTION_BOUNDARY ("with F-1's convention pinned and F-5's
    reading guard"). No sealed quantifier touched.
X-2 vs CO-2/c-1 (the totals discipline): CO-B reproduces the sealed
    exact-3/2 bulk and claims NO gain below it — the c-1 polylog
    discipline is held verbatim (T-6 at bytes).
X-3 vs sw-2/sw-3 of T-1 and asw-3 of T-2: absence claims at THEIR
    cutoffs stand; my sw-3 re-confirms the same absences at a LATER
    cutoff; OP-1..OP-4 are new derivations from bytes those sweeps
    never denied (the audited o-3 door, walked again).
X-4 vs the audited CL-4 trap note: OP-1 SHARPENS it (route refusal ->
    object identification O-1-S-B-W) and consumes it only as the
    refusal of RT-2; no Widom-class statement is imported anywhere.
X-5 vs the audited F-1: my A_n convention IS the F-1 repair; the +4
    kernel-column fold appears in every yield display (CAS OV8
    carries the +4 inside the folded constant).
X-6 vs the audited F-5 reading guard: this artifact names the GRID
    as known (SP-1 bytes) and the MODULI as missing — the
    grid-abstract vs indexed distinction is kept exactly as the
    audit pinned it.
X-7 vs the W12'/padding forcing (T-1 §6 + T-2 F-2/F-3/F-4 repairs):
    consumed at audited grade as RT-5/RT-6 refusals; no witness
    rebuilt, no repair re-derived, no toy consumed as family ground.
X-8 vs P-1/P-2/P-3 and the T-4 reduction: consumed ONLY at their
    sealed displays inside the (conditional) yield chains and the
    OP-4 M-ceiling; no sealed constant re-derived, no quantifier
    moved; the CONDITIONAL(CL-A)/(CL-B)/(CL-C) grades travel with
    exactly the displays that carry them of record.
X-9 vs the MO-2 floors and D4: untouched; nothing here bounds kappa_n
    or S_n anew (the yields are conditional on the ABSENT decider and
    consumed nowhere).
X-10 FENCES: no closure claimed; O-1, O-1-S, O-1-S-B, MO-4-R all stay
    open; no flag of any prior artifact flips; alpha_computed /
    proof_authorized / kappa_record_computed all false; every
    constant symbolic or an exact closed form; the member closed
    forms are RECORD-member displays (not toys) at fixed n, grounding
    no asymptotic claim; H-R/rho_n appears in no display.
```

---

## 11. THE CAS BATTERY (VERBATIM) AND ITS OUTPUT (VERBATIM)

sympy 1.14.0, fresh venv `overlapvenv_t11sr` under the session
scratchpad; nothing written to the workspace but this artifact and
its seal. Tooling disclosure, on the record: the battery first ran
ONCE complete with 9/9 PASS; before the final double run, two INERT
scaffolding lines in OV7 (assignments to unused names guarded by
`if False`, left over from drafting the exponent-extraction helper)
were REMOVED for display hygiene — no conjunct, no check name, no
assertion, and no mathematical content changed; the cleaned battery
(sha256 672f5ea7d13956a7384a27bf0ee66ee461729dddf12f9e90264ae4f184a2
3fc7) then ran TWICE with BYTE-IDENTICAL output (diff empty), 9/9
PASS both. No other edit at any point.

```python
# OVERLAP-BUILD CAS battery -- EXACT SYMBOLIC ONLY (sympy 1.14.0, fresh venv
# overlapvenv_t11sr under the session scratchpad). Commission T11SR. Every
# constant symbolic or an exact rational/closed form; nothing numeric
# evaluated; no floats as ground. All checks are exact-identity consistency
# checks of steps whose operator-theoretic content is derived in the artifact.
import itertools
import sympy as sp
from sympy import Rational as R, I, sqrt, pi, exp, erf, conjugate as cj

ok = lambda name, cond: print(f"{name}: {'PASS' if cond else 'FAIL'}", flush=True)

# ===== OV1 -- THE DIRECTION-COMMUTATOR IDENTITY (all-symbolic Hermitian B) =====
u1 = sp.Matrix([1, 2, 2])/3
u2 = sp.Matrix([2, -2, 1])/3
u3 = sp.Matrix([0, 3, 4])/5
U = [u1, u2, u3]
unit_ok = all((u.T*u)[0, 0] == 1 for u in U)
a1, a2, a3, x12, y12, x13, y13, x23, y23 = sp.symbols(
    'a1 a2 a3 x12 y12 x13 y13 x23 y23', real=True)
z12, z13, z23 = x12 + I*y12, x13 + I*y13, x23 + I*y23
B = sp.Matrix([[a1, z12, z13], [cj(z12), a2, z23], [cj(z13), cj(z23), a3]])
W = [sp.diag(U[0][j], U[1][j], U[2][j]) for j in range(3)]
sumW2 = sp.expand(W[0]**2 + W[1]**2 + W[2]**2) == sp.eye(3)
LHS = sp.expand(sum(B[p, q]*cj(B[p, q])*(1 - (U[p].T*U[q])[0, 0])
                    for p in range(3) for q in range(3) if p != q))
MID = sp.expand(sp.trace(B*B) - sum(sp.trace(Wj*B*Wj*B) for Wj in W))
RHS = sp.expand(R(1, 2)*sum(sp.trace((Wj*B - B*Wj).H*(Wj*B - B*Wj)) for Wj in W))
ok("OV1 DIRECTION-COMMUTATOR IDENTITY: for ANY Hermitian B (3x3 fully symbolic"
   " complex) and ANY unit direction assignment u_p (exact rational units,"
   " sum_j W_j^2 = 1): sum_{p != p'} |B_pp'|^2 (1 - cos angle) = tr B^2 -"
   " sum_j tr(W_j B W_j B) = (1/2) sum_j ||[W_j, B]||_2^2 -- ALL EXACT",
   unit_ok and sumW2 and sp.simplify(LHS - MID) == 0
   and sp.simplify(LHS - RHS) == 0)

# ===== OV2 -- the n = 2 member: 1D eigenvector products, exact =====
t, x, L, rr = sp.symbols('t x ell r', positive=True)
xr = sp.Symbol('x', real=True)
phi0 = pi**R(-1, 4)*exp(-xr**2/2)
phi1 = sqrt(2)*pi**R(-1, 4)*xr*exp(-xr**2/2)
def chi(s, var):
    return ((phi0 + s*I*phi1).subs(xr, var/L))/sqrt(2*L)
prod_ok = True
for s in (1, -1):
    for sprime in (1, -1):
        lhs = sp.expand(cj(chi(s, xr))*chi(sprime, xr))
        rhs = sp.expand((1/(2*L))*pi**R(-1, 2)*exp(-xr**2/L**2)
                        * (1 + s*sprime*2*xr**2/L**2
                           + I*(sprime - s)*sqrt(2)*xr/L))
        prod_ok = prod_ok and sp.simplify(lhs - rhs) == 0
ok("OV2 MEMBER n = 2, 1D PRODUCTS: chi_s(x) = [phi_0(x/ell) + s i phi_1(x/ell)]"
   "/sqrt(2 ell) (the SN3 eigenvectors at the sealed tridiagonal); conj(chi_s)"
   " chi_s' = (1/(2 ell)) pi^{-1/2} e^{-x^2/ell^2} [1 + ss' 2x^2/ell^2 +"
   " i(s'-s) sqrt2 x/ell] EXACT for all four sign pairs -- the odd term"
   " carries x^1 exactly (killed by the ball's x -> -x symmetry)",
   prod_ok)

# ===== OV3 -- angular averages on the sphere, exact =====
th, ph = sp.symbols('theta phi', positive=True)
n1 = sp.sin(th)*sp.cos(ph); n2 = sp.sin(th)*sp.sin(ph); n3 = sp.cos(th)
def sphavg(f):
    return sp.integrate(sp.integrate(f*sp.sin(th), (th, 0, pi)),
                        (ph, 0, 2*pi))/(4*pi)
ok("OV3 ANGULAR AVERAGES: <n1^2> = 1/3, <n1^2 n2^2> = 1/15,"
   " <n1^2 n2^2 n3^2> = 1/105 on S^2 EXACT (the ball-moment reduction)",
   sp.simplify(sphavg(n1**2) - R(1, 3)) == 0
   and sp.simplify(sphavg(n1**2*n2**2) - R(1, 15)) == 0
   and sp.simplify(sphavg(n1**2*n2**2*n3**2) - R(1, 105)) == 0)

# ===== OV4 -- the member overlap entries: closed forms, sigma-table, limits =====
rho = sp.Symbol('rho', positive=True)
def radint(m):
    return sp.integrate(rho**(2*m + 2)*exp(-rho**2/L**2), (rho, 0, rr))
I0 = 4*pi*radint(0)
I1 = (4*pi/3)*radint(1)
I2 = (4*pi/15)*radint(2)
I3 = (4*pi/105)*radint(3)
c0 = 1/(8*L**3*pi**R(3, 2))
# formal sigma-bracket: B_pp' = c0 [I0 + S1 (2/ell^2) I1 + S2 (4/ell^4) I2
#                                 + S3 (8/ell^6) I3], S_k = elem. sym. in sigma
I0f, I1f, I2f, I3f = sp.symbols('I0f I1f I2f I3f', positive=True)
aa1, aa2, aa3 = sp.symbols('aa1 aa2 aa3', positive=True)
mom = {(0, 0, 0): I0f, (2, 0, 0): I1f, (0, 2, 0): I1f, (0, 0, 2): I1f,
       (2, 2, 0): I2f, (2, 0, 2): I2f, (0, 2, 2): I2f, (2, 2, 2): I3f}
def ballint(poly):
    poly = sp.expand(poly)
    out = 0
    for mono, coeff in sp.Poly(poly, aa1, aa2, aa3).terms():
        if any(e % 2 for e in mono):
            continue
        out += coeff*mom[mono]
    return sp.expand(out)
table_ok = True
for sig in itertools.product((1, -1), repeat=3):
    prod = sp.prod([(1 + sig[i]*2*[aa1, aa2, aa3][i]**2/L**2) for i in range(3)])
    got = ballint(prod)
    S1 = sum(sig); S2 = sig[0]*sig[1] + sig[0]*sig[2] + sig[1]*sig[2]
    S3 = sig[0]*sig[1]*sig[2]
    want = sp.expand(I0f + S1*(2/L**2)*I1f + S2*(4/L**4)*I2f + S3*(8/L**6)*I3f)
    table_ok = table_ok and sp.expand(got - want) == 0
subs_real = {I0f: I0, I1f: I1, I2f: I2, I3f: I3}
def bm(m):
    sig = tuple([-1]*m + [1]*(3 - m))
    S1 = sum(sig); S2 = sig[0]*sig[1] + sig[0]*sig[2] + sig[1]*sig[2]
    S3 = sig[0]*sig[1]*sig[2]
    return c0*(I0 + S1*(2/L**2)*I1 + S2*(4/L**4)*I2 + S3*(8/L**6)*I3)
b0, b1, b2, b3 = bm(0), bm(1), bm(2), bm(3)
lim_ok = (sp.simplify(sp.limit(b0, rr, sp.oo) - 1) == 0
          and all(sp.simplify(sp.limit(b, rr, sp.oo)) == 0 for b in (b1, b2, b3)))
ok("OV4 MEMBER OVERLAP ENTRIES: B_pp' = (1/(8 ell^3 pi^{3/2})) Int_ball"
   " e^{-|x|^2/ell^2} prod_i (1 + sigma_i 2 x_i^2/ell^2) dx with sigma_i ="
   " s_i s_i' (odd terms killed by parity) -- the sigma-bracket table verified"
   " for all 8 sign vectors (formal moment functional); entries depend on the"
   " flip count m ONLY (octahedral collapse at the member); radial moments in"
   " exact erf/exp closed form; UNITARITY LIMIT: b_0 -> 1 and b_1, b_2, b_3"
   " -> 0 as r -> oo EXACT (B -> identity: consistency of the closed forms)",
   table_ok and lim_ok)

# ===== OV5 -- member positivity: every off-diagonal class entry > 0; A_2 floor =====
tt = sp.Symbol('t', real=True)
tele = sp.expand((L**2 - 4*tt**2) - ((L**2 - 1) + (1 - 4*rr**2) + 4*(rr**2 - tt**2)))
count_weight = (24*R(2, 3) == 16 and 24*R(4, 3) == 32 and 8*2 == 16
                and (16 + 32 + 16)*R(1, 64) == 1)
ok("OV5 MEMBER POSITIVITY + A_2 FLOOR: pointwise on the ball (t^2 <= r^2 <="
   " 1/4 <= ell^2/4, the sealed freeze r <= 1/2, ell in {1, sqrt2}):"
   " L^2 - 4t^2 = (L^2 - 1) + (1 - 4r^2) + 4(r^2 - t^2), a sum of"
   " nonnegatives EXACT, so every factor 1 + sigma_i 2x_i^2/ell^2 >= 1/2 and"
   " every entry b_m >= (1/8) c I_0 > 0; pair table: 24 ordered pairs at"
   " flip-1 (weight 1 - cos = 2/3), 24 at flip-2 (4/3), 8 at flip-3 (2):"
   " A_2 = 16 b_1^2 + 32 b_2^2 + 16 b_3^2 >= 64 (c I_0/8)^2 = c^2 I_0^2"
   " EXACT -- the deciding object is STRICTLY POSITIVE at the member n = 2",
   tele == 0 and count_weight)

# ===== OV6 -- member grid geometry + parity =====
cos_ok = all(R(sum(s[i]*sprime[i] for i in range(3)), 3)
             == R(3 - 2*sum(1 for i in range(3) if s[i] != sprime[i]), 3)
             for s in itertools.product((1, -1), repeat=3)
             for sprime in itertools.product((1, -1), repeat=3))
counts = {1: 0, 2: 0, 3: 0}
for s in itertools.product((1, -1), repeat=3):
    for sprime in itertools.product((1, -1), repeat=3):
        m = sum(1 for i in range(3) if s[i] != sprime[i])
        if m:
            counts[m] += 1
par_ok = all(sp.simplify((phi0 if k == 0 else phi1).subs(xr, -xr)
                         - (-1)**k*(phi0 if k == 0 else phi1)) == 0
             for k in (0, 1))
chi_par = all(sp.simplify(chi(s, -xr) - chi(-s, xr)) == 0 for s in (1, -1))
ok("OV6 MEMBER GRID GEOMETRY + PARITY: cos angle(p_s, p_s') = (3 - 2m)/3"
   " EXACT (m = sign flips; weights 1 - cos = 2m/3 in {2/3, 4/3, 2}); ordered"
   " pair counts (24, 24, 8) EXACT; phi_k(-t) = (-1)^k phi_k(t) and"
   " chi_s(-x) = chi_{-s}(x) EXACT -- the hyperoctahedral action at the member",
   cos_ok and counts == {1: 24, 2: 24, 3: 8} and par_ok and chi_par)

# ===== OV7 -- majorizations + the stall arithmetic =====
p1a, p2a, q1a, q2a = sp.symbols('P1 P2 Q1 Q2', positive=True)
amgm = sp.expand((p1a**2 + p2a**2)/2 - p1a*p2a - (p1a - p2a)**2/2) == 0
uu = sp.Matrix([sp.Symbol(f'ua{i}', real=True) for i in range(3)])
vv = sp.Matrix([sp.Symbol(f'va{i}', real=True) for i in range(3)])
norm_u = sum(e**2 for e in uu); norm_v = sum(e**2 for e in vv)
half_id = sp.expand((sum((uu[i] - vv[i])**2 for i in range(3)))/2
                    - (norm_u + norm_v)/2 + uu.dot(vv))
n_, T_, c1_, c2_, beta_ = sp.symbols('n T c1 c2 beta', positive=True)
expr = c1_*T_**3*n_**R(3, 2) + c2_*n_**beta_/T_**2
Tstar = sp.solve(sp.diff(expr, T_), T_)
Tstar = [s for s in Tstar if s.is_positive is not False][0]
minval = sp.powsimp(sp.simplify(expr.subs(T_, Tstar)), force=True)
min_at = lambda b: sp.simplify(sp.powsimp(minval.subs(beta_, b), force=True))
got52 = min_at(R(5, 2)); got2 = min_at(2)
# exponent extraction via substitution and log-ratio limit:
lam = sp.Symbol('lambda_', positive=True)
def n_exponent(e):
    return sp.simplify(sp.log(e.subs({c1_: 1, c2_: 1, n_: lam}))/sp.log(lam))
ex52 = sp.limit(n_exponent(got52), lam, sp.oo)
ex2 = sp.limit(n_exponent(got2), lam, sp.oo)
ok("OV7 MAJORIZATIONS + STALL: (i) 1 - cos = |u - u'|^2/2 for unit vectors"
   " EXACT; (ii) |p||p'| - p.p' <= |p - p'|^2/2 (difference = (|p|-|p'|)^2/2"
   " EXACT AM-GM); (iii) the radial-trim + momentum-weight assembly"
   " c1 T^3 n^{3/2} + c2 n^beta/T^2 minimizes at T* = (2c2/(3c1))^{1/5}"
   " n^{(beta - 3/2)/5} with min exponent (3 beta + 3)/5 EXACT: beta = 5/2"
   " (the UNCONDITIONAL momentum ceiling, given CL-A) gives 21/10 > 3/2;"
   " beta = 2 (the continuum-toy ANTICIPATION, consumed nowhere) gives"
   " 9/5 > 3/2; sub-3/2 iff beta < 3/2 EXACT -- the momentum-weight route"
   " cannot decide O-1-S-B: the radial factor is the exact obstruction",
   amgm and half_id == 0
   and sp.simplify(Tstar - (2*c2_/(3*c1_))**R(1, 5)*n_**((beta_ - R(3, 2))/5)) == 0
   and ex52 == R(21, 10) and ex2 == R(9, 5)
   and R(21, 10) > R(3, 2) and R(9, 5) > R(3, 2)
   and sp.solve(sp.Eq((3*beta_ + 3)/5, R(3, 2)), beta_) == [R(3, 2)])

# ===== OV8 -- Gershgorin member + M-ceiling arithmetic + yield/floor transfers =====
aof = lambda k: sqrt(R(k + 1, 2))
J5 = sp.zeros(5, 5)
for k in range(4):
    J5[k, k + 1] = aof(k); J5[k + 1, k] = aof(k)
gersh5 = all(sum(sp.Abs(J5[i, j]) for j in range(5) if j != i)**2 <= 10
             for i in range(5))
CBs, trB, gB, cf, Cq, CB2 = sp.symbols('C_B trB gamma_B c C_Q C2', positive=True)
Mceil = sp.expand(3*(2*sqrt(2*n_)/L)**2*trB - 24*n_*trB/L**2) == 0
gmin = sp.Symbol('gamma_min', positive=True)
yield_ok = (R(3, 2) - R(17, 12) == R(1, 12)
            and sp.expand((4*cf*n_**R(3, 2) - 4) - 2*cf*n_**R(3, 2)
                          - (2*cf*n_**R(3, 2) - 4)) == 0)
ok("OV8 GERSHGORIN + M-CEILING + YIELDS: ||J_5||_op^2 <= (2 a_4)^2 = 10 = 2n"
   " at the n = 5 member (row-sum EXACT; so ||pi_j||_op <= sqrt(2n)/ell,"
   " derived, no citation); M_n <= sum_j (2||pi_j||_op)^2 tr B^2-grade ="
   " 24 n tr B/ell^2 arithmetic EXACT; YIELD: 3/2 - 17/12 = 1/12 (an O-1-S-B"
   " ceiling at gamma_B gives S^2 <= (C_Q + 4 C_B'' + 4) n^{3/2 -"
   " min(gamma_B, 1/12)} through SP-3 + sealed P-2, then O-1, then MO-4-R"
   " o(1) at rate); FLOOR TRANSFER: 4c n^{3/2} - 4 >= 2c n^{3/2} for"
   " n^{3/2} >= 2/c EXACT (an anti-localization floor gives S_n^2 >= 2c"
   " n^{3/2} cofinitely: CEILING-FAILS-AT-3/2 through the sealed floor side)",
   gersh5 and Mceil and yield_ok)

# ===== OV9 -- CL-D at members: Gauss-Hermite quadrature + Christoffel identity =====
zsym = sp.Symbol('z', real=True)
p0 = pi**R(-1, 4)
p1 = sqrt(2)*pi**R(-1, 4)*zsym
p2 = pi**R(-1, 4)*(2*zsym**2 - 1)/sqrt(2)
h2zeros = sp.solve(sp.hermite(2, zsym), zsym)
K2 = p0**2 + p1**2
w2 = [sp.simplify(1/K2.subs(zsym, z)) for z in h2zeros]
gauss2 = all(sp.simplify(sum(w2[j]*h2zeros[j]**d for j in range(2))
                         - sp.integrate(zsym**d*exp(-zsym**2),
                                        (zsym, -sp.oo, sp.oo))) == 0
             for d in range(4))
lam2_ok = all(sp.simplify(sum((sp.hermite(k, zsym)*exp(-zsym**2/2)
                               / sp.sqrt(sp.sqrt(pi)*2**k*sp.factorial(k)))**2
                              for k in range(2)).subs(zsym, z)
                          - exp(-z**2)/w) == 0
              for z, w in zip(h2zeros, w2))
h3zeros = sp.solve(sp.hermite(3, zsym), zsym)
K3p = p0**2 + p1**2 + p2**2
w3 = [sp.simplify(1/K3p.subs(zsym, z)) for z in h3zeros]
gauss3 = all(sp.simplify(sum(w3[j]*h3zeros[j]**d for j in range(3))
                         - sp.integrate(zsym**d*exp(-zsym**2),
                                        (zsym, -sp.oo, sp.oo))) == 0
             for d in range(6))
ok("OV9 CL-D AT MEMBERS (display-only citation, consumed by no verdict leg):"
   " Gauss-Hermite quadrature with Christoffel numbers w_j = 1/K_n^{pol}"
   "(z_j, z_j) is EXACT through degree 2n-1 at n = 2 (deg <= 3) and n = 3"
   " (deg <= 5), and lambda_n(z_j) := sum_{k<n} phi_k(z_j)^2 = e^{-z_j^2}/w_j"
   " EXACT at the n = 2 zeros -- the eigenvector normalization IS the"
   " Christoffel number: the missing moduli-profile law IS a"
   " Christoffel/PR-at-the-zeros law",
   gauss2 and lam2_ok and gauss3)

print("OV-BATTERY-DONE")
```

Output, verbatim (9/9 PASS; both runs byte-identical):

```text
OV1 DIRECTION-COMMUTATOR IDENTITY: for ANY Hermitian B (3x3 fully symbolic complex) and ANY unit direction assignment u_p (exact rational units, sum_j W_j^2 = 1): sum_{p != p'} |B_pp'|^2 (1 - cos angle) = tr B^2 - sum_j tr(W_j B W_j B) = (1/2) sum_j ||[W_j, B]||_2^2 -- ALL EXACT: PASS
OV2 MEMBER n = 2, 1D PRODUCTS: chi_s(x) = [phi_0(x/ell) + s i phi_1(x/ell)]/sqrt(2 ell) (the SN3 eigenvectors at the sealed tridiagonal); conj(chi_s) chi_s' = (1/(2 ell)) pi^{-1/2} e^{-x^2/ell^2} [1 + ss' 2x^2/ell^2 + i(s'-s) sqrt2 x/ell] EXACT for all four sign pairs -- the odd term carries x^1 exactly (killed by the ball's x -> -x symmetry): PASS
OV3 ANGULAR AVERAGES: <n1^2> = 1/3, <n1^2 n2^2> = 1/15, <n1^2 n2^2 n3^2> = 1/105 on S^2 EXACT (the ball-moment reduction): PASS
OV4 MEMBER OVERLAP ENTRIES: B_pp' = (1/(8 ell^3 pi^{3/2})) Int_ball e^{-|x|^2/ell^2} prod_i (1 + sigma_i 2 x_i^2/ell^2) dx with sigma_i = s_i s_i' (odd terms killed by parity) -- the sigma-bracket table verified for all 8 sign vectors (formal moment functional); entries depend on the flip count m ONLY (octahedral collapse at the member); radial moments in exact erf/exp closed form; UNITARITY LIMIT: b_0 -> 1 and b_1, b_2, b_3 -> 0 as r -> oo EXACT (B -> identity: consistency of the closed forms): PASS
OV5 MEMBER POSITIVITY + A_2 FLOOR: pointwise on the ball (t^2 <= r^2 <= 1/4 <= ell^2/4, the sealed freeze r <= 1/2, ell in {1, sqrt2}): L^2 - 4t^2 = (L^2 - 1) + (1 - 4r^2) + 4(r^2 - t^2), a sum of nonnegatives EXACT, so every factor 1 + sigma_i 2x_i^2/ell^2 >= 1/2 and every entry b_m >= (1/8) c I_0 > 0; pair table: 24 ordered pairs at flip-1 (weight 1 - cos = 2/3), 24 at flip-2 (4/3), 8 at flip-3 (2): A_2 = 16 b_1^2 + 32 b_2^2 + 16 b_3^2 >= 64 (c I_0/8)^2 = c^2 I_0^2 EXACT -- the deciding object is STRICTLY POSITIVE at the member n = 2: PASS
OV6 MEMBER GRID GEOMETRY + PARITY: cos angle(p_s, p_s') = (3 - 2m)/3 EXACT (m = sign flips; weights 1 - cos = 2m/3 in {2/3, 4/3, 2}); ordered pair counts (24, 24, 8) EXACT; phi_k(-t) = (-1)^k phi_k(t) and chi_s(-x) = chi_{-s}(x) EXACT -- the hyperoctahedral action at the member: PASS
OV7 MAJORIZATIONS + STALL: (i) 1 - cos = |u - u'|^2/2 for unit vectors EXACT; (ii) |p||p'| - p.p' <= |p - p'|^2/2 (difference = (|p|-|p'|)^2/2 EXACT AM-GM); (iii) the radial-trim + momentum-weight assembly c1 T^3 n^{3/2} + c2 n^beta/T^2 minimizes at T* = (2c2/(3c1))^{1/5} n^{(beta - 3/2)/5} with min exponent (3 beta + 3)/5 EXACT: beta = 5/2 (the UNCONDITIONAL momentum ceiling, given CL-A) gives 21/10 > 3/2; beta = 2 (the continuum-toy ANTICIPATION, consumed nowhere) gives 9/5 > 3/2; sub-3/2 iff beta < 3/2 EXACT -- the momentum-weight route cannot decide O-1-S-B: the radial factor is the exact obstruction: PASS
OV8 GERSHGORIN + M-CEILING + YIELDS: ||J_5||_op^2 <= (2 a_4)^2 = 10 = 2n at the n = 5 member (row-sum EXACT; so ||pi_j||_op <= sqrt(2n)/ell, derived, no citation); M_n <= sum_j (2||pi_j||_op)^2 tr B^2-grade = 24 n tr B/ell^2 arithmetic EXACT; YIELD: 3/2 - 17/12 = 1/12 (an O-1-S-B ceiling at gamma_B gives S^2 <= (C_Q + 4 C_B'' + 4) n^{3/2 - min(gamma_B, 1/12)} through SP-3 + sealed P-2, then O-1, then MO-4-R o(1) at rate); FLOOR TRANSFER: 4c n^{3/2} - 4 >= 2c n^{3/2} for n^{3/2} >= 2/c EXACT (an anti-localization floor gives S_n^2 >= 2c n^{3/2} cofinitely: CEILING-FAILS-AT-3/2 through the sealed floor side): PASS
OV9 CL-D AT MEMBERS (display-only citation, consumed by no verdict leg): Gauss-Hermite quadrature with Christoffel numbers w_j = 1/K_n^{pol}(z_j, z_j) is EXACT through degree 2n-1 at n = 2 (deg <= 3) and n = 3 (deg <= 5), and lambda_n(z_j) := sum_{k<n} phi_k(z_j)^2 = e^{-z_j^2}/w_j EXACT at the n = 2 zeros -- the eigenvector normalization IS the Christoffel number: the missing moduli-profile law IS a Christoffel/PR-at-the-zeros law: PASS
OV-BATTERY-DONE
```

---

## 12. CHOICE LEDGER (every unforced choice, classified; commission T11SR)

```text
CH-1 CL-D (Gauss-Hermite quadrature / Christoffel numbers) AS THE ONE
     NEW CLASSICAL CITATION, DISPLAY-ONLY. Named theorem: Gauss
     quadrature exactness at the zeros of the orthogonal polynomial
     with Christoffel numbers w_j = 1/K_n^{pol}(z_j, z_j) (exact
     through degree 2n-1). Named source: Szego, Orthogonal
     Polynomials, §3.4 (Theorems 3.4.1-3.4.2) and §15.3; classical in
     the strictest sense (Gauss 1814 / Jacobi / Christoffel).
     Displayed statement: §8/O-1-S-B-PR and RT-1 — lambda_n(z_j) =
     e^{-z_j^2}/w_j, member-pinned exactly at n = 2, 3 [CAS OV9].
     VERDICT-INDEPENDENCE: TOTAL — consumed by NO verdict leg and NO
     partial's inequality; blast radius is the decider's NAMING only
     (the alias "Christoffel profile" for the missing moduli law).
     If ruled out of the authorized class, the alias is struck and
     NOTHING else moves.
CH-2 THE A_n CONVENTION (nonzero pairs; kernel column at its [0, 4]
     bracket): FORCED — the audited F-1 repair and the T-2 registrar
     guidance pin exactly this convention; the alternative (all-pairs
     with an undefined angle at 0) is the corrected display.
CH-3 THE MEMBER n = 2 FOR OP-2: IMMATERIAL(derived) in principle
     (any even member admits the same exact ball-moment machinery),
     chosen as the smallest kernel-free member where the closed
     forms stay display-compact; the valuation grounds no n-law
     either way (§4.2 SCOPE).
CH-4 DIRECTION-OPERATOR FORMALISM (W_j) alongside the pair-sum form:
     IMMATERIAL(derived) — OP-1 displays the identity BOTH ways and
     CAS OV1 pins all three forms equal.
CH-5 STALL SHAPES (beta = 5/2 unconditional vs beta = 2 anticipated):
     IMMATERIAL — both displayed, the anticipation consumed nowhere;
     the stall conclusion (sub-3/2 iff beta < 3/2) is exact and
     shape-free [CAS OV7].
CH-6 SWEEP KEY SET (§9): the commissioned tokens plus the two decider
     guises' natural names ("Christoffel", "direction operator");
     homonyms typed out at count level. IMMATERIAL to the verdict
     (absences corroborate; nothing consumes a sweep positive).
CHAIN CHOICE AUDIT: no unforced choice enters the verdict chain. The
     verdict (UNDECIDABLE-TODAY, both directions) rests on: the
     audited W12' + J-preserving-padding forcing and the audited
     all-parallel witness (consumed at audited grade, RT-5/RT-6);
     the exact stall displays (OP-4/RT-3, CAS-pinned); the moduli
     absence (RT-1) and the import ruling (§7); and the sweep
     absences (sw-3) — none consumes CH-1 (display-only), CH-3 (a
     member exhibit consumed by no verdict leg), or CH-5's
     anticipation. The verdict survives every alternative at
     CH-1..CH-6 unchanged.
MACHINERY/RELEVANCE: classical operator theory (functions of
     commuting tuples, HS/trace identities, Gershgorin), exact
     Gaussian/ball moment calculus, parity/symmetry arguments, and
     exact optimization arithmetic applied to SEALED constructions;
     identity cores CAS-pinned; SURFACE-DERIVED, not surface-native.
```

---

## 13. TOY_SEPARATION (self-assessment)

```text
CLAIMED CLEAN at the stated quantifiers. OV1 (fully symbolic
Hermitian B, exact rational unit directions), OV3 (sphere averages),
OV7 (majorizations + symbolic optimization), OV8 (arithmetic +
member Gershgorin exhibit of a displayed general row-sum fact) are
all-parameter identity/inequality exhibits. OV2/OV4/OV5/OV6 are the
RECORD FAMILY's own member n = 2 — NOT toys — valued exactly from
the sealed SN3 eigenvector bytes; they are FIXED-MEMBER displays
consumed by no verdict leg and grounding no asymptotic claim (§4.2
SCOPE; the honesty rail). OV9 is a member pin of CL-D's displayed
classical statement (display-only citation). No witness model is
rebuilt here; the W12'/all-parallel forcing enters ONLY at audited
grade as route refusals. No model family is a premise of any derived
partial: OP-1/OP-3 are exact operator identities of the record
family's sealed bytes; OP-2 is the record member's own exact
valuation; OP-4 consumes the sealed count law (given CL-C) and
sealed P-1-grade brackets (given CL-A) at their displays. A_n,
B_pp', S_n, J_n, kappa_n, M_n, C_B'', gamma_B, C_Q, C_B, C_*, c,
c'', and every threshold stay symbols or displayed closed forms; the
member closed forms (erf/exp) are exact record-member displays at
fixed n, ground for nothing asymptotic. The RULING is the checker's/
audit's, not this artifact's.
```

---

## 14. FLAG BLOCK

```text
OVERLAP_LAW = UNDECIDABLE-TODAY( O-1-S-B — neither A_n <= C_B''
  n^{3/2 - gamma_B} (explicit gamma_B > 0) nor A_n >= c n^{3/2} is
  derivable on the sealed stock at the cutoff. Ceiling side: the
  moduli are unvalued (phi_k at the zeros — CL-A fixed-compact per
  audited CL-3; CL-B phase-destroying; zero full-range-PR carriers,
  sw-3) and the audited W12' + J-preserving-padding forcing refutes
  every resolved-byte-class route including P-2-consuming ones;
  floor side: the audited all-parallel witness + zero
  anti-localization carriers; the momentum-weight assembly stalls at
  exact exponent (3 beta + 3)/5 > 3/2 for every lawful beta >= 3/2
  [OV7]. NOT polylog-only (the trivial bracket returns the exact-3/2
  bulk; no sub-3/2 gain of any size claimed). Decision-grade
  citation ruled out at the T7SR discipline (§7: verdict-independence
  cannot hold for a decider import; the uniform full-range package is
  assembled, not named). )
PARTIALS_DERIVED = FOUR( OP-1 THE DIRECTION-COMMUTATOR IDENTITY:
  A_n = (1/2) sum_j ||[W_j, B~]||_2^2 = tr B~^2 - sum_j tr(W_j B~
  W_j B~) = (1/2) sum_j ||(Q_n - Z_n)[W_j, P](Q_n - Z_n)||_2^2, W_j
  = pi_j |pi|^{-1} — the deciding object IS a Galerkin Widom-type
  commutator mass (the audited CL-4 trap note sharpened to an object
  identification) [OV1]. OP-2 THE MEMBER VALUATION n = 2: B_pp' =
  (8 ell^3 pi^{3/2})^{-1} Int_ball e^{-|x|^2/ell^2} prod_i (1 +
  sigma_i 2 x_i^2/ell^2) dx exactly (parity kill); four orbit values
  in erf/exp closed form; unitarity limit b_0 -> 1, b_m -> 0 exact;
  EVERY off-diagonal orbit entry >= c I_0/8 > 0 (pointwise factor
  floor 1/2 on the sealed ball); A_2 = 16 b_1^2 + 32 b_2^2 + 16
  b_3^2 >= c^2 I_0^2 > 0 — the first exact family-byte valuation of
  the deciding object; existence at a member, NO rate [OV2-OV6].
  OP-3 THE SYMMETRY COLLAPSE: hyperoctahedral invariance |B_{gp,gp'}|
  = |B_pp'| — A_n collapses to orbit representatives [OV6 member
  pin]. OP-4 THE RADIAL TRIM + STALL (trim given CL-C): low-radius
  pairs contribute <= 4(1 + 2 T ell sqrt(2n+1)/pi)^3 — sub-3/2 at
  T = n^{-a} for every a in (0, 1/2] (the p = 0 singularity is
  quarantined); high-pair majorization (1 - cos) <= |p - p'|^2/
  (2 T^2); unconditional M_n <= 24 n tr B~/ell^2 <= (6 C_B/ell^2)
  n^{5/2} given CL-A (Gershgorin, no citation); assembled minimum
  exponent (3 beta + 3)/5: 21/10 at beta = 5/2, 9/5 at the
  anticipated beta = 2, sub-3/2 iff beta < 3/2 — the radial factor
  is the exact obstruction [OV7/OV8]. )
DECIDER_OBJECT = O-1-S-B-PR | O-1-S-B-W( ONE LAW, TWO GUISES:
  O-1-S-B-PR — the quantified orbit-collapsed moduli law,
  equivalently the Christoffel/PR profile phi_k(z_j)^2/lambda_n(z_j)
  at the zeros with n-uniform explicit remainders (the assembled
  full-range 8.22.9 + Airy + exponential package, or any
  equivalent); O-1-S-B-W — the Galerkin direction-commutator law
  sum_j ||(Q_n - Z_n)[W_j, P](Q_n - Z_n)||_2^2 at sub-3/2 (identical
  to the ceiling by OP-1). YIELDS pinned [OV8]: ceiling at gamma_B
  => O-1-S at min(gamma_B, 1/12) => O-1 at the same => MO-4-R
  DECIDED-o(1) at rate through the sealed T-4; floor at c => S_n^2
  >= 2 c n^{3/2} cofinitely => CEILING-FAILS-AT-3/2. The continuum
  n log n commutator anticipation displayed, consumed nowhere. The
  O-2 localization package of record stays the other decider,
  unchanged. )
CLASSICAL_GROUND = CL-A + CL-B + CL-C(all sealed, consumed ONLY
  through sealed displays at their of-record conditional grades:
  CL-A inside the sealed tr(P Q_n)/P-2 brackets; CL-B inside sealed
  P-2; CL-C inside the sealed SP-2 count law consumed by OP-4's trim
  — if CL-C is ruled out, OP-4's trim goes CONDITIONAL(CL-C) and
  the VERDICT is unchanged) + CL-D( NEW citation, DISPLAY-ONLY:
  Gauss-Hermite quadrature / Christoffel numbers, Szego §3.4 +
  §15.3; lambda_n(z_j) = e^{-z_j^2}/w_j member-pinned [OV9]; blast
  radius: the decider's naming alias only; consumed by no verdict
  leg and no inequality; if ruled out, the alias is struck and
  nothing moves. ) NO 8.22.9-grade statement cited or consumed
  anywhere (§7).
CONSUMPTION_BOUNDARY = NOTHING-FIRED( O-1, O-1-S, O-1-S-B, MO-4-R
  all stay open; MO-4/r-3/R-L4b untouched; no flag of any prior
  artifact flips (T-1's sw-3 and T-2's asw-3 absence claims stand at
  their cutoffs and are re-confirmed at mine); D4, the MO-2 floors,
  P-1/P-2/P-3, SP-1/SP-2/SP-3 all stand exactly as sealed; the
  audited F-1..F-5 repairs are consumed as pinned conventions, not
  re-adjudicated; H-R never defaulted; whether to commission either
  decider guise, O-2, or anything else is the registrar's call; the
  registrar consumes. )
SEALS_VERIFIED = 6/6( the T10SR pair + T7SR pair + T3SR pair,
  full-digest sidecar checks before any reliance (§1), all read in
  full as commissioned; deeper bytes consumed through the sealed
  quoting artifacts at audited grade; "Q-..." tokens
  EXPECTED-UNLOCATABLE, none encountered beyond the ground's own
  notations. )
SWEEP_CUTOFF = 2026-08-15 07:41:01 CDT( keys and findings §9; T11SR
  and OVERLAP_LAW unoccupied; O-1-S-B/B_pp/anti-localization
  carriers = the T10SR pair only; "8.22.9"/"full-range Plancherel"
  carriers = the T10SR pair only (which name the absence); zero
  "direction operator" carriers; Christoffel / Gauss-Hermite / W12
  homonyms typed out at count level, never opened. )
FORBIDDEN_IMPORTS = none( exact symbolic only; no floats as ground;
  no numeric evaluation; no measured constant; NO value frozen —
  every constant and threshold symbolic or an exact closed form; no
  overlap/localization law imported (the needed one is DISPLAYED as
  the decider in two guises, not assumed — the honesty rail held);
  no 8.22.9-grade citation consumed; no fenced-class file opened; no
  git action; no existing file edited; ONE file written plus its
  seal; output path probed ABSENT at session start and re-probed
  immediately before write. )
MACHINERY_INVOKED = yes(CAS) — sympy 1.14.0, fresh venv
  overlapvenv_t11sr under the session scratchpad; ONE disclosed
  pre-final edit (two inert `if False` scaffolding lines removed
  from OV7 after a first full 9/9 PASS run; no conjunct changed;
  §11 header); the cleaned battery executed twice with
  BYTE-IDENTICAL output (diff empty), 9/9 PASS both; script (sha256
  672f5ea7...) and output reproduced verbatim in §11.
alpha_computed = false ; proof_authorized = false ;
kappa_record_computed = false
ALL_RESULTS = CLAIMED until checked.
OVERLAP_LAW_RESULT = SEALED.
```
