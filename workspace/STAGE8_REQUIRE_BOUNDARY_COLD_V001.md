# STAGE 8 — DOES THE DERIVED CONNECTION-ONLY BOUNDARY FORCE phi_H? BLIND COLD RE-DERIVATION
## REQUIRE-BOUNDARY-COLD — cross-lineage, independent verdict — [CLAIMED]

Date: 2026-08-13
Role: BLIND COLD RE-DERIVER. I received the objects and the QUESTION only. I did NOT
open any prior answer to this question (no BUILD_BOUNDARY_SPLIT, no BOUNDARY_CHECK, no
register/tracker/plan/road/ledger/lens). The verdict below is my own, derived from the
record's sealed connection-only content.

Gates: `alpha_computed = false` ; `proof_authorized = false` ;
`kappa_record_computed = false` ; `coupling_evaluation_authorized = false`

Fences held throughout: connection-only, scale-free, symbolic. NO scale (no ell_P,
K_KK, c^2, metric length, quasilocal energy, Lorentzian diamond). NO faithfulness as a
premise. NO imported GR — GR's boundary structure is used ONLY as derived from the
record's own complex, and where imported GR objects appear in the sources they are
consumed only for their connection-only content or flagged as excluded.

---

## 1. SOURCES READ, SEALS VERIFIED AT PATH

All under `/Users/bgm/MB Work/alpha-program-archive/workspace/`. Full digests
recomputed by `shasum -a 256` before reading; each MATCHES its sidecar / tasked digest.

| # | Source | Seal | Role |
|---:|---|---|---|
| RF | `STAGE8_R_RECORD_L_FORM_FABLE_V001.md` | `5e49d209…658f37` MATCHES-TASKED | the three-block split A^1 = im(d_0) ⊕ H ⊕ im(d_1^dagger); H = ker(d_1)∩im(d_0)^perp (dim-32, non-coboundary); im(Q_flux)=im(d_1^dagger); the write functionals Phi with components phi_f, phi_H; the finite-N total-only forcing |
| EB | `STAGE8_EMERGENT_BOUNDARY_WINDING_FABLE_V001.md` | `e6fae142…3ca6ee` SEALED-OK | the six derived boundary legs (E1 exterior shape, E2 volume transport, E3 coframe, E4 face-response, E5 conservation dF=0, E6 two-branch CTP); geometric half winding/character-blind; face-response bulk |
| RA2 | `STAGE8_7A_RA27_2_DISCHARGED_DARIO_V001.md` | `660e0c14…975df1f` SEALED-OK | the sealed face-response spans: Q_flux lift "orthogonal to ker(d_1) ∩ im(d_0)^perp"; the materiality criterion Q_flux^† R_record,L Q_flux = c_L G_(2,ell) on F_phys; the dim-32 freedom leaves the measure's value unchanged |
| FX | `STAGE8_7A_FLUX_CORRESPONDENCE_DARIO_V001.md` | `3c6cd9a2…744c0b` SEALED-OK | dF=0 makes ∫F a topological invariant independent of the source; the conservation leg forces nothing about the flux-class datum |
| FR | `STAGE8_7A_RA27_3_FRONTIER_DARIO_V001.md` | `4d072e76…a38a6abc` SEALED-OK | the dim-32 physical, non-gauge assignment freedom; support and current density NOT SUPPLIED |
| SF | `STAGE8_SADDLE_FOUNDATION_PARENT_ACTION_DARIO_V001.md` | `1d11f150…effc775` SEALED-OK | connection-only interior; the one-argument import-block at g (no metric argument anywhere) |

No register, tracker, plan, road, ledger, or lens file read. No prior answer to this
question read. No git action. Output name probed before write: ABSENT.

---

## 2. THE OBJECTS, RESTATED ON THE RECORD'S OWN COMPLEX

From the sealed complex `d_1 d_0 = 0` (RF D1, quoting V011 B4), orthogonally in the
sealed Gate-3 counting metric:

```text
A^1 = im(d_0)  ⊕  H  ⊕  im(d_1^dagger)
  im(d_0)        = exact / pure gauge (coboundaries)
  H              = ker(d_1) ∩ im(d_0)^perp   -- the FLUX-FREE physical block,
                                                dim 32, non-coboundary (a genuine
                                                cohomology class H^1: harmonic)
  im(d_1^dagger) = ker(d_1)^perp             -- the FLUX-CARRYING physical block (coexact)
```

`d_1` is the flux/curvature operator; the EM field is `F = d_1 a`, `F_phys = im(d_1)`.
The write differentials are `Phi = (<ell_j, ·>)_j`; `phi_f` and `phi_H` are the
`im(d_1^dagger)`- and `H`-components of the write functional. Of record the (finite-N)
write forces only the TOTAL `phi_f + phi_H != 0`; the split is free (RF D4, 4.3).

The DERIVED connection-only boundary legs (EB §3), each posed as a candidate detector:

```text
E1 exterior shape        (G1, geometric) -- T_R-keyed shape content, per cell
E2 volume transport      (G1, geometric) -- per-cell measure V_cell·sum F^2, exact additivity
E3 child-intrinsic coframe(G1, geometric) -- diag(ell/2) from the child's own extents
E4 face-response         (G2, dynamical) -- mathcal_K_L(xi,zeta) = R_record,L(Q_flux xi, Q_flux zeta)
E5 conservation dF=0     (G3)            -- EM Bianchi closedness; the flux class of the boundary
E6 two-branch CTP algebra                -- the doubled contour; carries a_Delta = a_+ - a_-
```

---

## 3. LEG-BY-LEG SENSITIVITY TO THE H-BLOCK [PROVABLE on the sealed complex]

### 3.1 Face-response E4 — reads phi_f ONLY, orthogonal to H by construction

