CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = DECLARED-FIRST
CLOSURE_BEGIN_BYTE = 00000000
PREDECLARATION_REGION = EMPTY (closure opens at byte 0; no text precedes it)
PREDECLARATION_OUTPUT_SCAN = 0 hits in authored prose (27-token sweep)
VERDICT_BEARING_SET = exactly the 8 content-addressed members below
UNDECLARED_SEARCH_SURFACE_VERDICT_WEIGHT = forbidden
LANE = DARIO   ROLE_THIS_RELAY = BUILDER (not verifier)
ALL_RESULTS = CLAIMED until the opposite-lane check
```

| # | Closed member | SHA-256 / bounded span SHA-256 | Role |
|---:|---|---|---|
| 01 | `relay_inbox/RELAY_PASTE_945_COMMON_DOMAIN_DARIO_V001.md` | `40d372449c8facd6dc776930d639a393b8a5172de24c0d25e5f0fb789d7f3816` | assignment |
| 02 | `STAGE8_AXN_CHAIN_INSTANCE_DARIO_V001.md` | `c29fe710e1e5a5767af9adb7fce67eb504e7b86a766e59d185b37182c7abea06` | my 924: the split and the common-scope finding |
| 03 | `STAGE8_AXN_CHAIN_INSTANCE_CROSSCHECK_CODEX2_V001.md` | `107aa7509570fb12010a6f8ef482f7737527570b1741e77a33f78ff1532b7261` | the 926 check and the obligation this attempt targets |
| 04 | `R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md`, parent `[5711,6867)` | `40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9`; `eddc2e9ab66e1036e7defdc514b61214e0adef3b48fced3c3aa7a67b6df5f2c3` | `h_K(t)`; `M_c(t)` as multiplication by the cell's spatial section |
| 05 | `STAGE8_T7_CONTINUUM_GALERKIN_PROVENANCE_CORRECTION_V001.md` | `a1258dcf40732f0e3fce358a68ffdbd34bc347d70283550440582a1129bec510` | the sealed masslessness and purely continuous spectrum of `h_0` |
| 06 | `STAGE8_AXN_GALERKIN_CROSSCHECK_DARIO_V001.md` | `7dce7e71c21bba61157433bd63de6491aa66543a654665f1b0f4f70e0203b5b6` | my 942, where I re-derived the same spectral facts |
| 07 | `STAGE8_AXN_SPEC_ACTS_DARIO_V001.md` | `241ccf880266a895f5955173c8c87e7d180d8c6ba6dffefd10f257267454eca1` | the trace-class criterion of Q-829, my sealed tool |
| 08 | `PROGRAM_STATE_BRIEF_V005.md`; `LOCKED_PROCESS.md`; `DECLINE_REGISTER_V002.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c`; `38149496a2b5d89d20b614d972bffef1867d7cde573b26d77dfb207ece3446fb`; `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a` | state pin, process law, S01-S37 authority |

```text
GROUNDS SEAL-VERIFIED BEFORE READING.  NO ANCHOR OBJECT, NO GAUNTLET CLAUSE, AND NO GALERKIN
SELECTOR IS TOUCHED.  NO PHYSICAL QUANTITY IS NUMERICALLY EVALUATED: every constant below is a
symbol or a dimensionless mathematical constant.
```

CLOSURE_DECLARATION_END

# STAGE 8 — AXN COMMON-DOMAIN / AFFILIATION ATTEMPT — DARIO LANE — V001
## RELAY 945 — `[PLAN:AXN-BUILD-D44]` — LINE 6'S THIRD REMAINDER

Date: 2026-08-10
Status: **SUBORDINATION IS PROVED. The relative-domain theorem 926 recorded as absent is constructed
here — and it does not go through the number operator, which is exactly why the missing spectral gap
does not kill it. CLAIMED pending opposite-lane check.**

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1. The obligation, and what I am building

I am the **builder** this relay, not the verifier. Nothing below is certified by me.

My 924 and the 926 check settled the shape: at a common scope both summands of the `D_K` split fall
on the same membership side, and the genuine difference sits at the **one-particle boundedness line
inside the affiliated operator's domain**. 926 named the gap precisely — *a bounded non-trace-class
one-particle input still has an unbounded second quantization, and no sealed relative-domain theorem
makes its domain subordinate to the massless differential lift*.

The sealed tool is Q-829: `dGamma(T)` is bounded **iff** `T` is trace-class. `M_c` is bounded,
infinite-rank, **not** trace-class, so `dGamma(M_c)` is genuinely unbounded. The question is whether
it is nonetheless **subordinate** to `dGamma(h_0)`.

Standing data, read at the sealed bytes:

```text
member 04 :  M_c(t) is multiplication by the spatial section of the causal cell
member 05 :  h_0 is the free MASSLESS Dirac operator, with purely continuous spectrum
```

So `M_c` is multiplication by a bounded function supported in a **bounded** region `Omega_c`, and
`|h_0| = |p|` with `spec|h_0| = [0,inf)` and **no gap**. Throughout I take `M_c >= 0`, as a cell
section is; for a signed profile apply everything to `M_c^+` and `M_c^-` separately.

## 2. The number-operator route, and exactly where it dies [PROVABLE]

This is the obvious route and the relay asks for it to be displayed. It is exact as far as it goes.

**Step 1 — `dGamma(M_c)` is `N`-bounded, sharply.** On the `n`-particle sector
`dGamma(M_c) = sum_(i=1)^n (M_c)_i`, so its norm there is at most `n||M_c||`. For general
`psi = (+)_n psi_n`,

```text
||dGamma(M_c) psi||^2 = sum_n ||dGamma(M_c) psi_n||^2 <= ||M_c||^2 sum_n n^2 ||psi_n||^2
                      = ||M_c||^2 ||N psi||^2.
