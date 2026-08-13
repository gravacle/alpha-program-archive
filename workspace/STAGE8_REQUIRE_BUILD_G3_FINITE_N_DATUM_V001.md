# STAGE 8 — REQUIRE-BUILD G3: THE FINITE-N DECIDING DATUM (WRITE-CHAIN SUPPORT / CURRENT-DENSITY)
## BLIND BUILDER (REQUIRE-BUILD-G3) — TRANSPORT-FIELD REALIZATION AND FINITE-N CROSS-BLOCK READ — [CLAIMED]

Date: 2026-08-13
Role: DETERMINE, do not confirm. This artifact realizes the transport-field datum (B1:
connection, support, current-density) as far as the record fixes it, states what is a
FREE input, and reads the finite-N status of the three sub-conditions of PROP(cross)
(phi_f != 0 ; phi_H != 0 ; Phi_f^T C_N Phi_H != 0). It builds ON Q-1013 and the sealed
FORM; it does NOT re-derive the FORM. No value of R_record,L, n, kappa, alpha, mu, C,
any scale, length, coefficient, spectrum, or constant is computed, bounded, estimated,
or compared. Every symbol is symbolic; every numeric string is a sealed-text quotation
or an exact structural integer.

Gates: `alpha_computed = false` ; `proof_authorized = false` ;
`kappa_record_computed = false` ; `coupling_evaluation_authorized = false`

Forbidden imports, held and audited throughout: NO SCALE (no ell_P, fiber radius,
metric length, K_KK, c^2, G_4, Lorentzian causal-diamond metric, sea-covariance);
NO FAITHFULNESS AS A PREMISE (the |n|=1-via-injectivity route is BARRED — flagged where
a sealed source invokes it); NO IMPORTED GR (no metric g, KK ansatz, Einstein-Hilbert,
quasilocal energy). Connection-only, scale-free, symbolic. No register/tracker/plan/
road/ledger/lens read.

---

## 0. VERDICT IN ONE LINE

**The record FIXES the write chain ell_j only as a gauge-invariant, cell-local,
conserved-current-typed 1-chain with nonzero total variation for n != 0 (phi_f + phi_H
!= 0); it does NOT fix the block-split of ell_j — which edges / which current density the
per-cell holonomy reads — that split is exactly the FREE datum G3, NOT SUPPLIED, with the
only of-record constraint being "not both zero." Consequently, at finite N: phi_f and
phi_H are each CONTINGENT on G3 (of record: only their non-simultaneous vanishing is
forced); the finite-N cross term Phi_f^T C_N Phi_H is CONTINGENT (present iff G3 makes the
write straddle BOTH blocks AND the unbuilt scalarization G2 makes mu != 0); the finite-N
branch is therefore CONTINGENT — the gate does NOT settle FREE of record (no sector is
provably inactive) and does NOT yet hand to the post-limit C-existence node G1 (the write
must first be shown to straddle both sectors, which G3 does not supply).**

---

## 1. SOURCES READ, SEALS VERIFIED AT PATH

All under `/Users/bgm/MB Work/alpha-program-archive/workspace/`. Full digests recomputed
by `shasum -a 256` at path this relay before reading; sidecars checked where present.

