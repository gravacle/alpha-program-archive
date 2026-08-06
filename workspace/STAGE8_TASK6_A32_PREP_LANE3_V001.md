# STAGE 8 / TASK 6 — A32 PREPARATION

Date: 2026-08-06  
Lane: Codex Lane 3 (SOL, high effort)  
Task: PASTE 599 / Task 6, Step 1  
Custody: consolidation and draft only; Dario reviews; the principal ratifies

## Lead determination

```text
REGISTER_HEAD = Q-532
TASK_5 = CLOSED
ESCROW = OPENED

A32 = RATIFIED_PROCEDURE_NOT_ATTAINED
A32_SOURCE_CENSUS = 15_LOAD_BEARING_SOURCES
A32_LIVE_TOP_LEVEL_OBLIGATIONS = 20

SATISFIABLE_AS_INHERITED = 6
NEEDS_A_TASK_6_STEP = 6
IN_TENSION = 8

INSTRUMENT = DRAFTED_NOT_RATIFIED
GATE_LIFTED_BY_THIS_ARTIFACT = none

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The central distinction is fixed at the outset:

```text
A32_FREEZE_RATIFIED
  != A32_PRE_EVALUATION_READY
  != A32_RESULT_PASSED
  != FINAL_CLAIM_AUTHORIZED.                              (L0)
```

This relay prepares the first object only. It creates no holdout seal, prediction-map
seal, result seal, numerical value, comparison, or authorization.

## 0. Preflight, method, and protected scope

### 0.1 Preflight

The following read-only checks passed before drafting:

```text
QUESTIONS_SETTLED_REGISTER terminal row                  = Q-532
QUESTIONS_SETTLED_REGISTER SHA-256                       =
  89cab1627e258e8e994fde23c6aede79e89fa7e3ffee10f10b605c2056d59bdf

DECISION_ESCROW_OPENED SHA-256                           =
  f82a7b27f5476b5e620ae8f0827618e435076d72b0a87b38e13114299de7c229
sidecar                                                    = verified

FABLE_WITNESS_CERTIFICATION_TASK5 SHA-256                =
  fc2ed58687c226c3b549b66da30b4184504bd205fbd345fea4f81d95f84374b1
sidecar                                                    = verified

required output absent in cleanroom                      = true
required output absent in archive workspace              = true
```

The escrow ruling at `DECISION_ESCROW_OPENED_2026-08-06.md:5-14` says, in its
load-bearing words, that Task 6 is licensed **“in sequence”**, beginning with
“A32 preparation,” followed by the evaluation DoR whose scope is “the LOCAL
chain, its product typed LOCAL-SHADOW”; each protected flag lifts only at its own
gate. This artifact is that preparation and no later act.

### 0.2 Register sweep and semantic inclusion rule

The register and sealed corpus were swept by name and content for:

```text
A32
external holdout
unused structure-sensitive prediction
ratification / authorization
evaluation before seal
HOLDOUT-UNIVERSE-SEAL
PREDICTION-MAP-SEAL
ALPHA-RESULT-SEAL
HOLDOUT-RESULT-SEAL
FINAL-CLAIM-SEAL
```

A source enters the numbered B1 census only if it directly supplies at least one
of the following:

1. an A32 obligation or authorization dependency;
2. a ratified or expressly incorporated freeze term;
3. a later principal amendment or supersession;
4. a present-state implementation constraint needed to apply A32 to the Task-6
   subject.

Duplicate mirrors, relay prompts, plans, trackers, supporting findings already
consumed by a principal ruling, and superseded drafts are excluded. The one
exception is V000: its specified clauses are expressly incorporated by the
sealed V002 ratification and are therefore load-bearing through that attachment.

### 0.3 Seal topology

The corpus warning is operative. A seal was accepted only through the applicable
attachment form:

```text
adjacent sidecar:          X.md.seal.sha256 or X.seal.sha256;
multi-target manifest:    X is a verified row of a sealed manifest;
sealed incorporation:     a sealed authority pins X's hash and incorporates
                           an exact range of X.                  (S0)
