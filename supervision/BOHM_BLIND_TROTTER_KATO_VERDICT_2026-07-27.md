# BLIND TROTTER-KATO REFERRAL — VERDICT (Bohm reviewer lane, 2026-07-27)

**BLINDNESS PROTOCOL.** Six independent agents (3 assigned to prove, 3 to refute), each
cross-examined by an agent assigned to break it, then adjudicated. NO agent had filesystem or
corpus access; the question was posed as self-contained functional analysis. None knew of R-L2b,
F'-5, the trilemma, or what turned on the answer.

---

# VERDICT

All six attempts converge on the truth values. The disagreements are (i) the *label* on (5) — whether Trotter–Kato is the instrument — and (ii) a claimed conditional fork (prove-3, refute-3) making (5) `DELICATE_UNRESOLVED` if the cutoff is genuinely sharp. I rule on both. The fork is spurious. The label is wrong in four of six answers.

---

## 1. ITEM (3): **TRUE**

Write `N = (-Δ + |x|²) ⊗ I₄` (Hermite functions are its eigenfunctions), `B¹ := D(N^{1/2}) = {u : ∇u ∈ L², |x|u ∈ L²}` (Shubin `Q¹`). Two facts do all the work:

**(F1)** `h₀² = -Δ ⊗ I₄`. From `{α^j,α^k} = 2δ^{jk}`, the cross terms in `(-iα·∇)²` cancel. Hence for `u ∈ B¹`,
```
||h₀u||² = ||∇u||² ≤ ||∇u||² + |||x|u||² = ||N^{1/2}u||².
```

**(F2)** `Q_n` is diagonal in an orthonormal eigenbasis of `N`, hence `Q_n N^{1/2} = N^{1/2} Q_n` on `D(N^{1/2})`. This holds for **any** enumeration of the 3-D multi-indices, including one that splits a degenerate oscillator level — the "first n Hermite functions" ambiguity in 3-D is genuinely immaterial, and no Simon/Thangavelu rapid-decay machinery is needed (prove-1 invokes it unnecessarily; `||N^{1/2}(I-Q_n)ψ||² = Σ_{α∉S_n} λ_α|c_α|²` is just the tail of a convergent series).

**Proof of (3).** `Ran Q_n ⊂ S`, so `h_{0,n} := Q_n h₀ Q_n` is finite-rank, symmetric, everywhere defined, hence **bounded self-adjoint on H**. Therefore *every* dense subspace is a core for `h_{0,n}`; `S` is a core for `h₀` by hypothesis; so `S` **is** a common core, with no work. For `ψ ∈ B¹ ⊇ S`:
```
Q_n h₀ Q_n ψ - h₀ψ = Q_n h₀(Q_n - I)ψ + (Q_n - I)h₀ψ,
||Q_n h₀(Q_n-I)ψ|| ≤ ||h₀(Q_n-I)ψ|| ≤ ||N^{1/2}(Q_n-I)ψ|| = ||(Q_n-I)N^{1/2}ψ|| → 0,
```
and the second term → 0 since `h₀ψ ∈ H`. ∎

**Sense of convergence:** strongly on the core, **and** therefore in strong resolvent sense (Reed–Simon I, Thm VIII.25(a), whose hypotheses are met exactly, not approximately). **Not** in norm resolvent sense: on `(I-Q_n)H` the resolvent of `h_{0,n}` is `-i`, while `(h₀+i)^{-1}` is small on high-frequency states, so `||(h_{0,n}+i)^{-1} - (h₀+i)^{-1}|| ≳ 1` for every `n`.

**Two corrections to the record.**
- (3) is **not** a consequence of (1)+(2). It is a theorem about *this* family, resting on (F1)+(F2). Rotate the Hermite basis slightly and the basis vectors leave `D(h₀)`; `Q_n h₀ Q_n` is then not even defined. All four agents who stressed this are right, and it is the correct place to put the weight.
- The proof gives convergence on `B¹ = D(N^{1/2})`, **not** on `D(h₀) = H¹`. Several agents asserted that convergence on `H¹` "likely fails," citing Askey–Wainger. **That citation does not support the claim** — Askey–Wainger concerns `L^p`, `p ≠ 2`, and says nothing about `H¹`. The correct status is: *unknown, and irrelevant*. Trotter–Kato needs a core, `S ⊂ B¹` is one, and nothing downstream touches `H¹ \ B¹`. Do not assert `h_n φ → hφ` for all `φ ∈ D(h₀)`; it is unproven either way.

