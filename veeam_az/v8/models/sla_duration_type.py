from enum import Enum


class SlaDurationType(str, Enum):
    DAY = "Day"
    HOUR = "Hour"
    MINUTE = "Minute"
    MONTH = "Month"
    WEEK = "Week"
    YEAR = "Year"

    def __str__(self) -> str:
        return str(self.value)
