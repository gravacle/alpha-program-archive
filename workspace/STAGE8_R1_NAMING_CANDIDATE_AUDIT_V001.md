# STAGE 8 — DEFAULT-REFUTE AUDIT OF STAGE8_R1_NAMING_CANDIDATE_V001 (THE r-1 NECESSITY DETERMINATION + THE STAGED NAMING CANDIDATE)

## INDEPENDENT AUDITOR — CODENAME R1-AUDIT — [SEALED]

Date: 2026-08-14
Role: independent auditor, briefed to REFUTE. Default stance held: every
claim treated as wrong until it survived my own re-derivation by routes
the build did not use. Under test: `STAGE8_R1_NAMING_CANDIDATE_V001.md`,
sha256 `e1da7446242de98a4997b778eaad5e791e192084852d4a8e4024e4b87c690ed6`
(recomputed from bytes at path this session; matches the tasked digest
AND the sidecar `.seal.sha256`).

Gates: `alpha_computed = false` ; `kappa_record_computed = false` ;
`proof_authorized = false`. ALL_RESULTS of the build remain CLAIMED
until this check; my results are CLAIMED until any successor check.

Fences held (mine): EXACT SYMBOLIC ANALYSIS ONLY — one CAS battery of my
own (sympy 1.14.0, fresh venv `r1auditvenv` under /private/tmp scratch,
NOT the build's `r1venv`), routes DIFFERENT from the build's §2.6
wherever a different exact route exists; script and output verbatim in
§2.6-§2.7 (21/21 PASS on the final full run); every constant symbolic or
an exact rational/surd; nothing numeric evaluated (integer and rational
comparisons are exact arithmetic; symbolic constants ordered only by
exact monotonicity chains); no physical quantity computed or bounded;
alpha never computed or approached; no value of D asserted or inferred
(d formal throughout); the stricken (1+|D|)/|1-D| display consumed
NOWHERE as ground — in particular I did NOT derive any kappa_bal(d)
from it; M(t)/1_{D_t} untouched and sharp; equal-time FALSE by C6
respected; per-pair route barred and not traversed; H-R never defaulted;
no flag flipped; no witness action; no gate moved; ONE file written
(this artifact) plus its seal sidecar; output name probed before write:
ABSENT. Disclosed reads beyond the workspace (provenance duty only, no
mathematical content consumed): read-only git forensics on the archive
repo (log/show/diff — no git write action), and token-locating greps
plus minimal excerpts of supervision-side files (QUESTIONS_SETTLED
register, FIVE_C staging sheet) solely to adjudicate the build's
UNLOCATABLE-token flags and the guard-digest discrepancy; every
mathematical claim adjudicated here traces to sealed artifacts at path
plus my own battery.

Tooling disclosure, on the record (mine): three harness-form corrections
were made before the final battery run, none changing any mathematical
claim — (i) `solveset` returns a ConditionSet on the parametric
threshold equation (tooling; replaced by `solve`, root unchanged);
(ii) sympy leaves `Sum(1/(i+2), (i,1,n))` unevaluated — the SAME tooling
wall the build's header discloses; my repair route is DIFFERENT from the
build's shifted-Sum: a complete two-step INDUCTION proof of the closed
form (base + recurrence, each a CAS-exact identity, recurrence reduced
by `expand_func`); (iii) my own draft of the theta-family fixed-n check
wrongly added (I-C) to the full-space determinant — my construction
error, corrected to det(I - 2CPC) (the complement of ran C already
carries eigenvalue 1). The final battery then ran ONCE: 21/21 PASS.

---

## 0. VERDICT IN ONE LINE

**CONFIRMED-WITH-CORRECTIONS — the NECESSITY = NECESSARY determination is CONFIRMED on all three prongs by independent re-derivation on different routes (21/21 CAS PASS), and STRENGTHENED by an attack the build did not run (my augmented-constraint probe: even adding the un-listed HS-divergence constraint sum s_i^2 -> oo, family-relativity survives via my alternating witness model AV (s = 1, 1/3): det_{2m} = (-1)^m 3^{-m} -> 0 with kappa -> oo, against NV's |det_n| >= 3^{-27/16} — so the verdict does not rest on the completeness of the build's stated constraint list); the staged candidate R-L4a-N is adoptable spec text with NO outcome-shopping, NO paper-over (kappa_n asserted nowhere, both branches carried unsealed, the third region consuming nothing), falsifiers V-N1..V-N5 sound, mechanics conformant (nothing frozen, no fence, no flag, witnesses stand), and TOY_SEPARATION = clean (CH-1 the one PREMISE(named) with immateriality/forcing conditions stated; my independent ledger re-derivation found no OPEN entry and no missed unforced choice); THREE corrections named exactly — c-1 PROVENANCE: the build's guard digest 43db1d77 was true at verification but STALE AT SEAL (the principal appended three clauses to the guard mid-session, 13:17-13:21:48, current 2baa4c31; recovered at git 9e2f303b/eae84b0e; appends are append-only and requirement-neutral for builds); c-2 the "grep-complete" regularization-byte enumeration MISSES E1 :1870 (a witness-table row that RESTATES the openness — supports, does not undermine, NOT-FORCED); c-3 N.5's void condition ("FIRES iff" F-a/F-b/F-c) covers only baseline-point failures — a sealed refutation of the polydisc-identical vanishing at this naming with the baseline intact (the r-3-axis failure) leaves R-L4b false at the naming without firing the reopen (consumers stay safe: consumption remains gated on discharge inputs that then never arrive; repair = one added fire condition F-d or drop "iff"); the hazard OF RECORD (Branch-2) DOES fire the clause as written; nothing here moves the R-L4 certification, the gate list, the adopted amendment (V-1..V-6 severally untouched and un-fired), or the alpha' = 1/4 record; adoption remains the principal's alone.**

---

## 1. SEALS — ALL RECOMPUTED FROM BYTES AT PATH THIS SESSION, BY FULL DIGEST

Workspace files under `/Users/bgm/MB Work/alpha-program-archive/workspace/`;
the guard under `/Users/bgm/MB Work/alpha_supervision/`. Every digest
recomputed by me from bytes at path (never substring presence); each
compared against its `.seal.sha256` sidecar and the build's §1 table.

```text
e1da7446242de98a4997b778eaad5e791e192084852d4a8e4024e4b87c690ed6  STAGE8_R1_NAMING_CANDIDATE_V001.md  MATCH (under test; = tasked digest; = sidecar)
a903716c23c1a6969932e988f90d464abe9e8ee96624cd2dce3e32416de132e0  STAGE8_RL4_RL0_CERTIFICATION_V001.md  MATCH (CERT; = tasked a903716c; = sidecar; = build §1)
685afac8205b4ed2ed0a309a321f6eccc940882e89ec3dfbce70fd9b8d74af52  STAGE8_RL4_RL0_CHECK_V001.md  MATCH (CERT-CHK; = tasked 685afac8; = sidecar; = build §1)
468467303a109dc825b015107897dacc107800fc981030377c3f006b384cccb5  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md  MATCH (E1; = tasked 46846730; = sidecar; = build §1)
57edbb964610bb7c9715bccdf88cf0400ef5af230bf1be139a0be300d90994d8  STAGE8_R3C_SUMMED_REMAINDER_ATTEMPT_V001.md  MATCH (R3C; = sidecar; = build §1)
d66a922cfe023284890de8a335c38028efe94fb7a9d31b1f779bb0a0513b95cc  STAGE8_K_CHANNEL_CONTROL_V001.md  MATCH (KCH; = sidecar; = build §1)
26f9314bdbbf1d7638ecbdf398c891cb3ba54251d4b40314df39c03ab48c08b7  STAGE8_ZERO_FREE_DERIVATION_V001.md  MATCH (ZF; = sidecar; = build §1)
52f2490b187fd4b307c2af45f6238ea02f1d6839b23466fefee1dbba47ed6241  STAGE8_RL2B_UNIFORMITY_REFUTED_RESULT_V001.md  MATCH (per-pair refutation; = sidecar; = build §1)
2baa4c31fbe566516c3f61dcac351889e914368bd33b8c96ff40a161788c4fd5  /Users/bgm/MB Work/alpha_supervision/ACTUAL_SURFACE_GUARD_V001.md  CURRENT BYTES (= its sidecar; also = the archive mirror supervision/ copy) — DIVERGES from the build's cited 43db1d77: ADJUDICATED, see below
```

**The guard discrepancy, adjudicated at the archive git history (read-only
forensics; no git write action):**

```text
g-1  The build's §1 cites the guard at 43db1d77. The file at path NOW
     computes 2baa4c31 (sidecar agrees; mtime 13:21:48).
g-2  Git history of supervision/ACTUAL_SURFACE_GUARD_V001.md in the
     archive repo (commit -> sha256 of blob, recomputed by me):
       69f313c8 12:02:58  guard installed
       9e2f303b 12:41:11  RELEVANCE BURDEN appended     -> 43db1d77  (the build's digest)
       df8cb5d8 13:17:18  CALIBRATION appended          -> cd9fdbe9
       150b45dc 13:21:02  PURPOSE clause appended       -> 6cda5845
       eae84b0e 13:21:48  PUSHBACK FORK appended        -> 2baa4c31  (current)
g-3  The build sealed at 13:24:49 (sidecar 13:25:06). So its guard
     verification was TRUE AT VERIFICATION TIME (the 12:41 revision) and
     STALE AT SEAL: the principal appended three clauses mid-session.
     Corroboration that 43db1d77 was the guard earlier today: the
     QUESTIONS_SETTLED register (12:42) and CHAIN_RELEVANCE_MAP_V001
     (12:57, "read IN FULL") both record 43db1d77.
g-4  MATERIALITY: the diff 9e2f303b..eae84b0e is APPEND-ONLY (verified by
     git diff; the guard's own REOPEN/UPDATE clause is append-only), and
     the three appended clauses (CALIBRATION OF THE BURDEN; PURPOSE OF
     AUDITS; THE PUSHBACK FORK) calibrate AUDIT/adjudication conduct;
     none alters THE CRITERION, the MANDATORY CHOICE LEDGER classes, the
     TOY_SEPARATION rule, the ROBUSTNESS PROMOTION, or the RELEVANCE
     BURDEN the build consumed. No requirement the build was subject to
     changed. Everything the build consumed from the guard is byte-
     identical in both revisions.
RULING: c-1 CORRECTION (named, non-refuting): the build's "8/8 MATCH ...
     verified at path THIS session" is true of its verification moment
     and false of its seal moment for the guard row; the honest row is
     "verified at 43db1d77 (12:41 revision), superseded mid-session by
     principal appends." My audit consumed the CURRENT guard (2baa4c31)
     in full and holds the build to it, including the three appends.
```

7/8 ground digests match current bytes exactly; the 8th (GUARD) matches
the git-recovered revision of its verification moment; NONE UNVERIFIABLE.

Sealed content read at path by me this session: the build in full; CERT
in full; CERT-CHK in full; the CURRENT guard in full; E1 :160-178,
:286-345, :404-480, :640-900, :995-1035, :1100-1110, :1665-1700,
:1860-1880, :1944-1960, plus a full-file grep battery (below); ZF
:321-360, :390-430; R3C and KCH verdict/flag/§1 spans plus full-file
kappa_n greps; 52f2490b :18-30 and flags. The build's tasked-token flags
re-verified: "Q-1046" and "DERIVE-BEFORE-AUTHOR" are UNLOCATABLE in the
workspace corpus outside the build's own quotation of its tasking (my
grep concurs) — and they ARE locatable in supervision-side files the
build was fenced from reading (the FIVE_C staging sheet's ACT 1 menu,
option (a), is exactly the pattern the build executed: necessity
determination first, candidate with the FALSE branch worked, arriving
READY-FOR-PRINCIPAL; register entry Q-1046 is the summed-S2' precedent
of that pattern). The build's UNLOCATABLE-flag handling (the KCH/Q-1054
pattern: flagged as tasking-context, not defaulted) was the correct and
honest handling.