```

No file was treated as sealed merely because its prose says “sealed.” External
supervision inputs are admitted only by path and hash under
`STAGE8_AUTHORITY_CHAIN_PRECEDENCE_BINDING_V001.md:18-26`.

### 0.4 Tags and fences

```text
[PROVABLE]       displayed consequence of a verified source;
[PART-PROVABLE]  exact conditional statement with its missing premise shown;
[YOURS]          proposed binding text, not an adopted rule;
[IN-TENSION]     two live requirements cannot presently be jointly certified;
[TYPE-U]         typed but uninhabited or unexecuted object.
```

No member is bound. No fixed point is executed. No seed/end test is run. No
prediction, uncertainty, distinctness statistic, coupling, or other value is
evaluated. No measured central value is read or compared.

## 1. B1 — A32 consolidated

### 1.1 The fifteen-source load-bearing census

The hash in every numbered row below was recomputed and its seal attachment was
verified before its text was consumed.

| # | Source and SHA-256 | Seal attachment | Load-bearing lines and exact text |
|---:|---|---|---|
| 1 | `STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V002.md` — `7995f6fda75e78795cbfe167f8c8df634170ea3b43affd5bbe6e22bcda8f6ffe` | row 6 of `STAGE6_PARENT_ACTION_LEDGER_V002.seal.sha256` | `:119-140`: the open `Q_spec` list ends with **“one unused structure-sensitive prediction.”** |
| 2 | `BID_CONSOLIDATED_HOSTILE_AUDIT_MATRIX_V005.md` — `78f6bb08b7ae89d700cf84a19ebf8e62fa489a4ec6762429ac46d027538cbfe3` | hash pinned by the sealed Gate-5 authority | `:51-53`: final evidential independence requires A32; `:82`: exhaustive public registry, outcome-blind commitments, future beacon, eligible same-alpha difference, prediction sealed before unmask, fail closed; `:84`: passed A32 is a literal A34 dependency and `proof_authorized` is equivalent to evaluator-computed `FINAL-CLAIM-SEAL=true`. |
| 3 | sealed packet `review_packets/STAGE7_QSPEC_CANDIDATE_V001/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` — `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a` | row 64 of `STAGE7_PACKET_MANIFEST_V001.sha256`, independently pinned by the sealed Gate-5 authority | `:1781-1826`: the complete seal DAG and **“proof_authorized if and only if FINAL-CLAIM-SEAL is true”**; `:1947-2016`: base registry, eligibility, all-ID prediction-map, future beacon, selected-prediction seal, unmask, contamination, and fail-closed rules. |
| 4 | `A32_FREEZE_V002_RATIFIED_2026-07-28.md` — `32dbfc33b4f07407903ec014627ea64de57b5b1a6dc017dd27c6504729c3a327` | adjacent sidecar | `:3-8`: ratified, but **“SPEC-SEAL becomes ATTAINABLE, not attained”**; `:35-38`: thirteen V000 mechanics incorporated; `:42-80`: registry/family, beacon, comparator/calibration, threshold; `:82-104`: commit-before-execute order and evaluator still blocked. |
| 5 | `AUTHORITY_CHAIN_PRECEDENCE_PRINCIPAL_DECISION_2026-07-29.md` — `85bacbee7c9b6ef9f4e65e5eb898bd5273440d600fadd342c5556c2075f5dc8e` | adjacent sidecar | `:18-41`: the cleanroom chain, V011, seal ladder, and ratified A32 govern procedure; conflicting parent order is void; a final claim remains behind passed A32. |
| 6 | `STAGE8_AUTHORITY_CHAIN_PRECEDENCE_BINDING_V001.md` — `61c6de58a8690852fbae5d95cfbe21cd377e80b5ceeb3c52852e007755c60150` | adjacent sidecar | `:18-39`: the cleanroom chain governs A32; every external input must be cited by path and hash; evidence admission does not import parent premises. |
| 7 | `A32_FREEZE_DRAFT_V000_2026-07-28.md` — `13faf0bc9a455590bd99d1a40587d798bc558e87aa1d1bc6dcf6778731138123` | not standalone-sealed; exact clauses sealed by V002 incorporation at `:28-38` | `:11-15`: freeze precedes construction/prediction/evaluation; `:21-58`: thirteen mechanical items; `:62-90`: six principal items. Only the incorporated ranges are consumed. |
| 8 | `A32_MASKING_DISPOSITION_PRINCIPAL_DECISION_2026-07-30.md` — `d7153b91039974af15ab88fa6698e0573a0113fa826aa4f4ba9651b2277467bc` | adjacent sidecar | `:15-19`: the limitation is permanent and must travel with every A32 headline; process independence and independent attestation were never established; `:35-49`: covariance is vacuous only for the present scalar source, while vector/multicomponent extension requires collector revision and recommitment before prediction. |
| 9 | `SLOT18_ADMISSIBILITY_PRINCIPAL_DECISION_2026-07-30.md` — `a132f4b2421610c7df4e9a8746286999b31672f1f2d805588ed3f1ad81ad6259` | adjacent sidecar | `:12-35`: `unused` is identified with complete-lineage absence and F-U1/F-U2 remain armed; `:44-64`: comparator-precision clause 3 is added before beacon selection, never using a measured central value, with F-C3. |
| 10 | `QUESTIONS_SETTLED_REGISTER_V001.md` — `89cab1627e258e8e994fde23c6aede79e89fa7e3ffee10f10b605c2056d59bdf` | adjacent sidecar | `:130-139`: slot 18 is not list-last, but unmasking is after alpha; `:1083-1111`: Q-25 supersedes Q-24; `:1162-1226`: Q-27/Q-28 control; `:13119-13121`: Q-532 opens Task 6 with A32 preparation first. |
| 11 | `STAGE8_SLOT18_Q23_Q28_GOVERNING_REGISTRATION_V001.md` — `84966722ba7d7430a66f360d8f5ca3edde19f5b5035a26c7eb374f88e477424f` | adjacent sidecar | `:5-17`: current screen has no live family and eligibility is unexecuted; `:236-299`: permanent masking qualification and scalar-only present collector; `:331-417`: Q-27/Q-28; `:419-434`: all A32 ladder seals remain false. |
| 12 | `STAGE8_SLOT18_COMPARATOR_PREREGISTRATION_V001.md` — `2dbd3d1e3780f8ac96ada796fc070f085cc770ba9a4336d8702fcf929232485b` | adjacent sidecar | `:5-19`: five families lack a formula payload and the sixth is refuted by Q-28; `:67-101`: same-alpha/calibration/uncertainty contract; `:140-174`: identical serialized alpha token, fixed vintage/order, exact candidate identity, explicit units, scalar-only collector, Q-28; `:218-233`: no live current comparator path. |
| 13 | `STAGE8_SLOT18_Q34_NATIVENESS_AND_HOLONOMY_BRIDGE_RESULT_V001.md` — `8abb40899bda75d90a36c17448ced180df311e55aa50d10f66fa01c1f024d095` | adjacent sidecar | `:5-45`: a deterministic alpha re-expression is ineligible and dimensionlessness removes none of four bridges; the top family still lacks the physical observable, canonical A32 record, comparator, and sealed uncertainties; `:47-65`: Q-25 qualification carried. |
| 14 | `STAGE8_SLOT18_BOUNDED_SCOPE_INVENTORY_V001.md` — `3a1a9d985d518937821cdd2af6c6a33fd4878969eaddae44b036ab0d29a37b0a` | adjacent sidecar | `:245-279`: observed public record shape and hashes, without independently promoting the producer's “value-free” label; `:281-297`: 355 collected rows are not the eligible universe and no universe seal exists; `:352-391`: still-live response-schema and preselection-uncertainty mismatches. Its then-current `unused` and comparator findings are historical and superseded by sources 9 and 12. |
| 15 | `STAGE8_PREREGISTRATION_ENCODING_PRECEDENCE_AND_A32_PREPARED_TEMPLATE_AUTHORITY_RECORD_V001.md` — `bec512930fceffe99ca8acff398e68df453c94c490df2db2487c6b59ecd2a178` | adjacent sidecar | `:33-43`: V001 is prepared, not ratified, not sealed, and not ladder authority; V002 alone controls. |

Sources 14 and 15 are included because they constrain what may truthfully be
called inherited and what may truthfully be called authority. Supporting Q-23/Q-24
and Q-28 findings are not counted separately because sources 8, 9, and 11 consume
and supersede them. Duplicate archive mirrors are not separate sources.

`STAGE8_SLOT18_DERIVATION_DEPENDENCY_MAP_V001.md`
(`a983f15abecd5d542198abe56082a59c50c6259aa667dce4d190b5873800c1d3`,
sidecar verified) is excluded as a derivative map: its live
`prediction_derivable_now=false` state and bridge debts are already fully
consumed by sources 11-14 and add no independent obligation, amendment, or
authorization rule.

### 1.2 The V011 byte-version finding

[PROVABLE] The root copy and sealed packet copy of V011 are different bytes:

```text
root BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md
  SHA-256 = 20a3a17d44e15841baded9eaed3fdbecfde0ecb14bdb8162ea41a8bcd21d1a48
  seal attachment for those bytes = none found

