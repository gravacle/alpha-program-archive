# Stage 8 CTP Physical-Input Package U1 DoR-008 Assembly Determination v001

Date: 2026-08-01  
Lane: Codex lane 2  
Register head checked at send-time: Q-215  
Road role: Task 2c, assemble the convention layer on `C0_008`

## Verdict

```text
U1_008_ASSEMBLED_AT_C0_SCOPE = true | TYPE-P | premises: DoR-008

U1_008_COMPONENT_COUNT = 6 | TYPE-P | premises: DoR-008
U1_008_COMPONENTS_INSTANTIATED =
  branch/source orientation,
  branch metric,
  reality involution,
  compound-index order,
  source symmetry,
  embeddings on C0

d_U1_PREMISE_LEVEL_TOTAL = true | TYPE-P | premises: DoR-008
d_U1_COMMON_ORIGIN_DERIVED = false | TYPE-U |
  would-build: derive the same certified U1 presentation from an independently
               supplied B0-role common-origin object together with C0

U1_008_EXTENDED_TO_COMPLETED_PHYSICAL_QUOTIENT = false | TYPE-U |
  would-build: construct U3's quotient/domain package and prove that the U1_008
               metric, real structure, source subspaces, and embeddings descend
               to it naturally

DOR008_U1_FINITE_INCIDENCE_FALSIFIER_CERTIFIED = false | TYPE-U |
  would-build: Q-215's two map classes, then restrict U1_008 to each sealed
               finite incidence/sector carrier and execute the comparisons

NEW_ADOPTION_MADE = false | TYPE-S |
  scope: this artifact's U1 construction data |
  reason: the branch signs and Keldysh normalization are inherited from sealed
          formal conventions; the C-star real structure and symmetric-source
          restriction are forced mathematical constructions on the ratified
          C0_008 branch/source interface

PHYSICAL_VERDICT = NO_VERDICT
CONSTRUCTION_VERDICT = U1_ASSEMBLED_CONDITIONALLY_AT_C0_SCOPE
```

This is the package's second conditional component. It is not an unconditional
microscopic derivation. It also does not complete Item 4 on the future physical
quotient: that compatibility test requires U3 and remains unbuilt.

## 1. Currency, exact contract, and frozen authorities

The register was re-read through Q-215 immediately before construction. Q-215
adds two unbuilt comparison-map classes but does not supersede Q-212's DoR-008
ratification, Q-213's `C0_008`, or the U1 contract. The new maps bear on the
standing finite-authority falsifier and are recorded in Sections 7 and 9; they
are not inserted into U1.

Decision of Record 006 fixes the current typing scheme at
`DECISION_OF_RECORD_006_TYPE_P_ADOPTED_LAZY_MIGRATION_2026-08-01_V001.md:8-14`:
premise-conditional claims are `TYPE-P`, while `TYPE-U` remains unbuilt and
`TYPE-C` is reserved for constraint-blocked checks.

Decision of Record 008, hash
`d51a6d5c5bb0020a081cfd2adfb545b9f5ed86ce660d3feacadc5ef68140fb19`,
ratifies the seven presentation premises at `:8-14`, imposes the finite-result
falsifier at `:16-22`, and requires every descendant construction to carry
`TYPE-P | premises: DoR-008` at `:33-37`.

The package contract is exact. The B0 stop specification at
`STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md:1001-1013`
states:

```text
U1 = physical branch/source orientation, metric, involution, compound-index
     order, source symmetry, and embeddings on C0
```

and at `:1016-1027` requires:

```text
d_U1 : (B0_candidate,C0) -> U1
```

with no undeclared post-output supplement. The substitute-admissibility
adjudication at
`STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_SUBSTITUTE_ADMISSIBILITY_ADJUDICATION_V001.md:173-192`
repeats the six fields. Its `:352-358` is decisive for this construction: a
certified U1 presentation suffices extensionally; unique microscopic origin
does not. The price is that common-origin provenance remains open.

### 1.1 Frozen inputs

