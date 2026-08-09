# STAGE 8 / 7A / [PLAN:B2] — THE SEALED GLUING SIGNATURE REQUIRES DENSITY, CURRENT, AND SUPPORT

Lane: CODEX 2. Relay 808. All headline determinations are **CLAIMED** pending registrar cross-check.

## Lead determination

The RA27-4 gluing diagnostic is **not coframe-only**. Its sealed input signature expressly requires a common-refinement cospan carrying

```text
incidence, degree, connection, coframe, volume,
current-density normalization, and support,
```

and it evaluates transported `ResponseData` through `eta_resp`, `r_F^*`, and `Eval`. The signature therefore consumes the density/current/support rows that Dario 806 records as absent.

The gluing test is not run. Returning zero would replace missing response and density carriers by emptiness; returning nonzero would author an obstruction. Both would violate the sealed signature. B2 remains gated on the six absent receiver components `f_g, F_g, s_g, S_g, delta_K', d_g`.

## 0. Preflight, pins, and custody

| object | SHA-256 | result |
|---|---|---|
| `PROGRAM_STATE_BRIEF_V005.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c` | digest and adjacent seal verified; read before task work |
| governing 806, `STAGE8_B1C_RECEIVER_INHABIT_DARIO_V001.md` | `3151fd1a38ab30a5c442339b879c450fd2c00d7013331c08b2c5634effd50277` | adjacent seal verified before reading |
| corrected joint solve 807, `STAGE8_B1A_CORRECTED_JOINT_SOLVE_CODEX2_V001.md` | `9cf9b329bfad1656f91eb75600ca2a60d44853fbe4a1172186beef78e34f1eb9` | adjacent seal verified |
| frontier/support stock, `STAGE8_7A_SUPPORT_AND_FORCING_DARIO_V001.md` | `9685af44cc48f01fb04e57329cedf4f9a871eb393c6d41396179776957287e9b` | adjacent seal verified |
| RA27 specification, `STAGE8_TASK6_A25_A27_SCOPING_LANE2_V003.md` | `74bbb7aa971554f83d5ce2eb38710b6aae38d340055ab31eca1c23379bc685da` | adjacent seal verified |
| stitching scope, `STAGE8_7A_STITCHING_SCOPING_DARIO_V001.md` | `b1a834e7ac972f2176418193774db8a0b31af078f48349a4e985000e5d5803ba` | adjacent seal verified |
| JREF interface, `STAGE8_TASK5_JREF_AND_LOCAL_KERNEL_ESTIMATES_LANE2_V001.md` | `8dd59b35bb9f63f8c8107d438c757c0cb9a110ee1078c173213c6da657bdfb24` | adjacent seal verified |

Decisive spans:

| content | sealed span | span SHA-256 |
|---|---:|---|
| RA27-4 addressed-object and response input signature | D012 `[30747,33958)` | `b6844e3c1b6115d8254ea6db443b802f0e34510ad575c0e3458abcb61988c2f2` |
| RA27-3/4/5 repair rows and dependency order | D012 `[44665,46055)` | `37864971e8898a920d455abbdf22cfb17f6e8baa3c6e0d3bae8f41397fce7f27` |
| JREF response-naturality square and named missing inputs | JREF `[13461,14260)` | `7cf0dd38d08b47b6a3c25fe4596602cb6ca393e61b382b22347e08e52fd83ba9` |
| 806 supplied 4/10 and absent 6/10 component census | 806 `[727,2831)` | `d1f9f3157beb1105ffa93d7adce96d789f895f741bf8442a192821efdaee8058` |
| 807 B1a-interface consequence | 807 `[11933,13254)` | `476028eb8140c1099b70ae1de4b8c520d6ef41db744aefe5393e0c5718d84c43` |

PE-1 through PE-7 were pointer-known only, unopened, unconsulted, and carry zero weight. In particular, PE-1's adjacent subject was not used to interpret or score the signature.

## 1. AS1 — scope determination from the sealed input signature

### 1.1 Addressed cospan signature

D012 defines one addressed source object as

```text
a = (Omega, theta=e dx, A, boundary/support data).
```

It then requires each common-refinement cospan to preserve that same address and states that the cospan must carry

```text
incidence,
degree,
connection,
coframe,
volume,
current-density normalization,
support.
```

This is an input inventory, not an implementation suggestion. `current-density normalization` and `support` occur in the signature itself. Omitting them would change the domain of the gluing map.

### 1.2 Response-map signature

The same sealed span types RA27-4 with the closed carrier chain

```text
r_F^*       : F_phys(K) -> F_phys(R),
eta_resp(r) : ResponseData(K) -> ResponseData(R),
Eval_K      : ResponseData(K) -> Quad(F_phys(K)),
Eval_R      : ResponseData(R) -> Quad(F_phys(R)),
(r_F^*)^*   : Quad(F_phys(R)) -> Quad(F_phys(K)).
```

For `d_K in ResponseData(K)`, the exact diagnostic is

