# Gamma-Gate Record Parity Lemmas — Full Operator Proofs (DRAFT V001)

Status: PRIMARY-LANE DRAFT — NOT SEALED. Written by the gamma-gate primary
execution lane under `STAGE8_T7_GAMMA_REFUTATION_AND_PARITY_LEMMAS_GATE_SPEC_V001.md`
(sha256 5f7e99655cd92935406606ad03e33befded65a0091e2ccbe6d91689e76473e75) as
repaired by `STAGE8_T7_GAMMA_GATE_SPEC_REPAIR_AMENDMENT_V001.md`
(sha256 83ff0d4f818370b271c10caa265ffbea431f31c7b7437d98d4d040201c5c5759).
The amendment overrides the spec wherever they differ; in particular Lemma 2
is proved for the amended involution T' = P_x (x) (i gamma^1) in conjugation
form. No `.seal` file is written by this lane; the construction lane seals
after blind comparison.

Machine verification companion:
`stage8_execution/work/T07_gamma_refutation_gate_primary_v001.json`.

## 0. Notation and conventions

Dirac representation (as constructed in the sealed executors, verbatim):

```text
gamma^0 = diag(I2, -I2);   gamma^j = [[0, sigma_j], [-sigma_j, 0]];
gamma^5 = i gamma^0 gamma^1 gamma^2 gamma^3 = [[0, I2], [I2, 0]];
alpha_j = gamma^0 gamma^j;   S = -i gamma^0 gamma^5.
```

Exact algebra facts used repeatedly (all are entries of the Clifford
relations {gamma^mu, gamma^nu} = 2 eta^{mu nu}, eta = diag(+,-,-,-), and
{gamma^5, gamma^mu} = 0):

```text
(C1) (gamma^0)^2 = I,  (gamma^j)^2 = -I  (j = 1,2,3);
(C2) gamma^mu gamma^nu = -gamma^nu gamma^mu  (mu != nu);
(C3) gamma^5 gamma^mu = -gamma^mu gamma^5,  (gamma^5)^2 = I;
(C4) conjugation sign rule: for an invertible product P of distinct gamma
     factors and a single factor X, P X P^{-1} = (-1)^{n(P,X)} X where
     n(P,X) = number of factors of P that anticommute with X.
```

Hermite carrier (sealed Phase-A A1): H_(n,ell) = span{phi_a(x/ell)
phi_b(y/ell) phi_c(z/ell)} (x) C^4, n = 2, ell in {1, sqrt2};
h_0 = sum_j p_j (x) alpha_j; M(t) = Q 1_(|x|<=r(t)) Q;
B_D(t) = Q b_D(t,.) Q; J(t) = -B_D(t) (x) alpha_x;
h_lambda(t;a) = h_0 + lambda v(t) M(t) (x) S + a J(t).

Three-site fixture (sealed executor 3d8aea1a..., single-record adaptation
per amendment R4): h_0^f = (-i D_0) (x) alpha_x with D_0[j,j+1] = 1/2,
D_0[j,j-1] = -1/2 (indices mod 3); W^f = diag(1,1,0) (x) S;
J^f = -i (dD/dtheta)|_0 (x) alpha_x = (A/6) (x) alpha_x with
A[j,j+-1] = 1 (the sealed tangent dD/dtheta[j,j+-1] = i/6);
h^f_lambda(t;a) = h_0^f + lambda v(t) W^f + a J^f, one unit pulse.

Envelopes (sealed comparison spec, critical-path scope correction sec. 1):
v_A(t) = tau_R 32 r(t)^3, v_B = 24 tau_R / pi, tau_R = pi/sqrt2,
r(t) = min(t, 1-t).

## 1. Lemma 1 (lambda-parity / chiral conjugation)

STATEMENT (as sealed). T := I_spatial (x) gamma^5 satisfies

```text
T = T^dagger,  T^2 = I,  [T, h_0] = 0,
T (M (x) S) T = -(M (x) S),   T J T = +J,
```

hence u_{-lambda}(a) = T u_lambda(a) T for all a and both envelopes, and
D_{-lambda}(a) = D_lambda(a) exactly for every T-invariant admitted state —
exact under Galerkin compression and the sealed quadratures.

PROOF.

