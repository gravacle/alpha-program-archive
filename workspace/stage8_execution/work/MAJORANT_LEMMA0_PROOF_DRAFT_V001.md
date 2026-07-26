# Majorant Lemma 0 Proof Draft V001 (Phase-1 execution lane)

Date: 2026-07-25. Status: DRAFT — NOT SEALED, NOT A RESULT ARTIFACT.
Lane: MAJORANT-GATE PHASE-1 EXECUTION LANE (fresh context).

Governing texts (hashes verified this session before any work; all 20
pinned authorities of the spec table matched exactly; the spec seal
`818083a5...` and amendment seal `60223e6a...` matched their computed
hashes):

- Spec: `STAGE8_T7_CONNECTED_LINKED_CLUSTER_MAJORANT_DERIVATION_SPEC_V001.md`
  (sha256 `818083a52165bc5c2ee86bd43e3b7e30d87f5c9eb82e54935e7829bb6f1f84e3`).
- Amendment (GOVERNS where it differs):
  `STAGE8_T7_D6_SPECS_REPAIR_AMENDMENT_V001.md`
  (sha256 `60223e6a175c5fee122f253491fd279daccfa15f8771af12104710f57ce09e5d`).

Phase-1 scope: O1 (Lemma 0, full proof — the discharge site of the named
blocker `T7III_MULTICELL_COMPOSITION_AND_LIFT`), O2, E1, O3 attempt
(TT1 + TT2 partial), NC1, NC2. O4-O7 and the remaining controls are NOT
attempted here. Per the spec's own rule, this partial execution reports
every completed obligation and every named block.

Exact-arithmetic companion: every decidable numeric claim below was
verified in exact arithmetic over Q(i, sqrt(2)) by the phase verifier
(stdlib-only, pinned runtime python 3.12.13; 29/29 checks pass; script and
output in the lane scratch directory `majorant_p1/`; script digest
recorded in the phase JSON). No float decides anything in this draft.

---

## 0. Sealed objects and exact record spectral data

Per the Phase-A A3 construction (sealed spec `789338ad...`, section A3),
the record factor is H_R = C^3 with |ready> = |0>, |pointer> = |1>, and

```text
c = [[0,0,-i],[0,0,+i],[+i,-i,0]],   spectrum {0, +sqrt(2), -sqrt(2)}.
```

Lagrange interpolation on the (exactly verified) spectrum gives the
spectral projectors in closed form,

```text
P_0 = I - c^2/2;   P_{+sqrt2} = (c^2 + sqrt2 c)/4;   P_{-sqrt2} = (c^2 - sqrt2 c)/4,
```

verified exactly (idempotent, self-adjoint, mutually orthogonal, complete,
and c = sum_lambda lambda P_lambda, all in Q(i,sqrt2) arithmetic). The
sealed weight functionals evaluate exactly to

```text
p_lambda = <ready|P_lambda|ready>   = (1/2, 1/4, 1/4)   for lambda = (0, +sqrt2, -sqrt2);
w_lambda = <pointer|P_lambda|ready> = (1/2, -1/4, -1/4)  (all real rational);

m0 = sum_lambda w_lambda = <pointer|ready> = 0            (EXACT — the D1 restatement);
sum_lambda p_lambda = 1;   |w_lambda| = p_lambda          (amendment M-7 identity, verified);
sum_lambda |w_lambda| = 1;  ||w||^2 = sum |w_lambda|^2 = 3/8.
```

Every constant appearing below is a functional of
`(||b_D||, tau_R, sea-kernel decay data, p_lambda)` only (with tuples read
`|w_lambda|` per M-7, and `|w_lambda| = p_lambda` verified above). No
carrier index, no `ell`, no truncation level, no cellulation-family index
appears in any constant (spec-header scoping 1).

---

## 1. O1 — LEMMA 0: completed-chain relayed multi-cell composition identity

### 1.1 Setup (exactly the sealed objects)

Fix a relayed causal exhaustion K (D2) with cells c = 1, ..., N listed in
a linear extension of the sealed causal order. Per the sealed
relayed-family resolution (`52401eef...`), any two linear extensions
differ by adjacent swaps of incomparable (disjoint) cells whose operators
commute exactly; the relay-ordered product below is therefore independent
of the chosen extension, and "relay-ordered" is well defined.

The total space is

```text
H_tot = F  tensor  ( tensor_c H_R^(c) )  tensor  ( tensor_c H_E^(c) ),
```

with F the CAR/Fock factor over the one-particle carrier, H_R^(c) = C^3
the c-th record factor, H_E^(c) the c-th environment (relayed-record)
copy. The sealed chain dynamics (D2; relay-necessity result `0df721a1...`
O2) is the alternating composition

```text
W^(K)(a) := R_N W^(N)(a_N) R_(N-1) W^(N-1)(a_(N-1)) ... R_1 W^(1)(a_1) iota_1,
```

where, per cell c:

- (cell closure, sealed A4 form) W^(c)(a_c) = sum_lambda
  Gamma(u_lambda^(c)(a_c)) tensor P_lambda^(c), acting on
  F tensor H_R^(c), identity elsewhere; Gamma is the sealed
  number-preserving quasifree lift;
