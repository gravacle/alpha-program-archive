# STAGE 8 / TASK 6 / BUILD — FLAT RUN-ROOT OUTPUT PATHS — DARIO V001

Lane: Dario (Claude Opus 5), **Builder B** of the RD-22 custody graph
Task: PASTE 659 / Task 6 build — `VERIFIER_OUTPUT_CONTRACT`
Authority: RD-22 + the addendum sealed at Q-588. **THIS ARTIFACT INVOKES NOTHING.**

```text
PATHS = flat run-root (verifier.verdict.json, verifier.receipt.json)
WRITE_SURFACE = run root only (confirmed)
INSTANCE = canonical, sidecar-pinned
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 interface fact surfaced, §2.2)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**Run 008 passed the evidence-root gate: my independently computed
`e7820ca5…` and Builder A's `declared_root` agree exactly.** Two builders reading
one sealed definition, neither seeing the other's work, converged on the same
digest. That is the custody split paying for itself, and it is worth one line
before moving to the next stop.

## 0. Preflight

| Check | Result |
|---|---|
| Output artifact collision | none — clear to write |
| Builder A's **code** | never listed, opened, or searched |
| Prior instance | `a96b3c9a…` (evidence root bound, paths still package-relative) |

---

## 1. Q1 — THE PATHS

[PROVABLE] The defect was mine and the parent named it correctly.
`verifier/verdict.json` and `verifier/receipt.json` contain a separator, so under
a custodian's run root they resolve into a `verifier/` subdirectory — which is
also the name of my package directory. Corrected to the flat producer-child form:

```text
BEFORE   output_path  = "verifier/verdict.json"      receipt_path = "verifier/receipt.json"
AFTER    output_path  = "verifier.verdict.json"      receipt_path = "verifier.receipt.json"
```

[PROVABLE] Verified mechanically: **neither path contains `/` or the platform
separator**, so neither can resolve into any subdirectory under any run root.
The `verifier.` prefix is a name component, not a directory — which is exactly
the producer-child pattern the parent enforces.

---

## 2. Q2 — THE WRITE SURFACE

### 2.1 The principle, in one line

**A verifier that writes inside its own immutable package would corrupt its next
run's integrity baseline — its `verifier_root_sha256` is a digest over those very
bytes — so the custodian's fresh run root is the only writable surface.**

### 2.2 The confirmation is stronger than the requirement, and one interface fact

[PROVABLE] I checked every write call site in the package rather than reasoning
about intent. **The runtime package opens no file for writing at all:**

```text
the ONLY open() in the runtime package:
    verifier/hashing.py:39      handle = open(path, "rb")        <- READ-ONLY

every write in verify.py:
    :264  sys.stderr.write(...)     fail-closed diagnostics
    :265  sys.stdout.write(...)     the verdict
    :270  sys.stdout.write("\n")
    :273  sys.stdout.write(...)     the verdict
    :274  sys.stdout.write("\n")

