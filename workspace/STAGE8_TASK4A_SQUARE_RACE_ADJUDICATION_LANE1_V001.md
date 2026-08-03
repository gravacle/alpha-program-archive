# STAGE8 TASK 4A: SQUARE RACE ADJUDICATION - LANE 1 V001

Date: 2026-08-03  
Task: PASTE 442 / Task 4a / square-race adjudication  
Lane: CODEX LANE 1  
Register head at preflight: Q-359  
Custody: adversarial adjudication by the derive arm's lane  
Reserved ruling: DoR-017; this artifact adopts nothing

```text
LEAD_RESULT = NOT_READY

KILLING_DEFECT =
  the proposal's load-bearing action-comparison proof is ill-typed:
  rho_f:Y_M->Y_N and F_M:Y_M->R do not compose as F_M o rho_f;
  the lawful pullback is F_N o rho_f.  Consequently B1-18a does not
  prove B1-18, and the proposal does not contain the derived D_G^*
  comparison square exactly.

DERIVED_ROUTE_RESOLUTION =
  Variant Q is forced for the declared phi_div square;
  Variant QE remains lawful for other consumers and is banked, not adopted.

RESIDUE_AUDIT = FAIL |
  the proposal leaves all five derived residue items wholly or partly open
  and adds an unforced algebraic-tensor comparison-family law.

MERGED_CANDIDATE = NOT_READY
READY_FOR_DOR017_RULING = no

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The proposal contains the correct physical cycle carrier and most of the
right finite regressions.  Those passes do not cure the action-square defect.
The canonical comparison operation was already derived: precomposition
`D_G^*f=f o D_G`.  The proposal replaces that forced operation by an authored
stagewise tensor family and then proves its naturality with a composite whose
domains do not match.  Four of the five downstream residue items are also
explicitly left `TYPE-U`, while the first is not instantiated as a generated
action member.  The candidate therefore cannot be sent to DoR-017.

---

## 0. Seal, preflight, and custody

### 0.1 Locked process and register

`alpha_supervision/LOCKED_PROCESS.md` was read in full.  Its sidecar passed.
The live questions-settled register sidecar passed before substantive work,
and its head was exactly Q-359.

```text
DOES_THE_OBJECT_EXIST = yes | Lane-2 proposal under review
IS_THE_VERSION_CURRENT = yes | Q-359
ARE_ITS_INPUTS_PRESENT = yes for adjudication |
  no for a completed action-comparison/2PI square
PREFLIGHT = PASS
```

### 0.2 Hash-verified authorities

| Authority | Verified SHA-256 | Use |
|---|---|---|
| Lane-2 proposal | `c419e7985884e337fae2e03a56352bb1948f3b408bffeed520ea6c9278c096a9` | object under review |
| Lane-1 derive standard | `a9b733c711a692d5eedad8ae6acb5e2829c357c2c6aa3870c1aca2c570604136` | forced diagram and five-item residue |
| descent V003 | `a03e836380cbbfa08d8763bf62d6104f70aec69ae484b3b69f63489a5ce1c68c` | `D_G`, kernel, restrictions, consumer boundary |
| extension V002 | `eb3675d525af7d1420c4ed033a5e5b94eb7494c1bac1305029b25ac9169567a0` | scoped `T^char` and `j_NM^Q` square |
| FIELD_SIGNATURE V005 / DoR-015 source | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | quotient and endpoint routes |
| network law V004 / DoR-016 source | `69f4d93b9f84075a3112fb011b9838f380fb8c0341610572170cf7a13d5aed08` | doubled endpoint access and prefix traces |
| transverse-action draft | `ed49624b6f5f0bcda94ee88a939a5751113b30d73192b2c28a5aec25829e1797` | `phi_div` signature and determination condition |
| Q-313 Map 1 | `ea8f4e9a79a9e4aca4a0b9e9aab470d78cd4d9c78794c20d9e979c0db16fbeab` | sealed `T^char` scope |
| Q-408 stationary package | sidecar PASS | formal 2PI placement |

Every available sidecar used in this adjudication passed.  No proposal was
read before its expected hash and sidecar matched.

### 0.3 Governing Q-359 resolution

Q-358 derives:

```text
ACTION_COMPARISON_CONSUMER_CLASS_IS_QUOTIENT_ONLY = true | TYPE-P |
  scope: phi_div and its declared action-comparison/2PI square

