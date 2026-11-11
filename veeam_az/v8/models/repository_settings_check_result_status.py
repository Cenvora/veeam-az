from enum import Enum


class RepositorySettingsCheckResultStatus(str, Enum):
    CONTAINERDOESNOTEXIST = "ContainerDoesNotExist"
    DOESNOTEXIST = "DoesNotExist"
    INCORRECTFORMAT = "IncorrectFormat"
    NOTREADY = "NotReady"
    STORAGEACCOUNTDOESNOTEXIST = "StorageAccountDoesNotExist"
    UNKNOWN = "Unknown"
    VALID = "Valid"

    def __str__(self) -> str:
        return str(self.value)
