# Stage 8 Task 4a Finite Nonzero-R Reference Exact Probe-Source Computation V001

Date: 2026-08-02  
Task: 4a  
Lane: CODEX LANE 1  
Status: **SEALED FINITE RESTRICTION TARGET FOR P5**

Marks on premise-dependent positives:

```text
TYPE-P | premises: DoR-008, DoR-009, DoR-013, DoR-014
```

Gates:

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 0. Lead result

**The exact finite mixed retarded-candidate block remains zero and
`p_[A]`-free with the independent bilocal probe switched on.** At every finite
`N`, for every admitted ordered-rank class `[A]`, and at every nonzero probe in
the local Log domain, the finite scalar germ is

```text
Z_ref,N[J,R]
  =(1-p)+p exp[-Q_N(R)/2] product_(j=1)^N r_j^n,

r_j:=conjugate(z_(-,j))z_(+,j),
n in {+1,-1}.
```

The probe changes the effective charged weight from `p` to

```text
omega_R
  := p exp[-Q_N(R)/2]
      / (1-p+p exp[-Q_N(R)/2]).
```

Consequently the finite difference/difference Hessian carries
`omega_R(1-omega_R)`, and the nonzero `J_delta/R_delta,delta` mixed derivative
carries the same factor. But the exponent contains no `J_c` direction. The
exact Keldysh Hessian therefore remains

```text
H_W^(J,J)(R)
  = [[0,0],
     [0,i hbar omega_R(1-omega_R) ell_N tensor ell_N]]_(c,delta),

H_W^(J,J)(R)_(delta,c)=0.
```

No division or normalization removes `p`; the retarded-candidate block is
`p`-free because it is structurally zero. The probe-dependent
difference/difference and `J_delta/R_delta,delta` blocks are **not** `p`-free.

A second exact boundary is load-bearing. Equal linear histories with an
independent nonzero bilocal probe do not give unity:

```text
Z_ref,N[J_delta=0,R]
  =1-p+p exp[-Q_N(R)/2].
```

Unity is recovered on the full physical zero-source surface `J=R=0` (and on
probe-null directions with `Q_N(R)=0`). This is not a violation of the sealed
equal-history law: the original law has no independent `R` port, and the
PhysicalLogGerm authority expressly limits normalization to the physical
trace-preserving source surface.

```text
FINITE_NONZERO_R_REFERENCE_CONSTRUCTED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

FINITE_NONZERO_R_MIXED_RETARDED_BLOCK = ZERO_AND_P_FREE | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

NONZERO_FINITE_RETARDED_BLOCK_APPEARS_WITH_R_PROBE = false | TYPE-R |
  test: exact finite Hessian has no common-linear-source leg

ARBITRARY_NONZERO_R_EQUAL_HISTORY_VALUE_IS_UNITY = false | TYPE-R |
  test: exact sourced value is 1-p+p exp[-Q_N(R)/2]
```

The conclusion is finite and source-analytic. It does not prove that a later
physical retarded response is a continuum effect. It proves the narrower
statement P5 must respect: no direct finite scalar-germ restriction may
produce a nonzero `(delta,c)` block from this probe port. Any nonzero physical
response must enter through an additional physical raw-`G`, inversion,
stationarity, contour/boundary, or background operation and must pass this
restriction test.

## 1. Preflight, currency, scope, and authorities

### 1.1 Preflight

```text
DOES_THE_OBJECT_EXIST?  NO at start -- Q-274 names it TYPE-U
IS_THE_VERSION_CURRENT? YES -- P2 V002 at Q-277
ARE_ITS_INPUTS_PRESENT? YES -- finite law, germ ports, calculus, and Keldysh map
```

The relay snapshot named register head Q-277. The register advanced to Q-278
before construction. Q-278 does not supersede this finite task; it confirms
that the complete P3 measure, contour, boundary, and unbounded-domain fields
remain absent. Those objects are not used here.

### 1.2 Roots and exclusions

Roots entered:

```text
gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003/
/Users/bgm/MB Work/alpha_supervision/
/Users/bgm/MB Work/alpha-program-archive/workspace/
```

Excluded:

```text
a32_holdout/
custodian_private/
all continuum P3/P5 constructions;
all response evaluation, residual solving, rank selection, and measured comparison.
```

### 1.3 Frozen authorities

