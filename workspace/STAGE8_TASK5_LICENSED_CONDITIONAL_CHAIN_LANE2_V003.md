# STAGE 8 TASK 5 — LICENSED CONDITIONAL CHAIN V003

[EQ6] Date: 2026-08-04
[EQ6] Lane: Codex Lane 2
[EQ6] Task: PASTE 534
[EQ6] Parent: `STAGE8_TASK5_LICENSED_CONDITIONAL_CHAIN_LANE2_V002`
[EQ6] Parent SHA-256: `1069e4f442ebfd083944c7cf6df8ba04058c531846fa61e1b6452d7ba551a269`
[EQ6] Repair authority: `STAGE8_TASK5_CHAIN_V002_CROSS_CHECK_LANE1_V001.md`
[EQ6] Repair-authority SHA-256: `9a8008b98ed48e61886e7e2d1e380dc72fe3d3a0b48480f2274b238ac05e0965`

[EQ6] ## Preflight

[EQ6] ```text
[EQ6] DOES_THE_OBJECT_EXIST = yes
[EQ6] IS_THE_VERSION_CURRENT = yes_through_Q-458
[EQ6] ARE_ITS_INPUTS_PRESENT = yes
[EQ6] PRECHECK = PASS (artifact and register seals verified)
[EQ6] RELAY_REGISTER_HEAD = Q-457
[EQ6] LIVE_REGISTER_HEAD = Q-458
[EQ6] Q458_EFFECT = stage-1 finite assembly built pending cross-review;
[EQ6]               full finite certificate remains under construction;
[EQ6]               this bounded V003 repair remains current.
[EQ6] OUTPUT_PREEXISTED = false
[EQ6] ```

[EQ6] ## Lead result

[EQ6] ```text
[EQ6] C_RET = TYPED
[EQ6] ENTRANCE_GATE = INSTALLED
[EQ6] D_W_COMPLETENESS = CERTIFICATE_ADDED
[EQ6] MAP = STEP_0_PLUS_TWELVE_STEP_REPAIRED
[EQ6] THEOREMS = RETAGGED
[EQ6] C_RET_SCOPE = [EQ6] + D_COMPLETE_w
[EQ6]               + branch scope (interval/convex OR AC scope)
[EQ6] CHAIN_V003 = READY_FOR_CROSS_CHECK
[EQ6] alpha_computed = false
[EQ6] proof_authorized = false
[EQ6] kappa_record_computed = false
[EQ6] FENCE_BLOCKED_STRUCTURAL_RESULT = false
[EQ6] MACHINERY_APPEAL = false
[EQ6] ```

[EQ6] ### 0. Authority scan and fence check

[EQ6] Read hash-verified:
[EQ6] - `9a8008b98ed48e61886e7e2d1e380dc72fe3d3a0b48480f2274b238ac05e0965` (V002 cross-check and exact K2/K3 repairs),
[EQ6] - `88854f08966c15e6afbcb300c6151f59a169e2725c3d5a8643b653abfe3ddcb3` (conditional Banach framework),
[EQ6] - `aebe708d2e7ba4b67e828976bd01eae2d5eec04afbb6a28f3f77f9dc8003fc97` (scalar carrier/modulus),
[EQ6] - `b569a89e661ad92b744213bfc7cd65985908bc509b8dd9de77bcae3a2bdb4bad` (return interface),
[EQ6] - `feb84216103c5c86f5d53c6323d4bb4a6fbe26d6d2c849d0f89c66d8ba47d9f0` (premise ledger),
[EQ6] - `d7dcbc3ad7c470c8aaf0d8407db625d3e910cf180cd7b035fbc96bdfe58471b4` (J1–J15),
[EQ6] - `a681c784b451790c1163d083865988d2256170d1f0c468609b9a803864a0ab4b` (`F_actual` exhibition and missing certificate type),
[EQ6] - DoR-020 and DoR-020-A1 decision files,
[EQ6] - the proposed-not-adopted A2 artifact and its constraint/adjudication chain.
[EQ6]
[EQ6] Q-458 records that Stage 1 of `F_ACTUAL_JOINT_FINITE_PACKAGE_CERT`
[EQ6] is built but pending cross-review; physical J2/J7 and the joint diamonds
[EQ6] still prevent the full certificate and membership theorem. V003 therefore
[EQ6] types the entrance dependency and does not presuppose its discharge.
[EQ6] No alpha or kappa numeric operations were introduced.

