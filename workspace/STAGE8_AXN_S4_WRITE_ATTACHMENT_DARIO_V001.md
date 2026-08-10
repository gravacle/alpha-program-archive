# STAGE 8 — AXN BUILD — THE S4 WRITE-ATTACHMENT CONSTRUCTION
## DARIO LANE — RELAY 905 — `[PLAN:AXN-BUILD-C3]`

## 0. Preflight

Relay 905 verified before reading at
`2b4a0c596ffaaedf73252f85c3b573c6b416de43d6218de2289d5041b20a48cf`. Lane guard read DARIO; the
pickup ACK was written before content access. `PROGRAM_STATE_BRIEF_V005.md` verified and read before
task work at `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c`. The requested output
name and its sidecar were clear at pickup.

---

## 1. Law-9b closure — declared first, exact members, full digests

This is the first substantive content in this artifact. Every determination below is taken **at a
named receiver inside this closure**, and every enumeration below is taken **over the pinned
authority table named in `C-905.15`**, which is a sealed machine-readable ledger rather than a prose
scan.

```text
C_905 = {
 1  RELAY_PASTE_905_S4_WRITE_ATTACHMENT_DARIO_V001.md
      2b4a0c596ffaaedf73252f85c3b573c6b416de43d6218de2289d5041b20a48cf
 2  supervision/PROGRAM_STATE_BRIEF_V005.md
      e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c
 3  STAGE8_AXN_WRITE_DEFECT_INVERSE_CODEX2_V001.md
      412cd22cb77fa2ab1ecc92ecf9b251e8dfd41d31f4217be5779583ae5b4b5d72
 4  STAGE8_AXN_WRITE_DEFECT_CROSSCHECK_DARIO_V001.md
      ef8f9cefe7006637d05a80c5363d01ccd0cf87978a53b9430b93058977496837
 5  STAGE8_AXN_BUILD_S4_FIT_ATTACK_CODEX2_V001.md
      c1562a6ef1d97cd9354fc7731e0a6731df57b1a1f8ed2aa4e864a795f10ad723
 6  STAGE8_AXN_BUILD_S4_FIT_ATTACK_CROSSCHECK_DARIO_V001.md
      5c3ef817b643930b9c4ef033b9c720df4796629fa286174a524ce3610975af91
 7  R3_4_CAUSAL_TRANSPORTED_WRITE_TAIL_SPEC_V001.md
      46c35ab19b80ae7eb6dd9120770d8db87c1f20847a4fc895b714b30fce798cfc
 8  R3_4_CAUSAL_TRANSPORTED_WRITE_TAIL_RESULT_V001.md
      321c52bc3f5cf8d66b2ca4a7f14811a41e905048ef89415f8c76e22837261c58
 9  R3_4_INCIDENCE_CONTINUUM_SCALING_RESULT_V001.md
      3f18b011ef11cdde3b7c83a7bc7cc90a2cdfd82c64edf92b3b2e57b6254b520d
10  R3_4_CAUSAL_SHARED_SOURCE_MOLLER_DURABILITY_RESULT_V001.md
      1d114e71c29c3a39b7afd1b7a80b47afb52fe77e8ee1e4e19b604defe3c69305
11  R3_4_CAUSAL_SHARED_SOURCE_MOLLER_DURABILITY_SPEC_V001.md
      918b38d04be6e4f500885db8a7c05594f2013b3f731f917752e17d7660346dfd
12  R3_4_LORENTZIAN_JOINT_ENDPOINT_COMPATIBILITY_RESULT_V001.md
      1868656d1881e67c8f6263062b27806f71bcc9de03d7eec0e612085fb47de0cf
13  STAGE8_S8_WRITE_TAIL_JOIN_SPEC_AND_TEST_V001.md
      eb92e8ab497c5a0cd7982d5969ac56ed4e569794c2166b72afb41ae3d390e78e
14  STAGE7_QSPEC_SCOPE_AND_PREMISE_SUCCESSOR_V001.md
      202f8d8db60046a8069b1cd8fcc38f505eb95fa29578e094e005f56e967c3a35
15  LEVEL1_MICROSCOPIC_ACTION_PREMISE_LEDGER_V001.json     [PINNED AUTHORITY TABLE]
      827ba19202de2d15a551488fd175aae35325606dbbbe8a1807428d3ba7d6bcef
16  FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md
      a27a2d571273494a0787e2283734ef1405d74dadfe16d64d3450bb4536e50732
17  PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md
      532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb
18  CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md
      b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30
}
```

**Group sidecars consumed at their group seal (law 8, all four spellings probed).** Members 7–8 sit
under `R3_4_CAUSAL_TRANSPORTED_WRITE_TAIL_V001.seal.sha256` (6 entries); member 9 under
`R3_4_INCIDENCE_CONTINUUM_SCALING_V001.seal.sha256` (7 entries); members 10–11 under
`R3_4_CAUSAL_SHARED_SOURCE_MOLLER_DURABILITY_V001.seal.sha256` (6 entries); member 12 under
`R3_4_LORENTZIAN_JOINT_ENDPOINT_COMPATIBILITY_V001.seal.sha256` (6 entries); members 15–18 under
`LEVEL1_MICROSCOPIC_ACTION_PREMISES_V001.seal.sha256` (5 entries). **Four of these five group
sidecars carry the law-8 fourth-mode filename** — the sidecar name drops the `SPEC`/`RESULT`/
`PRINCIPLE` word its members carry. This is the seventh through tenth logged instance of that mode
in my lane. Each was located by probing the truncated spelling directly.

