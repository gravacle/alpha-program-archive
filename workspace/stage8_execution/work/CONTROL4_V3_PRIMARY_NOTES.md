# Stage-8 T7 Control-4 v3 — PRIMARY LANE derivation notes

Date: 2026-07-26. Lane: PRIMARY (fresh context). Write-scope: this scratch
directory only. No workspace write, no blind-lane read, no production-lane
invocation, no measured constant.

Result JSON: `T07_control4_v3_primary_v001.json` (same directory).

---

## 0. Seal verification (drift blocks; all three PASS)

| Authority | Sealed SHA-256 | Recomputed | Match |
|---|---|---|---|
| `STAGE8_T7_CONTROL4_V3_SPEC_V001.md` | `557c68a1aa5f75129dceb9261c393216a4e873a54ccbfc17915a0d0205fa8589` | identical | yes |
| `STAGE8_T7_CONTROL4_CONDITION1_SAME_APPARATUS_RESULT_V001.md` | `608eafb26c70cf3a4f2dc7b76e702eefcebf51514d37e72ab264663c20f78d47` | identical | yes |
| `STAGE8_T7_GAMMA_GATE_CONTROL4_V3_CONDITIONAL_AUTHORIZATION_V001.md` | `67bb5cff532523daa60600bbd69517e4edf353d0425d255ae03e453567e6c271` | identical | yes |

Apparatus texts consulted (read-only, unmodified): Phase-A spec
`STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md`
(A1–A6), `STAGE8_T7_HERMITE_GALERKIN_BASELINE_SPEC_V001.md`,
`STAGE8_T7_GAMMA_GATE_CONTROL4_REPAIR_AMENDMENT_V001.md` (apparatus note),
`STAGE8_T7_ENVELOPE_REALIZATION_COMPARISON_SPEC_V001.md`,
`STAGE8_T7_GAMMA_REFUTATION_AND_PARITY_LEMMAS_GATE_SPEC_V001.md`,
`STAGE8_T7_RECORD_PARITY_LEMMAS_RESULT_V001.md`.

## 1. Apparatus (independent reconstruction)

Carrier n = 2, ell in {1, sqrt2}; spatial dim 8, total dim 32. Basis order
lexicographic `(a,b,c,s)` with s fastest, so the spatial index is
`i = 4a + 2b + c`. Dirac representation, `alpha_j = gamma^0 gamma^j`,
`S = -i gamma^0 gamma^5`. `h_0 = sum_j p_j (x) alpha_j` from the exact
Hermite ladder momenta. Causal ball `r(t) = min(t, 1-t)`,
`M(t) = Q 1_{|x|<=r(t)} Q`, sealed spherical quadrature (10 radial,
10 polar-cosine, 20 azimuthal). Envelope A `v(t) = tau_R · 32 r(t)^3`
(tau_R = pi/sqrt2) is the pinned Phase-A envelope; envelope B
`v = 24 tau_R/pi` is also executed and reported. Record data
`lambda = (-sqrt2, 0, +sqrt2)`, `w = (-1/4, 1/2, -1/4)`. Both pinned finite
states: `C_mix = Q P_- Q` (20^3 Gauss-Hermite) and
`C_pure = 1_{(-inf,0)}(h_0)` (rank 16). Strang N_t = 48,
`Step_lambda = F A G_lambda A F` at midpoints `t_k = (k+1/2)/48`.

Smooth connection profile `b_D(t,x) = exp(16 - 1/s)` on the open unit
diamond, `s = (t^2-|x|^2)((1-t)^2-|x|^2)`, zero outside;
`B_D(t) = Q b_D(t,·) Q` on the same sealed quadrature.

**Exponentials.** Own scaling-and-squaring Padé (Higham) at orders
3/5/7/9/13; no scipy. Per the repair amendment's apparatus note, every
step exponential in this lane is scaling-and-squaring, not eigh.
Self-test vs. eigh on a random 32×32 Hermitian: residual 2.20e-14.

**Apparatus validation against the sealed record.** Reproducing the sealed
`T07_hermite_galerkin_baseline.json` n=2, N_t=48 completed amplitudes:

| ell | state | |Z − Z_sealed| |
|---|---|---|
| 1 | mixed | 1.05e-14 |
| 1 | pure | 1.21e-13 |
| sqrt2 | mixed | 2.71e-14 |
| sqrt2 | pure | 9.67e-14 |

Per-history determinants agree to <= 1.8e-13. Clifford residual 0.0;
`h_0` Hermiticity residual 0.0.

## 2. The falsifier, implemented exactly as pinned by S2

`A_0[m][n] = +1 if n = m+1; -1 if m = n+1; 0 otherwise`, then normalized.
Raw spectral radius `2cos(pi/9) = 1.879385…`; after normalization
`||A_0||_2 = 1.000000` (residual 0), antisymmetry residual 0.

`J'(t) = -( B_D(t) + i·||B_D(t)||_2·A_0 ) (x) alpha_x`, amplitude pinned at
100% and **not** reduced anywhere in the certified reading. Amplitude-pin
residual `max_k | ||i·||B_k||·A_0||_2 − ||B_k||_2 | = 0` exactly.
`J'` is Hermitian (real-symmetric + i·real-antisymmetric = Hermitian),
so the propagator stays unitary.

Unbroken counterpart: the sealed `J(t) = -B_D(t) (x) alpha_x`, unchanged.

## 3. Two independent readings of Z'(0)

**(a) Certified central differences (the deciding measurement).**
`Z(a) = sum_lambda w_lambda det(1 − C + C·U_lambda(a))`, with `U_lambda(a)`
the full Strang product including `A = exp(-i a J'(t_k) dt/2)`.
`D(h) = [Z(h) − Z(−h)]/2h` on the ladder h ∈ {4e-2, 2e-2, 1e-2, 5e-3,
2.5e-3}; Richardson `R(h) = (4D(h) − D(2h))/3`; enclosure radius =
(spread of the Richardson ladder about the finest centre, plus |D−R|/3)
+ roundoff bound `64·eps·max|Z| / 2h_min`. Reported as
`[max(0, |centre|−radius), |centre|+radius]`.

**(b) Exact discrete linear response (the slot-resolved reading).**
Differentiating the Strang product at a = 0 gives an exact additive
decomposition over the 144 slots (lambda, k):

```
Z'(0) = sum_{lambda,k} T_{lambda,k},
T_{lambda,k} = tr[ Phi_{lambda,k} J(t_k) ],
Phi_{lambda,k} = -i (dt/2) w_lambda D_lambda(0)
                 [ M_k Gamma_{k,lambda} M_k^dag + F Gamma_{k,lambda} F^dag ],
Gamma_{k,lambda} = L_{k,lambda} G_lambda L_{k,lambda}^dag,
G_lambda = (1 − C + C u_lambda)^{-1} C u_lambda,   M_k = G_k F.
```

This is the discrete counterpart of the sealed Condition-1 identity
`Z'(0) = int tr[Phi(t) J(t)] dt` with
`Phi(t) = -i sum_lambda w_lambda D_lambda(0) u_lambda(t) G_lambda u_lambda(t)^dag`
(the two half-slot conjugations replace the single midpoint value). Phi is
built entirely from a = 0 data and contains no reference to J — so Z'(0) is
one linear functional with one slot, exactly as the sealed Condition-1
argument states, and it is **exactly linear in J** by construction.

Detector extraction, per Condition-1: `Psi[i,j] = tr_spinor(Phi_{ij} alpha_x)`,
so that `tr[Phi (B (x) alpha_x)] = tr[Psi B]`; `sym(Psi)` reads the L4 class,
`antisym(Psi)` reads the class-leaving part.

**Cross-validation of (a) against (b)** on a connection that actually reads
(stride-4 diagnostic, §6): agreement to relative 1.5e-7 – 2.2e-7 with
enclosure radii 7.3e-14 – 1.1e-12. Both routes are therefore certified.

## 4. MEASURED RESULTS

### 4.1 Non-vacuity gate (S4 precondition) — CLEARS in every case

