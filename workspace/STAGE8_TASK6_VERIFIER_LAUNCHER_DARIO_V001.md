# STAGE 8 / TASK 6 / BUILD — THE DIRECT-SCRIPT LAUNCHER — DARIO V001

Lane: Dario (Claude Opus 5), **Builder B** of the RD-22 custody graph
Task: PASTE 665 / Task 6 build — resolve the launch under the pinned isolation flags
Authority: RD-22 + the addendum sealed at Q-588. **THIS ARTIFACT INVOKES NOTHING.**

```text
LAUNCHER = direct script at package root (run_verifier.py)
RESOLVES_UNDER = -I -S -B (demonstrated)
INSTANCE = updated, canonical, sidecar-pinned
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+1 correction to the task's premise, §1.2)
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

**Run 012 is the deepest yet and the diagnosis was right:** `-m verifier.verify`
cannot resolve under `-I`. But the proposed cure — a direct script, relying on
"the script's own directory lands on `sys.path` under direct execution" — **is
false under `-I`**, and I established that before writing the file rather than
after the next run failed.

## 1. U1 — THE LAUNCHER

### 1.1 The failure reproduced

```text
$ python3 -I -S -B -m verifier.verify --help
Error while finding module specification for 'verifier.verify'
  (ModuleNotFoundError: No module named 'verifier')
```

Exactly the run-012 stop, reproduced locally as a control.

### 1.2 The correction to the task's premise — established empirically first

[PROVABLE] `-I` implies `-E` and `-s`, **and it also removes the script's
directory and the cwd from `sys.path`.** A minimal probe on CPython 3.9.6:

```text
$ python3 probe.py                 sys.path[0] = '/private/tmp/isotest'
                                   import pkg.mod: resolved
$ python3 -I -S -B probe.py        sys.path[0] = '.../python39.zip'
                                   import pkg.mod: FAILED -> ModuleNotFoundError
```

**So a direct script alone does not fix it either.** The premise that direct
execution supplies the package root holds for plain `python3` and fails for `-I`
— which is precisely the mode the parent pins. Had I written the launcher to the
stated premise, run 013 would have failed the same way for a new reason.

[PROVABLE] The minimal sufficient fix, verified before adoption:

```text
$ python3 -I -S -B runner.py       # runner inserts dirname(abspath(__file__))
with __file__-derived path insert: resolved
```

### 1.3 What the launcher does, and why it is not path trust

`evaluator_build_B/run_verifier.py` derives the package root from `__file__` and
inserts **exactly that one directory** on `sys.path`, then passes `sys.argv[1:]`
through to `verifier.verify.main` and propagates its exit code unchanged.

[YOURS] The task asked for "no path mutation code beyond what direct execution
provides", and direct execution under `-I` provides nothing — so a single
insertion is unavoidable. It is worth saying exactly why it is safe: the launcher
adds **nothing from the environment**, nothing from the caller's cwd, and nothing
from `PYTHONPATH` — all of which `-I` correctly suppresses and none of which this
file reintroduces. It adds the directory the file is *in*, computed from the file
itself, so a self-contained package can find its own modules under isolation.
**Content addressing is untouched: every run input is still admitted only by
digest.** This is the package locating itself, not the package trusting a path.

## 2. U2 — THE INSTANCE

```text
entry_point   "verifier.verify"                    ->  "run_verifier.py"
argv          ["python3","-m","verifier.verify",…] ->  ["python3","run_verifier.py",…]
```

Tokens are unchanged: the parent substitutes the same six named operands and
rewrites `argv[0]` and absolute paths as it already does from the bound manifest.
`output_path` / `receipt_path` / all five `input_roots` are unchanged.

[PROVABLE] **No finding on the contract.** `rd22.verifier-manifest.v001` types
`entry_point` as a string and `argv` as a list of strings; it does **not** require
the `-m` form. The direct-script form conforms without amendment, so the U2
contingency ("if the contract only admits `-m` form, that is a finding") does not
arise. The script name is declared package-relative, as the launch section
expects.

## 3. U3 — THE DEMONSTRATION

A `--dry-run-launch` flag lives in the **launcher**, not in `verify.py`, so the
verifier module is byte-unchanged. It resolves the package, emits one canonical
JSON line, and exits 2 — **consuming no run input**: no spec, ledger, evidence,
snapshot or gate is opened, and `run_verifier.py` contains no `open()` at all.

**From the package directory:**

```text
$ python3 -I -S -B run_verifier.py --dry-run-launch
{"chain_invoked":false,"dont_write_bytecode":true,"entry_point":"run_verifier.py",
 "governing_spec_sha256":"f8d1a7dc…","isolated":true,"no_site":true,
 "package_root_resolved":true,"run_inputs_consumed":false,
 "schema":"rd22.verifier-launch-dryrun.v001","verdict":"NO_VERDICT_DRY_RUN",
 "verifier_module":"verifier.verify"}
