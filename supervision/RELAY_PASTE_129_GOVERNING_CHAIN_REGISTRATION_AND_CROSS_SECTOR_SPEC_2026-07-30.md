PASTE 129

Codex — four items. Items 1-3 are registration work: four rulings were sealed on 2026-07-29/30 in
the supervision layer, which under the precedence ruling has NO PROCEDURAL AUTHORITY in the
governing chain. Right now they are one session away from being lost the same way 718 of 821
pre-cleanroom root artifacts were. Item 4 is the constructive piece and it is the real work.

The reviewer lane is concurrently running a separate question — whether the first-opening-root
principle fixes the internal/external metric conversion. DO NOT WORK THAT QUESTION. Item 4 is
deliberately complementary to it.

Fences unchanged: read-only outside your own writes; compute no alpha, kappa, coupling, radius,
scale, root or eigenvalue; no comparison to any measured constant; file:line + verbatim quote for
every claim; bounded negatives state roots and exclusions; report refutations, never repair them.
`alpha_computed = false; proof_authorized = false` on everything you write. Never touch
`a32_holdout/custodian_private/`.

Watch the `C_R` collision throughout: CLEANROOM `C_R` is a compactness ratio; PARENT `C_R(x)` is
the induced Einstein coefficient. `K_H` also collides (Maxwell stiffness vs. the Hermitised Dirac
operator at PRIMITIVE_SOURCE_RECORD_CHIRAL_OPERATOR_GATE_V002.md:42) and is NOT yet in the
namespace register.

---

### ITEM 1 — REGISTER THE IMPOSSIBILITY PROOF (this one forecloses a route class)

Source: `MB Work/alpha_supervision/RESULT_TRACE_COLLAPSE_THEOREM_AND_GRAVITY_GAUGE_IMPOSSIBILITY_2026-07-29.md`
(sealed `a7b82f9a180945844b95dc3931a649591e7c7ad7449e26f035ce7f270cb50d5e`).

Write a governing-chain artifact recording, by path and hash:

(a) THE THEOREM. `Tr_{Lambda^k}(XY) = C(N-2,k-1) Tr_fund(XY)` when at least one of `X,Y` is
    traceless; without tracelessness it acquires `C(N-2,k-2)(Tr X)(Tr Y)`. Cartan is NOT required —
    the map is a `GL(N)`-invariant symmetric bilinear form on `gl(N)`, and `gl(N) = sl(N) + center`
    with `sl(N)` adjoint-irreducible gives a 2-dimensional space of such forms by Schur. Verified
    exact-rational for `N = 3..6`, every `k`, non-commuting generators included.

(b) THE IMPOSSIBILITY PROOF. No x-independent gravity-to-gauge ratio exists on the
    `Lambda^even(C^5)` carrier. Gauge coefficients carry weight `t = (0,3,1)` (Dynkin index),
    gravitational coefficients carry `d = (1,10,5)` (dimension); these are linearly independent
    functionals on the representation ring (minors of `[d;t]` are 3, 1, -5). Assuming
    `a_4^grav = lambda K_Q` on an open interval and using linear independence of `E_1(x+c)` at the
    distinct branch points `0, 12/5, 18/5` forces the `I_1(x)` coefficient to vanish, i.e.
    `1/23040 = 0`. **The contradiction localises entirely on `Lambda^0`: the singlet has dimension
    1 but index 0.**

(c) THE CONSEQUENCE FOR ROUTE PLANNING, which is the operational point: depth selection is
    PROVABLY unavoidable on this carrier. There is no "the depth cancels in the ratio" escape. This
    does not kill the ratio route — which already carried DEPTH_OPEN — it converts an open
    condition into a proven necessity.

