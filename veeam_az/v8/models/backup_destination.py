from enum import Enum


class BackupDestination(str, Enum):
    AZUREBLOB = "AzureBlob"
    MANUALSNAPSHOT = "ManualSnapshot"
    SNAPSHOT = "Snapshot"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
