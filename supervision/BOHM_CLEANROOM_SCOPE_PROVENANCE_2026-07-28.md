# THE GRAVITY MATERIAL OUTSIDE THE CLEANROOM — DISPOSITION (Bohm, 2026-07-28)

Run after the principal asked whether we were looking in all the right places. We were not:
a week of searches covered 840 of ~4800 files. Five trees swept, four angles, each adversarially
tested in both directions.

---

# GRAVITY MATERIAL OUTSIDE THE CLEANROOM — DISPOSITION REPORT

**Read-only sweep across five trees. Nothing computed: no alpha, no kappa_record, no kappa_Thomson, no G, and no function of them. Every numeral below is a verbatim transcription.** Four prior sweeps and their adversarial tests were reconciled; the tests' corrections are adopted, and I re-verified every load-bearing claim at source. Where the sweeps and their tests disagreed with each other, I ran the tie-breaking search myself and say so.

**The one-line answer to the principal's question.** We were not looking in all the right places, and now that we have: the material exists, it is large, somebody *did* rule on almost all of it, and the single best piece of it is a hostile-reviewed proof that the thing we hoped to find cannot work.

---

## 1. WHY THE CLEANROOM EXCLUDES IT

There is no single rule. There are **four distinct exclusion instruments operating in three different lanes**, and the brief's four-way question (quarantined / superseded / out of scope / never migrated) resolves differently in each. Stating them separately is the finding.

### 1a. The handoff construction lane — blanket directory isolation, by LOCATION

`/Users/bgm/Documents/New project/_external_handoffs/fable_alpha_cleanroom/FORBIDDEN_INPUTS.md:17-19`
```
Do not:

- inspect a parent or sibling directory;
- invoke repository discovery from this workspace;
```

`.../fable_alpha_cleanroom/DEPENDENCY_POLICY.md:3-5`
```
This package contains the known target-independent files needed to understand
and begin the active proof stages. It intentionally excludes the historical
repository and measured targets.
```

This names no gravitational object. It excludes the whole repository, and gravity only as a side effect. **It also carries its own amendment clause**, `DEPENDENCY_POLICY.md:20-22`:
```
A later curator may add a hash-verified, target-independent copy and issue a
new package manifest. A missing file never authorizes access to historical
target-aware material.
```

**The clause was exercised eleven times and never once for gravity.** `OUTPUT/DEPENDENCY_REQUEST.md` is 55 lines with eleven numbered items; `grep -niE "gravit|stress|graviton|newton|metric|sakharov|einstein"` over it returns **0** (verified this sweep). In this lane the answer is **NEVER MIGRATED** — the mechanism existed, was known, was used, and was never used for gravity.

### 1b. The live cleanroom preregistration chain — the axis is ALPHA-DIRECTEDNESS, not gravity

**Correction adopted, and it retires four of the first sweep's headline findings.** The v001 preregistration — the one carrying `S_micro[g, A, psi, R]`, Newton's constant on the input whitelist, and a stress-energy-conservation gate — is a **rejected protocol**. `alpha_fundamental_record_action_cleanroom_v002/PREREGISTRATION_V002.md:6-10`:
```
The sealed v001 preregistration is preserved. Its hostile review rejected it
as a contamination-resistant Level-2/Level-3 protocol. Version 002 is a new
gate; it does not rewrite the v001 seal or treat the intervening carrier
classification as confirmatory evidence.
```
The v001 seal is genuine (recomputed `d8eba9f9…`, matches) — but a sealed document is not a live one. v003 imports v002 by hash and never mentions v001.

**Bounded negative, narrowly stated and verified by me this sweep:** `grep -ci "gravit"` over `PREREGISTRATION_V002.md` returns **0**; over `PREREGISTRATION_V003.md` returns **0**. `grep -niE "stress.energy|stress tensor"` over both returns **zero lines**. The live charter of the current cleanroom does not mention gravity in any form, and the stress-energy gate was **dropped when the protocol was replaced, not left undischarged**.

The live exclusion clause is `PREREGISTRATION_V002.md:79-81`:
```
Old alpha-directed files, successful or failed, are not construction inputs.
They may be inspected only by a post-freeze auditor. Their absence cannot make
the present historically target-blind.
```
This is the rule that actually reaches the outside gravity corpus, and its axis is **alpha-directedness**. It converts "may we import gravity at all?" into a checkable per-file question. For this lane the answer is **OUT OF SCOPE** for the axis, with a standing permission for post-freeze inspection.

### 1c. The alpha_br lane — gravity IS excluded by name, by subject, in executable code

This overturns the first sweep's repeated thesis that the exclusion is "never by physics subject." `scripts/audit_alpha_br_replacement_carrier_forbidden_ancestry_v001.py:34-37` (verified verbatim):
```python
BASE_FORBIDDEN = {
    "gravity_emergence_theory_v008.md",
    "gravity_electromagnetism_surface_unification_v022.md",
    "alpha_induced_only_boundary_action_principle_v001.md",
```
and `:64`: `FORBIDDEN = BASE_FORBIDDEN | EXTERNAL_QUARANTINE`.

