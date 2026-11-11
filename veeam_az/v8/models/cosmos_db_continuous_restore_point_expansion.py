from enum import Enum


class CosmosDbContinuousRestorePointExpansion(str, Enum):
    NONE = "None"
    VBRBACKUP = "VbrBackup"

    def __str__(self) -> str:
        return str(self.value)
