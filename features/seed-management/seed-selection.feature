@smoke @regression
Feature: Seed management behavior
  As a scan operator
  I want jurisdiction seed handling to be consistent
  So that scan inputs are predictable across runs

  # FTR-SEED-001
  Scenario: Select one jurisdiction seed for validation
    Given a maintained TOON seed set with one file per jurisdiction
    When I run URL validation for one selected seed
    Then only that seed's domains are validated in the run
    And the run metadata records the selected jurisdiction

  # FTR-SEED-002
  Scenario: Split import data into per-jurisdiction seed files
    Given a source import with domains from multiple US jurisdictions
    When I run the seed splitting process
    Then one TOON seed file is produced per jurisdiction
    And the federal scope is preserved in a dedicated seed file