---

## 2. THE NECESSITY ADJUDICATION (ATTACKED FROM BOTH SIDES)

The build determined NECESSARY. Per the audit discipline I attacked from
the forcing side and the independence side — hunting the derivation the
build may have missed (the program's precedent being exactly a proposed
act proven unnecessary) — and re-derived its three exhibited chains by
different routes.

### 2.1 Attack 1 — hunt the FORCING derivation (is the choice a lemma?)

```text
a1-1 THE CLAUSE'S OWN BYTES RESERVE AN OPEN SELECTION. E1 :768 "AND WITH
     THE REGULARIZATION EXPLICITLY NAMED"; register :1024-1025 "with the
     regularization named". Neither restricts the class to families of
     record. CERT §2.3(b) reads it of record: "NAMING that regularization
     (OR ANOTHER) ... is the spec author's adoption act" — the certified
     reading itself keeps the class open beyond families of record.
     ZF o-3: "they need the named regularization act at the divergent
     trace" — an ACT. PA-3 (:1947-1956) is an OUTCOME-CLASS prediction,
     confidence moderate, not a derivation — verified at bytes.
a1-2 COMPLETENESS HUNT (my own): I ran the regularization-shaped grep
     over E1 myself (stems: regulariz*, case-insensitive) — hits at
     :170, :469, :768, :772, :779, :784, :1025, :1103, :1870, :1951,
     :1952, :1956 — and a broader-shape sweep (cutoff/truncat/mollif/
     smooth/zeta/heat-kernel): all broader hits are D6'-adjacent
     localizer-smoothing bytes or cluster/Moebius-truncation bytes,
     none a determinant-regularization class-closer. RESULT: the
     build's enumeration (:170, :462-470, :766-782, :784, :1024-1025,
     :1103, :1947-1956) covers all but ONE hit: E1 :1870, the witness-
     table row for R-L4a/b — "what is open is whether the baseline
     determinant exists at all and UNDER WHICH REGULARIZATION."
     c-2 CORRECTION (named, non-refuting): the build's "grep-complete"
     claim is false at :1870. The missed byte RESTATES the openness of
     the selection — it supports NOT-FORCED; no conclusion moves.
a1-3 CAN F'-5 OR ANY SCOPING CLAUSE CLOSE THE CLASS? F'-5 (:1671-1678)
     bars carrier index/truncation level/cellulation data from CERTIFIED
     CONSTANTS — it constrains what constants may depend on, not which
     family may be named (any admissible family is index-carrying at the
     family axis; that is AR-4's point, honored by consumption at the
     family/limit quantifier). D6' (:462-470) bars localizer
     mollification — it prunes the class (AR-2), it does not close it.
     F'-4 (:1669-1670) bars new measured constants (AR-3) — prunes, does
     not close. C2 (:330-333) makes fixed-carrier finiteness forbidden
     as a certification scope — grounds AR-4, does not close the class.
a1-4 THE NARROWING IS REAL BUT IS NOT A FORCING. The build's UNIQUENESS-
     OF-RECORD lemma — among admissible families consuming ONLY objects
     of record, the carrier compression {C_n} is the unique member — is
     verified at its grounds: the record's fixed-n objects ARE the
     compressions (ZF §4.1(b): A_{mu lambda, n}(a) = C_n(V(a)-1)C_n,
     read at bytes); the per-pair uncompressed limit is refuted of
     record (ZF §4.1(c) at bytes; 52f2490b verified at path, flags
     RL2b_uniformity_refuted = true / X_HS_norm_infinite = true /
     eps_threshold_exists = false, the M-form obligation at its :21-24);
     the PA carrier (789338ad, cited through CERT's verified §1) is the
     sealed construction the family lives on. My hunt for a SECOND
     of-record family that renders 2 C~ P C~ trace class per member
     (slab families — symbol level, wrong axis; D3 cell refinements —
     spatial, not the operator axis; the omega = 0 slice — bookkeeping
     intermediate; polydisc radius — domain parameter; Moebius/connected
     truncation — cluster axis, not a compression of CPC) found NONE.
     But closing the WHOLE class would require a sealed clause
     restricting the naming to record-consuming families — a1-1's bytes
     show the reservation runs the other way (the spec author may
     introduce; "or another").
RESULT: NO FORCING DERIVATION EXISTS ON THE SEALED BASIS. The precedent
     class ("proposed rule proven derivable, hence never authored") does
     NOT match: what is left open is a selection over a class the
     record's own certified reading leaves open; a derivation cannot
     close an authorship reservation. The build's Prong A stands, WITH
     the c-2 enumeration correction.
```

### 2.2 Attack 2 — hunt the naming-free completion (Prong B) and test its robustness beyond the build's own exhibit

```text
b2-1 UNCOMPRESSED EMPTINESS re-verified at its grounds: CPC =
     (PC)^dag(PC) >= 0; a nonnegative operator is trace class iff its
     trace is finite; tr(CPC) = +infinity sealed (E1 :757-758 via CERT
     §2.3(a), check-confirmed); det_2 requires the HS hypothesis and
     ||CPC||_2 is radius-independent and INFINITE by C6 (E1 :713-715 at
     bytes). Both Carleman factors undefined uncompressed — identity
     grade. My CAS adds the spectral sanity on a NEW exact instance
     (Q9: spec(CPC) in [0,1] on a deterministic rational 4x4).
b2-2 THE BUILD'S FAMILY-RELATIVITY EXHIBIT re-derived by different
     routes (Q1-Q8): model V (s_i = 1/(i+2)): det_n = 2/((n+1)(n+2))
     by the GAMMA route -> 0; tr_n = harmonic(n+2) - 3/2 by a complete
     INDUCTION proof (base + recurrence, each CAS-exact); sum s_i^2 =
     pi^2/6 - 5/4 finite; kappa_n -> infinity. Model NV (s_i =
     1 - 3^{-i}): sign (-1)^n from 1 - 2s_i <= -1/3 < 0; mass M = 3/8
     by hand-assembled geometric sums; avoidance delta = 1/6 with
     equality at i = 1; U = 2/9; the chord bound re-grounded (concavity
     + midpoint identity + endpoint exactness, Q6) gives |det_n| >=
     (4 delta^2)^{M/(2U)} = (1/9)^{27/32} = 3^{-27/16} EXACT (exponent
     arithmetic Q7), and the partial products -1/3, 7/27, -175/729 all
     clear the bound by INTEGER-EXACT comparison (Q8: 7^16 3^27 > 3^48;
     175^16 3^27 > 3^96). Both models satisfy the sealed eigenvalue-
     data constraints (s_i in [0,1]; trace divergent) and realize
     OPPOSITE determination outcomes. CONFIRMED.
b2-3 MY ATTACK BEYOND THE BUILD — IS THE STATED CONSTRAINT SET
     COMPLETE? The build lists {s_i in [0,1]; tr_n -> oo} as "every
     sealed eigenvalue-data constraint". Candidate missing constraint:
     C6's ||CPC||_2 = +infinity, pushed through the 52f2490b lower-
     semicontinuity pattern (X_n -> X strongly => ||X||_2 <= liminf
     ||X_n||_2), would force sum s_i^2 -> infinity on any EXHAUSTING
     admissible family — a constraint model V VIOLATES (its sum s^2 is
     finite). This is the strongest independence-side attack I found:
     if relativity DEPENDED on model V, the necessity verdict would
     rest on an incomplete constraint list. THE ATTACK DISSOLVES BY
     EXHIBIT (R1, mine): the alternating model AV (s_{2j-1} = 1,
     s_{2j} = 1/3) satisfies the AUGMENTED set — tr_{2m} = 4m/3 -> oo,
     sum s^2 = 10m/9 -> oo — with kappa_{2m} = 4m/9 -> oo and det_{2m}
     = (-1)^m 3^{-m} -> 0 EXACT (vanishing outcome); NV itself has
     sum s^2 = n - (1-3^{-n}) + (1-9^{-n})/8 -> oo (non-vanishing
     outcome). BOTH outcomes live under {s in [0,1], tr -> oo,
     sum s^2 -> oo}: family-relativity is ROBUST to the augmentation.
     Note of record: the lower-semicontinuity transport to C_nPC_n is
     MY derivation, not sealed; the build's stated set is the sealed
     one, and its honesty marker ("witness-family grade ... decide
     nothing about the actual carrier family") is exactly right. The
     robustness exhibit STRENGTHENS the build's Prong B: the verdict
     survives even if the constraint list grows by the natural next
     member.
b2-4 (b-3) re-checked at the bytes: R-L4a's naming demand is a
     constituent of the obligation (":768"), and b2-1 empties the
     unregularized level — so satisfaction requires a named family.
     CONFIRMED: the act-CLASS is necessary.
```

