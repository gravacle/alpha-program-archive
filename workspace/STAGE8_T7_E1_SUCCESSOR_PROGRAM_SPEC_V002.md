# Stage-8 T7 E1 Successor Program Spec V002 — Cancellation-First Replacement Architecture, Arm-2 Cross-Term Target, and Three-Route IR Attack

Date: 2026-07-26
Root: `/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/`
Author: E1 successor spec v002 drafting lane (Claude). **Draft for construction-lane seal.**

## Status

```text
SPEC_DRAFT_V002 — APPEND_ONLY SUCCESSOR TO 9cfafde1 (which is PRESERVED,
UNEDITED, AND NOT EXECUTABLE). NOT EXECUTABLE UNTIL A FRESH-CONTEXT
HOSTILE LANE CLEARS IT (repair binding R9 step 2). Named blocks are
victories. Failures preserved, never repaired.
```

This v002 discharges the append-only repair mandate of
`STAGE8_T7_E1_SPEC_REPAIR_BINDING_V001.md` (`53717fca…`, R1-R9), its supplement
`STAGE8_T7_E1_REPAIR_BINDING_SUPPLEMENT_CODEX_RECONCILIATION_V001.md`
(`fc4368c7…`, S1-S4), and the typing freeze
`STAGE8_T7_D3_QUANTIFIER_READING_FREEZE_AND_LEMMA_CONSUMPTION_V001.md`
(`9a0c2045…`), under the principal's pre-registered
`STAGE8_T7_Q2_TRIGGER_AND_CLASSIFICATION_STANDARD_V001.md` (`38e15177…`).
It closes every BLOCKING and CONDITION finding of
`E1_SPEC_HOSTILE_REVIEW_SEALED_TRANSCRIPT_V001.md` (`d95c7a16…`, verdict
NOT_READY); the transcript governs over every paraphrase in this text.

**Named blockers this spec owns:**

```text
E1_SEA_KERNEL_ACTION_DENSITY_UNCERTIFIED
    live blocker of O4-M2 in the parent majorant spec; per C2 the Phase-1
    functional that carried it is DIVERGENT and is REPLACED here (§R), not
    certified.
E1_ONE_LINE_CONNECTED_CROSS_TERM_UNCERTIFIED
    named blocker of equal standing to Q6 (supplement S2). Discharge site:
    A-L0 arm 2 (§O.A0). OPEN.
E1_ANCHORED_SUM_NOT_D3_UNIFORM
    NEW, created by this spec (§O.A0.4): under the compelled reading A the
    anchored-sum bound must be supplied DIRECTLY and D3-uniformly by M2, and
    the Chebyshev shell counts do not supply it. OPEN.
```

**Named blocker this spec does NOT own and does not absorb:**

```text
Q6 — RE-CAST FORM ONLY (weighted, subdivision-insensitive polymer counting,
     PROVED, raw degree may not appear). Live only if reading B is ever
     pursued. Its RAW-DEGREE form is CLOSED FALSE on full D3 (§Q6').
     Owner: the parent majorant spec's Route-Q line.
```

---

## §A0 — Pinned authorities

All hashes recomputed by this drafting lane with `shasum -a 256` on 2026-07-26.
The executor re-verifies every row before any computation; **drift blocks**.
`SEAL_MATCH` = checked against the adjacent `.seal.sha256` and matched this
session. `NO_SEAL_FILE` = no adjacent seal exists in the cleanroom; see the
seal-time carve-out in §H.

