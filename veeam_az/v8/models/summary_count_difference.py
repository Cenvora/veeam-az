from enum import Enum


class SummaryCountDifference(str, Enum):
    DECREASED = "Decreased"
    INCREASED = "Increased"
    NOTCHANGED = "NotChanged"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
