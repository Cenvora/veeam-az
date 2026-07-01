from enum import Enum


class AzureStorageContainerSort(str, Enum):
    IMMUTABILITYENABLEDASC = "ImmutabilityEnabledAsc"
    IMMUTABILITYENABLEDDESC = "ImmutabilityEnabledDesc"
    NAMEASC = "NameAsc"
    NAMEDESC = "NameDesc"

    def __str__(self) -> str:
        return str(self.value)
