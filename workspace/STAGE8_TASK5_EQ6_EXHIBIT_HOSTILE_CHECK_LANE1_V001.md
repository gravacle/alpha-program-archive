# STAGE 8 TASK 5 / EQ6 - Q-408 EXHIBIT HOSTILE CHECK - LANE 1 V001

Date: 2026-08-04  
Task: PASTE 504 / Task 5 / EQ6  
Lane: Codex Lane 1  
Custody: adversarial review of Lane 2's primitive-generator exhibit  
Standing: DoR-020 in force conditional on `[EQ6]`

## Lead result

```text
EXHIBIT = KILLED(
  U1_COVARIANCE_ORBIT_IS_NOT_A_DEFINED_NO_SELECTION_FAMILY
  + U3_CYCLE_CREATING_KERNEL_RESTRICTION_IS_FALSE
  + U4_THE_OLD_DIFFICULTY_IS_RELOCATED_INTO_Q_o
  + U6_GLOBAL_SKELETON_AND_NEW_PROFILE_COUNTEREXAMPLES
)

DECISIVE_WITNESS =
  K_old=R,
  K_new=R^2,
  S(x)=(x,0),
  A_new=id,
  A_old=S^* A_new,
  P_R=id,
  H_new=diag(0,1):

  Kern_old(S^* H_new S)=0,
  Res_R^literal(P_R=id) Kern_new(H_new)[(0,1),(0,1)]=1.

SURVIVING_SUBPACKAGE =
  for one fixed compatible physical tuple:
  actual finite path/current maps,
  the Q-408 analysis square,
  the old-cylinder generated-profile square,
  and free composition on that restricted class.

C1_RESUMPTION = N/A
EQ6_STATUS = OPEN
FENCE_BLOCKED_STRUCTURAL_RESULT = false
```

The root is not proved empty.  The review kills this exhibit as the claimed
proof-carrying family.  A repair may retain the full carrier-moduli groupoid,
define a coherent stagewise physical realization, and scope kernel
restriction to the old-cylinder generated class; those repairs are not made
here.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member_bound = false
fixed_point_executed = false
end_test_executed = false
numeric_evaluation = false
measured_constant_compared = false
```

---

## 0. Preflight and standards

### 0.1 Three-line preflight

The locked process was read in full before review.  The artifact hash and
sidecar were verified before its contents were read.

```text
DOES_THE_OBJECT_EXIST = yes | Lane 2 exhibit exists and is sealed
IS_THE_VERSION_CURRENT = yes | register head Q-426
ARE_ITS_INPUTS_PRESENT = yes | exhibit, frontier, regressions, C1, Q-408
PREFLIGHT = PASS
```

| Authority | Verified SHA-256 | Use |
|---|---|---|
| locked process | `e8a4c00d3cd13126bd8d20588419aba344a50d27c6d084a8243ed5494d7721f2` | custody and fences |
| register at Q-426 | `804966650936347aee757876dde897c6a2b9ddfbd0707c3d43ead7e77844d700` | current scope |
| artifact under review | `cd03cc87554b5ec0372e7b3b62662fac12e523f0ce9f63b08200aea9c2bd3e8c` | review target |
| frontier map | `b8294e917531dd4f1731aedd54fd1c52a320840335061bbb4ab872830d001028` | 1A exhibit contract |
| hostile regressions | `510ebda9c05220b3eb229e865a0a41868f5ce166ff2a5805762d540309a6ab1b` | five permanent attacks |
| C1 build | `5203347c9bba7f99c2f033467815defa7ac047f74ea73b313972f44975d250a5` | P4-core handoff |
| minimal-six/equalizer theorem | `288a3d4147cb10f2e51180b21f7c6b2b4749503504c57b8a1121e3925c70c94c` | joint-equalizer attack |
| Q-408 kernel build | `ccb94dfa8927cf8d2ec76cf85ff2f402d02d5aa5673b9d39c214a6de4c92309c` | exact restriction scope |

### 0.2 Exact review standard

The frontier's 1A contract is:

```text
one target-blind actual-Q408 primitive generator per primitive orbit;
actual path/test-form/current/coframe/density data on new edges;
connection/curvature transports;
free-category composition;
common-refinement compatibility;
no abstract kernel and no member selected by a consequence.
```

Q-408's sealed restriction theorem is narrower than the exhibit's new claim:

```text
rank-preserving W3 isometry
  => compression commutes with restriction to the old current cylinder.

cycle creation
  => the new stage has its own current/kernel class;
     no canonical upward map onto the new cycle direction is claimed.
