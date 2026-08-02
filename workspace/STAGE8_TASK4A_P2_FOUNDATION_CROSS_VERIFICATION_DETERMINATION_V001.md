# Stage 8 Task 4a P2 Foundation Cross-Verification Determination V001

Date: 2026-08-02  
Task: 4a / P2 cross-verification  
Lane: CODEX LANE 1  
Status: **DEFECT -- ONE EXACT SIGN ERROR; FUNCTIONAL-ANALYTIC FOUNDATION CONFIRMED**

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 0. Lead determination

P2's functional-analytic foundation survives independent reconstruction:

1. the discrete-character times
   `(ell^1 direct-sum ell^1 direct-sum trace-class)` topology is a well-defined
   Banach-component topology on the ratified germ domain;
2. finite sources are norm dense;
3. restrictions are contractive and zero extensions are isometric;
4. Frechet differentiation commutes with finite pullback at first, second,
   mixed, and higher order;
5. no nonzero source or norm-holomorphic germ tail is invisible to every
   finite restriction.

But P2 contains one exact algebraic defect at
`STAGE8_TASK4A_P2_PHYSICAL_SOURCE_TOPOLOGY_AND_DIFFERENTIAL_CALCULUS_CONSTRUCTION_V001.md:448-463`.
It states

```text
D^2 Log_0 Z_inc|_0
  = +p_[A](1-p_[A]) ell_delta tensor ell_delta.
```

For the sealed amplitude

```text
Z(theta)=1-p+p exp(i theta),
```

direct differentiation instead gives

```text
D Log_0 Z|_0   = +i p ell_delta,
D^2 Log_0 Z|_0 = -p(1-p) ell_delta tensor ell_delta.
```

The positive sign belongs to `-Log_0 Z`, not to `Log_0 Z`. The
response-facing object is `W=-i hbar Log_0 Z`; its Hessian is
`+i hbar p(1-p) ell_delta tensor ell_delta`, exactly the Q-243 convention.

Therefore:

```text
P2_LOG_HESSIAN_SIGN_CORRECT = false | TYPE-R |
  test: exact differentiation of Z(theta)=1-p+p exp(i theta)

P2_DIRECT_LOG_DERIVATIVES_EQUAL_Q243 = false | TYPE-R |
  test: Q-243 differentiates the response-facing -i Log convention, not Log

P2_W_DERIVATIVES_REPRODUCE_Q243 = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

P2_FINITE_MIXED_RETARDED_BLOCK_ZERO = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

P2_CROSS_VERIFICATION_VERDICT = DEFECT
```

The sign defect does **not** move the finite Hessian out of the
difference/difference Keldysh block. Multiplication by a nonzero scalar sign
changes the bilinear coefficient, not its branch support. The ordered mixed
retarded block therefore remains zero.

P4 already records the correct three-object convention at
`STAGE8_TASK4A_P4_PHYSICAL_LOG_GERM_ON_P2_CALCULUS_CONSTRUCTION_V001.md:408-431`.
P4 does not inherit the defect. Any future consumer copying P2's displayed
positive `D^2 Log_0` sign rather than P4's convention table would inherit it.

## 1. Preflight, currency, and scope

### 1.1 Preflight

```text
DOES THE OBJECT EXIST?  YES
IS THE VERSION CURRENT? YES -- register head Q-274
ARE ITS INPUTS PRESENT? YES
```

Input hashes independently verified:

| Artifact | SHA-256 | Role |
|---|---|---|
| `STAGE8_TASK4A_P2_PHYSICAL_SOURCE_TOPOLOGY_AND_DIFFERENTIAL_CALCULUS_CONSTRUCTION_V001.md` | `1339e3ce9793b8a528595835091d83db5266705041a440cc9d0c790d16cfb542` | object under review |
| `STAGE8_TASK4A_P4_PHYSICAL_LOG_GERM_ON_P2_CALCULUS_CONSTRUCTION_V001.md` | `b4c77ea948a02f3736fc824976f9ebd6381deff35f5c339a646739ea159725c5` | current sign and branch authority |
| `DECISION_OF_RECORD_014_SOURCE_GERM_PHYS_RATIFIED_2026-08-02_V001.md` | `b6e4116df63403478d28be8cdb6589b091cc1aa8b6ad5a40776a28b135cd138f` | authority ratifying the P2 source presentation |
| `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V004.md` | `d4cdbb6623797df6accb7dc9b24134d179bfc8e8d039c585d5c91ae23255869e` | ratified germ formula and C-A lineage |
| `STAGE8_FINITE_P_CH_DEPENDENCE_AND_PHASE_RESIDUAL_TRANSPORT_DETERMINATION_V001.md` | `8a71b6cdeca839fb6e52dbac4c2d13f7b9d2dafc3531dc1cc8bdc9089b3410b0` | exact finite `-Log` derivatives |
| `STAGE8_TASK4A_FINITE_HESSIAN_TO_DELTAPHI_TRANSPORT_MAP_CONSTRUCTION_AND_P_CH_TRACE_V001.md` | `70185aa842bc500724719c65bd66b5f07005e2214b97be0d35e07fd029d5c68c` | Q-243 finite Keldysh authority |

