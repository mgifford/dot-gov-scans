@smoke @regression
Feature: URL validation lifecycle behavior
  As a maintainer
  I want URL validation rules to be applied consistently
  So that seed quality improves without manual cleanup

  # FTR-VAL-001
  Scenario: Record final URL after redirects
    Given a seed URL that responds with an HTTP redirect
    When validation runs for that URL
    Then the final destination URL is recorded
    And redirect handling is reflected in validation output

  # FTR-VAL-002
  Scenario: Remove URLs only after two consecutive failures
    Given a previously known URL in a seed
    And the URL fails validation in one run
    When the same URL fails validation in the next run
    Then the URL is removed from maintained validation output
    And it is not removed after only one failed run