The following byte-level authorities were frozen before the output tuple was
formed:

| Authority | SHA-256 | Role |
|---|---|---|
| `STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md` | `76916244bdbcac7c2a6d4afae40f35127540d1d9e4cfc86fb72318506671161f` | Ratified branch algebra, embeddings, source domains/maps, star covariance |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_C0_DOR008_ASSEMBLY_AND_FIRST_RESTRICTION_TEST_V001.md` | `1467ab9850022931e68dc9ffa625d95099d8f6bb74d734dc9d0466f169bd00b6` | Exact `C0_008` instance |
| `primitive_record_cell_selection_principle_v004.md` | `13d227ceb2198d96b0e4e2fef57b874cea71cb755320508fbf4c6d64a00c507e` | Formal compound index, symmetric bilocal source, CTP reality obligation |
| `alpha_complete_dimension_convention_ledger_v004.md` | `bbf2bdddfcefe851e985c4db03a62906082660af9a3c639d259afc93b4bbcc66` | Exact branch/Keldysh signs and normalization |
| `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md` | `57c06fcbedf4a486b87b42c02e6d13a92096ac6a56751d3ae5fd55f4b11deb57` | Exact Keldysh matrix and ordered mixed block |
| `COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_AMPLITUDE_RESULT_V001.md` | `273e1473a1a8bf0be0467634411cec1b7daeee0c9f24c330fad5d288d191dcbb` | Independent finite CTP Hermiticity cross-check only |
| `STAGE8_TASK2F_PRESENTATION_TO_FINITE_AND_SRE_BRIDGE_BUILD_DETERMINATION_V001.md` | `9721dc049a79c0c9b9069ade6436ab93e3ff1266cfb25da753f39143c45794c5` | Current Q-215 finite-comparison boundary |

Write `F_U1` for the four sealed formal convention authorities in rows 3-6.
`F_U1` is frozen construction provenance, not a seventh field of `P_008` and
not a post-output supplement.

### 1.2 The already-assembled carrier

`C0_008` is not reconstructed here. At
`STAGE8_CTP_PHYS_INPUT_PACKAGE_C0_DOR008_ASSEMBLY_AND_FIRST_RESTRICTION_TEST_V001.md:142-184`
it has branch algebra and joint carrier

```text
A_F_CTP := A_F,+ tensor_min (A_F,-)^op,
A_C0 := A_SR graded-tensor_min A_F_CTP,
E_C0 := H_SR external-tensor (A_F_CTP)_(A_F_CTP),
pi_C0 : A_C0 -> L_(A_F_CTP)(E_C0).
```

At `:200-221`, `D_C0=E_C0` is the common domain. At `:223-265` it supplies
the branch embeddings, finite-support source domains, source maps, and star
covariance, while expressly withholding orientation, metric, physical reality,
and compound-index order for U1. The exact C0 tuple is at `:267-285`.

## 2. Exact U1 construction on C0_008

### 2.1 Component 1 — physical branch/source orientation

Let the branch set and exchange be

```text
B_CTP := {+,-},
bar(+) := -,
bar(-) := +.
```

The ratified carrier already identifies `+` as the forward factor and `-` as
the opposite/backward factor. The proposal at
`STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md:331-347`
states that `op` records backward composition while keeping the two factors
distinct.

The sealed formal action convention fixes the orientation coefficients:

```text
epsilon(+) := +1,
epsilon(-) := -1.
```

This is not inferred from a desired response. It is the coefficient pattern
already written in
`alpha_complete_dimension_convention_ledger_v004.md:269-287`:

```text
Gamma_M[A_+,A_-;K] = S_M[A_+;K] - S_M[A_-;K].
```

That authority also forbids silently reversing the induced response sign.
The source orientation is the pullback of `epsilon` along the first projection
of the actual source domain

```text
D_J = C_c(B_CTP x (Lambda without {0}); C).
```

No state, action operator, or measure is used in this pullback.

```text
U1_BRANCH_SOURCE_ORIENTATION_INSTANTIATED = true | TYPE-P |
  premises: DoR-008 and the sealed formal action-difference convention
