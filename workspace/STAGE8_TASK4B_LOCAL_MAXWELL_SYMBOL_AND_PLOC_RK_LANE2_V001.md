# STAGE 8 TASK 4B→5 — LOCAL MAXWELL SYMBOL AND `p_loc[R_K]` — LANE 2 V001

Date: 2026-08-03  
Custody: Codex Lane 2, derivation-first  
Register head verified before work: Q-398  
Status: structural derivation; no registration action taken

## Lead result

```text
P_LOC_RK = UNDERDETERMINED |
  exact fiber: the covariant normalized local-reading rules restricted to
  the R4-dressed R_K direction; normalization fixes p_loc[L_T]=1 but no
  ratified relation identifies R_K with L_T or places R_K in its complement

MAXWELL_SYMBOL = BLOCKED |
  the carrier-rank-one symbol is constructed exactly, but promotion to the
  local Maxwell symbol requires an unbuilt covariant spectral/long-wavelength
  symbol map sigma_loc on the completed R5 operator class

PUSHFORWARD = CONDITIONAL |
  on the S8-A exchange orbit it is controlled exactly by chi_K:=p_loc[R_K]
  with the R4 unit/reality dressing understood; at general rank it also
  consumes chi_x:=p_loc[x^flat tensor x^flat] on each covariant orbit
```

The decisive distinction is now proved.  DoR-019 forces the carrier metric,
its Riesz maps, and their unit classes.  It does **not** turn the carrier
Riesz map into the normalized Maxwell operator.  From the ratified geometry
one can construct, without choice, the algebraic carrier symbol

```text
P_x(v,w)=g_K(x,v)g_K(x,w),
H_x(v,w)=f(s)g_K(v,w)+2f_1(s)g_K(x,v)g_K(x,w),
s=g_K(x,x).
```

That object is quotient-compatible, covariant, restriction-natural on the
ratified W3 scope, reality-compatible, and already in the retarded CTP block.
What is absent is the map which says how this carrier bilinear decomposes
into the local Maxwell `F^2` symbol and the declared nonlocal/higher sector.
No branch below chooses that map.

```text
ALPHA_COMPUTED = false
PROOF_AUTHORIZED = false
KAPPA_RECORD_COMPUTED = false
REGISTERED_P_VERDICT = false
NUMERIC_RESPONSE_VALUE_EVALUATED = false
ROOT_OR_K_STAR_EVALUATED = false
```

---

## 0. Preflight, seals, and authority ledger

### 0.1 Locked process and register

The locked process was read before substantive work.

| Object | Verified SHA-256 | Use |
|---|---|---|
| `alpha_supervision/LOCKED_PROCESS.md` | `e8a4c00d3cd13126bd8d20588419aba344a50d27c6d084a8243ed5494d7721f2` | seal/mirror/report/stop discipline |
| `QUESTIONS_SETTLED_REGISTER_V001.md` at Q-398 | `ca342bb7791b58cd886410cbce4696416678ca3be38aa1448ba67613b05efcf6` | current head and reopen condition |

Preflight verdict:

```text
REGISTER_HEAD = Q-398 | PASS
NAMED_AUTHORITIES_PRESENT = true | PASS
AUTHORITY_HASHES_MATCH = true | PASS
PREFLIGHT = PASS
```

### 0.2 Load-bearing authorities

| Authority | Verified SHA-256 | Load-bearing content |
|---|---|---|
| `STAGE8_TASK4B_CONSUMPTION_VERIFICATION_AND_PUSHFORWARD_SWEEP_LANE1_V001.md` | `041498bb5a83d454212482412ab3fe0c609031f48f7adca94e34489f44bf5562` | exact S8-A reduction; coefficient/symbol residue |
| `STAGE8_TASK4B_P_LOC_CONSUMPTION_PATH_LANE2_V001.md` | `cacd317391759c1b1c6925c671be33cf4e91b7cccf4c3a529669dea6c18400fc` | completed R5 consumption path and exact reading-rule gap |
| `STAGE8_TASK4B_REPRESENTATIVE_INDEPENDENCE_LANE1_V001.md` | `f0f8b09b1aa6a16c0ed0dffedbd275aba9e647fb5841fc8ce06ce9e6a8b00857` | Q-396 witness family and rank-one profiles |
| `STAGE8_TASK4B_CARRIER_METRIC_AND_UNITS_PROPOSAL_LANE2_V005.md` | `2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961` | ratified `g_K`, `R_K`, quotient, units, R4 seam |
| `STAGE8_TASK4A_ACTION_COMPARISON_SQUARE_ADOPTION_PROPOSAL_LANE2_V004.md` | `abf6d366a5a7e375b9b53df75402f35d37f7c6a4b1bb0b10a44309ad3b0e1912` | completed R5 square, Hessian restrictions, covariance cube |
| DoR-016 network-sourcing decision | `b4157df6f327e261f40389d5a3011a0aef66ee0f198d8ebba8b1b9303142d708` | doubled CTP law and finite trace/tower scope |
| DoR-017 action-comparison decision | `ee9d81bf78ab0ac9361cad5b48dde2b6b8b1e9fb0e28a4fdbba41e1c43db3e45` | N member, square, R5 stationary package |
| DoR-019 carrier-metric decision | `6ab72b0cb3a93e123eb1d3c5088fc83361d86c6dc739f0a886380dbd2d143f1f` | metric/units ratification and authored completion scope |

