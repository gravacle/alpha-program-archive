# Causal Direct-Limit Covector-Ray Lift Result

## Verdict

```text
QUASILOCAL_STATE_LIFT_ONLY
```

The finite public-collapse covector ray does not survive as a nonzero
bounded covector in the direct-limit Hilbert space. It does survive as a
compatible state on the quasi-local outgoing-record algebra, conditional on
BID's inherited symmetric-monoidal composition law for disjoint independent
record cells.

No alpha or measured physical constant entered this derivation.

## 1. Why the Hilbert-covector lift fails

Let

```text
c_N=sum_(j=1)^N e_j in l2({1,...,N}).
```

The three canonical normalizations exhaust the immediate choices:

```text
||c_N||=sqrt(N)                 -> unbounded;
||c_N/sqrt(N)||=1              -> weak limit zero;
||c_N/N||=1/sqrt(N)            -> norm limit zero.
```

For the unit-normalized sequence and any `x in l2`, approximate `x` by a
fixed finite-support vector. Its overlap with `c_N/sqrt(N)` vanishes as
`N` grows, while the tail is uniformly controlled by the approximation.
Therefore the weak limit is zero. No nonzero bounded Hilbert covector is
obtained by normalization.

This is not a failure of the finite covector-ray theorem. It says that a
macroscopic public record is not one normalizable vector obtained by adding
infinitely many one-cell covectors.

## 2. The quasi-local lift

For

```text
A_N=tensor_(j=1)^N M_2,
iota_N(A)=A tensor I,
```

the finite public-label states

```text
omega_h^N(A)=<h^tensor_N|A|h^tensor_N>
```

obey

```text
omega_h^(N+1)(iota_N(A))=omega_h^N(A).
```

The audit checked this equality on a nontrivial complex Hermitian local
observable. The equality is algebraic and therefore holds for every local
observable. The compatible family defines a unique state `omega_h` on the
quasi-local inductive-limit algebra.

For

```text
M_N=(1/N) sum_(j=1)^N Z_j,
```

and an observable `O` supported on a fixed `m` cells,

```text
||[M_N,O]|| <= 2m ||O||/N -> 0.
```

Thus `M_N` is a central sequence. Its limiting expectation distinguishes the
two public labels:

```text
omega_0(M_N)=+1,
omega_1(M_N)=-1.
```

The outgoing record algebra is therefore the direct-limit home of the
finite registration-counting ray.

## 3. Scope of the result

This closes the outgoing-record-algebra sub-obligation of Fork 8 more
strongly than merely inserting an environment algebra. The lift follows
from:

1. the finite canonical public-collapse covector ray;
2. one-record normalization; and
3. the inherited symmetric-monoidal composition premise for disjoint
   independent record cells.

It does not prove the connected-cell linked-cluster thermodynamic limit,
derive the primitive write Hamiltonian, or select the covariant cell
spectral measure.

## 4. Regulator consequence

The three discrete regulators in the architecture audit independently gave
late-time root-return probability exponents

```text
2.96649, 2.99634, 3.05060,
```

all consistent with the analytic `t^-3` class. This is positive evidence
that the half-line, radial-tree, and cubic-lattice regulator fork is benign
at the decay-class level. It supports treating them as
scheme-equivalence checks.

It does not select the physical covariant spectral measure: the sealed
covariant representative gave `t^-6`, and covariance still permits more
than one tip-dependent cell measure. The shared regulator exponent narrows
the problem to the physical spectral measure; it does not solve that
problem.

## Status

```text
finite_covector_ray_used = true
nonzero_Hilbert_covector_limit = false
quasilocal_state_limit_derived = true
outgoing_record_algebra_subobligation_closed = true
connected_linked_cluster_limit_derived = false
unique_covariant_spectral_measure_derived = false
fork_8_closed = false
hypothesis_promoted_to_principle = false
alpha_computed = false
```
