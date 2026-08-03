# Stage 8 Task 4a Origin-Fed Refinement Tower — Gen_Omega Port Typecheck Determination — Codex Lane 2 V001

Date: 2026-08-03  
Task: PASTE 416 / Task 4a / finite depth program computation four  
Lane: CODEX LANE 2  
Register head at freeze: Q-333  
Status: **SHARP STOP AT THE FIRST SUBSTITUTION. `Gen_Omega` GENERATES THE SOURCE-SECTOR DENSITY `rho_S`, NOT EITHER SOURCE-HISTORY ARGUMENT `J` OR `R` CONSUMED BY THE LIVE GERM. THE RATIFIED ORIGIN THEREFORE FIXES THE SYMBOLIC BRANCH WEIGHT `p_[A]` BUT DOES NOT FIX THE TOWER EXPONENT. THE COMPLETE ORIGIN-FED NONZERO TOWER IS TYPE-U. THE MAXIMAL NO-ADDED-SOURCE SLICE IS EXACT AND TRIVIAL: WEIGHTS `(1-p_[A],p_[A])`, `A_k=1`, `Gamma_k=0`, AND `D_k=0` AT EVERY FINITE TIER.**

```text
GEN_OMEGA_D_STATE_EXACT_OUTPUT
  = rho_S,[A]=I_A/Tr_A(I_A) | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013

GEN_OMEGA_BRANCH_WEIGHT
  = p_[A]=Tr_A(P_ch)/Tr_A(I_A)=r_ch/(r_0+r_ch) | TYPE-P |
  symbolic only; no rank pair selected; no ratio evaluated

D_STATE_OUTPUT_IS_A_J_HISTORY = false | TYPE-R |
  test: d_state lands in normalized source densities, whereas J is in E_J

D_STATE_OUTPUT_IS_AN_R_PROBE = false | TYPE-R |
  test: d_state lands in normalized source densities, whereas R is in E_R

ORIGIN_TO_GERM_SOURCE_PORT_MAP_FOUND = false | TYPE-S |
  bounded roots: DoR-013, Gen_Omega V003, germ V004/V007, Q-332, Q-333

NONZERO_ORIGIN_FED_TOWER_CONSTRUCTED = false | TYPE-U |
  would-build: d_J:Omega_prim->E_J and d_R:Omega_prim->E_R,
               or one certified d_src:Omega_prim->E_J direct-sum E_R

THEORY_INTRINSIC_NONZERO_DEPTH_LAW = NO_VERDICT

MAXIMAL_NO_ADDED_SOURCE_SLICE =
  weights=(1-p_[A],p_[A]); A_k=1; Gamma_k=0; D_k=0 | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014 as amended (2),
            DoR-015, C38

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

---

## 0. Lead determination

The relay's proposed substitution does not type-check.

DoR-013 ratifies exactly three generative maps:

```text
d_state : Omega_prim,N -> normalized source-sector densities,
d_ready : Omega_prim,N -> the forced plus-root ready ray,
d_law   : Omega_prim,N -> the DoR-009 E_post transition law.
```

The exact state output is

```text
d_state(Omega_prim,N)=rho_S,[A]:=I_A/Tr_A(I_A).     (OF-1)
```

The live germ instead consumes two independent source-history arguments:

```text
J in E_J:=ell^1(N)_+ direct-sum ell^1(N)_-,
R in E_R:=S_1,sym(H_CTP),
s=(J,R) in E_src:=E_J direct-sum E_R.               (OF-2)
```

Its exponent is

```text
Xi_n^007[J,R]
  =L_n^Theta(J)-(1/2)Q_n^even(R).                   (OF-3)
```

No ratified map sends `(OF-1)` to either coordinate in `(OF-2)`. The germ's
actual consumption of `rho_S` is the scalar contraction

```text
p_[A]:=Tr_A(rho_S,[A] P_ch)
      =Tr_A(P_ch)/Tr_A(I_A)
      =r_ch/(r_0+r_ch),                             (OF-4)
```

which appears as a coefficient in

```text
Z_[A],n[J,R]
  =(1-p_[A])+p_[A] exp(Xi_n^007[J,R]).              (OF-5)
