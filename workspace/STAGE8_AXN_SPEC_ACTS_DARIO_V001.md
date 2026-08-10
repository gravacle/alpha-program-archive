# STAGE 8 — AXN BUILD — THE TWO SPEC ACTS AS DERIVATIONS
## DARIO LANE — RELAY 916 — `[PLAN:AXN-BUILD-C14]`

## 0. Preflight

Relay 916 verified before reading at
`5f424b246d69fbc5019ba02e975b3ca9e2d643a56529ec2a539ca0189ba57700`. Lane guard read DARIO; the
pickup ACK was written before content access. `PROGRAM_STATE_BRIEF_V005.md` verified and read before
task work at `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c`. The requested
output name and its sidecar were clear at pickup.

---

## 1. Law-9b closure — declared first, exact members, full digests

This is the first substantive content in this artifact. Every determination below is taken **at a
named receiver inside this closure**. The two spec acts are attempted **as derivations from the
sealed structure**, and wherever a step turns out to be authorship it is named and typed for the
ledger rather than performed.

```text
C_916 = {
 1  RELAY_PASTE_916_SPEC_ACTS_DARIO_V001.md
      5f424b246d69fbc5019ba02e975b3ca9e2d643a56529ec2a539ca0189ba57700
 2  supervision/PROGRAM_STATE_BRIEF_V005.md
      e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c
 3  STAGE8_AXN_S2_BINDING_CROSSCHECK_CODEX2_V001.md                    [914 — the governing correction]
      87ddbc07bac0692790057e8599a9a0bf4e6217818c162f62a25b46f7d4461aba
 4  STAGE8_AXN_FINITE_BINDING_DARIO_V001.md            [my 911 — SUBJECT of the correction; BR-1, §2.1]
      5f5d3a73e5d9317eef9c91b9d11ffb94904b69ff40ffbe753535503de80e2cce
 5  R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md
      40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9
 6  STAGE8_GAMMA_K_COMPLETED_ALGEBRA_EXTENSION_ATTEMPT_V001.md
      2198524f9f4b4f048953526e4084ae7282e85edce1767e410aef50b013ed0ab1
 7  PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md                          [Level-1]
      532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb
 8  R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md
      10909b5c21e73ecf655462339a27bd645b8d35e3ad11fb6f8cb204c601992995
}
```

**Exact span index** — each recomputed here from the sealed bytes:

| key | sealed bytes | span SHA-256 | content |
|---|---|---|---|
| `CARRIER` | member 5 `[4287,4905)` | `a4953cb66daa6dacf588351447c24defea88068681cbd586e7dd8452a1207f6a` | `K_Sigma`, `R(K)`, `R_c`, the global CAR declaration, the cell matrices |
| `PARENT` | member 5 `[5711,6867)` | `eddc2e9ab66e1036e7defdc514b61214e0adef3b48fced3c3aa7a67b6df5f2c3` | `S_n`, `h_0[g,a]`, `h_K(t)`, the Galerkin permission, and `H_K = dGamma_R(h_K)` |
| `DESCEND` | member 5 `[6867,7879)` | `827cf361f052d36c62e7fc6ea57e61c04cf8c18fc552dcde18bd7ee5e5ef8e3a` | `D_K`, `C_K(x)`, `D_K^2`, the curvature sentence |

All three reproduce the digests I computed at relay 911 and were recomputed rather than carried
forward. Member 3 is used at its §§9.1–9.3 and §10, and member 3's own seal verified before reading.

**Name probe.** `STAGE8_AXN_SPEC_ACTS_DARIO_V001.md` and its sidecar: the workspace listing at
pickup returned a clear name for both. This artifact creates the first instance.

---

## 2. Gates, claim status, and the corrections I am carrying

```text
alpha_computed         = false
proof_authorized       = false
kappa_record_computed  = false
```

