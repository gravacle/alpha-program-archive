# Stage 8 `Gen_Omega` Generative-Origin-Rule Adoption Proposal v003

**PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL RATIFICATION (DoR-013 RESERVED)**

Date: 2026-08-02  
Lane: CODEX LANE 2  
Task: 4a  
Register head checked at construction start: Q-264

## 0. Lead determination

**No sealed or ratified statement forces the orbit-collapsing anchor.** The
ratified reduced channel is unital, but it is not the preparation channel.
Even the strongest natural consistency relation available between them—exact
commutation with the reduced dephasing channel—admits every charge-block-
diagonal affine preparation channel with an arbitrary invariant state. The
pure-phase/unitary law and charge/flux-access condition likewise constrain the
transition law, not the preparation channel's trace-one affine basepoint.

V003 therefore authors, and does not claim to derive, an anchor family whose
minimal member is the benchmark Q-263 proved sufficient:

```text
ANCHOR_BI(P_src):
  P_src is trace preserving;
  P_src(I_src)=I_src;
  P_src is input-faithful on the charge-superselected traceless space;
  P_src is mixing with one normalized invariant state.
```

Because the current ratified `C0_008` carrier is a Hilbert C-star module and
exports no scalar trace or scalar state, that anchor also needs one disclosed
authored carrier field: a finite scalar source realization
`(H_src^A,Tr_A,P_0,P_ch)` on which `P_0+P_ch=I_src`. This is the price of making
the normalized-identity conclusion well typed. It is not silently attributed
to DoR-008.

Two proven equivalent-strength presentations—finite-trace detailed balance and
irreducible symmetry covariance—are retained as separately disclosed anchor
members. No member is selected: all three force the same state output, while
their distinct transient-dynamics restrictions remain visible. Conditional on
the proposed carrier and any one anchor member, the invariant state is forced
by a theorem internal to the proposal:

```text
rho_anchor = I_src/Tr_A(I_src),

kappa_ch
  = Tr_A(P_ch)/Tr_A(I_src)
  = dim(P_ch H_src^A)
    / [dim(P_0 H_src^A)+dim(P_ch H_src^A)].
```

This is a **forced symbolic form under authored premises**, not an evaluated
value and not a sealed-record derivation. The anchor family was declared
because every member supplies the structural orbit-collapse required by Q-263;
BI is its minimal member. This was done before the consequence was used. The
consequence does not enter membership.

The second V002 kill is repaired by removal. V003 has one root only:

```text
root = |r>,
W(z)|r>=z|p>.
```

The exchanged root is refuted by the sealed finite amplitude and charge/flux
access. It is not retained as an alternative.

Fresh attacks give:

```text
GEN_OMEGA_V003_STATUS = PROPOSED_NOT_ADOPTED

SEALED_ANCHOR_DERIVATION_FOUND = false | TYPE-U |
  missing: a sealed rule transporting unitality or an equivalent
           orbit-collapser from the ratified record dynamics to P_src

ANCHOR_PROVENANCE = AUTHORED_PROPOSAL
AUTHORED_ANCHOR_FAMILY = {ANCHOR_BI,ANCHOR_DB,ANCHOR_SYM}
AUTHORED_COMMON_CARRIER_FIELD_COUNT = 1 [A0]
AUTHORED_ANCHOR_MEMBER_CLASS_COUNT = 3 [BI,DB,SYM]

AFFINE_ARBITRARY_STATE_FAMILY_ADMITTED = false | TYPE-R |
  test: unitality of P_(sigma,lambda) forces sigma=I_src/Tr_A(I_src)

REPLACEMENT_CHANNELS_ADMITTED = false | TYPE-R |
  test: every replacement map annihilates the traceless space

Q242_TWO_STATE_COUNTERMODEL_KILLS_V003 = false | TYPE-R |
  test: every admitted member has the same invariant state

V003_FAMILY_NONEMPTY = true
  [PROPOSAL EXISTENCE THEOREM; NOT RATIFICATION]

ROOT_ORIENTATION_FAMILY_SIZE = 1 [SEALED-INTERFACE DETERMINATION]
EXCHANGED_ROOT_ADMITTED = false | TYPE-R

P_CH_VERDICT = FORCED_SYMBOLIC_FORM_UNDER_AUTHORED_ANCHOR
P_CH_NUMERICALLY_EVALUATED = false

Q254_BATTERY_PASS_COUNT = 11 [PROPOSAL TEST COUNT]
Q254_BATTERY_CONDITIONAL_COUNT = 3 [PROPOSAL TEST COUNT]
Q254_BATTERY_FAIL_COUNT = 0 [PROPOSAL TEST COUNT]

DOR_013_ELIGIBILITY_VERDICT = ELIGIBLE_FOR_CROSS_LANE_ADVERSARIAL_REVIEW
```

Nothing in this document is ratified premise content. DoR-013 remains
reserved. No response, root, coupling, scale, or measured target is evaluated.

## 1. Preflight, currency, authorities, and search scope

**PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL RATIFICATION (DoR-013 RESERVED)**

### 1.1 Preflight

```text
DOES_THE_OBJECT_EXIST = V002_EXISTS_AND_IS_DEAD; V003_IS_THIS_PROPOSAL
IS_THE_VERSION_CURRENT = true_through_Q264_at_construction_start
ARE_THE_INPUTS_PRESENT = true
  V002, both kill determinations, Q-263 benchmark, ratified finite structures
```

