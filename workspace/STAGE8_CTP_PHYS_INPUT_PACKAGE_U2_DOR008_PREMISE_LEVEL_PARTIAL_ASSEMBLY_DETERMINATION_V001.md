# Stage 8 CTP Physical-Input Package U2 DoR-008 Premise-Level Partial Assembly Determination v001

Date: 2026-08-01  
Lane: Codex lane 2  
Task: 2d  
Register head at construction start: Q-216  
Send-time currency recheck: Q-217

## Lead determination

**`U2_008` does not assemble minus only the dynamics instance. The declared
`rho_pre` cannot be placed on `C0_008`: it is a trace-class state role on a
scalar Hilbert space, while `C0_008` is deliberately a state-free Hilbert
C-star-module and exports no positive scalarization or trace.**

The honest output is a typed U2 skeleton with two instantiated pieces and four
uninstantiated ports:

```text
INSTANTIATED
  1  inclusive module identity I_EC0
  2  bounded carrier/domain anchor D_C0=E_C0 for existing C0 operations

UNINSTANTIATED
  1  scalarization plus joint positive normalized rho_pre
  2  common-origin action/evolution and doubled CTP influence-functional instance
  3  nontrivial admitted record effects with completed domains
  4  predeclared action/source contact rules and dynamics/effect common domain
```

```text
U2_008_SKELETON_ASSEMBLED = true | TYPE-P | premises: DoR-008
U2_008_INSTANCE_EXISTS = false | TYPE-U |
  would-build: instantiate all four open ports above on one common construction
               trace and pass the U2 certificates

U2_008_COMPLETE_EXCEPT_DYNAMICS = false | TYPE-R |
  test: the scalar-state, nontrivial-effect, contact-rule, and dynamics-domain
        ports are independently empty before the dynamics instance is tested

RHO_PRE_PLACED_ON_C0_008 = false | TYPE-U |
  would-build: a common-origin positive functional B->C, its scalar
               realization, and a positive normalized trace-class joint state

INCLUSIVE_MODULE_IDENTITY_INSTANTIATED = true | TYPE-P | premises: DoR-008
ADMITTED_NONTRIVIAL_RECORD_EFFECT_INSTANCE_COUNT = 0 | TYPE-S |
  scope: Q-200-compliant P5 census members on C0_008

d_U2_SKELETON_PREMISE_LEVEL_TOTAL = true | TYPE-P | premises: DoR-008
d_U2_PREMISE_LEVEL_TOTAL = false | TYPE-U |
  would-build: the four missing ports
d_U2_COMMON_ORIGIN_DERIVED = false | TYPE-U |
  would-build: a P5 common-origin descent presentation from an independently
               supplied microscopic construction trace

PHYSICAL_VERDICT = NO_VERDICT
CONSTRUCTION_VERDICT = U2_SKELETON_ASSEMBLED__FOUR_INSTANCE_PORTS_OPEN
```

The four open ports may ultimately arrive in one joint common-origin physical
CTP realization. The corpus has not proved that collapse, so this artifact does
not rename four absent fields as one present object. The doubled influence
functional remains the integrator that Tasks 2d, 3a, and 3c all need; it is not
identified with the state, effects, contacts, or their descent certificates.

## 1. Preflight, currency, and exact U2 contract

### 1.1 Preflight

```text
DOES_THE_OBJECT_EXIST = PARTIAL
  reason: the U2 signature and two canonical C0-level pieces exist; no complete
          U2 instance exists

IS_THE_VERSION_CURRENT = true
  basis: register read through Q-217; Q-216 makes U1_008 current and leaves U2
         next; Q-217 confirms that C0/U1 still supplies no finite scalar
         representation or non-tautological B_square source operator

ARE_THE_INPUTS_PRESENT = PARTIAL
  basis: C0_008 and U1_008 exist; the P5 census contains rows rather than
         complete packages; common-origin dynamics remains TYPE-U
```

Q-216 does not supply state, dynamics, effects, contacts, or U3 content. It
only establishes U1 conventions on the C0 interface. Q-217 arrived after the
initial construction and seal. It does not supply a missing U2 instance. It
independently confirms the scalar-realization absence found here and redirects
the finite-incidence realization problem to future source/dynamics operators
across U2/U3. That redirect is a consumer requirement, not permission to pull
the `B_square` bridge or any U3 datum into this U2 assembly.

### 1.2 Exact signature

The B0 stop specification at
`STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md:1001-1013`
defines:

```text
U2 = microscopic action/evolution, positive normalized pre-state, inclusive
     identity, admitted effects, action/source contact rules, and common domains
```