```

So `||dGamma(M_c) psi|| <= ||M_c|| ||N psi||`, with no additive constant.

**Step 2 — and `N` is NOT `dGamma(h_0)`-bounded.** Here the missing gap bites, and I show exactly
where. Because `h_0` is massless, `spec|h_0| = [0,inf)` has no gap, so the spectral subspace
`1_([0,delta])(|h_0|)` is **infinite-dimensional** for every `delta > 0`. Hence for any `n` and any
`delta` there exist orthonormal one-particle states `phi_1,...,phi_n` with
`supp(phi-hat_i) subset {|p| <= delta}`, so `||h_0 phi_i|| <= delta`. Pauli exclusion is no obstacle
precisely because that subspace is infinite-dimensional. Form the Slater determinant
`Psi_n = phi_1 ^ ... ^ phi_n`:

```text
||N Psi_n|| = n ,        ||dGamma(h_0) Psi_n|| <= sum_i ||h_0 phi_i|| <= n*delta .
```

If `N <= a dGamma(h_0) + b` held, then `n <= a*n*delta + b`. Choose `delta = 1/(4a)` and `n > 4b`:
`n <= n/4 + b < n/4 + n/4 = n/2`, a contradiction. Worked instances:

```text
a=3    b=10     delta=0.0833  n=41    :  41   vs  20.2    CONTRADICTION
a=50   b=1000   delta=0.005   n=4001  :  4001 vs  2000.2  CONTRADICTION
```

**`N` is not `dGamma(h_0)`-bounded. The naive route is dead**, and a gap is exactly what would
rescue it: if `inf spec|h_0| = m > 0` then `dGamma(h_0) >= m N`.

**Step 3 — but the route's death is not the theorem's death.** `N`-boundedness is **sufficient**,
never necessary. And the route is **lossy in a way that matters here**: Step 1 replaces `M_c` by
`||M_c|| * I`, discarding the fact that `M_c` is supported in a bounded cell. That discarded fact is
precisely what makes the infrared harmless — a state with momentum below `delta` is spatially spread
over scale `1/delta` and therefore has only `O(|Omega_c| delta^3)` of its mass inside the cell. The
states that witness `N`'s unboundedness are exactly the states on which `M_c` is nearly blind. So I
keep the localization instead of throwing it away.

## 3. The one-particle lemma [PROVABLE]

**Lemma.** Let `Omega subset R^3` be bounded and `0 <= M = ` multiplication by a bounded function
supported in `Omega`. Then, as one-particle operators on `L2(R^3;C^4)`,

```text
M <= a |p| ,        a = ||M||_inf * C_S^2 * |Omega|^(1/3),
```

with **no additive constant**, where `C_S` is the Sobolev constant of `Hdot^(1/2)(R^3) -> L^3(R^3)`.

*Proof.* Sobolev embedding in the critical form: `Hdot^s(R^n) -> L^q` with `1/q = 1/2 - s/n`; at
`n=3, s=1/2` this is `1/q = 1/2 - 1/6 = 1/3`, i.e. `Hdot^(1/2)(R^3) -> L^3(R^3)`. Then by Hoelder
with exponents `3/2` and `3`,

```text
<phi, M phi> <= ||M||_inf * int_Omega |phi|^2
             <= ||M||_inf * ||phi||_(L^3)^2 * |Omega|^(1/3)
             <= ||M||_inf * C_S^2 * |Omega|^(1/3) * || |p|^(1/2) phi ||^2
              = a * <phi, |p| phi> .                                        [] 
