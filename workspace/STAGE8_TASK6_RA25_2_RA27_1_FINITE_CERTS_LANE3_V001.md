# STAGE 8 / TASK 6 / BLOCKED-REPAIR — RA25-2 + RA27-1 FINITE CERTIFICATES

Date: 2026-08-06  
Lane: Codex Lane 3 (SOL, high effort)  
Task: PASTE 625  
Custody: derivation by Codex Lane 3; Dario reviews  
Status: **HELD-OUT FINITE CERTIFICATES; NO LINEAGE TOUCH**

## Lead determination

```text
REGISTER_COMMISSION = Q-560
REGISTER_HEAD_AT_FINAL_PREFLIGHT = Q-561
  live append Q-561 concerns the A35 evaluator specification review;
  it neither supersedes nor modifies Q-560 or the two finite-work targets

RA27-1 = PROVEN on the local reconstructed six-dimensional tensor space
RA25-2 = COMPLETE on the strict joint-fixed-space target of record

LINEAGE_LP_SHA256 =
  4c04e4aae924f87736809d2a119a0fdeda271f77cd5141d26aa453cfc5c4abc2

LINEAGE_DISPOSITION = HELD OUT
  sealing and mirroring this artifact does not add it to LINEAGE_LP;
  no thirty-row rerun is triggered;
  only a later explicit batched lineage act may import it

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

[PROVABLE] Both certificates are exact structural algebra on frozen finite
subjects. Neither calculation evaluates a physical quantity, binds a member,
runs a fixed point, executes an end test, or consults a measured constant.

---

## 0. Preflight, authorities, scope, and custody

### 0.1 Access, head, no-clobber, and packet integrity

[PROVABLE] The cleanroom, archive workspace, and archive supervision roots were
readable. At the final preflight the living questions-settled register had
advanced from the commissioned Q-560 to Q-561. The append is the A35 evaluator
specification review and is unrelated to these certificates, so the stated
live-append tolerance applies. The register is cited by **entry Q-560**, not by
whole-file hash.

[PROVABLE] Before writing, the requested artifact name and its
`.seal.sha256` sidecar were absent in both the cleanroom and the archive
workspace.

[PROVABLE] The sealed packet verifier was rerun:

```text
manifest rows = 113
OK            = 113
FAILED        = 0
```

### 0.2 Hash-verified authorities

| Role | Sealed source | SHA-256 | Load-bearing content |
|---|---|---|---|
| repair inventory | `STAGE8_TASK6_A25_A27_SCOPING_LANE3_V002.md` | `02bbe362622bf560d83f222812d78726a0e650da8d9ba7fae6f1b65bd4f66094` | strict `Fix_L` target; RA25-2 and RA27-1 finite-work classifications; repair-map boundaries |
| packet closure | `review_packets/STAGE7_QSPEC_CANDIDATE_V001/STAGE7_PACKET_MANIFEST_V001.sha256` | `9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311` | pins all 113 packet members |
| governing finite subject | packet `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` | `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a` | carriers, source-fiber orientation rule, periodic shifts, baseline `[U_0]`, ordered bivector basis, Lorentzian Hodge conventions |
| executed thirty-row board | `STAGE8_TASK6_LP_MATRIX_LEDGER_LANE3_V001.md` | `bc6c3e496ffd6e8d06cc3237e47a6a02b76faaa88b63b0ffb38684971c2d1362` | current row state and frozen lineage |
| custody correction | `STAGE8_TASK6_LP_MATRIX_LEDGER_REVIEW_DARIO_V001.md` | `a83289e67615d6faa2c1c942105ee6b595034f78d31fcf4e16ac5366fd1d7743` | A25/A27 are BLOCKED; full rerun follows only a lineage increment |
| current process law | supervision `LOCKED_PROCESS.md` | `0bff5ac1beec656386054505ca9ebb0c43e34332e94289c8f0f08188529b8d58` | surface anchor, living-file pins, appeal preflight, M-2 guards |

### 0.3 Exact scope of the two certificates

[PROVABLE] RA27-1 consumes only the frozen local data

```text
eta = diag(+1,-1,-1,-1),
epsilon_0123 = +1,
(*F)_(mu nu) = (1/2) epsilon_(mu nu rho sigma) F^(rho sigma),
basis B = (01,02,03,23,31,12).
```

Its subject is the reconstructed **local six-dimensional tensor space**. It is
not the finite global carrier `F_phys`.

[PROVABLE] RA25-2 consumes the admitted response baseline

```text
G_L = (Z/LZ)^4,
L = 2m+1 >= 3,
K_L = oriented two-skeleton of G_L,
[U_0] = flat plaquette holonomy and trivial four fundamental Wilson loops,
H_BID(K_L) = C_0(K_L;L) direct-sum C_1(K_L;L).
```

The calculation is not asserted for arbitrary periodic, non-flat `U`. The
flat/trivial-Wilson baseline is what makes the four shifts a commuting periodic
action and makes the uniform fixed-space answer possible.

### 0.4 Held-out lineage discipline

[PROVABLE] Q-560 states that these two certificates are held out of the audit
subject until a later explicit batched act. Therefore:

```text
seal this artifact
  -/-> increment LINEAGE_LP
  -/-> rerun A01--A29 plus A35
  -/-> move A25, A27, SPEC-SEAL, or any descendant seal
