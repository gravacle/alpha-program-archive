# STAGE 8 TASK 5 — THE COMMON SEAMS, BUILT ONCE FOR BOTH ROUTES

Lane: CODEX LANE 3 (SOL, HIGH EFFORT)  
Version: V001  
Date: 2026-08-05  
Custody: builder; Dario reviews  
Scope: symbolic construction and determination only

## 0. Preflight and lead determination

[PROVABLE — no-clobber] Before construction, the requested artifact and its seal were absent in
both the Lane-3 cleanroom and the archive workspace.

[PROVABLE — register at start] Before any construction, the supervision register ended at Q-508
before its usage instructions, so the commissioned preflight passed. A final read found Q-509 had
been appended concurrently by the parallel Lane-583 work. Q-509 records a not-adopted Xi_N V002
draft; it neither changes the sealed authorities consumed here nor retroactively changes the
Q-508 start condition. This lane did not edit the register or consume Q-509 as law.

[PROVABLE — controlling review] The gap audit and its sidecar were verified before reading:

~~~text
STAGE8_TASK5_GAMMA_H_REVIEW_DARIO_V001.md
lines   = 288
SHA-256 = 61d41a3ed13039b8db1c149215763f97e0c4f2a5376ae717fd400f1962eae712
sidecar = OK.
~~~

Its J-I, J-III, and J-IV sections were read first. The original Gamma-H joint boards were then read
against that correction. The resulting determination is:

~~~text
S1 orientation-address structure
 = BUILT as the two-member sign orbit at each primitive
   orientation orbit; the independent positive dimensionless scale
   remains a carried family coordinate and no member is selected;

S2 corestriction/descent
 = DISPLAYED; descent is automatic after a continuous source-extension
   member is supplied, but that member and the addressed response leg
   remain uninhabited;

S3 physical F3 on nonidentity arrows
 = PARTIAL; represented Q-408 transport and composition conditional
   on S22/S22a plus physical generator squares are proved, but no
   actual nonidentity physical F3 base square is.
~~~

The gates remain:

~~~text
alpha_computed = false;
proof_authorized = false;
kappa_record_computed = false;
member_bound = false;
fixed_point_executed = false;
end_test_executed = false;
numeric_evaluation = false.
~~~

## 1. Authority and type ledger

### 1.1 Verified sources

| Key | Sealed authority | SHA-256 |
|---|---|---|
| GAP | STAGE8_TASK5_GAMMA_H_REVIEW_DARIO_V001.md | 61d41a3ed13039b8db1c149215763f97e0c4f2a5376ae717fd400f1962eae712 |
| GH | STAGE8_TASK5_GAMMA_H_ROUTE_LANE3_V001.md | f2317e41367dc906ffa23f6055f2ed96a0f59f74b4e412966809d292c23e5402 |
| SEED | STAGE8_TASK5_EQ6_TWO_LEMMAS_LANE3_V001.md | 48616c239ccdd777d1ac7cf5a049f324b98ca6abdba84966c5dc98151c461de4 |
| HODGE | STAGE8_TASK5_EQ6_MAXWELL_HODGE_PROJECTOR_CERT_LANE2_V001.md | f074ca24e8b96c576f5c64b856377f39ed8d4fc729c02cbf591326322558f816 |
| MET | DOR_019_CARRIER_METRIC_AND_UNITS_RATIFICATION_2026-08-03.md | 6ab72b0cb3a93e123eb1d3c5088fc83361d86c6dc739f0a886380dbd2d143f1f |
| SYM | STAGE8_TASK5_R4_LOCAL_SYMBOL_MAP_BUILD_LANE1_V001.md | bae34116c4d6792b5e39b913addeeff1650989660d89ba01bf5de62ec2d9aa50 |
| KER | STAGE8_TASK5_R4_KERNEL_REALIZATION_AND_SYMBOL_CALCULUS_LANE2_V001.md | ccb94dfa8927cf8d2ec76cf85ff2f402d02d5aa5673b9d39c214a6de4c92309c |
| LOC | STAGE8_TASK5_EQ6_THE_LOC_BUILD_LANE3_V001.md | b53d9e931efe1ebde333ef49fb4243e41917bb5d467f5a86e7052102ae5a0310 |
| NAT | STAGE8_TASK5_EQ6_LOC_NATURALITY_LANE3_V001.md | 474bf721517f77b240e2a215325a86227d4e0fd4934e89ba910d955627b5ab60 |
| AUD1 | STAGE8_TASK5_CHAIN_CONFORMANCE_AUDIT_LANE3_V001.md | d02576c8a40d6b317819b369f8a6413e24d0e2a792c18a3610df0600e3480ea1 |
| AUD2 | STAGE8_TASK5_CHAIN_CONFORMANCE_AUDIT_LANE3_V002.md | 44202c060821728fba2c46b81b82487002e639f3242565b7a5fed387e41fcae8 |
| GUARD | STAGE8_TASK5_EQ6_AXIOM_V002_AND_EXHIBITION_LANE2_V001.md | a681c784b451790c1163d083865988d2256170d1f0c468609b9a803864a0ab4b |
| A8 | DOR_020_A8_GAMMA_BOTH_ROUTES_2026-08-05.md | 0ee6c897055f803b31bc570b9f4ef852ccb3c4aba21fcd5274a7d740c8eb601d |
| XI-R | STAGE8_TASK5_XI_N_REVIEW_AND_DISPLAYS_LANE3_V001.md | c9b62076cc07951ec26fcf4aa4c15e21ec973f6089fb83ca476a98b83aefd071 |

### 1.2 Notation frozen before construction

An oriented address and its reverse are

~~~text
a=(w,N,gamma),
a^-=(w,N,-gamma),
[a]:={a,a^-}.                                    (T1)
~~~

The primitive harmonic representatives obey

~~~text
c_a:=c_(N,gamma),
c_(a^-):=c_(N,-gamma)=-c_a.                     (T2)
~~~

The cochain-valued physical localization, when a future member exists, is

~~~text
Loc_N^phys:D_N^Loc->Sym_N^loc,
iota_N^H:Sym_N^loc->C_N^k,
Loc_N^C:=iota_N^H compose Loc_N^phys.            (T3)
~~~

The following distinctions are load-bearing:

~~~text
qtilde_N:E_N->O_R5,N             raw R5 realization;
Q_N^quot:E_N->O_prof,N           quotient projection;
Q_N^core:E_N->im(qtilde_N)       literal corestriction;

O_w^resp:=O_R5,w                 unaddressed response carrier;
Res_(w,a)^resp:O_w^resp->O_a^resp
                                  addressed restriction;

Loc_N^fin / sigma_N^fin          finite datum or declared shadow;
Loc_N^C                           physical kernel-to-cochain map. (T4)
~~~

No equality between the last two lines of T4 is assumed.

## 2. S1 — the orientation-address structure

### 2.1 [PROVABLE] The unit half dissolves

Let U_k be the ratified unit torsor of C_N^k. The DoR-019 rule

~~~text
[R_k]=U_k^(-2)                                   (O1)
~~~

gives, degree by degree,

~~~text
[d_k]
 =U_(k+1) U_k^(-1),

[delta_(k+1)]
 =[R_k^(-1)] [d_k^*] [R_(k+1)]
 =U_k^2
   (U_(k+1) U_k^(-1))
   U_(k+1)^(-2)
 =U_k U_(k+1)^(-1),                             (O2)

[Delta_k]
 =[d_(k-1)] [delta_k]
 =(U_k U_(k-1)^(-1))
  (U_(k-1) U_k^(-1))
 =1,

