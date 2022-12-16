from decimal import Decimal

from rest_framework.exceptions import ValidationError


def validate_amount(amount: str) -> int:
    """Validates the provided amount."""
    if not amount:
        raise ValidationError(
            detail={"amount": ["Missing required field."]},
            code="missing_value",
        )

    if not amount.replace(".", "").isdigit():
        raise ValidationError(
            detail={"amount": ["Invalid amount, should be a valid decimal."]},
            code="invalid_type",
        )

    if Decimal(amount) < Decimal(1):
        raise ValidationError(
            detail={"amount": ["Amount must exceed zero."]},
            code="invalid_amount",
        )
    return f"{Decimal(amount):2f}"
