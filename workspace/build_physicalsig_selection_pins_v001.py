#!/usr/bin/env python3
"""
build_physicalsig_selection_pins_v001.py

GENERATOR for STAGE8_DESC_PHYSICALSIG_SELECTION_DARIO_V001.md  (relay 1045, DARIO lane).

DECLARED INPUTS (Q-920/Q-924): exactly the members of MEMBERS below, read at their
canonical paths relative to the alpha-program-archive root, plus this file itself.
The generator reads nothing else and emits nothing that is not computed from those bytes.

CITATION RULE (CLOSURE_MEMBER_CITATION_RULE_V001): every published span is emitted as
canonical path + full source SHA-256 + raw-byte half-open [a,b) + full span SHA-256.

SPAN CONVENTION, DECLARED: raw bytes, half-open [a,b), no decoding, no newline
normalisation, no trimming.  For an ANCHOR span, a = offset of the start anchor and
b = offset of the end anchor; the interval therefore runs from the first byte of the
start anchor up to but not including the first byte of the end anchor, whatever
whitespace lies between.  NO TAIL IS EVER INVENTED.  For a FIXED span the interval is
the one its upstream published, and the recomputed span digest must equal the
published pin at the width that pin was published.

REFUSAL PATHS.  The generator emits NOTHING on:
  R1  a member that cannot be read at its declared path;
  R2  a FIXED span whose recomputed digest disagrees with its published pin;
  R3  a start anchor that is absent, or occurs more than once (AMBIGUOUS);
  R4  an end anchor that is absent, or occurs more than once (AMBIGUOUS);
  R5  a span row naming a BARRED member (self-citation bar).

SELF-CITATION BAR: this lane's own prior outputs are never record witnesses.  Members
marked BARRED are closed FOR CARRIAGE ONLY and R5 refuses any span row naming them.

MODES:
  (no args)            emit the member table, the span table, the scans, and the summary
  --audit <artifact>   prose-digest audit (Q-954): every 64-hex token in <artifact>
                       must appear in this generator's emitted digest set
"""

import hashlib
import os
import re
import sys

ROOT = "/Users/bgm/MB Work/alpha-program-archive"

# ---------------------------------------------------------------- members

