"""
Módulo de Gestión de Proveedores
Implementa reglas de validación y ciclo de vida del proveedor.
"""

class InvalidSupplierException(Exception):
    """Excepción lanzada cuando los datos del proveedor no cumplen las reglas de negocio."""
    pass

class SupplierHasActiveOrdersException(Exception):
    """Excepción lanzada al intentar eliminar un proveedor con órdenes activas."""
    pass

class Supplier:
    def __init__(self, nit: str, nombre: str, correo: str, estado: str = "ACTIVO"):
        self.nit = nit
        self.nombre = nombre
        self.correo = correo
        self.estado = estado

class SupplierService:
    def __init__(self, repo_ordenes=None):
        self.repo_ordenes = repo_ordenes
        self.proveedores = {}

    def _validar_nit(self, nit: str):
        if not nit or len(str(nit).strip()) < 9:
            raise InvalidSupplierException("NIT inválido: debe tener al menos 9 caracteres.")

    def _validar_correo(self, correo: str):
        if not correo or "@" not in correo or "." not in correo.split("@")[-1]:
            raise InvalidSupplierException("Formato de correo inválido.")

    def es_nit_valido(self, nit: str) -> bool:
        return bool(nit and len(str(nit).strip()) >= 9)

    def existe_por_nit(self, nit: str) -> bool:
        return nit in self.proveedores

    def create_supplier(self, supplier: Supplier) -> Supplier:
        self._validar_nit(supplier.nit)
        self._validar_correo(supplier.correo)
        
        if not supplier.nombre or not supplier.nombre.strip():
            raise InvalidSupplierException("El nombre del proveedor es obligatorio.")

        if supplier.nit in self.proveedores:
            raise InvalidSupplierException("El NIT ya está registrado.")

        supplier.estado = "ACTIVO"
        self.proveedores[supplier.nit] = supplier
        return supplier

    def delete_supplier(self, nit: str) -> Supplier:
        if nit not in self.proveedores:
            raise InvalidSupplierException("Proveedor no encontrado.")

        # Verificar si tiene órdenes activas mediante el repositorio simulado (Mock)
        if self.repo_ordenes and self.repo_ordenes.has_active_orders(nit):
            raise SupplierHasActiveOrdersException("No se puede eliminar un proveedor con órdenes activas.")

        # Eliminación lógica: cambia a INACTIVO
        proveedor = self.proveedores[nit]
        proveedor.estado = "INACTIVO"
        return proveedor