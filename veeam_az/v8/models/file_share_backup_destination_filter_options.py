from enum import Enum


class FileShareBackupDestinationFilterOptions(str, Enum):
    IMPORTEDSNAPSHOT = "ImportedSnapshot"
    MANUALSNAPSHOT = "ManualSnapshot"
    SNAPSHOT = "Snapshot"

    def __str__(self) -> str:
        return str(self.value)
