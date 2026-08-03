# Stage 8 Task 4a C5 External-History to Mutual-Sourcing Drive Derivation Arm — Lane 1 V001

Date: 2026-08-03  
Lane: CODEX LANE 1  
Task: PASTE 417 / Task 4a / drive race, derivation arm  
Register head checked at freeze: Q-334  
Plan head checked at freeze: C44  
Status: **THE PROPOSED INVERSION OF C5 IS REFUTED. C5 DERIVES A RECEIVER-SIDE MAP FROM AN ALREADY-SUPPLIED EXTERNAL U(1) HISTORY TO THE CHARGED WRITE. ON THE DOUBLED FINITE CORE, THAT RECEIVE CLASS HAS A LOCAL `J`-PORT REPRESENTATION. C5 CONTAINS NO BILOCAL `R` DATUM AND NO ARROW FROM A NEIGHBOR'S RECORD OR HISTORY INTO EITHER V007 PORT. A RESPONSE MAP `r:X->Y` DOES NOT INDUCE AN EMISSION MAP `e:H->X`; MULTIPLE INEQUIVALENT EDGE FEEDS COMPOSE WITH THE SAME C5 LAW. RECIPROCITY IS THEREFORE NOT FORCED. THE EXACT TWO-SYSTEM TOWER EXISTS ONLY CONDITIONALLY ON TWO UNBUILT DIRECTED EDGE MAPS. AT THE MAXIMAL C5-ONLY IDENTITY START, BOTH SYSTEMS REMAIN ON `J=R=0`, SO `A_k=1` AND `D_k=0` FOR EVERY FINITE TIER. THERE IS NO DERIVED BOOTSTRAP DRIVE.**

```text
C5_RECEIVER_MAP_EXISTS = true | TYPE-P |
  premises: DoR-008, DoR-009 |
  map: external history a -> z_n[a] -> D_n[a]S -> charged write

C5_RECEIVE_CLASS_HAS_LOCAL_FINITE_J_REPRESENTATION = true | TYPE-P |
  premises: DoR-009, source-germ source chart |
  scope: doubled finite-support histories in the zero-anchored logarithmic chart

C5_RECEIVE_CLASS_GLOBALLY_EQUALS_E_J = false | TYPE-R |
  test: group-valued holonomy history versus local additive logarithmic chart

C5_CONTAINS_R_PORT_DATA = false | TYPE-R |
  test: exact C5 formula contains z/D/W only and no symmetric bilocal source

C5_DERIVES_NEIGHBOR_TO_J_MAP = false | TYPE-R |
  counterfamily: identity, direct, and proper-subset routing maps all compose
                 with the same C5 receiver law

C5_DERIVES_NEIGHBOR_TO_R_MAP = false | TYPE-R |
  test: C5 is independent of R, so it constrains no R-valued emission

MUTUAL_SOURCING_MAP_CONSTRUCTED = false | TYPE-U |
  would-build: for each directed network edge Y->X,
               d_J^(Y->X):Hist_Y->E_J,X and
               d_R^(Y->X):Hist_Y->E_R,X,
               with source-chart, covariance, restriction, reality, quotient,
               next-tier, common-origin, and no-supplementation certificates

RECIPROCITY_FORCED_BY_C5_OR_E_POST = false | TYPE-R |
  test: directed and exchange-symmetric edge pairs obey the same local C5 law

CONDITIONAL_TWO_SYSTEM_TOWER_EXISTS = true | TYPE-P |
  premises: DoR-008, DoR-009, V007 source germ, supplied finite edge-source cylinders

DERIVED_IDENTITY_START_NETWORK =
  A_A,k=A_B,k=1; D_A,k=D_B,k=0; weights fixed | TYPE-P |
  premises: same stack; no added edge source

GENUINE_NETWORK_K_DEPENDENCE = NO_VERDICT |
  reason: it is the partial-sum law of the unbuilt edge-source sequences

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

---

## 0. Lead determination

The derivation arm stops at a type-theoretic obstruction, not at a difficult
normalization.

C5 supplies a response map of the form

```text
r_X : ExternalHistory_X -> ChargedWrite_X.             (C5D-1)
```

Mutual sourcing requires an additional directed edge map

```text
e_(Y->X) : History_Y -> ExternalHistory_X,             (C5D-2)
```

or, at the live V007 interface,

```text
d_src^(Y->X)
  =(d_J^(Y->X),d_R^(Y->X))
  : History_Y -> E_J,X direct-sum E_R,X.               (C5D-3)