| Tag | Source | Seal (sha256) | Role |
|---|---|---|---|
| FORM | `STAGE8_R_RECORD_L_FORM_FABLE_V001.md` | `5e49d209…34658f37` MATCHES-TASKED | the FORM `n^2 Phi^T C Phi`; finite-N rank-one anchor; three-block split; §4 sector fork; G1/G2/G3 |
| POSE | `STAGE8_REQUIRE_TARGET_POSED_V001.md` | `e3c48…d88db784` MATCHES-TASKED | PROP(cross); the three conjuncts (F-i/F-ii/F-iii); G3 as the finite-N deciding datum |
| CHK | `STAGE8_REQUIRE_TARGET_POSE_CHECK_V001.md` | `860683…f0fa47a` MATCHES-TASKED | the pose-check correction: FREE-branch degeneracy holds only at the finite-N rank-one anchor |
| FR | `STAGE8_7A_RA27_3_FRONTIER_DARIO_V001.md` | `4d072e76…a38a6abc` MATCHES-FORM(FR) | the five transport fields field-by-field: connection UNDERDETERMINED (dim-32 free, non-coboundary), support UNDERDETERMINED, current density UNSUPPLIED |
| T2 | `STAGE8_7A_RA27_2_DISCHARGED_DARIO_V001.md` | `660e0c14…a975df1f` MATCHES-FORM(T2) | face-response objects; materiality criterion (flux-block-only, logically independent of the cross block) |
| CV | `STAGE8_7A_COUNTEREXAMPLE_CONTEST_DARIO_V001.md` | `c854c8b2…6cedc1e6` MATCHES-FORM(CV) | the dim-32 non-coboundary certificate: `E(x_alt)=E(x_F)=1`, `d_0 lambda = x_alt - x_F` inconsistent |
| P1/M03 | `STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_FUNCTIONAL_RESULT_V001.md` | `2cd1ffce…d79e6d0f` MATCHES-FORM(M03) | the ratified finite-N functional `F_N = P_0 + Z_N P_ch`; connection/holonomy-only; source operator |
| M06 | `STAGE8_TASK2D_SCALARIZATION_FUNCTIONAL_FORCING_PROTOCOL_RESULT_V001.md` | `d13920e2…` (via FORM B8) | scalarization unbuilt (TYPE-R/TYPE-U) — G2 |
| W | `STAGE8_BARE_SURFACE_ALPHA_DETERMINATION_FABLE_V001.md` | `82e81f6e…fc5a62010` MATCHES-FORM(W) | the one-character-power write; the charge/flux-access requirement; the n=0 elimination; the faithfulness result (BARRED) |
| B1A | `STAGE8_B1A_CONNECTION_IDENTIFICATION_CODEX2_V001.md` | `1b45d5a6…bfbf4a538` SEALED-OK | connection per-object carrier DERIVED; refinement lift on new interior edges FREE |
| B1B | `STAGE8_B1B_SUPPORT_QUESTION_DARIO_V001.md` | `585d309d…f68048b8` SEALED-OK | support containment sealed; exhaustion-vs-refinement index gap; Omega_c a Lorentz-covariant continuum diamond, uniqueness OPEN |
| B1C | `STAGE8_B1C_CURRENT_DENSITY_HUNT_CODEX2_V001.md` | `f7b218cd…5727ccd37` SEALED-OK | current-density PARTIAL: conserved-current half sealed (`J_c`, `∂J_c=0`, `S_R`, `Dens_R`); Ref_a receiver UNSUPPLIED; zero-vs-nonzero current NOT selected |

All twelve seals verified at path. No seal failed. No register/tracker/plan/road/ledger/
lens read. No git action. Output name probed before write: ABSENT.

---

## 2. DELIVERABLE 1 — THE TRANSPORT-FIELD DATUM (B1), REALIZED OF RECORD

The write is `z_j^(n)[a_j] = chi_n(h_j[a_j])`, `h_j[a] = exp(i <ell_j, a>)`; its
differential is the per-cell functional `Phi = (<ell_j, ·>)_j` on difference-branch
connection tangents (FORM D2 :159-178). The deciding datum G3 is the realization of the
three transport fields that fix `ell_j`: connection, support, current-density. Field by
field, of record:

### 2.1 CONNECTION — per-object carrier DERIVED; the refinement lift FREE

```text
FIXED OF RECORD:
 - The per-object connection carrier is the Gate-4 unit-weight covariant incidence
   connection: edge data U_e : L_s -> L_t on oriented edges, the 1-cochain a, with
   d_0 (gauge) and d_1 (curvature/flux), d_1 d_0 = 0.  [B1A §2.1-2.2 :139-178;
   FORM B4/D1 :90-94, :134-157]
 - The write is GAUGE-INVARIANT on the difference branch (abelian relative holonomy,
   W's C4).  Gauge-invariance = <ell_j, d_0 lambda> = 0 for all lambda = d_0^dagger
   ell_j = 0 = ell_j lives in the PHYSICAL block im(d_0)^perp = H (+) im(d_1^dagger),
   with NO gauge component.  [FORM D3 :180-199]

FREE INPUT (G3, of record):
 - The refinement-transport LIFT — the assignment of connection values to the new
   interior edges created under a refinement — is FREE: on the tested A2 instance it is
   free on a 32-dimensional set at fixed energy, and the difference x_alt - x_F is NOT a
   coboundary (physical, not gauge).  [FR §2.1 :174-199; CV certificate quoted in FR;
   B1A §4.2 G1 :266]  This is exactly the inhabitant of the non-gauge complement in which
   the block-split of ell_j is decided (FORM §4.1 :293-301).
```

### 2.2 SUPPORT — containment/locality SEALED; transport field UNDERDETERMINED; SCALE/GR FENCED

