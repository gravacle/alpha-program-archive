# BLIND VERDICT — WEAK SCHATTEN / DIXMIER TRACE (Bohm, 2026-07-28)

Reviewer-lane PROPOSAL, tested blind and REFUTED. Six agents, six routes, unanimous on Q1 = NO;
all six cross-examinations sustained. No corpus access. The proposal was the reviewer's, not the
corpus's — Dixmier, weak Schatten, Connes, Lorentz ideal, Macaev all return ZERO hits corpus-wide.

---

# ADJUDICATION

## Bottom line

**The construction fails, and it fails one level below where the question expected.** Not "in the weak class but non-measurable" — that outcome does not occur here in either direction. The object is not in any ideal at all, because it is not compact. And the premise that supplies the log is arithmetically wrong in d = 3.

Six agents, six independent routes, **unanimous on Q1 = NO**. All six cross-examinations sustained. I rule with them, and I sharpen the diagnosis below in a way none of them stated completely.

---

## 1. Q1 — IS X ∈ S_{2,∞}?

**NO. X is not compact.** μ_n(X) does not tend to 0, let alone like n^{-1/2}.

Two independent proofs, both short.

**(i) Exact algebraic identity.** Since (α·p̂)² = I, write F := α·p̂ = sgn(h₀); F = F\* = F^{-1}. Then C = (I − F)/2 and the off-diagonal part of the kernel is exactly the operator **C_off = −F/2**. Hence

  C_off W C_off = (1/4) F W F ≅ (1/4) W  (unitary equivalence, F unitary).

The most charitable reading — drop the δ-term, sandwich with the pure Calderón–Zygmund piece — is *unitarily equivalent to W/4*. Singular values (1/4)·(essential range of |w|). This forecloses the standard objection that the δ³(r) term is an artifact of the decomposition: it isn't the δ-term that kills you.

**(ii) Weyl sequence, for the literal X = CWC.** Fix ê ∈ S², a spinor v with C(ê)v = v, φ ∈ C_c^∞ supported in the interior of supp w. Put u_λ(x) = e^{iλê·x}φ(x)v. Then u_λ ⇀ 0; since C is Lipschitz on S² and the packet lives at |p| ~ λ → ∞ (the p = 0 singularity is invisible), ‖Cu_λ − u_λ‖ → 0; so ⟨u_λ, Xu_λ⟩ → ∫w|φ|² ≠ 0. Hence ‖X‖_ess = ‖w‖_∞ for scalar w. Equivalently: the principal symbol c(ξ)w(x)c(ξ) = w(x)c(ξ) does not vanish.

**Why no estimate can rescue it.** Every Cwikel / Birman–Solomyak / Kato–Seiler–Simon statement bounds ‖M_f g(−i∇)‖ by a norm of g in some L^{p} or L^{p,∞}, p < ∞. Here ‖c(p)‖_op = **1 for every p ≠ 0** — c is a rank-2 projection pointwise. Its distribution function is +∞ for every λ < 1. So c ∈ L^∞ and in nothing smaller: every such estimate has an infinite right-hand side. This is not a marginal miss; and by (i)–(ii) it is *necessary*, since the conclusion (compactness) is false. **OBSTRUCTION, not technicality.**

**The best case available, and it is still no.** If W is matrix-valued and anticommuting (mass-type, W = v(x)β), then c(ξ)βc(ξ) = 0, the principal symbol vanishes, X drops to order −1, and X ∈ S_{3,∞}: μ_n ~ n^{−1/3}. Still strictly outside S_{2,∞}. The reachable rungs in this algebra are order 0 (non-compact) and order −1 (S_{3,∞}). Order −3/2, which is what S_{2,∞} demands in d = 3, is not among them.

