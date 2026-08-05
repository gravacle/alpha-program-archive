# STAGE 8 / TASK 5 / EQ6 — LOC FAMILY V002: THE HONEST FAMILY, AND CAN IT THREAD?

Date: 2026-08-05  
Lane: Codex Lane 3 (SOL, high effort)  
Task: PASTE 571 / Task 5 / EQ6  
Custody: builder repair for Dario cross-family review

## Lead determination

```text
REGISTER_HEAD = Q-497

HONEST_FAMILY
 = C1' stated
   (+the Hodge-range clause is struck;
    +neither (S28) nor not-(S28) is a membership condition)

THREADING
 = UNDETERMINED
   (+acyclic stages vanish because P_H=0 there;
    +on the cycle-carrying reciprocal stage the unresolved quantity is
       q_T,RL(L)
        :=<iota_RL^H(s_Max,RL^unit),c_RL>_RL;
    +no full-gate member is presently sealed)

HOL_PROVENANCE
 = A1_AMENDMENT_NEEDED
   (+this is the separate provenance verdict for any added Hol_N route;
    +it does not decide the intrinsic C1' harmonic component)

MEMBER_BOUND = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false
MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = true
  (+sealed stock supplies neither a full-gate C1' member of record
   nor a theorem fixing B_RL(L)(s_Max,RL^unit)
   to zero or nonzero)

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The range condition in the old `(C1)` was absent from the Hodge fiber.
It imposed the zero answer to the very question the family was meant to
test and, more strongly, deleted the exact Hodge sector. After removing that
condition, the symbol-side Maxwell pin remains fixed but its Hodge harmonic
coordinate is not fixed. The displayed genuine Hodge subclauses have both
zero and nonzero clause-separation models; the stock supplies neither an
actual full-gate member nor a theorem selecting one polarity. Outcome Y2(c),
**UNDETERMINED**, is therefore the only licensed outcome.

## 0. Preflight, authorities, tags, and fences

### 0.1 Access and no-clobber

The following checks were completed before construction:

```text
register head                                  = Q-497
register SHA-256                               =
  6482eddac166fe73a7bc92ab8aa507695a0d176f22cd1668ad514258c91d8b8e

review sidecar verification                    = OK
review SHA-256                                 =
  a58400f6949322885802bf0c22d765025aa526e252f63cbc47b4c194b2c24104

prior Loc-build sidecar verification           = OK
prior Loc-build SHA-256                        =
  b53d9e931efe1ebde333ef49fb4243e41917bb5d467f5a86e7052102ae5a0310

output absent in cleanroom before construction = true
output absent in archive before construction   = true
```

The review was read before the repair. Its H1(a) finding is the controlling
scope correction in this artifact.

### 0.2 Result tags

- `[PROVABLE]` marks a consequence of sealed finite linear algebra or a
  direct comparison of displayed predicates.
- `[PART-PROVABLE]` marks a displayed implication conditional on a future
  full-gate member.
- `[YOURS]` marks candidate syntax or a new audit control authored here. It
  is not promoted to sealed law or to an inhabitance theorem.

### 0.3 Fences

This artifact is symbolic. Zero versus nonzero is used only as a structural
classification. It binds no member, evaluates no seed, executes no end test,
and consumes neither the algebraic reader nor the equation

```text
p_Mx,N^sym(
  Loc_N^phys(
    Kernbarhat_N(Q_N(L_T,N))))=1.                (FALSE-ANCHOR)