UNIVERSAL_PHYSICAL_SCALAR_CONSUMER_CLASS_IS_QUOTIENT_ONLY = false | TYPE-R
```

Q-359 sends the two-variant proposal to this lane with a specific
adjudication rule:

```text
Variant Q = candidate for phi_div by derivation;
Variant QE = lawful typing of other consumers, banked only;
the authored content must cover exactly the five-item residue.
```

There is no live route-selection question for the `phi_div` square.

---

## 1. Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| J1 forced-diagram containment | **KILL** | `B1-18a` forms the undefined composite `F_M o rho_f`; `D_G^*`, the complete Q-408 placement, and the full DoR-008 restriction obligations are not contained exactly. |
| J2 route resolution | **PASS** | Q-358 forces Variant Q for `phi_div`; banking QE for other consumers is compatible with no-selection and does not select by outcome. |
| J3 residue coverage | **KILL** | none of the five residue items is fully discharged; the algebraic-tensor comparison family and QE fields are extra to the forced Variant-Q residue. |
| J4 choice table and voids | **KILL** | A8 and A10 are accurate, but A3 is unforced and ill-typed in its naturality proof; A1/A6/A7/A9 belong only to the banked QE record. |
| J5 self-kill battery | **PASS** | the pendant, cycle-creating, and F7 witnesses are run at the correct carriers; the battery is genuinely adversarial, though not exhaustive. |
| J6 falsifier suite | **KILL** | the proposal says no finite check fails, but its finite restriction-square proof is itself a finitely checkable domain failure; the physical bottom-leg falsifier remains unrun. |
| J7 fresh attack | **KILL** | the retained zero member and full nonzero rescaling orbit make every member-sensitive Q-408 contribution non-invariant, so the family cannot yield a physical action result without the missing member/normalization rule. |

```text
PASS_ITEMS = J2,J5
KILL_ITEMS = J1,J3,J4,J6,J7
```

---

## 2. J1 - forced-diagram containment

### 2.1 The derived standard

The forced finite diagram is:

```text
DoR-016 doubled endpoint access
  -> DoR-009 every-prefix traces Tr_pref,N^009
  -> P_G^fam
  -> D_G
  -> Q_G.
```

For an already-instantiated quotient action functional
`f:Q_G->C`, the forced comparison is the canonical pullback

```text
D_G^*:Act_N^quot -> Fun(P_G^fam,C),
(D_G^*f)(Z)=f(D_G(Z)).                            (J1-1)
```

For a signed cellular restriction with

```text
P_f:P_M->P_N,
rho_f:Q_M->Q_N,
D_N P_f=rho_f D_M,
```

the forced naturality identity is

```text
D_M^* rho_f^* = P_f^* D_N^*,                     (J1-2)