sealed packet V011
  SHA-256 = aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a
  manifest row = verified.                                  (S1)
```

The only substantive diff is the later expanded A32 freeze block. The lawful
current composite is therefore

```text
V011_base[aa7c6d49...]
 + A32_FREEZE_V002[32dbfc33...]
 + incorporated_V000[13faf0bc...]
 + Q25[d7153b91...]
 + Q27_Q28[a132f4b2...],                                  (S2)
```

not the unsealed root V011 bytes consumed wholesale. All V011 line citations in
this artifact point to the sealed packet unless expressly labeled as an
unsealed-root drift observation.

### 1.3 Version drift and supersession board

| Earlier text | Controlling text | Disposition |
|---|---|---|
| sealed packet V011 says exact freeze fields are unset | V002 ratifies those fields and incorporates V000 | Freeze-field component is attainable; no ladder seal is attained. |
| prepared V001 resembles a ruling | source 15 and V002 say prepared/not-ratified/nonauthority | Excluded from authority. |
| V002 `:51-53` cites “five eligibility conditions (V011:1983-1993)” | those line numbers match the sealed packet; the unsealed expanded root shifts eligibility to `:2080-2089` | Content controls; stale line numbers are not silently transplanted. |
| unsealed expanded-root V011 says comparator expressions are “cited before” | sealed V002 says “citable BEFORE,” and source 12 records that later phrase as controlling | The V002 ratified phrase controls; the unsealed-root phrase supplies no authority and no backdated citation claim is invented. |
| Q-23 says `unused` undefined | Q-27 identifies it with complete-lineage absence | Q-23's open state is superseded; F-U1/F-U2 remain. |
| Q-24 says masking compliance not established | Q-25 accepts cryptographic concealment with permanent process-independence limitation | The original independence requirement is not proved; the limitation is disclosed, not erased. |
| original covariance path permits vector/Mahalanobis treatment | Q-25 finds the present collector scalar-only | A vector extension requires collector revision and recommitment before prediction. |
| V002 expected alpha-adjacent precision observables as plausible candidates | Q-28 adds comparator-precision clause 3 | The only frozen formula branch is presently refuted; current all-three screen is empty, while eligibility itself remains unexecuted. |
| old witness-to-number board says “attain A32” before evaluation DoR | current escrow says “A32 preparation,” then a scope DoR | The two are not equated. Section 1.6 separates pre-evaluation readiness from post-alpha A32 completion. |

### 1.4 The live top-level obligation count

The count follows the corpus's own enumeration:

```text
13 mechanical items in V000, ratified through V002
 +6 principal items in V000, covered by V002's four rulings
 +1 genuinely added Q-28 comparator-precision clause
 =20 live top-level obligations.                            (O0)
```

Q-25 qualifies the existing custodian/covariance row. Q-27 identifies terms
already inside eligibility and contamination scope. Neither adds a duplicate
top-level row.

### 1.5 What A32 requires of the number

[PROVABLE] An A32-facing output is not a bare scalar. From incorporated V000
item 12, V002's comparator/calibration ruling, and sealed V011's selected-output
rule, the source-required core record is

```text
A32CorePayload_i :=
  (canonical_id_i,
   predicted_output_i,
   units_i,
   theory_uncertainty_i,
   covariance_i_if_applicable,
   propagation_trace_i,
   comparator_output_i,
   structure_sensitivity_i,
   pass_fail_template_i).                                    (O1)
```

The payload must be produced from an immutable map for every eligible canonical
ID before alpha evaluation. The selected payload is sealed while the measured
outcome remains masked. Its comparator consumes the identical alpha token and
candidate metadata, under the frozen physical convention
`alpha(0)=1/(4 pi kappa_Thomson)`. No candidate-specific fit, refit, channel
coefficient, order choice, or post-selection is allowed.

[YOURS — proposed binding, not an inherited A32 field] For the inherited Task-6
subject, the source-required core must be wrapped without erasure as

```text
Task6TypedPayload_i :=
  (A32CorePayload_i,
   output_type_i = LOCAL-SHADOW,
   route_i = LOCAL,
   trial_i = ONE-SIDED_ON_CURRENT_FINITE_CHI_LATTICE,
   period_native_i = false,
   A7_branch_i,
   CARRY_1_labels_i,
   cross_sector_unit_trace_i,
   open_premises_and_falsifiers_i).                         (O2)
```

A32 cannot transform `(O2)` into a global period or Thomson quantity. If no
public observable and same-alpha comparator can consume `(O2)` faithfully, that
candidate fails computability or structure sensitivity; an empty eligible set
fails closed.

### 1.6 What A32 requires of the evaluation and authorization chain

The sealed DAG separates two halves:

```text
PRE-EVALUATION HALF
  frozen protocol
  -> exhaustive registry + eligibility implementation + commitments + beacon rule
  -> HOLDOUT-UNIVERSE-SEAL
  -> immutable all-eligible-ID prediction-map code
  -> PREDICTION-MAP-SEAL
  -> only then may alpha be evaluated;

