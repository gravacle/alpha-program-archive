# STAGE 8 / 7A STEP 11 — CONSTRUCTIBLE / DERIVATIONAL SPLIT — CODEX 2 V001

Lane: Codex 2  
Relay: PASTE 720  
Disposition: analysis only; 57-row remainder decomposed into finite carrier elements and classified `C`, `D`, or `U`; tooling proposed, not built  
Authority claimed: none

```text
RELAY_SHA256 = 86bea0ac27923bda3edea4fc92377dfdc868c1d1ee58d05f9719e7f977bb2b65
Q595_MAP_SHA256 = e85a6113e5b45624d19f987ae2603f63ac418df10f33669cc6a44742e5918ed5
SPEC_V012_SHA256 = 382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504
CHECK_MAP_SHA256 = 280004821c532def203ae81cec35bcac26bd3ab4bdd03752f5196aa7b9c23f3d
EVIDENCE_MANIFEST_SHA256 = 20c68f9cf0eb81238bae0f0835e9d7a6e55a979818e783726b793e2cf0773bb0
CALIBRATION_SHA256 = 27ad6b2b9d55fb1d323b3489bda8d5632ec69d0436750b740f0fa373bbe3bbfb
ROWS = 57
TOOLS_BUILT = 0
CHAIN_INVOKED = false
```

## 1. Pickup, jurisdiction, and census law

The single relay-720 inbox file and its sidecar agree at the displayed digest;
the lane guard says `CODEX 2`. `relay_outbox/720_ACK.md` was written before
substantive work. The output and sidecar names were absent in both the cleanroom
and archive workspace before creation.

The 57 rows are the Q-595 59-item census less the already lawful
`C-B-V009-06` and the calibration row `C-B-V010-12`. The latter's still-open
eight-element debt is classified separately in §5 and is not silently counted
as a 58th row.

An **element** is the smallest independently sealable bundle consumed by one
opcode family: one schema/typed instance, one finite grammar/certificate, one
proof or proof index, one expected ledger, one corpus definition, one mutation
family, one runtime record family, one fixture observation, or one envelope
binding. Per-ID repetitions governed by one proof index or grammar count as one
element; unrelated proofs, corpora, or grammars remain separate. `BASE`/P0
carriers common to all rows are excluded. This declared convention makes the
counts below reproducible and prevents word-level overcounting.

Classification law:

- `C` — deterministic generation is possible once the named schema, universe,
  mutation form, corpus member list, or primary output is sealed. The generator
  and input are named below. `C` does **not** assert that its prerequisite form
  is already sealed.
- `D` — a semantic statement, carrier choice, corpus membership decision, proof,
  theorem, or physical result must first be derived and sealed. The owner is
  named.
- `U` — current pins do not decide whether the object already has a derivation,
  which authority selects it, or which contract owns it. The reason is named;
  it is not forced into either other class.

## 2. Generator and owner codes

### 2.1 Constructible generators

| Code | Proposed deterministic generator | Required sealed input | Output class |
|---|---|---|---|
| `EB` | `emit_envelope_bindings` | V012 descriptor row, current check-map row, source spans, carrier payload digests | seven-field invocation/citation binding, input root, envelope record |
| `CS` | `compile_schema_instance` | closed schema or typed-form statement plus content-addressed subject bytes | canonical schema instance, typed graph/table/expression |
| `FG` | `generate_finite_family` | sealed finite universe/rules and ordering | grammar, independent completeness certificate, canonical IDs |
| `EL` | `generate_expected_ledger` | spec-fixed result constants, sealed per-ID map, or sealed expected conclusions | ID/result ledger and comparison targets |
| `MG` | `generate_mutation_fixture` | base carrier plus sealed mutation path/operator and expected class | canonical mutation instance and result key |
| `CD` | `generate_corpus_definition` | principal- or spec-sealed member list | `rd22.sealed-corpus-definition.v001`, member pins, declared root |
| `RC` | `capture_runtime_record` | sealed launch/runtime/trust manifests and declared masks | runtime, receipt, terminal, and cross-mode records |
| `OB` | `extract_fixture_observation` | admitted primary-row output plus sealed fixture form | positional-ID fixture observation and digest binding |

`EB` applies exactly once to every row and is shown in every row's `C` cell.
Generated values come from input bytes; none is transcribed.

### 2.2 Derivation owners