The defining `p_loc` lineage cited by `cacd3173…` was reverified directly:

| Defining artifact | Verified SHA-256 | Clause used |
|---|---|---|
| `primitive_record_cell_selection_principle_v004.md` | `13d227ceb2198d96b0e4e2fef57b874cea71cb755320508fbf4c6d64a00c507e` | `p_loc[L_T]=1`, `Pi_loc=iota_loc compose p_loc`, completed response path |
| `primitive_zero_bare_induced_response_projection_principle_v004.md` | `d386bb74c28424a55a68a1bdb78108711537a7bc36ffffd1a76fe5ffd8a4eb80` | local `F^2` separation must be derived spectrally/at long wavelength |
| `alpha_complete_dimension_convention_ledger_v004.md` | `bbf2bdddfcefe851e985c4db03a62906082660af9a3c639d259afc93b4bbcc66` | action-kernel input and dimensionless scalar output |
| `alpha_symbolic_first_proof_gate_v003.md` | `2ec93961c2e764cc7218dd24608af42fc2b7db2c61e5bb9b52a383df502ccabd` | unique full-CTP projection remains a required derivation |

All named seals matched their contents.  Nothing was read from an unverified
named authority.

---

## 1. Register sweep before derivation

The questions-settled register was searched for `p_loc`, `local Maxwell`,
`coefficient`, `R_K`, `Riesz`, `rank-one`, `completion fiber`, `RetExtract`,
and `finite response`.  The following rows bear directly on this task.

| Entry | Settled content consumed here |
|---|---|
| Q-247 | separation is class-relative; no physical response class follows merely from a finite class |
| Q-251 | the possible tail contribution to `B_ind` is exactly `p_loc(t_ind)`; consumption was unspecified |
| Q-255 | `p_loc` is output-local but consumption-untyped in the sealed lineage |
| Q-279 | every finite probed retarded block is exactly zero and p-free; p occurs in noise/probe blocks |
| Q-288 | the R5 class-formation and stationary/Schur operations require explicit topology/tail accounting |
| Q-309 | finite kernel and kernel-mixing blocks are exactly zero, including probes |
| Q-314 | `p_loc` is background-agnostic, while its argument is the stationary completed response |
| Q-315 | finite restriction squares exist; source and physical tangent carriers may not be identified |
| Q-368 | exact completed Schur/RetExtract expression exists; finite retarded shadows remain zero |
| Q-391 | p-dependence reduces to the completed base Schur derivative before `p_loc` |
| Q-393 | Keldysh support is not decided by carrier type alone |
| Q-394 | the completed metric carrier selects no physical action representative |
| Q-395 | completed R5 is required by the live value path but not forced by finite record law |
| Q-396 | two admissible completions have equal finite shadows and unequal completed retarded operators |
| Q-397 | `p_loc` receives the completed operator; finite-factorization versus fiber detection is underdetermined |
| Q-398 | the S8-A pushforward reduces to `p_loc[R_K]`; the full fiber also needs the rank-one local Maxwell symbol |

No row defines `p_loc[R_K]`, a local-symbol functor on the R5 class, a trace
on response operators, or an identification `R_K=L_T`.  The present task
therefore has not been pre-solved.

---

## 2. Types and notation

For a physical realization `G`, write

```text
K_G       := the record-visible completed cycle carrier;
g_K,G     := the ratified positive carrier metric;
R_K,G     : K_G -> K_G^*,  (R_K,G x)(v)=g_K,G(x,v);
O_R5,G    := the completed physical retarded action-kernel class;
L_T,G     := the uniquely normalized transverse Maxwell kernel in O_R5,G;
p_loc,G   : O_R5,G -> Scalar_dimensionless.
```

The DoR-019 unit diagram is

```text
K_G[U_K] --R_K,G[U_K^(-2)]--> K_G^*[U_K^(-1)].  (T2-1)
```

Hence bare `R_K,G` is a same-sector carrier map, not by itself an action
kernel.  Q-396's expression uses it only after the ratified R4 action-unit
and reality transport.  To avoid an implicit conversion, define

```text
j_R4,G : U_action tensor Hom(K_G,K_G^*) -> O_R5,G,
Rhat_K,G := j_R4,G(u_action tensor R_K,G),         (T2-2)
```

