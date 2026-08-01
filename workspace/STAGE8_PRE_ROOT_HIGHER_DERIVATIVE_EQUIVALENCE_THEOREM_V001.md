# CODEX 2 — Pre-root higher-derivative equivalence theorem V001

Date: 2026-08-01. Road role: UNBLOCKS STEP 3 conditionally.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
coupling_evaluation_authorized = false
production_authorized = false
```

## Lead result

**The tower bounds only at each fixed derivative order. It does not acquire a finite all-orders basis.**

The standard equation-of-motion/field-redefinition redundancy transfers to this record-incidence setting
only for local, invertible, boundary-preserving redefinitions that act trivially on the sealed incidence
normalization, preserve the compact `U(1)` holonomy class, and preserve the physical quotient, measure,
contacts, and Ward domains. Under those hypotheses, EOM-exact and total-boundary operators are response-
equivalent and removable before any root exists. At each fixed order the quotient basis is finite, assuming
finite field content and the usual local finite-jet hypothesis. Across all derivative orders it remains
infinite. The corpus supplies no cutoff, convergence theorem, or UV completion that closes the union.

Therefore this theorem gives a genuine pre-root equivalence relation but **does not discharge §5.3's
all-orders exhaustiveness requirement**.

## Scope and authority

Roots entered:

1. current cleanroom root;
2. its parent gravity-program root;
3. `/Users/bgm/MB Work/alpha-program-archive/cleanroom_output/`;
4. `/Users/bgm/MB Work/alpha_supervision/`.

Excluded: `.git`, dependency/vendor directories, review packets as primary authority, and all of
`a32_holdout/`; `a32_holdout/custodian_private/` was neither entered nor listed.

Queries were case-insensitive and word-boundaried: `higher-derivative`, `field redefinition`, `equations of
motion`, `response-equivalent`, `action-form`, `unit-weight`, `unit modulus`, `counting metric`, `holonomy`,
`Ward`, `boundary`, and `contact`.

Sealed corpus inputs used:

* §5.3 requires the five-channel pre-root mutation audit and defines the pass/fail relation at
  `STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md:530-581`.
* The required action-form theorem must cover gauge-covariant higher-derivative source terms and must not
  narrow after a root at `STAGE8_ACTION_FORM_CLOSURE_THEOREM_SPEC_AND_BUILD_STOP_V001.md:190-236`.
* The concrete control pair `S_0,S_1`, and its response-changing Pauli vertex, are stated at
  `STAGE8_ACTION_FORM_UNDERDETERMINATION_INVENTORY_V001.md:35-105`.
* The higher-derivative class has no sealed member, order, coefficient, or suppression statement at
  `STAGE8_DELTAPHI_PI_PROTECTION_DETERMINATION_V001.md:266-310`.
* Gate 4's surviving incidence content is one constant on a connected complex, then unit modulus, at
  `STAGE8_PARENT_NORMALIZATION_FROM_RECORD_STRUCTURE_DETERMINATION_EINSTEIN_V001.md:156-159,325-326`.

The field-redefinition lemma below is a **standard EFT import**. Its transfer to this corpus is proved only
conditionally; it is not represented as a sealed native theorem.

## 1. Response-equivalence relation

Let `Phi` denote the complete collection of continuum source/field variables and record variables on the
fixed admitted carrier, and let `S[Phi]` be a complete microscopic source-record-field action with fixed
physical quotient, measure, boundary/contact prescription, and Ward domain.

Two action mutations `Delta S_1` and `Delta S_2` are pre-root response-equivalent, written
`Delta S_1 ~_R Delta S_2`, iff there exists a local invertible change of variables

```text
Phi^i -> Phi'^i = Phi^i + F^i[Phi]
```

such that:

1. `F` is target-independent and defined before any response/root evaluation;
2. it preserves the physical quotient, causal/boundary domains, measure class, contacts, and Ward identities;
3. it is the identity on the discrete incidence carrier except for already-derived gauge equivalences;
4. it preserves the compact `U(1)` holonomy/conjugacy class and introduces no new incidence magnitude;
5. after transforming sources and observables covariantly, the two actions generate the same physical
   retarded-response functional, modulo contact terms already identified by the fixed prescription.

This relation refines the corpus's live physical equivalences—gauge, public isometry, charge-conjugate
orientation, and Boundary-Resolved equivalence—without identifying any flag with the object that discharges
it (`STAGE8_ACTION_FORM_CLOSURE_THEOREM_SPEC_AND_BUILD_STOP_V001.md:190-216`).

## 2. Conditional redundancy theorem

### Theorem

Assume H1–H8 below. If an admitted local operator has the form

```text
O_red = F^i[Phi] E_i[Phi] + nabla_mu B^mu[Phi],
E_i[Phi] := delta S_0 / delta Phi^i,
```

then adding `epsilon integral O_red` to `S_0` is removable through the relevant EFT order by the local
field redefinition `Phi^i -> Phi^i - epsilon F^i[Phi]`. It is therefore `~_R`-equivalent to the identity
mutation at that order.

### Proof

The first variation gives, algebraically and before any root exists,

```text
S_0[Phi - epsilon F]
 = S_0[Phi]
   - epsilon integral F^i (delta S_0/delta Phi^i)
   + epsilon integral_boundary B_F
   + O(epsilon^2).