[EQ6] ## R1. Entrance gate for the completed chain

[EQ6] ### R1.1 The opening premise

[EQ6] Define the entrance condition as the conjunction

[EQ6] ```text
[EQ6] ENTRANCE_020(F_actual,A2) :=
[EQ6]   JOINT_FINITE_CERT(F_actual)
[EQ6]   and ADOPTED(A2)
[EQ6]   and FiniteCoherent_020(F_actual).                 (R1-1)
[EQ6] ```

[EQ6] The three conjuncts are distinct proof obligations:

[EQ6] 1. `JOINT_FINITE_CERT(F_actual)` means the full
[EQ6]    `F_ACTUAL_JOINT_FINITE_PACKAGE_CERT` is built and cross-certified:
[EQ6]    one full package functor, one package bottom, physical J2/J7, one
[EQ6]    finite J1–J15 term, and the simultaneous joint diamonds.
[EQ6] 2. `ADOPTED(A2)` means the completed-existence axiom has passed its
[EQ6]    gate and has been adopted. The present A2 is proposed, not adopted;
[EQ6]    this artifact neither adopts nor invokes it.
[EQ6] 3. `FiniteCoherent_020(F_actual)` is the inhabited-actual-antecedent
[EQ6]    membership theorem on the full live tuple, not a formal schema and
[EQ6]    not six marginal memberships.

[EQ6] At the current state:

[EQ6] ```text
[EQ6] JOINT_FINITE_CERT(F_actual) = UNDER_CONSTRUCTION;
[EQ6] ADOPTED(A2) = false;
[EQ6] FiniteCoherent_020(F_actual) = unproved;
[EQ6] ENTRANCE_020 = NOT_YET_DISCHARGED.                  (R1-2)
[EQ6] ```

[EQ6] Stage-1 builder status, including Q-458's pending functor/bottom claim,
[EQ6] is not silently promoted to the full certificate. No completed witness
[EQ6] exists on this chain before `(R1-1)` is proved.

[EQ6] ### R1.2 Conditional Step-1 discharge

[EQ6] Only under `ENTRANCE_020` may A2 be applied to the actual tuple:

[EQ6] ```text
[EQ6] ENTRANCE_020(F_actual,A2)
[EQ6]   -> exists nonempty covariant completed family W_actual
[EQ6]      such that for every w in W_actual,
[EQ6]      Res_fin(w)=F_actual and Eq_J1-J15(w).          (R1-3)
[EQ6] ```

[EQ6] Equation `(R1-3)` is an existence statement over a family. It is not a
[EQ6] Skolem function and binds no member. Step 1 certifies the completed
[EQ6] equalizer family-wide; it does not select a `w` for computation.

[EQ6] Step 2 remains the exact finite/regression recheck. It cannot manufacture
[EQ6] any conjunct of `(R1-1)` and cannot substitute for the entrance.

[EQ6] ## O1. Construct and certify `C_ret` (stationary-return certificate)

[EQ6] 1) Definition (typed candidate, not selected):
[EQ6]
[EQ6] ```text
[EQ6] C_ret[w] :=
[EQ6]   (D_w, Crit_w, S_w, B_w, ell_w, Pi_w, H_w, I_w, cplx_w,
[EQ6]    L_G,w, L_Pi,w, M_ell,w,
[EQ6]    topologies, restrictions, covariance/reality/batching/unit certificates,
[EQ6]    domain_complete_cert_w, closure_bound, branch_scope_w)
[EQ6] ```
[EQ6] with
[EQ6] ```text
[EQ6] S_w : D_w -> Crit_w,      B_w := ell_w o Pi_w o Schur o S_w.
[EQ6] ```

[EQ6] 2) Derivation from built carrier and adopted clauses:
[EQ6]
[EQ6] - `K` carrier and stationarity problem data are available from Q-403 and the adopted V004 package clauses.
[EQ6] - Reader normalization and `Rhat_K` direction are available from `bae34116...` and Q-403.
[EQ6] - Return-branch structure (`B_w(D_w) subset D_w`) is not supplied by DoR-020; it is the core return clause of `C_ret`.
[EQ6] - Completeness of the ambient scalar carrier does not imply completeness of `D_w`; `domain_complete_cert_w` is an independent item.

