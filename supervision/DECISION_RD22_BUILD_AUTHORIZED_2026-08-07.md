# DECISION OF RECORD — RD-22: THE EVALUATOR BUILD AUTHORIZED (2026-08-07)

**Principal ruling (Brian Mulconrey), 2026-08-07, three parts:**

**1. RD-22 AUTHORIZATION.** The A35 evaluator implementation is authorized,
governed by the sealed specification V005
(`STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md`, SHA-256
`f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b`),
which stands BUILD-READY per both cross-family reviewers (Q-583, Q-584).
Scope: implementation of the parent runner, producer, verifier, manifests,
schemas, and fixtures; and the FIRST STRUCTURAL RUN — the 56 STRUCTURAL checks
and the structural fixtures only. The 10 GATED-EXECUTION checks and gated
fixtures return NOT_RUN_GATE by construction. THIS AUTHORIZATION OPENS NO
PHYSICAL GATE: alpha_computed = false; proof_authorized = false;
kappa_record_computed = false; no member binding, fixed point, end test,
numeric evaluation of any physical quantity, or comparison to measured
constants. A runner PASS confers no seal and no physics authority (the
authority firewall of record).

**2. THE RUNTIME PIN.** The authorized content triple:
```text
runtime_subject = {
  snapshot_sha256 = 50a6fc141a45451678aa7543e4f267ce26beb6e53182170b478acb6fb0e0f5bb
                    (provenance/primitive_step6_runtime_snapshot_v012.json),
  gate_sha256     = 2ad7f72a88184c11e1253f2c47598fca11e60d05e8e71a26db4e19b16bf98d42
                    (primitive_step6_content_addressed_runtime_gate_v010.md — the
                     pinned snapshot's own governing contract),
  trust_root      = extracted from the pinned snapshot at R0 and displayed
}
```
Ground: SP14's "runtime v012" names the snapshot; the triple is internally
consistent. Fail-closed: a trust-root mismatch against the current machine
stops the run, and the pin is re-ruled with the fact displayed. The v014
substitution is expressly NOT authorized.

**3. BUILDER CUSTODY.**
```text
Builder A (producer + parent)  = Codex Lane 2   (GPT family)
Builder B (verifier)           = Dario          (Claude family; may consume ONLY
                                 the sealed spec, schemas, immutable inputs, and
                                 output contracts — never A's code, expected-
                                 verdict generator, comparison function, or
                                 mutable receipts)
Custodian C (invokes; authored neither implementation) = the registrar
Terminal assurance record      = the public git deploy (the program's standing
                                 integrity mechanism), with this authorization
                                 artifact as the content-addressed RD-22 input
Obligation carried (Q-583)     = BRANCH_OUTCOME per-ID values displayed in the
                                 implementation manifest
```

**Custody.** Ruled by the principal on the converged record (Q-584); registered
and sealed by the reviewer.