```

That scope distinction is load-bearing below.

---

## 1. Verdict table U1-U6

| Item | Verdict | One-line reason |
|---|---|---|
| U1 generators orbit by orbit | **KILL** | a fixed tuple gives actual maps, but `Q_o=[q]_Cov` is either one unspecified physical orbit or the full moduli family mislabeled as one orbit; the all-stage domain of `iota_o^CTP` is also undefined |
| U2 absolute regressions/smuggling | **KILL** | abstract-kernel, reader-circularity, and target-tuning checks pass on a fixed tuple, but global generator-family nonemptiness is misstated because the coherent all-stage tuple is not constructed |
| U3 composition and refinement | **KILL** | free composition works on the old-cylinder generated class; the claimed arbitrary-profile cycle-creating restriction square is refuted by `(U3-5)` |
| U4 the too-easy question | **KILL** | the former obstruction is relocated into an authored `Q_o` whose physical moduli and coherent master realization are not supplied, then called an exhibit |
| U5 C1 handoff | **KILL / N/A** | the failed exhibit cannot populate C1's P4 core; even a repaired exhibit would not derive cross-orbit bounded geometry or `W5` |
| U6 two fresh attacks | **KILL** | the pure-new-profile witness and coarse/refined global-skeleton contradiction independently refute advertised certificates; conformal rescaling exposes the hidden moduli fork |

---

## 2. U1 - the generator family under maximum audit

### 2.1 What is concrete after fixing one tuple

Fix one compatible tuple

```text
q=(X,N^CTP,iota^CTP,h^CTP,E^CTP,mu^CTP,nabla^CTP,F^CTP). (U1-1)
```

For a fixed finite cellulation `G`, the exhibit's formulas then give genuine
objects:

```text
gamma_(G,e)=iota(r_G(|e|)),
<J_(G,c),a>=sum_e c_e integral_(gamma_(G,e)) a,
(A_G a)(c)=<J_(G,c),a>.                         (U1-2)
```

If distinct edge interiors in that one stage have disjoint local tubes, an
edge-local test form detects each coefficient.  Therefore `A_G` is onto
`K_G^*`, the finite Q-408 kernel is faithful, and a nonzero finite cycle is
not deleted.  Pushforward of the whole fixed tuple gives covariance;
conjugation gives reality; the listed unit classes are consistent; and
restriction along a genuinely compatible subdivision gives the analysis
square.

These fixed-tuple facts pass.  They do not establish the advertised
no-selection family.

### 2.2 The covariance-orbit/moduli dichotomy

The exhibit defines

```text
Q_o=[(X_o,N_o,iota_o,h_o,E_o,mu_o,nabla_o,F_o)]_Cov. (U1-3)
```

and calls it one covariance orbit while claiming that no background or Gram
member was selected.  Those two claims cannot both be read literally.

Take any valid positive Gram field `h` on a compactly supported carrier
neighborhood and, for symbolic `lambda>0`, define

```text
h_lambda=lambda^2 h,
mu_lambda=lambda^d mu.                           (U1-4)
```

The paths, incidence maps, line integrals, Q-408 kernels, reality, and all
finite restrictions are unchanged.  Yet the carrier volume changes by
`lambda^d`.  An admitted relabeling/frame change does not change this volume;
an ordinary pushforward preserves its integral.  Absent a ratified Weyl
gauge identification, `lambda!=1` therefore gives a physically inequivalent
carrier orbit.

Hence exactly one of these readings is possible:

```text
SINGLE_ORBIT_READING:
  one lambda/orbit has been chosen without a carrier-only selection rule;
  hidden member selection.

ALL_TUPLES_READING:
  every lambda and every inequivalent embedding/Gram/connection tuple is
  retained;
  this is a union/groupoid of covariance orbits, not the one orbit stated,
  and every downstream family/uniformity claim must be retyped over it.
                                                               (U1-5)