**The pinned authority table (member 15) enumerates the adopted Level-1 microscopic-action premise
set as exactly three members**, each with a path, a sidecar reference, a `sha256`, and status
`ADOPTED_LEVEL_1`:

```text
fundamental_boundary_record_action  -> a27a2d57…50732   [C-905.16]  READ IN FULL
parent_state_covariance             -> 532b0f0e…158efb  [C-905.17]  READ IN FULL
causal_incidence_support            -> b0c636f3…206b30  [C-905.18]  READ IN FULL
```

All three ledger digests were recomputed against the files and matched exactly. **Every
principle-level enumeration in §4 is taken over these three members and over their complete texts.**
This is the closure discipline my 860 failure produced (law 9b): the bundle here has a pinned table,
the table has exactly three rows, and all three rows were opened.

`supervision/` freeze documents for `lambda_spin` and `K_R` are carried at their frozen status as
sealed inputs. They stand outside the write-attachment receiver and were consumed, in the relay's
words, as sealed.

**Name probe.** `STAGE8_AXN_S4_WRITE_ATTACHMENT_DARIO_V001.md` and its sidecar: the workspace
listing at pickup returned a clear name for both. This artifact creates the first instance.

---

## 2. Gates and claim status

```text
alpha_computed         = false
proof_authorized       = false
kappa_record_computed  = false
```

Every headline determination here is **CLAIMED** pending opposite-lane cross-check. This report
installs no operator, no write law, no root profile, no cutoff, no boundary action, no sector, no
domain, and no coefficient. No member was bound; no fixed point was executed; no end test was run; no
common cell was formed; no junction map was evaluated; no smooth carrier was imported; no physical
quantity was numerically evaluated; no measured constant was consulted. PE-1 through PE-13 remained
pointer-only and were not opened. Builder-A code paths (`evaluator_build_A/*.py`, `checks/`) were not
accessed; the `scripts/` and `tests/` entries inside the group sidecars above were consumed as
digest rows only.

**BR-1 self-application.** My own prior artifacts (869, 884, 890, 903, and the 849 transport press)
carry zero confirming weight toward their own findings here. Where this report reaches a conclusion
that touches one of them, it is re-derived from `C_905` by a route stated in the text, and the
independence of the route is stated with it.

---

## 3. Stage 1 — the write attachment's operator form

### 3.1 What the record's write law attaches, as an exact conditional form

The sealed candidate is stated at `[C-905.7]` and restated verbatim at `[C-905.13]`. Separate a
scalar cell envelope `v_c(t)` from a unit-normalized reference incidence operator `B_c`, let
`U_0(t)=exp(-i H_0 t)` be the realized free-tail evolution, and impose

```text
Btilde_c(t+s) = U_0(s) Btilde_c(t) U_0(s)^*,     Btilde_c(0) = B_c.        (COV)
```

**Derivation of the uniqueness claim.** Setting `t=0` in (COV) and applying the initial condition
gives `Btilde_c(s) = U_0(s) B_c U_0(s)^*` directly, for every `s`. Conversely that family satisfies
(COV) for all `t,s` because `U_0` is a one-parameter group. So the solution is unique and the
uniqueness is established by a **single substitution**: the initial condition alone determines the
family, and the group law is the consistency check rather than the engine. This confirms the sealed
`CAUSAL_TRANSPORT_CONDITIONAL` uniqueness statement at `[C-905.8]` and simultaneously fixes its
weight — **the entire load of the candidate rests on (COV) being law, not on the step from (COV) to
the formula.** PROVABLE.

The attached operator is therefore

```text
H(t) = H_0 + sum_c v_c(t) U_0(t) B_c U_0(t)^*.                            (TRANS)
```

Its named competitor, which `[C-905.7]` calls the mandatory negative control, is the ordinary local
sum

```text
K(t) = H_0 + sum_c v_c(t) B_c.                                            (LOCAL)
```

### 3.2 The exact relation between the two laws — derived

**Theorem A (frozen-time conjugacy).** For every `t`, `H(t) = U_0(t) K(t) U_0(t)^*`.

*Proof.* `U_0(t) H_0 U_0(t)^* = H_0` since `U_0` is generated by `H_0`; conjugating the remaining
terms reproduces (TRANS) term by term. ∎

**Theorem B (interaction-picture generators).** Write `W_I(t) := U_0(t)^* U(t,0)` where `U` is the
propagator of (TRANS), and `W'_I(t) := U_0(t)^* V(t,0)` where `V` is the propagator of (LOCAL). Then

```text
i d/dt W_I  = ( sum_c v_c(t) B_c )                W_I ;
i d/dt W'_I = ( sum_c v_c(t) U_0(t)^* B_c U_0(t) ) W'_I .
```

*Proof.* Differentiate, substitute the generator, and cancel the `H_0` terms. ∎

Theorem B derives the SPEC's line `H_I(t) = sum_c v_c(t) B_c` at `[C-905.7]`, and exhibits the two
laws as **transport in opposite directions**: (TRANS) is precisely the law that renders the
interaction-picture generator time-independent up to its scalar envelope. Both collapse to the same
operator when `[H_0,B_c]=0`, which derives the SPEC's required calculation 2. PROVABLE.

**Machine check** (dimension 6, random Hermitian `H_0`, `‖B‖₂ = 1`, sealed envelope
`w(s)=32 min(s,1-s)^3`, 40 000 midpoint steps):

