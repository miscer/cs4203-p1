Feature: Adding
  Scenario: Adding public key
    When I run `python -m crypto add Kevin kevin@example.com 0c9b358e75276a759b4b2d3cb35e8dbb352ee3be47da8e85998815052eb0bd22`
    Then the output should contain "Added Kevin"