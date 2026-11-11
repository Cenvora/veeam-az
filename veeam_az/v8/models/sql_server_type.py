from enum import Enum


class SqlServerType(str, Enum):
    MANAGED = "Managed"
    UNKNOWN = "Unknown"
    UNMANAGED = "Unmanaged"

    def __str__(self) -> str:
        return str(self.value)
