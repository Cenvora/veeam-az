from enum import Enum


class ProtectedDataBackupTierNullable(str, Enum):
    ALL = "All"
    ARCHIVE = "Archive"
    NONARCHIVE = "NonArchive"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