(1.1) T^2 = I (x) (gamma^5)^2 = I by (C3); gamma^5 is Hermitian in this
representation ((gamma^5)^dagger = gamma^5 entrywise), so T = T^dagger.

(1.2) [T, h_0] = 0. Each term of h_0 is p_j (x) alpha_j with p_j acting on
the spatial factor only. T acts on the spinor factor alone, so it commutes
with p_j (x) I. On the spinor factor, by (C4) with P = gamma^5:
gamma^5 alpha_j gamma^5 = gamma^5 gamma^0 gamma^j gamma^5: gamma^5
anticommutes with both gamma^0 and gamma^j, so the sign is (-1)^2 = +1:
gamma^5 alpha_j gamma^5 = alpha_j. Hence T (p_j (x) alpha_j) T =
p_j (x) alpha_j, term by term. QED (1.2).

(1.3) T (M (x) S) T = -(M (x) S). M acts spatially; T commutes with it.
On the spinor factor: gamma^5 S gamma^5 = -i gamma^5 gamma^0 gamma^5
gamma^5 = -i gamma^5 gamma^0 = +i gamma^0 gamma^5 = -S, using (C3) twice
and (gamma^5)^2 = I. QED (1.3).

(1.4) T J T = +J. J = -B_D (x) alpha_x; B_D spatial; gamma^5 alpha_x
gamma^5 = alpha_x by the same two-anticommutation count as (1.2). QED (1.4).

(1.5) Generator conjugation: for every t, a, lambda,

```text
T h_lambda(t;a) T = h_0 - lambda v(t) M(t) (x) S + a J(t)
                  = h_{-lambda}(t;a).
```

(1.6) Propagator conjugation. For the exact time-ordered exponential,
conjugation by the constant unitary T passes through products, integrals
and limits: T [T-exp(-i int h_lambda dt)] T = T-exp(-i int T h_lambda T dt)
= u_{-lambda}(a). The same holds exactly for every sealed discrete
factorization: in the Strang chain F A G_lambda A F,

```text
T F T = F            (F = exp(-i h_0 dt/2), by (1.2)),
T A T = A            (A = exp(-i a J dt/2), by (1.4)),
T G_lambda T = G_{-lambda}   (G = exp(-i lambda v M (x) S dt), by (1.3)),
```

because conjugation by a unitary commutes with the matrix exponential.
Since T is spinor-only, it commutes with every Galerkin compression
Q f(x) Q of a spatial multiplication operator; hence the identities hold
exactly on the compressed carrier with the sealed quadrature matrices —
machine-precision equalities, no quadrature error term. The fixture case
is identical with T^f = I_3 (x) gamma^5 (D_0, A, masks untouched;
(1.2)-(1.4) verbatim). QED (1.6).

(1.7) State invariance.
(i) Mixed covariance C_mix = (1/2)(1 - sum_j phat_j (x) alpha_j) (sealed
momentum-space half-projector; phat_j spatial): T C_mix T = C_mix by the
alpha_j-invariance of (1.2).
(ii) Pure scheme C_pure = 1_{(-infty,0)}(h_0): [T, h_0] = 0 implies T
commutes with every spectral projector of h_0 (functional calculus on a
finite Hermitian matrix), so T C_pure T = C_pure. The sealed n = 2 carrier
has no h_0 zero modes (amendment R4(e)), so the sea projector is
unambiguous.
(iii) Fixture states (amendment R4(d)): [T^f, h_0^f] = 0 gives invariance
of the sea projector P_neg, the 4-dim kernel projector P_ker, and hence of
the kernel-excluded sea (occupation 0) and of the mixed analogue
C = P_neg + (1/2) P_ker. QED (1.7).

(1.8) Scalar consequence. For the pure scheme, with V an orthonormal basis
of the occupied subspace: T-invariance of the subspace gives T V = V U_T
with U_T unitary (4x4 resp. occupied-dim), so

```text
D_{-lambda}(a) = det(V^dag T u_lambda(a) T V)
             = det(U_T^dag V^dag u_lambda(a) V U_T) = D_lambda(a).
```