[EQ6] [C_RET] CERTIFICATE CORE ITEMS (for each `w`):
[EQ6]
[EQ6] (A) **Domain-Connectivity/Nonemptiness Clause**
[EQ6] - `D_w subset K_amb`, with the complete scalar ambient topology from Q-403.
[EQ6] - `D_w` nonempty (carried only by explicit `C_ret` clause; not from `[EQ6]` alone).

[EQ6] (A2) **Domain-Completeness Certificate**
[EQ6] - one of the following failure-capable witnesses is attached:
[EQ6]
[EQ6] ```text
[EQ6] ClosedWitness_w :=
[EQ6]   D_w is closed in complete K_amb,
[EQ6]   hence (D_w,d_amb|D_w) is complete;               (R2-1a)
[EQ6]
[EQ6] CompleteMetricWitness_w :=
[EQ6]   (D_w,d_w) is complete,
[EQ6]   inclusion (D_w,d_w) -> K_amb is continuous,
[EQ6]   and every later norm/difference estimate uses d_w. (R2-1b)
[EQ6] ```

[EQ6] Define

[EQ6] ```text
[EQ6] D_COMPLETE_w := ClosedWitness_w or CompleteMetricWitness_w. (R2-2)
[EQ6] ```

[EQ6] Neither interval/convexity nor absolute continuity is accepted as a
[EQ6] completeness witness. The certificate is fixed before a modulus,
[EQ6] threshold, fixed point, or root is examined.

[EQ6] (B) **Return Clause**
[EQ6] - `B_w(K) in D_w` for all `K in D_w`.

[EQ6] (C) **Stationary Solution Clause**
[EQ6] - `S_w(K)` solves full stationary equations at level 6 and `R_comp[S_w(K)] = 0`.

[EQ6] (D) **Branch-Regularity Clause**
[EQ6] - either
[EQ6]   1. interval/convex branch certificate on `D_w`, or
[EQ6]   2. absolute-continuity certificate on the scalar branch of `S_w`.
[EQ6]
[EQ6] (E) **One-branch Certificate Scope**
[EQ6] - branch map and branch-sensitive differences are carried as
[EQ6]
[EQ6] ```text
[EQ6] C_RET_SCOPE_w := D_COMPLETE_w + branch_scope_w.    (R2-3)
[EQ6] ```

[EQ6] [C_RET] The V001 repair's two rungs remain the explicit construction of
[EQ6] the return object and branch scope. V003 adds `(A2)` as a separate,
[EQ6] falsifiable Banach-domain obligation; it is not folded into `(D)`.

[EQ6] 3) Construction status:
[EQ6]
[EQ6] ```text
[EQ6] C_RET_EXISTS[w] :=
[EQ6]   (A),(A2),(B)-(E) + compatibility with Q404 return template.
[EQ6]
[EQ6] C_RET_EXISTS[w] can be:
[EQ6]   - PROVEN for a scoped instance carrying D_COMPLETE_w and (D),
[EQ6]   - TYPED as a condition when either certificate remains unbuilt.
[EQ6] ```

[EQ6] The current artifact tags the unconstructed parts as:
[EQ6] - `[C_RET] domain_complete_cert_w` = TYPE-U until `(R2-1a)` or `(R2-1b)` is produced,
[EQ6] - `[C_RET] branch_regularization` = TYPE-U until `(D)` is produced,
[EQ6] - `[C_RET]` does not include `[EQ6]` full witness binding.

[EQ6] ## O2. Permanent domain regressions

[EQ6] ### O2.1 Disconnected-domain regression

[EQ6] The counterexample reported at Q-448:
[EQ6] ```text
[EQ6] D = {-1,1},
[EQ6] b(K)=K^3/2-3K/2,
[EQ6] B(K)=K maps to ell_w[Schur_w(S_w(K))] = b(K).
[EQ6] ```
[EQ6] has:
[EQ6] - `b(D)=D`, `b'(-1)=b'(1)=0` and `q_der=0`,
[EQ6] - true difference quotient `q_true=1`,
[EQ6] - no fixed point on `D`.
[EQ6]
[EQ6] This finite set is closed and complete, so it passes `(A2)`. It is
[EQ6] excluded independently by `(D)`: it has no interval/convex branch and no
[EQ6] absolute-continuity branch certificate connecting its two points. Thus
[EQ6] the completeness repair does not weaken the original Q-448 falsifier.

[EQ6] ### O2.2 Nonclosed-domain regression

[EQ6] Take the complete ambient scalar line and

