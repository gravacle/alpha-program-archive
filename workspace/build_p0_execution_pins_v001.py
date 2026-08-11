#!/usr/bin/env python3
"""
build_p0_execution_pins_v001.py
PIN GENERATOR for STAGE8_DESC_P0_EXECUTION_DARIO_V001.md  (relay 1040, DARIO lane)

DECLARED INPUTS: exactly members 01-27 of the MEMBERS table below.  Nothing else is
opened, hashed, or consulted.  Every path is resolved from the alpha-program-archive
ROOT and rehashed at that path at run time (Q-913).

REFUSAL PATHS (Q-920/Q-924).  The generator emits NOTHING -- no member table, no span
table, no partial output -- if any of these fires:

  R1  a declared member is unreadable at its declared archive-root path.
  R2  a FIXED span's recomputed digest does not agree with the upstream pin it carries.
      A mismatch is a REFUSAL, never a correction.

      PIN-WIDTH CONVENTION, DECLARED RATHER THAN IMPROVISED.  Some upstream artifacts
      publish a span digest in full (64 hex) and some display it TRUNCATED (8 hex,
      written "abcd1234...").  A pin is carried HERE AT EXACTLY THE WIDTH THE UPSTREAM
      PUBLISHED IT, and agreement is prefix-agreement at that width.  A truncated pin
      is a weaker check than a full one and is labelled PIN8 in the emitted table so no
      consumer can mistake one for the other.  No tail is ever invented to make a
      truncated pin look full; that would be pinning from a description of bytes.
  R3  an ANCHOR span's start anchor is absent, or occurs more than once (AMBIGUOUS).
  R4  an ANCHOR span's end anchor is absent, or does not occur at/after the start.

  R5  SELF-CITATION BAR: a span row names a DARIO-lane artifact of relay 1034 or 1037
      (members 23, 24).  Those members are closed FOR CARRIAGE ONLY.  The bar is
      enforced here by construction, not by the author's discipline.

SPAN CONVENTION: raw bytes, half-open [a,b), no decoding, no newline normalisation.
  FIXED  = a literal [a,b) carried from an upstream pin and re-verified.
  ANCHOR = a UNIQUE start anchor running through the LAST byte of a named end anchor.

CITATION RULE: CLOSURE_MEMBER_CITATION_RULE_V001 -- every emitted span row carries
canonical path + full source SHA-256 + half-open interval + full span SHA-256, so no
consumer needs to rebind a closure-local member number.
"""

import hashlib
import os
import sys

ROOT = "/Users/bgm/MB Work/alpha-program-archive"

W = "workspace/"
S = "supervision/"
R = "relay_inbox/"

