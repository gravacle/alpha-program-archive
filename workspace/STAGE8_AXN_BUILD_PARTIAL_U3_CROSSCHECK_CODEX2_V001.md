# STAGE 8 / [PLAN:AXN-BUILD-A23] — CLAIMED CROSS-CHECK OF THE PARTIAL-U3 PLACEMENT
## CODEX 2 LANE (Verifier) — V001

Relay 856. The inbox artifact
`RELAY_PASTE_856_PARTIAL_U3_CROSSCHECK_CODEX2_V001.md` =
`1f18422fdc02c4d2fdfd51bc1ce69569da2b055ab8066268318f57dfe00f3a5e`
was seal-verified before reading. Pickup acknowledgement preceded task work.
`PROGRAM_STATE_BRIEF_V005.md` =
`e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c`
was seal-verified and read.

The first invocation of 856 stopped cleanly because the 855 subject was not
then present. On renewed principal invocation, the subject was present, the
prescribed output was still absent, and the subject seal verified. This report
therefore performs the cross-check; it does not treat the earlier gate stop as
a verdict.

All headline items in this report are `CLAIMED`. PE-1..PE-12 remain
pointer-only and were not opened. This verifier does not rewrite the builder's
artifact.

GATES: `alpha_computed = false`; `proof_authorized = false`;
`kappa_record_computed = false`. No member binding, fixed-point execution, end
test, numerical evaluation of a physical quantity, comparison to a measured
constant, smooth import, or electromagnetic identification occurred.

---

## CLAIMED 1. Seal and source closure

Every file read as evidence was seal-verified first.