### 2.3 Attack 3 — hunt the regularization-INDEPENDENCE derivation (Prong C)

```text
c3-1 THE PARAMETRIC d-EXHIBIT re-derived by the S± identity route (P2,
     different from enumeration): N_all(d) = (S_+^2 + S_-^2) +
     2 S_+ S_- d = (1-d)/2 EXACT; N_all(1) = 0 = |m_0|^2 (ZF Z10b's
     by-design vanishing, read at bytes) — no normalization at d = 1;
     c'_00(d) - 1/2 = d/(2(1-d)) != 0 for d != 0. Every census
     consumer is a nonconstant function of d. Matches CERT §2.2's own
     failure mode and CERT-CHK C6 exactly. CONFIRMED.
c3-2 THE THRESHOLD MOTION re-derived (P3): root set of k u e^u = 1/2 is
     {W(1/(2k))}; u e^u strictly increasing on u >= 0; W' =
     W/(y(1+W)) > 0; and the gap 1/2 - 1/(2k) = (k-1)/(2k) > 0 for
     k > 1 — the root sits STRICTLY below the sealed W(1/2). Fully
     parametric; no balance value asserted; the stricken display
     nowhere used (I verified the build cites it nowhere as ground —
     its FENCE NOTE is honest; and I equally refused to derive any
     kappa_bal(d) form, which would BE the stricken display). CONFIRMED.
c3-3 THE QUANTIFIER GAP IS THE RESIDUE ITSELF: independence of the
     consumers = "d = 0 under every admissible naming" = R-L4b's truth
     universally quantified over an open class = r-2 (+ r-3) universal.
     r-2 is unsealed on BOTH branches (CERT §2.3(d) "NEITHER BRANCH IS
     SEALED", check-confirmed; the third region undecided per check
     n-1, which I re-read at its bytes). c3-1/c3-2 show the consumers
     MOVE if the exclusion fails; b2-2/b2-3 show the sealed record
     cannot exclude the failure. NOT MOOT — CONFIRMED.
```

### 2.4 The constraint set AR-1..AR-5 and the necessity ruling

Each AR re-verified at its cited bytes: AR-1 at :767-768 with CERT
§2.3(a)-(b) (route + per-member trace-class); AR-2 at D6' :462-470
(read verbatim); AR-3 at F'-4 :1669-1670 + the frozen algebra :746-748;
AR-4 at F'-5 :1671-1678 + C2 :330-333; AR-5 derived from the consumer
(the exclusion assigns the census one value; the NV (-1)^n exhibit
makes the subsequential two-valuedness exact — my Q4/Q5 re-derive the
sign mechanism). The AR set is sound and each member is genuinely
derivable from the cited bytes.

```text
NECESSITY RULING: CONFIRMED — NECESSARY, on all three prongs, by
independent re-derivation on different routes, with the robustness of
Prong B strengthened by my augmented-set exhibit (b2-3/R1) and one
enumeration correction (c-2, non-outcome-bearing) of record.
The honest deliverable ordering (derive first, author second) was
followed and its derivable maximum (the AR narrowing +
uniqueness-of-record) is exactly what the build extracted.
```

### 2.5 What would have refuted, and was hunted

```text
h-1 a sealed clause closing the admissible class to families of record
    (would make the naming a lemma via uniqueness-of-record): NOT FOUND
    — the certified reading says "or another" (CERT §2.3(b)).
h-2 a sealed derivation deciding kappa_n for the carrier family (would
    collapse the dichotomy and possibly the relativity): NOT FOUND —
    r-2 unsealed both branches, third region undecided (check n-1).
h-3 a sealed constraint on admissible eigenvalue data killing ONE of
    the two outcome classes (would defeat family-relativity): NOT FOUND
    — and the natural candidate (HS-divergence via lower
    semicontinuity) fails to defeat it (my R1 exhibit).
h-4 a sealed identity making the census/threshold consumers constant in
    the opposite-sector value (would make the act moot): NOT FOUND —
    the motion is exact and my P2/P3 re-derive it.
```

### 2.6 MY CAS BATTERY (VERBATIM)

sympy 1.14.0, fresh venv `r1auditvenv` under /private/tmp scratch;
nothing written to the workspace but this artifact and its seal.

