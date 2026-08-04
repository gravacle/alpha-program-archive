# STAGE 8 TASK 5 - CROSS-CHECK OF THE LICENSED CONDITIONAL CHAIN - LANE 1 V001

Date: 2026-08-04
Task: PASTE 522 / Task 5
Lane: Codex Lane 1
Custody: adversarial cross-check of Lane 2 artifact

## Lead result

```text
CHAIN = KILLED (M1, M2, M3, M4, M5, M6)

TEN_STEP_MAP = DEFECTIVE (steps 3-4)

LOAD_BEARING_DEFECT_1 =
  [EQ6] inhabits the continuum-package J1-J15 equalizer; it does not
  inhabit the separate GLOBAL_STATIONARY_RETURN_REGULARITY_AND_COMMON_READER
  certificate.  The reviewed artifact silently supplies D_w, S_w, full
  stationarity, B_w(D_w) subset D_w, and regularity from [EQ6].

LOAD_BEARING_DEFECT_2 =
  q_loop=sup_D |partial_K B| is exact only on the interval/convex C1 or
  absolute-continuity scope stated by the scalar-carrier authority.  The
  reviewed artifact assumes only that D_w is a nonempty closed subset of
  the scalar line.

COUNTEREXAMPLE =
  D={-1,1}; B(k)=k^3/2-3k/2;
  B(D)=D; B'(-1)=B'(1)=0; derivative-sup=0;
  true Lipschitz modulus=1; B has no fixed point in D.

PROTECTED_ACTION_AUDIT = CLEAN
  member binding, fixed-point execution, end test, numeric evaluation,
  and measured-constant comparison were not performed.

REQUIRED_CONDITION =
  [EQ6] + independently certified C_ret + interval/absolute-continuity
  branch scope (or use q_true as the difference quotient without replacing
  it by a derivative supremum).
```

The artifact contains useful conditional algebra, but its condition is too
weak for the conclusions attached to it.  The failure is not a numerical or
physical evaluation issue.  It is a logical-domain mismatch between three
different objects: the DoR-020 equalizer witness, the stationary-return
certificate, and the convex differentiable branch required by the exact
derivative modulus.

## 0. Preflight and authority verification

### 0.1 Three-line preflight

```text
DOES_THE_OBJECT_EXIST = yes
IS_THE_VERSION_CURRENT = yes_through_Q-447
ARE_ITS_INPUTS_PRESENT = yes
PREFLIGHT = PASS
```

The artifact under review was hash-verified before reading:

```text
STAGE8_TASK5_LICENSED_CONDITIONAL_CHAIN_LANE2_V001.md
dda80773a472d9368b1f7fc71593b6ebe1b9d263759b5c8f77895cc0ee7b9320
```

The canonical `LOCKED_PROCESS.md` was read in full at SHA-256
`d537e294c03b3fc50fa49844f5b166bdcee1d64fe1513b9201047f602cd1518f`.
The register ended at Q-447 at preflight, SHA-256
`cd8466f0d51a05af7eb6af85461c2c182b2dea3b8fc629620cff033e21e3ede4`.

The load-bearing standards were independently hash-verified:

| Authority | SHA-256 | Use |
|---|---|---|
| Q-401 conditional theorem | `88854f08966c15e6afbcb300c6151f59a169e2725c3d5a8643b653abfe3ddcb3` | Banach and sensitivity implications |
| Q-404 return-certificate build | `b569a89e661ad92b744213bfc7cd65985908bc509b8dd9de77bcae3a2bdb4bad` | exact `C_ret` interface and threshold scope |
| local orthogonal excision certificate | `d61a550a33bf1215c35f4d6f27cd2ec5d644b93a05e16d08fe3d43ded3416817` | geometric refinement certificate, not stationary return |
| scalar carrier/modulus build | `aebe708d2e7ba4b67e828976bd01eae2d5eec04afbb6a28f3f77f9dc8003fc97` | exact difference-quotient modulus and derivative conditions |
| continuum constraint system | `d7dcbc3ad7c470c8aaf0d8407db625d3e910cf180cd7b035fbc96bdfe58471b4` | J1-J15 content |
| DoR-020 | supervision seal verified | conditional license and prohibitions |

