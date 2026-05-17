@smoke @regression
Feature: Reporting behavior
  As an accessibility advocate
  I want generated reports to reflect current scan state
  So that follow-up decisions are evidence-based

  # FTR-REP-001
  Scenario: Generate validation report from metadata
    Given validation metadata exists for recent runs
    When I generate the validation report
    Then a markdown report is produced
    And it includes success and failure trends for reviewed URLs

  # FTR-REP-002
  Scenario: Generate scan progress report artifacts
    Given scan outputs exist across jurisdictions
    When I generate scan progress outputs
    Then report artifacts are updated consistently
    And outputs can be published to the project documentation site