| Owner | Meaning |
|---|---|
| `S11-SPEC` | Step-11 specification/prose owner must seal carrier semantics, a corpus membership set, or a principal choice. |
| `S11-FORMAL` | Step-11 formalization owner must derive and seal a proof, identity bundle, or construction not deterministically emitted from a sealed finite form. |
| `A23`, `A24`, `A25`, `A27`, `A28` | the named physics road row produces the statement as a side effect of its existing work. |

`U-SOURCE` means an `NM?` source-locus search is unresolved. `U-PRINCIPAL`
means no authority selects the carrier. `U-CONTRACT` means the sealed interfaces
do not decide which contract owns the receiver.

## 3. Searched spaces and object-name probes

The classification consumed the Q-595 spans over V005, the blocker ledger,
matrix ledger, packet V011, A21 disposition, and CPT derivation; the current
V012 descriptors/check map; the D1 evidence manifest's 120-member four-mode
search space (`scope_sha256=691e871e4b2a13f09cdf5481abb1c7a32c05ba9426bf657436a5f5f2597db032`);
the sealed grounding relocation; the five batch-1 records; and the calibration.

The current delta probe scanned 2,972 Markdown/JSON/text/seal files and extracted
431 descriptor-shaped object names from the 54 check rows. It searched exact
names plus whitespace-normalized, scope/self-reference, and
hyphen/space/underscore variants. 276 names occur only in requirement/spec,
machine-copy, prior-run, or relay/report surfaces rather than a positive sealed
carrier. Probed families include:

```text
S_*, M_*, G_*, p_*, P_*, E_*, q_*, BRANCH_OUTCOME, EQUIV_CLASS,
preseal_sources, selector_sources, selection_sources, output_claim_sources,
response_sources, d1, F_phys, Q_flux, K_L, E_open, M_W, B_lambda,
Q_Sigma, P_ch, b_partial, c_partial, Gamma_cell
```

This is a carrier-location statement, not a claim that name occurrence proves
an object. Requirement-only occurrences remain absent as carrier evidence.

## 4. EE1 — row-by-row split

The last column is `C/D/U` element count under §1's convention.

### 4.1 V008

| Row | Q-595 | C — generator(input) | D — object `[owner]` | U — reason | Σ |
|---|---|---|---|---|---:|
| `C-B-V008-01` | SI/S | `EB`; `CS`(carrier/map schema + five manifests) | — | — | `2/0/0` |
| `C-B-V008-02` | SI/S | `EB`; `CS`(decorated category + finite generators/composition) | — | — | `2/0/0` |
| `C-B-V008-03` | MX(SI+KP)/M | `EB`; `CS`(collapse covectors + orientation involution) | naturality/orientation/sequential proof bundle `[S11-FORMAL]` | — | `2/1/0` |
| `C-B-V008-04` | SI/S | `EB`; `CS`(`K_L` + global shifts); `MG`(nonperiodic partial-shift fixture) | — | — | `3/0/0` |
| `C-B-V008-05` | SI/S | `EB`; `CS`(`W_univ`, `pi_U`); `MG`(`W^{-1}` competitor from sealed mutation form) | noncommuting plaquette fixture values `[S11-SPEC]` | — | `3/1/0` |
| `C-B-V008-06` | SI/M | `EB`; `CS`(authority AST + pullback maps); `CD`(FS/uniqueness corpus after membership seal) | FS/uniqueness corpus membership `[S11-SPEC]` | — | `3/1/0` |
| `C-B-V008-07` | SI/S | `EB`; `CS`(component quotient + real/complex seams) | — | — | `2/0/0` |
| `C-B-V008-08` | MX(SI+EC+KP)/L | `EB`; `CS`(`d1`, `F_phys`, `Q_flux`, domains, outside fixture); `FG`(`G_im,p_im`); `EL`(`E_flux`) | `p_right,p_min` proof bundle `[S11-FORMAL]` | — | `4/1/0` |
| `C-B-V008-09` | EC/M | `EB`; `CS`(branch schema + dependency DAG); `FG`(`G_branch,p_branch`); `EL`(`E_branch,BRANCH_OUTCOME`) | — | — | `4/0/0` |
| `C-B-V008-10` | SI/S | `EB`; `CS`(principal-selected stage graph); `CD`(alpha/core corpus); `CD`(reconstruction/review corpus) | content-addressed parent/report mapping `[S11-SPEC]`; alpha/core membership `[S11-SPEC]`; reconstruction/review membership `[S11-SPEC]` | — | `4/3/0` |
| `C-B-V008-11` | MX(SI+EC+KP)/L | `EB`; `CS`(`S_holdout,M_holdout`); `FG`(`G_contam,p_contam`); `EL`(`E_contam,FAILS`); `CD`(`preseal_sources`) | protocol proof `p_holdout` `[S11-FORMAL]`; `preseal_sources` membership `[S11-SPEC]` | — | `5/2/0` |

