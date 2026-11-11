from enum import Enum


class FlrSessionRestoreTaskStatus(str, Enum):
    CANCELLED = "Cancelled"
    FAILED = "Failed"
    RUNNING = "Running"
    SUCCESS = "Success"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
