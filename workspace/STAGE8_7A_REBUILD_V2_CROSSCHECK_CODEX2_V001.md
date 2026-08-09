# STAGE 8 / 7A / [PLAN:A2-CORRECTIVE-2] — REBUILD V2 ADVERSARIAL CROSS-CHECK

Lane: CODEX 2 (independent cross-check). Relay 787. Date: 2026-08-09.

All headline dispositions in this report are **CLAIMED pending registrar/Dario cross-check**. The
result is not convergence: the radius, tier, and member-bound repairs survive, but the beta
surface and its freedom accounting do not.

## 0. Preflight, custody, and fences

```text
PICKUP ACK       relay_outbox/787_ACK.md written before relay content was read
LANE GUARD       CODEX 2
STATE BRIEF      PROGRAM_STATE_BRIEF_V005.md
                 e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c
SUBJECT          STAGE8_7A_DBR_LAYER_REBUILD_V2_DARIO_V001.md
                 dcc84e6a58a9fae4de42ff06181febbff7348b285233bec43717432f4b985b71
768              STAGE8_7A_TOWER_CONTEST_DARIO_V001.md
                 03db8d3da273f42c62acdea5d453ec0b780934c73aa897fdf2cfb986c0e7bc9b
781              STAGE8_7A_DBR_LAYER_REBUILD_DARIO_V001.md
                 d55b64459be8bdacbcc102486bc5948362f6e45b8c6b3a512bea2689fe9c20f7
783              STAGE8_7A_REBUILD_CROSSCHECK_CODEX2_V001.md
                 8cef86b990895978898b8020e053c6c04120e5064608559a8dd0f1a598a27f21
DECLINES         DECLINE_REGISTER_V002.md
                 957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a
764              STAGE8_7A_TOWER_REBUILD_DARIO_V001.md
                 84ceeb49dd282736ce0cb1347e923c8a8c9b1d26ea151ccbb19f6d857dd9e0bf
PRINCIPLE        alpha_global_record_surface_superconnection_principle_v001.md
                 ae1d04922cb37f8b5631a11551b7db57f483bd6b0d8b7c54d59b4f4ae593768f
OUTPUT PROBE     artifact and sidecar absent before write
```