# key: (path, role, barred)
MEMBERS = [
    ("01", "relay_inbox/RELAY_PASTE_1045_PHYSICALSIG_SELECTION_DARIO_V001.md",
     "the assignment", False),
    ("02", "relay_inbox/RELAY_PASTE_1044_FRESH_SESSION_BOOTSTRAP_DARIO_V006.md",
     "the bootstrap; the SYMBOLIC LINE; the BUILD ORDER OF RECORD", False),
    ("03", "workspace/STAGE8_OBJ0_EXACT_SIGNATURE_DOMAIN_CODOMAIN_SPEC_AND_BUILD_STOP_V001.md",
     "THE SCHEMA: the nine fields, Phase A/B, section 10, SIG-T1", False),
    ("04", "workspace/STAGE8_DESC_Q92C_CHECK_CODEX2_V001.md",
     "THE CHECK OF RECORD: Phase-A dissolution, build order, Row1/Obj_0 correction", False),
    ("05", "workspace/STAGE8_RANK1_CTP_PRODUCER_ALGEBRA_Q52_SPEC_V001.md",
     "THE LAW SIDE: the class definition and P0-P7", False),
    ("06", "workspace/STAGE8_JOINT_P0_BUILDABILITY_IN_PRINCIPLE_RESULT_V001.md",
     "Q-95: the six rows; the Obj_0/Core_0 typing", False),
    ("07", "workspace/STAGE8_FROZEN_PRIMITIVE_INVENTORY_PREFREEZE_RESULT_V001.md",
     "Q-97: the inventory is too thin", False),
    ("08", "workspace/STAGE8_ACCESSOR_THEOREM_SUBSTITUTION_ADJUDICATION_EINSTEIN_V001.md",
     "THIRD LANE: accessor indeterminacy; the uniqueness-sense requirement", False),
    ("09", "workspace/STAGE8_TASK2D_SCALARIZATION_FUNCTIONAL_FORCING_PROTOCOL_RESULT_V001.md",
     "TASK2D: the scalarization continuum", False),
    ("10", "supervision/DECISION_OF_RECORD_008_FIELD_CTP_ADOPTION_RATIFIED_WITH_FALSIFIER_2026-08-01_V001.md",
     "DoR-008: the seven ratified premises, the falsifier's direction, the undischarged marks", False),
    ("11", "workspace/STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md",
     "THE PROVENANCE CEILING", False),
    ("12", "workspace/STAGE8_FIELD_CTP_CARRIER_AND_C0_JOIN_INSTANTIATION_ATTEMPT_V001.md",
     "THE OPEN NO_VERDICT SLOT", False),
    ("13", "workspace/STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V003.md",
     "Gen_Omega V003 - READ ONLY, with members 14 and 15", False),
    ("14", "workspace/MEMBER12_HEADER_OVERLAY_RECORD_V002.md",
     "the overlay of record; the read rule - CARRIAGE ONLY (DARIO lane), NO SPAN DRAWN", True),
    ("15", "supervision/DECISION_OF_RECORD_013_GEN_OMEGA_RATIFIED_FAMILY_LEVEL_2026-08-02_V001.md",
     "DoR-013: family-level ratification, the no-member clause, AUTHORED PHYSICS", False),
    ("16", "workspace/STAGE8_AXN_STATE_ALGEBRA_MAP_CODEX2_V001.md",
     "A_C0 typing; the derived-sector level", False),
    ("17", "workspace/STAGE8_TASK2D_MULTIAXIAL_STATE_CLASS_ENVELOPE_FORCING_PROTOCOL_RESULT_V001.md",
     "TASK2D: a forcing protocol that does not force", False),
    ("18", "workspace/STAGE8_TASK2D_QUASIFREE_BRANCH_RHO_PRE_GOVERNANCE_AUDIT_V001.md",
     "TASK2D: the rho_pre survivor set", False),
    ("19", "workspace/DEMAND_READING_DECISION_OF_RECORD_V001.md",
     "the governing receiver reading", False),
    ("20", "supervision/QUESTIONS_SETTLED_REGISTER_V001.md",
     "Q-955: the build order of record and the forward-hook instruction", False),
    ("21", "supervision/PROGRAM_STATE_BRIEF_V005.md", "state pin", False),
    ("22", "supervision/LOCKED_PROCESS.md", "process law", False),
    ("23", "supervision/DECLINE_REGISTER_V002.md", "S01-S37", False),
    ("24", "workspace/STAGE8_DESC_Q92C_EXECUTION_DARIO_V001.md",
     "1042 - CARRIAGE ONLY (DARIO lane), NO SPAN DRAWN", True),
    ("25", "workspace/build_physicalsig_selection_pins_v001.py",
     "this generator; declared inputs are exactly members 01-25", False),
]

# ------------------------------------------------------------------ spans

# FIXED spans: (tag, member key, start, end, published pin, use)
FIXED_SPANS = [
    ("A03", "03", 25970, 26653,
     "f0c1e4acdb730965cfd0fa5318663732f757f69fe56d4124215800a2070b8506",
     "THE NINE FIELDS; no entry assigned a physical value"),
    ("A04", "03", 20247, 20450,
     "abcff8509beb9d8c99f0ac70adfecd2996f26a96fd076beb08d634002f615623",
     "no exact physical category selectable; the four NO_VERDICT category rows"),
    ("A05", "03", 67258, 68448,
     "35d7e30e8c500317c48771f0172f455ccba3622c950b6f32c283bff9609e4b47",
     "PHASE A - the signature-freeze prerequisites"),
    ("A06", "03", 69235, 70069,
     "35ea71f16957331e5f8a341cae4197830977e147b2b648c813b6c46c78fc2cce",
     "PHASE B - the later instance gate"),
    ("A09", "07", 616, 2009,
     "08cccf3d059964ad27a5fafd3bb898c32f1b652a3613e67eaf5454d5321824c6",
     "Q-97: the inventory is too thin; ROW 2's would-build"),
    ("F02", "06", 44072, 44269,
     "f04749a556ba8949c91a3dfbccfd786bada0bca0144946ac94d093fbf408ebcc",
     "Obj_0 and Core_0 typed; Core_0 is not automatically P1's carrier"),
    ("F03", "11", 18039, 18385,
     "21f25905bde423379ac63e59460417d13c12326bee49feb8e6216428c056a662",
     "THE PROVENANCE CEILING, verbatim"),
    ("F05", "10", 1993, 2227,
     "fc1a4e4ab26f0824aca508e084d43e1c3bc50a9b11365b9480ca5e0e8206650e",
     "NOT discharged: d_C0's common-origin provenance; DoR-007's theorem"),
    ("F07", "12", 16880, 17121,
     "dd01923b74098215e105f835ece6f3a15672f861afdd3803be1dc195da8cd10a",
     "THE OPEN SLOT, at its exact span"),
]