Every headline determination here is **CLAIMED** pending opposite-lane cross-check. This report
installs no chain, projection, representation, state, domain, slicing map, or physical object, and
moves no program flag. No member was bound; no fixed point was executed; no end test was run; no
smooth carrier was imported; no common cell was formed; no junction map was evaluated; no physical
quantity was numerically evaluated; no measured constant was consulted. PE-1 through PE-13 remained
pointer-only and were not opened. Builder-A code paths were not accessed.

### 2.1 The 914 correction, accepted in full, with what it costs me

My 911 asserted that for **any** nonzero one-particle `T`, the fermionic `dGamma(T)` is unbounded,
with an `n·||T||` growth law, and built a headline on it: that the C*-membership demand has a
*structural negative answer* on the source side. **That universal claim is false, and the headline
built on it goes with it.** The growth law I quoted is the bosonic picture. Under the CAR relations
occupation numbers are `0` or `1`, so a rank-one projection lifts to an occupation projection.
Reproduced here from the CAR relations rather than taken on report:

```text
CAR relations at n=3 (Jordan-Wigner):  max || {a_i,a_j} ||, || {a_i,a_j^*} - delta_ij I || = 0.000e+00
|| dGamma(|e><e|) - a^*(e)a(e) ||                                                          = 0.000e+00
spec dGamma(P) = {0, 1}          || dGamma(P) || = 1.000000000000
```

I do not get to keep the conclusion and repair the reason underneath it. What I claimed in the ACK
would survive — the *direction* — is tested in §3 and does survive, but only because §3 replaces the
false universal with a criterion, and the criterion is a different and better object.

**CORRECTION PROPAGATION (law 7) — consumers of my wrong sentence, restated rather than left to be
inherited.** Member 3 names them as member 7 §§4.3, 5.2, 6, 7, 9 and the final inclusion/verdict
lines. Restated:

| 911 location | what it said | what it should say |
|---|---|---|
| §4.3 | C*-membership fails on the source side "for structural reasons" | membership **holds exactly on the trace-class part** and fails off it — §3 |
| §5.2 | source inclusion `OBSTRUCTED` in the limit | obstructed **for non-trace-class terms**, which is where `h_0` and the uncompressed `M_c` sit |
| §6 / ITEM14 | component (1) source third reduced to a spec act | unchanged in outcome, corrected in mechanism |
| DISCLOSURE 1 | the demand "should be affiliation, not membership" | the demand should be **split**: membership on the trace-class part, affiliation off it |
| final `INCLUSION` line | `OBSTRUCTED (source limit)` | obstructed **off the trace-class part**; the mechanism is summability, not nonvanishing |

**Two further corrections of mine, from member 3, accepted and checked rather than nodded at.**
(i) Under `R=(h-z)^(-1)` the upper-minus-lower discontinuity is `+2 pi i rho_+`, not the `-2 pi i`
my 909 wrote. Verified: `1/(E'-E-i eps)` has positive imaginary part, so `Im<R(E+i0)> = +pi rho`
and the difference is `+2 pi i rho`. Magnitudes unchanged, so 909's fork-size table stands.
(ii) My 909 called the Stone/Poisson limit "the boundary-value map"; it is the density at one vector
and one component, not a full weak boundary map. Accepted; 909's E3 line is over-scoped and should
read as the density limit only.

### 2.2 BR-1

Member 4 is my own 911 and is the subject of the correction. It carries **zero** confirming weight;
it is present so the propagation table above has an addressee. Everything derived below rests on
members 5–8 and on the CAR relations, not on member 4.

---

## 3. The corrected criterion — a prohibition replaced by a test

**Theorem (fermionic lift: exact norm).** Let `T` be self-adjoint on the one-particle space `K` with
eigenvalues `{lambda_i}` and eigenbasis `{f_i}`. On fermionic Fock space

```text
dGamma(T) = sum_i lambda_i a^*(f_i) a(f_i),
```

and the `a^*(f_i)a(f_i)` are **mutually commuting projections** — this is exactly Pauli exclusion.
Hence the spectrum is the set of subset-sums,

```text
spec dGamma(T) = { sum_(i in S) lambda_i : S subset I },
|| dGamma(T) || = max( sum_i lambda_i^+ , sum_i lambda_i^- ).
```

