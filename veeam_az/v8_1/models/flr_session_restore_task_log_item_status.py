from enum import Enum


class FlrSessionRestoreTaskLogItemStatus(str, Enum):
    CANCELLED = "Cancelled"
    ERROR = "Error"
    PENDING = "Pending"
    RUNNING = "Running"
    STARTING = "Starting"
    SUCCESS = "Success"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
