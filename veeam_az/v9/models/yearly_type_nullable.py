from enum import Enum


class YearlyTypeNullable(str, Enum):
    FIRST = "First"
    FOURTH = "Fourth"
    LAST = "Last"
    SECOND = "Second"
    SELECTEDDAY = "SelectedDay"
    THIRD = "Third"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
