from enum import Enum


class BackupType(str, Enum):
    ALLSUBSCRIPTIONS = "AllSubscriptions"
    SELECTEDITEMS = "SelectedItems"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
