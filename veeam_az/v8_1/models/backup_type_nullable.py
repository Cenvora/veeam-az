from enum import Enum


class BackupTypeNullable(str, Enum):
    ALLSUBSCRIPTIONS = "AllSubscriptions"
    SELECTEDITEMS = "SelectedItems"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
