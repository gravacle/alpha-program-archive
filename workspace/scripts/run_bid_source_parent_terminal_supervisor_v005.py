#!/usr/bin/env python3
"""Fresh parent supervisor for the source-parent SP14 runtime gate."""

from __future__ import annotations

import _imp
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import subprocess
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
PROGRAM = Path(__file__).resolve()
RUNTIME = PROJECT_ROOT / "provenance" / "primitive_step6_runtime_snapshot_v014.json"
LAUNCHER = PROJECT_ROOT / "scripts" / "launch_content_addressed_runtime_script_v014.py"
ALIAS_TEST = (
    PROJECT_ROOT / "tests" / "test_content_addressed_runtime_source_namespace_alias_v002.py"
)
PRODUCER_BUILDER = (
    ROOT / "scripts" / "build_bid_source_parent_terminal_producer_manifests_v005.py"
)
VERIFIER_BUILDER = (
    ROOT / "scripts" / "build_bid_source_parent_terminal_verifier_manifest_v005.py"
)
NORMAL_MANIFEST = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_terminal_producer_normal_v005_execution_manifest.json"
)
OPTIMIZED_MANIFEST = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_terminal_producer_optimized_v005_execution_manifest.json"
)
VERIFIER_MANIFEST = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_terminal_children_verifier_v005_execution_manifest.json"
)
TERMINAL = PROJECT_ROOT / "results" / "bid_source_parent_sp14_terminal_v005.json"
SIGNATURE = PROJECT_ROOT / "results" / "bid_source_parent_sp14_terminal_v005.json.asc"
GPG = Path("/opt/homebrew/bin/gpg")
SIGNER = "18488605D44F65A9B57B610AA5F3A86512A04D61"
V003_FAILURE_RECORD = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_sp14_terminal_v003_failure_record.json"
)
V003_FAILURE_SEAL = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_sp14_terminal_v003_failure_record.seal.sha256"
)
V003_FAILURE_RECORD_SHA256 = (
    "4195917299558acd17b5c94c64d8e1b33a440d7c32db578a143b9319c07407c6"
)
V003_FAILURE_SEAL_SHA256 = (
    "1465596364b659f6bfaf86f1501441669cdf03ab1de2c78e628d961a8557f627"
)
BUILTIN_CHILD_MODULE_ALIASES = frozenset(
    {
        ("pyexpat.errors", "pyexpat", "errors"),
        ("pyexpat.model", "pyexpat", "model"),
    }
)
SEALED_MODULE_REEXPORT_ALIASES = frozenset(
    {
        (
            "xml.parsers.expat.errors",
            "xml.parsers.expat",
            "errors",
            "pyexpat.errors",
            "pyexpat",
            "errors",
        ),
        (
            "xml.parsers.expat.model",
            "xml.parsers.expat",
            "model",
            "pyexpat.model",
            "pyexpat",
            "model",
        ),
    }
)
BASE_MODULE_KEYS = {
    "module",
    "origin",
    "loader_origin",
    "cached_origin",
    "cached_file_exists",
    "sha256",
    "classification",
    "causal_provenance",
}
FILE_MODULE_NAME_ALIASES = frozenset(
    {
        ("_frozen_importlib", "importlib._bootstrap"),
        ("_frozen_importlib_external", "importlib._bootstrap_external"),
        ("os.path", "posixpath"),
    }
)
TRANSIENT_EVENTS = [
    {"event": "os.putenv", "key": "OPENBLAS_MAIN_FREE", "value": "1"},
    {"event": "os.putenv", "key": "GOTOBLAS_MAIN_FREE", "value": "1"},
    {"event": "os.unsetenv", "key": "OPENBLAS_MAIN_FREE", "value": None},
    {"event": "os.unsetenv", "key": "GOTOBLAS_MAIN_FREE", "value": None},
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha(value: Any) -> str:
    data = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError(f"duplicate JSON key: {key}")
        output[key] = value
    return output


def finite(value: Any, label: str) -> None:
    if isinstance(value, float) and not math.isfinite(value):
        raise RuntimeError(f"non-finite value at {label}")
    if isinstance(value, dict):
        for key, item in value.items():
            finite(item, f"{label}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            finite(item, f"{label}[{index}]")


def strict_json(path: Path) -> dict[str, Any]:
    value = json.loads(
        path.read_text(encoding="utf-8"),
        parse_constant=lambda item: (_ for _ in ()).throw(
            ValueError(f"forbidden JSON constant: {item}")
        ),
        object_pairs_hook=reject_duplicate_keys,
    )
    if not isinstance(value, dict):
        raise RuntimeError(f"{path} is not a JSON object")
    finite(value, str(path))
    return value


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(PROJECT_ROOT.resolve()))


def validate_preserved_failure_lineage() -> dict[str, str]:
    require(
        V003_FAILURE_RECORD.is_file() and V003_FAILURE_SEAL.is_file(),
        "preserved v003 failure lineage is absent",
    )
    record_hash = sha256(V003_FAILURE_RECORD)
    seal_hash = sha256(V003_FAILURE_SEAL)
    require(
        record_hash == V003_FAILURE_RECORD_SHA256
        and seal_hash == V003_FAILURE_SEAL_SHA256
        and V003_FAILURE_SEAL.read_text(encoding="utf-8").strip()
        == f"{V003_FAILURE_RECORD_SHA256}  {V003_FAILURE_RECORD.name}",
        "preserved v003 failure lineage changed",
    )
    return {
        "record": relative(V003_FAILURE_RECORD),
        "record_sha256": record_hash,
        "seal": relative(V003_FAILURE_SEAL),
        "seal_sha256": seal_hash,
    }


def file_manifest(root: Path, excluded: Path | None = None) -> dict[str, str]:
    output: dict[str, str] = {}
    excluded_path = excluded.resolve() if excluded else None
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix == ".pyc" or "__pycache__" in path.parts:
            continue
        resolved = path.resolve()
        if excluded_path and (
            resolved == excluded_path or excluded_path in resolved.parents
        ):
            continue
        output[str(path.relative_to(root))] = sha256(path)
    return output


def current_trust() -> dict[str, str]:
    sw_vers = subprocess.run(
        ["/usr/bin/sw_vers"], check=True, text=True, capture_output=True
    ).stdout
    csrutil = subprocess.run(
        ["/usr/bin/csrutil", "status"], check=False, text=True, capture_output=True
    ).stdout
    return {
        "policy": (
            "SIP-protected dyld shared cache and System Library paths are a "
            "revalidated mutable host trust base; every non-system loaded "
            "native image must be a hashed runtime file"
        ),
        "machine": platform.machine(),
        "platform": platform.platform(),
        "sw_vers": sw_vers,
        "csrutil_status": csrutil,
    }


def allowed_runtime_files(runtime: dict[str, Any]) -> dict[str, str]:
    output: dict[str, str] = {}
    for root_key, files_key in (
        ("python_runtime_root", "python_runtime_files"),
        ("bundled_site_packages_root", "bundled_site_packages_files"),
        ("workspace_site_packages_root", "workspace_site_packages_files"),
    ):
        base = Path(runtime[root_key])
        for name, digest in runtime[files_key].items():
            output[str((base / name).resolve())] = digest
    output[str(Path(runtime["python_executable"]).resolve())] = runtime[
        "python_executable_sha256"
    ]
    output[str(Path(runtime["libpython_path"]).resolve())] = runtime["libpython_sha256"]
    return output


def validate_runtime() -> tuple[dict[str, Any], dict[str, str]]:
    runtime = strict_json(RUNTIME)
    require(runtime.get("schema") == "gravacle.content-addressed-runtime.v014", "runtime schema")
    require(runtime.get("alpha_computed") is False, "runtime alpha firewall")
    require(runtime.get("required_flags") == ["-I", "-S", "-B"], "runtime flags")
    require(runtime.get("allowed_optimization_levels") == [0, 1], "runtime optimize")
    require(runtime.get("native_system_trust_root") == current_trust(), "host trust changed")
    launcher = Path(runtime["launcher_path"]).resolve()
    builder = Path(runtime["builder_path"]).resolve()
    gate = Path(runtime["gate_path"]).resolve()
    for path, expected in (
        (launcher, runtime["launcher_sha256"]),
        (builder, runtime["builder_sha256"]),
        (gate, runtime["gate_sha256"]),
        (Path(runtime["python_executable"]), runtime["python_executable_sha256"]),
        (Path(runtime["libpython_path"]), runtime["libpython_sha256"]),
    ):
        require(path.is_file() and sha256(path) == expected, f"runtime input changed: {path}")
    expected_trees = {
        "python": runtime["python_runtime_files"],
        "bundled": runtime["bundled_site_packages_files"],
        "workspace": runtime["workspace_site_packages_files"],
    }
    actual_trees = {
        "python": file_manifest(
            Path(runtime["python_runtime_root"]),
            excluded=Path(runtime["bundled_site_packages_root"]),
        ),
        "bundled": file_manifest(Path(runtime["bundled_site_packages_root"])),
        "workspace": file_manifest(Path(runtime["workspace_site_packages_root"])),
    }
    require(actual_trees == expected_trees, "runtime tree changed")
    pycache = Path(runtime["source_only_pycache_root"])
    require(pycache.is_dir() and not any(pycache.iterdir()), "runtime cache is not empty")
    return runtime, allowed_runtime_files(runtime)


def run_python(
    runtime: dict[str, Any], script: Path, args: list[Path] | None = None, optimize: int = 0
) -> subprocess.CompletedProcess[str]:
    pycache = runtime["source_only_pycache_root"]
    command = [
        runtime["python_executable"],
        "-I",
        "-S",
        "-B",
        "-X",
        f"pycache_prefix={pycache}",
    ]
    if optimize:
        command.append("-O")
    command.append(str(script.resolve()))
    command.extend(str(path.resolve()) for path in (args or []))
    result = subprocess.run(command, check=False, text=True, capture_output=True, env={})
    if result.returncode:
        raise RuntimeError(
            "isolated child failed\n"
            f"command={command!r}\n"
            f"stdout={result.stdout}\n"
            f"stderr={result.stderr}"
        )
    return result


def validate_contract(output: dict[str, Any], contract: dict[str, Any]) -> None:
    required = contract.get("required_fields")
    require(isinstance(required, list) and set(output) == set(required), "output inventory")
    for key, expected in contract.get("exact_values", {}).items():
        require(output.get(key) == expected, f"output contract mismatch: {key}")
    checks = output.get("checks")
    expected_checks = contract.get("required_check_keys")
    require(
        isinstance(checks, dict)
        and isinstance(expected_checks, list)
        and set(checks) == set(expected_checks)
        and all(value is True for value in checks.values()),
        "output checks mismatch",
    )


def validate_causal(
    causal: Any, module_names: set[str], allowed: dict[str, str]
) -> None:
    require(isinstance(causal, dict), "module causal provenance absent")
    kind = causal.get("kind")
    if kind == "direct_launcher_baseline":
        require(set(causal) == {"kind"}, "baseline causal row malformed")
        return
    require(
        kind == "sealed_loader_transaction"
        and set(causal) == {"kind", "creator", "creator_origin", "phase"}
        and causal.get("creator") in module_names
        and causal.get("phase") in {"create_module", "exec_module"},
        "loader causal row malformed",
    )
    origin = causal.get("creator_origin")
    if origin in {"built-in", "frozen"}:
        return
    require(isinstance(origin, str), "causal creator origin malformed")
    path = Path(origin).resolve()
    require(
        allowed.get(str(path)) is not None
        and path.is_file()
        and sha256(path) == allowed[str(path)],
        "causal creator is not sealed",
    )


def validate_live_source_namespace_alias(
    row: dict[str, Any], allowed: dict[str, str]
) -> None:
    """Independently reconstruct a reported alias in the fresh parent."""

    name = row.get("module")
    parent_name = row.get("sealed_parent_module")
    attribute = row.get("sealed_parent_attribute")
    require(
        isinstance(name, str)
        and isinstance(parent_name, str)
        and isinstance(attribute, str),
        "source-namespace alias identity fields malformed",
    )
    parent = sys.modules.get(parent_name)
    module = sys.modules.get(name)
    require(
        parent is not None
        and module is not None
        and getattr(parent, attribute, object()) is module,
        "source-namespace alias absent from fresh-parent live reconstruction",
    )
    namespace = getattr(module, "__dict__", None)
    exports = namespace.get("__all__") if hasattr(namespace, "get") else None
    require(
        isinstance(module, type)
        and getattr(module, "__name__", None) == name
        and getattr(module, "__module__", None) == parent_name
        and getattr(module, "__spec__", None) is None
        and getattr(module, "__file__", None) is None
        and getattr(module, "__loader__", None) is None
        and getattr(module, "__package__", None) is None
        and type(namespace) is type(type.__dict__)
        and isinstance(exports, (list, tuple))
        and bool(exports),
        "source-namespace alias fresh-parent shape false",
    )
    alias_type = type(module)
    require(
        alias_type.__module__ == parent_name
        and getattr(parent, alias_type.__name__, None) is alias_type,
        "source-namespace alias fresh-parent metaclass provenance false",
    )
    parent_spec = getattr(parent, "__spec__", None)
    parent_origin = getattr(parent_spec, "origin", None) or getattr(
        parent, "__file__", None
    )
    require(isinstance(parent_origin, str), "fresh-parent alias origin absent")
    parent_path = Path(parent_origin).resolve()
    parent_digest = row.get("sealed_parent_sha256")
    require(
        allowed.get(str(parent_path)) == parent_digest
        and parent_path.is_file()
        and sha256(parent_path) == parent_digest,
        "fresh-parent alias parent is not sealed",
    )
    expected_keys = {
        "__module__",
        "__doc__",
        "__dict__",
        "__weakref__",
        "__all__",
        *exports,
    }
    require(
        set(namespace) == expected_keys
        and all(
            namespace.get(exported, object()) is getattr(parent, exported, None)
            for exported in exports
        ),
        "source-namespace alias fresh-parent export identity false",
    )
    require(
        row.get("sealed_parent_origin") == str(parent_path)
        and row.get("alias_type")
        == f"{alias_type.__module__}.{alias_type.__qualname__}"
        and row.get("namespace_exports") == sorted(exports),
        "source-namespace alias receipt differs from fresh-parent reconstruction",
    )


def canonical_module_name_for_file(path: Path) -> str:
    leaf = path.name
    if leaf == "__init__.py":
        parts = [path.parent.name]
        parent = path.parent.parent
    else:
        stem = leaf[:-3] if leaf.endswith(".py") else leaf.split(".", 1)[0]
        parts = [stem]
        parent = path.parent
    while (parent / "__init__.py").is_file():
        parts.append(parent.name)
        parent = parent.parent
    return ".".join(reversed(parts))


def validate_file_backed_module_name(row: dict[str, Any], path: Path) -> None:
    name = row.get("module")
    require(isinstance(name, str) and bool(name), "file-backed module name malformed")
    if name == "__main__":
        require(
            row.get("classification") == "sealed_file"
            and row.get("causal_provenance", {}).get("kind")
            == "direct_launcher_baseline",
            "file-backed __main__ row is not the direct launcher baseline",
        )
        return
    canonical = canonical_module_name_for_file(path)
    require(
        name == canonical or (name, canonical) in FILE_MODULE_NAME_ALIASES,
        "file-backed module name does not follow from its sealed origin",
    )


def validate_modules(rows: Any, allowed: dict[str, str]) -> None:
    require(isinstance(rows, list) and bool(rows), "module inventory absent")
    require(all(isinstance(row, dict) for row in rows), "malformed module row")
    names = [row.get("module") for row in rows]
    require(names == sorted(set(names)), "module names not unique/sorted")
    by_name = {row["module"]: row for row in rows}
    for row in rows:
        validate_causal(row.get("causal_provenance"), set(by_name), allowed)
        kind = row.get("classification")
        origin = row.get("origin")
        digest = row.get("sha256")
        require(row.get("cached_file_exists") is False, "executed cache reported")
        if kind in {"sealed_file", "sealed_originless_source"}:
            require(
                set(row) == BASE_MODULE_KEYS
                and isinstance(origin, str)
                and isinstance(digest, str),
                "sealed module fields",
            )
            path = Path(origin).resolve()
            require(
                allowed.get(str(path)) == digest
                and path.is_file()
                and path.suffix != ".pyc"
                and sha256(path) == digest,
                "sealed module bytes not independently bound",
            )
            validate_file_backed_module_name(row, path)
        elif kind == "sealed_interpreter_builtin":
            require(
                origin == "built-in"
                and row.get("loader_origin") == "built-in"
                and digest is None
                and _imp.is_builtin(row["module"]) != 0,
                "builtin classification false",
            )
        elif kind == "sealed_interpreter_frozen":
            require(
                origin == "frozen"
                and row.get("loader_origin") == "frozen"
                and digest is None
                and _imp.is_frozen(row["module"]),
                "frozen classification false",
            )
        elif kind == "sealed_builtin_parent_module_alias":
            require(
                set(row)
                == BASE_MODULE_KEYS
                | {
                    "sealed_parent_module",
                    "sealed_parent_origin",
                    "sealed_parent_attribute",
                    "alias_type",
                },
                "builtin-parent alias field inventory changed",
            )
            parent_name = row.get("sealed_parent_module")
            attribute = row.get("sealed_parent_attribute")
            parent = by_name.get(parent_name)
            causal = row.get("causal_provenance")
            require(
                origin is None
                and digest is None
                and row.get("loader_origin") is None
                and row.get("cached_origin") is None
                and row.get("sealed_parent_origin") == "built-in"
                and row.get("alias_type") == "builtins.module"
                and (row["module"], parent_name, attribute)
                in BUILTIN_CHILD_MODULE_ALIASES
                and parent is not None
                and parent.get("origin") == "built-in"
                and _imp.is_builtin(str(parent_name)) != 0
                and isinstance(causal, dict)
                and (
                    causal.get("kind") == "direct_launcher_baseline"
                    or causal.get("creator") == parent_name
                    and causal.get("creator_origin") == "built-in"
                    and causal.get("phase") in {"create_module", "exec_module"}
                ),
                "builtin-parent module alias classification false",
            )
        elif kind == "sealed_module_reexport_alias":
            require(
                set(row)
                == BASE_MODULE_KEYS
                | {
                    "sealed_parent_module",
                    "sealed_parent_origin",
                    "sealed_parent_sha256",
                    "sealed_parent_attribute",
                    "canonical_module",
                    "canonical_parent_module",
                    "canonical_parent_attribute",
                    "alias_type",
                },
                "module re-export alias field inventory changed",
            )
            parent_name = row.get("sealed_parent_module")
            parent_attribute = row.get("sealed_parent_attribute")
            parent = by_name.get(parent_name)
            parent_origin = row.get("sealed_parent_origin")
            parent_digest = row.get("sealed_parent_sha256")
            canonical_name = row.get("canonical_module")
            canonical = by_name.get(canonical_name)
            canonical_parent_name = row.get("canonical_parent_module")
            canonical_parent_attribute = row.get("canonical_parent_attribute")
            canonical_parent = by_name.get(canonical_parent_name)
            require(
                origin is None
                and digest is None
                and row.get("loader_origin") is None
                and row.get("cached_origin") is None
                and row.get("alias_type") == "builtins.module"
                and (
                    row["module"],
                    parent_name,
                    parent_attribute,
                    canonical_name,
                    canonical_parent_name,
                    canonical_parent_attribute,
                )
                in SEALED_MODULE_REEXPORT_ALIASES
                and parent is not None
                and isinstance(parent_origin, str)
                and parent.get("origin") == parent_origin
                and parent.get("sha256") == parent_digest
                and allowed.get(str(Path(parent_origin).resolve())) == parent_digest
                and canonical is not None
                and canonical.get("classification")
                == "sealed_builtin_parent_module_alias"
                and canonical_parent is not None
                and canonical_parent.get("origin") == "built-in"
                and _imp.is_builtin(str(canonical_parent_name)) != 0,
                "sealed module re-export classification false",
            )
        elif kind == "sealed_source_namespace_alias":
            require(
                set(row)
                == BASE_MODULE_KEYS
                | {
                    "sealed_parent_module",
                    "sealed_parent_origin",
                    "sealed_parent_sha256",
                    "sealed_parent_attribute",
                    "alias_type",
                    "namespace_exports",
                },
                "source-namespace alias field inventory changed",
            )
            parent_name = row.get("sealed_parent_module")
            parent = by_name.get(parent_name)
            parent_origin = row.get("sealed_parent_origin")
            parent_digest = row.get("sealed_parent_sha256")
            parent_attribute = row.get("sealed_parent_attribute")
            alias_type = row.get("alias_type")
            exports = row.get("namespace_exports")
            prefix, separator, suffix = str(row.get("module")).rpartition(".")
            causal = row.get("causal_provenance")
            require(
                origin is None
                and digest is None
                and row.get("loader_origin") is None
                and row.get("cached_origin") is None
                and parent is not None
                and parent.get("origin") == parent_origin
                and parent.get("sha256") == parent_digest
                and isinstance(parent_origin, str)
                and allowed.get(str(Path(parent_origin).resolve())) == parent_digest,
                "source-namespace alias parent binding false",
            )
            require(
                separator
                and prefix == parent_name
                and suffix == parent_attribute
                and isinstance(alias_type, str)
                and alias_type.startswith(f"{parent_name}.")
                and isinstance(exports, list)
                and bool(exports)
                and exports == sorted(set(exports))
                and all(isinstance(item, str) and item for item in exports)
                and isinstance(causal, dict)
                and causal.get("kind") == "sealed_loader_transaction"
                and causal.get("creator") == parent_name
                and causal.get("creator_origin") == parent_origin
                and causal.get("phase") == "exec_module",
                "source-namespace alias causal structure false",
            )
            validate_live_source_namespace_alias(row, allowed)
        elif kind == "sealed_native_empty_runtime_module":
            causal = row.get("causal_provenance")
            require(
                row.get("module") == "cython_runtime"
                and origin is None
                and digest is None
                and isinstance(causal, dict)
                and causal.get("kind") == "sealed_loader_transaction",
                "empty native runtime classification false",
            )
        elif kind == "sealed_native_generated_runtime_module":
            references = row.get("sealed_native_export_references")
            require(origin is None and isinstance(references, list) and bool(references), "native generated row")
            for reference in references:
                path = Path(reference["origin"]).resolve()
                require(
                    allowed.get(str(path)) == reference.get("sha256")
                    and sha256(path) == reference.get("sha256"),
                    "native generated exporter not sealed",
                )
        else:
            raise RuntimeError(f"unknown module classification: {kind!r}")


def validate_originless_alias_negative_controls(
    rows: list[dict[str, Any]], allowed: dict[str, str]
) -> None:
    candidates = []
    for kind in (
        "sealed_builtin_parent_module_alias",
        "sealed_module_reexport_alias",
        "sealed_source_namespace_alias",
    ):
        index = next(
            (i for i, row in enumerate(rows) if row.get("classification") == kind),
            None,
        )
        require(index is not None, f"negative-control cohort absent: {kind}")
        candidates.append(index)
    for index in candidates:
        for field, value in (
            ("module", "totally.unrelated"),
            ("sealed_parent_module", "sys"),
            ("loader_origin", "forged-loader"),
        ):
            mutated = [dict(row) for row in rows]
            mutated[index][field] = value
            try:
                validate_modules(mutated, allowed)
            except RuntimeError:
                continue
            raise RuntimeError(f"originless alias negative control survived: {field}")
        if rows[index].get("classification") == "sealed_source_namespace_alias":
            for field, value in (
                ("alias_type", "forged.ParentType"),
                ("namespace_exports", ["forged_export"]),
                ("sealed_parent_sha256", "0" * 64),
            ):
                mutated = [dict(row) for row in rows]
                mutated[index][field] = value
                try:
                    validate_modules(mutated, allowed)
                except RuntimeError:
                    continue
                raise RuntimeError(
                    f"source-namespace live negative control survived: {field}"
                )
            mutated = [dict(row) for row in rows]
            mutated[index]["causal_provenance"] = {
                "kind": "direct_launcher_baseline"
            }
            try:
                validate_modules(mutated, allowed)
            except RuntimeError:
                pass
            else:
                raise RuntimeError("source-namespace baseline-alias control survived")
            source = rows[index]
            for downgraded_kind in ("sealed_file", "sealed_originless_source"):
                downgraded = {
                    key: source.get(key)
                    for key in BASE_MODULE_KEYS
                }
                downgraded.update(
                    {
                        "module": f"{source['sealed_parent_module']}.forged",
                        "origin": source["sealed_parent_origin"],
                        "loader_origin": source["sealed_parent_origin"],
                        "sha256": source["sealed_parent_sha256"],
                        "classification": downgraded_kind,
                    }
                )
                mutated = [dict(row) for row in rows]
                mutated[index] = downgraded
                mutated.sort(key=lambda row: row["module"])
                try:
                    validate_modules(mutated, allowed)
                except RuntimeError:
                    continue
                raise RuntimeError(
                    f"source-namespace classification downgrade survived: "
                    f"{downgraded_kind}"
                )
        causal = dict(rows[index]["causal_provenance"])
        if causal.get("kind") == "sealed_loader_transaction":
            causal["phase"] = "forged-phase"
            mutated = [dict(row) for row in rows]
            mutated[index]["causal_provenance"] = causal
            try:
                validate_modules(mutated, allowed)
            except RuntimeError:
                continue
            raise RuntimeError("originless alias wrong-phase negative control survived")


def validate_native_images(rows: Any, runtime_allowed: dict[str, str]) -> None:
    require(isinstance(rows, list) and bool(rows), "native-image inventory absent")
    seen: set[str] = set()
    for row in rows:
        require(isinstance(row, dict), "malformed native-image row")
        path_text = row.get("path")
        require(isinstance(path_text, str) and Path(path_text).is_absolute(), "native path")
        path = Path(path_text).resolve()
        key = str(path)
        require(key not in seen, "duplicate native image")
        seen.add(key)
        kind = row.get("classification")
        if kind == "sealed_file":
            require(
                path.is_file()
                and row.get("exists_as_file") is True
                and runtime_allowed.get(key) == row.get("sha256")
                and sha256(path) == row.get("sha256"),
                "native runtime image not sealed",
            )
        elif kind == "system_trust_root":
            require(
                path.is_file()
                and row.get("exists_as_file") is True
                and key.startswith(("/System/Library/", "/usr/lib/"))
                and sha256(path) == row.get("sha256"),
                "system image not revalidated",
            )
        elif kind == "SIP_dyld_shared_cache_trust_root":
            require(
                row.get("exists_as_file") is False
                and row.get("sha256") is None
                and key.startswith(("/System/Library/", "/usr/lib/")),
                "dyld-cache image outside revalidated host scope",
            )
        else:
            raise RuntimeError(f"unknown native classification: {kind!r}")


def request_writes(row: dict[str, Any]) -> bool:
    mode = row.get("mode")
    flags = row.get("flags")
    if isinstance(mode, str) and any(marker in mode for marker in ("w", "a", "x", "+")):
        return True
    if isinstance(flags, int):
        return bool(
            flags
            & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND)
        )
    return False


