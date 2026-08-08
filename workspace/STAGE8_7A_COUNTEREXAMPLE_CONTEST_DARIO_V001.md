# STAGE 8 / 7A / STEP 8 — THE COUNTEREXAMPLE: CONFIRMED, AND THE CORRECTED VERDICT

**Lane:** Dario (Opus 5, cross-family from the Codex build lanes)
**Date:** 2026-08-08
**Scope:** PASTE 738 only — TT1 recompute, TT2 require-test, TT3 corrected verdict
**Custody:** archive-side read and write; the registrar owns any mirror
**Governing:** the refutation `97587de8…`; my 733 `c434f392…`; VOID in force
**Charge:** re-derive, not trust — including when what I am re-deriving is my own refutation.

## Lead determination

```text
COUNTEREXAMPLE = CONFIRMED (exact).  I rebuilt it from nothing -- my own Kuhn
   complex, my own Whitney forms, my own quadratic -- and every number reproduces:
   33 free edges, rank 33, E_min = 191/252, E(x_alt) = E(x_F) = 1, 22 of 33 values
   differing, and all three named edge values (1/7, -1/7, 1/3) to the digit.
   I add two checks Codex did not display, and both go against me:
     -- all 24 coarse square-face fluxes reproduce (I verified, not assumed);
     -- x_alt - x_F is NOT a coboundary.  The difference is PHYSICAL, not gauge.
   My FORCED(Branch F) falls.  No divergence to display.

REQUIRE_KILL = NONE FOUND, and the reason is worth the principal's eye: the one
   clause that WOULD kill x_alt -- C_ref's "preserving the same smooth coframe and
   connection", which would force the refined field to be one global form's
   sampling -- is the clause BARRED AS A SOURCE.  x_alt survives every unbarred
   require, including all three of my own locks.

CORRECTED VERDICT
   FORCED: the ENERGY.  sum F^2 per cell transports exactly -- E(x_alt) = E(x_F)
           = 1 = parent -- and my 733 bulk-residual argument stands where it was
           actually proved: the equal two-child cubical bisection share family.
   FREE:   the ASSIGNMENT on the simplicial move.  A 32-dimensional equal-energy
           set through x_F, with an explicit non-gauge member.

DOWNSTREAM = the decisive question, and the answer is NOT uniform.  Three of the
   four named consumers take the energy; ONE does not.  V011's generated face
   response is a BILINEAR FORM ON F_phys evaluated at particular xi, not a
   function of sum F^2.  That is where the ruling lives, and §3.3 names it.
```

---

## 0. Preflight

[PROVABLE] `relay_outbox/738_ACK.md` was written **before** source work. Lane guard:
the header names **DARIO**. Read only after its sidecar verified:

```text
relay_inbox/RELAY_PASTE_738_COUNTEREXAMPLE_CONTEST_DARIO_V001.md
  edbcd0e6071a556d17b7d38c156e1ca5b9bf829785f821cf2af94ad82fe27ade   shasum -c OK
```

[PROVABLE] `STAGE8_7A_COUNTEREXAMPLE_CONTEST_DARIO_V001.md` and its seal sidecar were
probed before the write and returned ABSENT.

### 0.1 Sources verified before use

```text
XCHK  STAGE8_7A_BRANCH_F_CROSSCHECK_CODEX2_V001.md            97587de8…  sidecar OK
733   STAGE8_7A_XI_F_REQUIRE_HUNT_DARIO_V001.md               c434f392…  (mine)
V011  review_packets/.../BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md  aa7c6d49…
MAJ   workspace/stage8_execution/work/MAJORANT_PHASE2_O3_O7_PROOF_DRAFT_V001.md 08b91543…
R33R  R3_3_INTRINSIC_CELL_MEASURE_DERIVATION_RESULT_V001.md   e60aec3c…  (packet D038)
CARR  STAGE8_7A_R9JII_JOINT_LANDING_TEST_V001.md              5f4979d5…
```

### 0.2 Gates and method

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