(d) THE ADMISSIBILITY CRITERION, which is sharper than the corpus's current statement. The collapse
    requires each threshold level set to satisfy the SECOND-MOMENT CONDITION
    (`sum_s w_s mu_s (x) mu_s` proportional to the Cartan metric), NOT merely to be a Casimir class
    function. Admissible weightings form a 7-dimensional subspace of the 16-dimensional weighting
    space; enumerating all `2^16` level sets gives exactly 27 admissible subsets, only 7 of which
    are unions of whole `Lambda^k` blocks.

(e) THE LIVE COUNTEREXAMPLE INSIDE OUR OWN CODE, and please do not soften this:
    `derive_alpha_br_homogeneous_operator_pullback_v001.py` builds its operator on
    `internal_abs_h_block(flux_degree)` — decomposed by `|H|`, not by Casimir. `|H|` is not a class
    function and cuts across the degree blocks (`Lambda^2` splits 4+6, `Lambda^4` splits 3+2). Exact
    restricted traces give ratios `(0,0)` on the `|H|=0` sector and `(2, 4/3)` on `|H|=1` — neither
    is `(3/2, 1)`, and in the `|H|=0` sector `K_H` and `K_QH` vanish outright. Both indicator
    vectors are INADMISSIBLE. `STAGE8_SCHUR_RATIO_PROTECTION_SCOPE_ATTACK_V001.md` states this
    hazard abstractly; it is now exhibited with exact numbers.
    What SAVED the collapse and is a real hypothesis, not a triviality: the `MASS_CHEVALLEY` return
    map is unitary (`..._pullback_v001.py:92-94` asserts `mass^dag mass = 1` per block), so the mass
    enters as a uniform shift absorbed into `x` rather than as a splitting.

---

### ITEM 2 — RETYPE THE RATIOS, AND FIX FOUR CONSUMERS

The ratios `K_H/K_Q = 3/2` and `K_QH/K_Q = 1` are EXACT and CORRECT. They are NOT dynamical.

(a) The producer's PASS/FAIL gates at
    `derive_alpha_br_common_induced_coefficients_v001.py:264-273` and `:242-244` **CANNOT FAIL** —
    they are identities over the same inventory that defines them. `K_Q = (8/3) K_5` asserts
    `1/24 = 8/192`, i.e. identical expressions. The
    `PASS_COMMON_BR_LOCAL_COEFFICIENT_FUNCTIONS_DEPTH_OPEN` flag is weaker than it reads. These are
    a THIRD and FOURTH instance of the cannot-fail class.

(b) TWO REDUCTIONS THE CORPUS HAS THE INGREDIENTS FOR AND NEVER ASSEMBLES — please record them,
    they are the clean statement of what the ratios mean. With `H = Q + C`,
    `C = diag(1/3,1/3,-2/3,0,0)` the colour-centre cocharacter: `Tr(QC) = 0`, so **`K_QH = K_Q` IS
    exactly the trace-orthogonality of `C` to `Q`**; and `Tr(C^2)/Tr(Q^2) = 1/2`, so
    **`K_H/K_Q = 1 + Tr(C^2)/Tr(Q^2) = 3/2`**. Both are properties of a single 2-plane in the
    weight lattice.

(c) A THIRD FINDING ON THE PARENT-FLUX SADDLE. `reports/alpha_br_parent_flux_local_saddle_v001.md:8,11`
    uses `s(y,x) = C_V y - 2 C_R + K_H/(8y)`; stationarity gives `y = C_R/C_V` and
    `K_H C_V = 8 C_R^2`. Under the collapse, `y = C_R/C_V` is COMPLETELY INDEPENDENT of the
    cocharacter choice, and the entire "H versus Q" distinction — which that report's line 15 flags
    as substantive — enters through EXACTLY ONE RATIONAL NUMBER, `2` versus `4/3`. The `Q` version
    is the `H` version under `K_H -> (2/3) K_H`. The corpus treats this choice as carrying physical
    content; at the level of these coefficients it does not.

