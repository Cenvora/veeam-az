from enum import Enum


class VnetRestorePointRestoreType(str, Enum):
    SELECTEDITEMS = "SelectedItems"
    TODIFFERENT = "ToDifferent"
    TOORIGINAL = "ToOriginal"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