```

[YOURS] A later import would have to name this artifact as a lineage member,
produce the new lineage/content hash, and rerun all thirty rows. No delta-only
promotion is claimed here.

---

## 1. RA27-1 — exact local Lorentzian Hodge certificate

### 1.1 Coordinate convention and index raising

[PROVABLE] Write the lower-index component column in the frozen order as

```text
f = (F_01,F_02,F_03,F_23,F_31,F_12)^T.
```

Because `eta = diag(+1,-1,-1,-1)`, raising both indices gives

```text
F^01 = eta^00 eta^11 F_01 = -F_01,
F^02 = eta^00 eta^22 F_02 = -F_02,
F^03 = eta^00 eta^33 F_03 = -F_03,

F^23 = eta^22 eta^33 F_23 = +F_23,
F^31 = eta^33 eta^11 F_31 = +F_31,
F^12 = eta^11 eta^22 F_12 = +F_12.
```

Antisymmetry supplies the complementary ordered components:

```text
F^32=-F_23,  F^13=-F_31,  F^21=-F_12,
F^10=+F_01,  F^20=+F_02,  F^30=+F_03.
```

The last line includes both antisymmetry and the Lorentzian raising sign. It is
why the second application of the star returns a minus sign.

### 1.2 Every epsilon sign and every matrix entry

[PROVABLE] The epsilon signs below are obtained from inversion parity relative
to `0123`; the inversion counts are displayed so no sign is inserted by
assertion:

```text
0123: 0 inversions -> +       0132: 1 inversion  -> -
0213: 1 inversion  -> -       0231: 2 inversions -> +
0312: 2 inversions -> +       0321: 3 inversions -> -
2301: 4 inversions -> +       2310: 5 inversions -> -
3102: 4 inversions -> +       3120: 5 inversions -> -
1203: 2 inversions -> +       1230: 3 inversions -> -
```

For each output component, the two complementary ordered pairs cancel the
factor `1/2`:

```text
(*F)_01
 = (1/2)[epsilon_0123 F^23 + epsilon_0132 F^32]
 = (1/2)[(+1)(+F_23) + (-1)(-F_23)]
 = +F_23.

(*F)_02
 = (1/2)[epsilon_0213 F^13 + epsilon_0231 F^31]
 = (1/2)[(-1)(-F_31) + (+1)(+F_31)]
 = +F_31.

(*F)_03
 = (1/2)[epsilon_0312 F^12 + epsilon_0321 F^21]
 = (1/2)[(+1)(+F_12) + (-1)(-F_12)]
 = +F_12.

(*F)_23
 = (1/2)[epsilon_2301 F^01 + epsilon_2310 F^10]
 = (1/2)[(+1)(-F_01) + (-1)(+F_01)]
 = -F_01.

