# STAGE 8 / TASK 5 / EQ6 — THE TWO LEMMAS: SEED THEOREM AND LOC-NATURALITY

Lane: Codex Lane 3  
Artifact: `STAGE8_TASK5_EQ6_TWO_LEMMAS_LANE3_V001.md`  
Register head checked: `Q-492`  
Mode: symbolic only

## 0. Preflight and mandatory stopping rule

The three STEP-0 locations were accessible. The supervision register has
`Q-492` as its last question row; its SHA-256 at read time was
`e48e62cb789cb68092fdd081cf8ea25f86f8c062ef91df429c73157bae85d76d`.
The requested output and its sidecar were absent from both the cleanroom and
the archive workspace before creation.

The review of record was read first through its sealed archive copy. Its
sidecar names the same digest as the recomputed review-artifact digest:

```text
STAGE8_TASK5_EQ6_J7_REVIEW_AND_ADJUDICATION_DARIO_V001.md
SHA-256 = f76139e5424c34d1198faf15ce2d0fa06d2e984f53c7da6854b8dad79384f80b
```

In particular, F1(a), F1(b), and O1 say respectively that no actual stage has
an established nonzero `m_T`, that the displayed J2 chain still lacks its
`Q`-descent and `Loc`-naturality premises, and that a cyclic harmonic sector
does not by itself force a nonzero projection.

The inputs consumed below were hash-verified against the archive workspace:

| Sealed input | SHA-256 | Content consumed |
|---|---|---|
| `STAGE8_TASK5_EQ6_J7_REVIEW_AND_ADJUDICATION_DARIO_V001.md` | `f76139e5424c34d1198faf15ce2d0fa06d2e984f53c7da6854b8dad79384f80b` | F1(a), F1(b), O1, and the no-seed finding |
| `STAGE8_TASK5_EQ6_J7_FACE_AND_J2_DISPLAY_LANE3_V001.md` | `9c74ed3dbe748450e525102128b0367ce21c0e5029929eab33a111ca9802dc3c` | `(T2)`--`(T5)` and the stated `(F1)`/`(F3)` premises |
| `STAGE8_TASK5_EQ6_PROJECTOR_CERT_V003_LANE1_V001.md` | `0bef9a003abb586666535689e98d7af29e7fc75b81e06fe439397ce2b8ef9100` | proved `d`, `delta`, Laplacian, and harmonic-projector intertwiners |
| `STAGE8_TASK5_EQ6_MAXWELL_HODGE_PROJECTOR_CERT_LANE2_V001.md` | `f074ca24e8b96c576f5c64b856377f39ed8d4fc729c02cbf591326322558f816` | fixed-stage Hodge construction and reciprocal-loop edge-orbit witness |
| `STAGE8_TASK5_R4_KERNEL_REALIZATION_AND_SYMBOL_CALCULUS_LANE2_V001.md` | `ccb94dfa8927cf8d2ec76cf85ff2f402d02d5aa5673b9d39c214a6de4c92309c` | actual conserved currents, faithful finite kernels, and Ward law |
| `STAGE8_TASK5_EQ6_DIAMOND_CENSUS_LANE3_V001.md` | `676863b5ac68108a87dc6b5cf070908bdb15ad45d44a0f80edd473fe2c6ee245` | rank-one nonvanishing criterion and exact seed debt |
| `STAGE8_TASK5_EQ6_PHYSICAL_J2_LANE2_V001.md` | `3fd4b924ec1a70f3e730bcf99f406d697c53937b26467d2ae6d5aa8c1bb6822c` | nonzero reciprocal Q-408 kernel and the physical-coefficient boundary |
| `STAGE8_TASK4B_LOCAL_MAXWELL_SYMBOL_AND_PLOC_RK_LANE2_V001.md` | `70dde1c0cb776abec4a61cac118d4edf1f4c75a1185a2e984dc341961d4b643c` | exact scope of `p_loc(L_T)=1` |

The relay imposes this priority rule:

```text
if L1 cannot establish m_T != 0 at an actual named stage,
report the exact failed quantity and STOP on L1.             (STOP)
```

