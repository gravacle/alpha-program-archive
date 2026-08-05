# STAGE 8 / TASK 5 / EQ6 — FAMILY V003 DISPLAY REPAIRS AND THE CONTACT ACTION ON THE LOOP

Date: 2026-08-05  
Lane: Codex Lane 3 (SOL, high effort)  
Task: PASTE 575 / Task 5 / EQ6  
Custody: builder repair for Dario cross-family review

## Lead determination

```text
REGISTER_HEAD = Q-499

DISPLAY_REPAIRS
 = DONE
   (+full (S21) restored;
    +old void 12 deleted at (C1b) and entered in the ledger;
    +the E_C route added to the Y2 exhaustion)

E_C_ON_LOOP
 = AUTHORABLE
   (+the sealed laws derive exactly
       E_C,RL c_RL in {0,c_RL};
    +they do not decide which contact-incidence branch is actual;
    +the minimal gate is the basis-free Boolean classification
       H_RL subset (I_contact,RL^k)^perp
       versus
       H_RL subset I_contact,RL^k)

THREADING
 = UNDETERMINED
   (+identity branch E_C,RL c_RL=c_RL forces reciprocal vanishing
       family-wide;
    +zero branch E_C,RL c_RL=0 leaves the pairing q_T,RL(L)
       and full-gate inhabitance unresolved)

E_C_VALUE_DIRECTION
 = AMBIENT_STRUCTURAL_INPUT_CONSUMED_UPSTREAM
   (+the map and subject are typed;
    +the reciprocal incidence value is not derived;
    +it is not produced by the loop;
    +therefore not an END_TEST datum)

MEMBER_BOUND = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false
MEASURED_CONSTANT_COMPARISON = none

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The determination was opened by asking what the sealed carrier and contact
split decide. No proof demand for either value was assumed. The answer is a
derived dichotomy and an unchosen structural incidence bit. This artifact
does not adopt that bit.

## 0. Preflight, authorities, version rule, and fences

### 0.1 Preflight

The access checks succeeded. Before any source was read, the review artifact
and its sidecar were verified at the commissioned hash. The no-clobber check
found neither this output nor its seal in the cleanroom or archive workspace.

```text
register head                                  = Q-499
register SHA-256                               =
  ae325be7cf838802e3d75869558a331ba17c940cf96db10c59d0679b5d505297

V002 family SHA-256                            =
  c4826773456c68972c1f70f5aea5a8ca8387b1b61c55923fd4f3902aaccf1b41

Dario family review SHA-256                    =
  9c232579d2953f3810ecd0b725555076be8820a99c3008e7f06ac06540f189ea

output absent before construction              = true
output seal absent before construction         = true
```

### 0.2 Sealed authority ledger

| Authority | Verified SHA-256 | Use here |
|---|---|---|
| `STAGE8_TASK5_EQ6_LOC_FAMILY_V002_LANE3_V001.md` | `c4826773456c68972c1f70f5aea5a8ca8387b1b61c55923fd4f3902aaccf1b41` | family text under repair |
| `STAGE8_TASK5_EQ6_LOC_FAMILY_REVIEW_DARIO_V001.md` | `9c232579d2953f3810ecd0b725555076be8820a99c3008e7f06ac06540f189ea` | K1/K2/K5/K6 findings |
| `STAGE8_TASK5_EQ6_THE_LOC_BUILD_LANE3_V001.md` | `b53d9e931efe1ebde333ef49fb4243e41917bb5d467f5a86e7052102ae5a0310` | full `(S21)` and Loc-family typing |
| `DOR_020_A4_J12_CONTACT_GLUE_STRICT_PUSHOUT_2026-08-04.md` | `5fd95472bd6f0507a371779505fe91e2c3c4657ee3afc664ca563a3743d668a4` | actual contact overlap and strict pushout |
| `DOR_020_A5_CONTACT_LAPLACIAN_REDUCING_2026-08-04.md` | `5beccc617f4c5f5f76aba777c664f3dd4393f72257fc850950e2246109a7a424` | adopted reducing law and voids |
| `DOR_019_CARRIER_METRIC_AND_UNITS_RATIFICATION_2026-08-03.md` | `6ab72b0cb3a93e123eb1d3c5088fc83361d86c6dc739f0a886380dbd2d143f1f` | positive finite carrier metric and orthogonal projection |
| `STAGE8_TASK5_EQ6_PROJECTOR_LOCALITY_REDUCING_CERT_V002_LANE1_V001.md` | `c81f61c4921275f1e38edd1c48c698788523e5f3ab5960b611b106dc2b66d837` | `E_C` typing and functional calculus |
| `STAGE8_TASK5_EQ6_PROJECTOR_CERT_V003_LANE1_V001.md` | `0bef9a003abb586666535689e98d7af29e7fc75b81e06fe439397ce2b8ef9100` | finite Hodge carrier and reciprocal touchstone |
| `STAGE8_TASK5_EQ6_MAXWELL_HODGE_PROJECTOR_CERT_LANE2_V001.md` | `f074ca24e8b96c576f5c64b856377f39ed8d4fc729c02cbf591326322558f816` | actual rank-one reciprocal harmonic line and contact boundary |
| `STAGE8_TASK5_EQ6_JOINT_FINITE_ASSEMBLY_STAGE1_LANE1_V003.md` | `a46beae26048a0d093de339363fb8597d362a0101d103cfc06305edabac53f4c` | pushout injection/no-deletion calculation |
| `STAGE8_TASK5_R4_KERNEL_REALIZATION_AND_SYMBOL_CALCULUS_LANE2_V001.md` | `ccb94dfa8927cf8d2ec76cf85ff2f402d02d5aa5673b9d39c214a6de4c92309c` | reciprocal current, homogeneous Ward law, and missing contact/Hodge split |
| `STAGE8_TASK5_EQ6_TWO_LEMMAS_LANE3_V001.md` | `48616c239ccdd777d1ac7cf5a049f324b98ca6abdba84966c5dc98151c461de4` | named nonzero reciprocal harmonic line |

The review was read first. DoR-020-A5 is ratified. Its exact force is an
ambient stage law: at every admitted finite stage, the *actual* degree-`k`
contact subspace has an orthogonal projector reducing the Hodge Laplacian,
and “no member ... is selected.” The Loc build confirms the custody:
`Hdg` varies only `(iotatilde_N^H,iota_N^H)_N`; `(S21)` references the
already ambient `E_C,N`, which is not a Loc-family coordinate. What remains
unbuilt is not an `E_C` package instance but the reciprocal contact-incidence
certificate that decides its action on `H_RL`. A4's response contact leg and
A5's degree-`k` contact subspace are kept typed separately below; no
cross-carrier identification is inferred from the shared word “contact.”

### 0.3 Claim tags

```text
PROVABLE
 = forced by the displayed sealed definitions or finite linear algebra;