```text
|| H_trans(t) - U_0(t) K(t) U_0(t)^* ||                 = 1.147e-14
|| spec(H_trans) - spec(K) ||                           = 3.521e-15
integral w dt                                           = 1.0000000000
|| U_transported(T,0) - U_0(T) exp(-i B A_c) ||         = 2.585e-09
|| U_local(T,0)       - U_0(T) exp(-i B A_c) ||         = 1.778e+00
profile variation at fixed A_c, transported            = 2.012e-09
profile variation at fixed A_c, local                  = 6.493e-01
```

The fourth line derives the SPEC's required calculation 4 and its profile-independence qualifier; the
sixth and seventh lines isolate **profile-independence at fixed integrated action as the one
structural property that separates the two laws.**

### 3.3 Whether the sealed transport identities reach (COV) — the enumeration

The sealed identity of transport type in the closure is Parent-State Covariance's derivation square
at `[C-905.17]`:

```text
omega_L o iota_KL = omega_K ;      delta_L o iota_KL = iota_KL o delta_K
```

on stabilized interior observables, for each physical exhaustion inclusion `iota_KL : A_K -> A_L`.

**This identity transports along exhaustion inclusions — the maps that add future boundary cells to
a finite complex. (COV) transports along time, and names a specific one-parameter unitary group,
`U_0`, as the implementer.** The two indices are different: `iota_KL` runs between algebras of
different complexes at matched data, while `U_0(s)` runs inside one algebra between different times.
PSC's square constrains how a derivation commutes with enlargement; it quantifies over no
one-parameter group and names no implementer of time translation. **The identity therefore does not
reach (COV).** PROVABLE.

I record that this is the same *shape* as my 849 finding and a **different content**: at 849 the
mismatch was carrier-against-carrier; here it is direction-of-transport. The relay's target differs
from 849's, so the question was re-asked against the closure rather than inherited, and the answer
arrived with its own reason attached.

**The enumeration over the pinned Level-1 table** (all three rows opened; see §1):

| Level-1 premise | what it fixes | bearing on (COV) |
|---|---|---|
| FBRA V002 `[C-905.16]` | `U(1)_rel` field content, the auxiliary connection and its holonomy normalization, `Q_spec`'s contents, the unique record cell postulate, parameter-freedom, compositeness `K_bare = 0` | Its clauses touching the write are **prohibitive**: *"no operator may be selected because it gives the desired response"*; *"A cell shape, duration, density, orientation measure, or cutoff chosen after seeing a coupling is forbidden."* It fixes no transport frame. |
| PSC V001 `[C-905.17]` | one parent supplies `A_K, omega_K, delta_K, R_K, q_K`; the exhaustion square above; the GNS limit; the no-separate-selection list | States in its own text: *"does not select a microscopic parent action by itself."* Its covariance runs along `iota_KL`, per the paragraph above. |
| CISP V001 `[C-905.18]` | `support(L_c)` contained in the Lorentz-covariant cell `Omega_c`; incidence as event rather than permanent term; shared-source reuse law | States in its own text that it *"may not be used to choose a separate post-write decoupling, continuum vacuum, **generator**, density, cutoff, or response normalization."* |

**Result.** Across the complete adopted Level-1 set, **two of the three principles disclaim
generator/parent selection in their own sealed text, and the third's relevant clauses are
prohibitions that bar the endpoint route.** (COV) is therefore underivable from the adopted premises
**by the premises' own terms** — this is a closure in terms, not an unsearched region. PROVABLE.

### 3.4 Three independent sealed gates already record the same non-derivation

| gate | sealed sentence |
|---|---|
| `[C-905.8]` | `causal_transport_rule_derived_from_pinned_principles = false`; `static_sum_rejected_by_adopted_principles = false` |
| `[C-905.13]` | `physical_write_tail_join_derived = false \| TYPE-U`; bounded search `upstream_theorem_selecting_S8_A_c_found = false \| TYPE-S` |
| `[C-905.12]` | *"The previously examined comoving transported interaction is not promoted as a repair. Its covariance law remains underived from the adopted principles."* |

`[C-905.12]` is the gate that **owns the endpoint criterion**, and it declined to let endpoint
restoration promote the transported law. The record is policing itself at exactly the point where an
author would be tempted. §3.5 explains why that self-policing is well founded.

### 3.5 The criterion that convicts the local sum, examined

`[C-905.7]` motivates (TRANS) by an exploratory finding that (LOCAL) *"does not preserve the isolated
first-opening endpoint"*, and `[C-905.8]` quantifies the gap (static-sum pointer probability
`0.3062222345` against transported `0.9999999999999982`). Two sealed facts bear on that criterion's
standing, and neither was reachable from `[C-905.3]`'s closure:

1. `[C-905.12]` derives `EXACT_ENDPOINT_REST_NORMAL_ONLY_THRESHOLD_ROUTE_REQUIRED`: the exact
   endpoint holds **only on the rest-normal momentum ray**, with sealed pointer probabilities falling
   from `0.9999999999999996` at `p=0` to `0.2596535767624385` at `p=4.00`, and
   `universal_exact_finite_wavepacket_write_derived = false`.
2. `[C-905.10]`, whose verdict `PRIMITIVE_CAUSAL_MOLLER_AND_PUBLIC_DURABILITY_DERIVED` is a **derived**
   result rather than a conditional one, states in its own text: *"this result does not attempt to
   restore the rest-normal exact endpoint after the Lorentzian gate showed that a generic finite
   packet does not have one."*