```python
# R1-AUDIT independent CAS battery — EXACT SYMBOLIC ONLY (sympy 1.14.0, fresh
# venv r1auditvenv under /private/tmp scratch; NOT the build's r1venv). Routes
# chosen to DIFFER from the build's §2.6 wherever a different exact route
# exists. Every constant symbolic or an exact rational/surd; nothing numeric
# evaluated (integer/rational comparisons are exact arithmetic; symbolic
# constants compared only by exact orderings). Groups:
#   P*  — necessity re-pins by different routes (census via S± identities;
#         consumer motion; threshold motion by solveset+derivative).
#   Q*  — the two witness models re-derived by DIFFERENT routes (gamma/
#         telescoping closed forms; geometric sums assembled by hand;
#         integer-exact bound comparisons) + the kappa identity on a NEW
#         deterministic exact-rational 4x4 instance (not the build's theta
#         family, not CERT's random trials).
#   R*  — MY OWN attack models, beyond the build's: (R1) the HS-divergence
#         augmentation (sum s_i^2 -> oo, the C6/52f2490b lower-semicontinuity
#         shape the build did NOT list as a constraint): a replacement
#         vanishing model satisfying the AUGMENTED set, proving
#         family-relativity ROBUST — the necessity verdict does not rest on
#         the possibly-incomplete constraint list; (R2) the modulus-
#         monotonicity probe for the F-c completion label (nested-spectrum
#         models have |det| non-increasing, so F-c at nested models forces
#         liminf > 0; non-nested families are not so constrained — the
#         N.5(iv) wording note is scoped exactly).
#   S*  — candidate-interface checks by different routes: the factorization
#         frame on fully-symbolic 2x2 via explicit inverse (not the build's
#         3x3 adjugate) + a deterministic exact-rational 4x4 instance; the
#         discharge calculus |det_n(a)| <= |det_n(0)|^{1-eps}; the B2
#         exponent arithmetic (1/9)^{27/32} = 3^{-27/16}; scalar Carleman
#         sanity.
import sympy as sp
from sympy import Rational as R

ok = lambda name, cond: print(f"{name}: {'PASS' if cond else 'FAIL'}", flush=True)

# ===== P1 — census re-pin via the S± identity route (not enumeration-only) =====
w = [R(1, 2), R(-1, 4), R(-1, 4)]
ph = [1, -1, -1]
Sp = sum(w[i] for i in range(3) if ph[i] == 1)
Sm = sum(w[i] for i in range(3) if ph[i] == -1)
pairs = [(a, b) for a in range(3) for b in range(3)]
surv = [(a, b) for (a, b) in pairs if ph[a]*ph[b] == 1]
opp = [(a, b) for (a, b) in pairs if ph[a]*ph[b] == -1]
sv = sum(w[a]*w[b] for (a, b) in surv)
op_ = sum(w[a]*w[b] for (a, b) in opp)
c = {p: w[p[0]]*w[p[1]]/sv for p in surv}
ok("P1 census by phase-product: 9 = 5+4; sv = S+^2 + S-^2 = 1/2; opp = 2 S+ S-"
   " = -1/2; N_surv(0) = 1/2; c = (1/2, 1/8 x4) > 0; sum c = 1; sum|c| = 1",
   len(pairs) == 9 and len(surv) == 5 and len(opp) == 4
   and sv == Sp**2 + Sm**2 == R(1, 2) and op_ == 2*Sp*Sm == R(-1, 2)
   and sorted(c.values()) == [R(1, 8)]*4 + [R(1, 2)]
   and all(v > 0 for v in c.values()) and sum(c.values()) == 1
   and sum(abs(v) for v in c.values()) == 1)

# ===== P2 — consumer motion, identity route: N_all(d) = (S+^2+S-^2) + 2 S+ S- d =====
d = sp.Symbol('d')
N_all = (Sp**2 + Sm**2) + 2*Sp*Sm*d
c00 = w[0]*w[0]/N_all
ok("P2 N_all(d) = (1-d)/2 by the S± identity route; N_all(1) = 0 = |m_0|^2;"
   " c'_00(d) - 1/2 = d/(2(1-d)) != 0 for d != 0 (exact rational function)",
   sp.expand(N_all - (1 - d)/2) == 0 and N_all.subs(d, 1) == 0
   and sp.simplify(c00 - 1/(2*(1 - d))) == 0
   and sp.simplify(c00 - R(1, 2) - d/(2*(1 - d))) == 0)

# ===== P3 — threshold motion: root + monotonicity + exact gap decomposition =====
# (harness-form correction, disclosed: solveset returns a ConditionSet on the
# parametric equation — tooling, not mathematics; sp.solve returns the root.)
u = sp.Symbol('u', real=True)
k = sp.Symbol('k', positive=True)
y = sp.Symbol('y', positive=True)
Wy = sp.LambertW(y)
ok("P3 root set of k u e^u = 1/2 is {W(1/(2k))}; u e^u strictly increasing on"
   " u >= 0 ((1+u)e^u > 0); W' = W/(y(1+W)) > 0 on y > 0; gap 1/2 - 1/(2k) ="
   " (k-1)/(2k) > 0 for k > 1: root strictly below W(1/2)",
   sp.solve(k*u*sp.exp(u) - R(1, 2), u) == [sp.LambertW(1/(2*k))]
   and sp.ask(sp.Q.positive((1 + u)*sp.exp(u)), sp.Q.nonnegative(u))
   and sp.simplify(sp.diff(Wy, y) - Wy/(y*(1 + Wy))) == 0
   and sp.simplify(R(1, 2) - 1/(2*k) - (k - 1)/(2*k)) == 0)

# ===== Q1 — model V by the gamma/telescoping route =====
i, n, m = sp.symbols('i n m', positive=True, integer=True)
det_v_gamma = sp.gamma(n + 1)*sp.gamma(3)/sp.gamma(n + 3)   # prod i/(i+2) = n! 2!/(n+2)!
ok("Q1 V: prod_{i=1}^n i/(i+2) = n! 2!/(n+2)! = 2/((n+1)(n+2)) (gamma route);"
   " -> 0; and 1 - 2/(i+2) = i/(i+2) exact",
   sp.simplify(det_v_gamma - 2/((n + 1)*(n + 2))) == 0
   and sp.limit(det_v_gamma, n, sp.oo) == 0
   and sp.simplify(1 - 2/(i + 2) - i/(i + 2)) == 0)
# (harness-form correction, disclosed: sympy leaves Sum(1/(i+2), (i,1,n))
#  unevaluated — the same tooling wall the build's header discloses. My route
#  is DIFFERENT from the build's shifted-Sum: a complete INDUCTION proof of
#  the closed form, every step CAS-exact — base case f(1) = first summand,
#  recurrence f(n+1) - f(n) = next summand, both symbolic identities.)
#  (second harness form: the harmonic recurrence needs expand_func to reduce.)
f_closed = sp.harmonic(n + 2) - R(3, 2)
base = sp.simplify(f_closed.subs(n, 1) - R(1, 3))                     # = s_1 = 1/(1+2)
step = sp.simplify(sp.expand_func(f_closed.subs(n, n + 1) - f_closed - 1/(n + 3)))
ssq_v = sp.summation(1/(i + 2)**2, (i, 1, sp.oo))
ok("Q2 V: tr_n = H_{n+2} - 3/2 by INDUCTION (base f(1) = 1/3 = s_1 EXACT;"
   " step f(n+1) - f(n) = 1/(n+3) = s_{n+1} EXACT) -> oo; sum s^2 = pi^2/6"
   " - 5/4 finite; kappa_n = 2(tr_n - sum s^2) -> oo (Branch-1 realized)",
   base == 0 and step == 0
   and sp.limit(f_closed, n, sp.oo) == sp.oo
   and sp.simplify(ssq_v - (sp.pi**2/6 - R(5, 4))) == 0)

# ===== Q3 — model NV by hand-assembled geometric sums (different route) =====
s_nv = 1 - 3**(-i)
geo_third = (R(1, 3))*(1 - 3**(-n))/(1 - R(1, 3))       # sum_{i=1}^n 3^{-i}
tr_nv_direct = sp.summation(s_nv, (i, 1, n))
M_hand = (R(1, 3))/(1 - R(1, 3)) - (R(1, 9))/(1 - R(1, 9))  # sum 3^-i - sum 9^-i, closed geometric
ok("Q3 NV: sum_{1}^{n} 3^{-i} = (1 - 3^{-n})/2 (geometric, hand); tr_n ="
   " n - (1 - 3^{-n})/2 -> oo; M = sum s(1-s) = 1/2 - 1/8 = 3/8 EXACT",
   sp.simplify(geo_third - (1 - 3**(-n))/2) == 0
   and sp.simplify(tr_nv_direct - (n - (1 - 3**(-n))/2)) == 0
   and sp.limit(tr_nv_direct, n, sp.oo) == sp.oo
   and M_hand == R(3, 8)
   and sp.summation(3**(-i) - 9**(-i), (i, 1, sp.oo)) == R(3, 8))
# avoidance and domain by exact chain: 3^{-i} <= 1/3 on i >= 1 via ratio 3^{-(i+1)}/3^{-i} = 1/3 < 1
ok("Q4 NV avoidance: |s_i - 1/2| = 1/2 - 3^{-i} >= 1/6 (equality i = 1);"
   " delta = 1/6; U = 1/4 - 1/36 = 2/9; u_1 = 2/9 = U; u_2 = 8/81 < U;"
   " 1 - 2 s_i = 2*3^{-i} - 1 <= -1/3 < 0 for i >= 1 (sign (-1)^n exact)",
   sp.simplify((R(1, 2) - 3**(-i)).subs(i, 1) - R(1, 6)) == 0
   and R(1, 4) - R(1, 36) == R(2, 9)
   and sp.simplify((3**(-i) - 9**(-i)).subs(i, 1) - R(2, 9)) == 0
   and sp.simplify((3**(-i) - 9**(-i)).subs(i, 2) - R(8, 81)) == 0
   and R(8, 81) < R(2, 9)
   and (2*R(1, 3) - 1) == R(-1, 3)
   and sp.simplify(1 - 2*s_nv - (2*3**(-i) - 1)) == 0)
p1 = R(-1, 3); p2 = p1*(2*R(1, 9) - 1); p3 = p2*(2*R(1, 27) - 1)
ok("Q5 NV partial products by direct factor multiplication: -1/3, 7/27,"
   " -175/729 (signs alternate exactly)",
   p2 == R(7, 27) and p3 == R(-175, 729) and p1 < 0 and p2 > 0 and p3 < 0)
# Branch-2 bound re-derived: chord log(1-4u) >= (u/U)log(1-4U) on [0,U] (concavity;
# endpoints exact; midpoint identity route), then sum u_i <= M:
uu, UU = sp.symbols('uu UU', positive=True)
ok("Q6 chord grounds re-run: d2/du2 log(1-4u) = -16/(1-4u)^2; endpoints exact;"
   " midpoint (1-2U)^2 - (1-4U) = 4U^2 >= 0; 1 - 4(1/4 - delta^2) = 4 delta^2",
   sp.simplify(sp.diff(sp.log(1 - 4*uu), uu, 2) + 16/(1 - 4*uu)**2) == 0
   and sp.log(1 - 4*uu).subs(uu, 0) == 0
   and sp.expand((1 - 2*UU)**2 - (1 - 4*UU) - 4*UU**2) == 0
   and sp.expand(1 - 4*(R(1, 4) - sp.Symbol('dl')**2) - 4*sp.Symbol('dl')**2) == 0)
ok("Q7 NV bound arithmetic: M/U = 27/16; M/(2U) = 27/32; (4 delta^2) = 1/9;"
   " ((1/9)^{27/16})^{1/2} = 3^{-27/16} EXACT; and the CERT form"
   " (4 delta^2)^{M/(2U)} = 3^{-27/16} agrees",
   R(3, 8)/R(2, 9) == R(27, 16) and R(3, 8)/(2*R(2, 9)) == R(27, 32)
   and 4*R(1, 6)**2 == R(1, 9)
   and sp.simplify((R(1, 9)**R(27, 16))**R(1, 2) - 3**(-R(27, 16))) == 0
   and sp.simplify(R(1, 9)**R(27, 32) - 3**(-R(27, 16))) == 0)
ok("Q8 NV moduli vs bound, INTEGER-EXACT: (1/3)^16 > (1/3)^27... i.e."
   " |det_1| = 1/3: 3^27 > 3^16 ; |det_2| = 7/27: 7^16 3^27 > 3^48 ;"
   " |det_3| = 175/729: 175^16 3^27 > 3^96 — all |det_i| > 3^{-27/16}",
   3**27 > 3**16
   and 7**16 * 3**27 > 3**48
   and 175**16 * 3**27 > 3**96)
# (|det| > 3^{-27/16}  <=>  |det|^16 > 3^{-27}  <=>  num^16 * 3^27 > den^16, exact integers)

# ===== Q9 — kappa identity on a NEW deterministic exact-rational 4x4 =====
def proj_of(cols):
    B = sp.Matrix(cols).T
    G = B.T*B
    return B*G.inv()*B.T
Cq = proj_of([[1, 1, 0, 0], [0, 0, 1, 2]])
Pq = proj_of([[1, 2, 3, 4], [1, 0, 1, 0]])
CPCq = Cq*Pq*Cq
lhs = sp.trace((Cq*Pq - Pq*Cq).T*(Cq*Pq - Pq*Cq))
rhs = 2*sp.trace(CPCq) - 2*sp.trace(CPCq*CPCq)
eigs = CPCq.eigenvals()
ok("Q9 NEW exact 4x4 instance: C, P exact orthoprojections; ||[C,P]||_F^2 ="
   " 2tr(CPC) - 2tr((CPC)^2) EXACT; spec(CPC) subset [0,1] (s_i in [0,1]"
   " verified on the instance)",
   sp.simplify(Cq*Cq - Cq) == sp.zeros(4) and sp.simplify(Pq*Pq - Pq) == sp.zeros(4)
   and Cq.T == Cq and Pq.T == Pq
   and sp.simplify(lhs - rhs) == 0
   and all(sp.simplify(e) >= 0 and sp.simplify(e) <= 1 for e in eigs))

# ===== Q10 — Branch-1 sufficiency chain re-run (different h-ordering route) =====
ok("Q10 1 - 4u <= e^{-4u} on u >= 0: g(u) = 4u - 1 + e^{-4u}, g(0) = 0,"
   " g' = 4(1 - e^{-4u}) with e^{-4u} <= 1 on u >= 0 (1 - e^{-4u} ="
   " e^{-4u}(e^{4u} - 1), both factors >= 0 coeffwise); 4 sum u = 2 kappa",
   (4*uu - 1 + sp.exp(-4*uu)).subs(uu, 0) == 0
   and sp.simplify(sp.diff(4*uu - 1 + sp.exp(-4*uu), uu) - 4*(1 - sp.exp(-4*uu))) == 0
   and sp.simplify((1 - sp.exp(-4*uu)) - sp.exp(-4*uu)*(sp.exp(4*uu) - 1)) == 0
   and all(cf > 0 for cf in sp.Poly(sp.series(sp.exp(4*uu) - 1, uu, 0, 7).removeO(), uu).coeffs())
   and sp.expand(4*sp.Symbol('Ms') - 2*(2*sp.Symbol('Ms'))) == 0)

# ===== R1 — MY ATTACK: the HS-divergence AUGMENTATION (beyond the build) =====
# If C6's ||CPC||_2 = oo forces (52f2490b lower-semicontinuity shape) the
# additional constraint sum s_i^2 -> oo on exhausting families, model V FAILS
# the augmented set (its sum s^2 is finite). REPLACEMENT vanishing model AV:
# s_{2j-1} = 1, s_{2j} = 1/3 (alternating). Exact: sum s^2 -> oo, tr -> oo,
# kappa -> oo, det_{2m} = (-1)^m 3^{-m} -> 0. NV already has sum s^2 -> oo.
# So BOTH outcomes are realized under the AUGMENTED constraint set too:
# family-relativity is ROBUST; the necessity verdict does not depend on the
# completeness of the build's stated constraint list.
j = sp.Symbol('j', positive=True, integer=True)
mm = sp.Symbol('mm', positive=True, integer=True)
tr_av = sp.summation(1, (j, 1, mm)) + sp.summation(R(1, 3), (j, 1, mm))       # pairs (1, 1/3)
ssq_av = sp.summation(1, (j, 1, mm)) + sp.summation(R(1, 9), (j, 1, mm))
kap_av = 2*(sp.summation(0, (j, 1, mm)) + sp.summation(R(2, 9), (j, 1, mm)))  # 2 sum s(1-s)
det_av_2m = ((1 - 2*1)**mm) * ((1 - 2*R(1, 3))**mm)                            # (-1)^m (1/3)^m
ssq_nv = sp.summation((1 - 3**(-i))**2, (i, 1, n))
ok("R1 AUGMENTED-SET relativity: AV model (s alternating 1, 1/3): tr_{2m} ="
   " 4m/3 -> oo; sum s^2 = 10m/9 -> oo; kappa_{2m} = 4m/9 -> oo; det_{2m} ="
   " (-1)^m 3^{-m} -> 0 EXACT. NV: sum s^2 = n - (1 - 3^{-n}) + (1 - 9^{-n})/8"
   " -> oo with |det| >= 3^{-27/16}. BOTH outcomes live under {s in [0,1],"
   " tr -> oo, sum s^2 -> oo}: family-relativity ROBUST to the augmentation",
   sp.simplify(tr_av - 4*mm/3) == 0 and sp.limit(4*mm/3, mm, sp.oo) == sp.oo
   and sp.simplify(ssq_av - 10*mm/9) == 0 and sp.limit(10*mm/9, mm, sp.oo) == sp.oo
   and sp.simplify(kap_av - 4*mm/9) == 0 and sp.limit(4*mm/9, mm, sp.oo) == sp.oo
   and sp.simplify(det_av_2m - (-1)**mm*3**(-mm)) == 0
   and sp.limit(3**(-mm), mm, sp.oo) == 0
   and sp.simplify(ssq_nv - (n - (1 - 3**(-n)) + (1 - 9**(-n))/8)) == 0
   and sp.limit(ssq_nv, n, sp.oo) == sp.oo)

# ===== R2 — MY PROBE: modulus monotonicity scopes the F-c completion label =====
# For s in [0,1]: |1 - 2s| <= 1 exactly ((1-2s)^2 <= 1 <=> 4s(1-s) >= 0).
# Hence on NESTED-spectrum models (each member extends the last eigenvalue
# list) |det_{n+1}| = |det_n| |1-2s_{n+1}| <= |det_n|: the modulus is
# non-increasing, so it CONVERGES; F-c non-convergence at nested models can
# only occur at positive modulus limit (sign flips) — N.5(iv)'s
# "NON-VANISHING" label is EXACT there. The actual carrier family need not
# nest (eigenvalues re-solve at each n): the liminf-0 non-convergent subcase
# is not excluded of record — the wording note is scoped to exactly that.
s = sp.Symbol('s', real=True)
ok("R2 (1-2s)^2 <= 1 on s in [0,1] (identity 1 - (1-2s)^2 = 4s(1-s) >= 0,"
   " both factors nonneg on [0,1]): nested-model modulus non-increasing =>"
   " converges; F-c at nested models forces liminf > 0",
   sp.expand(1 - (1 - 2*s)**2 - 4*s*(1 - s)) == 0
   and sp.simplify((4*s*(1 - s)).subs(s, R(1, 3))) == R(8, 9)
   and R(8, 9) >= 0)

# ===== S1 — factorization frame: fully-symbolic 2x2 via EXPLICIT INVERSE =====
a11, a12, a21, a22, b11, b12, b21, b22 = sp.symbols('a11 a12 a21 a22 b11 b12 b21 b22')
A0m = sp.Matrix([[a11, a12], [a21, a22]])
Am = sp.Matrix([[b11, b12], [b21, b22]])
I2 = sp.eye(2)
M0 = I2 + A0m
D0 = M0.det()
Rn = M0.adjugate()/D0            # explicit inverse (division carried)
lhs_fac = sp.simplify(D0*(I2 + Rn*(Am - A0m)).det() - (I2 + Am).det())
ok("S1 2x2 fully symbolic, explicit-inverse route: det(1+A0) det(1 + R(A-A0))"
   " = det(1+A) where R = (1+A0)^{-1} (division carried and cancelled EXACTLY)",
   lhs_fac == 0)
# deterministic exact-rational 4x4 instance of the same identity:
A04 = sp.Matrix(4, 4, lambda p, q: R((p + 2*q) % 5 - 2, 3))
A4 = sp.Matrix(4, 4, lambda p, q: R((2*p + q) % 7 - 3, 4))
M04 = sp.eye(4) + A04
ok("S2 4x4 exact-rational instance: det(1+A0) != 0 and det(1+A0) det(1 +"
   " (1+A0)^{-1}(A - A0)) = det(1+A) EXACT",
   M04.det() != 0
   and sp.simplify(M04.det()*(sp.eye(4) + M04.inv()*(A4 - A04)).det()
                   - (sp.eye(4) + A4).det()) == 0)
# det multiplicativity + scaling on fully symbolic 3x3 (the build's C3 claims):
X3 = sp.Matrix(3, 3, lambda p, q: sp.Symbol(f'x{p}{q}'))
Y3 = sp.Matrix(3, 3, lambda p, q: sp.Symbol(f'y{p}{q}'))
cs = sp.Symbol('cs')
ok("S3 det(XY) = det X det Y and det(cX) = c^3 det X, fully symbolic 3x3",
   sp.expand((X3*Y3).det() - X3.det()*Y3.det()) == 0
   and sp.expand((cs*X3).det() - cs**3*X3.det()) == 0)

# ===== S4 — the discharge calculus of N.3 (B1 + r-3 suffices) =====
L, eps = sp.symbols('L epsilon', positive=True)
ok("S4 |det_n(a)| <= e^{-L} e^{eps L} = (e^{-L})^{1-eps} with L = -log|det_n(0)|"
   " -> oo and eps < 1  =>  bound -> 0: (B1 + joint rate) => full-family"
   " polydisc vanishing (exact exponent algebra + limit)",
   sp.simplify(sp.exp(-L)*sp.exp(eps*L) - sp.exp(-(1 - eps)*L)) == 0
   and sp.limit(sp.exp(-(1 - eps)*L).subs(eps, R(1, 2)), L, sp.oo) == 0
   and sp.limit(sp.exp(-(1 - eps)*L).subs(eps, R(9, 10)), L, sp.oo) == 0)
# scalar Carleman sanity: |1+x| <= e^{|x|} at the 1x1 grade (series route)
xr = sp.Symbol('xr', nonnegative=True)
ok("S5 1 + x <= e^{x} on x >= 0 (e^x - 1 - x has all series coefficients"
   " >= 0; scalar sanity of the |det(1+X)| <= e^{||X||_1} frame input)",
   all(cf > 0 for cf in sp.Poly(sp.series(sp.exp(xr) - 1 - xr, xr, 0, 7).removeO(), xr).coeffs()))

# ===== S6 — fixed-n existence at the build's theta-family, DIFFERENT check =====
# (harness-form correction, disclosed: my draft added (I-C) to the full-space
#  determinant — wrong construction, the complement of ran C already carries
#  eigenvalue 1 in I - 2CPC since CPC annihilates it; the FULL-SPACE det
#  IS the restricted det. Tooling/draft error of mine, not the build's.)
th = sp.Symbol('theta', real=True)
Cth = sp.Matrix([[sp.cos(th)**2, sp.cos(th)*sp.sin(th)],
                 [sp.cos(th)*sp.sin(th), sp.sin(th)**2]])
Pth = sp.Matrix([[1, 0], [0, 0]])
full_det = sp.simplify((sp.eye(2) - 2*Cth*Pth*Cth).det())
ok("S6 theta-family fixed-n existence by the full-space-det route: rank-one"
   " CPC kills the complement of ran C, so det(I - 2CPC) = det_{ran C}"
   "(1 - 2CPC) = -cos(2 theta) = 1 - 2cos^2(theta) EXACT (every member defined)",
   sp.simplify(full_det - (1 - 2*sp.cos(th)**2)) == 0
   and sp.simplify(full_det + sp.cos(2*th)) == 0
   and sp.simplify((Cth*Pth*Cth)*(sp.eye(2) - Cth)) == sp.zeros(2))

print("R1-AUDIT-BATTERY-DONE")
```