and at `:1016-1027` requires

```text
d_U2 : (B0_candidate,C0) -> U2
```

with no post-output supplementation. The substitute-admissibility adjudication
at
`STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_SUBSTITUTE_ADMISSIBILITY_ADJUDICATION_V001.md:194-215`
adds the operational requirements: positivity, normalization, effect
completeness where claimed, common-domain compatibility, dynamics
compatibility, action/source contacts, and one descent witness.

The producer signature sharpens the same interface at
`STAGE8_RANK1_CTP_PRODUCER_ALGEBRA_Q52_SPEC_V001.md:251-262`:

```text
P5  positive normalized rho_pre, admitted E_r, and their domains from the same
    microscopic source;
P6  S_CTP or U_BR on the common domain, supplying the normalized inclusive CTP
    amplitude;
P7  contact/source rules and a raw-correlator output interface.
```

### 1.3 Frozen authorities

| Authority | SHA-256 | Use |
|---|---|---|
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_C0_DOR008_ASSEMBLY_AND_FIRST_RESTRICTION_TEST_V001.md` | `1467ab9850022931e68dc9ffa625d95099d8f6bb74d734dc9d0466f169bd00b6` | Exact `C0_008` carrier and bounded domain |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_U1_DOR008_ASSEMBLY_DETERMINATION_V001.md` | `1b0e928c452c10a8be72be22ff81fd7677f5045d2ad8d398a9f7f7f57b9ab3b0` | Current branch/source convention layer |
| `STAGE8_SECTION53_P5_AXIS_COVERAGE_AND_EXCLUSION_AUDIT_V001.md` | `1274b1b71b46e6a34b641c0053d61ce1ed16c94e8d570317a7831f558bcfef58` | Frozen P5 row ledger |
| `STAGE8_P5_FAMILY_EXCLUSION_THEOREM_ATTEMPT_V001.md` | `00300b0a888fd3efe2ab3be48cd275d35da58b547002aecb4adb8bb36f155fce` | Q-200 package-instance audit |
| `STAGE8_P5_COMMON_ORIGIN_DESCENT_REQUIREMENT_V001.md` | `a33be83c1ee7cbfbda2cc3857425cb9e7e90a23bbe3d61c9ec89432e50b77874` | Minimal common-origin presentation |
| `STAGE8_TASK3A_FOUR_LORENTZIAN_FORMS_AND_DURABILITY_ADJUDICATION_V001.md` | `056c30481c9c2a055e9b4c7cd7d381e25caf4eaf5aa4ec8a170aa6ba67f65b00` | Current dynamics/output architecture |
| `STAGE8_FIELD_CTP_V002_SECOND_ADVERSARIAL_KILL_DETERMINATION_V001.md` | `58f2c82121e7fb34c91212ca0181c71c455eca077ce9f6d060835eb0407c3c93` | Scalarization firewall and countermodel |
| `primitive_record_cell_selection_principle_v004.md` | `13d227ceb2198d96b0e4e2fef57b874cea71cb755320508fbf4c6d64a00c507e` | Formal state/effect/contact consumer roles |
| `primitive_complete_boundary_transition_functional_principle_v002.md` | `be79ca5e08010b53285cd157ba4c18d2029f08bc93bea2db02d5423b67428c34` | Complete record-conditioned CTP architecture |
| `STAGE8_TASK2F_FINITE_INCIDENCE_REALIZATION_FUNCTOR_FORCING_PROTOCOL_RESULT_V001.md` | `a4d8b9c44fd0705ba97fd49d1e0c8373c28e12e2c3acea9409b60217b274a0f8` | Q-217: 1,088 filtration survivors and missing scalar/source realization of `B_square` |
| Decision of Record 008 | `d51a6d5c5bb0020a081cfd2adfb545b9f5ed86ce660d3feacadc5ef68140fb19` | Premise standing and finite-authority falsifier |

All conditional construction claims below carry `TYPE-P | premises: DoR-008`.
No P5 role statement is promoted to an instance merely because its row is
sealed.

## 2. Carrier-type test — can rho_pre be placed on C0_008?

### 2.1 What rho_pre requires

`primitive_record_cell_selection_principle_v004.md:17-25` says:

```text
rho_pre is a positive trace-class initial density operator on the full
source-record-field Hilbert space, normalized by Tr rho_pre=1.
```

The P5 census repeats that role at
`STAGE8_SECTION53_P5_AXIS_COVERAGE_AND_EXCLUSION_AUDIT_V001.md:203-257`.
Its row at `:266-274` expressly says that the completed Hilbert space, physical
domain, and common-origin producer are absent.