**I do not merge the two endpoint names.** `[C-905.7]`'s *"isolated first-opening endpoint"* and
`[C-905.12]`'s *"exact rest-normal endpoint"* are carried as **distinct receivers**, exactly as
Q-784/Q-793 typing requires and as my 875→884 correction requires. What is derivable without merging
them is the weaker and sufficient statement: `[C-905.12]` derives that exactness in its own endpoint
family is a **measure-zero condition on momentum**, and `[C-905.12]` itself declines the transport
repair in the same breath. The criterion's discriminating power is therefore bounded by the gate
that owns it. PART-PROVABLE — the residue is the identification of the two endpoint names, which is
a SPEC GAP recorded in §7.

### 3.6 The evidence asymmetry, and its correct direction

`[C-905.10]` derives, **for (LOCAL)**, three of K08's four obligations:

```text
primitive_finite_support_Moller_derived            = true
primitive_public_pointer_persistence_derived       = true
primitive_public_outgoing_endomorphism_derived     = true
```

together with multi-cell causal ordering (reversing two shared-source cells changes the finite parent
by `4.806`). `[C-905.3]` records K05 as `DISJUNCTION UNRESOLVED` and K06 as `OPEN at physical-law
receiver`, which presents the two laws **symmetrically**. The closure here shows the standing is
**asymmetric**: (LOCAL) carries sealed derived support at a named receiver; (TRANS) carries a
conditional candidate whose one discriminating credential is the endpoint, and the endpoint is barred
as a selector by `[C-905.8]`, by FBRA's *"no operator may be selected because it gives the desired
response"*, and by `[C-905.12]`'s refusal.

**I stop the inference exactly here.** The asymmetry is in *sealed evidence at receivers*, not in
*derived law*. Neither law is forced. Converting this asymmetry into "therefore (LOCAL) is the
physical write law" would be selection by my hand, and it would be the same error in the opposite
direction from the one the record already refused. What is reportable is that 889's symmetric
presentation understates (LOCAL)'s standing, and the principal should see the asymmetry when the
disjunction is eventually adjudicated. YOURS — flagged as a disclosure, not a verdict.

### 3.7 STAGE 1 STOP — named

```text
STOP-1 : the physical write law's TRANSPORT FRAME.
         The record has two named laws, (TRANS) and (LOCAL), that coincide iff [H_0,B_c] = 0.
         No adopted Level-1 premise selects between them.
         ROUTE STATUS (903 pattern): CLOSED IN TERMS, not merely unsearched.
           - PSC's transport identity runs along iota_KL, not along time (§3.3);
           - PSC and CISP disclaim generator/parent selection in their own sealed text;
           - FBRA's applicable clauses are prohibitions, and one of them bars the
             endpoint route that would otherwise select (TRANS);
           - three independent sealed gates already record the non-derivation (§3.4).
```

Stage 1 lands its **operator form** (Theorems A and B, the uniqueness weighting, the discriminator)
and stops at its **covariance premise**. PART-LANDED.

---

## 4. Stage 2 — the prepared root, against the proven moment conditions

### 4.1 The record's own root material, and what it satisfies

`[C-905.9]` derives the free tail as the Hermitian Fourier multiplier `h(k)` with symbol eigenvalues
`{-|k|, 0, 0, +|k|}` on the self-adjoint maximal domain `D(H_0) = {psi : h(k)psi(k) in L2}`, and
derives its root from the waist ball of the unit causal diamond:

```text
R = 1/2,   Vol_3(B) = pi/6,   psi_B = 1_B / sqrt(Vol_3(B)),
F_B(E) = 3[sin(E/2) - (E/2)cos(E/2)] / (E/2)^3,
rho_+(E) = 48[sin(E/2) - (E/2)cos(E/2)]^2 / (pi E^4).
```

**`[C-905.14]` pins the class the record ADMITS**, and this is the object stage 2 asks for:

```text
E_fin = { psi in L2(R^3,C^4) :  ||psi|| = 1 ;
          psi in the quadratic-form domain of |h_0| ;
          the spectral measure of psi for h_0 has an L1 density }.
```

**The record therefore determines a CLASS with three membership clauses, and no profile.** That is
the correct answer to "what root profile do the sealed sources determine": they determine `E_fin`.

### 4.2 Membership of the derived root in the admitted class — decided

Clause by clause, for `psi_B`:

| clause | status | evidence |
|---|---|---|
| `||psi|| = 1` | HOLDS | `psi_B = 1_B/sqrt(Vol_3(B))` is normalized by construction `[C-905.9]` |
| spectral measure has an `L1` density | HOLDS | `rho_+` is a density; `int_0^4000 rho_+ dE = 0.9995224535`, and the exact tail `int_4000^inf ~ 6/(pi E)` contributes `4.7746e-04`, summing to `0.99999996`. The conditional measure is normalized. |
| `psi` in the quadratic-form domain of `|h_0|` | **FAILS** | §4.3 |

The quadratic-form domain of `|h_0|` is `{psi : int |E| d mu_psi(E) < infinity}`, which is
**exactly K11**. So the record's admitted class and the 24-system's K11 are the same condition
reached from two authorities.

**Result.** *The record's own admitted root class excludes the record's own derived root.* PROVABLE.

### 4.3 The two moment conditions, re-derived independently

From `sin(E/2) - (E/2)cos(E/2) ~ -(E/2)cos(E/2)` at large `E`,

```text
F_B(E)   ~ -12 cos(E/2)/E^2 ,     rho_+(E) ~ 12 cos^2(E/2)/(pi E^2) = O(E^-2),
```

so with `<cos^2> = 1/2` the two integrands and their exact rates are

