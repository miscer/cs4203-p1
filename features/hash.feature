Feature: Hashing
  Scenario: Generating a hash
    Given a file named "file.txt" with:
    """
    Hello, CS4203!
    """
    When I run `python -m crypto hash generate file.txt`
    Then the output should contain exactly:
    """
    130589b0dbfd4eaaa9da52c6392d271ab0978f78469c882fa5a3e023517d39c5
    """

  Scenario: Checking a correct hash
    Given a file named "file.txt" with:
    """
    Hello, CS4203!
    """
    When I run `python -m crypto hash check 130589b0dbfd4eaaa9da52c6392d271ab0978f78469c882fa5a3e023517d39c5 file.txt`
    Then the output should contain "All good"

  Scenario: Checking an incorrect hash
    Given a file named "file.txt" with:
    """
    Hello, CS4203!
    """
    When I run `python -m crypto hash check abc file.txt`
    Then the output should contain "something is fishy"