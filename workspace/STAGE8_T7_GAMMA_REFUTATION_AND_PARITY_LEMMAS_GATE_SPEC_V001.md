# Stage-8 T7 Gamma-Refutation and Parity-Lemmas Gate Spec V001

Date: 2026-07-25 (night)

## Status

```text
SPECIFICATION_SEALED_BEFORE_EXECUTION
```

Authorized by Brian's disposition (recorded:
/Users/bgm/MB Work/alpha_supervision/DISPOSITION_2026-07-25_gamma_
killtest_beta.md) on the gamma scoping memo (sealed da6d8cc7…). One gate,
two predeclared outputs: (A) the two exact parity lemmas as standalone
sealed theorems (unconditional, independent of the fork); (B) the gamma
kill-test — exact symbolic refutation computation with the verdict rule
and prediction frozen here. No selection of ER-A or ER-B may occur under
any outcome; the reparametrization-principle route is REFUSED by the
principal and may not be used.

## Pinned authorities

Three-site fixture: the sealed 12-dimensional periodic operator regression
of `STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_SPEC_V001.md` (2f2aa7f7…) /
`..._RESULT_V001.md` (76f5505e…) and its executor (3d8aea1a…), retained
per Phase-A A1 as a separate operator regression. Route-1 comparator: the
sealed one-dimensional closed forms and canonical result (6dbda44a…).
Record data: Phase-A spec A3 (789338ad…). Envelope profiles: the sealed
comparison branches (v_A(t) = tau_R·32·r(t)^3; v_B = 24·tau_R/pi) per
`STAGE8_T7_ENVELOPE_REALIZATION_COMPARISON_SPEC_V001.md` and the
critical-path scope correction (section 1). Gamma memo (da6d8cc7…) for
the reduction Xi(v) and the toy closed form. All hashes verified before
execution; drift blocks.

## Part A - Parity lemmas (statements frozen; proofs to be sealed)

```text
LEMMA 1 (lambda-parity). T := I_spatial (x) gamma^5 satisfies
  [T, h_0] = 0,  T (M (x) S) T = -(M (x) S),  T J T = +J,
hence u_{-lambda}(a) = T u_lambda(a) T and, for any T-invariant admitted
state, D_{-lambda}(a) = D_lambda(a) exactly — both envelopes, all a, all
record orders; exact under Galerkin compression and the sealed
quadratures (T acts on the spinor factor alone).

LEMMA 2 (a-parity). T' := P_x (x) gamma^1 satisfies
  [T', h_0] = 0,  T' (M (x) S) T' = +(M (x) S),  T' J T' = -J,
hence u_lambda(-a) = T' u_lambda(a) T'^{-1} and, for any T'-invariant
admitted state, D_lambda(-a) = D_lambda(a) exactly; hence Z(-a) = Z(a)
and Z'(0) = 0. Exact on the sealed quadrature grids (P_x-closed).
```

Obligations: (A1) full operator proofs written out (each step an exact
algebra identity: gamma-matrix anticommutation, radiality of M and B_D,
parity of the Hermite basis and quadrature grids); (A2) machine
verification at machine precision on the sealed Hermite carrier (n=2,
both ell) and on the three-site fixture: transported-conjugation
residuals ||u_{-lambda} - T u_lambda T||_2 and ||u_lambda(-a) -
T' u_lambda(a) T'^{-1}||_2 at frozen histories, plus state-invariance
checks for both pinned finite state schemes, all required <= 1e-12;
(A3) the two teeth controls: the lambda-odd weight vector
(0, -1/(2 sqrt 2), +1/(2 sqrt 2)) must give exactly zero completed sum
(machine <= 1e-14), and a predeclared P_x-BROKEN variant (b_D center
displaced to x_0 = 1/10 along x) must produce Z'(0) != 0 at a scale
exceeding 1e3 x its unbroken counterpart. Lemma results seal as
STAGE8_T7_RECORD_PARITY_LEMMAS_RESULT_V001 regardless of Part B's
outcome.

## Part B - Gamma kill-test (frozen verdict rule and prediction)

Compute, in EXACT arithmetic (rationals and symbolic transcendentals;
`.proof_deps` sympy admissible; no floating-point value may decide the
verdict):

```text
Delta_Xi := Xi(v_A) - Xi(v_B)
```

per the gamma memo's exact reduction (Xi(v) = F_v(sqrt2)·[H_v(sqrt2) -
H(0)] / [F_v(sqrt2) - F(0)]), at second order in a and to ALL record
orders, on:

```text
B1: the three-site periodic fixture (12-dim), with the fixture's sealed
    h_0, M, S analogues and the connection direction of its sealed
    regression, both envelope profiles;
B2: the Route-1 one-dimensional comparator (closed forms; degenerate
    cross-check);
B3: the toy model of the memo (S^2 = 1, {S, alpha_x} = 0, h_0 = 0,
    M = B_D = 1): its closed form must reproduce kappa_A != kappa_B
    symbolically (teeth control 5).
```

If the time-ordered structure on B1 does not admit an exact closed form,
the executor must document the obstruction and may use exact power-series
in the record coupling ONLY with a symbolically certified remainder bound
that decides the sign question rigorously; if no exact-decidable route
exists, return the BLOCKED arm — never a numeric verdict.

Negative controls (all six from the memo, frozen): (1) single-history
D_{sqrt2} must show envelope sensitivity (must NOT be annihilated);
(2) the split-history exhaustive kernel (p-weights, m0 = 1) must show
envelope sensitivity — this also polices the completed/exhaustive
substitution fence; (3) lambda-odd exact zero (Part A3); (4) broken-P_x
Z'(0) != 0 (Part A3); (5) the toy symbolic kappa_A != kappa_B; (6)
correlated-record variant: recorded as a labeled non-blocking observation
only.

## Predeclared verdicts (frozen; not revisable)

```text
GAMMA_REFUTED_NONZERO   iff Delta_Xi != 0 exactly (symbolically) on B1
                        (with B2, B3 and all controls consistent)
                        => gamma dead; beta proceeds per the principal's
                           disposition;
GAMMA_SURVIVES_EXACT_ZERO iff Delta_Xi = 0 exactly on B1 and B2 with all
                        controls behaving => a mechanism-identification
                        lane runs BEFORE any derivation spec;
GATE_BLOCKED            on authority drift, exactness unachievable, or
                        any control failure.
```

## Frozen prediction (calibration record)

```text
P1: GAMMA_REFUTED_NONZERO (per the memo's structural analysis; the
    principal has ordered this prediction not be revised).
P2: |Delta_Xi| on B1 scales as the fixture's ||J||^2 with an O(1)-to-
    O(10^-1) shape coefficient (toy analogy), i.e., unambiguously
    nonzero symbolically.
```

## Fences

No ER selection under any verdict. No reparametrization or equal-action
principle may be introduced (REFUSED by the principal). No measured
constant. No kappa_record computation. Fresh-context execution from this
sealed text; the lemma proofs and the symbolic verdict get independent
verification (a second fresh lane re-derives Delta_Xi's sign/zero status
from this spec without the primary's worksheets) before any result
seals. Failures preserved, never repaired.

## Protected status

```text
ER_A_selected = false
ER_B_selected = false
record_parity_lemmas_sealed = false
gamma_refutation_computed = false
kappa_record_computed = false
alpha_computed = false
proof_authorized = false
```