```

There is no inversion from `(C5D-1)` to `(C5D-2)`. For every well-typed
candidate `e_(Y->X)`, the composite `r_X o e_(Y->X)` exists. The receiver
law therefore cannot select the emitter. This remains true even if the
neighbor is granted, in the derivation's favor, the same finite holonomy
carrier as the receiver.

The exact C5 algebra narrows the codomain that a future `d_J` must reach. It
does not construct the map, and it says nothing about `d_R`. The phrase
"derived up to normalization" is therefore too strong: the missing data are
the emission domain identification, network routing, local-chart placement,
bilocal component, and directed-edge law. A normalization would address none
of these.

---

## 1. Custody, currency, and symbol discipline

### 1.1 Send-time preflight

```text
DOES_THE_RECEIVER_DEPENDENCE_EXIST = yes
DOES_THE_MUTUAL_SOURCING_MAP_EXIST = no | TYPE-U
IS_THE_VERSION_CURRENT = yes through Q-334 and C44
ARE_ALL_INPUTS_FOR_A_NONZERO_NETWORK_TOWER_PRESENT = no | TYPE-R |
  missing: d_J and d_R on directed network edges
```

Q-334 is not used as a substitute for this derivation. Its independent
origin-port typecheck is a consistency check after C5 is read from source.
The derivation below starts from the ratified law, the live source-port
definitions, and the exact finite tower.

### 1.2 Roots entered

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003/

/Users/bgm/MB Work/alpha_supervision/

/Users/bgm/MB Work/alpha-program-archive/workspace/  [mirror destination only]
```

`a32_holdout/custodian_private/` was excluded and not entered.

### 1.3 Frozen authorities

| Authority | SHA-256 | Use |
|---|---|---|
| `LOCKED_PROCESS.md` | `f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba` | process, typing, fences, custody |
| relay 417 | `04633f12927fb6aee15d1a45018841cfb42dfddb1d5cf514a943d88fba33091a` | commissioned derivation arm |
| live Q-register at freeze | `7f47df26f1ac9c2d9e9a797d530c2cba03d84dc4f62b01ca55a2924fe4d6aa9a` | Q-334 currency |
| governing plan at freeze | `5051d2333d5516cfd74402345481a4407de488c332858b0b5f8dea89ad0cbce9` | C44 commission |
| DoR-009 | `11632fa30dfe9225c228f07a3be4717c73bdfc9e38b0c76c46d905d3fe193bc5` | ratification of `E_post`, finite locality, external-parent scope |
| transition-law V002 | `db1808e4da38cbfed8b12017885aff1bf63b0378e9971c37294e21fa08766fee` | exact law and C5 certificate |
| source germ V007 | `bd33e54c27ddb8ed5224637d7888a071026db33a1a17c7127a27ffa647b69896` | live exponent and source-output normalization |
| source germ V001 | `112a6658ef09ae9c309e2ff8b567d71c88e08e3692761162a0fb81fd1fdb3975` | explicit `J/R` carriers, local character chart, source functionals |
| full-source tower Q-333 | `fc63b0d885450d3d23f0cdfca0bbb46d96c3be7c23f5f3a905a1d1bfe19efbcb` | exact finite source-cylinder tower |
| C5 access-channel typecheck Q-332 | `99d294e5b2d511e6e6abf3f0cee8bc6892e5ab6eba2a474cc9a9e6abe55d6ad7` | independent completed-record boundary check |
| origin-port typecheck Q-334 | `4e00c7edbec105cd9c60cba483f11c1888a541e5963f3c1168fc6d00085669b0` | independent current-stack consistency check |

All cleanroom authority sidecars used here were verified before use.

### 1.4 Load-bearing symbol collisions

```text
C5  = DoR-009 charge/flux-access certificate,
      not an unrelated construction convention or plan clause.

A_j = external connection/history argument of the law.
SysA, SysB = the two record systems below; they are not the source variable A_j.

R   = V007 symmetric bilocal source.
|r> = ready-record ray; it is not R.

p_X = branch weight of system X.
P_ch,X = charged-sector projector; it is not p_X.
```

