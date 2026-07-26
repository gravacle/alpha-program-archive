# Route Memo — IR / Sea-Kernel Attack on E1 (theory lane return)
Claude lane · 2026-07-26 · fresh-context attack lane, read-only. Recorded
verbatim below. Construction-lane spot-verification of the load-bearing
algebra was performed before sealing (moments, second-difference identity,
tau_R phase saturation, zeta constants, kernel modulus) — all confirmed.

HEADLINE: the block called "T7's true bottom" is NOT an infrared clustering
problem. The connected two-cell cumulant is a TWO-LINE object decaying as
R^-6; the anchored n >= 2 sums converge with spare powers. The pointer-weight
cancellation hoped for is real (m0 = m1 = 0, an exact second difference) but
is EXACTLY SATURATED by the full-tau_R e^{+-i pi} record phases, leaving the
SHARP causal-ball localizer paired against the marginal |x|^-3 massless sea
— a coincidence-limit, definition-level obstruction confined to n = 1.
Phase-1's K_sea is DIVERGENT rather than uncertified. And E1, not O7, is the
true bottom.

---

## ROUTE MEMO — IR / SEA-KERNEL ATTACK LANE

**Target:** `E1_SEA_KERNEL_ACTION_DENSITY_UNCERTIFIED`, live blocker of O4‑M2 in `STAGE8_T7_CONNECTED_LINKED_CLUSTER_MAJORANT_DERIVATION_SPEC_V001.md`.
**Status of this text:** route memo, not a spec, not a result. Read-only lane. No measured constant appears anywhere below; every number is derived (π, √2, ζ‑values, exact rationals from the sealed record data).

**Seals verified this session** (computed vs `.seal.sha256`, all match):

| file | sha256 |
|---|---|
| `STAGE8_T7_CONNECTED_LINKED_CLUSTER_MAJORANT_DERIVATION_SPEC_V001.md` | `818083a5…f84e3` |
| `STAGE8_T7_D6_SPECS_REPAIR_AMENDMENT_V001.md` | `60223e6a…09e5d` |
| `stage8_execution/work/MAJORANT_LEMMA0_PROOF_DRAFT_V001.md` | `679ba036…7b9c` |
| `stage8_execution/work/MAJORANT_PHASE2_O3_O7_PROOF_DRAFT_V001.md` | `08b91543…7e0e3` |

Also read: `STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_RESULT_V001.md`, `STAGE8_T7_L2_INTENSIVE_HESSIAN_TYPING_FREEZE_V001.md`, `STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md` (A1/A2/A3), `STAGE8_T7_CONNECTED_ANALYTIC_CLOSURE_RESULT_V001.md`, `R3_4_CAUSAL_DIAMOND_SPECTRAL_PULLBACK_RESULT_V002.md`, `STAGE8_T7_MAJORANT_PHASE2_STATUS_AND_O7_ESCALATION_V001.md`, `T07_majorant_phase2_primary_v001.json`, and `/Users/bgm/MB Work/alpha_supervision/ROUTE_MEMO_2026-07-25_linked_cluster_majorant.md`.

---

# 1. THE OBSTRUCTION, STATED SHARPLY

## 1.1 The exact inequality

For each admitted state (M‑3: the two Phase‑A pinned finite schemes `C_mix = Q P_- Q`, `C_pure = 1_(-inf,0)(Q h_0 Q)`; per‑state, never promoted), each relayed causal exhaustion `K` (D2), each cellulation `X` in the D3 quantifier, each cell `C ∈ X`, each `n ≥ 1`, and each CTP pair history with `max(|a_{c,+}|,|a_{c,-}|) ≤ ε_*` (M‑2):

```
  SUM_{gamma ∋ C, |gamma| = n, gamma connected}  |Phi_gamma(a_+,a_-)|   ≤   |C|_4 · eta^n ,
  eta = eta(eps_*) ≤ 1/2   certified,   eta a functional of (||b_D||, tau_R, sea-kernel decay data, |w_lambda|) ONLY.
```

with, unfolding the sealed definitions all the way down,

```
Phi_gamma = - SUM_{∅≠g'⊆gamma} (-1)^{|gamma|-|g'|} Log [ Z_comp^{(g')}(a) / Z_comp^{(g')}(0) ]     (O2, Möbius)

Z_comp^{(g')}(a) = SUM_{(mu_c),(lambda_c)} PROD_c w*_{mu_c} w_{lambda_c}
                     det_{ran C}( C · U_mu^{(g')}(a_-)^dag U_lambda^{(g')}(a_+) · C )              (Lemma 0(b) + M1)

u_lambda^{(c)}(a) = T exp{ -i ∫_cell [ h_0 + lambda v(t) M(t) ⊗ S + a J(t) ] dt }                  (A2)
h_0 = SUM_j p_j ⊗ alpha_j ;  M(t) = Q 1_{|x| ≤ r(t)} Q ;  r(t) = min(t,1-t) ;  v(t) = tau_R·32 r(t)^3
S = -i n̸ gamma^5  (S² = I) ;  J(t) = -(Q b_D(t,·) Q) ⊗ alpha_x ;  b_D = exp(16 - 1/s)
tau_R = pi/sqrt2 ;  w = (1/2, -1/4, -1/4) on colors lambda = (0, +sqrt2, -sqrt2)
```