# ---------------------------------------------------------------- members
# (number, path-from-archive-root, role)
MEMBERS = [
    ("01", R + "RELAY_PASTE_1040_PIPELINE_EXECUTION_DARIO_V001.md", "the assignment"),
    ("02", R + "RELAY_PASTE_1039_FRESH_SESSION_BOOTSTRAP_DARIO_V005.md", "the bootstrap; the SYMBOLIC LINE"),
    ("03", W + "STAGE8_RANK1_CTP_PRODUCER_ALGEBRA_Q52_SPEC_V001.md", "THE LAW SIDE: P0-P7"),
    ("04", W + "STAGE8_JOINT_P0_BUILDABILITY_IN_PRINCIPLE_RESULT_V001.md", "THE JOINT P0 CONTRACT and its six preconstruction rows"),
    ("05", S + "DECISION_OF_RECORD_008_FIELD_CTP_ADOPTION_RATIFIED_WITH_FALSIFIER_2026-08-01_V001.md", "DoR-008: the ratified premises and the Q-212 void trigger"),
    ("06", W + "STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md", "THE SEVEN ADOPTIONS DoR-008 RATIFIES; the provenance ceiling"),
    ("07", W + "STAGE8_AXN_S1_MEMBER_ATTEMPT_CODEX2_V001.md", "THE SEALED S1 RECEIVER: Theta_hist's typing and K7"),
    ("08", W + "STAGE8_AXN_STATE_ALGEBRA_MAP_CODEX2_V001.md", "carrier typing, i_B, res_B, the K4 handoff"),
    ("09", W + "STAGE8_OBJ0_EXACT_SIGNATURE_DOMAIN_CODOMAIN_SPEC_AND_BUILD_STOP_V001.md", "port signatures and the sealed execution order"),
    ("10", W + "STAGE8_TASK2D_SCALARIZATION_FUNCTIONAL_FORCING_PROTOCOL_RESULT_V001.md", "B iso C(Y), forced record-side FROM member 06"),
    ("11", W + "STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V003.md", "the three descent maps. READ ONLY, with 12 and 13"),
    ("12", W + "MEMBER12_HEADER_OVERLAY_RECORD_V002.md", "the overlay of record; the read rule"),
    ("13", S + "DECISION_OF_RECORD_013_GEN_OMEGA_RATIFIED_FAMILY_LEVEL_2026-08-02_V001.md", "the ratification, by digest"),
    ("14", W + "STAGE8_DESC_DIAG_A_DARIO_V001.md", "Arm A: the d_C0/d_Ui prefix and the C0/U1 state-term reading"),
    ("15", W + "STAGE8_AXN_LIVE_FAMILIES_CODEX2_V001.md", "P_src's carrier; THE CODOMAIN CENSUS AT State(A_C0)"),
    ("16", W + "STAGE8_CTP_PHYS_INPUT_PACKAGE_U2_DOR008_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md", "v004's rho_pre clause"),
    ("17", W + "STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_SUBSTITUTE_ADMISSIBILITY_ADJUDICATION_V001.md", "L5: the d_U2 descent-witness signature"),
    ("18", W + "STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md", "L4: the U2 role content"),
    ("19", W + "STAGE8_AXN_ENTRY_DECISION_INSTRUMENT_CODEX2_V002.md", "the entry instrument (frame-fallen; carried, not consumed as demand)"),
    ("20", S + "PROGRAM_STATE_BRIEF_V005.md", "state pin"),
    ("21", S + "LOCKED_PROCESS.md", "process law"),
    ("22", S + "DECLINE_REGISTER_V002.md", "S01-S37"),
    ("23", W + "STAGE8_DESC_B03_DARIO_V003.md", "1034 derivation - CARRIAGE ONLY; NO SPAN DRAWN (self-citation bar)"),
    ("24", W + "STAGE8_DESC_ARROW_NECESSITY_DARIO_V001.md", "1037 arrow necessity - CARRIAGE ONLY; NO SPAN DRAWN (self-citation bar)"),
    ("25", W + "STAGE8_DESC_B03_V003_CHECK_CODEX2_V001.md", "the check of record: STOPS-CONFIRMED; the citation rule"),
    ("26", W + "STAGE8_DESC_ARROW_NECESSITY_CHECK_CODEX2_V001.md", "the check of record: the Theta_hist widening"),
    ("27", W + "build_p0_execution_pins_v001.py", "this generator; declared inputs are exactly members 01-27"),
]

SELF_CITATION_BARRED = {"23", "24"}

