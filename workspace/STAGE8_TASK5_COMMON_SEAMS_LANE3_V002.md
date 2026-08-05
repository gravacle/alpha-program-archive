# STAGE 8 TASK 5 — COMMON SEAMS V002: R9 AND EPSILON-ZERO CARRIAGE

Lane: CODEX LANE 3 (SOL, HIGH EFFORT)  
Version: V002  
Date: 2026-08-05  
Custody: builder repair; Dario reviews  
Scope: bounded symbolic delta to Common Seams V001

## 0. Preflight and bounded determination

[PROVABLE — register] Before this delta began, the supervision register ended at Q-512 before its
usage instructions. A final read found Q-513 appended concurrently by the Xi-V003 drafting relay.
Q-513 records a draft pending re-review; it changes neither the sealed A7/A8 authorities used here
nor the Q-512 start condition. This lane did not consume Q-513 as law or edit the register.

[PROVABLE — no clobber] Before this delta began, the requested artifact and seal were absent from
both the Lane-3 cleanroom and `alpha-program-archive/workspace/`.

[PROVABLE — inputs] The controlling review, the V001 build, the modulus audit, and A7/A8 were checked
against their sealed sidecars before use:

```text
STAGE8_TASK5_SEAMS_REVIEW_DARIO_V001.md
 SHA-256 = 7a0cb7ad4b8a2f663ef4428169efb0764e60c4999b5f0c105d4d752b0c24ff05
 sidecar = OK
 mirror  = byte-identical

STAGE8_TASK5_COMMON_SEAMS_LANE3_V001.md
 SHA-256 = 5de94e16db09b982f85fdf117281af62df6ab0d05c9e7577ac258d47594b69b7
 sidecar = OK

STAGE8_TASK5_CHAIN_CONFORMANCE_AUDIT_LANE3_V002.md
 SHA-256 = 44202c060821728fba2c46b81b82487002e639f3242565b7a5fed387e41fcae8
 sidecar = OK

DOR_020_A7_EC_BRANCH_CARRIED_2026-08-05.md
 SHA-256 = 834e46029a292122c1e4c604af4f3e3249e6a9ee2638255464685623fba5eb8f
 sidecar = OK

DOR_020_A8_GAMMA_BOTH_ROUTES_2026-08-05.md
 SHA-256 = 0ee6c897055f803b31bc570b9f4ef852ccb3c4aba21fcd5274a7d740c8eb601d
 sidecar = OK.                                           (P0)
```

[YOURS — bounded determination]

```text
old R9
 =RETIRED: its independent Triv_[a] x Scal^Hol quantifier
  compares a varying H representative with a frozen HOL return and
  therefore annihilates the common period;

R9-V002
 =REPAIRED: compare the two equivariant route-return sections as one
  associated-orbit object on each A8-common formed instance;

epsilon=0 carriage
 =TYPED: carry the route-indexed full-cell family (T on H, S on HOL)
  and require every retained index to be formed and certified; no single q
  and no uniform contraction verdict;

epsilon=1 carriage
 =family-invariant zero only under the displayed formed-route premises,
  with A7_HOL_BRANCH_COMPAT additionally required on HOL.             (P1)
```

This artifact replaces only V001 `(R9)` and adds the family-dependent A7 carriage typing. It does
not rewrite the sound S1 construction, inhabit either route, repair V001's S2 bookkeeping residue,
or execute A8, A7, a contraction theorem, a fixed point, or an end test.

The gates remain

```text
alpha_computed = false;
proof_authorized = false;
kappa_record_computed = false;
member_bound = false;
fixed_point_executed = false;
end_test_executed = false;
numeric_evaluation = false;
measured_constant_comparison = none.                         (P2)
```

## 1. Frozen types

### 1.1 Orientation orbit and return types

For an admitted oriented address `a=(w,N,gamma)`, V001 retains

```text
[a]:={a,a^-},

R_or,[a]
 :=(R x [a])/((q,a^-)~(-q,a)),

iota_a:R->R_or,[a],

Triv_[a]
 :=Iso_R(R_or,[a],K_amb).                              (T1)
```

For `T,T' in Triv_[a]`, define the unique transition