```

Thus the origin and the germ sources occupy different slots:

```text
Gen_Omega fixes:       rho_S,[A], p_[A], ready ray, law;
V007 still requires:  J and R as independent source arguments.
```

Calling both objects "source" does not compose their types. `rho_S` is a
source-sector **state**; `J` and `R` are source **histories/probes**. The
origin-fed tower requested by the relay would need one more descent map. It
is not present.

The exact result is therefore a boundary theorem:

> **Origin/source factorization theorem.** On every fixed ratified origin
> fiber `[A]` and every finite tower depth `k`, the origin determines only
> the invariant coefficient `p_[A]`; all nontrivial depth dependence remains
> in the independent source sequence through the partial sum of `(OF-3)`.

The maximal construction using no datum beyond the ratified origin is the
already sealed identity-source slice `J_t=0`, `R_t=0`. It is exact and
trivial at every tier. This does **not** mean the origin forces its missing
ports to zero. It means zero is the sealed identity input, while every
nonzero feed requires an unbuilt map.

---

## 1. Custody, currency, and authorities

### 1.1 Preflight correction

The relay froze at Q-332. At execution, the live register had advanced to
Q-333. Q-333 does not supersede the task; it strengthens the typecheck:

```text
Q-333: the full tower is a transducer over arbitrary P2 source cylinders;
       its growth law is the supplied source sequence's partial-sum law;
       no source sequence or growth class is selected by the tower itself.
```

The relay's statement `ARE_ITS_INPUTS_PRESENT = YES, ALL RATIFIED` is false
for the intended nonzero substitution. The origin state exists, and the
source ports exist, but the map between them does not.

```text
DOES_THE_REQUESTED_NONZERO_OBJECT_EXIST = false | TYPE-U
IS_THE_VERSION_CURRENT_AFTER_Q333_CHECK = true
ARE_ALL_COMPOSITION_MAPS_PRESENT = false | TYPE-R
```

### 1.2 Roots entered

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003/
/Users/bgm/MB Work/alpha_supervision/
/Users/bgm/MB Work/alpha-program-archive/supervision/
/Users/bgm/MB Work/alpha-program-archive/workspace/  [mirror destination]
```

Excluded:

```text
a32_holdout/custodian_private/                       NOT ENTERED
anchor member or ordered rank pair                   NOT SELECTED
record density converted to a source by convention  NOT DONE
continuum response, bridge, root, coupling, scale    NOT CONSTRUCTED OR EVALUATED
comparison to a measured constant                    NOT PERFORMED
register, plan, tracker, git, commit, push            NOT TOUCHED
```

### 1.3 Frozen authorities

| Authority | SHA-256 | Use |
|---|---|---|
| `LOCKED_PROCESS.md` | `f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba` | fences, typing, custody |
| `RELAY_PASTE_416_THE_ORIGIN_FED_TOWER_V001.md` | `1d09ca11ba56679b8a7c97f3baeedc9ffbeab57cf70e564f4f7ef4a5132e32a0` | task contract |
| DoR-013 | `f2a7838d41b7b7df42ae92bc3d59399ee04bbec65cecadc8a43f6a36ac4756ec` | ratified family and exact three maps |
| `STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V003.md` | `1be5f6a7e40c34586f3b5ab78f9129de0b5d2041cb6695b0e549443ddd6c6ee0` | primitive tuple, `d_state`, `d_ready`, `d_law` |
| `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V004.md` | `d4cdbb6623797df6accb7dc9b24134d179bfc8e8d039c585d5c91ae23255869e` | explicit origin-to-germ state contraction |
| `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V007.md` | `bd33e54c27ddb8ed5224637d7888a071026db33a1a17c7127a27ffa647b69896` | live exponent and source carriers |
| Q-332 intrinsic feedback determination | `99d294e5b2d511e6e6abf3f0cee8bc6892e5ab6eba2a474cc9a9e6abe55d6ad7` | record export and identity tower |
| Q-333 full-source tower | `fc63b0d885450d3d23f0cdfca0bbb46d96c3be7c23f5f3a905a1d1bfe19efbcb` | arbitrary-source factorization and growth classification |

All local authority sidecars used here were verified. DoR-013's archived
sidecar was verified from its own directory because it names its artifact
relatively.

---

## 2. Exact extraction of the origin output

### 2.1 The primitive tuple and its outputs

For every admitted finite stage `N`, Gen_Omega freezes

```text
Omega_prim,N^v003 := (
  A0 finite scalar source realization,
  P_0,P_ch,E_ch,Tr_A,I_src,
  P_src, anchor tag and finite anchor certificate,
  rooted signed incidence, plus root, faithful characters,
  E_post, tensor/zero-extension grammar, finite domains
).
```