where `u_action` denotes the unit **class**, not a selected unit
representative.  Similarly `Phat_x` below denotes the R4-dressed rank-one
operator.  In the established shorthand,

```text
p_loc[R_K] := p_loc(Rhat_K)                       (T2-3)
```

with unit and reality transport understood.  This artifact never applies
`p_loc` directly to an undressed carrier map.

```text
BARE_P_LOC_OF_R_K_WELL_TYPED = false
R4_DRESSED_P_LOC_OF_R_K_WELL_TYPED = true
IMPLICIT_CROSS_SECTOR_OR_UNIT_CONVERSION_USED = false
```

---

## 3. S1 — derivation-first determination of `p_loc[R_K]`

### 3.1 The live clauses, one by one

The ratified defining lineage supplies exactly:

```text
p_loc,G is linear;
p_loc,G is covariant;
p_loc,G[L_T,G]=1;
iota_loc(b)=b L_T,G;
Pi_loc=iota_loc compose p_loc;
Cod(p_loc,G)=dimensionless scalars;
the local F^2 term must be separated from nonlocal/higher terms by a
  derived covariant spectral/long-wavelength limit.              (S1-1)
```

The effect of each clause on `chi_K,G:=p_loc,G[Rhat_K,G]` is:

| Clause | What it forces | What it does not force |
|---|---|---|
| normalization | value `1` on `L_T` | any value on an operator not proved equal to `L_T` modulo the local-symbol kernel |
| linearity | the exact formulas in Sections 5–6 | a complement or a coefficient on `Rhat_K` |
| realization covariance | equal/transported values on one admitted orbit | the common value of that orbit |
| reality | the proper real/conjugate unit class of the value | zero, nonzero, or a normalization |
| R4-only unit seam | makes the dressed evaluation type-correct | an identification of K-sector Riesz and Maxwell operator units or tensors |
| locality | requires a future covariant local-symbol construction | a presently executable symbol calculus |
| DoR-008 | every completed answer must reproduce the finite shadows | a value on a direction whose every finite active restriction is zero |

Thus no live clause contains an equation with left-hand side `chi_K`.

### 3.2 Normalization theorem and its exact scope

Let

```text
P_adm(G):={ell:O_R5,G->Scalar |
  ell linear and covariant,
  ell[L_T,G]=1,
  ell obeys the ratified reality, unit, restriction, batching, and local
  interface obligations whenever those interfaces are instantiated}.
                                                               (S1-2)
```

For any `p_0 in P_adm(G)` and any lawful covariant linear functional
`delta` satisfying

```text
delta[L_T,G]=0,                                    (S1-3)
```

the map `p_0+delta` preserves normalization.  Therefore normalization is
unique on `span{L_T}` and nowhere else without an additional quotient or
direct-sum theorem.

On the two-direction test span generated by `L_T` and `Rhat_K`, the live
clauses allow the formal family

```text
p_chi(a L_T+b Rhat_K)=a+b chi,                    (S1-4)
```

for every covariance- and reality-compatible scalar `chi`, unless one of
the following missing relations is proved:

```text
Rhat_K=a_K L_T+R_perp with p_loc(R_perp)=0; or
Rhat_K lies in ker(sigma_loc); or
O_R5/span{L_T} has zero admitted covariant dual.   (S1-5)
```

No authority proves any line of `(S1-5)`.  Formula `(S1-4)` is not an
adoption of a functional; it is the countermodel family showing that the
listed algebraic clauses do not force `chi`.

If `Rhat_K` were later proved proportional to `L_T` in the physical local
symbol quotient, normalization would force the proportionality coefficient.
The ratified stack supplies neither that quotient relation nor its
coefficient.  Thus even the dependent-direction branch is not executable.

### 3.3 Covariance is an orbit equality, not an orbit value

For an admitted isometric realization automorphism `U:K_G->K_G'`, DoR-019
gives

```text
R_K,G' U=U^(-*) R_K,G.                            (S1-6)
```

The R5 covariance cube transports the dressed operator correspondingly.
Scalar covariance therefore yields

```text
chi_K,G'=chi_K,G                                  (S1-7)
```

after the simultaneous relabeling quotient.  Orientation reversal invokes
the ratified semilinear reality action and conjugates the appropriate unit
representative; it does not change the invariant scalar class.  Equation
`(S1-7)` proves family-natural equality.  It does not choose the equal
value.

This directly defeats the tempting inference

```text
automorphism invariant => zero.                  (S1-8)
```

Invariant scalars need not vanish.

### 3.4 Units do not make a coefficient map

DoR-019's Riesz maps and R4 seam type `Rhat_K` as an admissible retarded
action-kernel direction.  They do not supply:

```text
an operator ideal on O_R5;
a trace on that ideal;
a Hilbert-Schmidt or spectral pairing;
a nonzero normalization denominator;
a restriction/batching theorem for such a trace;
an identification of its coefficient with the Maxwell F^2 coefficient.
                                                               (S1-9)
```

Consequently

```text
Tr(R_K^(-1)H)/Tr(R_K^(-1)L_T)                    (S1-10)
```

is not a derived reading rule.  It adds every missing item in `(S1-9)` and
is excluded.

### 3.5 DoR-008 finite falsifier

The Q-396 direction has zero restriction in every Q-243/Q-279/Q-309 finite
active retarded block.  There is no sealed finite `p_loc,N` and no
coefficient commuting square.  Hence both symbolic assignments

```text
chi_K=0;                  chi_K!=0                (S1-11)
```

have the same presently checkable finite shadow.  DoR-008 rejects a future
rule which changes a finite shadow; it cannot select between assignments
which the finite consumer never evaluates.

This is a genuine underdetermination, not a failure to run an available
calculation.

### 3.6 Exact reading-rule fiber

Define the completed witness operator span

```text
W_Q396,G:=span{
  Rhat_K,G,
  Phat_x,G | x in K_G
}.                                                (S1-12)
```

The exact remaining reading-rule object is

```text
READING_RULE_FIBER_Q396
 := restrictions to W_Q396 of all normalized, covariant, reality-compatible,
    unit-correct, restriction/batching-compatible local-symbol functionals
    on O_R5.                                      (S1-13)
```

Its visible coordinates are

```text
chi_K,G :=p_loc,G[Rhat_K,G],
chi_[x],G:=p_loc,G[Phat_x,G],                     (S1-14)
```

with `chi_[Ux],G'=chi_[x],G`.  This is an interface/fiber, not an enumerated
set, because the required topology and local-symbol class on `O_R5` are
themselves absent.  A future ratification must instantiate those structures
before choosing any coordinate.

```text
P_LOC_RK = UNDERDETERMINED | TYPE-U
P_LOC_RK_FREEDOM = READING_RULE_FIBER_Q396
P_LOC_NORMALIZATION_FORCES_CHI_K = false | TYPE-R
P_LOC_COVARIANCE_FORCES_CHI_K_ZERO = false | TYPE-R
R4_UNITS_FORCE_CHI_K = false | TYPE-R
FINITE_FALSIFIER_FORCE_CHI_K = false | TYPE-R
```

---

## 4. S2 — the rank-one carrier symbol and the Maxwell-symbol stop

### 4.1 Choice-free construction on the ratified carrier

For `x in K_G`, define

```text
x^flat:=R_K,G x in K_G^*,
P_x:=x^flat tensor x^flat:K_G->K_G^*,
(P_x v)(w):=g_K,G(x,v)g_K,G(x,w).                (S2-1)
```

`P_x` is positive semidefinite, rank one when `x!=0`, even under `x->-x`,
and has image `span{x^flat}` and kernel `x^perp`.  No basis, frame,
orientation member, filtration, rank value, or carrier representative is
selected.

With the already fixed flat profile

```text
f(s)=exp(-1/s) for s>0,  f(0)=0,
f_1(s)=f(s)/s^2 for s>0,                          (S2-2)
```

the Q-396 rank-one law-side profile is

```text
H_x:=f(s)R_K,G+2f_1(s)P_x,
s:=g_K,G(x,x).                                    (S2-3)
```

Its exact carrier quadratic symbol is

```text
sigma_car(H_x)(v,w)
 :=f(s)g_K,G(v,w)
   +2f_1(s)g_K,G(x,v)g_K,G(x,w),                 (S2-4)
```

or, on one test direction `v`,

```text
sigma_car(H_x)(v)
 =f(s)||v||_K^2+2f_1(s)g_K,G(x,v)^2.             (S2-5)
```

Equations `(S2-1)`–`(S2-5)` are forced by the ratified metric and the
Q-396 Hessian.  They are not authored.

### 4.2 Quotient and record-visibility certificate

`K_G` is already the Gate-4/path-visible physical cycle quotient.  DoR-019
fullness proves

```text
ker(I_K,G)=0;                                     (S2-6)
```

hence every nonzero record-visible cycle has nonzero `g_K` norm and
`R_K,G` is an isomorphism.  Pendant/tree coboundaries are zero before
`(S2-1)` is formed.  Therefore

```text
x=[x'] in K_G => P_x=P_x';
x!=0 in K_G   => P_x!=0.                          (S2-7)
```

No record-visible cycle is deleted by the carrier-symbol construction.

### 4.3 Automorphism and reality covariance

Let `U:K_G->K_G'` be an admitted isometric automorphism or realization
transport.  From `(S1-6)`,

```text
(Ux)^flat=U^(-*)x^flat,
P_(Ux)=U^(-*)P_x U^(-1),
H_(Ux)=U^(-*)H_x U^(-1).                         (S2-8)
```