(d) FOUR SUPERVISION ARTIFACTS STILL CITE THE RATIOS AS EXECUTED DYNAMICAL EVIDENCE.
    `GRAVITY_EVIDENCE_REGISTER_V001_2026-07-29.md:117-119` (now carries erratum pointer 002),
    `WHAT_THE_GRAVITY_DISCOVERY_MEANS_2026-07-29.md:29`, `PLAN_TO_ALPHA_V006_2026-07-29.md:99`,
    `BOHM_CTP_ABSOLUTE_RESPONSE_ROUTE_SWEEP_2026-07-28.md:246` ("not a hope — it is an executed
    in-tree result"). The retraction at `CONTINUATION_STATE.md:2347` is single-source and unsealed.
    Record the inconsistency; do not edit the sealed one.

(e) DETECTOR GAP TO CLOSE: `corpus_check.py`'s `cannot_fail_checks` still reports 2 and does not
    reach the two found above, which are in the PARENT tree. Extend its scope or its pattern so it
    fires on them, and say in the report which of the two it was blind to and why. Add them as
    named seed cases the detector must catch.

---

### ITEM 3 — REGISTER TWO PROCESS DEFECTS AND THE MODULUS RULING

(a) **G3 HAS NO RELEASE CONDITION.** The one genuine comparison ban says "before Stage 12
    authorizes the single comparison". `stage12_exists_in_corpus = false`
    (`STAGE8_STEP_LIST_AND_DOWNSTREAM_STAGE_FINDING_V001.md:204`;
    `STAGE8_STAGE_LABEL_RETIREMENT_9_10_11_V001.md:114`). Read literally the fence NEVER OPENS, and
    the corpus contains no procedure for weakening a fence. This is a live structural defect in the
    fence apparatus. Note it is also MOOT in the governing chain — bounded negative: zero cleanroom
    files cite either G3 carrier (`19_DIMENSIONLESS_RATIO_SPEC_V001.md`,
    `45_STAGE10_HANDOFF_GEOMETRIC_BRIEF_V001.md`), and
    `STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_AUTHORITY_FABLE_V002.md:273-278` explicitly
    replaced the dangling G1-G5 reference with rules containing NO comparison clause. Record BOTH
    facts; do not rule on whether the fence should be repaired.

(b) **"SLOT 18 IS LAST" WAS NEVER SEALED TEXT.** `STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V002.md:119-140`
    carries no ordering language; the frozen order at `:142-156` is a separate NINE-item
    electromagnetic sequence that does not contain slot 18; the JSON encodes the slots as an
    unordered dictionary, the only ordered array being `EM_dependency_order`, length 9. The genuine
    sealed dependency is that A32 unmasking sits behind ALPHA-RESULT-SEAL (`V011:1816-1819`), so the
    HOLDOUT cannot complete before alpha — the PREDICTION can be derived any time. **Slot 18 is
    workable in parallel.**

(c) **THE MODULUS RADIUS IS NOT THE CELL RADIUS, AND THE GATE PROVES IT.** Source:
    `RESULT_MODULUS_RADIUS_VS_RECORD_CELL_AND_THE_UNATTEMPTED_BRIDGE_2026-07-29.md`. The decisive
    quote, from `COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:53-61`: "every `R = beta c Delta tau,
    beta > 0` preserves the base interval, phase periodicity, topology, gauge covariance, and unit
    character while changing `K_KK` by `beta^2`." Handing the gate a fully derived record interval
    leaves a one-parameter family free. Also record: S3 is MEMO-ONLY (no audit script, no result
    JSON, no test — bounded negative), and `C_R = 1` is an ADOPTED Level-1 rule with the threshold
    passed in as a script function argument, not a projected curvature term.

---

### ITEM 4 — THE CONSTRUCTIVE PIECE: SPECIFY THE MISSING CROSS-SECTOR METRIC RULE

This is the item that matters, and it is complementary to the reviewer's concurrent run rather than
overlapping it. The reviewer is asking *whether the first-opening condition supplies* the missing
object. You are asking *what the missing object would have to satisfy to be admissible at all* — so
that when a candidate appears, from that run or any other, we can evaluate it in an hour instead of
a week.

THE GAP, named by the corpus in two independent places:
- `COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:63-66` — "The Fubini-Study metric fixes dimensionless
  distances in projective state space. It does not fix their dimensional conversion relative to the
  spacetime metric or `ell_P`."
- `_external_handoffs/fable_alpha_cleanroom/OUTPUT/45_STAGE10_HANDOFF_GEOMETRIC_BRIEF_V001.md:36-42`
  and `:58-62` — "The causal diamond is present but unconsulted ... the cell's Lorentzian geometry
  never entered"; "the ratio of internal (Fubini-Study/phase) geometry to external
  (Lorentzian/diamond) geometry of one record cell. This is the first point in the program where
  the gravity-facing geometry becomes load-bearing for the coupling."

WRITE A SPECIFICATION ANSWERING:

1. **What must it derive?** State the target object precisely and dimensionally: a map from
   internal/projective geometric data on one record cell to a spacetime length scale, or
   equivalently a determination of `beta`. Say exactly what inputs are admissible and what its
   output type is.

2. **What is it forbidden from assuming?** Enumerate the fences it must clear, by file:line: no
   adoption by dimensional analogy; no circular use of an order the corpus forbids; F'-1 (no assumed
   clustering or decay); F'-5 (no carrier-indexed constants in bounds); R-9 (never bare "kappa"); no
   entry of any measured constant; no selection by value. Quote each.

3. **What must it OVERDETERMINE?** This is the crux and the most likely failure mode. Permissions
   compose and never force a number; only overdetermination does. State precisely which two
   independent requirements would have to meet on `beta` such that only one value satisfies both. A
   candidate supplying one equation for one unknown is NOT enough if that equation is a permission.
   **Cite the precedent:** `boundary_access_closure_threshold_principle_v001.md` was typed
   `CELL_CONSTRAINT_ONLY` and "RETIRED AS A STANDALONE K_R SELECTOR" for exactly this reason — quote
   its typing and say what a successor must do differently.

4. **What already-executed no-gos must it survive?** At minimum
   `alpha_first_durable_capacity_moduli_v001` (BLOCKED_CAPACITY_ONE_LEAVES_CONTINUOUS_MODULI),
   `alpha_capacity_constrained_induced_action_v001`
   (NO_GO_CAPACITY_CONSTRAINED_LOGDET_HAS_NO_INTERIOR_RQ_STATIONARY_POINT),
   `alpha_coupled_flux_logdet_modulus_selection_v001`
   (NO_GO_ONE_STATISTICS_COUPLED_LOGDET_NO_FINITE_RADIUS_SADDLE), and
   `alpha_coupled_flux_first_capacity_moduli_v001` (which withdraws the earlier `r=1` claims).
   SEARCH FOR MORE — assume they exist. For each, state what failed and construct the specific test
   a new candidate must pass to show it escapes that failure rather than repeating it.

5. **What would falsify it?** Write a real falsifier, not a tautology. Frozen before any candidate
   is evaluated.

6. **Bounded prior-art search, and do this FIRST.** Has anyone attempted this? Search all four roots
   for: dimensional conversion, metric conversion, internal to external, state space to spacetime,
   phase to length, fiber metric, radion stabilization, modulus stabilization, cross-sector metric,
   scale bridge. Prefer OLDER artifacts and search the PARENT tree hard — it is ~5,930 files and
   most are cited by nothing. **If prior work exists, it governs and this becomes a
   re-derivation, which must be disclosed as such on the face of the artifact.**

Do NOT attempt the derivation. Specify the target. A spec with a real falsifier, sealed before any
candidate exists, is worth more here than an attempt.

---

Report back with: paths and hashes of everything written, the register rows added, the detector-gap
result from item 2(e), and — for item 4 — the prior-art search result FIRST, before the spec, since
it may make the spec a re-derivation.