```

The local existence observation that a finite graph embeds in a coordinate
ball proves that individual tuples exist.  It does not choose the first horn
or define the all-moduli family and its natural transformations on the
second horn.

```text
ONE_COVARIANCE_ORBIT_WITHOUT_SELECTION = false | TYPE-R
REPAIRED_FULL_MODULI_GROUPOID = NOT_BUILT / TYPE-U
U1 = KILL
```

### 2.3 All-stage domain of the path map

There is a second typing failure.  `iota_o^CTP` is declared on the
"complete branch-marked one-skeleton", while `(U1-2)` evaluates it on every
edge image `r_G(|e|)` from every refinement stage.  The artifact supplies no
colimit one-skeleton and no map from that colimit to the physical carrier.

If "complete" means the union of the stagewise edge sets, a coarse edge and
its two refined subedges overlap and cannot be distinct edges of one embedded
graph with pairwise-disjoint open interiors.  If "complete" means one fixed
stage, `iota(r_G(|e|))` is not defined for the new edges of another stage.
This is developed as the second fresh attack in Section 7.

---

## 3. U2 - permanent regressions and smuggling audit

### 3.1 Absolute regression table

| Regression | Independent check | Result |
|---|---|---|
| abstract-kernel substitution | for a fixed `q`, `Gamma` and line integrals precede `A` and `Kern` | **PASS on fixed tuple** |
| circular `pi_Mx` | no reader or localization map defines a generator | **PASS** |
| misstated reader nonemptiness | no reader nonemptiness is claimed | **PASS** |
| Hodge from isometry | no Hodge/closed-range result is inferred | **PASS** |
| objectwise minimum/restriction | no minimum is taken inside this exhibit | **PASS** |
| joint equalizer | the other five roots and J1-J15 remain open | **PASS** |

The exhibit is therefore not killed by the old abstract-operator or reader
circularity failures.  Its failure is earlier: the global physical family it
uses to make the fixed-tuple construction simultaneous is not exhibited.

### 3.2 Nonemptiness is proved only stagewise

The existence argument establishes:

```text
for each one finite graph, there exists a tame embedding, a positive Gram
field, a coframe torsor, and compatible connection data.              (U2-1)
```

The root requires:

```text
there exists one covariance-compatible family over every primitive orbit,
with stage maps, common refinements, and all generator squares.        (U2-2)
```

`(U2-1)` does not imply `(U2-2)`.  The complete-skeleton conflict, the
moduli dichotomy, and the cycle-creating restriction failure are exactly the
missing compatibility data.  Calling the entire collection `Q_o` does not
prove the equalizer nonempty.

### 3.3 Smuggling and target-awareness

The physical carrier datum is openly authored, and no response, threshold,
fixed point, end test, or measured value is used.  Edge-separating test forms
are required by Q-408 membership rather than selected for a downstream
number.  The construction is therefore target-blind at the fixed-tuple
level.

The defect is not hidden response tuning.  It is schema-passed-as-instance:
the compatibility predicates are written into the definition of `Q_o`, and
the definition is then used as its own inhabitance proof.

```text
ABSTRACT_STANDIN_USED_ON_FIXED_TUPLE = false
CIRCULAR_READER_USED = false
TARGET_TUNING_USED = false
GLOBAL_GENERATOR_FAMILY_NONEMPTY = not_proved
U2 = KILL
```

---

## 4. U3 - composition and refinement recomputation

### 4.1 What composes correctly

For nested compatible subdivisions

```text
K_0 --S_R--> K_1 --S_S--> K_2,
```

line-integral additivity gives

```text
A_0=S_R^* A_1,
A_1=S_S^* A_2,
A_0=(S_S S_R)^* A_2.                            (U3-1)
```

Chain maps, physical restrictions, reality, and fixed master-geometry
pullbacks compose associatively.  With the induced metrics, the adjoint left
inverses compose, so the old-cylinder inclusions satisfy

```text
j_(S o R)^H=j_S^H j_R^H.                        (U3-2)
```

Thus free-category composition is valid on a fixed compatible tuple and on
the generated old-cylinder profile class.

### 4.2 The cycle-creating restriction claimed in V001

V001 goes further.  For an arbitrary new-stage profile `H'`, it claims

```text
Kern_G^fin(S_R^* H' S_R)
  =Res_R Kern_(G')^fin(H').                     (U3-3)
```

while also setting `P_R=id` on the common physical test-form space.  Q-408
proved this only for rank-preserving W3 isometries and explicitly left a
new cycle with its own current/kernel class.  V005's actual P4 membership
condition requires only the old-cylinder generated statement

```text
Kern_G^fin(H)
  =Res_R Kern_(G')^fin(j_R^H H).                (U3-4)
```

The stronger `(U3-3)` is false.

### 4.3 Explicit pure-new-profile counterexample

Use real finite carriers with identity metrics:

```text
K_G=R,
K_(G')=R^2,
S_R x=(x,0),
T=R^2,
A_(G')=id_(R^2),
A_G=S_R^* A_(G'):(a_0,a_1)|->a_0,
P_R=id_T.                                        (U3-5)
```

All analysis and metric equations in V001 hold.  Let the new profile be