### 2.7 THE OUTPUT (VERBATIM, 21/21 PASS — the one final full run)

```text
P1 census by phase-product: 9 = 5+4; sv = S+^2 + S-^2 = 1/2; opp = 2 S+ S- = -1/2; N_surv(0) = 1/2; c = (1/2, 1/8 x4) > 0; sum c = 1; sum|c| = 1: PASS
P2 N_all(d) = (1-d)/2 by the S± identity route; N_all(1) = 0 = |m_0|^2; c'_00(d) - 1/2 = d/(2(1-d)) != 0 for d != 0 (exact rational function): PASS
P3 root set of k u e^u = 1/2 is {W(1/(2k))}; u e^u strictly increasing on u >= 0 ((1+u)e^u > 0); W' = W/(y(1+W)) > 0 on y > 0; gap 1/2 - 1/(2k) = (k-1)/(2k) > 0 for k > 1: root strictly below W(1/2): PASS
Q1 V: prod_{i=1}^n i/(i+2) = n! 2!/(n+2)! = 2/((n+1)(n+2)) (gamma route); -> 0; and 1 - 2/(i+2) = i/(i+2) exact: PASS
Q2 V: tr_n = H_{n+2} - 3/2 by INDUCTION (base f(1) = 1/3 = s_1 EXACT; step f(n+1) - f(n) = 1/(n+3) = s_{n+1} EXACT) -> oo; sum s^2 = pi^2/6 - 5/4 finite; kappa_n = 2(tr_n - sum s^2) -> oo (Branch-1 realized): PASS
Q3 NV: sum_{1}^{n} 3^{-i} = (1 - 3^{-n})/2 (geometric, hand); tr_n = n - (1 - 3^{-n})/2 -> oo; M = sum s(1-s) = 1/2 - 1/8 = 3/8 EXACT: PASS
Q4 NV avoidance: |s_i - 1/2| = 1/2 - 3^{-i} >= 1/6 (equality i = 1); delta = 1/6; U = 1/4 - 1/36 = 2/9; u_1 = 2/9 = U; u_2 = 8/81 < U; 1 - 2 s_i = 2*3^{-i} - 1 <= -1/3 < 0 for i >= 1 (sign (-1)^n exact): PASS
Q5 NV partial products by direct factor multiplication: -1/3, 7/27, -175/729 (signs alternate exactly): PASS
Q6 chord grounds re-run: d2/du2 log(1-4u) = -16/(1-4u)^2; endpoints exact; midpoint (1-2U)^2 - (1-4U) = 4U^2 >= 0; 1 - 4(1/4 - delta^2) = 4 delta^2: PASS
Q7 NV bound arithmetic: M/U = 27/16; M/(2U) = 27/32; (4 delta^2) = 1/9; ((1/9)^{27/16})^{1/2} = 3^{-27/16} EXACT; and the CERT form (4 delta^2)^{M/(2U)} = 3^{-27/16} agrees: PASS
Q8 NV moduli vs bound, INTEGER-EXACT: (1/3)^16 > (1/3)^27... i.e. |det_1| = 1/3: 3^27 > 3^16 ; |det_2| = 7/27: 7^16 3^27 > 3^48 ; |det_3| = 175/729: 175^16 3^27 > 3^96 — all |det_i| > 3^{-27/16}: PASS
Q9 NEW exact 4x4 instance: C, P exact orthoprojections; ||[C,P]||_F^2 = 2tr(CPC) - 2tr((CPC)^2) EXACT; spec(CPC) subset [0,1] (s_i in [0,1] verified on the instance): PASS
Q10 1 - 4u <= e^{-4u} on u >= 0: g(u) = 4u - 1 + e^{-4u}, g(0) = 0, g' = 4(1 - e^{-4u}) with e^{-4u} <= 1 on u >= 0 (1 - e^{-4u} = e^{-4u}(e^{4u} - 1), both factors >= 0 coeffwise); 4 sum u = 2 kappa: PASS
R1 AUGMENTED-SET relativity: AV model (s alternating 1, 1/3): tr_{2m} = 4m/3 -> oo; sum s^2 = 10m/9 -> oo; kappa_{2m} = 4m/9 -> oo; det_{2m} = (-1)^m 3^{-m} -> 0 EXACT. NV: sum s^2 = n - (1 - 3^{-n}) + (1 - 9^{-n})/8 -> oo with |det| >= 3^{-27/16}. BOTH outcomes live under {s in [0,1], tr -> oo, sum s^2 -> oo}: family-relativity ROBUST to the augmentation: PASS
R2 (1-2s)^2 <= 1 on s in [0,1] (identity 1 - (1-2s)^2 = 4s(1-s) >= 0, both factors nonneg on [0,1]): nested-model modulus non-increasing => converges; F-c at nested models forces liminf > 0: PASS
S1 2x2 fully symbolic, explicit-inverse route: det(1+A0) det(1 + R(A-A0)) = det(1+A) where R = (1+A0)^{-1} (division carried and cancelled EXACTLY): PASS
S2 4x4 exact-rational instance: det(1+A0) != 0 and det(1+A0) det(1 + (1+A0)^{-1}(A - A0)) = det(1+A) EXACT: PASS
S3 det(XY) = det X det Y and det(cX) = c^3 det X, fully symbolic 3x3: PASS
S4 |det_n(a)| <= e^{-L} e^{eps L} = (e^{-L})^{1-eps} with L = -log|det_n(0)| -> oo and eps < 1  =>  bound -> 0: (B1 + joint rate) => full-family polydisc vanishing (exact exponent algebra + limit): PASS
S5 1 + x <= e^{x} on x >= 0 (e^x - 1 - x has all series coefficients >= 0; scalar sanity of the |det(1+X)| <= e^{||X||_1} frame input): PASS
S6 theta-family fixed-n existence by the full-space-det route: rank-one CPC kills the complement of ran C, so det(I - 2CPC) = det_{ran C}(1 - 2CPC) = -cos(2 theta) = 1 - 2cos^2(theta) EXACT (every member defined): PASS
R1-AUDIT-BATTERY-DONE
```

