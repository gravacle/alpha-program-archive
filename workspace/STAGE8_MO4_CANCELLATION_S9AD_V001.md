# STAGE 8 — MO-4 OF RECORD: THE PRODUCT-LEVEL CONTROL OF ||R_n Delta_n(a)||_1 — THE PROFILE-SPLIT GRAM FACTORIZATION, THE CROSSING IDENTITY, AND THE EXACT RESIDUAL — S9AD V001

## BLIND BUILDER — CODENAME MO4-BUILD — COMMISSION S9AD — [CLAIMED]

Date: 2026-08-14 (session CDT 2026-08-14 late / UTC 2026-08-15)
Role: BLIND builder (MO4-BUILD). Commission: MO-4 of record — a
PRODUCT-LEVEL CANCELLATION IDENTITY controlling ||R_n Delta_n(a)||_1
DIRECTLY (not via the rank x op budget, proven dead at r-3 D10), attempted
exactly, route by route, with the NEW sealed structure the original r-3
sweep (bebc0f08 s-6) did not have: the chiral involution (MO-2), the exact
delta + CZ jet of Delta with closed-form coefficients (MO-3, p = -3), the
n-free polydisc operator bound c(eps_*) (r-3 P-2), the parity/monodromy
structure (K-channel d66a922c; WB4 splitting 80db260f). Target as
commissioned: with MO-2, ||R_n Delta_n(a)||_1 = o(kappa_n) uniformly on
the closed pair polydisc closes r-3 directly. "Q-..." tokens inside sealed
artifacts are EXPECTED-UNLOCATABLE by design; noted, never chased.

Gates: `alpha_computed = false` ; `proof_authorized = false` ;
`kappa_record_computed = false`. ALL_RESULTS = CLAIMED until checked.