| item | SHA-256 | receiving use |
|---|---|---|
| `STAGE8_AXN_BUILD_PARTIAL_U3_DARIO_V001.md` | `54d75ea787820b3e7e3cdea1252cf06034d5cbb82d2df8d0b0678f39cb7d0e57` | subject |
| `STAGE8_AXN_BUILD_ROUND2_FRONTIER_MAP_CODEX2_V001.md` | `5e163d85c49361d315dd8de1d61fc9b50629eb5aee4305fb5465808082331df0` | N1 contract and SC5-D baseline |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_U3_DOR008_DOR009_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md` | `b0118d89e0b4b321fbf9caab5bfb811a0b5fd572e808d02615ee8503db2bc1ac` | finite U3 skeleton and `d_U3` ceiling |
| `STAGE8_TASK4A_P3_SECOND_ATTACK_LAW_SIDE_CONSTRUCTION_AND_NARROWED_STOP_V001.md` | `8e9a09c104f4b6352263591037b2e0bb9a82b659aa1b6276cdd48117f872acec` | exact law-side subpackage, provenance port, four stops |
| `STAGE8_TASK4A_PHYSICAL_INVERSE_SCHUR_COMPLETED_DOMAIN_AND_P_VERDICT_ATTEMPT_V001.md` | `c09783785546a8d6273b2fd104f3aeea0751e83c337ee4e8ac7677d9df87f3d0` | later completed-operation/domain ceiling |
| `STAGE8_TASK4A_P3_COMPLETE_U3_PACKAGE_CONSTRUCTION_AND_FOUR_FIELD_STOP_V001.md` | `f97ee43e052969f0c999b7e57d13310f818222a102c21c249845b8beef1301ff` | upstream four-field flag block actually quoted by 855 |
| `LOCKED_PROCESS.md` | `eae8f9d6f44ef1611b69cbc7d7bac735f7cfde44b6b1c3a2f4af6f1504a54066` | flattening and freedoms-consumed laws |
| `DECLINE_REGISTER_V002.md` | `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a` | authoritative S01-S37 table |

Load-bearing byte blocks were recomputed:

| source | half-open bytes | span SHA-256 | content |
|---|---:|---|---|
| `b0118d89...` | `[1592,2995)` | `b0b294252ec1f0a7149cfc203451d4be2988c112782d80b96d286218871044e9` | finite skeleton true; full U3 false; five original open fields |
| `b0118d89...` | `[20785,21950)` | `6c32c90555d60813237374b3c83566234a89a9398ae09ed4ac21ccdfd5165367` | finite `d_U3` map total; complete map and common-origin derivation false |
| `8e9a09c1...` | `[1824,3038)` | `f471cceea8506278088b7ab37014daf65f799520515594149889bd170d5182e2` | seven-component `P3_LAW_SIDE_SUBPACKAGE`, its status, and four stops |
| `8e9a09c1...` | `[19042,19212)` | `889bca65a58871fd17986e70268bd7617b999f148dd598b6870bb0c8411f2b82` | provenance-port discharge, conditional on DoR-013/014 |
| `8e9a09c1...` | `[19457,19968)` | `126a4c421d61b14a6f4c932a96a2b8951494c4013dfdb284fee7a525850488e0` | four-field roll-up; `d_U3_TOTAL=false`; complete U3 false |
| `c0978378...` | `[14536,16910)` | `2f868a3fab047409d833d0f7edb0687b62ff71d6751e536598dd17059dbdd86b` | completed measure/contour/boundary/domain package remains unbuilt |
| `f97ee43e...` | `[1907,2702)` | `8368dcbbc5d4af2f5708914a67eea9723617b203644e124694a03e819cc7c17f` | concise two positives, four false/TYPE-U fields, U3 false |

### CLAIMED 1.1 N1 source-set result

The N1 contract pins the three law-side/current-ceiling sources
`b0118d89...`, `8e9a09c1...`, and `c0978378...`. The 855 subject contains two
occurrences of `8e9a09c1...`, but zero occurrences of `b0118d89...` and zero
occurrences of `c0978378...`. It instead cites `f97ee43e...` three times for the
concise flag block.

This is a **source-closure correction**, not evidence of authored physical
content:

1. the content-addressed pointer to `8e9a09c1...` is correct;
2. its premise scope is carried correctly as TYPE-P on
   DoR-008/009/013/014, with the provenance port separately conditional on
   DoR-013/014;
3. no premise is widened or silently discharged;
4. but the N1 three-source set is not consumed exactly, because the earlier
   finite-skeleton/`d_U3` ceiling and later completed-domain ceiling are absent
   from the displayed evidence chain;
5. `f97ee43e...` is a sealed upstream authority cited by `8e9a09c1...`, so its
   use does not fabricate content, but it is not a replacement for the two
   omitted N1 pins.

### CLAIMED 1.2 Exact-object versus status display

The exact `P3_LAW_SIDE_SUBPACKAGE` in `8e9a09c1...` is the seven-component
tuple
`(OscCyl, EpostEndpointOrientation, BdGlue_law_src, BdGlue_law_rec, Dom_bdd,
GNS_out, CommonOriginTrace)`. The 855 subject never displays that tuple or its
`P3_LAW_SIDE_SUBPACKAGE_BUILT` atom. It says instead that two true status flags
are “the content of the filled leg.”

The source hash lawfully identifies the full tuple, but two flags are not a
serialization of the tuple. Under decline S12, status flags are not the
objects that discharge them. The placement therefore stands only after this
correction:

```text
PLACED OBJECT = the complete seven-component tuple addressed by 8e9a09c1...
STATUS EVIDENCE = P3_LAW_SIDE_SUBPACKAGE_BUILT and the separately typed
                  provenance/glue flags
