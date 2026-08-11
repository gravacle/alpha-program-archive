#!/usr/bin/env python3
"""
build_q92c_execution_pins_v001.py
PIN GENERATOR for STAGE8_DESC_Q92C_EXECUTION_DARIO_V001.md  (relay 1042, DARIO lane)

DECLARED INPUTS: exactly members 01-24 of the MEMBERS table below.  Nothing else is
opened, hashed, or consulted.  Every path is resolved from the alpha-program-archive
ROOT and rehashed at that path at run time (Q-913).

REFUSAL PATHS (Q-920/Q-924).  The generator emits NOTHING -- no member table, no span
table, no partial output -- if any of these fires:

  R1  a declared member is unreadable at its declared archive-root path.
  R2  a FIXED span's recomputed digest does not agree with the upstream pin it carries,
      at the width the upstream published that pin.  A mismatch is a REFUSAL, never a
      correction.  PIN-WIDTH CONVENTION carried unchanged from relay 1040: a pin is
      recorded at exactly the width the upstream published (64 hex, or an 8-hex display
      truncation labelled FIXED-PIN8), and NO TAIL IS EVER INVENTED to make a truncated
      pin look full.
  R3  an ANCHOR span's start anchor is absent, or occurs more than once (AMBIGUOUS).
  R4  an ANCHOR span's end anchor is absent, or does not occur at/after the start.
  R5  SELF-CITATION BAR: a span row names a DARIO-lane artifact of this relay's own
      lineage (member 22, the 1040 execution).  Closed FOR CARRIAGE ONLY.  Enforced here
      by construction, not by the author's discipline.

SPAN CONVENTION: raw bytes, half-open [a,b), no decoding, no newline normalisation.
CITATION RULE: CLOSURE_MEMBER_CITATION_RULE_V001 -- canonical path + full source SHA-256
+ half-open interval + full span SHA-256 on every emitted row.
"""

import hashlib
import os
import sys

ROOT = "/Users/bgm/MB Work/alpha-program-archive"
W, S, R = "workspace/", "supervision/", "relay_inbox/"

MEMBERS = [
    ("01", R + "RELAY_PASTE_1042_PRECONSTRUCTION_EXECUTION_DARIO_V001.md", "the assignment"),
    ("02", R + "RELAY_PASTE_1039_FRESH_SESSION_BOOTSTRAP_DARIO_V005.md", "the bootstrap; the SYMBOLIC LINE"),
    ("03", W + "DEMAND_READING_DECISION_OF_RECORD_V001.md", "THE GUARD, and the governing reading"),
    ("04", W + "STAGE8_JOINT_P0_BUILDABILITY_IN_PRINCIPLE_RESULT_V001.md", "THE SIX ROWS at their sealed source"),
    ("05", W + "STAGE8_OBJ0_EXACT_SIGNATURE_DOMAIN_CODOMAIN_SPEC_AND_BUILD_STOP_V001.md", "rows 1/4/5/6 at SCHEMA depth; the two-phase dependency order"),
    ("06", W + "STAGE8_FROZEN_PRIMITIVE_INVENTORY_PREFREEZE_RESULT_V001.md", "ROW 2's dedicated sealed result"),
    ("07", W + "STAGE8_COMMON_ORIGIN_GENERATIVE_VS_FORMATION_TYPING_V001.md", "ROW 3's negative: the joint generative P0 unconstructed"),
    ("08", W + "STAGE8_DESC_SOURCE_HUNT_CODEX2_V001.md", "the both-lane four-modality hunt (Q-949)"),
    ("09", W + "STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md", "THE PROVENANCE CEILING"),
    ("10", S + "DECISION_OF_RECORD_008_FIELD_CTP_ADOPTION_RATIFIED_WITH_FALSIFIER_2026-08-01_V001.md", "DoR-008: ratified premises, marks, void trigger"),
    ("11", W + "STAGE8_FIELD_CTP_CARRIER_AND_C0_JOIN_INSTANTIATION_ATTEMPT_V001.md", "THE OPEN FORCING SLOT -- the ceiling ruling's ground"),
    ("12", W + "STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V003.md", "READ ONLY, with 13 and 14"),
    ("13", W + "MEMBER12_HEADER_OVERLAY_RECORD_V002.md", "the overlay of record; the read rule"),
    ("14", S + "DECISION_OF_RECORD_013_GEN_OMEGA_RATIFIED_FAMILY_LEVEL_2026-08-02_V001.md", "the ratification, by digest"),
    ("15", W + "STAGE8_AXN_STATE_ALGEBRA_MAP_CODEX2_V001.md", "A_C0 typing; res_B; the U2 bypass locus"),
    ("16", W + "STAGE8_AXN_S1_MEMBER_ATTEMPT_CODEX2_V001.md", "the sealed S1 receiver: Theta_hist"),
    ("17", W + "STAGE8_RANK1_CTP_PRODUCER_ALGEBRA_Q52_SPEC_V001.md", "the law side: P0-P7"),
    ("18", W + "STAGE8_PRIMITIVE_INVENTORY_CORPUS_WIDE_EXHAUSTIVENESS_AUDIT_V001.md", "row 2 corroboration"),
    ("19", S + "PROGRAM_STATE_BRIEF_V005.md", "state pin"),
    ("20", S + "LOCKED_PROCESS.md", "process law"),
    ("21", S + "DECLINE_REGISTER_V002.md", "S01-S37"),
    ("22", W + "STAGE8_DESC_P0_EXECUTION_DARIO_V001.md", "1040 - CARRIAGE ONLY; NO SPAN DRAWN (self-citation bar)"),
    ("23", W + "STAGE8_DESC_P0_EXECUTION_CHECK_CODEX2_V001.md", "the check of record: the factorization correction"),
    ("24", W + "build_q92c_execution_pins_v001.py", "this generator; declared inputs are exactly members 01-24"),
]

