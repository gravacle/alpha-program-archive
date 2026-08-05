# STAGE 8 TASK 5 — RE-REVIEW OF XI_N V002: THE TOPOLOGICAL-CHARGE TYPING

Lane: CODEX LANE 3 (SOL, HIGH EFFORT)  
Version: V001  
Date: 2026-08-05  
Custody: cross-family re-review; adoption ruling follows  
Scope: symbolic determination only

## 0. Preflight and lead verdict

[PROVABLE — no clobber] Before this review began, the requested artifact and its seal were absent
from both the Lane-3 cleanroom and the archive workspace.

[PROVABLE — register] Before any review work, the supervision register ended at Q-510 before its
usage instructions.

[PROVABLE — input] The candidate, its sidecar, the V001 review standard, and the common-seams
artifact were verified before reading:

```text
STAGE8_TASK5_XI_N_CANDIDATE_DARIO_V002.md
 lines   = 420
 SHA-256 = 7958b54d9964f387750f70a52bcaf869dded9fbe3df5e6c14a53255e94ca18c4
 sidecar = OK
 mirror  = byte-identical

STAGE8_TASK5_XI_N_REVIEW_AND_DISPLAYS_LANE3_V001.md
 lines   = 675
 SHA-256 = c9b62076cc07951ec26fcf4aa4c15e21ec973f6089fb83ca476a98b83aefd071
 sidecar = OK

STAGE8_TASK5_COMMON_SEAMS_LANE3_V001.md
 lines   = 1592
 SHA-256 = 5de94e16db09b982f85fdf117281af62df6ab0d05c9e7577ac258d47594b69b7
 sidecar = OK
 mirror  = byte-identical.
```

[YOURS — determination] The redraft genuinely fixes the two V001 type kills and consumes the
relative integral-cycle holonomy correctly. It is nevertheless **DEFECTIVE** at adoption strength:

```text
old connectedness horn       = evaded by dropping continuity/global additivity;
old real-ray horn            = evaded by dropping degree-one homogeneity;
third horn                   = found: every nonzero scale-invariant member
                               is discontinuous at zero;
physical signed-scale test   = conditional failure: t=-1 makes Xi even, but
                               collapse requires the still-unbuilt G5 action to
                               identify source reversal with x |-> -x;
winding class                = typed, but V001's linear winding proof is
                               inapplicable to the new zero-homogeneous type;
relative holonomy            = correctly consumed;
D-side units                 = mistyped by transfer from the cochain carrier;
rank-preserving transport    = placeholder rather than the exact tau_f^Loc square;
cycle-creating transport     = wrong seal claim and incomplete old-image typing;
A7 repayment                 = not an obligation at all: the written biconditional
                               is a tautology and imposes no neutrality;
U^Hol                        = route-neutral orientation carrier available and a bare
                               T-indexed candidate exhibited; no HOL member inhabited.
```

The gates remain

```text
alpha_computed = false;
proof_authorized = false;
kappa_record_computed = false;
member_bound = false;
fixed_point_executed = false;
end_test_executed = false;
numeric_evaluation = false;
measured_constant_comparison = none.
```

## 1. Authority and type board

### 1.1 Controlling objects

The sealed authority ledger used by the displays is

| Key | Authority | SHA-256 |
|---|---|---|
| `XI-V2` | `STAGE8_TASK5_XI_N_CANDIDATE_DARIO_V002.md` | `7958b54d9964f387750f70a52bcaf869dded9fbe3df5e6c14a53255e94ca18c4` |
| `XI-R` | `STAGE8_TASK5_XI_N_REVIEW_AND_DISPLAYS_LANE3_V001.md` | `c9b62076cc07951ec26fcf4aa4c15e21ec973f6089fb83ca476a98b83aefd071` |
| `COMMON` | `STAGE8_TASK5_COMMON_SEAMS_LANE3_V001.md` | `5de94e16db09b982f85fdf117281af62df6ab0d05c9e7577ac258d47594b69b7` |
| `FIELD` | `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md` | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` |
| `A1` | `DOR_020_A1_WHERE_CLAUSES_AMENDMENT_2026-08-04.md` | `c4dc5976d7e65fe8a6597870629e64cabe6a031b95de97f5572bb36379abb588` |
| `A7` | `DOR_020_A7_EC_BRANCH_CARRIED_2026-08-05.md` | `834e46029a292122c1e4c604af4f3e3249e6a9ee2638255464685623fba5eb8f` |
| `A8` | `DOR_020_A8_GAMMA_BOTH_ROUTES_2026-08-05.md` | `0ee6c897055f803b31bc570b9f4ef852ccb3c4aba21fcd5274a7d740c8eb601d` |

The first three hashes and their sidecars were checked directly in preflight. The remaining hashes
were checked directly before their reality/branch/falsifier content was used.

### 1.2 Frozen types

The distinctions used throughout are

```text
K_N^(cyc,R)
 :=ker(B_N^T:R^(E_N)->R^(V_N)),

