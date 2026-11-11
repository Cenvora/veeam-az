from enum import Enum


class UserTypeNullable(str, Enum):
    IDENTITYPROVIDER = "IdentityProvider"
    INTERNAL = "Internal"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
