# Complete-Qspec Boundary-Adapted Nonautonomous Factorization Lemma v001

Date: 2026-07-25

## Purpose

Supply the operator-theoretic step needed to pass from a homogeneous
zero-free disk to independently addressable local sources. The result is a
finite-sequence theorem. It uses the physical incoming and trace boundaries
and does not infer a multivariable statement from homogeneous powers.

## Setting

Let a finite-dimensional Hilbert space split orthogonally as

```text
H=P H direct-sum Q H,
rank(P)=1.
```

Choose a unit vector `p` spanning `P H`. Let

```text
A=P+R,
R=Q R Q,
||R||<=r<1.
```

For `j=1,...,N`, let

```text
M_j=A+E_j,
||E_j||<=eta.
```

Write the blocks relative to `p direct-sum QH`:

```text
M_j=[a_j b_j; c_j D_j].
```

Then

```text
|a_j-1|<=eta,
||b_j||<=eta,
||c_j||<=eta,
||D_j||<=r+eta.
```

Freeze `0<X<1` and define

```text
d=1-eta(1+X),
n=eta+(r+eta)X,

L=(r+eta)/d + eta*n/d^2.
```

Assume

```text
d>0,
n/d<X,
L<1.
```

The strict inequalities are part of the theorem's hypotheses.

## Right boundary recursion

Set `u_0=0` in `QH`. For `j=1,...,N`, define

```text
s_j=a_j+b_j u_(j-1),

u_j=(c_j+D_j u_(j-1))/s_j.
```

If `||u_(j-1)||<=X`, then

```text
|s_j|>=d>0,
||c_j+D_j u_(j-1)||<=n,
||u_j||<=n/d<X.
```

Induction therefore defines every `u_j` and keeps it in the open
`X`-ball. With

```text
r_j=p+u_j,
```

the recursion is exactly

```text
M_j r_(j-1)=s_j r_j.
```

## Left boundary recursion

Set `v_N=0` in the dual of `QH`. For `j=N,...,1`, define

```text
t_j=a_j+v_j c_j,

v_(j-1)=(b_j+v_j D_j)/t_j.
```

The same estimates give

```text
|t_j|>=d>0,
||v_(j-1)||<X.
```

With

```text
ell_j=p^dagger+v_j,
```

the recursion is exactly

```text
ell_j M_j=t_j ell_(j-1).
```

Both recursions are holomorphic in every matrix entry on the declared
operator ball because their scalar denominators remain uniformly separated
from zero.

## Graph contraction

For completeness, the right graph map

```text
G_j(u)=(c_j+D_j u)/(a_j+b_j u)
```

maps the closed `X`-ball into its interior. For `||u||,||w||<=X`,
direct subtraction gives

```text
||G_j(u)-G_j(w)||
 <=[(r+eta)/d + eta*n/d^2] ||u-w||
 =L ||u-w||.
```

The complex-linear dual left map, with no conjugation of the holomorphic
parameters, has the same bound. Thus the effect of changing a boundary
condition or a remote matrix decays at least geometrically as `L` is
iterated. This decay statement is an input to a later cumulant majorant; it
is not itself that majorant.

## Intertwining projectors

Define

```text
h_j=ell_j r_j=1+v_j u_j.
```

Since `||u_j||,||v_j||<X`,

```text
|h_j|>=1-X^2>0.
```

Set

```text
Pi_j=r_j ell_j/h_j.
```

Each `Pi_j` is rank one and idempotent. Moreover,

```text
s_j h_j
 =ell_j M_j r_(j-1)
 =t_j h_(j-1),
```

so

```text
M_j Pi_(j-1)=Pi_j M_j.
```

The projectors are boundary adapted:

```text
u_0=0,
v_N=0,

Pi_0=p(p^dagger+v_0),
Pi_N=(p+u_N)p^dagger.
```

## Exact amplitude factorization

Let the output row and input column obey

```text
l=sqrt(m) p^dagger,
||x||=1,
l x=1
```

for some positive integer `m`. Because `v_N=0`,

```text
l Pi_N=l.
```

Repeated intertwining therefore gives

```text
l M_N...M_1(I-Pi_0)x=0.
```

Using the right recursion,

```text
l M_N...M_1 x
 =sqrt(m)
  [product_(j=1)^N s_j]
  (p^dagger+v_0)x.
```

Since `v_0 p=0` and `sqrt(m) p^dagger x=l x=1`,

```text
|sqrt(m)(p^dagger+v_0)x|
 >=1-sqrt(m) X ||Qx||
 >=1-sqrt(m)X.
```

If

```text
sqrt(m)X<1,
```

then every factor on the right is nonzero and

```text
|l M_N...M_1 x|
 >=[1-sqrt(m)X] d^N
 >0
```

for every finite `N` and every admissible sequence.

## Holomorphic consequence

If each `M_j` depends holomorphically on an independent variable `z_j` and
the operator-ball bound holds on a closed polydisc, the displayed
factorization is holomorphic there and has no zero. On the open polydisc,
choose the logarithm value at the origin. In the normalized case
`Z(0)=1`, the choice `Log Z(0)=0` fixes a unique holomorphic logarithm.

This conclusion proves finite-volume multivariable zero-freedom and the
existence of its connected generating function. It does not prove
thermodynamic convergence, physical continuum addressability, or absolute
summability of connected cumulants.
