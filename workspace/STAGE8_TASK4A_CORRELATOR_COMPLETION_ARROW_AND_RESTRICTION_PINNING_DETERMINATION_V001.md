# Stage 8 Task 4a Correlator Completion Arrow and Restriction Pinning Determination v001

Date: 2026-08-01
Lane: CODEX LANE 1
Task: 4a
Authority: DoR-011, construction and symbolic trace only
Register head consulted at completion: Q-244

## 0. Lead determination

**NAMED FREEDOM REMAINS. The DoR-008 falsifier pins the direct finite
cylindrical retarded block to the Q-243 zero wherever a genuine restriction
map exists. It does not pin the complete physical retarded block `p_ch`-free.**

The maximal arrow that the ratified data actually construct is

```text
{Abar_N^(p)}_N
  -> one scalar function A_fin^(p) on the direct union of eventually-identity
     finite quotient histories
  -> exact finite first and second derivatives
  -> exact zero finite mixed retarded block.
```

The next arrow does not construct:

```text
A_fin^(p)
  -/-> one completed physical Z_inc[J,R]
  -/-> one raw bilocal correlator G
  -/-> one complete H_R[G].
```

There are three independent reasons.

1. DoR-008 ratifies a **state-free kinematic C-star completion** and bounded
   finite-support operator source maps. It deliberately supplies no scalar
   state, dynamics, effect contraction, measure, or scalar functional.
2. The finite scalar family depends on relative linear holonomy histories. It
   has no independent symmetric bilocal source `R`, so the derivative defining
   raw `G` cannot be taken from it.
3. No physical source topology or derivative calculus is frozen. In fact, the
   obvious continuous extension through the ratified compact spectrum fails:
   the all-stage product amplitude is discontinuous in that product topology
   for every admitted interior `p_ch`.

The exact first missing object is therefore the already specified physical
source germ package

```text
SOURCE_GERM_PHYS :=
  (Z_inc, D_src, 0_src, topology_src, Diff_src, Reg_D1, U1, U3),
```

extended to the independent symmetric bilocal source derivative needed for
raw `G`, and equipped with genuine finite-to-physical restriction maps.

The standing falsifier decides uniqueness only after a separation theorem:

```text
intersection_N kernel(rho_H,N) = {0}
```

on the declared physical retarded-operator class. No such density/core/
continuity theorem is sealed. A possible `p_ch` re-entry is therefore localized
to one completed generating object: `Z_inc[J,R]` and its descendants. Within
that object it can appear either as restriction-invisible physical content or
indirectly through the `p_ch`-dependent stationary background/on-shell cell.

```text
MAXIMAL_FINITE_CYLINDRICAL_ARROW_CONSTRUCTED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-011

FINITE_SCALAR_TO_COMPLETED_RAW_G_ARROW_CONSTRUCTED = false | TYPE-U |
  would-build: SOURCE_GERM_PHYS with independent bilocal source, physical
               topology/calculus, scalar state/dynamics/effect contraction,
               common-origin provenance, and restriction intertwiners

NAIVE_CSTAR_CONTINUOUS_AMPLITUDE_EXTENSION_EXISTS = false | TYPE-R |
  test: the moving-tail phase sequence in Section 4

DOR008_FALSIFIER_PINS_COMPLETE_RETHESS_P_CH_FREE = NO_VERDICT |
  prerequisite: physical restriction maps and the separation theorem are
                unbuilt

P_CH_REENTRY_CHANNEL = COMPLETED_Z_INC_SOURCE_GERM_OUTSIDE_DIRECT_FINITE_RETHESS_BLOCK
```

This does not refute existence of a physical completion. It refutes one
shortcut: treating the ratified kinematic C-star completion as if it already
were the scalar, differentiable, physical source completion.

## 1. Preflight, currency, premises, and scope

### 1.1 Preflight

```text
DOES_THE_OBJECT_EXIST = NAMED_NOT_BUILT
  Q-243 names the finite scalar/source functional to completed raw bilocal
  correlator arrow. The live raw-map spec already types it TYPE-U.

IS_THE_VERSION_CURRENT = true_through_Q_244
  The relay was issued at Q-243. Q-244 landed during this run and bears on the
  restriction test: a matching proxy is not a restriction of C0_008. It is
  incorporated here.

ARE_THE_INPUTS_PRESENT = SPLIT
  finite quotients, amplitudes, source maps, branch grammar: present;
  scalar physical source germ, bilocal derivative, topology, restriction
  intertwiners, and complete physical package: absent.
```

