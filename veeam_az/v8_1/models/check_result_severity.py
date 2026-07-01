from enum import Enum


class CheckResultSeverity(str, Enum):
    ERROR = "Error"
    SUCCESS = "Success"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
