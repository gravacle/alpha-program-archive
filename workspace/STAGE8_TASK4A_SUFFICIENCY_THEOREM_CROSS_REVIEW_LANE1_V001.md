# STAGE8 TASK 4A: SUFFICIENCY THEOREM CROSS-REVIEW (LANE 1 V001)

**ADVERSARIAL CROSS-REVIEW OF THE Q-348 PREFIX-TRACE THEOREM**

```text
LEAD_RESULT = CONFIRMED

SUFFICIENCY_THEOREM = CONFIRMED

PREFIX_FAMILY_AT_RANK2 = CARRIES_CYCLE_CONTENT |
  proof: on the S8-A stage the prefix tuple reconstructs every cell character
         and hence all c_1, c_2, c_3 holonomies;
  boundary: the family-natural cell-to-edge/action comparison map remains
            NOT_BUILT / TYPE-U

TERMINAL_TRACE_AT_RANK2 = STILL_OBSTRUCTED | TYPE-R |
  proof: Q-347's one-scalar automorphism obstruction remains exact

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 0. Preflight and custody

The artifact under review was hashed before it was read.

| Authority | Expected and verified SHA-256 | Result |
|---|---|---|
| Q-348 sufficiency arm | `d9a507fc8b5645981ed1519a04e180620ee7c22f65d5c9425437a701185f9001` | PASS; sidecar OK |
| DoR-016 V004 | `69f4d93b9f84075a3112fb011b9838f380fb8c0341610572170cf7a13d5aed08` | PASS; sidecar OK |
| Q-347 extension arm | `04002fb49fcf91a544544a798519cfe56017f42659a1eb6d6947f9defbc76a5a` | PASS; sidecar OK |
| Door-7 cross-review | `d738661e1e8038bd0a4a7f7121e244b15dffab76d5fad7ca2584017ebff49b14` | PASS; sidecar OK |
| DoR-009 decision | `11632fa30dfe9225c228f07a3be4717c73bdfc9e38b0c76c46d905d3fe193bc5` | PASS; sidecar OK |
| DoR-009 V002 law | `db1808e4da38cbfed8b12017885aff1bf63b0378e9971c37294e21fa08766fee` | PASS; sidecar OK |
| locked process | `f3bd9a62e172ba58667840e7717eb7ab8cd74be9fbe8d190802794ee5c3377ba` | PASS; sidecar OK |

The live questions-settled register is at the required Q-348 head. Its
send-time SHA-256 at preflight was
`e26e16c916488681d8408e7a776ba3c1f69741daacd02623f51c6ff2d1343a41`.
The reviewer-maintained register sidecar did not match those live bytes.
That custody discrepancy is reported but is not used as theorem evidence;
this lane did not edit the register or its sidecar.

```text
DOES_THE_OBJECT_EXIST = yes | Q-348 theorem artifact verified
IS_THE_VERSION_CURRENT = yes | live register head Q-348
ARE_THE_INPUTS_PRESENT = yes | finite relative-CTP data and both parallel arms
NAMED_PREFLIGHT = PASS
REGISTER_SIDECAR_CURRENT = false | reviewer-custody discrepancy reported
```

## 1. Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| W1 - triangular isomorphism | **PASS** | consecutive prefix ratios recover every character; `n=+/-1` then recovers every relative endomorphism |
| W2 - terminal kernel | **PASS** | the terminal multiplication kernel is exactly `U(1)^(N-1)` and the N=2 X7 pair is a member |
| W3 - domain honesty | **PASS** | the theorem stops at relative `R_CTP`; raw pairs, untraced operators, and the physical action remain explicitly `TYPE-U` |
| W4 - prefix availability | **PASS** | DoR-016 ratifies each finite `Z_N^CTP`; all prefixes are its finite restrictions, and V004 separately calls each tier factor an already traced scalar |
| W5 - seam with Q-347 | **PASS** | prefixes remove the one-scalar information obstruction at fixed rank two; the geometric comparison map remains unbuilt |
| W6 - regressions/selections | **PASS** | reality, sequential restriction, batching, and identity extension commute with the inverse; no member or value is selected |
| W7 - fresh attack | **PASS** | edge-order permutation acts by a derived automorphism of prefix coordinates; the theorem is covariant rather than falsely invariant |

No item kills the scoped Q-348 theorem.

## 2. W1 - triangular isomorphism

### 2.1 Exact map and inverse

For a fixed receiver and finite ordered stage, write

```text
R=(R_1,...,R_N) in U(1)^N,
r_j=chi_n(R_j)=R_j^n,
Z_0=1,
Z_m=product_(j=1)^m r_j.
```

Define

```text
Pi_N(R)=(Z_0,Z_1,...,Z_N).
```

Then, identically in `U(1)`,

```text
Z_(m-1)^(-1) Z_m
 =(product_(j=1)^(m-1) r_j)^(-1)
   (product_(j=1)^m r_j)
 =r_m.                                             (W1-1)
