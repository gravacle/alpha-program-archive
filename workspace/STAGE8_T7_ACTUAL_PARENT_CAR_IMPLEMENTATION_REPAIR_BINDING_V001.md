# Stage-8 T7 Actual-Parent CAR Implementation Repair Binding V001

Date: 2026-07-25

## Status

```text
APPEND_ONLY_REPAIR_BINDING_SEALED_BEFORE_AUTHORING
```

This binding freezes the scope, design, and every new threshold of the
Phase-A implementation repairs BEFORE any repair code is written. It is
subordinate to the sealed Phase-A specification (789338ad…) and the sealed
Phase-A execution binding (6fa8845a…); it relaxes nothing in either.

Authorities:

```text
Hostile implementation re-review (verdict NOT_READY):
/Users/bgm/MB Work/alpha_supervision/REVIEW_2026-07-25_route2_implementation_hostile_rereview.md
Hostile spec review (verdict READY_WITH_CONDITIONS):
/Users/bgm/MB Work/alpha_supervision/REVIEW_2026-07-25_route2_phaseA_spec_hostile_preexecution.md
Custody note Sections 5-6:
STAGE8_CODEX_STANDING_DOWN_CUSTODY_V001.md (d8b587a1…)
```

## R0 - Custody Section-6 item 3: DISCHARGED

The hostile re-review of the refactored Route-2-to-O6 production
compression returned TAUTOLOGY_FREE: closed forms independently rederived;
expected values are typed closed forms outside the tested code path;
outcome-index selection is fixed by the closed form; the two coverage
caveats (reshape-convention blindness at source dimension 1; outcome
index 0 vs production index 1) are each independently closed by existing
3e-9 gates (primary spectral-Kraus gate; independent kraus_from_spectral
residuals; comparator pointer-kernel pin). Item 3 of the custody note's
Section 6 is closed by that recorded return. Items 1, 2, 4, 5, 6 remain
open and are addressed below.

## R1 - Repair scope (append-only v002 successors)

The v001 scripts remain in place untouched. The following v002 successors
are authorized, each repairing ONLY the enumerated findings:

1. `scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_v002.py`
   - Finding 1: single-read buffer hashing (read once, hash the buffer,
     parse JSON from the buffer, np.load from BytesIO; no re-read window).
   - Finding 5: rebuild every Kraus member K_x = sum_lambda
     <x|P_lambda|ready> u_lambda from stored propagators + projectors for
     BOTH lanes and gate against stored direct Kraus members at 3e-9;
     enforce the adjoint-exchange residual for both lanes at 3e-9.
   - Finding 6: compute E_conn's fourth term transported, matching the
     spec text exactly.
   - Finding 7: output flags renamed comparison_supports_*; no A7-level
     protected-flag names may appear as true in comparator output.
   - Finding 8: record resolved absolute input and output paths and a
     controller-context field in the sealed output.
   - Execution-binding B2/B3 enforcement: E_conn components pinned to
     (7/100,-11/100); same-history identity set = all five frozen values,
     both kernels, both ell, at 3e-9.
   - LINEAGE GATE (Section-6 item 2, in-band closure): for each lane,
     rebuild each declared one-particle propagator from that lane's
     STORED generator pieces (R2 below) by an independent midpoint
     product integrator (Hermitian-eigendecomposition exponentials) and
     require agreement with the stored propagator in operator 2-norm
     within the preregistered budgets of R3. Every (ell, lambda, history)
     combination used by any gated response must pass separately.
2. `scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_primary_v002.py`
   and `..._independent_v002.py`
   - Sole functional change: store the generator pieces per R2 in the
     precomparison bundle (plus the bundle-schema field naming that
     storage). No numerical pipeline, threshold, quadrature, ordering, or
     convention may change. The v002 lanes must reproduce the v001
     computation paths verbatim otherwise.
   - Execution-binding B3: primary lane executes the same-history
     identity checks for all five frozen values (it already computes at
     the N_t=48 resolution; the check set is widened, nothing removed).
   - Execution-binding B4: primary lane's isolated Route-1 rerun
     additionally value-compares every completed component and exhaustive
     kernel value against the canonical sealed result (6dbda44a…) at
     1e-12 absolute per component.
