"""
Application configuration using Pydantic settings.
"""

from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    # Environment
    ENVIRONMENT: str = Field(default="development", env="ENVIRONMENT")
    DEBUG: bool = Field(default=True, env="DEBUG")

    # API
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Currency Converter API"

    # CORS
    ALLOWED_HOSTS: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:8000"],
        env="ALLOWED_HOSTS",
    )

    # Database
    DATABASE_URL: str = Field(
        default=(
            "postgresql://currency_user:currency_password@localhost:"
            "5432/currency_app"
        ),
        env="DATABASE_URL",
    )

    # Redis
    REDIS_URL: str = Field(
        default="redis://localhost:6379",
        env="REDIS_URL",
    )

    # Logging
    LOG_LEVEL: str = Field(default="INFO", env="LOG_LEVEL")

    # External APIs
    EXCHANGE_RATE_API_URL: str = Field(
        default="https://api.exchangerate.host",
        env="EXCHANGE_RATE_API_URL",
    )

    # Rate limiting
    RATE_LIMIT_PER_MINUTE: int = Field(default=60, env="RATE_LIMIT_PER_MINUTE")

    # Cache settings
    CACHE_TTL_SECONDS: int = Field(
        default=30,
        env="CACHE_TTL_SECONDS",
    )
    HISTORICAL_CACHE_TTL_DAYS: int = Field(
        default=7,
        env="HISTORICAL_CACHE_TTL_DAYS",
    )

    class Config:
        env_file = ".env"
        case_sensitive = True


# Create settings instance
settings = Settings()
