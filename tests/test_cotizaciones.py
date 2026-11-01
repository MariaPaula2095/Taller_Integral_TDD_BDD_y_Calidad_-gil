import pytest

from src.cotizacion_service import (
    InvalidQuotationError,
    QuotationRequest,
    QuotationService,
)

NIT = "900123456"


@pytest.fixture
def service():
    return QuotationService()


@pytest.fixture
def open_request():
    return QuotationRequest("REQ-001", "Screws", status="ABIERTA")


# ---------- Valid amounts ----------
@pytest.mark.parametrize("amount", [1, 0.01, 150000, 2500000.75])
def test_positive_amount_is_accepted(service, open_request, amount):
    quotation = service.register(open_request, NIT, amount)
    assert quotation.amount == amount


@pytest.mark.parametrize("amount", [1, 150000])
def test_registered_quotation_has_status_received(service, open_request, amount):
    quotation = service.register(open_request, NIT, amount)
    assert quotation.status == "RECIBIDA"


# ---------- Zero and negative amounts ----------
@pytest.mark.parametrize(
    "amount",
    [0, 0.0, -1, -250.5, -1000000],
    ids=["zero", "decimal-zero", "minus-one", "negative-decimal", "large-negative"],
)
def test_zero_or_negative_amount_is_rejected(service, open_request, amount):
    with pytest.raises(InvalidQuotationError, match="greater than zero"):
        service.register(open_request, NIT, amount)


@pytest.mark.parametrize("amount", [None, "100", "abc", True])
def test_non_numeric_amount_is_rejected(service, open_request, amount):
    with pytest.raises(InvalidQuotationError, match="number"):
        service.register(open_request, NIT, amount)


# ---------- Request and supplier rules ----------
@pytest.mark.parametrize("status", ["CERRADA", "CANCELADA", "RECIBIDA"])
def test_only_open_requests_can_be_quoted(service, status):
    request = QuotationRequest("REQ-002", "Nuts", status=status)
    with pytest.raises(InvalidQuotationError, match="not open"):
        service.register(request, NIT, 1000)


@pytest.mark.parametrize("nit", ["", "   ", None])
def test_empty_supplier_nit_is_rejected(service, open_request, nit):
    with pytest.raises(InvalidQuotationError, match="NIT"):
        service.register(open_request, nit, 1000)


def test_rejected_quotation_is_not_stored(service, open_request):
    with pytest.raises(InvalidQuotationError):
        service.register(open_request, NIT, -5)
    assert service.list_by_request("REQ-001") == []


def test_list_by_request_returns_only_that_requests_quotations(service):
    request_1 = QuotationRequest("REQ-001")
    request_2 = QuotationRequest("REQ-002")
    service.register(request_1, NIT, 1000)
    service.register(request_1, "800111222", 900)
    service.register(request_2, NIT, 500)
    assert len(service.list_by_request("REQ-001")) == 2
    assert len(service.list_by_request("REQ-002")) == 1