| ell | max_k ||J'(t_k)||_2 | max_k ||J_sealed(t_k)||_2 | > 1e-6 |
|---|---|---|---|
| 1 | 7.3865e-04 | 5.7491e-04 | yes (2.9 decades) |
| sqrt2 | 2.6224e-04 | 2.0424e-04 | yes (2.4 decades) |

26 of 48 time slots carry `||B_D(t_k)||_2 > 1e-12` (k = 11 … 36), i.e.
78 of the 144 (lambda, k) slots.

### 4.2 BROKEN reading under the pinned class-leaving falsifier

Certified central-difference enclosures of |Z'(0)|, amplitude 100%:

| ell | env | state | |Z'(0)| enclosure | analytic slot sum |
|---|---|---|---|---|
| 1 | A | mixed | [0, 7.16e-15] | 2.14e-24 |
| 1 | A | pure | [0, 2.10e-13] | 1.68e-22 |
| sqrt2 | A | mixed | [0, 2.33e-14] | 6.01e-24 |
| sqrt2 | A | pure | [0, 1.11e-13] | 3.54e-23 |
| 1 | B | mixed | [0, 3.01e-14] | 1.35e-23 |
| 1 | B | pure | [0, 3.08e-13] | 1.04e-21 |
| sqrt2 | B | mixed | [0, 2.71e-14] | 3.67e-24 |
| sqrt2 | B | pure | [0, 8.36e-14] | 2.19e-22 |

**Window placement: the reading is BELOW the S3(a) window and BELOW the
S4 floor, in every case.** Worst certified upper bound 3.08e-13 versus the
1e-9 floor — 3.5 decades of margin, versus the predicted central 1e-6 and
the widened window [1e-8, 1e-4]. The analytic slot sums (1e-24 – 1e-21)
are themselves at the roundoff floor of the contraction, not a signal:
per-slot they track `2e-20 × ||B_k||_2`.

### 4.3 UNBROKEN counterpart (sealed J) — ceiling 1e-12 MET

`Z(+h)` and `Z(−h)` are **bit-identical** in all 8 configurations, so the
central difference is exactly 0.0. Enclosures are the pure roundoff bound:
[0, 2.84e-15] (best) to [0, 1.93e-13] (worst). Analytic slot sums 1.9e-26
– 1.0e-23 (again the contraction roundoff floor, `sym(Psi) ~ 1e-15` times
`||B_k|| ~ 1e-4` times dt). Ceiling 1e-12 met with >= 0.7 decade margin
on the enclosure and ~12 decades on the analytic value.

### 4.4 Detector diagnostics (Condition-1 reproduction)

`||sym(Psi)||_F` and `||antisym(Psi)||_F`, time-integrated per lambda,
envelope A:

| ell | state | lambda | ||sym||_F | ||antisym||_F |
|---|---|---|---|---|
| 1 | mixed | ±sqrt2 | 4.83e-16 | **6.702e-02** |
| 1 | mixed | 0 | 9.60e-16 | 1.357e-01 |
| 1 | pure | ±sqrt2 | 4.74e-15 | 8.064e-01 |
| 1 | pure | 0 | 9.71e-15 | 1.633e+00 |
| sqrt2 | mixed | ±sqrt2 | 3.16e-15 | 2.013e-01 |
| sqrt2 | mixed | 0 | 6.03e-15 | 4.033e-01 |
| sqrt2 | pure | ±sqrt2 | 1.10e-14 | 8.151e-01 |
| sqrt2 | pure | 0 | 2.10e-14 | 1.633e+00 |

`sym(Psi) = 0` pointwise in t and per lambda to <= 4.7e-14 (max over all
slots, all cases) — Lemma L4 as a detector property, reproduced
independently. The nearest match to Condition-1's quoted `6.809e-02` is
**6.702e-02** (ell = 1, C_mix, lambda = ±sqrt2, envelope A), 1.6% away,
consistent with that lane's disclosure that its numerics were
order-of-magnitude. Per-slot values are in the JSON
(`detector.<i>.sym_F_per_slot` / `antisym_F_per_slot`, 48 entries each).
The detector is loaded in **every** slot, including slots where `B_D` has
no support: `antisym_F_per_slot` is flat at 6.70e-02 (ell = 1, C_mix,
lambda = ±sqrt2) across all 48 slots.