[P_H,k]=1.                                      (O3)
~~~

For x,h in C_N^k, the Hodge pairing has

~~~text
[<x,h>_N]
 =[(R_k x)(h)]
 =U_k^(-1) U_k
 =1.                                             (O4)
~~~

Thus the period evaluation is dimensionless. There is no dimensionful or cross-sector C-to-K unit
conversion coefficient, and there is no application of the chi_CK exclusion. The independent
dimensionless trivialization scale remains a carried family coordinate below. The object formerly
called ChargeUnit_N is correctly read here as a signed orientation line of physical unit class 1.

### 2.2 [PROVABLE] The sign is real and address-sensitive

Metric positivity and the primitive integral scale give

~~~text
r_[a]^2
 :=<c_a,c_a>_N
 >0,                                             (O5)

<c_(a^-),c_(a^-)>_N
 =<-c_a,-c_a>_N
 =<c_a,c_a>_N
 =r_[a]^2.                                       (O6)
~~~

For lambda in (H_N^k)^*, define

~~~text
ev_a(lambda):=lambda(c_a).                       (O7)
~~~

Then every reversal equality is displayed:

~~~text
ev_(a^-)(lambda)
 =lambda(c_(a^-))
 =lambda(-c_a)
 =-lambda(c_a)
 =-ev_a(lambda).                                 (O8)
~~~

At the actual reciprocal-loop stage, the Q-493 W3 stock gives the concrete sign regression.
Writing e_1,e_2 for the two oriented edge-local inputs so they are not confused with address a,

~~~text
0 < <c_RL,c_RL>_RL
 =<e_1,c_RL>_RL-<e_2,c_RL>_RL.                  (O9)
~~~

Under address reversal,

~~~text
<e_1,-c_RL>_RL-<e_2,-c_RL>_RL
 =-<e_1,c_RL>_RL+<e_2,c_RL>_RL
 =-(<e_1,c_RL>_RL-<e_2,c_RL>_RL)
 =-<c_RL,c_RL>_RL
 <0.                                             (O10)
~~~

Equations O9-O10 use the whole sealed edge orbit. They do not select e_1 or e_2. At this actual
reciprocal-loop stage they establish that the raw evaluation has a nonzero-capable sign
representation and cannot be relabelled as an address-independent trivial scalar. Equation O8
establishes formal oddness at every address for which the primitive representative has already
been exhibited; O9-O10 do not export reciprocal-loop nonvanishing to other stages.

### 2.3 [YOURS] Construction of the retained family

For the unoriented orbit [a], define the addressed real orientation line without choosing one of
its two addresses:

~~~text
R_or,[a]
 :=(R x [a])/equivalence,

(q,a^-) equivalent_to (-q,a),

iota_b:R->R_or,[a],
iota_b(q):=[q,b],
iota_(b^-)(q)=iota_b(-q).                       (O11)
~~~

This quotient is a one-dimensional real line of physical unit class 1. For every b in [a], the
ordinary evaluation O7 has the typed lift

~~~text
ev_b^or:(H_N^k)^*->R_or,[a],
ev_b^or(lambda):=iota_b(lambda(c_b)).            (O12)
~~~

The two sign reversals now occur inside one carrier:

~~~text
ev_(b^-)^or(lambda)
 =iota_(b^-)(lambda(c_(b^-)))
 =iota_(b^-)(-lambda(c_b))
 =iota_b(lambda(c_b))
 =ev_b^or(lambda).                               (O13)
~~~

Define the full nonzero linear-trivialization family

~~~text
Triv_[a]
 :=Iso_R(R_or,[a],K_amb).                        (O14)
~~~

For T in Triv_[a], define its addressed coefficient by

~~~text
1 in R,
1_Kamb in K_amb,

T(iota_b(1))=:mu_T(b) 1_Kamb.                   (O15)
~~~

From O11 and linearity,

~~~text
mu_T(b^-) 1_Kamb
 =T(iota_(b^-)(1))
 =T(iota_b(-1))
 =-T(iota_b(1))
 =-mu_T(b) 1_Kamb,

mu_T(b^-)=-mu_T(b).                             (O16)
~~~

The complete parameter account is

~~~text
r_T:=abs(mu_T(b)) in R_(>0),
sigma_T(b):=mu_T(b)/r_T,

Sigma_[a]
 :={sigma:[a]->{+1,-1}:
       sigma(b^-)=-sigma(b)},

Triv_[a]
 isomorphic_to R_(>0) x Sigma_[a],
T maps_to (r_T,sigma_T),

T_(r,sigma)(iota_b(q))
 :=r sigma(b) q 1_Kamb.                         (O17)
~~~

The last formula is well defined because replacing `(q,b)` by `(-q,b^-)` leaves its value
unchanged. Sigma_[a] has two members, but neither member has a canonical `+` label until an address
is selected. The trivialization condition excludes r=0 by definition; metric positivity and the
unit rule do not force r=1. Thus O14-O17 carry every sign and positive-scale member and bind none.

### 2.4 [PROVABLE from O11-O17] Address covariance

For b in [a] and T in Triv_[a], first type the addressed raw-coordinate map and then the scalar
return:

~~~text
U_(b,T)^H
 :=T compose iota_b
 :R->K_amb,

u_(b,T)^H
 :=U_(b,T)^H compose ev_b
 =T compose ev_b^or
 :(H_N^k)^*->K_amb.                              (O18)
~~~

Equations O13 and O16 give the two required covariance statements separately:

~~~text
mu_T(b^-)=-mu_T(b),

U_(b^-,T)^H
 =T compose iota_(b^-)
 =T compose iota_b compose (-id_R)
 =-U_(b,T)^H,

u_(b^-,T)^H
 =U_(b^-,T)^H compose ev_(b^-)
 =(-U_(b,T)^H) compose (-ev_b)
 =U_(b,T)^H compose ev_b
 =u_(b,T)^H.                                    (O19)
~~~

Thus the addressed coefficient, the raw coordinate evaluation, and U_(b,T)^H are odd. The address
injection is also odd, so the lifted orientation-line evaluation O13 and the final typed composite
are invariant. Every equality holds memberwise and therefore for the retained family without
binding a representative.

For an admitted rank-preserving W3 arrow f carrying the primitive class isometrically,

~~~text
j_f^C(c_a)=c_(f.a),

<c_(f.a),c_(f.a)>_M
 =<j_f^C c_a,j_f^C c_a>_M
 =<c_a,c_a>_N.                                   (O20)
~~~

Define the induced orientation-line isomorphism and transport the whole family by

~~~text
f_or:R_or,[a]->R_or,[f.a],
f_or(iota_a(q)):=iota_(f.a)(q),

f_*T:=T compose f_or^(-1)
 in Triv_[f.a],

mu_(f_*T)(f.a)=mu_T(a),
r_(f_*T)=r_T.                                    (O21)
~~~

The two sign components and every positive-scale coordinate map bijectively to the target family.
For a cycle-creating arrow h:N->M, let a_M^old be an exhibited target primitive in the old-image
sector with the lawful downward cochain map

~~~text
rho_h^C(c_(a_M^old))=c_(a_N).

rho_h^or:R_or,[a_M^old]->R_or,[a_N],
rho_h^or(iota_(a_M^old)(q)):=iota_(a_N)(q),

T_M^old
 :=T_N compose rho_h^or
 in Triv_[a_M^old]
 for every T_N in Triv_[a_N].                  (O21a)
~~~