Thus

```text
sigma_car(H_(Ux))(Uv,Uw)=sigma_car(H_x)(v,w).    (S2-9)
```

For orientation reversal/reality, `U` is replaced by the ratified
antiunitary transport.  Because `P_x` is quadratic and `f(s),f_1(s)` are
real scalar functions, the profile acquires exactly the sealed conjugation
and sign action; no orientation is selected.

The S8-A exchange `Ue_1=e_2`, `Ue_2=e_1` therefore transports `P_(re_1)`
to `P_(re_2)` rather than fixing either member.  This is covariance, not
the forbidden cycle-member selection.

### 4.4 Restriction and zero-extension certificate

On the ratified W3 rank-preserving scope, let

```text
j_NM:K_N->K_M
```

be the isometric inclusion and `rho_MN=j_NM^*` its adjoint restriction.
Then

```text
j_NM^* R_K,M j_NM=R_K,N,
j_NM^* P_(j_NM x) j_NM=P_x,
j_NM^* H_(j_NM x) j_NM=H_x.                     (S2-10)
```

So the carrier symbol commutes with every rank-preserving restriction
square already ratified.  Identity zero-extension is the corresponding
special case and adds no cycle contribution.

For a cycle-creating extension there is no representative-independent
upward map from the old quotient onto every new cycle direction.  V003's
established discipline is retained:

```text
upward naturality on cycle-creating extensions = NOT CLAIMED;
contravariant restriction of an existing new-stage profile = lawful;
the newly created cycle receives its own R_K and P_x at the new stage.
                                                               (S2-11)
```

This prevents the old G7 overclaim from returning.

### 4.5 Batching and retarded-sector placement

DoR-016 batches systems as an ordered pair and forbids an unlicensed
amplitude product.  The Q-396 family is componentwise:

```text
H_(x_1,...,x_n)=direct-sum_i H_(x_i)              (S2-12)
```

on the ratified isometric direct-sum scope.  No cross-component trace or
normalization is added.

Q-396 forms `(S2-3)` **after** the stationary Schur reduction and
`RetExtract`; it occupies the ordered difference/common block

```text
<A_delta,Pi_R,ind A_c>.                           (S2-13)
```

Therefore it is a retarded input to `p_loc`.  It is not a noise-only block,
a tree direction, or an element already known to lie in
`ker(RetExtract)`.

### 4.6 Why the carrier symbol is not yet a local Maxwell symbol

The local Maxwell coefficient is defined by the `F^2` term, equivalently by
a covariant low-eigenvalue/long-wavelength separation normalized on `L_T`.
To turn `(S2-4)` into that physical symbol one still needs

```text
sigma_loc:O_R5 -> Scalar,
sigma_loc(L_T)=1,
O_R5 = span{L_T} plus a proved nonlocal/higher kernel,              (S2-14)
```

together with:

```text
a topology on the completed response-operator class;
a local spectral/cotangent or equivalent field-symbol realization;
the embedding of the cycle bilocal into that realization;
Ward/transversality and boundary/contact separation;
restriction, zero-extension, batching, covariance, and reality squares;
the R4 unit transport;
common-origin provenance for a restriction-invisible coefficient. (S2-15)
```

DoR-015 provides the physical field signature, DoR-016 the doubled CTP
network law, DoR-017 the action-comparison square, and DoR-019 the carrier
metric.  None supplies the arrow `(S2-14)` or the first three interfaces in
`(S2-15)`.  Contact support of `H_x` is insufficient: distinct local tensor
and higher-derivative structures may share contact support.

Accordingly, the exact result is

```text
CARRIER_RANK_ONE_SYMBOL = CONSTRUCTED | TYPE-P |
  premises: DoR-015/016/017/019 and Q-396

LOCAL_MAXWELL_SYMBOL = BLOCKED | TYPE-U |
  missing: P_LOC_R5_COVARIANT_LOCAL_SYMBOL_MAP
```

### 4.7 Choice table at the stop

No row is selected.

| Candidate continuation | Added physics/mathematics | Why not derived | Void condition |
|---|---|---|---|
| spectral/long-wavelength `sigma_loc` | topology, spectral limit, local `F^2` splitting | explicitly required but unbuilt in the projection principle | any target-dependent limit, failed Ward/contact/restriction square |
| identify `Rhat_K` with `L_T` | a carrier-to-Maxwell symbol isomorphism and normalization | no ratified seam relates the abstract Riesz map to `L_T` | unequal finite/physical tensor action or implicit unit conversion |
| metric-trace coefficient | response-operator ideal, trace and denominator | DoR-019 gives no operator trace | noncanonical trace, zero denominator, batching/restriction failure |
| finite-factorized reading | a coefficient square through all finite restrictions | the full operator identification is refuted; scalar factorization remains unproved | one completion-fiber witness with nonzero scalar image |
| annihilate the completion fiber | declaration `chi_K=chi_[x]=0` | finite silence is not a kernel theorem | chosen for the desired verdict or contradicted by derived local symbol |
| covariant reading-rule family | the full fiber `(S1-13)` | honest authored alternative, but not ratified | hidden member/frame/filtration choice or failure of any covariance cube |

