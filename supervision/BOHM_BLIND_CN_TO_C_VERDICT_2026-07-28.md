# BLIND VERDICT — DOES C_n -> C STRONGLY? (Bohm, 2026-07-28)

**BLINDNESS.** Six independent agents (3 prove, 2 refute, 1 well-posedness sceptic), each
cross-examined by an agent assigned to break it, then adjudicated. NO filesystem or corpus access;
posed as self-contained functional analysis. None knew of R-L2b, F'-5, the trilemma, or what turned
on the answer. Codex was offered this question first and STOPPED on its own contamination
declaration (D3 = YES), which is why it was re-run here.

---

## VERDICT

**C_n → C STRONGLY.** Unanimous across all six attempts and six cross-examinations, and — more to the point — I re-derived the decisive chain by hand and checked it numerically in an exactly-solvable surrogate. This is not a vote count; the mathematics is decisive.

---

### 1. Does C_n → C strongly? — YES. Strongly, on all of H, for every cut convention.

The proof needs only **C_c** test functions and one exact operator identity. It never touches the approximants' spectrum, which is why every alleged obstruction evaporates.

Fix ψ; write μ^ψ = ⟨ψ, 1_(·)(h_0)ψ⟩.

- **Lower bound.** For f ∈ C_c, 0 ≤ f ≤ 1, supp f ⊂ (-∞,0): f ≤ 1_{(-∞,0)} pointwise, so f(h_{0,n}) ≤ C_n. SRC gives liminf_n ⟨ψ,C_nψ⟩ ≥ ⟨ψ,f(h_0)ψ⟩; sup over such f (inner regularity) gives **liminf ≥ μ^ψ((-∞,0))**.
- **Upper bound.** For g ∈ C_c, 0 ≤ g ≤ 1, supp g ⊂ (0,∞): g(h_{0,n}) ≤ 1_{(0,∞)}(h_{0,n}) ≤ I − C_n. Hence **limsup ⟨ψ,C_nψ⟩ ≤ ‖ψ‖² − μ^ψ((0,∞)) = μ^ψ((-∞,0])**.
- **The gap between the two bounds is exactly μ^ψ({0}) = ‖1_{{0}}(h_0)ψ‖² = 0.** Squeeze closes.
- Polarization (complex H) upgrades quadratic-form convergence to WOT; then ‖(C_n−C)ψ‖² = ⟨ψ,C_nψ⟩ + ⟨ψ,Cψ⟩ − 2Re⟨ψ,C_n Cψ⟩ → 0, using C_n² = C_n = C_n\*. **SOT.** ∎

Two things this formulation buys that several attempts obtained only after detours: f(0) = g(0) = 0, so the approximants' infinite-multiplicity kernel is never touched by either bound; and the exact relation C_n + 1_{(0,∞)}(h_{0,n}) ≤ I with fixed total mass ‖ψ‖² simultaneously forbids mass escaping to −∞. No tightness lemma, no C_b functional calculus. (**Audit note:** prove-1, prove-2 and prove-3 all routed through "SRC ⟹ f(A_n)→f(A) strongly for f ∈ C_b" via Stone–Weierstrass. That step as written is *unjustified* — C_∞ is not uniformly dense in C_b, and strong convergence is not adjoint-continuous. Two cross-examiners caught it and supplied correct repairs. The conclusion is unaffected; the C_c route above avoids the issue entirely.)

**Independent numerical confirmation** (1D surrogate with identical structural profile: h_0 = −i d/dx, σ = R purely a.c., 0 ∈ σ_ess \ σ_p; Hermite Galerkin, which conjugates to the Gauss–Hermite Jacobi matrix). Test vector φ = (e_0+e_1)/√2, exact target ⟨φ,Cφ⟩ = ½(1 − √(2/π)) = 0.1010577, reference columns of C by quadrature (M₀₀ = 0.500000, M₀₁ = −0.3989423 — exact to 10 digits):

| n | ⟨φ,C_nφ⟩ | ‖C_nφ − Cφ‖ | open−closed gap |
|---|---|---|---|
| 33 | 0.05687 | 0.1891 | 0.0296 |
| 129 | 0.07607 | 0.1395 | 0.0107 |
| 513 | 0.08787 | 0.1007 | 0.0038 |
| 1025 | 0.09159 | 0.0851 | 0.0023 |

Monotone decay at roughly n^(−1/4) — convergence, and slow. Script: `/private/tmp/claude-501/-Users-bgm/4e0e6fab-2cb1-4db4-92f0-cffaf55fb229/scratchpad/adjudicate.py`.

---

### 2. The kernel — CONVENTIONAL, and provably immaterial. The claim IS well posed.

**Placement.** h_{0,n} = 0 ⊕ A_n reduces H = (I−Q_n)H ⊕ Q_nH, so 1_{{0}}(h_{0,n}) = (I−Q_n) + P_{ker A_n}. The open cut puts all of it **out**; the closed cut puts all of it **in**.