```

`(FALSE-ANCHOR)` is displayed only to identify the prohibited dependency.

## 1. Y1 — the honest family `(C1')`

### 1.1 The old clause and its exact force

The final membership clause of the old `(C1)` was

```text
x_T,N
 :=iota_N^H Loc_N^phys(kappa_T,N)
   in closure(ran(M_N^(Hdg,k))),

M_N^(Hdg,k)
 :=delta_N^(k+1) d_N^k.                         (R1)
```

[PROVABLE] On the finite Hodge carrier, with
`delta_N^(k+1)=(d_N^k)^*`, orthogonal decomposition gives

```text
C_N^(k+1)
 =ran(d_N^k) (+)_perp ker(delta_N^(k+1)),

delta_N^(k+1)(C_N^(k+1))
 =delta_N^(k+1)(ran(d_N^k))
  +delta_N^(k+1)(ker(delta_N^(k+1)))

 =ran(delta_N^(k+1)d_N^k)+{0},

ran(M_N^(Hdg,k))
 =ran(delta_N^(k+1)).                           (R2)
```

The projector certificate gives

```text
ker(P_H,N)
 =ran(d_N^(k-1))
   (+)_perp ran(delta_N^(k+1)).                 (R3)
```

Consequently

```text
closure(ran(M_N^(Hdg,k)))
 =ran(delta_N^(k+1))
 subset ker(P_H,N),                             (R4)
```

where closure adds nothing on the finite carrier. Applying `(R4)` to `(R1)`
gave

```text
P_H,N x_T,N=0.                                  (R5)
```

Because `Loc_N^C=iota_N^H Loc_N^phys`, `(R5)` is exactly

```text
P_H,N Loc_N^C(kappa_T,N)=0,                     (R6)
```

which is `not-(S28)`. Moreover, whenever
`ran(d_N^(k-1))` is nonzero, `(R3)`--`(R4)` show that `(R1)` is stronger
than `(R6)`: it also excludes the entire exact sector
`ran(d_N^(k-1))`.

### 1.2 Why no lawful retained clause forces `(R1)`

[PROVABLE] The Hodge fiber declared in the Loc build is exactly

```text
Hdg
 :={ (iotatilde_N^H,iota_N^H)_N :
      (S14),(S19),(S21),(S25),(S25b),
      and every Hodge diamond equation hold }.  (R7)
```

Displayed by content, `(R7)` requires

```text
iota_N^H:Sym_N^loc -> C_N^k,                    (S14)

iota_N^H(a s+b s')
 =a iota_N^H(s)+b iota_N^H(s'),                 (S19)

Ctc_N^sym subset ker(iotatilde_N^H),
iota_N^H([s]_Ctc_sym)=iotatilde_N^H(s),
iota_N^H([s]_Ctc_sym)
 =(1-E_C,N)iota_N^H([s]_Ctc_sym),               (S21)

iota_M^H j_f^Sym
 =j_f^C iota_N^H                               (S25)
```

on rank-preserving arrows, and

```text
rho_a^C iota_M^H|_(Sym_M^old)
 =iota_N^H rho_a^Sym                            (S25b)
```

on the old-image part of a cycle-creating arrow. None of these equations
contains `d`, `delta`, `M^(Hdg,k)`, `ran`, or `P_H`. Projector naturality

```text
rho_f P_H,M=P_H,N rho_f                         (R8)
```

only transports a harmonic component after it exists; `(R8)` does not make
that component zero and does not imply `(R1)`.

The retained symbol pin likewise says only

```text
Loc_N^phys(kappa_T,N)
 =s_Max,N^unit
 :=[sigma_2^op(M_N^loc)]_Ctc_sym.               (R9)
```

There is no retained bridge

```text
iota_N^H(s_Max,N^unit)
  in closure(ran(delta_N^(k+1)d_N^k)).          (UNLICENSED-BRIDGE)
```

Thus the words “principal Maxwell symbol” do not license a Hodge-range
inclusion. The physical-symbol carrier and the cochain carrier remain
separately typed.

### 1.3 Exact strike

[PROVABLE — predicate comparison] The repair deletes exactly this old
membership predicate:

```text
STRIKE_FROM_C1
 := { iota_N^H Loc_N^phys(kappa_T,N)
       in closure(ran(M_N^(Hdg,k))) }.           (R10)
```

It adds neither `(S28)` nor `not-(S28)`. In particular, it does **not**
replace `(R10)` by the weaker condition `P_H,N x_T,N=0`.

The derived ambient operator

```text
M_N^(Hdg,k)=delta_N^(k+1)d_N^k                 (R11)
```

remains available for Hodge calculations. If it is retained syntactically
in the old `P_N^Loc` tuple, it is a fixed derived ambient entry, not a freely
varying datum and not a membership selector in the honest family.

### 1.4 Exact family definition

Let the already-displayed compatibility solution space be

```text
Sol_Loc
 :=Ext
    fiber-product_Gates Hdg
    fiber-product_Gates Tar
    fiber-product_Gates
      Product_N Hom(D_N^Loc,Sym_N^loc).         (C1a)
```

Here `Ext`, `Hdg`, and `Tar` have exactly the meanings in `(D12)` of the Loc
build, and the fiber-product gates are the retained stage, arrow, and
diamond equations enumerated below. The honest family is

```text
L_F2'
 := { (P_N^Loc)_N in Sol_Loc :

      D_N^Loc subset Sch_N(Op_N^(loc,2)),

      Op_N^(loc,2) is the declared properly supported
        classical pseudodifferential operator class
        of order <=2,

      for every K in D_N^Loc,
      Loc_N^phys(K)
       =[sigma_2^ker(K)]_Ctc_sym,

      kappa_T,N
       =Sch_N(M_N^loc)
        with the bundle, density, topology, and transport
        typing required in (S4) }.              (C1')
```

The label `F2` in `L_F2'` records the reader-free local Maxwell principal-
symbol construction and `(R9)`. It does **not** mean “Hodge-range blind” or
“harmonic projection zero.” Equivalently,

```text
(C1')
 =old (C1) minus STRIKE_FROM_C1,

(S28) notin membership(C1'),
not-(S28) notin membership(C1').                (C1b)
```

No member is selected by `(C1')`, and its nonemptiness is not proved.

### 1.5 Complete genuine-clause ledger

The phrase “all clauses” is resolved here so that an explanatory warning or
an unbuilt optional seam cannot become a membership predicate by accident.

| Clause block | Status in `(C1')` | Provenance and exact reading |
|---|---|---|
| `(S1),(S2),(S2a)` | ambient, not package choices | sealed profile and scoped Q-408 cycle branch |
| `(S13)` and projector intertwiners | ambient, not package choices | sealed `d/delta/P_H` carrier and naturality |
| `(S2b)`--`(S7)` | retained `[YOURS]` full-gate obligations | extension of Q-408 and the separate `L_T` branch; quotient descent and common topology must be proved by a member |
| `(S8)` | retained consequence, not an extra cut | the displayed direct-image expansion of `(S4)`--`(S7)` once those gates hold |
| `(S9),(S9a),(S10),(S11)` | retained `[YOURS]` target gates | symbol quotient, closed contact ideal, Maxwell split, and projection |
| `(S12)` | retained type discipline | `L_T`, `kappa_T`, the local symbol, and its Hodge image remain distinct objects |
| `(S14),(S19),(S21),(S25),(S25b)`, Hodge diamonds | retained exact Hodge fiber | linearity, contact descent, rank-preserving transport, old-image downward transport, and diamonds; no Hodge-range clause |
| `(S15),(S15a)` | retained `[YOURS]` map/type and symbol pin | `Loc^phys`, `Loc^C=iota^H Loc^phys`, and the independent unit Maxwell-symbol comparison |
| `(S15b)` | explanatory only | records that `(S15a)` does not imply `(S28)` |
| `(S16),(S16a),(S16b),(S16c)` | retained typing conventions | separate physical-symbol and bundled Hodge readings |
| `(S16d)` and `beta_N` | excluded from membership | explicitly unbuilt optional comparison seam; not a coordinate of the package |
| `(S17),(S17a)` | retained `[YOURS]` gates | typed finite-shadow recovery and component/test comparison |
| `(S18),(S20)`--`(S20e)` | retained `[YOURS]` gates | continuity/linearity, locality, Ward, long-wave, kernel, and record-visibility obligations |
| `(S22),(S22a),(S23),(S24),(S25a),(S25c)`--`(S25g)` | retained `[YOURS]` gates | rank-preserving, cycle-old-image, covariance, support, batching, and common-refinement laws |
| `(S26),(S27)` | retained dependency gates | reader-free forward construction and prohibited reverse dependencies |
| `(S28)` and every normalization of it | excluded | later structural end-test condition, neither construction premise nor family selector |
| old Hodge-range clause `(R10)` | struck | uninherited `not-(S28)` plus deletion of `ran(d^(k-1))` |

Every retained authored gate is independently premise-marked to its sealed
input: Q-408 for the old kernel branch, the Maxwell local operator and its
principal symbol for `(R9)`, DoR-019 for metric/unit typing, A5/projector
stock for the Hodge carrier, A1 for bundle/transport laws, and the sealed
assembly arrows for the naturality and diamond obligations. “Premise-marked”
does not mean “constructed”: these gates remain falsifiable obligations of a
future member.

```text
HONEST_FAMILY_DEFINITION = (C1')
OLD_RANGE_CLAUSE = STRUCK
SEED_POLARITY_IN_MEMBERSHIP = none
FULL_GATE_FAMILY_NONEMPTY = not proved
```

## 2. Y2 — can `(C1')` thread the harmonic line?

### 2.1 The exact subject, conditional on a member

[PART-PROVABLE] Let `L in L_F2'` be a future full-gate member. At any typed
stage `N`, `(R9)` gives the displayed chain

```text
m_T,N(L)
 :=P_H,N Loc_N^C(kappa_T,N)

 =P_H,N iota_N^H Loc_N^phys(kappa_T,N)

 =P_H,N iota_N^H(s_Max,N^unit).                 (T1)
```

Thus the exact unresolved cross-sector map and its value are

```text
B_N(L)
 :=(P_H,N compose iota_N^H)|_(Mx_N^sym)
   :Mx_N^sym->im(P_H,N),

HRoute_N(L)
 :=B_N(L)(s_Max,N^unit)
  =m_T,N(L).                                    (T2)
```

and `(T1)` is its value on the unit Maxwell symbol.

At the named reciprocal-loop stage `N_RL`, sealed cycle content supplies a
rank-one harmonic line

```text
im(P_H,RL)=span{c_RL},
c_RL != 0.                                      (T3)
```

Define, still conditional on `L`,

```text
q_T,RL(L)
 :=<iota_RL^H(s_Max,RL^unit),c_RL>_RL.          (T4)
```

The ratified metric is positive on the nonzero line, so

```text
<c_RL,c_RL>_RL != 0.                            (T5)
```

Rank-one orthogonal projection gives every intermediate equality:

```text
m_T,RL(L)
 =P_H,RL iota_RL^H(s_Max,RL^unit)

 =(<iota_RL^H(s_Max,RL^unit),c_RL>_RL
    /<c_RL,c_RL>_RL) c_RL

 =(q_T,RL(L)/<c_RL,c_RL>_RL)c_RL.               (T6)
```

Therefore, without evaluating either side,

```text
m_T,RL(L) != 0  iff  q_T,RL(L) != 0,
m_T,RL(L)  = 0  iff  q_T,RL(L)  = 0.            (T7)
```

`(T4)`, equivalently `(T2)` on `s_Max,RL^unit`, is the exact blocking
quantity.

### 2.2 The boundary that is already decided

[PROVABLE] At an acyclic stage `A`, there is no harmonic sector:

```text
im(P_H,A)={0}.                                  (T8)
```

For every future member and every typed input,

```text
m_T,A(L)
 =P_H,A iota_A^H(s_Max,A^unit)
 =0.                                            (T9)
```

This is structural vanishing on acyclic positions only. It does not decide
the cycle-carrying reciprocal stage `(T3)`.

### 2.3 Why the old vanishing proof no longer applies

The old proof began with `(R1)` and then used harmonicity:

```text
<delta_N^(k+1)d_N^k v,c_N>_N
 =<d_N^k v,d_N^k c_N>_N
 =<d_N^k v,0>_N
 =0.                                            (T10)
```

Equation `(T10)` remains a correct ambient operator identity. What is no
longer licensed is its first substitution:

```text
iota_N^H(s_Max,N^unit)
 =delta_N^(k+1)d_N^k v                          (UNAVAILABLE)
```

for some `v`. No genuine clause supplies that witness. Hence `(T10)` cannot
be applied to `(T4)`.

The other retained clauses also do not select a polarity:

```text
(S14),(S19):  iota^H is linear and continuous;
(S21):        iota^H descends through contact and lies in ker(E_C);
(S25):        a chosen Hodge image is transported on RP arrows;
(S25b):       only the old-image part is constrained downward;
(R8):         P_H commutes with certified transport;
(R9):         the symbol input is s_Max^unit.   (T11)
```

None of `(T11)` says that `(T2)` is the zero map or a nonzero map.

### 2.4 Displayed clause-separation pair

[PROVABLE — logical independence control, not an actual-surface member]
The following finite-dimensional pair shows that the genuine Hodge clauses,
including their arrow forms, do not themselves choose zero or nonzero.

At a cycle-carrying target `M`, take

```text
Sigma_M^(2),Ward
 =span{otilde,etilde,t},

Ctc_M^sym=span{t},

Sym_M^loc
 =Sigma_M^(2),Ward/Ctc_M^sym
 =span{o,e},

o:=[otilde]_Ctc_sym,
e:=[etilde]_Ctc_sym,

s_Max,M^unit=e.                                 (T12)
```

Take the displayed bases to be orthonormal and set

```text
C_M^k=span{r,u,h},
C_M^(k-1)={0},
C_M^(k+1)=span{r_plus,u_plus},

d_M^(k-1)=0,
d_M^k(r)=r_plus,
d_M^k(u)=u_plus,
d_M^k(h)=0,

delta_M^(k+1)(r_plus)=r,
delta_M^(k+1)(u_plus)=u,

delta_M^k=0,

all remaining displayed-degree d/delta maps are zero,

delta_M^(k+1)=(d_M^k)^*,

Delta_M^(Hdg,k)
 :=delta_M^(k+1)d_M^k+d_M^(k-1)delta_M^k,

Delta_M^(Hdg,k)(r)=r,
Delta_M^(Hdg,k)(u)=u,
Delta_M^(Hdg,k)(h)=0,

ker(Delta_M^(Hdg,k))=span{h},

P_H,M
 :=the orthogonal projector onto ker(Delta_M^(Hdg,k)),

P_H,M(h)=h,
P_H,M(r)=P_H,M(u)=0,

E_C,M=0.                                        (T13)
```

Then `im(P_H,M)=span{h}` and `h!=0`. For a symbolic scalar
`lambda!=0`, define two linear Hodge realizations:

```text
iotatilde_M^(0)(otilde)=r,
iotatilde_M^(0)(etilde)=u,
iotatilde_M^(0)(t)=0,

iotatilde_M^(lambda)(otilde)=r,
iotatilde_M^(lambda)(etilde)=u+lambda h,
iotatilde_M^(lambda)(t)=0.                      (T14)
```

Both descend through the contact quotient:

```text
iota_M^(0)(o)=r,
iota_M^(0)(e)=u,

iota_M^(lambda)(o)=r,
iota_M^(lambda)(e)=u+lambda h.                  (T15)
```

They satisfy `(S21)` because

```text
Ctc_M^sym subset ker(iotatilde_M^(0))
                 intersection
                 ker(iotatilde_M^(lambda)),

(1-E_C,M)iota_M^(0)=iota_M^(0),
(1-E_C,M)iota_M^(lambda)=iota_M^(lambda),

[E_C,M,Delta_M^Hdg]=0.                          (T16)
```

For a cycle-creating arrow `a:A->M`, take the acyclic source

```text
Sigma_A^(2),Ward=span{otilde_A,t_A},
Ctc_A^sym=span{t_A},
Sym_A^loc=span{o_A},
o_A:=[otilde_A]_Ctc_sym,

C_A^k=span{r_A},
C_A^(k+1)=span{r_A_plus},
C_A^(k-1)={0},

d_A^k(r_A)=r_A_plus,
delta_A^(k+1)(r_A_plus)=r_A,
delta_A^k=0,

Delta_A^(Hdg,k)
 :=delta_A^(k+1)d_A^k,
Delta_A^(Hdg,k)(r_A)=r_A,
ker(Delta_A^(Hdg,k))={0},

P_H,A=0,
E_C,A=0,

iotatilde_A^H(otilde_A)=r_A,
iotatilde_A^H(t_A)=0,
iota_A^H(o_A)=r_A.                             (T17a)
```

The source bases are orthonormal, so
`delta_A^(k+1)=(d_A^k)^*` and the harmonic sector is zero. Type the old
target and downward arrows as

```text
Sym_M^old=span{o},
C_M^(k,old)=span{r},

rho_a^Sym:Sym_M^old->Sym_A^loc,
rho_a^C:C_M^(k,old)->C_A^k,

rho_a^Sym(o)=o_A,
rho_a^C(r)=r_A,

iota_M^(theta)(Sym_M^old)
 subset C_M^(k,old)
 for theta in {0,lambda}.                       (T17)
```

For every scalar `b`, the `(S25b)` square is identical for both
realizations:

```text
rho_a^C iota_M^(0)(b o)
 =rho_a^C(b r)
 =b r_A
 =iota_A^H(b o_A)
 =iota_A^H rho_a^Sym(b o),                      (T18a)

rho_a^C iota_M^(lambda)(b o)
 =rho_a^C(b r)
 =b r_A
 =iota_A^H(b o_A)
 =iota_A^H rho_a^Sym(b o).                      (T18b)
```

The target-new direction `e` is outside the domain of the downward
old-image square and is therefore not constrained by `(T18)`.

For a nonidentity rank-preserving copy `f:M->M'`, let `M'` be a full primed
copy of `(T12)`--`(T16)`, including `r_plus'` and `u_plus'`, and transport
the displayed bases by

```text
j_f^Sym(o)=o',
j_f^Sym(e)=e',

j_f^C(r)=r',
j_f^C(u)=u',
j_f^C(h)=h',

j_f^(C,k+1)(r_plus)=r_plus',
j_f^(C,k+1)(u_plus)=u_plus'.                    (T19)
```

The copy model also has the following forward commutation equalities on the
bases:

```text
d_M'^k j_f^C(r)=d_M'^k(r')=r_plus'
 =j_f^(C,k+1)(r_plus)=j_f^(C,k+1)d_M^k(r),

d_M'^k j_f^C(u)=d_M'^k(u')=u_plus'
 =j_f^(C,k+1)(u_plus)=j_f^(C,k+1)d_M^k(u),

d_M'^k j_f^C(h)=d_M'^k(h')=0
 =j_f^(C,k+1)(0)=j_f^(C,k+1)d_M^k(h),

delta_M'^(k+1)j_f^(C,k+1)(r_plus)
 =delta_M'^(k+1)(r_plus')=r'
 =j_f^C(r)=j_f^C delta_M^(k+1)(r_plus),

delta_M'^(k+1)j_f^(C,k+1)(u_plus)
 =delta_M'^(k+1)(u_plus')=u'
 =j_f^C(u)=j_f^C delta_M^(k+1)(u_plus),

P_H,M' j_f^C(r)=0=j_f^C P_H,M(r),
P_H,M' j_f^C(u)=0=j_f^C P_H,M(u),
P_H,M' j_f^C(h)=h'=j_f^C P_H,M(h),

E_C,M' j_f^C=0=j_f^C E_C,M.                    (T19a)
```

To match the sealed projector certificate's contravariant signature, define
the inverse basis maps

```text
rho_f^(C,k):C_M'^k->C_M^k,
rho_f^(C,k)(r')=r,
rho_f^(C,k)(u')=u,
rho_f^(C,k)(h')=h,

rho_f^(C,k+1):C_M'^(k+1)->C_M^(k+1),
rho_f^(C,k+1)(r_plus')=r_plus,
rho_f^(C,k+1)(u_plus')=u_plus.                  (T19b)
```

The three certificate directions are displayed basiswise:

```text
rho_f^(C,k+1)d_M'^k(r')
 =rho_f^(C,k+1)(r_plus')
 =r_plus
 =d_M^k(r)
 =d_M^k rho_f^(C,k)(r'),

rho_f^(C,k+1)d_M'^k(u')
 =rho_f^(C,k+1)(u_plus')
 =u_plus
 =d_M^k(u)
 =d_M^k rho_f^(C,k)(u'),

rho_f^(C,k+1)d_M'^k(h')
 =rho_f^(C,k+1)(0)
 =0
 =d_M^k(h)
 =d_M^k rho_f^(C,k)(h'),

rho_f^(C,k)delta_M'^(k+1)(r_plus')
 =rho_f^(C,k)(r')
 =r
 =delta_M^(k+1)(r_plus)
 =delta_M^(k+1)rho_f^(C,k+1)(r_plus'),

rho_f^(C,k)delta_M'^(k+1)(u_plus')
 =rho_f^(C,k)(u')
 =u
 =delta_M^(k+1)(u_plus)
 =delta_M^(k+1)rho_f^(C,k+1)(u_plus'),

rho_f^(C,k)P_H,M'(r')=0=P_H,M(r)
 =P_H,M rho_f^(C,k)(r'),

rho_f^(C,k)P_H,M'(u')=0=P_H,M(u)
 =P_H,M rho_f^(C,k)(u'),

rho_f^(C,k)P_H,M'(h')
 =rho_f^(C,k)(h')
 =h
 =P_H,M(h)
 =P_H,M rho_f^(C,k)(h').                      (T19c)
```

Hence, as map equalities on the displayed carriers,

```text
rho_f^(C,k+1)d_M'^k
 =d_M^k rho_f^(C,k),

rho_f^(C,k)delta_M'^(k+1)
 =delta_M^(k+1)rho_f^(C,k+1),

rho_f^(C,k)P_H,M'
 =P_H,M rho_f^(C,k).                            (T19d)
```

The two `(S25)` base squares are displayed on the Maxwell direction as

```text
iota_M'^(0) j_f^Sym(e)
 =iota_M'^(0)(e')
 =u'
 =j_f^C(u)
 =j_f^C iota_M^(0)(e),                          (T20a)

iota_M'^(lambda) j_f^Sym(e)
 =iota_M'^(lambda)(e')
 =u'+lambda h'
 =j_f^C(u+lambda h)
 =j_f^C iota_M^(lambda)(e).                     (T20b)
```

For `theta in {0,lambda}` and `s=b o+d e`, the whole RP square is

```text
iota_M'^(theta) j_f^Sym(s)
 =iota_M'^(theta)(b o'+d e')
 =b r'+d(u'+theta h')
 =j_f^C(b r+d(u+theta h))
 =j_f^C iota_M^(theta)(s).                      (T20c)
```

The identity and one composition step are, with every intermediate equality
displayed,

```text
iota_M^(theta) j_id^Sym
 =iota_M^(theta) id_Sym
 =iota_M^(theta)
 =id_C iota_M^(theta)
 =j_id^C iota_M^(theta),                        (T20d)

iota_L^(theta) j_gf^Sym
 =iota_L^(theta) j_g^Sym j_f^Sym
 =j_g^C iota_M^(theta) j_f^Sym
 =j_g^C j_f^C iota_N^(theta)
 =j_gf^C iota_N^(theta).                        (T20e)
```

On a Hodge diamond `g_1 f_1=g_2 f_2`, define the copy transports by the
common terminal basis. For a generic symbol `s` and cochain `v`, this gives

```text
j_g1^Sym j_f1^Sym(s)
 =s_P
 =j_g2^Sym j_f2^Sym(s),

j_g1^C j_f1^C(v)
 =v_P
 =j_g2^C j_f2^C(v).                            (T20f-0)
```

The two Hodge-realization routes are then

```text
iota_P^(theta)j_g1^Sym j_f1^Sym
 =j_g1^C iota_M1^(theta)j_f1^Sym
 =j_g1^C j_f1^C iota_N^(theta)

 =j_g2^C j_f2^C iota_N^(theta)

 =j_g2^C iota_M2^(theta)j_f2^Sym
 =iota_P^(theta)j_g2^Sym j_f2^Sym.              (T20f)
```

The middle equality is the displayed cochain-transport diamond equation;
the two outer chains use `(T20c)`. Thus both realizations satisfy the same
identity, composition, and Hodge-diamond laws. Their harmonic outputs are
different:

```text
P_H,M iota_M^(0)(s_Max,M^unit)
 =P_H,M(u)
 =0,                                            (T21a)

P_H,M iota_M^(lambda)(s_Max,M^unit)
 =P_H,M(u+lambda h)
 =lambda h
 !=0.                                           (T21b)
```

The old range clause accepted `(T21a)` and excluded `(T21b)`. The genuine
Hodge clauses displayed in `(T12)`--`(T20)` accept both.

This pair is a **clause-separation model only**. It is not asserted to be an
actual surface, an element of the full assembly category, or a member of
`L_F2'`; it therefore does not bind a member or establish outcome Y2(a).
Its role is exactly to refute an inference from the genuine Hodge clauses
alone to either seed polarity.

### 2.5 The family-level free direction

[PART-PROVABLE] The Hodge-fiber freedom has the following display without
choosing a value. For a future member `L^0 in L_F2'`, define the admissible
Hodge-fiber correction space

```text
HNat_Hdg(L^0)
 :={ (h_N)_N :
      h_N:Sym_N^loc
          ->im(P_H,N) intersection ker(E_C,N)
        is continuous, linear, and reader-free;

      h_M j_f^Sym=j_f^C h_N
        on every certified rank-preserving arrow;

      h_M(Sym_M^old) subset C_M^(k,old)
        on every cycle-creating arrow;

      rho_a^C h_M|_(Sym_M^old)
       =h_N rho_a^Sym
        on every cycle-creating old-image square;

      every Hodge covariance, restriction,
        composition, and diamond equation holds }.             (T22)
```

For `h in HNat_Hdg(L^0)` and symbolic scalar `lambda`, set

```text
iota_N^(H,lambda)
 :=iota_N^(H,0)+lambda h_N,

q_N^sym:Sigma_N^(2),Ward->Sym_N^loc,
q_N^sym(s):=[s]_Ctc_sym,

iotatilde_N^(H,lambda)
 :=iotatilde_N^(H,0)+lambda h_N q_N^sym.         (T23)
```

For `t in Ctc_N^sym`, quotient descent and off-contact range are displayed:

```text
iotatilde_N^(H,lambda)(t)
 =iotatilde_N^(H,0)(t)+lambda h_N(q_N^sym(t))
 =0+lambda h_N(0)
 =0,

Ctc_N^sym subset ker(iotatilde_N^(H,lambda)),

(1-E_C,N)iota_N^(H,lambda)
 =(1-E_C,N)iota_N^(H,0)
   +lambda(1-E_C,N)h_N

 =iota_N^(H,0)+lambda h_N
 =iota_N^(H,lambda).                            (T23a)
```

For arbitrary `s in Sigma_N^(2),Ward`, the prequotient map descends to the
specific map in `(T23)`:

```text
iotatilde_N^(H,lambda)(s)
 =iotatilde_N^(H,0)(s)+lambda h_N(q_N^sym(s))

 =iota_N^(H,0)(q_N^sym(s))
   +lambda h_N(q_N^sym(s))

 =iota_N^(H,lambda)(q_N^sym(s)).                (T23b)
```

Every equality in `(T22)` is linear, so the displayed rank-preserving
calculation is

```text
iota_M^(H,lambda) j_f^Sym
 =(iota_M^(H,0)+lambda h_M)j_f^Sym

 =iota_M^(H,0)j_f^Sym
   +lambda h_M j_f^Sym

 =j_f^C iota_N^(H,0)
   +lambda j_f^C h_N

 =j_f^C(iota_N^(H,0)+lambda h_N)

 =j_f^C iota_N^(H,lambda).                      (T24)
```

On a cycle-creating old-image square, the corresponding downward chain is

```text
rho_a^C iota_M^(H,lambda)|_(Sym_M^old)
 =rho_a^C iota_M^(H,0)|_(Sym_M^old)
   +lambda rho_a^C h_M|_(Sym_M^old)

 =iota_N^(H,0)rho_a^Sym
   +lambda h_N rho_a^Sym

 =(iota_N^(H,0)+lambda h_N)rho_a^Sym

 =iota_N^(H,lambda)rho_a^Sym.                   (T24a)
```

The old-image containment required before that downward square is

```text
iota_M^(H,lambda)(Sym_M^old)
 subset iota_M^(H,0)(Sym_M^old)
         +lambda h_M(Sym_M^old)

 subset C_M^(k,old)+C_M^(k,old)

 =C_M^(k,old).                                  (T24b)
```

At the reciprocal stage, its effect on the blocking quantity is

```text
q_T,RL(lambda)
 =<iota_RL^(H,lambda)(s_Max,RL^unit),c_RL>_RL

 =q_T,RL(0)
   +lambda<h_RL(s_Max,RL^unit),c_RL>_RL.        (T25)
```

Sealed stock constructs neither `L^0` nor a nonzero member of
`HNat_Hdg(L^0)`, and it proves neither that `HNat_Hdg(L^0)={0}` nor that the
last pairing in `(T25)` vanishes. Equations `(T22)`--`(T25)` classify only
an admissible Hodge-fiber correction. They do not assert that every other
`C1'` gate remains satisfied. Equation `(T25)` is a conditional freedom
calculation, not a selected correction.

### 2.6 Exhaustion of the three Y2 outcomes

**Outcome (a), member displayed, is not licensed.** A displayed nonzero
clause-separation model is not a full-gate surface member. The actual source
extension, target split, `iota^H`, nonidentity base squares, and all other
`Sol_Loc` gates have no single sealed inhabitant.

**Outcome (b), vanishing re-proved, is not licensed on cycle-carrying
stages.** The only former bridge into `ran(delta d)` was `(R10)`, now struck.
Equations `(T21a)`--`(T21b)` show that the genuine Hodge clauses do not
replace it. Vanishing remains proved only on the acyclic boundary `(T8)`--
`(T9)`.

**Outcome (c), undetermined, is forced by the present record.** At the
cycle-carrying reciprocal stage, the subject is conditional on inhabitance
and the exact harmonic coordinate `(T4)` is fixed by no genuine clause.
Neither zero nor nonzero is asserted.

```text
Y2_OUTCOME = (c) UNDETERMINED
BLOCKING_MAP = B_RL(L)
BLOCKING_QUANTITY =
  q_T,RL(L):=<iota_RL^H(s_Max,RL^unit),c_RL>_RL
ACYCLIC_BOUNDARY = VANISHING
CYCLE_CARRYING_MEMBER_INHABITANCE = NOT_ESTABLISHED
S28_ASSUMED = false
NOT_S28_ASSUMED = false
```

## 3. Y3 — consequence board

### 3.1 All three mathematical outcomes

The following board separates the logical consequences of Y2(a), Y2(b),
and Y2(c). It does not promote the two counterfactual rows to facts.

| Consequence | Y2(a): full member and nonzero route displayed | Y2(b): vanishing from genuine clauses re-proved | Y2(c): undetermined — actual |
|---|---|---|---|
| Seed | The subject is defined for that member and the named nonzero stage inhabits the seed support. Nonvanishing does not propagate beyond arrows on which all transport and generator compatibilities are proved. | A formed member has zero seed on the theorem's stated scope; if the family is empty, even the subject remains uninstantiated. No division by the zero route is permitted. | `SEED_TYPE=END_TEST_STRUCTURAL`; the conditional subject is `(T1)` and condition `(T7)` is carried but not evaluated. |
| J2 premise board | A full member instantiates extended `Kernbarhat`, physical `Loc`, linearity, and its certified `(F2)/(F3)` squares. Generic `(F1)` quotient identification, the scalar/bottom seam `(S16d)`, and the independent reader equalizer still remain; J2 is not automatically proved. | A member may instantiate maps, but the rank-one coefficient normalization cannot form on the proved-zero scope. The independent `(F1)` and comparison debts remain. | No new premise. `(F1)` remains subscope, `(F2)` remains represented-old only outside an instantiated package, physical `(F3)` remains uninstantiated, and projector `(F4)` alone is proved. |
| Coefficient face | For the fixed member, the rank-one face contains the displayed nonzero stage and any separately proved compatible nonzero transport support. The `tau_r`, response-tuple, and diamond-route equalities remain independent debts. | The face has no formable coefficient denominator on the proved-zero scope. This is an unmet demand, not a vacuous proof of the face. | For each fixed future member `L`, the face remains conditional on `A_RP^+(L)`; inhabitance is not established. |
| A1 amendment | Not needed for the intrinsic C1' seed furnished by that member. It is still required before claiming any separate `Hol_N` summand from A1. | Needed if the program pursues the separately added holonomy route; current A1 cannot type it. | Needed for any `Hol_N` route, but not consumed merely to state or continue testing `(C1')`. |
| J7 ruling | For the fixed member, quantify only over FC11 squares whose four positions lie in its proved nonzero `A_RP^+(L)` support and whose four transport legs are rank-preserving. The `tau_r`, response-tuple, and diamond-route equations still require their own displays. | The honest-family support is empty on the proved-zero subfamily; J7 cannot replace the missing face by J2 or call it discharged. An enlarged family would require new authority. | For each fixed future member `L`, quantify intensionally over every FC11 square wholly in `A_RP^+(L)`; make no inhabitance assertion. `A_CC` old-image positions retain only the weaker A6 comparison, target-new-cycle positions remain post-scope, and unclassified arrows carry no verdict. |

Two separations are load-bearing:

```text
a typed route exists  -/->  its reciprocal pairing is nonzero,

