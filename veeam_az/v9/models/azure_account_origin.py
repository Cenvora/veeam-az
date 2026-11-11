from enum import Enum


class AzureAccountOrigin(str, Enum):
    DEVICE_AUTHENTICATION = "Device Authentication"
    IMPORTED_CERTIFICATE = "Imported Certificate"
    IMPORTED_SECRET = "Imported Secret"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