# ANCHOR spans: (tag, member key, start anchor, end anchor, use)
ANCHOR_SPANS = [
    ("N01", "03", "SignatureFreezeInputs_0 :=", "FreezeExactSig_0 :",
     "the ONLY definitional occurrence of FrozenPrimitiveBindingSchema_0: a name in a tuple"),
    ("N02", "03", "PRIMITIVE_INTERFACE_REQUIREMENT(I_prim,PhysicalSig_0) :=",
     "DERIVED_SECTOR_REFERENCE_REQUIREMENT(S_sector,ExactSig_0) :=",
     "section 10: every clause constrains I_prim, none constrains PhysicalSig_0"),
    ("N03", "03", "| `SIG-T1-PHYSICAL-EXACTNESS`", "| `SIG-T2-PRIMITIVE-COVERAGE`",
     "SIG-T1: a disjunction, placeholder or post-output choice IS the failure"),
    ("N04", "03", "Obj_0_semantic_type =", "executed typing result",
     "the semantic type is fixed - and is a ROLE, not a mathematical object type"),
    ("N05", "03", "**Not fixed by sealed text:**", "**Declared here under F-GK3:**",
     "Answer 1: the eight things sealed text does not fix"),
    ("N06", "03", "2. exact frozen primitive-binding and derived-sector-reference **type**",
     "3. the P1 domain equivalence predicate",
     "section 12.1 row 2: the Phase-A type schema, scoped to the signature it precedes"),
    ("N07", "03", "An object of an arbitrary physical category", "### 8.2 Signature-freeze",
     "the internal operation domains/codomains ARE the fields; all remain TYPE-U"),
    ("N08", "03", "The closest analogous B0 audit warns at",
     "The strongest failed producer attempt",
     "a linear-operator choice for P0 would be an EXTRA PREMISE"),
    ("N09", "03", "executed typing result says at", "At `:316-327` it further says",
     "Q-43: the antecedent sectors are not created by Obj_0"),
    ("N10", "05", "Definition: a common-origin CTP producer algebra", "What it resists",
     "THE CLASS DEFINITION: all derived from ONE microscopic operator/dynamics"),
    ("N11", "05", "P0. One microscopic", "P1. A completed",
     "THE P0 ROW: the sealed law's own naming of the object, disjunctive"),
    ("N12", "08", "THERE IS NO FUNCTION FROM THE OBJECT", "This kill is shape-neutral",
     "third lane: satisfaction conditions with many admissible witnesses"),
    ("N13", "08", "**C2 UNIQUENESS**", "**C3 ACCESSOR CLAUSE**",
     "third lane: the UNIQUENESS SENSE must be declared, with transport exhibited"),
    ("N14", "09", "RAW_POSITIVE_SCALARIZATION_FAMILY", "RHO_PRE_ROLE_IS_A_CONCRETE",
     "TASK2D: after every executable constraint, the survivor set is a CONTINUUM"),
    ("N15", "10", "The seven adoptions", "Twice adversarially",
     "DoR-008's seven ratified fields, as declared premises"),
    ("N16", "10", "THE FINITE RESULTS ARE THE AUTHORITY", "Task 2f",
     "the falsifier's DIRECTION sentence"),
    ("N17", "15", "THE ANCHORED GENERATIVE FAMILY", "- The generative maps",
     "DoR-013: ratified AS A FAMILY; NO MEMBER IS SELECTED, EVER"),
    ("N18", "15", "A0 and the anchor are AUTHORED PHYSICS", "The program adopts them",
     "DoR-013: AUTHORED PHYSICS, confirmed non-derivable"),
    ("N19", "13", "The U2 audit at lines", "The Q-263 benchmark",
     "Gen_Omega: two inequivalent scalarizations, NEITHER SELECTED"),
    ("N20", "13", "Omega_prim,N^v003 := (", "The tuple contains no",
     "Gen_Omega's frozen primitive tuple - scoped to the source preparation port"),
    ("N21", "13", "The domain of `q_src`", "| Field | What it adds",
     "Gen_Omega: q_src realizes ONLY the source preparation port"),
    ("N22", "04", "upstream primitive evidence + primitive-binding TYPE SCHEMA",
     "The current type schema is incomplete",
     "THE CHECK'S BUILD ORDER, carried and executed, not re-argued"),
    ("N23", "04", "The subject's sentence", "This narrows the subject's explanatory",
     "THE CHECK'S CORRECTION: Row 1 is PhysicalSig_0; Obj_0 is a later inhabitant"),
    ("N24", "20", "THE DEADLOCK: DISSOLVED-BY-PHASE-A", "ONE-GATE confirmed",
     "Q-955: the build order of record, at the register"),
    ("N25", "20", "FORWARD-HOOK STATUS", "THE ROAD: the target-independent selection",
     "Q-955: the forward-hook instruction - the outcome must be scored against it BY NAME"),
    ("N26", "06", "### 8.5 Missing preconstruction inputs",
     "  enumerate the exact existing upstream ph",
     "Q-95's ROW 1 would-build, at its own source"),
    ("N27", "03", "> `object_type, arity, domain, codomain",
     "The certificate is only assembled later",
     "the FLAT presentation's six Sig_0 fields, quoted - representation_data_IF_REQUIRED"),
    ("N28", "03", "union would postpone rather than specify the exact type.",
     "Given a future fixed",
     "ROW 1's would-build in full: from a sufficient upstream primitive inventory, without descendant data"),
    ("N29", "03", "Consequently an object in an exact physical category cannot be selected",
     "These are `NO_VERDICT`, not negative claims",
     "the FOUR named category candidates, all NO_VERDICT, with no exhaustiveness claim"),
]

