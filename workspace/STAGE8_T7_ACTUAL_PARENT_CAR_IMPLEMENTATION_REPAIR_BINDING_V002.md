# Stage-8 T7 Actual-Parent CAR Implementation Repair Binding V002

Date: 2026-07-25 (evening)

## Status

```text
APPEND_ONLY_REPAIR_BINDING_SEALED_BEFORE_AUTHORING
```

Successor to STAGE8_T7_ACTUAL_PARENT_CAR_IMPLEMENTATION_REPAIR_BINDING_
V001 (dc7cdd15…), whose R2 fabrication-economics claim is falsified by
the sealed erratum (STAGE8_T7_REPAIR_BINDING_R2_LINEAGE_CLAIM_
FALSIFICATION_ERRATUM_V001). Implements the external Fable audit's
confirmed findings (supervision record: EXTERNAL_AUDIT_2026-07-25_
fable_v002_return.md) and the GPG supersession amendment. All new
tolerances are frozen HERE, before any repair code exists and with zero
production values in existence.

## S1 - Repair scope (v003 successors; derive lanes UNCHANGED)

The audit found zero scope drift in the two derive lanes; they remain at
v002. New files:

1. `scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_v003.py`
   (base: v002), changes:
   a. PIECE AUTHENTICITY (Blocking 1): the comparator reconstructs EVERY
      generator piece from the sealed spec text with its OWN third
      implementation (no import from either lane): Hermite basis and
      momentum matrices p_j; M(t_k)=Q 1_(|x|<=r(t_k)) Q and
      B(t_k)=Q b_D(t_k) Q at every midpoint of BOTH lanes' grids (48 and
      384), reproducing each lane's declared quadrature rule exactly as
      pinned in the sealed Hermite numerics protocol (primary 10/10/20,
      independent 12/12/24); alpha_stack and S_n typed from the sealed
      spinor convention. Stored pieces must match the reconstruction:
      - alpha_stack, Sn: max abs entry difference <= 2e-15;
      - primary-lane p/M/B/h0: operator 2-norm <= 2e-11;
      - independent-lane p/M/B/h0 after transport through the PINNED
        overlap: operator 2-norm <= 5e-11.
      Any failure returns the sealed blocked verdict. This restores the
      falsified R2 claim: a passing bundle's propagators must then solve
      the SEALED parent's ODE within the (unchanged) R3 budgets.
   b. TRANSPORT PIN (Blocking 2, one line + docstring): require
      `basis_overlap_key == "basis_overlap_primary_from_independent"`;
      every transported comparison uses the array under that pinned name;
      the false docstring at the lineage validator is corrected.
   c. TIED DIAGNOSTICS (Major): for every midpoint k and ell,
      `diag_connection_midpoint__<ell>[k] == -kron(genpiece_B_stack__<ell>[k], alpha_x)`
      at 2e-11 (independent lane: after pinned transport, 5e-11);
      `diag_h0__<ell> == genpiece_h0__<ell>` at 2e-15. The connection
      non-vacuity gate thereby binds to the same matrices the lineage
      gate integrates.
   d. RECEIPT-CHAIN RECORDING (Major): new CLI inputs
      `--independent-receipt-sha256`, `--primary-receipt-sha256`;
      recorded in the sealed output. The controller_context comment is
      corrected to state plainly: these fields are RECORDINGS for the
      anchored receipt chain, not self-authentication.
2. `scripts/launch_stage8_t7_content_addressed_runtime_v003.py`
   (base: v002): READ-ONCE execution (Minor): read the target bytes
   once, hash that buffer, execute that same buffer (compile + exec with
   __main__/__file__ semantics); the attestation's target_sha256 is the
   digest of the executed bytes by construction.
3. `scripts/run_stage8_t7_actual_parent_car_pipeline_v003.py`
   (base: v002), changes:
   a. GPG REMOVED per the supersession amendment (no signing, no .asc,
      no fingerprint checks); receipts remain sealed immutable JSON.
   b. PER-LANE INVOCATION: `--lane {independent,primary,comparison}`
      runs exactly one lane, so each receipt is externally anchored
      (commit+push) BEFORE the next lane runs. Lane-order enforcement:
      the primary lane refuses to run unless the independent receipt
      (+seal) exists and verifies; comparison refuses unless both lane
      receipts exist and verify.
   c. PRE-FLIGHT (Major + amendment rule): before ANY canonical path is
      consumed in a given invocation, verify ALL fail-closed
      preconditions: implementation manifest v002 (complete row set for
      the v003 file inventory) + adjacent seal; launcher/target manifest
      hashes; absence of ALL FIVE canonical production outputs and ALL
      THREE receipts before the independent lane (absence of the
      remaining outputs/receipts appropriate to later lanes); v003
      comparator reachable. Any pre-flight failure blocks BEFORE any
      output exists.
   d. RECEIPT ATTESTATION FIX (Major): the hardcoded
      `output_paths_absent_before_execution` is replaced by
      `paths_verified_absent`: the exact list of canonical paths whose
      absence was verified in pre-flight, so the independent receipt
      attests the absence of the PRIMARY outputs as B1 designates.
   e. Passes the receipt digests to the v003 comparator (S1-1d) and
      cross-checks the recorded values.
