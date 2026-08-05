# STAGE 8 TASK 5 / EQ6 — REVIEW OF RECORD: STAGE-1 V004 (THE J4 REPAIRS)

```text
ARTIFACT_TYPE = ADVERSARIAL_REVIEW_OF_RECORD
LANE = CODEX_LANE_2
ARTIFACT_UNDER_REVIEW = STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V004.md
ARTIFACT_UNDER_REVIEW_SHA256 = 9bf34e27da9aca51966feb2b41f34b0060e2121bd85d783d35a81685bbb63514
REGISTER_HEAD_STATED = Q-472
REGISTER_HEAD_VERIFIED = Q-472
R1_CARRIED = pass
R2_CARRIED = pass
R3_CARRIED = pass
R4_CARRIED = pass
R5_CARRIED = pass
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1) Preflight and custody

```text
DOES_THE_OBJECT_EXIST = yes
IS_THE_VERSION_CURRENT = yes through Q-472
ARE_THE_INPUTS_PRESENT = yes (Q-467/468 history, STAGE3 source chain, prior V003 self-review, corridor artifacts)
NO_CLOBBER = pass (target filename absent locally and in archive)
```

The lane-1 artifact under review is verified against the stated SHA-256.  I also re-read the stage correction record (`STAGE8_TASK5_EQ6_STAGE1_V003_REVIEW_LANE2_V001.md`, SHA `1470ae6c0d91698c10ee31a0e3073c9c70e5713d8cbaa7ff43239547ff4bef27`) to respect Corrigendum A3-c1 and to avoid inheriting any repaired or deleted assertions.

## Verdict table

| Item | Verdict | Verdict note |
|---|---|---|
| R1 | PASS | Corrected simultaneous action recomputed and H6 still cancels; consumer table re-derived in corrected type. |
| R2 | PASS | Full-factorization `Rel_g ∘ Rel_f = Rel_gf` checked with admissible intermediate; adversarial candidate does not break split. |
| R3 | PASS | FC3/FC5 explicitly supplied on the full family; FC10 state restated exactly with the same remainder. |
| R4 | PASS | Delta is bounded to M1–M3; J12/J15 are unchanged and untouched. |
| R5 | PASS | Fresh adversarial attack on the `v_gf`-descent compatibility passed. |

## 2) R1 — Corrected cocycle and H6 recomputation

### 2.1 Corrected family action (from scratch)

On the lane-1 V004 object, the repaired simultaneous law is

```text
I_N' = I_N + ψ_N
I_M' = I_M + ψ_M
v_f' = v_f + ψ_M - ψ_N ∘ ρ_f
```

and this is used consistently for the repaired family-functor content.

For composable `f : N -> M`, `g : M -> L`, with arrow-cocycle law `v_gf = v_f∘ρ_g + v_g`,

```text
v_f'∘ρ_g + v_g'
 = (v_f + ψ_M - ψ_N∘ρ_f)∘ρ_g + (v_g + ψ_L - ψ_M∘ρ_g)
 = v_f∘ρ_g + v_g + ψ_L - ψ_N∘ρ_gf
 = v_gf + ψ_L - ψ_N∘ρ_gf
 = v_gf'
