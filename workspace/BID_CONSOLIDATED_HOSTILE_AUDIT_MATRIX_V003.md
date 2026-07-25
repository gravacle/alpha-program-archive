# BID Consolidated Hostile Audit Matrix v003

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
A30-A34 have an explicit dependency graph;
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
| A04 | Object separation | Comparison group, associated vertex bundle/gauge action, common ray quotient, endpoint carrier, chain carrier, tangent cochains, and face carrier remain distinct and are connected only by explicit functors. | PENDING |
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
| A16 | Equivalences | Only declared unitary/gauge/orientation equivalences are used; positive metric rescaling is not hidden as coordinates. | PENDING |
| A17 | Adjoint | D-sharp follows from the derived Hilbert metric and agrees with the directional difference under the exact carrier convention. | PENDING |
| A18 | Filtration | A target-free universal `*`-algebra, augmentation homomorphism, kernel ideal, and `I`-adic completion are explicit; a translation-complete test object supplies global unitary shifts; no extension to the completion is silently assumed. | PENDING |
| A19 | Face curvature | Boundary orientation, path order, holonomy, logarithm domain, gauge law, and base-point endomorphism are exact. | PENDING |
| A20 | Curvature order | `W-I` and `Log W` are proved to lie in the required ideal power; exact order is claimed only after a nonzero associated-graded symbol is exhibited. | PENDING |
| A21 | Clifford lift | `3+1`D/Lorentz/spin/CPT and Dirac-4 are disclosed inputs; the Dirac-square identity, pullback, sign, and Pauli scope are consistent; no anomalous moment or alpha evidence is claimed. | PENDING |
| A22 | Primitive/effective scope | Postulate-based exclusions are separated from incompatibility theorems and generated coefficients. | PENDING |
| A23 | Response selector | Standard Born/Fubini-Study kinematics are explicitly disclosed and hash-pinned as imported; no passive-symmetry uniqueness claim is made; the covariance kernel is obtained by differentiating the explicit orbit `f(A)=[exp(-iB_A)r]`. | PENDING |
| A24 | Root/interval | Root ray and self-adjoint domain are exact; an external target-free interval authority must return one positive Lorentz-scalar stationary record cell, nondegenerate physical Hessian, and consistent `T_R,V_R`, or absolute response fails. | PENDING |
| A25 | Tangent complex | Connection cochains, `d0`, `d1`, componentwise stabilizers, real/complex face map, horizontal quotient, and operator tangent map are explicit and typed. | PENDING |
| A26 | Flux lift | Every flux in `F_phys=im(d1)` has one representative-independent minimum-norm lift; individual unit faces outside that image are not assigned a lift; surviving zero-flux additions fail. | PENDING |
| A27 | Maxwell completion | Rotation/parity first yield independent `kappa_E,kappa_B`; only an independently constructed Hodge-duality action commuting with the response may equate them; the positive energy form is not equated with an indefinite metric; a separately derived symplectic/Legendre map yields the Lorentzian action. | PENDING |
| A28 | Functional quarantine | Determinants, heat kernels, Wick rotations, regulators, and counterterms cannot enter the primitive response gate. | PENDING |
| A29 | Loop preregistration | Complex, gauge, matrix, phase, carrier, outputs, and symbolic/numerical roles are immutable and mutually consistent. | PENDING |
| A30 | Core seal | Gates 1-5, the loop output, all three content-addressed hostile reviews, and an independent reconstruction seal without opening the historical parent. | PENDING |
| A31 | Parent comparison | Parent opens only after a content-addressed core seal and cannot alter BID. | PENDING |
| A32 | External holdout | Unused observable and complete prediction map are sealed before alpha evaluation. | PENDING |
| A33 | End-to-end reconstruction | After the external holdout and charged-response calculation, an independent implementation reproduces every symbolic and numerical result from sealed inputs; this is distinct from A30's independent core reconstruction. | PENDING |
| A34 | Claim gate | Alpha is not claimed unless every preceding row passes on one immutable lineage. | PENDING |

## Current state

This matrix is an audit protocol only.

```text
BID_consolidated_matrix_sealed = false
BID_specification_sealed = false
BID_core_result_sealed = false
independent_end_to_end_reconstruction_sealed = false
alpha_computed = false
proof_authorized = false
```
