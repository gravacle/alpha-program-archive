# R3.4 Shared-Source Causal Parent Result v001

## Verdict

```text
SHARED_SOURCE_CAUSAL_PARENT_PUBLIC_MOLLER_DERIVED
```

The adopted Causal Incidence Support Principle closes the primitive
stationary-reuse defect. On the actual shared source carrier, causal order
and exact primitive pointer persistence are derived together. The result is
an outgoing local endomorphism on the public record algebra, not yet a
same-GNS unitary Moller operator or complete physical durability theorem.

## Shared source and causal order

For the three-cell chain, the source projectors are derived from

```text
d_j=e_(j+1)-e_j,
P_j=|d_j><d_j|/2.
```

The calculation gives

```text
Tr(P_0 P_1)=Tr(P_1 P_2)=1/4;
Tr(P_0 P_2)=0.
```

Consequently the adjacent full generators are genuinely connected:

```text
||[B_0,B_1]||_F=||[B_1,B_2]||_F=8.48528137423857,
||[B_0,B_2]||_F=0.
```

Reversing adjacent order changes the finite parent by
`16.97056274847714` in Frobenius norm. Reordering disjoint cells changes it
by zero. Causal order is therefore physical structure rather than harmless
notation.

## Exact primitive pointer persistence

Although adjacent source projectors overlap, a later primitive term acts on
its own new record factor. Hence for `k>j`,

```text
[B_k,O_j]=0
```

for every operator `O_j` on the earlier record factor. This statement holds
for arbitrary source-projector overlaps because the record tensor factors
are distinct.

The executable writes the first pointer with probability
`0.9999999999999996`. After both later shared-source interactions, its
probability remains the same to machine precision. Reduced-state restriction
errors are below `2.1e-16`.

This is an arbitrary-chain result. If

```text
W_N=U_(N-1)...U_0
```

and `A` is supported on the first `m` record factors, then every
`U_k`, `k>=m`, commutes with `A`. In

```text
W_N^* A W_N
```

those later factors cancel from the inside outward. The image is therefore
independent of `N` for every `N>=m`. The local limit defines a unital
star-endomorphism on the public quasi-local record algebra.

## Why this is not yet full PSC closure

The source is shared, so later cells legitimately change source-record
correlations. The reduced source-plus-first-record state changes by

```text
0.5303300858899105
```

between the first and third causal events. Thus the naive source-inclusive
embedding does not supply a projectively compatible finite-state family.
Local source observables do stabilize after their finite causal buffer, but
the inverse sequence has not been shown to converge. The present result is
therefore an outgoing endomorphism, not an automorphism or a unitary Moller
implementer in one GNS representation.

The parent derives the outgoing state given a disclosed in-sector. It does
not yet select the physical in-state.

## Mandatory negative control

The isolated stationary generator still gives

```text
U(tau_R)|r>=|p>,
U(2 tau_R)|r>=|r>.
```

The recurrence error is below `1e-15`. Causal one-use support, not first
orthogonality alone, is what prevents primitive rewriting.

## Scope

Closed here:

```text
shared-source causal order;
profile-independent isolated first-opening endpoint;
exact primitive pointer persistence;
public-record finite-state restriction;
and the outgoing public-record Moller endomorphism.
```

Still open:

```text
selection of the physical in-state;
a same-GNS or representation-covariant full Moller construction;
all generated descendants and complete physical durability;
the nontrivial outgoing tail generator;
the complete write-plus-tail spectrum and root measure;
and every coupling calculation.
```

```text
complete_parameter_free_Q_spec_frozen = false
parent_selected_physical_in_state_derived = false
generated_descendant_durability_closed = false
complete_physical_durability_derived = false
nontrivial_outgoing_tail_generator_derived = false
complete_write_plus_tail_spectrum_derived = false
physical_spectral_measure_derived = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