**The detector is loaded and it is not small. The reading is still zero.**

## 5. WHY the pinned falsifier reads zero — an exact selection rule

This is the substantive finding of this lane, and it is a theorem, not a
numerical observation.

### Proposition (C4v3-P1)

On the sealed carrier, for every lambda, every t, both states, both
envelopes and both ell:

```
Psi[i,j] = 0   unless   a_i != a_j  AND  b_i = b_j  AND  c_i = c_j,
```

i.e. for n = 2 the detector is supported **exactly on the |i − j| = 4
stride** (the pairs (0,4), (1,5), (2,6), (3,7)) and nowhere else.

**Proof.** Let `T'_j = P_j (x) (i gamma^j)` be the sealed Lemma-2
involutions, `P_j` the Hermite parity `(-1)^{quantum number}` in axis j.
Machine-verified on this carrier: `[T'_j, h_0] = 0` exactly (residual 0.0
for all three j), `T'_j (M(t) (x) S) T'^{-1}_j = M(t) (x) S` (residual
<= 6.6e-18), `T'^2_j = I`. Phi is assembled entirely from a = 0 data
(h_0, M (x) S, C, w, D_lambda), so `T'_j Phi T'^{-1}_j = Phi` for each j.
Conjugation acts on the spatial index by `(-1)^{q_i - q_j}` and on the
spinor factor by `(i gamma^j)^{-1} alpha_x (i gamma^j)`, whose sign is
machine-verified as `(-1, +1, +1)` for j = (x, y, z). Hence
`Psi[i,j] = -(-1)^{a_i-a_j} Psi[i,j]` (x-axis) and
`Psi[i,j] = +(-1)^{b_i-b_j} Psi[i,j]`, `= +(-1)^{c_i-c_j} Psi[i,j]`
(y-, z-axes), forcing `a_i - a_j` odd and `b_i - b_j`, `c_i - c_j` even. ∎

**Numerical certification.** `max|Psi|` on the predicted support:
5.12e-02 to 5.77e-01. `max|Psi|` off the predicted support:
**1.11e-17 to 3.05e-16** — over all lambda, all 48 slots, all 8
configurations.

### Corollary — the pinned A_0 is trace-orthogonal to the detector

`A_0` is supported exclusively on the `|i − j| = 1` stride. Enumerating
those seven pairs in the sealed `(a,b,c)` order:

| pair | binary | a differs? | b,c same? | Psi |
|---|---|---|---|---|
| (0,1) | 000–001 | no | — | 0 |
| (1,2) | 001–010 | no | — | 0 |
| (2,3) | 010–011 | no | — | 0 |
| (3,4) | 011–100 | yes | **no** (b and c both differ) | 0 |
| (4,5) | 100–101 | no | — | 0 |
| (5,6) | 101–110 | no | — | 0 |
| (6,7) | 110–111 | no | — | 0 |

Every entry of `A_0` sits on a pair where Psi vanishes identically.
Therefore `tr[antisym(Psi) A_0] = 0` **exactly**, and hence
`Z'(0) = 0` for the pinned falsifier. Measured:
`max |tr[antisym(Psi) A_0]| = 2.05e-18 … 4.12e-16` over all slots and
configurations — floating-point zero — against
`max |tr[antisym(Psi) A_4]| = 3.81e-01 … 4.62e+00` for the stride-4
direction of §6.

The zero is a **support mismatch**, forced by the very Lemma-2 parity the
control set out to probe. It is not a dynamical cancellation, not a new
symmetry, and not a tau-grading effect.

## 6. Disclosed diagnostic — NOT the pinned falsifier

To separate "the channel is dead" from "the probe missed the channel", the
identical construction was run with the stride-4 analogue of `A_0`:

```
A_4[m][n] = +1 if n = m+4 ; -1 if m = n+4 ; 0 otherwise ; ||A_4||_2 = 1.
```