rho_f^*(a_N)=a_N o rho_f,
P_f^*(b_N)=b_N o P_f.
```

This variance is not optional.  The coefficient being pulled back is a
function on the **codomain** `Q_N`, not a function on the domain `Q_M`.

### 2.2 Proposal's replacement square

The proposal instead introduces

```text
comp_G(y)(x)=sum_k F_(G,k)(y)b_(G,k)(x),
F_(G,k):Y_G->R,
b_(G,k) in Flat(S_G),
```

and states, for

```text
rho_f:Y_M->Y_N,
rho_f^Act:Act_M^basic(f)->Act_N,
```

the obligation

```text
rho_f^Act comp_M C_M = comp_N C_N P_f.            (J1-3)
```

Equation `(J1-3)` is a meaningful obligation if `comp_M` lands in the domain
of `rho_f^Act`.  The displayed proof is not meaningful.  It claims the
carrier pullback sends `F_M:Y_M->R` to

```text
F_M o rho_f.                                      (J1-4)
```

But `rho_f` has codomain `Y_N`, whereas `F_M` requires an argument in `Y_M`.
Therefore `(J1-4)` is undefined.  The lawful pullback is

```text
rho_f^*F_N = F_N o rho_f:Y_M->R,                  (J1-5)
```

and it begins with a **coarse** coefficient `F_N`, not `F_M`.

Consequently the proposal's line

```text
(F_M o rho_f) odot (rho_f^Act b_M)                (J1-6)
```

cannot be the value of either composite.  It neither proves compatibility
between `comp_M` and `comp_N` nor proves nonempty globally compatible
nonzero stage families.

There is a second domain gap.  The proposal defines
`rho_f^Act` only on `Act_M^basic(f)`, but does not prove that every value of
every `comp_M` lies in `Act_M^basic(f)`.  Defining `Comp` to include families
for which the square holds does not repair the missing typing; it merely
repeats the desired conclusion as a membership condition.

```text
B1_18A_TYPECHECK = FAIL | TYPE-R
B1_18_PROVED_BY_TENSOR_FUNCTORIALITY = false
```

### 2.3 Missing forced components

The proposal contains `D_G` as its physical leg and correctly confines
`T^char` to its proven scope.  It does not state the canonical operation
`D_G^*` at all.  Its `comp o D_G` can be interpreted as a vector-valued
precomposition only after a `comp` member exists; that is authored action
content, not a replacement for the already-forced scalar pullback.

The proposal also lists only

```text
D_C D_K phi,
D_C(delta phi),
```

whereas the derived Q-408 placement records the full conditional block
effect

```text
Delta H_CC = D_C^2 phi,
Delta H_CK = D_C D_K phi,
Delta H_KC = D_K D_C phi,
Delta H_KK = D_K^2 phi,
delta c_phi[psi]=-[D_C^2 Gamma_phi]^-1 D_C psi.    (J1-7)
```

Finally, the derived DoR-008 obligations name `rho_Gamma,N`, `rho_H,N`,
differentiation/restriction, the independent finite action bottom leg, and
the inverse/restriction theorem.  The proposal leaves these in open doors
without placing the complete obligations in the forced diagram.

```text
UPSTREAM_TRACE_LEG = PRESENT_IN_CARRIER_DESCRIPTION_BUT_NOT_EXPLICIT_MAP
D_G = PRESENT_AND_CORRECT
D_G_STAR = OMITTED
TCHAR_SCOPE = CORRECT
Q408_PLACEMENT = INCOMPLETE
DOR008_RESTRICTION_OBLIGATIONS = INCOMPLETE
J1 = KILL
```

---

## 3. J2 - route resolution without selection

The derived certificate resolves only this consumer:

```text
phi_div:X_phys or K_cycle -> scalar action correction.
```

Its domain contains cycle-quotient data and no endpoint vector, frame, or
open-path transport.  Therefore:

```text
PHI_DIV_ROUTE = Variant Q | forced by signature
VARIANT_SELECTED_BY_OUTCOME = false
```

DoR-016's endpoint-matched carrier remains essential upstream:

```text
(T_+,T_-)
  -> R_CTP=T_-^dagger T_+
  -> prefix traces
  -> D_G
  -> quotient action slot.
