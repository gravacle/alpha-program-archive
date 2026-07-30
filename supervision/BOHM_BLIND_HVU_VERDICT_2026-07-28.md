# BLIND VERDICT — H-VU: IS THE CONTINUED FAMILY UNIFORMLY BOUNDED IN n? (Bohm, 2026-07-28)

Six independent agents (3 prove, 2 refute, 1 ill-posedness sceptic), each cross-examined, then
adjudicated. NO corpus access; posed as self-contained functional analysis. None knew what turned on
the answer. H-VU was named by the construction lane, so it could not take this question.

---

# ADJUDICATION

**Unanimous across all six attempts and all six cross-examinations: FINITE.** I verified the mathematics independently rather than counting votes, and it holds. There is no dissent to arbitrate — the interesting work is in correcting the specific reasons given, several of which are wrong, and in locating the one question that *is* open (which is not the one asked).

---

## 1. IS sup_n sup_polydisc ||V_n(a)|| FINITE?

**YES.** Sharp form:

    sup_n ||V_n(a_-,a_+)||  <=  exp( (|Im a_-| + |Im a_+|) * C_J ),    C_J := Int_J ||M_c(t)|| dt

hence `<= exp(2 eps C_J)`, with `n` nowhere in the constant. Two refinements over "exp(2 eps ||M_c|| T)": only the **imaginary** parts enter (so the bound returns exactly 1 on the real slice, as it must), and only the **L^1-in-time** norm of the profile enters. The identical bound holds for the uncompressed `V(a_-,a_+)`.

A second, independent bound that no attempt produced and that is strictly stronger near the diagonal — differentiate `V = u_-^{-1}u_+` directly:

    V' = -i(a_+ - a_-) [ u_-(t)^{-1} N_n(t) u_-(t) ] V,   N_n = Q_n M_c Q_n

so `||V_n(a_-,a_+) - I|| <= exp(|a_+ - a_-| * C_J * e^{2 eps C_J}) - 1`, uniformly in n, **valid on the closed polydisc**. This supersedes the Schwarz-lemma corollaries offered by prove-3 and illposed-sceptic, whose admissible radius degenerates at the boundary (their cross-examiners were right to flag it). It also makes `V_n(a,a) = I` and the equi-Lipschitz/equi-analyticity of the family explicit with a computable constant.

## 2. THE CRUX

**Yes, it goes through uniformly in n. The argument sketched in (b) is correct and the worry is unfounded. Say so plainly.** Three lines:

Write `a = a_R + i a_I` and `G_n(t,a) = A_n(t) + i a_I N_n(t)`, with `A_n = Q_n h_0 Q_n + a_R N_n` self-adjoint (legitimate: `ran Q_n ⊂ Schwartz ⊂ D(h_0)`, so `Q_n h_0 Q_n` is finite-rank symmetric hence bounded self-adjoint) and `N_n = Q_n M_c(t) Q_n` self-adjoint. For `f(t) = ||u_n(a,t,s)psi||^2`,

    f' = 2 Re< phi, -i A_n phi >  +  2 a_I < phi, N_n phi >,   phi = u_n psi.

**The first term is identically zero**, because `<phi, A_n phi>` is real for *any* self-adjoint `A_n` irrespective of its norm. Gronwall (forward and backward, so the inverse obeys the same bound) gives the estimate above. The single uniformity input is `||Q_n M_c Q_n|| <= ||M_c||`, exact for any orthogonal projector.

`||Q_n h_0 Q_n|| ~ n^theta` never appears: it lives entirely inside a factor that is **exactly unitary for every n**. A large self-adjoint generator makes the compressed free flow oscillate fast; it does not make it grow. This is Lumer–Phillips / the Dahlquist logarithmic-norm bound `||e^{-i(A+iB)t}|| <= e^{t||B||}`, which is indifferent to `||A||` — including `||A|| = infinity`, so it covers the uncompressed propagator verbatim.

**Corrections to the attempts on this point:**

