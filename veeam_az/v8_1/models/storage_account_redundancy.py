from enum import Enum


class StorageAccountRedundancy(str, Enum):
    GRS = "GRS"
    GZRS = "GZRS"
    LRS = "LRS"
    RAGRS = "RAGRS"
    RAGZRS = "RAGZRS"
    UNKNOWN = "Unknown"
    ZRS = "ZRS"

    def __str__(self) -> str:
        return str(self.value)