```

Variant QE is mathematically lawful for a different consumer whose signature
includes matching endpoint data.  Recording that type does not add it to the
`phi_div` square.

```text
VARIANT_Q = FORCED_FOR_THIS_SQUARE | TYPE-P
VARIANT_QE = BANKED_FOR_OTHER_CONSUMERS | NOT_ADOPTED_HERE
ROUTE_SELECTION_BY_OUTCOME = false
J2 = PASS
```

The merged candidate must consequently remove the two-route choice row A1
from the `phi_div` adoption surface.  A6, A7, and A9 remain useful banking
notes only.

---

## 4. J3 - one-to-one residue coverage

Q-358 leaves exactly five items.  The proposal's coverage is:

| Derived residue item | Proposal mapping | Adjudication |
|---|---|---|
| 1. divergence/action datum plus generated quotient action member | A2-A5 and AC-7 describe an admissible family and an open datum; no generated nonzero member or determining datum is supplied | **MISSING** |
| 2. completed-to-finite action restrictions `rho_Gamma,N` | B1-17 introduces a stage restriction only where already typed; AC-3 explicitly leaves `rho_Gamma,N` `TYPE-U` outside the basic class | **MISSING** |
| 3. independently instantiated finite physical action bottom leg | no object is constructed; the proposal correctly refuses source/action identification | **MISSING** |
| 4. scalar comparison equality plus normalization | B1-18 is the proposed equality, but its proof is ill-typed; A5 deliberately leaves normalization open | **MISSING** |
| 5. stationary physical 2PI package | B1-19 is only a formal interface; AC-4 explicitly leaves the blocks, inverse, and domain `TYPE-U` | **MISSING** |

The proposal itself confirms the absences:

```text
NORMALIZED_NONZERO_ACTION_MEMBER = NOT_SELECTED / TYPE-U
AC-3 rho_Gamma,N = TYPE-U outside finite basic class
AC-4 stationary/2PI package = TYPE-U
full off-section action value = TYPE-C
stationary/2PI image = TYPE-C
```

### 4.1 Extra authored content

The following content is not part of the five-item Variant-Q residue as
stated:

```text
1. A1's live {Q,QE} route family for phi_div;
2. A6/A7/A9's endpoint orbit, mixed QE comparison, and endpoint batching;
3. A3's algebraic-tensor comparison-family law;
4. A3's collective-separation membership requirement.
```

Items 1-2 may be banked for other consumers.  Items 3-4 require independent
justification.  The derive arm forced `D_G^*`; it did not force an
algebraic finite-rank tensor ansatz or require the complete action-member
family to separate every point of `Q_G`.

The collective-separation condition does not replace a physical action
member: an individual admitted member may still delete arbitrary carrier
coordinates, and downstream use is forbidden unless member-invariant.

```text
FIVE_ITEM_COVERAGE = 0 fully discharged / 5
UNJUSTIFIED_EXTRA = algebraic tensor ansatz plus collective separation
QE_CONTENT = bankable, not part of merged Variant-Q candidate
J3 = KILL
```

---

## 5. J4 - choice table and void conditions

### 5.1 Rows that survive

```text
A8 = PASS |
  upward action transport only on cycle-rank-preserving isomorphisms;
  no cycle-creating upward square.

A10 = PASS |
  member-dependent output may not be reported as physical without an
  invariance theorem or later member rule.

A4 = PASS_WITHIN_PROPOSAL |
  equal-history correction anchored to zero.
```

A8 states the V003/Z7 boundary at the right strength.  A10 carries the
family-level no-selection discipline honestly.

### 5.2 Rows that fail the merged-candidate audit

```text
A1 = REMOVE_FROM_PHI_DIV_CHOICE_TABLE |
  Variant Q is derived; QE is banking content.

A3 = KILL |
  the algebraic-tensor law is extra, its displayed naturality proof is
  ill-typed, and the claimed nonzero globally compatible family is not
  established on general noninvertible restrictions.

A5 = OPEN_RESIDUE, NOT DISCHARGE |
  it records rescaling freedom but supplies no normalization.

A6,A7,A9 = BANK_QE_ONLY |
  lawful but outside the forced phi_div consumer.