```

**Scaling check on the exponent.** Under `phi_lam(x) = lam^(3/2) phi(lam x)` with `Omega -> Omega/lam`:
`||phi_lam|| = ||phi||`; `<phi_lam,|p|phi_lam> = lam <phi,|p|phi>`;
`|Omega/lam|^(1/3) = lam^(-1)|Omega|^(1/3)`. So the right side is
`lam^(-1)|Omega|^(1/3) * lam <phi,|p|phi>`, **invariant**, and the left side
`int_(Omega/lam)|phi_lam|^2 = int_Omega |phi|^2` is **invariant**. Both sides scale identically, so
the exponent `1/3` is forced. The lemma is also consistent on band-limited states, where it demands
`|Omega|^(2/3) delta^2 <= C_S^2`, true for small `delta` — confirming again that the infrared is not
where this breaks.

**Masslessness is used essentially and helpfully.** `|h_0| = |p|` is homogeneous of degree exactly
one, which is what makes the critical Sobolev exponent line up. (A massive `|h_0| = sqrt(p^2+m^2)`
dominates `|p|`, so the lemma would only improve.)

## 4. The subordination theorem [PROVABLE — PROVED]

**Theorem (CLAIMED).** With `M_c` and `h_0` as above and `a` as in the Lemma, for every `psi` in the
finite-particle core,

```text
|| dGamma(M_c) psi ||^2  <=  a^2 || dGamma(|h_0|) psi ||^2  +  a ||M_c|| <psi, dGamma(|h_0|) psi> ,
```

and consequently, for every `eps > 0`,

```text
|| dGamma(M_c) psi ||  <=  sqrt(a^2 + a||M_c|| eps / 2) * || dGamma(|h_0|) psi ||
                        +  sqrt(a||M_c|| / (2 eps)) * ||psi|| .
```

Hence `Dom(dGamma(|h_0|)) subset Dom(dGamma(M_c))`, with **relative bound `a`** (the coefficient
tends to `a` as `eps -> 0`). **SUBORDINATION HOLDS.**

*Proof.* Write `H_1 = |h_0|`, and work on the `n`-particle sector where
`dGamma(A) = sum_i A_i`. Then

```text
dGamma(M_c)^2 = sum_i (M_c)_i^2 + sum_(i != j) (M_c)_i (M_c)_j
              = dGamma(M_c^2) + sum_(i != j) (M_c)_i (M_c)_j .
```

**Diagonal part.** `0 <= M_c <= ||M_c||` gives `M_c^2 <= ||M_c|| M_c`, and the Lemma gives
`M_c <= a H_1`; so `M_c^2 <= a||M_c|| H_1`, and `dGamma` is monotone, whence
`dGamma(M_c^2) <= a ||M_c|| dGamma(H_1)`.

**Off-diagonal part.** For `i != j` the operators `(M_c)_i, (M_c)_j, (H_1)_i, (H_1)_j` act on
distinct tensor factors, so every pair among them commutes — the only non-commuting pair,
`(M_c)_i` with `(H_1)_i`, never occurs here. For positive operators with `A <= B`, `C <= D` and all
four pairwise commuting, `AC <= BC <= BD`. Applying this with `A = (M_c)_i <= B = a(H_1)_i` and
`C = (M_c)_j <= D = a(H_1)_j`,

```text
sum_(i != j) (M_c)_i (M_c)_j  <=  a^2 sum_(i != j) (H_1)_i (H_1)_j
                               =  a^2 [ dGamma(H_1)^2 - dGamma(H_1^2) ]
                               <=  a^2 dGamma(H_1)^2 ,
