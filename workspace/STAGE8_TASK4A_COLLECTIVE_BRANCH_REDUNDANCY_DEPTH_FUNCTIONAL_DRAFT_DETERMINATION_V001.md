# Stage 8 Task 4a Collective Branch-Redundancy Depth Functional Draft Determination v001

Date: 2026-08-03  
Lane: CODEX LANE 1  
Task: PASTE 411 / Task 4a  
Register head at freeze: Q-328  
Plan head: C42  
Status: **THE SEALED COLLECTIVE RECORD STATE EXISTS, BUT IT DOES NOT SELECT A UNIQUE REDUNDANCY FUNCTIONAL. THE MINIMAL WHOLE-ENSEMBLE INFORMATION CANDIDATE SATURATES AFTER ONE CELL AND IS CYCLE-INERT; THE NATURAL GROWING CANDIDATE IS EXTENSIVE AND FAILS C42'S NO-PER-CELL-ADDITIVITY BATTERY. NO CANDIDATE COMPLETES THE EIGHT-ITEM BRIDGE OR RELATES TO THE SEALED GEOMETRY ESTIMATOR. DoR-016 REMAINS RESERVED.**

```text
PROPOSED_NOT_ADOPTED -- NOT_RATIFICATION_READY -- DoR-016_RESERVED
NEW_TYPE_P_CLAIMS = 0

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

---

## 0. Lead determination

The exact finite outgoing record state is already sealed. For every finite
`N>=1`, the current ratified write gives

```text
sigma_0,N = |R_N><R_N|,
sigma_1,N = |P_N><P_N|,

omega_N^(p)
  =(1-p) sigma_0,N + p sigma_1,N,                 (RD-1)

<R_N|P_N>=0,
p=p_[A]=r_ch/(r_0+r_ch).                          (RD-2)
```

The one branch label is shared by all cells. Equation `(RD-1)` is a global
Bernoulli mixture, not a tensor product of independent Bernoulli mixtures.
Its finite restrictions obey

```text
omega_M^(p) composed with iota_NM = omega_N^(p).  (RD-3)
```

This is enough to compute candidate distinguishability and correlation
functionals. It is not enough to select one as **the** physical depth.

The literal sector distinguishability is already maximal at every `N>=1`:

```text
(1/2)||sigma_0,N-sigma_1,N||_1 = 1,
F(sigma_0,N,sigma_1,N)=0,
P_error,opt=0.                                    (RD-4)
```

Those quantities carry no symbolic `p` and no stage depth. The smallest
prior-weighted whole-ensemble candidate is the branch information

```text
R_N^info
  := I(B:E_N)
   = h_2(p)
   = -(1-p) Log(1-p)-p Log p,                     (RD-5)
```

where `B` is the single charge-branch label and `E_N` is the complete finite
record ensemble. This candidate is collective, real, quotient-invariant,
symbolic in the rank pair, and exactly unchanged by identity extension. But
it also obeys

```text
R_M^info=R_N^info=h_2(p) for every M,N>=1.         (RD-6)
```

It therefore measures the information carried by the branch record, not how
deeply the record has accumulated. The ideal current law commits fully after
one cell.

The canonical growing correlation quantity is instead

```text
T_N
  := sum_(j=1)^N S(omega_1^(p))-S(omega_N^(p))
   =(N-1)h_2(p).                                  (RD-7)
```

It measures correlation among cells through the shared branch, but it is
exactly extensive in the number of genuine cells. C42 makes “no per-cell
additivity anywhere” a battery row, so `(RD-7)` is not an admissible draft
answer. Applying an arbitrary nonlinear monotone `f(T_N)` removes literal
additivity but introduces an unselected function `f`.

The remaining exact state functionals disagree just as sharply: purity and
branch variance are stage-independent; relative entropy between the two
orthogonal sectors is singular; posterior/probe entropies require treating a
source insertion as evidence and are not monotone on the full symbolic
family. No relevant sealed text names Holevo information, mutual information,
total correlation, trace distance, or another selector for this role.

Consequently:

```text
COLLECTIVE_BRANCH_STATE_EXISTS = true | SEALED_INPUT