The construction branch stops here, before any Maxwell coefficient is
assigned.

---

## 5. S3 — pushforward assembled as far as the derivation runs

### 5.1 General-stage formula

Q-396's completed response difference is

```text
h_i(x)
 =dot_omega_i mu_i
   [f(s)R_K+2f_1(s)x^flat tensor x^flat],
s=||x||_K^2.                                     (S3-1)
```

Here `p` enters only through the already derived symbolic
`dot_omega_i`; `mu_i` remains a symbolic action-unit/reality member.  It is
not identified with `nu`, and neither scale is fixed.

By linearity, the exact general pushforward is

```text
p_loc[h_i(x)]
 =dot_omega_i mu_i
   [f(s)chi_K+2f_1(s)chi_[x]],                   (S3-2)

chi_K:=p_loc[Rhat_K],
chi_[x]:=p_loc[Phat_x].
```

Covariance gives

```text
chi_[Ux]=chi_[x]                                  (S3-3)
```

with the appropriate reality conjugation.  Equations `(S3-2)`–`(S3-3)`
are the maximal general-stage result.

### 5.2 Rank-zero/tree stage

For a connected tree,

```text
K_G=ker(B_G^T)={0}.                               (S3-4)
```

There is no nonzero `x`, `P_x`, or `H_x`; the pushforward of this fiber is
zero before `p_loc`.  Open-path access remains upstream endpoint-covariant
content and is not relabeled as a scalar cycle response.

### 5.3 Reciprocal-loop rank-one stage

Choose a temporary unit vector `e` only to compute the invariant statement,
and write `x=r e`, `s=r^2`.  In one cycle dimension,

```text
P_x=s R_K.                                        (S3-5)
```

Hence

```text
p_loc[h_i(x)]
 =dot_omega_i mu_i
   [f(s)+2s f_1(s)]chi_K.                        (S3-6)
```

The temporary frame disappears from `(S3-6)`.  The expression is
conditional on `chi_K`; no scalar is evaluated.

### 5.4 S8-A exchange orbit

Let `e_1,e_2` be a temporary orthonormal frame exchanged by the admitted
rank-two realization automorphism, and let `x_j=r e_j`.  The basis-free
orbit identity is

```text
P_(x_1)+P_(x_2)=r^2 R_K.                         (S3-7)
```

For

```text
H_j=f(r^2)R_K+2f_1(r^2)P_(x_j),                  (S3-8)
```

linearity and covariance yield

```text
p_loc(H_1)=p_loc(H_2)
 =[f(r^2)+r^2 f_1(r^2)]chi_K.                    (S3-9)
```

Restoring the symbolic source/action coefficient gives the exact requested
pushforward:

```text
p_loc[h_i(r e_1)]=p_loc[h_i(r e_2)]
 =dot_omega_i mu_i
   [f(r^2)+r^2 f_1(r^2)]chi_K.                   (S3-10)
```

This reproduces the Q-398 reduction exactly.  The coefficient in brackets
is structurally nonzero for `r!=0`; whether `(S3-10)` vanishes is therefore
exactly the unresolved `chi_K` question.

### 5.5 Classification of the pushforward

The alternatives are now exact:

```text
S8-A:
  chi_K=0     => exchange-orbit pushforward ANNIHILATED;
  chi_K!=0    => exchange-orbit pushforward DETECTED.

GENERAL STAGE:
  f(s)chi_K+2f_1(s)chi_[x]=0 for every admitted x
                => full Q-396 fiber ANNIHILATED;
  the bracket is nonzero for at least one admitted x
                => completion choice DETECTED;
  absent sigma_loc and its kernel theorem
                => CONDITIONAL on READING_RULE_FIBER_Q396.       (S3-11)
```

The present ratified stack realizes the third line.  No branch is promoted
to the registered p-verdict.

```text
PUSHFORWARD_S8A = CONDITIONAL_ON_CHI_K | TYPE-U
PUSHFORWARD_GENERAL = CONDITIONAL_ON_READING_RULE_FIBER_Q396 | TYPE-U
FIXED_POINT_FIBER_BLIND = NO_VERDICT
COMPLETION_CHOICE_INSIDE_ALPHA = NO_VERDICT
```

---

## 6. S4 — finite checks, regressions, and anti-tuning ledger

### 6.1 Falsifier and regression table

