Feature: Listing

  Scenario: Listing added keys
    Given I run `python -m crypto add Alex alex@example.com 4056ff92cd089f988c884e1e18d9caf3c4751ed9993fbaae1f2b7af5060219cb`
      And I run `python -m crypto add Jane jane@example.com 0c9b358e75276a759b4b2d3cb35e8dbb352ee3be47da8e85998815052eb0bd22`
      And I run `python -m crypto add Mark mark@example.com e715655a6bb2c6cc7e26eb4a7743df3cc25bc27edaa70f37790e5f6adf547535`
    When I run `python -m crypto list`
    Then the output should contain "Alex"
      And the output should contain "jane@example.com"
      And the output should contain "e715655a6bb2c6cc7e26eb4a7743df3cc25bc27edaa70f37790e5f6adf547535"