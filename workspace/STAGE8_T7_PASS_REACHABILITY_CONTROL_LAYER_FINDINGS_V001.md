# Stage-8 T7 PASS-Reachability Control — Layer Findings V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY. THE CONTROL IS NOT COMPLETE. NO PASS OBSERVED, AND NO CLAIM
IS MADE THAT ONE IS OR IS NOT REACHABLE.
What IS established: FOUR distinct binding layers stand between an honest
agreeing bundle pair and the component comparison, each found by hitting
it. The component comparison was never reached, so the five
never-executed accepting-branch gates remain never-executed.
STOPPED DELIBERATELY at a principled boundary (§3), not because the work
became hard. PRODUCTION PROHIBITED ON BOTH GATES.
```

## §1 — What was built and how far it got

```text
CONSTRUCTION (corrected from the name-matched first attempt): walk each
bundle's MANIFEST COMPONENT STRUCTURE — manifest.matrix_components[
category][identifier] -> npz key — and back-transport per component:
    M_ind := O^H M_prim O      for every transported category
    M_ind := M_prim            for record_projectors (not transported)
COVERAGE ACHIEVED: 138 back-transported, 3 copied untransported,
ZERO identifiers missing. Measured unitarity residual of O: 0.0 EXACTLY.
So by construction transported == primary identically for every one of the
138 transported components — the exact condition the 34 failures violate.
INVOCATION: the REAL comparator, UNMODIFIED, through the REAL launcher
v007 (satisfying precondition 1, which refused direct invocation).
DISCLOSED DEVIATION: the CONTROLLER wrapper was not used. Its receipt
cross-check would correctly reject a synthesised bundle, so using it would
require forging a receipt — which is the one thing this control must not
do. The comparator's own comment is the authority for why this is
acceptable: the receipt digests "are RECORDINGS for the anchored receipt
chain, not self-authentication ... by themselves they authenticate
nothing."
```

## §2 — THE FOUR LAYERS, in the order they were hit

Each was found by running into it. None was predicted in advance.

```text
L-1  RUNTIME ATTESTATION. Direct import-and-call raises ComparisonBlocked:
     "comparison requires the sealed Stage-8 runtime launcher".
     RESOLVED legitimately: invoke through the launcher.
L-2  ADJACENT SEALS. "independent JSON adjacent-seal hash mismatch". The
     derive lane's .seal.sha256 describes the bundle that was replaced.
     RESOLVED legitimately: a seal that does not match its file is simply a
     wrong seal; the synthetic bundle's own seals were rewritten, in the
     disposable copy only.
L-3  BUNDLE SELF-BINDING. "independent NPZ binding mismatch" —
     payload["npz_sha256"] must equal the NPZ's own digest (comparator
     line 829) — and separately payload["manifest_sha256"] must equal
     canonical_sha256(manifest) (line 901).
     RESOLVED legitimately: a bundle must describe itself; both were
     recomputed with the comparator's OWN canonical_sha256.
L-4  INTERNAL DIAGNOSTIC-TO-AGGREGATE BINDING. *** NOT RESOLVED, AND
     DELIBERATELY NOT RESOLVED. *** "independent production diagnostic is
     not bound to aggregate ell0.p1.all". The bundle's diagnostic arrays
     must be consistent with its aggregate matrix components. The
     synthesis replaced the aggregates but left the independent lane's own
     diagnostics untouched, so they no longer agree.
```

## §3 — THE BOUNDARY, and why the work stopped here rather than continuing

```text
L-1, L-2 and L-3 are PROVENANCE WRAPPERS: they assert that a bundle is
what it says it is. For a SYNTHETIC bundle, re-describing it truthfully is
not a relaxation — the new seals and digests are CORRECT statements about
the new content. Nothing was weakened.
L-4 IS DIFFERENT IN KIND. It is an INTERNAL PHYSICAL CONSISTENCY relation
of the lane's own output — the diagnostics and the aggregates must agree
because they are two views of the same computation. Overriding it by hand
would produce a bundle that is NOT SELF-CONSISTENT, and a PASS obtained
from such a bundle WOULD PROVE NOTHING: it would demonstrate that the
comparator accepts a fabricated object, which is the opposite of the
question asked.
*** THE STOPPING RULE THIS LANE APPLIED, STATED SO IT CAN BE CHECKED:
re-describing a synthetic bundle is legitimate; forcing its internal
physics relations to agree without recomputing them is FABRICATION. The
control stops at that line. ***
THE HONEST ROUTE PAST L-4, named so it is not rediscovered: back-transport
the ENTIRE independent bundle — every array carried in the source basis,
diagnostics included — by the same unitary conjugation, so the whole
object is one consistent transported copy rather than a spliced one.
Unitary conjugation preserves every internal relation, so a fully
transported bundle should satisfy L-4 by construction rather than by
override. That is the next attempt.
```

## §4 — What this already establishes, independent of the outcome

```text
1. THE ANSWER TO "WHY HAS THE ACCEPTING BRANCH NEVER RUN" IS NOW CONCRETE
   AND MEASURED: at least four independent binding layers sit between an
   honest agreeing pair and the component comparison, and the component
   comparison is itself upstream of the five gates that have never
   executed. The accepting path is not one branch behind one condition; it
   is behind a chain.
2. THE COST IS REAL AND BELONGS NEXT TO RULE 8. The principal's reasoning
   was that each integrity mechanism adds surface that itself needs
   verifying. This control is a direct measurement of that: the machinery
   built to prove the pipeline honest is the same machinery that has
   prevented anyone from ever demonstrating it can succeed. That is not an
   argument to remove it — it is the quantified price, and it was not
   visible until something tried to reach a PASS.
3. THE CONSTRUCTION ITSELF IS SOUND WHERE MEASURED. 138/138 transported
   components covered, zero missing identifiers, overlap unitarity
   residual exactly 0.0. If a PASS is reachable, this is the right shape of
   input to reach it with.
4. NOTHING IS CONCLUDED ABOUT v003. P-D1/P-D2 remain unscoreable until the
   accepting branch is shown reachable, which was the whole reason this
   control precedes v003 in the build order.
```

## Protected status

```text
pass_control_complete = false
pass_observed = false
pass_unreachable_claimed = false
binding_layers_found = 4
layers_resolved_legitimately = 3            (L-1, L-2, L-3)
layer_deliberately_not_overridden = L-4     (internal consistency)
fabrication_boundary_recorded = true
transported_components_covered = 138_of_138
identifiers_missing = 0
overlap_unitarity_residual = 0.0
component_comparison_reached = false
accepting_branch_gates_executed = 0_of_5
controller_wrapper_exercised_on_pass_path = false
next_attempt = full_bundle_unitary_back_transport_including_diagnostics
v003_started = false
D3_object_spec_status = HELD_PENDING_PRINCIPAL
sliver_naturality_attempt_started = false
production_authorized = false
alpha_computed = false
proof_authorized = false
```
