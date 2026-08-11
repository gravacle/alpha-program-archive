#!/usr/bin/env python3
"""
build_b03_v003_pins_v001.py  --  pin generator for STAGE8_DESC_B03_DARIO_V003.md

LANE: DARIO.  RELAY 1034.  [PLAN:DESC-26].

DECLARED INPUTS (Q-920/Q-924): exactly the members in MEMBERS below, each named by its
FULL path from the alpha-program-archive root (Q-913 PATH_RULE) and rehashed at that path
at run time.  This generator reads nothing else.  It writes nothing but its own stdout.

REFUSAL DISCIPLINE (Q-920/Q-924): the generator emits NO table if any of the following
holds.  It refuses rather than degrades; it never reports a span it cannot ground.
  R1  a declared member is unreadable at its declared path;
  R2  a FIXED span's recomputed digest does not equal the upstream pin it re-verifies;
  R3  an ANCHOR span's start anchor is absent, or occurs more than once (AMBIGUOUS);
  R4  an ANCHOR span's end anchor is absent at or after the start anchor.

SPAN CONVENTIONS, DECLARED (Q-927/Q-931/Q-935) -- offsets are byte offsets into the raw
file bytes, half-open [a,b), no decoding, no newline normalisation:
  FIXED   a literal [a,b) carried from an upstream pin.  The generator recomputes the
          span digest from the member's bytes and compares it to the upstream value.
          A mismatch is a REFUSAL, never a correction.
  ANCHOR  a byte interval fixed by a UNIQUE start anchor, running through the last byte
          of a named end anchor.  Uniqueness of the start anchor is tested over the whole
          member; a second occurrence is a REFUSAL.

NO OUTPUT INSPECTION: this generator computes digests over sealed record bytes only.
It reads no downstream object and no consumer, and nothing it emits is conditioned on
what any later stage would need the answer to be.

BLIND HELD: no physical quantity is read, formed, evaluated or compared.  Every scale
symbolic.  No member bound.  No fixed point executed.
"""

import hashlib
import os
import sys

ARCHIVE_ROOT = "/Users/bgm/MB Work/alpha-program-archive"

