from enum import Enum


class VnetBackupDestination(str, Enum):
    ALL = "All"
    AZUREBLOB = "AzureBlob"
    DATABASE = "Database"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