### 2.2 What C0_008 actually is

The ratified presentation at
`STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md:368-439`
sets

```text
B := A_F_CTP,
E_C0 := H_SR external-tensor B_B,
<xi tensor x,eta tensor y>_B := <xi,eta>_H_SR x* y.
```

`E_C0` is a Hilbert `B`-module, not a scalar Hilbert space. Every coefficient
of its inner product lies in `B`. A scalar realization requires a positive
functional

```text
omega : B -> C
```

followed by a null-space quotient and completion. The presentation supplies no
`omega`, cyclic vector, density, trace, integration map, or measure.
`C0_008` preserves this exclusion at
`STAGE8_CTP_PHYS_INPUT_PACKAGE_C0_DOR008_ASSEMBLY_AND_FIRST_RESTRICTION_TEST_V001.md:493-517`.

Consequently, “put the declared `rho_pre` on the joint carrier” is not an
assignment operation. The expression `Tr rho_pre` has no typed trace on
`E_C0` as it stands, and trace-class is not canonically the same notion as a
positive adjointable module operator.

### 2.3 Adversarial scalarization countermodel

The independent V002 kill-pass at
`STAGE8_FIELD_CTP_V002_SECOND_ADVERSARIAL_KILL_DETERMINATION_V001.md:195-260`
exhibits two inequivalent positive scalarizations of the same field algebra:

```text
tau_0(U_lambda)=0 for lambda!=0, tau_0(1)=1,
epsilon(U_lambda)=1 for every lambda.
```

Both are mathematically available; C0 selects neither. Therefore the carrier
does not force one scalar Hilbert realization, still less one density operator
on it. Selecting either here would be a new adoption in U2, contrary to the
task.

```text
C0_008_IS_SCALAR_HILBERT_SPACE = false | TYPE-R |
  test: compare the B-valued inner product codomain with C-valued Hilbert-space
        inner-product and trace requirements

C0_008_EXPORTS_POSITIVE_FUNCTIONAL_B_TO_C = false | TYPE-S |
  scope: C0_008 tuple and all operation codomains

C0_008_FORCES_UNIQUE_PHYSICAL_SCALARIZATION = false | TYPE-R |
  test: tau_0 and epsilon are inequivalent positive candidates and neither is
        exported

RHO_PRE_ROLE_IS_A_CONCRETE_C0_008_STATE_INSTANCE = false | TYPE-R |
  test: the role supplies properties but no omega, scalar realization, density
        operator, or common-origin descent map

RHO_PRE_PLACED_ON_C0_008 = false | TYPE-U |
  would-build: StatePort_U2_008 in Section 3.2
```

This is not a defect in DoR-008. The scalarization firewall was a ratified C0
boundary designed to prevent exactly this state import. U2 is the correct
owner of the missing state construction.

## 3. The U2_008 skeleton

### 3.1 Instantiated carrier and U1 interface

Freeze without rebuilding:

```text
Carrier_U2_008 := C0_008,
Convention_U2_008 := U1_008,
D_anchor_008 := D_C0 = E_C0.
```

`D_anchor_008` is invariant under the bounded adjointable C0 generators and
source-map outputs. It is not yet a dynamics domain.

```text
U2_CARRIER_ANCHOR_INSTANTIATED = true | TYPE-P | premises: DoR-008
U2_BOUNDED_DOMAIN_ANCHOR_INSTANTIATED = true | TYPE-P | premises: DoR-008
```

### 3.2 State port — specified, not instantiated

The smallest state object that can meet the sealed role is

```text
StatePort_U2_008 := (
  omega_phys : B -> C,
  H_omega := completion of E_C0 / N_omega,
  pi_omega : A_C0 -> B(H_omega),
  rho_pre in trace-class(H_omega),
  rho_pre >= 0,
  Tr_omega(rho_pre)=1,
  state_domain,
  state_descent_map,
  state_provenance_certificate
).
```

`N_omega` here is the null space of the scalarized module form, not U3's
physical gauge quotient. No U3 quotient or measure is constructed by naming
this representation-theoretic port.

The source-sector quasifree state is not transported across this gap. It does
not supply `omega_phys` on the field/CTP factor, the completed joint density,
or effects. This is exactly the ceiling recorded at
`STAGE8_P5_COMMON_ORIGIN_DESCENT_REQUIREMENT_V001.md:152-180`.

```text
U2_STATE_PORT_SPECIFIED = true | TYPE-P | premises: DoR-008
U2_STATE_PORT_INSTANTIATED = false | TYPE-U |
  would-build: choose or derive omega_phys without output inspection, construct
               H_omega and rho_pre, and certify common origin
```