# ---------------------------------------------------------------- spans
# FIXED: (tag, member, start, end, upstream_pin, note)
FIXED = [
    ("F01", "03", 8085, 8283, "375dd96a7b7c3806c063075f7346685efa8fbd8c1eddab9bbb19c5e723157d6d", "P0 and P1, the demand's own carrier"),
    ("F02", "03", 8954, 9569, "8917c67f455bb0b152950c1931891311c3c96029c1ba4100219370038198dbb0", "P5/P6/P7: rho_pre on the completed object, same microscopic source"),
    ("F03", "03", 18296, 18480, "cf696d88abeacea1019aa129c6b686e7d0e21027d5e8f854c5b7fda0e9adced7", "REFUTATION CONDITION 4 - the law side's only C0"),
    ("F04", "16", 7290, 7829, "f9fb7a84", "v004's rho_pre clause"),
    ("F05", "08", 10436, 11034, "b9c7a355890def386696ac4a075b1da79420d2b03e1f0d026e83983b5e18566d", "A_SR / B := A_F_CTP iso C(Y) / A_C0; i_R and i_B"),
    ("F06", "08", 11419, 11482, "5efbab19d594957daf88b9c27b0342e5bc3f2d5bc191d4aee4e3563843042348", "State(B) iso Prob_reg_Borel(Y) - K4's receiver"),
    ("F07", "08", 14039, 14411, "438e92ae", "res_B EXACT; and its input missing"),
    ("F08", "08", 21194, 21565, "e76be5c6f0536f2573c79f5d02a46e94f497cac5e87b744613ccf9c0636d011d", "the K4 handoff: omega_hist = Omega_C0 compose i_B"),
    ("F09", "09", 37255, 37521, "a5900fd81fb9040b370f39a59fc7314b2302dbbd9ce5c3b1cac93cc3fafd1ffb", "THE PORT ORDER: P2 after P5, consuming c5.rho_pre"),
    ("F10", "09", 38867, 39276, "56a575d104416d75ef19aa289eee9639c3650135f429cf1fbabccf1c068902c0", "i_rec : RecordSector[S_3] -> c1.A_SRF_CTP"),
    ("F11", "07", 5034, 6439, "fe8ccfb88beefeba13f1ec5b2f9fb8e9ef130501cf7426524445c9b5e70d0a72", "THETA_HIST'S TYPING, and the continuum family F_1"),
    ("F12", "07", 14105, 14810, "f9907d3337701df3f2e713dd08eda9d3be135446c0bfb81a9f2d8a8ab7aeadb8", "K7: direction-bearing descent; controls fail provenance"),
    ("F13", "10", 6743, 7035, "e0497a680c590abf5ab7987534de68a2e85561bc6abfb77afad22339922374ac", "B iso C(Y) FORCED FROM MEMBER 06's OWN FIELDS"),
    ("F14", "05", 1993, 2227, "fc1a4e4ab26f0824aca508e084d43e1c3bc50a9b11365b9480ca5e0e8206650e", "TYPE-P | premises: DoR-008, propagating downstream"),
    ("F15", "04", 14772, 15078, "3955ef7041cf28d2525f98e748456983c4893f3e191cc620e8f91c6876c87736", "R4 CONSUMES the state/evolution/effect rather than constructing their joint origin"),
    ("F16", "04", 33735, 34103, "c5257697adf761f3a919232b6ee0d0ae06ea9ffe64fcbdf60a94cde0041acc6c", "the exact missing object is AN OBLIGATION, NOT A CONSTRUCTOR"),
    ("F17", "15", 16571, 16744, "155721b5", "P_src's carrier; DoR-013's d_state solves its invariant state"),
    # NOTE ON F18's LOCUS.  Arm A (member 14) cites this span as "member 09 at [38121,38437)",
    # meaning member 09 OF ARM A'S OWN CLOSURE -- which resolves to member 18 HERE, the B0
    # load-bearing stop spec.  A first draft of this generator assigned it to member 14 and R2
    # REFUSED it.  That refusal was not a test: it happened, and it is the same closure-local
    # numbering hazard the 1034 derivation documented at its section 6.  The span is re-pinned at
    # its true file rather than corrected into agreement.
    ("F18", "18", 38121, 38437, "cb264602a0537a07948c31d2763094395c5670a5001ea8378d9e7f83b67ed72c", "d_C0 : B0_candidate -> C0 ; d_Ui : (B0_candidate,C0) -> Ui"),
    ("F19", "17", 6266, 6883, "e6093b0f48c11d3f05d3c6fd3692b6ea2c4b320746bb92eebe72ef28ed697efe", "L5: U2 role content and d_U2's C0-naming domain"),
    ("F20", "19", 10322, 10545, "602ab0bff8d0d3d442271fe0850a6141f15fc1f139acb5b0311f13f63eaa26ff", "the fallen identification clause - carried as FRAME, not as demand"),
]

