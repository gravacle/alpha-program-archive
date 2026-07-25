# Stage-7 Q_spec Review Candidate v001

Date: 2026-07-24

## Candidate status

```text
FROZEN_REVIEW_CANDIDATE
COMPLETE_Q_SPEC_NOT_YET_ESTABLISHED
```

This candidate freezes the strongest target-value-free parent construction
currently supported by the corpus. It is submitted to three independent
reviews. It is not a coupling calculation.

## Declared branch

```text
ordinary 3+1 Lorentzian globally hyperbolic spin spacetime;
one massless-bare vectorlike charged Dirac pair;
one smooth compact relative-U(1) connection a;
finite primitive causal diamonds;
distinct even M3 record factors;
and a flat source-free asymptotic region for the first construction.
```

The spacetime branch, source inventory, and smooth compact connection are
disclosed inputs. Additional vectorlike pairs and enlarged branches are not
excluded.

## Fields and carriers

On a Cauchy surface `Sigma`:

```text
K_Sigma=L2(Sigma,S tensor L^q);
R(K)=tensor_(c in K) R_c;
R_c=span{|r_c>,|p_c>,|e_c>}.
```

There is one global `CAR(K_Sigma)` source algebra. Record factors are even,
distinguishable, and are not fermionized.

The primitive relative-phase character has unit winding. The smooth
principal relative-`U(1)` bundle and connection are adopted microscopic
field content. They are not inferred from a passive ray phase.

## Primitive cell and measure

For each primitive cell:

```text
Gamma_c=diag(+1,+1,-1);
b_c=
  [[0,0,-1],
   [0,0,+1],
   [-1,+1,0]];
c_c=i Gamma_c b_c.
```

The intrinsic probability measure on a flat primitive causal diamond is
uniquely normalized four-volume in the classified measure class. Its time
marginal is:

```text
w(s)=32 min(s,1-s)^3,  0<=s<=1;
integral_0^1 w(s) ds=1.
```

The dimensionless first-opening interval is:

```text
tau_R=pi/sqrt(2).
```

The physical tip-to-tip duration `T_R>0` is not numerically fixed. The
candidate retains its scale orbit.

## First-order parent

For cell `c` with causal section multiplier `M_c(t)`:

```text
v_c(t)
 =(tau_R/T_R) w((t-t_c)/T_R)
```

inside the causal cell and zero outside. With

```text
S_n=-i slash(n) gamma^5,
```

the one-particle parent is:

```text
h_K(t)
 =h_0[g,a]
  +sum_(c in K) v_c(t) M_c(t)
     tensor S_n tensor iota_c(c_c).
```

The many-source primitive parent is the adopted number-preserving
operator-valued quasifree lift:

```text
H_K(t)=dGamma_R(h_K(t)).
```

No source carrier is copied per record. Shared source support is retained.

## Generated descendants

The covariant first-order kernel is:

```text
D_K=i gamma^mu nabla_mu+i gamma^5 C_K(x),
C_K(x)=sum_c v_c(x) M_c(x) iota_c(c_c).
```

Direct squaring gives:

```text
D_K^2
 =(i gamma^mu nabla_mu)^2
  -C_K^2
  -gamma^mu gamma^5 nabla_mu C_K.
```

Single-cell, overlap, spin-curvature, `U(1)`-curvature, and closure-face terms
are descendants of this operator. No independent descendant coefficient is
introduced.

The absence of an independent bare parity-even `F^2` stiffness is an adopted
compositeness condition. The separate question whether an arbitrary finite
`c F^2` deformation survives renormalized matching remains open.

## State, contour, and domain

For every finite cell set, the interaction is a bounded,
compact-time-supported self-adjoint perturbation of `h_0` on one common
domain. It gives a unique finite propagator and finite Moller maps.

The incoming source state is the stationary quasifree state of `h_0`; finite
energy excitations are boundary data. Record factors enter in their ready
state.

The positive/negative spectral projectors of the same free Hamiltonian fix
the free Schwinger-Keldysh greater, lesser, time-ordered, anti-time-ordered,
retarded, and advanced propagators. A normalized interacting CTP generating
amplitude and its full gauge/ghost/edge functional measure are not yet
constructed.

## Tail and durability

In the flat source-free asymptotic branch:

```text
h_0(p)=alpha_D dot p.
```

Its source spectrum is purely absolutely continuous for the declared
finite-energy `L2` class and has no source point spectrum. Every admitted
source root has thresholded nonreturn.

Causal Incidence Support prohibits reuse of a completed primitive incidence.
Later cells may act on the shared source and new record factors, but as the
identity on completed record factors.

The compatible completed-record states define:

```text
R_infinity=inductive_limit tensor_(j=1)^N M_3(C);
(pi_out,H_out,Omega_out)=GNS(R_infinity,omega_out).
```

Completed-record dynamics is the strongly continuous identity
automorphism. The incoming representation is the coherent source-dressed
net:

```text
Phi_N(A)=W_N^*(I_source tensor A)W_N;
j_NM=Phi_M o iota_NM o Phi_N^(-1).
```

Central pointer averages separate the public output labels.

## Derived scope

The candidate derives, in its declared branch:

```text
the finite causal durability parent;
its generated descendants;
the free in-state and contour;
the free source tail and thresholded source nonreturn;
the outgoing record inductive state and GNS;
the coherent dressed record net;
and the Causal Direct-Limit Record Principle.
```

## Open `Q_spec` slots

The following are frozen as open, not delegated silently:

```text
absolute physical T_R;
full gravity action and gravitational quantum measure;
dynamical U(1) functional action beyond the auxiliary connection;
interacting CTP generating amplitude;
gauge fixing, ghosts, and gauge edge modes;
functional regulator and finite renormalization;
exclusion of the finite c F^2 deformation;
interacting charged pole or infraparticle threshold;
complete charged-species and threshold map;
enlarged-branch exhaustion;
Thomson matching;
and one unused structure-sensitive prediction.
```

## Review questions

### Mathematical/operator review

1. Does the single first-order parent have the claimed common domain and
   generated descendant identity?
2. Does Causal Incidence Support imply exact record-state compatibility and
   the stated outgoing GNS/dressed-net construction?
3. Is Fork-8 promotion valid at its stated scope without a global
   source-inclusive Moller limit?

### Physical/QED review

1. Is the candidate a physically coherent durability parent?
2. Which open gauge, edge, spectrum, renormalization, and matching slots are
   mandatory before it can become a complete electromagnetic `Q_spec`?
3. Does any existing term already smuggle in an electromagnetic
   normalization?

### Provenance/anti-circularity review

1. Are all adopted premises and disclosed branch inputs visible?
2. Is any result promoted beyond its least-favorable authority?
3. Is any architecture, state, measure, operator, or normalization selected
   because of alpha or an equivalent endpoint?

## Frozen authorization state

```text
stage7_candidate_frozen = true
independent_reviews_completed = false
complete_parameter_free_Q_spec_frozen = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
