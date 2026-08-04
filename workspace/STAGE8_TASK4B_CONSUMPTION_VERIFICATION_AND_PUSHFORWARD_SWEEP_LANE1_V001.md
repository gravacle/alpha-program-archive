# STAGE 8 TASK 4B TO 5 — CONSUMPTION VERIFICATION AND PUSHFORWARD SWEEP — LANE 1 V001

Date: 2026-08-03  
Task: PASTE 476 / Task 4b to 5  
Lane: CODEX LANE 1  
Custody: adversarial verification and derivability sweep; no registration authority

```text
REGISTER_HEAD_AT_PREFLIGHT = Q-397
PREFLIGHT = PASS

LEAD_RESULT = CONSUMPTION_CONFIRMED__PUSHFORWARD_REDUCED_BUT_NOT_EVALUABLE

CONSUMPTION_RESULT = CONFIRMED

PUSHFORWARD = NEEDS |
  P_LOC_R5_LOCAL_MAXWELL_SYMBOL_AND_Q396_FIBER_PUSHFORWARD_CERTIFICATE

EXACT_REDUCTION_ON_S8A_EXCHANGE_ORBIT =
  p_loc[h_i(r e_1)] = p_loc[h_i(r e_2)]
    = dot_omega_i mu_i [f(r^2)+r^2 f_1(r^2)] p_loc[R_K]
  with unit/reality transport understood and no coefficient evaluated

WITNESS_IS_IN_RETARDED_INPUT_SECTOR = true
WITNESS_IS_FORCED_IN_KERNEL_P_LOC_BY_SECTOR = false | TYPE-R
P_LOC_OF_R_K_FIXED_BY_RATIFIED_STRUCTURE = false | TYPE-U
P_LOC_COEFFICIENT_FUNCTIONAL_DERIVABLE = false | TYPE-U

REGISTERED_P_VERDICT_WRITTEN = false
NUMERIC_EVALUATION = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The Lane-2 consumption result survives.  The current live path applies
`p_loc` to the completed R5 retarded operator; no finite-stage substitute is
the definition.  The lineage nevertheless leaves the scalar coefficient map
uninstantiated.  Neither the carrier Riesz maps nor the R4-only unit seam is an
operator-space local-Maxwell projection.

The forward sweep narrows the remaining pushforward.  The Q-396 direction is
already in the ordered difference/common retarded block, so no Keldysh-sector
rule annihilates it.  On the rank-two S8-A exchange orbit, its orbit average is
a nonzero multiple of `R_K`.  Covariance therefore reduces the scalar question
on that minimal orbit to the one unbuilt coefficient `p_loc[R_K]` (with the
required action-unit and reality transport), rather than proving zero.  The
full fiber additionally requires the local symbol of its rank-one profiles.
The ratified stock supplies no
relation between the abstract carrier Riesz map `R_K` and the normalized
Maxwell operator `L_T`.  It consequently supplies neither a zero nor a nonzero
pushforward.

This is a strict narrowing of the named Q-397 certificate.  A future
certificate need not rediscover the R5 input stage, the Q-396 fiber, or its
Keldysh block.  It must construct the covariant spectral/long-wavelength
Maxwell-symbol map on the R5 operator class and evaluate that map on the
`R_K` orbit component.

---

## 0. Preflight, process, and authority ledger

### 0.1 Locked-process preflight

`alpha_supervision/LOCKED_PROCESS.md` was read before the artifact under
review.  The register and the reviewed artifact's sidecar verified before the
artifact was opened.

```text
DOES_THE_OBJECT_EXIST = yes |
  Q-397 names the consumption derivation and the forward certificate

IS_THE_VERSION_CURRENT = yes |
  register head Q-397 includes Q-396 and the Lane-2 consumption result

ARE_ITS_INPUTS_PRESENT = yes_for_review_and_derivability_sweep |
  the live p_loc lineage, R5 response class, Q-396 direction, carrier metric,
  finite restrictions, and standing falsifier are present

ARE_ITS_INPUTS_PRESENT_FOR_PUSHFORWARD_VALUE = no / TYPE-U |
  the R5 local-Maxwell symbol/coefficient map is not instantiated