The calculation below reaches that stop. Consequently L2 is not attempted;
no result about `Loc`-naturality is manufactured from the narrower projector
intertwiners.

## 1. L1 — the actual reciprocal-loop seed calculation

### 1.1 Named actual stage and fixed data

Let `N_RL` be the actual two-corridor reciprocal-loop finite stage from the
Q-408 stock, with oriented corridors `a,b`. Its degree carrying the finite
connection/current symbol has one-dimensional harmonic sector

```text
H_N_RL = span{c_RL},
c_RL != 0,
supp(c_RL) = {a,b}.                               (S1)
```

The inner product is the already-ratified positive carrier metric. Hence

```text
<c_RL,c_RL>_N_RL > 0.                            (S2)
```

No new metric, orientation, edge, current, or realization member is chosen
in this artifact. The projector formula and seed equivalence `(S5)`--`(S9)`
hold for any nonzero generator of the one-dimensional harmonic line. The
edge-orbit identity `(W3)`--`(W4)` instead uses the sealed
incidence-normalized oriented representative and its transported edge orbit.

### 1.2 The particular symbol whose projection is at issue

Define exactly the symbol used by the coefficient-face construction:

```text
s_T,RL
 := Loc_N_RL Kernbar_N_RL Q_N_RL(L_T,N_RL),       (S3)

m_T,N_RL
 := P_H,N_RL s_T,RL.                              (S4)
```

This is the particular `L_T`-generated symbol. It is not an arbitrary
edge-local input, an arbitrary Q-408 profile, or the cycle current itself.

Because `(S1)` is rank one, the orthogonal projector is completely fixed:

```text
P_H,N_RL(s)
 = <s,c_RL>_N_RL / <c_RL,c_RL>_N_RL c_RL.        (S5)
```

Substituting `(S3)` into `(S4)` and then using `(S5)` gives the requested
symbolic computation in full:

```text
m_T,N_RL
 = P_H,N_RL Loc_N_RL Kernbar_N_RL
     Q_N_RL(L_T,N_RL)

 = <Loc_N_RL Kernbar_N_RL Q_N_RL(L_T,N_RL),
      c_RL>_N_RL
     / <c_RL,c_RL>_N_RL c_RL.                    (S6)
```

Name the numerator

```text
q_T,RL
 := <Loc_N_RL Kernbar_N_RL Q_N_RL(L_T,N_RL),
       c_RL>_N_RL.                                (S7)
```

Equations `(S1)`, `(S2)`, and `(S6)` display both implications:

```text
q_T,RL != 0
 => q_T,RL/<c_RL,c_RL>_N_RL != 0
 => m_T,N_RL != 0,                               (S8a)

m_T,N_RL != 0
 => q_T,RL/<c_RL,c_RL>_N_RL != 0
 => q_T,RL != 0.                                 (S8b)
```

Therefore the seed theorem at this actual stage is exactly, neither more nor
less,

```text
m_T,N_RL != 0  iff  q_T,RL != 0.                 (S9)
```

### 1.3 What the Ward/flux stock proves

The sealed Q-408 and Hodge stock proves all of the following structural
facts.

First, `c_RL` is a nonzero incidence cycle. Its actual current

```text
<J_c_RL,A>
 := sum_e (c_RL)_e integral_(gamma_e) A           (W1)
```

is faithful and conserved:

```text
<partial J_c_RL,varphi>
 = <J_c_RL,d varphi>
 = <B_N_RL^T c_RL,varphi>
 = 0.                                             (W2)
```

The finite analysis map onto the cycle dual supplies test fields detecting a
nonzero cycle, and Q-408 faithfulness supplies nonzero bilocal kernels for
nonzero profile operators. The two Ward equations hold for every such
profile kernel.

Second, if `epsilon_a,epsilon_b` are the two actual edge-local finite inputs,
the sealed orientation signs and metric positivity give

```text
0 < <c_RL,c_RL>_N_RL
  = <epsilon_a,c_RL>_N_RL
    - <epsilon_b,c_RL>_N_RL.                     (W3)
```

Thus, without selecting an edge, the full edge orbit contains some
`epsilon_e` satisfying

