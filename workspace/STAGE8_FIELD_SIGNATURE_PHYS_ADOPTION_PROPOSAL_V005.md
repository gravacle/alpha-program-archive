# FIELD_SIGNATURE_PHYS V005 — TRIANGULATED GATE-4 QUOTIENT, UNAUGMENTED CYCLE CURRENTS, AND PHYSICAL SEPARATION

**PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL RATIFICATION (DoR-015 RESERVED)**

**Status:** `V005_COMPLETE_FOR_THIRD_FINAL_ADVERSARIAL_REVIEW`

**Register head at start:** Q-297, register SHA-256
`65d8808b0f031f6fb9656174b497efb48234258426380dc9e2d3d1857e37f0da`.

**Scope:** one structural replacement after the Q-294/Q-297 triangulation.
V005 removes V004's augmented endpoint-frame source, retains V004 Door F,
and replaces the over-fine framed visibility carrier by the exact finite
Gate-4 quotient followed by all-finite path visibility. The six authored
fields, full torsor family, endpoint intertwiners, D0 theorem, and every
Q-293 survivor remain unless this artifact explicitly retargets their domain.

```text
PROPOSAL_PAGE_FLAG = PROPOSED_NOT_ADOPTED -- PENDING PRINCIPAL RATIFICATION

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

---

## 1. Authorities, roots, and exact preflight

### 1.1 Frozen authorities

| Authority | SHA-256 | Load-bearing use |
|---|---|---|
| `STAGE8_FIELD_SIGNATURE_PHYS_V004_FINAL_ADVERSARIAL_REVIEW_DETERMINATION_V001.md` | `a2fc3b98bec23bd1b3b8db23467ae17ca0bbbdc0fe7fb95c395b67f115ac77db` | Q-297 kill, incidence split, surviving Door F, and successor option 1 |
| `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V004.md` | `5a8d5598716e26eabdc90a58e8e61acf7021a2a03129b60875d5bd265bd741e6` | Door F and bounded door-accounting base; augmented current removed |
| `STAGE8_FIELD_SIGNATURE_PHYS_V003_FINAL_ADVERSARIAL_REVIEW_DETERMINATION_V001.md` | `6e191e562988180f4a7051ca3601d051cce7bcc7689d9f68cfd1afeffe3274f4` | Q-294 over-fine tangent counterexample |
| `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V003.md` | `a5a8420da4878f735553b1cc7870d2e722b0bb039328621070bcb29fc066aaa2` | S3 finite identifying functor, full frame family, and endpoint intertwiner |
| `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V002.md` | `deaa86ee58edb9f841ae3f7bae8ccf9b1cf659328b99fb60cd290a348641e1ad` | six-field baseline and original seam definitions |
| `STAGE8_TASK4A_RECORD_SURFACE_TO_PHYSICAL_FIELD_SIGNATURE_DERIVATION_AND_BETA_GAP_ATTACK_V001.md` | `65e4dd6a6e2926c9c100edb162f57352311e73438f23dd19509dda0403e2e4f6` | derived/authored split and residue accounting |
| `STAGE8_TASK4A_P5_MAXIMAL_TRANSPORT_CHAIN_AND_DEPENDENCE_ACCOUNTING_PACKAGE_V002.md` | `31a738ec17696ea01e1cb6a6ee7a37a29e6c0ca24d6fb8cc050d06aed32a583f` | Q-288 mandatory door fields (`:572-629`) |
| `32_GATE4_DIFFERENTIAL_UNIQUENESS_RESULT_V001.md` | `a0d8b3f71632bd56cc3646fa59e84a2c2776539fadf04be733c7a1eaa997bdbb` | derived vertex-gauge quotient and physical loop-holonomy class (`:9-31`) |
| `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md` | `57c06fcbedf4a486b87b42c02e6d13a92096ac6a56751d3ae5fd55f4b11deb57` | source/bilocal and endpoint-intertwiner contracts (`:641-688`) |
| `STAGE8_TASK4D_STITCHING_THEOREM_GERM_INDEPENDENT_HALF_V001.md` | `430f09715146cc03dabb0e349c422ae2499cff893d4e46b490fc0870954d1cb4` | separated `T_cyl` and finite retractions (`:213-243`) |
| `STAGE8_COMPOSITION_LOOP_STRUCTURAL_PREDICTION_BUILD_V001.md` | `5810377123b823e680891a3337855750ac8f362951dca048dad3a78a34c79d79` | instantiated surviving cycle witness, not a curvature face (`:186-225,300-322`) |

### 1.2 Roots entered

```text
ROOTS_ENTERED = (
  /Users/bgm/Documents/New project/gravity_emergence_evidence_program/
    alpha_fundamental_record_action_cleanroom_v003,
  /Users/bgm/MB Work/alpha-program-archive/cleanroom_output,
  /Users/bgm/MB Work/alpha-program-archive/workspace,
  /Users/bgm/MB Work/alpha_supervision
)

EXCLUSIONS = (
  a32_holdout/custodian_private,
  every response/value/root/rank-member/background-member evaluation,
  every measure/contour/boundary/domain construction,
  every register/plan/tracker/git/commit/push act
)
```

The fenced holdout was not opened, listed, or searched.

### 1.3 Preflight answers

```text
DOES_THE_OBJECT_EXIST = THE_SHAPE_AND_INPUTS_EXIST; V005_ITSELF_DID_NOT
IS_THE_VERSION_CURRENT = YES_THROUGH_Q297
ARE_INPUTS_PRESENT = YES
```

Q-297 is binding. It establishes that V003 S3 is the finite identifying map,
that the Q-294/V004 endpoint tangent is vertex gauge, that `u^aug` does not
descend, and that Door F survives independently
(`...V004_FINAL_ADVERSARIAL_REVIEW...:18-87,175-342,346-398`).

---

## 2. Lead precision: what “unaugmented currents” means after the quotient

V005 uses no endpoint-frame term. Let

```text
(L_N a)_e = integral_(gamma_e) a,
(B_N theta)_e = theta_t-theta_s.
```

The Gate-4 tangent is `coker(B_N)`. Therefore an individual open-edge scalar
`(L_N a)_e` is not, by itself, a scalar covector on the quotient: its physical
dual is the annihilator

```text
ker(B_N^T) = {c in R^(E_N): B_N^T c=0}.
```

The canonical physical current is consequently the basis-free family

```text
u_c(a) = <c,L_N a>
       = sum_(e in E_N) c_e integral_(gamma_e) a,