```

The family-size accounting is honest at an isolated stage.  It is not a
proof of the size or nonzero separation of the **globally compatible** family,
because the stage-to-stage construction is exactly where `(B1-18a)` fails.

```text
CHOICE_TABLE_MINIMAL_FOR_MERGED_Q = false
A8_EXACT = true
A10_EXACT = true
HONEST_ISOLATED_STAGE_SIZE = true
GLOBAL_FAMILY_SIZE_PROVED = false
J4 = KILL
```

---

## 6. J5 - self-kill battery

The requested hostile witnesses are at the correct carrier levels.

### 6.1 Pendant witness

For cycle characters equal to one and pendant character `w!=1`:

```text
D_G(Z)=1,
T_G^char(Z)=w.
```

Both variants use `D_G` for the cycle leg, so no pendant content is injected
into the physical cycle coordinate.  QE may retain endpoint-matched content
only in its distinct endpoint coordinate.

```text
PENDANT_WITNESS = PASS
```

### 6.2 Cycle-creating extension

Adding an identity edge that creates a cycle takes a point quotient to a
nontrivial quotient.  V003 proves no representative-independent upward map.
The proposal does not assert one and limits upward transport to rank-
preserving isomorphisms.

```text
CYCLE_CREATING_EXTENSION = PASS
```

The phrase "vertical new-cycle increments finite-tested independently" is a
future obligation, not an executed finite action test; this limitation is
carried into J6.

### 6.3 F7 one-edge endpoint witness

On a connected one-edge tree:

```text
Q_G={*},
D_G(Z)=*,
S_e([v_t,R_e,v_s])=<v_t,R_e v_s>.
```

Variant Q cannot distinguish endpoint tuples.  Variant QE retains the joint
orbit and may distinguish them without calling the edge a cycle.  This is the
correct split.

```text
F7_Q = EXCLUDED_BY_SIGNATURE
F7_QE = REPRESENTABLE_ON_BANKED_ENDPOINT_CARRIER
```

The target-tuning, normalization, contact/double-counting, batching,
nonemptiness, and source/action attacks are real attacks, not ceremonial
restatements.  They missed the variance defect, but an adversarial battery
need not be complete in order to be genuinely adversarial.

```text
SELF_KILL_BATTERY_GENUINELY_ADVERSARIAL = true
SPECIFIED_WITNESSES_AT_CORRECT_CARRIER = true
J5 = PASS
```

---

## 7. J6 - finite falsifier suite

### 7.1 Checks that recompute

```text
equal history: r_j=1, D_G=1, anchor phi=0                       PASS
pendant: D_G unchanged while T^char sees w                      PASS
S8-A: H_(c3)=Z_1 Z_2 Z_3^-1 survives and is conjugated/inverted PASS
reality: D_G(Theta Z)=Theta D_G(Z)                              PASS
batching: r_[a,b]=Z_(a-1)^-1 Z_b                               PASS
cycle-creating identity edge: no upward claim                  PASS
active-section flatness: every correction jet vanishes         PASS_BY_DEFINITION
```

These are carrier or active-jet checks.  They do not instantiate a finite
physical action bottom leg.

### 7.2 Finitely executable failure omitted by the board

The stage-restriction square is a finite typed claim, and its displayed
proof can be checked without any continuum machinery.  The type computation
is:

```text
rho_f:Y_M->Y_N,
F_M:Y_M->R,