a nonzero seed         -/->  the independent J2/J7
                              route equalities are proved.       (Y1)
```

### 3.2 Actual board after outcome (c)

```text
SEED_TYPE
 = END_TEST_STRUCTURAL

SEED_SUBJECT_OF_RECORD
 = undefined
   (+well-typed condition (T4) for any future member;
    +no member bound)

J2_RP_PREMISES
 = INCOMPLETE
   (+generic (F1) quotient descent/identification;
    +extended Kernbarhat and physical (F2)/(F3) member;
    +map-level construction/linearity;
    +scalar-vs-bottom comparison seam;
    +independent reader equalizer)

COEFFICIENT_FACE_BASIS
 = CONDITIONAL_ONLY

A_RP_PLUS(L)
 := { N in Ob(A_RP) : m_T,N(L) != 0 },          (Y2)

A_RP_PLUS_INHABITANCE
 = NOT_ESTABLISHED
   (+no full-gate member of record and no seed theorem)

J7_QUANTIFIER
 = for every fixed L in L_F2', every FC11 square whose
     four stage positions lie in A_RP_PLUS(L) and whose
     four legs lie in A_RP;
   A_CC-old carries only its explicitly weaker A6 comparison;
   A_CC-new remains post-scope;
   unclassified arrows carry no verdict