### 1.2 Controlling authorities

| Authority | Use |
|---|---|
| `STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V002.md` (`479cfb89...`) | dead predecessor; faithfulness, incidence, law and finite-family limbs retested here |
| `STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADVERSARIAL_KILL_DETERMINATION_V001.md` (`a340f007...`) | Q-260 replacement/root-not-bag kill |
| `STAGE8_GEN_OMEGA_NONCIRCULAR_GENERATIVITY_NO_GO_ATTEMPT_V001.md` (`7000963e...`) | Q-263 anchor-or-Q-260 dichotomy and `C_BI` existence theorem |
| `STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_V002_ADVERSARIAL_KILL_DETERMINATION_V001.md` (`e6586159...`) | Q-264 arbitrary-affine-state and exchanged-root kills |
| `STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_FUNCTIONAL_RESULT_V001.md` | exact `U_N`, `F_N`, reduced `Phi_N`, equal-history identity and plus-root amplitude |
| `STAGE8_SHARED_FINITE_STATE_EFFECT_CONDITIONED_AMPLITUDE_SHARP_STOP_V001.md` | exact visible state quotient and proof that inclusive identity does not select it |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_C0_DOR008_ASSEMBLY_AND_FIRST_RESTRICTION_TEST_V001.md` | current module carrier and state/trace exclusion |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_U2_DOR008_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md` | scalarization firewall and typed state port |
| `STAGE8_LAW_READY_STATE_SEALED_COMMON_ORIGIN_DETERMINATION_V001.md` | law/state signature separation and zero-history exchange |
| `STAGE8_MINIMAL_OMEGA_P5_COMMON_ORIGIN_ROLE_REALIZATION_ATTEMPT_V001.md` | Q-242 root-not-bag standard |
| `STAGE8_TASK4A_MISSING_PHYSICAL_LAYER_CONSOLIDATED_SPEC_AND_CONSTRAINT_BATTERY_V001.md` | Q-254 P1-P11 and B1-B14 |

### 1.3 Anchor-search roots entered

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha-program-archive/workspace
/Users/bgm/MB Work/alpha-program-archive/cleanroom_output
/Users/bgm/MB Work/alpha_supervision
```

Excluded:

```text
a32_holdout/custodian_private/ [not entered]
.git/
binary/media payloads
archive duplicates as independent authorities
superseded versions except the V001->V002->kill lineage
```

Case-insensitive query families run before authoring:

```text
bistochastic | unital | Phi(I) | normalized identity
Phi_N | preparation channel | P_src | commute | intertwine | compose
pure phase | unitary | F_N dagger F_N | equal-history identity
charge/flux access | require | P_0 | P_ch | invariant state
finite source carrier | CAR(H_src) | scalarization | trace-class
```

`rg` was unavailable; `grep`, `find`, `sed`, `awk`, and `nl` were used. No
occurrence was transported without checking its signature.

## 2. The anchor-forcing search

**RESULT: NO SEALED ANCHOR DERIVATION; THREE SPECIFIC TRANSPORTS REFUTED**

### 2.1 Candidate A — unital reduced dynamics

The ratified source-coupled result states at lines 142-150 that

```text
U_N[a]
  =P_0 tensor I_(3^N)+P_ch tensor W_N[a],
P_0+P_ch=I_src.
```

At lines 370-375 it derives the equal-history reduced channel

```text
Phi_N(rho)=P_0 rho P_0+P_ch rho P_ch.
```

Therefore

```text
Phi_N(I_src)=P_0+P_ch=I_src.
```

This is a sealed structural fact. It does not yet concern `P_src`.

The strongest available candidate consistency relation is that `P_src`
commute with the reduced dephasing map. It still does not force unitality.
Let `sigma` be any normalized charge-block-diagonal state and let the symbolic
mixing coefficient be in the nontrivial mixing interval. Define

```text
P_(sigma,lambda)(tau)
  =lambda tau+(1-lambda)Tr_A(tau)sigma.
```

Writing `E_ch=Phi_N`, charge block diagonality gives

```text
E_ch P_(sigma,lambda)(tau)
  =lambda E_ch(tau)+(1-lambda)Tr_A(tau)sigma
  =P_(sigma,lambda) E_ch(tau).
```

But

```text
P_(sigma,lambda)(I_src)
  =lambda I_src+(1-lambda)Tr_A(I_src)sigma,
```

which equals `I_src` exactly when

```text
sigma=I_src/Tr_A(I_src).
```

Thus even exact commutation with the ratified unital channel leaves the whole
state orbit open. Mere composability is weaker and cannot do more.

```text
PHI_N_IS_UNITAL = true [SEALED FINITE FACT]
P_SRC_IS_IDENTICAL_TO_PHI_N = false | TYPE-S |
  scope: ratified law, U2 state port and Gen_Omega lineage

COMMUTATION_WITH_PHI_N_FORCES_P_SRC_UNITAL = false | TYPE-R |
  test: block-diagonal affine channel above

RATIFIED_UNITALITY_TRANSPORTS_TO_P_SRC = false | TYPE-R |
  test: disjoint signatures plus explicit commuting nonunital witness
