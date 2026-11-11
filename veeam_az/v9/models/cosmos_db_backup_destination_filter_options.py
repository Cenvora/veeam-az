from enum import Enum


class CosmosDbBackupDestinationFilterOptions(str, Enum):
    AZUREBLOB = "AzureBlob"
    MANUALBACKUP = "ManualBackup"

    def __str__(self) -> str:
        return str(self.value)