---

## 2. ITEM (4): **TRUE**, trivially

For any bounded `A` and orthogonal `Q_n → I` strongly:
```
Q_n A Q_n ψ - Aψ = Q_n A(Q_n-I)ψ + (Q_n-I)Aψ,  norm ≤ ||A||·||(Q_n-I)ψ|| + ||(Q_n-I)Aψ|| → 0.
```
Uses **only** `||Q_n|| ≤ 1` and boundedness. No Gevrey regularity, no self-adjointness, no compactness, no property of the cutoff. ∎

**Uniform-in-t form** (needed for (5)): `sup_{|t|≤T} ||(Q_n M_c(t)Q_n - M_c(t))ψ|| → 0`. The first term is already `t`-uniform; the second needs `{M_c(t)ψ : |t| ≤ T}` compact, i.e. **strong continuity of `t ↦ M_c(t)`**. That does hold here (dominated convergence across the moving sphere, `r` continuous; under the flat-profile reading it is even norm continuity). This is the one hypothesis in the whole problem that is *imported* rather than stated — the problem gives boundedness and uniform boundedness in `t`, not `t`-continuity of `b_D`. Flag it, but it is supplied by the construction.

Never in norm: `||Q_n A Q_n - A|| → 0` forces `A` compact. Correct, as stated, and costless.

---

## 3. ITEM (5): **TRUE**, uniformly on compact time intervals — and **Trotter–Kato is necessary but not sufficient**

### The proof (unconditional; this is the adjudication)

Both generators split additively under compression: `h_n(t) = h_{0,n} + M_n(t)` with `M_n(t) := Q_n M_c(t)Q_n`, `||M_n(t)|| ≤ ||M_c(t)|| ≤ C_T` **uniformly in n** (compression is a contraction — this is the free stability estimate).

Both propagators satisfy Duhamel integral equations *against their own free groups*, with **no domain hypotheses whatever** (put `W(t,s)` = Dyson solution of `∂_t W = -i e^{ith₀}M_c(t)e^{-ith₀}W`, `U := e^{-ith₀}W e^{ish₀}`; the series converges in operator norm, term `k` bounded by `(C_T|t-s|)^k/k!`):
```
U(t,s)   = e^{-i(t-s)h₀}   - i∫_s^t e^{-i(t-τ)h₀}   M_c(τ) U(τ,s) dτ,
U_n(t,s) = e^{-i(t-s)h_{0,n}} - i∫_s^t e^{-i(t-τ)h_{0,n}} M_n(τ) U_n(τ,s) dτ.
```
Subtract, splitting the integrand three ways:
```
e^{-i(t-τ)h_{0,n}} M_n(τ)[U_n - U](τ,s)ψ            → ≤ C_T ||D_n(τ,s)ψ||
e^{-i(t-τ)h_{0,n}}[M_n(τ) - M_c(τ)]U(τ,s)ψ         → uniformly small
[e^{-i(t-τ)h_{0,n}} - e^{-i(t-τ)h₀}] M_c(τ)U(τ,s)ψ → uniformly small
```
so with `D_n(t,s)ψ := (U_n - U)(t,s)ψ`,
```
||D_n(t,s)ψ|| ≤ ε_n(T) + C_T |∫_s^t ||D_n(τ,s)ψ|| dτ|,  hence  sup_{|t|,|s|≤T}||D_n(t,s)ψ|| ≤ ε_n(T) e^{2C_T T}
```
by Grönwall, where
```
ε_n(T) = sup_{|σ|≤2T}||(e^{-iσh_{0,n}} - e^{-iσh₀})ψ||
       + 2T sup_{τ,s}||(M_n(τ) - M_c(τ))U(τ,s)ψ||
       + 2T sup_{σ,τ,s}||(e^{-iσh_{0,n}} - e^{-iσh₀})M_c(τ)U(τ,s)ψ||.
```
`ε_n(T) → 0` because: (a) `h_{0,n} → h₀` in SRC by (3), so by **Trotter–Kato** (RS I, VIII.21) `e^{-iσh_{0,n}} → e^{-iσh₀}` strongly, uniformly for `σ` in compacts; (b) `K₁ = {U(τ,s)ψ}` and `K₂ = {M_c(τ)U(τ,s)ψ}` over `[-T,T]²` are **compact** in `H` (continuous images of a compact square), and strong convergence of a uniformly bounded family is uniform on compact sets of vectors; (c) item (4) with the same compactness upgrade. ∎

