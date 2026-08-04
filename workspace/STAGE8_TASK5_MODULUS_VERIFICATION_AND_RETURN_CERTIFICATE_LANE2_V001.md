# STAGE 8 TASK 5 — MODULUS VERIFICATION AND RETURN CERTIFICATE — LANE 2 V001

Date: 2026-08-04  
Task: PASTE 482 / Task 5  
Lane: Codex Lane 2  
Custody: adversarial cross-verification plus forward interface typing

## Lead result

```text
BUILD = CONFIRMED |
  ambient Maxwell scalar line complete;
  reader boundedness confirmed memberwise on the enlarged (ell,n_ell)
  family; no common physical operator topology is thereby obtained

FACTORIZATION = CONFIRMED |
  reciprocal loop:
  q_loop=|p_loc[Rhat_K]| sup_(K in D)|a_loop(K,p,nu,I)|,
  with the zero-times-infinity case stated piecewise;
  S8-A retains additional covariant reader coordinates

RETURN_CERTIFICATE = CONSTRUCTIBLE |
  GLOBAL_STATIONARY_RETURN_REGULARITY_AND_COMMON_READER_CERT;
  its interface is forced and all input types exist, but nonemptiness,
  regularity bounds, self-map return, and the strict modulus result remain
  unproved/underdetermined
```

The reciprocal loop has a one-dimensional physical cycle carrier.  After
Schur reduction and retarded extraction, every scalar-`K` response derivative
there is therefore a unique multiple of the R4-dressed Riesz direction:

```text
J_loop(K)=a_loop(K,p,nu,I) Rhat_K.
```

For one fixed reader `ell`, linearity gives the factorization exactly.  No
hidden tensor direction survives at rank one.  At S8-A, by contrast, the
rank-two response space contains anisotropic/rank-one directions in addition
to `Rhat_K`; the full modulus consumes their covariant local-reader
coordinates as well.

The structural sweep finds only these constraints on
`chi_K:=p_loc[Rhat_K]`:

```text
dimensionless after the R4 unit dressing;
real/conjugation-compatible on the physical reality slice;
constant/covariant on admitted automorphism orbits;
normalized on L_T only, not on Rhat_K.
```

No ratified sign or magnitude bound `|chi_K|<=B` exists.

```text
ALPHA_COMPUTED = false
PROOF_AUTHORIZED = false
KAPPA_RECORD_COMPUTED = false
NUMERIC_EVALUATION = false
REGISTERED_VERDICT_WRITTEN = false
```

---

## 0. Preflight and authority ledger

### 0.1 Locked process, register, and reviewed artifact

The locked process was read in full.  The artifact under review and its seal
were hash-verified before its contents were read.

| Object | Verified SHA-256 | Verdict |
|---|---|---|
| `alpha_supervision/LOCKED_PROCESS.md` | `e8a4c00d3cd13126bd8d20588419aba344a50d27c6d084a8243ed5494d7721f2` | PASS |
| `QUESTIONS_SETTLED_REGISTER_V001.md` at Q-403 | `9c27c3365011f6bbf150990db52b574f40da71de2c71e7e496b305719d4f9d2d` | PASS |
| `STAGE8_TASK5_SCALAR_CARRIER_BUILD_AND_MODULUS_LANE1_V001.md` | `aebe708d2e7ba4b67e828976bd01eae2d5eec04afbb6a28f3f77f9dc8003fc97` | PASS; sidecar check OK |

```text
DOES_THE_OBJECT_EXIST = yes
IS_THE_VERSION_CURRENT = yes | Q-403
ARE_ITS_INPUTS_PRESENT = yes | for verification and interface typing
PREFLIGHT = PASS
```

### 0.2 Load-bearing authorities