```

### 2.2 Candidate B — pure phase and unitary finite dynamics

The ratified result derives at lines 169-203

```text
F_N[a_+,a_-]=P_0+Z_N[a_+,a_-]P_ch,
```

with unit-modulus `Z_N`, and at lines 286-298

```text
F_N[a,a]=I_src.
```

Those are relative-history/equal-history facts of `U_N` and the record
sandwich. They do not type a preparation channel. The law/state audit states
at lines 271-297 that the law and source state remain independent inputs and
that the ratified law scope contains no `d_state`.

The affine witness from Section 2.1 composes with the same unitary `U_N` for
every `sigma`; changing `sigma` changes neither `U_N`, `F_N`, nor their
pure-phase certificates.

```text
PURE_PHASE_DYNAMICS_FORCES_PREPARATION_ANCHOR = false | TYPE-R |
  test: hold U_N and F_N fixed while sigma ranges through the affine family

UNITARITY_OF_U_N_IMPLIES_UNITALITY_OF_P_SRC = false | TYPE-R |
  test: the channels act in different ports and the nonunital witness composes
```

### 2.3 Candidate C — required charge/flux access

The source-law kill determination at lines 372-387 defines the relevant test:

```text
W_post(z)|r>=z|p>
```

must vary with the admitted history; `pre`-only fails because it erases the
history. This test selects endpoint attachment in `U_N`. It neither applies
`P_src` nor inspects its invariant state.

The complete visible state quotient proof at
`STAGE8_SHARED_FINITE_STATE_EFFECT_CONDITIONED_AMPLITUDE_SHARP_STOP_V001.md`
lines 183-223 shows that charge superselection permits the entire normalized
weight interval and does not select relative occupation. Every affine channel
in Section 2.1 can be combined with the same charge/flux-accessing `E_post`
law.

```text
CHARGE_FLUX_ACCESS_FORCES_ORBIT_COLLAPSE = false | TYPE-R |
  test: fixed E_post law plus arbitrary block-diagonal affine state family

CHARGE_SUPERSELECTION_SELECTS_RELATIVE_WEIGHT = false | TYPE-R |
  test: exact finite visible-state quotient
```

### 2.4 Search verdict

The corpus supplies an orbit-collapsing **benchmark theorem**, Q-263. It does
not supply the physical premise that makes the benchmark govern `P_src`.

```text
SEALED_OR_RATIFIED_ANCHOR_EXISTS = false | TYPE-S |
  scope: roots and queries in Section 1.3

ANCHOR_DERIVATION_COMPLETED = false | TYPE-U |
  missing: one antecedent record/source rule requiring P_src to be unital or
           imposing an equivalent singleton fixed-state theorem
```

The `TYPE-S` row is a scoped search result. The `TYPE-U` row is the current
construction standing. Neither says an anchor is physically impossible.

## 3. Carrier typing — the authored price before the anchor

**PROPOSED_NOT_ADOPTED — NEW PHYSICS DISCLOSED**

### 3.1 What the current carrier supplies

`C0_008` is

```text
A_src=CAR(H_src),
E_C0=H_SR external-tensor B_B,
<xi tensor x,eta tensor y>_B=<xi,eta> x* y.
```

The U2 audit at lines 164-228 proves that this is a Hilbert C-star module, not
a scalar Hilbert space; it exports no positive functional `B->C`, scalar trace,
or trace-class density. Two inequivalent scalarizations are mathematically
available and neither is selected.

The Q-263 benchmark, by contrast, uses a finite scalar source carrier with
`I_src/Tr(I_src)` a normal state. Q-264 correctly records the unresolved scope
conflict. V003 does not erase it.

### 3.2 Proposed carrier field A0

V003 authors the following field for its **source preparation port only**:

```text
A0_FINITE_SCALAR_SOURCE_REALIZATION := (
  H_src^A := P_0 H_src direct-sum P_ch H_src,
  AUTHORING CONDITION: dim(H_src^A)<infinity,
  A_src^A:=End(H_src^A),
  faithful ordinary trace Tr_A,
  P_0,P_ch orthogonal with P_0+P_ch=I_src,
  q_src:
    End(P_0 H_src direct-sum P_ch H_src) -> A_src^A,
    q_src(T):=T under the displayed carrier identification,
  restriction certificates reproducing every finite P_0/P_ch source result
).
```

The domain of `q_src` is the exact codomain stated at
`STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_FUNCTIONAL_RESULT_V001.md`
lines 554-564; it is not inferred from the field module. The new assertion is
the finite-dimensional physical-source-port typing, not a new matrix formula.
No dimension is selected or evaluated. The ranks remain symbolic. `q_src` is
not claimed to scalarize the full field/CTP module; it realizes only the source
preparation port consumed by the finite law.

| Field | What it adds | Alternatives considered | Why this member | Void condition |
|---|---|---|---|---|
| A0 finite scalar source realization | scalar carrier, faithful trace, source projectors and restriction map | full `C0_008` scalarization; abstract central `C^2` quotient; infinite normal reference state | smallest setting in which Q-263's benchmark and the already finite source law have the same signature | any sealed finite source restriction fails, or the physical source port is proved necessarily nonfinite |
| Full `C0_008` scalarization | state/trace on the entire field module | multiple positive functionals already exhibited | **REJECTED HERE**: imports field state/measure and exceeds Gen_Omega's source role | n/a |
| Abstract central quotient only | normalized state on `span{P_0,P_ch}` | leaves within-sector density and full source descent absent | **REJECTED HERE**: insufficient for complete `rho_S` | n/a |
| Infinite reference-state anchor | a chosen normal reference density or modular/KMS datum | many inequivalent choices | **REJECTED HERE**: the reference state is the output in primitive clothing unless independently derived | n/a |

```text
A0_PROVENANCE = AUTHORED_PROPOSAL
A0_DERIVED_FROM_DOR008 = false | TYPE-R |
  test: DoR-008 scalarization firewall
