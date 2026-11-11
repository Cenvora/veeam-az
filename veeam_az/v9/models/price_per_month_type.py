from enum import Enum


class PricePerMonthType(str, Enum):
    NOTAPPLICABLE = "NotApplicable"
    UNKNOWN = "Unknown"
    VALID = "Valid"

    def __str__(self) -> str:
        return str(self.value)
