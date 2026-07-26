# Duhamel-Gate Formal Derivations Draft V001 (primary execution lane)

Date: 2026-07-25 (primary execution lane, fresh context)
Governing texts:
`STAGE8_T7_COMPLETED_CONDITIONED_DUHAMEL_IDENTITY_AND_INTERCHANGE_SCHEMA_SPEC_V001.md`
as amended by `STAGE8_T7_D6_SPECS_REPAIR_AMENDMENT_V001.md` (the amendment
GOVERNS where it differs). All hashes of the frozen authority table and the
amendment-added authority were verified before any other action (M1).

Status: DRAFT execution artifact of the primary lane. No .seal files are
emitted by this lane; the construction lane seals only after the verifier
comparison. Exact arithmetic was used wherever the claim is decidable;
certified outward enclosures otherwise; no measured constant was consulted;
no coupling, kappa_record, or alpha target was read.

This document contains the M7 formal lane in full: the symbolic
re-derivations of FK-1, FK-2, FK-3, L-ADD, the C1/C2 hypothesis-lemma
verifications of S2, and the complete two-variable Vitali-Cauchy schema
proof of S5.2 on the AMENDED hypotheses (D-1 per-K zero-freeness; D-2
product-set convergence; D-3 N_4 := |X|_4). Machine verification of every
displayed algebraic identity was executed in exact Gaussian-rational
arithmetic (a minimal multivariate polynomial engine over Fraction
coefficients with a conjugation involution and q*q^-1 -> 1 localization;
no floating-point number decides any claim in this document).

---

## 1. Setting and frozen objects (S1, restated with the amended labels)

Per member `K` of the relayed causally-sequential exhaustion, per pinned
state `rho` (density operator; pure case `rho = |psi><psi|`):

```text
V_K[A] = W_K[A] i_r ;    Q = I_S tensor Q_comp ,  Q = Q^dagger = Q^2 ;
X_K(a) = Q V_K[A^(a)] rho^(1/2)  in  HS(H_S, H_S tensor H_R) ;
z_c,K(a_+,a_-) = omega( V_K[A_-]^dagger Q V_K[A_+] )
              = < X_K(a_-), X_K(a_+) >_HS .
```

The ordering label is the unified frozen display (amendment D-6/D-9):
`omega(V[A_-]^dagger Q V[A_+])` — the PLUS history stands on the ket
(right, forward) branch, the MINUS history on the bra branch under the
adjoint. Hermitian symmetry for real histories is exact:
`z_c,K(a_+,a_-)^* = z_c,K(a_-,a_+)` (O4 adjoint exchange, state-evaluated).

Diagonal (NOT flat on this chain): `q_K(a) := z_c,K(a,a) = ||X_K(a)||^2`.
Normalization anchor (hypothesis, never a structural identity):
`zhat_c,K := z_c,K / q_K(0)` under

```text
B0(K, rho):  q_K(0) != 0        [ = T7(ii) at fixed finite K; F2.3 ].
```

Per amendment D-7: (H1) presupposes and extends B0 (the verb "subsumes" is
replaced). Per D-3: `N_4(K) := |X(K)|_4`, the cellulation 4-volume, with
the unit-cell-skeleton equivalence to V011's 4-cell count recorded.

Sealed input (S3.1): the O5 operator Duhamel tangent, derived for
`Q = Q_comp` in `STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_EXACT_DERIVATION_
V001.md` D5 (finite-dimensional norm-`C^1` Duhamel differentiability),

```text
delta V = -i integral_0^T W(T,t) J_a(t) W(t,0) dt  i_r ;
eta := Q (delta V) rho^(1/2) ;   X_0 := X_K(0) ;   q := q_K(0) .
```

First derivatives of the Gram form are exact:

```text
d_(a_+) z_c |_0 = <X_0, eta> ;  d_(a_-) z_c |_0 = <eta, X_0> ;
d_(a_+) d_(a_-) z_c |_0 = <eta, eta> .
```

Machine check (exact): the degree-2 Taylor expansion of
`<X(a_-), X(a_+)>` with `X(a) = X_0 + a eta + (1/2) a^2 zeta` reproduces
these coefficients identically (polynomial identity in the ring generated
by the Gram data).

---

## 2. S2 — Hypothesis-lemmas C1 and C2 (proof obligations discharged)

### 2.1 C1 (branch generators affine in the branch tangent at baseline) — DERIVED

**Claim.** For every branch label `lambda` and admitted history direction
`a`, the Phase-A one-particle generator family is affine in the history
parameter at baseline, with the same `J(t)` for every `lambda`.

**Proof.** The sealed Phase-A A2 frozen form (`789338ad...` A2) is,
verbatim,

