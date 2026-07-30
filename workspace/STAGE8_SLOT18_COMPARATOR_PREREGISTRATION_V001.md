# Stage 8 Slot-18 Comparator Preregistration v001

Date: 2026-07-30

## Result first

**Five of six families do not yet support a formula-level comparator
payload.** The sixth, the electron magnetic-anomaly branch, has a
published formula payload frozen before any theory prediction, but Q-28 now
refutes that precision branch under the third admissibility clause. The
payload is retained as a preregistration and refutation record; it is not a
live Slot-18 comparator path. Zero of the six current families satisfies all
three conditions today; the eligibility stage has not been executed.

This record does not attain A32. Q-27 now identifies `unused` with the sealed
historical-lineage clause, but no candidate-specific lineage test is run here.
No expression is evaluated, no comparator mean or uncertainty value is
produced, no distinctness statistic is computed, and no candidate is declared
eligible.

### Standing A32 qualification

The Q-25 registration in
`STAGE8_SLOT18_Q23_Q28_GOVERNING_REGISTRATION_V001.md:236-259` records:

```text
THE LIMITATION IS PERMANENT AND
MUST TRAVEL WITH EVERY A32 HEADLINE
...
process independence between
collector and custodian was never established, and no independent attestation exists.
```

That permanent custodian-independence qualification accompanies this
comparator preregistration and any later A32 or FINAL-CLAIM use of it.

## Governing comparator contract

Sources consumed by this record, typed by role:

```text
RATIFIED AUTHORITY:
/Users/bgm/MB Work/alpha_supervision/A32_FREEZE_V002_RATIFIED_2026-07-28.md
SHA-256: 32dbfc33b4f07407903ec014627ea64de57b5b1a6dc017dd27c6504729c3a327

PROPOSAL PROVENANCE FOR THE RATIFIED WORDING:
/Users/bgm/MB Work/alpha_supervision/A32_SIX_ITEM_PROPOSALS_2026-07-28.md
SHA-256: 5185ad0f5e7097fe0e0886e61771fc57e49f169f034cc52cc7c9bf11543c07ea

PUBLIC COLLECTION-TIMING EVIDENCE:
/Users/bgm/MB Work/a32_holdout/transcript.md
SHA-256: 4052a842203204798b527246acc02e0768b06a33d76407c063c17ee1b40bb7cd

CURRENT APPEND-ONLY QUESTION REGISTER:
/Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md
SHA-256: 2bf6a21f4d70d63a85e3f11d347a21954143dd7a2b3301cc2ab49a7dde0098bb

CONTROLLING SLOT-18 ADMISSIBILITY AUTHORITY:
/Users/bgm/MB Work/alpha_supervision/SLOT18_ADMISSIBILITY_PRINCIPAL_DECISION_2026-07-30.md
SHA-256: a132f4b2421610c7df4e9a8746286999b31672f1f2d805588ed3f1ad81ad6259

SUPPORTING REFUTATION FINDING:
/Users/bgm/MB Work/alpha_supervision/FINDING_D_TEST_DEGENERATE_ON_PRECISION_OBSERVABLES_2026-07-30.md
SHA-256: 34f9f9658f9aae1632de23ba470e0de8c82eb91666c50e91f2d8e516568d7f4a
```

The ratified comparator rule says at
`/Users/bgm/MB Work/alpha_supervision/A32_FREEZE_V002_RATIFIED_2026-07-28.md:67-74`:

```text
published
standard-theory (QED/SM) expressions, citable BEFORE candidate-universe construction,
evaluated with the identical alpha input
under the frozen convention
alpha(0) = 1/(4 pi kappa_Thomson),
perturbative order FROZEN PER FORMULA at
preregistration, no candidate-specific fitted parameter, refit, channel coefficient, or
post-selection
...
A candidate with no published standard expression is ineligible FOR THAT
CANDIDATE.
```

The admissibility condition at V011:2083-2089 additionally requires:

```text
be computable from the sealed BID output with no new fitted parameter,
channel-specific coefficient, or post-selection;
...
and be structure-sensitive: BID and at least one preregistered comparator
calibrated to the same alpha must make distinct predictions.
```

The uncertainty source is fixed by V011:2025-2030:

```text
comparator uncertainty from preregistered comparator payloads only;
measurement uncertainty/covariance from the custodian commitment payload
```

The scalar distinctness rule at V011:2052-2058 is not evaluated here.

## Timing resolution and freeze point