(*F)_31
 = (1/2)[epsilon_3102 F^02 + epsilon_3120 F^20]
 = (1/2)[(+1)(-F_02) + (-1)(+F_02)]
 = -F_02.

(*F)_12
 = (1/2)[epsilon_1203 F^03 + epsilon_1230 F^30]
 = (1/2)[(+1)(-F_03) + (-1)(+F_03)]
 = -F_03.
```

[PROVABLE] In particular, the frozen fifth coordinate is `31`, not `13`.
Replacing it by `13` without also transforming coordinates would reverse a
column/row sign and is not an allowed basis change.

### 1.3 Generated matrix

[PROVABLE] Reading the six displayed output equations row by row gives

```text
                 input columns: 01  02  03  23  31  12

J_star =                       [ 0   0   0   1   0   0 ]  output 01
                               [ 0   0   0   0   1   0 ]  output 02
                               [ 0   0   0   0   0   1 ]  output 03
                               [-1   0   0   0   0   0 ]  output 23
                               [ 0  -1   0   0   0   0 ]  output 31
                               [ 0   0  -1   0   0   0 ]  output 12

       = [ 0_3   I_3 ]
         [-I_3   0_3 ].
```

Equivalently, its columns show

```text
J_star e_01 = -e_23,   J_star e_02 = -e_31,
J_star e_03 = -e_12,   J_star e_23 = +e_01,
J_star e_31 = +e_02,   J_star e_12 = +e_03.
```

### 1.4 Exact square

[PROVABLE] Exact block multiplication yields

```text
J_star^2
 = [ 0_3   I_3 ] [ 0_3   I_3 ]
   [-I_3   0_3 ] [-I_3   0_3 ]

 = [0_3 0_3 + I_3(-I_3)      0_3 I_3 + I_3 0_3]
   [-I_3 0_3 + 0_3(-I_3)     (-I_3)I_3 + 0_3 0_3]

 = [-I_3   0_3]
   [ 0_3  -I_3]

 = [-1  0  0  0  0  0]
   [ 0 -1  0  0  0  0]
   [ 0  0 -1  0  0  0]
   [ 0  0  0 -1  0  0]
   [ 0  0  0  0 -1  0]
   [ 0  0  0  0  0 -1]

 = -I_6.
```

This is the complete RA27-1 certificate.

### 1.5 RA27-1 scope fence

[YOURS] The proved statement is exactly

```text
J_star^2 = -I_6
on span_R{01,02,03,23,31,12},
with the frozen eta and epsilon conventions.
```

The same real matrix has a formal complex-linear extension for Fourier
bookkeeping, but that extension is not consumed by this certificate; the
certified subject is the reconstructed local six-dimensional **real**
bivector/tensor space.

It does **not** assert any of the following:

```text
J_star preserves the full finite global F_phys carrier;
[M_record,J_star]=0;
kappa_record,E = kappa_record,B;
a physical Ref or J_ref exists;
a common-refinement response square commutes;
a boundary-to-volume estimate holds.
```

Thus C27.3--C27.5 are untouched, as are the separate C27.6 completion and all
physical coefficient questions.

---

## 2. RA25-2 — induced edge translations and the strict fixed-space census

### 2.1 Frozen periodic carrier and positive edge representatives

[PROVABLE] Let

```text
G_L = (Z/LZ)^4,     L=2m+1 >= 3,
e_nu(x): x -> x+nu,     nu in {0,1,2,3},
```

where `e_nu(x)` is the frozen positive representative in direction `nu`.
Throughout §2, `U_mu(x)` denotes a representative link transport of the
baseline gauge class `[U_0]`.
The source-fiber convention gives

```text
C_0 = direct-sum_(x in G_L) L_x,
C_1 = direct-sum_(nu=0)^3 C_(1,nu),
C_(1,nu) = direct-sum_(x in G_L) L_x,
a_nu(x) := a_(e_nu(x)) in L_x.
```

For each direction define the canonical source-fiber identification

```text
I_nu:C_0 -> C_(1,nu),
(I_nu psi)_(e_nu(x)) = psi_x.
```

No metric normalization or fiber representative is selected: the coefficient
of `e_nu(x)` and the vertex coefficient at `x` literally occupy the same
source fiber `L_x`.

### 2.2 The induced `C_1` action

[PROVABLE] The frozen vertex pullback is

```text
T_mu^(0):C_0 -> C_0,
(T_mu^(0) psi)_x = U_mu(x)^dagger psi_(x+mu).
```

The direction-preserving cellular translation induces, under the canonical
direct-sum identification,

```text
T_mu^(1)
 := direct-sum_(nu=0)^3 I_nu T_mu^(0) I_nu^(-1)
 : C_1 -> C_1.
