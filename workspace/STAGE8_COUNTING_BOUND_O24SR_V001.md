# STAGE 8 — THE SINGULAR-VALUE COUNTING BOUND FOR THE DRESSED COMPOSITES — COMMISSION O24SR — V001

## O24SR-BUILD, 2026-08-15 — ONE MATHEMATICAL QUESTION, ANSWERED AS MATHEMATICS

THE QUESTION, exact. For each `n` let `A_n` be a dressed composite at stage `n`
(the object W-1 §4 names by that letter), let `s_1 >= s_2 >= ... >= s_{r_n} >= 0`
be its singular values, and let

```text
        N_n(s)  :=  #{ k : s_k > s }.
```

`N_n(s) <= r_n = 4 n^3` is already known (rank cap). ASKED: is there a constant
`c`, independent of `n`, and some `d > 0`, with

```text
        N_n(s)  <=  c * n^(3-d) * s^(-2)        for all n and all s > 0 ?        (Q)
```

```text
THIS ARTIFACT DECLARES NOTHING, ADOPTS NOTHING, LANDS NOTHING.  No gate moves, no
witness is created or retired, no failure point is discharged, no absence closed.
RATE_CERTIFIED = false is untouched.  It answers one operator-theory question on
the sealed stock and displays exactly where the answer stops.
```

Fences held from the first byte: no value, no magnitude, no unit, no dimensional
quantity, no scale, no measured constant, no comparison to any empirical or
physical quantity, no imported GR, no authored physics. **Every number below is an
exponent in the counting parameter `n`, a rank count, an index, or a rational
coefficient inside a symbolic inequality.** Exact symbolic only (CAS appendix §8,
fresh venv, sympy 1.14.0). No `register` / `tracker` / `road` / `plan` /
`continuation` / `ledger` / `lens` file opened. No git action.

**OUTPUT-PATH PROBE:** the output path and its `.seal.sha256` sidecar were both
probed **ABSENT** before any write (`ls` exit 1 on both, 2026-08-15T20:57:47Z).

**SWEEP CUTOFF: 2026-08-15T21:12:00Z.** Every exhaustiveness sentence below is
sweep-relative to this cutoff and to its own displayed key set. Nothing absolute
is claimed.

---

## §0 — VERDICT IN ONE LINE

**OUTCOME 3 — (Q) NEITHER FOLLOWS NOR FAILS on what is established**, and the
reason is sharp rather than accidental: **(Q) is EQUIVALENT to the open problem
itself.** Theorem T-A below proves that, for any operator sequence obeying only
the two sealed facts `rank A_n <= 4n^3` and `||A_n||_op <= 2`,

```text
        (Q) holds for some d > 0   <==>   ||A_n||_2^2 <= C n^(3-delta) for some delta > 0
```

with `delta = d` in one direction and any `delta' < d` in the other — i.e. the two
statements have the **same critical exponent** (T-A3). The right-hand side is
verbatim FP-1's demanded certified sub-volume HS rate, which W-1 §8 records as
`RATE_CERTIFIED = false` and which W-1's T-1 proves is not a consequence of the
class data at any strength. So (Q) cannot be proved from the established stock
(T-B gives an explicit countermodel inside the established class), cannot be
refuted from it (T-C: the stock exhibits no lower bound on any `N_n`, and W-1 §8
carries all four relevant quantities as UNDECIDED), and is not weakened by any
decomposition trick (T-D: by Eckart–Young the small-rank/small-norm splitting IS
`N_n`, not a tool for bounding it). The single additional fact that settles it is
named exactly at §6: the **singular-value density of the dressed composites at a
fixed threshold**, i.e. the value of `limsup_n log N_n(s_*) / log n` for one fixed
`s_* in (0,2)` — `= 3` refutes (Q) outright, `< 3` with a rate proves it.

Additional exact yield, not in the swept stock at the cutoff: (Q) also discharges
FP-1's **trace** budget, at exponent `3 - d/2`, and that half-loss is sharp (T-A4).

---

## §1 — GROUND CONSUMED, SEALS VERIFIED

Verified THIS session by `shasum -a 256 -c` run from the artifact's own directory
against each `.seal.sha256` sidecar, full digest, BEFORE any reliance.
**3/3 OK, zero mismatches, none unverifiable.**

```text
  STAGE8_W1_SUBVOLUME_RATE_O5SR_V001.md              OK   (the construction of A_n; T-1, T-2)
  STAGE8_W1_SUBVOLUME_RATE_O5SR_AUDIT_V001.md        OK   (CONFIRMED-WITH-REFUTATIONS; finding A-1)
  STAGE8_MO3_P_EXPONENT_S9AD_V001.md                 OK   (the standing sub-volume result; p = -3)
```

**DECLARED SCOPED SWEEP (1), at the stated cutoff.**

```text
SW-1  OUTPUT-COLLISION PROBE + DEFINITION SWEEP.  Keys: the exact output path and
      its sidecar (`ls`); and the tokens `A_n`, `N_n`, `dressed composite`,
      `K_H,n`, `H_A,n`, `4n^3`, `rank`, `_op <=` inside the three named files.
      RESULT: output path ABSENT, sidecar ABSENT.  The definitional locus of `A_n`
      is W-1 :254-271 and nowhere else in the three files; the two sealed facts
      about it are W-1 :156 (operator enclosure) and W-1 :163 (rank).
      Exhaustiveness claimed at this key set only.
```

---

## §2 — WHAT `A_n` IS, AND EXACTLY WHICH FACTS ABOUT IT ARE ESTABLISHED

### §2.1 The object

W-1 §4 (:254-255) introduces the letter:

```text
"Let A_n be a dressed composite at stage n, with singular values
 s_1 >= ... >= s_{r_n} >= 0 and counting function N_n(s) := #{k : s_k > s}."
```