c in ker(B_N^T).
```

Every term is an original unaugmented connection current. No `theta_t-theta_s`
is added. The coefficients are conserved cycle currents, not a selected cycle
basis.

This is the exact meaning of Q-297's successor option 1: “cycle-holonomy/
`coker(B)` source content” (`...V004_FINAL_ADVERSARIAL_REVIEW...:562-573`).
Literal individual open-edge `u_e` does not descend unless its edge coefficient
lies in `ker(B_N^T)`. V005 does not hide that quotient fact.

```text
V004_AUGMENTED_CURRENT_RETAINED = false | TYPE-R |
  test: u_e^aug is absent from every V005 definition and consumer

INDIVIDUAL_OPEN_EDGE_CURRENT_IS_GATE4_SCALAR = false | TYPE-R |
  test: its coefficient need not annihilate im(B_N)

PHYSICAL_CURRENT_FAMILY = UNAUGMENTED_CYCLE_CURRENTS_u_c
PHYSICAL_CURRENT_REQUIRES_SELECTED_CYCLE_BASIS = false | TYPE-R |
  test: the whole canonical kernel ker(B_N^T) is retained
```

This bounded correction is not a fourth route. It is the dual statement of
the quotient Q-297 ordered. Calling every raw open-edge coordinate physical
would recreate Door A's killed non-invariant cylinder in source notation.

---

## 3. The finite triangulated quotient

### 3.1 Gate-4 action and quotient coordinate

For the finite realized graph `G_N=(V_N,E_N)`, let

```text
Gamma_N = U(1)^(V_N),
(g.H)_e = g_t H_e g_s^(-1),
Q_N = U(1)^(E_N)/Gamma_N,
q_N:U(1)^(E_N)->Q_N.
```

The componentwise stabilizer is harmless; equivalently one may divide
`Gamma_N` by constants on each connected component. No representative or
spanning tree is selected.

V003 S3 supplies the finite equivariant map

```text
T_iota,p(U_e)=h_e(A,p),
T_iota,p(g_t U_e g_s^(-1))=g_t h_e(A,p) g_s^(-1)
```

(`V003:702-719`). Hence it induces the quotient map

```text
K_N = q_N compose H_N:X_N^fr -> Q_N.
```

### 3.2 Door-F compatible framed family

Retain V004's exact projective carrier

```text
X_inf^fr={(x_N)_N:r_MN(x_M)=x_N},
```

formed by Door F. Equivariance of `r_MN` makes the finite `K_N` compatible.

### 3.3 One combined physical relation

Define **one** relation on `X_inf^fr`:

```text
x ~phys y
  iff K_N(pi_N x)=K_N(pi_N y) for every finite N,

X_phys^005 := X_inf^fr/~phys
            isomorphic to image(K=(K_N)_N).
```

This is exactly

```text
physical = framed / (Gate-4 vertex rephasing + all-finite path-invisible content).
```

It is not a sequential choice of gauges. Equality in `Q_N` absorbs the
Gate-4 orbit; equality at every finite `N` then removes only content invisible
to the complete quotient-coordinate family.

```text
A3_V005_PHYSICAL_QUOTIENT_PROPOSED = true [PROPOSAL FIELD]
GATE4_REPHASING_ABSORBED = true | PROPOSAL-CONDITIONAL THEOREM
PATH_INVISIBLE_CONTENT_ABSORBED = true | PROPOSAL-CONDITIONAL THEOREM
GLOBAL_FRAME_OR_GAUGE_REPRESENTATIVE_SELECTED = false | TYPE-S |
  roots: quotient classes Q_N and X_phys^005 |
  exclusions: local representatives used only in proofs |
  fences: no selection |
  query: distinguished g, frame tuple, section, or spanning tree
```

---

## 4. Exactness: no more and no less

### 4.1 Both prior kill presentations lie in the kernel

The Q-294 tangent and the Q-297 killing tangent are the same finite vertical
motion viewed at two stages:

```text
(a,theta)=(0,theta),
dH_N(0,theta)=i diag(H_N)B_N theta.
```

The tangent quotient map kills `B_N theta`, so

```text
dK_N(0,theta)=0.
```

Thus raw `dH!=0` is representative motion and V004's
`u^aug(0,theta)=B_N theta` is removed with it.

```text
Q294_FRAME_TANGENT_IN_PHYSICAL_KERNEL = true |
  PROPOSAL-CONDITIONAL THEOREM
Q297_VERTEX_REPHASING_TANGENT_IN_PHYSICAL_KERNEL = true |
  PROPOSAL-CONDITIONAL THEOREM
V004_AUGMENTED_FRAME_TERM_SURVIVES_DOWNSTAIRS = false | TYPE-R |
  test: q_lin(B_N theta)=0
```

### 4.2 No physical tangent is removed

By definition, two classes are identified only when **every** finite quotient
coordinate agrees. Therefore a pair with different finite loop holonomy in
any `Q_N` survives.

At tangent level,

```text
T_phys,N = image(L_N) / (image(L_N) intersection image(B_N))
         subset coker(B_N).
