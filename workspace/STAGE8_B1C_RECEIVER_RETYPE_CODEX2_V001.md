# STAGE 8 / 7A / [PLAN:B1c-5] — LAWFUL RECEIVER DENSITY RETYPING

Lane: CODEX 2. Relay 811. All headline determinations are **CLAIMED** pending registrar cross-check.

## Lead determination

DS2 dissolves. The opacity in relay 793 was broader than the sealed record requires.

The receiver's density object is not an unknown scalar field and not `tau_density`. On the admitted finite four-cell complex it is the positive intrinsic four-volume density already carried by the supplied `mu_K` field:

```text
delta_K(C) = mu_K(C) = Vol_4(C),  C a four-cell of K,
```

valued in the positive ray of the same R4 volume-unit class as `Vol_4`. Its normalized restriction to a carrier cell `D` is the already-classified measure

```text
mu_D(A)=Vol_4(A)/Vol_4(D).
```

The coframe determines the local density evaluation: `|det e_C|` on a parallelepiped and `|det E_C|/4!` on a four-simplex. This is a type conversion, not a new measure. Relay 806 already lists `mu_K'` among the four supplied components; the opaque `R4Dens` name alone prevented the identity conversion `delta_K' := mu_K'`.

Under the sharp type, `delta_K'` is **SUPPLIED**. The arrow `d_g` is **DERIVABLE-FORCED**: it sends the canonical source density to the canonical target density cellwise, and the reverse aggregation/pullback check is the sealed relation `mu_K=f_g^*mu_K'` on the old image. A0 is identity; A1 and A2 use their intrinsic child volumes; finite composites follow by ordered composition and volume additivity. No density member or scale is selected.

With relay 810's forced `s_g/S_g`, the remaining path to a formable `d_K` has exactly three named nodes: the physical `f_g` bridge, the refinement support map `F_g`, and the completed response carrier/`eta_resp`. This is the same three-way node the principal identifies as adjacent to the lane-opposite AXN probe; that probe is not consumed here.

## 0. Preflight and pin check

The pickup acknowledgement `relay_outbox/811_ACK.md` was written before the relay body was read. The inbox SHA-256 is `cef87e2ad607879993e897a6d14b514893979bfb57c7e837d65bea8d2592a5ca`, matching its adjacent sidecar. The output artifact and sidecar were absent before this write.

The state brief was verified and read first:

```text
PROGRAM_STATE_BRIEF_V005.md
e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c
adjacent seal: OK
```

Decisive sources, all verified before use:

| key | sealed source | SHA-256 | load-bearing content |
|---|---|---|---|
| 810 | `STAGE8_B1C_DENSITY_LAYER_CODEX2_V001.md` | `00e2654a3b48bd8ab5a0bdb41bd48151a9b55c8cd982cb60be3c59a62196b7e5` | `[14109,15826)` classification; `[15826,22152)` assembly path |
| 793 | `STAGE8_B1C_DENSITY_RECEIVER_BUILD_CODEX2_V001.md` | `0c53549766730513635bd35f89cebcc03210ddb6de2531b5eaded4d4b0e23a00` | receiver rows before byte 6965; bridge `[7035,7848)` |
| 806 | `STAGE8_B1C_RECEIVER_INHABIT_DARIO_V001.md` | `3151fd1a38ab30a5c442339b879c450fd2c00d7013331c08b2c5634effd50277` | `[727,2831)` supplied `e_K',mu_K',a_K',F_K'`; `[2836,4821)` conversion table; `[4821,7937)` predicate split |
| CPKG | `STAGE8_TASK5_CONTINUUM_PACKAGE_ADOPTION_PROPOSAL_LANE2_V005.md` | `09883a0d7a5d1329033a09c59ff8d7c843a0098cba569d2a2b97f64f45b2dd95` | `(O1-5)` positive current/volume-density operator dual to `Cof_R` |
| WHERE | `STAGE8_TASK5_EQ6_WHERE_CLAUSES_LANE2_V005.md` | `19b2060392b6e04448c1c13416b87b67decf401246e3414a783b288fdb5d80ec` | `[9332,17064)` field relation, including `[11067,11566)` positivity/duality; `[19497,20512)` forced pullback transport |
| R4-FIELD | `STAGE8_TASK5_EQ6_Q408_PRIMITIVE_GENERATOR_EXHIBIT_LANE2_V004.md` | `c5254f663a1e3a6d1079027184c6dea96a35ab7255a856aa39e584b3d7c32dc2` | `[15287,18485)` current field-member type and conditional density pullback |
| MEAS-ADD | `STAGE8_7A_MEASURE_DENOTATION_SPEC_ADDENDUM_CODEX2_V001.md` | `9ae682eb7834304d329603d50f1b666152899e84f939324aa43d6f138660626d` | `[1517,2544)` intrinsic-volume denotation, unique measure, box/simplex evaluations |
| MEAS-RUN | `STAGE8_7A_MEASURE_ONELINER_CODEX2_V001.md` | `84db6f531e2eb42ee5e4993ed3e9f9e7265df28cfb82cec4b1284ffbb4c1ad8f` | `[3579,7639)` A1/A2/coframe-volume transports and composite rule |
| R33G | packet `R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md` | `e4cfaef14309b3acf5674f8c8faee756f744fec4691d5e01d9de0fa422592be2` | `[98,309)` unique `mu_D(A)=Vol_4(A)/Vol_4(D)` |
| SUPPORT | `STAGE8_7A_SUPPORT_AND_FORCING_DARIO_V001.md` | `9685af44cc48f01fb04e57329cedf4f9a871eb393c6d41396179776957287e9b` | `[13621,14918)` forced intrinsic `Vol_4` denotation and evaluations |
| JOINT | `STAGE8_B1A_CORRECTED_JOINT_SOLVE_CODEX2_V001.md` | `9cf9b329bfad1656f91eb75600ca2a60d44853fbe4a1172186beef78e34f1eb9` | exact A1/A2/common-refinement intrinsic-volume transport and member-existence bearing |
| D012 | `STAGE8_TASK6_A25_A27_SCOPING_LANE2_V003.md` | `74bbb7aa971554f83d5ce2eb38710b6aae38d340055ab31eca1c23379bc685da` | `[30747,33958)` current-density normalization in the addressed signature |
| JREF | `STAGE8_TASK5_JREF_AND_LOCAL_KERNEL_ESTIMATES_LANE2_V001.md` | `8dd59b35bb9f63f8c8107d438c757c0cb9a110ee1078c173213c6da657bdfb24` | `[13461,14260)` response/density square boundary |