| Authority | SHA-256 | Use |
|---|---|---|
| `STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_FUNCTIONAL_RESULT_V001.md` | `2cd1ffcefd68ac03c6c09a4eca0dc9fe8d1adc8ac564cc0d050dfd41d79e6d0f` | exact finite law, holonomy product, gauge action, equal-history and zero-extension checks |
| `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V001.md` | `112a6658ef09ae9c309e2ff8b567d71c88e08e3692761162a0fb81fd1fdb3975` | explicit `J/R` ports, C-A/C-B definitions, gauge covariance |
| `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V004.md` | `d4cdbb6623797df6accb7dc9b24134d179bfc8e8d039c585d5c91ae23255869e` | live retained germ and symbolic `p_[A]` family |
| `STAGE8_TASK4A_P2_PHYSICAL_SOURCE_TOPOLOGY_AND_DIFFERENTIAL_CALCULUS_CONSTRUCTION_V002.md` | `40b2af34443e051fffdc7bf2ec7025c811a98c501a82d19164596ee6f37f00c1` | current source topology, calculus, and finite naturality |
| `STAGE8_TASK4A_P4_PHYSICAL_LOG_GERM_ON_P2_CALCULUS_CONSTRUCTION_V001.md` | `b4c77ea948a02f3736fc824976f9ebd6381deff35f5c339a646739ea159725c5` | W convention, local branch, and comparison target |
| `STAGE8_TASK4A_FINITE_HESSIAN_TO_DELTAPHI_TRANSPORT_MAP_CONSTRUCTION_AND_P_CH_TRACE_V001.md` | `70185aa842bc500724719c65bd66b5f07005e2214b97be0d35e07fd029d5c68c` | exact Keldysh transform and Q-243 `R=0` block |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_U3_DOR008_DOR009_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md` | `b0118d89e0b4b321fbf9caab5bfb811a0b5fd572e808d02615ee8503db2bc1ac` | Q-239 finite quotient and sequential maps |
| `STAGE8_TASK4A_P3_SECOND_ATTACK_LAW_SIDE_CONSTRUCTION_AND_NARROWED_STOP_V001.md` | `8e9a09c104f4b6352263591037b2e0bb9a82b659aa1b6276cdd48117f872acec` | Q-278 current continuum boundary |

This computation starts from the live SG4-1 finite restriction and derives
its nonzero-probe derivatives independently. P4 is used as a convention and
comparison authority, not as the derivation of the table below.

## 2. Symbol and object distinctions

Four collisions matter here:

1. `R` in `Z_ref,N[J,R]` is the **independent symmetric bilocal source**.
   It is not the ready record vector, written here as `|Ready_N>`.
2. `Z_law,N[a_+,a_-]=product_j r_j^n` is the charged holonomy product from
   the ratified law. `Z_ref,N[J,R]` is the scalar source-state generating
   functional `(1-p)+p exp(Xi)`. They are not the same object.
3. `F_law,N=P_0+Z_law,N P_ch` is the record-sandwiched source operator.
   `F_src,N=P_0+exp(Xi_N[J,R])P_ch` is the source-inserted germ operator.
4. `omega_R` below is an effective charged weight. It is not the Q-239 orbit
   map `q_N` and not a new state parameter.

The scalar coefficient is always the unevaluated live family member

```text
p:=p_[A],  0<p<1.
```

No ordered rank pair is selected.

## 3. Exact finite source ports

### 3.1 Linear source `J`

The germ source carrier and Keldysh transform are fixed at
`STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V001.md:180-240`:

```text
J_c=(J_++J_-)/2,
J_delta=J_+-J_-.
```

The finite faithful-character exponent is, at `:256-280`,

```text
L_n,N(J)=i n sum_(j=1)^N J_delta,j.
```

The same lines prove that U1 orbit symmetrization leaves this exact finite
character exponent unchanged. In the ratified finite dynamics, this is the
logarithmic chart of

```text
product_j conjugate(chi_n(h_j[a_-]))chi_n(h_j[a_+])
 =product_j r_j^n.
```

Thus `J` couples to the charged source projector through the relative-holonomy
character. It does not couple to the neutral projector.

Define the real accumulated difference covector

```text
ell_N(j):=sum_(j=1)^N j_delta,j.
```

Then

```text
L_n,N(j)=i n ell_N(j),
D_(J_c)L_n,N=0.
```

### 3.2 Bilocal source `R`

The independent finite bilocal source is a symmetric operator on the doubled
finite cell carrier. The exact Keldysh source transform and C-B functional at
`STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V001.md:234-306` are

```text
R_(c,delta)=T_CTP^T R_(+,-) T_CTP,