```

### 2.2 Component 2 — oriented branch metric

On the ordered branch basis `(+, -)`, define

```text
eta_CTP(e_a,e_b) := epsilon(a) delta_(a,b),

eta_CTP = diag(+1,-1).
```

This is the unique unit-coefficient diagonal bilinear form that represents
the already-fixed `S_+ - S_-` contraction in that ordered basis. Encoding a
fixed signed two-point orientation by its diagonal bilinear form is imported
ordinary finite-dimensional linear algebra. It applies here because the
corpus itself supplies the two ordered branches and their unit coefficients;
it adds no physical premise.

The sealed Keldysh transform is

```text
A_c     = (A_+ + A_-)/2,
A_delta = A_+ - A_-,

[A_+]   [1  1/2] [A_c    ]
[A_-] = [1 -1/2] [A_delta].
```

The first two lines are at
`alpha_complete_dimension_convention_ledger_v004.md:260-267`; the matrix and
the ordered retarded extraction are at
`STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:785-819`.
Writing the matrix as `T_CTP`, direct multiplication gives

```text
T_CTP^T eta_CTP T_CTP = [[0,1],[1,0]].
```

Thus the metric has exactly the mixed common/difference form required by the
sealed `(delta,c)` retarded block; no free normalization remains.

```text
U1_BRANCH_METRIC_INSTANTIATED = true | TYPE-P |
  premises: DoR-008 and the sealed branch/Keldysh convention
```

### 2.3 Component 3 — CTP reality involution

The ratified opposite algebra makes a branch-exchange real structure
available without a state. On the CTP field factor define the anti-linear map

```text
Theta_F(f_+ tensor g_-^op)
  := g_+^* tensor (f_-^*)^op.
```

Equivalently, on the canonical character generators,

```text
Theta_F(e_+(U_lambda)) = e_-(U_(-lambda)),
Theta_F(e_-(U_lambda)) = e_+(U_(-lambda)).
```

`Theta_F` is an anti-linear algebra automorphism and `Theta_F^2=id`. This is
the standard real structure of `A tensor A^op`; that C-star-algebra fact is an
imported mathematical construction, not imported dynamics. Its hypotheses are
met exactly by the ratified `A_F,+ tensor (A_F,-)^op` carrier.

On the actual source domains, the induced involutions are

```text
(Theta_J j)(a,lambda)
  := conjugate(j(bar(a),-lambda)),

(Theta_R r)((a,lambda),(b,mu))
  := conjugate(r((bar(a),-lambda),(bar(b),-mu))).
```

They are distinct from the already-ratified operator-adjoint operations

```text
j^sharp(a,lambda) := conjugate(j(a,-lambda)),
r^sharp((a,lambda),(b,mu))
  := conjugate(r((b,-mu),(a,-lambda)))
```

at proposal `:494-508`. `sharp` supplies adjoint covariance within one branch;
`Theta` supplies CTP branch exchange. Identifying them would erase the branch
exchange and is rejected.

The finite amplitude identity

```text
Z_K[A_+,A_-]^* = Z_K[A_-,A_+]
```

at `COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_AMPLITUDE_RESULT_V001.md:28-37` is an
independent cross-check of this convention. It is not an input to the
construction: its proof consumes a state and evolution and therefore belongs
downstream of U1.

```text
U1_REALITY_INVOLUTION_INSTANTIATED = true | TYPE-P |
  premises: DoR-008 and the sealed CTP Hermiticity convention
DOWNSTREAM_STATE_OR_DYNAMICS_USED_TO_DEFINE_THETA = false | TYPE-S |
  scope: the displayed definitions of Theta_F, Theta_J, and Theta_R
