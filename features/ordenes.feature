Feature: Órdenes de compra
  Como jefe de compras
  Quiero aprobar órdenes de compra
  Para gestionar el presupuesto de los proveedores

  Scenario: Aprobar orden dentro del presupuesto
    Given supplier "ACME" has a budget of 10000000
    And a purchase order "OC-100" for supplier "ACME" with amount 5000000
    When I approve the order "OC-100"
    Then the order "OC-100" has status "APROBADA"
    And supplier "ACME" has a remaining budget of 5000000