### 3.3 Inclusive identity — instantiated at module level

The one canonical U2-facing effect already available on C0 is

```text
I_inc_008 := identity in L_B(E_C0).
```

It is positive, satisfies `0 <= I_inc_008 <= I_inc_008`, preserves `D_C0`,
and is fixed by the U1 branch/reality structure. Under any later lawful scalar
realization it descends to the identity operator. It is therefore an exact
module-level instance of the inclusive baseline effect.

It does not by itself produce a scalar normalization identity because
`rho_pre`, the trace, and dynamics are absent.

```text
U2_INCLUSIVE_MODULE_IDENTITY_INSTANTIATED = true | TYPE-P |
  premises: DoR-008
U2_INCLUSIVE_SCALAR_TRACE_NORMALIZATION_EXECUTED = false | TYPE-C |
  constraint: StatePort_U2_008 and DynPort_U2_008 are uninstantiated |
  release: instantiate both and test the zero-source identity
```

### 3.4 Admitted record effects — no nontrivial instance

The Q-200-compliant P5 ledger at
`STAGE8_SECTION53_P5_AXIS_COVERAGE_AND_EXCLUSION_AUDIT_V001.md:259-279`
contains:

```text
F0 formal rho_pre role
F1 one adopted source-sector state/contour branch
F2 alternative-state schema
F3 inclusive identity baseline
F4 record-conditioned effect schema E_r=C_r^dagger C_r
F5 exhaustive POVM/instrument schema
F6 domain-choice schema
```

The independent exclusion attempt at
`STAGE8_P5_FAMILY_EXCLUSION_THEOREM_ATTEMPT_V001.md:95-138` proves that these
are heterogeneous rows, not seven complete packages. Its `:198-245` confirms
that the identity is a baseline non-mutation and that the effect rows do not
supply executable members.

The current carrier makes `F3`'s module identity concrete. It does not turn
`F4-F6` into instances. No `C_r`, public record-label set, effect domain,
instrument map, completeness certificate, target-awareness declaration, or
common-origin descent map is supplied.

Define the required open port, without filling it:

```text
EffectPort_U2_008 := (
  public record-label set R_pub,
  {C_r,E_r=C_r^dagger C_r}_{r in R_pub},
  0 <= E_r <= I,
  {D_r},
  completeness/instrument certificate if exhaustive,
  effect descent maps,
  admission and provenance certificate
).
```

```text
P5_CENSUS_ROW_COUNT = 7
P5_COMPLETE_PACKAGE_COUNT = 0 | TYPE-S |
  scope: frozen Q-200 P5 row family
U2_NONTRIVIAL_EFFECT_INSTANCE_COUNT = 0 | TYPE-S |
  scope: Q-200-compliant admitted effects on C0_008
U2_EFFECT_PORT_SPECIFIED = true | TYPE-P | premises: DoR-008
U2_EFFECT_PORT_INSTANTIATED = false | TYPE-U |
  would-build: concrete public record classes, effects, domains, completeness
               claims where applicable, and one common-origin certificate
P5_CENSUS_CORRECTION_REQUIRED_BY_THIS_RUN = false | TYPE-S |
  scope: member-versus-schema classifications; only the baseline identity gains
         a C0 module-level realization
```

### 3.5 Dynamics — exact interface, no instance

Q-210 fixes the complete output architecture. At
`STAGE8_TASK3A_FOUR_LORENTZIAN_FORMS_AND_DURABILITY_ADJUDICATION_V001.md:78-139`
the complete object is one doubled complex CTP influence functional. Its
source-level form is

```text
Z_r[A_+,g_+;A_-,g_-]
  = Tr(E_r U_BR[A_+,g_+] rho_pre U_BR[A_-,g_-]^dagger)
    / Tr(E_r U_BR[0,g_0] rho_pre U_BR[0,g_0]^dagger),

Gamma_r = -i log Z_r.
```

The physical common-origin instance remains Type-U at that artifact
`:150-178`. A single-branch amplitude, noise kernel alone, or real kinetic
action alone fails as the complete counterpart.

The exact U2 dynamics interface is therefore

```text
DynPort_U2_008 := (
  S_CTP or equivalent U_BR[A,g],
  action/evolution domain D_dyn,
  action on the scalar realization of C0_008,
  compatibility with U1_008 branch/source conventions,
  consumption of StatePort_U2_008 and EffectPort_U2_008,
  predeclared action/source contact rules,
  zero-source inclusive normalization certificate,
  CTP reality and common gauge/source covariance certificates,
  common-origin descent map and construction trace,
  output interface to the doubled complex CTP influence functional
).
```