```text
FIXED OF RECORD (connection-only content):
 - support(L_c) is contained in Omega_c: the write's interaction density is CELL-LOCAL
   (a containment law, per incidence).  [B1B §1.2(i) :101-106]
 - one-use support leaves completed record factors exactly invariant.  [B1B §1.2, item 5]

FREE / UNDECIDABLE_FROM_STOCK (G3):
 - The support TRANSPORT field over the working refinement class is UNDERDETERMINED: the
   sealed support law is indexed by the causal EXHAUSTION (growing volume), while the
   refinement carrier Ref_a is indexed by SUBDIVISION; no sealed object bridges the two
   indices.  Omega_c's own uniqueness is OPEN of record.  [B1B lead + §2.2 :157-170,
   §4 :247-260; FR §2.3 :228-235 "support UNDERDETERMINED, structurally immediate,
   unsealed"]

FORBIDDEN-IMPORT FLAG (fenced OUT, NOT consumed):
 - Omega_c is typed of record as "a Lorentz-covariant CONTINUUM DIAMOND, NOT A CW OBJECT
   AT ALL" (B1B §3.2 :200-201).  That is a SCALE + GR-metric object (causal-diamond
   metric).  I use ONLY the connection-only containment/locality content of the support
   field (cell-locality of ell_j); I do NOT import the diamond metric, its length, or the
   exhaustion-scale.  The support field's scale/GR-bearing realization is held at arm's
   length and does not enter the block-split read below.
```

### 2.3 CURRENT DENSITY — conserved-current half SEALED; density receiver UNSUPPLIED; zero-vs-nonzero NOT selected

```text
FIXED OF RECORD (connection-only content):
 - A finite conserved-current object J_c exists: J_c in K_G^fin = ker(B_G^T), obeying the
   distributional conservation identity ∂J_c = 0, with an incidence-preserving old-current
   transport S_R and a law-only positive density relation Dens_R dual to the coframe.
   [B1C §1-2 :47-121]  This types ell_j as a CONSERVED-CURRENT (cycle) object:
   ∂ell_j = 0 half sealed.

FREE / UNSUPPLIED (G3):
 - There is NO single Ref_a-indexed current-density receiver, NO Ref_a<-Ref_path bridge,
   and NO inhabited coframe/Vol_4/support-compatible density transport.  Verdict PARTIAL:
   2 satisfied / 2 failed / 5 undecidable.  [B1C §3 :123-149, §4 :151-172]
 - The zero-versus-nonzero current branch is EXPLICITLY NOT SELECTED: freedom
   "zero versus nonzero current | false | no branch selected".  [B1C §4.1 :173-189]

FORBIDDEN-IMPORT FLAG (fenced OUT): the current-density interface item I8 references the
intrinsic Vol_4 measure and the exact-quadratic energy Q_K; the R-L2b existence route for
the connected limit is built on the SEA COVARIANCE on Lorentzian causal diamonds (scale/
metric-bearing, per CHK Attack 3-4).  Neither the Vol_4 metric normalization nor the
sea-covariance-on-diamonds is consumed here; the block-split read uses only the
connection-only current typing (ell_j a conserved cycle).
```

### 2.4 What the record fixes vs. what is free — consolidated

```text
FIXED (of record): ell_j is (i) GAUGE-INVARIANT — no im(d_0) component, lives in
   H (+) im(d_1^dagger); (ii) CELL-LOCAL — support(L_c) subset Omega_c; (iii)
   CONSERVED-CURRENT-typed — ∂ell_j = 0 (the conserved half sealed); (iv) TOTAL-NONZERO
   for n != 0 — phi_f + phi_H != 0 (from the n=0 zero-variation elimination; §3.1 below).

FREE (datum G3, NOT SUPPLIED): the BLOCK-SPLIT of ell_j — the projection weights of the
   write chain onto the flux block im(d_1^dagger) (= phi_f) vs. the flux-free physical
   block H (= phi_H).  Equivalently, WHICH edges / WHICH current density the per-cell
   holonomy reads.  The only of-record constraint on the split is NOT-BOTH-ZERO.
   No sealed object fixes the split either way (FORM §4.3 :340-342).
```

---

## 3. DELIVERABLES 2-4 — THE FINITE-N READ OF THE THREE SUB-CONDITIONS

### 3.1 The of-record constraint on the split: phi_f + phi_H != 0 (not both zero)

