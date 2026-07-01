from enum import Enum


class VerificationNeededResult(str, Enum):
    NOTCONFIGUREDATALL = "NotConfiguredAtAll"
    UNKNOWN = "Unknown"
    VERIFICATIONNEEDED = "VerificationNeeded"

    def __str__(self) -> str:
        return str(self.value)
