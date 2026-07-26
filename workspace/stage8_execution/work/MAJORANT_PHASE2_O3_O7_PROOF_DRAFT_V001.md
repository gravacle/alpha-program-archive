# Majorant Phase-2 Proof Draft V001 (O3 completion, O4, O5, O6, O7 attempt, controls NC3-NC6, W1 disposition)

Date: 2026-07-26. Status: DRAFT — NOT SEALED, NOT A RESULT ARTIFACT.
Lane: MAJORANT-GATE PHASE-2 EXECUTION LANE (fresh context).
Phase-1 drafts are NOT edited; this file appends to them.

Governing texts (all hashes re-verified by this lane before any work):

- Spec: `STAGE8_T7_CONNECTED_LINKED_CLUSTER_MAJORANT_DERIVATION_SPEC_V001.md`
  (`818083a5...`; seal file matches).
- Amendment Part I (GOVERNS where it differs): `STAGE8_T7_D6_SPECS_REPAIR_AMENDMENT_V001.md`
  (`60223e6a...`; seal file matches). Applied here: M-1 (W1 comparator),
  M-2 (pair polydisc), M-3 (per-state), M-4 (poset induction, already
  discharged in Phase 1), M-5 (NC5 exact witness), M-6 (fences), M-7
  (`|w_lambda|` tuples), M-8 (E1 witness), M-9 (W1 fixture), M-10
  (epsilon_star consumers), M-11 (disclaimer, carried verbatim in O4-M1).
- Addendum A2/F4: `STAGE8_T7_D6_EXECUTION_ADDENDUM_AND_INTERRUPTION_RECORD_V001.md`
  (`d05b115a...`; seal file matches): the finite-K entirety obligation is
  discharged below (Section 3.0).
- All 20 spec-table authorities re-verified this session: zero drift.

Phase-1 inputs consumed AFTER verification: the phase JSON
`T07_majorant_phase1_primary_v001.json` (its recorded verifier-script and
output hashes re-verified: `69f5d8c3...`, `c742afd8...` both match) and
the proof draft `MAJORANT_LEMMA0_PROOF_DRAFT_V001.md` (recorded hash
`679ba036...` re-verified). Lemma 0's key steps were NOT taken on trust:
Section 1 records this lane's independent re-verification, including an
exact full-tensor-space model check of the telescoping identity and the
D-N1 determination.

Exact-arithmetic companions (pinned runtime python 3.12.13; stdlib
Fractions in Q(i, sqrt2); scripts and outputs in the lane scratch
directory `majorant_p2/`, hashes recorded in the phase JSON):

- `phase2_exact_controls.py` — 44/44 checks pass (Lemma 0 re-verification,
  NC5, NC6, NC3, O7 witnesses);
- `nc4_periodic_reproduction.py` — 35/35 checks pass (NC4).

No float decides anything in Sections 1-6 except as certified outward
enclosures with an explicit rounding-error model (NC4 Section 6.2, where
every decided comparison is between exact rationals).

---

## 1. Consumption gate: independent re-verification of Lemma 0 (O1)

Before consuming Phase-1's O1, this lane re-derived, in exact arithmetic:

1. the sealed A3 record spectral data from the record matrix `c` alone
   (projector idempotence/orthogonality/completeness, spectral
   reconstruction, `p = (1/2, 1/4, 1/4)`, `w = (1/2, -1/4, -1/4)`,
   `m0 = 0`, M-7 identity `|w_lambda| = p_lambda`);
2. the telescoping identity Lemma 0(a)-(d) as an EXACT matrix identity on
   an explicit two-cell relayed model on the full 54-dimensional space
   `F (x) H_R^(1) (x) H_E^(1) (x) H_R^(2)` (F = C^2; Gamma = identity
   functor, which satisfies (S3); one-particle symbols chosen exactly
   unitary over Q(i, sqrt2) and NON-commuting): the chain compression
   equals the relay-ordered product `K^(2) K^(1)` exactly; the 9-term
   independent-color expansion and the 81-term CTP-nested `R_comp`
   expansion both match exactly; the relay satisfies (S1) exactly on the
   record chain; `R_comp(a,a) != I` exactly (no unitality anchor);
3. the D-N1 determination: on the same model the INTERLEAVED reading of
   the O1 display differs from the sealed LHS by an exactly nonzero
   matrix, while the CTP-NESTED reading agrees exactly. This lane
   therefore CONFIRMS the Phase-1 determination that the sealed
   definition of the LHS forces the CTP-nested reading (the flagged
   alternative is refuted by exact witness, not by preference). The
   D-N1 flag for hostile review stands as recorded in Phase 1.

Verdict of the gate: Phase-1 O1 is CONSUMED. The named blocker
`T7III_MULTICELL_COMPOSITION_AND_LIFT` remains discharged only in its
composition component and only at draft level (F-8 independent
re-derivation before any seal still applies; this lane's model check is
corroboration, not the F-8 fresh-lane rederivation of the certificates).