All workspace sources with adjacent seals passed `shasum -c`. `R33G` has no adjacent sidecar; its digest and workspace bytes match its entry in `review_packets/STAGE7_QSPEC_CANDIDATE_V001/STAGE7_PACKET_MANIFEST_V001.sha256`. Law 8 is satisfied. PE-1 through PE-9 were pointer-known only, unopened and unconsulted.

### 0.1 Version and supersession probe

The bounded name probe found an earlier V001 primitive-generator exhibit describing a determinant density `mu_o^CTP`. That version was killed on its new-cycle surface claims and is superseded by V004. It is not used. V004 says new-cell `(e_G',mu_G',A_G',F_G')` values are member data and derives density transport only after a lawful member exists. The later, current MEAS-ADD and relay 806 jointly provide the missing specialization for this receiver: `mu_K'` is the intrinsic `Vol_4` density. The retyping below therefore rests on current sealed bytes, not the superseded V001 shortcut.

## 1. AS1 — sharp receiver density type

### 1.1 Old opaque rows

Relay 793 used:

```text
R4Dens(K) := an opaque positive density sort in the R4 unit class,
             dual to Cof(K).

delta_K in R4Dens(K),
Pos(delta_K),
Dual(delta_K,Cof(K)),
VolNorm(delta_K,Vol_4|K),
CurrentDomain(delta_K)=Curr(K);

d_g:R4Dens(K)->R4Dens(K').
```

The predicates were sharp while the carrier was not. That mismatch made the supplied `mu_K'` invisible to the receiver.

### 1.2 Replacement type

Let `Cell_4(K)` be the already-given four-cell set and let `U_V` denote the same declared R4 volume-unit class carried by `Vol_4`. Define the **admissible receiver slice**, not a new physical field:

```text
R4Dens_sharp(K)
 := { delta_K : Cell_4(K) -> PosRay(U_V) |
        for every C in Cell_4(K),
          delta_K(C)=Vol_4(C);
        Dual(delta_K,Cof(K));
        CurrentDomain(delta_K)=Curr(K)
    }.
```

Here `PosRay(U_V)` is not an authored number system: it abbreviates “positive values in the exact unit class of `Vol_4`,” the unit-compatible positivity already required by CPKG/WHERE. The cellwise equation is the old `VolNorm` predicate expanded using MEAS-ADD, not an extra condition.

The coframe duality receiver is now explicit:

```text
box/parallelepiped C:  delta_K(C)=|det e_C|;
four-simplex C:        delta_K(C)=|det E_C|/4!.
```

The absolute value makes the density orientation-even while the signed coframe remains available to the orientation/reality equations. The child-intrinsic rule prevents carrying an arbitrary parent weight into a promoted child.

### 1.3 Positivity and normalization interface

The pointwise positivity carrier is the positive top-density ray `PosRay(U_V)` on each cell. The normalization interface has two equivalent sealed faces:

```text
cell mass:        delta_K(C)=Vol_4(C);
relative measure: mu_C(A)=Vol_4(A)/Vol_4(C), A contained in C.
```

Thus neither an independent density scale nor a counting density survives `VolNorm`. The current-domain interface remains exactly the one already sealed:

```text
CurrentDomain(delta_K)=Curr(K)=ker(B_K^T),
J_K'(S_gc)=g_*J_K(c) after the declared density normalization.
```

No extra pointwise current formula is invented. D012 and the continuum constraint arm demand this domain/naturality interface; the conserved `J_K(c)` realization supplies it. The density fixes the cell measure against which the realization is normalized and supplies no response-dependent coefficient.

### 1.4 Arrow variance and the sharp `d_g`

WHERE's sealed law is written in pullback form:

```text
mu_K=f_g^*mu_K' on the old image,
eta_dens,g(mu_K')=f_g^*mu_K'.
```

Relay 793 wrote the receiver arrow in the forward refinement direction. These are reconciled without inventing an inverse by defining `d_g` only on the canonical admissible slice:

```text
d_g(delta_K)=delta_K', where
  delta_K'(C')=Vol_4(C') for every target child C',

and the receiving check is
  Agg_g(delta_K')(C)
    := sum_(C' over C) delta_K'(C')
     = delta_K(C).
```

`Agg_g` is the finite-cell expression of the old-image pullback/restriction law. Since each `R4Dens_sharp(K)` has the unique intrinsic-volume member, the forward arrow has no free coordinate. It is determined by the target cellulation and is rejected if the eventual physical `f_g` does not realize the same child relation.

### 1.5 Residual opacity

```text
RESIDUAL_OPACITY = none inside the receiver's stated density rows.
```

The sharp type closes the exact fields 793 wrote: pointwise codomain, positivity, coframe duality, `VolNorm`, current domain, and arrow variance. It does not close `f_g`, `F_g`, `eta_resp`, a joint receiver inhabitant, or a response topology. Those are separate named objects, not residual density opacity.

## 2. AS2 — reclassification and generator derivation

### 2.1 `delta_K'` — SUPPLIED

Relay 806 `[727,2831)` displays `mu_K'` among the supplied four fields and identifies it with the forced intrinsic `Vol_4` on the same child objects as the supplied coframe. Under `R4Dens_sharp`, the conversion is byte-level in meaning and identity in type:

```text
delta_K' := mu_K'.
```

The four receiver predicates follow from the cited stock:

| predicate | discharge |
|---|---|
| `Pos(delta_K')` | intrinsic nondegenerate cell volume lies in `PosRay(U_V)` |
| `Dual(delta_K',Cof(K'))` | MEAS-ADD evaluates the top density through the supplied child coframe |
| `VolNorm(delta_K',Vol_4|K')` | definitional equality `delta_K'(C')=Vol_4(C')` |
| `CurrentDomain(delta_K')=Curr(K')` | receiver domain is the supplied `ker(B_K'^T)` current carrier; no new normalization scalar |

Classification: **SUPPLIED**, with identity conversion `mu_K' -> delta_K'`. No density member is selected because the intrinsic measure is unique.

### 2.2 `d_g` — DERIVABLE-FORCED

The inputs that pin `d_g` are the generator `g`, the supplied target cellulation/coframe, and the unique intrinsic density on each endpoint. There is exactly one arrow between the singleton admissible slices:

```text
d_g(delta_K)(C') := Vol_4(C').
```

The generator cases are:

| generator | derived density action | receiving check |
|---|---|---|
| `A0` | `d_id=id` | one unchanged cell density |
| `A1` cubical bisection | assign every child its child-intrinsic box density from its derived coframe | the 16 child masses aggregate to the parent mass |
| `A2` oriented order-simplex subdivision | assign every child `|det E_p|/4!` in the common volume-unit class | the 24 child masses aggregate to the parent mass |
| finite composite | ordered composition of the generator assignments | iterated finite additivity; the 384-cell common refinement agrees along both paths |

The counts and ratios are structural values already sealed in MEAS-RUN/JOINT; they are not a numeric evaluation of a physical observable. Positivity, orientation-evenness, duality, identity, composition, and exact `Vol_4` naturality follow at each step.

The eventual physical bridge supplies the final old-image equation `mu_K=f_g^*mu_K'`. It is a pass/fail check on the derived density arrow, not a free density input. Thus `d_g` is **DERIVABLE-FORCED**, conditional only on the separately missing `f_g` realization already named by relay 810.

```text
DELTA_K' = SUPPLIED by mu_K' under the sharp type.
D_G      = DERIVED on A0/A1/A2 and finite composites.
```

## 3. AS3 — updated path to a formable `d_K`