- (relay, sealed type) R_c |p_(c,h)> = |e_(c,h)> tensor |r_(c+1)>:
  an exact isometry from the cell-c public endpoint into
  H_E^(c) tensor H_R^(c+1), record-preserving (h -> e_(c,h) is a fixed
  orthonormal-basis map), acting as the identity on F and on all other
  factors; iota_1(psi) = psi tensor |r_1> is the tensor-form ready-root
  supply (Q_spec realization, sealed).

Three sealed facts are used and nothing else:

```text
(S1) R_c^dagger R_c = I on the cell-c record chain (exact isometry;
     relay-necessity O2, finite checks zero-error, tuple-level verified);
(S2) every operator of a later cell commutes exactly with the environment
     copies and pointer observables of earlier cells (relayed-family
     resolution: "Every later cell commutes exactly with prior pointer
     observables");
(S3) Gamma is multiplicative and adjoint-compatible on one-particle
     unitaries: Gamma(u)Gamma(v) = Gamma(uv), Gamma(u)^dagger =
     Gamma(u^dagger). This is the defining functorial property of the
     sealed number-preserving quasifree lift and is ALREADY load-bearing
     in the sealed corpus: the sealed A4 display
     R_all(a,a) = sum_lambda p_lambda Gamma(u_lambda^dagger u_lambda) = I
     is exactly this property applied termwise.
```

The chain-level pointer (completed) Kraus operator is the compression of
W^(K)(a) onto every cell's pointer record:

```text
K_pointer^(K)(a) := ( tensor_c <e_(c,pointer)| ) W^(K)(a) |root>,
```

acting on F, where <e_(c,pointer)| reads the preserved record of cell c
in its environment copy (for the final cell, on H_R^(N) directly if no
trailing relay is applied; both conventions give the same operator by
(S1)-(S2), and we fix the trailing-relay convention).

### 1.2 Statement

```text
LEMMA 0 (completed-chain relayed multi-cell composition).
For every relayed causal exhaustion K, every admitted cellulation, and
every per-cell history assignment (complex CTP pairs admitted per
amendment M-2 under the adjoint-continued convention):

(a) K_pointer^(K)(a) = prod_c^(relay-ordered) K_pointer^(c)(a_c),
    with K_pointer^(c)(a_c) = sum_lambda w_lambda Gamma(u_lambda^(c)(a_c))
    the sealed per-cell D1 object and the operator product taken in relay
    order (later cells to the left);

(b) R_comp^(K)(a_+, a_-) := K_pointer^(K)(a_-)^dagger K_pointer^(K)(a_+)
      = sum_((mu_c),(lambda_c))  [ prod_c w_(mu_c)^* w_(lambda_c) ]
          Gamma( U_(mu)^(K)(a_-)^dagger U_(lambda)^(K)(a_+) ),
    U_(lambda)^(K)(a) := u_(lambda_N)^(N)(a_N) ... u_(lambda_1)^(1)(a_1),
    the sum running over per-cell INDEPENDENT color pairs (mu_c, lambda_c)
    (all 9^N terms; product weights; no cross-cell record-color
    correlation) — this is the discharge of H-IND;

(c) the record-side relay isometries cancel exactly between the CTP
    branches (only (S1) is used; no unitality anchor is invoked anywhere);

(d) m0-consistency: the chain-level pointer weight sum is
    sum_((lambda_c)) prod_c w_(lambda_c) = prod_c m0 = 0 for every N >= 1;
    the completed chain has no unitality anchor at any size, and the
    normalization is carried solely by the T7(i) ratio anchor under the
    named hypothesis H-B (not discharged here).
```

### 1.3 Proof

Step 1 (per-cell compression is the sealed Kraus). For any record
outcome x on cell c, `<x| W^(c)(a_c) |ready> = sum_lambda
<x|P_lambda^(c)|ready> Gamma(u_lambda^(c)(a_c)) = K_x^(c)(a_c)` — the
sealed A4 display; for x = pointer the coefficient is w_lambda. This uses
only the spectral resolution; completeness `sum_lambda P_lambda = I_3`
(verified exactly) is a property of projectors, not a unitality anchor.

Step 2 (relay transports the record reading). Because R_c is
record-basis-preserving, for every h:
`<e_(c,h)| R_c = <p_(c,h)| tensor <r_(c+1)| ... ` more precisely, on the
range of the cell-c closure,

```text
( <e_(c,h)| tensor I ) R_c = <p_(c,h)|  followed by injection of |r_(c+1)>.
```

Equivalently: R_c maps the orthonormal record basis to an orthonormal
family (exact isometry, (S1)), so reading outcome h on the environment
copy AFTER the relay equals reading outcome h on the record factor BEFORE
the relay, while the relay simultaneously supplies the fresh ready root
|r_(c+1)> of cell c+1 in TENSOR form. No approximation; type equality.

Step 3 (later cells do not disturb earlier readings). By (S2), every
operator of cells c' > c (their W^(c') and relays) commutes exactly with
`|e_(c,h)><e_(c,h)|` and with the compression `<e_(c,pointer)|`. Hence in
the full compression of W^(K)(a), the bra `<e_(c,pointer)|` may be
commuted inward until it meets R_c W^(c)(a_c) directly.

Step 4 (telescoping). Apply Steps 1-3 inductively from cell 1 outward:

```text
<e_(1,pointer)| R_1 W^(1)(a_1) iota_1
  = <pointer| W^(1)(a_1) |ready>  tensor  |r_2>-supply
  = K_pointer^(1)(a_1)  tensor  |r_2>-supply,
```