**Corollary.** `dGamma(T)` is bounded — hence a genuine element of the C*-algebra — **if and only if
`T` is trace-class**, and then `|| dGamma(T) || <= || T ||_1`.

Machine check, four random Hermitian `T` at `n=3`, predicted against actual operator norm:

```text
lam = [-0.9529  0.4798  1.9077]   predicted 2.3874935202   actual 2.3874935202   err 4.44e-16
lam = [-1.3010  0.3916  1.1699]   predicted 1.5615887650   actual 1.5615887650   err 0.00e+00
lam = [-2.7993  1.4902  2.4906]   predicted 3.9808429958   actual 3.9808429958   err 4.44e-16
lam = [-1.7505 -0.3779  0.7843]   predicted 2.1284121423   actual 2.1284121423   err 8.88e-16
```

and the two regimes fall out of the one statement:

```text
T = |e><e|  (trace norm 1)   -> || dGamma(T) || = 1            BOUNDED, a CAR element
T = I_n     (trace norm n)   -> || dGamma(T) || = n            n = 2,3,4,5,6 verified exactly
```

**This subsumes every case in dispute.** It reproduces member 3's rank-one counterexample; it
reproduces my finite-Galerkin claim, since a compression is finite-rank and finite-rank is
trace-class; and it reproduces member 3's *surviving* negative, since an unbounded `T` is not
trace-class. **Being wrong bought a criterion in place of a prohibition** — the producing lane can
now decide any term by testing its summability, where my 911 offered only a blanket refusal.

---

## 4. SPEC ACT (i) — the finite Galerkin carrier and its embeddings

### 4.1 What is derivable

`CARRIER` fixes `K_Sigma = L2(Sigma, S tensor L^q)` with one global `CAR(K_Sigma)`; `PARENT` permits
*"the Galerkin compression of this multiplication operator"* while barring *"a target-selected
projector."* From that plus CAR functoriality:

```text
For any increasing chain of finite-dimensional subspaces  K_1 subset K_2 subset ... subset K_Sigma
with dense union, and orthogonal projections P_n : K_Sigma -> K_n,

  (a)  K |-> CAR(K) carries isometric inclusions to UNITAL *-MONOMORPHISMS, so
       CAR(K_1) subset CAR(K_2) subset ... subset CAR(K_Sigma) canonically;
  (b)  dim K_n = n  =>  CAR(K_n) isomorphic to M_(2^n)(C)          [verified n = 1..4]
  (c)  the union of the CAR(K_n) is norm-dense in CAR(K_Sigma);
  (d)  compressed one-particle operators P_n T P_n are FINITE RANK, hence trace-class,
       hence by section 3 their lifts are BOUNDED and are genuine C* elements;
  (e)  the finite target is CAR(K_n) tensor R(C), the record factor entering ungraded
       because record operators are even -- member 6's canonical-reduction sentence.
```

### 4.2 The stage embedding has the same form as the record side — derived

In the ACK I flagged a hazard: CAR embeddings are **graded**, and member 6's sentence collapsing the
graded tensor to an ordinary one is stated for the *source-record* join, where the record factors are
even — not for a *source-source* stage embedding, where both factors carry nontrivial grading. So I
could not borrow it.

**It is not needed.** The canonical inclusion `CAR(K_n) -> CAR(K_m)` requires no collapse: it is
`A |-> A tensor-hat 1`, and in the Jordan–Wigner representation **with the mode ordering compatible
with the chain** it is literally `A |-> A tensor I`. Verified:

```text
max_j || a_j^(n) tensor I_2  -  a_j^(n+1) ||   = 0.000e+00
unital        || iota(I) - I ||                = 0.000e+00
multiplicative|| iota(XY) - iota(X)iota(Y) ||  = 0.000e+00
*-preserving  || iota(X^*) - iota(X)^* ||      = 0.000e+00
isometric     | ||iota(X)|| - ||X|| |          = 0.000e+00
```

