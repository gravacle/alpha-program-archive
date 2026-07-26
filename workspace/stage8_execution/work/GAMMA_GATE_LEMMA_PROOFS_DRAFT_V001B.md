# Gamma Gate Parity Lemma Proofs — Draft V001B (primary lane, fresh re-run)

Date: 2026-07-26. Status: WORKING DRAFT — not a result artifact, not sealed.

Lane: GAMMA-GATE PRIMARY EXECUTION LANE, fresh re-run after an
infrastructure kill of a prior attempt. A stale draft
`GAMMA_GATE_LEMMA_PROOFS_DRAFT_V001.md` from the killed run exists in this
directory; per the re-run instruction it was NOT read, NOT trusted, and NOT
overwritten — this file carries the `_V001B` name for that reason.

Authorities (every hash verified this run before any construction; the
verification table is in
`stage8_execution/work/T07_gamma_refutation_gate_primary_v001.json`):

- `STAGE8_T7_GAMMA_REFUTATION_AND_PARITY_LEMMAS_GATE_SPEC_V001.md`
  (5f7e9965…, seal verified)
- `STAGE8_T7_GAMMA_GATE_SPEC_REPAIR_AMENDMENT_V001.md` (83ff0d4f…, seal
  verified) — T' redefined as P_x (x) (i gamma^1); lambda-odd table
  w~(lambda) = lambda/4; corrected toy assembly; frozen B1 cluster R4;
  ZERO_DENOMINATOR and Re/Im-corner verdict rule; B2 pinned identically
  zero; certified-rational outward enclosures admissible.
- `STAGE8_T7_GAMMA_GATE_CONTROL4_REPAIR_AMENDMENT_V001.md` (f7f93be8…,
  seal verified) — control-4 v2 double-broken falsifier; apparatus note
  (scaling-and-squaring step exponentials).

Conventions: sealed Dirac representation of the sealed executors
(gamma^0 = diag(I2, -I2); gamma^j = [[0, sigma_j], [-sigma_j, 0]];
gamma^5 = i gamma^0 gamma^1 gamma^2 gamma^3 = [[0, I2], [I2, 0]];
alpha_j = gamma^0 gamma^j; S = -i gamma^0 gamma^5). Useful block forms:
alpha_x = sigma_x (x) sigma_x, S = sigma_y (x) I2 (first Pauli factor =
particle/antiparticle block index), so {S, alpha_x} = 0 and S, alpha_y
anticommute, while [S, gamma^5-type checks] are as below.

---

## Lemma 1 (lambda-parity / chiral conjugation)

**Statement.** T := I_spatial (x) gamma^5 is a Hermitian involution with

```text
[T, h_0] = 0,   T (M (x) S) T = -(M (x) S),   T J T = +J,
```

hence T h_lambda(t; a) T = h_{-lambda}(t; a), u_{-lambda}(a) =
T u_lambda(a) T, and for every T-invariant admitted state,
D_{-lambda}(a) = D_lambda(a) exactly — both envelopes, all a, all record
orders; exact under Galerkin compression and the sealed quadratures.

**Proof.** Each step is an exact algebra identity.

1. *Involution/Hermiticity.* (gamma^5)^2 = I and gamma^5 = (gamma^5)^dagger
   in the sealed representation (direct block computation:
   gamma^5 = [[0, I], [I, 0]]). Hence T^2 = I, T = T^dagger.

2. *[T, h_0] = 0.* h_0 = sum_j p_j (x) alpha_j (Hermite carrier) or
   A (x) alpha_x (fixture; A = -i(U_+ - U_+^T)/2). gamma^5 anticommutes
   with gamma^0 and with every gamma^j, therefore it COMMUTES with every
   product alpha_j = gamma^0 gamma^j (two anticommutations). T acts as
   identity on the spatial factor, so [T, h_0] = 0 exactly.