These are not in the quarantine manifest; they are unioned in by the consuming script. And they are **not contaminated**: `grep -c "137"` returns **0** for `gravity_emergence_theory_v008.md` and **0** for `gravity_electromagnetism_surface_unification_v022.md` (verified). They are forbidden as **lineage**, not for contamination. For this lane the answer is **QUARANTINED, on subject-matter grounds.**

### 1d. The external-comparison quarantine — narrow, but wider than the manifest's purpose line admits

`alpha_br_external_comparison_quarantine_manifest_v001.json:3` states its purpose as denying "external Toms lineage, historical alpha replays, and target-aware control-plane artifacts." But its `forbidden_paths` array — which the first sweep never opened — contains **37 entries** (enumerated and verified), and they include the program's **own** gravity-EM machinery: the coupled-saddle RG cancellation gate, the orbit-space beta, all four induced-Casimir-branch artifacts, `alpha_br_orbit_space_quantization_corollary_v001.md`, and `alpha_strict_route_decision_ledger_v001.csv` itself. One forbidden prefix only, and it is not a gravity prefix.

### 1e. THE DECISIVE CORRECTION — somebody ruled, 774 times

`results/alpha_strict_route_effective_state_v002.json` is a **current control artifact** under `alpha_cleanroom_current_authority_spec_v001.json` (verified: it is the first entry in `control_artifacts`). I dumped it:

- `event_count: 780`, `effective_route_count: 774`, `overall: PASS_EFFECTIVE_ALPHA_ROUTE_LEDGER`, `alpha_computed: false`, `proof_authorized: false`
- `active_routes: ["primitive_same_cell_opening_selector_v002"]` — **one active route out of 774**
- I independently counted **172 routes** whose names match `gravity|graviton|newton|einstein|induced|coupled|metric|superconn|full98|sakharov`. **None is active.** Their statuses: 83 CLOSED_BUT_INSUFFICIENT, 16 PARTIAL, 15 BLOCKED, 15 RETIRED_NEGATIVE_REGRESSION, 9 CLOSED_NEGATIVE_RESULT, 7 REJECTED, 7 RETIRED_SUPERSEDED, 5 CLOSED_NEGATIVE_EXECUTION, 4 RETRACTED_OVERCLAIM, 3 CLOSED, 3 CONDITIONAL, 2 OPEN, 1 each BLOCKED_PREEXECUTION / DIAGNOSTIC / QUARANTINED.

The same spec voids the first sweep's "nobody ruled" evidence by name: `alpha_cleanroom_current_authority_spec_v001.json` carries `"superseded_authority_files": ["alpha_cleanroom_active_manifest_v001.csv"]`. Every "ACTIVE" row in that 277-row manifest — including the coupled gravity-EM saddle principle at row 152 and the common-induced-coefficient gate at row 268 — **carries no current authority.**

### The answer, plainly

**The cleanroom does not exclude gravity by a gravity rule.** It excludes the historical repository by location, excludes alpha-directed files by contamination discipline, hard-forbids three gravity documents by name in the alpha_br lane, and — the substantive answer — **re-seeded from a different foundation after the program had already retired 172 gravity-bearing routes.** `provenance_inputs_v003.json` admits exactly five inputs and all five are gravacle_v159 documents.

**The one genuine NEVER-MIGRATED body** is the Newtonian-limit lineage: zero rows in the 774-route effective state, zero rows in the route-decision CSV, zero rows in the active manifest, zero entries in the supersessions file, zero rows in the quarantine manifest (all five greps verified = 0 this sweep). Nobody ever ruled on it. It is nonetheless inadmissible on two other standing rules — see §3 and §4.

---

## 2. A_BR(g, a, phi) — WHAT IT ACTUALLY IS

> **Yes, one computation producing both couplings from one trace exists — but it is not A_BR(g,a,phi), it is `reports/alpha_br_common_induced_coefficient_normalization_v001.md`, and the program's own hostile review has already proved that even a perfect gravity match cannot fix the absolute electromagnetic coupling.**

### A_BR is a declared shape, and the metric was added later

The **adopted** principle has no metric argument and no Dirac operator — `alpha_boundary_superconnection_principle_v001.md:11`:
```
A_BR = nabla_A + Phi,
```
Route status in the live effective state: `boundary_superconnection_principle -> CLOSED`.

The metric-dependent version appears two days later in an unadopted extension, `alpha_br_full98_diffeomorphism_naturality_theorem_v001.md:12`:
```
A_BR(g,a,phi) = D_g + c_g(a) + Phi(phi).
```
Its own status line, `:3`: `` Status: `COMPONENTWISE_PROOF_FOR_THE_DECLARED_BR_SUPERCONNECTION` ``. It carries **no seal in either sidecar convention** and appears in no manifest.

