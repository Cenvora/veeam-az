from enum import Enum


class CosmosBackupDestinationFilterOptions(str, Enum):
    ARCHIVE = "Archive"
    AZUREBLOB = "AzureBlob"
    CONTINUOUSBACKUP = "ContinuousBackup"
    MANUALBACKUP = "ManualBackup"

    def __str__(self) -> str:
        return str(self.value)
