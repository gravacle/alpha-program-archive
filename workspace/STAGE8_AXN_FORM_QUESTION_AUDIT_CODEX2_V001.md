# STAGE 8 / [PLAN:AXN-CONSTRUCT-F] — THE FORM QUESTION AUDITED

Lane: CODEX 2. Relay 825. Date: 2026-08-09.

All headline items are **CLAIMED**. This is a typing audit only. No action was
derived, varied, selected, patched, or substituted; no flag was flipped.

## 0. Custody, scope, and governing pins

- Inbox `relay_inbox/RELAY_PASTE_825_FORM_QUESTION_AUDIT_CODEX2_V001.md`
  = `7fb486439c0e167e2e744fd8a52d74afe31718c3de3b1f8a52f2bf6716c0ff76`;
  adjacent seal verified before reading; pickup acknowledgement written first.
- `PROGRAM_STATE_BRIEF_V005.md`
  = `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c`;
  verified and read before task work.
- `QUESTIONS_SETTLED_REGISTER_V001.md` adjacent seal verified. Q-727 and Q-729
  were located before adjudicating the gap.
- `DECLINE_REGISTER_V002.md`
  = `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a`;
  adjacent seal verified.
- Packet sources below were read only from
  `review_packets/STAGE7_QSPEC_CANDIDATE_V001/` and verified through the packet
  manifest or their group sidecars. MF was verified through
  `R3_4_CAUSAL_CELL_MOVING_FRONT_V001.seal.sha256`.

Gates held throughout:

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member_binding = false
fixed_point_execution = false
end_test = false
numeric_evaluation_of_physical_quantities = false
comparison_to_measured_constants = false
smooth_import = false
electromagnetic_identification = false
```

## 1. AS1 — the demand, verbatim, and the checkable predicate

### 1.1 MF's conditional in full

Source: `R3_4_CAUSAL_CELL_MOVING_FRONT_RESULT_V001.md`, SHA-256
`ed4572ebfece9da2d57a2baede144f996aee1b196c26182c0d9e61f879bf9ef9`,
group-sidecar verified. Bytes `[2497,2818)`, span SHA-256
`3411fe299c99aba43ddc239ecbaf968b79254b4b0e450ce77a8d51bc40c6019b`:

> The current result proves:
>
> ```text
> if the complete parent realizes its already proposed primitive writes as
> one-use finite causal-cell events, durable public outgoing sectors follow
> without any spectral-density choice.
> ```
>
> It does not yet prove that the complete source/gauge/gravity/environment
> action has that form.

MF's own promotion gate is equally exact. Its specification,
`R3_4_CAUSAL_CELL_MOVING_FRONT_SPEC_V001.md`, SHA-256
`6f2eabe26294e9d576f4cb0256045aa8c44a22d83331803a1a0d2068b0d881a0`,
bytes `[2165,2668)`, span SHA-256
`0a086a38d920ce9cd6785522aab31a62de524dc490431cad69f1487226c92abc`,
requires the live principles to bind:

```text
each primitive interaction to one finite causal cell;
distinct future cells to distinct record factors;
and physical exhaustion to future cell addition rather than repeated action
on a completed cell.
```

If those bindings remain only part of the causal-direct-limit hypothesis, MF
requires the result to remain conditional.

### 1.2 T5's derive-and-vary demand

The governing typed source is `STAGE8_AXN0_ACTION_AS_ROLE_DARIO_V001.md`,
SHA-256
`5f802c10f34392573ecb600a0a9b3ff3b04c93e8749e25bbb7dd124c7f1ad36b`,
adjacent seal verified. Its complete T5 block is bytes `[8522,9217)`, span
SHA-256
`688292edaaaa3130cd4bb796c32d85371ca11d9f1ad40da9486afff320b19fc8`:

> “do not patch or choose `x`; **derive and vary** the complete compact
> nonlocal coupled action on a physically provenanced carrier”

The paired demand is to evaluate the full compact proper-time action and
public superdeterminant to select or reject a stable `x`. T5 types this as an
**OBJECT** demand: variation takes the action as its argument, and the
selection role is downstream of that object. The explicit anti-substitution
clause is part of the demand, not an interpretation added here.

### 1.3 The exact flag and all siblings

MF bytes `[2829,3481)`, span SHA-256
`53c8d50cbb2e9d01a129d5ace8df16770f11fa291d41e572924c71313facc179`,
read verbatim:

```text
pulse_profile_independence_derived = true
distinct_cell_generator_commutation_derived = true
causal_linear_extension_independence_derived = true
earlier_public_record_nondemolition_derived = true
central_pointer_sector_derived_for_moving_front = true
conditional_outgoing_public_dynamics_strongly_continuous = true
moving_front_bound_by_live_complete_parent = false
full_parent_state_covariance_derived = false
physical_durability_derived_unconditionally = false
complete_parent_action_derived = false
physical_response_spectral_measure_derived = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```

### 1.4 Closed, checkable form predicate

Let `A_complete` denote the **derived and varied** complete compact nonlocal
source/gauge/gravity/environment action on its physically provenanced
carrier, and let `Gen(A_complete)` be the generator/update law obtained from
that variation. The narrow antecedent MF needs is:

```text
FORM_MF(A_complete) :=
  A_complete exists as the complete coupled action object required by T5;
  AND for every primitive record-forming incidence c,
      Gen(A_complete) assigns one Lorentz-covariant finite causal cell Omega_c
      and one interaction density L_c with support(L_c) subset Omega_c;
  AND c is an event: after the future boundary crosses its closure face,
      its primitive term is absent from the active generator;
  AND a physical exhaustion adds future incidences on distinct new record
      factors and never reapplies a completed incidence to its old factor;
  AND the action-induced primitive restriction is the sealed moving-front
      write (or a proved intertwining-equivalent form), not a separately
      selected pulse, switch-off, tail, or spectral law;
  AND every descendant term generated by A_complete is accounted for and
      does not reactivate an old primitive or destroy the completed public
      outgoing sector.