| Authority | Verified SHA-256 | Use |
|---|---|---|
| Q-402 premise sweep | `feb84216103c5c86f5d53c6323d4bb4a6fbe26d6d2c849d0f89c66d8ba47d9f0` | four-premise ledger and scope precision |
| Q-401 conditional theorem | `88854f08966c15e6afbcb300c6151f59a169e2725c3d5a8643b653abfe3ddcb3` | Banach and sensitivity formulas |
| Q-400 coefficient result | `70dde1c0cb776abec4a61cac118d4edf1f4c75a1185a2e984dc341961d4b643c` | `chi_K`, rank-one readings, local-symbol gap |
| metric V005 / DoR-019 candidate | `2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961` | Riesz maps, carrier completion, units |
| DoR-019 decision | `6ab72b0cb3a93e123eb1d3c5088fc83361d86c6dc739f0a886380dbd2d143f1f` | ratified metric and completion scope |
| Q-397 consumption chain | `cacd317391759c1b1c6925c671be33cf4e91b7cccf4c3a529669dea6c18400fc` | completed response reception |
| Q-398 pushforward sweep | `041498bb5a83d454212482412ab3fe0c609031f48f7adca94e34489f44bf5562` | exact S8-A orbit formula |
| square V004 / DoR-017 candidate | `abf6d366a5a7e375b9b53df75402f35d37f7c6a4b1bb0b10a44309ad3b0e1912` | stationary, inverse, Schur, RetExtract, restrictions |
| Shape-K response computation | `27790d53b018a84f5f02e97f68e885de0ebb332735307ae0fa433322a6053189` | affine member term before total stationary pullback |
| germ V003 / DoR-018 candidate | `231bbd1d77c39a45249149b47f9bb543e7a748c67b477dfde1f245efecd4aa13` | Shape-K jets and `nu` homogeneity |
| DoR-008 decision | `d51a6d5c5bb0020a081cfd2adfb545b9f5ed86ce660d3feacadc5ef68140fb19` | finite restriction falsifier |

### 0.3 Register sweep

The register and authorities were searched for `Maxwell line`, `reader
boundedness`, `common topology`, `stationary return`, `reciprocal loop`,
`a_loop`, `modulus`, `p_loc[R_K]`, `normalization`, `S8-A`, `Shape K`, and
`nu`.  Bearing rows:

```text
Q-253  no finite B_ind or finite scalar reader exists;
Q-365  R5 restriction/covariance cube exists on generated Hessians;
Q-384  DoR-019 supplies C/K response geometry, not scalar-K dynamics;
Q-391  Shape-K response is base plus an explicit nu-linear member term;
Q-395  scalar fixed-point differentiation remains conditional;
Q-396  completion fibers can be finite-invisible and response-visible;
Q-397  p_loc receives the completed response but is uninstantiated;
Q-398  S8-A orbit evaluation reduces to chi_K;
Q-400  no local-symbol map or value/bound for chi_K is ratified;
Q-401  conditional Banach theorem;
Q-402  0/4 premises discharged, completeness/boundedness constructible;
Q-403  ambient carrier and memberwise reader build, reciprocal-loop
       factorization, global-return/regularity residue.
```

No later theorem supplies a common reader topology, a stationary-return map,
a uniform reader bound, a finite modulus, or a magnitude bound on `chi_K`.

---

## 1. Verdict table X1–X6

| Item | Verdict | Determination |
|---|---|---|
| X1 — carrier and reader build | **PASS_WITH_SCOPE** | scalar line complete; `||ell||=1` for each compatible `(ell,n_ell)` member; no common topology/uniform family bound |
| X2 — reciprocal factorization/S8-A | **PASS** | rank-one factor exact; S8-A adds non-Riesz covariant directions |
| X3 — obstruction/return certificate | **PASS** | obstruction genuine; exact certificate typed in Section 4 and constructible |
| X4 — structural bound on `|chi_K|` | **PASS** | units/reality/covariance constrain type and orbit behavior only; no magnitude bound |
| X5 — supremum factor | **PASS_WITH_SCOPE** | well-defined as an extended-real quantity only on a nonempty regular branch domain `D`, not yet on all `K_amb`; dependence localized |
| X6 — falsifiers/fresh attack | **PASS** | all standing regressions survive; `0·infinity` and family-topology attacks scoped explicitly |

---

## 2. X1 — completeness and memberwise boundedness

### 2.1 Scalar Maxwell line

The live coefficient maps are

```text
iota_loc:R_dimless->span_R{L_T},
iota_loc(a)=aL_T,
ell[L_T]=1,
ell compose iota_loc=Id.                           (X1-1)
```

With

```text
d_sc(a,b)=|a-b|,
d_M(aL_T,bL_T)=|a-b|,                             (X1-2)
```

`iota_loc` is an isometry.  Every Cauchy sequence in the ordinary real line
converges in the real line, hence both the ambient dimensionless scalar line
and `span_R{L_T}` are complete.

This construction uses only the physical reality slice and the normalized
Maxwell coordinate.  It does not identify scalar `K` with `K_cycle`, use a
C/K conversion, or prove that the physical positive saddle domain is closed.

