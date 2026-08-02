# STAGE8 Gen_Omega generative-origin rule V002 adversarial kill determination V001

Date: 2026-08-02

Status: RESULT -- GEN_OMEGA V002 DEAD AT THE DOR-013 GATE

Review target:

```text
STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V002.md
SHA-256:
479cfb89223106ae27de54742a09a52b37325618e95b2964ed0ad9bf58d75245
```

Register head checked at start and before freeze: Q-263.

This artifact is an independent adversarial review. It adopts nothing,
repairs nothing, and does not authorize DoR-013.

```text
A1_ANCHOR_TEST = KILLED
A2_FORCED_CHARGE_FORM = NOT_TRIGGERED_FOR_V002
A3_THREE_DOWNSTREAM_CONDITIONALS = SURVIVED_WITH_DEPENDENCY_BOUNDARY
A4_FINITE_OPERATIONAL_CERTIFICATE = WOUNDED
A5_TWO_MEMBER_ORIENTATION_FAMILY = KILLED
A6_SURVIVING_LIMB_REGRESSION = WOUNDED
A7_NONEMPTINESS_AUDIT = SURVIVED_AND_SUPPLIES_A1_COUNTEREXAMPLE

OVERALL_VERDICT = DEAD
DOR_013_RATIFICATION_READY = false | TYPE-R |
  test: arbitrary-state strict affine family and broken exchanged-root member
```

The decisive A1 counterexample is already V002's own nonemptiness witness.
For two distinct admitted charge-superselected states `sigma_0,sigma_1` and
one fixed nonzero mixing coefficient `lambda`, define

```text
P_i(tau)
  = lambda tau +(1-lambda)Tr(tau)sigma_i,
  i in {0,1}.
```

Both channels satisfy every V002 G1 condition. On every equal-trace
difference `Delta`, both have exactly the same action

```text
P_0(Delta)=P_1(Delta)=lambda Delta,
```

the same uniform input modulus, and the same finite operational certificate.
Only the state-valued affine offset differs. Thus V002's condition is the
input-faithfulness-only class Q-263 already refuted: it excludes pure reset
channels but leaves the complete invariant-state orbit open.

A second independent failure occurs in the root binary. With the ratified
`E_post` law `W(z)=D(z)S`,

```text
W(z)|r> = z|p>,
W(z)|p> = |r>.
```

The plus-root member carries the relative holonomy factor. The exchanged
minus-root member carries none; its branch overlap is identically one. It
therefore does not reproduce V002's own finite amplitude formula and fails the
charge/flux-access role. The two members are not a genuine E_post-symmetric
principal binary.

## 1. Scope and authorities

### 1.1 Roots entered

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha_supervision
```

### 1.2 Exclusions

```text
a32_holdout/custodian_private/                      NOT ENTERED
response evaluation, physical roots, alpha, scales  NOT PERFORMED
measured-constant comparison                        NOT PERFORMED
register, plan, tracker, git, commit, push           NOT TOUCHED
any hypothetical Gen_Omega V003                     NOT READ OR AUTHORED
```

### 1.3 Controlling artifacts

| Artifact | SHA-256 | Use |
|---|---|---|
| `STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V002.md` | `479cfb89223106ae27de54742a09a52b37325618e95b2964ed0ad9bf58d75245` | review target |
| `STAGE8_GEN_OMEGA_NONCIRCULAR_GENERATIVITY_NO_GO_ATTEMPT_V001.md` | `7000963e769362d87e17e36f06903e63aaa8caaeb284ee9c9f3676febe4f4163` | Q-263 orbit-collapse benchmark |
| `STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADVERSARIAL_KILL_DETERMINATION_V001.md` | `a340f0070dcab81eb44f177001da66db3061997a22e80c2b53086e5cf6145628` | Q-260 replacement/family kill |
| `STAGE8_TASK4A_MISSING_PHYSICAL_LAYER_CONSOLIDATED_SPEC_AND_CONSTRAINT_BATTERY_V001.md` | `241bf43f04aed7f215bad6ea80170a9c7733000896df839ac80974769d0a46c3` | Q-254 B1-B14 and P2-P11 dependencies |
| `STAGE8_MINIMAL_OMEGA_P5_COMMON_ORIGIN_ROLE_REALIZATION_ATTEMPT_V001.md` | `576da30f300a0362469d6b4f447423a2298efc0dd28a60f38057e7f4cc8bd888` | Q-242 root-not-bag test |

### 1.4 Exact V002 loci

```text
G1_v002 definition and modulus             V002:217-245
replacement exclusion                       V002:264-289
strict affine nonempty family               V002:291-334
family-level Q-242 argument                  V002:336-380
root binary and exchange square              V002:398-425
E_post law                                   V002:427-445
finite certificate claim                     V002:478-493
B5/B6/B9 conditionals                        V002:507-519
B14-v2                                       V002:525-551
channel fibers                               V002:561-603
battery                                      V002:606-633
strict affine self-kill discussion           V002:649-674
infinite-carrier statement                   V002:714-723
```

## 2. A1 -- the anchor test

### 2.1 What V002 actually constrains

V002 defines

```text
Delta_0^ss
  = {Delta charge-superselected : Tr(Delta)=0},