PREFLIGHT = PASS
```

The live process file verified at
`e8a4c00d3cd13126bd8d20588419aba344a50d27c6d084a8243ed5494d7721f2`.
The register verified at preflight at
`81338881506323735074a9e07e58ba906b14d2cde25aa68cf291cc6ac0df36e8`.

### 0.2 Reviewed artifact

```text
artifact = STAGE8_TASK4B_P_LOC_CONSUMPTION_PATH_LANE2_V001.md
expected_sha256 = cacd317391759c1b1c6925c671be33cf4e91b7cccf4c3a529669dea6c18400fc
observed_sha256 = cacd317391759c1b1c6925c671be33cf4e91b7cccf4c3a529669dea6c18400fc
sidecar_check = OK
```

### 0.3 Hash-verified authorities

| Authority | Verified SHA-256 | Use |
|---|---|---|
| Q-396 representative witness | `f0f8b09b1aa6a16c0ed0dffedbd275aba9e647fb5841fc8ce06ce9e6a8b00857` | fiber direction and finite-flat certificates |
| Q-395 seam audit | `337769f4a122512de5c79a9fe4f936c4edac2170bfe3bc471484d4ff85724a34` | R5 response versus fixed-point scope |
| Q-253 B-ind input theorem | `790ae95bfa7f7747f383a387842939cb8f024d3e0107a9cbe15683666058c73f` | completed input and exact linear reduction |
| Q-255 complete p_loc lineage | `df2dbdccb25d5ee62e0de9051a8300c3933fb4c07250e765632d2f6247a6df45` | prior corpus-wide definition audit |
| square V004 / DoR-017 candidate | `abf6d366a5a7e375b9b53df75402f35d37f7c6a4b1bb0b10a44309ad3b0e1912` | R5 Schur and RetExtract implementation |
| metric V005 / DoR-019 candidate | `2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961` | `R_K`, carrier units, R4-only seam |
| live record-cell definition | `13d227ceb2198d96b0e4e2fef57b874cea71cb755320508fbf4c6d64a00c507e` | completed `Pi_R,ind -> p_loc -> B_ind` contract |
| live response-projection definition | `d386bb74c28424a55a68a1bdb78108711537a7bc36ffffd1a76fe5ffd8a4eb80` | spectral/long-wavelength local coefficient obligation |
| live global response spine | `74a1d6224ed402e7f6622e0d1c2fe00a4f4311fba2897d7e162930e807b9573a` | global-kernel and probe-restriction typing |
| live dimension ledger | `bbf2bdddfcefe851e985c4db03a62906082660af9a3c639d259afc93b4bbcc66` | domain, codomain, and unit signature |
| live symbolic proof gate | `2ec93961c2e764cc7218dd24608af42fc2b7db2c61e5bb9b52a383df502ccabd` | unique projector remains a required derivation |
| DoR-008 | `d51a6d5c5bb0020a081cfd2adfb545b9f5ed86ce660d3feacadc5ef68140fb19` | finite-restriction falsifier and limit caveat |
| DoR-017 | `ee9d81bf78ab0ac9361cad5b48dde2b6b8b1e9fb0e28a4fdbba41e1c43db3e45` | ratified R5 stationary response package |
| DoR-019 | `6ab72b0cb3a93e123eb1d3c5088fc83361d86c6dc739f0a886380dbd2d143f1f` | ratified carrier metric and unit package |

### 0.4 Register sweep

The questions-settled register was searched for `p_loc`, coefficient
functional, local projector, `Pi_R,ind`, finite factorization, tail,
completion fiber, R5 response, and fixed-point consumption.  The bearing
entries were:

```text
Q-247   separation is class-relative; no physical p_loc class follows;
Q-251   the possible scalar tail term is exactly p_loc(t_ind);
Q-253   the B_ind input is completed and tail-blindness is equivalent to
        p_loc restricted to Tail_ind being zero;
Q-255   the complete definition lineage leaves input consumption unspecified;
Q-283   an independently authored tail functional is excluded; a generated
        completed action remains possible only with provenance;
Q-285   weak-star completion is a mathematical creator, not silently physical;
Q-288   every class-formation topology must be declared;
Q-314   p_loc is background-agnostic while its argument is stationary/on-shell;
Q-365-Q-368
        the R5 Hessian, restriction cube, Schur, and RetExtract are in force;
Q-384   the carrier metric and R4-only unit seam are in force;
Q-391-Q-393
        the operator p-derivative and exact RetExtract kernel are known;
