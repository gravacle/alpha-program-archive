# Complete-Qspec Sequential Transfer Induction Proof v001

Date: 2026-07-25

## Statement

Let `H_S` be the shared source Hilbert space. Let `H_R,c` be a fresh record
factor in ready density `sigma_c=|r_c><r_c|`. For each branch sign, let
`U_c^+` and `U_c^-` act on `H_S tensor H_R,c` and as the identity on all
closed record factors.

Define the global relative-history cross-operator after stage `c` by:

```text
Omega_c
 = W_c^+
   (rho_S tensor sigma_1 tensor ... tensor sigma_c)
   W_c^- dagger,
```

where the strictly sequential history satisfies:

```text
W_c^plus
 = (U_c^plus tensor I_R,<c)
   (W_(c-1)^plus tensor I_R,c),

W_c^minus
 = (U_c^minus tensor I_R,<c)
   (W_(c-1)^minus tensor I_R,c).
```

Tensor-factor permutations are the canonical ones that place `U_c` on
`H_S tensor H_R,c`; they do not change the argument.

For a source cross-operator `X`, define:

```text
T_c(X)
 = Tr_R,c [
     U_c^plus (X tensor sigma_c) U_c^- dagger
   ].
```

Then, at every completed-stage boundary:

```text
Tr_R,1...c Omega_c
 = T_c o ... o T_1 (rho_S).
```

Consequently:

```text
Tr_(S,R,1...N) Omega_N
 = Tr_S [T_N o ... o T_1 (rho_S)].
```

## Proof

### Base case

For `c=0`, there are no record factors and `W_0^plus=W_0^minus=I_S`.
Therefore:

```text
Omega_0 = rho_S,
Tr_empty Omega_0 = rho_S = X_0.
```

### Induction hypothesis

Assume at the completed boundary after stage `c-1` that:

```text
Tr_R,1...(c-1) Omega_(c-1)
 = X_(c-1)
 = T_(c-1) o ... o T_1 (rho_S).
```

Every earlier record is closed, and `U_c^plus/minus` acts as the identity on
those factors.

### Induction step

By sequential factorization:

```text
Omega_c
 = (U_c^plus tensor I_R,<c)
   (Omega_(c-1) tensor sigma_c)
   (U_c^- dagger tensor I_R,<c).
```

Because both branch operators act trivially on the closed factors, the
partial trace over those factors commutes with the left and right
multiplications:

```text
Tr_R,<c Omega_c
 = U_c^plus
   ([Tr_R,<c Omega_(c-1)] tensor sigma_c)
   U_c^- dagger.
```

Apply the induction hypothesis and then trace the fresh record:

```text
Tr_R,1...c Omega_c
 = Tr_R,c [
     U_c^plus (X_(c-1) tensor sigma_c) U_c^- dagger
   ]
 = T_c(X_(c-1))
 = T_c o ... o T_1 (rho_S).
```

This proves the induction step and hence the statement for all finite `N`.
Taking the remaining complete source trace gives the connected
relative-history scalar.

## Kraus form

For any orthonormal basis `|q>` of `H_R,c`, set:

```text
K_(c,q)^plus  = <q|U_c^plus|r_c>,
K_(c,q)^minus = <q|U_c^minus|r_c>.
```

Expanding the fresh-record partial trace yields:

```text
T_c(X)
 = sum_q K_(c,q)^plus X K_(c,q)^minus dagger.
```

No positivity assumption is required for this cross-history map. On the
diagonal branch it reduces to the ordinary completely positive,
trace-preserving reduced channel.

## Concurrent-cell exclusion

The proof uses the factorization:

```text
U_c on H_S tensor H_R,c,
identity on every closed H_R,j with j<c.
```

It does not apply while multiple record incidences remain open or when a
later interaction acts on an earlier open factor. In that case the induction
state must retain all open factors, and the admissible object is a block
transfer map on:

```text
H_S tensor H_open_records.
```

No one-record Markov claim is made for that case.

## Proof status

This is an exact finite-dimensional tensor and partial-trace identity under
the declared strictly sequential completed-record factorization. The
physical regression tests its implementation; the regression is not the
proof.
