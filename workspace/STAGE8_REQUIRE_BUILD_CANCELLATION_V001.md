# STAGE 8 — REQUIRE-BUILD-CANCELLATION: DOES THE LEADING DEGREE -3 SINGULARITY CANCEL BY AN EXACT CONNECTION-ONLY SYMMETRY?

## BLIND BUILDER — REQUIRE-BUILD-CANCELLATION — [CLAIMED]

Date: 2026-08-13
Role: BLIND BUILDER. DETERMINE ONE structural fact — a clean BINARY. In the connected-
covariance DIFFERENCE that certifies the Gate-5 kernel `C`, the object
`X_n = C_n (V_n(a) - V_n(0)) C_n` whose finiteness is "purchased ENTIRELY by cancellation
in the difference" (ECO :176-179): does the LEADING degree -3 singularity of the sea
covariance cancel by an EXACT connection-only SYMMETRY (Ward / gauge-invariance /
charge-conjugation / current-conservation `d ell_j = 0` / antisymmetry of the imaginary
degree -3 part)? This is a yes/no ALGEBRAIC fact about whether a cancellation SYMMETRY
exists — NOT an evaluation of any residual's number.

Gates: `alpha_computed = false` ; `proof_authorized = false` ;
`kappa_record_computed = false` ; `coupling_evaluation_authorized = false`

HARD FENCE held throughout: STRUCTURAL DETERMINATION, NOT A COMPUTATION. No value of `n`,
`kappa_record`, `alpha`, any exponent, coupling, norm, scale, length, or spectrum is
computed, bounded, estimated, evaluated, or compared. Symbolic only. The sealed degree -3
kernel FORM was read ONLY to analyze its cancellation symmetry (to decide CANCELS-or-NOT),
never to compute a value — a use the tasking explicitly permits. Connection-only where
possible; NO imported GR, NO faithfulness premise. No register/tracker/plan/road/ledger/
lens read. No git action.

---

## 0. VERDICT IN ONE LINE

**NO exact connection-only symmetry forces the leading degree -3 singularity to fully
cancel in the difference. The connection-only content fixes the a-dependence to enter
ONLY as an abelian unit-modulus holonomy character (a pure phase); hence `V_n(a)-V_n(0)`
is necessarily a PHASE-DIFFERENCE dressing of the singular baseline, which vanishes to
EXACTLY FIRST ORDER at the diagonal (via the write current `<ell_j, r>`) — a ONE-POWER
(PARTIAL) softening, degree -3 -> degree -2, not a removal to a bounded kernel. Full
cancellation would require the write current to vanish (the phase to be locally constant),
which contradicts the nonzero write forced by `n != 0`. The ONE candidate for an EXACT
cancellation — the antisymmetry (oddness) of the imaginary degree -3 part — is a genuine
exact symmetry, but it delivers cancellation ONLY in the operator-norm / L^2 sense (this
IS the sealed "Calderon-Zygmund kernel: L^2-BOUNDED BUT NOT HILBERT-SCHMIDT" property); it
is POWERLESS for the Hilbert-Schmidt / Schatten-2 object R-L2b actually requires, because
the HS integrand is `|kernel|^2`, which is EVEN and positive — parity gives nothing.
Therefore: CANCELLATION_SYMMETRY = PARTIAL; LEADING_DEGREE_3 = SURVIVES; NET =
DOES_NOT_FULLY_CANCEL -> alpha RUNS. The scale that then appears is the EMERGENT RG scale
(running `kappa_record`), not a re-import.**

---

## 1. SOURCES READ, SEALS VERIFIED AT PATH

