from enum import Enum


class WorkerWaitTimeState(str, Enum):
    EXCEEDED = "Exceeded"
    OPTIMIZED = "Optimized"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
