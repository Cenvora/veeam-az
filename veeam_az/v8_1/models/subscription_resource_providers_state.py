from enum import Enum


class SubscriptionResourceProvidersState(str, Enum):
    AVAILABLEALL = "AvailableAll"
    INSUFFICIENT = "Insufficient"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