3. *Record-term anticonjugation.* S = -i gamma^0 gamma^5.
   gamma^5 S = -i gamma^5 gamma^0 gamma^5 = +i gamma^0 gamma^5 gamma^5
   = i gamma^0; S gamma^5 = -i gamma^0 gamma^5 gamma^5 = -i gamma^0.
   Hence {gamma^5, S} = 0 (the anticommutator vanishes although the
   commutator does not), so T (M (x) S) T = M (x) (gamma^5 S gamma^5)
   = -(M (x) S). M is spatial (radial ball compression on the Hermite
   carrier; mask diag(1,1,0) on the fixture) and is untouched by T.

4. *Connection invariance.* J = -B_D (x) alpha_x (Hermite) or
   (1/6) K_3 (x) alpha_x (fixture sealed connection direction). By step 2,
   gamma^5 commutes with alpha_x, so T J T = +J. Note this holds for ANY
   spatial factor, hence also for every broken-variant connection of
   control 4.

5. *Propagator conjugation.* h_lambda(t; a) = h_0 + lambda v(t) M(t) (x) S
   + a J(t). Steps 2-4 give T h_lambda(t; a) T = h_{-lambda}(t; a)
   pointwise in t. Time-ordered products (and every discretized product
   of step exponentials: T e^{-i X dt} T = e^{-i T X T dt} termwise in the
   exponential series) conjugate factor by factor, so
   u_{-lambda}(a) = T u_lambda(a) T exactly — for the exact time-ordered
   exponential AND for the sealed Strang/midpoint discretizations, at
   every step count.

6. *State invariance and amplitudes.* For the pinned mixed covariance
   C = (1/2)(1 - sum_j phat_j (x) alpha_j): gamma^5 commutes with every
   alpha_j, so [T, C] = 0. For the pure Dirac-sea projector: [T, h_0] = 0
   implies T preserves every spectral subspace of h_0, hence commutes
   with the negative-energy projector (Hermite n=2 carrier: no zero
   modes, h_0^2 = (3/(2 ell^2)) I), and on the fixture with BOTH the
   4-dim kernel projector and the sea projector — the kernel-excluded
   convention of R4(d) is manifestly T-invariant. For any state with
   [T, N] = 0 and either functional
   D(u) = det(1 - N + N u) or D(u) = det(V^dagger u V) (V spanning a
   T-invariant subspace), conjugation invariance of determinants gives
   D(T u T) = D(u). With step 5: D_{-lambda}(a) = D_lambda(a). QED.

*Machine verification (A2, scaling-and-squaring apparatus):* Hermite
carrier n=2, ell in {1, sqrt2}, N = 96 sealed Strang assembly, both
envelopes, frozen histories: max conjugation residual
||u_{-lambda} - T u_lambda T||_2 = 1.39e-15; per-history amplitude
residual max |D_{+sqrt2} - D_{-sqrt2}| = 1.05e-15; state invariance
residuals <= 1.8e-15. Fixture: conjugation residual max 1.09e-14;
functional residual 1.08e-16. All well inside the 1e-12 bar.

---

## Lemma 2 (a-parity), amended operator T' = P_x (x) (i gamma^1)

**Statement.** T' := P_x (x) (i gamma^1) is a Hermitian involution with

```text
[T', h_0] = 0,  T' (M (x) S) T'^{-1} = +(M (x) S),  T' J T'^{-1} = -J,
```

hence u_lambda(-a) = T' u_lambda(a) T'^{-1} and, for every T'-invariant
admitted state, D_lambda(-a) = D_lambda(a) exactly; hence Z(-a) = Z(a)
and Z'(0) = 0. Exact on the sealed quadrature grids (P_x-closed).

**Proof.**

1. *Involution/Hermiticity.* (gamma^1)^2 = -I, so (i gamma^1)^2 = +I;
   (gamma^1)^dagger = -gamma^1, so (i gamma^1)^dagger = i gamma^1.
   P_x^2 = I, P_x = P_x^dagger (parity is the diagonal sign matrix
   (-1)^{a_x} on the Hermite basis — Hermite functions have definite
   parity; on the fixture the analogue is the ring reflection R: j -> 1-j,
   a real symmetric permutation with R^2 = I). Hence T'^2 = I,
   T' Hermitian; all identities below may be (and are) read in
   conjugation form T' X T'^{-1} = T' X T'.

