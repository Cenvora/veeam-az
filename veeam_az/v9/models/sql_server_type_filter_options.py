from enum import Enum


class SqlServerTypeFilterOptions(str, Enum):
    ALL = "All"
    MANAGED = "Managed"
    UNMANAGED = "Unmanaged"

    def __str__(self) -> str:
        return str(self.value)