**So the source-side stage embedding and the record-side inclusion have the identical form
`A |-> A tensor I`**, and 911's zero-residual record-side homomorphism composes with it to give a
joint chain

```text
CAR(K_n) tensor R(C_n)  -->  CAR(K_m) tensor R(C_m),   (A |-> A tensor I) tensor (A |-> A tensor I).
```

The hazard I named did not materialise, and the reason it did not is displayed rather than assumed:
the ordering compatibility does the work the collapse sentence would have had to do.

### 4.3 The residual, named and typed

**The record names no chain.** It permits a Galerkin compression and bars a target-selected
projector; it supplies no `{K_n}`. Therefore:

```text
DERIVED : the SCHEMA -- given any admissible increasing chain, (a)-(e) and section 4.2 follow
          canonically, with every residual above at 0.000e+00.
NOT DERIVED : a CANONICAL chain.  No sealed sentence names one.

TYPED FOR THE LEDGER:
  SUPPLEMENT-916-1 (naming act, cheapest kind) -- name one admissible chain {K_n}.
  It selects NO physical content: the schema is uniform over admissible chains, and the
  record already bars the one dangerous class (target-selected projectors).
```

**A forward disclosure, not a blocker for this act.** Chain-*independence of the limit* would need a
core/convergence statement for the Galerkin family. The sealed strong-resolvent convergence in the
record is for the **lattice** family `h_a -> h_0`, a different regulator; no Galerkin-chain
convergence is sealed. That does not affect the finite-stage binding this act asks for, but it is
the thing to prove before any limit statement leans on a particular chain.

```text
ACT_I = DERIVED (schema and embeddings, all residuals 0.000e+00; chain-naming typed as
        SUPPLEMENT-916-1, a naming act selecting no physical content)
```

---

## 5. SPEC ACT (ii) — `dGamma_R`'s receiver and scope for `D_K`

### 5.1 The sealed situation, checked independently

```text
"dGamma" occurs EXACTLY ONCE in member 5 -- line 145, H_K(t) = dGamma_R(h_K(t)).
```

I ran that count myself rather than carry member 3's. The lift's sealed argument is `h_K`, and
nothing applies it to `D_K`. The relevant displayed formulas are:

```text
PARENT   S_n = -i slash(n) gamma^5                                            (line 123)
PARENT   h_K(t) = h_0[g,a] + sum_c v_c(t) M_c(t) tensor S_n tensor iota_c(c_c) (line 133)
PARENT   h_0[g,a] = "the Dirac Hamiltonian OBTAINED FROM the same spin-plus-U(1)
                     connection used in the covariant superconnection"        (line 126)
DESCEND  D_K = i gamma^mu nabla_mu + i gamma^5 C_K(x),
         C_K(x) = sum_c v_c(x) M_c(x) iota_c(c_c)                             (line 162)
```

**The write halves are both displayed. The differential halves are related by a phrase.** That
asymmetry decides the whole act.

### 5.2 The write term: the slicing factor is derived, and fixed by Hermiticity

Comparing the two displayed write terms, `h_K`'s carries `S_n` exactly where `D_K`'s carries
`i gamma^5`. So the converting factor is read off:

```text
S_n = (- slash(n)) (i gamma^5)              || S_n - (-slash n)(i g5) || = 0.000e+00
```

and it is **not a convention**. Verified in an explicit Dirac representation (Clifford residual
`0.000e+00`, `g5^2 = I`, `{g0,g5} = 0`):

```text
i gamma^5   Hermitian ?  FALSE      (D_K is a covariant kernel)
S_n         Hermitian ?  TRUE       (h_K must be self-adjoint)
S_n^2 = I                            || S_n^2 - I || = 0.000e+00
```

Multiplication by `-slash(n)` is exactly what carries the anti-Hermitian covariant factor to the
Hermitian Cauchy-surface one. **The factor is forced by the self-adjointness `h_K` must have, so
this step is a derivation and not a choice.**

### 5.3 The scoped receiver — the split, derived exactly

