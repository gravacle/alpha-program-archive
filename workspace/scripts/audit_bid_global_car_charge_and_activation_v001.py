#!/usr/bin/env python3
"""Fail-closed finite-CAR audit of charge and activation projectors."""

from __future__ import annotations

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def annihilator(mode: int, mode_count: int) -> np.ndarray:
    identity = np.eye(2, dtype=complex)
    z = np.array([[1, 0], [0, -1]], dtype=complex)
    lowering = np.array([[0, 1], [0, 0]], dtype=complex)
    factors = []
    for index in range(mode_count):
        if index < mode:
            factors.append(z)
        elif index == mode:
            factors.append(lowering)
        else:
            factors.append(identity)
    result = factors[0]
    for factor in factors[1:]:
        result = np.kron(result, factor)
    return result


def fock_permutation(mode_map: tuple[int, ...]) -> np.ndarray:
    mode_count = len(mode_map)
    dimension = 1 << mode_count
    result = np.zeros((dimension, dimension), dtype=complex)
    for source in range(dimension):
        occupied = [
            index
            for index in range(mode_count)
            if source & (1 << (mode_count - 1 - index))
        ]
        mapped = [mode_map[index] for index in occupied]
        inversions = sum(
            left > right
            for position, left in enumerate(mapped)
            for right in mapped[position + 1 :]
        )
        target = 0
        for index in mapped:
            target |= 1 << (mode_count - 1 - index)
        result[target, source] = -1.0 if inversions % 2 else 1.0
    return result


def spectral_projector(
    diagonal_values: np.ndarray, predicate
) -> np.ndarray:
    return np.diag([1.0 if predicate(value) else 0.0 for value in diagonal_values])


def main() -> None:
    # Two particle-spin modes followed by their two antiparticle partners.
    mode_count = 4
    annihilators = tuple(annihilator(index, mode_count) for index in range(mode_count))
    identity = np.eye(1 << mode_count, dtype=complex)
    for left, a_left in enumerate(annihilators):
        for right, a_right in enumerate(annihilators):
            anticommutator = (
                a_left @ a_right.conj().T + a_right.conj().T @ a_left
            )
            expected = identity if left == right else np.zeros_like(identity)
            require(
                np.allclose(anticommutator, expected),
                f"CAR relation failed for modes {left},{right}",
            )

    numbers = tuple(a.conj().T @ a for a in annihilators)
    charge = numbers[0] + numbers[1] - numbers[2] - numbers[3]
    require(np.allclose(charge, charge.conj().T), "charge is not self-adjoint")
    charge_values = np.real(np.diag(charge))
    require(
        set(np.rint(charge_values).astype(int)) == {-2, -1, 0, 1, 2},
        "finite CAR charge spectrum is not the expected integer set",
    )

    theta = 0.713
    compact_action = np.diag(np.exp(1j * theta * charge_values))
    for index, annihilation in enumerate(annihilators):
        expected_phase = np.exp(-1j * theta) if index < 2 else np.exp(1j * theta)
        transformed = compact_action @ annihilation @ compact_action.conj().T
        require(
            np.allclose(transformed, expected_phase * annihilation),
            f"compact U1 action failed on mode {index}",
        )

    p_zero = spectral_projector(charge_values, lambda value: abs(value) < 1e-12)
    p_plus = spectral_projector(charge_values, lambda value: value > 0.5)
    p_minus = spectral_projector(charge_values, lambda value: value < -0.5)
    p_charged = p_plus + p_minus
    for name, projector in (
        ("zero", p_zero),
        ("plus", p_plus),
        ("minus", p_minus),
        ("charged", p_charged),
    ):
        require(
            np.allclose(projector @ projector, projector),
            f"{name} spectral projector is not idempotent",
        )
    require(
        np.allclose(p_zero + p_plus + p_minus, identity),
        "charge spectral projectors are incomplete",
    )
    charge_squared = charge @ charge
    require(
        not np.allclose(charge_squared, p_charged),
        "Q squared was incorrectly accepted on the full spectrum",
    )

    # Fermionic second quantization of p0<->a0 and p1<->a1.
    charge_swap = fock_permutation((2, 3, 0, 1))
    require(
        np.allclose(charge_swap @ charge.conjugate() @ charge_swap.conj().T, -charge),
        "antiunitary charge conjugation does not reverse Q",
    )
    require(
        np.allclose(
            charge_swap @ p_plus.conjugate() @ charge_swap.conj().T,
            p_minus,
        ),
        "charge conjugation does not exchange orientation projectors",
    )
    require(
        np.allclose(
            charge_swap @ p_charged.conjugate() @ charge_swap.conj().T,
            p_charged,
        ),
        "charge conjugation does not preserve charged access",
    )

    # Exact primitive quotient: vacuum and one excitation only.
    one_excitation_mask = np.array(
        [
            abs(sum(float(np.real(number[index, index])) for number in numbers) - 1.0)
            < 1e-12
            for index in range(identity.shape[0])
        ]
    )
    primitive_mask = one_excitation_mask | (
        np.sum(np.stack([np.real(np.diag(number)) for number in numbers]), axis=0)
        < 0.5
    )
    require(
        np.allclose(
            np.diag(charge_values[primitive_mask] ** 2),
            np.diag(np.diag(p_charged)[primitive_mask]),
        ),
        "Q squared does not recover access on the primitive quotient",
    )

    print(f"finite_CAR_modes={mode_count}")
    print(f"finite_Fock_dimension={identity.shape[0]}")
    print("CAR_relations=PASS")
    print("compact_vector_U1_action=PASS")
    print("integer_charge_spectrum=-2,-1,0,1,2")
    print("full_spectral_access_projectors=PASS")
    print("full_spectrum_Q_squared_access=REJECTED")
    print("primitive_vacuum_plus_one_Q_squared_access=PASS")
    print("antiunitary_charge_conjugation_sector_action=PASS")
    print("pure_branch_controlled_coupling_conditions=DISCLOSED_NOT_DERIVED_FROM_U1")
    print("complete_connected_source_record_action_derived=FALSE")
    print("alpha_computed=FALSE")
    print("BID_GLOBAL_CAR_CHARGE_ACTIVATION_AUDIT=PASS_BLOCKED")


if __name__ == "__main__":
    main()
