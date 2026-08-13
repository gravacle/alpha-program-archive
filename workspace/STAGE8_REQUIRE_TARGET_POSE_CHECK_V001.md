# STAGE 8 — REQUIRE-TARGET POSE CHECK: BLIND ADVERSARIAL VERIFICATION OF STAGE8_REQUIRE_TARGET_POSED_V001
## BLIND ADVERSARIAL VERIFIER (REQUIRE-POSE-CHECK) — TYPING/POSING VERIFICATION ONLY — [SEALED]

Date: 2026-08-13
Role: BLIND, cross-lineage, default-REFUTE. This artifact checks whether the TARGET was
POSED correctly. It decides NOTHING about forced/free, factorization, or the winding, and
computes/bounds NO value of R_record,L, the cross block, n, kappa, alpha, mu, C, beta, or
any scale/spectrum. Every symbol is symbolic. Verification is at the bytes: seals recomputed
at path, cited line spans opened and compared. No register/tracker/plan/road/ledger/lens read.

---

## 0. SEALS VERIFIED AT PATH (shasum -a 256, first 16 hex)

TARGET (verified before reading):
```text
STAGE8_REQUIRE_TARGET_POSED_V001.md
  e3c482b5facfb741...  MATCHES the tasked digest e3c482b5facfb7415199969d43155ddcaeae73b7...  OK
```