Q-394   finite shadows do not select the completed base action;
Q-395   p_loc[X_p], not X_p alone, is the registered map-level criterion;
Q-396   X_p varies along an admissible completed fiber;
Q-397   completed reception is fixed and the coefficient/pushforward
        certificate is named.
```

No row defines `p_loc[R_K]`, identifies `R_K` with `L_T`, or supplies an
operator-space trace, local-symbol map, finite coefficient square, or
restriction factorization.

### 0.5 Complete defining-lineage recheck

The active parent root was searched independently for exact `p_loc` hits.
The six paired lineages and their supersession status agree with Q-255:

```text
alpha_complete_dimension_convention_ledger_v003/v004;
alpha_post_cleanroom_route_state_v001/v002;
alpha_surface_symbolic_spine_v003/v004;
alpha_symbolic_first_proof_gate_v002/v003;
primitive_record_cell_selection_principle_v003/v004;
primitive_zero_bare_induced_response_projection_principle_v003/v004.
```

The live versions specify only:

```text
Dom(p_loc) = physical retarded action kernels;
Cod(p_loc) = dimensionless scalars;
p_loc is linear and covariant;
p_loc[L_T]=1;
Pi_loc=iota_loc compose p_loc;
the complete kernel must derive a unique full-CTP projection;
local F^2 must be separated from nonlocal/higher-derivative terms by a
derived covariant spectral/long-wavelength limit.
```

They do not specify a formula, topology, operator dual, trace, integral
pairing, restriction square, kernel, or coefficient on `R_K`.  The one older
source-germ V001 statement that imposed finite factorization was
`PROPOSED_NOT_ADOPTED` and self-killed at B14; the later germ V004 retained
B9 as `CONDITIONAL / TYPE-U`.  It is not a ratified `p_loc` definition.

An independent exact-word and semantic search was also run across the full
cleanroom root and archive workspace.  The bearing post-definition artifacts
were the currency audit, response-operator correspondence, dimension and
sector audits, raw-correlator map spec, Q-251/Q-253/Q-255 determinations, P7,
the P5 accounting packages, the background/stationarity audits, the
complement-scoped inverse audit, Q-395, Q-396, and the artifact under review.
Each either restates the live signature, types `p_loc` downstream of the
completed response, or records the same missing factorization/pairing.  No
artifact supplies an executable evaluation semantics.  In particular:

```text
finite scalarization flags in the raw-correlator spec != p_loc;
source-germ continuity language in killed V001 != ratified consumer rule;
DoR-019 carrier Riesz maps != operator coefficient pairing;
Q-393 RetExtract kernel != p_loc kernel;
Q-396 nonzero operator direction != nonzero scalar pushforward.
```

---

## 1. Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| R1 reception claim | **PASS** | the live value path and ratified R5 architecture feed the completed Schur/RetExtract operator into the `Pi_R,ind[G_K]` role before `p_loc` |
| R2 underdetermination | **PASS** | every live definition fixes the role and normalization but no coefficient formula, operator dual, or finite factorization |
| R3 full identification refutation | **PASS** | Q-396's flat deformation has all finite active jets zero yet a nonzero completed ordered block |
| R4(a) coefficient derivability | **PASS: NOT DERIVABLE / TYPE-U** | localization, covariance, units, and DoR-008 leave the quotient-dual coefficient free |
| R4(b) fiber pushforward | **PASS: NEEDS EXACT CERTIFICATE** | the witness is not sector-annihilated; the minimal exchange orbit reduces to `p_loc[R_K]`, while the full rank-one profile remains untyped |
| R5 falsifiers and fresh attack | **PASS** | finite regressions agree; the rank-two exchange-orbit attack rules out covariance as a zero proof but does not invent a detector |

---

## 2. R1 — the reception claim

### 2.1 Live definition

The active record-cell principle states at lines 127-155:

```text
G_K is a candidate normalized saddle;
H_R[G_K]=K L_T+declared higher/nonlocal structures;
p_loc[L_T]=1;
B_ind(K)=p_loc[Pi_R,ind[G_K]].                    (R1-1)
```

Lines 149-150 require the complete operator to derive the projection and its
extension to every physical CTP block.  The dimension ledger types

```text
p_loc: physical retarded action kernels -> dimensionless scalars. (R1-2)
```

The induced-response principle lines 81-100 starts coefficient extraction
only after the **complete induced kernel** and its low-eigenvalue derivative
expansion exist.  The symbolic spine lines 69-84 makes the unrestricted
global retarded kernel primary and calls `D x D` only a probe restriction.

### 2.2 R5 implementation chain

DoR-017 ratifies R5's critical family, completed Hessian blocks, reducing
complement inverse, Schur operator, restriction cube, and retarded extraction.
The current architecture is therefore

```text
Gamma_m on D_017
  -> Crit_m and G_star,m
  -> H_CC,H_CK,H_KC,H_KK
  -> Schur_m=H_KK-H_KC Inv_CC H_CK
  -> Response_R5,m=RetExtract_m(Schur_m)
  -> Pi_R,ind[G_K] role
  -> p_loc
  -> B_ind(K).                                    (R1-3)