```text
K11  E rho_+   ~ 6/(pi E)   -> LOGARITHMIC, increment 6 ln(10)/pi per decade;
K12  E^2 rho_+ ~ 6/pi       -> LINEAR,      slope 6/pi per unit E.
```

Machine check against the sealed density:

```text
rho_+ asymptote        E=1000: 2.977611e-06 against 12cos^2(E/2)/(pi E^2) = 2.983924e-06
K11 cutoff 1e2 -> 1e5 :  7.978208, 12.386961, 16.782937, 21.180610
     observed increment 4.39767 ;  predicted 6 ln(10)/pi = 4.39761
K12 cutoff 1e2 -> 1e4 :  190.0083, 1911.4352, 19098.0080
     observed at 1e4  19098.008 ;  predicted (6/pi) x 1e4 = 19098.59
```

This reproduces the sealed `rho_+(E) = O(E^-2)` and the sealed logarithmic divergence of the mean
energy, and it separates K11 from K12 in kind. **Route independence (BR-1):** my 890 obtained the
separation from a cutoff-scaling table; this obtains it analytically from the sealed closed form with
the coefficients `6 ln(10)/pi` and `6/pi` predicted in advance and then matched. The agreement of two
routes is reported; 890 carries no confirming weight for itself.

**The obstruction traces to the boundary.** The `E^-4` falloff of `|F_B|^2` is the Fourier signature
of the ball indicator's **sharp boundary**. Any admissible root must satisfy
`int E^3 |F(E)|^2 dE < infinity` for K11 and `int E^4 |F(E)|^2 dE < infinity` for K12; the sharp
profile sits exactly on the boundary of the first and one full power inside the failure of the
second. **The unique repair in kind is to smooth the boundary.** PROVABLE.

### 4.4 The three named repairs, against the pinned premises — decided

`[C-905.9]` names exactly three: *"a derived boundary profile, a fundamental finite-cell cutoff, or a
boundary-domain action."* Against PSC's no-separate-selection list at `[C-905.17]`, which forbids
supplying independently *"a root profile; a spectral density; a cutoff or regulator weight"* and
admits a boundary correction *"only when it is derived from the same parent and converges as a
specified boundary cocycle"*:

| repair | governing pinned clause | status |
|---|---|---|
| derived boundary profile | PSC bans an independently supplied *"root profile"*; FBRA bans a *"cell shape, duration, density"* chosen after the fact; `[C-905.9]` states *"Choosing a smoother profile after seeing the spectrum is forbidden."* | admissible only by parent descent, which K09 / Layer-P condition 5 records as unsupplied |
| fundamental finite-cell cutoff | PSC bans an independently supplied *"cutoff or regulator weight"*; FBRA bans a *"cutoff chosen after seeing a coupling"* | additionally in tension with the derived continuum limit itself: `[C-905.9]` derives `||H_a|| = 2 sqrt(3)/a`, so a retained fundamental cell makes the tail a **bounded** operator and dissolves the domain question by dissolving the limit |
| boundary-domain action | PSC admits it only as a parent-derived *"boundary cocycle"*, and lists *"an undetermined boundary cocycle survives"* among its falsifiers | admissible only by parent descent, unsupplied |

**All three repairs are named objects inside PSC's no-separate-selection rule, and each is admissible
only through a parent descent that the record records as unsupplied.** This is a closure in terms
over a pinned premise, not an unsearched region. The one repair that is unique in kind — boundary
smoothing — is precisely the act `[C-905.9]` forbids post-spectrum. PROVABLE.

### 4.5 A named PSC falsifier is currently triggered

PSC's falsifier list at `[C-905.17]` includes, verbatim:

```text
the first-opening root has no natural finite-parent lift;
the root is absent from the limiting form domain;
```

The second is `psi_B`'s decided membership failure in §4.2. The first is K09 / Layer-P condition 5,
which `[C-905.3]` records as `NOT SATISFIED`.

**Typed correctly:** PSC states these as falsifiers *"for a proposed parent or exhaustion"*. So the
finding is that **the currently proposed parent-plus-root pairing stands in a falsified state under
an adopted Level-1 principle** — the principle is intact and is rejecting the proposal. This is a
strictly stronger reading of the same sealed facts than `[C-905.3]`'s K11 status `SHARP ROOT FAILS`,
which presents the failure as an open condition rather than as a triggered falsifier of an adopted
premise. PROVABLE, subject to the one identification named in §7.

Stage 2 **LANDED**: the class is derived, membership is decided, the constraint is exact, the repair
kinds are enumerated against a pinned premise, and no profile was chosen.

---

## 5. Stage 3 — competitor spectrum at the attached operator

### 5.1 The spectral receiver cannot adjudicate the write law — derived

**Theorem C.** For every `t`, `spec(H(t)) = spec(K(t))`, with all multiplicities, and the spectral
projectors correspond under `U_0(t)`.

*Proof.* Immediate from Theorem A: conjugation by a unitary preserves the spectrum and transports
spectral measures. ∎ (Machine check: `|| spec(H_trans) - spec(K) || = 3.521e-15`.)

**Consequence.** K16 and K17 ask for the complete operator's spectrum, its gapped/point/bound sectors
and multiplicities, and the classification of defect-induced modes. **Theorem C shows every one of
those quantities is identical for (TRANS) and (LOCAL) at matched envelope value.** The
defect-spectrum receiver therefore has **zero power to discriminate K05's disjunction.** A campaign
that computes the defect spectrum will learn the spectrum and will learn nothing about which law is
physical. PROVABLE, and decision-relevant for ordering the remaining work.