[EQ6] ```text
[EQ6] D_open=(0,1),
[EQ6] B_open(K)=(K+1)/2.
[EQ6] ```

[EQ6] Then `D_open` is nonempty, interval, convex, and
[EQ6] `B_open(D_open) subset D_open`; its exact Lipschitz modulus is strictly
[EQ6] below one. But `D_open` is not closed or complete in the induced metric,
[EQ6] and the iterates converge to `1`, outside `D_open`. The iteration stays
[EQ6] in the domain at each finite step but exits it at its limit, so Banach
[EQ6] existence on `D_open` is false.

[EQ6] V003 rejects this input at `(A2)` before Steps 5–7. This is the witness
[EQ6] form foreclosing a nonempty, invariant, nonclosed physical domain.

[EQ6] ## O3. Repaired witness-to-number map (Step 0 + 12 steps)

[EQ6] The map is an ordered authorization chain. Every step inherits all
[EQ6] successful preceding gates; none is executed here.

[EQ6] 0. **Certify the entrance** `(R1-1)`:
[EQ6]    full finite package certificate cross-certified; A2 adopted; actual
[EQ6]    antecedent membership theorem proved.
[EQ6]    Consumer: completed-existence entrance / Gate: `ENTRANCE_020`.

[EQ6] 1. Under `ENTRANCE_020`, apply A2 to `F_actual` and certify the returned
[EQ6]    nonempty covariant completed family against all six J1–J15 generators,
[EQ6]    family-wide, with no member selected.
[EQ6]    Consumer: DoR-020/A2 / Gate: `(R1-3)`.

[EQ6] 2. Verify finite/rail certificates and regressions already attached to
[EQ6]    every `w` in the returned family.
[EQ6]    Consumer: adversarial checks / Gate: DoR-008, finite fences.

[EQ6] 3. **Construct `C_ret[w]` domain and stationarity** from carrier + adopted clauses.
[EQ6]    Consumer: return theorem route / Gate: built carrier coherence.

[EQ6] 4. **Certify `C_ret[w]` object and domain**:
[EQ6]    `(A)` nonempty physical domain, `(A2)` `D_COMPLETE_w`, `(B)` return,
[EQ6]    `(C)` stationarity, `(D)` interval/convex or AC branch scope, and
[EQ6]    `(E)` topology/restriction/rules.
[EQ6]    Consumer: Q404/Banach contract / Gate: `C_ret` object validity.

[EQ6] 5. Prove the boundedness estimate on the same certified complete `D_w`:
[EQ6]    `|B_w(K)-B_w(K')| <= q_cert,w d_w(K,K')`.
[EQ6]    Consumer: L1 boundedness theorem / Gate: `D_COMPLETE_w` + `C_ret` estimate constants.

[EQ6] 6. Prove the typed return map `B_w:D_w -> D_w` on that same complete domain.
[EQ6]    Consumer: L1 closure / Gate: `(B)` + `D_COMPLETE_w`.

[EQ6] 7. Invoke branch completeness **from `(A2)`**:
[EQ6]    `D_COMPLETE_w` proves the Banach domain complete; `(D)` separately
[EQ6]    proves the interval/convex or AC regularity required by the derivative
[EQ6]    route. Ambient completeness plus branch scope is not used as a proof.
[EQ6]    Consumer: conditional Banach / Gate: `C_RET_SCOPE_w` from `(R2-3)`.

[EQ6] 8. Compute exact Schur derivative and `a_loop` with full branch motion retained:
[EQ6]    `RetExtract[dot Schur] = a_loop Rhat_K`.
[EQ6]    Consumer: L2 derivative / Gate: all Steps 0–7, including `C_RET_SCOPE_w`, plus differentiability on that branch.

[EQ6] 9. Build exact modulus:
[EQ6]    `A_loop := sup_Dw |a_loop|`, `q_loop = sup_Dw |dot B_w| = |chi_K| A_loop`
[EQ6]    under `C_RET_SCOPE_w`.
[EQ6]    Consumer: threshold / Gate: complete branch scope and derivative-domain validity.

[EQ6] 10. Apply threshold: strict contraction iff `|chi_K| < A_loop^{-1}` on `0 < A_loop < infinity`
[EQ6]     OR the separately typed `A_loop=0` edge case.
[EQ6]     Consumer: threshold theorem / Gate: `C_RET_SCOPE_w` + `q_loop` formula.