UNIQUE_COLLECTIVE_REDUNDANCY_FUNCTIONAL_SELECTED = false | TYPE-S |
  scope: the sealed state, germ, finite-probe, PathCert, direct-limit,
         and geometry-estimator authorities read here

R_N_INFO_PROPOSED = true |
  standing: PROPOSED_NOT_ADOPTED |
  formula: h_2(p_[A])

R_N_INFO_IS_NONTRIVIAL_STAGE_DEPTH = false | TYPE-R |
  test: RD-6

T_N_TOTAL_CORRELATION_PASSES_C42_NO_ADDITIVITY = false | TYPE-R |
  test: RD-7

ADMISSIBLE_NONTRIVIAL_REDUNDANCY_DEPTH_CONSTRUCTED = false | TYPE-U
DIVERGENCE_TO_CYCLE_ACTION_BRIDGE_COMPLETED = false | TYPE-U
GEOMETRY_ESTIMATOR_RELATION_PROVED = false | TYPE-U
PHYSICAL_P_VERDICT = NO_VERDICT
```

This draft does not reject collective emergence. It locates a stronger
fact: under the present ideal write, collective distinguishability saturates
before there is any nontrivial depth to transport.

---

## 1. Custody, currency, and scope

### 1.1 Frozen authorities

| Authority | SHA-256 | Load-bearing use |
|---|---|---|
| `LOCKED_PROCESS.md` | `f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba` | fences, typing, custody |
| `QUESTIONS_SETTLED_REGISTER_V001.md` | `8d92eccf4323b200399d76de3d08fc80faf5f0b3bf3d060deac18e9b4c58c341` | Q-328 head at freeze |
| `TASK_LIST_HERE_TO_ALPHA_2026-08-01_V002.md` | `e28ec12da47c7e7f289f563f1f6a3c9825ae7bb7312da2e19bcd25ef4f0fb8a9` | C42 commission and DoR-016 reservation |
| `RELAY_PASTE_411_THE_REDUNDANCY_DRAFT_V001.md` | `71d97bdf7d6e6cd9ba4a3c945e30373ce09c3237f6f0f70da33cb472dc4d8c0a` | task contract |
| `STAGE8_TASK4A_BOHM_DEPTH_DEDUP_COCYCLE_BRIDGE_ADVERSARIAL_VERIFICATION_V001.md` | `7618adcc7846bd469624577442c19e28cfaa1318e53321d6666a444e0f1fa06d` | Q-328 mixture defect and battery constraints |
| `STAGE8_ENVELOPE_FINITE_PATHCERT_DYNAMICS_SUBTRACE_CONSTRUCTION_V001.md` | `74a1f903ce79fc76a0f32a036a872b2d59b8944aa9e4211135d65ba8e9800db0` | exact finite state, restrictions, outgoing GNS |
| `STAGE8_TASK4A_FINITE_NONZERO_R_REFERENCE_EXACT_PROBE_SOURCE_COMPUTATION_V001.md` | `c7624d88aedaa0659755b5c566121b24c2ad0c29a0060daada43a31b22a6ddfb` | historical finite probe weight and zero extension |
| `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V007.md` | `bd33e54c27ddb8ed5224637d7888a071026db33a1a17c7127a27ffa647b69896` | live source exponent and current bilocal functional |
| `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V004.md` | `d4cdbb6623797df6accb7dc9b24134d179bfc8e8d039c585d5c91ae23255869e` | symbolic rank quotient and `p_[A]` |
| `STAGE8_G_PRIMITIVE_OR_EMERGENT_ADJUDICATION_V001.md` | `273f03dd0b89c688289e47b9735250e9595d81ae6ade951fb5fa3df1daef81d3` | geometry estimator and `l_P` boundary |
| `STAGE8_GRAVITY_MATTER_SOURCE_SUMMANDS_LIVE_V004_STANDING_V001.md` | `58208084e8da8d9d7dd7c048d917363be1c00e5a9b5870ce1c6409083c23a72c` | active gravity and `l_P` premise standing |
| `STAGE8_TASK4A_DIVERGENCE_DETERMINED_TRANSVERSE_CYCLE_ACTION_DRAFT_DETERMINATION_V001.md` | `ed49624b6f5f0bcda94ee88a939a5751113b30d73192b2c28a5aec25829e1797` | eight-item bridge contract |

### 1.2 Preflight

```text
DOES_THE_COLLECTIVE_STATE_EXIST = true

