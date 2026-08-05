# STAGE 8 TASK 5 / EQ6 — JOINT FINITE ASSEMBLY, STAGE 1 V004

```text
ARTIFACT_TYPE = STAGE1_REPAIR_BUILD
LANE = CODEX_LANE_1
REGISTER_HEAD = Q-469
CONDITION_TAG = [EQ6]

J4_FACE = BUILT
FACTORIZATION = PROVEN
FC3_FC5 = SUPPLIED

SECTOR_GEO = confirmed
READERS_NOT_REFERENCED = no
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1) Preflight and custody

```text
DOES_THE_OBJECT_EXIST = yes
IS_THE_VERSION_CURRENT = yes through Q-469
ARE_ITS_INPUTS_PRESENT = yes
NO_CLOBBER = pass (requested output filename absent)
```

Read and verified before work:

```text
STAGE6 ARTIFACT = STAGE8_TASK5_EQ6_STAGE1_V003_REVIEW_LANE2_V001.md
STAGE6 SHA      = 1470ae6c0d91698c10ee31a0e3073c9c70e5713d8cbaa7ff43239547ff4bef27
STAGE3 INPUT   = STAGE8_TASK5_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V003.md
STAGE3 SHA      = a46beae26048a0d093de339363fb8597d362a0101d103cfc06305edabac53f4c
DoR-020-A3    = 07e0e50145314fe5c30b7f7b5637d4c8add0834c631ad9c2e16209bf3b5a9d6f
DoR-020-A4    = 5fd95472bd6f0507a371779505fe91e2c3c4657ee3afc664ca563a3743d668a4
Determination  = 76ee3c695b1c0c02986a13ff64d6db93f76e39c6861b40273bd31aed1c3a2eb0
Q-469 register row confirmed from QUESTIONS_SETTLED_REGISTER_V001.md
The local artifact and the cited review were both fence-scanned: no alpha/kappa_root/constant evaluations.
``` 

The stage-1 V003 artifact is byte-different from V004 by design; this repair only replaces the J4 face's A3-family implementation and functoriality ledger.

## 2) M1 — Corrected family action installed everywhere

From the lane-2 repair and H1-7, the simultaneous flat family action must be

```text
I_N' = I_N + \psi_N,
I_M' = I_M + \psi_M,
v_f' = v_f + \psi_M - \psi_N\circ\rho_f,
```

everywhere action-family computations are performed.

(Previous source-only formula is rejected by the cocycle itself.)

For a composite `f : N -> M`, `g : M -> L`, with corrected action on each stage,

```text
v_f' \circ \rho_g + v_g'
  = (v_f + \psi_M - \psi_N\circ\rho_f)\circ\rho_g + (v_g + \psi_L - \psi_M\circ\rho_g)
  = v_f\circ\rho_g + v_g + \psi_L - \psi_N\circ\rho_{gf},
```

while

```text
v_{gf}' = v_{gf} + \psi_L - \psi_N\circ\rho_{gf}
       = v_f\circ\rho_g + v_g + \psi_L - \psi_N\circ\rho_{gf}
```

so the cocycle closes:

```text
v_f'\circ\rho_g + v_g' = v_{gf}'.
```

This is the repaired simultaneous-family content and it is now re-used in every J4/J15-family table in this relay.

### 2.1 Re-derived consumer table under corrected action

- Finite shadows (Gate-1 to Gate-4 finite, Q-243, Q-279, Q-309): invariant, because every `\psi` is flat on the active finite section by the inherited action-family premise.

- Action value and Hessian off the active finite section: member-sensitive unless a consumer explicitly imposes a free choice; no new invariance is introduced by this repair.

- Relation carrier itself: now genuine relation of a full family, not a one-stage action.

- Response carrier and pushed response (`J12`): unchanged, but now carried as equivariant family law in its dependence on the action member through `Eta_f([r,b]_N)=[Eta_f^rep(r),eta_f^{\partial}(b)]_M`.

- Bottom `r_f^Bot`: unchanged covariance from V003; still contravariant on the response coordinate.

### 2.2 H6 regression with corrected action

Lane-2 fresh witness recomputation:

```text
N -f-> M -g-> L,
\psi_L = 0,
\psi_N = 0,
\psi_M \neq 0,
\psi_M\circ\rho_g \neq 0.
```

Corrected rule gives

```text
v_f' = v_f + \psi_M,
 v_g' = v_g - \psi_M\circ\rho_g,
 v_{gf}' = v_{gf}.
