# STAGE 8 — REQUIRE-G3-CHECK: BLIND ADVERSARIAL VERIFICATION OF STAGE8_REQUIRE_BUILD_G3_FINITE_N_DATUM_V001
## BLIND ADVERSARIAL VERIFIER (REQUIRE-G3-CHECK) — CROSS-LINEAGE, DEFAULT-REFUTE — [SEALED]

Date: 2026-08-13
Role: BLIND, cross-lineage, default-REFUTE. Attacks ONE build's central NEGATIVE claim at
the bytes. Decides NOTHING about the value of any coupling / n / kappa / alpha / mu / C /
Betti number; typing/posing only; everything symbolic. No scale / faithfulness / GR imported
BY ME as authority; a refutation is required to stand on connection-only bedrock. No
register / tracker / plan / road / ledger / lens read. No git action. No register/commit/push.

---

## 0. SEALS VERIFIED AT PATH (shasum -a 256; full digests recomputed before reading)

TARGET (verified before reading; MATCHES the tasked digest):
```text
STAGE8_REQUIRE_BUILD_G3_FINITE_N_DATUM_V001.md
  1a96e0954dc440aa616894e23fc932a1a81e5eb5fc75838d01af34f466d49bfb  MATCHES-TASKED  OK
```
NAMED SOURCES (all MATCH the tasked digests and their own sidecars):
```text
STAGE8_R_RECORD_L_FORM_FABLE_V001.md ................ 5e49d2093d4ee17b...34658f37  OK
STAGE8_REQUIRE_TARGET_POSED_V001.md ................. e3c482b5facfb741...d88db784  OK
STAGE8_REQUIRE_TARGET_POSE_CHECK_V001.md ............ 86068343c6e0ac1e...f0fa47a   OK
```
CITED B1 / TRANSPORT / WRITE-CHAIN SOURCES (recomputed at path; MATCH the build's §1 table):
```text
B1A  STAGE8_B1A_CONNECTION_IDENTIFICATION_CODEX2_V001.md ..... 1b45d5a657fff30b  OK
B1B  STAGE8_B1B_SUPPORT_QUESTION_DARIO_V001.md .............. 585d309dcf4d362a  OK
B1C  STAGE8_B1C_CURRENT_DENSITY_HUNT_CODEX2_V001.md ......... f7b218cd6c7a23bb  OK
FR   STAGE8_7A_RA27_3_FRONTIER_DARIO_V001.md ............... 4d072e7671113357  OK
CV   STAGE8_7A_COUNTEREXAMPLE_CONTEST_DARIO_V001.md ......... c854c8b25dcc4e9e  OK
W    STAGE8_BARE_SURFACE_ALPHA_DETERMINATION_FABLE_V001.md .. 82e81f6e659108c0  OK
M06  STAGE8_TASK2D_SCALARIZATION_FUNCTIONAL_FORCING_...V001.md d13920e2a7687ac5  OK
```
All seals verified at path. No seal failed. No source is stale or substituted. Line spans
opened and compared one by one below.

---

## 1. THE CLAIM UNDER ATTACK

Build G3's central negative claim (build §0 :26-38, §2.4 :147-160, flag :306-340): the record
FIXES ell_j as (i) gauge-invariant (⊥ im(d_0), in H ⊕ im(d_1^dagger)); (ii) cell-local
(support(L_c) ⊆ Omega_c); (iii) conserved-current-typed (∂ell_j = 0); (iv) TOTAL-nonzero for
n != 0 (phi_f + phi_H != 0) — but LEAVES FREE the BLOCK-SPLIT (phi_f onto im(d_1^dagger) vs
phi_H onto H = ker(d_1) ∩ im(d_0)^perp), the sole of-record constraint being "not both zero".
Hence PHI_F, PHI_H each CONTINGENT on the unsupplied datum G3; the finite-N cross
Phi_f^T C_N Phi_H CONTINGENT (also needs mu != 0, node G2, UNBUILT); FINITE_N_BRANCH =
CONTINGENT — does not settle FREE, does not hand to C.

DEFAULT = REFUTE. Three attacks, each pressed at a byte span.

---

## 2. ATTACK 1 — BREAK THE CONTINGENCY (find a MISSED forcing constraint) → NO FORCING FOUND

### 2.1 Sub-attack (a): does gauge-invariance + current-conservation FORCE the flux block?

The build adds a property the FORM did not carry: "conserved-current-typed, ∂ell_j = 0"
(build §2.3 :125-131, §2.4 :150-153), sourced from B1C. The refutation hypothesis: if
conservation means d_1 ell_j = 0 (flux-FREE / closed), then combined with gauge-invariance
(⊥ im(d_0)) it would FORCE ell_j ∈ ker(d_1) ∩ im(d_0)^perp = H alone, i.e. phi_f = 0 FORCED
(single block → FREE) — refuting CONTINGENT toward FORCED-SINGLE.

Checked at the bytes. B1C I5 (:65) seals conservation as:
```text
"the admissible currents are K_G^fin = ker(B_G^T) and the distributional realization
 obeys ∂J_c = 0."
```
`ker(B_G^T)` (B_G the incidence matrix) is the DIVERGENCE-FREE / cycle condition: ∂J = 0 is
a VERTEX (boundary) identity, ∂_1 J = 0. Under the sealed complex's inner-product
identification (FORM B4 :90-94: d_0 the coboundary/incidence, its adjoint d_0^dagger the
divergence), ∂_1 = d_0^dagger, so

```text
∂ell_j = 0  ⟺  d_0^dagger ell_j = 0  ⟺  ell_j ⊥ im(d_0)  ⟺  ell_j ∈ H ⊕ im(d_1^dagger).
```

This is IDENTICAL to the gauge-invariance condition (build :85-86: gauge-invariance =
d_0^dagger ell_j = 0 = ⊥ im(d_0)). Conservation is a VERTEX/boundary condition (∂_1), NOT a
FACE/curvature condition (d_1). The refutation hypothesis is false at the bytes: conservation
is NOT d_1 ell_j = 0. It therefore imposes NOTHING on the split between H (phi_H) and
im(d_1^dagger) (phi_f); it merely re-states ell_j ∈ H ⊕ im(d_1^dagger). No flux-block forcing
either way. NO FORCING FOUND. (B1C :65; FORM B4 :90-94; build :85-86, :125-131.)

MINOR FINDING (does not refute; reinforces freedom): at the bytes conservation (∂ell_j = 0,
B1C I5) is REDUNDANT with gauge-invariance — both are exactly ⊥ im(d_0). The build lists them
as two independent FIXED properties (§2.4 (i),(iii)); they are one condition. This is a benign
typing redundancy: it removes, rather than adds, an independent constraint, so it can only
enlarge the free set. It cannot manufacture a forcing the build missed.

### 2.2 Sub-attack (b): does the dim-32 non-coboundary H-freedom, or charge/flux-access, FORCE phi_H != 0?

CV certificate (CV :132-134, :19, :244; FR :30-31, :185-189, :340): `d_0 lambda = x_alt - x_F`
is solved by exact elimination and is INCONSISTENT, so x_alt - x_F is NOT a coboundary
(∉ im(d_0)) — "physical, not gauge"; the equal-energy free set is 32-dimensional. Checked: a
NON-coboundary lies in the non-gauge complement H ⊕ im(d_1^dagger); it does NOT localize to H.
"Not in im(d_0)" is strictly weaker than "nonzero harmonic part." So the dim-32 freedom does
NOT force phi_H != 0. NO FORCING FOUND.

Charge/flux-access requirement (W :167-170, :208-209): its SEALED operative content is
ZERO-VARIATION elimination — the baseline "has zero variation under every external history"
and is eliminated "without evaluating any physical response coefficient"; the trivial class
"fails the same charge/flux-access requirement that killed the baseline." This kills only
history-INDEPENDENT writes (Phi = phi_f + phi_H = 0), i.e. it forces the TOTAL nonzero, not the
flux block. A write with phi_f = 0, phi_H != 0 still varies (under H-histories) and PASSES;
symmetrically phi_H = 0, phi_f != 0 passes. The name "charge/flux-access" is suggestive of the
flux block but the sealed content is total-variation. So it forces phi_f + phi_H != 0 and
NOTHING more — it forces neither phi_f != 0 nor phi_H != 0. The FORM concurs verbatim: "the
tangent-block statement phi_f != 0 is not proven at that strength" (FORM §4.3 :338-340). NO
FORCING FOUND. (W :167-170,:208-209; FORM §4.3 :334-343; build §3.1 :166-188.)

MINOR FINDING (does not refute; lands on the safe side): the build's parenthetical "H is
INHABITED of record (the dim-32 non-coboundary freedom lives in the non-gauge complement)"
(build :211-212) conflates inhabitation of the non-gauge complement (H ⊕ im(d_1^dagger)) with
inhabitation of H. CV/FR certify only the former. This over-reaches the cited seal, but the
VERDICT (phi_H neither forced nonzero nor provably zero → CONTINGENT) does not require H to be
provably inhabited: the record neither forces the write to read H nor seals H empty (a Betti
number, a fenced value). Contingency is unaffected.

### 2.3 Sub-attack (c): does any constraint force SINGLE-block landing (⇒ FREE-degenerate)?

The strongest refuting line available: cell-locality. If "cell-local" forced ell_j to be a
contractible loop, ell_j would be a boundary ∈ im(d_1^dagger) (a plaquette/face reading:
<∂sigma, a> = <d_1^dagger e_sigma, a>), giving phi_H = 0 FORCED → single block → FREE
(YES_FORCED_SINGLE). This is the one line that would flip the build.

Checked at the bytes and REJECTED on connection-only bedrock:
- B1B seals only `support(L_c) ⊆ Omega_c` (B1B :20, :101-105) — a CONTAINMENT law. It does
  NOT seal that a cell-local cycle bounds, i.e. it does not seal H_1(Omega_c) = 0 or that the
  inclusion Omega_c ↪ K kills homology.
- Omega_c is typed "A LORENTZ-COVARIANT CONTINUUM DIAMOND, NOT A CW OBJECT AT ALL, with its
  own uniqueness open" (B1B :26-27, :200-201); "IT IS NOT A COMPLEX" (:29); its uniqueness is
  "NOT SUPPLIED" (:186). Its contractibility is a CONTINUUM/GR (metric-diamond) property.
- To run the forcing I would have to IMPORT Omega_c's diamond contractibility as authority —
  a forbidden SCALE/GR import BY the verifier. A refutation must stand on connection-only
  bedrock; this one cannot. There is NO sealed connection-only combinatorial substitute
  (Omega_c "is not a complex"; its H_1 is not sealed).
- Independently, WHICH edges / which current density the per-cell holonomy reads is exactly
  the UNSUPPLIED datum G3 (B1C :9-12, :132-137, FREEDOMS_CONSUMED "zero versus nonzero current
  | false | no branch selected" :181; FR :306-307 support UNDERDETERMINED / current density
  UNSUPPLIED). The homological type of ell_j inside Omega_c is precisely what is not sealed.

So single-block landing is NOT forced on connection-only bedrock. NO FORCING FOUND. The build's
own fence of Omega_c's diamond structure (build §2.2 :113-119) is exactly what makes CONTINGENT
the correct verdict rather than a GR-imported FREE: had the build consumed "Omega_c is a
contractible diamond," it would have forced phi_H = 0 by an illegal import.

### 2.4 Attack 1 verdict

Every of-record constraint on ell_j — gauge-invariance, conservation (= the same ⊥ im(d_0)
condition), cell-locality (containment only), total-nonzero (zero-variation elimination) —
collectively fixes exactly `ell_j ∈ H ⊕ im(d_1^dagger)` with `phi_f + phi_H != 0`, and leaves
the H-vs-flux split entirely free. No constraint forces phi_f != 0, forces phi_H != 0, or
forces single-block landing, on connection-only bedrock. SPLIT_FORCED = NO_CONTINGENCY_CONFIRMED.
Load-bearing spans: build :85-86, :150-153; B1C :65, :132-137, :181; FORM D1 :134-157, §4.3
:334-343; W :167-170, :208-209; CV :132-134; FR :306-307; B1B :20, :26-29, :186, :200-201.

---

## 3. ATTACK 2 — THE mu / G2 CLAIM → CONFIRMED_UNBUILT

Is `mu ≡ 0 iff w_0 w_ch = 0`, and is G2 genuinely UNBUILT — or is mu != 0 forced/derivable?

- `mu ≡ 0 iff w_0 w_ch = 0`: FORM D4 :203-222 derives, on the scalarized amplitude
  `A_N = w_0 + w_ch·chi_n(h_rel)`, the exact mixed second variation
  `Hess Gamma_N = n^2 · mu(w) · Phi_tot ⊗ Phi_tot` with `mu(w) ≡ 0 iff w_0 w_ch = 0`. Sound
  algebra: if w_ch = 0 the amplitude has no connection dependence (flat); if w_0 = 0 the
  amplitude is a pure phase (|A_N| constant → zero modulus Hessian). Either way mu = 0.
  Confirmed, structural, no value used.
- G2 UNBUILT, verified at the bytes in M06:
  `UNIQUE_SCALARIZATION_FORCED = false | TYPE-R` (M06 :32);
  `RHO_PRE_PLACED = false | TYPE-U` (M06 :502);
  `U2_STATE_PORT_INSTANTIATED = false | TYPE-U` (M06 :504);
  `U2_STATE_PORT_OPEN = false | TYPE-U` (M06 :51). The record sandwich leaves a source
  OPERATOR, not a scalar (FORM B5 :96-105, B8 :120-123; W R3 :218-222) — so the weights
  (w_0, w_ch) are not even DEFINED until a state-port is instantiated.
- Is mu forced/derivable of record? NO. The weights are outputs of the unbuilt
  scalarization/state-port pair (TYPE-R/TYPE-U). Nothing of record forces both nonzero;
  nothing of record computes them. mu is neither forced nonzero nor evaluable.

MU_G2_TYPING = CONFIRMED_UNBUILT. The build's use (finite-N cross nonzero requires mu != 0,
mu ≡ 0 iff w_0 w_ch = 0, G2 UNBUILT — build §3.4 :217-238, flag :328-332) is exact.

