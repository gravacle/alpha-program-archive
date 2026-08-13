# STAGE 8 — REQUIRE-G3 COLD RE-DERIVATION: THE FINITE-N CROSS-BLOCK Phi_f^T C_N Phi_H
## BLIND COLD RE-DERIVER — codename REQUIRE-G3-COLD — cross-lineage — [CLAIMED]

Date: 2026-08-13
Role: INDEPENDENT COLD VERDICT on ONE object only — the finite-N cross-block between
the flux sector im(d_1^dagger) (amplitude phi_f) and the flux-free physical sector
H = ker(d_1) ∩ im(d_0)^perp (amplitude phi_H). Derived from the objects and the
QUESTION alone. No other party's answer was read (the two named REQUIRE/G3 datum/check
files were NOT opened; no register/tracker/plan/road/ledger/lens file was read).

Gates held: `alpha_computed = false` ; `proof_authorized = false` ;
`kappa_record_computed = false` ; `coupling_evaluation_authorized = false`.

Fences held throughout: CONNECTION-ONLY, SCALE-FREE, symbolic. No value of any
coupling / n / kappa / alpha. NO scale (no ell_P, R, K_KK, c^2, metric length,
Lorentzian diamond, sea-covariance). NO faithfulness premise (|n| = 1 via injectivity
is BARRED and not consumed). NO imported GR. mu and C left symbolic.

---

## 0. VERDICT IN ONE LINE

**The finite-N cross-block is `Phi_f^T C_N Phi_H = n^2 · mu · Phi_{f,tot} · Phi_{H,tot}`
(rank-one coherent kernel `C_N,jk = mu` for all j,k). It is CONTINGENT — neither
forced nonzero nor forced zero — because it is a PRODUCT of three factors of which the
record forces only the winding prefactor `n^2` (admitted `n != 0`) and the TOTAL
`Phi_{f,tot} + Phi_{H,tot} != 0`, while the two factors that actually gate the cross
term are unbuilt: (i) the coherence coefficient `mu`, which vanishes exactly when either
source-sector weight vanishes and whose weights come from the UNBUILT scalarization /
state-port pair; and (ii) `Phi_{H,tot}`, the write-chain component in the flux-free
physical block H, which is exactly the NOT-SUPPLIED write-chain support/current datum
and requires both nontrivial cohomology and a non-bounding write support. The record
forces the SPLIT of `ell_j` into H vs im(d_1^dagger) NOWHERE; it forces only the total.**

---

## 1. SOURCES READ, SEALS RE-VERIFIED AT PATH

All under `/Users/bgm/MB Work/alpha-program-archive/workspace/`. Recomputed by
`shasum -a 256` before relying; first 8 hex shown.

| Tag | Source | Seal | Role in this derivation |
|---|---|---|---|
| FORM | `STAGE8_R_RECORD_L_FORM_FABLE_V001.md` | `5e49d209` MATCHES-TASKED | the FORM, three-block split, the cross term, Phi (the shared object of record; NOT consumed as an answer to this QUESTION) |
| V011 | `review_packets/STAGE7_QSPEC_CANDIDATE_V001/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` | `aa7c6d49` SEALED-OK | THE BEDROCK: the tangent complex, `d_1 d_0 = 0`, `Q_flux`, `R_record,L`, the Duhamel constraint (read directly, not via paraphrase) |
| W | `STAGE8_BARE_SURFACE_ALPHA_DETERMINATION_FABLE_V001.md` | `82e81f6e` SEALED-OK | the one-character-power write `chi_n`; unit-modulus characters; the trivial class eliminated by the charge/flux-access requirement (connection-only content only; the |n|=1 faithfulness line BARRED, not consumed) |
| M03 | `STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_FUNCTIONAL_RESULT_V001.md` | `2cd1ffce` SEALED-OK | the exact finite-N law `F_N = P_0 + Z_N P_ch`; the two source sectors (neutral P_0, charged P_ch); `Z_N = prod_j conj(z_j[a_-]) z_j[a_+]` |
| M06 | `STAGE8_TASK2D_SCALARIZATION_FUNCTIONAL_FORCING_PROTOCOL_RESULT_V001.md` | `d13920e2` SEALED-OK | scalarization / state-port UNBUILT: `UNIQUE_SCALARIZATION_FORCED = false|TYPE-R`; `U2_STATE_PORT_OPEN = false|TYPE-U`; `CONSTRUCTION_VERDICT = STATE_PORT_REMAINS_UNBUILT` |
| FR | `STAGE8_7A_RA27_3_FRONTIER_DARIO_V001.md` | `4d072e76` SEALED-OK | the physical, non-gauge assignment freedom; `support` and `current density` fields NOT SUPPLIED |
| CV | `STAGE8_7A_COUNTEREXAMPLE_CONTEST_DARIO_V001.md` | `c854c8b2` SEALED-OK | the non-coboundary certificate: `d_0 lambda = x_alt - x_F` inconsistent (the freedom is not gauge) |

