# Finite Record-Cell Flux Response Protocol v001

## Scope

This is a preregistered evaluation protocol, not a specification of the
microscopic record cell. It may run only after one complete finite
spacetime-plus-internal `Q_cell` has been derived, sealed, and passed through
the provenance gate.

The protocol contains no measured alpha and may not be altered after a result
is known.

## Preconditions

Before evaluation, `Q_cell` must fix:

1. the finite spacetime and internal carrier;
2. the complete gauge-covariant operator or update;
3. all species, masses, doublers, and zero-mode prescriptions;
4. the state, CTP contour, boundary data, edge modes, and gauge quotient;
5. the measure and exact normalized partition functional;
6. the compact unit-character normalization;
7. the physical cell lengths and volume; and
8. the rule that forbids an independent finite `c_R F^2` mutation.

No item may be selected by comparison with alpha.

## Exact parity-even functional

For a fermionic determinant realization, define

```text
Gamma_even[A]
  = -(1/2) log det'(D[A]^dagger D[A])
    + declared bosonic, ghost, edge, and record contributions.
```

For a different microscopic realization, `Gamma_even` is the exact
parity-even logarithm of its normalized partition functional. The prime may
remove only derived gauge/stabilizer zero modes; every removed mode must be
listed.

## Magnetic flux curvature

When the sealed cell has a closed `(1,2)` two-cycle, evaluate the integer
compact-flux sectors

```text
F_12(n) = 2 pi n/(L_1 L_2),  n in {-1,0,+1}.
```

Then

```text
K_B(L)
  = [L_1^2 L_2^2/(V_4 (2 pi)^2)]
    [Gamma_even(+1) + Gamma_even(-1) - 2 Gamma_even(0)].
```

This normalization follows from
`Gamma_M=(K/4) integral F_mu_nu F_mu_nu`.

## Electric flux curvature

Apply the same sealed prescription to the Euclidean `(0,1)` plane:

```text
F_01(n) = 2 pi n/(L_0 L_1),

K_E(L)
  = [L_0^2 L_1^2/(V_4 (2 pi)^2)]
    [Gamma_even(+1) + Gamma_even(-1) - 2 Gamma_even(0)].
```

The Lorentzian continuation and CTP retarded Hessian must be derived from the
same microscopic functional. A Euclidean equality alone is insufficient.

## Required gates

The response passes only if:

```text
K_E > 0,
K_B > 0,
c_cell^2 = K_B/K_E
```

recovers the sealed causal normalization, and

```text
K_Lor = sqrt(K_E K_B)
```

agrees with the independently computed zero-frequency retarded transverse
response, including contact and edge terms.

The calculation must be repeated under every mutation that preserves the
declared microscopic principles. If two admissible mutations give different
`K_Lor`, the specification is incomplete and alpha is not computed.

## Downstream map

Only after the finite-cell response, stitching rule, massive charged sector,
and Thomson matching all pass may one set

```text
alpha_Thomson = 1/(4 pi K_Thomson).
```

The numerical value remains hidden from construction and branch selection.

## Authorization state

```text
protocol_frozen_before_cell_evaluation = true
complete_Q_cell_derived = false
flux_curvature_evaluation_authorized = false
K_E_computed = false
K_B_computed = false
retarded_response_agreement_derived = false
mutation_exclusion_passed = false
Thomson_matching_derived = false
alpha_computed = false
proof_authorized = false
```
