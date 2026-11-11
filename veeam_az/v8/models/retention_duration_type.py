from enum import Enum


class RetentionDurationType(str, Enum):
    DAYS = "Days"
    MONTHS = "Months"
    UNKNOWN = "Unknown"
    YEARS = "Years"

    def __str__(self) -> str:
        return str(self.value)
