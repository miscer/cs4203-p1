Feature: Hashing

  Scenario Outline: Generating a hash
    Given a file named "file.txt" with:
    """
    Hello, CS4203!
    """
    When I run `python -m crypto hash --hasher <hasher> generate file.txt`
    Then the output should contain exactly "<output>"

    Examples:
      | hasher  | output                                                                                                                           |
      | sha256  | 2c9eabe7c88318810f1b29cf20382e1439c87241bf08ec54aa10ad2999e446ee                                                                 |
      | sha512  | f024466f9facf494872365b0201a5cf298159df3d0455e66af451d4ea5cedde3c84b78a0d353e93fc990dbf6bff1034c131ad86957ce29b78e6be9327f4ec88a |
      | blake2b | 130589b0dbfd4eaaa9da52c6392d271ab0978f78469c882fa5a3e023517d39c5                                                                 |


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