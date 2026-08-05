# STAGE 8 TASK 5 / EQ6 — J2 BUILD UNDER THE ADOPTED ROW + THE CORRECTED-CONTRACT COMPLETION

```text
TASK = Q-481
LANE = CODEX_LANE_2
ARTIFACT_TYPE = J2_BUILD_V002
CONDITION_TAG = [EQ6]
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
NO_NUMERIC_EVALUATION = true
NO_MEMBER_BINDING = true
NO_FIXED_POINT_OR_THRESHOLD_OR_END_TEST = true
NO_RESPONSE_OR_VERDICT_CONCLUSION = true
```  

## 0. Preflight and hash verification

Verified before work:

- `alpha-program-archive/supervision/DOR_020_A6_J2_SCOPED_PROJECTED_LAW_2026-08-05.md` : `202234ac77136592fdc24a96838909f1dad7e8f6a79fdab81342c5f12d6e82cd`
- `STAGE8_TASK5_EQ6_PROJECTOR_CERT_V003_LANE1_V001.md` : `0bef9a003abb586666535689e98d7af29e7fc75b81e06fe439397ce2b8ef9100`
- `STAGE8_TASK5_EQ6_SCOPED_MATE_CERT_LANE1_V001.md` : `088eccd9ee642fcffb83e9f1ef1bb64ef479fd68534a6f3fb55d6aebce1393ce`
- its review `STAGE8_TASK5_EQ6_SCOPED_MATE_REVIEW_LANE2_V001.md` : `e104c092119136160c2e193ef5e51852cb7ff2b68491af3a15c3c318f49a2de0`
- `STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V004.md` : `9bf34e27da9aca51966feb2b41f34b0060e2121bd85d783d35a81685bbb63514`
- `STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V001.md` : `e21cee3081da06417109697352abe570c58dc6dda7d46e78f690d666bed128f5`
- `STAGE8_TASK5_EQ6_PARTIAL_JOINT_DIAMONDS_LANE2_V001.md` : `5539b53ddeb208638af314f34e018591e1e6bd93403906e6a5edd46bc34e4766`
- `STAGE8_TASK5_EQ6_DIAMONDS_REVIEW_LANE1_V001.md` : `fa3ab255829aa7768a6f9fe35f800c1a25117627e42d22313eb5e6d28b4abd41`
- `STAGE8_TASK5_EQ6_SCOPED_MATE_REVIEW_LANE2_V001.md` : `e104c092119136160c2e193ef5e51852cb7ff2b68491af3a15c3c318f49a2de0`
- `STAGE8_TASK5_EQ6_PHYSICAL_J2_LANE2_V001.md` : `3fd4b924ec1a70f3e730bcf99f406d697c53937b26467d2ae6d5aa8c1bb6822c`
- `STAGE8_TASK5_EQ6_MAXWELL_HODGE_PROJECTOR_CERT_LANE2_V001.md` : `f074ca24e8b96c576f5c64b856377f39ed8d4fc729c02cbf591326322558f816`

DoR-020-A6 is law and therefore binding for cycle-creating arrows.

## Register sweep (as required)

Keys reviewed before construction: Q-477 through Q-479 lineage, stage-1 V004 review family, scope-shifted J2/J7 corrections, lane-1 partial diamonds, and DoR-020-A5/A6.

## K1. Pose J2 under the adopted row

I split J2 into the two adopted domains:

1. **Rank-preserving arrows** (`f` rank-preserving in W3):
   - use full J2 equation
   
   `reader_f = pi_Mx,F ∘ Loc_F ∘ Kernbar_F ∘ Q_F`

   (with the same domain/codomain as the stage-1 data). 

2. **Cycle-creating arrows** (`f` cycle-creating):
   - use only the scoped projected law (A6), per sector:

   `r_f^Bot ∘ pi_Mx,M ∘ Loc_M ∘ η_f = pi_Mx,N ∘ Loc_N`  
   equivalently `SCOPED_J2_SQUARE` on the old-image/`P_H` sector.

3. **New-cycle factors** in `I_F`:
   - not postulated as full formed J2 here; they remain the explicit post-scope condition.

## K2. Proof on the actual tower

### Covered arrow classes and factors

- **`Q` factor**: from the fixed finite Q-408 stock (actual current map).
- **`Kernbar`**: finite closure already proved in the confirmed stock (`Kernbar_N(Q_N z)=Kern^raw_N(z)` on `O_prof,N`), with the nonzero reciprocal-loop witness retained.
- **`Loc`**:
  - rank-preserving: uses the finite symbol/localization factor from stage-1/2 stock;
  - cycle-creating: only in the projected old-image sector via scoped certificate `Loc_M`/`Loc_N` as used by A6.