```text
h_(lambda,n,ell)(t;a) = h_(0,n,ell) + lambda v(t) M_(n,ell)(t) tensor S_n
                        + a J_(n,ell)(t),
J_(n,ell)(t) = -B_(D,n,ell)(t) tensor alpha_x .
```

As a polynomial in `a` with operator coefficients this expression has
degree exactly 1; hence `d^2 h_lambda(t;s)/ds^2 = 0` identically, and the
coefficient of `a` is `J_(n,ell)(t) = -B_(D,n,ell)(t) tensor alpha_x`,
which contains neither `lambda` nor `a` (nor `s`): the same `J` multiplies
the history at every branch. Machine check: symbolic second derivative of
the frozen form vanishes identically (exact). **C1 DERIVES** on the
Phase-A generator. QED.

**Recorded falsification channel (binding on successors, non-blocking
here).** A V011 link-holonomy generator depends on the connection through
`exp(i integral A)`-type factors and is not affine; its second history
derivative contributes a contact term. Concretely, on the sealed
three-site fixture generator `h_source(theta) = -i D_theta tensor alpha_x`
with phases `exp(+-i theta/3)`, the exact second derivative at baseline is

```text
d^2 D_theta / dtheta^2 |_0 : [j,j+1] = -1/18 ,  [j,j-1] = +1/18   (exact),
```

which is nonzero (machine-verified in exact Gaussian-rational arithmetic).
This spec exploits that fact as the S6.3(a) contact-term negative control;
C1 is quantified over the completed Phase-A chain only, and the fixture's
curvature term is included exactly wherever the fixture is used (see the
execution record: the second-order tangent ODE carries
`K = dGamma(P h''(0) P)` on every F-A conditioned run).

### 2.2 C2 (history-independence of boundary data along the relayed exhaustion) — DERIVED

