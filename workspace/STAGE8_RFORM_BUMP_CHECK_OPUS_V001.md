# STAGE 8 — BLIND ADVERSARIAL BUMP CHECK ON R_record,L → WINDING NOT-FORCED
## CODENAME OPUS-BUMP — INVERTED CHECK — [CLAIMED]

Date: 2026-08-13
Role: BLIND ADVERSARIAL CHECKER, INVERTED. The build concluded `WINDING_FORCED =
NOT-FORCED` from `R_record,L = n^2 · K` (K an n-blind kernel). My job is to BREAK
that negative: to find a record-internal way `R_record,L` DOES fix `|n|` that the
build folded into "n-blind" too fast. A false negative would send the program
chasing an external comparand it may not need, so the hunt is adversarial toward
NOT-FORCED, not toward the build.

Fences held throughout: BEDROCK ONLY (no carrier/KK/metric/scale/"alpha rides a
scale" used to attack or to defend). TYPING ONLY — no value of `n`, `kappa`,
`alpha`, any scale, coefficient, or constant is computed, bounded, estimated, or
compared; everything symbolic. No register/tracker/plan/road/ledger/lens read. No
git action. Output name probed before write: ABSENT.

---

## 1. SEALS VERIFIED AT PATH

Recomputed by `shasum -a 256` before reading, under
`/Users/bgm/MB Work/alpha-program-archive/workspace/`:

| Source | Tasked digest | Recomputed | Verdict |
|---|---|---|---|
| `STAGE8_R_RECORD_L_FORM_FABLE_V001.md` | `5e49d20…58f37` | `5e49d2093d4ee17b840cc096d5caf3a6edafda4e37abbd175a7a371c34658f37` | MATCHES-TASKED |
| `STAGE8_SADDLE_FOUNDATION_PARENT_ACTION_DARIO_V001.md` | `1d11f15…effa75` | `1d11f15040f8b85b7e081fccfeddb995c41941c55464d759a2fa91a8feffc775` | MATCHES-TASKED |

Byte spans below index the SUBJECT (`…RFORM_FABLE_V001.md`, 31727 bytes) unless
marked otherwise.

---

## 2. THE WRITE'S n-DEPENDENCE, RE-DERIVED FROM THE CONNECTION-ONLY GROUND

I re-derive the n-dependence myself from the Dario connection-only ground rather
than adopting the build's D2, then check the build against my derivation.

Connection-only ground (`…PARENT_ACTION_DARIO_V001.md`, member 03 span, quoted in
its closure): the record's ratified interacting object is "indexed by CONNECTION /
HOLONOMY HISTORIES ALONE — no metric argument anywhere." That is the whole
`a`-content of the object; there is no second channel.

Character law (subject B6, bytes [7077,7108) and [7245,7272)): the connection
enters each cell only through `z_j^(n)[a_j] = chi_n(h_j[a_j])`, unit-modulus
holonomy characters, with the doubled/relative combination
`Z_N^(n) = chi_n(relative holonomy)` and "exactly one character power" per cell.

Write the holonomy of the abelian record connection as `h_j[a] = exp(i<ell_j,a>)`.
Then `chi_n(h_j[a]) = exp(i n <ell_j, a>)`, a phase LINEAR in the tangent with the
integer character index `n` sitting in the exponent. Two facts I can state without
any value:

- `R_record,L` is, of record (B1), a SECOND mixed derivative at the base point
  `s=t=0`. For a phase `exp(i f)` with `f = n·Phi_tot[a]` LINEAR in `a`
  (`Phi_tot[a] = sum_j <ell_j,a>`), the base point second derivative pulls down
  exactly `(df/ds)(df/dt) = (n Phi_tot[a])(n Phi_tot[b]) = n^2 · Phi_tot[a]Phi_tot[b]`,
  because `f'' = 0`. Higher powers of `n` live only in HIGHER cumulants / higher
  derivatives, which a Hessian does not see. So the object `R_record,L` itself can
  carry `n` at second order and nowhere else in `n`.
- Everything the `n^2` multiplies is n-blind for the sealed reason, not by
  assumption: at the base point every character is trivial, `chi_n(identity) = 1`
  for EVERY `n`, so the base evolution, the write generators `X_j`, the base state,
  and hence the Duhamel kernel `C` carry no `n`; and `|chi_n| = 1` for every `n`
  makes the branch diagonal flat for every `n`. The chains `ell_j` are the
  incidence datum of which edges the holonomy reads — a geometric datum, not a
  representation label, so n-blind.

This reproduces the build's `R_record,L = n^2 · Phi^T C Phi` exactly. My
independent derivation agrees: the object is genuinely second order in `n` and the
kernel is genuinely n-blind. The attacks below therefore cannot come from a
mistake in the `n^2` factoring; they must come from somewhere the SCALING argument
does not reach.

---

## 3. ATTACK 1 — THE PREFACTOR CLAIM (does n appear anywhere but the global n^2?)

I swept every place `n` could hide beyond the prefactor.

- INSIDE K (the kernel C). C is the Duhamel covariance of `X_j` under base
  evolution. Base evolution and `X_j` are set at zero connection, where
  `chi_n(identity)=1` (subject [14500,14522): "n-INDEPENDENT (D2:…)"). CONFIRM
  n-blind.
- INSIDE THE WRITE CHAINS ell_j. `ell_j` selects edges (support/current density,
  the unsupplied G3). It is the argument of the holonomy, orthogonal to the
  character INDEX `n`. A change of `n` does not move `ell_j`; a change of `ell_j`
  does not change `n`. CONFIRM n-blind.
- INSIDE THE CLUSTER/LIMIT STRUCTURE. The relative phase is a SINGLE global
  `n·Phi_tot`, the SAME `n` in every cell's `z_j^(n)` (B5's `D_(n,j)` carries one
  index `n`, not a per-cell index). `n` does not couple to the cell count `N_4`,
  to cluster size, or to subdivision: `chi_n` is a homomorphism, so under
  refinement `chi_n(h_parent) = product chi_n(h_sub)` with the SAME `n` — the
  index is refinement-invariant for every `n`. The cluster-summability tension the
  build flags (subject [14806,14841): the coherent finite-N kernel is all-pairs and
  NOT cluster-summable) is a tension in the SHAPE `C_jk`, which the `n^2` prefactor
  multiplies uniformly; it does not introduce a second `n`. CONFIRM n-blind.