Note: **no density step is needed** — this holds for every `ψ ∈ H` directly.

**What this proof never touches:** `D(h₀)`, invariance of `H¹` or `B¹` under `U(t,s)`, `∇_x b_D`, `inf r(t) > 0`, differentiability in `t`, smoothness of the profile, compactness of `M_c`. The generator difference is never applied to anything; only the *bounded* difference `M_n - M_c` is, and the free groups are compared separately.

### Is it Trotter–Kato?

**No — not as posed, and the four `PROVABLE_BY_TROTTER_KATO` labels overstate it.** The form quoted in the question (SRC + common core ⟹ uniform strong convergence of the associated unitaries) is a **one-parameter-group** theorem. There is no group here, and there is **no** time-dependent theorem with `(3)+(4)` as hypotheses: pointwise-in-`t` strong resolvent convergence does not imply propagator convergence. Anyone writing "(3)+(4)+Trotter–Kato ⟹ (5)" as a citation has not proved (5).

The honest accounting: Trotter–Kato is used, once, essentially, and irreplaceably — on the **time-independent** compressed free generator, to convert (3) into `e^{-iσ h_{0,n}} → e^{-iσ h₀}` locally uniformly. The bridge to the time-dependent propagators is Duhamel + Grönwall, elementary *precisely because* `M_c(t)` is bounded and its compressions are uniformly bounded in `n` and `t`. That half-page is short but not omissible.

The correct citable statement is a lemma one should write down explicitly:

> **Lemma.** `A_n → A` in SRC (self-adjoint); `B_n(t), B(t)` bounded self-adjoint, strongly continuous in `t`, `sup_{n,|t|≤T}||B_n(t)|| < ∞`, and `B_n(t)φ → B(t)φ` uniformly for `|t| ≤ T` and `φ` in compact sets. Then the propagators of `A_n + B_n(t)` converge to that of `A + B(t)` strongly, uniformly on compact time intervals.

Verdict label for (5): **TRUE — by Trotter–Kato on the free part plus a bounded-perturbation Duhamel/Grönwall step.** Not "by Trotter–Kato" simpliciter; not "not by Trotter–Kato" either (refute-3 goes too far the other way — TK does the only non-elementary work).

Kato's evolution-family approximation theorem (Kato 1970; Pazy Ch. 5; Ethier–Kurtz 4.8) *is* available under the smooth-cutoff reading with `Y = B¹`, but it demands strictly more (`Y`-invariance of `U`, and `n`-uniform `Y`-stability of `U_n` — the latter never checked by prove-3, though it does follow from `[Q_n, N^{1/2}] = 0`). It is the wrong instrument: more hypotheses, same conclusion.

### Ruling on the claimed fork (prove-3, refute-3)

Both flagged that if `1_{|x|≤r(t)}` genuinely truncates a nonvanishing profile, then `[∂_j, M_c(t)]` is a surface measure, `U(t,s)` does not preserve `H¹`, the Duhamel integrand `||[h_n(τ)-h(τ)]U(τ,s)ψ||` is `+∞`, and (5) becomes `DELICATE_UNRESOLVED`.

**This is an obstruction to one technique, not to the proposition.** The Duhamel-through-the-full-generators route dies; the Duhamel-through-the-free-groups route above is untouched, because it never applies `h₀` to a propagated state. refute-3's own 1-D example (`h₀ = -i∂_x`, `V = 1_{x≤t}`, phase a genuine step function) proves only that `H¹` is not invariant — true and irrelevant to a statement about strong convergence in `H`. The `∫ r(σ)^{-2}dσ < ∞` and `inf r > 0` caveats are artifacts of the same route. **(5) is unconditional on the cutoff reading.** Both cross-examiners reached this; the Grönwall route is simpler than the weak-compactness/Radon–Riesz route refute-3's cross-examiner used and gives the same conclusion.