### No gravitational response is ever computed from it — and the theorem is not the kind of theorem the brief assumed

What the theorem proves is **equivariance**: `A_BR` transforms by unitary conjugation under diffeomorphisms. That is a covariance statement. The "gravitational response" it establishes is that the action *does not change*. Its own scope section, `:96-98`:
```
The theorem covers the declared ordinary compact BR superconnection and its
full98 tangent inventory. It does not compute the saddle, determinant,
threshold flow, or alpha.
```

The ledger's ruling, row 353: `full98_diffeomorphism_nonlinear_naturality, CLOSED_BUT_INSUFFICIENT, … "retain for the declared ordinary compact BR superconnection; do not infer enlarged operators saddle determinant thresholds or alpha"`. At the continuum — where any Sakharov-type induced-action argument would have to live — row 315 types it `OPEN, conditional_theorem_executable_gate_failed`. And row 333 records a **RETRACTED_OVERCLAIM** in the same lineage: `full98_global_physical_compression_oracle … "never call the old standalone comparison an independent oracle or physical-normalization proof"`. Four full98 routes are RETRACTED_OVERCLAIM and eleven are RETIRED_NEGATIVE_REGRESSION in the live effective state.

### The single computation that DOES produce both — and its self-limitation

`reports/alpha_br_common_induced_coefficient_normalization_v001.md` (read in full, verified verbatim):

- `:3` — `` Overall: `PASS_EXPLICIT_CLIFFORD_COMMON_COEFFICIENT_NORMALIZATION` ``
- `:8` — `K_Q per Weyl state = q^2 I_1(c)/(24 pi^2).`
- `:11` — "The same trace gives the per-state volume coefficient `I_3/(16 pi^2)` and the induced Einstein coefficient `-I_2 R/(192 pi^2)`."
- `:15` — **"This audits the local derivative expansion only; it is not used as a substitute for the exact nonlocal high-momentum form factor."**
- `:17` — **"This gate exists specifically to prevent the historical factor-of-two convention from re-entering the alpha route."**

So the Sakharov-shaped computation is real: one Dirac square, one heat trace, the Maxwell stiffness and the induced Einstein coefficient side by side. But the file itself types its gravitational half as a local-expansion audit, and states that its purpose is regression prevention. The consuming route is `common_br_induced_coefficients -> CLOSED_BUT_INSUFFICIENT` in the live effective state, because (ledger row 260) *"the carrier forces K_H=(3/2)K_Q and K_QH=K_Q while **no value of x is selected**."* One trace, both coefficients, **no numbers**.

### And the refutation, which is the most decision-relevant document in any tree

`reports/alpha_br_fresh_gravity_em_normalization_identifiability_v001.md` (read in full, verified verbatim):

- `:3` — `` Overall: `BLOCKED_GRAVITY_MATCHING_DOES_NOT_FIX_ADDITIVE_EM_STIFFNESS_BOUNDARY_RULE_REQUIRED` ``
- `:14` — **"These terms come from the same parity-even fermion determinant, but they do not make the absolute EM coupling identifiable. A gravity match can constrain a gravity coefficient/cutoff combination; the EM equation still contains an additive boundary value `K0`. The executable countermodels keep the carrier, cutoff, gravity coefficient, and EM slope fixed while changing only `K0`."**
- `:16` — "No measured gravitational constant and no alpha value is evaluated."

Ledger row 429, instruction of record: **"do not infer absolute EM normalization from G."** Live route status: `fresh_gravity_em_normalization_identifiability_v001 -> BLOCKED`.

**This is the answer to the brief's motivating inference.** The one-operator-both-couplings structure was built, run, hostile-reviewed, and shown to be non-identifiable. The mechanism is granted; the inference still fails.

### Three superconnections, three objects — do not conflate

1. `A_BR(g,a,phi) = D_g + c_g(a) + Phi(phi)` — parent, unsealed, unadopted, equivariance only.
2. The cleanroom's `A_BR` — `BID_GRADED_BOUNDARY_SUPERCONNECTION_REPAIR_V001.md:76-77`, `A_BR=nabla_(spin+U1+cell)+C_hat_partial`. **No metric argument at all**, so no gravitational response can be asked of it. Unsealed; 0 occurrences in `provenance_inputs_v003.json`.
3. The supervision panel's Complete Causal Superconnection Parent (Shale-Stinespring implementability) — where `α_j` are the **Dirac alpha matrices**, `REVIEW_2026-07-24_superconnection_parent_panel.md:23`.

---

## 3. THE SEVENTY-FIVE NEWTONIAN-LIMIT DERIVATIONS

**It is 75 files, not 67, and 74 distinct documents.** Verified: `shasum -a 256` over all 75 gives 74 unique digests; `v074` and `v075` are byte-identical, both `5d5956fe65525eb99f3d5f4413bd8cb1bc9d0850120476fad444fce1f8564074`.

### What they are