POST-ALPHA HALF
  ALPHA-RESULT-SEAL
  -> future beacon value
  -> selected prediction sealed
  -> contamination/commitment checks
  -> custodian unmask
  -> HOLDOUT-RESULT-SEAL
  -> A33 + three new final reviews
  -> FINAL-CLAIM-SEAL
  <-> proof_authorized.                                    (O3)
```

The full pre-alpha stop rule is stronger still:

```text
alpha evaluation requires
  THOMSON-RESULT-SEAL
  + PARENT-COMPARISON
  + HOLDOUT-UNIVERSE-SEAL
  + PREDICTION-MAP-SEAL.                                  (O4)
```

Thus “A32 preparation” may be drafted now, and an evaluation DoR may be drafted
as a conditional scope declaration, but neither makes `(O4)` true. The Task-6
instrument below makes this tension explicit instead of declaring A32 attained.

## 2. B2 — A32 applied to the inherited Task-6 state

### 2.1 Verified inherited-state inputs

These are application inputs, not additional members of the fifteen-source A32
census:

| Input | SHA-256 | Exact strength consumed |
|---|---|---|
| `FABLE_WITNESS_CERTIFICATION_TASK5_2026-08-06.md` | `fc2ed58687c226c3b549b66da30b4184504bd205fbd345fea4f81d95f84374b1` | `:32-35`: seed is END_TEST_STRUCTURAL, local trial one-sided, period route two-sided only if formed, both A7 branches carried; `:44-48`: executable local chain, product LOCAL-SHADOW, CARRY-1, armed falsifiers, fences unchanged. |
| `DECISION_ESCROW_OPENED_2026-08-06.md` | `f82a7b27f5476b5e620ae8f0827618e435076d72b0a87b38e13114299de7c229` | `:5-14`: A32 prep, scope DoR, binding, fixed point, end test, sensitivity, assembly, seal, then comparison; no gate lifted here. |
| `STAGE8_TASK5_LICENSED_CONDITIONAL_CHAIN_LANE2_V004.md` | `1da746c3956c6b23e17ce10c8bb5ff8e902f7afcf97c3d4eb8d717d7fd7c541a` | `:252-343`: Step 0 + twelve-step map; local product/threshold chain remains conditional and unexecuted. |
| `STAGE8_TASK5_CHAIN_CONFORMANCE_AUDIT_LANE3_V002.md` | `44202c060821728fba2c46b81b82487002e639f3242565b7a5fed387e41fcae8` | lead board: old `p_loc` route is LOCAL_SHADOW; period route CARRIED_CONDITIONAL; residues 3/6/9/12; both A7 branches retained; no number. |
| `DOR_020_A7_EC_BRANCH_CARRIED_2026-08-05.md` | `834e46029a292122c1e4c604af4f3e3249e6a9ee2638255464685623fba5eb8f` | `:5-21`: ZERO and IDENTITY branches are carried for future per-branch computation with no selection; exit from the certified lattice voids that branch's carriage. |
| `DECISION_SEQUENCED_PROGRAM_2026-08-06.md` | `eaeffd37982cc0063a42095a6880c34d6a95a95b7240cd02b61e485f4b17482a` | `:12-15`: every cross-sector supplier declares its unit; no invisible dimensionless parameter. |

The local product's exact retained mathematical form is

```text
chi_K^loc := p_loc[Rhat_K],
A_loop^loc := sup_(K in D) |a_loop^loc(K)|,
q_loop^loc = |chi_K^loc| A_loop^loc,                       (M0)
```

on its declared local-reader scope and modulus certificate. `(M0)` is not an
identity with the global harmonic pairing or period.

The carried A7 index is

```text
epsilon in {ZERO, IDENTITY},

ZERO:      E_C,RL c_RL = 0,
IDENTITY:  E_C,RL c_RL = c_RL.                            (M1)
```

No branch, route, address, or member is selected in this artifact.

### 2.2 Display of the public-schema tensions

The required and published field sets are, respectively, from incorporated V000
item 3 as ratified through V002 and from source 14:

```text
S_req := {
  registry_record_id,
  definition,
  value_or_masked_handle,
  units,
  uncertainty_or_covariance,
  kinematic_or_domain,
  source_identifier,
  timestamp_or_version,
  provenance_URL
};

S_pub := {
  definition,
  domain,
  record_id,
  source_id,
  units
}.                                                           (M2)
```

Therefore

```text
S_req \ S_pub contains at least {
  value_or_masked_handle,
  uncertainty_or_covariance,
  timestamp_or_version,
  provenance_URL
},                                                           (M3)
```

and the published `domain` is an empty default rather than exhibited kinematic
metadata. The public exclusion file is empty. It follows that:

```text
required response schema exhibited                     = false;
missing-required-key -> machine exclusion exhibited    = false;
canonical_id over the required canonical source record = unproved. (M4)
```

The public ID hashes `S_pub`; no sealed alias/default theorem identifies that
record with `S_req`. These are implementation tensions, not a claim that the
ratified rules are malformed.

For uncertainty timing:

```text
measurement uncertainty is inside the concealed commitment payload;
eligibility and beacon selection precede reveal;
preselection availability/typing rule = absent.             (M5)
```

Task-6 sensitivity can supply theory-side uncertainty; it cannot by itself
supply the missing preselection measurement-metadata bridge.

To prevent the old “attain A32” / new “A32 preparation” wording from creating a
circular board, define the completion subgate of Task-6 Step 1:

```text
A32_PRE_EVALUATION_READY :=
  instrument_ratified
  and schema_and_canonical_ID_tensions_resolved
  and current_scalar_commitment_qualification_carried
  and executable_eligibility_and_comparator_interfaces_frozen
  and HOLDOUT-UNIVERSE-SEAL
  and immutable_all_eligible_ID_prediction_map_code
  and PREDICTION-MAP-SEAL
  and every type in (O2) preserved.                         (M5a)