This specifies what dynamics must supply and to what. It does not evaluate a
functional or insert a trial action.

The two seam-11 trial potentials are not candidates for this port. Q-209
records them as fragments rather than complete actions, and both fail the
isolated-background durability test unchanged. Q-210 additionally establishes
that neither a trial potential nor any single component supplies the complete
two-history architecture.

```text
U2_DYNAMICS_INTERFACE_SPECIFIED = true | TYPE-P | premises: DoR-008
U2_DYNAMICS_COMMON_ORIGIN_INSTANCE_INSTANTIATED = false | TYPE-U |
  would-build: DynPort_U2_008 with the state/effect/domain/contact ports and
               one frozen common-origin trace
TRIAL_POTENTIAL_USED_AS_U2_DYNAMICS = false | TYPE-S |
  scope: this artifact's dynamics slot
```

### 3.6 Contacts and common domains — partial anchor only

The package split is explicit at
`STAGE8_CTP_PHYS_INPUT_PACKAGE_TRIAGE_AND_LOAD_BEARING_FUNCTIONAL_SPEC_V001.md:866-923`:
U2 supplies predeclared action/source contact rules and common domains, while
differentiated contact distributions are downstream `D3` outputs. The B0 stop
specification at `:1109-1114` assigns input contact rules to U2/U3 and leaves
derived contacts after source differentiation.

No sealed artifact supplies the U2 input contact rule for a concrete
`S_CTP`/`U_BR` on C0_008. The absence of unbounded generators inside C0 does not
make the later contact rule empty: U2 dynamics may introduce unbounded fields,
equal-time relations, and source insertions.

Define the open interfaces:

```text
ContactPort_U2_008 := (
  predeclared action/source insertion rule,
  equal-time and coincident-source convention where applicable,
  compatibility with U1 source symmetry/order,
  domain and provenance certificate
),

DomainPort_U2_008 := (
  D_anchor_008=D_C0 for existing bounded operations,
  D_dyn,
  {D_r},
  invariant-domain proofs for dynamics, effects, contacts, and observables
).
```

```text
U2_CONTACT_PORT_SPECIFIED = true | TYPE-P | premises: DoR-008
U2_CONTACT_RULE_INSTANTIATED = false | TYPE-U |
  would-build: a concrete pre-response action/source contact rule descending
               with DynPort_U2_008

U2_DOMAIN_ANCHOR_INSTANTIATED = true | TYPE-P | premises: DoR-008
U2_DYNAMICS_EFFECT_COMMON_DOMAIN_INSTANTIATED = false | TYPE-U |
  would-build: D_dyn and every D_r plus invariance/intersection certificates
```

## 4. Exact partial object and descent maps

### 4.1 U2 skeleton

The constructed object is deliberately not named `U2_008`:

```text
U2_Skel_008 := (
  carrier_anchor        = C0_008,
  convention_anchor     = U1_008,
  bounded_domain_anchor = D_C0,
  inclusive_identity    = I_inc_008,
  state_port            = StatePort_U2_008 [UNINSTANTIATED],
  effect_port           = EffectPort_U2_008 [UNINSTANTIATED except identity],
  dynamics_port         = DynPort_U2_008 [UNINSTANTIATED],
  contact_port          = ContactPort_U2_008 [UNINSTANTIATED],
  domain_port           = DomainPort_U2_008 [PARTIAL],
  provenance_record     = Prov_U2_Skel_008
).
```

The name prevents a slot presentation from masquerading as the complete U2
instance.

```text
U2_Skel_008_IS_AN_INSTANCE = true | TYPE-P | premises: DoR-008
U2_Skel_008_IS_COMPLETE_U2 = false | TYPE-R |
  test: four required ports are marked uninstantiated in the exact tuple
```

### 4.2 Premise-level partial descent

Let `F_U2` be the frozen U2 authorities in Section 1.3. The lawful total map is

```text
d_U2_Skel^P[F_U2]
  : (P_008,C0_008,U1_008) -> U2_Skel_008.
```

It instantiates only the carrier, convention, identity, and bounded-domain
anchors and fixes all missing interfaces before any descendant output exists.

The requested complete premise-level map would be

```text
d_U2^P : (P_008,C0_008) -> U2_008.
```

It is not total because `P_008` deliberately contains no scalarization, state,
dynamics, effects, contacts, or U2 domains. The map is reported absent rather
than supplied with an external choice.