A0_NUMERIC_DIMENSION_SELECTED = false | TYPE-S |
  scope: this proposal
```

## 4. The authored orbit-collapsing anchor family

**PROPOSED_NOT_ADOPTED — ANCHOR CHOSEN FOR STRUCTURAL MINIMALITY, NOT ITS OUTPUT**

### 4.1 Candidate family

On A0, every candidate retains the common G1 conditions

```text
Delta_0^ss
  :={Delta in T_1(H_src^A):
       Tr_A(Delta)=0 and E_ch(Delta)=Delta}.

G1_v003 := {
  P_src:
    P_src is normal, CPTP and charge covariant;
    P_src E_ch=E_ch P_src;
    P_src has one normalized mixing invariant state rho_P;
    ker(P_src restricted to Delta_0^ss)={0};
    Cert_IF(P_src) is an exact finite certificate;
    there exists a frozen anchor tag A in {BI,DB,SYM}
      with its exact Cert_A(P_src)
}.
```

The complete family is declared before `d_state`. Neither `rho_P`, `p_ch`, a
dimension ratio, nor a downstream output appears in membership.

The three authored anchor members are:

```text
ANCHOR_BI:
  P_src(I_src)=I_src.

ANCHOR_DB:
  P_src equals its adjoint for the finite Hilbert-Schmidt pairing
  <X,Y>_Tr:=Tr_A(X^dagger Y).

ANCHOR_SYM:
  a finite unitary action G on H_src^A is frozen;
  Comm(G)=C I_src;
  P_src is G-covariant.
```

### 4.2 Anchor theorem

For a BI member, unitality gives

```text
P_src(I_src/Tr_A(I_src))=I_src/Tr_A(I_src).
```

For a DB member, trace preservation gives `P_src^dagger(I_src)=I_src`;
self-adjointness then gives `P_src(I_src)=I_src`, reducing DB to the BI proof.

For a SYM member, covariance maps a fixed state to a fixed state. Fixed-state
uniqueness makes `rho_P` invariant under every member of `G`; the declared
commutant equation and normalization then give the same normalized identity.
Therefore, for all three anchor members,

```text
rho_P=I_src/Tr_A(I_src)
```

for every member. The invariant-state image is a singleton.

```text
G1_V003_INVARIANT_STATE_IMAGE_IS_SINGLETON = true
  [DERIVED WITHIN PROPOSAL; PREMISES A0 AND AUTHORED ANCHOR]

ANCHOR_MENTIONS_STATE_OUTPUT = false | TYPE-S |
  scope: displayed G1_v003 membership
ANCHOR_MENTIONS_P_CH_RESULT = false | TYPE-S |
  scope: displayed G1_v003 membership
```

### 4.3 Proven equivalent-strength presentations and their consequences

These are genuine authored alternatives with the same state verdict. They are
not identified as the same transient channel physics:

| Presentation | Structural rule | Exact implication | Standing in V003 |
|---|---|---|---|
| BI direct | `P_src(I)=I` plus trace preservation | normalized identity fixed; sector-dimension-ratio `kappa_ch` form | **AUTHORED MEMBER; MINIMAL** |
| finite-trace detailed balance | `P_src` equals its `Tr_A` adjoint; trace preservation | implies BI, hence the same `kappa_ch` form | **AUTHORED MEMBER; adds reversibility** |
| irreducible symmetry covariance | channel covariant under a frozen action with scalar commutant | uniqueness plus covariance forces normalized identity and the same `kappa_ch` form | **AUTHORED MEMBER; adds symmetry action** |
| reference-density balance | channel preserves a declared `rho_ref` | fixes `rho_ref` | rejected: without an independent derivation, the reference density is the state choice renamed |

The proposal admits the union of the first three certified member classes.
Their state and `kappa_ch` verdicts are invariant across the family; their
transient channel content is not declared equivalent.

### 4.4 Choice table

| Row | Proposed content | Genuine alternatives | Minimality reason | What voids it |
|---|---|---|---|---|
| A0 | finite scalar source realization and trace | full module scalarization; central quotient; infinite reference state | exact minimum making the benchmark well typed | finite restriction mismatch or proof of necessarily nonfinite source port |
| A1-BI | direct bistochasticity `P_src(I)=I` | none inside this member | minimal orbit-collapser | a BI-tagged member is nonunital or has nonidentity invariant state |
| A1-DB | finite-trace detailed balance | direct BI; symmetry covariance | independently meaningful reversibility presentation implying BI | adjoint certificate fails or the BI implication fails |
| A1-SYM | irreducible symmetry covariance | direct BI; detailed balance | orbit collapse by representation structure without naming a state | group/action is incomplete, commutant is nonscalar, or covariance fails |
| A2 | charge-superselected input-faithfulness | replacement channels; one-probe nonvanishing | preserves V002's surviving faithfulness limb and excludes information-erasing reset | kernel witness or invalid finite certificate |
| A3 | exact finite certificate format | unverified global infimum; downstream response witness | makes every datum finite-visible and pre-output | certificate verifier fails |
| A4 | plus root only | exchanged root | sealed `Z_N` and charge/flux access refute exchanged member | plus-root finite interface fails |

All A0-A3 rows are proposal physics. `A1-BI/A1-DB/A1-SYM` form an admitted
family, not a post-output selection. A4 is forced by sealed finite-interface
reproduction and is not an adoption.

## 5. Finite certificate format and nonempty family

**PROPOSED_NOT_ADOPTED — FINITE AUTHORITY EXPLICIT**

### 5.1 Instantiated certificate type

Because A0 is finite, freeze an exact basis

```text
B_ss=(Delta_1,...,Delta_m)
```

of `Delta_0^ss`. For each proposed member, the certificate is

```text
Cert_anchor_IF(P_src):=(
  B_ss,
  exact matrix M_P of P_src restricted to Delta_0^ss,
  exact factorization/inverse certificate for M_P,
  CPTP/charge/superselection certificates,
  finite fixed-space and mixing certificate,
  exactly one anchor certificate:
    BI -> direct check P_src(I_src)=I_src;
    DB -> exact matrix equality P_src=P_src^dagger_Tr;
    SYM -> explicit finite unitary matrices, scalar-commutant certificate,
           and exact covariance equations
).
```

Invertibility of the finite matrix is exactly the kernel condition. This is a
complete finite verifier, not V002's one-probe schema. No global infimum on an
uninstantiated infinite unit sphere is used.

### 5.2 Nonempty witness

Let

```text
omega_tr:=I_src/Tr_A(I_src),

