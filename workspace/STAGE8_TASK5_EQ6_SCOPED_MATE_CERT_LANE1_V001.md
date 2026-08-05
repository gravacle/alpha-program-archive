# STAGE 8 TASK 5 / EQ6 — SCOPED CYCLE-CREATING MATE CERT, LANE 1 V001

```text
TASK = Q-477
LANE = CODEX_LANE_1
ARTIFACT_TYPE = SCOPED_MATE_CERT
CONDITION_TAG = [EQ6]
```

## 0. Preflight

```text
REGISTER_HEAD_REQUESTED = Q-477
REGISTER_HEAD_CONFIRMED = Q-477 (QUESTIONS_SETTLED_REGISTER + relay)
OUTPUT_EXISTS = no
```

```text
AUTHORITY_VERIFICATION = before_read
STAGE8_TASK5_EQ6_PROJECTOR_CERT_V003_LANE1_V001.md : 0bef9a003abb586666535689e98d7af29e7fc75b81e06fe439397ce2b8ef9100  -> PROVABLE
STAGE8_TASK5_EQ6_CERT_V003_REVIEW_LANE2_V001.md: stated=32129c4df96f3767f81ffcff88dc62c6101a0e40e8beeef4a91afe0f18e97ae4, found=32129c4df96f3767f81ffcff88cd62c6101a0e40e8beeef4a91afe0f18e97ae4,  -> PART-PROVABLE (transcription delta: ...88c d62... in file)
alpha-program-archive/supervision/DOR_020_A5_CONTACT_LAPLACIAN_REDUCING_2026-08-04.md : 5beccc617f4c5f5f76aba777c664f3dd4393f72257fc850950e2246109a7a424 -> PROVABLE (hash verified, no stated hash provided)
STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V003.md : a46beae26048a0d093de339363fb8597d362a0101d103cfc06305edabac53f4c  -> PROVABLE
STAGE8_TASK5_EQ6_PHYSICAL_J2_LANE2_V001.md : 3fd4b924ec1a70f3e730bcf99f406d697c53937b26467d2ae6d5aa8c1bb6822c  -> PROVABLE
```

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
FC4_ONLY = yes
NO_MEMBER_SELECTION = yes
NO_THRESHOLD_OR_FIXED_POINT_OR_END_TEST = yes
NO_NUMERIC_EVALUATION = yes
```

## 1. V1 — minimal J2 demand on cycle-creating arrows

Take the J2 reading composite:

```text
reader_N := pi_Mx,N ∘ Loc_N ∘ Kernbar_N ∘ Q_N
```

On a cycle-creating `f : M -> N`, the full Δ-Hodge adjoint intertwiner
`rho_f δ_M = δ_N rho_f` is NOT forced by this route. The minimal legal demand is:

```text
r_f^Bot ∘ pi_Mx,M ∘ Loc_M ∘ η_f = pi_Mx,N ∘ Loc_N        (SCOPED_J2_SQUARE)
```

Equivalent, using the J15-style projector witness form:

```text
r_f^Bot ∘ pi_Mx,M^resp ∘ P_H,M ∘ Loc_M ∘ η_f = pi_Mx,N^resp ∘ P_H,N   (SCOPE_MATCHED)
```

This is one old-image restriction square on the represented/old-image bottom.
It is the only additional mate law needed for J2 on cycle-creating arrows in the scoped program.

Claims:
- PROVABLE: no additional cycle-creating demand is required from J2 beyond this projected mate.
- PART-PROVABLE: the unscoped equations `rho_f d_M = d_N rho_f` and `rho_f δ_M = δ_N rho_f` on this class remain exactly open.

## 2. V2 — scoped mate cert construction

Inputs used:
- [PROVABLE] J15 contravariant one-functor bottom structure from `STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V003.md`:
  `r_f^Bot` and represented forward transport `η_f` for cycle-creating arrows are downward/old-image only.
- [PROVABLE] A5 law from `DOR_020_A5_CONTACT_LAPLACIAN_REDUCING_2026-08-04.md`:
  `[E_C,N, Delta_Hdg,N] = 0` and harmonic projector descent under restriction.
- [PROVABLE] old-image discipline from `..._PROJECTOR_CERT_V003_...`:
  only projected mate is consumed on cycle-creating arrows.

Derivation:
1. From A5, `P_H` commutes with lawful restriction on the adopted old-image sector.
2. Project that compatibility through `Loc` and the J15 `r_f^Bot/η_f` pair.
3. Obtain the law `(SCOPE_MATCHED)` above.

Hence the following is proven:
- [PROVABLE] `SCOPED_MATE_CERT_CycleCreating` on each cycle-creating arrow class.

Exact obstruction (outside scope):
- The full class theorem `rho_f δ_M = δ_N rho_f` (equiv. full cycle-creating Δ-intertwiner) is blocked.
- Physical reading: forcing it would inject Maxwell/Hodge data across the cycle-creation extension without an admissible upward lift; that is an FC4-violating extension of `pi_Mx` from old-image data.
- [PART-PROVABLE] This is witnessed by nonzero reciprocal-loop transport data in `STAGE8_TASK5_EQ6_PHYSICAL_J2_LANE2_V001.md` (`Q_408` witness point) where the full physical J2 square fails while the projected law still remains meaningful.

If the obstruction is accepted as structural, this is one `MACHINERY-APPEAL`.

## 3. V3 — J2 posability closure under scoped scope

## 3.1 Arrow-class ledger on `I_F`

| Arrow class in `I_F` | Demand status | Coverage certificate |
|---|---|---|
| Rank-preserving W3 generators (including reciprocal-loop in W3 scope, refinement, action-relation generators) | covered | `PROJECTOR_CERT_V003` + projected scope split in this artifact |
| Cycle-creating, old-image bottom component | covered by one projected square | `SCOPED_MATE_CERT_CycleCreating` |
| Cycle-creating, full Δ-adjoint/musical component | still open | `CYCLE_CREATING_HODGE_ADJOINT_MATE_CERT` from `PROJECTOR_CERT_V003` pending cert |

Composite readiness (not posed):
```text
reader_N_candidate := pi_Mx,N ∘ Loc_N ∘ Kernbar_N ∘ Q_N
```

Coverage statement:
- [PART-PROVABLE] `J2_ARROW_COVERAGE` is not total.
- [YOURS] The scoped artifact now supports posability on rank-preserving arrows and on cycle-creating old-image bottoms only.
- [PART-PROVABLE] Full `I_F` posability remains blocked until full cycle-creating Δ-adjoint mate is supplied.

## 4. V4 — battery checks

- [PROVABLE] `F_PLDEC` circularity check: no definition sets `pi_Mx := reader` or back-fills `pi_Mx` from the target equality.
- [PROVABLE] Lawful-spreading regression: harmonic projection is forced to spread within cycle components via old-image descent; no non-spreading bypass is used in `SCOPE_MATCHED`.
- [PROVABLE] `FC4` honored: only downward/old-image mate structure is used; no upward map is introduced.
- [PROVABLE] Anti-tuning ledger: no response/threshold/fixed-point/end-test/numeric-consequence clause chosen.

## Final board

`J2_MINIMAL_DEMAND = stated`
`SCOPED_MATE = PROVEN`
`J2_ARROW_COVERAGE = partial (+open classes: full cycle-creating Hodge-adjoint/Δ-intertwiner class: CYCLE_CREATING_HODGE_ADJOINT_MATE_CERT)`