The tuple expressly does not contain `rho_S`, the ready ray, the law, or
`p_[A]` as output coordinates. The maps execute:

```text
d_state(Omega_prim,N)
  := unique normalized fixed state of P_src
   = I_A/Tr_A(I_A),                                 (OF-6)

d_ready(Omega_prim,N)
  := C |r>^(tensor N),                              (OF-7)

d_law(Omega_prim,N;a)
  := P_0 tensor I_(3^N)+P_ch tensor W_N^(n)[a].     (OF-8)
```

Equation `(OF-8)` is a law **depending on** an input background `a`. It does
not generate or select `a`, `J`, or `R`.

### 2.2 Family-level neutrality

DoR-013 adopts BI/DB/SYM as a family and forbids member selection. Every
member produces the same normalized-identity state and the same symbolic
sector-dimension-ratio form. Hence, on a fixed A0 rank fiber `[A]`,

```text
rho_S,t = rho_S,[A]                                 (OF-9)
p_t     = p_[A]                                     (OF-10)
```

for every tower tier at which the same frozen origin is evaluated. The
anchor tag and transient preparation-channel data do not change either
output.

This is the exact generated content available per tier. It is tier
independent. Reapplying `d_state` to the same frozen primitives merely
regenerates `(OF-9)`; it does not create a tier-dependent source history.

### 2.3 `N` and `k` remain different

The finite carrier label `N` in `Omega_prim,N` and the refinement depth `k`
are not identified. Q-333 proves that P2's finite-cell cutoff is not a
refinement-tier rule. Nothing in Gen_Omega adds such an identification.

```text
ORIGIN_FINITE_STAGE_N_EQUALS_REFINEMENT_DEPTH_K = false | TYPE-R |
  counterstructure: fixed origin stage with arbitrary finite tower depth
```

---

## 3. The port typecheck

### 3.1 Domain and codomain table

| Object | Type | Role |
|---|---|---|
| `Omega_prim,N` | finite generative primitive tuple | origin input |
| `rho_S,[A]` | normalized positive density on `H_A` | source-sector state |
| `p_[A]` | scalar finite-visible quotient | branch coefficient |
| `J` | `E_J=ell^1_+ direct-sum ell^1_-` | common/difference source history |
| `R` | `E_R=S_1,sym(H_CTP)` | symmetric bilocal probe |
| `Xi[J,R]` | scalar | live source exponent |

The available arrows are

```text
Omega_prim,N --d_state--> Dens_1^+(H_A) --Tr(P_ch .)--> C,

E_J --L_n^Theta--> C,
E_R --Q_n^even--> C.
```

The requested construction needs

```text
Omega_prim,N --d_src--> E_J direct-sum E_R,         (OF-11)
```

or its two components `d_J` and `d_R`. No such arrow occurs in DoR-013,
Gen_Omega V003, or the live germ.

### 3.2 Why the germ's “consumption port” does not supply the arrow

The germ consumes the origin output by tracing its controlled field factor
against the density:

```text
Z_[A],n[J,R]
  =Tr_A((P_0+exp(Xi[J,R])P_ch)rho_S,[A]).           (OF-12)
```

That trace yields `(OF-5)`. It is a density-to-coefficient contraction. It
does not turn the density into the arguments of `L_n^Theta` or
`Q_n^even`.

An attempted identification

```text
rho_S,[A] = J,  or  rho_S,[A] = R
```

fails before any formula is evaluated: the objects have different carriers,
symmetries, and operational roles. A density-to-`J` or density-to-`R` map
would require at least an observable pairing or preparation-to-history rule,
and its finite restrictions, reality, quotient, and no-supplementation
certificates.

### 3.3 Anti-relabeling result

```text
D_STATE_COMPOSES_DIRECTLY_WITH_L_N_THETA = false | TYPE-R
D_STATE_COMPOSES_DIRECTLY_WITH_Q_N_EVEN = false | TYPE-R
D_READY_SUPPLIES_J_OR_R = false | TYPE-R
D_LAW_SUPPLIES_J_OR_R = false | TYPE-R

RATIFIED_ORIGIN_TO_GERM_COEFFICIENT_MAP_EXISTS = true | TYPE-P
RATIFIED_ORIGIN_TO_GERM_EXPONENT_MAP_EXISTS = false | TYPE-S
```

The first map is `(OF-4)`. The second is the missing object `(OF-11)`.

---

## 4. Exact tower factorization with the origin exposed

### 4.1 General finite formula

For any externally supplied finite source sequence