```

`(M5a)` is a **Step-1 completion subgate**, before the Step-2 scope DoR and
before any numerical execution. It is not Task-6 Step 8. Step 8 later seals the
number and prediction outputs produced through the already-sealed interface.
This relay drafts the instrument only, so `A32_PRE_EVALUATION_READY=false`.

### 2.3 The twenty-row mapping

`SATISFIABLE-AS-INHERITED` means the inherited stock can meet the row without a
new Task-6 mathematical construction; it does **not** mean the corresponding
ladder seal is true. `NEEDS-A-TASK-6-STEP` identifies the later board step that
must supply or execute the row. `IN-TENSION` means the present record cannot yet
certify the row without resolving the displayed mismatch.

| ID | Live obligation | Inherited-state verdict | Exact Task-6 consequence |
|---|---|---|---|
| M1 | exact query/pagination/retry/rate/failure rule; no manual additions | **SATISFIABLE-AS-INHERITED** | Public collector/transcript stock exhibits the fixed one-artifact retrieval and machine path. This is not a universe seal. |
| M2 | frozen cutoff/vintage; unparseable supplied version excluded | **SATISFIABLE-AS-INHERITED** | CODATA 2022 vintage is already ratified and carried. |
| M3 | full response schema | **IN-TENSION** | `(M2)-(M4)` show the public five-field record does not exhibit the required schema. A schema-conforming rebuild or sealed lawful bridge is required inside the Step-1 completion subgate `(M5a)`, before Step 2. |
| M4 | canonical field mapping; missing required key machine-excluded, never hand-repaired | **IN-TENSION** | Missing fields were not mapped and the exclusions file is empty. A sealed mapping/default rule or rebuilt collector output is required. |
| M5 | RFC-8785 canonical JSON | **SATISFIABLE-AS-INHERITED** | The current all-string canonical records have deterministic serialization; any repaired schema must rerun canonicalization inside `(M5a)`. |
| M6 | canonical ID over the required value-free canonical source record | **IN-TENSION** | Current IDs hash `S_pub`, not the full `S_req` record. `(M5a)` must regenerate them or prove exact equivalence; no result-dependent alias is permitted. |
| M7 | deterministic dedup with complete suppression report | **SATISFIABLE-AS-INHERITED** | Collector stock carries deterministic clusters and reports. |
| M8 | raw bytes/hashes, canonical/exclusion/duplicate outputs, collector hash, transcript | **SATISFIABLE-AS-INHERITED** | These stock artifacts exist; their presence does not assert eligibility or seal status. |
| M9 | independent salted custodian commitments and no-disclosure attestation | **IN-TENSION** | Q-25 accepts concealment but records permanently that process independence and independent attestation were never established. Every headline carries that limitation. Current scalar covariance is vacuous; a vector extension must revise/recommit before prediction. |
| M10 | future-beacon selection only after PREDICTION-MAP-SEAL; lowest frozen hash; no discretion | **NEEDS-A-TASK-6-STEP** | The Step-1 completion subgate creates the prerequisite map seal and freezes the selector; the future beacon may select only after that seal and without unmasking. Step 9 retains contamination/unmask custody. No target is selected here. |
| M11 | full-lineage contamination audit before unmask; prior access fails | **NEEDS-A-TASK-6-STEP** | Q-27 fixes the scope; Step 9 executes the audit before unmasking and reports roots/file lists. F-U1/F-U2 remain. |
| M12 | immutable all-eligible-ID prediction-map interface and typed payload before evaluation | **IN-TENSION** | No map or seal exists, and “A32 prep” is not attainment. `(M5a)` must seal the code before Step 2 or any numerical execution. The map must preserve `(O2)`, `(M0)`, both `(M1)` branches, seven CARRY-1 rows, falsifiers, and units. |
| M13 | theory/comparator/measurement uncertainty and covariance from frozen sources | **IN-TENSION** | `(M5a)` must freeze a lawful preselection measurement-metadata bridge; Step 6 may later produce theory sensitivity and Step 7 assemble it through that frozen interface. `(M5)` is not repaired by sensitivity alone. Scalar-only qualification remains. |
| P1 | fixed public registry/API source and observable universe basis | **SATISFIABLE-AS-INHERITED** | NIST CODATA 2022 fixed-vintage source is ratified; all candidates still undergo eligibility. |
| P2 | drand primary, NIST fallback, frozen timing/parser/mirrors, fail closed | **NEEDS-A-TASK-6-STEP** | `(M5a)` freezes the metadata and map-seal instant that determine the future round; retrieval occurs only at the governed post-seal time under the 24/72-hour rule. No beacon is read here. |
| P3 | published same-alpha QED/SM comparator, citable before universe construction, fixed formula/order | **IN-TENSION** | Five current families lack a formula payload; the sixth is refuted by Q-28. No source establishes that a published physical comparator consumes `LOCAL-SHADOW` faithfully. |
| P4 | identical alpha input and metadata under `alpha(0)=1/(4 pi kappa_Thomson)`; no refit/coefficient/post-selection | **IN-TENSION** | The inherited product is `LOCAL-SHADOW`, not `kappa_Thomson`, global period, or alpha. A32 may not erase this type. A candidate lacking an exact domain bridge is ineligible. |
| P5 | fixed symbolic distinctness rule `D>=5`, never renegotiated; empty fails | **NEEDS-A-TASK-6-STEP** | Steps 6-7 supply frozen prediction/uncertainty payloads; Step 9 evaluates only after sealing. The one-sided seed rider means an out-of-lattice zero is not relabeled a negative prediction. |
| P6 | all machine-enumerated eligible candidates; no human subfamily; five sealed eligibility conjuncts; empty fails | **NEEDS-A-TASK-6-STEP** | `(M5a)` must freeze the exhaustive eligibility implementation and all-ID future-output map before Step 2. Later payload assembly uses that code without changing it. Current six-family screen is empty, and eligibility is unexecuted. |
| A20 | Q-28 comparator-precision clause 3 before beacon; no measured central value | **NEEDS-A-TASK-6-STEP** | `(M5a)` must freeze a pre-beacon executable clause. If the clause cannot be applied from frozen non-central-value metadata, F-C3 withdraws it and readiness fails; the clause is not deferred, softened, or fitted. |

The counts are displayed rather than inferred from prose:

```text
SATISFIABLE-AS-INHERITED = {M1,M2,M5,M7,M8,P1}                 = 6;
NEEDS-A-TASK-6-STEP      = {M10,M11,P2,P5,P6,A20}              = 6;
IN-TENSION               = {M3,M4,M6,M9,M12,M13,P3,P4}        = 8;
TOTAL                    = 6+6+8                               = 20. (M6)
```

### 2.4 Consequence for the Task-6 board

[PROVABLE] The inherited state supports an A32 **application draft**, not an
A32 pass:

```text
Task6_Step1a -> this relay drafts the exact binding only;