The n=0 elimination is sealed to run on ZERO VARIATION, not on flux specifically:
W (S4 §4.1, verbatim via W :166-172): the baseline `U_N^base` "has zero variation under
every external history" and is eliminated "without evaluating any physical response
coefficient"; the "charge/flux-access requirement" (W :207-209) is the SAME test that
"killed the baseline." Reading its operative content at the tangent-block level:

```text
A write FAILS the requirement  <=>  Phi = phi_f + phi_H = 0 (history-independent).
Therefore, for every admitted n != 0:  phi_f + phi_H != 0.        [OF RECORD]
```

This forbids the simultaneous vanishing phi_f = 0 AND phi_H = 0, and nothing more. The
name "charge/flux-access" is suggestive of the flux block, but the SEALED content is
zero-variation elimination — the FORM is correct that "phi_f != 0 is not proven at that
strength" (FORM §4.3 :340). A write with phi_f = 0, phi_H != 0 still varies under H-block
(homology) histories and so PASSES the requirement; a write with phi_H = 0, phi_f != 0
passes symmetrically. The requirement discriminates the TOTAL, not the blocks.

Note (FAITHFULNESS, BARRED): W :161-172 also carries "Faithfulness forces unit winding
... faithful means unit winding." That is the |n|=1-via-injectivity route. It is BARRED
by the fences and is NOT consumed here; it plays no role in the split read.

### 3.2 DELIVERABLE 2 — phi_f (flux block im(d_1^dagger))

```text
PHI_F = CONTINGENT.
 Exact condition: phi_f != 0  <=>  the FREE write-chain support/current-density
 realization (G3) gives ell_j a nonzero projection onto the flux block im(d_1^dagger)
 (equivalently, ell_j carries a nonzero BOUNDARY / flux-reading part <∂sigma,a> = flux
 through sigma).  NOT forced nonzero (the charge/flux-access requirement forces only the
 TOTAL phi_f + phi_H != 0, not the flux block specifically — §3.1); NOT provably zero
 (nothing seals ell_j into H alone).  [FORM §4.3 :334-343; W :166-172, :207-209]
```

### 3.3 DELIVERABLE 3 — phi_H (flux-free physical block H)

```text
PHI_H = CONTINGENT.
 Exact condition: phi_H != 0  <=>  the FREE write-chain realization (G3) gives ell_j a
 nonzero projection onto the flux-free physical block H = ker(d_1) ∩ im(d_0)^perp
 (equivalently, ell_j carries a nonzero nontrivial-cycle / homology part — the direction
 the dim-32 non-coboundary freedom inhabits).  The FORM states this verbatim: phi_H != 0
 "is exactly datum G3, NOT SUPPLIED of record.  No sealed object forces it either way"
 (FORM §4.3 :340-342).  H is INHABITED of record (the dim-32 physical, non-coboundary
 freedom lives in the non-gauge complement — FORM §4.1 :299-301; FR §2.1 :184-190; CV),
 so phi_H is NOT provably zero; but whether the write READS H is the unsupplied G3 datum,
 so phi_H is NOT forced nonzero.
```

### 3.4 DELIVERABLE 4 — the finite-N cross term Phi_f^T C_N Phi_H

At finite N the coherent kernel is the ALL-PAIRS weight `C_jk^(finite,coherent) = mu` for
all j,k, so the finite-N Hessian is the rank-one `n^2 mu (phi_f + phi_H) ⊗ (phi_f + phi_H)`
and the cross block is `n^2 mu · phi_f ⊗ phi_H` (FORM D4 :215-231, §4.2 :315). Its one
structural property: `mu ≡ 0 iff w_0 w_ch = 0` (either source-sector weight vanishes;
FORM D4 :222). The sector weights (w_0, w_ch) are the scalarization/state-port pair G2,
sealed UNBUILT (`CANONICAL_SCALAR_..._ALONE = false | TYPE-R`; `U2_STATE_PORT_INSTANTIATED
= false | TYPE-U`; FORM B8 :120-123; M06).

```text
FINITE_N_CROSS = CONTINGENT.
 Phi_f^T C_N Phi_H = n^2 mu · phi_f ⊗ phi_H is nonzero  <=>  ALL THREE hold:
   (F-i)  phi_f != 0        — G3 gives ell_j a flux-block part            [CONTINGENT, §3.2]
   (F-ii) phi_H != 0        — G3 gives ell_j an H-block part              [CONTINGENT, §3.3]
   (mu)   mu != 0 i.e. w_0 w_ch != 0 — G2 gives both source-sector weights nonzero
                                                                          [UNBUILT, TYPE-R/U]
 It is ZERO of record whenever G3 puts the write in a SINGLE block (phi_f=0 xor phi_H=0,
 which the of-record not-both-zero constraint permits) OR the unbuilt scalarization gives
 mu = 0.  Neither eventuality is settled of record; hence CONTINGENT, not PRESENT and not
 provably ZERO.
```