2. *[T', h_0] = 0.* Hermite carrier: P_x p_x P_x = -p_x,
   P_x p_{y,z} P_x = +p_{y,z}. Spin side: gamma^1 anticommutes with
   gamma^0 and commutes with itself, so
   (i gamma^1) alpha_x (i gamma^1)^{-1} = gamma^1 gamma^0 gamma^1
   (gamma^1)^{-1}-conjugation = -alpha_x (one anticommutation, with
   gamma^0); for alpha_{y,z} = gamma^0 gamma^{2,3}, gamma^1 anticommutes
   with both factors: two sign flips, so alpha_{y,z} -> +alpha_{y,z}.
   Hence p_x (x) alpha_x -> (-p_x) (x) (-alpha_x) = +p_x (x) alpha_x and
   the y, z terms are invariant: [T', h_0] = 0. Fixture: R A R = -A for
   A = -i(U_+ - U_+^T)/2 (reflection reverses ring orientation,
   R U_+ R = U_+^T), and alpha_x -> -alpha_x, so
   h_0 = A (x) alpha_x -> (-A) (x) (-alpha_x) = +h_0.

3. *Record-term invariance.* S = -i gamma^0 gamma^5: gamma^1 anticommutes
   with gamma^0 and with gamma^5; conjugation by i gamma^1 flips both
   signs: S -> +S. Spatial side: M and B_D are radial (ball indicator,
   b_D radial in |x|), so P_x M P_x = M, P_x B_D P_x = B_D exactly at the
   level of the compressed Galerkin matrices, because the quadrature
   grids are P_x-closed: the azimuthal grids have even counts (20, 24,
   28), so the node set is invariant under phi -> pi - phi (x -> -x) with
   equal weights, and the Hermite basis transforms with the exact parity
   signs. Fixture: R diag(1,1,0) R^{-1} = diag(1,1,0) — the ring
   reflection j -> 1-j swaps sites 0 and 1 and fixes site 2, so it fixes
   the sealed mask (this is R4(c): the reflection that fixes the mask).
   Hence T' (M (x) S) T'^{-1} = +(M (x) S).

4. *Connection anticonjugation.* Hermite: J(t) = -B_D(t) (x) alpha_x with
   B_D radial: T' J T'^{-1} = -B_D (x) (-alpha_x) * (-1)-bookkeeping =
   -J (spatial factor invariant, alpha_x -> -alpha_x). Fixture:
   J = (1/6) K_3 (x) alpha_x with K_3 = U_+ + U_+^T symmetric:
   R K_3 R = K_3, so T' J T'^{-1} = -J.

5. *Propagator and state.* T' h_lambda(t; a) T'^{-1} = h_lambda(t; -a)
   pointwise in t; conjugating every factor of the (exact or sealed
   discretized) time-ordered product gives u_lambda(-a) =
   T' u_lambda(a) T'^{-1}. Both pinned Hermite states are T'-invariant
   (mixed covariance: phat_x (x) alpha_x -> (-phat_x) (x) (-alpha_x);
   pure sea: [T', h_0] = 0, no zero modes). Fixture states: [T', h_0f]=0
   implies invariance of the kernel projector, the sea projector, and
   the mixed kernel-1/2 analogue (R fixes the k = 0 Fourier mode; the
   R4(d) convention is manifestly invariant — verified at machine
   precision below). Determinant conjugation invariance then gives
   D_lambda(-a) = D_lambda(a), hence Z(-a) = Z(a) and Z'(0) = 0. QED.

*Machine verification (A2):* Hermite: max
||u_lambda(-a) - T' u_lambda(a) T'^{-1}||_2 = 1.39e-15 (both ell, both
envelopes, all frozen parity pairs, all lambda); state invariance
<= 1.7e-15. Fixture (R4(c) operator (ring reflection) (x) (i gamma^1)):
max residual 1.09e-14; kernel/sea/mixed invariance <= 1.41e-15. All
inside 1e-12.

---

## Lemma 3 (recorded; antiunitary protection, control-4 amendment)

As recorded in the sealed control-4 amendment (blind-lane discovery):
Theta = (I (x) alpha_y) o K together with the time-symmetry of the sealed
pulse independently forces u_lambda(-a) = Theta u_lambda(a)^dagger
Theta^{-1}. This lane's verification: max residual
||u_lambda(-a) - A_y u_lambda(a)^T A_y||_2 = 3.39e-15 (Hermite, both ell,
both envelopes, all parity pairs; A_y = I (x) alpha_y). Statement and
proof responsibility for the sealed parity result remain with the
amendment's Lemma-3 obligation; this draft records the independent
machine confirmation only.

---

## Structural discovery of THIS run (control-4 v2 still protected)

The control-4 amendment pins the v2 falsifier (b_D center displaced to
x_0 = 1/10 AND J(t) multiplied by (1 + t/3)) and states: "If yet another
symmetry protects the broken variant, the gate blocks again with a new
named witness." That branch fired.

**Finding (machine-verified, mechanism partially characterized).** With
both v2 breakings active, Z'(0) remains numerically exact zero:
tangent-accumulation |Z'(0)| <= 8.8e-21 over all (ell, envelope, state)
cases, finite-difference cross-check consistent with zero at <= 2e-13.
The broken floor |Z'(0)| >= 1e-9 is therefore not met; the unbroken floor
(<= 1e-12) passes everywhere (max 3.0e-22).

**Characterization.** Define the linear transpose-type map
tau(X) = Omega X^T Omega^{-1} with Omega = I (x) alpha_y (equivalently the
antiunitary Theta_0 = Omega o K on Hermitian generators). Exact algebra
(machine-confirmed at exact zero):

```text
tau(h_0) = h_0;  tau(M (x) S) = M (x) S   (pointwise in t, no time
reflection used);  tau(R_spatial (x) alpha_{x or y}) =
-(R_spatial (x) alpha_{x or y})  for every REAL symmetric spatial factor.
```

Both v2 breakings preserve this reality class: displacing b_D's center
keeps B_D real symmetric, and a scalar time factor keeps J(t) in the
class pointwise. Empirically the first-order response D'_lambda(0)
vanishes at machine-exactness for EVERY connection in the reality class
— per history, both states, both envelopes, even with strongly
time-asymmetric J(t) (random real symmetric spatial factors, fresh at
every time step) and even with an artificially time-asymmetrized record
envelope; while a complex-Hermitian spatial factor escapes the
protection at first order (|dD| ~ 1e-4 under the same apparatus — the
apparatus demonstrably has teeth). At lambda = 0 the mechanism is fully
elementary: tr(P_- (R (x) alpha_j)) = 0 because the sea projector's
momentum structure is i*(real antisymmetric) while R is real symmetric.
The record-dressed (lambda != 0) annihilation is verified pointwise but
its complete operator proof is left to the mechanism-identification
obligation that a repaired control design will need; the tau-relation
above yields D(a) = D_rev(-a) (time-reversed profiles) exactly, which
kills the time-symmetric component of any conforming direction and is
already sufficient to show the v1 AND v2 designs cannot be satisfied by
b_D-displacement-plus-scalar-time-factor variants.

**Consequence (frozen rule).** The v2 falsifier is UNSATISFIABLE AS
PINNED by any conforming implementation. Per the sealed rule this is a
control failure: the gate blocks honestly with the new named witness

```text
CONTROL4_V2_DESIGN_DEFECT_REALITY_CLASS_PROTECTION
```

A satisfiable falsifier must leave the tau-reality class (e.g. a
complex-Hermitian spatial connection factor — verified to produce
|dD_lambda(0)| ~ 1e-4 — or a spin structure outside {real symmetric}
(x) alpha_j). That is a control-design repair decision for the
principal, not this lane's to make.

---

## B1 exact reductions used by Part B (recorded for the verifier)

1. In the exact h_0f eigenbasis (Fourier (x) alpha_x-eigenbasis) the
   fixture h_0f AND the sealed connection direction J_fix are BOTH
   diagonal: J_fix = (1/6) K_3 (x) alpha_x with K_3 circulant. Hence on
   the lambda = 0 branch everything commutes: u_0(a) =
   e^{-i h_0f} e^{-i a J}; F(0) = e^{2 i sqrt3} exactly; H(0) = 0
   exactly for the kernel-excluded sea state, and H(0) = -1/9 exactly
   for the mixed kernel-1/2 analogue (four kernel modes with j = +-1/3
   at half filling contribute -j^2/4 each). ||J_fix||_2 = 1/3 exactly.
2. lambda v_B = sqrt2 * (24 tau_R / pi) = 24 exactly: the v_B branch
   generator is constant, and the a-expansion blocks (U, U_1, U_2) are
   blocks of a single exact matrix exponential (Van Loan triple),
   certified by scaling-and-squaring Taylor with rigorous tail.
3. lambda v_A(t) = 32 pi r(t)^3 exactly, with integral pi: the v_A
   branch is computed by record-coupling Dyson partial sums in the
   interaction picture of h_0f (unitary dressing, single exponentials
   with frequencies in (sqrt3/2) Z), truncated at N = 24 with the
   certified pi^(N+1)/(N+1)! tails (a^0 tail: prefactor 1; a^1: ||J||;
   a^2: ||J||^2/2 by interleaving symmetrization), everything in
   certified midpoint-radius enclosures with exact-rational endpoints.
4. Lemma 1 collapses the pointer sum to Z = -(1/2)(D_sqrt2 - D_0); the
   amended verdict object is Xi(v) = F_v(sqrt2)[H_v(sqrt2) - H(0)] /
   [F_v(sqrt2) - F(0)] with Re and Im reported separately.

## B2 exact proof (pinned identically zero)

On the one-dimensional comparator all generator components are commuting
scalars; per history D_lambda(a) = exp(-i(eps + lambda sigma_v mu +
a j_0)), so log D is affine in a and d^2/da^2 log D = 0 identically
(sympy-verified exact zero), for every envelope. Hence H_v = H(0) = 0,
Xi(v_A) = Xi(v_B) = 0 identically, Delta_Xi_B2 = 0 exactly. Any
deviation would be an apparatus fault by the pinned R5 rule; none
occurred.

## B3 corrected toy assembly (amendment R3)

theta = sqrt2 sigma(1): theta_A = pi, theta_B = 24 exactly. kappa =
Jbar^2 Re{[1 - 2 e^{-i theta} Phi(sqrt2)]/[1 - e^{-i theta}]}. For the
envelope-A phase the exact reflection identity phi(1-t) = 2 pi - phi(t)
(from phi(1) = 2 sqrt2 sigma_A(1) = 2 pi exactly and r(1-t) = r(t))
reduces Phi_A to left-piece objects only:
Phi_A = 2 Phi_LL + g(1/2)^2 with Phi_LL = int_{0<s<t<1/2} e^{i phi(t)}
e^{-i phi(s)} and g(1/2) = int_0^{1/2} e^{-i phi}; the left phase
16 pi t^4 is a single monomial, so its certified exponential series is
well-conditioned (series truncated at 60 terms, sup tail
pi^61/61!). Exact
identity: [1 - 2 e^{-i theta} Phi] = [1 - e^{-i theta}] +
[e^{-i theta}(1 - 2 Phi)], and Xi_toy(v) = Jbar^2 e^{-i theta}
(1 - 2 Phi)/(e^{-i theta} - 1), hence kappa_v = Jbar^2 - Re Xi_toy(v)
and kappa_A - kappa_B = -Re[Delta_Xi_toy] EXACTLY (the amendment's
Re/Im-corner identity). Numerical values and certified enclosures are in
the primary JSON (kappa_A = 0.7070882 +- 3.6e-11 certified,
kappa_B = 0.5340003 exact closed form, difference 0.1730879 certified
nonzero), matching the expected 0.7071 / 0.5340.