where K_pointer^(1)(a_1) acts on F alone and the fresh root |r_2> is
exactly the ready state that cell 2's closure consumes. Repeating for
c = 2, ..., N (each step consuming the root supplied by the previous
relay, each compression yielding the scalar-weighted Fock operator
`sum_lambda w_lambda Gamma(u_lambda^(c)(a_c))`) gives

```text
K_pointer^(K)(a) = K_pointer^(N)(a_N) ... K_pointer^(1)(a_1)
                 = prod_c^(relay-ordered) K_pointer^(c)(a_c).
```

This proves (a). Expanding each factor and using (S3) to merge the Gamma
string per color assignment:

```text
K_pointer^(K)(a) = sum_((lambda_c)) [ prod_c w_(lambda_c) ]
                     Gamma( u_(lambda_N)^(N)(a_N) ... u_(lambda_1)^(1)(a_1) ).
```

The color sum is a product of INDEPENDENT per-cell sums because (and only
because) each cell's record factor is its own tensor factor supplied in
the ready root by the relay (tensor-form supply): the joint record state
entering cell c is |ready_c> exactly, independent of the colors drawn by
earlier cells — the earlier colors were absorbed into scalar weights at
Step 4 and the relayed records sit in orthogonal environment copies. No
cross-cell record-color correlation exists at any N. This is the
structural discharge of H-IND claimed in (b).

Step 5 (CTP branches and relay cancellation). By definition,
R_comp^(K)(a_+, a_-) = K_pointer^(K)(a_-)^dagger K_pointer^(K)(a_+).
Writing both branches by Step 4 and using (S3) again,

```text
R_comp^(K)(a_+, a_-)
 = sum_((mu_c),(lambda_c)) [ prod_c w_(mu_c)^* w_(lambda_c) ]
     Gamma( U_(mu)^(K)(a_-)^dagger U_(lambda)^(K)(a_+) ),
```

with U as in the statement. Where the two branches meet, the relay
contributions appear exactly as `R_c^dagger (projector onto the preserved
record) R_c`; by record-basis preservation and (S1) these collapse to the
per-branch scalar weights already extracted — the record-side relay
isometries cancel exactly between the CTP branches, proving (c). For
complex CTP pairs the bra branch is the adjoint-continued object
`Ktilde(w) = [K_pointer(conj w)]^dagger` (amendment M-2); the telescoping
above is purely algebraic and history-blind, so the identity holds for
the adjoint-continued branch verbatim, and restriction to real pairs
recovers the sealed D1 display.

Step 6 (m0 = 0 respected; (d)). No step above used `R(a,a) = I`,
`sum_lambda w_lambda = 1`, or any unitality anchor: Step 1 uses spectral
completeness of projectors; Steps 2-3 use isometry and commutation; Steps
4-5 use functoriality of Gamma. The chain-level weight sum factorizes by
(b)'s independence into `prod_c (sum_lambda w_lambda) = m0^N = 0`
(verified exactly for N = 2 in the companion; the general case is the
exact identity 0^N = 0). The diagonal `R_comp^(K)(a,a)` is NOT the
identity, and nothing here needs it to be; the normalization anchor is
the T7(i) ratio `Z_hat_comp = Z_comp(a)/Z_comp(0)` under the NAMED
hypothesis H-B, which this lemma does not discharge and does not use
(no logarithm is taken in Lemma 0). QED.

### 1.4 Notational determination D-N1 (recorded for hostile review)

The spec's O1 display writes the right-hand side of (b) as
`prod_c w_(mu_c)^* w_(lambda_c) Gamma(u_(mu_c)^(c)(a_-)^dagger
u_(lambda_c)^(c)(a_+))`, i.e. with Gamma applied per cell to the per-cell
CTP sandwich. Two readings of `prod_c` exist:

- (interleaved) the literal operator product of per-cell sandwiches
  `Gamma(u_(mu_N)^dagger u_(lambda_N)) ... Gamma(u_(mu_1)^dagger u_(lambda_1))`;
- (CTP-nested) the relay-ordered CTP composition proved in (b):
  weights per cell, one-particle string in the order forced by
  `K^(K)(a_-)^dagger K^(K)(a_+)`.

The two readings coincide exactly whenever the participating cells are
pairwise disjoint (sealed disjoint-cell commutation, relayed-family
resolution) and differ in general for causally comparable cells (the
sealed record exhibits non-commuting causally ordered cells:
`||U_1 U_0 - U_0 U_1||_F^2 = 288` for the overlapping pair of the
three-cell regression). The left-hand side R_comp^(K) is SEALED-DEFINED
(D1 lineage: `Z_comp(a) = omega_in(K_pointer^(K)(a_-)^dagger
K_pointer^(K)(a_+))`), and under the interleaved reading the displayed
identity would be FALSE for causally comparable cells; under the
CTP-nested reading it is the theorem proved above. The sealed definition
of the LHS therefore forces the CTP-nested reading; the ambiguity is
resolvable from the sealed texts alone and is resolved accordingly — not
by executor preference. This determination changes no sealed
mathematics; it is recorded here so the hostile lane can either confirm
it or convert it into a named block (`O1_DISPLAY_ORDER_AMBIGUITY`) if it
judges the sealed texts insufficient to force the reading. Every
downstream use in this phase (O2, E1, O3, NC1, NC2) is insensitive to the
distinction: only the per-cell weight structure and color independence
are consumed.