- **prove-2's diagnosis "the SERIES form of Duhamel fails, the DIFFERENTIAL form works" is FALSE**, and its cross-examiner is right. The Dyson series expanded about the free compressed **unitary** group has k-th term bounded by `(|a| C_J)^k / k!` — already n-free, no Gronwall needed. The real dichotomy is *which reference dynamics you expand about*: the identity (fatal, gives `exp(T||G_n||)`) versus the free compressed group (fine). The differential form's only gain is the exponent `|Im a|` in place of `|a|`.
- **prove-2's "stiffness suppresses growth / the bound is never approached" is an artifact of random-matrix numerics.** The bound is saturated when `[h_0, M_c] = 0`. There is a real effect underneath — as `n` grows the eigenvectors of `A_n` delocalize, so `<phi_j, M_c phi_j>` shrinks and the true growth rate falls below the bound — but that is a statement about the true rate, not a proved improvement, and it should not be presented as one.
- **prove-3's (f)(1) claim that free-factor cancellation would save the product even if `a` entered `h_0` is FALSE** and contradicts its own (d): the free factors are then `a`-dependent and leave `exp(-i(a_+-a_-)T Q_n h_0 Q_n)`, which diverges. **prove-3's (d) claim that an *uncompressed* perturbation would be an obstruction is also FALSE**: the numerical-range argument is indifferent to sandwiching, since `Q_n h_0 Q_n + Re(a) M_c` is still self-adjoint. Its failure-mode triage is unreliable in both directions and should not be reused as a checklist.

The correct one-line criterion: **uniformity holds iff `Im a` multiplies only operators whose compressions are norm-bounded uniformly in n.**

## 3. THE ADJOINT-CONTINUATION GAP

**Technicality, and a fully closed one.** `G_n(t,a)^dagger = G_n(t,abar)` (because `a` multiplies a self-adjoint coefficient), from which `u_n(t,s;a)^dagger = u_n(s,t;abar) = u_n(t,s;abar)^{-1}` by ODE uniqueness. So `a -> u_n(a)^dagger` is anti-holomorphic and is not the object being continued; the unique analytic continuation from the real slice is the **inverse/backward propagator**:

    V_n(a_-,a_+) = u_n(a_-)^{-1} u_n(a_+) = ( u_n(abar_-) )^dagger u_n(a_+).

"Continuing the dagger" and "daggering the continuation" differ **exactly** by `a -> abar`. The decisive observation, which makes this convention-proof: `||X^dagger|| = ||X||` and `|abar| = |a|`, so **both** candidate readings obey the same bound. The convention affects **analyticity in a_-** — and hence whether Cauchy/Vitali machinery is available at all — but it cannot affect a norm bound. No norm question can be sensitive to it. refute-2 attacked precisely here (non-normality of the compressed generator, whose departure from normality genuinely does diverge in n) and its attack correctly died: non-normality inflates the gap between spectral and numerical abscissa, and the estimate used is a *numerical*-abscissa estimate, blind to it by construction. The condition-number version of the attack (`||u_n^{-1}||` blowing up while `||u_n||` stays bounded) is closed by the *lower* half of the Gronwall estimate, which is the load-bearing half and which several attempts stated only in passing.

## 4. eps-DEPENDENCE

**No threshold. The answer is qualitatively eps-independent.** The family is entire in `a` (affine, bounded coefficient), and `exp(2 eps C_J)` is finite for every `eps > 0`; `eps` enters only as a linear factor in an exponent. The dichotomy is eps-free in *both* directions: the failure mechanisms of item 6 fail for every `eps > 0` as well. Any argument in this problem that produces a critical `eps_0` should be treated as suspect.

One genuine exception, which prove-1's cross-examiner alone identified correctly: affineness is not what matters — **uniform boundedness of the complexified direction** is. Any holomorphic family `a -> M_c(t,a)` with `sup_{|a|<=eps,t} ||M_c(t,a)|| < infinity` gives the same bound. So an `eps_0` *can* appear if `a` deforms the profile (a complex translation/dilation of a non-Gaussian-tailed profile stays entire but loses uniform boundedness at finite radius). That is a boundedness failure, not an analyticity failure, and it is the only route to a threshold.

## 5. THE WEAKER HYPOTHESIS