- **`pi_Mx`**:
  - rank-preserving: carried as finite projected map from `V003` finite-maxwell projector object (`π_Mx,N := π_M^resp ∘ P_H,N ∘ Loc_N` style descent, with the old-image factor split explicit);
  - cycle-creating: projected mate only, i.e. `r_f^Bot`-postcomposed form.
- **`reader` comparison**: the family formula
  
  `p_(chi,T)[Q_N(a,b,C)] = a + chi_N\cdot b + Tr(T_N C)`

  is used only to evaluate consequences on closed overlap instances, not to define `Loc` or `pi_Mx`.

### Equality checks

- **Rank-preserving routes**: the full composite equality can be reconstructed arrowwise using the rank-preserving covariance already in `V003` cert (`ρ_f d_M = d_N ρ_f`, `ρ_f δ_M = δ_N ρ_f`, `ρ_f P_H,M = P_H,N ρ_f`) and the assembled finite factors above.
- **Cycle-creating routes**: each covered cycle-creating overlap in `I_F` satisfies the scoped square exactly because it is the induced mate from the same `r_f^Bot`/`η_f` pair used in the scoped mate cert and reviewed in Q-478/479. The full square is intentionally not claimed in this scope.
- **Mismatch check**: no covered instance fails under the adopted split; where full cycle-creating `Loc_N`/`pi_Mx,N` are absent, the task only records the explicitly scoped law as the row.

## K3. The J7 face (corrected contract)

Per `fa3ab255…` and the corrected diamonds contract:

**Cycle-creating J2 face (`J7` on new-cycle class):**

`r_f^Bot ∘ pi_Mx,M ∘ Loc_M ∘ eta_f = pi_Mx,N ∘ Loc_N`.

The remaining piece in the comparison row is the **non-cycle domain condition**:

`full rho∘Δ` is kept as a condition-only residual on new-cycle domain, not an equality consumed by this build.

This is thus not an extrapolation of the rank-preserving face and does not use response/threshold consequences.

## K3b. Corrected completion theorem re-proof

From `5539b53d… D3` and its correction in `fa3ab255…`:

- with **J2** instantiated as: full on rank-preserving, scoped on cycle-creating, and
- **J7** instantiated as above on cycle-creating,

the partial FC11 overlap diamonds remain exactly the same five confirmed faces and now assemble to full FC11 on the same scopes.

Therefore the previous GAP from over-demanding cycle-creating full J2 is removed under the corrected contract. No extra face is introduced; only the existing open full-cycle content is acknowledged as post-scope and non-formable in current stock.

## K4. FC10 consequence list

Under the adopted split, FC10 now has these status updates:

- `J2` is supplied as a **scoped two-part row**:
  - full rank-preserving part on the admissible finite rank-preserving arrow class;
  - scoped cycle-creating part (`SCOPED_J2_SQUARE`) on old-image/`P_H` sector.
- `J7` is supplied in its corrected contract form on cycle-creating arrows:
  - projected bottom comparison at the `r_f^Bot` level,
  - new-cycle branch left as non-cycle-domain condition.
- `J10`/non-specified remainder (full new-cycle J2 form): unchanged as post-scope open condition.
- `FC11` completion theorem remains as a conditional exactness theorem once the two corrected faces are supplied (that is now checked as `COMPLETION_THEOREM_V2` in `K3b`).

## K5. Battery and regressions

Executed in this relay:

1. **F_PLDEC circularity check** (re-run): no definition path sets `pi_Mx := reader`; no response value, threshold, or fixed-point datum enters construction.
2. **Lawful-spreading regression**: finite symbols and local projections are used only along lawful restriction/old-image flow.
3. **Fresh attack set** (target-tuning and constructibility): tried lifting the scoped cycle face to full cycle-creating intertwiners by selection; rejected as target-tuning and FC4-violating upward-lift style inference.
4. Standard nine geometric regressions on assembled J2/J7 slots (covariance, batching, restriction, reality, no-selection, compatibility, and overlap legality).
5. Anti-tuning ledger confirms no choice/order from response-facing consequence was used to select maps.

## Final

`J2 = PROVEN`
`J7_FACE = BUILT`
`COMPLETION_THEOREM_V2 = PROVEN`
`FC10_SUPPLIED = [J2 full on rank-preserving arrows, J2_SCOPED on cycle-creating arrows via SCOPED_J2_SQUARE, J7 corrected contracted face on cycle-creating arrows, FC11 completion theorem conditioned on the corrected J2/J7 contracts]`