```text
s_t=(J_t,R_t) in E_src, 1<=t<=k,
```

Q-333 gives

```text
S_Xi,k[s_1,...,s_k]
  :=sum_(t=1)^k [L_n^Theta(J_t)-(1/2)Q_n^even(R_t)],

D_k[R_1,...,R_k]
  :=(1/2)sum_(t=1)^k Q_n^even(R_t),                 (OF-13)

F_k=P_0+exp(S_Xi,k)P_ch,

A_k(Omega_prim;s_1,...,s_k)
  =(1-p_[A])+p_[A]exp(S_Xi,k).                     (OF-14)
```

The physical branch weights remain

```text
weight_0(k)=1-p_[A],
weight_ch(k)=p_[A].                                 (OF-15)
```

Equations `(OF-13)`–`(OF-15)` prove the factorization theorem. The origin
appears only through `p_[A]`; the source sequence appears only through
`S_Xi,k`. Changing anchor/transient-channel members at fixed `[A]` cannot
change the depth law. Changing `J_t,R_t` can realize every growth class
already classified at Q-333.

### 4.2 What the origin determines

```text
ORIGIN_DETERMINES_BRANCH_WEIGHTS = true | TYPE-P
ORIGIN_DETERMINES_SOURCE_EXPONENT = false | TYPE-R
ORIGIN_DETERMINES_D_K = false | TYPE-R
ORIGIN_SELECTS_A_Q333_GROWTH_CLASS = false | TYPE-R
```

The last three refutations are witnessed by distinct Q-333 source sequences
above the same fixed origin fiber, including zero, repeated, alternating,
and telescoping inputs.

---

## 5. Constant-generation and refreshed-generation alternatives

### 5.1 Constant re-evaluation of the ratified state map

Applying `d_state` afresh at every tier to the same frozen origin gives

```text
rho_S,t=rho_S,[A],
p_t=p_[A]
```

for all `t`. This is derived and family-wide. It supplies `(OF-15)`, but it
does not supply `J_t` or `R_t`.

If a future certified map produced one constant germ source

```text
s_*=(J_*,R_*):=d_src(Omega_prim,N),
```

then, conditionally,

```text
S_Xi,k=k Xi_n^007[J_*,R_*],
D_k=(k/2)Q_n^even(R_*),
A_k=(1-p_[A])+p_[A]exp(k Xi_n^007[J_*,R_*]).        (OF-16)
```

Equation `(OF-16)` is an interface consequence, not a constructed tower:
`d_src` is absent. It cannot be used to claim linear intrinsic depth.

### 5.2 Tier-refreshed generation

A genuine refreshed tower would require a recurrence such as

```text
Omega_(t+1)=Upsilon(Omega_t,rho_t,record_t),
s_(t+1)=d_src(Omega_(t+1)).                         (OF-17)
```

DoR-013 ratifies neither `Upsilon` nor `d_src`. Its no-post-output-
supplementation certificate permits outputs to feed a later construction
only through an independently specified next-tier map; it does not create
that map.

Merely re-running `d_state` on unchanged primitives is not `(OF-17)`. It is
the constant state result of Section 5.1. Declaring the prior state to be the
next tier's primitive tuple would discard most fields of `Omega_prim` and
repeat the Q-242 anti-relabeling failure.

```text
TIER_REFRESH_MAP_RATIFIED = false | TYPE-S
PRIOR_STATE_IS_A_VALID_NEXT_OMEGA_PRIM = false | TYPE-R
TIER_REFRESHED_ORIGIN_TOWER = false | TYPE-U |
  would-build: Upsilon plus d_src and their full finite certificates
```

No refreshed variant is computed by fiat.

---

## 6. Maximal no-added-source slice

The live source spaces have a sealed identity input:

```text
J_t=0,
R_t=0,
Xi_t=0.
```

Using it at each tier adds no declared probe, no feedback channel, and no
authored conversion. Equations `(OF-13)`–`(OF-15)` reduce exactly to

```text
D_k=0,
F_k=P_0+P_ch=I_A,
A_k=(1-p_[A])+p_[A]=1,
Gamma_k=Log_0(1)=0,                                 (OF-18)

weight_0(k)=1-p_[A],
weight_ch(k)=p_[A].                                 (OF-19)
```

This is the same maximal branch-only tower independently derived at Q-332.
The origin supplies the symbolic weights; identity supplies the zero source.

Scope discipline:

