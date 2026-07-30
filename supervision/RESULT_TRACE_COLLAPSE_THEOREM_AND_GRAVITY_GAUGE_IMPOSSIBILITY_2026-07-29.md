# RESULT — THE TRACE COLLAPSE THEOREM, AND AN IMPOSSIBILITY PROOF FOR DEPTH-INDEPENDENT GRAVITY/GAUGE RATIOS

Derived and adversarially attacked 2026-07-29 at the reviewer lane's order. All arithmetic exact
rational (`Fraction`). No coupling, depth, scale, or coefficient value was evaluated. Nothing was
compared to a measured constant.

## 1. THE THEOREM (verified; stronger than the form previously stated)

Let `X, Y in gl(N,C)` with AT LEAST ONE traceless. For the derivation action on `Lambda^k(C^N)`:

```
Tr_{Lambda^k}(XY) = C(N-2, k-1) * Tr_fund(XY)          [one traceless]
Tr_{Lambda^k}(XY) = C(N-2, k-1) * Tr_fund(XY) + C(N-2, k-2) * (Tr X)(Tr Y)     [general]
```

PROOF SKETCH. `Lambda^k` weights are `x_S = sum_{i in S} x_i` over k-subsets. Counting
multiplicities `C(N-1,k-1)` for a fixed index and `C(N-2,k-2)` for a fixed ordered pair, then
Pascal (`C(N-1,k-1) - C(N-2,k-2) = C(N-2,k-1)`), gives the two-term form directly.

HYPOTHESES CHECKED IN BOTH DIRECTIONS:
- CARTAN IS NOT REQUIRED. `(X,Y) |-> Tr_{Lambda^k}(dX dY)` is a `GL(N)`-invariant symmetric
  bilinear form on `gl(N)`. Since `gl(N) = sl(N) + center` with `sl(N)` adjoint-irreducible,
  Schur gives a 2-dimensional space of such forms spanned by `Tr(XY)` and `(Tr X)(Tr Y)`. The
  identity therefore holds for ALL `X,Y`, non-commuting included. Verified the hard way by
  building full derivation matrices for generic non-commuting rational traceless `X,Y` at
  `N = 3,4,5,6`, every `k`: exact match every case.
- DUALISATION IS IRRELEVANT. `Tr_{R*}(XY) = Tr((-X^T)(-Y^T)) = Tr(XY)`. The corpus's
  `Lambda^4 ~ 5bar` labelling has no effect.
- SANITY: palindromic (`C(N-2,k-1) = C(N-2,N-k-1)`, matching `Lambda^k ~ (Lambda^{N-k})*`);
  vanishes at `k = 0, N`; sums to `2^{N-2}`, split evenly between even and odd degrees
  (verified `N = 2..9`).

At `N = 5`, `k in {0,2,4}`: `C(3,-1) = 0`, `C(3,1) = 3`, `C(3,3) = 1`. Hence
`K_XY(x) = Tr_fund(XY) * S(x)` with `S(x) = [I_1(x + 12/5) + 3 I_1(x + 18/5)] / (24 pi^2)`.

## 2. THE RATIOS — CONFIRMED EXACT, AND THEY REDUCE FURTHER

`Tr_fund(Q^2) = 4/3`, `Tr_fund(H^2) = 2`, `Tr_fund(QH) = 4/3`; ratios exactly `3/2` and `1`.
Per-block traces `(0,0,0)` / `(4,6,4)` / `(4/3,2,4/3)`, carrier totals `16/3, 8, 16/3` —
character-for-character the executable grouping at
`reports/alpha_br_common_induced_coefficients_v001.md:7`, including the
`C2 = 12/5 <-> dim 5` and `C2 = 18/5 <-> dim 10` assignment. AGREEMENT IS EXACT.

TWO REDUCTIONS THE CORPUS HAS THE INGREDIENTS FOR BUT NEVER ASSEMBLES. With `H = Q + C`,
`C = diag(1/3,1/3,-2/3,0,0)` the color-center cocharacter:
- `Tr(QC) = 0`, so **`K_QH = K_Q` IS EXACTLY THE TRACE-ORTHOGONALITY OF `C` TO `Q`**.
- `Tr(C^2)/Tr(Q^2) = 1/2`, so **`K_H/K_Q = 1 + Tr(C^2)/Tr(Q^2) = 3/2`**.
Both are properties of a single 2-plane in the weight lattice.