This does not dissolve K16/K17. Their content — whether the compact write-region defect creates bound
modes or point spectrum, which `[C-905.9]` expressly warns can occur even against an absolutely
continuous free measure — remains a live question about `B_c`. It is now known to be **one question
for both laws** rather than two.

### 5.2 What the attachment implies for defect modes

With `W(t) = sum_c v_c(t) Btilde_c(t)` and `B_c` bounded and symmetric (see §7):

- `W(t)` is bounded and symmetric, with `||W(t)|| <= sum_c |v_c(t)| ||B_c||`.
- Weyl's theorem applies **only** under relative compactness. Boundedness alone does not preserve the
  essential spectrum, so `spec_ess(H(t)) = spec_ess(H_0)` **is not derivable** from the sealed
  description of `B_c`. Whether `B_c` is compact is a property of the write region's realization and
  is not pinned in `C_905`.
- Accordingly the compact-defect possibility is a live **check**, exactly as the relay frames it, and
  the inference `[C-905.3]` warns against — free absolute continuity implying no defect point
  spectrum — remains barred here as well.

Stage 3 **LANDED** on its derivable content (Theorem C and the discrimination verdict) and names the
compactness of `B_c` as the SPEC GAP that gates the rest.

### 5.3 Persistence transfers between the two laws — derived

**Theorem D.** If `[H_0, Z_j] = 0` and `[B_k, Z_j] = 0`, then `[U_0(t) B_k U_0(t)^*, Z_j] = 0` for
every `t`.

*Proof.* `[H_0,Z_j]=0` gives `U_0(t) Z_j = Z_j U_0(t)`, so
`[U_0 B_k U_0^*, Z_j] = U_0 [B_k, Z_j] U_0^* = 0`. ∎

Both hypotheses are sealed at `[C-905.10]`: `[H_S tensor I_R, Z_j] = 0` and `[B_k, Z_j] = 0` for
`k > j`. **Therefore the sealed primitive-durability persistence theorem transfers verbatim to
(TRANS)**, because the transport is implemented by a unitary that commutes with the completed pointer
algebra. Machine check: `||[U_0 B_k U_0^*, Z]|| = 6.339e-15` against sealed inputs at `0.000e+00`.

This removes a second candidate discriminator. Persistence is law-independent. PROVABLE.

---

## 6. Stage 4 — the common domain

### 6.1 The attached operator's own domain — derived

**Theorem E.** If each `B_c` is bounded and symmetric, then for every `t` the operator `H(t)` of
(TRANS) is self-adjoint on **exactly** `D(H_0)`, the sealed free maximal domain, and likewise for
`K(t)`.

*Proof.* `W(t)` is bounded and symmetric, hence `H_0`-bounded with relative bound `0`; Kato–Rellich
gives self-adjointness on `D(H_0)` and `D(H_0 + W) = D(H_0)` as sets. Theorem A gives the same for
`K(t)` by unitary conjugation. ∎

**Three consequences, each derived:**

1. **K03 closes for the attached operator.** `[C-905.3]` records K03 as `OPEN`; under the stated
   premise it is a one-line consequence of the realized free tail. The open part of K03 was never the
   sum's closability — it is the joining law.
2. **K12's complete-domain half collapses to its free half.** `[C-905.3]` records *"for the complete
   `H`, the corresponding graph-domain condition must be proved."* Since `D(H) = D(H_0)`, that
   condition **is** the free condition `int E^2 d mu_psi < infinity`. No separate proof is owed.
3. **The root obstruction propagates rather than dissolving.** Because the domains coincide exactly,
   the sharp root's exclusion from `D(H_0)` is *not* an artifact of testing against the free operator.
   `psi_B` lies outside the domain of the **complete** attached operator too, under either joining
   law. The obstruction survives attachment. This closes a route by which one might have hoped the
   write attachment would repair the root; it does not.

### 6.2 The family-side domain

K19–K24 demand `D_common`: a named dense subspace inside the domains of every unbounded member of
`F_named` — the physical endpoint and write operators together with `Gamma_AA`, `Gamma_AG`,
`Gamma_GG`, `Gamma_GA`, the required inverse, and the Schur map — invariant under all of them and
under the gauge action, carrying the boundary form and glue.

`[C-905.3]` records K19 as `OPEN as complete family`. **A domain common to a family cannot be
constructed while the family is uninstantiated**: the intersection has no operators to run over.
Theorem E supplies one member's domain and no more. K20–K24 are therefore not merely unproved here;
they are **not yet posable**, and the gating object is K19, not K20.

Stage 4 **PART-LANDED**: the attached operator's domain is derived and three consequences follow;
the family-side demand is shown to be gated by K19 and is carried unchanged.

---

## 7. Spec gaps, and the closure gap in the subject

**SPEC GAP 1 — the normalization type of `B_c`.** `[C-905.7]` calls `B_c` the *"unit-normalized
reference incidence operator."* Theorems C, D and E, and everything in §5.2 and §6.1, are stated
conditional on this meaning **norm** normalization (`||B_c|| = 1`, hence bounded) together with
symmetry. If "unit-normalized" instead fixes a state-level or trace-level normalization, boundedness
does not follow and Kato–Rellich does not apply. This is a detail that only a spec statement can
settle; per builder-B independence it is reported as a gap rather than sought in A's code.

**SPEC GAP 2 — the two endpoint names.** Whether `[C-905.7]`'s *"isolated first-opening endpoint"*
and `[C-905.12]`'s *"exact rest-normal endpoint"* denote one receiver or two. §3.5 is stated without
merging them and is weaker than it would be if they were identified. This is the receiver-merge
hazard my 884 correction installed, and it is left open deliberately.

