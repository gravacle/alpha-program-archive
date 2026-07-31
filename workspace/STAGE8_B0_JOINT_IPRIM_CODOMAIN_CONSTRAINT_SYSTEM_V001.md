# Stage 8 B0 Joint I_prim/Codomain Constraint System v001

Date: 2026-07-31
Lane: CODEX 1
Register head at issue: Q-111
Road justification: Q-83, `ADVANCES STEP 1`

`alpha_computed = false; proof_authorized = false; kappa_record_computed = false.`

## 0. Premises, scope, and non-actions

This artifact answers relay 206. It consumes the two blind route results as
given and poses their constraints jointly:

```text
I_prim constraints + codomain constraints -> B0 ?
```

It does not re-run either route.

Premises declared at the outset:

1. No new physical premise is adopted.
2. No value, scale, root, eigenvalue, beta function, response coefficient,
   absolute interval, or measured constant is computed.
3. `B0` is not identified with P0, with any flag, or with the T7
   nonvanishing predicate.
4. The incidence-structure route is off limits to this lane.
5. The version-history route is off limits to this lane.
6. Q-91 is followed: no git, no gate, no baseline, no deploy status.

Search and citation scope:

```text
roots:
  /Users/bgm/Documents/New project/gravity_emergence_evidence_program
  /Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003
  /Users/bgm/MB Work/alpha-program-archive/workspace
  /Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md

exclusions:
  a32_holdout/custodian_private/
  Codex 2 version-history work under relay 207
  Einstein incidence-structure work under relay 208

consumed artifacts:
  STAGE8_B0_CODOMAIN_ROUTE_UNDERDETERMINATION_TEST_V001.md
  STAGE8_IPRIM_ROUTE_TO_B0_STOPPING_POINT_AUDIT_V001.md
```

## 1. Lead result

```text
joint_system_determines_B0 = false | TYPE-R |
  test: JOINT-SLOT-COLLAPSE-TEST over the nine Q-110 open slots

joint_system_conflict_found = false | TYPE-R |
  test: JOINT-CONSTRAINT-COMPATIBILITY-TEST over the same slots

B0_built_from_joint_system = false | TYPE-C |
  constraint: residual open fiber remains; no constructed candidate, no
  executed failed adversarial countermodel, and no uniqueness theorem
```

The joint system shrinks Q-110's fiber but does not cut it to a point.

Q-111 supplies presentation structure: six Level-1 upstream premises,
historical conversion constants `c,hbar,G`, and formal CTP presentation
conventions. Those close part of Q-110's "representation" openness and fix
permitted presentation vocabulary. They do not fix B0's type, arity, intrinsic
domain/codomain, dynamical parameters, carrier/core, physical representation,
descent maps, or equivalence relation.

Named residual fiber:

```text
IprimPresentedCodomainCompatibleBoundaryOriginRealizer :=
  {
    (Obj_B0, Sig_B0, Carrier_B0, Core_B0, Prov_B0, DESCEND_B0)
    in CodomainCompatibleBoundaryOriginRealizer
    such that
      presentation constants and formal CTP conventions are fixed by I_prim,
      DESCEND_B0 has the Q-110 production codomain,
      and the remaining open coordinates are not supplied by a new premise
  }.
```

New slot typing used below:

```text
SPLIT-CODOMAIN-SLOT:
  the production codomain of DESCEND_B0 is fixed, while the intrinsic codomain
  of Obj_B0 under Sig_B0 remains open.
```

This is not a new physics class. It is a bookkeeping class forced by Q-110's
distinction between the `DESCEND_B0` interface and the still-open internal
signature of the boundary-origin object.

## 2. Constraint set A: codomain route

Q-110 is recorded in the register at
`/Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md:4465-4489`:

```text
codomain_constraints_determine_B0 = false | TYPE-R
codomain_route_status = UNDERDETERMINED_FIBER
```

and names:

```text
CodomainCompatibleBoundaryOriginRealizer :=
  (Obj_B0, Sig_B0, Carrier_B0, Core_B0, Prov_B0, DESCEND_B0)
```

The source artifact records the production codomain at
`STAGE8_B0_CODOMAIN_ROUTE_UNDERDETERMINATION_TEST_V001.md:88-109`:

```text
DESCEND_B0 maps the candidate to:
SingleOriginPackageInputs(C0,U1,U2,U3,d_C0,d_U1,d_U2,d_U3)
```