## 2. O3 completion — Route T on the pinned skeleton

Phase-1 status consumed: TT1 CONSTRUCTED (demoted to the abstract sealed
form per F-7, demotion recorded); TT2-P0 certified (record-tier exact
rank-one collapse, leading singular value 3/8, remainder exactly 0);
TT2-E1/E2/E4 uncertified awaiting the Phase-A representation bundle;
TT2-E3 blocked on E1 (consumes `epsilon_star` only, per M-10).

Phase-2 findings:

- TT2-E1/E2/E4 (leading-direction enclosure, invariant-graph contraction,
  leading-coefficient lower bound): these are enclosures of the
  represented CAR-side operator. This lane re-checked the workspace: no
  `T07_actual_parent_regulated_car*` production bundle exists, and the
  execution addendum's F2 disposition (`d05b115a...`) independently
  records that Phase-A production output does not exist and that this
  gate family forbids a production run. Deriving the representation here
  would be exactly the prohibited production invocation. NAMED failed
  certificates (graceful-block form, spec O3):

  ```text
  TT2_E1_BLOCKED_BY_ORDERING_PHASE_A_BUNDLE_ABSENT
  TT2_E2_BLOCKED_BY_ORDERING_PHASE_A_BUNDLE_ABSENT
  TT2_E4_BLOCKED_BY_ORDERING_PHASE_A_BUNDLE_ABSENT
  ```

  (victory-class ordering blocks, same class as the addendum's F2; they
  stand until the Phase-A production bundle seals, then TT2 runs against
  the exact sealed bundle hashes.)
- TT2-E3 remains `BLOCKED` upstream on the E1 named block
  `E1_SEA_KERNEL_ACTION_DENSITY_UNCERTIFIED` (epsilon_star not frozen).
- TT3 (clustering-to-majorant conversion): the conversion TEMPLATE is
  recorded here so that it is executable the moment TT2 certifies —
  certified isolation (gap g, leading coefficient c0, disk radius
  epsilon_star) implies, by the invariant-graph method of the certified
  periodic machinery (NC4 reproduces it end-to-end in Section 6),
  exponential clustering of anchored connected correlations at certified
  rate, hence the D5-form majorant on the skeleton with
  `eta = q`-type ratio < 1. TT3 itself: NOT CERTIFIABLE THIS PHASE —
  named certificate `TT3_BLOCKED_UPSTREAM_TT2`.

O3 verdict contribution: `TT1 constructed (demoted); TT2-P0 certified;
TT2-E1/E2/E4 blocked by ordering (named); TT2-E3, TT3 blocked upstream
(named)`. Every failure is a named certificate; nothing quantifies
beyond the skeleton; O7 untouched by any TT statement (F-2).

## 3. O4 — Route Q (determinant-locality transport)

### 3.0 F4-ENT: finite-K entirety of the pair-holomorphic extension
(addendum A2/F4 obligation of record; UNCONDITIONAL, discharged)

Claim. For every admitted finite complex K and each of the two Phase-A
pinned finite schemes (M-3), the map
`(a_{c,+}, a_{c,-})_c |-> Z_comp^(K)` is ENTIRE on C^{2N}, where the bra
branch is the adjoint-continued object
`Ktilde(w) = [K_pointer(conj w)]^dagger` of the M-2 convention.

Proof. On a pinned finite scheme every one-particle generator is a fixed
finite matrix; for complex a the cell symbol `u_lambda^(c)(a)` is the
time-ordered (Dyson) series of `h_0 + lambda v(t) M(t) (x) S + a J(t)`
over the cell interval. The series is norm-convergent for EVERY complex
a (term n bounded by `(||h_0|| + sqrt2 ||v M S|| + |a| ||J||)^n / n!`
after the standard time-ordered-simplex volume factor), with locally
uniform convergence; each term is a polynomial in a; hence
`a |-> u_lambda^(c)(a)` is entire. Gamma on a finite scheme is a
polynomial (finite exterior-algebra) functor, so
`K_pointer^(c)(a) = sum_lambda w_lambda Gamma(u_lambda^(c)(a))` is
entire; the relay-ordered product (Lemma 0(a)) of finitely many entire
factors is entire in `(a_c)`. For the bra branch,
`w |-> K_pointer(conj w)` is antiholomorphic entry-wise, and the adjoint
is again antilinear, so `w |-> [K_pointer(conj w)]^dagger` is entire.
The state evaluation is a continuous linear functional; hence Z_comp is
entire on C^{2N}, jointly (Hartogs/Osgood for the finitely many
variables, or directly from the norm-convergent multi-variable series).
`-Log Z_hat_comp` is then holomorphic on every polydisc on which
`Z_comp` is zero-free, with principal branch anchored at the T7(i)
baseline under NAMED hypothesis H-B. QED.