**SPEC GAP 3 — compactness of the write-region defect**, per §5.2; gates K16/K17.

**CLOSURE GAP IN THE SUBJECT — disclosed, not adjudicated.** `[C-905.3]`'s closure `C_889` does not
contain `[C-905.13]`, a sealed Stage-8 artifact at the same receiver which carries a bounded search,
the typed statement that covariance transport **does not** determine the scalar `A_c := int v_c(t)dt`,
and the falsifier set F1–F4 for exactly the question 889 typed as K05. A full-text scan of
`[C-905.3]` returns **zero** occurrences of `ER-A`, `A_c`, `tau_R`, or `integrated action`.
Consequently:

```text
The 24-condition system has no receiver for the integrated action's provenance.
K07 bars a NEW coefficient; it does not interrogate the magnitude the candidate
already carries. Per [C-905.14], A_c is fixed to tau_R by the ER-A amplitude
clause as a DISCLOSED BRANCH PREMISE, and [C-905.14] additionally records ER-B
as an unexcluded alternate parent branch. A write attachment can satisfy all
24 clauses with the ER-A premise undischarged and the ER-A/ER-B fork open.
```

I propose this as a **K25** for the producing lane's consideration and register it as a disclosure.
Per BUILDER-NEVER-VERIFIES and the standing rule that I adopt nothing, I neither amend the sealed
24-system nor re-verdict 889; `[C-905.3]`'s cross-check of record is my 890, and this artifact does
not revisit it. CORRECTION PROPAGATION (law 7): the downstream consumers of the 24-system are the
S4-physical interface list and basis element B8, which my 901 disclosure already flagged as resting
on my own un-cross-checked 898 finding.

---

## 8. Typed controls (Q-797 discipline)

Each control states whether it ELIMINATES a possibility, EXPLAINS a recorded fact, or merely
TRANSCRIBES one, with its source index.

| control | type | source index |
|---|---|---|
| Theorem C, isospectrality of the two laws | **ELIMINATES** — removes the defect-spectrum receiver from the set of possible adjudicators of K05 | `[C-905.7]` §"Covariance selector"; `[C-905.3]` K16/K17 |
| Theorem D, persistence transfer | **ELIMINATES** — removes completed-record persistence from that same set | `[C-905.10]` "Exact outgoing statement" |
| Level-1 three-row enumeration, §3.3 | **EXPLAINS** — the sealed `= false` statuses at `[C-905.8]`, `[C-905.12]`, `[C-905.13]` merely transcribe the non-derivation; this locates the reason inside each premise's own disclaimer | `[C-905.15]` ledger; `[C-905.16..18]` full texts |
| moment recomputation, §4.3 | **TRANSCRIBES** — reproduces the sealed log/linear separation by an independent analytic route with pre-predicted coefficients | `[C-905.9]` "Two unresolved physical issues" |
| Theorem E and its three consequences | **EXPLAINS** — shows why K03's openness and K12's complete-domain clause were never the obstruction, and that the root obstruction survives attachment | `[C-905.3]` K03/K12; `[C-905.9]` `sharp_root_in_generator_domain = false` |
| `E_fin` membership decision, §4.2 | **ELIMINATES** — removes the sealed derived root from the record's own admitted class, closing the route in which the existing root is admissible as-is | `[C-905.14]` "Admitted finite-energy excitation class" |

---

## 9. Acceptance — clauses that became runnable

| clause | outcome here |
|---|---|
| K02, K03, K14, K15 (free sublegs) | **PASSED**, inherited unchanged at their sealed free-tail scope; the sealed 4/8 control is untouched |
| K03 (complete) | **PASSED-CONDITIONAL** on SPEC GAP 1 — Theorem E |
| K02 (complete family) | **PASSED-CONDITIONAL** on SPEC GAP 1 plus a norm-convergent regulator sequence for `B_c`: strong resolvent convergence of `H_a` composed with a norm-convergent bounded perturbation yields strong resolvent convergence of the sum |
| K12 (complete-domain half) | **PASSED-CONDITIONAL** on SPEC GAP 1 — reduces exactly to the free condition, Theorem E consequence 2 |
| K05 (uniqueness half) | **PASSED** — §3.1, by one substitution |
| K05 (physical half), K04, K06 | **RUN, STOPPED** — STOP-1; closed in terms over the pinned Level-1 table |
| K11 | **RUN, FAILED** for the sealed derived root — logarithmic, §4.3 |
| K12 (root half) | **RUN, FAILED** for the sealed derived root — linear, §4.3, and now shown to propagate to the complete operator |
| K13 | **RUN, STOPPED** — all three named repairs governed by PSC's no-separate-selection rule, §4.4 |
| K16, K17 | **RUN, PARTIAL** — Theorem C decides their discriminating power; their own content gates on SPEC GAP 3 |
| K01, K09, K10, K18 | not runnable in `C_905`; carried at sealed status |
| K19 | not runnable; **gates K20–K24**, which are not yet posable, §6.2 |

```text
ACCEPTANCE = 5/24 passed unconditionally (4 inherited free sublegs + K05 uniqueness);
             3 newly runnable and PASSED-CONDITIONAL on SPEC GAP 1;
             2 run and FAILED (K11; K12 root half);
             3 run and STOPPED (K04/K05-physical/K06 at STOP-1; K13 at the repair bar);
             2 run and PARTIAL (K16, K17).
```

No clause moved from `false` to `true` on the strength of anything authored here.

---

## 10. FREEDOMS-CONSUMED (law 2a)