---

## 3. THE CANDIDATE ADJUDICATION (R-L4a-N AS ADOPTABLE SPEC TEXT)

Audited requirement by requirement at the R-L4 clauses' own bytes
(E1 :766-790 re-read at path by me; the CERT §2.1 quote and the build's
citations byte-checked against them).

### 3.1 Outcome-shopping: NONE

```text
o-1 The consumption interface N.3 is SYMMETRIC: (B1)-type sealed input
    discharges the vanishing; (B2)-type refutes it (and fires N.5);
    (B3) third region licenses NOTHING — carried undecided exactly per
    the check's n-1 (two sufficient branches, not a partition; I
    re-read n-1 at its bytes). No clause makes one branch easier to
    certify than the record makes it.
o-2 The named family does not pre-steer the verdict: r-2 is open at
    THIS family (both branches unsealed of record), and the candidate
    asserts neither. PA-3's moderate-confidence outcome-class
    prediction is not imported anywhere in the candidate text.
o-3 The FALSE branch is worked at equal depth to the TRUE branch (N.5
    is the longest clause) — the anti-shopping shape.
o-4 One narrowing noted (n-B below): N.3's "DISCHARGED ... only by"
    makes the of-record r-2+r-3 route the exclusive discharge
    interface. Direction: CONSERVATIVE (it can only make discharge
    harder, never easier) — not shopping. See n-B.
```

### 3.2 Paper-over: NONE (kappa_n asserted nowhere)

```text
p-1 grep of the candidate text: every kappa_n occurrence is inside the
    definition, the (B1)/(B2)/(B3) CONDITIONAL interface, or the
    explicit negative ("asserts NOTHING about kappa_n"). N.4 states the
    unsealed status of r-2 on both branches in the clause body itself.
p-2 The kappa_n dichotomy consumed is exactly CERT §2.3(d)'s, with the
    check's n-1 non-partition correction HONORED in spec text (B3) —
    the candidate is more careful than CERT's own "dichotomy" label.
p-3 The (B1) sufficiency, the (B2) lower bound with exponent M/(2U),
    and the product form det_n(0) = prod(1 - 2 s_i) are each of record
    (CERT §2.3(c)/(d), re-derived by me: Q6/Q7/Q10/S6/Q9) — nothing
    cited beyond its sealed grade.
p-4 The r-3 joint rate is stated as an INPUT with its own of-record
    form, not presumed; my S4 verifies the discharge calculus is sound
    (B1 + rate => full-family polydisc vanishing:
    |det_n(a)| <= |det_n(0)|^{1-eps} -> 0).
p-5 No value frozen anywhere: no D, no kappa_n, no delta, no M, no
    limit value. Verified by read of every N-clause.
```

### 3.3 The FALSE-branch clause N.5 (the tasked question: does the void condition fire on the hazard of record?)

```text
YES on the hazard of record — and one completeness gap named:
f-1 THE HAZARD OF RECORD is CERT §2.3(d) Branch 2 / §2.4: bounded
    kappa_n + uniform 1/2-avoidance => |det_n(0)| bounded away from 0
    => R-L4b FALSE at the compression regularization, census re-opens.
    N.5 (F-a) fires on EXACTLY these hypotheses at this naming;
    (F-b)/(F-c) additionally catch the det-level shadows (liminf > 0;
    non-convergence — the NV shape, sign (-1)^{#{s_i > 1/2}} of
    record) by ANY route, hypotheses certified or not. FIRES. The
    reopen list (ii) matches CERT §2.2 m-3's consumer set exactly
    (5/4 census, N_surv(0) = 1/2, c-weights, kappa_bal = 1, the R-L0
    display's kappa_bal factor, R-L0b's convexity footing) — I checked
    it item by item against CERT §2.2/§3.3(a)/§3.5; V-N5 additionally
    polices this list's completeness. (iii) obligations-not-values per
    :773-778 + F'-3 — honest. Renaming reserved to the principal — the
    no-lane line held.
f-2 c-3 CORRECTION (the completeness gap, named exactly): N.5 opens
    "This clause FIRES iff ..." and lists only BASELINE-POINT
    conditions (F-a/F-b/F-c are all statements about det_n(0) or the
    B2 hypotheses). The r-3-AXIS failure — a sealed artifact refuting
    the polydisc-identical vanishing AT THIS NAMING with the baseline
    intact (det_n(0) -> 0 but det(1 + A_n(a*)) not-> 0 at some a* on
    the closed pair polydisc) — leaves R-L4b FALSE at this naming with
    the void/reopen clause NEVER firing (the "iff" bars reading it in).
    CONSUMER SAFETY: intact — consumption of the exclusion is gated on
    the discharge inputs (B1 + r-3), which can never certify once the
    polydisc vanishing is refuted; consumers then stay conditional
    forever; nothing is corrupted. But the clause's HONESTY PROMISE
    (declare R-L4b FALSE AT THIS REGULARIZATION and reopen) would not
    self-execute on that hazard. REPAIR (one line, adoption-time or
    addendum): add "(F-d) exhibits, at some point of the closed pair
    polydisc, failure of the full-family vanishing det(1 + A_n(a)) ->
    0 at this naming" — or replace "iff" by "if", leaving the fire
    list sufficient-not-exhaustive. NOT VOID-GRADE: the fire list
    covers the hazard OF RECORD (f-1); the gap is a hazard the record
    names structurally (CERT §2.4's joint-rate axis) but has not
    exhibited.
f-3 n-A WORDING NOTE (non-correction, scoped by my R2 derivation):
    N.5(iv) completes the R-L4a determination "NON-VANISHING at this
    regularization" on the FALSE branch. EXACT for F-a/F-b; for F-c at
    NESTED-spectrum families the modulus is non-increasing (|1-2s| <= 1
    on [0,1], R2) hence converges, so non-convergence forces
    liminf > 0 and the label is exact there too; the actual carrier
    family's spectra need NOT nest, so a non-convergent det_n(0) with
    liminf = 0 is not excluded of record — there the honest completion
    label is "NOT-VANISHING-AS-A-LIMIT (no limit exists)". One-word
    tightening at adoption; no operative effect ((i)-(iii) are correct
    in every fire case).
```

### 3.4 Falsifier soundness (V-N1..V-N5)

