# STAGE 8 / 7A / [PLAN:A2-CORRECTIVE] — ADVERSARIAL CROSS-CHECK OF THE LAYER REBUILD

Lane: CODEX 2 (independent cross-check). Relay 783.

Subject: `STAGE8_7A_DBR_LAYER_REBUILD_DARIO_V001.md`, SHA-256
`d55b64459be8bdacbcc102486bc5948362f6e45b8c6b3a512bea2689fe9c20f7`.

## Lead verdict

The rebuild is **partly refuted**.

The unconditional operator-functional form and the tight universal floor
`lambda >= C2_parent` survive. The displayed trace reductions and member-wise
refinements do not survive at their stated scope:

1. condition (F) makes the parent connection flat and the flux external, but it
   does not make the unselected odd finite map `Phi` scalar on `E_parent`.
   Therefore (F) alone cannot replace the trace over
   `L2(Sigma_BR,S_Sigma tensor E_parent)` by `16` times a trace over
   `L2(Sigma_BR,S_Sigma)` while leaving `Phi^dagger Phi` inside the latter.
2. the displayed `(F)+(S)` sum and the member-A `+1` suppress the three radius
   denominators. The sealed tower calls the denominator-free form a
   **unit-radii** form, while the rebuild's freedoms block says the radii remain
   parameters and that nothing was substituted.
3. the simple `T2 + S2` spectral floors used for the member bounds also require
   the flat/external parent specialization. The sealed source says that without
   it the parent factor is twisted and **the spectrum itself changes, not merely
   the count**. Thus the two refinements are not unconditional over the declared
   family, even though they remain unconditional in `Phi` after (F) is imposed.

No use of `mu^2=1` was found. No dead uniform item `U2`, `U5`, or `U7` was
silently reinstated. The failure is a condition-and-carrier failure, not a
return of D1.

---

## 0. Preflight, custody, and gates

### 0.1 Pickup and output

- the relay file and its sidecar verified before use;
- `PROGRAM_STATE_BRIEF_V004.md` verified at
  `50f2628638848b101d41294a009c96197ee214140ddba714fa7ac58e71e059c5`
  and read before task work;
- `relay_outbox/783_ACK.md` was written before reading the relay;
- the output artifact and sidecar were absent before the first write;
- the subject and adjacent seal verified at the digest stated above.

### 0.2 Source-pin verification

Every source used below was verified before its content was consulted.

| object | verified SHA-256 | result |
|---|---|---|
| `STAGE8_7A_PUBLIC_LAYER_CROSSCHECK_CODEX2_V001.md` (778) | `54d2af923f1b32a5f9327d905f0b74615cc1dcb6d62bee9337ff3b2e2ff87d1d` | adjacent seal OK |
| `STAGE8_7A_TOWER_CONTEST_DARIO_V001.md` (768) | `03db8d3da273f42c62acdea5d453ec0b780934c73aa897fdf2cfb986c0e7bc9b` | adjacent seal OK |
| `STAGE8_7A_DBR_FAMILY_BUILD_DARIO_V001.md` (777) | `da8720a43a9b4edae7dfdb833c92f0c3e3169a0ca00837c915fe7e086bbc3c5a` | adjacent seal OK |
| `STAGE8_7A_DBR_PUBLIC_LAYER_CAMPAIGN_DARIO_V001.md` (775) | `083e86e357a63e0ae6cec707e966f14e4161f9c6ece169f852c3231f8df5c450` | adjacent seal OK |
| `STAGE8_7A_TOWER_REBUILD_DARIO_V001.md` (764) | `84ceeb49dd282736ce0cb1347e923c8a8c9b1d26ea151ccbb19f6d857dd9e0bf` | adjacent seal OK |
| `STAGE8_7A_FLUX_CORRESPONDENCE_DARIO_V001.md` (770) | `3c6cd9a2ee1b6ea1093370e9868c93a200c3631317bb91ecaf3ec9153a744c0b` | adjacent seal OK |
| `alpha_global_record_surface_superconnection_principle_v001.md` (PRIN) | `ae1d04922cb37f8b5631a11551b7db57f483bd6b0d8b7c54d59b4f4ae593768f` | byte-exact to the content pin carried by the sealed stock; custody not upgraded |
| `STAGE8_BR_CLOSURE_OPERATOR_STRUCTURAL_SPECTRAL_GAP_DETERMINATION_V001.md` (GAP) | `e2fc00d21fdc4a1844648b7248140ab05d9205a652a2b42330c1a366d53e33ed` | adjacent seal OK |
| `DECISION_SELECTOR_OPEN_AND_GAP_CLASSIFICATION_2026-08-09.md` | `cbdc9432de77b29b4ec5fcf1f4f1e9bfb4a185f661b656b98b56103a39257bfb` | adjacent seal OK |
| `LOCKED_PROCESS.md` | `9bc4a8fad15ef5c711b2ebf9b2ae07012308be6d04aaf2fa12ce2d89b7140074` | adjacent seal OK |
| `DECLINE_REGISTER_V002.md` | `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a` | adjacent seal OK |
| `QUESTIONS_SETTLED_REGISTER_V001.md` | `e99e22811a5bcddbd51c0e1fa57e4aa9262e890d13e6bb9e0c7565d387a48dbf` | live-appended current bytes; adjacent seal OK |