Lambda_N^cyc
 :=K_N^(cyc,R) intersection Z^(E_N),

D_N^Loc                                      future ExtSrc image carrier;

Xi_N:D_N^Loc->Lambda_N^cyc                  proposed set map;

u_z:T_A Conn(P_N)->R                        sealed tangent/current functional;

Theta_N^rel(x;A_1,A_0)
 :=Hol_(A_1)(Xi_N(x)) Hol_(A_0)(Xi_N(x))^(-1),

A_0,A_1 in Conn(P_N)                        retained ordered pair on the
                                            same admitted bundle.       (T1)
```

`D_N^Loc`, `Ker_(a,K)`, and their physical transports have exact candidate types in COMMON but no
sealed member. `Lambda_N^cyc` is a torsion-free discrete abelian group because it is a subgroup of
`Z^(E_N)`. No singular connection, Xi member, support bridge, transport, logarithm chart, or scalar
normalization is selected here.

### 1.3 Determination tags

This review uses:

```text
PROVABLE      = established by displayed sealed or elementary structure;
PART-PROVABLE = a displayed implication with an uninhabited premise;
YOURS         = review determination or proposed correction;
PASS          = adoptable as a candidate clause at its stated conditional scope;
KILL          = not adoptable as written.                              (T2)
```

## 2. Q1 — corrected type and the three horns

### 2.1 [PROVABLE] The two V001 kills rerun

Let `D:=D_N^Loc` and `Lambda:=Lambda_N^cyc`.

For a continuous additive homomorphism,

```text
Xi:(D,+)->(Lambda,+),

D connected
 =>Xi(D) connected;

Lambda discrete
 =>Xi(D) is one point;

Xi(0)=0
 =>Xi(D)={0}.                                    (H1)
```

For an R-linear map into the real cycle space whose image is integral, fix x and write

```text
Xi(t x)=t Xi(x) in Lambda for every t in R.

{t Xi(x):t in R} is connected and contained in discrete Lambda,
so {t Xi(x):t in R}={0},
hence Xi(x)=0.                                   (H2)
```

V002 does not satisfy either antecedent. It claims no continuity, no global additivity, and no
degree-one homogeneity. Its ray law instead says `Xi(t x)=Xi(x)` for nonzero t. Therefore H1-H2 do
not kill the bare set-theoretic type.

### 2.2 [PROVABLE] A nonzero bare model exists

On a symbolic finite coordinate-support carrier let `z_i` be integral cycles and define

```text
D=R^m,

Xi(x_1,...,x_m)
 :=sum_(i:x_i !=0) z_i,

supp(x):={i:x_i !=0}.                            (H3)
```

Then, for every nonzero scalar t,

```text
supp(t x)=supp(x),
Xi(t x)=Xi(x).                                   (H4)
```

If x and y have disjoint coordinate supports,

```text
Xi(x+y)
 =sum_(i in supp(x) union supp(y)) z_i
 =Xi(x)+Xi(y).                                   (H5)
```

Thus the new axioms are algebraically consistent and genuinely evade H1-H2. This model does not
establish their physical correctness, continuity, covariance, or inhabitance on the actual surface.

### 2.3 [YOURS — determination] What the two laws mean physically

The bare model H3-H5 proves consistency, not the physical interpretation claimed by V002. Positive
rescaling is a plausible threading law only after the actual source carrier has a typed
support-stratum factorization for which

```text
q_D:D_N^Loc->{record-visible support strata},

t>0 =>q_D(t x)=q_D(x)
     =>Xi_N(t x)=Xi_N(x).                         (H6a)
```

No sealed member of that factorization is displayed in V002. Thus positive-scale invariance is a
coherent **YOURS** candidate, not verified physics.

Physical orientation reversal is a separate D-side action, not automatically scalar multiplication
by `-1`. V002's all-real scalar law gives

```text
Xi_N(-x)=Xi_N(x).                                 (H7)
```

The target identities

```text
J_(-z)=-J_z,
Hol_A(-z)=Hol_A(z)^(-1),
CTP/orientation reality sends z to -z              (H8)
```

prove that the **cycle** action is odd. They do not prove that the source action satisfies
`u_D(x)=-x`: a kernel/profile may transform by a distinct address involution, and a bilocal kernel
may reverse two current signs. The exact conditional test is therefore

```text
u_D|_S=-id_S and u_Lambda|_(Xi(S))=-id
 =>Xi_N(-x)=Xi_N(u_D x)
             =u_Lambda Xi_N(x)
             =-Xi_N(x)                            (H6b)
