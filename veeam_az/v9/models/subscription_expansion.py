from enum import Enum


class SubscriptionExpansion(str, Enum):
    ALL = "All"
    EXPIRINGAZUREACCOUNT = "ExpiringAzureAccount"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