### 4.2 V009

| Row | Q-595 | C — generator(input) | D — object `[owner]` | U — reason | Σ |
|---|---|---|---|---|---:|
| `C-B-V009-01` | SI/S | `EB`; `CS`(universal object-fiber/inclusion schema); `CD`(alias corpus after membership seal) | abstract-line-alias membership `[S11-SPEC]` | concrete `K_open`/fiber instance is unselected `[U-PRINCIPAL]` | `3/1/1` |
| `C-B-V009-02` | EC/M | `EB`; `CS`(unit/sector declarations); `FG`(`G_equiv,p_equiv`); `EL`(`E_equiv,EQUIV_CLASS`) | — | — | `4/0/0` |
| `C-B-V009-03` | SI/S | `EB`; `CS`(`M_W` + global word after carrier seal) | choose and seal `L`/object carrier `[S11-SPEC]`; restriction morphisms and local normal forms `[S11-FORMAL]` | — | `2/2/0` |
| `C-B-V009-04` | EC/M | `EB`; `CS`(three log domains + boundary fixtures); `FG`(`G_log_domain,p_log_domain`); `EL`(fixture/partition IDs) | — | — | `4/0/0` |
| `C-B-V009-05` | SI/M | `EB`; `CS`(filtration/graded quotient); `MG`(zero/nonzero symbol fixtures) | — | — | `3/0/0` |
| `C-B-V009-07` | EC/M | `EB`; `CS`(`S_config,M_config`); `FG`(`G_config_mut,p_config_mut`); `EL`(`E_config_mut,REJECTED`) | — | — | `4/0/0` |
| `C-B-V009-08` | SI/S | `EB`; `CS`(citation graph after form seal); `CD`(general-FS corpus) | citation/claim nodes, typed entailment edges, and separately pinned authority premise `[S11-SPEC]`; general-FS membership `[S11-SPEC]` | — | `3/2/0` |
| `C-B-V009-09` | SI/M | `EB`; `CS`(charged-response expression + unit/dependency graphs) | — | — | `2/0/0` |
| `C-B-V009-10` | MX(SI+EC+KP)/L `NM!` | `EB`; `CS`(reconstruction graph + expected ledger); `FG`(`G_basis20,p_basis20`); `FG`(`G_parity,p_parity`) | deterministic local-Maxwell reconstruction map/proof `[A27]` | — | `4/1/0` |
| `C-B-V009-11` | SI/S | `EB`; `CS`(generated Hodge matrix + domain); `EL`(square/sign/commutator targets) | — | — | `3/0/0` |
| `C-B-V009-12` | MX(SI+KP)/M | `EB`; `CS`(phase-space/unit carrier) | Hamiltonian-to-action derivation proof `[A23]` | — | `2/1/0` |
| `C-B-V009-13` | MX(SI+EC+KP)/L | `EB`; `CS`(registry schema/manifest); `FG`(eligible IDs); `FG`(contamination family); `EL`(`E_holdout`) | selection proof `p_select` `[S11-FORMAL]` | — | `5/1/0` |

### 4.3 V010