The sealed lift span (RA2 §3.1, V011 `aa7c6d49…[44961,45186)`): for every `xi in
F_phys`, `Q_flux xi` is the unique horizontal, minimum-norm lift **"orthogonal to
ker(d_1) ∩ im(d_0)^perp"** — i.e. orthogonal to `H` verbatim — with `im(Q_flux) =
im(d_1^dagger)` (RF D1). Therefore

```text
mathcal_K_L(xi,zeta) = R_record,L(Q_flux xi, Q_flux zeta)   with Q_flux xi, Q_flux zeta in im(d_1^dagger),
```

so the face-response pairs only `im(d_1^dagger)` directions and never inserts an `H`
direction into `R_record,L`. Pulling the write functional through the response reads
`phi_f = <Phi, im(d_1^dagger)>` and is IDENTICALLY INDEPENDENT of `phi_H`. The sealed
materiality criterion (RA2 §3.2, F-b) is `Q_flux^† R_record,L Q_flux = c_L G_(2,ell)`
**on F_phys** — a statement about the flux block alone (`Phi_f^T C Phi_f`), with no `H`
argument. E4 is BLIND to H.

### 3.2 Conservation E5 (dF=0) — vacuous on H

`H subset ker(d_1)`, so `d_1(H) = 0`: any write component in `H` produces `F = 0` —
zero curvature, zero EM field. The conservation leg constrains the flux `F = d_1 a` and
its topological class; FX derives that `dF = 0` makes `∫F` a source-independent
topological invariant. On the `H` direction there is no `F` to constrain. E5 is
satisfied vacuously for every value of `phi_H`. BLIND to H.

### 3.3 Geometric legs E1/E2/E3 — character-free, and E2 sealed-invariant under H

EB §5 states the geometric half "contains no character data at all" — the write
functional `Phi` (whose components are `phi_f, phi_H`) is exactly the character/
connection data, which these legs do not carry. Sharper, of record: RA2 §1.7 seals
that the dim-32 freedom "moves the assignment and **leaves the measure's value
unchanged**." The dim-32 freedom IS the `H` block (RF D1; FR: physical, non-gauge,
dim 32). So the volume transport E2 is PROVABLY invariant under motion in `H`, and by
the same character-free typing so are E1 shape and E3 coframe. BLIND to H.

### 3.4 Two-branch CTP E6 — carries the total, does not resolve the H-component

The doubled algebra carries the difference-branch functional `phi_j[(a_+,a_-)] =
<ell_j, a_Delta>` (RF D3). This is the TOTAL write functional on the doubled tangent;
the CTP structure nowhere decomposes it across `H ⊕ im(d_1^dagger)`. It is a doubling
of the contour, not a projector onto `H`. Not an H-probe.

### 3.5 Why the blindness is structural, not incidental

`H = ker(d_1) ∩ im(d_0)^perp` is the harmonic middle block — the cohomology `H^1` of
the record's tangent complex. Its defining property is: **simultaneously flux-free
(`d_1 H = 0`, no curvature) and non-gauge (`im(d_0)^perp`, not removable by gauge).**
The counterexample certificate (RF B7 / CV: `d_0 lambda = x_alt - x_F` inconsistent)
proves H is a NONZERO cohomology class. A nonzero harmonic class has zero curvature
everywhere yet nonzero periods — it is detected ONLY by a global holonomy/period
pairing over a non-contractible cycle, never by a local curvature/flux signature.
Every derived boundary leg is either (i) a flux/curvature signature (E4 via `Q_flux ->
im(d_1^dagger)`; E5 via `F = d_1 a`), which annihilates H, or (ii) a character-free
geometric/measure signature (E1/E2/E3), which the physical H-freedom leaves invariant.
The span visible to the derived boundary is exactly `im(d_1^dagger)` (phi_f); H is the
boundary's structural blind spot.

---

## 4. CAN ANY CONNECTION-ONLY BOUNDARY OBJECT CONSTRAIN phi_H? [PROVABLE]

No. Section 3 shows every sealed derived boundary leg is independent of `phi_H`. So no
boundary-local, connection-only object depends on `phi_H`, and none can constrain it —
directly or indirectly:

- **No direct constraint:** each leg's value is a function of `phi_f` and geometric/
  measure data only.
- **No indirect constraint via forcing phi_f = 0:** forcing `phi_H != 0` from the total
  would require the boundary to force `phi_f = 0` while the total stays nonzero. But the
  total-only forcing `phi_f + phi_H != 0` is a RECORD (finite-N) fact, not a boundary
  object; and no boundary leg forces `phi_f = 0` — the face-response and the
  charge/flux-access reading point the write TOWARD the flux block if anywhere, never
  away from it. So the indirect route does not force `phi_H` either.

What WOULD determine `phi_H` is a NON-boundary-local object, and it is connection-only,
not an import:

```text
O(G3) the write chains' support / current-density realization ell_j -- which interior
      edges the per-cell holonomy reads. This fixes the decomposition of the write
      direction across H ⊕ im(d_1^dagger), hence phi_H. RA27-3's `support` and
      `current density` fields are NOT SUPPLIED (FR). It is a BULK / interior connection
      datum, NOT a boundary signature; connection-only, NO metric/GR/scale import.
O(per) a global period / holonomy pairing over a non-contractible cycle of the complex
      -- the only object that pairs nontrivially with the harmonic class H. Also
      BULK / global-topological, connection-only, NOT a boundary-local object.
