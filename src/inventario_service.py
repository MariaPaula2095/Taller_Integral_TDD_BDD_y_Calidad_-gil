"""
Módulo de Inventario
Control de existencias y retiros de stock.
"""

class InsufficientStockException(Exception):
    """Excepción lanzada cuando el retiro supera el stock disponible."""
    pass

class InventoryService:
    def __init__(self):
        self.stock = {}

    def get_stock(self, product_id: str) -> int:
        return self.stock.get(product_id, 0)

    def set_stock(self, product_id: str, quantity: int):
        if quantity < 0:
            raise ValueError("El stock inicial no puede ser negativo.")
        self.stock[product_id] = quantity

    def update_stock(self, product_id: str, quantity: int) -> int:
        stock_actual = self.get_stock(product_id)
        stock_resultante = stock_actual + quantity

        if stock_resultante < 0:
            raise InsufficientStockException(
                f"Stock insuficiente para {product_id}. Actual: {stock_actual}, solicitado retirar: {abs(quantity)}"
            )

        self.stock[product_id] = stock_resultante
        return self.stock[product_id]