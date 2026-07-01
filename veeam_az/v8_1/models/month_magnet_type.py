from enum import Enum


class MonthMagnetType(str, Enum):
    FIRSTDAY = "FirstDay"
    LASTDAY = "LastDay"

    def __str__(self) -> str:
        return str(self.value)