B_delta,N(R)=Tr(P_N R_delta,delta P_N),

Q_N(R)=Q_delta,N^Theta(R)
  =(1/2)[B_delta,N(R)+conjugate(B_delta,N(Theta_R R))].
```

`R` therefore couples only through the U1-real, same-cell,
difference/difference trace, inside the same charged-event exponent as `J`:

```text
Xi_n,N[J,R]=L_n,N(J)-(1/2)Q_N(R).
```

It does not introduce a separate Gaussian, cross-cell kernel, contact term,
or neutral-sector coupling. This is the C-B placement ratified with the germ;
it is not an extra operator insertion already present in DoR-009's finite law.

### 3.3 Concrete nonzero probe family

For each finite `N>=1`, choose the U1-real symmetric source whose only
nonzero Keldysh block is

```text
(R_eta,N)_delta,delta := eta |e_1><e_1|,
```

with symbolic real `eta !=0`, all other branch blocks zero, and
`|eta|/2` inside the predeclared local Log neighborhood. Then

```text
Q_N(R_eta,N)=eta.
```

This probe is finite, gauge invariant under common U(1) conjugation, and
compatible with every zero extension `N<=M`. It is an explicit member, not an
anonymous nonzero source. The general formulas below apply to every finite
`R_0`; the `eta` family is the frozen reference instance used for the tables.

## 4. Closed form with both sources on

The live finite source-inserted operator and scalar generating functional are

```text
F_src,N[J,R]
  :=P_0+exp(Xi_n,N[J,R])P_ch,

Z_ref,N[J,R]
  :=Tr_A(F_src,N[J,R]rho_[A])
   =(1-p)+p exp(Xi_n,N[J,R]).                         (NR-1)
```

On the finite holonomy chart,

```text
exp(L_n,N(J))=product_(j=1)^N r_j^n,
```

so

```text
Z_ref,N[J,R]
  =(1-p)+p exp[-Q_N(R)/2] product_(j=1)^N r_j^n.     (NR-2)
```

This is closed at every finite `N`. The `J` part is pure phase on the unitary
history locus. A real nonzero `R_eta,N` contributes the exact attenuation
factor `exp(-eta/2)`; it is not relabeled as a phase.

For the first two finite stages:

```text
Z_ref,1[J,R_eta,1]
  =(1-p)+p exp(-eta/2) r_1^n,

Z_ref,2[J,R_eta,2]
  =(1-p)+p exp(-eta/2) r_1^n r_2^n.
```

Define the finite logarithm and response-facing functional on the frozen local
branch:

```text
Gamma_log,N:=Log_0 Z_ref,N,
Gamma_fin,N:=-Log_0 Z_ref,N,
W_N:=-i hbar Log_0 Z_ref,N.                          (NR-3)
```

The Q-274/Q-276 convention is preserved exactly.

## 5. Exact general derivative identity

Let

```text
x:=Xi_n,N[J,R],
a:=p exp(x),
Z:=1-p+a,
omega:=a/Z,
lambda(j,r):=L_n,N(j)-(1/2)Q_N(r).
```

Because `Xi_n,N` is linear, direct differentiation of (NR-1) gives

```text
D Z[h]=a lambda(h),
D^2 Z[h_1,h_2]=a lambda(h_1)lambda(h_2),             (NR-4)

D Log_0 Z[h]=omega lambda(h),
D^2 Log_0 Z[h_1,h_2]
  =omega(1-omega)lambda(h_1)lambda(h_2),             (NR-5)

D Gamma_fin[h]=-omega lambda(h),
D^2 Gamma_fin[h_1,h_2]
  =-omega(1-omega)lambda(h_1)lambda(h_2),            (NR-6)

D W[h]=-i hbar omega lambda(h),
D^2 W[h_1,h_2]
  =-i hbar omega(1-omega)
     lambda(h_1)lambda(h_2).                         (NR-7)
```

An independent algebra check is immediate:

```text
D omega
  =D(a/Z)
  =omega(1-omega) D x,
```

which reproduces (NR-5) without using P4's derivative table.

## 6. Nonzero-probe reference point and derivative table

Freeze

```text
s_eta,N:=(J=0,R=R_eta,N),
u_eta:=exp(-eta/2),
Z_eta:=1-p+p u_eta,
omega_eta:=p u_eta/Z_eta,
kappa_eta:=omega_eta(1-omega_eta)
          =p(1-p)u_eta/(1-p+p u_eta)^2.              (NR-8)
