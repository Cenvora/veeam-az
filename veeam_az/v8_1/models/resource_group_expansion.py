from enum import Enum


class ResourceGroupExpansion(str, Enum):
    ALL = "All"
    NONE = "None"
    REGION = "Region"
    SUBSCRIPTION = "Subscription"

    def __str__(self) -> str:
        return str(self.value)
