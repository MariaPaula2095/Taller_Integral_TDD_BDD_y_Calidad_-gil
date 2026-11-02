import sys
from pathlib import Path

# Permite importar desde src
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from behave import given, when, then
from src.orden_service import OrderService

@given('supplier "{nit}" has a budget of {amount:d}')
def step_set_budget(context, nit, amount):
    if not hasattr(context, 'order_service'):
        context.order_service = OrderService()
    context.order_service.assign_budget(nit, amount)

@given('a purchase order "{order_id}" for supplier "{nit}" with amount {amount:d}')
def step_create_order(context, order_id, nit, amount):
    context.order_service.create_order(order_id, nit, amount)

@when('I approve the order "{order_id}"')
def step_approve_order(context, order_id):
    context.order_service.approve_order(order_id)

@then('the order "{order_id}" has status "{status}"')
def step_check_status(context, order_id, status):
    order = context.order_service.orders.get(order_id)
    assert order is not None, f"Order {order_id} not found"
    assert order.status == status, f"Expected {status}, got {order.status}"

@then('supplier "{nit}" has a remaining budget of {amount:d}')
def step_check_budget(context, nit, amount):
    budget = context.order_service.budgets.get(nit, 0)
    assert budget == amount, f"Expected {amount}, got {budget}"