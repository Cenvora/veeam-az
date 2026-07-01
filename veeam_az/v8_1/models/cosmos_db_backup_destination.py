from enum import Enum


class CosmosDbBackupDestination(str, Enum):
    AZUREBLOB = "AzureBlob"
    MANUALBACKUP = "ManualBackup"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
