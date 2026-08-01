# Stage 8 PRPS Smooth-Phrasing Import Adjudication v001

Date: 2026-08-01
Lane: CODEX 1
Register head at issue: Paste 266

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
coupling_evaluation_authorized = false
production_authorized = false
```

## Scope and fences

This artifact asks whether `PRIMITIVE_RELATIVE_PHASE_STABILIZER_V002.md`'s
smooth localization phrasing is the only available route to a comparison
connection, or whether the record side already states the relevant condition in
discrete form.

No coupling, scale, root, eigenvalue, beta function, `E_R`, `T_R`, `k_R`,
`kappa_record`, `kappa_Thomson`, or `alpha` is computed or compared to any
measured constant. The Misner-Sharp / Brown-York fork is not resolved.
`a32_holdout/custodian_private/` was not opened. No git command was run.

The adopted smooth spacetime `(M,g)` is not used here to supply a domain. If
used, it would be an adopted/imported smooth-domain act, not a record-side
derivation.

## Lead verdict

A **discrete Gate-4 conditional exists at theorem-core level**, and Gate 4
satisfies it. It delivers a record-side discrete comparison connection:
unit-weight covariant incidence modulo vertex gauge, with loop holonomy as the
surviving physical freedom.

It does **not** deliver the same object as PRPS's smooth conclusion
`D = d - i a`, `a -> a + d theta`. The discrete conclusion is a finite
edge/vertex incidence-gauge object. The PRPS conclusion is a smooth patch
connection with an exterior derivative on a smooth domain. The bridge between
them is precisely the unbuilt smooth/discrete localization bridge.

```text
gate4_discrete_connection_conditional_found = true

standalone_PRPS_style_discrete_conditional_found = false | TYPE-S |
roots: cleanroom root, alpha-program-archive cleanroom_output |
excl: a32_holdout/custodian_private/, git, value-bearing computations |
query: "discrete conditional", "discrete connection", "unit-weight covariant
       incidence", "modulo gauge", "vertex rephasing", "connection required",
       "covariant comparison", "Gate 4", "PRPS"

gate4_satisfies_discrete_connection_conditional = true |
source: cleanroom_output/30_GATE4_DIFFERENTIAL_UNIQUENESS_SPEC_V001.md:21-60
        and cleanroom_output/32_GATE4_DIFFERENTIAL_UNIQUENESS_RESULT_V001.md:9-31

discrete_connection_equals_PRPS_smooth_connection = false | TYPE-R |
test: compare the typed conclusion objects. Gate 4 concludes a finite
      C0/C1 edge-vertex incidence differential modulo vertex gauge; PRPS
      concludes a smooth patch connection using exterior derivative `d`,
      local one-form `a`, and smooth transition functions.

PRPS_smooth_phrasing_as_record_side_connection_requirement =
  IMPORTED_OR_ADOPTED_SMOOTH_UPGRADE unless a separate record-derived
  smooth-domain theorem is supplied.