NOT opened (would contaminate): the two named REQUIRE/G3 build-datum and check files.
No register / tracker / plan / road / ledger / lens read. No git action. Output name
probed before write: ABSENT.

---

## 2. WHAT THE OBJECTS FORCE ABOUT ell_j (QUESTION PART 1)

### 2.1 Placement of ell_j: FORCED into H ⊕ im(d_1^dagger)

The tangent complex (V011, read directly): `A^0 --d_0--> A^1 --d_1--> A^2`,
`(d_0 lambda)_e = lambda_t - lambda_s`, `(d_1 a)_f = sum_(e in bd f) incidence(f,e) a_e`,
`d_1 d_0 = 0`. In the sealed Gate-3 counting metric this gives the orthogonal split

```text
A^1 = im(d_0)  ⊕  H  ⊕  im(d_1^dagger),
      (gauge)    (flux-free phys.)   (flux-carrying phys.)
H = ker(d_1) ∩ im(d_0)^perp ,   im(d_1^dagger) = ker(d_1)^perp .
```

The QUESTION states `ell_j` is (a) gauge-invariant, `⊥ im(d_0)`, and (b) conserved,
`∂ell_j = 0`. The boundary/divergence operator is `∂ = d_0^dagger` up to sign, so
`∂ell_j = 0 ⟺ d_0^dagger ell_j = 0 ⟺ ell_j ∈ ker(d_0^dagger) = im(d_0)^perp`. Both
stated properties say the same thing and both land `ell_j` in `im(d_0)^perp = H ⊕
im(d_1^dagger)`. **FORCED, and it is the ONLY thing conservation + gauge-invariance
force.** Crucially, BOTH H and im(d_1^dagger) lie inside `im(d_0)^perp = ker(∂)`;
conservation is silent on the split, since `∂` annihilates the whole complement.

### 2.2 The total: FORCED nonzero for admitted n != 0

On the ratified object the connection enters ONLY through the per-cell characters
`z_j^(n)[a] = chi_n(h_j[a])`, `h_j[a] = exp(i <ell_j, a>)` (W; M03: no other
`a`-dependence anywhere in the law). One character power exactly (W:
`D_n[a] S |r> = z_n[a] |p_Q>`). The differential is

```text
d/ds z_j^(n)[s a]|_(s=0) = i n <ell_j, a> · z_j^(n)[0],    chi_n(identity) = 1,
```

so the write differential is the single per-cell family `Phi = (<ell_j, ·>)_j`, and the
total write functional is `Phi_tot[a] = sum_j <ell_j, a>`. The sealed elimination of
the trivial character (`n = 0`) runs on ZERO VARIATION under every external history; for
any admitted `n != 0` the differential is a NONZERO functional, hence `ell_j != 0` as a
total and `Phi_{f,tot} + Phi_{H,tot} != 0`. **FORCED.** (This consumes no faithfulness:
I use only that `chi_n` is a character, one power, unit modulus, and that the trivial
class alone is eliminated. The |n|=1 faithfulness result in W is BARRED and not used.)

