# BID Consolidated Hostile Audit Matrix v004

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
| A07 | Category | Objects, roots, orientations, attaching maps, discrete connection, morphisms, and composition are fully typed through degree two. | PENDING |
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
| A21 | Clifford lift | `3+1`D/Lorentz/spin/CPT and Dirac-4 are disclosed inputs; the Dirac-square identity, pullback, sign, and Pauli scope are consistent; no anomalous moment or alpha evidence is claimed. | PENDING |
| A22 | Primitive/effective scope | Postulate-based exclusions are separated from incompatibility theorems and generated coefficients. | PENDING |
| A23 | Response selector | The general finite pure-state Born/Fubini-Study premise is disclosed as a standard input, not overstated as a consequence of the two-path authority. Fidelity loss fixes the metric normalization and `Gamma=-(1/2)log(Fidelity)` fixes the quadratic action Hessian, forbidding factor-two/four conventions. The covariance kernel is obtained only by differentiating the explicit orbit. | PENDING |
| A24 | Response object and scale | The odd periodic complexes, trivial-holonomy gauge class, translation-selected covariantly constant root ray, self-adjoint dimensionless one-record generator, full domain, and unit orbit interval are frozen without response access. Four-dimensional `ell^4`/`ell^-4` cancellation is proved; anisotropic factors must be exhausted by the frozen tetrad/Jacobian map, leaving one shape-independent scalar; no physical interval is required for dimensionless alpha. | PENDING |
| A25 | Tangent/local extraction | Connection cochains, `d0`, `d1`, componentwise stabilizers, horizontal quotient, operator tangent, and real/complex face map are typed. The complete exact-mode design is proved to have rank 20 and only the `F wedge F` topological null direction; a preregistered rank-20 Fourier design plus the predeclared parity-zero coefficient reconstructs the local `6x6` response tensor with paired sine/cosine agreement, verification rows, locality, and a certified fixed-momentum odd-L zero-momentum limit. Divergent/nonanalytic behavior cannot be relabeled as another scale. | PENDING |
| A26 | Flux lift | Every flux in `F_phys=im(d1)` has one representative-independent minimum-norm lift; individual unit faces outside that image are not assigned a lift; surviving zero-flux additions fail. Complex Fourier analysis must reproduce the real response. | PENDING |
| A27 | Maxwell/action completion | The Lorentzian Hodge matrix is generated from the frozen metric/orientation and satisfies `star^2=-I`; rotation/parity and anisotropy tests precede the exact Hodge commutator. A declared canonical boundary phase-space premise yields the Lorentzian action with no free symplectic scale, and the frozen unit-character convention maps `kappa_BR` to `alpha=1/(4pi kappa_BR)`. | PENDING |
| A28 | Functional quarantine | Determinants, heat kernels, Wick rotations, regulators, and counterterms cannot enter the primitive response gate. | PENDING |
| A29 | Loop preregistration | Complex, gauge, matrix, phase, carrier, outputs, and symbolic/numerical roles are immutable and mutually consistent. | PENDING |
| A30 | Core seal | Literal dependency: SPEC-SEAL plus Gates 1-5, loop output, three new content-addressed core reviews, and an independent core reconstruction, all on one immutable lineage without opening the historical parent. | PENDING |
| A31 | Parent comparison | Literal dependency: CORE-RESULT-SEAL and a predeclared comparison map. Parent access cannot alter BID or any holdout commitment. | PENDING |
| A32 | External holdout | An external custodian seals an outcome-masked candidate universe and commitments. An objective eligibility predicate plus `SHA256(H_spec||canonical_id)` selects the target; the full prediction map is sealed before unmasking; contamination, empty-set, commitment, and post-unmask edit failures are fail-closed. | PENDING |
| A33 | End-to-end reconstruction | After parent comparison, A32, charged response, and alpha calculation, an independent implementation reproduces every symbolic and numerical result from sealed inputs; this is distinct from A30's independent core reconstruction. | PENDING |
| A34 | Claim gate | Literal dependency: parent comparison, passed A32, charged response and alpha computation, passed A33, and three new final-claim reviews. `proof_authorized` is true if and only if FINAL-CLAIM-SEAL is true. | PENDING |

## Current state

This matrix is an audit protocol only.

```text
BID_consolidated_matrix_sealed = false
BID_v010_specification_sealed = false
BID_core_result_sealed = false
BID_parent_comparison_completed = false
BID_final_claim_sealed = false
independent_end_to_end_reconstruction_sealed = false
alpha_computed = false
proof_authorized = false
```