PART-PROVABLE
 = a displayed consequence conditional on a future full-gate family member,
   or a clause-separation calculation not promoted to an actual member;

YOURS
 = candidate gate syntax or audit control introduced here;
   it is not an adopted law and does not choose a branch.
```

### 0.4 V003 version rule — exactly three repairs

The family revision is defined by replacement, not by silent restatement:

```text
V003_FAMILY_TEXT
 :=V002_FAMILY_TEXT
   with exactly the following family-display repairs:

   P1  replace the abbreviated (S21) block by the full block in Section 1.1;
   P2  replace (C1b) and its ledger entry by Section 1.2;
   P3  replace the Y2 outcome-(b)/(c) exhaustion by Section 1.3.

UNCHANGED_FROM_V002
 :=every other family predicate, domain, topology, map type, arrow law,
   diamond law, void condition other than the old/new void-12 bookkeeping,
   consequence debt, and no-selection fence.                       (V3-0)
```

The Z2 determination and Z3 board below analyze the repaired family; they do
not add a membership clause. In particular, neither contact-incidence branch
is inserted into `(C1')`.

### 0.5 Fences and the named false anchor

This artifact is symbolic. It does not consume the equation-of-record

```text
pi_Mx,N^sym(
  Loc_N^phys(
    Kernbarhat_N(Q_N(L_T,N))))=1.                 (FALSE-ANCHOR)
```

as a theorem. It does not use a reader value, seed polarity, response,
threshold, fixed point, end test, or measured constant to classify contact
incidence.

## 1. Z1 — Family V003 display repairs

### 1.1 Repair P1: full `(S21)` and the exact `[PROVABLE]` scope

[PROVABLE — exact retained-clause restatement and predicate audit; no
inhabitance claim] The Hodge fiber retains, for every
`s in Sigma_N^(2),Ward`, the full block

```text
[E_C,N,Delta_N^Hdg]=0,

iotatilde_N^H:Sigma_N^(2),Ward->C_N^k,

Ctc_N^sym subset ker(iotatilde_N^H),

iota_N^H([s]_Ctc_sym)
 :=iotatilde_N^H(s),

iota_N^H([s]_Ctc_sym)
 =(1-E_C,N)iota_N^H([s]_Ctc_sym).                (S21)
```

Together with the unchanged clauses, the exact displayed Hodge fiber is

```text
Hdg
 :={ (iotatilde_N^H,iota_N^H)_N :
      (S14),(S19),the full (S21),(S25),(S25b),
      and every Hodge diamond equation hold }.    (V3-1)
```

The V002 sentence saying that none of these equations contains `d` or
`delta` is struck. The full `(S21)` contains `Delta_N^Hdg`, and

```text
Delta_N^Hdg
 =d_N^(k-1)delta_N^k+delta_N^(k+1)d_N^k.          (V3-2)
```

The narrower conclusion needed for the range-clause audit remains valid:

```text
no retained clause supplies v with

iota_N^H(s_Max,N^unit)
 =delta_N^(k+1)d_N^k v,

equivalently no retained clause places

iota_N^H(s_Max,N^unit)
 in closure(ran(delta_N^(k+1)d_N^k)).             (V3-3)
```

Thus no retained clause reconstructs the struck range predicate `(R10)`.
The commutator in `(S21)` does have a different consequence: contact
confinement. It is displayed in Section 1.3 rather than erased.

### 1.2 Repair P2: `(C1b)` deletes old void 12 at its point of use

The compatibility solution space and the extensional definition of the
honest family remain exactly V002's:

```text
Sol_Loc
 :=Ext
    fiber-product_Gates Hdg
    fiber-product_Gates Tar
    fiber-product_Gates
      Product_N Hom(D_N^Loc,Sym_N^loc),           (C1a)

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
        typing required in (S4) }.                (C1')
```

What needed repair was the two-sorted subtraction. A membership predicate
and a falsifier policy are not the same kind of object. The definitive
point-of-use ledger is

```text
membership(C1')
 :=membership(old C1) minus {R10},

void_policy(C1')
 :=(void_policy(old C1) minus {OLD-V12})
    union {NEW-V12-PRIME},

R10
 :=[iota_N^H Loc_N^phys(kappa_T,N)
      in closure(ran(delta_N^(k+1)d_N^k))],

OLD-V12
 :=[P_H,N iota_N^H Loc_N^phys(kappa_T,N)!=0
      => member void]
   =STRUCK,

NEW-V12-PRIME
 :=seed-polarity-or-undeclared-Hol-selection falsifier,

(S28) notin membership(C1'),
not-(S28) notin membership(C1').                 (C1b)
```

The replacement falsifier expands without imposing either polarity:

```text
NEW-V12-PRIME fires iff a construction or membership rule

  uses (S28), not-(S28), HRoute_N, or q_T,N
    as an admission or selection condition,

  or appends an undeclared Hol_N without its own provenance,
    units, covariance, restriction, and failure-capable tests. (V3-4)
```

The two repaired rows in the genuine-clause ledger are therefore:

| Clause/policy | Status at `(C1b)` | Exact reason |
|---|---|---|
| old Hodge-range predicate `(R10)` | struck from `membership(C1')` | it independently imposes `not-(S28)` and deletes the exact Hodge sector; no retained clause forces it |
| old void 12 `(OLD-V12)` | struck from `void_policy(C1')` | it separately rejects every nonzero harmonic image and would survive deletion of `(R10)` unless removed here |
| replacement void `12'` `(NEW-V12-PRIME)` | retained falsifier policy, not a seed-polarity cut | it rejects seed-driven selection and undeclared `Hol`, but does not reject an intrinsic nonzero harmonic image |

The detailed fourteen-void table in V002 is now read as a rerun of `(C1b)`,
not as the first normative deletion of `(OLD-V12)`.

```text
OLD_RANGE_CLAUSE = STRUCK_AT_C1b
OLD_VOID_12 = STRUCK_AT_C1b
NEW_VOID_12_PRIME = RETAINED_SEED_BLIND_FALSIFIER
SEED_POLARITY_IN_MEMBERSHIP = none
```

### 1.3 Repair P3: the second vanishing mechanism

[PART-PROVABLE — retained-clause consequence for each future
`L in L_F2'`] Define

```text
x_T,N(L)
 :=iota_N^H Loc_N^phys(kappa_T,N),

m_T,N(L)
 :=P_H,N x_T,N(L).                               (V3-5)
```

Here and below, `E_C,N` is the ambient stage projector fixed by A5. It is
not indexed by `L`; only `iota_N^H`, `Loc_N^phys`, and the resulting
`m_T,N(L)` carry the candidate-member dependence in this display.

The last equation of `(S21)` and idempotence of the orthogonal projector
give every intermediate equality:

```text
E_C,N x_T,N(L)
 =E_C,N(1-E_C,N)x_T,N(L)

 =E_C,N x_T,N(L)-E_C,N^2 x_T,N(L)

 =E_C,N x_T,N(L)-E_C,N x_T,N(L)

 =0.                                             (V3-6)
```

Because the finite Hodge Laplacian is self-adjoint and
`P_H,N=1_{0}(Delta_N^Hdg)`, functional calculus displays

```text
[E_C,N,Delta_N^Hdg]=0

 =>E_C,N 1_{0}(Delta_N^Hdg)
    =1_{0}(Delta_N^Hdg)E_C,N

 =>E_C,N P_H,N=P_H,N E_C,N.                     (V3-7)
```

Substituting `(V3-6)` into `(V3-7)` gives

```text
E_C,N m_T,N(L)
 =E_C,N P_H,N x_T,N(L)

 =P_H,N E_C,N x_T,N(L)

 =P_H,N 0

 =0,

m_T,N(L)
 in im(P_H,N) intersection ker(E_C,N).           (V3-8)
```

At the actual reciprocal stage,

```text
im(P_H,RL)=H_RL=span{c_RL},
c_RL!=0,

m_T,RL(L)=lambda_L c_RL.                        (V3-9)
```

Equations `(V3-8)`--`(V3-9)` yield

```text
0
 =E_C,RL m_T,RL(L)

 =E_C,RL(lambda_L c_RL)

 =lambda_L E_C,RL c_RL.                         (V3-10)
```

Consequently

```text
m_T,RL(L)!=0
 =>lambda_L!=0
 =>E_C,RL c_RL=0,                               (V3-11)

E_C,RL c_RL!=0
 =>lambda_L=0
 =>m_T,RL(L)=0.                                 (V3-12)
```

This is the second vanishing mechanism. It is distinct from the deleted
`ran(delta d)` route. V002's separation model set `E_C=0`; it therefore
tests only the branch on which `(V3-12)` is inactive. It remains a valid
clause-separation control on that branch, but it is not an exhaustion of
the retained mechanisms.

The repaired outcome enumeration, before deciding the contact-incidence
bit, is now exact:

```text
outcome (a), displayed full-gate threading member:
  not licensed; no full-gate member is sealed;

outcome (b), reciprocal vanishing:
  licensed for every future member if E_C,RL c_RL!=0;
  independently licensed on every acyclic stage because P_H=0 there;

outcome (c), present record:
  UNDETERMINED until the contact-incidence bit is classified;
  on its zero branch, q_T,RL(L) and inhabitance still remain.
                                                               (V3-13)
```

## 2. Z2 — type and determine `E_C,RL c_RL`

### 2.1 Determination question first

The locked-process question is

```text
DOES_SEALED_STOCK_DECIDE
  whether c_RL lies in the actual ambient I_contact,RL^k
  or in (I_contact,RL^k)^perp?                   (E0)
```

No desired threading consequence is consulted in answering `(E0)`.

### 2.2 Exact subject typing

[PROVABLE — definitive ambient typing] At the reciprocal stage, the finite
carrier and the A5 contact projector have types

```text
c_RL in H_RL subset C_RL^k,

I_contact,RL^k subset C_RL^k,

E_C,RL:C_RL^k->C_RL^k,

ran(E_C,RL)=I_contact,RL^k,

ker(E_C,RL)=(I_contact,RL^k)^perp,

E_C,RL^*=E_C,RL,
E_C,RL^2=E_C,RL.                                 (E1)
```

Thus `E_C,RL c_RL` is a formed ambient vector in `I_contact,RL^k`. The map,
subspace, and subject are typed by the adopted law; current stock does not
exhibit a reciprocal spanning manifest that decides this particular value.
The expression is not a scalar response and is not a Loc-member coordinate.

The contact-carrier collision is resolved explicitly:

```text
I_contact,RL^resp subset R_RL^resp
  =A4 response/contact pushout leg;

I_contact,RL^k subset C_RL^k
  =A5 ambient Hodge contact subspace and ran(E_C,RL);

Bridge_contact,RL:
  I_contact,RL^resp <-> I_contact,RL^k
  =NOT_SUPPLIED_BY_A4_OR_Q408.                    (E1a)
```

### 2.3 A4: what the strict pushout does and does not decide

[PROVABLE] A4 declares

```text
C_RL^ov
 :=R_RL^rep intersection I_contact,RL^resp,

R_RL^phys
 :=(R_RL^rep direct_sum I_contact,RL^resp)
    /Delta_RL,

Delta_RL
 :={(c,-c):c in C_RL^ov}.                       (E2)
```

The represented injection is not allowed to delete a nonzero class. The
displayed pushout calculation is

```text
[r,0]=0

 =>(r,0)=(c,-c) for some c in C_RL^ov

 =>-c=0

 =>c=0

 =>r=0.                                         (E3)
```

But `(E3)` does not say that a represented class cannot also be a contact
class. For every nonzero `z in C_RL^ov`, the pushout identifies `[z,0]`
with `[0,z]`; it does not set either class to zero:

```text
[z,0]=[0,z]!=0.                                  (E4)
```

Therefore, even if an independently typed bridge later places a response
realization of `c_RL` in the overlap, A4's no-deletion law cannot be
contraposed into `c_RL notin I_contact,RL^k`. Its declined
zero-intersection alternative also remains an allowed future upgrade if an
independent separation theorem is ever proved. A4 supplies neither the
bridge `(E1a)` nor a reciprocal Hodge contact-incidence classifier.

### 2.4 A5: the complete forced dichotomy

[PROVABLE] A5 supplies the adopted reducing equation

```text
[E_C,RL,Delta_RL^Hdg]=0.                         (E5)
```

Functional calculus, already displayed in `(V3-7)`, gives

```text
[E_C,RL,P_H,RL]=0.                               (E6)
```

Since `c_RL=P_H,RL c_RL`, equations `(E6)` and `(E1)` give

```text
E_C,RL c_RL
 =E_C,RL P_H,RL c_RL

 =P_H,RL E_C,RL c_RL

 in H_RL.                                       (E7)
```

The line is one-dimensional, so for a scalar `epsilon_C,RL`,

```text
E_C,RL c_RL=epsilon_C,RL c_RL.                  (E8)
```

Apply idempotence and use `c_RL!=0`:

```text
epsilon_C,RL c_RL
 =E_C,RL c_RL

 =E_C,RL^2 c_RL

 =E_C,RL(epsilon_C,RL c_RL)

 =epsilon_C,RL^2 c_RL,

epsilon_C,RL^2=epsilon_C,RL,

epsilon_C,RL in {0,1}.                           (E9)
```

Because `E_C,RL` is an orthogonal projector, the two branches are exactly

```text
epsilon_C,RL=0
 iff E_C,RL c_RL=0
 iff H_RL subset (I_contact,RL^k)^perp,

epsilon_C,RL=1
 iff E_C,RL c_RL=c_RL
 iff H_RL subset I_contact,RL^k.                 (E10)
```

There is no intermediate value. This ambient dichotomy is derived; choosing
its branch is not.

### 2.5 Reciprocal contact/Ward data do not choose the bit

[PROVABLE — source-content audit] The reciprocal stock supplies a genuine
cycle and its homogeneous Ward equation:

```text
c_RL!=0,

B_RL^T c_RL=0,

<partial J_cRL,varphi>
 =<J_cRL,d varphi>
 =<B_RL^T c_RL,varphi>
 =0.                                             (E11)
```

Equation `(E11)` proves conservation. It does not say whether the conserved
line is contact or contact-orthogonal. In particular, a homogeneous Ward
kernel can contain a contact vector and a noncontact vector alike.

The same source terminates with

```text
PHYSICAL_WARD_CONTACT_HODGE_SPLIT
 = NOT_BUILT / TYPE-U.                           (E12)
```

Thus record visibility of the Q-408 current cannot be transported into a
claim about `(E10)` without the missing contact-incidence/split bridge.
A4's `I_contact^resp` leg, A5's `I_contact^k` projector range, and Q-408's
visible current are not silently identified by notation.

The commissioned authority sweep is exhaustive on this question:

```text
A4 strict pushout:
  response overlap and injectivity, no Hodge contact manifest;

A5 decision + projector certificates:
  projector schema, reduction, and inherited voids,
  no reciprocal contact generator or incidence value;

Q-408 reciprocal current/Ward stock:
  visible conserved cycle and the explicit missing split (E12);

joint assembly:
  formal pushout legs and their maps,
  no identification supplying (E1a);

ACTUAL_RECIPROCAL_CONTACT_SPLIT_CERT = absent.    (E12a)
```

Thus the sealed stock contains neither the membership witness for `EC1`
nor the spanning orthogonality certificate for `EC0`. This is a finite
source-content determination, not a theorem that future physical data cannot
decide the branch.

[PART-PROVABLE — local clause separation only] The commutator and
homogeneous Ward equations alone do not choose between the two algebraic
line actions. On
`C_RL^k=H_RL direct_sum H_RL^perp`, choose any fixed reducing
`I_perp subset H_RL^perp`, hold all remaining data fixed, and compare

```text
I_contact,RL^(k,0):=I_perp,
E_C,RL^(0)|_H_RL=0,

I_contact,RL^(k,1)
 :=I_perp direct_sum H_RL,
E_C,RL^(1)|_H_RL=id_H_RL.                        (E13)
```

Because `Delta_RL^Hdg|_H_RL=0`, both line restrictions commute with the
Laplacian. Because `(E11)` is homogeneous, adding the conserved line does
not violate that equation. If a separate response/Hodge bridge is supplied,
A4's pushout remains injective whether or not the bridged line lies in the
overlap, by `(E3)`--`(E4)`. Equation `(E13)` is not an actual-surface member
and does not instantiate or alter the actual stage contact data; it is only a
finite clause-separation witness for those local equations. It does not check
the full `(S21)` map, the A5 no-deletion void, old-image restrictions,
family covariance, or common-refinement diamonds; it is not used as a
full-package non-obstruction certificate.

### 2.6 Determination verdict: `AUTHORABLE`, not `END_TEST`

[PROVABLE] The K5 direction test is displayed as follows:

```text
subject type-formed?
  yes, ambiently:
    E_C,RL c_RL is typed by (E1);

reciprocal incidence value determined?
  no:
    ACTUAL_RECIPROCAL_CONTACT_SPLIT_CERT is absent;
    the value-classification certificate is construction debt;

quantity produced by the self-consistency loop?
  no:
    E_C,RL and c_RL are ambient stage/carrier data fixed before Loc,
    and (V3-8)--(V3-12) consume their incidence to constrain m_T;

quantity consumed upstream?
  yes:
    epsilon_C,RL=1 closes the reciprocal harmonic route before any
    reader, fixed point, threshold, or end test can run.          (E14)
```

Therefore the unresolved bit cannot be filed as `END_TEST`: its subject is
constructed, its missing value-classification is construction debt, and the
value is consumed rather than produced. The sealed stock derives neither
branch. The remaining lawful classification is an authorable structural
gate.

[YOURS — candidate only, not adopted] The minimal full-gate question is

```text
GATE_EC_RL_CONTACT_INCIDENCE

required proof object:
  ACTUAL_RECIPROCAL_CONTACT_SPLIT_CERT;

subject:
  the basis-free actual line H_RL=im(P_H,RL)
  and the ambient actual subspace I_contact,RL^k;

alternatives:
  EC0  H_RL subset (I_contact,RL^k)^perp;
  EC1  H_RL subset I_contact,RL^k;

freedom:
  one Boolean incidence bit epsilon_C,RL in {0,1}
  on the actual reciprocal stage/relabeling orbit;

custody:
  ambient stage datum fixed by A5;
  not a coordinate of Hdg, Tar, Loc, or a C1' member;

not freedom:
  no scale, coefficient, basis, orientation, member, reader value,
  seed polarity, threshold, or fixed-point output;

required inherited certificates:
  typed response-to-Hodge bridge if A4 provenance is invoked;
  A5 projector/reducing equations and no-deletion void;
  units, reality, OLD_FID, RNL, LR;
  licensed old-image restriction and common-refinement coherence;

covariance/variance:
  the chosen line classification must be constant on the admitted
  relabeling/reality orbit and on certified rank-preserving transports;
  it creates no upward rule on a cycle-creating arrow.            (E15)
```

The certificate must make the branch test operational without choosing a
basis. Let it exhibit an actual finite spanning generator family, carried as
its whole admitted orbit,

```text
G_contact,RL subset C_RL^k,

I_contact,RL^k
 =span(G_contact,RL),

ell_C,RL:I_contact,RL^k->F,
ell_C,RL(b):=<b,c_RL>_RL.                       (E15a)
```

Then the two tests are displayed. If the functional vanishes on the full
spanning family,

```text
ell_C,RL|_(G_contact,RL)=0

 =>ell_C,RL=0

 =>c_RL perpendicular I_contact,RL^k

 =>EC0.                                         (E15b)
```

If an actual generator `b` has nonzero structural pairing, A5 reduction
gives

```text
b in I_contact,RL^k,
<b,c_RL>_RL!=0,

P_H,RL b
 =(<b,c_RL>_RL/<c_RL,c_RL>_RL)c_RL
 in I_contact,RL^k,

 =>c_RL in I_contact,RL^k

 =>EC1.                                         (E15c)
```

Only zero versus nonzero is used in `(E15b)`--`(E15c)`; no magnitude is
evaluated. The alternatives are algebraically exhaustive by `(E9)`, but
neither is promoted to a lawful actual incidence ruling until all inherited
certificates in `(E15)` pass. In particular, `EC1` still owes the A5
void-3 proof that contact descent deletes no `D_G^*`-visible bulk or harmonic
cycle. `EC0` leaves contact confinement neutral on `H_RL`; `EC1`
makes the honest-family harmonic composite zero at `N_RL`. Neither
consequence is a reason to prefer the alternative.

The gate is failure-capable:

| Void | Falsifier |
|---:|---|
| 1 | `EC0` is declared but an actual `b in G_contact,RL` satisfies `<b,c_RL>_RL!=0`, triggering `(E15c)` |
| 2 | `EC1` is declared but a complete spanning manifest satisfies `<b,c_RL>_RL=0` for every `b in G_contact,RL`, triggering `(E15b)` |
| 3 | the declared projector fails idempotence, self-adjointness, or `[E_C,RL,Delta_RL^Hdg]=0` |
| 4 | `EC1` or its response/Hodge bridge deletes a `D_G^*`-visible bulk or harmonic cycle, or any A4/A5 no-deletion test fails |
| 5 | units, reality, OLD_FID, RNL, LR, a licensed old-image restriction, relabeling transport, or a common-refinement diamond fails |
| 6 | the branch is chosen from `q_T,RL`, `chi`, a desired coefficient, response, threshold, fixed point, end test, or measured constant |
| 7 | the gate manufactures a cycle-creating upward lift or identifies current, response, symbol, and Hodge carriers without the required typed bridge |

Minimality follows from `(E9)`: the ambient A5-compatible action on
the one-dimensional harmonic line is already `EC0` or `EC1`. Any
extra continuous parameter would be surplus and unlawful. The generator
manifest, bridge, no-deletion, and coherence terms are proof obligations,
not added physical coefficients.

```text
E_C_MAP = TYPED_AMBIENT_ORTHOGONAL_PROJECTOR
E_C_SUBJECT = CONSTRUCTED_AND_TYPED
E_C_RECIPROCAL_INCIDENCE_CERT = UNBUILT
E_C_CUSTODY = AMBIENT_STAGE_DATUM_NOT_MEMBER_COORDINATE
E_C_DICHOTOMY = DERIVED
E_C_BRANCH = NOT_DERIVED
E_C_DIRECTION = CONSUMED_NOT_PRODUCED
E_C_END_TEST = false
E_C_GATE_CANDIDATE = GATE_EC_RL_CONTACT_INCIDENCE
GATE_ADOPTED = false
MACHINERY_APPEAL = true
  (+no reciprocal contact-incidence/split certificate in sealed stock)
```

## 3. Z3 — updated deciding-data and consequence board

### 3.1 Carry both contact branches through the pairing

For a future `L in L_F2'`, V002's rank-one calculation remains unchanged:

```text
q_T,RL(L)
 :=<iota_RL^H(s_Max,RL^unit),c_RL>_RL,

m_T,RL(L)
 =(q_T,RL(L)/<c_RL,c_RL>_RL)c_RL.               (B1)
```

On the ambient `EC1` branch, `(V3-8)` and `(E10)` give the complete displayed
vanishing chain

```text
m_T,RL(L)
 in H_RL intersection ker(E_C,RL)

 =H_RL intersection H_RL^perp

 ={0},

m_T,RL(L)=0,

q_T,RL(L)=0.                                     (B2)
```

On the ambient `EC0` branch,

```text
ker(E_C,RL) intersection H_RL
 =H_RL,

m_T,RL(L)
 in H_RL.                                        (B3)
```

Equation `(B3)` removes the contact obstruction only. It does not imply
`q_T,RL(L)!=0`, does not construct a member, and does not prove threading.

### 3.2 Definitive deciding-data board

```text
Y2_OUTCOME = (c) UNDETERMINED

PRIOR_STRUCTURAL_DATUM
 =epsilon_C,RL in {0,1}
 =AUTHORABLE_UNSET
 =ambient stage datum, not member-supplied

IF epsilon_C,RL=1:
  RECIPROCAL_THREADING = VANISHING_FOR_EVERY_FUTURE_C1_PRIME_MEMBER
  by (B2)

IF epsilon_C,RL=0:
  CONTACT_ROUTE = INACTIVE_ON_H_RL
  BLOCKING_QUANTITY =
    q_T,RL(L):=<iota_RL^H(s_Max,RL^unit),c_RL>_RL
  FULL_GATE_MEMBER_INHABITANCE = NOT_ESTABLISHED

ACYCLIC_BOUNDARY = VANISHING
S28_ASSUMED = false
NOT_S28_ASSUMED = false
MEMBER_SELECTED = none                           (B4)
```

The old board's phrase `E_C custody unassigned` is now split correctly:

```text
E_C_MAP_CUSTODY = A5 ambient adopted projector
E_C_MEMBER_COORDINATE = false
E_C_RECIPROCAL_INCIDENCE_CERT = UNBUILT
E_C_ON_RECIPROCAL_LINE = AUTHORABLE_UNSET incidence bit.       (B5)
```

### 3.3 Consequences for the seed, J2, the coefficient face, and A1

| Item | `EC0`: `E_C,RL c_RL=0` | `EC1`: `E_C,RL c_RL=c_RL` | Present unruled gate |
|---|---|---|---|
| seed | contact confinement does not force zero; subject still requires a full-gate member and nonzero `(B1)` pairing | every future honest-family member has `m_T,RL(L)=0`; no reciprocal seed support through ordinary `iota^H` | no seed polarity is licensed |
| J2 rank-preserving premise board | E_C route clears, but the V002 map/naturality, quotient, and comparison debts remain | map/naturality debts remain; the rank-one nonzero coefficient normalization cannot form at `N_RL` | no J2 premise is newly completed |
| coefficient-face basis | conditional on a member and `q_T,RL(L)!=0` | reciprocal position is outside `A_RP^+(L)` for every member | support remains member-indexed by `L` but ambient-branch conditional |
| A1 amendment | still needed for any separately claimed `Hol_N`; not needed merely to test intrinsic `(B1)` | needed if a nonzero loop-period route is pursued, because ordinary contact-descended Loc has zero `H_RL` component | banked route remains separate and unadopted |
| J7 scope | may quantify only over diamonds wholly inside the member-indexed proved nonzero support | the reciprocal position lies outside support-scoped `A_RP^+(L)`; any broader demand there is unformable, and J2 is not a substitute | keep the two-branch scope table explicit |

No row claims that a vanishing honest-family route makes an enlarged holonomy
family exist. No row claims that `EC0` supplies nonvanishing.

### 3.4 Handoff to PASTE 574's convergence adjudication

The convergence adjudication receives four exact facts:

```text
1  E_C,RL c_RL is a constructed, ambient upstream structural input.
   Its incidence value is not determined; the loop consumes that value
   and cannot produce it.

2  A5 reduces that input to one ambient Boolean contact-incidence gate;
   neither the local threshold nor a period replacement may choose it.

3  On EC1, the ordinary (C1') contact-descended Hodge composite has
   zero component on the reciprocal harmonic line for every member.
   A period construction that supplies a nonzero component
   would be a separately typed Hol/A1 route or a family amendment,
   not a reinterpretation of the same Loc.

4  On EC0, contact confinement no longer blocks the line, but a
   constructed period map, its producer/consumer direction, the pairing,
   and full-gate member inhabitance remain separate debts.              (B6)
```

Thus a record-native period construction may address the map/contraction
debt identified by the chain audit, but it cannot silently settle the
contact-incidence gate or infer a seed. This is the precise input from 575
to the 574 convergence review.

```text
HANDOFF_574
 = PERIOD_ROUTE_ORTHOGONAL_TO_UNRULED_EC_GATE
   + EC1_REQUIRES_SEPARATE_HOL_OR_FAMILY_AMENDMENT
   + EC0_STILL_REQUIRES_MAP_PAIRING_AND_INHABITANCE
```

## 4. Z4 — battery

### 4.1 F_PLDEC and false-anchor attack

The allowed dependency graph used in Sections 1--3 is

```text
V002 projector schema
 +DoR-019 ratified metric
 +A5 ambient Hodge-contact reducing law
 +finite Hodge functional calculus
 +rank-one H_RL

 ->ambient E_C typing
 ->the dichotomy (E9)--(E10)
 ->the conditional threading branches (B2)--(B3);

A4 response strict pushout
 ->injectivity/no-deletion calculation (E3)--(E4)
 ->no Hodge-contact incidence inference;

Q-408 reciprocal cycle + homogeneous Ward equation
 ->conservation (E11)
 ->explicit absence of the response/Hodge contact bridge (E12).
                                                               (BAT-1)
```

The prohibited graph is

```text
reader / chi / reader T / desired coefficient / computed response value
 / threshold / fixed point / end test / measured constant
 / (FALSE-ANCHOR) / S28 / not-(S28)

 -/-> E_C, I_contact^k, epsilon_C,RL,
      membership(C1'), a gate branch, or a member.             (BAT-2)
```

The derivation of the dichotomy was completed before the conditional
threading consequences were inspected. Neither branch was selected.

```text
READER_USED_TO_REPAIR_FAMILY = false
READER_USED_TO_TYPE_E_C = false
FALSE_ANCHOR_CONSUMED = false
SEED_POLARITY_CONSUMED = false
F_PLDEC = CLEAN
```

### 4.2 Anti-tuning ledger

| Hazard | Control | Result |
|---|---|---|
| choose `EC0` because it permits threading | both `EC0` and `EC1` retained; no branch adopted | clean |
| choose `EC1` because it forces a desired zero | consequences displayed only after the source audit; no branch adopted | clean |
| infer zero from A4 no-deletion | pushout injection and overlap identification separately displayed in `(E3)`--`(E4)` | rejected |
| infer contact exclusion from Ward conservation | homogeneous Ward equation and missing split displayed in `(E11)`--`(E12)` | rejected |
| tune a continuous eigenvalue | idempotence derives the exact set `{0,1}`; no continuous parameter remains | clean |
| select an orientation or basis | gate is stated on the whole line `H_RL`, invariant under rescaling/sign | clean |
| propagate a choice upward on cycle creation | gate covariance is rank-preserving/contravariant only | clean |
| force seed polarity through membership | `(C1b)` removes both `(R10)` and `(OLD-V12)` and retains seed-blind `12'` | clean |
| let the period convergence hypothesis choose contact incidence | `(B6)` separates the two questions | clean |
| use an output to construct an input | `(E14)` records only the incidence certificate as construction debt and the ambient value as consumed, not produced | clean |
| bind a family member | all member statements are universally conditional | clean |
| evaluate or compare a magnitude | only symbolic zero/nonzero and the projector bit are used | clean |

### 4.3 Fence and machinery ledger

```text
MEMBER_BOUND = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false
MEASURED_CONSTANT_COMPARISON = none

MACHINERY_APPEAL = true
  (+the exact missing object is a failure-capable reciprocal
     contact-incidence/Ward-Hodge split certificate deciding (E10);
   +the appeal does not stop the structural dichotomy,
     the family repair, or the two-branch consequence board)

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

### 4.4 Self verb audit

| Verb/claim | Display immediately supporting it | Audit |
|---|---|---|
| full `(S21)` `RESTORED` | complete five-part block `(S21)` and Hodge fiber `(V3-1)` | clean |
| `[PROVABLE]` scope `CORRECTED` | explicit `Delta` expansion `(V3-2)` and narrow absent bridge `(V3-3)` | clean |
| old void 12 `STRUCK_AT_C1b` | typed membership/void-policy equations `(C1b)` and ledger rows | clean |
| second vanishing route `DERIVED` | every equality `(V3-5)`--`(V3-12)` | clean |
| `E_C` subject `TYPED_AMBIENT` | A5/Loc custody statement plus domain, range, kernel, adjoint, and idempotence `(E1)`; missing cross-carrier bridge remains `(E1a)` | clean; no member coordinate invented |
| A4 `DOES NOT DECIDE` incidence | injectivity `(E3)`, surviving overlap `(E4)`, and no converse used | clean |
| dichotomy `DERIVED` | commutation `(E5)`--`(E7)`, scalar restriction `(E8)`, idempotence `(E9)`, equivalences `(E10)` | clean |
| branch `NOT DERIVED` | homogeneous Ward audit `(E11)`, missing split `(E12)`, and exhaustive commissioned-source ledger `(E12a)` | clean; `(E13)` is expressly local only and no stock-wide impossibility is claimed |
| `AUTHORABLE`, not `END_TEST` | constructed/value-undetermined/produced/consumed direction test `(E14)` and operational full gate `(E15)`--`(E15c)` | clean |
| threading board `UPDATED` | branchwise equalities `(B1)`--`(B5)` | clean |
| 574 handoff `STATED` | four exact conditional inputs `(B6)` | clean; no claim about 574's eventual verdict |
| `F_PLDEC = CLEAN` | allowed/prohibited dependency graphs `(BAT-1)`--`(BAT-2)` | clean |
| anti-tuning `clean` | hazard/control ledger above | clean |
| `MACHINERY-APPEAL = true` | missing reciprocal contact-incidence/split certificate named exactly | clean; structural work continued |

Every operative verb is limited to its displayed domain. The artifact does
not call the clause-separation model an actual member, does not call `EC0`
threading, and does not call `EC1` a deletion by the A4 pushout.

DISPLAY_REPAIRS = DONE
E_C_ON_LOOP = AUTHORABLE (+basis: A5 derives the ambient dichotomy `E_C,RL c_RL in {0,c_RL}`, while A4/Q-408 supply no `ACTUAL_RECIPROCAL_CONTACT_SPLIT_CERT`; `GATE_EC_RL_CONTACT_INCIDENCE` requires the spanning structural pairing test, typed bridge, no-deletion and coherence certificates; the subject is constructed and its value is an upstream consumed input, never an end test; no branch adopted)
THREADING_BOARD = updated (+ambient `EC1` forces reciprocal vanishing for every future `(C1')` member; ambient `EC0` leaves `q_T,RL(L)` and full-gate inhabitance unresolved; present verdict remains UNDETERMINED)
VERB_AUDIT_SELF = CLEAN