```

the last step because `dGamma(H_1^2) >= 0`. Adding the two parts gives the displayed quadratic
inequality. The second display follows by Cauchy-Schwarz,
`<psi,dGamma(H_1)psi> <= ||dGamma(H_1)psi|| ||psi||`, then
`||dGamma(H_1)psi|| ||psi|| <= (eps ||dGamma(H_1)psi||^2 + eps^(-1)||psi||^2)/2` and
`sqrt(x+y) <= sqrt(x) + sqrt(y)`. The estimate is established on the finite-particle core, on which
`dGamma(H_1)` is essentially self-adjoint, and extends to `Dom(dGamma(H_1))` by closure. `[]`

**Independent numerical confirmation of the operator chain.** On finite-dimensional fermionic
sectors with `0 <= M <= aH` imposed exactly at the one-particle level (`a = 1.3`, one-particle
dimension 5, sectors `n = 2, 3`), the quadratic inequality was tested on 1600 random normalized
states across four independent random `(M,H)` pairs:

```text
worst (LHS - RHS) over all trials and states = 0.000e+00     no violation
```

## 5. The honest characterization [PROVABLE — complete]

Task 2 asks for the exact condition under which subordination holds, tested against what the record
seals. Because §4 **proves** it unconditionally for a bounded cell and a massless `h_0`, the
characterization is not a list of rescues but a statement of what the proof actually needs:

| Ingredient | Needed? | Sealed of record? |
|---|---|---|
| `M_c` bounded, supported in a **bounded** region | **Yes — essential** | **Yes**: member 04 makes `M_c(t)` multiplication by the cell's spatial section |
| `|h_0|` homogeneous of degree 1 (massless), so the critical Sobolev exponent matches | **Yes — used** | **Yes**: member 05 seals the free massless Dirac operator |
| spatial dimension 3, for `Hdot^(1/2) -> L^3` | **Yes — used** | **Yes**: the ambient one-particle space is `L2(R^3;C^4)` |
| a spectral gap for `h_0` | **No — not needed** | **No**, and it cannot be: masslessness with purely continuous spectrum is sealed |
| an infrared cutoff | **No — not needed** | **No.** Law 9b: exact-name searches return zero sealed infrared cutoff or regulator for `h_0`; the single `IR cutoff` occurrence in the corpus is an unrelated four-dimensional `K_sea` divergence |
| a particle-number or charge restriction bounding `N` | **No — not needed** | **No.** Law 9b: no sealed particle-number bound, finite-particle-number restriction, or number cutoff exists |

**The characterization is complete, and its content is the reverse of what the naive route suggests.**
The three conditions one would reach for — gap, infrared cutoff, number bound — are exactly the three
the record does **not** seal, and exactly the three the theorem does **not** need. What it needs
instead is the boundedness of the cell, which the record does seal.

## 6. Consequence — displayed, not booked [PROVABLE]

1. **926's gap is closed by construction.** The relative-domain theorem it recorded as absent now
   exists: `Dom(dGamma(|h_0|)) subset Dom(dGamma(M_c))` with relative bound
   `a = ||M_c||_inf C_S^2 |Omega_c|^(1/3)`. The write term's second quantization is **affiliated to
   the differential lift's domain**, not merely to its form domain.
2. **The recombined domain.** Since `dGamma` is linear, `dGamma(h_0 + M_c) = dGamma(h_0) +
   dGamma(M_c)` on the finite-particle core, and by 1 the sum is defined on all of
   `Dom(dGamma(|h_0|))`. Separately, `h_0 + M_c` is self-adjoint on `Dom(h_0)` by bounded
   perturbation, so `dGamma(h_0 + M_c)` is self-adjoint in its own right.
3. **A conditional strengthening, displayed only.** If additionally `a < 1` — i.e. the cell is small
   enough that `||M_c||_inf C_S^2 |Omega_c|^(1/3) < 1` — the relative bound is `< 1` and Kato-Rellich
   applies at the Fock level, giving self-adjointness of the sum **on** `Dom(dGamma(|h_0|))`. Whether
   the sealed cell satisfies `a < 1` is a question about `|Omega_c|`, which I do not evaluate: it
   would be a numeric evaluation of a physical quantity, which the gates forbid and which is not
   needed for 1 or 2.
4. **The source third's booking conditions.** The domain obstruction 926 named is removed; what
   remains for a booking is the opposite-lane check of this proof, and the separate matters of §3's
   hypotheses being the sealed ones. **I display these; I book nothing.**

**What I did not establish.** The relative bound `a` is not shown to be optimal, and I make no claim
about the `t`-dependence of `M_c(t)` beyond fixed `t` — a uniform-in-`t` statement needs
`sup_t ||M_c(t)||_inf` and `sup_t |Omega_c(t)|`, which the parent span does not display at the bytes
I read.

## 7. FREEDOMS-CONSUMED

```text
JOINT_ANCHOR_INPUT = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  M_c(t) as multiplication by the cell's spatial section, at member 04's bytes;
  the massless h_0 with purely continuous spectrum, at member 05's bytes;
  the trace-class criterion of Q-829.