```

Every expression remains symbolic. Neither `p` nor `eta` is evaluated.

### 6.1 First derivatives of `Z_ref,N`

At `s_eta,N`:

| Direction | Exact derivative | symbolic weight |
|---|---|---|
| `J_c` | `0` | `p`-free zero |
| `J_delta` | `i n p u_eta ell_N(j_delta)` | `p u_eta` |
| `R` | `-(p u_eta/2) Q_N(r)` | `p u_eta` |

### 6.2 First derivatives of `Gamma_fin,N=-Log Z_ref,N`

| Direction | Exact derivative | symbolic weight |
|---|---|---|
| `J_c` | `0` | `p`-free zero |
| `J_delta` | `-i n omega_eta ell_N(j_delta)` | `omega_eta` |
| `R` | `+(omega_eta/2) Q_N(r)` | `omega_eta` |

### 6.3 First derivatives of `W_N=-i hbar Log Z_ref,N`

| Direction | Exact derivative | symbolic weight |
|---|---|---|
| `J_c` | `0` | `p`-free zero |
| `J_delta` | `hbar n omega_eta ell_N(j_delta)` | `omega_eta` |
| `R` | `+(i hbar/2)omega_eta Q_N(r)` | `omega_eta` |

The first `R` derivative is an exact finite source derivative. It is not
identified with a physical raw correlator; that identification still requires
P3/P5's quotient, measure, contacts, domains, connected subtraction, and
physical operator typing.

### 6.4 Complete second-derivative table for `W_N`

Write the source coordinate order as `(J_c,J_delta,R_delta,delta)`. The exact
nonzero entries are:

| Block | Exact bilinear form at `s_eta,N` | symbolic weight |
|---|---|---|
| `(delta,delta)` | `i hbar kappa_eta ell_N tensor ell_N` | `kappa_eta` |
| `(delta,R)` and `(R,delta)` | `-(hbar n/2)kappa_eta ell_N tensor Q_N` and transpose | `kappa_eta` |
| `(R,R)` | `-(i hbar/4)kappa_eta Q_N tensor Q_N` | `kappa_eta` |

Every block with a `J_c` leg is exactly zero:

```text
D^2_(c,c)W_N=0,
D^2_(c,delta)W_N=0,
D^2_(delta,c)W_N=0,
D^2_(c,R)W_N=0,
D^2_(R,c)W_N=0.                                    (NR-9)
```

The `J_delta/R` mixed derivative is nonzero in general. It must not be
name-matched to the retarded `(delta,c)` block: `R` is a bilocal probe port,
while `J_c` is the common linear-source coordinate. Their domains and roles
are different.

## 7. Keldysh rotation and retarded-candidate block

In the branch basis, the `J/J` Hessian has the exact rank-one shape

```text
M_DD=[[1,-1],[-1,1]].
```

Q-243's exact rotation gives

```text
T_CTP^T M_DD T_CTP=[[0,0],[0,1]].
```

The probe changes only the scalar coefficient. Therefore

```text
H_W,N^(J,J)(R_eta)
  =[[0,0],
    [0,i hbar kappa_eta ell_N tensor ell_N]]_(c,delta),

P_R^fin(H_W,N(R_eta))
  :=H_W,N(R_eta)_(delta,c)
   =0.                                                (NR-10)
```

This holds for every finite `N`, every admitted `[A]`, both faithful character
orientations, and every finite `R` in the local source domain, not only the
explicit `R_eta` family. The reason is structural:

```text
D_(J_c)Xi_n,N=0.
```

```text
FINITE_NONZERO_R_KELDYSH_ROTATION_EXECUTED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

FINITE_NONZERO_R_ORDERED_RETARDED_BLOCK = 0 | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

P_DEPENDENCE_IN_FINITE_NONZERO_R_RETARDED_BLOCK = false | TYPE-R |
  test: the block is identically zero before any p-dependent coefficient acts

P_DEPENDENCE_IN_FINITE_NONZERO_R_NOISE_AND_JR_BLOCKS = true | TYPE-P |
  form: kappa_eta=p(1-p)exp(-eta/2)/(1-p+p exp(-eta/2))^2
