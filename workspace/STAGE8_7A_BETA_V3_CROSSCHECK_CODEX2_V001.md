# STAGE 8 / 7A / CODEX 2 — SYMBOLIC BETA V3 CROSS-CHECK

## 0. Custody, scope, and method

This is the bounded cross-check requested by relay 796. It does not consult PE-1..7, invoke the evaluator chain, select a bundle member, or select any value of `w_Phi`.

| object | SHA-256 | custody result |
|---|---|---|
| `PROGRAM_STATE_BRIEF_V005.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c` | pinned relay contract; verified before task work |
| `STAGE8_7A_DBR_BETA_SECTORS_V3_DARIO_V001.md` | `dcb6617452a14c961fac13fee38bc71d3246809d87ffc97c7c93e67b00b352c8` | adjacent seal matches |
| `STAGE8_7A_TOWER_CONTEST_DARIO_V001.md` (768) | `03db8d3da273f42c62acdea5d453ec0b780934c73aa897fdf2cfb986c0e7bc9b` | adjacent seal matches |
| `STAGE8_7A_DBR_LAYER_REBUILD_DARIO_V001.md` | `d55b64459be8bdacbcc102486bc5948362f6e45b8c6b3a512bea2689fe9c20f7` | adjacent seal matches |
| `LOCKED_PROCESS.md` | `7ca46f2fc23e4c123f19489f22c8fc84ad0fc8209d0b4bca4b6f88d11a3204b7` | live file and current adjacent seal match; law 2a read at lines 546–550 |

Decisive spans:

| source | span | span SHA-256 | use |
|---|---:|---|---|
| 768 | `[10764,11705)` | `d08cccc778b13b4422097cefba00247c28f7dbe960668481328684ec16274dc2` | sealed operator decomposition and derivative orders |
| 768 | `[14179,15766)` | `f960f2be4c8b290bb0d31bafcad97c00a49199d4e417dc26cb7d15653ded78d0` | original beta table and the contradictory fixed-cross/unselected-`Phi` wording |
| V3 | `[4388,6691)` | `262b93222263b654938d7abdde265e5725fb17cccaf3e98b405cf895658dacde` | symbolic table and coincidences |
| V3 | `[6691,9486)` | `c64d7764ebeaa408fdb45ea33372506e47f1d880947554341653384cf642139e` | six unconditional and four conditional statements, plus ratios |
| V3 | `[9486,12032)` | `a2760984bc5438018a1cd0e0d3c2c5267952e7476cf7022484f513a2dee215f0` | freedom and flattening blocks |
| layer rebuild | `[16085,17032)` | `be1f48b94233df01725398f9f1380aef4d00a763c4fff3b878f2bfb2536276e8` | shared-`Phi`/class-independence statement |

All headline statements in V3 entered this check as `CLAIMED`. The verdicts below are the cross-check dispositions.

## 1. AS1 — sector table

Write the four exponents as

```text
g = -2                 geometric terms
x = w_Phi - 1          cross term
c = 0                  C2_parent
p = 2 w_Phi            Phi^dagger Phi
```

The sealed 768 operator span identifies three geometric denominators, one covariant derivative in `T = Gamma_Sigma c(nabla_A Phi)`, a radius-free internal `C2_parent`, and a zeroth-order two-`Phi` term. After carrying `Phi -> beta^(w_Phi) Phi`, the V3 table follows term by term:

| sector | V3 weight | cross-check |
|---|---|---|
| geometric | `beta^-2` | **CONFIRMED** — inverse-square radii; no `Phi` |
| cross | `beta^(w_Phi-1)` | **CONFIRMED** — sealed one-derivative factor times the carried `Phi` weight |
| `C2_parent` | `beta^0` | **CONFIRMED** — sealed radius-free internal invariant |
| `Phi^dagger Phi` | `beta^(2w_Phi)` | **CONFIRMED** — two powers of the carried `Phi`; no derivative factor |

The complete coincidence calculation is:

```text
x = g  iff w_Phi = -1       p = g iff w_Phi = -1
x = c  iff w_Phi =  1       p = c iff w_Phi =  0
x = p  iff w_Phi = -1       g = c has no solution
```

Therefore the weights are `{-2,-2,0,-2}` at `w_Phi=-1` (two distinct), `{-2,-1,0,0}` at `w_Phi=0` (three), `{-2,0,0,2}` at `w_Phi=1` (three), and four distinct weights away from `{-1,0,1}`. **CONFIRMED.**

### 1.1 Implicit-weight hunt

Every fixed exponent in the operative V3 table is either (i) the sealed derivative/radius weight, (ii) the sealed radius-free weight, or (iii) the definitional common-radius weight. Every occurrence of `w_Phi = -1`, `0`, or `1` is inside an expressly unselected specialization, coincidence equation, historical-defect quotation, or conditional classification. The cross term and `Phi^dagger Phi` remain symbolic everywhere they are used operatively. `Gamma_Sigma`/`c` introduce no unbooked freedom at the governing strength: 768 itself classifies the complete cross carrier as exactly one covariant derivative with `Phi`'s scaling left over.

**Verdict: no remaining implicit weight found.**

## 2. AS2 — unconditional core and conditional demotions

### 2.1 Six all-`w_Phi` statements

