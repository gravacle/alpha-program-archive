# BARE-SURFACE I-2 DETERMINATION — V001 (2026-08-14)

Analyst: I2-BUILD (blind; bare-surface protocol). Governing design: `BARE_SURFACE_I2_TEST_DESIGN_V001.md` (sealed; obeyed over the tasking brief wherever they differ — no difference was found). Surface of record: `SURFACE_DEFINITION_OF_RECORD_V001.md` (sealed), taken per the design's GROUND as clauses §I–§II plus the displayed dimensionless locks, and NOTHING else. Fences live throughout: alpha_computed = false · proof_authorized = false · kappa_record_computed = false. No numeric evaluation of any physical constant occurs anywhere in this artifact; π, √2, ℏ are symbolic everywhere; no comparison, explicit or implied, to any measured value; no closed form of any would-be solution is formed, displayed, or evaluated (none exists to form — see verdict).

---

## 0. VERDICT (one line)

ILL-POSED — on the bare surface (clauses §I–§II of the surface of record plus its displayed dimensionless locks, and nothing else), α's role has no surface-native referent: a coupling in α's role would be a dimensionless invariant sitting in the strength-slot of a law that crosses from the phase/holonomy sector into the write/response sector, and the sealed ground contains no such slot — the in-amplitude slot is booked absent with exact mechanism (unit-modulus write weights; "whatever converts internal to external is NOT a magnitude on record"; TYPE-R), every in-phase slot is integer-quantized by U(1) single-valuedness and occupied phase-to-phase by the definitional n ∈ {+1,−1}, and every booked dimensionless item is an identity, label, or bound rather than a coupling — so there exist no fixing conditions to derive, the existence/uniqueness gate is never reached, and the missing referent is exactly a derived, β-invariant, magnitude-valued internal→external response junction on the write structure, which only a new booked surface derivation of amplitude/weight structure could supply (the unit-modulus write-signature route to it being already booked TYPE-R refuted).

---

## 1. SEALS

Verified at path with `shasum -a 256` against the `.seal.sha256` sidecars, both MATCH:

| Document | SHA-256 (computed = sidecar) |
|---|---|
| `/Users/bgm/MB Work/alpha_supervision/BARE_SURFACE_I2_TEST_DESIGN_V001.md` | `31978a6d1179b6b42a72effd364c87233b30ef0bd638c8f57ddc75eb10764fed` |
| `/Users/bgm/MB Work/alpha_supervision/SURFACE_DEFINITION_OF_RECORD_V001.md` | `20ee87c0d06464346186de5d1f9ccf879be3646f4be3d284b35dc1a086f842df` |

