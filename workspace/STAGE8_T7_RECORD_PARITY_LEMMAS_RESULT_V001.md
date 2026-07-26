# Stage-8 T7 Record Parity Lemmas Result V001

Date: 2026-07-26

## Verdict

```text
RECORD_PARITY_LEMMAS_DERIVED
```

Four exact operator lemmas on the sealed completed-record chain, derived
and independently machine-verified by TWO lanes (gate-primary and blind),
under the sealed gate spec (5f7e9965…) + repair amendment (83ff0d4f…) +
control-4 amendment (f7f93be8…). Sealed independent of the gamma fork's
outcome, per the principal's disposition item 2 (unconditional yield).

Construction lane: Fable 5 (execution lanes) / Opus 5 (this seal) — see
STAGE8_LANE_MODEL_CHANGE_RECORD_V002.

## The lemmas

```text
L1 (lambda-parity).  T = I_spatial (x) gamma^5 is an involution with
   [T,h_0] = 0,  T (M (x) S) T = -(M (x) S),  T J T = +J,
   hence u_{-lambda}(a) = T u_lambda(a) T and D_{-lambda}(a) =
   D_lambda(a) exactly — both envelopes, all a, all record orders.

L2 (a-parity, amended involution).  T' = P_x (x) (i gamma^1), T'^2 = +I,
   Hermitian, with [T',h_0] = 0, T'(M (x) S)T'^{-1} = +(M (x) S),
   T' J T'^{-1} = -J, hence u_lambda(-a) = T' u_lambda(a) T'^{-1},
   Z(-a) = Z(a), Z'(0) = 0 exactly.

L3 (antiunitary a-parity).  Theta = (I (x) alpha_y) o K with the
   time-symmetric sealed pulse independently forces the same relation
   (discovered by the blind lane during control execution).

L4 (REALITY-CLASS PROTECTION — new; the deepest of the four).  The
   antiunitary Xi = (I (x) gamma^0 alpha_y) K satisfies
      Xi h_lambda(t;a) Xi^{-1} = -h_lambda(t;-a)  POINTWISE IN t,
   requiring only REALITY of B_D. Equivalently (primary lane's form)
   the transpose class tau(X) = (I (x) alpha_y) X^T (I (x) alpha_y)^{-1}
   fixes h_0 and the record term pointwise and is ODD on every
   J = (real symmetric spatial) (x) alpha_j. With the particle-hole
   relation (W^{-1} C W)^* = I - C holding exactly for BOTH pinned
   states, Z'(0) = 0 is annihilated at machine exactness CLASS-WIDE:
   for every history, both states, both envelopes, and every
   perturbation that keeps J in the class — including spatial
   displacement of b_D and arbitrary scalar time-asymmetry factors.
```

## Machine verification (two lanes, independent implementations)

```text
Primary lane (scaling-and-squaring apparatus per the amendment):
  Hermite n=2, both ell, N=96 sealed Strang assembly —
    L1 conjugation residual max 1.39e-15; L2 max 1.39e-15;
    state invariance (both pinned schemes, T and T') <= 1.8e-15;
  three-site fixture (R4(c) operator, ring reflection j -> 1-j):
    L1/L2 residuals <= 1.09e-14; kernel/sea/mixed invariance <= 1.41e-15;
  L3 Theta residual 3.4e-15.
Blind lane (own Higham Pade-13 expm; no shared code):
  L4 relation u_lambda(-a) = W u_lambda(a)^* W^{-1} residual <= 1.31e-15
    on the DOUBLY-BROKEN variant, all lambda, a in {7/100, 1/5};
  unbroken |Z'(0)| = 0.0 exactly (bit-identical Z(+-h)), both states.
Bar for every residual: <= 1e-12. All PASS.
Teeth control (lambda-odd table w~(lambda) = lambda/4, sealed ordering):
  |sum| <= 3.6e-16 (Hermite) / 3.8e-17 (fixture) vs the 1e-14 bar. PASS.
```

## Consequences of record

1. The V002 ER-gate stencil is proven EXACTLY odd-order-free (L2/L3/L4),
   retroactively hardening that sealed gate and deleting the odd-order
   component of every successor stencil's error budget.
2. The pointer-sum structure (m0 = m1 = 0 exactly) plus L1 fully
   explains the ~1e-13 vs ~1e-10 cancellation observed in the sealed ER
   insensitivity result — WITHOUT any envelope insensitivity. That
   observation is hereby attributed to these lemmas.
3. L4 is why successive falsifier designs (broken-P_x, then the
   double-symmetry-broken v2) both failed: a-parity is protected by a
   reality class, not by the individual symmetries the controls broke.

## Protected status

```text
record_parity_lemmas_sealed = true
gamma_refutation_computed = false
ER_A_selected = false
ER_B_selected = false
kappa_record_computed = false
alpha_computed = false
proof_authorized = false
```