SOURCES the target cites (all recomputed at path; all MATCH the target's own §1 table):
```text
FORM STAGE8_R_RECORD_L_FORM_FABLE_V001.md ............................ 5e49d2093d4ee17b  OK
V011 review_packets/.../BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md . aa7c6d4904706276  OK
T1   STAGE8_EMERGENT_BOUNDARY_WINDING_FABLE_V001.md .................. e6fae1428cecffb3  OK
M03  STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_..._V001.md .... 2cd1ffcefd68ac03  OK
M06  STAGE8_TASK2D_SCALARIZATION_FUNCTIONAL_FORCING_..._V001.md ....... d13920e2a7687ac5  OK
ECO  STAGE8_EXTENSIVITY_VERDICT_AND_RL2B_CAMPAIGN_OPENING_V001.md ..... 0f3082cab910f2eb  OK
RFA  STAGE8_RL2B_FRAME_ANSWER_AND_CAMPAIGN_TARGET_V001.md ............. 2ede02aea415157a  OK
R4O  STAGE8_RL2B_REFUTING_BRANCH_FOUR_OBLIGATION_..._V001.md .......... f6fe40724ff4dfeb  OK
XSM  STAGE8_CROSS_SECTOR_METRIC_RULE_ADMISSIBILITY_SPEC_V001.md ....... 3c008ecccc2b01ac  OK
```
All ten seals match. The posing is anchored on verifiable sealed bytes; no source is stale
or substituted. Line-span citations checked one by one below.

---

## 1. ATTACK 1 — THE ONE-OBJECT CLAIM  → CONFIRMED

Claim under test (target §2 :50-94; flag :335-339): BOTH the FORM's full closure AND the
post-limit cross-block arbitration reduce to a SINGLE kernel C.

Checked at the bytes, and the reduction is SHOWN, not merely asserted:
- FORM §0 :24-31 and D5 :241-243,:263-265 close the WHOLE of R_record,L to `n^2 Phi^T C Phi`
  — one kernel C. Verified verbatim.
- FORM §4.2 :310-313 displays the sector-block matrix as a PARTITION of that same pullback:
  the cross block `Phi_f^T C Phi_H` is literally a sub-block of the same C, not a second
  object. FORM :331 states the post-limit arbiter verbatim: "the same dichotomy is controlled
  by whether `Phi_f^T C Phi_H` vanishes." So the post-limit cross-block verdict consumes the
  SAME C. Verified.
- The target does NOT flatten object and datum: §2 :81-94 explicitly separates the ONE
  OBJECT (C = G1) from the finite-N DATUM (G3, whether the write reaches both blocks) and
  names C "the arbiter" of removability GIVEN the write straddles both sectors. This is exact
  to the FORM (:334-343 leaves phi_f/phi_H to G3; :354-356 adds C at post-limit).

NUANCE (handled correctly by the target, not a defect): the post-limit cross-block verdict is
not C ALONE — it also requires phi_f != 0 and phi_H != 0 (datum G3). The target's own
FORCED_CRITERION lists all three conjuncts (F-i,F-ii,F-iii) and pins G3 as a separate node, so
the "one object" scope ("the arbiter of present-or-removable, given both blocks reached") is
accurate. VERDICT: CONFIRMED (target §2 :50-94, backed by FORM :24-31, :305-331).

---

## 2. ATTACK 2 — FORCED/FREE CRITERIA  → CONFIRMED (binary), WITH ONE CORRECTION

The rank-one algebra is correct at the bytes (FORM :315-331, verified):
- Finite-N form is `n^2 mu (phi_f + phi_H) ⊗ (phi_f + phi_H)` — manifestly RANK ONE (FORM
  D4 :217,:225). Correct.
- (a) a rank-one form is never a direct sum of two nonzero blocks (rank >= 2 for such a sum)
  — correct. (b) a block-diagonal (sector-respecting) congruence sends the cross block
  M_{fH} -> S_f^T M_{fH} S_H with S_f,S_H invertible, so nonvanishing is preserved (FORM
  :319-323) — correct. A cross block CAN be removed only by a NON-block-diagonal change, which
  MIXES the sectors and is therefore not "sector-respecting"; so "no admissible congruence
  removes a nonzero cross block" is right RELATIVE to the tasked notion of factorization
  (direct sum respecting [flux | H]). No admissible congruence was overlooked.
- A "free" branch cannot hide a "forced" one: PROP(cross) holds ⟺ irreducible cross term
  present; PROP(cross) fails ⟺ form factorizes. Complementary and exhaustive.

CORRECTION (posing imprecision, does NOT flip the binary): the target's FREE_CRITERION
(§3 :128-133 and flag :346-348) attaches the SAME consequence — "factorizes only DEGENERATELY:
R = R_sector ⊕ 0, the other sector's response identically zero" — to ALL THREE disjuncts,
including the post-limit case (R-iii) `Phi_f^T C Phi_H = 0`. That is wrong for (R-iii): at
post-limit C is a general PSD kernel, so `Phi_f^T C Phi_H = 0` with BOTH diagonal blocks
`Phi_f^T C Phi_f` and `Phi_H^T C Phi_H` nonzero is a NON-degenerate direct sum
`R_flux ⊕ R_H` — both sectors respond, merely decoupled — NOT `R = R_sector ⊕ 0`. The FORM
itself is careful here: :326-331 confines "R = R_sector ⊕ 0 / other sector identically zero"
to the finite-N RANK-ONE anchor (where `mu != 0` forces phi_f=0 or phi_H=0), and states
separately "Post-limit, the same dichotomy is controlled by whether `Phi_f^T C Phi_H`
vanishes." The target over-merged the post-limit sub-case into the degenerate-consequence
sentence, and mis-cites it to FORM :326-329 (the degenerate finite-N span). The forced/free
BINARY criterion is unaffected. VERDICT: CONFIRMED as the binary; CORRECTION on the FREE
branch's characterization.

---

## 3. ATTACK 3 — C = R-L2b UNIFICATION  → OVERSTATED

Obligation-level chain, checked verbatim and byte-supported:
- ECO §2 :86-95 seals obligation 4 = CONNECTED EXTENSIVITY "depends entirely on the shrink
  rate of the connected cumulants, which IS R-L2b's exponent"; "IF R-L2b CLOSES, THE
  EXTENSIVITY QUESTION CLOSES WITH IT." Verified verbatim (target quote exact).
- FORM D5 :254-262 + V011 (quoted FORM :81-82): the FORM's C exists ⟺ the connected
  thermodynamic/linked-cluster limit clusters; the coherent finite-N all-pairs kernel is NOT
  cluster-summable. Verified.
- R4O :104 "refuted as written ... under the H1/F'-5 chain"; :139 and :206-208
  `connected_extensivity = UNRESOLVED_BY_RL2B_REFUTING_BRANCH`. Verified. The target's
  "OPEN / refuted-as-written, no sealed replacement (ECO §4 :133-134)" is faithful.
- R4O :106 shows `X_n = C_n(V_n(a)-V_n(0))C_n` is the SEALED R-L2b notation (not the target's
  invention); the target's rendering is faithful.

WHY OVERSTATED (the byte-level object mismatch the posing does not surface): R-L2b's object
`X_n = C_n(V_n(a)-V_n(0))C_n` is built on the SEALED SEA COVARIANCE, quoted in ECO §5 :151-171
verbatim: `C(r) = (1/2) delta^3(r) I - i alpha·r/(2 pi^2 |r|^4)`, off-diagonal modulus
`1/(2 pi^2 |r|^3)`, HOMOGENEOUS DEGREE -3, evaluated by a Schatten-2 norm over the SPATIAL
one-particle space `int int d^3x d^3y |X|^2` on a LORENTZIAN CAUSAL DIAMOND with
`|D|_3 ~ L^3`, `|D|_4 ~ L^4` (RFA §4 :66-89; RFA §6 :118-121,:161). That object is
LENGTH/METRIC/SCALE-bearing. The FORM's Gate-5 kernel C, by contrast, is typed cell-indexed,
connection-only, intensive per the COUNT `N_4`, scale-free (FORM D5 :248-252; B5 :96-98). The
target presents the identification as "SAME_OBJECT at the gate" and writes the shared symbol
`C_n`, which reads as object identity. Its "role caveat" (C broader; R-L2b the load-bearing
sub-estimate; "identification is of the OBLIGATION, not of a discharged result", §4.1
:184-191) partly rescues this — but it does NOT disclose that the two objects are
type-incompatible in exactly the dimension the target polices elsewhere (SCALE/metric): the
existence-certificate it binds to C (R-L2b) lives on causal diamonds with an explicit degree
-3 kernel, whereas C is asserted scale-free. Also uncautioned: the index "n" collides — the
FORM's `n` is the WINDING, R-L2b's `X_n` index is the shrinking-cell/refinement level. The
obligation co-reference is real and sealed (ECO's binding); the OBJECT-level "same C" reading
is not shown and is in tension with the posing's own scale-free typing. VERDICT: OVERSTATED —
correct as an ECO-asserted obligation co-reference; not a shown object identity; the
scale/metric-bearing character of R-L2b's object is undisclosed.

---

## 4. ATTACK 4 — beta DISTINCT / DOES C COVERTLY NEED A SCALE  → CONFIRMED (C scale-free as typed), WITH A FLAGGED SEAM

The specific BETA_DISTINCT claim holds at the bytes:
- XSM's conversion object is a SEPARATE census row from the R_record,L form: T1 :146-147
  (U2 = internal/external conversion, "booked a rail import ... scale-capable") vs T1 :152-153
  (U4 = the FORM of R_record,L, "SPEC GAP ... a definition and no form"). Verified verbatim;
  C is the closure of U4, the conversion is U2 — different rows.
- XSM is scale + GR bearing: XSM :48-54 "does not fix ... relative to the spacetime metric or
  ell_P ... and G_4"; :80-84 `R = beta c Delta tau`; :88-92 "external side: Lorentzian
  causal-diamond / spacetime metric geometry." Verified. This consumes forbidden imports #1
  (ell_P, G_4, c) and #3 (Lorentzian spacetime metric). It is correctly fenced OUT as the
  DISTINCT node.
- C-as-typed is scale-free: FORM D5 :248-252 (intensive per N_4, additive, n-independent) and
  B5 :96-98 ("indexed by CONNECTION / HOLONOMY HISTORIES ALONE — no metric argument
  anywhere"). Verified. XSM's beta does NOT re-enter C; they cannot be the same object.

So XSM's beta conversion stays distinct and does not smuggle a metric into C. BUT a SEAM the
posing does not reconcile (same finding as Attack 3, stated for the scale fence): the target's
§6 circularity guard asserts "the Gate-5 kernel C is posed entirely on connection-only, scale-
free content", while its §4.1 binds C's EXISTENCE to R-L2b, whose object is the metric-diamond
sea covariance (ECO §5, RFA §4). Thus "C is scale-free" is sound for C-AS-TYPED, but the
existence-certification ROUTE the posing invokes is NOT scale-free. This is a disclosure gap,
not a demonstration that the posed C consumes a scale. Separately checked and CLEARED: `tau_R`
(the Duhamel/record-time window in G_L, V011 B3 / FORM :84-87) is a record-native parameter
held FIXED (ECO §2), never consumed as a length or magnitude in the posing — not a forbidden
scale. VERDICT: CONFIRMED that C is scale-free at the bytes AS POSED and the beta node is
genuinely distinct; the scale carried by the bound-to R-L2b route is flagged, not smuggled
into C.

---

## 5. ATTACK 5 — BUILT TYPING (P1–P7)  → SOUND, no node over-typed

Load-bearing spot-checks:
- P3 (im(Q_flux) = im(d_1^dagger)): genuine one-line consequence of the sealed `d_1 d_0 = 0`
  → `d_0^dagger d_1^dagger = 0` → `P_h d_1^dagger = d_1^dagger` → `Q_flux = d_1^dagger
  (d_1 d_1^dagger)^+|_{F_phys}`, image = im(d_1^dagger) (FORM D1 :146-151). TYPE-P sound. The
  three-block split uses the "Gate-3 COUNTING metric" (FORM :137) — a combinatorial cochain
  inner product, NOT a spacetime/GR metric and NOT a scale; cleared, correctly unflagged.
- P4 (Phi sole connection dependence + winding factor-out): uses `chi_n(identity) = 1` and
  "exactly one character power" (FORM D2 :159-178; B6 :107-112). Factor-out is from
  triviality-at-identity, NOT from faithfulness/injectivity. TYPE-P sound; no faithfulness
  consumed.
- P6 (FORM typing `n^2 Phi^T C Phi`, C typed): the target is MORE careful than the FORM here —
  it lists P6's ratified typing as "symmetric, PSD, intensive, additive, n-independent" and
  moves CLUSTER-SUMMABILITY OUT of the ratified frame into the GAP G1 (target :260-262, :271),
  whereas the FORM's own flag :478 folds "cluster-summable" into the typing. Cluster-
  summability IS the open obligation, so the target's placement is the correct, non-over-typed
  one. TYPE-P (typing only) sound.
- P1 (M03-ratified finite-N functional), P2 (V011 "disjoint theorem is proved", connected
  limit correctly left to G1), P5 (D3 sealed CTP identities), P7 (T1 :234-257 verified: FACTORS
  ⇒ HOLDS-FOR-ANY winding; DOES-NOT-FACTOR ⇒ no forcing today). All TYPE-P and correctly
  scoped; none claims the connected limit or the kernel value.

VERDICT: BUILT_TYPING_SOUND = YES.

---

## 6. ATTACK 6 — FORBIDDEN IMPORTS IN THE TARGET  → none in the posed target

- SCALE: C is intensive per the COUNT N_4, connection-only, n-independent; PROP(cross),
  phi_f, phi_H, `Phi_f^T C Phi_H` are scale-free (FORM D5 :248-252, B5). `tau_R` appears only
  inside quoted sealed definitions, never consumed. No ell_P / fiber radius / metric length /
  K_KK / c^2 / G_4 / beta enters the posed object. CLEARED.
- FAITHFULNESS: not used; the |n|=1-via-faithfulness route is BARRED (T1 :250-257, verified)
  and the fork criteria carry no injectivity premise. CLEARED.
- IMPORTED GR: the response carrier im(d_1^dagger) is DERIVED from `d_1 d_0 = 0` (P3), not
  imported; no metric g, KK, Einstein-Hilbert, quasilocal energy, or Lorentzian diamond metric
  in the target. CLEARED.
- CORRECTLY FENCED OUT (not in the target): XSM's beta conversion (SCALE + GR) is the DISTINCT
  node, not part of the posing (§4.2, §6).
- FLAGGED SEAM (adjacent, not imported into the posed C): the R-L2b existence-route the
  unification binds to C is scale/metric-bearing (sea covariance on causal diamonds; §3–§4
  above). This is the single place SCALE/GR sits next to C, via the unification, and the posing
  does not disclose it.

VERDICT: FORBIDDEN_IMPORTS = none in the target-as-posed.

---

## 7. FLAG BLOCK

```text
ONE_OBJECT = CONFIRMED(target §2 :50-94; the FORM's full closure n^2 Phi^T C Phi (FORM
  §0 :24-31, D5 :263-265) and the post-limit cross-block arbiter Phi_f^T C Phi_H (FORM §4.2
  :310-313,:331) are the SAME kernel C — the cross block is a partition of the same pullback,
  shown not asserted; object C (G1) is kept distinct from datum G3, target :81-94)

FORCED_FREE_CRITERIA = CONFIRMED(binary criterion correct: rank-one form is never a nonzero
  direct sum, and block-diagonal congruence M_fH -> S_f^T M_fH S_H preserves nonvanishing —
  FORM :315-331; no admissible sector-respecting congruence overlooked) ; CORRECTION(the FREE
  branch's stated consequence "factorizes only DEGENERATELY: R = R_sector ⊕ 0, other sector
  identically zero" is attached to ALL of R-i/R-ii/R-iii but is FALSE for the post-limit
  R-iii Phi_f^T C Phi_H = 0 case, which is a NON-degenerate direct sum R_flux ⊕ R_H with both
  blocks nonzero; the FORM confines the degenerate form to the finite-N rank-one anchor at
  :326-331 — target :128-133 & flag :346-348 over-merged it)

C_EQ_RL2B = OVERSTATED(the OBLIGATION co-reference is real and ECO-sealed — connected
  extensivity = R-L2b's exponent, ECO §2 :86-95; C-side FORM D5 :254-262 + V011 :81-82; status
  R4O :139,:206-208 — but it is presented as "SAME_OBJECT at the gate" writing a shared C_n,
  while R-L2b's object X_n = C_n(V_n(a)-V_n(0))C_n is built on the sealed SEA COVARIANCE
  C(r)=(1/2)delta^3(r)I - i alpha·r/(2 pi^2 |r|^4), degree -3, on Lorentzian causal diamonds
  |D|_4 ~ L^4 (ECO §5 :151-171; RFA §4 :66-89, §6 :118-121) — a SCALE/METRIC-bearing object,
  type-incompatible with the FORM's connection-only scale-free C; object identity is not shown
  and the scale mismatch is undisclosed; the winding-n vs refinement-n index collision is also
  uncautioned)

BETA_DISTINCT = CONFIRMED(C is scale-free at the bytes AS POSED: intensive per the count N_4,
  connection/holonomy-only, no metric argument — FORM D5 :248-252, B5 :96-98; XSM's beta
  conversion is a genuinely distinct, type-incompatible SCALE+GR node — separate census row
  T1 U2 :146-147 vs U4 :152-153, and consumes ell_P/G_4/c/Lorentzian-diamond metric, XSM
  :48-54,:80,:88-92 — it does not re-enter C). FLAGGED SEAM: the R-L2b existence-route the §4.1
  unification binds to C IS scale/metric-bearing (sea covariance on diamonds), so §6's "C posed
  entirely on scale-free content" holds only for C-AS-TYPED, not for the invoked
  existence-certification route; disclosure gap, not a scale smuggled into the posed C

BUILT_TYPING_SOUND = YES(spot-checked P3 im(Q_flux)=im(d_1^dagger) one-line from d_1 d_0 = 0,
  FORM :146-151; P4 winding factor-out from chi_n(identity)=1 not faithfulness, FORM :159-178;
  P6 typing-only and MORE careful than the FORM — cluster-summability correctly demoted to gap
  G1 not ratified typing; P1/P2/P5/P7 correctly scoped; the Gate-3 counting metric in P3 is a
  combinatorial inner product, not a forbidden scale/GR metric)

FORBIDDEN_IMPORTS = none in the target-as-posed (SCALE none: C intensive per count N_4,
  tau_R only inside quoted sealed defs; FAITHFULNESS none: |n|=1 route BARRED, T1 :250-257;
  GR none: im(d_1^dagger) DERIVED from d_1 d_0 = 0, no metric/KK/EH/quasilocal/diamond).
  Correctly fenced OUT: XSM beta (SCALE+GR). Flagged adjacency, not an import into C: the
  bound-to R-L2b route carries scale/metric via the sea-covariance-on-diamonds object.

POSING_VERDICT = SOUND-WITH-CORRECTIONS(
  (1) FREE_CRITERION: the post-limit Phi_f^T C Phi_H = 0 sub-case factorizes NON-degenerately
      (R_flux ⊕ R_H, both nonzero), not R = R_sector ⊕ 0; restrict the "degenerate / other
      sector identically zero" consequence to the finite-N rank-one (R-i)/(R-ii) case.
  (2) C_EQ_RL2B: recast "SAME_OBJECT at the gate" as an ECO-asserted OBLIGATION co-reference,
      not a shown object identity; disclose that R-L2b's object is scale/metric-bearing (sea
      covariance on Lorentzian causal diamonds) and is type-incompatible with the scale-free C.
  (3) SCALE fence: scope §6's "C posed entirely on scale-free content" to C-as-typed; note the
      invoked R-L2b existence-route is not scale-free.
  Core structure holds: one kernel C, the binary forced/free criterion, the built/gap typing,
  and the beta-node distinctness are all sound at the bytes.)

MACHINERY_OR_FAITHFULNESS_USED_BY_ME = no (typing/posing only; nothing computed, bounded, or
  decided; no factorization/winding verdict; no faithfulness/injectivity premise used;
  everything symbolic; seals recomputed at path; no register/tracker/plan/road/ledger/lens read)

alpha_computed = false ; proof_authorized = false ;
kappa_record_computed = false ; coupling_evaluation_authorized = false
POSE_CHECK_RESULT = SEALED.
```