PE-1 through PE-6 remained pointer-known and zero-weight. None was opened,
searched, or consulted.

### 0.3 Decisive evidence spans

| ref | source; exact half-open span; span SHA-256 | meaning tested |
|---|---|---|
| E1 | PRIN `ae1d0492...`; `[867,1483)`; `f15851ffccd6d14b959b0fb7d33799bdb663da4a33dea4cf8c6c2af92a3ff19b` | `H_BR=L2(Sigma_BR,S_Sigma tensor E_parent)` and `Phi` is the odd finite map in the one superconnection. |
| E2 | 768 `03db8d3d...`; `[10764,11705)`; `d08cccc778b13b4422097cefba00247c28f7dbe960668481328684ec16274dc2` | exact `H_0` form, `N_lattice`, the conditional flat `x16`, and unit-radii status. |
| E3 | 764 `84ceeb49...`; `[13149,13997)`; `8c086fe9adc97ab527bc3371ddc162167e301b45135529863e1f96106cf11dda` | (F)'s full content; without it the parent factor is twisted and the spectrum itself changes. |
| E4 | 764 `84ceeb49...`; `[10978,11596)`; `e66086c6f5aeb2a7ca3becdf42cdadf82dcee6aeeb5596380a1937188436baf2` | the unspecialized tower carries `R_T`, `R_Q`, and `r_flux`; the denominator-free form is recovered at unit radii. |
| E5 | 764 `84ceeb49...`; `[7207,8921)`; `1bd5e453c2ee88868103b60c5a8847f4d24849315d1fce67333ee5bf1a7d1e28` | the fixed chiral 16 is irreducible, so its quadratic Casimir is one scalar, albeit convention-carrying. |
| E6 | 778 `54d2af92...`; `[12579,14246)`; `1b2adfbcab3f5a2d1a4deabba702e472d877ee8d3c98f18e3a70e5d783198a0a` | the admissible symbolic witness attaining `C2_parent`. |
| E7 | GAP `e2fc00d2...`; `[10402,11576)`; `7c15e2129d58ec21e66c259fc7ab4afb3bc132c6016567b3653b3255dd3ea403` | unselected profiles and twists can carry kernels; positivity is not uniform coercivity. |
| T1 | subject `d55b6445...`; `[6144,9002)`; `97385f9e581c5768deb228b777085095017f40221ce5aa7b3f622264ef3d34fb` | all three claimed trace tiers. |
| T2 | subject `d55b6445...`; `[9002,11901)`; `120401548fdef8f9d4c485bd7a3c05180f320b1130fe1efa97f217b1e80110e4` | tight global bound, member refinements, and the conditional-bottom correction. |
| T3 | subject `d55b6445...`; `[18579,21002)`; `9895a2f7fcf5c11a22c67f60197bbdf6081d20bd603a7a4c93db79f4eabb0636` | freedoms and flattening blocks. |