**(a) Ready injections.** Phase-A A3 (`789338ad...`): `|ready> = |0>` on
the qutrit record factor; the injection is `psi -> psi tensor |ready>`.
The display contains no connection argument. The sealed O5 gate
(`2f2aa7f7...` O5) already freezes the ready injection as
history-independent boundary data and BLOCKS if it varies ("its
derivative must be added and this specification blocks"). DERIVED by
inspection of the sealed displays.

**(b) Final PVMs and Q_comp.** Phase-A A3 constructs the record spectral
resolution from the fixed matrix
`c = [[0,0,-i],[0,0,+i],[+i,-i,0]]` — spectral projectors `P_lambda`,
`lambda in {-sqrt(2),0,+sqrt(2)}`; the O7 finite PVM is
`{|xi><xi| : xi in {0,1,2}^2}` with completed subset `{(1,1)}`. Neither
carries any `A` argument. DERIVED by inspection.

**(c) Relay isometries.** The relayed family resolution
(`52401eef...`) and the relay-necessity result (`0df721a1...`) construct
the relay binding member `K` to its successor from incidence projectors
(exact rational `Tr(P_0 P_1) = Tr(P_1 P_2) = 1/4`, `Tr(P_0 P_2) = 0`) and
typed tuple maps `L_(p_c) -> L_(r_(c+1))`; no display carries a history
argument. The relay preserves the completed record while supplying the
next ready root; its construction data are incidence/typing data only.
DERIVED by inspection of the sealed constructions.

**(d) Envelope clause (gamma memo condition 3(3)(d), `da6d8cc7...`).**
Over the declared ER envelope-profile class, the envelope profile enters
the generator ONLY through the scalar `v(t)` multiplying the `lambda`
write term (`789338ad...` A1: `v(t) = (pi/sqrt(2)) 32 r(t)^3`; A2 display
above). The ready injection (a), the PVM (b), and the relays (c) contain
no envelope profile dependence whatsoever. Hence (a)-(c) hold uniformly
over the envelope-profile class: envelope-independence is part of the
hypothesis, stated and verified, not assumed. DERIVED by inspection.

**Recorded falsification channel.** Any future gauge-covariance
completion transports the carrier by `exp(i chi)` and makes the injection
history-dependent in the transformed frame; C2 must then be re-derived,
not assumed (Phase-A A2 records the same caveat: fixed-gauge finite
response diagnostic, no local gauge covariance claimed).

**Role discharged.** C2 guarantees the O5 tangent has no
boundary-derivative terms, so the conditioned tangent of S3 is exactly
the compressed Duhamel integral, and the multi-cell composition retains
the same form along the exhaustion (interface to the majorant spec's
LEMMA 0, named in I3 V002 below).

---

## 3. S3 — The finite-K conditioned identity bundle (derivations in full)

All statements are per member `K`, per pinned state, under B0 and C2
(FK-2 additionally under C1 or with the contact term explicitly
included). All are finite-dimensional exact algebra on the sealed
objects.

### 3.1 FK-1 (mixed-CTP conditioned-covariance normal form; primary)

**Statement.** Under B0 and C2:

```text
g_(D,c,K) := d_(a_+) d_(a_-) log z_c,K |_(0,0)
  = <eta,eta>/q - <eta,X_0><X_0,eta>/q^2
  = [ <eta,eta><X_0,X_0> - |<X_0,eta>|^2 ] / q^2 .
```

**Derivation.** From the Gram derivatives of Section 1,

```text
d_+ d_- log z_c = [ z_c (d_+ d_- z_c) - (d_+ z_c)(d_- z_c) ] / z_c^2
   at (0,0):    = <eta,eta>/q - <X_0,eta><eta,X_0>/q^2 .
```

The ratio form is the same expression over the common denominator `q^2`.
Machine check (exact): with the truncated series
`z = q + a_+ al + a_- al^* + a_+ a_- n + (1/2)a_+^2 c_2 + (1/2)a_-^2
c_2^*` (the general hermitian-symmetric second-order Taylor ansatz; the
ansatz's hermitian symmetry `z(a_+,a_-)^* = z(a_-,a_+)` was itself
machine-verified), the mixed coefficient of `log z` equals
`n q^{-1} - al al^* q^{-2}` identically, and the ratio form is the same
polynomial. This is the conditioned-covariance normal form mandated by
freeze fence F2.3.

**Structural facts (verified, not assumed).**

```text
(P1) Reality: the mixed coefficient g is fixed by the conjugation
     involution (machine check: g - conj(g) == 0 identically, given
     hermitian symmetry). 
(P2) Positivity: by Cauchy-Schwarz on the HS inner product,
     <eta,eta><X_0,X_0> >= |<X_0,eta>|^2, with equality iff eta is
     parallel to X_0. Hence g_(D,c,K) >= 0, equality iff parallel.
     Positivity of the MIXED form is structural on this chain; no claim
     attaches to one-branch weak-value forms. (Numerically witnessed
     strictly positive on F-A; see execution record.)
(P3) Reduction: at Q = I_R, q = 1, pure rho: X_0 = |Psi_0>, eta = |eta>,
     and FK-1 reduces to g_D = <eta|eta> - |<psi|eta>|^2, the sealed
     exhaustive form of the crosscheck protocol (3d86dc4f...). This
     reduction is an executable control only; fences F2.1/F2.2 forbid
     transporting exhaustive results to the completed chain.
(P4) Degenerate endpoint: rank-one completed compression forces eta
     parallel to X_0, hence g_(D,c) = 0 exactly (machine-verified on the
     Route-1 comparator in exact arithmetic: g_c = 0).
```

### 3.2 FK-2 (attenuation corollary with the diagonal correction)

**Statement.** Under B0, C2, and the full second-order Duhamel expansion
(under C1 the contact term vanishes; otherwise it must be included):

```text
H_(att,K) := -Re d^2_(a_+) log z_c,K |_(0,0)
           = g_(D,c,K) - (1/2) d^2/da^2 log q_K(a) |_(a=0) .
```

**Derivation.** Write the exact second-order Taylor coefficients of
`L := log z_c` at `(0,0)` for real histories:

```text
L(a_+,a_-) = L_0 + alpha a_+ + conj(alpha) a_-
             + (1/2) L_(++) a_+^2 + (1/2) conj(L_(++)) a_-^2
             + g_(D,c,K) a_+ a_- ,
```

where hermitian symmetry forces the displayed conjugations and the
reality of the mixed coefficient (both machine-verified on the general
ansatz). Restricting to the diagonal:

```text
log q(a) = L(a,a)  =>  (log q)''(0) = 2 Re L_(++) + 2 g_(D,c,K)
        =>  -Re L_(++) = g_(D,c,K) - (1/2)(log q)''(0) .
```

Machine check (exact): the coefficient of `a^2` in `L(a,a)` equals
`(1/2)(L_(++) + conj(L_(++))) + g` identically in the polynomial ring,
and the rearrangement to the FK-2 statement is likewise an identity.

Second-derivative content from the sealed second-order Duhamel expansion:

```text
delta^2 V = 2 (-i)^2 integral_(T>=t>s>=0) W(T,t) J(t) W(t,s) J(s) W(s,0) dt ds  i_r
            + (-i) integral_0^T W(T,t) [d^2 H_s(t)/ds^2] W(t,0) dt  i_r ,
```

whose second line is the CONTACT TERM: it vanishes exactly under C1
(Section 2.1) and is computed exactly whenever the generator is
non-affine (three-site fixture: `K = dGamma(P h''(0) P)`, carried in the
second-order tangent ODE `zeta' = -i H_0 zeta - 2i J eta - i K psi`).
With `zeta := Q (delta^2 V) rho^(1/2)`: `d^2_(a_+) z_c|_0 = <X_0,zeta>`,
so `L_(++) = <X_0,zeta>/q - (<X_0,eta>/q)^2` (machine-verified). The
algebraic step connecting the diagonal identity to the covariance uses

```text
Re[c^2] = 2 (Re c)^2 - |c|^2      applied to  c = <X_0,eta> ,
```

machine-verified as the polynomial identity `x^2 - y^2 = 2x^2 -
(x^2+y^2)` in the real coordinates of `c`.

**Stencil realization.** With `zhat_c = z_c/q` (B0),

```text
H_(att,K) = lim_(h->0) [ -log|zhat_c(h,0)| - log|zhat_c(-h,0)| ] / h^2 :
```

by the Taylor display, `log|zhat_c(h,0)| = Re L(h,0) - log q =
(Re alpha) h + (1/2)(Re L_(++)) h^2 + O(h^3)`, so the symmetric sum
cancels the odd term and the stencil converges to `-Re L_(++)` — the
completed-chain re-typing of the sealed `H_CTP` stencil. The
un-normalized stencil diverges (adds `-2 log q / h^2`), the finite shadow
of the missing unitality anchor; this is why the normalization `zhat_c`
(hence B0) is load-bearing.

On the exhaustive chain `q(a) == 1` identically, the correction term
vanishes, and only then does the stencil equal the covariance — the
exact reason the exhaustive three-way agreement could equate them (fence
F2.2 made mechanical; enforced by control S6.3(c)).

### 3.3 FK-3 (Fubini-Study corollary on the completed output ray)

**Statement.** Under B0 and C2, the FS pullback of the normalized
completed output ray `Xhat(a) := X(a)/||X(a)||` at baseline equals the
conditioned covariance exactly:

```text
g_FS(completed ray)|_(a=0) = <X'(0),X'(0)>/q - |<Xhat(0),X'(0)>|^2/q
                           = g_(D,c,K) .
```

**Derivation.** For the curve `a -> X(a)` with `X'(0) = eta`,
`||X(0)||^2 = q`, the projective FS pullback is

```text
g_FS = [ <eta,eta> ||X_0||^2 - |<X_0,eta>|^2 ] / ||X_0||^4
     = [ <eta,eta> q - |<X_0,eta>|^2 ] / q^2 = g_(D,c,K) ,
```

using `<Xhat_0, eta> = <X_0,eta>/sqrt(q)` so that
`|<Xhat_0,eta>|^2/q = |<X_0,eta>|^2/q^2` (machine-verified as a
polynomial identity in the localized ring). This realizes battery T9 on
the completed chain exactly as V011 1300-1302 requires: the FS check
anchors on each normalized local COMPLETED output ray. The FS of the
full (exhaustive) output ray is a different number (it equals `g_all`);
conflation is an F2.2 violation, caught by control S6.3(c).

### 3.4 Scope of the bundle (S3.5, unchanged)

Pass of S3 derives {FK-1, FK-2, FK-3} per fixture and per pinned state,
conditional on B0, C1 (where invoked), C2. It does NOT derive: a
volume-uniform zero-free neighborhood; a linked-cluster density; any
intensive limit; any unconditional Duhamel/intensive-Hessian equality;
any statement about the actual parent's continuum. The flag
`Duhamel_intensive_Hessian_equality_proved` remains `false` on pass.

---

## 4. S4 — L-ADD (the additive Hessian-mixing lemma; freeze F2.4)

**Statement (exact).** With `z_all = z_c + z_r` (O3/D2 completeness,
state-evaluated), `z_all(0,0) = 1` (exhaustive unitality),
`q := z_c(0,0) in (0,1)`, `zhat_c = z_c/q`, `zhat_r = z_r/(1-q)`,
`alpha_c := d_(a_+) log zhat_c|_0`, `alpha_r := d_(a_+) log zhat_r|_0`,
and `g_c, g_r, g_all` the FK-1 mixed log-Hessians of the respective
functionals:

```text
L-ADD:   g_all = q g_c + (1-q) g_r + q(1-q) |alpha_c - alpha_r|^2 .
```

**Derivation.** At baseline `z_all = 1`:

```text
d_+ z_all|_0 = q alpha_c + (1-q) alpha_r ;
d_+ d_- z_all|_0 = q (g_c + |alpha_c|^2) + (1-q)(g_r + |alpha_r|^2) ;
g_all = d_+ d_- z_all - (d_+ z_all)(d_- z_all)
      = q g_c + (1-q) g_r
        + [ q|alpha_c|^2 + (1-q)|alpha_r|^2
            - |q alpha_c + (1-q) alpha_r|^2 ]
      = q g_c + (1-q) g_r + q(1-q)|alpha_c - alpha_r|^2 ,
```

the last step being the two-point variance decomposition with weights
`(q, 1-q)`. Machine check (exact): with
`z_c = q(1 + a_+ alpha_c + a_- alpha_c^* + a_+ a_- (g_c +
|alpha_c|^2))` and the analogous `z_r`, the mixed log coefficient of
`z_c + z_r` equals `q g_c + (1-q) g_r + q(1-q)(alpha_c - alpha_r)
(alpha_c^* - alpha_r^*)` identically in the polynomial ring.

**Degenerate endpoint `q = 1` (stated separately; the generic formula
requires `q != 1`).** There `X_r(0) = 0`, so `d_+ z_r|_0 = 0` while
`d_+ d_- z_r|_0 = ||eta_r||^2` need not vanish:

```text
g_all = g_c + ||eta_r||^2        (q = 1) .
```

Machine check (exact): with `z_c` as above at `q = 1` and
`z_r = a_+ a_- ||eta_r||^2`, the mixed log coefficient of the sum equals
`g_c + ||eta_r||^2` identically.

**Consequences recorded (the lemma equates nothing).** (i) the completed
and exhaustive mixed Hessians differ by
`(1-q)(g_r - g_c) + q(1-q)|alpha_c - alpha_r|^2`; no sealed identity
equates them. (ii) On the Route-1 comparator the attenuation-level
coincidence is reproduced WITHOUT Hessian equality — all six anchors
were verified in exact rational arithmetic (execution record, M4):

```text
g_c = 0 ;  (log q_c)''(0) = -1/2 ;  H_att,c = 1/4 ;
g_all = 1/4 ;  H_att,all = 1/4 ;  g_all - g_c = ||eta_r||^2 = 1/4 ;
```

with the sigma-witness curvatures (1/4, 1/4, 1/2, 0) reproduced exactly
against `e12fffcc...`/`52401eef...`. (iii) Auditability: any pipeline
claiming a completed Hessian obtained from an exhaustive computation
must violate L-ADD unless `q = 1`; the L-ADD residual runs as a check on
every executed fixture (M5).

---

## 5. S5.2 — The conditional interchange theorem schema (full proof on the AMENDED hypotheses)

### 5.1 Hypotheses (as amended; named underived inputs — NOT derived, NOT assumed, NOT discharged here)

Let `epsilon_* > 0` and let
`P = { (z,w) in C^2 : |z| <= epsilon_*, |w| <= epsilon_* }` (closed pair
polydisc; per amendment M-2 the per-cell histories are CTP pairs and the
bra branch is complexified by the adjoint-continued convention
`Ktilde(w) = [K_pointer(conj w)]^dagger`, making
`G_K(z,w) := omega( Ktilde(w) K(z) )` jointly holomorphic with
restriction to real pairs equal to `z_c,K`).

```text
(H1) [D-1; = battery T7(ii) restated]  PER-K ZERO-FREENESS: for every
     member K of the relayed exhaustion, Ghat_K (the normalized pair-
     holomorphic extension of zhat_c,K) is zero-free on the closed
     polydisc P at the COMMON epsilon_*. Any quantitative floor is
     K-DEPENDENT (e.g. >= exp(-N_4(K) Gamma_*)); NO K-uniform delta is
     hypothesized (the uniform delta of the sealed text is DELETED
     everywhere; it is not used below, and it is undischargeable
     whenever the intensive attenuation Hessian is nonzero). (H1)
     presupposes and extends B0 (D-7).

(H2) [= battery T7(iii)]  With the log branch anchored at
     Ghat_K(0,0) = 1, the intensive logs
         gamma_K := -Log Ghat_K / N_4(K),    N_4(K) := |X(K)|_4  (D-3),
     satisfy:
     (i)  sup_K sup_P |gamma_K| <= Gamma_* < infinity ;
     (ii) [D-2] gamma_K converges pointwise on a PRODUCT SET
          E_1 x E_2 subset of the open polydisc, where each factor E_j
          has an accumulation point in the open disc
          D = { |z| < epsilon_* }  (the real bidisc slice is the
          canonical choice), to a limit gamma_inf.
```

Plus C1 and C2 uniformly along the exhaustion (Section 2; they enter
only through the finite-K identity bundle being transported, never
through the complex-analytic argument below).

The sealed text's accumulation-point-per-variable clause is VOID (D-2);
the hostile review's counterexample is recorded in Step 3 below.

### 5.2 Theorem (conditional; derived here)

Assume (H1), (H2), C1, C2. Then `gamma_K -> gamma_inf` locally uniformly
on the open polydisc `P^o`; `gamma_inf` is jointly holomorphic; every
mixed partial derivative of `gamma_K` at every point of `P^o` converges
to that of `gamma_inf`; and in particular the interchange of the
intensive limit with the Hessian is VALID:

```text
lim_K  [ d_+ d_- (-log Ghat_K) / N_4(K) ] |_(0,0)
   =  d_+ d_- (-gamma_inf) |_(0,0) .
```

Via FK-2 transported term-by-term — read, per D-6/D-9, as three
separately normalized limits per the display — the intensive attenuation
Hessian equals the thermodynamic conditioned Duhamel covariance minus
the intensive diagonal correction:

```text
lim_K H_(att,K)/N_4(K)  =  lim_K g_(D,c,K)/N_4(K)
                           - (1/2) lim_K (log q_K)''/N_4(K) ,
```

with all three limits existing and the equality exact. The
identification of the `g_(D,c,K)`-density limit with the V011
`G_L`-computed Duhamel covariance is IMPORTED through interface I3
(Route B-L5 cluster resummation under the item-3 majorant) and is NOT
proved by this schema.

### 5.3 Proof

**Step 1 (holomorphic logarithm; uses (H1) and convexity only).**
`P^o` is a convex, hence contractible, domain in `C^2`. By (H1), each
`Ghat_K` is holomorphic and zero-free on (a neighborhood of) `P`. The
form `omega_K := dGhat_K / Ghat_K` is a holomorphic closed 1-form on
`P^o` (closedness: `d(dG/G) = -(dG ^ dG)/G^2 = 0`). On a contractible
domain every closed holomorphic 1-form is exact: there is a holomorphic
`L_K` with `dL_K = omega_K`. Then `d( Ghat_K e^{-L_K} ) = 0`, so
`Ghat_K = c e^{L_K}`; fixing the constant by `Ghat_K(0,0) = 1` and
`L_K(0,0) = 0` defines the anchored branch `Log Ghat_K := L_K`,
single-valued and holomorphic on `P^o`. Only zero-freeness (per-K; no
uniform floor is used at any point of this proof) and simple
connectivity are used. Define `gamma_K = -L_K / N_4(K)`, holomorphic on
`P^o`.

**Step 2 (normal family; uses (H2)(i)).** By (H2)(i),
`sup_K sup_{P} |gamma_K| <= Gamma_*`. For any closed sub-polydisc
`P_r = {|z| <= r, |w| <= r}` with `r < epsilon_*`, the two-variable
Cauchy integral over the distinguished boundary
`T_rho = {|zeta_1| = rho} x {|zeta_2| = rho}`, `r < rho < epsilon_*`,

```text
gamma_K(z,w) = (2 pi i)^{-2} oint oint
   gamma_K(zeta_1,zeta_2) / [(zeta_1 - z)(zeta_2 - w)] dzeta_1 dzeta_2 ,
```

gives the derivative bounds
`|d gamma_K| <= Gamma_* rho^2 / (rho - r)^2` on `P_r`, uniformly in `K`.
Hence `{gamma_K}` is uniformly bounded and equicontinuous on every
compact subset of `P^o`; by Arzela-Ascoli and a diagonal argument over a
compact exhaustion, every subsequence has a locally uniformly convergent
sub-subsequence whose limit is holomorphic (Weierstrass; the Cauchy
representation passes to the limit). This is Montel's theorem in two
variables, derived, not cited.

**Step 3 (iterated one-variable Vitali plus Osgood; uses (H2)(ii) on
the PRODUCT set).** We first prove the one-variable Vitali-Porter lemma
we use twice.

*Lemma (one-variable Vitali-Porter, derived).* Let `{f_n}` be
holomorphic on the disc `D`, `|f_n| <= M`, converging pointwise on a set
`E subset D` with an accumulation point `p in D`. Then `f_n` converges
locally uniformly on `D`.
*Proof.* By the one-variable Montel theorem (same Cauchy-estimate
argument as Step 2), `{f_n}` is normal. Let `f, g` be limits of two
locally uniformly convergent subsequences. On `E`, both equal
`lim f_n`, so `f = g` on `E`; `f - g` is holomorphic on the connected
domain `D` and vanishes on a set with an accumulation point in `D`,
hence `f - g == 0` by the identity theorem. If `f_n` failed to converge
locally uniformly, there would be a compact `C`, an `epsilon > 0`, and a
subsequence with `sup_C |f_{n_k} - f| >= epsilon`; by normality it has a
locally uniformly convergent sub-subsequence, whose limit must be `f`
(previous paragraph) — contradiction. QED (lemma).

Now iterate on the product set `E_1 x E_2`:

*(3a) Convergence in the first variable.* Fix `w_0 in E_2`. The family
`z -> gamma_K(z, w_0)` is holomorphic on `D`, bounded by `Gamma_*`, and
converges pointwise on `E_1` (accumulation point in `D`). By the lemma,
`gamma_K(., w_0)` converges locally uniformly on `D`. Hence `gamma_K`
converges pointwise on `D x E_2`.

*(3b) Convergence in the second variable.* Fix any `z in D`. The family
`w -> gamma_K(z, w)` is holomorphic on `D`, bounded by `Gamma_*`, and by
(3a) converges pointwise on `E_2` (accumulation point in `D`). By the
lemma again, it converges locally uniformly on `D`. Hence `gamma_K`
converges pointwise EVERYWHERE on `P^o = D x D`.

*(3c) Joint local uniformity and holomorphy of the limit (Osgood step).*
The pointwise limit `gamma_inf` on `P^o` is a pointwise limit of a
family that is normal by Step 2. If `gamma_K` failed to converge locally
uniformly to `gamma_inf`, some compact `C subset P^o`, `epsilon > 0`,
and subsequence would satisfy `sup_C |gamma_{K_j} - gamma_inf| >=
epsilon`; by Step 2 that subsequence has a locally uniformly convergent
sub-subsequence, whose limit is holomorphic and must agree with
`gamma_inf` pointwise (by (3b)) — contradiction. Hence `gamma_K ->
gamma_inf` locally uniformly on `P^o`, and `gamma_inf` is jointly
holomorphic (uniform limits of holomorphic functions on polydiscs are
holomorphic: the Cauchy representation passes to the limit — Osgood/
Weierstrass).

*Necessity of the product-set form (review counterexample, recorded).*
`gamma_K(z,w) := i(-1)^K (z - w)` is uniformly bounded on `P`, and
converges pointwise (indeed is identically zero) on the diagonal
`{z = w}` — a set with an accumulation point in each variable separately
— yet converges nowhere off the diagonal. The diagonal is not a product
set `E_1 x E_2` with both factors infinite; the amended clause D-2
excludes it. This is why the sealed text's accumulation-point-per-
variable clause is void and the product-set clause governs.

**Step 4 (derivative convergence; Cauchy representation).** For any
`(z,w) in P^o` choose `rho` with `max(|z|,|w|) < rho < epsilon_*`. For
all mixed orders `(m,n)`:

```text
d_z^m d_w^n gamma_K(z,w) = m! n! (2 pi i)^{-2} oint_(|zeta_1|=rho)
  oint_(|zeta_2|=rho) gamma_K(zeta_1,zeta_2)
  / [ (zeta_1 - z)^{m+1} (zeta_2 - w)^{n+1} ] dzeta_1 dzeta_2 .
```

The integrand converges uniformly on the compact torus `T_rho` (Step 3),
so every mixed partial converges to the corresponding derivative of
`gamma_inf`. In particular, at `(0,0)`:

```text
lim_K d_+ d_- (-Log Ghat_K)/N_4(K) |_(0,0) = d_+ d_- (-gamma_inf)|_(0,0),
```

the interchange claim.

**Step 5 (FK-2 transport, three separately normalized limits).** At
each finite `K` (under B0 — contained in (H1) — and C2, with C1 or the
contact term included), FK-2 of Section 3.2 is an exact identity between
three second-order coefficients of the SAME anchored log `L_K`:

```text
H_(att,K) = -Re L_(K,++) ;  g_(D,c,K) = mixed coefficient ;
(log q_K)'' = diagonal second derivative = 2 Re L_(K,++) + 2 g_(D,c,K) .
```

Dividing by `N_4(K)`, each term is a fixed real-linear combination of
second-order derivatives of `gamma_K` at the origin (restricted to real
slices). By Step 4 each of the three normalized sequences converges
separately (D-9 reading), and the exact finite-K identity
`H/N_4 = g/N_4 - (1/2)(log q)''/N_4` passes to the limit:

```text
R_record-candidate identity:
lim H_(att,K)-density = lim g_(D,c,K)-density
                        - (1/2) lim (log q_K)''-density .
```

**Step 6 (audit: what the proof used).** Steps 1-5 used exactly: (H1)
per-K zero-freeness at the common `epsilon_*` (Step 1 branch; no
uniform delta anywhere), (H2)(i) the uniform intensive bound (Steps 2,
3), (H2)(ii) product-set pointwise convergence (Step 3), C1/C2 only
through the finite-K FK-2 identities of Step 5, plus contractibility of
the polydisc and classical Cauchy-integral complex analysis (derived
inline, not cited). NO step used clustering, decay, correlation
inequalities, transfer operators, or ANY property of the actual parent
beyond (H1)/(H2)/C1/C2. In particular the schema cannot manufacture
(H1)/(H2): on the GHZ witness family `Z_N(A) = cos(N tau_R A)` the (H1)
input fails (zeros at `1/(sqrt(2) N)` enter every fixed polydisc) and
the schema REFUSES (executed control S6.1). QED.

### 5.4 Adoption fence (S5.3, honored)

Nothing in this execution discharges, assumes, or approximates (H1) or
(H2); no clustering principle was adopted; the periodic zero-free
lineage (F2.5) and the exhaustive chain's zero-freeness (F2.1) were not
cited for any completed-chain obligation. The flags

```text
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
Duhamel_intensive_Hessian_equality_proved = false
```

remain false. Any future attempt to discharge them by adoption is
`CLUSTERING_ADOPTION_ATTEMPT_BLOCKED` and escalates to Brian by name.

### 5.5 Interface I3 V002 (named identically per amendment Part III)

```text
I3 = { epsilon_star;
       per-K zero-freeness of Ghat_K on the closed pair polydisc P
         (common epsilon_star; K-dependent floors only);
       Gamma_star = eta(epsilon_star) / (1 - eta(epsilon_star));
       eta(epsilon_star) with cluster sums bounded by eta^n;
       per-cell activities in ACTION-DENSITY form;
       N_4(K) := |X(K)|_4 (both specs);
       LEMMA 0 as the majorant spec's first numbered obligation }.
```

Interface typing delta (flagged loudly, both directions): the
majorant memo's "discharged BY TYPE on the exhaustive object"
(`R_all(a,a) = I`) does NOT transport to the completed chain — the
completed diagonal is `q_K(a)`, not 1, and its non-vanishing is exactly
(H1)/B0. The majorant spec must supply (H1)/(H2) FOR THE COMPLETED
NORMALIZED FUNCTIONAL `Ghat_K`; exhaustive-typed versions do not satisfy
this interface. This paragraph is the citation anchor required by S5.4
so that both specs name the same interface with the same typing.

---

## 6. Per-state quantifier discipline and fences (standing)

Every scalar claim above is quantified per pinned state; no claim is
promoted to "for all states"; no cross-state averaging occurs anywhere
in this execution. Fences F2.1-F2.5 and the bidirectional substitution
fences (`9410ee80...`; O6 of `2f2aa7f7...`) were honored: the
all-outcome sum was never substituted for the completed component or
conversely (certified numerically in the S6.4 re-execution), the
exhaustive three-way agreement was never cited against the completed
chain (the S6.3(c) control certifies the two objects differ on the
executed fixture), and the periodic zero-free lineage was not cited.

## 7. Named blocks arising in this execution

One obligation could not be executed and is reported as a NAMED BLOCK
(a partial result per S8; the completed obligations above stand):

```text
FC_FIXTURE_SEALED_ARTIFACTS_ABSENT_BLOCKED (named witness):
  Amendment D-4 directs M3 and M5 to run also on F-C (the Phase-A
  one-particle-sector objects per 789338ad... A2-A5) with the two
  Phase-A pinned states. The spec's own F-C fixture definition (S7)
  requires F-C to be "used only as already sealed (no Phase-A
  production run is required or permitted by this gate)". At execution
  time the Phase-A gate (task: execute 789338ad...) has NOT produced or
  sealed its bundle: no sealed u_lambda(a), cross operators, or carrier
  matrices exist anywhere under the cleanroom root. Constructing the
  A1/A2 Galerkin matrices (M(t), B_D(t)) afresh would require the A6
  numeric conventions (cell quadratures), which S7 does not incorporate
  (it cites A2-A5 only), and a density-normalization convention mapping
  the two pinned covariance schemes (C_2^mix = Q_2 P_- Q_2 of 235246ab;
  C_2^pure = 1_(-inf,0)(Q_2 h_0 Q_2) of a79939ad) into the S1.2
  state-evaluation form — a convention the sealed record assigns to the
  separately forward-sealed Phase-B gate, which does not yet exist.
  Ambiguity unresolvable from the sealed texts is a BLOCK, not a
  choice. The F-A and F-B legs of M3/M4/M5 executed in full.
```

## 8. Attestations

```text
no measured constants consulted            = true
no coupling / kappa_record / alpha read    = true
exact arithmetic where decidable           = true
floats inform, never decide                = true
sealed/production files modified           = none
outputs written                            = this draft + the primary
  execution JSON (stage8_execution/work/
  T07_duhamel_conditioned_identity_primary_v001.json); no .seal files
```