```

Consequently every coefficient is carried by the displayed formula

```text
(T_mu^(1) a)_(e_nu(x))
 = U_mu(x)^dagger a_(e_nu(x+mu)),

T_mu^(1) = direct-sum_(nu=0)^3 T_mu^(0)
under C_1 = direct-sum_nu C_(1,nu).
```

[PROVABLE] The map is unitary in the frozen direct-sum Hermitian metric:

```text
||T_mu^(1)a||^2
 = sum_(nu,x) ||U_mu(x)^dagger a_(e_nu(x+mu))||^2
 = sum_(nu,x) ||a_(e_nu(x+mu))||^2
 = ||a||^2.
```

[YOURS] A nontrivial lattice translation moves the marked origin. It is
therefore **not** asserted to be an endomorphism in rooted `BareRec_2`, whose
morphisms preserve marked roots. The action above is derived directly on the
underlying periodic carrier (equivalently, between root-shifted copies) from
the frozen source-fiber decomposition. No sealed categorical arrow is
invented.

### 2.3 Flatness, commutation, period, and the odd periodic seam

[PROVABLE] On `[U_0]`, identity plaquette holonomy is the square equality

```text
U_lambda(x+mu) U_mu(x)
 = U_mu(x+lambda) U_lambda(x).
```

Hence on `C_0`, and componentwise on every `C_(1,nu)`,

```text
(T_mu T_lambda psi)_x
 = [U_lambda(x+mu) U_mu(x)]^dagger
     psi_(x+mu+lambda)

 = [U_mu(x+lambda) U_lambda(x)]^dagger
     psi_(x+lambda+mu)

 = (T_lambda T_mu psi)_x.
```

The trivial fundamental Wilson loop in direction `mu` gives

```text
(T_mu^(p))^L
 = W_mu(x)^dagger
 = I,
for p in {0,1}.
```

[PROVABLE] At the periodic seam `x_mu=L-1`, the index `x+mu` is read modulo
`L`, and

```text
U_mu(x)^dagger:L_(x+mu) -> L_x
```

is exactly the wrap transport already present in the formula. Translation
sends the positive representative `e_nu(x+mu)` to the positive representative
`e_nu(x)`; it never changes `e_nu` into `bar(e_nu)`. Therefore the seam sign is
`+1` for every `mu,nu`.

[PROVABLE] Compatibility with the frozen reversal rule can nevertheless be
checked explicitly. Since

```text
a_(bar e_nu(x)) = -U_nu(x) a_(e_nu(x)),
```

flatness gives

```text
(T_mu^(1)a)_(bar e_nu(x))
 = U_mu(x+nu)^dagger a_(bar e_nu(x+mu))

 = -U_mu(x+nu)^dagger U_nu(x+mu)
      a_(e_nu(x+mu))

 = -U_nu(x) U_mu(x)^dagger
      a_(e_nu(x+mu))

 = -U_nu(x)(T_mu^(1)a)_(e_nu(x)).
```

Thus the existing orientation sign is transported covariantly; no second
minus sign is created at a seam. Oddness contributes no sign. Its relevant
role here is to specify the admitted response sequence; the seam computation
above is exact for every admitted odd `L`.

### 2.4 The combined action and global parallel transport

[PROVABLE] Define

```text
T_tilde_mu
 := T_mu^(0) direct-sum T_mu^(1)
 : H_BID(K_L) -> H_BID(K_L).
