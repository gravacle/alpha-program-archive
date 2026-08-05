# STAGE8_TASK5_EQ6_DIAMONDS_REVIEW_LANE1_V001

## Register context
- Register head: **Q-478**.
- Scope: review of Lane-2 artifact `STAGE8_TASK5_EQ6_PARTIAL_JOINT_DIAMONDS_LANE2_V001.md` (SHA-verified before reading) against the confirmed stage-1 face family and the scoped mate certificate already available in Lane-1.

## U1 · Partial term check
- [PROVABLE] I recomputed two common-refinement diamonds directly from the confirmed constructions, not from renamed look-alikes: the **composition diamond** and the **bottom-naturality diamond**.
- [PROVABLE] Composition diamond (rank/cycle transport): using Lane-1 Stage-1 formulas `(C1-12)` and `(C1-13)` and the functorial summary `(C1-14)`, the path equality for overlap composites is:
  - `F_fin(gf)=F_fin(g)F_fin(f)` and `i_(gf)^Y = i_g^Y i_f^Y`, `j_(gf)^H = j_g^H j_f^H`, `S_(gf)^J = S_g^J S_f^J`, `~(gf)=~g~f`, with `rho_(gf)^* = rho_f^* rho_g^*` coordinatewise.
  - This closes the rank-preserving transport diamond and propagates to disjoint/flip finite-bottom faces exactly as the reviewed artifact states.
- [PROVABLE] Bottom-naturality diamond: using `(C2-4)` and the same functorial splitting, we have `rho_n^pkg o F_fin(f) = Bot(f) o rho_m^pkg` and similarly for Hessian, contact, C2, and C3 components. This is a genuine overlap-square face of the finite package and matches the claimed five-component closure.
- [PART-PROVABLE] The five named components (Face, finite bottom, J4, J12, J15) are jointly consistent in this two-diamond check; the remaining component-level route names are present in the file but not independently expanded into fully drawn six-cell pastings here.

## U2 · Contact cocycle through A4 pushout
- [PROVABLE] The file’s A4-corrected overlap uses the same contact-cocycle class as the confirmed stage-1 construction, with the explicit `OLD_FID + RNL + LR` compatibility stack and no drift in the new-cycle sector.
- [PROVABLE] From `(C1-7)` in the confirmed package, the contact defect term `β_f := rho_f^C2(C2_m^fin)-C2_n^fin` vanishes on old-image (`β_f=0`), and `(C1-9)` preserves Ward; combined with `(C2-4)` this gives preservation across a nontrivial overlap in the overlap square the artifact labels as A4-relevant.
- [PROVABLE] Hence the cocycle is transported in the same old-image regime required by scope, so this item is not introducing extra structure beyond what the finite assembly already licensed.

## U3 · J2/J7 contract (D2) against scoped mate
- [PROVABLE] `D2` in the reviewed artifact states the J2 slot with full reader/composite framing (`ell_N := pi_Mx,N ∘ Loc_N ∘ Kernbar_N ∘ Q_N`) and naturality as if a full physical `I_F`/Delta intertwiner were directly consumable on cycle-creating arrows.
- [PROVABLE] My scoped mate certificate proves the **minimal consumed demand** for cycle-creating arrows as the projected old-image square (labelled `SCOPE_MATCHED`):
  - `r_f^Bot ∘ pi_Mx,M ∘ Loc_M ∘ η_f = pi_Mx,N ∘ Loc_N`.
- [PROVABLE] Therefore `D2` as written over-demands by importing the blocked full square (`rho_f ∘ delta = delta ∘ rho_f`) into the cycle-creating class.
- [PART-PROVABLE] Physical reading: that over-demand would force every cycle-creation class to carry uncompromised Maxwell-image transport, i.e., no scope-limited suppression of harmonic leakage, contradicting the previously established cycle-creation obstruction mechanism.
- [PROVABLE] Corrected contract clause for this review lane: replace the cycle-creating J2 face in `D2` by `SCOPED_J2_SQUARE` exactly as above; keep the full `J2` intertwiners in the non-cycle subdomain only.

## U4 · Completion theorem (D3)
- [PROVABLE] I find no additional six-component simultaneity clause hidden in the finite assembly beyond the standard transport-and-contact families already audited in Stage-1.
- [PROVABLE] The only structural blocker in the reviewed completion step is `D2`’s contract width: with corrected scope, D3 is conditionally aligned; with uncorrected `D2`, D3 inherits a contract-overdemand gap.
- [PART-PROVABLE] No further new coherence failure was found from the partial diamonds alone.

## U5 · Fresh attack (new)
- [YOURS] Test attempt: inject the full `Δ`-intertwiner demand on cycle-creating arrows by substituting `r_f^Bot ∘ ell_M = ell_N ∘ r_f^{I_F}` into the overlap family. The attempt derives a forbidden upward lift step in the old-image branch, violating FC4 (downward/mate-only flow), so the injection is rejected as a structural move, not a mere bookkeeping miss.

PARTIAL_DIAMONDS = CONFIRMED (+C1-14 and C2-4 applied on two explicit common-refinement diamonds)
CONTRACT = OVER-DEMANDS (+corrected contract: replace cycle-creating J2 face in D2 with `r_f^Bot ∘ pi_Mx,M ∘ Loc_M ∘ η_f = pi_Mx,N ∘ Loc_N`; retain full `rho ∘ Δ` as non-cycle domain condition)
COMPLETION_THEOREM = GAP (+D2 over-demands full J2 in cycle sector; D3 closure needs corrected contract before final pass)
