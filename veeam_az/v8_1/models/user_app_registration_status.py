from enum import Enum


class UserAppRegistrationStatus(str, Enum):
    ALLOWED = "Allowed"
    NOTALLOWED = "NotAllowed"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