DOES_THE_UNIQUE_REDUNDANCY_FUNCTIONAL_EXIST = false | TYPE-U |
  reason: the state supports inequivalent exact distinguishability,
          information, uncertainty, and correlation functionals

IS_THE_VERSION_CURRENT = true |
  register head: Q-328 |
  plan head: C42

ARE_THE_INPUTS_PRESENT = PARTIAL |
  present: finite mixture, symbolic p, restrictions, outgoing GNS,
           live source germ, geometry estimator |
  absent: redundancy selector, genuine-depth rule, cycle descent,
          action square, geometry relation
```

### 1.3 Roots entered

```text
ROOTS_ENTERED = (
  /Users/bgm/Documents/New project/gravity_emergence_evidence_program/
    alpha_fundamental_record_action_cleanroom_v003,
  /Users/bgm/Documents/New project/gravity_emergence_evidence_program,
  /Users/bgm/MB Work/alpha_supervision,
  /Users/bgm/MB Work/alpha-program-archive/workspace
)

a32_holdout/custodian_private/ = NOT_ENTERED | TYPE-S
```

### 1.4 Acts not performed

```text
redundancy functional adopted or selected          false | TYPE-S
rank pair selected                                 false | TYPE-S
source insertion declared a physical measurement  false | TYPE-S
per-cell weight factorization assumed              false | TYPE-S
cycle representative or basis selected             false | TYPE-S
weak-* or bidual completion invoked                false | TYPE-S
physical response or fixed point evaluated         false | TYPE-S
coupling or alpha evaluated                        false | TYPE-S
measured constant compared                         false | TYPE-S
register, governing plan, or tracker edited        false | TYPE-S
git, commit, or push performed                     false | TYPE-S
```

---

## 2. The exact collective state

### 2.1 Finite completed state

`STAGE8_ENVELOPE_FINITE_PATHCERT_DYNAMICS_SUBTRACE_CONSTRUCTION_V001.md:190-250`
constructs the current finite dynamics and obtains

```text
rho_N
 =P_0 rho_S P_0 tensor |R_N><R_N|
  +P_ch rho_S P_ch tensor |P_N><P_N|.
```

Restricting to the record algebra gives

```text
omega_N^(p)(A)
 =(1-p)<R_N|A|R_N>+p<P_N|A|P_N>,                 (RD-8)
```

with

```text
|R_N>=|r>^(tensor N),
|P_N>=|p_Q>^(tensor N).
```

The ready and pointer vectors are distinct orthogonal cell-basis vectors, so
their tensor powers are orthogonal for every `N>=1`. The phase in the
single-history charged branch cancels against its adjoint. The state is
therefore a classical two-sector mixture on two orthogonal supports.

### 2.2 Sequential and direct-limit structure

The same authority at `:251-304` proves

```text
iota_NM(A)=A tensor I_(M-N),
omega_M composed with iota_NM=omega_N,
```

and constructs the isometric GNS direct limit. The state reaches an outgoing
record limit. The limit is record-only; it is not a completed physical action
or source-inclusive state.

### 2.3 Forced symbolic branch weight

`STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V004.md:338-368` gives

```text
p_[A]=Tr_A(P_ch)/Tr_A(I_A)
     =r_ch/(r_0+r_ch),
```

on each same-rank gauge class. No rank pair is selected. V007 preserves this
state weight and the source functional.

```text
COLLECTIVE_STATE_PROVENANCE = SEALED_AND_RATIFIED_INPUTS
REDUNDANCY_SELECTOR_PROVENANCE = ABSENT
```

---

## 3. Symbol collisions

The three `Q_N` objects required by C42 are:

```text
Q_N^carrier          = U(1)^N, the sequential relative-history carrier;

Q_N^hist(R)          = the Q-279 historical same-cell difference/difference
                       probe functional in artifact c7624d88...;

Q_n^even(R)          = the live V007 trace-dual of
                       hbar ell_n tensor ell_n.