---

## 2. C5 read as the exact receiver map

### 2.1 Ratified local law

DoR-009 ratifies V002 with `E_post`, explicitly saying that charge follows
the write's direction (`DECISION_OF_RECORD_009_...md:8-17`). V002 defines,
for `n in {+1,-1}`,

```text
z_(n,j)[a_j] := chi_n(h_j[a_j]),

D_(n,j)[a_j]
  := |r_j><r_j|+z_(n,j)[a_j]|p_j><p_j|+|e_j><e_j|,

W_N^(n)[a]
  := tensor_(j=1)^N (D_(n,j)[a_j] S_j),

U_N^(n)[a]
  := P_0 tensor I_(3^N)+P_ch tensor W_N^(n)[a].       (C5D-4)
```

This is quoted from
`STAGE8_SOURCE_COUPLED_RECORD_TRANSITION_LAW_ADOPTION_PROPOSAL_V002.md:281-301`.
At one and two cells, the same source gives

```text
W_1^(n)[a]|r> = z_n[a]|p>,

W_2^(n)[a_1,a_2]|rr>
  =z_(n,1)[a_1]z_(n,2)[a_2]|pp>.                    (C5D-5)
```

The two-cell action is displayed at V002 `:312-328`. The exact
zero-extension rule is

```text
W_M^(n)[a_1,...,a_N,0,...,0]
  =W_N^(n)[a_1,...,a_N] tensor S^(tensor(M-N)),       (C5D-6)
```

at V002 `:330-335`.

### 2.2 What C5 proves

The C5 row says `charge/flux access`, passes `E_post`, and kills the pre-only
victim (`V002:363-372`; the explicit victim is in V001 `:373-382`). Its
failure-capable distinction is

```text
D_n[a]S|r> = z_n[a]|p>       [history-sensitive],
S D_n[a]|r> = |p>            [history-blind].         (C5D-7)
```

Therefore C5 derives the receive-side chain

```text
ExternalHistory_N
  --h--> U(1)^N
  --chi_n--> U(1)^N
  --D(.)S--> U(H_record,N)
  --on charged ready ray--> C|P_N>.                  (C5D-8)
```

It also carries the exact endpoint covariance

```text
W_1^(n)[a^g]
  =G_out^(n)(g_t) W_1^(n)[a] G_in^(n)(g_s)^dagger,   (C5D-9)
```

from V002 `:337-347`.

This is the complete mathematical dependence C5 certifies. Its domain is an
already supplied external connection/history. Its test codomain is the
untraced written-record vector or, before evaluation, the controlled unitary.
It has neither a neighbor record as domain nor a source port as codomain.

```text
C5_IS_RECEIVER_SENSITIVITY_CERTIFICATE = true | TYPE-P | DoR-009
C5_IS_EMITTER_DEFINITION = false | TYPE-R |
  test: domain/codomain of (C5D-8)
```

### 2.3 The external-parent boundary is ratified, not accidental

DoR-009 ratifies three rows, including the external-parent scope. The
decision expressly excludes parent, curvature, distributed, and
source-contact classes by declaration (`DoR-009:15-17`). V002 likewise
prices the complete external parent as unbuilt (`V002:442-455`). A network
edge that generates the input `a`, `J`, or `R` is therefore not hidden
inside the ratified finite law. It is exactly the additional parent/edge
datum that the law leaves outside its scope.

---

## 3. Typing C5 against V007's ports

### 3.1 The live source domain

The source germ declares

```text
E_J   := ell^1(N;C)_+ direct-sum ell^1(N;C)_-,
E_R   := S_1,sym(H_CTP),
E_src := E_J direct-sum E_R.                          (C5D-10)
```

The exact source is

```text
Xi_n^007[J,R]
  =L_n^Theta(J)-(1/2)Q_n^even(R),

Z_n^007[J,R]
  =(1-p)+p exp(Xi_n^007[J,R]).                        (C5D-11)
```

The carrier definitions and norm occur in source germ V001 `:180-212`;
V007 states the inherited live exponent at `:101-124`.

### 3.2 The lawful local `J` overlap

V001 states that the local `J` variables are zero-anchored logarithmic charts
of the ratified U1 holonomy characters and that only the germ around the
identity is used (`:217-220`). It defines

