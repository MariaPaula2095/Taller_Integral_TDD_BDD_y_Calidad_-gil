"""
Módulo de Órdenes de Compra
Implementa la validación de presupuesto y aprobación de órdenes.
"""

class BudgetExceededException(Exception):
    """Excepción lanzada cuando el monto de la orden supera el presupuesto."""
    pass

class InvalidOrderException(Exception):
    """Excepción lanzada cuando la orden no cumple una regla de negocio."""
    pass

class PurchaseOrder:
    def __init__(self, order_id, supplier_nit, amount, status="PENDIENTE"):
        self.order_id = order_id
        self.supplier_nit = supplier_nit
        self.amount = amount
        self.status = status

class OrderService:
    def __init__(self):
        self.orders = {}
        self.budgets = {}

    def assign_budget(self, supplier_nit, amount):
        if amount < 0:
            raise InvalidOrderException("El presupuesto no puede ser negativo.")
        self.budgets[supplier_nit] = amount

    def create_order(self, order_id, supplier_nit, amount):
        if amount <= 0:
            raise InvalidOrderException("El monto de la orden debe ser mayor a cero.")
        self.orders[order_id] = PurchaseOrder(order_id, supplier_nit, amount)
        return self.orders[order_id]

    def approve_order(self, order_id):
        if order_id not in self.orders:
            raise InvalidOrderException("Orden no encontrada.")
        
        order = self.orders[order_id]
        
        if order.status == "APROBADA":
            raise InvalidOrderException("La orden ya ha sido aprobada.")
        
        current_budget = self.budgets.get(order.supplier_nit, 0)
        if order.amount > current_budget:
            raise BudgetExceededException("Presupuesto insuficiente para aprobar la orden.")
        
        self.budgets[order.supplier_nit] -= order.amount
        order.status = "APROBADA"
        return order