```

If `[L_N a]` is nonzero in `coker(B_N)`, then it is not in the physical
kernel. An instantiated witness is the sealed composition loop

```text
c_square=e_a0-e_0b+e_ab-e_ba,
B_N^T c_square=0,
```

whose incidence rank and cycle rank were proved exactly
(`STAGE8_COMPOSITION_LOOP_STRUCTURAL_PREDICTION_BUILD_V001.md:186-225`).
Choose a permitted connection tangent changing its global loop-holonomy
coordinate, structurally characterized by

```text
<c,L_N a> != 0.
```

Its cycle-holonomy coordinate changes and the pair survives. At a tree stage
`ker(B_N^T)={0}` and the phase sector is correctly scope-empty: Gate 4 says
tree phases are gauge.

```text
NONZERO_CYCLE_HOLONOMY_TANGENT_REMOVED = false | TYPE-R |
  test: some finite K_N changes
TREE_PHASE_DECLARED_PHYSICAL = false | TYPE-R |
  test: coker(B_N) is zero on a connected tree
RECORD_VISIBLE_SURVIVING_WITNESS = composition-loop connection pair with
  unequal K_N class along c_square
```

The quotient removes exactly `im(B_N)` plus the common all-finite kernel. It
does not collapse unequal quotient coordinates.

---

## 5. A4 separation with unaugmented quotient currents

### 5.1 Descent

For `c in ker(B_N^T)`,

```text
u_c([L_N a+B_N theta])=<c,L_N a+B_N theta>
                       =<c,L_N a>+<B_N^T c,theta>
                       =u_c([L_N a]).
```

In the proposal's framed tangent notation, pure frame motion has `a=0`, so
the same conclusion is immediate. The displayed equation also proves
representative-independence in the edge-phase quotient.

### 5.2 Separation

Finite-dimensional duality gives

```text
(ker B_N^T)^perp = image(B_N).
```

If `u_c(a)=0` for every `c in ker(B_N^T)`, then `L_N a in image(B_N)`, so
`[L_N a]=0` in `coker(B_N)`. Conversely a nonzero quotient class has some
`c in ker(B_N^T)` with nonzero pairing. Across all `N`, the family of all
finite conserved currents separates `X_phys^005` by the defining all-finite
relation.

Define without choosing a basis:

```text
J_fin^005 = algebraic directed union_N {u_c:c in ker(B_N^T)},
J_phys^005 = completion of J_fin^005 in the retained A4 proposal norm.
```

```text
A4_UNAUGMENTED_CYCLE_CURRENT_DESCENT = PASS_AS_PROPOSAL
A4_PHYSICAL_SEPARATION = PASS_AS_PROPOSAL
A4_INDIVIDUAL_EDGE_BASIS_SELECTED = false | TYPE-S |
  roots: complete kernels ker(B_N^T) |
  exclusions: no spanning-tree or cycle-basis evaluation |
  fences: family discipline |
  query: a distinguished cycle basis
A4_NORM_FORCED_BY_GATE4 = false | TYPE-U |
  would-build: independent physical source-normalization theorem on the
               complete quotient family
```

---

## 6. A5 phase calculus on the physical quotient

An open-edge phase `phi_e` is a representative coordinate and is removed.
For any integer cycle coefficient `c in ker(B_N^T)` in a retained
`Log_0` chart, define

```text
Phi_c([A,p];[A_0,p_0])
  = -i Log_0 product_(e in E_N)
      (h_e(A,p)h_e(A_0,p_0)^(-1))^(c_e).
```

Under vertex rephasing the endpoint factors telescope because
`B_N^T c=0`. Hence `Phi_c` is a scalar on `Q_N`, and

```text
d Phi_c(a)=sum_e c_e integral_(gamma_e) a=u_c(a).
```

No endpoint-frame term appears. No cycle basis or logarithm branch is selected
globally; all admissible local charts remain.

The integer kernel supplies the bounded U(1) characters above. Its real span
is the full Lie-algebra cotangent `ker(B_N^T)` used by A4 separation; incidence
matrices are integral, so this passage selects no basis and loses no real
cycle direction.

The physical bounded cylinder algebra is the invariant subalgebra

```text
Cyl_phys,N = C(U(1)^(E_N))^(Gamma_N)
           isomorphic to C(Q_N),

T_cyl^G = norm closure of the directed invariant finite cylinders in T_cyl.
```

Arbitrary non-invariant `f(H_N)` remains an upstairs presentation function and
is not consumed physically.

```text
A5_CYCLE_PHASE_DIFFERENTIAL = PASS_AS_PROPOSAL |
  identity: d Phi_c=u_c
OPEN_EDGE_PHI_E_IS_PHYSICAL_SCALAR = false | TYPE-R |
  test: it shifts under vertex rephasing
A5_INVARIANT_CYLINDER_ALGEBRA_PROPOSED = true [PROPOSAL FIELD]
A5_SCALAR_PHYSICAL_FUNCTIONAL_BUILT = false | TYPE-U |
  would-build: scalarization, measure/contour package, connected subtraction,
               and physical restriction certificate
```

---

## 7. A6 and the six authored structures

Use the corrected quotient source domain:

```text
E_J,phys^005=J_phys^005,
E_R,phys^005=S_1,sym(H_CTP^005),
Bil_phys^005=Bil_cont(J_phys^005 x J_phys^005;C),
RawGClass^005=Bil_phys^005 intersect D3-real symmetric forms.
```

The abstract bilinear class is separated on its finite conserved-current
core. The physical raw-G image remains unbuilt.

Per-field consumer audit:

| Field | Quotient-invariant consumption |
|---|---|
| A1 | background family unaffected; no member selected |
| A2 | full realization/frame family supplies representatives; physical outputs use only quotient classes |
| A3 | is the combined Gate-4/path-invisible quotient |
| A4 | consumes `ker(B_N^T)` conserved unaugmented currents only |
| A5 | consumes `C(Q_N)` invariant cylinders and cycle phases only |
| A6 | consumes the A4 quotient source domain only |

```text
A6_PHYSICAL_SOURCE_DOMAIN = PASS_AS_PROPOSAL
A6_ABSTRACT_CLASS_SEPARATED = true | PROPOSAL-CONDITIONAL MATHEMATICS
A6_RAW_G_PHYSICAL_IMAGE_EXISTS = false | TYPE-U |
  would-build: scalar physical functional, physical differentiation,
               connected subtraction, lift, restriction square, and Door-D image