```text
AMBIENT_SCALAR_CARRIER_COMPLETE = true | TYPE-P
PHYSICAL_STATIONARY_DOMAIN_COMPLETE = false_as_a_proven_claim
```

### 2.2 Reader norm recomputation

Fix an algebraic reader `ell:E_I->R` with `ell(L_T)=1`.  The splitting

```text
H=ell(H)L_T+k_H,
k_H:=H-ell(H)L_T in ker(ell)                     (X1-3)
```

is canonical once `ell` is the family member.  For one norm
`n_(I,ell)` on `ker(ell)`, define

```text
||H||_(I,ell)=|ell(H)|+n_(I,ell)(k_H).            (X1-4)
```

This is a norm: positivity follows because both summands vanishing implies
`ell(H)=0` and `k_H=H=0`; homogeneity and the triangle inequality follow
termwise.  Moreover

```text
|ell(H)|<=||H||_(I,ell),
||L_T||_(I,ell)=1,
therefore ||ell||_(I,ell)=1.                     (X1-5)
```

The bounded reader extends uniquely to the completion of `(E_I,||.||)`.
No numerical response quantity is evaluated by the structural equality
`||ell||=1`.

### 2.3 Exact family scope

The proof in `(X1-3)`–`(X1-5)` is memberwise on the enlarged family

```text
P_norm:={(I,ell,n_(I,ell)) |
  ell is a retained algebraic reader;
  n_(I,ell) is a compatible kernel norm}.         (X1-6)
```

Automorphisms/reality transport the entire triple; no `ell`, kernel norm,
basis, frame, or completion member is selected.  Therefore the no-selection
discipline passes.

The construction does **not** prove:

```text
one common norm on every E_I;
uniform equivalence of the member norms;
one uniform bound for all readers;
that every physical R5 response lies in every member completion. (X1-7)
```

Compatibility of `n_(I,ell)` with restrictions, batching, automorphisms,
and units is part of the admitted triple in `(X1-6)`.  It is not derived for
a common physical topology.  Thus `BUILT_FAMILY_WIDE` must be read as
"proved for every compatible normed member," not as "one topology has been
ratified family-wide."  The reviewed artifact states this boundary in its
fresh topology attack and next-interface section.

```text
MEMBERWISE_READER_BOUNDEDNESS = CONFIRMED | TYPE-P on P_norm
COMMON_PHYSICAL_READER_TOPOLOGY = NOT_BUILT / TYPE-U
FAMILY_UNIFORM_READER_BOUND = NOT_BUILT / TYPE-U
X1 = PASS_WITH_SCOPE
```

---

## 3. X2 — independent modulus factorization

### 3.1 True modulus on a regular branch

Fix one nonempty scalar domain `D`, one completion representative `I`, and
one fixed reader `ell`.  If

```text
H_I(K)=Pi_R,ind,I[G_(K,I)]
```

is differentiable in scalar `K` on an interval `D`, define

```text
J_I(K):=partial_K H_I(K)
       =RetExtract[partial_K^tot Schur_I(K)].      (X2-1)
```

The scalar modulus is

```text
q_true(I,ell,p,nu;D)
 =sup_(K in D)|ell[J_I(K)]|                      (X2-2)
```

under the C1/absolute-continuity hypothesis.  Without that regularity,
`(X2-2)` is a candidate derivative bound rather than an established equality
with the difference quotient.  This is exactly why the return certificate
is still required.

### 3.2 Reciprocal-loop dimension theorem

On the reciprocal two-edge loop, `dim K_cycle=1`.  Hence

```text
dim Hom(K_cycle,K_cycle^*)=1.                    (X2-3)
```

`R_K` is an isomorphism and spans this operator space.  The R4 action-unit
dressing preserves one-dimensionality.  Therefore there is one and only one
scalar coefficient `a_loop` such that

```text
J_loop(K)=a_loop(K,p,nu,I) Rhat_K.                (X2-4)
```

All inverse, contact, boundary, stationary-motion, Schur, and retarded
effects have already been assembled into `J_loop`; on a one-dimensional
source/target carrier none can create a second linear-map direction.  They
can only change `a_loop`.

DoR-019 makes `Rhat_K` fixed by the carrier realization `I`; it is not a
scalar-`K` response variable.  The reader `ell` is fixed along the branch.
Thus

