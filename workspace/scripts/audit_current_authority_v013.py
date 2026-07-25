#!/usr/bin/env python3
"""Snapshot-based semantic authority audit for CURRENT_AUTHORITY_LEDGER_V013."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import stat
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

EXPECTED_TOP_LEVEL_KEYS = {
    "schema_version",
    "current_authority",
    "parent_authority",
    "new_sealed_results",
    "subordinate_result_bindings",
    "new_level_1_postulates",
    "superseded_or_rejected_since_v010",
    "execution_state_additions",
    "protected_parent_flags",
}

EXPECTED_CURRENT_AUTHORITY = {
    "ledger": "CURRENT_AUTHORITY_LEDGER_V013.json",
    "audit": "scripts/audit_current_authority_v013.py",
    "test": "tests/test_current_authority_v013.py",
    "result": "results/current_authority_v013.json",
}

EXPECTED_PARENT_AUTHORITY = {
    "ledger": "CURRENT_AUTHORITY_LEDGER_V010.json",
    "ledger_seal": "CURRENT_AUTHORITY_LEDGER_V010.seal.sha256",
    "audit": "scripts/audit_current_authority_v010.py",
    "audit_seal": "scripts/audit_current_authority_v010.seal.sha256",
    "test": "tests/test_current_authority_v010.py",
    "test_seal": "tests/test_current_authority_v010.seal.sha256",
    "result": "results/current_authority_v010.json",
    "result_seal": "results/current_authority_v010.seal.sha256",
}

EXPECTED_NEW_SEALED_RESULTS = {
    "reduced_source_record_generator_structure":
        "SOURCE_RECORD_GENERATOR_STRUCTURE_GATE_V002.md",
    "conditional_pointer_commutant":
        "DURABLE_POINTER_CLOSURE_OPERATOR_SELECTOR_GATE_V002.md",
    "relative_record_orthogonalization_budget":
        "BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md",
    "conditional_source_flux_record_holonomy":
        "SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003.md",
}

EXPECTED_SUBORDINATE_BINDINGS = {
    "reduced_source_record_generator_structure":
        "results/source_record_generator_structure_v002.json",
    "conditional_pointer_commutant":
        "results/durable_pointer_closure_operator_selector_v002.json",
    "relative_record_orthogonalization_budget":
        "results/boundary_record_onset_saturation_action_v003.json",
    "conditional_source_flux_record_holonomy":
        "results/source_flux_conditioned_record_write_v003.json",
}

EXPECTED_NEW_LEVEL_1_POSTULATES = {
    "relative_record_onset_saturation":
        "BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md",
    "zero_flux_no_charged_write":
        "SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003.md",
}

EXPECTED_SUPERSEDED = {
    "SOURCE_RECORD_GENERATOR_STRUCTURE_GATE_V001.md":
        "SUPERSEDED_UNCOMPUTED_KERNEL_DIMENSIONS_AND_OVERCLAIMED_NONZERO_EXCHANGE",
    "DURABLE_POINTER_CLOSURE_OPERATOR_SELECTOR_GATE_V001.md":
        "REJECTED_IDENTITY_QUOTIENT_LEAKED_INTO_SOURCE_ACTION",
    "BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V001.md":
        "REJECTED_PRIVILEGED_STATIONARY_BRANCH",
    "BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V002.md":
        "REJECTED_COMMON_HAMILTONIAN_AND_PHYSICAL_ACTION_OVERCLAIMS",
    "SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V001.md":
        "REJECTED_GLOBAL_PHASE_AS_PHYSICAL_RELATIVE_PHASE",
    "SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V002.md":
        "SUPERSEDED_UNNORMALIZED_AND_UNQUALIFIED_PHASE_OBSERVABILITY",
    "CURRENT_AUTHORITY_LEDGER_V012.json":
        "REJECTED_INCOMPLETE_PARENT_SEMANTIC_FREEZE_AND_UNBOUND_SUBORDINATE_RESULTS",
    "scripts/audit_current_authority_v012.py":
        "REJECTED_PARENT_DRIFT_HARDLINK_ALIAS_AND_SNAPSHOT_GAPS",
    "tests/test_current_authority_v012.py":
        "SUPERSEDED_INCOMPLETE_ADVERSARIAL_COVERAGE",
    "results/current_authority_v012.json":
        "REJECTED_RESULT_OF_UNSEALED_FAILED_V012_AUTHORITY",
}

EXPECTED_PROTECTED = {
    "alpha_computed": False,
    "complete_parameter_free_Q_spec_frozen": False,
    "complete_source_record_closure_action_uniquely_derived": False,
    "coupling_evaluation_authorized": False,
    "proof_authorized": False,
    "record_generated_source_mass_derived": False,
    "spectral_evaluation_authorized": False,
    "unique_causal_record_cell_derived": False,
}

EXPECTED_PARENT_STATE = {
    "pointwise_active_relative_U1_derived": True,
    "smooth_principal_relative_U1_bundle_adopted_Level_1": True,
    "auxiliary_compact_connection_adopted_Level_1": True,
    "physical_public_EM_connection_derived": False,
    "transport_only_phase_complete_principle_adopted": True,
    "transport_only_phase_complete_principle_is_derived_theorem": False,
    "source_branch_charge_basis_corrected": True,
    "source_record_odd_component_identity_adopted_Level_1": True,
    "source_record_odd_component_principle_forward_sealed": True,
    "source_record_odd_component_authority_active": True,
    "source_record_odd_component_principle_target_value_free": True,
    "source_record_odd_component_principle_target_blind": False,
    "source_record_odd_component_identity_derived": False,
    "source_block_identified_with_complete_closure_map": False,
    "scalar_pseudoscalar_bilinear_class_declared": True,
    "displayed_fixed_time_block_algebra_verified": True,
    "free_mass_shell_relation_for_supplied_background_derived": True,
    "operator_tensor_structure_derived_from_record_principles": False,
    "declared_trial_potential_algebra_verified": True,
    "declared_trial_potentials_have_distinct_radial_stationary_points": True,
    "positive_trial_radial_second_derivatives_verified": True,
    "physical_closure_stability_derived": False,
    "historical_target_blindness_established_for_trial_potentials": False,
    "two_complete_admissible_closure_actions_exhibited": False,
    "full_Q_spec_nonuniqueness_proved": False,
    "response_inequivalence_evaluated": False,
    "binary_gap_interval_relation_is_conditional": True,
    "physical_binary_record_generator_derived": False,
    "controlled_x_write_candidate_unique": False,
    "durable_record_generator_derived": False,
    "complete_source_record_closure_action_uniquely_derived": False,
    "closure_magnitude_presently_derived": False,
    "closure_phase_presently_derived": False,
    "record_generated_free_mass_parameter_derived": False,
    "record_generated_source_mass_derived": False,
    "interacting_source_pole_and_residue_derived": False,
    "durable_record_dynamics_derived": False,
    "current_premises_admit_response_inequivalent_parent_actions": True,
    "complete_parent_action_uniquely_derived": False,
    "coupled_record_bundle_tree_relation_derived": True,
    "coupled_record_bundle_charge_radius_derived": False,
    "finite_cell_flux_protocol_frozen": True,
    "complete_dynamical_parent_kernel_frozen": False,
    "complete_parameter_free_Q_spec_frozen": False,
    "unique_causal_record_cell_derived": False,
    "unique_finite_coincident_extension_derived": False,
    "finite_flux_response_evaluated": False,
    "finite_c_F2_deformation_excluded_inside_adopted_primitive_branch": True,
    "finite_c_F2_deformation_excluded_as_universal_theorem": False,
    "spectral_evaluation_authorized": False,
    "coupling_evaluation_authorized": False,
    "alpha_computed": False,
    "proof_authorized": False,
}

EXPECTED_PARENT_RESULT = {
    "status": "PASS_AUTHORITY_V010_IDENTITY_SEALED_MAGNITUDE_BLOCKED",
    "missing_files": [],
    "verified_new_seals": 13,
    "verified_execution_state_keys": 53,
    "source_record_odd_component_identity_adopted_Level_1": True,
    "free_mass_shell_relation_for_supplied_background_derived": True,
    "closure_magnitude_presently_derived": False,
    "record_generated_source_mass_derived": False,
    "alpha_computed": False,
    "proof_authorized": False,
    "scope": "authority_and_seal_consistency_only",
}

NEW_SEALED_INPUTS = {
    "SOURCE_RECORD_GENERATOR_STRUCTURE_GATE_V002.md":
        "SOURCE_RECORD_GENERATOR_STRUCTURE_GATE_V002.seal.sha256",
    "scripts/audit_source_record_generator_structure_v002.py":
        "scripts/audit_source_record_generator_structure_v002.seal.sha256",
    "tests/test_source_record_generator_structure_v002.py":
        "tests/test_source_record_generator_structure_v002.seal.sha256",
    "results/source_record_generator_structure_v002.json":
        "results/source_record_generator_structure_v002.seal.sha256",
    "DURABLE_POINTER_CLOSURE_OPERATOR_SELECTOR_GATE_V002.md":
        "DURABLE_POINTER_CLOSURE_OPERATOR_SELECTOR_GATE_V002.seal.sha256",
    "scripts/audit_durable_pointer_closure_operator_selector_v002.py":
        "scripts/audit_durable_pointer_closure_operator_selector_v002.seal.sha256",
    "tests/test_durable_pointer_closure_operator_selector_v002.py":
        "tests/test_durable_pointer_closure_operator_selector_v002.seal.sha256",
    "results/durable_pointer_closure_operator_selector_v002.json":
        "results/durable_pointer_closure_operator_selector_v002.seal.sha256",
    "BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md":
        "BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.seal.sha256",
    "scripts/audit_boundary_record_onset_saturation_action_v003.py":
        "scripts/audit_boundary_record_onset_saturation_action_v003.seal.sha256",
    "tests/test_boundary_record_onset_saturation_action_v003.py":
        "tests/test_boundary_record_onset_saturation_action_v003.seal.sha256",
    "results/boundary_record_onset_saturation_action_v003.json":
        "results/boundary_record_onset_saturation_action_v003.seal.sha256",
    "SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003.md":
        "SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003.seal.sha256",
    "scripts/audit_source_flux_conditioned_record_write_v003.py":
        "scripts/audit_source_flux_conditioned_record_write_v003.seal.sha256",
    "tests/test_source_flux_conditioned_record_write_v003.py":
        "tests/test_source_flux_conditioned_record_write_v003.seal.sha256",
    "results/source_flux_conditioned_record_write_v003.json":
        "results/source_flux_conditioned_record_write_v003.seal.sha256",
}

APPROVED_SEALED_ARTIFACT_SHA256 = {
    "CURRENT_AUTHORITY_LEDGER_V010.json":
        "5c6c09064d5d4e58ead79108498655891890ea95d1a3cb8350b04f4f8d34b7cc",
    "CURRENT_AUTHORITY_LEDGER_V010.seal.sha256":
        "29dd1f5f428c6d866fd35507abba6dfa9c6f70efa217f554dec6261302aa1e10",
    "scripts/audit_current_authority_v010.py":
        "2d93d3c479a8aff816a2992bd430efa45273e4dc7dd0c1e1439765a3be01aab9",
    "scripts/audit_current_authority_v010.seal.sha256":
        "7e1efc174cdafc0f07ebe4843f6ef8bc2f2f276917071b205860d18f516cd31d",
    "tests/test_current_authority_v010.py":
        "0432d4665637d5bf166c29aa18a714d1a7f241e3c1cbbc31c5a935fa3364b721",
    "tests/test_current_authority_v010.seal.sha256":
        "7feb5bad78a18e9388c0a550b0262b2d5b44d701144b542ad70488591d07d510",
    "results/current_authority_v010.json":
        "2c3bc105d3f0c0b338a2032d449f6fc9f526ff21cf55446ca1b41dc7a27643d6",
    "results/current_authority_v010.seal.sha256":
        "fcb813380b4e1727f285701ed57cf4d660f641160aa0316d4cc2f75601f2e683",
    "SOURCE_RECORD_GENERATOR_STRUCTURE_GATE_V002.md":
        "bf530ddec40480919776611e15d0c6104f8ce7c3e8307af0d849dbe3994ad64f",
    "SOURCE_RECORD_GENERATOR_STRUCTURE_GATE_V002.seal.sha256":
        "415db35aa2fd6dff5d5afb9caa1a274f4d28cc23d888ae689bbb1604c61a8179",
    "scripts/audit_source_record_generator_structure_v002.py":
        "12beebe3c347a3f48dd45149f609d972d0b6cdefe5aec50a0a28c117aacce732",
    "scripts/audit_source_record_generator_structure_v002.seal.sha256":
        "af2c2366221de8b2858a81846215eb1b60516947ad6b0114640c205be9624806",
    "tests/test_source_record_generator_structure_v002.py":
        "b80d5dc4fec3c697d7a2915e664949955078f92dcea079e7ae90fae475076dd4",
    "tests/test_source_record_generator_structure_v002.seal.sha256":
        "b52a47d86989634bd1994d3dd042aa1e62992f5acdcaa0b75d6f16108df10fbf",
    "results/source_record_generator_structure_v002.json":
        "0b5794dc8eb7edccd184499b1ddd18e4be1b5f39ac584b1df31643dbbed9b407",
    "results/source_record_generator_structure_v002.seal.sha256":
        "aa2fa4c5e7842d75447ab2e3193da10f8cc1a94d0fd15f1d792237589ed9f423",
    "DURABLE_POINTER_CLOSURE_OPERATOR_SELECTOR_GATE_V002.md":
        "ace96d21d5c9116565357cf68844685056aac21967dd9132a2ff7be83c72d50b",
    "DURABLE_POINTER_CLOSURE_OPERATOR_SELECTOR_GATE_V002.seal.sha256":
        "4db6c285771e4fb9a9a9e6fe6957b70bc71031658b58f159d452f9bd80644aab",
    "scripts/audit_durable_pointer_closure_operator_selector_v002.py":
        "49e8c6eb9061078cf2849b5c7fc22e9e9e64414e730c1fbe790e0a5a430a86c7",
    "scripts/audit_durable_pointer_closure_operator_selector_v002.seal.sha256":
        "0e50749d78cada88a9c4be84aae93426d4c81d18e845dbff55998b7438862350",
    "tests/test_durable_pointer_closure_operator_selector_v002.py":
        "bff923efa588679801a6075ded0462d855608567e8ffce32f2bd796f9585991f",
    "tests/test_durable_pointer_closure_operator_selector_v002.seal.sha256":
        "8ce96bce0ade1455cb823d243c15cef391287ed0f08c3f31abb7b844a343d849",
    "results/durable_pointer_closure_operator_selector_v002.json":
        "80ca74cb737b0748d8677c50ff305f01a3038669ccc0c50a59361e5dff8e7c99",
    "results/durable_pointer_closure_operator_selector_v002.seal.sha256":
        "f4a291a1684bc568b6e8a8668011eda6d051cd067a0c6053398678a784585f93",
    "BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md":
        "cc113a169dd96c5f374d7af619362ef43a1da2b948840ff37861da3f6786e22c",
    "BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.seal.sha256":
        "3706063bec1f943614b2dd9ed6024c93c201daf3a4f2e275d741e6291ef9be73",
    "scripts/audit_boundary_record_onset_saturation_action_v003.py":
        "e30b12bbb801ce92e169fb961e33f00775255029daea9706ff9598166d4858f2",
    "scripts/audit_boundary_record_onset_saturation_action_v003.seal.sha256":
        "060cec05631241aefc67d3591668bc073d5a40124207b5218a94f55fd0107063",
    "tests/test_boundary_record_onset_saturation_action_v003.py":
        "d2bca8c3d69348a1cfce2dcf7f7b42d8658689354049303fbd05954b838e51be",
    "tests/test_boundary_record_onset_saturation_action_v003.seal.sha256":
        "a5b24a746b4af931a584a18e6b60f305e5c20e27bb054b4cbfa6af8534244e27",
    "results/boundary_record_onset_saturation_action_v003.json":
        "3b23c9df9a213c962325f9ee3ee5e1f7004f25cf7f886e776060ef466574b817",
    "results/boundary_record_onset_saturation_action_v003.seal.sha256":
        "2f102454f398327fd6f83effdcd479d29882ba201c821e16b725bd12c145527f",
    "SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003.md":
        "15a9ac602a3c1afa262675d059284618a6c6397abd46fef669b7a070530b3a64",
    "SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003.seal.sha256":
        "9f1fe0e643ef5c06043b73b08409a84bc94395a6f9786447ed435c1e2aefbda2",
    "scripts/audit_source_flux_conditioned_record_write_v003.py":
        "0be39a7bf0afab320e660cf134ea52a5b031d7d6dea06e1e0f0d9fa5bbde9d40",
    "scripts/audit_source_flux_conditioned_record_write_v003.seal.sha256":
        "ecc5e88a8744787e0c20d58aa228960ede39d315035fcd286b813ca022668b31",
    "tests/test_source_flux_conditioned_record_write_v003.py":
        "68105e5e3cd6df0f3646bcef4560f1f6a440af04505fa4841beac5f162da4fa1",
    "tests/test_source_flux_conditioned_record_write_v003.seal.sha256":
        "e507dc365da70de8fb08b1f061d8c09470943dc95772dc173b2ff8589d88fcf3",
    "results/source_flux_conditioned_record_write_v003.json":
        "d38356b63f4b539f2121ccc90a0df66aa5a32c5d9c5ec912129f089477085919",
    "results/source_flux_conditioned_record_write_v003.seal.sha256":
        "67b8dafe1477a8d828fb6ff6220c7ac9e475dd118e5dd68cfa5265f9467e8c51",
}

EXPECTED_SUBORDINATE_RESULTS = {
    "reduced_source_record_generator_structure": {
        "status": "PASS_REDUCED_SOURCE_RECORD_GENERATOR_RANKS_ONLY",
        "full_pauli_product_domain_dimension": 16,
        "reduced_odd_odd_linear_map_rank": 12,
        "reduced_odd_odd_kernel_dimension": 4,
        "reduced_odd_odd_kernel_basis": ["XX", "XY", "YX", "YY"],
        "conditional_restricted_commutator_rank": 2,
        "conditional_exchange_kernel_dimension": 2,
        "conditional_exchange_basis": ["XX+YY", "XY-YX"],
        "reduced_source_record_product_factor_declared": True,
        "minimal_product_carrier_derived": False,
        "complete_closure_operator_space_dimension_derived": False,
        "combined_grading_conservation_derived": False,
        "nonzero_exchange_derived": False,
        "exchange_magnitude_derived": False,
        "physical_record_interval_derived": False,
        "durable_record_dynamics_derived": False,
        "source_mass_derived": False,
        "spectral_evaluation_authorized": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "scope": "exact_linear_algebra_on_declared_reduced_factor_only",
    },
    "conditional_pointer_commutant": {
        "status": "PASS_CONDITIONAL_POINTER_COMMUTANT_CLASSIFICATION_ONLY",
        "primitive_record_algebra_input_inherited_from_sealed_authority": True,
        "endpoint_projectors_input_declared": True,
        "endpoint_projector_axioms_verified": True,
        "hermitian_domain_dimension": 4,
        "hermitian_domain_basis_rank": 4,
        "pointer_commutator_map_rank": 2,
        "hermitian_pointer_commutant_dimension": 2,
        "commutant_basis": ["I", "P1-P0"],
        "endpoint_contrast_equivalence_adopted": True,
        "endpoint_contrast_quotient_dimension": 1,
        "canonical_contrast_representative_defined": True,
        "canonical_contrast_representative": "P1_minus_P0",
        "canonical_contrast_square": "I",
        "identity_quotient_scope": "relative_endpoint_contrast_only",
        "post_closure_invariance_commutator_equivalence_derived": True,
        "physical_post_closure_invariance_realized": False,
        "physical_contrast_normalization_derived": False,
        "physical_pointer_operator_selected": False,
        "common_source_term_excluded": False,
        "source_scalar_embedding_selected": False,
        "complete_closure_operator_selected": False,
        "record_write_dynamics_derived": False,
        "physical_durability_derived": False,
        "kappa_I_derived": False,
        "kappa_Z_derived": False,
        "record_generated_source_mass_derived": False,
        "spectral_evaluation_authorized": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "scope": "conditional_post_closure_commutant_on_primitive_M2_factor_only",
    },
    "relative_record_orthogonalization_budget": {
        "status": "PASS_RELATIVE_FS_BUDGET_CONDITIONAL_PHYSICAL_ACTION_OPEN",
        "common_closed_dilation_declared": True,
        "conditional_overlap_object": "U0_dagger_U1",
        "conditional_overlap_relative_unitary_identity_derived": True,
        "relative_orthogonalization_bound_imported": True,
        "relative_endpoint_overlap_computed": 0,
        "orthogonality_budget_pi_over_two_derived": True,
        "relative_onset_saturation_derived": False,
        "relative_onset_saturation_adopted_Level_1": True,
        "relative_FS_budget_fixed_conditional_on_adopted_rule": True,
        "relative_FS_budget": "pi*hbar/2",
        "relative_generator_coefficient": "pi*hbar/(2*tau_star)",
        "symmetric_branch_product_verified": True,
        "physical_dynamical_action_fixed": False,
        "absolute_one_branch_energy_fixed": False,
        "arbitrary_common_additive_hamiltonian_cancels": False,
        "factored_common_left_unitary_cancels": True,
        "orthogonal_reduced_record_supports_derived": False,
        "physical_durability_derived": False,
        "unique_causal_record_interval_numerically_derived": False,
        "relative_generator_identified_with_pointer_coefficient": False,
        "relative_generator_identified_with_source_mass": False,
        "record_generated_source_mass_derived": False,
        "spectral_evaluation_authorized": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "scope": "closed_dilation_relative_FS_bound_and_adopted_saturation_only",
    },
    "conditional_source_flux_record_holonomy": {
        "status": "PASS_CONDITIONAL_SOURCE_FLUX_HOLONOMY_PHASE_OBSERVABILITY_OPEN",
        "unit_source_flux_sector_inherited": True,
        "zero_flux_no_charged_write_adopted": True,
        "relative_onset_saturation_inherited_as_adopted": True,
        "source_flux_spectrum": [0, 1],
        "equatorial_holonomy_classification_imported_analytic_result": True,
        "chosen_Y_representative_verified": True,
        "conditional_record_changing_holonomy_fixed": True,
        "integrated_record_changing_holonomy":
            "(pi/2)*Q_Sigma_tensor_Y_up_to_rephasing",
        "candidate_write_preserves_declared_flux_sector": True,
        "physical_source_flux_nondemolition_derived": False,
        "joint_density_changes_in_fixed_source_basis": True,
        "reduced_record_density_invariant": True,
        "coherent_flux_superposition_physically_admissible_derived": False,
        "source_phase_reference_supplied": False,
        "source_relative_phase_observability_derived": False,
        "gauge_invariant_phase_effect_derived": False,
        "complete_physical_write_operator_derived": False,
        "physical_dynamical_action_fixed": False,
        "complete_source_record_environment_operator_derived": False,
        "physical_durability_derived": False,
        "record_generated_source_mass_derived": False,
        "spectral_evaluation_authorized": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "scope": "conditional_zero_or_one_local_flux_ready_subspace_holonomy_only",
    },
}

SUBORDINATE_PROTECTED_FALSE = {
    "reduced_source_record_generator_structure": {
        "minimal_product_carrier_derived",
        "complete_closure_operator_space_dimension_derived",
        "combined_grading_conservation_derived",
        "nonzero_exchange_derived",
        "exchange_magnitude_derived",
        "physical_record_interval_derived",
        "durable_record_dynamics_derived",
        "source_mass_derived",
        "spectral_evaluation_authorized",
        "coupling_evaluation_authorized",
        "alpha_computed",
        "proof_authorized",
    },
    "conditional_pointer_commutant": {
        "physical_post_closure_invariance_realized",
        "physical_contrast_normalization_derived",
        "physical_pointer_operator_selected",
        "common_source_term_excluded",
        "source_scalar_embedding_selected",
        "complete_closure_operator_selected",
        "record_write_dynamics_derived",
        "physical_durability_derived",
        "kappa_I_derived",
        "kappa_Z_derived",
        "record_generated_source_mass_derived",
        "spectral_evaluation_authorized",
        "coupling_evaluation_authorized",
        "alpha_computed",
        "proof_authorized",
    },
    "relative_record_orthogonalization_budget": {
        "relative_onset_saturation_derived",
        "physical_dynamical_action_fixed",
        "absolute_one_branch_energy_fixed",
        "arbitrary_common_additive_hamiltonian_cancels",
        "orthogonal_reduced_record_supports_derived",
        "physical_durability_derived",
        "unique_causal_record_interval_numerically_derived",
        "relative_generator_identified_with_pointer_coefficient",
        "relative_generator_identified_with_source_mass",
        "record_generated_source_mass_derived",
        "spectral_evaluation_authorized",
        "coupling_evaluation_authorized",
        "alpha_computed",
        "proof_authorized",
    },
    "conditional_source_flux_record_holonomy": {
        "physical_source_flux_nondemolition_derived",
        "coherent_flux_superposition_physically_admissible_derived",
        "source_phase_reference_supplied",
        "source_relative_phase_observability_derived",
        "gauge_invariant_phase_effect_derived",
        "complete_physical_write_operator_derived",
        "physical_dynamical_action_fixed",
        "complete_source_record_environment_operator_derived",
        "physical_durability_derived",
        "record_generated_source_mass_derived",
        "spectral_evaluation_authorized",
        "coupling_evaluation_authorized",
        "alpha_computed",
        "proof_authorized",
    },
}

RESULT_SCHEMA = {
    "status": str,
    "schema_version": int,
    "parent_schema_version": int,
    "parent_status": str,
    "verified_authority_roles": int,
    "verified_unique_role_inodes": int,
    "verified_single_link_authority_roles": int,
    "verified_approved_artifact_digests": int,
    "verified_parent_seals": int,
    "verified_new_seals": int,
    "verified_parent_execution_state_keys": int,
    "verified_effective_execution_state_keys": int,
    "verified_delta_addition_keys": int,
    "verified_protected_parent_flags": int,
    "verified_subordinate_results": int,
    "verified_subordinate_result_fields": int,
    "verified_subordinate_protected_false_flags": int,
    "verified_new_level_1_postulates": int,
    "verified_superseded_entries": int,
    "conditional_pointer_commutant_classified": bool,
    "relative_orthogonalization_bound_derived": bool,
    "conditional_source_flux_holonomy_verified": bool,
    "complete_source_record_environment_operator_derived": bool,
    "alpha_computed": bool,
    "proof_authorized": bool,
    "scope": str,
}


@dataclass(frozen=True)
class FileSnapshot:
    role: str
    name: str
    data: bytes
    digest: str
    device: int
    inode: int
    link_count: int


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def strict_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return (
            set(left) == set(right)
            and all(strict_equal(left[key], right[key]) for key in left)
        )
    if isinstance(left, list):
        return (
            len(left) == len(right)
            and all(strict_equal(a, b) for a, b in zip(left, right))
        )
    return left == right


def reject_duplicate_object_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        require(key not in out, f"Duplicate JSON key: {key}")
        out[key] = value
    return out


def loads_strict(text: str) -> Any:
    return json.loads(text, object_pairs_hook=reject_duplicate_object_keys)


def validate_exact_map(
    actual: dict[str, Any],
    expected: dict[str, Any],
    label: str,
) -> None:
    require(type(actual) is dict, f"{label} is not an object")
    require(set(actual) == set(expected), f"{label} key drift")
    mismatches = {
        key: {"expected": expected[key], "actual": actual[key]}
        for key in sorted(expected)
        if not strict_equal(actual[key], expected[key])
    }
    require(not mismatches, f"{label} mismatches: {mismatches}")


def _snapshot_flags(directory: bool) -> int:
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    require(nofollow != 0, "O_NOFOLLOW is unavailable")
    flags = os.O_RDONLY | nofollow
    flags |= getattr(os, "O_CLOEXEC", 0)
    if directory:
        odirectory = getattr(os, "O_DIRECTORY", 0)
        require(odirectory != 0, "O_DIRECTORY is unavailable")
        flags |= odirectory
    return flags


def snapshot_regular_file(root: Path, name: str, role: str) -> FileSnapshot:
    require(type(name) is str and bool(name), f"{role} path is not a nonempty string")
    relative = Path(name)
    require(not relative.is_absolute(), f"{role} path is absolute")
    require(relative.parts not in ((), (".",)), f"{role} path is empty")
    require(".." not in relative.parts, f"{role} path escapes with '..'")

    descriptors: list[int] = []
    try:
        root_fd = os.open(str(root), _snapshot_flags(directory=True))
        descriptors.append(root_fd)
        directory_fd = root_fd
        for part in relative.parts[:-1]:
            next_fd = os.open(
                part,
                _snapshot_flags(directory=True),
                dir_fd=directory_fd,
            )
            descriptors.append(next_fd)
            directory_fd = next_fd

        file_fd = os.open(
            relative.parts[-1],
            _snapshot_flags(directory=False),
            dir_fd=directory_fd,
        )
        descriptors.append(file_fd)
        before = os.fstat(file_fd)
        require(stat.S_ISREG(before.st_mode), f"{role} is not a regular file: {name}")
        require(
            before.st_nlink == 1,
            f"{role} has a non-unique hardlink count before snapshot: {name}",
        )

        chunks: list[bytes] = []
        while True:
            chunk = os.read(file_fd, 1024 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
        data = b"".join(chunks)
        after = os.fstat(file_fd)
        require(
            after.st_nlink == 1,
            f"{role} has a non-unique hardlink count after snapshot: {name}",
        )
        require(
            (
                before.st_dev,
                before.st_ino,
                before.st_size,
                before.st_mtime_ns,
                before.st_ctime_ns,
                before.st_nlink,
            )
            == (
                after.st_dev,
                after.st_ino,
                after.st_size,
                after.st_mtime_ns,
                after.st_ctime_ns,
                after.st_nlink,
            ),
            f"{role} changed during snapshot: {name}",
        )
        require(len(data) == before.st_size, f"{role} short read: {name}")
        return FileSnapshot(
            role=role,
            name=name,
            data=data,
            digest=hashlib.sha256(data).hexdigest(),
            device=before.st_dev,
            inode=before.st_ino,
            link_count=before.st_nlink,
        )
    except OSError as error:
        raise RuntimeError(f"Unable to snapshot {role}: {name}: {error}") from error
    finally:
        for descriptor in reversed(descriptors):
            try:
                os.close(descriptor)
            except OSError:
                pass


def authority_role_paths() -> dict[str, str]:
    roles = {
        f"current.{role}": name
        for role, name in EXPECTED_CURRENT_AUTHORITY.items()
    }
    roles.update({
        f"parent.{role}": name
        for role, name in EXPECTED_PARENT_AUTHORITY.items()
    })
    for target, seal_name in NEW_SEALED_INPUTS.items():
        roles[f"new.target:{target}"] = target
        roles[f"new.seal:{target}"] = seal_name
    for name in EXPECTED_SUPERSEDED:
        roles[f"superseded:{name}"] = name
    require(
        len(set(roles.values())) == len(roles),
        "Authority roles contain duplicate paths",
    )
    return roles


def approved_sealed_artifact_paths() -> set[str]:
    return (
        set(EXPECTED_PARENT_AUTHORITY.values())
        | set(NEW_SEALED_INPUTS)
        | set(NEW_SEALED_INPUTS.values())
    )


def verify_approved_artifact_digests(
    snapshots: dict[str, FileSnapshot],
) -> None:
    expected_paths = approved_sealed_artifact_paths()
    require(
        set(APPROVED_SEALED_ARTIFACT_SHA256) == expected_paths,
        "Approved sealed-artifact digest inventory drift",
    )
    role_paths = authority_role_paths()
    snapshots_by_path = {
        path: snapshots[role]
        for role, path in role_paths.items()
        if path in expected_paths
    }
    require(
        set(snapshots_by_path) == expected_paths,
        "Approved sealed-artifact snapshot coverage drift",
    )
    for path, approved_digest in APPROVED_SEALED_ARTIFACT_SHA256.items():
        require(
            snapshots_by_path[path].digest == approved_digest,
            f"Approved artifact digest mismatch: {path}",
        )


def collect_authority_snapshots(root: Path = ROOT) -> dict[str, FileSnapshot]:
    snapshots: dict[str, FileSnapshot] = {}
    inode_roles: dict[tuple[int, int], str] = {}
    for role, name in sorted(authority_role_paths().items()):
        snapshot = snapshot_regular_file(root, name, role)
        inode_key = (snapshot.device, snapshot.inode)
        require(
            inode_key not in inode_roles,
            f"Hardlink authority-role alias: {role} and {inode_roles.get(inode_key)}",
        )
        inode_roles[inode_key] = role
        snapshots[role] = snapshot
    return snapshots


def load_json_snapshot(snapshot: FileSnapshot, label: str) -> dict[str, Any]:
    try:
        value = loads_strict(snapshot.data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise RuntimeError(f"Unable to parse {label}: {error}") from error
    require(type(value) is dict, f"{label} is not a JSON object")
    return value


def verify_seal_snapshots(
    target: FileSnapshot,
    seal: FileSnapshot,
) -> None:
    try:
        fields = seal.data.decode("utf-8").strip().split()
    except UnicodeDecodeError as error:
        raise RuntimeError(f"Seal is not UTF-8: {seal.name}") from error
    require(len(fields) == 2, f"Malformed seal: {seal.name}")
    digest, recorded_name = fields
    require(len(digest) == 64, f"Malformed SHA256 digest: {seal.name}")
    require(
        all(character in "0123456789abcdef" for character in digest),
        f"Non-hex SHA256 digest: {seal.name}",
    )
    require(recorded_name == Path(target.name).name, f"Seal target-name mismatch: {seal.name}")
    require(target.digest == digest, f"Seal mismatch: {target.name}")


def _role_for_new_target(name: str) -> str:
    return f"new.target:{name}"


def _role_for_new_seal(name: str) -> str:
    return f"new.seal:{name}"


def validate_subordinate_results(
    snapshots: dict[str, FileSnapshot],
) -> tuple[dict[str, dict[str, Any]], int]:
    results: dict[str, dict[str, Any]] = {}
    protected_count = 0
    for label, path in EXPECTED_SUBORDINATE_BINDINGS.items():
        result = load_json_snapshot(
            snapshots[_role_for_new_target(path)],
            f"subordinate result {label}",
        )
        validate_exact_map(
            result,
            EXPECTED_SUBORDINATE_RESULTS[label],
            f"subordinate result {label}",
        )
        for key in SUBORDINATE_PROTECTED_FALSE[label]:
            require(key in result, f"Missing subordinate protected flag: {label}.{key}")
            require(type(result[key]) is bool, f"Non-boolean subordinate flag: {label}.{key}")
            require(result[key] is False, f"Promoted subordinate flag: {label}.{key}")
            protected_count += 1
        results[label] = result
    return results, protected_count


def derive_execution_state_additions(
    results: dict[str, dict[str, Any]],
) -> dict[str, bool]:
    generator = results["reduced_source_record_generator_structure"]
    pointer = results["conditional_pointer_commutant"]
    onset = results["relative_record_orthogonalization_budget"]
    flux = results["conditional_source_flux_record_holonomy"]

    durability_values = (
        generator["durable_record_dynamics_derived"],
        pointer["physical_durability_derived"],
        onset["physical_durability_derived"],
        flux["physical_durability_derived"],
    )
    require(
        all(type(value) is bool for value in durability_values),
        "Subordinate durability flags are not boolean",
    )

    return {
        "reduced_source_record_generator_structure_classified": (
            generator["status"] == "PASS_REDUCED_SOURCE_RECORD_GENERATOR_RANKS_ONLY"
            and generator["reduced_odd_odd_linear_map_rank"] == 12
            and generator["reduced_odd_odd_kernel_dimension"] == 4
            and generator["conditional_exchange_kernel_dimension"] == 2
        ),
        "combined_grading_conservation_derived":
            generator["combined_grading_conservation_derived"],
        "nonzero_source_record_exchange_derived":
            generator["nonzero_exchange_derived"],
        "conditional_pointer_commutant_classified": (
            pointer["status"] == "PASS_CONDITIONAL_POINTER_COMMUTANT_CLASSIFICATION_ONLY"
            and pointer["hermitian_pointer_commutant_dimension"] == 2
            and pointer["endpoint_contrast_quotient_dimension"] == 1
        ),
        "physical_pointer_operator_selected":
            pointer["physical_pointer_operator_selected"],
        "physical_contrast_normalization_derived":
            pointer["physical_contrast_normalization_derived"],
        "common_source_term_excluded":
            pointer["common_source_term_excluded"],
        "relative_orthogonalization_bound_derived":
            onset["orthogonality_budget_pi_over_two_derived"],
        "relative_onset_saturation_adopted_Level_1":
            onset["relative_onset_saturation_adopted_Level_1"],
        "physical_dynamical_action_fixed":
            onset["physical_dynamical_action_fixed"]
            or flux["physical_dynamical_action_fixed"],
        "orthogonal_reduced_record_supports_derived":
            onset["orthogonal_reduced_record_supports_derived"],
        "conditional_source_flux_holonomy_verified": (
            flux["chosen_Y_representative_verified"]
            and flux["conditional_record_changing_holonomy_fixed"]
        ),
        "complete_physical_write_operator_derived":
            flux["complete_physical_write_operator_derived"],
        "physical_source_flux_nondemolition_derived":
            flux["physical_source_flux_nondemolition_derived"],
        "coherent_flux_superposition_physically_admissible_derived":
            flux["coherent_flux_superposition_physically_admissible_derived"],
        "source_relative_phase_observability_derived":
            flux["source_relative_phase_observability_derived"],
        "complete_source_record_environment_operator_derived":
            flux["complete_source_record_environment_operator_derived"],
        "physical_durability_derived": any(durability_values),
    }


def validate_result_schema(result: dict[str, Any]) -> None:
    require(type(result) is dict, "V013 result is not an object")
    require(set(result) == set(RESULT_SCHEMA), "V013 result schema drift")
    bad_types = {
        key: {
            "expected": RESULT_SCHEMA[key].__name__,
            "actual": type(result[key]).__name__,
        }
        for key in RESULT_SCHEMA
        if type(result[key]) is not RESULT_SCHEMA[key]
    }
    require(not bad_types, f"V013 result type drift: {bad_types}")


def validate_result_parity(
    stored: dict[str, Any],
    computed: dict[str, Any],
) -> None:
    validate_result_schema(stored)
    validate_result_schema(computed)
    require(strict_equal(stored, computed), "Stored V013 result parity failure")


def evaluate_snapshots(
    snapshots: dict[str, FileSnapshot],
) -> dict[str, Any]:
    require(
        set(snapshots) == set(authority_role_paths()),
        "Authority snapshot role drift",
    )
    require(
        all(snapshot.link_count == 1 for snapshot in snapshots.values()),
        "Authority snapshot contains a non-single-link artifact",
    )
    verify_approved_artifact_digests(snapshots)
    data = load_json_snapshot(snapshots["current.ledger"], "V013 ledger")
    require(type(data) is dict, "V013 ledger is not an object")
    require(set(data) == EXPECTED_TOP_LEVEL_KEYS, "V013 top-level schema drift")
    require(type(data["schema_version"]) is int, "V013 schema is not an integer")
    require(data["schema_version"] == 13, "Unexpected V013 schema")

    validate_exact_map(data["current_authority"], EXPECTED_CURRENT_AUTHORITY,
                       "current authority")
    validate_exact_map(data["parent_authority"], EXPECTED_PARENT_AUTHORITY,
                       "parent authority")
    validate_exact_map(data["new_sealed_results"], EXPECTED_NEW_SEALED_RESULTS,
                       "new sealed results")
    validate_exact_map(data["subordinate_result_bindings"], EXPECTED_SUBORDINATE_BINDINGS,
                       "subordinate result bindings")
    validate_exact_map(data["new_level_1_postulates"], EXPECTED_NEW_LEVEL_1_POSTULATES,
                       "new Level-1 postulates")
    validate_exact_map(data["superseded_or_rejected_since_v010"], EXPECTED_SUPERSEDED,
                       "superseded/rejected map")
    validate_exact_map(data["protected_parent_flags"], EXPECTED_PROTECTED,
                       "protected parent flags")

    for role in ("ledger", "audit", "test", "result"):
        verify_seal_snapshots(
            snapshots[f"parent.{role}"],
            snapshots[f"parent.{role}_seal"],
        )

    parent = load_json_snapshot(snapshots["parent.ledger"], "V010 parent ledger")
    parent_result = load_json_snapshot(snapshots["parent.result"], "V010 parent result")
    require(type(parent.get("schema_version")) is int, "Parent schema is not an integer")
    require(parent["schema_version"] == 10, "Unexpected parent schema")
    validate_exact_map(parent_result, EXPECTED_PARENT_RESULT, "parent result")
    require("execution_state" in parent, "Parent execution state is missing")
    validate_exact_map(parent["execution_state"], EXPECTED_PARENT_STATE,
                       "complete V010 parent execution state")

    for target_name, seal_name in NEW_SEALED_INPUTS.items():
        verify_seal_snapshots(
            snapshots[_role_for_new_target(target_name)],
            snapshots[_role_for_new_seal(target_name)],
        )

    for name in EXPECTED_NEW_SEALED_RESULTS.values():
        require(name in NEW_SEALED_INPUTS, f"New result lacks a sealed gate: {name}")
    for name in EXPECTED_SUBORDINATE_BINDINGS.values():
        require(name in NEW_SEALED_INPUTS, f"Subordinate result lacks a seal: {name}")
    for name in EXPECTED_NEW_LEVEL_1_POSTULATES.values():
        require(name in NEW_SEALED_INPUTS, f"Level-1 postulate lacks a seal: {name}")

    subordinate_results, subordinate_false_count = validate_subordinate_results(snapshots)
    derived_additions = derive_execution_state_additions(subordinate_results)
    validate_exact_map(data["execution_state_additions"], derived_additions,
                       "derived execution-state additions")

    effective_state = {**EXPECTED_PARENT_STATE, **derived_additions}
    require(
        len(effective_state) == len(EXPECTED_PARENT_STATE) + len(derived_additions),
        "V013 additions collide with parent keys",
    )
    require(
        all(type(value) is bool for value in effective_state.values()),
        "Effective state contains non-boolean values",
    )
    for key, expected in EXPECTED_PROTECTED.items():
        require(key in effective_state, f"Missing protected effective flag: {key}")
        require(effective_state[key] is expected, f"Protected flag changed: {key}")

    role_count = len(snapshots)
    subordinate_field_count = sum(len(result) for result in subordinate_results.values())
    out: dict[str, Any] = {
        "status": "PASS_AUTHORITY_V013_PINNED_SNAPSHOT_SEMANTIC_DELTA_ALPHA_BLOCKED",
        "schema_version": 13,
        "parent_schema_version": parent["schema_version"],
        "parent_status": parent_result["status"],
        "verified_authority_roles": role_count,
        "verified_unique_role_inodes": role_count,
        "verified_single_link_authority_roles": role_count,
        "verified_approved_artifact_digests":
            len(APPROVED_SEALED_ARTIFACT_SHA256),
        "verified_parent_seals": 4,
        "verified_new_seals": len(NEW_SEALED_INPUTS),
        "verified_parent_execution_state_keys": len(EXPECTED_PARENT_STATE),
        "verified_effective_execution_state_keys": len(effective_state),
        "verified_delta_addition_keys": len(derived_additions),
        "verified_protected_parent_flags": len(EXPECTED_PROTECTED),
        "verified_subordinate_results": len(subordinate_results),
        "verified_subordinate_result_fields": subordinate_field_count,
        "verified_subordinate_protected_false_flags": subordinate_false_count,
        "verified_new_level_1_postulates": len(EXPECTED_NEW_LEVEL_1_POSTULATES),
        "verified_superseded_entries": len(EXPECTED_SUPERSEDED),
        "conditional_pointer_commutant_classified":
            effective_state["conditional_pointer_commutant_classified"],
        "relative_orthogonalization_bound_derived":
            effective_state["relative_orthogonalization_bound_derived"],
        "conditional_source_flux_holonomy_verified":
            effective_state["conditional_source_flux_holonomy_verified"],
        "complete_source_record_environment_operator_derived":
            effective_state["complete_source_record_environment_operator_derived"],
        "alpha_computed": effective_state["alpha_computed"],
        "proof_authorized": effective_state["proof_authorized"],
        "scope":
            "pinned_single_link_snapshot_semantic_delta_and_stored_parity_only",
    }
    validate_result_schema(out)
    require(out["alpha_computed"] is False, "Alpha was promoted")
    require(out["proof_authorized"] is False, "Proof was authorized")
    return out


def build_result(
    root: Path = ROOT,
) -> dict[str, Any]:
    snapshots = collect_authority_snapshots(root)
    out = evaluate_snapshots(snapshots)
    stored = load_json_snapshot(snapshots["current.result"], "stored V013 result")
    validate_result_parity(stored, out)
    return out


def main() -> None:
    out = build_result()
    print(out["status"])


if __name__ == "__main__":
    main()