### 1.2 Premises declared at the outset

All positive constructions using the ratified carrier and law carry:

```text
TYPE-P | premises: DoR-008, DoR-009, DoR-011
```

Imported mathematical fact used conditionally:

```text
continuous maps into a Hausdorff codomain that agree on a dense subset agree
on its closure.
```

This is elementary topology/functional analysis. It applies only after the
program derives a topology, proves density/core status of the finite union,
and places the correlator or Hessian in the corresponding continuous class.
None of those physical applicability premises is imported here.

No state, measure, contour, completion topology, derivative calculus,
bilocal-source dependence, tail, or on-shell cell is chosen.

### 1.3 Current authorities

| Authority | SHA-256 | Load-bearing content |
|---|---|---|
| `DECISION_OF_RECORD_008_FIELD_CTP_ADOPTION_RATIFIED_WITH_FALSIFIER_2026-08-01_V001.md` | `d51a6d5c5bb0020a081cfd2adfb545b9f5ed86ce660d3feacadc5ef68140fb19` | ratified kinematic completion; every genuine finite restriction must agree |
| `DECISION_OF_RECORD_011_TASK4_TRANSPORT_CONSTRUCTION_AUTHORIZED_2026-08-01_V001.md` | `1a54d50a53da30efe5af39b17d81a908eec75daa6ff450563edffed1d616a660` | construction-only scope; five physical TYPE-U fields stay named |
| `STAGE8_TASK4A_FINITE_HESSIAN_TO_DELTAPHI_TRANSPORT_MAP_CONSTRUCTION_AND_P_CH_TRACE_V001.md` | `70185aa842bc500724719c65bd66b5f07005e2214b97be0d35e07fd029d5c68c` | Q-243 finite Keldysh result: zero mixed block, coherent one-point survives |
| `STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md` | `76916244bdbcac7c2a6d4afae40f35127540d1d9e4cfc86fb72318506671161f` | `Lambda`, `C*(Lambda)`, state-free module, finite-support `s_J/s_R` |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_C0_DOR008_ASSEMBLY_AND_FIRST_RESTRICTION_TEST_V001.md` | `1467ab9850022931e68dc9ffa625d95099d8f6bb74d734dc9d0466f169bd00b6` | executed C0_008 tuple and scalarization firewall |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_U3_DOR008_DOR009_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md` | `b0118d89e0b4b321fbf9caab5bfb811a0b5fd572e808d02615ee8503db2bc1ac` | finite quotients, exact sequential glue, five physical fields missing |
| `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md` | `57c06fcbedf4a486b87b42c02e6d13a92096ac6a56751d3ae5fd55f4b11deb57` | physical raw-G signature and finite restriction test T5 |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_ITEM2_PHYSICAL_LOG0_GERM_SPEC_V001.md` | `14573a676a385dd4c814f3fd12d8fb53caa601598e96b35525c6372329d506b3` | source topology/calculus and pointwise physical functional explicitly unbuilt |
| `primitive_record_cell_selection_principle_v004.md` | `13d227ceb2198d96b0e4e2fef57b874cea71cb755320508fbf4c6d64a00c507e` | live `Z_inc`, `W_inc`, raw `G`, physical-source signature |
| `STAGE8_SHARED_FINITE_STATE_EFFECT_CONDITIONED_AMPLITUDE_SHARP_STOP_V001.md` | `2cbec1f0adefaa7f962bde505117c95a0f8c08cd6a8ea508aec4eef006fd6c12` | exact finite conditional amplitude family |

Q-244 is also binding through the settled register and its sealed artifact
`STAGE8_TASK2F_X_K_INDEPENDENT_FIX_AND_K_SQUARE_FALSIFIER_ARM_ATTEMPT_V001.md`:
proxy agreement without a C0 restriction package is not a DoR-008 falsifier
pass.

## 2. The two source signatures

### 2.1 Ratified finite-support operator source maps

DoR-008 ratifies

```text
Lambda_N = Z^N,
Lambda = direct-sum_(j>=1) Z e_j,
A_F = C*(Lambda),
A_F_CTP = A_F,+ tensor_min (A_F,-)^op.
```

The source domains and maps are

```text
D_J^C0 := C_c({+,-} x (Lambda without {0}); C),
D_R^C0 := D_J^C0 tensor_alg D_J^C0,