```

on an admitted signed sector `S`. H7 plus H6b forces zero there because the lattice is torsion-free.
If G5 does not inhabit H6b, there is no scalar-sign contradiction: an independent address reversal
`r_N^D` may obey `Xi_N(r_N^D x)=-Xi_N(x)` while H7 remains true. Hence all-real scale invariance is
**conditionally incompatible** with an admitted sign-odd sector, while the relation between physical
reversal and scalar negation is **UNDETERMINED pending G5**. If the intended target discards sign,
it must instead be an unoriented quotient such as primitive-cycle orbits modulo `z~-z`; that quotient
is not directly consumable by `Hol_A` without a new orientation lift.

Disjoint-support additivity is likewise a plausible authored independence law:

```text
supp_D(x) disjoint supp_D(y)
 =>Xi(x+y)=Xi(x)+Xi(y).                          (H9)
```

It is not runnable on the actual carrier until a D-side support map or binary disjointness relation
is typed. That is a subdatum of the future ExtSrc/support package, not logically the full G4
D-side/cycle-side comparison: G4 is additionally needed by Y9 to compare `supp_D(x)` with
`supp_Lambda(Xi_N(x))`. V002 must split those debts (or enlarge and restate G4). H9 says nothing
about overlapping supports. Its status is **PART-PROVABLE / YOURS**, not a sealed physical theorem.

### 2.4 [PROVABLE] The third horn: continuity at zero is impossible

Assume one nonzero value exists:

```text
Xi(x_0)=z !=0.
```

For any positive sequence `t_n->0`, V002 scale invariance gives

```text
t_n x_0->0 in D,

Xi(t_n x_0)=Xi(x_0)=z !=0=Xi(0).                (H10)
```

Hence Xi is discontinuous at zero. More strongly, if x and y have disjoint supports and
`Xi(y)=z !=0`, then

```text
x+t_n y->x,

Xi(x+t_n y)
 =Xi(x)+Xi(t_n y)
 =Xi(x)+z
 !=Xi(x).                                       (H11)
```

Thus, whenever the typed D-side disjointness premise and such a nonzero `y` are inhabited,
discontinuity occurs at the corresponding support-birth boundary. H3 supplies an explicit algebraic
model with such boundaries, so Y2 does not imply “locally constant away from 0” in the ambient
topology. The new type may instead be constant within a fixed-support stratum. Independently of any
support predicate, H10 proves that a nonzero member cannot retain continuity at zero. This is the
requested third horn; it is a precise tradeoff, not by itself a contradiction with Y1 because Y1
explicitly drops continuity.

### 2.5 Q1 verdict

```text
Y1 integral set-map type             = PASS as a conditional family specification;
Y2 positive-scale component          = COHERENT YOURS candidate, physical factorization unbuilt;
Y2 all-real scale invariance          = CONDITIONAL KILL on an H6b sign-odd sector;
physical reversal = scalar negation  = UNDETERMINED pending G5;
Y2 disjoint-support additivity        = PART-PROVABLE, needs typed D-side support;
old connectedness horn                = evaded;
old real-ray horn                     = evaded;
third continuity-at-zero horn         = FOUND;
ambient local-constancy claim         = REFUTED.                  (H12)
```

## 3. Q2 — the eleven clauses against the relative display

### 3.1 Clause-by-clause PASS/KILL board

| Clause | Verdict | Exact review |
|---|---|---|
| `(Y1)` integral type | **PASS AS CONDITIONAL SPEC** | `Xi_N:D_N^Loc->Lambda_N^cyc` fixes V001's real/integral collision. It must be indexed over an alleged ExtSrc member; it inhabits neither `D_N^Loc` nor Xi. |
| `(Y2)` replacement law | **DEFECTIVE AS WRITTEN** | Positive-scale invariance is a coherent YOURS candidate, but its physical support-stratum factorization is unbuilt. All-real invariance collapses a nonzero member only conditionally on G5 inhabiting the H6b sign-odd source action; absent that, the physical sign action is undetermined. Disjoint-support additivity needs an uninhabited D-side support relation (not the whole cross-carrier G4), and “locally constant away from 0” is false. |
| `(Y3)` relative consumption | **PASS WITH SCOPE** | It is exactly the D1-5 relative formula for an integral image and an ordered same-bundle pair `(A_1,A_0)`. No absolute connection functional or reference selection occurs. |
| `(Y4)` winding | **PASS FOR THE CLASS; KILL FOR ITS PROOF OF G2** | The class in `R/2piZ` and the need to gate a real logarithm are correct. The reused V001 factor-line winding proof assumes linear Xi and is invalid under Y2. |
| `(Y5)` units | **KILL** | COMMON O1-O4 proves a Hodge pairing on `C_N^k` dimensionless; Xi consumes raw `D_N^Loc`. No displayed map transports that unit conclusion backward to the D-side carrier. |
| `(Y6)` integrality separation | **KILL AS WORDED / bounded repair** | Units and integrality are correctly separated, but integrality is imposed by Y1's codomain; Y2 does not supply or derive it. |
| `(Y7)` rank-preserving transport | **KILL AS DISPLAYED / gated repair** | “D-side transport of f” is not a map. COMMON supplies the exact future type `tau_f^Loc`; XI-R supplies the integral cycle map. The required square is displayed below and remains uninhabited. |
| `(Y8)` cycle creation | **KILL** | The draft falsely calls `rho_f^D` sealed and does not type a `D^Loc` old-image map or the old-cycle image premise. COMMON Q19c makes `rho_f^Loc` a future member. |
| `(Y9)` support | **NOT ADOPTABLE BEFORE G4** | The draft honestly calls it unrunnable, but an untyped predicate is not yet a live law or failure-capable void. |
| `(Y10)` covariance/no selection | **GATED / PASS for no-selection** | `u_D` is G5 and the connection pair must transform simultaneously. If G5 inhabits H6b, covariance exposes Y2's `t=-1` collapse; without that source-action identification the sign arm is unformed, not refuted. Family retention is correct. |
| `(Y11)` independence | **PASS** | The reader-, response-consequence-, threshold-, fixed-point-, and end-test-free condition is clean and establishes no inhabitance. |

Only Y1 at conditional scope, Y3, the class-valued half of Y4, the no-selection half of Y10, and
Y11 pass without a load-bearing repair.

### 3.2 [PROVABLE] Relative holonomy is consumed exactly

For `z=Xi_N(x) in Lambda_N^cyc` and a retained ordered pair on the same admitted bundle,

```text
Theta_N^rel(x;A_1,A_0)
 :=Hol_(A_1)(z) Hol_(A_0)(z)^(-1)

 =product_e h_e(A_1)^(z_e)
   product_e h_e(A_0)^(-z_e)

 =product_e (h_e(A_1)h_e(A_0)^(-1))^(z_e)

 =exp(i sum_e z_e integral_(gamma_e)(A_1-A_0))

 =exp(i u_z(A_1-A_0)).                          (R1)