INDEPENDENT_AUTHORED_STRUCTURE_COUNT = 6 | PROPOSAL-LEVEL COUNT
```

No authored field is marked `TYPE-P`. Derived/ratified inputs retain their
own standing; consequences on A1-A6 are proposal-conditional.

### 7.1 Six-field choice table

| Field | V005 proposed choice | Live alternatives considered | Minimality / price | Void condition |
|---|---|---|---|---|
| A1 | unchanged full globally hyperbolic oriented Lorentzian U(1)-bundle family | nonsmooth causal locale; fixed member; Euclidean family | preserves the V003 external family without selecting it | family empty or raw-G signature mismatch |
| A2 | unchanged complete causal/support realization and full endpoint-frame torsor family | selected section; selected frames; nonscalar groupoid only | retains all finite representatives required by S3 and chooses none | R1-R10 conflict or family empty |
| A3 | one combined quotient by finite Gate-4 rephasing and all-finite quotient-coordinate invisibility | over-fine raw-H quotient; fixed-frame fiber; authored gauge breaking | exactly the Q-297 triangulation; neither adds nor breaks gauge | unequal finite `K_N` classes become identified, or a killed vertical tangent survives |
| A4 | complete basis-free conserved current family `u_c`, `c in ker(B_N^T)`, with the retained source norm | V004 augmentation; raw individual edge currents; selected cycle basis | canonical dual of `coker(B_N)`; no endpoint term and no basis choice | a vertical direction pairs nontrivially, a nonzero cycle class is unseparated, or the norm is output-dependent |
| A5 | invariant finite cylinders `C(Q_N)` and local cycle phases `Phi_c` | arbitrary `f(H_N)`; global trivialization; selected spanning-tree gauge | least scalar algebra that descends through Gate 4 | a function varies on a Gate-4 orbit or `d Phi_c=u_c` fails |
| A6 | trace-class symmetric source and continuous bilinear raw class on `J_phys^005` | Hilbert-Schmidt; distributional dual; unrestricted algebraic bilinear | minimal separated abstract class; no physical image claimed | finite conserved core fails separation or hidden completion is invoked |

```text
CHOICE_TABLE_COMPLETE_FOR_Q297_REPAIR = true | MECHANICAL_AUDIT
GAUGE_BREAKING_AUTHORED = false | TYPE-S |
  roots: A3-A5 choices above |
  exclusions: no alternative promoted |
  fences: Gate4 equivalence preserved |
  query: any premise retaining vertex coboundaries as physical
```

---

## 8. Endpoint intertwiner and C_Emb consumer compatibility

The family-wide associated-line square survives upstairs:

```text
PT_A(gamma_e) I_(s,p)
  = I_(t,p) multiplication_by(h_e(A,p)).
```

Under vertex change both intertwiners and `h_e` transform equivariantly.
Physical scalar consumers use either:

1. closed-cycle products, for which endpoint factors cancel; or
2. an endpoint-covariant transport contracted with matching endpoint data.

No bare open-edge scalar is consumed as a gauge-invariant output.

Restrict the V003 family-wide pullback to invariant cylinders:

```text
C_Emb_phys^005:T_cyl^G -> C_b(X_phys^005),
C_Emb_phys^005(f)([x])=f(K([x])).
```

At every finite stage, pullback along the quotient-coordinate surjection is
injective and isometric in sup norm. The finite squares commute under
restriction, and Door F plus norm universality gives the completed map.

```text
ENDPOINT_INTERTWINER_FAMILY = SURVIVED_EQUIVARIANTLY
C_EMB_FULL_NONINVARIANT_TCYL_DESCENDS = false | TYPE-R |
  test: Q-297 one-edge non-invariant cylinder
C_EMB_INVARIANT_SUBALGEBRA_DESCENDS = PASS_AS_PROPOSAL
FRAME_OR_CYCLE_MEMBER_SELECTED = false | TYPE-S |
  roots: full torsor family and invariant algebra |
  exclusions: proof representatives |
  fences: family discipline |
  query: selected frame, spanning tree, or cycle basis
```

---

## 9. Seven-seam rerun

### S1 — orientation to causal path

A2-R2 and `E_post` still send every oriented write edge to a future-directed
physical path.

```text
S1_ORIENTATION_TO_CAUSAL_PATH = PASS_AS_PROPOSAL
```

### S2 — incidence/locality to support

A2-R4/R5 still preserve boundary and adjacency.

```text
S2_INCIDENCE_TO_SUPPORT = PASS_AS_PROPOSAL
```

### S3 — Gate-4 transport to the physical quotient

V003's equivariant map descends uniquely:

```text
[T_iota,p]: U(1)^(E_N)/Gamma_N -> Q_N,
[U] -> [h(A,p)].
```

This is the identification Q-297 made load-bearing.

```text
S3_GATE4_QUOTIENT_SEAM = PASS_AS_PROPOSAL
S3_SELECTED_FRAME_REQUIRED = false | TYPE-R |
  test: the map is defined on orbit classes
