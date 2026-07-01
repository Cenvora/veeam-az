from enum import Enum


class VnetRestorePointExpansion(str, Enum):
    ALL = "All"
    CHANGES = "Changes"
    NONE = "None"
    VBRBACKUP = "VbrBackup"

    def __str__(self) -> str:
        return str(self.value)