This is contravariant old-image transport: it restricts the target-old primitive to the source and
pulls the source trivialization back to that target-old line. It defines no member on the
target-new-cycle complement. A target-only new cycle receives its own address orbit and full
family; no upward sign or scale lift is installed.

The exact voids are:

1. address-independent mu with nonzero evaluation, because O8 would force mu=-mu and hence zero;
2. r=0 while claiming a trivialization, or r=1 claimed as forced without a normalization premise;
3. selecting T, sigma_T, r_T, or a sign from a reader, response, threshold, fixed point, end test, or
   desired consequence;
4. collapsing the sign pair or positive-scale family without a separately proved invariant
   consumer or normalization law;
5. claiming O21 on an arrow that does not carry the primitive isometrically;
6. assigning a sign upward to a target-only new cycle;
7. reintroducing a dimensionful unit-conversion coefficient or a bottom/scalar identification.

The orientation-address seam is therefore built as the honest family O14-O17. Its sign orbit is
two-member; its positive dimensionless magnitude remains free and carried. It is not a selected
scalar convention.

## 3. S2 — Q corestriction and automatic source descent

### 3.1 [PROVABLE] Four carriers and four arrows

The raw source and R5 realization are

~~~text
E_N
 :=R L_T,N
   direct_sum_1 R R_K,N
   direct_sum_1 S_(1,sa)(K_N),

qtilde_N:E_N->O_R5,N,

qtilde_N(a,b,C)
 :=a L_T,N+j_R4,N(b R_K,N+C).                   (Q1)
~~~

Set the underlying image and keep its two potentially different topologies distinct:

~~~text
I_N:=im(qtilde_N),
Rel_N:=closure(ker(qtilde_N)),

O_prof,N:=E_N/Rel_N,
Q_N^quot:E_N->>O_prof,N,

I_N^q
 :=I_N with the quotient topology induced by qtilde_N,

I_N^R5
 :=I_N with the subspace topology inherited from O_R5,N. (Q2)
~~~

The literal corestriction is

~~~text
Q_N^core
 :=corestr_(I_N^q)(qtilde_N)
 :E_N->>I_N^q,

Q_N^core(z)=qtilde_N(z).                         (Q3)
~~~

Whenever Rel_N=ker(qtilde_N) on the stated topology, the first-isomorphism map is

~~~text
beta_N:O_prof,N->I_N^q,
beta_N(Q_N^quot z):=qtilde_N(z),                 (Q4)

Q_N^core
 =beta_N compose Q_N^quot.                       (Q5)
~~~

The underlying-set identity and physical inclusion are

~~~text
kappa_N:I_N^q->I_N^R5,
kappa_N(x):=x,

jmath_N:I_N^R5->O_R5,N,
jmath_N(x):=x.

jmath_N kappa_N beta_N Q_N^quot(z)
 =jmath_N kappa_N(qtilde_N(z))
 =jmath_N(qtilde_N(z))
 =qtilde_N(z).                                   (Q6)
~~~

This displays the exact sense in which the quotient presentation may be read as the
corestriction. The canonical profile arrow points

~~~text
O_prof,N --beta_N--> I_N^q
 --kappa_N--> I_N^R5
 --jmath_N--> O_R5,N.                           (Q7)
~~~

not from O_R5,N back to O_prof,N.

[PART-PROVABLE — topology boundary] KER records that O_prof,N remains an abstract quotient until
continuity/topological embedding into the physical O_R5,N topology is proved. Giving I_N^q the
quotient topology makes beta_N a topological isomorphism by definition; it does not prove that the
identity kappa_N is continuous or that the quotient and inherited topologies agree. The inclusion
jmath_N is a topological embedding by the definition of I_N^R5, but that fact does not repair
kappa_N.

### 3.2 [PROVABLE] The canonical O_R5-to-response arrow

At unaddressed scope, response notation is definitional:

~~~text
O_w^resp:=O_R5,w.                                (Q8)
~~~

Hence

~~~text
iota_w^resp:
 O_R5,w->O_w^resp,

iota_w^resp(Y):=Y,
(iota_w^resp)^(-1)=iota_w^resp,                 (Q9)

iota_w^resp qtilde_w(z)
 =qtilde_w(z)                                    (Q10)
~~~

after the codomain relabelling in Q8.

The addressed arrow is separate and remains a required future member. Its complete local type is

~~~text
Res_(w,a)^resp:
 O_w^resp->O_a^resp
 continuous and linear,

Res_(w,a,K)^resp:=Res_(w,a)^resp
 for every allowed K,

res_(w,a)^supp:Supp_w->Supp_a,

supp_a(Res_(w,a)^resp(Y))
 subset res_(w,a)^supp(supp_w(Y)).               (Q11)
~~~

The second line displays K-independence; the last two type support compatibility without asserting
a particular support member. No member of Q11, inverse, section, or arrow
O_a^resp->O_prof,N is obtained from Q9. Thus the unaddressed identity is displayed without silently
manufacturing the addressed route.

### 3.3 [PART-PROVABLE] Automatic descent after source extension

Let a future source-extension member supply a Hausdorff topological vector space and a genuine
linear source scope

~~~text
D_N^ker                                          Hausdorff TVS,

O_R5,N^src subset O_R5,N                        vector subspace,

I_N^R5 subset O_R5,N^src,

S_N:O_R5,N^src->D_N^ker                         continuous linear. (Q12)
~~~

Every unaddressed response element on which S_N is consumed must be exhibited in O_R5,N^src.
An addressed response is not silently treated as such an element: it reaches D_N^ker only through
the separately typed Q30 factorization. On the raw realization, the linear composite is

~~~text
Kraw_N
 :=S_N compose qtilde_N
 :E_N->D_N^ker
 continuous and linear.                         (Q13)
~~~

For r in ker(qtilde_N),

~~~text
Kraw_N(r)
 =S_N(qtilde_N(r))
 =S_N(0)
 =0.                                             (Q14)
~~~

Therefore

~~~text
ker(qtilde_N) subset ker(Kraw_N).                (Q15)
~~~

Linearity gives S_N(0)=0 in Q14. Continuity into the Hausdorff carrier makes ker(Kraw_N) closed, so

~~~text
Rel_N
 =closure(ker(qtilde_N))
 subset closure(ker(Kraw_N))
 =ker(Kraw_N).                                   (Q16)
~~~

Consequently the quotient universal property gives the unique continuous linear induced map

~~~text
Sbar_N:O_prof,N->D_N^ker,

Sbar_N(Q_N^quot z)
 :=Kraw_N(z)
 =S_N(qtilde_N(z))                               (Q17)
~~~

is well defined. Every representative equality is

