# Stage-8 T7 Controller v006 Repair Binding V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY_REPAIR_BINDING_SEALED_BEFORE_AUTHORING
```

Implements the reviewer batch-audit BLOCKING 3 and MAJORs M-a/M-b/M-c.
Scope is EXACTLY this list; authored under discipline rules 1-4.

```text
1. controller v006 (base v005; sole changes):
   a. BLOCKING 3: hoist ALL FOUR bundle/receipt provenance conditions
      that comparator v005 enforces (executor row, launcher row,
      attested target hash, manifest stamp) into the comparison-lane
      pre-flight, verified against both bundles on disk BEFORE the
      comparison path is consumed. The enumeration method is
      mechanical per the rule's corollary: enumerate every require()
      in the comparator's bundle-provenance section and prove each is
      pre-flighted (the verification artifact lists the mapping
      comparator-require -> pre-flight step).
   b. M-a/M-b: hoist the primary derive lane's pinned-digest +
      input-inventory + Route-1-rerun preconditions into the
      controller pre-flight (PRECONDITIONS tuple extended; order
      documented).
2. test_controller v006 (base v005): fixtures updated; M-c: the
   real-chain startability test regains teeth — with manifest v004
   present it asserts PREFLIGHT_OK *and* additionally drives one REAL
   precondition regression (a temporarily-staged fixture-side
   corruption of a NON-canonical staging copy is not possible against
   the read-only canonical root, so the teeth are restored by
   asserting the full eight-step enumeration content and by a
   fixture-root real-launcher variant that corrupts a fixture manifest
   row and must block at the same step — the REAL launcher and REAL
   controller drive both assertions; no stub).
3. launcher v006: NOT authored (launcher v005 + quarantine satisfy
   rules 1-3; no allowlist change is in scope, and controller v006
   replaces the v005 row via manifest v005).
4. manifest v005 (+ seal) over the updated inventory after
   verification; anchor; then STOP pipeline work pending re-audit.
```

## Protected status

```text
alpha_computed = false
proof_authorized = false
```