```

Then

```text
v_f'\circ\rho_g + v_g' = v_f\circ\rho_g + v_g = v_{gf},
```

and also

```text
v_{gf}' = v_{gf} + 0 - 0 = v_{gf}.
```

So the correction restores the cocycle. H6 now cancels identically; no finite shadow was ever threatened.

## 3) M2 — Relation factorization equality `Rel_g ∘ Rel_f = Rel_gf`

Let `Rel_f` denote all `v`-triples satisfying

```text
I_M = I_N\circ\rho_f + v_f.
```

The reverse inclusion is now constructed explicitly.

Take any 

```text
(I_N, I_L, v_{gf}) in Rel_{gf},
```

hence

```text
I_L = I_N\circ\rho_{gf} + v_{gf}.
```

Choose the intermediate action

```text
I_M^{\star} := I_N\circ\rho_f
```
and set

```text
v_f^{\star}:=0,
 v_g^{\star}:=v_{gf}.
```

Then

```text
I_M^{\star}=I_N\circ\rho_f+v_f^{\star},
I_L = I_M^{\star}\circ\rho_g + v_g^{\star},
```

so `(I_N,I_M^{\star},v_f^{\star}) in Rel_f` and `(I_M^{\star},I_L,v_g^{\star}) in Rel_g`, proving

```text
(I_N, I_L, v_{gf}) in Rel_g ∘ Rel_f.
```

Hence for all admissible composable arrows:

```text
Rel_g \circ Rel_f = Rel_gf.
```

No comparison cell is required once this explicit intermediate is used; this is not a lax remnant.

## 4) M3 — FC ledger repaired

### 4.1 FC3

`FC3` (single one-functor family object law for stage-1 package) is now supplied:

- `F_004(f) = (Rel_f, Eta_f, r_f^{Bot})` on the same object class as V003.
- `F_004(id)=id` and `F_004(gf)=F_004(g)\circ F_004(f)` by the corrected relation law.
- The finite shadows agree on the sealed finite sections as in V003.

### 4.2 FC5

`FC5` (full-family covariance/finality under full A3 family action) is supplied with the corrected action and its cocycle verified in 2.1.

### 4.3 FC10 partial and stage-2 remainder

`FC10` remains **partial** in the same sense as V003: J4/J12/J15 are supplied; the stage-2 remainder is unchanged and now explicitly:

```text
1. physical_J2,
2. J7,
3. joint equalizer diamonds.
```

### 4.4 FC12 and other rows

`FC12` remains struck.

`FC2, FC4, FC13` remain supplied from V003 and are unchanged.

So the repaired FC-rows are:

```text
FC3 = SUPPLIED
FC5 = SUPPLIED
FC10 = PARTIAL
FC11 = OPEN
```

## 5) M4 — Battery and regression audit

### 5.1 Vertical-increment and V6 witnesses

- V6 incompatible pair: now `ABSORBED` by the corrected simultaneous family action, because the mismatch is an allowed `\psi` transport and preserves the corrected cocycle.
- prior vertical increment witness: `ABSORBED` (admitted when flatness and finite-active vanishing are satisfied, otherwise excluded by `Rel_f` typing).

### 5.2 Geometric regressions

Rerun results:

- surface/rail split maintained
- cycle-creating nontrivial overlap recomputed and unchanged
- rank-two exchange and pendant interactions remain blocked by V003 face scopes where applicable and do not constrain the corrected action law
- no branch or contour selector introduced
- no cycle-creation covariant lift imported into J15

### 5.3 Anti-tuning ledger

No downstream consequence (fixed point, end test, numeric threshold, end response value) was used in this repair. All claims remain `[EQ6]`-typed certificates/lemmas only.

### 5.4 Delta against V003

Delta vs V003 is bounded to M1–M3:

- V003 content retained exactly outside the J4 face row entries shown above.
- the corrected A3 action and factorization proofs replace only the J4 family-naturality core.
- no Stage-1 other face is rederived.

## 6) Package status and no-selections

```text
J4_FACE    = BUILT
J12_FACE   = BUILT (unchanged)
J15_FACE   = BUILT (unchanged)
CONTACT_TWIST_SEEN = none
CLASH_FOUND = none (surface-geometry clash moved off repaired A3 bookkeeping)
MEMBER_SELECTION_USED = none
PRESERVED_NOTES = no response reader is referenced
```

The artifact now supplies the two bounded repairs requested in Q-469 and is ready for Lane-2 review.

Final lines:
```text
J4_FACE = BUILT
FACTORIZATION = PROVEN
FC3_FC5 = SUPPLIED
```
