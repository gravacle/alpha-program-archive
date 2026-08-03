# STAGE8 TASK 4A: SQUARE V003 FINAL RE-ADJUDICATION - LANE 1 V001

Date: 2026-08-03  
Task: PASTE 446 / Task 4a / final square V003 re-adjudication  
Lane: CODEX LANE 1  
Register head at preflight: Q-363  
Custody: bounded adversarial review; this artifact adopts nothing  
Reserved ruling: DoR-017

```text
LEAD_RESULT = NOT_READY_ON_ONE_BOUNDED_COVARIANCE_GAP

THE_RANK_TWO_KILL_IS_REPAIRED = true
R1_MEMBER_GENERATOR_NORMALIZER_BOTTOM_COVARIANCE = PASS
ORIENTATION_SIGN_ACTION = PASS

KILLING_GAP =
  R1-COV covaries the finite bottom Hessian and rho_Gamma, while R5
  separately supplies rho_H,N for the completed Hessian.  V003 never
  defines the completed Hessian automorphism action or proves that rho_H,N
  intertwines it.  The claimed composition of automorphism covariance with
  the R5 restriction square is therefore absent.

MERGED_CANDIDATE = NOT_READY (P1,P3,P5)
READY_FOR_DOR017_RULING = no

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

V003 correctly excludes the rank-two cycle-selective witness that killed
V002, and its live R1 member fiber is now realization-covariant.  The bounded
repair does not yet reach the completed R5 response package which alternatives
Z and N purport to close.  A narrative ledger entry saying "automorphism
intertwining" cannot replace the missing typed square.

---

## 0. Preflight and authorities

### 0.1 Locked process and register

`alpha_supervision/LOCKED_PROCESS.md` was read in full and its sidecar
verified.  The questions-settled register sidecar verified before V003 was
read.  Its head was exactly Q-363.

```text
DOES_THE_OBJECT_EXIST = yes | square proposal V003
IS_THE_VERSION_CURRENT = yes | Q-363
ARE_ITS_INPUTS_PRESENT = yes for bounded review |
  no for the missing completed-Hessian covariance/restriction cube
PREFLIGHT = PASS
```

### 0.2 Hash-verified objects

| Authority | Verified SHA-256 | Use |
|---|---|---|
| square proposal V003 | `21d4085d84b2653740e26025c08948824a2fc61d30a38f12dd1083d0e0163e23` | object under review |
| Q-362 re-adjudication | `8629dd235a7ea072862381c9ba09128a3dd1fe650ec03ff5af900f7c54660c62` | M6/M7 kills and rank-two witness |
| Q-360 adjudication | `9521e9970704beca8818389df972e099dc1d2f7cd1c0c5b1254dd09fb25c9364` | forced diagram and earlier review standard |
| square proposal V002 | `5b4229fd4ba5cc5d8180a91a923c6293c95d71b929f003626363603803a6a30c` | bounded-delta base |

The V003 hash matched before reading.  Every sidecar used here passed.

### 0.3 Review scope

```text
P1 = R1-COV across the complete claimed package
P2 = permanent rank-two witness
P3 = Z/N/F/reject fiber
P4 = bounded V002-to-V003 delta
P5 = battery, no-selection, and a fresh attack
```

No member of `M_017`, rank, ratio, orientation, frame, filtration, cycle
basis, or response value is selected in this review.

---

## 1. Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| P1 R1-COV | **KILL** | Member, generator, normalizer, bottom-leg, finite-Hessian, sign, and `rho_Gamma` covariance are stated, but the completed R5 Hessian and its `rho_H,N` restriction square have no automorphism action or naturality equation. |
| P2 rank-two witness | **PASS** | the `c_1`-selective member is carried to the distinct `c_2` member by the admitted exchange and therefore fails fixed-member naturality exactly as required. |
| P3 fiber restatement | **KILL** | Z/N/F/reject and non-recommendation are correct at R1, but N is called fully certified and closing while its adopted R5 package lacks the P1 covariance/restriction certificate. |
| P4 verbatim carry | **PASS** | the diff is bounded to metadata plus the M6/M7 covariance repair, witness, fiber, battery, and ledger propagation; the previously confirmed M1-M5 equations remain present. |
| P5 battery and fresh attack | **KILL** | the selection scan otherwise passes, but the fresh completed-Hessian restriction-cube attack finds the same unproved propagation hidden behind the R5 ledger claim. |

```text
PASS_ITEMS = P2,P4
KILL_ITEMS = P1,P3,P5
```

---

## 2. P1 - R1-COV under full-package typing

### 2.1 What V003 proves

For an admitted signed-realization arrow `alpha:G->G'`, V003 defines