```

The Q-243/Q-279/Q-309 responses are restriction targets for `(R1-3)`, not an
alternate finite definition of `B_ind`.

```text
R1 = PASS
P_LOC_RECEIVES_COMPLETED_R5_OPERATOR = true |
  current ratified R5 value-path architecture
P_LOC_RECEIVES_ONLY_A_FINITE_SHADOW = false / TYPE-R
```

This is not a claim that finite record law forced R5.  Q-395 correctly types
R5 as the current authored-and-ratified implementation required by the live
value path.

---

## 3. R2 — independent underdetermination sweep

### 3.1 What normalization proves

Let `O_R5` be the completed physical retarded-operator class.  The explicit
algebraic requirements are

```text
p_loc in O_R5^*;
p_loc is covariant and linear;
p_loc[L_T]=1.                                    (R2-1)
```

Equation `(R2-1)` proves that `Pi_loc=iota_loc p_loc` is a retraction onto
`span{L_T}`.  It fixes no value on a complementary operator direction.

If one such functional `p_0` exists and `ell` is a covariant linear
functional satisfying `ell(L_T)=0`, then

```text
p_ell:=p_0+ell;
p_ell[L_T]=1.                                    (R2-2)
```

The live domain explicitly includes nonlocal and higher-derivative
structures, so it is not declared one-dimensional.  No theorem says the
covariant dual of `O_R5/span{L_T}` is zero.

### 3.2 Localization does not finish the map

The live projection principle requires a **derived** covariant
spectral/long-wavelength separation of the local `F^2` tensor.  That sentence
is an interface, not an executable symbol calculus.  The corpus has no map

```text
sigma_loc:O_R5 -> coefficient of L_T               (R2-3)
```

and no declared direct sum

```text
O_R5=span{L_T} direct-sum O_nonlocal/higher.        (R2-4)
```

Without `(R2-3)` or `(R2-4)`, the word `local`, contact support, and low
eigenvalue language cannot assign a scalar to a completed R5 operator.

### 3.3 Covariance does not imply uniqueness

Covariance requires an invariant scalar on each automorphism orbit.  It does
not prove that the invariant dual space is one-dimensional.  In particular,
the rank-two computation in Section 5 exhibits a nonzero invariant component
of the Q-396 orbit.  A covariance theorem may identify equal values on orbit
members; it does not make that common value zero.

### 3.4 R4-only units do not define an operator pairing

DoR-019 supplies

```text
R_K:K_cycle->K_cycle^*;
R_C:C_prop->C_prop^*;
H_CK,H_KC and compositions through Inv_CC as the exhaustive R4 mixing set.
                                                               (R2-5)