SELF_CITATION_BARRED = {"22"}

# (tag, member, start, end, pin, note)
FIXED = [
    ("F01", "04", 37985, 38148, "93028d928dc7c62e4e01115cb55fbe855087603ef6f07fad648e4d7f54f1600b", "the six-row gate: Q-92(c) blocks construction"),
    ("F02", "04", 44072, 44269, "f04749a556ba8949c91a3dfbccfd786bada0bca0144946ac94d093fbf408ebcc", "Obj_0 is the law/operator/dynamics object; Core_0 is NOT the carrier"),
    ("F03", "09", 18039, 18385, "21f25905bde423379ac63e59460417d13c12326bee49feb8e6216428c056a662", "THE PROVENANCE CEILING, read again at bytes for part (c)"),
    ("F04", "10", 291, 904, "95352c889006649b403176b1b056f6494893f89148424c7fc671dd6890a2a936", "the seven ratified adoptions"),
    ("F05", "10", 1993, 2227, "fc1a4e4ab26f0824aca508e084d43e1c3bc50a9b11365b9480ca5e0e8206650e", "TYPE-P | premises: DoR-008; d_C0's provenance NOT DISCHARGED"),
    ("F06", "07", 35009, 38619, "e37571dbfe1767e6be39aa7fd1809f64abf68b4f2d74f538391cf3fbe1776d41", "ROW 3's NEGATIVE: the actual joint GENERATIVE P0 unconstructed"),
    ("F07", "11", 16880, 17121, "dd01923b", "THE OPEN FORCING SLOT: a future derivation is NOT excluded"),
    ("F08", "15", 10436, 11034, "b9c7a355890def386696ac4a075b1da79420d2b03e1f0d026e83983b5e18566d", "A_C0's factor typing and i_B"),
    ("F09", "16", 5034, 6439, "fe8ccfb88beefeba13f1ec5b2f9fb8e9ef130501cf7426524445c9b5e70d0a72", "Theta_hist's typing at the sealed receiver"),
    ("F10", "17", 8085, 8283, "375dd96a7b7c3806c063075f7346685efa8fbd8c1eddab9bbb19c5e723157d6d", "P0 and P1, the demand's own words"),
]

# (tag, member, start_anchor, end_anchor, note)
ANCHOR = [
    ("A01", "04", "### 8.5 Missing preconstruction inputs", "constructor can run.",
     "THE EIGHT WOULD-BUILD CLAUSES grouping into the six rows, PLUS the record's own head-of-order sentence"),
    ("A02", "04", "| Q-92(c) prerequisite | Current status | Evidence |", "| Separately isolated validation package",
     "THE SIX ROWS as member 04 tables them"),
    ("A03", "05", "PhysicalSig_0 :=", "derive and freeze one justified physical category and every field above from",
     "ROW 1 AT SCHEMA DEPTH: nine named fields, and 'No entry is assigned a physical value here'"),
    ("A04", "05", "Consequently an object in an exact physical category cannot be selected from", "deciding evidence: selected exact PhysicalSig_0",
     "ROW 1's PHYSICAL HOLE, in the later artifact's own words"),
    ("A05", "05", "1. one selected exact physical category and internal operation signature;", "Those are later-instance requirements.",
     "THE DEPENDENCY ORDER, PHASE A: the four signature-freeze prerequisites, and what the freeze does NOT need"),
    ("A06", "05", "After `ExactSig_0` exists, constructing an instance additionally needs:", "separately blocks the instance.",
     "THE DEPENDENCY ORDER, PHASE B: the eight instance-gate requirements"),
    ("A07", "05", "all_seven_port_contracts_schematically_well_typed = NO_VERDICT", "or a joint incompatibility proof",
     "ROW 5: the port contracts are PROPOSED, their well-typedness NO_VERDICT"),
    ("A08", "05", "full roster can run.\n\n```text\nQ98_static_countermodel_suite_attempted_against_ExactSig_0", "hostile fixtures exist |",
     "ROW 6: the oracle roster exists; NO fixtures and NO instantiated owners do"),
    ("A09", "06", "The inventory is too thin to build anything of `Obj_0`'s kind.", "exhaustive premise universe",
     "ROW 2's DEDICATED RESULT, and its blocker: row 1 is a SEPARATE missing input"),
    ("A10", "03", "**THE RECEIVER READING GOVERNS.**", "per the demand map's\nconditions.",
     "THE GOVERNING READING, from the decision of record this relay is guarded on"),
    ("A11", "08", "That span records the actual joint generative P0 as unconstructed", "change those types.",
     "the both-lane hunt's own statement of ROW 3's negative"),
]


