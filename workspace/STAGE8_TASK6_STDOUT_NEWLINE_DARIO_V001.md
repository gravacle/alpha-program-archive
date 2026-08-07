# STAGE 8 / TASK 6 / BUILD — THE STDOUT NEWLINE — DARIO V001

Lane: Dario (Claude Opus 5), **Builder B** of the RD-22 custody graph
Task: PASTE 673 / Task 6 build — one byte
Authority: RD-22 + the Q-594 canon adjudication. **THIS ARTIFACT INVOKES NOTHING.**

```text
STDOUT = tight canonical value, no trailing newline (demonstrated)
SELF_CHECK = passed
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 note on the canon I won and then broke, §1.1)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**Run 018: the verifier ran complete.** It emitted its full canonical verdict —
24,555 bytes, one JSON value — and exited 1 because it found faults. That is the
preregistered honest behaviour, and it is the first end-to-end execution of the
independent verifier. The stop is one byte at the end of the stream.

## 1. THE FIX

### 1.1 The canon I won, and then broke on my own output

[YOURS] The Q-594 adjudication went my way: *"no insignificant whitespace"*
convicted Builder A's file canon of a trailing byte. **I then emitted the same
byte on my own stdout for five relays.** I applied the rule to the file I write
and never to the stream I write, as though a canon about JSON representation
stopped at the filesystem boundary.

The symmetry is the whole point, and the parent is right to enforce it in both
directions: a canon that only bites the other lane is not a canon.

### 1.2 What changed

Three emission sites, all removed — **the verdict itself, the fail-closed
verdict, and the launcher's dry-run payload**, so the rule holds on every path
that can reach stdout rather than only the one under test:

```text
verifier/verify.py:275   sys.stdout.write("\n")   after the fail-closed verdict   REMOVED
verifier/verify.py:279   sys.stdout.write("\n")   after the real verdict          REMOVED
run_verifier.py:80       sys.stdout.write("\n")   after the dry-run payload       REMOVED
```

Remaining `sys.stdout.write("\n")` sites in the runtime package: **zero**
(verified by scan).

`stderr` is untouched and keeps its own newlines — it is diagnostic text, not a
canonical value, and the two streams are governed by different rules.

## 2. THE DEMONSTRATION — byte-exact

```text
$ python3 -I -S -B run_verifier.py --dry-run-launch > so.bin 2> se.bin
exit                     = 2
stdout bytes             = 372
last byte (hex)          = 7d          <- '}'  , not 0a
ends with newline?       = False
rstrip() == raw          = True        <- no trailing whitespace of any kind
stderr bytes             = 0           <- success path emits nothing on stderr
parses as one JSON value = True
round-trips canonical    = True        <- dumps_canonical(loads_strict(d)) == d

first bytes: b'{"chain_invoked":false,"dont_write_bytecode":true,"entry_point":"run_verifier.py"…'
last  bytes: b'…UN","verifier_module":"verifier.verify"}'
```

The stream ends on `}`. The `rstrip()` identity is the stronger check: it rules
out **any** trailing whitespace, not merely `\n`, which is what *"no insignificant
whitespace"* actually says.

[PROVABLE] **`stderr` is empty on the success path.** It carries text only in the
fail-closed branch (`fail-closed: <reason>`) and in the launcher's import-failure
branch. Both are genuine faults, and neither is reachable when a verdict forms.

## 3. DELTA AND PIN CHECK

```text
CHANGED  verifier/verify.py                    two newline writes removed
CHANGED  run_verifier.py                       one newline write removed
CHANGED  rd22.verifier-manifest.v001.json      2616cf15… -> 83b688463b26a6d6409475e8059ecb017ea3a59c79a4d308d05fb8d3386c49bf
CHANGED  rd22.verifier-manifest.v001.json.seal.sha256   regenerated, verified OK

