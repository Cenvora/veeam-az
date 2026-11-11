from enum import Enum


class RestorePointType(str, Enum):
    CONTINUOUS = "Continuous"
    FULL = "Full"
    INCREMENTAL = "Incremental"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