def validate_open_events(
    rows: Any,
    allowed: dict[str, str],
    output: Path,
    receipt: Path,
    pycache: Path,
) -> None:
    require(isinstance(rows, list) and bool(rows), "open-event inventory absent")
    writable = {str(output.resolve()), str(receipt.resolve())}
    writes: set[str] = set()
    system_roots = (Path("/System/Library"), Path("/usr/lib"))
    for row in rows:
        require(isinstance(row, dict), "malformed open-event row")
        path_text = row.get("path")
        require(isinstance(path_text, str) and Path(path_text).is_absolute(), "open path")
        path = Path(path_text).resolve()
        write = request_writes(row)
        require(row.get("write_mode") is write, "open-event classification false")
        if write:
            require(str(path) in writable, "child wrote outside sealed outputs")
            writes.add(str(path))
        else:
            trusted_system = any(root == path or root in path.parents for root in system_roots)
            require(
                str(path) in allowed
                or str(path) in writable
                or trusted_system
                or path == pycache.resolve()
                or pycache.resolve() in path.parents,
                f"child read an unsealed file: {path}",
            )
    require(writes == writable, "exclusive output writes not fully observed")


def validate_manifest(manifest_path: Path, runtime: dict[str, Any], optimize: int) -> dict[str, Any]:
    manifest = strict_json(manifest_path)
    require(
        manifest.get("preserved_failure_lineage")
        == validate_preserved_failure_lineage(),
        "manifest does not bind the preserved v003 failure lineage",
    )
    require(manifest.get("schema") == "gravacle.sealed-target-execution.v002", "manifest schema")
    require(manifest.get("python_optimize") == optimize, "manifest optimize")
    require(manifest.get("alpha_computed") is False, "manifest alpha firewall")
    require(manifest.get("runtime_snapshot") == relative(RUNTIME), "manifest runtime path")
    require(manifest.get("runtime_snapshot_sha256") == sha256(RUNTIME), "manifest runtime hash")
    files = manifest.get("files")
    require(isinstance(files, dict) and bool(files), "manifest file inventory")
    for name, expected in files.items():
        path = (PROJECT_ROOT / name).resolve()
        path.relative_to(PROJECT_ROOT.resolve())
        require(path.is_file() and sha256(path) == expected, f"manifest input changed: {name}")
    require(files.get(relative(PROGRAM)) == sha256(PROGRAM), "supervisor not pre-frozen")
    target = (PROJECT_ROOT / manifest["target_script"]).resolve()
    require(files.get(relative(target)) == sha256(target), "target not pre-frozen")
    require(
        files.get(relative(V003_FAILURE_RECORD)) == V003_FAILURE_RECORD_SHA256
        and files.get(relative(V003_FAILURE_SEAL)) == V003_FAILURE_SEAL_SHA256,
        "manifest file inventory omits the preserved v003 failure lineage",
    )
    return manifest


