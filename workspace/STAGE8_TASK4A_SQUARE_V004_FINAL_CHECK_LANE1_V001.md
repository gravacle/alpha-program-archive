# STAGE8 TASK 4A: SQUARE V004 FINAL CHECK - LANE 1 V001

Date: 2026-08-03  
Task: PASTE 448 / Task 4a / final bounded square V004 check  
Lane: CODEX LANE 1  
Register head at preflight: Q-365  
Custody: bounded adversarial confirmation; this artifact adopts nothing  
Reserved ruling: DoR-017

```text
LEAD_RESULT = THE_RHO_H_N_CUBE_CLOSES

Q1_RHO_H_N_NATURALITY_CUBE = PASS
Q2_S8A_RANK_TWO_EXCHANGE = PASS
Q3_STATIONARY_PROPAGATION = PASS
Q4_BOUNDED_DELTA_AND_BATTERY = PASS

MERGED_CANDIDATE = READY
READY_FOR_DOR017_RULING = yes

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

V004 supplies the one certificate missing from V003.  On exactly the
R5-generated Hessian class, the signed/semilinear realization action
commutes with finite Hessian restriction.  The same intertwining carries the
reducing inverse, Schur complement, and retarded extraction.  The arbitrary
external-Hessian class remains outside the claim, consistently with the
original R2/R5 signature.

---

## 0. Preflight and scope

### 0.1 Locked process and register

`alpha_supervision/LOCKED_PROCESS.md` was read in full and its local sidecar
verified.  The live questions-settled register and its local sidecar verified
before V004 was read.  Its head was exactly Q-365.

```text
DOES_THE_OBJECT_EXIST = yes | square proposal V004
IS_THE_VERSION_CURRENT = yes | Q-365
ARE_ITS_INPUTS_PRESENT = yes | V004 plus the Q-364 bounded review standard
PREFLIGHT = PASS
```

### 0.2 Hash-verified authorities

| Authority | Verified SHA-256 | Use |
|---|---|---|
| square proposal V004 | `abf6d366a5a7e375b9b53df75402f35d37f7c6a4b1bb0b10a44309ad3b0e1912` | object under review |
| Q-364 V003 re-adjudication | `3f02fd6451b1a14748902df7ee3c12912d9153908e4a862ebcf501d552db6419` | sole open cube and bounded repair standard |
| square proposal V003 | `21d4085d84b2653740e26025c08948824a2fc61d30a38f12dd1083d0e0163e23` | direct delta base |

The supplied V004 hash matched before reading.  Every sidecar used here
passed.

### 0.3 Exact scope

```text
H_AB,G = D_A D_B Gamma_G for Gamma in the proposed R2/R5 action class;
rho_H,N(D^2 Gamma) = D^2(rho_Gamma,N Gamma);
AB in {CC,CK,KC,KK}.

Claimed class     = R5-generated Hessians on D_017;
unclaimed class   = arbitrary externally supplied Hessians;
selected member  = none.
```

That scope is the one requested by Q1.  No broader Hessian extension is
needed to close this proposal.

---

## 1. Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| Q1 `rho_H,N` cube | **PASS** | the completed action is first proved covariant from R2 zero-tail determinacy; differentiation gives all four block intertwiners, and the chain rule gives the missing `rho_H,N` naturality equation and commuting cube. |
| Q2 S8-A exchange | **PASS** | the signed exchange matrix preserves the rank-two relation and both restriction paths equal `S_sigma,N rho_H,N(H) S_sigma,N^(-1)`, with conjugation added on reversal. |
| Q3 stationary propagation | **PASS** | covariance transports the critical family and reducing support; uniqueness transports the two-sided inverse, direct substitution transports the Schur block, and sealed Keldysh/E_post covariance transports retarded extraction. |
| Q4 delta and battery | **PASS** | the mathematical delta is confined to O1/O2; remaining changes are metadata and exact ledger/battery propagation, with no selection or new live authored object. |

```text
PASS_ITEMS = Q1,Q2,Q3,Q4
KILL_ITEMS = none
```

---

## 2. Q1 - the completed Hessian restriction cube

### 2.1 Carrier action and reality

For every admitted realization arrow `alpha:G->G'`, V004 uses