D_lambda(tau)
  :=lambda tau+(1-lambda)Tr_A(tau)omega_tr,
```

with symbolic `lambda` in the nontrivial mixing interval. Then:

1. `D_lambda` is normal, CPTP, charge covariant and commutes with `E_ch`;
2. `D_lambda(I_src)=I_src`;
3. on `Delta_0^ss`, `D_lambda(Delta)=lambda Delta`, so the exact certificate
   matrix is `lambda I` and is invertible;
4. iteration mixes to `omega_tr`; and
5. the normalized fixed state is unique.

`D_lambda` passes BI and DB. It also passes every SYM member whose supplied
unitary action has scalar commutant, because the depolarizing map is covariant
under all unitaries; a finite generalized shift/phase matrix action supplies
an exact scalar-commutant witness in each declared finite carrier dimension.
Thus every anchor member class is nonempty. Unlike V002's witness, its affine
offset cannot range through arbitrary states.

```text
GENERAL_G1_V003_CERTIFICATE_FORMAT_INSTANTIATED = true
G1_V003_NONEMPTY = true [PROPOSAL EXISTENCE THEOREM]
NONEMPTY_WITNESS_CLASS = ANCHORED_DEPOLARIZING_CHANNELS_ACROSS_BI_DB_SYM
```

## 6. Orientation repair by removal

**RESULT: ONE ROOT, FORCED BY THE SEALED FINITE INTERFACE**

The exact one-cell law is

```text
S|r>=|p>,
S|p>=|r>,
D(z)=diag(1,z,1),
W(z)=D(z)S.
```

Therefore

```text
W(z)|r>=z|p>,
W(z)|p>=|r>.
```

The ratified influence result at lines 177-203 derives the plus-root product
`Z_N`. Q-264 computes that the exchanged root instead produces unit factor and
fails charge/flux access. V003 removes it.

```text
root := |r>,
successor := |p>,
|R_N>:=|r>^(tensor N).
```

```text
PLUS_ROOT_REPRODUCES_Z_N = true [SEALED FINITE FACT]
MINUS_ROOT_REPRODUCES_Z_N = false | TYPE-R
MINUS_ROOT_PASSES_CHARGE_FLUX_ACCESS = false | TYPE-R
ROOT_ORIENTATION_SELECTED_BY_FINITE_INTERFACE = true
ROOT_ORIENTATION_RESIDUAL_FAMILY = false | TYPE-R
```

This is not preference or authorship. It is exclusion against an already
sealed output and access requirement.

## 7. Primitive tuple and three maps

**PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL RATIFICATION (DoR-013 RESERVED)**

For every finite `N`, freeze before output:

```text
Omega_prim,N^v003 := (
  A0 finite scalar source realization,
  P_0,P_ch,E_ch,Tr_A,I_src,
  P_src, anchor tag and Cert_anchor_IF(P_src),
  K_cell,iota_cell,plus_root,
  chi_n with n in {+1,-1},
  E_post,
  tensor/zero-extension grammar,
  declared finite domains
).
```

The tuple contains no `rho_S`, ready ray, `U_N[a]`, `p_ch`, response, or
target output.

### 7.1 State map

```text
d_state(Omega_prim,N^v003)
  := the unique normalized fixed state of P_src.
```

The anchor theorem then proves, rather than defines,

```text
d_state(Omega_prim,N^v003)=I_src/Tr_A(I_src).
```

### 7.2 Ready map

```text
d_ready(Omega_prim,N^v003)
  :=C |r>^(tensor N).
```

There is no orientation coordinate and no exchanged member.

### 7.3 Law map

```text
D_n[a_j]=diag(1,chi_n(a_j),1),
W_N^(n)[a]=tensor_(j=1)^N (D_n[a_j]S_j),