`LOCKED_PROCESS.md` was read before the review. The retired corpus gate was
not run. No register, tracker, plan, or git object was touched.

### 1.2 Scope

Roots entered:

```text
gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003/
/Users/bgm/MB Work/alpha_supervision/
/Users/bgm/MB Work/alpha-program-archive/workspace/
```

Exclusions:

```text
a32_holdout/
custodian_private/
all response evaluation, residual solving, and measured comparison
```

Searches were word-boundaried or formula-specific. The sign-propagation search
used the exact expressions `D^2 Log_0`, `Gamma_log,N`, and
`p(1-p) ... tensor`; archive-mirror duplicates were not counted as independent
artifacts.

### 1.3 Imported mathematical facts

The independent verification uses four standard functional-analysis results:

```text
finite direct sums of Banach spaces are Banach;
S_1(H)^*=B(H) under the trace pairing;
strongly increasing finite-rank compressions converge in trace norm on S_1;
Frechet derivatives pull back naturally under bounded linear maps.
```

These are imported mathematical theorems, not corpus physics claims. They
apply because DoR-014 names exactly the `ell^1`, trace-class, Banach-sum, and
bounded restriction/inclusion structures appearing in their hypotheses. No
physical continuity, response class, or continuum law is inferred from them.

## 2. V1 -- topology and dual-pairing verification

### 2.1 The actual ratified domain

The C-A source carrier is frozen at
`STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V001.md:180-215`:

```text
E_J   = ell^1(N)_+ direct-sum ell^1(N)_-,
E_R   = S_1,sym(H_CTP),
E_src = E_J direct-sum E_R,

||s||_src = ||J_+||_1+||J_-||_1+||R||_1,trace,
D_src = {+1,-1} cross E_src.
```

V004 retains C-A as part of the fixed non-anchor base at
`STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V004.md:80-102`; DoR-014 ratifies
that presentation. P2 does not silently replace the germ's export domain.

### 2.2 Completeness

Both `ell^1(N)` factors are Banach. `S_1(H_CTP)` is Banach in trace norm.
The branch/source-symmetric part is the fixed subspace of the ratified bounded
branch/source involution and is therefore closed. A closed subspace of a
Banach space is Banach. The finite sum with the sum norm is therefore Banach.

The discrete character factor creates two open-and-closed Banach components.
Frechet differentiation is performed within one component, so no derivative
is incorrectly taken in the discrete direction.

```text
V1_PRODUCT_TOPOLOGY_WELL_DEFINED = true | TYPE-P |
  premises: DoR-014
```

### 2.3 Trace-class pairing

For the full trace-class space,

```text
S_1(H_CTP)^* = B(H_CTP)
```

under the bounded pairing `(B,R) -> Tr(BR)`. Restricting to the closed
symmetric source subspace gives bounded operator representers modulo its
annihilator. This is exactly the correct source/dual shape for taking an
operator-valued bilocal derivative. It does not by itself turn that derivative
into the physical raw correlator: P5 additionally requires the physical
quotient, measure, compound-index convention, contacts, domains, and connected
subtraction (`STAGE8_TASK4A_MISSING_PHYSICAL_LAYER_CONSOLIDATED_SPEC_AND_CONSTRAINT_BATTERY_V001.md:270-289`).