```text
d_U2_SKELETON_PREMISE_LEVEL_TOTAL = true | TYPE-P | premises: DoR-008
d_U2_PREMISE_LEVEL_TOTAL = false | TYPE-U |
  would-build: StatePort, EffectPort, DynPort, ContactPort, and completed
               DomainPort on one frozen trace
```

### 4.3 Common-origin provenance

The stronger package map remains

```text
d_U2 : (B0_candidate,C0) -> U2.
```

Q-158 names the weaker sufficient provenance object as a
`P5_COMMON_ORIGIN_DESCENT_PRESENTATION`: executable state/effect/domain/dynamics
descent maps, one construction trace, property and dynamics certificates, and
a target-independent admissibility manifest
(`STAGE8_P5_COMMON_ORIGIN_DESCENT_REQUIREMENT_V001.md:66-125`).

Nothing here supplies that trace.

```text
d_U2_Skel^P_EQUALS_COMMON_ORIGIN_d_U2 = false | TYPE-R |
  test: the skeleton map begins at ratified presentation data and has four open
        ports; d_U2 begins at one common-origin microscopic construction

d_U2_COMMON_ORIGIN_DERIVED = false | TYPE-U |
  would-build: the P5 common-origin descent presentation and execute its
               positivity, normalization, completeness, domain, covariance,
               causality, and no-supplementation tests
```

## 5. Failure-capable certificates

### U2-008-C1 — state carrier/type certificate

Required: a scalar Hilbert realization, a trace-class positive density, and
unit normalization.

Named failures:

- the bare role `rho_pre` fails because it has no operator identity or carrier
  map;
- an arbitrary positive adjointable module operator fails because no scalar
  trace makes it a normalized density;
- choosing `tau_0` or `epsilon` without authority fails no-supplementation.

```text
U2_C1_STATE_PLACEMENT = FAIL_UNBUILT | TYPE-U |
  would-build: StatePort_U2_008
```

### U2-008-C2 — inclusive identity certificate

Required: positivity, upper bound by identity, domain invariance, and U1
compatibility. `I_inc_008` passes all four algebraically on `E_C0`.

The scalar normalization check remains constraint-blocked because state and
dynamics are absent.

```text
U2_C2_MODULE_IDENTITY = PASS | TYPE-P | premises: DoR-008
U2_C2_SCALAR_NORMALIZATION = UNEXECUTABLE | TYPE-C |
  constraint: StatePort and DynPort absent
```

### U2-008-C3 — Q-200 effect-instance certificate

Required: canonical member identity, domain/codomain, effect operator, record
label, admission provenance, and common-origin trace.

Named failures: the `E_r=C_r^dagger C_r`, POVM, instrument, and domain rows
fail instance typing because `C_r`, labels, domains, and certificates are not
supplied. They are not physically refuted.

```text
U2_C3_NONTRIVIAL_EFFECT_INSTANCE = FAIL_UNBUILT | TYPE-U |
  would-build: EffectPort_U2_008
```

### U2-008-C4 — dynamics architecture certificate

Required: one doubled complex CTP influence-functional instance with both
coherent and noise components, state/effect consumption, CTP identities,
common-origin provenance, and zero-source inclusive normalization.

Named failures:

- one trial potential lacks the complete architecture and durability;
- a single-branch amplitude lacks the two-history identities;
- noise alone lacks coherent response;
- kinetic response alone lacks state/effects/noise.

```text
U2_C4_DYNAMICS_ARCHITECTURE_SPECIFIED = PASS | TYPE-P | premises: DoR-008
U2_C4_DYNAMICS_INSTANCE = FAIL_UNBUILT | TYPE-U |
  would-build: DynPort_U2_008
```

### U2-008-C5 — contact/domain certificate

Required: a predeclared contact rule and domains invariant under every U2
operator. `D_C0` passes only for existing bounded C0 operations and the
identity effect.

Named failure: reusing `D_C0` as `D_dyn` without testing the later action or
evolution exceeds C0's certificate at its own `:200-221`.

```text
U2_C5_BOUNDED_ANCHOR = PASS | TYPE-P | premises: DoR-008
U2_C5_COMPLETE_CONTACT_DOMAIN = FAIL_UNBUILT | TYPE-U |
  would-build: ContactPort and completed DomainPort
```

### U2-008-C6 — common-origin/no-supplementation certificate

Required: one trace supplies state, effects, domains, and dynamics before any
response output is inspected.

Named failure: combining the source quasifree branch, the module identity, an
arbitrarily chosen scalarization, and a trial action from unrelated artifacts
is an ad hoc cross-row assembly. Q-158 excludes that presentation.

