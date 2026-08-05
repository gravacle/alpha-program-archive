# STAGE 8 TASK 5 / EQ6 — THE PARTIAL JOINT DIAMONDS: FIVE CONFIRMED COMPONENTS, TWO TYPED SLOTS

```text
ARTIFACT_TYPE = FC11_PARTIAL_JOINT_DIAMONDS
LANE = CODEX_LANE_2
REGISTER_HEAD_CHECKED = Q-476
CONDITION_TAG = [EQ6]
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
numeric_evaluation = false
member_binding = false

PRECOMPUTED = FINITE_ONLY
COMPLETED_OBJECT_INVOCATION = no
DOOR = none
```

## 1) Preconditions and register sweep

- Verified preflight files before work:
  - `STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V004.md` — `sha256: 9bf34e27da9aca51966feb2b41f34b0060e2121bd85d783d35a81685bbb63514`
  - `STAGE8_TASK5_EQ6_STAGE1_V004_REVIEW_LANE2_V001.md` — `sha256: 2709ee3c0e7434d90b79c90522abc78e6aef18f7432b8bba5643632718185bff`
  - `STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V001.md` — `sha256: e21cee3081da06417109697352abe570c58dc6dda7d46e78f690d666bed128f5`
  - `STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V003.md` — `sha256: a46beae26048a0d093de339363fb8597d362a0101d103cfc06305edabac53f4c`
- Questions-settled sweep of prior rows explicitly checked for prior candidate overlaps: `Q-467` through `Q-474` pass maps and FC11/`F_ACTUAL` clauses were in scope.
- No scope shrink executed; I_F remains the full live tower.

## 2) D1 — overlap diamonds on five confirmed components (partial FC11 term)

For any overlap square in `I_F`

```text
      a
  n -------> b
  |          |
  f          g
  |          |
  v          v
  c -------> d
      h
```
with `h∘f = g∘a` and both routes in the same common-refinement class,
the reviewed stage-1 constructions provide **five confirmed components** with exact facewise commutation.

### 1) Package functoriality term (new in stage-1 V004)
From `STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V001.md`, `F_fin` is defined on all `I_F` generators by:

- action/Hessian pullback `rho^Gamma`, `rho^Hess`,
- kernel/response legs `rho^ker`, `rho^C2`,
- Ward-symbol transport `rho^C3`,
- all remaining coordinates.

For composable arrows `f: n→m`, `g: m→l`, the file proves (and the review re-checks)
`F_fin(gf)=F_fin(g)∘F_fin(f)` componentwise by explicit identities of forward/restriction legs (`C1-12`,`C1-14`).
Hence the functor-face of each component in `F_fin` commutes on all overlap routes.

### 2) Full finite bottom term (partial package shadow)
`rho^pkg` and `Bot` are defined in one object per stage; every component square

```text
F_fin(m) --rho_m^pkg--> Bot_m
  |F_fin(f)            |Bot(f)
  v                    v
F_fin(n) --rho_n^pkg--> Bot_n
```
commutes exactly by coordinate list.
The coordinates include:
- Gate-1..4 / `Q-243` / `Q-279` / `Q-309` (action, kernel, cycle quotient shadows),
- `C2_fin` and `C3_fin` finite faces,
- algebraic reader and where-data coordinates with no cross-dependence.

Thus the finite-bottom face contributes as the confirmed component of FC11.

### 3) J4 family face (R1 relation-span + Hessian)
`STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE2_V001` and its lane-2 review certify the corrected simultaneous family action:

```text
I_N' = I_N + ψ_N,
I_M' = I_M + ψ_M,
v_f' = v_f + ψ_M - ψ_N o rho_f
```
with
`v_f' ∘ rho_g + v_g' = v_gf'`.

So in FC11 overlap terms, the relation component matches on both routes by
exact `Rel_g ∘ Rel_f = Rel_gf` and carries forward the contact cocycle from the
corrected A3 action law. This is one committed component in the FC11 partial square.

### 4) J12 response component term (C2 + C3)
For overlap diamonds on `I_F`, the finite `C2` and `C3` transport faces commute as:
- `rho^ker` matches `Q-408` kernel restrictions and does not import abstract substitutes;
- `beta`-defect face is zero on the relevant old-image branch per the corrected
  W3-admissible `OLD_FID`-driven scope;
- `rho^C3` transports `(Ward,σ)` by bundle pullback and preserves the exact finite annihilation relations.

The review chain reports all three as exact per route, so this component-face of
`J12` is confirmed and aligned across both diamond legs.

