#!/usr/bin/env python3
"""Launch Stage-8 T7 lanes under the sealed content-addressed NumPy runtime."""

from __future__ import annotations

import hashlib
import json
import runpy
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
RUNTIME_MANIFEST = (
    ROOT / "provenance/stage8_t7_numpy_runtime_manifest_v001.json"
)
RUNTIME_SEAL = Path(f"{RUNTIME_MANIFEST}.seal.sha256")
EXPECTED_MANIFEST_SHA256 = (
    "f2e820d5d7a53335f1a6aacdbc03331d18e6afa350f99b7d2f2abd59d77bc46b"
)
EXPECTED_NUMPY_VERSION = "2.3.5"
EXPECTED_NUMPY_CONFIG_SHA256 = (
    "646c4646f99237f1d83cb2f4c62c82d3d65b2d24cd93fc7bf68da87ee3ea30b7"
)
RUNTIME_MARKER = "_stage8_t7_content_addressed_runtime_v001"
ALLOWED_TARGETS = frozenset(
    {
        "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
        "primary_v002.py",
        "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
        "independent_v002.py",
        "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
        "v002.py",
        "scripts/test_stage8_t7_actual_parent_regulated_car_operator_response_"
        "primary_v002.py",
        "scripts/test_stage8_t7_actual_parent_regulated_car_operator_response_"
        "independent_v002.py",
        "scripts/test_compare_stage8_t7_actual_parent_regulated_car_operator_"
        "response_v002.py",
        "scripts/run_stage8_t7_actual_parent_car_pipeline_v002.py",
        "scripts/test_stage8_t7_launcher_v002.py",
        "scripts/test_stage8_t7_controller_v002.py",
    }
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha256(value: Any) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
        default=str,
    ).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def strict_json(path: Path) -> dict[str, Any]:
    def object_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            require(key not in result, f"duplicate JSON key in {path}: {key}")
            result[key] = value
        return result

    def reject_constant(value: str) -> None:
        raise RuntimeError(f"non-finite JSON constant in {path}: {value}")

    value = json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=object_pairs,
        parse_constant=reject_constant,
    )
    require(isinstance(value, dict), f"runtime manifest is not an object: {path}")
    return value


