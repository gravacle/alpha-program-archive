# STAGE 8 TASK 5 / EQ6 — REVIEW OF RECORD: THE SCOPED MATE CERT, AND THE J2-SCOPE ADJUDICATION

```text
TASK = Q-478
LANE = CODEX_LANE_2
ARTIFACT_TYPE = PASS/KILL REVIEW (SCOPED_MATE)
REGISTER_HEAD_CHECKED = Q-478
CONDITION_TAG = [EQ6]

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
NO_MEMBER_SELECTION = yes
NO_FIXED_POINT_OR_THRESHOLD_OR_END_TEST = yes
NO_NUMERIC_EVALUATION = yes
NO_MEMBER_BOUNDING = yes
```

## 0. Preflight and verification

- `alpha-program-archive/workspace/STAGE8_TASK5_SCOPED_MATE_CERT_LANE1_V001.md` was verified at SHA-256 `088eccd9ee642fcffb83e9f1ef1bb64ef479fd68534a6f3fb55d6aebce1393ce` before reading.
- The required sidecar in the archive and local workspace matched that hash.
- The output filename did **not** preexist in the workspace.
- Authorities listed in the user preflight were hash-verified in this review run:
  - `STAGE8_TASK5_EQ6_PHYSICAL_J2_LANE2_V001.md` (`3fd4b924ec1a70f3e730bcf99f406d697c53937b26467d2ae6d5aa8c1bb6822c`)
  - `STAGE8_TASK5_CERT_V003_REVIEW_LANE2_V001.md` (`32129c4df96f3767f81ffcff88dc62c6101a0e40e8beeef4a91afe0f18e97ae4`)
  - `STAGE8_TASK5_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V003.md` (`a46beae26048a0d093de339363fb8597d362a0101d103cfc06305edabac53f4c`)
  - DoR-020-A5 file (`5beccc617f4c5f5f76aba777c664f3dd4393f72257fc850950e2246109a7a424`)

I used only the reviewed lane-1 artifacts and the sealed lane-2 counter-file; no new physical maps, completion assumptions, or numerical evaluation were introduced.

## 1. Register sweep (scope)

Swept and checked before analysis:

- Q-255, Q-397–Q-400, Q-407, Q-408, Q-409, Q-415, Q-424, Q-455, Q-456, Q-462, Q-477.
- `STAGE8_TASK5_EQ6_DETERMINATION_MAP_LANE1_V001.md`, `STAGE8_TASK5_CONTINUUM_PACKAGE_CONSTRAINT_ARM_LANE1_V001.md` (source of ratified FC10 form), `STAGE8_TASK5_JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V001.md`, `STAGE8_TASK5_SCOPED_MATE_CERT_LANE1_V001.md`, `STAGE8_TASK5_J2_*` lane-2 files.

## T1 — V2 derivation re-check

`STAGE8_TASK5_SCOPED_MATE_CERT_LANE1_V001.md` claims a three-step derivation:

1. **A5 harmonic descent on the reduced contact part**
   - Input: `[E_C,N, Δ_Hdg,N] = 0` from DoR-020-A5, and its restriction compatibility.
   - This indeed gives a lawful descent of `P_H` on the old-image contact subspace under admitted restrictions.

2. **Projection through `Loc`**
   - Lane-1 route composes the A5 descent with the already-built finite localization and the `Loc`/`Loc`-shadow structure in scope.
   - This is valid on the admitted old-image component; no hidden section is introduced.

3. **Composition with `J15` pair (`r_f^Bot`, `η_f`)**
   - Uses the one-functor package bottom from `STAGE8_TASK5_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V003.md` on cycle-creating generators.
   - The `SCOPED_J2_SQUARE` (and equivalent `SCOPE_MATCHED`) is exactly the stated projected mate:
     
     `r_f^Bot ∘ pi_Mx,M ∘ Loc_M ∘ η_f = pi_Mx,N ∘ Loc_N`.

**Result T1:** PASS (the derivation is syntactically and typedly coherent on confirmed objects).

### Itemized T1 check against inputs

- A5 commutator input is present and proved.
- `r_f^Bot` and `η_f` are available on cycle-creating arrows through `OLD_FID`-licensed old-image restriction.
- The projection appears in the `P_H` slot only (the open cycle component is not used, and not introduced).

## T2 — Minimality claim (V1) and quantification check

Your own J2 attempt text (`3fd4b924…`) states the physical composite as:

`reader_N := pi_Mx,N ∘ Loc_N ∘ Kernbar_N ∘ Q_N`.

On a cycle-creating arrow, the lane-1 scoped construction replaces a full cycle-creating mate claim by:

`SCOPE_MATCHED : r_f^Bot ∘ pi_Mx,M^resp ∘ P_H,M ∘ Loc_M ∘ η_f = pi_Mx,N^resp ∘ P_H,N`.