First, disambiguate the premise. **Banach–Steinhaus applies pointwise in `a`**: strong convergence of `V_n(a)` on all of H at a given `a` *forces* `sup_n ||V_n(a)|| < infinity` at that `a`. Several attempts overstated this as making the *joint* sup over the polydisc necessary; it does not. A family can have finite sup at every `a` and infinite joint sup. But the pointwise version already means: **if the sup fails at `a`, no weakening of hypotheses rescues strong convergence at `a` on all of H — one must weaken the conclusion.**

Dense convergence alone is genuinely insufficient, even with norm convergence of the other factor: `A_n = n<.,e_n>e_1` (→ 0 on the dense span, `||A_n|| = n`), `B_n = I + n^{-1/2}<.,e_1>e_n` (→ I in **operator norm**), yet `A_nB_n e_1 = sqrt(n) e_1`.

Three genuinely weaker sufficient conditions, in order of usefulness here:

1. **Bound the product, not the factors:** `sup_n ||A_nB_n|| < infinity` plus dense convergence. This is the right formulation for this problem, because `V_n` *is* the product and the estimate bounds it directly.
2. **Rate-beats-growth:** `||A_n|| * ||(B_n - B)psi|| -> 0` plus `A_n(B psi)` convergent. Available on Schwartz vectors in a Hermite scheme, but refute-2's cross-examiner is right that it is oversold: the relevant error is the *Galerkin propagator* error, not the projection error, and Hermite (position-weighted) approximation degrades under a free Dirac flow that transports support outward at speed 1. Do not lean on it.
3. **Uniform boundedness in a scale** `X -> H` with `X` a Hermite–Sobolev space: gives convergence with loss of derivatives, i.e. matrix elements on a fixed core, not an H-bounded limit.

Here none is needed, and the payoff of the true bound is the upgrade: **local boundedness on the polydisc plus strong convergence on the real slice implies locally uniform strong convergence on the whole open polydisc**, with n-uniform Cauchy estimates on every Taylor coefficient. Two corrections that every attempt needed:

- **The several-variables Vitali as stated by all six is false.** "Convergence on a set with an accumulation point" does not suffice for `N >= 2` (`f_n(z,w) = w` for even n, `0` for odd n: locally bounded, holomorphic, converges on the complex line `{w=0}`, diverges elsewhere). The conclusion survives for the right reason — `R^N` is **non-pluripolar** in `C^N` — but the clean repair is to iterate the **one-variable** Vitali one parameter at a time over the totally real slice.
- **Matrix-element Vitali gives only weak convergence.** For H-norm convergence use the vector-valued Vitali (Arendt–Nikolski; the Lagrange-interpolation-with-Cauchy-remainder proof transfers to Banach targets, the Montel proof does not), or apply the two-constants theorem to the subharmonic `||V_n(a)psi - V_m(a)psi||`.

The real-slice input is real, not assumed: `-i alpha.grad` maps each Hermite function into a finite combination of neighbouring-degree ones, they are Nelson analytic vectors, so the Hermite span is a **core**; `Q_n h_0 Q_n psi = Q_n h_0 psi -> h_0 psi` on it, Reed–Simon VIII.25(a) gives strong resolvent convergence, Trotter–Kato gives the free groups, the interaction picture carries the bounded perturbation. (`Q_n` does commute with the number operator despite degenerate 3-D levels, since each Hermite function is individually an eigenvector — cutting a level mid-way is harmless.) Spectral pollution, endemic to Dirac Galerkin schemes, is compatible with all of this and touches no propagator statement — but it would bite any downstream claim about eigenvalues or spectral projections, where the numerical-range argument gives nothing and the non-normality of item 3 genuinely does matter.

Also strike from the record the routine citation of **Kato's stable-family theorem** for the uncompressed complexified propagator: its constant-domain hypotheses effectively require `[h_0, M_c]` bounded, i.e. `M_c` Lipschitz, which is not granted. The two-stage interaction-picture Dyson construction needs only boundedness, strong measurability, and local integrability in `t`.

## 6. DECISIVE POINT, CONFIDENCE, AND WHAT WOULD CHANGE IT

**Decisive point.** `<phi, A phi>` is real for self-adjoint `A` *regardless of `||A||`*. The one divergent quantity in the problem sits entirely inside the self-adjoint part of the compressed generator and contributes **exactly zero** to `d/dt ||u_n psi||^2`. Uniformity in n then rests on the single exact inequality `||Q_n M_c Q_n|| <= ||M_c||`. The feared `exp(2 eps T ||G_n||)` is not a symptom of a real difficulty; it is simply the wrong estimate — it bounds the whole generator instead of splitting off its self-adjoint part.