```

### 2.4 Component 4 — compound-index order

The completed continuum index declared at
`primitive_record_cell_selection_principle_v004.md:21-35` is
`I=(a,mu,x)`, with branch coordinate first. `C0_008` does not yet carry the
DoR-007 continuum realization. Its actual, total finite-support source domain
instead supplies the exact sequential-cylinder index

```text
I_008 := (a,lambda),
a in ordered B_CTP=(+,-),
lambda in Lambda without {0}.
```

The branch coordinate is outer and the ratified sequential character label is
inner. Pointwise in `lambda`, the Keldysh order is

```text
I_K_008 := (kappa,lambda),
kappa in ordered (c,delta).
```

The response consumer's mixed differentiation order remains the separately
declared `(delta,c)` block. The distinction between coordinate order `(c,
delta)` and derivative block `(delta,c)` is retained rather than collapsed.

This is a complete index order for every source map presently in `C0_008`.
It does not claim the absent continuum refinement `(mu,x)` or its integration
order.

```text
U1_COMPOUND_INDEX_ORDER_INSTANTIATED_ON_C0_008 = true | TYPE-P |
  premises: DoR-008 and the sealed Keldysh convention
U1_CONTINUUM_COMPOUND_INDEX_REALIZATION_INSTANTIATED = false | TYPE-U |
  would-build: DoR-007's discrete-to-continuum realization and its certified
               source-index pullback
```

### 2.5 Component 5 — physical source symmetry

Let `tau_R` exchange the two compound slots:

```text
(tau_R r)(I,J) := r(J,I).
```

The formal authority at
`primitive_record_cell_selection_principle_v004.md:25-37` requires
`R_IJ=R_JI`, places the bilocal source in the symmetric compound-index dual,
and imposes the corresponding CTP reality condition. Instantiate those
requirements on the actual C0 domains:

```text
D_J_U1 := {j in D_J : Theta_J j = j},

D_R_U1 := {r in D_R : tau_R r = r and Theta_R r = r}.
```

The physical U1 source maps are restrictions, not replacements:

```text
s_J_U1 := s_J restricted to D_J_U1,
s_R_U1 := s_R restricted to D_R_U1.
```

The proposal's factor `1/2`, finite support, and star covariance remain
unchanged. Antisymmetric bilocal directions and non-real branch-exchange
sources are excluded from the U1 physical source coordinates; no source value
or source state is selected.

```text
U1_SOURCE_SYMMETRY_INSTANTIATED = true | TYPE-P |
  premises: DoR-008 and the sealed symmetric/reality source restriction
```

### 2.6 Component 6 — embeddings on C0

Use the existing represented branch embeddings without modification:

```text
Emb_U1_008 := (
  pi_C0 compose e_plus,
  pi_C0 compose e_minus
),

e_plus(a)  := 1_A_SR tensor (a tensor 1),
e_minus(a) := 1_A_SR tensor (1 tensor a^op).
```

They are total on `A_F`, preserve `D_C0`, have commuting ranges, and are
neither charge conjugation nor record-stage embeddings
(`C0_008` artifact `:223-265`; proposal `:457-473`). Their added U1
certificate is compatibility with `epsilon`, `eta_CTP`, and `Theta_F`:

```text
Theta_F compose e_plus  = e_minus compose star,
Theta_F compose e_minus = e_plus compose star.
```

```text
U1_EMBEDDINGS_ON_C0_INSTANTIATED = true | TYPE-P | premises: DoR-008
```

## 3. Exact U1_008 tuple

The assembled convention layer is

```text
U1_008 := (
  branch_source_orientation = (B_CTP,bar,epsilon),
  branch_metric             = eta_CTP,
  reality_involution        = (Theta_F,Theta_J,Theta_R),
  compound_index_order      = (I_008,I_K_008,(delta,c)_response_block),
  source_symmetry           = (D_J_U1,D_R_U1,s_J_U1,s_R_U1),
  embeddings_on_C0          = Emb_U1_008,
  provenance_record         = Prov_U1_008
).
```

`Prov_U1_008` records `P_008`, the exact `C0_008` hash, `F_U1`, DoR-008, and
the construction order in Section 2. It records the DoR-007 continuum layer,
U3 quotient action, common-origin descent, and Q-215 finite comparison maps as
open; none is represented as present.

```text
U1_008_IS_AN_INSTANCE = true | TYPE-P | premises: DoR-008
U1_008_IS_UNCONDITIONALLY_DERIVED_PHYSICS = false | TYPE-P |
  premises: its carrier and source maps descend from the ratified DoR-008
            presentation rather than an independently derived B0