```text
N_r(d_K)
  := [(r_F^*)^* Eval_R(eta_resp(r)d_K)]_resp
     - [Eval_K(d_K)]_resp
  in Q_resp(K),

N_r(d_K)=0 in Q_resp(K).
```

The named response topology/quotient and `eta_resp` are part of RA27-4. The density/current/support carriers feed the addressed realization on which those maps are typed. They cannot be replaced by the already-complete coframe/incidence/volume triple.

### 1.3 Independent JREF confirmation

The JREF interface independently says the top response arrow is absent because there is no completed response assignment on geometric refinements, **density map**, or common-region relation. Later work supplies the common-region grammar and the coframe transport, but 806 confirms that the density/current/support half remains absent. The density requirement is therefore not an inference from naming; it is explicit in both the specification and the interface failure record.

```text
SCOPE = DENSITY-REQUIRED.
```

## 2. AS2 — conditional run disposition

AS2 is conditioned on a coframe-only signature. That condition is false.

The admissible identity transport established by 807 is a lawful member of the corrected B1a family:

```text
identity in joint variety = yes,
a2 member = yes,
joint-family dimension = 1887,
coframe/incidence/Vol_4 transport = supplied.
```

But 806's receiver census is

```text
supplied:     e_K', mu_K', a_K', F_K'                       4/10
absent:       f_g, F_g, s_g, S_g, delta_K', d_g             6/10.
```

Those absent components are exactly the support, current, and density/response transports consumed by the RA27-4 signature. The identity law is therefore admissible as a B1a input but is not a complete input to the gluing diagnostic.

No residual was evaluated:

```text
N_r(d_K) cannot be formed because d_K and eta_resp(r)d_K are absent.
```

This is not a zero obstruction. It is a missing typed argument.

## 3. AS3 — exact gate and correction propagation

The sealed sentence requiring the absent rows is D012 `[30747,33958)`:

```text
the future cospan ... would have to carry incidence, degree, connection,
coframe, volume, current-density normalization, and support.
```

The corresponding response datum and maps are in the same span. Therefore B2 remains gated on

```text
support:  f_g, F_g,
current:  s_g, S_g,
density/response: delta_K', d_g,
```

plus the already-named `eta_resp`/response-carrier realization that consumes them.

Correction propagation under Law 7:

- 807's statement `B2_RUNNABLE = yes at B1a interface` remains true only at that explicitly limited interface.
- It must not be consumed as an overall B2-runnability verdict.
- Overall B2 remains gated because the gluing signature is receiver-complete, not B1a-only.
- 806's proposed scope question is answered: the full receiver rows are required.

No obstruction value or structure exists until the missing inputs are supplied and the exact `N_r` expression can be formed.

## 4. Freedoms consumed

| datum | treatment |
|---|---|
| identity/a2 transport | verified as admissible family input; **not consumed by a run and not adopted as the law** |
| 1887-dimensional B1a family | carried whole; no point selected by desired gluing outcome |
| density/current/support fields | absent; not authored, zero-filled, or inferred |
| `eta_resp`, `Q_resp`, response topology | absent at required realization; no quotient chosen |
| intrinsic `Vol_4` | carried as forced; no alternate measure |
| common-refinement grammar | carried as sealed address structure; no common junction cell formed |
| metric | none adopted |
| smooth constituent | not imported; S26 remains barred |
| electromagnetic identification | none; S08 remains intact |

`SUBSTITUTED = none.` In particular, absence was not substituted by the zero element of `ResponseData`.

## 5. Flattening, gates, and self audit

`FLATTENING_CHECK = clean (37 rows walked).` S26 remains clean: no smooth same-coframe/same-connection constituent supplies the absent maps. S08 remains clean: the finite coframe and response signatures are not identified with electromagnetism, gravity, or a smooth public field. S28 remains clean: no member of the free transport family was selected to force a diagnostic outcome.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member binding = none
fixed-point execution = none
end test = none
numeric evaluation of physical quantities = none
comparison to measured constants = none
curvature claim = none
gravity claim = none
EM claim = none
correspondence-ledger entry = none
common junction cell formed = false
junction map evaluated = false
```

Self verb audit: **NOT CLEAN — one correction.** Relay 807's final `B2_RUNNABLE` line could be read beyond its qualifier “at B1a interface.” This scope pass proves that the qualifier is decisive: the overall gluing test consumes density/current/support and remains gated. The 807 result is narrowed explicitly rather than silently reused.

SCOPE = density-required (D012 `[30747,33958)` explicitly requires current-density normalization and support in the addressed cospan, with ResponseData/eta_resp/Eval carriers)
GLUING_RUN = not run (six required density/current/support components absent; N_r(d_K) cannot be formed)
OBSTRUCTION = n-a
B2 = still gated (on f_g, F_g, s_g, S_g, delta_K', d_g and their eta_resp/response-carrier realization)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+1: 807 overall-runnability reading narrowed to B1a-interface-only)