m_in(P)
  = inf {||P(Delta)||_1 : Delta in Delta_0^ss,
                          ||Delta||_1=1},
```

and admits channels with `m_in(P)>0` plus `Cert_IF(P)`. This constrains the
linear action on equal-trace differences. It does not constrain the affine
offset on the trace-one hyperplane.

That decomposition is exact. For any normalized input `tau_0`, every
trace-one input can be written

```text
tau=tau_0+Delta,
Tr(Delta)=0.
```

The difference-space certificate sees `P(Delta)` but not the independently
variable basepoint `P(tau_0)`.

### 2.2 Direct state-parameterized counterexample

Choose any two distinct normalized charge-superselected states
`sigma_0,sigma_1` admitted by the source-state family and freeze one symbolic
`lambda` in V002's strict mixing interval. Define

```text
P_0(tau)=lambda tau +(1-lambda)Tr(tau)sigma_0,
P_1(tau)=lambda tau +(1-lambda)Tr(tau)sigma_1.
```

V002 itself proves at lines 291-334 that every such member is normal, CPTP,
charge covariant, commuting with superselection, mixing, and has unique fixed
state `sigma_i`.

For every `Delta in Delta_0^ss`,

```text
P_i(Delta)=lambda Delta.
```

Therefore the two channels have:

```text
the same m_in=lambda;
the same lower-bound proof;
the same admissible finite-rank Delta_test;
the same Cert_IF data up to names;
the same transient action on the entire certified difference space;
the same d_law, G3, character, E_post and tensor grammar.
```

For normalized `tau`, their difference is

```text
P_0(tau)-P_1(tau)
  =(1-lambda)(sigma_0-sigma_1).
```

This is a constant state-valued affine offset. It is exactly the datum the
certificate does not test.

### 2.3 Orbit verdict

The invariant states are

```text
inv(P_0)=sigma_0,
inv(P_1)=sigma_1.
```

Because `sigma_0,sigma_1` were arbitrary, V002's invariant-state image is the
same open source-state family used to construct its witnesses. Uniformity of
the difference-space bound does not collapse that image.

```text
A1_VERDICT = KILLED
V002_CONTAINS_AN_ORBIT_COLLAPSING_ANCHOR = false | TYPE-R |
  test: P_0,P_1 above have identical certified difference action and distinct fixed states

V002_INPUT_FAITHFULNESS_COLLAPSES_STATE_ORBIT = false | TYPE-R |
  test: strict affine family parameterized by arbitrary sigma

Q260_STATE_FREEDOM_SURVIVES_V002 = true
```

V002's claim at lines 336-380 that different channels have independently
observable transient action is not true for this pair in the certified sense:
their complete action on `Delta_0^ss` is identical. Their only difference is
the state-valued trace component.

### 2.4 B14 consequence

B14-v2 is syntactically non-circular: it does not mention a desired state or
target. But its operational-generativity limb is too weak. Both counterexample
members pass B14-v2.2 with identical certificates while encoding distinct
state choices.

```text
B14_V002_IS_SYNTACTICALLY_NONCIRCULAR = true
B14_V002_EXCLUDES_STATE_RELABELLING = false | TYPE-R |
  test: strict affine pair with identical difference-space certificate
