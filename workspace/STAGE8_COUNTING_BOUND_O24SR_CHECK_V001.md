# CHECK OF STAGE 8 — SINGULAR-VALUE COUNTING BOUND — COMMISSION O24SR-CHECK — V001

## O24SR-CHECK, 2026-08-15 — HOSTILE RE-DERIVATION. AUTHOR'S WORD CARRIES NO WEIGHT.

```text
THIS ARTIFACT DECLARES NOTHING, ADOPTS NOTHING, LANDS NOTHING.  No gate moves, no
witness created or retired, no failure point discharged.  RATE_CERTIFIED = false is
untouched.  It checks one artifact and reports where it holds and where it does not.
```

**OVERALL VERDICT: CONFIRMED WITH CORRECTIONS.**

Every load-bearing conclusion of the target survives independent re-derivation.
Two claims are overstated at the level of their supporting text — one factual
(§2.3's completeness assertion is FALSE at bytes), one verbal (T-A4's word
"identically" is FALSE as literally stated). Neither overturns the conclusion it
supports. A third correction concerns the evidentiary weight of the CAS battery.

**SWEEP CUTOFF: 2026-08-15T23:40:00Z.** Every exhaustiveness sentence below is
relative to this cutoff and to its own displayed key set. Nothing absolute is
claimed.

**OUTPUT-PATH PROBE:** this output path and its `.seal.sha256` sidecar were both
probed **ABSENT** before any write (`ls` exit 1 on both).

---

## §1 — SEALS, INDEPENDENTLY VERIFIED

`shasum -a 256 -c` run from inside the artifact's own directory, before any
reliance. **4/4 OK, zero mismatches.**

```text
  STAGE8_COUNTING_BOUND_O24SR_V001.md            OK   (the target)
  STAGE8_W1_SUBVOLUME_RATE_O5SR_V001.md          OK
  STAGE8_W1_SUBVOLUME_RATE_O5SR_AUDIT_V001.md    OK
  STAGE8_MO3_P_EXPONENT_S9AD_V001.md             OK
```

Two further files were opened as citation closure of the three named sources
(un-sealed reads, used only to test §2.3's completeness claim, which is precisely
what the commission demands):

```text
  STAGE8_WALL_BOUNDARY_CLOSURE_S9AD_V001.md      (80db260f — cited by W-1 :111, :156, :302)
  STAGE8_W3_GCM_HS_TYPE_O3SR_V001.md             (241262ff — cited by W-1 :105, §5.1)
```

**DECLARED SCOPED SWEEP.** Keys: `self-adjoint`, `selfadjoint`, `hermit`,
`symmetric`, `positive`, `semidefinite`, `projection`, `idempotent`, `normal`,
`commut`, `trace-class`, `traceless`, `nilpotent`, `unitar`, `isometr`,
`invertib`, `kernel`, `compact`, `spectrum`, `eigenvalue`, `compress`,
`sandwich`, `C_n`, `K_H`, `H_A`, `dressed composite`, `A_n`, `lower bound`,
`diverge`, `+infinity`, `>=`, over the four sealed files plus the two cited
files above. Exhaustiveness claimed at this key set only.

---

## §2 — CLAIM ONE: EQUIVALENCE TO THE HS RATE AT THE SAME CRITICAL EXPONENT

**VERDICT: CONFIRMED.** Both directions re-derived from scratch, not re-run from
the target's script.

### §2.1 T-A0 — the restatement on the singular-value sequence

`sup_{s>0} s^2 N(s) = max_k k s_k^2` re-proved and re-tested independently on 40
random rational singular-value lists by a threshold-grid evaluation that shares no
code with the target's. **HOLDS.** So (Q) `<=>` `k s_k^2 <= c n^(3-d)` for all `k`.

### §2.2 The easy direction (T-A1)

`s^2 N_n(s) <= sum_{k : s_k > s} s_k^2 <= ||A_n||_2^2`. Each of the `N_n(s)` terms
in the middle sum has `s_k^2 > s^2`. No exponent loss. **CONFIRMED.**

### §2.3 The delicate direction (T-A2) — truncation point, log factor, exponent

Re-derived independently in a fresh venv. All three commissioned sub-checks pass.

