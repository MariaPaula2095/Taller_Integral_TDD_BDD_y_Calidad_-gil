Feature: Quotation registration
  As a purchasing manager
  I want to register the quotations sent by suppliers
  So that I can compare them and choose the best offer

  Background:
    Given an empty quotation service

  Scenario: Register a quotation against an open request
    Given a quotation request "REQ-001" with status "ABIERTA"
    When supplier "900123456" registers a quotation for 1500000
    Then the quotation has status "RECIBIDA"
    And request "REQ-001" has 1 registered quotation

  Scenario: Cannot quote a closed request
    Given a quotation request "REQ-002" with status "CERRADA"
    When supplier "900123456" tries to register a quotation for 1500000
    Then the quotation is rejected with a message containing "not open"
    And request "REQ-002" has 0 registered quotations

  Scenario Outline: Zero or negative amounts are rejected
    Given a quotation request "REQ-003" with status "ABIERTA"
    When supplier "900123456" tries to register a quotation for <amount>
    Then the quotation is rejected with a message containing "greater than zero"
    And request "REQ-003" has 0 registered quotations

    Examples:
      | amount |
      | 0      |
      | -1     |
      | -5000  |
