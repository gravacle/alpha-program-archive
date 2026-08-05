# STAGE 8 TASK 5 / EQ6 — ADJOINT MATE CERT AND PROJECTOR CERT V003

```text
TASK = Q-471
CONDITION_TAG = [EQ6]
DOF3_HEAD = Q-471
L1 = built (with cycle-creating gap explicitly tagged)
L3-8 (CYCLE_CREATING_HODGE_ADJOINT_MATE_CERT) remains the exact unresolved gap
DoR-020-A5 = ADOPTED
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1. Lead result

```text
REGISTER_HEAD_CHECKED = Q-471
ARTIFACT_TYPE = DERIVE_LANE1
MATE_CERT = BLOCKED (cycle-creating adjoint lift square missing on non-well-defined operator scope)
CERT_V003 = BUILT
READER_REFERENCED = no
A5_VOID1_CHECK = clean_on_scope / WITNESS_FOUND
```

This relay executes a completion of the V002 projector program under the newly
adopted `[E_C,Δ^Hdg]=0` law. The finite Hodge operator is now fixed by
DoR-019+A5 on each admitted finite stage. The blocker that remains is not
contact reduction itself, but whether the full covariant Hodge intertwiner
`ρ_f δ_M = δ_N ρ_f` exists on all cycle-creating arrows in the same
strength as rank-preserving arrows.

## 2. Register sweep and preflight

I verified the following before drafting:

1. `alpha-program-archive/supervision/DOR_020_A5_CONTACT_LAPLACIAN_REDUCING_2026-08-04.md`
   (adopted exact law, SHA-checked).
2. `gravity_emergence_evidence_program/.../STAGE8_TASK5_EQ6_PROJECTOR_LOCALITY_REDUCING_CERT_V002_LANE1_V001.md`
   (the all-arrow gap `L3-8` was previously isolated).
3. `gravity_emergence_evidence_program/.../STAGE8_TASK5_EQ6_DETERMINATION_MAP_LANE1_V001.md`
   (provenance for the projected J15 mate and the cycle-creating mismatch).
4. `gravity_emergence_evidence_program/.../STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V003.md`
   (J15 contravariant face, no upward bottom lift).
5. `DOR_020_A1`, `DOR_019`, and the DoR stack entries in the questions-settled
   register through `Q-471`.

No evaluation of `alpha`, finite-point constants, or `q_*` occurred.

## 3. N1. The adjoint mate certificate

### 3.1 What is established at fixed finite stage
On every admitted finite stage `N`, DoR-019 and A5 give:

```text
delta_N := R_N^{-1} d_N^* R_N,
Δ_N^Hdg := d_N δ_N + δ_{N+1} d_N,
P_H,N := 1_0(Δ_N^Hdg),
[E_C,N, Δ_N^Hdg] = 0    (A5)
```

Hence `P_H,N` is the orthogonal harmonic/Maxwell projector in each finite stage.

### 3.2 Rank-preserving scope: full Hodge adjoint mate (lawful, proven)
For an admissible rank-preserving arrow `f: M -> N` in W3 scope with adjoint-restriction
structure `ρ_f = j_f^*` and `d_M j_f = j_f d_N`, the standard adjoint theorem gives

```text
ρ_f d_M = d_N ρ_f,
ρ_f δ_M = δ_N ρ_f,        (adjoint mate)
ρ_f Δ_M^Hdg = Δ_N^Hdg ρ_f,
ρ_f P_H,M = P_H,N ρ_f.
```

This yields the ordinary covariance square on rank-preserving arrows, including
the reciprocal-loop and refinement generators that are already in the adjoint scope.

### 3.3 Cycle-creating arrows: exact lawful comparison and exact gap
For a genuine cycle-creating arrow `f`, the sealed stock gives a downward
restriction and an honest no-upward-map theorem (FC4), but does not give the
second adjoint equation above on that class. The lawful replacement is therefore:

```text
r_f^Bot π_M^resp P_H,M Loc_M η_f = π_N^resp P_H,N        (L3-10)
```

where:
- `Loc` is the local-symbol map,
- `η_f` is the sealed forward transport,
- `π_*^resp` is the bottom/bulk projector in the one-functor model.

This is the **projected J15 comparison**: it compares the **old-image bottom**
entry only and is strictly downward only.

`L3-8` is the exact obstruction class:

```text
CYCLE_CREATING_HODGE_ADJOINT_MATE_CERT:
 ρ_f δ_M = δ_N ρ_f   on cycle-creating carriers.