| # | statement | verdict | independent check |
|---:|---|---|---|
| 1 | geometric sector is `beta^-2` | **CONFIRMED** | `g=-2` contains no `w_Phi` |
| 2 | `C2_parent` is `beta^0` | **CONFIRMED** | `c=0` contains no `w_Phi` |
| 3 | beta is non-uniform for every `w_Phi` | **CONFIRMED** | the `Phi`-free pair `(g,c)=(-2,0)` is distinct for every `w_Phi` |
| 4 | beta cannot be absorbed by one overall normalization | **CONFIRMED** | one normalization cannot remove two unequal exponents already present in the `Phi`-free pair |
| 5 | the two radius ratios are beta-invariant | **CONFIRMED** | re-derived in section 3 |
| 6 | non-uniformity is class-independent | **CONFIRMED** | the decisive witness is `Phi`-free and uses only the class-independent exponents `-2` and `0`; the sealed layer rebuild also records the unselected `Phi` scaling as shared |

The unconditional core is **6/6 confirmed**. In particular, it does not require a value, form, or class assignment for `Phi`.

### 2.2 Four demotions — one localized directional defect

| # | V3 demotion | verdict |
|---:|---|---|
| 7 | 768's compound claim that the cross term “adds a THIRD weight” and yields “three sectors” is true at `w_Phi in {0,1}` | **REFUTED AS STATED.** At `w_Phi=1`, `x=0=c`: the cross term does **not** supply a third weight; `p=2` supplies it. The two predicates must be separated. “Total count is three” holds at `{0,1}`; “the cross term supplies a third weight distinct from geometric and `C2_parent`” holds for `w_Phi` outside `{-1,1}`. Their conjunction holds only at `w_Phi=0`. |
| 8 | `Phi^dagger Phi` is in the `beta^0` sector only at `w_Phi=0` | **CONFIRMED** (`2w_Phi=0`) |
| 9 | four sectors occur only generically, not at `{-1,0,1}` | **CONFIRMED** by the complete coincidence set |
| 10 | count is two at `-1`, three at `{0,1}`, four generically | **CONFIRMED** |

This finding does not alter the symbolic table or any of the six unconditional statements. It does mean V3 did not survive **whole**: conditional row 7 conflates a direction-bearing “cross supplies” predicate with the undirected total count.

## 3. AS3 — ratios re-derived

Let the common rescaling send

```text
(R_T, R_Q, r_flux) -> (beta R_T, beta R_Q, beta r_flux).
```

Then

```text
(beta R_T)/(beta r_flux) = R_T/r_flux
(beta R_Q)/(beta r_flux) = R_Q/r_flux.
```

Neither ratio contains `Phi`, so the separate transformation `Phi -> beta^(w_Phi) Phi` has no operand in either expression. Hence both ratios are functions of the radii only and their formal derivatives with respect to `w_Phi` vanish identically. This is an independent algebraic derivation, not inheritance from 787 or V3.

**Verdict: re-derived CONFIRMED.**

## 4. AS4 — freedom block audited against every operative formula

| formula-consumed datum | V3 disposition | cross-check |
|---|---|---|
| `w_Phi` | carried as parameter | **TRUE** — occurs symbolically in both `Phi` sectors; no value consumed |
| odd profile `Phi` | carried as parameter | **TRUE** — no form, norm, commutation, or value supplied |
| `beta` | carried as parameter | **TRUE** — no value supplied |
| common radius weight `1` | definitional | **TRUE** — this defines the common rescaling rather than selecting a datum |
| `R_T`, `R_Q`, `r_flux` | carried as parameters | **TRUE** — retained in denominators and ratios |
| numerical `C2_parent` | carried as parameter | **TRUE** — only its sealed radius weight `0` is used |
| bundle class/chiral index `n` | not consumed | **TRUE** — no member is evaluated or selected; the non-uniformity witness is class-independent |
| spin structure / `p^2_min` | not consumed | **TRUE** — no floor or member bound is evaluated |
| `N_lattice` | not consumed | **TRUE** — no trace or multiplicity is evaluated |
| analytic input `f` | not consumed | **TRUE** — no functional is evaluated |
| counting inner product | not consumed | **TRUE** — no minimum-norm/counting object is used |

The implicit-weight hunt found no missing scaling-weight row. The error in conditional row 7 is a predicate-condition error, not an undisclosed consumption of a freedom. Therefore the block is complete and true against the formulas actually used.

## 5. Jurisdiction, gates, and self audit

The cross-check was adversarial in both directions: it confirms the load-bearing symbolic table and six-statement core, while refusing the one over-broad conditional classification. The attractive `w_Phi=-1` specialization was not selected. No bundle member was bound, adopted, or eliminated. No fixed point, end test, determinant, physical numerical evaluation, or comparison with measured constants was performed. The evaluator chain was not invoked.

Self verb audit: the report uses `CONFIRMED`/`REFUTED` only as the requested cross-check verdicts and does not convert a claim into authorization, proof authorization, or a physical conclusion. **CLEAN.**

```text
TABLE = CONFIRMED
IMPLICIT_WEIGHT = none found
UNCONDITIONAL_CORE = CONFIRMED (6/6; conditional demotion #7 separately REFUTED as directionally conflated)
RATIOS = re-derived CONFIRMED
FREEDOMS_BLOCK = complete and true
PHASE_A_BANKS = no (residual: split conditional row #7; at w_Phi=1 the third sector is supplied by Phi^dagger Phi, not the cross term)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