`A_4` is in the **same tau-EVEN class-leaving family**, at the **same 100%
amplitude pin**, differing only in which index stride it occupies. This is
a diagnostic disclosed as such: it is not the S2 falsifier, it was
constructed after seeing the null result, and no reading of it is offered
as the control's outcome.

| ell | env | state | |Z'(0)| (analytic) | FD enclosure |
|---|---|---|---|---|
| 1 | A | mixed | 3.7789e-07 | [3.778909e-07, 3.778910e-07] |
| 1 | A | pure | 4.5737e-06 | [4.573721e-06, 4.573724e-06] |
| sqrt2 | A | mixed | 5.1885e-08 | [5.188466e-08, 5.188516e-08] |
| sqrt2 | A | pure | 2.1308e-07 | [2.130820e-07, 2.130834e-07] |
| 1 | B | mixed | 3.9951e-06 | [3.995052e-06, 3.995052e-06] |
| 1 | B | pure | 4.7955e-05 | [4.795544e-05, 4.795544e-05] |
| sqrt2 | B | mixed | 5.7371e-07 | [5.737119e-07, 5.737126e-07] |
| sqrt2 | B | pure | 2.3442e-06 | [2.344180e-06, 2.344182e-06] |

Every one of these lies **inside the S3(a) window [1e-8, 1e-4]**, and the
envelope-A / C_mix / ell = 1 value 3.78e-07 sits within a factor 2.6 of the
frozen central prediction 1e-6. The 87x spread across configurations is
itself larger than the 11x envelope spread the spec cited when widening the
window — the widening was warranted.

So the S3(a) **magnitude** prediction is well calibrated for a class-leaving
direction that meets the detector. What failed is the S2 **choice of
direction**, not the S3 physics.

## 7. S3(c) STRUCTURAL PREDICTIONS — outcome by outcome

| # | Prediction | Outcome | Evidence |
|---|---|---|---|
| 1 | Per-slot vanishing for the in-class input (no ±lambda cancellation) | **CONFIRMED** | max_{lambda,k} \|T_{lambda,k}\| = 2.2e-24 … 2.0e-23, i.e. every one of the 144 slots is individually at the roundoff floor. Not a cancellation: the per-lambda sums are the same size as the per-slot values. |
| 2 | The class-leaving reading occupies the SAME (lambda, k) slots | **FAILED for the pinned A_0; CONFIRMED for A_4** | Pinned A_0 occupies **0** of 144 slots above 1e-12. A_4 occupies 72–78 of the 78 connection-supported slots, and `A_4-occupied \ detector-loaded = 0` in every case (the 0–6 shortfall is the tail slots where \|\|B_k\|\| itself falls under the print threshold). |
| 3 | Exact linearity in the class-leaving amplitude | **CONFIRMED (vacuous for A_0)** | On A_4, over c ∈ {0.1, 0.5, 2, 10}: max linearity residual **5.2e-15 … 2.6e-13**. Structural reason: Phi carries no J-dependence, so Z'(0) is exactly linear in the connection. For the pinned A_0 the identity is 0 = c·0 — satisfied, uninformative. |
| 4 | Lemma 1 (D_{+lambda} = D_{−lambda}) survives the falsifier | **CONFIRMED** | \|D_{+sqrt2}(a) − D_{−sqrt2}(a)\| at a = ±1e-2 under the pinned falsifier: max **9.49e-16** over all configurations (relative <= 1.3e-15). |
| 5 | A mixed connection gives the same Z'(0) as the pure class-leaving part | **CONFIRMED (vacuous for A_0)** | On A_4: relative difference **0.0 (bit-identical)** in 6 of 8 configurations, 5.5e-16 and 2.0e-15 in the other two. The in-class component contributes exactly nothing, reproducing the sealed Condition-1 claim. For A_0 both sides are at the roundoff floor. |

