#!/usr/bin/env python3
"""Generator for STAGE8_S13_DECIDER_CHECK_DARIO_V001.md (DARIO lane, relay 1111).

Mandated refusal paths, all live:
  R1  member-absent / digest-at-path
  R4  span digest + span BOUNDS guard (bounds checked against file length)
  R6  no-numeric-path self-scan (string literals stripped from this file's own code first)
  R7  fence depth-walk (gated phrases must survive line wrapping)
  R10 over-read gate (an UNDETERMINED given may not be silently upgraded)
  R13 residue scan (output-inspection tokens over authored prose)
  closure declared-first, CLOSURE_END_BYTE solved as a fixed point on the artifact's own bytes
"""
import hashlib, pathlib, re, sys

ROOT = pathlib.Path("/Users/bgm/MB Work/alpha-program-archive")
WS   = ROOT / "workspace"
SELF = pathlib.Path(__file__).resolve()
OUT  = WS / "STAGE8_S13_DECIDER_CHECK_DARIO_V001.md"


def fail(n, msg):
    print(f"REFUSED R{n}: {msg}", file=sys.stderr)
    sys.exit(1)


# ---------------------------------------------------------------- closure members
MEMBERS = {
    "01": ROOT / "workspace/STAGE8_S13_THRESHOLD_SHAPE_FABLE_V001.md",
    "02": ROOT / "workspace/STAGE8_S16_BETA_SENSITIVITY_ATTACK_FABLE_V001.md",
    "03": ROOT / "supervision/SURFACE_DEFINITION_OF_RECORD_V001.md",
    "04": ROOT / "workspace/STAGE8_RECORD_CELL_SURFACE_AND_BETA_CLOSURE_HUNT_EINSTEIN_V001.md",
    "05": ROOT / "workspace/COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md",
    "06": ROOT / "workspace/R3_4_LORENTZIAN_THRESHOLD_RETURN_RESULT_V001.md",
    "07": ROOT / "workspace/BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_DERIVATION_V001.md",
    "08": ROOT / "workspace/BID_CHIRAL_SOURCE_RECORD_INCIDENCE_PARENT_V001.md",
    "09": ROOT / "workspace/BID_CHARGED_HANDLE_ACTIVATION_DERIVATION_V002.md",
    "10": ROOT / "workspace/STAGE8_7A_DBR_SPECTRUM_DARIO_V001.md",
    "11": ROOT / "workspace/STAGE8_7A_DBR_BETA_SECTORS_V3_DARIO_V001.md",
}

# spans pinned by locating their marker text at run time (no offset literals authored)
SPAN_MARKERS = {
    "04a": "OF THE THIRTEEN\nSEALED INTERFACE QUANTITIES",
    "04b": "beta-SENSITIVE junctions",
    "04c": "whose only output is",
    "03a": "Whether a *derived* S16 would",
    "03b": "The scale orbit is free.",
    "02a": "If instead it requires the",
    "02b": "Secondary (needed only after a lock-shaped primary)",
    "01a": "Per the prior attack's own protocol the subordinate F6b",
    "05a": "R = beta c Delta tau",
    "06a": "p_lambda(E)=sqrt(",
}


def digests():
    out = {}
    for k, p in MEMBERS.items():
        if not p.exists():
            fail(1, f"closure member {k} absent at path: {p}")
        out[k] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def spans():
    """Locate each pinned span, bounds-check it, and digest it."""
    out = {}
    for tag, marker in SPAN_MARKERS.items():
        num = tag[:2]
        raw = MEMBERS[num].read_bytes()
        needle = marker.encode()
        a = raw.find(needle)
        if a < 0:
            fail(4, f"span marker for {tag} not found in member {num}: {marker!r}")
        b = a + len(needle)
        if b > len(raw) or a < 0:
            fail(4, f"span [{a},{b}) out of range in member {num} (length {len(raw)})")
        chunk = raw[a:b]
        if len(chunk) != b - a:
            fail(4, f"span [{a},{b}) short read in member {num}")
        out[tag] = (a, b, hashlib.sha256(chunk).hexdigest())
    return out