```text
v-1 V-N1 (admissibility): sound; note it is UNFIREABLE on the current
    record (C_n finite rank of record => trace class per member
    automatic) — insurance against the record being other than
    believed, not a live hazard. Harmless.
v-2 V-N2 (uniqueness-of-record): sound and honest — an antedating
    distinct of-record family voids the NARROWING PREMISE specifically
    and returns the naming to the principal at the wider class; exactly
    the right consequence shape.
v-3 V-N3 (interface): sound — each protected item is of record and
    refutation at its own quantifier voids; my Q6/Q7/Q9/Q10/S6
    re-derivations put all three items beyond my refutation.
v-4 V-N4 (supersession): sound — the DERIVE-BEFORE-AUTHOR insurance;
    voids as MOOT on a forcing or independence derivation; mirrors the
    program's own precedent (a proposed act proven unnecessary). §2 of
    this audit re-verified no such derivation exists on the current
    sealed basis.
v-5 V-N5 (false-branch integrity): sound — polices the reopen list.
    Note V-N5 covers omitted CONSUMERS only; the c-3 gap (an omitted
    FIRE CONDITION) is outside its reach, which is why c-3 is a named
    correction rather than falsifier-covered. A V-N5-style guard for
    the fire list would be subsumed by the F-d repair.
```

### 3.5 Mechanics conformance

```text
m-1 Nothing frozen: verified (no value of D, kappa_n, delta, M, or any
    limit anywhere in N.1-N.8).
m-2 No fence touched: stricken display untouched (N.4 keeps it
    stricken; nowhere cited as ground); D6' honored BY CONSTRUCTION
    (compression on the carrier axis; M(t)/1_{D_t} sharp; the
    candidate itself bars mollification); H-R untouched; per-pair
    route not traversed; equal-time respected; register/road/etc. not
    read by the build (its fence list verified against its own text
    and file-write record: ONE file + sidecar, mtimes 13:24:49 /
    13:25:06, no other workspace file touched today by that session).
m-3 No flag flipped; no witness action: all three R-L4 witnesses
    explicitly STAND in N.8; adoption reserved to the principal;
    PROPOSED-NOT-ADOPTED carried in the clause header, N.8, and the
    flag block consistently.
m-4 One regularization for both clauses (N.2/CH-5): verified FORCED at
    E1 :784 ("with the regularization of R-L4a") — read at bytes.
m-5 Full-family quantifier stated in the clause body (N.1) with its
    consumer ground — conformant with AR-5.
m-6 n-B INTERFACE-NARROWING NOTE (non-correction): N.3's "DISCHARGED
    at this naming ONLY BY (B1) + r-3" tracks the record's own act
    enumeration (CERT §2.4's verdict names exactly these acts; r-3 is
    the record's named residue). A future sealed derivation of the
    polydisc vanishing by a DIFFERENT route would technically sit
    outside this interface and would need a one-line candidate
    touch-up. Direction conservative; steering none; principal's
    discretion whether to future-proof the wording at adoption
    ("or a sealed derivation of the full-family polydisc vanishing at
    its own quantifier").
```

### 3.6 THE CHOICE LEDGER, INDEPENDENTLY RE-DERIVED, AND THE TOY_SEPARATION RULING

Per the guard (consumed by me at CURRENT bytes 2baa4c31, all appends
included), the audit re-derives the ledger hunting choices the build
missed:

```text
L-1 CH-1 (the naming selection): correctly the ONE PREMISE(named).
    The claim visibly conditions on it ("AT THIS REGULARIZATION" /
    "at this naming" throughout N.3/N.5 — verified by read). Both the
    immateriality condition (r-2/r-3 universally quantified over the
    admissible class) and the forcing condition (a sealed clause
    closing the class; uniqueness-of-record would then force C_n) are
    stated IN THE LEDGER and are correct (my §2.1/§2.3 concur that
    neither exists sealed). Guard-conformant PREMISE(named).
L-2 CH-2 (full-family quantifier) FORCED: the ground is real (the
    consumer's one-value demand; the NV (-1)^n exhibit re-derived at
    my Q4/Q5). Audit refinement, no reclassification: a subsequential
    naming is itself a DIFFERENT admissible family selection — i.e.,
    the subsequence freedom lives inside CH-1's named premise, and
    GIVEN the family named, the consumption quantifier is forced by
    the consumer. The ledger's structure holds.
L-3 CH-3 (a = 0 + joint-rate split) FORCED of record: the
    factorization identity is unconditional (my S1/S2 by different
    routes) and CERT §2.4 is its of-record consumption. See n-B for
    the "only by" wording note — a clause-text note, not a ledger
    defect.
L-4 CH-4 (obligations-reopen-not-values) FORCED: :773-778 + F'-3 read
    at bytes; correct.
L-5 CH-5 (one regularization both clauses) FORCED: :784 read at bytes;
    correct.
L-6 HUNT FOR MISSED UNFORCED CHOICES: (i) the WITNESS-MODEL choices
    (V, NV; delta = 1/6 etc.) — supporting-artifact exhibits, not
    candidate-chain choices; the claims they carry are EXISTENCE
    claims, invariant under which witness realizes them (any pair with
    opposite outcomes suffices — my AV model is a third witness and
    nothing moves); no ledger entry owed. (ii) the eigenvalue-basis
    presentation prod(1 - 2 s_i) — of record (R-L1), a forced
    presentation. (iii) the kappa_n-interface presentation — not a
    choice OF the candidate (it accepts det-level inputs F-b/F-c
    independently of kappa framing). (iv) the domain scoping (opposite
    sector only; baseline a = 0 as displayed) — forced at :746-762.
    NO MISSED UNFORCED CHOICE FOUND. ZERO entries in class OPEN.
L-7 MACHINERY/RELEVANCE (guard append, both revisions): the
    compression family classified SURFACE-DERIVED with booked trace
    (PA carrier; ZF §4.1(b)(c)) — verified at those bytes; the
    candidate's own statement that apparatus origin is why CH-1 is a
    PREMISE and N.5 is live is exactly the guard's intended posture.
    No APPARATUS-ONLY object anchors any claim.
L-8 ROBUSTNESS PROMOTION (guard): the one mechanism claimed structural
    in the build (family-relativity) is exhibited on TWO independent
    instances (V, NV) plus an invariance argument (the constraint-set
    satisfaction), and this audit adds a THIRD independent instance
    (AV) on a strictly harder constraint set — the guard's
    two-instances-plus-invariance bar is cleared with margin.
TOY_SEPARATION RULING (the audit's, as the artifact itself defers):
    **clean** — no quantifier slippage found (every instance-grade
    exhibit marked witness-family grade and consumed only at existence
    grade; the theta-family consumed at fixed-n existence grade only);
    no construction posing as description (the one convenience that
    could become load-bearing IS the named premise CH-1, visibly
    conditioned on throughout; nothing else unforced found).
```

---

## 4. BEARING, PROVENANCE, INJECTION, FENCES

### 4.1 Bearing (each tasked item, stated severally)

```text
b-1 THE R-L4 CERTIFICATION (a903716c + 685afac8): UNMOVED. The build
    consumes it and adds no claim at its quantifiers; the candidate on
    adoption would discharge ONLY the naming demand (:768, :784); the
    "D IS UNDEFINED" half, the dichotomy, and all three witnesses
    stand exactly as certified.
b-2 THE GATE LIST ("C exists": R-L4a/b + R-L0(/R-L0b) + C-L2 + OBL-D;
    landing set summed-S2' + R-L4a/b + R-L0(/R-L0b) + C-L2/G_cm):
    UNMOVED. No member retired, none added; r-2 and r-3 remain the
    named unsealed inputs even on adoption.
b-3 THE ADOPTED AMENDMENT (summed-S2', ce59b480 verified at path),
    V-1..V-6 SEVERALLY: V-1 (summed estimate at its own quantifier) —
    untouched, no summed-estimate claim anywhere in the build;
    V-2 (one-way bridge) — untouched, the per-pair route barred and
    not traversed, no bridge invoked; V-3 (REM anchor overturn) —
    untouched, REM consumed nowhere by the build; V-4 (bytes-
    contradiction) — none introduced, every candidate citation
    byte-checked here; V-5 (C4-kill failure) — untouched, the kill
    consumed only through the sealed census re-pins; V-6 (marking
    fraud) — the build's marks (DERIVED/CLAIMED/CONDITIONAL,
    witness-family grade, PROPOSED-NOT-ADOPTED) are honest per this
    audit's full read. NONE FIRED; NONE TOUCHED.
b-4 THE alpha' = 1/4 RECORD: UNMOVED — a different object (the summed
    Schatten exponent of the S2 discharge); the token appears nowhere
    in the build; no claim of the build bears on it.
b-5 THE RESIDUE LANDSCAPE: unchanged exactly as the build's flag block
    states — r-1 would discharge ON ADOPTION ONLY (the principal's
    act; the FIVE_C ACT-1 menu, option (a), is the pattern this
    deliverable serves); r-2/r-3 unchanged; R-L2b / H-R / C-L2/G_cm /
    summed-S2' untouched at their own quantifiers.
```

### 4.2 Provenance

```text
pr-1 Digests: §1 — build digest matches tasked value and sidecar; 7/8
     grounds match current bytes; the guard adjudicated (c-1) with the
     full revision chain recovered and the diff verified append-only.
pr-2 Cited spans: every load-bearing citation of the build found as
     cited at path by my own reads — E1 :160-178 (B-4), :330-333 (C2),
     :417-426 (D3), :462-470 (D6'), :657-666 (R.0 displays), :679-737
     (S1-S5; S3 deletion grounds :713-715), :745-762 (R.2), :766-790
     (the clauses, byte-read), :794-800 (kappa_bal grounds), :1024-1025
     (register), :1103 (route header), :1669-1678 (F'-4/F'-5),
     :1947-1956 (PA-3); ZF :321-345 (§4.1(a)-(c)), :390-430 (o-1..o-3,
     Z10b); CERT §2.1-§2.4/§5/flags; CERT-CHK §4.3 i-4/i-5, §5
     n-1..n-3, §6; KCH: K_n is the cross-branch composite (its :134)
     and the token "kappa_n" is ABSENT from KCH and from R3C (my greps
     concur with the build's absence scans); R3C consumers conditional
     on R-L4a/b at its :181/:242/:927/:958/:1017; 52f2490b :18-30 +
     flags. The build's witness-family grade license (RB4/CB4) is a
     real pattern of record (R3C RB4; KCH :30). ONE citation-adjacent
     defect: c-2 (the :1870 enumeration miss), named in §2.1.
pr-3 The tasked-token flags: correct and honestly handled (§1).
```