### 0.2 Governing logical distinction

DoR-020 defines `[EQ6]` as nonemptiness of one joint J1-J15 equalizer over
six continuum generators.  Its live variables are the completed
representative, reader, scalar-K action path, refinement data, completion
data, response/boundary data, and faithfulness data.  J1-J15 impose their
compatibility.

The Q-404 return authority separately defines an inhabitant

```text
C_ret=(D,O_phys,{ell},{S_I},{H_I},{B_(I,ell)},bounds,certs)
```

and explicitly records the following as unbuilt: a nonempty physical `D`, a
global stationary solve `S_I:D->Crit_I`, full residual equations, return
`B(D) subset D`, and branch regularity.  Neither DoR-020 nor J1-J15 adds an
equation asserting these objects.

The local orthogonal excision certificate is a refinement-geometry proof
object.  It cannot substitute for `C_ret`.  The reviewed artifact correctly
says this in prose, then incorrectly makes the same joint witness `w`
supply both objects.

## 1. Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| M1 | **KILL** | The boundedness inequality and closure implication recompute, but `[EQ6] -> inhabitant(C_ret)` is absent; closure is merely the missing RETURN premise restated. |
| M2 | **KILL** | The Schur derivative is correct on a fixed C1 carrier, but the equality of derivative supremum with the true modulus omits the authority's interval/convexity or absolute-continuity hypothesis. |
| M3 | **KILL** | The displayed closed-domain counterexample satisfies return and has `A_loop=0`, yet has modulus one and no fixed point; no protected execution occurred. |
| M4 | **KILL** | The sensitivity identities are valid only under the extra return, common-domain, differentiability, and strict-modulus hypotheses; they are not execution-ready under `[EQ6]` alone, and the Q-396 equality needs its special deformation scope. |
| M5 | **KILL** | Steps 3-4 treat `C_ret` and its branch scope as supplied by the package witness; a distinct construction/certification gate is missing. |
| M6 | **KILL** | Mechanical tags and protected-action flags pass, but semantic `[EQ6]` tagging hides two additional premises; both fresh attacks land. |

## 2. M1 - boundedness and closure

### 2.1 Recomputed conditional inequality

If an independently supplied return certificate gives

```text
||S(K)-S(K')|| <= L_G |K-K'|,
||Pi(G)-Pi(G')|| <= L_Pi ||G-G'||,
|ell(H)| <= M_ell ||H||,
```

then composition gives

```text
|B(K)-B(K')|
 =|ell(Pi(S(K))-Pi(S(K')))|
 <=M_ell L_Pi L_G |K-K'|.
```

The memberwise reader normalization gives `M_ell=1` on its compatible
completed norm.  This part is correct as an implication.

If the same independently specified certificate proves `B(D) subset D`,
closure follows.  It does not follow from scalar codomain typing,
completeness, reality, or finite shadows.  Q-404 states exactly that.

### 2.2 The illegal implication

The reviewed chain defines

```text
w in Eq6 = joint J1-J15 witness over the six DoR-020 generators
```

and then asserts that the witness clauses provide `D_w`, `S_w`, full
stationarity, return, and regularity.  The source equalizer has no such
clauses:

```text
J5  anchors a regular scalar-K action path to R1;
J12 response naturality;
J13 boundary/contact coherence;
J14 completion/faithfulness;
J15 finite restriction.
```

None says that the stationary equations have a solution for every `K`, that
the solution graph is regular, or that the scalar reading returns to an
independently specified domain.  A package equalizer term can therefore
exist while `Crit_I(K)` is empty at some `K`, or while `B(D)` leaves `D`.
Changing that downstream stationary fact does not alter J1-J15.

Correct type:

```text
[EQ6] and inhabitant(C_ret)
  -> boundedness and closure implications.

[EQ6] alone
  -/-> inhabitant(C_ret).
```

## 3. M2 - `A_loop` and the true modulus

### 3.1 Schur differentiation

For fixed carrier maps and total scalar-branch derivatives,