| Role | Path (cleanroom root unless absolute) | SHA-256 | Seal |
|---|---|---|---|
| **Repair binding (R1-R9); governs this spec** | `STAGE8_T7_E1_SPEC_REPAIR_BINDING_V001.md` | `53717fca7d011eff70bb2fb2b6e598c59e21d8da04b0a20ef024ca98d59d7e9b` | SEAL_MATCH |
| **Repair binding supplement (S1-S4; A-L0 arm 1 CLOSED DEAD)** | `STAGE8_T7_E1_REPAIR_BINDING_SUPPLEMENT_CODEX_RECONCILIATION_V001.md` | `fc4368c70140f477ecba6865e9db20b25d60ef5b095dd5f90148e7aa04fc6afa` | SEAL_MATCH |
| **D3 reading freeze; Q6 raw-degree CLOSED FALSE; reading A COMPELLED; arm-2 target** | `STAGE8_T7_D3_QUANTIFIER_READING_FREEZE_AND_LEMMA_CONSUMPTION_V001.md` | `9a0c20458c98b27aadeef0b2daee6329a0a6eef93ea78569c0a1e74a5fe20bb9` | SEAL_MATCH |
| **Q2 trigger + pre-registered classification standard (GOVERNS §Z; binding verbatim)** | `STAGE8_T7_Q2_TRIGGER_AND_CLASSIFICATION_STANDARD_V001.md` | `38e1517702f6ecb3792da9bb08334b4e344fb3d5bd4c2e1fac5bdc6ef08376a4` | SEAL_MATCH |
| **Hostile review of v001 (verdict NOT_READY); every finding closed in §CR** | `/Users/bgm/MB Work/alpha_supervision/E1_SPEC_HOSTILE_REVIEW_SEALED_TRANSCRIPT_V001.md` | `d95c7a1657a2e6aedbf0f274a350c81da7bbd2b4b6975e6675b6b6cf1b6a86ab` | SEAL_MATCH |
| **C3/C5 erratum — the arm-1 refuting witness; F-8 flag correction** | `STAGE8_T7_C3_C5_REFUTATION_AND_F8_FLAG_ERRATUM_V001.md` | `65a7b799f904a9d0fdaaafd7a462ff4258c3c3b4d1e7bf11ea46fe12881fd426` | SEAL_MATCH |
| **Predecessor spec, PRESERVED UNEXECUTED** | `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V001.md` | `9cfafde1774e78b61b65d44858faf73f177c2ec75f323911473bae06a805ce7b` | SEAL_MATCH |
| **F-8 findings: O1 CTP-NESTED reading FORCED; Q6 first named** (C-8 row 2) | `STAGE8_T7_F8_FIRST_HALF_RESULT_AND_TWO_NEW_FINDINGS_V001.md` | `f84c30367e077ea722e2647696cb7e37374aa388056b444a3c236cd6dd1c5872` | SEAL_MATCH |
| **F-8 second-half review (F8_GATE_NOT_DISCHARGED)** | `/Users/bgm/MB Work/alpha_supervision/F8_SECOND_HALF_REVIEW_SEALED_TRANSCRIPT_V001.md` | `3cacd4b748bbd1c67a3e49419da9728cda422f527236899fa36c6f293bc51b6d` | SEAL_MATCH |
| **F-8 first-half re-derivation transcript** | `/Users/bgm/MB Work/alpha_supervision/F8_REDERIVATION_RETURN_SEALED_TRANSCRIPT_V001.md` | `11512a7d6eba2ce647bf20310eb83caa4fbebaea7a658879c2be7e0eea685771` | SEAL_MATCH |
| **Independent-system blind E1 return (Codex Assignment A)** | `/Users/bgm/MB Work/alpha_supervision/CODEX_ASSIGNMENT_A_E1_BLIND_RETURN_V001.md` | `20b54b2e94c9213edfdfc4b9ee4820eeb75ad0fa6208b597cf65ae51d6c77e96` | SEAL_MATCH |
| **Pipeline repair binding: D1 reading, D2 contamination fence, D3 diff items (O6, KP line)** | `STAGE8_T7_PRODUCTION_GATE_NOGO_AND_PIPELINE_REPAIR_BINDING_V001.md` | `aa8758a9be4e9fa2171ad3817c069a9b946398137a79679218df8c7ba7bf36c9` | SEAL_MATCH |
| Corrected baseline C1-C6 (**read as corrected of record by `65a7b799…`**) | `STAGE8_T7_E1_RECLASSIFICATION_CORRECTIONS_AND_ESCALATION_V001.md` | `6c3e125ba7a43655b72ec75b218e64d1d5062213d5a10f740e89199cc1033aa1` | SEAL_MATCH |
| Route scoping IR-A/B/C; graceful-block table (**not an authority for its own constants, F'-14**) | `/Users/bgm/MB Work/alpha_supervision/ROUTE_MEMO_2026-07-26_ir_sea_kernel_attack.md` | `51f655a0a1bd3f20d7789f79e3ced16e08e56305521ebcafd4e9a7d4b8a3e528` | SEAL_MATCH |
| Parent spec supplied into (D3-D5, E1 rule, O4 M1-M3, O6, spec-header scoping, F-1..F-8) | `STAGE8_T7_CONNECTED_LINKED_CLUSTER_MAJORANT_DERIVATION_SPEC_V001.md` | `818083a52165bc5c2ee86bd43e3b7e30d87f5c9eb82e54935e7829bb6f1f84e3` | SEAL_MATCH |
| Parent repairs M-1..M-11; I3 tuple V002 | `STAGE8_T7_D6_SPECS_REPAIR_AMENDMENT_V001.md` | `60223e6a175c5fee122f253491fd279daccfa15f8771af12104710f57ce09e5d` | SEAL_MATCH |
| DERIVED arm = Route-Q predicate; F-8 is the gate | `STAGE8_T7_MAJORANT_ARM_RESCOPE_PRINCIPAL_DECISION_V001.md` | `209aa39015c955e46ec84519c05b8de52e65288ba883e01590b245fcbfe0bb53` | SEAL_MATCH |
| Exact sea covariance (C1's SOLE source) | `STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_RESULT_V001.md` | `3a6ff6173573a7d9dd99bdd1a6bb7eaa02c433ab50bc769e144d94c983b4f0ff` | NO_SEAL_FILE — **carve-out A, §H** |
| Phase-A A1-A4 (`h_0`, `M(t)`, `v(t)`, `b_D`, `J`, `S`, `w_lambda`) | `STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md` | `789338adb7d3d36da453113e98f371a4f92543cf2652b047f8481c407bed5bc3` | SEAL_MATCH |
| L2 typing freeze (fences 1-5) | `STAGE8_T7_L2_INTENSIVE_HESSIAN_TYPING_FREEZE_V001.md` | `cdbacdaf5efcd3a70a6ffa456bc790753e0ff36609c40c67b9bb606b79624746` | SEAL_MATCH |
| L1 assessment (Lemma 0 constitutive) | `STAGE8_T7_L1_MULTICELL_LEMMA_ASSESSMENT_V001.md` | `03fadd3634cf8dbc729795c4009012933d3ad836e663c9c509e4e43b7b4883bc` | SEAL_MATCH |
| Determinant fence, gate item 9 (mandatory M1 citation (i)) | `STAGE8_ROUTE2_CAR_STATE_BRIDGE_SCOPE_CORRECTION_V001.md` | `4e1282bc800c47441d255e9d9d576958608d955dce15f02969261cd6e601e268` | SEAL_MATCH |
| A4 relocation (mandatory M1 citation (ii); carries M-11 disclaimer) | `STAGE8_T7_OPERATOR_VALUED_PRIMITIVE_RESPONSE_ARCHITECTURE_AMENDMENT_V001.md` | `8a7f52ffa2500d20ad834b11e3762ed114ee1a201f2fec18bcb119e3c7ead860` | SEAL_MATCH |
| O7 obstruction record (`(3/8)^k`; `e^{+-i pi}`) | `STAGE8_T7_MAJORANT_PHASE2_STATUS_AND_O7_ESCALATION_V001.md` | `3c81647eb55ad01d4d71e23b2b45161427f82390098c95afa5721065206a7df2` | SEAL_MATCH |
| `tau_R = pi/sqrt(2)` derivation | `BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_DERIVATION_V001.md` | `b786db3adec8cc335967d49ec13b59923d67f424644f72c535b27b579dd1489f` | NO_SEAL_FILE — **carve-out B, §H** |
| CTP propagator typing (IR-B) | `BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001.md` | `6f6b822ac8ccf9ea19659f4ccf811268f60a27a361f817ee6513479d63b62546` | NO_SEAL_FILE |
| Envelope-profile class (`v_A`, `v_B`) | `STAGE8_T7_ENVELOPE_REALIZATION_COMPARISON_SPEC_V001.md` | `4059eff522426d06d41d2a0542ddf6be309867bd077491d84c6998b2098ede31` | NO_SEAL_FILE |
| Relay necessity | `STAGE8_T7_OPEN_EXHAUSTION_ATTACHMENT_AND_RELAY_NECESSITY_RESULT_V001.md` | `0df721a170f4f4a1ec630775a3ae47b0d793c82e100b326e681030389eaf0694` | NO_SEAL_FILE |
| Relayed-family resolution (causal order; disjoint-cell commutation) | `STAGE8_T7_RELAYED_FAMILY_RESOLUTION_RESULT_V001.md` | `52401eefc3ff84e22f04bbc329a619b830058661db7f969d2d43d167d97d893d` | NO_SEAL_FILE |
| Monoidality on disjoint cells | `BID_MONOIDAL_EXTENSIVITY_DERIVATION_V001.md` | `451550c3825288d699db35c7289e408e8314ad042450253b58f32722c4ead46b` | NO_SEAL_FILE |
| Closure result (GHZ witness; `t^-3` data = NC3's object) | `STAGE8_T7_CONNECTED_ANALYTIC_CLOSURE_RESULT_V001.md` | `f891d3afc58e695529d8d569b5d2ba4b853e30c9cfa4296817cb17b60f38b054` | NO_SEAL_FILE |
| Phase-1 draft (the REPLACED architecture; O1/O2, R1-R4, `\|\|b_D\|\|=1`) | `stage8_execution/work/MAJORANT_LEMMA0_PROOF_DRAFT_V001.md` | `679ba036b8c6c820a5367ae460f369c8bd6c0e03eb9de395b99e60472e3a7b9c` | SEAL_MATCH |
| Phase-2 draft (NC3 `24 H_K`; exact `e^{+-i pi}` witness) | `stage8_execution/work/MAJORANT_PHASE2_O3_O7_PROOF_DRAFT_V001.md` | `08b91543fdb72f656c756ca5f8df8233b87eb5487284c7fd2170cba67f7e0e3b` | SEAL_MATCH |
| Phase-1 primary record | `stage8_execution/work/T07_majorant_phase1_primary_v001.json` | `e4a725a9168129ffdd8128a153b557a3d4549225375ba1607d88f9428187a0e2` | SEAL_MATCH |
| Phase-2 primary record | `stage8_execution/work/T07_majorant_phase2_primary_v001.json` | `8d986314a93a2e5378a243a55ed919b37e859b1646f34b96fa315b40e1b30339` | SEAL_MATCH |
| Calibration ledger (governs §P) | `/Users/bgm/MB Work/alpha_supervision/CALIBRATION_LEDGER.md` | `d56a8b8111997087df42154ae2c4751cd0a13cf9d852a298b08c8c20327aa67c` | living document, unsealed by design |

```text
LEDGER PIN NOTE (mandatory, and a correction of record against v001): v001
pinned the ledger at fcf35d0d…; the current content hash is d56a8b81…. The
ledger is a LIVING DOCUMENT and its drift is BY DESIGN, so it is EXEMPT from
the drift-blocks rule and is the ONE exempt row. The executor re-reads it and
restates §P's calibration from its then-current content; it may not treat a
ledger hash mismatch as drift. Per review N-19 the ledger's standing header
still reads "MISSED TWICE CONSECUTIVELY" while its own entry table records the
third miss (07-26 Control-4 v3 S3(a)); THIS SPEC STATES THREE (§P), the spec
is correct and the ledger header is stale, and correcting the header is out of
this spec's scope.
```

**Drafting-lane verification evidence** (exact arithmetic; pinned runtime
`/Users/bgm/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`,
no scipy; disposable scratch
`/private/tmp/claude-501/-Users-bgm-MB-Work/578abe61-ea1d-48e6-8fb1-b06509d933a1/scratchpad/e1v2/`;
no canonical directory touched, no production lane invoked):

| script | sha256 | checked exactly this session |
|---|---|---|
| `verify_v002.py` | `47589c719cd43326bebd12c91e4fc00c0a7b1aa085f86c68bce22aac7fe93c24` | Chebyshev shell identities `(2k+1)^3-(2k-1)^3 = 24k^2+2`, `(2k+1)^4-(2k-1)^4 = 64k^3+16k`, `(2k+1)^2-(2k-1)^2 = 8k`, exact, k=1..400; exact-rational partials of the two-line 3-D and 4-D sums (S(3000) = 28.010443732…, 93.522482330…); the one-line 3-D sum minus `24 H_K` converging on `2 zeta(3)`; **the NEW arm-2 collar sum `sum_k (24k^2+2)/k^4` with closed form `24 zeta(2) + 2 zeta(4) = 4 pi^2 + pi^4/45` (partials 41.40426 / 41.61908 / 41.63507 / 41.64186 at K = 100/1e3/3e3/2e4 against 41.6430640717797…), and the exact coefficient checks `24/6 = 4`, `2/90 = 1/45`**; both arm-2 failure modes reproducing logarithmic divergence (`24 H_K + 2 zeta(3)`; `64 H_K + 16 zeta(3)`, residual 19.2329095 against `16 zeta(3) = 19.2329104…`); `Gamma_star^split(1/2,1/2) = 1 = eta/(1-eta)` at `eta = 1/2`; `int_0^1 32 min(t,1-t)^3 dt = 1` exactly |

These are drafting-lane checks. They are **not** certifications; every quantity
below still requires a certified outward enclosure under §N.

---

## §CR — Change report: hostile-review finding → repair (MANDATORY, complete)

Every BLOCKING and CONDITION finding of `d95c7a16…` is enumerated. The
transcript governs; where this table compresses, the transcript's text rules.

```text
--- BLOCKING ---
B-1  C3's no-cross-term clause frozen; two-line R^-6 FALSE by exact witness.
     REPAIR: (a) C3/C5 frozen-input status REVOKED (§B); the clause becomes
     numbered obligation A-L0, authored ARM 2 ONLY per supplement S1 with the
     exact rational witness quoted (§O.A0.1-2); witness
     E1_ONE_LINE_CONNECTED_CROSS_TERM_UNCERTIFIED named as a first-class
     blocker. (b) C5 and A-L3/A-L4 restated as the TWO-LINE SECTOR only, and
     §V forbids any verdict asserting n >= 2 certified until arm 2 closes.
     (c) NC8 recast as a two-SECTOR control (§O.NC). (d) Correction of record
     against 6c3e125b… and 51f655a0… is SEALED at 65a7b799… and pinned here;
     both are read through it. ADDITIONALLY, beyond the review: NC3 is given a
     POSITIVE role as the one-line-sector DETECTOR, PASS = detection (§O.NC).
B-2  S3 / G_bl frozen finite while C6 makes it infinite; baseline normed.
     REPAIR: S3 and G_bl DELETED (§R.1). The baseline is NEVER normed. §R.2
     restructured: same-phase sector `V(0) = I` up to the C-L2 commutator
     error; opposite-phase sector vanishes identically. G_bl replaced in R.3
     by S2b, a certified bound on the C-L2 commutator error, witness
     E1_RECORD_KINK_COMMUTATOR_FORM_UNCERTIFIED. CONSEQUENCE STATED, NOT
     BURIED: §R.6, §V and §P all state that SCAD is NOT an independent route
     — it is IR-C's wall re-expressed.
B-3  Colour sum divides by a baseline the spec predicts is zero; rho_res sup
     starts at a non-trace-class point.
     REPAIR: obligation R-L4b "OPPOSITE-PHASE SECTOR VANISHES IDENTICALLY on
     the closed pair polydisc" with witness
     E1_OPPOSITE_PHASE_SECTOR_VANISHING_UNCERTIFIED; `sum c = 1` and
     `sum |c| = kappa_bal` RE-DERIVED over the surviving sector only; S4's sup
     and the Carleman segment restricted to that sector; `kappa_bal = 1`
     obtained as `(1/2)/(1/2)` from the surviving weights, and the
     `(1+|D|)/|1-D|` display STRICKEN (§R.2-R.3).
B-4  "D = 0 exactly" is an invalid limit of a bound; at the point where the
     hypothesis holds the conclusion's object does not exist.
     REPAIR: the `D^2 <= exp(-2||[C,P]||_2^2)` route is STRICKEN as ground for
     `D = 0` (retained only as R-L4's finite-dimensional identity, reported,
     never used to value D). Replaced by R-L4a: establish
     existence-or-nonexistence of the baseline determinant via the Carleman
     factorization `det = det_2 · e^{tr}` WITH THE REGULARIZATION NAMED. PA-3
     restated as conditional on R-L4a. The `b_0 = 1/2` / `kappa_bal = 1`
     clause is REMOVED from the Q2 option-(i) cost block (with C-11).
B-5  R-L0 unsatisfiable as written because S1-S5 are sup-first.
     REPAIR: (a) S1-S5 re-frozen as PER-CELL functionals `S_i(C, eps)`, sup
     taken ONLY after the scale weight is exhibited, so ground (i) is testable
     (§R.1). (b) new obligation R-L0b: bound `Log(sum c rho)` WITHOUT an
     absolute bound on x, on the surviving sector. (c) mandatory pre-execution
     escalation slot E-Q1 (§H) putting the scoping question to the principal;
     weakening F'-5 is not a lane's to do and this spec may not execute on a
     provably unsatisfiable obligation.
B-6  The zeta constants are CUBIC-cellulation shell counts frozen as if
     D3-uniform; IR-A silently consumed Q6.
     REPAIR: A-L3/A-L4/C5 SCOPED to the cubic skeleton and family A, witness
     E1_SHELL_COUNT_NOT_UNIFORM_OVER_D3. Z.6's disclaimer corrected. AND
     SHARPENED by the D3 freeze (9a0c2045…): a D3-uniform raw-degree closure
     is not merely undeliverable, it is CLOSED FALSE; the only admissible
     D3-uniform route is reading B (weighted, subdivision-insensitive,
     PROVED), which is unavailable absent that proof. §G row 1 narrowed to the
     cubic family. The residue is named as a new blocker,
     E1_ANCHORED_SUM_NOT_D3_UNIFORM (§O.A0.4).
B-7  §E1' step 2 values the undischarged H-R inside a certified inequality.
     REPAIR: step 2's n = 1 leg restated as a CONDITIONAL certification of the
     implication "if rho_res <= rho_bar then eta_1(2^-k) <= 1/2", `rho_bar` an
     explicit disclosed-premise symbol whose admissible range the artifact must
     state; `eps_*^{(1)}` so obtained is premise-conditional and may NOT be
     supplied to I3 as unconditional. F'-3 amended to name this the ONLY
     permitted form of premise-carrying in a threshold comparison.

--- CONDITION ---
C-8  Q2 standard and F-8 findings unpinned; O1 display false as literally read.
     REPAIR: both rows ADDED to §A0 with hashes re-verified this session
     (38e15177…, f84c3036…, both SEAL_MATCH); §D records that the CTP-NESTED
     reading of O1 GOVERNS OF RECORD.
C-9  Z.2's (b) branch can launder a proof-architecture need via D5's own
     "REQUIREMENT" heading.
     REPAIR: Z.2 appended verbatim per the review — D5, Kotecky-Preiss
     convergence, action-density form and every requirement INTERNAL to the
     majorant/activity architecture are CONVENIENCES OF THE PROOF for (b) and
     may not ground a require-grade (b); a require-grade (b) must name a
     principle UPSTREAM of the activity architecture; the invoked principle
     and its grade are classified by fresh-context hostile review.
C-10 Three wiring failures between §Q2-STOP and §Z.
     REPAIR: step 2 explicitly includes the Z.2 (a)/(b)/(c) declaration in the
     sealed finding and step 1's prohibition does not extend to it; step 3
     reads "all three options (i), (ii), (iii)"; an option-(iii) COST BLOCK is
     added, costs only, no argument.
C-11 Evaluative comparatives and a pre-judged Z.2 grade in the cost blocks.
     REPAIR: "strictly more information / strictly better than the status quo"
     and every equivalent comparative STRICKEN from §Q2-STOP and §G; the "what
     is not refuted" clause replaced by the neutral statement the review
     dictates; NO COST BLOCK MAY ASSERT A Z.2 GRADE IN ADVANCE.
C-12 Z.3 dropped Tier 1's uniqueness criterion and Tier 2's T5b citation; §Z
     did not subordinate itself to the sealed text.
     REPAIR: "Where §Z's paraphrase and the sealed standard (38e15177…) differ
     in any respect, THE SEALED TEXT GOVERNS" appended; Tier 1's "uniquely, up
     to sealed conventions, competitors excluded" and Tier 2's T5b bucket rule
     restored (§Z.3).
C-13 The |C|_4^{-1/2} exponent is asserted, and R.3's "answer to C2" is a
     bookkeeping tautology.
     REPAIR: obligation R-L2b DERIVE THE SCALING EXPONENT, witness
     SCAD_HS_SCALING_EXPONENT_UNDERIVED; R.3's claim downgraded to
     "bookkeeping consistent with D5 CONDITIONAL on R-L2b"; "it is the answer
     to C2" DELETED.
C-14 F'-1's rationale pre-scripts the escalation on the strength of C5.
     REPAIR: the "evidence that the reaching obligation has been mis-derived"
     sentence and the instruction that the escalation "must say so" are
     STRICKEN. The fence's operative clauses are unchanged and absolute.
C-15 Parent O5 (differentiated series) not disclaimed.
     REPAIR: §X row added — no bound on the differentiated cluster series is
     supplied and parent O5 may not be inferred from anything here; matching
     fence-register row F'-15.
C-16 NC7 permits the C-L3 coefficient whose predicted window brackets the
     forbidden target.
     REPAIR: NC7 appended — the C-L3 coefficient is reported ONLY in exact
     symbolic form as an explicit rational/algebraic multiple of `2/pi`, never
     as a decimal; transform-grep runs on it with a pre-registered exemption
     keyed to that symbolic form; any numerical proximity to a target-adjacent
     value is recorded as coincidence and may not be commented on, compared,
     or propagated.

--- NOTE ---
N-17 Handoff said ELEVEN "no adjacent seal" rows; there are EIGHT.
     REPAIR: corrected to EIGHT and enumerated by path in §H, with the two
     carve-outs named.
N-18 The F-to-F' mapping claim is inaccurate; the list runs to F'-14.
     REPAIR: explicit F-to-F' mapping table in §F'; parent F-2's fate recorded
     (O7 retired by the re-scope; substance survives in §X); the list now runs
     to F'-16.
N-19 Ledger header stale (TWICE vs THREE).
     REPAIR: recorded in §A0's ledger pin note and §P; correcting the ledger
     is out of scope.
N-20 Prediction hygiene: PA-A5 near-unfalsifiable; PA-C4 gated; PA-B4
     one-directional; PA-3 an invalid-limit prediction.
     REPAIR: PA-A5 restated as a FUNCTIONAL-FORM prediction; PA-C4 marked
     conditional-and-probably-untested; PA-3 restated conditional on R-L4a;
     PA-B4 retained with its explicit no-permission clause (§P).
N-21 Items that check out: D5' split, W1/M-1/M-9, NC4-as-fence, F'-6, F'-10,
     F'-12, §G's memo rows.
     ACTION: carried unchanged, and the review's confirmation is recorded so a
     later lane does not re-open them without cause.
```

**Binding coverage.** R1 → §B, §O.A0, §O.NC (NC8), §V. R2 → §R.1-R.3, §R.6.
R3 → §R.2-R.3, R-L4b. R4 → this §CR. R5 → §CR.R5 below and §O.X. R6 → §O.X
(B-L2\*). R7 → filled by `fc4368c7…`; slot closed. R8 → §Z, §Q2-STOP. R9 →
§H ordering. Supplement S1-S4 → §O.A0, §O.NC (NC3), §P. Freeze parts 1-2 →
§D (D3), §Q6', §O.A0.3.

```text
CR.R5 — CODEX ROUTE MAPPING OF RECORD (binding R5, carried verbatim in
substance). Route 1 (cancellation-first CTP determinant) ~ IR-B, broader and
better-founded. Route 2 (renormalized single-cell anchor) ~ IR-A's spirit, but
treating the n >= 2 bound as an OBLIGATION TO PROVE — which, given the C3/C5
refutation, is exactly right, and IR-A's framing was wrong; it also requires an
EXACT completed-normalization identity, not a subtraction by convention.
Route 3 (smooth-localizer sharp-limit classifier) ~ IR-C's classifier role;
this is the Q2-trigger route.
ORGANIZING PRINCIPLE ADOPTED FROM THE INDEPENDENT SYSTEM: CANCELLATION-FIRST.
The root cause is that absolute trace-norm majorization was taken BEFORE the
CTP, determinant-ratio, oscillatory/PV and completed-normalization
cancellations were used. This is a cleaner statement of the root than this
lane's and governs §R.
CONVERGENCES RECORDED (Codex was blind to this lane's work): bound-class
failure rather than a proven divergence of the completed theory; the n = 1
coincidence limit as the locus; the missing unitality anchor, with
Z_comp(0) != 0 a NAMED HYPOTHESIS and not a structural identity.
WHERE CODEX DID NOT FOLLOW THIS LANE AND WAS RIGHT: it never leaned on the
two-line decomposition, so its routes do not inherit that error; and the C6
LOCUS REFINEMENT below.
THE SUPREMUM OVER ADMITTED CELLS is not the root but the ENFORCEMENT MECHANISM
preventing concealment in a chosen carrier/truncation/cell size — adopted as
this spec's reading of the spec-header scoping.
D2 CONTAMINATION FENCE (aa8758a9…) HONOURED: the addendum's withdrawn
two-line/R^-6/NC3 sentences remain NON-CITABLE. Only the corrected
restatement consumed in fc4368c7… may be cited, and it is cited nowhere as
independent confirmation of a two-line reading.
```

---

## §B — Derived starting point (FROZEN INPUTS: C1, C2, C4, C6 only)

C1, C2, C4 and C6 are **inputs**, not obligations, re-verified independently by
the reviewer (`d95c7a16…` BASELINE_CHECK) where checkable. An obligation
contradicting one of them without a new exact witness BLOCKS. **C3 and C5 are
NOT frozen inputs; their frozen status is REVOKED (R1). No fence bars an
executor from the correct algebra.**

```text
C1  SEA COVARIANCE PINNED EXACTLY, NOT BY CLASS. C = 1_(-inf,0)(h_0),
    C(p) = (I - alpha·p-hat)/2,
    C(r) = (1/2) delta^3(r) I - i alpha·r/(2 pi^2 |r|^4);
    off-diagonal operator modulus EXACTLY 1/(2 pi^2 |r|^3); homogeneous
    degree -3; odd (zero spherical mean; Calderon-Zygmund). Marginality
    quantified: int_{a<|r|<R} |C_off| d^3 r = (2/pi) log(R/a) EXACTLY —
    logarithmic at BOTH ends, with the divergence at the UV/coincidence end.
    E1 is a LEMMA UNPROVEN ABOUT A FULLY KNOWN OBJECT. Independently
    re-derived by the reviewer, including ||C_off||_F^2 = 1/(pi^4 |r|^6),
    which confirms the conservative A-L1 constant.
C2  PHASE-1 K_sea IS DIVERGENT, NOT UNCERTIFIED. The trace norm of
    (sea) x (sharp diamond-slice localizer) diverges as a power (~|D_t|
    Lambda^3) under carrier-blindness; finite only on a fixed carrier, which
    spec-header scoping clause 1 forbids. THE PHASE-1 eta(eps) ARCHITECTURE IS
    REPLACED BY §R, NOT CERTIFIED. Nothing here may cite (K_sea, T_R, b_0) as
    a target of certification. RECORDED, per the reviewer: the same divergence
    is what killed S3/G_bl (B-2) and what makes the baseline determinant a
    NON-EXISTENT rather than a zero object (B-4). This spec follows C2 all the
    way into its own replacement — that is what §R.1-R.3 now do.
C4  TWO MOMENTS VANISH; THE CANCELLATION IS EXACTLY SATURATED AT FULL tau_R.
    m_0 = m_1 = 0 exactly; m_{2j} = -2^{j-1} (j >= 1); all odd moments zero;
    sum_lambda w_lambda f(lambda) = -(1/4)[f(+sqrt2) - 2f(0) + f(-sqrt2)] —
    the completed per-cell Kraus operator IS a symmetric second difference.
    Every Dyson term with fewer than two record insertions PER CTP BRANCH is
    annihilated; the bare a-linear tadpole vanishes identically (also killed
    by the odd spinor trace tr_spinor[C(p) alpha_x] = -2 p-hat_x).
    BUT at full tau_R, lambda tau_R in {0, +pi, -pi} and on the ball where
    M(t) = 1, exp(-i lambda tau_R S) = (+1,-1,-1)·I EXACTLY (S^2 = I), so
    sum_lambda w_lambda phase_lambda = 1 = sum_lambda |w_lambda|: the l1-mass
    step is TIGHT, the zero-sum weights buy NO decay, and at the operator
    level sum_lambda w_lambda u_lambda = m_0(I-P) + 1·P = P — the weights
    PROMOTE the sharp causal-ball projector to the leading in-cell object.
    Fully confirmed by the reviewer in exact Q(sqrt2).
C6  THE BLOCK IS CONFINED TO n = 1 — AND ITS LOCUS IS THE VOLUME DIAGONAL.
    Equal-time localization of the 3-D massless Dirac sea fails
    Shale-Stinespring: ||[C, 1_B]||_2 = +infinity; a Lipschitz cutoff still
    gives int d^3 r · r^2/r^6 = int dr/r^2, divergent. Only TWO-TIME /
    scattering-type objects, where the cell time integration supplies the
    missing decay, can work.
    *** LOCUS REFINEMENT, ADOPTED OF RECORD (binding R5, from the independent
    system): THE FATAL LOCAL INTEGRAL IS THE VOLUME DIAGONAL x = y, NOT THE
    SHARP BOUNDARY. SMOOTHING ONLY THE BOUNDARY WILL NOT REMOVE A |x-y|^-3
    POSITIVE MAJORANT. *** C6 named the sharp localizer as the locus; the
    locus is refined to the diagonal and boundary smoothness is demoted to a
    secondary, testable factor. THIS BEARS DIRECTLY ON Q2: a
    smoothed-localizer successor MAY NOT FIX THE OBSTRUCTION AT ALL, and NC9
    and the §Q2-STOP option-(ii) cost block must both say so.
    Also binding on this spec's own constants (reviewer): dilation covariance
    makes ||CPC||_2 radius-independent, hence scale-free and infinite — which
    is why S3 is deleted (B-2) and why the baseline determinant does not exist
    as a Fredholm determinant (B-4).
```

**C3 and C5, restated as scoped statements of record (NOT inputs):**

```text
C3'  REFUTED AS STATED. The lowest connected two-cell cumulant is NOT a
     two-line object. For relay-ordered cell evolutions V^{(12)} = V_2 V_1,
     so V^{(12)} - 1 = Y_1 + Y_2 + Y_2 Y_1 with Y_i = V_i - 1, and
        Phi_12 = -tr[C Y_2 Y_1] + tr[C Y_1 C Y_2] + O(Y^3)
     — TWO terms at the SAME order, only the second two-line. The one-line
     term carries a SINGLE sea-kernel factor (R^-3) plus free propagation
     between the cells. The dismissal of NC3 is VOID; NC3 is REHABILITATED
     WITH A POSITIVE ROLE (§O.NC).
C5'  ARITHMETIC CONFIRMED; SCOPE AND STANDING NOT. The exact constants
     24 zeta(4) + 2 zeta(6) = 4 pi^4/15 + 2 pi^6/945 and 64 zeta(3) +
     16 zeta(5) are correct AS CHEBYSHEV SHELL COUNTS ON A CUBIC CELLULATION
     (family A), and only there. "The long-distance direction has margin" and
     "clustering was never the missing ingredient" are UNPROVEN and may not be
     asserted by any artifact of this program.
```

---

## §D — Frozen definitions

Inherited from the parent as repaired: **D1** (completed chain, `m_0 = 0`,
T7(i) anchor `Z_hat_comp = Z_comp(a)/Z_comp(0)`, named hypothesis H-B, no
unitality anchor — and, per CR.R5, `Z_comp(0) != 0` is a NAMED HYPOTHESIS, not
a structural identity), **D2** (relayed causal exhaustion, every cell at full
`tau_R`), **D3** (below), **D4 as repaired by M-2** (CTP pairs, polydisc
`max(|a_{c,+}|,|a_{c,-}|) <= eps_*`, adjoint-continued bra branch, joint
holomorphy), **M-3** (the two pinned finite schemes `C_mix`, `C_pure`;
per-state, reported separately, never promoted), **M-7** (tuples read
`|w_lambda|`).

```text
D-O1  CORRECTION OF RECORD, PINNED (C-8; from f84c3036…). The sealed O1
      display is FALSE as literally read: with prod_c scoping the whole term
      it is the INTERLEAVED reading (a per-cell product of Gammas), which is
      false in general; with prod_c scoping only the weights the display is
      ILL-FORMED. THE CTP-NESTED READING IS FORCED AND GOVERNS OF RECORD.
      The readings coincide on DISJOINT cells and diverge on
      overlapping/adjacent ones — exactly where the linked-cluster activities
      live. Every artifact of this program reads O1 nested. §R.0 and C-L5 are
      already consistent with the nested reading.

D3    FROZEN QUANTIFIER READING (9a0c2045… Part 1, verbatim in substance).
      "All common refinements of members of A and B" means ANY cellulation
      refining BOTH parents — UNRESTRICTED, UNIVERSALLY QUANTIFIED. It is NOT
      the minimal overlay. Grounds G1-G4 all antedate the lemmas that consume
      the freeze (sealed text; no narrowing definition exists in the corpus;
      F-2 forbids the narrow reading's finite-list effect; T13 locates one
      check, not the theorem's scope). Pinning the quantifier is unavailable
      to any lane under any outcome. If the principal holds that the sealed
      INTENT differed from the sealed TEXT, the freeze is superseded on his
      word; no lane may make that call.
```

### D5' — Action-density activity form, SPLIT (scoped supersession of D5)

```text
  sum_{gamma ni C, |gamma| = 1} |Phi_gamma(a)|  <=  |C|_4 · eta_1
  sum_{gamma ni C, |gamma| = n} |Phi_gamma(a)|  <=  |C|_4 · eta_{>=2}^n  (n>=2)
```

with `|C|_4` the cell 4-volume and both `eta_1`, `eta_{>=2}` functionals of
`(||b_D||, tau_R, sea-kernel decay data, |w_lambda|)` only, carrier-index-blind,
stated over the envelope-profile class.

```text
KOTECKY-PREISS DOES NOT RELEASE n = 1. Under the split the SAME aggregate must
be delivered:
   Gamma_star^split := eta_1 + eta_{>=2}^2/(1 - eta_{>=2})  <=  1  certified,
   with eta_{>=2} < 1 certified.
At eta_{>=2} <= 1/2 the tail term is <= 1/2, so the criterion reduces to
eta_1 <= 1/2 AND eta_{>=2} <= 1/2 — EXACTLY the parent's single threshold on
BOTH legs; the split reproduces the parent's Gamma_star = eta/(1-eta) term by
term and equals 1 at eta_1 = eta_{>=2} = 1/2 (re-verified exactly this
session). NO NUMBER IS LOOSENED. Its value is diagnostic and graceful-block
only. Any artifact reading the split as weakening n = 1, or reporting a verdict
with eta_1 uncertified, BLOCKS with witness D5_SPLIT_MISREAD_AS_RELEASE.
FURTHER, PER B-1: the n >= 2 leg is a statement about the TWO-LINE SECTOR ONLY
until A-L0 closes. `eta_{>=2}` certified does NOT mean "the n >= 2 sums are
certified", and §V forbids that wording.
```

The consumer interface is preserved: I3 tuple V002 receives
`Gamma_star := Gamma_star^split` and `eps_* := min(eps_*^{(1)}, eps_*^{(>=2)})`
per §E1' — subject to §E1' step 2's premise-conditional marking of
`eps_*^{(1)}` (B-7).

### D6' — Sharp localizers (frozen; not softenable by any lane)

```text
M(t) = Q 1_{|x| <= r(t)} Q,  r(t) = min(t, 1-t),  v(t) = tau_R · 32 r(t)^3,
int_0^1 v(t) dt = tau_R = pi/sqrt(2) EXACTLY (int_0^1 32 min(t,1-t)^3 dt = 1,
exact rational, re-verified), 1_{D_t} the sharp diamond slice, all per sealed
Phase-A A1/A2 (789338ad…). THESE ARE SEALED DEFINITIONS. No obligation, lemma,
control, repair, or enclosure may replace, mollify, smooth, or regularize M(t)
or 1_{D_t}. See §Q2-STOP and NC9.
```

### D7' — The three-line reading of E1 (a)/(b)/(c)

```text
(a) REMOVABLE: the a-independent, cell-local, carrier-blind-divergent part.
    Cancels in the T7(i) ratio and again in the Moebius truncation for
    |gamma| >= 2. Removed BY ARCHITECTURE (§R), never by enclosure.
(b) MARGINAL: the logarithmic residue of the degree-(-3) kernel against the
    in-cell SHARP localizers, AT THE VOLUME DIAGONAL (C6 refinement).
    Undecided by any sealed authority. The substantive n = 1 target.
(c) LONG-DISTANCE n >= 2: now split into TWO SECTORS by C3' —
    (c1) the TWO-LINE sector (spare powers; family-A constants of A-L3), and
    (c2) the ONE-LINE CONNECTED CROSS-TERM sector (R^-3 plus free
         propagation), which is A-L0's target and is UNCERTIFIED.
    NO ARTIFACT MAY TREAT (c) AS (c1).
```

---

## §O.A0 — A-L0: THE ONE-LINE CONNECTED CROSS TERM (arm 2 only)

### O.A0.1 — Arm 1 is CLOSED DEAD, with the exact rational witness

```text
A-L0 as originally sealed offered two arms. ARM 1 (prove Y_2 Y_1 = 0 as an
EXACT IDENTITY on the sealed forms) IS CLOSED AS DEAD (supplement S1,
fc4368c7…). It cannot succeed without a forbidden idealization. THE REFUTING
WITNESS IS THIS LANE'S OWN, sealed at 65a7b799…: exact Fractions, rank-3
rational projector, n = 6, one power of eps per cell vertex:

   Phi_12 : eps^1 coefficient = 0                    (connected, correct)
   Phi_12 : eps^2 coefficient = -346463176730651/17428667193612
   -tr[C Y_2 Y_1 C]  (ONE sea line)  = -1337849531/65078154
   +tr[C Y_1 C Y_2]  (TWO sea lines) = 35484269897501/52286001580836
   eps^2 == oneline + twoline : TRUE
   eps^2 == twoline alone     : FALSE
   one-line term identically zero : FALSE

A universal zero identity is refuted by that witness. Y_2 Y_1 = 0 holds only
in the strict equal-time multiplication-operator idealization with disjoint
supports; the actual V_i - 1 are Dyson-dressed by free h_0 propagation over
the whole interval. ANY EXECUTION ARTIFACT THAT ATTEMPTS ARM 1, OR THAT CITES
Y_2 Y_1 = 0, IS A SPEC VIOLATION AND BLOCKS with witness
A_L0_ARM1_REANIMATED.
LAPSE OF RECORD, CARRIED FORWARD UNSOFTENED: the two-armed A-L0 was sealed one
artifact after the erratum whose witness had already killed arm 1. This lane
did not cross-check its own binding against its own erratum; the independent
system caught it. No executor was misdirected because no execution occurred.
```

### O.A0.2 — A-L0 (arm 2), the Huygens-bound target: BOTH factors required

```text
A-L0  ONE-LINE CONNECTED CROSS-TERM BOUND (arm 2; the ONLY surviving
      certification route). Bound the ACTUAL Dyson-dressed, RELAY-ORDERED
      cross term tr[C Y_2 Y_1 C] with a CERTIFIED decay in the cell
      separation, UNIFORM over the D3 quantifier, AND WITH ENOUGH DECAY BEYOND
      BARE R^-3 THAT THE ANCHORED SUMS CONVERGE. Nothing weaker discharges it.

NAMED TARGET (9a0c2045… §2.2, binding):
      E1_ONE_LINE_CONNECTED_CROSS_TERM_FREE_HUYGENS_BOUND
The free/Dyson propagation bridge must supply BOTH:
      (i)  LIGHT-CONE / HUYGENS COLLAR SUPPORT, reducing the shell count from
           R^3 to R^2; AND
      (ii) AMPLITUDE DECAY of at least R^-1 after the cell-time integrations.
Then the anchored sum carries R^2 · R^-3 · R^-1 = R^-2, which is summable.
*** NEITHER FACTOR ALONE SUFFICES: (i) without (ii) leaves R^-1, DIVERGENT;
(ii) without (i) leaves R^-1, DIVERGENT. *** An artifact certifying one factor
and asserting the bound BLOCKS with witness
A_L0_HUYGENS_BOUND_ONE_FACTOR_ONLY.
FAILURE WITNESS: E1_ONE_LINE_CONNECTED_CROSS_TERM_UNCERTIFIED.

EXACT ARITHMETIC OF THE TARGET, frozen here and re-verified this session on
the cubic skeleton (family A instance; the D3-uniform statement is A-L0.4):
      BOTH FACTORS:  sum_k (24k^2+2)/k^4 = 24 zeta(2) + 2 zeta(4)
                                         = 4 pi^2 + pi^4/45   (CLOSED FORM)
                     exact-rational partials 41.404259 / 41.619076 / 41.635065
                     / 41.641864 at K = 100 / 1e3 / 3e3 / 2e4, against
                     41.6430640717797…; coefficient checks 24/6 = 4 and
                     2/90 = 1/45 exact.
      (i) ALONE:     sum_k (24k^2+2)/k^3 = 24 H_K + 2 zeta(3) — DIVERGENT as
                     24 log K. Residual at K = 3000: 2.4041136952 against
                     2 zeta(3) = 2.4041138063…
      (ii) ALONE:    sum_k (64k^3+16k)/k^4 = 64 H_K + 16 zeta(3) — DIVERGENT
                     as 64 log K. Residual at K = 3000: 19.2329095620
                     against 16 zeta(3) = 19.2329104506…
NOTE, AND IT IS THE REASON NC3 IS THE DETECTOR: BOTH failure modes reproduce a
LOGARITHMIC divergence of exactly NC3's 24 H_K / 64 H_K shape. NC3 is
therefore not a bystander — it is the executable detector of arm 2's failure.
Unlike A-L3's 4-D constant, this target's constant HAS a closed form; the
artifact must still certify it by outward enclosure (§N) and must not treat
the closed form as a substitute for the enclosure.

CANCELLATION INVENTORY, verified consistent with the sealed record (9a0c2045…):
CTP/Moebius kills DISCONNECTED terms ONLY; the spinor-odd trace and
m_0 = m_1 = 0 are SATURATED at full tau_R (C4); TIME-INTEGRATION SMOOTHING IS
THE ONLY REMAINING SUMMABILITY SOURCE. No artifact may claim a fourth source
without an exact witness.
CONVERGENCE OF RECORD: this is independently identical to this lane's own
finding that only TWO-TIME / scattering-type objects can work, the equal-time
object provably failing Shale-Stinespring (C6). Two systems reached it by
different routes; it is the ORGANIZING CONSTRAINT of arm 2, not an observation.
```

### O.A0.3 — Reading A is COMPELLED; Q6 recast (§Q6')

```text
Q6_UNIFORM_RAW_ADJACENCY_DEGREE_FALSE_ON_FULL_D3 (9a0c2045… §2.1). Arbitrary
further common refinements admit star-refined atoms of unbounded facet count,
so NO uniform raw adjacency-degree bound exists over full D3 (independent-
system construction). DECISIVE CONSEQUENCE: the
derive-D5-from-local-weights-plus-raw-degree route is IMPOSSIBLE on full D3.
RAW-DEGREE KP IS CLOSED. This is a RESULT, not a gap.

READING A (ADOPTED, AND NOW *COMPELLED*, NOT PREFERRED): M2/D5 supplies the
ANCHORED-SUM bound DIRECTLY; M3's closure is a GEOMETRIC SERIES and the KP
paragraph is rewritten as that. Already committed as D1 of aa8758a9…; now
compelled by the refutation.
READING B (admissible in ONE form only): a WEIGHTED, SUBDIVISION-INSENSITIVE
polymer-counting replacement, PROVED. RAW DEGREE MAY NOT APPEAR IN IT. Absent
that proof, reading B is NOT AVAILABLE.
Q6 IS NOT RETIRED: it is RE-CAST as that weighted/subdivision-insensitive
counting obligation, live only if reading B is ever pursued. ITS RAW-DEGREE
FORM MAY NOT APPEAR ANYWHERE IN THIS PROGRAM'S ARTIFACTS except as the
recorded closed-false result. Violation BLOCKS with witness
Q6_RAW_DEGREE_FORM_REANIMATED.
```

### O.A0.4 — The M2 burden, named as a blocker (the honest cost of reading A)

```text
A-L5  D3-UNIFORM ANCHORED-SUM OBLIGATION (NEW; created by this spec).
      Under reading A the anchored-sum bound of D5' must be delivered
      DIRECTLY, per unit cell 4-volume, UNIFORMLY OVER FULL D3. The Chebyshev
      shell counts of A-L3/A-L0.2 are a CUBIC-SKELETON, FAMILY-A INSTANCE and
      DO NOT deliver it (B-6): family B (oriented simplicial/barycentric) and
      arbitrary common refinements falsify those counts. What must be
      exhibited is a SUBDIVISION-INSENSITIVE per-4-volume argument — the R1-R4
      re-aggregation machinery (679ba036…) supplies exact 4-volume additivity
      and loss-free re-aggregation of the WEIGHT, but NOT the COUNT of
      anchored connected clusters of size n.
      Witnesses: E1_ANCHORED_SUM_NOT_D3_UNIFORM (primary);
      E1_SHELL_COUNT_NOT_UNIFORM_OVER_D3 (the family-B/common-refinement gap).
      STATED WITHOUT SOFTENING, AND REPEATED IN §V: reading A does not remove
      the counting problem, it MOVES IT ONTO M2 — which is this spec's own
      open obligation. That is the honest cost of the compelled reading, and
      it is the second reason (beside A-L0) that this program's predicted
      outcome is a BLOCK.
```

---

## §Q6' — Standing of Q6 in this spec

```text
This spec owns E1 only. Discharging every obligation here does not by itself
deliver the Route-Q predicate (correct in v001 and retained). CORRECTED
(B-6): v001's further claim that Q6 is "NOT absorbed by any route below" was
FALSE for IR-A as specified — IR-A silently consumed a D3-uniform
cluster/shell count. Under this v002: A-L3/A-L4 are SCOPED to the cubic
skeleton and family A; the D3-uniform statement is A-L5, owned here and named
as a blocker; the recast Q6 remains the parent's, live only under reading B;
its raw-degree form is CLOSED FALSE. Route Q carries the full D3 quantifier
alone contingent on BOTH (i) a successor E1 architecture and (ii) the recast
Q6 under whichever reading is pursued — two contingencies, not one
(f84c3036…).
```

---

## §R — REPLACEMENT ACTIVITY ARCHITECTURE (SCAD, repaired)

**Name:** `SCAD` — *Subtracted Carleman Action-Density*. Frozen outcome-blind,
before any verdict-bearing computation. Organizing principle:
**cancellation-first** (CR.R5) — the a-difference and the Moebius difference
are taken **before any norm is applied**, and **the baseline is never normed**
(B-2).

### R.0 — Reduction and the subtracted object

Per admitted state (M-3), per admitted cell `C` of D3, per record-color pair
`(mu, lambda)`, per CTP pair on the closed pair polydisc (M-2), with
`V_{mu lambda}(a) := u_mu^{(c)}(a_-)^dagger u_lambda^{(c)}(a_+)`:

```text
Block-triangular identity (obligation R-L1):
    1 + C(V-1) = [[ C V C , C V (1-C) ] , [ 0 , I ]]
  => det(1 + C(V-1)) = det_{ran C}(C V C).
    A_{mu lambda}(a)     := C(V_{mu lambda}(a) - 1)C
    Delta_{mu lambda}(a) := A(a) - A(0) = C(V(a) - V(0))C
    A_{mu lambda,s}(a)   := A(0) + s Delta(a),  s in [0,1]
Carleman: det(1+A) = det_2(1+A) e^{tr A}, Log det_2(1+A) = tr[Log(1+A) - A],
    Log rho(a) := Log[ det(1+A(a))/det(1+A(0)) ]
                = tr[Delta] - int_0^1 tr[(1+A_s)^{-1} A_s Delta] ds
    — VALID ONLY ON THE SURVIVING SECTOR (R.2), where det(1+A(0)) != 0.
```

**Correction to the memo's IR-B display, retained (F'-14).** The memo's §2
subtracted display is valid **per color pair**, not for the color-summed
object: `Z_comp^{(C)}(a) = sum_{mu,lambda} w_mu^* w_lambda det(1+A_{mu lambda}(a))`
is a sum of determinants and the log of a sum is not a sum of logs. Applying
the per-pair display to the summed object BLOCKS with witness
`SCAD_COLOR_SUM_LOG_MISUSE`.

### R.1 — The frozen SCAD constants: PER-CELL FIRST (B-5), S3 DELETED (B-2)

```text
*** ORDER OF QUANTIFICATION, REPAIRED. Each S_i is a PER-CELL functional
S_i(C, eps). The sup over admitted cells is taken ONLY AFTER the cell-scale
weight has been exhibited (R-L0 ground (i)). A sup-first freeze makes R-L0
unsatisfiable, because a cell-independent number cannot carry a scaling
weight; that defect is repaired here, not fenced. ***
All are functionals of (||b_D||, tau_R, sea-kernel decay data, |w_lambda|)
only — no Hermite carrier index n, no ell, no truncation level, no
cellulation-family index, NO CELLULATION GEOMETRIC DATUM. Each requires a
certified outward enclosure (§N). The sups over states, color pairs on the
SURVIVING sector, and the closed pair polydisc at radius eps are taken as
stated; the sup over CELLS is deferred to R-L0.

S1. G_tr(C, eps)  := |C|_4^{-1} · | tr_{ran C}[ C(V(a) - V(0))C ] |
      [SUBTRACTED TRACE DENSITY. The a-independent sea-depth divergence is
       absent by construction; the leading residue is killed TWICE — odd
       spinor trace tr_spinor[C(p) alpha_x] = -2 p-hat_x, and |m_0|^2 = 0.]

S2. G_hs(C, eps)  := |C|_4^{-alpha} · || C(V(a) - V(0))C ||_2
      [SUBTRACTED HILBERT-SCHMIDT DENSITY. MUST be a TWO-TIME (cell-S-matrix)
       object; the equal-time version is FALSE by C6. *** THE EXPONENT alpha
       IS NOT ASSERTED. *** v001 wrote 1/2 without derivation; R-L2b must
       DERIVE it. Until R-L2b closes, alpha is a symbol, not 1/2.]

S2b. G_cm(C, eps) := |C|_4^{-beta} · (certified bound on the C-L2 commutator
       error [h_0, M(t) ⊗ S] in the quadratic form C-L2 names)
      [*** REPLACES THE DELETED S3/G_bl. *** Under C-L1 the same-phase sector
       has V(0) = I EXACTLY up to this error, so the ONLY baseline quantity
       entering any bound is this error — never a norm of the baseline itself.
       beta is derived with alpha under R-L2b.
       Witness: E1_RECORD_KINK_COMMUTATOR_FORM_UNCERTIFIED.]

S3. *** DELETED. *** G_bl (the equal-time baseline HS density) is REMOVED FROM
      THE ARCHITECTURE. Reason, on the record: it is the cell-level
      Shale-Stinespring quantity, which C6 — a frozen input of this same spec
      — makes INFINITE; under C-L1's exact collapse the opposite-phase
      baseline is 2||CPC||_2, and ||CPC||_2 is radius-independent by dilation
      covariance and infinite by C6; and a scale-invariant numerator divided
      by |C|_4^{alpha} -> 0 under refinement diverges regardless. v001 froze
      it finite and consumed it. ANY REAPPEARANCE OF G_bl OR OF ANY NORM OF
      THE BASELINE BLOCKS with witness SCAD_BASELINE_NORMED.

S4. rho_res(C, eps) := sup_{s in [0,1]} || (1 + A_{mu lambda,s}(a))^{-1} ||_op,
      *** THE SUP AND THE CARLEMAN SEGMENT RESTRICTED TO THE SURVIVING SECTOR
      (R.2). *** On the opposite-phase sector the segment starts at
      1 + A(0) = 1 - 2CPC, which is not a trace-class perturbation of the
      identity, so an unrestricted sup is +infinity as written (B-3).
      NAMED HYPOTHESIS H-R. NOT discharged here. May NEVER default to 1 or to
      any other value (F'-3); it may enter a threshold comparison ONLY in the
      §E1' step-2 conditional form.

S5. kappa_bal := [ sum_{surviving (mu,lambda)} |w_mu^* w_lambda| ·
                     |det(1+A_{mu lambda}(0))| ]
                / | sum_{surviving (mu,lambda)} w_mu^* w_lambda ·
                     det(1+A_{mu lambda}(0)) |
      [BASELINE BALANCE RATIO, RE-DERIVED OVER THE SURVIVING SECTOR ONLY
       (B-3). NAMED HYPOTHESIS H-B0 = H-B in ratio form (L2 fence 3),
       inheriting its undischarged status. THE (1+|D|)/|1-D| DISPLAY IS
       STRICKEN and may not be cited.]
```

### R.2 — Derived structure of the baseline: the sector that drops out

**Offered as obligations R-L4a/R-L4b/R-L4, never as results.** Under C-L1's
exact record-phase collapse, with `P` the cell's sharp record projector and
phases `(+1,-1,-1)` on `lambda = (0, +sqrt2, -sqrt2)`:

```text
V_{mu lambda}(0) - 1 = (phase_mu · phase_lambda - 1) P
                     = 0     for SAME-phase pairs
                     = -2 P  for OPPOSITE-phase pairs.
Weight bookkeeping (exact; independently confirmed by the reviewer):
   S_+ := sum_{phase=+1} w_lambda = 1/2,  S_- := sum_{phase=-1} w_lambda = -1/2
   same-phase pair weight total     = S_+^2 + S_-^2 = 1/2 (signed and absolute)
   opposite-phase pair weight total = 2 S_+ S_-      = -1/2 signed, 1/2 absolute

SAME-PHASE (SURVIVING) SECTOR: V(0) = I exactly (M(t) = 0 off the ball, phases
   equal on it), hence A(0) = 0 up to the C-L2 commutator error, hence
   det(1 + A(0)) = 1 up to that error. NOTHING IS NORMED HERE.
OPPOSITE-PHASE SECTOR: tr A_{mu lambda}(a) = -2 tr(CPC) = -infinity, tr(CPC)
   being the mode count of the sea inside the ball (C2's own divergence).
   Obligation R-L4b: THE SECTOR VANISHES IDENTICALLY on the closed pair
   polydisc — det(1 + A(a)) = 0 for ALL a, not only at a = 0 — so it drops out
   of numerator AND denominator, and it is EXCLUDED from every sum, sup and
   segment rather than being assigned a value.
```

```text
R-L4a BASELINE DETERMINANT: EXISTENCE OR NON-EXISTENCE (replaces v001's
      invalid limit; B-4). Establish, via the Carleman factorization
      det = det_2 · e^{tr} AND WITH THE REGULARIZATION EXPLICITLY NAMED,
      whether the opposite-phase baseline determinant EXISTS. AT THE POINT
      WHERE C6's HYPOTHESIS HOLDS, THE OBJECT `D = det_{ran C}(1 - 2CPC)`
      DOES NOT EXIST AS A FREDHOLM DETERMINANT — tr(CPC) = +infinity — so the
      correct unregularized statement is "D IS UNDEFINED", NOT "D = 0".
      *** THE INEQUALITY D^2 <= exp(-2||[C,P]||_2^2) IS STRICKEN AS A GROUND
      FOR D = 0. *** It is a finite-dimensional identity/inequality (200 exact
      trials, no violation; the exact commutator identity
      ||[C,P]||_2^2 = 2 sum_i sigma_i(1-sigma_i) on 50 exact trials) and may
      be REPORTED as such; it may not be evaluated at an infinite right-hand
      side, and no artifact may infer a value of D from it.
      The conclusion may well be RECOVERABLE by the regularized route
      (det = det_2 · e^{tr} with tr = -infinity ⇒ det = 0). THAT IS A
      DIFFERENT AND HONEST ARGUMENT AND IT IS THE ONE R-L4b MUST MAKE.
      Witness: E1_BASELINE_DETERMINANT_EXISTENCE_UNCERTIFIED.
R-L4b OPPOSITE-PHASE SECTOR VANISHES IDENTICALLY, as displayed above, on the
      closed pair polydisc, with the regularization of R-L4a.
      Witness: E1_OPPOSITE_PHASE_SECTOR_VANISHING_UNCERTIFIED.
R-L4  BASELINE BOOKKEEPING, REPORTED PER STATE: the weight algebra above
      (independently confirmed), the finite-trial identity and inequality as
      REPORTED items only. MUST be reported as a CANDIDATE partial statement
      about the single-cell baseline, NEVER as a discharge of H-B.
      Witness: E1_BASELINE_COLLAPSE_UNCERTIFIED.
```

```text
CONSEQUENCE FOR kappa_bal, RE-DERIVED (B-3). With the opposite-phase sector
excluded, the surviving weights are 1/2 signed and 1/2 absolute, so
      kappa_bal = (1/2)/(1/2) = 1
follows FROM THE SURVIVING WEIGHTS — arithmetic re-checked exactly this
session — and NOT from the (1+|D|)/|1-D| display, and NOT from any claim that
D = 0. Any artifact deriving kappa_bal from that display, or from a value of
D, BLOCKS with witness KAPPA_BAL_DERIVED_FROM_STRICKEN_DISPLAY.
```

### R.3 — The derived per-cell (`n = 1`) majorant

```text
  x(C, eps) := |C|_4 · g(C, eps),
  g(C, eps) := G_tr(C,eps) + rho_res(C,eps) · G_hs(C,eps) · ( G_cm(C,eps)
                                                            + G_hs(C,eps) ).
```

Derivation: `||A_s||_2 <= ||A(0)||_2 + ||Delta||_2 <= |C|_4^{beta} G_cm +
|C|_4^{alpha} G_hs` on the surviving sector (where `A(0)` is the C-L2 error,
NOT a baseline norm), `||Delta||_2 <= |C|_4^{alpha} G_hs`, and
`|tr[B X Y]| <= ||B||_op ||X||_2 ||Y||_2`.

```text
*** BOOKKEEPING STATEMENT, DOWNGRADED (C-13). *** That the two half-powers
multiply to |C|_4 is BOOKKEEPING CONSISTENT WITH D5 *CONDITIONAL ON R-L2b*:
it holds for ANY exponent pair summing to 1 and asserts nothing unless the HS
norms are FINITE AT THOSE EXPONENTS UNIFORMLY OVER THE D3 REFINEMENT
QUANTIFIER. If the true scaling is |C|_4^{alpha} with alpha < 1/2 the sup
diverges under refinement — B-2 exhibits exactly that for the deleted S3,
where the true scaling is alpha = 0. THE CLAIM "IT IS THE ANSWER TO C2" IS
DELETED and may not be restated.

R-L2b SCALING-EXPONENT DERIVATION (new; C-13). DERIVE alpha (and beta):
      certify || C(V(a) - V(0)) C ||_2 <= |C|_4^{alpha} G_hs with G_hs finite
      uniformly over the D3 refinement quantifier, EXHIBITING THE MECHANISM
      that supplies the powers — cell time extent from the Duhamel bound, and
      the Gevrey b_D. State the same for beta and G_cm. alpha = 1/2 may be the
      answer; it may not be the assumption.
      Witness: SCAD_HS_SCALING_EXPONENT_UNDERIVED.
```

Colour-sum closure, **over the surviving sector only** (B-3):

```text
  Z_hat_comp^{(C)}(a) = sum_{surviving (mu,lambda)} c_{mu lambda} rho_{mu lambda}(a),
  c_{mu lambda} := w_mu^* w_lambda det(1+A_{mu lambda}(0)) / N_surv(0),
  N_surv(0)   := sum_{surviving} w_mu^* w_lambda det(1+A_{mu lambda}(0)),
  sum_surviving c = 1,   sum_surviving |c| = kappa_bal,
  |Log rho(a)| <= x(C,eps)                                        (R.3.a)
  |rho(a) - 1| <= x e^{x}
  |Phi_C(a)| <= kappa_bal x e^{x} / (1 - kappa_bal x e^{x})       (R.3.b)
      provided kappa_bal x e^{x} < 1.
NO TERM OF THE EXCLUDED SECTOR APPEARS IN ANY OF THESE SUMS. An artifact that
forms rho on a pair with det(1+A(0)) = 0, or that carries a 0·(0/0) term,
BLOCKS with witness SCAD_VANISHING_SECTOR_DIVIDED.
```

### R.4 — Cell-scale normalization: named, and NOT absorbed

```text
R-L0  CELL-SCALE NORMALIZATION OBLIGATION (load-bearing). Exhibit X_*(eps), a
      functional of (||b_D||, tau_R, sea-kernel decay data, |w_lambda|) ONLY,
      with x(C,eps) = |C|_4 g(C,eps) <= X_*(eps) for EVERY admitted cell of
      D3, and with kappa_bal · X_*(eps) · e^{X_*(eps)} <= 1/2 certified (the
      1/2 is the parent's frozen E1 threshold, re-used; NO new number).
      TWO ADMISSIBLE GROUNDS, AND ONLY THESE — both now TESTABLE because
      S1-S5 are per-cell (B-5):
        (i)  SCALE COVARIANCE: g(C,eps) carries a compensating negative
             scaling weight, so |C|_4 g(C,eps) is scale-invariant. Available
             inputs: per-cell scale covariance of the sealed construction;
             ||b_D^{(c)}||_inf = 1 EXACTLY for every admitted cell (679ba036…
             §3.1); v(t) scale-covariant; the diamond profile scale-free.
        (ii) UNIFORM SMALLNESS in the cell scale, per cell.
      THE HAZARD, STATED: tau_R is scale-INVARIANT — every refined cell
      inserts a FULL record cycle at every refinement depth, at exact phase
      e^{+-i pi} = -1. This is the structural root of the O7 obstruction
      (3c81647e…) and the same fact that saturates C4. It is therefore NOT a
      priori true that g carries the compensating weight, and R-L0 MAY FAIL.
      NAMED WITNESS: E1_CELL_SCALE_NORMALIZATION_UNCERTIFIED.
      FORBIDDEN: substituting any coarsest-cell 4-volume, any V_max, any
      skeleton datum, or any cellulation-family quantity for X_*. BLOCKS with
      witness SCOPING_CLAUSE_1_VIOLATION_CELLULATION_DATUM.

R-L0b EXPONENTIATION-FREE COLOUR-SUM CLOSURE (new; B-5). The requirement for
      an absolute bound on x arises SOLELY from the colour-sum step (the
      |rho - 1| <= x e^x exponentiation and the 1/(1 - kappa x e^x)
      denominator); THE LINEAR CARLEMAN ESTIMATE ALONE ALREADY YIELDS
      ACTION-DENSITY FORM. Bound Log(sum_surviving c rho) WITHOUT an absolute
      bound on x — e.g. by a signed-weight convexity argument on the surviving
      sector. If R-L0b closes, R-L0 is not needed for the n = 1 leg and that
      must be stated. Witness: SCAD_COLOR_SUM_REQUIRES_ABSOLUTE_X_BOUND.

RECORDED HONESTLY: R-L0 is not an artefact of this architecture.
Scale-uniformity of |Phi_C|/|C|_4 across the admitted scales IS the content of
E1. Any activity architecture must deliver it. The replacement's contribution
is to make it a named lemma with a checkable sufficient condition, and to
supply R-L0b as an alternative that does not need it.

With R-L0 discharged:  eta_1(eps) := 2 · kappa_bal · sup_C g(C,eps) · e^{X_*(eps)}
      [from (R.3.b) with kappa_bal x e^x <= 1/2].
```

### R.5 — Frozen supersession of the Phase-1 functional

```text
eta(eps) = (2 eps ||b_D||_inf K_sea / b_0) exp(1 + T_R + 2 eps ||b_D||_inf
K_sea) and its constants (K_sea, T_R, b_0) are RETIRED, not certified. They
may appear in exactly two places: the historical record of C2, and NC10. Any
bound, enclosure, tolerance, or verdict consuming them BLOCKS with witness
PHASE1_KSEA_ARCHITECTURE_REANIMATED.
```

### R.6 — HONEST STATEMENT: SCAD IS NOT AN INDEPENDENT ROUTE (B-2, mandatory)

```text
*** After the B-2 repair, EVERY surviving constant of this architecture rests
on C-L2. S2b IS the C-L2 commutator error; S2's two-time finiteness is what
C6 says only a two-time object can have; S4 and S5 are defined on the sector
that survives only because C-L1/C-L2 make V(0) = I there. THEREFORE SCAD IS
NOT AN INDEPENDENT ROUTE — IT IS IR-C's WALL RE-EXPRESSED. ***
This statement is repeated in §V and §P as the repair binding requires, and it
is the reason §O.X exists: a failure at the crux is reported ONCE.
```

---

## §O.X — B-L2\*: THE SINGLE NAMED CRUX WHERE BOTH ROUTE-SETS TRIANGULATE

```text
B-L2*  CARRIER-UNIFORM HILBERT-SCHMIDT BOUND ON THE RECORD-VERTEX PAIRING,
       WITH THE CELL-TIME INTEGRATION SUPPLYING THE DECAY THAT THE EQUAL-TIME
       OBJECT PROVABLY LACKS (repair binding R6, verbatim in substance).
       Equal-time localization of the 3-D massless Dirac sea fails
       Shale-Stinespring; only two-time / scattering-type objects can work
       (C6). The bound must be stated as a TWO-TIME (cell-S-matrix) object and
       must be carrier-uniform; the equal-time version is FALSE and the
       artifact must SAY SO rather than route around it.
       LOCUS, per the C6 refinement: the VOLUME DIAGONAL x = y. A bound that
       controls only the boundary region does not discharge B-L2*.
       Witness: E1_SEA_OFFDIAGONAL_HS_SHARP_RECORD_LOCALIZER.

*** BOTH ROUTE-SETS REDUCE TO B-L2*. *** IR-B / Codex Route 1 reduce to it
directly (it is their numerator bound). IR-C / Codex Route 3 reduce to it
through C-L2, and §R.6 shows SCAD's four surviving constants do too. IR-A does
not reduce to it — IR-A's wall is A-L0/A-L5.
REPORTING RULE, BINDING: a failure at B-L2* IS REPORTED ONCE, AS THE COMMON
WALL — not three times as three route failures, and not as independent
corroboration of itself. An artifact reporting the same B-L2* failure as
multiple independent route failures, or citing one route's failure as evidence
for another's, BLOCKS with witness COMMON_WALL_REPORTED_MULTIPLY.
```

---

## §E1' — Frozen derivation rule for the tolerances (outcome-blind)

```text
1. Derive S1, S2, S2b, S4, S5 as PER-CELL functionals and X_*(eps) per R-L0
   (or discharge R-L0b), each with a certified outward enclosure (§N).
   Assemble g, eta_1 per R.3-R.4, and eta_{>=2} per the route taken — noting
   that eta_{>=2} certifies the TWO-LINE SECTOR only until A-L0 closes, and
   only on the cubic skeleton / family A until A-L5 closes.

2. On the parent's frozen dyadic grid eps in {2^-k : k = 1..64}:
     eps_*^{(>=2)} := max { 2^-k : eta_{>=2}(2^-k) <= 1/2 certified }
     eps_*^{(1)}   := max { 2^-k : the IMPLICATION
                       "rho_res <= rho_bar  =>  eta_1(2^-k) <= 1/2"
                       is CERTIFIED }
   *** THE n = 1 LEG IS A CONDITIONAL CERTIFICATION (B-7). *** rho_bar is an
   EXPLICIT DISCLOSED-PREMISE SYMBOL; the artifact MUST state its admissible
   range; eps_*^{(1)} so obtained is PREMISE-CONDITIONAL and MAY NOT be
   supplied to I3 as unconditional. This is the ONLY permitted form of
   premise-carrying in a threshold comparison anywhere in this program
   (F'-3). Assigning rho_bar a numeric default — including 1 — BLOCKS.
     eps_* := min(eps_*^{(1)}, eps_*^{(>=2)}), carrying the conditionality.
   The threshold 1/2 is the parent's, frozen, outcome-blind, on BOTH legs.

3. Certify Gamma_star^split := eta_1(eps_*) + eta_{>=2}(eps_*)^2 /
   (1 - eta_{>=2}(eps_*)) <= 1, with the same premise-conditionality
   propagated and marked.

4. If no grid point qualifies on a leg: E1S_BLOCKED with witness
   EPSILON_STAR_VACUOUS_{n1 | nge2}. This is DISTINCT from "the enclosure
   could not be certified at all", which is E1S_BLOCKED with the route's own
   named witness. The distinction is mandatory in the artifact.

5. eps_*, eta_1, eta_{>=2}, Gamma_star^split, rho_bar may NEVER be tuned by
   any output — not by W1, not by any control, not by NC9, not by any
   consumer. Re-derivation requires a further append-only successor spec.

6. ETA_MONOTONICITY_UNCERTIFIED (parent M-8) is carried: the grid max is
   well-posed regardless of monotonicity; monotonicity is REPORTED, never
   assumed.

7. No measured constant appears in this spec, its constants file, or any
   admissible artifact. Permitted exact quantities: rationals, pi, sqrt(2),
   zeta values, e — all with certified outward enclosures.
```

---

## §O — Obligations

Inherited and cited, not re-proved: **O1 (Lemma 0, read CTP-NESTED per
D-O1)**, **O2 (action-density construction and the M-4 re-aggregation identity
over the full common-refinement poset; Lemmas R1-R4 of 679ba036…)**, **R1-R4**.

**M1's two compliance citations are mandatory verbatim in every result
artifact**: gate item 9 (`4e1282bc…`, determinant fence satisfied TERMWISE; no
single postselected determinant replaces the sum) and the A4 obligation
relocation (`8a7f52ff…`) carrying the **M-11 disclaimer verbatim**.

### O.R — Architecture obligations (common; must close first)

```text
R-L0   Cell-scale normalization, per R.4.  E1_CELL_SCALE_NORMALIZATION_UNCERTIFIED
R-L0b  Exponentiation-free colour-sum closure. SCAD_COLOR_SUM_REQUIRES_ABSOLUTE_X_BOUND
R-L1   Block-triangular reduction on the sealed forms, adjoint-continued pair
       (M-2).  SCAD_BLOCK_TRIANGULAR_REDUCTION_UNCERTIFIED
R-L2   Certified Carleman machinery: det(1+A) = det_2(1+A) e^{tr A};
       |det_2(1+A)| <= exp(||A||_2^2/2); the differentiated identity
       d/ds Log det_2(1+A_s) = tr[((1+A_s)^{-1} - 1) Delta]; the
       trace-of-product estimate. Every constant explicit and outward-enclosed;
       NO textbook constant by citation alone.  SCAD_CARLEMAN_CONSTANTS_UNCERTIFIED
R-L2b  Scaling-exponent derivation (alpha, beta), per R.3.
       SCAD_HS_SCALING_EXPONENT_UNDERIVED
R-L3   Colour-sum handling ON THE SURVIVING SECTOR: sum c = 1,
       sum |c| = kappa_bal, (R.3.b); includes the explicit refutation of
       applying the per-pair display to the summed object.
       SCAD_COLOR_SUM_LOG_MISUSE
R-L4a  Baseline determinant existence-or-nonexistence via det_2 · e^{tr}, with
       the regularization named.  E1_BASELINE_DETERMINANT_EXISTENCE_UNCERTIFIED
R-L4b  Opposite-phase sector vanishes identically on the closed pair polydisc.
       E1_OPPOSITE_PHASE_SECTOR_VANISHING_UNCERTIFIED
R-L4   Baseline bookkeeping, reported per state; never a discharge of H-B.
       E1_BASELINE_COLLAPSE_UNCERTIFIED
R-L5   Named-hypothesis register in every artifact: H-B (parent,
       undischarged), H-B0 (kappa_bal), H-R (rho_res), H-Z0
       (Z_comp(0) != 0, per CR.R5), H-IND (discharged by Lemma 0), plus the
       disclosed-premise symbol rho_bar. Silently valuing any of them BLOCKS
       (F'-3).
```

### O.A — ROUTE IR-A: the two-line sector, SCOPED (no n >= 2 claim)

```text
A-L1  CROSS-CELL HILBERT-SCHMIDT BOUND. Certify, in outward-enclosed exact
      rational arithmetic from C1's closed-form kernel:
          || 1_{D_1} C 1_{D_2} ||_2^2  <=  |D_1||D_2| / (pi^4 R^6),
          R = dist(D_1, D_2).
      CORRECTION TO THE MEMO, RETAINED AND NOW INDEPENDENTLY CONFIRMED: the
      memo's 1/(4 pi^4 R^6) is the PER-COMPONENT reading and is a factor 4
      optimistic; with (alpha·r)^2 = |r|^2 I_4 and ||alpha·r||_F^2 = 4|r|^2,
      ||C_off||_F^2 = 1/(pi^4 |r|^6). THIS SPEC FREEZES THE CONSERVATIVE
      CONSTANT 1/(pi^4 R^6). The execution must PROVE which convention the HS
      pairing requires; using the smaller constant without that proof BLOCKS
      with A_L1_SPINOR_TRACE_CONVENTION_UNPINNED. SECOND UNPINNED ITEM:
      |D_1|, |D_2| must be pinned as EQUAL-TIME spatial volumes or SPACETIME
      4-volumes, consistently with the two-time reading C6 and S2 demand.
      Witness: A_L1_VOLUME_TYPING_UNPINNED.

A-L2  LIGHT-CONE / NULL-SEPARATION CONTROL. Cells at NULL separation get no
      help from an equal-time bound. Certify that the Gevrey diamond profile
      b_D = exp(16 - 1/s) (vanishing to all orders at the diamond boundary and
      both tips, ||b_D||_inf = 1 exactly) TOGETHER WITH the cell time
      integration restores decay along the light cone, uniformly over D3 and
      over the envelope-profile class. NOTE: A-L2 and A-L0's factor (i) are
      the same physics seen from two sides — the collar that supplies A-L0's
      R^3 -> R^2 reduction is what A-L2 must control. They may be discharged
      together; a discharge of one may NOT be cited as a discharge of the
      other.  Witness: E1_NULL_SEPARATION_CLUSTER_DECAY_UNCERTIFIED

A-L3  TWO-LINE-SECTOR ANCHORED SUMS — *** SCOPED TO THE CUBIC SKELETON AND
      FAMILY A *** (B-6). Assemble with the exact shell identities
      (re-verified k = 1..400 this session):
          3-D shell(k) = 24k^2 + 2 ;  4-D shell(k) = 64k^3 + 16k
          two-line 3-D: sum_k (24k^2+2)/k^6 = 24 zeta(4) + 2 zeta(6)
                                            = 4 pi^4/15 + 2 pi^6/945
          two-line 4-D: sum_k (64k^3+16k)/k^6 = 64 zeta(3) + 16 zeta(5)
      with exact-rational partial sums PLUS a CERTIFIED OUTWARD TAIL (no
      floating tail). zeta(3), zeta(5) admit no closed form: the 4-D constant
      is certified by enclosure only and the artifact must say so.
      *** THESE ARE CHEBYSHEV SHELL COUNTS ON A CUBIC CELLULATION. THEY ARE
      FALSE ON FAMILY B AND ON GENERAL COMMON REFINEMENTS. *** A D3-uniform
      version is NOT deliverable on the raw-degree route (CLOSED FALSE, §Q6')
      and is available only via reading B, which is unavailable absent its
      proof; the D3-uniform obligation is A-L5.
      Deliver eta_{>=2}(eps) in D5' form for the TWO-LINE SECTOR ON FAMILY A,
      and close Gamma_star^split per §E1' step 3 with that scope stated.
      Witnesses: E1_SHELL_COUNT_NOT_UNIFORM_OVER_D3 ;
      D5_SINGLE_ETA_OVERBINDS_SPLIT_AMENDMENT_REQUIRED

A-L4  REFINEMENT SCALING, SAME SCOPE. Re-derive exactly: shell count R^3 dR /
      L^4; pair activity s^2 L^8/R^6; in-cell strength s <= eps ||b_D||_inf x
      (cell time extent) ~ eps L; int_L^inf R^-3 dR = 1/(2L^2); total
      eps^2 L^4/2 = |C|_4 (eps^2/2), so eta^2 is L-INDEPENDENT. Stated for the
      TWO-LINE SECTOR on family A, and NOT extended to n = 1, NOT extended to
      the one-line sector, NOT extended beyond family A.

A-L5  D3-UNIFORM ANCHORED-SUM OBLIGATION, per §O.A0.4.
      E1_ANCHORED_SUM_NOT_D3_UNIFORM

SEALED AUTHORITIES CITABLE: 3a6ff617…; 789338ad…; 679ba036…; 52401eef…;
0df721a1…; 451550c3…; b786db3a…; plus M1's two mandatory citations with the
M-11 disclaimer.
LIKELY FAILURE MODES: A-L0 (the one-line sector) and A-L5 (D3-uniformity).
A-L2 remains a substantive lemma. ADOPTION FLAG: none.
```

### O.B — ROUTE IR-B: subtracted / regularized determinant (n = 1)

```text
B-L1  TRACE PART. Certify tr[C(V(a) - V(0))C] finite (S1) using BOTH exact
      cancellations: the odd spinor trace tr_spinor[C(p) alpha_x] = -2 p-hat_x
      and |m_0|^2 = 0. Both derivable from sealed data.
      Witness: E1_SUBLEADING_SEA_TRACE_LOG_UNCERTIFIED
B-L2  HILBERT-SCHMIDT PART = B-L2* of §O.X. Not restated as a separate wall.
      - a-VERTEX SECTOR: plausible. J = -(Q b_D Q) ⊗ alpha_x with b_D Gevrey,
        all derivatives vanishing at boundary and tips, so its spacetime
        transform decays faster than any power.
      - RECORD VERTEX: M(t) is a SHARP indicator and by C4 the pointer weights
        put it in the LEAD at full tau_R (sum_lambda w_lambda u_lambda = P).
        The locus is the VOLUME DIAGONAL (C6 refinement).
B-L3  MOEBIUS / CONNECTED TRUNCATION removes the remaining cell-local residue
      for |gamma| >= 2 (from O2; cite, do not re-prove). NOTE, per C3': the
      Moebius difference does NOT remove the one-line connected cross term —
      that is precisely what survives it. An artifact citing B-L3 against
      A-L0 BLOCKS with witness MOEBIUS_CITED_AGAINST_CROSS_TERM.
SEALED AUTHORITIES: as IR-A, plus 6f6b822a… (CTP propagator typing).
LIKELY FAILURE MODE: B-L2* on the record vertex, whose only repair would be
to soften M(t) — a SEALED PHASE-A A1 DEFINITION, NOT A LANE'S TO CHANGE.
F'-1 is NOT triggered (no clustering axiom). Routes DIRECTLY to §Q2-STOP.
```

### O.C — ROUTE IR-C: exact record-cycle collapse (decide it either way)

```text
C-L1  EXACT RECORD-PHASE COLLAPSE, PROMOTED FROM PHASE TO OPERATOR. At
      lambda tau_R in {0, +pi, -pi} (exact: int_0^1 v = tau_R = pi/sqrt2,
      S^2 = I), exp(-i lambda tau_R S) = (+1,-1,-1)·I exactly on the ball
      where M(t) = 1. Already an exact Phase-2 witness (08b91543…); extend to
      u_lambda = (I - P) + phase_lambda · P + [error].
      Witness: E1_RECORD_PHASE_OPERATOR_COLLAPSE_UNCERTIFIED
C-L2  COMMUTATOR ERROR — *** THE WHOLE CONTENT OF THIS ROUTE, AND (per §R.6)
      OF SCAD'S SURVIVING CONSTANTS. *** Control [h_0, M(t) ⊗ S] in a
      QUADRATIC-FORM / Besov-type norm. Norm-based control is unavailable
      (||[h_0, 1_B]|| = +infinity for first-order h_0 against a sharp
      indicator), so the certification must be in a quadratic form and the
      artifact must state WHICH form and WHY the operator-norm route is
      excluded. Supplies S2b.
      Witness: E1_RECORD_KINK_COMMUTATOR_FORM_UNCERTIFIED
C-L3  SHARP-KINK LOG COEFFICIENT. Evaluate EXACTLY the coefficient of the
      logarithm in Z_comp^{(C)} read as the determinant of a sharp gauge kink
      on the Dirac sea, as a functional of the frozen tuple. Reference scale
      DERIVED, not measured: the marginal kernel's absolute integral has
      coefficient EXACTLY 2/pi (C1).
      - CERTIFIED ZERO: E1 is certified at the sharp localizer at n = 1.
      - CERTIFIED NONZERO: E1 is UPGRADED to CERTIFIED DIVERGENT AT THE SEALED
        DEFINITION OF M(t), with an exact witness.
        Witness: E1_RECORD_KINK_LOG_COEFFICIENT_NONZERO_CERTIFIED
        *** TRIGGERS §Q2-STOP IMMEDIATELY, AND THE Z.2 (a)/(b)/(c)
        DECLARATION IS MANDATORY WITH IT. ***
      REPORTING FORM (C-16): the coefficient is reported ONLY in exact
      symbolic form as an explicit rational/algebraic multiple of 2/pi, NEVER
      as a decimal.
C-L4  = R-L4/R-L4a/R-L4b, owned here because C-L1 supplies their input.
C-L5  MULTI-CELL BASELINE EXTENSION. The multi-cell baseline is
      det(1 + C(prod_c V_c - 1)C) summed over colour TUPLES (read CTP-NESTED,
      D-O1), not a product of per-cell determinants; the per-cell sharp
      projectors live at distinct times and do not commute with the h_0
      evolution. If it cannot be certified, scope R-L4 explicitly to the
      single cell.  Witness: E1_MULTICELL_BASELINE_EXTENSION_UNCERTIFIED
LIKELY FAILURE MODE: C-L2. This route returns information under failure.
ADOPTION FLAG: none.
```

### O.NC — Negative controls (all mandatory; any misbehaviour BLOCKS)

```text
NC1  GHZ REFUSAL WITH THE NAMED DISCRIMINATING HYPOTHESIS. CARRIED VERBATIM.
     Preparation (|0…0> + |1…1>)/sqrt2, Z_N(A) = cos(N tau_R A), first zero
     pi/(2 N tau_R). PASS: the pipeline REFUSES, naming H-IND. Numeric
     failure, silent acceptance, or refusal on any other ground = failure.
NC2  CORRELATED-COLOUR VARIANT. CARRIED VERBATIM. A single shared colour
     across cells must make the composition identity DETECTABLY fail (nonzero
     cross-cell correlation witness, certified enclosure excluding zero).
     Silence = failure.
NC3  *** ONE-LINE-SECTOR DETECTOR — POSITIVE ROLE, PASS = DETECTION. ***
     RECAST (supplement S2; C3's dismissal is VOID). An activity bound built
     ONLY from the sealed one-root temporal-return t^-3 data must EXHIBIT the
     one-line sector's logarithmic divergence, reproducing 24 H_K exactly
     (3-D) — and that EXHIBITION IS THE PASS. The divergence is the CORRECT
     BEHAVIOUR of a one-line-only bound and is the executable detector of
     A-L0's target and of both arm-2 failure modes (§O.A0.2).
     PASS: the detector FIRES, the 24 H_K form is reproduced in exact
     rational partial sums with a certified outward tail on the 2 zeta(3)
     residual, and the artifact records the result AS EVIDENCE BEARING ON
     A-L0.
     FAIL: the detector is silent; or the artifact reports the divergence as
     "a one-line counting artifact that says nothing about E1" — that reading
     is VOID and repeating it is a spec violation with witness
     NC3_DISMISSAL_REANIMATED.
     Witness on non-executability: ONE_LINE_SECTOR_DETECTOR_NOT_EXECUTABLE
NC4  PERIODIC POSITIVE REGRESSION — CARRIED AS A NAMED NON-APPLICABILITY AND
     CONVERTED INTO A CHECKABLE FENCE (209aa390…). This spec builds no
     anchored transfer operator. The evaluator greps every artifact for the
     anchored transfer operator, the spectral gap, TT1/TT2/TT3, the refinement
     intertwiner, or the periodic promotion results, and FAILS the gate on any
     hit that is load-bearing for a bound, a constant, or a verdict.
     Historical citation in a record section is permitted.
     Witness: ROUTE_T_ARTIFACT_CONSUMED_IN_ROUTE_Q_PREDICATE
NC5  DETUNED RELAY: RECORD-ERASING ADVANCE, with M-5's EXACT witness (the
     imprecise "toward" clause is void). Weight-sum restoration
     m_0' = sum_lambda p_lambda = 1 (against the completed chain's exact 0)
     AND/OR diagonal-unitality restoration R_erased(a,a) = I, each certified
     exactly. The pipeline must detect and REFUSE.
NC6  REFINEMENT-STABILITY EXECUTABLE CONTROL. CARRIED VERBATIM. A
     deliberately NON-action-density assignment (per-cell constant activity)
     must FAIL uniformity under one common refinement of a family-A and a
     family-B member, exhibited by certified enclosure.
NC7  NO-TARGET FENCE. No kappa_record value, no alpha, no function of either,
     no target-adjacent numeric. The evaluator runs the T15-style
     transform-grep over every artifact and FAILS on any hit. Permitted
     numerical outputs are EXACTLY: eps_*, eta_1, eta_{>=2},
     Gamma_star^split, the SCAD constants (G_tr, G_hs, G_cm, rho_res,
     kappa_bal, X_*), the A-L1/A-L3/A-L0.2 geometric and zeta constants, the
     control witnesses, W1, and the C-L3 coefficient SUBJECT TO:
     *** C-16 APPENDIX, BINDING. The C-L3 coefficient is reported ONLY in
     exact symbolic form as an explicit rational/algebraic multiple of 2/pi,
     NEVER as a decimal. The transform-grep IS run on it, with a
     pre-registered exemption keyed to that symbolic form. Any numerical
     proximity to a target-adjacent value is recorded as COINCIDENCE and may
     not be commented on, compared, or propagated. ***
NC8  *** TWO-SECTOR CONTROL (RECAST; the old form is VOID). *** MANDATORY.
     Exhibit BOTH sectors of the lowest connected two-cell cumulant
     separately, on the family-A shell counts, in exact rational partial sums
     with certified outward tails:
       TWO-LINE sector: sum_k (24k^2+2)/k^6 CONVERGES to 24 zeta(4)+2 zeta(6);
         4-D to 64 zeta(3)+16 zeta(5).
       ONE-LINE sector: must be shown EITHER to vanish OR to be SEPARATELY
         BOUNDED. Its DIVERGENCE (24 H_K) IS A PASS ONLY CONDITIONAL ON A-L0
         — i.e. the control passes on a divergent one-line leg only when the
         artifact simultaneously records A-L0 as OPEN with witness
         E1_ONE_LINE_CONNECTED_CROSS_TERM_UNCERTIFIED.
     *** THE OLD FORM — mandating that a one-line bound MUST FAIL AND BE
     DISMISSED — ENTRENCHED THE REFUTED C3 AND IS VOID. *** An artifact that
     dismisses the one-line leg, or that reports the two-line leg's
     convergence as certification of the n >= 2 sums, is a control failure.
     Witness: ONE_LINE_TWO_LINE_SECTOR_CONTROL_NOT_EXECUTABLE
NC9  SHARP-VS-SMOOTH LOCALIZER DIAGNOSTIC — REPORTED, NOT ADOPTED. MANDATORY.
     Recompute the n = 1 diagnostics (S2, S2b, ||[C,P]||_2, and — if C-L3
     reaches it — the log coefficient in symbolic form) with a MOLLIFIED
     localizer in place of 1_{|x| <= r(t)}, and REPORT the difference. The
     mollifier is named, hashed and frozen before the computation and must be
     a one-parameter family reducing to the sharp indicator.
     *** THE SMOOTHED VALUE IS DIAGNOSTIC ONLY. *** It may not enter any
     bound, constant, enclosure, tolerance, verdict, or I3 supply. Its sole
     permitted use is to quantify the COST side of §Q2-STOP option (ii).
     Violation BLOCKS with SMOOTHED_LOCALIZER_ADOPTED_WITHOUT_PRINCIPAL_DECISION.
     *** MANDATORY INTERPRETIVE CLAUSE, from the C6 locus refinement: THE
     FATAL INTEGRAL IS AT THE VOLUME DIAGONAL, NOT THE BOUNDARY. BOUNDARY
     SMOOTHING ALONE CANNOT REMOVE A |x-y|^-3 POSITIVE MAJORANT. The report
     must state (a) the mollifier's smoothness class, and (b) whether the
     mollification touches the diagonal at all; a mollifier that only smooths
     the boundary must be reported as DIAGNOSTICALLY UNINFORMATIVE for B-L2*.
NC10 SUBTRACTION IS LOAD-BEARING. MANDATORY. Run SCAD with the a-subtraction
     REMOVED (norm the unsubtracted A(a) rather than Delta(a)). It MUST
     reproduce C2's divergence: power divergence (~|D_t| Lambda^3) in the
     carrier-blind reading, finite only on a fixed carrier. PASS: the
     unsubtracted variant DIVERGES and the pipeline REFUSES it by naming
     PHASE1_KSEA_ARCHITECTURE_REANIMATED. A variant that appears to certify is
     a control failure indicating a smuggled carrier index.
     Witness: SUBTRACTION_NOT_LOAD_BEARING
NC11 *** NEW: BASELINE-NORMING TRIPWIRE. *** MANDATORY. Run the architecture
     with the deleted S3/G_bl reinstated. It MUST diverge (C6 + dilation
     covariance: ||CPC||_2 is radius-independent and infinite). PASS: the
     variant DIVERGES and the pipeline REFUSES it by naming
     SCAD_BASELINE_NORMED. A finite G_bl is a control failure and indicates a
     fixed carrier or a radius-dependent reading has been smuggled in.
     Witness: BASELINE_NORMING_TRIPWIRE_NOT_EXECUTABLE
```

### O.W — Preregistered sharpening witness W1

```text
W1 := -Log Z_hat_comp^{(12)}(a) + Log Z_hat_comp^{(1)}(a) + Log Z_hat_comp^{(2)}(a),
   Z_hat_comp^{(12)} = the TWO-CELL relayed member (relay-ordered), per pinned
   state, superscript = cell set (M-9), read CTP-NESTED (D-O1).
COMPARATOR (M-1), UNDER D5' AND SCOPED PER B-1:
   |C|_4 · eta_{>=2}^2/(1 - eta_{>=2}) at the frozen certified eta_{>=2},
   WHICH IS A TWO-LINE-SECTOR, FAMILY-A COMPARATOR. Inside SHARPENS; outside
   REFUTES — against THAT bound, and the artifact must state the scope in the
   same sentence. W1 outside the comparator is ALSO consistent with the
   one-line sector being real; the artifact may not report "REFUTES" without
   recording that alternative.
HISTORY (M-9): the frozen pair (7/100, -11/100) is used IFF eps_* >= 11/100
   under the M-2 pair-modulus reading; otherwise the fallback (eps_*, -eps_*).
W1 is computed under EVERY verdict arm in which R-L1..R-L3 survive, so a route
failure FALSIFIES rather than merely returning inconclusive. Permitted by NC7.
```

### O.O6' — Parent O6's density claim, re-verbed; the KP constant line specified

```text
Consumed diff item D3 of aa8758a9…: "O6's density-EQUALITY claim is stronger
than R1-R4 force (re-verb or re-derive); the KP constant line is
underspecified as written."

O6' RE-VERBING (this spec's disposition, for the E1/M2 obligation it owns).
    WHAT R1-R4 FORCE (679ba036…, re-read this session): R1 exact 4-volume
    re-partition; R2 exact additivity of the insertion-domain integral; R3
    loss-free re-aggregation of the D5 BOUND with the SAME eta; R4 the same
    over the full common-refinement poset. THESE ARE UPPER-BOUND AND
    ADDITIVITY STATEMENTS. They force: the per-4-volume majorant is
    REFINEMENT-UNIFORM, hence the UPPER density is uniformly bounded and
    non-increasing along refinement in the sense R3 states.
    THEY DO NOT FORCE: existence of the intensive limit
    lim |X|_4^{-1}(-Log Z_hat_comp^{(K,X)}), nor its EQUALITY across the
    quantifier of theorem clause (2). Parent O6 clause (4)(i) asserts both.
    RE-VERBED FORM, binding on any artifact of this program that touches it:
      (4)(i-a) [FORCED] the per-4-volume majorant is uniform over the D3
               quantifier, so the upper density is uniformly bounded —
               subject to E1/M2 supplying the bound at all;
      (4)(i-b) [NOT FORCED; SEPARATE OBLIGATION] existence and
               cellulation-independence of the intensive limit. A two-sided
               argument is required (a matching lower bound, or a
               Fekete/subadditivity argument together with clause (4)(ii)'s
               certified subextensive boundary rate). NO ARTIFACT MAY INFER
               (i-b) FROM (i-a) OR FROM R1-R4.
      Witness: O6_DENSITY_EQUALITY_NOT_FORCED_BY_R1_R4.
    THIS SPEC DOES NOT DISCHARGE (i-b) and claims nothing about it; the
    obligation belongs to the parent spec and is recorded here so the parent's
    verb is not inherited unexamined.

KP CONSTANT LINE, SPECIFIED (replacing "convergence at eta <= 1/2"):
    UNDER THE COMPELLED READING A, THE CLOSURE IS A GEOMETRIC SERIES AND NOT A
    KOTECKY-PREISS CRITERION. The line in force is exactly:
       sum_{n >= 1} sum_{gamma ni C, |gamma| = n} |Phi_gamma(a)|
          <=  sum_{n >= 1} |C|_4 eta^n  =  |C|_4 · eta/(1 - eta)  =:  |C|_4 · Gamma_star,
       Gamma_star <= 1 at eta <= 1/2, with eta < 1 certified;
    under D5' the same line reads Gamma_star^split := eta_1 +
       eta_{>=2}^2/(1 - eta_{>=2}) <= 1 (§D5'), verified exactly to reproduce
       the parent term by term.
    NO KP TEST FUNCTION a(gamma) IS USED, and none may be introduced. The
    classical criterion sum_{gamma' incompatible with gamma} |Phi_{gamma'}|
    e^{a(gamma')} <= a(gamma) IS NOT THE FORM IN FORCE and may not be cited as
    if it were; a lane that introduces it is re-entering reading B and must
    first prove the recast Q6. Witness: KP_TEST_FUNCTION_INTRODUCED_WITHOUT_Q6.
```

---

## §Q2-STOP — ABSOLUTE FENCE 1: THE PRINCIPAL'S Q2 STOP RULE (NON-NEGOTIABLE)

```text
TRIGGER. If ANY route terminates in a CERTIFIED FINDING that the SHARP record
localizer M(t) is itself the obstruction — a certified-divergent E1 against
the sharp localizer — the gate STOPS AT THAT FINDING.

Certified findings that trigger this rule include, and are not limited to:
  - C-L3 returning a certified NONZERO sharp-kink log coefficient;
  - B-L2* returning a certified FAILURE on the record vertex, where the
    failure is CERTIFIED rather than merely uncertified;
  - any certified demonstration that no X_*(eps) exists for R-L0 BECAUSE of
    the sharp localizer;
  - any certified demonstration that the surviving sector's numerator is
    unsatisfiable at the sealed D6' definitions.

ON TRIGGER, IN THIS ORDER:
  1. STOP. No further obligation is attempted. No route is switched to. No
     repair is attempted. No bound is re-derived. No tolerance is revisited.
     *** THIS PROHIBITION DOES NOT EXTEND TO THE Z.2 (a)/(b)/(c) DECLARATION,
     WHICH IS MANDATORY AND IS PART OF THE FINDING, NOT FURTHER WORK. ***
  2. SEAL THE FINDING with its exact witness, its enclosures, its lineage,
     *** AND THE Z.2 (a)/(b)/(c) DECLARATION, WHICH IS AN EXPLICITLY SEALED
     CONTENT OF THE FINDING. *** A sealed finding without it is incomplete and
     BLOCKS.
  3. ESCALATE TO THE PRINCIPAL with ALL THREE OPTIONS (i), (ii), (iii) and
     their FULL COSTS, AND NO ARGUMENT FOR ANY OF THEM.

NO LANE MAY ANSWER Q2, PRE-EMPT IT, OR DESIGN AROUND IT SILENTLY. Selecting an
option, ranking the options, recommending one, implying one, continuing work
that presupposes one, or scoping a subsequent obligation so that only one
option remains available, BLOCKS with witness Q2_ANSWERED_BY_A_LANE.
*** NO COST BLOCK BELOW MAY ASSERT A Z.2 (a)/(b)/(c) GRADE, IN ADVANCE OR AT
ALL. The grade is classified by fresh-context hostile review. ***
```

### Option (i) — SHARP LOCALIZER INVIOLABLE: certified-divergent E1 stands as a refutation of the current activity architecture

```text
COSTS AND CONSEQUENCES (costs only; no comparative, no recommendation):
- T7(iii) clause (2) has NO certified majorant on any route. The verdict is a
  named REFUTATION rather than a named uncertainty.
- The re-scoped DERIVED arm (M1 + M2-certified + M3-activated over the full D3
  quantifier) becomes UNSATISFIABLE at the sealed M(t). The re-scope's own
  stated contingency ("contingent on an E1 architecture that does not yet
  exist") resolves NEGATIVELY. The SECOND contingency (Q6, in its recast form)
  is unaffected and remains open.
- Route T offers no fallback: O7 is refuted as a MECHANISM (3c81647e…) and the
  O3 TT-certificates are blocked by ordering.
- Downstream, all of the following remain FALSE and acquire a refutation-grade
  obstruction: connected_linked_cluster_density_proved,
  volume_uniform_zero_free_neighborhood_proved, T7(iv),
  Duhamel_intensive_Hessian_equality_proved, kappa_record_computed,
  alpha_computed, proof_authorized.
- The Duhamel consumer's I3 tuple V002 has NO SUPPLIER: no eps_*, no
  Gamma_star, no eta, hence no radius at which its (H1) per-K zero-freeness
  can be stated.
- SCOPE OF WHAT THE FINDING TOUCHES, STATED NEUTRALLY (replaces v001's "what
  is not refuted" clause, per C-11): *** WHICH OF Z.2 (a)/(b)/(c) THIS FINDING
  ESTABLISHES IS NOT DETERMINED BY THIS SPEC AND IS CLASSIFIED BY HOSTILE
  REVIEW. The cost of option (i) is stated separately under each of the three
  classifications: under (a) the defined quantity itself is implicated and the
  cost extends to the T7(i) object; under (b) a stated bound class is
  implicated and the cost extends only as far as that class's grounding
  principle, which must be named and lies UPSTREAM of the activity
  architecture (Z.2 as amended); under (c) nothing is excluded and the cost is
  that of further IR work only. *** No claim is made here that H-B, the T7(i)
  normalization, or any sealed result is untouched: R-L4a/R-L4b are OPEN, and
  under B-4 the baseline determinant's very existence is undetermined.
- WHAT THE FINDING SUPPLIES: an exact witness naming a MECHANISM (sharp record
  localizer at the VOLUME DIAGONAL against the marginal degree-(-3) sea)
  rather than a symptom.
```

### Option (ii) — SMOOTHED-LOCALIZER SUCCESSOR: a scoped DEFINITION change to what a record cell is

```text
COSTS AND CONSEQUENCES (costs only):
- IT CHANGES A SEALED PHASE-A A1 DEFINITION: M(t) = Q 1_{|x| <= r(t)} Q —
  hence what a RECORD CELL IS, hence what kappa_record measures, hence the
  meaning of the program's target. Axis-3-adjacent.
- IT REQUIRES: its own spec, its own hostile review, and an EXPLICIT
  STATEMENT OF EVERY SEALED RESULT IT TOUCHES. Candidate enumeration, offered
  as a starting point and NOT claimed complete: Phase-A A1/A2/A3/A4
  (789338ad…); the Phase-A execution binding; the state-regulator restriction
  result (3a6ff617…) insofar as C_n = Q_n C Q_n is used; relay necessity
  (0df721a1…) and relayed-family resolution (52401eef…) insofar as cell
  closure at full tau_R uses M(t); the tau_R = pi/sqrt2 derivation
  (b786db3a…) — whether tau_R remains the UNIQUE controlled coupling once
  v(t)M(t) is smoothed; the envelope-realization comparison spec (4059eff5…)
  and the whole ER-A/ER-B fork; the connected analytic closure result
  (f891d3af…) and its GHZ witness; the L2 typing freeze (cdbacdaf…); NC1's
  and NC5's exact witnesses; the O7 obstruction record (3c81647e…), whose
  exact witnesses depend on int_0^1 v = tau_R holding ON THE BALL WHERE M = 1;
  and C4/C6 themselves, both of which are statements ABOUT the sharp localizer.
- SPECIFIC MATHEMATICAL COST: the exact record-phase collapse (+1,-1,-1) at
  lambda tau_R in {0, +-pi} is EXACT only where M(t) = 1. Smoothing creates a
  transition region where the phase is not +-1. Therefore C4's exactly
  saturated l1 step becomes an inequality OF UNKNOWN DIRECTION; the exact
  Phase-2 route-(b) witness becomes approximate; R.2's same-phase collapse
  V(0) = I and the sector-vanishing obligation R-L4b no longer apply as
  written; the O7 record's exact witnesses become approximate; exact
  arithmetic in Q(sqrt2) may no longer suffice.
- SPECIFIC DIAGNOSTIC COST, SHARPENED BY THE C6 LOCUS REFINEMENT: the fatal
  local integral is at the VOLUME DIAGONAL x = y, not the sharp boundary, and
  SMOOTHING ONLY THE BOUNDARY WILL NOT REMOVE A |x-y|^-3 POSITIVE MAJORANT.
  Even a LIPSCHITZ cutoff gives int d^3 r · r^2/r^6 = int dr/r^2, divergent.
  *** A SMOOTHED-LOCALIZER SUCCESSOR MAY THEREFORE NOT FIX THE OBSTRUCTION AT
  ALL. *** The required smoothness class, and whether any localizer smoothing
  reaches the diagonal, are unknown until NC9's diagnostic is read, and NC9 is
  diagnostic only.
- IT DOES NOT TRIGGER F'-1: no clustering axiom is involved.
- POSSIBLE GAIN: if a sufficient class exists and reaches the diagonal,
  [C, M] becomes Hilbert-Schmidt, the cell-level Shale-Stinespring condition
  holds, B-L2* closes, and E1 is certified — which would deliver clause (2)
  over the full D3 quantifier via Route Q, subject to the recast Q6 and to
  A-L0/A-L5.
- COST OF THE DECISION ITSELF: the front stops until the principal decides.
```

### Option (iii) — DERIVE the spatial localizer profile from sealed principles (ORDERED BEFORE (ii))

```text
*** ORDERING, FROM THE SEALED STANDARD: IF Q2 TRIGGERS, (iii) IS EVALUATED
BEFORE (ii) MAY BE ADOPTED. (i) REMAINS AVAILABLE THROUGHOUT. A DERIVATION
ATTEMPT THAT FAILS IS A RECORDED RESULT, NOT A DEFEAT — IT CLEANLY LICENSES
(ii) AS AN HONESTLY DISCLOSED DECISION. ***
SCOPE. The TEMPORAL write profile was DERIVED: the diamond-marginal pulse
w(s) = 32(1/2 - |s - 1/2|)^3, identical to 32 min(t,1-t)^3, with
int_0^1 32 min(t,1-t)^3 dt = 1 exactly (re-verified). The SPATIAL localizer
M(t) = Q 1_{|x| <= r(t)} Q was POSTULATED sharp. Option (iii) asks whether the
sealed principles force a spatial profile at all.
COSTS (costs only; no argument for or against, and no prediction of the tier):
- WHAT A DERIVATION ATTEMPT WOULD CONSUME: a scoped derivation spec and its
  own hostile review; identification of which sealed principles could bear on
  a spatial profile (the diamond-marginal construction that derived w(s); the
  relay/causal-exhaustion geometry; the unique-controlled-coupling derivation
  of tau_R; the monoidality and envelope-class constraints); and an explicit
  statement of which of those principles REQUIRE versus merely ALLOW a
  profile, under the program's own verb calibration.
- WHAT IT DOES NOT CONSUME: no Phase-A/B production output; no change to any
  sealed definition while the attempt runs.
- WHAT A FAILED ATTEMPT COSTS: the elapsed front-stop, plus a recorded
  negative result. IT IS NOT A DEFEAT AND IT LICENSES (ii).
- WHAT A SUCCESSFUL ATTEMPT COSTS: the tier is assigned by content under
  hostile review (Z.3) and the cost differs by tier — Tier 1 dissolves Q2 with
  no conditionality; Tier 2 requires the DERIVED EXCLUSION and the SELECTION
  to be recorded as TWO SEPARATE THINGS, with the residual classified by Z.4;
  Tier 3 collapses into option (ii) with full conditionality on every headline
  downstream of kappa_record. NO LANE MAY CLAIM ITS OWN TIER.
- INTERACTION WITH THE C6 LOCUS REFINEMENT, stated as a cost and not as an
  argument: because the fatal integral is at the volume diagonal, a derived
  profile that is smooth only at the boundary would not by itself remove the
  obstruction, so a Tier-1/Tier-2 outcome does not automatically discharge E1.
```

---

## §Z — THE PRINCIPAL'S Q2 STANDARD (governing; `38e15177…`)

```text
*** WHERE THIS SECTION'S PARAPHRASE AND THE SEALED STANDARD (38e15177…)
DIFFER IN ANY RESPECT, THE SEALED TEXT GOVERNS. *** (C-12.) The standard was
pre-registered before any IR route terminated and governs this spec and
supersedes any narrower Q2 language elsewhere in this text. Disclosure of
record retained: §Z's predecessor was authored at seal by a lane inside the
spec's own production chain; this v002 restates it as the drafting lane's
text, subordinated to the sealed original, and the hostile reviewer is asked
to re-check it against 38e15177… directly.
```

### Z.1 Option (iii) exists and is ordered before (ii)

```text
(i) sharp localizer inviolable; (ii) smoothed-localizer successor by decision;
(iii) DERIVE the spatial localizer profile from sealed principles — the
treatment the TEMPORAL write profile already received (w(s) = 32(1/2-|s-1/2|)^3
was DERIVED, not chosen), while the spatial M(t) was POSTULATED sharp.
ORDERING: if Q2 triggers, (iii) is evaluated BEFORE (ii) may be adopted;
(i) remains available throughout. A FAILED DERIVATION ATTEMPT IS A RECORDED
RESULT, NOT A DEFEAT, and cleanly licenses (ii) as an honestly disclosed
decision. Wired into §Q2-STOP step 3 and into the option-(iii) cost block.
```

### Z.2 Object-vs-bound tripwire (MANDATORY on any certified-divergent arm; BLOCK on omission)

```text
A DIVERGENT MAJORANT IS NOT A DIVERGENT THEORY. E1 certifying divergent
against the sharp localizer establishes that a BOUND ARCHITECTURE fails there
— NOT that the completed amplitude or its Hessian is ill-defined there.
Any artifact of this program that would EXCLUDE the sharp localizer MUST state
explicitly which of these it establishes:
  (a) the DEFINED QUANTITY ITSELF (the completed amplitude / its a = 0
      Hessian) is divergent or ill-defined under the sharp localizer —
      require-grade; or
  (b) only that every bound of a STATED CLASS fails — require-grade ONLY IF
      the finiteness demanded is itself a sealed principle rather than a
      convenience of the proof; or
  (c) only that the CURRENT architecture's bound fails — which EXCLUDES
      NOTHING and licenses only further IR work.
Excluding the sharp localizer BECAUSE IT RESISTS PROOF, absent (a) or a
principled (b), is SELECTING FOR PROVABILITY: route-shopping at the definition
level. *** ANY ROUTE RETURN OMITTING THE (a)/(b)/(c) DECLARATION BLOCKS. NO
CERTIFIED-DIVERGENT ARM MAY BE REPORTED WITHOUT IT. THE DECLARATION IS A
SEALED CONTENT OF THE FINDING (§Q2-STOP step 2) AND §Q2-STOP step 1's
PROHIBITION DOES NOT EXTEND TO IT. ***

*** C-9 AMENDMENT, BINDING AND APPENDED HERE VERBATIM IN SUBSTANCE: D5,
Kotecky-Preiss convergence, action-density form, and EVERY OTHER REQUIREMENT
INTERNAL TO THE MAJORANT/ACTIVITY ARCHITECTURE ARE *CONVENIENCES OF THE PROOF*
FOR THE PURPOSES OF (b) AND MAY NOT BE CITED AS THE SEALED PRINCIPLE GROUNDING
A REQUIRE-GRADE (b). This includes D5's own heading language ("REQUIREMENT,
not a convenience"), which is a statement about the architecture's internal
necessity and NOT a sealed principle upstream of it. A require-grade (b) MUST
NAME A PRINCIPLE UPSTREAM OF THE ACTIVITY ARCHITECTURE (definitional /
Axis-level). WHICH PRINCIPLE IS INVOKED, AND ITS GRADE, IS CLASSIFIED BY
FRESH-CONTEXT HOSTILE REVIEW, NEVER BY THE RETURNING LANE. ***
Witness on omission or on a self-classified grade: Q2_TRIPWIRE_DECLARATION_ABSENT.
```

### Z.3 Tier classification is NOT this spec's to claim (uniqueness and T5b restored)

```text
TIER 1 — FORCED PROFILE. Sealed principles force the spatial profile
  *** UNIQUELY (UP TO SEALED CONVENTIONS), COMPETITORS EXCLUDED — the standard
  the temporal pulse met. *** Then the "definition change" is a THEOREM, Q2
  dissolves, and NO conditionality attaches.
TIER 2 — FORCED EXCLUSION, ALLOWED FAMILY. The principles exclude the sharp
  member but permit a family. MUST be recorded as TWO SEPARATE THINGS — a
  DERIVED EXCLUSION plus a SELECTION — never blurred into one "DERIVED" (the
  ER-B failure class; *** THE T5b BUCKET RULE: excluded-by-theorem is never
  conflated with excluded-by-postulate ***). The residual selection is
  classified by Z.4.
TIER 3 — NOTHING FORCED. Option (iii) collapses into option (ii): a definition
  decision, labeled as such, carrying conditionality on every headline
  downstream of kappa_record, recorded in the same cumulative-conditionality
  register as the ER-A premise and the complex-vs-real selection.
THE TIER IS ASSIGNED BY CONTENT UNDER HOSTILE REVIEW — THE AUTHORING LANE
PROPOSES, A FRESH-CONTEXT REVIEW CLASSIFIES. NO LANE MAY CLAIM ITS OWN TIER,
and no execution of this spec may assign one.
```

### Z.4 Tier-2 residual: the record-invariance criterion, WITH its scope limit

```text
GAUGE:   if every record-level output (kappa_record and every quantity on its
         chain) is PROVABLY INVARIANT across the allowed family, the member
         choice is a redundancy of description and NO conditionality attaches.
         The invariance must be established AT THE OPERATOR LEVEL as an exact
         result — THE GAMMA STANDARD APPLIES VERBATIM: a numerical coincidence
         across sampled members is NOT the theorem and may not be labeled as
         one.
PREMISE: if any record-level output distinguishes members — OR INVARIANCE
         CANNOT BE PROVEN — the selection is a DISCLOSED PREMISE with full
         conditionality, alongside ER-A and complex-vs-real in the cumulative
         register.
*** SCOPE LIMIT, reproduced in full because it is binding on every lane: this
criterion is adopted as a CLASSIFICATION RULE FOR Q2's RESIDUAL ONLY. It is
deliberately NOT sealed as a physical principle. Its motivating idea — that
the theory's own allow/require boundary is drawn by record-distinguishability
— is a structural observation about the program; if it is ever to carry weight
beyond this classification rule it must earn its own derivation under its own
spec. NEITHER THE SEALED ADDENDUM NOR THIS PARAPHRASE MAY BE CITED AS
AUTHORITY FOR THAT IDEA ANYWHERE ELSE. ***
```

### Z.5 STOP rule

```text
If ANY route of this spec terminates in a certified finding that the sharp
record localizer M(t) is itself the obstruction, EXECUTION STOPS AT THAT
FINDING. The finding is sealed — with its Z.2 declaration — and escalated to
the principal with options (i), (ii), (iii) and their FULL COSTS stated, and
WITH NO ARGUMENT FOR ANY OF THEM. No lane may answer Q2, pre-empt it, or
design around it silently. Witness: Q2_ANSWERED_BY_A_LANE.
```

### Z.6 Second contingency of record

```text
This spec owns E1 only, and discharging every obligation here does not by
itself deliver the Route-Q predicate. *** CORRECTED FROM v001 (B-6): the
further claim that Q6 is "NOT absorbed by any route below" WAS FALSE for IR-A
as specified — IR-A silently consumed a D3-uniform cluster/shell count. ***
Under this v002: A-L3/A-L4 are scoped to the cubic skeleton and family A;
Q6's RAW-DEGREE form is CLOSED FALSE on full D3; Q6 survives only in its
RE-CAST weighted/subdivision-insensitive form, live under reading B alone; and
the D3-uniform anchored-sum obligation is A-L5, owned here and named as a
blocker (E1_ANCHORED_SUM_NOT_D3_UNIFORM). Route Q carries the full D3
quantifier alone contingent on BOTH a successor E1 architecture AND the recast
Q6 under whichever reading is pursued.
```

---

## §F' — ABSOLUTE FENCE 2 and the fence register

```text
F'-1  CLUSTERING-ADOPTION FENCE (ABSOLUTE; the principal's flag (a), standing
      REFUSAL, from parent F-1). If any route, lemma, obligation, control,
      repair, enclosure, or artifact of this program reaches for
      BUFFERED_EXHAUSTION_CLUSTERING or ANY clustering axiom or principle
      whatsoever, the gate BLOCKS IMMEDIATELY and escalates. Adoption is
      principal-only. No lane may adopt to rescue any route.
      Witness: CLUSTERING_ADOPTION_REACHED.
      *** C-14 REPAIR: v001's rationale — that a reach is "evidence that the
      reaching obligation has been MIS-DERIVED", and the instruction that the
      escalation "must say so" — IS STRICKEN. It rested on C5's margin claim,
      which B-1 and B-6 undercut. If the one-line connected term is real
      (A-L0 open) or the shell counts are not D3-uniform (A-L5 open), a reach
      for clustering may be evidence of a GENUINE NEED, and the escalation
      artifact must be neutral on that question and state both possibilities.
      The fence's operative clauses are UNCHANGED and absolute. ***
F'-2  Q2 STOP RULE per §Q2-STOP and §Z.5. Absolute.
F'-3  NAMED HYPOTHESES MAY NOT BE SILENTLY VALUED. H-B, H-B0, H-R, H-Z0 are
      undischarged. Assigning any a numeric value, a default (including 1), or
      an "assume for now" placeholder inside a certified bound BLOCKS with
      NAMED_HYPOTHESIS_SILENTLY_DISCHARGED. They may be carried as DISCLOSED
      PREMISES on a conditional statement, clearly marked. *** THE ONLY
      PERMITTED FORM OF PREMISE-CARRYING IN A THRESHOLD COMPARISON IS §E1'
      STEP 2's CONDITIONAL CERTIFICATION with the disclosed-premise symbol
      rho_bar and its stated admissible range (B-7). Any other
      premise-carrying comparison BLOCKS. ***
F'-4  eps_*, eta_1, eta_{>=2}, Gamma_star^split, rho_bar per §E1' ONLY; never
      tuned by any output. No measured constants anywhere. §N binds.
F'-5  SPEC-HEADER SCOPING CLAUSE 1 BINDS VERBATIM. Every constant, radius,
      decay rate and tolerance is an explicit functional of (||b_D||, tau_R,
      sea-kernel decay data, |w_lambda|) ONLY. No carrier index n, no ell, no
      truncation level, no cellulation-family index, AND NO CELLULATION
      GEOMETRIC DATUM. The SUPREMUM OVER ADMITTED CELLS is the ENFORCEMENT
      MECHANISM of this clause (CR.R5), not a definitional convenience — which
      is why R-L0 is a real obligation and not a formality. Violation BLOCKS.
      *** A-L3/A-L4's cubic shell counts ARE cellulation geometric data and
      are admitted ONLY inside the explicitly family-A-scoped statements of
      §O.A; using them in a D3-uniform claim BLOCKS with
      E1_SHELL_COUNT_NOT_UNIFORM_OVER_D3. ***
F'-6  ENVELOPE-PROFILE CLASS. The statement is over the sealed class
      containing both branches (v_A(t) = tau_R·32 r(t)^3; v_B = 24 tau_R/pi).
      ER-A is a DISCLOSED PREMISE on any downstream consumer; this program
      neither selects nor closes the ER fork.
F'-7  L2 FREEZE FENCES 1-5 BIND VERBATIM (parent F-3, extended by M-6).
F'-8  COMPANION-OBJECT FENCE (parent F-6). The exhaustive closure
      Z_K = omega_in(W_-^dagger W_+) is COMPANION ONLY; it appears here solely
      inside NC1/NC2/NC5. Substitution in EITHER direction blocks.
F'-9  NO-TARGET FENCE per NC7 including the C-16 appendix. VERDICT AUTHORITY
      RESTS WITH THE HASHED EVALUATOR ALONE (parent F-5).
F'-10 DEPENDENCY / INTERFACE. This program needs NO Phase-A/B production
      output; every input is a sealed DEFINITION. (i) The absence of the
      Phase-A bundle costs this work nothing and could not help it — any bound
      on the n = 2, ell in {1, sqrt2} carriers is carrier-indexed and
      forbidden by F'-5; the TT2 ordering blocks belong to O3 (Route T) and
      must not be conflated with E1. (ii) F-7's demotion clause DOES NOT APPLY
      — this work is a statement about the abstract sealed form.
F'-11 NO PRODUCTION-LANE INVOCATION. This program invokes no production lane
      and writes no production artifact. Sealed and production files are
      READ-ONLY to every lane, and the canonical stage8_execution/work and
      provenance directories are NOT to be chmod'ed by any lane; all fixture
      work happens in disposable copies under lane scratch.
F'-12 F-8 IS THE GATE, per the re-scope. Fresh-context execution from the
      sealed text; hostile PRE-EXECUTION review of this spec; and an
      INDEPENDENT fresh lane re-derives the SCAD constants, the A-L3/A-L0.2
      enclosures, the R-L4 bookkeeping and the W1 enclosure from the sealed
      text WITHOUT the primary's worksheets before anything seals. RECORDED
      HONESTLY: F8_gate_discharged = FALSE and CANNOT close before Phase-A
      executes (clause (3) sequencing, 65a7b799… erratum 2); the earlier
      "first half discharged" flag was an over-promotion and is corrected of
      record to two narrow reproductions.
F'-13 NO ROUTE-T ARTIFACT IN THE PREDICATE, per NC4-as-fence and the re-scope.
F'-14 THE MEMO IS A ROUTE MEMO, NOT AN AUTHORITY FOR ITS OWN CONSTANTS. Where
      this spec records a correction to the memo (A-L1's spinor factor; the
      IR-B per-pair-versus-summed display; and now the memo's two-line/R^-6
      frame, REFUTED at 65a7b799…), the CORRECTED form governs and the
      execution must certify the convention rather than inherit it.
      Witness: MEMO_CONSTANT_INHERITED_WITHOUT_CERTIFICATION
F'-15 *** NEW (C-15): NO DIFFERENTIATED-SERIES SUPPLY. *** This program
      supplies no bound on the DIFFERENTIATED cluster series. SCAD bounds
      Phi_C only; no a-derivative versions of S1/S2/S2b or of R.3 exist.
      Parent O5 (and M-10's consumption of eps_* by it) REMAINS UNSUPPLIED and
      MAY NOT BE INFERRED from anything in this program — the parent's own O5
      states that convergence of the undifferentiated series does not imply it
      "and may not be cited for it". Violation BLOCKS with witness
      O5_DIFFERENTIATED_SERIES_INFERRED_FROM_UNDIFFERENTIATED.
F'-16 *** NEW: SINGLE-REPORT RULE FOR THE COMMON WALL *** per §O.X.
      Witness: COMMON_WALL_REPORTED_MULTIPLY

F-TO-F' MAPPING TABLE (N-18; the v001 claim "F-1..F-8 carried as F'-1..F'-13"
was inaccurate and the list did not run to F'-13):
      parent F-1  ->  F'-1 (strengthened; rationale struck per C-14)
      parent F-2  ->  *** NO F' COUNTERPART. *** F-2 (O7 failure handled ONLY
                      by T7III_SCOPE_RESTRICTED_ESCALATE; never a silent
                      pinning, never a lemma-shaped restriction) is retired by
                      the majorant-arm re-scope, which removes O7 from the
                      DERIVED arm's predicate. ITS SUBSTANCE SURVIVES in §X
                      ("does not pin the D3 quantifier to any finite list,
                      under any outcome") and in D3's freeze. Nothing is lost;
                      the mapping is recorded rather than implied.
      parent F-3  ->  F'-7        parent F-4  ->  F'-4
      parent F-5  ->  F'-9        parent F-6  ->  F'-8
      parent F-7  ->  F'-10       parent F-8  ->  F'-12
      ADDED BY THIS PROGRAM: F'-2, F'-3, F'-5, F'-6, F'-11, F'-13, F'-14,
      F'-15, F'-16. The list runs to F'-16.
```

---

## §N — Frozen Numerics (implementation, binding)

```text
- Exact arithmetic decides: exact rationals (Fractions), exact symbolic
  arithmetic, exact Q(sqrt2) for the record-colour algebra. Certified OUTWARD
  interval enclosures over exact rationals for every transcendental bound (pi,
  e, exp, log, zeta values). FLOATS MAY INFORM ONLY and may never appear in a
  verdict-bearing enclosure, a threshold comparison, or a control pass/fail.
- Pinned runtime:
  /Users/bgm/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3
  No scipy. No numpy for any verdict-bearing quantity. Any matrix exponential
  must be a SELF-WRITTEN scaling-and-squaring implementation with a CERTIFIED
  OUTWARD REMAINDER ENCLOSURE; a float expm is diagnostic only and must be
  labelled as such.
- Every implementation is named and content-hashed at sealing; the evaluator is
  hashed and holds sole verdict authority (F'-9).
- Tail enclosures: every infinite sum (A-L3's zeta sums, A-L0.2's collar sum,
  NC3's and NC8's partial sums) is an exact rational partial sum PLUS a
  certified outward tail bound. No extrapolated, fitted, or floating tail.
- Zeta dependence stated honestly: 24 zeta(4) + 2 zeta(6) = 4 pi^4/15 +
  2 pi^6/945 and 24 zeta(2) + 2 zeta(4) = 4 pi^2 + pi^4/45 have closed forms;
  64 zeta(3) + 16 zeta(5) and 16 zeta(3) do NOT and are certified by enclosure
  only. The artifact must say which is which. A closed form is not a
  substitute for an enclosure.
- FIXTURE DISCIPLINE: no execution lane writes to the canonical root; the
  fence is live (stage8_execution/work and provenance are mode 555 at rest and
  are NOT to be chmod'ed). All fixture and rehearsal work happens in
  disposable copies under lane scratch. No production invocation against the
  canonical root under any verdict arm.
```

---

## §V — Predeclared verdicts (frozen; not revisable)

```text
E1S_REPLACEMENT_ARCHITECTURE_CERTIFIED
    iff R-L0 (or R-L0b) and R-L1, R-L2, R-L2b, R-L3, R-L4a, R-L4b, R-L4, R-L5
    discharge; AND A-L0 (arm 2, BOTH Huygens factors) closes; AND A-L5 closes;
    AND at least one of {IR-B closing n = 1 via B-L2*, IR-C closing n = 1 with
    a certified ZERO log coefficient} closes; AND eta_1, eta_{>=2} are
    certified at the §E1' thresholds with Gamma_star^split <= 1; AND ALL
    controls NC1-NC11 behave; AND W1 is computed and inside its comparator;
    AND §Q2-STOP is not triggered
    => E1 supplied into the parent's O4-M2, per state, under H-B, H-B0, H-R,
       H-Z0 as disclosed premises and with eps_*^{(1)}'s rho_bar
       premise-conditionality marked; the re-scoped DERIVED arm's E1
       dependency is met subject to F'-12, and the arm's SECOND contingency
       (recast Q6) remains open and unaffected.
    *** MANDATORY VERDICT-SECTION STATEMENTS, none of which may be relegated
    to a footnote:
      (1) SCAD IS NOT AN INDEPENDENT ROUTE — after the B-2 repair every
          surviving constant rests on C-L2, so SCAD is IR-C's wall
          re-expressed (§R.6), and B-L2* is the single crux at which
          IR-B/Codex-Route-1 and IR-C/Codex-Route-3 triangulate (§O.X).
      (2) READING A IS COMPELLED, NOT CHOSEN, and its burden SITS ENTIRELY ON
          M2 — which is this spec's own open obligation. Q6's raw-degree form
          is CLOSED FALSE; the recast form is retained for reading B.
      (3) NEITHER HUYGENS FACTOR ALONE SUFFICES for A-L0.
      (4) O6's density-EQUALITY clause is NOT forced by R1-R4 and is not
          discharged here (§O.O6').  ***

E1S_TWO_LINE_SECTOR_CERTIFIED_CROSS_TERM_AND_N1_OPEN
    (renames and REPLACES v001's E1S_N_GE_2_CERTIFIED_BLOCK_ISOLATED_TO_N1,
    which was FALSE-POSITIVE-CAPABLE per B-1)
    iff A-L1..A-L4 close ON THE TWO-LINE SECTOR AND THE CUBIC SKELETON /
    FAMILY A, with eta_{>=2} certified in that scope, but A-L0 does not close,
    or A-L5 does not close, or the n = 1 leg does not close; and §Q2-STOP is
    not triggered
    => the TWO-LINE-SECTOR anchored sums stand certified with the exact
       constants, IN THAT SCOPE AND NO OTHER. *** NO VERDICT UNDER THIS ARM
       MAY ASSERT THAT "the n >= 2 sums are certified", THAT THE PAIR ACTIVITY
       CARRIES R^-6, THAT THE LONG-DISTANCE DIRECTION HAS MARGIN, OR THAT
       CLUSTERING WAS NEVER THE MISSING INGREDIENT. Such wording is a spec
       violation and BLOCKS with witness N_GE_2_CERTIFIED_ASSERTED_BEFORE_A_L0. ***
       Residue: E1_SEA_KERNEL_ACTION_DENSITY_UNCERTIFIED restricted as stated,
       PLUS E1_ONE_LINE_CONNECTED_CROSS_TERM_UNCERTIFIED, PLUS
       E1_ANCHORED_SUM_NOT_D3_UNIFORM, PLUS (if the n = 1 leg is the residue)
       E1_SHARP_RECORD_LOCALIZER_VS_MARGINAL_SEA at the VOLUME DIAGONAL.
       eta_1 remains REQUIRED (D5'); nothing is released.

E1S_CERTIFIED_DIVERGENT_AT_SHARP_LOCALIZER
    on any §Q2-STOP trigger
    => STOP, SEAL (INCLUDING THE Z.2 (a)/(b)/(c) DECLARATION), ESCALATE per
       §Q2-STOP with ALL THREE OPTIONS, FULL COSTS, AND NO ARGUMENT FOR ANY.
       Not a block and not a derivation: a REFUTATION with an exact witness,
       terminating the program pending the principal's decision. The Z.2 grade
       is NOT asserted by this spec or by the returning lane.

E1S_BLOCKED
    on any other obligation failure, control misbehaviour, authority drift,
    EPSILON_STAR_VACUOUS_{n1|nge2}, R-L0 failure, A-L0 failure, A-L5 failure,
    or any spec violation named in §F' — ALWAYS with a named witness.
    Failures preserved, never repaired.

E1S_CLUSTERING_REACH_BLOCK
    on any F'-1 trigger => immediate block and escalation, with the
    escalation NEUTRAL as to whether the reach indicates a mis-derivation or a
    genuine need (C-14).
```

---

## §G — Graceful-block witness table (comparatives struck per C-11)

```text
| route fails                     | named witness                                        | honest partial result that survives                                                                                                                                     |
|---------------------------------|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A-L0 (one-line cross term)      | E1_ONE_LINE_CONNECTED_CROSS_TERM_UNCERTIFIED         | The cumulant's exact two-term structure is on the record with an exact rational witness; the obligation is localized to the one-line sector's propagation bridge.          |
| A-L0 one factor only            | A_L0_HUYGENS_BOUND_ONE_FACTOR_ONLY                   | Whichever factor was certified is recorded; the arithmetic showing that either alone leaves R^-1 (divergent) is exact and reusable.                                       |
| A-L5 (D3 uniformity)            | E1_ANCHORED_SUM_NOT_D3_UNIFORM                       | The family-A constants stand IN THAT SCOPE; the residual is a subdivision-insensitivity obligation, and the raw-degree route to it is closed-false (a result).            |
| IR-A (light cone)               | E1_NULL_SEPARATION_CLUSTER_DECAY_UNCERTIFIED         | Spacelike-separated TWO-LINE-SECTOR sums certified with 24 zeta(4)+2 zeta(6) / 64 zeta(3)+16 zeta(5), ON THE CUBIC SKELETON AND FAMILY A; the obligation narrows to null-separated cell chains AND to the family-B / common-refinement gap. |
| IR-A (shell counts not uniform) | E1_SHELL_COUNT_NOT_UNIFORM_OVER_D3                   | The constants are exact where they hold; the scope is named rather than assumed.                                                                                          |
| B-L2* (the common wall)         | E1_SEA_OFFDIAGONAL_HS_SHARP_RECORD_LOCALIZER         | The a-VERTEX SECTOR (Gevrey b_D) is certified carrier-uniformly; the block is confined to the sharp M(t) at the VOLUME DIAGONAL — a definition-level, not a clustering-level, obstruction. REPORTED ONCE (F'-16). |
| IR-B (trace part)               | E1_SUBLEADING_SEA_TRACE_LOG_UNCERTIFIED              | The leading sea-depth divergence certified to cancel exactly; only the subleading log remains.                                                                            |
| IR-C (commutator)               | E1_RECORD_KINK_COMMUTATOR_FORM_UNCERTIFIED           | Exact record-phase collapse certified; the error isolated in ONE named commutator — which is also S2b, hence also SCAD's dependency.                                      |
| IR-C (coefficient nonzero)      | E1_RECORD_KINK_LOG_COEFFICIENT_NONZERO_CERTIFIED     | A REFUTATION, NOT A BLOCK: E1 unsatisfiable at the sealed M(t). Escalates via §Q2-STOP with all three options. WHICH OF Z.2 (a)/(b)/(c) IT ESTABLISHES IS NOT DETERMINED HERE. |
| R-L0 (scale normalization)      | E1_CELL_SCALE_NORMALIZATION_UNCERTIFIED              | SCAD stands as the cancellation-first replacement for the divergent K_sea; what is uncertified narrows to ONE scalar bound X_*(eps) — or is bypassed entirely if R-L0b closes — with the full-tau_R-per-cell hazard named as its cause (the O7 root). |
| R-L2b (scaling exponent)        | SCAD_HS_SCALING_EXPONENT_UNDERIVED                   | The Carleman machinery and the subtraction stand; what is open is the exponent that makes the bookkeeping mean something.                                                 |
| R-L4a / R-L4b (baseline)        | E1_BASELINE_DETERMINANT_EXISTENCE_UNCERTIFIED / E1_OPPOSITE_PHASE_SECTOR_VANISHING_UNCERTIFIED | The exact weight bookkeeping and the finite-trial identity stand as REPORTED items; what is open is whether the baseline determinant exists at all and under which regularization. H-B is not touched either way. |
| C-L5 (multi-cell baseline)      | E1_MULTICELL_BASELINE_EXTENSION_UNCERTIFIED          | The single-cell statement stands, explicitly scoped to one cell and one state; H-B remains named and undischarged on multi-cell complexes.                                |
| A-L1 conventions unpinned       | A_L1_SPINOR_TRACE_CONVENTION_UNPINNED / A_L1_VOLUME_TYPING_UNPINNED | The kernel is exact and the HS pairing is the right tool; a factor-4 spinor convention (independently confirmed to favour the conservative constant) and an equal-time-vs-spacetime typing remain, both decidable by inspection. |
| NC3 silent                      | ONE_LINE_SECTOR_DETECTOR_NOT_EXECUTABLE              | C3' stands as a correction of record; what fails is the detector's encoding.                                                                                              |
| NC8 not executable              | ONE_LINE_TWO_LINE_SECTOR_CONTROL_NOT_EXECUTABLE      | Both sectors are exhibited arithmetically in this spec; what fails is the two-sector encoding.                                                                            |
| all fail                        | retain E1_SEA_KERNEL_ACTION_DENSITY_UNCERTIFIED, ADD E1_SHARP_RECORD_LOCALIZER_VS_MARGINAL_SEA (locus: volume diagonal) | The MECHANISM is named rather than the symptom, and the common wall is named once. |
```

---

## §P — Frozen predictions (outcome-class FIRST; magnitudes honestly wide)

```text
CALIBRATION STATEMENT, MANDATORY, AND NAMED RATHER THAN GESTURED AT:
(1) THIS LANE'S MAGNITUDE / SCALING PREDICTIONS HAVE MISSED THREE TIMES
    CONSECUTIVELY. Two were genuine magnitude misses. The third (Control-4 v3
    S3(a): predicted central 1e-6 in a 1e-8..1e-4 window; measured null) was
    caused by a PINNED DIRECTION trace-orthogonal to the detector — a
    direction-pin defect, not a magnitude-model error; the same model on the
    supported direction gave 4.57e-6, POST HOC AND NOT CREDITED. The ledger's
    standing header still says TWICE; the spec says THREE and the spec is
    right (N-19).
(2) THE INDEPENDENT-SYSTEM PREDICTION FAMILY HAS LANDED TWICE CONSECUTIVELY —
    P-C5 (cross-term lemma: honest split, no universal zero identity,
    certification only via a propagation-bridge bound) and P-C6 (no uniform
    raw adjacency-degree bound on full D3, with an explicit star-refinement
    construction), with P-C3 holding. In both cycles its predictions held
    while this lane's magnitude AND ROUTE-SURVIVAL predictions did not.
(3) CONSEQUENCE, APPLIED AND NOT MERELY STATED: *** WHERE THIS LANE'S
    PREDICTIONS AND THE INDEPENDENT FAMILY'S DISAGREE, THE INDEPENDENT
    FAMILY'S ARE WEIGHTED HIGHER, AND THIS SPEC'S OVERALL PREDICTED OUTCOME IS
    CHANGED TO MATCH THEIRS (P-C1: E1S_BLOCKED) RATHER THAN v001's PREDICTION
    OF A CERTIFIED n >= 2 SECTOR. *** This lane's own SIGN / DIRECTION /
    OUTCOME-CLASS register remains its stronger one (the O7 block prediction
    landed exactly on its predicted obligation with an exact refuting witness),
    so outcome-class predictions are stated first. Magnitude windows are
    DELIBERATELY WIDENED and the reason is NAMED in each; a magnitude
    prediction landing inside them should be credited WEAKLY. Not revisable
    after seal.
(4) THIS LANE'S OWN DEFECT LEDGER IS PART OF THE CALIBRATION: the structural
    defects (C3/C5; A-L0 sealed with an already-dead arm) were caught only by
    lanes that re-derived from scratch or probed a route this lane had not.
    That is the argument for F'-12's independent re-derivation being permanent.
```

### Route ranking (frozen)

```text
IR-C  FIRST FOR EXPECTED INFORMATION YIELD — the only route that returns
      information under failure (a certified nonzero log coefficient converts
      "uncertified" into "certified divergent with an exact witness"), and,
      per §R.6, the route on which SCAD's surviving constants actually rest.
IR-A  SECOND, AND DOWNGRADED FROM v001's FIRST. Its two-line-sector leg rests
      on exact constants but is SCOPED to family A, and the one-line sector
      (A-L0) plus D3-uniformity (A-L5) are both open. v001 ranked it first for
      certification yield on the strength of the refuted C5; that ranking is
      withdrawn.
IR-B  THIRD. Its a-vertex sector is likely certifiable and its record vertex
      is B-L2*, the common wall; its value is splitting the obligation into a
      certified sector and a named definition-level residue.
```

### Predictions

```text
PA-1  OUTCOME-CLASS. R-L1, R-L2, R-L3 discharge at the structural level.
      Confidence: high. Ground: the block-triangular reduction and the
      Carleman identities are structural.
PA-2  OUTCOME-CLASS. R-L0 does NOT close on ground (i), because tau_R is
      scale-invariant and every refined cell carries a full record cycle (the
      O7 root). Confidence: moderate-to-high, stated on the pessimistic side.
      SECONDARY: R-L0b (the exponentiation-free closure) is the more likely of
      the two to succeed, since the linear Carleman estimate already yields
      action-density form. Confidence: low-moderate — this is a NEW obligation
      this lane has not attempted.
PA-2b OUTCOME-CLASS. R-L2b returns alpha = 1/2 for the SUBTRACTED HS density
      (via cell time extent + Gevrey b_D) but the derivation is not
      trivial. Confidence: low-moderate. Stated because v001 asserted 1/2 with
      no derivation and was caught.
PA-3  OUTCOME-CLASS, RESTATED AS CONDITIONAL (B-4/N-20). CONDITIONAL ON R-L4a:
      the opposite-phase baseline determinant does NOT exist as an
      unregularized Fredholm determinant, and under the Carleman
      regularization det = det_2 · e^{tr} with tr = -infinity it VANISHES,
      giving R-L4b and hence kappa_bal = 1 as (1/2)/(1/2) from the surviving
      weights. Confidence: moderate. *** v001's "D = 0 exactly, therefore
      b_0 = 1/2 and kappa_bal = 1" was an INVALID LIMIT OF A BOUND and is
      withdrawn. This restatement predicts an EXISTENCE/REGULARIZATION
      outcome, not a value of a nonexistent object. ***
PA-4  OUTCOME-CLASS. H-R (rho_res) is NOT discharged by this program and is
      carried as the rho_bar disclosed premise. Confidence: high.
PA-5  OUTCOME-CLASS. No route reaches for a clustering axiom; F'-1 does not
      fire. Confidence: moderate — DOWNGRADED FROM v001's "high", because
      v001's ground was C5's margin claim, which is unproven. If A-L0's
      one-line sector proves genuinely non-summable, a reach becomes more
      tempting, and the fence, not a margin claim, is what holds.
PA-A0 OUTCOME-CLASS. A-L0 (arm 2) DOES NOT CLOSE in this program. Both
      Huygens factors are required and the amplitude factor (ii) — >= R^-1
      after cell-time integration — is the one with no sealed supplier.
      Confidence: moderate-high. THIS IS THE PREDICTION THAT DRIVES THE
      OVERALL OUTCOME, and it agrees with the independent family's P-C1/P-C4.
PA-A1 OUTCOME-CLASS. A-L1 and A-L3 CERTIFY *within their family-A scope*, with
      the exact constants delivered under certified outward enclosures.
      Confidence: high (exact partial sums re-verified).
PA-A2 OUTCOME-CLASS. A-L1's spinor-trace convention resolves in favour of the
      CONSERVATIVE 1/(pi^4 R^6). Confidence: high — UPGRADED, because the
      hostile reviewer independently re-derived ||alpha·r||_F^2 = 4|r|^2 and
      confirmed the factor 4. A direction prediction, not a magnitude.
PA-A5 OUTCOME-CLASS, RESTATED AS FUNCTIONAL FORM (N-20). eta_{>=2}(eps) =
      eps/sqrt2 EXACTLY on a ratio-2 grid, per A-L4's derived L-independent
      eta^2 = eps^2/2. Confidence: moderate-high. *** v001's PA-A5 (a
      1/64..1/2 window) was NEAR-UNFALSIFIABLE — its ceiling was the selection
      criterion itself — and is withdrawn. This form is falsifiable. ***
PA-A6 MAGNITUDE — WINDOW DELIBERATELY WIDE. eps_*^{(>=2)} lands on a dyadic
      grid point in 2^-1..2^-14, central band 2^-4..2^-8. REASON NAMED: three
      consecutive magnitude misses; eps_*^{(>=2)} depends multiplicatively on
      rho_res (H-R, no derived scale at all) and kappa_bal; and the A-L1
      factor-4 convention alone moves the answer by up to one grid point. A
      narrower window would be dishonest, not confident.
PA-A7 OUTCOME-CLASS. A-L5 does NOT close in this program. Confidence:
      moderate-high. Ground: the raw-degree route is closed false, reading B
      needs an unproven weighted counting theorem, and reading A moves the
      count inside M2 without supplying it.
PA-B1 OUTCOME-CLASS. B-L1 CERTIFIES; both exact cancellations hold.
      Confidence: high.
PA-B2 OUTCOME-CLASS. The a-VERTEX SECTOR of B-L2* CERTIFIES carrier-uniformly.
      Confidence: moderate-high.
PA-B3 OUTCOME-CLASS. THE RECORD VERTEX OF B-L2* IS THE WALL and does not
      certify. Confidence: high. Ground: C6 with the volume-diagonal locus,
      plus C4's promotion of P to the leading in-cell object.
PA-B4 OUTCOME-CLASS. Whether that failure is CERTIFIED (hence §Q2-STOP) or
      merely UNCERTIFIED (hence E1S_BLOCKED) is genuinely open; this lane
      predicts MERELY UNCERTIFIED for the two-time object — the equal-time
      failure is certified, the two-time failure is not. Confidence:
      low-moderate. STATED EXPLICITLY BECAUSE IT DETERMINES WHETHER Q2 FIRES.
      *** This prediction is informative in one direction only: it carries no
      weight and grants NO PERMISSION if it is wrong, and it must not be read
      as pre-empting Q2. ***
PA-C1 OUTCOME-CLASS. C-L1 CERTIFIES. Confidence: high.
PA-C2 OUTCOME-CLASS. C-L2 (commutator in quadratic form) IS THE BLOCK OF THIS
      ROUTE — and, per §R.6, of SCAD's surviving constants. Confidence:
      moderate-high. Ground: ||[h_0, 1_B]|| = infinity excludes norm control
      and no sealed authority supplies the correct quadratic form.
PA-C3 OUTCOME-CLASS. IF C-L2 is surmounted, C-L3's log coefficient is NONZERO.
      Confidence: moderate-high. Ground: the degree-(-3) kernel's absolute
      integral is logarithmic with derived coefficient exactly 2/pi at both
      ends and nothing in the sealed structure supplies a UV cancellation —
      C4 shows the one candidate is exactly saturated. *** IF THIS LANDS IT
      TRIGGERS §Q2-STOP. THIS LANE EXPRESSES NO PREFERENCE AMONG Q2's THREE
      OPTIONS AND ASSERTS NO Z.2 GRADE. ***
PA-C4 MAGNITUDE — WINDOW DELIBERATELY VERY WIDE, AND MARKED
      CONDITIONAL-AND-PROBABLY-UNTESTED (N-20). *** This prediction is gated
      behind PA-C2, which predicts the gate does not open, so the program's
      only sharp magnitude prediction will most likely NEVER BE TESTED, and
      that is recorded rather than hidden. *** If nonzero, the coefficient's
      modulus lies within four decades of 2/pi. REASON NAMED: three
      consecutive magnitude misses; the coefficient is a product of the
      derived 2/pi with UNDERIVED spinor-trace and record-colour group
      factors; and the most recent miss came from a pinned direction being
      orthogonal to the detector — the analogous hazard is that the leading
      spinor trace vanishes by parity (it does at first order), so the
      surviving coefficient may sit orders below the naive estimate.
      REPORTING: exact symbolic multiple of 2/pi only, never a decimal
      (NC7 / C-16).
PA-C5 OUTCOME-CLASS. C-L5 does NOT close; R-L4 is scoped to the single cell.
      Confidence: moderate.
PA-N1 OUTCOME-CLASS. NC1 refuses naming H-IND; NC2 and NC5 detectably fail
      with their exact M-5 witnesses; NC6 exhibits the D5 trap; NC7 finds no
      target-adjacent numeric. Confidence: high.
PA-N2 OUTCOME-CLASS. NC3 FIRES as a detector and NC8 is executable in both
      sectors, the one-line leg reproducing 24 H_K exactly and the two-line
      leg converging to the exact constants. Confidence: high (exact
      arithmetic this session).
PA-N3 OUTCOME-CLASS. NC10 and NC11 both behave: the unsubtracted variant
      diverges, and the reinstated G_bl diverges. Confidence: high — these are
      C2 and B-2 restated as controls.
PA-N4 OUTCOME-CLASS. NC9's diagnostic shows that a mollifier acting only on
      the localizer BOUNDARY does NOT restore Hilbert-Schmidt-ness, because
      the fatal integral is at the VOLUME DIAGONAL. Confidence: moderate-high
      — UPGRADED from v001 by the C6 locus refinement. REPORTED ONLY; grants
      no permission to smooth anything.
PA-N5 OUTCOME-CLASS. W1 is nonzero and inside its (two-line-sector, family-A)
      comparator in any arm that reaches it. Confidence: low-moderate —
      DOWNGRADED, because the comparator itself is now scoped and the one-line
      sector could put W1 outside it for a reason that is not a refutation.
```

### Overall predicted outcome (frozen)

```text
PREDICTED PROGRAM OUTCOME: *** E1S_BLOCKED ***, with the live blockers being
    E1_ONE_LINE_CONNECTED_CROSS_TERM_UNCERTIFIED (A-L0 arm 2), and
    E1_ANCHORED_SUM_NOT_D3_UNIFORM (A-L5),
alongside the retained E1_SEA_KERNEL_ACTION_DENSITY_UNCERTIFIED and, as an
independent block candidate, E1_CELL_SCALE_NORMALIZATION_UNCERTIFIED (R-L0).
THIS MATCHES THE INDEPENDENT-SYSTEM FAMILY'S P-C1 AND P-C2 AND OVERRIDES
v001's PREDICTION OF A CERTIFIED n >= 2 SECTOR, per the calibration weighting
above. Recorded plainly: v001's predicted outcome was FALSE-POSITIVE-CAPABLE
because it rested on the refuted C3/C5.
SECOND-MOST-LIKELY: E1S_TWO_LINE_SECTOR_CERTIFIED_CROSS_TERM_AND_N1_OPEN.
THIRD: E1S_CERTIFIED_DIVERGENT_AT_SHARP_LOCALIZER via C-L3, triggering
§Q2-STOP. THIS LANE EXPRESSES NO PREFERENCE AMONG Q2's THREE OPTIONS AND ITS
PREDICTION OF THIS OUTCOME IS NOT A DESIGN CHOICE.
LEAST LIKELY: E1S_REPLACEMENT_ARCHITECTURE_CERTIFIED.
This ordering errs toward blocks, per the standing calibration.
```

---

## §S — Scoped supersessions of the parent spec (complete list)

```text
S-1  D5 single eta -> D5' split (eta_1, eta_{>=2}) with the mandatory
     Gamma_star^split <= 1 clause. Scope: this spec's obligations only. The
     parent's D5 requirement — action-density form, per unit 4-volume,
     constants in the permitted tuple — is UNCHANGED and BINDING on both legs.
S-2  The parent's E1 rule steps 1-4 -> §E1' steps 1-7. The parent's dyadic
     grid and its 1/2 threshold are inherited UNCHANGED; the two-leg structure,
     the aggregate margin clause, and step 2's premise-conditional form for the
     n = 1 leg are added. No new number.
S-3  The parent's O4-M2 constant architecture (Phase-1 eta, K_sea, T_R, b_0) ->
     §R SCAD (G_tr, G_hs, G_cm, rho_res, kappa_bal, X_*). RETIREMENT, not
     amendment (C2). Enforced by F'-3, NC10 and NC11. *** G_bl is DELETED
     outright, not superseded. ***
S-4  The parent's O8 NC4 -> NC4-as-fence, per the re-scope.
S-5  The parent's O9 / M-1 comparator -> the same comparator read on
     eta_{>=2}, SCOPED to the two-line sector and family A.
S-6  The memo's A-L1 constant and its IR-B per-pair display -> corrected per
     F'-14; and the memo's two-line/R^-6 frame -> REFUTED per 65a7b799…. The
     memo remains the ROUTE authority only.
S-7  *** NEW: the parent's M3 "Kotecky-Preiss convergence at eta <= 1/2" line
     -> the SPECIFIED geometric-series line of §O.O6', under the compelled
     reading A. No KP test function is used and none may be introduced. ***
S-8  *** NEW: the parent's O6 clause (4)(i) density-EQUALITY claim -> the
     re-verbed (4)(i-a)/(4)(i-b) split of §O.O6'. This spec discharges
     neither; it prevents the parent's verb from being inherited unexamined. ***
S-9  *** NEW: the sealed O1 display -> read CTP-NESTED of record (D-O1, from
     f84c3036…). The interleaved reading is FALSE in general. ***
NOT SUPERSEDED, AND EXPLICITLY REAFFIRMED: D1, D2, D3 (with its frozen
standard reading), D4-as-M-2, M-3, M-4, M-7, M-8, M-11, O1, O2, R1-R4, the L2 typing freeze fences 1-5, and the T7(i) anchor with named H-B.
```

---

## §X — What this program does NOT claim

```text
- It does not discharge H-B, H-B0, H-R, or H-Z0.
- It does not close, select, or narrow the ER fork (F'-6).
- It does not pin the D3 quantifier to any finite list, under any outcome
  (this carries parent F-2's surviving substance; see the F-to-F' table).
- It does not answer Q1 (answered by the principal at 209aa390…) — it consumes
  that answer.
- It does not answer Q2, rank Q2's options, assert a Z.2 grade, or claim a
  Q2 tier (§Q2-STOP, §Z.2, §Z.3).
- *** It supplies NO BOUND ON THE DIFFERENTIATED CLUSTER SERIES; parent O5
  REMAINS UNSUPPLIED and may not be inferred from anything in this program
  (C-15, F'-15). SCAD bounds Phi_C only; no a-derivative versions of S1, S2,
  S2b or of R.3 exist. ***
- It does not discharge O6's density-EQUALITY clause (4)(i-b), and it does not
  infer it from R1-R4 (§O.O6').
- It does not certify "the n >= 2 sums", the R^-6 pair activity, the
  long-distance margin, or the claim that clustering was never the missing
  ingredient — all four are unproven and the last three are withdrawn of
  record.
- It does not own or discharge Q6 in any form, and its artifacts may not
  contain Q6's raw-degree form except as the recorded closed-false result.
- It says nothing about kappa_record, alpha, any coupling, T7(ii), or T7(iv).
- It does not revive Route T and consumes no Route-T artifact (F'-13).
- It does not adopt any clustering axiom (F'-1).
- It does not smooth, mollify, or otherwise alter the sealed sharp localizers
  (D6', NC9).
- It does not discharge F-8, which cannot close before Phase-A executes.
```

---

## Protected status

```text
E1_successor_spec_v001_executable = false
E1_successor_spec_v002_authored = true          (this draft; UNSEALED)
E1_successor_spec_v002_sealed = false
E1_successor_spec_v002_hostile_review_cleared = false
E1_successor_spec_v002_executable = false
E1_reclassified = true
C3_no_cross_term_claim = REFUTED
C5_long_distance_margin_claim = UNPROVEN
C3_C5_frozen_input_status = REVOKED
C1_C2_C4_C6_frozen_inputs = true
E1_locus_refined_to_volume_diagonal = true
A_L0_arm1_closed_dead = true
A_L0_arm2_target = E1_ONE_LINE_CONNECTED_CROSS_TERM_FREE_HUYGENS_BOUND
A_L0_arm2_requires_both_factors = true
E1_one_line_cross_term_uncertified = true        (named blocker, open)
E1_anchored_sum_not_D3_uniform = true            (named blocker, open, NEW)
D3_quantifier_reading_frozen = standard_all_common_refinements
Q6_raw_degree_form = CLOSED_FALSE
Q6_recast_weighted_form = open                   (reading B only; not owned here)
reading_A_compelled = true
M2_carries_the_reading_A_burden = true
O1_display_nested_reading_forced = true
O6_density_equality_reverbed_not_discharged = true
KP_constant_line_specified_as_geometric_series = true
E1_replacement_activity_architecture_frozen = true   (this draft; unsealed)
E1_replacement_activity_architecture_certified = false
SCAD_is_independent_route = false                (it is IR-C's wall re-expressed)
baseline_ever_normed = false                     (S3/G_bl DELETED)
S3_G_bl_deleted = true
cell_scale_normalization_certified = false       (R-L0)
exponentiation_free_colour_sum_certified = false (R-L0b)
subtracted_carleman_constants_certified = false  (S1, S2, S2b, S4, S5)
hs_scaling_exponent_derived = false              (R-L2b)
baseline_determinant_existence_certified = false (R-L4a)
opposite_phase_sector_vanishing_certified = false (R-L4b)
baseline_collapse_certified = false              (R-L4)
kappa_bal_derived_from_surviving_weights_only = true
two_line_sector_certified = false
two_line_sector_scope = cubic_skeleton_family_A_only
n_ge_2_certified = false                         (may not be asserted)
IR_A_light_cone_lemma_certified = false          (A-L2)
IR_B_a_vertex_sector_certified = false
record_vertex_two_time_HS_certified = false      (B-L2*, the common wall)
common_wall_reported_once = true                 (F'-16)
IR_C_record_phase_operator_collapse_certified = false  (C-L1)
IR_C_commutator_form_certified = false           (C-L2)
IR_C_log_coefficient_evaluated = false           (C-L3)
multicell_baseline_extension_certified = false   (C-L5)
epsilon_star_frozen = false
epsilon_star_n1_premise_conditional = true       (rho_bar)
Gamma_star_split_certified = false
H_B_discharged = false
H_B0_discharged = false
H_R_discharged = false
H_Z0_discharged = false
O5_differentiated_series_supplied = false
Q2_open = true
Q2_held_by_principal = true
Q2_triggered = false
Q2_answered_by_principal = false
Q2_classification_standard_preregistered = true
Q2_option_iii_ordered_before_ii = true
Q2_tripwire_mandatory_with_block_on_omission = true
clustering_adoption_reached = false
majorant_derived_arm_rescoped = true
O7_escalation_retired = true
refinement_intertwiner_derived = false           (unchanged; now not required)
routeT_skeleton_gap_certified = false            (unchanged; now not required)
F8_rederivation_first_half_discharged = false
F8_gate_discharged = false
connected_linked_cluster_density_proved = false
volume_uniform_zero_free_neighborhood_proved = false
Duhamel_intensive_Hessian_equality_proved = false
ER_fork_closed = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```

---

## §H — Handoff: seal-time checklist, escalation slots, and the hostile reviewer's targets

```text
FOR THE CONSTRUCTION LANE, AT SEAL:

H-1 Re-verify every hash in §A0. The CALIBRATION_LEDGER row is the ONE
    drift-exempt row (living document; its hash moved from fcf35d0d… to
    d56a8b81… since v001, by design).

H-2 THE "no adjacent seal" ROWS ARE *EIGHT*, NOT ELEVEN (N-17 corrects v001's
    count). Enumerated by path, all in the cleanroom root:
      1. STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_RESULT_V001.md (3a6ff617…)
      2. BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_DERIVATION_V001.md   (b786db3a…)
      3. BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001.md        (6f6b822a…)
      4. STAGE8_T7_ENVELOPE_REALIZATION_COMPARISON_SPEC_V001.md      (4059eff5…)
      5. STAGE8_T7_OPEN_EXHAUSTION_ATTACHMENT_AND_RELAY_NECESSITY_RESULT_V001.md (0df721a1…)
      6. STAGE8_T7_RELAYED_FAMILY_RESOLUTION_RESULT_V001.md          (52401eef…)
      7. BID_MONOIDAL_EXTENSIVITY_DERIVATION_V001.md                 (451550c3…)
      8. STAGE8_T7_CONNECTED_ANALYTIC_CLOSURE_RESULT_V001.md         (f891d3af…)
    All eight re-confirmed this session to have NO adjacent .seal.sha256.
    *** CARVE-OUT, REQUIRED BEFORE EXECUTION, NOT AT THIS LANE'S DISCRETION:
      CARVE-OUT A — row 1 (3a6ff617…) is the SOLE SOURCE of C1, the derived
        starting point of the entire program, including the A-L1 kernel
        constant, the C-L3 log coefficient, and the marginality coefficient
        2/pi. An unsealed sole-source authority for the most load-bearing input
        must be SEALED before execution, not merely hash-pinned.
      CARVE-OUT B — row 2 (b786db3a…), one grade lower: tau_R = pi/sqrt2, on
        which every exact phase collapse in C4 and C-L1 depends. Seal before
        execution.
      Rows 3-8 may proceed hash-pinned with mandatory executor re-verification.
      This drafting lane creates no seal files; sealing is the construction
      lane's act. ***

H-3 Decide whether the drafting-lane script verify_v002.py (47589c71…) is
    relocated into the cleanroom and hashed as part of the sealed record, or
    excluded as scratch. It is scratch as written and carries NO verdict
    authority.

H-4 Confirm the corrections of record this spec carries are acceptable as
    corrections rather than requiring separate artifacts: A-L1's spinor factor;
    the IR-B per-pair-versus-summed display; the deletion of S3/G_bl; the
    striking of the D^2 <= exp(-2||[C,P]||_2^2) route to D = 0; the striking of
    the (1+|D|)/|1-D| display; the O6 re-verbing; the KP-line specification;
    the CTP-nested reading of O1; and the renaming of the n >= 2 verdict.

H-5 Confirm that the D5' split, the S-7/S-8 supersessions, and the O6
    re-verbing are within the scope of an append-only successor spec, or route
    them as amendments to the parent.

H-6 Q6's raw-degree closed-false result and the recast form are the PARENT's
    to record; confirm the parent's Route-Q line is updated of record, since
    this spec does not own it.

ESCALATION SLOTS (must be resolved by the principal, not by a lane):

E-Q1 *** SCOPING QUESTION, MANDATORY BEFORE EXECUTION (B-5(c)). *** "Is the
     pinned skeleton's cell 4-volume an admissible constant under spec-header
     scoping clause 1?" Weakening F'-5 is not a lane's to do, and this spec
     may not be executed with an obligation that is unsatisfiable under its own
     fence. If the principal declines the relief and BOTH R-L0 grounds and
     R-L0b fail, R-L0 fails with its named witness and that is the honest
     outcome — stated here so the question is not answered by execution.
E-Q2 The CODEX_RECONCILIATION_ADDENDUM slot reserved by binding R7 is CLOSED:
     it was filled by fc4368c7… (corrected via the principal). NO NEW SLOT IS
     RESERVED. Any further independent-system return arrives as a fresh
     append-only amendment, sealed by hash; if it contradicts any repair here,
     THE CONTRADICTION IS REPORTED, NOT RESOLVED SILENTLY.
E-Q3 F-8 clause (3) cannot be discharged before Phase-A executes (sequencing
     fact, not a lane failure). Whether v002 executes before F-8 closes is the
     principal's scheduling call; this spec makes no claim on it.

FOR THE HOSTILE PRE-EXECUTION REVIEWER — the places this draft is most likely
wrong, named by its author:

A. A-L0 arm 2 is the whole program now, and this lane has NOT attempted either
   Huygens factor. Attack factor (ii) first: is there ANY sealed supplier of
   >= R^-1 amplitude decay after the cell-time integrations, given that C4's
   cancellation is exactly saturated at full tau_R and the freeze's own
   cancellation inventory says time-integration smoothing is the ONLY remaining
   summability source? If there is none, A-L0 is not merely open — it may be
   closed against, in which case the correct verdict is stronger than
   E1S_BLOCKED and this spec has under-called it.
B. A-L5. Check whether reading A's "M2 supplies the anchored-sum bound
   directly" can be made subdivision-insensitive AT ALL without a weighted
   counting theorem — i.e. whether A-L5 and the recast Q6 are the same
   obligation wearing two names. If they are, this spec's claim not to own Q6
   is wrong, and the honest disposition is to escalate the two as one.
C. §R.6's honesty claim. Verify that the four surviving SCAD constants really
   do all rest on C-L2 — and if any does NOT, then SCAD retains a sliver of
   independence and §R.6 overstates the collapse in the direction of pessimism,
   which is still an error.
D. R-L4b. The claim that the opposite-phase sector vanishes IDENTICALLY for all
   a on the closed polydisc is doing heavy work: it removes half the weight
   from every sum, sup and segment. Check whether tr A(a) = -infinity for all
   a actually follows for a != 0, or only at a = 0 — if only at a = 0, B-3 is
   not repaired, it is relocated.
E. §E1' step 2's conditional certification. Check whether a
   premise-conditional eps_*^{(1)} can be composed with an unconditional
   eps_*^{(>=2)} in the min without laundering the premise into the
   unconditional leg, and whether the I3 consumer can actually receive a
   premise-marked radius.
F. §P's weighting rule. This spec now overrides its own predicted outcome with
   the independent system's. Check that this is calibration and not deference —
   in particular, whether any prediction above was changed to agree with P-C1
   without an independent ground.
```

---

*End of E1 successor program spec V002 draft. Authored append-only; v001
(`9cfafde1…`) is preserved unedited and remains non-executable. No sealed
artifact, no v001-v006 production script, and no byte-frozen derive lane was
modified; no production lane was invoked; the canonical fence was not touched.
Execution requires a fresh-context hostile review clearing this text, the two
seal carve-outs of H-2, and the E-Q1 scoping answer.*