The subject and each sidecar-bearing source above were verified before use. `PRINCIPLE` has no
adjacent sidecar in this custody copy; its bytes match the digest pinned throughout the sealed
tower stock. The subject's reference to a live Q-690 append is not present in this custody copy
of the settled register; no conclusion below depends on that append because 783 independently
derives the same symbolic floor from the sealed operator.

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
No member binding; no fixed-point execution; no end test; no determinant evaluation; no numeric
evaluation of a physical quantity; no comparison to measured constants; no bundle class adopted
or eliminated; FAMILY-BEFORE-DETERMINANT maintained.
PE-1..PE-7 = pointer-known, ZERO WEIGHT, not consulted and not opened.
```

## 1. Evidence index

All spans are half-open byte spans; hashes cover exactly the cited bytes.

| ID | source | span | span SHA-256 | use |
|---|---|---:|---|---|
| E1 | subject | `[4153,7620)` | `ca9f9b33b8da261b366e45505178fc9fc952f4c46832cbe6aa748e390c17d07c` | radius derivation, (U), beta table |
| E2 | subject | `[7949,10516)` | `d3ff97c361d2096aa9c29917e590b94a27a7bff959fc0c72763a2a7e92e08a34` | tier-2 drop and replacement |
| E3 | subject | `[10516,11244)` | `b78c5779525258362c4626e579d1718dd4dd79f1aa7906e6b758c23035bc034f` | tier-3 conditions |
| E4 | subject | `[11549,13428)` | `03d758c94f39ad00f90b4f0cf964bcfe4c37672224d43a7f77fec726bf8738c9` | member bounds and separation |
| E5 | subject | `[15174,16594)` | `19fe0be5c6bca4fe4799cba6d0a81ee9ad98463e6d94aa4314445774207982c8` | freedom ledger |
| E6 | 768 | `[14179,15766)` | `f960f2be4c8b290bb0d31bafcad97c00a49199d4e417dc26cb7d15653ded78d0` | sealed beta display, including `Phi`'s unselected scaling |
| E7 | 764 | `[11016,11590)` | `22cf2e36b81346a3db8a32db92a969ffccb4b88f3f9bac2996f0c3678e9ce148` | radii-explicit tower and unit-radius recovery |
| E8 | declines | `[10949,11716)` | `b3e766e98e6d3f7137fd052d1bc8853021cbb4f683fc43d4fd6ea2cb7c140349` | S27 and S28 exact wording |
| E9 | principle | `[1532,2000)` | `69bf62767491d5aec49a8ac15f01a41265ed24846488d336d79792199aa9e777` | unselected data and selection rule |

## 2. AS1 — radius derivation

### 2.1 Product argument

**CONFIRMED at the sealed product-tower scope.** On a Riemannian product with product spin
structure,

```text
D_(Sigma,A) = D_(T2) tensor 1 + Gamma_(T2) tensor D_(S2,A).
```

The two first-order summands anticommute; after squaring, the cross term vanishes and the two
second-order summands commute. Hence the geometric spectrum has the exact symbolic form

```text
p_t^2/R_T^2 + p_q^2/R_Q^2 + ell(ell+2|q|)/r_flux^2.
```

This confirms E1 against E7. It does not upgrade the product-tower carrier into a selection of
the radii or of a particular torus spin structure: E9 leaves both free. The spin structure shifts
the occupied lattice labels and therefore `P_min`; it does not change the three denominators.

`Phi^dagger Phi` is zeroth order, so derivative counting supplies no geometric radius
denominator. Its intrinsic scale remains unselected. `C2_parent` is an internal invariant, not a
geometric derivative on `Sigma_BR`, so it is radius-free in the carried normalization.

### 2.2 Noncommutation and unit-radius audit

**The noncommutation flag is retained.** E1 states that `spec(H_0)` is not the sum of the
summands' spectra because `Phi^dagger Phi` need not commute with the geometric square. The only
scalarized trace is under condition `(S)`, which expressly requires scalarity and commutation.

I enumerated each operative occurrence of the geometric tower, the two member-bound right-hand
sides, the A–B bound separation, and the declined `mu^2=1` member. Every unconditional or
`(F)+(S)` formula keeps the denominators. Their removal is attached to precisely the five named
`(U)` sites:

1. the denominatorless tier-3 display;
2. member A's `+1` form;
3. member B's unchanged zero sphere term;
4. the numerical `1` separation;
5. the declined `mu^2=1` display that inherits the unit-radius presentation.

The repeated executive summary merely restates these conditioned surfaces. **No sixth implicit
unit-radius use was found.**

## 3. AS2 — tier 2

### 3.1 Independent negative-existential probe

**CONFIRMED over the accessible sealed cleanroom stock.** I independently searched 1,911
`.md`/`.json` corpus files after excluding relay inbox/outbox, evaluator builds, checks, run
directories, caches, PE material, and the subject under review. Positive controls were nonzero:
`Phi^dagger Phi` in 17 files, `E_parent` in 16, `C2_parent` in 14, and `flat parent connection` in
7. Exact forms for `Phi` proportional to or a multiple of the identity returned zero. The exact
scalar-carrier candidates were then read:

- 781 and 783 state `Phi^dagger Phi = mu^2 Id` only as condition `(S)`, expressly not as a fact;
- 768 lists `nabla_A Phi=0` and commutation/diagonalization as WOULD-BUILD alternatives;
- the earlier spectrum report says only *if* `Phi` is constant;
- the tower cross-check states that no sealed sentence makes `Phi` covariantly constant or sets
  `Phi^dagger Phi=1`.

No candidate is a sealed scalar-`Phi` carrier. The smaller independent custody census and the
subject's wider census therefore agree on the meaning result; this report does not claim that a
file count proves an unrestricted universal.

### 3.2 Replacement typing

The replacement is exactly typed:

```text
Tr_{L2(Sigma_BR,S_Sigma) tensor E_parent}
  f(D_base^2 tensor Id_E + Phi^dagger Phi + C2(16) Id_E).