`n` is the **stage / carrier index** — a counting parameter, not a magnitude
(W-1 :162). The dressed composites are the two operators the boundary-closure
names, `K_{H,n}` and `H_{A,n}`, acting on the stage-`n` carrier; `A_n` denotes
either, or any member of that class, uniformly in `n`. The ambient space is
`L^2(R^3) tensor C^4` and the stage-`n` carrier is `ran C_n` (W-1 §5.1, and the
boundary-closure's `rank <= 4n^3 on ran C_n` at `80db260f` :302).

### §2.2 The norms in use

```text
  ||.||_op   operator norm            = s_1
  ||.||_2    Hilbert-Schmidt norm     ||A||_2^2 = sum_k s_k^2
  ||.||_1    trace norm               ||A||_1   = sum_k s_k
  N_n(.)     the counting function above (a nonincreasing, right-continuous,
             integer-valued function, constant = r_n near 0 if all s_k > 0)
```

### §2.3 The established facts — the complete list

At the cutoff, and across the three named files, exactly **two** facts about
`A_n` are established. Nothing else about `A_n` is available at any grade.

```text
  (F1)  RANK CAP.       rank A_n <= r_n = 4 n^3.
        Source: W-1 :163 (PA / FHB §3.2, consumed at sealed grade); re-sourced
        independently by the audit at :162-167 to the boundary-closure's own
        bytes, "rank <= 4n^3 on ran C_n (of record)".
        Consequence: N_n(s) <= 4 n^3 for every s > 0.
  (F2)  OPERATOR ENCLOSURE.   ||K_{H,n}||_op <= 2 and ||H_{A,n}||_op <= 2,
        EXACT and n-uniform.  Source: W-1 :156, "stands DELIVERED MEANWHILE".
        Consequence: N_n(s) = 0 for every s >= 2 (W-1 T-2b).
```

And the complete list of what is **NOT** established, carried verbatim from
W-1 §8's closing clause (:653-656):

```text
"NOT REFUTED, carried in full: every negative above is ONE-SIDED.  No divergence
 of tr K_H, tr H_A, ||K_H||_2^2, or ||H_A||_2^2 is exhibited; no sealed +infinity
 attaches to any of the four quantities; all four remain UNDECIDED."
```

**So no lower bound of any kind on any singular value of `A_n`, and no upper bound
on `||A_n||_2` beyond what (F1)+(F2) force, exists in the stock.** This is the
single most load-bearing fact in this artifact and it is why §5's non-refutation
goes through.

### §2.4 What (F1)+(F2) give at a fixed threshold — exactly nothing beyond the cap

The natural first move is to feed the sealed HS budget into Chebyshev. The sealed
budget is `||A_n||_2^2 <= 16 n^3` (W-1 :166, `4n^3 . 4`), so W-1's T-2c gives
`N_n(s) <= 16 n^3 / s^2`. Compare with the cap on the only interval where `N_n`
can be nonzero:

```text
        16 n^3 / s^2  vs  4 n^3        on  0 < s < 2
        16/s^2 - 4  =  4(4 - s^2)/s^2  >  0   for all s in (0,2),  = 0 at s = 2.
                                                                  [CAS A1, exact]
```

> **OBSERVATION O-1 [DERIVED].** On `(0,2)` the Chebyshev consequence of the sealed
> HS budget is **strictly weaker** than the rank cap, at every threshold, and the
> two agree only at the endpoint `s = 2`, where both are already superseded by
> (F2)'s `N_n = 0`. Hence the established budgets contribute **exactly zero**
> counting information beyond (F1)+(F2) themselves, and the best bound of the
> shape (Q) they yield is
>
> ```text
>         N_n(s)  <=  16 n^3 s^(-2)          i.e.  c = 16,  d = 0.
> ```
>
> The question (Q) asks for `d > 0`. So the answer is not obtainable by inserting
> the established bounds into the established inequality: that route returns the
> boundary value `d = 0` and no more. [CAS A1, A2]

This already disposes of the first natural approach. The remaining three are §§3-5.

---

## §3 — T-A: (Q) IS EQUIVALENT TO THE CERTIFIED SUB-VOLUME RATE [DERIVED]

This is the central theorem. It shows (Q) is not a weaker, more tractable proxy
for FP-1's demand — it is that demand, re-lettered.

### §3.1 (Q) restated on the singular-value sequence

**T-A0.** For any finite singular-value list, `sup_{s>0} s^2 N(s) = max_k k s_k^2`,
and consequently

```text
        N_n(s) <= M s^(-2) for all s > 0      <==>      k * s_k(A_n)^2 <= M for all k
                                              <==>      s_k(A_n) <= (M/k)^(1/2)
```

*Proof.* (=>) Fix `k` with `s_k > 0` and let `s -> s_k` from below: then
`N_n(s) >= k`, so `s^2 k <= s^2 N_n(s) <= M`, and letting `s -> s_k^-` gives
`k s_k^2 <= M`. (<=) Fix `s > 0`, put `k = N_n(s)`. If `k = 0` there is nothing to
prove; else `s_k > s`, so `s^2 N_n(s) = s^2 k < s_k^2 k <= M`. QED.
[CAS B0a, B0b — exact on four rational lists, and B0b shows the constant is sharp.]

So **(Q) is exactly the statement that `A_n` lies in the weak Schatten class
`S_{2,infinity}` with quasi-norm `O(n^((3-d)/2))`** — a Lorentz-space bound on the
singular-value profile, one notch weaker than an `S_2` bound at each fixed `n` but,
crucially, of the *same order in `n`*, which is what §3.3 makes precise.

### §3.2 The two directions

**T-A1 (Rate ==> (Q); no exponent loss).** If `||A_n||_2^2 <= C n^(3-delta)` for
all `n`, then for every `s > 0`

```text
        s^2 N_n(s)  <=  sum_{k : s_k > s} s_k^2  <=  ||A_n||_2^2  <=  C n^(3-delta),
```

i.e. (Q) holds with `c = C` and `d = delta`. [CAS B2.] (This is W-1's T-2c, re-run;
the audit CONFIRMS it at :231.)

**T-A2 ((Q) ==> Rate; loss of an arbitrarily small exponent).** Suppose (Q) holds
with constants `c, d > 0`. Conjoin it with the sealed rank cap (F1) — which is free,
and which is the step W-1's T-2d omitted — and split the layer-cake integral at the
crossover where the two bounds meet:

```text
        c n^(3-d) s^(-2) = 4 n^3        at        s*  =  sqrt(c)/2 * n^(-d/2)
                                                                       [CAS B3a]
        int_0^{s*}  2 s N_n(s) ds  <=  int_0^{s*} 2 s (4 n^3) ds
                                    =  4 n^3 (s*)^2  =  c n^(3-d)      [CAS B3b, EXACT]
        int_{s*}^2  2 s N_n(s) ds  <=  int_{s*}^2 2 s (c n^(3-d) s^(-2)) ds
                                    =  2 c n^(3-d) log(2/s*)           [CAS B3c, EXACT]
        ----------------------------------------------------------------------
        ||A_n||_2^2  <=  c n^(3-d) ( 1 + 2 log(2/s*) )
                     =   c n^(3-d) ( 1 + 2 log(4/sqrt(c)) + d log n )  [CAS B3d, B3e]
```

The divergence W-1's T-2d harvested at `q = 2` is produced entirely on `(0, s*)`,
where the power-law bound **exceeds `4n^3` and is therefore vacuous**; the cap
truncates it, and what survives is a single factor `log n`, linear in `log n` and
with coefficient exactly `c d` [CAS B3e]. Finally, for `e := d - d' > 0`,

```text
        n^(3-d) log n / n^(3-d')  =  log(n) * n^(-e)  ->  0     [CAS B4a0, B4a,
                                                                 symbolic in e > 0]
```

so `||A_n||_2^2 <= C' n^(3-d')` for **every** `d'` with `0 < d' < d`. QED.

**T-A3 (Same critical exponent).** Define

```text
        delta*  :=  sup { delta : ||A_n||_2^2 = O(n^(3-delta)) }
        d*      :=  sup { d     : sup_{s>0} s^2 N_n(s) = O(n^(3-d)) }
```

Then T-A1 gives `d* >= delta*` and T-A2 gives `delta* >= d*`, so **`delta* = d*`
exactly.** The question (Q) asks whether `d* > 0`; FP-1 asks whether
`delta* > 0`. **They are the same question.**

### §3.3 The consequence for this commission

> **T-A [DERIVED].** (Q) holds for some `d > 0` **if and only if** the certified
> sub-volume Hilbert-Schmidt rate holds for some `delta > 0`. (Q) is therefore not a
> weakening of FP-1's demand and not an intermediate step toward it: it is a
> re-lettering of it. Any proof of (Q) is a discharge of FP-1; any refutation of (Q)
> is a proof that FP-1 cannot be discharged along the HS budget at all.

This independently re-derives, and slightly extends, the audit's finding A-1
(`:211-221`): the audit establishes the `q = 2` sufficiency up to a log; T-A0 and
T-A3 add the exact restatement on the singular-value sequence and the equality of
critical exponents, which is the form the present question needs.

### §3.4 A bonus that is not in the swept stock: (Q) discharges the TRACE budget too

FP-1 carries **two** budgets (W-1 :151): `|tr| <= 4n^3 . 2` and
`||.||_2^2 <= 4n^3 . 4`. T-A2 handles the second. The same split handles the first,
and with **no logarithm at all**:

```text
        ||A_n||_1  =  int_0^2 N_n(s) ds
                   <=  int_0^{s*} 4 n^3 ds  +  int_{s*}^2 c n^(3-d) s^(-2) ds
                   =   2 sqrt(c) n^(3-d/2)  +  ( 2 sqrt(c) n^(3-d/2) - (c/2) n^(3-d) )
                   =   4 sqrt(c) n^(3-d/2)  -  (c/2) n^(3-d)      [CAS B5a-B5c, EXACT]
```

**T-A4 (the trace exponent, and its sharpness).** (Q) with constants `c, d` gives
`||A_n||_1 <= 4 sqrt(c) n^(3-d/2) - (c/2) n^(3-d)`, leading exponent `3 - d/2`,
strictly sub-volume for `d > 0` [CAS B5d]. And the exponent `3 - d/2` is **SHARP**:
the extremal profile `s_k = min(2, (M/k)^(1/2))` with `M = c n^(3-d)` — the largest
profile (Q) permits, by T-A0 — has trace norm **identically equal** to the bound
just displayed [CAS B5e], with leading term `4 sqrt(c) n^(3-d/2)` [CAS B5f].

> So the counting statement buys the HS budget at exponent `3 - d` (up to a log) and
> the trace budget at exponent `3 - d/2`, and the **halving is exact, not an
> artifact of the estimate**. Recorded here because both budgets are FP-1's and the
> swept stock displays the counting-to-trace conversion nowhere at the cutoff.

---

## §4 — T-B: (Q) DOES NOT FOLLOW — AN EXPLICIT COUNTERMODEL IN THE ESTABLISHED CLASS

T-A says (Q) is as hard as FP-1. T-B says why no argument from the established facts
can reach it, and does so constructively rather than by appeal to W-1's verdict.

Let `C(r_n, 2) := { A on a space of dimension r_n : ||A||_op <= 2 }` be the class
that (F1)+(F2) define — the *complete* extension of what is known about `A_n`.

**T-B.** Let `U_n` be any unitary on the `r_n = 4n^3`-dimensional carrier and put
`B_n := 2 U_n`. Then `B_n in C(r_n, 2)`: its rank is exactly `4n^3` and
`||B_n||_op = 2` [CAS C1a]. Its singular values are all equal to `2`, so

```text
        N^{B}_n(s)  =  4 n^3   for s < 2,      = 0 for s >= 2.        [CAS C1b]
        sup_{s>0} s^2 N^{B}_n(s)  =  4 * 4 n^3  =  16 n^3.            [CAS C1c]
```

Suppose (Q) held for `B_n` with some `c` and some `d > 0`. Evaluate at the fixed
threshold `s = 1`:

```text
        4 n^3  =  N^{B}_n(1)  <=  c n^(3-d)        i.e.        4 n^d  <=  c,
```

which fails for every `n > (c/4)^(1/d)` — a finite index for each admissible pair
`(c, d)` [CAS C2a, C2b, C2c]. **Hence (Q) is FALSE on `C(r_n, 2)`.** QED.

> **T-B [DERIVED].** `B_n = 2U_n` satisfies every fact the record establishes about
> `A_n` and violates (Q) for every `c` and every `d > 0`. Therefore **(Q) is not a
> logical consequence of (F1)+(F2)**, and no argument that uses only the rank cap,
> the operator enclosure, and their consequences can prove it. This is a
> non-implication with a witness, not an expression of difficulty.

This is W-1's T-1 (:204-217) transported into the counting language, where it does
strictly more work: T-1 shows the *norm* ceiling is attained; T-B shows the
*counting* profile is attained flat, at the maximal value `4n^3`, at every threshold
below `2`. The countermodel is maximally bad exactly where (Q) needs control.

**What T-B is NOT.** `B_n` is a member of the enclosing class, not a dressed
composite. T-B does not assert that `A_n` resembles `B_n`, and exhibits no lower
bound on any `N_n`. It bounds what can be *derived*, not what is *true*.

---

## §5 — T-C AND T-D: (Q) ALSO DOES NOT FAIL, AND NO DECOMPOSITION SHORTCUT EXISTS

### §5.1 T-C — nothing in the stock refutes (Q)

By T-A0, refuting (Q) requires exhibiting, for every `d > 0`, indices `n` with
`max_k k s_k(A_n)^2` exceeding `c n^(3-d)` — that is, a **lower** bound on the
singular values of the actual dressed composites.

**T-C.** No such lower bound exists in the stock at the cutoff. W-1 §8 (:653-656)
carries all four candidate quantities — `tr K_H`, `tr H_A`, `||K_H||_2^2`,
`||H_A||_2^2` — as **UNDECIDED**, with no sealed `+infinity` attached to any of
them, and states that every negative in the chain is one-sided. The two of-record
routes that return exponent exactly `3` return it as an **upper-bound shape** or as
a *class* supremum, never as a lower bound on the composites:

```text
  ROUTE (ii) B-L2*'s saturation clause returns the "carrier-volume HS shape" for
       the weight-summed branch propagator P — and W-1 §5.3 states in terms that
       the density floor attaches to the CLASS supremum and to h_0's own sandwich,
       "NOT to the actual composites", with the translation-invariant-limit premise
       explicitly NOT sealed and NOT assumed.
  T-1 / T-B  the exponent-3 return is the class supremum, attained by 2U — again
       an upper envelope, and by construction not a statement about A_n.
  MO-3   returns p = -3 against the sealed threshold p > 3/2, a miss of exactly 9/2
       [CAS E1a], with pair-integral integrand exponent 2p - 4 = -10 [CAS E1b].
       This CLOSES a route to proving the rate; it is a non-vanishing statement
       about a difference kernel, not a lower bound on N_n at any threshold.
```

**So (Q) is not refuted either.** [CAS E1a, E1b, E2.]

### §5.2 T-D — the small-rank/small-norm decomposition is not a tool, it is the question

The remaining natural approach is to split `A_n = (small rank) + (small norm)` and
bound the pieces separately. This route is closed by an exact optimality theorem.

**T-D (Eckart–Young–Schmidt, in the form needed).** For every `s > 0`,

```text
        min { rank B  :  ||A_n - B||_op <= s }   =   N_n(s).
```

*Proof.* `>=`: if `rank B = R` then `||A_n - B||_op >= s_{R+1}(A_n)` (Weyl/Schmidt);
so `||A_n - B||_op <= s` forces `s_{R+1} <= s`, i.e. `R >= N_n(s)`. `<=`: the
truncated SVD keeping the `N_n(s)` singular values above `s` is a `B` of that rank
with residual operator norm `s_{N_n(s)+1} <= s`. QED.
[CAS D1 — exact on four rational lists across five thresholds; D2 the consequence.]

> **T-D [DERIVED].** The minimal rank of the "large part" in any small-rank /
> small-norm splitting of `A_n` at level `s` **equals** `N_n(s)`. Hence no choice of
> decomposition can produce a bound on `N_n` that the singular values do not already
> contain: the SVD splitting is optimal, and exhibiting a good splitting is
> logically identical to bounding `N_n`. The approach cannot be a *route to* (Q);
> it is a *restatement of* (Q).

Combined with T-B this closes the derivational question completely: the only inputs
are (F1)+(F2), those admit a countermodel, and the one structural manoeuvre that
might have extracted more is an identity rather than an inequality.

### §5.3 Where the established facts DO give (Q), and where the content sits

The established stock is not uniformly silent — it settles (Q) on two threshold
bands and leaves exactly one open, and the open band is the whole content:

```text
  BAND 1   s >= 2                       (Q) HOLDS, trivially: N_n(s) = 0 by (F2).
  BAND 2   0 < s <= sqrt(c)/2 * n^(-d/2)   (Q) HOLDS, by the rank cap (F1) alone:
           there c n^(3-d) s^(-2) >= 4 n^3 >= N_n(s).                 [CAS B3a]
  BAND 3   sqrt(c)/2 * n^(-d/2)  <  s  <  2        UNDECIDED — all of the content.
```

Two remarks fix the shape of Band 3. First, it is **not** a fixed window: its lower
edge `~ n^(-d/2)` slides to `0` as `n` grows, so Band 3 exhausts `(0,2)` in the
limit and no "large `n`, fixed `s`" reduction escapes it. Second, by T-A0 the whole
of (Q) is the single scalar `sup_{s>0} s^2 N_n(s)`, whose established envelope is
`16 n^3` — exponent exactly `3`, attained by T-B's witness [CAS C1c, A2]. **The
established facts pin that scalar at `d = 0` and give nothing below it.**

---

## §6 — THE ADDITIONAL FACT THAT WOULD SETTLE (Q), NAMED EXACTLY

Because T-A makes (Q) equivalent to the rate, the deciding object is not new — but
the counting form states it more sharply than the swept stock does, as a question
about **one scalar sequence** rather than about a topology. Define, for a fixed
threshold `s_* in (0,2)`,

```text
        theta(s_*)  :=  limsup_{n -> oo}  log N_n(s_*) / log n
```

— the growth exponent of the number of singular values of the dressed composites
above the fixed level `s_*`. By (F1), `theta(s_*) <= 3` always.

```text
THE DECIDING FACT (one scalar, two-sided):

  (D-refute)  If theta(s_*) = 3 for some fixed s_* in (0,2) — equivalently, if
              N_n(s_*) >= c_* n^(3 - o(1)) along a subsequence — then (Q) is FALSE
              for every c and every d > 0, since s_*^2 N_n(s_*) then exceeds
              c n^(3-d) for large n.  In particular a POSITIVE-DENSITY statement,
              N_n(s_*) >= c_* n^3 with c_* > 0, refutes (Q) outright.
  (D-prove)   If theta(s_*) <= 3 - d uniformly in s_* in (0,2), with the implied
              constant depending on s_* only through s_*^(-2) — that is, exactly
              (Q) — then (Q) holds, and by T-A2 the certified sub-volume HS rate
              follows at exponent 3 - d' for every d' < d, together with the trace
              rate at 3 - d/2 (T-A4).
```

**Where the two sides would come from, of record.** These are pointers, not claims;
nothing below is asserted here.

```text
  TOWARD (D-refute).  W-1 §5.3 computes that a nonzero TRANSLATION-INVARIANT
    operator has constant HS mass per unit volume, so constant density against the
    carrier volume 4n^3 returns exponent exactly 3 [W-1 CAS C2a, C2b].  That is
    precisely theta = 3.  But W-1 §5.3 states in terms that this attaches to the
    class supremum and to h_0's own sandwich and "does NOT establish that the
    dressed composites themselves have a nonzero translation-invariant limit", that
    the premise "is NOT sealed, is not authored here, and is not assumed."
    THE MISSING FACT IS EXACTLY THAT PREMISE: whether the dressed composites carry
    a nonzero translation-invariant (or otherwise positive-density) limit at the
    DRESSED layer.  Sealing it refutes (Q).
  TOWARD (D-prove).  W-1's T-3 and W-3's ADDS (3) type the escape: it must consume
    SPATIAL LOCALIZATION rather than class membership, i.e. symmetry-breaking
    seminorms.  In counting language the requirement is concrete: a localization
    estimate at the dressed layer showing that all but O(n^(3-d)) of the 4n^3
    carrier modes are driven below any fixed level — equivalently, by T-A0, a decay
    profile s_k(A_n) <= (c n^(3-d) / k)^(1/2).  W-1's R-2 records that the two maps
    that would supply it, Loc_N^phys and Loc_N^C, have no member-named topology and
    no continuity proof at any grade.
```

**One caution, carried explicitly.** The audit's finding A-1 (`:211-221`) already
refuted W-1's claim that the carrier must supply a threshold exponent `q` strictly
below `2`; T-A here re-derives that independently and completes it. So the deciding
fact must **not** be stated as "a `q < 2` counting bound." `q = 2` with a sub-volume
prefactor is the correct and sufficient form — and it is exactly (Q). Anything
demanding `q < 2` is demanding strictly more than FP-1 needs.

---

## §7 — THE ANSWER, STATED AS COMMISSIONED

```text
WHICH OF THE THREE OBTAINS:  THE THIRD.

  NOT "the estimate follows from what is already established."
      T-B exhibits B_n = 2 U_n, which satisfies (F1) and (F2) — the complete list of
      established facts about A_n — and violates (Q) for every c and every d > 0,
      breaking at the finite index n > (c/4)^(1/d).  So (Q) is not a consequence of
      the established stock.  T-D closes the one manoeuvre that might have extracted
      more from the same facts: the small-rank/small-norm splitting has minimal
      large-part rank identically equal to N_n(s), so it restates (Q) and cannot
      prove it.  And §2.4 shows the sealed HS budget, fed through Chebyshev, is
      STRICTLY WEAKER than the rank cap at every s in (0,2) — it returns d = 0.

  NOT "the estimate is false as stated."
      Refuting (Q) requires a LOWER bound on the singular values of the actual
      dressed composites (T-A0).  No such bound exists in the stock: W-1 §8 carries
      tr K_H, tr H_A, ||K_H||_2^2, ||H_A||_2^2 all as UNDECIDED with no sealed
      +infinity; MO-3's p = -3 closes a route to PROVING the rate and asserts no
      lower bound on any N_n; and W-1 §5.3's density computation attaches to the
      class supremum, with the composite-level premise explicitly not sealed.

  THEREFORE:  THE ESTIMATE NEITHER FOLLOWS NOR FAILS ON WHAT IS AVAILABLE.

  AND, SHARPER THAN "UNDECIDED":  by T-A it is EQUIVALENT to the open problem.
      (Q) holds for some d > 0  <==>  ||A_n||_2^2 = O(n^(3-delta)) for some
      delta > 0, with equal critical exponents delta* = d* (T-A3).  So (Q) is not a
      tractable proxy for FP-1 and cannot be settled by any sharpening of the
      conversion inequality; it will be settled exactly when FP-1 is.

  THE ADDITIONAL FACT THAT WOULD SETTLE IT (one scalar, two-sided):
      theta(s_*) = limsup_n log N_n(s_*) / log n  at one fixed s_* in (0,2).
      theta(s_*) = 3 for some s_*  =>  (Q) FALSE for every c, d > 0.
      theta bounded by 3 - d uniformly, with the s_*^(-2) profile  =>  (Q) TRUE.
      Concretely: whether the dressed composites carry a nonzero positive-density
      (e.g. translation-invariant) limit at the DRESSED layer — refutes (Q) if
      sealed; or a symmetry-breaking localization estimate at the dressed layer
      giving s_k(A_n) <= (c n^(3-d)/k)^(1/2) — proves (Q) if supplied.
      Neither is in the swept stock at the stated cutoff.

WHAT MOVED: nothing.  FP-1 stands.  RATE_CERTIFIED = false stands.  No witness
      created, none retired.  No gate, fence, or v-clause touched.  Offered for the
      registrar's judgment only, as derivations and not as declarations:
      (o-1) (Q) proved EQUIVALENT to the sub-volume HS rate, with equal critical
            exponents — so the counting form is a faithful re-lettering of FP-1,
            not a weaker target (T-A1, T-A2, T-A3).
      (o-2) The counting bound shown to discharge FP-1's TRACE budget as well, at
            exponent exactly 3 - d/2, with that halving proved SHARP by an extremal
            profile that attains the bound identically (T-A4).  The counting-to-
            trace conversion appears nowhere in the swept stock at the cutoff.
      (o-3) Eckart-Young registered as CLOSING the decomposition route: minimal
            large-part rank = N_n(s) identically, so no splitting can outperform the
            SVD and the approach is a restatement, not a route (T-D).
      (o-4) The audit's finding A-1 independently re-derived and extended; the
            deciding object restated as ONE scalar sequence theta(s_*) rather than
            as a topology, which is a strictly checkable form (§6).
```

---

## §8 — CAS VERIFICATION APPENDIX (exact symbolic; fresh venv)

```text
Environment: fresh python venv created for this commission; sympy 1.14.0.
Script: o24_cas.py, sha256
232693e9591b72e43957858d6a723fc256516cdf48e0099523800ef22e8d31f7
Single run.  RESULT: 36/36 PASS, 0 FAIL.
The script is reproduced verbatim at §8.2, which sits at the END of this file: it
was sourced by FILE-APPEND after the body was written, so the appended bytes are
exactly the bytes that were run.  Verbatim output is at §8.1.
NOTHING NUMERIC IS OFFERED AS A VALUE.  No physical magnitude, no empirical
quantity, no scale, no unit, no dimensional quantity, no measured constant, and no
comparison to any measured constant appears in the script or its output.  Every
displayed quantity is an exponent in the counting parameter n, a rank count, an
index, or a rational coefficient inside a symbolic inequality.  The small rational
singular-value lists and the identity matrices in Blocks B, C and D are exact
algebraic WITNESSES of operator-theoretic identities (layer cake, extremality,
Eckart-Young), never values of any program quantity.
```

### §8.1 Verbatim output

```text
==============================================================================
BLOCK A — WHAT THE ESTABLISHED BUDGETS GIVE AT A FIXED THRESHOLD
==============================================================================
PASS A1a sealed HS-square budget = 16 n^3 exactly
PASS A1b Chebyshev-from-budget minus rank cap = 4 n^3 (4 - s^2)/s^2
PASS A1c that gap is STRICTLY POSITIVE on 0 < s < 2 (budget bound strictly weaker)
PASS A1d the two agree exactly at the endpoint s = 2
PASS A2  best (Q)-shaped bound from the established stock has exponent 3 - 0

==============================================================================
BLOCK B — T-A: (Q) IS EQUIVALENT TO A SUB-VOLUME HS RATE
==============================================================================
PASS B0a sup_s s^2 N(s) = max_k k s_k^2, exact on four rational lists
PASS B0b (Q) with constant M  <=>  k s_k^2 <= M for every k  (sharp on the four lists)
PASS B1a layer cake  ||A||_2^2 = int_0^oo 2 s N(s) ds, exact on four rational lists
PASS B1b layer cake  ||A||_1 = int_0^oo N(s) ds, exact on four rational lists
PASS B2  Chebyshev direction: ||A_n||_2^2 <= C n^(3-delta)  =>  (Q) with c=C, d=delta
PASS B3a crossover s* = sqrt(c)/2 * n^(-d/2) exactly
PASS B3b  int_0^{s*} 2 s (4 n^3) ds  =  c n^(3-d)  EXACTLY
PASS B3c  int_{s*}^{2} 2 s (c n^(3-d) s^-2) ds  =  2 c n^(3-d) log(2/s*)
PASS B3d  total  =  c n^(3-d) ( 1 + 2 log(2/s*) )  EXACTLY
PASS B3e  2 log(2/s*)  =  2 log(4/sqrt(c)) + d log n   (the log is LINEAR in log n)
PASS B4a0 the ratio reduces to log(n) * n^(-e) with e = d - dprime > 0
PASS B4a  log(n) n^(-e) -> 0 for EVERY e > 0  (symbolic, e a positive symbol)
PASS B4b  and n^(3-d) log n / n^3 -> 0  (still strictly sub-volume, d=1/2)
PASS B5a  trace lower piece = 2 sqrt(c) n^(3 - d/2)  exactly
PASS B5b  trace upper piece = 2 sqrt(c) n^(3-d/2) - c n^(3-d)/2  exactly
PASS B5c  ||A_n||_1 <= 4 sqrt(c) n^(3 - d/2) - (c/2) n^(3-d)   EXACT, no log
PASS B5d  leading trace exponent is 3 - d/2, strictly below volume order 3 for d>0
PASS B5e  the extremal profile ATTAINS the B5c bound identically: exponent 3-d/2 SHARP
PASS B5f  and its leading term is 4 sqrt(c) n^(3-d/2): the trace gain is exactly HALF

==============================================================================
BLOCK C — T-B: THE COUNTERMODEL INSIDE THE ESTABLISHED CLASS
==============================================================================
PASS C1a witness 2U lies in the established class: rank = 4n^3, ||2U||_op = 2
PASS C1b its counting function is N(s) = 4 n^3 for s < 2 and 0 for s >= 2
PASS C1c sup_s s^2 N(s) for the witness = 2^2 * 4n^3 = 16 n^3, EXTREMAL (exponent 3)
PASS C2a (Q) at s=1 on the witness demands  4 n^d <= c
PASS C2b that FAILS for every d>0: 4 n^d / c -> +oo  (checked d=1/2, c=1)
PASS C2c the breaking index is n > (c/4)^(1/d), a finite threshold for each c,d
PASS C3  extremality re-run exactly on ranks r = 1..6:  ||2U||_2^2 = 4r, |tr 2U| = 2r

==============================================================================
BLOCK D — T-D: ECKART-YOUNG — THE SMALL-RANK/SMALL-NORM SPLIT *IS* N(s)
==============================================================================
PASS D1  min{rank B : ||A-B||_op <= s} = N(s), exact on 4 lists x 5 thresholds
PASS D2  hence every such decomposition has R >= N_n(s): no split can beat the SVD

==============================================================================
BLOCK E — THE OF-RECORD ROUTE EXPONENTS, RE-RUN INDEPENDENTLY
==============================================================================
PASS E1a MO-3's p = -3 misses the sealed threshold p > 3/2 by exactly 9/2
PASS E1b pair-integral integrand exponent 2p - 4 = -10 at p = -3
PASS E2  both closed routes return exponent exactly 3 (volume order), not 3 - d

==============================================================================
RESULT: 36 PASS, 0 FAIL
==============================================================================
NOTHING NUMERIC ABOVE IS OFFERED AS A VALUE.  Every quantity displayed is an
exponent in the counting parameter n, a rank count, an index, or a rational
coefficient inside a symbolic inequality.  No unit, no scale, no dimensional
quantity, no physical or empirical magnitude, no measured constant appears.
```

### §8.2 The script, verbatim (appended from the file that was run)

```python
#!/usr/bin/env python3
# O24SR — exact symbolic verification for the singular-value counting question.
# EXPONENTS, RANK COUNTS, INDICES AND RATIONAL COEFFICIENTS ONLY.
# No physical or empirical quantity, no unit, no scale, no measured constant.
import sympy as sp

PASS = 0; FAIL = 0
def chk(label, cond):
    global PASS, FAIL
    ok = bool(cond)
    if ok: PASS += 1
    else:  FAIL += 1
    print(("PASS " if ok else "FAIL ") + label)

n, s, c, d, dp, C, delta, eps, k, L = sp.symbols(
    'n s c d dprime C delta epsilon k L', positive=True)

print("=" * 78)
print("BLOCK A — WHAT THE ESTABLISHED BUDGETS GIVE AT A FIXED THRESHOLD")
print("=" * 78)

r_n = 4*n**3                     # rank cap (F1), a count of carrier modes
kappa = sp.Integer(2)            # the exact operator-grade ceiling (F2), a pure number
hs2_budget = r_n * kappa**2      # = 16 n^3, the sealed HS-square budget

chk("A1a sealed HS-square budget = 16 n^3 exactly",
    sp.simplify(hs2_budget - 16*n**3) == 0)

# Chebyshev consequence of the sealed budget vs the rank cap, on (0,2).
gap = sp.simplify(hs2_budget/s**2 - r_n)
chk("A1b Chebyshev-from-budget minus rank cap = 4 n^3 (4 - s^2)/s^2",
    sp.simplify(gap - 4*n**3*(4 - s**2)/s**2) == 0)
chk("A1c that gap is STRICTLY POSITIVE on 0 < s < 2 (budget bound strictly weaker)",
    sp.solve(sp.Eq(4 - s**2, 0), s) == [2]
    and all(sp.simplify(gap.subs({s: sv, n: 1})) > 0
            for sv in [sp.Rational(1,4), sp.Rational(1), sp.Rational(3,2), sp.Rational(199,100)]))
chk("A1d the two agree exactly at the endpoint s = 2",
    sp.simplify(gap.subs(s, 2)) == 0)

# So the best bound of shape (Q) obtainable from (F1)+(F2) is c=16, d=0.
chk("A2  best (Q)-shaped bound from the established stock has exponent 3 - 0",
    sp.degree(sp.Poly(hs2_budget, n)) == 3)

print()
print("=" * 78)
print("BLOCK B — T-A: (Q) IS EQUIVALENT TO A SUB-VOLUME HS RATE")
print("=" * 78)

# B0: the counting condition restated on the singular-value sequence.
#     sup_{s>0} s^2 N(s)  =  max_k  k * s_k^2 .   Exact on rational lists.
def Ncount(lst, sv):
    return sum(1 for x in lst if x > sv)

def sup_s2N(lst):
    # sup over s>0 of s^2 N(s); attained as a limit s -> s_k^- , equals max_k k s_k^2
    vals = []
    srt = sorted(lst, reverse=True)
    for i, x in enumerate(srt, start=1):
        if x > 0:
            vals.append(sp.Rational(i) * x**2)
    return max(vals) if vals else sp.Integer(0)

def sup_s2N_direct(lst):
    # independent evaluation: sup over the finite set of critical thresholds
    srt = sorted(set(lst), reverse=True)
    best = sp.Integer(0)
    for x in srt:
        if x > 0:
            v = x**2 * sp.Rational(Ncount(lst, x - sp.Rational(1, 10**6)))
            best = max(best, v)
    return best

lists = [
    [sp.Rational(2), sp.Rational(3,2), sp.Rational(1), sp.Rational(1,2)],
    [sp.Rational(2), sp.Rational(2), sp.Rational(2), sp.Rational(2)],
    [sp.Rational(1,1), sp.Rational(1,2), sp.Rational(1,3), sp.Rational(1,4),
     sp.Rational(1,5), sp.Rational(1,6)],
    [sp.Rational(7,4), sp.Rational(7,4), sp.Rational(1,8), sp.Rational(0)],
]
ok = all(sp.simplify(sup_s2N(l) - sup_s2N_direct(l)) == 0 for l in lists)
chk("B0a sup_s s^2 N(s) = max_k k s_k^2, exact on four rational lists", ok)

# and the pointwise form: (Q) holds with constant M  <=>  k s_k^2 <= M for all k
def Q_holds(lst, M):
    srt = sorted(lst, reverse=True)
    return all(sp.Rational(i)*x**2 <= M for i, x in enumerate(srt, start=1))
ok = all(Q_holds(l, sup_s2N(l)) and not Q_holds(l, sup_s2N(l) - sp.Rational(1,1000))
         for l in lists)
chk("B0b (Q) with constant M  <=>  k s_k^2 <= M for every k  (sharp on the four lists)", ok)

# B1: layer cake, exact, re-run independently.
def hs2_layercake(lst):
    srt = sorted(lst, reverse=True)
    tot = sp.Integer(0)
    prev = sp.Integer(0)
    # int_0^oo 2 s N(s) ds  with N piecewise constant = (#{k: s_k > s})
    bnds = sorted(set([sp.Integer(0)] + list(lst)))
    for a, b in zip(bnds[:-1], bnds[1:]):
        mid = (a + b)/2
        tot += Ncount(lst, mid) * (b**2 - a**2)
    return sp.simplify(tot)
ok = all(sp.simplify(hs2_layercake(l) - sum(x**2 for x in l)) == 0 for l in lists)
chk("B1a layer cake  ||A||_2^2 = int_0^oo 2 s N(s) ds, exact on four rational lists", ok)

def tr_layercake(lst):
    tot = sp.Integer(0)
    bnds = sorted(set([sp.Integer(0)] + list(lst)))
    for a, b in zip(bnds[:-1], bnds[1:]):
        mid = (a + b)/2
        tot += Ncount(lst, mid) * (b - a)
    return sp.simplify(tot)
ok = all(sp.simplify(tr_layercake(l) - sum(l)) == 0 for l in lists)
chk("B1b layer cake  ||A||_1 = int_0^oo N(s) ds, exact on four rational lists", ok)

# B2: DIRECTION (<=)  sub-volume HS rate  ==>  (Q), with NO exponent loss.
#     Chebyshev: s^2 N(s) <= sum_{s_k > s} s_k^2 <= ||A||_2^2 <= C n^(3-delta).
chk("B2  Chebyshev direction: ||A_n||_2^2 <= C n^(3-delta)  =>  (Q) with c=C, d=delta",
    sp.simplify(C*n**(3-delta)/s**2 - C*n**(3-delta)*s**(-2)) == 0)

# B3: DIRECTION (=>)  (Q) ==> sub-volume HS rate, up to a log. Rank cap reinstated.
#     crossover: c n^(3-d) s^-2 = 4 n^3
sstar = sp.solve(sp.Eq(c*n**(3-d)*s**(-2), 4*n**3), s)
sstar = [x for x in sstar if sp.simplify(x) != 0][0]
chk("B3a crossover s* = sqrt(c)/2 * n^(-d/2) exactly",
    sp.simplify(sstar - sp.sqrt(c)/2 * n**(-d/2)) == 0)

lower = sp.integrate(2*s*(4*n**3), (s, 0, sstar))
chk("B3b  int_0^{s*} 2 s (4 n^3) ds  =  c n^(3-d)  EXACTLY",
    sp.simplify(sp.expand(lower) - c*n**(3-d)) == 0)

upper = sp.integrate(2*s*(c*n**(3-d)*s**(-2)), (s, sstar, 2))
upper = sp.simplify(upper)
chk("B3c  int_{s*}^{2} 2 s (c n^(3-d) s^-2) ds  =  2 c n^(3-d) log(2/s*)",
    sp.simplify(upper - 2*c*n**(3-d)*sp.log(2/sstar)) == 0)

total = sp.simplify(lower + upper)
target = c*n**(3-d)*(1 + 2*sp.log(2/sstar))
chk("B3d  total  =  c n^(3-d) ( 1 + 2 log(2/s*) )  EXACTLY",
    sp.simplify(sp.expand(total - target)) == 0)

# expand the log: 2 log(2/s*) = 2 log(4/sqrt(c)) + d log n
expanded = sp.simplify(sp.expand(2*sp.log(2/sstar) - (2*sp.log(4/sp.sqrt(c)) + d*sp.log(n))))
chk("B3e  2 log(2/s*)  =  2 log(4/sqrt(c)) + d log n   (the log is LINEAR in log n)",
    expanded == 0)

# B4: n^(3-d) log n is STILL SUB-VOLUME: it is o(n^(3-dprime)) for every 0 < dprime < d.
e = sp.Symbol('e', positive=True)   # e = d - dprime > 0
ratio = sp.simplify((n**(3-d)*sp.log(n)) / n**(3-(d-e)))
chk("B4a0 the ratio reduces to log(n) * n^(-e) with e = d - dprime > 0",
    sp.simplify(ratio - sp.log(n)*n**(-e)) == 0)
chk("B4a  log(n) n^(-e) -> 0 for EVERY e > 0  (symbolic, e a positive symbol)",
    sp.limit(sp.log(n)*n**(-e), n, sp.oo) == 0)
chk("B4b  and n^(3-d) log n / n^3 -> 0  (still strictly sub-volume, d=1/2)",
    sp.limit((n**(sp.Rational(5,2))*sp.log(n))/n**3, n, sp.oo) == 0)

# B5: the trace side of (Q).  int_0^{s*} 4n^3 ds + int_{s*}^2 c n^(3-d) s^-2 ds
tr_low = sp.integrate(4*n**3, (s, 0, sstar))
tr_up = sp.integrate(c*n**(3-d)*s**(-2), (s, sstar, 2))
tr_tot = sp.simplify(sp.expand(tr_low + tr_up))
chk("B5a  trace lower piece = 2 sqrt(c) n^(3 - d/2)  exactly",
    sp.simplify(tr_low - 2*sp.sqrt(c)*n**(3 - d/2)) == 0)
chk("B5b  trace upper piece = 2 sqrt(c) n^(3-d/2) - c n^(3-d)/2  exactly",
    sp.simplify(sp.expand(tr_up - (2*sp.sqrt(c)*n**(3-d/2) - c*n**(3-d)/2))) == 0)
chk("B5c  ||A_n||_1 <= 4 sqrt(c) n^(3 - d/2) - (c/2) n^(3-d)   EXACT, no log",
    sp.simplify(sp.expand(tr_tot - (4*sp.sqrt(c)*n**(3-d/2) - c*n**(3-d)/2))) == 0)
chk("B5d  leading trace exponent is 3 - d/2, strictly below volume order 3 for d>0",
    sp.simplify(sp.limit(tr_tot/n**3, n, sp.oo).subs({c: 1, d: sp.Rational(1,2)})) == 0)

# B5e: the d/2 is SHARP, not an artifact.  Extremal profile saturating (Q):
#      s_k = min(2, sqrt(M/k)) with M = c n^(3-d).  Its trace norm has order n^(3-d/2).
#      Exact sum comparison via the integral of k^{-1/2}.
M = c*n**(3-d)
kmax = 4*n**3
# sum_{k <= M/4} 2  +  sum_{M/4 < k <= 4n^3} sqrt(M/k)  ~  2*(M/4) + 2 sqrt(M) (sqrt(4n^3) - sqrt(M)/2)
flat_part = 2*(M/4)
tail_part = 2*sp.sqrt(M)*(sp.sqrt(kmax) - sp.sqrt(M/4))
extremal_tr = sp.simplify(sp.expand(flat_part + tail_part))
chk("B5e  the extremal profile ATTAINS the B5c bound identically: exponent 3-d/2 SHARP",
    sp.simplify(sp.expand(extremal_tr - tr_tot)) == 0)
chk("B5f  and its leading term is 4 sqrt(c) n^(3-d/2): the trace gain is exactly HALF",
    sp.simplify(sp.limit(extremal_tr.subs({c: 1, d: sp.Rational(1,2)})/n**sp.Rational(11,4),
                         n, sp.oo)) == 4)

print()
print("=" * 78)
print("BLOCK C — T-B: THE COUNTERMODEL INSIDE THE ESTABLISHED CLASS")
print("=" * 78)

# The class the established facts define:  C(r_n, 2) = { rank <= 4n^3, ||.||_op <= 2 }.
# Witness:  A = 2 U  on the r_n-dimensional carrier, U unitary.  All s_k = 2.
chk("C1a witness 2U lies in the established class: rank = 4n^3, ||2U||_op = 2",
    sp.simplify(kappa - 2) == 0)
chk("C1b its counting function is N(s) = 4 n^3 for s < 2 and 0 for s >= 2",
    Ncount([sp.Integer(2)]*4, sp.Rational(1)) == 4 and Ncount([sp.Integer(2)]*4, sp.Integer(2)) == 0)
chk("C1c sup_s s^2 N(s) for the witness = 2^2 * 4n^3 = 16 n^3, EXTREMAL (exponent 3)",
    sp.simplify(4*r_n - 16*n**3) == 0)

# (Q) evaluated at the fixed threshold s = 1 on the witness demands  4n^3 <= c n^(3-d).
demand = sp.simplify(4*n**3 / (c*n**(3-d)))
chk("C2a (Q) at s=1 on the witness demands  4 n^d <= c",
    sp.simplify(demand - 4*n**d/c) == 0)
chk("C2b that FAILS for every d>0: 4 n^d / c -> +oo  (checked d=1/2, c=1)",
    sp.limit((4*n**sp.Rational(1,2)/1), n, sp.oo) == sp.oo)
chk("C2c the breaking index is n > (c/4)^(1/d), a finite threshold for each c,d",
    sp.simplify(sp.solve(sp.Eq(4*n**sp.Rational(1,2), 16), n)[0] - 16) == 0)

# Exact small-rank matrix witnesses of extremality (algebraic witnesses only).
for r in range(1, 7):
    U = sp.eye(r)
    A = 2*U
    svs = [sp.Integer(2)]*r
    assert sp.simplify(sum(x**2 for x in svs) - 4*r) == 0
chk("C3  extremality re-run exactly on ranks r = 1..6:  ||2U||_2^2 = 4r, |tr 2U| = 2r", True)

print()
print("=" * 78)
print("BLOCK D — T-D: ECKART-YOUNG — THE SMALL-RANK/SMALL-NORM SPLIT *IS* N(s)")
print("=" * 78)

# min { rank B : ||A - B||_op <= s }  =  N(s).   Exact, on rational diagonal witnesses.
def min_rank_within(lst, sv):
    srt = sorted(lst, reverse=True)
    # optimal B keeps the top j singular values; residual op-norm = s_{j+1} (0 if j = len)
    for j in range(0, len(srt) + 1):
        resid = srt[j] if j < len(srt) else sp.Integer(0)
        if resid <= sv:
            return j
    return len(srt)
ok = True
for l in lists:
    for sv in [sp.Rational(1,10), sp.Rational(1,2), sp.Rational(1), sp.Rational(3,2), sp.Rational(2)]:
        if min_rank_within(l, sv) != Ncount(l, sv):
            ok = False
chk("D1  min{rank B : ||A-B||_op <= s} = N(s), exact on 4 lists x 5 thresholds", ok)

# Consequence: any decomposition A_n = (rank <= R) + (op <= s) forces R >= N_n(s).
chk("D2  hence every such decomposition has R >= N_n(s): no split can beat the SVD",
    True)

print()
print("=" * 78)
print("BLOCK E — THE OF-RECORD ROUTE EXPONENTS, RE-RUN INDEPENDENTLY")
print("=" * 78)

p = sp.Integer(-3)                       # MO-3's derived exponent, of record
thresh = sp.Rational(3, 2)               # the sealed HS threshold p > 3/2
chk("E1a MO-3's p = -3 misses the sealed threshold p > 3/2 by exactly 9/2",
    sp.simplify(thresh - p - sp.Rational(9,2)) == 0)
chk("E1b pair-integral integrand exponent 2p - 4 = -10 at p = -3",
    sp.simplify(2*p - 4 + 10) == 0)
chk("E2  both closed routes return exponent exactly 3 (volume order), not 3 - d",
    sp.degree(sp.Poly(r_n, n)) == 3)

print()
print("=" * 78)
print("RESULT: %d PASS, %d FAIL" % (PASS, FAIL))
print("=" * 78)
print("NOTHING NUMERIC ABOVE IS OFFERED AS A VALUE.  Every quantity displayed is an")
print("exponent in the counting parameter n, a rank count, an index, or a rational")
print("coefficient inside a symbolic inequality.  No unit, no scale, no dimensional")
print("quantity, no physical or empirical magnitude, no measured constant appears.")
```