```text
Schur=D-C A^(-1) B,
d(A^(-1))/dK=-A^(-1) dot(A) A^(-1),

dot(Schur)
 =dot(D)-dot(C)A^(-1)B
  +C A^(-1)dot(A)A^(-1)B
  -C A^(-1)dot(B).
```

The signs and the four terms in the reviewed artifact are correct.  On the
one-dimensional reciprocal-loop operator line,

```text
RetExtract[dot(Schur)(K)]=a_loop(K) Rhat_K,
partial_K B(K)=chi_K a_loop(K)
```

when the reader and `RetExtract` carrier are fixed along the branch.  The
symbol ownership is also correct: `p`, `nu`, the completion member, and the
stationary motion remain inside `a_loop`; `chi_K` is the reader coordinate.

### 3.2 Exactness boundary omitted

The scalar-carrier authority first defines the true modulus by the
difference quotient:

```text
q_true=sup_(K!=K' in D)|B(K)-B(K')|/|K-K'|.
```

It replaces this by `sup_D |partial_K B|` only when `D` is an interval (or a
convex branch), the branch is C1/absolutely continuous, and the derivative
is controlled along the connecting segment.  Otherwise the derivative
supremum is only a candidate bound under additional extension hypotheses.

The reviewed chain assumes merely

```text
D_w is a nonempty closed subset of Scalar_dimless^real.
```

A closed subset can be disconnected.  Thus `(L2-10)` is not the true
modulus on the stated scope, and `q_loop=|chi_K| A_loop` is not established
as a Lipschitz equality there.

## 4. M3 - conditional existence and uniqueness

### 4.1 Counterexample on the chain's stated domain

Take

```text
D={-1,1},
b(k)=k^3/2-3k/2,
H(k)=b(k) Rhat_K,
ell[Rhat_K]=chi_K=1.
```

Then

```text
b(-1)=1,
b(1)=-1,
b(D)=D,
b'(k)=3k^2/2-3/2,
b'(-1)=b'(1)=0.
```

Therefore the chain's derivative coefficient gives

```text
A_loop=sup_(k in D)|b'(k)|=0,
q_loop_reported=|chi_K| A_loop=0.
```

But the exact difference quotient is

```text
q_true=|b(1)-b(-1)|/|1-(-1)|=|-1-1|/2=1.
```

The map swaps the two points, so it has no fixed point in `D`.  The chain
would invoke its `A_loop=0` horn and conclude a strict contraction with one
fixed point.  That conclusion is false.  The counterexample is C1 on the
ambient real line, `D` is nonempty, closed, and complete, and the self-map
condition holds.  The missing condition is exactly the interval/convex
branch condition named by the authority.

### 4.2 DoR-020 prohibition audit

No prohibited action was executed in the reviewed artifact:

```text
MEMBER_BINDING = false
FIXED_POINT_EXECUTION = false
END_TEST = false
NUMERIC_EVALUATION = false
MEASURED_CONSTANT_COMPARISON = false
```

The defect is in the theorem statement, not in an illicit execution.

## 5. M4 - sensitivity systems

### 5.1 Algebraic recomputation

On a common domain with a uniform genuine modulus `q<1`, the standard
difference estimate is correct:

```text
|K_theta-K_theta'|
 <=(1-q)^(-1) sup_D |B_theta-B_theta'|.
```

On a differentiable simple branch,

```text
F(K,theta)=K-B_theta(K),
(1-partial_K B) delta_theta K=delta_theta B,
delta_theta B=ell[delta_theta H]+(delta_theta ell)[H].
```

The pure reader numerator `eta[H]` and the distinguished `chi_K` direction
are correct when the response is formed before the reader acts.  The
Q-396 identity

```text
delta H=RetExtract[D_K^2 Psi]
```

is exact only for the special complement-independent Q-396 deformation for
which the critical family and the A/B/C blocks are unchanged.  It is not an
identity for an arbitrary admissible completion tangent.

### 5.2 Standing

These are valid formal systems under all of:

