# Complete-Qspec Exterior-Frame and Stinespring Lemmas v001

Date: 2026-07-25

## Lemma 1: exterior-power frame covariance

Let `V,V_f:C^d->H_parent` be isometries with the same range projector:

```text
V^dagger V=V_f^dagger V_f=I_d,
V V^dagger=V_f V_f^dagger=P.
```

Define `U=V^dagger V_f`. Then

```text
U^dagger U
 =V_f^dagger P V_f
 =I_d,

V U
 =P V_f
 =V_f.
```

Thus every orthonormal frame of the same exact active subspace is related
to the reference frame by a unitary; this conclusion does not depend on a
particular degenerate eigensolver output.

Let `H=C^d`, let `U` be any unitary on `H`, and let `Gamma_n(U)` be its
action on `Lambda^n H`:

```text
Gamma_n(U)(v_1 wedge ... wedge v_n)
 =Uv_1 wedge ... wedge Uv_n.
```

In the ordered occupation basis its matrix elements are

```text
[Gamma_n(U)]_(I,J)=det U_(I,J).
```

Cauchy-Binet and `U^dagger U=I` give

```text
sum_I det(U_(I,J))^* det(U_(I,K))
 =det[(U^dagger U)_(J,K)]
 =delta_(J,K).
```

Therefore `Gamma_n(U)` is unitary for every `U`.

For every one-body operator `b`,

```text
dGamma(b)
 =d/dt Gamma_n(exp(t b)) |_(t=0).
```

Functoriality of the exterior power gives

```text
Gamma_n(U)^dagger Gamma_n(exp(t b)) Gamma_n(U)
 =Gamma_n(exp(t U^dagger b U)).
```

Differentiating at zero proves the universal identity

```text
dGamma(U^dagger b U)
 =Gamma_n(U)^dagger dGamma(b) Gamma_n(U).
```

If `U=U_- direct-sum U_+` respects the negative/positive spectral split,
the filled negative sea obeys

```text
Gamma_n(U)|sea_->=det(U_-)|sea_->.
```

Thus its ray, every CTP scalar, and the dimension of every generated
invariant sector are independent of the chosen orthonormal active frame.

## Lemma 2: exact Stinespring completeness

Let `H_S` be the source space, `H_R` the record space, and `|0_R>` a
normalized ready state. Define the isometric ready embedding

```text
J:H_S->H_S tensor H_R,
J|psi>=|psi> tensor |0_R>,
J^dagger J=I_S.
```

Let `U` be any unitary on `H_S tensor H_R`, and let `{|q>}` be any complete
orthonormal record basis. Define

```text
K_q=(I_S tensor <q|) U J.
```

Then

```text
sum_q K_q^dagger K_q
 =J^dagger U^dagger
   [I_S tensor sum_q |q><q|]
   U J
 =J^dagger U^dagger U J
 =J^dagger J
 =I_S.
```

If a source projector `P` reduces every source generator appearing in the
time-ordered joint Hamiltonian, then `P tensor I_R` reduces every unitary
factor and their product. Consequently:

```text
(I-P)K_q P=0
```

for every outcome `q`.

For any cross-history operator `X=XP`,

```text
X K_q^dagger
 =X P K_q^dagger P
 =[X K_q^dagger]P.
```

Arbitrary left multiplication does not alter the right-support identity.
Summing outcomes and inducting over fresh, chronologically closed records
therefore preserves `X_N=X_NP` at every finite stage. Applying the full
source trace proves equality of the full CTP amplitude and its
`left-full x right-P` representation.

## Scope

These are exact finite-dimensional algebraic lemmas. They introduce no
response coefficient, continuum assumption, coupling, or alpha target.