```

They are not interchangeable. Two further symbols must remain separate:

```text
Q_j^grav = boundary flux record in the gravity estimator;
R_N      = the proposed redundancy functional in this draft,
           not the ready record vector |R_N> and not a bilocal source R.
```

For clarity, this artifact writes the proposal as `Red_N` whenever a formula
could otherwise collide with the ready vector or bilocal source.

---

## 4. Exact candidate census

No candidate below is adopted. The calculations show what the sealed state
permits and why the choice is physical content.

### 4.1 Literal sector distinguishability

For the conditional states `sigma_0,N` and `sigma_1,N`, orthogonality gives

```text
D_tr,N=(1/2)||sigma_0,N-sigma_1,N||_1=1,
F_N=0,
P_error,N=0.                                      (RD-9)
```

Properties:

```text
zero-extension       invariant
genuine-cell growth  none after the first cell
p dependence         none
reality              invariant
quotient descent     yes at record-state level
```

This is the most literal answer to “distinguishability of the two sectors,”
but it fails the requested manifest `p` dependence and is not a depth.

### 4.2 Whole-ensemble branch information

Introduce only as accounting the classical branch label `B` already encoded
by the two central projectors. Since `E_N` determines `B` without error,

```text
Red_N^info:=I(B:E_N)=S(omega_N)=h_2(p).           (RD-10)
```

This is the minimal proposed candidate retained by the draft because it uses
the whole state, not a product of invented cell weights.

Properties:

```text
zero-extension       exact equality
genuine-cell growth  nondecreasing but saturated: equality for N>=1
p dependence         h_2(p), symbolic
reality              real and phase-blind
quotient descent     depends only on the same-rank class p_[A]
direct limit         constant compatible family
```

It passes the extension checks but fails as a nontrivial depth object.

### 4.3 Branch variance and purity

The mixture also fixes

```text
V_N=p(1-p),
Tr[(omega_N)^2]=(1-p)^2+p^2.                      (RD-11)
```

These are exact and `p`-dependent, but stage-independent. `V_N` measures
uncertainty of the branch variable, not record redundancy. Purity moves in
the opposite semantic direction from accessible branch information.

### 4.4 Total correlation

Each one-cell marginal has entropy `h_2(p)`, while the entire orthogonal
two-branch mixture also has entropy `h_2(p)`. Therefore the standard total
correlation is `(RD-7)`:

```text
T_N=(N-1)h_2(p).
```

It has the attractive interpretation that every genuine new pointer copy is
correlated with the ensemble through the same branch. It also exposes the
exact price:

```text
T_(N+1)-T_N=h_2(p).
```

Thus it is a per-genuine-cell extensive count. C42 expressly disallows that
answer. It is listed to make the conflict visible, not to smuggle it through
under the word “collective.”

### 4.5 Redundancy count

The number of disjoint one-cell fragments that each reveal the branch is `N`
for the ideal current law. This is the direct-limit redundant-record result's
ideal-copy meaning. It is again an extensive per-cell count, has no `p`
dependence, and fails C42's battery.

The historical imperfect-overlap expression

```text
|<E_0^(N)|E_1^(N)>|=|gamma|^N
```

would provide nontrivial approach with depth when `0<|gamma|<1`, but `gamma`
is not a parameter of the current ratified exact write. The live law realizes
the orthogonal endpoint. Importing an imperfect overlap would add physics.

### 4.6 Nonlinear transforms

For any monotone `f`, the expression

```text
Red_N^f=f(T_N)
```

can be made bounded and nonadditive. Nothing in the relevant sealed stock
selects `f`, its normalization, or its asymptote. This is an unbounded
authored family, not a derivation.

### 4.7 Candidate verdict table

| Candidate | Collective | `p` visible | Nontrivial in `N` | Nonadditive | Sealed selector |
|---|---:|---:|---:|---:|---:|
| trace distance / optimal error | yes | no | no | yes | no |
| `Red_N^info=h_2(p)` | yes | yes | no | yes | no |
| variance/purity | yes | yes | no | yes | no |
| total correlation `(N-1)h_2(p)` | yes | yes | yes | **no** | no |
| redundancy count `N` | ensemble-level count | no | yes | **no** | no |
| `f((N-1)h_2(p))` | yes | generally | generally | can be | **no; free `f`** |

```text
EXACT_CANDIDATE_FAMILY_NONEMPTY = true
EXACT_CANDIDATE_FAMILY_SINGLETON = false | TYPE-R
C42_ALL_REQUIRED_PROPERTIES_HAVE_ONE_SELECTED_MEMBER = false | TYPE-U
```

---

## 5. Extension and monotonicity tests

### 5.1 Identity extension

If an appended factor is common to both sectors, `tau`, then

```text
sigma_b,N -> sigma_b,N tensor tau,
```

and all candidate sector distinguishabilities and `Red_N^info` are unchanged.
This is the correct collective identity-cell statement. It does not require
a local dephasing weight.

The actual direct-system certificate `(RD-3)` gives the corresponding
observable restriction equality.

```text
IDENTITY_CELL_ADDS_DISTINGUISHABILITY = false |
  result: exact for the collective state candidates