Separately: `K_Q = (8/3) K_5` is NOT representation theory. It compares `q2/(24 pi^2)` with
`(8/3) q2/(64 pi^2)`, i.e. asserts `1/24 = 8/192`. Identical expressions.

## 3. NOVELTY REFUTED — THIS ALREADY EXISTS IN THREE LAYERS

The claim that the collapse "has not been stated in the corpus" IS FALSE.

- **As executable code, general-N**: `scripts/derive_alpha_boundary_chiral_spectrum_v001.py:25-27`
  defines `dynkin_index(n,k) = Fraction(math.comb(n-2, k-1), 2)`. That IS `C(N-2,k-1)`. Only
  occurrence of that binomial in the trees; never stated in prose; only ever called at `N = 5`.
  `results/alpha_boundary_chiral_spectrum_v001.csv` tabulates `T = 1/2, 3/2, 3/2, 1/2` for
  `Lambda^1..Lambda^4` — the `1:3:3:1` ratios. `Lambda^0` is omitted, so `index = 0` is not in it.
- **In the supervision layer, yesterday**: `BOHM_SLOT9_THEORY_ATTACK_2026-07-29.md:38-52` gives
  the identity, the `K_XY = Tr_5(XY) S(x)` form with the same `S(x)`, the x-independence
  statement, and the `8/3` arithmetic catch. Line 38 calls it "not stated in the corpus and
  load-bearing" — that self-assessment was wrong on the first half.
- **The protection question was already adjudicated**:
  `STAGE8_SCHUR_RATIO_PROTECTION_SCOPE_ATTACK_V001.md` records
  `schur_arithmetic_recomputed_here = false`, verdict
  `CONDITIONAL_ON_FULL_SU5_INVARIANT_DEFORMATION_CLASS_AND_TRANSPORT`.
- **The collapsed one-function form is in the parent ledger**:
  `alpha_strict_route_decision_ledger_v001.csv:125` — "the induced parent coupling depends only
  on `W_ch = N_g[(1/3)E1(x_5bar) + E1(x_10)]`", weights `1/3 : 1` = `1 : 3` normalised, index
  weighting already factored. `reports/alpha_superconnection_finite_mass_spectrum_v001.md:22`
  writes `W_ch = N_index (4/3) E1(r^2/k_R^2)` with `4/3 = Tr_fund(Q^2)` pulled out explicitly.

REVIEWER FINDING ON PROCESS: the reviewer lane lost its OWN result within 24 hours and ordered a
re-derivation of it. Same loss class as the deleted rescaling-exclusion section and the 718
uncited root artifacts, at a 1-day timescale inside the supervision layer itself.

## 4. WHAT THE COLLAPSE ACTUALLY REQUIRES (new; sharper than "Casimir grouping")

The invariant-form argument shows the collapse is not about `Lambda^even` at all: for ANY carrier
that is a direct sum of representations of a simple algebra, `Tr_{R_a}(XY) = (index ratio) *
Tr_fund(XY)`. Exterior-power combinatorics only fix the numbers `(0,3,1)`.

TWO HYPOTHESES CAN BREAK:

(a) **TRACELESSNESS.** If a generator is not traceless — e.g. a `U(1)` normalised inside `u(5)`
rather than `su(5)`, which the corpus flags as live ("nor independently remove the extra central
`U(1)`") — the `(Tr X)(Tr Y)` term revives with block weights `(0,1,3)`. There are then TWO
independent scalar functions, not one, and THE RATIOS ACQUIRE x-DEPENDENCE. This hazard is
recorded nowhere.

(b) **BLOCK STRUCTURE — and the first attack on this was wrong.** The collapse does NOT require
Casimir grouping. Writing the condition as: the second-moment tensor `sum_s w_s mu_s (x) mu_s`
must be proportional to the Cartan metric, the admissible weightings form a **7-dimensional
subspace** of the 16-dimensional weighting space (codimension 9 — a real condition, but four
dimensions larger than the 3-dimensional space of degree-class functions). Enumerating all
`2^16` level sets: exactly **27 nonempty admissible subsets**, of which only 7 are unions of
whole `Lambda^k` blocks. The other 20 have index exactly 2 with profiles
`{6 of the 10} + {1 of the 5bar}` or `{4 of the 10} + {4 of the 5bar}`. THE HONEST CRITERION IS
THE SECOND-MOMENT CONDITION, NOT CLASS-FUNCTIONHOOD.

## 5. A LIVE COUNTEREXAMPLE INSIDE THE PROGRAM'S OWN OPERATOR (new)

`derive_alpha_br_homogeneous_operator_pullback_v001.py` builds its operator on
`internal_abs_h_block(flux_degree)` — the carrier decomposed by `|H|`, NOT by Casimir. `|H|` is
not a class function and cuts across the degree blocks: `Lambda^2` splits `4+6`, `Lambda^4`
splits `3+2`. Exact restricted traces:

| block | dim | Tr Q^2 | Tr H^2 | Tr QH | H^2/Q^2 | QH/Q^2 |
|---|---|---|---|---|---|---|
| `|H|=0` | 8 | 4/3 | 0 | 0 | 0 | 0 |
| `|H|=1` | 8 | 4 | 8 | 16/3 | 2 | 4/3 |

NEITHER SECTOR GIVES `(3/2, 1)`. In the `|H|=0` sector `K_H` and `K_QH` VANISH OUTRIGHT. Both
indicator vectors are INADMISSIBLE under the second-moment criterion. So if the induced action is
ever assembled flux-sector by flux-sector with sector-dependent weights — WHICH IS HOW THE
CORPUS'S OWN OPERATOR IS CONSTRUCTED — the collapse fails and the ratios become x-dependent.
This is a concrete instantiation of exactly the caveat
`STAGE8_SCHUR_RATIO_PROTECTION_SCOPE_ATTACK_V001.md` names abstractly as "no independent
per-factor threshold/local corrections below the breaking scale." The cleanroom STATES the
hazard; it does not EXHIBIT it. It is now exhibited with exact numbers.

PRECISION WORTH CARRYING: because the three `I_1(x + c_j)` are linearly independent, the ratios
are x-independent FOR ALL x iff EVERY threshold level set is individually admissible.
Admissibility of the total weighting at one depth is strictly weaker.

WHAT SURVIVED THAT COULD HAVE KILLED IT: the pullback carries `MASS_CHEVALLEY`, an
`su(5)`-breaking Chevalley return map. But `derive_alpha_br_homogeneous_operator_pullback_v001.py:92-94`
asserts `mass^dag mass = 1` on each block, so the mass enters as a UNIFORM SHIFT absorbed into
`x`, not as a splitting. The collapse survives BECAUSE THE RETURN MAP IS UNITARY — a real
hypothesis, not a triviality.

## 6. THE IMPOSSIBILITY PROOF — NO DEPTH-INDEPENDENT GRAVITY/GAUGE RATIO ON THIS CARRIER (new)

Every coefficient in this construction has the form (rational tensor constant) x
`sum_a w_a I_n(x + C2_a)` with `w in {d_a, t_a}`, `d_a = (1,10,5)`, `t_a = (0,3,1)`:

```
C_V           : (d, 3)
C_R (Einstein): (d, 2)
a_4 layer     : (d, 1)     [R^2, Ric^2, Riem^2, C^2, E_4; ratios 5:-8:-7 and -18:11]
K_Q, K_H, K_QH: (t, 1)
```

TWO COEFFICIENTS ARE EXACTLY PROPORTIONAL IFF THEY SHARE BOTH `w` AND `n`. So there are exactly
two maximal mutually-proportional families — the gauge triple and the `a_4` quintuple — and
**NO CROSS-FAMILY RATIO IS x-INDEPENDENT.**

The sharp case is the `a_4` gravitational coefficient, which carries the SAME `I_1` as the gauge
sector, so it fails for a structural reason rather than an index mismatch. Suppose
`a_4^grav(x) = lambda K_Q(x)` on an open interval. Then

```
(1/23040)[ I_1(x) + 5 I_1(x + 12/5) + 10 I_1(x + 18/5) ]
  - lambda (1/18)[ I_1(x + 12/5) + 3 I_1(x + 18/5) ]  ==  0
```

`I_1(x+c) = E_1(x+c)` has a logarithmic branch point at `x = -c` and is analytic elsewhere; the
three shifts `0, 12/5, 18/5` are distinct, so the three functions are LINEARLY INDEPENDENT. The
coefficient of `I_1(x)` must vanish: `1/23040 = 0`. CONTRADICTION. No evaluation at any depth is
involved. (`C_R` fails twice over, carrying `I_2` as well.)

**THE CONTRADICTION LOCALISES ENTIRELY ON `Lambda^0`, AND THAT IS THE STRUCTURAL CONTENT: THE
SINGLET HAS DIMENSION 1 BUT INDEX 0.** The gauge sector is blind to it; every gravitational
coefficient sees it. The sectors are weighted by two LINEARLY INDEPENDENT functionals on the
representation ring — `dim` and `index` (minors of `[d; t]` are `3, 1, -5`). Any construction on
this carrier is therefore FORBIDDEN from producing an x-independent gravity-to-gauge ratio, no
matter how the thresholds are arranged.

BOUNDED NEGATIVE (roots: cleanroom, parent, supervision, external handoffs): NO FILE STATES THIS.
Nearest is `BOHM_SLOT9_THEORY_ATTACK_2026-07-29.md:123`, which sets `d_a` and `Tr_a(Q^2)` side by
side and scopes the collapse "*within* the gauge sector" — but does not say `C_R` fails to
collapse, or why.

### WHAT THIS FORECLOSES, AND WHAT IT DOES NOT

FORECLOSES: any hope that the gravity/gauge ratio is depth-independent the way the gauge/gauge
ratios are. There is no "the depth cancels in the ratio" escape on this carrier. The ratio route
CANNOT produce a number without selecting the depth `x`.

DOES NOT foreclose: the ratio route itself, which already carried `DEPTH_OPEN` on its face. The
result converts an open condition into a PROVEN necessity — depth selection is not a gap to be
filled opportunistically, it is unavoidable.

## 7. THE PARENT-FLUX SADDLE — THE COCHARACTER CHOICE CARRIES ONE RATIONAL NUMBER (new)

`reports/alpha_br_parent_flux_local_saddle_v001.md:8,11` uses
`s(y,x) = C_V y - 2 C_R + K_H/(8y)`; stationarity gives `y = C_R/C_V` and `K_H C_V = 8 C_R^2`.
Substituting the collapse, the metric condition is

```
Tr_fund(X^2) * S(x) * C_V(x) = 8 C_R(x)^2
```

for whichever traceless Cartan direction `X` is used. TWO CONSEQUENCES:
1. `y = C_R/C_V` is COMPLETELY INDEPENDENT of the cocharacter choice.
2. The entire "H versus Q" distinction — which that report's line 15 flags as substantive ("It
   does not replace `H` with electromagnetic `Q`") and line 25 calls "the primitive parent-closing
   sphere cocharacter is kept separate" — enters this saddle through EXACTLY ONE RATIONAL NUMBER,
   `2` versus `4/3`. The `Q` version of the depth equation is the `H` version under the single
   substitution `K_H -> (2/3) K_H`. A whole family of cocharacter choices collapses to a
   one-parameter rational rescaling.

The corpus treats this choice as carrying physical content. AT THE LEVEL OF THESE COEFFICIENTS IT
DOES NOT.

## 8. THREE CONSUMER DEFECTS, ONE IN A SEALED ARTIFACT

(a) **THE PRODUCER GATE IS PARTLY TAUTOLOGICAL.**
`derive_alpha_br_common_induced_coefficients_v001.py:264-273` makes `K_H = 1.5 K_Q` and
`K_QH = K_Q` PASS/FAIL conditions at `2e-14`; `:242-244` does the same for `K_Q = (8/3) K_5`.
Failure flips the run to `FAIL_COMMON_BR_LOCAL_COEFFICIENT_FUNCTIONS`. ALL THREE ARE IDENTITIES
OF THE CONSTRUCTION AND CANNOT FAIL. The
`PASS_COMMON_BR_LOCAL_COEFFICIENT_FUNCTIONS_DEPTH_OPEN` flag is correspondingly weaker than it
reads. THIS IS A THIRD AND FOURTH INSTANCE OF THE CANNOT-FAIL-CHECK CLASS (baseline had 2).

(b) **FOUR SUPERVISION ARTIFACTS CITE THE RATIOS AS EXECUTED DYNAMICAL EVIDENCE.**
`GRAVITY_EVIDENCE_REGISTER_V001_2026-07-29.md:117-119` ("the forced-ratio mechanism has been
EXECUTED in-tree ... numerically asserted to 2e-14 per sampled depth"),
`WHAT_THE_GRAVITY_DISCOVERY_MEANS_2026-07-29.md:29`, `PLAN_TO_ALPHA_V006_2026-07-29.md:99`,
`BOHM_CTP_ABSOLUTE_RESPONSE_ROUTE_SWEEP_2026-07-28.md:246` ("not a hope — it is an executed
in-tree result"). The 2026-07-29 retraction at `CONTINUATION_STATE.md:2347` is SINGLE-SOURCE AND
UNSEALED and those four remain unamended. THE FIRST IS SEALED. An erratum pointer is owed, by the
same append-only mechanism as `ERRATUM_001`.

(c) **TWO UNREGISTERED NAMESPACE COLLISIONS.** `C_R` is registered
(`STAGE8_NAMESPACE_REGISTER_DRAFT_V002.md:86`) — induced Einstein coefficient in the parent,
compactness ratio in the cleanroom (`BID_MINIMAL_PUBLIC_CAUSAL_CELL_DERIVATION_V001.md:43`).
`K_H` is NOT registered and also collides:
`PRIMITIVE_SOURCE_RECORD_CHIRAL_OPERATOR_GATE_V002.md:42` uses `K_H` for a Hermitised Dirac
operator.

## 9. WHAT THE RESULT DOES NOT GIVE

No coupling, no depth, no absolute normalisation. `S(x)` is entirely unconstrained by any of
this, and one unknown function projected three ways is still one unknown function. It does NOT
exclude an additive counterterm — it says only that a counterterm which is itself a full
`su(5)`-invariant symmetric 2-tensor cannot move the ratios, which is the conditional the
cleanroom already recorded and whose antecedent it says is unestablished.

## 10. STATEMENT OF THE THEOREM, FOR THE RECORD

> Let `X, Y in gl(N,C)` with at least one traceless. Then for every `k` the derivation action on
> `Lambda^k(C^N)` satisfies `Tr_{Lambda^k}(XY) = C(N-2,k-1) Tr_fund(XY)`; without tracelessness
> the identity acquires `C(N-2,k-2)(Tr X)(Tr Y)`. Consequently, for any carrier that is a direct
> sum of `su(N)` representations and any spectral threshold assignment whose level sets each
> satisfy the second-moment condition `sum_s w_s mu_s (x) mu_s ~ Cartan metric` — in particular
> any assignment depending only on a Casimir — the induced gauge kinetic coefficients
> `K_XY(x) = sum_a Tr_a(XY) I_1(x + C2_a)/(24 pi^2)` all equal `Tr_fund(XY) S(x)` for a single
> scalar `S`, so every ratio among them is a rational Cartan inner-product ratio independent of
> `x`, of the `I_n`, and of the Casimir offsets. At `N = 5` on `Lambda^even(C^5)` this gives
> `K_H/K_Q = 3/2` and `K_QH/K_Q = 1`, the latter being exactly the trace-orthogonality
> `Tr(QC) = 0` of the color-center cocharacter to `Q`. NO ANALOGOUS RELATION HOLDS BETWEEN THE
> GAUGE AND GRAVITATIONAL SECTORS: those are weighted by `index` and `dim`, linearly independent
> functionals on the representation ring, and the trivial summand `Lambda^0` — dimension 1,
> index 0 — obstructs any x-independent gravity-to-gauge ratio identically.

CARRIED HYPOTHESES: at least one generator traceless; the carrier a genuine representation of the
simple algebra; the threshold weighting admissible level-set by level-set; and, in the corpus's
construction, the Chevalley return map unitary. THE CORPUS'S OWN `|H|` FLUX-SECTOR DECOMPOSITION
VIOLATES THE THIRD, EXHIBITED IN §5.

alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