**First, one of the prompt's two candidate definitions is not a second definition.** Since 1_{(-∞,0)}(0) = 0, the ambient open cut equals the in-space projection 1_{(-∞,0)}(A_n) embedded by zero — *identically*, not just in the limit. The only live axis is open vs. closed (plus hybrids C_n + R_n with 0 ≤ R_n ≤ 1_{{0}}(h_{0,n})).

**Is open vs. closed forced?** **No — it is a pure convention.** Nothing in the functional calculus, in the Galerkin scheme, or in the β/parity symmetry (both commute with Q_n and with the kernel projection) selects it. I take the prompt's invitation seriously and reject "not well posed" **on proof, not on taste**:

> **1_{{0}}(h_{0,n}) → 0 strongly**, despite having infinite rank and norm 1 for every n. Proof: for continuous χ_δ with 1_{[-δ,δ]} ≤ χ_δ ≤ 1_{[-2δ,2δ]}, ‖1_{{0}}(h_{0,n})ψ‖² ≤ ⟨ψ,χ_δ(h_{0,n})ψ⟩ → ⟨ψ,χ_δ(h_0)ψ⟩ ≤ μ^ψ([−2δ,2δ]) → μ^ψ({0}) = 0.

All conventions therefore have the **same strong limit C**. Ill-posedness would be real only if the conventions had different limits; they demonstrably do not. **Strong convergence is blind to rank** — that is the whole content.

**But do not over-read this.** The ambiguity is *enormous* at every finite n: ‖1_{(-∞,0]}(h_{0,n}) − 1_{(-∞,0)}(h_{0,n})‖ = 1 forever, and my table shows the two conventions differ at finite n by an amount of the same order as the total error. refute-1's claim that they "agree to 5 decimals" was correctly demolished by its cross-examiner as a parity artifact of an even test vector. Sharper still: in my first δ-sweep the sup was pinned by an eigenvalue at −10⁻¹⁷, i.e. **the floating-point sign of a machine-zero eigenvalue silently selected a convention** — a more vivid demonstration that the choice is free than any prose argument. The convention is inert *in the limit, in the strong topology, and nowhere else*.

---

### 3. Spectral pollution — NOT an obstruction, and the usual reason given is the weaker one.

Two independent reasons, in increasing order of force:

1. **Definitionally vacuous here.** DES/Lewin–Séré pollution = limit points of σ(Q_nAQ_n) lying *outside* σ(A), and the theory concerns gaps of σ_ess. h_0 is **massless**: σ(h_0) = R, no gap, nothing outside R. The famous Dirac pollution disease is a mass-gap phenomenon, absent by construction. (Note: refute-2's claim that eigenvalues must accumulate at 0 *from below* was justified by no-spectral-loss, which is degenerate here since 0 is an exact eigenvalue of h_{0,n}; its cross-examiner supplied the correct argument via the squeeze at cut −ε. The claim is true, the original proof was not.)
2. **The load-bearing reason — pollution could not obstruct this even if a gap existed.** If (a,b) lies in a gap of σ(A) and χ ∈ C_c is 1 on (a,b) with support in the gap, then 1_{(a,b)}(A_n) ≤ χ(A_n) → χ(A) = 0 strongly. **Spurious eigenvalues carry asymptotically zero spectral weight against any fixed vector.** Pollution is a statement about spectra as *sets* (eigenvalue approximation, norm-resolvent behaviour); strong projection convergence is a statement about spectral *measures of fixed vectors*. Importing the pollution literature's pessimism here is a category error.

**Does the Hermite/N structure help, and is it sufficient?** It is load-bearing but in exactly one place: [Q_n, N] = 0 with h_0² = −Δ ≤ N is what delivers SRC (‖h_0(I−Q_n)ψ‖ ≤ ‖(I−Q_n)N^{1/2}ψ‖ → 0 on the core, then RS VIII.25(a)). I verified this premise rather than assuming it. It buys nothing else, and nothing else is needed: **SRC + μ^ψ({0}) = 0 is the complete hypothesis set.** It does *not* give a Lewin–Séré no-pollution certificate, and the Lewin–Séré sufficient condition genuinely fails (C is a degree-0 homogeneous Fourier multiplier and does not preserve Hermite spans). Irrelevant.

Note also that a spurious kernel *inside* Q_nH is real and large: A_n is off-diagonal in the Hermite parity grading, forcing dim ker A_n ≥ |dim E_n − dim O_n| ~ m²/4 for degree-graded truncations in R³. Growing without bound — and still strongly null. Dimension is simply not the relevant measure.

---

### 4. The shifted cut — I rule AGAINST the shape the prompt guessed.

State it in five parts, because the sides differed here and the differences are real:

1. **For every fixed δ > 0 (indeed every cut λ ∈ R): converges strongly.** h_0 has *no eigenvalues at all*, so every cut point satisfies the hypothesis. The shifted cut is strictly easier, not a rescue.
2. **At fixed n, the δ↓0 limit of 1_{(-∞,-δ)}(h_{0,n}) is the OPEN cut C_n**, by continuity from below of the spectral measure. The closed cut is not the δ↓0 limit of the shifted family at any n; it differs by 1_{{0}}(h_{0,n}), norm 1.
3. **The δ→0 limit IS uniform in n, pointwise in ψ, for the open cut:** sup_n μ_n^ψ([−δ,0)) → 0 as δ↓0. (Fixed δ: limsup_n ≤ μ^ψ([−2δ,2δ]); each fixed n contributes 0 once δ drops below the smallest nonzero |eigenvalue| of h_{0,n}, ~ π/√(2n) in the surrogate; combine.) **Hence lim_δ lim_n = lim_n lim_δ = C.** Confirmed numerically: sup_n μ_n^φ([−δ,0)) = 0.059, 0.056, 0.038, 0.022, 0.012 for δ = 1, 0.5, 0.2, 0.1, 0.05 — tracking the limit mass and vanishing, with argmax n growing like δ⁻² exactly as predicted.
4. **It is NOT uniform in n for the closed cut** — the refinement the wellposed-sceptic's cross-examiner found, and it is correct: 1_{[−δ,0]}(h_{0,n}) ≥ 1_{{0}}(h_{0,n}) ≥ I − Q_n, so sup_n μ_n^ψ([−δ,0]) ≥ ‖(I−Q_1)ψ‖² > 0 for *every* δ. Measured: 0.203, δ-independent. So the interchange-of-limits statement is a **third** convention-sensitive category, alongside norm-level and index/charge statements.
5. **The genuine non-uniformity is in ψ, at every δ including 0.** ‖1_{(-∞,-δ)}(h_{0,n}) − 1_{(-∞,-δ)}(h_0)‖ = 1 for all n and δ. And ‖1_{(-∞,-δ)}(h_0) − C‖ = 1 for every δ > 0 — no Galerkin family involved. The δ-family of *exact* projections is itself norm-discontinuous at δ = 0.

So: **not** "converges for δ > 0 but the δ→0 limit is non-uniform." That guessed shape is wrong for the open cut; the honest shape is *uniform in δ, never uniform in ψ*.

---

### 5. The single decisive point

**μ^ψ({0}) = 0 for every ψ — i.e. 0 is not an eigenvalue of h_0 — and the hypothesis of the SRC/spectral-projection theorem (Weidmann, *Linear Operators in Hilbert Spaces*, Thm 9.19; not RS VIII.24, which is the norm-resolvent/spectrum-approximation statement several attempts misattributed) is a condition on the LIMIT ALONE.**

Everything follows. That 0 ∈ σ_ess(h_0) is irrelevant — the theorem constrains atoms, not essential spectrum. That the approximants carry an infinite-multiplicity atom exactly at the cut is not a hypothesis violation but a *consequence-free artifact*: SRC itself forces 1_{{0}}(h_{0,n}) → 0 strongly. In three languages it is one fact: *0 not an eigenvalue of h_0* = *μ^ψ has no atom at 0* = *ψ̂ carries no L² mass at p = 0, where the degree-0 homogeneous multiplier C(p) = (I − α·p̂)/2 is discontinuous*.

---

### 6. What would change the answer, and confidence

**Confidence: HIGH** on the verdict; near-certain. Only two inputs, both checked rather than assumed: SRC (verified via [Q_n,N] = 0, h_0² ≤ N, RS VIII.25(a)) and μ^ψ({0}) = 0 (verified in Fourier: eigenvalues ±|p|, {p=0} Lebesgue-null).

**What flips it:** a zero mode in the limit. Give h_0 an eigenvalue at 0 (zero-energy bound state of an interacting Dirac operator; *not* the massive free case, where 0 sits in the resolvent set and everything is easier) and the squeeze in §1 leaves a gap of exactly μ^ψ({0}) > 0. SRC then no longer *determines* the limit, the open/closed convention becomes load-bearing, and **"NOT WELL POSED" becomes the correct answer.** The knife edge is that sharp. The scalar witness: A_n = ∓1/n → A = 0 on any space — SRC in every sense, 1_{(-∞,0)}(A_n) = I or 0 depending on the sign.

**What does not flip it:** any amount of pollution, any growth rate of dim ker A_n, any accumulation of Galerkin eigenvalues at the cut, any reordering of the Hermite basis.

**Honest limitation — the result is weak, and the framing invites over-reading.** For *both* conventions:
- **No norm convergence, ever:** ‖C_n − C‖ = 1 for all n (open cut: Ran C ∩ ker C_n ≠ 0 by finite rank; closed cut: same on complements, since I − C_n^cl is finite rank).
- **C_n − C is not compact**, a fortiori not Hilbert–Schmidt.
- Therefore **Shale–Stinespring fails along this sequence**: the Galerkin sea does *not* converge as a second-quantized/Fock-space object, and nothing here supports a trace, a charge tr(C_n − Q_nCQ_n), a polarization density, or a renormalized vacuum energy. Those quantities are also genuinely convention-dependent.
- **No rate is proved in 3D.** The n^(−1/4) exponent is empirical in the 1D Fourier-invariant tridiagonal surrogate and should not be quoted as a property of Q_n(−iα·∇)Q_n.

If the downstream use of "the sea converges" needs any topology stronger than SOT, this theorem supplies nothing, and the real question is a different one.