Task6_Step1b -> after review/principal ratification, separately construct and
                evaluator-certify (M5a); if false, STOP before Step 2;

Task6_Step2 -> only after (M5a), state the conditional
               LOCAL / LOCAL-SHADOW scope; the DoR does not erase a type;

Task6_Step3 -> binds only under the later authorization and no-selection rules;

Task6_Step4_5 -> execute per retained branch only after applicable
                 pre-evaluation gates; seed-zero emits OUT_OF_LATTICE,
                 never an invented refutation value;

Task6_Step6 -> supplies theory sensitivity per branch;

Task6_Step7 -> assembles actual typed branch payloads and sensitivities through
               the already-sealed schema/map/comparator interfaces;

Task6_Step8 -> seals the assembled number and selected prediction output;
               it does NOT create the prerequisite prediction-map seal;

Task6_Step9 -> contamination, governed unmask, and comparison only after
               the required result seals.                              (M7)
```

If a required row remains in tension, the corresponding descendant fails
closed. The current all-three-condition screen being empty is not permission to
relax a rule, select a favorable branch, or strip the shadow type.

## 3. B3 — principal ratification instrument, drafted

The following is the exact draft submitted for review. It binds existing A32
conditions to the certified Task-5 subject; it does not add a physics law,
candidate, comparator, number, branch selector, or threshold.

> ### TASK-6 A32 APPLICATION AND TYPE-BINDING INSTRUMENT
>
> **DRAFT — NOT RATIFIED — NO GATE LIFT**
>
> I ratify only the binding below of the already-ratified A32 procedure to the
> Task-5-certified computation. This act does not declare A32 attained, create
> `HOLDOUT-UNIVERSE-SEAL`, `PREDICTION-MAP-SEAL`, `ALPHA-RESULT-SEAL`,
> `HOLDOUT-RESULT-SEAL`, or `FINAL-CLAIM-SEAL`, authorize numerical evaluation,
> bind a member, execute a fixed point or end test, compute a number, compare
> with a measured central value, or change a protected flag.
>
> **SUBJECT.** The only admitted subject is the certified V004 local chain with
> every displayed gate and certificate inherited. Its product carries:
>
> ```text
> COMPUTATION_SCOPE = LOCAL
> PRODUCT_TYPE = LOCAL-SHADOW
> TRIAL = ONE-SIDED_ON_CURRENT_FINITE_CHI_LATTICE
> PERIOD_NATIVE = false
> ```
>
> The product may be evaluated only under a later, separate evaluation DoR and
> after the applicable pre-evaluation A32 conditions below are true. It may not
> be renamed a global period, holonomy charge, period-native Maxwell quantity,
> `kappa_Thomson`, physical alpha, or a two-sided trial.
>
> **TYPE PRESERVATION.** The sealed theory-output record, immutable A32
> prediction map, and every prediction payload shall preserve without deletion
> or weakening:
>
> 1. `LOCAL-SHADOW`;
> 2. the one-sided rider: a nonzero seed may confirm inside the licensed local
>    lattice, while seed zero is a pole/out-of-lattice condition and is not a
>    negative verdict;
> 3. the period cure only as `CARRIED-CONDITIONAL`, requiring a formed period
>    route and the true `d^per` modulus certificate;
> 4. all seven CARRY-1 rows at their sealed verbs;
> 5. both A7 branches, ZERO and IDENTITY, carried now and, if later computed,
>    computed and reported per branch, with neither selected, averaged, merged,
>    or dropped;
> 6. every open premise and armed falsifier; and
> 7. every required cross-sector-unit factorization in the propagation trace,
>    with no conversion silently set to one.
>
> No aggregate branch verdict is created by this instrument. If the
> prediction-map schema cannot carry both branches, that is an unresolved gate,
> not permission to choose one. If a branch exits the licensed local lattice,
> no value is invented; the payload records `OUT_OF_LATTICE` or noncomputable.
>
> **PRE-EVALUATION A32 CONDITIONS.** Before numerical evaluation is authorized:
>
> - the V002 freeze and its incorporated thirteen mechanical items remain fixed;
> - the exhaustive registry snapshot, schema, serialization, canonical IDs,
>   deduplication, reports, commitments, and eligibility implementation meet
>   their live clauses;
> - eligibility applies complete-lineage `unused`, computability with no fit or
>   new coefficient, independent-value and non-alpha requirements, structure
>   sensitivity, and Q-28 comparator precision before beacon selection;
> - every eligible candidate has a preregistered same-alpha comparator or is
>   ineligible;
> - an empty eligible set fails closed;
> - `HOLDOUT-UNIVERSE-SEAL` and immutable `PREDICTION-MAP-SEAL` exist;
> - the prediction map covers every eligible ID and preserves all typing above;
> - no measured central value is consulted; and
> - M3/M4/M6/M12/M13/P3/P4 are discharged by sealed witnesses or return
>   fail-closed; M9 is carried exactly as Q-25's accepted permanent limitation,
>   never restated as independent custody proved.
>
> `LOCAL-SHADOW` is not promoted by passing through A32. If no public observable
> and comparator can consume it faithfully, the candidate fails computability
> or structure sensitivity, and the eligible set may fail closed.
>
> **MASKING QUALIFICATION.** Every A32 headline and any `FINAL-CLAIM` shall state:
> cryptographic concealment is accepted, but process independence between
> collector and custodian was never established and no independent attestation
> exists.
>
> The present collector is confined to the scalar fixed-column universe. Any
> vector or multicomponent extension requires collector revision and
> recommitment before any prediction exists.
>
> **ORDER.** This draft is Task-6 Step 1a. Before Step 2, a separate Step-1
> completion act must ratify this instrument, construct the pre-evaluation A32
> rails, and evaluator-certify `A32_PRE_EVALUATION_READY` as defined in `(M5a)`.
> If that predicate is false, the board stops before the evaluation DoR. Only
> after it is true may a separate principal evaluation DoR declare the
> conditional `LOCAL / LOCAL-SHADOW` scope. Member binding, fixed-point
> execution, end test, sensitivity, assembly, and result sealing then retain the
> escrow order. Task-6 Step 8 seals the resulting number/prediction output; it
> does not retroactively create the prerequisite prediction-map seal.
> Comparison occurs only after the governed result seal. Future beacon
> selection, selected-prediction sealing, custodian unmasking, and
> commitment/contamination checks occur only at their V011 positions.
>
> A32 alone authorizes none of those acts. `proof_authorized` remains equivalent
> only to `FINAL-CLAIM-SEAL`.
>
> **FAIL CLOSED.** F0-F7, the four A9-era falsifiers, A4/A5 voids,
> counterexample regressions, F-U1/F-U2/F-C3, and every A32 failure remain armed.
> Prior outcome access, an empty eligible set, registry/universe drift, failed
> commitment, beacon substitution, duplicate ambiguity, identical comparator
> prediction, post-unmask map editing, type erasure, undeclared cross-sector
> conversion, or branch/route/member selection fails the appropriate gate.
>
> A wrong result for one future bound member refutes that instance. It does not
> refute the whole family without a separate rigidity theorem.
>
> ```text
> alpha_computed = false
> proof_authorized = false
> kappa_record_computed = false
> ```

### 3.1 Why the instrument is binding-only

Every field in the draft has a source:

```text
canonical A32 mechanics               <- V000 incorporated by V002;
registry/beacon/comparator/threshold   <- V002;
seal order and all-ID map              <- sealed packet V011;
permanent masking qualification        <- Q-25;
unused + precision clause              <- Q-27/Q-28;
LOCAL-SHADOW + one-sided rider          <- Task-5 certification/audit;
CARRY-1 + both A7 branches              <- Task-5 certification/A7;
cross-sector-unit declaration           <- sequenced-program decision;
Task-6 order                             <- escrow decision.            (I0)
```

The only new act is the proposed conjunction of those existing fields on one
named subject. The draft is `[YOURS]`; every mathematical and procedural premise
inside it retains its source verb.

## 4. Surface anchor

### 4.1 Named actual objects

The preparation is anchored on the following actual objects, not schematic
replacements:

| Object | Anchor result |
|---|---|
| sealed packet V011 bytes `aa7c6d49...` | **PASS** — base DAG and A32 rules consumed at their sealed byte version. |
| ratified V002 bytes `32dbfc33...` | **PASS** — exact ratified freeze and incorporation consumed. |
| current public bootstrap as recorded in source 14 | **PASS AS EVIDENCE ONLY** — its five-field schema, collection count, output hashes, and unsealed eligibility state are carried; no candidate content or custodian-private payload is opened. |
| Task-5 certification `fc2ed586...` | **PASS** — only its certified local-chain, shadow, rider, branch, and fence strengths are consumed. |
| local product `(M0)` | **PASS AT LOCAL TYPE** — no global-period or Thomson interpretation is added. |
| A7 branch family `(M1)` | **PASS AS CARRIED FAMILY** — both labels retained, neither chosen. |

### 4.2 Geometry / rails split

```text
GEOMETRY / PHYSICS SUBJECT
  local reader product q_loop^loc;
  LOCAL-SHADOW type;
  one-sided seed rider;
  CARRY-1 rows;
  A7 branch index;
  explicit cross-sector units;