### 0.4 Gates

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member binding = none
fixed-point execution = none
end test = none
physical-quantity numeric evaluation = none
measured-constant comparison = none
determinant evaluation = none
bundle-class adoption/elimination = none
```

Only exact operator inequalities, byte comparisons, symbolic substitutions,
and finite custody checks were performed.

---

## 1. AS1 — the three trace tiers

### 1.1 Unconditional tier — CONFIRMED

The irreducible functional

```text
Tr_{H_BR} f(D_(Sigma,A)^2 + Phi^dagger Phi + C2_parent)
```

is the correct unconditional level. It does not claim a joint eigenbasis and
does not turn `Phi^dagger Phi` into a number. This is compatible with E1 and
E2.

One analytic input remains implicit: the class of admissible test functions
`f`. The earlier campaign expressly says convergence requires decay and that
no `f` was chosen. That omission affects the freedoms audit in §5; it does not
invalidate this formal functional identity.

### 1.2 Under (F) alone — REFUTED

The rebuild writes

```text
16 * Tr_{L2(Sigma_BR,S_Sigma)}
     f(D_(Sigma,A)^2 + Phi^dagger Phi + C2(16)).
```

This has no lawful receiving space for `Phi^dagger Phi`.

E1 puts the odd finite map in the same superconnection on
`S_Sigma tensor E_parent`. Condition (F), quoted correctly from E2/E3, says
that the flux `U(1)` is external to `Spin(10)` and the parent connection is
flat (E3 sharpens this to trivial holonomy on both circles). That makes the
geometric Dirac part act identically on the flat parent multiplicity and makes
`C2_parent` scalar on the irreducible 16. It says nothing that makes the
unselected finite map `Phi` act as one scalar on all 16 internal directions.

The lawful (F)-only surface is therefore still

```text
Tr_{L2(Sigma_BR,S_Sigma) tensor E_parent}
  f(D_base^2 tensor Id + Phi^dagger Phi + C2(16) Id),
```

not `16` copies of one base trace. The factor `16` becomes extractable only
after a separate scalarity condition on `Phi^dagger Phi`; that is work done by
(S), not by (F).

### 1.3 Under (F)+(S) — PARTLY CONFIRMED, displayed formula REFUTED

When `(S)` is read as
`Phi^dagger Phi = mu^2 Id` on the full carrier, constant and commuting, the
internal obstruction in §1.2 disappears. The eigenvalue and multiplicity
structure then reduces, and the rebuild correctly carries
`N_lattice(p_t,p_q)` explicitly:

```text
2 * N_lattice(p_t,p_q) * d_S2(ell) * 16.
```

No lattice multiplicity is suppressed.

But `(F)+(S)` is not enough for the exact sum printed in T1. E4 gives the
unspecialized geometric part as

```text
p_t^2/R_T^2 + p_q^2/R_Q^2 + ell(ell+2|q|)/r_flux^2,
```

and says the denominator-free form is recovered at **unit radii**. The rebuild
prints the denominator-free form while its freedoms block says the radii are
carried as parameters and `SUBSTITUTED: none`. The corrected upper tier is
therefore either:

```text
(F)+(S)+unit-radii convention,
```

or the same sum with all three radius denominators restored. As printed, the
third tier silently specializes a free datum.

### 1.4 D1 and the two specific hunts

- `mu^2=1` occurs only inside the visibly declined member of the `(S)` family.
  No proof, bound, or later disposition consumes it.
- `N_lattice` is explicit in the full sum and in the surrounding qualification.
  No suppression was found.

Verdict:

```text
unconditional functional       CONFIRMED
(F)-alone 16-fold base trace   REFUTED — Phi still acts on E_parent
(F)+(S) full sum               REFUTED AS PRINTED — unit-radii condition omitted
D1 consumption                 NONE
N_lattice suppression          NONE
```

---

## 2. AS2 — the universal bound and tightness

### 2.1 Positivity — CONFIRMED

For the displayed `H_0`,

```text
D_(Sigma,A)^2 >= 0,
Phi^dagger Phi >= 0,
C2_parent = scalar on the fixed irreducible 16.
```

Thus, in the carried normalization,

```text
H_0 >= C2_parent * Id
and therefore lambda >= C2_parent.
```

This needs neither (F) nor (S). Flatness controls separation of the parent
factor, not the scalar action of the central quadratic Casimir on one
irreducible representation. E5 supplies exactly that distinction. The
normalization is free, so the statement is symbolic within any carried
normalization; no numerical Casimir was adopted.

E7's statement that positivity does not force a **strictly positive public
gap** does not contradict this result. `C2_parent` itself is convention-
carrying and the public quotient is unbuilt; the surviving statement is only
the relative operator floor shown above.

### 2.2 Attempted violation — none

Any violation would require a negative expectation from at least one of
`D^2`, `Phi^dagger Phi`, or the scalar Casimir shift. The sealed definitions
give no such admissible term. Noncommutation between the first two positive
operators does not defeat positivity of their sum.

### 2.3 Tightness and attempted strengthening — CONFIRMED

E6 supplies one admissible symbolic completion:

```text
q = 1/2; ell = 0; periodic torus zero label; Phi = 0;
flat external parent arm.
```

The geometric and `Phi` contributions then vanish and the state attains
`lambda=C2_parent`. This is an adversarial witness against a universal
strengthening, not a selected family member. Hence no bound
`lambda >= C2_parent + epsilon` with a sealed strictly positive `epsilon` can
hold over the whole admissible family.

---

## 3. AS3 — bounds versus bottoms

### 3.1 The two printed member bounds — REFUTED at claimed scope

The rebuild argues from

```text
D_(Sigma,A)^2 = D_(T2)^2 + D_(S2,A)^2
```

and then imports the simple sphere floors `1` for member A and `0` for kind B.
That is not an unconditional identity for the declared operator family.

E3 says expressly that when (F) is absent the flux may twist the parent factor
and **changes the spectrum itself, not merely the count**. The parent
connection/class remains free. Therefore the base labels `p2min`, `ell`, and
the simple `S2` floor do not provide an unconditional spectral lower bound for
`D_(Sigma,A)^2` across all admissible parent connections.

There is a second independent scope error. Even after (F), E4 gives the
member-A sphere gap as `1/r_flux^2`, not `1`, unless the unit-radius convention
is imposed. The correct stock-supported refinements are therefore:

```text
under (F), for every admissible Phi:
  lambda_A >= p2min + 1/r_flux^2 + C2_parent
  lambda_B >= p2min + 0          + C2_parent