STATUS EVIDENCE != PLACED OBJECT
```

No physical field was authored; the defect is binding/display completeness.

---

## CLAIMED 2. Four-stop verification

All four stops match the sealed `f97ee43e...` block byte-for-byte in name,
truth status, and type:

| stop | subject display | sealed result |
|---|---|---|
| measure | `P3_MEASURE_BUILT = false | TYPE-U` | MATCH |
| interacting contour | `P3_INTERACTING_CONTOUR_BUILT = false | TYPE-U` | MATCH |
| complete boundary/edge carrier | `P3_COMPLETE_BOUNDARY_EDGE_BUILT = false | TYPE-U` | MATCH |
| unbounded endpoint domains | `P3_UNBOUNDED_ENDPOINT_DOMAINS_BUILT = false | TYPE-U` | MATCH |

The concise would-build text is the exact text of the verified
`[1907,2702)` block. The subject contains no positive assignment for any of
the four fields, no `U3_008_INSTANCE_EXISTS=true`, no constructed `d_U3`, and
no root-D discharge. No measure, contour, boundary value, extension, endpoint
domain, default, or merge is supplied.

`STOPS = CONFIRMED` is therefore independent of the source-closure and
reachability corrections.

---

## CLAIMED 3. Newly-reachable adjudication

The relevant receiver is not “anything made easier to read.” The relay asks
which `d_U3`/`DESCEND_B0` preconditions the partial placement actually makes
true.

| candidate precondition | before 855 | effect of 855 | adjudication |
|---|---|---|---|
| finite U3 skeleton and finite `d_U3,fin` | already true/TYPE-P at `b0118d89...` | re-addressed indirectly | NOT NEW |
| seven-component law-side P3 subpackage | already true/TYPE-P at `8e9a09c1...` | placed by content-addressed reference | PLACED, NOT NEWLY DERIVED |
| common-origin provenance port | already discharged/TYPE-P on DoR-013/014 at `8e9a09c1...` | status restated | NOT NEW |
| measure | false/TYPE-U | unchanged | UNSATISFIED |
| interacting contour | false/TYPE-U | unchanged | UNSATISFIED |
| complete boundary/edge carrier | false/TYPE-U | unchanged | UNSATISFIED |
| unbounded endpoint domains | false/TYPE-U | unchanged | UNSATISFIED |
| complete U3 instance | false/TYPE-U | unchanged | UNSATISFIED |
| total `d_U3` | false/TYPE-U at `8e9a09c1...` | unchanged | UNSATISFIED |
| `d_U3` contribution to aggregate `DESCEND_B0` | requires complete U3 plus its total map/certificates | unchanged | UNREACHABLE |

The statement “four fields over an already-disclosed common-origin port, not
four fields plus a new origin declaration” is a supported characterization of
the current P3 interface. It is not a newly satisfied `d_U3` or `DESCEND_B0`
precondition. The same characterization was already present in the
`8e9a09c1...` roll-up and in the map's SC5-D row before 855.

The 855 label `NEWLY_REACHABLE` and the claim that root D was newly narrowed in
shape are therefore overstatements. The corrected result is:

```text
NEWLY_REACHABLE_d_U3_DESCEND_B0 = none
DISPLAY_REFINEMENT = the exact already-sealed law-side leg is placed next to
                     the four already-sealed stops
ROOT_D_STATUS = absent and incomplete; count and dependency shape unchanged
```

This correction does not kill the lawful placement. It removes a causal verb
that the before/after statuses do not receive.

---

## CLAIMED 4. Non-completion

The non-completion guard is explicit and repeated:

- `THIS IS NOT A COMPLETE U3`;
- `U3_008_INSTANCE_EXISTS = false | TYPE-U` remains false;
- `THIS IS NOT A DISCHARGE OF ROOT D`;
- `d_U3 IS NOT CONSTRUCTED`;
- the partial record is not declared admissible where a complete package is
  required;
- no false flag is moved to true.

`NON_COMPLETION = CONFIRMED`.

---

## CLAIMED 5. Map-result consistency flags

Three items are surfaced for registrar attention:

1. **Pinned-source roles are not bound.** N1 lists five subjects, including
   the three law-side/current-ceiling sources, but its table has no per-source
   receiver column. The builder could cite only the middle source and still
   say it conformed. A later map revision should bind each pin to its required
   contribution or expressly mark it context-only.
2. **The map requires the exact law-side subpackage; 855 displays two status
   flags as its content.** The source pointer saves identity, but the displayed
   placement is not the map's exact seven-component object until the
   object/status correction in Section 1.2 is applied.
3. **The map's SC5-D row already states the four-field/common-trace shape.** The
   855 result is consistent with that row as a placement, but inconsistent
   when it calls the same shape a new narrowing or a newly reachable
   precondition.

These flags do not change the map's root graph: SC5-D remains an input to
`d_U3`; it is not produced by `DESCEND_B0`, and the partial placement does not
unlock it.

---

## CLAIMED 6. FREEDOMS-CONSUMED

```text
CARRIED-AS-PARAMETER:
  DoR-008/009/013/014 premise dependence of the law-side subpackage;
  the already-declared common-origin port, only at its sealed TYPE-P scope;
  all four false/TYPE-U field statuses;
  incomplete-U3 and incomplete-d_U3 status.