**One append-only working note, snapshotted 75 times in about eleven hours on 2026-07-07/08** — 9,529 bytes at v001 to 307,317 at v074/v075, one snapshot every two to five minutes. Two size *decreases* (v060→v061, v063→v064) and both are retractions. So *neither* prior reading is right: they are not 75 failed attempts, and they are not 29 duplicates of one file. Do not report either to the principal.

**Provenance hazard, verified:** line 5 of every file from **v047 through v075** reads `Working derivation note v046, July 7, 2026` while the bodies keep growing. Any citation of this material by internal version number is unreliable.

### Do they succeed? No — and the arrow is backwards, decisively

`v001:42`, on its face from the very first version:
> "The constant `G` is still fixed by calibration; this note does not derive the numerical value of Newton's constant."

In the latest version G enters as **hypothesis 7** of the central theorem — `v075:533`, `Q(boundary V) = -4 pi G M_R(V)` — and worse, `v075:301` defines an **accumulated-record coupling estimator** as a weighted least-squares fit over measured mass/flux pairs with declared-uncertainty weights. That is a *measurement* of G dressed as a recovery of G.

The G question was renamed four times across versions and then disappeared from the open list entirely, retired by declaring G primitive (`v075:1072`, `source records <-> geometry records via G`). The note concedes this at `v075:1160`: *"It also does not derive a unit-free numerical value for a dimensional constant… What the theorem derives is the role of the constants."*

The Einstein-form result at `v075:6121` reaches `8 pi G/c^4` by importing the **Lovelock uniqueness theorem** and fixing its free coefficient from the same Newtonian calibration that introduced G. **This is not a Sakharov argument**: bounded negative, narrowly stated — across all 75 files there is no metric-dependent Dirac operator, no one-loop sea determinant, no heat-kernel expansion, and no induced-Einstein-Hilbert coefficient; `A_BR`, `D_g` and `Dirac` return no hits in the derivation series.

**So the material would not help regardless of its status.** The cleanroom consumes G structurally (a Misner-Sharp bound). This note consumes it by fit. It is strictly *further* from an output than what the cleanroom already has.

### Contamination — 55 versions earlier than first reported

Verified per version: `137` count is **0** at v015, v016, **v017**, and **1** at v018, v019, v020. First occurrence `v018:1778`:
```
  approximately 1/137 at low energy?
```
Present in all 58 versions v018–v075. The `Xi_ep = alpha_low (m_p/m_e) = 13.39905342…` decimal at `v075:8627` is a *second, later* contamination on top of it. Everything from v018 is barred by `FORBIDDEN_INPUTS.md:6` ("the measured value of alpha or its inverse"), `:10` (cosmological/horizon), and `:11-12` (matter-ratio formulas compared to data).

### The apparent escape hatch at v017 — and why it closes

`v017` is numerically clean (verified: zero hits for `137|CODATA|measured value of alpha|m_p/m_e`) and it already carries the full assembly at `v017:703`:
```
G_ab + Lambda g_ab = (8 pi G / c^4) T_ab.
```
**But it is alpha-directed on its face.** `v017:1400`: *"The fine-structure constant is therefore a charge-sector spectral target:"*. Under `PREREGISTRATION_V002.md:79` that bars it as a construction input regardless of numerical cleanliness — numerical target-independence is not historical target blindness. And the governing precedent is adverse: its sibling `gravity_electromagnetism_surface_unification_v022.md` is equally 137-free (verified, count 0) and is **hard-forbidden by name** in `BASE_FORBIDDEN:36`.

### Seals — a fourth convention exists

No `.seal.sha256` in either sidecar convention for any of the 75 (verified, zero matches). But `v074` **is** sealed under a fourth convention: `gravity_emergence_theory_v006_packet_2026-07-07/SHA256SUMS.txt` carries `5d5956fe…` for `supporting_notes/gravity_emergence_newtonian_limit_derivation_v074.md`, and it verifies. A fifth convention exists too — `MANIFEST.sha256` in the handoff lane (25/25 OK). Any future seal claim in this corpus must check all five.

### One serious spillover that has nothing to do with gravity

`scripts/audit_b_c_singlet_spectral_action_gate_v001.py:27` reads `gravity_emergence_newtonian_limit_derivation_v057.md` as a gate input. All 18 of that gate's checks are **substring tests**; the suboperator check PASSES if three literal strings appear in v057 (`:~62-64`). Worse, its one strict check has **inverted logic and fails open** (`:~82-84`):
```python
"BLOCKED" if "Overall: `BLOCKED`" in matrix_scaffold else "PASS",
"strict pass requires all five suboperators to be computable, not merely named",
```
A missing input yields the empty string, so the check whose stated job is to stop "merely named" suboperators passing is the one check that passes when its evidence is absent. The cleanroom review packets v001–v005 ship this script *and* its PASS verdict, with 5 of its 12 inputs absent from the packet. **This is on the alpha critical path and should be raised separately from the gravity question.**