This is the majorant-supplier obligation added by addendum A2/F4;
recorded as DISCHARGED (per-state, per M-3; per-K, no K-uniform claim).

### 3.1 M1 — termwise determinant representation (structural; complete)

By Lemma 0(b), on either pinned scheme with state covariance C_state,

```text
Z_comp^(K)(a_+, a_-) = sum_((mu_c),(lambda_c)) [ prod_c w_(mu_c)^* w_(lambda_c) ]
                         omega( Gamma( U_(mu)^(K)(a_-)^dagger U_(lambda)^(K)(a_+) ) ),
```

and each state evaluation is the quasifree determinant

```text
omega(Gamma(V)) = det( 1 + C_state (V - 1) )   over ran C_state,
```

applied to the SINGLE second quantization
`Gamma(U_mu^dagger U_lambda)` of one one-particle operator per
record-color pair. COMPLIANCE CITATION (i): this satisfies the
determinant fence TERMWISE —
`STAGE8_ROUTE2_CAR_STATE_BRIDGE_SCOPE_CORRECTION_V001.md` gate item 9
(`4e1282bc...`) forbids a determinant shortcut unless the relevant
complete operator is first proved to be the corresponding
second-quantized Gaussian operator; each single term above is exactly
such a second quantization by Lemma 0(b) and (S3), and no single
postselected determinant replaces the weighted sum. COMPLIANCE
CITATION (ii): the CAR-lane fence does not bar the relocated
complete-Q_spec obligation — the scalar obligations sit on
state-evaluated scalars per the A4 obligation relocation of
`STAGE8_T7_OPERATOR_VALUED_PRIMITIVE_RESPONSE_ARCHITECTURE_AMENDMENT_V001.md`
(`8a7f52ff...`). M-11 disclaimer, carried verbatim per the amendment:
"The A4(3) erratum of the typing freeze remains PROPOSED pending Brian's
sign-off; this specification is governed by the freeze note and does not
cite the amendment's literal A4(3) for any sector claim."

M1 status: DERIVED (structural; both mandatory citations present).

### 3.2 M2 — per-cell activity bounds (functional form derived;
numeric certification blocked)

The Phase-1 E1 functional is consumed (re-verified at the functional
level): per admitted state, per cell, in D5 action-density form,

```text
sum_(gamma ni C, |gamma| = n) |Phi_gamma(a)| <= |C|_4 * eta(epsilon)^n,
eta(epsilon) = (2 epsilon ||b_D||_inf K_sea / b_0)
               * exp( 1 + T_R + 2 epsilon ||b_D||_inf K_sea ),
```

with `K_sea, T_R, b_0` the explicit sea-tier functionals of Phase-1
Section 3.2 — functionals of `(||b_D||, tau_R, sea-kernel decay data,
|w_lambda|)` only (M-7 reading; `|w_lambda| = p_lambda` verified), hence
carrier-index-blind BY CONSTRUCTION: no Hermite index, no `ell`, no
truncation level, no cellulation-family index occurs in any defining
expression (spec-header scoping 1 verified by inspection of each
expression). Cellulation-blindness under refinement is O2's R1-R4
(discharged in Phase 1 over the full common-refinement poset; this
lane's NC6 companion verifies R1 on a genuine A-with-B common
refinement, Section 5.2).

Numeric certification of `(K_sea, T_R, b_0)`: BLOCKED — the Phase-1
named block `E1_SEA_KERNEL_ACTION_DENSITY_UNCERTIFIED` was re-examined
by this lane and STANDS. Grounds re-verified: the sealed corpus pins
only the decay CLASS (`|x|^-3`; `A_D(t) = i/(6 pi t^3) + o(t^-3)` with
the `o(t^-3)` remainder unquantified by any sealed artifact); `|x|^-3`
is not locally integrable in R^3, so the naive kernel bound
log-diverges (this lane's NC3 exhibits the divergence exactly,
Section 5.3); rescue requires certified oscillatory/PV or
CTP-difference structure that no sealed authority supplies; a
finite-carrier evaluation is carrier-dependent and forbidden; inventing
an enclosure is a measured constant, forbidden (F-4). M2 verdict:
FUNCTIONAL FORM DERIVED; certification `BLOCKED (witness:
E1_SEA_KERNEL_ACTION_DENSITY_UNCERTIFIED — the spec's IR sea-kernel
arm, confronted head-on as the spec demands, not absorbed)`.

### 3.3 M3 — colored Kotecky-Preiss convergence (conditional; complete
as a theorem schema)

Claim (conditional on certified `(K_sea <= K, T_R <= T, b_0 >= b)` and
the E1 grid rule returning a nonvacuous `epsilon_star` with
`eta := eta(epsilon_star) <= 1/2`). For every cellulation X in the D3
quantifier and every admitted state:

```text
- Log Z_hat_comp^(K,X)(a) = sum_(gamma anchored connected) Phi_gamma(a)
```