| Check | Exact execution | Verdict |
|---|---|---|
| one-edge/tree | `K_G=0`; no scalar cycle profile is formed | PASS |
| reciprocal loop | rank-one identity `(S3-5)` gives `(S3-6)` | PASS, conditional on `chi_K` |
| S8-A exchange | orbit sum `(S3-7)` and covariance give `(S3-10)` | PASS |
| rank-two cycle-selective member | individual coordinate is transported, not selected; only orbit equality is used | PASS |
| pendant/tree quotient | pendant coboundary is zero before `R_K` and `P_x` are formed | PASS |
| DoR-008 finite restriction | every Q-396 fiber direction restricts to the exact Q-243/Q-279/Q-309 retarded zero | PASS |
| reality/orientation reversal | `P_x` is quadratic; antiunitary transport gives the sealed conjugation rule | PASS |
| batching | componentwise direct sum only; no amplitude product or trace is introduced | PASS |
| identity zero-extension | W3 pullback in `(S2-10)` returns the old profile exactly | PASS |
| cycle-creating extension | no upward naturality claimed; new cycle receives a new-stage profile and restricts contravariantly | PASS |
| R4 units | `p_loc` sees only `R4`-dressed operators; bare `R_K` is never consumed | PASS |
| hidden trace | candidate `(S1-10)` rejected for missing ideal/trace/normalization | PASS |
| finite-zero overreach | finite zero is not promoted to `chi_K=0` | PASS |
| response-support tuning | neither annihilating nor detecting symbol is selected | PASS |

### 6.2 Hostile attacks

1. **Normalization attack:** infer `p_loc[R_K]=1` from `p_loc[L_T]=1`.
   Killed: no `Rhat_K=L_T` theorem exists.

2. **Riesz-is-Maxwell attack:** call the metric Riesz isomorphism the
   Maxwell kernel because both are nondegenerate bilinears.  Killed: they
   live in different provenances and no local field-symbol arrow relates
   them.

3. **Covariance-annihilation attack:** use the rank-two exchange to force an
   invariant scalar to zero.  Killed by `(S3-7)`–`(S3-10)`: the orbit sum is
   a nonzero invariant `R_K` component.

4. **Trace shortcut attack:** use `(S1-10)` as the coefficient.  Killed by
   the missing structures in `(S1-9)`.

5. **Contact-equals-Maxwell attack:** declare every contact-supported
   retarded bilinear proportional to `L_T`.  Killed: contact support does
   not separate `F^2` from other local/higher tensor structures.

6. **Finite-silence attack:** conclude annihilation from exact finite
   zeros.  Killed: Q-396 is precisely a nonzero restriction-invisible
   completed operator, and no finite coefficient square exists.

7. **Fresh attack — metric-principal-symbol substitution:** treat
   `(S2-4)` as a spacetime cotangent principal symbol merely because it is a
   quadratic form.  Killed: `(S2-4)` is a symbol on the abstract cycle
   carrier; the field-local spectral/cotangent map in `(S2-14)`–`(S2-15)`
   is missing.  This is the exact category error the commission was meant
   to expose.

8. **Outcome-tuning attack:** choose `chi_K=0` because it annihilates the
   fiber, or choose `chi_K!=0` because it detects it.  Killed: the choice
   table is disclosed and no row is selected.

### 6.3 Anti-tuning order of construction

```text
1. Lock authority hashes and Q-398 scope.
2. Extract p_loc's normalization/covariance/unit/locality clauses.
3. Extract DoR-019's R_K and unit typing.
4. Construct P_x, H_x, and sigma_car from those inputs only.
5. Prove quotient/covariance/restriction/reality properties.
6. Test whether a ratified sigma_loc identifies the carrier symbol with L_T.
7. Only after the test fails, apply an abstract p_loc to derive (S3-2).
8. Only after that, compute the reciprocal-loop and S8-A reductions.
```

No desired annihilation/detection outcome appears before Step 8.  Neither
`p`, `nu`, a rank pair, a ratio, an orientation, a frame, a filtration, nor
a response representative was selected.

### 6.4 Operation accounting

| Operation | Domain → image | Kernel/image disclosure | Sector transfer | Restriction square | Tail/completion action | Status |
|---|---|---|---|---|---|---|
| `R_K` | `K_G→K_G*` | kernel zero by fullness; image full dual | same K sector | W3 adjoint square `(S2-10)` | extends by ratified DoR-019 completion | TYPE-P |
| `x↦P_x` | `K_G→Hom(K_G,K_G*)` | even map; `P_x=0 iff x=0`; operator kernel `x^perp` | same K sector | pullback in `(S2-10)` | no new tail; formed on completed `x` | TYPE-P |
| `x↦H_x` | completed K carrier → retarded K/K block | nonzero for `x!=0`; exact form `(S2-3)` | placed in ordered `(delta,c)` block | finite restrictions zero for Q-396 pair | carries the known completed fiber | TYPE-P on Q-396 premises |
| `sigma_car` | carrier bilinear → carrier quadratic form | faithful on the displayed bilinear | none | covariant pullback | does not create a spacetime symbol | TYPE-P |
| `sigma_loc/p_loc` | completed retarded operator → dimensionless scalar | kernel unknown on `W_Q396` | retarded operator to scalar Maxwell coefficient | no finite coefficient square | may annihilate or detect the completion fiber | TYPE-U |
| fixed-point pushforward | `p_loc[h_i(x)]` → scalar dependence input | formula `(S3-2)`; kernel conditional | scalar consumer | finite shadows all zero | exactly reading-rule dependent | TYPE-U |

