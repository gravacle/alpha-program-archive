## PASTE 654 — DARIO LANE = BUILDER B (OPUS 5 ULTRA, HIGH EFFORT) — [TASK 6 / BUILD] THE VERIFIER-MANIFEST INSTANCE

(Same Dario session rules. ARCHIVE-SIDE ONLY; the registrar mirrors. Builder A's code remains OFF LIMITS.)

CONTEXT (Q-593): first contact reached the verifier gate and found that `evaluator_build_B/contracts/rd22.verifier-manifest.v001.json` is the CONTRACT SCHEMA (draft-07), not the INSTANCE. The parent demands B's actual filled-in launch manifest — the 11 fields of the sealed addendum (`d17c5e79…`), canonical JSON (sorted keys, no insignificant whitespace), sidecar-pinned.

PREFLIGHT: register head Q-593 (live-append tolerance; the archive supervision register carries it — your sandbox reads MB Work).

TASK:
K1. **Write the INSTANCE**: `evaluator_build_B/rd22.verifier-manifest.v001.json` — the 11 fields filled with YOUR verifier's actual launch facts (entry point, argv, the five input roots, output/receipt paths under the run root, optimize declaration, `receipt_authoritative=false`), canonical JSON, plus its `.seal.sha256` protocol sidecar. Keep the schema where it is as the contract file (rename-free); state the two files' distinct roles in the artifact.
K2. **Self-validate** the instance against the schema and against your verifier's real entry point (the launch must be executable as declared by a parent that knows nothing of your internals).
K3. **The artifact** (sealed): the instance displayed in full, the validation transcript, PIN CHECK, VERDICT-LINE SCOPE.

OUTPUT: the instance + sidecar under archive `evaluator_build_B/` + one sealed artifact
`STAGE8_TASK6_VERIFIER_MANIFEST_INSTANCE_DARIO_V001.md`
with final lines: `INSTANCE = 11/11 fields, canonical, sidecar-pinned`, `SCHEMA_VALIDATION = passed`, `ENTRY_POINT = executable as declared`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the artifact name exists, STOP. Seal, report hashes, STOP (the registrar mirrors and re-invokes). No register, plan, tracker, git action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation; no comparison to measured constants.
