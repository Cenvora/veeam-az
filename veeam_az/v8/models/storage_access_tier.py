from enum import Enum


class StorageAccessTier(str, Enum):
    ARCHIVE = "Archive"
    COLD = "Cold"
    COOL = "Cool"
    HOT = "Hot"
    INFERRED = "Inferred"

    def __str__(self) -> str:
        return str(self.value)