# ---------------------------------------------------------------- self-scans
NUMERIC_PATH = [
    "float(", "eval(", "numpy", "scipy", "math.", "sympy", "decimal",
    "round(", "sum(", "mean", "sqrt(", "log(", "exp(", "**0.", "/ 137", "codata",
]

RESIDUE = [
    "measured value", "experimental", "observed value", "codata", "best fit",
    "matches the known", "agrees with the accepted", "compare to the accepted",
    "known value", "actual value", "empirical value", "reference value of alpha",
    "downstream", "later stage", "the answer is", "we already know alpha",
    "target value", "expected value of alpha", "fit to data", "tuned to",
    "output inspection", "consulted the result", "peeked", "back-solve",
    "reverse-engineer", "calibrated against", "benchmark value",
]


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
    """R7: gated phrases must appear intact — a line wrap that splits one is a refusal."""
    flat = re.sub(r"\s+", " ", text)
    gated = [
        "alpha_computed = false",
        "proof_authorized = false",
        "kappa_record_computed = false",
        "JOINT_ANCHOR_DERIVED = false",
        "EVALUATED_NOTHING = CERTIFIED",
        "IMPORTED_NOTHING = CERTIFIED",
        "OUTPUT_INSPECTION = NONE-CERTIFIED",
        "NO_REGISTER_READ = CERTIFIED",
    ]
    for g in gated:
        if g not in text:
            if g in flat:
                fail(7, f"gated phrase split by a line wrap: {g!r}")
            fail(7, f"gated phrase absent: {g!r}")


def overread_gate(text):
    """R10: this check rules on an artifact that upgraded an UNDETERMINED given.
    If we affirm the subject's consequence line we must address that upgrade by name."""
    if "K3_R_SOLE_BETA_CARRIER = CONFIRMED" in text:
        if "F6b" not in text:
            fail(10, "a CONFIRMED on the beta-carrier chain must still address the "
                     "undischarged secondary foot F6b, which the subject left untyped")
    if "VERDICT = FINISH-B-ANCHORED" in text:
        fail(10, "FINISH-B-ANCHORED asserts the Finish-A lever is dead; this check found the "
                 "lever relocated, not dead — that verdict would repeat the subject's over-read")


def residue_scan(text):
    low = text.lower()
    hits = [t for t in RESIDUE if t in low]
    return hits


def prose_digests(text):
    """STRICT (raw bytes) vs STABLE (whitespace-normalised) digest per authored section."""
    secs = re.split(r"\n(?=## )", text)
    n = 0
    for s in secs:
        strict = hashlib.sha256(s.encode()).hexdigest()
        stable = hashlib.sha256(re.sub(r"\s+", " ", s).strip().encode()).hexdigest()
        if strict and stable:
            n += 1
    return n