# ---------------------------------------------------------------- declared inputs
# id -> (archive-root-relative path, role)
MEMBERS = {
    "01": ("relay_inbox/RELAY_PASTE_1034_L3_DERIVATION_DARIO_V001.md", "the assignment"),
    "02": ("relay_inbox/RELAY_PASTE_1033_FRESH_SESSION_BOOTSTRAP_DARIO_V004.md", "the bootstrap; the SYMBOLIC LINE"),
    "03": ("workspace/STAGE8_DESC_B03_DARIO_V002.md", "V002, superseded append-only, byte-untouched"),
    "04": ("workspace/STAGE8_DESC_B03_V002_CHECK_CODEX2_V001.md", "the TWO-OBJECTS ruling of record"),
    "05": ("workspace/STAGE8_DESC_B03_DARIO_V001.md", "V001, still byte-untouched"),
    "06": ("workspace/STAGE8_DESC_DIAG_B_CODEX2_V001.md", "arm B"),
    "07": ("workspace/STAGE8_DESC_DIAG_B_CHECK_DARIO_V001.md", "arm B cross-check"),
    "08": ("workspace/STAGE8_DESC_DIAG_A_DARIO_V001.md", "arm A; the consumer ledger and its member table"),
    "09": ("workspace/STAGE8_RANK1_CTP_PRODUCER_ALGEBRA_Q52_SPEC_V001.md", "THE DEMAND: P0-P7, and the named obstruction"),
    "10": ("workspace/STAGE8_CTP_PHYS_INPUT_PACKAGE_U2_DOR008_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md", "v004's rho_pre clause at its span"),
    "11": ("workspace/STAGE8_AXN_STATE_ALGEBRA_MAP_CODEX2_V001.md", "the A_C0 typing, res_B, and the K4 handoff"),
    "12": ("workspace/STAGE8_AXN_ENTRY_CANDIDATE_SURVEY_DARIO_V001.md", "the three i_src declarations and their codomain"),
    "13": ("workspace/STAGE8_AXN_ENTRY_DECISION_INSTRUMENT_CODEX2_V002.md", "THE REQUIREMENT SPAN: joint i_src EMPTY"),
    "14": ("workspace/STAGE8_AXN_STAGE_RULE_CONSTRUCTION_CODEX2_V002.md", "A_F = C*(Lambda); the A_C0 limit"),
    "15": ("workspace/STAGE8_FIELD_CTP_CARRIER_AND_C0_JOIN_INSTANTIATION_ATTEMPT_V001.md", "THE PRIOR LEG-1 ATTEMPT and its stop"),
    "16": ("workspace/STAGE8_OBJ0_EXACT_SIGNATURE_DOMAIN_CODOMAIN_SPEC_AND_BUILD_STOP_V001.md", "the port signatures; the P1 domain-predicate TYPE-S"),
    "17": ("workspace/STAGE8_CROSSING_PRODUCER_POSE_AND_GLUING_VERDICT_EINSTEIN_V001.md", "S05's source: the tensor product refused by name"),
    "18": ("workspace/MEMBER12_HEADER_OVERLAY_RECORD_V002.md", "the overlay of record; the read rule"),
    "19": ("supervision/DECISION_OF_RECORD_013_GEN_OMEGA_RATIFIED_FAMILY_LEVEL_2026-08-02_V001.md", "the ratification, by digest"),
    "20": ("workspace/STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V003.md", "the forced d_state.  READ ONLY, with 18 and 19"),
    "21": ("workspace/STAGE8_AXN_LIVE_FAMILIES_CODEX2_V001.md", "P_src's carrier"),
    "22": ("workspace/STAGE8_DESC_DEMAND_DARIO_V008.md", "the demand map, CLOSED at V008"),
    "23": ("workspace/STAGE8_DESC_AUDIT_CODEX2_V002.md", "the supply map"),
    "24": ("supervision/PROGRAM_STATE_BRIEF_V005.md", "state pin"),
    "25": ("supervision/LOCKED_PROCESS.md", "process law"),
    "26": ("supervision/DECLINE_REGISTER_V002.md", "S01-S37"),
    "27": ("supervision/DECISION_OF_RECORD_008_FIELD_CTP_ADOPTION_RATIFIED_WITH_FALSIFIER_2026-08-01_V001.md", "DoR-008: THE FIELD/CTP PRESENTATION RATIFIED AS PREMISES, WITH A STANDING FALSIFIER"),
    "28": ("workspace/STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md", "the seven adoptions DoR-008 ratifies"),
    "29": ("workspace/build_b03_v003_pins_v001.py", "this generator; declared inputs are exactly members 01-29"),
}