```text
TRUNCATION POINT.   c n^(3-d) s^-2 = 4 n^3   =>   s^2 = (c/4) n^(-d)
                    =>  s* = (sqrt(c)/2) n^(-d/2).            CORRECT as displayed.
LOWER PIECE.   int_0^{s*} 2 s (4 n^3) ds = 4 n^3 (s*)^2 = c n^(3-d).   EXACT.
UPPER PIECE.   int_{s*}^{2} 2 s (c n^(3-d) s^-2) ds = 2 c n^(3-d) log(2/s*)
               = c n^(3-d) ( 2 log(4/sqrt(c)) + (d) log n ).            EXACT.
LOG FACTOR.    log(2/s*) = log(4/sqrt(c)) + (d/2) log n.  So the surviving factor
               is LINEAR in log n with coefficient exactly c*d on n^(3-d) log n.
               CORRECT as displayed.
EXPONENT.      n^(3-d) log n / n^(3-d') = log(n) n^(-(d-d')) -> 0 for every d' < d.
               So delta* >= d.  And n^(3-d) log n / n^(3-d) = log n -> +oo, so the
               exponent d ITSELF is NOT delivered by this route — exactly as the
               target states ("any delta' < d").  NOT SHIFTED, NOT SILENTLY
               PRESERVED: honestly reported as an epsilon-loss at fixed exponent
               and an exact equality at the critical exponent.
CRITICAL EXP.  T-A1 gives d* >= delta*; T-A2 gives delta* >= d - eps for all eps,
               hence delta* >= d*.  So delta* = d*.  CONFIRMED.
```

The truncation is legitimate: on `(0, s*)` the power-law bound EXCEEDS the rank cap
and is vacuous there, so replacing it by `4n^3` is a genuine strengthening of the
integrand bound, not an assumption. The `q = 2` divergence of W-1's T-2d lives
entirely on `(0, s*)` and is what the cap removes. **CONFIRMED.**

> **CHECK CORRECTION C-1 [MINOR, UNDECLARED HYPOTHESIS].** T-A2's split presumes
> `s* <= 2`, i.e. `c <= 16 n^d`. For `c > 16 n^d` (finitely many `n` for each
> admissible `(c,d)`) the crossover lies above the domain and the displayed split
> is ill-posed. Harmless — finitely many `n` are absorbed into the constant `C'`,
> and the `O(.)` statements T-A3 quantifies over are asymptotic — but the
> hypothesis is nowhere declared. Direction of effect: none on any conclusion.

### §2.4 The target's own O-1 (Chebyshev from the sealed budget is vacuous)

`16 n^3/s^2 - 4 n^3 = 4n^3(4-s^2)/s^2 > 0` on `(0,2)`, `= 0` at `s = 2`. Re-derived.
**CONFIRMED.** The established budgets contribute nothing beyond (F1)+(F2), and the
best (Q)-shaped bound they yield has `d = 0`.

---

## §3 — CLAIM TWO: NO PROOF IS POSSIBLE, ON A LIST SAID TO BE COMPLETE

**VERDICT: CONFIRMED WITH CORRECTIONS.** The conclusion stands. The stated ground
for it — §2.3's "exactly **two** facts ... Nothing else about `A_n` is available at
any grade" — is **FALSE AT BYTES**.

### §3.1 The completeness claim is refuted

The commission's own instruction is that one additional established fact the
witness violates destroys the claim. Three further established facts were found —
inside the citation closure the target itself opens, at the SAME bytes its (F2) is
sourced from.

```text
(F3)  SELF-ADJOINTNESS.  Both dressed composites are self-adjoint BY CONSTRUCTION:
      80db260f :288-289, verbatim — "K_H = (K+K^dag)/2, H_A = -i(K-K^dag)/2".
      These are the self-adjoint and (i-rotated) anti-self-adjoint parts of K_n.
      This is the very bracket from which the target's (F2) enclosure is read
      (80db260f :287, the line W-1 :156 carries).  The target quotes the
      CONSEQUENCE from those bytes and drops the STRUCTURE displayed beside it.
(F4)  THE PAIR IS ONE OPERATOR.  From the same bytes, K_n = K_{H,n} + i H_{A,n}.
      The two composites are not independent members of a class; they are the real
      and imaginary parts of a single K_n with ||K_n||_op <= 2 (80db260f :286-287).
      This is a JOINT constraint on the pair, which the target's class C(r_n,2)
      does not express.
(F5)  SUPPORT / COMPRESSION.  K_n = -i C(U S_- - S_+ U) C (80db260f :188, KD2 of
      record), so A_n = C_n A_n C_n, supported on ran C_n, with C^2 = C and
      ||C_n|| <= 1.  The target uses only the rank CONSEQUENCE of this (its F1) and
      never the structure.  (Audit :165-166 and :862-863 re-source the same bytes.)
```

