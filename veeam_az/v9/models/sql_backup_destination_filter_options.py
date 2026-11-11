from enum import Enum


class SqlBackupDestinationFilterOptions(str, Enum):
    ARCHIVE = "Archive"
    AZUREBLOB = "AzureBlob"
    MANUALBACKUP = "ManualBackup"

    def __str__(self) -> str:
        return str(self.value)