### 2.3 The SPLIT phi_f vs phi_H: NOT forced by the sealed connection-only content

Write `ell_j = phi_H^{(j)} + phi_f^{(j)}` with `phi_H^{(j)} ∈ H`,
`phi_f^{(j)} ∈ im(d_1^dagger)`; `Phi_{H,tot} = sum_j phi_H^{(j)}`,
`Phi_{f,tot} = sum_j phi_f^{(j)}`.

**phi_f (flux/co-exact component).** The record's charge/flux-access requirement (W:
the requirement that kills the trivial `n=0` baseline) POINTS the write's holonomy
reading at the flux block: the canonical realization of "holonomy around cell j" is the
co-exact boundary loop `d_1^dagger e_{f_j} ∈ im(d_1^dagger)`, which is cell-local,
divergence-free, and gauge-invariant — matching every stated property of `ell_j`. Under
that canonical realization `Phi_{f,tot} != 0` and `Phi_{H,tot} = 0`. BUT at connection-
only tangent-block strength the requirement is satisfied by ANY nonzero holonomy
variation, including a purely topological (harmonic, H-block) reading; pinning the
variation specifically to `im(d_1^dagger)` needs the write-chain support/current
realization, which is NOT SUPPLIED (FR: `support`, `current density` fields absent).
So `phi_f != 0` is strongly indicated but CONTINGENT on that datum — not proven
connection-only.

**phi_H (flux-free physical / harmonic component).** `H = ker(d_1) ∩ im(d_0)^perp` is
the harmonic/cohomology block. A nonzero `Phi_{H,tot}` requires TWO things, neither
sealed: (i) `H != 0` (nontrivial first cohomology of the cellulation — not fixed by any
connection-only object), and (ii) the write support to reach a NON-BOUNDING cycle. A
strictly cell-local conserved current — a loop that BOUNDS a single 2-cell — is exactly
`d_1^dagger(2-chain) ∈ im(d_1^dagger)`, orthogonal to H, so it has `phi_H = 0`
identically. The physical non-gauge freedom (FR/CV: the difference is not a coboundary,
`d_0 lambda = x_alt - x_F` inconsistent) lives in `H ⊕ im(d_1^dagger)`, but whether ANY
of it lands in H — rather than in the co-exact flux block, which is equally non-
coboundary — is undecided of record. **`phi_H != 0` is a free/unbuilt datum.**

**Answer to Part 1.** Only the TOTAL `phi_f + phi_H != 0` is forced. `phi_f != 0` is
contingent (charge/flux-access at write-chain-support strength); `phi_H != 0` is not
forced (needs nontrivial H and a non-bounding write support — the unsupplied write-chain
datum). The record forces the placement of `ell_j` in `H ⊕ im(d_1^dagger)` and the
non-vanishing of its total, and forces NOTHING about the split.

---

## 3. IS THE COHERENCE COEFFICIENT mu FORCED NONZERO? (QUESTION PART 2)

The finite-N record sandwich leaves a two-sector SOURCE OPERATOR
`F_N = P_0 + Z_N P_ch` (M03): a neutral sector `P_0` and a charged sector `P_ch`,
with `Z_N[a_+,a_-] = prod_j conj(z_j[a_-]) z_j[a_+] = chi_n(relative holonomy)`. Any
scalarization pairs this with a state to produce sector weights `w_0` (neutral) and
`w_ch` (charged) and the exact finite-N scalar amplitude

```text
A_N = w_0 + w_ch · chi_n(h_rel) = w_0 + w_ch · exp(i n Phi_tot[a_Delta]),
Gamma_N = -log|A_N|,
Hess Gamma_N (a,b) = n^2 · mu(w) · Phi_tot[a] Phi_tot[b],
```

whose sole used structural property is exact and derivable from `Gamma_N = -log|A_N|`:

```text
mu(w) ≡ 0  iff  w_0 · w_ch = 0.
```

i.e. `mu` is the interference weight of the neutral×charged cross term; on either sector
alone there is no cross term (the charged sector alone has `|Z_N| = 1`, modulus action
identically zero; the neutral sector alone is connection-constant). The weights
`w_0, w_ch` come entirely from the scalarization / state-port pair, and that pair is
**UNBUILT of record**: M06 seals `UNIQUE_SCALARIZATION_FORCED = false | TYPE-R`,
`RHO_PRE_PLACED = false | TYPE-U`, `U2_STATE_PORT_INSTANTIATED = false | TYPE-U`,
`CONSTRUCTION_VERDICT = STATE_PORT_REMAINS_UNBUILT`. With the port unbuilt, nothing of
record forces `w_0 != 0` and `w_ch != 0` simultaneously; a scalarization onto a single
sector (`w_0 = 0` XOR `w_ch = 0`) is not excluded. **Therefore `mu` is NOT forced
nonzero — it is an unbuilt scalarization datum. MU_FORCED = NO_UNBUILT.**

---

## 4. NET FINITE-N VERDICT ON THE CROSS-BLOCK (QUESTION PART 3)

At finite N the charged Hessian is the coherent rank-one kernel: `C_N,jk = mu` for all
j,k (all-pairs, separation-independent). Hence the cross-block is the scalar product

```text
Phi_f^T C_N Phi_H = n^2 · mu · ( sum_j phi_f^{(j)} ) ( sum_k phi_H^{(k)} )
                  = n^2 · mu · Phi_{f,tot} · Phi_{H,tot}.
```

This is nonzero **iff all four factors are nonzero**: `n != 0` AND `mu != 0` AND
`Phi_{f,tot} != 0` AND `Phi_{H,tot} != 0`. Tallying what the record forces:

```text
n != 0            : ADMITTED (given; prefactor n^2; R(n) = R(-n), sign invisible).
Phi_{f,tot}+Phi_{H,tot} != 0 : FORCED (Sec. 2.2).
mu != 0           : NOT FORCED — unbuilt scalarization/state-port (Sec. 3).
Phi_{f,tot} != 0  : CONTINGENT — charge/flux-access at write-chain-support strength.
Phi_{H,tot} != 0  : NOT FORCED — datum G3: needs nontrivial H AND non-bounding
                    write support; cell-local boundary-loop realization gives 0.
```

Two of the gating factors (`mu`, `Phi_{H,tot}`) are unbuilt, and the third (`Phi_{f,tot}`)
is only contingently nonzero. So the cross-block is NOT forced nonzero. It is equally NOT
forced zero: no sealed object sets `mu = 0`, `Phi_{f,tot} = 0`, or `Phi_{H,tot} = 0` —
each could be nonzero under an admissible (unbuilt) realization. **The cross-block is
CONTINGENT.**

The exact inputs it is contingent on, minimally and completely:

```text
(A) mu != 0  ⟺  BOTH source-sector weights nonzero (w_0 != 0 and w_ch != 0) —
    supplied only by the UNBUILT scalarization / state-port pair (M06 TYPE-R/TYPE-U).
(B) Phi_{H,tot} != 0  —  the write chains' component in the flux-free physical block H
    (the NOT-SUPPLIED support/current-density realization, FR), which further requires
    nontrivial first cohomology (H != 0) AND a write support that reads a non-bounding
    cycle rather than a single-cell boundary loop.
(C) Phi_{f,tot} != 0  —  supplied by the charge/flux-access requirement read at that
    same write-chain-support strength (the canonical cell-local boundary loop already
    gives it; it is the sector the write is required to access).
    All under the admitted winding n != 0.
```