```

Neither requires a metric, GR datum, faithfulness, or scale. The determination of
`phi_H` is a connection-only question; it is simply not answerable at the boundary.

---

## 5. VERDICT

The derived connection-only boundary structure does NOT force `phi_H != 0`. It CANNOT:
it is structurally blind to the entire `H` block (every leg proven independent of
`phi_H` in §3). A structure that cannot detect `phi_H` cannot require it nonzero; every
boundary leg is satisfied identically for `phi_H = 0` and for any `phi_H`. The derived
boundary leaves `phi_H` FREE. Whatever "require"-shaped pressure the boundary exerts
lands on the flux block `phi_f` (the only span it sees), never on `phi_H`. The actual
occupancy of `H` by the write is decided only by a bulk, connection-only object — the
write-chain support realization (or, equivalently for detection, a global period
pairing) — outside the boundary-local, curvature/flux-based structure.

This verdict consumes no scale, no faithfulness, no imported GR; it runs on the sealed
complex `d_1 d_0 = 0`, the orthogonal decomposition, the sealed `Q_flux`-lift
orthogonality to `H`, and `d_1 H = 0`.

---

## 6. FINAL FLAG BLOCK

```text
H_VISIBLE_TO_BOUNDARY = NO (structurally invisible). H = ker(d_1) ∩ im(d_0)^perp is the
  harmonic middle block (cohomology H^1): simultaneously flux-free (d_1 H = 0) and
  non-gauge. Every derived boundary leg is blind to it. Face-response E4: the sealed
  Q_flux lift is "orthogonal to ker(d_1) ∩ im(d_0)^perp" = orthogonal to H, im(Q_flux) =
  im(d_1^dagger), so mathcal_K_L = R_record,L(Q_flux ., Q_flux .) reads only phi_f and
  is identically independent of phi_H; the materiality criterion lives on F_phys /
  Phi_f^T C Phi_f alone. Conservation E5 (dF=0): H carries F = d_1 a = 0 -- zero flux --
  so the leg is vacuous on H. Geometric legs E1 shape / E2 volume transport / E3 coframe:
  character-free, and the volume transport is sealed-invariant under the dim-32 freedom,
  which IS the H block (RA2 §1.7). Two-branch CTP E6: carries only the total difference-
  branch functional <ell_j, a_Delta>, does not resolve the H-component. SPAN VISIBLE TO
  THE BOUNDARY = im(d_1^dagger) (phi_f) only; the flux-free block H is the blind spot.

BOUNDARY_FORCES_PHI_H = NO_FREE. The derived boundary cannot force phi_H because it
  cannot detect phi_H (proven blindness of all six legs, §3). Every leg is satisfied
  identically for phi_H = 0 and for any phi_H; no boundary object depends on phi_H. The
  total-only condition phi_f + phi_H != 0 is a finite-N RECORD fact, not a boundary
  object, and no boundary leg forces phi_f = 0, so there is no indirect forcing route
  either. Any require-shaped pressure the boundary exerts lands on the flux block phi_f,
  never on the flux-free H. The derived boundary leaves phi_H FREE.

FORCING_NEEDS_BULK_OR_IMPORT = BULK, connection-only (NOT import). Determining phi_H
  requires a NON-boundary-local object: the write chains' support / current-density
  realization ell_j (which interior edges the per-cell holonomy reads; fixes the write
  direction's decomposition across H ⊕ im(d_1^dagger); RA27-3 fields NOT SUPPLIED) -- a
  bulk/interior connection datum, not a boundary signature. The only alternative
  detector of the harmonic H is a global period/holonomy pairing over a non-contractible
  cycle -- also bulk/global-topological, connection-only. Neither needs a metric, GR
  datum, faithfulness, or scale.

FORBIDDEN_IMPORTS = none. Argument uses only d_1 d_0 = 0, the orthogonal decomposition,
  the sealed Q_flux-lift orthogonality to H, and d_1 H = 0 -- all connection-only,
  scale-free, symbolic. No metric, no imported GR, no faithfulness premise, no scale
  (no ell_P, K_KK, c^2, quasilocal energy, Lorentzian diamond); T_R appears only inside
  quoted sealed shape statements; every integer (32) is an exact structural quotation.

CONTAMINATED = no. No prior answer to this question read (no BUILD_BOUNDARY_SPLIT, no
  BOUNDARY_CHECK); no register/tracker/plan/road/ledger/lens read; seals verified at
  path before reading; no git action; output name probed ABSENT before write.

alpha_computed = false ; proof_authorized = false ;
kappa_record_computed = false ; coupling_evaluation_authorized = false
ALL_RESULTS = CLAIMED until the adversarial panel check.
```