```

## 4. Premise-level descent and the provenance ceiling

Freeze `F_U1` before construction and define the requested premise-level map
as a map with that frozen authority parameter:

```text
d_U1^P := d_U1^(P;F_U1)
  : (P_008,C0_008) -> U1_008,

d_U1^P(P_008,C0_008)
  := Assemble_U1(F_U1;P_008,C0_008)
   = U1_008.
```

Displaying `F_U1` is provenance disclosure. Hiding it inside the code of the
map would falsely claim that DoR-008 itself selected the conventions; Q-214
already refuted that claim.

The stronger package map remains

```text
d_U1 : (B0_candidate,C0) -> U1.
```

The two maps are not identified:

```text
d_U1_PREMISE_LEVEL_TOTAL = true | TYPE-P | premises: DoR-008
d_U1_PREMISE_LEVEL_NO_POST_OUTPUT_SUPPLEMENTATION = true | TYPE-P |
  premises: DoR-008 and F_U1 frozen before assembly

d_U1^P_EQUALS_DERIVED_COMMON_ORIGIN_d_U1 = false | TYPE-R |
  test: compare domains and provenance; d_U1^P begins at a ratified premise
        package plus sealed convention authorities, while d_U1 begins at an
        independently supplied common-origin B0-role object

d_U1_COMMON_ORIGIN_DERIVED = false | TYPE-U |
  would-build: the independently derived B0-role source and its certified
               descent of this same U1 presentation
```

The independent-provenance requirement is therefore named, not papered:
construct a B0-role common-origin candidate and a naturality certificate
showing that its branch/source typing descends to an object isomorphic to
`U1_008` while preserving all six fields.

## 5. Failure-capable certificates and executed checks

### U1-008-C1 — orientation and metric

Pass condition: the metric encodes the sealed unit-coefficient action
difference and transforms to a purely mixed common/difference bilinear form.

Failure mutations:

- `diag(+1,+1)` fails by producing a sum rather than the sealed branch
  difference;
- `diag(-1,+1)` fails against the sealed sign convention as written;
- a rescaled diagonal metric fails because the sealed transform and action
  coefficients contain no compensating normalization.

Result:

```text
U1_C1_ORIENTATION_METRIC = PASS | TYPE-P | premises: DoR-008
```

### U1-008-C2 — real structure

Pass condition: `Theta_F`, `Theta_J`, and `Theta_R` are anti-linear,
involutive, exchange the two CTP branches, and invert character labels under
star.

Failure mutations:

- omitting branch exchange fails the finite CTP Hermiticity relation;
- omitting character inversion fails `U_lambda^*=U_(-lambda)`;
- identifying `Theta` with `sharp` fails because `sharp` does not exchange
  branches.

Result:

```text
U1_C2_REAL_STRUCTURE = PASS | TYPE-P | premises: DoR-008
```

### U1-008-C3 — compound order

Pass condition: the contour order is `(+,-)`, the Keldysh coordinate order is
`(c,delta)`, and the consumer block is separately `(delta,c)`.

Failure mutation: treating `(c,delta)` and `(delta,c)` as the same ordered
pair transposes the sealed retarded extraction.

```text
U1_C3_COMPOUND_ORDER = PASS_AT_C0_SCOPE | TYPE-P | premises: DoR-008
U1_C3_CONTINUUM_ORDER_TEST = UNEXECUTABLE | TYPE-U |
  would-build: DoR-007 continuum realization