```text
V1_TRACE_CLASS_COMPONENT_SUPPORTS_BILOCAL_DUAL_PAIRING = true | TYPE-P |
  premises: DoR-014

V1_TRACE_CLASS_DERIVATIVE_IS_ALREADY_PHYSICAL_RAW_G = false | TYPE-R |
  test: P5's sealed consumer signature requires additional physical-package data
```

### 2.4 Sequential zero extension

The character `n` is unchanged by every cell restriction and zero extension.
On the Banach factor, coordinate zero extension preserves both `ell^1` norms
and the trace norm of a finite compression. Thus the discrete-character factor
does not interfere with the sequential system.

```text
V1_DISCRETE_CHARACTER_COMPATIBLE_WITH_ZERO_EXTENSION = true | TYPE-P |
  premises: DoR-014
```

## 3. V2 -- dense core and contraction verification

### 3.1 `ell^1` factors

For `J in ell^1(N)`, let `P_N J` retain the first `N` coordinates. Then

```text
||J-P_N J||_1 = sum_(j>N)|J_j| -> 0.
```

Also `||P_N J||_1 <= ||J||_1`; zero extension preserves the norm.

### 3.2 Trace-class factor

Let `P_N` increase strongly to the identity on the cell carrier. For
`R in S_1`, choose finite-rank `F` with `||R-F||_1` arbitrarily small. Then

```text
||R-P_N R P_N||_1
 <= ||R-F||_1
    +||F-P_N F P_N||_1
    +||P_N(F-R)P_N||_1.
```

The first and third terms are controlled by `||R-F||_1`, because compression
by an orthogonal projection is trace-norm contractive. The middle term tends
to zero for fixed finite-rank `F`. Therefore

```text
||R-P_N R P_N||_1 -> 0.
```

The symmetry is retained because the ratified branch/source involution is
cell-independent and commutes with the coordinate compression.

### 3.3 Direct-sum conclusion

Componentwise convergence gives

```text
||s-iota_src,N rho_src,N(s)||_src -> 0.
```

Hence the finite-source union is dense. Every restriction has operator norm
at most one; the bound is sharp on any nonzero source supported in the first
`N` cells. Every zero extension is isometric.

```text
V2_FINITE_SOURCE_CORE_DENSE = true | TYPE-P |
  premises: DoR-014
V2_RESTRICTIONS_CONTRACTIVE = true | TYPE-P |
  premises: DoR-014
V2_ZERO_EXTENSIONS_ISOMETRIC = true | TYPE-P |
  premises: DoR-014
```

## 4. V3 -- differentiation and restriction

For any `C^k` germ `f` on the P2 Banach component, define its finite pullback

```text
f_N := f compose iota_src,N.
```

Because `iota_src,N` is bounded linear, its first derivative is itself and all
higher derivatives vanish. The Banach chain rule gives

```text
D^k f_N(s_N)[h_1,...,h_k]
 =D^k f(iota_src,N s_N)
    [iota_src,N h_1,...,iota_src,N h_k].
```

This is independently proved by induction on `k`: apply the first-order chain
rule to the previous derivative and use the constancy of the linear inclusion.
It covers:

```text
J/J derivatives,
J/R mixed derivatives in both orders,
R/R derivatives,
common/difference Keldysh derivatives,
all higher bounded multilinear derivatives.
```

The Keldysh change of variables is a fixed bounded linear automorphism on the
two branch factors, and finite branch congruence preserves trace class. It
therefore does not break the argument.

The result is a pullback theorem at zero-extended finite points. It does not
claim that a derivative at an arbitrary completed point equals a derivative at
an unrelated finite point.

```text
V3_DIFFERENTIATION_COMMUTES_WITH_FINITE_PULLBACK = true | TYPE-P |
  premises: DoR-014
V3_SECOND_AND_MIXED_ORDERS_INCLUDED = true | TYPE-P |
  premises: DoR-014
```

## 5. V4 -- tail exclusion

### 5.1 The named moving tails

For unit source vectors translated to distinct cells,

```text
||e_m||_1 is fixed,
||e_m-e_n||_1 is bounded away from zero for m != n.
```

The sequence is not Cauchy in `ell^1`. The analogous translated rank-one
bilocal sources are mutually separated in trace norm. Neither moving-tail
sequence has a limit in P2's topology.

### 5.2 All source tails, not only the named example