[EQ6] 11. Conditional fixed-point consequence:
[EQ6]     existence/uniqueness under Step 10 for the same `w` and the same complete `D_w`.
[EQ6]     Consumer: Banach theorem / Gate: conditional contraction on `D_COMPLETE_w`.

[EQ6] 12. Sensitivity-system and witness-to-number ladder preparation:
[EQ6]     set up parameter-difference systems and record the consumer chain:
[EQ6]     `ENTRANCE_020 -> family w -> C_ret[w] -> (boundedness, return,
[EQ6]      completeness, contraction, fixed-point theorem) -> downstream gates`.
[EQ6]     Consumer: `WITNESS_TO_NUMBER` map / Gate: no member binding, no execution.

[EQ6] ## O4. Theorem retagging and condition refinement

[EQ6] Repaired conditional declarations:
[EQ6] - `BOUNDEDNESS`: from `ENTRANCE_020 + [EQ6] + C_ret[w] + D_COMPLETE_w`.
[EQ6] - `CLOSURE`: from `ENTRANCE_020 + [EQ6] + C_ret[w] + D_COMPLETE_w`.
[EQ6] - `CONDITION`: `ENTRANCE_020 + [EQ6] + C_RET_SCOPE_w`, where
[EQ6]   `C_RET_SCOPE_w = D_COMPLETE_w + interval/convex-or-AC branch scope`.
[EQ6] - `A_LOOP` and threshold formulas remain symbolic; exact difference-quotient scope remains explicit.
[EQ6] - Steps 3 and 4 remain separated: the witness does not auto-supply return or domain completeness.

[EQ6] DoR-020 consequences are preserved:
[EQ6] - `[EQ6]` remains a non-selected universal conditional condition.
[EQ6] - the proposed A2 is not treated as adopted.
[EQ6] - `C_ret` remains independent of `[EQ6]` and carries its own complete-domain and branch certificates.

[EQ6] ## O4.1 `C_ret` status ledger

[EQ6] - `ENTRANCE_020`: TYPE-U until all three opening conjuncts are proved.
[EQ6] - `[EQ6]` universal: `w` remains a family index; no member selected.
[EQ6] - `[C_RET]` object: fields `(A),(A2),(B)-(E)` defined with scopes.
[EQ6] - `[C_RET]` completeness: TYPE-U until `ClosedWitness_w` or `CompleteMetricWitness_w` is supplied.
[EQ6] - `[C_RET]` branch regularity: TYPE-U until interval/convex or AC certificate is produced.
[EQ6] - disconnected-domain regression: excluded by `(D)`.
[EQ6] - nonclosed-domain regression: excluded by `(A2)`.

[EQ6] ## O5. Registry of remaining gates and tags

[EQ6] - MEMBER_BINDING = false (unchanged)
[EQ6] - FIXED_POINT_EXECUTION = false (unchanged)
[EQ6] - END_TEST = false
[EQ6] - NUMERIC_EVALUATION = false
[EQ6] - MEASURED_CONSTANT_COMPARISON = false
[EQ6] - ENTRANCE_020 = installed but not discharged
[EQ6] - C_RET = constructed as typed object; not selected
[EQ6] - THEOREMS = entrance/[EQ6]/C_RET-tagged with explicit complete-domain scope

[EQ6] ## O6. Falsifiers and anti-tuning

[EQ6] ### O6.1 Required reruns

[EQ6] **Disconnected-domain regression.** The finite set is complete but
[EQ6] fails branch regularity. No derivative-only modulus or fixed-point
[EQ6] theorem is licensed. **PASS.**

[EQ6] **Hidden-uniformity attack.** Every `D_w`, metric, completeness witness,
[EQ6] return proof, and modulus remains indexed by `w`. V003 proves no common
[EQ6] domain and no `sup_w q_w<1`. A family-wide theorem still requires a
[EQ6] uniform domain/equivalent metrics, reducing domains, and perturbation
[EQ6] bounds. **PASS FOR THE PER-w CHAIN; FAMILY UNIFORMITY NOT LICENSED.**

[EQ6] **Gate-bypass attack.** Step 8 explicitly inherits Steps 0–7. A local
[EQ6] derivative formula cannot bypass `ENTRANCE_020`, `D_COMPLETE_w`, return,
[EQ6] or branch regularity. There is no route to Step 8 with only ambient
[EQ6] completeness or an isolated `C_RET_SCOPE_w` label. **PASS; NO BYPASS.**