no makedirs, no mkdir, no shutil, no remove, no unlink, no rename.
```

So the claim "never into its package" holds **a fortiori**: the verifier cannot
write into its package because it cannot write to disk anywhere. Its entire
output surface is one canonical-JSON line on stdout, with diagnostics on stderr —
which is what `stdout_discipline` already declares.

[YOURS] **The interface fact I am surfacing rather than assuming past.** The task
says "confirm your verifier writes to the argv-substituted paths at run time."
It does not, and I will not report that it does. `argv` carries **no output
token** — there is no `--output` or `--receipt` flag — so the declared
`output_path` and `receipt_path` are **destinations for the parent to place the
captured stdout and the receipt it composes**, not paths the child opens.

I believe that is the right division and I have not changed it: a child that
cannot write anywhere cannot scribble outside its lane, and `stdout_discipline`
exists precisely because the verdict travels on stdout. But if the parent expects
the **child** to write those two files, then this is an interface disagreement,
not a path bug, and the repair would be a new argv token rather than a new path
string. **I state it so the next run tests the right thing.**

---

## 3. Q3 — THE DELTA AND PIN CHECK

### 3.1 Disclosed delta — exactly two files

```text
rd22.verifier-manifest.v001.json              a96b3c9a…  ->  373aff8ca35c5d5db1593d4ca8eb6cee010189b1ac4cc8f8596a9cd12c8154e2
rd22.verifier-manifest.v001.json.seal.sha256  d5515c8e…  ->  (regenerated, verified OK)
```

**No code changed.** Two string fields in the instance; nothing else. The package
remains 17 files.

### 3.2 Pin check

| Claim | Verified before sealing |
|---|---|
| both paths flat | no `/` and no platform separator in either |
| instance canonical | round-trip identical; sorted keys; single line; **no trailing newline** (Q-594 canon) |
| 11 fields | counted from the parsed instance |
| sidecar verifies | `shasum -c` OK, and equals `manifest_sha256()` = `373aff8c…` |
| ledger guard intact | `require_roots_bound` still refuses, naming `ledger_sha256` alone |
| evidence root retained | `e7820ca5…` unchanged — the value run 008 accepted |
| write surface empty | every call site enumerated; the only `open()` is `"rb"` |
| self-check CLEAN, `-O` parity | both executed; output byte-identical |

### 3.3 `F_PLDEC` and coverage

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. **The chain was not invoked.** `alpha_computed = false`;
`proof_authorized = false`; `kappa_record_computed = false`; no member bound; no
fixed point; no end test; no numeric evaluation; no comparison to any measured
constant.

**Coverage, stated exactly:** I changed two string fields, reissued the instance
and sidecar, and enumerated the package's write surface. I claim **no check or
fixture outcome**, and I do **not** claim the next gate will pass — §2.2 names an
interface question that only the run can settle.

---

## 4. SELF VERB AUDIT

| My verb | Check |
|---|---|
| `PATHS = flat run-root` | Both names displayed; flatness verified by separator test, not by inspection. |
| `WRITE_SURFACE = run root only` | Confirmed by enumerating **every** write call site: the package opens no file for writing at all. Stronger than the requirement, and checkable. |
| Interface fact surfaced | The task's premise — that my verifier writes to argv-substituted paths — **is not true of my build**, and I say so rather than let a false confirmation stand. `argv` carries no output token. |
| Delta honesty | Exactly two files; "no code changed" is checkable against the prior digests. |
| Convergence noted, not claimed as mine | Run 008's agreement is a joint result of two independent computations; I record it in one line and move on. |
| `CHAIN_INVOKED = false` | Literally true. |

---

```text
PATHS = flat run-root (+both names: output_path = "verifier.verdict.json",
  receipt_path = "verifier.receipt.json". The prior values contained a separator
  and so resolved into a "verifier/" subdirectory -- which is also my package
  directory name. Flatness verified mechanically: neither path contains "/" or the
  platform separator, so neither can resolve into any subdirectory under any run
  root; the "verifier." prefix is a name component, matching the producer-child
  pattern the parent enforces.)
WRITE_SURFACE = run root only (confirmed, and by a stronger fact than required:
  the runtime package OPENS NO FILE FOR WRITING AT ALL. The only open() is
  verifier/hashing.py:39 open(path,"rb"), read-only; verify.py writes solely to
  sys.stdout (the verdict) and sys.stderr (fail-closed diagnostics); there is no
  makedirs, mkdir, shutil, remove, unlink or rename anywhere. The principle:
  a verifier that wrote inside its own immutable package would corrupt its next
  run's integrity baseline, since verifier_root_sha256 is a digest over those very
  bytes -- so the custodian's fresh run root is the only writable surface.
  INTERFACE FACT SURFACED, NOT ASSUMED PAST: argv carries NO output token, so the
  declared paths are destinations for the PARENT to place captured stdout and the
  receipt it composes, not paths the child opens. If the parent expects the CHILD
  to write them, that is an interface disagreement and the repair is a new argv
  token, not a new path string.)
INSTANCE = canonical, sidecar-pinned (1145 bytes; sorted keys, no insignificant
  whitespace, single line, no trailing newline per the Q-594 canon; 11 fields;
  sha256 373aff8ca35c5d5db1593d4ca8eb6cee010189b1ac4cc8f8596a9cd12c8154e2, equal
  to manifest_sha256(), with its sidecar regenerated and verified OK. The ledger
  guard is intact -- require_roots_bound still refuses, naming ledger_sha256
  alone -- and the evidence root e7820ca5… that run 008 accepted is unchanged.
  DELTA: exactly two files, the instance and its sidecar; NO CODE CHANGED;
  17 files; self-check CLEAN; -O parity byte-identical.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote. No check and
  no fixture has been run; no outcome is claimed; and I do NOT claim the next gate
  will pass -- the interface question at §2.2 can only be settled by the run.)
VERB_AUDIT_SELF = CLEAN (+1 interface fact surfaced rather than confirmed falsely:
  the task's premise that my verifier writes to argv-substituted paths is not true
  of my build, and reporting that it was would have been the easy answer and a
  false one.)
```

Run 008's convergence is the first hard evidence the two-builder split was worth
its cost: two implementations, written without sight of each other, computed the
same content root from the same sealed definition. This relay's fix is small by
comparison — two strings — but the check underneath it is the same discipline:
I did not confirm that my verifier writes where the task assumed it writes. It
writes nowhere, and saying so is more useful than agreeing.
