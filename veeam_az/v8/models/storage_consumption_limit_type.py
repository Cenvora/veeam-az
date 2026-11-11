from enum import Enum


class StorageConsumptionLimitType(str, Enum):
    GB = "GB"
    MB = "MB"
    TB = "TB"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
