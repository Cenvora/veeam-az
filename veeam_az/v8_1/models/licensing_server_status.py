from enum import Enum


class LicensingServerStatus(str, Enum):
    AVAILABLE = "Available"
    NOTAVAILABLE = "NotAvailable"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