| Row | Q-595 | C — generator(input) | D — object `[owner]` | U — reason | Σ |
|---|---|---|---|---|---:|
| `C-B-V010-02` | MX(SI+EC+KP)/L | `EB`; `CS`(control/status/parent records); `FG`(`G_c,p_c`); `CD`(explicit `{p_c_status,G_c_selector_parents}` members); `EL`(status/expected rejection); `MG`(`c=1`) | controls/status/rejection proof bundle `[S11-FORMAL]` | — | `6/1/0` |
| `C-B-V010-03` | MX(SI+EC+KP)/L | `EB`; `CS`(control/status/parent records); `FG`(`G_tau,p_tau`); `CD`(explicit selector-proof/parent members); `EL`(status/expected rejection); `MG`(`tau=1`) | controls/selector/rejection proof bundle `[S11-FORMAL]` | — | `6/1/0` |
| `C-B-V010-04` | SI/S | `EB`; `CS`(primitive/Thomson/Q-spec type DAG); `CD`(occurrence corpus after membership seal); `MG`(primitive-to-Thomson alias) | occurrence-corpus membership `[S11-SPEC]` | — | `4/1/0` |
| `C-B-V010-05` | SI/L `NM!` | `EB`; `CS`(anisotropic tetrad/Hodge carrier after theorem seal) | exact anisotropic cancellation theorem `[A27]` | — | `2/1/0` |
| `C-B-V010-06` | MX(SI+EC+KP)/L `NM!` | `EB`; `CS`(domain/status records); `FG`(competitor family); `EL`(competitor decisions) | target-independent domain plus per-competitor decision proofs `[A25]` | — | `4/1/0` |
| `C-B-V010-07` | SI/M | `EB`; `CS`(Gram/design/conversion tables) | — | — | `2/0/0` |
| `C-B-V010-08` | SI/M | `EB`; `CS`(rank/nullspace/section data); `MG`(rank-21 revival); `EL`(expected rejection) | — | — | `4/0/0` |
| `C-B-V010-09` | KP/L `NM!` | `EB` | uniform-neighborhood theorem and certified remainder `[A25]` | — | `1/1/0` |
| `C-B-V010-10` | MX(SI+EC+KP)/L | `EB`; `CS`(common-refinement/status records); `FG`(`G_ref,p_ref`); `FG`(`G_comp,p_comp`); `EL`(`E_ref`); `CD`(`output_claim_sources`) | generator/composite proof indexes `[S11-FORMAL]`; universality-claim corpus membership `[S11-SPEC]` | — | `6/2/0` |
| `C-B-V010-11` | SI/S | `EB`; `CS`(universal decorated-category schema) | closed finite object/morphism/identity/composition instance `[S11-SPEC]` | — | `2/1/0` |
| `C-B-V010-13` | MX(SI+EC+KP)/L | `EB`; `CS`(registry/custodian schemas); `FG`(registry family); `FG`(failure family); `EL`(selection/failure ledger); `CD`(`preseal_sources`) | independence + selection proof bundle `[S11-FORMAL]`; `preseal_sources` membership `[S11-SPEC]` | — | `6/2/0` |
| `C-B-V010-14` | SI/S | `EB`; `CS`(claim/provenance graph after statement seal); `MG`(factor-two/factor-four/later mutations); `CD`(`preseal_sources`) | physical amplitude/action provenance + Hessian/claim ordering statement `[A23]` (also an A28 side effect); `preseal_sources` membership `[S11-SPEC]` | check map omits descriptor `DAG`/`EXACT` receiver ownership `[U-CONTRACT]` | `4/2/1` |

### 4.4 V011 MR

| Row | Q-595 | C — generator(input) | D — object `[owner]` | U — reason | Σ |
|---|---|---|---|---|---:|
| `C-B-V011-MR-01` | MX(SI+EC+KP)/L | `EB`; `CS`(monoidal categories + target record); `FG`(coherence diagrams); `EL`(`E_monoidal`) | target-scope and per-diagram proofs `[S11-FORMAL]` | — | `4/1/0` |
| `C-B-V011-MR-02` | MX(SI+EC+KP)/L | `EB`; `CS`(restriction/status records); `FG`(statistics family); `EL`(`E_stats`); `CD`(`selector_sources`) | selector proof `[S11-FORMAL]`; selector-source membership `[S11-SPEC]` | — | `5/2/0` |
| `C-B-V011-MR-03` | SI/L `NM!` | `EB`; `CS`(pushout grammar + two/three-cell fixtures after construction seal) | shared-boundary gluing/descent construction `[S11-FORMAL]` | — | `2/1/0` |
| `C-B-V011-MR-04` | MX(SI+EC+KP)/L | `EB`; `CS`(claim manifest); `FG`(claim census); `EL`(claim IDs/expected restrictions); `CD`(`S_claim`) | higher-sector distinctness + per-claim completeness proofs `[S11-FORMAL]`; claim-corpus membership `[S11-SPEC]` | — | `5/2/0` |
| `C-B-V011-MR-05` | MX(SI+EC+KP)/L | `EB`; `CS`(rule-source/overlap records); `FG`(evolution family); `EL`(`E_evolution`) | adopted-or-derived rule proof `[S11-FORMAL]` | — | `4/1/0` |
| `C-B-V011-MR-06` | MX(SI+EC+KP)/L | `EB`; `CS`(selector status + parent DAG); `FG`(preparation family); `EL`(`E_prep`); `CD`(explicit selector-proof/parent members) | target-independent preparation selector proof `[A25]` | — | `5/1/0` |