```text
g_(T',T)
 :=T' compose T^(-1)
 in Aut_R(K_amb),

T'=g_(T',T) compose T.                                (T2)
```

The H return already has the exact V001 type

```text
B_(a,epsilon,K,T)^H(Y)
 in K_amb.                                             (T3)
```

A formed HOL scalarization member has a raw arc/log package and a final linear map

```text
S=(U_b^S,log_b^S,U_a^S,...)
 in Scal_[a;A1,A0,N]^Hol,

U_a^S:R->K_amb,

B_(a,epsilon,K,S;A1,A0)^Hol(Y)
 in K_amb.                                             (T4)
```

Neither T3 nor T4 is inhabited here.

### 1.2 What “formed period return” means for A8

[YOURS — exact repair type] The structural HOL package required for an orbit-valued period return is
fixed at the route-package index `[a;A1,A0,N]`, independently of `epsilon`, `K`, `Y`, every route
output, every modulus, and every threshold:

```text
ScalOrb_[a;A1,A0,N]^Hol
 :=the families Sbold=(S_T)_(T in Triv_[a]) such that

   S_T=(U_b,log_b,U_T,Cert_T)
    in Scal_[a;A1,A0,N]^Hol
    for every T;

   U_b and log_b and their raw arc/image/log certificates
    are the same retained data for every T;

   U_T
    =T compose iota_a:R->K_amb;

   Cert_T separately certifies every required linearity, zero,
    normalization, address/reality, A7, and reader-free clause
    for S_T;

   for T,T' and g=g_(T',T),

   U_T'=g compose U_T,

   B_(a,epsilon,K,S_T';A1,A0)^Hol(Y)
    =U_T'(p_Hol)
    =g(U_T(p_Hol))
    =g(B_(a,epsilon,K,S_T;A1,A0)^Hol(Y)).          (T5)
```

Here the shared raw coordinate is

```text
p_Hol
 :=log_b(Theta_(A1,A0;N)(Ker_(a,K)(Y))).           (T6)
```

Membership of every `S_T` in the full `Scal^Hol` type is required directly; no undeclared action on
that certificate type is inferred. `ScalOrb^Hol` is a response-independent family specification, not
an inhabited family and not an output-dependent `Match`.

The already displayed H family has the same output covariance:

```text
B_(a,epsilon,K,T')^H(Y)
 =g_(T',T)(B_(a,epsilon,K,T)^H(Y)).                (T6a)
```

An A8 common physical cell is now only

```text
c=(a,epsilon,K,Y,A1,A0,N;
   one alleged H period-return construction;
   one alleged HOL period-return construction).                  (T7)
```

“Period-return construction” includes its return object in the associated carrier built below. Thus
the carrier is part of route-result typing, not a third filter on A8. If both upstream composites are
claimed formed on c but either lacks that return typing, the result is

```text
A8_COMMON_CARRIER_DEFECT(c),                        (T8)
```

not exclusion of c, not satisfaction of A8, and not a vacuous equality. If both typed period returns
are formed, A8 applies on c. The whole family of alleged cells and route packages is retained. No T,
HOL member, connection pair, route, or A7 branch is selected.

## 2. T1 — the non-degenerate R9 repair

### 2.1 [PROVABLE] The representative-free common carrier

The transition maps satisfy

```text
g_(T,T)=T T^(-1)=id_(K_amb),

g_(T,T')
 =T T'^(-1)
 =(T' T^(-1))^(-1)
 =g_(T',T)^(-1),

g_(T'',T') compose g_(T',T)
 =(T'' T'^(-1))(T' T^(-1))
 =T'' T^(-1)
 =g_(T'',T).                                      (R9a0)
```

Define the associated orbit carrier

```text
Kbar_[a]
 :=(Triv_[a] x K_amb)/equivalence,

(T,x) equivalent_to (T',x')
 iff x'=g_(T',T)(x).                                (R9a)
```

R9a0 displays reflexivity. If `x'=g_(T',T)x`, then

```text
x
 =g_(T,T')g_(T',T)x
 =g_(T,T')x',                                      (R9a1)
```

which displays symmetry. If additionally `x''=g_(T'',T')x'`, then