d_law(Omega_prim,N^v003;a)
  :=P_0 tensor I_(3^N)+P_ch tensor W_N^(n)[a].
```

This is exactly the ratified DoR-009 `E_post` law. No law coefficient or
attachment was changed.

### 7.4 Frozen construction order

```text
T0 freeze A0, anchor family, certificate format and all non-output fields;
T1 verify the finite carrier/restriction certificate;
T2 verify Cert_anchor_IF before solving a fixed state;
T3 solve the unique fixed-state problem;
T4 prove the anchor theorem and obtain rho_S;
T5 apply the sealed plus-root inclusion;
T6 build the exact E_post transition law;
T7 issue common-input, covariance, domain, no-supplementation and finite checks;
T8 expose outputs only after T0-T7 are frozen.
```

## 8. Mandatory attack reruns

**FRESH TESTS; NO V002 CREDIT INHERITED**

### 8.1 Arbitrary affine-state attack

For

```text
P_(sigma,lambda)(tau)
  =lambda tau+(1-lambda)Tr_A(tau)sigma,
```

unitality requires

```text
lambda I_src+(1-lambda)Tr_A(I_src)sigma=I_src.
```

In the nontrivial mixing interval this is equivalent to

```text
sigma=I_src/Tr_A(I_src).
```

This disposes of BI; DB implies BI and has the same result. For a SYM-tagged
affine member, exact covariance requires

```text
U_g sigma U_g^dagger=sigma for every g in G.
```

The scalar-commutant certificate and normalization again force
`sigma=I_src/Tr_A(I_src)`. Hence the arbitrary `sigma` family that killed V002
is excluded by every anchor member. The residual `lambda` family changes
transient dynamics but not the generated state.

```text
V002_AFFINE_ATTACK_SURVIVES_V003 = false | TYPE-R
ARBITRARY_STATE_OFFSET_SURVIVES_ANCHOR = false | TYPE-R
TRANSIENT_CHANNEL_FAMILY_SURVIVES = true
```

### 8.2 Replacement-channel attack

Every replacement channel

```text
R_rho(tau)=Tr_A(tau)rho
```

annihilates `Delta_0^ss`, so it fails input-faithfulness. The special reset to
`omega_tr` is unital but still fails the kernel test. Thus both anchor halves
are load-bearing.

```text
ALL_REPLACEMENT_CHANNELS_FAIL_V003 = true
REPLACEMENT_FAILURE = INPUT_FAITHFULNESS
```

### 8.3 Q-242 two-state countermodel

Q-242 permits two distinct candidate source states with identical law and
carrier. Under V003, any admitted `P_src` has invariant state `omega_tr`.
Therefore two distinct state outputs cannot both be generated by admitted
members. Origins may differ in transient channel data, as Q-194 permits, but
their state output is identical.

```text
Q242_STATE_IMAGE_CARDINALITY = 1 [PROPOSAL THEOREM]
Q242_COUNTERMODEL_RESULT = PASS_AS_PROPOSAL
ROOT_NOT_BAG_TEST = PASS_AS_PROPOSAL
```

### 8.4 Orientation attack

The attacked minus member is absent. The sole plus member reproduces `Z_N` and
charge/flux access. No binary remains to attack.

## 9. Fresh law, finite-authority, and common-origin certificates

**PROPOSED_NOT_ADOPTED — ALL CERTIFICATES PROPOSAL-RELATIVE**

### 9.1 C1-C8

| Certificate | Fresh V003 result |
|---|---|
| C1 zero-source reduction | PASS AS PROPOSAL: `D_n[0]=I`, exact sealed write |
| C2 equal-history baseline | PASS AS PROPOSAL: branch-unitary cancellation |
| C3 ready/pointer dephasing | PASS AS PROPOSAL on the sole plus root |
| C4 gauge/CTP covariance | PASS AS PROPOSAL with ratified endpoint representations |
| C5 charge/flux access | PASS AS PROPOSAL: `W(z)|r>=z|p>` |
| C6 one-cell authority | PASS AS PROPOSAL: exact `S` and `D_nS` |
| C7 zero extension | PASS AS PROPOSAL: appended `S` factors |
| C8 faithful character/reality | PASS AS PROPOSAL: inherited conjugate character pair |

### 9.2 Common origin, non-circularly

The common-origin certificate consists of four independent tests:

```text
CO1 output-free primitives:
  rho_S, ready ray and U_N[a] are absent from Omega_prim,N^v003.

CO2 orbit collapse before output:
  A0, the BI/DB/SYM anchor tag and Cert_anchor_IF are frozen before the
  fixed-state solution.

CO3 executable descent:
  state is obtained by the fixed-point solve, ready by the plus-root map,
  and law by the incidence/character construction.

CO4 frozen trace and target independence:
  no field is added after output; no field mentions a response, coupling,
  physical residual, measured datum, p_ch consequence, cancellation or survival.
```

Each can fail independently. In particular, a nonunital affine member fails
CO2 and a terminal state coordinate fails CO1.

### 9.3 Finite authority

Every A0/A1/A2/A3 datum is a finite matrix, finite basis, exact finite linear
map, or exact finite certificate. The finite source restriction, plus-root
carrier, and law are explicit. No tail-visible primitive is introduced.

```text
FINITE_CERTIFICATE_SCHEMA_ONLY = false | TYPE-R |
  test: explicit finite basis, matrix, inverse and fixed-space verifier

