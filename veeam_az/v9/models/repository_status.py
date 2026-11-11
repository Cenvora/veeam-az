from enum import Enum


class RepositoryStatus(str, Enum):
    CREATING = "Creating"
    FAILED = "Failed"
    IMPORTING = "Importing"
    READONLY = "ReadOnly"
    READY = "Ready"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