The earlier V011 wording says `cited before` at V011:2042-2050. The later
ratified A32 authority says `citable BEFORE`. Its proposal provenance makes
that reading explicit at
`/Users/bgm/MB Work/alpha_supervision/A32_SIX_ITEM_PROPOSALS_2026-07-28.md:55-64`:

```text
for each candidate observable,
the standard QED/standard-model expression as published in citable literature BEFORE
candidate-universe construction
```

The selected report identifies its publication date on its first page:
P. J. Mohr et al., *J. Phys. Chem. Ref. Data* 54, 033105 (2025), DOI
`10.1063/5.0279860`, “Published Online: 16 September 2025.” The public
collection transcript records collection on 2026-07-28 at
`/Users/bgm/MB Work/a32_holdout/transcript.md:10-23`. Thus the expression was
published in citable literature before candidate-universe construction.

The current seal state remains pre-prediction.
`provenance/boundary_incidence_dynamics_preregistration_v011.json:651-658`
states:

```text
"prediction_map_sealed": false,
...
"holdout_result_sealed": false,
"BID_final_claim_sealed": false,
"external_unused_holdout_preregistered": false
```

Therefore this record freezes the concrete formula, order, input convention,
uncertainty source, and units before a prediction exists. It does not claim
that the older V011 word `cited` was satisfied; the later ratified `citable`
rule controls this payload.

## Global execution contract, frozen without values

If a future candidate reaches a row marked `FORMULA_AVAILABLE`, its comparator
runner must obey all of the following:

1. **Shared alpha token.** Accept one symbolic serialized `alpha(0)` input from
   the sealed theory-output record under the ratified convention
   `alpha(0) = 1/(4 pi kappa_Thomson)` and pass the identical byte sequence to
   BID and comparator. The input record must carry both the symbolic token and
   that convention identifier; a bare token named `alpha(0)` is insufficient.
   The comparator must not load an independently inferred alpha. No alpha
   value appears in this record.
2. **Conditional theory uncertainty.** Treat the shared alpha token as the
   fixed calibration input for the distinctness comparison. `sigma_comp`
   includes only the fixed publication's intrinsic theory uncertainty,
   excluding uncertainty in the shared alpha input. Otherwise a shared-input
   covariance rule would be required but is not presently frozen.
3. **Candidate identity.** Require exact agreement of observable definition,
   particle/species, kinematic point, normalization, and units. No nearest
   analogue is substituted.
4. **Fixed vintage and order.** Use only the publication/version and order
   named below. No later coefficient replacement, per-candidate order choice,
   refit, or channel coefficient is allowed.
5. **Units.** Convert only by a deterministic conversion explicitly named in
   the publication payload. Missing or ambiguous conversion fails closed.
6. **Scalar-only present collector.** A vector or multi-component comparator
   fails closed under the Q-25 forward condition until a revised collector has
   committed its covariance before any prediction.
7. **Third admissibility clause.** Before beacon selection, require that the
   comparator's predictive uncertainty not be so far below a plausible BID
   deviation that a `D >= 5` difference would automatically conflict with
   established measurement. Apply this only as the comparator-precision
   condition Q-28 states; no measured central value may be consulted.

These are execution requirements, not an execution.

## Later admissibility disposition

Q-27 identifies `unused`. The controlling principal decision says at
`/Users/bgm/MB Work/alpha_supervision/SLOT18_ADMISSIBILITY_PRINCIPAL_DECISION_2026-07-30.md:12-27`:

```text
`unused` IS the condition already sealed at
`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:2080-2089` — "be absent as an outcome or target from the
complete historical lineage."
...
a bounded search over the rule-11 scope, returning zero occurrences of the
candidate observable as an outcome or a target.
```

Q-28 then adds clause 3 at `:44-56`:

```text
An observable is admissible only if the comparator's own predictive uncertainty is not so far below
any plausible BID deviation that a `D >= 5` difference would be automatically in conflict with
established measurement.
...
IT IS A CONDITION ON COMPARATOR PRECISION, NEVER ON A MEASURED CENTRAL VALUE.
```

The disposition of this record's only formula payload is explicit at `:75-80`:

```text
Family 6 — the charged magnetic form factor at the electron zero-momentum anomaly — is the one family
holding a comparator payload, and it is the clearest failure of clause 3.
```

The payload below is therefore preserved, not executed or repaired.

Q-28's falsifier at `:63-64` is binding:

