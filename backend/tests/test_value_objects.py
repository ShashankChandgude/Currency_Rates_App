import pytest
from app.core.value_objects import CurrencyCode

# Valid ISO 4217 codes for testing
VALID_CODES = ["USD", "EUR", "INR", "JPY", "GBP"]
INVALID_CODES = ["usd", "US", "123", "EURO", "", None]


def test_currency_code_accepts_valid_iso():
    for code in VALID_CODES:
        cc = CurrencyCode(code)
        assert cc.value == code


def test_currency_code_rejects_invalid_iso():
    for code in INVALID_CODES:
        with pytest.raises(ValueError):
            CurrencyCode(code)


def test_currency_code_is_immutable():
    cc = CurrencyCode("USD")
    with pytest.raises(AttributeError):
        cc.value = "EUR"


def test_positive_amount_accepts_positive_float():
    from app.core.value_objects import PositiveAmount

    for val in [0.01, 1.0, 12345.67]:
        amt = PositiveAmount(val)
        assert amt.value == val


def test_positive_amount_rejects_non_positive():
    from app.core.value_objects import PositiveAmount

    for val in [0, -1, -0.01, None, "abc"]:
        with pytest.raises(ValueError):
            PositiveAmount(val)


def test_positive_amount_is_immutable():
    from app.core.value_objects import PositiveAmount

    amt = PositiveAmount(1.23)
    with pytest.raises(AttributeError):
        amt.value = 2.34