---

## 4. IS ANY OF IT ADMISSIBLE?

**Yes — one file, at an existing lower tier, and it is a negative.**

### The rule that permits ROUTE_MEMO imports

`PREREGISTRATION_V002.md:60-70` — the five-field provenance test:
```
Every upstream input must carry:

source path;
date;
content hash;
logical status in its source;
documented non-alpha role predating this route.
```

It is executed twice over. `provenance_inputs_v003.json` reaches all five foundational inputs by `../../` paths that resolve **outside** the cleanroom, each with sha256 + classification + `non_alpha_role` + `does_not_supply`; `results/preregistration_v003_audit.json` re-resolves and re-hashes them and passes. And eight cleanroom Stage-8 files cite absolute supervision-tree paths in a hash-pinned table — e.g. `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V001.md:49` cites `/Users/bgm/MB Work/alpha_supervision/ROUTE_MEMO_2026-07-26_ir_sea_kernel_attack.md` with digest `51f655a0…` and `SEAL_OK`, and `:71` cites `CALIBRATION_LEDGER.md` marked "living document, unsealed by design."

**Unsealedness is therefore not a bar.** `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:2251` — "Rows 3-8 may proceed hash-pinned with mandatory executor re-verification."

### And there is a *second, lower* tier already holding parent-tree files

`CURRENT_AUTHORITY_LEDGER_V010.json:31-34` (V013 names V010 as `parent_authority`):
```json
"external_target_independent_route_audits": {
    "../alpha_spectral_ncg_absolute_stiffness_research_v001.md": "CONTINUUM_SPECTRAL_AND_DETERMINANT_ROUTES_BLOCK_ABSOLUTE_STIFFNESS",
    "../reports/alpha_target_free_finite_u1_route_audit_v001.md": "FINITE_GAUGE_AND_QCA_ROUTES_BLOCK_WITHOUT_COMPLETE_CELL",
    "../alpha_finite_cptp_ctp_record_cell_hostile_analysis_v001.md": "CPTP_KINEMATICS_FORGETS_ACTION_PHASE_AND_DOES_NOT_SELECT_GENERATOR"
```
Three parent-tree files, admitted by relative path, **no hash, no seal**, each carrying exactly one thing: a verdict that BLOCKS a route.

### Applying the standard file by file

| Candidate | Verdict | Ground |
|---|---|---|
| Newtonian lineage v018–v075 | **INADMISSIBLE** | `FORBIDDEN_INPUTS.md:6,:10,:11-12` — measured alpha, horizon calcs, mass-ratio formulas |
| Newtonian lineage v001–v017 | **Barred as construction input** | `PREREGISTRATION_V002.md:79` — alpha-directed (`v017:1400`); post-freeze audit only |
| `gravity_em_surface_unification` packets (24 versions) | **INADMISSIBLE** | v026 emits a coefficient stack and compares against CODATA; v022 hard-forbidden by name |
| `gravity_emergence_theory` (9 versions) | **QUARANTINED by name** | `BASE_FORBIDDEN:35` |
| A_BR / full98 line | **Barred** | alpha-directed lineage; partly RETRACTED_OVERCLAIM; its own scope line disclaims what would be imported |
| `alpha_br_common_induced_coefficient_normalization_v001.md` | **Admissible in principle, useless as a route** | Not on any forbidden list (verified, 0 hits). But it self-types as a local-expansion audit and its route leaves `x` unselected |
| **`reports/alpha_br_fresh_gravity_em_normalization_identifiability_v001.md`** | **ADMISSIBLE, at the negative-authority tier** | **Verified not on the 37-path forbidden list, not in BASE_FORBIDDEN, not in any manifest. Its own text: "No measured gravitational constant and no alpha value is evaluated." Its content is a BLOCK verdict — exactly the shape of the three files already in that slot.** |

One caveat to state honestly: the identifiability report is an alpha_br-lane artifact and therefore alpha-directed by lineage. That bars it as a *construction* input — but `PREREGISTRATION_V002.md:79` expressly permits post-freeze inspection of alpha-directed files, and admitting a **blocking verdict** is inspection, not construction. That is what the three existing entries in `external_target_independent_route_audits` are.

---

## 5. THE HONEST ASSESSMENT

**A graveyard with three small assets in it, and the largest asset is a negative.** Volume is not value here, and the sweep's own premise was half wrong in both directions.

### The graveyard, specifically

