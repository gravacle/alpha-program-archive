# Stage-8 T7 Completed-Continuum Response Provenance Spec v001

Date: 2026-07-24

## Purpose

Determine whether the exact completed-record history sum has a canonical,
regulator-independent continuum connection response in the declared flat
asymptotic branch.

This is a target-free provenance gate. It may derive the continuum response
object or identify its exact obstruction. It may not choose a regulator,
phase prescription, counterterm, norm, or operator because that choice gives
a preferred coupling value.

## Pinned authorities

| File | Limited role | SHA-256 |
|---|---|---|
| `BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md` | Selects the normalized complex completed-record transition amplitude | `6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb` |
| `R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md` | Supplies the continuum parent, causal-cell multiplication operators, and quasifree state | `40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9` |
| `BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001.md` | Supplies the stationary free contour and polarization | `6f6b822ac8ccf9ea19659f4ccf811268f60a27a361f817ee6513479d63b62546` |
| `STAGE8_T7_GAUSSIAN_PATH_SUM_REDUCTION_RESULT_V001.md` | Supplies the exact finite signed sum of valid determinant histories | `1fd82d0d42c7d7b1369adfa0e0061c80044afc847f7dae2f066bdfb89165e56f` |
| `STAGE8_T7_THREE_SITE_BASELINE_SCOPE_ERRATUM_V001.md` | Forbids promotion of the three-site regression to the physical regulator | `f1dc38f8a08b9e21675dc35fc91ffbd5e0b94d3feb5113f850c09a19b89bbd38` |
| `STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_RESULT_V001.md` | Supplies finite restrictions of the continuum negative-frequency covariance | `3a6ff6173573a7d9dd99bdd1a6bb7eaa02c433ab50bc769e144d94c983b4f0ff` |
| `R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md` | Supplies the intrinsic causal-cell measure | `e4cfaef14309b3acf5674f8c8faee756f744fec4691d5e01d9de0fa422592be2` |
| `FORK_8_CAUSAL_DIRECT_LIMIT_PROMOTION_RESULT_V001.md` | Selects the Lorentz-covariant causal-cell continuum as the physical architecture | `f84d5b5e8789e5e336db53265cc87dd25f5efddf1cd9c8931f1e521240125d4a` |
| `STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_V001.md` | Fixes the T7 zero-free, cluster, and Hessian obligations | `85d24996987278b285d63b8fe15a8732e55664e7c1b09063617b66cb4bc926b4` |
| `STAGE7_QSPEC_REVIEW_CANDIDATE_V002.md` | Preserves the open regulator, finite-renormalization, and CTP slots | `5026afb89b52ead9f309168cb2fa4f06b81039f8dd01b8940f40e64aad679a7e` |

## Continuum object under adjudication

Let

```text
h_K(t;A)
 =h_0(A)
  +sum_(c in K) v_c(t) M_c(t) S_n tensor c_c
```

be the pinned finite-cell one-particle parent. The incoming quasifree
polarization is `P_-=1_(-infinity,0)(h_0(0))`.

For each completed cell, diagonalize the record incidence operator:

```text
lambda in {-sqrt(2),0,+sqrt(2)};
w_lambda=<-pointer|lambda><lambda|ready>.
```

For a history `sigma:K->{-,0,+}`, let `u_sigma,K(A)` be the one-particle
propagator obtained by replacing each `c_c` by its eigenvalue
`lambda_sigma(c)`.

For an admissible finite Galerkin restriction `Q_n`, with occupied isometry
`V_n` for the restricted negative-frequency covariance, define only at the
finite stage:

```text
a_K,n(A)
 =sum_sigma [
    product_(c in K) w_sigma(c)
  ] det[V_n^dagger u_sigma,K,n(A)V_n].
```

No single-determinant shortcut is admissible.

The desired continuum object, if it exists, is:

```text
Z_K(A)=lim_(n->infinity) a_K,n(A)/a_K,n(0).
```

Its logarithmic Hessian is considered only after the normalized amplitude,
its common phase, and its zero-free neighborhood are established.

## Admissible Galerkin class

No one finite lattice is the physical theory. An admissible family must:

1. have nested orthogonal projections `Q_n -> I` strongly;
2. preserve charge, the record grading, and the disclosed spinor typing;
3. converge on a common core for `h_0`;
4. approximate every compact causal-cell multiplication operator `M_c(t)`
   strongly and uniformly in the integrated interaction norm;
5. retain the same intrinsic causal envelope and no fitted pulse profile;
6. introduce no zero-mode filling, thermal parameter, finite counterterm,
   or coupling normalization; and
7. admit at least two cofinal realizations not related by relabeling one
   finite matrix.

The proof may use an arbitrary member of this class only after showing that
the final object is independent of that member.

## Obligations

### C1. Exact record cancellation

Compute the weights and all moments needed for power counting. Prove
algebraically, before numerical evaluation, which Duhamel histories vanish.
In particular, determine whether every completed cell must occur at least
twice in every surviving term.

### C2. Finite-stage identity

Prove the signed determinant-history formula from the finite quasifree
parent for every admissible `Q_n`. The proof must not rely on the old
three-site periodic derivative. That model remains a regression fixture
only.

### C3. Implementability and relative phase

Determine whether the completed sum defines one canonical lift of the
Bogoliubov evolution in the asymptotic quasifree representation. A list of
separately chosen determinant phases is not an amplitude.

If only a determinant line, `det_p`, or phase-equivalence class exists,
state exactly which extra datum would be needed and whether it changes the
logarithmic Hessian.

### C4. Ultraviolet and finite-renormalization audit

Expand the normalized completed amplitude in connection insertions and
record-cell insertions. Use the exact moment cancellations, locality,
gauge covariance, and Ward identities to classify every potentially
divergent local term.

The audit must explicitly decide whether a finite local `F^2` ambiguity
survives. The adopted absence of an independent primitive `F^2` coefficient
may not silently be used as a finite renormalization condition.

### C5. Regulator independence

If C3 and C4 permit a continuum object, prove that the normalized amplitude
and its connection Hessian have the same limit for every admissible
Galerkin family. A numerical match between two finite cutoffs is a check,
not the proof.

### C6. Boundary of this gate

This gate does not:

```text
choose the physical connection-field norm;
prove the volume-uniform zero-free neighborhood;
derive the linked-cluster thermodynamic density;
compute kappa_record;
compute a coupling;
or compute alpha.
```

Those obligations remain downstream even if continuum provenance passes.

## Predeclared verdicts

```text
if C1-C5 are proved with no additional physical datum:
  COMPLETED_CONTINUUM_RESPONSE_PROVENANCE_DERIVED

if a common-Fock or determinant-line lift cannot be constructed:
  COMPLETED_CONTINUUM_RESPONSE_IMPLEMENTABILITY_BLOCKED

if a phase or finite local F^2 term remains freely selectable:
  COMPLETED_CONTINUUM_RESPONSE_FINITE_RENORMALIZATION_BLOCKED

if different admissible Galerkin families give inequivalent limits:
  COMPLETED_CONTINUUM_RESPONSE_REGULATOR_DEPENDENCE_BLOCKED

otherwise:
  COMPLETED_CONTINUUM_RESPONSE_PROVENANCE_INCOMPLETE
```

No favorable finite value can alter these verdict rules.

## Fixed status

```text
completed_continuum_response_provenance_derived = false
physical_connection_norm_frozen = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
