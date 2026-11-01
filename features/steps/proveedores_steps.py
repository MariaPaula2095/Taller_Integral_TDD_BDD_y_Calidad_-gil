"""Behave steps for features/proveedores.feature.

IMPORTANT: these steps use Person 1's code (src/proveedor_service.py).
Everything that depends on Person 1's names lives in the ADAPTER section.
If Person 1 uses different names, only that section changes and the
.feature scenarios stay untouched.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from behave import given, then, when  # noqa: E402

from src.proveedor_service import Supplier, SupplierService  # noqa: E402


# ======================= ADAPTER (agree names with Person 1) =======================
def create_service():
    return SupplierService()


def register(service, nit, name, email):
    service.add(Supplier(nit, name, email))


def exists(service, nit):
    try:
        return service.get(nit) is not None
    except Exception:
        return False


def status_of(service, nit):
    return service.get(nit).status


def mark_active_order(service, nit):
    service.register_active_order(nit)


def delete(service, nit):
    service.delete(nit)


# ===================================================================================
DEFAULT_NAME = "Test Supplier"
DEFAULT_EMAIL = "contact@supplier.co"


def attempt(context, action):
    """Run the action and store any error so it can be checked later."""
    context.supplier_error = None
    try:
        action()
    except Exception as error:  # noqa: BLE001 - we check the rejection, not its type
        context.supplier_error = error


@given("an empty supplier service")
def step_empty_supplier_service(context):
    context.suppliers = create_service()
    context.supplier_error = None


@given('a registered supplier with NIT "{nit}"')
def step_registered_supplier(context, nit):
    register(context.suppliers, nit, DEFAULT_NAME, DEFAULT_EMAIL)


@given('supplier "{nit}" has an active order')
def step_active_order(context, nit):
    mark_active_order(context.suppliers, nit)


@when('I register a supplier with NIT "{nit}", name "{name}" and email "{email}"')
def step_register_supplier(context, nit, name, email):
    register(context.suppliers, nit, name, email)


@when('I try to register a supplier with NIT "{nit}" and email "{email}"')
def step_try_register_supplier(context, nit, email):
    attempt(
        context,
        lambda: register(context.suppliers, nit, DEFAULT_NAME, email),
    )


@when('I delete supplier "{nit}"')
def step_delete_supplier(context, nit):
    delete(context.suppliers, nit)


@when('I try to delete supplier "{nit}"')
def step_try_delete_supplier(context, nit):
    attempt(context, lambda: delete(context.suppliers, nit))


@then('supplier "{nit}" exists with status "{status}"')
def step_supplier_exists_with_status(context, nit, status):
    assert exists(context.suppliers, nit), f"Supplier {nit} does not exist"
    assert status_of(context.suppliers, nit) == status


@then('supplier "{nit}" does not exist')
def step_supplier_does_not_exist(context, nit):
    assert not exists(context.suppliers, nit), f"Supplier {nit} exists"


@then("the system rejects the operation")
def step_system_rejects(context):
    assert context.supplier_error is not None, "A rejection was expected"