```text
ORIGIN_FORCES_J_EQUALS_ZERO = false | TYPE-R
ORIGIN_FORCES_R_EQUALS_ZERO = false | TYPE-R

ZERO_SOURCE_IS_THE_SEALED_IDENTITY_INPUT = true | TYPE-P
NO_ADDED_SOURCE_SLICE_IS_TRIVIAL = true | TYPE-P

ALL_POSSIBLE_THEORY_INTRINSIC_FEEDS_ARE_TRIVIAL = NO_VERDICT
```

The last line is essential. The absence of `(OF-11)` blocks the nonzero
theory-intrinsic feed; it does not prove that any future lawful feed must be
zero.

---

## 7. Exact theory boundary and would-build

### 7.1 Boundary theorem

**Theorem — ratified origin depth boundary.** Under DoR-008, DoR-009,
DoR-013, DoR-014 as amended (2), DoR-015, C38, and the live V007 germ:

1. Gen_Omega fixes the family-wide normalized source density and symbolic
   branch weight.
2. It does not fix a common/difference source history or symmetric bilocal
   probe.
3. Therefore it fixes the tower's require-side weights but not its
   allow-side exponent or depth law.
4. The only choice-free no-added-source slice is `(OF-18)`–`(OF-19)`.
5. A nonzero theory-intrinsic depth datum requires a new generative source-
   port map; the current corpus neither forces its value nor its growth form.

The proof is the codomain separation of Section 3 together with the exact
factorization `(OF-14)`.

### 7.2 Minimal build

The smallest object that changes the verdict is

```text
d_src=(d_J,d_R):Omega_prim,N -> E_J direct-sum E_R. (OF-20)
```

Its certificate battery must include:

```text
1. executable finite formulas for d_J and d_R;
2. DoR-008 finite restriction reproduction;
3. P2 norm compatibility and W3 adjoint naturality;
4. U1 reality covariance and source quotient compatibility;
5. family-level neutrality across every BI/DB/SYM anchor member;
6. no selected anchor, rank pair, torsor, or orientation;
7. no post-output supplementation;
8. target independence;
9. explicit statement whether the output is constant or refreshed;
10. if refreshed, a next-tier update map with its own domain and provenance.
```

No item is supplied by merely knowing `rho_S`. In particular, choosing an
observable basis to turn a density into `J`, or choosing a covariance kernel
to turn it into `R`, would add authored structure.

```text
MINIMAL_MISSING_OBJECT = GEN_OMEGA_TO_V007_SOURCE_PORT_DESCENT
MINIMAL_MISSING_OBJECT_STANDING = TYPE-U
AUTHORED_OR_DERIVED_STATUS = NO_VERDICT |
  derivation search over current ratified sources returned no map
```

---

## 8. Falsifiers and discipline

### 8.1 Tier one

At `k=1`, the general interface `(OF-14)` is the live V007 source germ. On
the no-added-source slice it reduces to the sealed source-free identity
`A_1=1`. No historical pairing or void row is revived.

```text
TIER_ONE_GENERAL_INTERFACE = PASS
TIER_ONE_NO_ADDED_SOURCE_IDENTITY = PASS
```

### 8.2 Declared tower recovery

Supplying declared `J_t,R_t` independently recovers Q-330/Q-333 exactly.
For a constant declared source, `(OF-16)` follows with `d_src` replaced by
the declared value. The origin adds no extra term and suppresses none.

```text
DECLARED_TOWER_RECOVERED = PASS
INTRINSIC_TERM_SUPPRESSED_BY_CONSTRUCTION = false | TYPE-R |
  reason: the exact exponent contains only the declared J/R terms
```

### 8.3 Restriction and identity

For a zero-appended source tier,

```text
A_(k+1)[s_1,...,s_k,0]=A_k[s_1,...,s_k].
```

On the identity slice this holds at every depth. The origin state is
restriction-compatible by the DoR-013 falsifier; no `N=k` identification is
used.

### 8.4 Reality, quotient, and ranks

The identity source is fixed by the source involution. The normalized state
and `p_[A]` are invariant across the admitted anchor/transient quotient. All
formulas carry the ordered rank pair symbolically. No anchor member and no
rank pair is selected, and the ratio in `(OF-4)` is not evaluated.

```text
REALITY = PASS
SOURCE_QUOTIENT = PASS
ANCHOR_FAMILY_NEUTRALITY = PASS
RANK_DISCIPLINE = PASS
NO_SELECTION = PASS
```

### 8.5 No-post-output supplementation