B14_V002_RESULT_FOR_DECLARED_FAMILY = FAIL
```

The circularity was removed; the physical defect was not.

## 3. A2 -- forced charge form

### 3.1 V002 does not trigger A2

V002 does not collapse the orbit, so no charge weighting is forced. For each
strict affine member,

```text
kappa_ch(P_(sigma,lambda))=Tr(sigma P_ch),
```

and `sigma` remains arbitrary. The fiber invariant is therefore parameterized,
exactly as V002 says.

```text
A2_FOR_V002 = NOT_TRIGGERED
V002_FORCES_ONE_KAPPA_CH = false | TYPE-R |
  test: choose sigma_0,sigma_1 with different charged marginals
```

### 3.2 What adding the Q-263 benchmark would force

On the finite-carrier reading used by Q-263, adding the missing bistochastic
anchor

```text
P(I_src)=I_src
```

to V002's faithfulness condition would force

```text
rho_P = I_src/Tr(I_src),

kappa_ch(P)
  = Tr(P_ch)/Tr(I_src)
  = dim(P_ch H_src)/dim(H_src).
```

Equivalently, when `I_src=P_0+P_ch`,

```text
kappa_ch(P)
  = dim(P_ch H_src)
    / (dim(P_0 H_src)+dim(P_ch H_src)).
```

This is a symbolic consequence only. No dimension, ratio, coupling, or
physical output is evaluated here.

### 3.3 Carrier-scope conflict

Q-263's benchmark explicitly uses the finite source carrier and normalized
identity. V002 line 721 instead says it avoids normalized identity on an
infinite carrier. The two descriptions are not interchangeable.

```text
SOURCE_CARRIER_FINITE_VS_INFINITE_SCOPE_CONFLICT = true

BENCHMARK_BISTOCHASTIC_ANCHOR_NONEMPTY_ON_V002_CARRIER = NO_VERDICT |
  missing: one authoritative carrier typing resolving whether I_src/Tr(I_src)
           is a normal admitted state on the physical source carrier
```

Thus "add unitality" is exact on Q-263's finite scope. If V002's infinite
scope is authoritative, a different orbit-collapsing normal anchor must be
constructed. Choosing a non-normalized identity on an infinite carrier would
empty or mistype the state family, not repair it.

## 4. A3 -- the three downstream conditionals

### 4.1 B5

```text
B5: prove RetHess_phys lies in a named ratified separation class.
```

This is non-circular and failure-capable. It is discharged by constructing
P2-P5 and the relevant class/restriction data through P6.

```text
B5_CIRCULAR = false | TYPE-R |
  test: condition can fail by physical-class mismatch
B5_DISCHARGEABLE_BY_P2_P6 = true
```

### 4.2 B6

```text
B6: instantiate physical restrictions and Tail_R.
```

This is non-circular and failure-capable. P5-P6 are its direct construction
site after P2-P4 provide the physical calculus/package.

```text
B6_CIRCULAR = false | TYPE-R |
  test: a nonzero restriction-invisible element is a failure witness
B6_DISCHARGEABLE_BY_P2_P6 = true
```

### 4.3 B9

```text
B9: prove a consumer-specific tail factorization or exhibit tail visibility.
```

This condition is non-circular, but P2-P6 alone cannot discharge it. They
construct the response class and tail. Q-254 assigns the actual consumers to
P9 (`p_loc/B_ind/C_EM/R_comp`), P10 (`DeltaPhi`), and P11 (Thomson). B9 waits
on the selected consumer after P2-P6.

```text
B9_CIRCULAR = false | TYPE-R |
  test: either factorization or a lawful tail witness can fail
B9_DISCHARGEABLE_BY_P2_P6_ALONE = false | TYPE-R |
  test: P2-P6 contain no selected alpha-facing consumer
B9_WOULD_BUILD = P2-P6 plus one selected consumer in P9/P10/P11
```

### 4.4 A3 verdict

```text
A3_VERDICT = SURVIVED_WITH_DEPENDENCY_BOUNDARY
```

None of the three is circular. Two are P2-P6 obligations; B9 is downstream of
P2-P6 at the selected consumer. This dependency correction does not cause the
A1 failure.

## 5. A4 -- finite operational certificate

### 5.1 Non-circularity

`Cert_IF` is defined before the invariant state is solved and does not mention
Q-242, `kappa_ch`, or a downstream target. Its intended content is therefore
non-circular.

```text
CERT_IF_IS_ANSWER_DEFINED = false | TYPE-R |
  test: expand V002:217-245
