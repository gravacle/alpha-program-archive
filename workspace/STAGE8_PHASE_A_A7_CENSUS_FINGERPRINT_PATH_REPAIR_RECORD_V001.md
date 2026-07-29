# Stage 8 Phase A A7 Census Fingerprint Path Repair Record v001

Date: 2026-07-29

## Scope

This artifact records the Phase A A7 repair of the external irreducible-mode
census fingerprint hardwire. It is a process repair record only.

No census gate is rerun here. No missing downstream report is fabricated. No
C-L3 coefficient, `kappa_record`, `kappa_Thomson`, alpha, `x`, `rho`, or `T_R`
is computed.

## Pre-Repair Obstruction

`STAGE8_P2_PUBLIC_SUPERDETERMINANT_PRECONDITION_RESULT_V001.md:81-84`
records that the existing census script was hardwired to the v001 operator
fingerprint path while the successor fingerprint existed:

```text
results/alpha_br_operator_artifact_fingerprint_v002.json
SHA-256: cad951f687dda61bcfe92eac92b3358fe373206ff99417b28f29518ad5a15f0f
```

The affected local script was:

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/scripts/audit_alpha_br_external_irreducible_mode_census_v001.py
```

Before repair it bound `FINGERPRINT_JSON` to
`results/alpha_br_operator_artifact_fingerprint_v001.json`.

## Repair Performed

The local script now separates the two fingerprint paths:

```text
FINGERPRINT_JSON_V001 = ROOT / "results" / "alpha_br_operator_artifact_fingerprint_v001.json"
FINGERPRINT_JSON_V002 = ROOT / "results" / "alpha_br_operator_artifact_fingerprint_v002.json"
```

It adds `--fingerprint-json`, defaulting to the v002 successor when present
and otherwise falling back to v001. The validation function now accepts either:

```text
PASS_CURRENT_OPERATOR_ARTIFACT_FINGERPRINT
CURRENT_OPERATOR_ARTIFACT_FINGERPRINT_SUCCESSOR_RECOMPUTED
```

For the successor status it additionally requires:

```text
missing_count == 0
predecessor_status == PASS_CURRENT_OPERATOR_ARTIFACT_FINGERPRINT
```

and still recomputes each tracked file hash before reporting the fingerprint
current.

## Verification

The patched local script was syntax-checked only:

```text
PYTHONPYCACHEPREFIX=/private/tmp/codex_pycache python3 -m py_compile scripts/audit_alpha_br_external_irreducible_mode_census_v001.py
```

The patched local script SHA-256 is:

```text
251dc6eb1600dcd4dfb655d2e17e6036433edbb654859a225b130da0c529a5cb
```

No project census run was executed.

## Residue

`STAGE8_P2_PUBLIC_SUPERDETERMINANT_PRECONDITION_RESULT_V001.md:86-129`
still records three missing hardwired deliverables:

```text
reports/alpha_br_external_prime_superdeterminant_v001.md
reports/alpha_br_public_conformal_contour_v001.md
reports/alpha_br_external_logdet_tail_v001.md
```

The A7 path hardwire is repaired as a script typing defect. The P2 precondition
does not close and the census remains blocked on the missing deliverables and
the absence of an authorized rerun.

## Protected Flags

```text
A7_fingerprint_path_hardwire_repaired = true
P2_executed = false
C_L3_computed = false
kappa_record_computed = false
kappa_Thomson_computed = false
x_computed = false
rho_computed = false
T_R_computed = false
alpha_computed = false
proof_authorized = false
```
