# Duhamel-Gate Formal Derivations Draft V001 (primary execution lane, fresh re-run)

Date: 2026-07-26 (fresh re-run after the session-limit interruption recorded
in `STAGE8_T7_D6_EXECUTION_ADDENDUM_AND_INTERRUPTION_RECORD_V001.md` A3;
the prior killed primary's partial draft at this path, sha256
`2d8b094e26975104b4b6b75bc7b8ab65b82ec33b2d3c949288e8d264c1442e99`, is
superseded by this fresh emission and its hash is preserved here for the
audit trail).

Governing texts:
`STAGE8_T7_COMPLETED_CONDITIONED_DUHAMEL_IDENTITY_AND_INTERCHANGE_SCHEMA_SPEC_V001.md`
as amended by `STAGE8_T7_D6_SPECS_REPAIR_AMENDMENT_V001.md` Part II (the
amendment GOVERNS where it differs) and the sealed execution addendum
(A1 pair-evaluated S6.3(b) reading; A2 F-C ordering block). Every frozen
authority hash, the amendment-added diagnostic-spec hash (D-4, joined across
its printed line wrap to
`d1b5ab24ebf8c1bc9b7598449596a6431c2152cab7edcf4d0cefcfd64e3815a5`), and the
three governing documents' seals were verified before any other action (M1:
24/24 exact matches).

Status: DRAFT execution artifact of the primary lane. No .seal files and no
result .md are emitted by this lane. Exact arithmetic decided every decidable
claim (fractions.Fraction; Gaussian-rational pairs; exact polynomial and jet
algebra); certified outward enclosures otherwise; floats inform, never
decide. No measured constant was consulted; no coupling, kappa_record, or
alpha target was read.

---

## 1. Setting (S1, restated)

Per member `K` of the relayed causally-sequential exhaustion and per pinned
state `rho`, with `Q = Q^dagger = Q^2` the completed compression and
`V_K[A] = W_K[A] i_r` the Stinespring isometry (sealed O1-O3 of
`2f2aa7f7...`), define the Hilbert-Schmidt vectors

    X_K(a) = Q V_K[A^(a)] rho^(1/2),

so that the completed state-evaluated kernel is the Gram form

    z_c,K(a_+, a_-) = omega(V_K[A_-]^dagger Q V_K[A_+]) = <X_K(a_-), X_K(a_+)>_HS,

with the pinned (-,+) Wightman ordering (D-6/D-9: the frozen display is
`omega(V[A_-]^dagger Q V[A_+])`; plus history on the ket branch). Hermitian
symmetry for real histories is exact:

    z_c,K(a_+,a_-)^* = <X(a_+), X(a_-)> = z_c,K(a_-,a_+).            (O4)

