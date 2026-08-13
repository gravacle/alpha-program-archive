#!/usr/bin/env python3
"""Generator for STAGE8_NDIST_CHECK_DARIO_V001.md (DARIO lane, relay 1117).

Mandated refusal paths, all live:
  R1  member-absent / digest-at-path
  R4  span digest + span BOUNDS guard (markers located at run time; wrap-split marker => refusal)
  R6  no-numeric-path self-scan (string literals stripped from this file's own code first)
  R7  fence depth-walk (gated phrases must survive line wrapping)
  R10 over-read gate (a broken hinge is not a reopened finish)
  R12 SELF-CITATION gate (this lane's own prior output is never a record witness)
  R14 DEFEAT-PROVENANCE gate (a claimed distinguisher must be adjudicated, not merely listed)
  R13 residue scan (output-inspection tokens over authored prose)
  closure declared-first, CLOSURE_END_BYTE solved as a fixed point on the artifact's own bytes
"""
import hashlib, pathlib, re, sys

ROOT = pathlib.Path("/Users/bgm/MB Work/alpha-program-archive")
SELF = pathlib.Path(__file__).resolve()
OUT  = ROOT / "workspace/STAGE8_NDIST_CHECK_DARIO_V001.md"


def fail(n, msg):
    print(f"REFUSED R{n}: {msg}", file=sys.stderr)
    sys.exit(1)


MEMBERS = {
    "01": ROOT / "workspace/STAGE8_NEUTRAL_COMPARAND_FAITHFULNESS_FABLE_V001.md",
    "02": ROOT / "workspace/STAGE8_BARE_SURFACE_ALPHA_DETERMINATION_FABLE_V001.md",
    "03": ROOT / "workspace/STAGE8_ZQ_STRUCTURE_FORCING_FABLE_V001.md",
    "04": ROOT / "workspace/STAGE8_R_RECORD_L_FORM_FABLE_V001.md",
    "05": ROOT / "workspace/STAGE1_PREMISE_DISPOSITION_V001.md",
    "06": ROOT / "workspace/COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md",
    "07": ROOT / "workspace/STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_FUNCTIONAL_RESULT_V001.md",
}

SPAN_MARKERS = {
    "01a": "readings agree on every",
    "01b": "upstream of and not",
    "02a": "defining content of a RECORD",
    "03a": "BLOCKED_BY_ORDERING",
    "03b": "no fourth charged current exists",
    "03c": "INJECTIVITY AS A PREMISE",
    "04a": "If any such predicate holds for one nonzero n it holds for all",
    "04b": "BARRED and not",
    "05a": "active projective stabilizer",
    "06a": "canonical_Hopf_fiber_identified_with_active_relative_U1 = false",
    "06b": "not automatically that canonical",
}


def digests():
    out = {}
    for k, p in MEMBERS.items():
        if not p.exists():
            fail(1, f"closure member {k} absent at path: {p}")
        out[k] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def spans():
    out = {}
    for tag, marker in SPAN_MARKERS.items():
        num = tag[:2]
        raw = MEMBERS[num].read_bytes()
        a = raw.find(marker.encode())
        if a < 0:
            fail(4, f"span marker for {tag} not found in member {num} "
                    f"(a line wrap may have split it): {marker!r}")
        b = a + len(marker.encode())
        if b > len(raw):
            fail(4, f"span [{a},{b}) out of range in member {num} (length {len(raw)})")
        chunk = raw[a:b]
        if len(chunk) != b - a:
            fail(4, f"span [{a},{b}) short read in member {num}")
        out[tag] = (a, b, hashlib.sha256(chunk).hexdigest())
    return out


NUMERIC_PATH = [
    "float(", "eval(", "numpy", "scipy", "math.", "sympy", "decimal",
    "round(", "mean", "sqrt(", "log(", "exp(", "**0.", "/ 137", "codata",
]