```

Under `(F)`, the geometric square is tensored with the identity and the central Casimir is scalar
on the irreducible 16. `Phi^dagger Phi` remains an endomorphism on the full carrier. Therefore no
factor `16` may be extracted from the trace. That is the strongest lawful `(F)`-only surface in
the cited stock.

## 4. AS3 — tier 3 and member bounds

### 4.1 Tier 3

**CONFIRMED.** The scalar sum consumes `(F)` to flatten the parent multiplicity and `(S)` to make
`Phi^dagger Phi = mu^2 Id` constant and commuting. With those two conditions, the trace keeps
all three radii. `(U)` is optional and is consumed only by the denominatorless specialization.
`N_lattice(p_t,p_q)` remains explicit. I found neither an omitted condition nor sealed ground
that would strengthen the `(F)+(S)` surface by removing either condition.

### 4.2 Bounds and attempted violations/strengthenings

**CONFIRMED as lower-bound statements, not bottoms.** Positivity gives the universal symbolic
floor `lambda >= C2_parent`; 783 supplies the operator proof and an admissible equality witness,
so no unconditional strictly positive strengthening is available. For the simple factorized
member laws, `(F)` is necessary because without it the parent connection can change the spectrum,
not merely its multiplicity. With `(F)`, positivity of `Phi^dagger Phi` gives

```text
member A: lambda_A >= P_min + 1/r_flux^2 + C2_parent
member B: lambda_B >= P_min + 0          + C2_parent.
```

These bounds are unconditional in `Phi`: noncommutation of positive summands does not make their
sum negative. `(S)` would be needed to locate exact bottoms, which the subject correctly declines.
`(U)` is not needed because the radius remains explicit.

Subtracting the two displayed right-hand sides gives exactly `1/r_flux^2`; this is a separation
of the **bounds**, not an evaluated spectral gap. It is a free datum because `r_flux` is unselected.
The only lawful strengthening found is the already displayed unit-radius specialization under
`(U)`, where the symbolic separation becomes `1` by convention.

## 5. AS4 — beta sectors

**REFUTED.** The three geometric terms have weight `beta^-2`; `C2_parent` has weight `beta^0`;
and the two radius ratios survive one common scalar rescaling. Those parts are confirmed.

The cross sector is not absolutely `beta^-1` while `Phi`'s transformation is unselected. Let the
unselected intrinsic scaling be represented symbolically by

```text
Phi -> beta^w_Phi Phi.
```

Then derivative counting gives the complete sector surface

```text
geometric squares                  -> beta^-2
Gamma c(nabla_A Phi)               -> beta^(w_Phi-1)
C2_parent                          -> beta^0
Phi^dagger Phi                     -> beta^(2 w_Phi).
```

E6 states this exact qualification in words: the cross term is `beta^-1` **times `Phi`'s own
unselected scaling**. E1 drops that factor for the cross term while declaring the same scaling
unselected for `Phi^dagger Phi`. The displayed four-sector assignment therefore silently uses
`w_Phi=0` in one row and refuses to choose `w_Phi` in another. A lawful repair would either carry
`w_Phi` in both `Phi` sectors or state explicitly that only the derivative-order contribution is
`-1`; it may not call the total cross-term weight `-1` unconditionally.

The ratio subclaim remains true and independent of this defect: one common `beta` removes one
overall scale from three free radii, leaving two independent ratios.

## 6. AS5 — freedoms block and S27

### 6.1 Item-by-item audit

| consumed freedom | subject tag | cross-check |
|---|---|---|
| analytic input `f` | carried-as-unselected | correct |
| `R_T`, `R_Q`, `r_flux` | carried; conditioned via `(U)` at five sites | correct |
| odd profile `Phi` | carried; conditioned via `(S)` at tier 3 | **incomplete/false at beta table**: its unselected scaling is silently fixed to `w_Phi=0` in the cross sector |
| parent bundle/class | conditioned via `(F)` at tiers 2/3 and both member bounds | correct |
| `C2_parent` normalization/value | carried | correct |
| torus spin structure, hence lattice and `P_min` | carried | correct |
| chiral-index/family parameter `n` | carried | correct |
| `N_lattice` | carried explicitly | correct |

Thus the block is **FALSE**, not because another geometric parameter disappeared, but because its
`Phi` row says *carried* while §1.3 substitutes one transformation direction. This is the
requested invisible-direction failure. The statement `SUBSTITUTED: none` is false at that site.

### 6.2 S27/S28 wording

**S27 is confirmed exactly.** E8 grants flat `x16` **multiplicity** only when the flux `U(1)` is
external to `Spin(10)` with flat parent connection. It does not state that an arbitrary
`Phi^dagger Phi` is scalar on the internal carrier, so it refuses 781's extraction of `16` from
the full trace. S28's five primary free-data classes all appear in the subject ledger and none is
selected by boundary closure or an induced action here. The residual concerns `Phi`'s scaling
account, not a selection of any S28 datum.

## 7. Claim ledger and jurisdiction

| claim | verdict | decisive reason |
|---|---|---|
| radius/product-tower derivation | **CONFIRMED** | product Dirac square splits; three denominators retained |
| noncommutation flag | **CONFIRMED** | no sum-of-spectra statement without `(S)` |
| implicit unit radii | **none found** | all five operative specializations named `(U)` |
| tier-2 drop | **CONFIRMED** | independent negative existential; tensor surface correctly does not factor 16 |
| tier-3 conditions | **CONFIRMED** | `(F)+(S)`, with `(U)` optional and explicit |
| member bounds | **CONFIRMED** | `(F)` attached, unconditional in `Phi`, exact RHS separation `1/r_flux^2` |
| four beta sectors | **REFUTED** | cross term omitted `Phi`'s unselected scaling factor |
| two beta-invariant radius ratios | **CONFIRMED** | one common scale acting on three independent radii |
| freedoms block | **FALSE** | invisible `w_Phi=0` substitution in cross sector |
| S27 reading | **CONFIRMED** | grant is multiplicity, not scalarization of `Phi` |

No class was adopted, preferred, evaluated, or eliminated. Conditions `(F)`, `(S)`, and `(U)`
remain conditions. The symbolic variable `w_Phi` above is an audit coordinate for an unselected
transformation law, not a selected value or a new physical postulate.

RADIUS_DERIVATION = CONFIRMED
IMPLICIT_UNIT_RADIUS = none found
TIER2_DROP = CONFIRMED (negative existential reproduced)
TIER3_CONDITIONS = CONFIRMED
MEMBER_BOUNDS = CONFIRMED
BETA_SECTORS = REFUTED (cross term silently fixes Phi scaling; sealed form is beta^-1 times Phi's unselected scaling)
FREEDOMS_BLOCK = FALSE (Phi tagged carried while w_Phi=0 is invisibly substituted in the cross sector)
CONVERGED = no (residuals: beta cross-sector assignment and the corresponding freedoms-account false negative)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