```text
x''
 =g_(T'',T')g_(T',T)x
 =g_(T'',T)x,                                      (R9a2)
```

which displays transitivity. Thus R9a is an equivalence relation.

The map

```text
psi_[a]:Kbar_[a]->R_or,[a],

psi_[a]([T,x]):=T^(-1)(x)                           (R9b)
```

is well defined, because for equivalent representatives

```text
T'^(-1)(x')
 =T'^(-1)(g_(T',T)(x))
 =T'^(-1)(T' T^(-1)(x))
 =T^(-1)(x).                                        (R9c)
```

Its inverse is `z |->[T,T(z)]`, because both inverse checks are

```text
psi_[a]([T,T(z)])
 =T^(-1)T(z)
 =z,

[T,T(psi_[a]([T,x]))]
 =[T,T(T^(-1)x)]
 =[T,x].                                           (R9c1)
```

For another representative T',

```text
[T',T'(z)]
 =[T',g_(T',T)T(z)]
 =[T,T(z)]                                         (R9c2)
```

by R9a. Therefore

```text
Kbar_[a] isomorphic_to R_or,[a].                    (R9d)
```

This quotient removes the choice of trivialization representative; it does not quotient away a sign
or magnitude. At a fixed representative T,

```text
[T,x]=[T,y]
 =>g_(T,T)=id_(K_amb)
 =>x=y.                                             (R9e)
```

### 2.2 [PART-PROVABLE] The two route sections

For one common physical cell c on which both typed period-return constructions are formed, use T only
as a display representative and put

```text
p_H(c)
 :=(Per_(a,epsilon,K)^H(Y))(c_a),

p_Hol(c)
 :=log_b(
     Theta_(A1,A0;N)(Ker_(a,K)(Y))),

B_(c,T)^H
 =T(iota_a(p_H(c))),

B_(c,T)^Hol
 =T(iota_a(p_Hol(c))).                              (R9f)
```

The equality for the HOL line is exactly the T5 orbit-family condition, not a claim that the current
HOL route has a member. From T2, T5, and T6a,

```text
B_(c,T')^H
 =T'(iota_a(p_H(c)))
 =g_(T',T)(T(iota_a(p_H(c))))
 =g_(T',T)(B_(c,T)^H),

B_(c,T')^Hol
 =T'(iota_a(p_Hol(c)))
 =g_(T',T)(T(iota_a(p_Hol(c))))
 =g_(T',T)(B_(c,T)^Hol).                           (R9g)
```

Hence the two orbit-return objects

```text
Bbar^H(c)
 :=[T,B_(c,T)^H] in Kbar_[a],

Bbar^Hol(c)
 :=[T,B_(c,T)^Hol] in Kbar_[a]                     (R9h)
```

are independent of the displayed representative T by R9a and R9g.

### 2.3 [YOURS — replacement contract] R9-V002

The identification falsifier is

```text
for every common physical cell c on which both typed period-return
constructions are formed,

Bbar^H(c)=Bbar^Hol(c);                              (R9-V002)

one such displayed c with

Bbar^H(c)!=Bbar^Hol(c)

voids the disagreeing construction(s) pending adjudication.      (R9i)
```

The only quantifier in R9-V002 ranges over instances on which A8's two route constructions are both
formed on one common physical cell. There is no independent quantifier over `Triv_[a]`, `Scal^Hol`,
or their Cartesian product. No identification is assumed as a premise: R9-V002 is a required
comparison and R9i is its falsifier.

Equivalently, at one display representative,

```text
B_(c,T)^H=B_(c,T)^Hol,

B_(c,T')^H
 =g_(T',T)B_(c,T)^H
 =g_(T',T)B_(c,T)^Hol
 =B_(c,T')^Hol.                                   (R9j)
```

Changing the representative transports both sides together. It never compares H at T' with HOL
frozen at T.

### 2.4 [PROVABLE] Permanent two-member regression

Let

```text
T^-
 :=(-id_(K_amb)) compose T,

mu_(T^-)(a)=-mu_T(a),

mu_T(a)!=0.                                        (R9k)
```

R9f gives all four values:

```text
B_(c,T)^H
 = mu_T(a) p_H(c) 1_Kamb,

B_(c,T)^Hol
 = mu_T(a) p_Hol(c) 1_Kamb,

B_(c,T^-)^H
 =-mu_T(a) p_H(c) 1_Kamb,

B_(c,T^-)^Hol
 =-mu_T(a) p_Hol(c) 1_Kamb.                       (R9l)
```

The repaired equality at the two representatives is therefore

```text
at T:
 mu_T(a)(p_H(c)-p_Hol(c))1_Kamb=0,

at T^-:
-mu_T(a)(p_H(c)-p_Hol(c))1_Kamb=0.                (R9m)
```

Because `mu_T(a)!=0` and `1_Kamb!=0`, both lines impose the same condition

```text
p_H(c)=p_Hol(c).                                   (R9n)
```

Their solution set is the full diagonal

```text
{(p_H,p_Hol) in R x R:p_H=p_Hol}
 ={(p,p):p in R},                                  (R9o)
```

not the singleton `{(0,0)}`. Thus R9-V002 does not force `p=0`. The old two-member computation froze
the HOL return while reversing only T_H; R9l reverses both common representatives, so no equation
`mu_T p 1_Kamb=-mu_T p 1_Kamb` occurs.

The positive-scale regression has the same form. For `s>0` and `T_s:=sT`,

```text
B_(c,T_s)^H=s B_(c,T)^H,
B_(c,T_s)^Hol=s B_(c,T)^Hol,

B_(c,T)^H=B_(c,T)^Hol
 =>B_(c,T_s)^H=B_(c,T_s)^Hol.                     (R9p)
```

No normalization `r_T=1` is introduced.

### 2.5 [PROVABLE] Fidelity to A8

| A8 text element | R9-V002 rendering |
|---|---|
| both routes are formed | both alleged period-return constructions, including their return carrier, are typed on c; otherwise T8 records a common-carrier defect |
| one commonly formed cell | the single instance `c` |
| their period returns agree | equality in `Kbar_[a]`, equivalent by R9e to equality in any common representative |
| displayed disagreement is first-order | R9i needs one exhibited unequal pair |
| void the disagreeing construction(s) pending adjudication | copied without upgrading the result to “both routes void” |
| no assumed identification | R9-V002 is retained as a falsifier; it is not consumed to build either route |

A8 does not name independent scalarization-family quantifiers, a Cartesian product, a normalization,
or an output-dependent matching relation. R9-V002 adds none. Today `ScalOrb_[a;A1,A0,N]^Hol` has no
exhibited member and both route period-return constructions remain unformed, so A8 is unexecutable
rather than passed, failed, or vacuously true.

## 3. T2 — family-dependent modulus and A7 carriage

### 3.1 [YOURS — route-typed family specification]

Fix `r in {H,Hol}`, `epsilon in {0,1}`, and an address in A7's literal reciprocal scope or a
separately certified covariance image. The scalarization index is route-specific:

```text
I_[a]^H
 :=Triv_[a],

I_[a;A1,A0,N]^Hol
 :=Scal_[a;A1,A0,N]^Hol.                           (C1)
```

Write `i=T` on H and `i=S` on HOL. A common R9 package `Sbold=(S_T)_T` supplies only the diagonal
subfamily `S_T` of the second index set; A7 carriage on HOL still ranges over every retained S, not
only that diagonal.

For one formed index i, the full carriage datum has the type

```text
D_(a,epsilon)^(per,r)
 =:D_(a,epsilon)^r,

d_(a,epsilon)^(per,r)
 =:d_(a,epsilon)^r,

B_(a,epsilon,i)^(per,r)
 :D_(a,epsilon)^r->D_(a,epsilon)^r,

d_(a,epsilon)^(per,r)
 :D_(a,epsilon)^r x D_(a,epsilon)^r
  ->[0,infinity),

q_(a,epsilon,i)^(per,r)
 :=sup_(K!=K' in D_(a,epsilon)^(per,r))
     d(B_(a,epsilon,i)^(per,r)(K),
       B_(a,epsilon,i)^(per,r)(K'))
     /d(K,K'),

Cell_(a,epsilon,i)^r
 :=(A_(a,epsilon,i)^r,
    chi_(a,epsilon,i)^r,
    q_(a,epsilon,i)^(per,r),
    modulus_mode_(a,epsilon,i)^r,
    required_factor_or_direct_identities_(a,epsilon,i)^r,
    contraction_cell_label_(a,epsilon,i)^r),

L_(a,epsilon,i)^(cert,r)
 :=the response-independent certified FULL-CELL lattice fixed
   before Cell_(a,epsilon,i)^r is classified.       (C2)
```

