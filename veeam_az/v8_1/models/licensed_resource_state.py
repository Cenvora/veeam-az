from enum import Enum


class LicensedResourceState(str, Enum):
    EXCEEDED = "Exceeded"
    GRACED = "Graced"
    LICENSED = "Licensed"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
