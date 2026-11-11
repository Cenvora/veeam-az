from enum import Enum


class FileShareRestorePointExpansion(str, Enum):
    ALL = "All"
    NONE = "None"
    VBRBACKUP = "VbrBackup"

    def __str__(self) -> str:
        return str(self.value)