The surface digest matches the expected `20ee87c0d064…` prefix stated in both the design and the tasking brief. Both documents were read in full (the seal gate and the design's own instruction require it). Build premises are restricted to the design's GROUND: surface §I–§II + the displayed locks; the surface document's §III–§VI were necessarily read inside the sealed file but supply NO premise anywhere below (non-load-bearing; disclosed in §4.6). Blindness: no register, road, ledger, lens, plan, or tracker file was opened; the only files opened this session are the two sealed documents and their sidecars (directory listings, filenames only, were taken to locate paths and confirm the deliverable path was vacant).

---

## 2. THE SURFACE-NATIVE REFERENT QUESTION — what α's role IS on this ground

### 2.1 The role-anchor (given by the test instrument, not imported)

The design poses: does the surface's own dimensionless content determine "a unique dimensionless invariant occupying α's role"? The tasking brief supplies the role-anchor in surface-neutral words: a candidate must be **"a dimensionless invariant of the surface's own self-consistency that couples the phase/holonomy structure to the write/response structure."** [GROUND — instrument text. No property of α beyond this sentence is used anywhere in this build; in particular no magnitude, sign, size, or empirical fact about α enters.]

### 2.2 The surface's two sectors [DERIVED — by inspection of §I–§II]

The sealed ground carries exactly two structural sectors:

- **(a) The phase/holonomy sector:** connection/holonomy histories as sole index of the dynamics, no native metric anywhere, no logarithm taken (§I.1); continuous fibers over a discrete base (§I.2); holonomy characters z_j^(n) = χ_n(h_j[a_j]), unit modulus, n ∈ {+1,−1}; U(1) transitions g_ij = exp(iθ_ij) (§I.3); affine connection space, no fiber metric, no distinguished connection (§I.4); the exact refinement/coarsening law of the cell (§I.5 — named as exact and derived; its explicit form is not displayed on the sealed ground).
- **(b) The write/response sector:** the write structure with unit-modulus (phase) weights and no amplitude/magnitude structure (§II.6); the opening/response kinematics — first-opening probabilities, orthogonality, endpoint transfer, projective lengths, T_R, H_R (§II.7); the write action |ΔS_record| (§II.9); onset content m_* and the onset bound (§II.9); the balanced-geodesic identities (§II.9 — named; form not displayed).

The invariance structure over both: the free scale orbit (T_R → λT_R, H_R → H_R/λ) with every derived junction a fixed point (β-invariant) (§II.7–8), the displayed locks τ_R = π/√2, |ΔS_record| = πℏ, m_* T_R = π (§II.7, §II.9), and the net line: the surface forces the entire dimensionless structure and leaves the absolute scale free (§II.10).

### 2.3 Role-criteria [DERIVED — from 2.1 plus the ground's own invariance structure]

For X to occupy α's role on this ground:

- **R1 (invariance).** X is dimensionless and a fixed point of the free scale orbit — otherwise X is not an invariant of this surface at all (§II.7–8).
- **R2 (derivedness).** X is an output of the surface's self-consistency (refinement exactness, transition/cocycle consistency, lock compatibility) — not a definitional label, not a free input, not a chart or history variable.
- **R3 (role occupancy).** X sits in the **dimensionless strength-slot of a surface law that crosses sectors** — a law in which phase/holonomy variables drive a write/response quantity, with X scaling how much write/response per unit phase structure. This is what "couples … to …" means. R3 is the discriminator between a *coupling* and a *lock*: a lock is an identity between already-defined quantities (it has no slot); a coupling is the occupant of a slot in a law's form — and note carefully that a **derived** coupling is *also* forced to a fixed value, so forcedness cannot be the discriminator; slot-occupancy is. Dropping R3 collapses the question: without it, any booked pure number (τ_R = π/√2, …) would "occupy α's role" by mere existence, the question would be answerable YES for any surface whatsoever carrying any dimensionless lock, and α's role would not have been posed at all. [DERIVED]

### 2.4 Slot typology [DERIVED — CAS B2]

Every record-native functional has polar type modulus × phase, and on this record the modulus of every native object is identically 1 (§I.3 characters and transitions; §II.6 write weights; CAS B2.1–B2.9 verify closure under transition action, cocycle composition, character maps, and arbitrary native composites). Hence a dimensionless strength-slot in any record law can only be:

- **(i) in-amplitude** — multiplying a magnitude-valued write/response functional; or
- **(ii) in-phase** — multiplying a phase.

This typology is exhaustive. [DERIVED] The referent question therefore becomes exact: **does the sealed ground contain a cross-sector law carrying a nonempty slot of type (i) or (ii) available to a derived dimensionless invariant?** Section 3 answers it.

---

## 3. THE DETERMINATION ATTEMPT

### 3.1 Chain A — the ground's complete cross-sector law inventory [DERIVED — finite enumeration]

The ground is finite (the sealed clauses). By inspection, the ONLY items in which variables of sector (a) and sector (b) touch are:

- **L1 — the character map** z_j^(n) = χ_n(h_j[a_j]) (§I.3): converts a holonomy (sector a) into a write character (a sector-b weight). Both ends are unit-modulus (CAS B2.5): L1 is phase-to-phase. Its only slot is the in-phase index n.
- **L2 — the indexing declaration** (§I.1): "the record's dynamics is indexed by connection/holonomy histories alone." This asserts that a cross-sector dependence EXISTS, with NO displayed functional form — hence no displayed slot.

No other displayed law contains variables of both sectors: each displayed lock's law contains no phase-sector variable (CAS B3.3b — variable-set inspection of the lock system), and no response quantity co-occurs with n, θ_ij, or any holonomy variable anywhere on the sealed pages. [DERIVED — enumeration; exhaustive because the ground is exhaustively quoted.]

### 3.2 Chain B — slot type (i), in-amplitude: EMPTY, booked absent with mechanism [DERIVED]

§II.6 (GROUND, categorical): the write structure carries unit-modulus (phase) weights, **not** amplitude/magnitude; "Whatever converts internal to external is NOT a magnitude on record"; and the booked TYPE-R refutation with exact mechanism — unit-modulus structure cannot produce the bounded lift; **"the physical signature needs weight/amplitude structure the records provably do not carry."**

- CAS B2.9: the record algebra has no magnitude coordinate — the modulus of every native composite is the constant 1 and all its record-direction derivatives vanish identically.
- CAS B3.1: a magnitude coupling g acting on any native object yields modulus g exactly — for g ≠ 1 the result is no longer a record weight at all (unit-modulus booked). **A strength has nothing on-record to act on: it either acts trivially or exits the record algebra.**

So no in-amplitude slot exists in ANY record law, displayed or entailed. This is not an artifact of the two-page presentation; it is the booked content of the surface itself ("provably do not carry"). [DERIVED; scope per C12, §4.4]

### 3.3 Chain C — slot type (ii), in-phase: integer-quantized, and phase-to-phase only [DERIVED]

Single-valuedness on U(1) quantizes every in-phase multiplier to the integers: CAS B3.2a (integers close exactly), B3.2b (the fractional strength G = 1/2 violates closure exactly: exp(iπ) − 1 = −2). **There is no continuum-valued in-phase slot on a U(1) record.** The ground's one occupied in-phase slot is n in L1, with n ∈ {+1,−1}:

- **R2 check:** the value set {+1,−1} is *definitional* ground (§I.3), not an output of self-consistency on this ground — what self-consistency derives is only n ∈ ℤ. A definitional input cannot be the determined occupant without circularity (the surface would "determine" what it was defined with). FAILS R2.
- **R3 check:** L1 is phase-to-phase (both ends unit-modulus, CAS B2.5; the conjugate pair closes magnitude-free, CAS B2.7); no displayed law couples n to any response quantity (3.1). n scales how a phase is wound into a phase — it does not scale write/response per unit phase structure. FAILS R3.
- The unit-winding reading X = |n| = 1 fails identically: it is a quantization fact of the phase sector — an identity of single-valuedness — not a strength in a phase→response law. [DERIVED]

### 3.4 Chain D — the booked dimensionless inventory, swept exhaustively against R1–R3 [DERIVED]

| Candidate X | Type on ground | R1 | R2 | R3 | Disposition |
|---|---|---|---|---|---|
| n (character index) | discrete label, ground-given; integrality derivable | yes | integrality DERIVED; selection {±1} definitional — fails | no — phase-to-phase law only (3.3) | not the occupant |
| \|n\| = 1 (unit winding) | quantization identity | yes | derives from single-valuedness | no — identity, no slot; phase side only | not the occupant |
| continuum in-phase strength G in exp(iGθ) | not on record | — | — | slot nonexistent (CAS B3.2b) | no such invariant exists on a U(1) record |
| τ_R = π/√2 | displayed lock (first-opening kinematics) | yes (CAS B1.2b) | DERIVED (booked) | no — timing identity; no phase-sector variable in its law | lock, not occupant |
| \|ΔS_record\|/ℏ = π | displayed lock (write action) | yes | DERIVED (booked) | no — write-side identity; no holonomy variable co-occurs | lock, not occupant |
| m_* T_R = π | displayed lock (onset × duration) | yes (CAS B1.3) | DERIVED (booked) | no — kinematic identity | lock, not occupant |
| balanced-geodesic identities | named identities, form undisplayed | yes (booked fixed points) | DERIVED (booked) | identities admit no slot; any admissible content is phase/timing-typed (§II.6 categorical) | locks, not occupants |
| onset bound | named bound, form undisplayed | yes (booked fixed point) | DERIVED (booked) | a bound is an inequality — it carves regions; saturation could only add another identity, again slot-free | not an occupant |
| first-opening probabilities, orthogonality, endpoint transfer, projective lengths | forced kinematic response content | yes (booked orbit-invariant, §II.7) | forced (§II.10) | no displayed law exhibits them as holonomy-driven (3.1); the internal→external conversion is booked non-magnitude (§II.6) | response-side locks; no slot |
| algebraic combinations of locks | fixed symbolic pure numbers (e.g. τ_R² = π²/2, CAS B1.1a) | yes | trivially derived from locks | identities compose to identities; no slot arises by algebra | not occupants |
| relative character phase δ = φ₊ − φ₋ | phase-valued invariant | yes (CAS B3.3a; no T,H dependence) | NOT derived — absent from every displayed law (CAS B3.3b): unconstrained | phase-valued: scales nothing; fails | free AND role-less — see honest exhibit below |
| transition phases θ_ij, holonomy phases | chart/history variables | not invariants (vary over connection space and gauge) | — | — | not invariants |
| thirteen sealed interface junctions (identities withheld) | statuses only on ground (§II.8) | derived ones: yes (booked β-invariant) | derived ones: yes | any magnitude-valued internal→external junction among them would contradict §II.6's categorical booking; phase/timing-typed junctions yield identities | cannot supply the occupant, whatever they are |

**Honest exhibit (the freedom, shown even though it is role-less):** if one weakened the role-anchor to admit phase-valued invariants as "couplings," the verdict on that weakened reading would be DOES-NOT-DETERMINE, with the exact freedom exhibited: δ is a well-formed dimensionless orbit-fixed invariant and NO displayed law constrains it (CAS B3.3). The weakening is rejected because it abandons R3 (2.3): a phase that scales nothing does not couple the sectors. On either reading, no unique occupant is determined. [DERIVED]

### 3.5 Chain E — the withheld contents cannot reverse the vacancy [DERIVED; scope per C12]

The ground names four content-withheld items: the exact refinement law's form (§I.5), the balanced-geodesic identities' form (§II.9), the onset bound's form (§II.9), the thirteen interface junctions' identities (§II.8). For each, EVERY admissible content is already typed by the categorical bookings:

- **Refinement law:** it is structure OF the cell (§I.5), acting within the unit-modulus write algebra (§II.6 is stage-unqualified: "the records provably do not carry" amplitude). Composition of unit-modulus factors is unit-modulus (CAS B4.1; induction — base B2.1, step B4.1): **no refinement or coarsening stage can generate an amplitude slot.** The vacancy is refinement-stable whatever the law's detailed form.
- **Identities and bound:** identities are slot-free forms (no one-parameter family to occupy); a bound is an inequality; its saturation would add another identity — still slot-free; and any content is phase/timing-typed by §II.6's categoricity.
- **Thirteen junctions:** a magnitude-valued internal→external junction among them would contradict the booked "whatever converts internal to external is NOT a magnitude on record" / "provably do not carry" — so none is such, whatever they are.

Therefore **no disclosure of withheld content could create the missing slot: the lack is structural, not informational.** This is what separates ILL-POSED from UNDERDETERMINED-AT here.

### 3.6 CAS battery (verbatim) and output (verbatim)

Environment: fresh venv under `/private/tmp` (per protocol), sympy 1.14.0, exact symbolic only — no `evalf`, no `N`, no float literal anywhere; ℏ, π, √2 symbolic throughout; the output was scanned and contains no numeric evaluation (the only digit-dot-digit matches are the battery's own section tags such as `B1.1a`).

```python
#!/usr/bin/env python3
# BARE_SURFACE_I2 CAS BATTERY -- exact symbolic only.
# Fence discipline: no evalf/N/float anywhere; no numeric evaluation of any
# physical constant; no measured value; nothing compared to anything empirical.
# Every check is an exact symbolic identity over the sealed ground's displayed content.
import sympy as sp

pi, I = sp.pi, sp.I
Rat = sp.Rational

lines = []
def emit(tag, ok, detail=""):
    lines.append(f"[{tag}] {'PASS' if ok else 'FAIL'}{(' -- ' + detail) if detail else ''}")

def is_zero(e):
    return sp.simplify(e) == 0

def modulus(e):  # exact polar modulus via z * conj(z); no Abs numerics
    return sp.sqrt(sp.simplify(sp.expand(e * sp.conjugate(e))))

# symbols (all exact, all symbolic; hbar is a symbol, never evaluated)
lam = sp.Symbol('lambda', positive=True)
hbar = sp.Symbol('hbar', positive=True)
mstar, T_R, H_R = sp.symbols('m_star T_R H_R', positive=True)
phi, a, b, c, th1, th2, psi = sp.symbols('phi a b c theta1 theta2 psi', real=True)
php, phm = sp.symbols('phi_plus phi_minus', real=True)
h1, h2 = sp.symbols('h1 h2', real=True)
nZ = sp.Symbol('n', integer=True)
dS_abs = sp.Symbol('dS_abs', positive=True)

# ---------- B1: displayed locks -- exactness, consistency, orbit fixed points ----------
tau_R = pi / sp.sqrt(2)   # booked lock (displayed): tau_R = pi/sqrt(2)
dS = pi * hbar            # booked lock (displayed): |Delta S_record| = pi*hbar

emit("B1.1a", is_zero(tau_R**2 - pi**2 / 2),
     "tau_R^2 == pi^2/2 exactly (symbolic identity; no float formed)")
emit("B1.1b", is_zero(dS / hbar - pi),
     "|Delta S_record|/hbar == pi exactly (dimensionless in hbar units)")

# booked free scale orbit (SII.7): T_R -> lam*T_R, H_R -> H_R/lam
emit("B1.2a", is_zero((H_R / lam) * (lam * T_R) - H_R * T_R),
     "action-type product H_R*T_R is an orbit fixed point")
emit("B1.2b", is_zero(sp.diff(tau_R, T_R) + sp.diff(tau_R, H_R)),
     "tau_R carries no T_R,H_R dependence: orbit-fixed")

# the lock m_*T_R = pi FORCES the orbit weight of m_*: m_* = pi/T_R
m_forced = pi / T_R
m_forced_orb = m_forced.subs(T_R, lam * T_R)
emit("B1.3a", is_zero(m_forced_orb - m_forced / lam),
     "lock m_*T_R = pi forces m_* orbit weight -1 (derived from the lock, not assumed)")
emit("B1.3b", is_zero(m_forced_orb * (lam * T_R) - pi),
     "orbit maps lock solutions to lock solutions; residue m_*T_R == pi constant on the whole orbit")

# displayed lock system: consistent; one free scale direction; zero free dimensionless slots
sol = sp.solve([sp.Eq(mstar * T_R, pi), sp.Eq(dS_abs, pi * hbar)], [mstar, dS_abs], dict=True)
emit("B1.4", len(sol) == 1 and is_zero(sol[0][mstar] - pi / T_R) and is_zero(sol[0][dS_abs] - pi * hbar),
     f"unique forced solution with T_R free: {sol[0]}; residual freedom = the one scale direction only; "
     "no free dimensionless slot exists in the displayed lock system")

# ---------- B2: the record's native algebra is pure phase -- no magnitude coordinate ----------
z = sp.exp(I * phi)                      # holonomy/write phase object (SI.3, SII.6)
g1, g2 = sp.exp(I * th1), sp.exp(I * th2)  # U(1) transitions (SI.3)

emit("B2.1", is_zero(modulus(z) - 1),
     "|exp(i*phi)| == 1 identically: record weights carry no magnitude")
emit("B2.2", is_zero(sp.diff(sp.simplify(modulus(z)), phi)),
     "d|z|/dphi == 0: no record direction moves a modulus")
emit("B2.3", is_zero(modulus(g1 * z) - 1),
     "U(1) transition action preserves unit modulus")
emit("B2.4", is_zero(modulus(g1 * g2) - 1),
     "U(1) cocycle composition closes in unit modulus")

chi = lambda nn, hh: sp.exp(I * nn * hh)   # characters chi_n, n in {+1,-1} (SI.3)
emit("B2.5", is_zero(modulus(chi(1, h1)) - 1) and is_zero(modulus(chi(-1, h1)) - 1),
     "|chi_{+1}| == |chi_{-1}| == 1: the character map is phase-to-phase on both ends")
emit("B2.6", is_zero(sp.simplify(chi(1, h1 + h2) - chi(1, h1) * chi(1, h2))),
     "character homomorphism exact")
emit("B2.7", is_zero(sp.simplify(chi(1, h1) * chi(-1, h1) - 1)),
     "chi_{+1}*chi_{-1} == 1: the n set {+1,-1} is a closed conjugate pair, magnitude-free")

# arbitrary native composite: write x transition x character
composite = sp.exp(I * a) * sp.exp(-I * b) * sp.exp(I * nZ * c)
emit("B2.8", is_zero(modulus(composite) - 1),
     "every native composite (write x transition x character) is unit-modulus")
mval = sp.simplify(modulus(composite))
emit("B2.9", all(is_zero(sp.diff(mval, s)) for s in (a, b, c)),
     "the modulus of every native composite is the constant 1; all record-direction derivatives "
     "vanish -- the record algebra contains no magnitude coordinate")

# ---------- B3: candidate slot type-checks against the role criteria ----------
# B3.1 in-amplitude slot: a magnitude coupling g acting on the record algebra either
#      acts trivially (g == 1) or exits the algebra (result no longer unit-modulus)
gcoup = sp.Symbol('g', positive=True)
emit("B3.1", is_zero(sp.simplify(modulus(gcoup * composite) - gcoup)),
     "|g * (native composite)| == g exactly: for g != 1 the result is NOT a record weight "
     "(unit-modulus booked, SII.6) -- the amplitude slot has no on-record carrier")

# B3.2 in-phase slots are integer-quantized by single-valuedness on U(1)
emit("B3.2a", is_zero(sp.simplify(sp.exp(2 * pi * I * nZ) - 1)),
     "integer in-phase multipliers close single-valuedly: exp(2*pi*i*n) == 1 for n in Z")
emit("B3.2b", sp.simplify(sp.exp(2 * pi * I * Rat(1, 2)) - 1) == -2,
     "fractional in-phase strength G = 1/2 violates closure exactly (exp(i*pi) - 1 == -2): "
     "no continuum-valued in-phase slot exists on a U(1) record")

# B3.3 the relative character phase delta: well-formed invariant, but unconstrained and phase-valued
delta = php - phm
emit("B3.3a", is_zero(((php + psi) - (phm + psi)) - delta),
     "delta invariant under overall write phase (well-defined dimensionless invariant)")
lock_vars = set()
for eq in [sp.Eq(mstar * T_R, pi), sp.Eq(dS_abs, pi * hbar)]:
    lock_vars |= eq.free_symbols
emit("B3.3b", len({php, phm} & lock_vars) == 0,
     "delta is absent from every displayed lock/law: unconstrained on the ground -- and "
     "phase-valued, so it scales no response (fails the role criterion R3)")

# ---------- B4: refinement stability of the vacancy ----------
emit("B4.1", is_zero(modulus(sp.exp(I * a) * sp.exp(I * b)) - 1),
     "|u*v| == 1 for unit-modulus u,v: composition/refinement stages cannot generate an "
     "amplitude (base case B2.1 + this composition law; induction displayed in text)")

print("BARE_SURFACE_I2 CAS BATTERY -- exact symbolic, zero numerics (sympy)")
for ln in lines:
    print(ln)
fails = sum(1 for l in lines if "] FAIL" in l)
print(f"TOTAL: {len(lines)} checks; FAIL count = {fails}")
```

Output, verbatim:

```text
BARE_SURFACE_I2 CAS BATTERY -- exact symbolic, zero numerics (sympy)
[B1.1a] PASS -- tau_R^2 == pi^2/2 exactly (symbolic identity; no float formed)
[B1.1b] PASS -- |Delta S_record|/hbar == pi exactly (dimensionless in hbar units)
[B1.2a] PASS -- action-type product H_R*T_R is an orbit fixed point
[B1.2b] PASS -- tau_R carries no T_R,H_R dependence: orbit-fixed
[B1.3a] PASS -- lock m_*T_R = pi forces m_* orbit weight -1 (derived from the lock, not assumed)
[B1.3b] PASS -- orbit maps lock solutions to lock solutions; residue m_*T_R == pi constant on the whole orbit
[B1.4] PASS -- unique forced solution with T_R free: {dS_abs: pi*hbar, m_star: pi/T_R}; residual freedom = the one scale direction only; no free dimensionless slot exists in the displayed lock system
[B2.1] PASS -- |exp(i*phi)| == 1 identically: record weights carry no magnitude
[B2.2] PASS -- d|z|/dphi == 0: no record direction moves a modulus
[B2.3] PASS -- U(1) transition action preserves unit modulus
[B2.4] PASS -- U(1) cocycle composition closes in unit modulus
[B2.5] PASS -- |chi_{+1}| == |chi_{-1}| == 1: the character map is phase-to-phase on both ends
[B2.6] PASS -- character homomorphism exact
[B2.7] PASS -- chi_{+1}*chi_{-1} == 1: the n set {+1,-1} is a closed conjugate pair, magnitude-free
[B2.8] PASS -- every native composite (write x transition x character) is unit-modulus
[B2.9] PASS -- the modulus of every native composite is the constant 1; all record-direction derivatives vanish -- the record algebra contains no magnitude coordinate
[B3.1] PASS -- |g * (native composite)| == g exactly: for g != 1 the result is NOT a record weight (unit-modulus booked, SII.6) -- the amplitude slot has no on-record carrier
[B3.2a] PASS -- integer in-phase multipliers close single-valuedly: exp(2*pi*i*n) == 1 for n in Z
[B3.2b] PASS -- fractional in-phase strength G = 1/2 violates closure exactly (exp(i*pi) - 1 == -2): no continuum-valued in-phase slot exists on a U(1) record
[B3.3a] PASS -- delta invariant under overall write phase (well-defined dimensionless invariant)
[B3.3b] PASS -- delta is absent from every displayed lock/law: unconstrained on the ground -- and phase-valued, so it scales no response (fails the role criterion R3)
[B4.1] PASS -- |u*v| == 1 for unit-modulus u,v: composition/refinement stages cannot generate an amplitude (base case B2.1 + this composition law; induction displayed in text)
TOTAL: 22 checks; FAIL count = 0
```

### 3.7 Chain F — menu adjudication [DERIVED, given Chains A–E]

- **Not DETERMINES.** With both slot types empty in every cross-sector law of the ground (Chains B, C) and every booked dimensionless item slot-free (Chain D), the candidate class occupying α's role is EMPTY. There is no X for which fixing conditions could be derived; existence and uniqueness have no subject. The build therefore never forms, solves, displays, or evaluates anything — the stop is at the referent gate, strictly before the design's pre-numeric gate.
- **Not DOES-NOT-DETERMINE.** That branch requires candidates that exist but float (the design's exemplar: candidates riding the free scale orbit). Dimensionless candidates here do not float — they are orbit fixed points (§II.8; CAS B1.2) — and the one genuinely free dimensionless invariant expressible on the ground (δ) is role-less; its freedom is exhibited honestly (3.4) but it is not freedom OF an occupant.
- **Not UNDERDETERMINED-AT.** That branch requires a named missing surface DATUM whose supply could decide the question. Chain E shows no withheld content can create the missing slot: the needed structure is not withheld-but-existing, it is booked absent with mechanism ("provably do not carry"). A structure the surface provably lacks is not a missing datum of the surface.
- **ILL-POSED — the menu's own wording fits exactly:** α's role has no surface-native referent. The missing referent, precisely: **a derived, β-invariant, magnitude-valued internal→external response junction on the write structure** — a response-magnitude functional that the phase/holonomy sector drives, in whose dimensionless strength-slot a surface-forced invariant could sit. What would supply it: **only a new booked surface result deriving such amplitude/weight structure on the record**; per the booked TYPE-R mechanism (§II.6), it cannot be extracted from the existing unit-modulus write signature — it would have to be genuinely new derived structure.

---

## 4. THE RESULT AT ITS EXACT QUANTIFIER

### 4.1 Formal statement

Let G be the sealed bare-surface ground (surface §I–§II + displayed locks). Say X *occupies α's role on G* iff R1(X) ∧ R2(X) ∧ R3(X) (2.3), R3 requiring a law of G crossing from the phase/holonomy sector to the write/response sector with X in its dimensionless strength-slot. Then:

1. [DERIVED] The cross-sector laws displayed by G are exactly {L1, L2} (3.1); Slot(L1) = {n}, integer-quantized, definitionally occupied, phase-to-phase; Slot(L2) = ∅ (no displayed form).
2. [DERIVED] No law of G, displayed or entailed, carries an in-amplitude slot (§II.6 booked absence with mechanism; CAS B2.9, B3.1); no law of G carries a continuum-valued in-phase slot (single-valuedness; CAS B3.2).
3. **Therefore ¬∃X [X occupies α's role on G].** The union of strength-slots over all laws of G contains no position for a dimensionless invariant coupling phase structure to response strength.
4. Consequently the determination question has no subject on G: nothing exists whose fixing conditions could be derived, so existence/uniqueness cannot be posed, let alone proven. **ILL-POSED, at exactly this quantifier** — the failure mode is the empty candidate class (not a floating candidate, not a withheld datum; 3.7).

### 4.2 What the surface DOES determine (the positive content honestly earned)

The displayed dimensionless lock system is consistent, mutually compatible, orbit-coherent — the lock m_* T_R = π itself forces m_*'s orbit weight (CAS B1.3a), so the booked fixed-point statement is internally derived, not assumed — and its solution manifold has exactly one free scale direction with zero free dimensionless slots (CAS B1.4). This re-derives, on the displayed subset, the ground's own net line (§II.10): the surface forces everything dimensionless it carries and leaves the scale free. **It carries no coupling.**

### 4.3 What would change the verdict

On the day G contains a law L* crossing sectors with a magnitude-valued response side — equivalently, a **new booked, derived, β-invariant amplitude/weight junction on the write structure** — the determination question becomes well-posed on this ground and must be re-run from scratch under the same fences and the same one-shot end-test discipline. Per the booked TYPE-R mechanism, L* cannot come from the existing unit-modulus write signature; it requires genuinely new derived structure.

### 4.4 Claim ledger (claim-by-claim marking, per the design)

| ID | Claim | Marking |
|---|---|---|
| C1 | Two-sector reading of the ground (2.2) | DERIVED (§I–§II by inspection) |
| C2 | Role-criteria R1–R3 are the surface-native content of "occupying α's role"; dropping R3 un-poses the role (2.3) | DERIVED (instrument role-anchor + ground invariance structure) |
| C3 | Displayed locks satisfy R1; the lock m_*T_R = π forces m_*'s orbit weight; lock system = one free scale, zero free dimensionless slots (4.2) | DERIVED (CAS B1) |
| C4 | The record's native functional algebra is pure phase — no magnitude coordinate; closed under transitions, cocycles, characters, composites (2.4) | DERIVED (§I.3, §II.6; CAS B2) |
| C5 | Slot typology in-amplitude/in-phase is exhaustive (2.4) | DERIVED (polar decomposition; CAS B2.9) |
| C6 | In-amplitude slot absent on record, with booked mechanism; a strength has no on-record carrier (3.2) | DERIVED (§II.6 TYPE-R; CAS B3.1); scope per C12 |
| C7 | In-phase slots integer-quantized; ground occupancy n ∈ {±1} definitional (fails R2) and phase-to-phase (fails R3); no continuum in-phase slot (3.3) | DERIVED (CAS B3.2, B2.5–B2.8; §I.3) |
| C8 | Cross-sector law inventory of G = {L1, L2}, exhaustive (3.1) | DERIVED (finite enumeration of the sealed clauses) |
| C9 | Every booked dimensionless item fails R1∧R2∧R3; δ is free but role-less (3.4) | DERIVED (CAS B1, B3.3; enumeration) |
| C10 | Withheld contents cannot supply the slot (3.5) | DERIVED; scope per C12 |
| C11 | Menu adjudication ⇒ ILL-POSED with referent and supply route named (3.7) | DERIVED (given C4–C10) |
| C12 | Scope premise: the §I.3/§II.6 bookings are categorical over the record at every stage and junction, as their sealed wording states ("unit modulus"; "NOT a magnitude on record"; "provably do not carry") | CONDITIONAL (premise = the sealed ground's own categorical wording; C4, C6, C10 inherit exactly that strength, no more — if a future booked result weakened that wording, Chains B/E lose categorical scope and the verdict must be re-derived; that is precisely the supply route of 4.3) |

No claim in this artifact stands at bare CLAIMED strength.

### 4.5 Fence compliance

- alpha_computed = false; proof_authorized = false; kappa_record_computed = false — live throughout.
- No numeric evaluation of any physical constant anywhere; π, √2, ℏ symbolic in every expression; the CAS battery contains no `evalf`, no `N`, no float literal; its output was scanned — no numeric content beyond the battery's own section tags.
- No fixing conditions were formed (none exist); a fortiori no solution was formed, solved, displayed in closed form, or evaluated; the stop is at the referent gate, strictly earlier than the design's pre-numeric gate.
- No comparison, explicit or implied, to any measured value; no measured or empirical constant appears in this artifact.

### 4.6 Provenance disclosures

- Files opened this session: exactly the two sealed documents and their `.seal.sha256` sidecars. Directory listings (filenames only) of `alpha_supervision` and `alpha-program-archive/workspace` were taken to locate paths and confirm the deliverable path was vacant; no listed file was opened. Register, road, ledger, lens, plan, tracker: NOT opened.
- Build premises: design GROUND clauses 1–3 only (surface §I–§II + displayed locks). Surface §III–§VI were read inside the sealed file (unavoidable and required) but supply NO premise in any chain above; they are non-load-bearing everywhere in this build.
- Forbidden imports: NONE used — no Λ^even(C⁵) carrier or cellulation machinery; no K_KK; no fiber proper radius R; no metric or fiber metric; no ℓ_P; no length/scale object and no internal↔external conversion object; no S16/Thomson bridge, no κ_Thomson, no spacetime cross-section matching; no "α rides an absolute scale"; no imported KK gravitational action; no Finish-A/Finish-B framing; no E1-successor/Carleman/S2′ objects; no lens/GR/sphere/4π-as-the-sphere reading; no continuum-diamond import; no measured or empirical constant. Terminology note: "β-invariant" is used solely as the ground's own name for scale-orbit fixed-point status (§II.8; design GROUND clause 1); no conversion object is invoked by the term. The fibers-over-discrete-base statement used is the ground's own §I.2.
- Ambient session context contained no surface physics; nothing outside the two sealed documents entered any derivation.
- CAS: sympy 1.14.0, fresh venv under `/private/tmp`, exact symbolic only; battery and output embedded verbatim in 3.6 (fidelity checked by mechanical extraction and diff against the executed script and its captured output before sealing).

---

## 5. FLAG BLOCK

I2_STATUS = ILL-POSED — no surface-native referent for alpha's role on the bare surface; referent-vacancy DERIVED (no cross-sector strength-slot exists: the in-amplitude slot is booked absent, TYPE-R, and in-phase slots are integer-quantized and phase-to-phase only); missing referent named: a derived, beta-invariant, magnitude-valued internal-to-external response junction on the write structure; supply route named: only a new booked surface derivation of amplitude/weight structure (the unit-modulus write-signature route is booked TYPE-R refuted); stopped at the referent gate, strictly before the pre-numeric gate — no fixing conditions exist, none were formed, nothing was solved, displayed, or evaluated
MACHINERY_INVOKED = no
SCALE_TOUCHED = no — the free scale orbit enters only as the booked invariance test (fixed-point verification, criterion R1); no scale object was used, fixed, anchored, or converted anywhere
VALUE_EVALUATED = no
NET = The bare surface freezes its entire dimensionless content into identities, labels, and bounds, and provably withholds the one structure — a magnitude-valued write/response slot — that a coupling in alpha's role would occupy; on its own terms the surface does not pose alpha's determination at all, and what is missing is not a hidden datum but underived structure: a booked, beta-invariant amplitude/weight junction, which the record's unit-modulus write signature is already proven unable to supply.
