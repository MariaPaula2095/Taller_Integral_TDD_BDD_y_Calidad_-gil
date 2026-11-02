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
        self.nit = str(nit)
        self.nombre = nombre
        self.name = nombre
        self.correo = correo
        self.email = correo
        self.estado = estado
        self.status = estado

class SupplierService:
    def __init__(self, repo_ordenes=None):
        self.repo_ordenes = repo_ordenes
        self.proveedores = {}
        self.suppliers = self.proveedores
        self._active_orders = set()

    def _validar_nit(self, nit: str):
        if not nit or len(str(nit).strip()) < 9:
            raise InvalidSupplierException("NIT inválido: debe tener al menos 9 caracteres.")

    def _validar_correo(self, correo: str):
        if not correo or "@" not in correo or "." not in correo.split("@")[-1]:
            raise InvalidSupplierException("Formato de correo inválido.")

    def es_nit_valido(self, nit: str) -> bool:
        return bool(nit and len(str(nit).strip()) >= 9)

    def existe_por_nit(self, nit: str) -> bool:
        return str(nit) in self.proveedores

    def get(self, nit: str):
        return self.proveedores.get(str(nit))

    def register_active_order(self, nit: str):
        """Registra una orden activa para el proveedor."""
        self._active_orders.add(str(nit))

    def create_supplier(self, supplier: Supplier) -> Supplier:
        self._validar_nit(supplier.nit)
        self._validar_correo(supplier.correo)
        
        if not supplier.nombre or not supplier.nombre.strip():
            raise InvalidSupplierException("El nombre del proveedor es obligatorio.")

        if str(supplier.nit) in self.proveedores:
            raise InvalidSupplierException("El NIT ya está registrado.")

        supplier.estado = "ACTIVO"
        supplier.status = "ACTIVO"
        self.proveedores[str(supplier.nit)] = supplier
        return supplier

    def add(self, supplier: Supplier) -> Supplier:
        """Alias para compatibilidad con steps de Behave."""
        return self.create_supplier(supplier)

    def delete_supplier(self, nit: str) -> Supplier:
        nit_str = str(nit)
        if nit_str not in self.proveedores:
            raise InvalidSupplierException("Proveedor no encontrado.")

        # Verificar si tiene órdenes activas (vía mock externo o registro local)
        if (self.repo_ordenes and self.repo_ordenes.has_active_orders(nit_str)) or (nit_str in self._active_orders):
            raise SupplierHasActiveOrdersException("No se puede eliminar un proveedor con órdenes activas.")

        proveedor = self.proveedores[nit_str]
        proveedor.estado = "INACTIVO"
        proveedor.status = "INACTIVO"
        return proveedor

    def delete(self, nit: str) -> Supplier:
        """Alias para compatibilidad con steps de Behave."""
        return self.delete_supplier(nit)