```

This is the "weaker conclusion" case. Four Target-2 failures were chasing the
smooth upgrade. They do not erase the already-derived discrete record-side
connection.

## 1. Does the corpus contain a discrete conditional already?

Yes, but not as a standalone PRPS-analogue sentence. The conditional appears as
Gate 4's theorem-core setup and result.

`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:276-304` defines the record
complex category: an object of `BareRec_2` is `(K,r,L,U)`, where `K` is a finite
oriented regular CW complex, `L` assigns one-dimensional Hermitian vertex
fibers, and `U` is the discrete unitary connection. Each oriented edge carries
unitary transport `U_e:L_s->L_t`; no flatness around filled two-cells is
imposed, because nontrivial face holonomy must remain admissible.

The same spec states Gate 4 at `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:1692-1712`.
Starting from `D_(a,b)` and the hostile counterfamilies, only the listed
orientation, public-closure, colimit/cocone, local boundary, differential
naturality, character covariance, orientation reversal, and one-record
normalization constraints may be applied. Pass requires exactly one normalized
differential equivalence class and one public-collapse covector ray.

The executable specification is even more explicit.
`cleanroom_output/30_GATE4_DIFFERENTIAL_UNIQUENESS_SPEC_V001.md:21-33` lists
the sealed constraints:

```text
C1 naturality/universality;
C2 interior closure / chain property;
C3 one-record normalization;
C4 per-vertex U(1) rephasing, form congruence, orientation bookkeeping.
```

The same artifact predicts the conditional conclusion at
`cleanroom_output/30_GATE4_DIFFERENTIAL_UNIQUENESS_SPEC_V001.md:35-60`: closure
kills the continuum, normalization plus rephasing leaves unit-modulus
transport with residual phases only on loops, no per-edge magnitude deformation
survives, forms do not reopen the family, and therefore there is exactly one
normalized differential equivalence class: unit-weight covariant incidence
modulo gauge, with holonomy the sole surviving physical freedom.

`cleanroom_output/32_GATE4_DIFFERENTIAL_UNIQUENESS_RESULT_V001.md:9-31`
confirms all four predictions. In particular, lines 22-25 state that
normalization forces `|a|=1`, vertex rephasing removes tree phases, loop
holonomy survives, and the unique class is unit-weight covariant incidence
modulo gauge, a compact gauge field.

Therefore:

```text
discrete_theorem_core_conditional_exists = true
```

But the corpus did not package this as the exact sentence "if local
edge-fiber comparisons are redundant under vertex gauge and transported along
incidence edges, then a discrete `U(1)` connection is required." That
standalone sentence is a reconstruction of Gate 4's theorem-core, not an
already sealed PRPS-style formulation.

## 2. Discrete analogues stated from derived record structure

The discrete analogue can be stated without importing `(M,g)` or a smooth patch
space. It uses only the Gate-4 record complex and its theorem-core constraints.

Premises, stated as premises rather than conclusions:

1. **Discrete locality.** The comparison carrier is local to a finite oriented
   record complex: vertex fibers `L_v`, oriented edge carriers, and maps between
   source and target vertex components. Source: `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:281-304`
   and `cleanroom_output/30_GATE4_DIFFERENTIAL_UNIQUENESS_SPEC_V001.md:12-19`.

2. **Discrete redundancy.** Choices of local vertex sections are redundant up
   to per-vertex `U(1)` rephasing, with matching form congruence and
   orientation bookkeeping. Source: `cleanroom_output/30_GATE4_DIFFERENTIAL_UNIQUENESS_SPEC_V001.md:31-33`.

3. **Discrete transport/closure.** Edge comparison data must compose so the
   boundary of a composite path is supported only on endpoints; no interior
   residue may survive. Source: `cleanroom_output/30_GATE4_DIFFERENTIAL_UNIQUENESS_SPEC_V001.md:26-29`
   and result `cleanroom_output/32_GATE4_DIFFERENTIAL_UNIQUENESS_RESULT_V001.md:17-21`.

4. **Discrete normalization.** One-record normalization fixes the magnitude
   class after closure, while vertex rephasing removes tree phases and leaves
   loop holonomy invariant. Source: `cleanroom_output/30_GATE4_DIFFERENTIAL_UNIQUENESS_SPEC_V001.md:30`
   and `:43-49`, confirmed by `cleanroom_output/32_GATE4_DIFFERENTIAL_UNIQUENESS_RESULT_V001.md:22-25`.

From these premises, Gate 4 derives the discrete conclusion:

```text
DISCRETE_CONDITIONAL:
If finite record-complex comparison data are local to vertex/edge incidence
carriers, physically redundant under vertex U(1) rephasing, transported by
edge/path composition with no interior boundary residue, natural over
universal-edge isomorphisms, and one-record normalized, then the only surviving
comparison differential is unit-weight covariant incidence modulo gauge, with
loop holonomy as the physical residual.

status = DERIVED_WITHIN_GATE4_ENUMERATED_FAMILY
```

This conditional does not manufacture a new theorem. It is a restatement of
Gate 4's already verified theorem-core, with the conclusion kept distinct from
the premises.

## 3. Does the discrete conditional deliver the same conclusion as PRPS?

No.

PRPS's active conditional is smooth. `PRIMITIVE_RELATIVE_PHASE_STABILIZER_V002.md:93-115`
states that the pointwise stabilizer does not imply independent local
variation. It requires a later target-independent theorem establishing:

```text
the endpoint comparison frame is local;
independent smooth relative-frame changes are physically redundant;
comparison data must be transported between overlapping patches;
```

Only then is a connection with

```text
D = d - i a,
a -> a + d theta
```

required. The same block says those premises are not established and that the
document neither introduces `a` as a physical field nor identifies it with
electromagnetism.

`LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md:16-43` supplies a smooth local-bundle
calculus: patches `U_i`, normalized lifts, overlap transition functions, and a
principal `U(1)` comparison bundle. Lines 45-79 then perform the familiar
smooth patching calculation: ordinary derivatives of local lifts do not patch,
while `D_i=d-i a_i` patches covariantly exactly when `a_j=a_i+d theta_ij`.

That smooth calculus is not current authority for deriving the physical
charged connection. `FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md:47-60`
states that the smooth principal `U(1)_rel` bundle and auxiliary compact
connection are adopted Level-1 field content, not derived from common projective
phase, passive basis rephasing, electromagnetism, or measured alpha. Its status
block at `:159-174` records `physical_public_EM_connection_derived = false`.

The mismatch is structural:

| Discrete Gate 4 | Smooth PRPS |
|---|---|
| finite oriented regular CW complex through degree two | smooth local patches / overlaps |
| vertex fibers and edge carriers | local lifts over open patches |
| per-vertex `U(1)` rephasing | smooth relative-frame functions |
| incidence differential on `C_1 -> C_0` | exterior derivative `d` on a smooth domain |
| unit-weight covariant incidence modulo gauge | one-form connection `a_i` with `a_j=a_i+d theta_ij` |
| loop/face holonomy in the finite record complex | curvature/connection on smooth patch bundle |

The prior bridge artifacts state the same obstruction. `STAGE8_PRPS_GATE4_LOCALIZATION_BRIDGE_ATTEMPT_V001.md:22-44`
records that the standard smooth-to-discrete connection map is imported
geometry and does not transfer without a canonical graph/cover/path realization
theorem. Lines 170-196 list the missing inputs and say the reverse
discrete-to-smooth bridge is not canonical. `STAGE8_CANONICAL_PATCH_COVER_TO_INCIDENCE_GRAPH_FUNCTOR_ATTEMPT_V001.md:281-299`
records the formal match between Cech lift changes and Gate-4 vertex gauge but
marks the actual PRPS-to-Gate4 discharge as unbuilt.

Therefore:

```text
same_physical_object_established = false | TYPE-U |
would-build: a canonical smooth/discrete bridge proving that the PRPS
endpoint-comparison patch connection and the Gate-4 finite incidence connection
are the same object up to the declared equivalences.

