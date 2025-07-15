from datetime import datetime
from app.core.value_objects import CurrencyCode, PositiveAmount

class Currency:
    def __init__(self, code: CurrencyCode, name: str):
        if not isinstance(code, CurrencyCode):
            raise ValueError("code must be a CurrencyCode")
        self._code = code
        self._name = name

    @property
    def code(self) -> CurrencyCode:
        return self._code

    @property
    def name(self) -> str:
        return self._name

    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise AttributeError(f"{self.__class__.__name__} is immutable")
        super().__setattr__(name, value)

    def __eq__(self, other):
        if isinstance(other, Currency):
            return self.code == other.code and self.name == other.name
        return False

    def __repr__(self):
        return f"Currency(code={self.code!r}, name={self.name!r})"

class Provider:
    def __init__(self, id: int, name: str, url: str):
        if not isinstance(id, int) or id < 0:
            raise ValueError("id must be a non-negative integer")
        self._id = id
        self._name = name
        self._url = url

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def url(self) -> str:
        return self._url

    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise AttributeError(f"{self.__class__.__name__} is immutable")
        super().__setattr__(name, value)

    def __eq__(self, other):
        if isinstance(other, Provider):
            return self.id == other.id and self.name == other.name and self.url == other.url
        return False

    def __repr__(self):
        return f"Provider(id={self.id!r}, name={self.name!r}, url={self.url!r})"

class Rate:
    def __init__(self, id: int, time: datetime, base: Currency, quote: Currency, value: PositiveAmount, provider: Provider):
        if not isinstance(value, PositiveAmount):
            raise ValueError("value must be a PositiveAmount")
        self._id = id
        self._time = time
        self._base = base
        self._quote = quote
        self._value = value
        self._provider = provider

    @property
    def id(self) -> int:
        return self._id

    @property
    def time(self) -> datetime:
        return self._time

    @property
    def base(self) -> Currency:
        return self._base

    @property
    def quote(self) -> Currency:
        return self._quote

    @property
    def value(self) -> PositiveAmount:
        return self._value

    @property
    def provider(self) -> Provider:
        return self._provider

    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise AttributeError(f"{self.__class__.__name__} is immutable")
        super().__setattr__(name, value)

    def __eq__(self, other):
        if isinstance(other, Rate):
            return (
                self.id == other.id and
                self.time == other.time and
                self.base == other.base and
                self.quote == other.quote and
                self.value == other.value and
                self.provider == other.provider
            )
        return False

    def __repr__(self):
        return (
            f"Rate(id={self.id!r}, time={self.time!r}, base={self.base!r}, "
            f"quote={self.quote!r}, value={self.value!r}, provider={self.provider!r})"
        ) 