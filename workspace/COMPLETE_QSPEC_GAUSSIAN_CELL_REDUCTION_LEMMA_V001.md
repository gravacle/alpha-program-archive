# Complete-Qspec Gaussian Cell Reduction Lemma v001

Date: 2026-07-25

## Lemma 1: exterior exponential identity

Let `b` be a finite-dimensional one-body operator and let `Gamma_n` be the
exterior-power representation on `Lambda^n H`. Define

```text
G(t)=Gamma_n(exp(t b)).
```

Differentiating the wedge action gives

```text
dG/dt=dGamma(b) G(t),   G(0)=I.
```

The finite-dimensional linear initial-value problem has a unique solution,
so

```text
Gamma_n(exp(t b))=exp(t dGamma(b)).
```

No spectral choice is used in this identity.

## Lemma 2: conditional-record decomposition

Let the Hermitian record generator have spectral resolution

```text
R=sum_mu mu Q_mu,
sum_mu Q_mu=I_R,
Q_mu Q_nu=delta_(mu,nu) Q_mu.
```

For a source interaction `H_a=dGamma(b_a)`,

```text
exp[-i tau H_a tensor R]
 =sum_mu exp[-i tau mu dGamma(b_a)] tensor Q_mu
 =sum_mu Gamma_n(exp[-i tau mu b_a]) tensor Q_mu.
```

A source-only free factor has the form `F tensor I_R`, so it preserves
every record spectral block. Therefore an arbitrary chronological product
of the frozen free and interaction factors has the exact form

```text
U_a=sum_mu U_(a,mu) tensor Q_mu,
```

where `U_(a,mu)` is the source product obtained by replacing `R` with its
eigenvalue `mu` while preserving the original chronological order.

For normalized ready state `|0_R>` and record outcome `|q>`, the Kraus
operator is consequently

```text
K_(a,q)
 =(I tensor <q|) U_a (I tensor |0_R>)
 =sum_mu <q|Q_mu|0_R> U_(a,mu).
```

## Lemma 3: exact support compression

Let `Q_S:H_S->H_full` be an isometry and `P=Q_S Q_S^dagger`. If `P`
reduces every source generator in every chronological factor, analytic
functional calculus and multiplication preserve the same reduction.
Hence:

```text
U_(a,mu) Q_S=Q_S U_(a,mu,S);
K_(a,q) Q_S=Q_S K_(a,q,S);
K_(a,q,S)=Q_S^dagger K_(a,q) Q_S.
```

The same identity holds for chronological composites:

```text
K_(q1,q2)=K_(2,q2)K_(1,q1).
```

Thus the directly constructed support cell and the compression of the
full unretracted cell are the same exact physical object.

## Corollary: no polar factor

Each source factor in every record block is unitary for real physical
times and Hermitian generators. The full joint cell is therefore unitary.
With a normalized ready state and a complete record basis,

```text
sum_q K_q^dagger K_q=I.
```

The physical Gram factor is exactly `I`; a generic numerical polar
retraction would change the object rather than derive it and is neither
needed nor admissible in the canonical transfer.

## Scope

This lemma concerns the frozen finite cell and its exact spin-2 support.
It supplies no zero-free estimate, continuum limit, response coefficient,
coupling, or alpha value.

