from enum import Enum


class ReportPeriod(str, Enum):
    DAY = "Day"
    MONTH = "Month"
    UNKNOWN = "Unknown"
    WEEK = "Week"
    YEAR = "Year"

    def __str__(self) -> str:
        return str(self.value)