```

This is D1-5, not the killed absolute formula. Integer exponents are used; no cycle basis, reference
connection, or gauge representative is selected. Ordered-pair indexing must remain explicit in
every consumer.

### 3.3 [PROVABLE] The winding class is typed; the copied winding proof is not

For an integral branch shift `n in Z^(E_N)`, the lifted real period changes by

```text
u_z(A_1-A_0)
 maps_to
u_z(A_1-A_0)+2 pi <z,n>,

z,n integral
 =><z,n> in Z.

[u_z(A_1-A_0)]
 in R/(2 pi Z)                                  (R2)
```

is therefore the class seen by the character. A real logarithm needs more than the phrase
“certified chart”:

```text
S=(U_b^S,log_b^S,U_a^S)
 in Scal_[a;A1,A0,N]^Hol,

im(Theta_N^rel compose Ker_(a,K)) subset U_b^S,
U_b^S subset U(1) open proper logarithm chart,
log_b^S:U_b^S->R continuous and single-valued,
exp(i log_b^S(g))=g for every g in U_b^S,
1_(U(1)) in U_b^S,
log_b^S(1_(U(1)))=0,

plus response independence, address/reality covariance,
normalization, and A7_HOL_BRANCH_COMPAT.         (R3)
```

G2 is genuine because no whole-image containment or R3 member is sealed. V002's inherited proof of
that gate, however, uses a premise it has just rejected. Put

```text
k:=Ker_(a,K)(Rhat_(Kcycle,a)),
p:=u_(Xi_N(k))(A_1-A_0).
```

For nonzero t, linearity of Ker and **zero-homogeneity** of Xi give

```text
Xi_N(Ker_(a,K)(t Rhat))
 =Xi_N(t k)
 =Xi_N(k),

Theta_N^rel(Ker_(a,K)(t Rhat);A_1,A_0)
 =exp(i p),                                     (R4)
```

not `exp(i t p)`. At t=0 the value is `exp(i u_0)=1`. Therefore the V001 full-line winding attack
does not apply to V002. Different support strata or rays may still send the whole route image
outside every single chart; absent a whole-image certificate, G2 remains open on that independent
basis.

### 3.4 [PROVABLE / YOURS] Units and integrality separated without crossing carriers

COMMON O1-O4 establishes

```text
x,h in C_N^k
 =>[<x,h>_N]=1.                                  (R5)
```

It does not establish

```text
x in D_N^Loc
 =>[x]=1.                                        (R6-KILLED)
```

The phase in R1 is dimensionless for a different, direct reason: the U(1) edge relation has

```text
h_e(A_1)h_e(A_0)^(-1)
 =exp(i integral_(gamma_e)(A_1-A_0)),            (R7)
```

so its exponent and the integral sum paired with integral z have phase class 1. Thus “no
phase-unit conversion is needed” is re-derivable, but Y5's statement that the raw D-side Xi input is
dimensionless does not follow. Integrality is the authored codomain condition in Y1:

```text
Xi_N(x) in Lambda_N^cyc.                         (R8)
```

It is neither a unit consequence nor supplied by the compatibility law Y2.

### 3.5 [PART-PROVABLE] Exact rank-preserving repair

For a rank-preserving f:N->M, XI-R gives the integral cycle transport and COMMON Q19a' gives the
future D-side map:

```text
S_f^Lambda
 :=S_f|_(Lambda_N^cyc)
 :Lambda_N^cyc->Lambda_M^cyc,