```text
alpha_D = alpha_C direct-sum alpha_K,
kappa_alpha = id                         for signed relabelings/exchanges,
kappa_alpha = complex conjugation        for reality/orientation reversal.
```

On the finite cylinder core, `alpha_C` and `alpha_K` are signed
permutation/relabeling isometries.  Therefore they extend uniquely to the
full P2-completed carrier and obey

```text
rho_A,N,(G') alpha_A = alpha_A,N rho_A,N,G,
A in {C,K}.                                           (Q1-1)
```

The induced transport on an A-sector Hessian covector is

```text
(alpha_H,A ell)(u')
  = kappa_alpha(ell(alpha_A^(-1)u')),

(alpha_H,A,N ell_N)(u_N')
  = kappa_alpha(ell_N(alpha_A,N^(-1)u_N')).           (Q1-2)
```

This is the correct dual transport.  A signed exchange is linear; an
orientation reversal is semilinear and conjugates coefficients while also
carrying the cycle sign.  Thus `H_(-c)=conjugate(H_c)` is preserved rather
than replaced by an orientation-independent equality.

### 2.2 Completed action and block covariance

Define on the full completed carrier

```text
Delta_alpha
  = Gamma_(G') compose alpha_D
    - kappa_alpha compose Gamma_G.
```

Every finite restriction of `Delta_alpha` is zero by finite R1-COV and
`rho_Gamma,N` naturality.  R2's action class has zero common
finite-restriction tail, so

```text
Delta_alpha = 0.                                    (Q1-3)
```

Twice differentiating in the declared real/reality-covariant P2 calculus
gives, for `A,B in {C,K}`,

```text
D_A D_B Gamma_(G')(alpha_A u,alpha_B v)
  = kappa_alpha(D_A D_B Gamma_G(u,v)),

H_AB,(G') alpha_B = alpha_H,A H_AB,G.               (Q1-4)
```

This covers `CC`, `CK`, `KC`, and `KK`.  Because the signed carrier maps are
bounded isometries and `(Q1-4)` holds on the common core, graph closure maps
the transported maximal graph domains bijectively.  Their common
intersection is therefore carried from `D_017,G` to `D_017,G'`.

The apparent ordering hazard in V004 is harmless when the proof is read in
this order: `alpha_D` first acts on the full P2 carrier; `(Q1-3)` is proved
there; `(Q1-4)` is then established on the core; graph-domain invariance is
a conclusion.  No domain invariance is used to derive itself.

### 2.3 Restriction naturality

On the generated class,

```text
rho_H,N(D^2 Gamma) := D^2(rho_Gamma,N Gamma).
```

Using `(Q1-2)`, the chain rule, and action-restriction naturality gives

```text
rho_H,N,(G') alpha_H,A(D^2 Gamma_G)
  = D^2[rho_Gamma,N,(G')(alpha_Act Gamma_G)]
  = D^2[alpha_Act,N(rho_Gamma,N,G Gamma_G)]
  = alpha_H,A,N rho_H,N,G(D^2 Gamma_G).             (Q1-5)
```

Hence

```text
rho_H,N,(G') alpha_H,A
  = alpha_H,A,N rho_H,N,G                           (Q1-6)
```

on every R5-generated Hessian.

### 2.4 The cube

Combining block covariance, domain restriction naturality, finite bottom
covariance, and R5-3 gives the same composite by every route:

```text
rho_H,N,(G') H_AB,(G') alpha_B
  = H_AB,(G'),N rho_B,N,(G') alpha_B
  = H_AB,(G'),N alpha_B,N rho_B,N,G
  = alpha_H,A,N H_AB,G,N rho_B,N,G
  = alpha_H,A,N rho_H,N,G H_AB,G.                  (Q1-CUBE)
```

Every map is typed:

```text
alpha_B      : D_B,G -> D_B,G';
H_AB,G       : D_B,G -> D_A,G^*;
alpha_H,A    : D_A,G^* -> D_A,G'^*;
rho_B,N,G    : D_B,G -> D_B,G,N;
rho_H,N,G    : D_A,G^* -> D_A,G,N^*.
```

```text
SIGN_AND_CONJUGATION = PASS
ALL_FOUR_BLOCKS = PASS
RHO_H_NATURALITY = PASS
R5_RESTRICTION_CUBE = PASS
Q1 = PASS
```

---

## 3. Q2 - S8-A rank-two exchange

### 3.1 Relation and signed action

At S8-A,

```text
H_(c_1)=Z_2,
H_(c_2)=Z_1^(-1) Z_3,
H_(c_3)=Z_1 Z_2 Z_3^(-1)=H_(c_1)H_(c_2)^(-1).
```

Thus the rank-two logarithmic relation is `q_3=q_1-q_2`.  The admitted
exchange

```text
sigma(c_1)=c_2,
sigma(c_2)=c_1,
sigma(c_3)=-c_3
```

acts by

```text
S_sigma = [[0,1,0],
           [1,0,0],
           [0,0,-1]],
S_sigma^(-1)=S_sigma.
```

It preserves the relation because

```text
q_3'=-q_3=q_2-q_1=q_1'-q_2'.
```

No basis or orientation member is selected by using this admitted
automorphism.

### 3.2 Both paths

For a Hessian bilinear form on the relation subspace,

```text
H_(G') = S_sigma H_G S_sigma^(-1).                 (Q2-1)
```

In the displayed character coordinates this sends

```text
h_11 -> h_22,     h_12 -> h_21,
h_13 -> -h_23,    h_31 -> -h_32,
h_33 -> h_33.
```

The equality is basis-free on the rank-two relation subspace; the 3-by-3
display merely exposes the sign.  Since finite restriction commutes with
the signed permutation,

```text
left
 = rho_H,N,(G')(S_sigma H_G S_sigma^(-1))
 = S_sigma,N [rho_H,N,G(H_G)] S_sigma,N^(-1),

right
 = alpha_H,N rho_H,N,G(H_G)
 = S_sigma,N [rho_H,N,G(H_G)] S_sigma,N^(-1).       (Q2-2)
```

The two sides agree entry by entry and on the constrained subspace.  For the
reality/orientation reversal, both expressions become

```text
S_sigma,N conjugate(rho_H,N,G(H_G)) S_sigma,N^(-1).
```

```text
S8A_RELATION_PRESERVED = true
S8A_LEFT_EQUALS_RIGHT = true
S8A_SIGN_VISIBLE = true
S8A_CONJUGATION_COMMUTES_WITH_RESTRICTION = true
Q2 = PASS
```

---

## 4. Q3 - inverse, Schur, and retarded propagation

### 4.1 Critical family and reducing support

Gradient covariance maps `Crit_m,G` to `Crit_m,G'`.  Therefore the
stationary object is transported as the full unselected family:

```text
G_star,(G') = alpha_D G_star,G.
```

If `C_red,G` reduces `H_CC,G`, block covariance makes

```text
C_red,(G') := alpha_C C_red,G
```

a reducing support for `H_CC,G'`.  A support moved by a stabilizer is
excluded from closing fixed-member mode and retained only as a nonclosing
orbit.  No complement is chosen silently.

### 4.2 Inverse

From

```text
H_CC,(G') alpha_C = alpha_H,C H_CC,G
```

and uniqueness of the declared two-sided inverse on the transported
reducing support,

```text
Inv_CC,(G') alpha_H,C = alpha_C Inv_CC,G.           (Q3-1)
```

The inverse remains complement-scoped; no cycle direction is inverted.

### 4.3 Schur block

Substitute all four block intertwiners and `(Q3-1)` into

```text
Schur_G = H_KK,G-H_KC,G Inv_CC,G H_CK,G.
```

Then