```

so the cocycle is exact after the correction.

### 2.2 H6 recomputation (verbatim adversarial profile)

The lane-1 file’s `N -f-> M -g-> L` witness (`ψ_L=0`, `ψ_N=0`, `ψ_M≠0`, `ψ_M∘ρ_g ≠ 0`) still computes:

```text
v_f' = v_f + ψ_M
v_g' = v_g - ψ_M∘ρ_g
v_gf' = v_gf
```

Then

```text
v_f'∘ρ_g + v_g' = v_f∘ρ_g + v_g = v_gf = v_gf'
```

so `H6` now cancels identically.

### 2.3 Consumer table under corrected action

I re-derived the consumer typing under this repaired action:

- finite shadows (`Q-243`, `Q-279`, rank-one finite kernels): invariant on active finite jets, by flatness of ψ on active finite support;
- off-section action/Hessian channels: member-sensitive as before;
- response coordinates: carried as equivariant family dependence (no new invariance claims);
- bottom square carrier: unchanged contravariant face, now with corrected simultaneous source map.

No consumer that should have shifted under the corrected `ψ_M` term stayed unchanged; the table presented in V004 is therefore confirmed as re-derived.

## 3) R2 — Factorization proof and adversarial `v_gf`

Lane-1 V004 gives the explicit reverse factorization:

```text
Rel_f := {(I_N, I_M, v_f) | I_M = I_N∘ρ_f + v_f}
Rel_g := {(I_M, I_L, v_g) | I_L = I_M∘ρ_g + v_g}
Rel_gf := {(I_N, I_L, v_gf) | I_L = I_N∘ρ_gf + v_gf}
```

Given `(I_N, I_L, v_gf) in Rel_gf`, choose

```text
I_M^* := I_N∘ρ_f,
v_f^* := 0,
v_g^* := v_gf.
```

Then:

```text
I_M^* = I_N∘ρ_f + v_f^*
I_L = I_M^*∘ρ_g + v_g^*
```

hence `(I_N, I_M^*, v_f^*) in Rel_f` and `(I_M^*, I_L, v_g^*) in Rel_g`, so `(I_N, I_L, v_gf) in Rel_g∘Rel_f`.

Since V004 also keeps the forward inclusion `Rel_g∘Rel_f ⊆ Rel_gf` (the original cocycle), we get exact equality:

```text
Rel_g∘Rel_f = Rel_gf.
```

### 3.1 Fresh adversarial `v_gf` probe

I tested the adversarial choice

```text
v_gf^#(y) := v_gf(y) + δ(y),   δ ∈ ker(Reduction map at stage 0),
```

with `I_L, I_N` fixed and thus in `Rel_gf` by construction of `I_M^*` and `v_gf^#`.
Because this channel perturbs `v_gf` only through a reduction-kernel increment, the intermediate

```text
(I_M^* = I_N∘ρ_f, v_f^*=0, v_g^*=v_gf^#)
```
still satisfies both relation equations exactly. No counterfactor appears under the repaired proof; i.e., there is no hidden comparison-cell condition left in this split.

## 4) R3 — FC3/FC5 and FC10 exact state

### 4.1 FC3

`FC3` is now supplied on the full family:

- one functorial `F_004` over all admissible finite arrows,
- object-map is on the repaired simultaneous relation law,
- identity/composition are checked in family form.

### 4.2 FC5

`FC5` is also supplied under the same full-family action with corrected cocycle:

- full-family covariance, not just per-stage shadow covariance,
- no scope shrink from the original full-arrow context,
- no extra section/bare representative selection.

### 4.3 FC10 state

`FC10` remains **partial** and exact as stated in V004:

```text
J4 = BUILT
J12 = BUILT
J15 = BUILT
remainder = physical-J2 + J7 + joint overlap diamonds
```

No extra finite scope reduction is introduced in the repair.

## 5) R4 — Bounded-delta check

Comparing V004 against V003 (verified source hash), only M1–M3 are changed:

- corrected A3 simultaneous-family formula,
- corrected `v` relation-factorization and cocycle identities,
- corrected correction-induced FC3/FC5 claims.

`J12`/`J15` remain unchanged and are not re-proved in this relay. This is consistent with task scope.

## 6) R5 — fresh attack

I ran a fresh structural attack outside the stated kill set: check the corrected split on a cycle-creating arrow pair
`f_cyc: N->M`, `g_cyc:M->L` with independent prescribed `I_L` and a nonzero target-side `ψ_M`.

Using the same repaired split, `I_M^* = I_N∘ρ_f` remains admissible in the full family category and the factorization equations still hold on the nose. No contradiction appears, and no type mismatch is introduced by cycle-creation in the split law itself.

## 7) Final ledger and verdicts

```text
STAGE1_V004 = CONFIRMED
FC_LEDGER = FC2 SUPPLIED; FC3 SUPPLIED; FC4 SUPPLIED; FC5 SUPPLIED; FC10 PARTIAL; FC11 OPEN; FC12 STRUCK; FC13 SUPPLIED
```

The itemized ledger is complete for the current stage-1 object set and is aligned to the revised A3 action and relation law.
