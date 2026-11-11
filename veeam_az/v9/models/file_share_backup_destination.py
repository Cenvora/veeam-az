from enum import Enum


class FileShareBackupDestination(str, Enum):
    IMPORTEDSNAPSHOT = "ImportedSnapshot"
    MANUALSNAPSHOT = "ManualSnapshot"
    SNAPSHOT = "Snapshot"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