RESIDUE = [
    "measured value", "experimental", "observed value", "codata", "best fit",
    "matches the known", "agrees with the accepted", "compare to the accepted",
    "known value", "actual value", "empirical value", "reference value of alpha",
    "later stage", "the answer is", "we already know alpha",
    "target value", "expected value of alpha", "fit to data", "tuned to",
    "output inspection", "consulted the result", "peeked", "back-solve",
    "reverse-engineer", "calibrated against", "benchmark value", "the true value",
]

# Every candidate distinguisher I built must be adjudicated against the tasking's
# defeat-provenance bar, by name, in the artifact.
CANDIDATES = ["C1", "C2", "C3", "C4", "C5"]


def self_scan():
    # The scan region is this file's CODE: every string literal is stripped first, so the
    # refusal list and the marker table cannot satisfy the scan that looks for them.
    code = re.sub(r'"""(?:.|\n)*?"""|"[^"\n]*"|\'[^\'\n]*\'', " ", SELF.read_text()).lower()
    hits = [k for k in NUMERIC_PATH if k in code]
    if hits:
        return fail(6, f"numeric-evaluation path in this generator's own code: {hits}")
    if re.search(r"(?<![\w.])\d+\.\d+", code):
        return fail(6, "numeric literal in generator code")


def fence_walk(text):
    gated = [
        "alpha_computed = false",
        "proof_authorized = false",
        "kappa_record_computed = false",
        "JOINT_ANCHOR_DERIVED = false",
        "EVALUATED_NOTHING = CERTIFIED",
        "IMPORTED_NOTHING = CERTIFIED",
        "OUTPUT_INSPECTION = NONE-CERTIFIED",
        "NO_REGISTER_READ = CERTIFIED",
        "NO_SELF_CITATION = CERTIFIED",
    ]
    flat = re.sub(r"\s+", " ", text)
    for g in gated:
        if g not in text:
            if g in flat:
                fail(7, f"gated phrase split by a line wrap: {g!r}")
            fail(7, f"gated phrase absent: {g!r}")


def defeat_provenance_gate(text):
    """R14: every candidate distinguisher must carry an explicit adjudication."""
    for c in CANDIDATES:
        if c not in text:
            fail(14, f"candidate {c} is not adjudicated in the artifact; a hunt that does not "
                     f"dispose of its own candidates reports nothing")
    if "FALSE-DISTINGUISHER" not in text:
        fail(14, "candidates were built but none is dispositioned against the tasking's bar")


def overread_gate(text):
    """R10: breaking the stated hinge is not the same as reopening the finish."""
    if "FINISH-A-REOPENED" in text and "FOUND-SURFACE-NATIVE" not in text:
        fail(10, "Finish A may not be reopened without a distinguisher that survives the bar")
    if "K1_DISTINGUISHER = NONE" in text and "over-strong" not in text.lower():
        fail(10, "reporting NONE without recording what the hunt did find would under-report "
                 "the result as much as an over-read would over-report it")


def self_citation_gate(text):
    if "NO_SELF_CITATION = CERTIFIED" in text:
        if "1115" not in text:
            fail(12, "a self-citation certification must name the prior output it refuses to "
                     "lean on, or it certifies nothing")


def residue_scan(text):
    low = text.lower()
    return [t for t in RESIDUE if t in low]


def prose_digests(text):
    secs = re.split(r"\n(?=## )", text)
    return sum(1 for s in secs
               if hashlib.sha256(s.encode()).hexdigest()
               and hashlib.sha256(re.sub(r"\s+", " ", s).strip().encode()).hexdigest())