```text
alpha_Act(phi_G) = phi_G compose alpha_Q^(-1).
```

Its displayed `(R1-COV)` then supplies:

```text
Gen_(G',m)(alpha_Div delta_(G,m))
  = alpha_Act Gen_(G,m)(delta_(G,m));

phi_(G',m) compose alpha_Q = phi_(G,m);

Norm_(G',m)(alpha_Act phi_(G,m))
  = Norm_(G,m)(phi_(G,m)) = nu_m;

I_(G',m)^bot compose alpha_Ref
  = alpha_Jet compose I_(G,m)^bot;

Gamma_base,(G',m)^bot compose alpha_Q
  = Gamma_base,(G,m)^bot;

b_(G',m)^bot compose alpha_Q = b_(G,m)^bot;

H_(G',m)^bot alpha_D = alpha_D H_(G,m)^bot;

rho_Gamma,(G') alpha_Act
  = alpha_Act,fin rho_Gamma,G.
```

Those equations are sufficient for the repaired R1 member, generator,
normalizer, finite reference/bottom legs, finite bottom Hessian, and action
restriction.  They also exclude a member tied to a bare cycle label.

### 2.2 Sign action

V003 does not erase orientation.  It states

```text
alpha_* c = -c,
H_(-c) = conjugate(H_c)
```

for an orientation reversal.  Thus an orientation reversal transports the
character to its conjugate.  It is not replaced by equality at fixed oriented
representative.

```text
ORIENTATION_SIGN_ACTION = PASS
```

### 2.3 The missing composition square

R5 introduces a different restriction carrier:

```text
rho_H,N H_AB = H_AB,N rho_D,N,
AB in {CC,CK,KC,KK}.                              (R5-3)
```

This concerns the completed Hessian blocks and completed domain, not the R3
finite bottom Hessian `H^bot`.  To compose R1-COV with R5-3, the package needs
typed automorphism actions and the following commuting data (equivalent
notation is acceptable):

```text
alpha_D      : D_G -> D_(G'),
alpha_H      : H_G -> H_(G'),
alpha_D,N    : D_G,N -> D_(G'),N,
alpha_H,N    : H_G,N -> H_(G'),N;

H_AB,(G') alpha_D = alpha_H H_AB,G;

rho_D,N,(G') alpha_D = alpha_D,N rho_D,N,G;
rho_H,N,(G') alpha_H = alpha_H,N rho_H,N,G;

H_AB,(G'),N alpha_D,N = alpha_H,N H_AB,G,N.
```

Then both paths around the required cube agree:

```text
rho_H,N,(G') H_AB,(G') alpha_D
  = H_AB,(G'),N rho_D,N,(G') alpha_D
  = H_AB,(G'),N alpha_D,N rho_D,N,G
  = alpha_H,N H_AB,G,N rho_D,N,G
  = alpha_H,N rho_H,N,G H_AB,G.
```

V003 contains no `alpha_H`, no naturality equation for `rho_H,N`, and no
completed-Hessian covariance equation.  `(R1-COV)` ends with `rho_Gamma`.
`(R5-3)` supplies only stage restriction.  The six-account row later says
"`(R5-3)` and automorphism intertwining," but no such R5 intertwiner has been
defined or proved.