tau_f^Loc:D_N^Loc->D_M^Loc.                     (R9)
```

The candidate naturality square must be

```text
Xi_M tau_f^Loc
 =S_f^Lambda Xi_N.                              (R10)
```

Under R10 and `A_0,A_1 in Conn(P_M)`, every relative equality is

```text
Theta_N^rel(x;eta_conn,f(A_1),eta_conn,f(A_0))
 =Hol_(eta_conn,f(A_1))(Xi_N x)
   Hol_(eta_conn,f(A_0))(Xi_N x)^(-1)

 =Hol_(A_1)(S_f^Lambda Xi_N x)
   Hol_(A_0)(S_f^Lambda Xi_N x)^(-1)

 =Hol_(A_1)(Xi_M tau_f^Loc x)
   Hol_(A_0)(Xi_M tau_f^Loc x)^(-1)

 =Theta_M^rel(tau_f^Loc x;A_1,A_0).             (R11)
```

R10-R11 are the display Y7 needs. `tau_f^Loc` is an uninhabited ExtSrc member, so the result is a
gated condition, not a proved square.

### 3.6 [PART-PROVABLE] Exact cycle-creating repair

For a cycle-creating f:N->M, one unquestionably lawful old-image typing is

```text
S_f^Lambda
 :=S_f|_(Lambda_N^cyc)
 :Lambda_N^cyc->Lambda_M^cyc
 integral and injective on the admitted old-current image,

Lambda_M^(cyc,old)
 :=S_f^Lambda(Lambda_N^cyc),

r_f^(Lambda,old)
 :=(S_f^Lambda)^(-1)
 :Lambda_M^(cyc,old)->Lambda_N^cyc,

rho_f^Loc:D_M^(Loc,old)->D_N^Loc,                (R12)
```

with the image premise and downward square

```text
Xi_M(D_M^(Loc,old)) subset Lambda_M^(cyc,old),

Xi_N rho_f^Loc
 =r_f^(Lambda,old) Xi_M|_(D_M^(Loc,old)).        (R13)
```

Then, on old image only,

```text
Theta_N^rel(rho_f^Loc y;eta_conn,f(A_1),eta_conn,f(A_0))
 =Hol_(eta_conn,f(A_1))(Xi_N rho_f^Loc y)
   Hol_(eta_conn,f(A_0))(Xi_N rho_f^Loc y)^(-1)

 =Hol_(eta_conn,f(A_1))(r_f^(Lambda,old) Xi_M y)
   Hol_(eta_conn,f(A_0))(r_f^(Lambda,old) Xi_M y)^(-1)

 =Hol_(A_1)(S_f^Lambda r_f^(Lambda,old) Xi_M y)
   Hol_(A_0)(S_f^Lambda r_f^(Lambda,old) Xi_M y)^(-1)

 =Hol_(A_1)(Xi_M y) Hol_(A_0)(Xi_M y)^(-1)

 =Theta_M^rel(y;A_1,A_0).                       (R14)
```

The penultimate equality uses `Xi_M y in Lambda_M^(cyc,old)` from R13 and
`S_f^Lambda r_f^(Lambda,old)=id` there. `S_f^Lambda` is used to name the admitted old-image
sublattice; it is not an upward Xi law. No value or lift is assigned on the target-new-cycle
complement. If a sealed full downward mate
that kills new cycles exists, it is lawful only after its type and equations are displayed; V002
neither names nor derives one. As written,
Y8 uses an ambient `rho_f^D`, calls it sealed contrary to COMMON Q19c, and omits the `D^Loc` and
cycle-image premises. It therefore fails before R14.

## 4. Q3 — U^Hol and the parity rule

### 4.1 [PROVABLE] What COMMON builds and what this review only exhibits

For every primitive address orbit `[a]`, COMMON builds

```text
R_or,[a],
Triv_[a]=Iso_R(R_or,[a],K_amb),

iota_a:R->R_or,[a],
iota_(a^-)=iota_a compose (-id_R).
```

Thus, for every retained `T in Triv_[a]`, this review exhibits the route-neutral bare candidate

```text
U_(a,T)^bare
 :=T compose iota_a
 :R->K_amb,

U_(a^-,T)^bare
 =-U_(a,T)^bare                                 (P1)
```

using the same no-selection carrier family used on H. No sign or positive dimensionless scale is
selected. COMMON O18 builds that carrier and its H-labeled use; COMMON R7 expressly does not build a
HOL scalarization member. P1 therefore exhibits a candidate of the required bare map type. It does
not inhabit G1 or any singular `U^Hol`: that requires inclusion in a complete retained P3 member and
the HOL-specific input/parity equations below.

### 4.2 [PART-PROVABLE] Why the full HOL seam remains open

The H orientation proof also has an exhibited odd input evaluation. V002 does not display the HOL
analogue. To transpose it requires at least

```text
chi_(A_1,A_0)(z)
 :=Hol_(A_1)(z) Hol_(A_0)(z)^(-1),

