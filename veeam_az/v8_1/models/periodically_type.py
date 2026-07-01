from enum import Enum


class PeriodicallyType(str, Enum):
    CONTINUOUSLY = "Continuously"
    HOURS = "Hours"
    MINUTES = "Minutes"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