```

These maps type Hessian blocks and the Schur expression.  They do not supply
a trace or Hilbert-Schmidt pairing on `Hom(K_cycle,K_cycle^*)`; they also do
not identify `R_K` with the physical Maxwell operator `L_T`.  Using
`Tr(R_K^{-1}H)` would add, at minimum, an operator ideal/domain, a trace,
normalization, completion theorem, and batching/restriction certificates.

```text
DOR019_RIESZ_MAP_IS_P_LOC = false / TYPE-R
R4_UNIT_SEAM_FIXES_P_LOC = false / TYPE-R
R_K_EQUALS_L_T = NO_VERDICT / TYPE-U
```

### 3.5 DoR-008 applied to the scalar consumer

DoR-008 requires every completed framework to reproduce every sealed finite
result on restriction.  It expressly leaves `B_ind` convergence as a
limit-only theorem.  There is no sealed finite `p_loc,N`, no commuting
coefficient square, no finite `B_ind` value, and no finite fixed-point root.

For the Q-396 direction `h`, every finite active restriction is zero.  Thus
both assignments

```text
p_loc(h)=0;
p_loc(h)=nonzero                                  (R2-6)
```

are transparent to the current finite restriction table.  A future nonzero
assignment still owes physical provenance and every battery certificate; the
falsifier does not create that provenance.  A future zero assignment still
owes the factorization or local-symbol theorem; finite silence does not prove
it.

The suggestion that a completion-dependent fixed point must already have a
sealed finite consequence fails for the same reason: the corpus contains no
finite fixed-point consumer to compare.  The scalar is first formed only
after `(R1-3)` reaches the completed layer.

```text
DOR008_FORCES_P_LOC_FINITE_FACTORING = false / TYPE-R
DOR008_FORCES_P_LOC_FIBER_DETECTION = false / TYPE-R
FINITE_FIXED_POINT_FALSIFIER_EXISTS = false / TYPE-S
```

### 3.6 R2 conclusion

```text
R2 = PASS
P_LOC_COEFFICIENT_FUNCTIONAL_DERIVABLE = false / TYPE-U |
  would-build: (R2-3), (R2-4), operator topology/dual, normalization,
  covariance/reality/batching/restriction squares, and full-CTP extension
```

---

## 4. R3 — the full finite/completed identification is refuted

Let `I_0` be an admitted R5 completion and let Q-396's target-blind flat
deformation be

```text
Psi_(a,b,d)(p;c,k)
 =sum_i omega_i(p_i) f(s_K(k_i)) q_(a_i,b_i,d_i)(k_i),

f(s)=exp(-1/s) for s>0 and f(0)=0.                (R3-1)
```

At every finite active section `S_N`, `k_N=0`; smooth flatness gives

```text
D^m Psi_N|S_N=0 for every finite m.              (R3-2)
```

Therefore `I_0` and

```text
I_mu=I_0+Psi_(0,mu,0)                            (R3-3)
```

have identical Q-243/Q-279/Q-309 restrictions, including all sealed ordered
retarded zeros.

At a completed nonzero common-cycle direction `x`, however,

```text
h_i(x)
 :=X_p[I_mu](x,0)-X_p[I_0](x,0)

 =dot_omega_i mu_i
   [f(s)R_K+2 f_1(s)x^flat tensor x^flat],
s=||x||_K^2,
x^flat=R_K x,
f_1(s)=f(s)/s^2,                                 (R3-4)
```

which is nonzero because `f(s)>0`, `f_1(s)>0`, and `R_K` is an isomorphism.

Thus an equality between every completed R5 response and the canonical zero
finite-limit response would identify two unequal operators.  The weaker
scalar equality remains open because `(R3-4)` has not yet been pushed through
`p_loc`.

```text
R3 = PASS
FULL_FINITE_TO_COMPLETED_OPERATOR_IDENTIFICATION = false / TYPE-R |
  witness: (R3-2)-(R3-4)
P_LOC_QUOTIENT_IDENTIFICATION = TYPE-U
```

---

## 5. R4 — forward sweep and exact pushforward reduction

### 5.1 The witness is not in a Keldysh-forbidden sector

`RetExtract` has already placed `(R3-4)` in the ordered difference/common
block.  That is the retarded block which the live local Maxwell term occupies:

```text
Gamma_ind^(2)
 =<A_delta,Pi_R,ind A_c>+(i/2)<A_delta,N A_delta>. (R4-1)
```

The finite zeros say the finite restrictions of `(R3-4)` vanish.  They do not
move `(R3-4)` into the noise block, an antisymmetric source direction, the
tree quotient, or `ker(RetExtract)`; Q-396 computed it after `RetExtract`.

```text
Q396_DIRECTION_IS_RETARDED = true
Q396_DIRECTION_IS_NOISE_ONLY = false / TYPE-R
Q396_DIRECTION_IS_KILLED_BY_RETEXTRACT = false / TYPE-R
SECTOR_TYPING_FORCES_P_LOC_H_ZERO = false / TYPE-R
```

### 5.2 Rank-two exchange-orbit computation

Work on the S8-A rank-two carrier and choose an orthonormal metric frame only
for the computation; no frame member is retained.  Let `e_1,e_2` be exchanged
by the admitted signed realization automorphism and set

```text
x_1=r e_1,
x_2=r e_2,
s=r^2,