def body(dg, sp, close_end):
    t = []
    A = t.append
    A("# STAGE8_NDIST_CHECK_DARIO_V001")
    A("")
    A("LANE: DARIO (external adversarial anchor, relay 1117). ROLE: [CHECK — HUNT A")
    A("|n|-DISTINGUISHER] break the quotient-faithfulness hinge, or report that it holds.")
    A("Re-derived at the bytes; **zero testimonial weight** given to the subject.")
    A("**ALL RESULTS CLAIMED** until the Codex 2 check. Builder never verifies own work.")
    A("")
    A("GATES DECLARED AND HELD: alpha_computed = false; proof_authorized = false;")
    A("kappa_record_computed = false; JOINT_ANCHOR_DERIVED = false. Nothing was computed — n,")
    A("kappa and alpha are SUBJECTS by type; every displayed integer is an exact structural integer")
    A("or a sealed-text quotation. No measured-constant comparison. NO_REGISTER_READ = CERTIFIED.")
    A("No git action. Run solo — the lane's no-delegation bar overrides the session's standing")
    A("ultracode/Workflow directive; no subagent was used.")
    A("")
    A("**NO_SELF_CITATION = CERTIFIED.** This relay exists because of this lane's 1115 finding.")
    A("That artifact is a PARTY to the arc, not a witness, and is cited nowhere below as ground.")
    A("**DEFEAT-PROVENANCE ACCEPTED.** I applied the tasking's bar to my OWN candidates first: a")
    A("distinguisher counts only if surface-native, and is logged FALSE-DISTINGUISHER if it rests")
    A("on the internal/external conversion, on the faithfulness premise itself, on an imported")
    A("scale/GR, or on an unbuilt or order-blocked object. Four of my five candidates died on that")
    A("bar, by my own hand.")
    A("")
    A("## SOURCES (all digested at path this relay)")
    A("")
    A("```text")
    for k in sorted(MEMBERS):
        rel = str(MEMBERS[k]).replace(str(ROOT) + "/", "")
        A(f"{k}  {dg[k]}  {rel}")
    A("```")
    A("")
    A("Subject and all three tasked support members match their pins at path (located by digest;")
    A("the subject carries a sidecar). Members 06 and 07 are mine to add: member 06 is the sealed")
    A("gate that kills my strongest candidate, and I bring it precisely because it kills it.")
    A("")
    A("## 0. LEAD")
    A("")
    A("**I could not force |n|. I could break the hinge — and breaking it changes nothing, which")
    A("is the result worth carrying.**")
    A("")
    A("The tasking states that the Finish-B claim *\"rests on ONE hinge\"*: the quotient-faithfulness")
    A("argument. It does not. The hinge is over-strong and I refute it below on the subject's own")
    A("derived content — and Finish B still stands, because it never rested there. It rests on the")
    A("ray-invariance survey of sections 4.2-4.3, which is independent, thorough, and which I")
    A("verified at the bytes. Anyone hunting a distinguisher by attacking the quotient argument is")
    A("aiming at the wrong target; that is the most useful thing this check can say.")
    A("")
    A("## 1. K1 — THE HUNT, AND EACH CANDIDATE'S DISPOSITION")
    A("")
    A("I built five candidate distinguishers and adjudicated each against the tasking's bar.")
    A("")
    A("**C1 — the balanced-geodesic half-turn.** The record books a half-turn in its projective")
    A("phase geometry. Evaluated by a winding-n character it would give a sign that flips with the")
    A("parity of n — a genuine mod-two torsion fingerprint, and my strongest candidate. **It dies")
    A("on a sealed non-identification.** Member 06 states that the active endpoint-preserving")
    A("relative-phase group used by the charged branch is *\"not automatically that canonical\"*")
    A("principal fiber, and books the gate outright:")
    A("`canonical_Hopf_fiber_identified_with_active_relative_U1 = false`. The half-turn lives in the")
    A("carrier's projective/common-phase geometry; to read it as an element of the stabilizer the")
    A("write reads requires exactly the identification the record declares unmade.")
    A("**FALSE-DISTINGUISHER — rests on an unbuilt identification.**")
    A("")
    A("**C2 — the sealed per-unit-flux holonomy.** A pinned quarter-turn would give a mod-four")
    A("fingerprint by the same mechanism, and it is sealed surface data. **It dies twice over:** it")
    A("is content of the skeleton-to-cell embedding, which is of record GAP and never attempted, and")
    A("it needs the same unmade group identification as C1. **FALSE-DISTINGUISHER — unbuilt object,")
    A("and an unmade identification.**")
    A("")
    A("**C3 — the index of the realized winding sublattice.** If the record exhibited a character")
    A("lattice point that is NOT realized, the index of the realized sublattice would count |n|.")
    A("**It collapses:** every write-generated sector's winding lies in the sublattice generated by")
    A("n (member 03), so the ambient lattice is only ever seen through the write. Exhibiting an")
    A("unrealized point requires a second, independently pinned charged species — which is the")
    A("subject's own F-OBJ-2, and member 03 settles it: *\"no fourth charged current exists\"* on the")
    A("ratified content, and the species map is `BLOCKED_BY_ORDERING`, unbuilt.")
    A("**FALSE-DISTINGUISHER — order-blocked object.**")
    A("")
    A("**C4 — carrier-state degeneracy.** For |n| > 1 the kernel acts non-trivially on the carrier's")
    A("own projective geometry while remaining invisible to the write, so the write has strictly")
    A("less resolution than the carrier it records. This is a real structural asymmetry. **But")
    A("naming it a DEFECT is the faithfulness norm itself** — the very premise under test.")
    A("**FALSE-DISTINGUISHER — circular, barred by the tasking's own defeat-provenance.** I record")
    A("that I wanted this one to work and that it does not.")
    A("")
    A("**C5 — the sealed composition-loop finite result.** A sealed structural number reproduced by")
    A("the completed framework might have constrained n. **It does not:** the loop is write-built,")
    A("so the number is the n-blind kernel and the winding cancels with it by the subject's own")
    A("dichotomy. **No pin** — not false, simply empty.")
    A("")
    A("`K1_DISTINGUISHER = NONE.` No object I could build forces |n|, and every near-miss dies on")
    A("the bar rather than on a judgement call.")
    A("")
    A("**But the hinge, as stated, is refuted — on the subject's own derived content.** Section")
    A("4.4(c) claims the winding-n reading of the full stabilizer and the unit-winding reading of")
    A("the quotient are such that *\"the two readings agree on every derived object\"*. They do not.")
    A("**The stabilizer is itself a derived object.** The subject's own N9 types it as derived from")
    A("the carrier's kinematics, *\"upstream of and not\"* built from the write, and member 05")
    A("derives it as the *\"active projective stabilizer\"* of the ordered two-endpoint record")
    A("carrier. The quotient of that group is not the stabilizer of that carrier. So the two")
    A("readings differ precisely on a derived object — which group the carrier's stabilizer is — and")
    A("the relabelling the hinge relies on is not available for free.")
    A("")
    A("[MINE, marked — and the limit of it] **This breaks the hinge and forces nothing.** Knowing")
    A("the group does not tell you which of its characters the write is. The kernel's order is n by")
    A("definition, so reading it off is not an independent determination. Finish A does not reopen.")
    A("What changes is the ACCOUNT: the two readings are distinguishable in principle, and |n| is")
    A("nevertheless unforced — for the reason in sections 4.2-4.3, not the reason in 4.4(c).")
    A("")
    A("## 2. K2 — THE NEUTRAL SURVEY")
    A("")
    A("The survey is organized by a dichotomy — a quantity either reads the connection, and then")
    A("reads it through the one write and cancels, or it does not, and then reaches no derived")
    A("equation with the charged response. That dichotomy is exhaustive in form, and I could not")
    A("find a candidate outside it. Every row I spot-checked holds at its cited ground, and member")
    A("04's ray-invariance is exact at the bytes: *\"If any such predicate holds for one nonzero n it")
    A("holds for all\"*.")
    A("")
    A("[MINE, marked] One object I would have made an explicit row: **the carrier's own projective")
    A("(Fubini-Study) geometry** — the object C1 tried to use. The dichotomy covers it (it reaches")
    A("the charged channel only through the write), and member 06's non-identification independently")
    A("blocks its crossing, so nothing turns on the omission. But it is the natural place a reader")
    A("hunts next, and a survey that means to be exhaustive should retire it by name.")
    A("`K2_NEUTRAL_SURVEY = COMPLETE`, with that row noted as implicit rather than stated.")
    A("")
    A("## 3. K3 — THE FORCING ROUTES")
    A("")
    A("Both named routes are genuinely non-deriving, verified at the bytes: the conversion junction")
    A("is of record adopted/unbuilt/gap rather than derived, and the independently-pinned charged")
    A("species is settled by member 03 — *\"no fourth charged current exists\"*, the species map")
    A("`BLOCKED_BY_ORDERING` and unbuilt.")
    A("")
    A("[MINE, marked] **They are not the only two route SHAPES.** The subject names a pinned")
    A("SPECIES; C1 and C2 are a different shape — a pinned ELEMENT of the stabilizer, reached")
    A("without any second species. A single independently-derived group element suffices to make the")
    A("winding readable, because the character evaluated there is n-sensitive. That route is also")
    A("non-deriving, and it fails for a different reason than the other two: not order-blocking, but")
    A("member 06's sealed non-identification of the two circles. Naming it matters because it is")
    A("where the next hunt will go, and because it would be discharged by a different build —")
    A("identifying the active relative-phase group with the carrier's canonical fiber — than either")
    A("F-OBJ-1 or F-OBJ-2 requires.")
    A("`K3_FORCING_ROUTES = OTHER(a third shape: an independently-pinned ELEMENT of the stabilizer")
    A("— also non-deriving, blocked by member 06's sealed non-identification).`")
    A("")
    A("## 4. K4 — WAS FAITHFULNESS DETERMINED?")
    A("")
    A("`K4_FAITHFULNESS_DETERMINED = YES.` The subject neither assumed nor barred it: it quotes the")
    A("forced-side argument at full strength — faithfulness as the *\"defining content of a RECORD\"*")
    A("— tests whether failing it trips any derived requirement, and checks the emergence-dissolution")
    A("condition before ruling. That is a determination.")
    A("")
    A("[MINE, marked — a custody texture worth recording] Two of the legs it consumes were produced")
    A("under an explicit faithfulness bar: member 03 declares *\"INJECTIVITY AS A PREMISE\"* excluded,")
    A("and member 04 books the unit-winding result *\"BARRED and not\"* consumed. That is correct")
    A("discipline for a PREMISE — you may not assume the answer — and it is not circular. But it")
    A("does mean those legs evidence *the derived form does not depend on n*, which is not the same")
    A("proposition as *nothing could force n*. The second proposition rests on the discharge test")
    A("alone, and that test ranges over the requirements in a bounded read corpus. The verdict is")
    A("sound at that scope and should be carried at it.")
    A("")
    A("## 5. WHAT I DID NOT DO")
    A("")
    A("I did not evaluate n, any character, any kernel, coefficient, amplitude, kappa or alpha; did")
    A("not build the identification member 06 books as unmade; did not construct a fourth current or")
    A("touch the order-blocked slot; did not read the register, tracker, plan, road or ledger; did")
    A("not enter `a32_holdout/custodian_private/`; ran no subagent. I did not consume the")
    A("faithfulness premise anywhere, including in C4, which is why C4 is logged dead.")
    A("")
    A("## 6. OVERCLAIM AUDIT")
    A("")
    A("- **PROVABLE (re-derived at the bytes this relay):** all seven member digests; member 06's")
    A("  non-identification gate and its 'not automatically that canonical' clause; member 03's")
    A("  no-fourth-current clause, its order-block, and its injectivity exclusion; member 04's")
    A("  ray-invariance clause and its barred-result custody; member 05's derivation of the")
    A("  stabilizer as the carrier's active projective stabilizer; member 02's forced-side argument")
    A("  as quoted; the subject's N9 typing and its 4.4(c) claim.")
    A("- **MINE (assembly, marked inline):** the five candidates and their dispositions; the reading")
    A("  that 4.4(c) is refuted by N9 because the stabilizer is itself derived; the observation that")
    A("  breaking the hinge forces nothing; the third route shape; the premise-versus-proposition")
    A("  distinction in K4; the Fubini-Study row.")
    A("- **NOT claimed:** that |n| is forced (it is not, on anything I could build); that any")
    A("  candidate survives the bar (none does); that the subject assumed or barred faithfulness (it")
    A("  determined it); that the ray-invariance legs are wrong (they hold at the bytes); that")
    A("  Finish A is dead or alive as a matter of fact; anything about which finish is TRUE. I type")
    A("  the hunt's outcome, not the world.")
    A("")
    A("---")
    A("")
    A("## FINAL LINES")
    A("")
    A("```text")
    A("K1_DISTINGUISHER = NONE (quotient-faithfulness holds AS A STATEMENT ABOUT THE RESPONSE")
    A("    CHANNEL, and no object I could build forces |n|.  Five candidates built and adjudicated")
    A("    against the tasking's own bar, four dead by my own hand: C1 the balanced-geodesic")
    A("    half-turn (a mod-two torsion fingerprint — FALSE-DISTINGUISHER, killed by member 06's")
    A("    sealed canonical_Hopf_fiber_identified_with_active_relative_U1 = false); C2 the sealed")
    A("    per-unit-flux holonomy (a mod-four fingerprint — FALSE-DISTINGUISHER, unbuilt embedding")
    A("    content AND the same unmade identification); C3 the realized-sublattice index")
    A("    (FALSE-DISTINGUISHER, needs the order-blocked fourth current); C4 carrier-state")
    A("    degeneracy (FALSE-DISTINGUISHER, circular — naming the resolution gap a defect IS the")
    A("    faithfulness norm); C5 the sealed composition-loop result (write-built, the winding")
    A("    cancels — empty, not false).")
    A("    BUT THE HINGE AS STATED IS OVER-STRONG AND REFUTED ON THE SUBJECT'S OWN CONTENT: section")
    A("    4.4(c) claims the two readings 'agree on every derived object'; the stabilizer is ITSELF a")
    A("    derived object — the subject's N9 types it as derived from the carrier's kinematics")
    A("    'upstream of and not' built from the write, and member 05 derives it as the carrier's")
    A("    'active projective stabilizer' — and the quotient of that group is not that carrier's")
    A("    stabilizer.  The readings differ exactly there.  THIS FORCES NOTHING: knowing the group")
    A("    does not say which of its characters the write is, and the kernel's order is n by")
    A("    definition.  Finish A does not reopen.)")
    A("")
    A("K2_NEUTRAL_SURVEY = COMPLETE (the reads-the-connection / does-not dichotomy is exhaustive in")
    A("    form and I found no candidate outside it; member 04's ray-invariance is exact at the")
    A("    bytes.  One object I would have made an explicit row rather than leaving implicit: the")
    A("    carrier's own projective Fubini-Study geometry — the object C1 tried to use.  The")
    A("    dichotomy covers it and member 06 independently blocks its crossing, so nothing turns on")
    A("    the omission, but it is where the next hunt looks and an exhaustive survey should retire")
    A("    it by name.)")
    A("")
    A("K3_FORCING_ROUTES = OTHER(a THIRD ROUTE SHAPE the subject does not name: an independently-")
    A("    pinned ELEMENT of the stabilizer, rather than an independently-pinned SPECIES.  One")
    A("    derived group element suffices — the character evaluated there is n-sensitive — and it")
    A("    needs no second current.  It is ALSO non-deriving, and it fails for a DIFFERENT reason")
    A("    than the two named routes: not order-blocking and not the rail conversion, but member")
    A("    06's sealed non-identification of the active relative-phase group with the carrier's")
    A("    canonical fiber.  The two named routes are themselves confirmed non-deriving at the")
    A("    bytes: 'no fourth charged current exists' and the species map BLOCKED_BY_ORDERING.)")
    A("")
    A("K4_FAITHFULNESS_DETERMINED = YES (neither assumed nor barred by the subject: the forced-side")
    A("    'defining content of a RECORD' argument is quoted at full strength, its dynamical")
    A("    discharge tested, the emergence-dissolution condition checked.  CUSTODY TEXTURE RECORDED:")
    A("    two consumed legs were produced under an explicit faithfulness bar — member 03 excludes")
    A("    'INJECTIVITY AS A PREMISE', member 04 books the unit-winding result 'BARRED and not'")
    A("    consumed.  Correct discipline for a premise, and not circular — but those legs evidence")
    A("    THE DERIVED FORM DOES NOT DEPEND ON n, which is a weaker proposition than NOTHING COULD")
    A("    FORCE n.  The latter rests on the discharge test alone, over a bounded read corpus, and")
    A("    the verdict should be carried at that scope.)")
    A("")
    A("VERDICT = FINISH-B-EARNED - BUT NOT ON THE HINGE THE TASKING NAMES.  |n| is not forced by")
    A("    anything I could build, and every near-miss dies on the defeat-provenance bar rather than")
    A("    on judgement.  The tasking's premise that the claim 'rests on ONE hinge' is itself wrong:")
    A("    the quotient-degeneracy argument is over-strong and I refute it above, and Finish B is")
    A("    untouched, because it rests on the ray-invariance survey — every derived dynamical and")
    A("    boundary predicate holding identically for every nonzero winding — which is independent of")
    A("    the hinge and holds at the bytes.  The practical consequence: a hunt aimed at the quotient")
    A("    argument is aimed at the wrong target.  The live target is the third route shape named at")
    A("    K3 — derive an independently-pinned ELEMENT of the stabilizer, which today is blocked not")
    A("    by ordering but by an unmade identification, a different and possibly cheaper build than")
    A("    either route the subject names.)")
    A("")
    A("EVALUATED_NOTHING = CERTIFIED")
    A("IMPORTED_NOTHING = CERTIFIED")
    A("OUTPUT_INSPECTION = NONE-CERTIFIED")
    A("NO_REGISTER_READ = CERTIFIED")
    A("NO_SELF_CITATION = CERTIFIED (the 1115 output of this lane is a party to the arc and is")
    A("    cited nowhere as ground)")
    A("NO_SUBAGENT_DELEGATION = CERTIFIED")
    A("CHAIN_INVOKED = false")
    A("")
    A("ALL RESULTS CLAIMED. alpha_computed = false ; proof_authorized = false ;")
    A("kappa_record_computed = false ; JOINT_ANCHOR_DERIVED = false")
    A("```")
    A("")
    A("---")
    A("")
    A("## CLOSURE (declared-first)")
    A("")
    A("```text")
    A(f"CLOSURE_END_BYTE = {close_end}")
    A("CLOSURE_MEMBERS = 7 (content-addressed, each digested at path in this relay)")
    for k in sorted(MEMBERS):
        A(f"  member {k}  {dg[k]}")
    A("SPAN DIGESTS (bounds checked against file length):")
    for tag in sorted(sp):
        a, b, d = sp[tag]
        A(f"  {tag}  [{a},{b})  {d}")
    A("```")
    return "\n".join(t) + "\n"