*(Adjudicated: "refute-class" §7's "half orders are structurally unavailable" is a heuristic, correctly demoted by its cross-examiner. The rigorous closure is Janson–Wolff: for p ≤ d, [b, R_j] ∈ S_p forces b constant; since S_{2,∞} ⊂ S_{5/2} and 5/2 ≤ 3, no non-constant w reaches S_{2,∞}. Elementary version: a kernel |r|^{−3/2} would need |w(x)−w(y)| ≲ |x−y|^{3/2}, exponent > 1, forcing w constant.)*

## 2. Q2 — IS THE DIXMIER TRACE DEFINED?

**On X\*X: NO, and vacuously.** μ_n(X\*X) = μ_n(X)² → ‖w‖_∞² > 0, so Σ_{n<N} μ_n(X\*X) ~ ‖w‖_∞²N and the log-Cesàro means diverge for *every* generalised limit. X\*X lies outside S_{1,∞} and outside the larger Dixmier–Macaev ideal M_{1,∞}. Tr_ω(X\*X) is undefined, not non-canonical.

Two structural notes:

- **Q2 as posed is not independent of Q1.** μ_n(X\*X) = μ_n(X)², so X ∈ S_{2,∞} ⟺ X\*X ∈ S_{1,∞} identically. All the content is in Q1.
- **The question's stated equivalence is slightly off, and the correction matters.** Dixmier traces live on M_{1,∞} = {Σ_{n<N} μ_n = O(log N)}, which **strictly contains** S_{1,∞}. So "Σ_{n≤N} μ_n(X)² ~ c log N" does *not* force μ_n(X) = O(n^{−1/2}); monotonicity gives only μ_n = O(√(log n / n)). The "direct" agent's sparse-block diagonal counterexample is valid and this is its one genuinely important contribution: **the chain "log-divergent HS ⟹ S_{2,∞}" is invalid as a general implication**, before one even looks at this operator. (Its verdict grid, however, equivocates between two branches — Q1 = NO is proved for the literal X, Q2 = YES is asserted for a hypothetical object. Its cross-examiner is right; the grid must be read branch-labelled.)

**The right object** (see §7): |[F, M_w]|³, exponent **3**, not 2.

## 3. Q3 — IS IT MEASURABLE? *(the decisive question)*

**Ruling, in three parts.**

**(a) For X\*X: NOT APPLICABLE — and this is established, not open.** There is no Dixmier trace whose ω-dependence could be tested. Four agents reported "UNRESOLVED"; that label is schema-forced and misleading downstream. The correct report is **VACUOUS**. This is a *stronger* negative than non-measurability: non-measurability would leave a family of finite ω-dependent numbers; here there is no number at all.

**(b) The sharp cutoff does NOT break measurability. It breaks compactness.** This is the single most important correction to the question's framing, and all six agents converged on it independently.

- Non-smoothness of the *spatial* factor is a **technicality** for measurability. The non-smooth Connes trace formulas (Kalton–Lord–Potapov–Sukochev; Lord–Sukochev–Zanin) give measurability with the spatial factor merely in L²: for f ∈ L²(R³), M_f(1−Δ)^{−3/4} ∈ S_{2,∞} and Tr_ω(M_f(1−Δ)^{−3/2}M_f̄) = c₃‖f‖₂² for **every** ω, with f = 1_Ω a sharp indicator explicitly allowed.
- What sharpness *does* is destroy compactness of the only object that could have carried a trace. C_off = −F/2 with F = i Σ_j α_j R_j; the bounded partial-trace extraction A ↦ ¼tr_{C⁴}(α_k A) returns −(i/2)[R_k, b] and preserves every ideal. By **Coifman–Rochberg–Weiss + Uchiyama**, [R_j, b] is bounded for b ∈ BMO and compact **iff b ∈ VMO**. 1_Ω ∈ BMO \ VMO whenever ∂Ω ≠ ∅. Hence **[C, 1_Ω] is bounded and not compact.** Structural corroboration: C is homogeneous of degree 0 so it commutes with dilations; a half-space is dilation-invariant; a nonzero operator commuting with a unitary group with no eigenvectors cannot be compact.
- Quantitatively: for w ∈ Ẇ^{1,3} the canonical invariant is ∫|∇w|³, and for a mollification at scale ε this blows up like Area·ε^{−2}. **The sharp limit has no finite canonical residue** — it is not that the residue becomes ω-dependent, it is that it diverges and the operator leaves the class.

**(c) Above the regularity threshold, measurability HOLDS.** For w ∈ Ẇ^{1,3}(R³) ∩ L^∞, [F, M_w] ∈ L_{3,∞} and |[F,M_w]|³ is measurable (Connes; Lord–McDonald–Sukochev–Zanin, JFA 2017 — a theorem literally about sgn(D) for the massless Dirac operator, i.e. exactly this F). For w ∈ C_c^∞ one gets it unconditionally from the two-sided Birman–Solomyak Weyl asymptotic μ_n([C,w]) ~ Cn^{−1/3}, which is a genuine Tauberian condition and forces all Dixmier traces to agree.

**So the regularity dial has two settings and neither yields the feared third outcome:** below threshold you fall out of compactness entirely; at or above threshold you are measurable. I looked for an intermediate Hölder/Besov window producing "in the class but ω-dependent" and, like the agent assigned to find it, could not construct one.

⚠️ **One honest citation-level caveat.** Some quantum-differentiability formulas are established for Dixmier traces built from dilation- or Cesàro-invariant ω, which is weaker than measurability against *all* Banach limits. For w ∈ C_c^∞ this is closed by the Weyl asymptotic. For w merely in Ẇ^{1,3} it rests on the cited theorem. Flag as a citation risk, not an obstruction.

*(Adjudicated: "right-object" reported `q3: YES_CANONICAL` in its verdict line while its body says the question is vacuous for X\*X and YES only for a different, repaired object. Its cross-examiner is right that this inverts the finding if read alone. **Corrected to VACUOUS, with the YES quarantined to |[C,w]|³.**)*

## 4. Q4 — DOES IT EXTRACT THE LOG COEFFICIENT?

**NO for this object. But state the affirmative half first, because it is real and the question deserves it.**

**Affirmative half.** For A ∈ Ψ^{−d}_cl compactly supported, Tr(A·1_{|D|≤Λ}) = Res_W(A)·log Λ + O(1) and Tr_ω(A) = (1/d)Res_W(A). So a Dixmier trace *is* a log-Cesàro mean and can see nothing but a log coefficient; log coefficients, unlike power-law coefficients, are regularization-scheme independent. The mechanism the question hopes for exists and is universal.

**But the "universal constant" is not universal.** If the divergence is stated in a *spatial* cutoff a rather than a spectral one, the dictionary is log N = κ·log(1/a) with κ = the dimension of the set carrying the divergence: κ = d for a bulk/phase-space log, κ = d−1 for a boundary log, κ = 1 for a curve. So the constant is a geometric dimension that must be determined case by case, not a universal number. Any identification that omits it is wrong by a factor of 2 or 3.

**Negative half, four reasons in decreasing order of generality.**

1. **There is no log in ‖X‖₂² at all.** This is load-bearing; the other three are corroborating. The premise conflates ∫|K| with ∫|K|². Squaring the given kernel (Frobenius, which is what HS requires): ‖C_off(r)‖_HS² = tr[(α·r̂)²]/(4π⁴r⁶) = 1/(π⁴r⁶), so ∫_{a<|r|<R} = (4/3π³)(a^{−3} − R^{−3}). **Cubic power divergence.** For the literal X = CWC the (1/4)M_w term alone gives ‖X‖₂² ~ ca^{−3}∫|w|², exactly as non-compactness demands (Σ_{n<N}μ_n² ~ ‖w‖_∞²N, N ~ Vol·a^{−3}).
2. **The 2/π log is an order-0 certificate, i.e. the wrong end of the order scale.** ∫_{a<|r|<R}‖K‖ = log(R/a)·∫_{S²}‖Ω(θ)‖dσ is the Calderón–Zygmund marginality statement: a degree −d odd kernel is bounded by cancellation and locally non-integrable by an inch. It is the log that makes the Riesz transforms bounded-and-non-compact. A Wodzicki residue, by contrast, is the coefficient of **log|x−y| in the diagonal expansion** of an order −d kernel. Same word, opposite ends of the order scale. And Res_W(CWC) = 0: by the trace property Res(C·WC) = Res(WC·C) = Res(WC), and σ(M_W ∘ C) = W(x)c(ξ) is *exact* (no lower-order terms), homogeneous of degree 0, so σ_{−3} ≡ 0.
3. **2/π exists only because an absolute value discarded a cancellation.** C_off is odd (zero spherical mean) and tr_{C⁴}(α_j) = 0, so *every* linear symbol- or kernel-functional annihilates it. Traces are linear. No trace can reproduce a number manufactured by taking ‖·‖_op pointwise before integrating.
4. **2/π is convention-dependent and not a unitary invariant.** ‖α·r̂‖_op = 1, ‖·‖_HS = 2, ‖·‖_tr = 4, giving 2/π, 4/π, 8/π. It is a position-representation kernel quantity, not invariant under unitary conjugation, whereas every Dixmier trace is. It is also W-independent, whereas Tr_ω(X\*X) is quadratic in W. And the *same* constant 2/π comes out of the 1D Hilbert kernel 1/(π|r|) — the same number in two different dimensions, so it encodes no d = 3-specific content.

*(Adjudicated: "right-object" advertised four independent, each-fatal reasons. Its cross-examiner is correct that (3) and (4) attack the number 2/π, not the question as literally posed — the log coefficient of ‖X‖₂² would be a unitary invariant and quadratic in W. On the posed reading only (1) bites; on the "is 2/π canonical" reading (2)–(4) bite. Both readings are answered; the "four independent fatal reasons" framing is overstated by half. "connes" and "direct" reported PARTIALLY; that correctly captures the affirmative half and I have folded it in.)*

---

## 5. THE DECISIVE POINT

**One counterexample, in the dimension where the premise is literally true, killing the inference anyway.**

Take d = 1: P = 1_{(0,∞)}(p), Hilbert-transform projection — same structure, degree-0 homogeneous symbol, no UV scale, sharp spatial cutoff χ = 1_I. Here the premise's scenario is *exactly realized*: the off-diagonal block Y = χPχ^⊥ has

  ‖Y‖₂² = Tr(A − A²) = (1/π²)·log(L/a) + O(1),  A := χPχ,

a genuine logarithm with an exact coefficient (Kac–Murdock–Szegő / Widom). And the conclusion is still **false**: χPχ has **purely absolutely continuous spectrum filling [0,1]** (Koppelman–Pincus, Rosenblum — the classical spectral theory of the finite Hilbert transform). So Y is bounded and **not compact**, μ_n(Y) ↛ 0, and there is no Dixmier trace of any kind.

I verified this numerically (grid sizes 256–4096, exact diagonalization of A = χPχ):

| N | Tr(A−A²) | Δ per doubling / log2 | #{λ > 10⁻³} | max_n n·λ_n | λ₁ |
|---|---|---|---|---|---|
| 256 | 0.7384 | — | 9 | 0.413 | 0.2439 |
| 512 | 0.8086 | 0.1013 | 10 | 0.453 | 0.2448 |
| 1024 | 0.8789 | 0.1013 | 11 | 0.487 | 0.2456 |
| 2048 | 0.9491 | 0.1013 | 12 | 0.516 | 0.2462 |
| 4096 | 1.0193 | 0.1013 | 13 | 0.540 | 0.2466 |

0.1013 = 1/π² to four figures — the log is exactly as advertised. And simultaneously: λ₁ → 1/4 (i.e. μ₁(Y) → 1/2, saturating, no decay); the number of eigenvalues above any fixed threshold grows like log N; and sup_n n·λ_n grows without bound in the cutoff. **S_{2,∞} would force sup_n n·λ_n bounded uniformly in the UV regulator. It is not.**

**This is the whole lesson.** The log divergence in the marginal case is *not* a tail phenomenon (many small singular values decaying like n^{−1/2}); it is a *bulk* phenomenon — the singular values spread out to fill an interval as the cutoff is removed, and the log is the rate at which the bulk fills in. Those two mechanisms produce the same Σμ_n² and completely different spectra. A log-divergent Hilbert–Schmidt norm is **compatible with, and here is a symptom of, non-compactness.**

Combine with the d = 3 arithmetic and the construction is dead twice: **in d = 3 there is no log; and where there is a log (d = 1) there is no compactness.**

**The dimensional bookkeeping, which no agent stated in full and which is the cleanest diagnostic available:**

| divergence of ‖·‖₂² | general d | logarithmic iff |
|---|---|---|
| smooth profile w, bulk: ‖[C,w]‖₂² ~ ∫_a ρ^{1−d}dρ | a^{−(d−2)} | **d = 2** |
| sharp region Ω, boundary: ‖χ_Ω C χ_Ω^⊥‖₂² ~ Area·∫_a ρ^{−d}dρ | Area·a^{−(d−1)} | **d = 1** |
| literal CWC (δ-term) | a^{−d} | never |

In d = 3: a^{−1}, Area·a^{−2}, a^{−3}. **No log anywhere.** The picture the question paints — order −d/2, S_{2,∞}, square in S_{1,∞}, Dixmier trace = log coefficient — is *entirely correct in two dimensions*, where [C,w] has order −1 = −d/2. In three dimensions the commutator still has order −1, and −d/2 = −3/2 is unreachable. The premise looks like a correct d = 1 or d = 2 fact transplanted to d = 3.

---

## 6. WHAT WOULD CHANGE THE ANSWER, AND CONFIDENCE

**Confidence.**
- Q1 = NO: **essentially certain** (two independent proofs, one an exact unitary equivalence; numerically corroborated in the 1D shadow).
- Q2 = NO on X\*X: **essentially certain** (immediate from Q1 via μ_n(X\*X) = μ_n(X)²).
- Q3 diagnosis (vacuous for X\*X; sharpness kills compactness not measurability; measurable above threshold): **high**, with the one flagged caveat about which class of ω the Ẇ^{1,3} theorems cover.
- Q4 = NO: **essentially certain** on the arithmetic (a^{−3}/a^{−1}/Area·a^{−2}), with the affirmative half of the mechanism stated correctly.

**What would change it:**

1. **A genuine UV cutoff in momentum** — replacing C by a projection onto a *bounded* momentum region with a smooth Fermi surface (or a lattice regularization). Then Cwikel applies, the kernel decays like |r|^{−(d+1)/2} with oscillation, compactness returns, and the **Widom–Sobolev** theorem gives a canonical L^{d−1}log L coefficient. But that log is a *scaling asymptotic*, not a Dixmier trace; its coefficient is a double boundary integral over ∂Ω × ∂Γ; and it depends on the cutoff scale, so it is not scale-free. Note the structural tension: **the exact scale invariance that makes the massless Dirac projection attractive (degree-0 symbol, no scale in C) is precisely what forbids the compactness a Dixmier trace requires.** For massless Dirac, χ_{LΩ}Cχ_{LΩ} is *L-independent* by dilation invariance — there is no log L at all.
2. **d = 2 instead of d = 3.** The entire construction is correct in two dimensions. If the underlying program's dimension count is what is really at issue, that is where to look.
3. **A partial-wave / half-line reduction.** Then the log premise becomes true — but the 1D counterexample in §5 shows the operator is *still* not compact, so it still fails, unless a UV cutoff is supplied.
4. **Inserting a momentum weight of order exactly −3/2**, e.g. M_w(1−Δ)^{−3/4} or |h₀|^{−3/4}M_w|h₀|^{−3/4}. Then w ∈ L²(R³) (sharp indicators allowed) gives S_{2,∞}, and Tr_ω = c₃∫|w|² for every ω — measurable, canonical, sharp cutoff and all. But that is not CWC, and the constant is a volume integral of |w|², carrying no trace of 2/π.

**None of these delivers 2/π.** If the program needs 2/π to be canonical, it must be argued as what it actually is: the L¹(S²) angular mass of the Calderón–Zygmund kernel of an order-0 operator. That *is* a well-defined, scheme-independent number in its own right (log coefficients are), but it is convention-dependent (2/π, 4/π, 8/π), representation-dependent, W-independent, and cannot be a spectral invariant of anything.

---

## 7. THE CANONICAL FINITE OBJECT, IF YOU WANT ONE

There *is* a canonical, measurable, computable number in this algebra. It is not a square and it is not 2/π.

**Setup.** F := sgn(h₀) = α·p̂ = I − 2C, so (H, F) is a (3,∞)-summable Fredholm module. Let w ∈ Ẇ^{1,3}(R³) ∩ L^∞ be real-valued and compactly supported (**a sharp cutoff is excluded** — 1_Ω ∉ Ẇ^{1,3}, its gradient is a surface measure).

**Object.** The quantized differential dw := [F, M_w] = −2[C, M_w]. Then dw ∈ L_{3,∞} (μ_n ~ n^{−1/3}), and the Dixmier-traceable object is the **cube**:

  |dw|³ ∈ L_{1,∞}, measurable.

**Symbol.** With g = ∇w and g_⊥ = g − ξ̂(ξ̂·g),

  σ_{−1}([F,M_w])(x,ξ) = −(i/|ξ|)·α·g_⊥,  |σ_{−1}| = (|∇w| sin θ /|ξ|)·I₄, θ = ∠(ξ, ∇w).

**Value.** Using Tr_ω(A) = (1/(d(2π)^d))∫_{S\*M} tr σ_{−d}, with ∫_{S²} sin³θ dσ = 3π²/4:

  **Tr_ω(|[sgn h₀, M_w]|³) = (1/(8π)) ∫_{R³} |∇w(x)|³ dx**, for every ω,

and equivalently **Tr_ω(|[C, M_w]|³) = (1/(64π)) ∫_{R³} |∇w|³ dx** (factor 8 from C = (I−F)/2).

**Citation, corrected.** Three agents derived this via "Seeley complex powers + Connes' trace theorem." **That step is invalid**: Seeley requires ellipticity, and [C,w] is not elliptic — σ_{−1} vanishes identically off supp ∇w *and* wherever ξ̂ ∥ ∇w. So |[C,w]| is not a classical ΨDO and (A\*A)^{3/2} is not in the class Connes' theorem covers. The correct authorities are **(i) Birman–Solomyak / Grubb eigenvalue asymptotics for negative-order, non-elliptic ΨDOs**, μ_n(A) ~ (C/n)^{m/d} with C = (1/(d(2π)^d))∫∫_{|ξ|=1} tr|σ_{−m}|^{d/m} — which yields the same number and, being a two-sided pointwise asymptotic, gives full measurability directly; and **(ii) Lord–McDonald–Sukochev–Zanin (JFA 2017)** for the sharp Ẇ^{1,d} threshold. The displayed constant follows from either; anyone computing should re-verify the Connes normalization convention, which is where factors of d and (2π)^d are most often lost.

**What this number is and is not.** It is canonical, ω-independent, and a genuine noncommutative-geometric integral. It is **cubic in w**, supported on ∇w, blows up like Area·ε^{−2} as a cutoff is mollified at scale ε, contains no angular L¹ mass of C_off, and is not a logarithm of anything. Its universal constant is an L³-with-cancellation average of the symbol of F over S², never the L¹ mass 2/π.

**If the program needs a log in a second-power quantity in three dimensions, the dimensional bookkeeping is wrong upstream — independently of everything about ω.** In d = 3 the canonical quantized integral is cubic.

---

## Errata to carry forward (each caught in cross-examination, each verified)

| # | Item | Correction |
|---|---|---|
| 1 | Seeley + Connes' trace theorem for \|[C,w]\|³ | Invalid — [C,w] is not elliptic. Use Birman–Solomyak/Grubb Weyl asymptotics or LMSZ. Value unchanged. |
| 2 | "Res_W(CWC)=0 because C has no lower-order expansion" | False premise (the composition σ(C∘M_W) does have an \|α\|=3 term). Correct proof: Res(C·WC) = Res(WC·C) = Res(WC), and σ(WC) = W(x)c(ξ) is exact, degree 0, so σ_{−3} ≡ 0. |
| 3 | HS constant (1/3π³)a^{−3} | Uses ‖·‖_op²; HS requires Frobenius, ‖C_off‖²_HS = 1/(π⁴r⁶) ⟹ **(4/3π³)a^{−3}**. Power either way. |
| 4 | "{p : ‖C(p)‖>t} is a cone of infinite measure for t<1/2" | ‖C(p)‖_op = **1** for all p ≠ 0; the set is all of R³\{0} for every t < 1. Hypothesis failure is total, not partial. |
| 5 | "p=2 Cwikel endpoint (L²,L^{2,∞})→S_{2,∞} is false" | The *symmetric weak-weak* endpoint is false; (L², L^{2,∞}) → S_{2,∞} is the correct LSZ statement. Irrelevant here (c ∉ L^{q,∞} ∀q<∞). |
| 6 | "orders step by integers, so −3/2 unreachable" | Heuristic. Rigorous: Janson–Wolff (p ≤ d ⟹ b constant), applied to S_{2,∞} ⊂ S_{5/2}; or elementary Hölder-3/2 ⟹ w constant. |
| 7 | `q3: YES_CANONICAL` in a verdict line | Contradicts its own body. Must read **VACUOUS for X\*X**; the YES belongs only to \|[C,w]\|³ with w ∈ Ẇ^{1,3}. |
| 8 | Silent scalar-W assumption | If W = v(x)β (anticommuting/mass-type), c β c = 0, X drops to order −1 and lands in S_{3,∞}. Best case — still not S_{2,∞}. |