So the sentence "exactly **two** facts about `A_n` are established. Nothing else
about `A_n` is available at any grade" (target :130-131) is refuted. The load
placed on it at :154-156 ("This is the single most load-bearing fact in this
artifact") is therefore misplaced.

### §3.2 But the witness survives all three — the conclusion stands

The target's witness is `B_n := 2 U_n` for **ANY** unitary `U_n`. That family is
strictly larger than the record admits: a general unitary is not self-adjoint, and
a free choice per `n` disregards (F4) and (F5). The witness as stated is
over-general. It is repairable, and the repair is explicit:

> **CHECK-REPAIRED WITNESS W\*.** Put `K_n := sqrt(2)(1 + i) C_n`. Then
> `||K_n||_op = |sqrt(2)(1+i)| * ||C_n||_op = 2 * 1 = 2`, satisfying (F2) and (F4).
> Its parts are `K_{H,n} = H_{A,n} = sqrt(2) C_n`. Each is:
> **self-adjoint** (F3, since `C_n` is a projection); **supported on ran C_n** with
> `C_n A_n C_n = A_n` (F5); of **rank exactly 4n^3** (F1); of **operator norm
> sqrt(2) <= 2** (F2). Every singular value equals `sqrt(2)`, so
> `N_n(s) = 4 n^3` for `s < sqrt(2)` and `0` above.
> At the fixed threshold `s = 1`: `4 n^3 <= c n^(3-d)` demands `4 n^d <= c`, which
> fails for every `c` and every `d > 0` at all `n > (c/4)^(1/d)`.
> **W\* satisfies (F1), (F2), (F3), (F4) AND (F5), and violates (Q) for every
> `c` and every `d > 0`.**

Independently verified symbolically (self-adjointness, rank, flat singular-value
profile) and the breaking index re-derived with `d` a free positive symbol, not a
single instance. The target's own `2U_n` also survives (F3)-(F5) under the
specialization `U_n = I`, giving `2 C_n`; the general-unitary phrasing is what is
unsupported, not the countermodel.

> **CHECK FINDING F-1 [CORRECTION, does not overturn].** §2.3's completeness claim
> is FALSE: (F3) self-adjointness, (F4) the `K_n = K_H + i H_A` pairing, and (F5)
> the `C_n`-compression support are established at `80db260f` :188, :286-289, the
> same locus the target's own (F2) is read from. Direction of effect: it makes the
> non-implication argument REST ON A FALSE PREMISE AS STATED. **The conclusion is
> nevertheless CONFIRMED**, because a witness satisfying all five facts exists and
> is exhibited above. Required corrections: §2.3's "exactly two / nothing else at
> any grade" must be struck or restated as "exactly two facts BEARING ON THE
> SINGULAR-VALUE PROFILE"; §4's "Let `U_n` be any unitary" must be specialized;
> §7's "(F1) and (F2) — the complete list of established facts about `A_n`" must be
> corrected. T-B's status as a non-implication with a witness is unaffected.

### §3.3 Nothing further was found that the repaired witness violates

Swept for any established statement constraining the singular values, spectrum,
decay, symmetry, or support of `K_{H,n}` / `H_{A,n}` beyond (F1)-(F5). None found
at the cutoff. Two near-misses tested and rejected:

```text
  W-3's fixed-n enclosures  ||C_n T_g C_n||_2 <= 12 n^{3/2} sqrt(2n-1)/ell (order
    n^2) and ||.||_1 <= 24 n^3 sqrt(2n-1)/ell (order n^{7/2}) — audit :534-535.
    NOT a fact about A_n: T_g is a surrogate, not a dressed composite (audit :921,
    "NO surrogate composite class is introduced"); and squared, the first is order
    n^4 > n^3 — ABOVE volume order.  Not a sub-volume asset.  Correctly excluded.
  "definite-signed real quantities tr K_H, tr H_A, ||K_H||_2^2, ||H_A||_2^2"
    (80db260f :189) — a TYPE declaration on the four tasked quantities, not a
    proved sign or bound.  W* has tr = sqrt(2)*4n^3 > 0 in any case.
```

### §3.4 T-D (Eckart–Young–Schmidt), checked separately

`min{ rank B : ||A_n - B||_op <= s } = N_n(s)` — proof re-read line by line. The
`>=` direction uses `||A - B||_op >= s_{R+1}(A)` for `rank B = R`; the `<=`
direction is the truncated SVD. Both correct. **CONFIRMED.** The consequence — that
no small-rank/small-norm splitting can outperform the SVD, so the manoeuvre is a
restatement of (Q) and not a route to it — follows. **CONFIRMED.**

---

## §4 — CLAIM THREE: NO REFUTATION IS POSSIBLE EITHER

**VERDICT: CONFIRMED.**

The named quantities are genuinely undecided at their own sources, verified at
three independent loci, not one:

```text
  W-1 :653-656   "no divergence of tr K_H, tr H_A, ||K_H||_2^2, or ||H_A||_2^2 is
                 exhibited; no sealed +infinity attaches to any of the four
                 quantities; all four remain UNDECIDED".      VERIFIED VERBATIM.
  80db260f :437-438  same four quantities, same clause, at the ORIGIN artifact —
                 not merely carried by W-1.                   VERIFIED VERBATIM.
  241262ff :714-715  W-3's own one-sidedness clause, same four quantities.
                                                              VERIFIED VERBATIM.
```

So the target's reliance is not a single-link quotation chain; it is triple-sourced.

**HUNT FOR A MISSED LOWER BOUND — the most likely place to find one was MO-3, and
it is not there.** MO-3 derives `p = -3`: the unsandwiched difference kernel
DIVERGES at coincidence at degree `-3` with a contact term (:33-34, :385-388), and
the per-cell pair-integral diverges at rate `eps^-9` (:376, :739). A divergence is
the right SHAPE for a lower bound, so this was tested directly. It is not one:

```text
  (a) The object is Delta_n(a), the sandwiched MO-3 surrogate, not K_{H,n}/H_{A,n}
      (audit :921 names it as the surrogate).
  (b) It is a KERNEL-level statement at coincidence, and MO-3 states flatly at :475
      "Nothing diverges on a fixed carrier" — the finite-rank compression by C_n
      regularizes it.  A divergent kernel gives no lower bound on the singular
      values of its finite-rank compression.
  (c) MO-3's own verdict is that it CLOSES a route to PROVING the rate ("The F1
      escape closes NEGATIVELY", :390-393), which is a negative on the proof side,
      not a positive on the refutation side.
```

The target's characterisation of MO-3 at §5.1 — "a non-vanishing statement about a
difference kernel, not a lower bound on `N_n` at any threshold" — is accurate.
Route (ii)'s density floor is verified as attaching to the class supremum, with
W-1 §5.3 :375-383 stating in terms that it "does NOT establish that the dressed
composites themselves have a nonzero translation-invariant limit" and that the
premise "is NOT sealed, is not authored here, and is not assumed". **CONFIRMED.**
`p = -3` misses `p > 3/2` by `9/2`; integrand exponent `2p - 4 = -10`. Re-derived.

One tightening, not a correction: the target should say Route (ii)'s and MO-3's
object is the SANDWICHED SURROGATE, which is what makes (a) above decisive.

---

## §5 — CLAIM FOUR: ONE EXPONENT SETTLES IT, TWO-SIDED

**VERDICT: CONFIRMED WITH CORRECTIONS.** The exponent settles it in ONE direction
outright. The other direction is, by the target's own parenthetical, a restatement.

```text
(D-refute).  theta(s_*) = 3 at ONE fixed s_* in (0,2)  =>  for every eps>0,
   N_n(s_*) >= n^(3-eps) along a subsequence, so s_*^2 N_n(s_*) >= s_*^2 n^(3-eps).
   Choosing eps < d contradicts (Q) for large n.  GENUINELY DECISIVE from a single
   scalar.  CONFIRMED.  The positive-density corollary N_n(s_*) >= c_* n^3 likewise.
(D-prove).   theta(s_*) <= 3-d at one fixed s_* does NOT prove (Q).  It gives no
   uniformity in s_* and no rate.  The target's own text supplies the hypothesis it
   actually needs — "uniformly in s_* in (0,2), with the implied constant depending
   on s_* only through s_*^(-2)" — and then concedes in the same breath "that is,
   exactly (Q)".  So the prove side is not a single scalar and is not an additional
   fact; it is (Q) itself.
```

> **CHECK CORRECTION C-2 [OVERSTATEMENT].** The headline "THE DECIDING FACT (one
> scalar, two-sided)" (:447) and §0's "`= 3` refutes (Q) outright, `< 3` with a rate
> proves it" (:67) are **asymmetric in fact and symmetric in presentation**. One
> scalar refutes; nothing less than the full uniform family proves. The correct
> statement is: `theta` is a **one-sided decider** — decisive against (Q), and on
> the affirmative side a re-labelling of (Q). The target discloses this in its own
> fine print but not in its headline or its §7 summary. Direction of effect: it
> makes §6 look like a new object when the affirmative half is not one.