s_J(j) := sum_(a,lambda) j(a,lambda) pi_C0(e_a(U_lambda)),

s_R(r) := (1/2) sum_(a,lambda,b,mu)
          r((a,lambda),(b,mu))
          pi_C0(e_a(U_lambda)e_b(U_mu)).
```

Every sum is finite and operator-valued
(`STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md:475-516`).
The source choice table says expressly that these maps leave continuum
topology open (`:595-609`).

The C0 scalarization firewall is load-bearing:

```text
no omega:B->C;
no cyclic vector;
no density operator;
no trace;
no integration map;
no measure.
```

It also excludes dynamics and every response result (`:419-439,701-723`).
Thus `s_R` is not a scalar generating functional and its symbol `D_R^C0` is
not a retarded kernel.

### 2.2 Completed physical raw correlator

The live physical signature is

```text
Z_inc[J,R]
  = Tr_full { I_final T_C exp[(i/hbar)
      {S_CTP + J_I A^I + (1/2)A^I R_IJ A^J}] rho_pre },

W_inc[J,R] = -i hbar Log_0 Z_inc[J,R],
Abar^I = delta W_inc/delta J_I,
G^(IJ) = 2 delta W_inc/delta R_IJ - Abar^I Abar^J.
```

Here `I=(a,mu,x)` includes branch, physical field, and spacetime point; `R` is
in the symmetric physical compound-index dual; contraction uses the physical
branch metric and invariant spacetime measure
(`primitive_record_cell_selection_principle_v004.md:17-69`).

The response consumer then has signature

```text
E_R:
  Dom_R(CTP_PHYS_INPUT_PACKAGE)
    -> RetHess(CTP_PHYS_INPUT_PACKAGE),

E_R(G)=H_R[G].
```

Its codomain consists of action-valued bilinear operators from common-history
physical connection perturbations to dual difference-history perturbations
(`STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:613-706`).

The maps in Section 2.1 provide the algebraic shapes of `J` and `R`. They do
not provide the scalar trace, physical source set, topology, differentiable
logarithm, expectation field, or raw correlator in this signature.

```text
C0_OPERATOR_BILOCAL_SOURCE_MAP_EQUALS_PHYSICAL_RAW_G = false | TYPE-R |
  test: compare domains, codomains, scalarization, and derivative roles
```

## 3. Maximal premise-level arrow

### 3.1 Exact finite quotient family

At finite `N`, Q-239 constructs

```text
Q_N = U(1)^N,
r_j = conjugate(z_(-,j)) z_(+,j),

Abar_N^(p)(r) = (1-p) + p product_(j=1)^N r_j.
```

For `N<=M`, the exact zero-extension is

```text
j_NM^Q(r_1,...,r_N)
  = (r_1,...,r_N,1,...,1),

Abar_M^(p) compose j_NM^Q = Abar_N^(p).
```

These are sealed at
`STAGE8_CTP_PHYS_INPUT_PACKAGE_U3_DOR008_DOR009_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md:190-330`.

Define the direct union

```text
Q_fin := colim_(N,j_NM^Q) Q_N
       = {r=(r_j) : r_j=1 for all but finitely many j}.
```

The compatibility equation gives one well-defined scalar function

```text
A_fin^(p):Q_fin->C,

A_fin^(p)(r)
  := (1-p) + p product_(j:r_j!=1) r_j.
```

The product is finite by the definition of `Q_fin`; no output or target is
used.

```text
FINITE_ZERO_EXTENSION_SCALAR_ARROW_CONSTRUCTED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-011

A_FIN_P_RESTRICTS_TO_EVERY_A_N_P = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-011
```

### 3.2 What this arrow determines

On every finite tangent, it determines exactly the Q-243 derivatives:

```text
D Gamma_CTP,N|_0
  = p_ch sum_j delta theta_j,

D^2 Gamma_CTP,N|_0
  = i p_ch(1-p_ch)
      (sum_j delta_1 theta_j)(sum_k delta_2 theta_k).