def validate_child(
    manifest_path: Path,
    runtime: dict[str, Any],
    runtime_allowed: dict[str, str],
    optimize: int,
) -> tuple[dict[str, Any], dict[str, str]]:
    manifest = validate_manifest(manifest_path, runtime, optimize)
    output_path = (PROJECT_ROOT / manifest["expected_output"]).resolve()
    receipt_path = (PROJECT_ROOT / manifest["execution_receipt"]).resolve()
    output = strict_json(output_path)
    validate_contract(output, manifest["output_contract"])
    require(output.get("alpha_computed") is False, "child output alpha firewall")
    receipt = strict_json(receipt_path)
    require(
        receipt.get("schema") == "gravacle.sealed-target-child-execution-record.v014"
        and receipt.get("status") == "CHILD_LOCAL_OUTPUT_CONTRACT_VALIDATED_ALPHA_FALSE"
        and receipt.get("python_optimize") == optimize
        and receipt.get("record_authoritative_for_terminal_pass") is False
        and receipt.get("child_local_validators_mutable_by_target") is True
        and receipt.get("reviewed_hash_sealed_target_in_local_tcb") is True
        and receipt.get("malicious_target_code_resistance_claimed") is False
        and receipt.get("alpha_computed") is False,
        "child receipt authority/scope mismatch",
    )
    require(
        receipt.get("runtime_snapshot_sha256") == sha256(RUNTIME)
        and receipt.get("target_manifest_sha256_before") == sha256(manifest_path)
        and receipt.get("target_manifest_sha256_after") == sha256(manifest_path)
        and receipt.get("target_output_sha256") == sha256(output_path)
        and receipt.get("target_source_sha256")
        == sha256((PROJECT_ROOT / manifest["target_script"]).resolve()),
        "child receipt hash chain mismatch",
    )
    require(
        receipt.get("runtime_manifest_sha256_before")
        == receipt.get("runtime_manifest_sha256_after"),
        "runtime changed during child",
    )
    require(
        receipt.get("observed_transient_environment_events") == TRANSIENT_EVENTS
        and receipt.get("conditional_environment_mutation_policy") == TRANSIENT_EVENTS,
        "transient environment sequence changed",
    )
    files = {
        str((PROJECT_ROOT / name).resolve()): digest
        for name, digest in manifest["files"].items()
    }
    allowed = dict(runtime_allowed)
    allowed.update(files)
    allowed[str(RUNTIME.resolve())] = sha256(RUNTIME)
    allowed[str(manifest_path.resolve())] = sha256(manifest_path)
    validate_modules(receipt.get("loaded_modules"), allowed)
    validate_originless_alias_negative_controls(receipt["loaded_modules"], allowed)
    validate_native_images(receipt.get("loaded_native_images"), runtime_allowed)
    validate_open_events(
        receipt.get("open_events"),
        allowed,
        output_path,
        receipt_path,
        Path(runtime["source_only_pycache_root"]),
    )
    return output, {
        "manifest": sha256(manifest_path),
        "output": sha256(output_path),
        "receipt": sha256(receipt_path),
    }


