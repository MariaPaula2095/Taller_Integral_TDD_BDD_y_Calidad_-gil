import sys
from pathlib import Path

# Allows `from src...` when running `behave` from the project root.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from behave import given, then, when  # noqa: E402

from src.cotizacion_service import (  # noqa: E402
    InvalidQuotationError,
    QuotationRequest,
    QuotationService,
)


@given("an empty quotation service")
def step_empty_quotation_service(context):
    context.quotations = QuotationService()
    context.quotation_requests = {}
    context.quotation = None
    context.quotation_error = None


@given('a quotation request "{code}" with status "{status}"')
def step_quotation_request(context, code, status):
    context.quotation_requests[code] = QuotationRequest(code, status=status)
    context.current_request = context.quotation_requests[code]


@when('supplier "{nit}" registers a quotation for {amount:d}')
def step_register_quotation(context, nit, amount):
    context.quotation = context.quotations.register(
        context.current_request, nit, amount
    )


@when('supplier "{nit}" tries to register a quotation for {amount:d}')
def step_try_register_quotation(context, nit, amount):
    try:
        context.quotations.register(context.current_request, nit, amount)
    except InvalidQuotationError as error:
        context.quotation_error = error


@then('the quotation has status "{status}"')
def step_quotation_status(context, status):
    assert context.quotation is not None, "No quotation was registered"
    assert context.quotation.status == status, context.quotation.status


@then('the quotation is rejected with a message containing "{text}"')
def step_quotation_rejected(context, text):
    assert context.quotation_error is not None, "A rejection was expected"
    assert text in str(context.quotation_error), str(context.quotation_error)


@then('request "{code}" has {count:d} registered quotation')
@then('request "{code}" has {count:d} registered quotations')
def step_quotation_count(context, code, count):
    registered = context.quotations.list_by_request(code)
    assert len(registered) == count, f"There are {len(registered)}"