```

### 5.2 Genuine current-law cell

A new genuine current-law cell appends `|r>` on the neutral branch and
`|p_Q>` on the charged branch. Because the old conditional sectors were
already orthogonal, the whole-ensemble information and distinguishability
remain saturated:

```text
Red_(N+1)^info-Red_N^info=0.
```

Thus weak monotonicity holds by equality. Strict monotonicity fails.

```text
R_INFO_MONOTONE_NONDECREASING = true | DRAFT_CALCULATION
R_INFO_STRICTLY_INCREASES_ON_GENUINE_CELL = false | TYPE-R
```

The only exact current-state candidates that increase are extensive counts
or functions chosen from those counts.

---

## 6. Probe-on collective weights

### 6.1 Historical Q-279 source weight

Artifact `c7624d88...` gives the historical local-source expression

```text
w_N(R)=1-p+p exp[-Q_N^hist(R)/2].                 (RD-12)
```

If one additionally interprets a real attenuating source as Bayesian
evidence, normalization would produce the tilted charged weight

```text
omega(R)
 =p exp[-Q/2]/[1-p+p exp(-Q/2)].                  (RD-13)
```

That evidence interpretation is not sealed: `R` is a generating source, not
a declared measurement outcome or effect. Even conditionally, the candidate
entropy `h_2(omega(R))` is not globally monotone in `Q`. Exact differentiation
gives

```text
d omega/dQ=-(1/2)omega(1-omega),

d h_2(omega)/dQ
 =-(1/2)omega(1-omega) Log[(1-omega)/omega].       (RD-14)
```

The sign changes across the symbolic family. Other choices such as posterior
variance, likelihood-ratio shift, or relative entropy give different
functionals.

Under lawful zero extension,

```text
Q_M^hist(iota_NM R)=Q_N^hist(R),
w_M(iota_NM R)=w_N(R),
```

so no depth accumulates for one fixed source.

### 6.2 Live V007 source weight

The current germ is

```text
Z_n^007[J,R]
 =(1-p_[A])+p_[A] exp[L_n^Theta(J)-(1/2)Q_n^even(R)],

Q_n^even(R)=<hbar ell_n tensor ell_n,R>.           (RD-15)
```

Q-328 records the live kernel fact: a cycle direction lies in `ker ell_n`.
Consequently the generated bilocal line has zero component when tested on a
cycle direction. Every smooth scalar redundancy candidate built only from
the live tilted weight has zero first cycle response at that interface.

```text
LIVE_WEIGHT_CYCLE_RESPONSE_NONZERO = false | TYPE-R |
  test: cycle direction in ker ell_n

HISTORICAL_Q279_NONZERO_R_ROWS_DEFINE_LIVE_CYCLE_RESPONSE = false | TYPE-R |
  reason: pairing/version mismatch plus absent cycle map