```

The displayed commutation and period equalities make the four `T_tilde_mu` a
unitary action of `G_L` on the baseline carrier.

[PROVABLE] Flat plaquettes and trivial fundamental Wilson loops make parallel
transport from the origin path independent. Write

```text
P_x := U_(0->x):L_0 -> L_x,
P_0 = I_(L_0),
P_(x+mu) = U_mu(x) P_x.
```

Define five global mode maps:

```text
V:L_0 -> C_0,
(V z)_x = P_x z,

E_nu:L_0 -> C_1,
(E_nu b)_(e_rho(x)) = delta_(nu rho) P_x b,
nu=0,1,2,3.
```

[PROVABLE] Each displayed mode is jointly fixed. For the vertex mode,

```text
(T_mu^(0)Vz)_x
 = U_mu(x)^dagger P_(x+mu)z
 = U_mu(x)^dagger U_mu(x)P_xz
 = (Vz)_x.
```

For every edge direction,

```text
(T_mu^(1)E_nu b)_(e_rho(x))
 = U_mu(x)^dagger delta_(nu rho)P_(x+mu)b
 = delta_(nu rho)P_xb
 = (E_nu b)_(e_rho(x)).
```

### 2.5 Exact joint fixed space

[PROVABLE] The commissioned target is

```text
Fix_L
 := intersection_(mu=0)^3 ker(T_tilde_mu-I)
    subset H_BID(K_L).
```

Let `(psi,a)` lie in `Fix_L`. The vertex fixed equations are

```text
U_mu(x)^dagger psi_(x+mu)=psi_x
iff
psi_(x+mu)=U_mu(x)psi_x.
```

Path independence therefore yields

```text
psi_x=P_x psi_0,
psi=V(psi_0).
```

For each edge direction `nu`, the fixed equations are independently

```text
U_mu(x)^dagger a_nu(x+mu)=a_nu(x)
iff
a_nu(x+mu)=U_mu(x)a_nu(x),
```

so

```text
a_nu(x)=P_x a_nu(0),
a=sum_(nu=0)^3 E_nu(a_nu(0)).
```

Hence

```text
Fix_L
 = im(V) direct-sum im(E_0) direct-sum im(E_1)
             direct-sum im(E_2) direct-sum im(E_3)

 isomorphic to L_0^(direct-sum 5),

dim_C Fix_L = 5.
```

### 2.6 Two-sided completeness certificate

[PROVABLE] Define origin evaluation on the fixed space by

```text
ev_0:Fix_L -> L_0^(direct-sum 5),
ev_0(psi,a)
 = (psi_0,a_(e_0(0)),a_(e_1(0)),a_(e_2(0)),a_(e_3(0))).
```

Define the displayed reconstruction

```text
Phi:L_0^(direct-sum 5) -> Fix_L,
Phi(z,b_0,b_1,b_2,b_3)
 = (Vz, E_0b_0+E_1b_1+E_2b_2+E_3b_3).
```

At the origin `P_0=I`, so

```text
ev_0(Phi(z,b_0,b_1,b_2,b_3))
 = (z,b_0,b_1,b_2,b_3).
```

Conversely, the recurrences in §2.5 show at every vertex and positive edge

```text
Phi(ev_0(psi,a))=(psi,a).
```

Therefore

```text
ev_0 compose Phi = I_(L_0^5),
Phi compose ev_0 = I_(Fix_L).
```

The upper bound (five origin/source-fiber values determine every fixed vector)
and lower bound (the five displayed independent mode lines exist) coincide.
No strict fixed vector or strict fixed ray lies outside the display.

### 2.7 Projectivization of the whole fixed space

[PROVABLE] Since `L_0` is a complex line,

```text
InvRayKin_L
 := P(Fix_L)
 = P(L_0^(direct-sum 5))
 isomorphic to CP^4
