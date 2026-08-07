"""A35 evaluator — Builder B (independent verifier), governed by spec V005.

Independence attestation (RD-22 custody ruling): this package consumes only the
sealed specification, sealed schemas/contracts, immutable inputs, and the
authorized runtime pin. It imports no producer code, no expected-verdict
generator, no comparison function, and no mutable receipt.
"""

__all__ = [
    "canonical_json",
    "hashing",
    "spec_census",
    "contracts",
    "replay",
    "runtime_state",
    "comparison",
    "verify",
]