Worth recording why the question nonetheless deserved to be asked: `log ||V_n(a)||` is plurisubharmonic, the real slice is a totally real interior submanifold, and the maximum principle propagates from the distinguished boundary *inward*, not from a real slice *outward*. So "unitary on the real slice" carries, by itself, **zero** information off it — witness `e^{-i lambda_n a}`. Any proof resting on real-slice unitarity plus analyticity is fallacious. The differential estimate is genuinely required. prove-2's Part 1 established this cleanly and it is the most valuable negative result in the set.

**Confidence: very high.** The proof is three elementary lines, I verified each independently, all six independent attempts (including two assigned to refute and one to show ill-posedness) converged, and all six adversarial cross-examinations failed to break it.

**What would flip it to NO:**

1. **`a` reaching `h_0` in any disguise** — complex dilation/boost/rotation, complex mass, complex time or time-reparametrization, or an `a`-dependent support radius `r(t)` implemented as a complex translation. Then the anti-self-adjoint part has norm `~ eps ||Q_n h_0 Q_n|| ~ n^theta` and `sup_n = infinity` at rate `exp(c eps T n^theta)`, for every `eps > 0`. Worse, the limit object would not exist: `spec(h_0) = R` (masslessness) means no semiboundedness, no sector, no Hille–Yosida rescue in either time direction. **This is the single switch, and it is a fact about the source construction that a self-contained statement cannot certify.** Report the verdict as "YES given that `a` enters only through a term uniformly bounded on the polydisc."
2. **An oblique projector** (Petrov–Galerkin, collocation, interpolation, non-orthonormal basis) in place of `Q_n`. Then `P_n h_0 P_n` is not symmetric, its skew part is of size `||h_0 P_n||`, and stability is lost **already at real `a`**. Verify that the truncation is a two-sided orthogonal compression.
3. **A resolvent, Born series, spectral projection, or Fredholm determinant** substituted for the propagator. illposed-sceptic's Abel–Liouville argument (`det v_n = exp(-i Int tr b_n) != 0` for all complex `a`) is what rules out migrating truncation-dependent singularities, and it is specific to propagators. Insert an inverse of anything other than the flow itself and the migrating-singularity worry becomes live again.

**And the one thing that is genuinely open, which is not the question asked.** The constant is `exp(2 eps C_J)` with `C_J = Int_J ||M_c(t)||dt`: uniform in n at **fixed T**, and *not* uniform in T. The framing — a profile supported in a ball of radius `r(t)`, an in/out parameter pair `(a_-, a_+)`, boundedness assumed only "on compact intervals" — reads like a `T -> infinity` scattering object. If so:

- **The two limits do not commute, and the truncation is exactly what breaks the good one.** At fixed n, `Q_n h_0 Q_n` has finite rank, hence pure point spectrum, hence no dispersion and no local decay. For time-independent `M_c >= 0`, first-order perturbation gives spectral abscissa `~ eps max_j <phi_j, M_c phi_j> > 0` for every n (a nonzero finite Hermite combination cannot vanish on the ball, being polynomial times a Gaussian), so `sup_T ||u_n(i eps)|| = infinity` at every fixed n. Therefore `sup_n sup_T` is infinite for trivial reasons, while `sup_n` at each fixed `T` is finite. Any construction needing `T -> infinity` **must** take `n -> infinity` first, or use a `T`-window chosen independently of n.
- The only routes to a `T`-uniform bound are `Int_0^infinity ||M_c(t)||dt < infinity` (adiabatic or `L^1` switching), or a Kato-smoothness / local-decay estimate for the pair `(h_0, M_c)` — and that route must survive the non-unitary deformation, where transporting local decay costs a factor `exp(eps C_J)`, i.e. is circular precisely when `C_J = infinity`. Note also that the polydisc contains both signs of `Im a`, so it includes the anti-damped direction, where even the limit object generically grows.

So: **the Galerkin index is exonerated; the time horizon is where the work is.** If anything downstream is fragile, look at `T`, never at `n`.