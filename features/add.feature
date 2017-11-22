Feature: Adding
  Scenario: Adding valid public key
    When I run `python -m crypto add Kevin kevin@example.com 0c9b358e75276a759b4b2d3cb35e8dbb352ee3be47da8e85998815052eb0bd22`
    Then the output should contain "Added Kevin"

  Scenario: Adding invalid public key
    When I run `python -m crypto add Kevin kevin@example.com abc123`
    Then it should fail with:
    """
    The key is not valid
    """