```

for every admitted odd `L`. A temporary nonzero vector in `L_0` gives
homogeneous coordinates

```text
[c_v:c_0:c_1:c_2:c_3].
```

Changing that temporary vector multiplies all five coordinates by one common
nonzero scalar and changes no projective ray.

[PROVABLE] The **whole** `CP^4`, not five selected coordinate rays, is the
census. Its exact structural counts are:

```text
connected projective components = 1;
canonical invariant line generators = 5;
degree/address strata = 3;
nonempty coordinate-support strata = 2^5-1 = 31.
```

The three degree/address strata are:

| Stratum | Projective description | Degree | Root/address incidence |
|---|---|---|---|
| vertex only | `[c_v:0:0:0:0]`, one `CP^0` point | homogeneous degree 0 | parallel support at all `L^4` vertices, including root `0`; this is `P(im J_r,L)` |
| edge only | `[0:c_0:c_1:c_2:c_3]`, a full `CP^3` | homogeneous degree 1 | each nonzero direction coefficient has parallel support on all `L^4` positive edges of that direction, including the root-sourced and wrap edges |
| vertex-edge mixed | `c_v != 0` and `(c_0,c_1,c_2,c_3) != 0` | degree-inhomogeneous in `C_0 direct-sum C_1` | combines all-address vertex support with all-address support in every nonzero edge direction |

[PROVABLE] The support refinement is finite and exhaustive:

```text
1 vertex-only stratum;
15 edge-only strata, one for each nonempty subset of four edge directions;
15 mixed strata, one for the vertex coordinate plus each nonempty subset
  of edge directions;
total = 1+15+15 = 31.
```

The four constant edge-direction rays named in V011 are only the four
single-direction coordinate points inside the edge `CP^3`. Direction-mixed
edge rays and every vertex-edge mixed ray are included. The 31 support strata
are not 31 connected components; the complete projective fixed locus remains
one connected `CP^4`.

### 2.8 Exact scope distinction: fixed lifts versus projective eigenlines

[YOURS] The repair inventory and this commission explicitly define

```text
Fix_L = intersection_mu ker(T_tilde_mu-I),
InvRayKin_L = P(Fix_L).
```

The completeness claim in §§2.5--2.7 is for that **strict joint-fixed-space
census of record**.

[PROVABLE] There is a mathematically broader notion that must not be silently
confused with it. In the global parallel trivialization,

```text
H_BID(K_L) isomorphic to L_0 tensor C[G_L] tensor C^5.
```

A ray can be fixed by the *projectivized* action even when its vectors carry a
nontrivial common translation character. For

```text
k in {-m,...,m}^4,
chi_k(x)=exp(2 pi i (k dot x)/L),
```

define the five-dimensional character block by

```text
E_k
 := { (psi,a):
        psi_x = chi_k(x)P_x z,
        a_(e_nu(x)) = chi_k(x)P_x b_nu,
        (z,b_0,b_1,b_2,b_3) in L_0^5 }.
```

Direct substitution gives

```text
T_tilde_mu restricted to E_k
 = exp(2 pi i k_mu/L) I_(E_k),
P(E_k) isomorphic to CP^4.
```

Thus the broader projective fixed-point locus would be

```text
disjoint-union_(k in {-m,...,m}^4) P(E_k),
```

with `L^4` components; the strict `Fix_L` target is exactly its `k=0`
component. This displayed boundary is a semantic negative control, not a
broadening of RA25-2. No nonzero-character ray is mislabeled as a strict fixed
lift, and no claim about its physical preparation admissibility is made.

### 2.9 No admissibility or exclusion conclusion

[YOURS] This certificate enumerates kinematics only. It does not infer that an
edge-only or mixed ray is a lawful primitive preparation, and it does not infer
that one is excluded. Those predicates require the missing C25.1
first-opening/admissibility grammar and the later C25.3 theorem. In particular,
the root ray is not selected merely because its projectivization is a
singleton.

---

## 3. Consequence board

### 3.1 Repair-map fields filled

| Repair field | This artifact supplies | Exact disposition |
|---|---|---|
| RA27-1 / C27.2 | generated six-by-six local Lorentzian `J_star` and exact square | **closed inside this held-out certificate** |
| RA25-2 / C25.2 | induced `C_1` action, strict joint fixed space, whole projectivization, degree/address classification, and two-sided completeness proof | **census display supplied inside this held-out certificate** |

### 3.2 Fields untouched

```text
A25:
  C25.1 preparation/admissibility grammar                 untouched / TYPE-U;
  C25.3 lawful exclusion and full uniqueness              untouched;
  C25.4 connected response and uniform locality theorem   untouched / TYPE-U.

