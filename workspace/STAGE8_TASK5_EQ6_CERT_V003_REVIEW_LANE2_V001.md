# STAGE 8 TASK 5 / EQ6 — REVIEW OF RECORD: PROJECTOR CERT V003, A5 VOID-1, AND J2 ROUTE — LANE 2 V001

```text
TASK = Q-474
ARTIFACT_TYPE = PASS/KILL REVIEW
ARTIFACT_UNDER_REVIEW = STAGE8_TASK5_EQ6_PROJECTOR_CERT_V003_LANE1_V001.md
ARTIFACT_UNDER_REVIEW_SHA256 = 0bef9a003abb586666535689e98d7af29e7fc75b81e06fe439397ce2b8ef9100
REGISTER_HEAD_STATED = Q-474
REGISTER_HEAD_VERIFIED = Q-474
CONDITION_TAG = [EQ6]
GATE = SEAL / MIRROR / REPORT / STOP
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1. Preflight and constraints

1. `STAGE8_TASK5_EQ6_PROJECTOR_CERT_V003_LANE1_V001.md` was verified at SHA-256
   `0bef9a003abb586666535689e98d7af29e7fc75b81e06fe439397ce2b8ef9100`.
2. `STAGE8_TASK5_EQ6_PROJECTOR_CERT_V003_LANE1_V001.md.seal.sha256` was verified.
3. `STAGE8_TASK5_EQ6_PROJECTOR_LOCALITY_REDUCING_CERT_V002_LANE1_V001.md` (the
   `c81f61c4…` determination, SHA-256
   `c81f61c4921275f1e38edd1c48c698788523e5f3ab5960b611b106dc2b66d837`) was
   read and used for the A5-void analysis and the exact cycle-creating gap.
4. DoR-020-A5 file
   `DOR_020_A5_CONTACT_LAPLACIAN_REDUCING_2026-08-04.md` was verified.
5. The earlier lane-2 J2 attempt
   `3fd4b924ec1a70f3e730bcf99f406d697c53937b26467d2ae6d5aa8c1bb6822c`
   was checked to confirm the original fields and intended `pi_Mx` split.
6. Output filename was absent in workspace and archive before writing; no clobber.

No numeric evaluation, no fixed-point execution, and no end-test run is performed.

## 2. Verdict table (S1–S5)

| Item | Verdict | Result |
|---|---|---|
| S1 rank-preserving mate | PASS | Recomputed and confirmed. |
| S2 cert-field ledger | PASS | Types are explicit and separated. |
| S3 A5 void-1 classification | PASS | `A5` still stands; countermodel is not an actual record-surface witness. |
| S4 J2 route | PASS | J2 is not fully posable on `I_F` yet; it is post-mate-cert. |
| S5 fresh attack | PASS | New attack shows the mate gap is exact and cannot be inferred by extension. |

## 3. S1 — rank-preserving mate on nontrivial W3 arrow

### 3.1 Recompute on a nontrivial W3 arrow

On a rank-preserving W3 arrow `f: M -> N` in admitted scope (adjoint-restriction
mode), the derivation gives:

```text
ρ_f d_M = d_N ρ_f
ρ_f δ_M = δ_N ρ_f                      (intertwiner)
ρ_f Δ_M^Hdg = Δ_N^Hdg ρ_f
ρ_f P_H,M = P_H,N ρ_f
```

This is exactly the same chain of equalities used in the lane-1 proof and is valid
on nontrivial rank-preserving generators because they are in the isometry/adjoint
package of W3 scope.

### 3.2 Scope check: reciprocal-loop and refinement generators

The same derivation was checked against the lane-1 scope ledger:

- Reciprocal-loop arrow classes are genuine rank-preserving W3 arrows under the
  fixed-stage two-edge cycle family; they satisfy `d_M j_f = j_f d_N` with
  `ρ_f = j_f^*`.
- Refinement generators (record refinements already retained by the same scope)
  also satisfy the same hypotheses (`j_f` chain map + adjoint formula),
  hence are covered by the rank-preserving mate equations.

So S1 is pass: no contradiction to the claimed rank-preserving mate exists on
the stated scope; the unresolved object is correctly separated as a cycle-creating
class gap.

## 4. S2 — projector field ledger typing audit

### 4.1 Ledger reconstructed from the reviewed artifact

| Field group | In artifact | Required type |
|---|---|---|
| finite stage differential/Hodge data (`d`, `R`, `δ`, `Δ^Hdg`, `P_H`) | present | derived |
| `[E_C,Δ^Hdg]=0` and contact-reducing law | present | adopted (A5) |
| rank-preserving covariant Hodge mate | present | derived |
| cycle-creating full adjoint mate `ρ_f δ_M = δ_N ρ_f` | explicitly marked not proved | **conditional / explicit open** |
| projected J15-comparison mate | present | derived from J15 |
| reader dependence | absent in construction | pass (no target use) |

### 4.2 Exactness of explicit conditionality

The only conditional field is the cycle-creating adjoint mate (`L3-8` in the V002
ledger). Lane-1 correctly keeps it conditional and does not pretend to use it to
derive the full projector naturality. The artifact’s `CERT_V003 = BUILT` status
is therefore coherent: all non-conditional fields are established on their
declared premises and the open item is typed exactly.

Hence S2 is pass.

## 5. S3 — A5 VOID-1 classification

Reconstructing the `c81f61c4…` countermodel from `L2-5 ... L2-8`:

```text
C^1 = span{e_c, e_b},    I_contact^1 = span{e_c},
d^0 = sqrt(A_ε),         d^1 = 0,
A_ε = [[1, ε],[ε,1]],    0<|ε|<1.
```

Then

```text
Δ_1^Hdg e_c = e_c + ε e_b ∉ I_contact^1,
```

so `I_contact^1` is not reducing for `Δ^Hdg` unless additional reducing law is
added.

The key check is whether this data is an actual record-surface contact witness in the
adopted scope. It is **not**:

1. It supplies only a positive finite Hilbert pair and a closed-form `d^0` choice.
2. It omits the actual surface transport data required for an actual `[EQ6]` contact
   realization on the finite live tower (path current data, admissible transport,
   and the `Loc/σ` realization stack under `A1`-scope).
3. It therefore is a **pre-A5 countermodel family** (showing logical non-implying),
   not a direct admitted object of the current surface coherence class.

So A5 void-1 is **not** triggered by this model on the actual scope; `DoR-020-A5`
remains in force.

Conclusion for S3: **PASS**, `A5_STATUS = STANDS`.

## 6. S4 — J2’s route and posability under current scope

### 6.1 What J2 requires

The J2 equality is over the actual finite tower category `I_F` arrows:

```text
reader = pi_Mx ∘ Loc ∘ Kernbar ∘ Q .
```

For this to be a typed theorem on the tower, both:

1. a lawful `pi_Mx` and `Loc` pair on the same carrier, and
2. the full covariance needed on every arrow class used in `I_F`,

are required.

### 6.2 Current scope of J2

- On rank-preserving W3 arrows: the rank-preserving Hodge mate is available, so
  the adjoint-side covariance needed for J2 exists.
- On cycle-creating arrows: lane-1 only supplies the projected J15 comparison
  (old-image bottom), not the full `π_Mx ∘ Loc` compatibility.

Therefore, J2 is not presently poseable on **all** arrows of `I_F`; it is only
poseable on the non-cycle-creating/rank-preserving subcategory already in the
existing mate scope. Full tower posability requires the cycle-creating mate
certificate (`CYCLE_CREATING_HODGE_ADJOINT_MATE_CERT` plus contact-to-Maxwell
route).

So S4 is pass with:

`J2_POSABLE = after_mate_cert (+rank-preserving W3 arrows now; cycle-creating arrows wait on the cycle-creating adjoint mate cert)`

## 7. S5 — fresh attack

**Attack:** attempt to infer J2 on cycle-creating arrows from the projected
`r_f^Bot π_M^resp P_H,M Loc_M η_f = π_N^resp P_H,N` alone by selecting one
upward section of cycle classes.

**Result:** the projected formula only compares old-image bottoms and is contravariant
only. There is no admissible upstream component (and no selected section is allowed)
to recover the full `pi_Mx`/`Loc` output on new-cycle directions. This confirms the
documented boundary: `CYCLE_CREATING_HODGE_ADJOINT_MATE_CERT` is not redundant.

## 8. Final board

```text
CERT_V003 = CONFIRMED
A5_STATUS = STANDS
J2_POSABLE = after_mate_cert (rank-preserving W3 arrows now; cycle-creating arrows blocked until the cycle-creating adjoint mate cert and full J2 route are in place)

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

