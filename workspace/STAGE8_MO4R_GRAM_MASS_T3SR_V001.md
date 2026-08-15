# STAGE 8 — MO-4-R OF RECORD: THE NEAR-1/4 CLASS vs THE b_D-BULK GRAM MASS — THE GRAM-TRANSFER REDUCTION, THE WITNESS PAIR, AND THE VERDICT — T3SR V001

## BLIND BUILDER — CODENAME MO4R-BUILD — COMMISSION T3SR — [CLAIMED]

Date: 2026-08-15 (session CDT). Role: BLIND builder (MO4R-BUILD).
Commission: THE QUESTION, exact — does the near-1/4 eigenvector class of
Y_n Y_n^dag carry an o(1) fraction of the b_D-bulk Gram mass? The ONE
residue left from the MO-4 round (MO-4-R as named of record). Verdict
menu as commissioned: DECIDED-o(1) / DECIDED-NOT-o(1) /
UNDECIDABLE-TODAY. Technique named of record: the Gram transfer (the
profile-split factorization) — attempted FIRST (§3); other exact routes
lawful (§4). "Q-..." tokens inside sealed artifacts are
EXPECTED-UNLOCATABLE by design; noted, never chased (none encountered
beyond the ground pair's own notations).

Gates: `alpha_computed = false` ; `proof_authorized = false` ;
`kappa_record_computed = false`. ALL_RESULTS = CLAIMED until checked.
DETERMINATION ONLY — no adoption, no authored physics, no member
binding; the registrar consumes.

Fences held: EXACT SYMBOLIC DERIVATION ONLY — one CAS battery (sympy
1.14.0, fresh venv `mo4rvenv` under the session scratchpad), reproduced
verbatim in §9 (final battery ran ONCE, 9/9 PASS, no pre-final
corrections); every constant symbolic or an exact rational/closed form;
NOTHING numeric evaluated; no floats as ground; no measured constant; NO
value frozen (kappa_n, rho_n, eps_*, ell, c_G, C_G, C_*, K(eps_*), all
thresholds and all decider constants stay symbols; symbolic scales
only); no file matching register|road_|ledger|lens|plan|tracker|
THE_HANDOFF|continuation opened (filename-level listing only, per the
audited discipline); no git action; no existing file edited; ONE output
(this artifact) plus its seal sidecar at the commission-distinct path,
probed ABSENT at session start AND re-probed immediately before write.
Marks: DERIVED / CLAIMED / CLASSICAL(cited, inherited) /
CONDITIONAL(premise named) span by span.

SWEEP CUTOFF, DECLARED: the corpus sweep of §7 was executed against the
tree state as of **2026-08-15 02:57:40 CDT** (supplementary post-cutoff
mtime scan immediately following, same state). Artifacts sealed after
that instant are not consumed and not swept. MO-4-R occupation at the
cutoff: NONE (§7 sw-1); commission id T3SR appears nowhere but here.

---

## 0. VERDICT IN ONE LINE

**UNDECIDABLE-TODAY — and the undecidability is FORCED at the
displayed-hypothesis grade, not a search failure. What IS derived (new,
exact): the Gram transfer applies to the class itself and yields the
CLASS-MASS REDUCTION — for every window eps in (0, 1/2), the near-1/4
spectral projection E_n(eps) of Y_n Y_n^dag obeys E_n(eps) <=
(1/4 - eps^2)^{-1} Y_n Y_n^dag as PSD operators (boundary-tight), so the
class b_D-Gram mass obeys mass_n(eps) <= (1/4 - eps^2)^{-1} X_n with
X_n := int_0^1 tr(Y_n Y_n^dag (b_D(s) tensor 1_4)) ds <= kappa_n/2, and
with the certified two-sided Gram mass of record (G_n >= c_G n^{3/2}),
the FRACTION obeys F_n(eps) <= 2 kappa_n / ((1 - 4 eps^2) c_G n^{3/2}):
THE QUESTION is thereby REDUCED, on its o(1) side, to the clock's upper
exponent — any certified kappa_n <= C n^{3/2 - gamma} (gamma > 0)
DECIDES o(1) with rate n^{-gamma} through today's display. The exact
blockers, swept: (i) o(1) is blocked SOLELY by the absent sub-3/2 clock
ceiling — the only sealed ceiling is D4's kappa_n <= 2n^3, whose
substitution is VACUOUS at exact power n^{3/2} (CAS R6); r-3 D9 of
record: no upper rate; re-swept at the cutoff: no carrier exists;
(ii) NOT-o(1) is blocked by the absent quantified 1/2-approach/
localization law (r-3 :469/:808 absence, s-6 of record, re-swept: no
carrier exists) — a class-count floor of order n^{3/2} would already
force kappa_n >= c n^{3/2} (unsealed; only the linear floor is sealed),
and the required per-vector b_D-mass floor is a localization statement
the corpus does not own. The WITNESS PAIR (CAS R8): two exact models
with IDENTICAL projections, identical clock value, identical profile
bounds 0 <= b <= 1, whose class fractions are 0 and 1 — no
identity-grade route from the hypothesis class my lawful ground displays
can decide THE QUESTION in either direction; a family-specific
joint-localization datum is REQUIRED (exactly the audited countermodel's
yield, now at the fraction grade). Scope display (CAS R7): R_n =
(1 - 2 T_n)^{-1} commutes with the class, the far-class resolvent norm
is <= 1/(2 eps_n), and the far-class chain over the certified linear
clock is EXACTLY (4 K C_G/(C_* eps_n)) sqrt(n): even F_n identically 0
would NOT close MO-4 at the linear clock — the fraction is the
localization HALF of MO-4-R, the clock exponent is the other half. THE
NEW SEALED OBJECT THAT WOULD DECIDE IT: O-1 (the clock ceiling, the
ceiling twin of MO-2): a certified kappa_n <= C-dag n^{3/2 - gamma},
gamma > 0 — decides DECIDED-o(1) with certified rate via today's
display; or O-2 (the localization package): a class-count floor >=
c' n^{3/2} PLUS a quantified surface-localization mass floor on the
class — decides DECIDED-NOT-o(1) with a displayed positive fraction
floor. Exhaustive trichotomy displayed (§6). Nothing fires: MO-4 stays
open, MO-4-R stays open but stands REDUCED; no flag flips; the
registrar consumes. CAS battery 9/9 PASS.**

---

## 1. SEALS VERIFIED AT PATH (shasum -a 256), BEFORE ANY RELIANCE

All under `/Users/bgm/MB Work/alpha-program-archive/workspace/`. Every
file consumed at any grade this session was seal-verified by FULL digest
against its sidecar BEFORE consumption. 9/9 MATCH.

```text
GROUND (read in full; the residue-naming section §4.5 + RESIDUAL_NAMED
flag read whole, as commissioned):
T-G1 0e894372d1c53dc6d66d171da08b13c4a756bea9da9bcd7c4c2863645300e127
     STAGE8_MO4_CANCELLATION_S9AD_V001.md          MATCH — the
     profile-split Gram factorization; the trace chain and K(eps_*); the
     two-sided Gram mass c_G n^{3/2} <= G_n <= C_G n^{3/2} (given CL-A,
     at MO-2's authorized discipline); the exact ratio (8 K C_G/C_*)
     rho_n sqrt(n); the crossing identity (1 + A_n(0))^2 = 1 - 4 Y_n
     Y_n^dag, Y_n = C_n P C_n^perp, tr Y_n Y_n^dag = kappa_n/2; the
     refused corpus mechanisms at their displays (§3 there — NOT
     re-walked here); MO-4-R named at §4.5; the surface-vs-bulk
     diagnosis (Lambda^2 vs Lambda^3).
T-G2 bfd86217319ecabca67352fa23d0cf4d0f9926b564924681cb383c57622678b0
     STAGE8_MO4_CANCELLATION_S9AD_AUDIT_V001.md    MATCH —
     CONFIRMED-WITH-CORRECTIONS (all cosmetic); the independent
     countermodel bracket (first jet always dies; jet order 2 breaks
     under plane mixing; phase-only cancels identically); the yield:
     MO-4-R needs a family-specific localization/plane statement;
     c-4's notational note (crossing operator vs scalar G_n) respected
     here: the scalar Gram mass is G_n, the crossing operator is
     written 1 - 4 Y_n Y_n^dag throughout.
SWEEP-CONSUMED (match-level lines only, seal-verified before reliance):
T-S1 STAGE8_R3_JOINT_RATE_S9AD_V001.md             MATCH — D2/D4/D10
     displays (kappa_n = 2 sum s_i(1-s_i) <= 2N(1/4) = N/2 = 2n^3 with
     N = 4n^3 EXACT; near-1/2 eigenvalues MAXIMIZE kappa mass); :469/
     :808 (the missing quantified 1/2-approach/avoidance law).
T-S2 STAGE8_R3_JOINT_RATE_S9AD_AUDIT_V001.md       MATCH — same
     displays at audited grade.
T-S3 STAGE8_MO2_KAPPA_RATE_S9AD_V001.md            MATCH — sweep-key
     corroboration only (its own sweep keys include "Widom"; no ceiling
     carrier).
T-S4 STAGE8_MO2_KAPPA_RATE_S9AD_AUDIT_V001.md      MATCH — CL-4: the
     MO-2 build "does NOT cite Widom/Sobolev-class" — no ceiling-grade
     classical ground was ever imported for kappa_n.
T-S5 STAGE8_WALL_BOUNDARY_CLOSURE_S9AD_AUDIT_V001.md MATCH — ceiling
     mentions are D4-references only.
T-S6 STAGE8_REFUTING_BRANCH_S9AD_V001.md           MATCH — same.
T-S7 STAGE8_RATE_GAP_LINKAGE_S9AD_V001.md          MATCH — same.
```

Consumption through sealed quotes: every r-3/MO-2/MO-3/PA byte relied on
below enters through T-G1/T-G2 at audited grade (their §1 tables pin
bebc0f08, 6997ff61, 9fdc3d1c, and the PA displays); the T-S reads are
corroboration of the SAME displays at their source bytes, seal-verified.
No other file opened. No fenced-class file opened.

---

## 2. THE QUESTION AND THE OBJECTS, AT BYTES

The residue naming, verbatim from T-G1 §4.5 (the commissioned ground):

```text
"MO-4-R asks: do the near-1/4 eigenvectors of Y_n Y_n^dag (the crossing
class, ball-SURFACE mass kappa_n) carry an o(1) fraction of the
b_D-BULK Gram mass? UNDECIDED in both directions on the sealed stock
(no closed-form spectrum, r-3 F-3; no eigenvector localization theorem
sealed anywhere — §5 sweep)."
```

Objects, pinned (all of record via T-G1 at audited grade):

```text
O-a  T_n := C_n P C_n on ran C_n; spectrum {s_i} subset [0,1];
     N := rank C_n = 4n^3 (T-S1 D4 display at bytes). 1 + A_n(0) =
     C_n S C_n = 1 - 2 T_n on ran C_n (S = 1 - 2P; one-line algebra),
     hence R_n = (1 - 2 T_n)^{-1}: R_n is a FUNCTION of T_n and
     commutes with every spectral projection of T_n. [DERIVED; the
     square of this display is the sealed crossing identity.]
O-b  Y_n Y_n^dag = C_n P C_n^perp P C_n = T_n - T_n^2 (projection
     algebra; fresh exact instance CAS R3a); eigenvalues s_i(1 - s_i),
     eigenvectors THOSE OF T_n; tr Y_n Y_n^dag = kappa_n/2, kappa_n >=
     C_* n/8 cofinitely (MO-2, constants symbolic); kappa_n <= 2n^3
     (D4); kappa_n = ||[P, C_n]||_2^2 (CAS R4 + cyclicity: expand
     tr((PC - CP)^dag(PC - CP)) = 2[tr(CPC) - tr((CPC)^2)]). [DERIVED]
O-c  THE CLASS, window-exact: for eps in (0, 1/2), E_n(eps) :=
     1_{[1/4 - eps^2, 1/4]}(Y_n Y_n^dag) restricted to ran C_n
     = 1_{|s_i - 1/2| <= eps}(T_n) — the two descriptions coincide by
     s(1-s) = 1/4 - (s - 1/2)^2 (CAS R1). "Near-1/4 class" of record =
     this family; both quantifications covered: fixed eps, and
     shrinking windows eps_n -> 0.
O-d  THE MASS AND THE FRACTION: b_D(s,x) = e^{16 - 1/(s_- s_+)} on the
     open diamond (PA bytes via T-G1); 0 <= b_D <= 1 with equality only
     at (1/2, 0) (CAS R5). Class mass mass_n(eps) := int_0^1
     tr(E_n(eps) (b_D(s) tensor 1_4) E_n(eps)) ds. Denominator, pinned
     at the residue's own naming: the b_D-bulk Gram mass G_n = 4
     int_0^1 int b_D(s,x) K3(x,x) dx ds, certified c_G n^{3/2} <= G_n
     <= C_G n^{3/2} (given CL-A; grades inherited). FRACTION F_n(eps)
     := mass_n(eps) / G_n. THE QUESTION: F_n(eps) -> 0?
```

---

## 3. THE TECHNIQUE OF RECORD, ATTEMPTED FIRST — THE GRAM TRANSFER, AND EXACTLY WHERE IT STOPS

The profile split b_D = (b_D^{1/2})^2 is what makes the class mass a
Gram (HS) quantity: mass_n(eps) = int_0^1 ||(b_D(s)^{1/2} tensor 1_4)
E_n(eps)||_2^2 ds. The transfer then runs in three exact steps.

```text
T-1 CLASS DOMINATION (spectral, boundary-tight). For every eps in
    (0, 1/2):  E_n(eps) <= (1/4 - eps^2)^{-1} (T_n - T_n^2)
    as PSD operators on the whole space. Proof: both sides vanish off
    ran C_n and are diagonal in the eigenbasis of T_n; on an
    eigenvector with |s_i - 1/2| <= eps the right side's coefficient is
    s_i(1-s_i)/(1/4 - eps^2) >= 1 (CAS R1: the difference factors as a
    product of nonnegatives on the window); off the window the left
    side is 0 and the right side >= 0. Boundary-TIGHT at |s_i - 1/2| =
    eps (CAS R3b: gap exactly 0 there). [DERIVED]
T-2 THE TRANSFER. Conjugation preserves the PSD order (CAS R2:
    tr(X^T (M^T M) X) = ||MX||_F^2 all-symbolic), so with b~ :=
    b_D(s) tensor 1_4:  tr(E b~ E) = tr(b~^{1/2} E b~^{1/2}) <=
    (1/4 - eps^2)^{-1} tr(b~^{1/2} (T_n - T_n^2) b~^{1/2}), hence
      mass_n(eps) <= (1/4 - eps^2)^{-1} X_n,
      X_n := int_0^1 tr(Y_n Y_n^dag (b_D(s) tensor 1_4)) ds
    — the resolvent-free core of the sealed W_n object: the b_D-weighted
    crossing mass. [DERIVED]
T-3 THE SPECTATOR CEILING. 0 <= b_D <= 1 (CAS R5), and for PSD A and
    0 <= b <= 1: 0 <= tr(A b) <= tr(A) (CAS R9: tr((N^T N)(M^T M)) =
    ||M N^T||_F^2 >= 0, applied to b and to 1 - b). Hence
      X_n <= tr(Y_n Y_n^dag) = kappa_n / 2,
    and the COUNT TWIN: tr E_n(eps) <= 2 kappa_n / (1 - 4 eps^2).
    [DERIVED]
T-4 ASSEMBLY (CAS R6). mass_n(eps) <= 2 kappa_n / (1 - 4 eps^2), and
    with the certified floor G_n >= c_G n^{3/2} (n >= n_1', given CL-A):
      F_n(eps) <= 2 kappa_n / ((1 - 4 eps^2) c_G n^{3/2}),
    uniformly in the window family (shrinking windows eps_n -> 0 give
    constant -> 2/c_G). [DERIVED given CL-A through the sealed floor]
THE STOP, EXACT: the transfer's terminal display cannot value kappa_n.
    The ONLY sealed ceiling is D4's kappa_n <= 2n^3, and its
    substitution gives F_n(eps) <= 4 n^{3/2}/((1 - 4 eps^2) c_G) —
    VACUOUS at exact power 3/2 (CAS R6). The sealed floor runs the
    wrong way. r-3 D9 of record: the denominator has no upper rate;
    re-swept at the cutoff (§7 sw-2): no sub-3/2 ceiling carrier exists
    in either commissioned root. The Gram transfer therefore DELIVERS
    the reduction and CANNOT deliver the verdict.
```

What the transfer proves about the question's structure: THE o(1) SIDE
IS EXACTLY A CLOCK-CEILING QUESTION — any certified kappa_n <=
C n^{3/2 - gamma} (gamma > 0) decides DECIDED-o(1) with rate n^{-gamma}
through T-4 (CAS R6, limit exact), for every window at once. No converse
is claimed (localization could make F_n small with a large clock).

---

## 4. THE OTHER EXACT ROUTES, SWEPT — EACH REFUSED AT ITS OWN DISPLAY

```text
RT-A MOMENT/COUNTING ROUTES. Within the lawful ground the certified
     spectral data of T_n are EXACTLY: 0 <= T_n <= 1; rank = N = 4n^3
     (D4 bytes); tr(T_n - T_n^2) = kappa_n/2 with the linear floor and
     the 2n^3 ceiling. Every moment route to the window count factors
     through tr(T_n - T_n^2) — the clock again (T-3's count twin is
     already the sharp form); interlacing/rank routes give tr E <= N =
     4n^3, vacuous by n^{3/2} against the bulk. tr T_n itself is
     unsealed and would not localize the window without the second
     moment, which IS the clock. REFUSED: every counting route lands on
     the same absent ceiling. [DERIVED]
RT-B X_n FLOOR ROUTES (toward NOT-o(1)). b_D >= b_min 1_W on the exact
     rational window W (V10 bytes of record) gives X_n >= b_min
     int_{3/8}^{5/8} tr(Y_n Y_n^dag 1_W-box) ds — unvalued: nothing
     sealed locates ANY crossing mass inside (or outside) the central
     box; the of-record surface heuristic even points the other way
     (class mass at |x| = r(t), outside a small central box), and a
     heuristic is not ground. No X_n floor is derivable; equally no
     improved X_n ceiling below kappa_n/2 (joint localization absent in
     both directions). CAS R9 + R8-A: X = 0 is realizable at fixed
     clock in the hypothesis class. REFUSED both ways. [DERIVED]
RT-C INVOLUTION/PARITY. The chiral involution exits ran C_n (block
     exchange — refusal of record, T-G1 §3.1); its spectral consequence
     (s <-> 1-s cross-block symmetry up to rank <= 4) fixes the WINDOW
     setwise and carries no mass information into the block; spatial
     parity is a norm symmetry (T-G1 §3.2). REFUSED at the sealed
     displays; not re-walked. [of record]
RT-D C_n-BYTES ROUTES. kappa_n = ||[P, C_n]||_2^2 (CAS R4) is the
     ceiling object in its natural form, but valuing it needs the
     r-2 realization bytes of C_n — OUTSIDE this commission's lawful
     ground (r-2 is not named in the T3SR ground; the pure-Hermite
     realization enters only as the inherited premise CH-8 of record).
     The ceiling is a NEW commission (O-1), not a today-derivation.
     REFUSED as out of ground, exactly. [DERIVED at the boundary]
RT-E THE CLOSURE-SIDE SPLIT (scope display). R_n = (1 - 2 T_n)^{-1}
     (O-a) commutes with E_n(eps_n); on the far class the spectral
     bound |1 - 2s| = 2|s - 1/2| >= 2 eps_n gives ||R_n E_n^perp||_op
     <= 1/(2 eps_n); running the sealed §4.2 chain with that spectator:
     ||R_n E_n^perp Delta_n(a)||_1 <= K(eps_*) G_n/(2 eps_n), and over
     the certified linear clock the ratio is EXACTLY (4 K(eps_*) C_G /
     (C_* eps_n)) sqrt(n) (CAS R7). Since eps_n <= 1/2 always, the far
     class ALONE overshoots the linear clock by sqrt(n): even F_n
     identically ZERO would not close MO-4 at the certified clocks.
     THE QUESTION is the localization HALF of MO-4-R; the clock
     exponent is the other half; the deciders of §6 cover both. This
     display refutes nothing sealed — it sharpens the of-record
     tightening ("the package needs the extra sqrt(n)"). [DERIVED]
```

---

## 5. THE WITNESS PAIR — UNDECIDABILITY AT THE DISPLAYED-HYPOTHESIS GRADE IS FORCED

CAS R8, exact: P = rank-1 projection onto (e_1 + e_2)/sqrt(2), C =
diag(1, 0). Then T = CPC = diag(1/2, 0): an EXACT crossing eigenvector
(s = 1/2, the class at every window), Y Y^dag = diag(1/4, 0), clock
value 2 tr Y Y^dag = 1/2. Two profiles, both multiplication operators
with 0 <= b <= 1 and total profile-Gram mass tr b = 1:

```text
  b_A = diag(0, 1):  class b-mass = 0   -> fraction 0;
  b_B = diag(1, 0):  class b-mass = 1   -> fraction 1.
```

IDENTICAL projections, identical clock value, identical profile bounds,
identical total mass — opposite fractions. Consequence: no
identity-grade route quantified over the hypothesis class my lawful
ground displays (projections P, C; a [0,1]-bounded multiplication
profile; the clock's value and floor; the Gram mass's two-sided rate)
can decide THE QUESTION in either direction. Deciding it REQUIRES a
family-specific joint-localization datum — the fraction-grade twin of
the audited countermodel's yield ("MO-4-R needs a family-specific
localization/plane statement"). UNDECIDABLE-TODAY is therefore FORCED,
not a search shortfall. TOY STATUS: the pair refutes derivability
claims only; it asserts NOTHING about the record family's own fraction,
which stays undecided in both directions.

---

## 6. THE VERDICT AND THE DECIDER MENU

**VERDICT: UNDECIDABLE-TODAY.** Both directions blocked at exact,
swept absences; the blockers and the deciding objects:

```text
BLOCKER-1 (blocks o(1)): no sealed ceiling kappa_n <= C n^{3/2 - gamma}
  for any gamma > 0 (D4's 2n^3 vacuous at power 3/2, CAS R6; D9 of
  record; sw-2 at the cutoff: no carrier).
BLOCKER-2 (blocks NOT-o(1)): no sealed quantified 1/2-approach/
  localization law for {s_i} or their eigenvectors (r-3 :469/:808;
  s-6 of record; sw-3 at the cutoff: no carrier). A class-count floor
  of order n^{3/2} would force kappa_n >= (1 - 4 eps^2) c' n^{3/2} / 2
  by the count twin (T-3) — itself unsealed — AND a per-vector b_D-mass
  floor on the class is required, which is a localization statement.

O-1 THE CLOCK CEILING (the ceiling twin of MO-2; decides o(1)): a NEW
  sealed certificate kappa_n <= C-dag n^{3/2 - gamma}, gamma > 0, both
  symbolic — equivalently any X_n = o(n^{3/2}) certificate (X_n <=
  kappa_n/2 makes the kappa form sufficient). CONSUMES: the r-2
  realization bytes of C_n (kappa_n = ||[P, C_n]||_2^2 is the object's
  natural form, CAS R4) plus classical ground at CL-A's discipline —
  the anticipated shape per the of-record surface diagnosis (the clock
  counts the crossing-SURFACE class, Lambda^2 at Lambda = sqrt(2n)/ell)
  is kappa_n ~ n x polylog(n); ANTICIPATION only, never ground. YIELD:
  DECIDED-o(1) with certified rate F_n(eps) <= (2 C-dag / ((1 - 4
  eps^2) c_G)) n^{-gamma} — today's T-4 display, nothing else needed.
O-2 THE LOCALIZATION PACKAGE (decides NOT-o(1)): (i) a class-count
  floor tr E_n(eps_0) >= c' n^{3/2} at some fixed eps_0 in (0, 1/2),
  AND (ii) a quantified surface-localization law: int_0^1 <v_i, (b_D(s)
  tensor 1_4) v_i> ds >= m_0 > 0 for at least a c''-fraction of the
  eps_0-class. YIELD: DECIDED-NOT-o(1) with the displayed floor
  F_n(eps_0) >= c'' c' m_0 n^{3/2} / (C_G n^{3/2}) = c'' c' m_0 / C_G
  > 0 (n-free, symbolic), using the certified Gram CEILING of record.
TRICHOTOMY (exhaustive in the clock's true upper exponent alpha-k :=
  limsup log kappa_n / log n, displayed for the registrar):
    alpha-k < 3/2  ==> O-1 exists in principle; once sealed, o(1) is
                       DECIDED by T-4. THE QUESTION = the clock race.
    alpha-k = 3/2  ==> T-4's ceiling is n-free (CAS R6): the ceiling
                       route saturates; localization alone decides.
    alpha-k > 3/2  ==> T-4 vacuous; NOT-o(1) becomes possible but
                       still requires O-2(ii) — count alone never
                       supplies the b_D-mass floor (R8 witness A).
  In EVERY regime a family-specific new sealed object is required;
  none exists at the cutoff (§7). The commissioning choice between O-1
  and O-2 is not a lane's call; the registrar consumes.
```

---

## 7. THE SWEEP (exhaustive at this displayed sweep only; cutoff in header)

```text
ROOTS (as commissioned): /Users/bgm/MB Work/alpha-program-archive/
workspace (primary; the parent archive ranged at FILENAME level only)
and /Users/bgm/Documents/New project/gravity_emergence_evidence_program/
alpha_fundamental_record_action_cleanroom_v003 (cleanroom). Fenced name
classes (register|road_|ledger|lens|plan|tracker|THE_HANDOFF|
continuation) excluded from every opening; filename-level listing only.
KEYS RUN: "MO-4-R"; "MO4R"; "T3SR"; "near-1/4"; "1/2-approach";
"eigenvector localiz"; "clock ceiling"; "kappa ceiling"; "upper rate
for kappa"; "Widom"; post-audit-cutoff mtimes + residue keys
("MO-4"; "Y_n Y_n"; "near-1/4"; "Gram mass").
FINDINGS:
 sw-1 MO-4-R/T3SR OCCUPATION: the only carriers of the residue's name
      are the sealed ground pair. No artifact claims MO-4-R; T3SR
      appears nowhere. UNOCCUPIED at the cutoff; no collision.
 sw-2 CLOCK-CEILING CARRIERS: every hit is the D4 ceiling 2n^3 (r-3
      + audit D4 displays, at bytes, seal-verified) or an absence
      disclaimer (MO-2 audit CL-4: "does NOT cite Widom/Sobolev-
      class"; MO-2's own sweep lists "Widom" as a KEY with a
      supervision FILENAME hit only). NO kappa_n upper rate below
      2n^3 exists in either commissioned root.
 sw-3 LOCALIZATION CARRIERS: only the absence statements (r-3 :469
      "a quantified 1/2-approach/avoidance law for {s_i}" listed as
      missing; :808 same; the ground pair's s-6). No law exists.
 sw-4 CLEANROOM ROOT: ZERO hits on every key.
 sw-5 POST-AUDIT-CUTOFF ARTIFACTS (IDEAL_EXTENT pair, RK_LT_BIT S9AD
      and T1SR pairs, WALL_SUMMED_REQUANT audit): none carries any
      residue key — the residue is untouched since the audit's cutoff.
 sw-6 OUT-OF-ROOT NOTE: one supervision FILENAME surfaced under the
      "Widom" key (BOHM_BLIND_DIXMIER_VERDICT_2026-07-28.md), outside
      the commissioned roots; NOT opened; noted for the registrar.
```

Each sentence claims only this displayed sweep at the declared cutoff.

---

## 8. CONSISTENCY WITH THE SEALED STOCK — EVERY CONTACT POINT

```text
X-1 vs T-G1 §4.5 (the residue): consumed verbatim; the reduction T-1..
    T-4 REFINES the residue (its o(1) side now hangs on one named
    exponent) and moves no verdict: UNDECIDED-of-record becomes
    UNDECIDABLE-TODAY with the blockers exact — strictly more
    information, no contradiction.
X-2 vs D4/D9 (r-3): D4's ceiling is consumed ONLY as the vacuity
    display (power 3/2 exact, CAS R6); D9's "no upper rate" is
    re-confirmed by sw-2. Nothing bounds kappa_n anew here.
X-3 vs MO-2: the floor is consumed at its sealed quantifier (kappa_n >=
    C_* n/8 cofinitely, constants symbolic) in R7's scope display only;
    the floor is never used to decide the fraction (it runs the wrong
    way for o(1) and is too weak for NOT-o(1) — displayed in §6).
X-4 vs the audited countermodel (T-G2 §2): my witness pair is its
    fraction-grade twin — same verdict shape (family-specific datum
    required), new grade (the b_D-mass fraction itself). Consistent;
    neither consumes the other's toy as family ground.
X-5 vs H-R / FRAME-N2: rho_n appears NOWHERE as a bound in this
    artifact; the far-class display uses the SPECTRAL bound 1/(2 eps_n)
    on the far window only, which is exact functional calculus of T_n
    (O-a), not an H-R default. The near-class resolvent stays unvalued.
X-6 vs the fences: no closure claimed, no member bound, no physics
    authored; the fraction stays undecided of record; whether to
    commission O-1 or O-2 is the registrar's call. F-d, R-L4b, r-3:
    untouched; no flag of the sealed pair flips; all witnesses STAND.
```

---

## 9. THE CAS BATTERY (VERBATIM) AND ITS OUTPUT (VERBATIM)

sympy 1.14.0, fresh venv `mo4rvenv` under the session scratchpad;
nothing written to the workspace but this artifact and its seal. The
final battery ran ONCE: 9/9 PASS; no pre-final corrections.

```python
# MO4R-BUILD CAS battery -- EXACT SYMBOLIC ONLY (sympy 1.14.0, fresh venv
# mo4rvenv under the session scratchpad). Commission T3SR. Every constant
# symbolic or an exact rational/closed form; nothing numeric evaluated; no
# floats as ground. All checks are exact-identity consistency checks of steps
# whose operator-theoretic content is derived in the artifact text.
import sympy as sp
from sympy import Rational as R

ok = lambda name, cond: print(f"{name}: {'PASS' if cond else 'FAIL'}", flush=True)

# ===== R1 -- the window identity: the near-1/4 class of Y Y^dag IS the
# |s_i - 1/2| <= eps class of C_n P C_n =====
s, e = sp.symbols('s epsilon', real=True)
ok("R1 WINDOW: s(1-s) = 1/4 - (s-1/2)^2 EXACT, so s(1-s) in [1/4-eps^2, 1/4]"
   " iff |s-1/2| <= eps; and on the window s(1-s) - (1/4-eps^2) ="
   " (eps-(s-1/2))(eps+(s-1/2)), a product of nonnegatives -- the window"
   " floor grounding E <= (1/4-eps^2)^{-1}(T - T^2)",
   sp.expand(s*(1-s) - (R(1,4) - (s - R(1,2))**2)) == 0
   and sp.expand((e - (s - R(1,2)))*(e + (s - R(1,2)))
                 - (e**2 - (s - R(1,2))**2)) == 0)

# ===== R2 -- the conjugation step of the Gram transfer, all-symbolic =====
Xm = sp.Matrix(2, 2, lambda i, j: sp.Symbol(f'x{i}{j}', real=True))
Mm = sp.Matrix(2, 2, lambda i, j: sp.Symbol(f'm{i}{j}', real=True))
MX = Mm*Xm
frob2 = sum(MX[i, j]**2 for i in range(2) for j in range(2))
ok("R2 TRANSFER GROUND: tr(X^T (M^T M) X) = ||MX||_F^2 = sum of squares"
   " EXACT all-symbolic ==> A <= B implies tr(X^T A X) <= tr(X^T B X)"
   " (apply to B - A = M^T M) -- the b^{1/2}-conjugation step that carries"
   " the class mass through the crossing operator",
   sp.expand((Xm.T*(Mm.T*Mm)*Xm).trace() - frob2) == 0)

# ===== R3 -- crossing algebra (fresh exact instance) + class domination,
# boundary-tight =====
w1 = sp.Matrix([1, 2, 0, 2])/3          # unit
w2 = sp.Matrix([2, -1, 2, 0])/3         # unit, orthogonal to w1
P4 = w1*w1.T + w2*w2.T                  # rank-2 exact projection
C4 = sp.diag(1, 1, 0, 0)                # exact projection
I4 = sp.eye(4)
T4 = C4*P4*C4
ok("R3a CROSSING ALGEBRA (fresh rank-2 exact instance, distinct from the"
   " sealed pair's): T - T^2 = C P C^perp P C = Y Y^dag for projections"
   " P, C -- pure P^2 = P, C^2 = C algebra",
   sp.simplify(T4 - T4*T4 - C4*P4*(I4 - C4)*P4*C4) == sp.zeros(4, 4)
   and sp.simplify(P4*P4 - P4) == sp.zeros(4, 4))
Td = sp.diag(R(1,2), R(3,8), R(1,8))    # spectral exhibit
Ed = sp.diag(1, 1, 0)                   # window eps = 1/8 keeps 1/2, 3/8
ceps = 1/(R(1,4) - R(1,64))             # = 64/15
D3 = ceps*(Td - Td*Td) - Ed
ok("R3b CLASS DOMINATION E <= (1/4-eps^2)^{-1}(T - T^2) as PSD operators,"
   " boundary-TIGHT at |s-1/2| = eps (spectral exhibit eps = 1/8: gaps"
   " 1/15, 0, 7/15, all >= 0, middle exactly 0; the general case is R1 +"
   " the spectral theorem, displayed in text)",
   all(D3[i, i] >= 0 for i in range(3)) and D3[1, 1] == 0
   and sp.simplify(ceps - R(64, 15)) == 0
   and [D3[0, 0], D3[2, 2]] == [R(1, 15), R(7, 15)])

# ===== R4 -- the clock as commutator mass, same fresh instance =====
ok("R4 CLOCK = COMMUTATOR MASS: ||[P,C]||_2^2 = 2 tr(CPC - (CPC)^2)"
   " = 2 tr(C P C^perp P C) = kappa_n at projection grade (exact instance;"
   " general proof by cyclicity displayed in text) -- the clock-ceiling"
   " decider object in its natural form",
   sp.simplify(((P4*C4 - C4*P4).T*(P4*C4 - C4*P4)).trace()
               - 2*(T4 - T4*T4).trace()) == 0)

# ===== R5 -- the profile ceiling b_D <= 1 at the PA bytes =====
u = sp.Symbol('u', nonnegative=True)    # u = |x|^2
sig = (s**2 - u)*((1 - s)**2 - u)
dsig = sp.expand(sp.diff(sig, u) + (s**2 - u) + ((1 - s)**2 - u))
smax = sp.solve(sp.diff(s*(1 - s), s), s)
ok("R5 PROFILE CEILING b_D <= 1: d(sigma)/d|x|^2 = -[(s^2-|x|^2) +"
   " ((1-s)^2-|x|^2)] < 0 on the open diamond (sigma maximal at x = 0);"
   " max_s s(1-s) = 1/4 at s = 1/2 exactly; so sigma <= 1/16,"
   " 16 - 1/sigma <= 0, b_D = e^{16-1/sigma} <= e^0 = 1, equality only at"
   " (s, x) = (1/2, 0) -- the ||b_D(s)||_op <= 1 spectator of the transfer",
   dsig == 0 and smax == [R(1, 2)]
   and sp.simplify((R(1, 2)*(1 - R(1, 2)))**2 - R(1, 16)) == 0
   and sp.exp(16 - 16) == 1)

# ===== R6 -- the fraction ceiling assembly and the clock trichotomy =====
kap, cG, CG, n, g, Cc = sp.symbols('kappa c_G C_G n gamma C', positive=True)
ep = sp.Symbol('epsilon_0', positive=True)   # eps in (0,1/2): 1-4eps^2 > 0
Frac = 2*kap/((1 - 4*ep**2)*cG*n**R(3, 2))
ok("R6 FRACTION CEILING + TRICHOTOMY: F_n(eps) <= 2 kappa_n/((1-4 eps^2)"
   " c_G n^{3/2}) (and the count twin tr E <= 2 kappa_n/(1-4 eps^2));"
   " regimes EXACT: kappa = C n^{3/2-gamma} ==> ceiling -> 0 (DECIDES"
   " o(1) with rate n^{-gamma}); kappa = C n^{3/2} ==> ceiling n-free"
   " (undecided by the ceiling); kappa at the sealed D4 ceiling 2n^3 ==>"
   " ceiling = 4 n^{3/2}/((1-4 eps^2) c_G), VACUOUS at exact power 3/2",
   sp.limit(Frac.subs(kap, Cc*n**(R(3, 2) - g)), n, sp.oo) == 0
   and sp.simplify(sp.diff(Frac.subs(kap, Cc*n**R(3, 2)), n)) == 0
   and sp.simplify(Frac.subs(kap, 2*n**3)
                   - 4*n**R(3, 2)/((1 - 4*ep**2)*cG)) == 0)

# ===== R7 -- the far-class geometry: the residual's o(1) answer alone
# cannot close MO-4 at the linear clock =====
Keps, Cst, eN = sp.symbols('K C_star epsilon_n', positive=True)
far = (Keps*CG*n**R(3, 2)/(2*eN))/(Cst*n/8)
ok("R7 FAR-CLASS GEOMETRY: |1-2s| = 2|s-1/2| identity, so the far-class"
   " resolvent norm is <= 1/(2 eps_n); far-class chain over the certified"
   " clock = (K C_G n^{3/2}/(2 eps_n))/(C_* n/8) = (4 K C_G/(C_* eps_n))"
   " sqrt(n) EXACT: even TOTAL near-class mass vanishing leaves sqrt(n)"
   " in the far class at the linear clock (eps_n <= 1/2 always) -- the"
   " fraction question is the localization HALF of MO-4-R, not the whole",
   sp.expand((1 - 2*s) - 2*(R(1, 2) - s)) == 0
   and sp.simplify(far - 4*Keps*CG*sp.sqrt(n)/(Cst*eN)) == 0)

# ===== R8 -- the witness pair: the displayed hypotheses do not determine
# the fraction (TOY-SEPARATED: refutes derivability only) =====
P2 = sp.Matrix([[R(1, 2), R(1, 2)], [R(1, 2), R(1, 2)]])
C2 = sp.diag(1, 0)
T2 = C2*P2*C2
YY2 = T2 - T2*T2
bA = sp.diag(0, 1)
bB = sp.diag(1, 0)
vcl = sp.Matrix([1, 0])
ok("R8 WITNESS PAIR: P, C exact projections, T = CPC = diag(1/2, 0) --"
   " exact crossing s = 1/2; YY^dag = diag(1/4, 0); clock kappa ="
   " 2 tr YY^dag = 1/2 in BOTH; profiles 0 <= b <= 1 multiplication in"
   " BOTH; class b-mass 0 under b_A = diag(0,1) vs 1 under b_B ="
   " diag(1,0); total profile-Gram mass tr b = 1 in BOTH: fraction 0 vs 1"
   " at IDENTICAL {projections, clock value, profile bounds} -- no"
   " identity-grade route from the displayed hypothesis class alone can"
   " decide THE QUESTION; a family-specific joint-localization datum is"
   " REQUIRED",
   sp.simplify(P2*P2 - P2) == sp.zeros(2, 2)
   and T2 == sp.diag(R(1, 2), 0) and YY2 == sp.diag(R(1, 4), 0)
   and 2*YY2.trace() == R(1, 2)
   and (vcl.T*bA*vcl)[0, 0] == 0 and (vcl.T*bB*vcl)[0, 0] == 1
   and bA.trace() == 1 and bB.trace() == 1)

# ===== R9 -- positivity ground of the X-bracket: X_n <= kappa_n/2 and no
# unconditional floor =====
Nm = sp.Matrix(2, 2, lambda i, j: sp.Symbol(f'n{i}{j}', real=True))
MN = Mm*Nm.T
ok("R9 X-BRACKET GROUND: tr((N^T N)(M^T M)) = ||M N^T||_F^2 >= 0"
   " all-symbolic EXACT ==> for PSD A and 0 <= b <= 1 (multiplication):"
   " 0 <= tr(A b) <= tr A (apply with M^T M = b and M^T M = 1-b); hence"
   " X_n := int_0^1 tr(Y Y^dag (b_D(s) x 1_4)) ds <= kappa_n/2, and NO"
   " positive floor for X_n/kappa_n exists without localization (R8's"
   " witness A realizes X-analog = 0 at clock 1/2)",
   sp.expand((Nm.T*Nm*(Mm.T*Mm)).trace()
             - sum(MN[i, j]**2 for i in range(2) for j in range(2))) == 0)

print("MO4R-BATTERY-DONE")
```

Output, verbatim (9/9 PASS):

```text
R1 WINDOW: s(1-s) = 1/4 - (s-1/2)^2 EXACT, so s(1-s) in [1/4-eps^2, 1/4] iff |s-1/2| <= eps; and on the window s(1-s) - (1/4-eps^2) = (eps-(s-1/2))(eps+(s-1/2)), a product of nonnegatives -- the window floor grounding E <= (1/4-eps^2)^{-1}(T - T^2): PASS
R2 TRANSFER GROUND: tr(X^T (M^T M) X) = ||MX||_F^2 = sum of squares EXACT all-symbolic ==> A <= B implies tr(X^T A X) <= tr(X^T B X) (apply to B - A = M^T M) -- the b^{1/2}-conjugation step that carries the class mass through the crossing operator: PASS
R3a CROSSING ALGEBRA (fresh rank-2 exact instance, distinct from the sealed pair's): T - T^2 = C P C^perp P C = Y Y^dag for projections P, C -- pure P^2 = P, C^2 = C algebra: PASS
R3b CLASS DOMINATION E <= (1/4-eps^2)^{-1}(T - T^2) as PSD operators, boundary-TIGHT at |s-1/2| = eps (spectral exhibit eps = 1/8: gaps 1/15, 0, 7/15, all >= 0, middle exactly 0; the general case is R1 + the spectral theorem, displayed in text): PASS
R4 CLOCK = COMMUTATOR MASS: ||[P,C]||_2^2 = 2 tr(CPC - (CPC)^2) = 2 tr(C P C^perp P C) = kappa_n at projection grade (exact instance; general proof by cyclicity displayed in text) -- the clock-ceiling decider object in its natural form: PASS
R5 PROFILE CEILING b_D <= 1: d(sigma)/d|x|^2 = -[(s^2-|x|^2) + ((1-s)^2-|x|^2)] < 0 on the open diamond (sigma maximal at x = 0); max_s s(1-s) = 1/4 at s = 1/2 exactly; so sigma <= 1/16, 16 - 1/sigma <= 0, b_D = e^{16-1/sigma} <= e^0 = 1, equality only at (s, x) = (1/2, 0) -- the ||b_D(s)||_op <= 1 spectator of the transfer: PASS
R6 FRACTION CEILING + TRICHOTOMY: F_n(eps) <= 2 kappa_n/((1-4 eps^2) c_G n^{3/2}) (and the count twin tr E <= 2 kappa_n/(1-4 eps^2)); regimes EXACT: kappa = C n^{3/2-gamma} ==> ceiling -> 0 (DECIDES o(1) with rate n^{-gamma}); kappa = C n^{3/2} ==> ceiling n-free (undecided by the ceiling); kappa at the sealed D4 ceiling 2n^3 ==> ceiling = 4 n^{3/2}/((1-4 eps^2) c_G), VACUOUS at exact power 3/2: PASS
R7 FAR-CLASS GEOMETRY: |1-2s| = 2|s-1/2| identity, so the far-class resolvent norm is <= 1/(2 eps_n); far-class chain over the certified clock = (K C_G n^{3/2}/(2 eps_n))/(C_* n/8) = (4 K C_G/(C_* eps_n)) sqrt(n) EXACT: even TOTAL near-class mass vanishing leaves sqrt(n) in the far class at the linear clock (eps_n <= 1/2 always) -- the fraction question is the localization HALF of MO-4-R, not the whole: PASS
R8 WITNESS PAIR: P, C exact projections, T = CPC = diag(1/2, 0) -- exact crossing s = 1/2; YY^dag = diag(1/4, 0); clock kappa = 2 tr YY^dag = 1/2 in BOTH; profiles 0 <= b <= 1 multiplication in BOTH; class b-mass 0 under b_A = diag(0,1) vs 1 under b_B = diag(1,0); total profile-Gram mass tr b = 1 in BOTH: fraction 0 vs 1 at IDENTICAL {projections, clock value, profile bounds} -- no identity-grade route from the displayed hypothesis class alone can decide THE QUESTION; a family-specific joint-localization datum is REQUIRED: PASS
R9 X-BRACKET GROUND: tr((N^T N)(M^T M)) = ||M N^T||_F^2 >= 0 all-symbolic EXACT ==> for PSD A and 0 <= b <= 1 (multiplication): 0 <= tr(A b) <= tr A (apply with M^T M = b and M^T M = 1-b); hence X_n := int_0^1 tr(Y Y^dag (b_D(s) x 1_4)) ds <= kappa_n/2, and NO positive floor for X_n/kappa_n exists without localization (R8's witness A realizes X-analog = 0 at clock 1/2): PASS
MO4R-BATTERY-DONE
```

---

## 10. CHOICE LEDGER (every unforced choice, classified; commission T3SR)

```text
CH-1 WINDOW CONVENTION (eps-parametrized family, fixed and shrinking
     both covered): IMMATERIAL(derived) — every display is
     eps-explicit; the verdict is window-uniform.
CH-2 DENOMINATOR PINNED AT THE OF-RECORD G_n (the residue's own
     naming): FORCED. The C_n-restricted alternative int tr(C_n b~ C_n)
     ds is noted and consumed NOWHERE (it has no certified floor of
     record; comparing it to G_n needs the carrier-subprojection
     reading of CH-8, CONDITIONAL and unused).
CH-3 SEAL-VERIFY-BEFORE-CONSUME EXTENDED TO SWEEP MATCH-READS (7
     additional seals verified): FORCED by the commission's
     verify-every-input-seal clause.
CH-4 D4/RANK BYTES CONSUMED AT r-3's AUDITED DISPLAY (N = 4n^3;
     kappa_n <= 2n^3): lawful (named in the ground's seal table;
     seal-verified at path this session); corroborates T-G1's quotes;
     blast radius: RT-A and the vacuity display only.
CH-5 WITNESS-PAIR SHAPE (2x2 minimal): IMMATERIAL(derived) — any pair
     with crossing mass on/off the profile support works; minimality is
     display economy.
CH-6 THE ANTICIPATED O-1 SHAPE (kappa_n ~ n polylog): marked
     ANTICIPATION, grounded in the sealed surface diagnosis (Lambda^2),
     consumed nowhere; only the gamma > 0 form is the decider.
CH-7 FRESH CAS INSTANCES (distinct from the sealed pair's and the
     audit's): independence hygiene; IMMATERIAL(derived).
CHAIN CHOICE AUDIT: no unforced choice enters the verdict chain. T-1..
     T-4 are algebra plus sealed floors; §5's witnesses are
     derivability refutations; the verdict survives any alternative at
     CH-1..CH-7 unchanged.
MACHINERY/RELEVANCE: classical operator theory (spectral calculus,
     PSD-order conjugation, trace positivity) applied to SEALED
     constructions; identity cores CAS-pinned; SURFACE-DERIVED, not
     surface-native.
```

---

## 11. TOY_SEPARATION (self-assessment)

```text
CLAIMED CLEAN at the stated quantifiers. R1/R2/R5/R6/R7/R9 are
all-parameter identity/inequality exhibits with universal quantifiers
in the check names. The exact-rational INSTANCES (R3a's rank-2
projections; R3b's spectral exhibit; R4's commutator instance) are
identity-grade exhibits of displayed general facts whose general proofs
are displayed in text (spectral theorem + R1; cyclicity). The WITNESS
PAIR (R8) is used ONLY against derivability-from-displayed-hypotheses
claims, which a single exact countermodel per direction lawfully
refutes; it asserts NOTHING about the record family's own fraction
(§5 TOY STATUS), which stays undecided of record. No model family is a
premise; no spectral datum of the actual family is valued; kappa_n,
rho_n, eps_*, ell, c_G, C_G, C_*, K(eps_*), C-dag, gamma, c', c'', m_0,
all thresholds stay symbols. The RULING is the checker's/audit's, not
this artifact's.
```

---

## 12. FLAG BLOCK

```text
MO4R_GRAM_MASS = UNDECIDABLE-TODAY( THE QUESTION — does the near-1/4
  eigenvector class of Y_n Y_n^dag carry an o(1) fraction of the
  b_D-bulk Gram mass — is not decidable on the sealed stock at the
  cutoff, and the undecidability is FORCED at the displayed-hypothesis
  grade (the R8 witness pair: identical projections, clock, and profile
  bounds realize fraction 0 AND fraction 1). Blockers exact: o(1) is
  blocked SOLELY by the absent sub-3/2 clock ceiling (D4's 2n^3
  vacuous at exact power 3/2; D9 no-upper-rate re-confirmed; sw-2 no
  carrier); NOT-o(1) is blocked by the absent quantified 1/2-approach/
  localization law (r-3 :469/:808; s-6; sw-3 no carrier). )
REDUCTION_DERIVED = T-1..T-4( the Gram transfer, attempted first as
  commissioned, DELIVERS: E_n(eps) <= (1/4 - eps^2)^{-1} Y_n Y_n^dag
  (PSD, boundary-tight); mass_n(eps) <= (1/4 - eps^2)^{-1} X_n; X_n :=
  int_0^1 tr(Y_n Y_n^dag (b_D(s) tensor 1_4)) ds <= kappa_n/2; count
  twin tr E_n(eps) <= 2 kappa_n/(1 - 4 eps^2); FRACTION CEILING
  F_n(eps) <= 2 kappa_n/((1 - 4 eps^2) c_G n^{3/2}) [given CL-A via the
  sealed G_n floor]: the o(1) side of THE QUESTION is REDUCED to the
  clock's upper exponent; any certified kappa_n <= C n^{3/2 - gamma}
  decides it at rate n^{-gamma} with no further work. )
NEW_STRUCTURE = TWO( R_n = (1 - 2 T_n)^{-1} on ran C_n — the resolvent
  is functional calculus of T_n and commutes with the class (makes the
  near/far split exact); kappa_n = ||[P, C_n]||_2^2 — the clock in
  commutator form, the O-1 object's natural shape. )
SCOPE = FRACTION-IS-HALF( R7: the far-class chain over the certified
  linear clock is EXACTLY (4 K C_G/(C_* eps_n)) sqrt(n) — even F_n
  identically 0 cannot close MO-4 at the linear clock; the fraction is
  the localization HALF of MO-4-R, the clock exponent the other half;
  consistent with the sealed tightening. )
DECIDER_OBJECTS = TWO+TRICHOTOMY( O-1 THE CLOCK CEILING (ceiling twin
  of MO-2): certified kappa_n <= C-dag n^{3/2 - gamma}, gamma > 0 —
  consumes r-2's C_n realization bytes + CL-A-discipline classical
  ground; yields DECIDED-o(1) at rate n^{-gamma} through today's T-4.
  O-2 THE LOCALIZATION PACKAGE: class-count floor >= c' n^{3/2} at a
  fixed window PLUS per-vector b_D-mass floor m_0 on a c''-fraction of
  the class; yields DECIDED-NOT-o(1) at floor c'' c' m_0 / C_G.
  Trichotomy in the clock's true upper exponent alpha-k: < 3/2 the
  ceiling decides; = 3/2 the ceiling saturates n-free and localization
  alone decides; > 3/2 the ceiling is vacuous and O-2(ii) is still
  required. In every regime a NEW family-specific sealed object is
  required; none exists at the cutoff. Commissioning is the
  registrar's call. )
CONSUMPTION_BOUNDARY = NOTHING-FIRED( MO-4 NOT closed; MO-4-R NOT
  discharged — REDUCED and stands; r-3, R-L4b, F-d, all witnesses of
  the sealed pair untouched; no flag of any prior artifact flips; H-R
  never defaulted (rho_n appears in no display; the far-class bound is
  spectral); the registrar consumes. )
SEALS_VERIFIED = 9/9( ground pair 0e894372 + bfd86217 read in full;
  sweep-consumed T-S1..T-S7 seal-verified at path before any
  match-level reliance; "Q-..." tokens EXPECTED-UNLOCATABLE, none
  chased. )
SWEEP_CUTOFF = 2026-08-15 02:57:40 CDT( keys and findings §7; MO-4-R
  and T3SR unoccupied; no sub-3/2 clock-ceiling carrier; no
  localization-law carrier; cleanroom root zero hits; post-audit lanes
  touch no residue key; one out-of-root supervision filename noted,
  unopened. )
FORBIDDEN_IMPORTS = none( exact symbolic only; no floats as ground; no
  numeric evaluation; no measured constant; NO value frozen — every
  constant and threshold symbolic; symbolic scales only; no fenced-
  class file opened; no git action; no existing file edited; ONE file
  written plus its seal; output path probed ABSENT at session start
  and re-probed immediately before write. )
MACHINERY_INVOKED = yes(CAS) — sympy 1.14.0, fresh venv mo4rvenv under
  the session scratchpad; final battery ran ONCE, 9/9 PASS, script and
  output reproduced verbatim in §9; no pre-final corrections.
alpha_computed = false ; proof_authorized = false ;
kappa_record_computed = false
ALL_RESULTS = CLAIMED until checked.
MO4R_GRAM_MASS_RESULT = SEALED.
```
