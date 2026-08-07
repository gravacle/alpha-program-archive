## PASTE 643 — DARIO LANE (OPUS 5 ULTRA, HIGH EFFORT) — [TASK 6 / SUBGATE] ASSEMBLY V005: THE LINE-LEVEL DECOMPOSITION (BOUNDED)

(Same Dario session rules. ARCHIVE-SIDE ONLY; the registrar mirrors. C-V5a is now law: shared hunks require line-level disjoint span decomposition.)

PREFLIGHT (verify before starting; report any failure and STOP; live-append tolerance applies):
- Register head: Q-580 (live appends recording 644's outputs are verify-and-proceed).
- Base: archive `STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V004.md` = `5e46e8f437ee34d8493dee02195df464e31a20829181542264bc01b23e1f0066`. Verify before reading.
- The conviction (Q-577): `STAGE8_TASK6_ASSEMBLY_V004_CHECK_LANE2_V001.md` = `f37e04fd400739d4118432d898a00b503ec8f42fd3e4d1d0a679c831685a3e8c` — Z2/Z5 under the C-V5a amendment; implement, do not relitigate.

TASK — bounded, certificate prose only:
W1. For each of the seven shared hunks (H05, H10, H11, H13, H19, H20, H25): decompose its changed lines into DISJOINT SPANS, each span assigned to exactly one delta row, displayed as a table (hunk, span, row, line counts summing exactly to the hunk's total).
W2. Correct the two line counts (760/978 -> 759/977) and any dependent arithmetic; state the counting method (robust to blank lines) and display the total-line reconciliation.
W3. Update the audit lines to match W1/W2. Nothing else changes: the operative assembly has been byte-identical since V003 and must remain so — verified by diff scope in your certificate.
W4. Certificate per current law: delta from the diff, conventions declared, paired blocks diffed, PIN CHECK displayed, VERDICT-LINE SCOPE RULE.

OUTPUT: one artifact, lane-tagged filename, written and sealed IN THE ARCHIVE WORKSPACE
`STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V005.md`
with final lines: `DECOMPOSITION = 7/7 (line-level, sums exact)`, `COUNTS = corrected (+method)`, `OPERATIVE_CONTENT = byte-identical to V004 (by diff scope)`, `CARRIAGE = complete_finite_delta (+hunks)`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the output filename already exists, STOP and report — do not overwrite. Seal in the archive workspace, report both hashes, STOP (the registrar mirrors). No register, plan, tracker, git, commit, or push action.

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false. No member binding; no fixed-point execution; no end test; no numeric evaluation of any physical quantity; no comparison to measured constants. If a fence blocks a structural result, flag MACHINERY-APPEAL and continue.