```

## 8. Certificate battery

### 8.1 Equal histories with the probe on

Equal histories set every relative holonomy to one, hence `J_delta=0`. The
exact sourced value is

```text
Z_ref,N[a,a,R]=1-p+p exp[-Q_N(R)/2].                 (C-NR1)
```

Thus:

```text
EQUAL_HISTORY_SOURCED_COLLAPSE_CERTIFIED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014 |
  value: 1-p+p exp[-Q_N(R)/2]

FULL_ZERO_SOURCE_NORMALIZATION_CERTIFIED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014 |
  condition: J_delta=0 and R=0

PROBE_NULL_NORMALIZATION_CERTIFIED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014 |
  condition: J_delta=0 and Q_N(R)=0
```

The stronger statement `Z=1` at arbitrary nonzero bilocal source is refuted
by (C-NR1). The PhysicalLogGerm specification at
`STAGE8_CTP_PHYS_INPUT_PACKAGE_ITEM2_PHYSICAL_LOG0_GERM_SPEC_V001.md:196-203`
already states that unitarity does not imply `Z=1` for an arbitrary
cross-branch bilocal source.

### 8.2 `R=0` internal falsifier

Setting `R=0` gives

```text
u_eta -> 1,
omega_eta -> p,
kappa_eta -> p(1-p).
```

Then

```text
Z_ref,N[J,0]=(1-p)+p product_j r_j^n,

D_(J_delta)W_N|_0=hbar n p ell_N,

D^2_(delta,delta)W_N|_0
  =i hbar p(1-p)ell_N tensor ell_N,

D^2_(delta,c)W_N|_0=0.
```

These are exactly Q-243's finite coherent, noise, and ordered-retarded
results with the Q-274/Q-276 W convention. Q-243 did not define the independent
`R` derivatives; those new rows are not falsely reported as prior matches.

```text
R_ZERO_RESTRICTION_REPRODUCES_Q243_J_SECTOR = PASS | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
```

### 8.3 Sequential compatibility with probes on

For `N<=M`, zero extension appends identity holonomies and zero bilocal
components. Therefore

```text
L_n,M(iota_NM J)=L_n,N(J),
Q_M(iota_NM R)=Q_N(R),

Z_ref,M[iota_NM J,iota_NM R]=Z_ref,N[J,R].           (C-NR2)
```

The same equality holds for every derivative after zero-extending its
directions, by P2 V002's restriction naturality. The explicit first-cell
`R_eta` probe is fixed by every such zero extension.

```text
NONZERO_R_ZERO_EXTENSION_CERTIFICATE = PASS | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
```

### 8.4 Gauge covariance and Q-239 quotient descent

Q-239 constructs the common-gauge quotient coordinates

```text
r_j=conjugate(z_(-,j))z_(+,j),
Q_N^phys isomorphic to U(1)^N.
```

Each `r_j` is invariant under the simultaneous vertex-gauge action. The germ
authority at `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V001.md:522-530`
states that `Q_N(R)` is the U1-symmetrized trace of the covariantly transformed
bilocal source and is invariant under common unitary conjugation. Hence

```text
Zbar_ref,N(r,R)
  :=1-p+p exp[-Q_N(R)/2] product_j r_j^n            (C-NR3)
```

is a well-defined quotient function and

```text
Z_ref,N=Zbar_ref,N compose q_N
```

on the history variables, with the covariant bilocal-source action understood.

```text
NONZERO_R_COMMON_GAUGE_COVARIANCE = PASS | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

NONZERO_R_Q239_QUOTIENT_DESCENT = PASS | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
```

### 8.5 U1 reality

The ratified source involution gives

```text
Xi_(-n)(Theta_src(J,R))=conjugate(Xi_n(J,R)).
```

Since `p` is real,

```text
Z_(-n)(Theta_src(J,R))=conjugate(Z_n(J,R)),
W_(-n)(Theta_src(J,R))=-conjugate(W_n(J,R)).
```

The derivative tables transform accordingly. The `n=-1` orientation reverses
the first `J_delta` derivative and leaves every `n^2` `J/J` bilinear
unchanged.

```text
NONZERO_R_U1_REALITY_CERTIFICATE = PASS | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014
```

## 9. P5 restriction-target interface

Define the exact finite reference tuple

```text
FiniteNonzeroRRef_N := (
  source_domain       = E_src,N,
  probe_family        = {R_eta,N},
  exponent            = Xi_n,N,
  scalar_functional   = Z_ref,N,
  finite_minus_log    = Gamma_fin,N,
  response_functional= W_N,
  first_J             = D_J W_N,
  first_R             = D_R W_N,
  Hessian_blocks      = D^2_(J,J),D^2_(J,R),D^2_(R,R),
  Keldysh_block       = H_W,N^(J,J),
  retarded_candidate  = H_(delta,c)=0,
  certificates        = C-NR1,C-NR2,C-NR3,U1,R=0
).
```

P5's future finite restriction must reproduce, on this same source convention:

1. the sourced scalar value (NR-2);
2. the first `R` derivative and all `J/R` derivative factors in Section 6;
3. the full Keldysh block matrix (NR-10), not only its zero entry;
4. the sourced equal-history value (C-NR1), not an incorrectly imposed unity;
5. zero-extension, quotient, and U1 certificates.

A mismatch on the same finite carrier, source directions, branch convention,
and probe is the DoR-008 falsifier. Different physical quotient, measure,
contact, or boundary data are not silently treated as a failed comparison;
they must first be supplied and intertwined by P3/P5.

```text
P5_FINITE_NONZERO_R_RESTRICTION_TARGET_READY = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