A27:
  C27.1 local geometric inputs already decided elsewhere  not repaired here;
  C27.3 physical Ref/J_ref realization                    untouched / TYPE-U;
  C27.4 response naturality squares                       untouched / TYPE-U;
  C27.5 boundary/contact subextensivity                    untouched / TYPE-U;
  C27.6 coefficient-invariance completion                 untouched / conditional.
```

[YOURS] Consequently A25 and A27 remain BLOCKED on the current lineage. Neither
certificate forms a physical response, proves locality, selects a preparation,
or establishes cellulation independence.

### 3.3 Thirty-row and seal-rail consequence

```text
current LINEAGE_LP member set = unchanged;
current thirty-row board      = unchanged;
A25 row                       = unchanged / BLOCKED;
A27 row                       = unchanged / BLOCKED;
SPEC-SEAL and descendants     = unchanged;
full rerun now                = not triggered.
```

[PROVABLE] This is Q-560's held-out discipline, not an inference from the
results. A later explicit batched import must increment the lineage and rerun
all thirty rows before either display can count as audit-subject evidence.

---

## 4. Battery

### 4.1 F_PLDEC

[PROVABLE] Both derivations are reader-free:

```text
inputs used:
  eta, epsilon, local ordered basis;
  K_L, [U_0], source fibers, periodic shifts, flatness, Wilson loops.

inputs not used:
  reader, p_loc, response coefficient, alpha, kappa_record,
  measured value, fixed point, end test, or physical evaluation.
```

Therefore no reader or desired output can feed either matrix sign or fixed-ray
classification.

### 4.2 Anti-tuning ledger

| Hazard | Control displayed here | Result |
|---|---|---|
| choose Hodge signs to obtain `-I` | every epsilon parity and every raised-index sign derived before squaring | clean |
| reorder the basis | frozen `(01,02,03,23,31,12)` carried, including `31` | clean |
| insert a Euclidean Hodge rule | Lorentzian `(+---)` raising signs displayed | clean |
| favor the root ray | whole strict `CP^4` projectivized | clean |
| omit mixed vertex-edge rays | mixed stratum and all 15 mixed support strata displayed | clean |
| hide a periodic seam sign | wrap transport and reversal compatibility calculated | clean |
| infer admissibility from the census | all admissibility/exclusion claims refused | clean |
| consult a coefficient or measured consequence | none appears in either derivation | clean |

```text
ANTI_TUNING = CLEAN
```

### 4.3 Surface anchor — geometry versus rails

#### Actual surface objects

```text
RA27-1:
  local reconstructed tensor coordinates
    (F_01,F_02,F_03,F_23,F_31,F_12),
  eta, epsilon, and the resulting local linear map J_star.

RA25-2:
  actual odd periodic K_L at baseline [U_0];
  vertices x, positive edges e_nu(x), wrap edges, source fibers L_x;
  root address 0, parallel transports P_x;
  C_0, C_1, H_BID and their four actual baseline shifts.
```

#### Organizing rails, not new physical inhabitants

```text
I_nu, V, E_nu, ev_0, and Phi are canonical bookkeeping maps on the
  displayed finite carrier;
the 31 entries are coordinate-support strata, not selected preparations;
the nonzero-character addendum marks a scope boundary, not a new
  preparation law;
