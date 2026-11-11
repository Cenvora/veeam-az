from enum import Enum


class LicenseType(str, Enum):
    EXTERNALVBR = "ExternalVbr"
    FREE = "Free"
    METEREDBILLING = "MeteredBilling"
    SUBSCRIPTION = "Subscription"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
