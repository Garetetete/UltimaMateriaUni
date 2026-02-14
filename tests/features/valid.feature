Feature: Number Validation API
    Scenario Validating a correct Number
    Given I have a number <number>
    When I validate de number
    Then the resut shoul be <result>
    Examples:
    | number | result |
    | 1234   | true   |
    | 5678   | true   |
    | 9012   | true   |
    | 1123   | false  |
    | 12a4   | false  |
    | 123    | false  |
    | 12345  | false  |