Suppose `s` lies in every `ker(rho_src,N)`. The `ell^1` coordinates of both
linear sources vanish one by one. Every finite matrix compression of `R`
vanishes; equivalently every matrix element in the increasing cell basis
vanishes. Thus `s=0`:

```text
intersection_N ker(rho_src,N) = {0}.
```

This also closes the more general sequential loophole. If a sequence or net
converges to `s` in `topology_src` while all of its finite shadows tend to
zero, continuity of each restriction gives `rho_src,N(s)=0` for every `N`;
hence `s=0`. No other tail-like family can acquire a nonzero limit in this
topology merely by differing from the named moving-tail example.

Weak, weak-star, or bidual limits do not refute this statement: none is
convergence in `topology_src`. Admitting one would change the source class.
P2 correctly leaves the physical response tail outside its conclusion.

### 5.3 Germ tail

Let a norm-continuous germ vanish on every finite-support neighborhood. For a
point `s` in its open domain, the truncations
`iota_src,N rho_src,N(s)` converge to `s` and eventually remain in that open
domain. The germ vanishes on each truncation and therefore vanishes at `s` by
continuity. The same argument applies coefficientwise to continuous
multilinear derivatives.

```text
V4_TAIL_SRC_ZERO = true | TYPE-P |
  premises: DoR-014
V4_TAIL_GERM_ZERO = true | TYPE-P |
  premises: DoR-014
V4_PHYSICAL_TAIL_R_ZERO = NO_VERDICT |
  prerequisite: instantiated RetHess_phys class and physical restriction maps
```

## 6. V5 -- P4 consistency and the sign defect

### 6.1 Domain topology

P4 writes `Xi_n` as a bounded nonzero complex-linear functional
(`STAGE8_TASK4A_P4_PHYSICAL_LOG_GERM_ON_P2_CALCULUS_CONSTRUCTION_V001.md:228-237`).
Therefore

```text
N_[A],n={s:|Xi_n(s)|<epsilon_p}
```

is open in P2's topology. Each exact zero set is the inverse image of one
closed scalar value under `Xi_n`, hence a closed affine hyperplane
(`ibid.:239-249`). P4's log domain and zero-hyperplane claims are consistent
with P2's topology.

```text
V5_P4_LOG_NEIGHBORHOOD_OPEN_IN_P2 = true | TYPE-P |
  premises: DoR-014
V5_P4_ZERO_HYPERPLANES_CLOSED_IN_P2 = true | TYPE-P |
  premises: DoR-014
```

### 6.2 Independent sign calculation

Use only the sealed one-variable finite restriction:

```text
Z(theta)=1-p+p exp(i theta).
```

At the base point:

```text
Z(0)=1,
Z'(0)=i p,
Z''(0)=-p.
```

Therefore

```text
(Log Z)'(0)=Z'(0)/Z(0)=i p,

(Log Z)''(0)
 =Z''(0)/Z(0)-(Z'(0)/Z(0))^2
 =-p-(i p)^2
 =-p(1-p).
```

This agrees with P4's current convention table at `:408-424` and with the
finite authority's `Gamma_fin=-Log Z` calculation at
`STAGE8_FINITE_P_CH_DEPENDENCE_AND_PHASE_RESIDUAL_TRANSPORT_DETERMINATION_V001.md:154-203`.

Q-243 defines the real branch-difference covector at
`STAGE8_TASK4A_FINITE_HESSIAN_TO_DELTAPHI_TRANSPORT_MAP_CONSTRUCTION_AND_P_CH_TRACE_V001.md:148-178`
and obtains the response-facing Hessian

```text
i p(1-p) ell_delta tensor ell_delta.
```

That is exactly

```text
D^2[-i Log Z]|_0.
```

It is not `D^2 Log Z|_0`.

### 6.3 Block consequence

Both the correct negative `Log` Hessian and the positive `-Log` Hessian are
scalar multiples of `ell_delta tensor ell_delta`. The exact Keldysh transform
therefore puts both in the difference/difference block. The ordered
difference/common block remains zero. Thus the sign defect does not refute
P2's finite retarded-zero statement.

### 6.4 Lineage and propagation scope

The same stale positive `D^2 Log_0` sign appears earlier in
`STAGE8_SOURCE_GERM_PHYS_V002_ADVERSARIAL_REVIEW_DETERMINATION_V001.md:324-346`.
The current P4 artifact explicitly corrects it. The formula-specific sweep
found no further independent exact copy in the entered public roots.