CONDITIONED-ON:
  every positive law-side statement remains conditioned on its exact premise
  list; no premise is absorbed by placement.

SUBSTITUTED:
  none.

SELECTED:
  none — no measure, contour, boundary condition, extension, endpoint domain,
  U3 member, B0 member, topology, or physical value.

CORRECTED, NOT CONSUMED:
  a status flag cannot substitute for the seven-component subpackage or for a
  trace object; the source tuple supplies the object identity.
```

No freedom was used to rescue a missing field or convert a placement into a
completion.

---

## CLAIMED 7. Flattening check and absence discipline

The subject's claimed `37/37` flattening line is not itself clean:

- it calls `S03` “the void condition,” but authoritative
  `DECLINE_REGISTER_V002.md` S03 is the refusal to identify the comparison
  group, local gauge-coordinate action, and projective-ray quotient as three
  interchangeable `U(1)` assumptions;
- the applicable object/status decline is S12;
- 855's use of two status flags as “the content” of the placed subpackage is
  exactly the S12 class and requires the correction in Section 1.2;
- S08, S19, S24, and S26 are not violated: no EM/smooth identification,
  masslessness-to-decay inference, clustering rescue, or `C_ref` source use
  occurs.

Thus the physical no-import result is clean, while the builder's flattening
transcript is **CORRECTED** for one wrong row label and one status/object
binding. This cross-check has walked the load-bearing identifications against
the authoritative V002 table rather than repeating `37/37` without receivers.

No new corpus-wide absence is claimed here. The four TYPE-U absences are
sealed status rows, and the two missing subject pins are fixed-string facts
about the 855 bytes. Law-9 discipline is therefore satisfied without turning
a bounded document sweep into a nonexistence theorem.

---

## CLAIMED 8. Battery and self-audit

```text
F_PLDEC         = PASS (no physical quantity evaluated)
ANTI_TUNING     = PASS (no value, branch, or member selected)
M2_CASE         = PASS
M2_SPACING      = PASS
M2_BOUNDARY     = PASS (full hashes and half-open spans used)
M2_RECEIVER     = PASS (display/readability separated from d_U3/DESCEND reach)
PIN_CHECK       = PASS before seal
PE_POINTER_ONLY = PASS
FLATTENING      = CORRECTED (S03 label; S12 object/status binding)
```

Verb-audit controls: every headline is `CLAIMED`; a lawful pointer placement is
not called a new derivation; existing trace/port content is not called a new
`d_U3` precondition; false/TYPE-U is not called nonexistence; the four stops
are not weakened; a status is not called an object; premise-dependent content
is not made unconditional; correction does not become construction.

PLACEMENT = CORRECTED (N1 source closure omits b0118d89... and c0978378...; the exact seven-component subpackage must be distinguished from two status flags; no physical content was authored and the 8e9a09c1... pointer/scope stand)
STOPS = CONFIRMED (4 displayed)
NEWLY_REACHABLE = CORRECTED (no d_U3 or DESCEND_B0 precondition became newly true; the common-origin port and four-on-one-trace shape were already sealed)
NON_COMPLETION = CONFIRMED
MAP_FLAGS = listed (pinned-source roles unbound; exact-object display incomplete; SC5-D shape pre-existed the claimed narrowing)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+7 scope controls: all headlines CLAIMED; placement not derivation; status not object; premise scope retained; no absence theorem; no field supplied; correction not construction)
