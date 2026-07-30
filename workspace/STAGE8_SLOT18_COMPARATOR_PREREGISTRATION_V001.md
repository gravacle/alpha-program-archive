# Stage 8 Slot-18 Comparator Preregistration v001

Date: 2026-07-30

## Result first

**Five of six families have no presently candidate-compatible published
same-alpha comparator.** Only a future electron magnetic-anomaly output has a
formula-level comparator that can be frozen now. Even that positive row does
not establish A32 compliance: the ratified rule required the expression to be
citable before candidate-universe construction, and the universe was already
collected before this record.

This is a formula/payload freeze and a timing finding. It evaluates no
expression, produces no comparator mean or uncertainty value, computes no
distinctness statistic, and declares no candidate eligible.

## Governing comparator contract

`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:2042-2050` states:

```text
Comparators are published standard-theory QED/SM expressions cited before
candidate-universe construction. They are evaluated with the identical alpha
input
...
with perturbative order frozen per formula
at preregistration. No candidate-specific fitted parameter, refit, channel
coefficient, or post-selection is allowed
...
A candidate with no published standard expression is
ineligible for that candidate.
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

## Independent timing defect

The comparator class requires citation **before candidate-universe
construction**. Lane evidence
`STAGE8_SLOT18_BOUNDED_SCOPE_INVENTORY_V001.md:450-476` records both the
requirement and the absence of a concrete instance:

```text
published standard-theory (QED/SM) expressions, citable BEFORE
candidate-universe construction
...
The governing A32 sources name this class, but do not name one concrete
publication, expression, formula version, perturbative order, or comparator
payload.
...
a later silent choice cannot cure the timing defect.
```

The public collection already exists, while
`provenance/bid_stage_subjects_v011.json:22-24` says only that its seal remains
unresolved:

```text
No sealed HOLDOUT-UNIVERSE-SEAL immutable subject exists; A32 public collection artifacts are deployed
```

Therefore the present record is early relative to any theory prediction but
late relative to the literal pre-universe citation clause. It freezes a usable
payload for review; it does not retroactively prove preregistration timing.
Closing that conflict requires a later authority ruling. This lane does not
repair or reinterpret it.

## Global execution contract, frozen without values

If a future candidate reaches a row marked `FORMULA_AVAILABLE`, its comparator
runner must obey all of the following:

1. **Shared alpha token.** Accept one symbolic serialized `alpha(0)` input from
   the sealed theory-output record and pass the identical byte sequence to BID
   and comparator. The comparator must not load an independently inferred
   alpha. No alpha value appears in this record.
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

These are execution requirements, not an execution.

## Per-family availability

| Rank from the Slot-18 inventory | Theory-output family | Comparator state | Frozen formula/order | `sigma_comp` source | Unit state |
|---:|---|---|---|---|---|
| 1 | Finite global-holonomy response | **MISSING** | None candidate-compatible | Undefined; fail closed | Physical observable and units not mapped |
| 2 | Temporal-plaquette / connected-kernel susceptibility | **MISSING** | None candidate-compatible | Undefined; fail closed | Physical observable, kinematics, and units not mapped |
| 3 | Electric/magnetic flux and retarded response | **MISSING** | Published QED response formulae exist as a class, but no formula is compatible with the current unexecuted protocol without a fixed candidate, kinematic domain, current normalization, and contact/edge prescription | Undefined; fail closed | Not fixed |
| 4 | Causal-record durability / recoverability | **MISSING** | No QED/SM operational observable matching the defined record object was found in the bounded primary-source search | Undefined; fail closed | No quantitative observable or unit |
| 5 | Charged spectrum / thresholds / nonzero-momentum response | **MISSING / SPLIT** | Charged masses are independent SM inputs, not same-alpha predictions; momentum-dependent QED expressions are not candidate-compatible until species, domain, current normalization, thresholds, and observable are fixed | Undefined; fail closed | Not fixed |
| 6 | Charged magnetic form factor | **FORMULA AVAILABLE, CONDITIONALLY** for an electron zero-momentum magnetic anomaly only | Fixed-vintage CODATA-2022 electron-anomaly prescription: QED terms through `n = 5`, plus its specified weak and hadronic terms | CODATA Eq. (87), intrinsic theory uncertainty apart from alpha-input uncertainty | Dimensionless `a_e`; Eq. (72) is the only allowed deterministic `g` conversion |

Five rows therefore cannot produce `D` regardless of a future BID mean until
their comparator and candidate interfaces are supplied. The sixth still fails
eligibility unless BID independently derives the same electron observable and
Q-23's `unused` predicate is resolved.

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

The nearest screened QED worldline/effective-action paper was
Gies and Langfeld, arXiv:`hep-ph/0102185`, Eqs. (1)-(4),
`https://arxiv.org/abs/hep-ph/0102185`. It is not the named three-site
relative-history CTP scalar, and no canonical candidate map or
publication-supplied uncertainty for that scalar was identified. No comparator
is frozen.

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

