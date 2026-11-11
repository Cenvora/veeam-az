from enum import Enum


class ProtectionStatus(str, Enum):
    PROTECTED = "Protected"
    UNKNOWN = "Unknown"
    UNPROTECTED = "Unprotected"

    def __str__(self) -> str:
        return str(self.value)