[EQ6] **Fresh entrance attack — pending-cert laundering.** Substitute Q-458's
[EQ6] pending Stage-1 builder artifact for the full certificate and attempt to
[EQ6] apply A2. The attempt fails twice: Stage 1 is not yet cross-certified and
[EQ6] the full finite certificate still lacks physical J2/J7 plus the joint
[EQ6] diamonds; independently, A2 is not adopted. `(R1-1)` therefore remains
[EQ6] false and no completed family is returned. **PASS; PROVISIONAL BUILD IS
[EQ6] NOT AN ENTRANCE TOKEN.**

[EQ6] **Nonclosed-domain attack.** `(0,1)` with `B(K)=(K+1)/2` passes
[EQ6] nonemptiness, interval/convex scope, return, and strict Lipschitz bound,
[EQ6] but its limit lies outside the domain. `(A2)` rejects it. **PASS.**

[EQ6] The pre-existing finite one-edge/tree/S8-A checks, branch edge cases,
[EQ6] hidden reader-scaling check, and S8-A perpendicular-term visibility are
[EQ6] unchanged from V002 and remain passing on their exact prior scopes.

[EQ6] ### O6.2 Anti-tuning ledger

[EQ6] 1. `F_actual`, the certificate interface, and A2 adoption status are fixed before any `w` is available.
[EQ6] 2. No member is chosen from the completed family.
[EQ6] 3. `D_COMPLETE_w` is certified before any modulus, threshold, fixed point, or root is inspected.
[EQ6] 4. No target-driven choice is made between `(R2-1a)` and `(R2-1b)`; either must independently prove completeness.
[EQ6] 5. The two domain counterexamples are fixed falsifiers, not coefficient sources.
[EQ6] 6. No response, threshold, or end-test consequence justifies the entrance or completeness clauses.

[EQ6] ## R3. Bounded delta versus V002

[EQ6] | V002 location | V003 bounded change | Reason |
[EQ6] |---|---|---|
[EQ6] | preflight/head | rechecked through Q-458; Q-458 does not discharge full entrance | send-time currentness |
[EQ6] | lead block | add `ENTRANCE_GATE` and `D_W_COMPLETENESS` statuses | R1/R2 |
[EQ6] | before O1 | add `ENTRANCE_020` and conditional A2 application | K2 repair |
[EQ6] | `C_ret` tuple | add `domain_complete_cert_w` | K3 repair |
[EQ6] | clause (A) | split nonemptiness from new `(A2)` completeness witness | prevents ambient/subset conflation |
[EQ6] | clause (E) | define `C_RET_SCOPE_w = D_COMPLETE_w + branch_scope_w` | separates completeness from regularity |
[EQ6] | domain regressions | retain disconnected test; add nonclosed invariant-domain test | failure-capable propagation |
[EQ6] | ordered map | add Step 0; rewrite Step 1 entrance; propagate `(A2)` through Steps 4–7 and cumulative Step-8 gate | required repair |
[EQ6] | theorem tags/status | add entrance and complete-domain tags | no hidden weakening |
[EQ6] | falsifiers | rerun required attacks and add pending-cert laundering attack | R3 |

[EQ6] All V002 material not named in this table is retained verbatim. The
[EQ6] bounded propagation edits preserve the C_ret/[EQ6] separation, stationary tuple, reader and
[EQ6] Schur interfaces, threshold formulas and edge typing, Steps 8–12 escrow,
[EQ6] finite regressions, no-selection rules, and protected-action registry.

[EQ6] ## Final board

[EQ6] ```text
[EQ6] CHAIN_V003 = READY_FOR_CROSS_CHECK
[EQ6] ENTRANCE_GATE = INSTALLED
[EQ6] D_W_COMPLETENESS = CERTIFICATE_ADDED
[EQ6]
[EQ6] ENTRANCE_020 = NOT_YET_DISCHARGED
[EQ6] D_COMPLETE_w = PER-w_CERTIFICATE_OBLIGATION
[EQ6] MEMBER_BINDING = none
[EQ6] FIXED_POINT_EXECUTION = none
[EQ6] END_TEST = none
[EQ6] NUMERIC_EVALUATION = none
[EQ6]
[EQ6] alpha_computed = false
[EQ6] proof_authorized = false
[EQ6] kappa_record_computed = false
[EQ6] ```