Additional structural observation (not predicted): the pointer sum
suppresses the class-leaving reading by a further factor ~40–80. Per-lambda
slot sums for A_4 (ell = 1, env A, C_mix) are 1.518e-05, 3.072e-05,
1.518e-05, while the completed |Z'(0)| is 3.779e-07 — the `w = (-1/4, 1/2,
-1/4)` second difference acting on `D_{+lambda} = D_{-lambda}` (Lemma 1 plus
`m0 = m1 = 0`). This is the same mechanism the sealed parity-lemmas result
attributes the ER-insensitivity cancellation to.

## 8. S4 — read carefully, the criterion and its stated mechanism diverge

S4 refutes teeth on the conjunction:

```
|Z'(0)| < 1e-9  AND  max_k ||J'(t_k)||_2 > 1e-6  AND  ||antisym(Psi)||_F ~ O(1e-2)
```

**All three clauses are met, in all 8 configurations.** Certified:
|Z'(0)| <= 3.08e-13; max_k ||J'|| >= 2.62e-04; ||antisym(Psi)||_F
∈ [5.92e-02, 1.63e+00] (time-integrated per lambda; per-slot maxima
∈ [5.96e-02, 1.63e+00]).

But S4 states its *reason*: "that combination would mean the alpha_x
channel is annihilated in BOTH tau gradings — a FIFTH protection."
**That reason is false here, and demonstrably so.** The tau-EVEN channel
is fully live: a class-leaving direction of the same class and the same
pinned amplitude, differing only in index stride, reads 5.19e-08 to
4.80e-05 — inside the S3(a) window. There is no fifth protection. There is
an exact parity selection rule (§5) that confines the detector to the
stride-4 sector, and a pinned probe that lives entirely in the stride-1
sector.

The consequence for the S6 disposition is a matter for the principal and
the construction lane, not this lane. What this lane certifies is the
disjunction the record must carry:

- Under the **letter** of S4, the pinned falsifier does not bite, and the
  outcome is the S6 "does not bite" arm: a fourth defeated falsifier.
- Under the **substance** of S1 — whether the Z'(0) reading path on the
  completed-record object is LIVE — the answer measured here is **yes**,
  and it is live at the predicted magnitude. The teeth proposition is
  supported by the A_4 diagnostic, but that diagnostic was chosen after
  seeing the null, so it carries the exact foreknowledge defect the
  authorization's Condition 2 was written to prevent. It cannot be
  promoted to the control's result without a fresh commitment-first cycle.

Both statements are measurements from this lane. Neither may be cited
without the other.

## 9. Floors and thresholds — outcome table

| Floor / threshold | Source | Result |
|---|---|---|
| broken \|Z'(0)\| >= 1e-9 | S4 / repaired control floors | **NOT MET** (<= 3.08e-13 certified) |
| broken \|Z'(0)\| in [1e-8, 1e-4] | S3(a) window | **NOT MET** |
| unbroken \|Z'(0)\| <= 1e-12 | S3(b) ceiling | **MET** (bit-identical Z(±h); enclosure <= 1.93e-13) |
| max_k \|\|J'(t_k)\|\|_2 > 1e-6 | S4 non-vacuity | **MET** (>= 2.62e-04) |
| \|\|antisym(Psi)\|\|_F ~ O(1e-2) | S4 detector-loaded | **MET** (5.92e-02 … 1.63) |
| \|\|sym(Psi)\|\|_F = 0 pointwise | L4 detector property | **MET** (<= 4.7e-14) |
| amplitude pinned at 100% | S2 mandatory | **HELD** (residual 0; never reduced in any certified reading) |

## 10. Fences honoured

Sealed and production files: read only, never modified. All output confined
to this scratch directory. No blind-lane path read. No production lane
invoked. No measured constant used or produced. Pinned runtime
`/Users/bgm/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`
(numpy 2.3.5, Python 3.12.13; scipy absent — expm is own-written). The
amplitude pin was never reduced for any reading offered as the control's
result; the amplitude ladder in §7 row 3 is a structural linearity
diagnostic, run at the pin and above and below it, and is labelled as such.

## 11. Files

- `T07_control4_v3_primary_v001.json` — full result, 144-slot tables,
  per-slot detector norms, all enclosures, verdict roll-up.
- `apparatus.py` — carrier, states, expm, propagation.
- `run_control4_v3.py` — measurement driver.
- `validate.py` — apparatus validation against the sealed baseline record.
