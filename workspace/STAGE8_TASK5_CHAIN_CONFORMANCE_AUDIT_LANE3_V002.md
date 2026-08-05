# STAGE 8 / TASK 5 — CHAIN-CONFORMANCE AUDIT V002

## The `d^per` modulus repair, the period gate, and the branch-carried lattice

Date: 2026-08-05  
Lane: Codex Lane 3 (SOL, high effort)  
Commission: PASTE 576 / Task 5  
Custody: bounded builder repair for Dario cross-family review

## Lead determination

```text
REGISTER_HEAD = Q-501

V002_DELTA
 = D1  Banach modulus repaired to use d^per in both numerator
       and denominator;
   D2  Step 6 retyped as a carrier residue;
   D3  the period lattice duplicated and symbolically evaluated on both
       DoR-020-A7 E_C branches, without choosing one;
   D4  the two response-to-period routes and the seven bounded
       relays displayed without sizing either route realization
       (Gamma^H or Theta^Hol).

CHAIN_MATHEMATICS
 = PARTLY_CONFORMAL

THRESHOLD
 = LOCAL_SHADOW on the old p_loc route
   and CARRIED_CONDITIONAL on either global-period route

FIXED_POINT_CARRIER = UNDETERMINED
ROUTE_CHOSEN = none
E_C_BRANCH_CHOSEN = none

MEMBER_BOUND = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false
MEASURED_CONSTANT_COMPARISON = none

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

V002 does not rewrite the portions of V001 that survived review. It replaces
V001's `(S5-1)`, `(S9-2)`, `(S9-5b)`, `(S10-1)`, Step-6 verdict, consequence
board, period lattice, and route-program board by the displays below. All
other step analyses remain hash-cited input, not silently re-authored here.

## 0. Preflight, authority, scope, and notation

### 0.1 Preflight

The following checks passed before construction:

```text
register head = Q-501
register SHA-256 =
  47650d5594456a26cd4fdda1889aa8b679dac0dedfb1b188cab782bb01bdfb33

DoR-020-A7 SHA-256 =
  834e46029a292122c1e4c604af4f3e3249e6a9ee2638255464685623fba5eb8f
DoR-020-A7 sealed sidecar = OK

review SHA-256 =
  73524d7a803fb182b1c2988b6b8343cc348b037f2cc4fe04b5a7376505d16992
review sealed sidecar = OK

audit V001 SHA-256 =
  d02576c8a40d6b317819b369f8a6413e24d0e2a792c18a3610df0600e3480ea1
audit V001 sealed sidecar = OK

licensed chain V004 SHA-256 =
  1da746c3956c6b23e17ce10c8bb5ff8e902f7afcf97c3d4eb8d717d7fd7c541a

E_C determination SHA-256 =
  258680c45cbec53ceceabca6d5b3e1a10f8ff4d2c9b8197bfb986c1f9a0cfb48

output artifact absent in cleanroom before construction = verified
output artifact absent in archive workspace before construction = verified
```

The review was read before the repair. In particular, its two hand
counterexamples, Step-6 type correction, route debts, ordering statement,
and instruction that `Gamma` is not relay-sized are consumed explicitly.
DoR-020-A7 is law: its two branches are carried, never selected.

### 0.2 Tags and bounded-delta rule

- `[PROVABLE]` marks an equality or implication derived from the cited
  analytic or structural premises.
- `[PART-PROVABLE]` marks a displayed conditional theorem whose route object
  or certificate has not been inhabited.
- `[YOURS]` marks audit notation, a replacement interface, or a gate. It
  authors no family member and adopts no new law.

The one-verdict definitions remain V001 `(A0)`. In particular, a missing
carrier is a `CONTINUUM_RESIDUAL`, not merely a map reissue.

### 0.3 Common indexing

Fix only for display an admitted address in A7's reciprocal branch scope

```text
a:=(w,N,gamma),
epsilon in {0,1},
r in {H,Hol}.                                    (N0)
```

Here `epsilon` is the carried DoR-020-A7 branch,

```text
E_C,N c_(N,gamma)=epsilon c_(N,gamma),           (N1)
```

and `r=H` denotes the displayed harmonic route through `Loc`, while `r=Hol`
denotes the alternative route through `Xi_N` and connection holonomy. The
A7 scope consists of the actual reciprocal stage and any admitted
covariance image on which `(N1)` is transported by a displayed law. No
`epsilon` datum is authored at an unrelated address. The notation in no way
chooses `a`, `epsilon`, or `r`. Every statement below is universally
quantified over the addresses and branch labels for which its premises are
formed.

When a route is formed, abbreviate

```text
D:=D_(a,epsilon)^(per,r),
d:=d_(a,epsilon)^(per,r),
B:=B_(a,epsilon)^(per,r):D->D.                  (N2)
```

The self-map in `(N2)` is a premise, not a result of notation.

## 1. D1 — the modulus repair

### 1.1 Banach's metric in both slots

[YOURS — required route reissue] The Lipschitz estimate that must replace
V001 `(S5-1)` is

```text
q_cert,(a,epsilon)^(per,r)<infinity,