and at `:486-496` defines the fiber by conformance, descent, common-origin,
no-supplement, and property-test conditions.

Q-110's open list is at
`STAGE8_B0_CODOMAIN_ROUTE_UNDERDETERMINATION_TEST_V001.md:499-516`:

```text
Type_B0        open
Arity_B0       open
Dom_B0         open
Cod_B0         open
Params_B0      open
Carrier_B0     open if required by the selected type
Core_B0        open if required by the selected type
representation open
descent maps   open: d_C0,d_U1,d_U2,d_U3
equivalence    open
```

The same artifact states at `:518-527`:

```text
B0_underdetermination_degree =
  FIBER-WITH-OPEN-SIGNATURE-AND-OPEN-DESCENT
```

## 3. Constraint set B: I_prim route

Q-111 is recorded in the register at
`/Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md:4493-4525`:

```text
REACHES     the six Level-1 upstream premises
            historical conversion constants c, hbar, G
            formal index, Keldysh ordering, CTP branch metric/reality conventions

DOES NOT    the physical B0 operator; the dynamics; quotient/measure; rho_pre;
REACH       U_BR; effects/domains; the common-origin certificate
```

The source artifact says at
`STAGE8_IPRIM_ROUTE_TO_B0_STOPPING_POINT_AUDIT_V001.md:5-10`:

```text
I_prim reaches only the formal presentation layer of B0
```

and:

```text
It stops before a complete microscopic source-record-field operator/dynamics,
physical quotient/measure, correlator, or common-origin certificate exists.
```

Its surviving upstream inventory at `:12-23` lists:

- six Level-1 rows from
  `STAGE8_FROZEN_PRIMITIVE_INVENTORY_PREFREEZE_RESULT_V001.md:115-131`;
- historical conversion constants `c,hbar,G` from
  `gravity_emergence_newtonian_limit_derivation_v053.md:1063-1077`;
- formal layers in the raw-map specification;
- and excludes `rho_pre`, `U_BR`, effects/domains, quotient/measure, raw
  physical map, B0 witness, and `PrimitiveInventory_0`.

The frozen primitive inventory itself says at
`STAGE8_FROZEN_PRIMITIVE_INVENTORY_PREFREEZE_RESULT_V001.md:115-131`:

```text
The current authority ledgers give only six current Level-1 postulates, not a
full P0 primitive inventory.
```

and:

```text
These six are explicit primitive authorities. They are not enough to supply
Obj_0, because P0 requires source-record-field state, quotient, measure,
effects/domains, dynamics, and raw interface from one microscopic origin.
```

The same file at `:190-218` says `rho_pre`, `U_BR`, effects/domains,
quotient/measure, the raw physical map, `B0_CONSTRUCTION_WITNESS`, and
`PrimitiveInventory_0` are not supplied primitives.

The historical conversion-constant source states at
`gravity_emergence_newtonian_limit_derivation_v053.md:1063-1077`:

```text
c, hbar, and G ... are the three primitive conversion constants
```

with the record meanings:

```text
space records <-> time records       via c
action records <-> phase records     via hbar
source records <-> geometry records  via G
```

The formal Keldysh/order convention is visible at
`STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:795-819`, where
`T_CTP` is displayed and the retarded block is ordered as `(delta,c)`.

Thus:

```text
Iprim_route_supplies_presentation_structure = true
Iprim_route_supplies_B0_physical_operator = false | TYPE-R |
  test: Q-100 upstream/dependency walk and complete-functional hard-gate audit
  recorded in STAGE8_IPRIM_ROUTE_TO_B0_STOPPING_POINT_AUDIT_V001.md:60-62
```

## 4. Joint slot table

The table uses the exact Q-110 open coordinates.