RAILS / A32 PROCEDURE
  registry and canonical record;
  commitments and qualification;
  eligibility and comparator;
  prediction-map code and seals;
  beacon, contamination, unmasking;
  seal DAG and final authorization.                         (SA0)
```

The rails neither derive nor upgrade the geometry. The geometry neither waives
nor repairs a failed rail.

### 4.3 R9-lesson quantification check

The instrument quantifies exactly over:

```text
every machine-enumerated eligible canonical ID;
each certified A7 branch carried by the named Task-5 subject;
each later lawfully bound member within its actual family scope. (SA1)
```

It does not quantify universally over an orientation orbit, a phantom common
member, an unformed period route, or a class A8/A9 did not name. No equality is
required across different branches. A comparison is formed only when the two
routes or payloads exist on the same lawful subject. The nondegenerate R9 lesson
is therefore preserved.

`SURFACE_ANCHOR = present`.

## 5. Dependency re-audit

Every argument depending on a draft clause was re-walked after the clause was
stated:

| Draft clause | Upstream dependency | Re-audit result |
|---|---|---|
| subject = V004 local chain | certification §III + audit V002 | Keeps `LOCAL-SHADOW`; no period equality inserted. |
| one-sided rider | certification §I.8-9 | Seed zero remains out of the finite-chi lattice; no negative verdict invented. |
| both branches | A7 + certification | Payload is branch-indexed; no average, selection, or cross-branch equality. |
| all seven CARRY-1 rows | certification §I.5 / membership V002 as certified | Exact carried verbs remain; no TYPE-U family called inhabited. |
| all-ID prediction map | V000 item 12 + sealed V011 | Map remains missing and pre-evaluation; draft does not call it built. |
| schema/ID obligations | source 14 + `(M2)-(M4)` | Three separate tensions retained; canonicalization does not launder missing fields. |
| uncertainty | V000 item 13 + source 14 | Theory sensitivity and preselection measurement metadata remain separate debts. |
| comparator/calibration | V002 + source 12 | Physical shared-alpha token is not replaced by shadow output. |
| Q-28 | principal decision | Applied before beacon and without measured central value; F-C3 retained. |
| masking qualification | Q-25 | Original independence fact is not rewritten as satisfied. |
| cross-sector units | sequenced decision | Propagation trace must name each conversion; absence blocks, never defaults to one. |
| sequence | sealed V011 + escrow | Pre-evaluation and post-alpha halves remain separated; preparation is not attainment. |
| authorization | sealed V011 + A34 | `proof_authorized` remains iff `FINAL-CLAIM-SEAL`; no earlier object inherits that verb. |

No dependent formula changes. No candidate is made eligible. No comparator is
selected. No branch is collapsed. No seal or flag changes.

`DEPENDENCY_REAUDIT = DISPLAYED`.

## 6. Battery

### 6.1 F_PLDEC

The physical reader is not used to decide the procedure:

```text
A32 source/query/cutoff/schema/commitment/beacon/threshold
  are fixed without ell, p_loc[Rhat_K], q_loop^loc,
  a seed result, a branch result, or a desired number;