P5_PHYSICAL_RAW_G_OR_RETHESS_BUILT_HERE = false | TYPE-S |
  roots: this finite reference and its frozen authorities |
  exclusions: P3/P5 continuum package |
  query: "raw G|inverse|RetHess_phys|stationary|contour boundary value"
```

## 10. Kill passes and final typed ledger

### 10.1 No continuum import

No measure, physical contour, boundary/contact prescription, unbounded domain,
raw correlator inverse, stationary background, or completed response operator
is used. Q-278's four continuum-dynamics fields remain open.

### 10.2 Rank discipline

Every formula is family-wide in the symbolic `p_[A]`. No ordered rank pair or
ratio is instantiated.

### 10.3 W convention

The calculation keeps the three objects distinct:

```text
Gamma_log=Log_0 Z,
Gamma_fin=-Log_0 Z,
W=-i hbar Log_0 Z.
```

At `R=0` the signs reproduce Q-274 and P2 V002 exactly.

### 10.4 Null directions exposed

The finite functional depends on `R` only through `Q_N(R)`. Every nonzero
source in `ker Q_N` is invisible to this reference and all its displayed
derivatives. This is a real null space of C-B, not a proof that the physical
bilocal source has no other content. Whether the later physical quotient and
inverse can accommodate it remains P5's standing test.

```text
R_PROBE_NULL_SPACE = ker Q_N
C_B_SURVIVES_P5_PHYSICAL_INVERSION = NO_VERDICT |
  prerequisite: physical quotient, measure, boundary/contact domains,
                raw-G inverse, and retarded extraction
```

### 10.5 Final ledger

```text
FINITE_NONZERO_R_REFERENCE_EXISTS = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

FINITE_NONZERO_R_CLOSED_FORM_EXISTS = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

FINITE_NONZERO_R_FIRST_J_AND_R_DERIVATIVES_EXIST = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

FINITE_NONZERO_R_MIXED_JR_DERIVATIVE_EXISTS = true | TYPE-P |
  form: -(hbar n/2)kappa_eta ell_N tensor Q_N

FINITE_NONZERO_R_MIXED_RETARDED_CANDIDATE = ZERO_AND_P_FREE | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

FINITE_NONZERO_R_NOISE_BLOCK_P_FREE = false | TYPE-R |
  test: exact coefficient is kappa_eta

FINITE_NONZERO_R_EQUAL_HISTORY_UNITY = false | TYPE-R |
  test: exact sourced value C-NR1

R_ZERO_INTERNAL_FALSIFIER = PASS | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

NONZERO_R_SEQUENTIAL_CERTIFICATE = PASS | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

NONZERO_R_GAUGE_QUOTIENT_CERTIFICATE = PASS | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014

RANK_VALUE_SELECTED = false | TYPE-S |
  roots: all formulas and tables in this artifact |
  exclusions: none within finite reference scope |
  query: "r_0|r_ch|rank pair|evaluate p"

CONTINUUM_OBJECT_IMPORTED = false | TYPE-S |
  roots: exact input inventory and construction trace |
  exclusions: P3/P5 continuum layer |
  query: "measure|contour|boundary|unbounded|inverse|RetHess_phys"

FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-S |
  roots: this computation |
  exclusions: barred physical evaluations |
  query: "structural step stopped by fence"
```

No coupling, scale, residual root, response value, or measured constant was
computed, bounded, or compared. No protected holdout was entered. No register,
tracker, plan, or git object was modified.
