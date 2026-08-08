"""Derive the expected census from the SEALED SPECIFICATION BYTES.

This module is the independence core of Builder B. Every expectation the
verifier holds — the check-ID universe, the execution-class partition, the
binding board, the descriptor digests — is parsed out of the sealed spec
itself. Nothing is taken from the producer's manifests, from Builder A's code,
or from any mutable receipt. If the producer and the spec disagree, the spec
wins and the run fails closed.

Governing spec: V012. State R9's duty passage is byte-identical to V005's, so
the expectations below are re-derived, not restated:
    "checks the exact 63 blocker IDs plus 3 discrepancy IDs, all 66 V005
     descriptor hashes, the 56/10 class partition, and the 35 carried BOUND +
     13 carried RE-RENDERED + 8 V004-REPAIRED + 10 V005-REPAIRED specification
     binding board"
The board's `V004-REPAIRED`/`V005-REPAIRED` labels are HISTORICAL tags naming
when a row was repaired; they are not a claim about which spec governs.
"""

import re

from .canonical_json import VerifierFault
from .hashing import load_addressed, sha256_bytes

SPEC_SHA256 = "382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504"

EXPECTED_TOTAL_IDS = 66
EXPECTED_BLOCKER_IDS = 63
EXPECTED_DISCREPANCY_IDS = 3
EXPECTED_CLASSES = {"STRUCTURAL": 56, "GATED-EXECUTION": 10}
EXPECTED_BOARD = {
    "BOUND": 35,
    "RE-RENDERED": 13,
    "V004-REPAIRED": 8,
    "V005-REPAIRED": 10,
}

_DESCRIPTOR = re.compile(r"^\|\s*`(C-[BD]-[A-Za-z0-9\-]+)`\s*\|\s*([^|]+)\|")
_BOARD_ROW = re.compile(
    r"^\|\s*\d+\s*\|\s*`(C-[BD]-[A-Za-z0-9\-]+)`\s*\|\s*([A-Z0-9 \-]+?)\s*\|")

_VALID_CLASSES = ("STRUCTURAL", "GATED-EXECUTION")


def _decode(spec_bytes):
    try:
        return spec_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise VerifierFault("spec is not valid UTF-8: %s" % exc)


def _section(text, start_marker, end_marker, where):
    start = text.find(start_marker)
    if start < 0:
        raise VerifierFault("%s: start marker not found" % where)
    end = text.find(end_marker, start)
    if end < 0:
        raise VerifierFault("%s: end marker not found" % where)
    return text[start:end]


def parse_descriptors(spec_text):
    """Return {check_id: {class, row_sha256}} for the 66 descriptor rows."""
    out = {}
    for line in spec_text.split("\n"):
        match = _DESCRIPTOR.match(line)
        if match is None:
            continue
        if line.count("|") < 5:
            continue
        klass = match.group(2).strip().replace("**", "")
        if klass not in _VALID_CLASSES:
            continue
        check_id = match.group(1)
        if check_id in out:
            raise VerifierFault("duplicate descriptor row for %s" % check_id)
        out[check_id] = {
            "execution_class": klass,
            # the descriptor's own content address: the exact row bytes
            "check_spec_sha256": sha256_bytes(line.encode("utf-8")),
            # V010-M1 needs the SEALED ROW TEXT itself: a ground atom's constant
            # must occur literally in the same row, and the atom shape is read
            # from these bytes and from nowhere else.
            "row": line,
        }
    return out


def parse_board(spec_text):
    """Return {check_id: disposition} from the §8.3 binding board."""
    segment = _section(spec_text, "### 8.3", "### 8.4", "binding board")
    out = {}
    for line in segment.split("\n"):
        match = _BOARD_ROW.match(line)
        if match is None:
            continue
        check_id, disposition = match.group(1), match.group(2).strip()
        if check_id in out:
            raise VerifierFault("duplicate board row for %s" % check_id)
        out[check_id] = disposition
    return out


class SpecCensus(object):
    """The verifier's independently derived expectations."""

    def __init__(self, spec_path, spec_sha256=SPEC_SHA256):
        self.spec_sha256 = spec_sha256
        spec_bytes = load_addressed(spec_path, spec_sha256, "governing spec")
        text = _decode(spec_bytes)
        self.descriptors = parse_descriptors(text)
        self.board = parse_board(text)
        self._validate()

    def _validate(self):
        ids = set(self.descriptors)
        if len(ids) != EXPECTED_TOTAL_IDS:
            raise VerifierFault(
                "census: %d descriptor IDs, expected %d"
                % (len(ids), EXPECTED_TOTAL_IDS))

        blockers = sorted(i for i in ids if i.startswith("C-B-"))
        discrepancies = sorted(i for i in ids if i.startswith("C-D-"))
        if len(blockers) != EXPECTED_BLOCKER_IDS:
            raise VerifierFault(
                "census: %d blocker IDs, expected %d"
                % (len(blockers), EXPECTED_BLOCKER_IDS))
        if len(discrepancies) != EXPECTED_DISCREPANCY_IDS:
            raise VerifierFault(
                "census: %d discrepancy IDs, expected %d"
                % (len(discrepancies), EXPECTED_DISCREPANCY_IDS))

        counts = {}
        for row in self.descriptors.values():
            counts[row["execution_class"]] = counts.get(
                row["execution_class"], 0) + 1
        if counts != EXPECTED_CLASSES:
            raise VerifierFault(
                "census: class partition %s, expected %s"
                % (counts, EXPECTED_CLASSES))

        if set(self.board) != ids:
            missing = sorted(ids - set(self.board))
            extra = sorted(set(self.board) - ids)
            raise VerifierFault(
                "census: board universe mismatch (missing=%s extra=%s)"
                % (missing, extra))

        board_counts = {}
        for disposition in self.board.values():
            board_counts[disposition] = board_counts.get(disposition, 0) + 1
        if board_counts != EXPECTED_BOARD:
            raise VerifierFault(
                "census: binding board %s, expected %s"
                % (board_counts, EXPECTED_BOARD))

    def check_ids(self):
        return sorted(self.descriptors)

    def execution_class(self, check_id):
        row = self.descriptors.get(check_id)
        if row is None:
            raise VerifierFault("unknown check_id %r" % check_id)
        return row["execution_class"]

    def check_spec_sha256(self, check_id):
        row = self.descriptors.get(check_id)
        if row is None:
            raise VerifierFault("unknown check_id %r" % check_id)
        return row["check_spec_sha256"]

    def descriptor_row(self, check_id):
        """The sealed descriptor row's own text. V010-M1's only atom source."""
        row = self.descriptors.get(check_id)
        if row is None:
            raise VerifierFault("unknown check_id %r" % check_id)
        return row["row"]

    def gated_ids(self):
        return sorted(i for i in self.descriptors
                      if self.descriptors[i]["execution_class"]
                      == "GATED-EXECUTION")

    def structural_ids(self):
        return sorted(i for i in self.descriptors
                      if self.descriptors[i]["execution_class"] == "STRUCTURAL")

    def summary(self):
        return {
            "spec_sha256": self.spec_sha256,
            "total_ids": len(self.descriptors),
            "blocker_ids": len([i for i in self.descriptors
                                if i.startswith("C-B-")]),
            "discrepancy_ids": len([i for i in self.descriptors
                                    if i.startswith("C-D-")]),
            "class_partition": dict(EXPECTED_CLASSES),
            "binding_board": dict(EXPECTED_BOARD),
        }