### 4.5 V011 SP1

| Row | Q-595 | C — generator(input) | D — object `[owner]` | U — reason | Σ |
|---|---|---|---|---|---:|
| `C-B-V011-SP1-01` | SI/M | `EB`; `CS`(charge carriers, hypersurface form, CAR/chirality maps, competitor) | — | — | `2/0/0` |
| `C-B-V011-SP1-02` | MX(SI+EC+KP)/L `NM?` | `EB`; `CS`(boundary/representation/selected-map type); `FG`(candidate maps); `FG`(Lorentz generators); `EL`(`E_map`) | — | selected-map derivation source locus unresolved `[U-SOURCE]` | `5/0/1` |
| `C-B-V011-SP1-03` | SI/M | `EB`; `CS`(complete CPT equation set + legacy control) | — | — | `2/0/0` |
| `C-B-V011-SP1-05` | EC/L | `EB`; `CS`(typed candidate graphs); `FG`(source-incidence family); `CD`(`selection_sources`) | selection-source membership `[S11-SPEC]` | — | `4/1/0` |
| `C-B-V011-SP1-06` | MX(SI+KP)/L `NM?` | `EB`; `CS`(current/charge/projector graph + domain) | — | current→charge→projector proof-chain source unresolved `[U-SOURCE]` (likely A23/A24 overlap) | `2/0/1` |
| `C-B-V011-SP1-07` | MX(SI+EC+KP)/L `NM?` | `EB`; `CS`(composition/typed graph); `FG`(overlap/order family); `EL`(required-ID/proof-index records) | — | gluing/ordering derivation sources unresolved `[U-SOURCE]` (possible A25 overlap) | `4/0/1` |
| `C-B-V011-SP1-09` | EC/L | `EB`; `CS`(reference-verdict schema); `FG`(SP1 family); `EL`(reference/producer ledgers); `RC`(independent enumeration/cross-compare) | — | — | `5/0/0` |

### 4.6 V011 SP2, repair row, and fixtures

| Row | Q-595 | C — generator(input) | D — object `[owner]` | U — reason | Σ |
|---|---|---|---|---|---:|
| `C-B-V011-SP2-01` | SI/L | `EB`; `CS`(CPT/normals/transports/adjoints/nullspace/controls exact system) | — | — | `2/0/0` |
| `C-B-V011-SP2-02` | SI/S | `EB`; `CS`(displayed partial operator relation); `MG`(alias control after relation seal) | domains/codomains and exact square relation `[S11-FORMAL]` | — | `3/1/0` |
| `C-B-V011-SP2-04` | EC/L `NM!` | `EB`; `CS`(factorization/commutant); `FG`(control family after solution seal); `FG`(rescaled controls); `EL`(`E_control`) | complete control-superoperator solution family `[A28]` | — | `5/1/0` |
| `C-B-V011-SP2-05` | MX(SI+EC+KP)/L `NM?` | `EB`; `CS`(global graph/premise/fixtures); `FG`(pushout family); `FG`(orientation family); `EL`(proof indexes/expected records) | — | pushout/orientation/quartic proof and quasi-free premise sources unresolved `[U-SOURCE]` (likely A28 overlap) | `5/0/1` |
| `C-B-V011-SP2-07` | MX(SI+KP)/L | `EB`; `CS`(receipt/terminal schemas + masks); `CD`(producer/verifier source corpus); `EL`(expected terminal/comparison records); `RC`(normal/optimized/verifier runtime records) | terminal-seal proof `p_terminal` `[S11-FORMAL]` | — | `5/1/0` |
| `C-D-A35-02-QUASIFREE-CAR-LIFT` | SI/M `NM?` | `EB`; `CS`(operator/CAR/covariance/quartic carrier after source seal) | — | operator-valued lift derivation source unresolved `[U-SOURCE]` (likely A28 overlap) | `2/0/1` |
| `FX-A35-03-C-FAMILY` | MX observation/M | `EB`; `OB`(admitted V010-02 output + fixture form) | — | — | `2/0/0` |
| `FX-A35-04-TAU-FAMILY` | MX observation/M | `EB`; `OB`(admitted V010-03 output + fixture form) | — | — | `2/0/0` |
| `FX-A35-05-PRIMITIVE-THOMSON-CONFLATION` | SI observation/S | `EB`; `MG`(sealed alias mutation); `OB`(admitted V010-04 output + fixture form) | — | — | `3/0/0` |

