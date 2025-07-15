import re

class CurrencyCode:
    _iso_4217_pattern = re.compile(r"^[A-Z]{3}$")

    def __init__(self, value: str):
        if not isinstance(value, str) or not self._iso_4217_pattern.match(value):
            raise ValueError(f"Invalid ISO 4217 currency code: {value!r}")
        self._value = value

    @property
    def value(self) -> str:
        return self._value

    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise AttributeError(f"{self.__class__.__name__} is immutable")
        super().__setattr__(name, value)

    def __eq__(self, other):
        if isinstance(other, CurrencyCode):
            return self.value == other.value
        if isinstance(other, str):
            return self.value == other
        return False

    def __repr__(self):
        return f"CurrencyCode({self.value!r})"

class PositiveAmount:
    def __init__(self, value: float):
        if not isinstance(value, (int, float)) or isinstance(value, bool) or value <= 0:
            raise ValueError(f"PositiveAmount must be a positive number, got: {value!r}")
        self._value = float(value)

    @property
    def value(self) -> float:
        return self._value

    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise AttributeError(f"{self.__class__.__name__} is immutable")
        super().__setattr__(name, value)

    def __eq__(self, other):
        if isinstance(other, PositiveAmount):
            return self.value == other.value
        if isinstance(other, (int, float)):
            return self.value == float(other)
        return False

    def __repr__(self):
        return f"PositiveAmount({self.value!r})" 