The empty-secants convention remains `q_i=0` on a singleton domain. The domain and denominator metric
are index-free exactly as the review requires; only the scalarized self-map in the numerator carries
i. The q-coordinate is M2 with the correct family index. The lattice entry is the full audit cell, not
the total q-projection `{0} union (0,1) union [1,infinity]`. A fully formed and certified Cell outside
the independently fixed full-cell lattice remains an exit witness. A missing or inconsistent
factor/direct identity, certificate mode, or certificate is `PENDING` or its own earlier falsifier,
not silently reclassified as an A7 lattice exit.

In `Q` mode, `PERIOD_MODULUS_COMPATIBILITY_CERT[...,Q]` contains exactly one of the audit's two
witnesses: `DIFF_TO_METRIC_Q` (M7) or `DIRECT_MODULUS_Q` (M8); either one identifies q exactly with
the M2 same-metric quotient. In `FACTOR` mode it contains `L0`, the `FIXED_PERIOD_FACTOR_CERT`, and
`PERIOD_MODULUS_COMPATIBILITY_CERT[...,FACTOR]`, using either the M8a differential arm or the
M8-plus-M9 direct-secant arm, together with the displayed `q_i=|chi_i|A_i` identity and the
zero-times-infinity rule. These fields are fixed by certificates, not inferred from the eventual
contraction label.

### 3.2 [YOURS — non-vacuous dependent-product carriage]

For each index i, define the failure-capable member type

```text
CarryDatum_(a,epsilon,i)^r
 :={(B,D,d,q,Cell,RouteCert,ModulusCert,LatticeCert):

     ROUTE_FORMED[a,epsilon,r;i]
     and B:D->D
     and d is the certified complete-domain metric
     and q is exactly the d/d supremum in C2
     and Cell is exactly the full tuple in C2
     and RouteCert and ModulusCert and LatticeCert are inhabited
     and Cell in L_(a,epsilon,i)^(cert,r)}.          (C3)
```

Then A7 carriage is the single well-typed statement

```text
A7_CARRIAGE_CERT_([a],epsilon)^r
 :<=>I_[a]^r is nonempty
     and the dependent product

       product_(i in I_[a]^r) CarryDatum_(a,epsilon,i)^r

     is inhabited.                                 (C4)
```

For HOL, the suppressed `[A1,A0,N]` indices in C4 remain present as in C1. C4 never evaluates an
undefined q: q and Cell exist only inside an inhabited `CarryDatum_i`. The nonempty-index clause
prevents an empty HOL scalarization family from passing vacuously.

The exit and pending states are distinct:

```text
A7_LATTICE_EXIT_([a],epsilon)^r
 :<=>there exist i and an otherwise formed, certified tuple
      (B,D,d,q,Cell,RouteCert,ModulusCert,LatticeCert)
      satisfying every C3 clause except

      Cell notin L_(a,epsilon,i)^(cert,r);

A7_CARRIAGE_PENDING_([a],epsilon)^r
 :<=>I_[a]^r is empty
      or some required route, metric, modulus, full-cell,
         or lattice certificate needed for a total C4 member
         is unformed.                               (C5)
```

One exhibited `A7_LATTICE_EXIT` witness triggers A7's carriage falsifier for that branch. C5 is not an
exit witness and does not pass carriage. The product in C4 carries one route's own family; it equates
no values at distinct indices and is not the cross-route quantifier retired from R9.

### 3.3 [PART-PROVABLE] H-family covariance and its exact missing certificate

On H, the review proves non-invariance in general because T is postcomposed while the modulus
denominator is T-free. An exact transition law additionally requires the following typed data. For
`g=g_(T',T)`, require