```text
ell[J_loop(K)]=a_loop(K,p,nu,I) chi_K(I,ell),
chi_K(I,ell):=ell[Rhat_K].                        (X2-5)
```

Taking absolute values and the supremum yields

```text
q_loop
 =|chi_K| A_loop,
A_loop(p,nu,I;D):=sup_(K in D)|a_loop(K,p,nu,I)|. (X2-6)
```

No additive reader term is hidden in `(X2-6)`.

### 3.3 Extended-real precision

Until global regularity is proved, `A_loop` may be infinite.  The exact
factorization is therefore best written piecewise:

```text
chi_K=0:
  q_loop=0, because ell[J_loop(K)]=0 pointwise;

0<|chi_K|<infinity:
  q_loop=|chi_K| A_loop in [0,infinity].          (X2-7)
```

This avoids the ambiguous notation `0 times infinity`.  Every algebraic
reader returns a finite `chi_K` on `Rhat_K`; boundedness on a common physical
topology is a separate question.

### 3.4 S8-A and additional directions

At S8-A, `dim K_cycle>=2`, so `Hom(K_cycle,K_cycle^*)` contains more than
`span{R_K}`.  Decompose one derivative, only as a vector-space statement,

```text
J_S8A(K)=a_0(K)Rhat_K+J_perp(K),                 (X2-8)
```

where `J_perp` carries the remaining covariant orbit representations.  Then

```text
q_S8A
 =sup_(K in D)|a_0(K)chi_K+ell[J_perp(K)]|.      (X2-9)
```

Q-396/Q-400 exhibit rank-one coordinates inside the second term:

```text
chi_[x]:=ell[Phat_x],
ell[h_i(x)]
 =dot_omega_i mu_i
  [f(s)chi_K+2f_1(s)chi_[x]].                    (X2-10)
```

On the special exchange orbit, covariance and orbit averaging collapse the
displayed Q-396 variation to

```text
ell[h_i(r e_j)]
 =dot_omega_i mu_i
  [f(r^2)+r^2 f_1(r^2)]chi_K.                    (X2-11)
```

Equation `(X2-11)` is a p/completion variation of the response, not the full
scalar-`K` derivative `J_S8A`.  It cannot be substituted for `(X2-9)` absent
the stationary regularity and derivative-commutation theorem.

```text
RECIPROCAL_LOOP_HIDDEN_OPERATOR_DIRECTION = false | TYPE-R
RECIPROCAL_LOOP_FACTORIZATION = CONFIRMED
S8A_SINGLE_FACTOR_FACTORIZATION = false / TYPE-R at general rank
S8A_ADDITIONAL_READER_COORDINATES = chi_[x] and any further covariant
  local-symbol directions in J_perp
X2 = PASS
```

---

## 4. X3 — exact return/regularity certificate

### 4.1 Why the obstruction is genuine

The constructed scalar line proves only an ambient complete codomain.  The
member norm proves only that one algebraic reader is continuous on its own
completion.  Neither proves that

```text
K -> G_(K,I) -> H_I(K) -> ell[H_I(K)]            (X3-1)
```

is defined on a nonempty complete physical domain, returns to that domain,
or is Lipschitz there.

Finite trace/tower bounds do not control `(X3-1)`: the route includes an
anchored logarithm, derivatives, a stationary solve, a complement inverse,
Schur reduction, retarded extraction, and a local-symbol reader.  DoR-019's
carrier norm controls inputs to those operations, not their global scalar
return.

### 4.2 Typed certificate

```text
GLOBAL_STATIONARY_RETURN_REGULARITY_AND_COMMON_READER_CERT := {

  CARRIER:
    one target-independent nonempty closed/complete domain
    D subset K_amb, with its physical reality and sign rule;

  FAMILY:
    the full no-selection family of completion representatives I and
    retained readers ell; no rank/frame/orientation/member selected;

  COMMON_OPERATOR_HOME:
    one Banach response class O_phys containing H_I(D) for every admitted
    (I,ell), or a family of topologies with proved uniform equivalence;

  READER:
    each ell extends boundedly to O_phys, with a uniform symbolic bound
    when family sensitivity/contraction is claimed; normalization,
    covariance, reality, units, restriction, batching, and local-symbol
    obligations all pass;

  GLOBAL_STATIONARY_SOLVE:
    S_I:D->Crit_I exists for every K, is family-natural, and satisfies every
    source/metric/Gauss/record/boundary/glue stationarity equation;

  FULL_RESIDUAL:
    R_comp[G_(K,I)]=0 on the whole graph, not only after scalar projection;

  RETURN:
    B_(I,ell)(D) subset D;
    real-slice and required sign preservation;
    G_(B_(I,ell)(K),I) exists and satisfies the same full system;

  REGULARITY:
    S_I and H_I are C1/Lipschitz on D, inverse/reducing domains remain
    uniform, total scalar-K Schur jets exist, and RetExtract/ell commute
    with those derivatives;

  MODULUS:
    q_true or one certified upper bound is finite and its dependence on
    p, nu, I, ell, chi_K, and higher reader coordinates is explicit;

  RESTRICTIONS:
    DoR-008, Q-243/Q-279/Q-309, rho_H,N, W3, reality, batching,
    zero-extension, pendant/tree, reciprocal-loop, S8-A, and Q-396
    regressions pass at every K and after return.
}.                                                 (X3-2)
```

