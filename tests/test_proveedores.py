import unittest
from unittest.mock import MagicMock
from src.proveedor_service import (
    Supplier,
    SupplierService,
    InvalidSupplierException,
    SupplierHasActiveOrdersException
)
from src.inventario_service import (
    InventoryService,
    InsufficientStockException
)

class TestSupplierService(unittest.TestCase):

    def setUp(self):
        self.service = SupplierService()

    # --- Validaciones de Creación (Ejercicio práctico 2) ---

    def test_crear_proveedor_valido(self):
        proveedor = Supplier("900123456", "ACME S.A.S.", "contacto@acme.com")
        creado = self.service.create_supplier(proveedor)
        self.assertEqual(creado.estado, "ACTIVO")
        self.assertTrue(self.service.existe_por_nit("900123456"))

    def test_no_deberia_crear_proveedor_con_nit_invalido(self):
        proveedor = Supplier("123", "ACME S.A.S.", "contacto@acme.com")
        with self.assertRaises(InvalidSupplierException):
            self.service.create_supplier(proveedor)

    def test_no_deberia_crear_proveedor_con_correo_invalido(self):
        proveedor = Supplier("900123456", "ACME S.A.S.", "correo-sin-arroba.com")
        with self.assertRaises(InvalidSupplierException):
            self.service.create_supplier(proveedor)

    def test_no_deberia_crear_proveedor_duplicado(self):
        p1 = Supplier("900123456", "ACME", "acme@test.com")
        p2 = Supplier("900123456", "ACME COPIA", "copia@test.com")
        self.service.create_supplier(p1)
        with self.assertRaises(InvalidSupplierException):
            self.service.create_supplier(p2)

    # --- Taller 1: Eliminación y Órdenes Activas ---

    def test_no_deberia_eliminar_con_ordenes_activas(self):
        repo_ordenes = MagicMock()
        repo_ordenes.has_active_orders.return_value = True

        service = SupplierService(repo_ordenes=repo_ordenes)
        service.create_supplier(Supplier("900123456", "ACME", "contacto@acme.com"))

        with self.assertRaises(SupplierHasActiveOrdersException):
            service.delete_supplier("900123456")

    def test_deberia_desactivar_proveedor_sin_ordenes_activas(self):
        repo_ordenes = MagicMock()
        repo_ordenes.has_active_orders.return_value = False

        service = SupplierService(repo_ordenes=repo_ordenes)
        service.create_supplier(Supplier("900123456", "ACME", "contacto@acme.com"))

        proveedor_eliminado = service.delete_supplier("900123456")
        self.assertEqual(proveedor_eliminado.estado, "INACTIVO")


class TestInventoryTDD(unittest.TestCase):

    def setUp(self):
        self.inventario = InventoryService()

    # --- Ejercicio práctico 1 (TDD update_stock) ---

    def test_update_stock_agrega_unidades_correctamente(self):
        self.inventario.set_stock("PROD-001", 10)
        nuevo_stock = self.inventario.update_stock("PROD-001", 5)
        self.assertEqual(nuevo_stock, 15)

    def test_update_stock_permite_retiro_si_hay_suficiente(self):
        self.inventario.set_stock("PROD-001", 10)
        nuevo_stock = self.inventario.update_stock("PROD-001", -4)
        self.assertEqual(nuevo_stock, 6)

    def test_update_stock_lanza_excepcion_si_stock_insuficiente(self):
        self.inventario.set_stock("PROD-001", 3)
        with self.assertRaises(InsufficientStockException):
            self.inventario.update_stock("PROD-001", -5)


if __name__ == "__main__":
    unittest.main()