# R3.4 Parent-State Covariance Adjudication Specification v001

Date: 2026-07-24

## Purpose

Test the live microscopic-parent lineage against the sealed
Parent-State Covariance Principle before constructing an outgoing spectral
measure. This gate may invalidate earlier conditional durability claims, but
it may not replace missing parent data with a convenient continuum model.

No alpha, measured coupling, mass, endpoint, or cosmological value may enter.

## Authorities

The adjudication must read:

```text
PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md;
CURRENT_AUTHORITY_LEDGER_V013.json;
PRIMITIVE_REVERSIBLE_RECORD_WRITE_PRINCIPLE_V001.md;
PRIMITIVE_REVERSIBLE_RECORD_WRITE_PRINCIPLE_V002.md;
SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003.md;
COMPLETE_PARENT_ACTION_UNDERDETERMINATION_GATE_V001.md;
PRIMITIVE_TRANSPORT_ONLY_PHASE_COMPLETE_GENERATOR_PRINCIPLE_V001.md;
BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md;
R3_4_PARENT_TO_OUTGOING_GNS_COMPATIBILITY_RESULT_V001.md;
CAUSAL_DIRECT_LIMIT_REDUNDANT_RECORD_RESULT_V001.md.
```

Version 002 of the reversible-write file is the authority correction over
version 001. The current authority ledger's protected false flags may not be
promoted by a subordinate result.

## Tests

1. Verify the Parent-State Covariance Principle seal.
2. Recompute the one-cell static-parent completed-label invariance test:

   ```text
   ||[c_partial,P_p]||_F=sqrt(2).
   ```

3. Determine whether the redundancy result relies on the superseded v001
   controlled-write principle and whether the live authority derives a
   complete physical write operator.
4. Separate two logically different exclusions:

   ```text
   Parent-State Covariance compatibility;
   adopted primitive transport-only/single-operator admissibility.
   ```

   A local Pauli-completed parent is not rejected by covariance merely
   because the adopted transport-only branch rejects it.
5. Test whether the live parent supplies, in one lineage:

   ```text
   compatible finite states;
   compatible finite derivations;
   a parent-derived compact write/scattering defect;
   an outgoing GNS generator;
   a finite-parent root in its form domain;
   and the root spectral measure.
   ```

## Sealed adjudication rules

Return:

```text
PARENT_STATE_COVARIANCE_CURRENT_PARENT_PASSES
```

only if every required object descends from one live parent authority.

Return:

```text
PARENT_STATE_COVARIANCE_CURRENT_PARENT_BLOCKED
```

if the static parent fails completed-label invariance and the live authority
does not derive a complete scattering or post-write parent.

The gate may not:

```text
reactivate the superseded v001 controlled-write principle;
treat conditional record holonomy as a complete write operator;
credit the Pauli exclusion to Parent-State Covariance;
select an outgoing density separately;
or promote any protected false alpha/proof flag.
```

## Fixed statuses

```text
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
