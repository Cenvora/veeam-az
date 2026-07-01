from enum import Enum


class ConfigurationCheckStatus(str, Enum):
    CANCELLED = "Cancelled"
    CANCELLING = "Cancelling"
    FAILED = "Failed"
    RUNNING = "Running"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"
    VERIFICATIONNEEDED = "VerificationNeeded"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
