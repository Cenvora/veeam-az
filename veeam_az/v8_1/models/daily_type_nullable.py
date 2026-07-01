from enum import Enum


class DailyTypeNullable(str, Enum):
    EVERYDAY = "Everyday"
    SELECTEDDAYS = "SelectedDays"
    UNKNOWN = "Unknown"
    WEEKDAYS = "WeekDays"

    def __str__(self) -> str:
        return str(self.value)