```

### 5.2 Finite witness versus uniform theorem

The finite-rank probe `Delta_test` certifies only

```text
P(Delta_test)!=0.
```

It does not certify the global condition

```text
inf_(Delta in Delta_0^ss, ||Delta||_1=1) ||P(Delta)||_1 > 0.
```

V002 says `Cert_IF` also "supplies the lower bound," but gives no certificate
format, finite basis reduction, exact matrix inequality, or verifier for an
arbitrary admitted channel. A single nonzero probe cannot perform that work.

For the explicit strict affine family the algebraic identity

```text
P_(sigma,lambda)(Delta)=lambda Delta
```

does prove the uniform bound exactly. Thus the witness class has a genuine
finite certificate, while the general V002 family has only a certificate
schema.

```text
A4_VERDICT = WOUNDED
STRICT_AFFINE_CERT_IF_IS_FINITE_AND_COMPLETE = true
GENERAL_G1_V002_FINITE_LOWER_BOUND_CERTIFICATE_INSTANTIATED = false | TYPE-U |
  would-build: an explicit finite certificate object and verifier proving the
               lower modulus for each non-affine admitted member
ONE_FINITE_PROBE_PROVES_UNIFORM_INPUT_MODULUS = false | TYPE-R |
  test: one-point nonvanishing does not bound an infimum over the unit sphere
```

This wound is repairable by restricting the family to a class with an exact
finite lower-bound theorem or by instantiating the missing certificate format.
It does not repair A1.

## 6. A5 -- the two-member root orientation family

### 6.1 Exact one-cell action

V002 keeps the ratified E_post law

```text
D(z)=diag(1,z,1),
S|r>=|p>,
S|p>=|r>,
W(z)=D(z)S.
```

Therefore

```text
W(z)|r>=z|p>,
W(z)|p>=|r>.
```

The plus member prepares `|r>`; the minus member prepares `|p>`.

### 6.2 Branch-relative factors

For forward/backward holonomies `z_+,z_-`, the plus member gives

```text
<r|W(z_-)^dagger W(z_+)|r>
  = conjugate(z_-) z_+.
```

The minus member gives

```text
<p|W(z_-)^dagger W(z_+)|p>
  = 1.
```

At finite `N`, the plus factor is the sealed product `Z_N`; the minus factor
remains one. Consequently V002's own Section 8 amplitude

```text
A_N^P=(1-kappa_ch(P))+kappa_ch(P)Z_N
```

holds for the plus root and not for the minus root. Under the minus root it
collapses structurally to the branch-independent unit factor.

### 6.3 Verdict

The zero-history exchange square commutes, but that is not enough: `E_post`
breaks the exchange away from zero history. The minus member has no physical
holonomy/flux access along its prepared trajectory and fails V002's claimed
C5/finite-amplitude interface.

```text
A5_VERDICT = KILLED
ROOT_PLUS_E_POST_FINITE_FACTOR = Z_N
ROOT_MINUS_E_POST_FINITE_FACTOR = 1

BOTH_ROOT_MEMBERS_REPRODUCE_Q236_FINITE_AMPLITUDE = false | TYPE-R |
  test: exact one-cell branch overlap

ROOT_MINUS_PASSES_CHARGE_FLUX_ACCESS_ON_PREPARED_PATH = false | TYPE-R |
  test: W(z)|p>=|r> contains no z

ROOT_BINARY_IS_A_GENUINE_TWO_MEMBER_PRINCIPAL_CHOICE = false | TYPE-R |
  test: one member fails an inherited finite interface
```

Repair alternatives are not executed here. The record can either derive the
plus root from the inherited finite-interface requirement, or separately
author and gate a different endpoint-law package for the exchanged root. The
current same-E_post binary cannot be ratified as a two-member family.

## 7. A6 -- surviving-limb regression

### 7.1 Incidence primitive versus filtration selection

V002 adds no global filtration, refinement map, or J_ref field. G3 remains the
same local one-cell signed-incidence object Q-260 A1 cleared.

```text
INCIDENCE_PRIMITIVE_IS_A_RELABELLED_1088_SELECTION = false | TYPE-R |
  test: unchanged local domain/codomain
