#!/usr/bin/env python3
# collector_v001.py -- A32 registry collector, frozen rules, fail-closed.
# Purely mechanical collection. No research corpus file is accessed.
import datetime
import hashlib
import json
import os
import subprocess
import sys

OUT = "/Users/bgm/MB Work/a32_holdout"
PRIV = os.path.join(OUT, "custodian_private")
URL = "https://physics.nist.gov/cuu/Constants/Table/allascii.txt"
SOURCE_ID = "NIST_CODATA_2022_allascii"
VINTAGE_MARKER = "2022 CODATA adjustment"

RAW_PATH = os.path.join(OUT, "raw_allascii.txt")
EXCLUSIONS_PATH = os.path.join(OUT, "exclusions.jsonl")
CANDIDATES_PATH = os.path.join(OUT, "candidates.jsonl")
DUPLICATES_PATH = os.path.join(OUT, "duplicates.jsonl")
COMMITMENTS_PATH = os.path.join(OUT, "commitments.jsonl")
FLAGS_PATH = os.path.join(OUT, "flags.jsonl")
CUSTODIAN_PATH = os.path.join(PRIV, "custodian.jsonl")
TRANSCRIPT_PATH = os.path.join(OUT, "transcript.md")
SELF_PATH = os.path.abspath(__file__)

ATTESTATION = ("No outcome payload was disclosed outside custodian_private/. "
               "The collector accessed no research corpus file.")
LINEAGE_NOTE = ("Lineage exclusion is executed later at the eligibility stage "
                "under the frozen rule; this file only pre-flags name matches. "
                "No row was dropped for content.")

steps = []


def utc_now():
    return datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ")


def log(msg):
    steps.append((utc_now(), msg))


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def jdump(obj):
    # RFC-8785-style for all-string fields: sorted keys, compact separators,
    # UTF-8. All fields are strings so number normalization is moot.
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False)


def write_jsonl(path, rows):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(jdump(r) + "\n")


def norm(s):
    return " ".join(s.split()).lower()


def write_transcript(status, detail, counts, file_hashes,
                     collector_hash, raw_hash):
    lines = []
    lines.append("# A32 Registry Collection Transcript (collector_v001)")
    lines.append("")
    lines.append("- Status: %s" % status)
    if detail:
        lines.append("- Detail: %s" % detail)
    lines.append("- Canonical source URL: %s" % URL)
    lines.append("- source_id: %s" % SOURCE_ID)
    lines.append("- Collector script: %s" % SELF_PATH)
    lines.append("- Collector version hash (SHA-256 of collector_v001.py): %s"
                 % collector_hash)
    if raw_hash:
        lines.append("- Raw bytes SHA-256 (raw_allascii.txt): %s" % raw_hash)
    lines.append("")
    lines.append("## Steps (UTC)")
    lines.append("")
    for ts, msg in steps:
        lines.append("- %s -- %s" % (ts, msg))
    lines.append("")
    lines.append("## Row counts")
    lines.append("")
    for k in sorted(counts):
        lines.append("- %s: %d" % (k, counts[k]))
    lines.append("")
    lines.append("## File SHA-256 hashes")
    lines.append("")
    for p in sorted(file_hashes):
        lines.append("- %s: %s" % (p, file_hashes[p]))
    lines.append("- %s: (own hash; computed after this transcript is "
                 "finalized and reported by the runner)" % TRANSCRIPT_PATH)
    lines.append("")
    lines.append("## Flag-file note (frozen rule 9)")
    lines.append("")
    lines.append(LINEAGE_NOTE)
    lines.append("")
    lines.append("## Attestation")
    lines.append("")
    lines.append(ATTESTATION)
    lines.append("")
    with open(TRANSCRIPT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))


def fail_closed(status, detail, counts=None, file_hashes=None, raw_hash=None):
    collector_hash = sha256_file(SELF_PATH)
    log("FAIL CLOSED: %s -- %s" % (status, detail))
    write_transcript(status, detail, counts or {}, file_hashes or {},
                     collector_hash, raw_hash)
    result = {"status": status, "detail": detail,
              "transcript": TRANSCRIPT_PATH,
              "transcript_sha256": sha256_file(TRANSCRIPT_PATH)}
    print(json.dumps(result, sort_keys=True))
    sys.exit(1)


