import pytest
from datetime import datetime
from app.core.value_objects import CurrencyCode, PositiveAmount
from app.core.entities import Currency, Provider, Rate

# --- Currency Entity ---
def test_currency_creation_valid():
    c = Currency(code=CurrencyCode("USD"), name="US Dollar")
    assert c.code == CurrencyCode("USD")
    assert c.name == "US Dollar"

def test_currency_creation_invalid_code():
    with pytest.raises(ValueError):
        Currency(code=CurrencyCode("usd"), name="US Dollar")

def test_currency_immutable():
    c = Currency(code=CurrencyCode("USD"), name="US Dollar")
    with pytest.raises(AttributeError):
        c.name = "Euro"

# --- Provider Entity ---
def test_provider_creation_valid():
    p = Provider(id=1, name="TestProvider", url="https://api.example.com")
    assert p.id == 1
    assert p.name == "TestProvider"
    assert p.url == "https://api.example.com"

def test_provider_creation_invalid_id():
    with pytest.raises(ValueError):
        Provider(id=-1, name="TestProvider", url="https://api.example.com")

def test_provider_immutable():
    p = Provider(id=1, name="TestProvider", url="https://api.example.com")
    with pytest.raises(AttributeError):
        p.name = "Other"

# --- Rate Entity ---
def test_rate_creation_valid():
    base = Currency(code=CurrencyCode("USD"), name="US Dollar")
    quote = Currency(code=CurrencyCode("EUR"), name="Euro")
    provider = Provider(id=1, name="TestProvider", url="https://api.example.com")
    rate = Rate(
        id=1,
        time=datetime(2024, 1, 1, 12, 0, 0),
        base=base,
        quote=quote,
        value=PositiveAmount(1.23),
        provider=provider
    )
    assert rate.base == base
    assert rate.quote == quote
    assert rate.value == PositiveAmount(1.23)
    assert rate.provider == provider

def test_rate_creation_invalid_amount():
    base = Currency(code=CurrencyCode("USD"), name="US Dollar")
    quote = Currency(code=CurrencyCode("EUR"), name="Euro")
    provider = Provider(id=1, name="TestProvider", url="https://api.example.com")
    with pytest.raises(ValueError):
        Rate(
            id=1,
            time=datetime(2024, 1, 1, 12, 0, 0),
            base=base,
            quote=quote,
            value=PositiveAmount(-1),
            provider=provider
        )

def test_rate_immutable():
    base = Currency(code=CurrencyCode("USD"), name="US Dollar")
    quote = Currency(code=CurrencyCode("EUR"), name="Euro")
    provider = Provider(id=1, name="TestProvider", url="https://api.example.com")
    rate = Rate(
        id=1,
        time=datetime(2024, 1, 1, 12, 0, 0),
        base=base,
        quote=quote,
        value=PositiveAmount(1.23),
        provider=provider
    )
    with pytest.raises(AttributeError):
        rate.value = PositiveAmount(2.0) 