- **172 gravity-bearing routes in the live effective state, zero active.** Four RETRACTED_OVERCLAIM in the full98 line alone.
- `induced_casimir_gravity_fixed_point_conversion -> REJECTED`, ledger row 121, *"do not patch or reuse this root"* — and its four artifacts are additionally on the quarantine `forbidden_paths`. Double-killed. Any Sakharov revival must not re-enter through this door.
- `coupled_saddle_rg_cancellation -> REJECTED`, row 172 — a one-loop Einstein-Maxwell term combined with the coupled saddle **cancels the absolute alpha and leaves a residue with no alpha in it.** The route did not fail on provenance; the target dropped out of the answer.
- `coupled_surface_saddle_equations -> CLOSED_BUT_INSUFFICIENT`, row 157 — the most explicit gravity-EM relation in any tree "admits an exact saddle for every positive alpha." Non-selecting by construction.
- The 75-version Newtonian note, which consumes G by weighted least squares.
- Process failures worth naming: the v047–v075 version-label freeze; byte-identical v074/v075; a gate that PASSES by substring and fails **open** on its one strict check; review packets shipping an unreproducible PASS; and a certifying flag in `alpha_fundamental_record_action_cleanroom_v003/scripts/audit_coupled_gravity_charged_fixed_point_selector_v001.py:~80` that is a **hardcoded Python literal** (`"coupled_fixed_point_is_valid_selector_form": True`) sitting in the payload dict rather than in the `checks` dict — though in fairness the same script self-types `"executable_role": "SELECTOR_ALGEBRA_REGRESSION_GUARD_NOT_DYNAMICS_PROOF"`.

### The three genuine assets

1. **`reports/alpha_br_fresh_gravity_em_normalization_identifiability_v001.md`** — the identifiability refutation. Importable at zero cost, and it permanently closes the one-operator-two-couplings hope inside the cleanroom.
2. **`reports/alpha_br_common_induced_coefficient_normalization_v001.md`** — the real one-trace-both-coefficients computation. Valuable as a normalization veto against a factor-of-two convention error; not a route.
3. **`reports/alpha_eh_subspace_invariance_v001.md:3`** — `` NO_GO_EINSTEIN_HILBERT_SUBSPACE_NOT_HEAT_FLOW_INVARIANT ``. Do not over-read it: the ledger types this **BLOCKED with two stated reopen conditions** (row 114 — the universal heat coefficient generates R², Ricci², Riemann² terms), not permanently rejected. An EH-only truncation not being preserved is not the same as no induced Newton coefficient being derivable.

### The premise correction the principal should hear

**The cleanroom is not gravity-free.** Verified this sweep, restricting to `*.md` and `*.json` (the raw counts everyone has been quoting are contaminated by the vendored `.proof_deps/sympy` tree — all 16 "Newtonian" hits and all "Ricci" hits are sympy):

| term | files in cleanroom v003 |
|---|---|
| stress-energy / stress tensor / graviton / vierbein / backreaction / induced gravity / Ricci / Newtonian | **0** |
| **Sakharov** | **4** |
| **Susskind** | **4** |
| **Einstein-Hilbert** | **2** |
| **"induced coupling"** | **5** |

- `COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:42` is a **sealed, live gravity→EM normalization transfer** (Kaluza-Klein reduction) that "does not use alpha" — and it failed on a **radius modulus** (`:56`), not on admissibility. This alone disproves any blanket gravity-exclusion rule inside the cleanroom.
- `FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md:85` puts gravity and the charged sector in one `Q_spec[g, a, psi, R]`, sealed (recomputed `a27a2d57…`, matches).
- Sakharov and Susskind-Uglum are the principal's **stated reason of record** for three principal acts (R-17, R-18, R-19), and each act fences itself: `STAGE8_T7_CL3_NONZERO_TYPING_PRINCIPAL_DECISION_V001.md:88` — *"no new principle enters the corpus by this act, and no artifact may cite this one as authority for the physical claim itself."*
- **And that ground has already been adjudicated in the supervision lane, on 2026-07-27.** `BOHM_DIVERGENCE_RETYPING_SWEEP_2026-07-27.md:219` finds the object the ground actually fits is the Thomson gate rather than C-L3, that **the gate survives**, and — a scope limit stated nowhere in the outside corpus — *"Susskind-Uglum and Sakharov are UV-induction arguments… Your ground does not transfer to an IR limit."* The same file records the deeper problem: the only corpus sentence naming a stiffness-generating mechanism is a "may", which under the program's own verb calibration is a premise. **The mechanism is presupposed, not derived.**

### The orphan

`alpha_fundamental_record_action_cleanroom_v003/COUPLED_GRAVITY_CHARGED_FIXED_POINT_SELECTOR_GATE_V001.md` states `alpha_* = f_grav / b_ch` — the exact structure the sweep went outside to find, sitting **inside** the cleanroom. Verified: **unsealed**; appears in **none** of `CURRENT_AUTHORITY_LEDGER_V001..V013.json`; cited by **exactly one file in the entire cleanroom, its own audit script**. Its flags read `f_grav_derived = false`, `b_ch_derived = false`. The supervision tree already ruled on it — `BOHM_SWEEP_2026-07-27_route_graveyard.md:158-163`: *"It is a CROSSCHECK, not a route — importing it as an input to the microscopic action would be circular."*

### Net