## 5. Calibration-row debt, classified but excluded from 57-row totals

The eight `C-B-V010-12` elements from PASTE 718 resolve as follows:

| Element | Class | Generator or owner | Reason |
|---|---|---|---|
| `CLOSED_REPORT_SCHEMA_TYPES_AND_EXTRA_FIELD_RULE` | D | `S11-SPEC` | field names exist; types and closed-field law do not |
| `CONTENT_ADDRESSED_STAGE_PARENT_KEYS` | C | `emit_envelope_bindings` over sealed report instances | digest keys are mechanical after report identity is fixed |
| `CONTENT_ADDRESSED_STAGE_REPORT_INSTANCES` | U | `U-PRINCIPAL` | current law does not decide synthetic fixtures versus actual future stage reports |
| `PARENT_MUTATION_INSTANCE` | C | `generate_mutation_fixture` | deterministic after edge/path mutation form is sealed |
| `PARENT_MUTATION_EXPECTED_REJECTION` | C | `generate_expected_ledger` | deterministic after rejection class is sealed |
| `FORBIDDEN_CORE_ALPHA_MUTATION_INSTANCE` | C | `generate_mutation_fixture` | deterministic after field/path/value form is sealed |
| `FORBIDDEN_CORE_ALPHA_MUTATION_EXPECTED_REJECTION` | C | `generate_expected_ledger` | deterministic after rejection class is sealed |
| `MUTATION_RECEIVER_BINDING` | D | `S11-SPEC` / Builder-B contract subgate | one nonrepeatable `DAG` cannot receive positive + two mutation cases without new receiver law |

Calibration debt: `C=5 / D=2 / U=1`. It is displayed for strategy but excluded
from the 247-element primary total and compressed estimate for the other 57.

## 6. Totals and owners

### 6.1 Mechanical/derivational census

| Class/code | Elements |
|---|---:|
| `C:EB` | 57 |
| `C:CS` | 53 |
| `C:FG` | 31 |
| `C:EL` | 25 |
| `C:MG` | 10 |
| `C:CD` | 17 |
| `C:RC` | 2 |
| `C:OB` | 3 |
| **C total** | **198** |
| `D:S11-SPEC` | 18 |
| `D:S11-FORMAL` | 16 |
| `D:physics side effect` | 8 |
| **D total** | **42** |
| `U:SOURCE` | 5 |
| `U:PRINCIPAL` | 1 |
| `U:CONTRACT` | 1 |
| **U total** | **7** |
| **All elements** | **247** |

Section arithmetic re-derived from the row table:

```text
V008 = 11 rows / C34 D9 U0
V009 = 12 rows / C39 D8 U1
V010 = 12 rows / C47 D13 U1
MR   =  6 rows / C25 D8 U0
SP1  =  7 rows / C24 D1 U3
SP2  =  5 rows / C20 D3 U1
D02  =  1 row  / C2  D0 U1
FX   =  3 rows / C7  D0 U0
ROWS = 57; C=198; D=42; U=7; 198+42+7=247
```

### 6.2 D owners and physics overlap

| Primary owner | D elements | Rows/objects |
|---|---:|---|
| `S11-SPEC` | 18 | semantic carrier forms, principal choices, and corpus membership sets |
| `S11-FORMAL` | 16 | proof bundles, gluing/identity constructions, and terminal proof |
| `A23` | 2 | V009-12 action derivation; V010-14 amplitude/action/Hessian ordering (also A28 side effect) |
| `A24` | 0 | no D element is assigned primarily; SP1-06 remains U and may overlap |
| `A25` | 3 | V010-06 target-independent competitor decisions; V010-09 uniform theorem; MR-06 preparation selector |
| `A27` | 2 | V009-10 deterministic local-Maxwell reconstruction; V010-05 anisotropic cancellation |
| `A28` | 1 | SP2-04 complete control-superoperator family; V010-14 is a secondary overlap |
| **Total** | **42** | 34 Step-11 derivations + 8 physics side effects |