### 4.3 Classification

Every type consumed by `(X3-2)` exists: scalar line, R5 carriers, stationary
interface, Schur/RetExtract operations, reader interfaces, and finite
restrictions.  Therefore the certificate is a well-posed construction, not
an untyped request.

Its truth is not derivable from current ratified data.  The stationary map
may fail globally; the return may leave the domain; an inverse may become
singular; no common topology or uniform bound may exist.  Those possible
failures are outcomes of the construction, not reasons the interface is
undefined.

```text
RETURN_CERTIFICATE = CONSTRUCTIBLE | TYPE-U until built
RETURN_CERTIFICATE_DERIVED_NOW = false / TYPE-R
RETURN_CERTIFICATE_TRUTH = UNDETERMINED
STRICT_Q_RESULT_INSIDE_CERTIFICATE = UNDETERMINED
X3 = PASS
```

---

## 5. X4 — structural sweep on `|p_loc[R_K]|`

### 5.1 Ratified constraints

For

```text
chi_K(I,ell):=ell[Rhat_K],                        (X4-1)
```

the ratified stack proves:

| Clause | Consequence for `chi_K` |
|---|---|
| R4 units | `R_K` must be action-unit dressed before reading; the output is dimensionless |
| physical reality | `chi_K` lies in the appropriate real/conjugation-compatible scalar class |
| automorphism covariance | corresponding realization members have equal/transported `chi_K` |
| batching/restriction | any future physical reader must transport the coefficient lawfully |
| normalization | `ell[L_T]=1` only |

No clause identifies `Rhat_K` with `L_T`, makes `Pi_loc` orthogonal, declares
`ell` positive, or supplies an operator trace.

### 5.2 No ratified magnitude bound

Normalization on `L_T` cannot bound an independent operator direction.  On
the formal two-direction span, the algebraic family

```text
ell_t(aL_T+bRhat_K)=a+t b                         (X4-2)
```

preserves `ell_t[L_T]=1`; real `t` preserves the minimal reality condition,
and `Rhat_K` is an automorphism-invariant direction.  Q-400 uses this family
only as a forcing countermodel: the full physical topology and restriction
certificates remain unbuilt.  It therefore proves that the **listed clauses**
do not force a bound, while not claiming every `t` is an adopted reader.

The memberwise norm gives

```text
|chi_K|<=||Rhat_K||_(I,ell),                      (X4-3)
```

but by definition

```text
||Rhat_K||_(I,ell)
 =|chi_K|+n_(I,ell)(Rhat_K-chi_K L_T).            (X4-4)
```

Thus `(X4-3)` is tautological and reader-dependent.  It supplies no common
constant `B`.  In a future common topology one would have the conditional
bound

```text
|chi_K|<=M_ell ||Rhat_K||_O,                      (X4-5)
```

but neither factor is ratified uniformly.

```text
CHI_K_UNIT_CLASS = CONSTRAINED
CHI_K_REALITY_CLASS = CONSTRAINED
CHI_K_AUTOMORPHISM_ORBIT = CONSTRAINED
CHI_K_SIGN = UNDETERMINED / TYPE-U
CHI_K_MAGNITUDE_BOUND = NOT_RATIFIED / TYPE-U
CHI_K_NORMALIZED_TO_ONE = false / TYPE-R
STRUCTURAL_BOUND_COMBINABLE_WITH_Q = none currently
X4 = PASS
```

---

## 6. X5 — the supremum factor and `(p,nu)` dependence

### 6.1 Domain and well-definedness

