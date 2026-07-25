# R3.4 Dressed Outgoing-Record Range Correction Result v001

## Verdict

```text
STABLE_DRESSED_RECORD_MONOMORPHISM_DERIVED
```

The earlier phrase "public-record Moller endomorphism" was too strong. The
stabilized Heisenberg map does not generally take the bare record-only
algebra into itself. It takes that algebra isomorphically into a
source-dressed subalgebra of the full parent algebra.

This result supersedes the bare-endomorphism flags in:

```text
R3_4_SHARED_SOURCE_CAUSAL_PARENT_RESULT_V001.md
R3_4_CAUSAL_SHARED_SOURCE_MOLLER_DURABILITY_RESULT_V001.md
```

Their numerical causal-order, state-restriction, Moller, and pointer-
persistence results remain valid.

## Complete range test

For all nine matrix units of the first three-state record factor,

```text
Phi_N(E_ab)
 =W_N^*(I_source tensor E_ab tensor I)W_N
```

stabilizes after the first closure. The maximum change after the overlapping
second source event is

```text
5.28e-15.
```

However, eight matrix-unit images lie a Frobenius distance `2` from the bare
record-only algebra. For the pointer projector:

```text
||Phi(P_pointer)-E_R(Phi(P_pointer))||_F=2;
```

and its commutator with a source observable has norm

```text
1.7320508075688774.
```

The source dressing is therefore real and cannot be omitted.

## Correct algebraic object

The map passes a complete matrix-unit test:

```text
maximum star error:            0
maximum multiplication error: 3.64e-15
unitality error:               6.45e-15
maximum norm error:            2.22e-15
```

It is consequently a stable unital injective star-homomorphism from the
record algebra into the full source-record algebra. Equivalently, the full
parent contains a dressed outgoing copy of the public record algebra.

The bare output-record state restrictions remain compatible, with error
`8.78e-16`.

## Scope correction

```text
prior_bare_record_endomorphism_claim_superseded = true
bare_record_endomorphism_derived = false
stable_dressed_record_monomorphism_derived = true
dressed_output_record_algebra_embedded_in_full_parent = true
bare_output_record_state_family_restriction_compatible = true
```

Still open:

```text
same_GNS_unitary_Moller_implementer_derived = false
complete_parent_to_outgoing_GNS_map_derived = false
generated_descendant_action_derived = false
complete_physical_durability_derived = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