### 1.5 Blocker disposition

O1 discharges the composition-identity component of the named blocker
`T7III_MULTICELL_COMPOSITION_AND_LIFT` at the level of this draft
(pending hostile review and independent re-derivation per F-8). The
blocker's other components (uniform differentiated-series convergence =
O5; K-level density = O6) are OUT of Phase-1 scope and remain open; the
blocker as a whole is therefore NOT yet discharged and no protected flag
changes.

---

## 2. O2 — Action-density activity construction and re-aggregation (M-4)

### 2.1 Construction of the activities (per-state; amendment M-3)

Admitted states: the two Phase-A pinned finite schemes
(C_mix = Q P_- Q; C_pure = 1_(-infinity,0)(Q h_0 Q)); every claim below
is per-state and is never promoted across states.

For a cellulation X of the exhaustion K and a nonempty finite subset
gamma of cells of X, let Z_hat_comp^(K,gamma)(a) denote the T7(i)-
normalized completed amplitude of the sub-collection gamma (the relayed
sub-chain on the cells of gamma in the induced relay order), defined
whenever its baseline is nonzero — which is exactly hypothesis H-B
applied to the admitted finite sub-complexes; H-B is NAMED and not
discharged here. Define, for nonempty gamma (Moebius/Ursell truncation):

```text
Phi_gamma(a) := - sum_(emptyset != gamma' subseteq gamma)
                   (-1)^(|gamma| - |gamma'|) Log Z_hat_comp^(K,gamma')(a),
```

principal branch anchored at the T7(i)-normalized baseline (D1; F-3).
Finite Moebius inversion over the Boolean lattice of subsets of X gives
the EXACT identity (a finite algebraic identity, no convergence input):

```text
- Log Z_hat_comp^(K,X)(a) = sum_(emptyset != gamma subseteq X) Phi_gamma(a).
```

Two exact structural properties:

- (support/connectivity) if gamma = gamma_1 union gamma_2 with gamma_1,
  gamma_2 nonempty and mutually disjoint (no common refinement cell and
  spacelike/causally incomparable so that the sealed disjoint-cell
  commutation and the monoidal-extensivity authority `451550c3...` apply),
  then Z_hat^(gamma) = Z_hat^(gamma_1) Z_hat^(gamma_2) exactly
  (monoidality on disjoint cells + Lemma 0's factorization), and the
  alternating sum telescopes to Phi_gamma = 0. Activities are supported
  on CONNECTED clusters, and the sum above collapses to the anchored
  connected-cluster sum of theorem clause (2).
- (independent colors) by Lemma 0(b), each Z_hat^(gamma') is a ratio of
  sums over per-cell independent color pairs with product weights — the
  activity construction inherits H-IND structurally and never introduces
  cross-cell color correlation.

The single-cell activity is Phi_C(a) = -Log Z_hat_comp^(C)(a).

### 2.2 Action-density form (D5) — where the 4-volume enters

The required BOUND shape is `sum_(gamma ni C, |gamma| = n) |Phi_gamma(a)|
<= |C|_4 * eta^n` with eta per unit 4-volume. The mechanism (proved at
the level available in Phase 1; the certified constants are E1's):

- the connection difference enters each cell only through
  `a_c J^(c)(t)` with `J^(c)(t) = -Q b_D^(c)(t,.) Q tensor alpha_x`
  supported in the cell's causal diamond;
- every Duhamel insertion therefore carries the in-cell profile
  b_D^(c), and the sea-kernel pairing of that insertion is an integral
  over the cell's diamond: its natural majorant is (sea-kernel trace
  density per unit 4-volume) x |C|_4 — this is the action-density form;
- the profile construction is scale-covariant with invariant sup:
  for EVERY admitted cell, `||b_D^(c)||_inf = 1` exactly (proof in 3.1;
  the sup is a fixed dimensionless number, so per-cell strength is
  carried entirely by the 4-volume factor, never by a per-cell constant).

An activity normalization that is per-CELL rather than per-4-volume
breaks under refinement (its executable exhibition is NC6, out of this
phase's scope).

### 2.3 Re-aggregation identity over the refinement poset (amendment M-4)

Definitions. An ELEMENTARY refinement step on a cellulation X replaces
one closed 4-cell C by finitely many closed 4-cells C_1, ..., C_k with
pairwise disjoint interiors, union C, leaving all other cells unchanged.
X' <= X ("X' refines X") iff every cell of X' is contained in a cell of X
and every cell of X is the union of the X'-cells it contains. The
admitted poset is generated by the skeleton, families A and B, and all
common refinements (D3; the quantifier is NEVER pinned to a finite list,
F-2).

Lemma R1 (exact 4-volume re-partition). For an elementary step,
`|C|_4 = sum_i |C_i|_4` exactly. Proof: the C_i are closed polyhedral
(cubical or simplicial or their polyhedral common-refinement) cells with
pairwise disjoint interiors whose union is C; polyhedral cell boundaries
are finite unions of affine pieces of dimension <= 3, hence Lebesgue-null
in R^4; finite additivity of Lebesgue measure on interior-disjoint closed
sets with null boundaries gives the identity exactly. QED.

Lemma R2 (activity-level additivity of the insertion domain). Any
integral of a fixed integrable density over C splits exactly as the sum
of its integrals over the C_i (same null-boundary argument). Hence every
Duhamel-insertion domain integral that produces the |C|_4 factor of 2.2
re-partitions exactly under the step — the majorant's 4-volume weight is
not an inequality artifact but an exactly additive set function. QED.

Lemma R3 (bound re-aggregation without loss, one step). Assume the D5
bound holds on the refined cellulation X' with the SAME eta (constants
are cellulation-blind by construction: eta is a functional of
`(||b_D||, tau_R, sea-kernel decay data, p_lambda)` only, and by 2.2 the
per-cell data entering it — sup of profile, weight sums, per-unit-volume
sea density — are the same for every admitted cell of every admitted
cellulation). Then for the coarse cell C = union C_i and each n:

```text
sum_i sum_(gamma' ni C_i, |gamma'| = n) |Phi_gamma'(a)|
   <= sum_i |C_i|_4 eta^n  =  |C|_4 eta^n        (Lemma R1),
```

i.e. the total activity mass anchored anywhere in C obeys the SAME
aggregate bound after refinement as before — the majorant re-aggregates
without loss. QED.

Proposition R4 (full-poset induction; the M-4 closure argument). Claim:
the re-aggregation identity (Lemmas R1-R3) holds between X and Z for
EVERY pair X >= Z in the admitted poset, not merely for one elementary
step. Proof. (i) Reachability: let Z <= X. Each cell C of X is
partitioned by the finitely many Z-cells contained in it (definition of
refinement; finiteness because the admitted complexes are finite). Doing
one elementary step per cell of X, in any order, transforms X into Z in
exactly |X| steps. Steps on distinct cells act on disjoint closed cells
and commute as operations on cellulations, so the chain is well defined
and order-independent. (ii) Induction: R1-R2 compose along the chain
because finite sums of finite sums re-associate exactly (finite
additivity is transitive: if |C|_4 = sum_i |C_i|_4 and each
|C_i|_4 = sum_j |C_ij|_4 then |C|_4 = sum_ij |C_ij|_4); R3 applies at
each step with the same eta. (iii) Closure (the explicit obligation):
one elementary step from a family-A member does NOT reach an A-with-B
common refinement, and no finite iteration STARTING INSIDE family A
alone need do so; the argument above does not require it to. What is
required and proved is: an A-with-B common refinement Z is BY DEFINITION
a refinement of the A-member X_A (and of the B-member X_B); reachability
(i) runs from X_A to Z directly, with the elementary steps partitioning
each X_A-cell into its Z-pieces — which are polyhedral cells of the
common refinement, admitted by D3. The induction therefore covers every
A-with-B common refinement, and symmetrically from the B side; both
chains yield the same re-aggregated identity because the identity's two
sides depend only on (X, Z), not on the chain (order-independence in
(i)). QED.

Status: O2 discharged at Phase-1 level: activities constructed in
action-density form (2.1-2.2), exact Moebius identity, connectivity
support, and the re-aggregation identity proved over the FULL
common-refinement poset with the closure argument explicit (Proposition
R4). The quantitative content of eta itself is E1's (see its named block
below); nothing in O2 depends on eta's numeric value.

---

## 3. E1 — eta(epsilon) as an explicit certified functional; epsilon_star

### 3.1 Exact ingredients derived this session

```text
||b_D||_inf = 1  EXACTLY.
```

Proof: on the open diamond, s = s_- s_+ with s_- = t^2 - |x|^2 <= t^2 and
s_+ = (1-t)^2 - |x|^2 <= (1-t)^2, both factors positive there, so
s <= t^2(1-t)^2; the exact polynomial identity 4t(1-t) = 1 - (2t-1)^2
(verified coefficientwise in exact arithmetic) gives t(1-t) <= 1/4, so
s <= 1/16 with equality iff (t,x) = (1/2, 0); exp is monotone, so
b_D = exp(16 - 1/s) <= exp(0) = 1 = b_D(1/2, 0). Scale covariance: the
per-cell profile is the same construction on the affinely rescaled
diamond, and the bound is scale-free, so `||b_D^(c)||_inf = 1` for every
admitted cell. Derived, not measured.

```text
tau_R = pi/sqrt(2)                       (sealed authority b786db3a...);
p_lambda = (1/2, 1/4, 1/4);  |w_lambda| = p_lambda;  sum |w_lambda| = 1
                                          (exact; section 0);
envelope class: int_0^1 v_A(t) dt = tau_R exactly
  (int_0^1 32 min(t,1-t)^3 dt = 1, exact rational integral);
int_0^1 v_B dt = 24 tau_R / pi;  class-uniform bound
  V_env := 24 tau_R / pi  (24/pi > 1 certified outward from
  pi = 4 int_0^1 dx/(1+x^2) < 4; derived, not measured).
```

The envelope-profile class enters eta only through the record-side
propagators inside the sea functionals below; the derived
epsilon-dependence of eta is envelope-class-uniform, so the functional is
stated over the CLASS as the spec-header requires.

### 3.2 The derived functional

Per admitted state (M-3), per cell, per color pair (mu, lambda), the
state evaluation of the sealed Gaussian objects is determinantal
(quasifree formula on the sealed schemes): omega(Gamma(V)) =
det(1 + C(V - 1)). Write V_(mu lambda)(a) = u_mu(a_-)^dagger
u_lambda(a_+) (adjoint-continued on the M-2 pair polydisc). Exact
one-particle Duhamel bound (operator norm, unitary invariance):

```text
||u_lambda(a) - u_lambda(0)|| <= |a| int_0^1 ||J(t)|| dt
                              <= |a| ||b_D||_inf = |a|;
||V_(mu lambda)(a) - V_(mu lambda)(0)|| <= (|a_+| + |a_-|) <= 2 epsilon.
```

Assembling the standard determinant-difference bound
`|det(1+A) - det(1+B)| <= ||A - B||_1 exp(1 + max(||A||_1, ||B||_1))`
with the per-cell weight sum `sum_(mu,lambda) |w_mu^* w_lambda| =
(sum_lambda |w_lambda|)^2 = 1` (exact) and localizing every Duhamel
insertion in the cell diamond (J = 1_D J 1_D since supp b_D is the closed
diamond) yields the per-unit-4-volume single-cell majorant and, at the
KP threshold frozen in E1, the explicit monotone functional

```text
eta(epsilon) = (2 epsilon ||b_D||_inf K_sea / b_0)
                 * exp( 1 + T_R + 2 epsilon ||b_D||_inf K_sea ),
```

where the three sea-tier constants are the explicit functionals

```text
K_sea := sup_(admitted cells C) |C|_4^(-1)
           int_0^1 max_mu || C_state u_mu^(c)(1<-t; 0) Q 1_(D_t) Q ||_1 dt
         (sea-kernel action-density constant: state covariance, full-
          record in-cell propagation, diamond-slice localization);
T_R   := sup_(mu,lambda) || C_state ( V_(mu lambda)(0) - 1 ) ||_1
         (full-record baseline trace norm; records at full tau_R);
b_0   := |Z_comp^(C)(0)|
         (single-cell completed baseline modulus; exists nonzero under
          named H-B; a functional of tau_R and the sea data only).
```

All three are functionals of `(||b_D||, tau_R, sea-kernel decay data,
p_lambda)` only — carrier-index-blind BY DEFINITION (no n, no ell, no
truncation enters their defining expressions).

Monotonicity (exact-symbolic): eta'(epsilon) = (2||b_D||K_sea/b_0)
exp(1 + T_R + 2 epsilon ||b_D|| K_sea)(1 + 2 epsilon ||b_D|| K_sea), a
product of strictly positive factors for positive inputs — eta is
strictly increasing on epsilon > 0. The amendment's named witness
`ETA_MONOTONICITY_UNCERTIFIED` (M-8) does NOT fire at the functional
level; the E1 grid rule is well-posed regardless (M-8).

### 3.3 NAMED BLOCK: the sea tier is uncertifiable from the sealed corpus

The grid evaluation `epsilon_star = max{2^-k : eta(2^-k) <= 1/2
certified}` requires certified outward enclosures for (K_sea, T_R, b_0).
This session establishes, and reports as a named block, that the sealed
corpus does not supply them:

```text
NAMED BLOCK: E1_SEA_KERNEL_ACTION_DENSITY_UNCERTIFIED
(the spec's own "IR sea-kernel witness" arm, surfacing at E1 because
E1's frozen tuple includes the sea-kernel decay data).
```

Grounds (each checkable against the sealed record):

1. The sealed corpus pins only the decay CLASS of the sea kernel: the
   `|x|^-3` class named by the spec itself (O4, known failure mode), and
   the sealed temporal-return amplitude `A_D(t) = i/(6 pi t^3) + o(t^-3)`
   (R3_4 causal-diamond spectral pullback lineage). No sealed artifact
   certifies an outward enclosure for any integrated sea-kernel
   functional on a cell.
2. `|x|^-3` is not locally integrable in R^3: the naive kernel-integral
   bound for K_sea log-diverges at coincidence. In the continuum, the
   operator (state covariance) x (smooth compactly supported
   multiplication) is not trace class; on the finite Phase-A carrier the
   trace norm is finite but CARRIER-DEPENDENT — and a carrier-dependent
   constant is a spec violation (spec-header scoping 1), not an out.
3. Finiteness of the properly defined functional must come from the
   oscillatory/PV structure of the sealed return amplitude (the
   imaginary-coefficient `i/(6 pi t^3)` class) or from the CTP
   difference structure (determinant differences of adjoint-continued
   pairs). Certifying either is exactly the infrared work the spec names
   as "the same infrared structure already named as T7's true bottom".
   No sealed authority discharges it, and inventing an enclosure would
   be a measured constant — forbidden (F-4).

Consequences, reported per the spec's own arms:

- epsilon_star is NOT frozen in Phase 1. This is not
  `EPSILON_STAR_VACUOUS` (no certified grid evaluation returned "no
  point qualifies"; the evaluation could not be certified at all).
- The conditional content is preserved and certified: for any future
  certified enclosures (K_sea <= K, T_R <= T, b_0 >= b), the grid rule
  reads `2^(-k+1) K exp(1 + T + 2^(-k+1) K) <= b/2`, decidable in exact
  rational arithmetic with outward exp enclosures (the phase verifier
  carries a self-tested certified outward exp enclosure; e in [2, 2.72]
  witnessed by exact Taylor bounds with an exact rational remainder).
- Under E1 step 3's spirit read strictly, Phase-1's E1 verdict
  contribution is the BLOCKED arm with the named IR sea-kernel witness
  (already anticipated by the spec's verdict table); the block is
  reported as a victory of the fence system, not repaired.

---

## 4. O3 — Route T attempt: TT1 constructed (demoted form); TT2 partial

### 4.1 F-7 demotion recorded (not silent)

No Phase-A regulated-CAR production bundle exists in
`stage8_execution/work/` at execution time (checked: no
`T07_actual_parent_regulated_car*` artifact). Per fence F-7 this does not
block the theorem work but DEMOTES representation-level constructions to
statements about the abstract sealed form. Recorded here as required:
TT1 below is the anchored transfer operator OF THE ABSTRACT SEALED FORM;
its concrete matrix representation awaits the Phase-A bundle.

### 4.2 TT1 — anchored transfer operator on the pinned hypercubic skeleton

Skeleton: the primary hypercubic fixture (D3; a regression fixture, not
proof of universality). Slab decomposition: cells organize into time
slabs; within a slab cells are pairwise disjoint and commute exactly
(sealed); the relay order lists slabs sequentially.

Definition (TT1, exact representation at the sealed-form tier). For slab
histories a restricted to the M-2 pair polydisc, the slab Kraus operator
is (well defined by Lemma 0(a) and disjoint-cell commutation)

```text
K_slab(a) := prod_(c in slab) K_pointer^(c)(a_c)
           = prod_(c in slab) sum_lambda w_lambda Gamma(u_lambda^(c)(a_c)),
```

and the ANCHORED TRANSFER OPERATOR at anchor a = 0 is the completely
bounded map on the observable space of the CAR factor

```text
T_0[X] := K_slab(0)^dagger X K_slab(0),
```

with the a-dependent family T_a[X] := K_slab(a_-)^dagger X K_slab(a_+)
(adjoint-continued off the real slice per M-2). Content-addressed exact
representation emitted with this phase (in the phase JSON): the exact
record data (weight vector w = (1/2, -1/4, -1/4) over colors
(0, +sqrt2, -sqrt2); all exact), the slab color-sum structure (9 color
pairs per cell, independent across cells — Lemma 0(b)), and the
one-particle symbol references (the sealed A1/A2 generators
h_0 + lambda v(t) M(t) tensor S + a J(t) over the cell, envelope class
{v_A, v_B}). The composition law across slabs is Lemma 0(a) applied
slab-wise; iterating T reproduces the chain functional exactly.

TT1 status: CONSTRUCTED at the demoted (abstract sealed form) tier;
representation-level instantiation named as awaiting the Phase-A bundle.

### 4.3 TT2 — isolation certificate: named partial

Template: the certified periodic machinery (invariant-graph method;
sealed results `b54f20ea...`, `50613168...`). The certificate reduces to
four named enclosure obligations on the represented operator:

```text
TT2-E1: leading-direction candidate and its Gram/SVD enclosure
        (template step: independent reconstruction of the zero-history
        transfer with a certified norm bound);
TT2-E2: off-leading contraction bound (invariant-graph map radius and
        contraction constant, outward-enclosed);
TT2-E3: history-disk robustness radius (generator/Stinespring bound) —
        consumes epsilon_star ONLY (amendment M-10), hence BLOCKED
        pending E1's sea-tier block above;
TT2-E4: leading-mode coefficient lower bound (nonvanishing enclosure).
```

Certified partial obtained this session (record tier):

```text
TT2-P0 (certified, exact): the record-weight factor of T_0 — the
color-pair form W = w_bar w^T — has EXACTLY isolated leading structure:
rank one (every 2x2 minor vanishes identically in exact arithmetic),
leading singular value ||w||^2 = 3/8 exactly, all other singular values
exactly 0. This is a genuine but strictly partial ingredient: it
certifies the record-side spectral collapse of the transfer structure
and is NOT the TT2 isolation certificate, which lives on the full
CAR-side operator.
```

TT2 verdict contribution (named partial, not a failure):

```text
TT2_PARTIAL_AWAITING_REPRESENTATION
  certified: TT2-P0 (record tier, exact);
  uncertified: TT2-E1, TT2-E2, TT2-E4 (await the Phase-A
    representation bundle; F-7 demotion recorded);
  blocked upstream: TT2-E3 (consumes epsilon_star; E1 sea-tier block).
```

TT3 not attempted (depends on TT2). No TT certificate quantifies beyond
the skeleton; nothing here touches the refinement families (O7 untouched,
its fence F-2 respected).

---

## 5. O8 controls in scope: NC1 and NC2

### 5.1 NC1 — GHZ refusal naming H-IND (PASS, by the named ground only)

Input: the sealed closure result's witness (`f891d3af...`): preparation
`(|0...0> + |1...1>)/sqrt(2)`, amplitude family `Z_N(A) = cos(N tau_R A)`,
first zero `pi/(2 N tau_R)`.

Pipeline gate (structural, evaluated BEFORE any amplitude computation):
Lemma 0(b) makes tensor-form per-cell ready-root supply — hypothesis
H-IND — a typed precondition of the composition identity. The checker
computes, in exact arithmetic, the cross-cell record correlation of the
input preparation across any two-cell bipartition:

```text
joint branch distribution  = [[1/2, 0], [0, 1/2]];
product of marginals       = [[1/4, 1/4], [1/4, 1/4]];
correlation matrix         = [[ 1/4, -1/4], [-1/4, 1/4]]  (exact);
max modulus                = 1/4, enclosure [1/4, 1/4] EXCLUDES ZERO;
Schmidt witness: product of squared Schmidt coefficients = 1/4 != 0
                 => Schmidt rank 2 => not tensor-form supply.
```

REFUSAL issued, citing exactly and only the violated hypothesis:

```text
REFUSED: H-IND (per-cell independent record colors; the input
preparation is the perfectly-correlated-color limit; cross-cell record
correlation 1/4 != 0 certified exact).
```

No numeric failure occurred; no other ground is cited; the GHZ amplitude
and its zeros were not evaluated (they are quoted above only from the
sealed closure result). The exhaustive companion object appears nowhere
in the gate (F-6 respected: the control consumes the sealed WITNESS, not
the exhaustive closure). PASS per the NC1 pass condition; prediction P4's
NC1 clause confirmed.

### 5.2 NC2 — correlated-color variant detectably fails (PASS)

Variant: replace the per-cell independent color sums of Lemma 0 by a
single shared color across cells:

```text
K_shared^(12)(a) := sum_lambda w_lambda Gamma(u_lambda^(2)(a_2))
                                    Gamma(u_lambda^(1)(a_1)).
```

Detectable-failure witnesses, all exact, all enclosures excluding zero:

```text
(i)   weight-sum witness: completed two-cell chain weight sum
      = m0^2 = 0 exactly; shared-color weight sum
      = sum_lambda w_lambda^2 = 3/8 exactly;
      cross-cell record-color correlation witness
      = 3/8 - 0 = 3/8, enclosure [3/8, 3/8] EXCLUDES ZERO.
(ii)  elementwise witness: W_shared(0,0) - W_indep(0,0)
      = w_0 - w_0^2 = 1/2 - 1/4 = 1/4 != 0 exact.
(iii) factorization obstruction: the independent weight matrix
      w_bar w^T is exactly rank one (every 2x2 minor vanishes
      identically); the shared-color weight matrix diag(w_lambda) has
      the exact 2x2 principal minor w_0 w_+ = -1/8 != 0; hence NO
      per-cell weight vectors reproduce the shared-color object — the
      composition identity DETECTABLY fails, with certified enclosures.
```

Silence is impossible under these witnesses; PASS per NC2's condition.
Prediction P4's NC2 clause confirmed. (NC5's exact witness M-5 —
`m0' = sum p_lambda = 1` vs 0 — is out of this phase's scope but is
noted to be exactly computable from the same data: sum p_lambda = 1
verified exact.)

---

## 6. Fences respected; no-target statement

F-1: no clustering axiom or principle reached for anywhere (the only
convergence input in this phase is the frozen E1/KP threshold, unused
because blocked). F-2: cellulation quantifier never pinned; O7 untouched.
F-3: no exhaustive zero-free citation toward completed obligations; the
D1 restatement (m0 = 0, T7(i) anchor, named H-B) governs throughout;
Lemma 0 Step 6 records the anchor-free bookkeeping. F-4: no measured
constants; every number above is derived exactly or named as blocked;
Frozen Numerics respected (exact rational/symbolic arithmetic; certified
outward enclosures; pinned runtime; verifier script hashed in the phase
JSON). F-5: no in-execution PASS string claims authority; verdicts here
are the lane's report, subject to the hashed evaluator and hostile
review. F-6: the exhaustive closure appears only inside the NC1
discussion as the sealed witness's home, never substituted. F-7:
demotion recorded (4.1). F-8: this is the primary lane's draft;
independent re-derivation is required before any result seals.

NC7 statement: the numerical outputs of this lane are exactly: the exact
record spectral data (1/2, 1/4, -1/4, 3/8, -1/8 and companions), the
derived exact ingredients of eta (||b_D|| = 1, envelope integrals,
weight sums), the control witnesses (1/4, 3/8, -1/8), and the TT2-P0
record-tier enclosure (3/8). No kappa_record, no alpha, no function of
either, no target-adjacent numeric appears.

## 7. Phase-1 verdict summary (per-obligation; nothing sealed)

```text
O1  (Lemma 0)  DERIVED IN DRAFT (full proof above; notational
               determination D-N1 recorded for hostile review;
               discharges the composition component of the named
               blocker, pending F-8 independent re-derivation).
O2             DERIVED IN DRAFT (action-density construction; exact
               Moebius identity; connectivity support; re-aggregation
               proved over the full refinement poset, M-4 closure
               explicit).
E1             PARTIAL WITH NAMED BLOCK: functional derived explicitly,
               monotone (M-8 witness does not fire); exact ingredients
               certified; sea tier BLOCKED —
               E1_SEA_KERNEL_ACTION_DENSITY_UNCERTIFIED (the spec's IR
               sea-kernel witness); epsilon_star NOT frozen; conditional
               grid rule certified and preserved.
O3             TT1 CONSTRUCTED (demoted to abstract sealed form per
               F-7, demotion recorded); TT2
               TT2_PARTIAL_AWAITING_REPRESENTATION with certified
               record-tier partial TT2-P0; TT2-E3 blocked on E1; TT3
               not attempted.
NC1            PASS (refusal naming exactly H-IND; exact witnesses).
NC2            PASS (detectable failure; three exact witnesses, all
               enclosures exclude zero).
O4-O7, NC3-NC7, O9/W1: NOT ATTEMPTED THIS PHASE (out of scope).
```

Protected status: unchanged; every flag remains false. Named blocks are
reported as victories per the standing culture.