The ambient carrier `K_amb=R` is built, but `a_loop(K,p,nu,I)` is not defined
on all of it.  It is defined only where a regular completed stationary branch
exists and the derivative in `(X2-1)` is lawful.

For a nonempty such domain `D`, define

```text
A_loop(p,nu,I;D)
 :=sup_(K in D)|a_loop(K,p,nu,I)| in [0,infinity]. (X5-1)
```

`(X5-1)` is a well-defined extended-real quantity.  It is finite only if the
return/regularity certificate supplies a global bound.  On the built ambient
line with no branch, `A_loop` is not yet an instantiated function or
supremum.

```text
SUP_FACTOR_ON_K_AMB = NOT_INSTANTIATED / TYPE-U
SUP_FACTOR_ON_NONEMPTY_REGULAR_D = WELL_DEFINED_EXTENDED_REAL | TYPE-P
SUP_FACTOR_FINITE = UNDETERMINED / TYPE-U
```

### 6.2 Symbolic p dependence

The ratified p port is

```text
p -> (omega(p),kappa(p))
  -> base stationary blocks
  -> stationary solve, Schur, RetExtract
  -> a_loop.                                      (X5-2)
```

No operation carries the rank pair beyond its forced scalar form `p`.
Therefore

```text
A_loop=A_loop(p,nu,I;D),                          (X5-3)
```

with all `p` dependence located in the base block/branch route `(X5-2)`.
The exact closed base stationary jets needed to simplify it are absent.

### 6.3 Symbolic `nu` dependence

Before the full stationary pullback, Shape K gives

```text
Schur_K(p,nu;k)
 =Schur_base(p;k)+nu T_K(k),                      (X5-4)
```

and `T_K` has no explicit p or `nu`.  Hence the direct response at fixed
carrier coordinate is affine in `nu`.

The total scalar-`K` derivative on a physical branch may also differentiate
the completed cycle/background coordinates.  Because the global stationary
return is unbuilt, those coordinates may depend on `(K,p,nu,I)`.  Thus the
maximal exact statement is

```text
a_loop
 = coefficient of Rhat_K in
   RetExtract[partial_K^tot{
     Schur_base(p;k_*(K,p,nu,I))
     +nu T_K(k_*(K,p,nu,I))
   }].                                            (X5-5)
```

If a future certificate proves the stationary carrier coordinate is
`nu`-independent, `(X5-5)` reduces to

```text
a_loop=a_base(K,p,I)+nu a_flat(K,p,I),            (X5-6)
```

and then, with

```text
A_base:=sup_D|a_base|,
A_flat:=sup_D|a_flat|,
```

one has the symbolic bounds

```text
|A_base-|nu|A_flat| <= A_loop
                    <= A_base+|nu|A_flat,         (X5-7)
```

whenever the suprema are finite.  Since the branch-independence premise is
not proved, `(X5-6)`–`(X5-7)` are correctly marked conditional and are not
used to decide `q<1`.

### 6.4 Completed freedom map

```text
q_loop=|chi_K(I,ell)| A_loop(p,nu,I;D).

reading-rule freedom  -> chi_K;
completion freedom    -> chi_K's transported member and A_loop through I;
p                      -> A_loop through base stationary blocks;
nu                     -> explicit Shape-K term plus any branch pullback;
physical domain        -> the supremum set D;
regularity choice      -> existence/finiteness of A_loop.          (X5-8)
```

No factor is assigned a value.  If `a_loop` vanishes identically, then
`q_loop=0` for every `chi_K`; the multiplicative appearance of `chi_K` does
not alone prove physical sensitivity.

```text
X5 = PASS_WITH_SCOPE
```

---

## 7. X6 — falsifiers and fresh attacks

### 7.1 Regression table

| Attack/check | Execution | Verdict |
|---|---|---|
| scalar `K` versus `K_cycle` | kept distinct in every formula | PASS |
| Maxwell-line completeness | ordinary Cauchy proof rerun | PASS |
| strict-positive domain | not called complete; zero boundary not declared physical | PASS |
| memberwise reader norm | norm and dual norm recomputed exactly | PASS_WITH_SCOPE |
| common-topology overclaim | explicitly remains in return certificate | PASS |
| reciprocal-loop hidden direction | killed by one-dimensional Hom space | PASS |
| S8-A over-factorization | rejected; `J_perp` and `chi_[x]` retained | PASS |
| finite-zero-implies-q-zero | rejected; no finite `p_loc,N` or `B_ind,N` | PASS |
| `ell[L_T]=1` implies `chi_K=1` | rejected | PASS |
| trace/tower bound implies modulus bound | rejected across stationary/inverse/reader route | PASS |
| real/sign return | required explicitly | PASS |
| full residual | `R_comp=0` required after return | PASS |
| identity zero-extension/restriction | no upward scalar map inferred | PASS |
| reality/batching/units | carried in common-reader/return interface | PASS |
| Q-396 witness | finite invisibility and completed visibility both retained | PASS |
| p/nu values | symbolic only | PASS |