```

### S4 — CTP reality

Branch exchange and conjugation preserve the invariant cylinder algebra and
send a cycle to its orientation-reversed cycle.

```text
S4_CTP_REALITY_REPRESENTATION = PASS_AS_PROPOSAL
```

### S5 — finite labels to conserved physical currents

The Gate-4 physical label space is `coker(B_N)` and its scalar source dual is
`ker(B_N^T)`. The map `c->u_c` is well typed and separating by Section 5.

```text
S5_CONSERVED_SOURCE_KERNEL_AND_SEPARATION = PASS_AS_PROPOSAL
S5_ALL_OPEN_EDGE_LABELS_SURVIVE_AS_PHYSICAL_SCALARS = false | TYPE-R |
  test: only coefficients annihilating im(B_N) descend
```

### S6 — zero-extension

An old finite cycle remains divergence-free under zero-extension:

```text
B_M^T j_NM(c)=j_V(B_N^T c)=0.
```

Thus `c->u_c` commutes with the directed inclusion on the conserved finite
core and its declared completion.

```text
S6_ZERO_EXTENSION_TO_QUOTIENT_SOURCE_RIGGING = PASS_AS_PROPOSAL
```

### S7 — T_cyl to physical invariant cylinders

The finite invariant subalgebras are natural under restriction. Pullback along
`K_N` and Door F yields `C_Emb_phys^005`.

```text
S7_INVARIANT_TCYL_TO_PHYSICAL_CYLINDERS = PASS_AS_PROPOSAL
S7_NONINVARIANT_PRESENTATION_CYLINDERS_CONSUMED_PHYSICALLY = false | TYPE-R |
  test: their values vary on a Gate-4 orbit
S7_CREATED_TAIL_IMAGE = zero | PROPOSAL-CONDITIONAL THEOREM
```

```text
SEVEN_SEAMS_V005 = CONDITIONAL_PASS_ON_PHYSICAL_QUOTIENT
SEAMS_PROVE_A1_A6_EXIST = false | TYPE-R |
  test: every seam retains proposed A1-A6 existence antecedents