The outside corpus does not supply what the inside lacks. What the inside lacks is a rule that fixes the absolute stiffness — `K0` outside, `c_R` inside (`ABSOLUTE_STIFFNESS_SELECTOR_ROUTE_LEDGER_V003.md:20`, `K -> K + c_R`, with the induced-gauge/compositeness route enumerated there and typed `BLOCK_CURRENT_SPECIFICATION` at `:47`). The outside corpus's single best attempt at exactly that problem is a hostile-reviewed proof that gravity matching cannot solve it. **Those two ledgers are describing the same obstruction in two notations and do not cite each other.** That, more than any missing gravity file, is the finding.

---

## 6. WHAT THE PRINCIPAL WOULD BE DECIDING

**Not a new charter. Nothing found supports one.** Typed, in order of cost:

**D1 — AN IMPORT AUTHORIZATION at an existing tier. Recommended. Low cost, high value.**
Add `reports/alpha_br_fresh_gravity_em_normalization_identifiability_v001.md` to `external_target_independent_route_audits` in the next `CURRENT_AUTHORITY_LEDGER`, with verdict string `GRAVITY_MATCHING_DOES_NOT_FIX_ADDITIVE_EM_STIFFNESS_K0`. No new rule; the slot exists and holds three files already; hash-pinning is optional at that tier and free to add. Effect: the induced-gravity→alpha route is closed **inside** the cleanroom, by an artifact that evaluates no measured constant, and the K0/c_R identity between the two ledgers becomes citable.

**D2 — A SCOPE RULING on the one body nobody ever ruled on. Medium cost.**
The 75 Newtonian-limit derivations and the 24-version unification lineage have zero rows in every ruling register (five greps, all verified = 0). Recommendation: rule them **INADMISSIBLE** and record the ground — v018+ fail `FORBIDDEN_INPUTS.md:6/:10/:11-12`; v001–v017 fail `PREREGISTRATION_V002.md:79` as alpha-directed; and in any case the arrow is backwards, so admission would not help. One ledger row ends a recurring sweep target permanently.

**D3 — A DISPOSITION RULING on the orphan. Medium cost, and this one is hygiene.**
`COUPLED_GRAVITY_CHARGED_FIXED_POINT_SELECTOR_GATE_V001.md` is inside a sealed cleanroom, unsealed, in no authority ledger, cited only by its own audit script, and carrying the corpus's most seductive equation. Either enter it in the ledger with an honest typing (the supervision lane's "crosscheck, not a route" is already drafted) or retire it. Leaving it as it stands is the exact failure mode the discipline exists to prevent.

**D4 — NOTHING AT ALL** on the remaining outside gravity corpus. 172 retired routes, a REJECTED induced-Casimir conversion with "do not patch or reuse this root", a REJECTED coupled-saddle route that cancels the target out of the answer, and a non-selecting saddle relation. No revival is warranted on anything found.

**D5 — SEPARATE LANE, NOT A GRAVITY DECISION, BUT URGENT.**
`scripts/audit_b_c_singlet_spectral_action_gate_v001.py` fails open on its one strict check and the cleanroom review packets ship its PASS with 5 of 12 inputs absent. This is on the alpha critical path and was found only incidentally.

---

## 7. ESTABLISHED / BOUNDED NEGATIVE / UNRESOLVED

### ESTABLISHED (verified at source this sweep)

1. **774 effective routes, 1 active, and it is not gravitational.** `results/alpha_strict_route_effective_state_v002.json` — `active_routes: ["primitive_same_cell_opening_selector_v002"]`; 172 gravity/induced/coupled/metric/full98-named routes, none active.
2. **The active manifest is a superseded authority file, by name.** `alpha_cleanroom_current_authority_spec_v001.json` → `"superseded_authority_files": ["alpha_cleanroom_active_manifest_v001.csv"]`.
3. **Gravity IS excluded by subject in the alpha_br lane, in executable code.** `scripts/audit_alpha_br_replacement_carrier_forbidden_ancestry_v001.py:34-37` and `:64`; the two named gravity manuscripts carry zero `137`.
4. **The v001 preregistration is a rejected protocol.** `PREREGISTRATION_V002.md:6-10`. The `S_micro[g,A,psi,R]` charter, the G whitelist entry, and the stress-energy gate all belong to it.
5. **A one-trace-both-couplings computation exists and self-limits.** `reports/alpha_br_common_induced_coefficient_normalization_v001.md:8, :11, :15, :17`.
6. **Gravity matching cannot fix the absolute EM stiffness.** `reports/alpha_br_fresh_gravity_em_normalization_identifiability_v001.md:3, :14`; ledger row 429.
7. **The Newtonian lineage consumes G rather than producing it.** `v001:42`, `v075:301`, `v075:533`, `v075:1160`.
8. **Contamination enters at v018:1778**, not v073; 75 files, 74 distinct; v074≡v075 (`5d5956fe…`); v047–v075 all self-declare "v046".
9. **External citation is established, hash-pinned practice.** `provenance_inputs_v003.json`; `results/preregistration_v003_audit.json`; eight cleanroom files citing absolute supervision paths (`STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V001.md:49, :71`).
10. **A second, lower external tier already exists** and holds three unsealed, unhashed parent-tree files admitted solely for their blocking verdicts — `CURRENT_AUTHORITY_LEDGER_V010.json:31-34`.