This is a **strictly weaker scope** than the full J2 quantification, because it contains only the projected old-image/Δ-harmonic piece.

So the minimality claim is true only in this precise sense:
- from sealed current objects, one can *force* the projected mate law;
- the full cycle-creating Δ-intertwiner (`rho_f δ_M = δ_N rho_f`) and its full square are not derivable in the current stock and remain open.

No part of the scoped law forces the new-cycle component; but the full J2 formula in the unscoped statement does quantify over those components, if and only if `Loc_N` and `pi_Mx,N` are separately constructed.

**Result T2:** PASS-with-scope note — the lane-1 minimality claim is coherent only as a scoped weakening of full J2, not as an unqualified derivation from the full physical J2 formula.

## T3 — Scope adjudication (load-bearing item)

Tension (V1/V3) is resolved as follows:

- **Ratified FC10 form (from constraint arm):** `reader = pi_Mx ∘ Loc ∘ Kernbar ∘ Q` on the intended `I_F` scope, with no scoped projection baked in.
- **Current confirmable lane-1 form:** `SCOPE_MATCHED` on cycle-creating arrows, i.e. the old-image projected law only.

Therefore, the artifact’s V1 is best read as: 

**(a) J2_TRUE_SCOPE = SCOPED_FORM**, with explicit distinction that full cycle-creating Hodge-adjoint content is not yet a derived demand because the full left and right cycle-creating factors of J2 are missing.

Because this differs from ratified FC10 text, an amendment is required before lane-1 could be interpreted as strictly FC10-compliant.

### Proposed amendment text (typed)

`J2_SCOPED (cycle-creating arrows):` demand only
`r_f^Bot ∘ pi_Mx,M ∘ Loc_M ∘ η_f = pi_Mx,N ∘ Loc_N` on the admitted old-image/`P_H` sector,

while retaining the full `J2` equation as post-scope requirement on any arrow class where `Loc_N` and `pi_Mx,N` are independently constructed.

This is not a claim of physical truth of full J2; it is a staged compatibility contract and a guarded scope discipline.

**Result T3:** `AMENDMENT_PROPOSED` is needed; full-scoped J2 is not yet licensed on current inputs.

## T4 — Full square failure witness

Recomputing the witness from the physical-J2 attempt (`3fd4b924…`):

- reciprocal-loop profile `H_x` has nonzero `Kernbar_N(Q_N H_x)` via built Q-408 faithfulness;
- the algebraic reader evaluates this explicitly as `ell(Q_N H_x)= [f(r^2)+2r^2 f_1(r^2)] chi_N` (nonzero in general);
- `Loc_N` into a Maxwell/contact local symbol and `pi_Mx,N` on that codomain are not independently built.

Hence the full J2 map `pi_Mx,N ∘ Loc_N ∘ Kernbar_N ∘ Q_N` is currently not a formed composite on `I_F` (the right half is absent), so equality `reader = ...` cannot be proven or disproven at map level. This is exactly the reciprocal-loop stop from `3fd4b924…`.

This is not an algebraic artifact of wrong scalarization under `scope`—it is a structural absence in the physical factorization chain.

**Result T4:** `FULL_SQUARE_FAILURE = GENUINE_PHYSICS` (constructibility boundary, not a circularity-only artifact).

## T5 — Fresh attack

**Attack:** Assume full J2 were to remain equivalent to the scoped law on the same data (i.e. try to infer full cycle-creating `pi_Mx/Loc` content from `SCOPE_MATCHED` by choosing a lifting/selection of new-cycle coordinates).

**Result:** fails. `SCOPE_MATCHED` only constrains the projected old-image block; any lift choice for the new-cycle block is unconstrained by the scoped law, so this would be target-tuning/selection by definition. The physical file `3fd4b924…` confirms that such a lift would amount to defining `pi_Mx` from reader data (`F_PLDEC` circularity class), which is forbidden.

## Verdict table

- **T1. V2 derivation:** PASS (reconfirmed)
- **T2. V1 minimality:** PASS-with-scope note (true only under scoped carrier projection)
- **T3. Scope adjudication:** option **(a)** selected (scoped form is the licensed current content)
- **T4. Failure witness:** PASS (structural witness reproduced)
- **T5. Fresh attack:** PASS (no target-tuning route)

## Final lines

`SCOPED_MATE = CONFIRMED`

`J2_TRUE_SCOPE = scoped_form (+full J2 stays blocked on new-cycle factor until independent `Loc_N`/`pi_Mx,N` is supplied; scope contract is now explicit in T1/T2/T3)`

`AMENDMENT_PROPOSED = replace cycle-creating J2 with scoped projected law on old-image `P_H` sector; keep full J2 as post-scope condition pending full mate certificate`

`FULL_SQUARE_FAILURE = GENUINE_PHYSICS`