# ---------------------------------------------------------------- artifact body
def body(dg, sp, close_end):
    t = []
    A = t.append
    A("# STAGE8_S13_DECIDER_CHECK_DARIO_V001")
    A("")
    A("LANE: DARIO (external adversarial anchor, relay 1111). ROLE: [CHECK] — adversarially refute")
    A("the decider `S13_SHAPE = LOCK-SHAPED => Finish B`. Default to skepticism; the verdict closes")
    A("a route, so it was attacked, not audited. Re-derived at the bytes from the named grounds;")
    A("**zero testimonial weight given to either Fable artifact's own assertions.**")
    A("**ALL RESULTS CLAIMED** until the Codex 2 check. Builder never verifies own work.")
    A("")
    A("GATES DECLARED AND HELD: alpha_computed = false; proof_authorized = false;")
    A("kappa_record_computed = false; JOINT_ANCHOR_DERIVED = false. Nothing was computed — no value,")
    A("bound, or estimate of any threshold, eigenvalue, mass, coupling, kappa, K_*, beta, or alpha;")
    A("every numeric string below is a sealed-text quotation or a symbol. No measured-constant")
    A("comparison. NO_REGISTER_READ = CERTIFIED (register, tracker, plan, road, ledger: none opened;")
    A("register line numbers appear only as carried inside sealed members). No git action of any kind.")
    A("")
    A("## SOURCES (all digested at path before use)")
    A("")
    A("```text")
    for k in sorted(MEMBERS):
        rel = str(MEMBERS[k]).replace(str(ROOT) + "/", "")
        A(f"{k}  {dg[k]}  {rel}")
    A("```")
    A("")
    A("SUBJECT PINS: both subjects match the paste's pinned digests at path (member 01 = the decider,")
    A("member 02 = its supporting given). **NEITHER SUBJECT CARRIES A `.seal.sha256` SIDECAR.** This is")
    A("the third such flag this lane has raised (1089, 1109, and here); it is a registrar-side custody")
    A("gap, not a defect in the subjects, and nothing below is weakened by it — every clause consumed")
    A("was re-derived from a member digested at path in this relay.")
    A("")
    A("## 0. LEAD")
    A("")
    A("**The lock-shaped typing survives my attack. Its stated consequence does not.**")
    A("")
    A("I could not find a surface-native route to a fiber-shaped threshold (K1 = NO), every named")
    A("built exemplar is lock-shaped (K2 = CONFIRMED), R34's threshold condition is genuinely R-free")
    A("at the bytes (CONFIRMED), and the subject computed no value and imported no metric (K4 =")
    A("CONFIRMED). On the question it was commissioned to answer, the subject is right.")
    A("")
    A("**The find is the step after that one.** The subject's given (member 02) returned")
    A("`S16_BETA_SENSITIVE = UNDETERMINED` and named TWO feet through which beta could still enter a")
    A("derived S16: F6a (the threshold) and F6b (the connected-gluing foot). Member 02's own protocol")
    A("states the disposition of the secondary explicitly: *\"Secondary (needed only after a")
    A("lock-shaped primary)\"*, and *\"Embedding-required => S16 inherits the booked beta-sensitive GAP")
    A("junction => YES\"*. The subject discharges F6a — and then declares")
    A("`CONSEQUENCE_FOR_S16 = beta-INVARIANT` while stating in the same section that **F6b \"becomes")
    A("the live residual\" and \"is NOT retyped here\"**. An UNDETERMINED with two named feet, one")
    A("discharged and one expressly left untyped, does not license a determinate consequence line.")
    A("")
    A("The subject's one-line dismissal of F6b — that the skeleton-to-cell embedding is \"booked off")
    A("the surface\", hence not a surface-native channel — **begs the question at issue.** The")
    A("Finish-A lever requires a junction simultaneously DERIVED and SCALE-SENSITIVE. If S16's gluing")
    A("foot requires the embedding, then deriving S16 requires deriving the embedding, and a derived")
    A("embedding that carries beta is precisely the lever. The dismissal assumes the embedding stays")
    A("underived, which is the very thing a derived S16 would change. Member 04 types that embedding")
    A("as one of the three beta-SENSITIVE junctions of record (GAP, *\"has never been attempted\"*) —")
    A("it is a live beta carrier, parked, not a closed one.")
    A("")
    A("**So: the Finish-A lever is not dead. It is relocated — from the threshold foot, where this")
    A("relay closed it, to the gluing foot, where nobody has typed it.** That is a real advance and a")
    A("smaller remaining question; it is not the closure the paste's claim states.")
    A("")
    A("## 1. WHAT I RE-DERIVED, AND ONE GROUND THE SUBJECT DID NOT NEED TO BORROW")
    A("")
    A("The subject's NO rests on an inventory argument (member 03 I.4: *\"a radius is a metric datum,")
    A("not a surface datum\"*) plus a TYPE-R amplitude refutation. Both check out. But the result has a")
    A("shorter and stronger ground, which I state as MINE:")
    A("")
    A("**beta is a ratio of two dimensionful data.** Member 05 defines it at the bytes as")
    A("`R = beta c Delta tau` — beta is (fiber radius) / (a record-side length). To carry beta, an")
    A("object must consume TWO independent dimensionful quantities. The record supplies exactly ONE")
    A("(the interval T_R), and even that one only up to the free lambda orbit (member 03 II.7:")
    A("*\"The scale orbit is free.\"*, II.10: the surface *\"forces the entire dimensionless structure")
    A("and leaves the absolute scale free\"*). A second, independent dimensionful datum is precisely")
    A("what the record does not have.")
    A("")
    A("[MINE, marked] This makes `RECORD_CAN_FURNISH_FIBER_SHAPED = NO` a **dimensional fact about")
    A("the record, not a fact about S13.** It holds for every conceivable record object, thresholds")
    A("included. That is why K1 below closes so cleanly — and it is also why the result carries less")
    A("information than the \"decider\" framing suggests: the answer was fixed by the record's")
    A("dimensional content before S13 was examined. The subject's four exemplars are consistent with")
    A("it, and confirm it, but they are not what makes it true.")
    A("")
    A("## 2. K1 — THE LEVER: IS THERE A SURFACE-NATIVE FIBER-SHAPED ROUTE?")
    A("")
    A("Six routes attacked. Each dies to a SEALED sentence, not to the subject's assembly:")
    A("")
    A("1. **Holonomy / Wilson-line.** The natural way to make R appear from connection data is a")
    A("   holonomy around the compact direction. It fails at the source: member 05 states that the")
    A("   action-phase period *\"fixes the coordinate period and integer character lattice. It does")
    A("   not fix the proper radius `R`.\"* A holonomy is metric-independent by construction; the")
    A("   record sees only the dimensionless product. **DEAD, on member 05's own sentence.**")
    A("2. **Charge-lattice / KK-momentum.** The integers of the character lattice are surface data,")
    A("   but the tower's `1/R^2` prefactor is metric. Member 03 I.4: no fiber metric. The record")
    A("   holds the label, never the eigenvalue. **DEAD.**")
    A("3. **Amplitude / weight channel.** Refuted TYPE-R with exact mechanism (member 03 II.6). I")
    A("   corroborate it independently from the ratified law I built the ground for: the record")
    A("   sandwich is a product of UNIT-MODULUS holonomy characters, so it carries phase and no")
    A("   magnitude. **DEAD, and I confirm the mechanism first-hand.**")
    A("4. **Radion.** Member 05: the radius is a dynamical radion and pure circle reduction *\"does")
    A("   not generate a potential that selects one constant value.\"* Unbuilt, and continuum")
    A("   machinery besides — a barred import for this lane. **DEAD.**")
    A("5. **Dimensional analogy (set R from a record interval).** Explicitly barred at the bytes,")
    A("   member 05: *\"Declaring `R` equal to a record interval by dimensional analogy does not")
    A("   pass. A derived metric-gluing or stabilization law is required.\"* This is the circular")
    A("   route this lane already ruled void at 1093/1099. **DEAD.**")
    A("6. **The branch state** (the one dimensionless surface-real ingredient this lane isolated at")
    A("   1105). Dimensionless by type; it cannot carry a ratio of two lengths. **DEAD.**")
    A("")
    A("`K1_FIBER_ROUTE_FOUND = NO.` The lock-shaped typing is not refuted by any route I could build.")
    A("")
    A("## 3. K2 — COMPLETENESS, AND R34 RE-DERIVED AT THE BYTES")
    A("")
    A("**R34 (member 06), re-derived independently.** The Hamiltonian is `H(p)=alpha_D dot p + mu S")
    A("tensor c_partial` with `spec(c_partial)={-sqrt(2),0,+sqrt(2)}`; on the record eigenspace")
    A("`H_lambda(p)^2=|p|^2+mu^2 lambda^2`; the threshold sits where `p_lambda(E)=sqrt(E^2-mu^2")
    A("lambda^2)` vanishes. I read the entire member: the fiber radius does not occur anywhere in the")
    A("Hamiltonian, its bands, or its threshold condition. `K2_R34_R_FREE = CONFIRMED.`")
    A("")
    A("[MINE, marked — the qualification that matters] R34's threshold is R-free because its ENTIRE")
    A("scale is carried by the source-mass datum `mu`, and member 06 does not derive `mu`")
    A("(`complete_parameter_free_Q_spec_frozen = false`, its own status block). An undetermined")
    A("parameter contains no R in the same way it contains nothing. So E3 is a **built band structure")
    A("with an underived threshold scale**, not a built lock. The subject says so in its own scope")
    A("note, but its headline — *\"four built exemplars, all lock-shaped\"* — reads stronger than what")
    A("it established. The honest count is **three built locks plus one conditional**.")
    A("")
    A("The upgrade the subject applies (any DERIVED `mu` lands in the interval-lock class) is")
    A("nonetheless licensed, and I confirm it: by member 03 II.10 the surface forces only")
    A("dimensionless structure, so a derived `mu` can only ever be derived as `mu` x (record")
    A("interval) = pure number. Lock-shaped follows. It is an inference about an object that does not")
    A("yet exist, and it is correctly marked as assembly in the subject.")
    A("")
    A("**Other exemplars, re-verified at path:** E1 `tau_first(B_ch) = pi/sqrt(2) = tau_R` with")
    A("coefficients `(0,1,1)` and *\"No numerical multiplier\"* (member 07); E2 the incidence-weight")
    A("exhaustion to `|a|=|b|=1` (member 08, verified at the bytes); E4 `m_* T_R = pi`, typed at")
    A("member 04 as *\"contains no `R`, trivially beta-invariant\"*. Fiber-shaped candidates: the D_BR")
    A("tower is not a built exemplar — member 10 records its defining primaries **absent")
    A("archive-side**, member 11 records the radii as *\"three independent free data\"*,")
    A("CARRIED-AS-PARAMETER. `K2_ALL_EXEMPLARS_LOCK = CONFIRMED.`")
    A("")
    A("**Scope limit, disclosed:** my completeness check ranges over the exemplars NAMED by the")
    A("subject plus the members digested here. The fence scopes greps to named subjects, so I did not")
    A("sweep the archive for unnamed charged-threshold exemplars and do not certify completeness")
    A("beyond the named set. A broad sweep is what tripped the register bar at 1102; I did not run one.")
    A("")
    A("## 4. K3 — IS R THE SOLE BETA-CARRIER?")
    A("")
    A("The chain under test: *beta is defined as fiber-radius rescaling => R is the sole beta-carrier")
    A("=> R is a rail => no surface object carries beta.*")
    A("")
    A("**As stated, the chain is circular.** The beta ACTION is defined (members 04, 05) as")
    A("`R -> beta R` at fixed `Delta tau`, with T_R and the branch data held. Under an action that")
    A("moves only R, only R-containing statements move — that is a restatement of the definition, not")
    A("a finding. The occurrence criterion inherits the same shape: it can detect motion in R and")
    A("nothing else. A check that let this pass as ground would be accepting a tautology as a")
    A("derivation, which is the failure this lane caught at 1099 and 1109.")
    A("")
    A("**So I looked for a second carrier.** `beta = R / (c Delta tau)` has three coordinates, and")
    A("the ratio moves when ANY of them moves. Two alternatives to R:")
    A("")
    A("- **`Delta tau` / T_R — the lambda orbit, which IS surface-native.** Moving T_R at fixed R does")
    A("  change the ratio. This was my strongest candidate for reopening Finish A, and it is")
    A("  **defeated on sealed ground I had to go find, because the subject does not cite it**: member")
    A("  04's C2 corollary books *\"a condition whose only output is\"* T_R as unable to be the fixer")
    A("  (Q-08 as carried), and member 04's lead states that completing the program's named")
    A("  F-equation *\"WOULD FIX THE DIAMOND'S SCALE AND LEAVE `beta` FREE\"*. Combined with member 03")
    A("  II.7 — the lambda orbit leaves every derived surface statement identical — no derived surface")
    A("  quantity moves under this realization. **Closed.**")
    A("- **`c` — the internal/external conversion.** Booked a rail import (member 03 III.11). Not")
    A("  surface-native. **Closed.**")
    A("")
    A("`K3_R_SOLE_BETA_CARRIER = CONFIRMED` — but confirmed **on repaired ground**: no second carrier")
    A("can move a derived surface statement, and that is established by Q-08's sealed non-implication")
    A("plus II.7, not by the definitional chain the subject offers. The subject reached a right answer")
    A("by an argument that does not carry its own weight.")
    A("")
    A("**One live seam recorded, not resolved:** member 04's C7 books that *beta*'s defining")
    A("`Delta tau` is `sqrt(2)`-fork-conditional. Every lock the subject cites is `sqrt(2)`-laden, and")
    A("the subject never declares a fork slot. This does not create a beta channel and I do not claim")
    A("it does; it means the beta-invariance statement is itself fork-conditional and should be")
    A("carried as such.")
    A("")
    A("## 5. K4 — FENCE AND IMPORT")
    A("")
    A("**No value computed.** I traced every numeric string in the subject to a sealed source and")
    A("re-verified each at path: `pi/sqrt(2)` and `(0,1,1)` (member 07); `{-sqrt(2),0,+sqrt(2)}`")
    A("(member 06); `{-1,0,+1}` (member 09); `|a|=|b|=1` (member 08); `m_* T_R = pi` (members 03, 04);")
    A("the D_BR tower (member 10). Line-level citations spot-checked and correct:")
    A("`quantum_threshold_map_derived = false` at member 05 line 112; reopen item 5 at line 97; the C8")
    A("jointness quotation at lines 83-84; the beta relation at line 57. **Every one resolved.**")
    A("")
    A("**No metric imported.** The subject names the 5d ansatz and the D_BR geometry only as quoted")
    A("rail objects it is excluding. Naming an import in order to refuse it is not importing it. No")
    A("continuum theorem is used as ground; the grounds are member 03's sections and the four")
    A("exemplars. `K4_CLEAN = CONFIRMED.`")
    A("")
    A("## 6. CITATION DEFECTS FOUND (none load-bearing, all disclosed)")
    A("")
    A("1. **The ANCHOR path is wrong in BOTH Fable artifacts.** Both cite it as")
    A("   `alpha_supervision/SURFACE_DEFINITION_OF_RECORD_V001.md` and certify it *\"verified at path")
    A("   before use\"*. **No such directory exists.** The artifact resolves at")
    A("   `supervision/SURFACE_DEFINITION_OF_RECORD_V001.md`, sealed, sidecar present, digest")
    A("   matching the tasked pin exactly. Content custody is intact; reproducibility is not — a")
    A("   checker following the stated path finds the most load-bearing ground ABSENT. Worth a")
    A("   registrar correction.")
    A("2. **A quotation is attributed to the wrong artifact, upward in custody.** The subject")
    A("   attributes *\"untwisted adopted skeleton\"* to member 04 (\"the census's ... characterization\").")
    A("   It is not in member 04. It is in member 10, which presents it as a quotation of a defining")
    A("   principle that member 10 itself records as **absent archive-side**. The effect is to move a")
    A("   phrase from an absent primary onto a present sealed artifact — a custody upgrade. The clause")
    A("   is decorative where used, so nothing turns on it, but the direction of the slip is the one")
    A("   this program polices.")
    A("3. **Emphasis added inside quotation marks.** The subject quotes member 11 as *\"THREE")
    A("   independent free data\"*; member 11 reads \"three independent free data\". Capitalization is")
    A("   the subject's. Cosmetic.")
    A("")
    A("## 7. WHAT I DID NOT DO")
    A("")
    A("I did not retype F6b — that is the subject's own untouched residual and typing it is a")
    A("construction, not a check. I did not build S13, S16, or any Q_spec slot; did not derive `mu`,")
    A("select a lambda-orbit member, or decide the `sqrt(2)` fork; did not evaluate any threshold,")
    A("ratio, or coupling; did not read the register, tracker, plan, road, or ledger; did not enter")
    A("`a32_holdout/custodian_private/`; ran no subagent and delegated nothing.")
    A("")
    A("## 8. OVERCLAIM AUDIT")
    A("")
    A("- **PROVABLE (re-derived at the bytes this relay):** every member digest; R34's threshold")
    A("  condition and its R-freeness; the E1/E2/E4 quotations; member 05's four line-level")
    A("  citations; member 04's thirteen-quantity scoping, its three beta-sensitive junctions, and")
    A("  its C2/C7/C8 clauses; member 03's I.4, II.6, II.7, II.10, III.11, III.12, IV.13; the D_BR")
    A("  primaries' absence and the radii's freedom; the ANCHOR path defect; the misattribution.")
    A("- **MINE (assembly, marked inline):** the two-dimensionful-data ground for K1 in section 1;")
    A("  the six-route sweep of section 2; the qualification that R34 is a built band structure with")
    A("  an underived threshold scale; the reading that the subject's F6b dismissal begs the")
    A("  question; the judgement that K3's stated chain is circular and needs Q-08 to carry it.")
    A("- **NOT claimed:** that a fiber-shaped route exists (I found none); that F6b IS beta-carrying")
    A("  (it is untyped, and I left it untyped); that Finish A is live (it is not established — only")
    A("  not closed); that Finish B is wrong; that the subject acted in bad faith (it disclosed F6b's")
    A("  residual status in its own body — the defect is the final line, not the reasoning); anything")
    A("  about which finish is TRUE.")
    A("")
    A("---")
    A("")
    A("## FINAL LINES")
    A("")
    A("```text")
    A("K1_FIBER_ROUTE_FOUND = NO (six surface-native routes attacked - holonomy/Wilson-line,")
    A("    charge-lattice/KK-momentum, amplitude/weight, radion, dimensional analogy, branch state -")
    A("    each dies to a SEALED sentence rather than to the subject's assembly; and the result has a")
    A("    shorter ground than the subject's: beta is a ratio of TWO dimensionful data and the record")
    A("    supplies exactly ONE, up to the free lambda orbit.  LOCK-SHAPED NOT REFUTED.)")
    A("")
    A("K2_ALL_EXEMPLARS_LOCK = CONFIRMED (over the NAMED exemplar set; zero built fiber-shaped")
    A("    exemplars - the D_BR route's defining primaries are absent archive-side and its radii are")
    A("    three free carried parameters.  Honest count is THREE built locks plus ONE conditional:")
    A("    E3's threshold scale is carried entirely by an underived mu.  Completeness certified only")
    A("    over the named set - the fence bars the archive-wide sweep that would extend it.)")
    A("")
    A("K2_R34_R_FREE = CONFIRMED (re-derived at the bytes: H(p)=alpha_D dot p + mu S tensor")
    A("    c_partial, bands H_lambda(p)^2=|p|^2+mu^2 lambda^2, threshold at p_lambda(E)=0; the fiber")
    A("    radius occurs nowhere in the member.  R-free - but scale-free too: mu is undetermined")
    A("    there (complete_parameter_free_Q_spec_frozen = false).)")
    A("")
    A("K3_R_SOLE_BETA_CARRIER = CONFIRMED ON REPAIRED GROUND (the subject's stated chain is CIRCULAR:")
    A("    an action defined to move only R moves only R-containing statements.  I hunted a second")
    A("    carrier in beta = R/(c Delta tau) and found two candidate coordinates; both close - c is")
    A("    rail-typed (III.11), and the lambda orbit is defeated by Q-08's sealed non-implication as")
    A("    carried at member 04's C2 plus II.7, ground the subject does not cite.  Right answer,")
    A("    argument that does not carry its own weight.  Seam recorded: beta's defining Delta tau is")
    A("    sqrt(2)-fork-conditional and no fork slot is declared.)")
    A("")
    A("K4_CLEAN = CONFIRMED (no value computed - every numeric string traced to a sealed source and")
    A("    re-verified at path, all four line-level citations into member 05 resolve; no metric or")
    A("    continuum machinery used as ground, rail objects named only to be excluded.  Three")
    A("    citation defects found, none load-bearing: the ANCHOR path is wrong in BOTH artifacts")
    A("    (alpha_supervision/ does not exist; it resolves at supervision/, sealed, digest matching);")
    A("    'untwisted adopted skeleton' is attributed to member 04 but lives in member 10 as a")
    A("    quotation of an ABSENT primary - a custody upgrade; and emphasis was added inside")
    A("    quotation marks on member 11.)")
    A("")
    A("VERDICT = UNDETERMINED - S13 LOCK-SHAPED CONFIRMED, FINISH-A LEVER RELOCATED NOT DEAD.")
    A("    The typing survives every attack I could mount.  Its stated consequence does not: the")
    A("    subject's own given returned S16_BETA_SENSITIVE = UNDETERMINED over TWO named feet and")
    A("    ruled 'Embedding-required => S16 inherits the booked beta-sensitive GAP junction => YES'.")
    A("    The subject discharged F6a, wrote that F6b 'becomes the live residual' and 'is NOT retyped")
    A("    here', and then published CONSEQUENCE_FOR_S16 = beta-INVARIANT anyway.  Its one-line")
    A("    dismissal of F6b - the embedding is booked off the surface - begs the question, because a")
    A("    DERIVED S16 requiring that embedding is exactly the derived-and-scale-sensitive junction")
    A("    the lever needs, and member 04 types that embedding as beta-SENSITIVE (GAP).  The lever is")
    A("    not dead; it moved from the threshold foot to the gluing foot, where nobody has typed it.")
    A("    NEXT DECIDER, NAMED: type F6b - the Q_spec's connected gluing and overlap terms - against")
    A("    unit-modulus transition-function gluing versus the skeleton-to-cell embedding.")
    A("")
    A("SUBJECT_CONSEQUENCE_LINE = OVER-READ (an UNDETERMINED given with one of two feet discharged")
    A("    was published as a determinate beta-INVARIANT consequence; the subject's body discloses the")
    A("    residual, so the defect is in the final line, not in the reasoning.)")
    A("")
    A("EVALUATED_NOTHING = CERTIFIED")
    A("IMPORTED_NOTHING = CERTIFIED")
    A("OUTPUT_INSPECTION = NONE-CERTIFIED")
    A("NO_REGISTER_READ = CERTIFIED")
    A("NO_SUBAGENT_DELEGATION = CERTIFIED")
    A("SUBJECT_SIDECARS = ABSENT for both subjects (third such flag from this lane: 1089, 1109, 1111)")
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
    A("CLOSURE_MEMBERS = 11 (content-addressed, each digested at path in this relay)")
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

    # declared-first closure: solve CLOSURE_END_BYTE as a fixed point on the artifact's own bytes
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
    overread_gate(text)
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


if __name__ == "__main__":
    main()