```text
dGamma_R RECEIVER FOR D_K, on the trace-class criterion of section 3:

IN -- genuine C* elements of CAR(K_n) tensor R(C):
  the write/incidence term   i gamma^5 C_K = i gamma^5 sum_c v_c M_c iota_c(c_c).
  Its h_K image is  sum_c v_c M_c tensor S_n tensor iota_c(c_c),  via the displayed
  factor S_n = (-slash n)(i gamma^5) of section 5.2.
  Under the Galerkin compression of section 4, P_n M_c P_n is FINITE RANK, hence
  trace-class, hence its lift is BOUNDED with || dGamma || <= || . ||_1.
  Its record factor iota_c(c_c) rides through unchanged -- dGamma_R is fiber-preserving
  and no source carrier is copied per record (CARRIER).
  TARGET: MEMBERSHIP.

AFFILIATION-TYPED -- not C* elements at the declared carrier:
  the differential term  i gamma^mu nabla_mu,  whose h_K image h_0[g,a] is unbounded.
  Member 3's surviving negative applies exactly: dGamma(T) restricts to T on the
  one-particle sector, so an unbounded T gives an unbounded lift; equivalently, an
  unbounded T is not trace-class and section 3 refuses it.
  TARGET: AFFILIATION to the represented von Neumann closure.

The split is COMPLETE: D_K has exactly these two summands and each is assigned.
```

### 5.4 The one residual inside the affiliation branch

Assigning the differential term to the affiliation branch needs only that `h_0[g,a]` is unbounded,
which its own description as a Dirac Hamiltonian supplies. **Writing its lifted image concretely
would need the 3+1 slicing identity carrying `i gamma^mu nabla_mu` to `h_0[g,a]` — and member 5
names that relation without displaying it anywhere.** The write half needed no such map because both
its formulas are displayed; the differential half does.

```text
TYPED FOR THE LEDGER:
  SUPPLEMENT-916-2 (display act) -- display the 3+1 slicing identity relating
  i gamma^mu nabla_mu to h_0[g,a].  Standard, but UNSTATED in the closure; writing it
  here would be authorship of an identity the record has only gestured at.
  IT DOES NOT AFFECT THE SPLIT: unbounded is unbounded under either spelling.
```

```text
ACT_II = DERIVED (scope displayed; both branches assigned; SUPPLEMENT-916-2 named and
         shown not to disturb the assignment)
```

---

## 6. Booking line 6

| third | status | basis |
|---|---|---|
| **record** | **BOOKED** (Q-820) | 911's explicit `E_ij` memberships and zero-residual tensor-unit inclusion; member 3 confirms `CLOSED` |
| **source** | **BOOKED (here)** | ACT (i) schema and embeddings at `0.000e+00`; ACT (ii) scope split derived; two supplements typed as a naming act and a display act, neither selecting physical content |
| **field** | **CORE-GATED** | unchanged: `D_K^2` carries U(1)-curvature by member 5's own sentence and the field/CTP sector has no declared algebra; member 3 types it `CORE-BLOCKED` |

```text
LINE6 = 2/3 booked
```

The cascade consequence stands unchanged and is member 3's as much as mine: **line 6 cannot complete
ahead of the core**, because its field third consumes the unbuilt common-origin binding. Booking two
thirds does not soften that; it sharpens it, by leaving exactly one gated component.

---

## 7. Downstream

**Item 14, component (1) — the finite-carrier membership map.** Its record part was closed at 911;
its source part now has both a carrier chain with derived embeddings and a lift receiver with a
derived split. What remains inside component (1) is the field part alone, plus the two typed
supplements. Components (2) the scaling-to-record resolvent intertwiner and (3) the generic
write-plus-tail attachment are untouched.

**The S4 family side.** K19's named family inherits the same split: any member built from the write
term is a finite-stage C* member by §5.3, and any member carrying the differential term is
affiliation-typed. S4 and this receiver stay distinct — `SAME-FAMILY-DISTINCT-RECEIVERS` is carried
unchanged — but the split is a *shared supplier* for both.

