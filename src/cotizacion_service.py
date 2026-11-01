"""Quotation service.

Business rule: a quotation can only be registered against a quotation request
whose status is "ABIERTA" (open), and its amount must be a number greater than
zero. A registered quotation is created with status "RECIBIDA" (received).
"""

from decimal import Decimal

STATUS_OPEN = "ABIERTA"
STATUS_CLOSED = "CERRADA"
STATUS_RECEIVED = "RECIBIDA"


class InvalidQuotationError(ValueError):
    """Raised when a quotation breaks a business rule."""


class QuotationRequest:
    def __init__(self, code, description="", status=STATUS_OPEN):
        self.code = code
        self.description = description
        self.status = status


class Quotation:
    def __init__(self, request, supplier_nit, amount):
        self.request = request
        self.supplier_nit = supplier_nit
        self.amount = amount
        self.status = STATUS_RECEIVED


class QuotationService:
    def __init__(self):
        self._quotations = []

    def register(self, request, supplier_nit, amount):
        """Register a quotation and return it with status RECIBIDA."""
        if request.status != STATUS_OPEN:
            raise InvalidQuotationError(
                f"Request {request.code} is not open (status: {request.status})"
            )
        if not str(supplier_nit or "").strip():
            raise InvalidQuotationError("Supplier NIT is required")
        if isinstance(amount, bool) or not isinstance(amount, (int, float, Decimal)):
            raise InvalidQuotationError("Amount must be a number")
        if amount <= 0:
            raise InvalidQuotationError("Amount must be greater than zero")

        quotation = Quotation(request, supplier_nit, amount)
        self._quotations.append(quotation)
        return quotation

    def list_by_request(self, request_code):
        return [q for q in self._quotations if q.request.code == request_code]