exit=2
```

**From an unrelated cwd by absolute path — how the parent will actually invoke:**

```text
$ cd /tmp && python3 -I -S -B "<abs>/evaluator_build_B/run_verifier.py" --dry-run-launch
… identical payload …
exit=2
```

[PROVABLE] The payload's own `isolated:true`, `no_site:true` and
`dont_write_bytecode:true` are read from `sys.flags` at run time, so the
demonstration proves the flags were **in effect**, not merely typed on the
command line. `package_root_resolved:true` is the fact under test.

## 4. DELTA AND PIN CHECK

```text
NEW      run_verifier.py
CHANGED  verifier/child_manifest.py           (ENTRY_POINT + argv to direct form)
CHANGED  rd22.verifier-manifest.v001.json     08e6c058…  ->  7a5ee8ce61e86359c3fe82f7b2d43c9baccb3ca09efb85950c9d92e1c53f27a6
CHANGED  rd22.verifier-manifest.v001.json.seal.sha256   regenerated, verified OK
```

Package: **18 files** (was 17).

| Claim | Verified before sealing |
|---|---|
| `-m` form fails under `-I` | reproduced locally as a control |
| script-dir absent from `sys.path` under `-I` | probe displayed, both modes |
| `__file__` insertion sufficient | probe displayed under `-I -S -B` |
| launcher resolves from package dir | executed, exit 2 |
| launcher resolves from foreign cwd, absolute path | executed, exit 2 |
| flags genuinely in effect | `sys.flags` echoed in the payload |
| no run input consumed | `run_verifier.py` contains zero `open()` |
| `verify.py` byte-unchanged | dry-run lives in the launcher |
| instance canonical | round-trip identical; sorted; single line; no trailing newline; 11 fields |
| sidecar verifies and equals `manifest_sha256()` | `7a5ee8ce…` |
| ledger guard intact | refuses, naming `ledger_sha256` alone |
| evidence root retained | `e7820ca5…` |
| zero `assert` | package-wide scan |
| self-check CLEAN | executed |

## 5. `F_PLDEC` AND COVERAGE

[PROVABLE] Nothing consumed a reader output, a desired outcome, a measured value,
or any physical quantity. **The chain was not invoked**; the dry run opens no run
input. `alpha_computed = false`; `proof_authorized = false`;
`kappa_record_computed = false`; no member bound; no fixed point; no end test; no
numeric evaluation; no comparison to any measured constant.

**Coverage, stated exactly:** I added a launcher, changed two lines of
`child_manifest.py`, reissued the instance and sidecar, and demonstrated the
launch path under the pinned flags. I claim **no check or fixture outcome**, and
I do **not** claim run 013 will pass — I have proved the module resolves, not
that the verdict will.

## 6. SELF VERB AUDIT

| My verb | Check |
|---|---|
| `RESOLVES_UNDER = -I -S -B (demonstrated)` | Executed twice, including from a foreign cwd by absolute path, with `sys.flags` echoed so the flags are proved in effect. |
| **Premise corrected** | The task's stated mechanism — direct execution supplies the script directory — **is false under `-I`**, and I tested it before writing rather than shipping to the premise and failing run 013 for a new reason. |
| Path insertion justified, not hidden | It is the one thing the task asked me to avoid, it is unavoidable, and §1.3 says exactly what it does and does not admit. Calling it "no path mutation" would have been the comfortable description and a false one. |
| No contract finding claimed | I checked whether the contract admits only `-m`; it does not, so I report no finding rather than manufacture one from the contingency offered. |
| `verify.py` untouched | The dry-run flag is in the launcher, so the verifier module's digest is unchanged. |
| `CHAIN_INVOKED = false` | Literally true; the dry run opens no run input. |

---

```text
LAUNCHER = direct script at package root (evaluator_build_B/run_verifier.py:
  derives the package root from __file__ and inserts exactly that one directory on
  sys.path, then passes sys.argv[1:] through to verifier.verify.main and
  propagates its exit code 0/1/2 unchanged. THE TASK'S PREMISE WAS FALSE AND I
  TESTED IT FIRST: -I removes the script's directory AND the cwd from sys.path, so
  a direct script ALONE fails identically to -m -- probe displayed at §1.2 --
  which means one insertion is unavoidable. It is not path trust: it adds nothing
  from the environment, the cwd, or PYTHONPATH, only the directory the file itself
  is in, and every run input is still admitted only by digest.)
