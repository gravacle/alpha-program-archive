# BID Consolidated Hostile Audit Matrix v005

Date: 2026-07-23

## Purpose

This matrix prevents serial blocker review. Every audit evaluates every row
against one immutable version, but it distinguishes a sealed specification
from an executed result.

Finding and repairing one failed row invalidates that version. The repair
must increment the version and rerun every row, including rows that previously
passed. No delta-only review can seal BID.

## Invalidation rule

An edit to a row's input invalidates that row and every row below it. An edit
to the category, carrier, Hilbert metric, differential, orientation law,
response rule, or seal protocol invalidates the entire matrix.

## Stage semantics

`SPEC-SEAL` means:

```text
all A01-A29 tests and failure conditions are completely and consistently
specified without a target value;
A30-A34 have a literal fail-closed dependency graph;
all unexecuted result rows are PENDING-BY-DESIGN rather than silently passed;
and every result, coupling, alpha, proof, and result-seal flag remains false.
```

`CORE-RESULT-SEAL` additionally requires executed passes through A30 on one
immutable lineage. `FINAL-CLAIM-SEAL` requires executed passes through A34,
including the external holdout and independent reconstruction.

No report may use the unqualified word `SEAL`. Each stage requires agreement
from at least:

1. one formal type/category review;
2. one physics/operator review; and
3. one independent full-stack red-team review.

Any reviewer may return `NO-SPEC-SEAL`, `NO-CORE-RESULT-SEAL`, or
`NO-FINAL-CLAIM-SEAL`. Majority vote is not used.

## Matrix