```text
D_(a,epsilon)^(per,H)
 =:D subset K_amb,

g(D)=D,

g_D:=g|_D:D->D is a bijection,

B_(a,epsilon,T')^(per,H)
 =g_D compose B_(a,epsilon,T)^(per,H),

d(g_D x,g_D y)=h_d(g)d(x,y),
h_d(g)>0.                                           (C6)
```

Under C6, the exact computation is

```text
q_(a,epsilon,T')^(per,H)
 =sup_(K!=K')
    d(g_D B_T(K),g_D B_T(K'))/d(K,K')

 =sup_(K!=K')
    h_d(g)d(B_T(K),B_T(K'))/d(K,K')

 =h_d(g)q_(a,epsilon,T)^(per,H).                   (C7)
```

The strong orbit-covariance certificate is

```text
PERIOD_ORBIT_COVARIANCE_CERT[a,epsilon,H]
 :=C6-C7
   and there are coherent full-cell transports kappa_g with

      kappa_g(Cell_(a,epsilon,T)^H)
       =Cell_(a,epsilon,T')^H,

      kappa_g(L_(a,epsilon,T)^(cert,H))
       =L_(a,epsilon,T')^(cert,H),

      kappa_g(RouteCert_T,ModulusCert_T,LatticeCert_T)
       =(RouteCert_T',ModulusCert_T',LatticeCert_T'),

      kappa_id=id,
      kappa_(g2 g1)=kappa_g2 compose kappa_g1.       (C8)
```

C8 types the orbit-covariant full-cell class; no member is asserted. Without C8, C4 remains the
well-typed carry-all-index predicate, while the stronger numeric/lattice orbit class is `PENDING`.

For central sign reversal, an inhabited inversion-isometry arm of C6 has `h_d(-id)=1`, so

```text
q_(a,epsilon,-T)^(per,H)
 =q_(a,epsilon,T)^(per,H).                         (C9)
```

Only under C8-C9 does the full cell descend through the sign quotient. Positive scale is never
quotiented out. If a later degree-one metric certificate supplies `h_d(s id)=s`, then C7 reads

```text
q_(a,epsilon,sT)^(per,H)
 =s q_(a,epsilon,T)^(per,H),                       (C10)
```

but C10 is conditional and is not used to claim a sealed homogeneity degree.

### 3.4 [PART-PROVABLE] Epsilon zero

On H at A7's zero branch,

```text
E_C,RL c_RL=0,

im(P_H,RL) intersection ker(E_C,RL)
 =span{c_RL}.                                      (C11)
```

C11 removes the H contact obstruction but decides neither `chi_(a,0,T)^H` nor `q_(a,0,T)^H`. HOL has
no `E_C` action, so C11 is not transferred there. On both routes, epsilon-zero carriage is exactly

```text
A7_CARRIAGE_CERT_([a],0)^r                         (C12)
```

with the route-specific index set C1 and full cells C2-C4. Different H scales, or different HOL
scalarization members, may occupy different certified cells. In particular,

```text
q_(a,0,T)^H<1
and q_(a,0,T')^H>=1                                (C13)
```

does not itself violate C4 when both full cells belong to their independently fixed certified
lattices. The `q>=1` cell is non-strict, not automatically a lattice exit. C12 gives no single
branch-level contraction verdict, preferred index, fixed point, or end-test execution.

Thus epsilon-zero carriage is **TYPED** as a dependent family and, conditionally on C8, as an
orbit-covariant full-cell class. Its present state is `PENDING`: neither route has the total C4
member, and C8 has no member.

### 3.5 [PART-PROVABLE] Epsilon one, displayed for contrast

For every formed H index T at the literal reciprocal stage, the identity branch gives

```text
E_C,RL c_RL=c_RL,

im(P_H,RL) intersection ker(E_C,RL)={0},

P_H,RL Gamma_(a,1,K)^H(Y)=0,
Per_(a,1,K)^H(Y)=0,

B_(a,1,T)^(per,H)(K)
 =u_(a,T)^H(0)
 =0,

d(B_T(K),B_T(K'))=d(0,0)=0,

q_(a,1,T)^(per,H)=0.                              (C14)
```