If the scalarization is later built onto both sectors (A holds) AND the write chains are
realized with a non-bounding H-component on a topologically nontrivial cellulation (B
holds), the cross-block is nonzero and, being rank-one, admits no sector-respecting basis
that removes it (block-diagonal congruence preserves a nonzero cross block). If either
(A) or (B) fails — a single-sector scalarization, or a purely co-exact / cell-local-
boundary write, or a topologically trivial complex — the cross-block is exactly zero and
the finite-N form degenerates to a one-sector response. Both outcomes are admissible on
the sealed connection-only content; nothing of record selects between them. That is the
precise sense of CONTINGENT.

---

## 5. FENCE / OVERCLAIM AUDIT

```text
NO SCALE consumed: tau_R and the counting metric appear only inside quoted sealed
   definitions; no ell_P, radius, K_KK, c^2, metric length, or Lorentzian object used.
   The integer 32 (dim of the physical freedom) and all incidence integers are sealed-
   text quotations / exact structural integers.
NO FAITHFULNESS: the |n|=1-via-injectivity result in W is BARRED and not consumed; the
   winding enters only as the admitted n^2 prefactor. The total-nonvanishing of the
   write uses only "one character power + trivial class eliminated", not injectivity.
NO IMPORTED GR: the derivation runs on the ratified connection-only tangent complex and
   the holonomy-character write; no metric, KK ansatz, Einstein-Hilbert, or quasilocal
   object appears.
mu AND C LEFT SYMBOLIC: mu is used only via the exact structural fact "mu ≡ 0 iff
   w_0 w_ch = 0"; no weight, kernel, spectrum, or coupling value is computed, bounded,
   estimated, or compared.
NO CONTAMINATION: the two named REQUIRE/G3 datum/check files were never opened; no
   register/tracker/plan/road/ledger/lens read; the verdict is derived from the sealed
   objects (V011, W, M03, M06, FR, CV) and the QUESTION alone.
FLATTENING CHECK: CONTINGENT is not flattened to FORCED-NONZERO by the attractiveness
   of the interference cross term (mu and Phi_H are named as the unbuilt gates), nor to
   FORCED-ZERO by the canonical cell-local reading (the non-bounding H-realization is
   left open). "Only the total is forced" is not flattened into "phi_f is forced".
```

---

## 6. FLAG BLOCK

```text
PHI_F_FORCED = CONTINGENT(charge/flux-access requirement points the write to
  im(d_1^dagger); tangent-block phi_f != 0 needs the NOT-SUPPLIED write-chain
  support/current realization; only the total phi_f + phi_H != 0 is forced connection-
  only) ;
PHI_H_FORCED = NO(free/unbuilt datum: the write chains' block decomposition; nonzero
  requires nontrivial first cohomology H != 0 AND a non-bounding write support — neither
  sealed; a strictly cell-local boundary-loop write gives phi_H = 0 identically) ;
MU_FORCED = NO_UNBUILT(mu ≡ 0 iff w_0 w_ch = 0; the sector weights come from the
  scalarization/state-port pair, sealed UNBUILT — M06 TYPE-R/TYPE-U,
  STATE_PORT_REMAINS_UNBUILT) ;
COLD_VERDICT = CONTINGENT(Phi_f^T C_N Phi_H = n^2 mu Phi_{f,tot} Phi_{H,tot}; nonzero iff
  (A) mu != 0 = both source-sector weights nonzero from the UNBUILT scalarization/state-
  port, AND (B) Phi_{H,tot} != 0 = write-chain component in H, requiring nontrivial H and
  a non-bounding write support (unsupplied support/current datum), AND (C) Phi_{f,tot}
  != 0 from the charge/flux-access requirement at that same write-chain strength, under
  admitted n != 0; the record forces only the total phi_f + phi_H != 0 and the n^2
  prefactor; none of mu, Phi_{H,tot} is forced nonzero and none is forced zero) ;
FORBIDDEN_IMPORTS = none ;
CONTAMINATED = no
```

`alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false ;
coupling_evaluation_authorized = false`
ALL_RESULTS = CLAIMED until adversarial panel check.
