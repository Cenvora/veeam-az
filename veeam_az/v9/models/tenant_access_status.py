from enum import Enum


class TenantAccessStatus(str, Enum):
    AVAILABLE = "Available"
    GUESTACCOUNTDISABLED = "GuestAccountDisabled"
    MFAREQUIRED = "MfaRequired"
    TOKENACQUISITIONERROR = "TokenAcquisitionError"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
