# Causal Direct-Limit Covector-Ray Lift

## Status

Forward specification for the outgoing-record part of Fork 8.

This test asks whether the finite canonical public-collapse covector ray
derived by BID has a direct-limit home. It contains no alpha or measured
physical constant.

## Inherited finite result

For one oriented record edge,

```text
epsilon_e(y_s,y_t)=U_e y_s+y_t,
[epsilon_e]=[U_e,id].
```

The ray is fixed by the finite-cell operational colimit, gauge covariance,
orientation coherence, path composition, and one-record normalization.

## Competing limit homes

### H: Hilbert-dual lift

On `H_N=l2({1,...,N})`, let

```text
c_N=sum_(j=1)^N e_j.
```

Test all three natural normalizations:

```text
c_N;
c_N/sqrt(N);
c_N/N.
```

A nonzero Hilbert-dual lift requires a bounded sequence converging to a
nonzero vector or bounded covector on `l2(N)`.

### A: quasi-local algebra lift

For independent outgoing record cells define

```text
A_N = tensor_(j=1)^N M_2,
iota_N(A)=A tensor I.
```

For each public label `h` fixed by the finite one-record ray, define

```text
omega_h^N(A)=<h^tensor_N|A|h^tensor_N>.
```

Test compatibility:

```text
omega_h^(N+1)(iota_N(A))=omega_h^N(A).
```

If compatible, the family defines one state `omega_h` on the quasi-local
inductive-limit algebra. The empirical record observable

```text
M_N=(1/N) sum_(j=1)^N Z_j
```

must become central against every observable with fixed finite support and
must distinguish the public labels.

## Blind adjudication

Return:

```text
HILBERT_COVECTOR_LIFT
QUASILOCAL_STATE_LIFT_ONLY
NO_DIRECT_LIMIT_LIFT
```

The quasi-local result is allowed to use BID's already-declared symmetric
monoidal composition for disjoint independent record cells. It must state
that this composition law is an inherited physical premise and that the
connected-cell linked-cluster limit remains separate.

## Non-promotion rule

Deriving the outgoing algebra does not select a unique microscopic causal
complex or cell spectral measure. It closes only the outgoing-record-algebra
sub-obligation of Fork 8.

```text
alpha_used = false
alpha_computed = false
```