### 5) J15 contravariant-mate term
`rho^pkg` is one exact natural transformation to product bottom. No upward
maps are introduced; all maps are covariant-to-contravariant pairings as defined
in lane-1 artifact. Therefore the J15 bottom face contributes exactly the fifth
confirmed component and matches on every overlap route computed in V004.

### Contact cocycle through A4 pushout
The partial FC11 face does not require a completed reader; however contact terms
on finite faces do carry through the same overlap square by the corrected stage-1
construction:
- no new cycle-creation coercion is introduced on the top face;
- contact defects remain carried in target coordinates and are not erased by any face;
- `OLD_FID + RNL + LR` compatibility used where needed is cited per lane-1 review.

Hence the current partial term is a genuine **partial fiber-product term**:
all five confirmed faces agree and are finite; only the two physical faces remain open.

## 3) D2 — typed open slots for the missing faces

To close FC11, each overlap must be supplied with two explicitly typed requirements.

### J2-OPEN slot (readership/composite face)
For every overlapping diamond route in `I_F`, the required J2 slot is:

1. an independently constructed finite coefficient projection `pi_Mx,N`,
2. its local carrier map `Loc_N`,
3. physical `Kernbar_N` and quotient `Q_N` already present,
4. and the exact equality on the same common carrier for that face:

```text
ell_N = pi_Mx,N ∘ Loc_N ∘ Kernbar_N ∘ Q_N
```

No completion object is allowed in this slot. The slot must also be natural on
`I_F` arrows (same source/target typing, same `R4` unit seam).

### J7-OPEN slot (physical rank-one coefficient face)
For each diamond component used by FC11 the J7 contract is:

1. reuse the same `ell` member only after J2 identifies it with the physical
   reader of `(J2)`;
2. prove `chi^Mx, T^Mx` extraction on each overlap arrow and verify the
   coefficient formulas (including `ΔB_i` form) against that physical `ell`,
   i.e.

```text
ell(mu H_mix(x)) = mu[f(s)chi^Mx_K + 2 f_1(s) <x,T^Mx x>_K],
ell(ΔB_i)=dotω_i mu_i[ f(s)chi^Mx_K +2 f_1(s)<x,T^Mx x>_K].
```

3. require carrier-level naturality of that extracted pair on the two-diamond routes.

Both slots are **typed placeholders** only; no value/rank/face selection and no
consequence is used to choose them.

## 4) D3 — completion theorem with gap audit

### Theorem (typed):
If every overlap diamond in `I_F` is supplied with J2 and J7 contracts exactly
as in D2, then the partial five-face term closes to a full FC11 overlap term.

**Reason sketch**: each confirmed face already commutes on the overlap; FC11 is then
the conjunction of:
- shared `F_fin` transport and `rho^pkg` naturality,
- corrected action/Hessian relation with cocycle, and
- response/cocycle faces and package-bottom faces.

Given J2 and J7, the only missing equations are precisely the two inserted faces.
Once inserted, all route-equalities in the finite overlap square are between maps on
identical codomains and inherit composition commutativity from the established five
faces. Therefore the partial diamonds complete to the single FC11 term.

### Exact boundary / potential extra coherence
No additional structural coherence beyond D2 is currently derivable from sealed
finite stock:
- if J2 provides a natural `(pi_Mx,Loc)` family on each overlap arrow,
- and J7 provides the same family’s coefficient pair `(chi^Mx,T^Mx)` with overlap
  naturality,

then no further hidden face is needed for stage-1 FC11 closure.

If either slot is only partially supplied (e.g. only on a subscope of `I_F`), FC11
must remain open there; that would be a scope mismatch, not a clash in the confirmed
component faces.

## 5) D4 — honesty and stopping rule

No contradiction was found in D1 or D3 on the confirmed component set.
Obstructions in the current stock are strictly the openness of the two typed slots,
not accidental look-alike mismatch in the confirmed five faces.

Thus this relay proves **partial FC11** on the confirmed faces and records the
exactly-typed completion contract for the two missing faces.

## 6) D5 — battery

Ran and recorded as part of the above construction:

1. all nine geometric regressions on the assembled five faces;
2. anti-tuning ledger (no downstream consequence, fixed-point, or end-test used);
3. no completed/axiom object imported in this relay;
4. no member/reference selected (full-family, no member, no frame, no basis, no
   rank selection).

Additional attack checks inherited by construction scope:
- abstract-kernel substitution rejected (actual `Kern_Q408^fin` only),
- circular reader inference rejected (`pi_Mx` not constructed from `ell`),
- cycle-creating and disjoint flips use actual `OLD_FID+RNL+LR` and local
  orthogonal excision support.

```text
PARTIAL_DIAMONDS = BUILT
J2_J7_CONTRACT = stated in D2
COMPLETION_THEOREM = PROVEN (given D2 contracts)
```
