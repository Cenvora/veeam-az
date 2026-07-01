from enum import Enum


class StorageTier(str, Enum):
    ARCHIVE = "Archive"
    COLD = "Cold"
    COOL = "Cool"
    HOT = "Hot"
    INFERRED = "Inferred"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
