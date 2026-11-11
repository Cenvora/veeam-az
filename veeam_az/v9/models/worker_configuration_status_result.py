from enum import Enum


class WorkerConfigurationStatusResult(str, Enum):
    FAILURE = "Failure"
    OK = "Ok"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