~~~text
Q_N^quot z=Q_N^quot z'

 =>z-z' in Rel_N

 =>Kraw_N(z-z')=0

 =>Kraw_N(z)=Kraw_N(z')

 =>Sbar_N(Q_N^quot z)=Sbar_N(Q_N^quot z').       (Q18)
~~~

Thus the old clauses Rel_N subset ker(Kraw_N) and quotient descent are not independent axioms
once Q12-Q13 are inhabited. This is the automatic half; it neither exhibits S_N nor proves that an
independently topologized physical response carrier contains the quotient as an embedded subspace.

### 3.4 [YOURS — exact remaining source-extension package]

The uninhabited package is a family over every stage N, address a, response stage w, and allowed
parameter K:

~~~text
ExtSrc
 :=(((D_N^ker,
      O_R5,N^src,
      iota_N^Q408,
      Sch_N,
      S_N,
      Kraw_N,
      Sbar_N,
      D_N^Loc))_N,
    (Res_(w,a)^resp,
     res_(w,a)^supp,
     QuotResCert_(w,a))_a,
    (T_(w->N,K)^D,
     t_(w->N,K)^supp,
     S_(w->N,K),
     Ker_(a,K)^im,
     Ker_(a,K)^ker,
     Ker_(a,K))_(a,K),
    Coh_ExtSrc),                                  (Q19)
~~~

Here `Coh_ExtSrc` is not a name hiding declarations. For every admitted rank-preserving
f:N->M it must type

~~~text
tau_f^E:E_N->E_M,
tau_f^src:O_R5,N^src->O_R5,M^src,
tau_f^prof:O_prof,N->O_prof,M,
tau_f^D:D_N^ker->D_M^ker,
tau_f^Op:Op_N^(loc,2)->Op_M^(loc,2),
tau_f^supp:Supp_N^ker->Supp_M^ker,
tau_(f,w)^D:D_w^ker->D_(f.w)^ker,
tau_(f,w)^supp:Supp_w^ker->Supp_(f.w)^ker,
tau_f^resp:O_w^resp->O_(f.w)^resp,
tau_f^a:O_a^resp->O_(f.a)^resp,
tau_f^K:Kpar_N->Kpar_M,
tau_f^K(K)=:f.K,

tau_f^src qtilde_N=qtilde_M tau_f^E,
tau_f^prof Q_N^quot=Q_M^quot tau_f^E,
tau_f^D S_N=S_M tau_f^src,
tau_f^D Kraw_N=Kraw_M tau_f^E,
tau_f^D Sbar_N=Sbar_M tau_f^prof,

tau_f^D iota_N^Q408
 =iota_M^Q408 eta_f^K,

tau_f^D Sch_N
 =Sch_M tau_f^Op,

tau_f^D(D_N^Loc) subset D_M^Loc,

tau_f^D S_(w->N,K)
 =S_(f.w->M,f.K) tau_f^resp,

tau_f^D T_(w->N,K)^D
 =T_(f.w->M,f.K)^D tau_(f,w)^D,

tau_f^supp t_(w->N,K)^supp
 =t_(f.w->M,f.K)^supp tau_(f,w)^supp,

tau_f^D Ker_(a,K)^ker
 =Ker_(f.a,f.K)^ker tau_f^a,

tau_f^a Res_(w,a)^resp
 =Res_(f.w,f.a)^resp tau_f^resp.                 (Q19a)
~~~

The image clause in Q19a defines the corestriction

~~~text
tau_f^Loc
 :=corestr_(D_M^Loc)(tau_f^D|_(D_N^Loc))
 :D_N^Loc->D_M^Loc,

tau_f^Loc Ker_(a,K)
 =Ker_(f.a,f.K) tau_f^a.                        (Q19a')
~~~

For identities and composable rank-preserving arrows it must display

~~~text
tau_id^X=id_X,
tau_(g compose f)^X=tau_g^X tau_f^X
 for X in {E,src,prof,D,Loc,Op,supp,resp,a,K};

for every common-refinement relation g_1 f_1=g_2 f_2,
tau_g1^X tau_f1^X=tau_g2^X tau_f2^X.            (Q19b)
~~~

For a cycle-creating h:N->M it must replace, not reverse, these covariant equations by separately
typed downward old-image maps

~~~text
rho_h^src:O_R5,M^(src,old)->O_R5,N^src,
rho_h^D:D_M^(ker,old)->D_N^ker,
rho_h^a:O_(a_M^old)^resp->O_(a_N)^resp,
rho_h^K:Kpar_M^old->Kpar_N,

K_N:=rho_h^K(K_M),

S_M(O_R5,M^(src,old)) subset D_M^(ker,old),

rho_h^D S_M|_(O_R5,M^(src,old))
 =S_N rho_h^src,

Ker_(a_M^old,K_M)^ker(O_(a_M^old)^resp)
 subset D_M^(ker,old),

rho_h^D Ker_(a_M^old,K_M)^ker
 =Ker_(a_N,rho_h^K(K_M))^ker rho_h^a,

D_M^(Loc,old)
 :=D_M^Loc intersection D_M^(ker,old),

rho_h^D(D_M^(Loc,old)) subset D_N^Loc,

rho_h^Loc
 :=corestr_(D_N^Loc)(rho_h^D|_(D_M^(Loc,old)))
 :D_M^(Loc,old)->D_N^Loc,

rho_h^Loc Ker_(a_M^old,K_M)
 =Ker_(a_N,rho_h^K(K_M)) rho_h^a.               (Q19c)
~~~

No map is extended to the target-new-cycle complement. Equations Q19a-Q19c are required member laws;
this artifact does not assert their inhabitance. Any source transport used to form S_(w->N,K) must
be one of these typed members or be added with an equally explicit square.

Its map types are

~~~text
iota_N^Q408:
 Ker_N^Q408->D_N^ker
 continuous, injective;

Sch_N:
 Op_N^(loc,2)->D_N^ker
 continuous, injective;

S_N:
 O_R5,N^src->D_N^ker
 continuous and linear;

Kraw_N=S_N qtilde_N:
 E_N->D_N^ker
 continuous, linear;

Sbar_N:
 O_prof,N->D_N^ker
 continuous and linear;

Res_(w,a)^resp:
 O_w^resp->O_a^resp
 continuous, linear, K-independent,
 and support-compatible as in Q11;

QuotResCert_(w,a):
 Res_(w,a)^resp is a quotient map onto its image;

S_(w->N,K):
 O_w^resp->D_N^ker
 continuous and linear;

T_(w->N,K)^D:
 D_w^ker->D_N^ker
 continuous and linear;

t_(w->N,K)^supp:Supp_w^ker->Supp_N^ker;

Ker_(a,K)^im:
 im(Res_(w,a)^resp)->D_N^ker
 continuous and linear;

Ker_(a,K)^ker:
 O_a^resp->D_N^ker
 continuous and linear in its response argument. (Q20)
~~~

The single source agreement is

~~~text
S_N(qtilde_N(a,b,C))
 =a Sch_N(M_N^loc)
  +iota_N^Q408 Kernbar_N^cyc(
      Q_N^quot(0,b,C)).                          (Q21)
~~~

Its two restrictions are

~~~text
S_N(qtilde_N(1,0,0))
 =Sch_N(M_N^loc)
 =:kappa_T,N,                                    (Q22)

S_N(qtilde_N(0,b,C))
 =iota_N^Q408 Kernbar_N^cyc(
     Q_N^quot(0,b,C)).                           (Q23)
~~~

Mixed relations already present in O_R5,N must receive one value under Q21. That is a
failure-capable agreement condition, not a direct-sum assumption.

Equations Q21-Q23 determine only the restriction of S_N to the underlying set
I_N=im(qtilde_N). The extension question uses the inherited response topology, not the quotient
topology. The package must
therefore exhibit one of the following, without silently identifying them:

~~~text
O_R5,N^src=I_N^R5
 with the inherited subspace topology;

or

S_N^I:I_N^R5->D_N^ker
 has a continuous linear extension
 S_N:O_R5,N^src->D_N^ker.                      (Q23a)
~~~

No equality `I_N^q=I_N^R5` as topological carriers is used in Q23a; such an equality is precisely
the missing kappa_N embedding certificate. This is the source-extension inhabitance half left
after automatic descent.

Define

~~~text
D_N^Loc
 :=im(Sbar_N)
 =im(Kraw_N)
 subset D_N^ker,

D_N^Loc carries the quotient topology from
 E_N/ker(Kraw_N)
 isomorphic_to O_prof,N/ker(Sbar_N),

and the inclusion
 D_N^Loc->D_N^ker
 is a topological embedding.                    (Q24)
~~~

The quotient topology in Q24 is not inferred to equal the subspace topology merely from
continuity; their agreement is an explicit, failure-capable member condition. Sbar_N need not be
injective.

The required image statements are

~~~text
kappa_T,N in D_N^Loc,                            (Q25)

iota_N^Q408 Kernbar_N^cyc(O_N^cyc)
 subset D_N^Loc,                                 (Q26)

D_N^Loc
 =span{kappa_T,N}
  +iota_N^Q408 Kernbar_N^cyc(O_N^cyc),          (Q27)

D_N^Loc
 subset Sch_N(Op_N^(loc,2))                     (Q28)
~~~

on the physical L_F2-prime family. The plus sign in Q27 is not a direct sum. The inclusion
D_N^Loc->D_N^ker must be a topological embedding, and the quotient and subspace topologies must
agree.

The addressed raw map and its image clause are

~~~text
Ker_(a,K)^ker:O_a^resp->D_N^ker,

im(Ker_(a,K)^ker) subset D_N^Loc,

Ker_(a,K)
 :=corestr_(D_N^Loc)(Ker_(a,K)^ker)
 :O_a^resp->D_N^Loc.                            (Q29)
~~~

If the addressed map is to factor an unaddressed source map through Q11, type that source map
directly at the N-stage kernel carrier and connect it to the stage source extension rather than
introducing an unrelated map:

~~~text
S_(w->N,K):O_w^resp->D_N^ker,
S_(w->N,K) continuous and linear,

T_(w->N,K)^D:D_w^ker->D_N^ker
 continuous and linear,

T_(w->N,K)^D(D_w^Loc) subset D_N^Loc,

supp_N(T_(w->N,K)^D x)
 subset t_(w->N,K)^supp(supp_w(x)),

T_(N->P,K_N)^D T_(w->N,K_w)^D
 =T_(w->P,K_w)^D
 whenever the displayed parameter transports identify
 K_w maps_to K_N maps_to K_P,

T_(w->w,K)^D=id_(D_w^ker),

t_(w->w,K)^supp=id_(Supp_w^ker),

t_(N->P,K_N)^supp t_(w->N,K_w)^supp
 =t_(w->P,K_w)^supp
 on the same typed parameter chain,

S_(w->N,K)|_(iota_w^resp(O_R5,w^src))
 =T_(w->N,K)^D S_w (iota_w^resp)^(-1),

QuotResCert_(w,a):
 Res_(w,a)^resp is a quotient map onto its image,

ker(Res_(w,a)^resp)
 subset ker(S_(w->N,K)),

Ker_(a,K)^im:
 im(Res_(w,a)^resp)->D_N^ker,
Ker_(a,K)^im continuous and linear,

Ker_(a,K)^im(Res_(w,a)^resp(Y))
 :=S_(w->N,K)(Y),

Ker_(a,K)^im compose Res_(w,a)^resp
 =S_(w->N,K),

Ker_(a,K)^ker|_(im(Res_(w,a)^resp))
 =Ker_(a,K)^im,

im(Ker_(a,K)^ker) subset D_N^Loc.                (Q30)
~~~

QuotResCert makes the displayed factor through the image continuous. The package must then extend
Ker_(a,K)^im continuously and linearly from that image to all of
O_a^resp, with the extension equal to Ker_(a,K)^ker and with image in D_N^Loc. The T line in Q30 is
the required connection to the stage-w source extension; it prevents S_(w->N,K) from being an
unrelated second source map. The transport, its support/image/composition certificates, the
full-domain extension S_(w->N,K), the quotient factorization, and the addressed extension are all
unsealed.

No member of Q19-Q30 is supplied by the corestriction display. The finite cycle-profile kernel is
built, but the common L_T realization, common topology, physical image membership, and addressed
Res/Ker factorization are not.

~~~text
MACHINERY-APPEAL(S2)
 =source-extension/common-kernel inhabitance
  +physical topology and image certificate
  +addressed Res/Ker factorization.
~~~

Equations Q12-Q18 prove that descent is derived inside any inhabited ExtSrc member; they do not
supply such a member. The structural review therefore continues.

## 4. S3 — F3 on actual nonidentity generators

### 4.1 Target equation and the three tempting substitutes

For a rank-preserving f:N->M, physical F3 is

~~~text
F3(f):
 Loc_M^C compose etahat_f
 =j_f^C compose Loc_N^C
 :D_N^Loc->C_M^k.                               (F1)
~~~

Using T3, the only direct two-joint proof is

~~~text
Loc_M^C etahat_f
 =iota_M^H Loc_M^phys etahat_f
 ?=iota_M^H j_f^Sym Loc_N^phys
 ?=j_f^C iota_N^H Loc_N^phys
 =j_f^C Loc_N^C.                                (F2)
~~~

The first question mark is the uninhabited S24 physical-symbol square. The second is the
uninhabited S25 Hodge-realization square.

The following sealed statements do not fill either question mark:

~~~text
eta_f^K Kernbar_N^cyc(H)
 =Kernbar_M^cyc(j_f^prof H)                     (F3)
~~~

is represented Q-408 kernel transport;

~~~text
rho_M^resp Eta_f
 =Bot_resp(f) rho_N^resp                        (F4)
~~~

is finite-bottom naturality; and

~~~text
P_H,M j_f^C
 =j_f^C P_H,N                                   (F5)
~~~

is rank-preserving Hodge/projector naturality after a cochain already exists.

The finite C3 expression

~~~text
(j_f^fld)^* sigma_M^fin j_f^fld                 (F6)
~~~

is a contravariant datum pullback. It is not a map Ker_N^Q408->C_N^k, and no sealed equality
j_f^fld=j_f^C is supplied. Thus F3-F6 cannot be composed into F1.

### 4.2 [PROVABLE only as an identity schema] Identity arrows

Conditional on a typed future Loc member and an inhabited S22/S22a identity-transport law
`etahat_id=id_D`,

~~~text
Loc_N^C etahat_id
 =Loc_N^C id_D
 =Loc_N^C
 =id_C Loc_N^C
 =j_id^C Loc_N^C.                               (F7)
~~~

This is a formal identity schema, not an inhabited physical square, because neither Loc_N^C nor the
S22/S22a physical identity law has a sealed member. For a nonidentity actual-surface isomorphism or
relabeling, the route is F2 and stops at S24/S25. The full F1 quotient result on linear A_iso is a
different equation and supplies no F3 step. The copy model in the Loc-family artifact is a logical
clause-separation model, not an actual-surface member.

### 4.3 [PART-PROVABLE] Reciprocal-loop generator

Let u:N->M be the actual rank-preserving reciprocal generator. The maximum sealed kernel equality
is

~~~text
eta_u^K(Kernbar_N^cyc H)
 =Kernbar_M^cyc(j_u^prof H).                    (F8)
~~~

A future source package would form

~~~text
K_N^D(H)
 :=iota_N^Q408 Kernbar_N^cyc(H)
 in D_N^Loc,

K_M^D(j_u^prof H)
 :=iota_M^Q408 Kernbar_M^cyc(j_u^prof H)
 in D_M^Loc.                                    (F9)
~~~

The physical lift stops before F3:

~~~text
etahat_u K_N^D(H)
 ?=iota_M^Q408 eta_u^K(Kernbar_N^cyc H)
 =iota_M^Q408 Kernbar_M^cyc(j_u^prof H)
 =K_M^D(j_u^prof H).                            (F10)
~~~

The question mark is the uninhabited S23 source-embedding/transport square. Even after granting
F10, the physical Loc display is

~~~text
Loc_M^C etahat_u
 =iota_M^H Loc_M^phys etahat_u
 ?=iota_M^H j_u^Sym Loc_N^phys
 ?=j_u^C iota_N^H Loc_N^phys
 =j_u^C Loc_N^C.                                (F11)
~~~

The question marks are S24 and S25.

Even on the older finite declaration, the exact missing equality is visible:

~~~text
Loc_M^fin eta_u^K(K)
 =sigma_M^fin(eta_u^K K)
 ?=j_u^C sigma_N^fin(K)
 =j_u^C Loc_N^fin(K).                           (LOC-RL)
~~~

No counterexample is exhibited. Reciprocal F3 is unestablished, not refuted.

### 4.4 [PART-PROVABLE] Nontrivial q=2 Ref_path generator

For r_nm:n->m, sealed stock gives the two child paths, P_nm=id on the relevant current
restriction, the current/Riesz square, and two differently typed transport statements:

~~~text
eta_nm^K(Kernbar_n^cyc H)
 =Kernbar_m^cyc(j_nm^prof H),

eta_nm^K(Kernbar_n H)
 =Kernbar_m(j_nm^H H),                          (F12)

Kern_m^fin(j_nm^H H)[P_nm a_1,P_nm a_2]
 =Kern_n^fin(H)[a_1,a_2].                       (F13)
~~~

The first line is the represented cycle-profile statement; the second and F13 are the finite
Hodge-input statements. They cannot be hybridized by replacing j_nm^prof with j_nm^H inside
Kernbar_m^cyc. The finite/cochain route stops at

~~~text
Loc_m^fin eta_nm^K(Kernbar_n H)
 =sigma_m^fin(Kernbar_m(j_nm^H H))
 ?=j_nm^C sigma_n^fin(Kernbar_n H)
 =j_nm^C Loc_n^fin(Kernbar_n H).                (LOC-RF)
~~~

The physical route repeats the S23 stop in F10 and the S24/S25 stops in F11 with u replaced by
r_nm. Projector naturality F5 acts only after a cochain has been produced. Therefore neither the
reciprocal nor the q=2 generator supplies a physical base case.

### 4.5 [PART-PROVABLE] Cycle-creating old-image scope

For a cycle-creating arrow a_cc:N->M, full forward F3 on the target-new-cycle complement is not the
lawful contract. A future member may satisfy the downward old-image squares

~~~text
rho_a^Sym Loc_M^phys|_(D_M^old)
 =Loc_N^phys rho_a^D,

rho_a^C iota_M^H|_(Sym_M^old)
 =iota_N^H rho_a^Sym.                           (F14)
~~~

Only under F14 does the cochain display close:

~~~text
rho_a^C Loc_M^C|_(D_M^old)
 =rho_a^C iota_M^H Loc_M^phys|_(D_M^old)
 =iota_N^H rho_a^Sym Loc_M^phys|_(D_M^old)
 =iota_N^H Loc_N^phys rho_a^D
 =Loc_N^C rho_a^D.                              (F15)
~~~

Both middle equalities and all physical maps are uninstantiated. A6's ratified comparison

~~~text
r_a^Bot pi_Mx,M Loc_M eta_a
 =pi_Mx,N Loc_N                                  (F16)
~~~

is postprojected and bottom-valued. No monicity or section permits cancellation of r_a^Bot,
pi_Mx, or P_H from F16, so F16 does not prove F14 or full F3. No upward lift is assigned to the
new-cycle complement.

### 4.6 [PART-PROVABLE] Common-refinement legs

For a common-refinement relation g_1 f_1=g_2 f_2, represented Eta diamonds are sealed. Physical F3
would propagate along route 1 as

~~~text
Loc_P^C etahat_g1 etahat_f1
 =j_g1^C Loc_M^C etahat_f1
 =j_g1^C j_f1^C Loc_N^C,                       (F17)
~~~

and along route 2 as

~~~text
Loc_P^C etahat_g2 etahat_f2
 =j_g2^C Loc_L^C etahat_f2
 =j_g2^C j_f2^C Loc_N^C.                       (F18)
~~~

Equations F17-F18 consume F3 on each constituent leg. The physical etahat diamond, the physical
Hodge-realization diamond, and the nonidentity leg base cases are uninhabited. If a constituent leg
is cycle-creating, only F15 on the old image is licensed.

### 4.7 Complete actual-arrow status

| I_F generator class | Maximum sealed reach | Physical F3 status and exact block |
|---|---|---|
| identities | formal equation F7 | conditional identity only; Loc member and S22/S22a identity transport uninhabited |
| nonidentity A_iso actual-surface isomorphism/relabeling/reality/orientation/frame/gauge | quotient covariance and finite data | F2 stops on S24/S25; finite C3 pullback has wrong type and variance |
| W3/DoR-008 restrictions | represented kernel transport; Hodge projector on certified RP scope | no response-to-physical-Loc-to-cochain bridge; non-RP members may also lack etahat_f |
| reciprocal A_RP | F8 | F10 stops on S23; F11/LOC-RL stop on S24/S25 |
| q=2 Ref_path A_RP | F12-F13 | LOC-RF and the physical S23/S24/S25 chain stop |
| A_CC cycle-creating | finite old-image bottom law F16 | only conditional downward F14-F15; full new-cycle F3 is outside scope |
| A_CR disjoint/contact common refinements | represented diamonds | conditional propagation F17-F18 has no physical leg base |
| clause-(vi)-only consumer arrows | their sealed consumer-specific bottom legs | generally unformed: no package-wide etahat_f, j_f^Sym, or cochain transport |

An arrow overlapping several rows inherits every applicable restriction; no class is deleted to
make F3 appear total. In particular, clause (vi) from GUARD prevents replacing the actual category
by only A_iso union A_RP union A_CC union A_CR when consumer-only arrows remain.

### 4.8 [PROVABLE as a fully stated conditional theorem] Composition and induction

The word argument has a separate transport-functor antecedent. Let an inhabited S22/S22a package
give

~~~text
etahat_id=id_D,
etahat_(g compose f)=etahat_g compose etahat_f,

j_id^C=id_C,
j_(g compose f)^C=j_g^C compose j_f^C,           (F19a)
~~~

on words made entirely of rank-preserving legs for which full covariant F3 is the contract. The
`j^C` equations are the sealed cochain functor laws; the `etahat` equations are uninhabited
S22/S22a data. If, in addition, physical F3 is proved for
f:N->M and g:M->P, then

~~~text
Loc_P^C etahat_(g compose f)
 =Loc_P^C etahat_g etahat_f
 =j_g^C Loc_M^C etahat_f
 =j_g^C j_f^C Loc_N^C
 =j_(g compose f)^C Loc_N^C.                    (F19)
~~~

For a word F_k=f_k...f_1 whose generators each have physical F3, the base and induction step would
be

~~~text
Loc_N1^C etahat_F1
 =Loc_N1^C etahat_f1
 =j_f1^C Loc_N0^C
 =j_F1^C Loc_N0^C,                              (F20)

Loc_N(k+1)^C etahat_F(k+1)
 =Loc_N(k+1)^C etahat_f(k+1) etahat_Fk
 =j_f(k+1)^C Loc_Nk^C etahat_Fk
 =j_f(k+1)^C j_Fk^C Loc_N0^C
 =j_F(k+1)^C Loc_N0^C.                          (F21)
~~~

F20 cannot start on the reciprocal or q=2 generator, or on any other actual nonidentity class in
the table. Thus F19-F21 prove closure only conditional on an inhabited S22/S22a transport functor
and physical F3 for every constituent generator; they supply neither datum and prove no base case.
They do not include a cycle-creating leg. Iterating the downward old-image equation F15 would
require a separate contravariant word, reversed order, and typed nested old-image domains; no such
induction package is asserted here.

### 4.9 Statement-versus-proof audit

The corpus contains F3 in at least six files, but its occurrences separate as follows:

1. a bare premise in the J7/J2 display;
2. the finite declaration and failed LOC-RL/LOC-RF attempt in NAT;
3. S24/S25 requirements of a possibly empty future-member family in LOC and its successors;
4. conditional N2/N3 displays;
5. the Gamma-H stopped board;
6. reviews correcting “unstated” to “stated but unproved.”

None is an inhabited proof on an actual nonidentity arrow. The membership theorem's earlier
promotion was killed by its cross-family review and is not consumed here.

~~~text
MACHINERY-APPEAL(S3)
 =inhabited physical Loc/source/Hodge member
  +S23/S24/S25 generator base squares
  +physical common-refinement diamonds
  +typed transports for clause-(vi)-only arrows.
~~~

The structural result is recorded as PARTIAL rather than upgraded from repeated declarations.

## 5. S4 — consequence board for both A8 routes

### 5.1 Common seams after S1-S3

| Common item | Result | What remains |
|---|---|---|
| unit class of Hodge pairing | derived dimensionless by O1-O4 | no conversion coefficient |
| orientation address | signed carrier R_or,[a] and full family Triv_[a] isomorphic to R_(>0) x Sigma_[a] built; O19 is covariant | no sign or scale member selected; target-only new cycles get their own orbit |
| R5/profile relation | Q3-Q7 display corestriction and direction | physical topological embedding remains in ExtSrc |
| quotient descent | automatic under Q12-Q13, displayed in Q14-Q18 | source extension itself uninhabited |
| unaddressed response identity | O_R5,w->O_w^resp is Q9 | addressed Res has no inverse/section |
| addressed response-to-kernel leg | exact type Q20/Q29 | Ker_(a,K), image, support, and factorization uninhabited |
| physical F3 | represented legs and conditional induction retained | no actual nonidentity base square |

The three seams are therefore not declared globally complete. S1 is built as a family; S2 removes
an independent descent axiom but leaves ExtSrc; S3 exposes exact generator-level proof debts.

### 5.2 H route: remaining route-specific core

[YOURS — restatement, no member bound] After the common source and arrow debts, H still needs the
J-II realization member

~~~text
Rlz_N^H
 :=(Loc_N^phys,iota_N^H),

Loc_N^phys:D_N^Loc->Sym_N^loc,
iota_N^H:Sym_N^loc->C_N^k,

Loc_N^C
 :=iota_N^H compose Loc_N^phys.                 (R1)
~~~

It must satisfy the reader-free symbol, Ward/contact, support, linearity, reality, branch, S24/S25,
old-image, and diamond conditions. Only then is the cochain-valued map

~~~text
Gamma_(a,epsilon,K)^H
 :=Loc_N^C compose Ker_(a,K)
 :O_a^resp->C_N^k                               (R2)
~~~

formed. The finite sigma_N^fin datum is not R1. The S1 family supplies the corrected addressed
orientation return after R2 exists; it does not inhabit R1 or Ker. To prevent that family from
silently becoming one scalar map, carry T explicitly. Define, only after R2 is formed,

~~~text
lambda_x:H_N^k->R,
lambda_x(h):=<x,h>_N,

Per_(a,epsilon,K)^H(Y)
 :=lambda_(P_H,N Gamma_(a,epsilon,K)^H(Y))
 in (H_N^k)^*,

B_(a,epsilon,K,T)^H(Y)
 :=u_(a,T)^H(Per_(a,epsilon,K)^H(Y))
 in K_amb,

T in Triv_[a].                                  (R2a)
~~~

Thus Gamma^H and Per^H do not select an orientation trivialization, while the scalar return is the
whole T-indexed family. Address reversal uses O19 memberwise. A single unindexed scalar B^H is not
licensed, and a consumer must either carry all T, prove a sign/scale-invariant quotient, or supply
a separately authorized matching/normalization law.

~~~text
H_ROUTE_SPECIFIC_DEBT
 =one J-II physical realization member Rlz^H
  with its route conditions;

the eventual scalar comparison additionally carries
 T in Triv_[a] or proves an authorized family quotient. (R3)
~~~

### 5.3 HOL route: remaining route-specific core

[YOURS — corrected necessary form, not an amendment] XI-R proves that geometric U(1) holonomy is
sealed on the integral cycle lattice

~~~text
Lambda_N^cyc
 :=ker(B_N^T) intersection Z^(E_N),             (R4)
~~~

while the period functional consumes a connection difference. A corrected correspondence must
therefore choose, through an authorized gate rather than here, between two honestly typed forms:

~~~text
(A) Xi_N^int:X_N^int->Lambda_N^cyc,
    where X_N^int is a non-vector/discrete or factored domain
    and the changed regularity, additivity, and bridge
    D_N^Loc->X_N^int are stated;

(B) Xi_N^R:D_N^Loc->K_N^(cyc,R)
    continuous and R-linear,
    together with a separately authored integral/reference/log lift
    on every argument sent to geometric holonomy.               (R5)
~~~

A nonconstant continuous additive map from the connected real vector carrier D_N^Loc to the
discrete lattice Lambda_N^cyc cannot serve as the missing bridge: its image is connected and hence
is `{0}`. Form (A) must therefore change the domain or regularity honestly; form (B) must add the
integral/reference lift. Merely calling Xi nonlinear does not close the seam.

For an alleged connection pair A_0,A_1 on the same admitted bundle, and only when the chosen R5
form produces an integral cycle z_N(k), the lawful relative composite would be

~~~text
Theta_(A1,A0;N)(k)
 :=Hol_(A1)(z_N(k))
    Hol_(A0)(z_N(k))^(-1)

 =exp(i u_(z_N(k))(A_1-A_0)).                   (R6)
~~~

Equation R6 is conditional on a correctly typed R5 member, an integral image, and a retained
same-bundle connection pair. No connection, reference, lift, or Xi member is selected here.

The HOL scalar leg remains a retained candidate family, not one unindexed map:

~~~text
S=(U_b^S,log_b^S,U_a^S)
 in Scal_[a;A1,A0,N]^Hol,

im(Theta_(A1,A0;N) compose Ker_(a,K))
 subset U_b^S subset U(1),

log_b^S:U_b^S->R,

U_(a,epsilon;A1,A0,N,S)^Hol:R->K_amb,

u_(a,epsilon;A1,A0,N,S)^Hol
 :=U_(a,epsilon;A1,A0,N,S)^Hol
   compose log_b^S,

B_(a,epsilon,K,S;A1,A0)^Hol(Y)
 :=u_(a,epsilon;A1,A0,N,S)^Hol(
     Theta_(A1,A0;N)(Ker_(a,K)(Y))).             (R7)
~~~

S1 does not build R7: R7 still needs a response-independent arc/image proof, log branch,
normalization, address covariance, and A7_HOL_BRANCH_COMPAT, all carried with `(S,A1,A0,N)`. Its
source being R does not turn an unbuilt route map into an identity. An absolute holonomy formula
would additionally require a selected or retained reference A0 with the required neutrality;
none is supplied.

~~~text
HOL_ROUTE_SPECIFIC_DEBT
 =one authorized R5 alternative and its member
  +retained same-bundle connection-pair/reference family
  +integral-image or integral/reference-lift certificate
  +an inhabited retained Scal^Hol family with its
   (S,A1,A0,N)-indexed arc/log/image/A7 certificates. (R8)
~~~

No route is chosen, and both A7 branches remain carried.

### 5.4 What the A8 identification falsifier can bite on

A8 is already law. Both scalarized outputs in R2a and R7 land in the same K_amb, so no optional
matching relation may prefilter the falsifier. For every pair of alleged route members formed on
the same physical cell, the required comparison is

~~~text
B_(a,epsilon,K,T_H)^H(Y)
 =B_(a,epsilon,K,S_Hol;A1,A0)^Hol(Y)

for every
(a,epsilon,K,Y,T_H,S_Hol,A1,A0)
such that
T_H in Triv_[a],
S_Hol in Scal_[a;A1,A0,N]^Hol,
and both route outputs are formed on the same
(a,epsilon,K,Y,A1,A0) physical cell;

one displayed disagreement on one common formed cell
voids the disagreeing construction(s) pending adjudication. (R9)
~~~

An empty, output-dependent, or agreement-filtered `Match` relation would make A8 vacuous and is
forbidden. Carrying T_H and S_Hol universally does not bind either member; it retains the two
families and exposes every jointly formed candidate pair to the law. Dropping T_H or S_Hol would
select or suppress a scalarization member; dropping `(A1,A0)` would select or suppress the HOL
affine reference. None is permitted. A comparison made before scalarization would instead require
a separately exhibited common carrier; none is sealed.

The falsifier does not wait for a fixed point, threshold, witness certification, or end test. Its
execution premise is exactly: both route contracts supply typed period outputs on one common cell
and state their common comparison carrier.

At present,

~~~text
Gamma^H is unformed because ExtSrc, Ker, and Rlz^H
have no member;

Theta^Hol is unformed because neither R5 alternative has an
adopted and inhabited member, integral-image/lift certificate,
and inhabited retained connection-pair/reference family;

the HOL scalar comparison is additionally unformed
because R7 has no member.                        (R10)
~~~

Therefore no actual A8 equality or disagreement is evaluated in this artifact. The new
orientation family already supplies a common address/reversal test, but failure of O19 is a route
covariance falsifier, not evidence of H/HOL disagreement. No value is imported from one route to
fill the other.

## 6. S5 — battery

### 6.1 F_PLDEC and false-anchor audit

The permitted construction order is

~~~text
sealed metric + primitive orientation orbit
 ->addressed orientation line
 ->full nonzero-trivialization family;

raw R5 source + quotient relation
 ->corestriction display
 ->future independent source extension;

represented kernel + independently constructed physical symbol/Hodge maps
 ->future F3 base squares
 ->conditional word/diamond closure.             (B1)
~~~

The prohibited order is

~~~text
reader, chi, response value, threshold, fixed point,
end test, desired sign, or desired coupling
 ->mu, source extension, Loc, Xi, U^Hol, or F3.  (B2)
~~~

No reader or false-anchor equality appears in O1-O21, Q1-Q30, or F1-F21. In particular,

~~~text
pi_Mx Loc Kernbar Q =1
~~~

is not consumed as a definition, normalization, existence theorem, or naturality premise.

~~~text
F_PLDEC = CLEAN.
~~~

### 6.2 Anti-tuning ledger

| Hazard | Control | Result |
|---|---|---|
| choose which address receives + or choose its scale | all of Triv_[a] isomorphic to R_(>0) x Sigma_[a] retained in O14-O17 | clean |
| set an orientation map to zero to make covariance easy | zero is excluded only by the declared trivialization/isomorphism type O14; no metric normalization is claimed | clean |
| add a dimensionful conversion | O1-O4 derive class 1; no dimensionful conversion coefficient introduced; r_T remains an explicit dimensionless family coordinate | clean |
| call O_prof a proved physical subspace | topology boundary after Q7 retained | clean |
| infer source extension from quotient descent | Q12 is explicitly a future member | clean |
| invert addressed Res | Q11 and Q30 retain the one-way boundary | clean |
| call finite sigma a physical Loc map | T4 and F6 keep the types separate | clean |
| count repeated F3 statements as proofs | section 4.9 classifies every occurrence | clean |
| infer F3 from P_H naturality | F5 is used only after cochain formation | clean |
| use A6 bottom equality to cancel into F3 | F16 records absent monicity/section | clean |
| omit clause-(vi) consumer arrows | section 4.7 retains the residual class | clean |
| lift an old-image sign or Loc law to a new cycle | O21a and F14-F16 prohibit it | clean |
| use A8 as an identification premise | R9-R10 retain it only as a falsifier | clean |
| prefilter A8 with an empty or agreement-dependent matching relation | R9 quantifies over every jointly formed `(T_H,S_Hol)` pair | clean |
| choose H or HOL | R3 and R8 remain parallel | clean |
| evaluate a magnitude, coupling, constant, fixed point, or end test | none executed | clean |

### 6.3 Self verb audit

| Verb/status | Display that licenses it |
|---|---|
| verified | preflight hash, sidecar, line count, register, and no-clobber checks |
| derived/dissolved | full unit chain O1-O4 |
| built as a family | typed quotient line and evaluation O11-O13, full retained family O14-O17, and covariance O18-O21 |
| corestriction displayed | Q1-Q7, without topological overclaim |
| automatic descent | conditional implication Q12-Q18; never used to claim S_N exists |
| uninhabited | exact missing package Q19-Q30, not an emptiness proof |
| proved represented transport | F3/F8/F12-F13 on their exact carriers |
| partial F3 | every nonidentity question mark and arrow-class block appears in sections 4.3-4.8 |
| conditional induction | inhabited S22/S22a and constituent physical F3 antecedents are explicit in F19a before F19-F21 |
| route debt restated | exact types R1-R8, T_H/S_Hol family indexing, and affine reference indexing; no adoption or inhabitance claim |
| falsifier can bite | scoped by R9 to common formed cells; R10 denies a current execution |
| clean | matched to B1-B2 and the anti-tuning ledger |

No operative verb is stronger than the display above it.

~~~text
MACHINERY-APPEAL
 =ExtSrc inhabitance and addressed Ker image
  +physical Rlz^H member
  +S22/S22a transport functor and nonidentity S23/S24/S25
   base squares and physical diamonds
  +one corrected Xi_N alternative, integral/reference lift,
   retained connection-pair family, and HOL scalar seam.

The fenced items block inhabitance, not the structural
orientation and corestriction results recorded above.
~~~

ORIENTATION_ADDRESSES = BUILT (+for every primitive orbit [a], R_or,[a] and the whole family Triv_[a] isomorphic to R_(>0) x Sigma_[a]; mu_T(a^-)=-mu_T(a); no sign or scale member selected; rank-preserving and old-image scope only)
CORESTRICTION = DISPLAYED
F3_NONIDENTITY = PARTIAL (+represented Q-408 transport and composition conditional on inhabited S22/S22a plus constituent F3 proved; reciprocal LOC-RL and q=2 LOC-RF unproved; physical S22/S22a/S23/S24/S25 uninstantiated; no actual nonidentity F3 base square)
ROUTE_DEBTS = restated
VERB_AUDIT_SELF = CLEAN