### 3.5 DELIVERABLE 5 — the finite-N branch verdict

```text
FINITE_N_BRANCH = CONTINGENT.

 NOT FREE:  no sector is inactive OF RECORD.  The only of-record constraint on the split
   is phi_f + phi_H != 0 (not both zero, §3.1); it makes NEITHER phi_f NOR phi_H provably
   zero, so the gate cannot settle FREE cheaply.  (A single-block write — phi_f=0 or
   phi_H=0 — WOULD give the degenerate FREE factorization R = R_sector (+) 0 at the
   finite-N rank-one anchor, per CHK's correction that the degenerate consequence holds
   only there; but no sealed object selects a single-block write.)

 NOT HANDS-TO-C-LIMIT:  that verdict requires BOTH sectors AND the finite-N cross FORCED
   nonzero, leaving only the post-limit C-existence node G1.  Here phi_f, phi_H, and mu
   are all contingent/unbuilt, so the question does NOT yet reduce to G1.  The write must
   first be shown to STRADDLE both blocks (G3) and the scalarization must give mu != 0
   (G2) before the post-limit cross-pairing Phi_f^T C Phi_H (G1) becomes the residual
   question.

 EXACT FREE-INPUT CONDITION THAT DECIDES THE BRANCH:
   (1) G3 — the write-chain support/current-density realization: does the per-cell write
       chain ell_j straddle BOTH the flux block im(d_1^dagger) (phi_f != 0) AND the
       flux-free physical block H (phi_H != 0)?  NOT SUPPLIED; only "not both zero" is
       forced.  If it lands in one block => FINITE_N_BRANCH = FREE (degenerate).  If it
       straddles both => proceed to (2)/(3).
   (2) G2 — the scalarization/state-port pair: is mu != 0 (w_0 w_ch != 0)?  UNBUILT.  If
       mu = 0 => finite-N cross vanishes (degenerate) even with a straddling write.
   (3) THEN, and only then, the post-limit cross-block verdict hands to G1 (whether the
       Gate-5 cluster kernel C annihilates the cross pairing).
```

---

## 4. WHAT THIS DOES NOT SAY / OVERCLAIM AUDIT

```text
IT DOES NOT decide FORCED vs FREE: it reads the finite-N status of the three PROP(cross)
   sub-conditions and returns CONTINGENT.  PROP(cross) is neither asserted nor denied.
IT DOES NOT compute mu, C, w_0, w_ch, phi_f, phi_H, any spectrum, or any value; mu's one
   used property (≡ 0 iff w_0 w_ch = 0) is structural and sealed.
IT DOES NOT flatten "G3 not supplied" into "phi_H = 0": H is inhabited of record and the
   write's reading of it is genuinely open — CONTINGENT, not ZERO.
IT DOES NOT flatten the charge/flux-access requirement into "phi_f != 0": the sealed
   content is zero-variation (total) elimination; the flux-block specificity is NOT
   sealed (FORM §4.3 concurs) — so phi_f is CONTINGENT, not FORCED.
IT DOES NOT import GR, a metric, a KK ansatz, or a quasilocal object: the block-split runs
   entirely on the connection-only tangent complex; Omega_c's causal-diamond metric and
   the Vol_4 / sea-covariance normalizations are FLAGGED and fenced OUT (§2.2, §2.3).
IT DOES NOT consume faithfulness: W's |n|=1-via-faithfulness result is BARRED and flagged
   (§3.1), and plays no role.
IT DOES NOT use scale: 32, 24, 16, dim-1 are exact structural integers or sealed
   quotations; tau_R, Vol_4, causal-diamond length appear only inside quoted sealed
   context, never consumed.
YOURS assemblies, marked: the tangent-block reading of the charge/flux-access requirement
   as total-variation (not flux-block) elimination (§3.1); the identification of phi_f
   with ell_j's boundary/flux part and phi_H with its homology part via gauge-invariance
   (§2.1, §3.2-3.3); the three-way CONTINGENT typing of the finite-N cross (§3.4); the
   branch trichotomy placement (§3.5).  Each runs on quoted sealed identities; none
   consumes an unsealed value.
```