The omission is load-bearing because the square's closing alternatives adopt
R5 as the selected member's stationary package.  The finite bottom-Hessian
equation cannot be silently substituted for the completed R5 equation.

```text
COMPLETED_HESSIAN_AUTOMORPHISM_ACTION = absent
RHO_H_AUTOMORPHISM_NATURALITY = absent
R5_RESTRICTION_CUBE = unproved | TYPE-U
P1 = KILL
```

This is a bounded typing repair.  It does not refute the finite bottom
covariance already proved, and it does not reopen M1-M5.

---

## 3. P2 - rank-two witness

At the admitted rank-two stage, let

```text
sigma(c_1)=c_2,
sigma(c_2)=c_1,
sigma(c_3)=-c_3,

phi_(c_1)(q,t)=g(t)(Re H_(c_1)(q)-1),
g(t)=exp(-1/t^2) for t!=0, g(0)=0.
```

The induced action gives

```text
[alpha_Act phi_(c_1)](q,t)
  = phi_(c_1)(alpha_Q^(-1)q,t)
  = g(t)(Re H_(c_2)(q)-1)
  = phi_(c_2)(q,t).
```

Surjectivity of the rank-two quotient provides separated points with

```text
Re H_(c_1)(q) != Re H_(c_2)(q).
```

Hence

```text
alpha_Act phi_(c_1) != phi_(c_1).
```

The fixed `c_1` member fails natural-section covariance and is excluded from
alternative N.  Its full automorphism orbit can only remain in the unselected,
nonclosing F record.  This exactly meets the Q-362 witness.

```text
RANK_TWO_C1_SELECTIVE_MEMBER_IN_N = false
RANK_TWO_ORBIT_CONFINED_TO_F = true
P2 = PASS
```

---

## 4. P3 - the DoR-017 fiber

### 4.1 R1-level classification

The four rows are honest at the R1 level:

| Alternative | Check | Result |
|---|---|---|
| Z | `0_(G') compose alpha_Q=0_G`; zero generator, normalizer, and transverse bottom correction remain zero | PASS |
| N | only one nonzero natural section satisfying R1-COV may be chosen | PASS at R1 |
| F | complete automorphism-covariant orbit/fiber, no member selected and no member-sensitive output | PASS as nonclosing record |
| reject | no R1/R4 member; forced map survives and action square remains open | PASS |

No row is recommended, and no member of `M_017` is selected.

### 4.2 Closing overclaim

Alternative N is described as "one fully certified" member which closes the
square and then adopts R2 and R5 as its restriction/stationary package.  That
statement reaches beyond the R1-level table: R5 still lacks the completed
Hessian covariance/restriction cube from P1.

The exact lawful status is therefore:

```text
Z = R1-covariant; full R5 closure pending P1 repair;
N = R1-covariant natural member; full R5 closure pending P1 repair;
F = covariant unselected family, nonclosing;
reject = unchanged.
```

```text
FIBER_FOUR_ROWS = correctly_partitioned
NONE_RECOMMENDED = true
N_FULLY_CERTIFIED = false_as_written
P3 = KILL | inherited bounded P1 gap
```

---

## 5. P4 - bounded delta and verbatim carry

A direct unified diff of V002 against V003 reports one file changed, with
234 insertions and 33 deletions.  The changes fall into the disclosed bounded
classes:

```text
1. metadata, Q-362 preflight, and custody;
2. R1-COV and the covariant R1 fiber;
3. R4 covariance stability;
4. Z/N/F/reject covariance wording;
5. the rank-two permanent witness;
6. battery and no-selection additions;
7. delta, ledger, and final-board propagation.
```