# ------------------------------------------------------------------- span table
# (label, member id, shape, spec, upstream_pin_or_None, note)
#   FIXED  spec = (a, b)                 upstream pin REQUIRED
#   ANCHOR spec = (start_bytes, end_bytes)
SPANS = [
    # ---- FIXED: upstream pins this relay re-verifies rather than re-derives
    ("F01", "09", "FIXED", (8085, 8283),
     "375dd96a7b7c3806c063075f7346685efa8fbd8c1eddab9bbb19c5e723157d6d",
     "P1 -- the completed carrier A_SRF_CTP and its common dense domain"),
    ("F02", "09", "FIXED", (8954, 9569),
     "8917c67f455bb0b152950c1931891311c3c96029c1ba4100219370038198dbb0",
     "P5 -- rho_pre ON THE COMPLETED OBJECT"),
    ("F03", "10", "FIXED", (7290, 7829),
     "f9fb7a84ce4e3b954e5444baedc6703d9cc8ec52fe04f41e1b3b6d915b3d5372",
     "v004: the FULL source-record-field Hilbert space; the completed Hilbert space is ABSENT"),
    ("F04", "11", "FIXED", (10436, 11034),
     "b9c7a355890def386696ac4a075b1da79420d2b03e1f0d026e83983b5e18566d",
     "the A_C0 typing: A_SR, B := A_F_CTP iso C(Y), i_R, i_B"),
    ("F05", "11", "FIXED", (14039, 14411),
     "438e92aecb461348646cdb13c4faec51fa445b68aeee0bf5d11717078a869341",
     "res_B : State(A_C0) -> State(B)"),
    ("F06", "12", "FIXED", (7028, 7663),
     "43f3129a8b5059caa7979ab9ab0274296ec49c0cbd995c1785ab66d087af764d",
     "all three i_src declarations land in A_SRF_CTP; identification, not transcription"),
    ("F07", "13", "FIXED", (10322, 10545),
     "602ab0bff8d0d3d442271fe0850a6141f15fc1f139acb5b0311f13f63eaa26ff",
     "THE REQUIREMENT: joint i_src EMPTY -- author the carrier identification and typed embedding"),
    ("F08", "11", "FIXED", (21194, 21565),
     "e76be5c6f0536f2573c79f5d02a46e94f497cac5e87b744613ccf9c0636d011d",
     "K4 requires an ACTUAL omega_hist; omega_hist = Omega_C0 compose i_B -- LOCUS CORRECTED, see V003 section 6"),
    ("F09", "17", "FIXED", (6905, 8106),
     "e7a873cd5e3026d362b545e2297ec70b75697ecf62a1f629a71e6cf2ad83111f",
     "S05: the tensor product is CO-LOCATION and is refused as the field/CTP extension"),
    ("F10", "19", "FIXED", (355, 992),
     "bc83e53db7e46f27b570b1492ebd9ea53f168c344e1b06d1b82b45bb36a00750",
     "DoR-013's adoption clause, family level, no-member clause carried"),
    ("F11", "20", "FIXED", (22842, 24541),
     "84a5b7050188448e2a0cc526de0131b297cb734bc96b292968e1e37080b61cf0",
     "d_state := the unique normalized fixed state of P_src (CONTAINS overlay pin #7 -- carried whole)"),
    ("F12", "20", "FIXED", (22882, 22958),
     "65dfdedb8e8dc7a513904f4443ab215c08aa9d6c59d5a42ae75eb1395ede0662",
     "overlay pin #7 -- the stale status surface inside F11.  STALE, NOT GOVERNING"),
    ("F13", "21", "FIXED", (16571, 16744),
     "155721b5ad376b6fb6fc15387603ba4b92d69e9da98ceb882b7d0a2a4fc08df9",
     "P_src is a channel on the authored finite scalar SOURCE carrier"),

    # ---- ANCHOR: this relay's own new grounds
    ("A01", "09", "ANCHOR",
     (b"What is `NOT_SPECIFIED`", b"producer construction."), None,
     "no sealed text gives the extension to the full source-record-field CTP object, in ANY class"),
    ("A02", "15", "ANCHOR",
     (b"It does not fix the algebra generated by the compact connection", b"those objects."), None,
     "LEG 1's pre-algebra: the record does not fix it"),
    ("A03", "15", "ANCHOR",
     (b"The sealed stack provides the compact `U(1)` field label", b"unit-character connection"), None,
     "no generator set and no relation set for a field algebra; no completion norm"),
    ("A04", "15", "ANCHOR",
     (b"ITEM_4_COMMON_DENSE_DOMAIN_INSTANTIATED", b"common-domain certificate"), None,
     "P1's common dense domain: not instantiated"),
    ("A05", "16", "ANCHOR",
     (b"no definition of its equivalence predicate", b"qualifying_definition_file_list: EMPTY"), None,
     "P1's `equivalent domain object` predicate has NO definition anywhere in the packet"),
    ("A06", "16", "ANCHOR",
     (b"RecordEmbeddingPackage_3(o,c1,S_3) :=", b"base_tensor_carrier_compatibility_witness(i_rec,S_3)"), None,
     "i_rec exists as a PROPOSED PORT SIGNATURE, not as sealed instantiated content"),
    ("A07", "14", "ANCHOR",
     (b"Lambda = direct-sum", b"A_C0 = A_SR graded-tensor_min A_F_CTP."), None,
     "A_C0's third factor is A_F_CTP built from A_F = C*(Lambda), the LABEL algebra"),
    ("A08", "11", "ANCHOR",
     (b"Their ranges commute", b"dynamical-independence theorem."), None,
     "the only sealed commutation statement -- inside A_C0, and a kinematic premise only"),
    ("A09", "27", "ANCHOR",
     (b"The seven adoptions of", b"Honest count: SEVEN."), None,
     "DoR-008 RATIFIES the presentation AS DECLARED PREMISES -- including the completion and the common domain"),
    ("A10", "27", "ANCHOR",
     (b"Everything built on this presentation is TYPE-P", b"under these marks."), None,
     "the mark that propagates: TYPE-P | premises: DoR-008.  C0_prop AVAILABLE FOR USE under it"),
    ("A11", "15", "ANCHOR",
     (b"4. The adoption cannot include state", b"C0's narrow interface."), None,
     "C0's NARROW INTERFACE: quotient and measure are barred from the adoption"),
    ("A12", "15", "ANCHOR",
     (b"future_derivation_can_select_the_field_CTP_presentation", b"\n        presentation"), None,
     "the record's own slot for a FORCING theorem: NO_VERDICT -- neither supplied nor excluded"),
    ("A13", "28", "ANCHOR",
     (b"This artifact is a proposal for another adversarial pass", b"ratifies it."), None,
     "the proposal's own build-bar, standing in its bytes: nothing may be built on it un-ratified"),
]


