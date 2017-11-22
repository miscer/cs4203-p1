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

  Scenario Outline: Generating a hash
    Given I use a fixture named "files"

    When I cd to ".."
      And I run the following commands:
      """bash
      python -m crypto --profile alice encrypt bob@example.com files/<file> message.enc
      python -m crypto --profile bob decrypt alice@example.com message.enc output
      """

    Then the output should not contain anything
      And the file "message.enc" should exist
      And the file "output" should exist
      And the file "files/<file>" should be equal to file "output"

    Examples:
      | file       |
      | hello.txt  |
      | puppy.jpg  |
      | spec.pdf   |

  Scenario: Encrypting nonexistent file
    When I run `python -m crypto --profile alice encrypt bob@example.com file.txt message.enc`
    Then it should fail with:
    """
    File does not exist
    """

  Scenario: Decrypting nonexistent file
    When I run `python -m crypto --profile alice decrypt bob@example.com message.enc file.txt`
    Then it should fail with:
    """
    File does not exist
    """