3. `scripts/run_stage8_t7_actual_parent_car_pipeline_v002.py`
   - Finding 2: re-hash each lane target immediately before and after its
     subprocess; record both digests in the receipt; block on mismatch
     with the manifest row.
   - Finding 4: assert the complete required row set (controller,
     launcher, both derive lanes, comparator, all three v002-relevant
     test files) is present in the manifest BEFORE running any lane.
   - Finding 3 (architectural): after sealing each receipt, produce a
     detached GPG signature of the receipt with the same disclosure key
     as the manifest (fingerprint 18488605D44F65A9B57B610AA5F3A86512A04D61);
     absence of the signing capability blocks production (fail closed).
   - Finding 8: cross-check the comparator's recorded resolved paths
     against the canonical paths; mismatch blocks.
   - Route the pipeline through the v002 scripts and the v002 launcher.
4. `scripts/launch_stage8_t7_content_addressed_runtime_v002.py`
   - Finding 2: hash the resolved target file and embed target_sha256 in
     the runtime attestation; lanes bind it into their bundles; the
     comparator (v002) checks the recorded value against the manifest row.
   - Finding 3 disclosure: the attestation records
     `attestation_is_launcher_cooperative_only = true`.
5. Test successors (append-only): primary-lane failure-fence tests
   (authority drift, immutable-output refusal, attestation absence,
   blocked-write path), launcher tests (allowlist escape, symlink,
   runtime drift, attestation content incl. target_sha256), controller
   integration test against a FIXTURE workspace (never the canonical
   root), comparator v002 tests covering the new lineage gate (a
   fabricated-u bundle must BLOCK) and the new Kraus/adjoint gates.

## R2 - Stored generator pieces (bundle schema extension)

Each lane stores, per ell and per midpoint/stage time on its own grid
(primary: the 48 Strang midpoints t_k=(k+1/2)/48; independent: the 384
RK4 step midpoints t=(k+1/2)/384):

```text
M_spatial(t_k)   8x8 complex (Galerkin causal-ball multiplication);
B_spatial(t_k)   8x8 complex (Galerkin b_D multiplication);
```

plus once per ell: the spatial momentum matrices entering h_0, and the
fixed spinor factors (alpha_j, S_n) with their sealed convention labels.
The comparator assembles h_lambda(t;a) = h_0 + lambda v(t) M(t) (x) S_n
+ a J(t), J(t) = -B(t) (x) alpha_x, from these pieces with its OWN
tensor-assembly code (no import from either lane), using v(t) and
r(t)=min(t,1-t) typed from the sealed spec text.

Fabrication economics: after this gate, a passing bundle's propagators
must solve the declared generator's ODE to the R3 budgets — which is
precisely the lineage claim. Colluding fabrication then requires actually
integrating the declared parent, i.e., performing the computation.

## R3 - Preregistered lineage budgets (frozen now, before any code runs)

The comparator's midpoint-product rebuild differs from the lane
integrators by bounded local error (midpoint and Strang are both
second-order; RK4 is fourth-order). From the sealed Hermite n=2 baseline
tail scale (d_24_48 up to 1.16e-4), frozen with wide, outcome-blind
headroom:

```text
primary lineage budget      (N_t=48 grid):   5e-3  operator 2-norm;
independent lineage budget  (N_t=384 grid):  1e-4  operator 2-norm.
```

These are lineage-authenticity gates, not precision claims; they sit
orders of magnitude below any O(1) fabrication and orders above the
integrator-difference scale. They may not be revised after any production
value is seen; revision requires an append-only successor citing a
retained failure.

## R4 - Ordering

1. Author v002 scripts + tests per R1 (construction lane).
2. Verify: full test suites pass under the pinned runtime; fresh-context
   hostile verification lane reviews every v002 against this binding and
   the two review returns; a blocking finding stops the line.
3. Only then: implementation manifest v001 covering the complete row set
   (v002 production files + launcher + controller + tests), adjacent
   seal, detached GPG signature, and an external trust anchor recorded
   before production.
4. Only then: production per the Phase-A spec and execution binding
   (independent first; receipts; comparator v002).

## R5 - No relaxation and no promotion

No sealed threshold, formula, carrier, history value, verdict string, or
fence is altered. The v001 scripts are not relabeled. Nothing here
discharges any Phase-A obligation; this binding only constrains how the
implementation may earn the right to run.

## Protected status

```text
actual_parent_regulated_CAR_operator_response_derived = false
actual_parent_same_carrier_one_source_restriction_derived = false
route1_special_case_reexecution_passed = false
actual_finite_parent_state_evaluation_derived = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