```

### 7.2 d_law fidelity

The operator formula is unchanged:

```text
U_N=P_0 tensor I + P_ch tensor tensor_j(D_n[a_j]S_inc).
```

It remains the DoR-009 E_post law. The orientation failure in Section 6 is a
state/law-package mismatch, not drift in `d_law` itself.

```text
D_LAW_EQUALS_DOR009 = true
```

### 7.3 Finite authority

G3 and the law remain finite-visible. The strict affine witness has a complete
finite algebraic `Cert_IF`. The general G1-v2 certificate is uninstantiated as
shown in Section 5.

```text
A6_VERDICT = WOUNDED
LOCAL_INCIDENCE_LIMB = SURVIVED
D_LAW_LIMB = SURVIVED
FINITE_AUTHORITY_LIMB = WOUNDED_BY_GENERAL_CERT_IF_SCHEMA
```

## 8. A7 -- nonemptiness and family relationship

### 8.1 Independent nonemptiness verification

The strict affine witness class is genuinely nonempty. For every admitted
`sigma` and symbolic nontrivial mixing `lambda`, the map

```text
P_(sigma,lambda)(tau)
  =lambda tau +(1-lambda)Tr(tau)sigma
```

is normal, CPTP, charge covariant, commutes with superselection, mixes to the
unique state `sigma`, and acts as `lambda` times the identity on
`Delta_0^ss`. Its certificate is exact.

```text
A7_NONEMPTY = SURVIVED
```

This positive result is also the A1 killing construction.

### 8.2 Relationship to the Q-263 benchmark

On Q-263's finite-carrier scope, let

```text
F_V002 = {G1 channels with m_in>0 and Cert_IF},
F_BI   = {G1 channels that are unital and input-faithful}.
```

Finite dimensionality turns injectivity on the traceless space into a
positive lower modulus, so every certified `F_BI` member is in `F_V002`.
But `P_(sigma,lambda)` with `sigma!=I_src/Tr(I_src)` is in `F_V002` and not in
`F_BI`. Hence

```text
F_BI is a proper subset of F_V002
```

on the benchmark's finite scope.

```text
V002_FAMILY_EQUALS_BENCHMARK_FAMILY = false | TYPE-R |
  test: nonunital strict affine witness
V002_FAMILY_IS_STRICTLY_BROADER_THAN_BENCHMARK = true | premises: finite Q-263 scope
```

On V002's asserted infinite-carrier reading, the exact normalized-identity
benchmark needs the carrier typing identified in Section 3.3 before the
subset statement transports.

## 9. Combined verdict

| Attack | Verdict | Decisive content |
|---|---|---|
| A1 anchor | KILLED | strict affine pair has identical difference certificate and arbitrary invariant states |
| A2 forced charge form | NOT TRIGGERED | V002 does not collapse the state orbit |
| A3 conditionals | SURVIVED WITH BOUNDARY | B5/B6 are P2-P6; B9 needs P9/P10/P11 consumer |
| A4 finite certificate | WOUNDED | exact for affine witness; schema-only for general G1-v2 |
| A5 orientation binary | KILLED | exchanged root loses E_post holonomy and finite amplitude |
| A6 surviving limbs | WOUNDED | incidence and law survive; general finite certificate does not |
| A7 nonemptiness | SURVIVED | genuine, but the witness is the A1 counterexample |

```text
ATTACKS_KILLED = 2
ATTACKS_WOUNDED = 2
ATTACKS_SURVIVED = 2
ATTACKS_NOT_TRIGGERED = 1

OVERALL = DEAD
```

V002 cannot advance to DoR-013. A successor requires at least:

1. an orbit-collapsing structural anchor in addition to input-faithfulness;
2. an authoritative carrier typing so the anchor's passing family is proved
   nonempty on the actual source carrier;
3. removal or re-authoring of the broken minus-root/E_post member;
4. an instantiated finite certificate format for every admitted non-affine
   channel, if the family remains broader than the exact affine class;
5. a fresh B14/Q-242 rerun against the anchored family;
6. corrected battery/dependency text preserving B9's consumer requirement.

On the finite Q-263 carrier, the exact anchor repair is

```text
P(I_src)=I_src
```

added to V002's input-faithfulness. On an infinite carrier, that formula may
not produce a normal trace-class invariant state; an alternative normal
orbit-collapsing anchor must be stated and proved nonempty. No anchor is chosen
or authored here.

```text
GEN_OMEGA_V002_STATUS = DEAD
DOR_013_MAY_RATIFY_V002 = false | TYPE-R |
  test: A1 and A5

GEN_OMEGA_CONCEPT_REFUTED_IN_ALL_FORMS = false | TYPE-S |
  scope: only V002/hash 479cfb89... was reviewed

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
