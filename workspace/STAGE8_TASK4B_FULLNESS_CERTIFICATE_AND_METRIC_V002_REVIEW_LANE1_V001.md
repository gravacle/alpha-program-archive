# STAGE8 TASK 4B - FULLNESS CERTIFICATE AND METRIC V002 REVIEW - LANE 1 V001

```text
ARTIFACT = STAGE8_TASK4B_FULLNESS_CERTIFICATE_AND_METRIC_V002_REVIEW_LANE1_V001.md
LANE = CODEX LANE 1
TASK = PASTE 458 | fullness derivation and metric V002 review
DATE = 2026-08-03
STATUS = COMPLETE | DERIVATION AND REVIEW | NOTHING ADOPTED

LEAD_RESULT:
  FULLNESS = PROVEN
  FINITE_THEOREM = ker(I_K,G)={0} for every admitted A2 realization and stage
  COMPLETION_THEOREM = the forced-semiform Hilbert completion preserves injectivity
  DECIDING_CLAUSE = A2-R10, retained through V004/V005 and ratified by DoR-015
  R2_COUNTERMODEL = integral if desired, but not admitted because it violates A2-R10
  NULL_SECTOR = absent on the admitted family
  METRIC_V002 = NOT_READY | false NO_VERDICT/countermodel standing and over-authored W3 isometry
  DOR019_RESIDUE = R5 carrier identification | A4 automorphism isometry | units

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 0. Preflight and authorities

Preflight passed before V002 was read.

| Check | Result |
|---|---|
| register head | `Q-376` exactly |
| V002 SHA-256 | `7788e29da98be54e983a660768c0c70258e7d6d89eb51a2dafc4dbe17a9ea825` - match |
| V002 sidecar | verified `OK` |
| DoR-015 / V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` - match |
| descent V003 | `a03e836380cbbfa08d8763bf62d6104f70aec69ae484b3b69f63489a5ce1c68c` - match |
| prior Lane-1 review | `55975bfa4358a720b9bffe091a6c5b246e6231d2d974dd4d270021040056eec5` - match |

The deciding adopted clauses are:

1. Field-signature V003 A2-R10: the differential of the finite framed scalar
   transport reaches every admitted edge-coordinate direction modulo the displayed
   vertex-frame action.
2. Field-signature V004 Section 3.1: A1 and A2-R1 through R11 are preserved verbatim.
3. Field-signature V005 opening scope: every V004 survivor remains unless explicitly
   retargeted; V005 retargets the quotient/current domain, not A2-R10.
4. DoR-015: V005 and its external realization are ratified.
5. DoR-015 W3 precision: finite source restrictions are adjoints of retained
   isometric inclusions.

Symbol precision used below:

```text
K_G       = real finite cycle carrier ker(B_G^T);
K_G^Z     = its integral cycle lattice;
I_K,G     = finite map c -> u_c;
I_K       = its directed/completed extension only after the completion is named;
L_G       = connection-tangent edge-integral map;
B_G       = vertex-frame coboundary map.
```

## 1. T1 - bounded review verdicts

| Repair | Verdict | Reason |
|---|---|---|
| T1.1 forced semiform | **PASS** | `s_G(c,d)=g_A4(u_c,u_d)` and `ker(s_G)=ker(I_K,G)` are correctly premise-marked derived |
| T1.2 quotient family naturality | **PASS** | automorphisms, restrictions, and certified inclusions preserve `ker(I_K)` by the displayed commuting squares; the quotient proof is valid as an abstract fallback theorem |
| T1.3 A4 isometry provenance | **KILL** | automorphism isometry is honestly authored, but rank-preserving source isometry is already ratified by DoR-015 W3 and is falsely re-authored |
| T1.4 Riesz unit correction | **PASS** | every live table uses `[R_A]=U_A^-2` and `[R_A^-1]=U_A^2`; the derivative units are propagated consistently |
| T1.5 choice table | **KILL** | the Q/N null-sector branches are presented as live although A2-R10 already proves the kernel zero; the table overstates DoR-019's carrier choice |
| T1.6 R2 countermodel | **KILL** | its linear algebra is correct, and `e_2` may be integral, but the model violates the adopted A2-R10 fullness clause and is not admitted |

The useful V002 repairs remain useful despite the kills: the semiform, quotient
naturality lemma, unit correction, completed-carrier certificate shape, and the clean
response-independent provenance all survive.

## 2. T2 - the finite fullness theorem

### 2.1 Differential of the adopted finite transport

For each admitted finite realization `G`, the adopted framed scalar transport has
edge coordinates `h_e(A,p)`. V004 computes its logarithmic differential exactly:

```text
-i h_e^(-1) d h_e(a,theta)
  =(L_G a)_e+(B_G theta)_e,

(L_G a)_e=integral_(gamma_e) a,
(B_G theta)_e=theta_t-theta_s.                  (T2-1)
```

A2-R10 says this differential reaches every finite edge-coordinate direction modulo
the displayed vertex-frame action. In linear form, either equivalent reading is

```text
image(L_G)+image(B_G)=E_G,                       (T2-2)

or

q_G image(L_G)=E_G/image(B_G).                  (T2-3)
```

Thus the missing `FULLNESS_CERT` is already a ratified realization clause.

### 2.2 Kernel proof

Let

```text
c in K_G=ker(B_G^T)
```

and suppose

```text
I_K,G(c)=u_c=0,
u_c(a)=c^T L_G a.                               (T2-4)
```

Take arbitrary `x in E_G`. By `(T2-2)`, choose `a,theta` with

```text
x=L_G a+B_G theta.
```

Then

```text
c^T x
 =c^T L_G a+c^T B_G theta
 =u_c(a)+(B_G^T c)^T theta
 =0.                                             (T2-5)
```

Because the standard edge pairing on `E_G` is nondegenerate and `x` was arbitrary,
`c=0`. Therefore

```text
ker(I_K,G)={0}                                   (T2-6)
```

for every admitted realization member and every finite stage. The proof is
family-wide: it uses only R10, not a chosen path, frame, orientation, filtration, or
realization member.

The same result follows directly from `(T2-3)`: `u_c=0` says `c` annihilates the
entire quotient, and Gate-4 nondegeneracy then gives `c=0`.

```text
FINITE_FULLNESS = true | TYPE-P | premises: DoR-015 A2-R10
FINITE_KERNEL_STAGES = none
MINIMAL_NONZERO_KERNEL_CYCLE = does not exist on the admitted family
```

### 2.3 Integral cycles

Since `(T2-6)` holds on the full real carrier, it holds a fortiori on the integral
lattice:

```text
ker(I_K,G) intersection K_G^Z={0}.               (T2-7)
```

No integrality subtlety remains. A nonzero integer cycle cannot define the zero
connection-current functional on an admitted R10 realization.

### 2.4 Directed finite core and completion

Let `K_fin` be the algebraic directed union of the finite `K_G` and let `J_fin` be
the corresponding union of finite A4 currents. Any `c in K_fin` occurs at some finite
stage, so `(T2-6)` gives

```text
ker(I_K:K_fin->J_fin)={0}.                        (T2-8)
```

The forced form is

```text
s(c,d)=g_A4(I_K c,I_K d),
||c||_s=||I_K c||_A4.                            (T2-9)
```

DoR-015 W3 supplies the retained isometric finite inclusions. Hence `(T2-9)` is a
consistent pre-Hilbert norm on the directed core. Completing `K_fin` in this norm,
`I_K` extends uniquely as an isometry into `J_phys^005`. If the extension sends `k`
to zero, then

```text
||k||_s=||I_K k||_A4=0,
```

so `k=0`. Therefore

```text
ker(completed I_K)={0}                            (T2-10)
```

on the forced-semiform Hilbert completion.

This does not silently identify an arbitrary larger R5 carrier with that completion.
The remaining `CARRIER_IDENTIFICATION_CERT` must state that R5 `K_cycle` is this
dense completion and that `C_prop` is its declared Hilbert dual. An external
non-dense enlargement would be a new carrier, not a counterexample to fullness.

```text
ALGEBRAIC_CORE_FULLNESS = true | TYPE-P
SEMIFORM_COMPLETION_FULLNESS = true | TYPE-P
ARBITRARY_EXTERNAL_R5_ENLARGEMENT_IDENTIFIED = false | TYPE-U |
  exact residue: CARRIER_IDENTIFICATION_CERT
```

## 3. Re-examination of the prior R2 countermodel

The prior model used

```text
Q_G^lin=R^2,
K_G=R^2,
T_phys,G=span{e_1},
u_(c_1,c_2)(t e_1)=c_1 t.
```

Choose the integral lattice `K_G^Z=Z^2`. Then `e_2` is an integral cycle, so the
witness was not an artifact of passing from an integral lattice to a real carrier.

Its failure is instead exact and simpler:

```text
T_phys,G=span{e_1} != Q_G^lin=R^2,
image(L_G)+image(B_G) != E_G.                    (T2-11)
```

Thus it violates A2-R10. It remains a valid countermodel to the weaker statement
"point-separation alone implies coefficient injectivity," which is what the prior
review correctly refuted. It is not a countermodel to the full ratified stack.