def refuse(code, detail):
    sys.stderr.write("GENERATOR REFUSAL [%s]: %s\n" % (code, detail))
    sys.stderr.write("NO TABLE EMITTED.\n")
    sys.exit(2)


def main():
    blobs = {}
    digests = {}
    for mid in sorted(MEMBERS):
        rel, _role = MEMBERS[mid]
        path = os.path.join(ARCHIVE_ROOT, rel)
        try:
            with open(path, "rb") as fh:
                data = fh.read()
        except OSError as exc:
            refuse("R1", "member %s unreadable at %s (%s)" % (mid, path, exc))
        blobs[mid] = data
        digests[mid] = hashlib.sha256(data).hexdigest()

    rows = []
    fixed_total = 0
    fixed_match = 0
    for label, mid, shape, spec, pin, note in SPANS:
        data = blobs[mid]
        if shape == "FIXED":
            a, b = spec
            if pin is None:
                refuse("R2", "%s is FIXED with no upstream pin" % label)
            if b > len(data):
                refuse("R2", "%s span [%d,%d) exceeds member %s (%d bytes)" % (label, a, b, mid, len(data)))
            got = hashlib.sha256(data[a:b]).hexdigest()
            fixed_total += 1
            if got != pin:
                refuse("R2", "%s member %s [%d,%d) recomputed %s but upstream pin is %s"
                       % (label, mid, a, b, got, pin))
            fixed_match += 1
        elif shape == "ANCHOR":
            start, end = spec
            i = data.find(start)
            if i < 0:
                refuse("R3", "%s start anchor absent in member %s" % (label, mid))
            if data.find(start, i + 1) >= 0:
                refuse("R3", "%s start anchor AMBIGUOUS in member %s (>=2 occurrences)" % (label, mid))
            j = data.find(end, i)
            if j < 0:
                refuse("R4", "%s end anchor absent at or after start in member %s" % (label, mid))
            a, b = i, j + len(end)
            got = hashlib.sha256(data[a:b]).hexdigest()
        else:
            refuse("R3", "%s has unknown shape %s" % (label, shape))
        rows.append((label, mid, shape, a, b, b - a, got, note))

    out = []
    out.append("MEMBER DIGEST TABLE -- rehashed at full archive-root paths at run time")
    out.append("")
    for mid in sorted(MEMBERS):
        rel, role = MEMBERS[mid]
        out.append("| %s | `%s` | `%s` | %s |" % (mid, rel, digests[mid], role))
    out.append("")
    out.append("SPAN TABLE -- %d spans; %d FIXED; %d/%d FIXED MATCH"
               % (len(rows), fixed_total, fixed_match, fixed_total))
    out.append("")
    for label, mid, shape, a, b, ln, got, note in rows:
        out.append("| %s | member %s | `[%d,%d)` | %d | %s | `%s` | %s |"
                   % (label, mid, a, b, ln, shape, got, note))
    out.append("")
    out.append("FILES=%d  SPANS=%d  FIXED-REVERIFIED=%d/%d MATCH"
               % (len(MEMBERS), len(rows), fixed_match, fixed_total))
    print("\n".join(out))


if __name__ == "__main__":
    main()
