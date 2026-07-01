from enum import Enum


class StorageAccountPerformance(str, Enum):
    PREMIUM = "Premium"
    STANDARD = "Standard"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
