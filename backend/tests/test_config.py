"""
Tests for the application configuration.
"""

import os

from app.core.config import settings


def test_settings_instance():
    """Test that settings instance is created successfully."""
    assert settings is not None
    assert hasattr(settings, "ENVIRONMENT")


def test_environment_default():
    """Test that environment has a default value."""
    expected = os.getenv("ENVIRONMENT", "development")
    assert settings.ENVIRONMENT == expected


def test_debug_default():
    """Test that debug has a default value."""
    assert settings.DEBUG is True


def test_api_v1_str():
    """Test that API_V1_STR is set correctly."""
    assert settings.API_V1_STR == "/api/v1"


def test_project_name():
    """Test that PROJECT_NAME is set correctly."""
    assert settings.PROJECT_NAME == "Currency Converter API"


def test_allowed_hosts_default():
    """Test that ALLOWED_HOSTS has default values."""
    assert isinstance(settings.ALLOWED_HOSTS, list)
    assert "http://localhost:3000" in settings.ALLOWED_HOSTS
    assert "http://localhost:8000" in settings.ALLOWED_HOSTS


def test_database_url_default():
    """Test that DATABASE_URL has a default value."""
    assert settings.DATABASE_URL is not None
    assert "postgresql://" in settings.DATABASE_URL


def test_redis_url_default():
    """Test that REDIS_URL has a default value."""
    assert settings.REDIS_URL == "redis://localhost:6379"


def test_log_level_default():
    """Test that LOG_LEVEL has a default value."""
    assert settings.LOG_LEVEL == "INFO"


def test_exchange_rate_api_url_default():
    """Test that EXCHANGE_RATE_API_URL has a default value."""
    assert settings.EXCHANGE_RATE_API_URL == "https://api.exchangerate.host"


def test_rate_limit_default():
    """Test that RATE_LIMIT_PER_MINUTE has a default value."""
    assert settings.RATE_LIMIT_PER_MINUTE == 60


def test_cache_ttl_defaults():
    """Test that cache TTL settings have default values."""
    assert settings.CACHE_TTL_SECONDS == 30
    assert settings.HISTORICAL_CACHE_TTL_DAYS == 7