RESTRICTION_INVISIBLE_ORIGIN_DATUM_ADDED = false | TYPE-S |
  scope: V003 proposal fields
```

## 10. Forced symbolic `p_ch` form and honest fiber account

**CONSEQUENCE OF AUTHORED ANCHOR; NOT AN ANCHOR PREMISE**

After the anchor theorem gives `rho_P=omega_tr`, define the existing visible
quotient

```text
kappa_ch:=Tr_A(rho_P P_ch).
```

Then

```text
kappa_ch
  =Tr_A(P_ch)/Tr_A(I_src)
  =dim(P_ch H_src^A)
   /[dim(P_0 H_src^A)+dim(P_ch H_src^A)].
```

This symbolic ratio is not inserted into the anchor and is not evaluated.
Every admitted preparation channel has the same `kappa_ch`; the residual
channel fiber consists only of transient dynamics invisible to the exact
finite state-conditioned amplitude.

```text
P_SRC_TO_KAPPA_CH_IS_MANY_TO_ONE = true
KAPPA_CH_STATE_FIBER_COUNT = 1 [PROPOSAL CONSEQUENCE]
KAPPA_CH_TRANSIENT_CHANNEL_FIBER_NONTRIVIAL = true

KAPPA_CH_FORM_PROVEN_WITHOUT_TARGET_USE = true
KAPPA_CH_VALUE_EVALUATED = false
```

Target-awareness audit:

```text
ANCHOR_DECLARED_BEFORE_KAPPA_CH_DERIVATION = true
KAPPA_CH_CONSEQUENCE_USED_IN_MEMBERSHIP = false | TYPE-S
KNOWN_OR_MEASURED_TARGET_USED = false | TYPE-S
```

## 11. Full Q-254 battery rerun

**PROPOSAL TESTS DO NOT RATIFY V003**

| Battery row | V003 verdict | Fresh reason |
|---|---|---|
| B1 finite-restriction reproduction | PASS AS PROPOSAL | A0 restriction certificate, plus root and unchanged law reproduce sealed finite interfaces |
| B2 finite retarded baseline | PASS AS PROPOSAL | anchor changes the state origin, not the exact zero finite retarded block |
| B3 finite restrictions remain `p_ch`-free in retarded block | PASS AS PROPOSAL | forced state quotient is not injected into the finite retarded block |
| B4 no naive continuous extension | PASS BY NONCLAIM | V003 asserts only the authored finite source realization and no physical response completion |
| B5 separation only on named class | CONDITIONAL/DOWNSTREAM | needs P2-P6 and a typed `RetHess_phys` class |
| B6 tail explicit | CONDITIONAL/DOWNSTREAM | needs P5-P6 and physical restrictions/`Tail_R` |
| B7 modulo-tail determinacy | PASS BY COMPATIBILITY | no finite equality is promoted to a completed physical identity |
| B8 visible quotients finite-domain | PASS AS PROPOSAL | `kappa_ch` remains explicitly a finite source-state quotient |
| B9 consumer-specific tail certificate | CONDITIONAL/DOWNSTREAM | requires P2-P6 **plus the selected consumer in P9, P10, or P11**; it is not discharged by P2-P6 alone |
| B10 no finite interior stationary point | PASS | no stationary point is asserted or used |
| B11 C1 is not an evaluation rule | PASS | C1 is only the zero-source law limit |
| B12 three zero surfaces distinct | PASS | none are identified |
| B13 finite authority | PASS | A0 and every anchor certificate are finite-visible |
| B14 target independence/no supplementation/common origin | PASS AS PROPOSAL | CO1-CO4 and singleton state-image theorem |

```text
Q254_V003_PASS_COUNT = 11 [PROPOSAL COUNT]
Q254_V003_CONDITIONAL_COUNT = 3 [PROPOSAL COUNT]
Q254_V003_FAIL_COUNT = 0 [PROPOSAL COUNT]
Q254_V003_ACCOUNTING_TOTAL = 14 [PROPOSAL COUNT]

B9_DISCHARGE_PACKAGE = P2-P6_PLUS_SELECTED_CONSUMER_IN_P9_OR_P10_OR_P11
B9_DISCHARGED_BY_V003 = false | TYPE-U
```

## 12. Mandatory self-kill

**PROPOSED_NOT_ADOPTED — INDEPENDENT REVIEW STILL REQUIRED**

### 12.1 Was the condition tuned to the known affine attack?

The anchor is Q-263's independently produced no-go counterexample and is
stated by one carrier equation. It was selected before the `kappa_ch`
consequence and does not name `sigma`, the affine family, Q-242, or any output.
It has an independent operational meaning: maximally mixed input is preserved.

The attack did determine which missing logical function V003 had to supply—an
orbit collapser. That is not answer-defined membership; it is the gate's
predeclared failure condition.

### 12.2 Was circularity moved into A0?

A0 is the weakest part of the proposal. A finite scalar carrier and trace are
new authored physics. They are not called a consequence of DoR-008 and are
not hidden in a certificate. If the physical source port is necessarily the
unscalarized full module, A0 fails and V003 dies.

A0 does not contain `rho_anchor` as a coordinate. It contains carrier, trace,
and projectors; the density follows only after unitality and fixed-point
uniqueness are applied. Nonetheless ratifying A0 knowingly selects a tracial
source realization. The price travels with every downstream use.

### 12.3 Could the same state still be smuggled through a channel coefficient?

No arbitrary state coefficient survives. For the entire affine family,
unitality algebraically forces the coefficient state to `omega_tr`. For a
general admitted channel, fixed-point uniqueness plus unitality gives the same
result without reading Kraus coefficients.

### 12.4 Is the p consequence tuning the anchor?

No. The construction order freezes A0 and A1 before `d_state`; `kappa_ch` is
derived only after the state theorem. Removing every mention of `kappa_ch`
from this artifact leaves the family definition, nonemptiness proof, and
Q-242 result unchanged.

### 12.5 Hostile alternative

A reference-density balance rule could force any desired state while looking
structural. V003 rejects it unless the reference density is independently
derived. This is the reverse-A2 trap and is why the direct normalized-identity
anchor is the only proposed member.

```text
SELF_KILL_HIDDEN_STATE_COORDINATE_FOUND = false | TYPE-S
SELF_KILL_HIDDEN_REFERENCE_DENSITY_FOUND = false | TYPE-S
SELF_KILL_P_CH_TARGET_TUNING_FOUND = false | TYPE-S