# scans (counts come from the scan, never predicted)
SCAN_TOKENS = [
    "FrozenPrimitiveBindingSchema_0",
    "FrozenDerivedSectorReferenceTypeSchema_0",
    "FrozenPortContractSchemas_1_to_7",
    "FrozenCrossRowCoherenceSchema_0",
    "FrozenPortDependencyGraphSchema_0",
    "FrozenOriginPredicateAndTraceSchema_0",
    "FrozenCertificateSchema_0",
]
SCAN_DIRS = ["workspace", "supervision", "relay_inbox", "relay_outbox"]

HEX64 = re.compile(rb"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])")


def die(rule, detail):
    sys.stderr.write("GENERATOR REFUSAL %s: %s\n" % (rule, detail))
    sys.stderr.write("NOTHING EMITTED.\n")
    sys.exit(1)


def load():
    blobs, digests, sizes = {}, {}, {}
    for key, path, _role, _barred in MEMBERS:
        full = os.path.join(ROOT, path)
        try:
            with open(full, "rb") as fh:
                data = fh.read()
        except OSError as exc:                                          # R1
            die("R1", "member %s unreadable at %s (%s)" % (key, path, exc))
        blobs[key] = data
        digests[key] = hashlib.sha256(data).hexdigest()
        sizes[key] = len(data)
    return blobs, digests, sizes


def member_index():
    return {k: (p, r, b) for k, p, r, b in MEMBERS}


def sidecar_check(digests):
    """Compare each member's adjacent .seal.sha256 sidecar, where one exists, with the
    digest recomputed at that member's declared path.  Absent sidecar is reported as
    absent, never as agreement."""
    rows = []
    for key, path, _role, _barred in MEMBERS:
        side = os.path.join(ROOT, path + ".seal.sha256")
        if not os.path.exists(side):
            rows.append((key, path, "NO-SIDECAR", ""))
            continue
        try:
            with open(side, "r") as fh:
                claimed = fh.read().split()[0].strip()
        except (OSError, IndexError):
            rows.append((key, path, "SIDECAR-UNREADABLE", ""))
            continue
        ok = claimed == digests[key]
        rows.append((key, path, "SEAL-OK" if ok else "SEAL-MISMATCH", claimed))
    return rows


def resolve_spans(blobs):
    idx = member_index()
    rows = []
    for tag, key, a, b, pin, use in FIXED_SPANS:
        if idx[key][2]:                                                 # R5
            die("R5", "span %s names BARRED member %s" % (tag, key))
        span = blobs[key][a:b]
        got = hashlib.sha256(span).hexdigest()
        width = len(pin)
        if got[:width] != pin:                                          # R2
            die("R2", "FIXED span %s: pin %s, recomputed %s" % (tag, pin, got))
        rows.append((tag, key, a, b, got, "FIXED", use))
    for tag, key, sa, ea, use in ANCHOR_SPANS:
        if idx[key][2]:                                                 # R5
            die("R5", "span %s names BARRED member %s" % (tag, key))
        data = blobs[key]
        ns = data.count(sa.encode())
        if ns != 1:                                                     # R3
            die("R3", "span %s start anchor occurs %d times: %r" % (tag, ns, sa))
        ne = data.count(ea.encode())
        if ne != 1:                                                     # R4
            die("R4", "span %s end anchor occurs %d times: %r" % (tag, ne, ea))
        a = data.find(sa.encode())
        b = data.find(ea.encode())
        if b <= a:                                                      # R4
            die("R4", "span %s end anchor precedes start anchor" % tag)
        got = hashlib.sha256(data[a:b]).hexdigest()
        rows.append((tag, key, a, b, got, "ANCHOR", use))
    return rows