No D element is left ownerless. The seven U elements are the honest unowned or
unresolved remainder: five source-locus questions, one principal carrier choice,
and one cross-contract receiver question. A source-locus relay may convert a U
to C (existing complete derivation found) or D (new statement required); this
artifact does not pre-adjudicate that outcome.

## 7. EE2 — smallest tooling proposal

Five tools cover all 198 C elements; no tool is built here.

| Tool | Codes covered | Elements | Must be sealed first | Batch output |
|---|---|---:|---|---|
| `compile_carriers.py` | `CS` | 53 | closed schema/typed-form statements and exact subject spans | canonical schema instances, graphs, tables, expressions |
| `generate_finite_families.py` | `FG`,`EL` | 56 | finite universe/rules, canonical ordering, expected constants or proof conclusions | grammars, independent certificates, IDs, expected ledgers |
| `generate_mutation_observations.py` | `MG`,`OB` | 13 | mutation forms, base carriers, fixture schemas; admitted primary outputs for observations | mutation payloads and positional fixture observations |
| `generate_corpora_pins_envelopes.py` | `CD`,`EB` | 74 | corpus member lists; completed carrier payloads; current descriptor/check-map pins | corpus definitions, roots, pins, seven-field envelopes |
| `capture_runtime_records.py` | `RC` | 2 | runtime/launch/trust manifests and masks | normal/optimized/verifier records and masked comparisons |

Required safeguards are common: tight canonical JSON; generated pin manifest;
source/span rehash; exact schema keys; declared-root recomputation; deterministic
ordering; negative fixtures; output collision refusal; and a dry-run using only
synthetic non-authoritative fixtures. The tools must refuse any missing semantic
form rather than infer it from a requirement sentence.

Tooling relay estimate:

```text
tool contracts + implementations + independent fixtures     8-12
batch carrier/family/mutation/corpus/runtime production     12-24
C-class total with tooling                                  20-36
```

This replaces row-by-row transcription of 198 mechanical elements. It does not
reduce the D or U work and does not admit anything to the chain.

## 8. EE3 — honest remainder and compressed estimate

The original calibration projected `112–232` authoring relays for the remaining
57. With the proposed batch tools:

| Work | Relay band | Basis |
|---|---:|---|
| C tooling + batch generation | 20–36 | five tool families over 198 C elements |
| D derivation/sealing | 42–126 | 42 independently sealable semantic/proof elements at 1–3 relays each |
| U source/authority/contract disposition | 7–14 | seven bounded decisions, before any converted C/D work |
| **Compressed authoring band** | **69–176** | admission and chain runs excluded |

Thus at least **42 relay-equivalents** of the original `112–232` band are
irreducibly derivational under this element convention, with a realistic
derivation band of `42–126`. Eight D elements are expected side effects of the
five physics rows (none assigned primarily to A24); 34 are Step-11
specification/formalization work. The seven U elements are not counted as
derivations until their bounded ownership/source questions are resolved.

The endpoint compression is `112→69` and `232→176`, a planning reduction of
43–56 relays. It is not a schedule, authorization, or promise. Builder-B
contract/replay subgate work and actual chain executions remain outside the
band.

## 9. Does-not-do, pin check, and verb audit

No generator, schema, fixture, carrier, envelope, proof, corpus, or runtime
record was created. Existing package bytes and manifests are unchanged. Input
pins displayed at the head were rehashed before use; the output collision check
remained clear through creation and the report is sealed only after its row/count
arithmetic is rechecked.

Verb audit under the verdict-line scope rule: CLEAN. “Constructible” is a
conditional tooling classification, not an implemented object. “Derivational”
names a required sealed statement, not a proof claim. “Projection” is an
evidence-based planning band. No physical, proof, evaluator, board, admission,
or seal verdict is claimed.

ELEMENTS = 247 classified (C198/D42/U7; 57-row total; calibration debt C5/D2/U1 displayed separately)
TOOLING = proposed (inputs named, nothing built)
COMPRESSED_ESTIMATE = 69-176 authoring relays with tooling (admission and chain excluded)
IRREDUCIBLE_D = 42 (owners mapped: S11-SPEC 18, S11-FORMAL 16, physics side effects 8)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN / (+analysis only; no tool, carrier, envelope, proof, admission, board change, or seal claim)
