from enum import Enum


class DatabaseType(str, Enum):
    MANAGED = "Managed"
    UNKNOWN = "Unknown"
    UNMANAGED = "Unmanaged"

    def __str__(self) -> str:
        return str(self.value)