No common cell formed, no junction map evaluated, no member bound, **no physical
quantity evaluated numerically**. All arithmetic below is exact rational
(`fractions.Fraction`) structural computation on the displayed finite interfaces, which
the relay names as the task. No floating point. Nothing adopted. No register, plan,
tracker, git action.

---

## 1. TT1 — THE INDEPENDENT RECOMPUTATION

### 1.1 Method — built from nothing, not checked against theirs

[YOURS] I did not verify Codex's arithmetic by re-reading it. I constructed the object
myself and compared only at the end:

```text
complex     Kuhn/Freudenthal order-simplices: for each permutation of (0,1,2,3),
            the monotone vertex chain (0,0,0,0) -> ... -> (1,1,1,1).
edges       all comparable pairs u < v in {0,1}^4.
potential   A = x_0 dx_1 ; edge value = exact line integral
            int_u^v A = (v_1-u_1)(u_0+v_0)/2.
per simplex barycentric gradients g_i by exact 5x5 inversion of [1, v_j];
            Whitney 1-form A = sum_(i<j) a_ij (lam_i dlam_j - lam_j dlam_i);
            F = dA = 2 sum_(i<j) a_ij (g_i wedge g_j)   -- constant on the simplex.
energy      E = sum_(24 simplices) (1/24) * sum_(mu<nu) F_(mu nu)^2       [V011's form]
```

### 1.2 The numbers

| Quantity | Codex `97587de8…` | **My independent value** | Agrees |
|---|---|---|---|
| simplices | 24 | **24** | ✔ |
| vertices | 16 | **16** | ✔ |
| edges | 65 | **65** | ✔ |
| parent cube edges fixed | 32 | **32** | ✔ |
| new/free edges | 33 | **33** | ✔ |
| `rank(Hessian(E))` | 33 | **33** | ✔ |
| `E(Branch-F)` | 1 | **1** | ✔ |
| `E_min` | **191/252** | **191/252** | ✔ |
| `E(x_alt)`, `x_alt = 2x_min − x_F` | 1 | **1** | ✔ |
| new-edge values differing from `x_F` | 22 of 33 | **22 of 33** | ✔ |
| `(0,0,0,0)→(0,1,0,1)` | `x_F=0`, `x_alt=1/7` | **0, 1/7** | ✔ |
| `(0,0,0,0)→(1,0,0,1)` | `x_F=0`, `x_alt=−1/7` | **0, −1/7** | ✔ |
| `(0,0,0,0)→(0,1,1,1)` | `x_F=0`, `x_alt=1/3` | **0, 1/3** | ✔ |
| simplex-0 components `(01,02,03,12,13,23)` | `(1,−43/84,−13/84,43/84,13/84,0)` | **identical** | ✔ |

```text
ARITHMETIC DIVERGENCE = NONE.  Every displayed value reproduces exactly.
```

### 1.3 Two checks Codex asserted and I verified rather than accepted

[PROVABLE] **(a) Coarse-flux reproduction.** I enumerated the cube's 24 oriented square
2-faces and evaluated each face's circulation under both cochains: **all 24 agree
exactly.** (It is in fact forced — the 32 parent edges are held at their exact values
and a square face's flux is their signed sum — but the relay asked me to check it, and
"forced" is a reason, not a substitute.)

[PROVABLE] **(b) The difference is not gauge — and this is the check that decides
whether the counterexample is real.** I solved `d_0 lambda = x_alt − x_F` over all 65
edges and 16 vertices by exact elimination: **the system is inconsistent.** So
`x_alt − x_F` is *not* a coboundary, the two cochains are not gauge copies, and their
field content genuinely differs — as the simplex-0 component vector independently shows
(`(1,−43/84,…)` versus `(1,0,0,0,0,0)`).

[YOURS] Had this come out the other way, the counterexample would have collapsed into a
gauge artifact and my verdict would have survived. It did not. I record that I looked
for that escape first.

[PROVABLE] **(c) `im(d_1')` membership** is immediate and needs no check: `xi' = d_1'
x_alt` by construction, so it lies in the image by definition.