```

### U1-008-C4 — source symmetry

Pass condition: only the `tau_R`-symmetric and `Theta_R`-real bilocal source
directions, and the `Theta_J`-real linear sources, enter the U1 subdomains.

Named killed candidates:

- any nonzero antisymmetric bilocal source is killed by `tau_R r=r`;
- any source pair not related by branch exchange, conjugation, and character
  inversion is killed by the relevant fixed-point condition.

```text
U1_C4_SOURCE_SYMMETRY = PASS | TYPE-P | premises: DoR-008
```

### U1-008-C5 — representation naturality

Pass condition: any allowed C0 intertwiner preserving `e_plus`, `e_minus`,
star, and the source maps also intertwines `epsilon`, `eta_CTP`, `Theta`, and
the symmetric/reality restrictions. This holds because every U1 operation is
defined on branch/source labels before representation and then transported by
`pi_C0`.

Failure mutation: a representation change that identifies the two branches
or fails to preserve star is not an allowed C0 representation change and
fails the certificate.

```text
U1_C5_REPRESENTATION_NATURALITY = PASS | TYPE-P | premises: DoR-008
```

### U1-008-C6 — scope exclusion

The construction contains no scalar functional, state, evolution, quotient,
measure, effect, contact, Ward identity, response kernel, or value. In
particular, the complete-Qspec amplitude was used only as an independent
Hermiticity cross-check and not as construction data.

```text
U1_C6_SCOPE_EXCLUSION = PASS | TYPE-P | premises: DoR-008
U2_OR_U3_DATUM_PULLED_FORWARD = false | TYPE-S |
  scope: the exact fields and operations of U1_008
```

### 5.1 Executed algebraic verifier

An independently coded finite verifier checked:

```text
branch involution                  PASS
T_CTP^T eta_CTP T_CTP             [[0,1],[1,0]]
source reality involution squared PASS
antisymmetric bilocal rejection   PASS
```

The verifier also used explicit failure samples: a branch-unexchanged reality
map and a nonzero antisymmetric two-slot source. Both were rejected by the
relevant certificate. This computes only finite convention identities; it
evaluates no physical quantity.

```text
U1_008_CERTIFICATES_C1_TO_C6_PASSED = true | TYPE-P | premises: DoR-008
```

## 6. Adversarial boundary checks

### 6.1 Downstream CTP identity attack

Attempt: define U1 directly from
`Z_K[A_+,A_-]=omega_in(W[A_-]^dagger W[A_+])`.

Rejected. That formula consumes state and evolution and would pull U2 into
U1. The kinematic `Theta_F` construction provides the same branch exchange
without either.

### 6.2 `sharp = Theta` attack

Attempt: reuse the C0 source-map adjoint as the physical CTP reality map.

Rejected. The displayed `sharp` maps invert character labels and reverse
bilocal slots but do not exchange branches. U1 needs both structures and keeps
them distinct.

### 6.3 Charge/branch identity attack

Attempt: identify CTP `+/-` with source charge-conjugate sectors.

Rejected by the ratified proposal's identity fence at `:701-706` and by the
branch embedding certificate. The U1 bar operation acts on CTP branch labels,
not charge sectors.

### 6.4 Continuum inflation attack

Attempt: transport the sequential label `lambda` to a continuum field/spacetime
index `(mu,x)` without DoR-007.

Rejected. U1_008 is exact on the source domains C0_008 actually has. The
continuum extension remains separately Type-U.

### 6.5 Finite-incidence transport attack

Attempt: claim U1_008 already acts on `K_square` or the S/R/E planes by name
matching.

Rejected. Q-215 proves that a finite-incidence realization functor and an
S/R/E operator embedding are two separate, noncanonical map classes. Neither
is supplied here.

```text
U1_008_ADVERSARIAL_BOUNDARY_CHECKS_PASSED = true | TYPE-P |
  premises: DoR-008