Fences held: EXACT SYMBOLIC DERIVATION ONLY — one CAS battery (sympy
1.14.0, fresh venv `mo4venv` under the session scratchpad), reproduced
verbatim in §7 (14/14 PASS on the final run; ONE pre-final check-form
correction disclosed in §7's header: check V4's expected instance value
was mis-transcribed as 12 where the exact value is 17 (<= 18); the
displayed constant was corrected — no derivation step changed); every
constant symbolic or an exact rational/closed form (pi, surds, e^{16 -
65536/1089}); NOTHING numeric evaluated; no floats as ground; no measured
constant; NO value frozen (every conclusion is an inequality with symbolic
constants, an exponent statement, or a named refusal; eps_*, ell, C_G,
c_G, K(eps_*), M_{K0}, C_*, rho_n = ||R_n||_op all symbols); M(t)/1_{D_t}
sharp (D6'); the stricken display (E1 :773-778) consumed NOWHERE; no file
matching register|road_|ledger|lens|plan|tracker|THE_HANDOFF opened; no
git action; no existing file edited; ONE output (this artifact) plus its
seal sidecar at the commission-distinct path, probed ABSENT at session
start AND re-probed immediately before write. Every enumeration sentence
claims only its own displayed sweep. H-R NOWHERE defaulted: rho_n stays an
uncontrolled symbol in every display. Marks: DERIVED / CLAIMED /
CLASSICAL(cited) / CONDITIONAL(premise named) span by span.

SWEEP CUTOFF, DECLARED: the corpus sweep of §5 was executed against the
workspace/supervision state as of **2026-08-14 23:55:31 CDT**; artifacts
sealed after that instant are not consumed and not swept. Parallel S9AD
lanes checked at the cutoff for MO-4 occupation: NONE claims it
(REFUTING_BRANCH §5: "MO-4 ... UNTOUCHED AS A NAMED ABSENCE"; the wall:
"MO-4's absence re-confirmed by the splitting sweep"; the MO2/MO3 lanes
occupy MO-2/MO-3 only).

---

## 0. VERDICT IN ONE LINE

**PARTIAL — a product-level identity controlling ||R_n Delta_n(a)||_1
directly DOES exist and is DERIVED here (the first in the corpus; the r-3
s-6 absence ends), but it delivers the commissioned o(kappa_n) only up to
ONE exactly-named residual factor. THE IDENTITY (the profile-split Gram
factorization): the sealed coupling J_n(s) = -(Q_n b_D(s) Q_n) tensor
alpha_x factors EXACTLY through the positive profile's square root,
J_n(s) = -[(Q_n b_D^{1/2}) tensor 1_4][(b_D^{1/2} Q_n) tensor alpha_x],
so the sealed Duhamel expansion of Delta_n(a) = C_n(V(a) - V(0))C_n splits
every term into TWO Hilbert–Schmidt halves whose Gram mass is the
profile-weighted carrier diagonal G_n := 4 int_0^1 int b_D(s,x) K3(x,x)
dx ds — and CL-A (the SAME classical ground MO-2 consumed, here used for
the diagonal CEILING as MO-2 used it for the floor) certifies G_n
TWO-SIDEDLY: c_G n^{3/2} <= G_n <= C_G n^{3/2} (n >= thresholds; all
constants symbolic). Consequences, exact: (i) ||Delta_n(a)||_1 <=
K(eps_*) G_n <= K C_G n^{3/2} uniformly on the closed pair polydisc,
K(eps_*) = eps_*(e^{2 eps_*} + e^{eps_*}) — a certified SUB-VOLUME
trace-norm rate, n^{3/2} against the refuted rank budget 4n^3: THE r-3
MISSING OBJECT MO-3 IS SUPPLIED AS A COROLLARY, by a route MO3-BUILD's
negative verdict explicitly left open (not through coincidence vanishing —
through the jet's derived unit-ball support monetized against the
carrier's UV density); (ii) ||Delta_n(a)||_2 <= sqrt(c(eps_*) K C_G)
n^{3/4} — the first certified HS upper rate, refining the of-record
divergence-without-rate and correcting the "carrier-volume" paraphrase to
the ball-bulk count; hence the P-5 necessary condition ||Delta_n||_2 =
o(kappa_n) is SATISFIED at the certified clocks (n^{3/4} = o(n)): MO-4 is
NOT refutable through the P-5 floor — the race is genuinely open; (iii)
with the resolvent, ||R_n Delta_n(a)||_1 <= K(eps_*) rho_n G_n, rho_n =
||R_n||_op, and the certified-clock ratio is EXACTLY (8 K C_G / C_*)
rho_n sqrt(n) (CAS V13): the commissioned o(kappa_n) follows IFF the
residual rho_n sqrt(n)-type factor falls, and the budget itself cannot be
improved in n (G_n's floor is certified: the split is SHARP). THE
RESIDUAL, NAMED EXACTLY (MO-4-R): the resolvent-weighted profile Gram
mass W_n(s; a) := ||(b_D(s)^{1/2} Q_n tensor 1_4) u(0; s, 1)-chain C_n
R_n||_2^2 with closing condition sup_polydisc int_0^1 sqrt(W_n(s; a) ·
4 g_n(s)) ds = o(kappa_n); the crossing identity derived here — (1 +
A_n(0))^2 = 1 - 4 Y_n Y_n^dag on ran C_n with Y_n = C_n P C_n^perp, tr
Y_n Y_n^dag = kappa_n / 2, hence R_n = (1 + A_n(0)) (1 - 4 Y_n
Y_n^dag)^{-1} (CAS V5/V6) — localizes ALL resolvent blow-up in the SAME
operator that carries the clock's mass: MO-4-R asks whether the near-1/4
eigenvectors of Y_n Y_n^dag carry an o(1) fraction of the b_D-bulk Gram
mass. UNDECIDED both directions; the structural diagnosis is exact: G_n
counts the momentum-ball BULK (Lambda^3, Lambda = sqrt(2n)/ell), the
certified clock counts the crossing-SURFACE class (Lambda^2) — the whole
remaining race is one power of Lambda = sqrt(n) plus the unquantified
resolvent weight. Every corpus-named cancellation mechanism is
individually REFUSED at an exact display: the chiral involution EXITS ran
C_n (block exchange, never returns to the product's block); spatial
parity maps a -> -a (norm symmetry, CAS V7/V8); the jet's k_hat_x-oddness
kills traces, never trace norms (unitary invariance, V8); support
separation between the jet and the ball-surface near-kernel FAILS (MO-3's
ray witness is strictly positive at |x| = r; b_D's all-orders vanishing
meets the frame surface only on the measure-zero slice s = t); WB4-type
splittings are trace-grade and norm-inflating at trace-norm grade (the
wall's own F1/F2). Nothing fires: r-3 is NOT discharged (the residual
stands), R-L4b is NOT discharged, F-d is NOT exhibited, no flag flips,
all three R-L4 witnesses STAND; the registrar consumes. CAS battery
14/14 PASS.**

---

## 1. SEALS VERIFIED AT PATH (shasum -a 256), BEFORE ANY RELIANCE

All under `/Users/bgm/MB Work/alpha-program-archive/workspace/`. Every
digest recomputed from bytes at path THIS session by FULL digest and
matched against its `.seal.sha256` sidecar (and the commission's pinned
prefixes bebc0f08, 72c95d42, 6997ff61, 9fdc3d1c, d66a922c, 80db260f
reproduced exactly). 9/9 MATCH.

```text
G-1  bebc0f085d10082e1229e2638637e12681687356daf86fbe652179514230c6a9
     STAGE8_R3_JOINT_RATE_S9AD_V001.md            MATCH (sidecar, tasked)
     — THE FRAME at bytes (§2.1); FRAME-N1/N2/N3; K-2..K-5 (the Duhamel
     operator identity, the propagator bounds ||u(0;1,s)|| = 1,
     ||u(a;s,0)|| <= e^{|Im a| C_b} <= e^{eps_*}, c(eps_*)); P-5
     (||R_n Delta||_1 >= ||Delta||_2, D3); D10 (rank x op dead); the MO
     list (:807-815); sweep s-6 (no cancellation identity in the corpus);
     F-2 note (the "carrier volume" phrase is a PARAPHRASE, check n-3);
     read in full.
G-2  72c95d42308921ad7e64bb9fee127752cb7256ff8b8c9f57949d508636d4c407
     STAGE8_R3_JOINT_RATE_S9AD_AUDIT_V001.md      MATCH (sidecar, tasked)
     — CONFIRMED-WITH-CORRECTIONS, cosmetic: r-3 consumable at audited
     grade; blocker list (incl. MO-4) GENUINE.
G-3  6997ff617ae746ab335c6728da7440baf29ae77ee591b55adc89a91739c60117
     STAGE8_MO2_KAPPA_RATE_S9AD_V001.md           MATCH (sidecar, tasked)
     — MO-2 DERIVED: kappa_n >= C_* n / 8 for n >= N_0 (C_* = r^2 L /
     (8 pi^3 ell^2), symbolic); the chiral involution FACT TWO (beta C_n
     beta = Q_n - C_n - W_n, rank W_n <= 4); CL-A cited classical
     (Plancherel–Rotach fixed-compact) with the sealed FIXED-COMPACT
     diagonal floor "for each fixed compact and any theta in (0,1) there
     is n_1 with k_n(t,t) >= theta sqrt(2n)/pi there; take theta = 1/2";
     k_n^ell(x,x) = (1/ell) k_n(x/ell, x/ell) exact scaling; X-3 (the
     rank-budget/clock gap n^2); read in full.
G-4  baab38c242529e0c6a0d9d14c172f6edc048cb563b6c47bcfb0f8a0ebfc4c79c
     STAGE8_MO2_KAPPA_RATE_S9AD_AUDIT_V001.md     MATCH (sidecar) — MO-2
     consumable at audited grade.
G-5  9fdc3d1c4d3e450db3245c8401a15c6eeafbfddd824479a5c29183444c1447e3
     STAGE8_MO3_P_EXPONENT_S9AD_V001.md           MATCH (sidecar, tasked)
     — p = -3; the delta + CZ jet with closed coefficients; the ray
     witness (beta_s > 0 at every 0 < |x| < 1; support exactly
     0 < |x| < 1); b_D bytes (= exp(16 - 1/s), s = s_- s_+, support the
     open diamond {|x| < min(t, 1-t)}); V_{mu lambda}(a) =
     u_mu(a_-)^dag u_lambda(a_+); J(t) = -(Q b_D(t,x) Q) tensor alpha_x;
     "MO-3 as a NAMED OBJECT remains open only through routes that do not
     pass through coincidence vanishing"; read in full.
G-6  549362d460416b5ebbad3b42b8758c858d905693cda72893eef4d6590f5234c2
     STAGE8_MO3_P_EXPONENT_S9AD_AUDIT_V001.md     MATCH (sidecar) — MO-3
     consumable at audited grade.
G-7  d66a922cfe023284890de8a335c38028efe94fb7a9d31b1f779bb0a0513b95cc
     STAGE8_K_CHANNEL_CONTROL_V001.md             MATCH (sidecar, tasked)
     — the insertion-parity splitting (K_H/K_A); the swap law DOUBLES odd
     strata (KB4); consumed as mechanism-typology corroboration only.
G-8  80db260fa1561d76296d5f54e1e52397b79009b8a0d12bc060c140818c38fdf7
     STAGE8_WALL_BOUNDARY_CLOSURE_S9AD_V001.md    MATCH (sidecar, tasked)
     — WB4 (the exact closure trace splitting); WB5 (odd content
     DOUBLED); F1 (rank x op stop = MO-3); F2 (boundary-supported assets
     never reach the diagonal locus); WB8 (the poisoning ceiling
     ||R_n||_op <= exp(-log|det_n(0)|), displayed to close the R_n
     detour); "MO-4's absence re-confirmed by the splitting sweep".
G-9  48ecdabeeee132a08c7a6c8b06f505ac1eca3619c19ad2e3684a3cd7bebe31d1
     STAGE8_REFUTING_BRANCH_S9AD_V001.md          MATCH (sidecar) — §5:
     MO-4 unoccupied of record ("UNTOUCHED AS A NAMED ABSENCE"); the
     MO-2+MO-4 package "the only sealed r-3 closure package whose route
     content is entirely unclipped by p = -3"; consumed as occupation and
     framing evidence only.
```

CONSUMPTION THROUGH SEALED QUOTES: 52f2490b (LINK 1/LINK 2, the per-pair
HS divergence), E1 displays, and PA bytes enter ONLY through the sealed
and audited quoting artifacts G-1/G-3/G-5 at their audited grade — no
additional file opened for them (ledger CH-2). EXPECTED-UNLOCATABLE
tokens this session: "Q-1054", "Q-1059", "Q-1062" (register pointers
inside sealed artifacts) — noted per standing design; not chased.

---

## 2. THE COMMISSIONED QUESTION AND THE OBJECTS, AT BYTES

```text
FRAME (G-1 §2.1): det(1 + A_n(a)) = det(1 + A_n(0)) det(1 + R_n
  Delta_n(a)), R_n = (1 + A_n(0))^{-1} on ran C_n, per-member conditional
  (invertibility where no s_i = 1/2). Delta_n(a) = C_n(V(a) - V(0))C_n.
  1 + A_n(0) = 1 - 2 C_n P C_n = C_n S C_n |_{ran C_n} with S := 1 - 2P
  = P^perp - P a UNITARY INVOLUTION (S^2 = 1, S = S^dag) — the baseline
  is the compression of an involution; this observation powers §4.5.
TARGET (commission): ||R_n Delta_n(a)||_1 = o(kappa_n) uniformly on the
  closed pair polydisc (max(|a_+|, |a_-|) <= eps_*), which with r-2's
  chain -log|det_n(0)| >= kappa_n closes r-3; MO-2 now clocks kappa_n >=
  C_* n / 8 (G-3).
DEAD OF RECORD: the rank x op budget (r-3 D10: 4n^3 c(eps_*) vs the
  ceiling 2n^3, ratio n-free); the bounded-numerator shortcut (r-3 P-5:
  ||R_n Delta||_1 >= ||Delta||_2, sup_n = +infinity per pair).
NEW SEALED STRUCTURE AVAILABLE TO THIS ATTEMPT (not available to the r-3
  sweep): the chiral involution beta (G-3 FACT TWO); the exact jet of
  Delta's kernel — contact + CZ at degree -3, coefficients the null-ray
  averages beta_s(x, k_hat) of b_D, SUPPORT derived exactly 0 < |x| < 1
  (G-5); the parity/insertion-parity structure (G-7/G-8); c(eps_*) and
  the sealed Duhamel operator identity (G-1 K-5).
```

---

## 3. THE CANCELLATION ROUTES OF THE COMMISSION, ATTEMPTED EXACTLY — FOUR REFUSALS, EACH AT ITS OWN DISPLAY

### 3.1 Route A — the chiral involution on the product: EXITS THE BLOCK (refused)

beta conjugation sends C_n to Q_n - C_n - W_n (G-3 FACT TWO, rank W_n <=
4): it maps ran C_n onto (essentially) its orthogonal complement within
ran Q_n. R_n is defined ONLY on ran C_n; beta (R_n Delta_n(a)) beta is an
operator on the OTHER block, where the frame supplies no resolvent and no
determinant. The involution therefore acts on the product as a
block-EXCHANGE, never as a within-block symmetry: there is no
beta-invariant decomposition of R_n Delta_n(a) in which contributions can
pair and cancel. Its one product-relevant consequence is spectral and
cross-block ({s_i on ran C_n} matches {1 - s_i on the complement} up to
rank <= 4 — unitary conjugation of C_n P C_n), which constrains NEITHER
factor of the product on its own block. What beta DOES supply downstream
is the clock kappa_n >= C_* n/8 (G-3), consumed in §4.6. REFUSED as a
cancellation source; the exit is exact. [DERIVED at the sealed displays;
CAS V7 pins the matrix bytes.]

### 3.2 Route B — the exact parity grading: A NORM SYMMETRY, NEVER A DECAY (refused)

The spatial parity Pi := beta compose (x -> -x) satisfies, at the sealed
bytes: Pi h_0 Pi = h_0 (both p_j and alpha_j flip sign — V7); Pi Q_n Pi
= Q_n (Hermite parity); Pi P Pi = P (ball symmetric); hence Pi C_n Pi =
C_n and Pi R_n Pi = R_n. And Pi (a J) Pi = -a J (b_D even in x; beta
alpha_x beta = -alpha_x, V7). Conjugating the propagator: Pi u(a) Pi =
u(-a), so

```text
  Pi Delta_n(a) Pi = Delta_n(-a),  Pi (R_n Delta_n(a)) Pi = R_n Delta_n(-a),
  ||R_n Delta_n(a)||_1 = ||R_n Delta_n(-a)||_1     (unitary invariance, V8).
```

The polydisc is symmetric under a -> -a: the parity grading is an exact
SYMMETRY of the quantity to be bounded and cancels nothing. The same
typology of record: the K-channel swap law and WB5 show insertion parity
DOUBLING odd strata in single composites rather than killing them
(G-7/G-8) — graded structure grades; it does not kill. REFUSED. [DERIVED;
CAS V7/V8.]

### 3.3 Route C — the delta + CZ jet against the near-kernel of 1 + A_n(0): BOTH SUB-MECHANISMS FAIL (refused)

(i) SUPPORT SEPARATION. The blow-up directions of R_n are the near-1/2
spectral directions of C_n P C_n — the ball-surface crossing class (the
locus where MO-2's own mass accumulates, G-3 X-4). A cancellation would
need Delta_n(a)'s amplitude to vanish there. It does not: MO-3's ray
witness (G-5 §3.5) certifies beta_s(x, k_hat) > 0 on an open set of
directions at EVERY 0 < |x| < 1 — including |x| = r(t), since 0 < r(t)
<= 1/2 < 1. The only all-orders vanishing the coupling owns — b_D(s, .)
vanishes to all orders at |x| = min(s, 1-s) — coincides with the frame's
ball surface |x| = r(t) ONLY on the measure-zero cell-time slice s = t
inside the Duhamel integral: no uniform separation exists. REFUSED, with
the failure locus displayed.
(ii) ODDNESS. The jet's leading amplitude carries k_hat_x [(beta_+ -
beta_-) I + (beta_+ + beta_-) alpha.k_hat] — odd structure that kills
TRACES (the sealed S1 mechanism). Trace NORMS are unitarily invariant
functions of the singular values (V8): sign structure in the symbol is
norm-invisible; |a_0| is what the trace norm sees, and it is strictly
positive on an open phase-space set (G-5 §3.5). REFUSED — the same
grammar by which r-3 refused trace-level rescues.
WHAT THE JET DOES SUPPLY (constructive, not cancelling): its DERIVED
support — the coupling lives on the unit-ball bulk — is exactly the
structure the profile split of §4 monetizes. [DERIVED at the sealed
displays.]

### 3.4 Route D — WB4-type splittings and the K-channel identities: TRACE-GRADE ONLY (refused)

WB4 splits tr K_n EXACTLY into branch-asymmetry + boundary-commutator
terms; at TRACE-NORM grade any such splitting is consumed through the
triangle inequality and can only INFLATE ||.||_1. The wall's own verdict
locates its stops: F1 (rank x op — the same ceiling r-3 D10 proved dead)
and F2 (its decay assets are boundary-supported while the divergent locus
is the volume diagonal). The profile split of §4 is precisely the
diagonal-REACHING replacement: it does not attempt to kill the diagonal
mass; it COUNTS it, at the carrier's UV smearing, against b_D's support.
WB8's poisoning ceiling ||R_n||_op <= exp(-log|det_n(0)|) is displayed
and NEVER consumed as a bound here (it is exponentially poisoned — V14);
rho_n stays symbolic (H-R held). REFUSED as a cancellation source;
consumed as typology. [DERIVED at the sealed displays.]

---

## 4. THE DELIVERABLE — THE PROFILE-SPLIT GRAM FACTORIZATION (DERIVED), ITS COROLLARIES, AND THE EXACT RESIDUAL

### 4.1 The identity

The sealed coupling is J_n(s) = -(Q_n b_D(s) Q_n) tensor alpha_x (G-5 §2
bytes; G-1 K-3), with b_D >= 0 a multiplication profile. EXACTLY (V2,
associativity of multiplication; tensor bookkeeping):

```text
  J_n(s) = -[(Q_n b_D(s)^{1/2}) tensor 1_4] · [(b_D(s)^{1/2} Q_n) tensor alpha_x].
```

Every appearance of J in the sealed Duhamel structure of Delta_n(a)
therefore splits into two HS halves through the positive square root of
the profile. This is the product-level structure the commission asked
for: it controls ||R_n Delta_n(a)||_1 DIRECTLY, and the rank budget never
enters.

### 4.2 The trace chain (exact, polydisc-uniform)

By the sealed two-factor decomposition and the sealed Duhamel operator
identity (G-1 K-5; V1 pins the scalar shape):

```text
Delta_n(a) = C_n u_mu(a_-)^dag [u_lambda(a_+) - u_lambda(0)] C_n
           + C_n [u_mu(a_-) - u_mu(0)]^dag u_lambda(0) C_n,
u(a;1,0) - u(0;1,0) = -i a int_0^1 u(0;1,s) J_n(s) u(a;s,0) ds.
```

Insert §4.1 and apply the trace-Hoelder inequality |||A B|||_1 <=
||A||_2 ||B||_2 (classical, singular-value grade; its Cauchy–Schwarz core
and an exact-rational instance pinned at V3/V4) to each s-integrand, with
the sealed norm facts ||u(0;1,s)|| = 1 (unitary), ||u(a;s,0)||,
||u_mu(a_-)|| <= e^{eps_*} (G-1 K-5, adjoint-continuation closed of
record), ||C_n|| <= 1:

```text
  g_n(s)   := tr_spatial(Q_n^{sp} b_D(s) Q_n^{sp})
            = int b_D(s,x) K3(x,x) d^3x           (Gram mass unfold, V11),
  G_n      := 4 int_0^1 g_n(s) ds                  (spinor factor 4 exact),
  ||C_n u_mu(a_-)^dag u_lambda(0;1,s) (Q_n b^{1/2} tensor 1_4)||_2
            <= e^{eps_*} sqrt(4 g_n(s)),
  ||(b^{1/2} Q_n tensor alpha_x) u_lambda(a_+;s,0) C_n||_2
            <= sqrt(4 g_n(s)) e^{eps_*},
  ==> ||Delta_n(a)||_1 <= |a_+| e^{2 eps_*} G_n + |a_-| e^{eps_*} G_n
                       <= K(eps_*) G_n,   K(eps_*) := eps_*(e^{2 eps_*} + e^{eps_*}),
  and, prepending the resolvent to the left factor,
  ==> ||R_n Delta_n(a)||_1 <= K(eps_*) rho_n G_n,   rho_n := ||R_n||_op,
```

uniformly on the closed pair polydisc, per frame-defined member (V12
assembly). rho_n is NOT bounded (H-R held); it is carried as a symbol.
[DERIVED.]

### 4.3 The Gram mass, two-sided: G_n ≍ n^{3/2} (DERIVED given CL-A)

The profile's support is {|x| < min(s, 1-s)} ⊂ the ball of radius 1/2
(G-5 bytes), so only the carrier's diagonal density ON A FIXED COMPACT
enters — the bulk phase-space count, not the carrier volume.

```text
CEILING. CL-A (the SAME classical ground MO-2 consumed; commission-chain
  authorized there; everything used derived from its statement): on the
  fixed compact |t| <= 1/(2 ell), phi_k^2 <= A_k^2 (1 + e_k)^2 with
  A_k^2 = (2/pi)(2k)^{-1/2}; choose K_0 with e_k <= 1 for k >= K_0; the
  head is bounded by the symbolic constant M_{K0} := sum_{k<K0} sup
  phi_k^2; the tail by 4 (2/pi) sum_{k>=K0}^{n-1} (2k)^{-1/2} <=
  (8/pi) sqrt(2n) (integral test; V9 grounds). Hence k_n(t,t) <= M_{K0}
  + (8/pi) sqrt(2n) on the compact, and with the exact scaling k^ell(x,x)
  = (1/ell) k_n(x/ell, x/ell) and int int b_D <= pi/6 (support volume,
  b_D <= 1):
    G_n <= 4 (pi/6) ell^{-3} (M_{K0} + (8/pi) sqrt(2n))^3 <= C_G n^{3/2}
  for n >= n_c (C_G, n_c symbolic; nothing numeric).
FLOOR. On the exact-rational window s in [3/8, 5/8], |x_j| <= 1/16
  (|x|^2 <= 3/256): s_- >= 33/256 and s_+ >= 33/256, so b_D >= b_min :=
  e^{16 - 65536/1089} > 0 (V10, exact rationals; b_D monotone in s); and
  MO-2's SEALED fixed-compact diagonal floor at theta = 1/2 gives
  k_n^ell(x_j, x_j) >= sqrt(2n)/(2 pi ell) on the window for n >= n_1'.
  Window measure (1/4)(1/8)^3 = 1/2048:
    G_n >= 4 b_min (1/2048) (sqrt(2n)/(2 pi ell))^3 =: c_G n^{3/2},
  n >= n_1'. [Floor DERIVED given CL-A via MO-2's sealed display.]
CONSEQUENCE: G_n ≍ n^{3/2}. The profile-split budget is SHARP in n: no
  better n-power can come out of this split; any further gain must come
  from the resolvent-weighted factor (§4.5), not from a better budget.
```

### 4.4 Corollaries (each at its own grade)

```text
COR-1 (MO-3 SUPPLIED AS A COROLLARY). ||Delta_n(a)||_1 <= K(eps_*) C_G
  n^{3/2}, polydisc-uniform, n >= n_c — a certified SUB-VOLUME trace-norm
  rate (n^{3/2} against the refuted 4n^3 rank budget: factor n^{3/2}
  below the carrier volume). This is r-3's MO-3 as NAMED (:811-813),
  reached by a route MO3-BUILD's negative verdict explicitly left open
  ("routes that do not pass through coincidence vanishing", G-5 §5): the
  rate comes from the jet's derived SUPPORT (the b_D bulk) against the
  carrier's UV diagonal density, not from any coincidence vanishing —
  fully consistent with p = -3. Grade: DERIVED given CL-A; CLAIMED until
  checked; candidate input, the registrar consumes.
COR-2 (FIRST CERTIFIED HS UPPER RATE). ||Delta_n(a)||_2^2 <=
  ||Delta_n(a)||_op ||Delta_n(a)||_1 (V14) <= c(eps_*) K(eps_*) C_G
  n^{3/2}, so ||Delta_n(a)||_2 <= sqrt(c K C_G) n^{3/4}. Consistent with
  the of-record per-pair divergence (52f2490b via G-1: sup_n = +infinity
  — n^{3/4} -> infinity); it CORRECTS the informal "carrier-volume"
  reading to the ball-bulk count, exactly as the r-3 check's n-3 note
  anticipated (the phrase was a paraphrase, never a certified display).
COR-3 (THE P-5 GATE IS OPEN). r-3 P-5 makes ||Delta_n||_2 = o(kappa_n)
  NECESSARY for the commissioned target. At the certified clocks:
  n^{3/4} = o(n) (V13 limit) — the necessary condition HOLDS. MO-4 is
  NOT refutable through the P-5 floor on today's stock: the race is
  genuinely open, in both directions.
```

### 4.5 The crossing identity and the exact residual object (MO-4-R)

The baseline is the compression of the unitary involution S = 1 - 2P
(§2). Pure distributivity plus S^2 = 1, C_n^2 = C_n (V5):

```text
  (C_n S C_n)^2 = C_n - C_n S C_n^perp S C_n = C_n - 4 Y_n Y_n^dag,
  Y_n := C_n P C_n^perp,   tr Y_n Y_n^dag = kappa_n / 2   (r-3 §2.2),
  ==>  R_n = (1 + A_n(0)) (1 - 4 Y_n Y_n^dag)^{-1}  on ran C_n   (V6),
```

with ||1 + A_n(0)||_op <= 1: ALL resolvent blow-up sits in (1 - 4 Y_n
Y_n^dag)^{-1}, whose singular directions are the near-1/4 eigenvectors
of Y_n Y_n^dag — the SAME operator whose total mass is the clock. The
residual of the trace chain is then named exactly:

```text
MO-4-R (the resolvent-weighted profile Gram mass): W_n(s; a) :=
  ||(b_D(s)^{1/2} Q_n tensor 1_4) u_lambda(0; s, 1) u_mu(a_-) C_n R_n||_2^2
  (and the term-2 analog). EXACT SUFFICIENT CLOSING CONDITION:
    sup_polydisc [ int_0^1 sqrt(W_n(s; a) 4 g_n(s)) ds  + term-2 ] = o(kappa_n)
  ==> the commissioned MO-4 target holds and r-3 closes via MO-2.
  The crude ceiling W_n <= rho_n^2 4 g_n(s) e^{2 eps_*} recovers §4.2.
  MO-4-R asks: do the near-1/4 eigenvectors of Y_n Y_n^dag (the crossing
  class, ball-SURFACE mass kappa_n) carry an o(1) fraction of the
  b_D-BULK Gram mass? UNDECIDED in both directions on the sealed stock
  (no closed-form spectrum, r-3 F-3; no eigenvector localization theorem
  sealed anywhere — §5 sweep).
```

### 4.6 The certified-clock arithmetic (exact) and where the race now stands

```text
  ||R_n Delta_n(a)||_1 / kappa_n <= K(eps_*) rho_n G_n / (C_* n / 8)
                                  = (8 K C_G / C_*) rho_n sqrt(n)   (V13),
```

the n-powers cancelling to sqrt(n) EXACTLY. Consequences, displayed:
(i) even GRANTED MO-1 (rho_n bounded), the budget alone leaves the gap
sqrt(n) at the certified linear clock — r-3's package sentence
"MO-1+MO-2+MO-3 close Route 1" is TIGHTENED: with MO-3 realized at its
sharp budget n^{3/2}, the package closes only if additionally kappa_n
outgrows n^{3/2} (a strengthened MO-2', unsealed) or MO-4-R fires; (ii)
the improvement over the dead budgets is exact: r-3 D10's ratio was
n-free at 4n^3, MO-2 X-3's gap was n^2 — the profile split brings the
gap to sqrt(n); (iii) the structural diagnosis: G_n counts the momentum-
ball BULK (Lambda^3 at Lambda = sqrt(2n)/ell), the certified clock
counts the crossing-SURFACE class (Lambda^2): the entire remaining race
is ONE power of Lambda plus the resolvent weight; (iv) nothing here
bounds the race from below: no trace-norm FLOOR for R_n Delta_n(a) above
||Delta_n(a)||_2 is derived, so no refutation of the target is available
either. The determinant race of r-3 §4.6 now stands clocked on both
sides at the named grades: numerator <= K rho_n C_G n^{3/2} (new),
>= ||Delta_n(a)||_2 (of record, no lower rate); denominator >= C_* n / 8
(MO-2), no upper rate (r-3 D9).

---

## 5. THE SWEEP (exhaustive at this displayed sweep only; cutoff in header)

```text
ROOTS: /Users/bgm/MB Work/alpha-program-archive and /Users/bgm/MB Work/
alpha_supervision, recursive, minus the fenced name classes (register|
road_|ledger|lens|plan|tracker|THE_HANDOFF, case-insensitive).
KEYS RUN: "cancellation identity"; "R_n Delta"; "b_D^{1/2}"; "sqrt(b_D)";
"profile split"; "Gram factoriz"; "finite propagation"; "sub-volume";
"MO-4".
FINDINGS:
 s-1 NO product-level cancellation identity for R_n Delta_n(a) exists in
     either root prior to this artifact: the only "cancellation identity"
     carriers are the r-3 pair (the DEFINING absence, s-6), its audit,
     the linkage, and the refuting branch (which re-confirms the absence,
     §5 there). The absence of record ENDS with §4; nothing prior is
     contradicted (the sweeps claimed absence at their own cutoffs).
 s-2 NO b_D^{1/2} / profile-split / Gram-factorization carrier exists
     anywhere in either root: §4.1 is NEW input, nowhere sealed, and
     nothing sealed obstructs it (the only requirements are b_D >= 0 —
     PA bytes via G-5 — and associativity).
 s-3 "finite propagation" hits are the AXN lattice files — r-3's s-5
     already typed them as DIFFERENT OBJECTS (the lattice free-
     Hamiltonian); NOT consumed; the chain of §4 nowhere uses finite
     propagation speed.
 s-4 "sub-volume" carriers: the wall (F1 = the MO-3 shape, no rate), the
     FORM_TO_HS bridge (a realized sub-volume instance at the GENERATOR
     layer T_g — a different object at a different site; no conflict
     with COR-1, which is at the propagator-difference layer), MO-3
     (the named object), r-3/audit (the definition). None supplies a
     Delta_n(a) trace rate; COR-1 is the first.
 s-5 MO-4 occupation at the cutoff: NONE (G-9 §5 "UNTOUCHED AS A NAMED
     ABSENCE"; the wall's splitting sweep; the MO2/MO3 lanes disclaim).
 s-6 NO eigenvector-localization or 1/2-approach law for C_n P C_n
     exists in either root (re-confirming r-3 F-3/s-3): MO-4-R and MO-1
     are genuinely unsupplied of record.
```

Each sentence claims only this displayed sweep at the declared cutoff.

---

## 6. CONSISTENCY WITH THE SEALED STOCK — EVERY CONTACT POINT (exact, never numeric)

```text
X-1 vs r-3 P-2/K-5: §4.2 consumes K-5's displays verbatim (Duhamel
    operator identity; e^{eps_*} propagator bounds; c(eps_*)); COR-2's
    HS ceiling and P-2's op ceiling are compatible grades of one object.
X-2 vs r-3 P-5 and 52f2490b: the numerator still DIVERGES (>=
    ||Delta_n||_2, sup_n = +infinity per pair) — COR-2 caps the
    divergence at n^{3/4} without contradicting it (no sealed display
    ever gave a lower RATE). The bounded-numerator shortcut stays dead;
    COR-3 shows the P-5 floor does not kill the target either.
X-3 vs r-3 D10 and MO-2 X-3: both said the RANK budget cannot close
    (ratio n-free at the ceiling; gap n^2 at the clock). §4 does not
    revive the rank budget — it replaces it: the gap at the certified
    clocks is now sqrt(n) (V13). No sealed sentence is contradicted;
    D10's "any product-of-norms discharge REQUIRES a sub-volume
    trace-norm rate" is CONFIRMED — COR-1 is exactly that rate.
X-4 vs MO-3 (p = -3): no coincidence vanishing is used anywhere; the
    budget uses the jet's derived SUPPORT and the carrier's UV smearing —
    the mechanism MO-3's §8 itself describes ("on any fixed carrier the
    delta/CZ structure is smeared at the carrier's UV scale"). The
    sub-volume rate arrives through the door G-5 left open. p = -3
    stands untouched.
X-5 vs the wall (F1/F2) and the K-channel: F1's stop (rank x op) is gone
    AROUND by the split; F2's ruling (boundary assets never reach the
    diagonal) is RESPECTED — §4 counts the diagonal mass rather than
    killing it; WB8's poisoning ceiling is displayed and never consumed;
    the swap-law typology (odd strata double) is consistent with §3.2's
    refusal.
X-6 vs H-R / FRAME-N2: rho_n = ||R_n||_op is a symbol in every display;
    no default, no bound claimed; MO-1 remains open and REQUIRED for any
    budget-side closure.
X-7 vs r-2 / MO-2: the clock is consumed at its sealed quantifier
    (kappa_n >= C_* n/8 cofinitely, constants symbolic); §4.6's
    arithmetic weakens nothing; kappa_n's ceiling 2n^3 (r-3 D4) leaves
    o(kappa_n) undecided exactly as displayed — this artifact does not
    decide it.
X-8 THE STRICKEN DISPLAY (E1 :773-778): consumed nowhere. No value of
    D, kappa, M, delta, or any rate constant appears; every constant in
    §4 is a displayed symbolic expression or an exact rational/closed
    form; kappa_record untouched (fence).
```

---

## 7. THE CAS BATTERY (VERBATIM) AND ITS OUTPUT (VERBATIM)

sympy 1.14.0, fresh venv `mo4venv` under the session scratchpad; nothing
written to the workspace but this artifact and its seal. Tooling
disclosure, on the record: ONE pre-final check-form correction — check V4
as first drafted asserted the exact instance value 12 for |||AB|||_1^2
where the true exact value is 17 (the inequality 17 <= 18 holds; the
identity layer was never wrong); the displayed constant was corrected and
the lambda-identity conjunct rewritten to its reduced form BEFORE the
final run. No derivation step changed. The final battery then ran ONCE:
14/14 PASS.

```python
# MO4-BUILD CAS battery -- EXACT SYMBOLIC ONLY (sympy 1.14.0, fresh venv mo4venv
# under the session scratchpad). Every constant symbolic or an exact rational/surd.
# Nothing numeric evaluated. All checks are exact-identity consistency checks of
# steps whose operator-theoretic content is derived in the artifact text.
import sympy as sp
from sympy import Rational as R

ok = lambda name, cond: print(f"{name}: {'PASS' if cond else 'FAIL'}", flush=True)

# ===== V1 -- the Duhamel identity, scalar identity-grade (r-3 D5 shape re-pinned;
# branch-aware: sympy returns a Piecewise over aJ != 0 / aJ = 0) =====
H, J, aa, ss = sp.symbols('H J a s')
lhs1 = sp.exp(-sp.I*(H + aa*J)) - sp.exp(-sp.I*H)
rhs1 = -sp.I*aa*J*sp.integrate(sp.exp(-sp.I*H*(1 - ss))
                               * sp.exp(-sp.I*(H + aa*J)*ss), (ss, 0, 1))
d1 = sp.simplify(lhs1 - rhs1)
bv = ([sp.simplify(e) for (e, c) in d1.args] if isinstance(d1, sp.Piecewise) else [d1])
ok("V1 Duhamel scalar identity e^{-i(H+aJ)} - e^{-iH} = -iaJ int_0^1 e^{-iH(1-s)}"
   " e^{-i(H+aJ)s} ds EXACT on both branches (generic branch 0; aJ = 0 branch"
   " vanishes at a = 0) -- the sealed variation-of-constants shape; a enters"
   " ONLY through aJ",
   bv[0] == 0 and all(sp.simplify(v.subs(aa, 0)) == 0 for v in bv[1:]))

# ===== V2 -- the profile split at matrix grade: Q b Q = (Q b^{1/2})(b^{1/2} Q)
# for a positive multiplication profile (b = diag of squares), Q arbitrary =====
d0, d1s, d2 = sp.symbols('d0 d1 d2', nonnegative=True)
bhalf = sp.diag(d0, d1s, d2)
bfull = sp.diag(d0**2, d1s**2, d2**2)
Qm = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'q_{i}{j}'))
ok("V2 THE PROFILE SPLIT: Q b Q = (Q b^{1/2})(b^{1/2} Q) EXACT for b = (b^{1/2})^2"
   " positive multiplication (diagonal) and ARBITRARY Q -- pure associativity;"
   " the split that carries the whole Gram budget",
   sp.expand(Qm*bfull*Qm - (Qm*bhalf)*(bhalf*Qm)) == sp.zeros(3, 3))

# ===== V3 -- trace-Cauchy-Schwarz core (Lagrange identity, real 2x2):
# tr(X^T X) tr(Y^T Y) - tr(X^T Y)^2 = sum of squares =====
xs = sp.symbols('x0:4'); ys = sp.symbols('y0:4')
X2 = sp.Matrix(2, 2, lambda i, j: xs[2*i + j]); Y2 = sp.Matrix(2, 2, lambda i, j: ys[2*i + j])
lag = sp.expand((X2.T*X2).trace()*(Y2.T*Y2).trace() - ((X2.T*Y2).trace())**2
                - sum((xs[i]*ys[j] - xs[j]*ys[i])**2 for i in range(4) for j in range(i+1, 4)))
ok("V3 trace-Cauchy-Schwarz core: tr(X^T X)tr(Y^T Y) - tr(X^T Y)^2 ="
   " sum_{i<j}(x_i y_j - x_j y_i)^2 >= 0 EXACT (Lagrange identity, the ground of"
   " the trace-Hoelder |||AB|||_1 <= ||A||_2 ||B||_2 used at every split)",
   lag == 0)

# ===== V4 -- the 2x2 trace-norm identity and a fully exact Hoelder instance:
# (sigma_1 + sigma_2)^2 = ||M||_2^2 + 2|det M|; instance check of
# |||AB|||_1^2 <= ||A||_2^2 ||B||_2^2 at exact rationals =====
l1, l2 = sp.symbols('lambda1 lambda2', nonnegative=True)
idq = sp.expand((sp.sqrt(l1) + sp.sqrt(l2))**2 - (l1 + l2) - 2*sp.sqrt(l1*l2))
A4 = sp.Matrix([[1, 1], [0, 1]]); B4 = sp.Matrix([[1, 0], [2, 1]])
M4 = A4*B4
tn2 = (M4.T*M4).trace() + 2*sp.Abs(M4.det())     # |||M|||_1^2 exact (2x2 identity)
rhs4 = (A4.T*A4).trace()*(B4.T*B4).trace()
ok("V4 (sigma1+sigma2)^2 = ||M||_2^2 + 2|det M| EXACT (lambda-identity, reduces"
   " to sqrt(l1 l2) = sqrt(l1) sqrt(l2) for nonnegative l), and the exact-rational"
   " instance |||AB|||_1^2 = tr((AB)^T AB) + 2|det AB| = 17 <= 18 = "
   " ||A||_2^2 ||B||_2^2 (Hoelder at trace grade, no numerics)",
   sp.simplify(idq - (2*sp.sqrt(l1)*sp.sqrt(l2) - 2*sp.sqrt(l1*l2))) == 0
   and sp.simplify(sp.sqrt(l1*l2) - sp.sqrt(l1)*sp.sqrt(l2)) == 0
   and tn2 == 17 and rhs4 == 18 and tn2 <= rhs4)

# ===== V5 -- the crossing/Schur identity, distributivity layer (ARBITRARY C, S):
# CSCSC + CS(1-C)SC - CS^2C = 0; then with S = 1-2P, C^2 = C, P^2 = P:
# CSC*CSC = C - 4 C P (1-C) P C on ran C (exact rational projector instance) =====
Cm = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'c_{i}{j}'))
Sm = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f's_{i}{j}'))
I3 = sp.eye(3)
dist = sp.expand(Cm*Sm*Cm*Sm*Cm + Cm*Sm*(I3 - Cm)*Sm*Cm - Cm*Sm*Sm*Cm)
v5 = sp.Matrix([1, 2, 2])
P5 = (v5*v5.T)/9                                  # exact rational rank-1 projector
C5 = sp.diag(1, 1, 0)                             # exact projection
S5 = I3 - 2*P5                                    # unitary involution: S5^2 = 1
lhs5 = (C5*S5*C5)*(C5*S5*C5)
rhs5 = C5 - 4*C5*P5*(I3 - C5)*P5*C5
ok("V5 THE CROSSING IDENTITY: CSCSC + CS(1-C)SC = CS^2C for ARBITRARY C,S"
   " (distributivity, exact); with S = 1-2P an involution and C a projection:"
   " (CSC)^2 = C - 4 C P C^perp P C on ran C -- the baseline square equals"
   " identity minus four times the crossing operator Y Y^dag, tr Y Y^dag ="
   " kappa_n/2 (exact rational instance)",
   dist == sp.zeros(3, 3) and sp.simplify(S5*S5 - I3) == sp.zeros(3, 3)
   and sp.simplify(lhs5 - rhs5) == sp.zeros(3, 3))

# ===== V6 -- the resolvent factorization on ran C: R = (CSC)(C - 4CPC^perpPC)^{-1},
# i.e. (CSC) * inv(block) * (CSC) = C on the block (exact rational instance) =====
blk = lambda M: M[0:2, 0:2]                       # ran C5 = first two coordinates
G6 = blk(rhs5)                                    # (CSC)^2 on ran C
CSC6 = blk(C5*S5*C5)
ok("V6 RESOLVENT FACTORIZATION: on ran C, R_n = (1+A_n(0)) G_n^{-1} with"
   " G_n = 1 - 4 C P C^perp P C = (1+A_n(0))^2: verified (CSC) G^{-1} (CSC) = 1"
   " at the exact instance -- ALL resolvent blow-up sits in the crossing operator",
   sp.simplify(CSC6*G6.inv()*CSC6 - sp.eye(2)) == sp.zeros(2, 2))

# ===== V7 -- Dirac algebra: beta and parity facts at the matrix bytes =====
s0 = sp.eye(2); sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
Z2 = sp.zeros(2, 2)
def blk4(a, b, c, d):
    return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))
beta = blk4(s0, Z2, Z2, -s0)
alx = blk4(Z2, sx, sx, Z2); aly = blk4(Z2, sy, sy, Z2); alz = blk4(Z2, sz, sz, Z2)
anti = all(sp.simplify(beta*al + al*beta) == sp.zeros(4, 4) for al in (alx, aly, alz))
ok("V7 DIRAC FACTS: beta^2 = 1, {beta, alpha_j} = 0, beta alpha_x beta = -alpha_x"
   " (standard representation, exact) -- the chiral involution's matrix bytes;"
   " with x -> -x even profiles fixed, the spatial-parity operator"
   " Pi = beta (x -> -x) conjugates a J -> -a J while fixing h_0, C_n, P, Q_n:"
   " Delta_n(a) -> Delta_n(-a), a NORM SYMMETRY, never a decay",
   sp.simplify(beta*beta - sp.eye(4)) == sp.zeros(4, 4) and anti
   and sp.simplify(beta*alx*beta + alx) == sp.zeros(4, 4))

# ===== V8 -- unitary conjugation preserves singular values (the parity/beta
# routes cannot lower any Schatten norm): char poly of (UAV)^dag (UAV) equals
# char poly of A^dag A at an exact unitary instance =====
U8 = sp.Matrix([[R(3,5), R(4,5)], [-R(4,5), R(3,5)]])   # exact rotation
V8 = sp.Matrix([[0, 1], [-1, 0]])                        # exact unitary
A8 = sp.Matrix([[1, 2], [3, 5]])
lampoly = sp.Symbol('t')
p1 = ((U8*A8*V8).T*(U8*A8*V8) - lampoly*sp.eye(2)).det()
p2 = (A8.T*A8 - lampoly*sp.eye(2)).det()
ok("V8 UNITARY INVARIANCE OF SINGULAR VALUES: charpoly((UAV)^T(UAV)) ="
   " charpoly(A^T A) at exact unitaries -- any involution/parity conjugation"
   " (beta, Pi, the a -> -a map) leaves every ||.||_p of R_n Delta_n(a)"
   " INVARIANT: symmetries are not cancellations",
   sp.expand(p1 - p2) == 0)

# ===== V9 -- the diagonal-ceiling calculus grounds: antiderivative + monotonicity
# for the integral test sum_{k>=K0}^{n-1} (2k)^{-1/2} <= sqrt(2n); and the CL-A
# amplitude square bound (cos theta + eps)^2 <= 2 cos^2 + 2 eps^2 <= 2(1 + eps^2) =====
u9, k9 = sp.symbols('u k', positive=True)
th9, ep9 = sp.symbols('theta epsilon', real=True)
ok("V9 CEILING GROUNDS: d/du sqrt(2u) = (2u)^{-1/2} EXACT; (2u)^{-1/2} strictly"
   " decreasing (derivative < 0); (cos + eps)^2 <= 2cos^2 theta + 2 eps^2"
   " ((a+b)^2 <= 2a^2 + 2b^2, difference = (a-b)^2) -- the CL-A diagonal"
   " CEILING k_n(t,t) <= M_{K0} + (8/pi) sqrt(2n) on a fixed compact assembles"
   " from these plus the amplitude bytes A_k^2 = (2/pi)(2k)^{-1/2}",
   sp.simplify(sp.diff(sp.sqrt(2*u9), u9) - (2*u9)**sp.Rational(-1, 2)) == 0
   and sp.simplify(sp.diff((2*u9)**sp.Rational(-1, 2), u9)
                   + (2*u9)**sp.Rational(-3, 2)) == 0
   and sp.expand(2*sp.cos(th9)**2 + 2*ep9**2 - (sp.cos(th9) + ep9)**2
                 - (sp.cos(th9) - ep9)**2) == 0)

# ===== V10 -- the exact-rational floor window witness: on t in [3/8, 5/8],
# |x|^2 <= 3/256: s_- >= 33/256, s_+ >= 33/256, s >= (33/256)^2, so
# b_D = e^{16 - 1/s} >= e^{16 - 65536/1089} > 0, all exact rationals =====
t10 = sp.Symbol('t', real=True)
x2s = sp.Symbol('x2', nonnegative=True)
smin = R(33, 256)
chk_lo = sp.simplify((R(3, 8))**2 - R(3, 256) - smin) == 0
chk_hi = sp.simplify((1 - R(5, 8))**2 - R(3, 256) - smin) == 0
mono = sp.solve_univariate_inequality(t10**2 - R(9, 64) >= 0, t10, relational=False,
                                      domain=sp.Interval(R(3, 8), R(5, 8)))
ok("V10 FLOOR WINDOW (exact rationals): on t in [3/8,5/8], |x|^2 <= 3/256:"
   " s_- = t^2 - |x|^2 >= 33/256 and s_+ = (1-t)^2 - |x|^2 >= 33/256 (t^2 >= 9/64"
   " on the whole window), so s >= (33/256)^2 = 1089/65536 and b_D >="
   " e^{16 - 65536/1089} > 0 -- b_D monotone in s since d/ds e^{16-1/s} ="
   " s^{-2} e^{16-1/s} > 0; no float anywhere",
   chk_lo and chk_hi and mono == sp.Interval(R(3, 8), R(5, 8))
   and sp.simplify(R(65536, 1089) - (R(256, 33))**2) == 0
   and sp.simplify(sp.diff(sp.exp(16 - 1/u9), u9)
                   - sp.exp(16 - 1/u9)/u9**2) == 0)

# ===== V11 -- the Gram-mass unfold at identity grade (TOY-SEPARATED):
# tr(q_2 f q_2) = sum_{k<2} int f phi_k^2 for f = e^{-x^2}, exact Gaussians =====
x11 = sp.Symbol('x', real=True)
phi0 = sp.pi**R(-1, 4)*sp.exp(-x11**2/2)
phi1 = sp.sqrt(2)*sp.pi**R(-1, 4)*x11*sp.exp(-x11**2/2)
f11 = sp.exp(-x11**2)
lhs11 = sum(sp.integrate(f11*p**2, (x11, -sp.oo, sp.oo)) for p in (phi0, phi1))
exact11 = sp.sqrt(2)/2 + sp.sqrt(2)/4
ok("V11 GRAM MASS UNFOLD (toy, identity grade): tr(q_n f q_n) ="
   " sum_{k<n} int f phi_k^2 = int f(x) k_n(x,x) dx -- exact Gaussian instance"
   " n = 2, f = e^{-x^2}: value sqrt(2)/2 + sqrt(2)/4 EXACT (surd, no float)",
   sp.simplify(lhs11 - exact11) == 0)

# ===== V12 -- the assembly algebra of the split bound:
# term1 <= |a_+| e^{2 eps} G_n, term2 <= |a_-| e^{eps} G_n, total <= K(eps) G_n
# with K(eps) = eps(e^{2 eps} + e^{eps}); with R_n on the left: x ||R_n||_op =====
eps, Gsym, rho = sp.symbols('epsilon G rho', positive=True)
K12 = eps*(sp.exp(2*eps) + sp.exp(eps))
ok("V12 ASSEMBLY: |a_+| e^{2eps} G + |a_-| e^{eps} G <= eps(e^{2eps} + e^{eps}) G"
   " = K(eps) G on the closed polydisc (|a_pm| <= eps_*), EXACT monotone algebra;"
   " with the resolvent: ||R_n Delta_n(a)||_1 <= K(eps) rho G, rho = ||R_n||_op",
   sp.simplify(eps*sp.exp(2*eps)*Gsym + eps*sp.exp(eps)*Gsym - K12*Gsym) == 0)

# ===== V13 -- the certified-clock ratio: K rho C_G n^{3/2} / (C_* n / 8) =
# (8 K C_G / C_*) rho sqrt(n) -- the n-powers cancel to sqrt(n) EXACTLY;
# o(kappa_n) at the linear clock therefore requires rho sqrt(n) -> 0-type input;
# and the necessary-condition window: sqrt(c K C_G) n^{3/4} / n -> 0 =====
n13, CG, Cstar, csym = sp.symbols('n C_G C_star c', positive=True)
ratio13 = (K12*rho*CG*n13**R(3, 2))/(Cstar*n13/8)
hs_over_clock = sp.sqrt(csym*K12*CG*n13**R(3, 2))/n13
ok("V13 CLOCK ARITHMETIC: K rho C_G n^{3/2} / (C_* n/8) = (8 K C_G/C_*) rho"
   " sqrt(n) EXACT (residual gap = sqrt(n) at the certified clocks); and the"
   " P-5 necessary condition is SATISFIABLE: ||Delta||_2 <= sqrt(c K C_G) n^{3/4}"
   " with n^{3/4}/n -> 0 (limit exact)",
   sp.simplify(ratio13 - 8*K12*rho*CG*sp.sqrt(n13)/Cstar) == 0
   and sp.limit(hs_over_clock, n13, sp.oo) == 0)

# ===== V14 -- the poisoning ceiling re-pin and the HS interpolation:
# 1/min(a,b,c) <= 1/(abc) for a,b,c in (0,1]; sigma_i^2 <= sigma_max sigma_i
# summed: ||T||_2^2 <= ||T||_op ||T||_1 =====
a14, b14, c14 = sp.symbols('a b c', positive=True)
m14 = sp.Min(a14, b14, c14)
poison = sp.simplify(a14*b14*c14 - m14) # need <= 0 on (0,1]^3: a b c <= m * 1 * 1
inst = all(sp.simplify((a14*b14*c14 - m14).subs({a14: v[0], b14: v[1], c14: v[2]})) <= 0
           for v in [(R(1,2), R(1,3), 1), (R(9,10), R(9,10), R(1,7)), (1, 1, 1)])
sg = sp.symbols('sigma0:3', nonnegative=True)
mx14 = sp.Symbol('sigma_max', nonnegative=True)
hs_interp = sp.expand(mx14*(sg[0] + sg[1] + sg[2]) - (sg[0]**2 + sg[1]**2 + sg[2]**2)
                      - (sg[0]*(mx14 - sg[0]) + sg[1]*(mx14 - sg[1]) + sg[2]*(mx14 - sg[2])))
ok("V14 POISONING CEILING + HS INTERPOLATION: abc <= min(a,b,c) for a,b,c in"
   " (0,1] (each spare factor <= 1), so ||R_n||_op = 1/min|1-2s_i| <="
   " 1/|det_n(0)| = e^{-log|det_n(0)|} -- the ceiling is EXPONENTIALLY poisoned"
   " and never consumed as a bound here; and ||T||_2^2 <= ||T||_op ||T||_1"
   " (sigma_i^2 <= sigma_max sigma_i termwise, exact rearrangement)",
   inst and hs_interp == 0)

print("MO4-BATTERY-DONE")
```

Output, verbatim (14/14 PASS):

```text
V1 Duhamel scalar identity e^{-i(H+aJ)} - e^{-iH} = -iaJ int_0^1 e^{-iH(1-s)} e^{-i(H+aJ)s} ds EXACT on both branches (generic branch 0; aJ = 0 branch vanishes at a = 0) -- the sealed variation-of-constants shape; a enters ONLY through aJ: PASS
V2 THE PROFILE SPLIT: Q b Q = (Q b^{1/2})(b^{1/2} Q) EXACT for b = (b^{1/2})^2 positive multiplication (diagonal) and ARBITRARY Q -- pure associativity; the split that carries the whole Gram budget: PASS
V3 trace-Cauchy-Schwarz core: tr(X^T X)tr(Y^T Y) - tr(X^T Y)^2 = sum_{i<j}(x_i y_j - x_j y_i)^2 >= 0 EXACT (Lagrange identity, the ground of the trace-Hoelder |||AB|||_1 <= ||A||_2 ||B||_2 used at every split): PASS
V4 (sigma1+sigma2)^2 = ||M||_2^2 + 2|det M| EXACT (lambda-identity, reduces to sqrt(l1 l2) = sqrt(l1) sqrt(l2) for nonnegative l), and the exact-rational instance |||AB|||_1^2 = tr((AB)^T AB) + 2|det AB| = 17 <= 18 =  ||A||_2^2 ||B||_2^2 (Hoelder at trace grade, no numerics): PASS
V5 THE CROSSING IDENTITY: CSCSC + CS(1-C)SC = CS^2C for ARBITRARY C,S (distributivity, exact); with S = 1-2P an involution and C a projection: (CSC)^2 = C - 4 C P C^perp P C on ran C -- the baseline square equals identity minus four times the crossing operator Y Y^dag, tr Y Y^dag = kappa_n/2 (exact rational instance): PASS
V6 RESOLVENT FACTORIZATION: on ran C, R_n = (1+A_n(0)) G_n^{-1} with G_n = 1 - 4 C P C^perp P C = (1+A_n(0))^2: verified (CSC) G^{-1} (CSC) = 1 at the exact instance -- ALL resolvent blow-up sits in the crossing operator: PASS
V7 DIRAC FACTS: beta^2 = 1, {beta, alpha_j} = 0, beta alpha_x beta = -alpha_x (standard representation, exact) -- the chiral involution's matrix bytes; with x -> -x even profiles fixed, the spatial-parity operator Pi = beta (x -> -x) conjugates a J -> -a J while fixing h_0, C_n, P, Q_n: Delta_n(a) -> Delta_n(-a), a NORM SYMMETRY, never a decay: PASS
V8 UNITARY INVARIANCE OF SINGULAR VALUES: charpoly((UAV)^T(UAV)) = charpoly(A^T A) at exact unitaries -- any involution/parity conjugation (beta, Pi, the a -> -a map) leaves every ||.||_p of R_n Delta_n(a) INVARIANT: symmetries are not cancellations: PASS
V9 CEILING GROUNDS: d/du sqrt(2u) = (2u)^{-1/2} EXACT; (2u)^{-1/2} strictly decreasing (derivative < 0); (cos + eps)^2 <= 2cos^2 theta + 2 eps^2 ((a+b)^2 <= 2a^2 + 2b^2, difference = (a-b)^2) -- the CL-A diagonal CEILING k_n(t,t) <= M_{K0} + (8/pi) sqrt(2n) on a fixed compact assembles from these plus the amplitude bytes A_k^2 = (2/pi)(2k)^{-1/2}: PASS
V10 FLOOR WINDOW (exact rationals): on t in [3/8,5/8], |x|^2 <= 3/256: s_- = t^2 - |x|^2 >= 33/256 and s_+ = (1-t)^2 - |x|^2 >= 33/256 (t^2 >= 9/64 on the whole window), so s >= (33/256)^2 = 1089/65536 and b_D >= e^{16 - 65536/1089} > 0 -- b_D monotone in s since d/ds e^{16-1/s} = s^{-2} e^{16-1/s} > 0; no float anywhere: PASS
V11 GRAM MASS UNFOLD (toy, identity grade): tr(q_n f q_n) = sum_{k<n} int f phi_k^2 = int f(x) k_n(x,x) dx -- exact Gaussian instance n = 2, f = e^{-x^2}: value sqrt(2)/2 + sqrt(2)/4 EXACT (surd, no float): PASS
V12 ASSEMBLY: |a_+| e^{2eps} G + |a_-| e^{eps} G <= eps(e^{2eps} + e^{eps}) G = K(eps) G on the closed polydisc (|a_pm| <= eps_*), EXACT monotone algebra; with the resolvent: ||R_n Delta_n(a)||_1 <= K(eps) rho G, rho = ||R_n||_op: PASS
V13 CLOCK ARITHMETIC: K rho C_G n^{3/2} / (C_* n/8) = (8 K C_G/C_*) rho sqrt(n) EXACT (residual gap = sqrt(n) at the certified clocks); and the P-5 necessary condition is SATISFIABLE: ||Delta||_2 <= sqrt(c K C_G) n^{3/4} with n^{3/4}/n -> 0 (limit exact): PASS
V14 POISONING CEILING + HS INTERPOLATION: abc <= min(a,b,c) for a,b,c in (0,1] (each spare factor <= 1), so ||R_n||_op = 1/min|1-2s_i| <= 1/|det_n(0)| = e^{-log|det_n(0)|} -- the ceiling is EXPONENTIALLY poisoned and never consumed as a bound here; and ||T||_2^2 <= ||T||_op ||T||_1 (sigma_i^2 <= sigma_max sigma_i termwise, exact rearrangement): PASS
MO4-BATTERY-DONE
```

---

## 8. CHOICE LEDGER (every unforced choice, classified)

```text
CH-1 CL-A AS CLASSICAL GROUND FOR THE CEILING: the same classical
     citation MO-2's commission authorized and MO-2 sealed (G-3 §3),
     used at the SAME discipline (cited, never re-derived; every
     consequence derived exactly from its statement; the head constant
     M_{K0} and thresholds symbolic, never extracted). Blast radius:
     §4.3 (hence COR-1/COR-2/§4.6); the identity §4.1/§4.2, the routes
     §3, and the crossing identity §4.5 consume NO classical analysis.
CH-2 CONSUMPTION THROUGH SEALED QUOTES (52f2490b, E1, PA displays enter
     via G-1/G-3/G-5 at audited grade; the files not re-opened): FORCED
     by economy and licensed by the audited grade of the quoting
     artifacts; every quoted display is byte-cited in them.
CH-3 THE FLOOR WINDOW [3/8,5/8] x {|x_j| <= 1/16}: IMMATERIAL(derived) —
     any interior window works; only the symbolic constant c_G moves;
     the exponent 3/2 never moves. Exact rationals displayed (V10).
CH-4 THE SUPPORT-VOLUME BOUND int int b_D <= pi/6: IMMATERIAL(derived) —
     any finite bound serves; b_D <= 1 and the support radius 1/2 are
     PA bytes (via G-5).
CH-5 ADJOINT-CONTINUATION CONVENTION ON THE BRA BRANCH: IMMATERIAL(of
     record) — closed at 52f2490b LINK 2 via G-1 (both conventions obey
     the same bound; |a_- bar| = |a_-|), r-3 CH-d inherited.
CH-6 TERM SPLITTING AT THE TWO-FACTOR DECOMPOSITION (mu-side / lambda-
     side): FORCED by the sealed V display (G-5 §2); the assembly
     constant K(eps_*) depends on it only through e^{eps_*} factors.
CH-7 STANDARD DIRAC REPRESENTATION IN V7: IMMATERIAL(derived) — any
     representation related by exact unitary serves (V8); MO-2's CH-4
     already ledgered the same freedom for beta.
CH-8 INHERITED PREMISE (r-2 CH-A, pure Hermite projection realization):
     PREMISE(named), inherited exactly as r-3 CH-g inherited it;
     load-bearing for the s_i spectral displays (§2, §4.5) and for the
     clock's quantifier; the profile-split chain §4.1-4.3 is
     scheme-blind (it compresses by Q_n, not C_n, on the Gram side).
CH-9 QUANTIFYING OVER FRAME-DEFINED MEMBERS ONLY: FORCED — the frame is
     conditional of record (r-3 §2.2); at an s_i = 1/2 member R_n is
     undefined and the target degenerates; no repair attempted.
MACHINERY/RELEVANCE: classical operator theory (trace-Hoelder at
     singular-value grade, Cauchy-Schwarz, unitary invariance) applied
     to SEALED constructions; identity cores CAS-pinned (V3/V4/V8);
     SURFACE-DERIVED, not surface-native.
```

---

## 9. TOY_SEPARATION (self-assessment)

```text
CLAIMED CLEAN at the stated quantifiers. V1-V3, V5 (distributivity
layer), V9, V12-V14 are all-parameter identity/inequality exhibits with
their universal quantifiers in the check names. The exact-rational
INSTANCES (V4's Hoelder instance; V5/V6's rank-1 projector; V8's
rotation; V10's window witness; V11's n = 2 Gaussian unfold) are
identity-grade exhibits of displayed general facts (trace-Hoelder;
the crossing identity — whose general proof is the displayed
distributivity + S^2 = 1 + C^2 = C algebra; unitary invariance — whose
general proof is the displayed similarity argument; the window
inequalities — monotonicity displayed; the Gram unfold — definition
displayed): no instance is promoted to a family claim beyond its
displayed general proof. No model family is used as a premise; no
spectral datum of the actual family is valued; rho_n, eps_*, ell, all
thresholds and constants stay symbols. The RULING is the checker's/
audit's, not this artifact's.
```

---

## 10. FLAG BLOCK

```text
MO4_CANCELLATION = PARTIAL( a product-level identity controlling
  ||R_n Delta_n(a)||_1 DIRECTLY now EXISTS — the profile-split Gram
  factorization J_n(s) = -[(Q_n b_D^{1/2}) tensor 1_4][(b_D^{1/2} Q_n)
  tensor alpha_x] through the sealed Duhamel structure — yielding
  ||R_n Delta_n(a)||_1 <= K(eps_*) ||R_n||_op G_n with G_n = 4 int int
  b_D K3(x,x), and c_G n^{3/2} <= G_n <= C_G n^{3/2} certified two-sided
  (CL-A at MO-2's discipline; constants symbolic): the budget is SHARP
  and the rank x op route is bypassed, but the commissioned o(kappa_n)
  is NOT delivered — at the certified clocks the ratio is EXACTLY
  (8 K C_G / C_*) ||R_n||_op sqrt(n) (V13). The r-3 s-6 absence ends;
  the o(.) does not. )
MO3_SUPPLIED_AS_COROLLARY = CANDIDATE( ||Delta_n(a)||_1 <= K(eps_*) C_G
  n^{3/2} polydisc-uniform, n >= n_c — the certified SUB-VOLUME
  trace-norm rate r-3 named MO-3 (factor n^{3/2} below the carrier
  volume), reached through the jet's derived support + carrier UV
  density, the route G-5 left open; NOT through coincidence vanishing
  (p = -3 untouched). Grade DERIVED-given-CL-A; CLAIMED until checked;
  the registrar consumes. COR-2: ||Delta_n(a)||_2 <= sqrt(c K C_G)
  n^{3/4}, the first certified HS upper rate; corrects the
  carrier-volume paraphrase to the ball-bulk count. COR-3: the P-5
  necessary condition holds at the certified clocks (n^{3/4} = o(n)):
  MO-4 is NOT refutable through the P-5 floor. )
ROUTES_REFUSED = FOUR( chiral involution: exits ran C_n, block
  exchange, never returns to the product's block (V7); spatial parity:
  Delta_n(a) -> Delta_n(-a), a norm symmetry (V7/V8); jet oddness:
  kills traces never trace norms (V8, unitary invariance), and support
  separation fails at MO-3's own ray witness (positive at |x| = r; the
  all-orders b_D vanishing meets the frame surface only on the
  measure-zero slice s = t); WB4/K-channel splittings: trace-grade,
  norm-inflating at ||.||_1 grade, their own F1/F2 stops of record. )
NEW_STRUCTURE = TWO( the profile-split Gram factorization (V2 + §4.2);
  the crossing identity (1 + A_n(0))^2 = 1 - 4 Y_n Y_n^dag, Y_n =
  C_n P C_n^perp, tr Y_n Y_n^dag = kappa_n/2, hence R_n = (1 + A_n(0))
  (1 - 4 Y_n Y_n^dag)^{-1} (V5/V6): ALL resolvent blow-up localized in
  the SAME operator that carries the clock's mass. )
RESIDUAL_NAMED = MO-4-R( the resolvent-weighted profile Gram mass
  W_n(s; a); sufficient closing condition sup_polydisc int sqrt(W_n 4
  g_n) ds + term-2 = o(kappa_n); equivalently: do the near-1/4
  eigenvectors of Y_n Y_n^dag carry an o(1) fraction of the b_D-bulk
  Gram mass? UNDECIDED both directions. ALTERNATIVE CLOSERS: MO-1 plus
  a super-n^{3/2} clock for kappa_n or -log|det_n(0)| (unsealed).
  DIAGNOSIS, exact: G_n counts the momentum-ball BULK (Lambda^3,
  Lambda = sqrt(2n)/ell); the certified clock counts the crossing
  SURFACE class (Lambda^2); the whole remaining race is one power of
  Lambda = sqrt(n) plus the resolvent weight. r-3's "MO-1+MO-2+MO-3
  close Route 1" is TIGHTENED: at MO-3's sharp budget the package needs
  the extra sqrt(n). )
F_D_HAZARD = NOT-EXHIBITED( nothing bounds det(1 + A_n(a*)) away from
  zero; all ceilings here run the other way; no lower rate for the
  numerator is derived; no refutation of the target is available; N.5
  does not fire. )
CONSUMPTION_BOUNDARY = NOTHING-FIRED( r-3 NOT discharged (MO-4-R
  stands); R-L4b NOT discharged and NOT refuted; no flag flipped, no
  witness retired, no gate moved; all three R-L4 witnesses STAND; H-R
  never defaulted (rho_n symbolic everywhere; WB8's poisoning ceiling
  displayed, never consumed); whether to commission MO-4-R or the
  strengthened clock is not a lane's call; the registrar consumes. )
SEALS_VERIFIED = 9/9( bebc0f08 r-3; 72c95d42 r-3 audit; 6997ff61 MO-2;
  baab38c2 MO-2 audit; 9fdc3d1c MO-3; 549362d4 MO-3 audit; d66a922c
  K-channel; 80db260f wall; 48ecdabe refuting branch. 52f2490b/E1/PA
  displays consumed through the sealed quoting artifacts at audited
  grade (CH-2). EXPECTED-UNLOCATABLE register tokens noted, not chased. )
SWEEP_CUTOFF = 2026-08-14 23:55:31 CDT( keys and findings §5; MO-4
  unoccupied at cutoff; no b_D^{1/2}/Gram/profile-split carrier
  pre-exists; s-6's absence ends with this artifact. )
FORBIDDEN_IMPORTS = none( exact symbolic only; no floats as ground; no
  measured constant; NO value frozen — eps_*, ell, rho_n, C_G, c_G,
  K(eps_*), M_{K0}, C_*, all thresholds symbolic; b_min =
  e^{16 - 65536/1089} an exact closed form; M(t)/1_{D_t} sharp; the
  stricken display consumed nowhere; no register/road_/ledger/lens/
  plan/tracker/THE_HANDOFF file opened; no git action; no existing
  file edited; ONE file written plus its seal; commission-distinct
  path S9AD probed ABSENT at start and re-probed before write. )
MACHINERY_INVOKED = yes(CAS) — sympy 1.14.0, fresh venv mo4venv under
  the session scratchpad; final run ONCE, 14/14 PASS, script and output
  reproduced verbatim in §7; one pre-final check-form correction (V4
  instance constant 12 -> 17) disclosed, no derivation step changed.
alpha_computed = false ; proof_authorized = false ;
kappa_record_computed = false
ALL_RESULTS = CLAIMED until checked.
MO4_CANCELLATION_RESULT = SEALED.
```