No map is inferred after inspecting the tower output. The missing descent
is reported, not supplied retroactively. The zero-source slice uses the
germ's antecedent identity element and not an answer-chosen probe.

```text
POST_OUTPUT_SOURCE_SUPPLEMENT_ADDED = false | TYPE-S
TARGET_TUNED_SOURCE_ADDED = false | TYPE-S
```

---

## 9. Six-account and door ledger

| Operation | Domain | Image | Restriction | Tail/class action | Standing |
|---|---|---|---|---|---|
| `d_state` | `Omega_prim,N` | normalized finite density | DoR-013 restriction falsifier | finite; no tail | built / TYPE-P |
| state contraction | density plus `P_ch` | symbolic `p_[A]` | finite trace-compatible | finite-visible quotient | built / TYPE-P |
| `d_state` to `J` | density | none | no square exists | would require new source class map | TYPE-U |
| `d_state` to `R` | density | none | no square exists | would require new bilocal map | TYPE-U |
| V007 exponent | `E_J direct-sum E_R` | scalar `Xi` | P2/W3 natural | `Tail_src={0}` | built, inputs unfilled by origin |
| finite tower sum | `E_src^k` | scalar partial sum | prefix exact | finite only | built conditionally on sources |
| no-added-source sum | zero element of `E_src^k` | zero | exact | no new class | built / TYPE-P |
| refreshed origin recurrence | no ratified domain | none | absent | new dynamical class | TYPE-U |

Door flags:

```text
DOOR_GEN_OMEGA_STATE_DESCENT = OPENED_UNCHANGED
DOOR_GERM_SOURCE_PORT = OPENED_UNCHANGED
DOOR_ORIGIN_TO_SOURCE_PORT = NOT_OPENED | TYPE-U
DOOR_TIER_REFRESH = NOT_OPENED | TYPE-U
DOOR_P2_COMPLETED_SOURCE = NOT_REOPENED
DOOR_INFINITE_TIER_COMPLETION = NOT_OPENED
DOOR_CONTINUUM_RESPONSE = NOT_OPENED
DOOR_BRIDGE = NOT_OPENED
```

No measure, contour, inter-tier carrier, continuum response, weak-star
completion, bidual, root, coupling, or physical value is introduced.

---

## 10. Final determination

The origin-fed tower separates into one completed and one missing half:

```text
COMPLETED_ORIGIN_HALF:
  rho_S,[A]=I_A/Tr_A(I_A),
  p_[A]=r_ch/(r_0+r_ch),
  weights=(1-p_[A],p_[A]) at every tier.

MISSING_SOURCE_HALF:
  no d_J, no d_R, no selected source sequence,
  no origin-determined S_Xi,k or D_k.
```

Consequently:

```text
ORIGIN_FED_TOWER_AS_NONZERO_SOURCE_TOWER = UNBUILT | TYPE-U

ORIGIN_SOURCE_FACTORISATION =
  A_k=(1-p_[A])+p_[A] exp(sum_t Xi[J_t,R_t]) | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014 as amended (2),
            DoR-015, C38 |
  scope: arbitrary independently supplied finite P2 source cylinder

NO_ADDED_SOURCE_BOUNDARY =
  A_k=1; Gamma_k=0; D_k=0; weights invariant | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014 as amended (2),
            DoR-015, C38

THEORY_INTRINSIC_K_DEPENDENCE = NO_VERDICT |
  reason: ratified origin fixes p but does not feed J/R

CONSTANT_NONZERO_ORIGIN_FEED = TYPE-U |
  missing: d_src

TIER_REFRESHED_ORIGIN_FEED = TYPE-U |
  missing: d_src plus next-tier update Upsilon
```

This is not another failed depth computation. It locates the exact boundary
of the ratified generative theory: **Gen_Omega generates the state that
weights the interference, but it does not generate the source history whose
accumulation would define depth.** The theory's require side is intrinsic;
its allow-side depth remains uninstantiated.

```text
REGISTER_HEAD_AT_START = Q-333
REGISTER_SHA256_AT_START =
  decccd564812a559ab052d009e00236a251163337302372a1cdff12042919922

FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-S
ALPHA_FACING_RESULT_PRODUCED = false | TYPE-S
COUPLING_OR_SCALE_EVALUATED = false | TYPE-S

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 11. Custody

This lane seals this lane-tagged artifact, verifies its sidecar, mirrors the
artifact and sidecar byte-identically, reports hashes, and stops. It does not
edit the register, governing plan, or tracker and performs no git, commit, or
push action.