### BOUNDED NEGATIVES (each is exactly the search named, nothing wider)

- `grep -ci "gravit"` over `PREREGISTRATION_V002.md` → **0**; over `PREREGISTRATION_V003.md` → **0**. `grep -niE "stress.energy|stress tensor"` over both → **zero lines**.
- Restricted to `--include='*.md' --include='*.json'` over `alpha_fundamental_record_action_cleanroom_v003`: stress-energy, stress tensor, graviton, vierbein, backreaction, induced gravity, Ricci, Newtonian → **0 files each**. All raw hits for Ricci/Newtonian live in `.proof_deps/sympy`.
- `grep -niE "gravit|stress|graviton|newton|metric|sakharov|einstein"` over `OUTPUT/DEPENDENCY_REQUEST.md` (55 lines, 11 items) → **0**.
- `grep -ci "newtonian"` → **0** in `alpha_strict_route_decision_ledger_v001.csv`, **0** in `results/alpha_strict_route_effective_state_v002.json`, **0** in `alpha_cleanroom_active_manifest_v001.csv`, **0** in the quarantine manifest, **0** in `alpha_strict_route_supersessions_v001.json`.
- `ls gravity_emergence_newtonian_limit_derivation_v*.seal.sha256` and `*.md.seal.sha256` → **no matches** (all 75 unsealed in both sidecar conventions).
- `COUPLED_GRAVITY_CHARGED_FIXED_POINT_SELECTOR_GATE_V001.md` appears in **no** `CURRENT_AUTHORITY_LEDGER_V*.json` and is cited by exactly one file in the cleanroom.
- `grep -rliE "sakharov|induced gravity|newtonian limit|stress-energy"` over `/Users/bgm/MB Work/memory-bank` (800 md) → **0 files**. That tree is irrelevant to this question.
- The identifiability report is **not** in the quarantine manifest, **not** in the active manifest, **not** in `BASE_FORBIDDEN` (three greps, all 0).

### UNRESOLVED

- **Whether `K0` (outside) and `c_R` (inside `ABSOLUTE_STIFFNESS_SELECTOR_ROUTE_LEDGER_V003.md:20`) are the same object.** They are described identically as an additive Maxwell-stiffness freedom no symmetry forbids, in two ledgers that do not cite each other. I did not attempt to prove the identity, and doing so would require an operator-level comparison outside this sweep's remit.
- **Whether the depth `x` in `common_br_induced_coefficients` and the radius modulus `beta` in `COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:56` are the same unselected scale.** Both are single free parameters that block otherwise complete gravity→EM transfers. Not investigated.
- **The `f_charged_step13b` / `alpha_G` electron-anomaly comparison** is target-scored and is **not** quarantined (grep against the quarantine manifest returns nothing); it is disposed of only by ledger row 88. Its disposition should be checked by someone with authority over that lane.
- **The b_c_singlet fail-open gate and the unreproducible packet PASS** (§3, §6-D5) — real, on the alpha critical path, and outside this sweep's question.

### ALPHA-COLLISION REGISTER (flagged per standing instruction — at least twelve senses)

Inside the cleanroom: the **Schatten-2 exponent**; the translation index `alpha_x`; `alpha_tree` (Kaluza-Klein tree coupling, `COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:42`); `alpha(0)` / `kappa_Thomson` (`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:1660`).
In supervision: the **Dirac alpha matrices** `α_j` (`REVIEW_2026-07-24_superconnection_parent_panel.md:23`).
Outside: `alpha_low` (fine-structure, ~2938 uses); `alpha_c` (color-boundary/singlet threshold, ~4858); `alpha_s` (strong, ~2863); `alpha_L` (running color coupling at scale L, ~1883); `alpha_i = eta_i^2` (per-species charge response); bare `alpha` as the **Lovelock coefficient** in `E_ab = alpha G_ab + beta g_ab` (`v075:6118`) and as a Lagrangian normalization in `k/alpha = 8 pi G/c^4`; `alpha_EM` as the **SU(5) parent-scale coupling** (ledger row 104) and as a rejected conversion output "about 1936" (row 121) — **neither is the fine-structure constant**; and `alpha_G` with **two incompatible meanings in one tree** — the gravitational fine-structure coupling `G m^2/(hbar c)` (`field_access_allow_require_unification_v001.md:268`) and a Gravacle-derived EM value scored against the electron anomaly (`f_charged_step13b_electron_anomaly_prediction_freeze_v001.md:35`).

**No automated grep for `alpha` is trustworthy anywhere outside the cleanroom.** None of these were conflated in this sweep.