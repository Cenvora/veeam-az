from enum import Enum


class StorageAccountExpansion(str, Enum):
    ALL = "All"
    NONE = "None"
    SUBSCRIPTION = "Subscription"

    def __str__(self) -> str:
        return str(self.value)