J7_ACTUAL_DISCHARGE_FROM_THIS_ARTIFACT
 = none.                                        (Y3)
```

### 3.3 A1 is a separate provenance question

[PROVABLE — inherited review verdict] Current A1 supplies a bundle with
connection and transport derived from declared members. It does not supply
the map demanded by an added holonomy localization:

```text
Hol_N:D_N^Loc -> im(P_H,N).                     (Y4)
```

The missing first bridge is

```text
Xi_N:D_N^Loc
      ->{record-visible cycles}
       or H^1,                                  (Y5)
```

followed by a unit conversion from a circle-valued phase or connection
period into the DoR-019 Hodge carrier, plus covariance, restriction,
falsifiers, and an inhabited witness. The review therefore establishes

```text
HOL_PROVENANCE = A1_AMENDMENT_NEEDED.           (Y6)
```

No amendment is drafted, adopted, or inhabited here. Equations `(Y4)`--
`(Y6)` concern a **separately appended** holonomy route. They do not imply
that the intrinsic map `(T2)` vanishes, and they do not change outcome (c).

## 4. Y4 — battery

### 4.1 F_PLDEC and false-anchor regression

The compressed allowed dependency graph used by `(C1')` is

```text
Q-408 old kernel + candidate L_T common-kernel realization
                       subject to (S3)--(S7)
 + local Maxwell operator/principal symbol
 + DoR-019 metric/unit classes
 + A5/projector Hodge carrier
 + A1/assembly transport laws

 -> Ext, Tar, Hdg, and their full-gate compatibility fiber

 -> L_F2'

 -> conditional HRoute_N and q_T,N.             (B1)
```

The prohibited graph remains

```text
algebraic reader / chi / reader T / desired coefficient
 / (FALSE-ANCHOR) / S28 / not-(S28)

 -/-> Ext, Tar, Hdg, Loc^phys, iota^H,
      membership(C1'), or a member-selection rule.              (B2)
```

The clause-separation scalar `lambda` in `(T14)` is not selected and is not
an input to `(C1')`; it is a symbolic witness that two logical models of the
retained Hodge equations exist. No output or measured constant fixes it.

```text
READER_USED_TO_BUILD_C1_PRIME = false
FALSE_ANCHOR_CONSUMED = false
SEED_POLARITY_CONSUMED = false
F_PLDEC = CLEAN
```

### 4.2 Fourteen void conditions rechecked on `(C1')`

This is a scope/design audit. “Retained” means the condition remains a
genuine falsifier of a future candidate; it does not assert that an
unconstructed member has passed it.

| No. | `(C1')` void/falsifier | Recheck |
|---:|---|---|
| 1 | `Sch_N` or `kappa_T,N` cannot be realized with the fixed bundle/density convention in the common kernel topology; the two `(S7)` topologies differ; or `(S2b)` fails continuity, injectivity, or naturality. | RETAINED; source/common-topology falsifier, seed-blind. |
| 2 | `Krawhat_N(Rel_N)` contains a nonzero element. | RETAINED; exact quotient-descent falsifier. |
| 3 | A Q-408 kernel is not properly supported or lies outside the symbol domain, including failure of required diagonal-pullback wavefront transversality. | RETAINED; PDO-domain falsifier. |
| 4 | `Sym_N^loc`, the closed `Ctc_N^sym`, or split `(S10)` does not exist, or the independent symbol computation fails `(S15a)`. | RETAINED; target/symbol-pin falsifier; it does not mention the harmonic coordinate. |
| 5 | No reader-free `iota_N^H` satisfies `(S14),(S19),(S21),(S25),(S25b)` and every Hodge diamond. | RETAINED and sharpened to the exact Hodge fiber; no range condition added. |
| 6 | Either nonidentity base square `(S23)`--`(S25)` fails on the reciprocal generator or on the nontrivial `q=2` refinement generator. | RETAINED; the current lack of a member leaves it an open gate. |
| 7 | The shadow construction/comparison, Ward/contact law, units, reality, support, restriction, batching, any retained stage/arrow gate, or any common-refinement/Hodge diamond fails. | RETAINED; completed to every genuine diamond gate. |
| 8 | A contact quotient deletes a record-visible cycle kernel. | RETAINED; record-visibility falsifier. |
| 9 | A cycle-creating arrow is assigned an unlicensed canonical upward lift. | RETAINED; asymmetry falsifier. |
| 10 | Any construction input or member rule references the algebraic reader, `chi`, reader `T`, a desired coefficient, or `(FALSE-ANCHOR)`. | RETAINED; F_PLDEC falsifier. |
| 11 | A hidden smoothing scale, measure, contour, boundary condition, frame, Cauchy slice, gauge representative, or cross-sector unit is required. | RETAINED; anti-tuning/provenance falsifier. |
| 12' | The construction or membership rule uses the value or zero/nonzero status of `HRoute_N` or `q_T,N` as an admission/selection criterion, assumes `(S28)` or `not-(S28)`, or silently appends `Hol_N` without separately declaring the enlarged family and proving provenance, units, covariance, restriction, and falsifiers. | REPLACES old void 12. Intrinsic harmonic image through ordinary `iota^H` is allowed; seed-polarity selection is void. `(C1')` passes this syntax check. |
| 13 | The field symbol or limit `(S20a)` does not exist in the named topology, changes under a certified restriction/realization, or fails `(S20b)`. | RETAINED; field/limit falsifier. |
| 14 | A kernel or Q-396 intersection in `(S20c)`--`(S20d)` remains undisclosed, or record-visible injectivity `(S20e)` fails without an independent physical-kernel theorem. | RETAINED; kernel/visibility falsifier. |

The old void 12 was

```text
P_H,N iota_N^H Loc_N^phys(kappa_T,N) != 0
  => member void.                               (OLD-V12)
