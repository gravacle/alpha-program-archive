# Alpha Derivation Program — Sealed Archive

Snapshot archive of the Gravacle alpha derivation program (record-theoretic
framework; target-value-free sealed derivation discipline).

- `workspace/`  — the canonical build tree (specs, results, seals, scripts,
  execution state). Source: gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003 (Codex construction lane).
- `cleanroom_output/` — the original sealed cleanroom corpus (OUTPUT 00–45,
  hash-chained manifest; 12-cycle derivation program).
- `supervision/` — the Fable supervision lane: reviews, adjudication
  returns, battery spec + evaluator, continuation state.

Status at first commit: Stage 8 in progress (T7 scope extension on the
critical path); alpha_computed = false everywhere; no value ever compared
to a measured constant. Every seal is a SHA-256 over the file it names;
verify with `shasum -a 256 -c <seal file>` from the containing directory.

This archive is a read-only snapshot series. The live trees remain the
authorities; commits here record their evolution.