- SIGN. `R_record,L(n) = R_record,L(-n)` (subject [21602,21660)); the quadratic can
  reach at most `|n|`, never the sign. CONFIRM (this is a WEAKENING, not a second
  appearance).

I found NO second, non-scaling appearance of `n`. The one exponent-level
appearance (`exp(i n <ell_j,a>)`) collapses to `n^2` under the second derivative
and to n-blindness under `chi_n(identity)=1`; no third derivative or higher cumulant
enters `R_record,L`.

**ATTACK 1 RESULT: CONFIRMS the build.** `N_ONLY_GLOBAL_PREFACTOR = CONFIRMED`.
Anchor: subject [10094,10135) (the linearization), [12608,12666) (the exact `n^2`
Hessian), [13273,13321) ("scales as n^2 and as nothing else in n"), [13798,13859)
(the post-limit `n^2 Phi^T C Phi`).

---

## 4. ATTACK 2 — THE PREDICATE SWEEP (is there an n-selecting record-internal invariant?)

The build's enumeration (subject [20671,…): PSD, rank, kernel, carrier,
cluster-summability, additivity, refinement-naturality, commutation with pullback,
cross-term presence) is a list of CONGRUENCE-LEVEL / typing predicates of a
symmetric bilinear form. I tested exhaustiveness and n-sensitivity of each and
hunted for omissions.

- EXHAUSTIVENESS. Under congruence, a symmetric bilinear form is classified by rank
  and signature (Sylvester); with the extra sealed structure, add kernel/carrier,
  the cluster-decay type, additivity, and naturality. The build's list covers all
  of these. Signature is captured by PSD (a PSD form has signature `(rank,0,nullity)`).
  The only remaining discriminant is OVERALL SCALE — and reading a scale is barred
  (it is a value) and requires an external normalization. So the typing-level list
  is complete.
- n-SENSITIVITY. Every listed predicate is invariant under `n^2 -> n'^2` (a positive
  global rescaling): PSD (`n^2>0`), rank/kernel/carrier (rescaling is invertible),
  cluster-decay type (shape of `C_jk`), additivity, naturality, cross-term presence
  (subject [21363,21394): the cross term is `n^2 mu phi_f ⊗ phi_H`, its existence a
  property of n-blind `(mu, phi_f, phi_H, C)`). None selects `|n|`.
