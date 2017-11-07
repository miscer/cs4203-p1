Feature: Encrypting and Decrypting
  Background:
    When I run the following commands:
    """bash
    python -m crypto --profile alice setup Alice
    python -m crypto --profile bob setup Bob
    python -m crypto --profile alice add Bob bob@example.com $(python -m crypto --profile bob export)
    python -m crypto --profile bob add Alice alice@example.com $(python -m crypto --profile alice export)
    """

  Scenario: Encrypting and decrypting through pipes
    When I run the following commands:
    """bash
    echo "Hello, CS4203!" |
    python -m crypto --profile alice encrypt bob@example.com |
    python -m crypto --profile bob decrypt alice@example.com
    """
    Then the output should contain "Hello, CS4203!"

  Scenario: Encrypting and decrypting files
    Given a file named "input.txt" with:
    """
    Hello, CS4203!
    """
    When I run the following commands:
    """bash
    python -m crypto --profile alice encrypt bob@example.com input.txt message.enc
    python -m crypto --profile bob decrypt alice@example.com message.enc output.txt
    """
    Then the file "output.txt" should contain "Hello, CS4203!"
