from enum import Enum


class ImmutabilityState(str, Enum):
    IMMUTABLE = "Immutable"
    MUTABLE = "Mutable"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