(Caveat of phrasing, not substance: under a genuinely sharp cutoff `U(t,s)` is the unique *mild* solution — the unique strongly continuous unitary family solving the Duhamel integral equation. Calling it "generated by `h(t)`" is then a mild abuse. Under the flat-profile reading `M_c(t)` is a `C_c^∞` multiplier, `H¹` is invariant, and `U` is a genuine strong solution.)

---

## 4. THE COMPRESSION-DOMAIN QUESTION: **not an obstruction**

Both readings are legitimate objects and they are **exactly** related:
```
h_n(t) = Q_n h(t) Q_n on H  is bounded self-adjoint, block diagonal = h̃_n(t) ⊕ 0,
so   U_n^H(t,s) = Ũ_n(t,s)Q_n + (I - Q_n),
and  U_n^H(t,s)ψ - Ũ_n(t,s)Q_nψ = (I - Q_n)ψ,
```
which is **independent of `(t,s)`** and `→ 0` for each fixed `ψ`. So the two readings give the same answer to (5), with the same uniformity. The variable-space (Kurtz / Ito–Kappel) formulation with `P_n = Q_n`, `J_n = ι` reduces to the same thing.

**Which is correct:** reading on all of `H`. It is the only one under which proposition (3) parses at all (`S ⊄ Q_nH`; "common core" is a category error otherwise), it makes `h_n(t)` bounded self-adjoint so RS VIII.25(a) applies verbatim, and it makes `U_n` unitary on `H`, supplying the `t`-independent bound `||U_n - U|| ≤ 2`. Reading on `Q_nH` is the computationally natural object and is equivalent in the strong topology — but that equivalence is a lemma (block diagonality of `Q_n h Q_n`), not a convention.

**Where the choice does matter, and it is not (5):**
- On `H`, `0` is an eigenvalue of `h_n(t)` of **infinite multiplicity**; on `Q_nH` there is no such artifact. Genuine spectral pollution, present only in the first reading.
- Norm resolvent convergence, norm propagator convergence, and spectral convergence fail in both readings, permanently. `U_n^H = I` on `(I-Q_n)H` while `U(t,s)` rotates high-frequency packets by `O(1)`, so `||U_n(t,s) - U(t,s)|| ↛ 0` for `t ≠ s`.

The refutation assigned to this angle (refute-2) is correct that `(h_n - z)^{-1}ψ = (h̃_n - z)^{-1}Q_nψ - z^{-1}(I-Q_n)ψ`, but the offending term has norm `|z|^{-1}||(I-Q_n)ψ|| → 0` pointwise, and in the VIII.25(a) proof the resolvent is only ever applied to `(h - h_n)φ`, already `o(1)`. The kernel is never probed. **The attack fails.**

---

## 5. THE UNIFORMITY CLAUSE: **free, not an extra hypothesis**

Two independent mechanisms deliver it:
1. Trotter–Kato's own local-uniformity clause. (This does need proof, and is asserted without one in several answers; the proof is: `t ↦ e^{itA_n}(A_n+i)^{-1}χ` is equi-Lipschitz with constant `2||χ||` since `||A_n(A_n+i)^{-1}χ|| = ||(I - i(A_n+i)^{-1})χ|| ≤ 2||χ||`; equi-Lipschitz + pointwise convergence ⟹ uniform on compacts; then `||e^{itA_n} - e^{itA}|| ≤ 2` and density of `D(A)`.)
2. In the Grönwall step the suprema over `(t,s) ∈ [-T,T]²` are taken **before** the limit in `n`, and the Duhamel bound is monotone in the time interval. No Arzelà–Ascoli on `{U_n}` is needed — refute-3's opening objection (that `||Q_n h₀ Q_n|| ≍ n^{1/6} → ∞` destroys equicontinuity) is correct as stated and irrelevant, because equicontinuity of the approximating *flows* is never used.

Both `t` and `s` are covered. Two things the uniformity is **not**: uniform in `T` (the constant `e^{2C_T T}` and the free-group convergence both degrade), and uniform in `ψ` (that is norm convergence, permanently false).

