Feature: Setting up
  Scenario: Adding to default profile
    When I run `python -m crypto setup Alice`
    Then the output should contain "Hello Alice"

  Scenario: Adding to different profiles
    When I run `python -m crypto --profile alice setup Alice`
    Then the output should contain "Hello Alice"

    When I run `python -m crypto --profile bob setup Bob`
    Then the output should contain "Hello Bob"