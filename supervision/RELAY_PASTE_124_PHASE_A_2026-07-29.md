PASTE 124 — CODEX. FULL PHASE A WORK PACKAGE. Work items in order; do not stop at the first
obstruction — if an item blocks, record the obstruction at a file:line (that is a sealable
result under ratified convention C2) and MOVE TO THE NEXT ITEM.

TO: Codex. FROM: reviewer lane via principal. 2026-07-29.
AUTHORITY: PLAN_TO_ALPHA_V008_2026-07-29.md (sealed) Phase A. Read it first.

A1. CLEAR THE THREE RED CLASSES from corpus_check.py's first run.
    (a) seal_integrity: 20 issues — seal the load-bearing artifacts it names. Do NOT bulk-seal
        the 287-file backlog; seal exactly what the check flags.
    (b) authority_currency: 2 issues — principal rulings not cited by any governing-chain
        artifact. The known one is Q1: PREREGISTRATION_ENCODING_PRECEDENCE_PRINCIPAL_DECISION_
        2026-07-29.md. Record it in the cleanroom chain and index it in STAGE8_LANE_STATUS.md
        in the same act. RULING SUMMARY: `stage_dependencies` is AUTHORITATIVE for graph
        structure (it is the stricter encoding, and the one the evaluator consumes);
        `stage_dag` is DESCRIPTIVE **and its non-seal preconditions REMAIN BINDING** — say
        that explicitly on the recording artifact's face, it is the likeliest misreading. No
        bytes of the preregistration are changed; immutability intact; R-14 "applied, not
        amended" is the precedent.
    (c) deploy_state: 1 issue — self-referential timing; re-run after committing.
    THEN RE-RUN corpus_check --report and report the new verdict.

A2. REPAIR THE EVALUATOR FIELD NAME. scripts/evaluate_bid_stage_dag_v011.py REPORT_KEYS
    (~:63-72) and the lookup (~:109) use `subject_sha256`; the IMMUTABLE preregistration
    (provenance/boundary_incidence_dynamics_preregistration_v011.json, review_stage_semantics.
    report_schema_required_fields) says `bundle_sha256`. Comparison at ~:100 is
    `if set(report) != REPORT_KEYS` — exact set equality, returns immediately. VERIFIED: the
    mismatch is EXACTLY ONE FIELD; all other keys identical. THE EVALUATOR IS THE SIDE THAT
    CHANGES — it has no seal sidecar and is named in no immutability clause. Do not touch the
    preregistration.

A3. AUTHOR THE MISSING `--subjects` FILE. The evaluator's `--subjects` is required=True and no
    such file exists in any root, so the ladder evaluator is currently UNINVOKABLE. It must map
    all 11 stages to the sha256 of each stage's immutable subject. Use the eleven-node set from
    `stage_dependencies` (authoritative per A1b). If a stage's immutable subject is not yet
    determinable, record that stage as UNRESOLVED with the reason — do NOT invent a hash.

A4. SEAL AND REPAIR stage8_battery_evaluator_v001.py. It is the corpus's designated sole
    authority for the Stage-8 verdict and is DISQUALIFIED by the corpus's own permanent
    regression obligation 7: no sidecar; three Python `assert`s in its selftest; prints
    "SELFTEST PASS" UNCHANGED under `python3 -O` where those asserts are compiled out. Replace
    asserts with unconditional checks that survive -O; prove it by running both ways and
    reporting both outputs. ALSO: its selftest CONSTRUCTS the leak it then detects — replace
    with a test against real state or a committed fixture. Then sidecar it. Then RE-RUN and
    report the verdict and blocker list.

A5. MAKE predictions.json ENFORCED. stage8_execution/predictions.json is sealed-before-
    execution and carries a pass condition for every T00-T16 and NC1-NC5 — and the evaluator
    NEVER READS IT (check_prediction_fence is a lexical numeral fence only). This is how
    T01/T02/T11 carry `pass:true` against voided results: they are CORRECTLY HASHED WRONG
    ANSWERS. Add condition enforcement: each report is compared against its preregistered
    condition. REPORT what changes verdict once enforced — do not repair the failing tests.

A6. WIDEN THE T15 ANTI-NUMEROLOGY FENCE. check_transform_fence iterates artifact_manifest.txt
    (52 lines) against a 3937-file cleanroom — 1.3% coverage. Widen to the full corpus.

A7. FIX THE CENSUS HARDWIRE you found in paste 122: the census script is hardwired to the
    superseded v001 fingerprint path, so the fingerprint refresh relocated the blocker rather
    than clearing it. Point it at the successor or make the path a parameter.

A8. NEW DETECTOR FOR corpus_check.py — CANNOT-FAIL CHECKS. Two instances are now documented:
    (i) scripts/audit_bid_absolute_record_scale_identifiability_v001.py builds the rescaled
    generator by DIVIDING by the same factor it multiplies the duration by, so its require()
    cannot fail for any operator; (ii) _external_handoffs/fable_alpha_cleanroom/OUTPUT/
    20_ratio_assembly_v001.py `require(rho.t == 0, "P1 violated")` is an identity over its own
    hand-entered table (all candidates assigned the same exponent), so it can never fire.
    ADD A CHECK that flags require()/assert-style conditions that are identities over
    hand-entered inputs, or that compare a quantity to itself after inverse operations. Add as
    YELLOW with a frozen baseline. *** THIS CLASS IS MORE DANGEROUS THAN THE ONES ALREADY
    BASELINED BECAUSE IT LOOKS LIKE VERIFICATION. ***

A9. SLOT-TO-STATUS MAP. Author one artifact mapping each of the EIGHTEEN open Q_spec slots
    (STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V002.md:119-138) to: its current status, the
    artifact(s) that bear on it, its owner, and whether it is lane-executable / principal /
    new-mathematics. NO artifact currently carries this and it is the plan's spine. Record the
    naming correspondence explicitly: slot 1 = "O2/record scale", slot 6 = "O3/UV boundary",
    slot 9 = "O1 / the c_R exclusion" — these were reinvented under new names this week.
    ADOPT NOTHING; this is an index.

FENCES: no computation of alpha, kappa_record, kappa_Thomson, C-L3, x, rho, T_R; do not touch
C4, O-1/F'-5, or C-L2; report refutations, never repair them; a named obstruction at a
file:line IS a sealable result (C2, ratified).
DEFINITION OF DONE: SEALED, MIRRORED, COMMITTED, AND PUSHED. Report per item: DONE / BLOCKED
(with the obstruction at a file:line) / NOT REACHED. End with deploy_status output and the
corpus_check --report verdict.
alpha_computed = false; proof_authorized = false.