and at unit radii only:
  lambda_A >= p2min + 1 + C2_parent
  lambda_B >= p2min     + C2_parent.
```

No new bound for the non-(F) family is authored here. The sealed stock says its
spectrum changes but does not supply a replacement universal decomposition;
the proper response is to refuse the unconditional formulas.

### 3.2 Bottom claims

Scalarity condition (S) removes the noncommuting-`Phi` obstacle to locating a
bottom from a known base spectrum. It does not flatten the parent connection
and does not set the radii. Consequently the rebuild's statement

```text
the two bottoms separate by exactly 1 under (S)
```

is too strong. The stock-supported form is:

```text
under (F)+(S): the bottoms separate by 1/r_flux^2;
under (F)+(S)+unit radii: the bottoms separate by exactly 1.
```

The rebuild was right to withdraw the unconditional bottom claim from 777,
but it stopped one condition short and retained the unit-radius number.

### 3.3 Counterexample search

- `Phi` alone cannot violate the corrected (F)-conditioned bounds because
  `Phi^dagger Phi >= 0`.
- the open parent connection can invalidate the imported base spectral floors;
  E3 is the sealed exhibit that the spectrum changes outside (F).
- an arbitrary radius changes the member-A gap from `1` to
  `1/r_flux^2`; this is already an exact symbolic counterexample to the
  literal unit coefficient, with no physical radius evaluated or selected.

Thus the problem is not the `+1`'s sphere provenance. Its provenance is sound;
its unconditional coefficient and its unstated carrier conditions are not.

---

## 4. AS4 — salvage ledger

### 4.1 Dead items

| item | attack result |
|---|---|
| `U2` fixed eigenvalue form with the D1 `+1` | **NOT CONSUMED.** The rebuild keeps `Phi^dagger Phi` operator-valued except in the named (S) family. |
| `U5` universal `lambda >= 1+C2_parent` | **NOT CONSUMED.** The surviving universal bound is the tighter-scoped `lambda >= C2_parent`; the displayed `mu^2=1` line is declined. |
| `U7` uniform branch boundary | **NOT CONSUMED.** The later A/B table uses the class-dependent `C6` disposition: absent for A, present for B. |

### 4.2 Demoted C4

The rebuild consistently labels the A/B expressions as **bounds** outside its
bottom discussion. It does not silently rename them bottoms. That part of the
salvage discipline is confirmed.

The condition attached to the later bottom statement is nevertheless
incomplete: (S) removes the `Phi` obstruction, while (F) and the radius carrier
remain necessary. This is a new scope defect in the reconstruction, not a
silent resurrection of the old C4 bottom table.

### 4.3 Twelve-item carriage

The twelve dispositions from 777 are all represented in the rebuild's salvage
table: family, integer-affine parameter, member A validation, Z/P partition,
cardinality fork, C4 demotion, bound separation, intra-B weight variation,
`U7 -> C6`, six free choices, four gaps, and the old U5 attainment withdrawal.
No item is silently dropped. The parent-flatness and radius findings above
qualify three of those dispositions; they do not change the finite census.

---

## 5. AS5 — freedoms consumed

### 5.1 Named physical freedoms

The block names the seven physical/spectral data it discusses: `Phi`, parent
bundle/class, `C2_parent`, torus spin structure/`p2min`, radii/`beta`, bundle
class/chiral index `n`, and `N_lattice`. No D1 value, class, member, radius, or
Casimir number is affirmatively adopted.

### 5.2 The block is not complete

Three receiver failures remain:

1. **test function `f` is missing.** Every trace tier consumes `f`, while the
   preceding campaign says convergence requires a decay condition and that no
   `f` was chosen. The rebuild should carry it as an unselected analytic
   argument and distinguish the formal functional from a trace-class value.
2. **the radii are listed but not carried into the formulas.** E4 supplies all
   three denominators. T1 omits them, and T3 nevertheless says
   `CARRIED-AS-PARAMETER` and `SUBSTITUTED: none`. That is a hidden unit-radius
   specialization.
3. **the parent connection is listed but its consumption is mislocated.** The
   block attaches (F) to the trace sections only. The member bounds and bottom
   statements also consume (F), because E3 bars the simple product spectrum
   outside it.

Accordingly `SUBSTITUTED: none` is refuted for the printed scalar sum and
member-A `+1`: the unit-radius form is substituted while the radii are declared
free. No numerical physical radius was evaluated here; the contradiction is
between two symbolic forms already present in sealed stock.

---

## 6. Battery and self-audit

### 6.1 F_PLDEC and M-2

F_PLDEC: no physical quantity was numerically evaluated; no measured constant
was consulted; no determinant, member, endpoint, fixed point, or junction map
was evaluated.

M-2 covered:

- `Phi^dagger Phi` / `Phi†Phi` and split-line occurrences;
- `unit radii` / `unit-radii`, each of the three radius names, and denominator
  forms;
- `flat parent`, `external to Spin(10)`, `trivial holonomy`, and split forms;
- `N_lattice` and its displayed/suppressed variants;
- `bottom` / `bound` and hyphenated forms;
- `U2`, `U5`, `U7`, `C4`, and `C6` at table and summary locations.

The meaning-bearing exhibits are definition/procedure spans, not glossary,
requirement, or same-name/different-object hits.

### 6.2 Jurisdiction

This report tests universal statements against the subject's own open family.
It adopts no counterexample member and supplies no selector. Conditions (F),
(S), and unit radii are classified as conditions; none is installed as a fact.
The corrected conditional formulas are scope repairs, not new physics.

### 6.3 Self verb audit

Clean. The report distinguishes:

- a refuted claimed equality from an uncomputed alternative;
- a tight family-wide floor from an unbuilt public gap;
- a symbolic counterexample from member adoption;
- a missing condition from a false operator identity;
- a formal functional from a convergent trace.

No verb claims proof authorization, alpha computation, kappa computation,
determinant evaluation, class selection, or physical numerical evaluation.

---

TRACE_TIERS = REFUTED (unconditional functional confirmed; F-alone factorization lacks a scalar Phi carrier; F+S sum also omits the unit-radii condition)
D1_CONSUMED = nowhere
BOUND_TIGHT = CONFIRMED
MEMBER_BOUNDS = REFUTED (unconditional scope; require F, and the literal +1 additionally requires unit radii)
DEAD_ITEMS_CONSUMED = nowhere
FREEDOMS_BLOCK = INCOMPLETE (missing f; radii silently specialized; parent-condition consumption omitted at member bounds)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