The forced diagram, corrected contravariance, `D_G^*`, Q-408 placement,
five-residue architecture, physical bottom-leg falsifier, QE banking, A8,
A10, and the K5 non-derivability chain all remain present.  No old killed
algebraic-tensor machinery returns.  The extra R4 and ledger lines are listed
in V003's bounded-delta table rather than hidden as byte-identical content.

```text
DELTA_TRACES_TO_M6_M7 = true
M1_TO_M5_CORE_PRESERVED = true
SILENT_NONCOVARIANCE_CHANGE = false
P4 = PASS
```

P4 does not cure P1: the ledger's unsupported R5 covariance phrase is itself
part of the disclosed propagation and must still be proved.

---

## 6. P5 - battery, no-selection, and fresh attack

### 6.1 Selection and target scan

The V003 construction selects no member, normalizer, rank, ratio, orientation,
frame, filtration, realization, cycle basis, endpoint tuple, response value,
or target outcome.  Variant Q remains forced by the quotient-only signature;
QE remains banked.  `p` is not evaluated.  All live authored fields remain
`PROPOSED_NOT_ADOPTED`.

```text
NO_SELECTION_SCAN = PASS
TARGET_AWARENESS_SCAN = PASS
GATES = clean
```

### 6.2 Fresh attack: the completed-Hessian restriction cube

This attack is not in V003's six self-attacks or permanent-witness table.
Take an admitted realization automorphism `alpha:G->G'`, a completed domain
vector `v in D_G`, and a stage N.  The two lawful ways to reach the finite
Hessian carrier should be

```text
Path A:
v -> alpha_D v -> H_AB,(G') alpha_D v
  -> rho_H,N,(G') H_AB,(G') alpha_D v;

Path B:
v -> H_AB,G v -> alpha_H H_AB,G v
  -> rho_H,N,(G') alpha_H H_AB,G v.
```

R5-3 determines the restriction part of Path A, but V003 provides neither
`alpha_H` nor the naturality law needed to compare the result with Path B.
The missing map also prevents a proof that `Inv_CC`, `Schur_m`, and
`RetExtract_m` are realization-natural after restriction.  Nothing in the
finite rank-two witness tests this completed package.

This is not a counterexample to the intended covariance law; it is a failed
construction of the law on a carrier V003 claims to certify.  It therefore
returns `TYPE-U`, which is fatal to readiness but calls for a bounded repair,
not a rebuild.

```text
FRESH_ATTACK = completed_Hessian_restriction_cube
ATTACK_OUTCOME = KILL | missing typed map and commuting proof
BATTERY_COMPLETE_AS_STATED = false
P5 = KILL
```

---

## 7. Bounded repair and final standing

The repair is limited to R5 and its propagation.  For every admitted
`alpha:G->G'`, V004 must:

```text
1. type the completed domain and Hessian actions alpha_D and alpha_H;
2. prove completed block covariance for CC, CK, KC, and KK;
3. prove rho_D,N and rho_H,N natural under alpha;
4. exhibit the commuting covariance/restriction cube;
5. carry the theorem through the reducing inverse, Schur block, and
   retarded extraction on their declared complement-scoped domains;
6. replace the unsupported R5 ledger phrase with citations to those equations.
```

No change is required to the rank-two exclusion, R1 member fiber, forced
diagram, five-residue accounting, or K5 non-derivability result.

```text
P1_R1_COV_FULL_PACKAGE = KILL | completed R5 cube absent
P2_RANK_TWO_WITNESS = PASS
P3_FIBER_RESTATEMENT = KILL | N/Z closure overclaims P1
P4_VERBATIM_CARRY = PASS
P5_BATTERY_FRESH_ATTACK = KILL | same bounded R5 propagation gap

MERGED_CANDIDATE = NOT_READY (P1,P3,P5)
READY_FOR_DOR017_RULING = no

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No alpha, `K_*`, root, physical response value, rank ratio, or measured
constant was evaluated.  No register, plan, tracker, git, commit, or push
action was performed.  No structural result was fence-blocked.