```

## 7. What is built, and what remains downstream

| Object or test | Standing after this construction |
|---|---|
| U1 conventions on the actual `C0_008` branch/source interface | **BUILT, `TYPE-P`** |
| Common-origin descent `d_U1` from B0 | **TYPE-U** |
| Continuum compound index `(a,mu,x)` | **TYPE-U**, waits on DoR-007 |
| Action of U1 on the completed physical quotient | **TYPE-U**, waits on U3 |
| Contact, boundary, Ward, inverse, or response consequences | **not U1; downstream** |
| Restriction to `K_square` and S/R/E finite carriers | **TYPE-U**, waits on Q-215 map classes |

The earlier package status
`complete_physical_branch_metric_reality_index_package_derived = false`
is therefore narrowed, not silently flipped. The U1 convention object now
exists conditionally on `C0_008`; its common-origin derivation, continuum
realization, quotient descent, and finite-incidence restriction still do not.

## 8. Scope, roots, exclusions, and queries

Roots entered:

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha-program-archive/cleanroom_output
/Users/bgm/MB Work/alpha-program-archive/workspace
/Users/bgm/MB Work/alpha_supervision
```

Exclusions:

```text
.git
seal sidecars as content authorities
superseded versions as current authority
a32_holdout/custodian_private
```

Word-boundaried, case-insensitive searches covered:

```text
branch metric | branch orientation | contour orientation
reality involution | CTP reality | Hermiticity involution
Keldysh | A_c | A_delta | eta_CTP | branch_metric
forward branch | backward branch | opposite-backward
compound index | source symmetry | branch embeddings
```

The exact-formula sweep found no pre-existing literal `eta_CTP`, `g_CTP`,
`c_CTP`, or displayed `diag(+1,-1)` definition. The metric in Section 2.2 is
therefore an executed representation of the already-sealed unit branch signs,
not a quotation falsely presented as one. The sweep did find downstream CTP
Hermiticity implementations; they were excluded as U1 inputs because they
consume state or dynamics.

`a32_holdout/custodian_private/` was not entered, listed, searched, opened,
summarized, or read.

## 9. Final status

```text
U1_REQUIRED_COMPONENTS_INSTANTIATED = true | TYPE-P | premises: DoR-008
U1_008_ASSEMBLY_TRACE_FROZEN = true | TYPE-P | premises: DoR-008
U1_008_CERTIFICATES_C1_TO_C6_PASSED = true | TYPE-P | premises: DoR-008
U1_008_EXCLUSION_LIST_PASSED = true | TYPE-P | premises: DoR-008

d_U1_PREMISE_LEVEL_TOTAL = true | TYPE-P | premises: DoR-008
d_U1_DERIVED = false | TYPE-U |
  would-build: independently derive the common-origin B0-role source and its
               U1 descent certificate

U1_CONTINUUM_REALIZATION_COMPLETE = false | TYPE-U |
  would-build: DoR-007 discrete-to-continuum theorem
U1_PHYSICAL_QUOTIENT_COMPATIBILITY_EXECUTED = false | TYPE-C |
  constraint: U3 physical quotient/domain package does not yet exist |
  release: construct U3, descend all U1 fields, and execute naturality tests
U1_FINITE_INCIDENCE_RESTRICTION_EXECUTED = false | TYPE-C |
  constraint: Q-215's finite-incidence and S/R/E bridge maps are unbuilt |
  release: build the maps and execute DoR-008's standing falsifier

TASK2C_U1_INSTANCE_EXISTS = true | TYPE-P | premises: DoR-008
TASK2C_COMMON_ORIGIN_DESCENT_COMPLETE = false | TYPE-U

PHYSICAL_VERDICT = NO_VERDICT
CONSTRUCTION_VERDICT = U1_ASSEMBLED_CONDITIONALLY_AT_C0_SCOPE

alpha_computed = false [TERMINAL_FENCE_DECLARATION]
proof_authorized = false [TERMINAL_FENCE_DECLARATION]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION]
coupling_evaluation_authorized = false [TERMINAL_FENCE_DECLARATION]
production_authorized = false [TERMINAL_FENCE_DECLARATION]
```

No state, dynamics, quotient, measure, effect, contact, response, coupling,
scale, root, spectrum, eigenvalue, beta function, absolute interval, or
measured comparison was built, computed, or evaluated. No register, git,
commit, push, deployment, or publication action was performed.
