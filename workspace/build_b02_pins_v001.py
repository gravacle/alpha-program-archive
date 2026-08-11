#!/usr/bin/env python3
"""
build_b02_pins_v001.py -- pin generator for STAGE8_DESC_B02_DARIO_V001.md (relay 1005, DARIO lane).

WHAT THIS IS.  A TOOL, NOT EVIDENCE.  It computes every file digest and every byte-span digest that
the B02 artifact pins, so that no digest and no byte offset in that artifact is typed by hand.
Span boundaries are located by ANCHOR STRINGS and the offsets are COMPUTED, then printed; the
artifact quotes the printed offsets.  Nothing here constructs, selects, adopts, or evaluates any
descent object.  It performs no arithmetic on any physical quantity.

DECLARED INPUTS (Q-920 input-custody rule: no undeclared, unsealed input).
  Every file this script opens is listed in FILES below, at its FULL PATH from the
  alpha-program-archive root (Q-913 path rule).  It reads NOTHING ELSE -- no JSON sidecar, no
  environment, no network, no directory walk.  Run it from the archive root.

USAGE
  cd /Users/bgm/MB Work/alpha-program-archive && python3 workspace/build_b02_pins_v001.py
"""

import hashlib
import sys

ROOT = "."

# ---------------------------------------------------------------- declared inputs (full paths)

FILES = [
    ("M01", "relay_inbox/RELAY_PASTE_1005_B02_BUILD_DARIO_V001.md"),
    ("M02", "supervision/PROGRAM_STATE_BRIEF_V005.md"),
    ("M03", "supervision/LOCKED_PROCESS.md"),
    ("M04", "supervision/DECLINE_REGISTER_V002.md"),
    ("M05", "supervision/QUESTIONS_SETTLED_REGISTER_V001.md"),
    ("M06", "supervision/DECISION_OF_RECORD_013_GEN_OMEGA_RATIFIED_FAMILY_LEVEL_2026-08-02_V001.md"),
    ("M07", "workspace/STAGE8_DESC_AUDIT_CODEX2_V002.md"),
    ("M08", "workspace/STAGE8_DESC_DEMAND_DARIO_V006.md"),
    ("M09", "workspace/STAGE8_DESC_B01_DARIO_V002.md"),
    ("M10", "workspace/STAGE8_AXN_B0_ACCEPTANCE_INVERSE_CODEX2_V001.md"),
    ("M11", "workspace/STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md"),
    ("M12", "workspace/STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V003.md"),
    ("M13", "workspace/STAGE8_AXN_ORIGIN_PRODUCER_CODEX2_V001.md"),
    ("M14", "workspace/STAGE8_AXN_BUILD_B0_ROOT_CENSUS_CODEX2_V001.md"),
    ("M15", "workspace/STAGE8_TASK2D_MULTIAXIAL_STATE_TRANSITION_ENVELOPE_SPECIFICATION_V001.md"),
    ("M16", "workspace/STAGE8_P5_COMMON_ORIGIN_DESCENT_REQUIREMENT_V001.md"),
    ("M17", "workspace/STAGE8_FROZEN_PRIMITIVE_INVENTORY_PREFREEZE_RESULT_V001.md"),
]

# ------------------------------------------------------------------------------ span locators
#
# Each entry: (pin_id, member_id, start_anchor, end_rule, note)
#   end_rule ("line",)              -> span ends AFTER the newline terminating the anchor's line
#                                      (the audit's own table-row convention: B01's pinned
#                                      [32217,32292) includes its trailing newline)
#   end_rule ("to", anchor)         -> span ends at the first occurrence of anchor at-or-after start
#   end_rule ("through", anchor)    -> span ends AFTER the first occurrence of anchor
#   end_rule ("fixed", a, b)        -> literal [a,b), used ONLY to re-verify a span an upstream
#                                      sealed artifact already pinned, so a mismatch is visible