r_(a,K)^O:O_a^resp->O_(a^-)^resp,
r_a^K:Kpar_N->Kpar_N,
K^-:=r_a^K(K),
r_N^D:D_N^Loc->D_N^Loc,
Y^-:=r_(a,K)^O(Y),

r_N^D compose Ker_(a,K)
 =Ker_(a^-,K^-) compose r_(a,K)^O,

r_N^D(Ker_(a,K)(Y))
 =Ker_(a^-,K^-)(Y^-),

Xi_N(r_N^D x)=-Xi_N(x),

chi_(A_1,A_0)(-z)
 =Hol_(A_1)(-z) Hol_(A_0)(-z)^(-1)
 =Hol_(A_1)(z)^(-1) (Hol_(A_0)(z)^(-1))^(-1)
 =Hol_(A_1)(z)^(-1) Hol_(A_0)(z)
 =(Hol_(A_1)(z) Hol_(A_0)(z)^(-1))^(-1)
 =chi_(A_1,A_0)(z)^(-1),

U_b^(a^-,S)=(U_b^(a,S))^(-1),

log_(a^-,S)(g^(-1))=-log_(a,S)(g)
 for every g in U_b^(a,S),

U_(a^-,T)^Hol=-U_(a,T)^Hol.                     (P2)
```

Here `r_(a,K)^O`, `r_a^K`, and `r_N^D` are required future address-action data, not sealed arrows; if
the eventual action fixes `K`, the displayed premise specializes to `K^-=K`. P1 displays the bare
analogue of the last line; its `U^Hol` instance remains a member condition. The response/kernel
address square and Xi sign equation consume G5 and the uninhabited common
bridge; only if that action also has `r_N^D x=-x` on a sector does the Xi sign equation conflict with
all-real Y2 there. The character-inversion computation is displayed above after a signed cycle is
formed. The chart-inversion and logarithm lines consume G2 and a pair of compatible charts. COMMON itself states
that S1 does not inhabit its full R7 HOL family. Therefore V002's G1-F assertion—address independence
alone forces the HOL return to vanish—is not proved from V002: it lacks the displayed odd-input chain
on which that conclusion depends.

The complete retained HOL member still has the type

```text
S=(U_b^S,log_b^S,U_a^S)
 in Scal_[a;A1,A0,N]^Hol,                       (P3)
```

with whole-image, normalized-log, address/reality, A7, and no-selection certificates. P1 is
necessary but not sufficient for P3.

### 4.3 Q3 verdict

```text
parity rule, sound form
 =COMMON's route-neutral carrier is available to both routes, and P1 exhibits
  the bare candidate form without inhabiting a HOL member;

unsound stronger form
 =every H-specific discharge automatically proves the HOL log/phase seam;

U^Hol status
 =RESIDUE: route-neutral carrier built and T-indexed bare candidate exhibited;
  no HOL member inhabited; P2-P3, chart normalization, and A7 compatibility unbuilt. (P4)
```

## 5. Q4 — voids and the corrected X9 repayment

### 5.1 PASS/KILL void board

| Item | Verdict | Exact status |
|---|---|---|
| `V1` dependency | **PASS** | A traced dependence on reader, response consequence, threshold, fixed point, or end test is a single-datum failure. |
| `V2` curvature relabeling | **PASS** | A curvature/characteristic-class definition path rather than connection transport is failure-capable; the flat-holonomy regression remains. |
| `V3` hidden counterterm | **GATED, NOT LIVE** | Y9 is untyped until G4; the draft honestly says so, but the gate is not all-live. |
| `V4` discipline | **DEFECTIVE / PARTIAL** | Reality has no displayed D-side action; if G5 supplies H6b it clashes with Y2 at `t=-1`, while without H6b parity is unformed. Rank-preserving restriction is G3; D-side support is uninhabited and the cross-carrier support test is G4. The units arm should be retired or retyped, not silently counted clean. |
| `V5` selection | **PASS** | Binding Xi, a reference connection, gauge representative, sign, or scale gives a text-level witness. |
| `V6` A8 | **PASS WITH CAVEAT** | Every jointly formed H/HOL candidate pair is exposed to A8; disagreement voids the disagreeing construction(s) pending fault isolation, not Xi automatically. |
| `V7` identity branch | **KILL AS WRITTEN** | `(Y-A7)` displays a tautological equivalence, not the required neutrality assertion. |
| `V8` empty family | **PASS AS RELOCATION** | Global emptiness belongs on the stopping board and remains non-witnessing. |

The statement `VOIDS=V1..V7 live-or-repaired` is too strong: V3 is unrunnable, V4 is partial and
internally conflicted, and V7 imposes no obligation.

### 5.2 [PROVABLE] Y-A7 is a tautology, not a neutrality condition

For a fully formed integral same-bundle tuple, R1 gives

```text
Theta_N^rel(Ker_(a,K)(x);A_1,A_0)
 =exp(i p_x),