Phase 1 reduced this to the explicit monotone functional

```
eta(eps) = (2 eps ||b_D||_inf K_sea / b_0) · exp( 1 + T_R + 2 eps ||b_D||_inf K_sea )
K_sea := sup_{admitted cells C} |C|_4^{-1} ∫_0^1 max_mu || C_state · u_mu^{(c)}(1←t;0) · Q 1_{D_t} Q ||_1 dt
```

and blocked on `(K_sea, T_R, b_0)`.

## 1.2 The sea-kernel object, in closed form — and a correction to the Phase‑1 grounds

`STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_RESULT_V001.md` pins the covariance **exactly**, not by class:

```
C = 1_{(-inf,0)}(h_0),   C(p) = (I - h_0(p)/|p|)/2 = (I - alpha·p̂)/2,   C_n = Q_n C Q_n.
```

Because `h_0` is the massless Dirac operator (A1), the position kernel is closed-form. Using the exact 3‑D transform `FT[|p|^{-1}](x) = 1/(2π²|x|²)` and `p_j/|p| = -i∂_j ∘ |p|^{-1}`:

```
C(x-y) = (1/2) delta^3(x-y) I  -  i alpha·(x-y) / (2 pi^2 |x-y|^4).
```

The off-diagonal ("sea") half therefore has modulus **exactly** `1/(2π²|x−y|³)`, is homogeneous of degree −3, and is **odd** (zero mean on spheres — a Calderón–Zygmund kernel).

> **Correction of record.** Phase‑1 ground 1 (`MAJORANT_LEMMA0_PROOF_DRAFT_V001.md` §3.3) says "the sealed corpus pins only the decay CLASS of the sea kernel." That is too pessimistic. The covariance is pinned *exactly* by a sealed result; the kernel is computable in closed form; nothing is missing as *data*. What is missing is a *theorem* about a fully known object. This reclassifies E1 from "input absent" to "lemma unproven" — which matters for route selection and for the graceful-block wording.

## 1.3 Why degree −3 is marginal — quantitatively

```
∫_{a<|r|<R} |C_off(r)| d^3 r = ∫_a^R (4 pi r^2) dr / (2 pi^2 r^3) = (2/pi) log(R/a).
```

Degree −3 in 3 dimensions is scale-free: the kernel has *no* scale, so its absolute integral is logarithmic at **both** ends, with derived coefficient `2/π`. That is the whole content of "marginal." The label "infrared" in the spec's O4 note is inherited from masslessness (no gap ⇒ no exponential cutoff ⇒ pure power ⇒ log at both ends), **not** from a large-distance divergence in the cluster sum. Phase‑1's own ground 2 already located the divergence "at coincidence," i.e. at the UV end. This distinction is load-bearing and I take it up in §1.5.

## 1.4 Classification (a) / (b) / (c) — the block is three different objects

E1's single named witness conflates three distinct sub-objects with three distinct verdicts.

**(a) GENUINE DIVERGENCE — `K_sea` as literally defined by Phase 1.**
`|| C_state · u · Q 1_{D_t} Q ||_1` is a trace norm of (sea projector) × (sharp diamond-slice localizer). The `δ/2` half of `C` contributes the *mode count* of the sea inside `D_t`. Carrier-blind (i.e. as `n → ∞` on the Hermite carrier, or in the continuum) this is a **power divergence**, `~ |D_t| Λ³`, not a log. So `K_sea = +∞` under the very carrier-blindness the spec-header demands, and it is finite only on a fixed carrier — where it is forbidden. **The Phase‑1 functional cannot be "certified"; it must be replaced.** This is a bound-architecture failure, and it is good news: it is the removable part.