```text
Schur_(G') alpha_K = alpha_H,K Schur_G.             (Q3-2)
```

There is no leftover sign or conjugation factor: it is already carried by
`alpha_K` and `alpha_H,K`.

### 4.4 Retarded extraction and finite stages

The sealed Keldysh rotation commutes with simultaneous branch relabeling,
and the E_post order obeys the ratified conjugation law under reversal.
Therefore

```text
RetExtract_(G')(
  alpha_H,K Schur_G alpha_K^(-1))
  = alpha_R(RetExtract_G(Schur_G)).                 (Q3-3)
```

Composing `(Q3-1)` through `(Q3-3)` with Q1-6 and R5-3 gives the same
identities after every finite restriction.

### 4.5 External-Hessian boundary

V004 states

```text
RHO_H_NATURALITY_DOMAIN = R5_generated_Hessians_on_D_017
ARBITRARY_EXTERNAL_HESSIAN_NATURALITY = not_claimed.
```

This is honest and does not narrow a prior live certificate.  R2-2 already
defines `rho_H,N` by differentiating a restricted action, and R5's blocks
are the derivatives of `Gamma_phi`.  An independent external Hessian was
never one of R1-R5's five live residue objects.

```text
CRITICAL_FAMILY_COVARIANCE = PASS
INVERSE_COVARIANCE = PASS
SCHUR_COVARIANCE = PASS
RETARDED_EXTRACTION_COVARIANCE = PASS
EXTERNAL_HESSIAN_BOUNDARY = HONEST
Q3 = PASS
```

---

## 5. Q4 - bounded delta, battery, and no selection

### 5.1 Direct delta

A direct unified diff of V003 against V004 reports one file changed, with
293 insertions and 22 deletions.  Every mathematical change belongs to the
requested O1/O2 repair:

```text
O1: completed and finite carrier transports;
O1: completed action and four-block Hessian covariance;
O1: rho_H,N naturality and the commuting cube;
O1: critical/inverse/Schur/retarded propagation;
O1: exact R5-generated-class boundary;
O2: S8-A signed exchange and conjugation exercise.
```

The other changed lines are metadata, cross-references, battery rows,
door/account updates, and the V003-to-V004 delta table required to propagate
those proofs.  No prior P2/P4 content changes, no sixth live object appears,
and no V001 comparison family returns.

### 5.2 Battery and no-selection scan

The completed cube attack now passes by Q1-CUBE.  The stationary propagation
attack passes by Q3-1 through Q3-3.  Pendant, cycle-creating, one-edge,
rank-two member, reality, batching, zero-extension, and physical bottom-leg
regressions remain unchanged.

The finite Hessian action is induced by the signed realization map; it is not
selected.  The reducing support is required to form a covariant family.
No member, normalizer, rank, ratio, orientation, frame, filtration,
realization, cycle basis, endpoint tuple, measure, contour, response value,
or target outcome is selected.

```text
MATHEMATICAL_DELTA = O1,O2_only
BOOKKEEPING_PROPAGATION = complete
NEW_LIVE_AUTHORED_OBJECT = none
BATTERY = PASS
NO_SELECTION_SCAN = PASS
Q4 = PASS
```

---

## 6. Final standing

The Q-364 hold is discharged.  V004 proves the requested cube on the exact
class its stationary package consumes, exercises it on the rank-two signed
exchange, and propagates it through every R5 stationary operation.  No
member of the remaining DoR-017 fiber is selected by this review.

```text
Q1_RHO_H_N_NATURALITY_CUBE = PASS
Q2_S8A_RANK_TWO_EXCHANGE = PASS
Q3_INVERSE_SCHUR_RETARDED_PROPAGATION = PASS
Q4_DELTA_BATTERY_NO_SELECTION = PASS

MERGED_CANDIDATE = READY
READY_FOR_DOR017_RULING = yes

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No alpha, `K_*`, root, physical response value, rank ratio, or measured
constant was evaluated.  No register, plan, tracker, git, commit, or push
action was performed.  No structural result was fence-blocked.