```text
one EQ6 witness;
one independently certified C_ret inhabitant on that same member;
one common domain/topology;
the genuine q_true<1 condition;
differentiability for the differential systems;
Psi restricted to the Q-396 prepared family for the displayed D_K^2 term.
```

The reviewed artifact records some of these locally but labels the final
systems as `[EQ6]` consequences.  They are therefore not execution-ready on
the condition it declares.

## 6. M5 - ten-step authorization map

Steps 1-2 correctly separate witness construction from reviewer
certification.  Steps 5-10 correctly preserve fixed-point, Task-6, A32,
evaluation-DoR, and end-test gates.  No protected step was run.

The defect is at steps 3-4:

```text
step 3 says the certified package witness supplies C_ret and stationary maps;
step 4 gates D,S,H,B,A_loop and return bounds only on that witness.
```

DoR-020 supplies no such implication.  Between package-member binding and
threshold use the map needs a distinct action and certificate gate:

```text
construct and independently certify C_ret on the bound package member;
prove D is interval/convex with C1/absolute-continuity branch scope,
or retain q_true as the difference quotient and prove it directly;
only then instantiate A_loop and decide contraction.
```

Thus the map is not exact.  The defect is not merely renumbering: a currently
unbuilt physical object is absent from the authorization path.

## 7. M6 - tags, smuggling, and fresh attacks

### 7.1 Mechanical and protected-action scans

Every nonblank line of the reviewed artifact begins with the literal
`[EQ6]` tag.  No true-valued protected-action flag, bound member, fixed-point
iterate, evaluated modulus, end-test result, or measured-constant comparison
appears.  The mechanical scan passes.

The semantic scan fails.  A condition tag cannot make an unlisted premise a
consequence of the condition.  Two objects are smuggled under `[EQ6]`:

```text
1. inhabitant(C_ret);
2. interval/convex or absolute-continuity scope for the exact modulus.
```

### 7.2 Fresh attack 1 - equalizer/return independence

Hold one J1-J15 continuum tuple fixed.  Change only the downstream
stationary residual so that no global `S:D->Crit` exists, or so that the
reader image leaves an independently selected `D`.  Every J equation remains
unchanged, while `C_ret` fails.  Therefore one joint witness index does not
solve the marginal-package attack: all maps can share `w` and still lack the
return leg.

```text
FRESH_ATTACK_1 = LANDS
```

### 7.3 Fresh attack 2 - disconnected-domain swap

The polynomial swap in Section 4 passes completeness and return while
making the derivative supremum zero and the true modulus one.  It refutes
the claimed exact threshold and the fixed-point conclusion on the artifact's
own stated domain class.

```text
FRESH_ATTACK_2 = LANDS
```

### 7.4 Geometry/rails split

```text
RAILS =
  Banach implication, Schur derivative algebra, certificate shapes,
  refinement/excision equations, and the ten procedural gates.

SURFACE_GEOMETRY_AND_FIELD_CONTENT =
  an actual EQ6 witness, the global stationary solution/return family,
  its physical scalar domain, and its regularity on connecting branch arcs.
```

The rails cannot manufacture either the stationary-return inhabitant or the
branch geometry.  Treating both as fields of `w` relocates, rather than
solves, the physical construction burden.

## 8. Final board

```text
M1 = KILL
M2 = KILL
M3 = KILL
M4 = KILL
M5 = KILL
M6 = KILL

CHAIN = KILLED (M1: EQ6 does not entail C_ret;
                M2-M3: exact-modulus scope missing;
                M4: sensitivity scope overstated;
                M5: missing C_ret/branch gate;
                M6: semantic premise smuggling)

TEN_STEP_MAP = DEFECTIVE (steps 3-4)

REPAIR_BOUNDARY =
  retag the analytic chain by [EQ6 AND C_ret], then either add the
  interval/absolute-continuity certificate or use and prove the exact
  difference-quotient q_true.  Insert these as explicit gates before any
  threshold or fixed-point step.

MEMBER_BINDING = false
FIXED_POINT_EXECUTION = false
END_TEST = false
NUMERIC_EVALUATION = false
MEASURED_CONSTANT_COMPARISON = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false
MACHINERY_APPEAL = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
