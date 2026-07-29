# Stage 8 Namespace Register Draft v002

Append-only successor draft to `STAGE8_NAMESPACE_REGISTER_DRAFT_V001.md`.
This records additional namespace collisions discovered in Paste 126 W2.

## Status

```text
DRAFT ONLY. PROPOSED / AWAITING PRINCIPAL RATIFICATION.
No namespace rule is adopted by this artifact.
No prior artifact is renamed.
No register row is amended.
V001 is preserved unchanged.
alpha_computed = false
proof_authorized = false
```

## Purpose

This file is a proposed disambiguation table for short labels that have caused
or could cause audit defects.  Until ratified, it is a reader aid only.

## Search Scope

The W2 update searched the cleanroom, parent reports/scripts, and supervision
records for exact-token collisions around `C_R`, `C_R(x)`, `K_R`, `k_R`,
`K_bare`, and `X`.  Vendor/cache directories were excluded.  The rows below
record exact-symbol collisions or near-misses with demonstrated error risk.

## Authorities Read

Prior V001 authorities remain incorporated by reference.  New W2 authorities:

- `BID_MINIMAL_PUBLIC_CAUSAL_CELL_DERIVATION_V001.md`
  (`598ceb1ec246a5d7b192426e199fdfa3bf929239bacb479ee5e7035137b19f65`).
- `../reports/alpha_br_common_induced_coefficients_v001.md`
  (`f7caa5a252b3784de0058e302f03f5b7deec0d0490f3cfb9d6bf119084a2fde9`).
- `../scripts/derive_alpha_br_common_induced_coefficients_v001.py`
  (`fe2fac1f9f58abbfec67ad8a4315104b2246720952a79c4424edd90c06077938`).
- `COMPLETE_QSPEC_CONNECTED_KERNEL_INDEPENDENT_VERIFIER_PROTOCOL_V001.md`
  (`349d56e6b884664a8d99aa84c9a2fa2f2d833fa58018bda824bc623932ba09bf`).
- `COMPLETE_QSPEC_CONNECTED_KERNEL_LOCALITY_DIAGNOSTIC_SPEC_V001.md`
  (`1073e8d7c4aa590d1f45c0d1376b97ae7895181d22e2479ce2af9493f410a6b7`).
- `/Users/bgm/MB Work/alpha_supervision/BOHM_GR_EM_RELATION_REFUTED_2026-07-29.md`
  (`dd4563d4630349bd4da4cc583ae6762c25fdaa5d669a648e374e94be2133c681`).
- `STAGE8_P_COINCIDENCE_EXPONENT_DETERMINATION_V001.md`
  (`29084cd2c15bf1d3fa75230ca0b492381b064c0a56466afb03f5e8bb159cbc50`).

## Proposed Citation Rule

When citing a collision-prone label below, cite it as

```text
label [namespace-id]
```

on first use in a memo, artifact, or register row.  This is proposed only.

## Proposed Disambiguation Table