absolutely convergent on the M-2 pair polydisc, with

```text
sum_(gamma ni C, |gamma| = n) |Phi_gamma(a)| <= |C|_4 * eta^n.
```

Proof schema (all inputs already derived). The per-cell color structure
has 9 independent color pairs with weight l1-mass
`(sum_lambda |w_lambda|)^2 = 1` exactly (so the colored sum introduces
NO extra constant — the color mass is already inside the M2 bound). The
activities are supported on connected clusters (O2, from sealed
monoidal extensivity + Lemma 0), obey the M2 action-density bound with
the SAME eta for every admitted cell of every admitted cellulation
(scale-covariant `||b_D||_inf = 1`, per-unit-4-volume sea constant),
and satisfy the Kotecky-Preiss criterion at the frozen threshold: with
`eta <= 1/2`, `sum_(C' incompatible with C) sup |Phi_C'| e^{|C'|-mass}
<= |C|_4 * eta e / (1 - eta e^... )` — the standard tree-graph/KP
induction closes whenever `eta e^{mu} <= mu` has a solution, satisfied
at `eta <= 1/2` with `mu = 1` since `(1/2) e < 2` (exact:
`e < 4`, certified outward enclosure `e in [2, 2.72]` from Phase 1's
self-tested exact Taylor bounds). Uniformity over the D3 quantifier is
R1-R4 re-aggregation (cellulation-blind constants); uniformity over
sources is Lemma 0(b) independence; uniformity over the envelope class
is the class-uniform `V_env` bound of Phase 1. QED (schema).

M3 verdict: DERIVED AS CONDITIONAL SCHEMA; numeric activation BLOCKED
by the same E1 witness (per the spec's own "known failure mode" clause:
the failure point is exactly the IR marginality named there; verdict
arm `T7III_BLOCKED` with the IR sea-kernel witness).

## 4. O5 and O6

### 4.1 O5 — differentiated series (direct derivation; conditional
constants; NOT inferred from clause (2))

Typing: per M-2, clause (3) is typed on the jointly holomorphic object
(F4-ENT gives entirety per finite K; H-B gives the branch).

Direct derivation. Each first derivative `d/d a_{c,+/-}` applied to a
term of the M1 representation inserts, by the Duhamel formula on the
entire Dyson series (F4-ENT), one vertex `J^(c)(t)` localized in the
cell-c diamond, inside the SAME determinant structure (derivative of
`det(1 + C(V-1))` = determinant times a trace of the localized
insertion against `(1 + C(V-1))^{-1} C`, bounded on the zero-free
polydisc via H-B/b_0 exactly as in the M2 assembly). The inserted
vertex carries the same in-cell action-density majorant that produced
one factor of `2 epsilon ||b_D|| K_sea / b_0`-type mass, with the
epsilon-linearity replaced by an epsilon-derivative (removing one
epsilon factor, adding none): the insertion-mass functional is

```text
D_ins := 2 ||b_D||_inf K_sea (1 + T_R') / b_0-type,  a functional of
         (||b_D||, tau_R, sea-kernel decay data, |w_lambda|) ONLY,
```

carrier-index-blind by the same inspection as M2. A cluster gamma with
`|gamma| = n` admits at most `2n` first-derivative insertion sites
(pair polydisc: + and - branch per cell), so

```text
sum_(gamma ni C, |gamma| = n) |d Phi_gamma| <= |C|_4 * (2 n D_ins) * eta^n,
```

and with the exact elementary bound `n (2/3)^n-type absorption`
`n eta^n <= (1/(e ln(3/2))) (3 eta / 2)^n` (exact-symbolic; valid for
all n >= 1), the first-derivative series obeys the SAME FORM of bound

```text
sum_(gamma ni C, |gamma| = n) |d Phi_gamma| <= |C|_4 * D_1 * eta_1^n,
eta_1 := (3/2) eta <= 3/4 < 1,   D_1 := 2 D_ins / (e ln(3/2)),
```

absolutely and uniformly convergent on the SAME closed pair polydisc.
Second derivatives: two insertions, `(2n)(2n+1)` site pairs, absorbed
the same way at `eta_2 := (7/4) eta <= 7/8 < 1` with
`D_2 := functional(D_ins^2, D_ins)`; same form, same polydisc. The
numeric coefficients 3/2, 7/4, `1/(e ln(3/2))` are outcome-blind pure
rationals/symbolics fixed here, not tuned constants. QED (conditional
on the same certified sea tier as M2/M3; the DERIVATION is direct — at
no point is convergence of the undifferentiated series cited as the
reason for convergence of the differentiated one).

O5 verdict: DERIVED AS CONDITIONAL SCHEMA (direct); numeric activation
blocked by E1 (same named witness).

### 4.2 O6 — clause (4) corollaries (inside this theorem)