### 7.2 Fresh attack one — `0 times infinity`

If `chi_K=0` while `A_loop=infinity`, the unqualified extended-real product
`|chi_K|A_loop` is ambiguous in some conventions.  Pointwise linearity
settles the physical expression: every `ell[J_loop(K)]` is zero, so
`q_loop=0`.  The piecewise formula `(X2-7)` repairs the notation without
changing the factorization.

### 7.3 Fresh attack two — topology-dependent contraction comparison

Each norm `(X1-4)` makes its own reader norm one.  It does **not** follow that
two moduli computed in two different member topologies are comparable or
that their common supremum has meaning.  A forgetting/sensitivity theorem
must consume one common topology or uniform equivalence constants.  This is
now an explicit clause of `(X3-2)`.

### 7.4 Fresh attack three — coefficient cancellation

Even nonzero `chi_K` does not imply nonzero `q_loop`: `a_loop` may vanish on
the whole branch.  Conversely, a large formal `chi_K` cannot prove failure
of contraction without a nonzero/finitely controlled `A_loop`.  The artifact
and this review retain this cancellation possibility.

### 7.5 Anti-tuning and fence scan

No reader, kernel norm, common topology, domain endpoint, completion member,
rank, frame, orientation, `chi_K`, `p`, `nu`, stationary branch, modulus, or
strict inequality is selected.  No structural result was blocked by a
fence.

```text
TARGET_TUNED_DOMAIN = false
TARGET_TUNED_TOPOLOGY = false
TARGET_TUNED_MODULUS = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false
X6 = PASS
```

---

## 8. Final determination

```text
X1_CARRIER_COMPLETENESS = PASS
X1_READER_BOUNDEDNESS = PASS_WITH_SCOPE |
  per compatible (ell,n_ell) member, not common/uniform

X2_RECIPROCAL_FACTORIZATION = PASS
X2_S8A_ADDITIONAL_DIRECTIONS = CONFIRMED

X3_GLOBAL_OBSTRUCTION = CONFIRMED
X3_CERTIFICATE_INTERFACE = X3-2

X4_CHI_K_TYPE_AND_COVARIANCE = CONSTRAINED
X4_CHI_K_MAGNITUDE_BOUND = NOT_RATIFIED / TYPE-U

X5_SUP_FACTOR = CONDITIONAL_EXTENDED_REAL_ON_REGULAR_D
X5_SUP_FACTOR_FINITE = UNDETERMINED / TYPE-U
X5_P_NU_DEPENDENCE = X5-2 through X5-8

BUILD = CONFIRMED
FACTORIZATION = CONFIRMED
RETURN_CERTIFICATE = CONSTRUCTIBLE |
  exact: GLOBAL_STATIONARY_RETURN_REGULARITY_AND_COMMON_READER_CERT (X3-2)

RETURN_CERTIFICATE_DERIVED = false
RETURN_CERTIFICATE_TRUTH = UNDETERMINED
Q_LT_1 = UNDETERMINED / TYPE-U

P_SELECTED = false
NU_SELECTED = false
CHI_K_SELECTED = false
READER_OR_NORM_MEMBER_SELECTED = false
COMPLETION_MEMBER_SELECTED = false
SCALAR_DOMAIN_SELECTED = false
NUMERIC_EVALUATION = false
REGISTER_ACTION_TAKEN = false
PLAN_OR_TRACKER_ACTION_TAKEN = false
GIT_COMMIT_OR_PUSH_ACTION_TAKEN = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The build therefore survives with its intended boundary.  The ambient
coefficient carrier and memberwise reader continuity are complete; the
physical fixed-point map is not.  The exact next object is the constructible
certificate `(X3-2)`, whose execution will decide whether the supremum is
finite, whether return holds, and whether any certified modulus is strictly
below one.