def die(code, msg):
    sys.stderr.write("GENERATOR REFUSAL %s: %s\nNOTHING EMITTED.\n" % (code, msg))
    sys.exit(1)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    blob, digest = {}, {}
    for num, rel, _ in MEMBERS:
        p = os.path.join(ROOT, rel)
        try:
            with open(p, "rb") as fh:
                blob[num] = fh.read()
        except OSError as e:
            die("R1", "member %s unreadable at %s (%s)" % (num, rel, e))
        digest[num] = sha(blob[num])

    path_of = {num: rel for num, rel, _ in MEMBERS}
    rows, fixed_ok, pin8 = [], 0, 0

    for tag, num, a, b, pin, note in FIXED:
        if num in SELF_CITATION_BARRED:
            die("R5", "%s draws a span from barred member %s" % (tag, num))
        if len(pin) not in (8, 64) or any(c not in "0123456789abcdef" for c in pin):
            die("R2", "%s pin is neither full 64-hex nor an 8-hex upstream truncation: %r" % (tag, pin))
        d = blob[num]
        if not (0 <= a < b <= len(d)):
            die("R2", "%s interval [%d,%d) out of range for member %s" % (tag, a, b, num))
        h = sha(d[a:b])
        if not h.startswith(pin):
            die("R2", "%s FIXED pin mismatch in member %s [%d,%d)\n"
                      "        upstream pin %s\n        recomputed   %s" % (tag, num, a, b, pin, h))
        fixed_ok += 1
        shape = "FIXED" if len(pin) == 64 else "FIXED-PIN8"
        if len(pin) == 8:
            pin8 += 1
        rows.append((tag, shape, num, a, b, h, note))

    for tag, num, sa, ea, note in ANCHOR:
        if num in SELF_CITATION_BARRED:
            die("R5", "%s draws a span from barred member %s" % (tag, num))
        d = blob[num]
        sb, eb = sa.encode(), ea.encode()
        n = d.count(sb)
        if n == 0:
            die("R3", "%s start anchor ABSENT in member %s: %r" % (tag, num, sa[:60]))
        if n > 1:
            die("R3", "%s start anchor AMBIGUOUS (%d occurrences) in member %s: %r" % (tag, n, num, sa[:60]))
        a = d.find(sb)
        if d.count(eb, a) == 0:
            die("R4", "%s end anchor ABSENT at/after start in member %s: %r" % (tag, num, ea[:60]))
        b = d.find(eb, a) + len(eb)
        rows.append((tag, "ANCHOR", num, a, b, sha(d[a:b]), note))

    out = ["MEMBER TABLE -- rehashed at full archive-root paths at run time", "",
           "| # | Closed member | SHA-256 | Role |", "|---:|---|---|---|"]
    for num, rel, role in MEMBERS:
        out.append("| %s | `%s` | `%s` | %s |" % (num, rel, digest[num], role))
    out += ["", "SPAN TABLE -- CLOSURE_MEMBER_CITATION_RULE_V001 tuples", "",
            "| tag | shape | canonical path | source SHA-256 | [a,b) | span SHA-256 | role |",
            "|---|---|---|---|---|---|---|"]
    for tag, shape, num, a, b, h, note in rows:
        out.append("| %s | %s | `%s` | `%s` | `[%d,%d)` | `%s` | %s |"
                   % (tag, shape, path_of[num], digest[num], a, b, h, note))
    out += ["", "FILES=%d SPANS=%d FIXED-REVERIFIED=%d/%d MATCH (of which PIN8=%d, full-width=%d) ANCHORS=%d"
            % (len(MEMBERS), len(rows), fixed_ok, len(FIXED), pin8, fixed_ok - pin8, len(ANCHOR)),
            "SELF_CITATION_BAR: member(s) %s closed for carriage only; 0 span rows name them."
            % ", ".join(sorted(SELF_CITATION_BARRED))]
    print("\n".join(out))


if __name__ == "__main__":
    main()