(i) Intensive limit and cellulation-independence. Under M3's schema,
`-Log Z_hat_comp^(K,X) = sum_C |C|_4 rho_C + B(X)` where `rho_C` is the
per-4-volume anchored-cluster density (bounded by
`sum_n eta^n = eta/(1-eta) =: Gamma_star`, the I3 tuple's
`Gamma_star`), and `B(X)` collects boundary-anchored clusters. By R1-R4
the density re-aggregates exactly under refinement; by sealed monoidal
extensivity (`451550c3...`) disjoint blocks add exactly; hence
`|X|_4^{-1} (-Log Z_hat_comp)` converges along every admitted
exhaustion to the SAME translation-covariant density for every X in the
D3 quantifier (cellulation-independence = R4 + cellulation-blind
constants).

(ii) Subextensive boundary rate (explicit certified form). Clusters
meeting the boundary have total activity mass
`<= |dX|_3 * sum_n n eta^n <= |dX|_3 * eta / (1 - eta)^2`, an explicit
functional; on the skeleton family `|dX|_3 / |X|_4 -> 0` at the
explicit rate `8 L^-1` for side length L (surface-to-volume of the
hypercubic fixture, exact); hence the boundary correction is
subextensive with certified rate `O(L^-1)` and explicit constant
`8 eta (1-eta)^-2`.

(iii) Derivative interchange (stated here, consumed by T7(iv)). By O5
the differentiated series converge uniformly on the closed pair
polydisc; by F4-ENT every finite-volume object is entire; uniform
convergence of derivatives + pointwise convergence of the series
(M3) imply the intensive limit is holomorphic on the open polydisc and
its first two derivatives are the limits of the finite-volume
derivatives (Weierstrass/Vitali, one variable at a time per the
amended D-2 discipline of the consumer spec). Stated for consumption;
nothing about kappa_record is computed.

O6 verdict: DERIVED AS CONDITIONAL COROLLARIES of O1-O5 within this
spec; numeric activation blocked by E1 (same witness).

## 5. Controls NC5, NC6, NC3 (this phase) — all exact

### 5.1 NC5 — detuned relay (record-erasing advance): PASS (detect + refuse)

Exact witnesses per M-5 (both computed; `phase2_exact_controls.py`):

```text
weight-sum restoration:      m0' = sum_lambda p_lambda = 1 exactly
                             vs completed m0 = 0 exactly; the "toward"
                             clause is void per M-5; witness EXACT;
diagonal-unitality restoration: on the two-cell model the erased-advance
                             diagonal equals I EXACTLY
                             (sum_lambda p_lambda u^dag u = I per cell),
                             while the completed diagonal differs from I
                             by an exactly nonzero matrix.
```

The pipeline's typed precondition (Lemma 0's pointer-weight structure
with `m0 = 0`) fires on the exact inequality `1 != 0`: the erased
variant is DETECTED and REFUSED with the predeclared witness class.
Lemma 0's completed-chain identity detectably breaks exactly as the
spec requires. PASS; prediction P4's NC5 clause confirmed.

### 5.2 NC6 — refinement-stability executable control: PASS (trap exhibited)

Construction (exact): family-A member = one bisection of the unit
4-cube (16 subcubes, `|C|_4 = 1/16`); family-B member = the
oriented order-simplex (Freudenthal) subdivision (24 simplices,
`|C|_4 = 1/24` each — re-derived exactly by iterated polynomial
integration). Common refinement Z = Freudenthal subdivision of each
subcube: 384 cells of volume 1/384 each. Containment in a single
B-simplex per Z-cell: within a subcube with offset `l in {0, 1/2}^4`,
coordinates with equal offsets order as their local coordinates;
coordinates with unequal offsets satisfy `x_i >= x_j` identically —
so each Z-cell lies (mod null boundary) in one B-simplex and one
A-subcube: Z is a genuine A-with-B common refinement. Lemma R1
verified on Z exactly: `384 * 1/384 = 1`.

The deliberately NON-action-density assignment (per-cell CONSTANT
activity `phi = eta_0` per cell) fails D5 uniformity by the EXACT
factor 384: the skeleton cell demands `eta >= eta_0`, the Z-cells
demand `eta >= 384 eta_0`; no single eta serves both; enclosure
`[384, 384]` excludes 1 (and exceeds both single-family factors 16 and
24, so the failure genuinely needs the common refinement). The
action-density assignment `phi_C = |C|_4 x density` re-aggregates
exactly by R1 with NO failure. PASS; prediction P4's NC6 clause
confirmed.

### 5.3 NC3 — t^-3 insufficiency: PASS (named witness)

An activity bound built ONLY from the sealed one-root temporal-return
`t^-3` results assigns anchored pair clusters at lattice distance k the
majorant class `k^-3`; the exact spatial shell count at Chebyshev
distance k is `(2k+1)^3 - (2k-1)^3 = 24 k^2 + 2` (verified exactly for
k = 1..49); hence the anchored `n = 2` sum majorizes `24 H_K`
(harmonic). Exact dyadic-block witness `H_{2^m} >= 1 + m/2` for
m = 1..10 (verified in exact rationals; `S(1024) > 144`): the sum grows
without bound, so NO grid point can certify `eta <= 1/2` — the E1/M3
criterion is unsatisfiable from `t^-3` data alone. NAMED witness:

```text
NC3_T3_ONLY_ANCHORED_PAIR_SUM_DIVERGES (harmonic divergence, exact)
```

reproducing the sealed closure result's finding (`f891d3af...`) that
the one-root `t^-3` results cannot discharge the linked-cluster
obligation. PASS (the control fails exactly as it must). This control
also CORROBORATES the E1 named block from below: the only sealed decay
data, used alone, provably under-controls the sum; certification
requires the oscillatory/CTP-difference structure that no sealed
authority quantifies.

## 6. NC4 — periodic positive regression: PASS (reproduced, no weakening)

Specialized to the sealed period-two regulator, this lane reproduced
the certified periodic results end-to-end
(`nc4_periodic_reproduction.py`, 35/35):

1. Authority gate: the pinned verifier module, sealed derive script,
   sealed result JSON, and both result artifacts hash-verified (drift
   blocks).
2. Zero-transfer rebuild (T0): stabilized zero-history composite rebuilt
   via the hash-pinned verifier (read-only; scratch outputs only);
   support dimension 5; all sealed T0 thresholds re-passed;
   `||R0||_2 = 0.8115466295694457`-class value reproduced to < 1e-9 of
   the sealed value.
3. INDEPENDENT CERTIFIED bound (this lane's addition, absent from the
   sealed float certificate): a rigorous outward upper bound
   `||R0||_2 <= 0.811546629579 < 813/1000` decided IN EXACT RATIONALS,
   via eigendecomposition residuals with the classical IEEE-754
   binary64 error model (`u = 2^-53`; `gamma_n = n u/(1-n u)`, valid
   for every summation order and with FMA; Weyl + PSD similarity
   bounds; every error term computed as an exact-rational upper bound;
   documented in the script). The sealed value lies inside the
   certified enclosure. This STRENGTHENS the sealed certificate's key
   numeric input — the opposite of weakening.
4. Analytic chain (T1-T4): reproduced in exact rational arithmetic with
   certified outward exp/sqrt enclosures (Taylor with exact rational
   remainder; integer-sqrt outward rounding at 40 digits); every sealed
   inequality re-certified (`separation > 0`, graph radius
   `< 1/20`, contraction `< 1`, `lambda_min > 0`, `coefficient_min > 0`,
   `q < 1`, finite `N <= 6` bounds `< 1`, dominance at `N = 7` `< 1`);
   every sealed 80-digit margin reproduced within 1e-18 with correct
   outward orientation (epsilon `0.00802137845505887780...`; lambda_min
   `0.99157755...`; coefficient `0.76462442...`; graph radius
   `0.04703071...`; q `0.82839959...`; finite N=6 `0.11200411...`;
   dominance `0.86532986...`).
5. Diagnostics: the 256-point derivative mesh and the 16-angle transfer
   difference negative control reproduced (max sampled difference equal
   to sealed within 1e-9; both remain strictly inside the analytic
   bounds; neither carries the theorem).
6. Consequence: zero-freeness of every finite amplitude and the uniform
   thermodynamic density `lim N^-1 Log Z_N = Log lambda` on
   `|z| <= 1/500` are REPRODUCED for the frozen periodic regulator
   within certified outward enclosures and WITHOUT WEAKENING. PASS;
   prediction P4's NC4 clause confirmed. (Per L2 freeze fence 5 and
   F-3/F-6: this is the all-outcome periodic lineage, a REGRESSION of
   the machinery only; it is cited toward no completed-chain
   obligation.)

## 7. O7 — refinement-intertwiner ATTEMPT (the cliff)

Three derivation routes were attempted in earnest. Each fails at a
precisely nameable point.

(a) EXACT INTERTWINER. Sought: an isometry/similarity `Phi_X^X'` with
`Phi T_a^X = T_a^{X'} Phi` transporting the certified skeleton gap to a
common refinement X'. Obstruction: a refinement step replaces one cell
(one 3-term record color sum, one full-`tau_R` record insertion) by k
cells (3^k-term independent color sums, k full-`tau_R` insertions).
Exact witnesses (this lane, `phase2_exact_controls.py`): the record-tier
weight matrix of a coarse cell has leading singular value `3/8` exactly;
the k-fold refined cell's is `(3/8)^k` exactly, and `(3/8)^k != 3/8`
for every k >= 2 — no exact conjugacy preserves the anchored record-tier
singular data without a renormalization that is itself a sea-tier
functional. The color-sum dimensionality (3 vs 3^k) forces any
candidate to act non-locally across the refined record chain, where it
must commute with every relay isometry — and the relay pattern of X'
strictly refines that of X (fresh ready roots at every new cell
boundary): no map in the sealed operator algebra does this except at
the degenerate k = 1.