```text
if clause 3 cannot be applied without consulting a measured central value, it
breaches the comparison fence and must be withdrawn.
```

F-C3 is not tested here.

## Per-family availability

| Family number (inventory enumeration order) | Theory-output family | Comparator state | Frozen formula/order | `sigma_comp` source | Unit state |
|---:|---|---|---|---|---|
| 1 | Finite global-holonomy response | **MISSING** | None candidate-compatible | Undefined; fail closed | Physical observable and units not mapped |
| 2 | Temporal-plaquette / connected-kernel susceptibility | **MISSING** | None candidate-compatible | Undefined; fail closed | Physical observable, kinematics, and units not mapped |
| 3 | Electric/magnetic flux and retarded response | **MISSING** | No formula frozen: the current unexecuted protocol lacks a fixed candidate, kinematic domain, current normalization, and contact/edge prescription | Undefined; fail closed | Not fixed |
| 4 | Causal-record durability / recoverability | **MISSING** | No quantitative canonical operational quantity is defined yet, so no exact comparator identity can be selected | Undefined; fail closed | No quantitative observable or unit |
| 5 | Charged spectrum / thresholds / nonzero-momentum response | **MISSING / SPLIT** | Elementary charged-fermion masses are independent SM inputs, not same-alpha predictions; other spectrum/threshold and momentum-response branches remain too broadly typed to freeze an exact candidate comparator | Undefined; fail closed | Not fixed |
| 6 | Charged magnetic form factor | **FORMULA PAYLOAD AVAILABLE; BRANCH REFUTED BY Q-28 CLAUSE 3** for an electron zero-momentum magnetic anomaly only | Fixed-vintage CODATA-2022 electron-anomaly prescription: QED terms through `n = 5`, plus its specified weak and hadronic terms | CODATA Eq. (87), frozen as the fixed-vintage intrinsic theory uncertainty apart from alpha-input uncertainty | Dimensionless `a_e` only; no signed-`g` conversion is authorized |

Five rows cannot produce `D` until their comparator and candidate interfaces
are supplied. The sixth has a formula payload but is already ineligible under
Q-28 clause 3. Q-27 resolves the meaning of `unused`; a future candidate would
still have to pass its bounded rule-11 lineage test. No current row satisfies
all prerequisites today, and no eligibility execution is claimed.

## Family evidence and rejection records

### 1. Finite global holonomy — `MISSING`

The current output is limited by
`COMPLETE_QSPEC_FINITE_HOLONOMY_RESPONSE_RESULT_V001.md:131-153`:

```text
It does not establish:
a local transverse or plaquette Maxwell response;
continuum or regulator independence;
packing independence;
...
or proof authorization.
```

The exact Slot-18 bridge is already recorded at
`STAGE8_SLOT18_BOUNDED_SCOPE_INVENTORY_V001.md:655-657`:

```text
a regulator/refinement-independent physical observable
map, an A32-eligible canonical record, a concrete preregistered same-alpha
comparator, and the frozen prediction/uncertainty payload.
```

Because the theory record has not yet defined a physical observable identity,
domain, unit, or uncertainty interface, selecting any external
worldline/effective-action formula would choose a new target rather than match
an already frozen candidate. No comparator is frozen.

### 2. Temporal plaquette / connected kernel — `MISSING`

The required mathematics is
`COMPLETE_QSPEC_TEMPORAL_PLAQUETTE_RESPONSE_RESULT_V001.md:134-149`:

```text
derive the connected translation-invariant many-cell limit
...
the response kernel becomes local at long wavelength;
...
the intensive result is independent of cellulation and packing.
...
Only after that temporal locality gate passes is it meaningful to combine
the result with a spatial magnetic plaquette response
```

The connected-kernel status at
`COMPLETE_QSPEC_CONNECTED_KERNEL_LOCALITY_DIAGNOSTIC_RESULT_V001.md:58-64`
is:

```text
the correct prerequisite for a later temporal-gradient/Maxwell comparison; it
is not itself that comparison.
```

Because this result is expressly a prerequisite rather than the physical
comparison, there is no frozen observable identity against which an external
formula can be matched. No comparator is frozen.

### 3. Flux / retarded response — `MISSING`

The present object is not executable. 
`FINITE_RECORD_CELL_FLUX_RESPONSE_PROTOCOL_V001.md:3-8` says:

```text
This is a preregistered evaluation protocol, not a specification of the
microscopic record cell. It may run only after one complete finite
spacetime-plus-internal `Q_cell` has been derived, sealed, and passed through
the provenance gate.
```