```text
R2_LINEAR_ALGEBRA = valid
R2_INTEGRAL_WITNESS = yes
R2_ADMITTED_BY_DOR015 = false | TYPE-R | failure: A2-R10
```

## 4. T3 - visibility consequence

Descent V003 proves `D_G^*` injective on the integral cycle carrier. Therefore the
conditional statement in V002 is correct:

```text
if 0!=n in ker(I_K,G) intersection K_G^Z,
then D_G^* n is nontrivial.                       (T3-1)
```

But the antecedent is empty on the admitted family by `(T2-7)`. Hence there is no
record-visible current-null cycle, no stage witness to list, and no lawful need for
an independently authored null-sector metric `h_N`.

```text
D_G_VISIBLE_KERNEL_CLASSES = none
RECORD_VISIBLE_A4_NULL_SECTOR = absent
NEW_NULL_SECTOR_AUTHORED_FIELD_REQUIRED = false
```

The V002 visibility theorem remains bankable for any future realization family that
weakens R10. It does not create a live sector under DoR-015.

## 5. T4 - consequence for DoR-019

Horn (a) is the realized horn:

```text
K_G^vis=K_G/ker(I_K,G)=K_G,
g_K([c],[d])=s_G(c,d)=g_A4(u_c,u_d),              (T4-1)
```

and the finite Riesz map is an isomorphism. The quotient construction is harmless
but trivial; it is not a physical carrier replacement.

The DoR-019 content therefore shrinks to the following openly authored residue:

1. `CARRIER_IDENTIFICATION_CERT`: identify R5 `K_cycle` with the forced-semiform
   Hilbert completion and `C_prop` with the completed Hilbert dual on the declared
   dense domain.
2. `A4_AUTOMORPHISM_ISOMETRY_CERT`: require the retained A4 norm to be invariant
   under admitted exchanges/relabelings and antiunitary under reality reversal, or
   provide a disclosed invariant replacement.
3. Correct carrier-unit torsors and their relation to R4 action units, with
   `[R_A]=U_A^-2` and no numerical member selected.

The following are not DoR-019 authored residue:

```text
finite semiform              derived;
fullness                     derived from A2-R10;
visible-current quotient     equal to the full carrier;
rank-preserving source
  inclusion isometry         already ratified by DoR-015 W3;
finite Riesz maps            derived after positivity;
null-sector treatment        scope-empty.
```

The principal's live choices become: adopt the above completed full-carrier package,
request a different carrier metric law, or reject. V002's Q and N options are not
live on the admitted family.

## 6. T5 - fresh attack: W3 provenance double-charge

V002 states

```text
A4_RANK_PRESERVING_ISOMETRY_DERIVED=false
```

and includes rank-preserving A4 stage isometry in the authored certificate and choice
table. DoR-015's decision text already adopts the W3 precision:

```text
finite source restrictions are adjoints of the retained isometric inclusions;
naive truncation is invalid.                      (T5-1)
```

Thus the rank-preserving source inclusion isometry is already ratified on its
certified scope. V002 correctly keeps generic batching merely bounded and correctly
does not create a cycle-creating physical upward quotient map, but it charges the
principal a second time for `(T5-1)`.

```text
FRESH_ATTACK = succeeds
A4_AUTOMORPHISM_ISOMETRY = authored residue
A4_RANK_PRESERVING_SOURCE_ISOMETRY = ratified premise | DoR-015 W3
```

## 7. Final review board

| Claim | Standing |
|---|---|
| forced semiform and radical theorem | **CONFIRMED** |
| finite/full-family `ker(I_K)=0` | **PROVED** by A2-R10 |
| directed-core and semiform-completion injectivity | **PROVED** |
| quotient naturality theorem | **CONFIRMED**, but quotient is the full carrier |
| A4 automorphism isometry | **AUTHORED RESIDUE**, honestly disclosed |
| A4 rank-preserving source isometry | **ALREADY RATIFIED**, V002 provenance defect |
| corrected unit algebra | **CONFIRMED** |
| V002 R2 countermodel as admitted/permanent | **REFUTED** |
| V002 Q/N null branches as live | **REFUTED** on the admitted family |
| completed R5 carrier identification | **TYPE-U / DoR-019 authored residue** |

V002 cannot be ratified unchanged because its lead block, choice table, and final board
all record fullness as `NO_VERDICT`, call the excluded countermodel admitted, and
retain null-sector branches that the adopted realization forbids. A bounded V003 can
repair those statements without changing the confirmed semiform, unit, naturality,
provenance, or DP work.

```text
FULLNESS = PROVEN
METRIC_V002 = NOT_READY (T1.3, T1.5, T1.6; T5)
READY_FOR_DOR019_RULING = no

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
