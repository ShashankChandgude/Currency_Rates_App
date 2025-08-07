from datetime import datetime
from decimal import Decimal
from sqlalchemy import create_engine, select, and_
from sqlalchemy.orm import Session
from app.db.models import Currency, Provider, Rate

# Database connection
DATABASE_URL = "postgresql://currency_user:CuPSQL%402025%23@localhost:5432/currency_app"
engine = create_engine(DATABASE_URL)

# Test data configurations
CURRENCIES = [
    ("USD", "US Dollar"),
    ("EUR", "Euro"),
    ("GBP", "British Pound"),
    ("JPY", "Japanese Yen"),
    ("CAD", "Canadian Dollar"),
    ("AUD", "Australian Dollar"),
    ("CHF", "Swiss Franc")
]

PROVIDERS = [
    ("Alpha Exchange", "https://api.alpha-exchange.com"),
    ("Beta Markets", "https://api.beta-markets.com"),
    ("Gamma Rates", "https://api.gamma-rates.com")
]

# Base rates against USD
BASE_RATES = {
    "EUR": "0.85",
    "GBP": "0.72",
    "JPY": "110.25",
    "CAD": "1.25",
    "AUD": "1.35",
    "CHF": "0.92"
}

def generate_rates(variation: float = 0.0) -> list:
    """Generate rates with optional variation for different providers."""
    rates = []
    variation_decimal = Decimal(str(1 + variation))  # Convert float to Decimal
    for quote, base_value in BASE_RATES.items():
        value = Decimal(base_value) * variation_decimal
        rates.append(("USD", quote, str(round(value, 8))))
    return rates

def clean_database():
    """Remove old test data before seeding."""
    with Session(engine) as session:
        # Delete old rates first (due to foreign key constraints)
        session.query(Rate).delete()
        
        # Delete old providers
        session.query(Provider).delete()
        
        # Delete old currencies
        session.query(Currency).delete()
        
        session.commit()

# ...existing imports...

def seed_database():
    """Seed the database with fresh test data."""
    # Clean existing data first
    clean_database()
    
    with Session(engine) as session:
        # Add currencies
        for code, name in CURRENCIES:
            currency = Currency(code=code, name=name)
            session.add(currency)
        session.commit()

        # Add providers and store their IDs
        provider_ids = {}
        for name, url in PROVIDERS:
            provider = Provider(name=name, url=url)
            session.add(provider)
            session.commit()
            provider_ids[name] = provider.id

        # Generate and add rates for each provider
        for idx, (provider_name, provider_id) in enumerate(provider_ids.items()):
            variation = idx * 0.01  # 0%, 1%, 2% variation
            rates = generate_rates(variation)
            
            # Add base rates
            for base, quote, value in rates:
                rate = Rate(
                    time=datetime.utcnow(),
                    base_code=base,
                    quote_code=quote,
                    value=Decimal(value),
                    provider_id=provider_id
                )
                session.add(rate)
            
            # Add inverse rates
            for base, quote, value in rates:
                inverse_value = str(round(1 / Decimal(value), 8))
                rate = Rate(
                    time=datetime.utcnow(),
                    base_code=quote,
                    quote_code=base,
                    value=Decimal(inverse_value),
                    provider_id=provider_id
                )
                session.add(rate)
            
            session.commit()

if __name__ == "__main__":
    seed_database()