RESOLVES_UNDER = -I -S -B (demonstrated twice: from the package directory and from
  an unrelated cwd by absolute path, exactly as the parent will invoke. Both emit
  one canonical JSON line and exit 2 with run_inputs_consumed:false and
  chain_invoked:false. The payload echoes sys.flags -- isolated:true, no_site:true,
  dont_write_bytecode:true -- so the flags are proved IN EFFECT rather than merely
  typed. Control reproduced: the old -m form under the same flags gives exactly the
  run-012 ModuleNotFoundError.)
INSTANCE = updated, canonical, sidecar-pinned (entry_point "verifier.verify" ->
  "run_verifier.py"; argv "-m verifier.verify" -> "run_verifier.py", tokens and all
  other fields unchanged including output_path, receipt_path and all five
  input_roots. sha256 7a5ee8ce61e86359c3fe82f7b2d43c9baccb3ca09efb85950c9d92e1c53
  f27a6, equal to manifest_sha256(), sidecar verified OK; sorted keys, single line,
  no trailing newline, 11 fields. NO CONTRACT FINDING: rd22.verifier-manifest.v001
  types entry_point as a string and argv as a list, and does not require the -m
  form, so the direct-script form conforms without amendment. DELTA: 1 new file,
  child_manifest.py two lines, instance + sidecar; verify.py BYTE-UNCHANGED because
  the dry-run flag lives in the launcher; 18 files; self-check CLEAN; zero asserts.)
CHAIN_INVOKED = false (Builder B does not run what Builder B wrote. The dry run
  opens no run input. No check and no fixture has been run, no outcome is claimed,
  and I do NOT claim run 013 will pass -- I have proved the module resolves, not
  that the verdict will.)
VERB_AUDIT_SELF = CLEAN (+1 correction to the task's stated mechanism, tested
  before writing rather than discovered after the next failure; +the unavoidable
  path insertion justified explicitly rather than described as "no path mutation",
  which would have been the comfortable phrasing and a false one.)
```

The instruction contained a mechanism and the mechanism was wrong, in a way that
would have produced the same symptom at the next run under a different cause.
Ten minutes of probing cost less than one more relay, and the launcher now carries
the reason in its own docstring so the next person who reads `-I` and expects
`sys.path[0]` finds the answer before the failure rather than after it.