```

`(OLD-V12)` is struck. It was the dual enforcement of the deleted range
clause and would reject precisely outcome Y2(a). The review's proposed
scope falsifier—an otherwise full-gate package that fails the old range
clause—is now intentionally reversed: such a package is admitted by
`(C1')` and tested by `(T4)` rather than discarded.

```text
VOID_CONDITIONS_RECHECKED = 14
OLD_VOID_12 = STRUCK
NEW_VOID_12_PRIME = SEED_POLARITY_OR_UNDECLARED_HOL_SELECTION
```

### 4.3 Anti-tuning ledger

| Hazard | Control | Result |
|---|---|---|
| choose a family member after seeing the seed | family retained whole; no member bound | clean |
| force zero by a Hodge-range clause | `(R10)` and `(OLD-V12)` struck | clean |
| force nonzero by adding `(S28)` | `(S28)` excluded from membership and construction | clean |
| tune the formal correction parameter | `lambda` is symbolic and unselected; `(T22)`--`(T25)` are conditional only | clean |
| choose a scale, slice, contour, gauge, frame, or hidden unit | void 11 retained | clean |
| normalize with the algebraic reader or target coefficient | prohibited graph `(B2)` and void 10 | clean |
| infer holonomy from curvature | separate `Xi/Hol` provenance gap retained in `(Y4)`--`(Y6)` | clean |
| treat a typed route as nonzero | `(T7)` keeps nonvanishing as a separate condition | clean |
| extend a result from acyclic to cycle-carrying stages | exact boundary `(T8)`--`(T9)` | clean |
| compare to a measured constant | no numeric evaluation or measured comparison | clean |

### 4.4 Self verb audit

| Verb/claim | Display above it | Audit |
|---|---|---|
| `HONEST_FAMILY = stated` | exact family `(C1')`, set difference `(C1b)`, and complete clause ledger | clean |
| range clause `STRUCK` | exact predicate `(R10)` and its force `(R1)`--`(R6)` | clean |
| “nothing lawful forces it” | exact Hodge fiber `(R7)`, clause displays, and absent bridge | clean; no stock-wide impossibility claimed |
| `THREADING = UNDETERMINED` | blocking map `(T2)`, quantity `(T4)`, projection `(T6)`, clause-separation pair `(T12)`--`(T21)`, and exhaustion §2.6 | clean |
| acyclic `VANISHING` | `im(P_H,A)={0}` and arrowwise value `(T8)`--`(T9)` | clean; scope stated |
| `A1_AMENDMENT = needed` | inherited review verdict and exact gaps `(Y4)`--`(Y6)` | clean; no amendment authored/adopted |
| `MACHINERY_APPEAL = true` | no full-gate member of record and no zero/nonzero theorem for `B_RL(L)(s_Max,RL^unit)` | clean; exact witness stated, work continues structurally |
| fourteen voids `rechecked` | row-by-row transfer table and replaced void 12' | clean; no member claimed to pass open gates |
| `F_PLDEC = CLEAN` | allowed/prohibited graphs `(B1)`--`(B2)` | clean |
| anti-tuning `clean` | hazard/control ledger | clean |

Every operative verb in the audit is scoped to its displayed witness and
declared domain.

```text
MEMBER_BOUND = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false
MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = true
  (+no sealed full-gate C1' member;
   +no theorem fixes B_RL(L)(s_Max,RL^unit)
      to zero or nonzero)
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

HONEST_FAMILY = stated (+struck clauses: old `(C1)` Hodge-range predicate `(R10)` and its dual old void 12; neither `(S28)` nor `not-(S28)` is a member condition)
THREADING = UNDETERMINED (+blocking quantity `q_T,RL(L):=<iota_RL^H(s_Max,RL^unit),c_RL>_RL` for a future `L in L_F2'`; acyclic stages vanish, cycle-carrying reciprocal stage and family inhabitance remain open)
A1_AMENDMENT = needed (+for any separately appended `Hol_N` route: `Xi_N` domain correspondence, units, covariance/restriction/falsifiers, and witness; not drafted or adopted here)
VERB_AUDIT_SELF = CLEAN