```text
<epsilon_e,c_RL>_N_RL != 0,

P_H,N_RL epsilon_e
 = <epsilon_e,c_RL>_N_RL
     / <c_RL,c_RL>_N_RL c_RL
 != 0.                                            (W4)
```

These are genuine nonvanishing results. They prove that the harmonic sector,
the conserved current, a detecting field test, a nonzero faithful kernel,
and at least one nonzero harmonic projection all occur on the actual
reciprocal-loop stage.

### 1.4 Why those results do not prove the seed

No sealed source supplies any of the equalities or implications needed to
replace `(W4)` by `(S7)`:

```text
s_T,RL = epsilon_e,                               (M1)

q_T,RL = <epsilon_e,c_RL>_N_RL,                  (M2)

q_T,RL = <J_c_RL,A_T> with a sealed A_T
                         and a proved nonzero flux, (M3)

s_T,RL != 0 => P_H,N_RL s_T,RL != 0.             (M4)
```

`(M4)` is false as a general linear-algebra implication: a nonzero vector in
`H_N_RL^perp` has zero harmonic projection. The sealed stock does not exclude
that case for this particular `s_T,RL`. This is an entailment control, not a
claim that the actual `s_T,RL` has been proved orthogonal.

Ward conservation cannot fill the gap. It is a homogeneous condition obeyed
by the whole realized profile family, so it distinguishes neither the local
Maxwell line nor the harmonic period of the particular `L_T` image. Likewise,
faithfulness of `Kernbar Q` before `Loc` does not make `P_H Loc` injective.

The exact missing statement is therefore

```text
<Loc_N_RL Kernbar_N_RL Q_N_RL(L_T,N_RL),
  c_RL>_N_RL != 0.                               (M5)
```

Equivalently, a future proof could supply a sealed Ward/flux-to-`L_T` anchor
identifying `(S7)` with a named nonzero period. No such anchor is present.

### 1.5 Why normalization does not repair `(M5)`

The sealed equation

```text
p_loc,N_RL(L_T,N_RL) = 1                         (N1)
```

is the normalization of a functional on its declared local-symbol domain.
It proves a value on `L_T`; it does not identify
`Loc Kernbar Q(L_T)` with `c_RL`, with `epsilon_e`, or with any vector having
a nonzero harmonic period.

Nor may one use

```text
lambda_N_RL(m_T,N_RL)=1                          (N2)
```

to infer the seed. The definition

```text
lambda_N_RL(h)
 = <m_T,N_RL,h>_N_RL
     / <m_T,N_RL,m_T,N_RL>_N_RL                 (N3)
```

is formed only after `m_T,N_RL != 0` has already been established. Using
`(N2)` to prove that premise would be circular. Pulling the algebraic reader,
`chi^Mx`, or `T^Mx` backward to choose the nonzero branch would be the same
F_PLDEC circularity class.

The physical-J2 reciprocal witness sharpens, but does not close, this
boundary: a nonzero reciprocal profile has a nonzero faithful Q-408 kernel,
yet the sealed stock supplies no theorem that its later localized Hodge
projection is the `L_T` seed in `(S6)`.

## 2. L1 verdict and mandatory stop

[PROVABLE] The actual reciprocal-loop calculation reduces nonvanishing to
`q_T,RL != 0` by `(S6)`--`(S9)`.

[PROVABLE] The denominator is strictly positive, while the sealed nonzero
Ward/current/edge witnesses do not identify their input with `s_T,RL`.

[PART-PROVABLE] The requested seed is therefore **not established**. This is
a proof failure, not a proof that `q_T,RL=0` and not a refutation of a future
seed theorem.

The exact failed quantity is `(M5)`. Under `(STOP)`, this first-order failure
terminates the mathematical relay before L2.

```text
L2_LOC_NATURALITY_PROOF_OR_REFUTATION = NOT_RUN
F1_COMPANION_QUOTIENT_DESCENT         = NOT_RUN
REASON                                = mandatory L1 stop
```

In particular, this artifact neither promotes `d`/`delta` naturality to
`Loc`-naturality nor repeats the earlier unsupplied `(F1)`/`(F3)` assertions.

## 3. Consequence and custody board at the stop