no Ref, J_ref, response map, boundary object, or locality carrier is built.
```

### 4.4 R9 / quantification check

[PROVABLE] RA25-2 quantifies over every admitted odd `L` and every ray in the
whole strict `P(Fix_L)=CP^4`; it does not quantify over five selected
representatives. The actual baseline surface supplies the full five-dimensional
fixed space, and the two-sided origin-evaluation inverse proves the universal
claim on that space.

[PROVABLE] RA27-1 quantifies over exactly six frozen local basis coordinates
and displays every row. It does not quantify over the absent physical
refinement family or the global `F_phys` carrier.

```text
R9_QUANTIFICATION = CLEAN
```

### 4.5 M-2 three-guard search ledger

[PROVABLE] All 113 packet members were searched under fixed-string,
whitespace/hyphenation-normalized, and scope/synonym guards.

| Guard | Query family | Result |
|---|---|---|
| fixed string | `T_mu^(1)` | zero packet hits; zero was not treated as nonexistence |
| fixed string | `J_star` | governing V011 only, at the generation/square demand and downstream commutator/rejection clauses |
| scope/synonym | edge translation / source fiber / joint fixed / constant edge direction | V011's source-fiber carrier and named constant-direction rays; no pre-existing induced `C_1` matrix or completeness certificate |
| scope/synonym | Lorentzian Hodge / Hodge square / `epsilon_0123` / ordered bivector basis | governing V011 only at the frozen local test |
| false-friend sweep | `T_top`, `P_H`, cellular Hodge, Euclidean star | wrong types: symmetric topological tensor, Task-5 projector notation, or wrong signature/basis |

[YOURS] Nearby `J_1` realization maps were rejected as a justification for a
rooted translation endomorphism, because a nontrivial translation moves the
marked root. The unsealed root V011 drift and non-packet files were not used to
prove a packet-lineage statement.

### 4.6 Permanent negative controls

```text
NC-1  replacing 31 by 13 without coordinate transformation changes signs;
NC-2  Euclidean four-dimensional star would square to +I on two-forms and is
      not the frozen Lorentzian convention;
NC-3  omitting any of E_0,...,E_3 misses a displayed fixed edge mode;
NC-4  listing only five coordinate rays misses the CP^3 edge mixtures and all
      vertex-edge mixed rays;
NC-5  inserting (-1)^L at the seam double-counts orientation reversal;
NC-6  extending the result to arbitrary non-flat U loses commutation and the
      path-independent completeness proof;
NC-7  calling every projective eigenline a strict fixed lift conflates the
      nonzero-character blocks with Fix_L.
```

All seven negative controls are rejected by the displays above.

### 4.7 Self verb audit

| Verb used | Display that licenses it |
|---|---|
| `generated` for `J_star` | six epsilon/index expansions in §1.2 |
| `proved` for `J_star^2=-I_6` | exact block and full matrix multiplication in §1.4 |
| `induced` for `T_mu^(1)` | canonical source-fiber decomposition and formula in §2.2 |
| `commuting periodic action` | flatness and Wilson-loop equalities in §2.3 |
| `complete` for the strict fixed-space census | recurrences plus the two-sided `ev_0`/`Phi` inverse in §§2.5--2.6 |
| `whole projectivization` | `P(Fix_L)=CP^4` and exhaustive 31-stratum partition in §2.7 |
| `closes C27.2` / `supplies C25.2` | explicitly qualified as held-out repair-map fields in §3.1 |
| `untouched` for other conjuncts | negative scope lists in §§1.5, 2.9, and 3.2 |
| `LINEAGE_TOUCHED=false` | Q-560 custody display in §§0.4 and 3.3 |

No verb upgrades a declaration into an inhabitant, a held-out certificate into
current-lineage evidence, a strict fixed-space census into an admissibility
theorem, or a local Hodge identity into a physical response result.

---

J_STAR_CERT = J_star^2 = -I_6 displayed
CENSUS = complete (strict fixed-space: 1 connected CP^4; 5 line generators; 3 degree/address classes; 31 support strata)
ADMISSIBILITY_CLAIMS = none
LINEAGE_TOUCHED = false
VERB_AUDIT_SELF = CLEAN