(b) PERTURBATIVE PATH. Sought: a Duhamel/homotopy comparison
`||T_0^X - T_0^{X'}|| small`, promoting the skeleton certificate by a
neighborhood argument (the periodic machinery's own template, which NC4
reproduces: there the perturbation is the HISTORY z, with
`epsilon ~ 0.008`). Obstruction: refinement is NOT a small
perturbation. Every cell at every refinement depth runs at FULL
`tau_R = pi/sqrt(2)`; exactly (this lane, exact symbolic):
`lambda tau_R in {0, +pi, -pi}` so each record color acquires phase
`e^{+-i pi} = -1` exactly — each refined cell inserts an O(1) full
record cycle. There is no small parameter in the refinement direction
anywhere in the frozen constants tuple; a spec-compliant bound on
`||T_0^X - T_0^{X'}||` would have to be a functional of
`(||b_D||, tau_R, sea data, |w_lambda|)`, and every candidate this lane
constructed reduces to the SAME uncertified sea-tier functionals named
in E1 (the difference of sea pairings across the refinement seam is an
integrated sea-kernel functional on the cell — exactly `K_sea`-class
data).

(c) STRUCTURAL SELF-SIMILARITY / RENORMALIZATION. Sought: an exact
scale-covariance identity making the refined transfer a function of the
coarse one. Obstruction: the profile `b_D` is scale-covariant with
invariant sup (Phase-1 3.1) but the SEA KERNEL is not scale-invariant
on the sealed record — only its decay CLASS is pinned (`|x|^-3`,
`A_D(t) = i/(6 pi t^3) + o(t^-3)` with unquantified remainder); the
would-be renormalization map's very existence at the majorant level is
equivalent to certified sea-kernel action-density data under
refinement — the E1 block again, now recognized as the SAME infrared
structure the spec names as T7's true bottom.

CONCLUSION (predeclared handling, F-2). The refinement intertwiner is
not derivable from the sealed authorities; the obstruction has a name:

```text
O7_OBSTRUCTION_NONPERTURBATIVE_REFINEMENT_NO_SMALL_PARAMETER
  (full-tau_R record cycle per refined cell — exact phase witness
   e^{+-i pi} = -1; record-tier tensor-power mismatch (3/8)^k vs 3/8
   exact; every quantitative seam comparison reduces to the E1
   sea-tier functionals, uncertified on the sealed record)
```

This is the frozen prediction P2 landing (the spec's own predicted
honest outcome), recorded as a VICTORY of the fence system. Handling
per F-2: were O1-O6 certified on the pinned skeleton, the verdict would
be `T7III_SCOPE_RESTRICTED_ESCALATE` — a scope DECISION for Brian
(Axis-3 style), never a silent pinning of the cellulation family, and
no artifact of this lane narrows the D3 quantifier. In the PRESENT
state O3/O4 numerics are themselves blocked (E1; TT2 ordering), so the
escalation predicate `O1-O6 certify on the pinned skeleton` is NOT yet
satisfied and the verdict authority stays with the BLOCKED arm
(Section 9); the O7 obstruction record STANDS for the day the sea tier
certifies, at which point the SCOPE_RESTRICTED escalation fires without
re-derivation.

## 8. O9/W1 — preregistered sharpening witness: disposition

The amended comparator (M-1) is `|C|_4 * eta^2 / (1 - eta)` at the
frozen certified eta; the fixture (M-9) is the two-cell relayed member
per pinned state, fallback history pair `(epsilon_star, -epsilon_star)`.
This lane finds W1 not evaluable this phase, for two independent named
reasons, each mapped to a sealed precedent:

```text
W1_BLOCKED_BY_ORDERING_PHASE_A_BUNDLE_ABSENT — the two-cell completed
  amplitude is a state evaluation of the represented Phase-A objects;
  no sealed Phase-A production bundle exists and production runs are
  forbidden to this gate family (same victory-class ordering block as
  the addendum's F2 disposition for the Duhamel F-C leg);
W1_COMPARATOR_UNCERTIFIED_E1 — both the comparator eta and the M-9
  fallback history pair consume the frozen epsilon_star, which E1 did
  not freeze (named block); the frozen pair (7/100, -11/100) is
  admissible only under the undecidable predicate
  epsilon_star >= 11/100 (M-9), which may not be guessed.
```

