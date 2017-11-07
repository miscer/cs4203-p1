Feature: Exporting
  Scenario: Exporting my public key
    Given I run `python -m crypto setup Jacob`
    When I run `python -m crypto export`
    Then the output should contain "Your public key"
      And the output should match /^[a-z0-9]{64}$/

  Scenario: Exporting other public key
    Given I run `python -m crypto add Anne anne@example.com 5cbb894732849a28fd0231f30f118840836b3a62017aba712d2b6683c8f21136`
    When I run `python -m crypto export anne@example.com`
    Then the output should contain "5cbb894732849a28fd0231f30f118840836b3a62017aba712d2b6683c8f21136"