The bounded primary-source screen included arXiv:`hep-lat/0011058` and
arXiv:`hep-lat/9408014`. Their lattice-action observables do not supply a
candidate-level expression, fixed uncertainty, and unit map for this CTP
kernel. No comparator is frozen.

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

The bounded primary-source screen included arXiv:`hep-th/0110180`,
arXiv:`1303.3042`, and QED vacuum-polarization literature. Those formulae are
background-, state-, species-, and kinematics-specific. Because the current
protocol fixes none of the eventual canonical observable, momentum/domain
metadata, contact/edge prescription, or output units, choosing one would
select the candidate rather than preregister its comparator. No comparator is
frozen.

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

The bounded search returned generic QED, circuit-QED measurement-record, and
information-theory uses of "record"; none matched completed-record persistence
or quasi-local recoverability as a published QED/SM observable with an
equation, order, uncertainty, and units. No comparator is frozen.

### 5. Charged spectrum / thresholds / momentum response — `MISSING / SPLIT`

V011:1592-1605 requires the future complete charged specification to include:

```text
the regulator-removal and locality theorem;
the Ward identity and transverse physical quotient;
the derived charged spectrum and every threshold entering the response;
decoupling and matching rules;
```

For a charged-mass or mass-threshold candidate, the 2025 Particle Data Group
Standard Model review, Sec. 10.2.3, p. 6, states:

```text
Only the nine fermion masses ... and four independent variables ...
are "physical" and have to be taken from experiment.
```

Publication:
`https://pdg.lbl.gov/2025/reviews/rpp2025-rev-standard-model.pdf`,
S. Navas et al., *Phys. Rev. D* 110, 030001 (2024) and 2025 update.
Using the candidate mass itself as a comparator input would be a
candidate-specific identity, not a distinct same-alpha prediction.

For the momentum-response branch, the bounded screen included Aoyama et al.,
*Phys. Rev. D* 83, 053002 (2011), Eqs. (8)-(9), DOI
`10.1103/PhysRevD.83.053002`, and Bonciani, Mastrolia, and Remiddi,
arXiv:`hep-ph/0307295`, QED vertex form factors at arbitrary momentum
transfer. These are possible formula classes only. The current family has not
fixed the species, momentum/domain record, current normalization, mass and
threshold inputs, or canonical observable, so no candidate-compatible
formula/order/uncertainty payload can be frozen.

### 6. Electron magnetic anomaly — conditional fixed payload

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

The comparator payload is nevertheless formula-complete for a future
electron-anomaly output:

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
  publication Eq. (72)

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
  the identical sealed symbolic `alpha(0)` token used by BID;
  no CODATA-adjusted alpha value is loaded

sigma_comp =
  publication Eq. (87), intrinsic theory standard uncertainty apart
  from uncertainty in the fine-structure constant

units =
  dimensionless `a_e`

allowed_conversion =
  publication Eq. (72) only

later_coefficient_substitution =
  forbidden
```

The publication gives the relevant formulae verbatim:

```text
ae(th) = ae(QED) + ae(weak) + ae(had)                         (74)
...
The QED contribution may be written as [the n-indexed series] (75)
...
The theoretical uncertainty of the electron anomaly (apart from
uncertainty in the fine-structure constant) ...                  (87)
```

No term is evaluated here. A future prediction must first derive the same
physical electron observable from the sealed theory output, with its own
uncertainty, rather than relabel an existing scalar coefficient.

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

The negative is bounded to those roots, search families, publications, and
exclusions. It is not a claim that no related equation exists anywhere.

## Status

```text
RETURN_VERDICT = MISSING SPECIFICATION
families_reviewed = 6
formula_available_families = 1
candidate_compatible_comparator_missing_families = 5
pre_universe_timing_condition_satisfied = false
comparator_expression_evaluated = false
mu_comp_computed = false
sigma_comp_computed = false
D_computed = false
candidate_eligibility_asserted = false
measured_value_comparison_performed = false
prediction_attempted = false
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
