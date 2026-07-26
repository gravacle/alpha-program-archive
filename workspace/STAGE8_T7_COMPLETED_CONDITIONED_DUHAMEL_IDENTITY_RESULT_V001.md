# Stage-8 T7 Completed-Chain Conditioned Duhamel Identity Result V001

Date: 2026-07-26

## Verdict

```text
T7IV_COMPLETED_CHAIN_FINITE_CONDITIONED_IDENTITY_DERIVED
T7IV_CONDITIONAL_INTERCHANGE_SCHEMA_SEALED
LADD_HESSIAN_MIXING_LEMMA_SEALED
```

Issued under the sealed spec (4fe8d42d…), the D6 repair amendment
(Part II) and the sealed execution addendum, after the two-lane protocol
(primary execution lane + independent verifier lane, no shared code, the
verifier's commitment sealed before the primary re-ran). Both lanes pass
every runnable obligation, with two standing named blocks (below).

## Two-lane agreement

```text
Primary lane: T07_duhamel_conditioned_identity_primary_v001.json
              (4d80bf13…), formal derivations draft (b28b665b…).
Verifier lane: VERIFIER_COMMIT.json, sealed transcript 36e6ec72…
Both independently: FK-1, FK-2 (incl. the Re[c^2] = 2(Re c)^2 - |c|^2
step), FK-3, L-ADD and its q=1 endpoint DERIVED; C1 and C2 DERIVED;
the amended two-variable Vitali-Porter + Osgood schema proof written in
full and confirming that the deleted K-uniform delta is never used.
```

## Load-bearing values (both lanes)

```text
F-B exact anchors (exact rational arithmetic, no floats):
  g_c = 0 ; (log q_c)'' = -1/2 ; H_att,c = 1/4 ; g_all = 1/4 ;
  H_att,all = 1/4 ; g_all - g_c = ||eta_r||^2 = 1/4 ; L-ADD endpoint
  identity exact; sigma witnesses (1/4, 1/4, 1/2, 0) reproduced.
F-A conditioned crosscheck (Slater fill, 8 modes / 4 particles /
Fock 70 x record 9, unsplit RK4 200/400, sealed radius convention):
  q = 0.2541064940 +- 2.86e-7 (excludes 0, margin 8.9e5)
  g_D,c = +0.008450951 +- 4.93e-8   (lower bound > 0)
  (log q)'' = 0.10210007 +- 1.01e-6
  H_att = -0.04259908 +- 5.50e-7    (stencil intersects; FK-2 residual 0)
  L-ADD residual = -5.4e-10 +- 1.56e-8 (contains 0)
M2 regression: plus/all = minus/all = 8.19415e-8;
               plus/comp = minus/comp = 6.69468e-8; factors 4.000.
```

STRUCTURAL FACT OF RECORD: on F-A the attenuation Hessian is NEGATIVE
(-0.0426) while the conditioned covariance is POSITIVE (+0.00845) — the
diagonal correction -(1/2)(log q)'' dominates. This is exactly the
completed-chain departure FK-2 predicts and the exhaustive chain cannot
exhibit (there q == 1 and the correction vanishes). It is what makes the
L2 freeze's fence 2 mechanical rather than advisory, and it gives the
wrong-form control real teeth (mismatch 0.051050 = (1/2)|(log q)''|).

## Controls

All pass in their predeclared directions: GHZ returns H1_VIOLATED and the
schema REFUSES; V010 stays failed (exact bound kappa_L <= 1/(16 L^2));
contact-omission mismatches by 0.058578 with the discrepancy enclosure
matching the independently integrated contact term to 5e-11 (the mismatch
IS the contact term, at second order); wrong-ordering flips sign with the
Im-enclosure excluding zero (pair-evaluated reading, per the addendum);
wrong-form fails detectably; Route-1 re-execution matches its sealed
closed forms (4.45e-16 / 3.34e-16); degenerate endpoint exact.

## Standing named blocks (both victory-class; nothing repaired)

```text
F_C_INPUT_BUNDLE_NOT_YET_SEALED — the F-C leg (Phase-A pinned states)
  cannot run: no Phase-A sealed bundle exists and production is
  prohibited. Runs against the sealed bundle hashes when Phase-A seals.
S63B_D5_BASELINE_READING_UNSATISFIABLE_ON_FA — retained witness; the
  baseline first derivative vanishes on F-A by an exact fixture symmetry
  (itself consistent with the sealed parity lemmas).
```

## What this does NOT establish

(H1) and (H2) remain NAMED UNDERIVED INPUTS — they are T7(ii) and
T7(iii), owned by the majorant spec via interface I3 (tuple V002). No
volume-uniform zero-free neighborhood, no linked-cluster density, no
intensive limit on the actual parent, and no unconditional
Duhamel/intensive-Hessian equality follows. Piece 3 (instantiation)
remains out of scope behind Phase-A/B and the relay chain.

## Protected status

```text
completed_chain_finite_conditioned_identity_derived = true
conditional_interchange_schema_sealed = true
additive_hessian_mixing_lemma_sealed = true
C1_affine_tangent_lemma_derived = true
C2_boundary_history_independence_lemma_derived = true
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
Duhamel_intensive_Hessian_equality_proved = false
kappa_record_computed = false
alpha_computed = false
proof_authorized = false
```