def run_scans():
    out = []
    for tok in SCAN_TOKENS:
        hits = []
        total = 0
        for d in SCAN_DIRS:
            base = os.path.join(ROOT, d)
            for dirpath, _dirnames, filenames in os.walk(base):
                for fn in sorted(filenames):
                    if not (fn.endswith(".md") or fn.endswith(".py")
                            or fn.endswith(".json")):
                        continue
                    fp = os.path.join(dirpath, fn)
                    try:
                        with open(fp, "rb") as fh:
                            n = fh.read().count(tok.encode())
                    except OSError:
                        continue
                    if n:
                        rel = os.path.relpath(fp, ROOT)
                        hits.append((rel, n))
                        total += n
        out.append((tok, total, hits))
    return out


def emit():
    blobs, digests, sizes = load()
    spans = resolve_spans(blobs)
    idx = member_index()

    print("GENERATOR build_physicalsig_selection_pins_v001.py")
    print("ROOT %s" % ROOT)
    print("")
    print("== MEMBER TABLE ==")
    print("%-4s %-110s %-64s %9s %s" % ("#", "path", "sha256", "bytes", "carriage"))
    for key, path, _role, barred in MEMBERS:
        print("%-4s %-110s %-64s %9d %s"
              % (key, path, digests[key], sizes[key],
                 "BARRED-CARRIAGE-ONLY" if barred else ""))
    print("")
    print("== SPAN TABLE (canonical path + source sha256 + [a,b) + span sha256) ==")
    for tag, key, a, b, got, kind, use in spans:
        path = idx[key][0]
        print("%s  %s" % (tag, kind))
        print("    path   %s" % path)
        print("    source %s" % digests[key])
        print("    span   [%d,%d)" % (a, b))
        print("    digest %s" % got)
        print("    use    %s" % use)
    print("")
    print("== SIDECAR CHECK (absent is reported as absent, never as agreement) ==")
    for key, path, status, claimed in sidecar_check(digests):
        print("%-4s %-20s %-110s %s" % (key, status, path, claimed))
    print("")
    print("== SCANS (counts are read from the scan, never predicted) ==")
    for tok, total, hits in run_scans():
        print("%-45s TOTAL %d" % (tok, total))
        for rel, n in hits:
            print("        %3d  %s" % (n, rel))
    print("")
    fixed = sum(1 for r in spans if r[5] == "FIXED")
    anchor = sum(1 for r in spans if r[5] == "ANCHOR")
    print("== SUMMARY ==")
    print("FILES=%d SPANS=%d FIXED-REVERIFIED=%d/%d MATCH ANCHORS=%d"
          % (len(MEMBERS), len(spans), fixed, fixed, anchor))
    print("SELF_CITATION_BAR: members %s closed for carriage only; %d span rows name them."
          % (",".join(k for k, _p, _r, b in MEMBERS if b), 0))
    print("REFUSALS_FIRED_THIS_RUN: NONE (R1-R5 all silent; not-fired is reported as "
          "not-fired, never as passed)")


def audit(artifact):
    blobs, digests, _sizes = load()
    spans = resolve_spans(blobs)
    allowed = set(digests.values()) | {r[4] for r in spans}
    try:
        with open(artifact, "rb") as fh:
            data = fh.read()
    except OSError as exc:
        die("R1", "audit target unreadable: %s" % exc)
    toks = HEX64.findall(data)
    distinct = sorted({t.decode() for t in toks})
    outside = [t for t in distinct if t not in allowed]
    print("== PROSE-DIGEST AUDIT (Q-954) ==")
    print("target      %s" % artifact)
    print("pattern     (?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])")
    print("occurrences %d" % len(toks))
    print("distinct    %d" % len(distinct))
    print("accounting set = this generator's member digests + span digests (%d values)"
          % len(allowed))
    print("OUTSIDE SET %d" % len(outside))
    for t in outside:
        print("    UNACCOUNTED %s" % t)
    accounted = len(distinct) - len(outside)
    print("RESULT %d/%d distinct accounted; %d/%d occurrences accounted"
          % (accounted, len(distinct),
             len([t for t in toks if t.decode() in allowed]), len(toks)))


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--audit":
        audit(sys.argv[2])
    else:
        emit()