```

The last conjunct is not an embellishment. CIS expressly permits effective
source, record, gauge, gravitational, and environmental descendants only
when they come from the same complete parent and are tested on the outgoing
sector. Thus checking only a primitive summand is not checking the complete
action's form.

MF has already proved what follows **if** `FORM_MF(A_complete)` holds at its
declared pure-charge/moving-front scope. The audit must type whether the
antecedent's argument exists; it must not re-prove the conditional or weaken
its argument from `A_complete` to a record-sector limit.

## 2. AS2 — supply inventory

| item | sealed source and exact span | what stands | exact limit against `FORM_MF` |
|---|---|---|---|
| One-use law | packet `CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md`, file SHA `b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30`, `[527,1397)`, span SHA `bfb109f4668b51991036b9a515d428223459ab30c757abdacb1fe6f95311e3ca` | One cell and support-contained density per primitive incidence; event rather than permanent term; future additions use new record factors; completed primitive reuse barred; shared source expressly allowed. | It is an adopted Level-1 support law frozen before construction/evaluation of its parent. It does not prove that the eventual complete action realizes it. |
| Complete-parent descendant rule | same CIS, `[1430,1933)`, span SHA `eba8d6b443015e89b3c0dc345500193279fccbf40175f189b546ce0ec67ccfdb` | Descendants must come from the sealed parent, inherit causal/gauge covariance, and be tested on the public outgoing sector. | This prevents a primitive-only check from closing the full-action predicate. |
| Finite causal-cell carrier | packet `R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md`, file SHA `40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9`, `[4287,4905)`, span SHA `a4953cb66daa6dacf588351447c24defea88068681cbd586e7dd8452a1207f6a` | `K_Sigma`, one global source CAR algebra, and distinguishable finite record factors `R(K)=tensor_(c in K)R_c`; each cell carries its fixed record-incidence operator, extended by identity on all other factors. | This is the carrier and local incidence data, not the complete varied action. |
| Intrinsic cell envelope | same parent spec, `[4905,5711)`, span SHA `6b25a7aa8d2af4f4956604e8b996549c6328f347ca44c0ae17828732508f822d` | A fixed compact causal envelope `v_c(t)`, zero outside its interval; pulse reshaping and independently normalized tails barred. | It proposes the finite cell realization; it does not exhaust all complete-action terms. |
| Proposed primitive writes | same parent spec, `[5711,6867)`, span SHA `eddc2e9ab66e1036e7defdc514b61214e0adef3b48fced3c3aa7a67b6df5f2c3` | On a finite causal complex, `h_K(t)=h_0[g,a]+sum_(c in K) v_c(t) M_c(t) tensor S_n tensor iota_c(c_c)` and `H_K(t)=dGamma_R(h_K(t))`; one local first-order parent, no separately chosen post-write Hamiltonian. | The source labels this a forward-sealed construction specification. It is a concrete proposed operator form, not T5's derived-and-varied complete compact nonlocal action. |
| Finite result | packet `R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md`, file SHA `345d447eaf6d730caa6fa655b92a7b0cd93a68b5f86e0c8929cf969f40aeb7cb`, `[157,774)`, span SHA `e24c7c94ec458e0ea0bf8c7fcff5b63a0331df8c1259783f639ebce9240346d1` | A finite causal source-record parent is derived with intrinsic envelope, shared source, distinct record factors, generated descendants, propagator, compact-support Møller maps, and exact completed-record persistence. | The verdict is explicitly finite and withholds the full source-inclusive/infinite-future completion. It does not supply the T5 action object. |
| Exact record completion | packet `R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md`, file SHA `10909b5c21e73ecf655462339a27bd645b8d35e3ad11fb6f8cb204c601992995`, `[653,1861)`, span SHA `50e45c5a2ea94271fadbf44e5473161451420cd45f23e2adad7cf2953cc20591` | Exact compatibility on `R_N=tensor_(j=1)^N M_3(C)`, one quasi-local state, GNS representation, identity dynamics, and a coherent dressed incoming net. | Its scope boundary `[3983,4443)`, span SHA `3d4e70197164f2a6184df85bbf5d149de1f81ad7d44b370e4a609ec4a87fa545`, expressly withholds a projective limit of full source-record states and an infinite-future source Møller unitary. The completed-record algebra is not `A_complete`. |
| Sealed completion principle | `CAUSAL_DIRECT_LIMIT_RECORD_PRINCIPLE_V002.md`, file SHA `7333204581ef3183665c9dd056d79f2caa073724e3566295ab888ccc5494c53a`, adjacent seal verified, `[250,1275)`, span SHA `e03ee560a2d60bdd02aec74035a0a67608447846420f8e69962547b6c75d1b60` | In the ordinary flat-asymptotic branch, the durable public record is the outgoing sector of a causally sequential exhaustion governed by the same finite parent; exact completed-record persistence and the recoverable record state stand. | It says source and record results remain distinct and supplies neither a source-inclusive projective state limit nor an infinite-future Møller unitary. It seals the downstream record-sector theorem, not a complete action functional. |
| Fork-8 admitted exhaustion class | packet `FORK_8_CAUSAL_DIRECT_LIMIT_PROMOTION_SPEC_V001.md`, file SHA `ac73f30ae529f4ad3a789b7cc4318540b52275cf98fe2b0498c3ec40d8fec8dc`, `[2789,3256)`, span SHA `5afa0f79a447d7bd0ad007a5201d9cc18aef1c1139c97c2be0a468a707034306` | Promotion is limited to physical exhaustions that add future primitive cells without subdividing an already primitive cell. | This is a declared/admitted scope. It is not a derivation that every exhaustion induced by the missing complete action belongs to that class. |
| One-parent-chain inventory | packet `FORK_8_CAUSAL_DIRECT_LIMIT_PROMOTION_RESULT_V001.md`, file SHA `f84d5b5e8789e5e336db53265cc87dd25f5efddf1cd9c8931f1e521240125d4a`, P5 `[3648,4469)`, span SHA `bed34dfb35acda1790dcd0fcd38e960c5bc237c904e01f482049bfb65495c23d` | Intrinsic measure, causal envelope, first-order parent and descendants, incoming state class, source tail, output state, and dressed representation descend from one sealed parent chain; no separate spectral law is added. | A chain of finite/operator and record-sector objects is not a varied complete source/gauge/gravity/environment action. P5 does not assert that the chain exhausts T5's action terms. |
| E4a | `STAGE8_C1_E4_VERIFICATION_DARIO_V001.md`, file SHA `b760e1b91c93154517ca15e7d93cbf15b490f9667147319b5d6293393ee12eaf`, `[5843,7448)`, span SHA `e91fb0a9a62711eb0d5be2cbbe5409158438b254a5beb8350da89cf6767f8437` | For the cycle-7/DC3 bounded-incidence class, every exhaustion yields the same strong limit generated by the one global incidence operator `B`; cofinality is not needed. | This is an exhaustion-independence theorem for the bounded-incidence colimit. It is not a source-inclusive action-form theorem and flips no complete-parent flag. |
| MF commutativity machinery | MF result `[806,1131)`, span SHA `c0e1c679dfc4fa28673e13f6315899cfd0b172feb20c7560f748d89e530cc42d` | For distinct record cells, `[B_j,B_k]=0`; causal-linear-extension independence follows in the declared pure-charge branch. MF additionally seals pulse independence, earlier-record nondemolition, the central pointer sector, and conditional strongly continuous public dynamics. | Its scope is the declared pure-charge moving-front construction. Shared-source/full-parent operations are not thereby proved to commute, and MF itself leaves the parent binding false. |

### Inventory verdict

The supply is extensive and sharply useful. It gives the entire **consequent
machinery** and a concrete finite/operator candidate for the antecedent. What
it does not give is the antecedent's typed argument: a derived and varied
complete coupled action with an exhaustive descendant inventory.

That distinction is forced by the sources themselves:

1. CIS is adopted before its parent is constructed and expressly distinguishes
   primitive terms from complete-parent descendants.
2. The parent result is finite and operator-native.
3. The GNS/CDL completion is exact on the completed-record algebra and
   expressly not source-inclusive.
4. E4a and MF commutativity have narrower operator/branch scopes.
5. T5 demands an action object and its variation, and bars patching a selector
   in place of that object.

## 3. AS3 — gap type and price

### 3.1 Determination: CONSTRUCTION

`moving_front_bound_by_live_complete_parent` is **not** a verification-only
gap on the existing sealed completion, and it is not already present.

The proposed verification route fails at its first typing step:

```text
wanted:   prove FORM_MF(A_complete)
present:  C_out = completed-record inductive-limit/GNS completion
invalid:  replace A_complete by C_out and prove FORM_MF(C_out)
```

`C_out` has no action variation and is expressly missing the source-inclusive
objects. Proving one-use record compatibility of `C_out` would reproduce the
sealed consequent while leaving unanswered whether every primitive and
descendant of the complete source/gauge/gravity/environment action has that
form. That replacement is exactly the substitute this audit is forbidden to
make.

Nor may the finite operator proposal be silently promoted. It is strong
evidence and the likely receiver of a future proof, but T5 says “derive and
vary,” while the parent specification says forward-sealed construction
specification and the finite result withholds the complete object. A concrete
candidate is not its own completeness/derivation certificate.

Therefore the flag closes only after the construction end of T5 supplies the
action object. The **minimal construction requirement** is:

1. derive the complete compact nonlocal coupled
   source/gauge/gravity/environment action on the physically provenanced
   carrier, with a closed/exhaustive term and descendant inventory;
2. vary that action to obtain its generator/update law, rather than patching
   or choosing `x` or a post-write switch-off;
3. prove that the varied primitive restriction is the sealed finite
   causal-cell write (or exhibit a proved intertwiner), with one-use support,
   new-factor addition, and no completed-factor reuse;
4. replay every generated descendant against the CIS outgoing-sector
   falsifiers, so no omitted source/gauge/gravity/environment term reactivates
   or destroys a completed public record; and
5. only then invoke MF's already-derived pulse, commutativity,
   linear-extension, nondemolition, and central-sector machinery at its exact
   scope.

### 3.2 T5 reading

T5 does **not** bar verification of a form property once its action object has
been lawfully derived. That verification is required by items 3–5 above.
T5 bites **now** because the proposed shortcut changes the object being
verified: the record-sector completion or finite operator would stand in for
the missing complete action. “Do not patch or choose `x`; derive and vary”
bars that substitution by its own words.

### 3.3 Relay price, without invented precision

The construction cannot be honestly priced as an isolated finite relay count
from present stock:

- 820's former **1–2 relay** price applied only to A1 after assuming “no new
  object required.” Relay 821 corrected that score because A1 waits on T5.
- The nearest valid **post-object** comparator remains 820's A1 assembly:
  once `A_complete` and its varied generator exist, the form/intertwining and
  falsifier replay is reasonably **1–2 relays**.
- AXN-BOUND already used four relays (809/812/814/818) merely to type and
  partially bound the admissible family, without deriving a selector or the
  action. That history proves that 1–2 relays cannot price the construction
  itself.
- C1-PRE's two-relay colimit theorem and 820's 4–8 estimate for O1 concern
  different objects; neither may be copied over as a T5 construction price.

Accordingly the honest price is: **T5/AXN-CONSTRUCT, not separately estimable
until its construction specification and release condition exist; then 1–2
relays for the bounded form verification.** This is a refusal of false
precision, not a claim that the construction is costless.

## 4. AS4 — FREEDOMS-CONSUMED and flattening check

### FREEDOMS-CONSUMED

```text
CARRIED, NOT CONSUMED:
  CIS one-use/support law                         adopted at its sealed scope
  finite cell carrier and intrinsic envelope     proposed/derived at finite scope
  first-order parent and generated descendants   carried as finite operator stock
  outgoing-record GNS/CDL completion              carried at record-sector scope
  Fork-8 exhaustion class                         carried as admitted scope
  E4a                                             carried at bounded-incidence scope
  MF commutativity and five positive flags        carried at pure-charge moving-front scope
  complete action                                 carried as absent/T5-fenced