H_j:=f(s)R_K+2f_1(s)x_j^flat tensor x_j^flat.     (R4-2)
```

Because

```text
x_1^flat tensor x_1^flat
 +x_2^flat tensor x_2^flat
 =r^2 R_K,                                       (R4-3)
```

the orbit sum is

```text
H_1+H_2
 =2[f(s)+r^2 f_1(s)]R_K.                         (R4-4)
```

The bracket is nonzero for `r!=0`.  Covariance of a scalar coefficient
functional under the exchange gives

```text
p_loc(H_1)=p_loc(H_2).                            (R4-5)
```

Applying linearity to `(R4-4)` and `(R4-5)` yields the exact reduction

```text
p_loc(H_1)=p_loc(H_2)
 =[f(r^2)+r^2 f_1(r^2)] p_loc(R_K).               (R4-6)
```

Restoring Q-396's symbolic source and action-unit coefficient,

```text
p_loc[h_i(x_j)]
 =dot_omega_i mu_i
  [f(r^2)+r^2 f_1(r^2)] p_loc(R_K),               (R4-7)
```

where `(R4-7)` denotes the corresponding unit-dual pairing; it does not set a
torsor member to one.

This computation is basis-free in content: `(R4-4)` is the orbit average
under the admitted exchange.  The temporary frame only writes the two orbit
members.  Reversal sends the pair through the ratified semilinear reality
action and leaves the real coefficient condition intact.

### 5.3 What `(R4-7)` proves and does not prove

It proves:

```text
the witness orbit contains a nonzero automorphism-invariant R_K component;
covariance does not force its scalar value to zero;
the minimal exchange-orbit pushforward is controlled by the local-Maxwell
coefficient of `R_K`.
```

It does not prove:

```text
p_loc(R_K)=0;
p_loc(R_K)!=0;
R_K=L_T;
R_K lies wholly in the nonlocal/higher-derivative complement.
```

Normalization gives `p_loc(L_T)=1`, not `p_loc(R_K)`.  The latter would
follow only from a ratified relation such as

```text
R_K=a L_T+R_perp with p_loc(R_perp)=0,             (R4-8)
```

or from an executable local-symbol map.  Neither exists.

### 5.4 Universal-annihilation test

The proposed universal theorem

```text
p_loc[h]=0 for every admissible p_loc and every Q-396 h (R4-9)
```

cannot follow from sector, covariance, reality, units, or finite
restrictions:

1. `h` is in the exact retarded input block.
2. Its exchange-orbit average is nonzero and proportional to `R_K`.
3. No ratified rule places `R_K` in `ker(p_loc)`.
4. DoR-008 cannot evaluate the scalar on a finite restriction because no
   finite coefficient map is sealed.

This refutes the **available proofs** of `(R4-9)`; it does not refute the
possibility that a future derived local-symbol map happens to annihilate
`R_K`.

### 5.5 Detector-construction attack

At a finite rank-two stage one might try

```text
ell_tr(H)=Tr(R_K^(-1)H) / Tr(R_K^(-1)L_T).        (R4-10)
```

When its denominator exists, `(R4-10)` is exchange invariant and detects the
orbit average.  It is **not an admissible construction from the ratified
stock**: no operator trace ideal, completed trace, nonzero denominator,
restriction normalization, batching rule, or spectral identification with
the Maxwell coefficient is supplied.  Using `(R4-10)` would silently author
the missing map.  This attack prevents an algebraic detector from being
misreported as the physical detector.

### 5.6 Exact remaining object

The required certificate is

```text
P_LOC_R5_LOCAL_MAXWELL_SYMBOL_AND_Q396_FIBER_PUSHFORWARD_CERTIFICATE := {
  O_R5 with a named topology and continuous/covariant dual class;
  the embedding of L_T in O_R5 on every physical CTP block;
  a target-independent local-symbol map sigma_loc:O_R5->Scalar;
  sigma_loc(L_T)=1;
  the derived separation of local F^2 from nonlocal/higher terms;
  covariance, reality, Ward, boundary/contact, automorphism, unit,
    restriction, zero-extension, and batching squares;
  the relation of R_K and x^flat tensor x^flat to the local symbol;
  the evaluation chi_K:=sigma_loc(R_K), equivalently the value in (R4-7);
  the kernel of sigma_loc on the full Q-396 admissible fiber;
  compatibility with Pi_loc and R_comp on the same stationary saddle;
  common-origin provenance for any restriction-invisible nonzero component.
}.                                                (R4-11)
```

The resulting alternatives are exact:

```text
chi_K=0
  => the displayed S8-A exchange orbit is p_loc-annihilated;
     full-fiber annihilation still requires sigma_loc on every
     x^flat tensor x^flat profile;