p_x
 :=u_(Xi_N(Ker_(a,K)(x)))(A_1-A_0).             (A1)
```

Elementary character theory gives, for every real p_x,

```text
exp(i p_x)=1_(U(1))
 <=>p_x in 2 pi Z.                              (A2)
```

V002 writes exactly A2 as `(Y-A7)`. If `p_x not in 2 pi Z`, then both sides of A2 are false and the
biconditional remains true. Therefore one such x does **not** refute the written clause, contrary to
the candidate's single-element-refutability claim.

The actual A7 obligation must assert either side, universally over the retained family:

```text
for every retained (A_1,A_0), every allowed K,
every addressed identity-branch response x,
and the addressed factor basis element,

Theta_N^rel(Ker_(a,K)(x);A_1,A_0)=1_(U(1));

equivalently,
p_x in 2 pi Z.                                  (A3)
```

One displayed x with `p_x not in 2 pi Z` refutes A3 for that alleged tuple. It does not refute A2.

### 5.3 [PART-PROVABLE] Even repaired A3 repays only raw neutrality

For every carried scalarization member S, full HOL2 still needs

```text
1_(U(1)) in U_b^S,
log_b^S(1_(U(1)))=0,
U_(a,1;A_1,A_0,N,S)^Hol(0)=0.                   (A4)
```

G2 says only “certified chart”; it does not state identity containment or zero normalization. G1
types a singular unindexed map and does not state zero preservation. Thus the candidate sentence
“G1/G2 carry the rest” is not a display of A4. With A3 and A4 both inhabited, the raw-neutrality
chain closes; without them the identity branch remains unformed.

### 5.4 Gate completeness

The stopping board lists only G1-G5. Route inhabitance additionally consumes the common, still
uninhabited package

```text
ExtSrc and D_N^Loc,
Ker_(a,K),
the retained same-bundle (A_1,A_0) family,
the corrected Xi member,
the complete Scal^Hol member P3,
and the repaired A3/A4 conditions.               (A5)
```

Calling Xi the one *new correspondence symbol* is syntactically accurate. Calling the route closed
by one new map is not; A5 remains. Adoption would license a specification, never an inhabitant.

## 6. Q5 — fresh attack and consequence board

### 6.1 [PROVABLE conditional on the candidate's claimed reality sector] Negative-scale collapse

V002 scale invariance gives H7. On any admitted signed sector where reality/orientation acts by

```text
u_D(x)=-x,
u_Lambda(z)=-z,                                 (F1)
```

Y10 covariance would give

```text
Xi_N(-x)
 =Xi_N(u_D x)
 =u_Lambda Xi_N(x)
 =-Xi_N(x).                                     (F2)
```

Combining H7 and F2,

```text
Xi_N(x)=-Xi_N(x),
2 Xi_N(x)=0.

Lambda_N^cyc subset Z^(E_N) is torsion-free,
so Xi_N(x)=0.                                   (F3)
```

This is a genuine **conditional** candidate attack. If G5 inhabits F1 on an admitted sector, the
nonzero topological charge collapses there. If F1 is unavailable, no contradiction between scalar
negation and covariance has been derived; instead V002 cannot claim its reality arm or G1-F parity
proof. If physical reversal is intended to equal scalar negation, the repair is positive-scale
invariance plus the separately typed H6b sign law. If it is a distinct address action, V002 must type
that distinction and prove the P2 square without identifying `r_N^D` with `-id`.

The holonomy version reaches the same boundary:

```text
Xi_N(-x)=Xi_N(x)
 =>Theta_N^rel(-x)=Theta_N^rel(x),

signed orientation compatibility
 =>Theta_N^rel(-x)=Theta_N^rel(x)^(-1).          (F4)
```

On an F1 sector, H7 and the signed-orientation line in F4 require every relative phase in that sector
to be two-torsion. No such restriction is sealed or authored.

### 6.2 [YOURS] Consequence board

| Question | Result |
|---|---|
| Do Y1-Y2 evade the old kills? | Yes, set-theoretically, by dropping their antecedents. |
| Is Y2 verified as the physical law? | No. Positive-scale support factorization is unbuilt; all-real scaling is incompatible only on an admitted H6b sign-odd sector, while G5 leaves the source sign action undetermined. |
| Is a nonzero member continuous at zero? | No; H10 is the third horn. |
| Is relative holonomy correctly consumed? | Yes, R1. |
| Is the winding class correct? | Yes, R2; the old factor-line proof is not. |
| Is a real log available? | No; R3 is uninhabited. |
| Are units/integrality correctly separated? | The separation is right, but Y5 crosses carriers and Y6 credits the wrong clause. |
| Are Y7-Y8 exact transport laws? | No; use R10 and R12-R13, all still gated. |
| Does COMMON close U^Hol? | No. COMMON builds the route-neutral carrier; P1 exhibits a bare T-indexed candidate, while the HOL member and P2-P3 remain. |
| Does Y-A7 impose neutrality? | No; it is the tautology A2. |
| Is the void gate all live? | No. |
| Is V002 ready for an adoption ruling? | No; repairs or missing premises affect Y2, Y5-Y8, Y10, Y-A7, G1-G2, and the gate board. |

```text
MACHINERY-APPEAL
 =ExtSrc/DLoc/Ker inhabitance
  +tau_f^Loc/rho_f^Loc and support/covariance members
  +complete HOL chart/scalarization family P3
  +A7 conditions A3-A4;