All under `/Users/bgm/MB Work/alpha-program-archive/workspace/`. Full digests recomputed by
`shasum -a 256` at path BEFORE reading; CONN = connection-only, SCALE = scale-bearing (read
ONLY to analyze the kernel's cancellation symmetry, never as a value authority).

```text
TASKED (the wall + "cancellation in the difference"):
  STAGE8_REQUIRE_BUILD_CLUSTER_SUMMABILITY_V001.md
    5cdd5dafccd1dfd5075426cce384cb84136a21df1cecad56576da3799cea9455  MATCHES-TASKED  CONN
  STAGE8_REQUIRE_CLUSTER_CHECK_V001.md
    a7f75d0f2c4ed9604be78a9024461d93ff097c77fbf9b46e0207c4e7eea93c13  MATCHES-TASKED  CONN
  STAGE8_R_RECORD_L_FORM_FABLE_V001.md
    5e49d2093d4ee17b840cc096d5caf3a6edafda4e37abbd175a7a371c34658f37  MATCHES-TASKED  CONN

SEA-COVARIANCE / DIFFERENCE SOURCES (carry V_n(a)-V_n(0) and the degree -3 kernel):
  STAGE8_EXTENSIVITY_VERDICT_AND_RL2B_CAMPAIGN_OPENING_V001.md (ECO)
    0f3082cab910f2eb6769698fc03cdb0201830c2551ecd8201fa6748b24e07505  MATCHES (build-recorded)  SCALE
  STAGE8_RL2B_FRAME_ANSWER_AND_CAMPAIGN_TARGET_V001.md (RFA)
    2ede02aea415157ada9edd6f685aabcc824acf2716777f4aa2dc98467fe92840  MATCHES (build-recorded)  SCALE
```

Five seals recomputed at path; all match (three tasked digests exactly; ECO/RFA against
the digests the wall §1 records). The degree -3 kernel FORM and the difference structure
were read for STRUCTURE only. No register/tracker/plan/road/ledger/lens read.

---

## 2. THE OBJECT AND THE SEALED FACTS IT RESTS ON — QUOTED, NOT PARAPHRASED

**S1 — the object and the reduction to one yes/no (ECO :174-179; RFA :119-121).**
```text
ECO :174   "R-L2b asks for  || C (V(a) - V(0)) C ||_2  <=  |D|_4^alpha G_hs."
ECO :176-179  "THE FINITENESS OF R-L2b's OBJECT IS NOT A PROPERTY OF THE SUPPORT VOLUME
  AT ALL — IT IS PURCHASED ENTIRELY BY CANCELLATION IN THE DIFFERENCE. AND THEREFORE
  alpha IS SET BY THE CANCELLATION RATE, NOT BY |D|_4."
RFA :119-121  "DOES  V_(mu lambda)(a) - V_(mu lambda)(0)  HAVE A BOUNDED KERNEL ON A
  DIAMOND — I.E. DOES THE DEGREE -3 SINGULARITY OF C FULLY CANCEL IN THE DIFFERENCE?"
```
The corpus has itself reduced the whole extensivity/intensivity question to ONE analytic
yes/no: is the kernel of `V(a)-V(0)` bounded (equivalently, does the degree -3 fully
cancel) — FULLY -> alpha=1 (RFA :122-125, "aggregation FLAT ... CONNECTED EXTENSIVITY");
PARTIALLY -> alpha<1 (RFA :126-128, aggregate divergence `A^(3(1-alpha))`). And RFA
:137-138: "whether the singularity fully cancels is UNKNOWN." My task is to decide whether
an EXACT connection-only SYMMETRY settles that yes/no.

**S2 — the sealed leading singularity FORM (ECO :151-155), read to analyze its symmetry.**
```text
C(r) = (1/2) delta^3(r) I  -  i alpha·r / (2 pi^2 |r|^4)
   off-diagonal modulus EXACTLY 1/(2 pi^2 |r|^3); HOMOGENEOUS degree -3
   ||C_off(r)||_op = 1/(2 pi^2 |r|^3)
```
The leading (off-diagonal) singular term `C_off(r) = - i alpha r / (2 pi^2 |r|^4)` has, as
pure STRUCTURE (no value): (i) it is PURELY IMAGINARY (the explicit `i`); (ii) it is ODD
in `r` — proportional to `r` (equivalently `r-hat/|r|^3`), so `C_off(-r) = - C_off(r)`;
(iii) homogeneous degree -3.

**S3 — the CZ / norm fact, sealed (ECO :168-171), read to classify the symmetry's reach.**
```text
"|| 1_D C 1_D ||_2 = INFINITY, ON EVERY DIAMOND, AT EVERY SCALE. ... a Calderon-Zygmund
 kernel of degree -3 in three dimensions is L^2-BOUNDED BUT NOT HILBERT-SCHMIDT."
```
This is exactly the fingerprint of the odd-part antisymmetry (S2.ii): an odd/imaginary
CZ kernel defines a BOUNDED operator (its angular average / principal value cancels) yet
is NOT Hilbert-Schmidt. The exact cancellation the antisymmetry provides lives in the
OPERATOR-NORM sense, and R-L2b is a Hilbert-Schmidt (`||.||_2`) object.

**S4 — the CONNECTION-ONLY fact that fixes the difference's form (FORM B5, B6, D2, D3).**
```text
FORM B5   the connection enters the ratified object ONLY through the per-cell characters
          z_j^(n)[a_j] = chi_n(h_j[a_j]); "no other a-dependence exists anywhere in the law."
FORM B6   z_(±,j)^(n) = chi_n(h_j[a_±]) are "unit-modulus holonomy characters"; the write
          carries "exactly one character power"; the trivial character n = 0 has zero
          variation and is eliminated (nonzero write requires n != 0).
FORM D2   with h_j[a] = exp(i <ell_j, a>):  chi_n(identity) = 1, and
          d/ds z_j^(n)[s a]|_0 = i n <ell_j, a> z_j^(n)[0].
FORM D3   on the doubled tangents the write reads phi_j = <ell_j, a_Delta>, invariant under
          the licensed common-gauge moves — "abelian relative holonomy."
```
This is the decisive connection-only lever: the ONLY way `a` enters ANY ratified object is
as a UNIT-MODULUS ABELIAN PHASE. Consequently `V_n(a)` differs from `V_n(0)` by a phase
dressing, and `chi_n(identity) = 1` makes the phase trivial exactly at `a = 0` and exactly
on the diagonal (coincident points).

---

## 3. THE DETERMINATION — THE DIFFERENCE IS A PHASE-DIFFERENCE, AND WHAT THAT FORCES

### 3.1 The exact structural form of `V_n(a) - V_n(0)` [PROVABLE from S4]

Because `a` enters only through the abelian unit-modulus character (S4/B5), the a-dependent
operator acts on the two-point (kernel) structure by an abelian phase dressing: with
`Theta_a` the local write phase (`Theta_a(x) = n <ell(x), a>` from the per-cell holonomy),

```text
V_n(a)(x,y)  =  exp( i [ Theta_a(x) - Theta_a(y) ] ) · V_n(0)(x,y),
V_n(a)(x,y) - V_n(0)(x,y)  =  [ exp( i [ Theta_a(x) - Theta_a(y) ] ) - 1 ] · V_n(0)(x,y).
```

This is a pure phase-conjugation difference — the connection-only content permits nothing
else. Two exact structural consequences of the FORM (no value used):

- **Diagonal triviality (subtraction removes the coincident value).** At `x = y` (`r=0`)
  the phase difference `Theta_a(x)-Theta_a(y) -> 0`, so `[exp(...)-1] -> 0`. The subtraction
  at baseline `a=0` removes the a-INDEPENDENT bare kernel exactly, and forces the difference
  kernel to VANISH AT the diagonal. This is what "cancellation in the difference" IS,
  structurally: the a-independent leading term is common to `V(a)` and `V(0)` and drops.
- **Order of vanishing = ONE (the write current).** A phase difference vanishes to FIRST
  order: `exp(i[Theta_a(x)-Theta_a(y)]) - 1 = i[Theta_a(x)-Theta_a(y)] + O(2)`, and
  `Theta_a(x)-Theta_a(y) = <grad Theta_a, r> + O(|r|^2) = n <ell_a, r> + O(|r|^2)`. So the
  prefactor is `O(|r|)` — degree +1 — with leading coefficient the WRITE CURRENT `<ell, r>`.

### 3.2 What the one-power prefactor does to the degree -3 singularity [STRUCTURAL order-count]

Multiplying the leading degree -3 singularity by an `O(|r|)` (degree +1) prefactor yields a
degree -2 object at the diagonal:

```text
[ O(|r|) ] · [ degree -3 ]  =  degree -2.
```

This is a PARTIAL softening by EXACTLY ONE power. It is NOT a removal to a bounded (degree
0) kernel. Degree -2 in three dimensions is still not the bounded/HS regime (the corpus's
own accounting: the untamed degree -3 diverges as `eps^-3` (ECO :162-165); one power of
softening is the "short one power" the wall names at §3.4). No value is computed here — this
is the symbolic order of the product of two homogeneous factors whose degrees are sealed
(-3) and structural (+1, the phase-gradient). To reach FULL cancellation (bounded kernel)
the phase difference would have to vanish to THIRD order at the diagonal — i.e. the write
current `ell` and its next two derivatives would all have to vanish — i.e. the phase is
locally CONSTANT, i.e. the write is TRIVIAL. That contradicts the nonzero write forced by
`n != 0` (FORM B6/D3). **So no phase-structure symmetry forces full cancellation.**

### 3.3 The candidate EXACT symmetries, each tested — none forces full HS cancellation

```text
(A) UNIT-MODULUS-CHARACTER / GAUGE (phase) structure  ->  PARTIAL, not full.
    The abelian phase dressing (3.1) forces the difference to vanish to first order only;
    it delivers exactly ONE power (3.2). Full cancellation needs a vanishing write current,
    excluded by n != 0. NOT an exact full-cancellation symmetry.

(B) CURRENT CONSERVATION  d ell_j = 0  (closed write chain)  ->  no help to the order.
    Conservation makes the abelian holonomy gauge-invariant / well-defined (FORM D3) — a
    consistency symmetry. It makes the current DIVERGENCE-FREE, NOT ZERO. A divergence-free
    but nonzero ell still gives a first-order phase gradient <ell, r> != 0, hence the same
    one-power softening. Conservation does not raise the diagonal vanishing order. NOT a
    full-cancellation symmetry.

(C) CHARGE CONJUGATION  (n -> -n, complex conjugation)  ->  relates, does not cancel.
    V(0) is n-blind (chi_n(identity) = 1, FORM D2), so the difference at -n is the complex
    conjugate of the difference at +n; the first-order term i n <ell,r> C_off flips sign
    under n -> -n. This would cancel only if one AVERAGED over +/- n — but R-L2b is at a
    FIXED winding n, not a +/- n average, so no cancellation is available. (The sealed
    R(n) = R(-n) evenness, FORM 5.1 pt 4, is a property of the FULL quadratic response after
    the C-sandwich and squaring, NOT a cancellation of the fixed-n middle kernel.) NOT a
    full-cancellation symmetry for the object at hand.

(D) ANTISYMMETRY of the imaginary degree -3 part (C_off odd in r)  ->  EXACT, but wrong norm.
    C_off(r) = - i alpha r/(2 pi^2 |r|^4) is odd (S2). Oddness is a GENUINE exact symmetry
    and it DOES cancel the leading singularity — in the OPERATOR-NORM / L^2 sense: the
    angular average / principal value vanishes, which is precisely why the sealed kernel is
    "L^2-BOUNDED BUT NOT HILBERT-SCHMIDT" (S3, ECO :168-171). But R-L2b is a HILBERT-SCHMIDT
    (Schatten-2) object: ||X||_2^2 = int int |X(x,y)|^2 (RFA :66). The HS integrand is
    |C_off|^2 = alpha^2/(4 pi^4 |r|^6), which is EVEN and POSITIVE — parity/antisymmetry
    contributes NOTHING to it. So the one exact symmetry present cancels in the operator norm
    and is POWERLESS for the HS norm the object requires. NOT a full HS-cancellation symmetry.
```

Across all four offered mechanisms: the phase/gauge and conservation symmetries force only
one-power (partial) softening; charge conjugation relates `+/-n` without cancelling a
fixed-n object; the antisymmetry is exact but in the operator norm, not the HS norm. **No
connection-only symmetry forces the leading degree -3 singularity to fully cancel in the
Hilbert-Schmidt difference.**

### 3.4 Why this is a DETERMINATE binary and not a fence-undetermined

Deciding "does an EXACT symmetry force full cancellation?" required only: (i) the sealed
FORM of the a-dependence (abelian unit-modulus phase, FORM B5/B6/D2 — CONN); (ii) the sealed
FORM of the leading term (odd, imaginary, degree -3, ECO :151-155); (iii) the elementary
structural fact that a phase difference vanishes to first order at the diagonal (Taylor —
pure structure); (iv) the elementary fact that `|odd|^2` is even (parity — pure structure);
and (v) the sealed CZ classification that pins the antisymmetry's cancellation to the
operator norm (ECO :168-171). NONE of these is `kappa_record`'s value or a numeric kernel
evaluation. The fence-guard (STOP -> UNDETERMINED) triggers only if deciding the SYMMETRY
would need such a computation; it does not. So the binary is DECIDED, not fence-deferred.

What remains a COMPUTATION (not a symmetry) is whether the surviving degree -2 residual is
nonetheless rendered HS-finite by the OPERATOR COMPOSITION in the sandwich `C(...)C` — the
commutator route `|| [C,P] ||_2` the corpus opened (ECO :189-201, "ROUTE_NOT_LEMMA"). That
is an operator-algebra reorganization whose success is a metric computation on the kernel,
NOT an exact symmetry. Per the tasking's own mapping — "needing a scale/computation to see
the residual just means the residual survives (the RUNS horn); there is no third road" — this
computation-openness is the RUNS horn, not a fence-undetermined of the symmetry binary I was
asked to decide. I decline to evaluate it (that would cross the fence) and classify it
accordingly.

---

## 4. IMPORT / MACHINERY AUDIT (MINE)

```text
No value of n, kappa_record, alpha, any exponent, coupling, norm, length, scale, or spectrum
  computed, bounded, estimated, evaluated, or compared. The degrees used (-3 sealed; +1 the
  phase-gradient; -2 their product) are SYMBOLIC orders of homogeneous factors, used to
  locate the one-power deficit — not evaluations of the kernel's value.
The sealed degree -3 kernel FORM (ECO S2) was read ONLY to analyze its cancellation symmetry
  (odd/imaginary/degree -3 -> antisymmetry is operator-norm not HS), a use the tasking
  explicitly permits; never to compute a value.
No GR imported, no faithfulness premise, no scale used as authority. The connection-only
  bedrock (FORM B5/B6/D2/D3: a enters only as a unit-modulus abelian phase; nonzero write
  for n != 0) carries every positive step. ECO/RFA (SCALE) were read only to classify the
  singularity's symmetry and to name the HS-vs-operator-norm distinction — the fence itself.
No register/tracker/plan/road/ledger/lens read. Seals recomputed at path before reading.
  No git action; output name probed before write: ABSENT.
```

---

## 5. FLAG BLOCK

```text
DIFFERENCE_STRUCTURE = PHASE-DIFFERENCE DRESSING(the connection enters ONLY as an abelian
  unit-modulus holonomy character chi_n(h_j[a]) = exp(i n <ell_j,a>) — "no other a-dependence
  exists anywhere in the law" (FORM B5 :96-98, B6 :107-113, D2 :167-168, D3 :198-199). Hence
  V_n(a)(x,y) - V_n(0)(x,y) = [ exp(i[Theta_a(x)-Theta_a(y)]) - 1 ] · V_n(0)(x,y). WHAT
  SUBTRACTION REMOVES: the a-INDEPENDENT bare kernel, common to V(a) and V(0); it forces the
  difference to VANISH AT the diagonal (chi_n(identity)=1, phase -> 1 at r=0) — this IS the
  "cancellation in the difference" (ECO :176-179; RFA :119-121). But it vanishes to EXACTLY
  FIRST ORDER: [exp(i Delta)-1] = i Delta + O(2), Delta = <grad Theta_a, r> + O(|r|^2) =
  n<ell,r>+O(|r|^2), an O(|r|) prefactor whose leading coefficient is the write current.
  Span: ECO :174-179; RFA :66, :119-131; FORM B5/B6/D2/D3.)

CANCELLATION_SYMMETRY = PARTIAL(the abelian unit-modulus-character/gauge structure forces the
  difference to vanish to first order only -> a ONE-POWER softening (degree -3 -> degree -2),
  NOT a full removal to a bounded kernel; full cancellation would require the write current
  (phase gradient <ell,r>) to vanish, i.e. a trivial write, contradicting n != 0 (FORM
  B6/D3). Current conservation d ell_j = 0 gives gauge-invariance/well-definedness but a
  DIVERGENCE-FREE current is still NONZERO, so it does not raise the diagonal vanishing order.
  Charge conjugation n -> -n only conjugates the fixed-n difference (V(0) is n-blind) — a
  +/-n cancellation is unavailable at fixed winding. The ONE exact symmetry present — the
  ANTISYMMETRY (oddness) of the imaginary degree -3 part C_off(r) = -i alpha r/(2 pi^2 |r|^4)
  — cancels EXACTLY but ONLY in the OPERATOR-NORM/L^2 sense (this IS the sealed "L^2-BOUNDED
  BUT NOT HILBERT-SCHMIDT" property, ECO :168-171); it is POWERLESS for the Hilbert-Schmidt
  object R-L2b requires because the HS integrand |C_off|^2 is EVEN and positive (parity gives
  nothing). Span: ECO :151-155, :168-171; RFA :66. No connection-only symmetry forces full
  HS cancellation.)

LEADING_DEGREE_3 = SURVIVES(the connection-only phase-difference softens the leading degree
  -3 by exactly ONE power (to degree -2), leaving a residual singularity in the Hilbert-
  Schmidt difference; it is NOT reduced to a bounded kernel by any connection-only symmetry.
  Full removal is excluded by symmetry: it would require the nonzero write current to vanish.
  The antisymmetry that would kill it acts in the operator norm, not the HS norm. This
  reproduces, independently and via the phase/write-current mechanism, the corpus's own
  "short one power" (wall §3.4).)

NET = DOES_NOT_FULLY_CANCEL (alpha runs)(no exact connection-only symmetry forces the leading
  degree -3 to fully cancel in the HS difference; the phase structure delivers only a one-
  power partial softening and the exact antisymmetry lives in the wrong (operator) norm. By
  the corpus arithmetic this is the alpha < 1 / partial-cancellation horn (RFA :126-128) ->
  aggregate divergence -> C not intensive -> running kappa_record / RG -> alpha RUNS; the
  scale that appears is the EMERGENT RG scale, not a re-import. CAVEAT, honestly flagged: the
  SYMMETRY binary is decided NO; whether the surviving degree -2 residual is nonetheless
  rendered HS-finite by the operator COMPOSITION in the C(...)C sandwich (the commutator route
  ECO :189-201, ROUTE_NOT_LEMMA) is a METRIC COMPUTATION, not a symmetry — and per the
  tasking's mapping ("needing a computation/scale to see the residual = the residual survives
  = RUNS horn; no third road") this is the RUNS horn, NOT a fence-undetermined of the symmetry
  question. This determination does NOT contradict the CHECK's correction (STAGE8_REQUIRE_
  CLUSTER_CHECK Joint 3): IF full cancellation THEN alpha=1 clean success; I determine there
  is NO full-cancellation SYMMETRY, so we are on the partial/runs side — resolving, at the
  symmetry level, the corpus's "UNKNOWN.")

FENCE_PRESSURE = one point, declined: the HS-fate of the surviving degree -2 residual under
  the operator COMPOSITION C(V(a)-V(0))C / the commutator route (the unbuilt R-L2b metric
  computation). I decided ONLY the symmetry binary (which needs no kappa_record and no numeric
  kernel evaluation) and did NOT evaluate the residual's number; per the tasking that
  computation-openness is the RUNS horn, not a fence-undetermined. Fence NOT crossed.

FORBIDDEN_IMPORTS = none. No GR, no faithfulness premise, no scale used as authority. The
  sealed degree -3 kernel FORM (odd/imaginary/degree -3), the HS-vs-operator-norm CZ fact, and
  the |D|_4/alpha arithmetic are QUOTATION-AND-CLASSIFICATION of sealed text (ECO/RFA, SCALE),
  read only to analyze the cancellation symmetry — never a positive certifier, never evaluated.

MACHINERY_INVOKED = no. Nothing computed, bounded, estimated, evaluated, or compared; n,
  kappa_record, alpha, and every scale/spectrum left symbolic. The degrees (-3 sealed; +1 the
  phase-gradient; -2 their product) are symbolic orders of homogeneous factors; |odd|^2 = even
  is elementary parity; both locate the deficit without a numeric evaluation. Seals recomputed
  at path before reading; no register/tracker/plan/road/ledger/lens read; no git action.

alpha_computed = false ; kappa_record_computed = false ; proof_authorized = false ;
coupling_evaluation_authorized = false
ALL_RESULTS = CLAIMED until the adversarial panel.
```