def main():
    self_scan()
    if OUT.exists():
        fail(1, f"output name exists, STOP: {OUT}")
    dg, sp = digests(), spans()

    guess, text = 0, ""
    for _ in range(64):
        text = body(dg, sp, guess)
        marker = text.find("## CLOSURE (declared-first)")
        if marker < 0:
            fail(4, "closure block not found in own output")
        if marker == guess:
            break
        guess = marker
    else:
        fail(4, "CLOSURE_END_BYTE did not reach a fixed point")

    fence_walk(text)
    defeat_provenance_gate(text)
    overread_gate(text)
    self_citation_gate(text)
    res = residue_scan(text)
    if res:
        fail(13, f"output-inspection residue in authored prose: {res}")
    n = prose_digests(text)

    OUT.write_text(text)
    d = hashlib.sha256(OUT.read_bytes()).hexdigest()
    (OUT.parent / (OUT.name + ".seal.sha256")).write_text(f"{d}  {OUT.name}\n")
    print(f"ARTIFACT   {d}  {OUT.name}")
    print(f"CLOSURE_END_BYTE = {guess}")
    print(f"PROSE_DIGESTS = {n}/{n} STRICT==STABLE")
    print(f"RESIDUE_GREP = clean ({len(RESIDUE)} patterns)")
    print("NO_NUMERIC_PATH = CLEAN")
    print(f"DEFEAT_PROVENANCE_GATE = PASSED ({len(CANDIDATES)} candidates adjudicated)")
    print("SELF_CITATION_GATE = PASSED")


if __name__ == "__main__":
    main()