```text
COUNTEREXAMPLE = CONFIRMED (exact).  My FORCED(Branch F) verdict of 733 FALLS.
```

### 1.4 What survives of 733, stated precisely

[PROVABLE] **L1 stands.** The ruled subject is `sum F^2` identically; nothing here
touches it, and Codex confirms it.

[PROVABLE] **L2 stands where it was actually proved** — the equal two-child cubical
bisection with shares `s`, `1−s`, where the residual `V F^2 (2s−1)^2` is bulk and only
`s = 1/2` survives. Codex's own sub-verdict is scoped identically: *"CONFIRMED for the
stated equal two-child bisection."*

[YOURS] **Neither of us has done a full cubical free-space analysis** of the kind I have
now done for Freudenthal. My 733 argument quantified over a one-parameter share family;
the general cubical move has its own new-edge free space, and whether an equal-energy
non-F survivor exists there is **open and untested**. I flag it because "the cubical
assignment is forced" is the natural reading of both artifacts and neither of us has
earned it in general.

[PROVABLE] **L3 falls with the verdict.** My two bars (R7 shape-dependent scalar, R9
intrinsic-cell binding) do not reach `x_alt` — §2.

---

## 2. TT2 — TESTING `x_alt` AGAINST EVERY REQUIRE

Each of 733's nine requires, tested against the confirmed survivor.

| # | Require | `x_alt` |
|---|---|---|
| R1 | `F_phys = im(d_1)` | **S** — `xi' = d_1' x_alt` by construction |
| R2 | A26 lift, representative-independence, zero-flux additions fail | **S** — a distinct `xi'` with its own unique `Q_flux` lift |
| R3 | min-norm determinacy | **S** — operates downstream of `xi'`, on any branch |
| R4 | `d_1 d_0 = 0` gauge | **S** — and §1.3(b) shows the difference is not in the gauge orbit |
| R5 | the measure / `xi = ell ell F` | **S** — used to build it |
| **R6** | invariance up to a boundary term whose ratio → 0 | **S — residual exactly ZERO.** The lock that carried 733 is *satisfied*, not merely evaded |
| **R7** | no residual shape-dependent scalar | **S** — `x_alt` is an edge cochain, not a weight multiplying the measure; no compensator is inserted |
| **R9** | may not retain a weighting profile from an arbitrarily chosen parent | **S** — `x_alt` is not a parent-inherited profile; it is a distinct configuration |
| R8 | the subject ruling | **S** — the subject is `sum F^2`, which it matches |

### 2.1 The hunt for a kill, by meaning