SELF_KILL_CARRIER_ADOPTION_RISK_FOUND = true
  [DISCLOSED PROPOSAL PRICE; CROSS-LANE REVIEW REQUIRED]
```

## 13. Release ceiling and final typed board

**PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL RATIFICATION (DoR-013 RESERVED)**

If independently approved and ratified, V003 would supply at every admitted
finite stage:

```text
one scalar source preparation realization;
an anchored nonempty preparation-channel family;
one generated source state and one forced symbolic charge-weight form;
the sealed plus-root ready ray;
the exact DoR-009 law;
finite common-origin and no-supplementation certificates.
```

It would not:

```text
scalarize the complete field/CTP module;
build P2-P11 or SOURCE_GERM_PHYS;
construct a physical response, tail, stationary background, or consumer;
discharge B9;
evaluate kappa_ch or any physical target;
authorize downstream production.
```

```text
GEN_OMEGA_V003_IS_A_PROPOSAL = true [PROPOSAL STATUS]
GEN_OMEGA_V002_REMAINS_DEAD = true

ANCHOR_SEARCH_COMPLETED = true
ANCHOR_DERIVED_FROM_SEALED_RECORD = false | TYPE-U
ANCHOR_AUTHORED_AND_DISCLOSED = true [PROPOSAL STATUS]
AUTHORED_ANCHOR_MEMBER_CLASS_COUNT = 3 [BI,DB,SYM]

A0_FINITE_SCALAR_SOURCE_REALIZATION_PROPOSED = true
A0_FULL_C0_SCALARIZATION_CLAIMED = false | TYPE-S

G1_V003_ANCHOR_FAMILY = {BI,DB,SYM} [PROPOSAL DEFINITION]
G1_V003_BI_IS_MINIMAL_MEMBER = true [PROPOSAL ORDERING]
G1_V003_INPUT_FAITHFUL = true [PROPOSAL DEFINITION]
G1_V003_REPLACEMENT_FREE = true [PROPOSAL THEOREM]
G1_V003_NONEMPTY = true [PROPOSAL THEOREM]
G1_V003_STATE_IMAGE_SINGLETON = true [PROPOSAL THEOREM]

D_STATE_EXECUTABLE = true [PROPOSAL MAP]
D_READY_EXECUTABLE = true [PROPOSAL MAP]
D_LAW_EXECUTABLE = true [PROPOSAL MAP]
D_LAW_EQUALS_DOR009 = true [RATIFIED-FORM REPRODUCTION]

ROOT_PLUS_ONLY = true [SEALED-INTERFACE DETERMINATION]
ROOT_MINUS_REFUTED = true | TYPE-R

KAPPA_CH_FORCED_FORM_UNDER_PROPOSAL = SECTOR_DIMENSION_RATIO
KAPPA_CH_EVALUATED = false

AFFINE_WITNESS_TEST = PASS_AS_PROPOSAL
REPLACEMENT_CHANNEL_TEST = PASS_AS_PROPOSAL
Q242_COUNTERMODEL_TEST = PASS_AS_PROPOSAL
Q254_BATTERY = 11_PASS__3_CONDITIONAL__0_FAIL

V003_SURVIVES_OWN_KILL_PASS = true [PROPOSAL AUDIT]
INDEPENDENT_ADVERSARIAL_REVIEW_COMPLETED = false | TYPE-C |
  constraint: cross-lane review of this exact V003/hash has not run |
  release: independent adversarial determination

DOR_013_ISSUED = false | TYPE-C |
  constraint: proposal is not independently reviewed or ratified |
  release: principal decision after review

PHYSICAL_P5_INSTANCE_COMPLETED = false | TYPE-U
PHYSICAL_VERDICT = NO_VERDICT

TARGET_OUTPUT_USED_TO_NARROW_V003 = false | TYPE-S |
  scope: family, maps and tests in this artifact
FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-S |
  scope: this artifact

alpha_computed = false [TERMINAL_FENCE_DECLARATION]
proof_authorized = false [TERMINAL_FENCE_DECLARATION]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION]
```

No register, gate, decision, plan, tracker, or sealed authority was edited.