**NEITHER NAMED ROUTE SMUGGLES IN SOMETHING ALREADY KNOWN. CONFIRMED.**
The refute route's premise (a nonzero translation-invariant / positive-density
limit at the DRESSED layer) is verified NOT sealed and explicitly not assumed at
W-1 :375-383 — so it is a genuine gap, not a known fact re-badged. The prove
route's requirement (`s_k(A_n) <= (c n^(3-d)/k)^(1/2)`) is, by T-A0, literally (Q)
— the target says so ("equivalently, by T-A0"), so nothing is smuggled, but nothing
is added either. Both are correctly flagged "pointers, not claims".

The caution at :485-490 — that the deciding fact must NOT be stated as a `q < 2`
counting bound, since audit finding A-1 refuted that demand — is **CONFIRMED**
against the audit's own bytes (:211-221).

---

## §6 — CLAIM FIVE: THE TRACE BUDGET AT A HALVED EXPONENT, SAID TO BE SHARP

**VERDICT: CONFIRMED WITH CORRECTIONS.** The halving is right and the exponent is
genuinely sharp. The word "identically" is FALSE, and the CAS check that certifies
it is circular.

### §6.1 The halving — CONFIRMED

Re-derived independently:

```text
  int_0^{s*} 4 n^3 ds            =  4 n^3 * (sqrt(c)/2) n^(-d/2)
                                 =  2 sqrt(c) n^(3 - d/2)                  EXACT
  int_{s*}^{2} c n^(3-d) s^-2 ds =  c n^(3-d) (1/s* - 1/2)
                                 =  2 sqrt(c) n^(3-d/2) - (c/2) n^(3-d)    EXACT
  ||A_n||_1  <=  4 sqrt(c) n^(3 - d/2)  -  (c/2) n^(3-d).   No logarithm.  EXACT
```