```

The probe tables therefore do not build the desired bridge. They either
remain source functionals or become trivial on the live cycle kernel.

---

## 7. Eight-item bridge accounting

Q-409's contract is applied without assuming any missing item.

| Item | Current result | Verdict |
|---|---|---|
| 1. `DivergenceDatum` / redundancy datum | exact collective state plus a non-singleton candidate functional family; minimal proposal `Red_N^info` | **PARTIAL / selector `TYPE-U`** |
| 2. `DepthMap` | `N` indexes compatible record states, but `Red_N^info` is constant and growing candidates are extensive or unselected transforms | **FAIL / `TYPE-U`** |
| 3. `CycleMap` | no map from record-state redundancy to `X_phys` or `K_cycle`; live probe line vanishes on cycle directions | **FAIL / `TYPE-U`** |
| 4. `AccumulationRule` | identity extension is certified; no admissible nontrivial nonadditive accumulation rule is selected | **FAIL / `TYPE-U`** |
| 5. `ActionComparisonSquare` | no map turns state information into a scalar physical action | **FAIL / `TYPE-U`** |
| 6. generator/uniqueness | candidate census proves nonuniqueness; no failure-capable selector | **FAIL / `TYPE-R` against uniqueness** |
| 7. form certificates | source/state reality and quotient properties hold for `Red_N^info`; flatness, off-section content, action restrictions, and physical domain do not exist | **PARTIAL / physical rows `TYPE-U`** |
| 8. provenance | state and `p` have provenance; information-functional choice, depth rule, cycle descent, and action normalization do not | **FAIL / `TYPE-U`** |

```text
BRIDGE_ITEMS_COMPLETE = 0
BRIDGE_ITEMS_PARTIAL = 2
BRIDGE_ITEMS_FAILED = 6

REDUNDANCY_TO_CYCLE_ACTION_BRIDGE_EXISTS = false | TYPE-U
```

The count treats partial items as incomplete. No bridge item is silently
promoted because its input state exists.

---

## 8. Coupling-side test against Q-408

Q-408's exact formal dependence is

```text
Delta M_CK=D_C D_K phi,
delta G_K[delta phi]=-H_CC^(-1)D_C(delta phi).      (RD-16)
```

There is no lawful substitution because `Red_N^info` is a scalar state
functional, not a physical action on the `(C,K)` tangent carrier.

Even under the deliberately stronger hypothetical identification

```text
phi(C,K):=Red_N^info=h_2(p),
```

with symbolic ranks held fixed, the candidate is constant in both physical
directions, so

```text
D_C D_K phi=0,
D_C(delta phi)=0.                                  (RD-17)
```

This is not the sought nonperturbative content. It is an action-irrelevant
constant. Total correlation is likewise only a stage/rank scalar until a
cycle/action map is supplied; its `N` dependence does not create `(C,K)`
derivatives.

The live probe route also gives zero on cycle directions by Section 6.2.

```text
Q408_REDUNDANCY_SUBSTITUTION_EXECUTED = false | TYPE-U

R_INFO_WOULD_GENERATE_NONZERO_Q408_MIXING = false | TYPE-R |
  scope: hypothetical constant identification RD-17

PI_R_IND_FROM_REDUNDANCY_EXISTS = false | TYPE-U
PHYSICAL_P_VERDICT_FROM_REDUNDANCY = NO_VERDICT
```

The exact `p` dependence exists in the state information, but no exact map
places it in the physical response.

---

## 9. Geometry-estimator test

### 9.1 The estimator's actual functional form

The gravity source read by
`STAGE8_G_PRIMITIVE_OR_EMERGENT_ADJUDICATION_V001.md:133-157` defines

```text
Q_j^grav=integral_boundary(V_j) g dot n dA,

G_N^est
 =-[sum_j w_j M_j Q_j^grav]
   /[4 pi sum_j w_j M_j^2],                        (RD-18)
```

with declared positive uncertainty/covariance weights. Its convergence
requires calibrated, nondegenerate records governed by one universal
weak-field coupling. It is a weighted regression estimator of a
source-to-boundary-flux conversion.

### 9.2 Comparison with the redundancy candidates

The candidate `Red_N^info` consumes

```text
(p_[A], sigma_0,N, sigma_1,N)
```

and returns branch information. The geometry estimator consumes

```text
{(w_j,M_j,Q_j^grav)}_j
```

and returns a dimensional conversion estimator. The two functions share no
argument, restriction map, covariance, or extremization rule in the sealed
text. The shared word “record” is not a mathematical map.

```text
REDUNDANCY_FUNCTIONAL_EQUALS_GEOMETRY_ESTIMATOR = false | TYPE-R |
  test: different domains, codomains, and functional forms