```text
A_n(J)=i n sum_j J_delta,j,

L_n^Theta(J)
  =(1/2)[A_n(J)+conjugate(A_(-n)(Theta_J J))].        (C5D-12)
```

At `R=0` and finite support, the germ reproduces exactly

```text
(1-p)+p product_(j=1)^N
  conjugate(chi_n(h_j[J_-])) chi_n(h_j[J_+]),        (C5D-13)
```

from V001 `:326-340`.

Thus, after the ratified forward/backward doubling, C5's finite relative
character has a local finite-core representation in the `J` port:

```text
product_j conjugate(z_-,j) z_+,j
  =exp(L_n^Theta(J))                                  (C5D-14)
```

on the admitted zero-anchored chart.

This is a receiver-interface compatibility result. It does not identify a
neighbor history with `J`. It also does not globalize the logarithm: the C5
input is group-valued, while `J` is an additive local chart. The exact result
is therefore:

```text
C5_FINITE_DOUBLED_RECEIVE_CONTENT_TYPES_TO_LOCAL_J_CHART = true | TYPE-P
C5_RECEIVE_CONTENT_GLOBALLY_IDENTICAL_TO_E_J = false | TYPE-R
```

### 3.3 C5 has no `R` component

The `R` port is an independent symmetric trace-class bilocal source. Its
functional is a U1-real same-cell trace (`V001:282-306`). Nothing in
`(C5D-4)` through `(C5D-9)` contains a bilocal source, a trace-class operator,
or the contraction `Q_n^even`.

Consequently:

```text
C5_RESPONDED_TO_INFLUENCE_HAS_FULL_J_R_STRUCTURE = false | TYPE-R
C5_SUPPLIES_J_LIKE_RECEIVE_CONTENT = true | TYPE-P | local finite chart only
C5_SUPPLIES_R_LIKE_RECEIVE_CONTENT = false | TYPE-R
```

The missing `R` datum cannot be called a normalization. It is a different
source coordinate with a different carrier and different derivative role.

### 3.4 Necessary emission contract, not an emitted value

C5 and V007 jointly derive only the interface a future edge law must satisfy:

```text
d_J^(Y->X)(h_Y) in E_J,X,
d_R^(Y->X)(h_Y) in E_R,X,

exp(L_X^Theta(d_J^(Y->X)(h_Y)))
  must reproduce the admitted relative character seen by C5
  on every finite restriction,                              (C5D-15)

d_R must obey V007 reality, trace-class, restriction,
and common-origin requirements.                            (C5D-16)
```

Equations `(C5D-15)` and `(C5D-16)` are requirements on a future map. They
are not formulas for one.

---

## 4. Counterexample to inversion: the emitter family remains open

### 4.1 General type theorem

Let `r_X:X_X->Y_X` be the C5 receiver map and let `H_Y` be any proposed
neighbor-history carrier. C5 places no predicate on maps `e:H_Y->X_X`.
Every such well-typed map yields a composite

```text
H_Y --e--> X_X --r_X--> Y_X.                         (C5D-17)
```

Unless `r_X` is supplied with a universal property that represents maps out
of every `H_Y`, there is no induced `e`. No sealed C5 or DoR-009 clause states
such a property. C5 is not invertible in the relevant direction even when
`r_X` happens to be injective on a local history chart: inversion could at
most recover an already observed external input from a write, not determine
which neighbor emits it or how.

### 4.2 Hostile best-case counterfamily on the same carrier

Grant the derivation its strongest possible assumption, after passing to the
doubled relative-holonomy quotient on which common endpoint gauge has already
cancelled:

```text
H_Y = Q_N = ExternalRelativeHistory_X = U(1)^N.      (C5D-18)
```

At `N>=2`, all of the following are well-typed, preserve the identity input,
commute with componentwise conjugation, are natural under zero-extension, and
compose with the same C5 law:

```text
e_0(z_1,...,z_N)   := (1,...,1),
e_all(z_1,...,z_N) := (z_1,...,z_N),
e_1(z_1,...,z_N)   := (z_1,1,...,1).                 (C5D-19)
```

`e_all` and `e_1` are both nontrivial. They differ on the exact charged
write:

```text
r_X(e_all(z))|R_N> = product_j z_j |P_N>,
r_X(e_1(z))|R_N>   =z_1 |P_N>.                       (C5D-20)
```