DERIVED HERE:       nothing; gap typed only
CONSTRUCTED HERE:   nothing
VARIED HERE:        nothing
SELECTED HERE:      nothing
SUBSTITUTED HERE:   nothing
SCALING WEIGHTS:    none consumed
FLAGS FLIPPED:      none
PE-1..PE-11:        zero verdict weight; no criterion consulted them
```

### FLATTENING CHECK

- **T5 is live and load-bearing.** The completed-record GNS is not renamed a
  complete action; the finite operator candidate is not promoted to a varied
  complete compact action.
- **CIS is not flattened.** Its adopted primitive support law is not reported
  as a derivation that the eventual action obeys it, and its descendant clause
  remains part of the predicate.
- **E4a/MF scope is not flattened.** Bounded-incidence exhaustion independence
  and pure-charge distinct-record commutation are not promoted to
  source-inclusive full-parent commutation.
- **Decline S25 remains live.** No equal-action or reparameterization principle
  is introduced.
- **Decline S26 remains live.** No smooth/classical object or `C_ref` is used as
  a source.
- **S28/S34 remain conditional.** No downstream value, stable solution, or
  desired comparison selects the action or its form.
- The audit answers the form question without doing the action derivation, so
  it does not become the substitute it was commissioned to detect.

`FLATTENING_CHECK = CLEAN`.

## 5. Self-audit

One process disclosure is recorded. A broad preliminary term search emitted
lines from the principal-expectations ledger before the search was narrowed.
No expectation was used, scored, cited as evidence, or given verdict weight;
the substantive audit was rebuilt entirely from the sealed sources listed
above. Because the standing rule is pointer-only, the accidental emission is
reported rather than hidden.

No numerical value in the cited historical text was used as evidence here;
all computations performed in this relay were byte counts and SHA-256 checks.

PREDICATE = stated checkable (MF `[2497,2818)`, MF gate `[2165,2668)`, CIS `[527,1397)` + `[1430,1933)`, T5 `[8522,9217)`)
SUPPLY = one-use law + finite causal-cell carrier + proposed first-order writes + exact record GNS/CDL completion + Fork-8 admitted exhaustion + E4a/MF commutativity, all cited; complete varied action absent
GAP_TYPE = CONSTRUCTION (minimal requirement: derive and vary the complete coupled action, bind its primitive restriction to the sealed cell write, and replay every generated descendant against the outgoing-sector falsifiers before invoking MF)
PRICE = T5/AXN-CONSTRUCT not separately estimable from current stock; after the action exists, 1–2 relays for bounded form verification (820/821 comparator; four-relay AXN-BOUND history prevents pricing the construction as 1–2)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = NOT CLEAN (+1: broad preliminary search emitted PE-8 text; zero weight, not used)