| Q-110 slot | Codomain constraint | I_prim constraint | Joint status | Conflict? |
|---|---|---|---|---|
| `Type_B0` | Allows function, operator, flow, family, relation, algebraic generator, or other type; no type selected. | Supplies Level-1 premises and formal vocabulary only; Q-111 stops before physical operator/dynamics. | **OPEN.** No type collapse. | No. I_prim does not fix a type inconsistent with the codomain role. |
| `Arity_B0` | Requires some candidate to feed `DESCEND_B0`, but leaves intrinsic arity open. | Does not supply an arity; presentation conventions do not choose one. | **OPEN.** | No. |
| `Dom_B0` | Requires conformance to whatever `Sig_B0` declares and descent to C0/U1/U2/U3; does not choose intrinsic domain. | Excludes `rho_pre`, `U_BR`, effects/domains, quotient/measure, and B0 witness from primitives. Supplies no physical domain. | **OPEN.** | No. The I_prim exclusions agree that the domain is not supplied. |
| `Cod_B0` | **SPLIT-CODOMAIN-SLOT:** production codomain of `DESCEND_B0` is fixed as `SingleOriginPackageInputs(C0,U1,U2,U3,d_C0,d_U1,d_U2,d_U3)`; intrinsic `Sig_B0.Cod_B0` remains open. | Does not supply intrinsic codomain; supplies only presentation conventions for later representation. | **PARTIALLY FIXED / INTRINSICALLY OPEN.** | No. |
| `Params_B0` | Leaves parameters open; forbids post-output supplements and target-aware repairs. | Supplies conversion constants `c,hbar,G` and six Level-1 premises, but Q-111 does not make them B0 parameters or close dynamical parameters. | **SHRUNK.** Presentation/unit constants fixed; B0 dynamical parameter record remains open. | No. |
| `Carrier_B0/Core_B0` | Carrier/core data remain open if selected type requires them; C0 must descend from candidate. | Supplies no completed source-record-field carrier or core; Q-111 stops before physical B0 operator and quotient/measure, and formal conventions do not define a core. | **OPEN.** | No. |
| `representation` | Open in Q-110; U1/U3 descendants must be compatible with whatever representation is selected. | **PARTLY FIXES FORMAL PRESENTATION:** index `I=(a,mu,x)`, Keldysh ordering, branch metric/reality convention. Does not fix physical representation, quotient, measure, source/record embeddings, or dynamics. | **SHRUNK.** Formal representation layer fixed; physical representation remains open. | No. |
| `descent maps` | Requires `d_C0,d_U1,d_U2,d_U3`, but leaves the maps open. | Supplies no descent maps and no common-origin certificate. | **OPEN.** | No. |
| `equivalence relation` | Open; no sealed relation collapses candidates with same descendant package. | Pre-registers a comparison criterion for route convergence, but does not supply a B0 candidate-equivalence relation. | **OPEN.** | No. |

Slot verdict:

```text
joint_slot_collapse_count = 0/9
joint_slot_shrink_count = 3/9
joint_slot_conflict_count = 0/9
```

The three shrinkages are:

1. `Cod_B0`: production codomain fixed, intrinsic codomain open.
2. `Params_B0`: presentation/unit constants fixed, dynamical parameter record
   open.
3. `representation`: formal CTP presentation fixed, physical representation
   open.

No slot is fully fixed by the joint system.

## 5. Residual fiber

Q-110's family was:

```text
CodomainCompatibleBoundaryOriginRealizer
```

The joint system narrows it to:

```text
IprimPresentedCodomainCompatibleBoundaryOriginRealizer
```

Definition:

```text
IprimPresentedCodomainCompatibleBoundaryOriginRealizer :=
  {
    r in CodomainCompatibleBoundaryOriginRealizer
    such that
      r uses the six Level-1 authority constraints as its primitive
      presentation frame;
      r uses the historical conversion constants c,hbar,G only in their
      primitive conversion-constant roles;
      r uses the formal compound-index, Keldysh, and CTP branch
      metric/reality presentation conventions; and
      r does not import any I_prim-excluded descendant object as primitive
  }.
```

Residual open coordinates:

```text
Type_B0
Arity_B0
Dom_B0
Sig_B0.Cod_B0
B0 dynamical/structural parameters beyond presentation constants
Carrier_B0/Core_B0
physical representation beyond formal CTP presentation
d_C0,d_U1,d_U2,d_U3
B0 candidate equivalence relation
```

How much smaller than Q-110:

```text
Q110_fiber_open_coordinates =
  type, arity, domain, codomain, parameters, carrier/core, representation,
  descent maps, equivalence

joint_residual_closes =
  none of those coordinates fully

joint_residual_restricts =
  codomain by fixing only DESCEND_B0's production codomain;
  parameters by fixing conversion constants and forbidding descendant imports;
  representation by fixing formal index/Keldysh/CTP reality conventions
```

