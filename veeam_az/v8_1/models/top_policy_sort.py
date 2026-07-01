from enum import Enum


class TopPolicySort(str, Enum):
    PERCENTAGEASC = "PercentageAsc"
    PERCENTAGEDESC = "PercentageDesc"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