If C4 is inhabited, C14 holds at every H index and the q-coordinate is the constant-zero family.

For every formed HOL index `S=(U_b^S,log_b^S,U_a^S,...)`, the full
`A7_HOL_BRANCH_COMPAT` package requires both response and factor-basis neutrality:

```text
Theta_(a,K)^Hol(Y_(a,1)^Hol(K))=1_(U(1)),
Theta_(a,K)^Hol(Rhat_(Kcycle,a))=1_(U(1)),

1_(U(1)) in U_b^S,
log_b^S(1_(U(1)))=0,
U_a^S(0)=0.                                         (C15)
```

The response arm gives the direct modulus chain

```text
B_(a,1,S)^(per,Hol)(K)
 =U_a^S(log_b^S(Theta_(a,K)^Hol(Y_(a,1)^Hol(K))))
 =U_a^S(log_b^S(1_(U(1))))
 =U_a^S(0)
 =0,

d(B_S(K),B_S(K'))=d(0,0)=0,
q_(a,1,S)^(per,Hol)=0.                             (C16)
```

The factor-basis arm gives

```text
chi_(a,1,S)^Hol
 :=U_a^S(log_b^S(Theta_(a,K)^Hol(Rhat_(Kcycle,a))))
 =U_a^S(log_b^S(1_(U(1))))
 =U_a^S(0)
 =0.                                               (C17)
```

Thus, under the respective formed-index premises, epsilon one has q-coordinate zero on H and HOL;
the HOL full factor cell additionally uses C17. Before a total C4 member is inhabited, neither route
receives a vacuous family-wide carriage pass.

### 3.6 Covariance scope

For a rank-preserving image, require a route-typed index transport

```text
f_*^H:Triv_[a]->Triv_[f.a],

f_*^Hol:
 Scal_[a;A1,A0,N]^Hol
 ->Scal_[f.a;f.A1,f.A0,f.N]^Hol,                   (C18)
```

and, for `i'=f_*^r(i)`, an isometric bijection plus the exact square

```text
f_D:D_(a,epsilon)^(per,r)->D_(f.a,epsilon)^(per,r),

d_(f.a,epsilon)^(per,r)(f_D K,f_D K')
 =d_(a,epsilon)^(per,r)(K,K'),

f_D compose B_(a,epsilon,i)^(per,r)
 =B_(f.a,epsilon,i')^(per,r) compose f_D.          (C19)
```

A change of variables in C2 then gives

```text
q_(f.a,epsilon,i')^(per,r)
 =q_(a,epsilon,i)^(per,r).                         (C20)
```

Transport of C4 additionally requires the full Cell/lattice/certificate square analogous to C8; C20
alone does not transport carriage. Absent C18-C20 and that square, C4-C17 stay at the literal
reciprocal stage. Cycle creation extends only over a certified contravariant old-image restriction;
no epsilon label, sign, scale, scalarization member, modulus, or lattice is lifted upward to a
target-new-cycle summand.

## 4. Bounded delta and consequence board

| Item | V001/review state | V002 delta | Result |
|---|---|---|---|
| S1 orientation family | SOUND | unchanged | no sign, scale, or address representative selected |
| old R9 | annihilator through independent cross-product quantification | retired | unavailable for any consumer |
| R9-V002 | absent | R9a-R9p | non-degenerate orbit-return falsifier typed |
| A8 execution today | both routes unformed | unchanged | no equality or disagreement evaluated |
| epsilon-zero modulus | q family dependence undisplayed | C1-C13 | carriage typed as a route-specific full-cell family; currently pending |
| epsilon-one modulus | zero under route/A7 premises | C14-C17 | zero q-coordinate displayed conditionally; HOL factor cell also uses C17 |
| S2 bookkeeping D3 | double-counting residue | outside bounded delta | remains for its owning repair |
| route boards D3 | carrier/modulus rows omitted | C1-C5 supply the full-cell modulus/carriage row type only | carrier-row bookkeeping remains |
| S3/J-II collapse | confirmed | unchanged | J-II inhabitance remains the common blocker |

R9-V002 regains discriminatory content only on an actually common formed instance. On epsilon one,
C14-C17 make equality `0=0` under their premises; A8's discriminating branch remains epsilon zero.
That observation selects neither branch and executes no falsifier.