# ANCHOR: (tag, member, start_anchor, end_anchor, note)
ANCHOR = [
    ("A01", "05", "The seven adoptions of", "Honest count: SEVEN.",
     "WHAT THE ASSEMBLY CONSUMES: the seven ratified adoptions, named"),
    ("A02", "05", "*** THE COMPLETED FRAMEWORK MUST REPRODUCE", "NEVER THE REVERSE. ***",
     "THE Q-212 VOID TRIGGER, carried with the premises"),
    ("A03", "05", "## SCOPE AND MARKS", "C0_prop is now AVAILABLE FOR USE under these marks.",
     "the marks: TYPE-P, and d_C0's common-origin provenance NOT discharged"),
    ("A04", "06", "A_F := C*(Lambda).", "no scalar functional or\nmeasure on that spectrum is a field of C0.",
     "THE FIELD ALGEBRA and ITS EXPORT CEILING, in the ratified premises' own bytes"),
    ("A05", "06", "A_F_CTP := A_F,+ tensor_min (A_F,-)^op.", "those remain U1.",
     "the CTP completion - the history sector of the assembly"),
    ("A06", "06", "A_C0 := A_SR graded-tensor_min A_F_CTP.", "a product physical CTP functional.",
     "THE JOIN the assembly produces, and what it does NOT assert"),
    ("A07", "06", "D_C0 := E_C0.", "scalar Hilbert-space\nrealizations.",
     "THE COMMON DOMAIN, and its explicit refusal of a scalar realization"),
    ("A08", "06", "This proposal declares the field/CTP algebraic presentation as premises at",
     "scalar physical Hilbert space.",
     "THE PROVENANCE CEILING: 'It claims no common origin for the source, record, and field sectors'"),
    ("A09", "11", "d_state(Omega_prim,N^v003)\n  := the unique", "d_state(Omega_prim,N^v003)=I_src/Tr_A(I_src).",
     "d_state, at its own bytes"),
    ("A10", "11", "d_ready(Omega_prim,N^v003)\n  :=C |r>", "There is no orientation coordinate and no exchanged member.",
     "d_ready, at its own bytes"),
    ("A11", "11", "d_law(Omega_prim,N^v003;a)", "No law coefficient or\nattachment was changed.",
     "d_law, at its own bytes"),
    ("A12", "15", "None has codomain `State(A_C0)`.", "`A_src -> A_src tensor R_inf tensor B`.",
     "THE CODOMAIN CENSUS - the record's own statement of the Step-2 hole"),
    ("A13", "15", "instantiated on the finite source carrier, not a positive",
     "not a positive normalized functional on all `A_C0`",
     "the finite scalar/source functional is NOT a state on all of A_C0"),
    ("A14", "08", "No sealed star-homomorphism has source `R_inf`", "does not land in\nthe range of `i_B`.",
     "no arrow between the record factor and the history factor"),
    ("A15", "08", "E_out := omega_out tensor id_B", "which imports exactly the member being sought.",
     "THE SLICE ROUTE, closed: it returns the observable, not a scalar"),
    ("A16", "04", "ConstructP0:\n  P0_CONSTRUCTION_INPUTS", "CommonOriginCertificate_0\n  )",
     "THE JOINT P0 CONTRACT: what ConstructP0 consumes and produces"),
    ("A17", "04", "`Obj_0` is the actual joint source-record-field law/operator/dynamics object.",
     "not automatically P1's completed carrier.",
     "Obj_0 IS THE LAW/OPERATOR/DYNAMICS OBJECT; Core_0 is not the carrier"),
    ("A18", "04", "At least the six mandatory preconstruction rows are not complete.",
     "This is a construction constraint, not physical\ncontent.",
     "the six rows: Q-92(c) blocks construction"),
    ("A19", "09", "CarrierPackage_1 :=", "canonical_carrier_domain_accessors)",
     "P1's port codomain - the carrier package c1"),
    ("A20", "09", "StateEffectPackage_5(o,c1,c3,c4;family_kind_5) :=", "ExactFrozenNonexhaustiveCriterionWitness(I_5))",
     "P5's port codomain - what the pre-state production must return"),
    ("A21", "09", "SourceEmbeddingPackage_2(o,c1,c5,S_2) :=", "c5.rho_pre,i_src,S_2)\n  )",
     "P2'S TEST SHAPE - exactly what i_src would verify"),
    ("A22", "09", "  Sigma(c2 : P2Structure(...,c5.rho_pre,...)).", "  Sigma(q : CrossRowCoherence_0(c1,...,c7)).",
     "the sealed dependent execution order, P5 before completed P2"),
    ("A23", "14", "C0  NO STATE TERM.", "the state (section 3.4)",
     "ARM A's READING: C0 and U1 carry NO STATE TERM"),
    ("A24", "03", "P0. One microscopic source-record-field", "B0-like source.",
     "P0, the demand's own words for the object Step 1 must assemble"),
]


