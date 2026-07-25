#!/usr/bin/env python3
"""Build the content-addressed NumPy runtime manifest for the Stage-8 T7 gate."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PYTHON_ROOT = Path(
    "/Users/bgm/.cache/codex-runtimes/"
    "codex-primary-runtime/dependencies/python"
).resolve()
SITE_PACKAGES = (
    PYTHON_ROOT / "lib/python3.12/site-packages"
)
PACKAGE_ROOTS = (
    SITE_PACKAGES / "numpy",
    SITE_PACKAGES / "numpy-2.3.5.dist-info",
)
OUT = ROOT / "provenance/stage8_t7_numpy_runtime_manifest_v001.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    if sys.flags.isolated != 1 or sys.flags.no_site != 1:
        raise SystemExit("run with the pinned Python using -I -S")
    if Path(sys.executable).resolve() != (PYTHON_ROOT / "bin/python3").resolve():
        raise SystemExit("unexpected Python executable")

    rows = []
    for package_root in PACKAGE_ROOTS:
        if not package_root.is_dir():
            raise SystemExit(f"missing package root: {package_root}")
        for path in sorted(package_root.rglob("*")):
            if path.is_file() and "__pycache__" not in path.parts:
                rows.append(
                    {
                        "path": str(path.relative_to(SITE_PACKAGES)),
                        "sha256": sha256(path),
                        "bytes": path.stat().st_size,
                    }
                )
    if not rows:
        raise SystemExit("empty NumPy runtime manifest")

    payload = {
        "schema": "stage8_t7_numpy_runtime_manifest_v001",
        "python_executable": str(Path(sys.executable).resolve()),
        "python_executable_sha256": sha256(Path(sys.executable).resolve()),
        "python_isolated": bool(sys.flags.isolated),
        "python_no_site": bool(sys.flags.no_site),
        "site_packages": str(SITE_PACKAGES),
        "package_roots": [
            str(path.relative_to(SITE_PACKAGES))
            for path in PACKAGE_ROOTS
        ],
        "file_count": len(rows),
        "files": rows,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    temporary = OUT.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(OUT)
    print(f"{sha256(OUT)}  {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