- CANDIDATE OMISSIONS I tried:
  - INTEGRALITY (`n in Z`). Real, record-internal (characters of a compact abelian
    holonomy form the integer lattice). But it is a predicate of the write LABEL,
    not of `R_record,L`. From `R = n^2 K` you cannot recover `n`: `n^2 K` with `K`
    of unfixed normalization is indistinguishable from `1 · (n^2 K)`. Integrality
    says the prefactor is a perfect square, but with `K`'s scale unfixed of record
    (mu, C symbolic), a perfect-square prefactor times an unknown-scale kernel reads
    off NO `|n|`. Does not force.
  - SIGN-OF-mu → PSD RECONCILIATION (subject [15209,15264): finite-N `mu` sign not
    fixed, post-limit `C` typed PSD). This constrains `mu ≥ 0` post-limit; `n^2 > 0`
    is neutral to it. n-blind. Does not force.
  - POSITIVITY / SELF-CONSISTENCY OVER THE dim-32 FREEDOM (subject [21142,21165):
    "THE FREEDOM IS n-BLIND"). The freedom moves base data (assignments, chains,
    kernels) carrying no `n`; quantifying any admissibility over it cannot introduce
    n-sensitivity. No sealed relation ties the structural integer of the freedom to
    the character index. Does not force.

I found NO record-internal invariant of `R_record,L` that is non-invariant under
n-scaling. The only n-carrier is the barred overall scale, which needs an external
comparand — precisely the build's claim.

**ATTACK 2 RESULT: CONFIRMS the build.** `RECORD_INTERNAL_FORCING_FOUND = NO`.

---

## 5. ATTACK 3 — |n|=1 vs |n|=2 (is there a surface-native discriminant the build missed?)

The surface eliminates `n=0` by zero-variation / charge-flux-access (subject
[21737,21754); B6 [7245,7272)). The task points at a possible surface-native
minimality/generation condition — NOT the barred faithfulness premise — that could
push `n != 0` to `|n|=1`. I examined the strongest such candidate and it is the one
place a naive checker could plant a false forcing, so I treat it in full.

STRONGEST DISSENT: read the sealed phrase "exactly one character power" (B6
[7245,7272)) as "one POWER of the fundamental character `chi_1`", i.e. `chi_n =
chi_1^n` with the exponent pinned to one → `|n|=1`. That would be a
generation/minimality forcing, not faithfulness.

WHY IT FAILS, two independent reasons, both bedrock:

1. IT IS NOT A PREDICATE OF `R_record,L`. Even granting the reading, it is a
   property of the WRITE / character source `W`, upstream of the Hessian. `R = n^2 K`
   exposes only `n^2`; you cannot recover "the character is fundamental / minimally
   generated" from a bilinear form. So this could at most be "the WRITE forces `|n|`",
   never "`R_record,L` forces `|n|`". The task asks the latter. `R_record,L` does not.

2. THE READING IS THE WEAKER ONE, on the surface's own evidence. (a) The surface
   keeps a SEPARATE `n=0` elimination test (subject [21737,21754); B6). If "one
   character power" already pinned `|n|=1`, an `n=0` candidate would never arise and
   no elimination test would be needed — its existence shows the surface treats `n`
   as ranging over the character family, consistent with the build's reading of "one
   character power" as "exactly one FUNCTIONAL per cell" (subject D2(ii), the "no
   second charged functional" clause), i.e. one insertion, not exponent-one. (b) The
   surface reaches `|n|=1` ONLY via the faithfulness result, which is BARRED and not
   consumed (subject [24206,24269)). If "one character power" delivered `|n|=1` for
   free, the surface would not route `|n|=1` through faithfulness. Its doing so is
   direct evidence that "one character power" does NOT pin `|n|=1`.

So the only surface-native handle from `n != 0` to `|n|=1` on record is the BARRED
faithfulness premise; the unbarred "generation" reading is both upstream of `R` and
the less-supported reading of the seal. No bedrock test inside `R_record,L`
discriminates `|n|=1` from `|n|=2`.

**ATTACK 3 RESULT: CONFIRMS the build.** `DISCRIMINATES_MAGNITUDE = NO`.

---

## 6. ATTACK 4 — FENCE CHECK (did the NOT-FORCED conclusion ride an import?)

I checked whether the negative was REACHED via machinery (which would make it a
false negative reached by an import).

- The negative rests on: D2's character-law factorization (bedrock B5/B6, the
  connection-only ground) and B4's tangent complex. The `n^2` factor-out uses only
  `chi_n(identity)=1` and `|chi_n|=1`. No carrier, KK, metric, scale, or `c^2` is
  consumed to reach it.
- The two external comparands the build names (energy form `c_L<.,.>_(2,ell)`;
  `kappa_record`→physical conversion via `Z_Q`) are cited at [22098,22152) and in
  §5.2 as UNAVAILABLE — they are named as the missing forcing route, not consumed to
  produce the negative. Naming an absent comparand is not importing it.
- FAITHFULNESS is explicitly held out (subject [24206,24269)): the negative is
  derived without any injectivity premise.
- I confirm the negative does not secretly need the dim-32 structural integer as a
  KK object: it is used only as an n-blind arena (§4), and the conclusion holds
  whether or not that block is populated.