```

---

## 10. Class-formation doors

### 10.1 Door D0 — inherited invariant norm completion

Restricting a separated norm algebra to its closed invariant subalgebra does
not create a common finite-restriction tail. The V003/V004 epsilon proof
applies unchanged to `T_cyl^G`.

```text
CLASS_FORMATION_DOOR_D0 := (
  input_class=directed finite invariant cylinder union,
  input_topology=D4 cylinder norm,
  input_restrictions=contractive finite invariant retractions,
  formation_or_completion_operation=norm closure inside separated T_cyl,
  output_class=T_cyl^G,
  output_topology=C-star/module norm,
  output_restrictions=continuous finite invariant retractions,
  topology_changed=true,
  every_limit_named=true,
  limit_topology=norm,
  weak_star_invoked=false,
  bidual_invoked=false,
  distributional_completion_invoked=false,
  nonseparating_extension_invoked=false,
  Tail_output=intersection_N ker(r_N|T_cyl^G)={0},
  created_tail_image=zero by the inherited contractive epsilon proof,
  class_separation_proved=true,
  quotient_exactness_proved=NOT_APPLICABLE,
  closure_uniqueness_proved=true by norm closure,
  restriction_square=PASS,
  Q279_full_tuple_reproduced=false | TYPE-U |
    would-build: physical raw-G image and full restriction tuple,
  common_origin_provenance=TYPE-P | premises: DoR-008 for D4 only,
  target_independence=PASS,
  kernel=zero common finite-restriction kernel,
  image=closed invariant cylinder algebra,
  sector_transfers=noninvariant grades excluded; no transfer,
  Tail_R_action=NOT_REACHED,
  door_verdict=CLOSED_SEPARATED_ZERO_CREATED_TAIL
).
```

### 10.2 Door F — finite framed presentations to compatible family

Door F is retained from V004. Its output is upstream of the physical quotient,
but its finite-projection zero-tail proof remains valid and its induced
physical restrictions are used by Door Q below.

```text
CLASS_FORMATION_DOOR_F := (
  input_class=directed finite framed presentations X_N^fr,
  input_topology=finite quotient topology on each X_N^fr,
  input_restrictions=continuous r_MN retaining old paths and forgetting later frames,
  formation_or_completion_operation=exact inverse/projective limit equalizer,
  output_class=X_inf^fr={(x_N):r_MN(x_M)=x_N},
  output_topology=projective subspace-product topology,
  output_restrictions=finite projections pi_N,
  topology_changed=true,
  every_limit_named=true,
  limit_topology=projective/subspace-product topology,
  weak_star_invoked=false,
  bidual_invoked=false,
  distributional_completion_invoked=false,
  nonseparating_extension_invoked=false,
  Tail_output=intersection_N ker(pi_N)={0},
  created_tail_image=zero by componentwise equality,
  class_separation_proved=true,
  quotient_exactness_proved=NOT_APPLICABLE,
  closure_uniqueness_proved=true by the inverse-limit universal property,
  restriction_square=PASS_AS_PROPOSAL | equation:pi_N=r_MN compose pi_M,
  Q279_full_tuple_reproduced=false | TYPE-U |
    would-build: physical raw-G image and complete restriction tuple,
  common_origin_provenance=false | TYPE-U |
    would-build: ratified A1/A2/A3 physical descent witness,
  target_independence=PASS,
  kernel=zero common finite-projection kernel,
  image=compatibility equalizer,
  sector_transfers=connection and frame sectors assembled componentwise; none mixed,
  Tail_R_action=NOT_REACHED | NO_VERDICT,
  proposal_conditional_verdict=CLOSED_SEPARATED_ZERO_CREATED_TAIL,
  door_verdict=UNDECIDED_TYPE_U pending DoR-015 and provenance
).
```

### 10.3 Door Q — the one triangulated physical quotient

```text
CLASS_FORMATION_DOOR_Q := (
  input_class=X_inf^fr from Door F,
  input_topology=Door-F projective topology,
  input_restrictions=K_N=q_N compose H_N compose pi_N,
  formation_or_completion_operation=one exact quotient by equality of all finite K_N,
  output_class=X_phys^005 identified with image(K),
  output_topology=subspace projective topology from product_N Q_N,
  output_restrictions=finite quotient coordinates K_N,
  topology_changed=true,
  every_limit_named=true,
  limit_topology=NOT_APPLICABLE -- no closure adjoined by the quotient,
  weak_star_invoked=false,
  bidual_invoked=false,
  distributional_completion_invoked=false,
  nonseparating_extension_invoked=false,
  Tail_output={0} relative to every finite K_N by construction,
  created_tail_image=zero -- the quotient deletes its common kernel,
  class_separation_proved=true by injection into image(K),
  quotient_exactness_proved=true by definition,
  closure_uniqueness_proved=NOT_APPLICABLE,
  restriction_square=PASS_AS_PROPOSAL by S3 and finite equivariance,
  Q279_full_tuple_reproduced=false | TYPE-U |
    would-build: physical raw-G image and complete Q279 execution,
  common_origin_provenance=false | TYPE-U |
    would-build: ratified A1/A2/A3 physical descent witness,
  target_independence=PASS,
  kernel=Gate4 vertex orbits plus the all-finite K_N common kernel,
  image=image(K) subset product_N Q_N,
  sector_transfers=frame coboundaries killed; connection cycle class retained,
  Tail_R_action=NOT_REACHED | NO_VERDICT,
  proposal_conditional_verdict=CLOSED_SEPARATED_ZERO_CREATED_TAIL,
  door_verdict=UNDECIDED_TYPE_U pending DoR-015 and provenance
).
```

Door F plus Door Q has zero common **physical** finite-restriction tail: Door F
creates none upstairs, and Door Q identifies its entire quotient kernel. No
element of `X_phys^005` can be invisible to every `K_N` except zero/equality.

### 10.4 Door A — invariant cylinder pullback

```text
CLASS_FORMATION_DOOR_A := (
  input_class=T_cyl^G separated invariant norm algebra,
  input_topology=C-star/module norm,
  input_restrictions=finite invariant retractions,
  formation_or_completion_operation=C_Emb_phys^005 pullback through K after Door F/Q,
  output_class=bounded invariant cylinders on X_phys^005,+ x X_phys^005,-,
  output_topology=sup norm,
  output_restrictions=finite K_N pullbacks,
  topology_changed=false,
  every_limit_named=true,
  limit_topology=norm/projective compatibility,
  weak_star_invoked=false,
  bidual_invoked=false,
  distributional_completion_invoked=false,
  nonseparating_extension_invoked=false,
  Tail_output={0} conditional on finite quotient-coordinate reach,
  created_tail_image=zero by injective isometry,
  class_separation_proved=true on image(K),
  quotient_exactness_proved=true through Door Q,
  closure_uniqueness_proved=true by D0 and Door-F universal properties,
  restriction_square=PASS_AS_PROPOSAL,
  Q279_full_tuple_reproduced=false | TYPE-U |
    would-build: raw-G physical image and full tuple run,
  common_origin_provenance=false | TYPE-U |
    would-build: ratified source-record-field descent witness,
  target_independence=PASS,
  kernel=zero on the finite quotient-coordinate algebra,
  image=compatible bounded invariant physical cylinders,
  sector_transfers=none,
  Tail_R_action=NOT_REACHED | NO_VERDICT,
  proposal_conditional_verdict=CLOSED_SEPARATED_ZERO_CREATED_TAIL,
  door_verdict=UNDECIDED_TYPE_U pending DoR-015 and provenance
).
```

### 10.5 Doors B and C — quotient source completions

```text
CLASS_FORMATION_DOOR_B := (
  input_class=J_fin^005 generated by all finite ker(B_N^T) currents,
  input_topology=retained A4 finite source norm,
  input_restrictions=finite conserved-current coefficient maps,
  formation_or_completion_operation=Hilbert norm completion,
  output_class=H_1^005 and doubled H_CTP^005,
  output_topology=Hilbert norm,
  output_restrictions=continuous finite conserved-current maps,
  topology_changed=true,
  every_limit_named=true,
  limit_topology=Hilbert norm,
  weak_star_invoked=false,
  bidual_invoked=false,
  distributional_completion_invoked=false,
  nonseparating_extension_invoked=false,
  Tail_output={0} by dense finite conserved-current span,
  created_tail_image=zero by norm density,
  class_separation_proved=true,
  quotient_exactness_proved=NOT_APPLICABLE,
  closure_uniqueness_proved=true by Hilbert completion,
  restriction_square=PASS_AS_PROPOSAL through S6,
  Q279_full_tuple_reproduced=false | TYPE-U |
    would-build: physical raw-G image and full tuple run,
  common_origin_provenance=false | TYPE-U |
    would-build: ratified A4 descent and common-origin witness,
  target_independence=PASS,
  kernel=zero common finite conserved-coordinate kernel,
  image=completed conserved physical-source span,
  sector_transfers=open-edge nonconserved sector absent; no transfer,
  Tail_R_action=NOT_REACHED | NO_VERDICT,
  proposal_conditional_verdict=CLOSED_SEPARATED_ZERO_CREATED_TAIL,
  door_verdict=UNDECIDED_TYPE_U pending DoR-015 and provenance
).

