# R3.4 Outgoing-Tail Generator Exhaustion Specification v001

## Purpose

Determine whether the inherited Gravacle rules force an incidence-only
outgoing public-record tail or leave a physical zero-form

```text
G_out = D_H + Phi
```

that can change durability or the root spectral measure.

The conditional scalar density computed in R3.4 v002 is already known.
Accordingly this is target-independent but not architecture-blind. No
candidate may be selected because it reproduces that density or any desired
decay exponent.

No measured coupling, mass, endpoint, cosmological value, or alpha may enter.

## Hash-pinned authorities

The evaluator must verify every authority and exact status fact in
`R3_4_OUTGOING_TAIL_GENERATOR_EXHAUSTION_PROVENANCE_V001.json`. Any absent,
duplicated, changed, or unhashed authority fact is a hard failure.

## Public-tail carrier

The already derived quasi-local outgoing record algebra is built from one
two-endpoint register per completed record cell. On one register use

```text
A_1=M_2(C),
A_public=span{I,Z},
```

where `Z` separates the two durable public labels.

The most general local Hermitian zero-form on this reduced register is

```text
Phi=a I+b_x X+b_y Y+b_z Z.
```

This is an exhaustion only of the reduced public-record factor. The audit
must separately report whether source, spin, edge, or enlarged record factors
have been proved absent from the asymptotic tail.

## Required tests

1. **Nondemolition:** require `[Phi,Z]=0`. Any term that rotates the public
   pointer is incompatible with an invariant durable pointer algebra.
2. **Projective quotient:** a common `a I` phase is physically null.
3. **Public-algebra action:** classify the adjoint action of the surviving
   `b_z Z` term on `A_public` and on the complete `M_2(C)`.
4. **Tail locality:** source-supported compact write-region terms vanish on
   the asymptotic tail; persistent position dependence violates homogeneous
   intrinsic-cell assembly unless independently generated.
5. **Primitive provenance:** an independent persistent tail detuning is
   inadmissible under the sealed transport-only primitive rule. Generated
   terms remain possible and must be tracked rather than silently forbidden.
6. **Continuum provenance:** report separately whether `D_H`, its scaling
   limit, self-adjoint domain, positive-energy projector, root embedding, and
   absence of bound modes have been derived.

## Interpretation rule

If `Phi` acts trivially on `A_public`, that establishes public-tail
equivalence only. It does not prove equality of full Hilbert generators or
their spectral measures. In particular, `b_z Z` rotates off-diagonal
operators and cannot be erased before the public superselection quotient.

## Sealed outcomes

```text
no nontrivial Phi survives on A_public, but continuum/operator obligations
remain:
  PUBLIC_TAIL_ZERO_FORM_EXHAUSTED_CONTINUUM_SCALING_OPEN

a nontrivial admissible Phi survives on A_public:
  NONTRIVIAL_PUBLIC_TAIL_ZERO_FORM_SURVIVES

the public zero-form and every continuum/operator obligation close:
  UNIQUE_INCIDENCE_ONLY_OUTGOING_GENERATOR_DERIVED
```

No outcome promotes the direct-limit hypothesis unless spectral density,
absolute continuity, decay, thresholded durability, and outgoing
recoverability all follow from the same operator.

```text
alpha_used = false
alpha_computed = false
proof_authorized = false
```