SPANS = [
    # --- the row being built, and its predecessor, at the audit's own row convention
    ("S01", "M07", b"| `B02` | target-independent constructor", ("line",),
     "THE B02 ROW -- the row this relay builds"),
    ("S02", "M07", b"| `B01` | content-addressed exhaustive", ("line",),
     "the B01 row, for the convention check against B01 V002's pin 397e300c..."),

    # --- the audit's ingredient classification for B02's four ingredients
    ("S03", "M07", b"| 02 | inhabited complete B0 candidate", ("line",), "audit item 02 -- INPUT"),
    ("S04", "M07", b"| 03 | target-independent B0 constructor", ("line",), "audit item 03 -- INPUT"),
    ("S05", "M07", b"| 04 | complete candidate signature instance", ("line",), "audit item 04 -- MIXED"),
    ("S06", "M07", b"| 05 | B0 provenance/domain certificate", ("line",), "audit item 05 -- MIXED"),

    # --- the audit's positive material rows P1/P2 (the partial subtraces) and the stop rule
    ("S07", "M07", b"| `P1` | frozen primitive origin", ("line",), "audit P1 -- source-sector subtrace"),
    ("S08", "M07", b"| `P2` | finite PathCert/common-origin subtrace", ("line",), "audit P2 -- finite subtrace"),
    ("S09", "M07", b"DESCENT_STOP_RULE_V001", ("to", b"\n```\n\nThis rule is installed"),
     "the installed descent stop rule, clauses 1-7"),
    ("S10", "M07", b"The **frozen joint common-origin trace required by K7", ("to", b"\n\n### 3.2"),
     "audit 3.1 -- the trace verdict"),

    # --- the receiver bar
    ("S11", "M10", b"### A01 \xe2\x80\x94 inhabited frozen B0-role candidate", ("fixed", 7262, 10112),
     "A01-A05 whole, the U7 span (demand V006 member 11)"),
    ("S12", "M11", b"```text\nCompleteMicroscopicBoundaryOriginCandidate :=", ("through", b"Obj_B0 conforms_to Sig_B0\n```"),
     "stop spec: the five-field candidate tuple and the minimal signature disclosure"),
    ("S13", "M11", b"C0 = joint carrier/algebra", ("fixed", 37523, 38115), "B0 role contents"),
    ("S14", "M11", b"The interface relation is:", ("fixed", 38121, 38437), "the B0 interface relation"),
    ("S15", "M11", b"test_id = B0-T1-OBJECT-DOMAIN-CONFORMANCE", ("to", b"\n```"),
     "T1, the conformance test A04's oracle must feed"),

    # --- the ratified ground
    ("S16", "M06", b"- THE ANCHORED GENERATIVE FAMILY", ("to", b"\n\n## WHAT THIS COMPLETES"),
     "DoR-013: family-level adoption, NO MEMBER IS SELECTED EVER, and the three generative maps"),
    ("S17", "M12", b"## 7. Primitive tuple and three maps", ("fixed", 22842, 24541),
     "Gen_Omega section 7 -- the primitive tuple, d_state/d_ready/d_law, and the T0-T8 order"),
    ("S18", "M12", b"# Stage 8 `Gen_Omega` Generative-Origin-Rule Adoption Proposal v003", ("through", b"(DoR-013 RESERVED)**"),
     "the proposal's own pre-ratification header, superseded by DoR-013"),

    # --- what is absent, at bytes
    ("S19", "M13", b"### 2.1 Field-by-field inhabitance audit", ("fixed", 8902, 10649),
     "the origin producer's field-by-field audit -- five UNBOUND/UNINSTANTIATED/WRONG-CODOMAIN rows"),
    ("S20", "M14", b"| inhabited frozen B0-role candidate |", ("line",),
     "the B0 root census: MATERIAL-ABSENT for the candidate"),
    ("S21", "M14", b"| complete candidate signature |", ("line",),
     "the B0 root census: MATERIAL-PARTIAL for the signature"),
    ("S22", "M15", b"### 4.2 Path-level witness specification", ("fixed", 19909, 21513),
     "PathCert(Omega): the field schema, the commuting squares, and INSTANTIATED = false"),

    # --- the demand this build is scored against, and B01's forward obligation
    ("S23", "M08", b"| 19 | An **inhabited** frozen B0-role candidate", ("to", b"\n\n**G \xe2\x80\x94"),
     "demand V006 conditions 19-23, the U7 group that binds B02 directly"),
    ("S24", "M09", b"## 4. What stops, and why it is a stop", ("to", b"\n\n---\n\n## 5."),
     "B01 V002's exhaustiveness stop -- the Q-914 forward obligation this signature is to serve"),
    ("S25", "M17", b"complete_corpus_wide_primitive_inventory_exhaustiveness = NO_VERDICT", ("to", b"\n```"),
     "the prefreeze result's own NO_VERDICT, blocked on the Obj_0 signature"),
]


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main() -> int:
    blobs = {}
    print("=" * 100)
    print("DECLARED INPUTS -- file digests computed at run time, full paths from the archive root")
    print("=" * 100)
    for mid, path in FILES:
        try:
            with open(path, "rb") as fh:
                b = fh.read()
        except OSError as exc:
            print(f"{mid}  FATAL: cannot read {path}: {exc}")
            return 2
        blobs[mid] = b
        print(f"{mid}  {sha(b)}  {len(b):>9,} B  {path}")

    print()
    print("=" * 100)
    print("PINNED SPANS -- offsets LOCATED by anchor, digests COMPUTED; nothing typed")
    print("=" * 100)
    rc = 0
    for pin, mid, anchor, rule, note in SPANS:
        b = blobs[mid]
        s = b.find(anchor)
        if s < 0:
            print(f"{pin}  {mid}  FATAL: anchor not found: {anchor!r}")
            rc = 2
            continue
        kind = rule[0]
        if kind == "line":
            e = b.find(b"\n", s) + 1
        elif kind == "to":
            e = b.find(rule[1], s)
        elif kind == "through":
            e = b.find(rule[1], s) + len(rule[1])
        elif kind == "fixed":
            s, e = rule[1], rule[2]
        else:
            print(f"{pin}  FATAL: bad rule {rule!r}")
            rc = 2
            continue
        if e <= s:
            print(f"{pin}  {mid}  FATAL: end anchor not found after start")
            rc = 2
            continue
        print(f"{pin}  {mid}  [{s},{e})  {e - s:>6,} B  {sha(b[s:e])}")
        print(f"      {note}")
    print()
    print("PINS =", len(FILES), "files +", len(SPANS), "spans")
    print("This script computed digests only.  No physical quantity was evaluated, no scale was")
    print("fixed, no member was bound, no fixed point was executed, no comparison to any measured")
    print("constant was formed.")
    return rc


if __name__ == "__main__":
    sys.exit(main())