Diagonal: `q_K(a) := z_c,K(a,a) = ||X_K(a)||^2`, not identically 1 on the
completed chain. Baseline hypothesis B0(K, rho): `q := q_K(0) != 0`
(decided per fixture in the execution record; never promoted — the
volume-uniform promotion is (H1), a named underived input, per D-7 "(H1)
presupposes and extends B0").

Under C2 (Section 6) the sealed O5 tangent has no boundary-derivative
terms, so with `A_s = A + s a`:

    delta V = -i integral_0^T W(T,t) J_a(t) W(t,0) dt  i_r,
    eta := Q (delta V) rho^(1/2),      X_0 := X_K(0),
    d_(a_+) z_c|_0 = <X_0, eta>,   d_(a_-) z_c|_0 = <eta, X_0>,
    d_(a_+) d_(a_-) z_c|_0 = <eta, eta>.                              (1.1)

The first-derivative displays follow from bilinearity of the Gram form and
the definition of eta; the mixed second derivative has one tangent on each
argument, hence `<eta, eta>`; no time-ordering symbol is inserted (S1.3).

## 2. FK-1 (mixed-CTP conditioned-covariance normal form)

THEOREM FK-1. Under B0 and C2,

    g_(D,c,K) := d_(a_+) d_(a_-) log z_c,K |_(0,0)
               = <eta,eta>/q - <eta,X_0><X_0,eta>/q^2
               = [ <eta,eta><X_0,X_0> - |<X_0,eta>|^2 ] / q^2.

PROOF. By the quotient rule on `log z_c`,

    d_+ d_- log z_c = [ z_c (d_+ d_- z_c) - (d_+ z_c)(d_- z_c) ] / z_c^2 .

Evaluating at (0,0) with (1.1) gives the first display; multiplying the
first term by q/q gives the second. QED. (Machine check: the ratio and
covariance forms have identical numerator over q^2 — exact polynomial
identity, `m7_symbolic_lane.py`.)

Structural facts, each verified rather than assumed:

(P1) Reality. Hermitian symmetry `z_c(a_+,a_-)^* = z_c(a_-,a_+)` forces the
second-order jet of `L = log z_c` to have the form

    L = L_0 + alpha a_+ + conj(alpha) a_-
        + (1/2) L_(++) a_+^2 + (1/2) conj(L_(++)) a_-^2 + g a_+ a_- ,

with g self-conjugate, i.e. real. (Exact jet computation confirms the
conjugation pattern and `Im g = 0` on the F-B closed forms.)

(P2) Positivity of the MIXED form. By Cauchy-Schwarz on the HS inner
product, `<eta,eta><X_0,X_0> >= |<X_0,eta>|^2`, so `g_(D,c,K) >= 0`, with
equality iff eta is parallel to X_0. No positivity is claimed for the
one-branch weak-value forms. (F-A numerics: lower(g interval) > 0, M3(ii).)

(P3) Reduction. At `Q = I_R`, pure rho: q = 1 and FK-1 reduces to the sealed
exhaustive `g_D = <eta|eta> - |<psi|eta>|^2` of `3d86dc4f...`. Executed as a
control only; F2.1/F2.2 forbid transport of exhaustive results.

(P4) Degenerate endpoint. If the compression is rank-one (F-B comparator),
X(a) = A_+(a) |fixed>, so eta is parallel to X_0 and `g_(D,c) = 0` EXACTLY
(and independently: z_c factorizes as f(a_-)^* f(a_+), so log z_c splits
additively and the mixed derivative vanishes). Verified in exact rational
arithmetic (M4).

## 3. FK-2 (attenuation corollary with the diagonal correction)

THEOREM FK-2. Under B0, C2, with the full second-order Duhamel expansion
(contact term included whenever the generator is non-affine; it vanishes
under C1):

    H_(att,K) := -Re d^2_(a_+) log z_c,K |_(0,0)
               = g_(D,c,K) - (1/2) (log q_K)''(0).

PROOF. Restrict the (P1) jet to the diagonal:
`log q(a) = L(a,a) = L_0 + 2 Re(alpha) a + [Re L_(++) + g] a^2 + O(a^3)`,
so `(log q)''(0) = 2 Re L_(++) + 2 g`. Then

    -Re L_(++) = g - (1/2)(log q)''(0),

which is the claim since `H_att = -Re L_(++)`. (Machine check: exact
polynomial identity in (Re L_++, g).) QED.

Second-derivative content. With
`zeta := Q (delta^2 V) rho^(1/2)` and the sealed second-order expansion

    delta^2 V = 2(-i)^2 integral_(T>=t>s>=0) W(T,t) J(t) W(t,s) J(s) W(s,0) dt ds i_r
                + (-i) integral_0^T W(T,t) [d^2 H_s(t)/ds^2] W(t,0) dt i_r,

the second line is the CONTACT TERM (zero under C1; nonzero and exactly
computable on the F-A three-site fixture, whose generator curvature is
`d^2 D_theta/dtheta^2|_0` with exact entries -1/18 (forward) and +1/18
(backward) — exact rationals, verified). Then `d^2_(a_+) z_c|_0 = <X_0, zeta>`
and

    L_(++) = <X_0, zeta>/q - (<X_0, eta>/q)^2 .

The scalar algebra `Re[c^2] = 2(Re c)^2 - |c|^2` (exact polynomial identity,
machine-verified) is what converts the square of the drift coefficient into
the attenuation bookkeeping. The stencil realization

    H_(att,K) = lim_(h->0) [ -log|zhat_c(h,0)| - log|zhat_c(-h,0)| ] / h^2,
    zhat_c := z_c / q,

requires B0 (the un-normalized stencil diverges — the finite shadow of the
missing unitality anchor). On the exhaustive chain `q == 1` kills the
correction; on the completed chain it is generically nonzero (F-A witness:
`(log q)''(0)` enclosure `0.10210007 +- 1.01e-6`, excluding zero), which is
the mechanical content of fence F2.2.

## 4. FK-3 (Fubini-Study corollary on the completed output ray)

THEOREM FK-3. Under B0 and C2 the FS pullback of the normalized completed
output ray `Xhat(a) = X(a)/||X(a)||` at baseline equals FK-1 exactly:

    g_FS(completed ray)|_0 = <X'(0),X'(0)>/q - |<Xhat(0),X'(0)>|^2 / q = g_(D,c,K).

PROOF. The FS pullback of a curve X(a) in ray space is
`[<X',X'> ||X||^2 - |<X,X'>|^2] / ||X||^4`. At a = 0 with X' = eta,
`||X||^2 = q`, this is `[<eta,eta> q - |<X_0,eta>|^2]/q^2 = g_(D,c,K)`. QED.
(Same numerator, exact identity, machine-verified.) This realizes battery T9
on the COMPLETED output ray; the FS of the exhaustive output ray equals
g_all and is a different number (F-A: 0.0648 vs 0.00845) — conflation is an
F2.2 violation caught by the wrong-form control.

## 5. L-ADD (q-weighted Hessian-mixing lemma; freeze F2.4 obligation)

THEOREM L-ADD. With `z_all = z_c + z_r` exact (D2 completeness),
`z_all(0,0) = 1` (exhaustive unitality), `q in (0,1)`,
`zhat_c = z_c/q`, `zhat_r = z_r/(1-q)`,
`alpha_c = d_+ log zhat_c|_0`, `alpha_r = d_+ log zhat_r|_0`, and
g_c, g_r, g_all the FK-1 mixed log-Hessians of the respective functionals:

    g_all = q g_c + (1-q) g_r + q(1-q) |alpha_c - alpha_r|^2 .

PROOF. At baseline `z_all = 1`:

    d_+ z_all|_0     = q alpha_c + (1-q) alpha_r ;
    d_+ d_- z_all|_0 = q (g_c + |alpha_c|^2) + (1-q)(g_r + |alpha_r|^2) ;
    g_all = d_+ d_- z_all - (d_+ z_all)(d_- z_all)
          = q g_c + (1-q) g_r
            + [ q|alpha_c|^2 + (1-q)|alpha_r|^2 - |q alpha_c + (1-q) alpha_r|^2 ].

The bracket equals `q(1-q)|alpha_c - alpha_r|^2`: this is an exact
polynomial identity in (q, Re alpha_c, Im alpha_c, Re alpha_r, Im alpha_r)
(machine-verified over Q; it is the variance decomposition of a two-point
distribution). QED.

DEGENERATE ENDPOINT (q = 1, stated separately; the generic formula needs
q != 1). There `X_r(0) = 0`, hence `d_+ z_r|_0 = <X_r(0), eta_r> = 0` while
`d_+ d_- z_r|_0 = ||eta_r||^2` need not vanish, and directly

    g_all = g_c + ||eta_r||^2                    (q = 1),

also machine-verified as an exact identity. On the F-B comparator
(q(0) = |A_+(0)|^2 = 1, exact): g_c = 0, ||eta_r||^2 = |A_-'(0)|^2 = 1/4,
g_all = 1/4 — all exact rationals (M4).

Consequences: (i) completed and exhaustive mixed Hessians differ by
`(1-q)(g_r - g_c) + q(1-q)|alpha_c - alpha_r|^2`; no identity equates them.
(ii) Route-1 endpoint attenuation coincidence WITHOUT Hessian equality:
`g_c = 0, (log q_c)'' = -1/2, H_att,c = 1/4; g_all = 1/4, (log q_all)'' = 0,
H_att,all = 1/4; g_all - g_c = 1/4` — the six mandatory exact anchors, all
verified in exact rational jet arithmetic, reproducing the sealed
sigma-witness curvatures (FS 1/4; linear-amplitude attenuation 1/4;
endpoint-probability 1/2; inclusive sandwich 0) of `e12fffcc...`.
(iii) L-ADD runs as a residual check on every fixture: F-A residual
enclosure `-5.42e-10 +- 1.56e-8`, containing 0 (M5).

## 6. C1 and C2 (hypothesis-lemmas of S2)

C1 (branch generators affine in the branch tangent at baseline). On the
sealed Phase-A A2 frozen form (`789338ad...`),

    h_(lambda,n,ell)(t; a) = h_(0,n,ell) + lambda v(t) M_(n,ell)(t) tensor S_n
                             + a J_(n,ell)(t),
    J_(n,ell)(t) = -B_(D,n,ell)(t) tensor alpha_x,

the a-dependence is a polynomial of degree <= 1 with coefficients
independent of a and of lambda; therefore `d^2 h/da^2 = 0` IDENTICALLY.
Machine check: formal second derivative of the degree-1 polynomial with
operator-coefficient placeholders is the zero polynomial. C1 DERIVES on the
Phase-A chain. Recorded falsification channel (binding on successors,
non-blocking here): V011 link-holonomy generators depend on the connection
through `exp(i integral A)` factors and are NOT affine; the F-A three-site
fixture generator (phases `exp(+-i theta/3)`) is itself non-affine with
exact curvature entries -/+ 1/18 and is exploited as the S6.3(a) contact-
term negative control, with its curvature term included exactly wherever
the fixture is used.

C2 (history-independence of boundary data along the relayed exhaustion).
(a) The ready injection: A3 fixes `|ready> = |0>` of the qutrit record; it
is built from the record carrier alone and takes no A argument (exact
inspection of the sealed display). (b) The final PVM and Q_comp: A3 builds
`P_lambda` as spectral projectors of the fixed c-matrix
`[[0,0,-i],[0,0,i],[i,-i,0]]`; no A dependence; Q_comp is their partial
sum. (c) The relay isometries: built from exact incidence projectors with
no history argument (`52401eef...` S-section: `Tr(P_0 P_1) = Tr(P_1 P_2) =
1/4`, `Tr(P_0 P_2) = 0`; `0df721a1...` for relay necessity along the
exhaustion). (d) Envelope clause (per `da6d8cc7...` 3(3)(d)): in the A2
display the envelope profile enters the generator ONLY through the scalar
`v(t)` multiplying lambda, never through i_r, the PVM, or the relays; the
history enters only through `a J(t)`. Hence (a)-(c) hold uniformly over the
declared ER envelope-profile class. C2 DERIVES. Recorded falsification
channel: any gauge-covariance completion transports the carrier by
`exp(i chi)` and makes the injection history-dependent in the transformed
frame; C2 must then be re-derived. On F-A the write operators and record
projectors are constructed without any theta argument (exact, by
construction in the hash-pinned realization `3d8aea1a...`).

## 7. S5.2 — the conditional interchange theorem schema (full proof, amended hypotheses)

HYPOTHESES (named underived inputs; consumed, not discharged):

(H1) [D-1 restatement; = battery T7(ii)] There exists a common
`epsilon_* > 0` such that for every member K, the normalized pair-holomorphic
extension `Ghat_K` is ZERO-FREE on the closed pair polydisc
`P = {(z,w): |z| <= epsilon_*, |w| <= epsilon_*}`; any quantitative floor is
K-DEPENDENT only (e.g. `>= exp(-N_4(K) Gamma_*)`); no K-uniform delta is
hypothesized. Here `Ghat_K` is jointly holomorphic on a neighborhood of P
(finite-K entirety: finite-dimensional Dyson series in z, adjoint-continued
bra branch `Ktilde(w) = [K_pointer(conj w)]^dagger` antiholomorphic-to-
holomorphic in w; recorded per addendum F4 as a majorant-supplier obligation
of record), restricting to `zhat_c,K` on real pairs. (H1) presupposes and
extends B0 (D-7).

(H2) [D-2/D-3 restatement; = battery T7(iii)] With the log branch anchored
at `Ghat_K(0,0) = 1`, the intensive logs `gamma_K := -Log Ghat_K / N_4(K)`,
`N_4(K) := |X(K)|_4` (cellulation 4-volume, D-3), satisfy
(i) `sup_K sup_P |gamma_K| <= Gamma_* < infinity`; and
(ii) `gamma_K` converges pointwise on a PRODUCT set `E_1 x E_2 subset P_open`
with each factor having an accumulation point in the open disc (canonical
choice: the real bidisc slice).

STEP 0 (branch anchoring uses only (H1) and simple connectivity). The open
polydisc is simply connected and `Ghat_K` is holomorphic and zero-free on a
neighborhood of the closed polydisc P by (H1). Hence `Ghat_K'/Ghat_K`
(in each variable) is holomorphic on P and the primitive

    Log Ghat_K(z,w) := integral over any path in P from (0,0) to (z,w) of
                       d(Ghat_K)/Ghat_K,

is single-valued (path-independence: P is simply connected — even convex —
and the integrand is a closed holomorphic 1-form there), holomorphic, and
satisfies `exp(Log Ghat_K) = Ghat_K`, `Log Ghat_K(0,0) = 0`. No K-uniform
floor is used in this step (the review's decisive D-1 finding: the schema
proof never needed one). gamma_K is then jointly holomorphic on the open
polydisc and bounded by Gamma_* on P by (H2)(i).

STEP 1 (Montel). {gamma_K} is uniformly bounded by Gamma_* on P, hence a
normal family on the open polydisc `D_1 x D_2` (Montel in several variables:
uniform boundedness gives local equicontinuity via the Cauchy estimates on
polydiscs strictly inside P — for (z,w), (z',w') in the closed polydisc of
radius r < epsilon_*, |gamma_K(z,w) - gamma_K(z',w')| <=
Gamma_* [ |z-z'| + |w-w'| ] * epsilon_* / (epsilon_* - r)^2 — and then
Arzela-Ascoli on a compact exhaustion with a diagonal argument).

STEP 2 (iterated one-variable Vitali on the product set; D-2). Fix `w in
E_2`. The one-variable family `z -> gamma_K(z,w)` is holomorphic on D_1,
uniformly bounded by Gamma_*, and converges pointwise on E_1, which has an
accumulation point in D_1. By the Vitali-Porter theorem it converges locally
uniformly on all of D_1. Hence gamma_K converges pointwise on `D_1 x E_2`.
Now fix `z in D_1`. The family `w -> gamma_K(z,w)` is holomorphic on D_2,
uniformly bounded, and converges pointwise on E_2, which has an accumulation
point in D_2; Vitali-Porter again gives locally uniform convergence on D_2.
Hence gamma_K converges POINTWISE ON ALL OF `D_1 x D_2`. (The sealed text's
accumulation-point-per-variable clause is void per D-2; the review
counterexample `i(-1)^K (z-w)` on the diagonal shows a non-product set with
per-variable accumulation does not suffice.)

STEP 3 (from pointwise to locally uniform; Osgood/normal-family argument).
Let S be any subsequence of {gamma_K}. By Step 1 (normality) S has a further
subsequence converging locally uniformly on D_1 x D_2 to some holomorphic
limit (holomorphy of the limit: locally uniform limits of holomorphic
functions are holomorphic — Osgood/Weierstrass; in several variables via
the Cauchy integral on product contours). By Step 2 every such limit agrees
with the pointwise limit gamma_inf on all of D_1 x D_2, so all subsequential
limits coincide with gamma_inf. A normal family whose subsequential limits
all coincide converges locally uniformly to that common limit (else some
neighborhood of some compact set and some epsilon witness a subsequence
staying epsilon-away, which itself has a convergent sub-subsequence —
contradiction). Hence `gamma_K -> gamma_inf` locally uniformly on
`D_1 x D_2` and gamma_inf is jointly holomorphic.

STEP 4 (Cauchy representation; derivative convergence). Fix any
`0 < r < epsilon_*` and any multi-index (m,n). For (z,w) in the open
polydisc of radius r' < r,

    d^m_z d^n_w gamma_K(z,w)
      = (m! n! / (2 pi i)^2) contour-integral over |u|=r, |v|=r of
        gamma_K(u,v) / [(u-z)^(m+1) (v-w)^(n+1)] du dv ,

and locally uniform convergence of gamma_K on the compact distinguished
boundary torus passes the limit through the integral (dominated by
sup-norm convergence; the kernel is bounded on |u| = r, |v| = r,
|z|,|w| <= r'). Hence EVERY mixed partial derivative converges, locally
uniformly, to the corresponding derivative of gamma_inf. In particular the
interchange of the intensive limit with the Hessian is VALID:

    lim_K [ d_+ d_- (-log Ghat_K) / N_4(K) ] |_(0,0) = d_+ d_- (-gamma_inf)|_(0,0).

STEP 5 (FK-2 transported term-by-term; D-9 reading). Each of `H_att,K`,
`g_(D,c,K)`, `(log q_K)''(0)` is (a real-linear combination of) second
derivatives at the origin of the SAME uniformly controlled family
`-Log Ghat_K` (restricted to real pairs and the diagonal respectively:
mixed derivative; `-Re` of the (2,0) derivative; diagonal second
derivative). By Step 4 each of the three normalized limits exists
separately, and the finite-K identity FK-2 (Section 3), which holds exactly
at every K, passes to the limit:

    R_record = lim_K H_(att,K)/N_4(K)-normalized
             = lim_K g_(D,c,K)-density - (1/2) lim_K (log q_K)''-density,

with all three limits existing and the equality exact. The identification
of the g-density limit with the V011 `G_L`-computed Duhamel covariance is
IMPORTED through interface I3 (tuple V002 of the amendment Part III) and is
NOT proved here.

USED: (H1), (H2)(i), (H2)(ii) product form, C1/C2 (for the finite-K FK
identities being transported), finite-dimensional holomorphy, Montel,
Vitali-Porter, Osgood/Weierstrass, Cauchy integrals. NOT USED: clustering,
decay, any property of the actual parent, any exhaustive-chain zero-free
result (F2.1), the periodic zero-free lineage (F2.5), any K-uniform lower
floor. The adoption fence S5.3 was not approached: neither (H1) nor (H2)
was discharged, assumed, or interpolated; the flag
`Duhamel_intensive_Hessian_equality_proved` remains false.

## 8. Negative-control derivations (S6, directions predeclared)

8.1 GHZ witness (must BLOCK). For `Z_N(A) = cos(N tau_R A)`,
`tau_R = pi/sqrt(2)` (`f891d3af...`), the first zero is at
`A = pi/(2 N tau_R) = 1/(sqrt(2) N)`. For ANY common `epsilon_* > 0` and all
`N > 1/(sqrt(2) epsilon_*)` the zero lies strictly inside the closed
polydisc (exact integer/rational comparison `1 < 2 N^2 epsilon_*^2`), so
per-K zero-freeness at a common epsilon_* (the amended (H1)) FAILS for
cofinally many members: checker verdict `H1_VIOLATED`; the schema REFUSES
and emits BLOCKED naming the violated structural premise — independent
record colors (the GHZ preparation `(|0...0>+|1...1>)/sqrt(2)` is the
perfectly-correlated-color limit). Producing a limit on this witness would
be a pipeline falsifier; none was produced.

8.2 V010 zero stiffness (stays failed). `kappa_L = 1/[4 L^4 sin^2(pi/L)]`
(V011 line 1243). Exact bound: for L >= 2, Jordan's inequality gives
`sin(pi/L) >= 2/L`, so `4 L^4 sin^2(pi/L) >= 16 L^2` and
`0 < kappa_L <= 1/(16 L^2) -> 0`. Failed stays failed; no post-hoc
extensive factor is applied (V011: multiplying by L^2, L^4, cell count, or
cell volume is a fail).

8.3 Contact-term / ordering / wrong-form teeth: executed numerically on F-A
(Section 9 of the JSON record): (a) omission of the exact contact term
shifts H_att by the state-evaluated contact term (predicted at second
order); the discrepancy enclosure intersects the independently integrated
contact-term enclosure and exceeds 3x the stencil radius by four orders.
(b) pair-evaluated reading (addendum A1): `Im z_c(7/100, -11/100)` excludes
zero and flips sign exactly under the ordering swap; the two orderings
mismatch by `2|Im z_c|`, exceeding 3x the combined radius by four orders.
(The baseline reading `Im<X_0, eta>` is unsatisfiable on F-A by exact
fixture symmetry; named witness S63B_D5_BASELINE_READING_UNSATISFIABLE_ON_FA
retained.) (c) the flat-diagonal (exhaustive-typed) stencil differs from
g_(D,c) by `(1/2)|(log q)''| ~ 5.1e-2`, with the `(log q)''` enclosure
excluding zero — F2.2 is mechanical.

## 9. What is and is not claimed

Derived here, per fixture and per pinned state, conditional on B0 (and C1
where invoked) and C2: the finite bundle {FK-1, FK-2, FK-3}, L-ADD with its
endpoint form, and the conditional interchange schema on the amended
hypotheses. NOT derived: a volume-uniform zero-free neighborhood ((H1)); a
linked-cluster density ((H2)); any unconditional Duhamel/intensive-Hessian
equality; any statement about the actual parent's continuum; kappa_record;
a coupling; alpha. The F-C conditioned-crosscheck leg is the standing
victory-class ordering block `F_C_INPUT_BUNDLE_NOT_YET_SEALED` (addendum
A2/F2): no Phase-A sealed result bundle exists and this gate forbids a
production run; the leg runs against the exact sealed bundle hashes once
Phase-A production seals.

Protected status (unchanged except the three S8 verdict components,
recorded in the JSON):

    completed_chain_finite_conditioned_identity_derived : see JSON verdict
    conditional_interchange_schema_sealed               : see JSON verdict
    additive_hessian_mixing_lemma_sealed                : see JSON verdict
    C1_affine_tangent_lemma_derived = true (this gate)
    C2_boundary_history_independence_lemma_derived = true (this gate)
    volume_uniform_zero_free_neighborhood_proved = false   # (H1) underived
    connected_linked_cluster_density_proved = false        # (H2) underived
    Duhamel_intensive_Hessian_equality_proved = false      # false even on pass
    A4_3_erratum_sealed = false
    ER_fork_closed = false
    kappa_record_computed = false
    physical_Thomson_stiffness_computed = false
    coupling_evaluation_authorized = false
    alpha_computed = false
    proof_authorized = false