```

The EOM-proportional bulk term cancels `epsilon integral F^i E_i`. H3 makes the boundary contribution
either zero or an already-fixed contact/boundary functional. H4–H7 ensure the change of variables does not
change the physical quotient, admitted record effects, Ward domain, incidence normalization, or holonomy.
H8 ensures the Jacobian is either trivial or absorbed into local operators at the next order without adding
an unregistered response mutation. Iterating order-by-order removes every operator in the ideal generated by
the leading EOM plus fixed total-boundary terms. QED, conditional on H1–H8.

### Hypotheses

H1. A complete local microscopic action `S_0` exists.

H2. The mutation admits a local finite-jet derivative expansion.

H3. Boundary/contact conditions make the integration-by-parts term fixed and Ward-compatible.

H4. The field redefinition is invertible on the physical domain and respects the causal prescription.

H5. Sources and response observables transform covariantly, so the comparison is between physical responses,
not bare off-shell kernels.

H6. The gauge-fixed quotient and measure are invariant or their Jacobian contribution is included.

H7. On record incidence, the transformation preserves the derived counting metric, the one-constant
connected-complex condition, unit modulus, and the compact-holonomy class.

H8. A regulator exists that respects H3–H7 and organizes Jacobian terms in the same derivative expansion.

## 3. Adversarial attack on the hypotheses

H1 fails as a discharged corpus premise: the complete microscopic action is still unbuilt. The `S_0/S_1`
pair proves that action-form alternatives exist, not that `S_0` is the unique complete parent.

H2 is unsealed: the corpus names higher-derivative terms but supplies no generating schema, coefficient
class, or locality theorem.

H3–H6 are unbuilt at the complete level: the physical quotient, measure, contacts, endpoint domains, and
response map are precisely parts of the outstanding CTP package.

H7 is the strongest native support. It blocks a field redefinition that rescales incidence weights or
changes holonomy merely to remove an operator. Such a mutation is not redundant under this theorem. This
prevents the EFT import from reintroducing the magnitude already eliminated by Gate 4.

H8 is absent: no symmetry-preserving all-orders regulator/Jacobian theorem is sealed.

The Pauli control `S_1-S_0` is not EOM-exact on the evidence cited: it changes the source vertex and exact
response type (`STAGE8_ACTION_FORM_UNDERDETERMINATION_INVENTORY_V001.md:35-105`). The theorem therefore does
not falsely erase the known inequivalent control.

## 4. Size of the quotient basis

At a fixed derivative order `N`, finite field content, locality, covariance, integration by parts, algebraic
identities, and quotienting by the EOM ideal yield a finite operator basis. This is a conditional standard-EFT
result.

Across `N = 0,1,2,...`, the union remains infinite unless one additionally derives at least one of:

1. a finite cutoff/order relevant to the exact response;
2. an all-orders convergence/resummation theorem with finitely many response invariants;
3. a UV completion or microscopic generator that fixes the full tower;
4. a stronger native incidence theorem reducing all higher orders to a finite algebra.

None is presently sealed. A finite basis **at each order** is not an all-orders bound and cannot, by itself,
make §5.3 exhaustive.

## 5. Typed verdicts

```text
pre_root_EOM_equivalence_relation_specified = true
conditional_EOM_redundancy_theorem_proved = true
theorem_native_to_record_corpus = false | TYPE-S |
  roots: four roots in Scope | query: field redefinition, EOM redundancy |
  reason: the lemma is a declared standard-EFT import

record_incidence_transfer_applicability_derived = false | TYPE-U |
  would-build: H1-H8 for the completed microscopic action and response

finite_basis_at_each_fixed_derivative_order = true | CONDITIONAL_ON_H1-H8_AND_FINITE_FIELD_CONTENT

finite_all_orders_response_changing_basis = false | TYPE-U |
  would-build: cutoff, convergence/resummation, UV completion, or stronger native finite-algebra theorem

higher_derivative_response_changing_bound_discharged = false | TYPE-U |
  would-build: the all-orders result immediately above

Section_5_3_all_orders_quantification_unblocked = false | TYPE-C |
  constraint: only order-by-order redundancy is available; no pre-root truncation is sealed

known_Pauli_control_removed_by_this_theorem = false | TYPE-R |
  test: its vertex/response change is not shown EOM-exact and survives the admissibility inventory
```

## Conclusion

The standard redundancy mechanism transfers conditionally and safely: it never changes the sealed incidence
magnitude or holonomy, and it removes only EOM-exact/boundary-exact operators. It is useful census structure,
but it leaves infinitely many derivative orders. The exact additional result needed is a **pre-root
truncation or all-orders completion theorem**. Until that exists, the higher-derivative census is bounded
order-by-order but not globally, and §5.3 remains blocked on this class.

No root, coupling, scale, eigenvalue, beta function, or measured comparison was computed. No fork was chosen.
No git, commit, push, gate, or deploy action was performed.