| ID | Layer | Required hostile check | Initial status |
|---|---|---|---|
| A01 | Provenance | Every authority exists and matches its pinned hash. | PENDING |
| A02 | Target firewall | No measured alpha, mass, endpoint, or residual enters construction; historical target awareness and every target-aware structural premise are disclosed; final evidential independence requires A32 rather than retroactive blindness. | PENDING |
| A03 | Status firewall | Every computation, coupling, alpha, proof, and seal flag remains false before its gate. | PENDING |
| A04 | Object separation | Comparison group, associated vertex bundle/gauge action, common ray quotient, endpoint carrier built from the actual object fibers, chain carrier, tangent cochains, and face carrier remain distinct and are connected only by canonical explicit maps. No basis or isometry is used before Gate 3. | PENDING |
| A05 | Comparison group | The common action-character quotient is well-defined, continuous, and faithful; finite alternatives are classified rather than dismissed by fit; the three U(1) roles are related without identification. | PENDING |
| A06 | First opening | Rooted-star and 4+3 dimensions follow only from the disclosed premise and are never counted as evidence. | PENDING |
| A07 | Category | Objects include the first-opening subset and its `{M,Q,G}` label map; roots, orientations, attaching maps, discrete connection, identities, label-preserving morphisms, and composition are fully typed through degree two. The bare and handle-forgetful functors state exactly which decorations they erase. | PENDING |
| A08 | Cell carriers | C0, C1, C2 fibers, orientation reversal, gauge action, and J0/J1/J2 are explicit and mutually consistent. | PENDING |
| A09 | Hilbert competitors | All coherent positive Hermitian forms, including nondiagonal forms and degree two, enter before the isometry hypothesis. | PENDING |
| A10 | Hilbert conclusion | Identity cell metrics are derived from the declared conditions, not asserted by status. | PENDING |
| A11 | Differential competitors | Full complex (a,b) family, zero cases, D_x continuum, edge/handle variation, and phases are included. | PENDING |
| A12 | Orientation | Reversal on carriers is involutive and gauge covariant; independent reversed coefficients are admitted and their swap law is derived without forcing equal weights. | PENDING |
| A13 | Public collapse | Full nonzero `(c,d)` family is admitted; operational closure axioms, colimit ray, naturality, orientation coherence, and path composition must derive `[c:d]=[1:1]`; no absolute cocone magnitude is claimed. | PENDING |
| A14 | Boundary closure | Orientation, colimit selection, closure, naturality, equivalence, and one-record normalization are applied in frozen order and leave one class or fail. | PENDING |
| A15 | Naturality | Differential naturality is well-typed; full-B intertwining is not substituted. | PENDING |
| A16 | Equivalences | Only declared unitary/gauge/orientation equivalences and nonzero rescaling of the closure-constraint covector are used; no positive metric or dimensionful scale equivalence is hidden as coordinates. | PENDING |
| A17 | Adjoint | D-sharp follows from the derived Hilbert metric and agrees with the directional difference under the exact carrier convention. | PENDING |
| A18 | Filtration | A target-free universal `*`-algebra, augmentation homomorphism, kernel ideal, and `I`-adic completion are explicit; a translation-complete test object supplies global unitary shifts; the global represented holonomy is distinguished from each local fiber block; no extension to the completion is silently assumed. | PENDING |
| A19 | Face curvature | Boundary orientation, path order, global direct-sum holonomy, local restriction, gauge law, and base-point endomorphism are exact; the formal I-adic log is separated from the holomorphic principal physical log, and the Taylor series is used only on its norm-convergence domain. | PENDING |
| A20 | Curvature order | Universal ideal membership is separated from represented exact order; `F_pi^n=pi(I^n)` and `gr_pi^n` are explicit; exact represented order is claimed only after a nonzero represented associated-graded symbol is exhibited. | PENDING |
| A21 | Clifford lift and relativistic source typing | `3+1`D/Lorentz/spin/CPT and Dirac-4 are disclosed inputs; the full Dirac particle/antiparticle carrier, hypersurface inner product, vector-`U(1)` action, and CPT antiunitary are explicit. The CPT audit must reject the legacy gamma5-only shortcut, type the geometric normal pushforward, target tetrad/coframe, future reorientation, and oriented one-cell sign, test different-normal `h_n`-isometric transport with the weighted adjoint, compute rather than insert the cellular phase-constraint nullspace, and exercise nonzero neutral plus charged/neutral negative controls. Raw incidence and its CPT-selected quadrature remain distinct and have the audited common square. Any chiral-odd source-record map is derived as a Lorentz-covariant boundary intertwiner. Axial reduction must construct charge conjugation and parity separately, compute their combined action on the complete scalar/pseudoscalar family, disclose the regulator and topological branch, prove that the discrete axial map preserves the regulated Dirac domain, account for boundary/eta phases or use an explicit closed regulator, derive rather than insert spectral pairing, evaluate the Fujikawa Jacobian and determinant ratio, and reject a nonzero-index/unpaired-zero-mode control; endpoint rephasing alone cannot establish physical sign equivalence. The Dirac-square identity, pullback, sign, and Pauli scope must remain consistent. No finite-cell frequency, anomalous moment, mass, or alpha evidence is claimed. | PENDING |
| A22 | Primitive/effective scope | Postulate-based exclusions are separated from incompatibility theorems and generated coefficients. | PENDING |
| A23 | Physical amplitude and action normalization | The complete competitor family `Gamma_c=-c log|A|`, `c>0`, is admitted. Fubini-Study geometry is only a check. Pass requires a complete physical transition amplitude from the sealed charged specification and the identity `Gamma=-log|A|`; any independent power `A^c`, multiplicity, or measure normalization leaves absolute stiffness open. | PENDING |
| A24 | Record interval, active-handle control, source-parent family, physical amplitude, and extensive response | The complete family `exp(-i tau B)`, `tau>0`, is admitted. A target-free durable-record/orthogonality rule must derive one least positive nondegenerate `tau_R`. Because the handle-conditioned interval does not complete the full three-handle star, the charged source-flux operator and its source/access projector, or a complete composite-handle operator, must be derived from the sealed current rather than hard-coded. The source carrier must separate unresolved multiplicity factors from structural Dirac data; charge-only naturality acts only on the former and its actual commutant must be computed. Charged control must be derived as the unique projection-module restriction of the already normalized parent incidence operator, with the complete control-map family solved and a rescaled competitor rejected by retraction; the interval may only crosscheck the result. The complete source-decorated incidence family must include arbitrary positive source metrics, all natural gauge/Lorentz-covariant chiral-odd columns, alternative intermediate vertices, and edge refinements; exact transfer may select weights only after that family is exhaustive. The root survival amplitude, which is exactly zero at the handle interval, is a mandatory rejected response object. Public record semantics must independently derive a nonzero physical final boundary condition and a normalized amplitude with a volume-uniform zero-free neighborhood. The record theory must derive or explicitly adopt a strong symmetric-monoidal functor into `(Hilb,tensor)` before tensor composition is used. Connected primitive dynamics additionally requires an explicitly adopted or independently derived global-boundary-descent/quasi-free-completeness rule. Its audit must retain one global fermionic source CAR carrier and separate even record factors, recover the actual SP17 one-cell operator, test relabeling/orientation covariance, compute connected shared-support structure in the primitive operator rather than borrowing a term from its square, recover the operator-valued CAR lift on the one-source sector, and reject a quartic competitor that agrees on vacuum/one-source sectors without target comparison. It must still derive connected preparation and a thermodynamic domain containing `tau_R`. The V010 normalized direct-sum global ray and its analytic `kappa_L->0` result are mandatory rejected competitors; no later volume factor is permitted. | PENDING |
| A25 | Preparation, tangent, and local extraction | Preparation is proved unique on a target-independently derived domain such as `P(im J_r,L)`, with all translation-invariant competitors enumerated. Connection cochains, `d0`, `d1`, stabilizers, horizontal quotient, operator tangent, and real/complex face maps are typed. Normalized real sine/cosine modes, normalized polarizations, Hermitian rows, and finite-volume factors are exact. The rank-20 quotient has an explicit normalized `T_top` and Frobenius-orthogonal section. Locality requires a uniform full-neighborhood analytic expansion with certified remainder, not finite ray sampling. | PENDING |
| A26 | Flux lift | Every flux in `F_phys=im(d1)` has one representative-independent minimum-norm lift; individual unit faces outside that image are not assigned a lift; surviving zero-flux additions fail. Complex Fourier analysis must reproduce the real response. | PENDING |
| A27 | Geometry, anisotropy, and cellulation | The Lorentzian Hodge matrix is generated from the frozen metric/orientation and satisfies `star^2=-I`. The exact tetrad/Jacobian map induces the bivector and face measures and removes coordinate anisotropy without an inserted compensator. The local coefficient is invariant under a sealed class of regular-CW refinements and elementary subdivision/common-refinement moves; one hypercubic sequence alone cannot establish universality. | PENDING |
| A28 | Primitive/full charged separation | The primitive gate may use no determinant, heat kernel, Wick rotation, regulator, counterterm, threshold, or source-mass identification and may output only `kappa_record`. A distinct downstream `Q_spec` must use one global fermionic CAR source algebra plus distinguishable record factors, and include the spatial Dirac kinetic operator, charged current, antiparticles, gauge/ghost/edge sectors, connected gluing and overlap terms, CTP preparation, durability, measure/regulator, Ward identity, full source pole/residue, induced transverse response, thresholds, decoupling, matching, and the zero-momentum Thomson limit. Only `kappa_Thomson` may enter `alpha(0)=1/(4pi kappa_Thomson)`. | PENDING |
| A29 | Loop preregistration | Complex, gauge, matrix, phase, carrier, outputs, and symbolic/numerical roles are immutable and mutually consistent. | PENDING |
| A30 | Core seal | An independent evaluator, not manuscript status strings, computes the noncyclic stage DAG. `CORE-RESULT-SEAL` requires `SPEC-SEAL`, Gates 1-5, loop output, three new content-addressed core reviews, and an independent core reconstruction on one immutable lineage. Core output is limited to primitive structural results and `kappa_record`; alpha evaluation is impossible at this stage. | PENDING |
| A31 | Parent comparison | Literal dependency: CORE-RESULT-SEAL and a predeclared comparison map. Parent access cannot alter BID or any holdout commitment. | PENDING |
| A32 | External holdout | An independently generated exhaustive public-registry snapshot has a fixed source/query/cutoff, canonical serialization, canonical IDs, and deterministic deduplication. An outcome-blind custodian publishes salted commitments. A future external randomness beacon selects among eligible structure-sensitive targets for which BID and at least one same-alpha comparator predict different outcomes. The full prediction is sealed before unmasking; contamination, empty set, registry drift, commitment failure, or post-unmask edit is fail-closed. | PENDING |
| A33 | Full charged reconstruction | After core and parent comparison, a separately sealed implementation constructs complete `Q_spec`, derives the Ward-consistent threshold-matched Thomson response, and only then computes alpha. An independent implementation reproduces every symbolic and numerical result from sealed inputs. | PENDING |
| A34 | Claim gate | Literal dependency: passed A01-A33, passed structure-sensitive A32, computed Thomson alpha, independent end-to-end reconstruction, and three new final-claim reviews. `proof_authorized` is true if and only if the independent evaluator computes `FINAL-CLAIM-SEAL=true`. | PENDING |
| A35 | V010/V011 regression firewall | Every blocker recorded in `BID_FULL_STACK_REVIEW_LEDGER_V003.md` has an executable check. In particular, the evaluator must reproduce and reject the V010 zero-stiffness response and the zero survival-amplitude response, admit `c` and `tau` competitors, reject primitive/Thomson conflation, and fail on any missing physical-amplitude, zero-free-domain, active-handle provenance, full Dirac/antiparticle typing, Lorentz/CPT covariance, computed CPT phase nullspace, explicit tetrad/normal reorientation, different-normal weighted-adjoint transport, nonzero neutral control, separately constructed C/P and combined CP actions, axial-domain invariance, boundary/eta accounting, derived spectral pairing, zero-index anomaly/determinant evaluation, nonzero-index negative control, multiplicity/Dirac factorization, projection-module control-map uniqueness, complete source-incidence family, one-global-source-CAR/even-record composition, associative shared-boundary descent, relabeling/orientation covariance, primitive rather than squared-operator overlap structure, operator-valued quasi-free CAR lift, rejected quartic competitor, physical pole/residue, normalization, topology, locality, anisotropy, cellulation, seal, holdout, strong-monoidal-target, statistics, gluing, overlap-interaction, ordering, connected-preparation, or record-interval-domain repair. The finite incidence-weight result may not satisfy any of these source-parent obligations by implication. | PENDING |

## Current state

This matrix is an audit protocol only.

```text
BID_consolidated_matrix_sealed = false
BID_v011_specification_sealed = false
BID_core_result_sealed = false
BID_parent_comparison_completed = false
BID_final_claim_sealed = false
independent_end_to_end_reconstruction_sealed = false
primitive_record_stiffness_computed = false
physical_Thomson_stiffness_computed = false
alpha_computed = false
proof_authorized = false
```