**(b) MARGINAL / LOGARITHMIC — the residue after the removable part is removed.**
The divergent part of (a) is manifestly `a`‑independent and cell-local; it cancels in the ratio `Ẑ = Z(a)/Z(0)` (D1's T7(i) anchor) and again in the Möbius truncation for `|γ| ≥ 2`. Moreover the leading subtracted term is killed *twice over*:
- spinor/parity: `tr_spinor[ C(p) alpha_x ] = -2 p̂_x`, odd in `p̂`, so `∫ d³p (…) = 0` — the naive `a`‑linear vacuum tadpole integrates to zero;
- pointer weights: the same term carries `Σ_{mu,lambda} w*_mu w_lambda = |m0|² = 0` (see §1.6).

What survives is the *logarithmic* residue of the degree‑(−3) kernel against the in-cell localizers. That is the genuine marginal object, and it is undecided by any sealed authority.

**(c) MERELY-UNPROVEN-BUT-TRUE — the long-distance cluster sums, `n ≥ 2`.**
See §1.5. These converge with two powers of margin. Nothing marginal happens there at all.

## 1.5 The two-cell connected activity: counting BOTH lines

This is the quantitative point the record has never made, and it changes the diagnosis.

The state evaluation is a determinant (M1). Write `A = C(V−1)C` on `ran C` and `V − 1 = X_1 + X_2` with `X_i` supported in cell `i`'s diamond (`J` and `v M ⊗ S` are diamond-supported by A2/A1). Then

```
Log det(1 + A) = tr A - (1/2) tr(A A) + ... ;   tr A = tr[C X_1 C] + tr[C X_2 C]   (DISCONNECTED)
```

The first-order term contains **no cross term**. The lowest connected two-cell object is therefore forced by determinant structure to be

```
Phi_{12} ⊃ - tr[ C X_1 C X_2 ]
         = - ∫_{D_1}∫_{D_2}∫_{D_2}∫_{D_1} C(y_1,x_2) X_2(x_2,y_2) C(y_2,x_1) X_1(x_1,y_1),
```

i.e. **two** sea propagators bridging the separation, one out and one back. This is not an assumption; it is the fermion-loop structure of a quasi-free determinant, available from Lemma 0(b) + M1 with no new hypothesis.

**Hence the pair activity carries `R^{-6}`, not `R^{-3}`.** With Chebyshev shell counts on a cubic cellulation, exact:

| counting | shell | one line (`k^-3`) | two lines (`k^-6`) |
|---|---|---|---|
| 3 spatial dims | `24k²+2` | `24 H_K + 2ζ(3)` → **diverges** (`24 ln K`) | `24ζ(4)+2ζ(6) = 4π⁴/15 + 2π⁶/945 = 28.0105…` **converges** |
| 4 spacetime dims | `64k³+16k` | `64K + …` → **diverges linearly** | `64ζ(3)+16ζ(5) = 93.5225…` **converges** |

(Verified by exact-rational partial sums: 3‑D two-line `S(100)=S(10⁴)=28.0104…`; 4‑D two-line `S(100)=93.5193`, `S(10⁴)=93.5225`.)

Two observations follow.

1. **NC3 is a one-line control and its divergence is an artifact of one-line counting.** `NC3_T3_ONLY_ANCHORED_PAIR_SUM_DIVERGES` reproduces exactly `24 H_K` — the top-left cell of that table. NC3 is doing precisely its job (an activity bound built *only* from the one-root temporal-return data must fail), and the Phase‑2 draft is right to call it a PASS. But the draft then writes that NC3 "CORROBORATES the E1 named block from below." **It does not.** It corroborates that a *one-line* bound fails; the actual lowest connected cumulant is two-line. The long-distance direction has 2 spare powers in 3‑D and 3 spare powers in 4‑D.

2. **The refinement quantifier does not fight D5 here.** Redoing the anchored sum with cell scale `L`: shell count `R³dR/L⁴`, pair activity `s²·L⁴·L⁴/R⁶`, and the in-cell strength `s ≤ ε ||b_D||_inf ×(cell time extent) ~ εL` from the sealed Duhamel bound. Then

```
SUM_{C_2} |Phi_{C C_2}|  ~  eps^2 L^2 ∫_L^inf (R^3/L^4)(L^8/R^6) dR / L^... = eps^2 L^4 / 2   =  |C|_4 · (eps^2/2),
```

i.e. exactly action-density form with an **L‑independent** `η² = ε²/2`. D5 plus R1–R4 (already discharged, Phase‑1 §2.3) genuinely absorbs refinement. **The shrinking cell volume is not what defeats the constant.**

**Conclusion of §1.5:** the obstruction is *not* the long-distance/clustering direction. It lives entirely at `n = 1` — the single-cell relative determinant `Φ_C = −Log Ẑ_comp^{(C)}(a)` — where the coincidence limit of the marginal kernel meets the in-cell localizers.

## 1.6 Does `m0 = 0` improve the decay? — the honest answer: NO, and the reason is sharp

You asked me to check this hardest. I did, in exact arithmetic (`Q(√2)`, stdlib Fractions; scratch `ir_seakernel/moments.py`).

**Step 1 — the weight structure is better than you supposed: TWO moments vanish, not one.**

```
m_k := SUM_lambda w_lambda lambda^k   with w = (1/2,-1/4,-1/4), lambda = (0,+sqrt2,-sqrt2):
m_0 = 0   m_1 = 0   m_2 = -1   m_3 = 0   m_4 = -2   m_5 = 0   m_6 = -4   m_7 = 0   m_8 = -8
(exactly: m_{2j} = -2^{j-1} for j ≥ 1; all odd moments vanish by the ±sqrt2 spectral symmetry with equal weights.)
```

Equivalently, the exact identity (verified): `Σ_λ w_λ f(λ) = −(1/4)[ f(√2) − 2f(0) + f(−√2) ]`. **The completed per-cell Kraus operator is exactly a symmetric second difference in the record color:**

```
K_pointer^{(c)}(a) = -(1/4) [ Gamma(u_{+sqrt2}) - 2 Gamma(u_0) + Gamma(u_{-sqrt2}) ].
```

**Step 2 — the CTP double moments.** `Σ_{μ,λ} w*_μ w_λ λ^j μ^k = m_j m_k`, nonzero **iff j and k are both even and ≥ 2**:

```
j\k   0  1  2  3  4
 0    0  0  0  0  0
 1    0  0  0  0  0
 2    0  0  1  0  2
 3    0  0  0  0  0
 4    0  0  2  0  4
```

So every Dyson term with fewer than two record insertions **on each CTP branch** is annihilated. In particular the bare (record-blind) `a`‑linear tadpole vanishes identically on the completed chain — a real and previously unrecorded structural fact.

**Step 3 — where the hope dies.** The color index `λ` is an *in-cell* index. By Lemma 0(b) the color sums factorize *per cell*, so in `−tr[C X̄_1 C X̄_2]` the annihilation acts only on `X̄_i`, the color-averaged **in-cell vertex**. The two `C`'s bridging the separation are color-blind. A weight vector summing to zero kills the leading long-distance term of a two-point sum only when the weighted objects share a common `λ`‑independent long-distance tail *and the weights sit on the tail*. Here they sit on the vertex. **The power of separation is untouched.**

**Step 4 — worse: at full `tau_R` the cancellation is EXACTLY SATURATED.** From A1/A2, `S² = I` (with `S = −i n̸ γ⁵`, `n̸² = 1`, `{γ⁵,γ^μ}=0`), and `∫₀¹ v(t)dt = τ_R = π/√2` exactly. So `λ τ_R ∈ {0, +π, −π}` (the Phase‑2 route‑(b) exact witness) and, on the ball where `M(t)=1`,

```
exp(-i lambda tau_R S) = cos(lambda tau_R) I - i sin(lambda tau_R) S = (+1, -1, -1) · I   EXACTLY (scalar).
```

Therefore

```
SUM_lambda w_lambda · phase_lambda = 1/2 + 1/4 + 1/4 = 1   EXACTLY
                                   = SUM_lambda |w_lambda|   (the l1 mass Phase 1 already used).
```

The second difference applied to the vector `(+1,−1,−1)` returns `−(1/4)(−1−2−1) = 1`. **The `m0 = 0` annihilation buys exactly nothing at full `τ_R`: the full record cycle's `e^{±iπ} = −1` phases are precisely the alternating signs that saturate it.** Phase 1's triangle-inequality step (`Σ|w*_μ w_λ| = 1`) is therefore *tight*, not lossy. There is no slack to recover.

**Step 5 — and it is actively harmful.** Reading the same collapse at the operator level with `P := M(t)` the sharp causal-ball projector, `u_λ ≈ (I − P) + phase_λ · P`:

```
SUM_lambda w_lambda u_lambda  =  m_0 (I-P) + 1·P  =  P      ← the SHARP ball projector
SUM_lambda p_lambda u_lambda  =  1 (I-P) + 0·P    =  I - P   (exhaustive companion, for contrast)
```

So the pointer-weight structure, at full `τ_R`, promotes the **sharp spatial indicator** `1_{|x| ≤ r(t)}` to the leading in-cell object. A sharp indicator is the single worst partner for a degree‑(−3) Calderón–Zygmund kernel: it is exactly the configuration in which the sea/localizer pairing is divergent rather than merely log‑marginal. (Concretely, for the massless Dirac projector in 3 spatial dimensions `[C, 1_B]` is not Hilbert–Schmidt: `‖[C,1_B]‖₂² ~ ∫∫_{B×B^c} |C_off|² ~ |∂B| ∫ du/u²`, power-divergent; even a Lipschitz cutoff gives `∫ d³r · r²/r⁶ = ∫dr/r²`, also divergent. Equal-time localization of the 3‑D Dirac sea fails the Shale–Stinespring condition; only *two-time* / scattering-type objects, where the cell time integration supplies the missing decay, have a chance.)

**Verdict on the `m0 = 0` question:** it does not help the decay; it is saturated by the full-record π‑phase; and the object it leaves behind is the sharp record localizer, which is the *cause* of the coincidence divergence. What it *does* buy is real but different: two annihilated moments, ≥2 record insertions per branch, and a vanishing bare tadpole. Those are strength/structure gains, not decay gains — and any strength gain in the numerator is at risk from `b_0 = |Z_comp^{(C)}(0)|` in the **denominator** of `η(ε)`: the completed baseline is itself a second difference of `O(1)` objects, with no sealed lower bound (it is H‑B, named and undischarged, per L2 fence 3).

---

# 2. CANDIDATE ROUTES TO CERTIFICATION

All three replace, rather than certify, the Phase‑1 `K_sea`. **None requires any clustering axiom; F‑1 is not approached by any of them.** Two require a spec *amendment*; one may require a *definition-level* escalation. Adoption flags are marked ⚑.

## Route IR‑A — SPLIT THE D5 THRESHOLD: certify `n ≥ 2` outright, localize the block to `n = 1`

**Idea.** §1.5 shows the `n ≥ 2` anchored sums are governed by two-line kernels evaluated at *separation*, where the marginal kernel is smooth and the coincidence limit never occurs. Bound them by Hilbert–Schmidt pairing, `|tr[C X_1 C X_2]| ≤ ‖C X_1‖₂ ‖X_2 C‖₂` restricted to the cross-cell block, which needs no trace-class data and no coincidence enclosure.

**Load-bearing lemmas.**
- A‑L1: cross-cell HS bound `‖1_{D_1} C 1_{D_2}‖₂² ≤ |D_1||D_2| / (4π⁴ R⁶)` with `R = dist(D_1,D_2)` — a direct integral of the closed-form kernel of §1.2, exactly certifiable in outward-enclosed rational arithmetic.
- A‑L2: light-cone control. §1.5's shell counting assumes a spacelike-type decay uniform in direction; cells at null separation get no help from the equal-time bound. Needs a certified statement that the diamond profile `b_D` (Gevrey, vanishing to all orders at the tips) plus the cell time integration restores decay along the light cone. **This is the substantive new lemma.**
- A‑L3: geometric-series closure of the KP criterion with two thresholds `(η_1, η_{≥2})`.

**Sealed authorities citable.** `STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_RESULT_V001` (exact `C`); Phase‑A A1/A2 (`b_D`, `M`, `v`, `J`, `S`); `MAJORANT_LEMMA0_PROOF_DRAFT_V001` O1/O2 (composition, color independence, R1–R4); M1's two mandatory compliance citations (gate item 9 `4e1282bc…`, A4 relocation `8a7f52ff…`) carry over verbatim, with the M‑11 disclaimer.

**New obligations created.** (i) A **spec amendment** splitting D5's single `η` into `(η_1, η_{≥2})` — D5 as sealed demands one `η` for all `n`, and Kotecky–Preiss still needs `η_1` bounded, so the split does not evade `n=1`; it *isolates* it. (ii) A‑L2 (light-cone/null-separation decay). (iii) A restated E1 grid rule over two constants.

**Likely failure mode.** A‑L2. If null-separated cell chains admit no certified decay, the shell counting collapses and the `n ≥ 2` sums are not certifiable either — which would move the whole obligation back into category (a).

**Adoption?** No. Amendment only (append-only successor spec). ⚑ nothing.

## Route IR‑B — SUBTRACTED / REGULARIZED-DETERMINANT ARCHITECTURE (discharge `n = 1`)

**Idea.** Never norm the unsubtracted operator. Use the exact block-triangular identity `1 + C(V−1) = [[CVC, CV(1−C)],[0, I]]`, so `det(1 + C(V−1)) = det_{ran C}(CVC)`, then split by Carleman: `det(1+A) = det_2(1+A) e^{tr A}` with `|det_2(1+A)| ≤ exp(‖A‖₂²/2)`. The `a`‑ and Möbius-differences act *before* the norms:

```
Log Ẑ_comp^{(C)}(a) = [ tr A(a) - tr A(0) ]  +  [ Log det_2(1+A(a)) - Log det_2(1+A(0)) ].
```

**Load-bearing lemmas.**
- B‑L1 (trace part): `tr[C(V(a)−V(0))C]` finite, using `tr_spinor[C(p) α_x] = −2p̂_x` (odd ⇒ leading sea-depth divergence integrates to zero) **and** `|m0|² = 0` (bare tadpole annihilated). Both cancellations are exact and derivable from sealed data.
- B‑L2 (HS part): a **carrier-uniform** bound on `‖C(V(a)−V(0))(1−C)‖₂` — the cell-level Shale–Stinespring condition. For the smooth `a`‑vertex `J = −(Q b_D Q) ⊗ α_x` this is very plausible: `b_D = exp(16 − 1/s)` is Gevrey with all derivatives vanishing at the diamond boundary and tips, so its spacetime transform decays faster than any power, and the sea-depth integral converges absolutely. **For the record vertex it is the wall:** `M(t) = Q 1_{|x|≤r(t)} Q` is a *sharp* indicator, and §1.6 Step 5 shows the pointer weights put it in the lead.
- B‑L3: Möbius/connected truncation removes the remaining cell-local residue for `|γ| ≥ 2` (already available from O2).

**Sealed authorities citable.** Same set as IR‑A, plus `BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001` for the CTP propagator typing.

**New obligations.** A carrier-uniform off-diagonal HS bound for the cell evolution — stated as a *two-time* (cell‑S‑matrix) object, not an equal-time one, since the equal-time version is false (§1.6 Step 5).

**Likely failure mode.** B‑L2 fails on the record vertex, and the only repair is to soften `M(t)` — which is a **sealed Phase‑A A1 definition**. That is not a lane's to change. ⚑ **Flag: a "smooth the record localizer" repair is a definition-level change to a sealed spec and must go to the principal.** It is *not* a clustering adoption and F‑1 is not triggered, but it is Axis‑3-adjacent: it changes what the record cell *is*.

## Route IR‑C — EXACT RECORD-CYCLE COLLAPSE (decide the question either way)

**Idea.** Stop expanding in the record coupling. At full `τ_R` the record color acts, up to `[h_0, M⊗S]`, as the exact scalar `(+1,−1,−1)` on the ball (§1.6 Step 4). Then `K_pointer^{(c)}(a) = P_ball · Γ(free) · (a‑dressing)` exactly, and `Z_comp^{(C)}` becomes the determinant of a **sharp gauge kink** on the Dirac sea — an object with a known, *computable* logarithmic structure. The lane then computes the coefficient of that log rather than trying to bound it away.

**Load-bearing lemmas.**
- C‑L1: exact record-phase collapse at `λτ_R = ±π` (already an exact Phase‑2 witness; extend from phase to operator).
- C‑L2: commutator error `[h_0, M(t)⊗S]` — must be controlled in a *quadratic-form* / Besov-type norm, since `‖[h_0, 1_B]‖ = ∞` for a first-order `h_0` against a sharp indicator.
- C‑L3: exact evaluation of the sharp-kink log coefficient as a functional of the frozen tuple.

**New obligations.** C‑L2 is the whole content.

**Likely failure mode.** C‑L2 defeats norm-based control. **But this route is the only one that returns information under failure:** if C‑L3 certifies a *nonzero* log coefficient, E1 is upgraded from "uncertified" to **certified divergent at the sealed definition of `M(t)`** — a refutation of the current activity architecture with an exact witness, which is a far more valuable artifact than another block. Given the calibration note (this lane family runs optimistic), I rank IR‑C first for expected information yield and IR‑A first for expected certification yield.

**Adoption?** None. ⚑ nothing — but note that a certified-divergent outcome forces the same definition-level escalation as IR‑B's failure mode.

## Routes explicitly NOT taken

- Any clustering axiom, `BUFFERED_EXHAUSTION_CLUSTERING`, or clustering principle. **REFUSED by standing decision (F‑1, principal's flag (a)).** No route above reaches for one, and none needs one: the long-distance direction has margin (§1.5) — clustering was never the missing ingredient.
- Any finite-carrier numerical enclosure of `(K_sea, T_R, b_0)`: carrier-indexed, forbidden by spec-header scoping 1 and F‑4, and in any case divergent in the carrier-blind limit (§1.4(a)).

---

# 3. THE REFINEMENT INTERACTION — is E1 entangled with the O7 refutation?

`O7_OBSTRUCTION_NONPERTURBATIVE_REFINEMENT_NO_SMALL_PARAMETER` (Phase‑2 §7, escalated in `STAGE8_T7_MAJORANT_PHASE2_STATUS_AND_O7_ESCALATION_V001.md`) is real and its witnesses are exact.

**They are entangled at the root, but E1 is the deeper one, and certifying E1 helps more than the record currently supposes.**

**(i) Shared root.** O7 route (b) fails because "every refined cell inserts an O(1) full record cycle, exact phase `e^{±iπ} = −1`, no small parameter." §1.6 Step 4 shows that the *same* π‑phase is what saturates the `m0 = 0` cancellation. One structural fact — *full `τ_R` per cell at every refinement depth* — kills both the perturbative refinement path and the weight-cancellation path. That is a genuine entanglement and it should be recorded as such.

**(ii) But logically E1 is independent of O7, and O7's refutation SHRINKS E1's obligation.** E1's core divergence (§1.4(a)/(b)) is a fixed-scale, continuum/carrier-blindness question about the coincidence limit. It neither needs nor is helped by a refinement intertwiner. Conversely, if the quantifier were ever pinned to the skeleton, E1's hardest clause — `sup` over admitted cells at *all* scales — would collapse to a single scale. O7's refutation therefore reduces E1's burden; it does not add to it.

**(iii) The important finding: O7 may not be load-bearing for clause (2) at all.** The spec frames O4 as "transport the *skeleton* majorant" (Route H = T then Q), and the verdict table makes `T7III_MAJORANT_DERIVED` require O7. But the executed M3 schema (Phase‑2 §3.3) does **not** consume any Route‑T output: its uniformity over the full D3 quantifier comes from *R1–R4 re-aggregation plus cellulation-blind constants*, i.e. from E1/O2 alone. If M2's constants are genuinely scale-uniform, Route Q carries the entire quantifier by itself and the refinement intertwiner is unnecessary for clause (2). Put differently:

> **E1 and O7 are two encodings of one requirement — refinement uniformity.** O7 is the Route‑T encoding (transport a numeric spectral-gap certificate) and it is refuted. E1 is the Route‑Q encoding (a scale-uniform sea constant) and it is merely uncertified. Refuting the first does not refute the second.

**(iv) Which is the true bottom?** **E1.** O7 refutes a *mechanism*; E1 gates a *quantity* that, if certified, would deliver clause (2) over the full D3 quantifier without O7. Nothing downstream (M3, O5, O6, `Γ_star`, the I3 tuple, the Duhamel consumer) waits on O7; everything waits on `(K_sea, T_R, b_0)`.

**(v) Would certifying E1 help while O7 stands refuted? Yes — substantially, and possibly more than "scope-restricted."**
- Minimum: it flips the arm from `T7III_BLOCKED` (no named result) to `T7III_SCOPE_RESTRICTED_ESCALATE` (a skeleton theorem plus a scope decision for Brian) — provided O3's Route‑T certificates also land, which they cannot until the Phase‑A production bundle seals (`TT2_E*_BLOCKED_BY_ORDERING_PHASE_A_BUNDLE_ABSENT`).
- Maximum: if (iii) holds, certifying E1 delivers clause (2) over the **full** quantifier via Route Q alone, and the O7 refutation becomes a recorded but non-blocking fact about Route T.

⚑ **This is a question for the principal, not a lane call:** *does the `T7III_MAJORANT_DERIVED` arm genuinely require O7, given that the executed M3 schema derives the D3 uniformity from R1–R4 + cellulation-blind constants without consuming any Route‑T output?* Answering "no" would change which named witness is the program's true bottom, and would retire an escalation currently sitting on Brian's desk. It must not be answered by amending a spec.

---

# 4. GRACEFUL-BLOCK DESIGN

A successor spec should carry these named witnesses, one per route, ranked so that failure still returns information.

| route fails | named witness a spec should carry | honest partial result that survives |
|---|---|---|
| IR‑A (light-cone lemma A‑L2) | `E1_NULL_SEPARATION_CLUSTER_DECAY_UNCERTIFIED` | Spacelike-separated anchored `n ≥ 2` sums certified with exact constants `24ζ(4)+2ζ(6)` (3‑D) / `64ζ(3)+16ζ(5)` (4‑D); the obligation narrows to null-separated cell chains. |
| IR‑A (split rejected) | `D5_SINGLE_ETA_OVERBINDS_SPLIT_AMENDMENT_REQUIRED` | The entire block localizes to `n = 1`; `n ≥ 2` certified. |
| IR‑B (record vertex) | `E1_SEA_OFFDIAGONAL_HS_SHARP_RECORD_LOCALIZER` | The **`a`‑vertex sector** (smooth Gevrey `b_D`) is certified carrier-uniformly; the block is confined to the sharp `M(t)` of A1 — a *definition-level*, not a clustering-level, obstruction. |
| IR‑B (trace part) | `E1_SUBLEADING_SEA_TRACE_LOG_UNCERTIFIED` | The leading sea-depth divergence certified to cancel exactly (odd spinor trace `−2p̂_x`; `|m0|²=0`); only the subleading log remains. |
| IR‑C (commutator) | `E1_RECORD_KINK_COMMUTATOR_FORM_UNCERTIFIED` | Exact record-phase collapse certified; error term isolated in one named commutator. |
| IR‑C (coefficient nonzero) | `E1_RECORD_KINK_LOG_COEFFICIENT_NONZERO_CERTIFIED` | **A refutation, not a block:** E1 is unsatisfiable at the sealed `M(t)`. Escalates to the principal as a definition decision (sharp vs. smoothed record localizer). Strictly better than the status quo. |
| all fail | retain `E1_SEA_KERNEL_ACTION_DENSITY_UNCERTIFIED`, **add** `E1_SHARP_RECORD_LOCALIZER_VS_MARGINAL_SEA` | The mechanism is named rather than merely the symptom. |

**The honest partial result available today, before any of these routes runs** (all of it derivable from sealed definitions, and I recommend it be written up as the successor spec's baseline whatever else happens):

1. The sea covariance is pinned **exactly**, with closed-form kernel `(1/2)δ − i α·r/(2π²|r|⁴)`; Phase‑1 ground 1 is over-pessimistic and should be corrected on the record.
2. `K_sea` as defined by Phase 1 is **divergent, not merely uncertified**, in the carrier-blind reading; the functional must be replaced, not certified.
3. The lowest connected two-cell cumulant is a **two-line** object; the anchored `n ≥ 2` sums converge with 2–3 spare powers, with exact constants. NC3's divergence is a one-line artifact and does not corroborate E1 from below.
4. `m0 = 0` is accompanied by `m1 = 0` (exact second-difference structure), annihilates the bare tadpole and all Dyson terms with fewer than two record insertions per CTP branch — and is **exactly saturated** at full `τ_R` by the `e^{±iπ}` record phases, returning the sharp ball projector with weight exactly 1. Phase‑1's `l1`-mass step is tight.
5. The block is therefore confined to `n = 1` and, within it, to the pairing of the marginal sea with the **sharp** localizers `M(t)`, `1_{D_t}` of the sealed Phase‑A construction.

That is a much smaller, much better-named target than "the infrared structure of the massless charged sector."

---

# 5. DEPENDENCY VERDICT

**CONFIRMED: this work needs no Phase‑A/B production output.** Every input is a sealed definition:

- `C = 1_{(-inf,0)}(h_0)`, `C(p) = (I − h_0(p)/|p|)/2` — `STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_RESULT_V001.md`;
- `h_0`, `S = −i n̸ γ⁵`, `M(t) = Q1_{|x|≤r(t)}Q`, `v(t) = τ_R·32r(t)³`, `b_D = exp(16−1/s)`, `J(t) = −(Qb_DQ)⊗α_x` — Phase‑A spec A1/A2 (`789338ad…`), *specification* text, not production output;
- `w_λ = (1/2,−1/4,−1/4)`, `p_λ`, `m0 = 0` — Phase‑A A3, re-derived exactly in Phase 1 §0 and independently re-verified in Phase 2 §1;
- `τ_R = π/√2` — `BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_DERIVATION_V001.md` (`b786db3a…`);
- Lemma 0, O2/R1–R4 — Phase‑1 draft, seal-verified.

This matches the route memo's dependency verdict and spec fence F‑7 verbatim. Two caveats to state in any successor spec:

- **The absence of the Phase‑A bundle costs this work nothing** — and could not help it: any bound evaluated on the `n=2, ℓ ∈ {1,√2}` carriers is carrier-indexed and forbidden by spec-header scoping 1. The `TT2_E*_BLOCKED_BY_ORDERING_PHASE_A_BUNDLE_ABSENT` blocks belong to **O3 (Route T)**, a different obligation, and must not be conflated with E1.
- **F‑7's demotion clause does not apply here.** The E1/M2 work is a statement about the abstract sealed form by construction; there is nothing to demote.

---

## One-line summary for the principal

The block called "T7's true bottom" is not an infrared clustering problem — the connected two-cell cumulant is a **two-line** object decaying as `R^{-6}`, and the anchored sums converge with spare powers (`24ζ(4)+2ζ(6)`, `64ζ(3)+16ζ(5)`). The pointer-weight cancellation you hoped for is real (`m0 = m1 = 0`, an exact second difference) but is **exactly saturated** by the full-`τ_R` `e^{±iπ}` record phases, and what it leaves behind is the **sharp** causal-ball localizer paired against the marginal `|x|^{-3}` massless sea — a coincidence-limit, definition-level obstruction confined to the single-cell activity `n = 1`. Phase 1's `K_sea` is divergent rather than uncertified and must be replaced, not certified. And E1, not O7, is the true bottom: O7 refutes only Route T's transport mechanism, which the executed Route‑Q schema does not use — a question I have flagged for you rather than answered.