| Item | Status after L1 | Exact consequence |
|---|---|---|
| `A_RP^+` inhabitance | **EMPTY_OF_RECORD** | No actual stage is recorded with proved `m_T != 0`. This means “no established inhabitant,” not “proved set-theoretically empty.” |
| J2 display premise | **UNCHANGED / UNADJUDICATED HERE** | L2 was not run; the review's missing `Loc`-naturality and quotient-descent premises remain debts. |
| J7 amendment inhabitance clause | **CANNOT CITE A SEED** | It may cite `(S9)` as the exact address test, but not a nonzero reciprocal-loop inhabitant. |
| FC11 | **NOT ATTEMPTED** | Its treatment of demanded-unformable positions remains the stated axiom-text question. |
| Membership route | **STOPPED AT FIRST FINAL GATE** | The seed theorem outranks the downstream gates. |

No law, axiom text, support amendment, or family member is adopted here.

## 4. L1 battery

### 4.1 F_PLDEC circularity rerun

The dependency order actually used is

```text
ratified metric + actual differential
 -> P_H
 -> sealed finite Loc Kernbar Q applied to declared L_T
 -> s_T,RL
 -> q_T,RL and m_T,N_RL.                          (B1)
```

No reader, reader value, `lambda`, `pi_Mx`, `chi^Mx`, or `T^Mx` occurs in
`(S1)`--`(S9)`. The reader-based normalization routes were considered only as
hostile attacks and rejected in Section 1.5. Thus the seed calculation itself
does not touch the reader.

```text
F_PLDEC_SEED = PASS
READER_REFERENCED_IN_SEED_COMPUTATION = no
```

### 4.2 Anti-tuning ledger

| Forbidden adjustment | Check | Result |
|---|---|---|
| choose an edge with the desired sign | `(W3)` is retained as an orbit-existence statement; no `epsilon_e` is substituted for `s_T,RL` | clean |
| rotate or rescale the metric to force a period | the ratified metric is held fixed | clean |
| choose a cycle basis | only the invariant one-dimensional projector formula is used; `(S9)` is unchanged under nonzero rescaling or sign of `c_RL` | clean |
| redefine `Loc`, `Q`, `Kernbar`, or `L_T` | every map and input is consumed with its sealed definition and typing | clean |
| infer a coefficient from a reader output | normalization/reader attacks are rejected as circular | clean |
| inspect magnitudes or measured constants | only the structural predicates zero/nonzero are used | clean |
| bind a member or execute downstream machinery | no member, fixed point, end test, or completed-family execution occurs | clean |

### 4.3 Self verb audit

| Verb/status used | Display supporting it | Audit |
|---|---|---|
| `computed symbolically` | `(S3)`--`(S7)` | full rank-one projection written without numeric evaluation |
| `iff` | `(S8a)` and `(S8b)` with positive denominator `(S2)` | both directions displayed |
| `nonzero Ward/current/edge witnesses` | `(W1)`--`(W4)` | claims kept on their exact inputs |
| `FAILED` for the seed theorem | exact unproved numerator `(M5)` after the equivalence `(S9)` | means “not established,” expressly not “refuted” |
| `EMPTY_OF_RECORD` for `A_RP^+` | no seed obtained and review's corpus finding | expressly not a proof of mathematical emptiness |
| `NOT_RUN` for L2 and FC11 | mandatory stop `(STOP)` | no downstream status invented |
| `CLEAN` for the battery | `(B1)` and the anti-tuning ledger | every claimed exclusion displayed |

```text
MACHINERY_APPEAL = false
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member_bound = false
fixed_point_executed = false
end_test_run = false
numeric_evaluation = false
comparison_to_measured_constants = false
```

No register, plan, tracker, git, commit, push, member-binding, fixed-point,
end-test, or numerical-evaluation action was performed.

SEED_THEOREM = FAILED (+quantity `q_T,RL := <Loc_N_RL Kernbar_N_RL Q_N_RL(L_T,N_RL),c_RL>_N_RL` is not provably nonzero)
LOC_NATURALITY = NOT_RUN (+mandatory L1 stop)
A_RP_PLUS = EMPTY_OF_RECORD
VERB_AUDIT_SELF = CLEAN