The quotient has trivial common-endpoint gauge action, so these maps introduce
no unverified gauge lift. The projection family is compatible with cellwise
source locality; selecting which neighbor cells are connected is network-
routing data, not a C5 fact.
The identity member gives the sealed null slice. C5 remains a valid
failure-capable receiver certificate under all three because its law is still
defined and history-sensitive on its full declared input domain.

The ratified `n=+1,-1` character family supplies an additional orientation-
reversed receive family. C5 passes both character labels; E_post selects the
write's temporal attachment, not one network emission map.

### 4.3 The `R` counterfamily is larger

Because C5 contains no `R`, for any candidate history carrier and any two
distinct well-typed maps

```text
e_R,0(h):=0,
e_R,1(h):=T(h) in S_1,sym(H_CTP),                    (C5D-21)
```

C5 gives the same verdict. The existence of a nonzero `T` is not asserted
here; `(C5D-21)` states the exact freedom any future authored or derived map
must resolve. C5 provides no equation capable of distinguishing its members.

```text
C5_INVERSION_UNIQUE_UP_TO_NORMALIZATION = false | TYPE-R
C5_EDGE_MAP_COUNTERFAMILY_SIZE_AT_LEAST_THREE = true | TYPE-P |
  scope: hostile same-carrier finite model (C5D-19)
```

---

## 5. Reciprocity is not derived

### 5.1 What consistency requires

For two systems `SysA` and `SysB`, a lawful directed network needs

```text
d_src^(B->A):Hist_B->E_src,A,
d_src^(A->B):Hist_A->E_src,B.                        (C5D-22)
```

The minimal consistency condition is merely that each image lies in the
receiving system's source domain and satisfies `(C5D-15)` and `(C5D-16)`.
With no post-output supplementation, a history produced at tier `t` may feed
the other system only as a declared input to tier `t+1`:

```text
s_A,t+1=d_src^(B->A)(Hist_B,t),
s_B,t+1=d_src^(A->B)(Hist_A,t).                       (C5D-23)
```

This is a typing and update contract, conditional on the maps. It is not a
construction of them.

### 5.2 Exchange reciprocity would be an additional law

If the two systems and their source carriers are separately identified by
exchange maps `tau_H` and `tau_src`, symmetric reciprocity would require

```text
d_src^(A->B)
  =tau_src o d_src^(B->A) o tau_H^(-1).              (C5D-24)
```

Neither `tau_H`, `tau_src`, nor `(C5D-24)` occurs in C5. Directed choices
with `d_src^(A->B)` unequal to the exchanged `d_src^(B->A)` remain compatible
with the local law. The counterfamily `(C5D-19)` may be assigned differently
on the two directed edges without changing either receiver's C5 certificate.

### 5.3 What E_post actually orients

E_post fixes

```text
W_post(a)=D(a)S,                                     (C5D-25)
```

so the character follows the write at each receiving cell. It gives a local
time arrow. Combined with the no-supplementation discipline, it supports the
next-tier direction in `(C5D-23)`. It does not turn a directed graph into an
undirected graph and does not equate the two edge maps.

```text
E_POST_FORCES_LOCAL_WRITE_ORIENTATION = true | TYPE-P | DoR-009
E_POST_FORCES_NETWORK_RECIPROCITY = false | TYPE-R
E_POST_SELECTS_NETWORK_ADJACENCY = false | TYPE-R
```

---

## 6. Exact two-system tower, conditional on supplied edge cylinders

### 6.1 Input family

Let, for each finite tier `1<=t<=k`,

```text
s_A,t=(J_(B->A),t,R_(B->A),t) in E_src,A,
s_B,t=(J_(A->B),t,R_(A->B),t) in E_src,B.            (C5D-26)
```

No map producing `(C5D-26)` is assumed. This section computes the exact
network transducer conditional on those inputs, which is the maximal lawful
two-system construction.

For `X in {A,B}`, define

```text
Xi_X,t
  :=L_X^Theta(J_X,t)-(1/2)Q_X^even(R_X,t),

S_Xi,X,k:=sum_(t=1)^k Xi_X,t,
D_X,k  :=(1/2)sum_(t=1)^k Q_X^even(R_X,t).           (C5D-27)
```

### 6.2 Closed forms