The one exposure: the negative's SCOPE claim ("an external comparand is genuinely
needed") is only as strong as the exhaustiveness of the comparand search, which is
NAMED (two candidates) rather than proved exhaustive of record. That does not make
the negative machinery-borne; it bounds the negative to "no forcing INSIDE
`R_record,L`", which is exactly what the flag block asserts.

**ATTACK 4 RESULT: CONFIRMS the build.** `NOT_FORCED_USED_MACHINERY = no`.

---

## 7. WHAT WOULD HAVE FLIPPED IT, AND WHY IT DID NOT

A REFUTE required ONE of: (a) a second, non-scaling appearance of `n` inside K /
the carrier / the chains / the cluster structure (Attack 1) — none exists, because
`R_record,L` is a second derivative and `chi_n(identity)=1`; (b) a record-internal
invariant of the FORM non-invariant under `n^2`-scaling (Attack 2) — none exists;
the typing-level invariant list is congruence-complete and every member is
scale-invariant, integrality reads off nothing without an external normalization;
(c) a surface-native `|n|=1` discriminant inside `R` (Attack 3) — the only handle is
the BARRED faithfulness premise and, even taken, it lives in `W` upstream of `R`,
not in `R`. All three fail on bedrock, and the negative itself imports nothing
(Attack 4). The magnitude-sensitive channel is genuinely a RAY: the record's
content fixes `R_record,L` up to the n-blind factor `Phi^T C Phi`, and no
record-internal predicate selects `n` from it.

---

## 8. FINAL FLAG BLOCK

```text
SEALS = BOTH MATCH-TASKED (subject 5e49d20…58f37; ground 1d11f15…effa75).

N_ONLY_GLOBAL_PREFACTOR = CONFIRMED. Re-derived independently from the
  connection-only ground: R_record,L is a base-point second mixed derivative of a
  phase exp(i n Phi_tot) with Phi_tot LINEAR in the tangent, so it pulls down exactly
  n^2 and nothing else in n; higher n-powers sit in higher cumulants a Hessian does
  not see; the kernel C, base evolution, write generators X_j, base state, and chains
  ell_j are n-blind because chi_n(identity)=1 and |chi_n|=1 for every n. No second,
  non-scaling appearance of n exists inside K, the carrier, the chains, or the
  cluster/limit structure. [10094,10135)·[12608,12666)·[13273,13321)·[13798,13859)·
  [14500,14522)·[14806,14841)·[21602,21660).

RECORD_INTERNAL_FORCING_FOUND = NO. The typing-level invariant list is
  congruence-complete (rank, signature-via-PSD, kernel, carrier, cluster-decay,
  additivity, naturality, cross-term presence) and every member is invariant under
  n^2-scaling; integrality n in Z is a predicate of the write label, not of the form,
  and cannot be read off n^2·K without an external normalization of the unfixed
  kernel scale; the sign-of-mu → PSD reconciliation and the cluster-summability
  tension are n-blind; the dim-32 freedom moves only n-blind data. [15209,15264)·
  [21142,21165)·[21363,21394).

DISCRIMINATES_MAGNITUDE = NO. The surface eliminates n=0 by zero-variation /
  charge-flux-access; the strongest surface-native candidate — "exactly one
  character power" read as fundamental-character generation forcing |n|=1 — fails
  twice: it is a property of the write W upstream of R (R=n^2·K exposes only n^2, not
  minimality), and it is the weaker reading of the seal (the surface keeps a separate
  n=0 elimination and reaches |n|=1 only via the BARRED faithfulness premise, both of
  which would be redundant if "one character power" pinned |n|=1). [7245,7272)·
  [21737,21754)·[24206,24269).

NOT_FORCED_USED_MACHINERY = no. The negative rests on the character law (B5/B6) and
  the tangent complex (B4); no carrier/KK/metric/scale/c^2/faithfulness is consumed
  to reach it; the two external comparands are named as unavailable, not consumed.
  [22098,22152).

VERDICT = NOT-FORCED-CONFIRMED (R_record,L alone cannot fix |n|; n enters only as
  the global quadratic prefactor n^2 of an n-blind form, an external n-blind
  comparand is genuinely needed, and the only surface-native |n|=1 handle is the
  barred faithfulness premise which in any case lives upstream of R, not inside it).

FENCE_RESPECTED = CERTIFIED. Typing/blind only; no value of n/kappa/alpha/any scale
  computed, bounded, estimated, or compared; mu and C left symbolic; no
  register/tracker/plan/road/ledger/lens read; seals verified at path; bedrock only
  (no carrier/KK/metric/scale used to attack or defend); no git action; output name
  probed ABSENT before write.

ALL_RESULTS = CLAIMED until panel adjudication.
```