def run_launcher(runtime: dict[str, Any], manifest: Path, optimize: int) -> None:
    run_python(runtime, LAUNCHER, [RUNTIME, manifest], optimize=optimize)


def main() -> None:
    require(
        sys.flags.isolated
        and sys.flags.no_site
        and sys.flags.dont_write_bytecode
        and sys.flags.ignore_environment
        and sys.flags.optimize == 0,
        "supervisor requires isolated normal Python",
    )
    forbidden = {
        key
        for key in os.environ
        if key in {"PYTHONPATH", "PYTHONHOME", "PYTHONSTARTUP", "PYTHONINSPECT"}
        or key.startswith(("DYLD_", "LD_"))
    }
    require(not forbidden, f"unsafe parent bootstrap environment: {sorted(forbidden)}")
    runtime, runtime_allowed = validate_runtime()
    failure_lineage = validate_preserved_failure_lineage()
    expected_host_trust = runtime["native_system_trust_root"]
    original = list(sys.orig_argv)
    require(
        bool(original)
        and Path(original[0]).resolve() == Path(runtime["python_executable"]).resolve()
        and "-c" not in original
        and "-m" not in original
        and len(sys.argv) == 1
        and Path(sys.argv[0]).resolve() == PROGRAM
        and Path(original[-1]).resolve() == PROGRAM
        and original[1:-1].count("-I") == 1
        and original[1:-1].count("-S") == 1
        and original[1:-1].count("-B") == 1
        and original[1:-1].count("-X") == 1
        and original[1:-1].count("-O") == 0
        and sum(
            token.startswith("pycache_prefix=") for token in original[1:-1]
        )
        == 1
        and sys.pycache_prefix is not None
        and Path(sys.pycache_prefix).resolve()
        == Path(runtime["source_only_pycache_root"]).resolve(),
        "supervisor direct-invocation contract failed",
    )
    produced = (
        NORMAL_MANIFEST,
        OPTIMIZED_MANIFEST,
        VERIFIER_MANIFEST,
        TERMINAL,
        SIGNATURE,
        PROJECT_ROOT / "results" / "bid_source_parent_terminal_producer_normal_v005.json",
        PROJECT_ROOT / "results" / "bid_source_parent_terminal_producer_optimized_v005.json",
        PROJECT_ROOT / "results" / "bid_source_parent_terminal_children_verifier_v005.json",
        PROJECT_ROOT / "provenance" / "bid_source_parent_terminal_producer_normal_v005_execution_receipt.json",
        PROJECT_ROOT / "provenance" / "bid_source_parent_terminal_producer_optimized_v005_execution_receipt.json",
        PROJECT_ROOT / "provenance" / "bid_source_parent_terminal_children_verifier_v005_execution_receipt.json",
    )
    require(not any(path.exists() for path in produced), "fresh terminal artifacts required")

    frozen_sources = {
        path: sha256(path)
        for path in (
            PROGRAM,
            PRODUCER_BUILDER,
            VERIFIER_BUILDER,
            LAUNCHER,
            RUNTIME,
            ALIAS_TEST,
            V003_FAILURE_RECORD,
            V003_FAILURE_SEAL,
        )
    }
    alias_test = run_python(runtime, ALIAS_TEST)
    require(
        alias_test.stdout.splitlines()
        == [
            "SOURCE_NAMESPACE_ALIAS_CLASSIFIER=PASS",
            "positive_aliases=2",
            "hostile_negative_controls=11",
            "independent_live_reconstructors=2",
            "name_specific_allowlist=FALSE",
            "alpha_computed=FALSE",
        ],
        "source-namespace alias unit/adversarial test did not pass exactly",
    )
    run_python(runtime, PRODUCER_BUILDER)
    require(
        all(path.is_file() and sha256(path) == digest for path, digest in frozen_sources.items()),
        "source changed during producer-manifest build",
    )
    validate_manifest(NORMAL_MANIFEST, runtime, 0)
    validate_manifest(OPTIMIZED_MANIFEST, runtime, 1)

    run_launcher(runtime, NORMAL_MANIFEST, 0)
    require(current_trust() == expected_host_trust, "host trust changed after normal child")
    normal, normal_hashes = validate_child(NORMAL_MANIFEST, runtime, runtime_allowed, 0)
    run_launcher(runtime, OPTIMIZED_MANIFEST, 1)
    require(
        current_trust() == expected_host_trust,
        "host trust changed after optimized child",
    )
    optimized, optimized_hashes = validate_child(
        OPTIMIZED_MANIFEST, runtime, runtime_allowed, 1
    )
    normal_cmp = dict(normal)
    optimized_cmp = dict(optimized)
    normal_cmp.pop("python_optimize")
    optimized_cmp.pop("python_optimize")
    require(normal_cmp == optimized_cmp, "normal and optimized producer outputs differ")

    run_python(runtime, VERIFIER_BUILDER)
    verifier_manifest = validate_manifest(VERIFIER_MANIFEST, runtime, 0)
    require(
        verifier_manifest.get("producer_semantics_parent_validated_before_manifest") is True,
        "verifier manifest lost parent-validation ordering",
    )
    run_launcher(runtime, VERIFIER_MANIFEST, 0)
    require(
        current_trust() == expected_host_trust,
        "host trust changed after verifier child",
    )
    verifier, verifier_hashes = validate_child(
        VERIFIER_MANIFEST, runtime, runtime_allowed, 0
    )
    require(
        verifier.get("normal_manifest_sha256") == normal_hashes["manifest"]
        and verifier.get("normal_output_sha256") == normal_hashes["output"]
        and verifier.get("normal_receipt_sha256") == normal_hashes["receipt"]
        and verifier.get("optimized_manifest_sha256") == optimized_hashes["manifest"]
        and verifier.get("optimized_output_sha256") == optimized_hashes["output"]
        and verifier.get("optimized_receipt_sha256") == optimized_hashes["receipt"],
        "independent verifier did not bind the parent-validated children",
    )
    require(
        verifier.get("preserved_v003_failure_record_sha256")
        == V003_FAILURE_RECORD_SHA256
        and verifier.get("preserved_v003_failure_seal_sha256")
        == V003_FAILURE_SEAL_SHA256
        and verifier.get("checks", {}).get("preserved_failure_lineage_validated")
        is True,
        "independent verifier did not bind the preserved v003 failure lineage",
    )
    require(
        failure_lineage == validate_preserved_failure_lineage()
        and all(
            path.is_file() and sha256(path) == digest
            for path, digest in frozen_sources.items()
        ),
        "frozen sources or preserved failure lineage changed before terminal seal",
    )

    terminal = {
        "schema": "gravacle.bid-source-parent-sp14-terminal.v005",
        "status": "PASS_SP14_LOCAL_RUNTIME_ASSURANCE_ONLY_ALPHA_FALSE",
        "assurance_scope": (
            "Fresh parent supervision, separate real normal and optimized CPython "
            "children, independent verifier child, current content hashes, and a "
            "revalidated mutable macOS trust base for reviewed hash-sealed target "
            "programs; not remote attestation and not resistance to a malicious "
            "target, kernel, interpreter, or signer."
        ),
        "trusted_target_source_boundary": (
            "The exact target sources are hash-sealed members of the local trusted "
            "computing base. Malicious target-code resistance is not claimed."
        ),
        "preserved_v003_failure_lineage": failure_lineage,
        "runtime_snapshot_sha256": sha256(RUNTIME),
        "supervisor_sha256": sha256(PROGRAM),
        "normal": normal_hashes,
        "optimized": optimized_hashes,
        "verifier": verifier_hashes,
        "normal_optimized_semantic_equivalence": True,
        "host_trust_revalidated_after_every_child": True,
        "originless_alias_negative_controls": True,
        "source_namespace_alias_adversarial_test_sha256": sha256(ALIAS_TEST),
        "originless_object_identity_scope": (
            "Object identity is enforced inside the hash-sealed launcher. The fresh "
            "parent and independent verifier each reconstruct the corresponding "
            "alias as a live object under the same sealed runtime and reject receipt "
            "rows that do not match; neither claims to inspect the dead child's "
            "memory after process exit."
        ),
        "known_source_parent_blockers_after_sp14": ["SP08", "SP09"],
        "sp14_runtime_assurance": True,
        "source_parent_closure": False,
        "proof_authorized": False,
        "alpha_computed": False,
        "signature": {
            "format": "OpenPGP detached ASCII armor",
            "path": relative(SIGNATURE),
            "signing_fingerprint": SIGNER,
            "required_for_terminal_acceptance": True,
        },
    }
    with TERMINAL.open("x", encoding="utf-8") as handle:
        json.dump(terminal, handle, indent=2, sort_keys=True, allow_nan=False)
        handle.write("\n")
    require(GPG.is_file(), "GPG signer unavailable")
    subprocess.run(
        [
            str(GPG),
            "--batch",
            "--armor",
            "--detach-sign",
            "--local-user",
            f"{SIGNER}!",
            "--output",
            str(SIGNATURE),
            str(TERMINAL),
        ],
        check=True,
    )
    verification = subprocess.run(
        [
            str(GPG),
            "--batch",
            "--status-fd",
            "1",
            "--verify",
            str(SIGNATURE),
            str(TERMINAL),
        ],
        check=True,
        text=True,
        capture_output=True,
    )
    require(
        any(
            line.startswith("[GNUPG:] VALIDSIG ")
            and line.split()[2] == SIGNER
            for line in verification.stdout.splitlines()
        ),
        "detached signature did not verify under the exact frozen fingerprint",
    )
    print(TERMINAL)
    print(SIGNATURE)
    print("SP14_LOCAL_RUNTIME_ASSURANCE=PASS")
    print("source_parent_closure=false")
    print("alpha_computed=false")


if __name__ == "__main__":
    main()