```text
U2_C6_COMMON_ORIGIN = UNEXECUTABLE | TYPE-C |
  constraint: no complete candidate trace exists |
  release: instantiate the P5 common-origin descent presentation
```

### U2-008-C7 — U3 scope fence

No gauge quotient, contour/spacetime measure, boundary/edge/gluing object,
endpoint domain, or contour prescription is present in `U2_Skel_008`.

```text
U2_C7_U3_EXCLUSION = PASS | TYPE-P | premises: DoR-008
U3_DATUM_PULLED_FORWARD = false | TYPE-S |
  scope: the exact U2_Skel_008 tuple and construction trace
```

### 5.1 Executed structural checker

A separately coded checker froze the seven census row types before testing,
counted complete packages and nontrivial effect instances, and evaluated the
two scalarization candidates on the same nonidentity character generator. It
returned:

```text
row_count                         7
complete_package_count            0
nontrivial_effect_instance_count  0
tau_0 versus epsilon              INEQUIVALENT / PASS
inclusive_identity_role           baseline_identity
```

The checker performs only finite type/count comparisons. It does not construct
a state, select a scalarization, or evaluate a physical functional.

## 6. Adversarial attacks

### 6.1 “The declaration is the state”

Refuted. The declaration fixes properties, not a density operator, carrier
map, scalar trace, or descent certificate. This is the Q-200 schema/instance
distinction applied to `rho_pre` itself.

### 6.2 “Use the source quasifree GNS state”

Rejected. It is a source-sector state/contour branch, not a state on the joint
source-record-field C0 module. It supplies neither field scalarization nor
record effects and common domains.

### 6.3 “The module norm scalarizes the carrier”

Refuted. The norm is nonlinear and cannot be the required positive linear
functional `B->C`; the V002 kill-pass states this at `:195-215`.

### 6.4 “Use the inclusive identity as the complete effect family”

Rejected. The P5 census classifies the identity as a baseline non-mutation.
It does not instantiate any record-conditioned public class or exhaustive
instrument family.

### 6.5 “The C0 common domain is automatically the dynamics domain”

Rejected. C0's certificate expressly stops before later unbounded local
fields, actions, response operators, and scalar Hilbert realizations.

### 6.6 “No contacts exist because C0 is bounded”

Rejected. U2's action/evolution is absent. Its future source insertions and
equal-time rules cannot be inferred empty from the narrower C0 algebra.

### 6.7 “Fill dynamics with a seam-11 trial potential”

Rejected. Both trial potentials are fragments, not complete Q-200 action
instances, and are sealed-rejected unchanged by the durability test.

### 6.8 “Pull the quotient and measure from U3 now”

Rejected by scope. U2 and U3 are siblings; this artifact specifies the U2
ports and leaves later physical evaluation to the joined package.

```text
U2_SKELETON_ADVERSARIAL_BOUNDARY_CHECKS_PASSED = true | TYPE-P |
  premises: DoR-008
```

## 7. Convergence with Tasks 3a and 3c

The doubled complex CTP influence-functional instance is a real shared
construction target:

- Task 2d needs its action/evolution component in `DynPort_U2_008`;
- Task 3a needs its record-facing common-origin physical instance;
- Task 3c needs the same complete response/record architecture rather than a
  trial normalization fragment.

This is one interface with three consumers. It is not the whole U2 gap.
Before it can be evaluated, U2 still needs a scalar state, admitted effects,
contacts, and common domains. A single common-origin producer could supply all
of them together, but no sealed theorem says the influence-functional output
alone generates its own inputs.

```text
ONE_SHARED_INFLUENCE_FUNCTIONAL_INTERFACE_HAS_THREE_CONSUMERS = true | TYPE-P |
  premises: DoR-008 and the sealed Q-210 output architecture
ONE_SHARED_INTERFACE_IS_ALL_OF_U2 = false | TYPE-R |
  test: compare DynPort output with the separate StatePort, EffectPort,
        ContactPort, and DomainPort fields
```

### 7.1 Send-time Q-217 incidence redirect

Q-217 establishes that the finite label-level functor is not forced: all
1,088 incidence-respecting sequential filtrations survive the applicable
tests, and even the additional `v_00`-first anchor leaves 272. More importantly
for this artifact, it finds that `C0_008/U1_008` has no finite scalar
representation or non-tautological source operator corresponding to
`B_square`. The operator-level falsifier therefore cannot yet be posed.

This does not change the U2 partial-assembly verdict. It confirms that the
scalar state port is genuinely absent at C0/U1 level, and it adds one
downstream requirement on the source/dynamics content still to be built:
the eventual U2/U3 package must make `B_square` expressible before the
incidence falsifier can run. Q-217 assigns that burden to U2/U3 jointly; it
does not identify U2 alone as the missing bridge.