def verify_runtime() -> dict[str, Any]:
    require(sys.flags.isolated == 1, "Stage-8 runtime requires Python -I")
    require(sys.flags.no_site == 1, "Stage-8 runtime requires Python -S")
    require(RUNTIME_MANIFEST.is_file(), "sealed NumPy runtime manifest is absent")
    require(RUNTIME_SEAL.is_file(), "sealed NumPy runtime seal is absent")
    require(
        sha256(RUNTIME_MANIFEST) == EXPECTED_MANIFEST_SHA256,
        "NumPy runtime manifest drift",
    )
    seal_fields = RUNTIME_SEAL.read_text(encoding="ascii").strip().split()
    require(len(seal_fields) == 2, "malformed NumPy runtime seal")
    require(
        seal_fields[0] == EXPECTED_MANIFEST_SHA256,
        "NumPy runtime seal digest mismatch",
    )
    require(
        seal_fields[1]
        == "provenance/stage8_t7_numpy_runtime_manifest_v001.json",
        "NumPy runtime seal path mismatch",
    )

    manifest = strict_json(RUNTIME_MANIFEST)
    require(
        manifest.get("schema") == "stage8_t7_numpy_runtime_manifest_v001",
        "NumPy runtime schema mismatch",
    )
    executable = Path(str(manifest.get("python_executable"))).resolve()
    require(Path(sys.executable).resolve() == executable, "unexpected Python executable")
    require(
        sha256(executable) == manifest.get("python_executable_sha256"),
        "Python executable hash mismatch",
    )
    require(manifest.get("python_isolated") is True, "manifest lost isolated flag")
    require(manifest.get("python_no_site") is True, "manifest lost no-site flag")

    site_packages = Path(str(manifest.get("site_packages"))).resolve()
    rows = manifest.get("files")
    require(isinstance(rows, list) and bool(rows), "empty NumPy file inventory")
    expected: dict[str, tuple[str, int]] = {}
    for row in rows:
        require(isinstance(row, dict), "malformed NumPy file row")
        relative = str(row.get("path"))
        digest = str(row.get("sha256"))
        size = int(row.get("bytes"))
        require(relative not in expected, f"duplicate NumPy manifest path: {relative}")
        expected[relative] = (digest, size)

    package_roots = tuple(str(value) for value in manifest.get("package_roots", []))
    require(
        package_roots == ("numpy", "numpy-2.3.5.dist-info"),
        "NumPy package-root inventory changed",
    )
    actual_paths: dict[str, Path] = {}
    for package_root in package_roots:
        root = (site_packages / package_root).resolve()
        require(root.is_dir(), f"NumPy package root is absent: {root}")
        for path in sorted(root.rglob("*")):
            if path.is_file() and "__pycache__" not in path.parts:
                relative = str(path.relative_to(site_packages))
                actual_paths[relative] = path
    require(
        set(actual_paths) == set(expected),
        "NumPy runtime file inventory differs from the sealed manifest",
    )
    for relative, path in actual_paths.items():
        expected_digest, expected_size = expected[relative]
        require(path.stat().st_size == expected_size, f"NumPy size drift: {relative}")
        require(sha256(path) == expected_digest, f"NumPy hash drift: {relative}")

    # Force source/extension loading from the verified tree rather than ambient
    # user-site state or an existing local __pycache__.
    sys.dont_write_bytecode = True
    sys.pycache_prefix = (
        f"/private/tmp/stage8_t7_no_cache_{EXPECTED_MANIFEST_SHA256[:16]}"
    )
    sys.path.insert(0, str(site_packages))
    import numpy as np

    require(np.__version__ == EXPECTED_NUMPY_VERSION, "NumPy version mismatch")
    require(
        Path(np.__file__).resolve() == (site_packages / "numpy/__init__.py").resolve(),
        "NumPy loaded from an unsealed origin",
    )
    config_hash = canonical_sha256(np.__config__.CONFIG)
    require(
        config_hash == EXPECTED_NUMPY_CONFIG_SHA256,
        "NumPy BLAS/LAPACK build configuration mismatch",
    )
    return {
        "schema": "stage8_t7_content_addressed_runtime_attestation_v001",
        "launcher_sha256": sha256(SELF),
        "runtime_manifest_sha256": EXPECTED_MANIFEST_SHA256,
        "python_executable": str(executable),
        "python_executable_sha256": manifest["python_executable_sha256"],
        "python_isolated": True,
        "python_no_site": True,
        "numpy_version": np.__version__,
        "numpy_origin": str(Path(np.__file__).resolve()),
        "numpy_file_count": len(expected),
        "numpy_config_sha256": config_hash,
        "blas_lapack_provider": "Accelerate (sealed NumPy build configuration)",
        "content_addressed_scope":
            "Python executable plus NumPy package and distribution files",
        "python_standard_library_trusted_host_boundary": True,
        "accelerate_framework_trusted_host_boundary": True,
        "loaded_native_dependencies_content_addressed": False,
        "malicious_interpreter_or_kernel_resistance_claimed": False,
        "attestation_is_launcher_cooperative_only": True,
    }


def resolve_target(value: str) -> tuple[Path, str]:
    target = Path(value)
    if not target.is_absolute():
        target = ROOT / target
    target = target.resolve()
    try:
        relative = str(target.relative_to(ROOT))
    except ValueError as error:
        raise RuntimeError("runtime target is outside the clean-room root") from error
    require(relative in ALLOWED_TARGETS, f"runtime target is not allowlisted: {relative}")
    require(target.is_file(), f"runtime target is absent: {target}")
    return target, relative


def main() -> int:
    attestation = verify_runtime()
    setattr(sys, RUNTIME_MARKER, attestation)
    if len(sys.argv) == 2 and sys.argv[1] == "--selftest":
        print(json.dumps(attestation, indent=2, sort_keys=True))
        return 0
    require(len(sys.argv) >= 2, "usage: launcher TARGET [TARGET_ARGUMENTS...]")
    target, _ = resolve_target(sys.argv[1])
    attestation["target_sha256"] = sha256(target)
    sys.argv = [str(target), *sys.argv[2:]]
    runpy.run_path(str(target), run_name="__main__")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