No operation is silently upgraded from carrier-symbol construction to
Maxwell-symbol construction.

---

## 7. Exact open interfaces

### Door LM-1 — completed local-symbol map

```text
input:
  completed R5 physical retarded operator with its CTP, unit, boundary,
  Ward, and restriction data

output:
  normalized dimensionless coefficient of L_T

certificate:
  sigma_loc(L_T)=1;
  target independence;
  covariant spectral/long-wavelength construction;
  local F^2 versus nonlocal/higher separation;
  continuity on a named topology;
  reality, automorphism, restriction, batching, and zero-extension squares;
  kernel on W_Q396;
  common-origin provenance for restriction-invisible content.

standing:
  P_LOC_R5_COVARIANT_LOCAL_SYMBOL_MAP = NOT_BUILT / TYPE-U
```

### Door LM-2 — carrier-to-field symbol seam

```text
input:
  sigma_car(H_x) on K_cycle

output:
  the physical local differential/spectral symbol on which L_T is normalized

missing:
  a ratified map identifying carrier covectors with the appropriate physical
  field-symbol variables, with Ward/contact/boundary and unit certificates

standing:
  CARRIER_TO_LOCAL_MAXWELL_SYMBOL_SEAM = NOT_BUILT / TYPE-U
```

LM-2 is a necessary part of LM-1 on the Q-396 fiber; it is not supplied by
the carrier metric itself.

---

## 8. Final result board

```text
PREFLIGHT = PASS
REGISTER_SWEEP = COMPLETE_THROUGH_Q398

R_K_METRIC_OPERATOR = DERIVED_AND_RATIFIED
R_K_FULLNESS = true | TYPE-P
R_K_RANK_PRESERVING_ISOMETRY = true | TYPE-P
R4_UNIT_DRESSING = RATIFIED

CARRIER_RANK_ONE_PROFILE = CONSTRUCTED | TYPE-P
CARRIER_RANK_ONE_SYMBOL = CONSTRUCTED | TYPE-P
CARRIER_SYMBOL_QUOTIENT_COMPATIBLE = true | TYPE-P
CARRIER_SYMBOL_AUTOMORPHISM_COVARIANT = true | TYPE-P
CARRIER_SYMBOL_W3_RESTRICTION_NATURAL = true | TYPE-P
CARRIER_SYMBOL_REALITY_COMPATIBLE = true | TYPE-P
CYCLE_CREATING_UPWARD_NATURALITY_CLAIMED = false

R_K_EQUALS_L_T = NO_VERDICT / TYPE-U
P_LOC_RK = UNDERDETERMINED / TYPE-U
P_LOC_RANK_ONE_PROFILE = UNDERDETERMINED / TYPE-U
LOCAL_MAXWELL_SYMBOL = BLOCKED / TYPE-U
READING_RULE_FIBER = READING_RULE_FIBER_Q396

S8A_PUSHFORWARD
 =dot_omega_i mu_i [f(r^2)+r^2 f_1(r^2)] chi_K
 | exact | symbolic

GENERAL_PUSHFORWARD
 =dot_omega_i mu_i [f(s)chi_K+2f_1(s)chi_[x]]
 | exact | symbolic

PUSHFORWARD = CONDITIONAL_ON_READING_RULE_FIBER_Q396
FIXED_POINT_FIBER_BLIND = NO_VERDICT
COMPLETION_CHOICE_INSIDE_ALPHA = NO_VERDICT

P_SELECTED = false
NU_SELECTED = false
RANK_OR_RATIO_SELECTED = false
ORIENTATION_OR_FRAME_SELECTED = false
FILTRATION_OR_MEMBER_SELECTED = false
NUMERIC_EVALUATION = false
REGISTER_ACTION_TAKEN = false
PLAN_OR_TRACKER_ACTION_TAKEN = false
GIT_COMMIT_OR_PUSH_ACTION_TAKEN = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The final coefficient layer therefore does **not** yet choose between
annihilation and detection.  It proves the complete carrier-side symbol,
reduces S8-A to one coefficient, and isolates the exact physics that a
future derivation or ratification must add: the covariant local Maxwell
reading rule on the completed R5 operator class.