```text
H'=diag(0,1).                                    (U3-6)
```

Then

```text
rho_R^H(H')=S_R^* H' S_R=0,
Kern_G^fin(rho_R^H H')=0.                        (U3-7)
```

But for the physical test form `a=b=(0,1)`, which detects the new cycle,

```text
Kern_(G')^fin(H')[a,b]
 =H'(A_(G')a,A_(G')b)=1.                        (U3-8)
```

Because `P_R=id`, literal physical restriction does not remove this test
form, so the right side of `(U3-3)` is nonzero.  If `Res_R` is instead
defined to project onto the old current cylinder, then V001 must supply that
projection as new physical data; it is not `P_R=id`, and the claimed literal
test-form restriction is false.

For `H` on `K_G`, `j_R^H H` has zero new/new and old/new blocks, and
`(U3-4)` passes.  The counterexample therefore locates the exact repair:
scope the certificate to the generated old cylinder, or construct a separate
physical old-cylinder projection.  It does not delete the new profile.

```text
T1_13_ARBITRARY_PROFILE_SQUARE = false | TYPE-R
CYCLE_CREATING_RESTRICTION_REGRESSION = FAIL
FREE_COMPOSITION_OLD_CYLINDER = PASS
U3 = KILL
```

### 4.4 Effect on common-refinement diamonds

Cellular chain subdivision of a coarse chain into a fixed compatible common
subdivision is path-independent.  Therefore the current/analysis diamond
can pass on the coarse image.  V001's statement that the "complete physical
diamond" commutes for arbitrary common-stage kernels relies on the false
`(U3-3)` scope.  What is proved is the old-cylinder restriction diamond;
new-cycle blocks remain independent and are not compared by the old stage.

The raw construction `Sd(G_1 meet_X G_2)` also presupposes that the two
cellulations are geometric in one already fixed compatible PL structure.
Same-region homeomorphisms alone do not provide that common affine
realization.  A common subdivision may exist, but the canonical covariant
choice claimed here belongs to the missing family data identified in U1.

---

## 5. U4 - the formal too-easy question

### 5.1 Where each former obstruction went

| Former obstruction | V001 location | Audit |
|---|---|---|
| actual new-edge path | `iota_o r_G(|e|)` | valid for a fixed compatible tuple; all-stage domain unbuilt |
| physical test forms/current | one fixed `T_o`, edge-local forms | valid stagewise; global compatibility conditional |
| coframe/density | arbitrary positive `h_o`, its torsor and volume | openly authored but retains untyped physical moduli |
| connection/curvature | Levi-Civita part plus full U(1) affine carrier | a lawful family type, not a selected physical member |
| common refinement | overlay plus barycentric subdivision | requires the common geometric realization it is invoked to prove |
| cycle-creating kernel square | `(T1-13)` | false beyond the old-cylinder generated class |

### 5.2 Genuine insight versus relocated definition

The fixed-tuple construction is a genuine observation: once one actual
carrier, embedding, and Gram field are supplied coherently, Q-408's finite
paths and old-cylinder maps follow.  That is useful surviving mathematics.

The claimed full-root inhabitance is obtained by defining `Q_o` to contain
the very globally compatible data whose existence was open.  The local graph
embedding theorem does not prove that family equalizer inhabited, and the
first new finite calculation refutes one of its required squares.  Therefore
the successful appearance comes from relocating the hard content into the
definition, not from constructing all of it.

```text
FIXED_TUPLE_CONSTRUCTION_INSIGHT = genuine
FULL_FAMILY_INHABITANCE = definitionally_relocated / not_proved
U4 = KILL
```

---

## 6. U5 - C1 handoff

The survival condition is not met, so no C1 resumption is licensed.

For scope only, a repaired exhibit would hand C1 the actual full P4 image
`S_phys` and the primitive-orbit maps.  C1 would then have to execute, in
order:

```text
1  form the complete covariant local-seminorm orbit P_phys;
2  prove cross-orbit bounded-geometry estimates;
3  prove the componentwise bound infimum finite and attained;
4  exhibit positive covariant W5;
5  prove ||.||_5 generates exactly the same physical topology;
6  complete and extend Jbar/Kernbar.              (U5-1)
```

V001 expressly supplies neither steps 2-5.  The rescaling family `(U1-4)`
and the path-length countermodel from the C1 build show why the P4 exhibit
would not make them automatic.  Retaining all Gram/carrier members enlarges,
rather than removes, the uniformity burden.