For a quasifree covariance state, D = det(1 - C + C u):
det(1 - C + C T u T) = det(T (1 - C + C u) T) = det(1 - C + C u), using
T C T = C and det(T X T) = det(X). Hence D_{-lambda}(a) = D_lambda(a)
exactly — both envelopes, all a, all record orders. QED Lemma 1.

(1.9) Folded reduction (used by Part B). With the A3 pointer weights
w = (-1/4, 1/2, -1/4) under the sealed ordering (-sqrt2, 0, +sqrt2)
(recovered from the c-matrix spectral resolution, not typed in; see the
companion JSON `record_data_check`), Lemma 1 gives for T-invariant states

```text
Z(a) = sum_lambda w_lambda D_lambda(a) = -(1/2) [ D_sqrt2(a) - D_0(a) ].
```

CAUTION (toy-model scope): this folding REQUIRES T-invariance of the
state. The gamma memo's toy state (S psi = psi) is NOT T-invariant, which
is exactly why the toy's three-history pointer sum gives the superseded
kappa_B = 1.802 while the corrected folded assembly (amendment R3) gives
kappa_B = 0.534. On the B1 fixture both pinned states are T-invariant
(1.7), so the folded and pointer forms coincide there.

## 2. Lemma 2 (a-parity), amended operator T' = P_x (x) (i gamma^1)

STATEMENT (amendment R1). T' := P_x (x) (i gamma^1) satisfies

```text
T' = T'^dagger,  T'^2 = +I,  [T', h_0] = 0,
T' (M (x) S) T'^{-1} = +(M (x) S),   T' J T'^{-1} = -J,
```

hence u_lambda(-a) = T' u_lambda(a) T'^{-1} and D_lambda(-a) =
D_lambda(a) for every T'-invariant admitted state; hence Z(-a) = Z(a) and
Z'(0) = 0. Exact on the sealed quadrature grids (P_x-closed).

PROOF.

(2.1) Involution and Hermiticity. (i gamma^1)^2 = -(gamma^1)^2 = +I by
(C1). In this representation gamma^1 is anti-Hermitian
((gamma^1)^dagger = -gamma^1), so (i gamma^1)^dagger = i gamma^1.
P_x is the spatial reflection x -> -x: P_x^2 = I, P_x = P_x^dagger.
Hence T'^2 = I and T' Hermitian; in particular T'^{-1} = T'.

(2.2) Spinor conjugation signs. By (C4) with P = i gamma^1 (the scalar i
cancels in conjugation): gamma^1 anticommutes with gamma^0, gamma^2,
gamma^3, gamma^5 and commutes with itself. Therefore

```text
(i gamma^1) alpha_x (i gamma^1)^{-1} = (-gamma^0)(+gamma^1) = -alpha_x;
(i gamma^1) alpha_y (i gamma^1)^{-1} = (-gamma^0)(-gamma^2) = +alpha_y;
(i gamma^1) alpha_z (i gamma^1)^{-1} = (-gamma^0)(-gamma^3) = +alpha_z;
(i gamma^1) S (i gamma^1)^{-1} = -i(-gamma^0)(-gamma^5) = S.
```

(2.3) Spatial action. On the continuum carrier (P_x psi)(x,y,z) =
psi(-x,y,z): P_x phat_x P_x = -phat_x, P_x phat_{y,z} P_x = +phat_{y,z},
and P_x (Q f Q) P_x = Q f(-x,y,z) Q for any multiplication operator f.
On the sealed Hermite basis this is EXACT at the matrix level: the
one-dimensional Hermite functions obey phi_a(-x) = (-1)^a phi_a(x)
(parity of the Hermite polynomials), so in the sealed lexicographic basis

```text
P_x = diag((-1)^a) (x) I_n (x) I_n            (spatial factor),
```

a signature matrix. Radiality: M(t) = Q 1_(|x|<=r(t)) Q and
B_D(t) = Q b_D(t, |x|) Q are compressions of x-even (indeed radial)
functions, so P_x M(t) P_x = M(t) and P_x B_D(t) P_x = B_D(t) exactly
PROVIDED the quadrature realization is P_x-closed, which it is: the map
(x,y,z) -> (-x,y,z) acts on the sealed spherical product grid by
phi -> pi - phi with r and cos(theta) fixed; the uniform azimuthal grid
{2 pi k / N_phi} is closed under phi -> pi - phi exactly when N_phi is
even, and the sealed counts (20 primary, 24/28 independent) are even; the
Gauss-Legendre radial/polar nodes and all weights are untouched. Hence
the compressed matrices satisfy the reflection identities exactly (to
machine representation), with no quadrature error term.