```text
STALE_POSITIVE_LOG_HESSIAN_FOUND_OUTSIDE_P2 = true |
  artifact: STAGE8_SOURCE_GERM_PHYS_V002_ADVERSARIAL_REVIEW_DETERMINATION_V001.md |
  lines: 324-346

CURRENT_P4_SIGN_TABLE_CORRECT = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
```

## 7. V6 -- rank discipline and no-import audit

P2 retains the rank dependence only through the symbolic family coefficient
`p_[A]`; it selects no ordered rank pair. The topology and all norm estimates
are rank independent.

The trace norm and trace pairing are operator-Banach data in ratified C-A.
They are not a spacetime measure, CTP contour, path-integral measure, or state
selection. No contour, boundary prescription, response class, or physical
stationary point is inserted in P2.

C-A is an authored and ratified source completion, not an upstream uniqueness
theorem. P2 states that premise dependence rather than relabeling it as a
derived physical topology.

```text
P2_RANK_VALUE_SELECTION_FOUND = false | TYPE-S |
  roots: P2, SOURCE_GERM_PHYS V001-V004, DoR-014 |
  exclusions: downstream P3-P6 objects |
  query: "rank pair|r_0|r_ch|p_[A]|selected"

P2_SPACETIME_OR_PATH_MEASURE_IMPORT_FOUND = false | TYPE-S |
  roots: P2 and its cited C-A/C-B source lineage |
  exclusions: P3 measure package |
  query: "measure|trace|integral|path|spacetime"

P2_CONTOUR_IMPORT_FOUND = false | TYPE-S |
  roots: P2 and its cited source-germ lineage |
  exclusions: P3 contour package |
  query: "contour|i-epsilon|boundary value"

P2_PHYSICAL_RESPONSE_CLASS_IMPORTED = false | TYPE-S |
  roots: P2 Sections 3-10 and cited P5 interface |
  exclusions: unbuilt P5/P6 construction |
  query: "RetHess_phys|topology_RetHess|physical response"

V6_NO_IMPORT_DISCIPLINE_CONFIRMED = true
```

## 8. Downstream consequence and final verdict

### 8.1 What remains load-bearing

The following P2 results are independently confirmed and remain usable:

```text
topology_src;
finite-source dense core;
contractive restrictions and isometric zero extensions;
Frechet calculus;
first/second/mixed/higher restriction naturality;
Tail_src=Tail_germ={0};
finite Keldysh difference/difference placement;
finite ordered mixed retarded block = 0.
```

### 8.2 What must not be consumed

The following P2 statement is refuted and must not be used:

```text
D^2 Log_0 Z_inc|_0
  = +p_[A](1-p_[A]) ell_delta tensor ell_delta.
```

The lawful convention map is:

```text
D^2 Log_0 Z_inc|_0
  = -p_[A](1-p_[A]) ell_delta tensor ell_delta,

D^2[-Log_0 Z_inc]|_0
  = +p_[A](1-p_[A]) ell_delta tensor ell_delta,

D^2[-i hbar Log_0 Z_inc]|_0
  = +i hbar p_[A](1-p_[A]) ell_delta tensor ell_delta.
```

This determination reports the defect; it does not edit or repair P2.

### 8.3 Verdict

```text
V1_TOPOLOGY = CONFIRMED
V2_DENSE_CORE_AND_CONTRACTIONS = CONFIRMED
V3_RESTRICTION_DIFFERENTIAL_CALCULUS = CONFIRMED
V4_SOURCE_AND_GERM_TAIL_EXCLUSION = CONFIRMED
V5_P4_TOPOLOGICAL_COMPATIBILITY = CONFIRMED
V5_P2_LOG_HESSIAN_SIGN = DEFECT | TYPE-R
V6_RANK_AND_NO_IMPORT_DISCIPLINE = CONFIRMED

P2_FOUNDATION_CROSS_VERIFICATION = DEFECT
DEFECT_SCOPE = displayed Log-Hessian sign and direct Log-to-Q243 identification
DOWNSTREAM_P4_STATUS = NOT INVALIDATED; P4 carries the corrected sign map
```

No physical response, residual, root, scale, coupling, or measured constant
was evaluated or compared. No protected holdout was entered.