claim_that_they_are_already_the_same = false | TYPE-R |
test: compare source/codomain variables and transformation laws. The smooth
object consumes patches, exterior derivative, local one-forms, and smooth
transition functions; the discrete object consumes vertices, edges, incidence
operators, vertex rephasing, and path closure.
```

## 4. What depends on the smooth phrasing?

The following standings change or sharpen:

1. **Gate 4 does not depend on PRPS smooth patches.** The record-side discrete
   connection is already derived within the Gate-4 enumerated family.

2. **The four Target-2 failures are failures of smooth upgrade, not failures of
   the discrete record connection.** They show that PRPS patches, covers, good
   nerves, and canonical graph/cover/path realization are not supplied. They do
   not undo the Gate-4 discrete theorem.

3. **The claim "no connection has been derived" is too broad.** Correct form:
   a discrete finite record-incidence connection has been derived; the smooth
   PRPS/physical public connection has not.

4. **`physical_public_EM_connection_derived` remains false.** The discrete
   connection is not identified with electromagnetism, a smooth public field, a
   Maxwell connection, or a response object.

5. **LPRB remains provenance/adopted smooth machinery, not a derivation from
   record structure.** Its smooth patch calculation is available as a standard
   smooth formulation once its premises are granted, but it is not supplied by
   Gate 4 alone.

6. **Downstream response, CTP, Maxwell stiffness, and alpha-path obligations do
   not move.** They require the smooth/external response layer or an explicit
   theorem relating the discrete record connection to that layer. No such
   theorem is supplied here.

7. **Future Target-2 work should be scoped as smooth-upgrade work.** It should
   not be described as the route to derive any connection at all; it is the
   route to derive or adopt the smooth PRPS/physical-public connection from the
   already discrete record-side gauge structure.

## 5. Is the smooth demand genuinely required?

Split answer.

For the internal record-side comparison connection, the smooth demand is **not**
required. Gate 4 already gives the discrete connection statement in its own
finite incidence language.

For PRPS's printed conclusion `D=d-i a`, `a -> a+d theta`, and for any claim
that the record-side structure has become a smooth physical/public
electromagnetic connection, the smooth demand **is** required. The program then
has exactly the two branches already identified:

```text
1. build a record-derived smooth-domain / patch / overlap / bridge theorem; or
2. adopt/import the smooth domain and smooth bundle/connection explicitly.
```

There is no third route in this artifact that turns Gate-4 finite edge
incidence into a smooth exterior-derivative connection without additional
structure.

## Roots, exclusions, and search record

Roots entered:

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha-program-archive/cleanroom_output
```

Exclusions:

```text
a32_holdout/custodian_private/
git commands
value-bearing computations
measured constants
adopted (M,g) as a supplied domain
```

Searches included:

```text
PRPS; Primitive Relative Phase; D=d; a ->; a+dtheta; smooth relative-frame;
endpoint comparison; overlapping patches; local patch; U_i; local projective;
Gate 4; gate4; differential; normalized differential; unit-weight covariant
incidence; modulo gauge; vertex rephasing; edge phase; loop holonomy; discrete
unitary connection; connection required; covariant comparison; smooth import;
smooth principal; auxiliary compact connection.
```

## Final status block

```text
DISCRETE_GATE4_CONNECTION_CONDITIONAL_EXISTS = true
GATE4_SATISFIES_DISCRETE_CONNECTION_CONDITIONAL = true

STANDALONE_PRPS_STYLE_DISCRETE_CONDITIONAL_FOUND = false | TYPE-S

DISCRETE_CONNECTION_DELIVERS_PRPS_SMOOTH_CONNECTION = false | TYPE-R
SMOOTH_DISCRETE_IDENTITY_BRIDGE_BUILT = false | TYPE-U

INTERNAL_RECORD_SIDE_CONNECTION_DERIVED = true | DISCRETE_GATE4_SCOPE
SMOOTH_PRPS_CONNECTION_DERIVED_FROM_RECORD_STRUCTURE = false | TYPE-U
PHYSICAL_PUBLIC_EM_CONNECTION_DERIVED = false | TYPE-U

TARGET_2_RESCOPING_RECOMMENDATION =
  smooth-upgrade / smooth-discrete-bridge road, not route to derive the
  internal discrete record connection.

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