review continues because the PASS/KILL results above are structural.
```

## 7. Battery and self verb audit

### 7.1 Anti-tuning and fence ledger

| Hazard | Control | Result |
|---|---|---|
| choose a Xi member to make an attack pass | every result is universal or a symbolic countermodel | clean |
| infer failure from a desired H/HOL outcome | no route output or A8 equality is evaluated | clean |
| select A_0 or A_1 | every relative formula carries the ordered pair universally | clean |
| select orientation sign or scale | the whole Triv family remains carried | clean |
| use a real logarithm without a chart | R3 retains the full chart/image/normalization debt | clean |
| call integrality a unit consequence | R5-R8 separate the carriers and reasons | clean |
| lift through a target-new cycle | R12-R14 stop on the old-image domain | clean |
| use reader, response consequence, threshold, fixed point, or end test | none consumed | clean |
| evaluate a program quantity or measured constant | none evaluated or compared | clean |

### 7.2 Verb audit of the candidate and this review

| Candidate verb/status | Audit |
|---|---|
| “locally constant away from 0” | **unsupported**; ray invariance is not ambient local constancy, and H11 gives support-boundary jumps |
| “winding attack settles it” | **unsupported for V002**; R4 is constant on the punctured factor ray, not `exp(i t p)` |
| “D-side datum is dimensionless” | **wrong carrier**; R5 is a cochain pairing result, not R6 |
| “Y2 supplies integrality” | **wrong provenance**; Y1 authors R8 |
| “rho_f^D sealed” | **false**; COMMON Q19c makes the needed `rho_f^Loc` a future member |
| “single x refutes Y-A7” | **false for the written clause**; A2 is true whether both sides are true or false |
| “G1/G2 carry the rest” | **under-displayed**; A4 and P2-P3 are absent |
| “voids V1-V7 live-or-repaired” | **overstated**; V3, V4, and V7 fail that description |
| “one new map” | accurate only as a count of new correspondence symbols, not route closure |

| This review verb | Display that licenses it |
|---|---|
| `verified` | preflight hashes, sidecars, lines, mirrors, register, and no-clobber checks |
| `evades` | H1-H5 exhibit the killed antecedents and a nonzero model |
| `third horn found` | H10 proves unavoidable discontinuity at zero for every nonzero member; H11 gives the stated conditional support-boundary propagation |
| `refuted/killed` | each use has a displayed contradiction, countermodel, wrong carrier, or missing type; H6b/F3 is explicitly conditional |
| `pass` | restricted to a conditional candidate clause with every premise retained |
| `exhibits bare candidate` | P1 is the displayed composition of COMMON's carrier data; lines P2-P4 expressly deny that it inhabits G1, `U^Hol`, or `Scal^Hol` |
| `residue` | exact missing P2-P3 or A3-A5 objects are displayed |
| `not ready` | repairs alter load-bearing clauses rather than editorial wording |

No verb in this review is stronger than its displayed argument.

```text
F_PLDEC = CLEAN;
ANTI_TUNING = CLEAN;
MEMBER_BOUND = false;
FIXED_POINT_EXECUTED = false;
END_TEST_EXECUTED = false;
NUMERIC_EVALUATION = false;
```

No register, plan, tracker, git, commit, push, member-binding, fixed-point, end-test, or evaluation
action was performed by this lane. No law was adopted.

XI_N_V002 = DEFECTIVE (+Y2's physical support factorization is unbuilt, its all-real law conditionally collapses any admitted H6b sign-odd sector, and its local-constancy claim is false; Y4 imports the killed linear winding proof; Y5 crosses C_N^k to D_N^Loc; Y6 miscredits integrality; Y7/Y8 transport types and seal claims fail; Y9/Y10 remain gated; Y-A7 is a tautology, not neutrality; G1/G2 and the void board overclaim closure)
THIRD_HORN = found (+any nonzero scale-invariant Xi with Xi(0)=0 is discontinuous at zero; where typed disjoint supports and a nonzero disjoint contribution exist, additivity propagates the fixed jump to support-birth boundaries)
U_HOL_VIA_SEAMS = RESIDUE (+COMMON builds the route-neutral orientation carrier and Triv family; this review exhibits U_(a,T)^bare=T compose iota_a as a T-indexed candidate of the required type, but no U^Hol or complete Scal^Hol member, odd-input/log-chart chain, normalization, or A7 compatibility is inhabited)
READY_FOR_RULING = no
VERB_AUDIT_SELF = CLEAN