d(B(K),B(K'))
 <=q_cert,(a,epsilon)^(per,r) d(K,K')

for every K,K' in D.                            (M1)
```

[YOURS — definition] The record-native exact modulus replacing V001
`(S9-2)` is

```text
q_loop,(a,epsilon)^(per,r)
 :=sup_(K!=K' in D)
      d(B(K),B(K'))/d(K,K')
   in [0,infinity].                             (M2)
```

Both occurrences of `d` in each quotient are the same Banach metric on the
same route and branch. No ambient absolute value occurs in `(M2)`. On a
singleton domain the empty secant supremum is defined to be `0`, matching
the unique self-map's zero Lipschitz modulus.

For a typed self-map on a complete nonempty metric domain,

```text
q_loop,(a,epsilon)^(per,r)<1

 iff

there exists q<1 such that
  d(B(K),B(K'))<=q d(K,K')
  for all K,K' in D.                            (M3)
```

Indeed, the forward implication uses `q=q_loop` in the defining supremum.
For the reverse implication, every quotient in `(M2)` is at most the
displayed `q<1`, hence its supremum is at most `q<1`.

Accordingly, the repaired Step-10 statement is

```text
for every admitted (a,epsilon,r),

Step-4--Step-9 route gates
 and B:D->D
 and D is nonempty and complete under d
 and PERIOD_MODULUS_COMPATIBILITY_CERT[a,epsilon,r;Q]

 ->

 (B is a strict d-contraction
    iff q_loop,(a,epsilon)^(per,r)<1).           (M4)
```

The compatibility certificate in `(M4)` exhibits that the quantity being
handed to the theorem is exactly `(M2)`. Once `(M2)` itself is formed, the
equivalence `(M3)` is direct; the gate prevents a derivative or an ambient
secant from being substituted for `(M2)`.

For direct comparison with V001 and the review:

```text
(S5-1-V002)  :=(M1),
(S9-2-V002)  :=(M2),
(S10-1-V002) :=(M4).                            (M4a)
```

### 1.2 `PERIOD_MODULUS_COMPATIBILITY_CERT`

[YOURS — exact falsifiable gate, mirroring V004] The certificate carries an
explicit consumer mode. `Q` certifies the direct Banach modulus; `FACTOR`
certifies the stronger coefficient/amplitude identification:

```text
PERIOD_MODULUS_COMPATIBILITY_CERT[a,epsilon,r;Q]
 :=DIFF_TO_METRIC_Q[a,epsilon,r]
   or DIRECT_MODULUS_Q[a,epsilon,r];

PERIOD_MODULUS_COMPATIBILITY_CERT[a,epsilon,r;FACTOR]
 :=DIFF_TO_METRIC_FACTOR[a,epsilon,r]
   or (DIRECT_MODULUS_Q[a,epsilon,r]
       and METRIC_SECANT_FACTOR_CERT[a,epsilon,r]).              (M5)
```

Every witness begins with the common typed data

```text
B:D->D,
d:D x D->[0,infinity) is the certified complete-domain metric,
q_loop^per is the d/d quotient (M2).             (M6)
```

The `Q` witness forms are as follows. On the differential arm, let

```text
md_d B(K)
 :=the certified metric derivative of B at K
```

in the common chart/absolutely-continuous structure. Equivalently, a chart
witness may define it by the correctly typed tangent norm of
`D(phi compose B compose phi^(-1))`; a bare metric is never written as an
operator-norm domain.

```text
DIFF_TO_METRIC_Q[a,epsilon,r]
 :=branch_scope_(a,epsilon)^(per,r)
     is interval/convex or absolutely continuous
   and there is a certified common chart or metric-derivative
     structure transporting the Step-8 differential exactly
     from its coordinate carrier to d on both input and output
   and the transport proves
     q_loop^per
      =sup_(K!=K' in D) d(B(K),B(K'))/d(K,K')
      =sup_(K in D) md_d B(K).                  (M7)
```

Thus an equivalence of topologies without the two exact transport
equalities is not a witness for `(M7)`.

```text
DIRECT_MODULUS_Q[a,epsilon,r]
 :=Step 9 defines q_loop^per directly by (M2)
   and the Step-8 derivative is used only as a consistency
     witness, never as the definition of q_loop^per.             (M8)
```

The stronger `FACTOR` mode has two exact witness forms. The differential
form is

```text
DIFF_TO_METRIC_FACTOR[a,epsilon,r]
 :=DIFF_TO_METRIC_Q[a,epsilon,r]
   and there is a displayed amplitude a_loop^per(K) with
     md_d B(K)=|chi_(a,epsilon)^(per,r)|
                 |a_loop,(a,epsilon)^(per,r)(K)|
     for every K in D
   and
     A_loop,(a,epsilon)^(per,r)
      :=sup_(K in D)|a_loop,(a,epsilon)^(per,r)(K)|.              (M8a)
```

The direct form requires the displayed metric-secant witness

```text
METRIC_SECANT_FACTOR_CERT[a,epsilon,r]
 :=there exists
a_sec,(a,epsilon)^(per,r):
  {(K,K') in D x D:K!=K'}->K_amb,

d(B(K),B(K'))
 =|chi_(a,epsilon)^(per,r)|
   |a_sec,(a,epsilon)^(per,r)(K,K')|
   d(K,K')

for every K!=K',

A_loop,(a,epsilon)^(per,r)
 :=sup_(K!=K' in D)
      |a_sec,(a,epsilon)^(per,r)(K,K')|.         (M9)
```

On a singleton domain, the last empty supremum is `0`, consistently with
the convention following `(M2)`.

Taking the supremum in `(M8a)` on the differential arm or `(M9)` on the
direct arm gives

```text
q_loop,(a,epsilon)^(per,r)
 =|chi_(a,epsilon)^(per,r)|
   A_loop,(a,epsilon)^(per,r),                  (M10)
```

subject to the separate zero-times-infinity rule displayed in §3. The
response-line vector equation from V001 may be retained as a consistency
witness, but it is not `(M9)`: an equality in an ambient coordinate does
not by itself determine distance in an alternate complete metric.

```text
(S9-5b-V002)
 :=PERIOD_MODULUS_COMPATIBILITY_CERT[a,epsilon,r;FACTOR],
   with (M8a) on the differential arm or (M8)+(M9)
   on the direct arm.                                            (M10a)
```

The gate fails, and the factor lattice is unavailable, if any one of the
following occurs:

```text
B is not a self-map of the displayed D;
the numerator is an ambient norm rather than d(BK,BK');
the derivative chart lacks exact input/output metric transport;
the factor consumer cites mode Q instead of mode FACTOR;
the direct factor branch lacks the metric-secant equality (M9);
the amplitude is imported from a different domain or route.     (M11)
```

When `(M11)` occurs, no surrogate modulus is used. If `(M2)` is nonetheless
formed directly, only the direct `q^per` trichotomy is available; if even
`(M2)` is unformed because `B`, `D`, or `d` is missing, Step 10 does not run.

### 1.3 Permanent regression A — the translated isometry

[PROVABLE — symbolic toy regression, not a program evaluation] Let

```text
D=R,
d(K,K')=2|K-K'|,
B(K)=K+1.                                       (RGA1)
```

The metric is a positive rescaling of the Euclidean metric, so `(D,d)` is
complete and its inclusion into the ambient real carrier is continuous.
Also `B(R) subset R`. Thus the counterexample satisfies the domain,
completeness, inclusion, and self-map premises attacked in the review.

Then for every `K!=K'`,

```text
d(B(K),B(K'))
 =2|(K+1)-(K'+1)|
 =2|K-K'|
 =d(K,K'),

d(B(K),B(K'))/d(K,K')=1,

q^per=1.                                       (RGA2)
```

Therefore `B` is a `d`-isometry, not a strict contraction. The fixed-point
equation would read

```text
K+1=K,
```

which has no solution. The rejected mixed quotient would have reported
`1/2`; `(M2)` reports the required value `1`.

```text
REGRESSION_TRANSLATED_ISOMETRY
 expected q^per = 1
 observed q^per = 1
 status = PASS.                                 (RGA3)
```

### 1.4 Permanent regression B — the quarter-contraction

[PROVABLE — symbolic toy regression, not a program evaluation] Let

```text
D=[0,1],
d(K,K')=|K^2-K'^2|,
B(K)=K/2.                                       (RGB1)
```

The map `phi:[0,1]->[0,1]`, `phi(K)=K^2`, is a bijective isometry from
`(D,d)` to the complete Euclidean interval. Hence `(D,d)` is complete. Its
inclusion into the ambient real carrier is continuous because
`d(K_j,K)->0` implies `K_j^2->K^2` and continuity of the nonnegative square
root implies `K_j->K`. Finally, `B([0,1]) subset [0,1]`. Thus the second
counterexample also satisfies the attacked structural premises.

For every `K!=K'`,

```text
d(B(K),B(K'))
 =|(K/2)^2-(K'/2)^2|
 =(1/4)|K^2-K'^2|
 =(1/4)d(K,K'),

d(B(K),B(K'))/d(K,K')=1/4,

q^per=1/4.                                     (RGB2)
```

Thus `B` is a genuine `d`-quarter-contraction. The rejected mixed quotient
has the form

```text
sup_(K!=K')
  (|K-K'|/2)/(|K-K'||K+K'|)
 =sup_(K!=K') 1/(2|K+K'|)
 =infinity,                                    (RGB3)
```

whereas `(M2)` reports `1/4`.

```text
REGRESSION_QUARTER_CONTRACTION
 expected q^per = 1/4
 observed q^per = 1/4
 status = PASS.                                 (RGB4)
```

The constants in `(RGA1)`--`(RGB4)` belong only to Dario's hand regressions.
No program observable, coupling, period, or measured constant was evaluated.

## 2. D2 — Step 6 retyped and the residue ledger corrected

### 2.1 Step 6 is the carrier commitment

[PROVABLE — review correction] **Step 6 verdict: `CONTINUUM_RESIDUAL`.**

The two route outputs before the generic carrier display are

```text
O_(a,epsilon)^H(K)
 :=Per_(a,epsilon,K)^H(Y_(a,epsilon)^H(K))
 in (H_N^k)^*,

u_(a,epsilon)^H:(H_N^k)^*->K_amb;              (C6-0H)

O_(a,epsilon)^Hol(K)
 :=Hol_(A_N)(Xi_N(Ker_(a,K)(Y_(a,epsilon)^Hol(K))))
 in U_b subset U(1),

log_b:U_b->R,
U_(a,epsilon)^Hol:R->K_amb,
u_(a,epsilon)^Hol
 :=U_(a,epsilon)^Hol compose log_b:U_b->K_amb.  (C6-0Hol)
```

Every map and image assertion in `(C6-0H)`--`(C6-0Hol)` is a route premise,
not a constructed inhabitant. In particular, `(C6-0Hol)` does not declare
a global logarithm on `U(1)`.

The scalar-carrier branch is formed only if the chosen route then supplies

```text
u_(a,epsilon)^r:X_(a,epsilon)^r->K_amb,

B_(a,epsilon)^(per,r)
 :=u_(a,epsilon)^r compose O_(a,epsilon)^r,

B_(a,epsilon)^(per,r):
 D_(a,epsilon)^(per,r)->D_(a,epsilon)^(per,r)
 subset K_amb,

d_(a,epsilon)^(per,r) and
D_COMPLETE_(a,epsilon)^(per,r).                 (C6-1)
```

For `r=H`, `X^H=(H_N^k)^*`. For a scalarized `r=Hol` branch,
`X^Hol=U_b`; before the independently certified arc, logarithm, and unit
map, the upstream object is merely in `U(1)`. If `(C6-1)` is absent, the
output remains in one of

```text
im(P_H,N),
(H_N^k)^*,
a signed real-period line,
or U(1).                                        (C6-2)
```

Then the old equation

```text
K=B(K) on a scalar Banach domain                (C6-3)
```

is not typed. It may require a changed or augmented carrier, a new metric,
and a new completeness proof. No such carrier is supplied or selected by
this audit. Because the carrier itself is the missing object, V001's
`RE-DERIVABLE_RECORD_FIRST` label did not meet its own `(A0)` definition.

### 2.2 Exact residues: `3/6/9/12`

| Step | Verdict in V002 | Exact residue | Risk to the number typing |
|---:|---|---|---|
| 3 | `CONTINUUM_RESIDUAL` | The addressed response-to-loop object is unbuilt: either `Gamma=Loc_N^C compose Ker` with its response-image, support, linearity and naturality proofs, or `Xi_N/Hol_(A_N)` with its kernel-to-loop bridge. The addressed nonzero response line, `Per^H`, scalarization/orientation seam, and any local-reader/period comparison are likewise unproved. | The return may still be an algebraic-reader return rather than a physical global-loop return. |
| 6 | `CONTINUUM_RESIDUAL` | The route has not supplied the self-map and carrier package `(C6-1)`; the possible codomains are `(C6-2)`. | `K=B(K)` may compare objects on different carriers; metric, completeness, and closure may refer to the wrong space. |
| 9 | `CONTINUUM_RESIDUAL` | The global functional and its possible `K`-motion are unbuilt; `FIXED_PERIOD_FACTOR_CERT`, `(M5)`, and any local-shadow/period comparison are undischarged. | A coordinate derivative or local reader can be mislabeled as the true `d^per` modulus or global loop charge. |
| 12 | `CONTINUUM_RESIDUAL` | No smooth addressed parameter object, tangent space, fixed common carrier/domain chart, old-image-only cycle-creation derivative, or family covariance square has been exhibited. | A scalar sensitivity can silently identify different addresses, new-cycle directions, carriers, or family members. |

The corrected complete step board is

```text
ALREADY_CONFORMAL = 0,1,2,7,8,11
RE-DERIVABLE_RECORD_FIRST = 4,5,10
CONTINUUM_RESIDUAL = 3,6,9,12.                  (C6-4)
```

Step 4 must reissue `C_ret` on the chosen route carrier. Step 5 must prove
`(M1)` on that same carrier. Step 10 may use `(M4)` only after the route and
metric are formed. Those are bounded reissues; they do not erase the four
residues in `(C6-4)`.

## 3. D3 — the DoR-020-A7 branch-carried period lattice

### 3.1 Conditions under which a factor lattice exists

The following tables are conditional structural tables, not evaluated
branches. Their factor entries require

```text
ROUTE_FORMED[a,epsilon,r]
 and FIXED_PERIOD_FACTOR_CERT[a,epsilon,r]
 and PERIOD_MODULUS_COMPATIBILITY_CERT[a,epsilon,r;FACTOR].      (L0)
```

Under `(L0)`, write

```text
chi_e^r:=chi_(a,epsilon)^(per,r),
A_e^r:=A_loop,(a,epsilon)^(per,r),
q_e^r:=q_loop,(a,epsilon)^(per,r).               (L1)
```

The infinity/zero cell is never obtained by multiplying `0` by `infinity`.
It uses the pointwise statement

```text
chi_e^r=0
 and the route functional F_e^r is fixed and linear

 and J_e^r(K)=a_loop,e^r(K) Rhat_(Kcycle,a)

 ->F_e^r(J_e^r(K))
    =F_e^r(a_loop,e^r(K) Rhat_(Kcycle,a))
    =a_loop,e^r(K) F_e^r(Rhat_(Kcycle,a))
    =a_loop,e^r(K) chi_e^r
    =0 for every K;

on DIFF_TO_METRIC_FACTOR:
  D B_e^r(K)=0 for every K
  and the interval/AC branch scope gives
  B_e^r(K)=B_e^r(K') for every K,K';

on DIRECT_MODULUS_Q plus METRIC_SECANT_FACTOR_CERT:
  (M9) gives
  d(B_e^r(K),B_e^r(K'))=0 for every K,K';

on either certified branch:
 ->q_e^r=0.                                     (L2)
```

If `(L0)` is absent but `(M2)` is formed, the only licensed case split is

```text
q_e^r=0,
0<q_e^r<1,
q_e^r>=1.                                      (L3)
```

No `chi/A` product is inferred from `(L3)`.

### 3.2 Harmonic/Loc route: effect of the carried contact branch

[PART-PROVABLE — conditional on the unbuilt route] On the displayed
harmonic route, the route contract is

```text
Gamma_(a,epsilon,K)
 =Loc_N^C compose Ker_(a,K),

Loc_N^C=iota_N^H compose Loc_N^phys,

ran(iota_N^H) subset ker(E_C,N),
[E_C,N,P_H,N]=0.                                (H1)
```

For every response `Y`, `(H1)` gives

```text
E_C,N P_H,N Gamma_(a,epsilon,K)(Y)
 =P_H,N E_C,N Gamma_(a,epsilon,K)(Y)
 =P_H,N 0
 =0,

P_H,N Gamma_(a,epsilon,K)(Y)
 in im(P_H,N) intersection ker(E_C,N).          (H2)
```

At the reciprocal rank-one position,

```text
im(P_H,RL)=span{c_RL},
c_RL!=0.                                        (H3)
```

Equations `(H3)`--`(H5)` and the two H tables below are stated at the
literal reciprocal stage. A covariance image inherits them only after a
separate displayed certificate transports `P_H`, preserves the nonzero
rank-one line, and identifies `im(P_H,N)=span{c_(N,gamma)}`. The eigenvalue
transport `(CV1)` alone does not supply those facts.

On the A7 identity branch, `E_C,RL c_RL=c_RL`; hence

```text
im(P_H,RL) intersection ker(E_C,RL)
 =span{c_RL} intersection ker(E_C,RL)
 ={0},

P_H,RL Gamma_(a,1,K)(Y)=0,
Per_(a,1,K)^H(Y)=lambda_0=0,

F_(a,1)^H
 :=u_(a,1)^H compose Per_(a,1,K)^H
 =0,

chi_1^H
 :=F_(a,1)^H(Rhat_(Kcycle,a))
 =0,

B_(a,1)^(per,H)(K)
 =u_(a,1)^H(Per_(a,1,K)^H(Y_(a,1)^H(K)))
 =u_(a,1)^H(0)
 =0,

d(B_(a,1)^(per,H)(K),B_(a,1)^(per,H)(K'))=0,
q_1^H=0.                                       (H4)
```

The equality `u^H(0)=0` uses the route premise that `u^H` is linear (or,
equivalently for this display, zero-preserving). The coefficient lines in
`(H4)` are consumed only when their factor subjects are formed; the direct
conclusion `q_1^H=0` follows from the displayed zero return.

Thus the identity branch's reciprocal vanishing is a theorem of the
route-plus-A7 premises and enters the lattice as a consequence. It is not a
defect, a discarded branch, or a reason to choose the zero branch.

On the A7 zero branch, `E_C,RL c_RL=0`; therefore

```text
im(P_H,RL) intersection ker(E_C,RL)
 =span{c_RL}.                                   (H5)
```

Equation `(H5)` removes the contact obstruction but proves neither
`chi_0^H=0` nor `chi_0^H!=0`. Both coefficient cells remain carried.

### 3.3 Full harmonic-route lattice, `epsilon=0`

Under `(L0)` for `r=H,epsilon=0`, every cell is:

| `A_0^H` | `chi_0^H` | `q_0^H` | Contraction verdict |
|---|---|---|---|
| `0` | `0` | `0` by `(L2)` | strict |
| `0` | `!=0` | `0` by `(M8a)` on the differential arm or `(M9)` on the direct arm | strict |
| `0<A_0^H<infinity` | `0` | `0` by `(L2)` | strict |
| `0<A_0^H<infinity` | `!=0` | `|chi_0^H|A_0^H` | strict iff `|chi_0^H|A_0^H<1` |
| `infinity` | `0` | `0` by the pointwise rule `(L2)`, not `0*infinity` | strict |
| `infinity` | `!=0` | `infinity` | not strict |

This table does not decide which row is realized.

Inside its finite, nonzero fourth row, the threshold split is exact:

```text
|chi_0^H|<(A_0^H)^(-1) ->0<q_0^H<1, strict;
|chi_0^H|=(A_0^H)^(-1) ->q_0^H=1, not strict;
|chi_0^H|>(A_0^H)^(-1) ->q_0^H>1, not strict.  (H6)
```

### 3.4 Full harmonic-route lattice, `epsilon=1`

Under `(L0)` and the route premises `(H1)`--`(H4)`, every nominal cell is:

| `A_1^H` | nominal `chi_1^H` cell | A7 identity-branch result | `q_1^H` | Contraction verdict |
|---|---|---|---|---|
| `0` | `0` | only possible coefficient cell; route inhabitance unproved | `0` by `(H4)` | strict |
| `0` | `!=0` | empty: `(H4)` forces `chi_1^H=0` | no member of this cell | not applicable |
| `0<A_1^H<infinity` | `0` | only possible coefficient cell; route inhabitance unproved | `0` by `(H4)` | strict |
| `0<A_1^H<infinity` | `!=0` | empty: `(H4)` forces `chi_1^H=0` | no member of this cell | not applicable |
| `infinity` | `0` | only possible coefficient cell; route inhabitance unproved | `0` by `(H4)`, not `0*infinity` | strict |
| `infinity` | `!=0` | empty: `(H4)` forces `chi_1^H=0` | no member of this cell | not applicable |

No branch is voided merely because its lawful result is zero. A7's
certified-lattice-exit, earlier-falsifier, sealed-derivation, and eventual
end-test rules remain in force; none is executed here. The zero-modulus
cells above remain inside the displayed conditional lattice.

### 3.5 Holonomy route: both A7 branches and the explicit compatibility debt

The alternative route has the shape

```text
O_a^resp
 --Ker_(a,K)->D_N^Loc
 --Xi_N------>Z_N^loop
 --Hol_(A_N)->U(1),                             (HOL1)

Theta_(a,K)^Hol
 :=Hol_(A_N) compose Xi_N compose Ker_(a,K)
 :O_a^resp->U(1).                               (HOL1a)
```

followed, on a scalar-return branch, by a certified arc/log/unit map. It
does not enter `C_N^k`; consequently the commutator/confinement calculation
`(H1)`--`(H4)` cannot be transported through `(HOL1)`. The Hol composite
evades `E_C` as a map-level statement.

DoR-020-A7 is later law, however, and independently declares reciprocal
vanishing on its identity branch. Therefore an admissible Hol route must
exhibit the additional, falsifiable interface. `[YOURS]` names that
route/law compatibility debt; it does not adopt the interface:

```text
A7 identity-branch "reciprocal vanishing"
 --unbuilt Hol interpretation bridge-->
neutral raw holonomy 1_(U(1))
 on both the actual response family and the addressed factor basis.      (HOL1b)
```

Without the bridge in `(HOL1b)`, A7's Hodge-side wording does not itself
identify `chi_1^Hol` or the Hol return.

```text
A7_HOL_BRANCH_COMPAT[a]
 :=Theta_(a,K)^Hol(Y_(a,1)^Hol(K))=1_(U(1))
      for every K in D_(a,1)^(per,Hol)

   and Theta_(a,K)^Hol(Rhat_(Kcycle,a))=1_(U(1))
      for every K whenever the addressed factor line is formed

   and 1_(U(1)) in U_b
   and log_b(1_(U(1)))=0
   and U_(a,1)^Hol(0)=0.                        (HOL2)
```

`(HOL2)` is not derived by pretending that `E_C` acts on `U(1)`. It is the
exact debt for making the Hol return conform to A7's carried identity
branch. If `(HOL2)` is absent, the Hol identity branch is **unformed**, not
silently dropped and not allowed to use a nonzero-coefficient row.

When `(HOL2)` and the scalar-return typing are exhibited, the consequence
is displayed rather than stipulated:

```text
Theta_(a,K)^Hol(Y_(a,1)^Hol(K))=1_(U(1))

 ->log_b(Theta_(a,K)^Hol(Y_(a,1)^Hol(K)))=0

 ->B_(a,1)^(per,Hol)(K)=U_(a,1)^Hol(0)=0
      for every K

 ->d(B_(a,1)^(per,Hol)(K),B_(a,1)^(per,Hol)(K'))=0
      for every K,K'

 ->q_1^Hol=0;

Theta_(a,K)^Hol(Rhat_(Kcycle,a))=1_(U(1))

 ->chi_1^Hol
    :=U_(a,1)^Hol(
        log_b(Theta_(a,K)^Hol(Rhat_(Kcycle,a))))
     =U_(a,1)^Hol(log_b(1_(U(1))))
     =U_(a,1)^Hol(0)
     =0.                                        (HOL2a)
```

Under `(L0)` and, for `epsilon=1`, `(HOL2)`, all twelve nominal cells are:

| `epsilon` | `A_e^Hol` | `chi_e^Hol` | `q_e^Hol` | Contraction verdict |
|---:|---|---|---|---|
| `0` | `0` | `0` | `0` by `(L2)` | strict |
| `0` | `0` | `!=0` | `0` by `(M8a)` on the differential arm or `(M9)` on the direct arm | strict |
| `0` | `0<A_0^Hol<infinity` | `0` | `0` by `(L2)` | strict |
| `0` | `0<A_0^Hol<infinity` | `!=0` | `|chi_0^Hol|A_0^Hol` | strict iff the product is `<1` |
| `0` | `infinity` | `0` | `0` by `(L2)`, not `0*infinity` | strict |
| `0` | `infinity` | `!=0` | `infinity` | not strict |
| `1` | `0` | `0` | `0` by `(HOL2a)` | strict |
| `1` | `0` | `!=0` | empty: `(HOL2a)` forces `chi_1^Hol=0` | not applicable |
| `1` | `0<A_1^Hol<infinity` | `0` | `0` by `(HOL2a)` | strict |
| `1` | `0<A_1^Hol<infinity` | `!=0` | empty: `(HOL2a)` forces `chi_1^Hol=0` | not applicable |
| `1` | `infinity` | `0` | `0` by `(HOL2a)`, not `0*infinity` | strict |
| `1` | `infinity` | `!=0` | empty: `(HOL2a)` forces `chi_1^Hol=0` | not applicable |

For `epsilon=0`, the finite nonzero row splits at `<`, `=`, and `>` of
`|chi_0^Hol|=(A_0^Hol)^(-1)` exactly as `(H6)`. For `epsilon=1`, the three
zero-coefficient rows remain inside the lattice; the three nonzero rows are
empty only after `(HOL2)`--`(HOL2a)` are exhibited. This carries A7 without importing a
false `E_C` action into the Hol composite.

If a later, otherwise certified Hol computation on `epsilon=1` produces a
nonzero reciprocal coefficient, it falsifies `(HOL2)` and triggers A7's
earlier-falsifier rule. That is a structural branch/route failure, not a
threshold-based selection of `epsilon=0`.

### 3.6 Covariance and no selection

For an admitted covariance map `g_C`, branch carriage requires

```text
g_C c_(N,gamma)=c_(gN,g_*gamma),
g_C E_C,N=E_C,gN g_C,

E_C,gN c_(gN,g_*gamma)
 =E_C,gN g_C c_(N,gamma)
 =g_C E_C,N c_(N,gamma)
 =epsilon g_C c_(N,gamma)
 =epsilon c_(gN,g_*gamma).                     (CV1)
```

Thus covariance preserves `epsilon`; it does not map one branch into the
other. A future formed return family must display, separately for each
`epsilon`,

```text
g_D^epsilon compose B_(a,epsilon)^(per,r)
 =B_(g.a,epsilon)^(per,r) compose g_D^epsilon.  (CV2)
```

The object carried forward is

```text
(B_(a,epsilon)^(per,r),
 D_(a,epsilon)^(per,r),
 d_(a,epsilon)^(per,r))_(epsilon in {0,1})      (CV3)
```

as an `epsilon`-tagged indexed family, not an ordinary set that would
collapse equal maps. It carries no selector, comparison-by-desired-output,
or cross-branch equality.
Step 11's Banach consequence, if all gates are later discharged, applies
fiberwise to each branch. It is not executed here.

On a cycle-creating arrow, `(CV1)`--`(CV2)` are asserted only for the
contravariant target-to-source map

```text
rho_f:C_M^k->C_N^k

on the old-image summand,

rho_f E_C,M=E_C,N rho_f,

rho_f c_(M,gamma_M^old)=c_(N,gamma)
  for an independently exhibited target old-image representative,

E_C,M c_(M,gamma_M^old)=epsilon c_(M,gamma_M^old)

 ->E_C,N rho_f c_(M,gamma_M^old)
    =rho_f E_C,M c_(M,gamma_M^old)
    =epsilon rho_f c_(M,gamma_M^old),

rho_f^D compose B_(M,epsilon)^(per,r)
 =B_(N,epsilon)^(per,r) compose rho_f^D
  on the certified old-image return domain.     (CV4)
```

They do not transport an `epsilon` label upward onto the new-cycle summand.
That summand remains unclassified unless an independent ratified branch
datum is supplied; no lift or cross-cycle selector is added.

## 4. D4 — route-choice board and the seven bounded relays

### 4.1 The two routes, side by side

[YOURS — analysis board; no route adopted]

| Field | Displayed harmonic route `r=H` | Connection-holonomy route `r=Hol` |
|---|---|---|
| route | `O^resp --Ker--> D_N^Loc --Loc_N^C--> C_N^k --P_H--> H_N^k --(x maps to lambda_x)--> (H_N^k)^* --ev_(N,gamma)--> ChargeUnit_N --U_(w,N,gamma)--> K_amb` | `O^resp --Ker--> D_N^Loc --Xi_N--> Z_N^loop --Hol_(A_N)--> U_b subset U(1) --log_b--> R --U^Hol--> K_amb`, after a whole-image-in-`U_b` proof |
| response realization | `Gamma^H=Loc_N^C compose Ker:O^resp->C_N^k`, with `Loc_N^C=iota_N^H compose Loc_N^phys` | no identification with `Gamma^H`; `Theta^Hol=Hol_(A_N) compose Xi_N compose Ker:O^resp->U(1)` |
| common debts | addressed, `K`-independent `Res^resp`; nonzero addressed-line certificate; definition and image typing of `Ker`; period-domain certificate; support, units, and reality; rank-preserving naturality; cycle creation only by contravariant downward old-image maps, never an upward lift | the same common debts, with each map retyped on the Hol carrier rather than imported from the H route |
| primary construction debt | `Ker` image membership; physical `Loc`; linearity; support and rank-preserving naturality; cycle-creation old-image law; addressed response-line certificate | `Xi_N` is unauthored; no sealed map sends a kernel response to a loop; A1 path/current and bundle holonomy do not supply that missing argument map |
| scalar seam | fixed `ev_(N,gamma)` and unit map `U_(w,N,gamma)` with orientation compensation | response-independent arc `U_b subset U(1)`, image proof, `log_b`, unit map, orientation covariance |
| carrier debt | closure into `D^per subset K_amb`, metric, completeness | either the scalar package after the log seam or a changed complete metric carrier on `U(1)` with a new contraction theorem instance |
| factor/modulus debt | addressed nonzero line; `FIXED_PERIOD_FACTOR_CERT`; `(M5)` in `Q` or `FACTOR` mode as consumed | after scalarization, a separate fixed-holonomy factor certificate and `(M5;FACTOR)`; on raw `U(1)` only `(M5;Q)` and the direct same-metric modulus type; `A7_HOL_BRANCH_COMPAT` for the identity branch |
| A7 effect | both branches carried; `epsilon=1` forces reciprocal zero by `(H4)`, while `epsilon=0` leaves the period pairing undecided | `E_C` is not consumed, so its map-level proof does not transfer; A7 requires the reciprocal-vanishing outcome, while this audit's unbuilt `(HOL1b)`--`(HOL2)` candidate types that outcome on Hol and yields `q=0`; `epsilon=0` retains the full lattice |
| Step 10 | unavailable until the route object, carrier, and certificates are formed | unavailable until `Xi_N`, holonomy scalarization/carrier, and certificates are formed |

The exact alternatives are therefore

```text
ROUTE_H_DEBT
 =physical Loc construction
  +Ker image/interface
  +Gamma/Per/u
  +A7-branchwise carrier and certificates;

ROUTE_HOL_DEBT
 =Xi_N kernel-to-loop amendment
  +Hol image and arc/log/unit interface
  +route carrier
  +A7_HOL_BRANCH_COMPAT
  +A7-branchwise certificates.                 (RB1)
```

No sealed implication orders these alternatives. This audit does not choose
a route.

### 4.2 Why the program has seven relays, not eight

Dario's review displayed rows `R1`--`R8` while also recording the verdict
`REDERIVATION_PROGRAM = 7 relays`. The honest reconciliation is to separate
its row `R2`, **route commitment**, as the principal's route decision
`D_ROUTE`, not as a mathematical repair relay:

```text
D_ROUTE :=principal-facing choice between ROUTE_H_DEBT
          and ROUTE_HOL_DEBT, after relay L1;

D_ROUTE is a decision precondition, not relay work;
no value, branch, family member, or fixed point decides it.      (RB2)
```

The construction of the selected route realization remains

```text
OPEN_ROUTE_H
 :=OPEN_GAMMA^H
 :=physical Loc/Gamma^H construction;

OPEN_ROUTE_Hol
 :=OPEN_THETA^Hol
 :=Xi_N/Hol/Theta^Hol construction
   plus its full route gate, including (HOL2);

OPEN_ROUTE_r :=the applicable one of those two case-typed objects.        (RB3)
```

`OPEN_ROUTE_r` is the standing open object. It is not assigned a relay
size, and the seven bounded relays do not substitute for it. Only the H
object has the type and name `Gamma^H`; the Hol object is `Theta^Hol`.

### 4.3 Seven-relay program under either route

| Bounded relay | Common deliverable | Harmonic-route instance | Holonomy-route instance | Depends on |
|---:|---|---|---|---|
| L1 | Modulus repair | use `(M1)`--`(M11)` with `d^H` | use `(M1)`--`(M8)` for direct `Q` mode on a certified scalar or circle metric; `(M9)`--`(M10)` only after scalarization | none; displayed in this V002 |
| L2 | Step-6 retype and carrier seam | exhibit `(C6-1)` for `(H_N^k)^* --u^H--> K_amb` | exhibit the arc/log scalar seam or an explicitly changed complete metric carrier on `U(1)` | `D_ROUTE`, `OPEN_ROUTE_r` |
| L3 | Fixed factor certificate | prove `F^H` is fixed and linear on the addressed response line and type `chi^H` | separately prove a single-valued scalarized Hol factorization is fixed on its response line and type `chi^Hol`; if it fails, retain direct `q` only | `D_ROUTE`, `OPEN_ROUTE_r` |
| L4 | `PERIOD_MODULUS_COMPATIBILITY_CERT` | discharge mode `Q` or `FACTOR`, as consumed, for both A7 branches | discharge the route-specific same-metric witness; factor mode is unavailable on an unscalarized circle carrier | L1, L2, L3 |
| L5 | Steps 4/5 reissue | reissue `C_ret^per` and `(M1)` for each `epsilon` | reissue the route return object and `(M1)` for each `epsilon` | `D_ROUTE`, `OPEN_ROUTE_r`, L2 |
| L6 | Step-10 lattice transfer | transfer §§3.3--3.4 under L3--L5; otherwise retain `(L3)` | transfer §3.5 under L3--L5; otherwise retain `(L3)` | L3, L4, L5 |
| L7 | Residues and witness boundary | carry exact `3/6/9/12`, A7 branch labels, and stop before any unbuilt object | same, with the `Xi_N`/arc-log and `(HOL2)` debts named | L1--L6 |

This is the review's dependency order with its principal decision taken out
of the work count:

```text
review R1 -> V002 L1;
review R2 -> D_ROUTE (decision after L1, not relay);
review R3,R4,R5,R6,R7,R8 -> V002 L2,L3,L4,L5,L6,L7.             (RB4)
```

Step 10 awaits `D_ROUTE` and `OPEN_ROUTE_r` because its return map, carrier, metric,
coefficient, amplitude, and compatibility witness are route-indexed. It
cannot be reissued by combining benefits from both unchosen routes.

### 4.4 Witness boundary after the bounded repairs

Even after L1--L7, witness certification may proceed only if the selected
`OPEN_ROUTE_r` object is actually built and all route gates are discharged.
Then it would certify a record-first, branch-carried conditional chain. It
would not certify any of the following:

```text
A_RP_PLUS is inhabited;
the seed is nonzero;
one E_C branch is physically selected;
one family member is selected;
the membership theorem is repaired;
the fixed point has been executed;
a coupling or measured constant has been computed.             (RB5)
```

## 5. Consequence board

### 5.1 V002 step verdicts

| Step | V002 verdict | V002 consequence |
|---:|---|---|
| 0 | `ALREADY_CONFORMAL` | entrance remains undischarged |
| 1 | `ALREADY_CONFORMAL` | nonempty covariant family; no selector |
| 2 | `ALREADY_CONFORMAL` | all-address/all-arrow regressions retained |
| 3 | `CONTINUUM_RESIDUAL` | choose neither route here; build the selected response-to-loop object separately |
| 4 | `RE-DERIVABLE_RECORD_FIRST` | reissue the return certificate on the selected route and each A7 branch |
| 5 | `RE-DERIVABLE_RECORD_FIRST` | use the same-metric inequality `(M1)` |
| 6 | `CONTINUUM_RESIDUAL` | carrier commitment remains absent until `(C6-1)` |
| 7 | `ALREADY_CONFORMAL` | completeness/regularity separation retained per route/branch |
| 8 | `ALREADY_CONFORMAL` | reader-free Schur pre-charge response retained |
| 9 | `CONTINUUM_RESIDUAL` | global functional, motion, factor, and modulus interface remain unbuilt |
| 10 | `RE-DERIVABLE_RECORD_FIRST` | direct threshold uses `(M2)`; product lattice only under `(L0)` |
| 11 | `ALREADY_CONFORMAL` | conditional Banach theorem remains fiberwise; not executed |
| 12 | `CONTINUUM_RESIDUAL` | smooth addressed contravariant family sensitivity remains unbuilt |

### 5.2 Threshold status by route and A7 branch

Every row below is restricted to the literal reciprocal stage or a
separately certified rank-one covariance image. The H identity branch's
direct `q=0` uses `(H1)`--`(H4)`; its `A/chi` cells additionally use `(L0)`.
The Hol identity row is conditional on the unbuilt interpretation and
compatibility interfaces `(HOL1b)`--`(HOL2)`.

| Route / branch | Structural threshold status now |
|---|---|
| `H, epsilon=0` | product lattice is well-shaped but conditional; coefficient zero/nonzero remains undecided |
| `H, epsilon=1` | once the route is formed, reciprocal vanishing gives the direct same-metric value `q=0`; branch remains carried |
| `Hol, epsilon=0` | full lattice conditional on the unauthored `Xi_N` route and its certs |
| `Hol, epsilon=1` | A7 supplies the required reciprocal-vanishing outcome but does not type it on Hol; if the unbuilt interpretation/compatibility interface `(HOL1b)`--`(HOL2)` is exhibited, `(HOL2a)` follows, only the zero-coefficient rows remain, and `q=0`; without that interface this route branch is unformed |

The old local threshold remains a local shadow. This V002 repairs the metric
of the global-period candidate; it does not prove the candidate's missing
maps or identify it with the old reader.

The word `strict` in the lattice tables classifies only the conditional
Lipschitz modulus. It does not execute Step 11; all self-map, completeness,
and `(M4)` gates remain required.

## 6. D5 — batteries

### 6.1 F_PLDEC

The repaired direct modulus consumes only

```text
B_(a,epsilon)^(per,r),
D_(a,epsilon)^(per,r),
d_(a,epsilon)^(per,r).                          (F1)
```

When formed, the H candidate depends only on addressed `Res^resp`, `Ker`,
`Loc^C`, `P_H`, `ev`, and `U^H`; the Hol candidate depends only on addressed
`Res^resp`, `Ker`, `Xi_N`, `Hol_(A_N)`, the arc/log/unit seam, and the raw A7
compatibility interface. Its factor branch would consume the independently
typed global period or holonomy functional and response line. No definition in `(M1)`--`(M11)`,
`(H1)`--`(H5)`, or `(HOL1)`--`(HOL2a)` consumes `p_loc`, the J2 reader, the false anchor
`pi_Mx compose Loc compose Kernbar compose Q=1`, a threshold result, or an
eventual fixed point. The mentions of the local reader in this audit are
scope comparisons only; it is never used to construct the period object.

```text
F_PLDEC = PASS
FALSE_ANCHOR_CONSUMED = false
READER_CONSUMED_BY_PERIOD_BUILD = false.         (F2)
```

### 6.2 Anti-tuning ledger

| Potential tuning point | Control used here | Result |
|---|---|---|
| numerator of `q^per` | fixed by Banach's own metric, before any threshold consequence | clean |
| regression scores | derived from the two stipulated toy metrics | clean |
| `E_C` boundary condition | both A7 labels retained; the Hol identity branch is gated/unformed absent `(HOL1b)`--`(HOL2)`, never dropped | clean; no branch selection |
| route | debts shown side by side; `D_ROUTE` remains external and no threshold consequence informs it | clean; no route selection |
| `chi=0` cell | on `epsilon=0`, zero/nonzero are both case labels; on H `epsilon=1`, zero is derived conditionally by `(H4)`; on Hol `epsilon=1`, zero follows only from `(HOL1b)`--`(HOL2a)` plus factor normalization | clean; no cell chosen from contractivity |
| factor versus direct modulus | product used only under `(L0)`; otherwise direct trichotomy `(L3)` | clean |
| family/address | arbitrary display index universally restored | clean; no member binding |
| carrier | marked residual rather than chosen to preserve the old scalar equation | clean |
| physical output | no root, coupling, period magnitude, or measured constant evaluated | clean |

### 6.3 Machinery appeals

```text
MACHINERY-APPEAL = true
  (+addressed Res^resp and nonzero-line certificate unbuilt;
   +Ker definition/image and period-domain objects unbuilt;
   +OPEN_ROUTE_H=OPEN_GAMMA^H unbuilt;
   +OPEN_ROUTE_Hol=OPEN_THETA^Hol unbuilt;
   +physical Loc and its nonidentity naturality unbuilt on route H;
   +Xi_N kernel-to-loop map unbuilt on route Hol;
   +route scalarization/carrier packages uninhabited;
   +A7_HOL_BRANCH_COMPAT unbuilt on route Hol;
   +fixed-factor and period-modulus witnesses unproved;
   +smooth addressed sensitivity object unbuilt).
```

These fences block constructions, not the structural modulus repair,
Step-6 type correction, branchwise conditional lattice, or route analysis.

### 6.4 Self verb audit

| Claim | Displayed support | Audit |
|---|---|---|
| modulus `REPAIRED` | `(M1)`--`(M4)` put `d` in both numerator and denominator | clean |
| period gate `STATED` | exact disjunction and witness forms `(M5)`--`(M11)` | clean; not called proved |
| regressions `PASS` | complete calculations `(RGA1)`--`(RGA3)` and `(RGB1)`--`(RGB4)` | clean |
| Step 6 `CONTINUUM_RESIDUAL` | carrier alternatives and missing package `(C6-1)`--`(C6-3)` | clean |
| residues `3/6/9/12 exact` | four-row ledger and complete board `(C6-4)` | clean |
| identity branch `forces reciprocal vanishing` | conditional route chain `(H1)`--`(H4)` | clean; route formation remains a premise |
| zero branch `leaves pairing undecided` | `(H5)` removes only the contact obstruction | clean |
| Hol route `evades E_C` but still owes A7 compatibility | `(HOL1)` never enters `C_N^k`; A7 is cited, while the raw interpretation/compatibility candidate is displayed in `(HOL1b)`--`(HOL2)` | clean; neither route nor candidate called built |
| branch lattice `carried` | conditional symbolic cells for both H labels and both nominal Hol labels, with `(HOL2)` gating the Hol identity rows and covariance `(CV1)`--`(CV4)` | clean; no route or branch inhabited |
| seven-relay board `stated` | decision/relay split `(RB2)`--`(RB4)` and seven rows | clean |
| selected route realization `unsized` | case-typed `Gamma^H` versus `Theta^Hol` in `(RB3)`, explicitly outside the relay count | clean |
| no execution | `(RB5)`, F_PLDEC, and anti-tuning ledger | clean |

No verb in this board upgrades a candidate interface, route, certificate, or
family branch into an inhabited construction.

MODULUS = REPAIRED (+regressions scored: translated isometry q^per=1; quarter-contraction q^per=1/4)
PERIOD_GATE = STATED
RESIDUES = 3/6/9/12 exact
BRANCH_LATTICE = carried
ROUTE_BOARD = stated
VERB_AUDIT_SELF = CLEAN