| Surface label | Proposed namespace id | Object | Primary carrier | Collision note |
|---|---|---|---|---|
| `R-1` | `STATUS-R-1-ROUTE2-ACCEPTANCE` | Lane-status register row accepting Route 2 restoration / ending custody split | `STAGE8_LANE_STATUS.md` R-1 | Register row, not route-list R1 |
| `R1` | `HESSIAN-ROUTE-LIST-R1` | Route-list R1 / Hessian-only re-posing / Hessian-first supersession object | `STAGE8_R2_DETERMINATION_ERRATUM_001_R1_RULING_REACH.md`; `STAGE8_LANE_STATUS.md` R-16 | Same token as repair and proof labels; ruled by content, not by label |
| `R.1` | `E1-SUCCESSOR-R1-SCAD-CONSTANTS` | E1 successor section "The frozen SCAD constants: per-cell first" | `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md` section R.1 | Dotted section label, not route-list R1 |
| `R1-R4` | `PHASE1-R1-R4-REAGGREGATION-LEMMA-BUNDLE` | Replaced Phase-1 draft lemma bundle consumed by E1 successor text | `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md` references to `679ba036...` R1-R4 | Often over-read as forcing later density/equality clauses |
| `R1` | `E1-REPAIR-R1-C3-DEMOTION` | E1 repair binding item "The C3-demotion repair" | `STAGE8_T7_E1_SPEC_REPAIR_BINDING_V001.md` section R1 | Repair-binding item, not Hessian route-list R1 |
| `R1` | `CAR-IMPLEMENTATION-R1-REPAIR-SCOPE` | Actual-parent CAR implementation repair scope for append-only v002 successors | `STAGE8_T7_ACTUAL_PARENT_CAR_IMPLEMENTATION_REPAIR_BINDING_V001.md` section R1 | Implementation repair item, not analytic route |
| `P-R1` | `PRIMARY-RESOLUTION-PREDICTION-R1` | Primary-resolution prediction: at primary `N_t = 96`, typical failing tier target | `STAGE8_T7_PRINCIPAL_DECISION_PRIMARY_RESOLUTION_RELAY_RECORD_V001.md` | Prediction family label, not route or register row |
| `R1` | `GAMMA-GATE-R1-LEMMA2-OPERATOR` | Gamma-gate repair item "Lemma 2 operator" | `STAGE8_T7_GAMMA_GATE_SPEC_REPAIR_AMENDMENT_V001.md` section R1 | Local repair item outside the Hessian/R-L2b route-list |
| `Route 2` | `STAGE8-ARCHITECTURE-ROUTE2-RATIFIED` | The Stage-8 architecture route ratified as a principal act | `STAGE8_ROUTE2_RATIFICATION_AND_FRAMING_CORRECTION_V001.md`; `STAGE8_LANE_STATUS.md` R-20 | Not the route-list R2 and not merely a route option |
| `Route 2` | `E1-REPAIR-CODEX-ROUTE2-SINGLE-CELL-ANCHOR` | Codex Route 2, renormalized single-cell anchor, rejected as insufficient in E1 repair binding | `STAGE8_T7_E1_SPEC_REPAIR_BINDING_V001.md` | Similar name but different object and status from architecture Route 2 |
| `Route 2` | `PRIMITIVE-OPERATOR-RESPONSE-ROUTE2` | Primitive operator-response route that must preserve completed component structure and pass Route-1 special-case falsifier | `STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_SPEC_V001.md` | Architecture-local route, not the ratified Stage-8 architecture route |
| `F'-5` | `E1-FPRIME-5-CARRIER-INDEX-FENCE` | E1 successor fence forbidding carrier-indexed constants and related non-whitelisted data in certified bounds | `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md` F'-5; `STAGE8_LANE_STATUS.md` O-1 | Often shortened to F5; principal-held, not a fallback term |
| `F5` | `HESSIAN-FALLBACK-F5-THEOREM3-OPEN-REGISTER` | Fifth fallback condition in the Hessian-first/R1 terms: Theorem 3's open register | `STAGE8_R2_DETERMINATION_ERRATUM_001_R1_RULING_REACH.md` | Not F'-5; this was explicitly flagged as a namespace collision |
| `F-5` | `PARENT-F5-HASHED-EVALUATOR-FENCE` | Parent fence that maps separately from E1-added F'-5 | `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md` fence mapping lines | Parent fence, not E1 F'-5 despite similar typography |
| `F5` | `FINITE-FOCK-F5-GAUSSIAN-SHORTCUT-NC` | Finite-Fock completed-record amplitude spec: Gaussian-shortcut negative control | `STAGE8_T7_FINITE_FOCK_COMPLETED_RECORD_AMPLITUDE_SPEC_V001.md` section F5 | Negative-control item, not any R-L2b/F'-5 decision |
| `F5` | `RELAYED-FAMILY-F5-INTERVAL-I` | Relayed-family resolution spec: Interval I | `STAGE8_T7_RELAYED_FAMILY_RESOLUTION_SPEC_V001.md` section F5 | Family-resolution filter, not the fallback fifth condition |
| `A4` | `BATTERY-A4-ROUTE-BLOCK` | Canonical-plan Part A battery section label | `STAGE8_MASTER_PLAN_TO_ALPHA_V001.md` | Distinct from v003 audit condition |
| `A4` | `V003-AUDIT-CONDITION-A4` | Audit condition in v003 successor package | Stage-8 v003 audit records | Same label, different authority family |
| `R-22` | `STATUS-R-22-A32-HOLDOUT-FREEZE` | Lane-status row for A32 holdout freeze written into V011 | `STAGE8_LANE_STATUS.md` R-22 | Row number only; not road item RD-22 |
| `RD-22` | `ROAD-RD-22-LADDER-GRADE-EVALUATOR-BLOCKER` | Road/dependency item: ladder-grade flag computation blocked on the unimplemented evaluator | `STAGE8_LANE_STATUS.md` R-22 scope text; `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` ladder text | Near miss with R-22; one is a row, one is a blocker |
| `kappa` | `AMBIGUOUS-KAPPA-FORBIDDEN` | Bare kappa token in alpha/firewall/EM-order contexts | R-9 rule | Must be written as `kappa_record` or `kappa_Thomson` |
| `kappa_bal` | `CL4-BALANCING-DIAGNOSTIC-NOT-KAPPA-RECORD` | C-L4/kappa_bal balancing diagnostic/rebuild object | C-L4/kappa_bal rebuild records | Not `kappa_record` |
| `C_R` | `CLEANROOM-COMPACTNESS-RATIO-C-R` | Compactness ratio `2 G E_R / (c^4 R_R)` for the public record cell, set to 1 at marginality | `BID_MINIMAL_PUBLIC_CAUSAL_CELL_DERIVATION_V001.md` lines 40-57 | This is the object that fixes the cleanroom record-cell scale; not the parent induced Einstein coefficient |
| `C_R(x)` / `C_R` | `PARENT-BR-INDUCED-EINSTEIN-COEFFICIENT-C-R` | Parent BR local induced Einstein coefficient `sum_a d_a I_2(x+C2_a)/(192 pi^2)` | `../reports/alpha_br_common_induced_coefficients_v001.md` lines 12-20; producer lines 326-334 | Same surface token as compactness ratio but different type, construction, and role |
| `C_R` | `QSPEC-CONNECTED-KERNEL-SECOND-MOMENT-C-R` | Connected-kernel low-frequency quadratic coefficient `-sum r^2 K(r)` or `-sum r^2 mean K(r)` | `COMPLETE_QSPEC_CONNECTED_KERNEL_INDEPENDENT_VERIFIER_PROTOCOL_V001.md` lines 65-71; `COMPLETE_QSPEC_CONNECTED_KERNEL_LOCALITY_DIAGNOSTIC_SPEC_V001.md` lines 86-95 | Same surface token as both C_R rows above; a diagnostic kernel moment, not compactness or Einstein coefficient |