The Q-333 operator induction applies separately to each receiver:

```text
F_X,k
  =P_0,X+exp(S_Xi,X,k)P_ch,X,

A_X,k
  =(1-p_X)+p_X exp(S_Xi,X,k),                        (C5D-28)

weight_0,X(k)=1-p_X,
weight_ch,X(k)=p_X.                                  (C5D-29)
```

Equations `(C5D-27)` through `(C5D-29)` are exact for arbitrary finite P2
source cylinders. They inherit Q-333's prefix, finite-core, reality, quotient,
and rank-symbolic certificates.

The complete network object constructed here is the ordered pair

```text
Tower_AB,k:=((F_A,k,A_A,k),(F_B,k,A_B,k)).           (C5D-30)
```

No tensor-product joint amplitude is asserted. Such a product would require
an independently certified joint state and interaction rule. C5 supplies
neither.

### 6.3 Source-conditioned network growth

For any supplied edge histories, all network `k` dependence is exactly the
pair of partial sums

```text
(S_Xi,A,k,S_Xi,B,k)                                  (C5D-31)
```

and the bilocal accumulations `(D_A,k,D_B,k)`. Thus the finite network law is
a two-way transducer. It does not choose whether the sums are bounded,
linear, super-linear, oscillatory, or zero. That classification belongs to
the edge-source sequences, exactly as Q-333 proved for one tower.

```text
TWO_SYSTEM_CONDITIONAL_CLOSED_FORM = true | TYPE-P
TWO_SYSTEM_EDGE_SEQUENCE_SELECTED_BY_C5 = false | TYPE-R
```

---

## 7. Identity-start bootstrap test

### 7.1 The exact null input

Both systems start in the ready configuration. C5 provides no outgoing edge
source from that fact. The maximal construction with no added map therefore
uses the exact source identity at every tier:

```text
J_A,t=R_A,t=J_B,t=R_B,t=0.                           (C5D-32)
```

Then

```text
Xi_A,t=Xi_B,t=0,
S_Xi,A,k=S_Xi,B,k=0,
D_A,k=D_B,k=0,                                       (C5D-33)

F_A,k=I_src,A,      A_A,k=1,
F_B,k=I_src,B,      A_B,k=1                          (C5D-34)
```

for every finite `k`. The physical branch weights remain

```text
(1-p_A,p_A), (1-p_B,p_B).                            (C5D-35)
```

This reproduces the Q-333 identity theorem and the independent Q-332/Q-334
null-slice determinations.

### 7.2 Why the local writes do not ignite the network

At identity source, `D_n[0]=I` and the ratified write still acts as `S` on
the charged record. A ready ray can therefore become a pointer ray. But C5
defines only how an external character modifies that write. It does not map
the resulting pointer ray, untraced phase, or completed record density into
the other system's `J` or `R` port.

Using the pointer as a next-tier source would be post-output supplementation
unless an edge map with the certificates in `(C5D-3)` were frozen before the
next tier. Using the untraced phase would additionally bypass the completed-
record boundary identified independently at Q-332. Hence no nonidentity
source appears merely because two systems are described as "listening."

### 7.3 Exact bootstrap verdict

```text
C5_ONLY_TWO_SYSTEM_BOOTSTRAP_IGNITES = false | TYPE-R |
  test: first next-tier source has no producing arrow

MAXIMAL_DERIVED_IDENTITY_NETWORK_DEPTH =
  D_A,k=D_B,k=0 for every finite k | TYPE-P

NONZERO_MUTUAL_DRIVE_FROM_READY_START = NO_VERDICT |
  would-decide: a certified edge map and its value on the ready/pointer history
```

A future edge law could map a written record to a nonzero next-tier source,
or it could leave the identity configuration fixed. C5 decides neither. The
present result refutes derivation from C5; it does not refute every possible
mutual-sourcing dynamics.

---

## 8. Certificates, six-account rows, and doors

### 8.1 Restriction and covariance