4. `scripts/test_compare_stage8_t7_actual_parent_regulated_car_operator_response_v003.py`,
   `scripts/test_stage8_t7_launcher_v003.py`,
   `scripts/test_stage8_t7_controller_v003.py` (bases: v002 tests):
   ported plus NEW mandatory negatives:
   - SURROGATE-PAIR TEST (audit's missing class): a fully
     self-consistent surrogate bundle (zero/diagonal pieces with
     closed-form exponential propagators, per the auditor's reproduced
     exploit) MUST BLOCK on the piece-reconstruction gate;
   - a wrong-quadrature piece set (correct construction, wrong declared
     rule) MUST BLOCK;
   - basis_overlap_key != pinned name MUST BLOCK;
   - untied diag_connection (O(1) Hermitian junk with B_stack ~ 0) MUST
     BLOCK;
   - controller pre-flight failures (missing manifest row; pre-existing
     canonical output; missing prior-lane receipt) MUST BLOCK before any
     fixture output is created;
   - launcher A/B/A swap: the executed bytes are the hashed bytes by
     construction (test executes a fixture target and confirms the
     attestation digest equals the digest of the source that actually
     ran, including under an adversarial swap attempt after resolve).
   The genuine-fixture PASS test must be rebuilt on SPEC-CONFORMING
   pieces (real Hermite/ball/b_D construction at fixture scale is not
   possible on the 8-dim spatial fixture carrier — the fixture must
   instead monkeypatch the comparator's reconstruction oracle explicitly
   and be labeled as doing so, so no test ever again demonstrates that
   arbitrary pieces pass the production gate).

## S2 - Frozen tolerances (chosen now, outcome-blind)

```text
alpha/Sn typed-equality             <= 2e-15  max abs entry;
primary piece reconstruction        <= 2e-11  operator 2-norm;
independent piece reconstruction    <= 5e-11  operator 2-norm (transported);
diag-connection tie                 <= 2e-11 / 5e-11 (transported);
diag-h0 tie                         <= 2e-15;
R3 lineage budgets                  UNCHANGED (5e-3 / 1e-4).
```

Rationale recorded: reconstruction with the SAME declared quadrature
rule is deterministic arithmetic on identical nodes — machine-precision
agreement expected; 2e-11 matches the sealed reconstruction-pin scale
used throughout the comparator; the transported allowance covers
composition with the 2e-11-unitary pinned overlap. These sit >=10^7
below any O(1) surrogate. Not revisable after any production value
exists.

## S3 - Anchoring and authorization procedure (per the amendment)

Pre-flight by the construction lane before the first lane: `git push`
capability to the archive verified (dry-run) and recorded. Sequence:
Brian's typed authorization artifact sealed+pushed -> independent lane ->
anchor push -> primary lane -> anchor push -> comparison lane -> anchor
push. Any push failure stops the sequence before the next lane.

## S4 - Ordering

1. Author v003 files per S1 (construction lane).
2. All test suites green under the pinned runtime.
3. Fresh-context hostile verification with an EXPLICIT surrogate-pair /
   self-consistent-substitution attack mandate (calibration lesson from
   the erratum).
4. Implementation manifest v002 over the v003 inventory + v002 derive
   lanes; seal; anchor push (no signature, per the amendment).
5. External re-audit via Brian's relay (different model family).
6. Brian's recorded typed authorization.
7. Production per S3. Not before.

## S5 - No relaxation and no promotion

No sealed spec threshold, formula, carrier, history value, or verdict
string changes. The v002 comparator/controller/launcher are not
relabeled; they remain preserved non-production artifacts. Nothing here
discharges any Phase-A obligation.

## Protected status

```text
actual_parent_regulated_CAR_operator_response_derived = false
generator_to_propagator_lineage_in_band_closed = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