def die(code, msg):
    sys.stderr.write("GENERATOR REFUSAL %s: %s\nNOTHING EMITTED.\n" % (code, msg))
    sys.exit(1)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    # ---- R1: read and hash every declared member at its archive-root path
    blob = {}
    digest = {}
    for num, rel, _role in MEMBERS:
        p = os.path.join(ROOT, rel)
        try:
            with open(p, "rb") as fh:
                blob[num] = fh.read()
        except OSError as e:
            die("R1", "member %s unreadable at %s (%s)" % (num, rel, e))
        digest[num] = sha(blob[num])

    path_of = {num: rel for num, rel, _ in MEMBERS}
    rows = []

    # ---- R2: FIXED spans re-verify their upstream pins at the width the upstream published
    fixed_ok = 0
    pin8 = 0
    for tag, num, a, b, pin, note in FIXED:
        if num in SELF_CITATION_BARRED:
            die("R5", "%s draws a span from barred member %s" % (tag, num))
        if len(pin) not in (8, 64) or any(c not in "0123456789abcdef" for c in pin):
            die("R2", "%s pin is neither a full 64-hex digest nor an 8-hex upstream truncation: %r"
                % (tag, pin))
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

    # ---- R3/R4: ANCHOR spans
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
        m = d.count(eb, a)
        if m == 0:
            die("R4", "%s end anchor ABSENT at/after start in member %s: %r" % (tag, num, ea[:60]))
        b = d.find(eb, a) + len(eb)
        rows.append((tag, "ANCHOR", num, a, b, sha(d[a:b]), note))

    # ---- emit
    out = []
    out.append("MEMBER TABLE -- rehashed at full archive-root paths at run time")
    out.append("")
    out.append("| # | Closed member | SHA-256 | Role |")
    out.append("|---:|---|---|---|")
    for num, rel, role in MEMBERS:
        out.append("| %s | `%s` | `%s` | %s |" % (num, rel, digest[num], role))
    out.append("")
    out.append("SPAN TABLE -- CLOSURE_MEMBER_CITATION_RULE_V001 tuples")
    out.append("")
    out.append("| tag | shape | canonical path | source SHA-256 | [a,b) | span SHA-256 | role |")
    out.append("|---|---|---|---|---|---|---|")
    for tag, shape, num, a, b, h, note in rows:
        out.append("| %s | %s | `%s` | `%s` | `[%d,%d)` | `%s` | %s |"
                   % (tag, shape, path_of[num], digest[num], a, b, h, note))
    out.append("")
    out.append("FILES=%d SPANS=%d FIXED-REVERIFIED=%d/%d MATCH (of which PIN8=%d, full-width=%d) ANCHORS=%d"
               % (len(MEMBERS), len(rows), fixed_ok, len(FIXED), pin8, fixed_ok - pin8, len(ANCHOR)))
    out.append("SELF_CITATION_BAR: members %s closed for carriage only; 0 span rows name them."
               % ", ".join(sorted(SELF_CITATION_BARRED)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
