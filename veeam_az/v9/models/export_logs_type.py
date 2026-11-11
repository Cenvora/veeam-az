from enum import Enum


class ExportLogsType(str, Enum):
    BETWEENDATES = "BetweenDates"
    LASTDAYS = "LastDays"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