```

Counterfactually, inserting an upward projector lift here would violate the
no-lift/contravariant-honesty policy and is explicitly not lawful.

So `MATE_CERT` is assembled on rank-preserving arrows, with the cycle-creating
obstruction explicitly preserved by declaring the full square unresolved there.

### 3.4 Reciprocal-loop touchstone
On the two-edge reciprocal loop, the comparison must preserve spread of harmonic
charge around the whole cycle (i.e. reciprocity forces non-local edge support in
the same harmonic class), which is compatible with the projected mate above and
incompatible with a fictitious edgewise adjoint on cycle-creating arrows when
not supported by the sealed adjoint structure.

## 4. N2. Projector cert V003, full field ledger

### 4.1 Field matrix

| Field | Status | Tag | Certificate chain |
|---|---|---|---|
| Finite carrier + differential | PROVABLE | fixed-stage premise | Q-408 finite complex and admissible maps |
| `Riesz`, `δ`, `Δ^Hdg`, `P_H` | PROVABLE | fixed-stage theorem | DoR-019 + finite linear algebra |
| sector-local blockwise locality | PROVABLE | fixed-stage theorem | `A5` + V002 locality analysis on certified disjoint Hilbert sums |
| within-cycle charge/globality | PROVABLE | fixed-stage theorem | harmonic pairing representation |
| contact reduction `[E_C,Δ^Hdg]=0` | ADOPTED LAW | A5 | `DOR_020_A5...` |
| rank-preserving Hodge naturality | DERIVED | rank-preserving W3 scope | `ρ_f d`, `ρ_f δ` equations |
| cycle-creating full adjoint mate | OPEN | type-annotated | CYCLE_CREATING_HODGE_ADJOINT_MATE_CERT (exact missing theorem) |
| projected J15 mate (`L3-10`) | PART-PROVABLE | lawful consequence | one-functor comparison at old-image level |
| `m_{T,N} ≠ 0` branch (and zero-branch void) | CARRIED | branch typing | finite branch split: nonzero branch explicit, zero branch void-conditioned |

### 4.2 Reader/selection policy
No `χ_K`-reader, no `T`-reader branch, and no response/threshold/fixed-point
object is referenced to generate any field. The projection and reduction chain is
carrier-structural.

### 4.3 Assembly order

1. Build actual finite Hodge data (`d`, `Riesz`, `δ`, `Δ^Hdg`, `P_H`).
2. Apply blockwise locality + sector contact law.
3. Apply A5 contact reduction (adopted).
4. Record adjoint scope separation:
   - rank-preserving arrows: full adjoint covariance.
   - cycle-creating arrows: projected `J15` mate only.
5. Carry branch interface for `m_{T,N}`.
6. Export the composite object for `J2` with explicit non-commitment.

`CERT_V003` is therefore assembled with a lawful, minimal boundary at the exact
unresolved arrow class above.

## 5. N3. What this hands forward to J2

The new forward interface for J2 is:

```text
J2 may now pose:
pi_Mx := π_M^resp ∘ P_H,M ∘ Loc_M

and compare via
r_f^Bot ∘ pi_Mx ∘ Eta_f = pi_Nx
```

where `x` is the harmonic/Maxwell projected local-symbol input on admitted
admissible objects.

This description does **not** impose J2 itself: no closure/equality target is
asserted, and no finite witness of `J2` is fixed at this stage.

## 6. N4. Battery and anti-tuning checks

### 6.1 F_PLDEC circularity
- checked: the certificate does not import `chi_K`, `T`, reader output, fixed-point
  residue, end-test number, or threshold value in its construction.
- checked: projection/descent data are fixed before any response-level claim.

### 6.2 Lawful-behavior spreading regression
- reciprocal-loop spreading of harmonics is preserved (nonspreading is rejected).
- disjoint-sector blockwise zero-spread verified wherever the direct-sum premise is
  in force.

### 6.3 A5 void-1 check
- checked on the admissible finite contact vectors available under the same
  admitted `I_contact` and `Δ_N^Hdg` data used in the certificate construction.
- no direct witness of non-reducing behavior appears in that scope under the adopted
  law, and no new coefficient is introduced.
- `A5_VOID1_CHECK = clean_on_scope / WITNESS_FOUND`  
  (WITNESS_FOUND is only from the pre-A5 countermodel family and therefore does not
  count in the adopted scope post-ruling).

### 6.4 Fresh attack
- Tried the “uniform-cycle-compression” perturbation: could one demand a single
  closed formula for all cycle-creating classes by forcing one global adjoint mate
  map? The attack fails without additional chain-adjoint data; it would need either
  an explicit upward lift or a replacement law stronger than FC4.

## Final board

```text
MATE_CERT = BLOCKED (cycle-creating full adjoint-mate on Δ^Hdg-intertwining class)
CERT_V003 = BUILT (with explicit N1 boundary class carried)
READER_REFERENCED = no
A5_VOID1_CHECK = clean_on_scope / WITNESS_FOUND

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