Relay 810 had seven assembly items. Retyping discharges the density-retyping and density-inhabitation items; `s_g` and `S_g` remain forced lane work once `f_g` is present. Exactly three missing objects remain:

1. **`f_g`, the physical bridge.** Supply a nonempty physical-path realization of each `Ref_a` generator or a sealed conversion to the actual path relation. Once present it triggers the already-pinned derivations of `s_g`, `S_g`, and the final pullback check for `d_g`.
2. **`F_g`, the refinement support map.** Supply the map from the CIS interaction-density support carrier to the `Ref_a` subdivision support carrier, with common-refinement coherence. Exhaustion reuse does not supply it.
3. **`eta_resp`, including its completed response carrier.** Seal `ResponseData`, `Eval`, `Q_resp`, the response topology, and the natural transformation; the materiality Hessian-form and evaluated-pair-set gaps remain inside this node.

After these three nodes are supplied, all six receiver components have either a supplied value or a forced construction, and a response datum `d_K in ResponseData(K)` can be typed for the D012 diagnostic. Nothing in this relay forms or evaluates that datum.

```text
D_K_PATH_REMAINDER = {physical f_g bridge, F_g support map, eta_resp/response carrier}.
```

This is the same three-object node the relay identifies as the target of the lane-opposite AXN probe 809. That artifact was not opened or consumed; the statement here is only the principal-supplied adjacency.

## 4. AS4 — freedoms, scope ledger, and flattening

### 4.1 `FREEDOMS_CONSUMED`

| datum | treatment |
|---|---|
| intrinsic `Vol_4` | **CARRIED AS UNIQUELY CLASSIFIED**; no alternate measure or scale |
| `mu_K' -> delta_K'` | **IDENTITY CONVERSION** under the sharp type; not a selected member |
| density pointwise codomain | **DERIVED FROM THE EXISTING VOLUME UNIT CLASS**; no new unit |
| A0/A1/A2 density arrows | **DERIVED** from cell-intrinsic volume and finite additivity |
| physical `f_g` | **CARRIED AS ABSENT**; no smooth map imported and no arrow member bound |
| `s_g/S_g` | **FORCED RECIPES CARRIED FROM 810**; not executed without `f_g` |
| `F_g` | **CARRIED AS ABSENT**; no cochain-support substitute |
| `eta_resp` / response topology | **CARRIED AS ABSENT**; no zero response or quotient selected |
| B1a 1887-dimensional family | **CARRIED WHOLE**; density denotation does not select a point |
| current coefficients and density scale | **NONE SELECTED** |
| downstream output or physical constant | **NOT CONSULTED** |

`SUBSTITUTED = none.`

### 4.2 Scopes-ledger disposition

```text
DS2 = DISSOLVED.
```

The declared wall served its original purpose: it prevented relay 793 from inventing a density codomain before the stock was assembled. Relay 811 now uses the later sealed intrinsic-measure denotation and 806's supplied `mu_K'` to replace the opaque name with the exact receiver slice. No record-boundary opacity remains in the density rows. The surviving gaps are independently named carrier/bridge gaps and remain visible.

### 4.3 Flattening check

`DECLINE_REGISTER_V002.md` SHA-256 `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a`; adjacent seal verified. All 37 rows were walked.

- **S08 clean:** the intrinsic density, discrete coframe, currents, and response signature are not identified with electromagnetism, Maxwell data, gravity, or a smooth public field.
- **S26 clean:** no smooth `C_ref` constituent supplies `f_g` or the density. The density is finite, cell-intrinsic, and record-side.
- **S28 clean:** the free B1a family remains unselected; the unique measure denotation is not a selector on that family.
- **DS2 cleanly retired:** the scope wall is removed only for the exact fields now pinned by sealed stock.

All other rows are untouched. `FLATTENING_CHECK = clean`.

### 4.4 Gates and verb audit

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
physics authored = none
joint member bound = none
fixed-point execution = none
end test = none
diagnostic run = none
physical quantity numerically evaluated = none
measured constant comparison = none
smooth import = none
EM identification = none
common junction cell formed = false
junction map evaluated = false
```

Self verb audit: **CLEAN.** `SUPPLIED` is limited to relay 806's existing `mu_K'` after an explicit type conversion. `DERIVED` is limited to the unique density arrow on the sharp intrinsic-volume slice; admissibility against the missing physical `f_g` remains a stated check. No global receiver member, response datum, or diagnostic result is claimed.

RETYPE = displayed (span-grounded; residual opacity: none)
DELTA_K' = SUPPLIED (identity conversion from sealed `mu_K'`)
D_G = DERIVABLE-FORCED / DERIVED on A0, A1, A2, and finite composites
D_K_PATH = 3 items remaining (`f_g` physical bridge; `F_g`; `eta_resp`/completed response carrier)
DS2 = dissolved
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