Leading exponent `3 - d/2`: the HS gain `d` is halved. The mechanism is transparent
and correct — `||A||_1 = int N(s) ds` has one fewer power of `s` in the integrand
than `||A||_2^2 = int 2s N(s) ds`, so the `s*`-truncated mass scales as `s*` rather
than `(s*)^2`, and `s* ~ n^(-d/2)`. **CONFIRMED, including the absence of a log.**

### §6.2 The sharpness — the extremal example ATTAINS the bound ASYMPTOTICALLY, NOT IDENTICALLY

The extremal profile is `s_k = min(2, sqrt(M/k))`, `M = c n^(3-d)`, `k = 1..4n^3`.
First checked that it is admissible: `k s_k^2 = min(4k, M) <= M`, so
`sup_k k s_k^2 = M` exactly — it does saturate (Q) with constant `M`, and by T-A0
it is the largest profile (Q) permits. **That part CONFIRMED.**

Its trace norm is a **DISCRETE SUM**, `sum_{k=1}^{4n^3} min(2, sqrt(M/k))`. The
target's CAS check B5e does not compute that sum. It computes
`2*(M/4) + 2 sqrt(M)(sqrt(4n^3) - sqrt(M/4))`, which is the CONTINUUM INTEGRAL
`int_0^{M/4} 2 dk + int_{M/4}^{4n^3} sqrt(M/k) dk` — the same integral as the
bound, written in the `k` variable instead of the `s` variable. **B5e is a change
of variables, so it passes by construction and certifies nothing.**

The discrete sum was therefore computed directly here, over the full index range
`k = 1..4n^3`, at three `(c,d)` pairs and five values of `n`:

```text
  c=1  d=1/2  n=8    discrete 1126.386812   bound 1127.238418   diff -0.851606
  c=1  d=1/2  n=32   discrete 52211.783219  bound 52212.678094  diff -0.894876
  c=1  d=1/2  n=128  discrete 2401265.2539  bound 2401266.1796  diff -0.925673
  c=4  d=1    n=128  discrete 1450141.4446  bound 1450142.4004  diff -0.955801
  c=1  d=2    n=128  discrete 65471.004557  bound 65472.000000  diff -0.995443
```

The discrete extremal trace is STRICTLY BELOW the bound at every point tested, by
an O(1) deficit. So "**has trace norm identically equal to the bound just
displayed**" (:298) is FALSE as written.

It is nevertheless asymptotically sharp, and that is what the claim needs: the
ratio is `0.99924, 0.99989, 0.99998, 0.99999, 0.999999...` — monotonically to `1`.
The O(1) gap is the standard sum-vs-integral defect (`f` decreasing gives
`int <= sum <= int + f(a)`, with `f(a) = 2` here), while the leading term
`4 sqrt(c) n^(3-d/2)` diverges. So both the exponent `3 - d/2` AND its leading
coefficient `4 sqrt(c)` are genuinely attained.

> **CHECK FINDING F-2 [CORRECTION, does not overturn].** T-A4's "identically equal"
> is false; the correct word is **asymptotically attained (ratio -> 1)**, and the
> exponent `3 - d/2` is **SHARP**, which is the claim that matters. CAS B5e must be
> struck as evidence — it re-computes the bound rather than the profile — and
> replaced by a discrete evaluation. Direction of effect: weakens the EVIDENCE for
> a claim that is nonetheless TRUE. The halving stands, the sharpness stands.

### §6.3 The re-derivation of audit finding A-1 — CONFIRMED

The audit's A-1 (:211-221) is: `q = 2` plus the sealed rank cap IS sufficient for a
sub-volume rate at `3 - delta'` for every `delta' < delta`; hence W-1's "must
deliver `q` strictly below 2" is not derived. The target's T-A2 is an independent
re-derivation of exactly this, and its T-A0/T-A3 extension (the restatement on the
singular-value sequence and the equality of critical exponents) is genuinely
additional at the cutoff. Attribution at :276-279 is accurate — the target does not
claim A-1 as new. **CONFIRMED.**

---

## §7 — SYMBOLIC RE-RUN, AND THE FENCES

### §7.1 Fresh-venv reproduction — EXACT

```text
  Fresh venv created for this check; sympy 1.14.0.
  Script extracted from the target's §8.2 by file-slice.
  sha256 = 232693e9591b72e43957858d6a723fc256516cdf48e0099523800ef22e8d31f7
  MATCHES the hash declared at :559-560.
  Single run: 36 PASS, 0 FAIL.  Verbatim output byte-IDENTICAL to §8.1.
```

An independent battery, sharing no code with the target's, re-derived T-A0, the
T-A2 truncation/log/exponent chain, the T-A4 trace bound, the discrete extremal
trace, and the witness (as an actual matrix SVD, and with `d` a free positive
symbol). All independent checks agree with the target except where F-2 records.

### §7.2 The evidentiary weight of the target's battery

The target's own consumed audit raised finding A-6 against W-1 for exactly this:
"31 of the 34 checks bear their labels; 3 do not ... the signature of a check
written around a conclusion rather than toward one." **The target reproduces that
defect at greater scale and does not disclose it.**

```text
  A2   label claims the BEST (Q)-shaped bound has exponent 3-0; checks degree(16n^3)=3.
  B2   label claims the Chebyshev IMPLICATION; checks C n^(3-d)/s^2 - C n^(3-d) s^-2 = 0,
       a trivial rewrite of division as a negative power.  Checks nothing of the claim.
  B5e  circular — recomputes the bound in the k variable.  See F-2.
  C1a  label claims "witness 2U lies in the established class: rank = 4n^3, ||2U||_op = 2";
       checks kappa - 2 == 0, i.e. 2 - 2 = 0.  Checks nothing about the witness.
  C3   creates U = eye(r) and A = 2*U and USES NEITHER; the assert runs on a
       hand-written list.  |tr 2U| = 2r, in the label, is never evaluated.  This is
       verbatim the A-6 defect, in the same block letter.
  D2   chk(label, True) — a hardcoded constant.
  E2   label claims BOTH closed routes return exponent 3; checks degree(4n^3)=3.
       One return checked once, presented as two — verbatim audit A-6's D4 defect.
  (C2b, C2c self-disclose that they test one instance of a universal claim.)
```