---

## 4. ATTACK 3 — PROVENANCE (both directions) → CLEAN

The path to CONTINGENT is audited for secret consumption of the three fenced imports.

What the split verdict actually consumes (all connection-only / symbolic):
- the sealed tangent complex `d_1 d_0 = 0` and its three-block split (FORM D1 :134-157; the
  "Gate-3 counting metric" is a combinatorial cochain inner product, POSE_CHECK :250-254, not
  a spacetime/GR metric);
- gauge-invariance from abelian relative holonomy (FORM D3 :180-199; build :83-86);
- conservation as `ker(B_G^T)` = ⊥ im(d_0) (B1C :65) — incidence-only;
- total-nonzero from zero-variation elimination (W :167-170, :208-209);
- the structural fact `mu ≡ 0 iff w_0 w_ch = 0` and G2 unbuilt (FORM D4 :217-222; M06).

Fenced imports checked for secret load-bearing:
- (a) Omega_c causal CONTINUUM DIAMOND (SCALE + GR-metric; B1B :26-27, :200-201): the build
  uses ONLY the connection-only containment/cell-locality content (support(L_c) ⊆ Omega_c);
  the diamond metric/length is flagged and fenced (build §2.2 :113-119). Cell-locality is NOT
  load-bearing for the split verdict (§2.3 above shows the only way to make it load-bearing is
  to import the diamond's contractibility, which the build does NOT do). NOT consumed.
- (b) intrinsic Vol_4 measure / R-L2b sea-covariance on Lorentzian diamonds (SCALE; B1C I8
  :68; POSE_CHECK Attack 3-4 :111-130, :150-161): NOT consumed. The block-split verdict is a
  FINITE-N read that never invokes the cross-kernel C — the finite-N anchor uses the all-pairs
  `mu` used only structurally. The scale-bearing R-L2b route enters only the FORM/POSE
  identification of the POST-LIMIT kernel C (flagged by the POSE_CHECK as a scale-adjacent
  disclosure gap), which the BUILD deliberately does not reach (build §3.5 (3) :267-268 defers
  C to node G1). Only the connection-only conserved-cycle typing of the current is used
  (B1C :65). NOT consumed.
- (c) W's |n|=1-via-FAITHFULNESS result (W :161-172, verified present): correctly BARRED and
  flagged (build §3.1 note :186-188). The split verdict is n-BLIND — n factors out entirely as
  the global prefactor (FORM D2 :159-178, D5/5.1), so faithfulness plays no role. NOT consumed.

No forbidden import is secretly relied on to reach CONTINGENT. PROVENANCE = CLEAN.

---

## 5. WHAT WOULD HAVE REFUTED, AND WHY IT DID NOT

```text
REFUTE→FORCED-SINGLE (FREE) required: a sealed constraint forcing phi_f=0 or phi_H=0.
  Candidates tried: (i) conservation = d_1-closed → FALSE at bytes (B1C :65 is ker(B_G^T),
  a vertex/divergence condition = ⊥ im(d_0), redundant with gauge-invariance);
  (ii) cell-locality ⟹ contractible ⟹ boundary ∈ im(d_1^dagger) ⟹ phi_H=0 → REQUIRES importing
  Omega_c's continuum-diamond contractibility (forbidden GR-as-authority) and is unsealed on
  connection-only bedrock (B1B :26-29,:186). Neither stands.
REFUTE→FORCED-BOTH (hands to C) required: sealed constraints forcing phi_f!=0 AND phi_H!=0.
  Charge/flux-access forces only the TOTAL (W :167-170); the dim-32 non-coboundary lands in
  the non-gauge complement, not in H specifically (CV :132-134). Neither block is forced.
REFUTE→mu forced: required the record to fix w_0,w_ch both nonzero; the scalarization/state-port
  producing them is TYPE-R/TYPE-U unbuilt (M06 :32,:51,:502,:504). Not forced.
REFUTE→provenance break: required a fenced import load-bearing to CONTINGENT; none is (§4).
All refutation routes fail at the bytes. The build's CONTINGENT is the correct, conservative,
connection-only verdict.
```

Two minor imprecisions were found (§2.1: conservation listed as independent when it is
redundant with gauge-invariance; §2.2: "H inhabited" justified by non-gauge-complement
inhabitation, weaker than cited). Both land on the SAFE side of the verdict (more free / more
contingent) and neither overturns any flag. G3_BUILD_VERDICT = SOUND.

---

## 6. FLAG BLOCK

```text
SPLIT_FORCED = NO_CONTINGENCY_CONFIRMED(the block-split of ell_j is genuinely FREE of record:
  every of-record constraint — gauge-invariance (⊥ im(d_0)), conservation (∂ell_j=0 =
  ker(B_G^T) = ⊥ im(d_0), the SAME condition, B1C :65), cell-locality (containment
  support(L_c)⊆Omega_c only, B1B :20), total-nonzero (zero-variation elimination, W
  :167-170,:208-209) — collectively fixes only ell_j ∈ H ⊕ im(d_1^dagger) with phi_f+phi_H!=0
  and leaves the H-vs-flux split unconstrained; no constraint forces phi_f!=0, phi_H!=0, or
  single-block; the strongest forcing line (cell-local ⟹ contractible ⟹ phi_H=0) requires the
  forbidden import of Omega_c's continuum-diamond contractibility and is unsealed on
  connection-only bedrock, B1B :26-29,:186,:200-201. Spans: build :85-86,:150-153; B1C
  :65,:132-137,:181; FORM D1 :134-157, §4.3 :334-343; W :167-170,:208-209; CV :132-134;
  FR :306-307)

MU_G2_TYPING = CONFIRMED_UNBUILT(mu ≡ 0 iff w_0 w_ch = 0 is sound structural algebra on
  A_N = w_0 + w_ch·chi_n(h_rel), FORM D4 :203-222; w_0,w_ch are outputs of the scalarization/
  state-port pair G2, sealed unbuilt in M06: UNIQUE_SCALARIZATION_FORCED=false|TYPE-R :32,
  RHO_PRE_PLACED=false|TYPE-U :502, U2_STATE_PORT_INSTANTIATED=false|TYPE-U :504; record
  sandwich leaves a source OPERATOR not a scalar so the weights are undefined until a port is
  instantiated; mu is neither computable nor forced nonzero of record)

PROVENANCE = CLEAN(the CONTINGENT verdict consumes only connection-only/symbolic content —
  d_1 d_0 = 0 three-block split, abelian-holonomy gauge-invariance, ker(B_G^T) conservation,
  zero-variation total-nonzero, symbolic scalarization typing; (a) Omega_c causal-diamond
  metric fenced, only containment used, not load-bearing for the split; (b) Vol_4 / R-L2b
  sea-covariance NOT consumed — the split read is finite-N and never invokes the post-limit
  cross-kernel C where they would enter; (c) W's |n|=1-via-faithfulness BARRED and flagged, and
  the split verdict is n-blind, faithfulness plays no role)

G3_BUILD_VERDICT = SOUND(the central negative claim — record FIXES ell_j as gauge-invariant/
  cell-local/conserved-current-typed/total-nonzero but LEAVES FREE the block-split G3; PHI_F and
  PHI_H each CONTINGENT; finite-N cross CONTINGENT on G3 + G2/mu; FINITE_N_BRANCH = CONTINGENT,
  does not settle FREE, does not hand to C — survives all three attacks at the bytes. Two minor
  imprecisions noted and non-overturning: conservation is redundant with gauge-invariance, not
  independent (§2.1); "H inhabited" is justified by non-gauge-complement inhabitation, weaker
  than the cited seal (§2.2). Both land on the safe side of the verdict.)

MACHINERY_USED_BY_ME = no(seals recomputed at path; sealed bytes read and compared; reasoning
  is connection-only symbolic — ∂=d_0^dagger, cycle=⊥im(d_0) is combinatorial incidence bedrock,
  machinery-as-connection-bedrock not machinery-as-authority; no value of n/kappa/alpha/mu/
  Betti/coupling computed, bounded, or compared; no scale/GR/faithfulness imported as authority;
  no fixed-point/end-test/member-binding; no register/tracker/plan/road/ledger/lens read; no git
  action; no register/commit/push)

alpha_computed = false ; proof_authorized = false ;
kappa_record_computed = false ; coupling_evaluation_authorized = false
G3_CHECK_RESULT = SEALED.
```