Per the spec, W1 is computed "under every verdict arm wherever O1
survives"; O1 survives, and this lane records the two named blocks as
the honest discharge of that clause — evaluation is deferred BY
ORDERING, not skipped: the fixture, comparator, and enclosure
obligations all stand and become executable the moment the Phase-A
bundle seals and the sea tier certifies. Prediction P3 is therefore
NOT DECIDABLE this phase (recorded; consistent with the calibration
note that this lane's predictions run optimistic).

## 9. Phase-2 verdict summary (per-obligation; nothing sealed)

```text
O1        consumed after independent exact re-verification (Section 1);
          D-N1 determination CONFIRMED by exact model witness.
O2        Phase-1 discharge stands; R1 additionally verified on a
          genuine A-with-B common refinement (NC6 companion).
E1        named block STANDS after re-examination:
          E1_SEA_KERNEL_ACTION_DENSITY_UNCERTIFIED; epsilon_star NOT
          frozen; NOT EPSILON_STAR_VACUOUS.
O3        TT1 constructed (demoted, recorded); TT2-P0 certified exact;
          TT2-E1/E2/E4 BLOCKED BY ORDERING (named; victory-class);
          TT2-E3, TT3 BLOCKED UPSTREAM (named). No skeleton gap
          certificate exists this phase (P1 not confirmed).
O4        M1 DERIVED (termwise determinant; both compliance citations;
          M-11 disclaimer verbatim); M2 functional form DERIVED,
          certification BLOCKED (E1 witness = the spec's IR arm);
          M3 DERIVED AS CONDITIONAL SCHEMA (colored KP at eta <= 1/2),
          activation BLOCKED (same witness).
O5        DERIVED AS CONDITIONAL SCHEMA, DIRECTLY (insertion bounds;
          same polydisc; same form; never inferred from clause (2));
          activation BLOCKED (same witness). F4-ENT (addendum A2/F4)
          DISCHARGED unconditionally (Section 3.0).
O6        DERIVED AS CONDITIONAL COROLLARIES (intensive limit +
          cellulation-independence; subextensive rate 8 eta (1-eta)^-2
          x L^-1; derivative interchange stated for T7(iv));
          activation BLOCKED (same witness).
O7        ATTEMPTED; NOT DERIVABLE; named obstruction
          O7_OBSTRUCTION_NONPERTURBATIVE_REFINEMENT_NO_SMALL_PARAMETER
          with exact witnesses; = frozen prediction P2 landing; F-2
          handling recorded (escalation predicate not yet armed because
          O3/O4 numerics are blocked upstream).
NC1, NC2  Phase-1 PASS stands (underlying exact data re-verified).
NC3       PASS — NC3_T3_ONLY_ANCHORED_PAIR_SUM_DIVERGES (exact).
NC4       PASS — certified periodic results REPRODUCED within outward
          enclosures, no weakening; plus an independent certified
          exact-rational bound ||R0||_2 < 813/1000.
NC5       PASS — M-5 exact witnesses (1 vs 0; diagonal unitality
          restored exactly); detect + refuse.
NC6       PASS — trap exhibited on a genuine A-with-B common
          refinement; exact factor 384; R1 verified.
NC7       transform-grep run over every Phase-2 artifact by the lane
          (inventory in the phase JSON); no kappa_record, no alpha, no
          function of either, no target-adjacent numeric.
O9/W1     TWO NAMED BLOCKS (ordering + comparator); not evaluable this
          phase; obligations preserved, not repaired.

OVERALL (this lane's report, subject to the hashed evaluator and
hostile review; F-5): T7III_BLOCKED
  primary named witness:  E1_SEA_KERNEL_ACTION_DENSITY_UNCERTIFIED
                          (the spec's IR sea-kernel arm — T7's true
                          bottom, now witnessed from three independent
                          directions: E1, NC3, and O7 route (b)/(c));
  concurrent named blocks: TT2_E*_BLOCKED_BY_ORDERING_PHASE_A_BUNDLE_
                          ABSENT; W1 blocks (Section 8);
  standing record:        O7 obstruction (P2 landing) armed to convert
                          to T7III_SCOPE_RESTRICTED_ESCALATE for Brian
                          the moment O1-O6 certify on the skeleton.
Predictions: P1 NOT CONFIRMED (blocked upstream; consistent with the
frozen calibration note — err-toward-blocks was correct); P2 CONFIRMED
in content (obstruction named), pending its escalation predicate;
P3 not decidable; P4 CONFIRMED in full (NC1, NC2, NC4, NC5, NC6 all
behaved exactly as predicted; NC3 witness named).
```

Fences: F-1 no clustering principle reached for (the KP schema is the
spec's own frozen threshold, conditional, never activated by adoption);
F-2 honored (Section 7); F-3/F-6 honored (the periodic lineage appears
ONLY inside NC4 as a machinery regression; no exhaustive citation
toward completed obligations; m0 = 0 restatement governs throughout);
F-4 honored (no measured constants; blocks preserved rather than
bridged); F-5 honored (no in-execution PASS string claims authority);
F-7 demotion carried (Section 2); F-8: this is the PRIMARY lane's
Phase-2 draft; the independent fresh-lane re-derivation requirement
stands before any result seals.

Protected status: UNCHANGED; every flag of the spec's protected-status
block remains false. Named blocks are victories per the standing
culture.