**The criterion is the reusable asset.** §3 decides membership for any future lifted term by a
summability test. That is the part of this relay most likely to be used again, and it exists because
member 3 corrected me.

---

## 8. Typed controls (Q-797 discipline)

| control | type | source index |
|---|---|---|
| CAR-relation and rank-one replay, §2.1 | **ELIMINATES** — removes my 911 universal claim by exhibiting a bounded lift | CAR relations; member 3 §9.2 |
| exact-norm theorem and 4-trial check, §3 | **EXPLAINS** — replaces both the false universal and member 3's example with the criterion that generates them | CAR relations |
| stage-embedding residuals, §4.2 | **ELIMINATES** — removes the graded-tensor hazard I named in the ACK, by displaying the ordering that dissolves it | `CARRIER`; member 6 |
| Hermiticity of `S_n` vs `i gamma^5`, §5.2 | **EXPLAINS** — shows the slicing factor is forced rather than chosen | `PARENT`; `DESCEND` |
| single-occurrence `dGamma` count, §5.1 | **TRANSCRIBES** — reproduces member 3's count independently | member 5 |

---

## 9. FREEDOMS-CONSUMED (law 2a)

```text
CARRIED-AS-PARAMETER:
  the declared carrier, the global CAR algebra, and R(C), at member 5's and member 6's scope;
  the Galerkin permission and its bar on target-selected projectors;
  member 3's corrections, all four, as governing;
  the record third as BOOKED and the field third as CORE-GATED;
  Q-784 SAME-FAMILY-DISTINCT-RECEIVERS, with S4 distinct;
  my 911 as the corrected subject, with zero confirming weight.

CONDITIONED-ON:
  every source-side statement on an admissible chain existing (SUPPLEMENT-916-1);
  section 4.2 on the mode ordering being compatible with the chain -- stated, not assumed;
  section 5.3's IN branch on the compression being finite-rank, which is what "finite
    Galerkin" means and is the only reading under which the act is answerable;
  any concrete lifted image of the differential term on SUPPLEMENT-916-2.

SUBSTITUTED:
  NOTHING. No chain {K_n}, projection family, mode ordering, slicing identity,
  representation, state, domain, spectrum, or physical object was authored or selected.
  The two residuals were TYPED FOR THE LEDGER rather than performed, and each was shown
  to select no physical content.

SCALING WEIGHTS:
  NONE CONSUMED; NONE FIXED; NONE SUBSTITUTED.
```

---

## 10. Flattening check, verb audit, byte audit

**FLATTENING CHECK — S01–S37 walked, clean.** A bounded lift was not identified with a bounded
one-particle operator, nor an unbounded one with a non-member without the trace-class step. Finite
rank was not identified with trace-class in general — it implies it, and the implication is the one
used. The record-side inclusion was not identified with the source-side embedding by resemblance:
they were shown to share a form, under a stated ordering condition, with the residual displayed. A
graded tensor was not identified with an ungraded one, and member 6's collapse sentence was **not**
borrowed across receivers. A named relation ("obtained from") was not identified with a displayed
one. A derived split was not identified with a completed lift: §5.4 says exactly what remains.
Booking two thirds was not identified with softening the core gate. `S4` was not merged with this
receiver.

**BUILDER-B INDEPENDENCE:** derived from sealed sources and the opposite lane's correction. A's code
was not accessed. **This lane verifies nothing of its own:** member 4 is my 911, present only as the
addressee of §2.1's propagation table, and every derivation rests on members 5–8 and the CAR
relations.

**SELF VERB AUDIT.** "Derived" is used for §3's theorem, §4's schema and embeddings, and §5's split,
each with a proof in text and a machine residual. "Corrected" and "withdrawn" are used for my own
prior claims, and the withdrawal is stated before anything is built on the replacement. "Typed for
the ledger" is used for the two residuals, and neither is performed. "Booked" is used only for the
two thirds whose content is displayed here or at 911. No chain, slicing map, lift image beyond the
displayed split, or authorization is claimed. `VERB_AUDIT_SELF = CLEAN`.