The same protocol requires at `:75-76`:

```text
The Lorentzian continuation and CTP retarded Hessian must be derived from the
same microscopic functional. A Euclidean equality alone is insufficient.
```

Because the current protocol fixes none of the eventual canonical observable,
momentum/domain metadata, contact/edge prescription, or output units,
selecting an external response formula would select the candidate rather than
match an already frozen candidate. No comparator is frozen.

### 4. Causal-record durability / recoverability — `MISSING`

The current object is defined at
`CAUSAL_DIRECT_LIMIT_RECORD_PRINCIPLE_V002.md:13-18`:

```text
Its durability consists jointly of thresholded
source nonreturn and exact completed-record persistence; its public content
is the recoverable quasi-local record state and central sequence.
```

The missing bridge is recorded at
`STAGE8_SLOT18_BOUNDED_SCOPE_INVENTORY_V001.md:752-754`:

```text
a quantitative operational observable, the missing
continuum/concurrency bridge if load-bearing, a public canonical candidate,
and a published same-alpha comparator.
```

No quantitative canonical observable, domain, uncertainty, or unit exists
yet. An exact-identity comparator cannot be selected before that object is
defined. No comparator is frozen.

### 5. Charged spectrum / thresholds / momentum response — `MISSING / SPLIT`

V011:1592-1605 requires the future complete charged specification to include:

```text
the regulator-removal and locality theorem;
the Ward identity and transverse physical quotient;
the derived charged spectrum and every threshold entering the response;
decoupling and matching rules;
```

For an elementary charged-fermion mass candidate, the 2025 Particle Data Group
Standard Model review, Sec. 10.2.3, printed p. 7, states:

```text
Only the nine fermion masses ... and four independent variables ...
are "physical" and have to be taken from experiment.
```

Publication:
`https://pdg.lbl.gov/2025/reviews/rpp2025-rev-standard-model.pdf`,
S. Navas et al., *Phys. Rev. D* 110, 030001 (2024) and 2025 update.
Using that candidate mass itself as a comparator input would be a
candidate-specific identity, not a distinct same-alpha prediction. This
finding does not classify every charged composite, bosonic, or bound-state
mass.

For every remaining spectrum, threshold, or momentum-response branch, the
current family has not fixed the species, momentum/domain record, current
normalization, mass and threshold inputs, or canonical observable. Therefore
no exact-identity formula/order/uncertainty payload can be frozen. Within this
scoped family inspection, this is a missing-interface finding, not a claim that
related QED formulae do not exist.

### 6. Electron magnetic anomaly — fixed payload, candidate branch refuted

The theory does not yet claim this output. 
`BID_CONSOLIDATED_HOSTILE_AUDIT_MATRIX_V005.md:71` states:

```text
No finite-cell frequency, anomalous moment, mass, or alpha evidence is claimed.
```

V011:1061-1065 also excludes relabeling a primitive coefficient:

```text
It is not an anomalous magnetic
moment and is not extracted from a scalar effective action.
```

The comparator payload remains formula-complete as a frozen audit record:

```text
comparator_id =
  CODATA_2022_FIXED_VINTAGE_ELECTRON_ANOMALY

publication =
  P. J. Mohr, D. B. Newell, B. N. Taylor, and E. Tiesinga,
  "CODATA recommended values of the fundamental physical constants: 2022",
  J. Phys. Chem. Ref. Data 54, 033105 (2025)
  DOI: 10.1063/5.0279860
  URL: https://physics.nist.gov/cuu/pdf/JPCRD2022CODATA.pdf

observable =
  dimensionless electron magnetic-moment anomaly `a_e`

observable_definition =
  publication Eq. (72), definition only

master_expression =
  publication Eq. (74)

QED_series =
  publication Eqs. (75)-(76)

frozen_QED_order =
  n = 1 through n = 5 inclusive

coefficient_payload =
  publication Table XVIII, exactly as printed

weak_and_hadronic_payload =
  publication Eqs. (82)-(85), exactly as printed

alpha_input =
  the identical sealed symbolic `alpha(0)` token used by BID under
  `alpha(0) = 1/(4 pi kappa_Thomson)`;
  no CODATA-adjusted alpha value is loaded

non_alpha_inputs =
  the fixed CODATA-2022 input vintage underlying Eqs. (82)-(85);
  no candidate-specific update or refit

weak_hadronic_alpha_treatment =
  hold the printed Eqs. (82)-(85) additive terms fixed;
  substitute the shared alpha token only in Eq. (75);
  this is a disclosed fixed-vintage convention, not a claim that every
  implicit higher-order alpha dependence vanishes

sigma_comp =
  publication Eq. (87), held as a fixed-vintage constant intrinsic theory
  standard uncertainty apart from uncertainty in the fine-structure constant;
  it is not rescaled as a function of the shared alpha token

units =
  dimensionless `a_e`

allowed_conversion =
  none; the canonical candidate must already be dimensionless `a_e`;
  signed `g_e` and `|g_e|` candidates fail this payload's identity check

later_coefficient_substitution =
  forbidden
```

