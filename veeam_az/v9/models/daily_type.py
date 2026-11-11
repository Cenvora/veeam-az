from enum import Enum


class DailyType(str, Enum):
    EVERYDAY = "Everyday"
    SELECTEDDAYS = "SelectedDays"
    UNKNOWN = "Unknown"
    WEEKDAYS = "WeekDays"

    def __str__(self) -> str:
        return str(self.value)