(2.4) [T', h_0] = 0:

```text
T' (phat_x (x) alpha_x) T' = (-phat_x) (x) (-alpha_x) = +phat_x (x) alpha_x;
T' (phat_y (x) alpha_y) T' = (+) (x) (+);  same for z.
```

(2.5) T' (M (x) S) T' = (P_x M P_x) (x) S = M (x) S by (2.2), (2.3).

(2.6) T' J T' = -(P_x B_D P_x) (x) (-alpha_x) = +B_D (x) alpha_x = -J.

(2.7) Generator and propagator: T' h_lambda(t;a) T' = h_lambda(t;-a) for
every t; conjugation passes through the exact T-exp and through every
sealed discrete factorization (T' F T' = F, T' G_lambda T' = G_lambda,
T' A(a) T' = A(-a)), giving u_lambda(-a) = T' u_lambda(a) T'^{-1} exactly
on the sealed grids. QED (2.7).

(2.8) State invariance. C_mix: phat_x (x) alpha_x -> (-)(-) = +, the
y,z terms are invariant by (2.2)/(2.3); so T' C_mix T' = C_mix.
C_pure: [T', h_0] = 0 and functional calculus. Fixture (amendment R4(c)):
T'_f = R (x) (i gamma^1) with R the ring reflection j -> 1-j (mod 3)
(0 <-> 1, 2 fixed), R^2 = I:

```text
(R D_0 R)[j,k] = D_0[1-j, 1-k] = -D_0[j,k]
```

(the reflection reverses the ring orientation: 1-k = (1-j)+1 iff
k = j-1), so h_0^f = (-i D_0) (x) alpha_x -> (-i)(-D_0) (x) (-alpha_x)
= h_0^f: [T'_f, h_0^f] = 0. R diag(1,1,0) R = diag(1,1,0) (R swaps sites
0,1 and fixes site 2), and S is fixed by (2.2): T'_f W^f T'_f = W^f.
R A R = A (adjacency of the triangle is invariant under every vertex
permutation), alpha_x -> -alpha_x: T'_f J^f T'_f = -J^f. [T'_f, h_0^f]=0
makes P_neg, P_ker, the kernel-excluded sea and the mixed analogue
C = P_neg + (1/2) P_ker all T'_f-invariant (R4(d)); verified at machine
precision in the companion JSON. QED (2.8).

(2.9) Scalar consequence: exactly as (1.8) with T' in place of T:
D_lambda(-a) = D_lambda(a) for both pinned schemes; hence Z(-a) = Z(a)
and Z'(0) = 0 exactly. QED Lemma 2.

## 3. Teeth controls (A3 as amended) — results and one control failure

(3.1) Lambda-odd control (amendment R2 table, w~(lambda) = lambda/4 under
the sealed ordering): sum_lambda w~_lambda D_lambda(a) =
[D_{+sqrt2}(a) - D_{-sqrt2}(a)] / (2 sqrt2) = 0 exactly by Lemma 1.
Machine: <= 1e-14 verified on both carriers, both ell, both envelopes,
both states (companion JSON). PASS.

(3.2) Broken-P_x control: FAILED — with a proven mechanism. The
predeclared variant displaces the b_D center to x_0 = 1/10 along x. The
machine result is |Z'(0)| ~ 1e-14..1e-16 for the displaced variant on
every (ell, envelope, state) — the amendment floor >= 1e-9 is not
reached. This is NOT an implementation artifact (the displaced operator
is verifiably P_x-broken: || T' J' T' + J' || / || J' || ~ 0.28, and the
propagator-level Lemma-2 residual rises from 1e-14 to 1.6e-6). It is a
structural protection theorem the review's floor did not anticipate:

PROTECTION THEOREM (a-parity of the amplitudes is doubly protected).
Let y := I_spatial (x) alpha_y and let B'(t) be ANY real symmetric
spatial profile matrix (in particular the displaced Q b_D(., x - x_0) Q),
J'(t) = -B'(t) (x) alpha_x. Then, writing Xbar for the entrywise complex
conjugate:

```text
y h_0bar y = h_0,   y (M (x) S)bar y = M (x) S,   y J'bar y = -J'.
```

Proof: conjugation by y = gamma^0 gamma^2 flips alpha_x, alpha_z, fixes
alpha_y, and flips S (count anticommutations as in (C4)); entrywise
conjugation gives pbar_j = -p_j (the sealed momentum matrices are purely
imaginary), alphabar_x = alpha_x, alphabar_y = -alpha_y, alphabar_z =
alpha_z, Sbar = -S, Bbar' = B' (real), Mbar = M. Composing the two sign
tables gives the three identities. Consequently, since h^T = hbar for
Hermitian h and transposition converts the time-ordered product to the
anti-time-ordered one,

```text
y u_lambda(a)^T y = Ttilde-exp(-i int [h_0 + lambda v W - a J'(t)] dt),
```

the ANTI-chronological propagator at flipped connection sign, i.e. the
chronological propagator of the TIME-REVERSED protocol at -a. The sealed
profiles are symmetric under t -> 1-t (r(t), b_D(t,.), v_A, v_B all are;
so is any x-displaced b_D), so this equals u_lambda(-a). Finally, for the
sea determinant: det(V^dag y u^T y V) = det over the transported basis
y Vbar, and y h_0bar y = h_0 implies h_0 (y Vbar) = (y Vbar) Lambda —
y Vbar spans the SAME sea, so the determinant is unchanged; the two
transpositions cancel ((alpha_y)^T = -alpha_y twice). Hence

```text
D_lambda(-a) = D_lambda(a)   for EVERY real spatial profile B',
```

x-displaced or not. The x-displacement can break the T' (P_x) route of
Lemma 2 but cannot break this transpose route; only a simultaneously
time-asymmetric AND spatially complex (or spinor-direction-changed)
connection could. (Empirically, even an additional t-asymmetric
modulation (1/2 + t) b'_D left |Z'(0)| at machine zero — recorded in the
companion JSON as a labeled observation; a complementary determinant-level
reversal invariance via the Jacobi complementary-minor identity for
unitaries with det u = 1 is the suspected mechanism, NOT proved here.)

CONSEQUENCE FOR THE GATE: the predeclared broken-P_x teeth control is
structurally unable to reach its amended floor (broken |Z'(0)| >= 1e-9);
the control FAILS as sealed. Per the frozen verdict rule ("GATE_BLOCKED
on ... any control failure") this is a GATE_BLOCKED trigger, preserved,
not repaired. No substitute breaking variant is executed in place of the
sealed one. The failure does not touch the LEMMAS (which are true and
verified — indeed the mechanism above STRENGTHENS the a-parity
conclusion); it defeats the control's negative-power only.

## 4. Part-B supporting exact reductions (recorded for the verifier)

(4.1) Toy (B3, corrected assembly R3). theta_A = sqrt2 sigma_A(1) =
sqrt2 tau_R = pi exactly, so 1 - e^{-i theta_A} = 2 and kappa_A =
1/2 + Re Phi_A. Exact identity: Phi + conj(Phi) over the ordered simplex
equals the full square integral |I|^2, I = int_0^1 e^{i phi(t)} dt (swap
the dummies in the s > t half), so Re Phi_A = |I_A|^2 / 2. The t -> 1-t
reflection of the sealed profile gives e^{i phi_A(1-u)} =
conj(e^{i phi_A(u)}) (phi_A(t) = 16 pi t^4 on [0,1/2], = 2 pi - 16 pi
(1-t)^4 on [1/2,1]), hence I_A = 2 int_0^{1/2} cos(16 pi t^4) dt is real
and kappa_A = 1/2 + 2 C^2, C = int_0^{1/2} cos(16 pi t^4) dt. theta_B =
sqrt2 * 12 sqrt2 = 24 exactly and Phi_B = (e^{48 i} - 1 - 48 i)/(48 i)^2
in closed form. Values (30 digits, sympy): kappa_A =
0.707088153007124588561388658144, kappa_B =
0.534000295799376337739661590011, difference
0.173087857207748250821727068133 — the amendment's corrected values,
confirmed independently by direct unitary propagation of the folded
object (0.7070872 / 0.5339989 at h = 1e-3 stencil).

(4.2) Comparator (B2, pinned in R5). Everything commutes on the
one-dimensional line; log D_lambda(a) = -i (hbar_0 + lambda sigma(1) m s
+ a jbar) is linear in a, so H_v(lambda) = 0 identically and Xi(v_A) =
Xi(v_B) = 0 exactly. Denominators certified nonzero: v_A: e^{-i pi} - 1 =
-2; v_B: e^{-24 i} != 1 because 3 < 24/(2 pi) < 4 strictly (rational
bounds 223/71 < pi < 22/7). No ZERO_DENOMINATOR trigger.

(4.3) B1 computational route (amendment R6 adopted): the a-expansion
coefficients (u^0, du/da, (1/2!) d^2u/da^2 as p, q, r) are the (1,1),
(1,2), (1,3) blocks of the propagator of the block-triangular Van Loan
generator X(t) = [[h, J, 0], [0, h, J], [0, 0, h]] (exact Duhamel
identity, finite dimension). v_B branch: h is time-independent
(lambda v_B = +-24 exactly), so the blocks are given by the closed form
exp(-i X), evaluated as an exact rational Taylor sum with the certified
remainder ||X||^{K+1}/(K+1)! (1 - ||X||/(K+2))^{-1}, ||X|| <= 87/100 + 24
+ 1/3. lambda = 0 arm identically (coupling 0). v_A branch: Dyson partial
sums in the record coupling: the level-triangular tower P_N (levels =
powers of the record vertex r(t)^3 W; coefficients exact rationals; the
coupling (+-sqrt2)(16 sqrt2 pi) = +-32 pi attached at assembly as a
certified interval) with the pinned tail bound: since ||W|| = 1,
|lambda| int_0^1 v_A = sqrt2 tau_R = pi,

```text
|| u^0_lambda - sum_{N<=K} || <= sum_{N>K} pi^N/N!
                             <= [pi^{K+1}/(K+1)!] (K+2)/(K+2-pi),
```

and the q/r blocks carry one resp. two J insertions distributed over the
ordered simplex, giving the same bound multiplied by ||J|| = 1/3 resp.
||J||^2/2 = 1/18. The minus-lambda arms are obtained EXACTLY from
u_{-lambda}(a) = T u_lambda(a) T (Lemma 1, rational T). Truncation of the
per-substep power series is padded by a certified defect bound (residual
polynomial norm times the variation-of-constants growth factor
1/(1 - ||h_0|| h)). Every scalar that reaches the verdict is a certified
rational outward enclosure; floating point informs only the labeled
cross-check lane.

(4.4) Determinant expansion (exact, second order in a): with
M(a) = M_0 + a M_1 + a^2 M_2 the state-compressed propagator,
det M(a) = det M_0 [1 + a tr X + a^2 (tr Y + ((tr X)^2 - tr X^2)/2)]
+ O(a^3), X = M_0^{-1} M_1, Y = M_0^{-1} M_2; hence

```text
dD/da / D |_0 = tr X       (interval ~ 0; Lemma-2 check),
H = d^2/da^2 log D |_0 = 2 tr Y - tr(X^2),
Xi(v) = F_v(sqrt2) [H_v(sqrt2) - H(0)] / [F_v(sqrt2) - F(0)].
```

Re and Im of Delta_Xi = Xi(v_A) - Xi(v_B) are reported separately with
certified rational outward bounds; the verdict arm keys on Re only
(amendment R5), with ZERO_DENOMINATOR and the Re/Im corner mapped to
their blocked arms.

## 5. Cross-checks bound into the machine run

(i) Tower level-0 vs the lambda = 0 Van Loan closed form (two independent
exact routes to the same object) — agreement required at 1e-25.
(ii) F(0) pure = det of the free flow over the sea = e^{2 i sqrt3}
exactly (four sea states at energy -sqrt3/2 for unit time); the certified
enclosure must contain the 110-digit value of e^{2 i sqrt3}.
(iii) The float lane (labeled informative) must agree with the certified
midpoints to ~1e-8.

— end of draft —