q_loop^loc enters A32 only as a future typed payload subject;

no A32 rule is inferred from q_loop^loc;
no period or Thomson identity is inferred from reader normalization. (B0)
```

The false-anchor shadow is therefore absent. `F_PLDEC = PASS`.

### 6.2 Anti-tuning ledger

| Possible tuning channel | Fixed response |
|---|---|
| registry/source/cutoff | Ratified before the Task-6 subject. |
| canonical fields and IDs | Missing fields are tensions; they are not filled after seeing an output. |
| threshold | Symbolic `D>=5` remains fixed; no renegotiation. |
| current empty screen | Fails/needs future lawful candidates; no clause relaxation. |
| comparator | Exact published identity/order/domain required; no nearest analogue or refit. |
| LOCAL-SHADOW label | Propagated into every payload; never stripped to gain eligibility. |
| one-sided result | Out-of-lattice stays out-of-lattice; no invented negative value. |
| A7 branches | Both carried for future per-branch computation; no favorable-branch choice. |
| member/route | No member or route selected here. |
| uncertainty | Frozen source and trace required; no post-result inflation or shrinkage. |
| measured central value | Not consulted by eligibility or this artifact. |
| cross-sector unit | Every conversion declared in advance; no invisible unit equal to one. |
| failed gate | No residual patch or target comparison may repair it. |

`ANTI_TUNING = CLEAN`.

### 6.3 Cross-sector-unit row

The A32 propagation trace must carry any actual conversion as

```text
U_cross : Carrier_source -> Carrier_target,
domain(U_cross), codomain(U_cross), units(U_cross),
covariance(U_cross), and source hash.                       (B1)
```

If no cross-sector arrow is consumed, the payload states
`CROSS_SECTOR_UNIT = not_applicable`. If one is consumed and `(B1)` is absent,
assembly and sealing stop. This artifact declares no value for `U_cross`.

### 6.4 Failure ladder

The following remain failure-capable:

```text
authority/hash drift;
schema/ID mismatch;
no independent-custodian qualification on a headline;
vector candidate without pre-prediction recommitment;
F-U1 or F-U2;
F-C3;
empty eligible set;
changed universe or prediction map;
prior outcome access;
commitment failure;
beacon substitution;
duplicate ambiguity;
identical comparator prediction;
type erasure;
undeclared cross-sector conversion;
branch/route/member selection;
post-unmask edit;
any attempted numerical execution before its gate.          (B2)
```

No item in `(B2)` is tested by a desired numerical consequence.

### 6.5 Self verb audit

| Verb used here | Display supporting it | Audit |
|---|---|---|
| `located` / `verified` | fifteen-row source census with attachment form and hash | clean |
| `ratified` | V002 and principal decisions only | clean |
| `incorporated` | V002 exact V000 range/hash | clean |
| `consolidated` | `(O0)` and the twenty-row mapping | clean |
| `satisfiable as inherited` | rows M1/M2/M5/M7/M8/P1; no seal claimed | clean |
| `needs` | named Task-6 step per row | clean |
| `in tension` | `(M2)-(M5)` plus M9/M12/P3/P4 displays | clean |
| `carried` | certification, CARRY-1, A7 source | clean |
| `drafted` | complete quoted instrument | clean |
| `fails closed` | sealed V011/V002/Q-28 rules | clean |
| `attained` | used only under negation | clean |
| `authorized` | used only for future conditional gate or explicit negation | clean |
| `computed` / `evaluated` / `compared` | used only under explicit negation | clean |

No display above calls an unbuilt map built, an unexecuted predicate passed, a
typed family inhabited, a shadow physical, or a preparation an attainment.

## Final board

```text
A32_FREEZE = RATIFIED
A32_PRE_EVALUATION_READY = false
A32_RESULT = UNATTAINED

LIVE_OBLIGATIONS = 20
SATISFIABLE_AS_INHERITED = 6
NEEDS_A_TASK_6_STEP = 6
IN_TENSION = 8

LOCAL_CHAIN = executable_of_record_but_not_executed_here
PRODUCT_TYPE = LOCAL-SHADOW
TRIAL = one_sided_on_current_finite_chi_lattice
A7_BRANCHES = both_carried_no_selection
CARRY_1 = exact
CROSS_SECTOR_UNIT = declared_if_consumed

MEMBER_BINDING = none
FIXED_POINT_EXECUTION = none
END_TEST = none
NUMERIC_EVALUATION = none
MEASURED_CONSTANT_COMPARISON = none

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

A32_SOURCES = 15 located (+hashes: 7995f6fd, 78f6bb08, aa7c6d49, 32dbfc33, 85bacbee, 61c6de58, 13faf0bc, d7153b91, a132f4b2, 89cab162, 84966722, 2dbd3d1e, 8abb4089, 3a1a9d98, bec51293)
OBLIGATIONS = consolidated (+20)
MAPPING = (SATISFIABLE-AS-INHERITED 6; NEEDS-A-TASK-6-STEP 6; IN-TENSION 8)
INSTRUMENT = DRAFTED
VERB_AUDIT_SELF = CLEAN
