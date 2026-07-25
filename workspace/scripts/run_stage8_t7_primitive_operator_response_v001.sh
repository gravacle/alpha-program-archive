#!/bin/sh
set -eu

ROOT="/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003"
PYTHON="/Users/bgm/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"

SPEC="$ROOT/STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_SPEC_V001.md"
EXACT="$ROOT/STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_EXACT_DERIVATION_V001.md"
AMENDMENT="$ROOT/STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_AUTHORITY_AMENDMENT_V001.md"
RUNTIME="$ROOT/provenance/stage8_t7_numpy_runtime_manifest_v001.json"
PRIMARY="$ROOT/scripts/derive_stage8_t7_primitive_operator_response_v001.py"
VERIFIER="$ROOT/scripts/verify_stage8_t7_primitive_operator_response_v001.py"

hash_file() {
    /usr/bin/shasum -a 256 "$1" | /usr/bin/awk '{print $1}'
}

require_hash() {
    actual="$(hash_file "$1")"
    expected="$2"
    if [ "$actual" != "$expected" ]; then
        echo "HASH_MISMATCH $1" >&2
        exit 1
    fi
}

if [ "$#" -ne 1 ]; then
    echo "usage: $0 primary|verify" >&2
    exit 2
fi

require_hash "$PYTHON" \
    "eb9d74b9c7cfdfb2c9b91614edb2c3607360ba46c5aa7fc4557b3a4a23e97cff"
require_hash "$SPEC" \
    "2f2aa7f7397b70616fa5c9e8ed628ca1d1e819bb698133a169c6d544086b3cde"
require_hash "$EXACT" \
    "a9875788301d8434113f77e3b5726b49d70d8609fbcfcc72c9fede76a1249e4a"
require_hash "$AMENDMENT" \
    "1d26607ad490c2ee02ee42171cedd9e3f24cecf7e37d49fb8c91fac20b6aca39"
require_hash "$RUNTIME" \
    "f2e820d5d7a53335f1a6aacdbc03331d18e6afa350f99b7d2f2abd59d77bc46b"
require_hash "$PRIMARY" \
    "3d8aea1a4779b0bfe7a472dca1fab0642750e8e010e339b9e3b100197b75a18c"
require_hash "$VERIFIER" \
    "75551faf7235166371aea9216f8bf67d1eb3aebfaf30cbd89c223f994802e6aa"

case "$1" in
    primary)
        SCRIPT="$PRIMARY"
        ;;
    verify)
        SCRIPT="$VERIFIER"
        ;;
    *)
        echo "unknown mode: $1" >&2
        exit 2
        ;;
esac

exec /usr/bin/env -i \
    HOME="$HOME" \
    TMPDIR="${TMPDIR:-/tmp}" \
    PATH="/usr/bin:/bin" \
    LC_ALL="C" \
    OMP_NUM_THREADS="1" \
    OPENBLAS_NUM_THREADS="1" \
    VECLIB_MAXIMUM_THREADS="1" \
    "$PYTHON" -I -S -B "$SCRIPT"