> **CHECK FINDING F-3 [CORRECTION, evidentiary].** "36/36 PASS" is arithmetically
> honest and fully reproducible byte-for-byte, but **at least 7 of the 36 checks do
> not bear their labels**, and one of them (B5e) certifies a statement that is false
> as written. The correction is to the WEIGHT of the battery, not to any result this
> check otherwise confirms — every load-bearing claim was re-derived here
> independently and holds. The target consumed the audit that raised A-6 and repeats
> it without acknowledgement, including in the same block letter (C3).

### §7.3 The declared fences — HELD

```text
  No numerical value of any physical or empirical quantity anywhere.  VERIFIED by
    keyed sweep (hbar, fine-structure, 1/137, GeV/MeV/eV, kg, metre, second, Planck,
    coupling constant, measured, experiment, observ, CODATA, alpha_s, kappa_record,
    g-2, Newton) over the full target including the appendix.  ZERO hits.
  No comparison to a measured constant.  VERIFIED: zero hits.
  Decimal-token census over the whole file returns ONLY section numbers (2.1 ... 8.2)
    and the sympy version 1.14.  Every other number is an exponent in n, a rank
    count, an index, or a rational coefficient inside a symbolic inequality.
  Fresh venv, exact symbolic, single run.  VERIFIED.
  Output-path probe before write.  Consistent (path was still absent at this check).
  No register / tracker / road / plan / continuation / ledger / lens file opened by
    this check.  No git action.  No gate, fence, or v-clause touched.
```

---

## §8 — VERDICT PER CLAIM

```text
  ONE   Equivalence to the HS rate at the same critical exponent, both
        directions, truncation point, log factor, exponent preservation.
                                                          CONFIRMED  (+ minor C-1)
  TWO   No proof possible, on a COMPLETE list of established facts.
                                       CONFIRMED WITH CORRECTIONS  (F-1: the list
        is NOT complete — (F3) self-adjointness, (F4) the K_n = K_H + i H_A
        pairing, (F5) the C_n-compression support are established at 80db260f
        :188, :286-289.  The CONCLUSION survives: witness W* = sqrt(2) C_n
        satisfies all five facts and violates (Q) for every c and every d > 0.)
  THREE No refutation possible; the named quantities genuinely undecided.
        CONFIRMED.  Triple-sourced at W-1 :653-656, 80db260f :437-438, 241262ff
        :714-715.  Independent hunt for a lower bound — including MO-3's degree
        -3 coincidence divergence and eps^-9 pair integral — found none.
  FOUR  One exponent settles it, one route each way.
                                       CONFIRMED WITH CORRECTIONS  (C-2: theta is
        a ONE-SIDED decider.  It refutes from a single scalar; the affirmative
        half is, by the target's own words, exactly (Q).  Neither named route
        smuggles in anything known.)
  FIVE  Trace budget at a halved exponent, said to be sharp; A-1 re-derived.
                                       CONFIRMED WITH CORRECTIONS  (F-2: halving
        and sharpness both TRUE; "identically equal" is FALSE — the discrete
        extremal trace is strictly below the bound by an O(1) deficit, ratio -> 1.
        CAS B5e is circular and must be struck as evidence.  A-1 re-derivation
        CONFIRMED and correctly attributed.)
  ALSO  Fresh-venv symbolic re-run: EXACT, byte-identical, 36/36.  But F-3: at
        least 7 of 36 checks do not bear their labels — the target's own consumed
        audit raised this defect (A-6) against W-1 and it is repeated undisclosed.
        Numeric/empirical fences: HELD, zero hits.

  OVERALL:  CONFIRMED WITH CORRECTIONS.
```

**WHAT MOVED: nothing.** No gate, no fence, no v-clause, no witness. FP-1 stands.
`RATE_CERTIFIED = false` stands. The target's OUTCOME 3 — (Q) neither follows nor
fails on what is established, and is equivalent to the open problem — **survives
this check in full**. Three corrections are owed to its supporting text: the
completeness assertion at §2.3 and the witness's over-general phrasing at §4 (F-1),
the word "identically" and its circular CAS check at §3.4/T-A4 (F-2), and the
evidentiary weight of the battery (F-3), plus two overstatement notes (C-1, C-2).
Offered for the registrar's judgment only, as a check and not as a declaration.