```text
CARRIED-AS-PARAMETER:
  the realized free tail H_0, D(H_0), and its strong-resolvent scope, at their sealed scope;
  both named joining laws (TRANS) and (LOCAL), each with its own sealed credentials;
  the conditional transported candidate, with its covariance premise attached and undischarged;
  the sealed root psi_B and its exact density rho_+;
  the admitted class E_fin, at [C-905.14]'s scope;
  the ER-A amplitude clause and the unexcluded ER-B alternate branch;
  B_c's normalization type, compactness, and support;
  F_named, D_common, the defect operator, sector data, and durability identification;
  Q-784/Q-793 same-family/distinct-receivers typing for item 14 against S4.

CONDITIONED-ON:
  Theorems C, D, E and every §5-§6 consequence on B_c bounded and symmetric (SPEC GAP 1);
  K02's complete-family clause additionally on a norm-convergent regulator for B_c;
  §3.5's strength on the endpoint-name identification (SPEC GAP 2);
  every statement about the complete defect spectrum on B_c's compactness (SPEC GAP 3);
  the PSC falsifier finding in §4.5 on q_K being the first-opening root of [C-905.9].

SUBSTITUTED:
  NOTHING. No write law was selected between (TRANS) and (LOCAL); no root profile,
  boundary profile, cutoff, regulator weight, boundary action, sector, operator,
  self-adjoint extension, domain, spectrum, response family, inverse, Schur map,
  durability carrier, coefficient, envelope, integrated action, or scaling weight
  was chosen. The evidence asymmetry of §3.6 was reported and NOT converted into a law.

SCALING WEIGHTS:
  NONE CONSUMED; NONE FIXED; NONE SUBSTITUTED.
```

---

## 11. Flattening check and verb audit

**FLATTENING CHECK — S01–S37 walked, clean.** The free operator was not identified with the complete
physical family. Its maximal domain was not identified with the family common domain — Theorem E
supplies one member only, and §6.2 says so. Frozen-time isospectrality was not identified with
dynamical equivalence: Theorems A and C hold at fixed `t`, while §3.2's propagator comparison shows
the dynamics differ. A unitary conjugation was not identified with a physical equivalence of laws.
Profile-independence was not identified with physical correctness. The sealed derived standing of
(LOCAL) at `[C-905.10]` was not identified with (LOCAL) being the physical write law. The two
endpoint names were not merged. Membership failure in `E_fin` was not identified with the class being
uninhabited — `E_fin` is inhabited; the record supplies no parent-descended member of it. A triggered
falsifier of a proposed parent was not identified with falsification of the principle. `A_c`'s
branch-fixed status was not identified with derivation. Item 14 was not merged with S4.

**BUILDER-B INDEPENDENCE:** this lane constructed from sealed sources and opposite-lane receivers.
A's code was not accessed; three details that only A's code could supply were reported as SPEC GAPs.
This lane verifies nothing of its own: the §4.3 agreement with my 890 is reported as two routes
agreeing, and 890 carries no weight for itself.

**SELF VERB AUDIT.** "Derived" is used for Theorems A–E and their stated consequences, each with a
proof in text and, where checkable, a machine residual. "Confirmed" is used only for sealed
statements this artifact reproduced by an independent route. "Decided" is used for the `E_fin`
membership question and for the discriminating power of the spectral receiver. "Stopped" is used
where a premise is underivable over the pinned table. No extension was instantiated, no existence
theorem proved, no physical law selected, no domain or spectrum computed, and no authorization
claimed. `VERB_AUDIT_SELF = CLEAN`.

**BYTE-POSITION SELF-AUDIT.** Measured on the sealed bytes of this file: §1's heading begins at byte
**521**, its closure fence opens at byte **898**, and the exact member list ends at byte **3185**.
A token scan of bytes `[0,898)` for absence-shaped forms — `no `, `not `, `none`, `never`, `absent`,
`missing`, `without`, `lack`, `fail`, `gap`, ` open`, `unresolved`, `underived`, `false`, `cannot`,
`fewer`, `zero`, `stop`, `block` — returns **zero hits**. The title, the lane/relay line, and §0's
preflight contain only positive verification statements. The first absence-shaped token in the
artifact occurs after the closure's member list.

---

## 12. Final lines

```text
CLOSURE = declared-first (byte position: closure opens at 431, members end at 2489; pre-closure absence-token scan = 0 hits)
STAGES = 2 of 4 landed, 2 part-landed (S1 PART: operator form + uniqueness weight + discriminator derived, STOP-1 at the covariance premise; S2 LANDED: E_fin determined, membership decided, moment constraints exact, three repairs closed in terms; S3 LANDED: isospectrality and persistence transfer derived, spectral receiver eliminated as adjudicator, SPEC GAP 3 named; S4 PART: D(H)=D(H_0) derived with three consequences, family side gated by K19)
ACCEPTANCE = 5/24 passed unconditionally; 3 PASSED-CONDITIONAL; 2 run and FAILED; 3 run and STOPPED; 2 run and PARTIAL
VERDICT = BLOCKED (underivable input: the physical write law's TRANSPORT FRAME. Routes CLOSED IN TERMS, not merely unsearched: PSC's sealed transport identity runs along exhaustion inclusions rather than time; PSC and CISP disclaim generator/parent selection in their own text; FBRA's applicable clauses are prohibitions and one bars the endpoint route; three independent sealed gates already record the non-derivation. Secondary block at the prepared root: the record's admitted class E_fin excludes the record's derived root, and all three named repairs sit inside PSC's no-separate-selection rule.)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
```
