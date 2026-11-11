from enum import Enum


class BackupDestinationFilterOptions(str, Enum):
    ARCHIVE = "Archive"
    AZUREBLOB = "AzureBlob"
    MANUALSNAPSHOT = "ManualSnapshot"
    SNAPSHOT = "Snapshot"

    def __str__(self) -> str:
        return str(self.value)