| Check | Result | Reason |
|---|---|---|
| tier one | `PASS` | `(C5D-28)` at `k=1` is the live one-source germ |
| identity | `PASS` | `(C5D-32)` gives `(C5D-34)` exactly |
| prefix | `PASS` | appending zero source leaves each finite partial sum unchanged |
| cell restriction | `PASS` | inherited P2 finite-corner restriction for each supplied edge cylinder |
| U1 reality | `PASS` | inherited separately for `L^Theta` and `Q^even` |
| quotient | `PASS` | only the live quotient-descended source functionals are evaluated |
| rank discipline | `PASS` | `p_A,p_B` remain symbolic; no rank pair is selected |
| network reciprocity | `UNBUILT` | no edge maps exist to test |
| common origin | `UNBUILT` | C5 is a receiver law, not an edge-map provenance witness |

### 8.2 Six-account ledger

| Account | Built content | Missing content | Tail/class action |
|---|---|---|---|
| measure | none | no measure is needed for the finite conditional tower | none |
| contour | inherited finite forward/adjoint CTP pairing only | no new contour | none |
| boundary/contact | E_post receiver endpoints inherited | inter-system boundary/adjacency map | none formed |
| domain closure | finite P2 source cylinders | no all-tier or network-history completion | no completion opened |
| stationary/Schur | none | outside this finite drive derivation | none |
| class formation | finite products and sums only | edge-map class and any infinite network limit | no weak-star/bidual step |

### 8.3 Door flags

```text
DOOR_C5_RECEIVER = OPENED | DoR-009 exact finite law

DOOR_LOCAL_FINITE_J_CHART = OPENED |
  topology: finite core inside V007/P2 norm source domain |
  scope: zero-anchored logarithmic neighborhood

DOOR_NETWORK_J_EMISSION = NOT_OPENED | TYPE-U
DOOR_NETWORK_R_EMISSION = NOT_OPENED | TYPE-U
DOOR_NETWORK_RECIPROCITY = NOT_OPENED | TYPE-U
DOOR_NETWORK_ADJACENCY = NOT_OPENED | TYPE-U
DOOR_NETWORK_HISTORY_COMPLETION = NOT_OPENED | TYPE-U
DOOR_WEAK_STAR_OR_BIDUAL = NOT_OPENED | TYPE-S
DOOR_CONTINUUM_RESPONSE = NOT_OPENED | TYPE-S
DOOR_BRIDGE = NOT_OPENED | TYPE-S
```

No measure, contour extension, inter-system boundary datum, infinite-tier
topology, weak-star completion, bidual, response object, physical root, or
numerical value is introduced.

---

## 9. Final determination

C5 can be read as a map, but only in its stated direction:

```text
external U(1) history -> charged write.               (C5D-36)
```

On the doubled finite core, the relative character in `(C5D-36)` is
represented by V007's local `J` chart. This gives a precise receive-interface
contract. It does not yield

```text
neighbor history -> J,R.                              (C5D-37)
```

The attempted inversion is refuted by the explicit emitter counterfamily
`(C5D-19)`, and the missing `R` coordinate is independent of that
counterexample. E_post orients the local write but supplies neither network
adjacency nor exchange reciprocity.

The exact two-system result is therefore split:

```text
WITH SUPPLIED DIRECTED EDGE CYLINDERS:
  A_X,k=(1-p_X)+p_X exp(sum_t Xi_X,t),
  D_X,k=(1/2)sum_t Q_X^even(R_X,t),
  X in {A,B}.                                         (C5D-38)

WITH C5 ALONE AT THE IDENTITY START:
  A_A,k=A_B,k=1,
  D_A,k=D_B,k=0,
  branch weights fixed for every finite k.            (C5D-39)
```

There is no derived mutual ignition and no derived network growth law. The
sharp residue is the pair of directed source-generation maps `(C5D-22)`,
including their reciprocity or nonreciprocity rule. That is the exact object
the other race arm would have to author openly; C5 does not shrink it to a
normalization choice.

```text
REGISTER_HEAD_AT_FREEZE = Q-334
REGISTER_SHA256_AT_FREEZE =
  7f47df26f1ac9c2d9e9a797d530c2cba03d84dc4f62b01ca55a2924fe4d6aa9a

FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-S
ALPHA_FACING_RESULT_PRODUCED = false | TYPE-S
PHYSICAL_ROOT_OR_VALUE_EVALUATED = false | TYPE-S

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 10. Custody

This lane seals this lane-tagged artifact, verifies its sidecar, mirrors the
artifact and sidecar byte-identically, reports both hashes, and stops. It does
not edit the register, governing plan, or tracker and performs no git, commit,
or push action.