```

Thus the inverse on characters is

```text
r_m=Z_(m-1)^(-1)Z_m.                              (W1-2)
```

At `n=+1`, `R_m=r_m`. At `n=-1`, `R_m=r_m^(-1)`.
Both are global group operations; no logarithm or branch choice occurs.

The codomain may be stated more strongly than the reviewed artifact does:
every tuple `(1,Z_1,...,Z_N)` occurs, because `(W1-2)` constructs its unique
preimage. Hence

```text
Pi_N:U(1)^N -> {1} x U(1)^N
```

is a group isomorphism, not merely an injection onto an unknown subset.

### 2.2 Trivial-kernel induction

Suppose `Pi_N(R')=Pi_N(R)` and write

```text
R'_j=R_j W_j,
w_j=chi_n(W_j).
```

Prefix equality gives

```text
product_(j=1)^m w_j=1 for all m.
```

At `m=1`, `w_1=1`. If `w_1=...=w_(m-1)=1`, the `m` equation gives
`w_m=1`. Induction yields `w_j=1` for all `j`. Faithfulness then gives
`W_j=1` for all `j`.

```text
ker(Pi_N)={identity}.                              (W1-3)
```

### 2.3 Faithfulness is load-bearing

DoR-009 V002 states `n in {+1,-1}` at lines 288-289, records C8 as
"faithful `n=+1,-1` and reality" at lines 356-372, and distinguishes these
as character orientations at lines 503-510. DoR-009 ratifies that V002 law.

If instead `chi_k(z)=z^k` with `|k|>1`, then every

```text
(W_1,...,W_N) in mu_|k|^N
```

is killed by every prefix character. The character-level ratios still recover
`R_m^k`, but each `R_m` has `|k|` preimages. For `k=0`, every input is killed.
Therefore the endomorphism reconstruction, rather than only character
reconstruction, fails exactly when faithfulness fails.

```text
W1 = PASS
FAITHFUL_CHARACTER_PREMISE_LOAD_BEARING = true | TYPE-P
UNFAITHFUL_ALL_PREFIX_KERNEL = mu_|k|^N | |k|>1
```

## 3. W2 - terminal kernel and X7

The terminal map is

```text
mu_N:U(1)^N -> U(1),
mu_N(r_1,...,r_N)=product_j r_j.
```

Its kernel is

```text
K_term,N={w:product_j w_j=1}.
```

The explicit isomorphism

```text
U(1)^(N-1) -> K_term,N,
(w_1,...,w_(N-1))
  |->(w_1,...,w_(N-1),(product_(j=1)^(N-1)w_j)^(-1))
```

has inverse given by the first `N-1` coordinates. Hence

```text
K_term,N isomorphic to U(1)^(N-1).                (W2-1)
```

At `N=2`, for generic `u,v,w`,

```text
r =(u,   v),
r'=(u w, v w^(-1)),

mu_2(r')=(u w)(v w^(-1))=uv=mu_2(r).             (W2-2)
```

But the first prefixes differ whenever `w!=1`:

```text
Z_1(r')=uw!=u=Z_1(r).
```

Thus the Door-7 X7 attack remains a valid refutation of terminal-trace or
terminal-`NetAcc` sufficiency, and Q-348 correctly absorbs rather than erases
it. The attack does not meet the hypothesis of equal complete prefix families.

```text
W2 = PASS
TERMINAL_TRACE_SUFFICIENCY = false | TYPE-R
COMPLETE_PREFIX_TRACE_KERNEL = {identity} | TYPE-P
```

## 4. W3 - domain honesty

### 4.1 Raw-pair fiber

DoR-016 V004 defines

```text
R_CTP=T_-^dagger T_+
```

at lines 309-328 and retains its conjugation covariance. The receiver then
uses the faithful character of this relative endomorphism. Therefore the raw
map has the fiber

```text
(T_+,T_-) ~ (T_+',T_-')
  iff T_-'^dagger T_+'=T_-^dagger T_+.
```

A common endpoint transformation is contained in this fiber after quotienting
by the ratified covariance. Prefix traces cannot distinguish two raw pairs in
the same fiber because every cellwise `R_CTP` already agrees.

### 4.2 Scope comparison

The reviewed artifact states at lines 27-29 and 71-74:

```text
RAW_DOUBLED_PAIR_OR_FULL_UNTRACED_OPERATOR_SUFFICIENCY = NO_VERDICT / TYPE-U
PHYSICAL_TRANSVERSE_ACTION_BUILT = false / TYPE-U
```

It repeats the raw/untraced ceiling at lines 684-710. It does not use the
prefix isomorphism to reconstruct `T_+`, `T_-`, `U_N`, an independent
bilocal source, or any 2PI block.

The line `TRANSVERSE_ACTION_IS_Z_LOCAL` at lines 82-86 is lawful only under
its printed scope: a future consumer's dependence on the DoR-016 relative
input can be re-coordinatized by the complete prefix family. It is not a
claim that the whole physical action has no independent transverse data.
The artifact expressly preserves that `NO_VERDICT`.

```text
W3 = PASS
RAW_PAIR_RECONSTRUCTED = false | TYPE-U
UNTRACED_OPERATOR_RECONSTRUCTED = false | TYPE-U
PHYSICAL_ACTION_RECONSTRUCTED = false | TYPE-U
```

## 5. W4 - availability of every prefix trace

### 5.1 Ratified finite trace

DoR-016 V004 lines 348-370 define, for every finite receiver stage,

```text
Z_N^CTP
 =product_(j=1)^N chi_n(R_(CTP,j))
 =product_(j=1)^N conjugate(z_(-,j)^n)z_(+,j)^n,
```

and type it as the ratified single-receiver finite ready-record trace. The
DoR-016 decision lines 13-16 adopts exactly this consumption and the resulting
per-system tower.

For every `m<=N`, restrict the same finite law to its first `m` cells. The
ratified finite output is then

```text
Z_m^CTP=product_(j=1)^m chi_n(R_(CTP,j)).          (W4-1)
```

This is not a newly authored observable. It is the already-ratified finite
trace evaluated on a sealed finite restriction. DoR-009 C7 supplies the
sequential zero-extension law; its V002 statement appears at lines 330-335.

### 5.2 The tower exposes factors, not only the final product

V004 lines 386-399 explicitly say:

```text
Let Z_(i,t)^CTP be the already traced scalar ... at tier t.
```

and only then form

```text
product_(t=1)^k Z_(i,t)^CTP.
```

The operation ledger at lines 614-622 likewise separates the finite C5 trace
from projector multiplication. Accordingly, each `Z_(i,t)^CTP` is a ratified
finite mathematical output. The accumulated product is downstream of those
factors, not their only licensed existence.

The theorem does not invert the conditioned amplitude
`A_m=(1-p)+pZ_m`; it consumes `Z_m` directly. No division by symbolic `p` is
required.

```text
W4 = PASS
ALL_PREFIX_TRACES_AVAILABLE = true | TYPE-P |
  route: finite restriction of the ratified DoR-009/DoR-016 trace
NEW_PREFIX_OBSERVABLE_AUTHORED = false | TYPE-S
```

## 6. W5 - seam with the Q-347 extension theorem

### 6.1 What Q-347 actually obstructs

Q-347 classifies lifts that depend only on one terminal scalar:

```text
s_G:U(1)->Q_G,
Hol_G(s_G(z))(c)=z^lambda(c).
```

At cycle rank at least two, such an image is at most one-dimensional. On the
S8-A graph, the parallel-edge exchange fixes the terminal product and forces
the record-visible `c_3` into the annihilator. Those statements remain exact.

Q-348 changes the source object from one scalar to the complete tuple

```text
(Z_1,...,Z_N) isomorphic to (r_1,...,r_N).
```

The one-dimensional classification no longer applies.

### 6.2 Fixed-stage rank-two computation

Use Q-347's S8-A stage, with oriented edge order `(a,b,d)` and

```text
c_1=(1,1,0),
c_2=(0,1,1),
c_3=(1,0,-1)=c_1-c_2.
```

Write the faithful relative characters as `(r_a,r_b,r_d)`. The prefix data
are

```text
Z_1=r_a,
Z_2=r_a r_b,
Z_3=r_a r_b r_d.                                  (W5-1)
```

Every physical cycle holonomy is recovered:

```text
H_(c_1)=r_a r_b              =Z_2,
H_(c_2)=r_b r_d              =Z_1^(-1) Z_3,
H_(c_3)=r_a r_d^(-1)         =Z_1 Z_2 Z_3^(-1).   (W5-2)
```

The third identity follows from
`r_d=Z_2^(-1)Z_3`. Thus the prefix family carries both independent rank-two
cycle coordinates and the S8-A triple. No cycle basis is selected by the
theorem; `(W5-2)` merely tests the already displayed Q-347 basis.

### 6.3 Automorphism computation

Let `sigma` exchange the parallel edges `a` and `d`. On cell characters,

```text
(r_a,r_b,r_d) |-> (r_d,r_b,r_a).
```

On prefixes this gives

```text
Z_1' =Z_2^(-1)Z_3,
Z_2' =Z_1^(-1)Z_3,
Z_3' =Z_3.                                         (W5-3)
```

The prefix tuple is not fixed generically. Substitution in `(W5-2)` gives

```text
H_(c_1)'=H_(c_2),
H_(c_2)'=H_(c_1),
H_(c_3)'=H_(c_3)^(-1),                            (W5-4)
```

exactly matching

```text
sigma(c_1)=c_2,
sigma(c_2)=c_1,
sigma(c_3)=-c_3.
```

Therefore Q-347's automorphism obstruction does not re-bind to the prefix
family: its crucial premise was that the one consumed scalar was fixed by
`sigma`. Here the source transforms nontrivially and covariantly.

### 6.4 What remains unbuilt

Equations `(W5-1)` through `(W5-4)` prove information sufficiency on a fixed
realized stage whose ordered cells are already identified with `(a,b,d)`.
Neither Q-348 nor this review constructs the family-natural assignment from
every ordered relative-history cell family to every incidence realization.
That comparison functor, its restriction squares, and its action/2PI
placement remain `TYPE-U`.

This is a strict split:

```text
PREFIX_INFORMATION_AT_RANK2 = SUFFICIENT | TYPE-P
SINGLE_TERMINAL_SCALAR_AT_RANK2 = INSUFFICIENT | TYPE-R
FULL_FAMILY_CELL_TO_EDGE_COMPARISON = NOT_BUILT / TYPE-U
PHYSICAL_ACTION_COMPARISON_SQUARE = NOT_BUILT / TYPE-U
```

```text
W5 = PASS
PREFIX_FAMILY_AT_RANK2 = CARRIES_CYCLE_CONTENT
```

## 7. W6 - regressions and selection scan

### 7.1 Reality

Under the ratified involution,

```text
R_j -> R_j^dagger,
Z_m -> conjugate(Z_m).
```

The inverse satisfies

```text
conjugate(Z_(m-1))^(-1)conjugate(Z_m)
 =conjugate(Z_(m-1)^(-1)Z_m).
```

Thus `Pi_N^(-1)` is reality-covariant.

### 7.2 Sequential restriction and identity extension

Restricting to the first `M<N` cells deletes only the later prefix entries;
all earlier inverse ratios are unchanged. Appending an identity cell gives

```text
Z_(N+1)=Z_N,
r_(N+1)=Z_N^(-1)Z_(N+1)=1.
```

### 7.3 Batching

Every consecutive batch is recovered without a branch:

```text
Z_[a,b]=Z_(a-1)^(-1)Z_b.                          (W6-1)
```

A fine prefix family therefore maps canonically to every coarse batch. The
reverse map from one coarse terminal product to its interior factors does not
exist; `(W2-2)` is the counterexample. This is not hidden by the reviewed
artifact: its theorem expressly consumes the complete family and rejects
coarse-terminal sufficiency.

Consequently a future comparison square may use `(W6-1)` from fine to coarse,
but it may not claim that a coarse terminal value reconstructs discarded
interior prefixes.

### 7.4 Selection and fence scan

```text
character orientation selected = false
rank or rank ratio selected = false
p evaluated = false
endpoint frame selected = false
orientation member selected = false
cycle basis selected = false
filtration member selected = false
joint contraction formed = false
physical response evaluated = false
alpha, K_*, or any root evaluated = false
measured constant consulted = false
```

Both `n=+1` and `n=-1` obey the same theorem. Symbolic `p` never enters the
inverse. The ordered prefix system is the ratified sequential carrier, not a
chosen geometric realization member.

```text
W6 = PASS
```

## 8. W7 - fresh permutation and global-branch attack

### 8.1 Attack

The prefix coordinates depend on order. A hidden ordering choice would make
the sufficiency theorem unusable under family relabelings. For any permutation
`pi` of cell characters, test whether the induced action on prefix data exists
without choosing logarithms or a preferred representative.

### 8.2 Result

Because `Pi_N` is a group isomorphism, define

```text
J_pi:=Pi_N compose pi compose Pi_N^(-1).           (W7-1)
```

This is a globally defined group automorphism of the prefix carrier. It is
forced, not selected. For the S8-A edge swap, `(W7-1)` is exactly `(W5-3)`.
The cycle characters then transform as `(W5-4)`.

No phase logarithm appears in `(W7-1)`. Hence there is no hidden branch at
the points where a local phase chart crosses its cut. The local triangular
Jacobian used in Q-348 is only a derivative check; global invertibility comes
from the group formula `(W1-2)`.

The attack therefore passes. It leaves a standing falsifier for the next
artifact: any proposed comparison square that holds prefix coordinates
pointwise fixed under a nontrivial realization permutation, rather than
commuting with `J_pi`, is wrong.

```text
W7 = PASS
FRESH_ATTACK = permutation/order covariance plus global branch
PREFIX_COORDINATES_POINTWISE_PERMUTATION_INVARIANT = false | TYPE-R
PREFIX_COORDINATES_PERMUTATION_COVARIANT = true | TYPE-P
```

## 9. Final determination

The projective prefix-trace theorem is a sound coordinate theorem on the
ratified relative-CTP input:

```text
(R_CTP,1,...,R_CTP,N)
  <--faithful character and consecutive ratios-->
(Z_0,Z_1,...,Z_N).
```

It does not build the physical action. Its contribution to the next
commission is exactly this:

1. terminal `Z_N` remains insufficient and Q-347 remains binding there;
2. the complete prefix family loses no cellwise relative-CTP information;
3. at fixed rank two it carries every cycle character, including the S8-A
   triple, so the one-scalar automorphism obstruction no longer applies;
4. the family-natural cell-to-edge comparison and action/2PI square remain
   separate unbuilt objects.

```text
W1 = PASS
W2 = PASS
W3 = PASS
W4 = PASS
W5 = PASS
W6 = PASS
W7 = PASS

SUFFICIENCY_THEOREM = CONFIRMED

PREFIX_FAMILY_AT_RANK2 = CARRIES_CYCLE_CONTENT |
  proof: equations W5-1 through W5-4;
  scope: information content on each typed realized stage;
  not_claimed: full-family comparison or physical action construction

FULL_FAMILY_PREFIX_TO_CYCLE_MAP = NOT_BUILT / TYPE-U
TRANSVERSE_ACTION_COMPARISON_SQUARE = NOT_BUILT / TYPE-U

FENCE_BLOCKED_STRUCTURAL_RESULT = false | TYPE-S

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No register, plan, tracker, git, commit, or push action was performed.
