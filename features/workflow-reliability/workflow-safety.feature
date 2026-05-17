@workflow @regression
Feature: Workflow reliability behavior
  As a repository maintainer
  I want workflow automation to be deterministic
  So that scheduled and manual operations are trustworthy

  # FTR-WF-001
  Scenario: Resume or cancel batch validation safely
    Given a batch validation cycle is in progress
    When a maintainer issues resume or cancel controls
    Then workflow state transitions are tracked safely
    And follow-up workflows honor the updated batch state

  # FTR-WF-002
  @site
  Scenario: Gate generated site accessibility checks in CI
    Given the documentation site is generated for CI
    When the site accessibility workflow runs on schedule or manual trigger
    Then Playwright-powered axe checks run against generated pages
    And CI fails when accessibility violations are detected