SEALED_MAP_REDUNDANCY_TO_GEOMETRY_ESTIMATOR = false | TYPE-S |
  scope: cited gravity adjudication, its primary estimator source,
         PathCert, live germ, and C42 authorities
```

### 9.3 `l_P` does not supply the relation

The active convention is

```text
l_P=sqrt(hbar G/c^3).
```

`STAGE8_GRAVITY_MATTER_SOURCE_SUMMANDS_LIVE_V004_STANDING_V001.md:175-213`
types the gravity action and `l_P` at premise level and says neither is
record-derived. A dimensional conversion constant cannot by itself select

```text
Red_N -> M_j,
Red_N -> Q_j^grav,
Red_N -> area/volume,
```

or a power of `l_P`. Any such choice would be an additional physical map and
normalization.

```text
L_P_STATUS = DECLARED_PHYSICAL_INPUT
L_P_DERIVED_FROM_REDUNDANCY = false | TYPE-U
L_P_ALONE_BRIDGES_REDUNDANCY_TO_GEOMETRY = false | TYPE-R

FIRST_COUPLING_GRAVITY_FUNCTIONAL_CONTACT_ESTABLISHED = false | TYPE-U
```

The double test therefore returns absence, not a numerical disagreement.

---

## 10. Battery and kill passes

| Battery row | Result |
|---|---|
| global mixture respected | **PASS for the draft census:** every formula starts from `(RD-1)` |
| no per-cell dephasing factor | **PASS:** none introduced |
| no per-cell additivity | **FAIL for the only natural growing candidate `(RD-7)`; candidate excluded** |
| three `Q_N` objects distinct | **PASS:** Section 3 |
| identity extension | **PASS for state candidates:** Section 5.1 |
| genuine-cell monotonicity | **weak pass / strict fail:** `Red_N^info` saturates |
| symbolic `p` and ranks | **PASS:** no rank selected |
| reality and quotient | **PASS at state level; physical action remains unbuilt** |
| no target tuning | **PASS:** no response consequence selects a candidate |
| no selection | **PASS:** choice table retained; no member installed |
| restriction execution | **PASS at record-state level; action square absent** |
| geometry estimator relation | **FAIL / absent map** |
| Q-408 physical test | **STOP at domain mismatch; constant hypothetical is inert** |

Counterexample to uniqueness:

```text
Red_N^info=h_2(p)
and
V_N=p(1-p)
```

are both real, collective, zero-extension invariant, rank-symbolic state
functionals. They are not equal as functions of `p`, and neither sealed
reality nor quotient structure selects between them. Adding trace distance
and purity enlarges the witness family.

```text
UNIQUE_REDUNDANCY_FROM_STATED_CONSTRAINTS = false | TYPE-R
TARGET_TUNING_USED_TO_BREAK_TIE = false | TYPE-S
```

---

## 11. Six-account and door ledger

| Account | Current content | Open residue |
|---|---|---|
| measure | finite matrix trace defines the record state; no entropy base or physical measure selected | information-functional convention and any physical measure |
| contour | no contour operation is needed for `(RD-1)` | no contour supplies record-to-cycle descent |
| boundary/contact | record restriction is built; gravity boundary flux is separately defined | map from branch state to boundary-flux records |
| domain closure | outgoing record GNS exists; `T_cyl` is a separate source-label completion | physical action domain and cycle embedding |
| stationary Schur | only formal Q-408 dependence is available | `phi`, stationary locus, complement blocks, inverse |
| class formation | exact candidate functionals can be calculated on finite states | selector, topology, action image, tail and restriction certificates |

Door flags:

```text
DOOR_ENTROPY_SELECTOR = OPEN | proposal choice required
DOOR_SOURCE_AS_EVIDENCE = CLOSED | no measurement/effect rule
DOOR_RECORD_TO_CYCLE = CLOSED | map absent
DOOR_CYCLE_TO_ACTION = CLOSED | comparison square absent
DOOR_REDUNDANCY_TO_GEOMETRY = CLOSED | map absent