F_M o rho_f = undefined.                               (J6-1)
```

Therefore the proposal's board entry

```text
contravariant restriction = PASS on finite typed carrier
```

does not extend to the authored action-comparison family.  Its account row
for `Comp_G^Q` cites B1-18 as though the restriction square had been proved.
It has not.

### 7.3 DoR-008 scope

`phi in Flat(S_G)` proves that adding the correction preserves all known
active-section jets.  It does **not** prove the completed-to-finite action
comparison required by DoR-008.  That test still needs:

```text
rho_Gamma,N;
an independent finite physical action bottom leg;
rho_H,N;
the reducing/inverse restriction theorem;
the physical stationary block system.
```

The proposal honestly marks the last rows `TYPE-C`, but the statement
"No finitely executable check fails" is false because `(J6-1)` already
fails at finite type-checking depth.

```text
DOR008_ACTIVE_JET_PRESERVATION = PASS_WITHIN_PROPOSAL
DOR008_PHYSICAL_ACTION_BOTTOM_LEG = NOT_EXECUTED
FINITE_ACTION_RESTRICTION_TYPECHECK = FAIL
J6 = KILL
```

---

## 8. J7 - fresh attack: family-invariance paralysis

This attack is not among the proposal's self-kills.

The proposal retains:

```text
0 in Comp^Q,
lambda comp in Comp^Q for every admitted nonzero scalar lambda,
```

and A10 allows a downstream result before member ratification only if it is
invariant across the member and normalization family.

For any nonzero action member `phi`, Q-408 gives linear Hessian shifts

```text
Delta H_AB[lambda phi]=lambda Delta H_AB[phi]       (J7-1)
```

for `AB in {CC,CK,KC,KK}`.  Comparing with the zero member gives

```text
Delta H_AB[0]=0.                                   (J7-2)
```

If a Q-408 contribution is invariant across the retained family, then from
`(J7-1)` and `(J7-2)` it must vanish.  The same point applies to every
member-sensitive scalar action value.  Therefore the family-level proposal
can support only:

```text
1. claims independent of the transverse action; or
2. claims made after the missing member/normalization rule is supplied.
```

This is not a reason to select a member.  It is a proof that the proposed
family does not discharge residue item 1 or make the stationary action square
executable.  Collective separation by the **set of all members** is irrelevant
to a physical output that must be invariant across those same members.

```text
FAMILY_COLLECTIVELY_SEPARATING = insufficient for a physical member
FAMILY_INVARIANT_NONZERO_LINEAR_2PI_SHIFT = impossible
ACTION_MEMBER_OR_NORMALIZER_STILL_REQUIRED = true
J7 = KILL
```

---

## 9. Merged-candidate statement

No adoption is made here.  The only lawful merged candidate presently
available is a repair specification.

### 9.1 Forced diagram to carry verbatim

```text
H_N^CTP
  | Tr_pref,N^009
  v
P_G^fam ---------------- D_G ----------------> Q_G
  |                                            |
  | D_G^*f = f o D_G                          | f in Act_N^quot
  v                                            v
C ---------------------- identity -----------> C.
```

For every declared signed cellular restriction:

```text
D_N P_f = rho_f D_M,
D_M^* rho_f^* = P_f^* D_N^*.
```

`T^char` remains confined to the sealed square and
`im(j_NM^Q)`.  The Q-408 block formulas `(J1-7)` and the complete DoR-008
restriction obligations must be carried as conditional forced structure.

### 9.2 Variant resolution

```text
Variant Q = forced for phi_div and its action-comparison/2PI square.
Variant QE = lawful endpoint-consumer typing, banked for future use.
No route choice appears in the DoR-017 candidate.
```

### 9.3 Authored content still required

The repaired candidate must supply, one-to-one and without extras:

```text
R1. a divergence/action datum and generated quotient action member,
    with any residual family and normalization freedom disclosed;

R2. completed-to-finite physical action restrictions rho_Gamma,N;

R3. an independently instantiated finite physical action bottom leg;

R4. the scalar comparison equality against D_G^* rho_Gamma,N,
    including units and normalization;

R5. the stationary physical 2PI package: A/G tangent, blocks,
    complement inverse, rho_H,N, and restriction/inverse theorem.
```

The algebraic tensor ansatz may return only if separately justified and
correctly typed.  It is not the canonical comparison operation and cannot
replace `D_G^*`.

### 9.4 Standing falsifiers for the repair

```text
1. the pendant witness must keep w out of the cycle leg;
2. no cycle-creating upward map may be asserted;
3. the one-edge endpoint witness must remain outside phi_div's arguments;
4. every restriction square must type-check before it is evaluated;
5. the finite physical bottom leg must be independent of the source log;
6. Q-243/Q-279 shadows must be reproduced exactly;
7. no member, normalization, rank, frame, orientation, filtration,
   realization, cycle basis, or endpoint tuple may be selected by outcome.
```

```text
VARIANT_Q_FORCED_DIAGRAM = PRESERVED_AS_REPAIR_BASE
VARIANT_Q_AUTHORED_CONTENT = INCOMPLETE
VARIANT_QE_BANKING_NOTE = PRESERVED_NOT_ADOPTED

MERGED_CANDIDATE = NOT_READY (J1,J3,J4,J6,J7)
READY_FOR_DOR017_RULING = no

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No alpha, `K_*`, root, physical response value, rank ratio, or measured
constant was evaluated.  No register, plan, tracker, git, commit, or push
action was performed.