chi_K!=0 for one admitted orbit
  => the completion representative reaches partial_p B_ind through (R4-7);

no unique chi_K but a covariant family
  => the p_loc-visible quotient is a new ratification fiber.       (R4-12)
```

No branch in `(R4-12)` is selected.

```text
R4 = PASS
PUSHFORWARD = NEEDS |
  P_LOC_R5_LOCAL_MAXWELL_SYMBOL_AND_Q396_FIBER_PUSHFORWARD_CERTIFICATE
```

---

## 6. R5 — falsifiers and fresh attacks

### 6.1 Finite and restriction checks

| Check | Re-execution | Verdict |
|---|---|---|
| one edge / tree | `K_cycle=0`, hence Q-396 `Psi` and its pushforward direction are zero | **PASS** |
| reciprocal loop | every finite ordered retarded block is zero before `p_loc` | **PASS** |
| reciprocal loop with probes | exact `omega_i`, noise, and dephasing data survive; ordered retarded block remains zero | **PASS** |
| S8-A rank two | finite active jet is zero; completed orbit computation is `(R4-2)`–`(R4-7)` | **PASS** |
| identity zero-extension | zero finite Hessian extends to zero; no upward completed response is inferred | **PASS** |
| rank-preserving restriction | W3/R5 adjoint square carries the zero finite response | **PASS** |
| cycle creation | only the lawful contravariant restriction and R2 vertical cocycle are used | **PASS** |
| reality | `Adv` completion and semilinear coefficient transport preserve `(R4-7)` | **PASS** |
| batching | components remain ordered/direct-sum; no joint scalar contraction is inserted | **PASS** |
| pendant quotient | `R_K` is formed after Gate-4 quotient; no tree direction returns | **PASS** |

All finite restrictions of the Q-396 direction remain zero.  This proves
finite compatibility, not scalar annihilation at the completed level.

### 6.2 Fresh attack: invariant-component test

The fresh attack asks whether covariance itself kills the witness.  Equations
`(R4-2)`–`(R4-4)` answer no: the orbit average is a nonzero multiple of
`R_K`.  A scalar covariant functional may annihilate the nontrivial
representation component `H_1-H_2`, but its value on the invariant component
is free until `p_loc(R_K)` is derived.

```text
AUTOMORPHISM_COVARIANCE_FORCES_WITNESS_ZERO = false / TYPE-R |
  test: nonzero invariant orbit sum (R4-4)
```

### 6.3 Fresh attack: uniqueness versus existence

The live proof gate requires a **unique** covariant local coefficient
functional.  Universal quantification over “every admissible p_loc” cannot be
used vacuously while existence remains unbuilt.  A proof that every member of
an empty class annihilates the fiber would not discharge the physical
consumer.  The future certificate must establish existence and uniqueness (or
declare the retained family) before applying `(R4-12)`.

```text
P_LOC_EXISTENCE_DERIVED = false / TYPE-U
VACUOUS_UNIVERSAL_ANNIHILATION_ACCEPTED = false / TYPE-R
```

### 6.4 Fence and selection scan

```text
P_LOC_SELECTED = false
COMPLETION_REPRESENTATIVE_SELECTED = false
LOCAL_SYMBOL_SELECTED = false
R_K_IDENTIFIED_WITH_L_T = false
UNIT_OR_FRAME_MEMBER_SELECTED = false
RANK_OR_RATIO_SELECTED = false
p_OR_nu_OR_mu_EVALUATED = false
ROOT_OR_K_STAR_EVALUATED = false

MACHINERY_APPEAL = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false
```

---

## 7. Cross-verification theorem

```text
THEOREM Q476:

1. Under the current ratified R5 value path, p_loc receives the completed
   physical retarded operator realizing Pi_R,ind[G_K].

