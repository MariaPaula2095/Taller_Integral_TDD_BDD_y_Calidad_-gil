Feature: Supplier management
  As a purchasing manager
  I want to register and remove suppliers
  So that I keep a reliable supplier directory

  Background:
    Given an empty supplier service

  Scenario: Register a supplier with valid data
    When I register a supplier with NIT "900123456", name "Andina Distributions" and email "sales@andina.co"
    Then supplier "900123456" exists with status "ACTIVO"

  Scenario Outline: Invalid data prevents registering the supplier
    When I try to register a supplier with NIT "<nit>" and email "<email>"
    Then the system rejects the operation
    And supplier "<nit>" does not exist

    Examples:
      | nit       | email            | reason                    |
      | 12345678  | sales@andina.co  | NIT shorter than 9 digits |
      | 900123456 | sales.andina.co  | email without @           |

  Scenario: Deleting a supplier without active orders makes it INACTIVO
    Given a registered supplier with NIT "900123456"
    When I delete supplier "900123456"
    Then supplier "900123456" exists with status "INACTIVO"

  Scenario: Cannot delete a supplier with active orders
    Given a registered supplier with NIT "900123456"
    And supplier "900123456" has an active order
    When I try to delete supplier "900123456"
    Then the system rejects the operation
    And supplier "900123456" exists with status "ACTIVO"