This is real progress: the residual premise would not be asked to select
formal presentation conventions. It must select the physical boundary-origin
object, its intrinsic signature, physical representation, descent maps, and
equivalence.

## 6. Conflict check

Test:

```text
test_id = JOINT-CONSTRAINT-COMPATIBILITY-TEST
hypothesis =
  I_prim and codomain constraints can be imposed simultaneously.
failure_criterion =
  A slot is fixed by I_prim in a way forbidden by the codomain constraints, or
  the codomain requires a datum that I_prim explicitly forbids from appearing
  even as a descendant.
observed =
  I_prim fixes only presentation/vocabulary/convention data and forbids
  descendant objects from being primitives. Codomain requires descendant objects
  to be produced from B0/C0, not imported as primitives.
execution_status = EXECUTED
```

Result:

```text
joint_system_conflict_found = false | TYPE-R |
  test: JOINT-CONSTRAINT-COMPATIBILITY-TEST; no slot has inconsistent
  assignments, and I_prim's exclusions are compatible with codomain descent
  because they prohibit primitive import, not descendant construction
```

The joint system is consistent as far as these two artifacts decide. It is not
complete.

## 7. Q-92 build decision

Q-92(a)-(f) do not all pass for the joint system.

```text
Q92a_premises_declared = true
Q92b_tests_attached = partial: JOINT-SLOT-COLLAPSE-TEST and
  JOINT-CONSTRAINT-COMPATIBILITY-TEST are attached here; full B0 property tests
  remain candidate-dependent
Q92c_prerequisites_exist = false | TYPE-U |
  would-build: one concrete B0 candidate with intrinsic signature, physical
  representation, descent maps, and equivalence relation
Q92d_road_step_named = true
Q92e_dedicated_verdict_owner_exists = partial: CODEX 1 owns the two structural
  joint tests here; no owner exists here for future candidate property tests
Q92f_adversarial_countermodel_failed = false | TYPE-U |
  would-build: receive and adjudicate the independent countermodel against the
  same constructed candidate
```

Therefore:

```text
B0_constructed_from_joint_system = false | TYPE-C |
  constraint: the joint system leaves a residual open fiber and lacks a
  concrete candidate plus Q-92(e,f) completion
  release: derive a uniqueness/universal property or freeze a principal-
  authorized selector for one residual family member, then execute the candidate
  tests and failed adversarial countermodel
```

No partial B0 is sealed. A partial presentation is not the root object.

## 8. Typed negatives summary

```text
joint_system_determines_B0 = false | TYPE-R |
  test: JOINT-SLOT-COLLAPSE-TEST over Q-110's slot list

joint_system_conflict_found = false | TYPE-R |
  test: JOINT-CONSTRAINT-COMPATIBILITY-TEST

Iprim_route_supplies_B0_physical_operator = false | TYPE-R |
  test: Q-100 upstream/dependency walk and complete-functional hard-gate audit

Q92c_prerequisites_exist = false | TYPE-U |
  would-build: concrete candidate with intrinsic signature, physical
  representation, descent maps, and equivalence relation

Q92f_adversarial_countermodel_failed = false | TYPE-U |
  would-build: receive and adjudicate an independently run Q-92 adversarial
  countermodel against the same candidate, if one is ever built

B0_constructed_from_joint_system = false | TYPE-C |
  constraint: residual fiber remains open and Q-92 candidate/countermodel
  conditions are unsatisfied
```

## 9. Relay answers

1. The joint system consists of Q-110's codomain fiber plus Q-111's presentation
   layer: Level-1 authorities, `c,hbar,G`, formal compound index, Keldysh
   ordering, and CTP branch metric/reality conventions.
2. The joint system does not cut the fiber to a point. The per-slot table is in
   Section 4.
3. The residual fiber is
   `IprimPresentedCodomainCompatibleBoundaryOriginRealizer`. It is smaller than
   Q-110 by fixing presentation constants/conventions and DESCEND_B0's
   production codomain, but it leaves the physical boundary-origin object open.
4. No conflict was found. I_prim's exclusions bar primitive import of
   descendant objects; the codomain route requires descendant construction, so
   the two constraints are compatible.
5. Under Q-92, B0 is not built. No candidate, uniqueness theorem, full verdict
   ownership, or failed adversarial countermodel is present.

No git, commit, push, gate, baseline, or deploy action was performed.