2. The live corpus does not derive p_loc on that operator class.  Its
   localization words, covariance, normalization, DoR-019 metric/units, and
   DoR-008 finite falsifier do not supply the missing operator coefficient.

3. Q-396 refutes full finite-to-completed operator identification by a pair
   with identical finite active jets and different completed ordered blocks.

4. The Q-396 direction is already retarded and is not killed by sector
   typing.  On the S8-A exchange orbit its p_loc pushforward reduces exactly
   to (R4-7), controlled by the unbuilt coefficient p_loc[R_K]; the full
   fiber also needs the local symbol of the rank-one profiles.

5. Therefore neither universal annihilation nor detection is proved.  The
   exact next object is (R4-11).  It determines whether the completion fiber
   is absent from or present in the registered fixed-point map.
```

Proof: item 1 is `(R1-1)`–`(R1-3)`.  Item 2 is Sections 3.1-3.5.  Item 3 is
`(R3-1)`–`(R3-4)`.  Item 4 follows from the Keldysh typing `(R4-1)` and the
exchange-orbit computation `(R4-2)`–`(R4-7)`.  Item 5 follows because no
ratified line fixes the final coefficient in `(R4-7)`.

---

## 8. Six-account disclosure

| Operation | Domain | Image | Kernel/freedom | Restriction | Completion/topology | Standing |
|---|---|---|---|---|---|---|
| R5 stationary/Schur path | completed action on `D_017` | completed K/K Schur | complement eliminated on `C_red` | R5 cube | graph/completed carrier | ratified architecture |
| `RetExtract` | completed Schur | ordered retarded operator | zero ordered-block class | exact finite zeros | completed R5 class | ratified map / derived kernel |
| Q-396 deformation | admissible base fiber | nonzero ordered block | every finite active jet | all zero | R2 declared topology | derived family witness |
| exchange-orbit averaging | rank-two covariant orbit | invariant `R_K` component | nontrivial exchange representation | finite orbit zero | finite carrier computation | derived `(R4-4)` |
| `p_loc` | completed retarded operator class | dimensionless Maxwell coefficient | unknown on `R_K` and Q-396 fiber | no coefficient square | topology/dual unbuilt | TYPE-U |
| fixed-point pushforward | scalar `p_loc[X_p]` | map/branch dependence | depends on `(R4-12)` and branch | no finite root consumer | downstream | TYPE-U |

---

## 9. Final board

```text
R1_RECEPTION = PASS
R2_UNDERDETERMINATION = PASS
R3_FULL_IDENTIFICATION_REFUTATION = PASS
R4_FORWARD_SWEEP = PASS
R5_FALSIFIERS_AND_FRESH_ATTACK = PASS

CONSUMPTION_RESULT = CONFIRMED

P_LOC_INPUT_STAGE = COMPLETED_R5_OPERATOR
P_LOC_COEFFICIENT_FUNCTIONAL_DERIVABLE = false / TYPE-U
FULL_FINITE_TO_COMPLETED_IDENTIFICATION = false / TYPE-R

Q396_WITNESS_RETARDED_SECTOR = true
Q396_WITNESS_FORCED_P_LOC_KERNEL_BY_SECTOR = false / TYPE-R
Q396_EXCHANGE_ORBIT_INVARIANT_COMPONENT =
  2[f(r^2)+r^2 f_1(r^2)] R_K !=0

PUSHFORWARD = NEEDS |
  P_LOC_R5_LOCAL_MAXWELL_SYMBOL_AND_Q396_FIBER_PUSHFORWARD_CERTIFICATE

PUSHFORWARD_MINIMAL_ORBIT_COEFFICIENT = p_loc[R_K] |
  unit/reality transport understood; not evaluated
PUSHFORWARD_FULL_FIBER_ADDITIONAL_DATA =
  p_loc[x^flat tensor x^flat] on every admitted covariant orbit

ANNIHILATED_FOR_ALL_ADMISSIBLE = NO_VERDICT
DETECTED_BY_A_RATIFIED_ADMISSIBLE_FUNCTIONAL = NO_VERDICT

REGISTERED_FIXED_POINT_MAP_EVALUABLE = false / TYPE-U
REGISTERED_P_VERDICT_WRITTEN = false
NUMERIC_EVALUATION = false
MEASURED_CONSTANT_COMPARISON = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No register, plan, tracker, git, commit, or push action was performed.