```

The Keldysh rotation places the second line entirely in the DD/noise block and
its finite `(delta,c)` block is zero.

Thus the DoR-008 falsifier already requires any **genuine** complete
restriction to reproduce:

```text
rho_H,N(H_R^complete) = 0
```

for the Q-243 finite mixed direction, after the physical state, carrier,
source convention, and restriction map have independently been identified.

### 3.3 Where the arrow stops

`A_fin^(p)` is a scalar function of relative linear holonomy histories. It has
no independent argument in `D_R^C0`, much less in the symmetric physical
bilocal source space. Therefore the formula

```text
G = 2 delta W_inc/delta R - Abar Abar
```

cannot be applied to `A_fin^(p)`.

Defining the missing `R` dependence to be zero would be an unlicensed choice
that makes a later derivative pass. It is not performed.

The live raw-map specification already records this exact stop:

```text
finite_scalar_CTP_to_complete_bilocal_raw_G_extension_derived = false |
  TYPE-U |
  would-build: a source-inclusive continuum/projective-limit CTP functional
               with symmetric bilocal source, regulator/gauge/edge
               completion, nonzero differentiable log domain, and a proof
               that its derivatives restrict to the finite scalar closure.
```

(`STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:420-466`).

```text
INDEPENDENT_BILOCAL_SOURCE_DEPENDENCE_CONSTRUCTED = false | TYPE-U |
  would-build: the physical item-1 Z_inc[J,R] functional from one common-origin
               state/dynamics/effect package

RAW_G_DERIVED_FROM_A_FIN_P = false | TYPE-U |
  would-build: SOURCE_GERM_PHYS plus its admitted first symmetric-R derivative
```

## 4. Hostile continuous-extension test

### 4.1 The ratified compact spectrum

The ratified field algebra is

```text
A_F = C*(Lambda),
Lambda = direct-sum_(j>=1) Z e_j.
```

The adoption states equivalently that `A_F` is the continuous
cylinder-function algebra on

```text
Q_infty := Hom(Lambda,U(1)) = product_(j>=1) U(1)
```

with its compact product topology
(`STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md:312-329`).
`Q_fin` is dense in this topology: every basic neighborhood constrains only
finitely many coordinates, and an eventually-identity point can match those
coordinates.

### 4.2 Countersequence

Fix any `u in U(1)` with `u!=1`. For every positive integer `m`, let

```text
r^(m)_j = u  if j=m,
          1  otherwise.
```

Every `r^(m)` is in `Q_fin`. In the product topology,

```text
r^(m) -> 1_Q_infty,
```

because each fixed coordinate is eventually equal to `1`. But for every
admitted interior `p_ch`,

```text
A_fin^(p)(r^(m)) = (1-p_ch)+p_ch u,
A_fin^(p)(1_Q_infty) = 1,
```

and the two values differ because `p_ch!=0` and `u!=1`.

Therefore `A_fin^(p)` has no continuous extension to `Q_infty` in the
ratified product topology.

```text
Q_FIN_DENSE_IN_RATIFIED_COMPACT_SPECTRUM = true | TYPE-P |
  premises: DoR-008 and elementary product topology

A_FIN_P_CONTINUOUS_IN_RATIFIED_PRODUCT_TOPOLOGY = false | TYPE-R |
  test: moving-tail countersequence above

A_FIN_P_IS_AN_ELEMENT_OF_C_OF_Q_INFINITY = false | TYPE-R |
  test: failure of continuous extension from the dense subset Q_fin
```

### 4.3 Tangent version

The same obstruction appears at the derivative level. The finite coherent
covector is

```text
w_N(v)=sum_(j=1)^N v_j.
```

On finite-support tangents, the coordinate vector `e_m` tends coordinatewise
to zero as `m` moves into the tail, while

```text
w(e_m)=1.
```

Thus the summed-phase covector, and hence its rank-one DD Hessian, is not
continuous in the product topology. A different source topology can change
that verdict, but selecting it is exactly the unperformed L1 construction.

This TYPE-R result is scoped narrowly:

```text
REFUTED = direct continuous extension through the ratified compact-spectrum
          product topology;
NOT_REFUTED = every possible distributional, restricted-domain, or differently
              topologized physical source completion.
