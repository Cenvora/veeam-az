from enum import Enum


class ValidationMessageSeverity(str, Enum):
    ERROR = "Error"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
