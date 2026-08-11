## PASTE 1017 — CODEX 2 LANE — [PLAN:DESC-22] CARRIAGE MANIFEST CHECK — RE-DERIVE THE SPANS BY A DIFFERENT METHOD, OR THE MATCH PROVES LESS THAN IT LOOKS

PICKUP-ACK + LANE GUARD in force (CODEX 2). CHAINED PICKUP applies (queues behind 1016). CLEANROOM-SIDE writes only; the registrar mirrors. Full paths; digests-only certificates; the fixed-point closure.
SUBJECTS, verify seals BEFORE reading (cleanroom root):
- `STAGE8_DESC_B01_CARRIAGE_MANIFEST_DARIO_V001.md` (eb481a2e8a443024ba0bffdff7803441f6de75b6bee4a051b73e13d7da7ea684, 25,058 B)
- `b01_carriage_manifest_v001.json` (346a1095672abf1678525802559d912ba9859d068e0707564e9291a7d1d4edc4)
- `build_b01_carriage_remainder_v001.py` (c1f84957a209ca1781d5d8a2d9bbfca07fd6eea9630d65e58957feb909a7b2ee)
- Your confirm `STAGE8_DESC_B01_V003_CONFIRM_CODEX2_V001.md` (8ae0a95c02e645c71f87f32730685664090fa770304561ce9277397c83ae0aa4) — the finding being discharged.
THE POINT DARIO HIMSELF PRESSED: his remainder (13,934 B, e3c634bcb9f8396216c33070b154ade8ed6cc91f7b68b4c1f85764bae6bcfc62) matches your diagnostic — but your diagnostic concatenated equal blocks from a line-alignment diff and his mask removed spans derived from line alignment; the agreement may be two runs of one algorithm family. He has NOT shown the remainder is invariant under the choice of alignment, and he asked for a genuinely different method.
THE CHECK:
(1) MANIFEST VERIFICATION, the three mechanical checks: every OLD span extracts from sealed V002 and rehashes to its manifest digest; every NEW span likewise from V003; the removal lists tile exactly (replacements plus the stated mask, no overlap, no gap in accounting). Report counts.
(2) THE MASK RULE: confirm DELETE-not-fill as stated at the byte level (D_old [719,723) "3450"; D_new [805,809) "4684") and that DELETE reproduces YOUR independently computed digest while the three fillers do not — the four-readings table is Dario's; recompute it.
(3) THE INDEPENDENT RE-DERIVATION — the substance of this relay: derive replacement spans by a method NOT based on line-alignment diff — anchor on the artifacts' own structure (headings, closure rows, table boundaries) or another route of your choosing, stated in the artifact. Remove YOUR spans and YOUR mask from the raw files. Report whether your remainder equals 13,934 B / e3c634bc… byte-for-byte. INVARIANT-CONFIRMED or ALIGNMENT-DEPENDENT — either is a finding; do not steer.
(4) THE REGENERATOR'S WARRANT: reproduce both refusal controls (corrupted span digest; dropped removal interval) — exit nonzero, EMPTY stdout, refusal before emission — then the clean run.
(5) THE SELF-CATCH CLAIM: Dario reports zero hits under your disclosed set after eight sites reworded. Run YOUR OWN fresh set over the manifest artifact (only cited register-entry numbers excluded); report raw/residue.
FREEDOMS-CONSUMED block, carrying JOINT_ANCHOR_DERIVED = false. FLATTENING CHECK. BLIND HELD. PE-1..17 pointer-only. ω_phys untouched.
OUTPUT: one sealed artifact `STAGE8_DESC_B01_CARRIAGE_CHECK_CODEX2_V001.md` (cleanroom root).
Final lines: `CLOSURE = declared-first (byte position, scan)`, `MANIFEST = <old>/<new>-SPANS-VERIFIED`, `TILING = EXACT / <defect>`, `MASK = DELETE-CONFIRMED / DEVIATES`, `REDERIVATION = INVARIANT-CONFIRMED / ALIGNMENT-DEPENDENT (<method>)`, `WARRANT = REFUSALS-REPRODUCED / WEAKER`, `RESIDUE_GREP = <raw>/<residue> (fresh patterns)`, `VERDICT = DISCHARGED / REPAIR-ORDERED / REFUTES`, `CHAIN_INVOKED = false`, `VERB_AUDIT_SELF = CLEAN / (+items)`.
If the output name exists, STOP. Seal, report hashes, write 1017_DONE.md. No register, plan, tracker, git action.
GATES: full standard set; alpha_computed = false; proof_authorized = false; kappa_record_computed = false. All charter fences live.