CLASS_FORMATION_DOOR_C := (
  input_class=finite-rank symmetric operators on H_CTP^005,
  input_topology=trace norm,
  input_restrictions=finite conserved-source matrix corners,
  formation_or_completion_operation=trace-norm completion,
  output_class=S_1,sym(H_CTP^005),
  output_topology=trace norm,
  output_restrictions=continuous finite corners,
  topology_changed=true,
  every_limit_named=true,
  limit_topology=trace norm,
  weak_star_invoked=false,
  bidual_invoked=false,
  distributional_completion_invoked=false,
  nonseparating_extension_invoked=false,
  Tail_output={0} by finite-rank density,
  created_tail_image=zero,
  class_separation_proved=true,
  quotient_exactness_proved=NOT_APPLICABLE,
  closure_uniqueness_proved=true by trace-norm completion,
  restriction_square=PASS_AS_PROPOSAL,
  Q279_full_tuple_reproduced=false | TYPE-U |
    would-build: physical raw-G image and full tuple run,
  common_origin_provenance=false | TYPE-U |
    would-build: ratified A4/A6 common-origin descent,
  target_independence=PASS,
  kernel=zero common finite-corner kernel,
  image=trace-class symmetric conserved-source carrier,
  sector_transfers=none beyond CTP doubling,
  Tail_R_action=NOT_REACHED | NO_VERDICT,
  proposal_conditional_verdict=CLOSED_SEPARATED_ZERO_CREATED_TAIL,
  door_verdict=UNDECIDED_TYPE_U pending DoR-015 and provenance
).
```

### 10.6 Door D — abstract bilocal class only

```text
CLASS_FORMATION_DOOR_D := (
  input_class=finite continuous bilinear forms on J_fin^005 x J_fin^005,
  input_topology=bounded-bilinear norm induced by A4,
  input_restrictions=finite conserved-source corners,
  formation_or_completion_operation=abstract continuous-bilinear class declaration,
  output_class=RawGClass^005,
  output_topology=bounded-bilinear norm,
  output_restrictions=finite bilinear corners,
  topology_changed=false,
  every_limit_named=true,
  limit_topology=NOT_APPLICABLE for absent physical image,
  weak_star_invoked=false,
  bidual_invoked=false,
  distributional_completion_invoked=false,
  nonseparating_extension_invoked=false,
  Tail_output={0} for the abstract finite-core-separated class,
  created_tail_image=zero for class declaration; physical image NO_VERDICT,
  class_separation_proved=true abstractly,
  quotient_exactness_proved=NOT_APPLICABLE,
  closure_uniqueness_proved=NOT_APPLICABLE,
  restriction_square=false | TYPE-U |
    would-build: scalar functional, derivatives, connected subtraction, and raw-G lift,
  Q279_full_tuple_reproduced=false | TYPE-U |
    would-build: the same physical image and restriction execution,
  common_origin_provenance=false | TYPE-U |
    would-build: physical raw-G descent witness,
  target_independence=PASS,
  kernel=NO_VERDICT for absent physical image map,
  image=NO_VERDICT for absent physical image map,
  sector_transfers=NO_VERDICT,
  Tail_R_action=NO_VERDICT,
  door_verdict=UNDECIDED_TYPE_U
).
```

---

## 11. Q-294 bounded reruns and DoR-008 restriction

| Required rerun | V005 result | Test |
|---|---|---|
| A4 separation | `PASS_AS_PROPOSAL` | `ker(B_N^T)` separates `coker(B_N)` at every finite stage |
| A5 differential | `PASS_AS_PROPOSAL` | `d Phi_c=u_c`; no endpoint term |
| A6 physical source | `PASS_AS_PROPOSAL` abstractly | completed conserved source domain; physical raw-G image remains TYPE-U |
| S5 | `PASS_AS_PROPOSAL` | finite Gate-4 quotient labels pair with conserved currents |
| S6 | `PASS_AS_PROPOSAL` | zero-extension preserves `ker(B_N^T)` |
| Doors B/C | `PASS_AS_PROPOSAL` | norm/trace completions start from descended quotient sources |
| Door A through F/Q | `PASS_AS_PROPOSAL` | invariant cylinders only; finite squares commute |
| choice table | `PASS` | Gate-4 quotient and cycle-source price explicit; no gauge-breaking alternative retained |
| unflagged scan | `PASS` | D0/F/Q/A/B/C/D account for every formation |

DoR-008 restriction result:

* the finite quotient reproduces the sealed Gate-4 result—tree phases are
  removed and loop holonomy survives;
* the endpoint-intertwiner square remains equivariant;
* the invariant finite cylinder restrictions commute;
* the complete physical Q-279/raw-G tuple remains unbuilt and is not claimed.

```text
DOR008_GATE4_FINITE_RESTRICTION_REPRODUCED = PASS_AS_PROPOSAL
DOR008_FULL_Q279_PHYSICAL_RESTRICTION_REPRODUCED = false | TYPE-U |
  would-build: physical raw-G image and complete restriction execution
```

---

## 12. Kill-passes and regression

### 12.1 Exact quotient kill-pass

* **No less:** the Q-294/Q-297 vertical tangent is in `im(B_N)` and is killed.
* **No more:** a nonzero finite cycle class changes `K_N` and survives.
* **Path invisible only:** equality requires agreement of every finite `K_N`.

### 12.2 No re-augmentation

The string `u_e^aug` appears only in authority/history statements and this
negative audit. It appears in no definition, map, door input, or consumer.

```text
RE_AUGMENTATION_IN_ACTIVE_V005_DEFINITION_FOUND = false | TYPE-S |
  roots: Sections 3-11 active definitions and tables |
  exclusions: Q-297 history and negative audit statements |
  fences: no endpoint source addition |
  query: u_e^aug; theta_t-theta_s in any physical current
```

### 12.3 Six-count and selection

```text
V005_INDEPENDENT_AUTHORED_STRUCTURE_COUNT = 6 | PROPOSAL-LEVEL COUNT
SELECTED_FRAME_GAUGE_CYCLE_OR_BACKGROUND_MEMBER_FOUND = false | TYPE-S |
  roots: A1-A6, S1-S7, and Doors D0/F/Q/A/B/C/D |
  exclusions: proof representatives only |
  fences: family discipline |
  query: distinguished frame, gauge, spanning tree, cycle basis, background