[PROVABLE] Probing by meaning (733's rule), recursive over `workspace/**` +
`supervision/**`, `*.md`, writer-excluded: `cell-local` (10), `locally determined` (0),
`determined by that cell` (0), `local rule` (1), `global minimization` (1),
`cell-by-cell` (1), `orientation covariance` (55), `presentation independence` (4),
`computed using that cell's own` (2). Every candidate was opened.

[YOURS] The most promising line was **locality**: `x_alt` is produced by a *global*
33-dimensional minimization and reflection, so its per-simplex components are not
computed from that simplex's own data. If the corpus required the refinement rule to be
cell-local, `x_alt` would die.

**It does not.** R3.3's clause — *"computed using that cell's own `V_cell`, state,
generator, and measure"* — governs how the **response is assembled on a given cell**,
not how the field configuration is *chosen*. `x_alt` does use each simplex's own
`V_cell = 1/24` and its own `F`. Reading it as a locality constraint on the rule would
be stretching a require past its own text, which is the failure mode I have charged
elsewhere and will not commit here.

### 2.2 The one clause that would kill it — and it is barred

[YOURS] There **is** a clause that kills `x_alt` cleanly. `x_alt`'s per-simplex fields
differ from one another, so the refined configuration is **not** the sampling of a
single global 2-form; `x_F` is. `C_ref`'s third family — *"common refinements preserving
the same smooth coframe and connection"* — demands exactly that global object, and would
therefore exclude `x_alt` at once.

**That clause is BARRED AS A SOURCE** (TYPE-R), the relay restates the bar, and I
decline to use it. Recording it is the honest move: the principal should know that the
survivor survives *because of a bar the program imposed on itself*, and that lifting the
bar is not available (DoR-007 forecloses it) — so this is not a latent escape, it is a
structural feature of where the program stands.

```text
REQUIRE_KILL = NONE FOUND.  x_alt satisfies every unbarred require, including all
three of my own 733 locks.
```

---

## 3. TT3 — THE CORRECTED VERDICT, AND WHAT DOWNSTREAM ACTUALLY NEEDS

### 3.1 What refinement forces

```text
FORCED
  THE ENERGY.  sum_(mu<nu) F^2 per cell, i.e. the ruled intensive quadratic
  coefficient, transports EXACTLY across the Freudenthal move on the whole
  equal-energy set: E(x_alt) = E(x_F) = 1 = V_parent * ||F_parent||^2.
  Functoriality of the MEASURE is therefore not at risk from this freedom at all.

  THE CUBICAL ASSIGNMENT, within the equal two-child share family only (§1.4).

FREE
  THE ASSIGNMENT ON THE SIMPLICIAL MOVE.  E is a rank-33 positive-definite
  quadratic with E_min = 191/252 < 1, so the level set {E = 1} through x_F is a
  32-DIMENSIONAL ellipsoid.  Branch F is ONE POINT on it.  x_alt is an explicit,
  exactly-rational, non-gauge second point.
  DIMENSION OF THE FREE SET = 32.
```

[YOURS] The structural reason is worth stating because it makes the result robust
rather than a curiosity: **once `E_min < 1` strictly and the form is nondegenerate, an
equal-energy non-`F` point exists automatically.** The reflection is only the easiest
witness. No further search is needed and no finer construction can remove it.

### 3.2 The decisive question — energy or assignment?

For each named consumer: does it consume `sum F^2`, which is functorial on the whole
class, or per-face `F`, which needs the free datum?

| Consumer | Consumes | Basis |
|---|---|---|
| **RA27-2's discharge** | **energy** | its demand is the measure's refinement functoriality; §3.1 gives it on the whole set |
| **T_ref's instance transport** | **energy** | the sealed density instance carries intensive logs over `N_4` — a per-cell scalar density, not a face-indexed object |
| **J2 / the junction's one-object comparison** | **energy-level** | the carrier's J2 tests *"their common value"* — the declared cross-sector unit `u(e)`, a scalar — for invariance under re-presentation, not a per-face field |
| **V011's generated face response** `mathcal_K_L(xi,zeta) = R_record,L(Q_flux xi, Q_flux zeta)` | **THE ASSIGNMENT** | it is a **bilinear form evaluated at particular `xi, zeta in F_phys`**, not a function of `sum F^2`. Two equal-energy cochains give different `xi`, hence different `Q_flux xi`, hence different response values |

```text
DOWNSTREAM_NEEDS = NOT energy-only.  Three consumers take the energy; the generated
face response takes the assignment.
```

### 3.3 So the freedom is gauge for most of the program — and not for one thing

[PART-PROVABLE] For **RA27-2, T_ref and the junction comparison**, the 32-dimensional
freedom is invisible: every member of the equal-energy set delivers the same subject,
the same transport, and the same scalar unit. **For those three, the freedom is gauge
in the program's own sense and no ruling is needed.**

[PART-PROVABLE] For **the generated face response**, it is not. `mathcal_K_L` is
evaluated at particular flux arguments; `x_F` and `x_alt` supply different ones. **That
is where the ruling lives.**

[YOURS] And the ordering matters: the subject ruling makes the response *the source of*
the coefficient and expressly **not identified with it**. So the object that needs the
assignment sits **upstream** of the object that does not. A ruling that fixed the
assignment for the response would settle the whole chain; a ruling that fixed only the
coefficient would leave the response's arguments undetermined and would not.

[YOURS] What I do **not** claim: that the response's dependence on the free datum is
*material* — i.e. that `mathcal_K_L` actually differs on the pairs the program will
evaluate. Establishing that would require evaluating the response, which the gates and
the void condition both bar here. I name the consumer and its type; whether the
difference survives into the quantities that matter is the next question, and it is not
mine to compute in this relay.

### 3.4 What this does and does not change

```text
UNCHANGED   the measure's functoriality (the 727 finding stays resolved -- on the
            whole equal-energy set, not merely on Branch F);
            the R9-JII carrier REMAINS PENDING on its common-cell quantifier;
            T_ref fields 2, 4-8 and the S5.3 burden;
            lambda/beta, still open and independent.
CHANGED     733's FORCED(Branch F) -> the ENERGY is forced, the simplicial
            ASSIGNMENT is free (dim 32);
            RA27-2's discharge no longer waits on a branch ruling -- it consumes
            the energy, which the whole class supplies.
NEW         Branch F's im(d_1') side condition is superseded as "the sharpest open
            item": the sharper one is now WHICH CONSUMER NEEDS THE ASSIGNMENT,
            answered at §3.2, and the cubical free-space gap flagged at §1.4.
```

---

## 4. VOID, GROUNDING, JURISDICTION, VERB AUDIT

### 4.1 VOID attestation

```text
VOID = CLEAN.  No downstream numeric consulted, computed, or estimated.  §1's
arithmetic is exact rational structural computation on the displayed finite
interfaces -- the task the relay set -- with no physical quantity evaluated and
nothing compared to a measured constant.  I did not evaluate the response (§3.3),
precisely because doing so to settle the question would be the move the void
condition bars.  No rule, branch, or member was adopted.
```

### 4.2 Grounding

| # | Step | Basis | Tag |
|---|---|---|---|
| 1 | The sealed Freudenthal construction (24 simplices, `|C|_4 = 1/24`) | `08b91543…[19632,19996)` | PROVABLE |
| 2 | The measure and cell contribution | `aa7c6d49…[45718,46068)`, `[46074,46387)` | PROVABLE |
| 3 | Complex: 24/16/65/32/**33** | my construction | PROVABLE |
| 4 | `E(x_F) = 1` | my exact computation | PROVABLE |
| 5 | rank 33; `E_min = 191/252` | my exact elimination | PROVABLE |
| 6 | `E(x_alt) = 1`; 22/33 differ; three named values | my exact computation | PROVABLE |
| 7 | Simplex-0 components match Codex exactly | my exact computation | PROVABLE |
| 8 | All 24 coarse fluxes reproduce | my exact check | PROVABLE |
| 9 | `x_alt − x_F` is **not** a coboundary | my exact elimination | PROVABLE |
| 10 | `xi' ∈ im(d_1')` by construction | definitional | PROVABLE |
| 11 | Every 733 require satisfied by `x_alt` | §2 table | PART-PROVABLE |
| 12 | No locality require exists to kill it | §2.1, probes displayed | PROVABLE |
| 13 | The killing clause is the barred one | §2.2 | PART-PROVABLE |
| 14 | Free set has dimension 32 | §3.1, from 5 | PART-PROVABLE |
| 15 | Response is a bilinear form on `F_phys` | `aa7c6d49…[45361,45440)` | PROVABLE |
| 16 | Three consumers take the energy; the response takes the assignment | §3.2 | PART-PROVABLE |
| 17 | L2's scope; the cubical free space untested | §1.4 | **YOURS** |
| 18 | The materiality question left uncomputed | §3.3 | **YOURS** |

```text
GROUNDED_STEPS = 16 / 18
YOURS, NAMED: 17 (the cubical scope flag), 18 (the refusal to evaluate).
```

### 4.3 Jurisdiction check

**R6.** Written to catch a coefficient that degrades under subdivision. Applied here
against the survivor and **satisfied by it** — residual exactly zero. I record a require
passing an object I would rather it failed; that is the direction the check has to work
in to be worth anything.

**R7, R9.** Applied and found not to reach `x_alt` (§2). Neither was stretched.

**The barred C_ref clause.** §2.2 records that it would kill the survivor and that I did
not use it. Its bar is DoR-007's, and DoR-007 forecloses lifting it.

**R9-JII.** §3.4 records the carrier still PENDING. Nothing here forms a common cell or
makes the junction test runnable.

### 4.4 Self verb audit

| Verb or status | Warrant |
|---|---|
| `CONFIRMED (exact)` | independent reconstruction; every displayed value reproduced |
| `falls` | my own 733 verdict, on my own arithmetic |
| `not gauge` | exact inconsistency of `d_0 lambda = x_alt − x_F` |
| `NONE FOUND` | nine requires tested, meaning-probes displayed, the barred clause named |
| `energy / assignment` | per consumer, each with its basis; the one that needs the assignment named |
| `not claimed` | §3.3 — materiality of the response's dependence, left uncomputed |

[YOURS] Disclosures against myself:

1. **My 733 verdict was wrong and this relay confirms it against me.** Two consecutive
   relays reversed by cross-family checking, and this time I reproduced the refutation
   digit for digit myself. The lane's charge is re-derive, not trust — including when
   the thing to re-derive is the refutation of my own result.
2. **I looked for the escape first.** The gauge test at §1.3(b) is the check that would
   have saved my verdict; I ran it before writing anything and it went against me.
   Recording that I hunted for it is more honest than presenting the confirmation as
   disinterested.
3. **My 733 locks were the wrong shape, not merely outvoted.** R7 and R9 bar an
   *inserted weight* and an *inherited profile*. `x_alt` is neither — it is a different
   admissible configuration at equal energy. I generalized two bars past the object type
   they name, which is the error I have charged in other lanes.
4. **Neither lane has earned "the cubical assignment is forced" in general** (§1.4).
   Both of us proved it inside a one-parameter share family. I flag it rather than let
   the pair of artifacts imply more.
5. **The most useful thing here is not the confirmation but §3.2**, and I nearly did not
   get to it: the relay had to tell me to ask what downstream consumes. The answer —
   three consumers take the energy, the response takes the assignment — reframes the
   open item from "which branch" to "which consumer", and that reframing came from the
   commission, not from me.
6. No verb here proves, authorizes, computes a physical quantity, binds a member, forms
   a common cell, evaluates a junction map, adopts anything, or grants a seal.

```text
COUNTEREXAMPLE = CONFIRMED (exact) — independently reconstructed; 33 free edges,
    rank 33, E_min = 191/252, E(x_alt) = E(x_F) = 1, 22/33 differing, all three named
    edge values and the simplex-0 component vector identical. Plus two checks of my
    own: all 24 coarse fluxes reproduce, and x_alt − x_F is NOT a coboundary — the
    difference is physical, not gauge. No arithmetic divergence.
REQUIRE_KILL = none found — x_alt satisfies all nine 733 requires including my three
    locks; the only clause that would kill it (C_ref's smooth-coframe preservation) is
    BARRED as a source, and DoR-007 forecloses lifting the bar
CORRECTED_VERDICT = stated (forced: the ENERGY, sum F^2 per cell, exactly, on the whole
    equal-energy set — plus the cubical assignment within the equal two-child share
    family only; free: the SIMPLICIAL ASSIGNMENT, a 32-dimensional equal-energy set
    through Branch F, with an explicit non-gauge witness)
DOWNSTREAM_NEEDS = NOT energy-only. RA27-2's discharge, T_ref's instance transport and
    J2's u(e) all consume the energy — for those three the freedom is gauge in the
    program's sense. V011's generated face response mathcal_K_L(xi,zeta) =
    R_record,L(Q_flux xi, Q_flux zeta) consumes THE ASSIGNMENT: it is a bilinear form
    at particular xi, not a function of sum F^2. THAT is where the ruling lives, and it
    sits upstream of the coefficient by the subject ruling's own words.
VOID = clean
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+6 disclosures at §4.4)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
