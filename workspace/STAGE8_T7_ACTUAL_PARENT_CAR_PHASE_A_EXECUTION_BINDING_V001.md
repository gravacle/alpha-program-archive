# Stage-8 T7 Actual-Parent CAR Phase-A Execution Binding V001

Date: 2026-07-25

## Status

```text
APPEND_ONLY_PRE_EXECUTION_BINDING
```

This binding is sealed BEFORE any Phase-A production execution. It narrows
and gates the sealed Phase-A specification; it relaxes nothing. The sealed
spec remains unchanged:

```text
STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md
789338adb7d3d36da453113e98f371a4f92543cf2652b047f8481c407bed5bc3
```

It implements the three CONDITIONS of the hostile pre-execution review
recorded at:

```text
/Users/bgm/MB Work/alpha_supervision/REVIEW_2026-07-25_route2_phaseA_spec_hostile_preexecution.md
```

(verdict READY_WITH_CONDITIONS), under the custody transferred by:

```text
STAGE8_CODEX_STANDING_DOWN_CUSTODY_V001.md
d8b587a1423dc48ef1b1a53b64260df1a12a3f97e90ca03dafefbdba660be5db
LANE_CHANGE_CUSTODY_CLAUDE_CONSTRUCTION_V001.md
(seal fc585326fb90003494ceb008a5c5b9af9b5c2ed3d794578c94c74657b8dd363d)
```

None of the bindings below is chosen with knowledge of any response value,
residual, or gate outcome. No production lane has run.

## B1 - Production gate (review CONDITIONS 1 and 3)

Phase-A production execution is PROHIBITED until every item below exists
and verifies:

1. Custody-note Section-6 items 1-3 are discharged append-only:
   canonical input binding with independently issued execution receipts;
   generator-to-propagator lineage for the actual parent; a hostile
   re-review of the refactored Route-2-to-O6 production compression that
   returns a non-blocking verdict, recorded in the supervision directory.
2. The implementation manifest, its adjacent seal, and its detached
   signature exist at the paths pinned in the draft controller, the
   manifest covers every executable implementation file (controller,
   launcher, both derive lanes, comparator, and all three test files)
   by SHA-256, and an external trust anchor for the manifest digest is
   recorded before production.
3. Production runs only through the controller path
   (`scripts/run_stage8_t7_actual_parent_car_pipeline_v001.py` or its
   append-only successor), which must verify the implementation manifest
   and signature, require pre-execution absence of every output, run the
   independent lane first, and issue an immutable sealed receipt per lane.
   A derive or comparator output produced outside a receipted controller
   run is void and may not be sealed as a Phase-A artifact.
4. The comparison verdict is authoritative only when its receipt chain
   (independent receipt, primary receipt, comparison receipt) exists,
   each receipt's recorded output hashes match the sealed outputs on
   disk, and the receipts' implementation-manifest digest matches the
   sealed manifest.

Lane-ordering proof (CONDITION 3) is carried by the receipts: the
independent lane's receipt must be sealed, immutable, and timestamped
before the primary lane starts, and the independent receipt must record
`output_paths_absent_before_execution = true` for the primary outputs per
the controller's pre-checks. Any post-hoc reconstruction of lane order is
inadmissible.

## B2 - E_conn history-pair pinning (review CONDITION 2)

Every component of `E_conn(ell)` in spec section A6 is evaluated at the
single frozen history pair

```text
(a_+,a_-)=(7/100,-11/100)
```

— the same pair that defines `S_conn(ell)` — separately for each `ell`.
Explicitly, all four elements of the max:

```text
d_24_48(all)                       at (7/100,-11/100);
primary-vs-independent quadrature  at (7/100,-11/100);
primary-vs-independent transported at (7/100,-11/100);
independent 192-vs-384 transported at (7/100,-11/100).
```

No other pair may be substituted for any component. This removes the
discretionary pair choice; it is pinned before any value is known.

## B3 - Same-history identity set pinning (review NOTE 5)

The same-history identity checks of A6 (`R_all^(1)(a,a)=I` and
`0<=R_pointer^(1)(a,a)<=I`) are executed for ALL five frozen history
values

```text
a in {0, 7/100, -11/100, 13/100, 4/100}
```

for both `ell` values, at the primary resolution `N_t=48`. All ten cases
per kernel must pass separately at the sealed `3e-9` residual.

## B4 - Route-1 canonical value comparison (review NOTE 6)

In addition to the sealed A5 closed-form comparison at `1e-10`, the
isolated-snapshot Route-1 re-execution must be value-compared against the
canonical sealed result

```text
stage8_execution/work/T07_primitive_operator_response_v001.json
6dbda44a0f21a28b57f114654a6df79fc091ccfd601c38518fd5cf5f21697dcc
```

component by component (every completed component and exhaustive kernel
value at both frozen comparator pairs), with absolute difference at most

```text
1e-12
```

per component. This bound is fixed now, before re-execution, well below
the analytic gate and well above reproduction noise recorded at first
execution (~4e-16). Failure blocks Phase A.

## B5 - Standing interpretive notes (review NOTES 4, 7, 8, 9)

1. The within-lane Gaussian-sum/direct agreement at `3e-9` (A5) is
   bookkeeping-grade evidence only: `H_direct` is block-diagonalized by
   the record spectral resolution, so this equality cannot certify
   `h_0`, `M(t)`, or `B_D(t)`. The certifying comparison is the
   cross-lane Strang-vs-RK4 transported comparison. No sealed artifact
   may cite the within-lane residual as physics evidence.
2. A failure of the preregistered non-vacuity gate
   `S_conn(ell) > 20 E_conn(ell)` is a SENSITIVITY BLOCK — an honest,
   reportable, preserved outcome — not an implementation defect. The
   multiplier 20 is frozen for this version. Any successor revising it
   must cite the retained failure explicitly and may not be authored by
   reference to a desired verdict.
3. The carrier metadata label `spinor dimension=32` in A1 denotes the
   total one-particle dimension (8 spatial x 4 spinor), an inherited
   field-name convention. Executors and reviewers read it as such; no
   artifact edit is made.

## B6 - No relaxation and no promotion

This binding adds gates and pins choices. It does not alter any sealed
threshold, formula, carrier, history value, or verdict string; it does
not discharge any obligation; it derives nothing.

## Protected status

```text
actual_parent_regulated_CAR_operator_response_derived = false
actual_parent_same_carrier_one_source_restriction_derived = false
route1_special_case_reexecution_passed = false
actual_finite_parent_state_evaluation_derived = false
actual_finite_parent_operator_to_scalar_bridge_derived = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
