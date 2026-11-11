from enum import Enum


class AzureAccountPermissionsState(str, Enum):
    ALLPERMISSIONSAVAILABLE = "AllPermissionsAvailable"
    MISSINGPERMISSIONS = "MissingPermissions"
    MISSINGSUBSCRIPTIONS = "MissingSubscriptions"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
