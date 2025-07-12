"""
Pytest configuration and fixtures.
"""

import pytest
from app.main import app
from fastapi.testclient import TestClient


@pytest.fixture
def client() -> TestClient:
    """Create a test client for the FastAPI application."""
    return TestClient(app)


@pytest.fixture
def sample_currency_data():
    """Sample currency data for testing."""
    return {
        "USD": {
            "code": "USD",
            "name": "US Dollar",
            "symbol": "$",
            "decimal_places": 2,
        },
        "EUR": {
            "code": "EUR",
            "name": "Euro",
            "symbol": "€",
            "decimal_places": 2,
        },
        "INR": {
            "code": "INR",
            "name": "Indian Rupee",
            "symbol": "₹",
            "decimal_places": 2,
        },
    }


@pytest.fixture
def sample_exchange_rate_data():
    """Sample exchange rate data for testing."""
    return {
        "base": "USD",
        "rates": {
            "EUR": 0.85,
            "INR": 83.17,
            "GBP": 0.73,
        },
        "date": "2024-01-15",
        "timestamp": 1705276800,
    }