```

It does not void DoR-008. DoR-008 ratifies kinematic bookkeeping and excludes
dynamics/scalarization. The test proves that the missing physical source
completion is additional structure, not that the kinematic algebra is
inconsistent.

## 5. What the standing falsifier forces

### 5.1 The one-way condition

DoR-008 states that the completed framework must reproduce every sealed finite
result on genuine restriction. Q-243 is therefore a binding finite target.

But the raw-map T5 test requires, before it can execute:

```text
one complete physical package;
finite-to-complete carrier/source restriction intertwiners;
finite Z/W -> finite raw G from the same source convention;
one independently fixed E_R^fin;
identical states, histories, orderings, contacts, and boundary data.
```

It currently returns `NO_VERDICT`
(`STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:960-996`).

Q-244 sharpens the same rule: an object built from finite incidence data that
matches the finite polynomial is still not a restriction of `C0_008`.
Agreement by proxy is not an executable falsifier arm.

```text
DOR008_Q243_RESTRICTION_ARM_EXECUTED = false | TYPE-C |
  constraint: no physical source/correlator restriction package and no
              independently fixed finite raw-G extraction square |
  release: construct the T5 applicability package and run the square

DOR008_VOIDED_BY_THIS_RESULT = false | TYPE-S |
  scope: this artifact constructs no domain-valid complete candidate on which
         a restriction disagreement could be tested
```

### 5.2 Separation criterion

Suppose a future physical package supplies continuous restriction maps

```text
rho_H,N: RetHess_phys -> RetHess_N.
```

Define the restriction-null class

```text
Tail_R := intersection_N kernel(rho_H,N).
```

All finite restrictions determine the complete retarded operator exactly if
and only if the declared admissible operator class satisfies

```text
Tail_R = {0}.
```

A sufficient route is:

```text
1. the union of finite source images is dense or a core in the physical source
   topology/domain;
2. the admissible retarded bilinear operators are continuous/closable in the
   topology used by the comparison;
3. the restriction maps preserve the state, measure, contour, contacts,
   boundary data, and domains;
4. inversion and retarded extraction commute with restriction on that class.
```

None is supplied by DoR-008. The physical Log0-germ specification says
explicitly that `topology_src` and `Diff_src` must be independently derived
and are TYPE-U
(`STAGE8_CTP_PHYS_INPUT_PACKAGE_ITEM2_PHYSICAL_LOG0_GERM_SPEC_V001.md:128-168,240-316`).

```text
RESTRICTION_SEPARATION_THEOREM_DERIVED = false | TYPE-U |
  would-build: a physical source topology/calculus, a dense-core theorem,
               continuous/closable correlator and Hessian classes, and the
               complete T5 commuting square

TAIL_R_PROVED_ZERO = NO_VERDICT |
  prerequisite: RetHess_phys and rho_H,N are uninstantiated

TAIL_R_PROVED_NONZERO = NO_VERDICT |
  prerequisite: RetHess_phys and rho_H,N are uninstantiated
```

The falsifier consequently forces the **cylindrical restrictions** to be
`p_ch`-free in the direct Q-243 mixed block. It does not force the completed
operator `p_ch`-free.

## 6. Structural p_ch re-entry channels

### 6.1 Restriction-invisible physical content

If a future physical package has `Tail_R!=0`, two complete candidates can
agree on every finite restriction and differ by

```text
H_tail^(p) in Tail_R.
```

A `p_ch`-dependent member would pass the finite zero test by definition while
changing the complete response. No such member is asserted to exist. The
point is that current data do not prove the class zero.

The five Q-239 fields decide whether this channel is available:

1. **Descended measure** fixes the physical pairing, delta distribution, and
   convolution topology used by the correlator and inverse.
2. **Interacting contour/i-epsilon prescription** fixes which completed block
   is retarded and which inverse is admitted.
3. **Complete boundary/edge/contact data** determine whether boundary-supported
   or contact-supported terms are visible under finite restriction.
4. **Complete unbounded endpoint domains** determine whether finite sources
   form a core and whether the complete operator is uniquely closable from
   them.
5. **Common-origin provenance** determines whether any `p_ch`-dependent
   completed term belongs to the same physical generating functional or is an
   illicit supplement.

The physical source topology/calculus is an additional explicitly named
unbuilt field upstream of the five. It is not silently folded into C0.

### 6.2 Coherent one-point background channel

Q-243 derives

```text
D Gamma_CTP,N|_0 = p_ch w_N
```

in the difference one-point block. It does not enter the direct mixed Hessian.
But a complete stationarity problem can evaluate its Hessian at a background
that depends on the one-point equation. Structurally, a future map may have

```text
(rho_pre,p_ch)
  -> stationary (Abar_*(p_ch),G_*(p_ch))
  -> H_R[G_*(p_ch)]
  -> X_K^phase(p_ch)
  -> DeltaPhi[K;X_K^phase(p_ch)].