## Known Near-Misses Not Promoted To Rows Here

- `T_R` versus `k_R`: same dimensional temptation, different tokens.  The
  GR-EM refutation records that they are objects in disjoint constructions with
  no derived bridge.
- `K_bare` versus `K_R(mu)`: related Maxwell-stiffness notation, but the
  refutation records a type difference rather than a same-token collision.
- `X`: a real error was recorded in `STAGE8_P_COINCIDENCE_EXPONENT_DETERMINATION_V001.md`,
  but the token is used as a generic variable in many unrelated maps and Pauli
  matrices.  A local route-specific alias may still be warranted; this draft
  does not propose a global `X` namespace rule.

## Proposed Minimal Author Names

If this register is ratified, first-use citations should prefer:

```text
R1 [HESSIAN-ROUTE-LIST-R1]
F'-5 [E1-FPRIME-5-CARRIER-INDEX-FENCE]
Route 2 [STAGE8-ARCHITECTURE-ROUTE2-RATIFIED]
C_R [CLEANROOM-COMPACTNESS-RATIO-C-R]
C_R(x) [PARENT-BR-INDUCED-EINSTEIN-COEFFICIENT-C-R]
C_R [QSPEC-CONNECTED-KERNEL-SECOND-MOMENT-C-R]
```

## Protected Status

```text
namespace_register_status = DRAFT_ONLY
rules_adopted = false
principal_ratification_required = true
rows_written = 0
artifacts_renamed = 0
v001_preserved = true
alpha_computed = false
proof_authorized = false
```
