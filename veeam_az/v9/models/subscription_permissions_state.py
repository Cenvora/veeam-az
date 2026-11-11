from enum import Enum


class SubscriptionPermissionsState(str, Enum):
    AVAILABLEALL = "AvailableAll"
    AVAILABLESUBSET = "AvailableSubset"
    INSUFFICIENT = "Insufficient"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
