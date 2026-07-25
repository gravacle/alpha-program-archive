# Complete-Qspec Open-Record Block Transfer Induction Proof v001

Date: 2026-07-25

## Statement

Let a finite causal schedule consist of record-opening events, branchwise
unitary evolution events, and record-closing events. At each boundary let
`A_e` contain exactly the records whose ready factors have been introduced
and whose last incident unitary has not yet passed.

Let `Omega_e` be the full global relative-history cross-operator, including
every record opened through event `e`. Define:

```text
X_e = Tr_(closed records) Omega_e.
```

Then `X_e` is generated exactly by the OPEN, EVOLVE, and valid CLOSE rules
in the block-transfer specification.

## Proof by event induction

### Base boundary

Before any record opens:

```text
Omega_0 = rho_source,in,
X_0 = rho_source,in.
```

The active record set is empty.

### Open event

Suppose fresh records `B` enter in product ready state `sigma_B`. The full
operator becomes:

```text
Omega_(e+1) = Omega_e tensor sigma_B.
```

The ready factors are disjoint from all closed factors, so:

```text
X_(e+1)
 = Tr_closed(Omega_e tensor sigma_B)
 = X_e tensor sigma_B.
```

This is OPEN(B).

### Evolution event

Let `U_e^plus/minus` act on the source and a subset of active records, and
as identity on every closed record. Then:

```text
Omega_(e+1)
 = (U_e^plus tensor I_closed)
   Omega_e
   (U_e^- dagger tensor I_closed).
```

Partial trace over the closed factors commutes with both multiplications:

```text
X_(e+1) = U_e^plus X_e U_e^- dagger.
```

This is EVOLVE.

### Valid close event

Let `C` be a subset of active records whose last incident evolution has
passed. By definition, every future unitary acts as identity on `C`.
Therefore the factors may be traced now without changing any later
relative-history scalar:

```text
X_(e+1) = Tr_C X_e.
```

Partial traces over disjoint factors commute, so closing several eligible
records together or in any order gives the same block operator. This is
CLOSE(C).

### Induction conclusion

Every valid event is one of the preceding three cases. Hence, by induction,
the block-transfer operator equals the corresponding partial trace of the
full global relative-history operator at every event boundary. After all
records close, the complete source trace equals the full global CTP scalar.

## Sequential reduction

If each record opens, evolves, and closes before the next record opens,
the active set has width at most one. OPEN-EVOLVE-CLOSE becomes:

```text
T_c(X)
 = Tr_R,c [
     U_c^plus (X tensor sigma_c) U_c^- dagger
   ],
```

which is the sealed sequential transfer theorem.

## Early-close exclusion

If a record is traced before its last incident unitary, that later unitary
does not act on the reduced block space. No source-only operation can in
general reproduce an arbitrary later joint unitary on the discarded
factor. The liveness condition is therefore necessary, not merely
convenient. Such a schedule is rejected rather than approximated.

## Scope

The proof is exact for every finite valid event schedule. Computational
cost may grow exponentially with the maximum simultaneous open-record
width. No bound on that width or thermodynamic convergence is asserted.