---

## 6. THE SINGLE DECISIVE POINT

> **`||h₀(I - Q_n)ψ|| → 0` on a core** — i.e. `Q_n → I` in the *graph norm of `h₀`* on `D(N^{1/2})` — which holds for exactly two reasons: `Q_n` commutes with `N^{1/2}` (Hermite functions are `N`-eigenfunctions), and `h₀² = -Δ ≤ N` so `||h₀u|| ≤ ||N^{1/2}u||`.

Two lines. Everything else is trivial (item 4) or standard machinery (VIII.25(a) → VIII.21 → Grönwall). This is where a counterexample lives: replace the Hermite family by a nested finite-rank family not diagonal in an operator dominating `h₀`, and (3) fails, SRC fails, and (5) goes with it — **while (1), (2) and (4) survive untouched, so the failure is silent**. Galerkin approximation of Dirac operators is the canonical setting for exactly this pathology (Dolbeault–Esteban–Séré; Lewin–Séré).

Runner-up, decisive for the *label* rather than the truth: **`M_c(t)` is bounded, and `||Q_n M_c(t) Q_n|| ≤ ||M_c(t)||`.** This `n`-uniform stability is what a time-dependent Trotter–Kato theorem would have to assume, and here it is free. It is also, per the problem statement, exactly the property (bounded but non-compact) that kills the smooth-to-sharp norm theorem. Boundedness-without-compactness kills the norm theorem and simultaneously saves the time-dependent step.

---

## 7. CONFIDENCE, AND WHAT WOULD CHANGE THE ANSWER

**High** on all of: (3) TRUE, (4) TRUE, (5) TRUE with the uniformity clause, compression-domain question inert, cutoff fork spurious. Each was verified independently above rather than accepted from any attempt.

**High** on the label ruling as well: the quoted time-dependent Trotter–Kato statement is not a theorem, and the gap is real though cheap to close.

What would flip it:
- **Different Galerkin basis** (not spectrally adapted to a scale dominating `h₀`): (3) fails, (5) fails. This is the live risk in any downstream reuse.
- **Unbounded perturbation** (Coulomb tail, unbounded profile): `C_T` and the `n`-uniform Dyson majorant are lost, Grönwall collapses, and one genuinely needs a checked time-dependent Trotter–Kato. I would then report **OPEN**.
- **`t ↦ M_c(t)` only strongly measurable**: (4) in its uniform-in-`t` form becomes false as stated; (5) survives (dominated convergence in `τ`, plus an equicontinuity-in-`s` argument from the Dyson bounds), but the write-up changes.
- **Nothing about the sharp cutoff, `∇_x b_D`, `inf r(t)`, the Gevrey class, or the non-compactness of `M_c`** would change any verdict. Those are all red herrings for (3)–(5).

Two minor errors in the record, corrected for the file: the cross-examination of prove-1 claims `e^{-ish₀}` does not preserve `S(R³)⊗C⁴` because the symbol is non-smooth at `ξ=0`. **False** — `e^{isα·ξ} = cos(s|ξ|)I + i sin(s|ξ|)(α·ξ)/|ξ|`, and both `cos(s|ξ|)` and `sin(s|ξ|)/|ξ|` are entire functions of `|ξ|²`. The free Dirac group preserves `S` and preserves `B¹` with linear growth (`e^{ish₀}x_j e^{-ish₀} = x_j + ∫_0^s α_j(τ)dτ`). And refute-2's assertion that `0` is not an eigenvalue of `h(t)` is unsupported (zero modes of massless Dirac with a bounded compactly supported potential are not excluded); the spectral-pollution point stands on the infinite degeneracy of `ker h_n` alone.

**Constraints on downstream use** (all six agree, and they are correct): (3)–(5) certify **dynamics in the strong topology only**. No norm convergence of anything, ever. **No rate** — the proof is `3ε`/compactness end to end and produces no modulus in `n`; any claim of `O(n^{-a})` uniform over states is unsupported by (3)–(5). **No spectral conclusion** — SRC forbids spectral loss but permits pollution, and the `⊕0` reading manufactures an infinite-multiplicity eigenvalue at `0`.