```text
C1_RESUMPTION = N/A
HYPOTHETICAL_REPAIRED_HANDOFF = TYPED_BY_(U5-1)
CROSS_ORBIT_BOUNDED_GEOMETRY_DERIVED = false
HILBERTIZABLE_W5_DERIVED = false
U5 = KILL / HANDOFF_NOT_ACTIVATED
```

---

## 7. U6 - fresh attacks

### 7.1 Fresh attack A: pure-new-profile restriction

The witness `(U3-5)`--`(U3-8)` is not in V001's battery.  It preserves the
analysis square, metric isometry, old-cylinder inclusion, reality, and units,
then isolates one pure new-cycle profile.  It directly refutes the advertised
cycle-creating restriction and the corresponding "complete physical diamond"
scope.

```text
FRESH_ATTACK_A = KILL
```

### 7.2 Fresh attack B: the complete-skeleton subdivision conflict

Take a coarse interval edge `e` and its refinement into consecutive edges
`e_1,e_2`.  Physical refinement requires

```text
gamma_e=gamma_(e_1) concatenated gamma_(e_2).     (U6-1)
```

If the "complete one-skeleton" contains `e,e_1,e_2` as distinct embedded
edges, the open image of `e` overlaps the open images of `e_1,e_2`.  This
contradicts V001's claim that open edge interiors in the embedded complete
skeleton are disjoint.  If the coarse edge is instead identified with the
refined chain, the domain is a directed colimit/stratified carrier, not the
finite embedded graph for which V001 invokes the tubular-neighborhood
theorem.  No such colimit carrier or tubular system is constructed.

```text
FRESH_ATTACK_B = KILL
```

### 7.3 Fresh attack C: conformal-modulus exposure

The symbolic rescaling `(U1-4)` preserves every Q-408 finite result but
changes the density and local geometry.  It proves that covariance alone
does not collapse the carrier family to one orbit and that C1 cannot inherit
a uniform geometry from this exhibit.

```text
FRESH_ATTACK_C = KILL_OF_ONE_ORBIT_CLAIM
U6 = KILL
```

---

## 8. Falsifiers, accounts, and final disposition

### 8.1 Finite and permanent checks

| Check | Result |
|---|---|
| one-edge/tree `K_G=0` | **PASS on fixed tuple** |
| reciprocal loop finite paths | **PASS on fixed tuple** |
| S8-A edge exchange | **PASS family-covariantly on fixed tuple** |
| identity zero-extension | **PASS** |
| rank-preserving `Ref_path` square | **PASS** |
| old-cylinder generated-profile square | **PASS** |
| arbitrary-profile cycle-creating square | **FAIL / `(U3-8)`** |
| reality and units | **PASS on fixed tuple** |
| abstract-kernel regression | **PASS** |
| circular-reader regression | **PASS** |
| false family-nonemptiness regression | **FAIL** |
| Hodge-from-isometry regression | **PASS** |
| objectwise-minimum regression | **PASS** |
| joint-equalizer regression | **PASS; joint EQ6 not claimed** |

### 8.2 Six-account rows

| Account | Review result |
|---|---|
| measure | symbolic `mu=vol_h` supplied for a fixed tuple; family modulus unresolved |
| contour | CTP branches retained; no downstream contour integration |
| boundary/contact | no response cocycle or contact ideal claimed |
| domain closure | no completion performed |
| stationary Schur | not touched |
| class formation | covariance orbit/groupoid claim fails the orbit-versus-moduli audit; no weak-star step |

### 8.3 Anti-tuning and fences

The review used only carrier types, finite linear algebra, topology of the
declared refinement, and the sealed restriction scope.  No response value,
threshold, fixed point, end test, alpha, root, or measured constant was
computed or compared.

```text
TARGET_TUNING_USED = false
MACHINERY_APPEAL = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false
```

### 8.4 Final lines

```text
EXHIBIT = KILLED(
  U1 + U3 + U4 + U6;
  anatomy = undefined orbit/moduli family
            + false arbitrary-profile cycle-creating restriction
            + undefined all-stage embedded skeleton
)

C1_RESUMPTION = N/A

SURVIVES_FOR_REPAIR =
  fixed-compatible-tuple Q408 paths/currents
  + analysis square
  + old-cylinder generated-profile restriction
  + free composition on that scope.

JOINT_EQ6 = OPEN
EQ6_MEMBER_BOUND = false
DOWNSTREAM_CONDITIONAL_EXECUTION_STARTED = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member_bound = false
fixed_point_executed = false
end_test_executed = false
numeric_evaluation = false
measured_constant_compared = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false
```
