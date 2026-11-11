from enum import Enum


class FrequencyType(str, Enum):
    DAILY = "Daily"
    MONTHLY = "Monthly"
    PERIODICALLY = "Periodically"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