```

The quotient is a derived consequence of Gate 4 plus the already-authored A3
finite realization; it adds no seventh authored field.

### 12.4 Forbidden class formation and target awareness

```text
UNFLAGGED_CLASS_FORMATION_STEP_FOUND = false | TYPE-S |
  roots: every inverse limit, quotient, invariant closure, pullback, Hilbert
         completion, trace completion, and bilinear class in V005 |
  exclusions: operations stated only as TYPE-U |
  fences: Q-288 mandatory schema |
  query: all class-forming arrows against Doors D0/F/Q/A/B/C/D

FORBIDDEN_COMPLETION_INVOKED = false | TYPE-S |
  roots: Doors D0/F/Q/A/B/C/D |
  exclusions: unbuilt alternatives |
  fences: Q-288 flags |
  query: weak-star, bidual, distributional, nonseparating, unnamed topology

TARGET_AWARE_MEMBERSHIP_PREDICATE_FOUND = false | TYPE-S |
  roots: A1-A6, choice rationales, seams, and every door |
  exclusions: terminal fences and downstream status prose |
  fences: no response/value evaluation |
  query: p_ch, alpha, stiffness, measured target, residual value
```

### 12.5 Symbol collisions bearing here

`holonomy` here means Gate-4 graph-cycle holonomy only. It is not the sealed
quarter-turn record-changing holonomy, a Wilson plaquette, or the composition
loop phase. `H_N` is the raw framed coordinate; `K_N=q_N H_N` is the physical
quotient coordinate. Neither is a retarded Hessian.

---

## 13. Preserved open boundaries

```text
PHYSICAL_SCALAR_FUNCTIONAL_BUILT = false | TYPE-U |
  would-build: scalarization with state/measure provenance
MEASURE_OPERATION_BUILT = false | TYPE-U |
  would-build: invariant descended physical measure and convolution pairing
CONTOUR_OPERATION_BUILT = false | TYPE-U |
  would-build: interacting prescription and named boundary-value topology
BOUNDARY_CONTACT_OPERATION_BUILT = false | TYPE-U |
  would-build: physical contact terms, boundary form, and gluing theorem
DOMAIN_CLOSURE_OPERATION_BUILT = false | TYPE-U |
  would-build: common unbounded domains and endpoint compatibility
FULL_SMOOTH_PRPS_WARD_EXHAUSTION_BUILT = false | TYPE-U |
  would-build: smooth endpoint-frame/Gate4 exhaustion beyond the finite S3 map
RAW_G_PHYSICAL_IMAGE_BUILT = false | TYPE-U |
  would-build: physical functional, derivatives, connected subtraction,
               lift, restriction square, and Door-D image theorem
STATIONARY_BACKGROUND_BUILT = false | TYPE-U |
  would-build: stationary lift fiber, 2PI blocks, and stationary selector
```

None is converted into physical failure. The finite Gate-4 quotient does not
claim the unbuilt full smooth exhaustion theorem.

---

## 14. Final V005 verdict and custody pre-seal block

```text
PHYSICAL_CARRIER = X_inf^fr / (Gate4 vertex rephasing + all-finite path-invisible)
PHYSICAL_FINITE_COORDINATE = K_N=q_N compose H_N
PHYSICAL_SOURCE = complete basis-free family {u_c:c in ker(B_N^T)}
PHYSICAL_PHASE_IDENTITY = d Phi_c=u_c
ENDPOINT_FRAME_DIRECTIONS = BOUNDARY_GAUGE

Q294_KILL_TANGENT_IN_KERNEL = true | PROPOSAL-CONDITIONAL THEOREM
Q297_KILL_TANGENT_IN_KERNEL = true | PROPOSAL-CONDITIONAL THEOREM
NONZERO_CYCLE_CLASS_SURVIVES = true | PROPOSAL-CONDITIONAL THEOREM

SEVEN_SEAMS_RERUN = CONDITIONAL_PASS
DOOR_D0 = CLOSED_SEPARATED_ZERO_CREATED_TAIL
DOOR_F = SURVIVED_ZERO_COMMON_FINITE_PROJECTION_TAIL
DOOR_Q = PROPOSAL_CONDITIONAL_CLOSED_SEPARATED_ZERO_CREATED_TAIL
DOOR_A = CONDITIONAL_PASS_ON_INVARIANT_CYLINDERS
DOORS_B_C = CONDITIONAL_PASS_ON_CONSERVED_QUOTIENT_SOURCES
DOOR_D_PHYSICAL_IMAGE = NO_VERDICT
DOR008_GATE4_FINITE_RESTRICTION = PASS_AS_PROPOSAL
DOR008_FULL_Q279_RESTRICTION = false | TYPE-U

OVERALL_PROPOSAL_STATUS = V005_COMPLETE_FOR_THIRD_FINAL_ADVERSARIAL_REVIEW
DOR_015_PACKAGE_ISSUED = false | TYPE-C |
  constraint: third final adversarial review and principal ratification have not occurred |
  release: V005 survives final review and the principal issues DoR-015
```

Send-time register currency is checked immediately before sealing.

```text
REGISTER_HEAD_AT_START = Q-297
REGISTER_HEAD_AT_SEND_TIME = Q-297
REGISTER_SHA256_AT_FINAL_CHECK =
  65d8808b0f031f6fb9656174b497efb48234258426380dc9e2d3d1857e37f0da
LATER_BEARING_RULING_CONSUMED = false | TYPE-S |
  roots: alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md through Q-297 |
  exclusions: no unregistered V005 or DoR-015 draft |
  fences: no cross-lane coordination |
  query: Q-298; FIELD_SIGNATURE_PHYS V005; DoR-015

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

Custody: seal V005, verify the sidecar, mirror artifact and sidecar to
`alpha-program-archive/workspace/`, report hashes and exact paths, and stop.
No register, plan, tracker, git, commit, push, gate, or deploy action is
performed by this lane.
