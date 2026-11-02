import unittest
from src.inventario_service import InventoryService, InsufficientStockException

class TestInventorySubtest(unittest.TestCase):

    def setUp(self):
        self.inventario = InventoryService()

    def test_retiro_inventario_con_subtest(self):
        # Evaluamos los 3 casos del taller
        casos = [
            # product_id, stock_inicial, cantidad_retiro, stock_esperado, debe_lanzar_error
            ("PROD-001", 10, -3, 7, False),
            ("PROD-002", 5, -5, 0, False),
            ("PROD-003", 2, -5, 2, True),
        ]
        
        for product_id, stock_inicial, retiro, stock_esperado, error in casos:
            with self.subTest(product=product_id, withdraw=retiro):
                self.inventario.set_stock(product_id, stock_inicial)
                
                if error:
                    with self.assertRaises(InsufficientStockException):
                        self.inventario.update_stock(product_id, retiro)
                    self.assertEqual(self.inventario.get_stock(product_id), stock_esperado)
                else:
                    stock_final = self.inventario.update_stock(product_id, retiro)
                    self.assertEqual(stock_final, stock_esperado)

if __name__ == "__main__":
    unittest.main()