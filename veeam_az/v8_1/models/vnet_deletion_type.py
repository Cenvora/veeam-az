from enum import Enum


class VnetDeletionType(str, Enum):
    ALL = "All"
    BACKUP = "Backup"
    BACKUPCOPY = "BackupCopy"

    def __str__(self) -> str:
        return str(self.value)