The publication supplies the master expression at Eq. (74), the QED series at
Eq. (75), and its intrinsic theory-uncertainty statement at Eq. (87):

```text
ae(th) = ae(QED) + ae(weak) + ae(had)                         (74)
...
The QED contribution may be written as
...
The theoretical uncertainty of the electron anomaly (apart from
uncertainty in the fine-structure constant) is dominated by two contributions
```

No term is evaluated here. Q-28 bars this branch as a current Slot-18
candidate. If Q-28 ever reopens, the exact physical electron observable would
still have to be derived from the sealed theory output, with its own
uncertainty, rather than by relabeling an existing scalar coefficient.

The fixed weak/hadronic terms and fixed Eq. (87) uncertainty make this payload
deterministic and auditable, but they are explicit fixed-vintage
approximations. If later authority requires every implicit alpha dependence or
an alpha-dependent recomputation of `sigma_comp`, this payload fails closed;
it may not be silently repaired after a prediction.

## Bounded negative method

Roots searched/reviewed:

```text
physics.nist.gov (NIST/CODATA)
pdg.lbl.gov (Particle Data Group)
journals.aps.org and link.aps.org (APS primary publications/manuscripts)
arxiv.org (primary preprints)
cds.cern.ch (CERN Document Server)
Muon g-2 Theory Initiative official publication index
```

Search families:

```text
QED finite-volume holonomy / Wilson-loop effective action
compact-lattice-QED plaquette susceptibility
Schwinger-Keldysh temporal response
retarded QED polarization / flux response
QED causal record durability / recoverability
SM fermion mass / Yukawa inputs
QED nonzero-momentum vertex and vacuum polarization
electron anomalous magnetic moment theory expression and uncertainty
```

Reviewed publication file list:

```text
https://physics.nist.gov/cuu/pdf/JPCRD2022CODATA.pdf
https://pdg.lbl.gov/2025/reviews/rpp2025-rev-standard-model.pdf
https://arxiv.org/abs/hep-ph/0102185
https://arxiv.org/abs/hep-lat/0011058
https://arxiv.org/abs/hep-lat/9408014
https://arxiv.org/abs/hep-th/0110180
https://arxiv.org/abs/1303.3042
https://arxiv.org/abs/hep-ph/0307295
https://doi.org/10.1103/PhysRevD.83.053002
https://arxiv.org/abs/1205.5368
```

Exclusions:

```text
secondary summaries without a primary equation payload;
measured-outcome pages used as comparator means;
non-QED/SM models;
nearest analogues lacking exact candidate identity;
formulae requiring a candidate-specific fitted coefficient or refit;
formulae lacking a frozen observable/domain/unit/uncertainty interface.
```

This publication screen is discovery evidence only. The five `MISSING`
verdicts above do not assert universal literary absence; they fail closed
because the theory-side canonical observable identity is not yet fixed. The
screen is bounded to those roots, search families, publications, and
exclusions.

## Status

```text
RETURN_VERDICT = MISSING SPECIFICATION
families_reviewed = 6
formula_available_families = 1
formula_payload_missing_families = 5
presently_candidate_compatible_families = 0
unused_identified_with_sealed_lineage_clause = true
third_admissibility_clause_registered = true
electron_anomaly_branch_refuted_by_clause3 = true
current_six_family_all_three_condition_screen_nonempty = false
eligibility_stage_executed = false
empty_eligible_set_declared = false
source_citable_before_universe_construction = true
comparator_payload_preregistered_before_prediction = true
older_V011_cited_wording_claimed_satisfied = false
comparator_expression_evaluated = false
mu_comp_computed = false
sigma_comp_computed = false
D_computed = false
candidate_eligible_declared = false
candidate_ineligibility_recorded = true
measured_value_comparison_performed = false
prediction_attempted = false
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