---

## 5. FLAG BLOCK

```text
TRANSPORT_DATUM = the record FIXES ell_j as gauge-invariant (⊥ im(d_0), lives in
  H (+) im(d_1^dagger)), cell-local (support(L_c) ⊆ Omega_c), conserved-current-typed
  (∂ell_j = 0 half sealed), total-nonzero for n != 0 (phi_f + phi_H != 0); it LEAVES FREE
  (datum G3, NOT SUPPLIED) the block-split of ell_j — which edges / which current density
  the per-cell holonomy reads, i.e. the projection weights onto im(d_1^dagger) (phi_f) vs
  H (phi_H) — with the sole of-record constraint "not both zero".  [FORM D2 :159-178,
  D3 :180-199, §4.1-4.3 :293-343; B1A :139-178,:266; B1B :101-106,:157-170,:200-201;
  B1C :47-121,:151-189; FR :174-235; W :166-172,:207-209]

PHI_F = CONTINGENT(phi_f != 0 <=> the free write-chain realization G3 gives ell_j a
  nonzero projection onto the flux block im(d_1^dagger) / a nonzero boundary-flux part;
  the charge/flux-access requirement forces only the TOTAL phi_f + phi_H != 0, not the
  flux block specifically — FORM §4.3 :340; W :166-172,:207-209; not provably zero, not
  forced nonzero)

PHI_H = CONTINGENT(phi_h != 0 <=> the free write-chain realization G3 gives ell_j a
  nonzero projection onto the flux-free physical block H = ker(d_1) ∩ im(d_0)^perp / a
  nonzero homology part; "exactly datum G3, NOT SUPPLIED of record.  No sealed object
  forces it either way" — FORM §4.3 :340-342; H inhabited by the dim-32 non-coboundary
  freedom, FORM §4.1 :299-301, FR §2.1 :184-190, CV; not provably zero, not forced
  nonzero)

FINITE_N_CROSS = CONTINGENT(Phi_f^T C_N Phi_H = n^2 mu · phi_f ⊗ phi_H at finite N, with
  the all-pairs coherent kernel C_jk = mu; nonzero iff phi_f != 0 [G3] AND phi_H != 0 [G3]
  AND mu != 0, where mu ≡ 0 iff w_0 w_ch = 0 and the scalarization/state-port pair G2 is
  UNBUILT (TYPE-R/TYPE-U); ZERO of record whenever G3 puts the write in a single block or
  G2 gives mu = 0 — FORM D4 :215-231, §4.2 :315, B8 :120-123)

FINITE_N_BRANCH = CONTINGENT(exact free-input condition: (1) G3 — does the per-cell write
  chain straddle BOTH im(d_1^dagger) (phi_f != 0) AND H (phi_H != 0)?  NOT SUPPLIED, only
  "not both zero" forced — a single-block landing gives FREE (degenerate R_sector (+) 0 at
  the finite-N rank-one anchor); (2) G2 — is mu != 0 (both source-sector weights nonzero)?
  UNBUILT; (3) only if (1) and (2) both hold does the post-limit cross-block verdict hand
  to the C-existence node G1.  The gate does NOT settle FREE of record (no sector provably
  inactive) and does NOT yet hand to G1 (both sectors not forced nonzero).)

FORBIDDEN_IMPORTS = none consumed.  FLAGGED and fenced OUT (not imported into the read):
  (a) Omega_c, the Lorentz-covariant causal CONTINUUM DIAMOND of the support field
  (SCALE + GR-metric; B1B :200-201) — only its connection-only cell-locality content used;
  (b) the intrinsic Vol_4 measure and the R-L2b sea-covariance-on-Lorentzian-diamonds
  existence route referenced by the current-density interface (SCALE/metric; B1C I8, CHK
  Attack 3-4) — not consumed;
  (c) W's |n|=1-via-FAITHFULNESS result (BARRED; W :161-172) — flagged, not consumed.

MACHINERY_INVOKED = no (no fixed-point execution, no end test, no member binding, no
  numeric evaluation, no response/junction/common-cell evaluation; typing/read only;
  everything symbolic; seals recomputed at path; no register/tracker/plan/road/ledger/
  lens read; no git action; output name probed ABSENT before write)

alpha_computed = false ; kappa_record_computed = false ; proof_authorized = false ;
coupling_evaluation_authorized = false
ALL_RESULTS = CLAIMED until the adversarial panel.
```
