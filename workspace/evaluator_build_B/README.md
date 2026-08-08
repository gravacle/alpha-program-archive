# A35 evaluator — Builder B: the independent verifier

Governed by sealed specification **V005**
(`STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V009.md`,
`900a240df2bfdee5867eb589ae88c7f282810a8c7718999ad5cdf2bfb3f80698`),
state **R9**, under RD-22
(`DECISION_RD22_BUILD_AUTHORIZED_2026-08-07.md`,
`ff84c4a8ba5c7f8eabfbcc587475d3a5050c21d758a2788c5b9e28b7ee022340`).

## Independence

This package consumes **only** the sealed spec, sealed contracts, immutable
inputs, and the authorized runtime pin. It imports no producer code, no
expected-verdict generator, no comparison function, and no mutable receipt.
Every expectation — the 63+3 check-ID universe, the 56/10 class partition, the
35/13/8/10 binding board, and each descriptor's digest — is parsed out of the
sealed specification bytes at run time by `verifier/spec_census.py`. If the
producer and the spec disagree, the spec wins and the run fails closed.

## Invocation contract (Custodian C invokes; Builder B never does)

```
python3 -m verifier.verify \
  --spec              <path to STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V009.md> \
  --ledger            <path to the producer's canonical verdict ledger JSON> \
  --ledger-sha256     <expected sha256 of that ledger> \
  --evidence-dir      <directory of content-addressed evidence, named <sha256>.json> \
  --runtime-snapshot  <path to provenance/primitive_step6_runtime_snapshot_v012.json> \
  --runtime-gate      <path to primitive_step6_content_addressed_runtime_gate_v010.md>
```

Run from this directory (`evaluator_build_B/`) so that `verifier` is importable.

**Exit codes.** `0` = VERIFIED; `1` = verifier ran and found faults (verdict
`FAIL`, findings enumerated); `2` = fail-closed fault before a verdict could be
formed. Any non-zero exit is a terminal FAIL for the chain.

**Output.** Canonical UTF-8 JSON on stdout, one line, conforming to
`contracts/verifier_verdict.schema.json`.

## Launch manifest — `rd22.verifier-manifest.v001`

`verifier/child_manifest.py` emits the R9 isolated-child launch manifest
(integration addendum §3.2). `optimize` is **declared, not inferred**, so the
normal and `-O` runs can be placed at the same `common_member_key`. `stdout`
carries the verdict and nothing else; diagnostics go to `stderr`. Exit `1`
(ran, found faults) and exit `2` (fail-closed before a verdict) are different
facts and are never conflated — both are terminal FAIL for the chain.

## Self-check (syntax and schema only)

```
python3 selfcheck/selfcheck.py
```

This compiles the package, validates the contract inventories, exercises the
canonical-JSON rejections, and derives the census from the sealed spec. **It does
not invoke the evaluator chain.** Builder B does not run what Builder B wrote.

## Discipline

- **No load-bearing `assert`** anywhere (B-V011-SP2-07): behaviour under
  `python -O` is identical. The self-check scans for and reports zero hits.
- **Content addressing throughout, no path trust**: `hashing.load_addressed` is
  the only admitted way to bring an external file in, and it admits bytes only
  when they hash to an independently supplied digest.
- **Fail-closed branches**: every unknown, missing, malformed, or duplicate
  field raises `VerifierFault`. No exception path yields PASS.
- **Gate discipline**: the 10 GATED-EXECUTION checks return `NOT_RUN_GATE` by
  construction; a gated row reporting PASS or FAIL, or reporting
  `procedure_started`, is unauthorized gated execution and fails the run.
- **Receipts are never authoritative**: `receipt_authoritative` must be `false`.
- **Comparison is `COMMON_MEMBER_ONLY`** (spec §12.5): normal and optimized
  results are compared only at the same `common_member_key`, and unmatched
  members are reported rather than silently intersected.
- **Authority firewall**: `alpha_computed`, `proof_authorized`,
  `kappa_record_computed`, `SPEC_SEAL`, `CORE_RESULT_SEAL` and
  `FINAL_CLAIM_SEAL` may never be true under RD-22. A runner PASS confers no
  seal and no physics authority.
