from enum import Enum


class JobStatus(str, Enum):
    CANCELED = "Canceled"
    CANCELING = "Canceling"
    ERROR = "Error"
    NEVEREXECUTED = "NeverExecuted"
    PENDING = "Pending"
    RUNNING = "Running"
    RUNNINGWITHERROR = "RunningWithError"
    RUNNINGWITHWARNING = "RunningWithWarning"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