**BYTE-POSITION SELF-AUDIT.** Measured on the sealed bytes of this file: §1's heading begins at byte
**518**, its closure fence opens at byte **918**, and the exact member list ends at byte
**2059**. A token scan of bytes `[0,918)` for absence-shaped forms — `no `, `not `, `none`,
`never`, `absent`, `missing`, `without`, `lack`, `fail`, `gap`, ` open`, `unresolved`, `underived`,
`false`, `cannot`, `zero`, `stop`, `block`, `wrong`, `refus`, `unswept`, `unsealed` — returns **zero
hits**.

---

## 11. Final lines

```text
CLOSURE = declared-first (byte position: sec-1 heading 518, closure fence 918, members end 2059; pre-closure absence-token scan over 22 forms = 0 hits)
ACT_I = DERIVED. CAR functoriality gives the chain CAR(K_1) subset ... subset CAR(K_Sigma) canonically with dense union; dim K_n = n gives M_(2^n)(C) (verified n=1..4); compressions are finite-rank hence trace-class hence boundedly liftable; and the stage embedding is A |-> A (x) I in the Jordan-Wigner representation with chain-compatible mode ordering -- unital, multiplicative, *-preserving and isometric, ALL RESIDUALS 0.000e+00 -- the SAME FORM as the record-side inclusion, so the joint chain composes with 911's record-side homomorphism. The graded-tensor hazard I flagged at pickup did NOT materialise and member 6's collapse sentence was not borrowed. RESIDUAL TYPED: SUPPLEMENT-916-1, a naming act (no chain is named by the record) selecting no physical content. FORWARD DISCLOSURE: the sealed strong-resolvent convergence is for the LATTICE family, not a Galerkin chain; chain-independence of the limit is unproven and is the thing to prove before any limit statement leans on a chain.
ACT_II = DERIVED (scope displayed). dGamma occurs EXACTLY ONCE in the parent spec, argument h_K -- counted independently. The write halves of D_K and h_K are both displayed, so the slicing factor is read off: S_n = (-slash n)(i gamma^5), residual 0.000e+00, and it is FORCED BY HERMITICITY (i gamma^5 anti-Hermitian, S_n Hermitian, S_n^2 = I) rather than chosen. SCOPED RECEIVER: the write/incidence term is IN as a genuine C* element -- its Galerkin compression is finite-rank hence trace-class hence boundedly lifted, with its record factor riding through unchanged; the differential term i gamma^mu nabla_mu is AFFILIATION-TYPED, since h_0[g,a] is unbounded and section 3 refuses non-trace-class arguments. The split is COMPLETE: D_K has exactly two summands and each is assigned. RESIDUAL TYPED: SUPPLEMENT-916-2, a display act -- the 3+1 slicing identity is NAMED ("obtained from the same spin-plus-U(1) connection") and never displayed; it does not disturb the assignment, since unbounded is unbounded under either spelling.
LINE6 = 2/3 booked (record BOOKED at Q-820; source BOOKED here; field CORE-GATED and unchanged -- D_K^2 carries U(1)-curvature by the record's own sentence and the field/CTP sector has no declared algebra). Line 6 still cannot complete ahead of the core; booking two thirds sharpens that rather than softening it.
DOWNSTREAM = displayed. Item 14 component (1) now lacks only its field part plus the two typed supplements; components (2) and (3) untouched. S4's K19 family inherits the same split as a SHARED SUPPLIER, receivers still distinct. The reusable asset is the criterion itself: || dGamma(T) || = max(sum lam+, sum lam-), so dGamma(T) is a C* element IFF T is trace-class, with || dGamma(T) || <= || T ||_1 -- verified to 8.9e-16 on four random Hermitian trials, reproducing 914's rank-one case at norm 1 and T=I_n at norm n. IT EXISTS BECAUSE 914 CORRECTED ME: my 911 offered a blanket prohibition, and the truth is a test the producing lane can run on any future term.
VERDICT = BOTH-DERIVED (line 6 = 2/3 booked)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
```