DOOR_WEAK_STAR_USED = false
DOOR_BIDUAL_USED = false
DOOR_DISTRIBUTIONAL_COMPLETION_USED = false
DOOR_NEW_MEASURE_USED = false
DOOR_NEW_CONTOUR_USED = false
DOOR_NEW_BOUNDARY_RULE_USED = false
DOOR_CYCLE_INVERSE_USED = false
DOOR_TARGET_AWARE_NORMALIZATION_USED = false
```

---

## 12. Exact successor residue

A ratifiable successor must provide, before consequence inspection:

```text
COLLECTIVE_REDUNDANCY_DEPTH_BRIDGE = (
  1. RedundancySelector:
       a failure-capable rule selecting one functional of omega_N;

  2. ImperfectOrUnsaturatedStructure:
       if strict depth growth is required, a derived non-orthogonal or
       otherwise unsaturated record law, not an imported gamma;

  3. GenuineCellRule:
       a definition separating identity extension from physical addition
       without assuming independent-cell weights;

  4. DepthMap:
       a nontrivial stage-compatible collective accumulation rule satisfying
       C42's no-additivity battery;

  5. CycleMap:
       a signed, quotient-compatible map from collective state variation to
       X_phys or K_cycle, nonzero on the live V007 cycle kernel;

  6. ActionComparisonSquare:
       a map from the selected state functional to a scalar physical action
       with finite restriction certificates;

  7. GeneratorAndFormCertificate:
       uniqueness or a sized family, plus reality, flatness/off-section
       content, topology, rank and no-selection certificates;

  8. CommonOriginProvenance:
       one descent for state, depth, cycle, action, and restrictions;

  9. GeometryRelation:
       a typed map to the arguments of RD-18, including the openly premise-
       level status of l_P and no unselected dimensional power.
)
```

Items 1-8 refine Q-409's contract for the collective-state route. Item 9 is
the second test surface required by C42.

---

## 13. Final verdict

```text
COLLECTIVE_BRANCH_MIXTURE_AVAILABLE = true | SEALED_INPUT

MINIMAL_DRAFT_CANDIDATE = Red_N^info=h_2(p_[A]) |
  standing: PROPOSED_NOT_ADOPTED

MINIMAL_DRAFT_CANDIDATE_PASSES_IDENTITY_EXTENSION = true
MINIMAL_DRAFT_CANDIDATE_PASSES_REALITY_AND_QUOTIENT = true
MINIMAL_DRAFT_CANDIDATE_STRICTLY_MEASURES_DEPTH = false | TYPE-R
MINIMAL_DRAFT_CANDIDATE_HAS_NONZERO_CYCLE_RESPONSE = false | TYPE-R

NATURAL_GROWING_TOTAL_CORRELATION = (N-1)h_2(p_[A])
NATURAL_GROWING_TOTAL_CORRELATION_ADMISSIBLE_UNDER_C42 = false | TYPE-R

UNIQUE_REDUNDANCY_FUNCTIONAL_DERIVED = false | TYPE-R
ADMISSIBLE_NONTRIVIAL_DEPTH_FUNCTIONAL_BUILT = false | TYPE-U
EIGHT_ITEM_BRIDGE_COMPLETE = false | TYPE-U
GEOMETRY_ESTIMATOR_RELATION = false | TYPE-U
Q408_CONSEQUENCES_EXECUTED = false | TYPE-U
PHYSICAL_P_VERDICT = NO_VERDICT

RATIFICATION_READINESS = false
DoR_016 = RESERVED
FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-S
```

The collective state is real physics already present in the program. What is
missing is not evidence of collectivity; it is a nontrivial, nonextensive,
selected measure of collective depth and the map carrying that measure into
the physical cycle action. Under the current ideal write, the most literal
distinguishability has already saturated.

---

## 14. Principal-facing one-line deliverable

```text
NO_VERDICT -- the exact shared-branch state yields a saturated collective
information h_2(p) and an extensive growing correlation (N-1)h_2(p), but no
sealed rule selects an admissible nonadditive depth or maps it to K_cycle,
Q-408, or the geometry estimator.
```