def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(PRIV, exist_ok=True)
    os.chmod(PRIV, 0o700)
    log("Collection started. Output directory prepared; "
        "custodian_private/ set to mode 700.")

    # ---- Rule 1: FETCH via curl, single canonical URL, 3 plain retries ----
    attempts = 4  # 1 initial attempt + 3 plain retries
    fetch_ok = False
    last_err = ""
    for i in range(1, attempts + 1):
        log("curl attempt %d of %d against canonical URL." % (i, attempts))
        try:
            proc = subprocess.run(
                ["curl", "-sS", "-o", RAW_PATH, "-w", "%{http_code}", URL],
                capture_output=True, text=True, timeout=120)
        except Exception as e:  # timeout or spawn failure
            last_err = "curl exception: %r" % (e,)
            log(last_err)
            continue
        code = (proc.stdout or "").strip()
        if proc.returncode == 0 and code == "200":
            fetch_ok = True
            log("curl attempt %d succeeded with HTTP 200." % i)
            break
        last_err = ("curl exit=%d http_code=%s stderr=%s"
                    % (proc.returncode, code, (proc.stderr or "").strip()))
        log("curl attempt %d failed: %s" % (i, last_err))
    if not fetch_ok:
        fail_closed("FAILED_CLOSED_NETWORK",
                    "Canonical URL unreachable after 1 attempt + 3 plain "
                    "retries. Last error: %s" % last_err)

    with open(RAW_PATH, "rb") as f:
        raw = f.read()
    raw_hash = sha256_bytes(raw)
    log("Raw bytes saved unmodified to raw_allascii.txt; SHA-256 recorded.")

    # ---- Rule 2: VINTAGE CHECK ----
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as e:
        fail_closed("FAILED_CLOSED_FORMAT",
                    "Raw bytes are not valid UTF-8: %r" % (e,),
                    raw_hash=raw_hash)
        return
    lines = text.splitlines()
    header_region = lines[:10]
    if not any(VINTAGE_MARKER in ln for ln in header_region):
        fail_closed("FAILED_CLOSED_WRONG_VINTAGE",
                    "Header does not identify the 2022 CODATA adjustment. "
                    "Header lines: %r" % (header_region,),
                    raw_hash=raw_hash)
    header_line = next(ln for ln in header_region if VINTAGE_MARKER in ln)
    log("Vintage check passed. Header line: %r" % header_line.strip())

    # ---- Rule 4: PARSE (fixed columns from the column-header line) ----
    col_idx = None
    for n, ln in enumerate(lines):
        if ("Quantity" in ln and "Value" in ln and "Uncertainty" in ln
                and "Unit" in ln):
            col_idx = n
            break
    if col_idx is None:
        fail_closed("FAILED_CLOSED_FORMAT",
                    "Column header line (Quantity/Value/Uncertainty/Unit) "
                    "not found.", raw_hash=raw_hash)
    hdr = lines[col_idx]
    idx_val = hdr.index("Value")
    idx_unc = hdr.index("Uncertainty")
    idx_unit = hdr.index("Unit")
    # Data begins after the dashed separator following the column header.
    data_start = None
    for n in range(col_idx + 1, len(lines)):
        s = lines[n].strip()
        if s and set(s) == {"-"}:
            data_start = n + 1
            break
    if data_start is None:
        fail_closed("FAILED_CLOSED_FORMAT",
                    "Dashed separator after column header not found.",
                    raw_hash=raw_hash)
    log("Column header found at line %d (0-based); value/uncertainty/unit "
        "column offsets %d/%d/%d; data region starts at line %d."
        % (col_idx, idx_val, idx_unc, idx_unit, data_start))

    parsed = []      # (line_number_1based, name, value, uncertainty, unit)
    exclusions = []  # machine reason codes only; no row content (masking)
    for n in range(data_start, len(lines)):
        line_no = n + 1
        ln = lines[n]
        if ln.strip() == "":
            exclusions.append({"line_number": line_no,
                               "reason": "EMPTY_LINE"})
            continue
        if len(ln) <= idx_val:
            exclusions.append({"line_number": line_no,
                               "reason": "LINE_TOO_SHORT_NO_VALUE_COLUMN"})
            continue
        name = ln[:idx_val].strip()
        value = ln[idx_val:idx_unc].strip()
        uncertainty = ln[idx_unc:idx_unit].strip()
        unit = ln[idx_unit:].strip()
        if not name:
            exclusions.append({"line_number": line_no,
                               "reason": "MISSING_QUANTITY_NAME"})
            continue
        if not value:
            exclusions.append({"line_number": line_no,
                               "reason": "MISSING_VALUE_FIELD"})
            continue
        if not uncertainty:
            exclusions.append({"line_number": line_no,
                               "reason": "MISSING_UNCERTAINTY_FIELD"})
            continue
        parsed.append((line_no, name, value, uncertainty, unit))
    rows_in_region = len(lines) - data_start
    log("Parse complete: %d lines in data region, %d parsed, %d excluded "
        "with machine reason codes." % (rows_in_region, len(parsed),
                                        len(exclusions)))

    # ---- Rule 5: CANONICAL RECORDS (value-free) ----
    records = []  # (canonical_id, record_dict, name, value, uncertainty, u)
    for (_ln, name, value, uncertainty, unit) in parsed:
        units = unit if unit else "dimensionless"
        record = {"definition": name, "domain": "", "record_id": name,
                  "source_id": SOURCE_ID, "units": units}
        canonical_id = sha256_bytes(jdump(record).encode("utf-8"))
        records.append((canonical_id, record, name, value, uncertainty,
                        units))
    log("Canonical value-free records built for %d rows; canonical_id = "
        "SHA-256 of sorted-key compact UTF-8 serialization. Observed values "
        "did not enter records or ids." % len(records))

    # ---- Rule 6: DEDUP ----
    clusters = {}
    for entry in records:
        canonical_id, record = entry[0], entry[1]
        key = "|".join([norm(record["source_id"]),
                        norm(record["definition"]),
                        norm(record["units"]),
                        norm(record["domain"])])
        clusters.setdefault(key, []).append(entry)
    kept = []
    duplicates = []
    for key in clusters:
        members = sorted(clusters[key], key=lambda e: e[0])
        keeper = members[0]
        kept.append(keeper)
        for m in members[1:]:
            duplicates.append({
                "canonical_id": m[0],
                "kept_canonical_id": keeper[0],
                "cluster_key": key,
                "reason": "DUPLICATE_CLUSTER_KEY_LOWER_CANONICAL_ID_KEPT"})
    # Preserve source order among kept candidates (deterministic).
    order = {id(e): i for i, e in enumerate(records)}
    kept.sort(key=lambda e: order[id(e)])
    log("Dedup complete: %d clusters, %d kept, %d suppressed."
        % (len(clusters), len(kept), len(duplicates)))

    # ---- Rule 7: PUBLIC CANDIDATE FILE (value-free) ----
    candidate_rows = [{"canonical_id": e[0], "record": e[1]} for e in kept]
    write_jsonl(CANDIDATES_PATH, candidate_rows)
    write_jsonl(EXCLUSIONS_PATH, exclusions)
    write_jsonl(DUPLICATES_PATH, duplicates)
    log("candidates.jsonl written (value-free); exclusions.jsonl and "
        "duplicates.jsonl written.")

    # ---- Rule 8: CUSTODIAN COMMITMENTS ----
    custodian_rows = []
    commitment_rows = []
    with open("/dev/urandom", "rb") as rnd:
        for (canonical_id, record, _name, value, uncertainty,
             units) in kept:
            salt = rnd.read(32)
            if len(salt) != 32:
                fail_closed("FAILED_CLOSED_ENTROPY",
                            "Short read from /dev/urandom.",
                            raw_hash=raw_hash)
            payload_obj = {"source_id": SOURCE_ID,
                           "uncertainty": uncertainty,
                           "units": units,
                           "value": value}
            payload_str = jdump(payload_obj)
            commitment = hashlib.sha256(
                salt + payload_str.encode("utf-8")).hexdigest()
            custodian_rows.append({"canonical_id": canonical_id,
                                   "payload": payload_str,
                                   "salt": salt.hex()})
            commitment_rows.append({"canonical_id": canonical_id,
                                    "commitment": commitment})
    write_jsonl(CUSTODIAN_PATH, custodian_rows)
    os.chmod(CUSTODIAN_PATH, 0o600)
    write_jsonl(COMMITMENTS_PATH, commitment_rows)
    log("Custodian commitments written: custodian_private/custodian.jsonl "
        "(mode 600, the ONLY file containing values/uncertainties) and "
        "public commitments.jsonl (canonical_id + commitment hex only).")

    # ---- Rule 9: ALPHA-DATUM NAME FLAGS (no content-based drops) ----
    flag_rows = []
    for (canonical_id, record, name, _v, _u, _units) in kept:
        if "fine-structure constant" in name.lower():
            flag_rows.append({"canonical_id": canonical_id,
                              "flag": "ALPHA_DATUM_NAME_MATCH"})
    write_jsonl(FLAGS_PATH, flag_rows)
    log("flags.jsonl written with %d ALPHA_DATUM_NAME_MATCH entries. %s"
        % (len(flag_rows), LINEAGE_NOTE))

    # ---- Rule 10: collector version hash ----
    collector_hash = sha256_file(SELF_PATH)
    log("Collector version hash recorded (SHA-256 of collector_v001.py).")

    # ---- Rule 11: TRANSCRIPT ----
    counts = {
        "rows_in_data_region": rows_in_region,
        "rows_parsed": len(parsed),
        "rows_parse_excluded": len(exclusions),
        "duplicates_suppressed": len(duplicates),
        "candidates_kept": len(kept),
        "alpha_name_flagged": len(flag_rows),
    }
    file_hashes = {p: sha256_file(p) for p in [
        RAW_PATH, EXCLUSIONS_PATH, CANDIDATES_PATH, DUPLICATES_PATH,
        COMMITMENTS_PATH, FLAGS_PATH, CUSTODIAN_PATH, SELF_PATH]}
    log("All output file hashes computed. " + ATTESTATION)
    write_transcript("COMPLETED", "", counts, file_hashes, collector_hash,
                     raw_hash)
    file_hashes[TRANSCRIPT_PATH] = sha256_file(TRANSCRIPT_PATH)

    result = {"status": "COMPLETED",
              "raw_sha256": raw_hash,
              "collector_version_hash": collector_hash,
              "counts": counts,
              "file_sha256": file_hashes}
    print(json.dumps(result, sort_keys=True, indent=1))


if __name__ == "__main__":
    main()