## 5. Battery and self verb audit

### 5.1 F_PLDEC and false-anchor audit

The construction order in this delta is

```text
sealed orientation orbit + retained route contracts
 ->response-independent ScalOrb route typing
 ->associated orbit returns
 ->A8 comparison;

formed route member + independently fixed metric/lattice certificates
 ->route-indexed self-map
 ->q_i by Banach's d/d quotient
 ->full Cell_i
 ->dependent-family carriage predicate.           (B1)
```

No reader, local symbol `p_loc`, response consequence, desired contraction cell, threshold, fixed
point, end test, measured value, or false-anchor equation enters before the common alignment, lattice,
or modulus definition. The full-cell lattice is fixed before q is classified; `ScalOrb` is indexed
only by `[a;A1,A0,N]` and is fixed before any `epsilon`, `K`, `Y`, or route return is compared.

### 5.2 Anti-tuning and no-selection ledger

| Hazard | Control | Result |
|---|---|---|
| choose T to make R9 agree | R9h is representative-free and R9g transports both sides | clean |
| compare every H member with a frozen HOL member | R9-V002 uses one associated-orbit object per common physical instance and retains all alleged route packages | removed |
| agreement-filter the HOL alignment | T5 fixes `ScalOrb` at the structural route-package index and each `S_T` must independently satisfy `Scal^Hol` | clean |
| choose `r_T=1` | full positive-scale family retained | clean |
| choose a contractive index | C4 requires a total dependent-product member; C13 gives no selection | clean |
| make lattice fit q | each full-cell lattice and certificate precedes q classification in C2-C3 | clean |
| treat `q>=1` as lattice exit | C13 keeps non-strict cells distinct from full-cell exit C5 | clean |
| choose epsilon zero because epsilon one vanishes | both labels remain carried | clean |
| infer exact positive-scale law without metric homogeneity | C10 remains conditional on C6-C8 | clean |
| lift onto a target-new cycle | C18-C20 stop at covariant/old-image scope | clean |
| execute A8, fixed point, or end test | all remain unexecuted | clean |

### 5.3 Self verb audit

| This artifact says | Display that licenses it | Audit |
|---|---|---|
| old R9 annihilates | review's two-member computation, restated as the retired premise in P1 | clean |
| R9 repaired | R9a-R9j type the carrier, equality, covariance, and single-cell falsifier | clean |
| no forced zero | R9k-R9o leave the full diagonal `{(p,p):p in R}` | clean |
| A8 honored | §2.5 matches every operative A8 phrase and introduces no cross-product quantifier | clean |
| modulus family-dependent | review D2 proves non-invariance in general; C7 gives an exact law only under C6 | clean |
| epsilon-zero carriage typed | C1-C5 and C12 define a non-vacuous full-cell dependent product without evaluating a member | clean |
| epsilon-one family zero | C14 on H and C15-C17 on HOL retain their distinct formed-index premises | clean |
| pending | C5 names the exact missing route/full-cell/certificate family | clean |

No verb upgrades a definition to an inhabitant, a conditional equality to a sealed theorem, a
non-strict cell to a lattice exit, or a typed falsifier to an executed one.

```text
F_PLDEC = CLEAN;
ANTI_TUNING = CLEAN;
MEMBER_BOUND = false;
FIXED_POINT_EXECUTED = false;
END_TEST_EXECUTED = false;
NUMERIC_EVALUATION = false.
```

No register, plan, tracker, git, commit, push, member-binding, fixed-point, end-test, or evaluation
action was performed by this lane. No law was adopted, no route was chosen, and no A7 branch was
selected.

R9 = REPAIRED (+on each common physical cell with both typed period-return constructions, equality of the two associated-orbit return sections; no independent Triv_[a] x Scal^Hol quantifier)
EPSILON0_CARRIAGE = TYPED (+the route-specific full-cell family is carried—q_T on H and q_S on HOL; the stronger orbit-covariant class is exactly gated by C8; one certified full-cell exit is a falsifier, missing certificates are pending, and no uniform contraction verdict is inferred)
VERB_AUDIT_SELF = CLEAN