verifier_root_sha256   d5f279c4…  ->  eb246168d86e945df78900903232314293bae382b11ecf1e3d5074caa3e62b92
```

The instance moves because the root covers both changed files — the root doing
its job. Field list unchanged at 11.

| Claim | Verified before sealing |
|---|---|
| all three emission sites removed | enumerated before and after; zero remain |
| stdout ends on `}` | last byte `0x7d` |
| no trailing whitespace at all | `rstrip()` identity, not just a `\n` test |
| one canonical value | parses, and round-trips through `dumps_canonical` |
| stderr empty on success | 0 bytes captured |
| instance canonical | round-trip identical; sorted; single line; no trailing newline; 11 fields |
| sidecar verifies, equals `manifest_sha256()` | `83b68846…` |
| root recomputed and consistent | manifest value == `package_root_digest()` |
| ledger guard, evidence root, T-labels intact | unchanged from the prior relay |
| 18 files; zero `assert`; self-check CLEAN | executed |

### 3.1 `F_PLDEC` and coverage

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. **The chain was not invoked**; the demonstration is the
dry run, which opens no run input. `alpha_computed = false`;
`proof_authorized = false`; `kappa_record_computed = false`; no member bound; no
fixed point; no end test; no numeric evaluation; no comparison to any measured
constant.

**Coverage, stated exactly:** I removed one byte from three code paths and
reissued the instance. I claim **no check or fixture outcome**. Run 018's exit 1
means my verifier found faults in what it was given — **those findings are its
output, not a verdict on the program**, and adjudicating them is a separate act
that has not happened here.

## 4. SELF VERB AUDIT

| My verb | Check |
|---|---|
| Canon applied to myself | I won the Q-594 adjudication and then broke the same rule on my own stdout for five relays. Recorded as mine, not as a parent preference. |
| Fixed on **all** paths | Three sites, including the fail-closed verdict and the dry-run payload — not only the one the demonstration exercises. |
| `demonstrated` | Byte-level: last byte in hex, `rstrip()` identity, canonical round-trip, and stderr byte count. Not "looks right". |
| stderr left alone | Deliberate and stated: diagnostics are not canonical values, and the two streams are governed differently. |
| Run 018 not overclaimed | The verifier ran and found faults. I do **not** report those faults as adjudicated, and exit 1 is its honest output, not a conclusion about the program. |
| `CHAIN_INVOKED = false` | Literally true — this relay's demonstration is the dry run. |

---

```text
STDOUT = tight canonical value, no trailing newline (demonstrated byte-exact:
  stdout ends on 0x7d '}', ends_with_newline = False, and rstrip() == raw so NO
  trailing whitespace of any kind survives -- the stronger test, and the one that
  matches what "no insignificant whitespace" actually says. The stream parses as
  one JSON value and round-trips through dumps_canonical unchanged. stderr is
  0 bytes on the success path. THREE emission sites were fixed, not one: the real
  verdict, the fail-closed verdict, and the launcher's dry-run payload, so the rule
  holds on every path that reaches stdout; zero sys.stdout.write("\n") remain in
  the runtime package. stderr keeps its newlines deliberately -- diagnostics are
  not canonical values. I WON THE Q-594 CANON AND THEN BROKE IT ON MY OWN STDOUT
  FOR FIVE RELAYS, applying the rule to the file I write and never to the stream;
  a canon that only bites the other lane is not a canon.)
SELF_CHECK = passed (package self-check CLEAN; 18 files; zero asserts; dry run
  exit 2 under -I -S -B. Instance reissued because verifier_root_sha256 covers both
  changed files: d5f279c4… -> eb246168d86e945df78900903232314293bae382b11ecf1e3d50
  74caa3e62b92, instance 2616cf15… -> 83b688463b26a6d6409475e8059ecb017ea3a59c79a4
  d308d05fb8d3386c49bf, sidecar regenerated and verified OK and equal to
  manifest_sha256(); field list unchanged at 11; ledger guard, evidence root and
  the Q-601 T-label contexts all intact.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote; this relay's
  demonstration is the dry run, which opens no run input. Run 018's exit 1 means
  the verifier FOUND FAULTS in what it was given -- that is its honest output and
  NOT a verdict on the program, and adjudicating those findings is a separate act
  that has not happened here.)
VERB_AUDIT_SELF = CLEAN (+1 note recorded as mine: I applied the whitespace canon
  to files and never to streams, for five relays, after winning the adjudication
  that established it.)
```

The verifier ran end to end and the only thing standing between it and a clean
handshake was a byte I had spent five relays not noticing, on the one rule I had
argued for. The useful part is not the fix; it is that the canon was enforced
against the lane that wrote it.