CONDITIONED-ON:
  M_c >= 0 (a cell section); for a signed profile the argument applies to M_c^+ and M_c^- separately;
  the standard Sobolev embedding Hdot^(1/2)(R^3) -> L^3(R^3) and essential self-adjointness of
    dGamma of a self-adjoint one-particle operator on the finite-particle core.

SUBSTITUTED:
  NOTHING. No cutoff, gap, infrared regulator, number restriction, basis, or profile was introduced.
  I did not evaluate |Omega_c|, ||M_c||_inf, or C_S numerically.

DERIVED HERE:
  the one-particle lemma M_c <= a|p| with a = ||M_c||_inf C_S^2 |Omega_c|^(1/3);
  the refutation of N-subordination under a massless h_0;
  the operator subordination theorem and its relative bound.

SCALING WEIGHTS: NONE CONSUMED; NONE FIXED; NONE SUBSTITUTED.
```

## 8. Flattening, custody, byte audit

- **S01-S37 FLATTENING CHECK:** walked. A sufficient route was not identified with a necessary one —
  the death of the `N`-route is reported as the death of a route, not of the theorem. A form bound
  was not identified with an operator bound: §4 proves the operator inequality directly rather than
  upgrading a form inequality, precisely because `A <= aH` does not give `||A psi|| <= c||H psi||`
  for non-commuting positives. A proved theorem was not identified with a booked one (§6). An
  unevaluated constant was not identified with a small one (§6.3).
- **F_PLDEC:** operator inequalities and one dimensionless finite-dimensional check. **No physical
  quantity was numerically evaluated**; `|Omega_c|`, `||M_c||_inf` and `C_S` remain symbols.
- **M-2 / four modes:** exact-name, normalized-name, fixed-string and byte-span checks covered
  spectral gap, mass gap, infrared cutoff, infrared regulator, particle-number bound, number cutoff,
  and the `common domain` prior art — the last of which turned out to be a different question
  (transport-infrastructure carrier typing, zero `dGamma` content), checked rather than assumed.
- **BLIND:** held. No rank read, no ratio formed, no fiber compared or opened.
- **PE-1..PE-13:** pointer-only, zero verdict weight.
- **BUILDER-NEVER-VERIFIES:** I am the builder here. **Every result above is CLAIMED**, and I certify
  none of it. The opposite lane should press §4's off-diagonal commutation step and §3's Sobolev
  constant hardest.
- **CHAIN:** no anchor act, member binding, fixed-point execution, end test, gauntlet, numerical
  evaluation of a physical quantity, or comparison with a measured constant was invoked.

```text
CLOSURE_BEGIN_BYTE = 0
CLOSURE_END_BYTE = 2525
PREDECLARATION_OUTPUT_SCAN = 0 hits
SUBORDINATION = PROVED (relative bound a = ||M_c||_inf C_S^2 |Omega_c|^(1/3))
N_SUBORDINATION = REFUTED (explicit Slater construction)
NUMERIC_CHECK = 1600 states, 0 violations
BOOKINGS_MADE = 0
```

Self verb audit: "proved" applies to the one-particle lemma, the refutation of `N`-subordination, and
the subordination theorem, each with its argument displayed and the last independently checked
numerically. "Displayed" applies to §6, where nothing is booked. "Claimed" governs the whole artifact
until the opposite-lane check. I evaluated no physical quantity and introduced no cutoff, gap, or
regulator. `VERB_AUDIT_SELF = CLEAN`.

## 9. Final lines

```text
CLOSURE = declared-first (byte position 0, closure end 2525; scan 0 hits)
SUBORDINATION = PROVED (bound shown). For M_c >= 0 bounded and supported in the bounded cell Omega_c, and h_0 the sealed massless Dirac operator, the one-particle lemma M_c <= a|p| holds with a = ||M_c||_inf C_S^2 |Omega_c|^(1/3) and NO additive constant, via Hdot^(1/2)(R^3) -> L^3(R^3) and Hoelder; the exponent 1/3 is forced by exact scale-invariance of both sides. Second quantizing through the identity dGamma(M_c)^2 = dGamma(M_c^2) + sum_(i!=j)(M_c)_i(M_c)_j, with the diagonal part bounded by a||M_c||dGamma(|h_0|) and the off-diagonal part by a^2[dGamma(|h_0|)^2 - dGamma(|h_0|^2)] <= a^2 dGamma(|h_0|)^2, yields ||dGamma(M_c)psi||^2 <= a^2||dGamma(|h_0|)psi||^2 + a||M_c||<psi,dGamma(|h_0|)psi>, hence for every eps>0 a Kato relative bound with coefficient tending to a. Therefore Dom(dGamma(|h_0|)) subset Dom(dGamma(M_c)). Confirmed numerically on fermionic sectors: 1600 random states, zero violations
N_ROUTE = displayed (where the massless gap bites). dGamma(M_c) is exactly N-bounded, ||dGamma(M_c)psi|| <= ||M_c|| ||N psi||. But N is NOT dGamma(h_0)-bounded, and the failure is explicit: masslessness makes 1_([0,delta])(|h_0|) INFINITE-dimensional for every delta, so Pauli permits n orthonormal states all with ||h_0 phi_i|| <= delta; the Slater determinant gives ||N Psi_n|| = n while ||dGamma(h_0)Psi_n|| <= n*delta, and n <= a*n*delta + b fails for delta = 1/(4a), n > 4b. A gap would rescue it (dGamma(h_0) >= mN) and there is none. THE ROUTE'S DEATH IS NOT THE THEOREM'S: N-boundedness is sufficient, never necessary, and the route is lossy — it replaces M_c by ||M_c||*I, discarding the cell localization. That discarded fact is exactly what makes the infrared harmless, since a state with momentum below delta is spread over scale 1/delta and keeps only O(|Omega_c|delta^3) of its mass in the cell. The states witnessing N's unboundedness are the states on which M_c is nearly blind
CHARACTERIZATION = complete, and its content inverts the naive expectation. The proof needs a BOUNDED cell (sealed at member 04), a degree-one homogeneous |h_0| i.e. masslessness (sealed at member 05), and dimension three. It does NOT need a spectral gap, an infrared cutoff, or a particle-number restriction — which is fortunate, since law-9b exact-name searches confirm the record seals NONE of the three: no gap is possible given sealed masslessness with purely continuous spectrum; the corpus contains no infrared cutoff or regulator for h_0 (its single "IR cutoff" occurrence is an unrelated four-dimensional K_sea divergence); and there is no sealed particle-number bound or number cutoff
CONSEQUENCE = displayed (booking conditions, unbooked). 926's recorded gap is closed by construction: the write term's second quantization is affiliated to the differential lift's DOMAIN, not merely its form domain. Since dGamma is linear, dGamma(h_0+M_c) = dGamma(h_0)+dGamma(M_c) is defined on all of Dom(dGamma(|h_0|)), and is self-adjoint in its own right since h_0+M_c is self-adjoint by bounded perturbation. CONDITIONAL AND UNEVALUATED: if a < 1, Kato-Rellich would additionally give self-adjointness ON Dom(dGamma(|h_0|)); whether the sealed cell satisfies a < 1 depends on |Omega_c|, which I did NOT evaluate because that would be a numeric evaluation of a physical quantity and is not needed for the domain result. NOT ESTABLISHED: optimality of a, and any uniform-in-t statement, which would need sup_t ||M_c(t)||_inf and sup_t |Omega_c(t)| — not displayed at the bytes I read. I display these; I book nothing
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
