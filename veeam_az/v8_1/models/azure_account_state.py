from enum import Enum


class AzureAccountState(str, Enum):
    CREATED = "Created"
    CREATING = "Creating"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
