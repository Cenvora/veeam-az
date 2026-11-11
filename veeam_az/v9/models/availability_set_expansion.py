from enum import Enum


class AvailabilitySetExpansion(str, Enum):
    ALL = "All"
    NONE = "None"
    RESOURCEGROUP = "ResourceGroup"

    def __str__(self) -> str:
        return str(self.value)