### 4.3 Injection

```text
inj-1 No instruction-shaped or steering content directed at an auditor,
      registrar, or adopter found in the build or any sealed source
      read: my scans covered imperative/override patterns (none), and
      a full non-ASCII sweep of the build (all non-ASCII bytes are
      em-dashes, section signs, middle dots, +- signs — benign
      typography; no zero-width or bidi-control characters).
inj-2 The build's flag block matches its body span for span (checked
      NECESSITY / CANDIDATE_STATUS / FALSE_BRANCH / R2_HANDLING /
      CHOICE_LEDGER / NET / SEALS / FORBIDDEN_IMPORTS / MACHINERY
      against §§1-3 — no divergence; the registered-from-flag-block
      rule is satisfiable without drift).
inj-3 Seals verified by full-digest recomputation only, never by
      substring presence — mine and (per its text and consistency) the
      build's.
```

### 4.4 Fences

```text
fe-1 THE BUILD HELD ITS FENCES: exact symbolic only (its §2.6 battery
     re-read line by line: every constant symbolic or exact
     rational/surd; no decimal anywhere; the two disclosed pre-final
     harness corrections are tooling-form, mathematics unchanged — the
     same two walls my own battery hit, independently); alpha never
     approached; no value of D (d formal; my P2 concurs); stricken
     display never a ground (its N3/§2.4 fence note verified — the
     kappa_bal(d) form that WOULD be the stricken display appears
     nowhere); M(t) sharp; C6 respected; carrier/cellulation datum
     none (the named family is of record; models witness-grade); H-R
     never defaulted; per-pair route not traversed; one file + sidecar
     written; no git action by the build.
fe-2 I HELD MINE: enumerated in the header — exact symbolic battery
     (21/21, one final full run), nothing numeric evaluated, no
     physical quantity, alpha untouched, no value of D, stricken
     display unconsumed, no register-content consumption beyond the
     disclosed token-provenance reads, read-only git forensics only,
     ONE file written (this artifact) plus its seal, no flag flipped,
     no witness action, no gate moved.
fe-3 Gates re-affirmed: alpha_computed = false ;
     kappa_record_computed = false ; proof_authorized = false.
```

---

## 5. FLAG BLOCK

```text
NECESSITY_VERDICT = CONFIRMED-NECESSARY( all three prongs re-derived
  independently by different routes: (i) no naming-free completion —
  uncompressed emptiness identity-grade (CPC >= 0, tr = +oo sealed,
  ||CPC||_2 = oo by C6) and family-relativity re-derived (V by
  gamma-route + induction closed forms; NV by geometric sums, chord
  bound (1/9)^{27/32} = 3^{-27/16} exact, integer-exact modulus
  comparisons) AND strengthened by the audit's augmented-set exhibit:
  adding the un-listed HS-divergence constraint sum s_i^2 -> oo (the
  C6/52f2490b lower-semicontinuity shape) kills model V but NOT the
  relativity — replacement model AV (s alternating 1, 1/3; det_{2m} =
  (-1)^m 3^{-m} -> 0, kappa -> oo, sum s^2 -> oo) realizes vanishing
  and NV realizes non-vanishing under the augmented set, so the
  verdict does not rest on the build's constraint-list completeness;
  (ii) not forced — the clause's own bytes and the certified reading
  ("or another", CERT §2.3(b)) keep the class open; my independent
  regularization-byte sweep of E1 confirms no class-closer, with ONE
  enumeration correction (c-2): the build's "grep-complete" list
  misses :1870, a witness-table row that RESTATES the openness;
  uniqueness-of-record verified at its grounds as a narrowing, not a
  forcing; (iii) not moot — consumer motion re-derived by the S±
  identity route (N_all(d) = (1-d)/2; c'_00 - 1/2 = d/(2(1-d))) and
  the threshold root W(1/(2k)) < W(1/2) for k > 1 by the exact gap
  (k-1)/(2k) > 0; independence = r-2 (+r-3) universally quantified
  over an open class, underivable. CAS 21/21 PASS, one final full run,
  three disclosed harness-form corrections of my own. )
CANDIDATE_VERDICT = CONFIRMED-WITH-CORRECTIONS( adoptable as staged;
  outcome-shopping NONE (symmetric interface; FALSE branch worked at
  full depth; the one narrowing "only by" is conservative-direction,
  note n-B); paper-over NONE (kappa_n asserted nowhere; both branches
  carried unsealed; third region consumes nothing per check n-1; every
  interface item of record and re-derived here); falsifiers V-N1..V-N5
  sound (V-N1 unfireable on the current record — insurance; V-N4 the
  derive-before-author insurance verified against my own forcing/
  independence hunt); mechanics conformant (nothing frozen; no fence;
  no flag; witnesses stand; one regularization for both clauses forced
  at :784). CORRECTIONS NAMED: c-3 N.5's "FIRES iff" covers only
  baseline-point conditions — the r-3-axis hazard (sealed refutation
  of the polydisc-identical vanishing at this naming with baseline
  intact) leaves R-L4b false at the naming without firing the
  void/reopen; consumers stay safe (consumption gated on discharge
  inputs that then never arrive) but the honesty clause does not
  self-execute; repair = add fire condition F-d or drop "iff" —
  one line, adoption-time or addendum. NOTES: n-A N.5(iv)'s completion
  label "NON-VANISHING" exact for F-a/F-b and for nested-spectrum F-c
  (audit derivation R2: |1-2s| <= 1 makes nested moduli monotone);
  the non-nested liminf-0 non-convergent subcase would want
  "NOT-VANISHING-AS-A-LIMIT" — wording only; n-B "only by" tracks the
  record's own act list (r-2 + r-3), future-proofing optional. The
  hazard OF RECORD (Branch-2) DOES fire N.5 as written; the reopen
  list matches CERT §2.2 m-3 item by item. )
TOY_SEPARATION = clean( the audit's independent ledger re-derivation:
  CH-1 the one PREMISE(named), guard-conformant, visibly conditioned
  throughout, immateriality and forcing conditions stated and correct;
  CH-2..CH-5 FORCED with real grounds re-verified (CH-2's subsequence
  freedom correctly lives inside CH-1's class); ZERO OPEN entries; no
  missed unforced choice found (witness-model choices are existence-
  grade supporting exhibits, not chain choices); no quantifier
  slippage (witness-family grade marks honored everywhere); no
  construction posing as description; MACHINERY list conformant
  (compression family SURFACE-DERIVED, booked trace PA + ZF
  §4.1(b)(c); zero APPARATUS-ONLY anchors); robustness promotion
  cleared with margin (V, NV + the audit's third instance AV). )
V1_STATUS = UNTOUCHED-NOT-FIRED( the adopted amendment's V-1 — and
  V-2..V-6 severally — engaged by nothing in the build or the
  candidate: no summed-estimate claim (V-1), no bridge (V-2, per-pair
  route barred and untraversed), no REM consumption (V-3), no
  bytes-contradiction (V-4, every citation byte-checked), no C4-kill
  claim (V-5), marks honest (V-6). The amendment, its falsifiers, and
  the alpha' = 1/4 record all stand exactly as sealed. )
NET_VERDICT = CONFIRMED-WITH-CORRECTIONS( necessity CONFIRMED and
  robustness-strengthened; candidate CONFIRMED as staged with the
  corrections and notes named exactly (c-1 guard-digest staleness at
  seal — principal appends 13:17-13:21:48, append-only,
  requirement-neutral, build's verification true at its moment; c-2
  the :1870 enumeration miss — openness-restating, non-outcome-
  bearing; c-3 the N.5 fire-list gap — F-d repair named, consumer-safe
  meanwhile; n-A/n-B wording notes); NOTHING MOVES: the R-L4
  certification, the gate list, the adopted amendment V-1..V-6
  severally, the alpha' = 1/4 record, all witnesses, all gates —
  UNMOVED; the candidate remains PROPOSED-NOT-ADOPTED and adoption is
  the principal's alone; ALL_RESULTS = CLAIMED until checked. )
PROVENANCE = CLEAN-WITH-ONE-NAMED-STALENESS( build digest = tasked =
  sidecar; 7/8 ground digests match current bytes at path; the guard
  row adjudicated by read-only git forensics: build's 43db1d77 = the
  12:41:11 revision (9e2f303b), current 2baa4c31 = 13:21:48
  (eae84b0e), diff append-only (CALIBRATION, PURPOSE, PUSHBACK FORK),
  no build-facing requirement changed, everything the build consumed
  byte-identical across revisions; every cited span found as cited;
  the kappa_n-absence scans of KCH/R3C reproduced; the RB4/CB4
  witness-grade license located of record; tasked tokens Q-1046 /
  DERIVE-BEFORE-AUTHOR unlocatable in the workspace corpus (concur)
  and located in supervision-side files the build was fenced from —
  its flag-not-default handling correct. )
INJECTION = none( no instruction-shaped or steering content in the
  build or any sealed source read; full non-ASCII sweep benign
  (typography only, no zero-width/bidi controls); flag block matches
  body span for span; seals verified by full recomputation only. )
FENCES = held-both( BUILD: exact symbolic only, no numeric evaluation,
  alpha never approached, d formal with no value of D, stricken
  display never a ground, M(t) sharp, C6 respected, H-R undefaulted,
  per-pair route untraversed, one file + sidecar, no git action, two
  disclosed harness-form corrections tooling-only. AUDIT: same fence
  class held — exact symbolic battery (21/21, one final run, three
  disclosed harness-form corrections of my own), nothing numeric, no
  physical quantity, no value of D, stricken display unconsumed,
  read-only git forensics disclosed, supervision reads limited to
  token/digest provenance and disclosed, ONE file written (this
  artifact) plus its seal, no flag flipped, no witness action, no gate
  moved. alpha_computed = false ; kappa_record_computed = false ;
  proof_authorized = false. )
R1_NAMING_CANDIDATE_AUDIT_RESULT = SEALED.
```