```text
Q217_SUPPLIES_MISSING_U2_INSTANCE = false | TYPE-S |
  scope: state, dynamics, effects, contacts, and domains supplied by Q-217
Q217_CHANGES_U2_PARTIAL_ASSEMBLY_VERDICT = false | TYPE-R |
  test: Q-217 supplies no instance for any of the four open U2 ports
B_SQUARE_SOURCE_DYNAMICS_REALIZATION_INSTANTIATED = false | TYPE-U |
  would-build: source/dynamics operator realization across the completed
               U2/U3 package that expresses B_square on its physical carrier
U2_ALONE_IDENTIFIED_AS_B_SQUARE_BRIDGE = false | TYPE-R |
  test: Q-217 assigns the remaining source/dynamics content to U2/U3 jointly
```

## 8. Scope and searches

Roots entered:

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha-program-archive/cleanroom_output
/Users/bgm/MB Work/alpha-program-archive/workspace
/Users/bgm/MB Work/alpha_supervision
```

Exclusions:

```text
.git
sidecars as content authorities
superseded versions as current authority
a32_holdout/custodian_private
```

Word-boundaried, case-insensitive searches included:

```text
rho_pre | positive functional | scalarization | trace-class | B->C
record effect | E_r | C_r | POVM | instrument | record projector
action/source contact | contact rule | common domain | D_dyn | D_r
S_CTP | U_BR | influence functional | complete transfer operator
```

Named record projectors outside the P5 ledger were checked by object role.
None supplies an admitted P5 effect on `C0_008` with a completed domain,
record-label manifest, target-awareness declaration, and common-origin
certificate. Effect-shaped finite or diagnostic projectors were not
transported by name.

`a32_holdout/custodian_private/` was not entered, listed, searched, opened,
summarized, or read.

## 9. Final status

```text
U2_008_SKELETON_ASSEMBLED = true | TYPE-P | premises: DoR-008
U2_008_INSTANCE_EXISTS = false | TYPE-U

U2_CARRIER_ANCHOR_INSTANTIATED = true | TYPE-P | premises: DoR-008
U2_BOUNDED_DOMAIN_ANCHOR_INSTANTIATED = true | TYPE-P | premises: DoR-008
U2_INCLUSIVE_MODULE_IDENTITY_INSTANTIATED = true | TYPE-P | premises: DoR-008

U2_STATE_PORT_INSTANTIATED = false | TYPE-U
U2_EFFECT_PORT_INSTANTIATED = false | TYPE-U
U2_DYNAMICS_COMMON_ORIGIN_INSTANCE_INSTANTIATED = false | TYPE-U
U2_CONTACT_RULE_INSTANTIATED = false | TYPE-U
U2_DYNAMICS_EFFECT_COMMON_DOMAIN_INSTANTIATED = false | TYPE-U
B_SQUARE_SOURCE_DYNAMICS_REALIZATION_INSTANTIATED = false | TYPE-U
U2_ALONE_IDENTIFIED_AS_B_SQUARE_BRIDGE = false | TYPE-R

d_U2_SKELETON_PREMISE_LEVEL_TOTAL = true | TYPE-P | premises: DoR-008
d_U2_PREMISE_LEVEL_TOTAL = false | TYPE-U
d_U2_COMMON_ORIGIN_DERIVED = false | TYPE-U

U3_DATUM_PULLED_FORWARD = false | TYPE-S |
  scope: exact U2_Skel_008 tuple
NEW_ADOPTION_MADE = false | TYPE-S |
  scope: this artifact

TASK2D_U2_COMPLETE = false | TYPE-U
TASK2D_U2_SKELETON_COMPLETE = true | TYPE-P | premises: DoR-008

PHYSICAL_VERDICT = NO_VERDICT
CONSTRUCTION_VERDICT = U2_SKELETON_ASSEMBLED__FOUR_INSTANCE_PORTS_OPEN

alpha_computed = false [TERMINAL_FENCE_DECLARATION]
proof_authorized = false [TERMINAL_FENCE_DECLARATION]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION]
coupling_evaluation_authorized = false [TERMINAL_FENCE_DECLARATION]
production_authorized = false [TERMINAL_FENCE_DECLARATION]
```

No state, dynamics, nontrivial effect, quotient, measure, contact distribution,
response, coupling, scale, root, spectrum, eigenvalue, beta function, absolute
interval, or measured comparison was constructed, computed, or evaluated. No
register, git, commit, push, deployment, or publication action was performed.
