# CODEX 2 — Q-106 Correlator-to-retarded-Hessian map

`alpha_computed = false; proof_authorized = false; kappa_record_computed = false.`

## Determination

The relay-158 specification fixes the **formal relation** independently of choosing a physical quotient,
but it does not fix the complete physical map.  The physical map remains downstream of the CTP package.

## Three components

1. **Relation.** The conditional Schur complement and Legendre relation are stated at
`STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:730-782`:
`D²Γ₁PI = ΓAA − ΓAG ΓGG⁻¹ ΓGA` and `H_C[G] := i hbar G⁻¹`.  Keldysh transformation and retarded
extraction are fixed formally at `:804-815`: `H_R[G] = (T_CTPᵀ H_C[G] T_CTP)_(delta,c)`.  This is a
specification, not a derived physical result (`:1077-1094`).
2. **Domain.** The formal domain is an invertible, bilocal physical correlator `G` on the stationary
`R=0` source surface, with differentiable `Log_0`, contacts, boundaries, and endpoint domains inherited
from the CTP package.  The exact physical domain is not fixed because P1–P8 and the package are TYPE-U
(`:782`, `:1094`).
3. **Physical quotient.** The map requires the completed gauge-fixed physical quotient, branch metric/reality,
DeWitt/contact conventions, and Ward-compatible endpoints.  Those are explicitly inherited package data
(`:815-817`) and are not independently sealed.

## Independence and dependency

The algebraic relation can be fixed without choosing a quotient: its Schur/Legendre identities and the
Keldysh block operation are quotient-parametric.  The **physical** relation cannot be certified separately,
because support, adjointness, contacts, boundaries, and Ward identities require the quotient.  Thus:

`formal_relation_fixed = true | TYPE-C | conditional specification only.`
`physical_map_derived = false | TYPE-U | would-build: CTP_PHYS_INPUT_PACKAGE plus P1-P8 and T1-T6.`

## Exact requirement from the quotient/measure bundle

Codex 1's bundle must provide one named, gauge-fixed physical space on which: (a) `G` is a bilocal
correlator with an invertible physical inverse; (b) `Log_0` and contour measure are defined; (c) branch
metric, reality involution, compound-index/DeWitt conventions are fixed; (d) contacts, boundary data, and
Ward-compatible endpoint domains are specified.  Only then can the retarded support and adjointness tests
at `:817-821` be run without selecting a quotient to make the map work.

## Q-100 classification

The map is not an `I_prim` object.  It consumes the completed physical CTP package and correlator, which
are outputs/inputs downstream of `Obj_0`; Q-100 therefore places it in `S_sector`, not among constructor
primitives.  The earlier “used as primitive” label was a miscategorizaton:

`raw_map_I_prim = false | TYPE-R | test: Q-100 upstream-of-Obj_0 criterion; map consumes Obj_0/CTP outputs.`
`raw_map_S_sector = true | TYPE-C | classification follows its consumer direction.`

## Q-92 action

No sealing occurred.  Although the formal relation exists as a specification, its physical prerequisites,
dedicated verdict owner, and failed adversarial countermodel do not.  The required countermodel is a map
defined on two inequivalent quotients that produces different physical retarded blocks; it has not been
run.

`raw_map_sealable_today = false | TYPE-C | constraint: physical quotient/package absent; owner and countermodel absent.`
`T1-T6_executed = false | TYPE-U | would-execute: after package completion.`
`NO_VERDICT` is the physical verdict because applicability inputs are unbuilt.

No git, commit, push, gate, or deploy action was performed.