```

This is an indirect background dependence, not reinjection of the finite DD
noise term into the mixed block.

Whether it is nonzero is decided by:

```text
the common-origin State/Dynamics/Effect source germ;
the stationary 2PI-to-1PI reduction;
the completed physical response;
the phase on-shell cell X_K^phase;
the response/state-to-DeltaPhi functional.
```

None is supplied here.

```text
P_CH_REENTERS_COMPLETE_RETHESS_THROUGH_TAIL = NO_VERDICT
P_CH_REENTERS_COMPLETE_RETHESS_THROUGH_BACKGROUND = NO_VERDICT
P_CH_REENTERS_DELTAPHI = NO_VERDICT
```

The strongest lawful sentence is:

> **`p_ch` cannot re-enter through the direct finite DD-to-retarded block; it
> can re-enter only through completed source-germ content not determined by
> that block, namely a restriction-null physical contribution or a
> `p_ch`-dependent stationary/on-shell background.**

## 7. Symbol collisions that bear on this result

### 7.1 `D_R`

```text
D_R^C0 = D_J tensor_alg D_J
```

is the finite algebraic bilocal source domain in Field 10. It is not the
retarded response kernel often written `D_R` or `D_R^(-1)`. No use of the
source-domain symbol supplies a retarded operator.

### 7.2 `X_K`

Q-244's `X_K` is a proposed finite **source incidence operator** used in the
K-square falsifier. The phase residual's `X_K` is a coupling-indexed
**on-shell physical cell/configuration**. Write them here as

```text
X_K^inc   versus   X_K^phase.
```

Q-244 bears on the restriction methodology. It does not instantiate
`X_K^phase` or provide the response-to-phase map.

### 7.3 `C0`

Package `C0_008` is not the chain group `C_0(K)`. Q-244 confirms that an
incidence-copy proxy is not a C0 restriction merely because its finite
polynomial agrees.

## 8. Mandatory kill-passes

### 8.1 No smuggled measure, contour, or topology

No measure or contour is installed. No `l1`, Hilbert, Sobolev, product,
distribution, or other physical source completion is selected. The product
topology appears only because it is the ratified compact-spectrum topology,
and the result against it is a counterexample, not an adoption.

```text
PHYSICAL_MEASURE_SUPPLIED_HERE = false | TYPE-S |
  scope: construction equations in Sections 3-6; measure remains a named
         TYPE-U premise

PHYSICAL_CONTOUR_SUPPLIED_HERE = false | TYPE-S |
  scope: construction equations in Sections 3-6; contour remains a named
         TYPE-U premise

PHYSICAL_SOURCE_TOPOLOGY_SELECTED_HERE = false | TYPE-S |
  scope: no candidate physical topology is adopted; only the ratified C-star
         spectrum topology is tested and refuted for the amplitude extension
```

### 8.2 No uniqueness smuggled into the word completion

The C-star algebra completion is unique in its ratified bounded algebraic
category. The scalar source germ, correlator, inverse, and retarded operator
are different objects with different continuity/domain data. No uniqueness
statement is transported between them.

```text
CSTAR_ALGEBRA_UNIQUENESS_IMPLIES_RAW_G_UNIQUENESS = false | TYPE-R |
  test: C0 exports no scalar functional/dynamics and the raw-G source topology
        is independently unbuilt
```

### 8.3 No overclaim from finite restriction

Only two finite results are claimed:

```text
A_fin^(p) restricts exactly to A_N^(p);
the finite Q-243 mixed block is zero.
```

No complete raw `G`, physical restriction map, or T5 square is claimed. Q-244
is carried explicitly: matching finite output without a restriction map is
not a pass.

### 8.4 No false cancellation

Nothing is divided by a `p_ch`-dependent quantity. The direct finite mixed
block is zero by branch projection. The complete verdict remains open.

## 9. Scope and bounded searches

Roots entered:

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha-program-archive/cleanroom_output
/Users/bgm/MB Work/alpha_supervision
```

Excluded:

```text
.git and binary/media payloads;
archive mirrors as independent authority;
superseded versions except where a live source names them for lineage;
a32_holdout/custodian_private (not entered, listed, searched, opened, or read).
```

Case-insensitive queries included:

```text
source topology | continuum topology | finite-support dense | dense
ell1 | l1 | Banach limit | restriction-invisible | annihilator | cylindrical
finite_scalar_CTP_to_complete | projective-limit CTP
finite-to-complete intertwiner | restriction complete correlator
Z_inc[J,R] | s_R | D_R := D_J | raw connected contour correlator
nonzero differentiable Log | finite restriction T5 | common origin
```

This artifact makes no corpus-wide claim that no topology-shaped phrase exists.
The bounded negative relied upon is the already sealed Item-2 result at lines
128-168: the six governing source-evidence files supply no named physical
source topology/calculus and leave L1 TYPE-U. Direct reads of the current
DoR-008, C0, U3, raw-map, and Item-2 authorities confirm no later producer in
this task's governing chain.

## 10. Answers in relay order

1. **Completed raw-correlator signature.** `G` is the symmetric-bilocal-source
   derivative of the scalar physical `W_inc=-i hbar Log_0 Z_inc` on the
   completed physical quotient/source domain. Its common/difference source
   family carries physical field and spacetime indices, measure, branch
   grammar, prescription, and domains. C0 supplies only bounded finite-support
   operator source maps.
2. **Constructed arrow.** The exact finite family constructs one scalar
   `A_fin^(p)` on the zero-extension direct union and reproduces all finite
   derivatives. The arrow stops before `Z_inc[J,R]`: no scalar common-origin
   functional, independent bilocal-source dependence, or physical source germ
   exists.
3. **Falsifier.** It pins the direct finite cylindrical mixed block to zero on
   every genuine restriction. It does not pin the completed block because the
   restriction maps and `Tail_R={0}` separation theorem are unbuilt. T5 remains
   inapplicable, and Q-244 bars proxy agreement.
4. **Re-entry channel.** `p_ch` can re-enter only through completed `Z_inc`
   content outside the direct finite mixed block: a restriction-null physical
   term or a `p_ch`-dependent stationary/on-shell background. The measure,
   contour, boundary data, domains, provenance, source topology, `X_K^phase`,
   and phase evaluator decide it.
5. **Kill-passes.** No measure, contour, topology, bilocal dependence, or
   uniqueness was supplied. The naive continuous C-star extension was attacked
   and refuted. No nonexecutable finite test was reported as a pass.

## 11. Final flags and custody

```text
TASK4A_FINITE_DIRECT_UNION_FUNCTIONAL_CONSTRUCTED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-011

TASK4A_CORRELATOR_COMPLETION_ARROW_COMPLETED = false | TYPE-U |
  would-build: SOURCE_GERM_PHYS, independent bilocal source dependence,
               common-origin scalar dynamics/state/effects, the five Q-239
               fields, and finite-to-physical restriction intertwiners

DIRECT_CSTAR_CONTINUOUS_EXTENSION_REFUTED = true | TYPE-R |
  test: moving-tail sequence in the ratified compact-spectrum topology

FINITE_DIRECT_RETHESS_BLOCK_P_CH_FREE = true | TYPE-P |
  premises: Q-243 and DoR-008, DoR-009, DoR-011

COMPLETE_RETHESS_BLOCK_P_CH_FREE = NO_VERDICT
DELTAPHI_P_CH_FREE = NO_VERDICT

DOR008_Q243_FALSIFIER_VERDICT = NO_VERDICT
RESTRICTION_SEPARATION_THEOREM_DERIVED = false | TYPE-U

Q_244_CARRIED = true
Q_244_EFFECT = matching proxy output is not a completion restriction pass

FENCE_BLOCKED_STRUCTURAL_RESULT = false
MACHINERY_APPEAL = NOT_TRIGGERED

alpha_computed = false [TERMINAL_FENCE_DECLARATION]
proof_authorized = false [TERMINAL_FENCE_DECLARATION]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION]
coupling_evaluation_authorized = false [TERMINAL_FENCE_DECLARATION]
production_authorized = false [TERMINAL_FENCE_DECLARATION]
```

Custody under `LOCKED_PROCESS.md`: this lane seals this append-only artifact,
verifies its sidecar, mirrors only the artifact and sidecar to the archive
workspace, reports, and stops. It does not register, commit, or push.
