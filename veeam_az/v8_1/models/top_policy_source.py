from enum import Enum


class TopPolicySource(str, Enum):
    ARCHIVE = "Archive"
    BACKUP = "Backup"
    SNAPSHOT = "Snapshot"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
