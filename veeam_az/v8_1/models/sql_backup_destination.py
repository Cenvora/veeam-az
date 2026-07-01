from enum import Enum


class SqlBackupDestination(str, Enum):
    AZUREBLOB = "AzureBlob"
    MANUALBACKUP = "ManualBackup"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
